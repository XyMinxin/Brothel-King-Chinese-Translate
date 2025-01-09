### RANDOM CITY ENCOUNTERS ###

label city_rape:

    $ norollback()

    $ loc = selected_location.name.lower()

    "Making your way through the [loc], you suddenly hear something."

    stop music fadeout 2.0

    hide screen visit_location

    hide screen overlay

    $ r = rand_choice(encounter_pics["rape"])
    $ pic = Picture(r, "NPC/encounters/" + r)

    scene black with dissolve

    play sound s_scream

    "Listening intently, you hear muffled screams coming from a dark corner. You rush towards the source..."

    if not is_censored("monster") or is_censored("beast"):
        $ renpy.show_screen("show_event", pic, _layer="master")

        with dissolve

    play sound s_screams

    ev_girl1 "Mmmmph! Aaaah!"

    "A poor girl is being raped mercilessly by a disgusting monster."

    ev_girl1 "Aaah, aah, noooo... It's ravaging me! Help! Help me!!!"

    "It seems the evil beast wants to impregnate this poor lass with his cursed semen."

    # Challenge
    $ tt = show_tt("top_right")
    $ chal = renpy.call_screen("challenge_menu", challenges=[("Fight it", "fight", selected_district.rank), ("Banish it", "control", selected_district.rank)], cancel=("Run away", False))

    if chal == "fight":
        $ norollback()

        "You ready your weapon."

        you "Back away, you filthy beast!"

        play sound s_roar

        "The monster turns to face you and roars threateningly."

        call challenge(chal, selected_district.rank) from _call_challenge_8 # result is stored in the _return variable
        $ r = _return

        if r and dice(6) >= 5 and farm.active:

            play sound s_sheath
            with vpunch

            "Charging at the monster with your sword drawn, you slice off a couple of tentacles that try to stop you."

            play sound s_sheath

            with vpunch

            pause 0.3

            play sound s_sheath

            with vpunch

            pause 0.2

            play sound2 s_roar

            "The monster roars in pain, rearing its ugly head towards you. You meet it with all your strength and a metal-clad gauntlet."

            play sound s_punch
            with vpunch

            pause 0.2

            play sound2 s_roar

            "You punch the monster square in what you think is his stupid face, although you're not quite sure."

            play sound s_crash
            with vpunch

            "The monster is stunned and falls flat on the ground in a cloud of dust. The girl screams."

            play sound s_scream

            you "Don't worry, I've got this under control."

            ev_girl1 "Thanks, you saved me... *sob* I will tell everyone what you did for me..."

            you "You be on your way. Don't stay here."

            you "Now, this knocked out monster... What should I do with it?"

            $ atk_type = "combat"

            call city_monster_menu() from _call_city_monster_menu


        elif r:

            play sound s_sheath

            with vpunch

            "Moving with lighting speed, you aim for weak spots on the creature's bloated body."

            play sound s_sheath

            with vpunch

            pause 0.5

            play sound s_sheath

            with vpunch

            "In a matter of seconds, the monster falls into the dirt, lifeless."

            ev_girl1 "Thank, you saved me... *sob* I will tell everyone what you did for me..."

            hide screen show_event

            with dissolve

            "You have earned prestige."

            $ MC.prestige += selected_district.rank * brothel.get_effect("boost", "city rewards")

        else:

            play sound s_clash

            with hpunch

            "The beast braces for your attack and parries your blow."

#                play sound s_roar

#                with vpunch

#                pause 0.5

            play sound s_punch

            with hpunch

            "The beast hits you to the side, bruising your ribs through your armor and sending you crashing into a wall."

            play sound s_scream_loud

            "Before you can get back to your feet, the beast grabs its unfortunate victim and runs off into the night."

            hide screen show_event

            with dissolve

            you "Damn you..."

            "You are wounded and lose your remaining actions for the day."

            $ MC.interactions = 0

    elif chal == "control":

        $ norollback()

        "You lift your staff high in the air."

        if MC.get_alignment() == "evil":

            you "Banish spell? Do I look like I have time for this nonsense?"

            you "Fry, you piece of shit!"

        else:
            if dice(6) == 6:
                you "Thou shall not pass...{w=1.0} your genes!"

            else:
                you "Back to the underworld with you, foul demon!"

        play sound s_roar

        "The monster hears you as you start your incantation, and turns to face you."

        call challenge(chal, selected_district.rank) from _call_challenge_9 # result is stored in the _return variable
        $ r = _return

        if r and farm.active and dice(6) >= 5:

            if MC.get_alignment() == "evil":

                play sound s_lightning

                with vpunch

                "The monster is hit squarely by a powerful bolt of lightning, sending it crashing into the alley's wall."

                play sound s_roar

                you "So, you're still alive?"

                "The monster curls up and whines as you approach menacingly, staff in hand. It is defeated."

            else:

                play sound s_spell

                you "Shazam!"

                play sound s_roar

                with hpunch

                "The monster freezes in its track, and just stands there hazily looking at you."

                ev_girl1 "Wh... What happenned?"

                you "I cast a hypnotic spell... Don't worry, child, it is unable to harm you now."

            ev_girl1 "Oh, you saved me... *sob* I will tell everyone what you did for me... *sob*"

            you "It is best for you to leave now, while I dispose of this creature."

            $ atk_type = "spell"

            call city_monster_menu() from _call_city_monster_menu_1

        elif r:

            if MC.get_alignment() == "evil":

                play sound s_lightning

                with vpunch

                "A great ball of lightning falls from the sky, frying the monster where he stands."

                play sound s_scream_loud

                "The girl screams in terror as her hair curls and stands out on end. Luckily, she is unharmed."

                you "What a dumb bitch... <sigh>"


            else:

                play sound s_spell

                you "Shazam!"

                play sound s_roar

                with hpunch

                "The beast whines and roars in vain as the fabric of space and time distorts and it is pulled back to its original dimension. Within a few seconds, it vanishes into thin air."


            ev_girl1 "Oh, you saved me... *sob* I will tell everyone what you did for me... *sob*"

            hide screen show_event

            with dissolve

            "You have earned prestige."

            $ MC.prestige += selected_district.rank * brothel.get_effect("boost", "city rewards")

        else:

            you "Now take that, you..."

            play sound s_roar

            with vpunch

            you "Uh oh..."

            play sound s_punch

            "The creature rushes towards you and viciously slams you off your feet. Your staff lands several feet away from you."

            play sound s_scream_loud

            "As you try frantically to reach for your staff, the beast seizes its victim and disappears into the night, uninterested in a fight."

            hide screen show_event

            with dissolve

            "You are wounded and lose your remaining actions for the day."

            $ MC.interactions = 0

    else:

        $ norollback()

        "The beast has now noticed you, and glares at you with murderous eyes..."

        you "Well, discretion is the better part of valor..."

        play sound s_screams

        "You hightail it while you still can, ignoring the screams of the poor girl you leave behind."

        hide screen show_event

        with dissolve

        play sound s_roar

        "As the beast roars, you almost feel as if it is mocking you."

        $ MC.good -= 1


    return

label city_monster_menu():

    $ mn = Minion("monster")

    menu:
        you "Now, this knocked out monster... What should I do with it?"

        "Keep it at the farm":

            you "How would you like to get room and board, pal, and fuck some girls all day?"

            $ r, msg = farm.add_minion(mn)

            if msg:
                "[msg]"

            if not r:
                jump city_monster_menu

            $ MC.interactions = 0
            play sound s_spell

            hide screen show_event
            scene black
            with dissolve

            "After sending the girl off, you drag the submissive monster to the farm. This consumes all your remaining actions."

        "Sell it to Willow" if sewers.action:
            you "I know someone who can take care of it, making me some money in the process..."

            hide screen show_event
            scene black
            with dissolve

            $ price = round_int(mn.get_price("sell") * brothel.get_effect("boost", "city rewards"))
            $ MC.gold += price
            $ NPC_willow.items.append(mn)

            "You sell [mn.name] the monster to Willow for [price] gold."

            willow "Thanks!"

            $ NPC_willow.love += 1

            # Selling a monster to Willow triggers her series of events
            $ story_add_event("willow fight", type="city", duplicates=False)


        "Finish it off":
            $ MC.good -= 1

            you "Your days of happily roaming around and randomly banging innocent girls are over, monster. Prepare to die."

            if atk_type == "combat":
                play sound s_sheath
            elif atk_type == "spell":
                play sound s_fire

            pause 0.3
            play sound2 s_roar
            pause 0.1
            play sound3 s_crash

            hide screen show_event
            scene black
            with dissolve

        "Spare it":
            $ MC.good += 1

            "You can't bring yourself to kill off a wounded opponent."

            you "Go, fly, little monster. But don't you dare ever attack an innocent girl again."

            play sound s_roar

            hide screen show_event
            scene black
            with dissolve

            "You're not sure if the monster understood you, but it retreats into the night swiftly to nurse its wounds."

    "You have earned prestige."

    $ MC.prestige += selected_district.rank * brothel.get_effect("boost", "city rewards")

    return


label city_impress:

    $ norollback()

    $ loc = selected_location.name.lower()

    "Walking through the [loc], you run into a party of women adventurers."

    hide screen visit_location

    hide screen overlay

#    stop music fadeout 2.0

    $ pic = Picture(encounter_pics["impress"], "NPC/encounters/" + encounter_pics["impress"])

    scene black with dissolve

    $ renpy.show_screen("show_event", pic, _layer="master")

    with dissolve

    play sound s_girls_laugh

    ev_girl1 "Aw... After so long scouting muddy swamps and dirty dungeons, it's good to be back ..."

    play sound s_sigh

    ev_girl2 "But look at those dumb peasants... I wish we could find a real man..."

    ev_girl3 "Patience, sister... Hey look, someone is coming."

    play sound s_surprise

    ev_girl2 "Hey, you! Are you man enough to party with us?"

    # Pick challenge
    $ tt = show_tt("top_right")
    $ chal = renpy.call_screen("challenge_menu", challenges=[("Show off", "stamina", 4), ("Flirt with the girls", "charm", 4)], cancel=("Ignore them", False))
    hide screen tool

    if chal == "stamina":

        $ norollback()

        you "Of course I am! Watch and enjoy the show, ladies!"


        # Run challenge
        call challenge(chal, 4, score=True) from _call_challenge_10 # result is stored in the _return variable
        $ r = _return

        if r < 0:

                play sound s_equip_dress

                "You take off your shirt and start doing a few push ups and abs flexes. You decide to impress them with a backflip."

                play sound s_dodge

                pause 0.5

                with vpunch

                play sound s_punch

                pause 0.3

                play sound2 s_wscream

                you "Ooooh... My back... <holding back tears>"

                play sound s_evil_laugh

                ev_girl2 "Well, that was an unexpected move! I suppose it deserves an artistic note... I bet Katya could show you how it's done..."

                ev_girl3 "I don't like to waste my time on losers."

                ev_girl4 "None of us does... This is embarrassing. Let's move on, sisters!"

                $ result = -1


        elif r <= 2:

                play sound s_equip_dress

                "Taking off your shirt, you perform a series of moves and flips, showing off your toned body and muscles."

                play sound s_girls_laugh

                ev_girl3 "So, what do you think?"

                ev_girl2 "I don't know... He's good, but I think I could take him in a fight."

                ev_girl1 "I like him. I can't wait anymore sisters... You! Come here."

                you "Yes?"

                ev_girl1 "I have waited for this moment... You, strong guy! Let's fuck!"

                $ result = 1


        elif r <= 4:

                play sound s_equip_dress

                "Ripping off your shirt, you easily lift one of the girls on your shoulder."

                play sound s_surprise

                ev_girl1 "Wow! He's strong!"

                ev_girl3 "And he's got a nice body..."

                you "I could easily carry the both of you, you know."

                ev_girl4 "You could take care of two of us?"

                ev_girl3 "Let's see about that..."

                $ result = 2

        elif r <= 6:

                play sound s_equip_dress

                "Stripping to your underwear, you demonstrate a series of spectacular martial arts moves."

                play sound s_mmmh

                "The girls watch you with rapture, their eyes glistening with lust."

                ev_girl2 "I want to fuck that one so bad..."

                ev_girl3 "Oh, me too!"

                ev_girl4 "Hey, what about me?"

                $ result = 3

        else:

                "You simply strip to your underwear, and show the girls your perfect muscular body. Their jaws drop in awe."

                play sound s_mmmh

                ev_girl3 "Girls, are we in heaven?"

                ev_girl2 "Look at those pecs..."

                ev_girl4 "And looks like he's got a big... too..."

                ev_girl1 "Oh, I want him!"

                ev_girl2 "I want him too!"

                ev_girl4 "Sisters! Calm down... Look how much man there is, we can all share!"

                ev_girl3 "Oh, what a wonderful idea!"

                $ result = 4


    elif chal == "charm":

        $ norollback()

        you "Well, hello, ladies! I'm always one to party..."

        "You start chatting up the girls."

        # Run challenge
        call challenge(chal, 4, score=True) from _call_challenge_11 # result is stored in the _return variable
        $ r = _return

        if r < 0:

                you "So, erm... The weather is quite fine today, don't you think? Even though, yesterday..."

                ev_girl3 "Aw... This man is a bore, don't you think?"

                play sound s_evil_laugh

                ev_girl2 "Totally! Get out of here, maggot! We have better things to do than waste our time with you."

                ev_girl4 "She's a little harsh, friend, but she's right. We do have to move on... Sorry!"

                $ result = -1

        elif r <= 2:

                you "...and then I said: 'I had the cactus in my pants all along!'"

                play sound s_girls_laugh

                ev_girl4 "Good one!"

                ev_girl1 "Can you tell us one more?"

                ev_girl2 "Aw, enough jokes, girls! I have an itch that funny guy here could scratch..."

                ev_girl3 "Ooh, lucky him! *wink*"

                $ result = 1

        elif r <= 4:

                you "Wow, you girls are all so pretty I can't decide which one I'd rather bring home..."

                play sound s_girls_laugh

                ev_girl1 "Oh, you're such a tease!"

                ev_girl2 "If you can't choose one, why don't you take two of us?"

                ev_girl3 "Sounds like a plan..."

                $ result = 2

        elif r <= 6:

                you "...and that's how I brought peace to the kingdom, and ended up in the princess's bed..."

                play sound s_girls_laugh

                ev_girl4 "She's a lucky one... I'd like you in my bed as well!"

                ev_girl3 "So would I!"

                ev_girl2 "Hey, what about me?"

                ev_girl3 "I go first!"

                play sound s_surprise

                ev_girl2 "No, I do!!!"

                $ result = 3

        else:

                you "...that's how I ended up with the three ninja sisters. It was a fun night!"

                play sound s_mmmh

                ev_girl1 "Ah, you're so cool... Talking about sex with you is making me all wet..."

                ev_girl2 "Me too... I want some!"

                play sound s_sigh

                ev_girl4 "Three sisters? You're a horny devil... Think you could take on the four of us?"

                ev_girl3 "Yes! Fuck the four of us! I bet we could show the ninja sisters a thing or two..."

                $ result = 4

    else:

        $ norollback()

        you "Sorry ladies, I have a schedule to keep."

        ev_girl2 "Hey! Who do you think you are!"

        ev_girl3 "Calm down, sister... Plenty of fish in the sea. Let's look elsewhere."

        $ result = 0

    $ spent_AP = 0

    if result == -1:

        hide screen show_event

        with dissolve

        "That could have gone better."

    elif result == 0:

        hide screen show_event

        with dissolve

    elif result == 1:

        $ p = rand_choice(encounter_pics["impress1"])

        $ pic = Picture(p, "NPC/encounters/" + p)

        $ renpy.show_screen("show_event", pic, _layer="master")

        with dissolve

        play sound s_aah

        "Before you have a chance to express agreement or disagreement, the woman shoves her clothing to the side and proceeds to milk you for all you're worth, right here in the [loc]."

        play sound s_orgasm_fast

        ev_girl1 "Oh, yes!!! Cum! Give me more cum! The smell of cock is driving me crazy..."

        ev_girl2 "That's our girl..."

        ev_girl4 "She's such a cum hungry whore, isn't she?"

        ev_girl3 "Way to go, sister..."

        hide screen show_event

        with dissolve

        "You have earned prestige."

        $ unlock_achievement("h impress", level_cap=1)

    elif result == 2:

        $ p = rand_choice(encounter_pics["impress2"])

        $ pic = Picture(p, "NPC/encounters/" + p)

        $ renpy.show_screen("show_event", pic, _layer="master")

        with dissolve

        play sound s_aah

        play sound s_mmmh

        "Before you know it, a couple of girls are running their hands and mouths all over your body."

        play sound s_sucking

        "They play with and each other and hungrily wait for you to cum all over them."

        ev_girl1 "I love it!"

        ev_girl3 "Oh, it's sooo good... Aaaaah!!!"

        play sound s_orgasm

        hide screen show_event

        with dissolve

        "You have earned prestige."

        $ unlock_achievement("h impress", level_cap=2)

    elif result == 3:

        $ p = rand_choice(encounter_pics["impress3"])

        $ pic = Picture(p, "NPC/encounters/" + p)

        $ renpy.show_screen("show_event", pic, _layer="master")

        with dissolve

        play sound s_girls_laugh

        "Three of the girls surround you and hungrily grab your manhood."

        ev_girl4 "Master, allow us to suck your dick dry..."

        play sound s_sucking

        ev_girl3 "Please, spare some cum for me! I love it..."

        ev_girl2 "You have to give us all a good fucking..."

        play sound s_orgasm

        pause 0.5

        play sound2 s_orgasm_fast

        "Today is a good day..."

        hide screen show_event

        with dissolve

        "You have earned prestige."

        $ unlock_achievement("h impress", level_cap=3)

    elif result == 4:

        $ p = encounter_pics["impress4"]

        $ pic = Picture(p, "NPC/encounters/" + p)

        $ renpy.show_screen("show_event", pic, _layer="master")

        with dissolve

        play sound s_girls_laugh

        "All the girls bend to your will, letting you fuck them all for hours on end."

        play sound s_aah

        ev_girl2 "Oh, master, it's sooo big... Fuck me harder! Ruin my pussy!"

        play sound s_surprise

        ev_girl1 "No, it's my turn! I want your cum!"

        play sound s_sigh

        ev_girl4 "Master, I feel empty inside... Why don't you stick it in my ass?"

        play sound s_aaha

        ev_girl3 "Oh, please, let me drink your milk..."

        play sound s_orgasm

        pause 0.5

        play sound2 s_orgasm_fast

        pause 0.5

        play sound3 s_orgasm

        "You have a hard time leaving..."

        hide screen show_event

        with dissolve

        "You have earned a lot of prestige. You are exhausted and can no longer act today."

        $ spent_AP = MC.interactions
        $ MC.interactions = 0
        $ unlock_achievement("h impress")

    if result > 0:
        $ MC.change_prestige((result+spent_AP) * selected_district.rank * brothel.get_effect("boost", "city rewards"))
        if spent_AP:
            "You have received a prestige boost from your [spent_AP] spent AP."

    if result > 1 and dice(6) >= 5:
        ev_girl1 "Hey, buddy, thanks for the ride... Here, we found this on our last adventure."

        ev_girl1 "You can have it. This will be a nice souvenir..."

        if game.chapter >= 3 and dice(6) >= 5:
            call receive_item(item_dict["Cimerian artefact"], msg="你得到了一个稀有的%s。", use_article=False) from _call_receive_item_30
        else:
            call receive_item(item_dict["Cimerian scrap"], msg="你得到了一块%s。", use_article=False) from _call_receive_item_31

    return


label city_slave:

    $ norollback()

    $ loc = selected_location.name.lower()

    "Wandering around the [loc], you hear a familiar voice."

    hide screen visit_location

    hide screen overlay

    slavegirl1 "Master [MC.name]! It's good to see you!"

    you "Hey, you're the trainer from the slave market! What are you doing at the [loc]?"

    slavegirl1 "Well, it's about this slave..."

    play sound s_chimes

    $ p = rand_choice(encounter_pics["slave"])

    $ pic = Picture(p, "NPC/encounters/" + p)

    scene black with dissolve

    $ renpy.show_screen("show_event", pic, _layer="master")

    with dissolve

    slavegirl1 "My master wants her broken and trained by tomorrow, but she stubbornly refuses to do her duties."

    play sound s_sigh

    slavegirl1 "I have tried everything and I'm at the end of my wits..."

    play sound s_surprise

    slavegirl1 "But wait, you're an experienced slave trainer! Maybe you could try some of your tricks on her?"

    slavegirl1 "Oh, please, Master, I beg of you!"

    # Pick challenge
    $ tt = show_tt("top_right")
    $ chal = renpy.call_screen("challenge_menu", challenges=[("Talk to her", "rally", 4), ("Hypnotize her", "control", 3)], cancel=("Not my concern", False))
    hide screen tool

    if chal == "rally":

        $ norollback()

        you "Let me see if I can talk some sense into her."

        slavegirl1 "Oh, thank you!"

        "You approach the bound slave. She gives you an indifferent look."

        slave "What do you want?"

        you "Your behavior is not gonna help, you know."


        # Run challenge
        call challenge(chal, 4, score=True) from _call_challenge_12 # result is stored in the _return variable
        $ r = _return

        if r < 0:

                "You give her a long lecture on the duties of a proper slave."

                slave "Go to hell."

                $ result = 0

        elif r <= 2:

                "You gently explain that being a slave is not the end of the world."

                you "You belong to your rightful owner. There is nothing you can do about it. If you accept it, it will be easier for you."

                "She sobs."

                slave "But I don't want to serve the needs of this dirty old man... *sob*"

                you "I'm sorry, but it's not your call."

                slave "..."

                play sound s_sigh

                slave "I understand. The choice is not mine, anyway. I have to find a way to live with this."

                you "This is the right attitude."

                $ result = 1

        elif r <= 6:

                "Sitting down next to her, you tell her about your life as a brothel owner. You tell her all about your girls, their lives, where they came from, and how they cope with their situation now."

                you "At first, everyone is afraid, but with time this work can grow on you. Being a slave doesn't mean giving up on life - it's an entirely new life. With the right mindset, it can be exciting."

                "As she listens to you, a glimmer of hope appears in her eyes."

                play sound s_surprise

                slave "Really? Can a sex slave find happiness?"

                you "Bliss, even. I have girls in my brothel who wouldn't do anything else for all the gold in Xeros."

                slave "I had never heard something like that before..."

                slave "You have given me some hope. I will give it my best."

                you "And I am certain you will do great."

                slave "Thank you, Master [MC.name]."

                $ result = 2

        else:

                "You tell her vivid details about the life of some of the famous sex slaves of Zan, explaining how they leveraged their situation to become legends in their own right."

                you "If you embrace your condition, you can do amazing things. You can be a godly vessel, harnessing the power of lust and vice and turning it into positive energy..."
                you "It is a holy duty."

                "She looks at you, eyes open wide in amazement."

                slave "I never knew that being a sex slave could lead to such fulfilling lives!"

                you "You can not only fulfill your life, but that of others. Using your body to serve others is the holiest sacrifice there is."

                you "And you can enjoy it, too."

                slave "I can see how wrong I was now! When can I start? I want to do it!"

                $ result = 3

    elif chal == "control":

        $ norollback()

        you "I could try an obedience spell."

        slavegirl1 "A spell? Oooh, this is exciting!"

        "You approach the bound girl, and swiftly cut a lock of her hair with your knife."

        play sound s_scream

        slave "Watch it! You psycho!"

        "Holding the lock of hair firmly in your palm, you start incanting."

        # Run challenge
        call challenge(chal, 3, score=True) from _call_challenge_13 # result is stored in the _return variable
        $ r = _return

        if r < 0:

                you "You will now do as I command! Obey your master!"

                slave "I command you to fuck off!"

                you "Damn, she's strong-willed..."

                "She resists your attempt."

                $ result = 0

        elif r <= 2:

                you "Follow my bidding now, child."

                play sound s_spell

                you "Resistance is futile..."

                slave "..."

                slave "Resistance..."

                slave "...is futile..."

                "She looks lost. Trying to elicit a reaction, you pinch her breast."

                play sound s_surprise

                "She shivers, but she doesn't fight you."

                you "I think it worked."

                $ result = 1

        elif r <= 6:

                you "Hear my voice. I am the voice of your master."

                play sound s_spell

                slave "You... You are the voice of my master..."

                you "Your master commands you to obey. You must do whatever is asked of you, whenever and wherever you are."

                slave "I must do whatever is asked of me, whenever and wherever I am."

                you "You will never forget my command."

                slave "I will never forget your command."

                you "Now, you may rest."

                "The girl looks up to you with bewildered eyes. It's like she notices you for the first time."

                slave "Master, what can I do for you? I will do whatever you ask. *smile*"

                $ result = 2

        else:

                you "I summon thee, succubus. Lend your powers of arousal and lust to that wretched slave."

                play sound s_spell

                "The hair in your palm whitens and the smell of sulfur floats in the air."

                slave "What... What is going on?"

                "A dark halo surrounds the girl and seems to penetrate beneath her skin. She shivers uncontrollably."

                play sound s_aah

                slave "Oooh... What's happening to me..."

                "Her chains jingle as her tits seem to grow larger. Her nipples stand firmly erect, and juice starts running along her thighs."

                slave "I'm so horny!!! AAAAAH!"

                play sound s_orgasm

                "She trembles as a strong orgasm washes over her."

                slave "Someone fuck me! Please, anyone!!!"

                play sound s_aaha

                slave "I'm a dirty whore, I'll do anything... Please... Fuck meeeeeeee!"

                play sound s_orgasm_fast

                $ result = 3

    else:

        $ norollback()

        you "Sorry, but I can't help you."

        slavegirl1 "I see."

        slavegirl1 "Of course. It was a silly request. I apologize, Master."

        hide screen show_event

        with dissolve

        return


    if result == 0:

        hide screen show_event

        with dissolve

        you "I'm sorry, it didn't work."

        "The slave trainer looks down."

        play sound s_sigh

        slavegirl1 "That was a long shot. Thank you for trying."



    elif result == 1:

        slavegirl1 "You did it! I hope she won't change her mind..."

        slavegirl1 "Thank you so much for your help."

        hide screen show_event

        with dissolve

        "You have earned prestige."

        $ MC.prestige += selected_district.rank * brothel.get_effect("boost", "city rewards")

    elif result == 2:

        hide screen show_event

        with dissolve

        slavegirl1 "Amazing! You succeeded where I failed... You are truly something."

        play sound s_sigh

        slavegirl1 "Perhaps you can help me with something else, if you have time..."

        slavegirl1 "One of the girls needs advanced sexual training. Would you care to help me with it?"

        slavegirl1 "She can do anything you ask."

        menu:

            "Let me..."

            "Fuck her mouth":

                $ act = "service"

            "Fuck her pussy":

                $ act = "sex"

            "Fuck her ass":

                $ act = "anal"

            "Do something else":

                $ act = "fetish"

            "I don't have time for this":

                $ norollback()

                slavegirl1 "I see, that's too bad then."

                hide screen show_event

                with dissolve

                "You have earned prestige."

                $ MC.prestige += selected_district.rank * brothel.get_effect("boost", "city rewards")

                return

        $ norollback()

        slavegirl1 "This is a great choice! Let's get to it. *smile*"

        $ pics = rand_choice(encounter_pics["slave_" + act])

        slavegirl1 "There she is! Be a nice girl now, Master [MC.name] is going to take good care of you."

        $ pic = Picture(pics[0], "NPC/encounters/" + pics[0])

        $ renpy.show_screen("show_event", pic, _layer="master")

        with dissolve

        play sound s_surprise

        slave "Oh!!!"

        if act == "service":

            slavegirl1 "Now, be a good girl and suck his dick off, like I showed you last time, ok?"

        elif act == "sex":

            slavegirl1 "Master [MC.name] will now fuck your pussy. Brace yourself, now, he's got a big dick. Mmmh..."

        elif act == "anal":

            slavegirl1 "It's good we performed that enema together this morning, don't you think? Raise your ass a little... There!"

        elif act == "fetish":

            slavegirl1 "Master [MC.name] will show you something new today. Make sure to enjoy it!"

        $ pic = Picture(pics[1], "NPC/encounters/" + pics[1])

        $ renpy.show_screen("show_event", pic, _layer="master")

        with dissolve

        play sound s_scream

        slave "Aaaaaah!!!"

        slavegirl1 "Take some time to get used to the feeling... Ease into it..."

        play sound s_mmmh

        "You come and go for a while. You can tell she is starting to enjoy it."

        slavegirl1 "There, that's better..."

        $ pic = Picture(pics[2], "NPC/encounters/" + pics[2])

        if act == "fetish":

            you "Let's not forget your other hole!"

            play sound s_screams

            $ renpy.show_screen("show_event", pic, _layer="master")

            with dissolve

        "You increase your pace."

        play sound s_moans_short

        you "Oh, you're good..."

        slavegirl1 "Looks like you managed to turn Master [MC.name] on... *giggle*"

        if act != "fetish":

            you "I'm close..."

            play sound s_orgasm_fast

            slave "Ohhhh, aaaahhh... AAAAAH!"

            with doubleflash

            $ renpy.show_screen("show_event", pic, _layer="master")

            with dissolve


            you "HAAAAAAAAAAAAA!!!"

            with flash

            if act == "service":

                "You shoot your load inside her mouth, and she gulps it down with a hiccup."

                "Pulling out, you spread white cum all over her face."

            else:

                "You cum buckets inside her, and her body shakes in a massive orgasm."

                "Pulling out, you shoot your last load over her body."

        else:

            "She seems lost in the feeling of her two holes being raped."

            you "You like it, don't you, slave? What if I push deeper!"

            play sound s_screams

            slave "AAAAH! UHHH!!!"

            slavegirl1 "Look like she's going to cum! This is so fun!"

            play sound s_scream_loud

            with doubleflash

            slave "AAAAAAAAAAAAAAH!!!!"


        $ pic = Picture(pics[2], "NPC/encounters/" + pics[3])

        $ renpy.show_screen("show_event", pic, _layer="master")

        with flash

        "Trembling with pleasure, the girl collapses in a pool of bodily fluids."

        play sound s_orgasm

        you "That was good..."

        hide screen show_event

        with dissolve

        you "Thank you, I enjoyed it."

        slavegirl1 "My pleasure! *smile*"

        you "Maybe I could show the girls a thing or two back at the brothel..."

        $ unlock_achievement("h slavegirl")
        $ act_cn = tl_cn(act, girl_related_dict)
        "You have earned prestige. Some of your girls have increased their [act] stat."

        $ MC.change_prestige(selected_district.rank * brothel.get_effect("boost", "city rewards"))

        python:

            for girl in MC.girls:

                if dice(6) >= 4:

                    girl.change_stat(act, 1 * brothel.get_effect("boost", "city rewards"))




    elif result == 3:

        hide screen show_event

        with dissolve

        slavegirl1 "That was incredible! You truly are a master among slave trainers!"

        play sound s_mmmh

        slavegirl1 "I want to personally reward you... Miki, come over here!"

        play sound s_sucking

        $ pic = Picture(encounter_pics["slave_success"][0], "NPC/encounters/" + encounter_pics["slave_success"][0])

        $ renpy.show_screen("show_event", pic, _layer="master")

        with dissolve

        play sound2 s_aah

        slavegirl2 "Mmmh, aaah..."

        slavegirl1 "This is so big..."

        $ pic = Picture(encounter_pics["slave_success"][1], "NPC/encounters/" + encounter_pics["slave_success"][1])

        $ renpy.show_screen("show_event", pic, _layer="master")

        with dissolve

        slavegirl1 "And such a strong taste... I love it..."

        play sound2 s_mmmh

        slavegirl2 "Mmmmh..."

        slavegirl1 "It's pulsating! It's so warm!"

        play sound2 s_surprise

        $ pic = Picture(encounter_pics["slave_success"][2], "NPC/encounters/" + encounter_pics["slave_success"][2])

        $ renpy.show_screen("show_event", pic, _layer="master")

        with doubleflash

        with vpunch

        play sound s_aaha

        slavegirl1 "Aaaaaaah!!!"

        slavegirl2 "Oooooh!!!"


#        play sound2 s_aah

        $ pic = Picture(encounter_pics["slave_success"][3], "NPC/encounters/" + encounter_pics["slave_success"][3])

        $ renpy.show_screen("show_event", pic, _layer="master")

        with flash

        play sound s_sigh

        slavegirl1 "Master... You came so much!"

        slavegirl2 "It's all over my face..."

        play sound s_mmmh

        slavegirl1 "So delicious... More..."

        "She licks the cum off her lips, giving you a salacious look."

        slavegirl1 "The night has only just started..."

        hide screen show_event

        with dissolve

        $ MC.change_prestige((1+MC.interactions) * selected_district.rank * brothel.get_effect("boost", "city rewards"))

        "You have earned prestige. Some of your girls have increased their sex stats.\nYou have expended all your actions for the day."

        if MC.interactions:
            "You have received a prestige boost from your [MC.interactions] spent AP."

        $ MC.interactions = 0

        $ unlock_achievement("h slavemarket")

        python:

            for girl in MC.girls:

                if dice(6) >= 4:

                    girl.change_stat("service", 1 * brothel.get_effect("boost", "city rewards"))
                    girl.change_stat("sex", 1 * brothel.get_effect("boost", "city rewards"))
                    girl.change_stat("anal", 1 * brothel.get_effect("boost", "city rewards"))
                    girl.change_stat("fetish", 1 * brothel.get_effect("boost", "city rewards"))

    return


label city_gamble:

    $ norollback()

    $ loc = selected_location.name.lower()

    "You are strolling around the [loc], daydreaming, when you hear someone call out to you."

    hide screen visit_location

    hide screen overlay

#    stop music fadeout 2.0

    $ pics = rand_choice(encounter_pics["gamble"])

    $ pic = Picture(pics[0], "NPC/encounters/" + pics[0])

    scene black with dissolve

    $ renpy.show_screen("show_event", pic, _layer="master")

    with dissolve

    play sound s_surprise

    ev_girl1 "Hello, mister! I'm bored... Won't you play with me? We can wage a few denars..."

    "A cute, innocent-looking girl is challenging you to a popular game."

    menu:

        "What will you do?"

        "Accept":

            $ norollback()

            you "A game? Sounds exciting!"

            ev_girl1 "Yay! *smile*"

            with fade

            "You win the first few games, making quite a bit of money."

            ev_girl1 "Haha, you really got me there mister!"

            you "Hey, this is fun!"

            with fade

            "You keep playing, but your luck runs out somehow."

            "Before you know it, your gains have been wiped out, and the girl is sitting in front of a pile of gold."

            ev_girl1 "Well, mister, it looks like lady luck is favoring me now... Teehee..."
            ev_girl1 "But you can catch up!"

            you "Aw..."

            "Suddenly, you realize that sweet, innocent girl is not so innocent after all. She must be an experienced gambler. She's been playing you for a fool from the beginning."

            ev_girl1 "Let's play another one!"

            # Pick challenge
            $ tt = show_tt("top_right")
            $ chal = renpy.call_screen("challenge_menu", challenges=[("Call her out", "bluff", selected_district.rank + 2), ("Cheat", "cast", selected_district.rank+3)], cancel=("Cut your losses", False))
            hide screen tool

            if chal == "bluff":

                # Run challenge
                call challenge(chal, selected_district.rank + 2) from _call_challenge_14 # result is stored in the _return variable
                $ r = _return

                $ norollback()

                if r:

                    you "All right, let's do this."

                    with fade

                    "Concentrating on her facial expressions and body language, you begin to understand her winning strategy."

                    "Putting this to your advantage, you manage to regain the edge and make up for your losses."

                    "The girl looks unassured now, and she is losing her composure."

                    play sound s_surprise

                    ev_girl1 "Grrr, you're so lucky all of a sudden! But this time, I'll show you!"

                    "She bets all of her remaining credit on her next move."

                    ev_girl1 "What do you say about that!"

                    you "And... {w=1.0}I win!"

                    play sound s_scream

                    with vpunch

                    ev_girl1 "Nooooooooo!!!"

                else:

                    "You try to focus and observe her play feverishly, looking for a weakness."

                    "But she remains unpredictable. Your losses pile up."

                    you "Oh no..."

                    play sound s_evil_laugh

                    ev_girl1 "Hahaha! *evil laugh*"

            elif chal == "cast":

                # Run challenge
                call challenge(chal, selected_district.rank + 3) from _call_challenge_15 # result is stored in the _return variable
                $ r = _return

                $ norollback()

                if r:

                    you "Ok, but let's take a break."

                    "Beaming with self-content, the girl gets up to buy herself a drink with your hard-earned money."

                    you "This is the right time..."

                    play sound s_spell

                    with hpunch

                    "Muttering a spell, you draw the shape of a pentagram into the air over the game table."

                    "The table glows faintly, the halo receding just in time for her to return to the table."

                    with dissolve

                    ev_girl1 "So, where were we?"

                    you "I was about to kick your sweet ass, I believe!"

                    ev_girl1 "Bring it on! *laugh*"

                    "The next few minutes see you winning round after round. The girl looks increasingly frustrated."

                    play sound s_surprise

                    ev_girl1 "This is uncanny! But your luck will run out, eventually! *frown*"

                    "Your luck doesn't run out, however, and before long she has used up all her credit."

                    ev_girl1 "What the hell! You're cheating, I'm sure! *mad*"

                    you "There, there, don't be a bad sport."

                else:

                    "You wait for her to look away so that you can cast your spell undetected."

                    "While she is busy counting her gold with a satisfied look on her face, your start muttering a few words, raising your hand towards the game."

                    "The words don't come easily, however, and you have a hard time harnessing magical energy while doing your best to look casual."



                    ev_girl1 "What are you doing?"

                    play sound s_fizzle

                    with vpunch



                    you "Oh, uh, ahem... Just stretching, hahahahaha!"

                    ev_girl1 "You're acting weird... Don't try to cheat, now, ok?"

                    you "Of course not, hahahahaha! *sweat*"

                    "You fail to cast your spell. Your luck just goes from bad to worse, and you end up with heavy losses."


            else:

                $ norollback()

                you "It's been a fun game, but it's getting late. I'll play you another time."

                "The girl makes a show of looking disappointed."

                ev_girl1 "Aw, that's too bad, I'm sure you were about to win big... *sneer*"

                hide screen show_event

                with dissolve

                $ loss = (29 + dice(41)) * selected_district.rank

                if loss >= MC.gold:
                    if MC.gold > 0:
                        $ loss = MC.gold
                    else:
                        $ loss = 0

                play sound s_gold

                "You have lost %(loss)d gold."

                $ MC.gold -= loss

                return


            if r:

                with fade

                you "All right honey, time to cough up the gold."

                if dice(6) < 6:

                    "She looks at you with teary eyes."

                    ev_girl1 "Aw... You're robbing me blind..."

                    hide screen show_event

                    with dissolve

                    $ gain = (99 + dice(51)) * selected_district.rank * brothel.get_effect("boost", "city rewards")

                    play sound s_gold

                    "You have earned %(gain)d gold."

                    $ MC.gold += gain

                else:

                    play sound s_surprise

                    "She looks at you with panicked eyes."

                    ev_girl1 "Uh... It's... I..."

                    you "What now?"

                    "She opens her purse. A mite flies out, but otherwise it is completely empty."

                    ev_girl1 "I do not have the gold to repay you, mister."

                    with vpunch

                    you "What?"

                    ev_girl1 "I don't have any money... This gig was supposed to earn me some..."

                    "Tears run along her cheeks."

                    you "I'm sorry. But you have to pay up. Don't make me fetch the guard..."

                    ev_girl1 "The guard? No, please! We can work this out!!!"

                    "She gives you a strange, devious look."

                    ev_girl1 "I can make it up to you in another way..."

                    $ pic = Picture(pics[1], "NPC/encounters/" + pics[1])

                    $ renpy.show_screen("show_event", pic, _layer="master")

                    with fade

                    play sound s_mmmh

                    ev_girl1 "Oh, mister, you're being rough, aaha!!"

                    you "You owe me a great deal, and I intend to collect, ha!"

                    "Pushing your dick inside her firm, slender body, you begin to pump in and out of her with rhythm."

                    play sound s_moans

                    ev_girl1 "Ooooh... I like it... Mister, your cock is huge, oh..."

                    you "This is only the beginning..."

                    "Increasing your pace, you fuck her harder and harder."

                    "Her screams of passion fill the room as her juices drip down from her pussy."

                    play sound s_scream

                    ev_girl1 "You're ravaging me! I love it!"

                    you "Take this, you little slut! Uuuuaaaahhhhh!!!!"

                    ev_girl1 "HAAAAAAAAAAA!!!"

                    play sound s_orgasm_young

                    $ pic = Picture(pics[2], "NPC/encounters/" + pics[2])

                    $ renpy.show_screen("show_event", pic, _layer="master")

                    with doubleflash

                    "She screams in delight as a powerful orgasm rocks her body back and forth."

                    with flash

                    "You come loads inside of her, and she squeezes you dry with her tight hole."

                    ev_girl1 "Cum... So warm inside... Feels so good... Aaaah..."

                    play sound s_mmmh

                    hide screen show_event

                    with dissolve

                    "You have earned prestige."

                    $ MC.change_prestige(selected_district.rank * brothel.get_effect("boost", "city rewards"))
                    $ unlock_achievement("h gambler")

            else:

                ev_girl1 "Time to pay up, now, mister!"

                you "Damn..."

                hide screen show_event

                $ loss = (99 + dice(51)) * selected_district.rank

                if loss >= MC.gold:
                    if MC.gold > 0:
                        $ loss = MC.gold
                    else:
                        $ loss = 0

                play sound s_gold

                "You have lost %(loss)d gold."

                $ MC.gold -= loss



        "Refuse":

            $ norollback()

            you "Sorry, but I'm not one to waste time playing games."

            ev_girl1 "Really? That's too bad, I figured you were the playing type... Goodbye, then."

            hide screen show_event

            with dissolve

    return


label city_thief:

    $ norollback()

    $ loc = selected_location.name.lower()

    "As you pass a group of people near the [loc], you suddenly hear a scream."

    hide screen visit_location

    hide screen overlay

#    stop music fadeout 2.0

    $ p = rand_choice(encounter_pics["thief"])

    $ pic = Picture(p, "NPC/encounters/" + p)

    scene black with dissolve

    $ renpy.show_screen("show_event", pic, _layer="master")

    with dissolve

    play sound s_scream

    with vpunch

    woman "Thief! A thief! Help me!"

    "You see a sneaky cutpurse running down the street, holding the woman's belongings."

    # Pick challenge
    $ tt = show_tt("top_right")
    $ chal = renpy.call_screen("challenge_menu", challenges=[("Run after the thief", "stamina", selected_district.rank + 3), ("Ensnare the thief", "cast", selected_district.rank + 3)], cancel=("Ignore her", False))
    hide screen tool

    if chal == "stamina":

        # Run challenge
        call challenge(chal, selected_district.rank + 3) from _call_challenge_16 # result is stored in the _return variable
        $ r = _return

        if r:

            "You bolt after the thieving scum, quickly catching up thanks to your superior training."

            "Desperate to escape you, the thief starts climbing a building, heading towards the roof."

            you "Damn you!"

            "Grabbing a rock from the ground, you expertly throw it as the wretch reaches for the top."

            play sound s_punch

            pause 0.5

            play sound s_wscream

            with vpunch

            "The thief falls down with a scream, and lays there, passed out. You recover the woman's purse."

        else:

            "You start running after the wicked thief, but the wretch is very fast."

            "You manage to keep up for a while, but you can feel your stamina running out."

            you "Damn..."

            "You finally give up on the chase, completely out of breath."

    elif chal == "cast":

        # Run challenge
        call challenge(chal, selected_district.rank + 3) from _call_challenge_17 # result is stored in the _return variable
        $ r = _return

        if r:

            "Trying to keep the thief within your view, you start chanting the words of a powerful weakening spell."

            play sound s_spell

            with vpunch

            "You can see the thief running desperately down the street, then suddenly falling flat on the pavement, legs shaking uncontrollably."

            "The wretch still tries to flee, creeping forward at an agonizing pace."

            "You leisurely walk up to the thief, whistling a popular bard song."

            "The thief sees you and begs for mercy as you loom close."

            if MC.get_alignment() == "evil":

                "Still whistling, you answer with a powerful blow to the the head. The skull gives in with a nasty crack."

                "You then retrieve the woman's belongings."

            else:

                "You reach down and recover the woman's purse from the ground. You then snap your fingers, and the thug's limbs stop shaking."

                "Swearing, the rascal jumps up and hightails it, as if a demon was giving chase."

        else:

            "You try to keep the thief in focus, but the constant leaping and dodging makes it too hard to aim a spell."

            play sound s_fizzle

            "You curse as the thief finally disappears from your sight, hidden by a passing carriage."

    else:

        $ norollback()

        you "This is none of my concern, really."

        "You watch with indifference as the thief expertly makes way through the crowd and vanishes from your sight."

        $ r = False


    if r:

        woman "Oh thank you, thank you!"

        "She smiles gratefully at you, and hands you a pouch of gold for your trouble."

        if MC.get_alignment() == "good":

            you "Thank you, but this isn't necessary..."

            woman "Please, I insist."

        else:

            you "Nice!"

        hide screen show_event

        with dissolve

        $ gain = (99 + dice(51)) * selected_district.rank * brothel.get_effect("boost", "city rewards")

        play sound s_gold

        "You have earned %(gain)d gold."

        $ MC.gold += gain


    else:

        play sound s_steps

        "The thief disappears into a side street, heading for one of the gates leading to the slums."

        hide screen show_event

        with dissolve

        "You shrug and step back towards the [loc], the sound of the woman's distraught cries echoing in your ears."

    return


label city_wrestle:

    $ norollback()

    $ loc = selected_location.name.lower()

    "You meet a group of sellswords sitting around a few tables, in a dodgy corner of the [loc]."

    hide screen visit_location

    hide screen overlay

#    stop music fadeout 2.0

    $ p = rand_choice(encounter_pics["wrestle"])

    $ pic = Picture(p, "NPC/encounters/" + p)

    scene black with dissolve

    $ renpy.show_screen("show_event", pic, _layer="master")

    with dissolve

    warrior "Hey, you! Think you're strong? What do you say to a bout of arm wrestling?"

    warrior "I wager a fistful of gold I could beat you fair and square right here, right now."

    play sound s_crowd_laugh

    "A crowd of mercenaries and idlers watches you with interest as they await for your response."


    # Pick challenge
    $ tt = show_tt("top_right")
    $ chal = renpy.call_screen("challenge_menu", challenges=[("Face him", "force", selected_district.rank + 3), ("Use your wits", "bluff", selected_district.rank+2)], cancel=("Ignore him", False))
    hide screen tool

    if chal == "force":

        $ norollback()

        you "Let's see about that!"

        "The crowd cheers and jeers as you sit down in front of the seasoned veteran."

        "One of the men fires his gun in the air to give the starting signal."

        play sound s_fire

        with vpunch

        "Your muscles tighten up as you prepare to resist your opponent."

        # Run challenge
        call challenge(chal, selected_district.rank + 3) from _call_challenge_18 # result is stored in the _return variable
        $ r = _return


        if r:

            "For a while, it looks like you are locked down and losing inch by inch to your adversary."

            "However, you are simply waiting for him to exhaust his energy."

            "Sweat is beading off his face as he tries desperately to push through the last few inches."

            "You suddenly fight him off with all your strength, however, and slam his hand down on the table so strongly that the drinks spill."


            play sound s_punch
            with vpunch



            warrior "Aaaargh!!!"

        else:

            "Both of your arms are locked in a tight grip. For a while, it's hard to tell who's winning or losing."

            "However, you can feel your stamina slowly draining out. Your arm starts to shake. Your opponent is grinning now."

            warrior "Feeling a little tired, greenhorn?"

            with vpunch

            play sound s_punch

            "With a final thump, the mercenary pushes your hand down onto the table. You are defeated."

            you "Shit..."

    elif chal == "bluff":

        $ norollback()

        you "Oh, a fight with a monkey. I hear they're strong, if a little intellectually-challenged."

        "The crowd erupts into loud laughter at your jest. The warrior's eyes narrow."

        warrior "Careful now, boy..."

        "Sitting down in front of him and getting ready, you give him a wink."

        # Run challenge
        call challenge(chal, selected_district.rank + 2) from _call_challenge_19 # result is stored in the _return variable
        $ r = _return

        if r:

            "As the contest begins, you keep poking fun at your opponent."

            you "Hey, you've got a chunk of pork on your face. Ah, sorry, that's your nose."

            warrior "Grrr..."

            you "So, ever rubbed your mother's cunt with your ears?"

            warrior "What??? No!!!"

            you "I see, you were born with a helmet then..."

            play sound s_crowd_laugh

            "The mercenaries laugh louder with each of your jokes, and taunt the poor bastard. He seems to be completely losing his concentration."

            "That's when you decide to make your push. Piling up against his arm, you send it flying into the table."

            with vpunch

            play sound s_punch

            you "Touché!"

            warrior "What?? How could I lose!"

        else:

            "Even as you try to get into his head, his superior strength threatens to overwhelm you. Beads of sweat start running into your eyes. This is going poorly."

            you "You know what? I'm... I'm stronger than you! You might as well give up."

            warrior "Oh yeah? I have another idea. How about I break your arm?"

            with vpunch

            play sound s_punch

            "With a thunderous grunt, the warrior slams your arm down on the table. It hurts like hell."

            you "Aaaargh!!!"

            warrior "Hahahahaha!!!"

    else:

        $ norollback()

        you "I can't, I have... stuff to do."

        warrior "I see. Then scram, weakling."

        $ dis = selected_district.name.lower()

        "The mercenaries scoff and jeer, calling you a coward and all sorts of unpleasant names as you pitifully make your way back to [dis]."

        play sound s_crowd_laugh

        hide screen show_event

        with dissolve



        return

    if r:

        play sound s_crowd_laugh

        "The crowd roars and erupts in applause as the warrior gives you a dejected look."

        you "Time to pay up."

        warrior "Fine, here's your gold... *frown*"

        hide screen show_event

        with dissolve

        $ gain = (99 + dice(51)) * selected_district.rank * brothel.get_effect("boost", "city rewards")

        play sound s_gold

        "You have earned %(gain)d gold."

        $ MC.gold += gain

    else:

        warrior "I want my money now, wimp."

        hide screen show_event

        with dissolve

        $ loss = (74 + dice(51)) * selected_district.rank

        if loss >= MC.gold:
            if MC.gold > 0:
                $ loss = MC.gold
            else:
                $ loss = 0

        play sound s_gold

        "You have lost %(loss)d gold."

        $ MC.gold -= loss

    return


label city_cat:

    $ norollback()

    $ loc = selected_location.name.lower()

    "While walking around the [loc], minding your own business, you hear a young woman call you."

    hide screen visit_location

    hide screen overlay

#    stop music fadeout 2.0

    $ p = rand_choice(encounter_pics["cat"])

    $ pic = Picture(p, "NPC/encounters/" + p)

    scene black with dissolve

    $ renpy.show_screen("show_event", pic, _layer="master")

    with dissolve

    play sound s_meow

    ev_girl3 "Nyaa! Mister, help me!"

    you "What is it? ...and what's with the strange ears??"

    play sound s_meow

    ev_girl3 "It's Yuna! My best friend! I can't find her anywhere!"

    ev_girl3 "She's been missing for days! She told me she was going out for a while, but..."

    you "Do you have any idea where she went? Did you talk to any of her other friends?"

    ev_girl3 "Well... She's been fooling around with those cool cats lately..."

    you "Cool cats?"

    ev_girl3 "There's Steve, the handsome dark one... Garfy, the fat, funny one... And the siamese twins..."

    you "Siamese twins?? That's rare... I don't remember ever meeting any of those guys..."

    play sound s_surprise

    ev_girl3 "Oh, mister, what am I gonna do... What if she gets eaten?"

    you "Eaten? Calm down, I don't think anyone will eat your friend..."

    ev_girl3 "But some people like eating cats!!! There's Alf, this dodgy dwarf, he..."

    you "Cats??? Wait a minute... Your friend is a cat?"

    ev_girl3 "Yes, of course! She's my best friend! We have such great conversations, you know, about life, love, nyaa... We share the same world view..."

    you "Okaay... Right..."

    # Pick challenge
    $ tt = show_tt("top_right")
    $ chal = renpy.call_screen("challenge_menu", challenges=[("Look for her cat", "charm", selected_district.rank + 3), ("Track it with a spell", "detect", selected_district.rank+3)], cancel=("Leave her alone", False))
    hide screen tool

    if chal == "charm":

        $ norollback()

        you "Very well, then. I'll help you find her."

        ev_girl3 "Oh, mister, thank you, nyaaa! I think she went this way..."

        hide screen show_event

        with fade

        "You spend an hour searching high and low for the kitty."

        $ p = rand_choice(encounter_pics["cat_found"])
        $ pic2 = Picture(p, "NPC/encounters/" + p)

        $ renpy.show_screen("show_event", pic2, _layer="master")

        with dissolve

        "Finally, you see the cat, lazily curling into a ball on the edge of a rooftop."

        ev_girl3 "Oh, it's her!"

        # Run challenge
        call challenge(chal, selected_district.rank + 3, score=True) from _call_challenge_20 # result is stored in the _return variable
        $ r = _return


        if r < 0:

            you "Hey, Yuna! Come down here you dumb critter!"

            "Your yelling startles the cat, who hisses at you before jumping from the roof into a side street and running off."

            play sound s_meow

            ev_girl3 "Nooo! Come back, Yuna, come baaaaack! Nyaaa!"

            "The strange girl runs after her pet, leaving you standing there with a dumbfounded look on your face."

            hide screen show_event

            with dissolve

            $ result = 0

        elif r <= 2:

            you "Come here, kitty kitty... Yuna, please come here, there's nothing to be afraid of..."

            play sound s_meow

            "The kitty gives you a lascivious look and yawns. She lazily stretches her limbs, then jumps down at your feet with effortless grace."

            ev_girl3 "Yuna!!! You're here! I'm so happy!!!"

            $ result = 1

        else:

            "Doing your best impersonation of a cat's meow, you call out to the cat in her own language."

            play sound s_meow

            you "Meow!!!"

            play sound s_meow

            "Yuna raises her head and looks at you with great curiosity."

            "She leaps down into your ready arms. You give her a pat on the head, and she starts purring. You gently put her on the ground."

            ev_girl3 "Amazing! You are a cat lover too, I can tell! Nyaa!"

            $ result = 2

            if r > 5:

                $ result = 3


    elif chal == "detect":

        $ norollback()

        you "I could locate your 'friend' using a spell. That might work."

        play sound s_meow

        ev_girl3 "Really? That's so cool! Thank you mister, nyaaah!"

        "She looks at you expectantly."

        you "Hum, hum. First, let me gather some personal item of her. A collar, perhaps?"

        ev_girl3 "Haha, mister, that's kinky! We don't do this kind of stuff. But I can find you some of her hair, I guess."

        "Holding the lock of hair firmly, you start chanting."

        # Run challenge
        call challenge(chal, selected_district.rank + 3, score=True) from _call_challenge_21 # result is stored in the _return variable
        $ r = _return

        if r < 0:

            you "Come hereforth, you furry beast! Come to daddy!"

            play sound s_fizzle

            ev_girl3 "What... What's this sound?"

            "You are startled to hear a barking noise in the distance, closing in fast."

            ev_girl3 "Oh no... It's..."

            play sound s_scream

            ev_girl3 "DOGS!!!"

            "A pack of flea-ridden street dogs appears down the street, charging in your direction."

            play sound s_meow

            ev_girl3 "Hiiiii!!! I hate dogs, nyaaa!"

            hide screen show_event

            with dissolve

            "The girl jumps and runs away with feline agility. You ponder whether or not to follow her, but your reflexion is cut short by dozens of paws bumping you to the ground as the dogs proceeds to lick you mercilessly."

            with vpunch

            you "Haaa! No!!! It tickles!!!"



            "You have got fleas."

            $ result = 0

        elif r <= 2:

            you "I summon thee, ye little feline furball! Thy friend misses thee..."

            play sound s_spell

            "Long minutes pass by. The girl gives you an inquisitive look."

            ev_girl3 "Did it work? It's like nothing happened..."

            you "I'm sorry. I think..."

            play sound s_meow

            ev_girl3 "..."

            with vpunch

            ev_girl3 "Yuna!!!"

            hide screen show_event

            with dissolve

            $ p = rand_choice(encounter_pics["cat_found"])
            $ pic2 = Picture(p, "NPC/encounters/" + p)

            $ renpy.show_screen("show_event", pic2, _layer="master")

            with dissolve

            "A cute, slender cat is lazily walking towards you."

            $ result = 1

        else:

            you "Nine tails, nine lives, I summon thee, Neko spirit... Bring me thy kin, do us a favor and we will repay thee..."

            play sound s_spell

            ev_girl3 "You're glowing! Your scent is strange... Musky..."

            play sound s_meow
            pause 0.5
            play sound2 s_meow
            pause 0.3
            play sound3 s_meow

            hide screen show_event

            with dissolve

            $ p = rand_choice(encounter_pics["cat_found"])
            $ pic2 = Picture(p, "NPC/encounters/" + p)

            $ renpy.show_screen("show_event", pic2, _layer="master")

            with dissolve

            "As if appearing from thin air, the courtyard now fills with cats."

            ev_girl3 "Amazing! Coral! Mr. Kitty! Steve... The siamese twins!"

            "A herd of cats has answered your call. They gather at your feet and start purring, rubbing themselves against your legs."

            with vpunch

            ev_girl3 "Yuna!!!"

            play sound s_meow

            "A cute, regal-looking cat come out of a bush and walks leisurely towards you."

            ev_girl3 "She's here! Oh, mister, you're a genius!"

            $ result = 2

            if r > 5:

                $ result = 3


    else:

        $ norollback()

        you "Ahem, I don't have time to look for your pet. Anyway, I'm sure she's fine."

        ev_girl3 "No, waaait! You must help me!"

        "Ignoring her, you hasten to walk away from the deranged girl."

        hide screen show_event

        with dissolve

        return


    if result > 0:

        play sound s_meow

        "Yuna rubs herself against the girl's legs and starts purring with a noise rivalling a snoring dragon."

        play sound s_sigh

        ev_girl3 "Oh, Yuna, you silly whore! I was here worried out of my mind, and all the while you were out there fooling around with male cats!"

        ev_girl3 "Well, at least you had fun..."

        $ renpy.show_screen("show_event", pic, _layer="master")
        with fade

        ev_girl3 "Thanks, mister, I was so worried... It was lucky you were here to help!"

        ev_girl3 "Here, please have this. I've had this forever and I don't use it."

        hide screen show_event

        with dissolve

        $ _rank = 0 + brothel.get_effect("change", "city rewards")
        $ it = get_rand_item(rank=_rank)

        if it:
            call receive_item(it) from _call_receive_item_32
        else:
            bk_error "Couldn't generate Item for rank [_rank]"

        if result > 1:

            with fade

            "You walk the girl and her cat back to their place."

            ev_girl3 "Thank you, mister, you were amazing."

            play sound s_meow

            ev_girl3 "Yuna would also like to thank you..."

            you "Yuna? Err, I don't think it's necessary..."

            ev_girl3 "It's very necessary! You won't be disappointed, believe me... *wink*"

            "Turning to look at the cat, you gasp in amazement."

            if result == 2:

                $ pics = rand_choice(encounter_pics["cat_sex"])

                $ pic = Picture(pics[0], "NPC/encounters/" + pics[0])

                $ renpy.show_screen("show_event", pic, _layer="master")

                with dissolve

                play sound s_meow

                yuna "Hello, mister!"

                "A very human, very sexy, and very naked Yuna is looking at you with hungry eyes."

                play sound s_aah

                yuna "Yuna is in heat... It burns... Mister, won't you help Yuna? Nyaah..."

                yuna "Yuna has been with many cats, but now, Yuna wants a human dick... Yuna is dripping down there, just to think about a big, fat human cock..."

                yuna "Mister, won't you help a poor lonely pussy?"

                "You do not waste time giving her an answer. Soon, the air is filled with the wet sound of your love-making."

                play sound s_moans_quiet

                yuna "Yuna is so horny... Yuna needed a cock so bad... Nyaaaaah!"

                "You both enjoy it tremendously. It isn't long before climax..."

                play sound s_orgasm_young

                with flash

                yuna "Haaahaaaaaa!!!"

                $ pic = Picture(pics[1], "NPC/encounters/" + pics[1])

                $ renpy.show_screen("show_event", pic, _layer="master")

                with doubleflash

                yuna "Yuna is so happy... Aaaaah..."

                play sound s_mmmh

                hide screen show_event

                with fade

                "You have earned prestige."

                $ MC.change_prestige(selected_district.rank * brothel.get_effect("boost", "city rewards"))
                $ unlock_achievement("h catgirl", level_cap=1)

            elif result == 3:

                yuna "Hello, mister!"

                "A very human-like, very sexy, and very naked Yuna is looking at you with hungry eyes."

                play sound s_aah

                "But it isn't all... You feel a hand reach down your crotch, freeing your dick from your pants."

                play sound s_mmmh

                ev_girl3 "Mind if I join? I can't control myself right now..."

                "It seems like you have little choice but to oblige..."

                $ pics = rand_choice(encounter_pics["cat_duo"])

                $ pic = Picture(pics[0], "NPC/encounters/" + pics[0])

                $ renpy.show_screen("show_event", pic, _layer="master")

                with dissolve

                ev_girl3 "Such a big cock... Mister, isn't it too big for Yuna?"

                yuna "Nooo! It's just perfect! Go ahead, mister, fuck Yuna's pussy as hard as you can! Ahaa!!!"

                you "So tight... Hmmm..."

                play sound s_moans

                play sound2 s_moans_quiet

                yuna "Yuna can't take it anymore... Yuna is cumming..."

                ev_girl3 "Good girl, Yuna! Squeeze the nice mister's cock hard!"

                you "Ooooh..."

                with flash

                $ pic = Picture(pics[1], "NPC/encounters/" + pics[1])

                $ renpy.show_screen("show_event", pic, _layer="master")

                with dissolve

                with doubleflash

                play sound s_orgasm_young

                "You blow a thick load of cum into the catgirl's pussy."

                yuna "Aw... Yuna's pussy is so full... Full of hot cum... Nyaaah..."

                play sound2 s_aah

                ev_girl3 "Oh, I want some too... *licking her lips*"

                you "*pant* *pant*"



                hide screen show_event

                with dissolve

                pause 1.0

                $ renpy.show_screen("show_event", pic, _layer="master")

                with fade

                $ pic = Picture(pics[2], "NPC/encounters/" + pics[2])

                $ renpy.show_screen("show_event", pic, _layer="master")

                with dissolve

                ev_girl3 "Mister, this isn't finished!!! Let's go for another round!"

                "Your cock is still fully erect. These two pussycat sluts are just too damn sexy."

                you "Of course... Come here and spread your legs... Show me everything... That's it..."

                "You start fucking her, pumping in and out with your large cock, drilling deep into her tight cunt."

                "It isn't long before you are ready to cum a second time."

                you "Haaaaa!"

                play sound s_scream

                ev_girl3 "Hiiiii!!!"

                play sound2 s_meow

                yuna "Nyaaaaaaaah!!!"

                with flash

                "You pull out as you cum, spurting semen all over the girl's pussy."

                $ pic = Picture(pics[3], "NPC/encounters/" + pics[3])

                $ renpy.show_screen("show_event", pic, _layer="master")

                with dissolve

                with doubleflash

                play sound s_orgasm

                ev_girl3 "Creampie!!! I love cream..."

                play sound2 s_orgasm_young

                yuna "Ooooh... Yuna wants to lick it clean... Nyaaah..."

                "The two girls kneel at your feet, and hungrily lap every last drop from your shaft, then sharing a mouthful of semen in a passionate kiss."

                $ unlock_achievement("h catgirl")

                "It is already nightfall when you leave the two napping catgirls, covered your with sticky semen and purring in their sleep."

                hide screen show_event

                with dissolve

                $ MC.change_prestige((2+MC.interactions) * selected_district.rank * brothel.get_effect("boost", "city rewards"))

                "You have earned prestige. You have no remaining actions for the day."

                if MC.interactions:
                    "You have received a prestige boost from your [MC.interactions] spent AP."

                $ MC.interactions = 0

    else:

        "Sighing, you walk back towards the [loc], cursing the unfathomable stupidity of furry animals."

    return


label city_secret:

    $ norollback()

    $ loc = selected_location.name.lower()

    "As you turn into an alley near the [loc], you notice a shady figure standing in a dark corner."

    hide screen visit_location

    hide screen overlay

#    stop music fadeout 2.0

    $ p = rand_choice(encounter_pics["secret"])

    $ pic = Picture(p, "NPC/encounters/" + p)

    scene black with dissolve

    $ renpy.show_screen("show_event", pic, _layer="master")

    with dissolve

    "You instinctively retreat in the shadows to observe. You want to figure out what's going on before showing yourself."

    "The man isn't paying attention to his surroundings, anyway. He is fiddling with some sort of mechanism on the wall."

    with vpunch

    play sound s_crash

    "You hear a slow rumble, then a heavy thump. The man steps back from the wall, and looks around cautiously. He then walks away, trying to look casual."

    "Once you are sure he is gone, you walk up to the place where he was standing."

    with fade

    "Looking at the wall, you see nothing at first. Upon close examination, thin lines seem to mark the shape of a secret door. If there is an opening mechanism, however, you don't see it."

    # Pick challenge
    $ tt = show_tt("top_right")
    $ chal = renpy.call_screen("challenge_menu", challenges=[("Force the door open", "force", selected_district.rank + 3), ("Reveal with magic", "detect", selected_district.rank+3)], cancel=("Walk away", False))
    hide screen tool


    if chal == "force":
        $ norollback()

        you "There's nothing that can't be solved with a little violence."

        "Taking the measure of the wall and its resistance before making your move, you take a step back."

        you "Kyaaaah!!!"

        "Using all your strength, you dash your shoulder into the door."

        # Run challenge
        call challenge(chal, selected_district.rank + 3) from _call_challenge_22 # result is stored in the _return variable
        $ r = _return

        if r:

            with vpunch

            play sound s_punch

            "The lock snaps with a cracking sound, and the battered door slams open before you. You barely avoid falling down a steep stairway right behind the door."

            you "I wonder where this leads..."

        else:

            play sound s_wscream

            you "Ouch!!!" with vpunch

            "You slam into the wall, doing no visible damage, except to your shoulder and pride."



    elif chal == "detect":

        $ norollback()

        "Stepping back, you take a pouch from your belt."

        "You take a handful of silver dust from the pouch, which you spread on the wall before you."

        you "I am the seeker of secrets! None shall be hidden from my all-seeing eye..."

        you "Open sesame!"

        # Run challenge
        call challenge(chal, selected_district.rank + 3) from _call_challenge_23 # result is stored in the _return variable
        $ r = _return

        if r:

            "The silver powder shines with incandescent light, illuminating the wall's surface."

            play sound s_spell

            "Eventually the light recedes, except over the right side of the wall, where it delineates a hidden runic seal."

            with vpunch

            play sound s_crash

            "Easily deciphering the rune, you apply pressure on the correct spot. The wall slides open, revealing a dark staircase."

        else:

            "A sudden gust of wind clears out all of the silver dust. Cursing, you reach inside your pouch, but there is not enough powder left."

            play sound s_fizzle

            you "Damn... This powder isn't cheap..."


    else:

        $ norollback()

        "You don't see any easy way to open it."

        you "This is a waste of time. Let's just go."

        hide screen show_event

        with dissolve

        return


    if r: # 33% * 50% chance of yielding a Wyvern egg (1 in 6)

        with fade

        "You carefully follow the steps down, eventually reaching a dark cellar."

        if dice(6) < 5:

            $ p = rand_choice(encounter_pics["secret_empty"])

            $ pic = Picture(p, "NPC/encounters/" + p)

            $ renpy.show_screen("show_event", pic, _layer="master")

            with dissolve

            "The place is eerily quiet as you move about and search the rooms."

            "There isn't much to be found in this labyrinth. You decide to follow some footprints in the dust."

            "The trail leads you to a chest, which looks like it was used recently."

            "Inside, you find something that could be of use to you."

            hide screen show_event

            with dissolve

            $ _rank = selected_district.rank + brothel.get_effect("change", "city rewards")
            $ it = get_rand_item(rank=_rank)

            if it:
                call receive_item(it) from _call_receive_item_33
            else:
                bk_error "Couldn't generate Item for rank [_rank]"

        else:

            play sound s_moans_quiet

            "You emerge into a candle-lit room, full of intriguing contraptions."

            "You can hear muffled moans coming from a corner of the room."

            $ p = rand_choice(encounter_pics["secret_girl"])

            $ pic = Picture(p, "NPC/encounters/" + p)

            $ renpy.show_screen("show_event", pic, _layer="master")

            with dissolve

            "You see a girl there, bound and gagged. She sees you, but doesn't seem to react to your presence."

            "The air is thick with the smell of moisture and semen."

            you "Do you need help?"

            play sound s_scream

            "She ignores you, instead concentrating on something that's happening to her."

            play sound s_vibro

            "You can hear the vibration of a sex toy, plugged deep inside the girl."

            play sound s_orgasm_fast

            ev_girl1 "Aaaaaaaaaah!!!"

            with flash

            "She reaches a quiet orgasm as you watch, apparently the latest in a long series."

            "You notice something unexpected, shoved into one of the girl's slutty holes."

            you "Do you mind?"

            with vpunch

            play sound s_mmmh

            "You retrieve the item. It could be useful, after Sill gives it a good washing."

            hide screen show_event

            with dissolve

            $ _rank = selected_district.rank + brothel.get_effect("change", "city rewards")

            if _rank >= 3 and dice(6 >= 4):
                $ it = wyvern_egg
            else:
                $ it = get_rand_item(rank=_rank)

            if it:
                call receive_item(it) from _call_receive_item_34
            else:
                bk_error "Couldn't generate Item for rank [_rank]"

    else:

        "There's nothing more you can do. Grumbling, you head back towards the [loc]."

        hide screen show_event

        with dissolve

    return


label city_gypsy:

    $ norollback()

    $ loc = selected_location.name.lower()

    "Strolling around the [loc], you meet a lone girl in exotic clothes, with a worried look on her face."

    hide screen visit_location

    hide screen overlay

#    stop music fadeout 2.0

    $ pics = rand_choice(encounter_pics["gypsy"])

    $ gypsy = ProportionalScale("NPC/encounters/" + pics[0], xres(560), yres(600))

    $ pic = selected_location.get_pic(config.screen_width, int(config.screen_height*0.8))

    scene black with dissolve

    show image pic at top

    with dissolve

    show image gypsy at center
    with dissolve

    if MC.playerclass == "Warrior":

        $ nickname = "猛男"

        $ nickname_l = "猛男"

    elif MC.playerclass == "Wizard":

        $ nickname = "怪胎"

        $ nickname_l = "怪胎"

    elif MC.playerclass == "Trader":

        $ nickname = "开心果"

        $ nickname_l = "开心果"

    play sound s_surprise

    ev_girl2 "Hey, you! [nickname]!"

    you "Uh? Me?"

    ev_girl2 "Yes! [nickname]! I need your help. Please?"

    "You look at her with suspicion. She has an exotic look about her. She doesn't look like she's from around here."

    ev_girl2 "My wagon broke down on the way to the market. It's stuck here, in this deserted place."

    "You can see her wagon down in a small street. It's in a sorry state, stuck in the mud with a broken wheel."

    ev_girl2 "I can't find any customers here, and without customers I cannot get the money I need to get the repairs done!"

    you "And what is it that you do?"

    ev_girl2 "I'm a fortune teller. Want to know the exact place, cause and depth of agony of your inevitable death? I can tell you."

    you "Erm, no, thanks..."

    ev_girl2 "So, [nickname_l]. Will you help me?"

    # Pick challenge
    $ tt = show_tt("top_right")
    $ chal = renpy.call_screen("challenge_menu", challenges=[("Fix the wagon", "force", selected_district.rank + 3), ("Bring some customers", "rally", selected_district.rank+3)], cancel=("Decline to help", False))
    hide screen tool

    if chal == "force":

        $ norollback()

        you "I could always try to fix your ride... Let me have a look."

        ev_girl2 "Thank you, [nickname_l]! You're a dear!"

        "You try to fix the broken cart to the best of your ability, but you're not sure it can hold together."

        "Now you must pull the cart out of the mud. This requires some heavy lifting."

        you "HAAAAAAAA..."

        # Run challenge
        call challenge(chal, selected_district.rank + 3, score=True) from _call_challenge_24 # result is stored in the _return variable
        $ r = _return

        if r < 0:

            with vpunch

            play sound s_punch

            "The cart is too heavy, and your hands slip. You fall down in the mud, cursing."

            you "Fuck!!!"

            ev_girl2 "Ooooh... The wheel broke down again... And you've splashed mud all over the place!"

            you "Well, excuse me, I was just trying to help..."

            $ result = 0

        elif r <= 2:

            "You push the cart with all your strength, trying different angles to get it unstuck."

            with hpunch



            "The wagon rocks back and forth, and you hear the sound of broken glass coming from the inside."

            ev_girl2 "Hey!!! My philters!!!"

            play sound s_crash

            with vpunch

            "After a few minutes, however, your efforts are rewarded. The cart rolls grudgingly out of the mud."

            ev_girl2 "You did it!!!"

            you "*pant*, *pant*"

            "It looks like the cart's damaged wheel can hold long enough to make it to the market."

            $ result = 1

        else:

            with vpunch

            "Using your considerable might, you lift the cart off the ground and safely put it back on the pavement."

            ev_girl2 "You did it, [nickname_l]!!! It's amazing!!!"

            you "*pant* It was easy... *pant*"

            ev_girl2 "Let me touch those big muscles of yours... Oh, they're nice..."

            $ result = 2



    elif chal == "rally":

        $ norollback()

        you "I can go to the main street, and tell people about your services. Word of mouth could help."

        ev_girl2 "Oh..."

        ev_girl2 "You're right, [nickname_l]! It's certainly worth trying."

        hide gypsy with dissolve

        "You walk back to the main street near the [loc], and start telling people about the fortune teller."

        you "Come with me, friends, meet the amazing lass who can reveal your future! Destiny awaits, just a few steps away!"

        # Run challenge
        call challenge(chal, selected_district.rank + 3, score=True) from _call_challenge_25 # result is stored in the _return variable
        $ r = _return

        if r < 0:

            "Most people ignore you, however, until you run into a group of Arios worshippers."

            man "Heretic! This foul heretic is advertising the services of a witch!"

            "You get into an argument with the man, while a crowd of curious onlookers gathers around you."

            man "No doubt he wants to lead us into an alley so he can slit our throat! Down with the heretic!"

            "The crowd roars in agreement. Things are starting to look nasty as the man becomes more threatening."

            man "Come with us!"

            play sound s_sword_sheath

            "You flash your weapon, and the crowd takes a step back. Before they can react, you jump into a side street and make your escape."

            with fade

            you "That was close..."

            $ result = 0

        elif r <= 2:

            "You don't have much success at first, but with time, you are able to send a few customers her way."

            "You hope it will be enough for her to make ends meet."

            with fade

            "After an hour or so, you come back to the wagon. You run into one of the customers, exiting the broken wagon with a large smile on his face."

            show image gypsy with dissolve

            you "Hello there! Did you get enough to get by?"

            ev_girl2 "I did! Some customers paid extra... It helped."

            "She looks a bit uneasy and straightens her clothes as she speaks."

            $ result = 1

        else:

            "Using your great people skills, you quickly convince a few passersby to listen to you."

            "The crowd grows even larger when a bunch of sailors come to listen, fresh off their ship."

            man "Hey, let's get our fortune told! I wanna know when I'm gonna get laid!"

            "People pour into the alley, eager to get their fortune told."

            with fade

            "You come back to the girl's wagon after a while, happy with the business you sent her way."

            show image gypsy with dissolve

            ev_girl2 "Hey, it's you!!! I made a killing! It's amazing!"

            "She hugs you and kisses your cheek."

            ev_girl2 "It's all thanks to you, [nickname_l]! I'm really grateful..."

            $ result = 2

    else:

        $ norollback()

        you "I'm sorry, but I can't do anything about it. Best of luck with your problem."

        ev_girl2 "Hey, waaaait!"

        hide gypsy with dissolve

        hide pic

        with dissolve

        return

    if result == 0:

        hide gypsy with dissolve

        hide pic

        with dissolve

        "You go back to the [loc]."



    elif result == 1:

        ev_girl2 "Thank you, [nickname_l], you did me a favor! Here, wait a second..."

        "The girl rummages through her wagon for a minute, then comes out, holding a dusty item."

        ev_girl2 "Here, have this."

        hide gypsy with dissolve

        hide pic

        with dissolve

        $ _rank = selected_district.rank + brothel.get_effect("change", "city rewards")
        $ it = get_rand_item(rank=_rank)

        if it:
            call receive_item(it) from _call_receive_item_35
        else:
            bk_error "Couldn't generate Item for rank [_rank]"


    elif result == 2:

        "She leans into your ear and whispers."

        ev_girl2 "You saved me, [nickname_l], so I will show you something interesting... Follow me..."

        hide gypsy

        with dissolve

        hide screen show_event

        with dissolve

        if dice(6) < 5:

            $ kinky = False
            $ pic = Picture(pics[1], "NPC/encounters/" + pics[1])

        else:

            $ kinky = True
            $ pic = Picture(pics[2], "NPC/encounters/" + pics[2])

        $ renpy.show_screen("show_event", pic, _layer="master")

        with dissolve

        play sound s_sucking

        ev_girl2 "Oh, [nickname_l]! Give it to me... Mmmh..."

        if kinky:

            play sound2 s_aah

            ev_girl2 "Aaaaaah! I... I didn't know you liked this sort of things..."

            you "You seem to enjoy it just as much as me..."

            "Her eyes are glistening with lust. You can't hold back much longer."

            play sound2 s_scream

            "She screams with delight as you proceed to cum all over her face."

            with flash

            you "Aaaaah!!!"

            with doubleflash

            play sound s_orgasm_fast

            ev_girl2 "I'm cumming!!! Hiiiiii!!!"

        else:

            ev_girl2 "Your dick is so big and tasty... Give me your juice..."

            you "Oh, it's good... Oooooh..."

            with flash

            play sound2 s_surprise

            ev_girl2 "Oooh!!!"

            with doubleflash

            "You cum hard thanks to the girl's expert technique, and she looks with satisfaction at your spurting cock."

            play sound s_ahaa

        "The girl gently licks the cum off your shaft while you take a short rest."

        play sound s_mmmh

        ev_girl2 "Mmmmh..."

        ev_girl2 "I almost forgot... I have this I no longer need. I'm sure you can put it to good use."

        ev_girl2 "Now... I hope you're ready for round two! *wink*"
        $ unlock_achievement("h gypsy")

        play sound s_mmmh

        hide pic

        hide screen show_event

        with dissolve

        $ _rank = selected_district.rank + brothel.get_effect("change", "city rewards")
        $ it = get_rand_item(rank=_rank)

        if it:
            call receive_item(it) from _call_receive_item_36
        else:
            bk_error "Couldn't generate Item for rank [_rank]"

        $ MC.change_prestige(selected_district.rank * brothel.get_effect("boost", "city rewards"))


    return


label city_rob:

    $ norollback()

    $ loc = selected_location.name.lower()

    "As you pass through one of the [loc]'s less reputable parts, you see a woman barring your way."

    hide screen visit_location

    hide screen overlay

    stop music fadeout 2.0

    $ pics = rand_choice(encounter_pics["rob"])

    $ robber = ProportionalScale("NPC/encounters/" + pics[0], xres(560), yres(600))

    $ pic = selected_location.get_pic(config.screen_width, int(config.screen_height*0.8))

    scene black with dissolve

    show image pic at top

    with dissolve

    show image robber with dissolve

    woman "Hey there, Mister! Going somewhere?"

    play sound s_sword_sheath

    woman "Don't be in such a hurry..."

    "The woman is armed, and casually pointing her weapon at you."

    woman "This pouch of gold is weighting you down, methinks. Why don't you hand it over, and be on your way?"

    $ sex = False

    $ girl_def = dice(3, selected_district.rank)

    # Pick challenge
    $ tt = show_tt("top_right")
    $ chal = renpy.call_screen("challenge_menu", challenges=[("Defend yourself", "fight", girl_def), ("Charm her", "charm", girl_def)], cancel=("Give her some gold", False))
    hide screen tool

    if chal == "fight":

        $ norollback()

        "You are not going to let yourself be pushed over by a girl."

        you "Out of my way, bitch, or I'll crush you like a worm."

        # Run challenge
        call challenge(chal, girl_def, score=True) from _call_challenge_26 # result is stored in the _return variable
        $ r = _return

        if r < 0:

            play sound s_evil_laugh

            "She laughs."

            woman "Oh, a stubborn one. Have it your way, sucker!"

            "She takes an attack stance. You reach for your weapon."

            play sound s_sword_sheath

            with vpunch

            "With lightning speed, the woman leaps in the air above you."

            woman "KYAAAAAAAAAAH!!!"

            play sound s_punch

            with vpunch

            "You have no time to react before she clubs you on the head with the blunt of her weapon. You fall down in the dirt, nearly passing out."

            woman "Taking on the queen of bandits! You're lucky to be alive..."

            play sound s_evil_laugh

            woman "Now, if you'll excuse me, I have other weaklings to attend to."



            "She swiftly liberates your purse from your belt."

            play sound s_gold

            woman "Thank you! Have a nice day!"

            "When you come back to your senses, she's long gone."

            hide robber with dissolve

            hide screen show_event

            with dissolve

            $ loss = (74 + dice(76)) * selected_district.rank

            if loss >= MC.gold:
                if MC.gold > 0:
                    $ loss = MC.gold
                else:
                    $ loss = 0

            $ MC.gold -= loss

            "You have lost %(loss)d gold."


        elif r <= 2:

            "She takes a second look at you."

            woman "Humph... Maybe this won't be as easy as I thought. *mutter*"

            play sound s_surprise

            woman "All right! I'm in a good mood today, you're in luck!"

            woman "You can go, but next time, you will have to pay my toll."

            you "Whatever. *sigh*"

            scene black with dissolve

            "You push past her and make your way back to the [loc]."

        else:

            woman "Who do you think you are! I'll teach you!!! I'll..."

            play sound s_sword_sheath

            pause 0.3



            play sound2 s_punch

            with vpunch



            "In one fell swoop, you draw your sword and smash her weapon out of her hands."

            play sound s_surprise

            "She squeals and looks at her empty hands in disbelief."

            woman "F... Fast... How..."

            "You point your weapon at her throat."

            you "Shut up. You're coming with me now, we'll have a word with the guard."

            play sound s_scream

            woman "The guard? Noooo! They'll rape and torture me! Please, Mister, I'll do anything!"



            you "..."

            "You take a good look at her. She's got a nice figure."

            you "Anything, uh?"

            play sound s_sigh

            woman "Yes..."

            you "Follow me, then."

            $ sex = "strength"

    elif chal == "charm":

        $ norollback()

        "You decide to charm your way out of this."

        you "Well, hello, my lady. *smile*"

        # Run challenge
        call challenge(chal, girl_def, score=True) from _call_challenge_27 # result is stored in the _return variable
        $ r = _return

        if r < 0:

            you "I, uh... I bet your dad was a thief too!"

            play sound s_sigh

            woman "Oh, really, why?"

            you "Because he stole all of the stars in the night sky... And put them into your eyes! Hahaha... *nervous*"

            woman "..."

            you "Stars? In your eyes? It means you have beautiful eyes, you see... get it?"



            "Her eyes narrow. She raises her weapon and points it at your face."

            play sound s_sword_sheath

            woman "I should kick your ass just for using such a cheesy pick up line!!! Hand over your purse, NOW!"

            you "Aw..."

            woman "And make sure to empty your pockets, too..."

            play sound s_gold

            "You reluctantly hand over all your gold."

            play sound s_evil_laugh

            woman "So long, sucker! *laugh*"

            scene black with dissolve

            $ loss = (74 + dice(76)) * selected_district.rank

            if loss >= MC.gold:
                if MC.gold > 0:
                    $ loss = MC.gold
                else:
                    $ loss = 0

            "You have lost %(loss)d gold."

            $ MC.gold -= loss

        elif r <= 2:

            you "I know you."

            woman "You do?"

            you "You're the one they call the queen of bandits, aren't you? Whose beauty and cunning is the talk of all the town?"

            play sound s_sigh



            woman "Well, err..."

            play sound s_evil_laugh

            woman "Yes! That's me, of course, haha!"

            you "They say you got out of a thousand traps, and evaded arrest a hundred times! You made a mockery of the guard and are the darling of the people..."

            woman "Oh, well... This is a little exaggerated... *blush*"

            you "They also said you were a real beauty, and now I can see they were telling the truth..."

            play sound s_sigh

            woman "Oh, what a gentleman... Ok, you may go. Spread the word of my generosity in those taverns of yours, will ya!"

            you "Of course, my lady. *smile*"

            scene black with dissolve

            "You head back to the [loc] without incident."

        else:

            you "Are you really going to rob me? A second time?"

            play sound s_surprise

            woman "What do you mean, a second time?"



            you "Because you already stole my heart..."

            play sound s_surprise

            woman "Uh, what?"

            you "I haven't seen a girl so fair in this entire kingdom. My lady, you're the jewel of the [loc]."

            woman "I am... What?"

            you "Your fair skin and beautiful smile is reason enough for anyone to drop at your feet in adoration."

            "You take a knee."

            play sound s_surprise

            woman "Oh..."

            play sound s_sigh

            woman "No one... No one has ever talked to me like this..."

            woman "You're quite handsome yourself, if I may say so... *blush*"

            you "My lady, you're even more beautiful when you're blushing.."

            play sound s_aah

            woman "Oh, you devil..."

            you "Come on, why don't we move from this wretched place to somewhere more... Comfortable?"

            "You offer your arm. She looks on hesitantly."

            play sound s_sigh

            "Eventually, she smiles and sheathes her weapon. She takes your arm and you lead her away from the [loc]."

            $ sex = "charm"


    else:

        $ norollback()

        "You decide it's best to avoid a confrontation."

        play sound s_gold

        you "I don't want no trouble. Here, have this."

        play sound s_evil_laugh

        woman "Good, very good! I knew you were a reasonable man."

        scene black with dissolve

        $ loss = (49 + dice(51)) * selected_district.rank

        if loss >= MC.gold:
            if MC.gold > 0:
                $ loss = MC.gold
            else:
                $ loss = 0

        "You have lost %(loss)d gold."

        $ MC.gold -= loss


    if sex:

        scene black with fade

        $ pic = Picture(pics[1], "NPC/encounters/" + pics[1])

        $ renpy.show_screen("show_event", pic, _layer="master")

        with dissolve

        play sound s_moans

        woman "Mister... Oh!!!"

        you "Who would have thought... The queen of bandits is also the queen of sluts... Hmmpf..."

        woman "Oh, ah, don't say that... *blush*"

        you "I am not finished with you..."

        with vpunch

        "You keep teasing and fucking her in different positions until she reaches her limit."

        play sound s_screams

        woman "Oh, no... I'm cumming again, aaaah!"

        play sound s_orgasm_young

        with flash

        "She squirts like a fountain as she cums once more. Exhausted, she falls to the floor in a pool of bodily fluids."

        with doubleflash



        woman "Aaaaah..."
        $ unlock_achievement("h robber")

        hide screen show_event

        with fade

        if sex == "strength":

            if MC.get_alignment == "good":

                "You let her rest for a while at the brothel, then send her on her way."

            else:

                "After you have your way with her, you have her thrown out into the street, naked and reeking of semen."

            "You have earned prestige."

            $ MC.change_prestige(selected_district.rank * brothel.get_effect("boost", "city rewards"))

        elif sex == "charm":

            "You make your escape while she lays there sleeping."

            "You have earned prestige."

            $ MC.change_prestige(selected_district.rank * brothel.get_effect("boost", "city rewards"))

    return


label city_ambush:

    $ norollback()

    $ loc = selected_location.name.lower()

    "Walking through the [loc] looking for a shortcut, you suddenly get a sinking feeling in your stomach."

    hide screen visit_location

    hide screen overlay

#    stop music fadeout 2.0

    $ p = rand_choice(encounter_pics["ambush"])

    $ pic = Picture(p, "NPC/encounters/" + p)

    scene black with dissolve

    $ renpy.show_screen("show_event", pic, _layer="master")

    with dissolve

    play sound s_sword_sheath

    "You hear a commotion, and turn to see a vicious thug rushing towards you."

    play sound2 s_sword_sheath

    pause 0.2

    play sound3 s_sword_sheath

    "It's an ambush!"

    $ ambush_attack = 2 + selected_district.rank

    # Pick challenge
    $ tt = show_tt("top_right")
    $ chal = renpy.call_screen("challenge_menu", challenges=[("Fight back", "fight", ambush_attack), ("Cast a spell", "cast", ambush_attack+1)], cancel=("Run for your life", False))
    hide screen tool

    if chal == "fight":
        $ norollback()

        "You won't give up without a fight."

        play sound s_sword_sheath

        you "Bring it on!"

        # Run challenge
        call challenge(chal, ambush_attack) from _call_challenge_28 # result is stored in the _return variable
        $ r = _return

        if r:

            "You exchange quick blows with the ruffian, matching each of his assaults with an attack of your own."

            play sound s_sword_clash

            with vpunch

            pause 0.2

            play sound2 s_sword_clash

            with hpunch

            pause 0.3

            play sound s_sword_clash

            with vpunch

            pause 0.1

            play sound2 s_sword_clash

            with vpunch

            "Your last blow is enough to make your opponent lose his footing momentarily. Seeing an opening, you plunge and strike a deadly blow."

            play sound s_sword_sheath

            pause 0.6

            play sound s_wscream

            with vpunch

            "Bandit" "Aaargh!!!"

            "You opponent falls flat into the dirt, lifeless. The rest of the scum scatters in fear."



            you "Anybody else wants to negotiate?"

            play sound s_sword_sheath

            hide screen show_event

            with fade

            "You escape unscathed and reach the relative safety of the [loc]."

        else:

            play sound2 s_sword_clash

            with hpunch

            pause 0.3

            play sound s_sword_clash

            with vpunch

            "You dodge an incoming blow and barely manage to parry another one."

            you "Damn you, lowlife!"

            "As you prepare to retaliate, however, an unseen opponent hits you from behind with a sap."

            play sound s_punch

            with vpunch

            you "Ouch!!!"

            with vpunch

            play sound s_punch

            "You see stars and fall down on the ground. Everything turns to black."

#                play sound s_crowd_laugh

            hide screen show_event

            with fade

            "You wake hours later, with a crippling headache and an empty purse."

            play sound s_gold

            $ loss = (74 + dice(76)) * selected_district.rank

            if loss >= MC.gold:
                if MC.gold > 0:
                    $ loss = MC.gold
                else:
                    $ loss = 0

            "You have lost %(loss)d gold. You are wounded and lose your remaining actions for the day."

            $ MC.gold -= loss

            $ MC.interactions = 0


    elif chal == "cast":

        $ norollback()

        you "Come on, punk, make my day."

        "Staff in hand, you stand amongst your opponents, reciting the words of a powerful spell."

        # Run challenge
        call challenge(chal, ambush_attack+1) from _call_challenge_63 # result is stored in the _return variable
        $ r = _return

        if r:

            play sound s_spell

            "A whirlwind of magic engulfs you, blinding your opponents."

            you "THUNDER!!!"

            play sound s_lightning

            with flash

            with vpunch

            pause 0.3

            play sound2 s_lightning

            with flash

#                pause 0.2
            play sound3 s_lightning

            with flash



            with vpunch

            "Chain lightning strikes all around you. Your opponent is hit and burnt to a crisp."

            play sound s_wscream

            man "Aha-ha-haw!"

            "Overwhelmed with shock and awe, the surviving bandits scatter in all directions, running for their lives."

            you "You've been... Thunderstruck!"

            hide screen show_event

            with fade

            "You return to the [loc] without further incident."

        else:

            you "KA!!!"

            you "ME!!!"

            you "HA..."

            play sound s_fizzle

            "Before you get a chance to finish your incantation, however, your opponent is upon you."


            play sound s_punch

            with vpunch


            you "ME... OUCH!!!"



            "The rogue hits you in the stomach, knocking you right out of breath."

            man "Disarm him!"

            play sound s_sword_clash

            with vpunch

            "The thugs kick your staff out of your hands, and proceed to give a good old-fashioned beating."

            play sound s_punch

            with vpunch

            pause 0.2

            play sound2 s_punch

            with vpunch

            pause 0.1

            play sound3 s_punch

            with vpunch

            you "Ouch! Arrh! Raah!!!"

            play sound3 s_punch

            with vpunch

            "They keep going until you have no fight left inside of you."

            you "Stop..."

            play sound s_crowd_laugh

            "They leave you crumpled on the floor in a sorry state, with an empty purse and an empty bladder."

            you "*sob*"

            hide screen show_event

            with fade

            $ loss = (74 + dice(76)) * selected_district.rank

            if loss >= MC.gold:
                if MC.gold > 0:
                    $ loss = MC.gold
                else:
                    $ loss = 0

            play sound s_gold

            "You have lost %(loss)d gold. You are wounded and lose your remaining actions for the day."

            $ MC.gold -= loss

            $ MC.interactions = 0


    else:

        $ norollback()

        you "Aaaaaah!!!!"

#            play sound s_steps

        with vpunch

        "You run away as quickly as possible, dodging throwing knives and arrows."

        you "Damn you!"

        "The bandits are hot on your trail. You have to find a way to throw them off."

        you "I guess I have no choice..."

        "Reaching for your purse, you start throwing denars into the air."

        play sound s_chimes

        man "Gold! It's gold!"

        "As expected, the men soon give up on their pursuit, stopping to gather the gold you've left behind."

        hide screen show_event

        with fade

        you "That was close..."

        $ loss = (49 + dice(51)) * selected_district.rank

        if loss >= MC.gold:
            if MC.gold > 0:
                $ loss = MC.gold
            else:
                $ loss = 0

        play sound s_gold

        "You have lost %(loss)d gold."

        $ MC.gold -= loss

    return


label city_mob:

    $ norollback()

    $ loc = selected_location.name.lower()

    "After an uneventful visit to the [loc], you find a large mob barring the road on your way back."

    hide screen visit_location

    hide screen overlay

    stop music fadeout 2.0

    $ p = rand_choice(encounter_pics["mob"])

    $ pic = Picture(p, "NPC/encounters/" + p)

    scene black with dissolve

    $ renpy.show_screen("show_event", pic, _layer="master")

    with dissolve

    man "Down! Down with demon worshippers and heretics!"

    man "They hide amongst our people, spreading vice and corruption in their filthy taverns and whorehouses..."

    "The crowd cheers frantically. You try to push through, but the mob is unwilling to let you pass."

    with vpunch

    "Somebody grabs you by the collar."

    man "Wait!!! I recognize him!"

    $ place = district.name.lower()

    man "He's one of the brothel owners! The scum of [place]!!!"

    "An angry chatter emerges from the crowd. People are blocking your way on every side, some trying to get ahold of you."

    "You push back desperately. They are too many for you to fight them off, however."

    you "Fellas, I..."

    $ mob_power = 1 + selected_district.rank

    # Pick challenge
    $ tt = show_tt("top_right")
    $ chal = renpy.call_screen("challenge_menu", challenges=[("Cast a control spell", "control", mob_power), ("Make a speech", "rally", mob_power)], cancel=("Divert attention with gold", False))
    hide screen tool

    if chal == "control":

        $ norollback()

        man "You! Confess! You're a devil worshipper, aren't you! A mage, a witch! Maybe even a druid!"

        you "You're making a mistake, good sir..."

        "Waving your hand in front of him, you cast a minor controlling spell."

        you "You need to let me go. I am not the one you are looking for."

        # Run challenge
        call challenge(chal, mob_power) from _call_challenge_30 # result is stored in the _return variable
        $ r = _return

        if r:

            play sound s_spell

            man "We... need to let him go. This is not the druid we are looking for."

            "The crowd wavers in surprise. Some people question the man's judgement."

            man "I said let him go! It's not him. End of story."

            "People grumble and curse, but they respect the elder's command. They reluctantly let you go, and you make it out more or less unharmed."

        else:

            play sound s_fizzle

            man "Oh, but I know who you are! Heretic!!! We'll give you a lesson you won't forget!"


    elif chal == "rally":

        $ norollback()

        "Stepping on a nearby crate, you turn to face the angry crowd."

        you "Good people of Zan! Listen to me."

        # Run challenge
        call challenge(chal, mob_power) from _call_challenge_31 # result is stored in the _return variable
        $ r = _return

        if r:

            you "Yes, brothels are places of sin and debauchery..."

            "The crowd grumbles menacingly."

            you "But think about it: whoring has been, is and will always be a part of our lives."

            you "Have you ever seen a place in Xeros without a hooker? It doesn't exist."

            "People mutter in agreement. The elder steps forward to confront you."

            man "Lies! Your kind is an abomination in the eyes of Arios!"

            you "Oh, really? But what does Arios teach us? To seek the light. If you refuse the sex trade to be out in the open, it will only move to the shadows. Into the realm of Shalia, far from Arios's reach. Is that what you want?"

            man "Well, err... No, I meant..."

            "The crowd is warming up to your argument."

            you "Who here hasn't sinned at least once? As long as brothels remain out in the open, they are sanctuaries of the Light just like any other place."

            "Men in the crowd start to show approval. The elder is struggling to find arguments, but the mob isn't listening to him anymore."

            you "Very well, friends, now you see why brothels are so important. Come to the brothel, tonight, and there will be a special discount for Arios worshippers!"

            play sound s_crowd_laugh

            "The crowd cheers and applauds your speech. The elder steps back, looking dejected."

        else:

            $ cover = rand_choice(brothel.get_common_rooms()).name

            you "He lies!"

            you "My establishment is not a whorehouse! It is a reputable [cover], and I am a lawful citizen!"

            man "It is a brothel! I went there on a, ahem, an errand, and I saw half-naked girls rubbing themselves against a customer. And the prices were outrageous, too! Not that I'd care, of course, but..."

            "Other witnesses come out of the crowd. Accusations fly. No one seems to believe you."

            you "Good people!"

            "Your cries of protest are drowned by angry booing and jeering."

            with vpunch

            man "Catch him!"

    else:

        $ norollback()

        you "Oh, wait! What's this?"

        "Opening your pouch, you throw a fistful of gold in the air."

        with vpunch

        play sound s_chimes

        "Forgetting all about heretics and righteousness, the crowd erupts into a massive brawl, trying to grab some of the money."

        man "People of Zan! Listen! Listen to me!!!"

        "The man is unable to restore order. He gives you a murderous look. You wink at him and elbow your way out of the crowd, safely retreating towards the [loc]."

        hide screen show_event

        with fade

        $ loss = (49 + dice(51)) * selected_district.rank

        if loss >= MC.gold:
            if MC.gold > 0:
                $ loss = MC.gold
            else:
                $ loss = 0

        play sound s_gold

        "You have lost %(loss)d gold."

        $ MC.gold -= loss

        return

    if r:

        hide screen show_event

        with fade



        if dice(6) >= 5:

            $ p = rand_choice(encounter_pics["mob_sex"])

            $ pic = Picture(p, "NPC/encounters/" + p)

            "Deprived of a scapegoat, the mob instead corners a group of women pilgrims."

            $ renpy.show_screen("show_event", pic, _layer="master")

            with dissolve

            play sound3 s_screams

            pause 0.3

            play sound s_scream

            pause 0.4

            play sound2 s_scream_loud



            "They rape them mercilessly, accusing them of withcraft."

            man "That will teach you, you evil demon-worshipping bitches! Hmm..."

            play sound s_screams

            with doubleflash



            hide screen show_event

            with dissolve

        "You retreat to the safety of the [loc]."

    else:

        "The angry mob starts beating you, spitting on you and ripping at your clothing as you do your best to escape."

        play sound s_punch

        with vpunch

        pause 0.3

        play sound2 s_punch

        with vpunch

        pause 0.1

        play sound3 s_punch

        with vpunch

        you "No... Not the face!!!"

        "Protecting yourself the best you can, you barely make it through to the other side of the crowd."

        play sound s_punch

        with vpunch

        you "Ouch! Aaah!"

        "You run off as fast as you can, followed by curses and rotten fruits thrown by the angry mob."

        "You do not stop running until you have reached the safety of your brothel."

        "Pausing to catch your breath and lick your wounds, you notice your purse is missing."

        you "Hell..."

        hide screen show_event

        with fade

        $ loss = (74 + dice(76)) * selected_district.rank

        if loss >= MC.gold:
            if MC.gold > 0:
                $ loss = MC.gold
            else:
                $ loss = 0

        play sound s_gold

        "You have lost %(loss)d gold. You are tired and lose your remaining actions for the day."

        $ MC.gold -= loss

        $ MC.interactions = 0


    return


label city_none:

    $ norollback()

    $ loc = selected_location.name.lower()

    $ choices = ["You take a stroll through the %s. Nothing meaningful happens.", "After a pleasant walk around the %s, you decide it's time to head home.",
                 "The %s is peaceful today. You have a pleasant walk.", "You spend time browsing the wares of some passing merchants near the %s. In the end, you don't find anything you like.",
                 "You have a nice time sitting on a bench near the %s, watching people come and go and whistling at pretty girls. None pay you any attention, however.",
                 "Walking around the %s, you see nothing special. A waste of time."]

    if MC.get_alignment() == "good":

        $ choices.append("You walk among the good people of the %s. Everyone looks friendly on such a beautiful day.")

    elif MC.get_alignment() == "neutral":

        $ choices.append("Watching people come and go through the %s, you wonder how you could profit from their endeavors.")

    elif MC.get_alignment() == "evil":

        $ choices.append("The people of the %s are a wretched and vicious bunch, just like anywhere else. Elbowing your way through this crowd of losers, you despise them all.")

    if MC.god == "Shalia":

        $ choices.append("In the nooks and shadows of the %s, you see discreet but unmistakable signs of Shalia worship. You nod approvingly.")

    elif MC.god == "Arios":

        $ choices.append("Looking at a group of pilgrims crossing the %s, you see some flamboyant, outspoken worshippers of Arios, wearing their faith on their sleeves. Others are more humble, and follow the idols in silent prayer. You wonder which ones are the true faithful.")

    else:

        $ choices.append("All sorts of religious nuts are travelling through the %s with feverish eyes, claiming to do the bidding of one god or another. 'Spice of the people', you tell yourself, shaking your head in disbelief.")

    $ text1 = rand_choice(choices) % loc

    "[text1]"

    return


label city_gossip(gossip=None):

    $ norollback()

    $ loc = selected_location.name.lower()

    $ text1 = rand_choice(("一些有趣的八卦", "令人不安的谣言", "一个令人好奇的故事", "一个有趣的传说", "一句人生格言"),)

    $ actor = article(__(selected_district.get_rand_pop().get_rand_name()))

    "On your way through the [loc], you overhear [text1] from [actor]."

    if not gossip:
        $ gossip = get_gossip()

    passerby "[gossip]"

    return

label city_luck():

    $ gain = (29 + dice(selected_district.rank*71)) * brothel.get_effect("boost", "city rewards")

    $ loc = selected_location.name.lower()

    "Strolling around the [loc], you notice something shiny on the ground."

    you "What's this... Oh! It's a purse of gold! Nice!"

    play sound s_gold
    $ MC.gold += gain
    "You have received %(gain)d gold."

    if dice(6) == 6:
        $ npc = rand_choice(["男人", "女人", "少年", "少女", "老头", "老太太"])
        npc "Oh no... Where is it? It must be around here..."

        "Someone seems to be looking for their lost belongings."

        npc "Mister, can you help me? I lost my purse... I really need it..."

        menu:
            "What do you do?"

            "Keep the gold":

                $ MC.good -= 1

                you "Are you looking for a bag of gold? Maybe one containing, like, %(gain)d gold?"

                npc "Yes, Sir... Have you seen it anywhere?"

                you "Nope. Not at all. Tough luck, friend."

                npc "Aw..."

            "Give back the gold":

                $ MC.good += 1

                you "Oh, so it's yours... Here, I found this."

                $ MC.gold -= gain
                play sound s_gold
                "You gave back %(gain)d gold."

                npc "Oh, thank you! It's good to see that gentlemen still exist in this rotten city."

    return



## SPECIAL TAG CITY EVENTS

init python:
    def slave_beach_event_happens():
        # Beach events will trigger for resting girls only, maximum once every five days

        if not story_flags["last beach event"] or story_flags["last beach event"] <= calendar.time - 5:
            if [g for g in get_resting_girls() if g.get_pic("beach", "swimsuit", naked_filter=True, soft=True)]: # Checks if the girl has a beach picture
                return True
        return False


label slave_beach_event(): # Happens in Seafront, Beach, lakefront, waterfalls during summer or spring

    $ girl = rand_choice(get_resting_girls())

    if not girl:
        $ debug_notify("no girl available for beach event")
        return

    # Only girls with a suitable pic may trigger this event

    $ beach_pic = girl.get_pic("beach", "swimsuit", and_tags=["profile"], not_tags=["naked", "wet"], soft=True, strict=True)
    if not beach_pic:
        $ beach_pic = girl.get_pic("beach", "swimsuit", naked_filter=False, soft=True, strict=True)
        if not beach_pic:
            $ debug_notify("no beach pic available for beach event")
            return
    # Not naked since she's hanging in the beach with her swimsuit.
    # Shouldnt have wet tag since it can mess with the oil rub event.

    $ story_flags["last beach event"] = calendar.time

    $ dis = selected_district.name.lower()
    $ loc = selected_location.name.lower()

    scene black with fade
    show bg beach at top with dissolve

    "By the [loc] is a long stretch of white sand where the people of [dis] come to relax. As you pass by, you spot a familiar sight."

    show screen show_event(beach_pic, x=config.screen_width, y=int(config.screen_height*0.8))
    with dissolve

    call dialogue(girl, "beach intro", narrator_mode=True) from _call_dialogue_237

    "You remember that today is her day off."

    you "Hey, if it isn't [girl.name]. What's up?"

    call dialogue(girl, "beach meet MC") from _call_dialogue_238

    if MC.get_alignment() == "good":
        "You chat amiably with [girl.name] for a few minutes. She seems pleased."
        $ girl.change_mood(2)

    elif MC.get_alignment() == "neutral":
        "You talk with [girl.name] about odds and ends. She relaxes a little."
        $ girl.change_mood(1)

    elif MC.get_alignment() == "bad":
        "Frowning, you scold [girl.name] on principle for her careless attitude. She looks down."
        $ girl.change_mood(-1)

    "Looking at [girl.name], you notice that she looks really hot in her tight beach wear... This gives you a few ideas."

    you "Listen..."

    $ s1 = get_fix_weakness_symbol(girl, "oil")

    menu:
        extend ""

        "Would you like some tanning oil?[s1]":
            you "The sun is getting high, I wouldn't want you to get sunburnt. Let me help you..."

            $ result = False

            if girl.check_fix("oil") == "neg":
                girl.char "Oil? No!!!"

                "She recoils in horror. You wonder what happened."

                if girl.personality_unlock["oil"]:
                    "You remember she hates oil. Damn."
                else:
                    $ girl.test_fix("oil", unlock=True, feedback=True)

            elif girl.is_("very dom") and girl.love <= 10:
                girl.char "Yeah, no, I don't think so. I'll do it myself."
            elif girl.is_("very sub"):
                girl.char "Oh... O-Okay..."
                $ result = True
            elif girl.love <= 0 and girl.fear <= -girl.love:
                girl.char "Oh, you're right. But you don't need to worry about it, I'll do it myself."
            else:
                girl.char "Well, it's nice of you to suggest it. Please do."
                $ result = True

            if result:
                "She lays down on her back as you warm the oil between your hands. As you start rubbing it on her exposed skin, you feel some warmth in your pants."

                $ pic = girl.get_pic("wet", and_tags=["beach", "swimsuit"], not_tags=["cumshot"], soft=True)

                if pic:
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with dissolve

                girl.char "Thank you, Master, it's nice..."

                "Running your hands against her arms, back, then thighs, you turn the oiling into a veritable massage. She doesn't stop you."

                call dialogue(girl, "beach oiling") from _call_dialogue_239

                "You can feel her muscles relax under your experienced hands, as you inch closer to her erogenous parts. Perhaps you could push your luck further?"

                $ s1 = get_fix_weakness_symbol(girl, "groping her ass")
                $ s2 = get_fix_weakness_symbol(girl, "fondling her boobs")
                $ s3 = get_fix_weakness_symbol(girl, "fingering")

                menu:
                    extend ""

                    "Grope her ass[s1]":
                        $ fix = "groping her ass"

                    "Fondle her boobs[s2]":
                        $ fix = "fondling her boobs"

                    "Finger her[s3]":
                        $ fix = "fingering"

                    "Leave it at that":
                        $ fix = None

                if fix:
                    if girl.personality_unlock[fix] and girl.check_fix(fix) == "pos":
                        $ narrator("You remember [girl.name] likes %s, and decide to exploit her weakness." % fix_description[fix + " description"][:-1])
                    elif girl.personality_unlock[fix] and girl.check_fix(fix) == "neg":
                        $ narrator("You remember [girl.name] dislikes %s, but you decide to go for it anyway." % fix_description[fix + " description"][:-1])

                    if fix == "groping her ass":
                        "Pretending you're still massaging her, you bring your hands closer and closer to her buttocks. She says nothing, although you can feel some tension build up."

                        "After pouring more oil on her backside, you suddenly squeeze both of her ass cheeks, bringing her swimsuit upwards so it looks like a thong."

                        $ target = 75

                    elif fix == "fondling her boobs":
                        "As you massage her back, you untie her top, as if by accident. She doesn't react, although you can feel her tense up a little."

                        "Sliding your oily hands around her, you reach for her tits and softly rub her mounds, lightly brushing against her nipples."

                        $ target = 100

                    elif fix == "fingering":
                        "Spreading her legs apart under the guise of the massage, you rub the insides of her thighs, inching your way up. She doesn't resist, seemingly waiting to see where this goes next."

                        "Casually, you then push her swimsuit's crotch aside, sliding a couple of fingers inside her."

                        $ target = 150

                    you "Let me massage here too..."

                    $ attitude = girl.get_sex_attitude(fix=fix) + girl.get_love()

                    if attitude >= target:

                        $ pic = girl.get_pic("beach", "swimsuit", and_tags=fix_dict[fix].tag_list[0], not_tags=["cumshot", "sex", "anal", "group", "bisexual"], strict=True, hide_farm=True)
                        if not pic:
                            $ pic = girl.get_pic(fix_dict[fix].tag_list[0], "naked", not_tags=["sex", "anal", "group", "bisexual"], strict=True, hide_farm=True)
                        # revome the wet tag for 2 reason: (1). It doesnt matter, the "beach" tag should be specific enough. (2). A lot of beach event use "wet" as andtag so it make the pic show up if not tagging carefully.

                        if pic:
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                            with dissolve

                        "She breathes heavily and her eyes get glassy, but she doesn't stop you as you keep touching her."

                        play sound s_moans_quiet

                        call dialogue(girl, "beach accept oiling") from _call_dialogue_240

                        if fix == "groping her ass":
                            "Moving her swimsuit out of the way, you spread her buttcheeks and expose her gaping asshole. She gasps as you spit in it, using your saliva to continue the massage."

                        elif fix == "fondling her boobs":
                            "Sand gets on her exposed tits as you proceed to fondle them, playfully pinching her nipples. She moans harder every time you do it."

                        elif fix == "fingering":
                            "Her love juice starts pouring out as you pump two, then three fingers inside her. She arches her butt towards you, as if trying to invite your hand deeper inside her."

                        girl.char "Aaaah! [emo_heart]"

                        if girl.check_fix(fix) == "pos":
                            "She loves this and moans louder and louder, enjoying herself tremendously."
                            $ girl.change_love(1)
                            $ girl.change_mood(2)

                        elif girl.check_fix(fix) == "neg":
                            "She grits her teeth, weakly fighting your touch, confused by how it makes her feel."
                            $ girl.change_love(-1)
                            $ girl.change_mood(-2)

                        $ girl.test_fix(fix, unlock=True, feedback=True)

                        "Under the hot sun, she seems lost in the sensations that wash over her. The fact that other people may see you increases her arousal. She cannot get enough of this, and her breathing intensifies as you increase your pace."

                        $ s1 = get_fix_weakness_symbol(girl, "denied orgasm")

                        menu:
                            "Make her come":
                                $ pic = girl.get_pic("beach", "swimsuit", "wet", and_tags=["orgasm"] + fix_dict[fix].tag_list[0], not_tags=["cumshot", "sex", "anal", "group", "bisexual"], strict=True, hide_farm=True)
                                if not pic:
                                    $ pic = girl.get_pic(["orgasm"] + fix_dict[fix].tag_list[0], strict=True, not_tags=["sex", "anal", "group", "bisexual"], hide_farm=True)

                                "You can see she is enjoying herself too much, and decide it's time to bring this massage to a happy ending."

                                if pic:
                                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                                    with dissolve

                                with flash
                                girl.char "Aaah, ah, AAAAAH!!!"

                                with doubleflash

                                "Love juice squirts out of her pussy as you expertly drive her to orgasm. Her whole body shakes, then she falls over the beach towel like a ragdoll, spent."

                                $ stat1 = "libido"
                                $ stat2 = rand_choice(["obedience", "sensitivity"])

                            "Deny her orgasm[s1]":
                                $ pic = girl.get_pic("beach", "swimsuit", "wet", and_tags=["denied"], not_tags=["sex", "anal", "group", "bisexual"], strict=True, hide_farm=True)
                                if not pic:
                                    $ pic = girl.get_pic(["denied"], not_tags=["sex", "anal", "group", "bisexual"], strict=True, hide_farm=True)

                                if pic:
                                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                                    with dissolve

                                "She is almost about to cum, and you decide to stop here, to teach her a lesson."

                                girl.char "What? Is it over? But..."

                                if girl.check_fix("denied") == "pos":
                                    "Her face is flushed, and love juice drips down her thighs. It seems like she loves being pushed to the brink."
                                    $ girl.change_love(2)
                                    $ girl.change_mood(3)

                                elif girl.check_fix("denied") == "neg":
                                    "She is livid, and she looks like she's about to burst into tears. It looks like she hates being denied orgasm like that."
                                    $ girl.change_love(-2)
                                    $ girl.change_mood(-3)

                                $ girl.test_fix("denied", unlock=True, feedback=True)

                                $ stat1 = "sensitivity"
                                $ stat2 = rand_choice(["obedience", "libido"])

                        scene black with fade

                        you "That was fun..."

                        $ girl.change_stat(stat1, dice(3)+3)
                        $ girl.change_stat(stat2, dice(3))

                        "[girl.fullname]'s {b}[stat1]{/b} and {b}[stat2]{/b} have increased."

                    else:
                        play sound s_surprise
                        call dialogue(girl, "beach refuse oiling") from _call_dialogue_241

                        you "Damn..."

                        hide screen show_event
                        with dissolve
                        "Disappointed, you take your leave."

                else:
                    "Satisfied with your little massage session, you dry your hands and take your leave. As [girl.name] says goodbye, her face is flushed and she looks flustered. Her sensitivity has increased."

                    $ girl.change_stat("sensitivity", dice(3))

            else:
                hide screen show_event
                with dissolve
                "Disappointed, you take your leave."


        "Have sex with me":

            you "I'm feeling horny right now. Let's fuck."

            girl.char "What?!? Here?"

            $ result = False

            $ s1 = get_fix_weakness_symbol(girl, "public acts")

            menu:
                "Let's do it in plain sight[s1]":
                    you "Yes, here! I don't care who's watching... Let's do it!"

                    if girl.check_fix("public acts") == "neg" and girl.get_stat("obedience") <= 150:
                        with vpunch
                        call dialogue(girl, "beach refuse public sex") from _call_dialogue_242

                        "She pushes you away with surprising strength and runs off the beach."

                        $ girl.test_fix("public acts", True, True)

                    elif girl.check_fix("public acts") == "pos" and girl.get_stat("libido") > 75:
                        girl.char "In... In public? I mean... Sure..."

                        "Before she has a chance to change her mind, you push her down and get yourself ready."

                        $ result = "public"

                    elif girl.is_("lewd") and girl.get_stat("libido") > 150 or girl.get_stat("libido") > 200:
                        call dialogue(girl, "beach accept public sex") from _call_dialogue_243

                        $ result = "public"

                    else:
                        call dialogue(girl, "beach refuse public sex") from _call_dialogue_244

                        "She darts away from you, leaving you looking stupid with a useless boner."


                "Let's hide":
                    you "Let us hide behind some rocks..."

                    if girl.check_fix("public acts") != "neg" and girl.is_("lewd") and girl.get_stat("libido") > 150:
                        girl.char "What are you talking about? Who cares about people watching? Do me now!" with vpunch

                        "She pushes you down in the sand, almost ripping your pants off."

                        $ result = "public"

                    elif girl.check_fix("public acts") == "pos" and girl.get_stat("libido") > 75:
                        girl.char "Hiding? Why? It's all the same to me... Let's just stay here."

                        "Surprised but aroused by her request, you waste no time before moving on her."

                        $ result = "public"

                    elif girl.get_stat("obedience") + girl.get_stat("libido") + girl.get_love() + girl.get_fear() > 250:
                        call dialogue(girl, "beach accept sex") from _call_dialogue_245

                        "You take her hand and lead her behind a large boulder. As soon as you're hidden from the crowd, your hands are all over her."

                        $ result = True

                    else:
                        call dialogue(girl, "beach refuse sex") from _call_dialogue_246

                        "She turns away from you, blushing, hugging her knees and legs tightly pressed together. You know better than to make a scene here."

            $ and_tags = []

            if result == "public":
                $ girl.test_fix("public acts", True, True)
                $ and_tags = ["public"]

            if result:
                $ s1 = get_fix_weakness_symbol(girl, "oral")
                $ s2 = get_fix_weakness_symbol(girl, "titjobs")
                $ s3 = get_act_weakness_symbol(girl, "sex")

                menu:
                    "What will you have her do?"

                    "Suck your dick[s1]":
                        $ act = "service"
                        $ fix = "oral"

                        $ pic = girl.get_pic("oral", "service", and_tags=["beach"] + and_tags, not_tags=["cumshot", "group", "bisexual"], strict=True)
                        if not pic:
                            $ pic = girl.get_pic("oral", "service", and_tags=["swimsuit"] + and_tags, not_tags=["cumshot", "group", "bisexual"], strict=True)
                            if not pic:
                                $ pic = girl.get_pic("oral", "service", "naked", and_tags=["beach", "swimsuit"], not_tags=["cumshot", "group", "bisexual"], strict=True)
                                if not pic:
                                    $ pic = girl.get_pic("oral", "service", "naked", and_tags=["beach", "swimsuit"], not_tags=["group", "bisexual"])
                        #adding cumshot to not_tags so it wont break immersion, i guess :v

                        you "Open your mouth and look me in the eyes..."

                    "Give you a titjob[s2]":
                        $ act = "service"
                        $ fix = "titjobs"

                        $ pic = girl.get_pic("titjob", "service", and_tags=["beach"] + and_tags, not_tags=["cumshot", "group", "bisexual"], strict=True)
                        if not pic:
                            $ pic = girl.get_pic("titjob", "service", and_tags=["swimsuit"] + and_tags, not_tags=["cumshot", "group", "bisexual"], strict=True)
                            if not pic:
                                $ pic = girl.get_pic("titjob", "service", "naked", and_tags=["beach", "swimsuit"], not_tags=["cumshot", "group", "bisexual"], strict=True)
                                if not pic:
                                    $ pic = girl.get_pic("titjob", "service", "naked", and_tags=["beach", "swimsuit"], not_tags=["group", "bisexual"])

                        you "I've got my eyes on your titties for some time... Why don't you use them to pleasure me?"

                    "Have sex[s3]":
                        $ act = "sex"
                        $ fix = None

                        $ pic = girl.get_pic("sex", and_tags=["beach"] + and_tags, not_tags=["cumshot", "group", "bisexual"], strict=True)
                        if not pic:
                            $ pic = girl.get_pic("sex", and_tags=["swimsuit"] + and_tags, not_tags=["cumshot", "group", "bisexual"], strict=True)
                            if not pic:
                                $ pic = girl.get_pic("sex", "naked", and_tags=["beach", "swimsuit"], not_tags=["cumshot", "group", "bisexual"], strict=True)
                                if not pic:
                                    $ pic = girl.get_pic("sex", "naked", and_tags=["beach", "swimsuit"], not_tags=["group", "bisexual"])

                        you "Spread your legs, babe. We're going to have some fun!"

                        if pic:
                            if pic.has_tag("cowgirl"):
                                $ fix = "cowgirl"
                            elif pic.has_tag("doggy"):
                                $ fix = "doggy"
                            elif pic.has_tag("piledriver"):
                                $ fix = "piledriver"
                            elif pic.has_tag("spoon"):
                                $ fix = "spooning"


                if fix:
                    if girl.check_fix(fix) == "pos":
                        call dialogue(girl, "slave positive fixation accept") from _call_dialogue_247
                        $ girl.change_mood(2)
                        $ girl.change_love(1)

                    elif girl.check_fix(fix) == "neg":
                        call dialogue(girl, "slave negative fixation accept") from _call_dialogue_248
                        $ girl.change_mood(-2)
                        $ girl.change_love(-1)

                if pic:
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with dissolve

                if fix == "oral":
                    "Obeying your order, she kneels down and opens her mouth, sticking her tongue out. You hold her chin as you push your cock inside."

                elif fix == "titjobs":
                    "Not waiting for her final answer, you move her swimsuit out of the way and insert your cock between her tits."

                elif fix == "cowgirl":
                    "As you lay down on the sand, she moves on top of you and lowers herself on your dick."

                elif fix == "doggy":
                    "Pushing her on all fours, you move her swimsuit out of the way and place your cock at the entrance of her pussy."

                elif fix == "piledriver":
                    "Holding her ankles, you push her back in the sand and spread her legs. Your cock quickly finds the entrance of her womb, shoving aside her swimsuit."

                elif fix == "spooning":
                    "Holding her from behind, you drag her panties down and push your cock inside her."

                elif act == "sex":
                    "Falling down on top of her, you furiously get rid of her thin swimsuit. She moans as you enter her."

                play sound s_ahaa

                girl.char "Ahaaa!"

                if act == "sex":
                    if girl.pop_virginity("MC"):
                        "You feel some resistance inside, and then something tears. A trickle of blood running down your shaft confirms that she is no longer a virgin."

                if fix:
                    $ girl.test_fix(fix, True, True)

                if act == "service":
                    play sound s_sucking
                else:
                    play sound s_moans

                if result == "public":
                    "A crowd quickly gathers. [girl.name] blushes but makes no effort to stop you."

                    passerby "Look at 'em go! I wish I had a recording crystal..."

                $ fix = None
                if act == "service":
                    "You mercilessly use her for your own pleasure, coming and going until you feel close to bursting."

                    you "Here it comes... Get ready!"

                    girl.char "Nggh!"

                    $ pic = girl.get_pic("beach", "swimsuit", and_tags=["cumshot"] + and_tags, not_tags=["sex", "anal", "fetish", "group", "bisexual"], strict=True, hide_farm=True)
                    if not pic:
                        $ pic = girl.get_pic("beach", "swimsuit", and_tags=["cumshot"], not_tags=["sex", "anal", "fetish", "group", "bisexual"], strict=True, hide_farm=True)
                        if not pic:
                            $ pic = girl.get_pic("beach", "swimsuit", "service", "naked", and_tags=["cumshot"], not_tags=["sex", "anal", "fetish", "group", "bisexual"], strict=True, hide_farm=True)

                    if pic:
                        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                        with flash

                        if pic.has_tag("cim"):
                            $ fix = "cum in mouth"

                            "Grabbing her hair, you push your cock deep inside her mouth before releasing a geyser of cum."

                            with doubleflash

                            girl.char "Ngggh!!! *cough* *cough*"

                            with flash

                            "She chokes on your cock and starts spitting cum all over her body and swimsuit."

                            girl.char "So rough... Aaah..."

                        elif pic.has_tag("cof"):
                            $ fix = "cum on face"

                            "Lifting her chin, you look straight into her eyes as you bring yourself over the limit, exploding all over her face."

                            with doubleflash

                            girl.char "Aah!"

                            with flash

                            "Sticky white cum drips down her face as you make sure to wipe the last drops on her forehead. She looks dazed."

                            girl.char "So... Much... Semen..."

                        elif pic.has_tag("cih"):
                            $ fix = "cum in hair"

                            "Wrapping your dick inside a lock of her hair, you rub against her silky soft curls until you are ready to cum."

                            with doubleflash

                            girl.char "Hey!!!"

                            with flash

                            "Thick white cum bursts out of your cock, and you leisurely spread it all over her soft hair, until it is completely soaked."

                            girl.char "It will take hours to wash it away... Aw..."

                        elif pic.has_tag("cob"):
                            $ fix = "cum on body"

                            "Aiming your dick at her tits, you instruct her to squeeze them tight together before exploding all over her."

                            with doubleflash

                            girl.char "Mmmh..."

                            with flash

                            "She looks at her soiled mounds strangely, absent-mindedly rubbing them together as the cum runs down her chest."

                            girl.char "There's cum all over my swimsuit... And I've got no other clothes to wear! Aw..."

                    if not pic or not fix:
                        "You cum hard all over her, covering her with sticky semen."

                        with doubleflash

                        girl.char "Ooh..."

                        girl.char "My swimsuit is ruined... And I have no spare clothes!"

                        you "Oh well, too bad..."

                    $ girl.change_stat("service", dice(3)+1)

                    $ girl.test_fix(fix, True, True)

                    "[girl.fullname]'s {b}service{/b} skill has increased."


                elif act == "sex":
                    "You fuck her with abandon, and she moans louder and louder with every thrust."

                    girl.char "Aah, aaah, aaaaaah!!!"

                    "You feel close to your limit and decide not to delay the inevitable any longer."

                    you "Take this!"

                    girl.char "AAAAAAH!"

                    $ pic = girl.get_pic("beach", "swimsuit", and_tags=["cumshot", "sex"] + and_tags, not_tags=["service", "anal", "fetish", "group", "bisexual"], strict=True, hide_farm=True)
                    if not pic:
                        $ pic = girl.get_pic("beach", "swimsuit", and_tags=["cumshot", "sex"], not_tags=["service", "anal", "fetish", "group", "bisexual"], strict=True, hide_farm=True)
                        if not pic:
                            $ pic = girl.get_pic("beach", "swimsuit", "sex", "naked", and_tags=["cumshot"], not_tags=["anal", "group", "bisexual"], strict=True, hide_farm=True)

                    if pic:
                        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                        with flash

                    if pic:
                        if pic.has_tag("cin"):
                            $ fix = "cum inside"

                            "Ramming your cock deeper inside her, you release a huge wad of cum as you hit her cervix. Her body arches back as she takes it all in."

                            with doubleflash

                            girl.char "Aaaaah!!!"

                            play sound s_orgasm

                            with flash

                            "She clings to you as your throbbing cock keeps pumping hot semen inside her."

                            girl.char "You came inside... Aaah..."

                        elif pic.has_tag("creampie"):
                            $ fix = "creampie"

                            "You withdraw as you feel about to cum, spurting white semen all over her gaping pussy."

                            with doubleflash

                            play sound s_aah

                            girl.char "Aaaaah!!!"

                            with flash

                            "She watches in a daze as hot cum flows out of her pussy."

                            play sound s_mmh

                            girl.char "I'm so dirty... Mmmh..."

                        elif pic.has_tag("cob"):
                            $ fix = "cum on body"

                            "Popping your cock out of her, you explode all over her smooth belly."

                            with doubleflash

                            girl.char "Hey!"

                            with flash

                            "More cum spurts out, smearing her body and swimsuit."

                            girl.char "My swimsuit is all sticky now... Aw..."

                    $ girl.change_stat("sex", dice(3)+1)

                    if fix:
                        $ girl.test_fix(fix, True, True)

                    "[girl.fullname]'s {b}sex{/b} skill has increased."

            else:
                "Disappointed, you go back to your other business."

        "Get ready to serve some customers":
            $ MC.good -= 1
            you "Well, I hope you enjoyed your time off - because it's over now."

            girl.char "Uh? What do you mean?"

            you "I mean, I can't let such a nice piece of booty go to waste even for a day. You look damn sexy in your swimsuit, and I'm sure customers are ready to pay some good money to use you right now!"

            if girl.is_("dom"):
                $ target = 300
            elif girl.is_("sub"):
                $ target = 150

            call dialogue(girl, "beach whoring request") from _call_dialogue_249

            menu:
                "Pay double her upkeep":
                    $ upk = round_int(girl.upkeep * girl.get_effect("boost", "total upkeep") * 2)
                    $ MC.good += 0.5
                    you "Listen, I'll give you... double your regular upkeep. How does that sound?"

                    girl.char "Double the money, uh..."

                    if girl.is_("materialist"): # Materialist girls are more swayed by money
                        $ target -= 75
                    else:
                        $ target -= 25

                "Pay her regular upkeep":
                    $ upk = round_int(girl.upkeep * girl.get_effect("boost", "total upkeep"))
                    $ MC.neutral += 1
                    you "I'll pay your normal upkeep, of course. It's only fair..."

                    girl.char "..."

                "Don't pay her":
                    $ upk = 0
                    $ MC.evil += 1
                    you "I own you, so why should I care about your opinion? Get your ass to work!"

                    girl.char "Hey! That's not fair..."

                    if girl.is_("materialist"):
                        $ target += 25
                    else:
                        $ target += 75 # Idealist girls are more outraged by unfairness

            if girl.remembers("punish", "disobey"):
                $ target -= 20 * girl.remembers("punish", "disobey")

            if girl.get_stat("obedience") + girl.get_stat("libido") + girl.get_fear() > target:
                call dialogue(girl, "beach whoring accept") from _call_dialogue_250
            else:
                $ girl.change_love(-2)
                call dialogue(girl, "beach whoring refuse") from _call_dialogue_251

                $ girl.track_event("disobey", "beach whore")

                hide screen show_event
                with fade

                "She leaves with her head held up high before you have a chance to object."

                return

            you "Good. Let me get things set-up..."

            hide screen show_event
            with fade

            you "Hear hear!"

            you "Ladies and Gentlemen, I mean, mostly you Gentlemen, why don't you come and sample one of the best produce of [brothel.name], brought to you right here at the [loc]?"

            you "Lovely miss [girl.fullname] is waiting for you here, ready to serve at your whim..."

            $ pic = girl.get_pic("beach", "swimsuit", and_tags=["libido"], soft=True)

            if pic:
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                with dissolve

            girl.char "Who wants to try me? Come forward, don't be shy!"

            "Dude" "Sweet! I want her to suck my dick... Is it cool?"

            man "No, dude! I want to bang her!"

            passerby "Not fair! I wanted to fuck her ass..."

            $ s1 = get_act_weakness_symbol(girl, "service")
            $ s2 = get_act_weakness_symbol(girl, "sex")
            $ s3 = get_act_weakness_symbol(girl, "anal")
            $ s4 = get_act_weakness_symbol(girl, "group")

            menu:
                "Choose what [girl.name] will do."

                "Service[s1]":
                    $ act = "service"
                    you "You there, get yourself ready. [girl.name] will take good care of you..."

                "Sex[s2]":
                    $ act = "sex"
                    you "One of you lucky bastards can get laid today... You! Step forward."

                "Anal sex[s3]":
                    $ act = "anal"
                    you "Did someone say 'anal sex'? You've come to the right place!"

                "Group sex[s4]":
                    $ act = "group"
                    you "Chill, guys, there's no need to fight: [girl.fullname] will serve all of you today!"

            if girl.obedience_check(act):
                if act == "service":
                    "[girl.name] kneels in front of the man, lowering his trunks. His erect shaft pops out, almost hitting her in the face."
                    "Dude" "Oh, this is my lucky day..."

                elif act == "sex":
                    "The customer moves on [girl.name]. She moans softly as his hands reach inside her swimsuit and fondle her privates."
                    man "Come on, babe! Let's fuck..."

                elif act == "anal":
                    "Grinning from ear to ear, the customer grabs her butt and bends her forward, pushing his hard cock against her butthole."

                    passerby "Let me just move this swimsuit out of the way... Nice."

                elif act == "group":
                    "The customers" "Hurray!!!"

                    "The three men eagerly jump on [girl.name], and she squeals as they start grabbing and rubbing her private parts."

                $ not_tags = opposite_sex_acts[act] + ["cumshot"]

                $ pic = girl.get_pic("beach", "swimsuit", act, and_tags=[act], not_tags=not_tags, hide_farm=True)

                if pic:
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with dissolve

                if act == "service":
                    play sound s_sucking
                else:
                    play sound s_moans

                girl.char "Aaaaah!"

                $ base_tip_change = 0

                if act == "service":
                    if pic.has_tag("oral"):
                        "[girl.name] uses her mouth to pleasure the customer, taking her time to bring him to a perfect climax."
                    elif pic.has_tag("handjob"):
                        "[girl.name] uses her hands to pleasure the customer, taking her time to bring him to a perfect climax."
                    elif pic.has_tag("titjob"):
                        "[girl.name] uses her tits to pleasure the customer, taking her time to bring him to a perfect climax."
                    elif pic.has_tag("mast"):
                        "[girl.name] masturbates in front of the customer, looking him in the eye as he brings himself off."
                    else:
                        "[girl.name] uses her mouth and hands to pleasure the customer, taking her time to bring him to a perfect climax."

                    "Dude" "Oh, man... I will not stand... this aggression... Man..."

                elif act == "sex":
                    "The man starts fucking [girl.name] wildly and she does her best to give him a good time."

                    if girl.pop_virginity():
                        "She yelps with pain as he enters her, forcing her hymen open. She is no longer a virgin."
                        $ base_tip_change = 100

                    man "Oh, yes! I'm on fire..."

                elif act == "anal":
                    "The guy fucks [girl.name]'s ass with abandon, spitting inside her crack to lubricate. She takes it all in stride."

                    passerby "Oh, I can go all the way in... I'm balls deep... This is the best!"

                elif act == "group":
                    if pic.has_tag("sex"):
                        "The men fuck her eagerly, and she does her best to make sure all of them are having fun."

                        if girl.pop_virginity():
                            man "Oh, man, look at that! She was a virgin, hahaha..."

                            passerby "Unbelievable!"

                            $ base_tip_change = 100

                    elif pic.has_tag("anal"):
                        "One of the men decides to fuck her ass while she uses the rest of her body to pleasure the others."
                    else:
                        "She uses her whore body and her skills to the max to help the customers reach climax."

                    "Dude" "Awesome..."

                    man "This is too good.."

                    passerby "That brothel guy wasn't joking... I've never had so much fun!"

                play sound s_mmmh

                girl.char "Hmm... Oooh..."

                $ pic = girl.get_pic("beach", "swimsuit", and_tags=[act, "cumshot"], not_tags=not_tags, strict=True, hide_farm=True)

                if not pic:
                    $ pic = girl.get_pic("beach", "swimsuit", act, and_tags="cumshot", not_tags=not_tags, strict=True, hide_farm=True)

                if act == "group":
                    $ cust = "men"
                    $ ending = ""
                    "After having their way with her, the group looks like they're about to cum already."
                else:
                    $ cust = "man"
                    $ ending = "s"
                    "After a while, the man looks like he's about to reach his limit."

                if pic:
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with flash

                    play sound s_surprise

                    if pic.has_tag("cof"):
                        "The [cust] decide[ending] to unload all over her face. She gives out a squeal as she receives it."

                        $ girl.test_fix("cum on face", True, True)

                    elif pic.has_tag("cim"):
                        "The [cust] want[ending] to cum in her mouth, and she complies. Doing her best not to gag, she swallows a flow of smelly cum."

                        $ girl.test_fix("swallowing", True, True)

                    elif pic.has_tag("cih"):
                        "The [cust] end[ending] up jerking off in her hair, covering it with sticky cum."

                        $ girl.test_fix("cum in hair", True, True)

                    elif pic.has_tag("buk"):
                        "The [cust] get[ending] ready to cover her face and hair with cum, and she squeals as it shoots all over her face."

                        $ girl.test_fix("bukkake", True, True)

                    elif pic.has_tag("cob"):
                        "The [cust] cum[ending] all over her body and swimsuit, until she is covered with sticky semen."

                        $ girl.test_fix("cum on body", True, True)

                    elif pic.has_tag("cin"):
                        "The [cust] want[ending] to cum inside, and she moans as her pussy fills up to the brim with hot white semen."

                        $ girl.test_fix("cum inside", True, True)

                    elif pic.has_tag("creampie"):
                        "It's creampie time! The [cust] jerk[ending] off and cum[ending] all over her gaping hole."

                        $ girl.test_fix("creampie", True, True)

                    else:
                        "Overwhelmed, the [cust] cannot endure anymore and cums hard."

                with doubleflash

                "While they were going at it, a line of would-be customers has formed by your improvised stall."

                hide screen show_event
                scene black
                with fade

                python:
                    nb = max(1, girl.get_max_cust_served("whore") + dice(3)-2)

                    if act == "group":
                        act = "sex"
                        nb += 2
                        tip = girl.get_tip(act, "good", [Customer(selected_district.get_rand_pop()), Customer(selected_district.get_rand_pop())], base_tip_change)[0]
                        en = 10 # Energy loss is more generous for that event
                    else:
                        nb += 1
                        tip = girl.get_tip(act, "good", [Customer(selected_district.get_rand_pop())], base_tip_change)[0]
                        en = 5 # Energy loss is more generous for that event

                "She ends up serving a total of [nb] customers."

                python:
                    for i in range(nb):
                        tip += girl.get_tip(act, "average", [Customer(selected_district.get_rand_pop())])[0]
                        en += 5

                $ MC.gold += tip - upk

                play sound s_gold

                if upk:
                    "The customers brought in [tip] gold. You gave [girl.name] [upk] gold for upkeep."
                else:
                    "The customers brought in [tip] gold. It was all profit, since you deprived [girl.name] of her rightful upkeep."

                $ text1 = girl.tire(en)[0]

                if text1:
                    $ narrator(text1)

            else:
                girl.char "What? No, I'm not going to do that with this guy!"

                menu:
                    "How dare you!":
                        $ MC.rand_say(("我是你的主人。你必须服从我的命令！", "照我说的做! 这是我最后一次警告你了!!!",
                            "ev: 把嘴闭上, 臭婊子。规矩是我定的!", "gd: 我已经没有多少耐心陪你浪费时间了，这次你逃不掉了。"))

                        call fight_attempt(girl, act, 2, outside=True) from _call_fight_attempt_21

                        if _return:
                            you "Damn you! Just you wait until I catch you again..."
                        else:
                            you "Hmph, you're not even worth the trouble... You'd better do what I tell you next time!"

                            "You realize she is in no shape to serve customers now. Frustrated, you tell her to pack her things and go back to the brothel."

                            $ girl.change_stat("obedience", 2)

                    "Give up":
                        $ MC.rand_say(("好吧....就照你说的做。", "真不敢相信，现在的奴隶....好吧！", "ne: 哼，这一次我放过你。你欠我一个人情。",
                                        "gd: 好吧，我不会强迫你做你讨厌的事情。", "ev: 他妈的，这一次我就放过你....但不要考验我的耐心。"))

                        $ girl.change_stat("obedience", -1)
                        $ brothel.change_rep(-20*game.chapter)

                        "Let down, the men scatter and grumble something about false advertising... Your brothel has lost reputation."

                        return

        "Nothing (Leave)":
            you "All right, I'll see you at [brothel.name]."

    hide screen show_event
    with dissolve
    return

#### END OF CITY EVENTS ####
