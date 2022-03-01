#### BK PERKS ####
## Labels are used instead of Functions to make sure we are using global variables

init python:
        ## PERK ARCHETYPES ##
        archetype_dict = {"The Maid" : PerkArchetype("The Maid", "the maid.jpg"),
                          "The Player" : PerkArchetype("The Player", "the player.jpg"),
                          "The Model" : PerkArchetype("The Model", "the model.jpg"),
                          "The Courtesan" : PerkArchetype("The Courtesan", "the courtesan.jpg"),

                          "The Escort" : PerkArchetype("The Escort", "the escort.jpg"),
                          "The Fox" : PerkArchetype("The Fox", "the fox.jpg"),
                          "The Slut" : PerkArchetype("The Slut", "the slut.jpg"),
                          "The Bride" : PerkArchetype("The Bride", "the bride.jpg"),}

label init_perks():
    python:
        ## PERK DESCRIPTIONS ##

        perk_description = {
                             "Maid Training" : "'{i}I am here to serve.{/i}'",
                             "Loyalty" : "The bond between a master and servant is a sacred thing.",
                             "Hardworking" : "'{i}Anything is possible if you put your heart into it.{/i}'",
                             "Try Again" : "'{i}I am so sorry. Let me make this up to you.{/i}'",
                             "Survivor" : "She's been through hell and back, and she is willing to do what it takes to survive.",
                             "Strive for Perfection" : "'{i}Never leave a job halfway done.{/i}'",

                             "Bunny Girl" : "'{i}Mister! Have you got any carrots for me?{/i}'",
                             "Party Girl" : "'{i}Where do you think you're going? The party's only started...{/i}'",
                             "Bimbo" : "Success comes easy to someone with such 'assets'.",
                             "Autograph" : "Star-struck fans are the best tippers.",
                             "Exhibitionist" : "All eyes on her, that's what she loves.",
                             "Star Power" : "A star is born. People come from far and wide just to meet her.",

                             "Modeling 101" : "'{i}Do I really have to wear this?{/i}'",
                             "Rules of Attraction" : "Her innocent looks make her the darling of the customers.",
                             "Overachiever" : "Nothing shall stop her from becoming the best in Zan.",
                             "Eye Contact" : "Lose yourself in those eyes, and forget all your troubles.",
                             "Life of Luxury" : "'{i}Sex is always better within Homokan silk sheets...{/i}'",
                             "Beauty Queen" : "No one can compare.",

                             "Court relations" : "'{i}The Earl of Kalderan was just here...{/i}'",
                             "Warm welcome" : "'{i}Would you like to slip into something... more comfortable?{/i}'",
                             "Refined taste" : "'{i}Can you give me a little more? I know how to be grateful...{/i}'",
                             "Five Stars" : "Quality comes at a price.",
                             "Heavenly Pleasures" : "'{i}I will give you pleasures you have never experienced...{/i}'",
                             "Royal Treatment" : "'{i}Tonight, you will be my King...{/i}'",

                             "Available" : "{i}Do you have what it takes? I'm waiting.{/i}",
                             "Focus" : "{i}Who called me a one-trick pony?{/i}",
                             "Next" : "{i}Aw, finished already? I can take more...{/i}",
                             "On Call" : "She's got a job to do, and she does it well.",
                             "Me So Horny" : "'{i}Me love you long time...{/i}'",
                             "Business and Pleasure" : "It's all a job to her. But boy, does she love her job.",

                             "Foxy Lady" : "'{i}Are you experienced?{/i}'",
                             "Something New" : "'{i}I heard about this at the spice market...{/i}'",
                             "Lost and Found" : "'{i}Maybe I should give it back, but how would I find him? He's halfway through the door already.{/i}'",
                             "Secret Admirers" : "She has her ways... Her regulars appreciate that.",
                             "Tempting Fate" : "Born under a lucky star...",
                             "Stars Are Aligned" : "Her presence is so magnetic, she can bring luck to the whole brothel. Hang on to her!",

                             "Teaser" : "{i}Mister, would you like to see more of me?{/i}",
                             "Open mind" : "'{i}How can you say you don't like it if you never try?{/i}'",
                             "Bedroom Eyes" : "'{i}Will you teach me something new?{/i}'",
                             "Loves Sex" : "'{i}I love what I do... Being fucked all day is hardly work at all!{/i}'",
                             "Convincing" : "'{i}Let me show you something really special...{/i}'",
                             "Work and Whore" : "{i}One thing leads to another... Let's have fun!{/i}",

                             "Enter The Bride" : "Codename: pink mamba.",
                             "Helping Hand" : "'{i}You can always count on me. We're all sisters.{/i}'",
                             "Confession" : "'{i}We shouldn't have any secrets for each other.{/i}'",
                             "Leading by Example" : "She can teach the other girls a thing or two.",
                             "The Healer" : "She cares a lot about others, and will do everything she can to protect those she loves",
                             "The Virgin Whore" : "'{i}You can do anything to me, but this hole is off-limits... Mister, are you okay? You're all sweaty...{/i}'",

                             "Naturist" : "",
                             "Ponygirl" : "She now only wears a revealing harness, and a tail. Guess where it's inserted... Free advertising.",
                             "Bisexual" : "Will sometimes serve a customer with another bisexual girl. Greatly increases tip and customer satisfaction, and reduce fatigue.",
                             "Group" : "A threesome with the customers is nothing she can't handle. May have sex with up to two customers at the cost of extra fatigue.",
                             "Orgy" : "What a slut! Looks like she wants every hole filled. May have sex with up to three customers, at the cost of extra fatigue.",
                             }

        ## REGULAR PERKS ##

        perk_dict = {
                     "Maid Training" : Perk(name="Maid Training", type="level", perk_level=0, archetype="The Maid", effects=[Effect("change", "obedience", 5), Effect("change", "maintenance", 1, scope="brothel")], pic = "maid0.jpg"),
                     "Loyalty" : Perk(name="Loyalty", type="level", perk_level=1, archetype="The Maid", effects=[Effect("change", "train obedience target", -10), Effect("change", "job obedience target", -10)], pic = "maid1_1.jpg"),
                     "Hardworking" : Perk(name="Hardworking", type="level", perk_level=1, archetype="The Maid", effects=[Effect("boost", "upkeep", -0.15), Effect("boost", "waitress jp gains", 0.15)], pic = "maid1_2.jpg"),
                     "Try Again" : Perk(name="Try Again", type="level", perk_level=2, archetype="The Maid", effects=[Effect("reroll", "job critical failure", 1), Effect("boost", "xp gains", 0.05)], pic = "maid2_1.jpg"),
                     "Survivor" : Perk(name="Survivor", type="level", perk_level=2, archetype="The Maid", effects=[Effect("boost", "fear", 0.5), Effect("resist", "hurt", 3, dice=True)], pic = "maid2_2.jpg"),
                     "Strive for Perfection" : Perk(name="Strive for Perfection", type="level", perk_level=3, archetype="The Maid", effects=[Effect("boost", "all skill gains", 0.25), Effect("change", "brothel reputation", 5, scope="brothel", scales_with="rank")], pic = "maid3.jpg"),

                     "Bunny Girl" : Perk(name="Bunny Girl", type="level", perk_level=0, archetype="The Player", effects=[Effect("change", "body", 10), Effect("change", "advertising", 1, scope="brothel")], pic = "player0.jpg"),
                     "Party Girl" : Perk(name="Party Girl", type="level", perk_level=1, archetype="The Player", effects=[Effect("change", "job customer capacity", 2), Effect("boost", "customer penalties", -0.5)], pic = "player1_1.jpg"),
                     "Bimbo" : Perk(name="Bimbo", type="level", perk_level=1, archetype="The Player", effects=[Effect("boost", "reputation gains", 0.15), Effect("boost", "dancer jp gains", 0.15)], pic = "player1_2.jpg"),
                     "Autograph" : Perk(name="Autograph", type="level", perk_level=2, archetype="The Player", effects=[Effect("change", "tip", 1, scales_with="rep"), Effect("special", "job prestige", 1)], pic = "player2_1.jpg"),
                     "Exhibitionist" : Perk(name="Exhibitionist", type="level", perk_level=2, archetype="The Player", effects=[Effect("boost", "naked bonus", 0.15)], pic = "player2_2.jpg"),
                     "Star Power" : Perk(name="Star Power", type="level", perk_level=3, archetype="The Player", effects=[Effect("increase satisfaction", "all jobs", 1), Effect("increase satisfaction", "all sex acts", 1)], pic = "player3.jpg"),

                     "Modeling 101" : Perk(name="Modeling 101", type="level", perk_level=0, archetype="The Model", effects=[Effect("change", "beauty", 10), Effect("boost", "quest results", 0.2)], pic = "model0.jpg"),
#                     "Rules of Attraction" : Perk(name="Rules of Attraction", type="level", perk_level=1, archetype="The Model", effects=[Effect("special", "BBCR bonus", 1, chance=0.25)], pic = "model1_1.jpg"), # Shelving stat bonuses for now
                     "Rules of Attraction" : Perk(name="Rules of Attraction", type="level", perk_level=1, archetype="The Model", effects=[Effect("change", "customers", 3, dice=True, scope="brothel")], pic = "model1_1.jpg"),
                     "Overachiever" : Perk(name="Overachiever", type="level", perk_level=1, archetype="The Model", effects=[Effect("change", "all skill max", 10), Effect("boost", "masseuse jp gains", 0.15)], pic = "model1_2.jpg"),
                     "Eye Contact" : Perk(name="Eye Contact", type="level", perk_level=2, archetype="The Model", effects=[Effect("special", "lucky"), Effect("change", "brothel reputation", 50, chance=0.2, scope="brothel")], pic = "model2_1.jpg"),
                     "Life of Luxury" : Perk(name="Life of Luxury", type="level", perk_level=2, archetype="The Model", effects=[Effect("special", "luxury"), Effect("change", "mood", 0.5, scales_with="equipped")], pic = "model2_2.jpg"),
                     "Beauty Queen" : Perk(name="Beauty Queen", type="level", perk_level=3, archetype="The Model", effects=[Effect("change", "all main skills", 15), Effect("boost", "job customer budget", 1.0)], pic = "model3.jpg"),

                     "Court relations" : Perk(name="Court relations", type="level", perk_level=0, archetype="The Courtesan", effects=[Effect("change", "refinement", 10), Effect("increase satisfaction", "bisexual", 1)], pic = "courtesan0.jpg"),
                     "Warm welcome" : Perk(name="Warm welcome", type="level", perk_level=1, archetype="The Courtesan", effects=[Effect("change", "first customer satisfaction", 1), Effect("boost", "half-shift resting bonus", 0.5)], pic = "courtesan1_1.jpg"),
                     "Refined taste" : Perk(name="Refined taste", type="level", perk_level=1, archetype="The Courtesan", effects=[Effect("boost", "bisexual chance", 0.5), Effect("boost", "geisha jp gains", 0.15)], pic = "courtesan1_2.jpg"),
                     "Five Stars" : Perk(name="Five Stars", type="level", perk_level=2, archetype="The Courtesan", effects=[Effect("change", "total tip", 25, scales_with="customer satisfaction")], pic = "courtesan2_1.jpg"),
                     "Heavenly Pleasures" : Perk(name="Heavenly Pleasures", type="level", perk_level=2, archetype="The Courtesan", effects=[Effect("boost", "perfect result tip", 0.1), Effect("boost", "perfect result xp", 0.1), Effect("boost", "perfect result jp", 0.1)], pic = "courtesan2_2.jpg"),
                     "Royal Treatment" : Perk(name="Royal Treatment", type="level", perk_level=3, archetype="The Courtesan", effects=[Effect("boost", "first customer tip", 1.5), Effect("boost", "first customer rep", 2.5), Effect("boost", "whore customer budget", 1.0)], pic = "courtesan3.jpg"),

                     "Available" : Perk(name="Available", type="level", perk_level=0, archetype="The Escort", effects=[Effect("change", "constitution", 5), Effect("increase satisfaction", "group", 1)], pic = "escort0.jpg"),
#                     "Extras" : Perk(name="Extras", type="level", perk_level=1, archetype="The Escort", effects=[Effect("special", "LOCS bonus", 1, chance=0.25)], pic = "escort1_1.jpg"), # Shelving stat bonuses for now
                     "Convincing" : Perk(name="Convincing", type="level", perk_level=1, archetype="The Escort", effects=[Effect("special", "temptress", 0.66)], pic = "slut2_2.jpg"),
                     "On Call" : Perk(name="On Call", type="level", perk_level=1, archetype="The Escort", effects=[Effect("boost", "group chance", 0.5), Effect("change", "whore obedience target", -10)], pic = "escort2_1.jpg"),
                     "Focus" : Perk(name="Focus", type="level", perk_level=2, archetype="The Escort", effects=[Effect("special", "focus", 1)], pic = "escort1_1.jpg"),
                     "Loves Sex" : Perk(name="Loves Sex", type="level", perk_level=2, archetype="The Escort", effects=[Effect("change", "all sex skills", 10)], pic = "slut2_1.jpg"),
                     "Business and Pleasure" : Perk(name="Business and Pleasure", type="level", perk_level=3, archetype="The Escort", effects=[Effect("boost", "total tip", 0.01, scales_with="job cust nb"), Effect("boost", "total tip", 0.03, scales_with="whore cust nb"), Effect("change", "mood", 0.25, scales_with="cust nb")], pic = "escort3.jpg"),

                     "Foxy Lady" : Perk(name="Foxy Lady", type="level", perk_level=0, archetype="The Fox", effects=[Effect("change", "charm", 10), Effect("boost", "class results", 0.2)], pic = "fox0.jpg"),
                     "Something New" : Perk(name="Something New", type="level", perk_level=1, archetype="The Fox", effects=[Effect("boost", "xp gains", 1.0, chance=0.1), Effect("boost", "all jp gains", 1.0, chance=0.1)], pic = "fox1_1.jpg"),
                     "Lost and Found" : Perk(name="Lost and Found", type="level", perk_level=1, archetype="The Fox", effects=[Effect("special", "random item", 1, chance=0.025)], pic = "fox1_2.jpg", base_description = "'I'm sure he won't miss it.'"),
                     "Secret Admirers" : Perk(name="Secret Admirers", type="level", perk_level=2, archetype="The Fox", effects=[Effect("boost", "tip", 1, chance=0.2)], pic = "fox2_1.jpg"),
                     "Tempting Fate" : Perk(name="Tempting Fate", type="level", perk_level=2, archetype="The Fox", effects=[Effect("special", "effect chance", 1)], pic = "fox2_2.jpg"),
                     "Stars Are Aligned" : Perk(name="Stars Are Aligned", type="level", perk_level=3, archetype="The Fox", effects=[Effect("boost", "income", 1, chance=0.02, scope="brothel")], pic = "fox3.jpg"),

                     "Teaser" : Perk(name="Teaser", type="level", perk_level=0, archetype="The Slut", effects=[Effect("change", "libido", 5), Effect("gain", "positive fixation", 1)], pic = "slut0.jpg"),
                     "Open mind" : Perk(name="Open mind", type="level", perk_level=1, archetype="The Slut", effects=[Effect("gain", "all sexual preferences", 250)], pic = "slut1_1.jpg"),
                     "Bedroom Eyes" : Perk(name="Bedroom Eyes", type="level", perk_level=1, archetype="The Slut", effects=[Effect("boost", "service jp bonus", 0.25), Effect("boost", "sex jp bonus", 0.25), Effect("boost", "anal jp bonus", 0.25), Effect("boost", "fetish jp bonus", 0.25)], pic = "slut1_2.jpg"),
                     "Next" : Perk(name="Next", type="level", perk_level=2, archetype="The Slut", effects=[Effect("change", "whore customer capacity", 1)], pic = "escort1_2.jpg"),
                     "Work and Whore" : Perk(name="Work and Whore", type="level", perk_level=2, archetype="The Slut", effects=[Effect("special", "workwhore", 1)], pic = "slut3.jpg"),
                     "Me So Horny" : Perk(name="Me So Horny", type="level", perk_level=3, archetype="The Slut", effects=[Effect("boost", "tiredness", -0.1)], pic = "escort2_2.jpg"),

                     "Enter The Bride" : Perk(name="Enter The Bride", type="level", perk_level=0, archetype="The Bride", effects=[Effect("change", "sensitivity", 5), Effect("change", "security", 1, scope = "brothel")], pic = "bride0.jpg"),
                     "Helping Hand" : Perk(name="Helping Hand", type="level", perk_level=1, archetype="The Bride", effects=[Effect("change", "making friends", 1), Effect("boost", "mood gains from friendship", 0.5)], pic = "bride1_1.jpg"),
                     "Confession" : Perk(name="Confession", type="level", perk_level=1, archetype="The Bride", effects=[Effect("spillover", "xp", 0.2), Effect("spillover", "jp", 0.2)], pic = "bride1_2.jpg"),
                     "Leading by Example" : Perk(name="Leading by Example", type="level", perk_level=2, archetype="The Bride", effects=[Effect("special", "skill catch up", 1)], pic = "bride2_1.jpg"),
                     "The Healer" : Perk(name="The Healer", type="level", perk_level=2, archetype="The Bride", effects=[Effect("boost", "love gains", 0.5), Effect("change", "heal", 1, chance=0.33, scope="brothel")], pic = "bride2_2.jpg"),
                     "The Virgin Whore" : Perk(name="The Virgin Whore", type="level", perk_level=3, archetype="The Bride", effects=[Effect("boost", "virgin tip", 1), Effect("boost", "virgin rep", 1)], pic = "bride3.jpg"),
                     }

        ## SPECIAL PERKS ##

        naked_perk = Perk("Naturist", type="sex", effects = [Effect("special", "naked", 1)])
        pony_perk = Perk("Ponygirl", type="sex", effects = [Effect("special", "ponygirl", 1.0, 0.5)])
        bis_perk = Perk("Bisexual", type="sex", effects = [Effect("special", "bisexual", 1.0, bis_chance)])
        group_perk = Perk("Group", type="sex", effects = [Effect("special", "group", 1.0, group_chance)])
        orgy_perk = Perk("Orgy", type="sex", effects = [Effect("special", "orgy", 1.0, 0.5)])



    return

#### END OF BK PERKS FILE ####
