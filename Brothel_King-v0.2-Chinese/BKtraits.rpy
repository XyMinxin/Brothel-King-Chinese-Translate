#### BK TRAITS ####
## Labels are used instead of Functions to make sure we are using global variables


## How to add a new Trait to the game:
## - If you want all newly-generated girls to have a chance to get this Trait, add the Trait object to one of the "gold_traits", "pos_traits" or "neg_traits" lists. (e.g.: 'pos_traits.append(Trait("my_trait"))')
## - If you only want a specific girl to have the trait, add the trait directly using the Girl 'add_trait' method (e.g.: 'girl.add_trait(Trait("my_trait"))')
## - In all cases, make sure to update the Trait dictionary to avoid trait lookup problems (e.g.: 'trait_dict[trait.name] = Trait("my_trait")')
## - Note that if you want to include a custom made Trait as part of a _BK.ini file, the Trait() must be added to the dictionary before girls are generated (right after the init_traits() label is run)

define renamed_traits = {"Good tits" : "Firm tits"} # For backwards compatibility

label init_traits():

    python:

        ## GOLD TRAITS (for unique girls) ##

        gold_traits = [
                        Trait("Naughty", verb="be", eff1 = Effect("boost", "tip", 0.1), eff2 = Effect("personality", "pervert"), archetype="The Slut"),
                        Trait("Fascinating", verb="be", eff1 = Effect("change", "job customer capacity", 2), archetype="The Courtesan"),
                        Trait("Lust", verb="have", eff1=Effect("change", "whore customer capacity", 1), archetype="The Slut"),
                        Trait("Warrior", verb="be a", eff1=Effect("change", "defense", 3), eff2=Effect("personality", "rebel"), archetype="The Bride"),
                        Trait("Skilled tongue", verb="have a", eff1=Effect("increase satisfaction", "service", 1), eff2=Effect("increase satisfaction", "bisexual", 1), archetype="The Fox"),
                        Trait("Always wet", verb="be", eff1=Effect("increase satisfaction", "sex", 1), eff2=Effect("increase satisfaction", "group", 1), archetype="The Escort"),
                        Trait("Tight ass", verb="have a", eff1=Effect("increase satisfaction", "anal", 1), eff2=Effect("increase satisfaction", "fetish", 1), archetype="The Maid"),
                        Trait("Playful", verb="be", eff1=Effect("boost", "service preference increase", 0.1), eff2=Effect("boost", "bisexual preference increase", 0.1), archetype="The Player"),
                        Trait("Wild", verb="be", eff1=Effect("boost", "sex preference increase", 0.1), eff2=Effect("boost", "group preference increase", 0.1), archetype="The Slut"),
                        Trait("Dirty mind", verb="be", eff1=Effect("boost", "anal preference increase", 0.1), eff2=Effect("boost", "fetish preference increase", 0.1), archetype="The Fox"),
                        Trait("Magnetic", verb="be", eff1=Effect("boost", "income", 0.02), archetype="The Model"),
                        Trait("Loose", verb="be", eff1=Effect("change", "train obedience target", -25), archetype="The Player"),
                        Trait("Dedicated", verb="be", eff1=Effect("change", "job obedience target", -25), archetype="The Maid"),
                        Trait("Provocative", verb="be", eff1=Effect("boost", "dress", 0.5), eff2=Effect("gain", "positive fixation", "cosplay"), archetype="The Model"),
                        Trait("Fashionista", verb="be", eff1=Effect("boost", "accessory", 0.25), eff2=Effect("boost", "necklace", 0.25), eff3=Effect("boost", "ring", 0.25), archetype="The Fox"),
                        Trait("Perfectionist", verb="be a", eff1=Effect("increase satisfaction", "all jobs", 1), archetype="The Courtesan"),
                        Trait("Elite", verb="be", eff1=Effect("special", "ignore budgets", 1), archetype="The Courtesan"),
                        Trait("Gifted", verb="be", eff1=Effect("increase satisfaction", "all sex acts", 1), archetype="The Bride"),
                        Trait("Fast learner", verb="be a", eff1=Effect("boost", "xp gains", 0.05), eff2=Effect("boost", "all jp gains", 0.05), archetype="The Escort"),
                        Trait("Caster", verb="be a", eff1=Effect("special", "rest shield", 1), archetype="The Bride"), #!
                        Trait("Driven", verb="be", eff1=Effect("boost", "max energy", 0.2), eff2=Effect("boost", "energy", 0.1), archetype="The Player"),
                        Trait("Country girl", verb="be a", eff1=Effect("special", "all farm weaknesses", 1), eff2=Effect("boost", "farm preference increase", 0.5), archetype="The Maid"),
                        Trait("Noble", verb="be a", eff1=Effect("boost", "prestige", 2), archetype="The Courtesan"),
                        Trait("Naturist", verb="be a", eff1=Effect("special", "naked", 1), archetype="The Model", base_description = "她毫无羞耻地将自己的裸体展示给完全陌生的人。"),
                        Trait("Vicious", verb="be", effects=[Effect("change", "service", 5), Effect("change", "sex", 5), Effect("change", "anal", 5), Effect("change", "fetish", 5)], archetype="The Escort")
                        ]

        gold_trait_dict = {}

        for trait in gold_traits:
            gold_trait_dict[trait.name] = trait

        ## POSITIVE TRAITS ##

        pos_traits = [
                      Trait("Cute", verb = "be", eff1 = Effect("change", "beauty", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Model"),
                      Trait("Long legs", verb = "have", eff1 = Effect("change", "beauty", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Player"),
                      Trait("Nice boobs", verb = "have", eff1 = Effect("change", "body", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Escort"),
                      Trait("Juicy ass", verb = "have a", eff1 = Effect("change", "body", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Slut"),
                      Trait("Sweet", verb = "be", eff1 = Effect("change", "charm", 5, scales_with = "rank"), eff2 = Effect("personality", "sweet"), archetype="The Bride"),
                      Trait("Exotic", verb = "be", eff1 = Effect("change", "charm", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Fox"),
                      Trait("Polite", verb = "be", eff1 = Effect("change", "refinement", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Courtesan"),
                      Trait("Feminine", verb = "be", eff1 = Effect("change", "refinement", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Model"),
                      Trait("Horny", verb = "be", eff1 = Effect("change", "libido", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Slut"),
                      Trait("Resilient", verb = "be", eff1 = Effect("change", "constitution", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Maid"),
                      Trait("Delicate", verb = "be", eff1 = Effect("change", "sensitivity", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Bride"),
                      Trait("Meek", verb = "be", eff1 = Effect("change", "obedience", 5, scales_with = "rank"), eff2 = Effect("personality", "meek"), archetype="The Maid"),

                      Trait("Pretty eyes", verb = "have", eff1 = Effect("change", "beauty", 10), eff2 = Effect("gain", "reputation", 5), archetype="The Model"), #!
                      Trait("Firm tits", verb = "have", eff1 = Effect("change", "body", 10), eff2 = Effect("gain", "reputation", 5), archetype="The Slut"), #!
                      Trait("Seductive", verb = "be", eff1 = Effect("change", "charm", 10), eff2 = Effect("gain", "reputation", 5), eff3 = Effect("personality", "superficial"), archetype="The Model"), #!
                      Trait("Graceful", verb = "be", eff1 = Effect("change", "refinement", 10), eff2 = Effect("gain", "reputation", 5), archetype="The Courtesan"), #!

                      Trait("Beautiful", verb = "be", eff1 = Effect("boost", "beauty gains", 0.25), archetype="The Model"),
                      Trait("Fit", verb = "be", eff1 = Effect("boost", "body gains", 0.25), archetype="The Escort"),
                      Trait("Charming", verb = "be", eff1 = Effect("boost", "charm gains", 0.25), archetype="The Fox"),
                      Trait("Elegant", verb = "be", eff1 = Effect("boost", "refinement gains", 0.25), archetype="The Courtesan"),
                      Trait("Slutty", verb = "be", eff1 = Effect("boost", "libido gains", 0.25), archetype="The Slut"),
                      Trait("Athletic", verb = "be", eff1 = Effect("boost", "constitution gains", 0.25), archetype="The Player"),
                      Trait("Sensitive", verb = "be", eff1 = Effect("boost", "sensitivity gains", 0.25), archetype="The Bride"),
                      Trait("Obedient", verb = "be", eff1 = Effect("boost", "obedience gains", 0.25), archetype="The Maid"),

                      Trait("Energetic", verb = "be", eff1 = Effect("boost", "max energy", 0.1), archetype="The Player"), ## This is a 10% increase
                      Trait("Tough", verb = "be", eff1 = Effect("boost", "hurt", -0.33), archetype="The Maid"),
                      Trait("Sexy", verb = "be", eff1 = Effect("boost", "reputation gains", 0.2), archetype="The Escort"),
                      Trait("Humble", verb = "be", eff1 = Effect("boost", "upkeep", -0.2), archetype="The Maid"),

                      Trait("Virgin", verb = "be a", eff1 = Effect("special", "virgin", 1), eff2 = Effect("change", "sex act requirements", 10), archetype="The Bride", base_description = "这个女孩是个处女。"), # Special trait, goes away after 1st sex
                      Trait("Sharp", verb = "be", eff1 = Effect("boost", "xp gains", 0.1), eff2 = Effect("personality", "nerd"), archetype="The Fox"),
                      Trait("Loyal", verb = "be", eff1 = Effect("boost", "love gains", 0.1), archetype="The Bride"),
                      Trait("Brave", verb = "be", eff1 = Effect("boost", "fear", -0.1), archetype="The Escort"),
                      Trait("Strong", verb = "be", eff1 = Effect("change", "defense", 2), archetype="The Player"),
                      Trait("Lucky", verb = "be", eff1 = Effect("special", "lucky", 1), archetype="The Fox", base_description = "她彻夜未眠……"),

                      Trait("Deft", verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.1), eff2 = Effect("boost", "masseuse jp gains", 0.1), archetype="The Maid"),
                      Trait("Nimble", verb = "be", eff1 = Effect("boost", "dancer jp gains", 0.1), eff2 = Effect("boost", "geisha jp gains", 0.1), archetype="The Player"),
                      Trait("Soft skin", verb = "have", eff1 = Effect("boost", "geisha jp gains", 0.1), eff2 = Effect("boost", "masseuse jp gains", 0.1), archetype="The Courtesan"),
                      Trait("Bright", verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.1), eff2 = Effect("boost", "geisha jp gains", 0.1), archetype="The Courtesan"),
                      Trait("Agile", verb = "be", eff1 = Effect("boost", "dancer jp gains", 0.1), eff2 = Effect("boost", "masseuse jp gains", 0.1), archetype="The Fox"),
                      Trait("Brisk", verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.1), eff2 = Effect("boost", "dancer jp gains", 0.1), archetype="The Model"),

                      Trait("Rowdy", verb = "be", effects = [Effect("boost", "waitress jp gains", 0.2), Effect("increase satisfaction", "waitress", 1), Effect("increase satisfaction", "geisha", -2)], opposite=['Modest', 'Unhurried'], archetype="The Slut"),
                      Trait("Powerful", verb = "be", effects = [Effect("boost", "dancer jp gains", 0.2), Effect("increase satisfaction", "dancer", 1), Effect("increase satisfaction", "masseuse", -2)], opposite=['Modest', 'Unhurried'], archetype="The Bride"),
                      Trait("Unhurried", verb = "be", effects = [Effect("boost", "masseuse jp gains", 0.2), Effect("increase satisfaction", "masseuse", 1), Effect("increase satisfaction", "waitress", -2)], opposite=['Powerful', 'Rowdy'], archetype="The Escort"),
                      Trait("Modest", verb = "be", effects = [Effect("boost", "geisha jp gains", 0.2), Effect("increase satisfaction", "geisha", 1), Effect("increase satisfaction", "dancer", -2), Effect("personality", "meek")], opposite=['Rowdy', 'Powerful'], archetype="The Fox"),

                      Trait("Sensual", verb = "be", eff1 = Effect("boost", "service jp gains", 0.1), eff2 = Effect("boost", "sex jp gains", 0.1), eff3 = Effect("personality", "pervert"), archetype="The Escort"),
                      Trait("Kinky", verb = "be", eff1 = Effect("boost", "anal jp gains", 0.1), eff2 = Effect("boost", "fetish jp gains", 0.1), eff3 = Effect("personality", "masochist"), archetype="The Player"),
                      Trait("Pervert", verb = "be a", eff1 = Effect("change", "sex act requirements", -10), eff2 = Effect("personality", "pervert"), archetype="The Slut"),
                      Trait("Thief", verb = "be a", eff1 = Effect("special", "pickpocket", 1), archetype="The Fox", base_description = "她可能在引诱客户时从客户那里偷点钱。声誉可能会受到影响。"),
                      ]

        ## NEGATIVE TRAITS ##

        neg_traits = [
                      Trait("Plain", verb = "be", eff1 = Effect("change", "beauty", -10, scales_with = "rank"), opposite = "Cute"),
                      Trait("Scars", verb = "have", eff1 = Effect("change", "body", -10, scales_with = "rank"), opposite = "Nice boobs"),
                      Trait("Mean", verb = "be", eff1 = Effect("change", "charm", -10, scales_with = "rank"), opposite = "Sweet"),
                      Trait("Rude", verb = "be", eff1 = Effect("change", "refinement", -10, scales_with = "rank"), opposite = "Polite"),
                      Trait("Cold", verb = "be", eff1 = Effect("change", "libido", -10, scales_with = "rank"), eff2 = Effect("personality", "cold"), opposite = "Horny"),
                      Trait("Weak", verb = "be", eff1 = Effect("change", "constitution", -10, scales_with = "rank"), opposite = "Resilient"),
                      Trait("Rough", verb = "be", eff1 = Effect("change", "sensitivity", -10, scales_with = "rank"), opposite = "Delicate"),
                      Trait("Defiant", verb = "be", eff1 = Effect("change", "obedience", -10, scales_with = "rank"), opposite = "Meek"),

                      Trait("Scruffy", verb = "be", eff1 = Effect("boost", "beauty gains", -0.5), opposite = "Beautiful"),
                      Trait("Plump", verb = "be", eff1 = Effect("boost", "body gains", -0.5), opposite = "Fit"),
                      Trait("Timid", verb = "be", eff1 = Effect("boost", "charm gains", -0.5), opposite = "Charming"),
                      Trait("Vulgar", verb = "be", eff1 = Effect("boost", "refinement gains", -0.5), opposite = "Elegant"),
                      Trait("Tame", verb = "be", eff1 = Effect("boost", "libido gains", -0.5), opposite = "Slutty"),
                      Trait("Frail", verb = "be", eff1 = Effect("boost", "constitution gains", -0.5), opposite = "Athletic"),
                      Trait("Jaded", verb = "be", eff1 = Effect("boost", "sensitivity gains", -0.5), opposite = "Sensitive"),
                      Trait("Rebellious", verb = "be", eff1 = Effect("boost", "obedience gains", -0.5), eff2 = Effect("personality", "rebel"), opposite = "Obedient"),

                      Trait("Lazy", verb = "be", eff1 = Effect("boost", "max energy", -0.15), opposite = ["Energetic", "Driven"]),
                      Trait("Sickly", verb = "be", eff1 = Effect("boost", "hurt", +2), opposite = "Tough"),
                      Trait("Homely", verb = "be", eff1 = Effect("boost", "reputation gains", -0.25), opposite = "Sexy"),
                      Trait("Expensive", verb = "be", eff1 = Effect("boost", "upkeep", 0.25), opposite = "Humble"),

                      Trait("Slow", verb = "be", eff1 = Effect("boost", "xp gains", -0.25), opposite = ["Fast learner", "Sharp"]),
                      Trait("Distrustful", verb = "be", eff1 = Effect("boost", "love gains", -0.25), opposite = "Loyal"),
                      Trait("Fearful", verb = "be", eff1 = Effect("boost", "fear", 0.25), opposite = "Brave"),
                      Trait("Vulnerable", verb = "be", eff1 = Effect("change", "defense", -2), opposite = ["Strong", "Warrior"]),
                      Trait("Unlucky", verb = "be", eff1 = Effect("special", "unlucky", 1), base_description = "她不应该打破那面魔镜……工作时危急失败的机会增加。", opposite = "Lucky"),

                      Trait("All thumbs", verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.5), eff2 = Effect("increase satisfaction", "waitress", -1), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy']),
                      Trait("Awkward", verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.5), eff2 = Effect("increase satisfaction", "dancer", -1), opposite=['Nimble', 'Agile', 'Brisk', 'Powerful']),
                      Trait("Brutal", verb = "be", eff1 = Effect("boost", "masseuse jp gains", -0.5), eff2 = Effect("increase satisfaction", "masseuse", -1), opposite=['Deft', 'Soft skin', 'Agile', 'Unhurried']),
                      Trait("Dumb", verb = "be", eff1 = Effect("boost", "geisha jp gains", -0.5), eff2 = Effect("increase satisfaction", "geisha", -1), opposite=['Nimble', 'Soft skin', 'Bright', 'Modest']),
                      Trait("Oafish", verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.5), eff2 = Effect("boost", "geisha jp gains", -0.5), opposite=['Nimble', 'Agile', 'Brisk', 'Soft skin', 'Bright']),
                      Trait("Clumsy", verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.5), eff2 = Effect("boost", "masseuse jp gains", -0.5), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy', 'Soft skin', 'Agile']),

                      Trait("Prude", verb = "be", eff1 = Effect("boost", "service jp gains", -0.5), eff2 = Effect("boost", "sex jp gains", -0.5), opposite = "Naughty"),
                      Trait("Naive", verb = "be", eff1 = Effect("boost", "anal jp gains", -0.5), eff2 = Effect("boost", "fetish jp gains", -0.5), opposite = "Kinky"),
                      Trait("Square", verb = "be", eff1 = Effect("change", "sex act requirements", 25), opposite = "Pervert")
                      ]

        trait_dict = {}

        for trait in gold_traits + pos_traits + neg_traits:
            trait_dict[trait.name] = trait

        ## SPECIAL TRAITS ##

        expensive_trait = trait_dict["Expensive"]

        clumsy_trait = trait_dict["Clumsy"]

        godless_trait = trait_dict["Godless"] = Trait("Godless", verb = "be", eff1 = Effect("boost", "reputation gains", -0.2))

        housebroken_trait = trait_dict["Housebroken"] = Trait("Housebroken", verb="be", effects = [Effect("change", "job obedience target", -10), Effect("change", "whore obedience target", -10)], base_description = "她在一家青楼里被一位客人夺去了贞操。她只记得这些了。")

        t_pet_trait = trait_dict["Teacher's pet"] = Trait("Teacher's pet", verb="be a", effects = [Effect("change", "train obedience target", -20), Effect("boost", "love", 0.2)], base_description = "她的第一次献给了你。你对于她来说是特别的。")

        trauma_trait = trait_dict["Trauma"] = Trait("Trauma", verb="have a", effects = [Effect("change", "obedience", 15), Effect("change", "libido", -15), Effect("boost", "fear", 0.2)], base_description = "她在违背自己意愿的情况下失去了处女之身，不得不忍受创伤生活。")

        farmgirl_trait = trait_dict["Farmgirl"] = Trait("Farmgirl", verb="be a", effects = [Effect("change", "obedience", 10), Effect("boost", "farm preference increase", 0.25)], base_description = "她在农场里像肮脏的动物一样失去了她的贞操。")


        ## STORY GIRLS TRAITS ##

        trait_dict["Dynamo"] = Trait("Dynamo", verb = "be", effects = [Effect("boost", "max energy", 0.3), Effect("boost", "energy", 0.15)], base_description = "燃烧着炽热的能量。")
        trait_dict["Lolita"] = Trait("Lolita", verb = "be a", effects = [Effect("boost", "tip", 2, chance=0.2)], base_description = "她实际上并不是未成年，但看起来像是未成年 —— 一些顾客很喜欢这样。")
        trait_dict["Ghost"] = Trait("Ghost", verb = "be a", effects = [Effect("special", "immune", 1)], base_description = "她是一个幽灵，不能用任何正常的手段来伤害她。")
        trait_dict["Stalwart"] = Trait("Stalwart", verb = "be", effects = [Effect("change", "all skill max", 5, scales_with = "rank")], base_description = "她做什么都无所谓，她会比别人更努力地训练。")

        trait_dict["Firebound"] = Trait("Firebound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 7)], base_description = "不会攻击你。对其他所有人都是致命的。")
        trait_dict["Voidbound"] = Trait("Voidbound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 7)], base_description = "不会攻击你。对其他所有人都是致命的。")
        trait_dict["Waterbound"] = Trait("Waterbound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 7)], base_description = "不会攻击你。对其他所有人都是致命的。")
        trait_dict["Earthbound"] = Trait("Earthbound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 7)], base_description = "不会攻击你。对其他所有人都是致命的。")

    return

#### END OF BK TRAITS FILE ####
