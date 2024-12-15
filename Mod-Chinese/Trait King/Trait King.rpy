init -4 python:

    traitking_activated = False

    tag_dict = {
    # The key (left-hand side of the ':') is the string of characters BK looks for in the file name. The values (right-hand side) are the actual tags that will be added to the picture in-game.

                # Frequency tags

                "freq_highest" : "freq_highest",
                "freq_high" : "freq_high",
                "freq_low" : "freq_low",
                "freq_lowest" : "freq_lowest",

                # Old frequency tags (for retrocompatibility)

                "xq" : "freq_highest",
                "hq" : "freq_high",
                "lq" : "freq_low",

                # Portrait and profile tags (every girl should have at least one)

                "portrait" : "portrait",

                "profile" : "profile",

                # Specialized profile tags

                "market" : "market", # Used with preference to profile for the slavemarket
                "beauty" : ("profile", "model"), # Model is used for advertising pictures
                "card" : "profile",
#                "ent" : "profile", # Obsolete (conflicts with 'tent')
                "model" : ("profile", "model"), # Model is used for advertising pictures
                "advertise" : "model",
                "quest" : "profile",
                "shop" : "profile",
                "battle" : "fight",
                "fight" : "fight",
                "combat" : "fight",
                "hurt" : "hurt", # Use this instead of 'fight' if it shows her losing a fight

                "gallery" : "gallery", # Used as a background for the girl's CG gallery

                "happy" : "happy",
                "neutral" : "neutral",
                "sad" : "sad",
                "refuse" : "refuse",

                # Rest and work tags (highly recommended)

                "rest" : "rest",
                "ecchi" : ("rest", "libido"),

                "wait" : "waitress",
                "bunny" : ("waitress", "bunny", "cosplay"), # Bunny isn't used for now = cosplay
                "maid" : ("maid"), # Maid is used in the farm (obedience training)

                "danc" : ("dancer", "dance"), # Dancer is used for the job. Dance might be used in the future for classes and quests.
                "run" : ("constitution"), # Run is also used in the farm (constitution training)
                "sing" : ("dancer", "sing"), # Sing might be used in the future for classes and quests.
                "strip" : ("strip", "naked"), # Strip might be used in the future for classes and quests.

                "mass" : "masseuse",
                "swim" : ("swimsuit", "swim"), # Swimsuit might be used in the future for classes and quests. It is a fallback tag if no masseuse pic is found.

                "geisha" : "geisha",
                "etiquette" : "geisha",
                "kimono" : ("geisha", "kimono"), # kimono might be used in the future for classes and quests.
                "date" : "date", # Date is used for free girl interactions and court location profiles, and as a fallback tag for geisha

                "naked" : "naked", # Used in combination with other tags to make a girl appear naked
                "nude" : "naked",

                # Location tags (optional)

                "public" : "public", # The girl is in a publicly accessible place where there might be onlookers. Recommended for sexual events only (in BK)
                "beach" : ("public", "beach", "swimsuit", "swim"), # Beach pictures imply the swimsuit tag
                "nature" : ("public", "nature"), # The girl is in nature (except on a beach), such as in a garden, a forest or a field
                "town" : ("public", "town"), # The girl is in an urban environment, such as a street, a plaza or a market
                "city" : ("public", "town"),

                # Sexual tags (highly recommended)

                "virgin" : "virgin", # Used for images where the girl is losing her virginity

                # Note: Some service tags such as oral or handjob can have an effect on the text used in-game for flavor.

                "service" : "service",
                "mast" : ("mast"), # Most masturbating pics should be tagged service.
                "oral" : ("oral"), # Most oral pics should be tagged service.
                "blowjob" : ("oral"),
                "bj" : ("oral"),
                "cunnilingus" : ("cunni"), # Most cunnilingus pics should be tagged service.
                "hand" : ("handjob"),  # Most handjob pics should be tagged service.
                "titj" : ("titjob"), # Most titjob pics should be tagged service.
                "ttj" : ("titjob"),
                "tits" : ("titjob"),
                "titty" : ("titjob"),

                "sex" : "sex",
                "fuck" : "sex",
                "xxx" : ("sex", "XXX"), # XXX is used for XXX classes only, no need for it in girl packs

                "anal" : "anal",

                "fetish" : "fetish",
                "bdsm" : ("bondage"), # Bondage pics should be tagged fetish.
                "bondage" : ("bondage"),
                "hardcore" : ("fetish", "hardcore"), # hardcore is used for hardcore class stock pictures only, no need to use it in girl packs
                "foot" : ("footjob"), # Footjob pics should be tagged fetish (not service).
                "fj" : ("footjob"),

                # Optional tags: used for special sex acts and the farm. Can be mixed with regular sexual tags (necessary for the farm)

                "group" : "group",
                "bis" : "bisexual", # Bisexual pictures may feature up to one male
                "bisexual" : "bisexual", # This is needed to avoid 'bisexual' detecting the 'sex' tag
                "les" : ("lesbian", "bisexual"), # Lesbian pictures may not feature a male. The bisexual tag is added so that these pictures can proc during the appropriate sex act (the male protagonist is then assumed to be off-camera). Recommended for sexual events only (in BK)

                "beast" : "beast",
                "best" : "beast",

                "big" : "big",
                "stallion" : "big",

                "toy" : "toy", # Toy will be used inside and outside the farm (unless used with machine). Mostly used with service (masturbation) or fetish (administered by someone else).
                "machine" : "machine", # Machine will be excluded from regular events (except fetish if fuzzy tagging is on) and should be used for heavier machinery such as the ones found on the farm.

                "monster" : "monster",
                #"tent" : "monster",

                "libido" : "libido", # For the farm: Girl tending to minions
                "obedience" : "obedience", # For the farm: Girl cleaning up the farm
                "sensitivity" : "sensitivity", # For the farm: Girl tending to Gizel
                "constitution" : "constitution", # For the farm: Girl running in the yard
#                "sports" : "constitution", # Disabled to avoid confusion with watersports

                # Fixation tags: Used for specific fixations (recommended)

                "cosplay" : "cosplay",
                "dild" : ("dildo", "toy"),
                "vibr" : ("vibrator", "toy"),
                "plug" : ("plug", "toy"),
                "dirty" : "dirty",
                "penis w" : ("handjob"), # Most handjob pics should be tagged service as well
                "penisw" : ("handjob"),
                "penis_w" : ("handjob"),
                "penis-w" : ("handjob"),
                "oil" : "wet",
                "wet" : "wet",
                "sub" : "sub",
                "humiliat" : "sub",
                "master" : "sub", # Some Internet packs apparently use this tag, included here to avoid conflict with mast (masturbate)
                "dom" : "dom",
                "gag" : "gag",
                "strap" : "strap-on",
                "role" : "cosplay", # roleplay has been deprecated to cosplay
                "bead" : ("beads", "toy"),

                "irru" : ("deep"), # irrumatio has been deprecated to deepthroat
                "deep" : ("deep"),
                "dt" : ("deep"),
                "double" : "double", # Will add the 'group' tag if not used with the beast/monster/machine tag (hardcoded)
                "finger" : "finger",
                "fist" : "fist",
                "insults" : ("sub"),
                "sixty" : ("69"),
                "watersp" : ("watersports"), # watersports means the girl peeing
                "enema" : ("enema"),
                "kiss" : "kiss",
                "spank" : ("spank"),
                "rim" : "rim",
                "grop" : "grope",
                "fondl" : "fondle",
                "lact" : "lactation",
                "doggy" : "doggy",
                "cowg" : "cowgirl",
                "pile" : "piledriver",
                "spoon" : "spoon",

                "cum" : "cumshot",
                "buk" : ("buk", "cumshot"),
                "cim" : ("cim", "cumshot"),
                "mouth" : ("cim", "cumshot"),
                "cif" : ("cof", "cumshot"),
                "cof" : ("cof", "cumshot"),
                "face" : ("cof", "cumshot"),
                "cih" : ("cih", "cumshot"),
                "coh" : ("cih", "cumshot"),
                "hair" : ("cih", "cumshot"),
                "cob" : ("cob", "cumshot"),
                "body" : ("cob", "cumshot"),
                "shower" : ("cum shower", "cumshot"),
                "swa" : ("cim", "cumshot"),
                "cream" : ("creampie", "cumshot"), # Creampie differs from cum inside in that the dick is shown outside
                "cin" : ("cin", "cumshot"), # Cum inside differs from creampie in that the dick is shown inside her
                "inside" : ("cin", "cumshot"),
                "orgasm" : "orgasm",
                "denied" : "denied",
                "squirt" : ("squirt", "orgasm"),


                # Unused tags: Used for pictures that are ignored by the 'Check untagged girl pics' cheat. Mostly ignore this.

                "death" : "unused",
                #"preg" : "unused", # the pregnant tag might be used one day. One day...

                #activities
                "ceremony" : "ceremony",
                "study" : "study",

                # social
                "party" : "party",
                "friend" : "friend",

                "embar" : "embar",
                "angry" : "angry",
                "tempt" : "tempt",

                # cosplay/apparel
                "apron" : ("apron", "cosplay"),
                "china" : ("china", "geisha"),
                "dress" : "dress",
                "hooker" : ("hooker", "cosplay"),
                "nun" : ("nun", "cosplay"),
                "miko" : ("miko", "cosplay"),
                "casual" : "casual",
                "student" : ("student", "cosplay"),
                "teacher" : ("teacher", "cosplay"),
                "nurse" : ("nurse", "cosplay"),
                "santa" : ("santa", "cosplay"),
                "bride" : ("bride", "cosplay"),
                "catgirl" : ("catgirl", "cosplay"),

                "panties" : "panties",
                "lingerie" : "lingerie",

                # sexual
                "blindfold" : "blindfold",
                "collar" : "collar",
                "tentacles" : ("tentacles", "monster"), # in tag_dict now as "monster"

                # other
                "futanari" : "futanari",
                "pregnant" : "pregnant", # in tag_dict now as an ignored/forbidden tag

                }

init python:
    
    traitking_template = Mod(
        
                ## Basic mod information (Important: Version is used to check for new versions of the mod. Failure to update the version number may lead to broken mods and saved games)
                name = "traitking",
                folder = "Trait King",
                creator = "_neronero",
                version = 0.25, # Build 2024-09-13, for BK 0.3t
                pic = "title.webm",
                description = "Trait King adds more traits and various other features surrounding traits.",
                
                ## Mod option menu (access through the Help (click on '?') menu)
                #help_prompts = [("Activate","traitking_activate"),("Deactivate (experimental)","traitking_revert")],
                
                ## Early init label: This will run after the game is started, before the district and brothel is set-up.
                early_label="traitking_early_init",
                                
                ## Init label: This will run when the mod is activated, allowing you to set some variables and events if necessary
                init_label = "traitking_init",
                update_label = "traitking_update"
                
                )
                
    # custom dialogue: new year
    add_dialogue("holiday new year", ("very extravert"), (__("HAPPY NEW YEAR! This year it's {i}my{/i} time to shine. I just know it!"), __("Master! I wish you {i}so{/i} many blessings this year."), __("This is going to be, like, the best year ever!"), __("Happy new year, Master!"), __("A whole year has gone by already? Best wishes to you and yours, Master!")))
    add_dialogue("holiday new year", ("very introvert"), (__("Good wishes to you, Master."), __("All the very best, Master."), __("Oh... A year has gone by already?")))
    add_dialogue("holiday new year", ("very idealist"), (__("I've got my resolutions for this year all figured out. How about you, Master?"), __("Let's make this a year to remember!"), __("Together we can achieve even greater heights this year.")))
    add_dialogue("holiday new year", ("very materialist"), (__("Happy new year, [MC.name]."), __("Thank you for your guidance, [MC.name]."), __("Let's toast to another amazing year!")))
    add_dialogue("holiday new year", ("very lewd"), (__("Where's the champagne? We've got to drink to celebrate!"), __("Last year was a fucking blast, but I think we can do even better!"), __("Cheers, [MC.name]. Best year ever!")))
    add_dialogue("holiday new year", ("very modest"), (__("May Arios guide your path, [MC.name]. Happy new year."), __("May the light of Arios shine down on [brothel.name] this year."), __("Thank Arios for another year ahead of us. I pray that His Light may shine upon the world through our actions!")))
    add_dialogue("holiday new year", ("very dom"), (__("Happy new year! Let's get wasted!"), __("*sigh* Will we really be spending this year in [district.name]? I'd like a change of scenery."), __("I wonder what else [brothel.name] will have to offer this year.")))
    add_dialogue("holiday new year", ("very sub"), (__("T-thank you for everything, Master."), __("I love you, Master. I wish you all the best!"), __("I hope I can help [brothel.name] for many years to come, Master!")))

    # custom dialogue: valentines
    add_dialogue("slave love", ("very extravert"), (__("Master, I just want you and everyone else to know... I LOVE YOU!"), __("I love you {i}so{/i} much, Master!"), __("You're the best, [MC.name]. I love you more than anyone in the world!")))
    add_dialogue("slave love", ("very introvert"), (__("I-is this a good time? I love you, Master!"), __("*kiss* I love you, Master."), __("*kiss* Thank you for everything, Master.")))
    add_dialogue("slave love", ("very idealist"), (__("You're the love of my life! I hope we'll never be apart."), __("*kiss* I love everything about you!"), __("*blush* You are truly something special, Master. I love you!")))
    add_dialogue("slave love", ("very materialist"), (__("I adore you, Master."), __("Oh, Master! I don't care about anyone but you!"), __("I can't believe how much I've come to care about you, Master.")))
    add_dialogue("slave love", ("very lewd"), (__("I can't stop fantasizing about you, my love."), __("None of my toys come close to the experience of riding your cock, Master."), __("Fuck, you get me {i}so{/i} wet, [MC.name]")))
    add_dialogue("slave love", ("very modest"), (__("You complete me, [MC.name]."), __("[MC.name], you should know how much you mean to me... I love you!"), __("Oh [MC.name], I cannot imagine a life without you. We should get married!")))
    add_dialogue("slave love", ("very dom"), (__("You're awesome. You know that, right?"), __("I'm not that good at talking about this kind of stuff... I just wanted to let you know that I care about you."), __("Hey, uhm... I just wanted to confess that I really like you. A lot.")))
    add_dialogue("slave love", ("very sub"), (__("I love you more than anyone, Master!"), __("[MC.name], you're the one that I love. The only one."), __("Oh [MC.name], my sweetheart! I love you, love you, love you!")))
    
    # custom dialogue: salvation (Arios)
    add_dialogue("holiday salvation", ("very extravert"), (__("Isn't it fun to see the streets light up in this time of year?"), __("I'm always surprised at how they manage to fit all those candles inside the Cathedra.")))
    add_dialogue("holiday salvation", ("very introvert"), (__("Is it okay if I keep one candle lit inside my room?"), __("It takes just one candle to keep the darkness at bay.")))
    add_dialogue("holiday salvation", ("very idealist"), (__("What a beautiful day! Let's enjoy it to the fullest."), __("I love how traditions like this bring us all together."), __("I love to wander through Zan on this day. Wherever you are, a river of candles guides you towards the Cathedra."))) # likes holiday
    add_dialogue("holiday salvation", ("very materialist"), (__("We should totally sell our own candles next year. Imagine the gold you could rake in!"), __("What are we celebrating again? I don't get it.")))
    add_dialogue("holiday salvation", ("very lewd"), (__("Ugh, this is such a pain... I can think of somewhere else to stick those candles."), __("What's the point of all this? It's a waste of our time.")))
    add_dialogue("holiday salvation", ("very modest"), (__("May the Light of Arios guide our hearts!"), __("Thank you, Master. May Arios bless all those who frequent [brothel.name]."), __("That was a beautiful gesture, Master. Thank you."), __("I appreciate what you did today, Master."))) # loves holiday
    add_dialogue("holiday salvation", ("very dom"), (__("Is that all?"), __("*sigh* I've got better things to do today.")))
    add_dialogue("holiday salvation", ("very sub"), (__("*giggle* I'll worship whatever you want me to worship, Master."), __("Thank you, Master.")))
    add_dialogue("holiday salvation evil", ("very extravert"), (__("Aww, don't you like seeing all those candles light up the streets of Zan?"), __("Okay, Master. If you say so.")))
    add_dialogue("holiday salvation evil", ("very introvert"), (__("Oh... You don't like this tradition?"), __("W-we're not lighting up any candles? Not even one?")))
    add_dialogue("holiday salvation evil", ("very idealist"), (__("*pout* Why can't we just enjoy today's celebrations?"), __("*sigh* Well, that ruined my mood. Guess there's always next year."), __("We don't have to celebrate Arios, but let's at least enjoy the moment!"))) # likes holiday
    add_dialogue("holiday salvation evil", ("very materialist"), (__("Those candles are a fire hazard. Better safe than sorry."), __("I don't care much about this tradition anyways.")))
    add_dialogue("holiday salvation evil", ("very lewd"), (__("Thank you for saying what needed to be said, Master. [brothel.name] gets much more fun in the dark!"), __("I really don't care about any of this.")))
    add_dialogue("holiday salvation evil", ("very modest"), (__("*pout* I'm sorry, Master. I must excuse myself."), __("*sob* Oh, Master... I'm praying for you!"), __("*sob* I hope you will see Arios' Light one day, Master."), __("*sob* I can't believe this! I pray that Arios will bring light into our lives."))) # loves holiday
    add_dialogue("holiday salvation evil", ("very dom"), (__("Are we done? Who cares about any of this?"), __("Let's just get on with our day, shall we?")))
    add_dialogue("holiday salvation evil", ("very sub"), (__("Not a big fan of Arios? Then neither am I!"), __("Whatever you wish, Master.")))

    # custom dialogue: night of nights
    add_dialogue("slave defense", ("very extravert"), (__("You'll protect us, won't you [MC.name]?"), __("I hope things won't get too chaotic tonight.")))
    add_dialogue("slave defense", ("very introvert"), (__("Please keep [brothel.name] safe, Master."), __("I'm scared...")))
    add_dialogue("slave defense", ("very idealist"), (__("We'll be okay! Our security guards can handle it."), __("We have nothing to fear. Our Master will take care of things.")))
    add_dialogue("slave defense", ("very materialist"), (__("I'm not afraid of using a weapon if I have to."), __("I'm ready for anything tonight!")))
    add_dialogue("slave defense", ("very lewd"), (__("Nothing wrong with a bit of violence now and then to set people straight."), __("*sigh* Boys will be boys.")))
    add_dialogue("slave defense", ("very modest"), (__("Master! Protect me!"), __("Aah! I can't stand this!")))
    add_dialogue("slave defense", ("very dom"), (__("If anyone tries anything funny I'll slice off his cock."), __("If you want to test me, then come and get it.")))
    add_dialogue("slave defense", ("very sub"), (__("Master, I'm scared..."), __("Master, will we be okay?")))

    # custom dialogue: solstice/hmas
    add_dialogue("holiday hmas", ("very extravert"), (__("Okay, I admit it! I've been a naughty girl this year. *giggle*"), __("Ho ho ho, welcome one and all to [brothel.name]!"), __("What do Kosmo and a Hmas tree have in common? They both have ornamental balls.")))
    add_dialogue("holiday hmas", ("very introvert"), (__("Ho ho ho!"), __("Merry Hmas, [MC.name]."), __("You look jolly today.")))
    add_dialogue("holiday hmas", ("very idealist"), (__("It's so cold outside... Let's snuggle up together, shall we?"), __("My, look at the weather! Let's spend all day under a blanket together. *giggle*"), __("Everyone has been so naughty this year.")))
    add_dialogue("holiday hmas", ("very materialist"), (__("I wonder if I'll recieve any presents tomorrow..."), __("I really hope someone will put something precious in my stocking."), __("Merry Hmas to you, [MC.name].")))
    add_dialogue("holiday hmas", ("very lewd"), (__("*giggle* You've been such a naughty boy this year!"), __("*giggle* Is that a candy cane in your pocket, or are you just happy to see me?"), __("Naughty or nice? As if you even have to ask... Naughty ofcourse! *giggle*")))
    add_dialogue("holiday hmas", ("very modest"), (__("Have you been a good boy, [MC.name]?"), __("Are you giving away any presents tomorrow, [MC.name]?"), __("You've been really good to me, [MC.name]. Thank you.")))
    add_dialogue("holiday hmas", ("very dom"), (__("Are you looking forward to Hmas?"), __("I'm glad we can spend this time together."), __("I wonder if we'll get any snow this year.")))
    add_dialogue("holiday hmas", ("very sub"), (__("Have I been a good girl, [MC.name]?"), __("I wonder if I'll get any presents this year."), __("Am I naughty or nice, [MC.name]?")))

    # custom dialogue: birthday congrats
    add_dialogue("slave congrats", ("very extravert"), (__("Happy birthday, sweetie."), __("Congratulations! I wish you all the best."), __("*sings* Happy birthday to you! Happy birthday to you!"), __("There's our birthday gal! Let's get this party started!")))
    add_dialogue("slave congrats", ("very introvert"), (__("Happy birthday! Have a wonderful day."), __("*giggle* Surprise!"), __("Happy birthday!"), __("Congratulations!")))
    add_dialogue("slave congrats", ("very idealist"), (__("*sings* Happy birthday to you! Happy birthday to you!"), __("Yay! Let's celebrate!"), __("We're so glad to have you here."), __("You deserve the greatest birthday ever. Congratulations!")))
    add_dialogue("slave congrats", ("very materialist"), (__("So how old are you exactly?"), __("*giggle* You're wearing {i}that{/i} on your birthday?"), __("Surprise! Happy birthday, girl!"), __("Happy birthday, sweetie!")))
    add_dialogue("slave congrats", ("very lewd"), (__("To celebrate, you can sleep in my bed tonight."), __("HAPPY BIRTHDAY!"), __("Let's all stay up late tonight!"), __("*grin* Any customers you would like to celebrate with?")))
    add_dialogue("slave congrats", ("very modest"), (__("Happy birthday! You look absolutely radiant."), __("I hope you'll have a great day and a great year to come."), __("Congratulations! The years fly by, don't they?"), __("My, you look beautiful today. Have a wonderful birthday.")))
    add_dialogue("slave congrats", ("very dom"), (__("Did you get any presents yet?"), __("Any presents you're looking forward to?"), __("Perhaps we could visit the city together?"), __("Congrats!")))
    add_dialogue("slave congrats", ("very sub"), (__("Here, I made us some cake."), __("Happy birthday! Enjoy your day."), __("Look at that smile! Congratulations."), __("*hug* Congratulations!")))
    
    # custom dialogue: birthday-gal
    add_dialogue("slave birthday", ("very extravert"), (__("Thanks for coming, everyone. LET'S PARTY!"), __("Haha, HURRAY FOR ME!!")))
    add_dialogue("slave birthday", ("very introvert"), (__("T-thanks, I guess..."), __("O-okay... That's enough already.")))
    add_dialogue("slave birthday", ("very idealist"), (__("*sniff* T-thank you for coming... I love all of you so much!"), __("What a great surprise! Thanks everyone!")))
    add_dialogue("slave birthday", ("very materialist"), (__("Ahaha! I'm sure you've all been looking forward to this day. Where are my presents?"), __("Ahahaha! Thank you all so much. Now where are my presents?")))
    add_dialogue("slave birthday", ("very lewd"), (__("Yay! *giggle* Happy birthday to me!"), __("Yeah yeah, thanks I suppose. Now where's the stripper? I demand a stripper on my birthday!")))
    add_dialogue("slave birthday", ("very modest"), (__("I really appreciate this. Thank you!"), __("Aww, what a lovely surprise! Thanks everyone.")))
    add_dialogue("slave birthday", ("very dom"), (__("How did you all know this was my birthday?"), __("Damn, I'm tearing up... Thank you.")))
    add_dialogue("slave birthday", ("very sub"), (__("Aww, thanks everyone!"), __("T-thank you all so much.")))
    
    def add_trait_perkless(self, trait, _pos=None, forced=False): # Where 'trait' is an object (important)

        if not forced:
            for t in self.traits:
                if t.name in trait.opposite:
                    return False

        if _pos:
            self.traits.insert(_pos, trait)
        else:
            self.traits.append(trait)

        self.add_effects(trait.effects)

        return True

       
## This label runs when the mod version number is changed
label traitking_update:

    return
    
label traitking_early_init:

    python:
    
        ## GOLD TRAITS
        
        traitking_gold_s = [

                # Vanilla reworked

                Trait(_("Fascinating"), verb="be", eff1 = Effect("change", "job customer capacity", 2), eff2 = Effect("special", "job prestige", 1), archetype="The Courtesan", base_description = __("She is always the center of attention.")),
                Trait(_("Magnetic"), verb="be", effects=[Effect("boost", "prestige", 0.25, scales_with = "rank"), Effect("boost", "income", 0.01, scales_with = "rank"), Effect("change", "valuation", +100)], archetype="The Model", base_description = __("There is something about her that makes her unforgettable.")),

                Trait(_("Provocative"), verb="be", effects=[Effect("boost", "dress", 1.0), Effect("gain", "positive fixation", "cosplay")], archetype="The Model", base_description = __("She has an eye for fashion and knows how to dress to impress.")),
                Trait(_("Fashionista"), verb="be a", effects=[Effect("boost", "accessory", 0.1, scales_with = "rank"), Effect("boost", "necklace", 0.1, scales_with = "rank"), Effect("boost", "ring", 0.1, scales_with = "rank")], archetype="The Model", base_description = __("She is a trendsetter when it comes to fashion and jewelers all over Xeros would love to be worn by her.")),

                Trait(_("Perfectionist"), verb="be a", eff1=Effect("increase satisfaction", "all jobs", 1, chance=0.5), eff2=Effect("personality", "class president"), archetype="The Courtesan", base_description = __("She is unable to accept failure, always striving for perfection.")),
                Trait(_("Gifted"), verb="be", effects=[Effect("increase satisfaction", "all sex acts", 1, chance=0.5), Effect("change", "valuation", +100)], archetype="The Bride", base_description = __("She knows some amazing tricks that will make any sexual encounter more pleasurable.")),

                # Trait King originals

                Trait(_("Genius"), verb="be a", effects=[Effect("boost", "xp gains", 0.5), Effect("boost", "class results", 2.0), Effect("boost", "all skill gains", 0.25, scales_with = "rank")], archetype="The Escort", base_description = __("She has an exceptionally sharp mind.")),

                Trait(_("Famously beautiful"), verb = "be", effects = [Effect("change", "beauty", 40), Effect("gain", "reputation", 20), Effect("change", "customers", 4, dice=True, scope="brothel", scales_with="rank"), Effect("change", "valuation", +150)], archetype="The Model", base_description = __("She is known throughout the realm as one of Zan's crown jewels.")),

                Trait(_("Princess"), verb = "be a", effects=[Effect("boost", "prestige", 1.0, scales_with = "rank"), Effect("boost", "job customer budget", 1.0), Effect("boost", "whore customer budget", 1.0), Effect("change", "refinement", 15, scales_with = "rank"), Effect("boost", "upkeep", 4.0), Effect("change", "job obedience target", 80), Effect("change", "whore obedience target", 200), Effect("change", "train obedience target", 50), Effect("personality", "princess"), Effect("gain", "reputation", 100), Effect("change", "valuation", +1000)], archetype="The Courtesan", base_description = __("They say she has royal blood flowing through her veins.")),
                Trait(_("Royal Concubine"), verb = "be a", effects=[Effect("boost", "prestige", 1), Effect("boost", "refinement gains", 0.5), Effect("change", "whore obedience target", -50), Effect("change", "train obedience target", -50), Effect("boost", "tip", 0.25), Effect("boost", "upkeep", 1.0), Effect("gain", "reputation", 25), Effect("change", "valuation", +250)], archetype="The Courtesan", base_description = __("Rumour has it she once served as one of the King's concubines.")),

                Trait(_("Ambitious"), verb = "be", eff1 = Effect("boost", "reputation gains", 0.5), eff2=Effect("boost", "quest results", 1.0), eff3 = Effect("change", "all skill max", 10), archetype="The Player", base_description = __("She is filled with determination to succeed and climb the social ladder.")),

                Trait(_("Exhibitionist"), verb="be an", effects=[Effect("boost", "naked bonus", 0.1, scales_with = "rank"), Effect("boost", "libido gains", 0.25), Effect("change", "valuation", +50)], archetype="The Player", base_description = __("She loves showing her naked body, especially to strangers.")),

                Trait(_("Karkyrian Hymen"), verb = "have a", effects=[Effect("boost", "sex preference increase", -0.75)], base_description = __("She is equipped with a self-repairing hymen which perpetually rips and bleeds during intercourse.")),

                Trait(_("Idol"), verb = "be an", effects=[Effect("change", "customers", 8, dice=True, scope="brothel"), Effect("boost", "job customer budget", 0.1, scales_with = "cust nb")], base_description = __("She has lots of adoring fans."))
        ]

        traitking_gold_a = [

                # Vanilla reworked

                Trait(_("Naughty"), verb="be", eff1 = Effect("boost", "tip", 0.1), eff2 = Effect("special", "temptress", 0.33), eff3=Effect("personality", "pervert"), archetype="The Slut", base_description = __("She enjoys recieving dirty requests.")),
                Trait(_("Lust"), verb="have", eff1=Effect("change", "whore customer capacity", 1), eff2=Effect("change", "libido", 25), archetype="The Escort", base_description = __("She has a limitless desire for sex.")),
                Trait(_("Warrior"), verb="be a", effects=[Effect("change", "defense", 1, scales_with = "rank"), Effect("change", "security", 1, scope = "brothel", scales_with = "rank"), Effect("personality", "rebel")], base_description = __("She is a trained warrior who knows how to defend herself.")),

                Trait(_("Fast learner"), verb="be a", effects=[Effect("boost", "xp gains", 0.25), Effect("boost", "all jp gains", 0.25), Effect("boost", "class results", 1.0), Effect("personality", "class president")], archetype="The Courtesan", base_description = __("She is an exemplary student with an insatiable thirst for knowledge.")),

                Trait(_("Caster"), verb="be a", effects= [Effect("change", "mana", 2, scope="brothel"), Effect("special", "rest shield", 1), Effect("special", "shield", 1), Effect("change", "valuation", +100)], archetype="The Bride", base_description = __("She is educated in the spiritual arts.")),

                Trait(_("Driven"), verb="be", eff1=Effect("boost", "max energy", 0.3), eff2=Effect("boost", "energy", 0.2), eff3=Effect("boost", "quest results", 0.25), archetype="The Player", base_description = __("She works tirelessly to improve herself.")),

                Trait(_("Noble"), verb="be a", effects=[Effect("boost", "prestige", 2), Effect("boost", "upkeep", 2.0), Effect("change", "job obedience target", 50), Effect("change", "whore obedience target", 50), Effect("change", "train obedience target", 25), Effect("change", "valuation", +500), Effect("personality", "prude")], opposite = "Humble", archetype="The Courtesan", base_description = __("Supposedly she belongs to a well-known noble family.")),
                Trait(_("Elite"), verb="be", effects=[Effect("special", "ignore budgets", 1), Effect("personality", "princess"), Effect("change", "valuation", +200), Effect("change", "brothel reputation", 5, chance=0.25, scope="brothel")], archetype="The Courtesan", base_description = __("She is perceived to have noble connections. Customers consider time spent with her as an investment and are willing to overspend.")),

                Trait(_("Naturist"), verb="be a", effects = [Effect("boost", "naked bonus", 0.2), Effect("change", "valuation", +25), Effect("special", "naked", 1)], archetype="The Player", base_description = __("She prefers to do everything in the nude.")),

                # Trait King originals

                Trait(_("Ferocious"), verb="be", effects=[Effect("change", "all sex skills", 5, scales_with="rank"), Effect("boost", "constitution", 0.25)], archetype="The Escort", base_description = __("She turns into an wild beast in the bedroom, filled with primal sexual energy.")),

                Trait(_("Empyreal"), verb = "be", effects=[Effect("special", "immune", 1), Effect("resist", "hurt", 3)], base_description = __("She is under the effects of a powerful spell that makes her immune to physical violence.")),

                Trait(_("Nurse"), verb = "be a", effects=[Effect("change", "heal", 1, chance=0.25, scope="brothel"), Effect("increase satisfaction", "masseuse", 1)], base_description = __("She has some experience as a medical specialist.")),

                Trait(_("Porter"), verb = "be a", effects=[Effect("boost", "city rewards", 0.05, scales_with = "rank", scope="brothel"), Effect("boost", "resource extraction", 0.25, scope="brothel")], base_description = __("She carries more baggage than any girl you know.")),

                Trait(_("Mentor"), verb = "be a", effects=[Effect("special", "skill catch up", 1), Effect("change", "making friends", 1)], base_description = __("She gets along famously with other girls.")),

                Trait(_("Hustler"), verb = "be a", effects=[Effect("special", "workwhore", 1), Effect("boost", "service preference increase", 0.5), Effect("special", "deep throat", 1), Effect("personality", "schemer")], base_description = __("She doesn't mind earning some extra cash on the side through special services.")),

                Trait(_("Prodigy"), verb = "be a", effects=[Effect("change", "valuation", +20, scales_with = "rank")], base_description = __("She has great potential.")),
        ]

        traitking_gold_b = [

                # Vanilla reworked

                Trait(_("Skilled tongue"), verb="have a", effects=[Effect("increase satisfaction", "service", 1), Effect("increase satisfaction", "bisexual", 1)], archetype="The Fox", base_description = __("She is exceptionally skilled at oral sex acts.")),
                Trait(_("Always wet"), verb="be", effects=[Effect("increase satisfaction", "group", 1), Effect("increase satisfaction", "sex", 1)], archetype="The Escort", base_description = __("She is always ready to have sex. No foreplay required.")),
                Trait(_("Tight ass"), verb="have a", eff1=Effect("increase satisfaction", "anal", 1), eff2=Effect("increase satisfaction", "fetish", 1), base_description = __("Her rectum is nice and tight.")),

                Trait(_("Country girl"), verb="be a", eff1=Effect("special", "all farm weaknesses", 1), eff2=Effect("boost", "farm preference increase", 1.0), eff3=Effect("change", "valuation", -50), archetype="The Maid", base_description = __("She loves working with animals. Not the human kind.")),

                Trait(_("Vicious"), verb="be", effects=[Effect("change", "sex", 20), Effect("change", "anal", 20), Effect("change", "fetish", 20), Effect("personality", "bimbo")], archetype="The Escort", base_description = __("She leads a depraved life filled with debauchery.")),

                # Trait King originals

                Trait(_("Nymphomaniac"), verb = "be a", effects=[Effect("boost", "libido gains", 0.5), Effect("change", "sex", 25), Effect("change", "sex act requirements", -25), Effect("change", "whore obedience target", -25)], archetype="The Slut", base_description = __("She posesses an uncontrollable sexual desire.")),

                Trait(_("Enchanting"), verb="be", effects=[Effect("increase satisfaction", "geisha", 1), Effect("gain", "reputation", 25), Effect("change", "refinement", 10), Effect("change", "valuation", +50)], archetype="The Fox", base_description = __("She carries a captivating aura with her.")),
                Trait(_("Eye-catching"), verb = "be", effects=[Effect("increase satisfaction", "dancer", 1), Effect("change", "advertising", 1, scope="brothel", scales_with = "rank")], archetype="The Player", base_description = __("She has an incredible body that demands your attention.")),

                Trait(_("Insatiable"), verb = "be", effects=[Effect("change", "libido", 25), Effect("increase satisfaction", "group", 1), Effect("increase satisfaction", "bisexual", 1)], archetype="The Slut", base_description = __("She enjoys the thrill of satisfying multiple people at once.")),
                
                # ? - Kemono (fairy-folk with animal characteristics)
        ]

        traitking_gold_c = [

                # Vanilla reworked

                Trait(_("Playful"), verb="be", effects=[Effect("boost", "service preference increase", 0.25), Effect("boost", "bisexual preference increase", 0.25), Effect("boost", "service jp gains", 1.0), Effect("boost", "waitress jp gains", 1.0)], archetype="The Player", base_description = __("She likes to have fun and play around.")),
                Trait(_("Wild"), verb="be", effects=[Effect("boost", "sex preference increase", 0.05, scales_with = "rank"), Effect("boost", "group preference increase", 0.05, scales_with = "rank"), Effect("change", "defense", 1)], archetype="The Slut", base_description = __("She is an adventurous type.")),
                Trait(_("Dirty mind"), verb="have a", effects=[Effect("boost", "anal preference increase", 0.05, scales_with = "rank"), Effect("boost", "fetish preference increase", 0.05, scales_with = "rank")], archetype="The Fox", base_description = __("She gets a kick out of crossing boundaries and performing taboo sex acts.")),

                Trait(_("Loose"), verb="be", effects=[Effect("change", "train obedience target", -40), Effect("change", "valuation", -40), Effect("personality", "pet")], archetype="The Player", base_description = __("She does not mind trying out new things with her master, making her very easy to train.")),
                Trait(_("Dedicated"), verb="be", effects=[Effect("change", "job obedience target", -25), Effect("change", "valuation", -25), Effect("personality", "loyal")], archetype="The Maid", base_description = __("She likes to make herself useful.")),
                
                ### NEW IN 0.3
                Trait(_("Conduct"), verb = "be a", eff1 = Effect("change", "mojo cost", -1), archetype="The Fox", base_description = __("Her body is unusually attuned to mojo.")), #?

                Trait("Dynamo", verb = "be a", effects = [Effect("boost", "max energy", 0.3), Effect("boost", "energy", 0.15)], base_description = "She burns with a fiery energy.", public=False),
                Trait("Lolita", verb = "be a", effects = [Effect("boost", "tip", 2, chance=0.2)], base_description = "She isn't actually underage, but looks like she is - and some customers love that.", public=False),
                Trait("Ghost", verb = "be a", effects = [Effect("special", "immune", 1)], base_description = "She is a ghost, and cannot be hurt by any normal means.", public=False),
                Trait("Stalwart", verb = "be", effects = [Effect("change", "all skill max", 5, scales_with = "rank")], base_description = "It doesn't matter what she does, she'll train harder than anyone else.", public=False),
                
                # Trait King originals

                Trait(_("Angelic"), verb = "be", effects=[Effect("boost", "reputation gains", 0.5), Effect("special", "effect chance", 0.25), Effect("change", "valuation", +60)], opposite = "Godless", archetype="The Fox", base_description = __("She has a saint-like aura about her.")),
                Trait(_("Irresistable"), verb = "be", effects=[Effect("change", "charm", 10, scales_with = "rank"), Effect("boost", "reputation gains", 0.1, scales_with = "rank"), Effect("personality", "superficial")], archetype="The Fox", base_description = __("She has an incredible allure that fills hearts with desire.")),

                Trait(_("Erudite"), verb = "be", effects=[Effect("change", "refinement", 30), Effect("boost", "class results", 0.5), Effect("boost", "xp gains", 0.5)], archetype="The Courtesan", base_description = __("She is cultured and well-educated.")),

                Trait(_("Caretaker"), verb = "be a", effects=[Effect("change", "maintenance", 1, scope="brothel", scales_with = "rank"), Effect("increase satisfaction", "waitress", 1)], archetype="The Maid", base_description = __("She has the qualities of an ideal maid.")),

                Trait(_("Anal slut"), verb="be an", effects=[Effect("increase satisfaction", "anal", 1), Effect("boost", "anal preference increase", 0.5), Effect("boost", "anal jp gains", 1.0)], archetype="The Slut", base_description = __("She prefers using the back door.")),
                Trait(_("Uninhibited"), verb="be", effects=[Effect("increase satisfaction", "fetish", 1), Effect("boost", "fetish preference increase", 0.5)], archetype="The Slut", base_description = __("She knows no boundaries and outperforms other girls during extreme sex acts.")),
        ]

        traitking_gold_special = [

                # Vanilla reworked

                # Trait King originals

                Trait(_("In demand"), verb = "be", eff1 = Effect("change", "valuation", +200), base_description = __("She's a hot commodity and would fetch a pretty price on the slave market."), public=False),
                Trait("Fan favorite", verb = "be a", eff1 = Effect("change", "valuation", +350), base_description = "She's extremely popular right now and would fetch a superb price on the slave market.", public=False)

        ]
        
        traitking_gold_traits = traitking_gold_s + traitking_gold_a + traitking_gold_b + traitking_gold_c + traitking_gold_special
        

        ## POSITIVE TRAITS

        traitking_pos_s = [

                # Vanilla reworked

                # Trait King originals

                Trait(_("Tight pussy"), verb="have a", effects = [Effect("increase satisfaction", "sex", 1, chance=0.75), Effect("change", "sensitivity", 5, scales_with = "rank")], archetype="The Slut", base_description = __("She has a young, tight pussy that feels absolutely amazing.")),

                Trait(_("Submissive"), verb="be", effects = [Effect("increase satisfaction", "fetish", 1, chance = 0.5), Effect("change", "obedience", 30),  Effect("personality", "masochist"), Effect("change", "valuation", +20)], archetype="The Slut", base_description = __("She likes to be dominated.")),
                Trait(_("Good Kisser"), verb="be a", effects = [Effect("change", "libido", 20), Effect("increase satisfaction", "bisexual", 1, chance = 0.75)], archetype="The Escort", base_description = __("She is a great kisser.")),
                Trait(_("Bisexual"), verb="be", effects = [Effect("increase satisfaction", "bisexual", 1), Effect("boost", "bisexual chance", 0.25), Effect("change", "valuation", +25)], base_description = __("She likes to pleasure the ladies just as much as the men.")),
                Trait(_("Orgy girl"), verb="be an", effects = [Effect("increase satisfaction", "group", 1), Effect("boost", "group chance", 0.25), Effect("change", "valuation", +30)], archetype="The Slut", base_description = __("She would like to pleasure you and all of your friends.")),

                Trait(_("Happy-Go-Lucky"), verb="be", effects = [Effect("change", "mood", 4), Effect("personality", "sweet")], archetype="The Bride", base_description = __("Nothing ever gets her down")),
                Trait(_("Trendy"), verb="be", effects = [Effect("boost", "dress", 0.1), Effect("boost", "accessory", 0.1), Effect("boost", "necklace", 0.1), Effect("boost", "ring", 0.1)], archetype="The Escort", base_description = __("She dresses fashionably.")),
                Trait(_("Passionate"), verb="be", effects = [Effect("reroll", "job critical failure", 1, chance=0.5)], archetype="The Maid", base_description = __("She takes pride in her work and sets a high bar for herself.")),
                Trait(_("Persuasive"), verb="be", effects = [Effect("boost", "customer penalties", -0.5)], archetype="The Bride", base_description = __("She knows how to get her way.")),
        ]

        traitking_pos_a = [

                # Vanilla reworked

                Trait(_("Athletic"), verb = "be", eff1 = Effect("boost", "constitution gains", 1.0), eff2 = Effect("increase satisfaction", "dancer", 1, chance=0.5), eff3=Effect("change", "valuation", +10), archetype="The Escort", base_description = __("She has an athletic body and is very healthy.")),
                Trait(_("Sensitive"), verb = "be", eff1 = Effect("boost", "sensitivity gains", 1.0), eff2 = Effect("gain", "reputation", 10), eff3=Effect("increase satisfaction", "geisha", 1, chance=0.5), archetype="The Bride", base_description = __("She has a great capacity for empathy.")),
                Trait(_("Deft"), verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.25), eff2 = Effect("boost", "masseuse jp gains", 0.5), eff3 = Effect("increase satisfaction", "masseuse", 1, chance=0.5), archetype="The Maid", base_description = __("She has dexterous hands.")),

                Trait(_("Energetic"), verb = "be", eff1 = Effect("boost", "max energy", 0.25), eff2=Effect("change", "valuation", +10), archetype="The Player", base_description = __("She is always bursting with energy.")),

                Trait(_("Strong"), verb = "be", eff1 = Effect("change", "defense", 2), eff2=Effect("change", "security", 2, scope = "brothel"), archetype="The Bride", base_description = __("She could probably beat you in an armwrestling contest.")),

                Trait(_("Sensual"), verb="be", effects = [Effect("change", "beauty", 10), Effect("change", "sensitivity", 10), Effect("change", "customers", 1, dice=False, scope="brothel", scales_with="rank"), Effect("gain", "reputation", 10), Effect("change", "valuation", +20)], archetype="The Model", base_description = __("She likes to cuddle.")),
                Trait(_("Kinky"), verb = "be", effects = [Effect("increase satisfaction", "fetish", 1), Effect("increase satisfaction", "group", 1), Effect("personality", "masochist"), Effect("gain", "reputation", 10), Effect("change", "valuation", +20)], base_description = __("She won't mind if you bring out the whip."), archetype="The Slut"),

                # Trait King originals

                Trait(_("Groomed"), verb="be", effects = [Effect("change", "refinement", 5, scales_with = "rank"), Effect("change", "all main skills", 10), Effect("gain", "reputation", 10), Effect("change", "valuation", +40)], opposite = "Uncouth", archetype="The Courtesan", base_description = __("She has been educated in mannerisms befitting a Lady of the Court.")),

                Trait(_("Flasher"), verb="be a", effects = [Effect("special", "flasher", 1), Effect("increase satisfaction", "waitress", 1, chance=0.5), Effect("boost", "reputation gains", 0.25)], archetype="The Player", base_description = __("She may lift her top up when you least expect it, so don't blink.")),
                Trait(_("Contortionist"), verb="be a", effects = [Effect("increase satisfaction", "dancer", 1, chance=0.5), Effect("change", "advertising", 1, scope = "brothel"), Effect("change", "valuation", +20)], archetype="The Player", base_description = __("Her body is flexible enough to build a circus act around it.")),
                Trait(_("Tantric masseuse"), verb="be a", effects = [Effect("increase satisfaction", "masseuse", 1,chance=0.5), Effect("change", "advertising", 1, scope = "brothel")], archetype="The Model", base_description = __("She can unlock your latent sexual energy through massages.")),
                Trait(_("Multilingual"), verb="be", effects = [Effect("increase satisfaction", "geisha", 1, chance=0.5), Effect("change", "advertising", 1, scope = "brothel")], archetype="The Courtesan", base_description = __("She speaks several languages.")),

                Trait(_("Diligent"), verb = "be", effects=[Effect("boost", "max energy", 0.1), Effect("boost", "energy", 0.1), Effect("boost", "customer penalties", -0.25)], archetype="The Maid", base_description = __("She approaches her work with great care.")),  

                Trait(_("Fake Orgasms"), verb="have", effects = [Effect("increase satisfaction", "sex", 1, chance=0.5), Effect("change", "sex", 20), Effect("change", "valuation", -15, scales_with = "rank")], archetype="The Escort", base_description = __("Her moans make it seem as if you're penetrating her soul. Most people like it, but not everyone is convinced.")),


        ]

        traitking_pos_b = [

                # Vanilla reworked

                Trait(_("Cute"), verb = "be", eff1 = Effect("change", "beauty", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Player", base_description = __("She's just so damn cute.")),
                Trait(_("Nice boobs"), verb = "have", eff1 = Effect("change", "body", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Escort", base_description = __("She is blessed with a great set of tits.")),
                Trait(_("Feminine"), verb = "be", eff1 = Effect("change", "refinement", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Model", base_description = __("She is characteristically female.")),
                Trait(_("Horny"), verb = "be", eff1 = Effect("change", "libido", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 10), archetype="The Slut", base_description = __("She easily gets turned on.")),

                Trait(_("Juicy ass"), verb = "have a", effects = [Effect("increase satisfaction", "anal", 1, chance=0.25)], archetype="The Model", base_description = __("Playing with her ass is one of life's greatest pleasures.")),

                Trait(_("Exotic"), verb = "be", eff1 = Effect("change", "charm", 20), eff2 = Effect("gain", "reputation", 10), eff3 = Effect("change", "valuation", +100), archetype="The Fox", base_description = __("She does not look like a Xeros native.")),

                Trait(_("Pretty eyes"), verb = "have", eff1 = Effect("change", "beauty", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +20), archetype="The Model", base_description = __("She has eyes that twinkle like the stars above Karkyr.")),
                Trait(_("Firm tits"), verb = "have", eff1 = Effect("change", "body", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +20), archetype="The Player", base_description = __("She has unusually firm tits. Some say that's because her tits have been magically enhanced to deter evil. Her boobs are a force for good.")),
                Trait(_("Graceful"), verb = "be", eff1 = Effect("change", "refinement", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +30), archetype="The Courtesan", base_description = __("She moves with grace, like a princess.")),
                Trait(_("Seductive"), verb = "be", effects=[Effect("change", "charm", 5, scales_with = "rank"), Effect("change", "valuation", +10, scales_with = "rank"), Effect("personality", "superficial")], archetype="The Fox", base_description = __("She likes to take the initiative.")),

                Trait(_("Beautiful"), verb = "be", eff1 = Effect("boost", "beauty gains", 1.0), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +20, scales_with = "rank"), archetype="The Model", base_description = __("She is gorgeous to look at.")),

                Trait(_("Slutty"), verb="be", effects = [Effect("change", "libido", 20), Effect("boost", "reputation gains", 0.25), Effect("change", "valuation", +5, scales_with = "rank")], archetype="The Slut", base_description = __("She likes to sleep around.")),

                Trait(_("Lucky"), verb = "be", eff1 = Effect("special", "lucky", 1), archetype="The Fox", base_description = __("Her life is filled with good surprises.")), 

                Trait(_("Brisk"), verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.5), eff2 = Effect("boost", "dancer jp gains", 0.25), eff3 = Effect("boost", "tip", 0.05), archetype="The Player", base_description = __("She's quick and lively.")),

                Trait(_("Rowdy"), verb = "be", effects = [Effect("boost", "waitress jp gains", 0.5), Effect("increase satisfaction", "waitress", 1, chance=0.5), Effect("increase satisfaction", "geisha", -2)], opposite=['Modest', 'Unhurried'], archetype="The Player", base_description = __("She likes it when things are a bit chaotic.")),
                Trait(_("Powerful"), verb = "be", effects = [Effect("boost", "dancer jp gains", 0.5), Effect("increase satisfaction", "dancer", 1, chance=0.5), Effect("increase satisfaction", "masseuse", -2), Effect("change", "defense", 1)], opposite=['Modest', 'Unhurried'], archetype="The Bride", base_description = __("She tends to underestimate her own strength.")),
                Trait(_("Unhurried"), verb = "be", effects = [Effect("boost", "masseuse jp gains", 0.5), Effect("increase satisfaction", "masseuse", 1, chance=0.5), Effect("increase satisfaction", "waitress", -2)], opposite=['Powerful', 'Rowdy'], archetype="The Escort", base_description = __("She can give you all of her attention.")),
                Trait(_("Modest"), verb = "be", effects = [Effect("boost", "geisha jp gains", 0.5), Effect("increase satisfaction", "geisha", 1, chance=0.5), Effect("increase satisfaction", "dancer", -2), Effect("personality", "meek")], opposite=['Rowdy', 'Powerful'], archetype="The Fox", base_description = __("An air of decency surrounds her.")),

                Trait(_("Pervert"), verb = "be a", effects = [Effect("change", "sex act requirements", -30), Effect("personality", "pervert"), Effect("change", "valuation", +20)], archetype="The Slut", base_description = __("She can't stop thinking about sex.")),

                # Trait King originals

                Trait(_("Sexually curious"), verb = "be", effects = [Effect("boost", "service jp gains", 0.5), Effect("boost", "sex jp gains", 0.5), Effect("change", "all sex skills", 10), Effect("change", "valuation", +40)], archetype="The Escort", base_description = __("She likes to gain more experiences in the bedroom.")),

                Trait(_("Dedicated"), verb="be", eff1=Effect("change", "job obedience target", -50), eff2=Effect("change", "valuation", +10, scales_with = "rank"), archetype="The Maid", base_description = __("She likes to make herself useful.")),
                Trait(_("Open-minded"), verb = "be", effects = [Effect("change", "sex act requirements", -50), Effect("boost", "anal jp gains", 0.5), Effect("boost", "fetish jp gains", 0.5)], archetype="The Escort", base_description = __("She is not quick to judge others and open to new experiences.")),

                Trait(_("Fast Orgasms"), verb = "be", effects = [Effect("boost", "libido gains", 1.0), Effect("increase satisfaction", "sex", 1), Effect("increase satisfaction", "group", 1), Effect("boost", "tiredness", 0.2)], archetype="The Slut", base_description = __("She reaches climax very easily.")),

                Trait(_("Housekeeper"), verb="be a", effects = [Effect("change", "obedience", 20), Effect("change", "maintenance", 2, scope="brothel")], archetype="The Maid", base_description = __("She enjoys doing household tasks.")),


        ]

        traitking_pos_c = [

                # Vanilla reworked

                Trait(_("Long legs"), verb = "have", eff1 = Effect("change", "body", 20), eff2 = Effect("gain", "reputation", 5), archetype="The Model", base_description = __("She has beautiful long legs.")),
                Trait(_("Sweet"), verb = "be", eff1 = Effect("change", "charm", 20), eff2 = Effect("gain", "reputation", 5), eff3 = Effect("personality", "sweet"), archetype="The Bride", base_description = __("She is just a very nice girl.")),
                Trait(_("Polite"), verb = "be", eff1 = Effect("change", "refinement", 20), eff2 = Effect("gain", "reputation", 5), archetype="The Courtesan", base_description = __("She has great manners.")),
                Trait(_("Resilient"), verb = "be", eff1 = Effect("change", "constitution", 20), archetype="The Maid", base_description = __("She seems to be a hardy girl.")),
                Trait(_("Delicate"), verb = "be", eff1 = Effect("change", "sensitivity", 20), eff2 = Effect("gain", "reputation", 5), archetype="The Bride", base_description = __("She revels in intimate physical contact.")),
                Trait(_("Meek"), verb = "be", eff1 = Effect("change", "obedience", 20), eff2 = Effect("personality", "meek"), archetype="The Maid", base_description = __("She is a gentle and docile girl.")),

                Trait(_("Fit"), verb = "be", eff1 = Effect("boost", "body gains", 1.0), eff2 = Effect("boost", "constitution gains", 0.5), eff3=Effect("change", "valuation", +20), archetype="The Player", base_description = __("She is a healthy girl.")),
                Trait(_("Charming"), verb = "be", eff1 = Effect("boost", "charm gains", 1.0), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +10), archetype="The Fox", base_description = __("She is pleasant to talk to.")),
                Trait(_("Elegant"), verb = "be", eff1 = Effect("boost", "refinement gains", 1.0), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +40), archetype="The Courtesan", base_description = __("She moves with grace.")),  

                Trait(_("Obedient"), verb = "be", eff1 = Effect("boost", "obedience gains", 1.0), eff2=Effect("change", "train obedience target", -20), eff3 = Effect("change", "obedience", 10), archetype="The Maid", base_description = __("She likes following orders.")),

                Trait(_("Tough"), verb = "be", eff1 = Effect("boost", "hurt", -0.5), archetype="The Maid", base_description = __("She recovers from injuries faster than most.")),

                Trait(_("Sexy"), verb = "be", eff1 = Effect("boost", "reputation gains", 0.5), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +40), archetype="The Escort", base_description = __("She is a hot piece of ass.")),
                Trait(_("Humble"), verb = "be", eff1 = Effect("boost", "upkeep", -0.5), archetype="The Maid", base_description = __("She is not concerned with living in luxury.")),

                Trait(_("Sharp"), verb = "be", eff1 = Effect("boost", "xp gains", 0.5), eff2 = Effect("personality", "nerd"), archetype="The Fox", base_description = __("She is quick-witted.")),
                Trait(_("Loyal"), verb = "be", eff1 = Effect("boost", "love", 0.5), eff2 = Effect("change", "obedience", 5, scales_with = "rank"), eff3=Effect("change", "valuation", +20), archetype="The Bride", base_description = __("She is faithful to her master.")),
                Trait(_("Brave"), verb = "be", eff1 = Effect("boost", "fear", -0.5), eff2 = Effect("change", "security", 1, scope = "brothel"), archetype="The Escort", base_description = __("She does not scare easily.")),

                Trait(_("Nimble"), verb = "be", effects = [Effect("boost", "dancer jp gains", 0.5), Effect("boost", "geisha jp gains", 0.25)], archetype="The Courtesan", base_description = __("She always stays on her feet.")),
                Trait(_("Soft skin"), verb = "have", eff1 = Effect("change", "beauty", 10), eff2 = Effect("change", "refinement", 10), archetype="The Courtesan", base_description = __("She has unblemished skin.")),

                Trait(_("Bright"), verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.25), eff2 = Effect("boost", "geisha jp gains", 0.5), archetype="The Fox", base_description = __("She has an uplifting outlook on life.")),
                Trait(_("Agile"), verb = "be", effects = [Effect("boost", "dancer jp gains", 0.5), Effect("boost", "masseuse jp gains", 0.25)], archetype="The Escort", base_description = __("She has great coordination.")),

                Trait(_("Thief"), verb = "be a", eff1 = Effect("special", "pickpocket", 1), eff2=Effect("change", "valuation", -25), eff3 = Effect("boost", "income", -0.01, scales_with = "rank"), archetype="The Fox", base_description = __("Customers tend to leave items in her possession.")),

                ### NEW IN 0.3
                Trait(_("Sane"), verb = "be", eff1 = Effect("change", "sanity loss", -1), archetype="The Courtesan", base_description = __("She is surprisingly stable mentally, unlike every other girl in Zan.")),
                Trait(_("Trusting"), verb = "be", eff1 = Effect("change", "fear per day", -1, chance=0.25), archetype="The Maid", base_description = __("She has no quams about meeting and befriending strangers.")),
                Trait(_("Loving"), verb = "be", eff1 = Effect("change", "love per day", 1, chance=0.25), archetype="The Bride", base_description = __("She has a big heart and accepts everyone for who they are.")),

                # Trait King originals

                Trait(_("Mind Fucked"), verb="be", effects = [Effect("change", "obedience", 250), Effect("change", "job obedience target", -250), Effect("change", "whore obedience target", -250), Effect("change", "train obedience target", -250), Effect("change", "all main skills", -15, scales_with="rank")], archetype="The Slut", base_description = __("She has been completely brainwashed and will never question her master's orders.")),

                Trait(_("Subservient"), verb = "be", effects=[Effect("boost", "obedience gains", 0.25), Effect("change", "train obedience target", -100), Effect("change", "tip", -10, scales_with="cust nb")], archetype="The Model", base_description = __("She enjoys serving her master and would prefer to be at his side and tending to his needs at all times.")), 

                Trait(_("Cum Addict"), verb="be a", effects = [Effect("boost", "service jp gains", 0.5), Effect("boost", "service preference increase", 0.2, scales_with = "rank")], archetype="The Slut", base_description = __("She prefers blowjobs over ice-cream smoothies.")),

                Trait(_("Innocent"), verb = "be", effects = [Effect("change", "charm", 10, scales_with = "rank"), Effect("change", "libido", -25), Effect("gain", "reputation", 10), Effect("change", "valuation", +20)], archetype="The Player", base_description = __("She is a pure and kindhearted girl.")),
                Trait(_("Great Figure"), verb = "have a", effects=[Effect("change", "body", 20), Effect("gain", "reputation", 10), Effect("change", "valuation", +10)], archetype="The Model", base_description = __("She has a lovely body.")), 
                Trait(_("Adorable"), verb = "be", effects = [Effect("change", "beauty", 20), Effect("boost", "max energy", -0.1), Effect("gain", "reputation", 10), Effect("change", "valuation", +5, scales_with = "rank")], archetype="The Model", base_description = __("She has a charm about her that makes you fall in love with her.")),

                Trait(_("for Public use"), verb="be", effects = [Effect("boost", "group chance", 0.25), Effect("boost", "tiredness", -0.25), Effect("boost", "tip", -0.15, scales_with="rank"), Effect("change", "whore obedience target", -100), Effect("increase satisfaction", "all jobs", -1)], archetype="The Slut", base_description = __("She wouldn't mind being used by everyone in the room.")),

                Trait(_("Beauty Mark"), verb="have a", effects = [Effect("change", "beauty", 20)], archetype="The Courtesan", base_description = __("She has a unique birthmark on her face.")),
                Trait(_("Tattoo"), verb="have a", effects = [Effect("change", "beauty", 10), Effect("change", "charm", 5)], archetype="The Slut", base_description = __("She has a nice tattoo. I won't tell where, that's for you to find out.")),
                Trait(_("Exotic Tattoo"), verb="have an", effects = [Effect("change", "beauty", 10), Effect("change", "charm", 10), Effect("change", "valuation", +40)], archetype="The Escort", base_description = __("She has a unique tattoo, one they only make in foreign lands.")),
                Trait(_("Pierced Clit"), verb="have a", effects = [Effect("boost", "sex preference increase", 0.2), Effect("change", "sensitivity", 10), Effect("change", "libido", 10)], archetype="The Slut", base_description = __("Her clitoris is pierced.")),
                Trait(_("Pierced Navel"), verb="have a", effects = [Effect("boost", "dancer jp gains", 0.5)], archetype="The Model", base_description = __("She likes to expose her midriff to show off her naval piercing.")),
                Trait(_("Pierced Nipples"), verb="have", effects = [Effect("boost", "service preference increase", 0.25), Effect("change", "sensitivity", 10), Effect("change", "libido", 10)], archetype="The Escort", base_description = __("Her nipples are pierced.")),

                Trait(_("Tomboy"), verb = "be a", effects = [Effect("change", "constitution", 30), Effect("change", "obedience", -20), Effect("change", "valuation", -20)], archetype="The Bride", base_description = __("She's an energetic girl with boyish hobbies.")),

        ]

        traitking_pos_special = [

                # Vanilla reworked

                Trait(_("Virgin"), verb = "be a", effects=[Effect("special", "virgin", 1), Effect("change", "sensitivity", 10), Effect("change", "sex act requirements", 40), Effect("gain", "reputation", 10, scales_with = "rank"), Effect("change", "valuation", +50, scales_with = "rank")], archetype="The Bride", base_description = __("She has never experienced vaginal intercourse.")), # Special trait, goes away after 1st sex

                # Trait King originals
                
                Trait(_("Unknown"), verb = "have an", eff1 = Effect("boost", "prestige", -0.25), base_description = __("This girl is hiding something from you."), public=False)

        ]

        traitking_pos_traits = traitking_pos_s + traitking_pos_a + traitking_pos_b + traitking_pos_c + traitking_pos_special
        

        ## NEGATIVE TRAITS
        
        traitking_neg_traits = [

                # Vanilla reworked 
                Trait(_("Plain"), verb = "be", eff1 = Effect("change", "beauty", -10, scales_with = "rank"), opposite = "Cute", base_description = __("She's a bit too ordinary.")),
                Trait(_("Scars"), verb = "have", eff1 = Effect("change", "body", -10, scales_with = "rank"), opposite = "Nice boobs", base_description = __("She has some nasty scars.")),
                Trait(_("Mean"), verb = "be", eff1 = Effect("change", "charm", -10, scales_with = "rank"), opposite = "Sweet", base_description = __("She can be a bit of a bitch.")),
                Trait(_("Rude"), verb = "be", eff1 = Effect("change", "refinement", -10, scales_with = "rank"), opposite = "Polite", base_description = __("She can be very impolite.")),
                Trait(_("Cold"), verb = "be", eff1 = Effect("change", "libido", -10, scales_with = "rank"), eff2 = Effect("personality", "cold"), opposite = "Horny", base_description = __("She doesn't like showing affection.")), # needs evolution desc
                Trait(_("Weak"), verb = "be", eff1 = Effect("change", "constitution", -10, scales_with = "rank"), eff2=Effect("change", "valuation", -20), opposite = "Resilient", base_description = __("She's a bit of a pushover.")),
                Trait(_("Rough"), verb = "be", eff1 = Effect("change", "sensitivity", -10, scales_with = "rank"), opposite = "Delicate", base_description = __("She doesn't consider other people's feelings.")),
                Trait(_("Defiant"), verb = "be", eff1 = Effect("change", "obedience", -10, scales_with = "rank"), eff2=Effect("change", "valuation", -40), opposite = "Meek", base_description = __("She doesn't always listen.")),
                
                Trait(_("Timid"), verb = "be", eff1 = Effect("boost", "charm gains", -0.5), opposite = "charming", base_description = __("She's a bit too passive.")),
                Trait(_("Plump"), verb = "be", eff1 = Effect("boost", "body gains", -0.5), opposite = "Fit", base_description = __("She's fat.")),
                Trait(_("Scruffy"), verb = "be", eff1 = Effect("boost", "beauty gains", -0.5), opposite = "Beautiful", base_description = __("She doesn't present herself well.")),
                Trait(_("Vulgar"), verb = "be", eff1 = Effect("boost", "refinement gains", -0.5), opposite = "Elegant", base_description = __("She can swear like a sailor.")),
                Trait(_("Tame"), verb = "be", eff1 = Effect("boost", "libido gains", -0.5), eff2=Effect("change", "valuation", -20), opposite = "Slutty", base_description = __("She's not very imaginative.")),
                Trait(_("Frail"), verb = "be", eff1 = Effect("boost", "constitution gains", -0.5), eff2=Effect("change", "valuation", -20), opposite = "Athletic", base_description = __("She's easily winded.")),
                Trait(_("Rebellious"), verb = "be", eff1 = Effect("boost", "obedience gains", -0.5), eff2 = Effect("personality", "rebel"), eff3=Effect("change", "valuation", -50), opposite = "Obedient", base_description = __("She likes to fight authority.")),
                Trait(_("Jaded"), verb = "be", eff1 = Effect("boost", "sensitivity gains", -0.5), eff2 = Effect("change", "valuation", -10, scales_with = "rank"), opposite = "Sensitive", base_description = __("She hates this job.")), # needs evolution desc
                
                Trait(_("Lazy"), verb = "be", eff1 = Effect("boost", "max energy", -0.20), opposite = ["Energetic", "Driven"], base_description = __("She would prefer to lie in bed all day.")),
                Trait(_("Sickly"), verb = "be", eff1 = Effect("boost", "hurt", +2), eff2=Effect("change", "valuation", -40), opposite = "Tough", base_description = __("She may have some disease.")), # needs evolution desc
                
                Trait(_("Homely"), verb = "be", eff1 = Effect("boost", "reputation gains", -0.25), opposite = "Sexy", base_description = __("She is not very attractive.")),
                Trait(_("Expensive"), verb = "be", eff1 = Effect("boost", "upkeep", 1.0), eff2=Effect("change", "valuation", +25), opposite = "Humble", base_description = __("She wants to be treated like a princess.")),
                Trait(_("Slow"), verb = "be", eff1 = Effect("boost", "xp gains", -0.5), eff2 = Effect("boost", "class results", -0.5), opposite = ["Fast learner", "Sharp", "Genius"], base_description = __("Her brain does not work as well as it should.")),
                Trait(_("Distrustful"), verb = "be", eff1 = Effect("boost", "love gains", -0.5), opposite = "Loyal", base_description = __("She's an independant girl.")),
                Trait(_("Fearful"), verb = "be", eff1 = Effect("boost", "fear", 0.5), opposite = "Brave", base_description = __("She's easily frightened.")),
                Trait(_("Vulnerable"), verb = "be", eff1 = Effect("change", "defense", -4), opposite = ["Strong", "Warrior"], base_description = __("She is an easy target.")),
                
                Trait(_("Unlucky"), verb = "be", eff1 = Effect("special", "unlucky", 1), base_description = __("She shouldn't have broken that magic mirror... She has some terrible luck."), opposite = "Lucky"),  # needs evolution desc
                
                Trait(_("All thumbs"), verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.5), eff2 = Effect("increase satisfaction", "waitress", -1), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy'], base_description = __("She's a bit useless.")),
                Trait(_("Awkward"), verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.5), eff2 = Effect("increase satisfaction", "dancer", -1), opposite=['Nimble', 'Agile', 'Brisk', 'Powerful'], base_description = __("She lacks tact.")),
                Trait(_("Brutal"), verb = "be", eff1 = Effect("boost", "masseuse jp gains", -0.5), eff2 = Effect("increase satisfaction", "masseuse", -1), opposite=['Deft', 'Soft skin', 'Agile', 'Unhurried'], base_description = __("She underestimates her own strength.")),
                Trait(_("Dumb"), verb = "be", effects = [Effect("boost", "geisha jp gains", -0.5), Effect("increase satisfaction", "geisha", -1), Effect("boost", "jp gains", -0.5)], opposite=['Nimble', 'Soft skin', 'Bright', 'Modest'], base_description = __("She's stupid.")),
                Trait(_("Oafish"), verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.5), eff2 = Effect("boost", "geisha jp gains", -0.5), opposite=['Nimble', 'Agile', 'Brisk', 'Soft skin', 'Bright'], base_description = __("She lacks manners and grace.")),
                Trait(_("Clumsy"), verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.5), eff2 = Effect("boost", "masseuse jp gains", -0.5), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy', 'Soft skin', 'Agile'], base_description = __("She lacks basic coordination.")),
                
                Trait(_("Prude"), verb = "be", eff1 = Effect("boost", "service jp gains", -0.5), eff2 = Effect("boost", "sex jp gains", -0.5), eff3=Effect("change", "valuation", -25), opposite = "Naughty", base_description = __("She lacks sexual desire.")),
                Trait(_("Naive"), verb = "be", eff1 = Effect("boost", "anal jp gains", -0.5), eff2 = Effect("boost", "fetish jp gains", -0.5), eff3=Effect("change", "valuation", +10), opposite = "Kinky", base_description = __("She does not do the weird stuff.")),
                Trait(_("Square"), verb = "be", eff1 = Effect("change", "sex act requirements", 50), opposite = "Pervert", base_description = __("She's not very adventurous.")),

                ### NEW IN 0.3
                Trait(_("Insane"), verb = "be", eff1 = Effect("change", "sanity loss", 1), opposite = "Sane", base_description = __("She's mentally deranged.")),

                Trait("Distrustful", verb = "be", eff1 = Effect("change", "fear per day", 1, chance=0.25), opposite = "Trusting", base_description = "She's unable to trust anyone."),
                Trait("Spiteful", verb = "be", eff1 = Effect("change", "love per day", -1, chance=0.25), opposite = "Loving", base_description = "She has an insatiable desire to hurt those around her."),

                Trait("Earthbound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = "Will not attack you. Deadly to everyone else.", public=False),
                Trait("Waterbound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = "Will not attack you. Deadly to everyone else.", public=False),
                Trait("Voidbound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = "Will not attack you. Deadly to everyone else.", public=False),
                Trait("Firebound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = "Will not attack you. Deadly to everyone else.", public=False),

                # Trait King originals

                Trait(_("Slave Brand"), verb="have a", effects = [Effect("boost", "prestige", 1), Effect("change", "valuation", -100)], archetype="The Bride", base_description = __("She has a tattoo that says {i}'Property of Kosmo. If found, please return to rightful owner.'{/i}.")), 
                Trait(_("Lesbian"), verb = "be a", eff1=Effect("increase satisfaction", "all sex acts", -1), eff2=Effect("increase satisfaction", "bisexual", 2), archetype="The Courtesan", base_description = __("She does not get aroused by men.")), 
                
                Trait(_("City girl"), verb="be a", eff1=Effect("boost", "farm preference increase", -1.0), eff2=Effect("change", "valuation", +40), archetype="The Escort", base_description = __("Living in the city is all she knows. She would despise living in the countryside.")), 
                Trait(_("Circumcised"), verb = "be", effects = [Effect("change", "libido", -50), Effect("change", "sensitivity", -50), Effect("change", "whore obedience target", 100), Effect("change", "valuation", -60)], base_description = __("Her genitalia have been mutilated.")),  
                Trait(_("Deceitful"), verb = "be", eff1=Effect("boost", "income", -0.01, scales_with = "rank"), eff2=Effect("change", "valuation", +25), base_description = __("She only cares about herself.")), 
                Trait(_("Inbred"), verb = "be an", eff1 = Effect("boost", "love", 0.5), eff2 = Effect("boost", "all jp gains", -0.5), eff3=Effect("change", "valuation", -60), base_description = __("Her father and mother were closely related by blood.")), 
                Trait(_("Depressed"), verb="be", eff1=Effect("change", "mood", -4), eff2=Effect("boost", "tiredness", 0.2), eff3=Effect("change", "valuation", -50), base_description = __("She gains no joy from life.")), 

                Trait(_("Chaste"), verb = "be", eff1 = Effect("change", "sex act requirements", 50), eff2 = Effect("change", "whore obedience target", 50), eff3=Effect("change", "valuation", -40), opposite = "Pervert", base_description = __("She thinks sex outside of marriage is immoral.")), 
                Trait(_("Disfigured"), verb = "be", eff1 = Effect("boost", "naked bonus", -0.25), eff2 = Effect("change", "beauty", -10, scales_with = "rank"), eff3=Effect("change", "valuation", -50), opposite = "Nice boobs", base_description = __("She has been in a nasty accident.")),

                Trait(_("Drunkard"), verb="be a", eff1=Effect("change", "obedience", -10, scales_with = "rank"), eff2= Effect("boost", "reputation gains", -0.25), eff3=Effect("change", "valuation", -30), base_description = __("She likes drinking herself into a stupor.")), 
                # Trait(_("Kidnapped"), verb = "be", eff1=Effect("change", "obedience", -40), eff2 = Effect("personality", "rebel"), eff3=Effect("change", "valuation", -20), base_description = __("She was kidnapped and desires to go home.")), # needs evolution desc

                Trait(_("Frigid"), verb = "be", eff1 = Effect("change", "libido", -10, scales_with = "rank"), eff2 = Effect("personality", "cold"), eff3=Effect("change", "valuation", -10, scales_with = "rank"), opposite = "Horny", base_description = __("She hates showing affection.")), 
                Trait(_("Asexual"), verb = "be", effects = [Effect("change", "libido", -50), Effect("change", "valuation", -50), Effect("increase satisfaction", "all sex acts", -1)], opposite = "Pervert", base_description = __("She has little to no interest in intimacy.")), 

                Trait(_("Dull"), verb = "be", eff1 = Effect("special", "effect chance", -0.5), opposite = ["Brisk", "Energetic", "Wild"], base_description = __("Nothing interesting ever happens to her.")),
                Trait(_("Gluttonous"), verb = "be", eff1 = Effect("change", "constitution", -30), eff2=Effect("change", "valuation", -5, scales_with = "rank"), base_description = __("She likes eating a bit too much.")),
                Trait(_("Uncouth"), verb="be", eff1=Effect("change", "refinement", -40), eff2= Effect("boost", "reputation gains", -0.1), opposite = "Groomed", base_description = __("She has absolutely no manners.")),
                Trait(_("Deaf"), verb = "be", eff1 = Effect("change", "obedience", -20), eff2 = Effect("boost", "waitress jp gains", -0.5), eff3=Effect("change", "valuation", -20), base_description = __("She's hard of hearing.")),
 
                Trait(_("Paranoid"), verb = "be", effects=[Effect("boost", "fear gains", 2.0), Effect("change", "defense", 1), Effect("boost", "love gains", -0.25)], base_description = __("She thinks someone's out to get her.")),
                Trait(_("Strong Gag Reflex"), verb = "have a", eff1 = Effect("increase satisfaction", "service", -1), base_description = __("She has vomited and choked on plenty of dicks.")),

                Trait(_("Arrogant"), verb = "be", eff1 = Effect("boost", "all jp gains", -0.5), opposite = "Humble", base_description = __("She mistakenly thinks the world revolves around her.")),
                Trait(_("Stubborn"), verb = "be", eff1 = Effect("boost", "xp gains", -0.25), eff2 = Effect("boost", "all jp gains", -0.25 ), base_description = __("She does not listen to advice.")),
                Trait(_("Blind"), verb = "be", eff1 = Effect("change", "defense", -4), eff2 = Effect("change", "sensitivity", 10), eff3=Effect("change", "valuation", -20), base_description = __("Her eyes don't work very well.")),
                Trait(_("Greedy"), verb = "be", eff1 = Effect("boost", "upkeep", 2), eff2 = Effect("special", "random item", 1, chance=0.02), opposite = "Humble", base_description = __("She demands more than her fair share.")),

                Trait(_("Bloodslut"), verb = "be a", effects=[Effect("change", "whore obedience target", -250), Effect("change", "valuation", -20, scales_with = "rank"), Effect("change", "brothel reputation", -10, scales_with = "rank", chance=0.1, scope="brothel"), Effect("change", "customers", -2, scales_with = "rank", scope="brothel"), Effect("personality", "creep")], opposite = "Virgin", base_description = __("She is discriminated against because she has served time as a meatsleeve on the Blood Islands.")), 
                Trait(_("Half-elf"), verb = "be a", effects=[Effect("boost", "tiredness", -0.1), Effect("boost", "perfect result tip", -0.75)], base_description = __("She is discriminated against because she has elven blood running through her veins.")), 
                Trait(_("Monsterkin"), verb = "be a", effects=[Effect("special", "immune", 1), Effect("change", "security", -1, scales_with = "rank", scope = "brothel"), Effect("change", "valuation", -10, scales_with = "rank")], base_description = __("She is discriminated against because people believe she was birthed by a monster.")), 
                Trait(_("Vivified"), verb = "be", effects=[Effect("change", "constitution", -15, scales_with = "rank"), Effect("change", "valuation", +100)], base_description = __("People believe that she is an unnatural being, conjured up by a magician.")), 
                
                # ? - Desert Pox (debilitating disease with expensive spice addiction)
                

        ]

        traitking_neg_evolved_desc = {  
                    # Evolved negative traits, must contain options for all negative traits
                    # Description:  She tells you that she really wants to try to [text1]
                    # training:       (menu item)

                   "Godless description" : __("stop being a godless heathen."),
                   "Godless training" : __("Worship a God"),
                   "Godless intro" : __("You educate her on the teachings and virtues of Shalia and Arios."),
                   "Godless pos_reaction" : __("She comprehends that her life is lived in service of a greater power and starts confessing her sins."),
                   "Godless neg_reaction" : __("She is very confused about how the scriptures contradict themselves all over the place."),
                   "Godless pic" : "geisha",
                   "Godless and_tag" : "study",
                   
                   "Trauma description" : __("overcome her trauma."),
                   "Trauma training" : __("Overcome trauma"),
                   "Trauma intro" : __("The two of you talk at length about her childhood, to eventually lead into talking about her defloration."),
                   "Trauma pos_reaction" : __("She vividly describes her memories of the event and gains a better understanding of her reaction towards it."),
                   "Trauma neg_reaction" : __("She breaks down and starts crying uncontrollably."),
                   "Trauma pic" : "rest",
                   "Trauma and_tag" : "profile",
                   
                   "Dull description" : __("be a bit more adventurous."),
                   "Dull training" : __("Experience exciting things"),
                   "Dull intro" : __("You walk around the streets of Zan together, deliberately wandering into dangerous corridors and side-streets you'd normally never explore."),
                   "Dull pos_reaction" : __("She enjoys the outing tremendously and has plenty of new stories to tell about what she has seen."),
                   "Dull neg_reaction" : __("She absolutely hates it and is disturbed by the things you happen to stumble upon. She longs for the safety of her own bedroom."),
                   "Dull pic" : "town",
                   "Dull and_tag" : "profile",
                   
                   "Mean description" : __("stop being such a cunt."),
                   "Mean training" : __("Cultivate kindness"),
                   "Mean intro" : __("You tell her to compliment Sill."),
                   "Mean pos_reaction" : __("She praises Sill for her great work and devotion towards the brothel."),
                   "Mean neg_reaction" : __("She delivers a vicious backhanded compliment to Sill."),
                   "Mean pic" : "profile",
                   "Mean and_tag" : "",
                   
                   "Scars description" : __("improve her body image."),
                   "Scars training" : __("Strike poses in the mirror"),
                   "Scars intro" : __("You bring her in front of a big standing mirror and instruct her to mimic your actions as you start acting out various heroic poses."),
                   "Scars pos_reaction" : __("She gets very excited by this game and even starts inventing new poses on the spot, daring you to follow her lead."),
                   "Scars neg_reaction" : __("She can't overcome her embarassement about her scars and is unable to mimic your body language."),
                   "Scars pic" : "naked",
                   "Scars and_tag" : "profile",
                   
                   "Plain description" : __("be more unique."),
                   "Plain training" : __("Invite more attention"),
                   "Plain intro" : __("You order her to dress up and take a walk around the neighborhood while loudly singing hymns."),
                   "Plain pos_reaction" : __("She puts on her outfit and does as you asked. She loves being the center of attention and starts singing louder and louder."),
                   "Plain neg_reaction" : __("She dresses up and walks around, but can't bring herself to loudly sing hymns because she is too afraid to stand out."),
                   "Plain pic" : "cosplay",
                   "Plain and_tag" : "sing",
                   
                   "Rude description" : __("stop being such a bitch."),
                   "Rude training" : __("Cultivate respect"),
                   "Rude intro" : __("You order her to kneel down and lick your feet."),
                   "Rude pos_reaction" : __("She complies with your order, but can't help herself and takes a few jabs at you for requesting to have your feet licked."),
                   "Rude neg_reaction" : __("She refuses to do as you ask and hurls insults at you."),
                   "Rude pic" : "profile",
                   "Rude and_tag" : "sub",

                   "Rough description" : __("act like a proper lady."),
                   "Rough training" : __("Host a formal dinner"),
                   "Rough intro" : __("You host a formal dinner, giving her a seat at the table with delegates from all the major guilds."),
                   "Rough pos_reaction" : __("She has a lovely evening and somehow manages not to upset any of your guests."),
                   "Rough neg_reaction" : __("She accidentally upsets one of the delegates by telling an obscene joke."),
                   "Rough pic" : "geisha",
                   "Rough and_tag" : "",

                   "Weak description" : __("stand up for herself."),
                   "Weak training" : __("Train for a fight"),
                   "Weak intro" : __("You arrange for her to recieve one-on-one training from one of the gladiators in the arena."),
                   "Weak pos_reaction" : __("She trains hard to improve her methods of self-defense and picks up a few new tricks."),
                   "Weak neg_reaction" : __("She spends more time shrieking and crying than actually training."),
                   "Weak pic" : "fight",
                   "Weak and_tag" : "",

                   "Defiant description" : __("be more compliant."),
                   "Defiant training" : __("Rearrange the bookshelf"),
                   "Defiant intro" : __("You order her to rearrange your collection of books in alphabetical order."),
                   "Defiant pos_reaction" : __("She begrudgingly follows your orders."),
                   "Defiant neg_reaction" : __("She refuses to busy herself with such a mundane task."),
                   "Defiant pic" : "profile",
                   "Defiant and_tag" : "",

                   "Gluttonous description" : __("stop eating like a pig."),
                   "Gluttonous training" : __("Organise a feast"),
                   "Gluttonous intro" : __("You prepare a table filled with lavish meals to test the girl's self-control, warning her that she will recieve the whip for every bite she dares to take."),
                   "Gluttonous pos_reaction" : __("She manages to restrain herself and doesn't dare to come near any of the food."),
                   "Gluttonous neg_reaction" : __("She pigs out despite your warning. True to your word, you spend the rest of the night punishing her."),
                   "Gluttonous pic" : "obedience",
                   "Gluttonous and_tag" : "profile",

                   "Uncouth description" : __("be groomed."),
                   "Uncouth training" : __("Visit a festival"),
                   "Uncouth intro" : __("You visit a festival together in order to learn more about local customs and traditions."),
                   "Uncouth pos_reaction" : __("She behaves well and manages not to make a scene."),
                   "Uncouth neg_reaction" : __("She feels uncomfortable in her kimono and decides to undo it halfway through the festival. The other visitors stare as she plays traditional festival games in the nude."),
                   "Uncouth pic" : "kimono",
                   "Uncouth and_tag" : "naked",

                   "Deaf description" : __("listen."),
                   "Deaf training" : __("Fetch groceries"),
                   "Deaf intro" : __("You recite a list of groceries, ordering her to memorise and purchase them at the market."),
                   "Deaf pos_reaction" : __("She comes back from the market with most of the items you requested."),
                   "Deaf neg_reaction" : __("She comes back from the market with sandals, a bottle of lube and fishnet stockings, none of which were on your list."),
                   "Deaf pic" : "profile",
                   "Deaf and_tag" : "",

                   "Timid description" : __("be more outgoing."),
                   "Timid training" : __("Deliver a toast"),
                   "Timid intro" : __("Before supper, you order all your girls to listen to her as she delivers a toast."),
                   "Timid pos_reaction" : __("She keeps it short and sweet, toasting on the bright future of the brothel."),
                   "Timid neg_reaction" : __("She quietly says a few words, but is unable to hold the attention of the girls."),
                   "Timid pic" : "profile",
                   "Timid and_tag" : "",

                   "Plump description" : __("lose some weight."),
                   "Plump training" : __("Exercise"),
                   "Plump intro" : __("You order her to start running laps around the brothel."),
                   "Plump pos_reaction" : __("She starts running and wheezing immediately and does not stop until you tell her to."),
                   "Plump neg_reaction" : __("She starts running immediately, but falls flat on her face after two laps and is unable to get back up due to exhaustion."),
                   "Plump pic" : "constitution",
                   "Plump and_tag" : "",
                   
                   "Scruffy description" : __("invest more time in improving her appearance."),
                   "Scruffy training" : __("Apply cosmetics"),
                   "Scruffy intro" : __("You suggest that she should try spending some time dolling herself up in front of the mirror."),
                   "Scruffy pos_reaction" : __("She spends hours trying to accentuate her best features in front of the mirror."),
                   "Scruffy neg_reaction" : __("She returns ten minutes later, defaced by the most unholy combination of lipstick, mascara and eye shadow you have ever seen."),
                   "Scruffy pic" : "portrait",
                   "Scruffy and_tag" : "",

                   "Vulgar description" : __("expand her... her words... Vocabulary!"),
                   "Vulgar training" : __("Read a dictionary"),
                   "Vulgar intro" : __("You give her a dictionary and order her to learn five new words that start with the letter C."),
                   "Vulgar pos_reaction" : __("She studies the dictionary with great interest and even manages to introduce you to a new word: Cacidrosis! You immediately forget its definition."),
                   "Vulgar neg_reaction" : __("She misremembers your instructions and spends her time looking up five words she already knows: Cunt. Cock. Cum. Clit. Cunnilingus."),
                   "Vulgar pic" : "profile",
                   "Vulgar and_tag" : "",           

                   "Tame description" : __("be more daring."),
                   "Tame training" : __("Go streaking"),
                   "Tame intro" : __("You order her to run through the market in the nude."),
                   "Tame pos_reaction" : __("She gathers some courage and complies with your request, even though she is clearly very embarrassed by it."),
                   "Tame neg_reaction" : __("She chickens out two seconds into the dare and runs towards a fabrics stall to cover her nakedness."),   
                   "Tame pic" : "constitution",
                   "Tame and_tag" : "naked",

                   "Frail description" : __("defend herself."),
                   "Frail training" : __("Throw a punch"),
                   "Frail intro" : __("You instruct her to fend off Sill, while ordering Sill to play the part of a handsey drunk customer."),
                   "Frail pos_reaction" : __("She gets fondled a bit and then punches Sill right in the balls!"),
                   "Frail neg_reaction" : __("She is unable to stand her ground as Sill pounces on her and thorougly fondles and gropes her."), 
                   "Frail pic" : "lesbian",
                   "Frail and_tag" : "fondle",

                   "Rebellious description" : __("follow your lead."),
                   "Rebellious training" : __("Go on a date"),
                   "Rebellious intro" : __("You bring her along to a fancy lunchroom frequented by nobility."),
                   "Rebellious pos_reaction" : __("Afraid of breaching etiquette, she attempts to fit in by closely following your example."),
                   "Rebellious neg_reaction" : __("She is unfamiliar with everything on the menu and asks if they also serve 'grub'. She threatens to fight the chef when he asks her to clarify her request."), 
                   "Rebellious pic" : "geisha",
                   "Rebellious and_tag" : "",
                   
                   "Distrustful description" : __("trust your judgement."),
                   "Distrustful training" : __("Trust building exercise"),
                   "Distrustful intro" : __("You stand behind her and tell her to let herself fall backwards into your arms."),
                   "Distrustful pos_reaction" : __("She's scared to relinquish control, but eventually closes her eyes lets herself fall. You catch her ofcourse."),
                   "Distrustful neg_reaction" : __("She closes her eyes and leans backwards, but panics and attempts to regain her footing halfway through the fall. As a result you are unable to catch her and she makes a nasty smack on the floor."), 
                   "Distrustful pic" : "profile",
                   "Distrustful and_tag" : "",

                   "Fearful description" : __("be more courageous."),
                   "Fearful training" : __("Horror stories"),
                   "Fearful intro" : __("You take her along on an evening stroll through the cemetary. During the walk you start telling horror stories."),
                   "Fearful pos_reaction" : __("She is extremely scared and clings closely to your body, but manages to preservere in the end."),
                   "Fearful neg_reaction" : __("She is trembling and sweating throughout the walk and then faints when you get to the scariest part of the story."), 
                   "Fearful pic" : "profile",
                   "Fearful and_tag" : "",

                   "Paranoid description" : __("stop the government from poisoning the water supply."),
                   "Paranoid training" : __("Go on a secret mission"),
                   "Paranoid intro" : __("You feign interest in her consipiracy theories. The two of you depart on an adventure to stop the government from poisoning the water supply."),
                   "Paranoid pos_reaction" : __("She is unable to undo government's evil machinations, but you have a great time together and her trust in you has grown."),
                   "Paranoid neg_reaction" : __("She accidentally falls into the water supply and becomes completely preocuppied with mentally resisting the government's enchantments."), 
                   "Paranoid pic" : "profile",
                   "Paranoid and_tag" : "wet",

                   "Homely description" : __("dress more provocatively."),
                   "Homely training" : __("Fashion show"),
                   "Homely intro" : __("You give her multiple bikini's that would best accentuate her features and tell her to put on a fashion show for you."),
                   "Homely pos_reaction" : __("She has a lot of fun walking back and forth in different types of revealing swimwear. For her last outfit she comes out of the dressing room completely in the nude, overflowing with confidence."),
                   "Homely neg_reaction" : __("She is a lousy model with terrible posture. You are unable to enjoy the show and decide to leave halfway through."), 
                   "Homely pic" : "swim",
                   "Homely and_tag" : "",

                   "Prude description" : __("have a more liberal disposition towards sexual intercourse."),
                   "Prude training" : __("Have an orgy"),
                   "Prude intro" : __("You throw her to the wolves by offering her services free of charge towards your security guards."),
                   "Prude pos_reaction" : __("She screams wildly as she both her front and back holes are secured by the security guards. She is clearly not accustomed to it, but enjoys it all the same."),
                   "Prude neg_reaction" : __("She enjoys the foreplay, but becomes very upset when they suddenly start penetrating her in both holes."), 
                   "Prude pic" : "group",
                   "Prude and_tag" : "double",

                   "Naive description" : __("try playing with toys and machines."),
                   "Naive training" : __("Go to Gizel's workshop"),
                   "Naive intro" : __("You explain the workings of various machines in Gizel's workshop to her. Eventually she picks one and you start preparing it for use."),
                   "Naive pos_reaction" : __("She shakes with a massive orgasm as the machine does its work. You decide to leave her strapped onto it for a few hours."),
                   "Naive neg_reaction" : __("She can't get in the mood while being surrounded by Gizel's bizarre sex toys and is unable to climax."), 
                   "Naive pic" : "machine",
                   "Naive and_tag" : "toy",

                   "Square description" : __("attract younger clients."),
                   "Square training" : __("Public exposure"),
                   "Square intro" : __("You suggest that she should flash her goods to younger men in public."),
                   "Square pos_reaction" : __("She walks around town and exposes herself to a younger audience, whose loins are immediately filled with desire. She becomes just as turned on by the exhibitionism herself."),
                   "Square neg_reaction" : __("She feels too embarrassed to immediately expose herself and instead tries to lead into it with a conversation. The men seem disinterested."), 
                   "Square pic" : "public",
                   "Square and_tag" : "naked",

                   "Strong Gag Reflex description" : __("stop gagging and vomiting on massive cocks."),
                   "Strong Gag Reflex training" : __("Bring out the massive cocks!"),
                   "Strong Gag Reflex intro" : __("You bring her to your stable where the stallions are willing and able to fuck her mouth until it becomes numb."),
                   "Strong Gag Reflex pos_reaction" : __("Instead of gagging, she nearly chokes on the massive cock and the lack of oxygen heightens her own orgasms."),
                   "Strong Gag Reflex neg_reaction" : __("She can't help herself and eventually starts puking all over their massive cocks."), 
                   "Strong Gag Reflex pic" : "big",
                   "Strong Gag Reflex and_tag" : "oral",

                   "All thumbs description" : __("make herself more useful."),
                   "All thumbs training" : __("Clean the brothel"),
                   "All thumbs intro" : __("You tell her to do some housekeeping for the brothel."),
                   "All thumbs pos_reaction" : __("She does what she can and manages to clean her bedroom."),
                   "All thumbs neg_reaction" : __("She manages to break a few things and create more of a mess than when she started."), 
                   "All thumbs pic" : "maid",
                   "All thumbs and_tag" : "obedience",

                   "Awkward description" : __("feel more comfortable on stage."),
                   "Awkward training" : __("Dance on stage"),
                   "Awkward intro" : __("You tell her that the best way to learn is by confronting your fears and giving it a try."),
                   "Awkward pos_reaction" : __("She manages to hide her anxiety and perform a captivating dance routine on stage."),
                   "Awkward neg_reaction" : __("She remains very nervous and eventually stumbles and falls while performing her dance routine."), 
                   "Awkward pic" : "dancer",
                   "Awkward and_tag" : "",

                   "Brutal description" : __("test her strength."),
                   "Brutal training" : __("Armwrestling competition"),
                   "Brutal intro" : __("You decide to arrange an armwrestling competition between her and your security guards."),
                   "Brutal pos_reaction" : __("She has a lot of fun trying to beat the security guards."),
                   "Brutal neg_reaction" : __("The game abruptly comes to a halt as she manages to break the arm of one of the security guards."), 
                   "Brutal pic" : "fight",
                   "Brutal and_tag" : "",

                   "Dumb description" : __("tell a clever joke."),
                   "Dumb training" : __("Tell a joke"),
                   "Dumb intro" : __("You tell her to give it her best shot."),
                   "Dumb pos_reaction" : __("She tells you a joke: '{i}") + rand_choice(jokes["harmless"]) + "{/i}'",
                   "Dumb neg_reaction" : __("She tells a joke she must've heard somewhere else, but butchers the delivery: '{i}") + rand_choice(jokes["mean"]) + "{/i}'", 
                   "Dumb pic" : "profile",
                   "Dumb and_tag" : "",

                   "Oafish description" : __("reach a more cultured audience."),
                   "Oafish training" : __("Talk politics"),
                   "Oafish intro" : __("You ask her what she thinks about the King's foreign policy."),
                   "Oafish pos_reaction" : __("She admits to her own ignorance, but proceeds to genuinely reflect on ways in which exotics enrich our culture."),
                   "Oafish neg_reaction" : __("She clearly doesn't have a clue and attempts to answer your question by making something up about the King's whoring policy."), 
                   "Oafish pic" : "geisha",
                   "Oafish and_tag" : "",

                   "Clumsy description" : __("turn her clumsiness into a strength by becoming a jester."),
                   "Clumsy training" : __("Perform as a jester"),
                   "Clumsy intro" : __("You give her the go-ahead to perform on stage as a jester."),
                   "Clumsy pos_reaction" : __("She trips over as soon as she climbs on stage and everyone thinks it's hilarious."),
                   "Clumsy neg_reaction" : __("She somehow manages to hide her clumsiness. Unfortunately it makes her performance atrocious as this takes all the fun out of her jester routine."), 
                   "Clumsy pic" : "cosplay",
                   "Clumsy and_tag" : "dancer",

                   "Slow description" : __("be more alert."),
                   "Slow training" : __("Train with the guards"),
                   "Slow intro" : __("You give her permission to train with the guards."),
                   "Slow pos_reaction" : __("She manages to improve her reaction time by training with the guards."),
                   "Slow neg_reaction" : __("She's too slow to keep up with the guards and is quickly overpowered in most training situations."), 
                   "Slow pic" : "fight",
                   "Slow and_tag" : "",

                   "Arrogant description" : __("be more humble."),
                   "Arrogant training" : __("Self-reflection"),
                   "Arrogant intro" : __("You ask her to briefly describe her biggest shortcomings."),
                   "Arrogant pos_reaction" : __("She describes herself with surprising accuracy and even mentions that because of her arrogance she finds it difficult to improve herself."),
                   "Arrogant neg_reaction" : __("She thinks about it for a long, then says that she's simply too good at everything and makes everyone around her look terrible by comparison."), 
                   "Arrogant pic" : "profile",
                   "Arrogant and_tag" : "rest",

                   "Stubborn description" : __("become a famous gladiator."),
                   "Stubborn training" : __("Visit the arena"),
                   "Stubborn intro" : __("You allow her to visit the arena and chat with one of the gladiators. He offers to arrange a sparring match."),
                   "Stubborn pos_reaction" : __("She gets her ass whooped and starts doubting her ideas about becoming a famous gladiator."),
                   "Stubborn neg_reaction" : __("She is demoloshed in the ring, but too stubborn to give up her ideas of becoming a famous gladiator."), 
                   "Stubborn pic" : "hurt",
                   "Stubborn and_tag" : "fight",

                   "Lazy description" : __("try harder."),
                   "Lazy training" : __("Strict training regimen"),
                   "Lazy intro" : __("You create a strict training regimen for her, so she can make an effort to improve herself."),
                   "Lazy pos_reaction" : __("She starts training immediately and puts a lot of effort into it, but clearly gains no enjoyment from working on her fitness."),
                   "Lazy neg_reaction" : __("She lacks the determination to stick to your strict regimen and gives up partway through."), 
                   "Lazy pic" : "constitution",
                   "Lazy and_tag" : "",

                   "Blind description" : __("improve her eyesight."),
                   "Blind training" : __("See a specialist"),
                   "Blind intro" : __("You take her to a wizard that specialises in healing magics, who attempts to cure her blindness through the use of a spell."),
                   "Blind pos_reaction" : __("She miraculously regains some of her vision. However, she is way off the mark when ask her how many fingers you're holding up."),
                   "Blind neg_reaction" : __("She is still blind as a bat."), 
                   "Blind pic" : "portrait",
                   "Blind and_tag" : "",

                   "Vulnerable description" : __("expose herself to less danger."),
                   "Vulnerable training" : __("Work as a nurse"),
                   "Vulnerable intro" : __("You suggest that she could try working in a safer environment, caring for the elderly."),
                   "Vulnerable pos_reaction" : __("She absolutely loves her job as a nurse, but seems especially interested in attending to mentally unstable individuals."),
                   "Vulnerable neg_reaction" : __("She starts a fistfight with one of her clients after he dares to suggests that whoring is immoral."), 
                   "Vulnerable pic" : "masseuse",
                   "Vulnerable and_tag" : "cosplay",

                   "Expensive description" : __("prove she deserves a raise."),
                   "Expensive training" : __("Give her a challenge"),
                   "Expensive intro" : __("You suggest that if she is able to consistently milk all of Gizel's fiends within half an hour, she deserves a raise."),
                   "Expensive pos_reaction" : __("She puts forth a great effort and manages to satisfy the entire monster den within the set time limit. If she keeps this up, she might well deserve that raise."),
                   "Expensive neg_reaction" : __("She gives it her all and makes most of the monsters cum violently many times over, but is unable to milk the entire den within the time limit."), 
                   "Expensive pic" : "monster",
                   "Expensive and_tag" : "",

                   "Greedy description" : __("use her gold to improve the lives of the poor."),
                   "Greedy training" : __("Donate to the poorhouse"),
                   "Greedy intro" : __("You suggest that she could share her wealth with the poorhouse."),
                   "Greedy pos_reaction" : __("She agrees, donates a substantial amount of gold and even visits the poorhouse to lend a helping hand in the soup kitchen."),
                   "Greedy neg_reaction" : __("She agrees that the poorhouse is a great cause and pledges a token 5 gold. She can't stop bragging about her good deeds."), 
                   "Greedy pic" : "profile",
                   "Greedy and_tag" : "town",
                   
                   "Cold description" : __("have a tickle-fight."),
                   "Cold training" : __("TICKLE ATTACK!"),
                   "Cold intro" : __("You leap into action and start tickling her."),
                   "Cold pos_reaction" : __("She comfortably withstands your attacks with a smile on her face."),
                   "Cold neg_reaction" : __("You are unable to make her laugh. She responds to the physical intimacy with annoyed grunts."), 
                   "Cold pic" : "sensitivity",
                   "Cold and_tag" : "embar",

                   "Jaded description" : __("take it easy."),
                   "Jaded training" : __("Supervise the other girls"),
                   "Jaded intro" : __("You recommend that she practices taking on a supervisory role to support the younger girls."),
                   "Jaded pos_reaction" : __("The girls respond remarkably well to her guidance."),
                   "Jaded neg_reaction" :__( "Chaos ensues as the girls refuse to acknowledge her authority."), 
                   "Jaded pic" : "party",
                   "Jaded and_tag" : "bisexual",

                   "Sickly description" : __("write some poetry."),
                   "Sickly training" : __("Write a poem"),
                   "Sickly intro" : __("You suggest that she should write about her life."),
                   "Sickly pos_reaction" : __("She composes a poignant haiku about sickness and hardship. It brings a tear to your eyes."),
                   "Sickly neg_reaction" : __("She writes a crass limerick about a whore from some place called Nantucket. It's dreadfully dull."), 
                   "Sickly pic" : "study",
                   "Sickly and_tag" : "geisha",
                   
                   "Unlucky description" : __("overcome her bad luck."),
                   "Unlucky training" : __("Listen to motivational speech"),
                   "Unlucky intro" : __("You start delivering an intense inspirational monologue about persevering and not letting her dreams be dreams."),
                   "Unlucky pos_reaction" : __("She looks pumped and ready to challenge the Gods."),
                   "Unlucky neg_reaction" : __("She goes pale and keels over about halfway through your speech. Perhaps your delivery was a bit too intense."), 
                   "Unlucky pic" : "sensitivity",
                   "Unlucky and_tag" : "sub",
                   
                   "Slave Brand description" : __("vandalise Kosmo's brothel."),
                   "Slave Brand training" : __("Sneak into 'HʘʘKERS'"),
                   "Slave Brand intro" : __("You encourage her to infiltrate and vandalise Kosmo's brothel, 'HʘʘKERS'. She's hesitant at first, but after some convincing she accepts your challenge."),
                   "Slave Brand pos_reaction" : __("You distract the guards as she squirms through a window unnoticed. A while later she returns, boasting proudly that a pillow in the master bedroom has been decorated with her excrement."),
                   "Slave Brand neg_reaction" : __("You distract the guards, but she can't muster the courage to sneak into the establishment. You both decide to try again some other time."), 
                   "Slave Brand pic" : "town",
                   "Slave Brand and_tag" : "profile",
                   
                   "Lesbian description" : __("pleasure more women."),
                   "Lesbian training" : __("Ladies first"),
                   "Lesbian intro" : __("You invite a few of her female friends over and give them access to the brothel's collection of erotic toys."),
                   "Lesbian pos_reaction" : __("She confidently takes the lead and guides her friends towards multiple orgasms."),
                   "Lesbian neg_reaction" : __("The plan backfires when her friends insist that you should hang around and watch as they play. They bicker and fight for your attention."), 
                   "Lesbian pic" : "lesbian",
                   "Lesbian and_tag" : "toy",
                   
                   "City girl description" : __("explore the city."),
                   "City girl training" : __("Go on a date"),
                   "City girl intro" : __("You take her on a date to a high-class establishment near the Cathedra."),
                   "City girl pos_reaction" : __("The two of you have a great time as she enthousiastically shares all kinds of interesting anecdotes about her time in Zan."),
                   "City girl neg_reaction" : __("You quickly grow bored and disinterested as she yaps on and on about her life in the brothel."), 
                   "City girl pic" : "town",
                   "City girl and_tag" : "date",
                   
                   "Circumcised description" : __("pray at the Cathredra."),
                   "Circumcised training" : __("Go to the Cathedra"),
                   "Circumcised intro" : __("You light a candle for her and order her to take it to the Cathedra, to pray for Arios' blessing."),
                   "Circumcised pos_reaction" : __("She brings the candle to the Cathredra. As she returns to the brothel, she passionately proclaims that Arios has enkindled a flame in her heart."),
                   "Circumcised neg_reaction" : __("On her way towards the Cathedra a strong gust of wind extinguishes the candle's flame. She's inconsolable."), 
                   "Circumcised pic" : "ceremony",
                   "Circumcised and_tag" : "sub",
                   
                   "Deceitful description" : __("earn some extra coin."),
                   "Deceitful training" : __("Encourage manipulative behavior"),
                   "Deceitful intro" : __("You teach her a few simple techniques she could use to manipulate her customers."),
                   "Deceitful pos_reaction" : __("She's a quick learner. Manipulating people seems to come naturally to her."),
                   "Deceitful neg_reaction" : __("She realises that you've used a few of these techniques on her in the past. She stops in her tracks as she starts to question your motives."), 
                   "Deceitful pic" : "model",
                   "Deceitful and_tag" : "tempt",
                   
                   "Inbred description" : __("learn more about her lineage."),
                   "Inbred training" : __("Scour the archives"),
                   "Inbred intro" : __("You visit the library together with faint hope that you may be able to uncover something in the genealogical records."),
                   "Inbred pos_reaction" : __("You explain how inbreeding is commonplace among royalty. Even though you can't find any evidence, she starts to entertain the thought that she might be a princess."),
                   "Inbred neg_reaction" : __("You're unable to uncover any new information about her ancestry. Better luck next time!"), 
                   "Inbred pic" : "study",
                   "Inbred and_tag" : "profile",
                   
                   "Depressed description" : __("kill herself."),
                   "Depressed training" : __("Be there for her"),
                   "Depressed intro" : __("You take a walk together. You explain to her that she can treat you as a pillar of support and doesn't have to suffer alone."),
                   "Depressed pos_reaction" : __("She takes comfort in your words and gains a bit more strength to carry on."),
                   "Depressed neg_reaction" : __("She spends the entire outing talking about the upsides and downsides of different methods of suicide. She has clearly put a lot of tought into this."), 
                   "Depressed pic" : "profile",
                   "Depressed and_tag" : "sad",
                   
                   "Chaste description" : __("educate the customers about abstinance."),
                   "Chaste training" : __("Promote abstinance"),
                   "Chaste intro" : __("You manage to contain the urge to laugh as you encourage her foolish plan to promote abstinance to the brothel's visitors."),
                   "Chaste pos_reaction" : __("The customers share a good laugh. They seem convinced that she's in on the joke and is merely portraying a puritanical character to satirize the church's teachings."),
                   "Chaste neg_reaction" : __("The customers share a good laugh as she makes a fool of herself."), 
                   "Chaste pic" : "nun",
                   "Chaste and_tag" : "profile",
                   
                   "Disfigured description" : __("visit a specialist to repair her disfigurement."),
                   "Disfigured training" : __("Visit a specialist"),
                   "Disfigured intro" : __("You take her to an expert in body repair. He uses a mixture of magic and surgery to improve her appearance."),
                   "Disfigured pos_reaction" : __("The operation is completed without a hitch."),
                   "Disfigured neg_reaction" : __("The result is underwhelming. One disfigurement has been covered up by another."), 
                   "Disfigured pic" : "hurt",
                   "Disfigured and_tag" : "rest",
                   
                   "Drunkard description" : __("drink herself into a coma."),
                   "Drunkard training" : __("Stage an intervention"),
                   "Drunkard intro" : __("You confront her with the pain and frustration she causes for everyone due to her alcoholism."),
                   "Drunkard pos_reaction" : __("She's genuinely moved by your words and promises to better her life."),
                   "Drunkard neg_reaction" : __("She thinks you're overreacting and suggests that you could use a drink to loosen up a little."), 
                   "Drunkard pic" : "dom",
                   "Drunkard and_tag" : "libido",
                   
                   # "Kidnapped description" : ".",
                   # "Kidnapped training" : "",
                   # "Kidnapped intro" : ".",
                   # "Kidnapped pos_reaction" : ".",
                   # "Kidnapped neg_reaction" : ".", 
                   # "Kidnapped pic" : "",
                   # "Kidnapped and_tag" : "",
                   
                   "Frigid description" : __("rebuff customers who make a move on her."),
                   "Frigid training" : __("Mentorship by the guards"),
                   "Frigid intro" : __("You pair her up with one of the guards, instructing him to teach her some basic grapples and de-escalation techniques."),
                   "Frigid pos_reaction" : __("She learns a few psychological techniques and restraining holds. And more importantly, she now carries herself with much more confidence than before."),
                   "Frigid neg_reaction" : __("Their training abruptly comes to an end when the guard becomes a bit too intimate with her. She fights him off and flees to her room."), 
                   "Frigid pic" : "fight",
                   "Frigid and_tag" : "constitution",
                   
                   "Asexual description" : __("do her bit to help the brothel succeed."),
                   "Asexual training" : __("Pursue excellence"),
                   "Asexual intro" : __("You make it clear to her that whoring is a brothel's bread and butter. If she has no interest in sexual acts, then she'd better excel at something else to make up for that."),
                   "Asexual pos_reaction" : __("She takes your message to heart and vigorously studies to improve herself further, without leaving her comfort zone."),
                   "Asexual neg_reaction" : __("She attempts to become a bit more comfortable with whoring, but has a tough time making any progress at all."), 
                   "Asexual pic" : "study",
                   "Asexual and_tag" : "student",
                   
                   "Bloodslut description" : __("rip someone's dick off the next time a customer dares to call her a Bloodslut."),
                   "Bloodslut training" : __("Overcome prejudice"),
                   "Bloodslut intro" : __("Sadly prejudice against Meatsleeves from the Blood Islands is commonplace in Zan. You tell her to take comfort in the fact that loyal customers have grown very fond of her."),
                   "Bloodslut pos_reaction" : __("Radical changes can start in small ways. She agrees that the best way to deal with this is to befriend more customers, to make them realise that Meatsleeves are ordinary people too."),
                   "Bloodslut neg_reaction" : __("She remains frustrated. It's tough to see the positives when some visitors still regularly hurl insults at her head."), 
                   "Bloodslut pic" : "model",
                   "Bloodslut and_tag" : "happy",
                   
                   "Half-elf description" : __("improve public opinion regarding elves."),
                   "Half-elf training" : __("End racism?"),
                   "Half-elf intro" : __("You decide to position her as a rolemodel for young girls, spinning her elven heritage within a positive message of overcoming obstacles and challenging preconceptions."),
                   "Half-elf pos_reaction" : __("The message is recieved well, but not by the demographic you had expected. Her popularity among pubescent boys skyrockets as the seeds for change are planted in their young and impressionable minds."),
                   "Half-elf neg_reaction" : __("Regrettably the message doesn't take root and the majority of Zanic society still distrusts the elves."), 
                   "Half-elf pic" : "model",
                   "Half-elf and_tag" : "dom",
                   
                   "Monsterkin description" : __("control her animalistic instincts."),
                   "Monsterkin training" : __("Channel the anger"),
                   "Monsterkin intro" : __("She tells you about her temperamental nature. You suggest that she could bring it into an act of roleplay and play a ruthless dominatrix."),
                   "Monsterkin pos_reaction" : __("She really enjoys bossing the customers around. It's as if she was born to prey on them."),
                   "Monsterkin neg_reaction" : __("She might be bit too ruthless for comfort. Some of her clients break down in tears."), 
                   "Monsterkin pic" : "dom",
                   "Monsterkin and_tag" : "teacher",

                   "Vivified description" : __("dispel the rumours that she's a magician's creation."),
                   "Vivified training" : __("Allow the Magician's Guild to study her"),
                   "Vivified intro" : __("You send her to the magicians guild to conduct a thorough investigation of her personhood. The magicians seem very excited by this opportunity."),
                   "Vivified pos_reaction" : __("The magicians are fascinated by her. It's not often that they get to study a real girl so intimately. They are unable to unanimously agree that she's an ordinary person."),
                   "Vivified neg_reaction" : __("The studious magicians become a bit nervous in the presence of a female. They're unable to complete their investigation and inform you that she'll have to return at a later date."), 
                   "Vivified pic" : "sensitivity",
                   "Vivified and_tag" : "ceremony",
                   
                   }

         # Boost applies a % increase (or decrease). Value is a float number
         # Change applies a fixed value change which is not limited by stat max. Change can be reversed. Value is a number. 
         # Gain applies a one time permanent gain and is limited by stat max. Gain cannot be reversed. Value is a number.
         # Set replaces a base value with the new value
         # Allow unlocks a brothel option
         # Special is hard-coded

        ## Evolved negative traits
        
        traitking_neg_evolved = { 
                "Godless" : Trait(_("Devout"), verb = "be", eff1 = Effect("boost", "reputation gains", 0.1), base_description = __("She once was lost, but now faithfully serves her God."), public=False),
                "Trauma" : Trait(_("Stoic"), verb="be", effects = [Effect("boost", "love", -0.2), Effect("boost", "fear", -0.4)], base_description = __("She is emotionally stable despite losing her virginity against her will."), public=False),
                "Dull" : Trait(_("Curious"), verb = "be", eff1 = Effect("special", "effect chance", 0.1), base_description = __("She once led a sheltered life, but now invites new experiences into her life."), public=False),
                "Mean" : Trait(_("Reserved"), verb = "be", eff1 = Effect("change", "charm", -5, scales_with = "rank"), eff2 = Effect("change", "refinement", 10), base_description = __("She has a mean streak, but tries not to speak her mind whenever it is filled with negativity."), public=False),
                "Scars" : Trait(_("Marks"), verb = "be", eff1 = Effect("change", "body", -5, scales_with = "rank"), eff2 = Effect("change", "charm", 10), base_description = __("She carries herself with such confidence that you barely notice her nasty scars."), public=False),
                "Plain" : Trait(_("Odd"), verb = "be", eff1 = Effect("change", "beauty", -5, scales_with = "rank"), eff2 = Effect("change", "charm", 10), base_description = __("She's looks like an ordinary girl, but makes up for it with her unique personality."), public=False),
                "Rude" : Trait(_("Raw"), verb = "be", eff1 = Effect("change", "refinement", -5, scales_with = "rank"), base_description = __("She tries to be considerate, despite her uncultured origins."), public=False),
                "Rough" : Trait(_("Impolite"), verb = "be", eff1 = Effect("change", "sensitivity", -5, scales_with = "rank"), opposite = "Delicate", base_description = __("She occasionally acts without considering decorum."), public=False),
                "Weak" : Trait(_("Tender"), verb = "be", eff1 = Effect("change", "constitution", -5, scales_with = "rank"), opposite = "Resilient", base_description = __("She has trained hard to be a bit less vulnerable than she once was."), public=False),
                "Defiant" : Trait(_("Resistant"), verb = "be", eff1 = Effect("change", "obedience", -5, scales_with = "rank"), eff2=Effect("change", "valuation", -20), opposite = "Meek", base_description = __("She likes to rebel against authority every now and then."), public=False),
                "Gluttonous" : Trait(_("Craving"), verb = "be", eff1 = Effect("change", "constitution", -15), base_description = __("She is always hungry, but has learned not to overindulge."), public=False),
                "Uncouth" : Trait(_("Primitive"), verb="be", eff1=Effect("change", "refinement", -20), opposite = "Groomed", base_description = __("She lacks basic manners, but has good intentions."), public=False),
                "Deaf" : Trait(_("Inattentive"), verb = "be", eff1 = Effect("change", "obedience", -10), eff2 = Effect("change", "waitress jp gains", -0.25), base_description = __("She may not be deaf, but she is often absentminded."), public=False),
                "Timid" : Trait(_("Bashful"), verb = "be", eff1 = Effect("boost", "charm gains", -0.25), eff2 = Effect("change", "sensitivity", 10), opposite = "charming", base_description = __("She's is endearingly shy."), public=False),
                "Plump" : Trait(_("Full-figured"), verb = "be", eff1 = Effect("boost", "body gains", -0.25), eff2 = Effect("change", "constitution", 10), opposite = "Fit", base_description = __("She has generous natural curves."), public=False),
                "Scruffy" : Trait(_("Authentic"), verb = "be", eff1 = Effect("boost", "beauty gains", -0.25), eff2 = Effect("change", "beauty", 10), opposite = "Beautiful", base_description = __("She prefers to be genuine and acknowledges her imperfections instead hiding them."), public=False),
                "Vulgar" : Trait(_("Honest"), verb = "be", eff1 = Effect("boost", "refinement gains", -0.25), eff2 = Effect("change", "libido", 10), opposite = "Elegant", base_description = __("She freely speaks her mind without mincing words."), public=False),
                "Tame" : Trait(_("Restrained"), verb = "be", eff1 = Effect("boost", "libido gains", -0.25), eff2=Effect("change", "refinement", 10), opposite = "Slutty", base_description = __("She is well-behaved."), public=False),
                "Frail" : Trait(_("Cherished"), verb = "be", eff1 = Effect("boost", "constitution gains", -0.25), eff2=Effect("change", "sensitivity", 10), opposite = "Athletic", base_description = __("She is frail, but worth protecting."), public=False),
                "Rebellious" : Trait(_("Liberated"), verb = "be", eff1 = Effect("boost", "obedience gains", -0.25), eff2 = Effect("change", "charm", 10), opposite = "Obedient", base_description = __("She is free to make her own choices."), public=False),
                "Distrustful" : Trait(_("Independent"), verb = "be", eff1 = Effect("boost", "love gains", -0.25), eff2 = Effect("change", "refinement", 10), opposite = "Loyal", base_description = __("She's an independent and reliable girl."), public=False),
                "Fearful" : Trait(_("Anxious"), verb = "be", eff1 = Effect("boost", "fear", 0.25), eff2 = Effect("change", "defense", 1), opposite = "Brave", base_description = __("She's nervous and quick to worry."), public=False),
                "Paranoid" : Trait(_("Cautious"), verb = "be", eff1 = Effect("boost", "fear", 1.0), eff2 = Effect("change", "defense", 2), base_description = __("She's wary and takes great care to avoid danger."), public=False),
                "Homely" : Trait(_("Comfortable"), verb = "be", eff1 = Effect("boost", "reputation gains", -0.1), eff2 = Effect("boost", "love", 0.25), opposite = "Sexy", base_description = __("She feels at ease."), public=False),
                "Prude" : Trait(_("Behaved"), verb = "be", eff1 = Effect("boost", "service jp gains", -0.25), eff2 = Effect("boost", "sex jp gains", -0.25), eff3=Effect("change", "refinement", 10), opposite = "Naughty", base_description = __("She does not like meaningless sex and prefers to build a connection first."), public=False),
                "Naive" : Trait(_("Green"), verb = "be",eff1 = Effect("boost", "anal jp gains", -0.25), eff2 = Effect("boost", "fetish jp gains", -0.25), eff3=Effect("change", "beauty", 10), opposite = "Kinky", base_description = __("She does not like doing the weird stuff... Yet..."), public=False),
                "Square" : Trait(_("Traditional"), verb = "be", eff1 = Effect("change", "sex act requirements", 20), eff2=Effect("change", "refinement", 10), opposite = "Pervert", base_description = __("She prefers to do things by the book."), public=False),
                "Strong Gag Reflex" : Trait(_("Throat spasms"), verb = "have", eff1 = Effect("increase satisfaction", "service", -1), eff2=Effect("change", "libido", 10), base_description = __("She used to choke a lot more, but still vomits on a dick now and then."), public=False),
                "All thumbs" : Trait(_("Klutzy"), verb = "be", eff1 = Effect("increase satisfaction", "waitress", -1), eff2 = Effect("change", "libido", 10), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy'], base_description = __("She still struggles to make herself useful."), public=False),
                "Awkward" : Trait(_("Embarrassed"), verb = "be", eff1 = Effect("increase satisfaction", "dancer", -1), eff2 = Effect("change", "charm", 10), opposite=['Nimble', 'Agile', 'Brisk', 'Powerful'], base_description = __("She feels uncomfortable in some situations."), public=False),
                "Brutal" : Trait(_("Fierce"), verb = "be", eff1 = Effect("increase satisfaction", "masseuse", -1), eff2 = Effect("change", "constitution", 10), opposite=['Deft', 'Soft skin', 'Agile', 'Unhurried'], base_description = __("She likes to openly display her strength."), public=False),
                "Dumb" : Trait(_("Dopey"), verb = "be", effects = [Effect("increase satisfaction", "geisha", -1), Effect("change", "charm", 10)], opposite=['Nimble', 'Soft skin', 'Bright', 'Modest'], base_description = __("She's stupid and funny."), public=False),
                "Oafish" : Trait(_("Simple"), verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.25), eff2 = Effect("boost", "geisha jp gains", -0.25), eff3 = Effect("change", "libido", 10), opposite=['Nimble', 'Agile', 'Brisk', 'Soft skin', 'Bright'], base_description = __("She does not like thinking about complicated things."), public=False),
                "Clumsy" : Trait(_("Silly"), verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.25), eff2 = Effect("boost", "masseuse jp gains", -0.25), eff3 = Effect("change", "sensitivity", 10), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy', 'Soft skin', 'Agile'], base_description = __("People like to make fun of her mistakes."), public=False),
                "Slow" : Trait(_("Relaxed"), verb = "be", eff1 = Effect("boost", "xp gains", -0.25), eff2 = Effect("change", "libido", 10), opposite = ["Fast learner", "Sharp", "Genius"], base_description = __("She prefers to take it easy."), public=False),
                "Arrogant" : Trait(_("Self-assured"), verb = "be", eff1 = Effect("boost", "all jp gains", -0.25 ), eff2 = Effect("change", "body", 10), opposite = "Humble", base_description = __("She may be a bit too confident in her abilities."), public=False),
                "Stubborn" : Trait(_("Determined"), verb = "be", eff1 = Effect("boost", "xp gains", -0.1 ), eff2 = Effect("boost", "all jp gains", -0.1 ), eff3 = Effect("change", "constitution", 10), base_description = __("She feels driven pursue her own ideas, even when they are questionable."), public=False),
                "Lazy" : Trait(_("Peaceful"), verb = "be", eff1 = Effect("boost", "max energy", -0.1), eff2 = Effect("change", "refinement", 10), opposite = ["Energetic", "Driven"], base_description = __("She is serene and carefree."), public=False),
                "Blind" : Trait(_("Myopic"), verb = "be", eff1 = Effect("change", "defense", -2), eff2 = Effect("change", "sensitivity", 10), base_description = __("She is short-sighted."), public=False),
                "Vulnerable" : Trait(_("Accessible"), verb = "be", eff1 = Effect("change", "defense", -2), eff2 = Effect("change", "sensitivity", 10), opposite = ["Strong", "Warrior"], base_description = __("She sees it as her duty to comfort even the most unstable individuals."), public=False),
                "Expensive" : Trait(_("Valuable"), verb = "be", eff1 = Effect("boost", "upkeep", 1), eff2=Effect("change", "valuation", +50), opposite = "Humble", base_description = __("She deserves to be treated like a princess."), public=False),
                "Greedy" : Trait(_("Philanthropic"), verb = "be", eff1 = Effect("boost", "upkeep", -0.8), base_description = __("She wishes to live a frugal life and donates whatever she can to those in need."), public=False),
                "Cold" : Trait(_("Cool"), verb = "be", eff1 = Effect("change", "refinement", -10, scales_with = "rank"), eff2 = Effect("boost", "tiredness", -0.1), base_description = __("She knows how to hold her nerve."), public=False),
                "Jaded" :  Trait(_("Veteran"), verb = "be a", eff1 = Effect("special", "skill catch up", 1), eff2 = Effect("change", "valuation", -10, scales_with = "rank"), opposite = "Sensitive", base_description = __("She guides the others through her experience and know-how."), public=False),
                "Sickly" : Trait(_("Empathic"), verb = "be", eff1 = Effect("boost", "hurt", +2), eff2=Effect("change", "sensitivity", 20), opposite = "Tough", base_description = __("Disease and hardship has made her become more compassionate."), public=False),
                "Unlucky" : Trait(_("Unrelenting"), verb = "be", eff1 = Effect("special", "unlucky", 1), eff2 = Effect("reroll", "job critical failure", 1), base_description = __("She has some terrible luck, but perseveres through sheer willpower."), opposite = "Lucky", public=False),
                "Slave Brand" : Trait(_("Trophy"), verb="be a", effects = [Effect("boost", "prestige", 1.5), Effect("change", "valuation", -100)], archetype="The Bride", base_description = __("She has a tattoo that says {i}'Property of Kosmo Industries. If found, please return to rightful owner.'{/i}."), public=False),

                "Lesbian" : Trait(_("Queer"), verb = "be a", eff1=Effect("increase satisfaction", "all sex acts", -1), eff2=Effect("increase satisfaction", "bisexual", 3), archetype="The Courtesan", base_description = __("She does not get aroused by men, but serves women like no other."), public=False),
                "City girl" : Trait(_("Cosmopolitan"), verb="be a", eff1=Effect("boost", "farm preference increase", -1.0), eff2=Effect("change", "valuation", +60), eff3 = Effect("change", "refinement", 20), archetype="The Escort", base_description = __("She is a cultured soul who thrives in the city, but would despise living in the countryside."), public=False),
                "Circumcised" : Trait(_("Priestess"), verb = "be a", effects = [Effect("change", "libido", -50), Effect("change", "sensitivity", -50), Effect("increase satisfaction", "all jobs", 1), Effect("change", "whore obedience target", 100), Effect("change", "valuation", +200)], base_description = __("She has dedicated her life to serving Arios and the church has honored her with the title of Priestess."), public=False), 
                "Deceitful" : Trait(_("Sly"), verb = "be", eff1=Effect("boost", "income", -0.01), eff2=Effect("change", "valuation", +50), base_description = __("She is a manipulative girl who makes sure she gets whatever she wants."), public=False),
                "Inbred" : Trait(_("Pureblood"), verb = "be a", eff1 = Effect("boost", "love", 0.5), eff2 = Effect("boost", "all jp gains", -0.5), eff3=Effect("change", "valuation", +400), base_description = __("Her father and mother were closely related by blood, which leads people to assume that she might come from a royal bloodline."), public=False),
                "Depressed" : Trait(_("Cynical"), verb="be", eff1=Effect("change", "mood", -1), eff2=Effect("change", "constitution", 10), base_description = __("She has a pessimistic outlook on life and copes with this by openly showing her contempt."), public=False),
                "Chaste" : Trait(_("Pure"), verb = "be", eff1 = Effect("increase satisfaction", "waitress", 1), eff2 = Effect("increase satisfaction", "geisha", 1), eff3=Effect("change", "valuation", +100), opposite = "Pervert", base_description = __("She disapproves of sex outside of marriage, yet she works in a brothel. Visitors consider it endearing."), public=False),
                "Disfigured" : Trait(_("Repaired"), verb = "be", eff1 = Effect("boost", "naked bonus", -0.1), eff2 = Effect("change", "beauty", -10), eff3=Effect("change", "valuation", -25), opposite = "Nice boobs", base_description = __("She was disfigured in a nasty accident, but specialist doctors have concealed the damage as much as they could."), public=False),
                "Drunkard" : Trait(_("Teetotaler"), verb="be a", eff1=Effect("change", "constitution", 15, scales_with = "rank"), eff2= Effect("boost", "reputation gains", -0.25), eff3=Effect("change", "valuation", +50), base_description = __("She completely abstains from intoxicating beverages."), public=False),
                # "Kidnapped" : Trait(_("Bonded"), verb = "be", eff1=Effect("change", "obedience", 40), eff2 = Effect("boost", "love", 0.5), eff3=Effect("change", "maintenance", 1, scope="brothel"), base_description = __("She was kidnapped, but cares deeply about you due to Stockholm Syndrome."), public=False),
                "Frigid" : Trait(_("Composed"), verb = "be", eff1 = Effect("change", "libido", -10), eff2 = Effect("increase satisfaction", "masseuse", 1), eff3=Effect("increase satisfaction", "dancer", 1), opposite = "Horny", base_description = __("She is always calm and collected, which allows the customers to wind down."), public=False),
                "Asexual" : Trait(_("Celibate"), verb = "be", effects = [Effect("change", "libido", -50), Effect("increase satisfaction", "all sex acts", -1), Effect("increase satisfaction", "all jobs", 1)], opposite = "Pervert", base_description = __("She has little to no interest in intimacy, but understands that she must earn her keep one way or the other."), public=False),
                "Bloodslut" : Trait(_("Islander"), verb = "be a", effects=[Effect("gain", "all sexual preferences", 250), Effect("change", "valuation", -20), Effect("change", "brothel reputation", -10, scales_with = "rank", chance=0.01, scope="brothel"), Effect("change", "customers", -2, scope="brothel"), Effect("personality", "creep")], opposite = "Virgin", base_description = __("Despite a shady past on the Blood Islands, most customers have grown fond of her."), public=False),
                "Half-elf" : Trait(_("Fey Blood"), verb = "be a", effects=[Effect("boost", "tiredness", -0.1)], base_description = __("She has elven blood running through her veins, but customers don't seem to mind."), public=False),
                "Monsterkin" : Trait(_("Beastly"), verb = "be a", effects=[Effect("special", "immune", 1), Effect("change", "security", -1, scope = "brothel")], base_description = __("Some believe that she was birthed by a monster. But don't let that scare you, she's an admirable creature once you get to know her."), public=False),
                "Vivified" : Trait(_("Awakened"), verb = "be", effects=[Effect("change", "constitution", -20), Effect("change", "valuation", +600)], base_description = __("People believe that she is an unnatural being, conjured up by a magician. Collectors from all over Xeros are interested in obtaining and studying her."), public=False),

                        }

        neg_traits_fixable = []
        
        for trait in traitking_neg_traits:
            if trait.name in traitking_neg_evolved:
                neg_traits_fixable += [trait]

        neg_traits_fix = [t for o, t in traitking_neg_evolved.items()]
        
        for trait in traitking_gold_traits:
            register_trait(trait, type="gold")
        
        for trait in traitking_pos_traits:
            register_trait(trait, type="pos")

        for trait in traitking_neg_traits:
            register_trait(trait, type="neg")

        for trait in neg_traits_fix:
            register_trait(trait, type="neg")
            
        expensive_trait = trait_dict["Expensive"]
        clumsy_trait = trait_dict["Clumsy"]

        # Adding special traits to trait dict (but not to pos/neg traits)
        godless_trait = trait_dict["Godless"] = Trait(_("Godless"), verb = "be", eff1 = Effect("boost", "reputation gains", -0.2))

        housebroken_trait = trait_dict["Housebroken"] = Trait(_("Housebroken"), verb="be", effects = [Effect("change", "job obedience target", -10), Effect("change", "whore obedience target", -10), Effect("change", "refinement", -10, scales_with = "rank")], base_description = __("She lost her virginity in a brothel with a customer. This is all she knows."))
        t_pet_trait = trait_dict["Teacher's pet"] = Trait(_("Teacher's pet"), verb="be a", effects = [Effect("change", "train obedience target", -20), Effect("boost", "love", 0.25), Effect("change", "mood", -0.25, scales_with="cust nb")], base_description = __("Her first time was with me. I'm special to her."))
        trauma_trait = trait_dict["Trauma"] = Trait(_("Trauma"), verb="have a", effects = [Effect("change", "obedience", 20), Effect("gain", "negative fixation", 2), Effect("boost", "fear", 0.5)], base_description = __("She lost her virginity against her will, and has to live with the trauma."))
        farmgirl_trait = trait_dict["Farmgirl"] = Trait(_("Farmgirl"), verb="be a", effects = [Effect("change", "fetish", 20), Effect("boost", "farm preference increase", 0.25), Effect("boost", "customer penalties", 0.1)], base_description = __("She has lost her virginity in the farm like a filthy animal."))

        ## Important! It is necessary to copy the mod template to a variable upon initializing it if you would like mod variables to save together with the player's saved game (ie. most cases)
        traitking = traitking_template
       
        ## GIRL GENERATION TRAIT DISTRIBUTIONS
        ## Original girls will recieve +1 gold traits on top of this. Positive values must be at least gold values + 1
        
        traitking_t1_chance = 99 # 1% chance
        traitking_t1_gold = 2
        traitking_t1_positive = 3
        traitking_t1_regular = 0

        traitking_t2_chance = 95 # 4% chance
        traitking_t2_gold = 1
        traitking_t2_positive = 3
        traitking_t2_regular = 0
                           
        traitking_t3_chance = 85 # 10% chance
        traitking_t3_gold = 0
        traitking_t3_positive = 1
        traitking_t3_regular = 2
       
        traitking_t4_chance = 75 # 10% chance
        traitking_t4_gold = 0
        traitking_t4_positive = 3
        traitking_t4_regular = 0
       
        traitking_t5_chance = 55 # 20% chance
        traitking_t5_gold = 0
        traitking_t5_positive = 2
        traitking_t5_regular = 0
       
        traitking_t6_chance = 35 # 20% chance
        traitking_t6_gold = 0
        traitking_t6_positive = 3
        traitking_t6_regular = 1
       
        traitking_t7_gold = 0 # 35% chance    
        traitking_t7_positive = 2
        traitking_t7_regular = 1

        # schedule recurring trait king events
        calendar.set_alarm(calendar.time + 28, StoryEvent(label="traitking_morning", type="morning"))
        calendar.set_alarm(calendar.time + 7, StoryEvent(label="traitking_day", type="day"))
        calendar.set_alarm(calendar.time + 1, StoryEvent(label="traitking_night", type="night"))
        
        # schedule holidays
        renpy.call("traitking_holidays")        

    return
    

label traitking_init:

    return
    
