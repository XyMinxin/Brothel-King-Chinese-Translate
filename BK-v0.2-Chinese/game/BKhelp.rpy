####            HELP MENUS                     ####
##      Help about the game and the              ##
##          various screens                      ##
####                                           ####

label help(scr):

    sill happy "{nw}"

    menu:

        sill "How can I help you?"

        "Help with the current screen":

            $ renpy.call("help_" + scr)

            if scr != "main":

                "You can exit this screen by right-clicking or using the 'back' button."

        "Tell me about night events" if scr == "main":

            call help_night_events from _call_help_night_events

        "How to win":
            call help_how_to_win from _call_help_how_to_win

        "Replay last achievements":
            show screen achievement_notification(latest_achievements, replay=True)

        "Reset food effects":
            python:
                for girl in game.get_all_girls():
                    girl.current_food_effect = defaultdict(bool)
            "Food effects reset."

        "Cheat menu - Main Screen only" if (game.cheats and scr == "main") or debug_mode:
            call cheat_menu from _call_cheat_menu

        "Activate cheats (disable achievements)" if not game.cheats and not debug_mode:
            $ game.activate_cheats()

        "Mods" if game.active_mods:

            label mod_menu():

                python:
                    menu_list = []

                    for mod in game.active_mods.values():
                        if mod.help_prompts: # Where 'help_prompts' is a list of tuples: (text, target_label)
                            menu_list += mod.help_prompts

                if menu_list:
                    $ menu_list.append(("取消", "back"))

                    $ target_label = menu(menu_list)

                    if target_label != "back":
                        call expression target_label from _call_expression
                    else:
                        return

                else:
                    "There are no active mods for this game, or the mods do not provide options."

                jump mod_menu


        "Repair girl/MC pictures":

            if renpy.call_screen("yes_no", "This will reset all girl and MC pictures (useful if you changed some pictures or renamed them). Would you like to proceed?"):

                python:
                    missing_girls = []
                    for girl in (MC.girls + slavemarket.girls + game.free_girls + MC.escaped_girls + farm.girls):
                        if girl.update_files():
                            girl.load_pics()
                            girl.refresh_pictures()
                            girl.create_char()
                        else: # Existing girls will be removed if their files cannot be found
                            missing_girls.append(girl)

                    MC.load_pics()

                if missing_girls:
                    if renpy.call_screen("yes_no", "All files are missing for " + and_text([g.path for g in missing_girls]) + ". Do you want to erase all girls with these templates from the game (you might run into bugs otherwise)?"):
                        python:
                            for girl in missing_girls:
                                for glist in (MC.girls, slavemarket.girls, game.free_girls, MC.escaped_girls, farm.girls):
                                    if girl in glist:
                                        glist.remove(girl)

                    elif renpy.call_screen("yes_no", "All files are missing for " + and_text([g.path for g in missing_girls]) + ". Do you want to replace their profile and portrait pictures with stock pictures? (debugging only)"):
                        python:
                            for girl in missing_girls:
                                girl.refresh_pictures(force_default=True)
                                girl.create_char()

                    $ cycle_free_girls() # Only cycle free girls if there are missing girls

                $ rating_dict = defaultdict(dict)

        "Activate picture count in gallery (girl packs)" if not persistent.debug_pic_counter:
            if renpy.call_screen("yes_no", "Warning! This is a debug feature and might slow down your game. Would you like to proceed?"):
                $ persistent.debug_pic_counter = True

                "The number of times a girl pack picture is drawn in-game will now be tracked and visible in the gallery."

                menu:
                    "Would you like to reset all existing counters to zero?"

                    "Yes":
                        $ persistent.debug_pic_counter_dict = defaultdict(int)

                    "No":
                        pass

        "Deactivate picture count in gallery" if persistent.debug_pic_counter:
            $ persistent.debug_pic_counter = False

            "Girl pack pictures will no longer be counted."


        "More about this game":

            call help_about_game from _call_help_about_game


        "Never mind":

            return

    return

label help_main():

    sill happy "This location is the main hub of your brothel, from where you can control everything in your business."

    sill "On top of the screen, you can see from left to right: the {b}current date{/b}, your available {b}gold{/b}, your
          remaining {b}actions{/b} and {b}mana{/b} for the day, and the {b}Help{/b} button. Hints may also appear if you hover over something."

    sill "The {b}Character{/b} tab allows you to see more information about yourself."

    sill "The {b}Girls{/b} tab is where you interact with your slavegirls in all sorts of ways. It is very important!"

    sill "The {b}Brothel{/b} tab allows you to upgrade your brothel and set up your advertising, security and maintenance. Don't neglect this one!"

    if story_flags["found wagon"] and story_flags["met carpenter"]:
        sill "From the Brothel tab, you can also access the {b}Wagon{/b} to build furniture and set up {b}Customer options{/b}."

    if farm.active:
        sill "The {b}Farm{/b} tab allows you to visit Gizel and her spooky farm. This will only lead to trouble, if you ask me."

    sill "The {b}City{/b} tab allows you to visit the city and its available district. Give it a go if you get bored here!"

    sill "The {b}Slave Market{/b} is bustling with sex slaves and the people who buy and sell them! Use it to get fresh slaves - if you can afford it."

    sill "The {b}Shop{/b} is where you can buy all sorts of mundane items for you or your girls. Maybe you'll find a bargain?"

    sill "The {b}Postings{/b} tab allows you to look for ads about quests and classes for your girl. It is useful to build up their skills and reputation."

    "From the main screen, you can access the option menu by right clicking or pressing 'Esc'. You can save or load a game and change all sorts
     of useful options from there."

    return


label help_MC():

    sill happy "{nw}"

    menu:

        sill "{b}The Character tab{/b}. This is you, Master! From here, you can see your personal information, change your portrait, manage your items and your spells."

        "Can I rename my character?":

            sill "Sure thing! Just click on your name, and choose a new one. Oh, I'm curious!!! What's it gonna be?"

        "Tell me about my character and skills":

            sill "First, let me tell you about your character class. Your class affects events in the game, your available spells and starting skills."

            if MC.playerclass == "战士":

                sill "You are a warrior, a skilled fighter with a tough spirit. Your social skills are a bit lacking, though, if I may say so."

                you "Grumph."

            elif MC.playerclass == "法师":

                sill "You are a wizard, skilled in spellcasting and with some wits to match. Don't get into close combat, though, this is not your style."

                you "I wouldn't want my hands to get dirty anyway. What with this expensive manicure I just got."

            elif MC.playerclass == "奸商":

                sill "You are good at barter and trade, and have learned the skills to survive in the streets. Magic is not your forte, however."

                you "Well, there were all those books to read, so... I figured I'd just sell them."

            sill "You are currently level [MC.level]. Each new level will grant you a skill point which you may use to boost your skills."

            sill "You may also learn new {b}Spells{/b} and {b}Talents{/b}, so it's worth getting all the {b}prestige{/b} you can get."

            sill "There are four skills you need to be concerned with: {b}Strength{/b}, {b}Spirit{/b}, {b}Charisma{/b}, and {b}Speed{/b}."

            sill "{b}Strength{/b} affects how well you perform physical tasks and hold your own in close combat. It also boosts your brothel security if you have remaining AP at the end of the day."

            sill "{b}Spirit{/b} affects how well you can sense magic and cast spells. Spirit lowers the cost of class spells for all player classes."

            sill "{b}Charisma{/b} affects your social skills and people's reactions to dialog, including your girls."

            sill "{b}Speed{/b} affects how many actions are available to you every day."

            sill "Finally, you can find information about your {b}beliefs{/b} and {b}alignment{/b}.
                  This is impacted by the actions you take, and used during dialog and story events."


        "How can I change my portrait?":

            sill "Just click on the arrows to select your portrait. This is just for flavor and doesn't affect the game in any other way."

            sill "By the way, if you don't like those, did you know you can add more portraits in the {b}game\\MC\\{/b} folder?"


        "Tell me about prestige and skill points":

            sill "{b}Prestige{/b} reflects your character's renown in Zan. Earning prestige allows you to level up and get skill points."

            sill "You earn prestige everytime you or your girls have sex. You also earn prestige when a girl levels up."

            sill "You may use {b}Skill points{/b} to increase your {b}Strength{/b}, {b}Spirit{/b}, {b}Charisma{/b}, and {b}Speed{/b}, up to a maximum of 10."


        "Tell me how to use items":

            sill "It's easy! Just click on the item you want to use, and select 'use' or 'equip'. You can unequip an item in the same way."

            sill "Please note that you can only use items that are intended {color=[c_steel]}{b}for you{/b}{/color} and not
                  {color=[c_pink]}{b}for your girls{/b}{/color}. Watch for the color in the item tab."


        "Tell me how to learn and use spells":

            sill "You can learn new {b}Spells{/b} and {b}Talents{/b} from your character class when increasing your level."

            sill "Spells must be cast and cost mana. Talents are always active."

            sill "After you learn a Spell, you can use it any time from the {b}Spellbook{/b}. Press 'K' for fast access to the Spellbook."

            sill "Casting spells costs {b}Mana{/b}. Mana Points (MP) depend on your Spirit skill. They are replenished every day."

            "{b}Left click{/b} on a spell in the spells tab to cast it."

            sill "Did you know that you can {b}auto-cast{/b} spells? If you automate a spell,
                  you will keep casting it every day - provided you have enough leftover MP."

            "{b}Right click{/b} on a spell in the spells tab to cast it. You can choose between auto-casting at night or in the morning by right-clicking again."

            sill "But no matter what you do, you may only cast one spell of a given type every day. For instance, wizards can only have one aura active
                  at any given time."

            sill "Some spells are only active for one night, and some last until a specific event occurs. {b}Hover{/b} over a spell to see its description."


        "Never mind":

            return

    return


label help_girls():

    sill happy "{nw}"

    menu:

        sill "{b}The Girls' rooms{/b}. This is where you can check your girls' information, interact with them, choose their job and schedule, and more."

        "Can I change a girl's name?":

            sill happy "You sure can! This is your privilege as the slave's master."

            sill "Just click on her {b}name{/b}, and choose a new one"

            if sill_name == "希露":
                sill sad "You can't rename me, though. I like my name!"

            you "Wait a minute. Didn't you say it was my privilege to rename you, as your owner?"

            sill sad "B-But..."

            menu:
                "Rename her 'Sill'" if sill_name != "希露":
                    $ sill_name = "希露"

                    you "Go back to Sill."

                    sill "Th... Thank you! Finally!"

                    $ NPC_sill.love += 3

                    jump help_girls

                "Rename her 'Rose'":
                    $ new_name = "Rose"

                "Rename her 'Lolita'":
                    $ new_name = "Lolita"

                "Rename her 'Pinky'":
                    $ new_name = "Pinky"


                "Rename her 'Peggy'":
                    $ new_name = "Peggy"

                "Rename her 'Bitch'":
                    $ new_name = "Bitch"

                "Don't rename her":
                    jump help_girls

            you "Your new name is... [new_name]"

            sill "Wh... What?"

            you "You heard me... [new_name]."

            $ NPC_sill.love -= 3

            $ sill_name = new_name

            sill sad "Oh no... T_T"

            jump help_girls


        "Tell me about defense, mood, love and fear":

            sill "Your girl's {b}defense{/b} is the number seen in the shield icon on top of your girl's profile. You can improve it by giving her certain perks or items."

            sill "Defense allows her to hold her own in a fight, because some customers do get rough. Being assaulted might not only hurt her, but damage
                  her trust and her mood."

            sill sad "But if you give her a weapon, watch out! If she rebels, she might well use it against you."

            sill happy "Your girl's {b}Mood{/b} can be seen as a circle on top of your girl's profile. Its color indicates how happy or discontent your girl is."

            sill "Keep your girl happy so that she doesn't rebel and progresses faster! Happiness comes from many factors, such as resting time, accommodation,
                  security, and how much love and respect your girl has for you."

            sill "However, you can also keep a girl sufficiently scared so that she won't refuse work or run away from you. Fear can be a powerful tool."

            sill sad "But please, there is no need to act like this with me! I'm always good!!!"

            sill "Let me tell you about {b}Love{/b} and {b}Fear{/b}."

            sill "Depending on how you treat them, girls will come to {b}love{/b} or {b}hate you{/b}. They will also {b}fear{/b} or {b}trust{/b} you."

            sill "But be careful... Some girls will take advantage of your leniency if you are too nice... Not me, of course!!!"

            sill "Your {b}Alignment{/b} will have consequences on how fast your girls' {b}Love{/b} and {b}Fear{/b} evolve."

            sill "Unlike Mood, Love and Fear change slowly. Keep it in mind before you decide how to treat your girls."

            jump help_girls


        "Tell me about ranks, levels and job skills":

            menu:

                sill "What are you interested in?"

                "Rank and reputation":

                    call help_rank_introduction from _call_help_rank_introduction

                    "You can use the shortcuts to sort your girls by name, job, level or rank (right-click on a sort method to sort backwards)."

                "Leveling and experience":

                    sill "As your girl works, goes on quests or attends classes she will become more experienced. Once she has enough {b}experience{/b} (XP),
                          she will be ready to reach a new level."

                    sill "New levels will allow you to increase your girls main skills with {b}skill points{/b}."

                    sill "Also, every level, you will receive {b}perk points{/b}. Perk points allow you to unlock some useful perks in a girl's {b}zodiac{/b} trees."

                    sill "The maximum level a girl can reach is capped by her current {b}rank{/b}, however. Don't forget to rank up!"

                "Zodiac signs and perks":

                    call help_zodiac() from _call_help_zodiac

                "Job skill and job points":

                    sill "Every time your girl accomplishes a specific job or sex act, she will receive {b}job points{/b} (JP). Job points will allow her to automatically
                          increase her job level."

                    sill "Improving job level will in turn raise a girl's relevant {b}skills{/b} by a good amount, and improve {b}customer satisfaction{/b} for this particular job or sex act."

                    sill "The maximum job level a girl can reach is capped by her current {b}rank{/b}, however. But she can always learn a new job!"

                    "You can use the shortcuts to sort your girls by name, job, level or rank (right-click on a sort method to sort backwards)."

                "Back":

                    jump help_girls


        "Tell me about the available actions":

            menu:
                sill "What do you want to know about?"

                "Changing a girl's job":

                    sill "The first button is the {b}job{/b} button. It allows you to change a girl's job. Keep in mind that she may refuse to be a whore if her obedience and/or libido is too low."

                    sill sad "You cannot change a girl's job while she is away, hurt, sick or exhausted. Sorry."

                "Changing a girl's schedule":

                    sill "You can set a weekly schedule for your girls using the {b}schedule{/b} button."

                    sill "Girls cannot work every day, or they will deplete their energy and become sick. A girl can work a half shift on certain days
                          if you want to spare some of her energy."

                "Interacting with a girl":

                    sill "The {b}interact{/b} button allows you to visit your girl and talk to her. You might find it useful to know your girls better, and maybe try to influence their behavior."

                "Equipping and using items":

                    sill "Use the {b}equip{/b} button to have a girl take, give, use or equip items. Some effects are permanent: think carefully before you use an item!"

                "Selling a girl":

                    sill "Oh, that one is easy. Just click the {b}sell{/b} button to get rid of a girl. But not me, of course."

                "Perks, leveling and ranking up":

                    sill "The {b}level up{/b} or {b}rank up{/b} buttons become available once your girl is ready to advance. Otherwise, you can use the {b}perks{/b} button to check
                          on your girl's current perks"

                "Tracking a girl's performance":

                    sill "The {b}stats{/b} button is handy if you want to keep track of the latest information about your girl's performance."

                "Back":

                    jump help_girls

        "Tell me about girl skills and traits":

            call skills_introduction from _call_skills_introduction

            jump help_girls

        "Tell me more about jobs":

            call jobs_introduction from _call_jobs_introduction

            "You can use the shortcuts to sort your girls by name, job, level or rank (right-click on a sort method to sort backwards)."

            jump help_girls

        "How can I train a girl to become a whore?":
            call help_whores from _call_help_whores_6


        "Never mind":

            return

    return

label help_whores():

    sill sad "Turning a regular girl into a whore is not as easy as it seems. Girls need training before they will accept to be whores."

    sill happy "There are several ways to train your girls, however."

    sill "First, you can train girls yourself. To do this, choose to 'interact' with them."

    sill "The typical way of training sex slaves is to go soft on them at first, lecturing them about sex and making them comfortable with their body, until
          they are ready for more advanced sex acts."

    sill sad "But some brothel masters choose to use fear and coercion instead... Some even brutally rape their slaves into submission."

    sill happy "Other choose to use magic... In the end, it's up to you to decide how you prefer to train your girls."

    sill "If you do not train your girls yourself, there are other ways to get them to become whores."

    sill "Working in the brothel will make your girls more receptive to sex work over time. Sometimes, interacting with customers will make
          them more interested in sex... Until they are ready for the next step."

    sill "This is quite a slow process, however. Obedient, libidinous, or sensitive girls are more likely to progress that way."

    sill "Alternatively, you can buy trained girls in the slavemarket. Those girls have been trained for sex already, although sometimes it's hard to know just how
          effective this training was."

    sill "Trained girls are more expensive to buy, of course. On the plus side, they also sell for more."

    sill "At first, you will only have access to girls with a low level of training, but the quality of available girls will improve
          as you unlock higher brothel licenses."

    sill "Finally, please know that all girls have different tastes in sex acts... They might even have some strange fetishes. If you discover them, you can make your training more effective."

    return

label skills_introduction():

    menu:
        sill "What are you interested in?"

        "Tell me about skills":

            sill "There are two types of skills for your girls: main skills and sex skills. Working jobs may increase, and sometimes decrease, specific stats."

            sill "Main skills are generic skills that every girl can improve working on any job."

            sill "Sex skills are skills that can only be improved by doing specific sex acts. They are the most important skills for a whore."

            sill "Your girl will choose which sex acts to perform on her own, but you can make her perform only specific acts if you tick or untick
                  the box next to each sex skill. Keep in mind, however, that some girls may refuse certain sex acts if their libido and/or obedience are too low."

            sill "You can hover over a specific skill to learn more about it."

            sill "The maximum skill a girl can have is limited by her current rank, however. Be sure to rank up your girls!"

        "Tell me about traits":

            sill "Every girl has {b}3 traits{/b} that she is born with. You cannot change those."

            sill "Some traits can have powerful effects on your girl, but beware! No one is perfect, so your girls will usually have a
                  negative trait as well."

        "Tell me about upkeep":

            sill "You can freely adjust {b}upkeep{/b}. Upkeep covers how much money you spend every night keeping your girl suitably fed and groomed."

            sill "Slave or not, your girls have some expensive tastes, you know! Giving your girls extra money will keep them content.
                  Watch that you don't let their upkeep sink too low, however! They will be mad at you."

        "Back":

            return

    return

label bis_introduction(unlock=True):

    if unlock:
        sill happy "Master! It seems you have trained your first bisexual girl."

    menu:
        sill "Would you like to learn more about how {b}bisexual{/b} whores work?"
        "Yes, fill me in":
            sill "Bisexual girls are able to have a threesome with a customer. For that, you will need {b}at least two bisexual whores{/b} active at the same time."

            $ bonus = percentage_description(tip_act_modifier["bisexual bonus"] * 2)[1:]

            sill "During a threesome, the lucky customer will be extra happy and pay {b}[bonus] of the usual tip{/b}."

            sill "Each girl will use an {b}interaction{/b}. But your girls will also share the, ahem, load, so their {b}energy{/b} expenditure will be halved."

            sill "Bisexual girls are useful if you want to get the {b}maximum value{/b} out of a few customers!"

            you "I see. Thanks!"

        "No thanks":
            sill "All right."

    return

label group_introduction(unlock=True):

    if unlock:
        sill happy "Master! It seems you have trained your first group girl."

    menu:
        sill "Would you like to learn more about how {b}group{/b} works for whores?"
        "Yes, fill me in":
            sill "Group girls are able to have orgies with several customers. For that, you will need {b}at least two willing customers{/b} that want the same sex act."

            $ bonus = percentage_description(tip_act_modifier["group bonus"])[1:]

            sill "During an orgy, customers will have fun but are not ready to pay your girl as much. Each customer will pay {b}[bonus] of the usual tip{/b}."

            sill "Of course, because a girl can service several customers with only one {b}interaction{/b}, it's still a good deal for you."

            sill "You have to watch the energy level of your group girls, though. They will spend double or triple the {b}energy{/b} depending on how many customers there are."

            sill "Group girls are useful if you want to serve the {b}maximum number of customers{/b}!"

            you "I'll keep that in mind. Thanks!"

        "No thanks":
            sill "Okay. Call me if you need anything..."

    return

label jobs_introduction():

    sill "Waitresses, dancers, masseuses and geishas entertain several customers at once. Whores usually entertain one customer at a time, but
                  they can have several customers per night." #to move

    menu:

        sill "What job do you want to know about?"

        "Waitress":

            sill "The {b}tavern{/b} will allow you to train your girl as a {b}waitress{/b}. With time, they will start wearing sexy uniforms
                  and providing all kinds of 'entertainment' to the customers."

            sill "Waitresses need {b}charm{/b} to keep the customers entertained. They also need a strong {b}constitution{/b}: working tables is not easy, you know!
                  Finally, it cannot hurt if they are {b}beautiful{/b}, and have a good {b}body{/b}."

        "Dancer":

            sill "The {b}strip club{/b} will allow you to train her as a {b}dancer{/b}. With time, they will remove more and more clothing, and
                  take the customers to a room for a 'private dance'."

            sill "You should pick girls with a good {b}body{/b} to be dancers. A {b}libidinous{/b} girl is always better, the customers can sense it.
                 {b}Refinement{/b} and {b}charm{/b} are also good qualities for a dancer."

        "Masseuse":

            sill "The {b}onsen{/b} will allow you to train her as a {b}masseuse{/b}. With time, they will provide more erotic massages
                  to the customers, and eventually give them 'full service'"

            sill "Masseuses should be {b}beautiful{/b} girls, to attract customers to the onsen. {b}Sensitive{/b} girls fare better as they can
                  make the customer more comfortable. A good {b}body{/b} and a little {b}refinement{/b} are also important."

        "Geisha":

            sill "The {b}okiya{/b} will allow you to train her as a {b}geisha{/b}. With time, they'll learn a thousand ways to please their
                  customers, and how to take care of their more 'special' requests."

            sill "Geishas should be {b}refined{/b} girls. {b}Obedience{/b} is a prized quality, to make the customers feel important. {b}Beauty{/b} and {b}charm{/b} also help
                  make a perfect geisha."

        "Whore":

            sill "Girls need to be trained before they will accept to be whores. Forcing them never gives good results. Girls with a high libido or obedience can be trained faster."

            sill "There are {b}4 different sex acts{/b} a whore can perform. You can select which acts they may or may not perform by ticking or unticking
                  the box next to each sex skill."

            sill "{b}Service{/b} includes all kinds of foreplay, including masturbation, handjobs and blowjobs. A good {b}service{/b} skill is required to perform service,
                  of course, as well as good {b}sensitivity{/b}. {b}Charm{/b} and the {b}fetish{/b} skill also help."

            sill "{b}Sex{/b} means vaginal intercourse, of course. A high {b}sex{/b} skill and {b}libido{/b} gives the best results. {b}Beauty{/b} and the {b}service{/b} skill also boost sex."

            sill "{b}Anal{/b} means anal sex. A high {b}anal{/b} skill together with a good {b}constitution{/b} is a must. A good {b}body{/b} and the {b}sex{/b} skill also help."

            sill "{b}Fetish{/b} includes BDSM, spanking, fisting, and all the weirder sexual practices. A girl needs a good {b}fetish{/b} and {b}obedience{/b} skill to succeed.
                  {b}Refinement{/b} and {b}anal{/b} skill also factor in fetish acts."

            sill "Later, you can also train your girls to accept {b}bisexual{/b} or {b}group{/b} sex."

            call bis_introduction(False) from _call_bis_introduction
            call group_introduction(False) from _call_group_introduction

        "Back":

            return

    return


label help_brothel():

    sill happy "{nw}"

    menu:

        sill "{b}Your Brothel{/b}. This is where you can check your brothel information, buy new rooms, and hire freelancers."

        "How can I check my brothel's information?":

            sill "The {b}Rooms{/b} you own are highlighted on the brothel tab. You can also see the number and type of bedrooms you have."

            sill "You can hover over the {b}Advertising{/b}, {b}Security{/b} and {b}Maintenance{/b} labels to learn more about your brothel's current state."

            if story_flags["found wagon"] and story_flags["met carpenter"]:

                sill "From the Brothel, you can also access the {b}Carpenter's Wagon{/b} and {b}Customer options{/b}."

        "Tell me more about rooms":

            sill "There are two types of rooms: bedrooms and common rooms."

            sill "Each girl must have her own {b}bedroom{/b}. They're not sharing! More comfortable bedrooms increase both girl mood and customer satisfaction."

            sill "You can click on the bedroom {b}picture{/b} to increase the number of bedrooms. Keep in mind that space is limited by your brothel's size, however.
                  Click on the {b}upgrade{/b} button to improve the quality of all of your bedrooms."

            sill "{b}Common rooms{/b} are where your girls perform their jobs when they aren't whoring. You need a specific room for each job type. A common room can
                  host any number of girls at the same time."

            sill "A word of warning: The more common rooms you build, the more expensive they get! Think before you buy. Contractors are so unreliable these days..."

        "Tell me more about freelancers":

            sill "You can hire {b}3 types of freelancers{/b} to help with your business: advertising girls, goons and cleaners."

            sill "{b}Advertising girls{/b} increase your brothel reputation, which in turn will bring in more customers every night."

            sill "In addition, advertising can give a temporary boost to how many customers will come ({b}customer attraction{/b}),
            and increase {b}customer budget{/b}, allowing you to make the most of a customer's visit.
            You need advertising to get people to visit your brothel, at least at the beginning!"

            menu:
                sill "Would you like to know more about advertising?"

                "Yes":
                    call help_advertising() from _call_help_advertising_1
                "No":
                    pass

            sill "{b}Goons{/b} improve your brothel security by beating the unpleasantness out of rowdy customers. Trouble is sure to show up at your door
                  some day, make sure to have a few of them handy!"

            menu:
                sill "Would you like to know more about security?"

                "Yes":
                    call help_security() from _call_help_security
                "No":
                    pass

            sill "{b}Cleaners{/b} are maids that take care of the maintenance of your brothel. Low maintenance may cause your girls to fall sick and turn away customers."

            sill sad "Please hire some cleaners, I don't want to do all the dirty work alone!!!"

            sill happy "Please note that freelancers get more expensive as you move your operations to fancier city districts. But they are also more efficient."

        "Tell me about trainers":

            sill "{b}Trainers{/b} can help run your brothel more efficiently! You may meet some interesting people in Zan, which will be able to help managing your girls.
                  Only one trainer can be active at all times."

            sill "There is no right or wrong trainer, it all depends on your management style."

        "Tell me about the Carpenter's Wagon and Customer options" if story_flags["found wagon"] and story_flags["met carpenter"]:
            call help_wagon() from _call_help_wagon
            call help_customers() from _call_help_customers

    return

label help_advertising():

    sill "{b}Advertising{/b} helps grow the renown of your brothel and draws more and wealthier {b}customers{/b} to your brothel."

    sill "Advertising has three different effects: it boosts {b}brothel reputation{/b}, {b}customer attraction{/b} and {b}customer budgets{/b}."

    sill "Each of these effects is strengthened by {b}advertising power{/b}."

label help_advertising_menu():
    menu:
        "Tell me about..."

        "Customers":

            sill "Some {b}customers{/b} will come to your brothel every night. At least one will show up no matter what, but your {b}brothel reputation{/b} and {b}customer attraction{/b} can increase that manyfold."

            sill "There are different {b}customer populations{/b} in Zan, each with a different level of difficulty and rewards, as well as some special effect."

            sill "You will mostly serve only {b}beggars{/b} at first, though. But as your brothel increases in rank and you reach higher districts, more customer populations will become available."

            sill "When that happens, you can choose which populations to attract in the {b}customer options{/b} tab. Not only that, but you can choose to allow or restrict customer populations on a girl by girl basis if you need to."

            sill "Harder customers also have a higher {b}customer budget{/b}. Keep that in mind as your brothel grows to make the most money out of it."

        "Brothel reputation":

            sill "{b}Brothel reputation{/b} receives a boost from advertising every night. It is also affected negatively or positively by your {b}customers' satisfaction{/b}."

            sill "{b}Brothel reputation{/b} is nice because it draws customers to your brothel for free, unlike advertising. It does {b}decay{/b} over time, though, especially in higher districts."

            sill "Of course, it will cost more brothel reputation to attract higher rank customers than the usual riff-raff. If you need more customers than your current reputation allows, blocking some higher rank populations from coming in {b}customer options{/b} could be a way to do it."

            sill "And a word of warning: {b}Unhappy customers{/b} may really drag your reputation down, especially at higher ranks. It is best to focus on drawing only as many customers as you can serve to the brothel to avoid grumbling."

        "Customer attraction":

            sill "{b}Customer attraction{/b} is a temporary boost your advertising girls will bring to the total number of customers that come to the brothel."

            sill "If you lower advertising, though, you will lose those extra customers. This is the main difference between {b}brothel reputation{/b} and {b}customer attraction{/b}."

            sill "Ultimately, if you want many customers to come, it is good to keep advertising high."

            sill "One day, you may even be able to unlock a way to increase {b}customer attraction{/b}, at the expense of {b}customer budgets{/b}."

        "Customer budgets":
            sill "Each customer has a {b}maximum budget{/b} he's ready to spend on activities at your brothel."

            sill "Customers have a separate budget for {b}entertainment{/b}, such as hanging by the tavern or club, and {b}whoring{/b}. Their budget for whoring is higher, naturally.
            But if you want to get the most value out of a customer, entertaining him first is a good idea."

            sill "Advertising increases {b}customer budgets{/b}. In rare cases, it is also possible to convince customers to go over their allowance. Some girl perks help with that."

            sill "Of course, this is only their {b}maximum{/b} allowance. If your girls perform badly, they will pay a lot less regardless of their budget."

            sill "Ultimately, if you want customers to spend a lot, it is good to keep advertising high."

            sill "One day, you may even be able to unlock a way to increase {b}customer budgets{/b}, at the expense of {b}customer attraction{/b}."

        "Advertising power":

            sill "{b}Advertising power{/b} is influenced by your advertising girls' current {b}outfits{/b}."

            sill "There may be a way to unlock new outfits in the future."

        "Nothing":

            you "I'm good now, thanks."

            return

    jump help_advertising_menu


label help_wagon():

    carpenter "This baby here is where I ply my trade, boss."

    carpenter "{b}Furniture-making{/b}, of course. I also do decorations. Heck, I can even arrange a whole room real nice if you have the resources."

    carpenter "I need {b}Resources{/b} to build stuff. That was our deal, remember?"

    carpenter "Resources can be found all over town, I hear."

    carpenter "When you give me a new task, I might take a few days to complete it. An' I don't like to be interrupted. Make sure to get yer priorities straight."

    carpenter "After you build something, it cannot be undone. But some furniture will open new options for you, or even be switched on/off. Check the {b}Customer options{/b} tab to learn more."

    return

label help_customers():

    carpenter "Heya boss, it's me."

    carpenter "You might've noticed, building new furniture has opened new {b}Customer options{/b} for ya."

    carpenter "It's real simple: choosing which furniture and decoration to display will attract different categories of customers."

    carpenter "Customers come from one of the many populations in Zan, from the rabble to the high 'n' mighty.
    Check out their characteristics by hovering over their portrait: some might surprise you."

    carpenter "They also have different budgets and whatnot. Your pink-haired girlfriend tried to explain all this to me once, it made my head hurt."

    carpenter "There are more subtle ways customers differ, though. Some just like different things for entertainment, in and out of the sack."

    carpenter "I've designed some furniture that can attract different types so that you can tailor it to your liking."

    carpenter "Just remind 'em, though: the next one who tries to pinch my ass gets his skull split with a 10-pound hammer."

    return

label help_districts():

    sill happy "{nw}"

    menu:

        sill "This is {b}Zan{/b}, the City of Jade! From here, you can visit all of the districts you have unlocked."

        "Tell me about districts":

            sill "Zan is home to {b}six districts{/b}, from the sprawling Slums outside the city walls to the heart of the city's power: the King's Hold."

            sill "You can visit the districts that are currently unlocked, in order to meet new people or pursue some private business."

            sill "In time, you will be able to unlock new districts and relocate your brothel to fancier areas."

        "Tell me about unlocking new districts":

            sill "You need a proper brothel {b}license{/b} to move out of the Slums. Accessing the more upscale districts requires an even higher license."

            sill "When you advance in the game, you will be able to {b}relocate{/b} your brothel to a fancier district. Relocating your brothel will allow you to
                  improve the quality and size of your operation, while increasing both the difficulty and rewards of the game. You may relocate only once
                  every chapter."

            sill "New licenses and brothel relocation will become available as you advance in the game."

        "Never mind":

            return

    return


label help_visit_district():

    sill happy "From here, you can see the various locations available in {b}[district.name]{/b}. Click on their picture to visit them."

    return


label help_visit_location():

    sill happy "{nw}"

    menu:

        sill "You are visiting the {b}[selected_location.name]{/b}. From here, you can meet and chat with people, or take a random tour of the area."

        "Tell me about meeting girls":

            sill sad "Aw, Master, you're such a playboy!!!"

            sill "There are many girls idling about in Zan. You know, in this economy..."

            sill happy "Some may be happy to talk to you. Who knows, in time you might even convince them to join your workforce?"

            sill "But it will take some hard convincing. Or charms... And even then, there is no way to know in advance if the girl is any good.
                  You might be pleasantly surprised, though."

        "Tell me about looking around":

            sill "Touring the area may allow you to learn some interesting rumors or meet new people..."

            sill sad "But be careful, Master! The streets aren't safe, you know."

    return


label help_slavemarket():

    sill happy "This is the {b}slave market{/b}!"

    sill sad "I am in no hurry to go back there..."

    sill happy "At the slavemarket, you can {b}buy{/b} new girls to work for you. Watch out for their stats and traits before you decide, however."

    menu:

        sill "Do you want to know more?"

        "Tell me about girl skills and traits":

            call skills_introduction from _call_skills_introduction_1

        "Tell me more about jobs":

            call jobs_introduction from _call_jobs_introduction_1

        "Tell me about sexual experience":

            sill "Sexual experience... Well, you know... *blush*"

            sill "The slaves sold here are sex slaves. Most of them have seen some 'use' by the slavers, or their former masters.
                  There is the odd virgin, though, but even then, she has often been 'used' in other ways..."

            sill "Experienced girls are more expensive. They might not have been trained the way you'd like, though."

            sill "You can get a general idea about a slave's sexual training by looking at her experience level and stats."

        "No, I'm good":

            return

    "You can use the shortcuts to sort market girls by name, level or sexual experience (right-click on a sort method to sort backwards)."

    return


label help_shop:

    sill happy "This is the {b}item shop{/b}! From here, you can buy anything you like for you or your girls."

    sill sad "I do not like that shopkeeper, though! She cannot keep her eyes off you..."

    sill happy "There are 3 types of items: {color=[c_steel]}personal items{/color}, {color=[c_pink]}girl items{/color}, and {color=[c_orange]}gifts{/color}. Watch for the color on the item profile.
                Hover your mouse on each item or click it to learn more."

    sill "{b}{color=[c_steel]}Personal items{/color}{/b} are intended for your use."

    sill "{b}{color=[c_pink]}Girl items{/color}{/b} are intended for your girls."

    sill "{b}{color=[c_orange]}Gifts{/color}{/b} can be given to your girls or to strangers you meet in the city. You might want to learn more about a person's taste before you
          give them a present, however. Not everyone likes everything!"

    "You can use the shortcuts to sort or filter items by name, type, or cost (right-click on a sort method to sort backwards)."

    return


label help_postings():

    sill happy "{nw}"

    menu:

        sill "The {b}posting{/b} board. This is a good place to look for classes or quests!"

        "Tell me about classes":

            sill "{b}Classes{/b} can improve your girls' {b}skills{/b} as well as slightly raise their {b}reputation{/b} and {b}experience{/b}."

            sill "Committing to a class means that your girl will be away for a few days. Several girls can enroll in the same class, up to a maximum."

            sill "Please be aware that classes can only improve a girl's skill up to a point. To raise her skills further, you might need more advanced classes."

        "Tell me about quests":

            sill "{b}Quests{/b} are special requests posted by locals that your girl can fulfill. Questing rewards include {b}gold{/b}, {b}skills{/b}, {b}experience{/b} and {b}reputation{/b}."

            sill sad "Some of those quests look quite dodgy! Committing to a quest means that your girl will be away for a few days."

            sill happy "Quests are a good way to increase a girl's reputation so you can rank her up."

            sill "Watch for specific {b}traits{/b} that the customers love or hate. This might increase or decrease the reward for the quest by a large amount."

        "Never mind":

            return

    return


label help_how_to_win:

    menu:

        sill "What do you want to know about?"

        "How to win the game":

            sill "To win the game, you must reach the last chapter. As the story of Brothel King develops, proper endings will be added to the game."

        "My current goal":

            $ renpy.say(sill, game.get_goal_description(channel="advance"))

            "In addition, you may have to complete elements of the story to advance. Please hover on the bottom right message in the home screen to know your current goals."

        "Never mind":

            return

    return


label help_about_game:



    menu:

        sill "What would you like to know about this game?"

        "DISCLAIMER":

            $ text1 = """我不拥有本游戏中使用的任何图像、音乐和声音效果。我希望我可以把这些东西归功于合法的作者。
但其中大部分已经在我的硬盘上放了很久了。\n如果你是这些材料的作者，而你觉得这个游戏以任何方式侵犯了你的权利，请在[URL]论坛上联系我，我会把它从游戏中删除。\n\n
请在[URL]与我联系，以获得反馈、批评、错误报告等。"""

            call screen OK_screen("免责声明", text1)


        "What is this game?":

            $ text1 = """作为最初的《Sim Brothel》和它所激发的一些游戏的粉丝，以及像《Slave Maker》这样的游戏的粉丝，我很久以来一直想'做我自己的'，并尝试我的编码工作。

我第一次遇到Ren'py是为优秀的《Ashford Academy》游戏做了一个小MOD，从那时起，我就对Ren'py为像我这样的非编码者提供的可能性感兴趣。这就是为什么我在几年前开始了这个项目，对Ren'py和Python进行修补，直到我可以让它达到一个可玩的状态。

我现在决定向全世界发布它，看看是否能让一些人有兴趣玩它并给予一些反馈。
"""

            $ text2 = """我对这个游戏的理念很简单：让它成为我想玩的游戏。它必须有一些故事和味道，一个用户友好的用户界面，以及高质量的艺术。我还想把微观管理减少到一个可接受的水平。出于这个原因，我擅自撤销了一些我个人认为很烦人的传统模拟青楼的功能，例如在许多青楼之间玩弄女孩。

这个游戏不是一个开放式的项目。我只是一个人，我的目标是在一个现实的时间框架内提供一个完成的游戏，完成一个完整的故事和平衡的机制。在此之后，缺乏时间和注意力意味着我将无法继续增加新的功能，但我很乐意将此交给社区。
"""

            $ text3 = """顺便说一下，任何人都可以自由地修改代码，修改任何你喜欢的关于这个游戏的东西，虽然有一个严肃的警告。我不是程序员，我把这个项目作为一个机会来教自己使用ren'py和python进行编码。因此，这个游戏写得很差，有很多多余的和糟糕的代码。
如果我可以的话，我会重新开始并清理一切，但恐怕我暂时没有时间和精力去做。所以，如果你真的看了下引擎盖，那么祝你好运，还有，呃，对不起……"

请通过[URL]与我联系，以获得反馈、批评、错误报告等。
"""

            call screen OK_screen("这是个什么游戏？ (1/3)", text1)
            call screen OK_screen("这是个什么游戏？ (2/3)", text2)
            call screen OK_screen("这是个什么游戏？ (3/3)", text3)


        "How can I help?":

            $ text1 = """玩这个游戏! 到现在为止，我已经花了很多时间在这个游戏上，所以我真的不知道它是否好。如果你发现了一个错误，一个错别字（我不是母语者），有一些改善游戏性、游戏平衡或乐趣的想法，请说出来，这将对我有很大帮助。

虽然我不会从头开始重新设计所有的游戏机制，但我希望能做出很多调整，使游戏更加平衡和有趣，所以我们会阅读并欢迎你的所有建议。

如果你是一个有经验的程序员，并想看看引擎盖下的东西或修补游戏，通过各种方式，做吧！（请记住，我不需要你的帮助。(请记住，我并不真正知道如何编码，所以希望你看到的东西会让你感到害怕。)

最后，如果你有一些艺术作品可以推荐，比如好的hentai系列或符合游戏风味的音乐，通过各种方式，请这样做。

如有反馈意见、批评、错误报告等，请与我联系：[URL]。"""

            call screen OK_screen("我怎样才能提供帮助？", text1)

        "Special thanks":
            "Thanks to all the people on the [URL] forum for their support and all the good ideas, girl packs and mods they contributed."

            "Special thanks to OhWee for making some great screens (including the load/save screen and the input screen)."

            "Special thanks to kite80, Dragonblood, Chris12, OhWee, Xela, and all the early testers, for helping me with develop the story, improve gameplay, and learn some coding along the way."

        "I have a bug to report/gameplay suggestion":

            "Contact me at [URL] for feedback, criticism, bug reports, etc."


        "Never mind":

            return

    jump help_about_game


label help_night_events:

    menu:

        sill "{b}Night events{/b} are where the action is!"

        "Tell me about brothel reputation and customers":

            sill "Every night, customers will flock to your brothel in the hope of getting some action, both in the form of entertainment and sex.
                  How many customers actually show up depends on your {b}brothel reputation{/b}."

            sill "Each customer has his own preferences in terms of entertainment and sexual practices. Meeting your customers expectations is key to
                  their satisfaction."

            sill "Eventually, your brothel's reputation will rise or fall depending on how many customers have been entertained and sexually gratified."

            sill "If no girls are working at the brothel on a given night, the brothel will close. Security and advertising babes will go home.
                 You will still have to pay for upkeep and maintenance."

        "Tell me about advertising, security and maintenance":

            sill "{b}Advertising{/b} is pretty straightforward. Get a bunch of young, hot girls out there with signs, flyers or bodily tattoos with the brothel's name on it,
                 and its reputation will increase. Reputation begets more customers."

            sill "If your {b}brothel security{/b} is insufficient, your brothel may suffer from attacks during the night. Attacks can deplete your money, hurt your girls and damage
                  their mood, so watch out!"

            menu:
                sill "Would you like to know more about security?"

                "Yes":
                    call help_security from _call_help_security_1
                "No":
                    pass

            sill "Customers are messy and will dirty up the place every night as they go about their business. {b}Maintenance{/b} is essential is you don't want your brothel to become a hotbed
                  for disease. By the way, sex is dirtier than entertainment."

            sill "If no girls are working at the brothel on a given night, the brothel will close. Security and advertising babes will go home.
                 You will still have to pay for upkeep and maintenance."


        "Tell me about girl performances":

            sill "Every night, the available working girls will {b}perform{/b} for the visiting customers."

            sill "Some girls might rebel and go on strike. This happens when their mood and/or obedience is too low."

            sill "The girls that do work will service the customers by doing their job or performing sex acts. Each customer will choose the form of entertainment
                  and sex act that matches his tastes, if a girl is available."

            sill "Performance depends on a number of factors: customer difficulty (which is higher in fancier districts), girl skills and job level, bedroom quality,
                  special items, and so on."

            sill "A good performance will massively increase the rewards from the customers, especially the tipping."

        "Never mind":

            return

    return

label security_introduction:

    sill sad "Master! Something happened last night!"

    menu:
        "You've just had your first security event. Would you like to learn more about security events?"

        "Yes":
            call help_security from _call_help_security_2
        "No":
            pass

    return

label help_security:

    sill happy "Security events happen when the {b}threat{/b} to your brothel is high, or when {b}crazy customers{/b} visit your brothel."

    sill "Brothel {b}Threat{/b} is based on your gold and the number of working girls in your brothel. Higher ranking girls attract more threat."

    sill "Security is based on your available goons. Your Strength counts too, but only if you have remaining AP at the end of the day or the 'Defender' talent."

    sill "Threat builds up more or less quickly depending on your level of security. Over time, {b}security events{/b} will happen, although it will happen much less often if you have adequate security. A good level of security will help mitigate the results of security events as well."

    sill "Be careful! Security events may {b}escalate{/b} over time, until something really bad happens."

    sill "Another risk to your brothel is {b}crazy customers{/b}. Crazy customers may attack your girls or brothel. Because they are customers, it's hard to prevent them from coming in, but your security level may help avoid negative consequences. Arming your girls is also a good option."

    sill "Some customer populations, like thugs, are well-known for causing trouble. So watch out!"

    return

label help_rank_introduction:

    sill happy "Rank is a very important factor for a sex slave!"

    sill "In Zan, regular citizens are only allowed to own common sex slaves. Owning sex slaves of a higher rank requires a suitable brothel license. As you unlock
          better licenses, you will be able to upgrade your girls' rank further."

    sill "Common slaves are known as rank 'C'. Better sex slaves can reach rank 'B', 'A', then 'S' for the most special sex slaves. Some say there is a even higher rank,
          accessible only to the most legendary sex slaves... But if it exists, it is a well-kept secret."

    sill "Reaching a new rank is difficult. First, a girl must have reached the {b}maximum level{/b} for her rank (for rank 'C', she must be level 5). She must also have a
          high enough {b}reputation{/b} with her customers."

    sill "Girls can earn reputation when performing well with customers, and when accomplishing special quests."

    sill "A higher rank allows you to train a girl's stats and job skills further, increase her level cap, and affects many other aspects of the game."

    sill "But ranking up costs money, and higher rank girls are also more expensive to maintain. They are also more fickle: all this glory is getting to their head."

    $ rk = rank_name[district.rank]

    sill "With your current license, you can train girls up to rank [rk]."

    return

## FARM HELP ##

label help_farm_question():
    menu:
        gizel "Do you need some help with the farm?"

        "Yes":
            call help_farm() from _call_help_farm_2
        "No":
            pass

    return

label help_farm():
    gizel normal "The 'farm' is the unoriginal name you stupid humans give this place."

    gizel "Of course, it is much more than that. It is a shining place of power acting like a beacon through space and time, sitting on a whirlpool of dark magical energy..."

    you "Yeah yeah. To the point, Giz'."

    gizel upset "Hmpf! You're just a foolish barbarian. Anyway. I'll just stick to concepts you can easily understand."

    you "*sigh* You do that..."

    gizel normal "{nw}"

label help_farm_menu():

    menu:
        gizel "What do you want to know, then?"

        "Tell me about the farm":

            gizel "You can send girls here at the {b}farm{/b}, where they will remain in my care for a fixed duration, or until you want them back."

            gizel "The girls will be held in {b}pens{/b} here with my animals and minions for company. While they're here, they won't be using their room in the brothel, so you are free to assign it to someone else."

            gizel "For training, I will use the farm {b}facilities{/b} and my sweet {b}minions{/b}. Each facility is suitable for only one type of minions."

            "You can use the shortcuts to sort your girls by name, level or rank (right-click on a sort method to sort backwards)."

        "Tell me about pens and facilities":

            gizel normal "Certainly. {b}Pens{/b} are where your girls are being kept while they are at the farm. {b}Facilities{/b} are where I host my beloved minions."

            gizel "Because the farm was in such a state of disrepair when we got it, not all pens and facilities will be immediately available, however."

            gizel "If you have the coin, you can build new {b}pens{/b} to hold more girls at the farm. The farm's {b}facilities{/b} can be also rebuilt and improved on, which will increase the number of minions they can hold."

            gizel "Our activities here are a bit unusual, I guess, and might attract attention from the wrong crowd... Like those Arios-worshipping apes. So let's keep our little operation quiet."

            $ p = farm.get_pen_limit()

            gizel "Right now, we can build a maximum of [p] pens and improve our facilities up to level [district.rank], before the neighbors get suspicious."

            if district.rank == 5:
                extend " This is the farm's maximum capacity, so we cannot improve our facilities beyond that."
            else:
                extend " We can develop the farm further if you obtain a higher brothel license and some protection in high places."

        "Tell me about minions and facilities":

            gizel smirk "Ah, the minions! My little babies, my loves..."

            gizel normal "There are various kinds of minions, using various facilities."

            gizel "Minions are useful for training. It takes at least one minion to train a girl, so make sure you have enough minions to do the work."

            gizel "You can find new minions in town, I guess, but I'm not sure where. I don't go out much."

            gizel "The {b}Stallions{/b}, such as my beloved Bob, are held in the {b}Stables{/b}, in the barn."

            gizel "Stallions are magically brainwashed sex-slaves from the Blood Islands, bred selectively for their unnaturally large dicks..."

            you "Freaky..."

            if farm.installations["pig stall"].rank > 0:
                gizel "The {b}Beasts{/b} stay in the {b}Pig stall{/b}."

                gizel "Beasts are simply animals, but I have fun messing around with their natural instincts with magic.
                       They're not just pigs too: their structure is so basic I can morph them into different animals when the need arises."

                you "Cool..."

            else:
                gizel "There's an old pig stall in the courtyard... I guess we could use it to hold some {b}animals{/b}."

            if farm.installations["monster den"].rank > 0:
                gizel "The {b}Monsters{/b} dwell underground in the {b}Monster den{/b}, where else?"

                gizel "Monsters come in many shapes and forms, but they are all hungry for juicy nipples and wet holes... I wouldn't have them any other way!"

                you "Spooky..."

            else:
                gizel "I spotted the entrance to an old cellar in the back, which seems linked to an ancient and intricate cave network... A perfect place to breed {b}monsters{/b}, I should say."

            if farm.installations["workshop"].rank > 0:
                gizel "Finally, there are the {b}Machines{/b}, which are kept in the {b}Workshop{/b} at the back."

                gizel "Those machines aren't the crude tools your backward species use either... They are artefacts of great magical power,
                       designed with one thing in mind: pleasure. Or pain. What was the difference you people make between both, again? This always confused me!"

                you "Nerdy..."
            else:
                gizel "Finally, there's the old toolshed in the farmhouse, I could repurpose it to hold various artefacts and {b}machines{/b}... I have plenty of ideas..."

            gizel smirk "My minions will take good care of your slaves! *smirk*"

            gizel normal "As they play around with your girls, minions will earn {b}experience{/b}. Eventually, they might become more powerful. And more power means one thing of course: BIGGER DICKS!!!"

            you "..."

            gizel normal "But watch out for the minions and their health. If you take good care of them, and deliver them a steady flow of dumb sluts to play with,
                          they will serve you better over time."

            gizel "Finally, you should note that for {b}group sex training{/b}, I'll need more than one minion of the same type. But that's obvious, right?"

        "Tell me about girl training and rules":

            gizel normal "Right, let's get to the main reason we're here. {b}Training{/b}."

            gizel "Basically, there are two kinds of things I can do with your girls while they're at the farm."

            gizel "First, I can simply keep them locked in a pen. This is what I call {b}holding{/b}. Nothing will happen to them then, however, so that's not FUN."

            gizel "Fortunately, I can spice things up by setting {b}holding rules{/b}."

            call help_farm_rules_holding from _call_help_farm_rules_holding

            gizel normal "Next, you can let my minions play with your girls to {b}train{/b} them."

            gizel "I can train your girls for all kinds of sex acts with my minions here. Depending on the {b}rules{/b} you choose for their training, I can go soft or hard on the little bitches...
                   But who doesn't like it hard?"

            call help_farm_rules_training from _call_help_farm_rules_training

            gizel "Because we work and play hard here at the farm, your girls will occasionally {b}get tired{/b}, being wimps and all."

            call help_farm_rules_resting from _call_help_farm_rules_resting

#         "Tell me about training objectives and duration":

#             gizel normal "When you send a girl to train with me, you can decide to set a specific {b}training objective{/b} or {b}duration{/b}."

#             gizel "A {b}training objective{/b} is a condition that tells me when to stop training a particular sex act. Once the girl reaches a given threshold, I will send her back to you, or switch to a different training."

#             gizel "{b}Duration{/b} is simply how many days you want me to hold on to a girl before I send her back. Regardless of training advancement, she will be brought back at the end of that duration."

#             gizel "Please note that when {b}punishing{/b} a girl by sending her to the farm, you cannot take the girl back until she has served here for the chosen duration. Discipline is paramount, you know."

#             gizel normal "Make sure you have enough room in your brothel before I bring a girl back, though. I do so {i}hate{/i} to drag myself, and a whining bitch, all the way to your place for nothing."

#             gizel smirk "Of course, you're free not to set any condition, and keep a girl at the farm indefinitely. I have many {i}ways{/i} to keep the slaves entertained, don't you worry..."

        "Go back":
            return

    jump help_farm_menu


label help_farm_rules_training():

    gizel normal "{b}Training rules{/b} are very important. Most importantly, they affect the amount of FUN {b}I{/b} get while training your dumb sluts."

    gizel "The most boring and useless option is to go '{b}soft{/b}' on the bitches. When going soft, I won't make them do anything they don't already agree to."

    gizel upset "Can't you see how lame it is! LAME! Never choose this option, ever! *mad*"

    gizel normal "The second option is to go '{b}hard{/b}' on them. When being trained hard, I'll ignore most of the girls' complaints and threaten the dumb slaves into submission.
                  I'll push them hard, but I won't go all out on them just yet, introducing them to harder sex acts gradually."

    gizel "Finally, you can leave it all to me... This is what I call the '{b}hardest{/b}', or most FUN, option."

    gizel smirk "In hardest mode, I will ignore any and all complaints your girls have, even if they try to fight it, and inflict on them whatever hardcore sex act I wish on a whim. They will be harshly punished if they disobey."

    gizel "Now isn't that FUN? Muhahahaha!"

    gizel upset "But let's be careful, because some hard-headed sluts might try to fight back... Make sure you disarm the bitches before sending them here, or we'll be in trouble."

    return

label help_farm_rules_resting():

    gizel normal "I've never understood this concept of {b}rest{/b} myself, being blessed with endless libido and stamina."

    gizel "But petty lifeforms like yours seem to need it, otherwise they just become exhausted or even injured. Lame."

    gizel "So if you want, I can keep an eye on your girls' level of {b}energy{/b}, and remove them from working or training if they become too weak."

    gizel "I'll set them to rest automatically before they become exhausted. Of course, I could always misjudge and injure a slave or two if I'm not paying attention, but who CARES!"

#     gizel "If you want me to be {b}conservative{/b}, I'll always rest your girls before they have any chance to become exhausted."

#     gizel upset "Have I mentioned this is for sissies and weaklings? I'm sure you wouldn't ever consider that."

#     gizel normal "I can also work your girls in a more {b}intensive{/b} way. This means I'll wait until the last minute to rest them. This can result in some girls becoming exhausted from time to time,
#                   but no pain, no gain... You know."

#     gizel "Finally, you can choose '{b}no rest{/b}', and I can leave this resting business aside altogether. Train the girls 'til they drop, or choose when to remove them yourself. It's all the same to me."

#     gizel smirk "Of course, we could injure a slave or two in the process, but who CARES!"

    return


label help_farm_rules_holding():

    gizel normal "While your girls are not in training, you can choose what you want them to do during their stay ({b}holding{/b})."

    gizel "Because an idle slave is prone to become a fat and lazy cow, I recommend keeping them busy at all times!"

    gizel "While you keep them busy, their {b}skills{/b} will improve... But they will get tired, and whine. They always do."

    gizel "Alternatively, you can set them to {b}rest{/b}, and the spoiled sluts will do nothing but recover their {b}energy{/b}."

    gizel upset "Why not give them a nice massage, and a pouch of gold too, why don't you? *hiss*"

    return


label help_zodiac():

    sill happy "I read a fascinating story... Astrology is very popular in Zan, and {b}Zodiac saints{/b} play a foremost role at every level of society."

    sill "Different classes of people have different belief systems. They have hundreds of popular spirits and other minor deities to choose from..."

    you "Oh, really? Does that sit well with the major religions?"

    sill "Well, the established religions don't really bother with mere superstitions such as the Zodiac saints... They find a way to include the saints in their own particular pantheon, in one way or another."

    sill "For instance, the women of Zan follow {b}the Eight{/b} for good fortune, especially slaves and whores. The Eight are saintly women-like figures that appear in the heavens when the conditions are right."

    sill "By dedicating ourselves to a particular {b}Zodiac saint{/b}, we believe that we can improve and be better at serving our purpose."

    you "Sounds nice."

    sill "Every slave girl and prostitute follows a few of those Saints. A new girl will usually follow one or two of those depending on her natural inclinations."

    sill "With experience, girls can learn to pay their respects to different deities or deepen their relationship with one they already follow. The saints are rumored to grant {b}perks{/b} to their followers, each according to their own character."

    sill "No girl can get all the benefits of all zodiac signs at once, though. They have to carefully choose their path."

    "Every girl starts with {b}one or two zodiac signs{/b} unlocked according to her base traits."

    "If a girl has only one zodiac sign unlocked, she receives the first perk for that sign for free."

    "Every level, a girl receives {b}one or two perk points{/b}. Perk points can be used to unlock a new zodiac sign, or learn a new perk."

    "Higher-end perks can only be bought after the girl improves her rank. To learn more, click on the level up or perks button in the girls tab."

    return


## CHEATS ##

label cheat_menu():

    sill sad "{nw}"

    menu:

        sill "WARNING! These cheats are for testing purposes, and may easily break your game! Only call this menu from the Home screen."

#        "Test line counting" if debug_mode:

#            $ text1 = "abcdefghijklmnopqrstuvwxyz7890abcdefghijklmnopqrstuvwxyz7890abcdefghijklmnopqrstuvwxyz7890abcdefghijklmnopqrstuvwxyz7890abcdefghijklmnopqrstuvwxyz7890"
#            $ line_count = count_lines(text1, 60)

#            "[text1]"

#            "Line count is [line_count]."

#        "Test too tired":
#            call too_tired(MC.girls[0])

#        "Test security" if debug_mode:

#            while True:
#                menu:
#                    "Continue?"
#                    "Yes":
#                        pass
#                    "No":
#                        jump main

#                $ log = Log(calendar.time)
#                $ working_girls = MC.girls

#                if brothel.threat_build_up(): # Returns True if security event may proc
#                    hide screen home
#                    hide screen tool
#                    with dissolve

#                    stop music fadeout 3.0

#                    scene black with Fade(0.15, 0.3, 0.15)

#                    call security(working_girls, ev_type="raid")

#        "List items" if debug_mode:

#            python:

#                for dis in district_dict.values():
#                    renpy.say(dis.name + " junk", and_text([it.name for it in dis.items["junk"]]))
#                    renpy.say("common", and_text([it.name for it in dis.items["common"]]))
#                    renpy.say("rare", and_text([it.name for it in dis.items["rare"]]))
#                    renpy.say("exceptional", and_text([it.name for it in dis.items["exceptional"]]))


        "Test event" if debug_mode:

            $ test_event_name = renpy.input("Event name", default=test_event_name)

            $ selected_district = district_dict["slum"]
            $ selected_location = rand_choice(all_locations)

            hide screen home
            hide screen tool

            scene black with fade

            $ renpy.call("display_events", [StoryEvent(label=test_event_name)])

            $ renpy.pop_call()

            jump main

#        "Test girl story" if debug_mode:

#            $ ev = renpy.input("Event name", default = "slave_story1")
#            $ free = bool(renpy.input("Free", default = ""))

#            $ girl = get_girls(1, free=free)[0]
#            $ girl.free = free
#            $ girl.personality = gpersonalities[renpy.input("Personality", default = girl.personality.name)]
#            $ girl.rank = 5

#            menu:
#                "Select stage"

#                "First":
#                    $ girl.flags["story"] = 4
#                "Second":
#                    $ girl.flags["story"] = 10
#                "Third":
#                    $ girl.flags["story"] = 20
#                "Repeat choices":
#                    $ girl.flags["story"] = 50

#            $ renpy.call(ev, girl)

#            return

        "Cheat modifier":

            menu:
                "The cheat modifier is a float number affecting stat gains, xp, jp, reputation and gold earned by your girls. Use it to adjust the difficulty level (e.g.: a modifier of 1.5 gives your girl a 50\% increase); a modifier of 0.75 decreases gains by 25\%)"

                "Set global cheat modifier":
                    $ global_cheat_modifier = float(renpy.input("Cheat modifier", default = 1.0))

                    python:
                        for cheat in cheat_modifier.keys():
                            cheat_modifier[cheat] = global_cheat_modifier

                "Set modifiers separately":
                    $ cheat_modifier["gold"] = float(renpy.input("Gold cheat modifier", default = cheat_modifier["gold"]))
                    $ cheat_modifier["xp"] = float(renpy.input("XP cheat modifier", default = cheat_modifier["xp"]))
                    $ cheat_modifier["jp"] = float(renpy.input("JP cheat modifier", default = cheat_modifier["jp"]))
                    $ cheat_modifier["rep"] = float(renpy.input("Girl reputation cheat modifier", default = cheat_modifier["rep"]))
                    $ cheat_modifier["stats"] = float(renpy.input("Girl stats cheat modifier", default = cheat_modifier["stats"]))
                    $ cheat_modifier["prestige"] = float(renpy.input("Prestige cheat modifier", default = cheat_modifier["prestige"]))


        "Gold":

            menu:

                "Get 1,000 gold":
                    $ MC.gold += 1000

                "Get 10,000 gold":
                    $ MC.gold += 10000

                "Get 100,000 gold":
                    $ MC.gold += 100000

                "Custom amount":
                    $ MC.gold += int(renpy.input("How much?"))

                "Back":
                    jump cheat_menu


        "Main character":

            menu:
                "Level MC":
                    python:
                        nb = int(renpy.input("How many levels?", default = "1"))

                        for i in xrange(nb):
                            MC.level_up(forced = True)

                "Reset interactions":
                    $ MC.reset_interactions()

                "Check MC effects":

                    python:

                        brothel.update_effects()

                        for eff in MC.effects:

                            renpy.say("", eff.target + " " + str(eff.value))


                "Back":

                    jump cheat_menu


        "Girls":

            menu:
                "Get naked":
                    python:
                        for girl in MC.girls:
                            girl.naked=True
                            girl.refresh_pictures()

                "Give girls perk points":

                    $ nb = int(renpy.input("Perk points", default = "1"))

                    python:
                        for girl in MC.girls:
                            girl.perk_points += nb

                "Give girls upgrade points":

                    $ nb = int(renpy.input("Upgrade points", default = "10"))

                    python:
                        for girl in MC.girls:
                            girl.upgrade_points += nb

                "Rank girls up":
                    $ nb = int(renpy.input("How many ranks", default = "1"))
                    python:
                        for girl in MC.girls:
                            for i in xrange(nb):
                                girl.rank_up(forced = True)

                "Level girls up":
                    python:
                        for girl in MC.girls:
                            girl.level_up(forced = True)

                "Job skill up":
                    $ job = renpy.input("Choose skill to improve", default = "waitress").lower()

                    python:
                        for girl in MC.girls:
                            girl.job_up(job, forced = True)

                "Raise libido and obedience" if debug:
                    $ val = int(renpy.input("Raise libido/obedience", default = 50))
                    python:
                        for girl in MC.girls:
                            girl.change_stat("obedience", val)
                            girl.change_stat("libido", val)

                "Raise sexual preferences" if debug:
                    $ val = int(renpy.input("Raise all sexual preferences", default = 1000))
                    python:
                        for girl in MC.girls:
                            for s in extended_sex_acts:
                                girl.change_preference(s, val)

                "Set all girls to rest":
                    python:
                        for girl in MC.girls:
                            girl.set_job(None, forced=True)

                "Sell all girls":
                    python:
                        for girl in MC.girls:
                            MC.gold += girl.get_price("sell")
                        MC.girls = []
                    play sound s_gold

                "Give all girls a random job":
                    python:
                        for girl in MC.girls:
                            if girl.will_do("whore"):
                                girl.set_job("whore")
                            else:
                                girl.set_job(rand_choice(all_jobs))

                "Fully rest girls":
                    python:
                        for girl in MC.girls:
                            girl.change_energy(250)
                            girl.heal(99)

                "Reset girl interactions":
                    python:
                        for girl in MC.girls:
                            girl.reset_interactions()

                "Change love":

                    $ nb = int(renpy.input("Change", default = "10"))

                    python:
                        for girl in MC.girls:
                            girl.change_love(nb)

                "Change fear":

                    $ nb = int(renpy.input("Change", default = "10"))

                    python:
                        for girl in MC.girls:
                            girl.change_fear(nb)

                "Force girl to run away" if debug_mode:
                    call run_away(MC.girls[0]) from _call_run_away_2


                "Back":
                    jump cheat_menu

        "Free girls":

            menu:

                "Get new free girls":
                    $ game.free_girls = []
                    $ update_free_girls()
                    $ cycle_free_girls()
                    $ renpy.restart_interaction()

                "Update free girls":
                    $ update_free_girls()
                    $ renpy.restart_interaction()

                "Cycle free girls":
                    $ cycle_free_girls()
                    $ renpy.restart_interaction()

                "Reset girl interactions":
                    python:
                        for girl in game.free_girls:
                            girl.reset_interactions()

                "List free girls":
                    python:
                        l = []
                        for g in game.free_girls:
                            l.append(g.fullname + " (id: " + str(g.id) + ")")
                        renpy.say("", "自由女孩：" + and_text(l))

                "Back":
                    jump cheat_menu

        "Items":

            menu:

                "Refresh shops":

                    $ update_shops()


                "Get all items":

                    python:

                        for it in all_items + extractor_items.values():

                            MC.items.append(copy.deepcopy(it))

                "Get item":

                    $ name = renpy.input("Item name contains")

                    python:

                        for it in all_items + extractor_items.values():

                            if name in it.name:

                                MC.items.append(copy.deepcopy(it))

                "Clear items":

                    $ MC.items = []

                "Build all furniture":
                    python:
                        for furn in all_furniture:
                            furn.build(message=False)
                        all_furniture.append(vitals_scanner)
                        all_furniture.append(billboard)

                "Back":
                    jump cheat_menu

        "Tags":
            menu:
                "Check girls for missing pictures (main)":

                    call check_missing_pictures("main") from _call_check_missing_pictures

                "Check girls for missing pictures (optional)":

                    call check_missing_pictures("optional") from _call_check_missing_pictures_1



                "Check untagged girl pics":

                    "This allows you to check if some girl pics have no usable tags (excluding the 'unused' tag)."

                    python:
                        if untagged_pics:
                            for p in untagged_pics:
                                renpy.say("", "无法标记 " + p)
                        else:
                            "No picture found missing a tag"

                "Check tags for duplicates":
                    python:
                        for tag in tag_dict.keys():
                            for tag2 in tag_dict.keys():
                                if tag in tag2 and tag != tag2:
                                    renpy.say("", "警告：" + tag + " 在 " + tag2 + " 中。")

        "Others":

            menu:

                "Test brothel events" if debug_mode:
                    python:
                        ev_list = []
                        for key, pic_list in security_pics.items():
                            for pic in pic_list:
                                ev_list.append(Event(Picture(pic, "events/" + pic), text = "", sound = s_cash))

                    while ev_list:
                        $ ev = ev_list.pop(0)

                        call show_night_event(ev) from _call_show_night_event_4

                "Change brothel reputation":
                    $ brothel.rep = int(renpy.input("Brothel reputation", default = brothel.rep))

                "Refresh slave market":
                    $ update_slaves()
                    jump slavemarket

                "Refresh postings":

                    $ update_quests()
                    $ selected_girl, available_girls = refresh_quest_girls(selected_girl, selected_quest)

                "Toggle secret locations":
                    call toggle_secrets from _call_toggle_secrets

                "Skip time":

                    $ t = int(renpy.input("How many days do you want to skip", default = 1))

                    $ calendar.newday(t)

                "Advance to chapter":

                    $ c = int(renpy.input("Advance to chapter", default = game.chapter + 1))

                    $ renpy.call("advance_to_chapter", c, silent=True, free=True)

                    jump brothel

                "Change goal":

                    menu:

                        "What type of goal are you going to achieve?"

                        "Raise gold":
                            $ type = "gold"
                            $ val = int(renpy.input("How much gold will you need?", default = 2500))
                            $ target = 0

                        "Rank up your girls":
                            $ type = "ranked"
                            $ val = int(renpy.input("Which rank will they need to reach?", default = 2))
                            $ target = renpy.input("How many girls will need to reach that rank?", default = 4)

                        "Raise brothel reputation":
                            $ type = "reputation"
                            $ val = int(renpy.input("How much reputation will you need to get?", default = 250))
                            $ target = 0

                        "Raise player prestige":
                            $ type = "prestige"
                            $ val = int(renpy.input("How much prestige will you need to collect?", default = 1000))
                            $ target = 0

                    $ game.goals = (Goal(type, val, target, channel="advance"),)
                    $ renpy.say(sill, game.get_goal_description(channel="advance"))

                "Check goals" if debug_mode:

                    $ text1 = ""

                    python:
                        for g in game.goals:

                            if g.reached():
                                text1 += "开启 "
                            else:
                                text1 += "关闭 "
                    $ renpy.say("", text1)

#                 "Reset girlpack ratings":
#                     $ rating_dict = defaultdict(dict)

#                 "Repair safes":
#                     call repair_safes() from _call_repair_safes


                "List available story events":

                    $ renpy.say("", and_text([ev.label for ev in city_events]))

#                "Repair farm bugs":
#                    if renpy.call_screen("yes_no", "This will reset programs to default for all girls in the farm. Would you like to proceed?"):
#                        $ farm.reset()

#                "Test perks" if debug_mode:
#                    jump test_perks

#                "Test tip" if debug_mode:

#                    hide screen home
#                    hide screen overlay

#                    label test_tip:
#                        python:
#                            rank = int(renpy.input("Girl rank"))
#                            cust_nb = int(renpy.input("Service customer number"))
#                            cust_nb2 = int(renpy.input("W customer number"))
#                            diff = int(renpy.input("Customer difficulty"))

#                            g = Girl()
#                            g.rank = rank
#                            cust_list = []

#                            for i in range(cust_nb):
#                                c = Customer(district)
#                                c.diff = diff
#                                cust_list.append(c)

#                            results = []

#                            for act in all_jobs:
#                                min_t = g.get_tip(act, "very bad", cust_list)
#                                max_t = g.get_tip(act, "perfect", cust_list)
#                                results.append((act, min_t, max_t))

#                            for act in all_sex_acts:
#                                min_t = g.get_tip(act, "very bad", (cust_list[0],)) * cust_nb2
#                                max_t = g.get_tip(act, "perfect", (cust_list[0],)) * cust_nb2
#                                results.append((act, min_t, max_t))

#                            text1 = ""

#                            for res in results:
#                                text1 += res[0][:1] + ": " + str(res[1]) + "/" + str(res[2]) + "\n"

#                        call screen OK_screen("RESULTS", text1)

#                        menu:
#                            "Test again?"

#                            "Yes":
#                                jump test_tip
#                            "No":
#                                return

                "Check active brothel effects" if debug_mode:
                    python:
                        for eff_list in brothel.effect_dict.values():
                            for eff in eff_list:
                                renpy.say("", eff.type + ", " + eff.target + ", " + str(eff.value))

                "Add minion" if debug_mode:
                    menu:
                        "Stables":
                            $ farm.installations["pig stall"].minions.append(Minion("stallion"))
                        "Pig stall":
                            $ farm.installations["pig stall"].minions.append(Minion("beast"))
                        "Monster den":
                            $ farm.installations["pig stall"].minions.append(Minion("monster"))
                        "Workshop":
                            $ farm.installations["pig stall"].minions.append(Minion("machine"))


                "Get resources":
                    python:
                        nb = int(renpy.input("How many?", 50))
                        for resource in build_resources:
                            MC.gain_resource(resource, nb, message=False)

                "Wound minions":
                    python:
                        for mn in farm.get_minions("stallion"):
                            mn.hurt = True

#                "Set alarms":
#                    $ calendar.set_alarm(calendar.time + 1, Event(label = "test1"))
#                    $ calendar.set_alarm(calendar.time + 1, Event(label = "test2"))
#                    $ calendar.set_alarm(calendar.time + 1, Event(label = "collect_wood"))

                "Back":
                    jump cheat_menu

            return

#        "TEST FARM SCREEN":

#            show screen night(event_pic = farm.get_pic("anal"))

##            $ ev = Event(pic="gizel whip", background=Picture("pen.jpg", "brothels/rooms/pen.jpg"))
##            show screen night(event_pic = ev.pic, event_bg = ev.background)
#            ""
#            hide screen night

#        "Generate names":
#            python:
#                text1 = ""

#                for i in xrange(50):
#                    text1 += generate_name("stallio") + ", "

#                text1 = text1[:-2]

#            "[text1]"


        "Nothing":

            return

    return

label check_missing_pictures(type):

    python:
        template_girls = generate_girls()

        for girl in template_girls:
            girl.randomize(force_original=True)

    menu:
        "Choose an option"

        "Check all girl packs":
            pass

        "Check a specific girl pack":
            $ girl = long_menu("Select a girl pack", [(" ".join(get_name(girl.path)), girl) for girl in template_girls])
            $ template_girls = [girl]

    if type == "main":

        "Step 1: Checking profile and portrait pictures"

        python:
            missing = defaultdict(list)
            for girl in template_girls:
                for tag in ["profile", "portrait"]:
                    if not girl.get_pic(tag, not_tags = "naked", strict=True):
                        missing[tag].append(girl.fullname)

            for tag in ["profile", "portrait"]:
                if missing[tag]:
                    renpy.say("", and_text(missing[tag]) + ": 缺少 {b}" + tag + "{/b} 图片。")
                elif len(template_girls) > 1:
                    renpy.say("", "没有女孩缺少 " + tag + " 图片。")


        "Step2: Checking job/sex pictures"

        python:
            for girl in template_girls:
                for tag in ["rest", "waitress", "dancer", "masseuse", "geisha"]:
                    if not girl.get_pic(tag, not_tags = ["naked"], strict=True):
                        missing[tag].append(girl.fullname)
                for tag in ["service", "sex", "anal", "fetish"]:
                    if not girl.get_pic(tag, not_tags = ["group", "bisexual", "beast", "monster", "machine"], strict=True):
                        missing[tag].append(girl.fullname)

            for tag in ["rest", "waitress", "dancer", "masseuse", "geisha", "service", "sex", "anal", "fetish"]:
                if missing[tag]:
                    renpy.say("", and_text(missing[tag]) + ": 缺少常规 {b}" + tag + "{/b} 图片。")
                elif len(template_girls) > 1:
                    renpy.say("", "没有女孩缺少 " + tag + " 图片。")


        "Step3: Checking naked pictures"

        python:
            missing = defaultdict(list)
            for girl in template_girls:
                for tag in normal_tags:
                    if not girl.get_pic(tag, and_tags = "naked", strict=True):
                        missing[tag].append(girl.fullname)

            for tag in normal_tags:
                if missing[tag]:
                    renpy.say("", and_text(missing[tag]) + ": 缺少{b}裸体 " + tag + "{/b} 图片。")
                elif len(template_girls) > 1:
                    renpy.say("", "没有女孩缺少裸体 " + tag + " 图片。")

        "Step4: Checking group and bisexual sex pictures"

        python:
            for girl in template_girls:
                for tag in ["group", "bisexual"]:
                    for act in all_sex_acts:
                        if not girl.get_pic(tag, and_tags=act):
                            missing[(tag, act)].append(girl.fullname)

            for tag in ["group", "bisexual"]:
                for act in all_sex_acts:
                    if missing[(tag, act)]:
                        renpy.say("", and_text(missing[tag]) + ": 缺少 {b}" + tag + " " + act + "{/b} 图片。")
                    elif len(template_girls) > 1:
                        renpy.say("", "没有女孩缺少 " + tag + " " + act + " 图片。")

    elif type == "optional":

        "Step1: Checking farm pictures"

        python:
            missing = defaultdict(list)
            for girl in template_girls:
                for tag in ["big", "beast", "monster", "toy"]:
                    for act in extended_sex_acts:
                        if not girl.get_pic(tag, and_tags=act, strict=True):
                            missing[(tag, act)].append(girl.fullname)

            for tag in ["big", "beast", "monster", "toy"]:
                for act in extended_sex_acts:
                    if missing[(tag, act)]:
                        renpy.say("", and_text(missing[(tag, act)]) + ": 缺少 {b}" + tag + " " + act + "{/b} 图片。")
                    elif len(template_girls) > 1:
                        renpy.say("", "没有女孩缺少 " + tag + " " + act + " 图片。")

        "Step2: Checking optional fixation pictures"

        python:
            for girl in template_girls:
                for fix in fix_dict.values():
                    for act in fix.acts:
                        if not girl.get_pic(fix.tag_list[0], and_tags=act, not_tags= fix.not_list, strict=True):
                            missing[(fix, act)].append(girl.fullname)

            for girl in template_girls:
                for fix in fix_dict.values():
                    for act in fix.acts:
                        if missing[(fix, act)]:
                            renpy.say("", and_text(missing[(fix, act)]) + ": 缺少 {b}" + act + " " + fix.name + "{/b} 图片")
                        elif len(template_girls) > 1:
                            renpy.say("", "没有女孩缺少 " + act + " " + fix.name + " 图片。")

    "End of picture check."

    return


label debug_load_chapter(chapter, c1_path="good"):

    if not 0 < chapter <= 7:
        return

    python:
        if chapter > 6:
            district = endless_district
            game.blocked_districts = all_districts
        else:
            district = all_districts[chapter-1]
            game.blocked_districts = all_districts[:chapter-1]

        if chapter > 1:
            story_flags["c1_path"] = c1_path
            extras_dict["locations"] = True
            extras_dict["farm"] = True

            if chapter > 2:
                extras_dict["carpenter"] = True

                if chapter > 6:
                    extras_dict["shops"] = 6
                    extras_dict["resources"] = 6
                elif chapter > 4:
                    extras_dict["shops"] = 4
                    extras_dict["resources"] = 4
                else:
                    extras_dict["shops"] = 2
                    extras_dict["resources"] = 2
            else:
                extras_dict["shops"] = 1
                extras_dict["resources"] = 1

            unlocking_extras()

        bg_bro = "bg brothel" + str(chapter)
        brothel = copy.deepcopy(blist[chapter])
        brothel.setup("Debug Palazzio", free_room=district.room)
        get_starting_furniture(chapter)


        for girl in MC.girls:
            girl.debug_auto_level(chapter)

        calendar.updates()
        refresh_available_locations()
        reset_girl_jobs()

    return


label invoke_packstate_log():
    $ os.chdir(config.gamedir[:config.gamedir.rfind("/")])
    $ os.startfile(str("packstate_log.txt"))
    return


label repair_chapter2():

    python:
        NPC_homura = NPC(name="Homura", char=homura)

        event_dict["c2_suzume_arena"] = StoryEvent(label = "c2_suzume_arena", chapter=2, location = "arena")
        event_dict["c2_suzume_forest2"] = StoryEvent(label = "c2_suzume_forest2", chapter=2, location = "farm")
        event_dict["c2_suzume_brothel"] = StoryEvent(label = "c2_suzume_brothel", chapter=2, location = "seafront")
        event_dict["c2_homura_okiya1"] = StoryEvent(label = "c2_homura_okiya1", chapter=2, room="okiya", chance=0.3)

        story_add_event("c2_suzume_arena")

    return


label toggle_secrets:

    $ thieves_guild.secret = not thieves_guild.secret

    return


label toggle_actions:

    $ thieves_guild.action = not thieves_guild.action
    $ watchtower.action = not watchtower.action

    return


label test_get_girls():

    python:
        game.func_time_log = ""
        for i in xrange(30):
            get_girls(100)

    call screen OK_screen(message=game.func_time_log)

    # call screen OK_screen(message=game.func_time_log2)

    return

## Below is a failed attempt at auto-testing perks. Code remains here for possible resurrection attempts


label test_perks:

    python:

        choice_dict = defaultdict(bool)

        result = None

        while result != "commit":

            menu_list = []

            l = sorted(perk_dict.values(), key=lambda x: x.archetype)

            for perk in l:
                menu_list.append((perk.archetype + " - " + perk.name + "(" + str(choice_dict[perk]) + ")", perk))

            menu_list.append(("提交", "commit"))

            result = long_menu("Choose perks to test", menu_list)

#            renpy.say("", "Choice is " + str(result))

            if isinstance(result, Perk):
                choice_dict[result] = not choice_dict[result]

    $ choice_list = [p for p, v in choice_dict.items() if v]
    $ girl_nb = 3
    $ duration = 12
    $ jobs = "cycle all"
    $ show_ev = False

label test_perks_menu:

    $ perk_text = and_text([p.name for p in choice_list])

    menu:
        "Testing perks: [perk_text]"

        "Girls: [girl_nb]":
            $ girl_nb = int(renpy.input("Girl nb", default=girl_nb))

        "Duration: [duration] months":
            $ duration = int(renpy.input("Duration", default=duration))

        "Job: [jobs]":
            $ jobs = menu([("Whore", "whore"), ("Waitress", "waitress"), ("Dancer", "dancer"), ("Masseuse", "masseuse"), ("Geisha", "geisha"), ("Cycle jobs", "cycle jobs"), ("Cycle all", "cycle all")])

        "Show events: [show_ev]":
            $ show_ev = not show_ev

        "GO":
            jump test_perks_launch

    jump test_perks_menu

label test_perks_launch:

    "Generating girls...{nw}"

    python:

        # Get test girls

        girls = get_girls(girl_nb)

        # Get control group

        girls2 = copy.deepcopy(girls)

        # Add perks

        for girl in girls:
            for perk in choice_list:
                girl.acquire_perk(perk, forced=True)

#        for g in girls:
#            renpy.say("", "Generated " + g.fullname + " with perks " + and_text([p.name for p in g.perks]))


    "Running tests...{nw}"

    python:

        month = 0
        day = 0
        test_job_list = all_jobs
        test_all_list = all_jobs + ["whore"]
        girl_stats = {}

#        MC.girls += girls

        for girl in (girls + girls2):
            if jobs in test_all_list:
                girl.set_job(jobs)
            elif jobs == "cycle jobs" or jobs == "cycle all":
                girl.set_job("waitress")

            girl_stats[girl] = {}

    while duration > month:
        $ month += 1
        $ event_list = []
        "Simulating month [month] out of [duration]...{nw}"

        python:
            for x in xrange(28):
                day += 1
                log = Log(day)

                logs.append(log)
                log.threat = 0

                brothel.update_effects()

                for girl in (girls + girls2):

                    girl_stats[girl][day] = defaultdict(int)

                    girl_stats[girl][day]["stat_total"] = sum(stat.value for stat in (girl.stats + girl.sex_stats))
                    girl_stats[girl][day]["level"] = girl.level
                    girl_stats[girl][day]["rank"] = girl.rank
                    girl_stats[girl][day]["rep"] = girl.rep


                    if girl.works_today():

                        if jobs == "cycle jobs":
                            girl.job = cycle_list(test_job_list, girl.job)
                        elif jobs == "cycle all":
                            girl.job = cycle_list(test_all_list, girl.job)

                        girl_stats[girl][day][girl.job] += 1

                        cust_list = []

                        for x in xrange(girl.get_max_cust_served()):
                            if girl.rank == 1:
                                c = Customer(district_dict["slum"])
                            elif girl.rank == 2:
                                c = Customer(district_dict["docks"])
                            elif girl.rank == 3:
                                c = Customer(district_dict["gardens"])
                            elif girl.rank == 4:
                                c = Customer(district_dict["hold"])
                            else:
                                c = Customer(endless_district)
                            cust_list.append(c)
                            log.add_report(c.name + "来到了青楼。他希望得到" + c.wants_entertainment + "的服务，并喜欢" + c.wants_sex_act + "。")

                        if girl.job in all_jobs:
                            event_list += perform(girl.job, (girl,), cust_list)

                        else: # Whr
                            for cust in cust_list:
                                if girl.job == "whore":
                                    act = rand_choice(all_sex_acts)
                                    event_list += perform(act, (girl, ), (cust,))
                                    girl_stats[girl][day][act] += 1

                        girl_stats[girl][day]["income"] = log.gold_made * min(2, brothel.get_effect("boost", "income"))
                        girl_stats[girl][day]["upkeep"] = girl.upkeep

                        log.gold_made = 0

                    else:
                        girl_stats[girl][day]["rest"] += 1

                        girl.rest()

                    girl.reset_interactions()

                    if girl.ready_to_rank(ignore_district=True):
                        girl.rank_up(forced=True)

                    if girl.ready_to_level():
                        girl.auto_level_up()

                    if girl.ready_to_job_up(girl.job):
                        girl.job_up(girl.job)

        if show_ev:
            while event_list:
                $ ev = event_list.pop(0)

                call show_night_event(ev) from _call_show_night_event_2

    "Yielding test results...{nw}"

    $ dur = duration*28
    $ days = [dur//10, dur//4, dur//2, dur//1.25, dur]

#    python:
#        for girl in girls:
#            MC.girls.remove(girl)

    call screen perk_test_results(days, girls, girls2, girl_stats)

    "Ending test..."

    jump main


screen perk_test_results(days, girls, girls2, girl_stats):


    frame:
        xsize 0.9
        ysize 0.9
        xalign 0.5
        yalign 0.5
        background c_black

        has vbox

        text "Test results - " + perk_text

        viewport:

            mousewheel True
            draggable True
            scrollbars "vertical"

            has vbox

            $ x = 1 + len(days)
            $ y = 17 + len(girls)*10

            grid x y spacing 3:

                text ""

                for d in days:
                    text str(int(d))

                text "Gold made-Test" size res_font(14) yalign 0.5

                for d in days:
                    text str(int(get_test_total(girls, d, "income")-get_test_total(girls, d, "upkeep"))) size res_font(14) yalign 0.5

                for g in girls:
                    text g.name size res_font(12) yalign 0.5
                    for d in days:
                        text str(int(get_test_total(g, d, "income")-get_test_total(g, d, "upkeep"))) size res_font(12) yalign 0.5

                text "Gold made-Ctrl" size res_font(14) yalign 0.5

                for d in days:
                    text str(int(get_test_total(girls2, d, "income")-get_test_total(girls2, d, "upkeep"))) size res_font(12) yalign 0.5

                for g in girls2:
                    text g.name size res_font(12) yalign 0.5
                    for d in days:
                        text str(int(get_test_total(g, d, "income")-get_test_total(g, d, "upkeep"))) size res_font(12) yalign 0.5

                text "Gold adv." size res_font(14) yalign 0.5 color c_green

                for d in days:
                    text str(int(get_test_advantage(girls, girls2, d, "income"))) + "%" size res_font(14) yalign 0.5

                text ""
                for d in days:
                    text ""

                text "Stats-Test" size res_font(14) yalign 0.5
                for d in days:
                    text str(int(get_test_total(girls, d, "stat_total"))) size res_font(14) yalign 0.5

                for g in girls:
                    text g.name size res_font(12) yalign 0.5
                    for d in days:
                        text str(int(girl_stats[g][d]["stat_total"])) size res_font(12) yalign 0.5

                text "Stats-Ctrl" size res_font(14) yalign 0.5
                for d in days:
                    text str(int(get_test_total(girls2, d, "stat_total"))) size res_font(14) yalign 0.5

                for g in girls2:
                    text g.name size res_font(12) yalign 0.5
                    for d in days:
                        text str(int(girl_stats[g][d]["stat_total"])) size res_font(12) yalign 0.5

                text "Stat adv." size res_font(14) yalign 0.5 color c_green
                for d in days:
                    text str(int(get_test_advantage(girls, girls2, d, "stat_total"))) + "%" size res_font(14) yalign 0.5

                text ""
                for d in days:
                    text ""

                text "Level-Test" size res_font(14) yalign 0.5
                for d in days:
                    text str(int(get_test_average(girls, d, "level"))) size res_font(14) yalign 0.5

                for g in girls:
                    text g.name size res_font(12) yalign 0.5
                    for d in days:
                        text str(int(girl_stats[g][d]["level"])) size res_font(12) yalign 0.5

                text "Level-Ctrl" size res_font(14) yalign 0.5
                for d in days:
                    text str(int(get_test_average(girls2, d, "level"))) size res_font(14) yalign 0.5

                for g in girls2:
                    text g.name size res_font(12) yalign 0.5
                    for d in days:
                        text str(int(girl_stats[g][d]["level"])) size res_font(12) yalign 0.5

                text ""
                for d in days:
                    text ""

                text "Rank-Test" size res_font(14) yalign 0.5
                for d in days:
                    text str(round(get_test_average(girls, d, "rank"),2)) size res_font(14) yalign 0.5

                for g in girls:
                    text g.name size res_font(12) yalign 0.5
                    for d in days:
                        text str(int(girl_stats[g][d]["rank"])) size res_font(12) yalign 0.5

                text "Rank-Ctrl" size res_font(14) yalign 0.5
                for d in days:
                    text str(round(get_test_average(girls2, d, "rank"),2)) size res_font(14) yalign 0.5

                for g in girls2:
                    text g.name size res_font(12) yalign 0.5
                    for d in days:
                        text str(int(girl_stats[g][d]["rank"])) size res_font(12) yalign 0.5

                text ""
                for d in days:
                    text ""

                text "Rep-Test" size res_font(14) yalign 0.5
                for d in days:
                    text str(int(get_test_average(girls, d, "rep"))) size res_font(14) yalign 0.5

                for g in girls:
                    text g.name size res_font(12) yalign 0.5
                    for d in days:
                        text str(int(girl_stats[g][d]["rep"])) size res_font(12) yalign 0.5

                text "Rep-Ctrl" size res_font(14) yalign 0.5
                for d in days:
                    text str(int(get_test_average(girls2, d, "rep"))) size res_font(14) yalign 0.5

                for g in girls2:
                    text g.name size res_font(12) yalign 0.5
                    for d in days:
                        text str(int(girl_stats[g][d]["rep"])) size res_font(12) yalign 0.5

            text ""

        hbox:
            textbutton "RESTART" action (Return(), Jump("test_perks_launch"))
            textbutton "NEW TEST" action (Return(), Jump("test_perks"))
            textbutton "STOP" action Return()


init python:

    def get_test_total(g, day, stat):
        g = make_list(g, obj_type = Girl)

        total = 0

        for girl in g:
            for i in xrange(int(day)):
                total += girl_stats[girl][i+1][stat]

        return total

    def get_test_average(g, day, stat):
        return sum(girl_stats[girl][day][stat] for girl in g) / len(g)

    def get_test_advantage(g, g2, day, stat):
        return 100 * get_test_total(g, day, stat)/get_test_total(g2, day, stat) - 100

#### END OF BK HELP ####
