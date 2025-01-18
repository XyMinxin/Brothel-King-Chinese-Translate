#### BK TRAITS ####
## Labels are used instead of Functions to make sure we are using global variables


## How to add a new Trait to the game: Use the 'register_trait(trait, type)' function below at init or later.
## - init_traits runs at game start, before mods are initiated
## - If you want all newly-generated girls to have a chance to get a Trait, set its public attribute to 'True' (default) --> Trait(..., public=True)
## - If you only want a specific girl to have the trait, set its public attribute to 'False' --> Trait(..., public=False), then use code or _BK.ini to set-up the trait
## - In all cases, make sure to use register_trait() to update the Trait dictionary and avoid trait lookup problems
## - Note that if you want to include a custom made Trait as part of a _BK.ini file, the Trait() must be registered separately in a .rpy file

define renamed_traits = {"Good tits" : "Firm tits"} # For backwards compatibility

init -1 python:
    traits_initiated = False
    custom_traits = {"gold" : [], "pos" : [], "neg" : []}

    def register_trait(trait, type="pos"): # Where trait is a Trait object. Type can be "pos", "neg" or "gold".
        # WARNING: Registering a trait with the same name as an existing one will override it.

        if not isinstance(trait, Trait):
            raise AssertionError("Register trait failed: %s is not a valid Trait object." % trait)

        if type not in ("gold", "pos", "neg"):
            raise AssertionError("Register trait failed: %s is not a valid type (only 'gold', 'pos' and 'neg' are accepted values)." % type)

        custom_traits[type].append(trait)

        if traits_initiated: # Updates trait lists and dictionaries if they have already been generated
            if type == "gold":
                target_list = gold_traits
            elif type == "pos":
                target_list = pos_traits
            elif type == "neg":
                target_list = neg_traits
            
            for t in target_list:
                if t.name == trait.name:
                    target_list.remove(t)
                    break

            target_list.append(trait)
            trait_dict[trait.name] = trait


    def deregister_trait(trait_name, type="pos"): # Where trait_name is a string (not the same as register_trait!). Type can be "pos", "neg" or "gold".

        if not is_string(trait_name):
            raise AssertionError("Deregister trait failed: %s is not a string." % trait_name)

        if type not in ("gold", "pos", "neg"):
            raise AssertionError("Register trait failed: %s is not a valid type (only 'gold', 'pos' and 'neg' are accepted values)." % type)

        custom_traits[type] = [t for t in custom_traits[type] if t.name != trait_name]

        if traits_initiated: # Updates trait lists and dictionaries if they have already been generated
            if type == "gold":
                target_list = gold_traits
            elif type == "pos":
                target_list = pos_traits
            elif type == "neg":
                target_list = neg_traits
            
            target_list = [t for t in target_list if t.name != trait_name]

            del trait_dict[trait_name]

    def count_archetypes(): # Debugging - For balance
        d = {arc : 0 for arc in archetype_list}

        for trait in gold_traits + pos_traits + neg_traits:
            if trait.archetype:
                d[trait.archetype] += 1

        return d




label init_traits():

    python:
        traits_initiated = True

        ## GOLD TRAITS (for unique girls) ##

        gold_traits = [
                        Trait(_("Naughty"), verb ="be", eff1 = Effect("boost", "tip", 0.1), eff2 = Effect("personality", "pervert"), archetype="The Slut"),
                        Trait(_("Fascinating"), verb ="be", eff1 = Effect("change", "job customer capacity", 2), archetype="The Courtesan"),
                        Trait(_("Lust"), verb ="have", eff1=Effect("change", "whore customer capacity", 1), archetype="The Slut"),
                        Trait(_("Warrior"), verb ="be a", eff1=Effect("change", "defense", 3), eff2=Effect("personality", "rebel"), archetype="The Bride"),
                        Trait(_("Skilled tongue"), verb ="have a", eff1=Effect("increase satisfaction", "service", 1), eff2=Effect("increase satisfaction", "bisexual", 1), archetype="The Fox"),
                        Trait(_("Always wet"), verb ="be", eff1=Effect("increase satisfaction", "sex", 1), eff2=Effect("increase satisfaction", "group", 1), archetype="The Escort"),
                        Trait(_("Tight ass"), verb ="have a", eff1=Effect("increase satisfaction", "anal", 1), eff2=Effect("increase satisfaction", "fetish", 1), archetype="The Maid"),
                        Trait(_("Playful"), verb ="be", eff1=Effect("boost", "service preference increase", 0.15), eff2=Effect("boost", "bisexual preference increase", 0.15), eff3=Effect("change", "service max", 10, scales_with = "rank"), archetype="The Player"),
                        Trait(_("Wild"), verb ="be", eff1=Effect("boost", "sex preference increase", 0.15), eff2=Effect("boost", "group preference increase", 0.15), eff3=Effect("change", "sex max", 10, scales_with = "rank"), archetype="The Slut"),
                        Trait(_("Firm buttocks"), verb ="have", effects=[Effect("boost", "anal preference increase", 0.1), Effect("change", "anal max", 5, scales_with = "rank")], archetype="The Model"),
                        Trait(_("Dirty mind"), verb ="be", effects=[Effect("boost", "fetish preference increase", 0.1), Effect("change", "fetish max", 5, scales_with = "rank")], archetype="The Slut"),
                        Trait(_("Magnetic"), verb ="be", eff1=Effect("boost", "income", 0.02), archetype="The Model"),
                        Trait(_("Loose"), verb ="be", eff1=Effect("change", "train obedience target", -25), eff2=Effect("boost", "all sex acts preference increase", 0.1), archetype="The Player"),
                        Trait(_("Dedicated"), verb ="be", eff1=Effect("change", "job obedience target", -25), eff2=Effect("boost", "all jp gains", 0.05), archetype="The Maid"),
                        Trait(_("Provocative"), verb ="be", eff1=Effect("boost", "dress", 0.5), eff2=Effect("gain", "positive fixation", "cosplay"), archetype="The Model"),
                        Trait(_("Fashionista"), verb ="be", eff1=Effect("boost", "accessory", 0.25), eff2=Effect("boost", "necklace", 0.25), eff3=Effect("boost", "ring", 0.25), archetype="The Fox"),
                        Trait(_("Perfectionist"), verb ="be a", eff1=Effect("increase satisfaction", "all jobs", 1), archetype="The Courtesan"),
                        Trait(_("Elite"), verb ="be", eff1=Effect("special", "ignore budgets", 1), archetype="The Courtesan"),
                        Trait(_("Gifted"), verb ="be", eff1=Effect("increase satisfaction", "all sex acts", 1), archetype="The Bride"),
                        Trait(_("Fast learner"), verb ="be a", eff1=Effect("boost", "xp gains", 0.05), eff2=Effect("boost", "all jp gains", 0.05), archetype="The Escort"),
                        Trait(_("Caster"), verb ="be a", eff1=Effect("special", "rest shield", 1), archetype="The Bride"), #?
                        Trait(_("Driven"), verb ="be", eff1=Effect("boost", "max energy", 0.2), eff2=Effect("boost", "energy", 0.1), archetype="The Player"),
                        Trait(_("Country girl"), verb ="be a", eff1=Effect("special", "all farm weaknesses", 1), eff2=Effect("boost", "farm preference increase", 0.5), archetype="The Maid"),
                        Trait(_("Noble"), verb ="be a", eff1=Effect("boost", "prestige", 2), archetype="The Courtesan"),
                        Trait(_("Naturist"), verb ="be a", eff1=Effect("special", "naked", 1), archetype="The Model", base_description = __("She has no shame showing her naked body to perfect strangers.")),
                        Trait(_("Vicious"), verb ="be", effects=[Effect("change", "service", 5), Effect("change", "sex", 5), Effect("change", "anal", 5), Effect("change", "fetish", 5)], archetype="The Escort"),
                        Trait(_("Conduit"), verb = "be a", eff1 = Effect("change", "mojo cost", -1), archetype="The Fox"), #?

                        Trait(_("Dynamo"), verb = "be a", effects = [Effect("boost", "max energy", 0.3), Effect("boost", "energy", 0.15)], base_description = __("Burns with fiery energy."), public=False, archetype="The Fox"),
                        Trait(_("Lolita"), verb = "be a", effects = [Effect("boost", "tip", 2, chance=0.2)], base_description = __("She isn't actually underage, but looks like she is - and some customers love that."), public=False, archetype="The Player"),
                        Trait(_("Ghost"), verb = "be a", effects = [Effect("special", "immune", 1)], base_description = __("She is a ghost, and cannot be hurt by any normal means."), public=False, archetype="The Escort"),
                        Trait(_("Stalwart"), verb = "be", effects = [Effect("change", "all skill max", 10, scales_with = "rank")], base_description = __("It doesn't matter what she does, she'll train harder than anyone else."), public=False, archetype="The Bride"),
                        ]

        gold_traits += custom_traits["gold"]

        gold_trait_dict = {}

        for trait in gold_traits:
            gold_trait_dict[trait.name] = trait

        ## POSITIVE TRAITS ##

        pos_traits = [
                        Trait(_("Cute"), verb = "be", eff1 = Effect("change", "beauty", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Model"),
                        Trait(_("Long legs"), verb = "have", eff1 = Effect("change", "beauty", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Player"),
                        Trait(_("Nice boobs"), verb = "have", eff1 = Effect("change", "body", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Escort"),
                        Trait(_("Juicy ass"), verb = "have a", eff1 = Effect("change", "body", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Slut"),
                        Trait(_("Sweet"), verb = "be", eff1 = Effect("change", "charm", 5, scales_with = "rank"), eff2 = Effect("personality", "sweet"), archetype="The Bride"),
                        Trait(_("Exotic"), verb = "be", eff1 = Effect("change", "charm", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Fox"),
                        Trait(_("Polite"), verb = "be", eff1 = Effect("change", "refinement", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Courtesan"),
                        Trait(_("Feminine"), verb = "be", eff1 = Effect("change", "refinement", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Model"),
                        Trait(_("Horny"), verb = "be", eff1 = Effect("change", "libido", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Slut"),
                        Trait(_("Resilient"), verb = "be", eff1 = Effect("change", "constitution", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Maid"),
                        Trait(_("Delicate"), verb = "be", eff1 = Effect("change", "sensitivity", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Bride"),
                        Trait(_("Meek"), verb = "be", eff1 = Effect("change", "obedience", 5, scales_with = "rank"), eff2 = Effect("personality", "meek"), archetype="The Maid"),

                        Trait(_("Pretty eyes"), verb = "have", eff1 = Effect("change", "beauty", 10), eff2 = Effect("gain", "reputation", 5), archetype="The Model"), #!
                        Trait(_("Firm tits"), verb = "have", eff1 = Effect("change", "body", 10), eff2 = Effect("gain", "reputation", 5), archetype="The Slut"), #!
                        Trait(_("Seductive"), verb = "be", eff1 = Effect("change", "charm", 10), eff2 = Effect("gain", "reputation", 5), eff3 = Effect("personality", "superficial"), archetype="The Model"), #!
                        Trait(_("Graceful"), verb = "be", eff1 = Effect("change", "refinement", 10), eff2 = Effect("gain", "reputation", 5), archetype="The Courtesan"), #!

                        Trait(_("Beautiful"), verb = "be", eff1 = Effect("boost", "beauty gains", 0.25), archetype="The Model"),
                        Trait(_("Fit"), verb = "be", eff1 = Effect("boost", "body gains", 0.25), archetype="The Escort"),
                        Trait(_("Charming"), verb = "be", eff1 = Effect("boost", "charm gains", 0.25), archetype="The Fox"),
                        Trait(_("Elegant"), verb = "be", eff1 = Effect("boost", "refinement gains", 0.25), archetype="The Courtesan"),
                        Trait(_("Slutty"), verb = "be", eff1 = Effect("boost", "libido gains", 0.25), archetype="The Slut"),
                        Trait(_("Athletic"), verb = "be", eff1 = Effect("boost", "constitution gains", 0.25), archetype="The Player"),
                        Trait(_("Sensitive"), verb = "be", eff1 = Effect("boost", "sensitivity gains", 0.25), archetype="The Bride"),
                        Trait(_("Obedient"), verb = "be", eff1 = Effect("boost", "obedience gains", 0.25), archetype="The Maid"),

                        Trait(_("Energetic"), verb = "be", eff1 = Effect("boost", "max energy", 0.1), archetype="The Player"), ## This is a 10% increase
                        Trait(_("Tough"), verb = "be", eff1 = Effect("boost", "hurt", -0.33), archetype="The Maid"),
                        Trait(_("Sexy"), verb = "be", eff1 = Effect("boost", "reputation gains", 0.2), archetype="The Escort"),
                        Trait(_("Humble"), verb = "be", eff1 = Effect("boost", "upkeep", -0.2), archetype="The Maid"),

                        Trait(_("Virgin"), verb = "be a", eff1 = Effect("special", "virgin", 1), eff2 = Effect("change", "all sex acts requirements", 10), archetype="The Bride", base_description = __("This girl is a virgin.")), # Special trait, goes away after 1st sex
                        Trait(_("Sharp"), verb = "be", eff1 = Effect("boost", "xp gains", 0.1), eff2 = Effect("personality", "nerd"), archetype="The Fox"),
                        Trait(_("Loyal"), verb = "be", eff1 = Effect("boost", "love gains", 0.1), archetype="The Bride"),
                        Trait(_("Brave"), verb = "be", eff1 = Effect("boost", "fear", -0.1), archetype="The Escort"),
                        Trait(_("Strong"), verb = "be", eff1 = Effect("change", "defense", 2), archetype="The Player"),
                        Trait(_("Lucky"), verb = "be", eff1 = Effect("special", "lucky", 1), archetype="The Fox", base_description = __("She's up all night...")),

                        Trait(_("Deft"), verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.1), eff2 = Effect("boost", "masseuse jp gains", 0.1), archetype="The Maid"),
                        Trait(_("Nimble"), verb = "be", eff1 = Effect("boost", "dancer jp gains", 0.1), eff2 = Effect("boost", "geisha jp gains", 0.1), archetype="The Player"),
                        Trait(_("Soft skin"), verb = "have", eff1 = Effect("boost", "geisha jp gains", 0.1), eff2 = Effect("boost", "masseuse jp gains", 0.1), archetype="The Courtesan"),
                        Trait(_("Bright"), verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.1), eff2 = Effect("boost", "geisha jp gains", 0.1), archetype="The Courtesan"),
                        Trait(_("Agile"), verb = "be", eff1 = Effect("boost", "dancer jp gains", 0.1), eff2 = Effect("boost", "masseuse jp gains", 0.1), archetype="The Fox"),
                        Trait(_("Brisk"), verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.1), eff2 = Effect("boost", "dancer jp gains", 0.1), archetype="The Model"),

                        Trait(_("Rowdy"), verb = "be", effects = [Effect("boost", "waitress jp gains", 0.2), Effect("increase satisfaction", "waitress", 1), Effect("increase satisfaction", "geisha", -2)], opposite=['Modest', 'Unhurried'], archetype="The Slut"),
                        Trait(_("Powerful"), verb = "be", effects = [Effect("boost", "dancer jp gains", 0.2), Effect("increase satisfaction", "dancer", 1), Effect("increase satisfaction", "masseuse", -2)], opposite=['Modest', 'Unhurried'], archetype="The Bride"),
                        Trait(_("Unhurried"), verb = "be", effects = [Effect("boost", "masseuse jp gains", 0.2), Effect("increase satisfaction", "masseuse", 1), Effect("increase satisfaction", "waitress", -2)], opposite=['Powerful', 'Rowdy'], archetype="The Escort"),
                        Trait(_("Modest"), verb = "be", effects = [Effect("boost", "geisha jp gains", 0.2), Effect("increase satisfaction", "geisha", 1), Effect("increase satisfaction", "dancer", -2), Effect("personality", "meek")], opposite=['Rowdy', 'Powerful'], archetype="The Fox"),

                        Trait(_("Sensual"), verb = "be", eff1 = Effect("boost", "service jp gains", 0.1), eff2 = Effect("boost", "sex jp gains", 0.1), eff3 = Effect("personality", "pervert"), archetype="The Escort"),
                        Trait(_("Kinky"), verb = "be", eff1 = Effect("boost", "anal jp gains", 0.1), eff2 = Effect("boost", "fetish jp gains", 0.1), eff3 = Effect("personality", "masochist"), archetype="The Player"),
                        Trait(_("Pervert"), verb = "be a", eff1 = Effect("change", "all sex acts requirements", -10), eff2 = Effect("personality", "pervert"), archetype="The Slut"),
                        Trait(_("Thief"), verb = "be a", eff1 = Effect("special", "pickpocket", 1), archetype="The Fox", base_description = __("She may steal a little amount from the customers while seducing them. Reputation may suffer.")),
                        Trait(_("Sane"), verb = "be", eff1 = Effect("change", "sanity loss", -1), archetype="The Courtesan"),
                        Trait(_("Trusting"), verb = "be", eff1 = Effect("change", "fear per day", -1, chance=0.25), archetype="The Maid"),
                        Trait(_("Loving"), verb = "be", eff1 = Effect("change", "love per day", 1, chance=0.25), archetype="The Bride"),

                        ]

        pos_traits += custom_traits["pos"]

        ## NEGATIVE TRAITS ##

        neg_traits = [
                        Trait(_("Plain"), verb = "be", eff1 = Effect("change", "beauty", -10, scales_with = "rank"), opposite = "Cute"),
                        Trait(_("Scars"), verb = "have", eff1 = Effect("change", "body", -10, scales_with = "rank"), opposite = "Nice boobs"),
                        Trait(_("Mean"), verb = "be", eff1 = Effect("change", "charm", -10, scales_with = "rank"), opposite = "Sweet"),
                        Trait(_("Rude"), verb = "be", eff1 = Effect("change", "refinement", -10, scales_with = "rank"), opposite = "Polite"),
                        Trait(_("Cold"), verb = "be", eff1 = Effect("change", "libido", -10, scales_with = "rank"), eff2 = Effect("personality", "cold"), opposite = "Horny"),
                        Trait(_("Weak"), verb = "be", eff1 = Effect("change", "constitution", -10, scales_with = "rank"), opposite = "Resilient"),
                        Trait(_("Rough"), verb = "be", eff1 = Effect("change", "sensitivity", -10, scales_with = "rank"), opposite = "Delicate"),
                        Trait(_("Defiant"), verb = "be", eff1 = Effect("change", "obedience", -10, scales_with = "rank"), opposite = "Meek"),

                        Trait(_("Scruffy"), verb = "be", eff1 = Effect("boost", "beauty gains", -0.5), opposite = "Beautiful"),
                        Trait(_("Plump"), verb = "be", eff1 = Effect("boost", "body gains", -0.5), opposite = "Fit"),
                        Trait(_("Timid"), verb = "be", eff1 = Effect("boost", "charm gains", -0.5), opposite = "Charming"),
                        Trait(_("Vulgar"), verb = "be", eff1 = Effect("boost", "refinement gains", -0.5), opposite = "Elegant"),
                        Trait(_("Tame"), verb = "be", eff1 = Effect("boost", "libido gains", -0.5), opposite = "Slutty"),
                        Trait(_("Frail"), verb = "be", eff1 = Effect("boost", "constitution gains", -0.5), opposite = "Athletic"),
                        Trait(_("Jaded"), verb = "be", eff1 = Effect("boost", "sensitivity gains", -0.5), opposite = "Sensitive"),
                        Trait(_("Rebellious"), verb = "be", eff1 = Effect("boost", "obedience gains", -0.5), eff2 = Effect("personality", "rebel"), opposite = "Obedient"),

                        Trait(_("Lazy"), verb = "be", eff1 = Effect("boost", "max energy", -0.15), opposite = ["Energetic", "Driven"]),
                        Trait(_("Sickly"), verb = "be", eff1 = Effect("boost", "hurt", +2), opposite = "Tough"),
                        Trait(_("Homely"), verb = "be", eff1 = Effect("boost", "reputation gains", -0.25), opposite = "Sexy"),
                        Trait(_("Expensive"), verb = "be", eff1 = Effect("boost", "upkeep", 0.25), opposite = "Humble"),

                        Trait(_("Slow"), verb = "be", eff1 = Effect("boost", "xp gains", -0.25), opposite = ["Fast learner", "Sharp"]),
                        Trait(_("Disloyal"), verb = "be", eff1 = Effect("boost", "love gains", -0.25), opposite = "Loyal"),
                        Trait(_("Fearful"), verb = "be", eff1 = Effect("boost", "fear", 0.25), opposite = "Brave"),
                        Trait(_("Vulnerable"), verb = "be", eff1 = Effect("change", "defense", -2), opposite = ["Strong", "Warrior"]),
                        Trait(_("Unlucky"), verb = "be", eff1 = Effect("special", "unlucky", 1), base_description = __("She shouldn't have broken that magic mirror... Increased chance of critical failure when working."), opposite = "Lucky"),

                        Trait(_("All thumbs"), verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.5), eff2 = Effect("increase satisfaction", "waitress", -1), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy']),
                        Trait(_("Awkward"), verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.5), eff2 = Effect("increase satisfaction", "dancer", -1), opposite=['Nimble', 'Agile', 'Brisk', 'Powerful']),
                        Trait(_("Brutal"), verb = "be", eff1 = Effect("boost", "masseuse jp gains", -0.5), eff2 = Effect("increase satisfaction", "masseuse", -1), opposite=['Deft', 'Soft skin', 'Agile', 'Unhurried']),
                        Trait(_("Dumb"), verb = "be", eff1 = Effect("boost", "geisha jp gains", -0.5), eff2 = Effect("increase satisfaction", "geisha", -1), opposite=['Nimble', 'Soft skin', 'Bright', 'Modest']),
                        Trait(_("Oafish"), verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.5), eff2 = Effect("boost", "geisha jp gains", -0.5), opposite=['Nimble', 'Agile', 'Brisk', 'Soft skin', 'Bright']),
                        Trait(_("Clumsy"), verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.5), eff2 = Effect("boost", "masseuse jp gains", -0.5), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy', 'Soft skin', 'Agile']),

                        Trait(_("Prude"), verb = "be", eff1 = Effect("boost", "service jp gains", -0.5), eff2 = Effect("boost", "sex jp gains", -0.5), opposite = "Naughty"),
                        Trait(_("Naive"), verb = "be", eff1 = Effect("boost", "anal jp gains", -0.5), eff2 = Effect("boost", "fetish jp gains", -0.5), opposite = "Kinky"),
                        Trait(_("Square"), verb = "be", eff1 = Effect("change", "all sex acts requirements", 25), opposite = "Pervert"),
                        Trait(_("Insane"), verb = "be", eff1 = Effect("change", "sanity loss", 1), opposite = "Sane"),

                        Trait(_("Distrustful"), verb = "be", eff1 = Effect("change", "fear per day", 1, chance=0.25), opposite = "Trusting"),
                        Trait(_("Spiteful"), verb = "be", eff1 = Effect("change", "love per day", -1, chance=0.25), opposite = "Loving"),

                        Trait(_("Earthbound"), verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = __("Will not attack you. Deadly to everyone else."), public=False),
                        Trait(_("Waterbound"), verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = __("Will not attack you. Deadly to everyone else."), public=False),
                        Trait(_("Voidbound"), verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = __("Will not attack you. Deadly to everyone else."), public=False),
                        Trait(_("Firebound"), verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = __("Will not attack you. Deadly to everyone else."), public=False),
                        ]

        neg_traits += custom_traits["neg"]

        trait_dict = {}

        for trait in gold_traits + pos_traits + neg_traits:
            trait_dict[trait.name] = trait

        ## SPECIAL TRAITS ##

        virgin_trait = trait_dict["Virgin"]

        expensive_trait = trait_dict["Expensive"]

        clumsy_trait = trait_dict["Clumsy"]

        godless_trait = trait_dict["Godless"] = Trait(_("Godless"), verb = "be", eff1 = Effect("boost", "reputation gains", -0.2))

        housebroken_trait = trait_dict["Housebroken"] = Trait(_("Housebroken"), verb ="be", effects = [Effect("change", "job obedience target", -10), Effect("change", "whore obedience target", -10)], base_description = __("She lost her virginity in a brothel. This is all she knows."))

        t_pet_trait = trait_dict["Teacher's pet"] = Trait(_("Teacher's pet"), verb ="be a", effects = [Effect("change", "train obedience target", -20), Effect("boost", "love", 0.2)], base_description = __("Her first time was with you. You're special to her."))

        trauma_trait = trait_dict["Trauma"] = Trait(_("Trauma"), verb ="have a", effects = [Effect("change", "obedience", 15), Effect("change", "libido", -15), Effect("boost", "fear", 0.2)], base_description = __("She lost her virginity against her will, and has to live with the trauma."))

        farmgirl_trait = trait_dict["Farmgirl"] = Trait(_("Farmgirl"), verb ="be a", effects = [Effect("change", "obedience", 10), Effect("boost", "farm preference increase", 0.25)], base_description = __("She has lost her virginity in the farm like a filthy animal."))

        chaos_trait = trait_dict["Mark of Chaos"] = Trait(_("Mark of Chaos"), verb ="have a", effects = [Effect("boost", "sanity loss", -0.33)], base_description = __("She lost her virginity in a strange feverish dream, yet emerged with reinforced sanity."))


    return

#### END OF BK TRAITS FILE ####
