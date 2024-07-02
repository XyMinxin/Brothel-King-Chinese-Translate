#### CHAPTER 2 STORY EVENTS ####

## SEWER GIRL ##

label c2_sewer_girl_returns(): # Happens after Chapter 2 if Sewers girl was protected. Sets up the event to happen in 10 days.

    $ calendar.set_alarm(calendar.time+6, StoryEvent(label = "sewer_girl_returns", type = "morning"))

    return

label sewer_girl_returns(): # Morning event

    stop music fadeout 3.0

    scene black with fade

    $ renpy.show_screen("show_img", brothel.pic, _layer = "master")
    with dissolve

    play sound s_knocks

    "As you get on with your morning routine, the brothel receives an unexpected visitor."

    show sewer_woman dressed with dissolve

    sewer_woman "I wonder... Is this the right address?"

    sewer_woman "Oh! It's you."

    "A serious-looking woman in a uniform is standing at your door. She looks somewhat familiar."

    you "Uh, hello... Do I know you from somewhere?"

    play sound s_sigh

    sewer_woman "Oh, you don't remember... We met under very different circumstances..."

    scene black with pixellate
    show bg cell at top with dissolve

    play sound s_scream

    show sewer_woman naked at right with dissolve

    sewer_woman "Ngggh!"

    show sewer_rapist at left with dissolve

    man "Bwahahahaha! What are you trying to say, you stupid bitch? I thought we told you to be quiet!"

    sewer_woman "Mmmmmngh!"

    play sound s_scream_loud

    scene black with pixellate
    $ renpy.show_screen("show_img", brothel.pic, _layer = "master")
    with dissolve

    you "The sewers!"

    show sewer_woman dressed with dissolve

    sewer_woman "Yes. You found me in such an embarrassing situation... *blush*"

    sewer_woman "And you saved me... You saved me from a horrible fate."

    sewer_woman "I owe you a debt of gratitude."

    if MC.get_alignment() == "evil":
        you "Humph. I hope it was worth the trouble."
    elif MC.get_alignment() == "neutral":
        you "I did, didn't I... Do I get a reward?"
    else:
        you "Please, don't mention it."

    sewer_woman "Actually, I came here to repay my debt."

    sewer_woman "I work for the biggest shipping company in the harbor. I am doing well now, but I have you to thank for that."

    sewer_woman "I could give you some money for your trouble."

    sewer_woman "Or, if you prefer, I could put in a few words for you with my employers. They draw a lot of water in this town... Literally, and figuratively."

    sewer_woman "What will it be?"

    $ diff = MC.challenges["rally"].estimate_diff(8)
    $ can_roll = True

label sewer_girl_returns_menu():

    menu:
        extend ""

        "I want the money":

            $ renpy.block_rollback()

            sewer_woman "All right, here is my pay for the month. You deserve it."

            play sound s_gold

            $ MC.gold += 750

            "You have received 750 gold."

        "I want the influence":

            $ renpy.block_rollback()

            sewer_woman "I'll put in a good word for you. The people I work for have good connections throughout the city."

            $ MC.prestige += 12

            "You have earned a lot of prestige."

        "I want both (Charisma test: [diff])" if can_roll:

            $ renpy.block_rollback()

            you "Money or influence? Why not both?"

            sewer_woman "Both? You're greedy..."

            you "Come on. I saved your life, didn't I?"

            call challenge("rally", 5) from _call_challenge_1
            $ r = _return

            if r:
                play sound s_sigh

                sewer_woman "All right, you got me... After what you did, I cannot deny you a fair reward."

                play sound s_gold

                $ MC.gold += 500
                $ MC.prestige += 8

                "You have received 500 gold. You have earned a good amount of prestige."

            else:
                play sound s_laugh

                sewer_woman "Aw, come on, I'm a business woman too, you know. I'm not that soft."

                sewer_woman "A deal is a deal, you must make a choice. What will it be?"

                jump sewer_girl_returns_menu


        "I want something more 'intimate'":

            $ renpy.block_rollback()

            you "Well, you know... I had something more intimate in mind for a reward..."

            play sound s_surprise

            sewer_woman "You mean... Oh."

            sewer_woman "How bold of you... *blush*"

            you "Come on, babe. I saw you naked once. It had to give me some ideas..."

            "She frowns and pauses, thinking for a moment."

            sewer_woman "It's true that if you hadn't rescued me, I would be reduced to a life of rape and torture..."

            play sound s_sigh

            sewer_woman "I guess I could have sex with you once, considering."

            sewer_woman "It helps that you're my type."

            you "See, I knew we could find some common ground here..."

            sewer_woman "But let's make it quick. I am expected at the docks soon for an important meeting."

            you "Sure thing! Quick is my specialty..."

            you "Err... Wait. That came out wrong."

            scene black with fade
            show bg sewer_girl_sex1 at top with dissolve

            play sound s_aah

            sewer_woman "Ah, aah, aaaaaaah!!!"

            play sound s_moans

            sewer_woman "You're too big... Aaaaah..." with hpunch

            "Your hard cock hits deep inside her wet pussy as she holds on for dear life."

            you "That pussy is amazing... I feel like I really picked the right reward!"

            sewer_woman "Aaah, aaaaaaah, nghhhh..." with hpunch

            sewer_woman "You're ravaging me... Aaaaah..."

            "She moans wildly as your cock makes wet noises pounding her hungry cunt."

            you "I'm getting close..."

            sewer_woman "Aaah! No... Don't... Don't cum inside..."

            "Instead of answering, you fuck her even harder, hitting her womb as you drive your dick deeper and deeper inside her."

            sewer_woman "No, aaaah!!! You brute... Don't... Don't make me pregnant..." with hpunch

            sewer_woman "It's too much..." with hpunch

            with flash

            play sound s_scream_loud

            sewer_woman "AAAAAAAAH!!!!"

            with doubleflash

            play sound s_orgasm

            show bg sewer_girl_sex2 at top with dissolve

            "Pulling out at the last moment, you shoot your load all over her tits and face."

            sewer_woman "Aaaah... Oooh..." with flash

            show bg sewer_girl_sex3 at top with dissolve

            sewer_woman "The fuck..."

            sewer_woman "You made me all dirty... You came all over my glasses!" with vpunch

            you "Well, you're the one who asked me to pull out."

            sewer_woman "Aw... I'm all dirty now... I need to clean up..."

            you "Don't worry. Sill will wash your clothes."

            you "Sill! Come over here."

            sewer_woman "B-But... What will I do without my clothes?"

            you "Well, you can hardly go to your important meeting naked... Let's go for round two while you're waiting!"

            play sound s_surprise

            sewer_woman "R-round two? Wait!"

            scene black with fade

            play sound s_screams

            $ unlock_achievement("h sewer")

            "Hours later..."

            $ renpy.show_screen("show_img", brothel.pic, _layer = "master")
            with dissolve

            show sewer_woman dressed with dissolve

            play sound s_sigh

            sewer_woman "Well, I hope you're happy with your reward. I missed all of my appointments. *sigh*"

            you "Hehe, sorry... I kind of got carried away..."

            sewer_woman "Still... I guess I had a good time, and I've repaid my debt. Thank you."

            you "You could stay a little longer, you know..."

            sewer_woman "Sorry, I really have to go. After what happened last time, I swore never to walk the streets of Zan alone at night again."

            you "Yes, I can imagine."

            sewer_woman "Farewell, then. Now, we're even, but I won't forget what you did for me."

            you "Godspeed."

            $ MC.change_prestige(2)

    hide sewer_woman with dissolve

    you "Well..."

    you "My folks used to say, a good deed never goes to waste. Maybe that's true, after all."

    scene black with fade

    return


## INTRO ##

label c2_intro():

    play music m_zan fadein 3.0

    # SHOPS #

    $ calendar.set_alarm(calendar.time+2, Event(label = "c2_princess_letter"))
    $ game.set_task("Get started with your new brothel.", "story")

    scene black with fade
    show bg brothel1 at top with dissolve

    "It's a bright new day, and you are filled with optimism as you give one last look to the empty shell of your old brothel."

    "You start laughing as you remember the visit you got this morning."

    show bg brothel1 bw at top with flashbackin

    show kosmo bw with dissolve

    kosmo "Finally! It wasn't cheap, but I bought this joint from under you! You're out of business, now, pal!!!"

    you "Actually... I was the one who put the 'for sale' note. But thank you for buying, anyway."

    kosmo "So you finally admitted your worthlessness as a brothel owner, eh?"

    play sound s_maniacal_laugh

    kosmo "MUHAHAHA-"

    you "Not quite. I'm moving to a bigger place downtown. Things are looking up."

    kosmo angry bw "Whaat?!?" with vpunch

    you "Anyway, congrats on your new acquisition. I have to warn you, though, I think some vagrants slept in the place. Or maybe just used it as a toilet and moved on."

    play sound s_wscream

    kosmo "GROSS!!" with vpunch

    hide kosmo
    hide bg
    show bg brothel1 at top

    with flashbackout

    call auction_brothel() from _call_auction_brothel

    $ change_brothel()

    if debug_mode:
        menu:
            "Skip Chapter 2 intro?"

            "Yes":
                stop music fadeout 3.0
                return
            "No":
                pass

    you "We won't be missing that place! Especially the smell... Right, Sill?"

    sill sad "*pant*, *pant*..."

    you "Tired, already? We have some way to go, you know..."

    play sound s_surprise

    sill "But... Master... You make me carry all of our stuff..."

    "Sill can barely stand under the weight of a giant backpack filled with clothes, tools, silverware, carpets, supplies, and your personal collection of lead weights (only you think that's cool). The bag threatens to crush her with every step."

    you "Ah, Sill, it's just like you to always complain. Can't you just enjoy a stroll?"

    sill "Aaaw... *pant*"

    you "Let's see this place old man Gio found us. It better be an upgrade..."

    scene black
    show expression district.get_pic(config.screen_width, int(config.screen_height*0.8)) at top
    with fade

    "Not letting Sill's whining spoil your mood, you watch with satisfaction as you leave the slums behind and enter the bustling streets of Zan's popular neighborhoods, stepping into [district.name]."

    if district.name == "The Docks":
        "The sounds of waves crashing on the pier and seagulls shrieking echo everywhere. It's a pleasant change from the Slums, although you have a feeling it might get old quickly."

        "As with every city, the docks are next to the seedier parts of town. The plazas near the docks are packed with the wildest taverns in the city. Rowdy sailors and shady dealers pass you by, not paying any attention to you."

        you "Just the kind of place where a brothel will blend right in... I'm sure it will be a great location for [brothel.name]."

    elif district.name == "The Warehouse":
        "Workers, merchants and craftsmen mingle in the busiest neighbourhood of the city. Zan's main market is just a few streets away, the noise of a thousand people bartering echoing in your ears."

        "Every trade known to man is represented in the side streets near the market. In the distance, the grim outline of the city prison and the nearby gallows give you a chill."

        you "I'd rather not stray too close to there..."

    you "Look, Sill, I think this is the street Gio mentioned."

    scene black
    show expression bg_bro at top
    with fade

    you "This is it. It's, uh..."

    you "It's FANTASTIC!" with vpunch

    sill "Is it? *pant*"

    "Sill is crawling on all fours now, she cannot even gather the strength to look up."

    you "Look at this! There's a wall outside! And, uh... A moot!"

    sill "That's not, *pant*... A moot... *pant*. And the correct word is 'moat', anyway... *pant*"

    sill "I think it's... *pant*, a public urinal. Old houses have them, *pant*... sometimes."

    you "Silence. Do not bad-mouth my beautiful moot. Anyway, what are you still doing here? Drop the luggage quickly, and get to work."

    sill "Wh... What?"

    you "Do you think there's time to lie down here, lazying off? The customers will be here tonight."

    you "You need to clean this place thoroughly, starting {i}now{/i}!"

    sill "Aaw... Master... I'm going to die..."

    you "Yeah yeah, but clean the place first."

    "Shoving Sill and her bags inside, you decide to enjoy a little break from all your hard work and step outside to take a look at your new neighbourhood."

    scene black
    show bg street at top
    with fade

    you "The streets are so busy this time of day... Travellers from everywhere drop by [district.name]. This should be good for business..."

    play sound s_laugh

    "A young girl's laugh draws your attention away from the rowdy crowds. Looking up the street, you spot a group of women walking down the street."

    show gurigura at left with dissolve

    gurigura "Teehee! This is so fun! I've never seen a city like this."

    play sound s_sigh

    show katryn at right with dissolve

    katryn "My, my, Gurigura... You're such a bumpkin. This is just like any city..."

    $ gurigura_name = "Gurigura"

    hide gurigura
    hide katryn
    with dissolve

    show riche at left with dissolve

    play sound s_surprise

    show riche at left with dissolve

    riche "Come on, Katryn, don't be such a killjoy... This {i}is{/i} the largest city in Xeros! Isn't it amazing? Right, Ramias?"

    $ katryn_name = "Katryn"

    show ramias at right behind riche with dissolve

    ramias "..."

    riche "Ramias?"

    $ ramias_name = "Ramias"

    ramias "I sense danger, Riche. These streets are not safe. There are too many places to hide..."

    $ riche_name = "Riche"

    hide riche
    hide ramias
    with dissolve

    show gurigura at left
    show katryn at right
    with dissolve

    gurigura "Hiding is fun! Why don't we play hide and seek?"

    katryn "SHUT UP, you simpleton! We're here on business, remember?" with vpunch

    gurigura "Uh... Are we?"

    katryn "Yes, you dumb f..." with vpunch

    hide katryn
    hide gurigura
    with dissolve

    show ramias at right
    show riche at left
    with dissolve

    ramias "Calm down, Katryn. You're drawing attention to us."

    riche "Yes, Kat, calm down please... *embarrassed*"

    hide riche
    hide ramias
    with dissolve

    show gurigura at left
    show katryn at right
    with dissolve

    katryn "WHY ARE YOU ALL TAKING HER SIDE? I'm the genius here!!!" with vpunch

    gurigura "Ge-ni-us, ge-ni-usss... Teehee, that word sounds funny! Does it mean something?"

    katryn "Grrrr..."

    "As the women walk down the street, they pass in front of [brothel.name] and you ogle them a bit."

    hide katryn
    hide gurigura
    with dissolve

    menu:
        you "Mmmh..."

        "The younger girl is cute":
            $ NPC_gurigura.love += 1

            show gurigura at left with dissolve

            "You look at the young girl, Gurigura, and flash her a bright smile. She notices you and smiles back."

            gurigura "(This man looks friendly.)"

            gurigura "Hiii!" with vpunch

        "I like the bitchy one":
            $ NPC_katryn.love += 1

            show katryn with dissolve

            "You look at the haughty girl and notice that for all her arrogance, she is quite pretty."

            you "(I wonder what she looks like underneath those clothes...)"

            "Suddenly, she turns her head and looks straight at you with cold eyes. It's like she just read your thoughts. Frowning disapprovingly, she turns her head away."

            hide katryn with dissolve
            show gurigura at left with dissolve

        "The white-haired woman is hot":
            $ NPC_ramias.love += 1

            show ramias with dissolve
            "The warrior girl cuts a sexy figure with her skimpy clothing, which is as diminutive as the weapons on her back are huge."

            play sound s_boing
            show ramias:
                ease 0.5 zoom 5.0 xoffset -500 yoffset 1450
                pause 0.5
                ease 0.5 zoom 1.0 xoffset 0 yoffset 0

            "Her chest bounces up and down suggestively as she walks over the pavement. Noticing your eyes are on her, she stares back, assessing you as a potential threat."

            ramias "(Who's that [MC.playerclass]? What is he looking at?)"

            katryn "That dodgy guy is checking your boobs."

            ramias "Oh. That's a relief, I thought he was plotting a sneak attack."

            hide ramias with dissolve
            show gurigura at left with dissolve

        "That blonde girl looks sweet":
            $ NPC_riche.love += 1

            show riche with dissolve
            "The pretty blonde girl looks sweet and innocent. You wonder if this delicate flower has a naughty side, and soon your mind is filled with racy thoughts."

            riche "Uh?"

            "She notices you looking at her, and blushes bright red."

            riche "(A m-man is looking at me... Who is that?)"

            hide riche with dissolve
            show gurigura at left with dissolve

    gurigura "Look at this biiig house! Is it a shop of some kind?"

    show katryn at right with dissolve

    katryn "Don't look at that, you idiot! Can't you see it's a... a... *blush*"

    gurigura "A what?"

    hide katryn
    hide gurigura
    with dissolve

    show riche at left with dissolve

    riche "What is it, Katryn? Your face looks flushed."

    show ramias at right behind riche with dissolve

    ramias "I think she means this place is a brothel."

    riche "A brothel? You don't mean..."

    "The blonde girl blushes bright red."

    ramias "Yes, a brothel, a place where people come to meet and f..."

    play sound s_surprise

    hide riche
    hide ramias
    with dissolve

    show gurigura at left
    show katryn at right
    with dissolve

    katryn "OK, OK!!!" with vpunch

    katryn "We know what a brothel is..."

    gurigura "I don't! What's a brothel, Katryn?"

    katryn "Well, uh... It's a place for loose women... *blush*"

    gurigura "What did they lose? I don't understand..."

    katryn "OF COURSE YOU DON'T, YOU MORON! *mad*" with vpunch

    hide katryn
    hide gurigura
    with dissolve

    show ramias
    with dissolve

    ramias "Quiet, Katryn. Trouble is brewing."

    play sound s_punch

    with vpunch

    pause 0.3

    play sound2 s_crash

    man "Ouch!"

    thug3 "Watch it, punk."

    man "I'm so sorry, sir! I didn't see you coming..."

    "Coming from a side street, you see a group of a dozen or so thugs making their way, shoving passersby out of their way."

    thug3 "Stay down and grovel like a dog, if you know what's good for you."

    man "Forgive me sir... Forgive me..."

    "You sense trouble as the thugs pour into your street and find themselves face-to-face with the group of girls."

    thug3 "Look here boys! What do we have... A bunch of sweet babes, ready for our cocks... Today's going to be a good day!"

    ramias "We're just passing by. Move out of the way."

    ramias "Please."

    thug3 "Whoever said I'd let you go? I'm looking forward to getting acquainted with those juicy boobs of yours..."

    play sound s_boing
    show ramias:
        ease 0.5 zoom 5.0 xoffset -500 yoffset 1450
        pause 0.5
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    ramias "Another boob fan... I seem to attract a lot of these."

    show ramias at right with move
    show gurigura at left with dissolve

    gurigura "Ramias, who's that? Are they your friends?"

    thug3 "Wow... I didn't see they had a kid with them."

    play sound s_surprise

    gurigura "I am NOT a kid! I'm FIFTEEN!" with vpunch

    thug3 "Are you, really? Well, you're definitely old enough, then... Hehehe."

    gurigura "Old enough?"

    ramias "Forget it, Gurigura. Can you deal with this bunch or do you need my help?"

    gurigura "Deal with them? Are they bad guys?"

    ramias "Yes. More importantly, they're in our way."

    thug3 "Hey! Shut up, bitches! Don't talk like we're not even there!" with vpunch

    play sound s_sheath

    "The thug looks mad now. He draws out a mean looking knife."

    thug3 "Enough chit-chat. You're outnumbered, and..."

    show gurigura at jumping

    play sound s_sheath

    pause 0.1
    with vpunch

    play sound2 s_sheath

    pause 0.3

    play sound3 s_wscream
    with vpunch

    pause 0.2

    play sound s_wscream

    show gurigura_attack at top with dissolve

    gurigura "JAGUAR ATTAAAACK!!!"

    play sound s_sheath

    with vpunch

    pause 0.3

    play sound3 s_wscream

    thug3 "GWAAAAAH!!!"

    gurigura "Tadaaa!"

    "Faster than your eyes can follow, the small girl whirls and hits the thugs like a tornado, the sharp blades at the end of her goofy paws cutting them to shreds."

    "In only a matter of seconds, the men are lying dead or wounded at the girl's feet. She giggles like nothing happened."

    play sound s_laugh

    hide gurigura
    hide ramias
    hide gurigura_attack
    with dissolve

    show riche at left
    show katryn at right behind riche
    with dissolve

    riche "Thank you, Gurigura! These men were scary."

    katryn "Yeah, you're dumb as a lamppost, but it's a good thing you're on {i}our{/i} side. I mean, we could have easily handled this, but..."

    riche "Be nice, Kat. Gurigura has been a great help."

    katryn "Humph. Well, I suppose so. It was good for the four of us to travel together all the way from the front lines. But I guess it's time to separate, now..."

    hide riche
    with dissolve

    show gurigura at left
    with dissolve

    gurigura "Separate? Aren't we all staying in the city?"

    katryn "We are. But we should split. I have to find the great library, and resume my studies of the dark and forbidden secrets of my order..."

    gurigura "You mean... *shiver*"

    katryn "Yes. ENGINEERING." with vpunch

    gurigura "Sounds scary... I'm just going to stick around and open a toy shop."

    katryn "A... A toy shop?"

    play sound s_evil_laugh

    katryn "Oh, poor Gurigura, you really have porridge for brains!"

    katryn "How can you hope to sell {i}toys{/i} in such a corrupt city? Sex and lucre is what this city's built on!"

    gurigura "You're so mean, big sis'... I wanna open a toy shop... *tearful*"

    "Gurigura's eyes fill with tears, and Katryn quickly backs off."

    katryn "Okay, okay, fine! Open a toy shop if you want to waste your time and money!"

    katryn "I, on the other hand, will make a fortune thanks to my legendary business acumen. I am going to sell trinkets."

    katryn "My advanced robotic skills should allow me to mass-produce them without breaking a sweat."

    gurigura "What about you guys? What are you going to do?"

    hide katryn
    hide gurigura
    with dissolve

    show ramias at right
    show riche at left
    with dissolve

    riche "Well... You know I'm nobility, so whether I like it or not, I have to pay my respects to my extended family in town... It's going to take some time."

    ramias "As for me, I think I'll stick around the Docks for now. I've never been comfortable around the court."

    riche "How are you going to make a living, though, Ramias? There must be less opportunities for soldiers here than on the front line..."

    ramias "Well, hahaha... *sweat*"

    ramias "(Arios, it's true that I'm broke...)"

    ramias "I guess I have a good eye for weapons: I could always buy used ones and sell them to adventurers?"

    riche "That sounds like a great idea! Less dangerous, too..."

    ramias "Yes... That would be a nice change of pace."

    riche "It's settled, then. We separate here for today, but don't forget we're a team! Girls, let's meet again soon!"

    ramias "Yes. You have my word."

    hide riche
    hide ramias
    with dissolve

    show gurigura at left
    show katryn at right
    with dissolve

    gurigura "Sure thing! See you later, sisters!"

    katryn "Yeah, yeah. Take care."

    scene black with fade

    "The women split and leave in different directions. You wonder if you'll see them again."

    stop music fadeout 3.0

    return






## MAIN STORY LINE ##

label c2_princess_letter:

    scene black with fade
    show expression bg_bro at top
    with dissolve

    if MC.playerclass == "战士":
        $ activity = "your early weapon training"
    elif MC.playerclass == "法师":
        $ activity = "your usual meditation session"
    elif MC.playerclass == "奸商":
        $ activity = "the daily farmer's market"

    "Late in the morning, you come back to [brothel.name] from [activity] when you hear a sudden scream."

    play sound s_woman_scream

    sill sad "Eeek!" with vpunch

    play sound s_shatter

    $ room = brothel.get_random_room_pic_path()

    scene black with fade
    show expression room at top
    with dissolve

    show sill at right with dissolve

    sill "Master! Save me!!!"

    play music m_gio fadein 3.0

    show gio at left with dissolve

    gio "Come on, my dear, what's with the overreaction..."

    sill "He pinched my butt! Right as I was carrying the breakfast plates!"

    "A bunch of plates lie shattered on the floor. It looks like half your tableware is broken."

    menu:
        "Whose fault is this?"

        "Blame Sill":
            $ renpy.block_rollback()
            you "Sill!!! What the hell did you think you were doing!!!"

            $ NPC_sill.love -= 1
            $ NPC_gio.love += 1

            sill "B-But... He attacked me!"

            you "I don't care what he did! It could have been me pinching you butt, is that a good reason to drop our precious plates on the floor?"

            sill "B-But, Master... If it's you, it's not the same thing..."

            gio "Hmpf! How unfair!"

        "Blame Gio":
            $ renpy.block_rollback()
            you "Gio!!! What on earth are you doing here, assaulting my... Sill?!?"

            sill "Your... Sill? *blush*"

            gio "Aw, hold your horses, partner, I didn't know she was this clumsy..."

            $ NPC_sill.love += 1
            $ NPC_gio.love -= 1

        "Blame the gods":
            $ renpy.block_rollback()
            if MC.god:
                you "O, [MC.god]! Why do you mock me so!!! Why did you curse your humble servant with such lousy friends and clumsy slaves!!!" with vpunch
            else:
                you "O, cruel and heartless gods! Why do you mock me so!!! Did you have to punish my defiance by giving me lousy friends and clumsy slaves?!?" with vpunch

            gio "Lousy friends... Hey!" with vpunch

            sill "Clumsy slaves..."

            sill sad "Hey!" with vpunch

        "Blame no one in particular":
            $ renpy.block_rollback()
            you "Stop the blame game, you two."

            you "It's no one's fault that Gio is stupid and that Sill is clumsy."

            gio "..."

            sill sad "Er..."

            you "But breaking a plate inside the house is bad luck, you know... Or is it good luck?"

            gio "Good luck!" with vpunch

            sill "Bad luck!" with vpunch

            gio "Ah, wait, maybe it's the other way around... Unless it's the opposite?"

            sill "Uh... You have me confused now..."

    gio "Anyway. I don't see what the big fuss is all about..."

    gio "Now, look at you, man! You've got it made!"

    gio "A full-fledged brothel owner with a bona fide licence and an attitude."

    gio "You must be rolling in cash now, what's a few plates to you!"

    you "So... You're not going to pay for these, are you?"

    gio "Listen, friend, this conversation is getting really unpleasant."

    gio "I come here bearing good news. If anything, {i}you{/i} should be paying me!"

    you "I don't see that happening."

    gio "I have a letter for you. It's from the Princess..."

    you "The Princess?!?" with vpunch

    gio "Yes... But first, I was hoping to enjoy the hospitality of your establishment!"

    if gio_fucked_sill:
        gio "I'd like another roll in the hay with your snobbish little slave, here... I've missed her squealing."

    else:
        gio "I'd like to teach miss Wishy-Washy here a few manners..."

        if gio_fucked_sill == "":
            gio "You promised me I would sleep with her, remember?"

            you "My... My memory is a little fuzzy..."

    play sound s_surprise
    sill sad "Master!!! No!!!" with vpunch

    gio "Come on, [MC.name], make an old man happy... I'll even throw in some extra information if you do!"

    menu:
        "Do you let Gio have his fun?"

        "Let him have Sill":
            $ renpy.block_rollback()
            you "Fine... I've been too lenient with Sill recently."

            play sound s_surprise
            sill "!!!" with vpunch

            you "What better way to make her learn her place than have her fuck a man she loathes every once in a while?"

            $ MC.evil += 2
            $ NPC_sill.love -= 5
            $ NPC_gio.love += 5
            $ gio_fucked_sill = True
            $ girl = "Sill"

            gio "Fantastic!"

            play sound s_woman_scream
            sill "Noooo!!!"

            you "Shut up and follow Gio to one of the back rooms. I've got some reading to do."

            hide gio
            hide sill
            with dissolve

        "Let him have one of your slaves" if len(MC.girls) > 0:
            $ renpy.block_rollback()

            $ NPC_sill.love += 1
            $ NPC_gio.love += 2

            you "Nah, Sill is my private pet. But you can have another girl on the house. Happy?"

            "Gio grumbles, but he's too horny to pass on a free hooker."

            $ girl = long_menu("Choose which girl will entertain Gio", [(g.name, g) for g in MC.girls])
            $ girl2 = None

            you "[girl.name]! Come over here."

            girl.char "Yes, Master?"

            you "We have a distinguished guest. Make sure you make him feel welcome... You can take one of the bedrooms."

            girl.char "*blush* Yes, Master."

            hide gio with dissolve

            you "Now, let's see this letter."

        "Let him have several of your slaves at once" if len(MC.girls) > 1:
            $ renpy.block_rollback()

            $ NPC_sill.love += 1
            $ NPC_gio.love += 5

            you "I'm sure you'd agree that two is better than one... Why don't you leave Sill alone and let some of my girls work their magic?"

            gio "A... A threesome...? *sweat*"

            you "Sure. If your heart can take it..."

            gio "*sweat a lot*"

            gio "Well, uh..."

            gio "I accept your generous offer, my friend!"

            "He seems to have forgotten all about Sill."

            $ girl = long_menu("Choose which girl will entertain Gio (first girl)", [(g.name, g) for g in MC.girls])
            $ girl2 = long_menu("Choose which girl will entertain Gio (second girl)", [(g.name, g) for g in MC.girls if g != girl])

            you "[girl.name]! [girl2.name]! Come here, darlings."

            girl.char "Yes, Master [MC.name]?"

            girl2.char "You called?"

            you "I want you two to entertain my good friend Gio here..."

            you "Think of it as a part of your training."

            girl.char "..."

            girl2.char "Well... If you say so, Master."

            gio "(Oh, boy...) *sweats a ton*"

            hide gio with dissolve

            "Gio elopes with the girls in one of the back rooms, while you turn your attention back to the letter."


        "Turn him down":
            $ renpy.block_rollback()
            you "Sorry, Gio. I don't give out anything for free."

            gio "You're... MEAN!!!" with vpunch

            $ MC.rand_say(["gd: I don't think you're any of the girls' type, anyway. Sorry.", "ne: Boohoo. Cry me a river.", "ev: Damn right I'm mean! Now give me this letter before I show you just how bad I am."])

            $ NPC_gio.love -= 2
            $ girl = None

            "Gio looks dejected."

            gio "Fine! Way to treat an old friend. Here's your damn letter."

            gio "But I'm keeping my precious intel for myself."

            you "Yeah, yeah, whatever."

    if girl:
        play sound s_door_close

        "After a few moments, you start hearing moans coming from the bedroom. You ignore them and turn your attention to the letter."

        play sound2 s_moans_quiet

    you "Let's see what this letter is all about."

    play sound s_dress

    call screen letter(header = _("A Royal Invitation"),
                       message = __("Dear ") + MC.name + __(",\n\nI have heard from our common acquaintance that you have recently settled in Zan. It warms my heart to know that another upstanding citizen is taking root in our city.\nI am forever in your debt for the aid you provided in my hour of need. If you please, I should like to meet you again to discuss an urgent matter. My messenger can give you the details."),
                          signature = "Princess Kurohime")

    "You are awestruck for a moment."

    you "The Princess!"

    you "And I'm supposed to ask Gio about the details... Erm... Gio?"

    if girl:
        scene black with fade

        "Meanwhile..."

        if girl == "Sill":

            show bg giofuck8 at top with dissolve

            play sound s_moans_short

            gio "Hahahaha! How does my dick feel, little slut slave?"

            sill "Hgn..."

            gio "Not bad for an old man, is it?"

            gio "Wait... I feel it coming..."

            sill "No! Not inside! Plea..." with vpunch

            with flash

            gio "UWAAAH!!!"

            with doubleflash

            play sound s_scream_loud
            sill "EEEEK!!!" with vpunch

        elif girl2:
            show expression girl.get_pic("bisexual", always_stock=True).path at top
            with dissolve

            play sound s_moans

            girl.char "Oh, Mister, aah!!!" with vpunch

            play sound s_moans_short

            girl2.char "Oh, yes! Touch me right there!" with vpunch

            "Gio has fun with [girl.name] and [girl2.name] for over an hour."

        else:
            show expression girl.get_pic("sex", always_stock=True).path at top
            with dissolve

            play sound s_ahaa

            girl.char "Mister Gio!!! Aaaaah!!!"

            play sound s_moans_short

            if girl.pop_virginity():
                gio "A virgin! A-Amazing..."

                "Tears of joy well up in Gio's eyes."

                gio "That [MC.name]... He's a {b}real{/b} friend!!! *sniff*"

                $ NPC_gio.love += 5

            girl.char "Aah, ah, aaaaaah!!!" with vpunch

        scene black with fade

        "..."

        show expression room at top
        with dissolve

        "Gio comes back after a while, buckling his pants and grinning like an idiot."

        show gio with dissolve

        you "Scratched that itch yet? I want to hear what you've got to say."

    else:
        "Gio is turning away from you, smoking a cigar, still sulking."

        you "Come on, Gio. Don't make it difficult. I know the Princess rewarded you already."

        gio "Uh? How did you..." with vpunch

        gio "Hmpf. Sure, she gives me a modest stipend, but..."

        you "Details, Gio. Details."

    gio "Well... The Princess gave me this letter for you just yesterday."

    gio "I mentioned that you had just moved into the city, and she seemed to pay inordinate attention to such trivial information."

    you "She did?"

    gio "Yeah. I haven't got a clue what she sees in you, but you sure made an impression. She told me to bring you to the Palace."

    you "You mean... We will meet the Princess... At the Palace?"

    gio "Yes, of course, where else?"

    you "*gulp*"

    you "But... I'm not allowed in the upper quarters yet, let alone the Palace!"

    gio "Come on, not a problem, I'll escort you. I've got a letter of conduct that can get us in there."

    you "You do? Well... Where should we meet, then?"

    gio "Meet me by the stables next Saturday. It's in the Warehouse district. I will take you from there."

    if girl:
        you "All right... But you mentioned some juicy intel. What is it?"

        gio "Well..."

        gio "I can't be sure, but I have a hunch about what the Princess might want to talk about."

        you "What is it?"

        gio "There's been a stream of murders recently... High-ranking people. People close to the court."

        you "Oh..."

        gio "I'm not sure what's the Princess's angle on this. She's not heavily involved in politics."

        gio "But she's a subtle presence in court... Even though she is only a young woman and has little clout, I wouldn't be surprised if she had her own agenda."

        you "Okay... But how does that involve me?"

        gio "I can't say... Maybe she trusts you more than the snakes at court?"

        gio "She's certainly eager to escape her royal shackles."

        you "Hmm..."

    else:
        you "Anything else?"

        gio "Hmpf. Not for you, pal. *sulk*"

        you "*sigh*"

    scene black with fade

    stop music fadeout 3.0

    "You show Gio out before he gets a chance to ransack the kitchen."

    you "A meeting with the Princess of Zan, uh? When did I become so fancy..."

    $ story_add_event("c2_princess_visit1")
    $ game.set_task("Meet Gio at the stables on Saturday.")
    $ game.set_task("Advance through the story to unlock the next chapter.", "advance2")

    return


label c2_princess_visit1:

    call hide_everything() from _call_hide_everything_47

    scene black with fade
    show expression selected_location.get_pic(config.screen_width, int(config.screen_height*0.8)) at top
    with dissolve

    play music m_oriental fadein 3.0

    you "Gio said to meet him here on Saturday..."

    play sound s_whistle

    gio "Hey! [MC.name]!"

    you "There you are."

    gio "Let's hurry. Princess Kurohime is a busy lady."

    you "Right. I'll follow you."

    gio "We'll go through the docks to reach the closest gate to the higher city..."

    scene black with fade
    show bg exotic_emporium at top with dissolve

    "Gio explains Zan to you as you move deeper inside the city."

    gio "The Warehouse and the Docks quarters are in the lower city, where most of the laboring classes live. It's a notch above the shanty housing in the Slums, but not by much."

    "You reach the inner gates. After Gio shows the guards a document, they let you pass through, into the upper city."

    show bg hanging_gardens at top with fade

    you "Wow! What is this place?"

    gio "Behold... The hanging gardens of Zan, famous all over Xeros. They're tended to by the magic guild."

    gio "Crazy, crazy people, those mages. Stay away from the gardens if you value your sanity, my friend."

    show bg pilgrim_road at top with fade

    "You soon reach a major artery, cleaving through the city in a long, straight line."

    you "Wow... I've never seen so many people crammed in one place!"

    gio "This is Pilgrim's Road. It leads all the way to the Cathedra of Arios. And the Cathedra faces the Palace, as a matter of course."

    gio "Arios worshippers are so insecure about their faith, they need to constantly rub it into everyone's face..."

    $ MC.rand_say(["sh: Yeah, sounds like them all right... Tsk.", "ar: Watch it! I won't suffer insults to the name of Arios!", "ng: No separation of church and state, uh... How primitive."])

    gio "Anyway. That's why this road is known as Pilgrim's Road. It's still the fastest way to get to the Palace, if you don't mind bumping into the tourists."

    scene black with fade
    show bg castle at top with dissolve

    gio "Here we are! The Palace, at last."

    show knight with dissolve

    knight "Halt! Who goes there!"

    "A bulky knight bars the way. Gio shows him the letter of conduct."

    knight "..."

    knight "This letter of conduct is in order, but it only mentions one visitor: Sir [MC.name]."

    gio "I know, I know, but I'm a good friend of the princess, and..."

    "The knight towers above Gio, resting his hand on the pommel of his sword."

    knight "No one but Sir [MC.name] is allowed to enter the palace. Do I make myself clear?"

    "Gio stutters to answer, but quickly backs down, grumbling."

    knight "You can wait outside while I conduct this business with Sir [MC.name]. Just stand over there, by the lepers' shack."

    gio "The... What?"

    you "Just go, Gio..."

    gio "Grrr..."

    you "So, can I see the princess?"

    knight "I'm afraid audiences are over for today. The next ones will be on Monday."

    knight "The palace will send someone to get you. No need to bring your servant this time."

    you "He's not... Uh... Yeah, I won't bring the uncouth wretch along next time. No problem."

    knight "Good. If you don't have any other business..."

    you "Wait, I was wondering if I could take a look at the Palace? I came all the way... And I've never been here before."

    knight "(Damn tourists... *sigh*)"

    you "What was that?"

    knight "I, er... Well, certainly, Sir, but do not linger. I'll walk you around the palace's grounds."

    hide knight with dissolve

    show bg courtyard at top with fade

    "Walking a few steps behind the knight, you take in the view of the royal palace from the inside."

    "A magnificent courtyard separates several massive aisles, each one larger than a high-ranking noble's estate."

    knight "To the left are the King's private quarters; to the center are the public halls where he holds court."

    "Although the masonry is top-notch, you notice a clear difference in design and material between the foundations and the newer buildings above."

    show bg ruins at top with fade

    knight "The palace foundations date back to Cimeria, the non-human civilization that settled the location where Zan now stands. It is said the center of their city lay right here on the highest hill."

    knight "Because of this, some ignorant lowborns believe the Palace to be haunted. Nonsense and worthless superstition, of course."

    knight "Everyone knows a simple charm from the Cathedra soaked in priestess tears on a full moon can drive away evil spirits."

    knight "In the name of Arios, I can't fathom why the royal family kept such pagan ruins intact right under their palace. But the cowardly builders argued their chisels couldn't even dent the damn stones, so they got away with it."

    knight "But if you ask me, something broke the walls of their city in the first place... So this nonsense about it being 'indestructible' is just a wad of lies spread by the mason guild, as far as I'm concerned."

    knight "But forgive my rambling."

    show bg courtyard at top with fade

    "The knight leads you towards the right aisle, which has the most breathtaking view of the city, hanging right on top of the cliff overlooking Zan."

    knight "These are the Princess's quarters. It is guarded around the clock by her personal retinue... Knights of honor, and formidable fighters."

    "This last piece of information sounded a little like a threat. You're not sure, but you feel like the knight is looking at you disapprovingly from under his helmet."

    $ MC.rand_say(["gd: (Well, that is to be expected, he's got his orders... I'm sure me being here is not making his job any easier.)", "ne: (What a welcome. I wonder if everyone at court is so stuck up?)", "ev: (Fuck that jerk...)"])

    knight "The Palace will now close to the visiting public for today. Let me show you the way out..."

    scene black with fade

    show bg castle at top with dissolve

    gio "There you are! Mister Fancy Pants! *grumble*"

    you "Cheer up, I'm part of high society now. If you're extra-nice to me, I might let you shine my boots!"

    gio "What the... Did that thick knight hit your head or something?"

    you "Just kidding... Maybe."

    gio "Grrr..."

    scene black with fade

    stop music fadeout 3.0

    "The Palace will send someone to pick you up {b}next Monday{/b}."

    $ story_add_event("c2_princess_visit2")
    $ game.set_task("Wait for someone to pick you up on Monday.")

    return

label c2_princess_visit2:

    "Today is the day you're supposed to visit the Princess again."

    scene black with fade
    show bg plaza at top with dissolve

    play music m_palace fadein 3.0

    you "(I've been waiting here for half an hour... Is that messenger coming or what?)"

    "???" "*clear throat* Sir?"

    you "Uh? Yes?"

    # show bg carriage at top with dissolve

    "A large man wearing a knight's helmet and the palace livery calls out to you from atop a fancy carriage."

    "Carriage driver" "Hi there. I've been instructed to take you to the palace."

    you "Oh, have you now? That's nice. I wasn't keen on walking all the way back!"

    "The man ignores your tone, and you try to shrug off your bad mood. He points you towards the carriage's door. You step inside the dark, cramped cabin."

    "Inside is very dark, and you feel your way towards your seat. Your hand meets a warm, supple yet firm cushion that feels nice to the touch."

    play sound s_boing

    "Female voice" "Ahem... Sir?"

    play sound s_surprise

    "Female voice" "Would you mind... letting go of my thigh?"

    "You weren't expecting anyone else to be in the carriage. Startled, you withdraw your hand in a hurry."

    you "Oh, my Lady, I'm sorry, I didn't see you, and I thought, uh..."

    show homura with dissolve

    "You give a profuse apology. As your eyes get used to the dim light, you see the kind face of a young woman smiling back at you."

    homura "It's all right. I apologize for riding along... I understand you have business with Her Ladyship?"

    you "Uh... Yes. My name is [MC.name]. And you are?"

    homura "Oh, of course, I apologize for not introducing myself. I am Lady Homura Henso, from the Henso family. No doubt you've heard about us. A pleasure to meet you."

    $ homura_name = "Homura"

    "The young lady extends her alabaster-white hand to you in a delicate gesture. You take it and bow, unsure about the proper salute."

    play sound s_laugh

    "The woman laughs gently."

    homura "You are not from around here, are you? I can see you are not used to court etiquette. Someone from the outside, how refreshing!"

    hide homura with dissolve
    show bg exotic_emporium at top with dissolve

    "The coach is rolling and shaking as it makes its way through the city streets."

    homura "Forgive my curiosity, but I don't believe I've seen you at court before, have I?"

    you "No... I've only been in Zan for a few weeks..."

    homura "And yet, in this short time, you have made the Princess's acquaintance. An impressive feat!"

    homura "Although it's true that she likes meeting outsiders more than hanging around with courtiers..."

    you "Ah... It seems you know her habits well."

    play sound s_laugh

    homura "Of course *giggle*. The Princess and I are childhood friends... I am a year younger, though. I've always looked up to her as a big sister."

    homura "She is so serious and responsible, and yet there is something mysterious about her, even to me... She always seems to carry the weight of the world on her shoulders. And maybe she does."

    homura "Lately we have grown apart, I'm afraid... She is so serious when it comes to affairs of state... I miss my friend, but I respect her commitment."

    show bg pilgrim_road at top with dissolve

    "The coach is now coming up Pilgrim's Road, the driver yelling at the pilgrims to clear a path for the carriage."

    you "So, you and Princess Kurohime are childhood friends?"

    homura "Yes. My father, Lord Henso, is a close advisor to the King. We have always enjoyed close ties with the royal family."

    homura "We have fond childhood memories together... But lately, politics cloud everything. There are great tensions at court."

    homura "That's why I try to escape to the city whenever I can... I cannot bear the atmosphere of intrigue and hypocrisy at court."

    you "I see..."

    homura "What about you? What does the Princess want with you?"

    you "I'm not sure, but I'm going to find out."

    homura "I see... It's probably about some grand palace intrigue, like in romantic novels. Oh, I'm so curious!"

    you "Well, I can't really tell you much more. I have yet to find out what it's all about."

    "The coach now reaches the gates to the Palace. You are finally there."

label c2_castle_interview():

    show bg castle at top with dissolve

    knight "Who goes there?"

    "The knight lets you in after checking your letter of conduct, and the carriage enters the courtyard. You and Lady Henso get off near the Princess's aisle."

    show bg carriage at top with dissolve
    show homura with dissolve

    homura "Well, have a nice day, then, Mister [MC.name]. I hope we run into each other again!"

    you "Sure, same here."

    hide homura with dissolve
    show bg courtyard at top with dissolve

    you "Now, let's see what the Princess wants from me..."

    show knight with dissolve

    knight "Just climb those stairs. The guards will let you in. When you are finished, I will meet you here to show you the exit."

    play sound s_door

    scene black with fade
    show bg palace corridor at top

    "After climbing the steep stairs, you reach a vast corridor."

    show guard:
        zoom 0.6
        xalign 0.2
        yalign 0.46
    with dissolve

    "A guard beckons you to come forward."

    guard "Sir [MC.name]? The Princess is waiting for you in the visitor's room."

    scene black with fade

    play sound s_knocks

    "Woman's voice" "Do come in."

    play sound s_door

    show bg palace room at top with fade
    show kuro with dissolve

    kuro "Ah, Master [MC.name]. Thank you so much for coming to visit on such short notice."

    you "My Lady."

    kuro "I must apologize, I haven't had the chance to thank you personally. But Gio told me in his message you were compensated handsomely for your trouble."

    you "(Handsomely?!?)"

    you "Well, err..."

    kuro "And I hear you now have a trading license that makes you a proper citizen. I am delighted to hear that an upstanding person like yourself can still make it in my city, regardless of its sorry state..."

    kuro "By the way, Gio never told me, what is it you do, exactly?"

    menu:
        extend ""

        "I am a brothel owner":
            $ renpy.block_rollback()
            $ NPC_kuro.flags["occupation"] = "truth"

            you "Well, I own a brothel in town. It wasn't exactly my plan when I got here, but one thing led to another..."

            kuro "Oh! *blush*"

            kuro "I... I mean... I didn't... *blush*"

            "She takes a moment to regain her composure. After she's done, she stiffens, and goes straight to the point."

        "I am in the entertainment business (half-lie)":
            $ renpy.block_rollback()
            $ NPC_kuro.flags["occupation"] = "half-lie"

            you "I, uh, I provide entertainment, for, uh, discerning gentlemen..."

            kuro "Oh! You must mean... Like opera?"

            you "Uh... Yes, kind of, it's like opera... The ladies are in costume, and, uh, they use their oral skills a lot..."

            kuro "How nice. Maybe you can arrange for me to attend one of the shows?"

            you "Err..."

            kuro "Well, who am I kidding. I don't have the kind of freedom that would allow me to visit you, anyway..."

        "I operate an orphanage (lie)":
            $ renpy.block_rollback()
            $ NPC_kuro.flags["occupation"] = "lie"
            $ MC.evil += 1

            you "I operate an orphanage called 'The Magic Rainbow'. We welcome disadvantaged children from all over Xeros, providing them with an education and a loving environment so that they can grow..."

            kuro "Arios protects! This is wonderful!"

            kuro "I had no idea my rescuer was such a kind soul... This city is filled with scoundrels, liars, even... *shiver* {i}whoremongers{/i}..."

            kuro "It's so good to know someone is looking after the little ones, out of their kind heart, not looking to make a profit..."

            you "Yup. That's me..."

            you "(Remind me to tell Gio to keep his trap shut...)"

            kuro "Here, take this."

            play sound s_gold
            $ MC.gold += 500

            "Princess Kurohime gives you a purse full of coins. You have earned 500 denars."

            kuro "Don't even think about refusing. It's for the children."

            you "Err... Thank you, Your Highness!"

    kuro "I'm afraid I don't have a lot of time for social niceties. I have asked you to come over, because I believe you could help me - again - with an urgent matter."

    you "I see... But if you don't mind, I had some questions..."

    kuro "Fair enough... Please make it quick, though. I really cannot spare a lot of time."

    $ _result_dict = defaultdict(bool)


label kurohime_conversation_menu():

    menu:
        you "I wanted to know more..."
        "About the Kingdom":
            you "How fares the Kingdom?"

            kuro "The Kingdom... This small, powerless city-state, you mean?"

            you "Well... Zan is by far the largest city in the land..."

            kuro "I suppose. Sadly, we are lacking a strong backbone."

            kuro "It's no secret that my father, Pharo the 1st, is a weak king..."

            $ _result_dict["father"] = True

            kuro "Everywhere I look at court, I see plotters eager to stab my father in the back. They don't even have the decency to hide their intentions anymore."

            you "But surely, you are a force to be reckoned with... The knights..."

            kuro "I'm afraid it's not so simple. We hardly have an army. The knights are mostly orders from the Church of Arios and would sooner follow the High Priest than the King..."

            kuro "The rank and file soldiers are picked from the retinue of our vassals. Then there are the mercenary companies..."

            play sound s_sigh

            kuro "All of them, their loyalty lays elsewhere. Only the royal knights are faithful to the crown. And even then, I can only fully trust my own personal retinue."

            you "But the economy... Trade is booming... Surely money is power?"

            kuro "We do benefit from trade, it is true... But nowhere as much as the guilds, whose interests dwarf those of noble families."

            kuro "Commoners have started to conspire as well. The bourgeois classes do not understand why us royals should wield all the power. They are getting restless."

            kuro "No offense, of course..."

            menu:
                extend ""

                "None taken":
                    $ renpy.block_rollback()
                    $ MC.noble = False
                    you "I can understand how you feel. Being in charge is a harsh responsibility."

                "So you don't like us commoners, uh?":
                    $ renpy.block_rollback()
                    $ MC.noble = False
                    you "Well, some would say this is their just due."

                    kuro "Believe me, I can understand how they feel... But I have to look out for the interests of the State. A civil war would be a disaster for the people."

                "I am a noble myself, actually":
                    $ renpy.block_rollback()
                    $ MC.noble = True
                    you "Actually, I do come from a minor noble family. It's a long way from Zan's court, though. I'm sure you wouldn't have heard of it."

                    kuro "You do? Interesting..."

                    "She looks at you a little differently."

            kuro "So you see... We are under pressure both from the ruling elites and the upstart classes."

            kuro "And now, this cursed wedding..."

            $ _result_dict["wedding"] = True
            jump kurohime_conversation_menu

        "About you":

            you "Your... Your Highness. What's your role in all of this?"

            play sound s_sigh

            kuro "Me? *sigh* I am the Princess. King Pharo's only child."

            kuro "As a court lady, there aren't very many things I can do. I am little more than a prisoner in this palace."

            kuro "Princess, housewife or slave, it's all the same in Zan. A woman cannot live her life freely."

            you "But surely, you have the power of the royal family behind you..."

            kuro "Do not be fooled by those grand trappings. What little power my father still has is dwindling fast."

            $ _result_dict["father"] = True

            kuro "I try my best to help and be worthy of our name. If my father won't take charge, I will have to, for the good of all of us..."
            jump kurohime_conversation_menu

        "About that night":

            you "When we first met... You were wandering alone at night. What was it all about?"

            kuro "So you remember... *shy smile* Thank you again for rescuing me..."

            "The Princess smiles rarely, but when she does, it looks lovely."

            kuro "I wanted to go out on my own that night. I ditched my escort... And went about my business. I was ambushed on my way back to the palace..."

            you "What were you..."

            kuro "If you don't mind, I'd rather not say. Let's just say that over the years, I have found ways to keep in touch with the common people of my city."

            kuro "Some of my contacts aren't fond of having a unit of armed knights around them... Take Gio, for instance. *laugh*"

            $ _result_dict["gio"] = True

            you "What did those men want from you?"

            kuro "Hmmm. Some low-level kidnappers, no doubt. I don't think they really knew who I was..."

            kuro "In a sense, I was lucky. The enemies we now face are a lot more dangerous..."
            jump kurohime_conversation_menu

        "About Gio" if _result_dict["gio"]:

            you "By the way, Your Highness, how in the world did you meet someone like Gio?"

            kuro "Ah, Gio, that nice man..."

            you "'Nice man'?!?"

            kuro "Well... I have only met him once. We are mostly corresponding through trusted agents."

            kuro "He is one of the cornerstones of my network of eyes and ears in the city, though..."

            kuro "As you can imagine, I cannot very well roam the streets and taverns of the lower city to fish for information."

            you "Right. But... How did the two of you get acquainted?"

            kuro "I... went to see him once. I was looking for information about..."

            kuro "..."

            "She looks uncomfortable."

            kuro "Never mind. It is an old story."
            jump kurohime_conversation_menu

        "About your father" if _result_dict["father"]:

            you "Your father... King Pharo... How is he?"

            play sound s_sigh

            kuro "*sigh*"

            kuro "Father has not been the same since the death of my mother."

            $ _result_dict["mother"] = True

            kuro "He became completely disinterested in the affairs of the State... Missing royal councils, locking himself up in his study..."

            kuro "Some even say he indulges in terrible vices.... *shiver*"

            kuro "Those are lies, of course!!! *offended*" with vpunch

            kuro "But it's hard to argue that he hasn't been neglecting his duties..."

            you "But what about his council? Surely, they are handling it for him?"

            kuro "You wish... *somber*"

            kuro "Those snakes only serve their own interests, and those of their handlers."

            kuro "It's a good thing they are too busy feuding between themselves to really challenge my father's power."

            kuro "But he grows older and weaker by the day... And no rightful male heir exists."

            kuro "Many people think that Zan is ripe for the taking... The only thing I can do is fight back, at my modest level."
            jump kurohime_conversation_menu

        "About your mother" if _result_dict["mother"]:

            kuro "She died. Many years ago. I was still little."

            play sound s_sigh

            kuro "I wish I could remember her better..."

            you "Was it a... natural death?"

            kuro "I... I'd rather not discuss it. Let old wounds heal..."
            jump kurohime_conversation_menu

        "About this wedding" if _result_dict["wedding"]:

            you "You mentioned a wedding. Whose wedding..."

            play sound s_sigh

            kuro "Why, my wedding of course..."

            you "Your wedding?" with vpunch

            you "With whom?"

            kuro "This is the million denar question, is it not..."

            "Her mood darkens."

            you "Uhm... What do you mean?"

            kuro "My apologies. I know you are not from here... I understand that our political situation concerns you little."

            you "Well... Zan is my home now. I need to learn."

            kuro "Well, it's straightforward, isn't it? My father is old and, many say, unfit to rule... There is no male heir..."

            kuro "So whoever gets to marry me can become the father to the heir, and become regent before long..."

            you "So... No one has been chosen yet?"

            kuro "No. Not for lack of trying. You wouldn't believe some of the idiotic proposals I've received..."

            kuro "Some petty noble even told me he would have a ceremony with the whores from his brothels wearing the same outfit as me! He thought it was a compliment! I should have got him lashed on the spot..."

            you "I think I know the type."

            kuro "But... My family is too weak now, even righting a dreadful insult seems out of reach..."

            you "Aren't there more... suitable candidates?"

            "Her voice becomes cold."

            kuro "For that, you'd have to ask my father... Or rather, his advisors."

            kuro "It's not his fault, but... Everyone is putting tremendous pressure on him to choose their own side."

            kuro "So far, he has used every excuse to delay the inevitable... I know he loves me, and wants the best for me..."

            kuro "But I am afraid his will is not strong enough to protect me forever..."

            "Her voice trails off."

            you "So... Your father gets to choose?"

            kuro "Of course."

            you "But... What about you? What do you want?"

            play sound s_surprise

            kuro "Uh? Me?"

            kuro "..."

            kuro "Your question is unexpected... No one's ever asked {i}me{/i} what I wanted before..."

            kuro "I suppose I don't want to marry anyone. But it is my duty to wed and bear a male heir for the throne..."

            kuro "What kind of choice do I really have?"

            "She looks lost and vulnerable. You feel an urge to protect her."
            jump kurohime_conversation_menu

        "About this urgent business":
            $ _result_dict["can_leave"] = True

            you "Let me go to the point, then, Your Highness. What is this urgent business you wanted to speak of?"

            kuro "Yes. I have a delicate matter to discuss with you... It is of the utmost confidentiality."

            if story_flags["c1_path"] == "evil":
                kuro "You have proven your worth to me once. I also heard from Captain Farah that you were among the upstanding citizens of the slums before you moved."

                you "Well... She and I are... well acquainted, it is true..."

            else:
                kuro "And you have proven your worth to me not once, but twice. Nicely done."

                $ text1 = globals()[new_captain.name]

                kuro "I won't forget the time when you exposed that wretch Farah for the fraud that she was... [text1] speaks highly of you."

            you "Thank you, Your Highness... But what can a low servant of the crown like me do for you?"

            kuro "Well, you see, there's been a stream of murders in the city recently."

            you "Well, I was told Zan was a seedy place..."

            kuro "But wait, there's more... The victims were not just anyone."

            kuro "High-ranking officials and citizens, all servants of the royal family in one way or another."

            you "The victims were linked to the royal family?"

            kuro "Yes. They all served my father. Some of them were of dubious loyalty, but others were trustworthy beyond all doubt..."

            you "But... Who?"

            kuro "This is precisely what I need to know. So far, we have been able to keep this under wrap by presenting them as isolated incidents, but the rumors are growing stronger..."

            kuro "If this comes out, it will be another stain on my father's reputation, another proof that he is weak. I cannot let that happen."
            jump kurohime_conversation_menu

        "No more questions (take your leave)" if _result_dict["can_leave"]:
            pass

    you "So... What would you have me do?"

    kuro "As you may have surmised, I am not at the liberty to come and go easily throughout the city..."

    kuro "...and my usual agents are already well known by the city's underbelly. Even Gio..."

    kuro "But you are a fresh face, and almost no one knows we have a connection. You could act a lot more freely."

    you "I see..."

    kuro "Will you help me uncover the truth about those murders?"

    menu:
        "I will gladly do it":
            $ renpy.block_rollback()
            $ MC.good += 1

            you "Say no more, Your Highness. I will gladly help."

            kuro "Why, how gallant of you, Sir [MC.name]."

            "Gratitude gleams in her eyes as she bows slightly towards you."

            kuro "I am relieved to hear that. Now, let me waste no time in telling you..."


        "I don't know. Sounds risky...":
            $ renpy.block_rollback()
            $ MC.neutral += 1

            you "Wow, hold on, Your Highness. Murders? Royal plots? This sounds like seriously dangerous business..."

            play sound s_sigh

            kuro "*sigh* There will be a reward for you, of course..."

            you "A reward? Is it a {i}sizeable{/i} reward?"

            "She looks at you coldly."

            kuro "Yes."

            you "Well, I suppose I'm not that busy, so... Yeah, I could probably find some time to deal with this..."

            kuro "Hmpf. Now, about the next steps..."

        "What's in it for me?":
            $ renpy.block_rollback()
            $ MC.evil += 1

            you "Look, Princess, surely you don't expect me to do it without some kind of payment?"

            play sound s_sigh

            kuro "*sigh*"

            kuro "I see that the manners of my people have quickly washed onto you... How disappointing."

            kuro "There will be a reward, of course, commensurate with the task... But now I wonder if you're the right man for the job..."

            you "Haha, fear not, Your Highness. When I'm paid, I always follow my job through. *smirk*"

            kuro "So you say... Anyway. Let me explain what I want from you..."

    stop music fadeout 3.0

label c2_palace_intrusion:

    play sound s_crash
    with vpunch
    guard  "Intruder! HELP!!!"

    play sound s_punch
    pause 0.3
    play sound s_wscream

    kuro "What?!?"

    play sound s_clash
    pause 0.3
    play sound s_clash

    play music m_danger fadein 3.0

    "Sounds of sudden fighting are coming from outside the room."

    scene black with fade
    show bg palace corridor at top
    show guard:
        zoom 0.6
        xalign 0.2
        yalign 0.46
    with dissolve

    pause 0.3

    hide guard with pixellate

    "Rushing outside, you stumble upon the inert body of the palace guard."

    show judge_head:
        zoom 0.3
        xalign 0.4
        yalign 0.75

    with dissolve

    "Before him, purposefully left there for everyone to see, you stumble upon a grim sight: A severed head."

    scene black with fade
    show judge_head at truecenter with dissolve

    you "Is it..."

    you "Oh! The judge!"

    scene black with fade
    show bg palace corridor at top
    show judge_head:
        zoom 0.3
        xalign 0.35
        yalign 0.75
    with dissolve

    "Before you can collect your bearings, you see movement at the end of the corridor."

    play sound s_maniacal_laugh

    mask unknown "Muhahahahaha..."

    play sound s_sheath

    pause 0.2

    play sound s_dodge

    "The hissing sound of a thrown dagger sends you dodging reflexively, tumbling on the floor."

    play sound s_punch
    pause 0.3
    play sound2 s_boing

    "The dagger's blade hits right where you were standing."

    you "You! Come back here!"

    play sound s_sheath

    "Drawing your weapon, you leap back to your feet and run after the intruder."

    hide judge_head
    show bg palace corridor2 at top
    with dissolve

    play sound s_maniacal_laugh

    mask "MUHAHAHAHAHAHA..." with vpunch

    "Swift like the wind, the dark silhouette keeps running away from you. You manage to close in as it stops by a large window at the end of the corridor."

    "Catching up with the intruder, you take your first good look at the man."

    show bg mask escape with fade

    "The intruder cuts a tall, fearsome figure, his sword dripping with fresh blood. He is wearing a metal mask, behind which his eyes burn with a fierce, dark light."

    mask normal "What do we have here... Another lapdog of the crown... *hiss*"

    you "You! Who are you!"

    mask "Tell your mistress more will soon share the fate of this traitorous judge. This is just the beginning..."

    play sound s_maniacal_laugh

    "The man turns around and leaps through the open window."

    show bg palace corridor2 at top with dissolve

    you "Hey! Come back here!"

    you "Come b..."

    play sound s_punch

    with vpunch

    "???" "GOTCHA!!!"

    scene black with fade
    stop music fadeout 3.0

    "Before you have a chance to go after him, you get hit from behind and thrown hard on the palace floor."

    play music m_kenshin

    show bg kenshin_meet1 at top with dissolve

    kenshin "Your Highness! I got him! I have the intruder!!!"

    you "Ouch... Who and where am I... Why are there so many stars..."

    "The knight is petite, but she has an iron grasp. She holds a dagger to your throat as you give her a confused look."

    you "..."

    you "(Hey... She's sexy...)"

    you "(And she's riding me like... Hmmm...)"

    "You cannot help but notice that as she sits on you to pin you to the floor, her lower body is pressing against your crotch."

    you "(I'm... I'm getting light-headed from the hit I took...)"

    kenshin "You! Dirty spy! Who are your masters..."

    play sound s_surprise

    kenshin "Uh?" with vpunch

    kenshin "(There's something hard where I am sitting... Maybe he's got a hidden weapon of some sort...)"

    you "(Oh no... I'm getting a boner...)"

    "Using her free hand, the knight pats you down to look for a hidden blade."

    kenshin "What's this... Uh?"

    play sound s_boing
    show bg kenshin_meet2 at top with dissolve

    kenshin "It's, uh... Whaaaat?!? *BLUSH*" with vpunch

    you "(Oh, no... Don't touch it with your small, soft hand...)"

    play sound s_boing

    "Unable to help yourself, you watch helplessly as your dick swells even more."

    show bg kenshin_meet3 at top with dissolve

    play sound s_scream
    kenshin "UWAAAAAAAH!!!" with vpunch

    show bg kenshin_meet4 at top with dissolve

    kenshin "It can't be!!! It's a... It's a... It's a man's..."

    kuro "Dick! Johnson! Wiener! And all the other knights! Catch the fleeing killer!!!" with vpunch

    kuro "Commander Uesugi!!! What in Arios's name are you doing?!? The killer is getting away!"

    $ kenshin_name = "Uesugi"

    kenshin "The killer? B-B-But... I got the killer..."

    kuro "Fool! This is not the intruder! He is my guest [MC.name], he was with me at the time of the attack!"

    kenshin "W-What?!? UWAAAH!!!" with vpunch

    scene black with fade
    show bg palace corridor2 at top with dissolve

    show kenshin at right with dissolve

    "Jumping away from you, the knight commander bows very low and apologizes profusely."

    kenshin "S-Sir! I am so sorry, Sir!!! My conduct has brought shame on the Royal Knight's order... Please accept my lowly apologies, Sir! I will..."

    show kuro at left behind kenshin with dissolve
    "Princess Kurohime grabs the knight and yanks her back and forth."

    kuro "What are you doing, Uesugi?!? The killer is getting away! Run NOW! Apologize LATER!!!"

    kenshin "YES, YOUR HIGHNESS!!!"

    play sound s_run

    hide kenshin with dissolve

    "Still blushing bright red, the knight commander runs down the corridor at superhuman speed, disappearing from sight in an instant."

    play sound s_sigh

    kuro "What's wrong with this one? *sigh*"

    kuro "Forgive Commander Uesugi, Sir [MC.name]. She is a very loyal and capable knight, it's not like her to act so oafish..."

    "You slowly get up on your feet, nursing the pain in your lower back."

    you "Well, uh... She certainly packs a punch..."

    kuro "My apologies. But let me get back to my most-pressing concerns: as you just witnessed, the killings are getting more and more brazen."

#     you "What?"

#     kuro "The door! Something hit it..."

#     play sound s_crash

#     "Slamming the door to the corridor open, you stumble upon a metal chest. It seems to have been hurled into the door with some force."

#     "The guard lies face down on the floor, unconscious."

#     you "What's this sh..."

#     kuro "Ahem."

#     you "Oh, Princess..."

#     kuro "What is this? A chest?"

#     you "Step back, Your Highness. I will open it..."

#     "Carefully lifting the lid with the tip of your weapon, you take a peek inside."

#     you "What the..."

#     scene black with fade
#     show bg palace corridor at top with dissolve
#     show bg judge_head with dissolve

#     play sound s_wscream

#     you "Uwaah!!!"

#     kuro "What... what is it...???"

#     you "T-T-The judge..."

#     "Princess Kurohime frowns as understanding dawns on her."

#     kuro "Oh no... Another one..."


    kuro "That the murderer would dare soil this palace with his presence! This is unforgiveable... Did you see who it was?"

    you "Not well... Just a tall man, with long, fair hair and a metal mask that hides his face... Not much to go by."

    "The princess looks deeply troubled. She doesn't seem surprised by your description, as if it is already known to her."

    "She takes a moment to regain her composure."

    kuro "I implore you, Sir [MC.name]. Please help me stop this foul murderer. I fear for the safety of my father..."

    "Her eyes brim with tears."

    $ MC.rand_say(("gd: Fear not, Your Highness. I will protect you!", "ne: All right, all right, Your Highness. I'll help...", "ev: Worry not, Your Highness, We have a deal, remember?"))

    kuro "..."

    kuro "Thank you, [MC.name]."

    you "But... Where should I start?"

    kuro "I think it's something you can best figure out by yourself. Maybe start by asking questions from the right people..."

    kuro "Nevertheless, I would request that you keep our discussion a secret from everyone. No one should know you work for me."

    you "Sure. I understand."

    kuro "You have best be on your way now. I must see to the security measures of the palace. They are obviously lacking."

    you "Indeed. Farewell, Your Highness."

    scene black with fade
    show bg courtyard at top with dissolve

    "Stepping out of the Princess's quarter, you see the Palace buzzing with activity as knights run around yelling orders and confused servants wander aimlessly."

    you "That masked guy sure has the whole royal court on edge..."

    you "(They must all wonder who's next.)"

    you "I'm not sure if this assignment is a golden opportunity, or a death sentence..."

    scene black with fade
    stop music fadeout 3.0

    "You must investigate the murders in town."

    $ game.set_task("Find out more about the murders of high-ranking officials.")
    $ calendar.set_alarm(calendar.time+1, Event(label = "c2_gio_message"))

    return


#     homura "Well, I'm not {i}supposed{/i} to go there..."

#     homura "But there was a commotion with the attack at the palace, and my music class got cancelled."

#     homura "I figured it was a perfect chance to escape on my own and have a little adventure."

#     you "An adventure?"

#     homura "Yes... The lower city is sooo exciting! The people, the sights... It's so different from court, you know!"

#     you "Well... I suppose so."

#     homura "You have no idea how liberating it is to walk among the common people, being anonymous in a crowd... I try to leave the noble quarters whenever I can."

#     you "It's funny... Most people want to get into the higher city, not the other way around."

#     homura "Everyone is assigned to their own place in this city. But I believe a real adventurer should break those barriers and go wherever she pleases!"

#     homura "Don't you agree?"

#     menu:
#         "Sure":
#             you "Sure. Class is an artificial social construct that is the outcome of centuries of subjective thinking, ontologically undifferentiated from vulgar prejudice and superstition."

#             "She blinks."

#             homura "Uh... Yeah. Sure..."

#             you "Nothing should stop you from mingling with the lower class, just like an outsider like me should be able to reach the top! Right?"

#             homura "Hahaha, right! That's the spirit. *smile*"

#         "No way":
#             you "No, not really. The aristocrats should keep separate from the plebs."

#             you "Otherwise, social distinctions will become blurred, and soon enough, people will start to question our most hallowed institutions, like absolute monarchy or slavery or beheadings..."

#             "She frowns."

#             homura "Oh, boo-hoo!!! You sound just like my father!"

#             homura "I didn't think you would be so old-fashioned. Anyway, regardless of what you think, I will live my life to the fullest."

#             you "Well... I was just saying..."

#     "The carriage comes down to a stop. Looking outside, you can see [brothel.name], its lights shining in the early evening."

#     you "It looks like I've arrived."

#     homura "Great, I'll go down with you."

#     "The coach leaves as you stand by the door of the brothel with Homura."

#     homura "Wow, so this is your house?"

#     you "Well, it's not..."

#     homura "It looks like an intriguing place! I might drop by one of these days..."

#     play sound s_laugh

#     homura "There's just so much to explore in the lower city! *giggle*"

#     homura "See you around, Mister [MC.name]"

#     you "Yeah... See you around..."

#     scene black with fade
#     show expression bg_bro at top with dissolve

#     "You come back to the brothel exhausted, thinking about your day. A princess, a killer, a knight and a court lady..."

#     you "It's going to take me a while to entangle this web..."

#     you "But maybe it's my ticket to glory in this city? Who knows..."

#     return



label c2_gio_message():

    play sound s_dress
    show bg letter at top with dissolve

    "The next morning, you wake up to find a note slipped under your door."

    call screen letter(header = __("Where have you been?"), message = MC.name + __(", where the heck have you been? I'm still waiting for you to tell me how the palace meeting that I arranged went. \n\nYou didn't forget your old pal, did you?\n\nAnyway, I have some juicy intel for you. Can we talk? You can meet me at the Plaza."),
                          signature = __("Your bestie, Gio"))

    you "Gio... Ever so slimy."

    you "Well, I've got to start my investigation somewhere, I suppose."

    scene black with fade

    "Meet Gio by the {b}Plaza{/b} in the warehouse district."

    $ game.set_task("Meet Gio at the plaza.")
    $ story_add_event("c2_gio_meeting")

    return

label c2_gio_meeting():

    play music m_gio

    "As you reach the plaza, you scan the area for signs of Gio."

    "You spot a shady figure leaning against a wall, trying to look inconspicuous in spite of his bulk."

    "Upon closer inspection, the fat man is wearing a fake nose and mustache, a top hat and ill-fitting glasses."

    you "Gio?"

    gio incognito "Hush!!! I am here incognito! Don't blow my cover!"

    you "..."

    you "I could spot you from the other end of that plaza, you know."

    gio "What?"

    "Gio looks around him carefully four or five times, with exaggerated caution."

    gio "Hmpf, I guess the coast is clear. I suppose I can take my cunning disguise off for a moment now."

    show gio with dissolve

    gio normal "So you finally came. You gave me a good scare, my boy!"

    gio "When I heard there was a murder at court, I thought..."

    you "You thought... You were worried about me?"

    gio "...I thought you might have done it. And as your patron, I was going to be in deep, deep trouble."

    you "..."

    gio "Anyway, the dust has settled now, and I've heard all about the masked intruder, the murdered judge, the chaos at court..."

    you "Well, you and a couple hundred other people..."

    gio "But you must tell me, [MC.name]. What did the Princess want from you?"

    menu:
        extend ""

        "Tell the truth":
            $ renpy.block_rollback()
            you "Well... She wants me to investigate the murders. Find out who's behind this."

            gio "I see... Why you, of all people, I wonder?"

            you "I don't know. I guess that night I rescued her from thugs convinced her I'm on the right side..."

            gio "Yeah. Maybe."

            gio "Or maybe she just likes you. *grin*"

            you "Wipe that stupid grin off your stupid face... Stupid!"

            gio "*grin*"

            you "Anyway. Know anything about the murders?"

        "Lie":
            $ renpy.block_rollback()
            $ NPC_gio.love -= 1

            you "Well, uh... She wanted to settle a land dispute that arose from, uh... The brothel's relocation..."

            "Gio gives you a skeptical look."

            gio "Come on, don't take me for a fool, buddy..."

            gio "I guess she asked you not to tell anyone."

            you "..."

            gio "*sigh* Fine, I'll respect the Princess's wishes."

            gio "But anyway. I suppose you wouldn't be interested in intel about the recent murders, then..."

            you "Well, you know... I can always use information. For my own, er, curiosity..."

    "Gio looks carefully around him and takes a conspiring tone."

    play music m_mafia fadein 3.0

    gio "Ever heard of the Kunoichi?"

    you "The Kuno... What?"

    gio "The Kunoichi."

    you "The Kunoichi? What's that?"

    gio "A secret order of ninjas... All of them, females."

    you "Female... ninjas?"

    gio "Yes. The Kunoichi are women trained from childhood as killers and spies... They work from the shadows..."

    gio "Blades, disguise, poison, even sex... They are experts at using every kind of weapons to achieve their ends."

    gio "They are deadly and invisible to even the most trained eyes. They're the most feared of the ninja orders."

    you "Who is their leader?"

    gio "No one is. Each ninjutsu school trains a single Kunoichi every generation. After they graduate, they become freelance operators."

    gio "Some of them follow a cause or a master, others offer their blade to the highest bidder. One thing is for sure: They don't come cheap."

    gio "There might not be more than a few dozen in all of Xeros, but each of them is worth a small army."

    you "Are there some here, in Zan?"

    gio "The Kunoichi are usually scattered across Xeros on various assignments. To my knowledge, only a handful are active in Zan. But as they stick to the shadows, tales of their deeds rarely surface."

    gio "Nevertheless, according to my sources, there's been a surge in their activities lately. Just when the murders started... Troubling, isn't it?"

    you "All right. But how does that help us? I saw the killer. He was a man... Not a female ninja."

    gio "Well, uh... Might have been a cross-dresser? Did he sport any man-boobs? Wiggled his ass much?"

    you "No! It was a dude. Believe me, I can tell. I'm a womanizer by trade."

    gio "Well, come on... What man hasn't ended up in bed with a ladyboy after a glass too many? Am I right? *wink*"

    you "No, Gio. You're {i}not{/i} right. And I don't want to picture you in that situation for even a second... *retch*"

    gio "Anyway. I'm sure the killer and the Kunoichi are in cahoots somehow."

    you "I don't know. Could be anyone... The thieves guild, Shalia worshippers... Doomsday cultists, mad scientists, foreign spies... Disgruntled servants, tax dodgers, jealous lovers, angry nerds..."

    gio "Stop it! My sources say that the Kunoichi have been all over the lower city recently. Spying and gathering information, no doubt. It cannot just be a coincidence."

    gio "The Kunoichi come and go as they please. Even I cannot keep track of what they do... But my gut feeling is, this is all related. There is also one more piece of information..."

    you "Okay, okay. For the sake of this argument, let's say the Kunoichi are involved. How do I find them?"

    gio "Find them? Well, it's impossible to find them... Unless they find you first."

    you "Ok, great. So I just wait for one to show up on my doorstep, then?"

    gio "Well, uh, that's the thing... There's this intel that says, uh..."

    "Gio looks nervous and starts glancing anxiously around him."

    you "Speak, Gio. I don't follow."

    gio "There's this... tiny little thingy, you see..."

    you "What now? *sigh*"

    gio "My sources say one of the Kunoichi has taken on a new contract..."

    you "A contract?"

    gio "Yes... And the word on the street is... Well... It's on your head, pal."

    you "A contract? On my head?" with vpunch

    gio "Yes."

    you "Wait, didn't you say the Kunoichi were incredibly efficient, cold-blooded assassins?!?"

    gio "Did I mention that? Well... It's certainly overblown... I mean, they only have a life-long training at killing by any means possible... And sure, they're proficient with all poisons and weapons known to man..."

    gio "But, you know, I'm sure you'll be fiiine. Look, you're not dead... Yet. *cough*"

    you "WHAAAAAAT!!!" with vpunch

    you "HOW CAN YOU TELL ME THIS SO MATTER-OF-FACTLY???"

    gio "Well, uh, I hear your concern, but do not worry, my friend. In everything, there is a silver lining."

    gio "I specifically inquired: they are after {b}you{/b}, nothing was said of your associates... So I figure, I should be safe from harm... *sweat*"

    you "THAT'S NOT THE DAMN POINT!!!" with vpunch

    gio "It's a pretty important point to me..."

    you "What am I going to do?"

    gio "Well, I mean... You wanted to meet the Kunoichi, right? Seems like a good occasion..."

    you "Not if I'm being MURDERED!!!" with vpunch

    gio "D-Don't be over-dramatic... Nobody is getting murdered..."

    "A paperboy runs past you both."

    "Paperboy" "Read the Zanic Magic Tribune! A JUDGE HAS BEEN GRUESOMELY MURDERED!!!"

    gio "I mean, except for the judge, but..."

    "Paperboy" "EVERYONE IS GETTING MURDERED LEFT AND RIGHT!" with vpunch

    "Paperboy" "MURDER MURDER MUUURRRRDEEER!!!" with vpunch

    gio "..."

    you "..."

    gio "Well... Really, I'm sure you'll be fine... Hehehe... *gulp*"

    "(Some weird boy in the background)" "Redrum, redrum..."

    play sound s_dress
    "Gio nervously fastens his fake nose and mustache back on."

    gio incognito "Look, I will be awfully busy in the coming days... Maybe take a little vacation outside the city for a while."

    you "Wait! Don't leave..."

    gio "It was nice knowing you, anyway... Don't forget me when writing your will, okay?"

    gio "If I were you, I'd do it sooner than later. Wouldn't want that cute slave of yours to go to just anyone, would you?"

    you "Gio... *homicidal stare*"

    gio "Well, see ya! Don't go looking for me, there's really no need! *sweat*"

    gio "Off I go!"

    hide gio with dissolve

    "Gio starts off, running across the plaza with an arm above his head in an exaggerated gesture, waving his cloak around with his other arm, like he's some cheap pulp novel adventurer."

    scene black with fade

    you "What the hell, why would the Kunoichi want to murder me..."

    you "Well, let's not worry too much about it. Gio is usually full of crap, so his intel is probably garbage... *nervous*"

    $ game.set_task("Wait for the Kunoichi to show up, and... Murder you?")
    $ temp_gossip += chapter_gossip["c2_kunoichi"]

    $ calendar.set_alarm(calendar.time + 2, StoryEvent("c2_suzume_invitation"))
    $ calendar.set_alarm(calendar.time + 5, StoryEvent("c2_homura_city_meet", type = "morning"))

    return


label c2_suzume_invitation():

    $ season = calendar.get_season()

    scene black with fade
    show expression bg_bro at top
    with dissolve

    play sound s_rooster

    "This morning, you come out of [brothel.name], ready to start your day."

    you "Aaah! Such a nice, fresh [season] morning!"

    "*SWOOSH*" with hpunch

    "As you come out of the house, a sudden strong gust of wind nearly makes you fall over."

    you "Aaaah!!! NGGH!"

    "Your scream is muffled by a piece of cloth that falls over your head."

    you "NNNGHH!!!"

    you "(Nooo!!! Don't kill me!!!)"

    "You go into a panic, desperately trying to free yourself from the gagging cloth. After a few moments, however, you realize what it is."

    scene black with fade
    show panties at truecenter with dissolve

    you "Uh... Wait... Those are... panties?"

    "The cloth that the wind pushed into your face is actually a piece of women's panties. Quite sexy panties, at that."

    you "It looks like silk..."

    you "*sniff* *sniff*"

    you "Used one, at that... *sniff* A young, hot girl, with a toned body... Smells kind of... Exotic."

    you "(Wait, why am I sniffing panties in the middle of the street???)"

    scene black
    show expression bg_bro at top
    with dissolve

    "Hiding the panties in your pocket, you strike the dust off of your clothes."

    you "Now, what was I..."

    "*SWOOSH*" with hpunch

    "Another strong gust of wind suddenly pushes you forward, and you stumble down the street, doing your best not to fall. You end up grabbing a wooden post to try to keep your balance, stopping your face inches from some sort of flyer."

    you "What the... Wait, what's this?"

    "A piece of paper is pinned to the wooden post. You feel like you might as well read the message."

    call screen letter(header = __("Looking for my panties"), message = __("Have you seen my panties?\n\nI have lost them somewhere in this part of town. I miss the soft, silk fabric rubbing against my smooth, nubile skin... I feel so exposed without them!\n\nPlease meet me off the main path in the forest near the farm, where no one will bother us. You will be rewarded with a big surprise..."),
                          signature = __("PS: Don't worry, this is totally not a trap."))

    you "This must be the panties I found before... What an amazing coincidence!"

    "Strangely, you notice several dozen such flyers, pinned everywhere around your side of the street."

    you "Hmmm."

    you "(I should think about returning those panties...)"

    menu:
        you "What should I do..."

        "I should return them":
            $ renpy.block_rollback()
            $ story_flags["panties trap"] = False

            you "Well, I should find the owner and return these. I'm not so heartless that I would leave a poor girl pantyless in the woods."

            you "Good thing the message mentions that it is {i}totally not a trap{/i}. At least I don't have to worry about anything bad happening."

        "It's a trap":
            $ renpy.block_rollback()
            $ story_flags["panties trap"] = True

            you "No! It's a TRAP!!!" with vpunch

            you "(But wait... The message explicitly says it's {i}totally{/i} not a trap, so it can't be...)"

            you "(Unless the message lies... But the panties are real...)"

            "You scratch your head."

            you "This is all terribly confusing..."

    "Visit the farm to return the panties to their rightful wearer."

    $ game.set_task("Visit the {b}farm{/b} to return the missing panties.")
    $ story_add_event("c2_suzume_forest1")

    return


label c2_suzume_forest1():

    "Girl panties held firmly in your hand, you decide to investigate the mysterious posting you saw outside your door."

    play music m_nature fadein 3.0

    scene bg farmland with fade

    "Ignoring the weird looks passersby are giving you, you head for the farmlands outside the city. Soon, you reach a little-used path that leads deep into the forest."

    show bg forest at top with dissolve

    if story_flags["panties trap"]:
        you "Well, it sure is off the beaten path... I should be on my guard; this has all the makings of a trap."

    else:
        you "Well, it sure is off the beaten path... I guess the poor lady was so embarrassed that she wanted to meet in a place as far from prying eyes as she could..."

    "Heading deeper into the forest, you quickly lose sight of the main road, light dimming around you."

    you "Hello! Anyone looking for missing panties? Helloooo!"

    play sound s_laugh

    "A gentle laugh echoes among the trees."

    "Female voice" "Mister..."

    you "Yes? Anyone here?"

    play sound s_laugh

    "Female voice" "Come, dear mister... Don't be afraid..."

    if story_flags["panties trap"]:

        you "(I have a bad feeling about this...)"

    else:
        you "Sure, where are you?"

    you "(I think the voice is coming from this clearing... Let's investigate.)"

    show bg clearing at top with dissolve

    "Standing in the middle of the clearing, you feel as if someone is watching your every move. Suddenly, you wonder if coming here was really such a good idea."

    play sound s_laugh

    "Female voice" "KU KU KU KU... *odd giggle*"

    play sound s_dodge
    show suzume with blinds

    "Out of thin air, a young woman appears before you, where no one was standing just a second before."

    play music m_suzume fadein 3.0

    you "Whoah!!!"

    suzume "Mister! HI!!! Ku ku ku..."

    you "Who... Who are you?"

    suzume "My name is Suzume. Nice to meet you, Mister [MC.name]. "

    $ suzume_name = "Suzume"

    suzume "Seen up close, you're cuter than I thought! So, you found my message?"

    you "You're the one who posted that message about missing panties?"

    suzume "Sure, Mister, I was expecting you. Ku ku ku..."

    you "Wait, something's not right here... How do you know my name? How did you know I would come?"

    suzume "Your name? Uh... So... Ku ku ku..."

    suzume "There's a perfectly reasonable explanation for it, you see... Ku..."

    suzume "It was a lucky guess!" with vpunch

    you "What?!?"

    suzume "Well..."

    play sound s_boing
    show suzume bend with dissolve

    suzume "*jiggle* *jiggle*"

    play sound s_horn

    show suzume bend:
        ease 0.5 zoom 2.5 xoffset -250 yoffset 75
        pause 0.5
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    you "OH!!!"

    you "(Boobies...) *drool*"

    play sound s_boing

    suzume "I'm sorry... *jiggle* What was your question again? *jiggle*"

    you "..."

    you "I... I forgot..."

    suzume "So..."

    show suzume normal with dissolve
    stop music fadeout 3.0

    suzume "You found my panties, Mister?"

    "Suddenly, you realize that you've been clutching the panties the whole time."

    you "Oh! Yes... Sorry..."

    suzume "I've been missing them sooo much... I was in danger of catching a cold!"

    you "Catching a... Wait..."

    you "(Does that mean she's not wearing any panties right now...)"

    show suzume bend with dissolve

    suzume "Mister?"

    you "*drool*"

    suzume "Mister? I think your nose is bleeding..."

    scene black with fade
    show bg suzume_forest2 at top with dissolve

    play music m_wind fadein 3.0

    suzume "I've been feeling the cool forest wind blow against my crotch for so long... It tickles..."

    you "*GULP*"

    suzume "I just can't take the stimulation... It makes my whole body feel weird..."

    you "I... See... *gulp*"

    suzume "It's cold, but it makes me feel hot... Mister, isn't it strange? Perhaps you could take a closer look? There might be something wrong with me..."

    you "Err... I see... Nothing... Wrong... You..."

    play sound s_dodge

    "A sudden gust of wind lifts suzume's skirt even more, giving you a perfect view of her round, youthful ass."

    play sound s_ahaa

    suzume "Oooh..."

    you "*GULP*"

    play sound s_dodge
    show bg suzume_forest3 at top with dissolve

    "The wind gets even stronger, this time bringing her top into disarray. It was never very clear how it held up in the first place."

    play sound s_surprise

    suzume "Oh no! Mister, help me, come quickly!"

    suzume "My chest and privates are exposed... Quick, cover them with your hands!"

    play sound s_boing

    "Suzume grabs your hands and places them firmly on her tits. You feel her nipples harden against your touch."

    you "What..."

    "Wind" "WOOSH..."

    suzume "No time to think! Now, my privates, you have to do something, I'm really going to catch a deadly cold!"

    you "But... My hands are taken..."

    suzume "Use something else than your hands! Anything that fits!"

    play sound s_dodge
    show bg suzume_forest4 at top with dissolve

    "The wind blows erratically, somehow shoving you forward as your pants mysteriously drop on your ankles. Suzume backs down towards you, and suddenly finds herself impaled on your erect dick."

    play sound s_aaah

    suzume "Ah! [emo_heart]"

    play sound s_moans

    suzume "Oh, Mister! I think you found something good to plug it..."

    suzume "It feels nice and warm now... Thank you, Mister... Ku ku ku [emo_heart]"

    "Before you can even take stock of the strange situation you're in, Suzume's petite body starts moving of its own volition."

    if story_flags["panties trap"]:
        you "(This is bad... I'm losing control...)"
    else:
        you "(This is incredible...)"

    "Her pussy is amazingly tight and seems alive as she expertly contracts around your dick, massaging your cock in all the right ways..."

    suzume "Oh, Mister, let me make you feel good..."

    show bg suzume_forest3 at top with dissolve

    "Her voice has become sultry and somewhat more mature. She turns her head and looks at you with dreamy eyes..."

    suzume "Trust me, you're going to love this {i}to death{/i}..."

    "Shaking and moving her butt, Suzume bends your cock at different angles, each time hitting more of your pleasure centers."

    suzume "Oh yes, Mister, this is so much fun! Let's keep going just a bit more... {i}The end is near{/i}..."

    "Suzume is now moving wildly, arching her back in impossible ways, bringing your cock deeper and deeper in until it hits her cervix, almost painfully."

    show bg suzume_forest4 at top with dissolve

    suzume "Here it comes!!! The {i}five-point pussy exploding dick technique{/i}!!!"

    "Your dick is hit simultaneously from all sides with jolts of energy as Suzume's pussy walls close in around you. It is more than you can possibly stand."

    play sound s_wscream
    show bg suzume_forest4 at top with flash

    you "UWAAAAAH!!!"

    "Your cock explodes like a volcano, filling her pussy with hot cum."

    play sound s_orgasm_young

    suzume "OH, YES!!!"

    show bg suzume_forest5 at top with doubleflash

    "Your cock keeps cumming and cumming. You almost feel as if your whole life energy is draining out of you."

    you "I feel... Dizzy..."

    show bg suzume_forest6 at top with flash

    play sound s_evil_laugh

    suzume "Ku ku ku ku ku..."

    you "(What's... Happening to me...)"

    suzume "Good night, sweet prince..."

    play sound s_mmmh

    scene black with circlein

    "..."

    play sound s_wolf

    show bg forest at top with dissolve

    "When you finally wake up, the sun is getting low on the horizon."

    you "(Man... I must have been out for hours...)"

    "You stand naked and shivering in the center of a large pool of bodily fluids. You try not to think about how all of this could have come out of your body."

    you "Wow, what a mess. I didn't know I had it in me to cum this much."

    "Limping back towards the farmlands before sunset, you try to make sense of what happened, but thinking back on it threatens to give you an erection again, and it hurts."

    scene bg farmland dusk with fade

    "Reaching the main road again, you start heading home. Little by little, your condition is improving."

    "As you approach the city, you spot a familiar figure."

    show suzume normal with dissolve

    you "Oh! Hey, it's Suzume!"

    suzume "Uh? What?"

    show suzume at jumping

    suzume "YOU!!! When... How... Why..."

    you "Hey, you left me out there in the cold... Not nice..."

    suzume "Wait, you shouldn't even be able to walk..."

    you "I know! I've got such a boner, even now! You little succubus..."

    suzume "A bo- What?!?" with vpunch

    you "A boner... It's a colloquial expression, it means..."

    suzume "I KNOW WHAT A FREAKING BONER IS!!!" with vpunch

    you "Gee, don't get angry..."

    "You poke Suzume in a booby."

    play sound s_boing

    you "You sure know how to raise a man's appetite!"

    suzume "..."

    suzume "(How is this happening... The secret technique of the iron pussy school is {i}flawless{/i}...)"

    you "Look, I think things have been moving a little fast between you and me..."

    suzume "(This cannot be... This man is more dangerous than he looks... I must retreat...)"

    you "What do you say, you and I go to the city sometime and have a..."

    play sound s_fire

    hide suzume with blinds

    you "Uh?"

    "She's gone. She disappeared so fast you couldn't even see her go."

    you "Afraid of commitment, uh? I know the type..."

    you "Still, she's got a body to {i}die{/i} for..."

    you "And that slutty, slutty dress..."

    "Your cock threatens to burst out of your pants just thinking about her."

    you "Ouch, it hurts... Better go home and have an ice-cold bath."

    scene black with fade

    $ MC.change_prestige(2)
    $ MC.interactions = 0

    "You have spent all your actions for today."

    $ calendar.set_alarm(calendar.time+1, StoryEvent("c2_suzume_report1", type = "morning"))
    $ game.set_task(__("Wait for events to unfold."))

    return


label c2_suzume_report1:

    scene black with fade
    show bg mansion night at top with dissolve

    "Somewhere within the rich districts of the Inner City..."

    play music m_wind fadein 3.0

    "Male voice" "It's cold out here... Where the hell is the damn girl?"

    show suzume:
        xpos 1.2
    show suzume at totheright with move

    "Male voice" "Gyaaah!" with vpunch

    suzume "Here, boss. Reporting from duty."

    "Male voice" "D-d-don't creep up on me like that!"

    suzume "Sorry, boss. *bow*"

    "Male voice" "Humph. Anyway, what's your report? Is the deed done?"

    suzume "There was a slight, er... setback. The target is tougher than I thought. I need a little more time."

    "Male voice" "WHAT? Do you know how much I pay you?" with vpunch

    suzume "Yes, boss..."

    "Male voice" "I want results. RESULTS, you hear! If I wanted incompetence, I'd have sent my own men!"

    suzume "..."

    "Male voice" "Make sure you take care of this by next week. Now, go. Dismissed, shoo!"

    suzume "Yes, boss..."

    hide suzume with blinds

    "Male voice" "(She'd better do what she's told... I need to get rid of this bastard [MC.name]...)"

    scene black with fade
    $ story_add_event("c2_suzume_arena")
    $ game.set_task(__("Keep exploring the city districts for clues."))

    return


label c2_suzume_arena(): # Arena

    scene black with fade
    show bg arena_front at top with dissolve

    "The arena is quiet today, as it is a holy day for gladiators. The lucky bastards have lots of perks like this, their unions being notoriously powerful."

    play music m_wind

    "An eerie silence fills the empty plaza in front of the arena as you cross it, there isn't a soul in sight."

    "You've heard many a deadly challenge has been cast here, the bloodlust of the arena spilling out into the nearby streets. Today, however, you're more in the mood for herbal tea."

    play sound s_mystery

    "Female voice" "HEY, YOU!!!" with vpunch

    you "Uh?"

    play sound s_wind

    "A sudden gust of wind engulfs the plaza, almost making you spin on your heels."

    play music m_suzume fadein 3.0
    show bg rooftop at top with dissolve

    "Voice" "YOU! I CHALLENGE YOU!!! FACE ME!!!" with vpunch

    "Looking up towards the voice, you see a colorful silhouette standing against the sky, as if she just materialized out of thin air."

    show suzume with blinds

    suzume "You may have bested me the last time we met... But this time, I shall beat you!"

    "Immediately upon seeing the girl, you have a keen recollection of her missing panties, meeting her in the forest, and everything else. Your groin grows swollen and painful..."

    you "Hey, I remember you! Suzume, isn't it?"

    you "What are you challenging me for... Is it what I think it is?"

    suzume "Don't you know it! I have prepared all my life for this battle... Meet me in the forest near the farm, right where we sparred the last time. I shall await you!"

    play sound s_mystery

    hide suzume with blinds
    suzume "KUKUKUKUKU..."

    stop music fadeout 3.0

    show bg arena_front at top with dissolve

    you "..."

    you "What the hell was that?"

    if story_flags["panties trap"]:
        you "I should be careful around the girl... I can't quite put my finger on it, but something smells fishy here. And it's not the panties..."
    else:
        you "Anyway, I'm pretty sure she invited me for a romp... That's what 'sparring' means, right?"

    scene black with fade

    "Go to the {b}farm{/b} again to meet with Suzume."

    $ story_add_event("c2_suzume_forest2")
    $ game.set_task("Meet the strange girl again at the {b}farm{/b}.")

    return


label c2_suzume_forest2():

    play music m_nature fadein 3.0

    scene bg farmland with fade

    "Going back to the farm, you follow the tracks to the middle of the forest to meet with the strange blue-haired girl."

    show bg forest at top with dissolve

    you "I've been thinking about our last encounter all night..."

    you "(Man, I shouldn't have worn tight pants. It's hard to walk with such a hard-on...)"

    play sound s_mystery

    "Female voice" "KU KU KU KU KU... You came..."

    you "Well, not yet, but..."

    play music m_suzume fadein 3.0
    show suzume bend with blinds

    "The cute girl from the last time materializes before your eyes."

    suzume "You! [MC.name]! You are brave to come and face me in open battle..."

    if story_flags["panties trap"]:
        you "So... Are you gonna tell me what this is all about yet? Or is it another sexual challenge?"
    else:
        you "Uh... Open battle means sex, right?"

    suzume "..."

    show suzume normal with dissolve

    suzume doubt "(Well, I was thinking of slicing him up... But I am a master of sex martial arts... I can't let a man beat me at my own game...)"

    show suzume bend with dissolve

    suzume bend "Ahem. YES! Yes, of course, we shall engage in a battle of the sexes... And by this I mean we should engage in combat using only our bodies!"

    "Her voice suddenly turns more seductive."

    suzume "I didn't forget how you ravaged me the last time we met... But I'm ready for more..."

    scene black
    show bg suzume_forest1 at top
    with fade

    suzume "My body is ready to withstand your assaults... You cannot win this! But try, if you dare... [emo_heart]"

    you "I... I have no idea what you're saying... But I'm super turned-on right now!"

    you "ATTACK!" with vpunch

    stop music fadeout 3.0

    show bg suzume_forest2 at top with fade

    "You waste no time and rip your clothes off, before lowering her panties and exposing her young, wet slit."

    you "I can't resist such a juicy pussy..."

    "Without further ado, you stick your tongue inside her. She squeals with pleasure as her love juice starts pouring out of her."

    play sound s_sucking

    suzume "Aaah, my weak spot... You're a worthy opponent, I can see that... Mmmh..."

    "Grabbing her ass, you start kneading her firm buttocks, all the while shoving your tongue deeper inside her. She moans wildly."

    suzume "Oh, that's the spot... Keep doing that... [emo_heart]"

    show bg suzume_forest3 at top with dissolve

    "Feeling your own desire grow, you start undressing her, popping her ample breasts out of her skimpy outfit."

    play sound s_aaah

    suzume naked "Oh yes, pinch my nipples... Harder! Oh, I'm close to... to..."

    with flash

    play sound s_orgasm_young

    suzume "AAAAAHAAAA!!!"

    "The blue-haired girl cums hard as you hungrily gulp her love juices."

    "She is far from being done, though."

    play sound s_laugh

    suzume "KU KU KU... Let's get serious, now!"

    show bg suzume_forest4 at top with fade

    "Before you know it, you are ramming her pussy furiously, her inner walls squeezing your dick like a boa constrictor."

    you "(Oh... this is even more amazing than the last time...)"

    suzume "Yes! Yes! Give it all you've got!!!"

    "Her stamina is amazing, and her pussy flows like a river. You bang her with abandon, slamming your dick deeper and deeper with every stroke."

    suzume "OH, YES! FUCK ME!!! HARDER!!!"

    "She is barely able to stand as you continue your assault, and the whole forest echoes with screams of passion."

    play sound s_scream_loud

    suzume "YYYESSSS!!!" with flash

    play sound s_orgasm_young
    show bg suzume_forest5 at top with doubleflash

    you "WHAAAAAAG!"

    "You cum an insane amount inside the young girl's pussy, filling her up to the brim until it leaks out of her tight cunt."

    "She shivers with pleasure with every spurt, her body enticing you to spend more."

    show bg suzume_forest6 at top with flash

    suzume "A-Amazing..."

    suzume shrewd "But the battle is only getting started..."

    suzume "Come on! Show me what you can do!"

    with Fade(0.5, 1.0, 0.5)

    play sound s_moans_short

    suzume naked "Ah yes! YES!!!" with hpunch

    with flash

    with Fade(0.5, 1.0, 0.5)

    play sound s_mmh

    suzume "MORE! MORE!" with doubleflash

    with Fade(0.5, 1.0, 0.5)

    play sound s_ahaa

    suzume "AGAIN! Cum inside me again!" with hpunch

    with flash

    with Fade(0.5, 1.0, 0.5)

    play sound s_evil_laugh

    suzume "Do you think you're done here? Come on! More!" with doubleflash

    with Fade(0.5, 1.0, 0.5)

    play sound s_orgasm_young

    show bg suzume_forest5 at top with doubleflash

    suzume "Oh yes... yes... YES!!!" with hpunch

    show bg suzume_forest6 at top with flash

    scene black with Fade(0.5, 1.0, 0.5)

    you "Come on! I can go one more time!"

    play sound s_surprise

    suzume "(What... What monstrous strength...)"

    show bg suzume_forest7 with fade

    you "UWAAH!!!" with flash

    suzume "NGGH!! *gulp* *gulp*"

    you "Aaaah... AGAIN!" with doubleflash

    suzume "(I've already made him cum a dozen times... What sorcery is this? My iron pussy techniques are... beaten?)"

    you "I feel great! I feel like I could go on forever!"

    suzume "Y-You... You're not human..."

    scene black with fade

    "You both keep fucking for a long time..."

    show bg suzume_forest8 with fade

    play music m_suzume fadein 3.0

    suzume shrewd "I... I need a break..."

    you "Phew... Well... It's true we went a bit far."

    you "I haven't felt like that in ages... You've got a body to die for!"

    suzume "Kukuku... Even though you say that... You're still standing. I've never met a man like that..."

    you "Oh well. Now that you mention it, running a brothel did increase my stamina. I mean, I've always been a horny bastard, but..."

    suzume "..."

    you "Suzume?"

    suzume "ZZZZ..."

    you "She's fallen fast asleep. Hey! That's my move!"

    suzume "ZZZZZZZ..."

    you "(Well, normally I'd have misgivings about abandoning a naked, passed-out girl at dusk in the middle of a forest...)"

    you "(But I'm late already, and she was the one to leave me out in the cold last time. I guess you could say we're even.)"

    scene bg farmland dusk with fade

    "Stumbling back to the brothel, you find yourself very light-headed."

    you "Man, this little fuck session did take its toll on my body... If I don't watch out, I might drop dead from exhaustion!"

    "When you finally reach home, all you have the strength to do is to fall in bed and sleep for twelve hours straight."

    $ MC.interactions = 0
    "You have lost your remaining actions for the day."

    $ game.set_task("Wait for events to unfold.")
    $ MC.change_prestige(2)
    $ calendar.set_alarm(calendar.time+1, StoryEvent("c2_suzume_report2", type = "morning"))

    return


label c2_suzume_report2():

    scene black with fade

    "Later that night."

    show bg mansion night at top with dissolve

    "Male voice" "YOU WHAT?!?" with vpunch

    show suzume normal with dissolve

    suzume normal "..."

    suzume "I failed again."

    "Male voice" "You did! You failed me twice!"

    suzume "My Master at the School of Wind used to say: choosing the right weapon is half-the-battle. I shouldn't have used sex against this man. His power level is too high."

    "Male voice" "Too high? How high?"

    suzume "By my estimate, I reckon..."

    suzume "Over nine thousand."

    "Male voice" "Over NINE THOUSAND??? AAAARGH!!!" with vpunch

    play sound s_shatter

    "The man breaks something in frustration."

    "Male voice" "Come to think of it... Over 9,000 what? I didn't know there was a scale for sexual stamina."

    suzume "Me neither, I just made up a number that sounded cool."

    suzume "But don't worry. I am as good with a blade as any ninja. I shall cut his manhood clean off, the old-fashioned way."

    "Male voice" "Whoah, isn't that a little extreme? I hired you to render him impotent..."

    suzume "Yeah, well, chopping one's manhood off tends to do that."

    "Male voice" "*gulp*"

    "Male voice" "Alright, if that's what it takes... But you will do this for half-pay!"

    "Male voice" "I've had enough of your failures!" with vpunch

    suzume "..."

    suzume "I shall do it for free. I have failed twice. I never failed before. My honor, and the honor of my school depend on me seeing this contract through."

    "Male voice" "For... free?"

    suzume "Yes."

    "Male voice" "Well... Very well, then, fufufu..."

    "Male voice" "Make him bleed! Cut his dick off!" with vpunch

    suzume "So be it..."

    suzume "(Such a waste, though...)"

    "Male voice" "Just make sure to stop the bleeding afterwards, cauterize it or something... I enjoy making fun of cripples, I mean, don't we all, but I don't want to be an accessory to murder."

    $ calendar.set_alarm(calendar.time+4, StoryEvent("c2_suzume_invitation2", type = "night"))

    return

label c2_suzume_invitation2():

    scene black with fade
    show bg street at top with dissolve

    play sound s_wind

    "As you walk back towards your brothel for the night, a big gust of wind engulfs the street."

    "A lone flyer glides in the air, as if aimed right towards you. It hits your chest, then lands softly at your feet."

    you "What's that?"

    play sound s_dress
    show bg letter at top with dissolve

    "Cautiously picking up the flyer, you quickly recognize the letterhead. It's from 'The Dark Serpent', one of the most upscale hostess clubs in the lower city."

    you "Free coupon for the Dark Serpent: Meet our most beautiful courtesan. You'll have the time of your {i}life{/i}."

    show bg street with dissolve

    you "The Dark Serpent club... Interesting."

    "You've heard it is a very selective club catering to the wealthiest clients of the lower city. Some of the big names from the upper city even visit from time to time."

    "Its imposing building is a familiar sight by the seafront. You've heard it's got all sorts of kinky rooms in there..."

    you "Someone must be upset to have lost this. Nevertheless, looks like a unique opportunity to sample the competition..."

    you "I might check it out later."

    "Visit the {b}Seafront{/b} to enjoy your free night at the Dark Serpent."

    $ game.set_task("Visit the upscale hostess club by the {b}Seafront{/b}.")
    $ story_add_event("c2_suzume_brothel")

    return


label c2_suzume_brothel():

    "You decide it's time to use the free hostess club coupon that you found in the street."

    scene black with fade
    show bg dock at top with fade

    you "I've seen the place before... There it is."

    "The Dark Serpent overlooks the seafront, its elegant architecture a mix of traditional Zanic features and more eccentric influences."

    you "I've heard they have over twenty rooms here, and no two are the same..."

    play sound s_chimes

    show bg desk at top with dissolve

    "You enter the lobby. An elderly majordomo mans the desk. He seems to take an instant dislike to you."

    "Receptionist" "Ahem, Sir, the taverns are further down the docks. Go back to the street, then take a right..."

    you "I know where I am. This is the Dark Serpent, isn't it?"

    "The old man stiffens."

    "Receptionist" "Indeed it is, we are the most upscale, and shall I say, {i}expensive{/i} entertainment this side of the inner gates. And I don't think you..."

    you "I have a voucher. See?"

    "You brandish the flyer under his nose. He picks it up with obvious distaste, between two fingers."

    "Receptionist" "We don't just give vouchers to..."

    "He frowns."

    "Receptionist" "Well, it is the Manager's seal..."

    "Out of the blue, the receptionist breaks into an obsequious smile."

    "Receptionist" "As our esteemed guest, you are most welcome to our humble establishment. We will do our utmost to make this the best night of your life."

    "His sudden mood change is even more unsettling."

    "Receptionist" "Your invitation gives you access to the Deluxe bedroom on the top floor. There are no other rooms on this floor, so you will be able to go about your business discreetly."

    "Recptionist" "(And not scare the other customers away, hopefully.)"

    you "What was that?"

    "Receptionist" "Nothing. Follow me, Sir."

    show bg room at top with fade

    "The old man leads you up a flight of grandiose stairs, past a couple of expensive paper sliding doors. Beyond lies a richly decorated room with lacquered flooring and a fancy king-size futon."

    you "Nice... *whistle*"

    "The rich scent of incense and rose's oil tickles your senses. The room opens on a large moonlit balcony which overlooks the whole district."

    you "What an awesome view..."

    "Receptionist" "Your companion shall join you shortly. Please make yourself comfortable."

    "You heave a sigh of relief as the grumpy majordomo leaves."

    you "Well... I might as well get ready."

    "You take all of your clothes off, and lay down on the silk sheets."

    you "If the girl matches the decor, I'm in for a treat..."

    "You can already feel the excitement as you get ready to meet the mysterious courtesan."

    "The room is warm, but a light scented mist starts filling the air from a vent mechanism, giving you a delicious chill."

    you "I'm getting hard already..."

    "After a moment, the first sliding door opens with a smooth sound, and a woman's silhouette appears in the entrance. "

    "You can only see her through the paper door as she prepares herself. Somehow, it makes the whole thing even more exciting."

    you "Even from here, I can see how shapely she is... A petite silhouette... Firm, athletic body..."

    "Your imagination is running wild, and you start feeling really horny. You hear some clanging sounds as the woman prepares herself."

    you "Jewelry, no doubt... I wonder what she'll be wearing?"

    you "I can already picture it: A silky, see-through blouse that leaves nothing to the imagination... I wonder what underwear she'll be wearing?"

    "Your dick is now rock-hard as you indulge in your fantasy."

    "You're also starting to feel light-headed. Sniffing a bit of the mist, you feel both extremely horny and more than a little dazed."

    you "It does smell a bit strange... Hmm..."

    "The woman is finished preparing, and she slowly opens the screen. As she advances into the light, you get your first good look at her."

    you "Hey... You look... familiar..."

    play music m_suzume fadein 3.0
    show bg suzume_brothel1 at top with dissolve

    suzume shrewd "We meet again! [MC.name], my nemesis... PREPARE TO DIE!"

    if story_flags["panties trap"]:
        you "Okay, I think I've got it figured out now! This is a trap! You're an assassin!"

        suzume "Good guess, [MC.name]. It's a little too late for you, though..."

    else:
        you "Hey! You're Suzume, the nympho girl from the forest! So it is you? The Dark Serpent's best courtesan?"

        suzume "This is just a disguise, you idiot! I am an assassin!"

    "Even though your mind is getting foggy, you notice she is holding a couple of short blades made of the best steel and covered in runes..."

    if story_flags["panties trap"]:
        you "This mist is some kind of narcotic... I'm being drugged... And why do I feel so hot?"
    else:
        you "So this is the kinky scenario we're playing today, uh? A slutty assassin coming to skewer me... Only she gets skewered back..."

    "She ignores your rambling as she walks slowly towards you."

    suzume "The mist you're breathing is dulling your senses, it drains your will to fight back..."

    "She steps forward menacingly. As she comes into the mist, her dress becomes wet and clings even more to her perfect shapes."

    show bg suzume_brothel2 at top with dissolve

    you "Ooooh..."

    "Your cock was already rock-hard, but it seems to grow even more in size. Suzume lifts an eyebrow."

    suzume "Well, it has the side-effect of being an aphrodisiac... Still, your stamina is amazing."

    suzume "No one has ever bested me in a sexual battle, but you did. Not once, but twice! Your dick is a formidable opponent..."

    "She tightens her grip on her blades, and lifts one over her head, ready to strike."

    suzume "It gives me no pleasure, but I have to resort to cruder weapons to carry out my contract. For the honor of my school... I'm sorry, [MC.name]."

    suzume "It's nothing personal. Say goodbye to your willie, Mister [MC.name]."

    you "No!!! Wait!!!" with vpunch

    suzume "Uh?"

    if story_flags["panties trap"]:
        you "Before you put me to the sword... There is something I must know."
    else:
        you "This scenario is getting very realistic, and I do feel a bit light-headed... But there is something I must know."

    suzume "A doomed man's wish... I cannot but grant it."

    you "What..."

    you "What are you wearing under your blouse???" with vpunch

    play sound s_surprise

    suzume normal "Uh?"

    you "Your panties! Show me!"

    suzume doubt "Well, I wear nothing, of course... Underwear hinders movement, and I can't have that. Look!"

    with dissolve

    pause

    with dissolve

    "She lifts her blouse, and you can see she isn't lying. From your futon, you get a perfect view of her moist slit."

    "It seems the mist is having an effect on her too. Your nose starts bleeding."

    you "(This... This is TOO MUCH!!!)"

    you "Uuuh..."

    suzume shrewd "Now, prepare to... Uh?"

    you "UUUUAAAAAAAH..."

    with flash

    you "UAAAAAAAAAAAAAGGGGH!!!"

    show bg suzume_brothel3 at top with doubleflash

    "Unable to contain yourself, you explode point-blank on Suzume, covering her body, clothes and blades with an eruption of thick semen."

    with flash

    suzume "..."

    "She watches in amazement as your cock releases an inhuman amount of cum."

    "The murderous glint in her eyes dims, and changes to something different, yet equally ravenous."

    suzume "Such a... Such a..."

    suzume normal "Such a MAGNIFICENT DICK!!!" with vpunch

    play sound s_clang

    "She drops her weapons to the side."

    suzume "I can't kill that perfect dick! It would be a crime!"

    "She rips her blouse off."

    suzume naked "YOU! Owner of the perfect dick! FUCK ME!"

    you "Uh? You don't mean to maim me after all?"

    suzume "NOW!" with vpunch

    stop music fadeout 3.0

    show bg suzume_brothel4 at top with fade

    "Suzume lands on top of you like a frenzied she-wolf. Before you know it, you are both fucking with abandon."

    play sound s_moans

    "As usual, you and Suzume have amazing chemistry."

    suzume "Oh yes, [MC.name]! Fuck me! Ravage my worthless pussy!" with vpunch

    you "K-Kinky..."

    you "Don't call yourself worthless, though... You're amazing... (One of the the best pussies I've had in years!)"

    suzume "Aah, but I have failed in my task... I am finished as a ninja..."

    you "A ninja? So this is, mmh... This is really what you are?" with vpunch

    suzume "(Hmm, harder, yes!) That's what I was. But by letting my mark escape with his dick, I am betraying my contract, my client... And my school's master..."

    you "Thats, ugh... Tough... "

    suzume doubt "Well, I never liked that job anyway, and that pompous asshole... Riding your dick is a lot better than carrying out old men's bidding!"

    suzume normal "I'm only nineteen, anyway... I've got lots of time to figure out something else to do with my life! (Aaah... Keep doing that...)" with vpunch

    you "Oh, I'm close... Suzume..."

    suzume "[MC.name]... Aaah... YES!!!"

    with flash

    show bg suzume_brothel5 at top with doubleflash

    "You cum inside her again, the first of a long series..."

    show bg room with Fade(0.5, 1.0, 0.5)

    "Hours later, when you are both fully satisfied, she lies down on your chest and breathes a deep sigh."

    play music m_zan fadein 3.0

    show suzume naked
    play sound s_sigh

    suzume "I have given up my life as a kunoichi, and spared you, just so I can enjoy your dick..."

    suzume "You owe me, pal! You better give it to me anytime I ask!"

    you "S-Sure..."

    you "Wait? What did you say?" with vpunch

    suzume "I said, 'you better give me your d..."

    you "No, the other part! did you say, 'kunoichi'?"

    suzume "Oh, that? Yeah, a kunoichi. That's what I am... was."

    you "So you're in league with the murderer!!! The masked dude!" with vpunch

    play sound s_surprise

    suzume "Uh?"

    you "Tell me the truth! Why do you plan on killing all those lords and officials in the higher city!"

    suzume "Are you high? I thought the psychedelic mist had run its course by now..."

    you "Don't try to fool me! The masked man works with the kunoichi, and you're part of the kunoichi, aren't you?" with vpunch

    suzume "Calm down! Oh... I think I see what this is about. Silly you!"

    you "Uh?"

    suzume "The kunoichi is not an organization, we're individuals."

    suzume "I know of at least three others working in Zan, not counting myself. One or several of them could be in league with your masked whatever, but not me."

    you "Who do you work for, then?"

    suzume "Hmph. That's a professional secret, and I won't fall so low as to..."

    you "Is it Kosmo?"

    suzume "..."

    suzume "Yeah. It's Kosmo."

    you "Damn! I'm going to get back at the bastard..." with vpunch

    suzume "Forget it! No one must know I spilled the beans, I can live as a failure, but not a traitor! Got it?"

    you "Hmph... Okay... We've got more pressing matters, anyway."

    you "Can you help me locate your colleagues? I will need to get to the bottom of these murders... My standing with the princess is on the line."

    suzume "Is that so? And why do you care?"

    menu:
        "I want to help her":
            $ renpy.block_rollback()
            $ MC.good += 1

            you "She may be a princess, but she's also a good woman. I want to help her."

            suzume "Ooh, I see, you've got a crush on her, haven't you?"

            suzume "Well don't worry, I'm not jealous, as long as your dick is not monogamous..."

        "I need the power":
            $ renpy.block_rollback()
            $ MC.good -= 1

            you "I can use the influence to advance my standing in the city. It's simple, really."

            suzume "Cold, calculating... That's my guy! I think you've got what it takes. Don't forget me when you're rich, okay?"

        "None of your business":
            $ renpy.block_rollback()
            $ MC.neutral += 1

            you "And that's none of your business."

            suzume "Ooh, burn... Well, you don't have to tell me anything. I'm good at finding out... *wink*"

    you "So. Will you help me solve these cases?"

    suzume "Well, you're more likely to get to the bottom of the harbor with some iron shackles but... Fine. I can help you."

    suzume "We'll discuss it tomorrow at your place. But first..."

    play sound s_moans
    scene black with fade

    you "Again!?!"

    "Suzume doesn't let you escape so easily. After she's done with you, you wonder if you didn't escape mutilation to die from oversex after all."

    $ MC.interactions = 0
    $ MC.change_prestige(2)
    $ unlock_achievement("h suzume")

    "You have spent all of your actions for the night."

    $ calendar.set_alarm(calendar.time+1, StoryEvent("c2_suzume_morning_visit", type = "morning"))
    $ game.set_task("Wait for Suzume to come back.")

    return


label c2_homura_city_meet():

    scene black with fade
    show expression bg_bro at top
    with dissolve

    "One morning, as you open your window, you spot a familiar figure that looks out of place in [district.name]."

    play music m_palace fadein 3.0

    show homura with dissolve
    you "Hey, Lady Henso!"

    play sound s_surprise

    homura surprise "Uh?"

    homura normal "Oh, Mister [MC.name]. Nice to see you again. So this is where you live?"

    you "Yes, for the moment at least. Would you like to come in for tea?"

    homura "Of course!"

    scene black with fade

    if brothel.get_common_rooms():
        $ room = brothel.get_random_room_pic_path()
    else:
        $ room = "black"

    show expression room at top
    with dissolve

    "Welcoming Lady Henso inside [brothel.name], you send Sill to the kitchen to fetch some tea."

    homura "Oh, my, lovely interior you have here... It's quite... rustic. I mean it in a good way, of course!"

    you "Well, yeah. I've only recently moved to the city, still getting my bearings..."

    homura "Good for you! As a noble woman, I never get to travel anywhere... You must tell me more about your adventures!"

    you "Well, at least you seem to be able to travel within Zan. What brings you to the lower city?"

    homura "Well, I'm not really supposed to leave the manor, but... The lower city is sooo exciting! The people, the sights... It's so different from court, you know!"

    you "It's funny. Most people want to get into the higher city, not the other way around."

    homura "Not me! Everyone is assigned to their own place in the city. But I believe a real adventurer should break those barriers and go wherever she pleases!"

    menu:
        homura "Don't you agree?"

        "Sure":
            $ renpy.block_rollback()
            you "Sure. Class is an artificial social construct that is the outcome of centuries of subjective thinking, ontologically undifferentiated from vulgar prejudice and superstition."

            "She blinks."

            homura "Uh... Yeah. Sure..."

            you "Nothing should stop you from mingling with the lower class, just like an outsider like me should be able to reach the top! Right?"

            homura "Hahaha, right! That's the spirit. *smile*"

            $ NPC_homura.love += 1

        "No way":
            $ renpy.block_rollback()
            you "No, not really. The aristocrats should keep separate from the plebs."

            you "Otherwise, social distinctions will become blurred, and soon enough, people will start to question our most hallowed institutions, such as absolute monarchy or sex slavery or public executions..."

            "She frowns."

            homura "Oh, boo-hoo!!! You sound just like my father!"

            homura "I didn't think you would be so old-fashioned. Anyway, regardless of what you think, I will live my life to the fullest."

            you "Well... I was just saying..."

    "She pauses for a moment."

    homura "Say, Mister..."

    you "Call me [MC.name]."

    homura blush "... [MC.name]. I couldn't help but notice the sign outside. Is this a..."

    you "A?"

    homura "A... House of ill-repute?"

    you "Err... I prefer not to call it that..."

    "Sill enters the room with a teapot. She looks at Lady Homura sideways."

    homura "And this girl, is she, a... a... I believe you'd say, 'soiled dove'?"

    "Sill overheard and is frowning, but she keeps quiet."

    you "Her? Oh, no, no... She's just my slave Sill."

    "Lady Homura looks slightly disappointed."

    homura normal "Oh, I see."

    homura "You must forgive my ignorance, I've only read about these places in... in some of the seedy books my father kept on top of his bookshelf."

    homura "I imagined those places would be a lot more dirty and disgusting, though..."

    you "Well, I pride myself in keeping everything neat and tidy. I mean, Sill does, but I am the one barking orders at her, so I think the merits are really mine."

    homura blush "This place, though... It must get really different at night, right? Such debauchery... I can barely imagine it... Mmh..."

    you "It's not that bad... You'd be surprised! You should see the Okiya, where the geishas work. They dress and talk like high-born ladies, the customers love it..."

    homura "Like... high-born ladies?"

    "She blushes."

    homura "My... I had no idea we were the objects of men's fantasies..."

    you "Oh, you definitely are! Trust me, I know."

    "She blushes even more. Sill grumbles something and excuses herself."

    you "Why not come to visit one night? I could give you a tour."

    play sound s_surprise

    homura surprise "Really? That's a tempting offer... I'm so curious about the world you live in!"

    homura blush "But I'm not allowed to go out at night... I'd have to slip through undetected... Use the sewers, maybe.."

    you "Ah, yeah, okay. Forget it, then..."

    homura normal "On the contrary! Sounds like an adventure! Count me in... I shall visit your Okiya!" with vpunch

    you "Err... All right, then."

    homura "It's a date! See you next time, then..."

    stop music fadeout 3.0

    "You wonder how an innocent noble girl can be so enthusiastic about smut. She's nice to talk to, though."

    $ story_add_event("c2_homura_okiya1")

    return


label c2_homura_okiya1():

    # Occurs if the player has an okiya

    show expression bg_bro at top
    with fade

    "As the sun starts to set and the first red lamps are lit in the street, you take some time to inspect your brothel."

    you "Everything seems to be ready... The first customers should be here soon."

    "Woman" "Ahem. Mister [MC.name]?"

    you "Yes?"

    play music m_palace fadein 3.0
    show homura with dissolve

    homura "Good evening! How are you? I was in the neighbourhood and saw you were open, so I figured I'd come and say hello..."

    homura blush "But perhaps you're too busy? I apologize, I shouldn't have barged in like that..."

    you "Not at all! I promised you a tour, didn't I? This is as good a time as any."

    you "The customers are going to come soon... You should stay close to me, I don't want them to think you're one of the service girls."

    homura "Oh! *blush*"

    you "Not that they would, of course, you're much too classy for that... Haha..."

    homura normal "So this is the calm before the storm... My father would kill me if he knew I was visiting this place!"

    you "Well, you are venturing quite far from the palace. How come you want to visit such a lowly place, anyway?"

    homura "Because! This is real life, isn't it? This is what ordinary people do, isn't it? I want to learn about the world..."

    menu:
        "I understand you":
            $ renpy.block_rollback()
            you "I understand. Seen from the palace towers, the women and men of Zan must be more like ants than real people..."

            homura surprise "Exactly. That's what makes it so easy for the higher-ups to step on them."

            "Her voice became harsher, but she quickly recovers her composure."

            $ NPC_homura.love += 1

        "I don't understand you":
            $ renpy.block_rollback()
            you "I don't get it. You've got everything you could want for up there. Why bother with ordinary people?"

            homura blush "You don't understand... A golden cage is a cage all the same. Sometimes, destiny locks you in..."

            "She seems a bit distant for a moment, but quickly recovers her composure."

            $ NPC_homura.love -= 1

    you "Nevertheless, the city can be dangerous at night. I'm not sure you should act so carefree..."

    if MC.playerclass == "战士":
        $ text1 = "mighty warrior"
    elif MC.playerclass == "法师":
        $ text1 = "grand wizard"
    elif MC.playerclass == "奸商":
        $ text1 = "charming rogue"

    homura normal "Oh, but surely I will be safe here! Escorted by [MC.name], [text1], and good friend of the Princess!"

    "She smiles and takes your arm."

    homura "Now, you promised me a tour, didn't you? Let's go!"

    you "Sure..."

    scene black with fade
    show bg okiya with dissolve

    show homura with dissolve

    you "...and this is the last room, the Okiya. Here, we organize tea ceremonies, and some other forms of entertainment for our guests..."

    homura "Wow. This definitely has more cachet than the rest of the place."

    you "Yes, I'll give you that. All kinds of gentlemen come to this place, you know..."

    homura blush "But still... Naughty stuff happens here too, right? *blush*"

    you "Well, not really... This section is only for entertainment. It can get a bit rowdy, but... Not like you imagine."

    homura normal "Oh."

    "You cannot tell if it is disappointment or relief that you hear in her voice."

    you "Since we're here, would you like to share a drink?"

    homura "With pleasure..."

    scene black with fade
    show bg homura_okiya sad at top with dissolve

    homura "So. Does the princess know you operate... such a place?"

    if NPC_kuro.flags["occupation"] == "truth":
        you "Indeed. In the end, it seems that didn't deter her from trusting me."

        homura "Yes. That's a bit surprising of her, she's always such a good girl..."

    else:
        you "Err... Not exactly. It's not really something she needs to know, you know?"

        homura "Eh. She doesn't know the people she surrounds herself with. Typical."

    "You detect a hint of sarcasm in her voice."

    you "But you're friends, right?"

    show bg homura_okiya serious at top with dissolve

    homura "Of course! Childhood friends! She's a good person. It doesn't mean we are one and the same, though."

    you "So... You're not a good girl?"

    homura blush "I-I... *blush*"

    "She quickly changes the subject."

    homura normal "So the princess granted you an audience, even though she has so little time! She doesn't even take time to meet with her dear friends anymore..."

    you "Yes, I guess she's all absorbed with her duties these days."

    show bg homura_okiya happy at top with dissolve

    homura "So it was about her duties! Did she request your help? How strange, given your occupation..."

    homura "You know, if it's something about the court, I'm sure I can help you! I know everyone, and every bit of gossip..."

    menu:
        "Tell her about the Princess's request":
            $ renpy.block_rollback()
            $ NPC_homura.flags["divulged assignment"] = True

            "You hesitate for a second, but you do need all the help you can get."

            you "Well, I might as well tell you. She wants help investigating the murders in town."

            homura "The murders... You mean, the high-ranking officials that have been killed recently?"

            you "Yes. I've established that the murderer was helped by one or more female ninjas, called the kunoichi."

            homura "The kuno... what?"

            you "The kunoichi. Female ninjas."

            homura "Ooh, it's just like an adventure novel! Mysterious organizations, crime, danger at every turn..."

            "She's way too giddy given the seriousness of the situation."

            you "This is serious. People have died, and more might soon... *gulp*"

            homura "Well, thank you for leveling with me..."

            homura "I'm sure I can help you! I don't know a thing about the... kurochichi, was it? But if they've been hired it must be by one of the wealthy families plotting against the throne..."

            homura "And I know all of them. I'm sure I can keep my ears open for interesting information. There's nothing like long, inebriated parties at my Dad's mansion to loosen lips..."

            you "Thanks. That would be useful."

        "Don't tell her":
            $ renpy.block_rollback()
            $ NPC_homura.flags["divulged assignment"] = False
            "You remember the Princess requested you keep your assignment secret."

            you "That's nice of you, my Lady... But I'm not at liberty to divulge this information."

            show bg homura_okiya serious with dissolve

            homura "Ooh, it must be pretty important! Now you got me even more curious..."

            homura "But I'm not one to snoop. Maybe I'll ask the Princess next time, she wouldn't keep that a secret from me."

    show bg homura_okiya sad at top with dissolve

    homura "But look at the time... I have to hurry, before my Dad's guards figure out I've skipped out on them."

    you "Will you be okay finding your way back at night?"

    show bg homura_okiya happy at top with dissolve

    homura "Sure! Look, thank you for showing me around. I've enjoyed this evening tremendously. Can I come back, one of these days?"

    you "Of course. You're always welcome."

    homura blush "Thank you, [MC.name]! See you..."

    stop music fadeout 3.0
    show bg okiya with fade
    show sill sad with dissolve

    "After Homura takes her leave, Sill comes to you unexpectedly. She looks concerned."

    sill sad "Master, I noticed you invited that little lady from the other day..."

    "Sill and Homura are about the same height."

    you "She's no smaller than you are."

    "Sill bites her lip, then blurts out."

    sill sad "Master, don't trust that shifty ingenue! I don't like the way she looks at you..."

    you "What's the problem?"

    sill "She's a little too... interested in you... Staring. It's odd, right?"

    sill "Anyway, she's just a noble brat! She doesn't belong in our place!"

    you "'Our' place?"

    menu:
        "Cajole Sill":
            $ renpy.block_rollback()
            $ MC.good += 1
            $ NPC_sill.love += 1

            "You pat Sill on the head."

            you "Always worried about something, aren't you? Come on, I'm not going to let a little doe-eyed aristocrat turn my head so easily, right?"

            sill happy "Oh, Master..."

            you "Especially since I have one right at home."

        "Scold Sill":
            $ renpy.block_rollback()
            $ MC.neutral += 1
            $ NPC_sill.love -= 1

            "You frown."

            you "What are you rambling on about. Did I ask you for your opinion?"

            sill "No, Master, but..."

            you "So quit yapping, and go do something about that sick customer. I don't want him puking on my tatami!"

            sill "Aw..."


        "Punish Sill":
            $ renpy.block_rollback()
            $ MC.evil += 1
            $ NPC_sill.love -= 2

            "Without a warning, you hit Sill in the back of the head."

            play sound s_scream

            sill sad "OUCH!" with vpunch

            you "You DARE come to me and insult my guests? You forget your place!"

            sill "I'm sorry, Master..."

            you "You'll be sorry, all right! Tonight, you'll sleep in the yard like a dog... Naked! With a leash!"

            hide sill with dissolve

            play sound s_scream_loud
            show bg sill_floor_naked at top with dissolve

            "You rip her clothes off, leaving her naked on the floor."

            $ seas =  calendar.get_season()

            if seas in ("winter", "fall"):
                sill "B-But... It's cold outside! It's [seas]!"
            else:
                sill "B-But... Even though it's [seas], it's..."

            you "You should have thought about it before blurting out your opinion without permission, slave! Off with you, now!"


    you "I know what this is about, anyway... You're salty because you're a high-born girl too!"

    sill "What?"

    you "Do you think I forgot that your parents were nobility? Formerly a great family, now broke aristocrats that ended up selling their daughter to a stranger, for a hundred denars?"

    "Sill grows pale, and her eyes well up."

    sill "You... You're... "

    play sound s_scream

    extend "A MEANIE!!!" with vpunch

    show bg okiya
    hide sill
    with dissolve

    "She runs out, sobbing."

    you "Maybe I went a little too hard on her... Oh well. She's a slave now. She has to come to terms with it."

    return

label c2_suzume_morning_visit():

    scene black with fade

    show expression bg_bro at top with dissolve

    "Late in the morning, you are standing just outside your porch, enjoying the soft breeze."

    play sound s_wind

    suzume "Heya!!!" with vpunch

    hide expression bg_bro
    show bg suzume_roof at top
    with dissolve

    you "BWAAH!" with vpunch

    suzume "Surprised you! Kukukuku..."

    you "You nearly gave me a heart attack! Do you always sneak up on people like that?"

    suzume "Well, it's kind of my job, after all... Or was..."

    hide bg
    show expression bg_bro at top
    with dissolve

    play sound s_dodge

    show suzume bend with easeintop
    show suzume bend at jumping:
        yalign 1.0

    "Suzume leaps down from the roof with feline grace. For the hundredth time, you wonder how her skimpy outfit can hold it together."

    suzume "Thanks to you, I'm a disgraced Kunoichi now. And a lot of people are going to be cross with me. *pout*"

    you "Come on, why don't you start over from the beginning. I have so many questions."

    suzume doubt "Well... Ask away! It's not like I have a lot of other things to do."


label c2_suzume_morning_visit_menu():

    menu:
        extend ""

        "Who are you?":
            you "Who are you, really?"

            play sound s_surprise

            suzume doubt "I'm Suzume... Do you always forget a girl's name after a night of steamy-hot sex? *frown*"

            you "I know your name, silly. But I don't know much about you. Where are you from? What's your story?"

            suzume normal "Ha! My story would fill a hundred books, and inspire a hundred songs! And none of them would be fit for children."

            you "Come on. You're young. You can't have lived through that much."

            play sound s_laugh

            suzume bend "Oh, but I did do many things in my short life... Because I'm fast! Swift like the wind! Kukukuku..."

            you "Ugh... Is this supposed to be funny?"

            suzume normal "Of course it is! Because I'm from the School of Air, you see?"

            you "The School of Air? Is that the name of your dojo? That would explain why you seem to command wind..."

            suzume "Yup. Easy beginner technique, you don't even need a strong magic affinity to master it."

            suzume doubt "Which is good, because I always sucked at those magic lessons anyway..."

            you "Focus. Start from the beginning..."

            suzume normal "Well, it's a little blurry, really. My earliest memories are from the monastery where I was raised, north of the Arik Mountains."

            you "You were raised in a monastery? You, of all people?"

            suzume "Yes. See, I had no parents or family, so the monks took me in."

            you "What happened to your family?"

            suzume doubt "Uh? What do you mean?"

            you "Your parents! What happened to them?"

            suzume normal "I just told you. I had no parents."

            you "Everyone has parents!"

            suzume doubt "Uh? Do they?"

            you "Of course!!!" with vpunch

            suzume "Now that you mention it, it seems like I've met an awful lot of people who had parents... Maybe it wasn't such a coincidence, after all."

            suzume bend "I see! People have parents, but I don't! So I must be really special!" with vpunch

            you "..."

            you "Are you telling me you don't know anything about your parents, and you've never even realized you had some?"

            suzume "I'm special, kukukuku... Lalalalala..."

            you "(Okay... I think I'll leave this one to her therapist.)"

            you "So... You said you were raised by monks."

            suzume normal "Right! The monks wanted to make me one of theirs once I got older, but eventually it dawned on them that maybe I wasn't nun material."

            you "And why is that, I wonder..."

            suzume doubt "I think it must have been after I was caught giving one of the novices a blowjob behind the altar... for the third time in a week."

            you "You... What?" with vpunch

            suzume bend "Well, you see, I've always had a healthy sex drive. Some people would say 'too healthy'. [emo_heart]"

            suzume doubt "The monks sometimes said it was because of my 'animal instincts', and whispered something about cats in heat, but I never really got their point."

            you "..."

            you "You don't overthink things a lot, now, do you?"

            suzume normal "Kukuku, you really know me! Thinking is exhausting. I'd much rather jump around, have sex, or lie down on the roof soaking up the sun..."

            suzume "Just don't get a cucumber near me. I hate those."

            you "Anyway *sigh*. Let's move on with your story."

            suzume "Well, the monks soon decided that I was a hindrance to their 'ascetic' and 'chaste' training, although I'm not sure what those words mean."

            jump c2_suzume_morning_visit_menu

        "How did you become a Kunoichi?":
            you "So, how did you become a ninja?"

            suzume "So I was living in a monastery. Up in the mountains, there was a secretive place that occasionally traded with the monks in the valley."

            suzume normal "One day, the monastery was visited by this really old guy. He might have been like, over forty."

            suzume "As he chatted with the monks, I heard them mention my name, and the geezer was looking at me in a way that made me uncomfortable."

            suzume "Later that day, I was told to pack my belongings and go with him. So I did."

            you "You didn't ask where he was taking you, or why?"

            suzume doubt "Hmm, good point. I probably should have asked those questions. Haha."

            you "..."

            you "You {i}really{/i} don't like to overthink things..."

            suzume normal "So I followed the old man. Turns out, he was the master of a ninja school!"

            you "I kind of guessed that already."

            suzume "At the school, I met other young ones who trained to become ninjas."

            suzume "Every one of us was trained in the way of the School of Air. We were taught fighting and assassination techniques, spying, some magic, even politics..."

            suzume "The training was grueling, seven days a week, and not many could withstand it. A majority of the trainees left, sometimes of their own volition, and sometimes kicked out because they were bad or lazy or crippled..."

            you "But you made it through?"

            suzume "I more than 'made it through'! I became the Kunoichi for the School of Air. It's the school's highest honor!"

            suzume "So Kunoichi was the title I held. Until yesterday, anyway."

            you "Why did they pick you?"

            suzume doubt "Well, you see, I was the best at my weapon of choice. Not all weapons have blades or arrows, you see..."

            you "I don't get it."

            suzume bend "Pussy, my dear! Pussy is a weapon, some say the best of all."

            you "You mean... Convincing men that they need to make peace, using sex?"

            suzume "Of course not, silly! MURDERING them with my pussy!" with vpunch

            you "*gulp*"

            suzume "School training fashioned my body into a weapon. The master used many secret techniques to enhance my body, some involving herbs and poisons, some involving bizarre machinery and massage instruments, some involving magic and dark rituals - and a lot, {i}a lot{/i}, of porn reading."

            suzume normal "But worst of all..."

            suzume "I was forbidden from having sex, the whole time!!!" with vpunch

            you "You were?"

            you "Well, considering the staggering amount of fucking we've done in the short time I've known you, that must have been hard on you."

            suzume "It was {b}HELL{/b}!!!" with vpunch

            suzume normal "You can imagine my 'relief' when I got out of that damn school."

            you "Yeah. I can almost picture it."

            suzume "I could finally have all the sex I wanted! But there was one problem..."

            you "What was it?"

            suzume doubt "Well, because of my training, everyone I had sex with ended up either dead or maimed. Found that out the hard way."

            you "*GULP*"

            suzume "So I ended up sleeping only with my marks. Which wasn't very fun, especially since most of them were old and creepy dudes."

            suzume normal "Honestly, that job was pretty lame. Not a big challenge at all. Any street hoe could give a seventy-year-old court official a heart attack. No offence to your pensioners, of course..."

            suzume bend "Until I met you! This is the single most interesting thing that happened since I became a Kunoichi."

            suzume "Finally, I've met my match! And you have yet to succumb to our lovemaking."

            you "'Yet'?"

            suzume shrewd "I'm taking bets with myself on how long you'll last... As long as possible, I hope!"

            you "..."

            jump c2_suzume_morning_visit_menu

        "What are the Kunoichi?":
            you "Tell me about your order, the Kunoichi."

            suzume normal "Order? The Kunoichi is not an order. We each hail from different ninjutsu schools."

            suzume "Every generation, a female ninja is chosen by her school to be its Kunoichi... It's a sacred role."

            you "So not all female ninjas are Kunoichi?"

            suzume "No! But the general public cannot usually tell the difference. I blame mangas."

            you "What makes the Kunoichi special?"

            suzume "Well, they're the best of the best in their school. Deadly efficient in all ninja arts."

            suzume "Also, they must be 'a perfect embodiment' of their school's element... Mine is Air, so I follow the Path of the Wind."

            suzume doubt "I guess that must be why people always called me an airhead..."

            you "That's not... Oh well."

            you "How many elements are there?"

            suzume "Four! I mean, five. Or was it seven? No, wait, there are more schools than that... But some revere 'aspects', and not elements... And let's not forget the Void School..."

            suzume bend "Actually, I haven't got the faintest idea! *smile*" with vpunch

            you "..."

            you "Anyway. Why are the Kunoichi all women?"

            suzume doubt "Well, the prophesy says that one day, a Kunoichi shall be seeded, and give birth to the ninja master who will unite all the ninja schools..."

            suzume "That's why we're all taught some potent contraceptive spells. Wouldn't want to pop a prophesied child after a drunken tavern orgy..."

            you "So you Kunoichi don't know each other?"

            suzume doubt "Well, there are sometimes gatherings, rituals, fan conventions, but..."

            suzume bend "I never went to any of them! It sounded boring. *smile*"

            you "..."

            you "(Some great informant I've found here...)"

            suzume doubt "But I know many of them by reputation. The most gifted are famous all around Xeros, in ninja circles anyway."

            you "Are there any in Zan?"

            suzume shrewd "Well, this is where it gets interesting... I know of {i}three{/i} other Kunoichi in Zan at this very moment, and all of them are famous!"

            you "Three? And at least one of them is in league with the masked killer... *gulp*"

            jump c2_suzume_morning_visit_menu

        "Who are the Kunoichi in Zan?":
            you "Tell me about the other Kunoichi."

            suzume normal "There are three of them in Zan. Any one of them could be in league with your killer... Of perhaps all of them."

            you "Let's not get ahead of ourselves. Who are they?"

            suzume "Well, I don't know them personally, but I know a little about them."

            suzume "They are the Kunoichi from the Earth School, the Kunoichi from the Water School, and the Kunoichi from the Void School."

            $ suzume_loop_menu = True

            while suzume_loop_menu:

                menu:
                    you "Tell me about the Kunoichi from..."

                    "The Earth School":
                        you "Tell me about the Kunoichi from the Earth School."

                        suzume doubt "The Earth School Kunoichi... Hmm."

                        suzume "AKA 'the Ninja School Class President'. She is the most cookie-cutter Kunoichi of the three."

                        suzume "She's older than me - about 25 I guess. She's an elite ninja."

                        suzume "I heard she was quite average when she joined, but she came through, simply because she worked harder than anyone else."

                        suzume "Her tenacity was legendary even before she became a Kunoichi. She became the leader of her school after her Master was brutally murdered, or something. Saved the whole School from extinction."

                        suzume "She set an example for her pupils to follow - and even beyond. People in my school were sharing snippets of her wisdom with each other."

                        suzume doubt "'You must be hard as a rock, flexible as a reed', that kind of senpai bullshit."

                        suzume shrewd "She seems strong, and serious, and capable... And boring, if you ask me."

                        you "I see. But what is she doing in Zan?"

                        suzume normal "Beats me! But I heard she can be found in the {b}Warehouse{/b} district."

                    "The Water School":
                        you "Tell me about the Kunoichi from the Water School."

                        suzume doubt "Hmm, water. Not my favorite element."

                        suzume "The Kunoichi from the Water School is shrouded in mystery..."

                        suzume normal "She's one of the oldest living Kunoichi, some say she is over a hundred years old. Imagine that!"

                        suzume "As a spy and an assassin, she has no equal when infiltrating even the most well-defended strongholds, coming and going without anyone noticing. They call her 'The Water Ghost'."

                        suzume "She only picks a handful of contracts a year, if any. Some say she's following her own agenda."

                        suzume "But she is very sought after. She is so good at blending in that no one knows what she really looks like. I guess no one suspects an old lady."

                        suzume "Others say she's a powerful witch, and doesn't age... Which would explain why her mastery of water magic is second to none."

                        you "I see... But why is she in Zan now?"

                        suzume normal "Who knows? Politics, most likely. But it could also be a personal score... You'll have to find out."

                        suzume normal "Anyway, wherever that old hag is hiding, it has to be near water. I'd check the {b}Docks{/b} district, if I were you."

                    "The Void School":
                        you "Tell me about the Kunoichi from the Void School."

                        suzume doubt "Aw, do I have to talk about that little brat? *annoyed*"

                        suzume "The Void Kunoichi, AKA 'Little Miss Ninja Princess'."

                        suzume "The current Kunoichi is the descendent of a long line of ninja warriors, going back all the way to the legendary couple, Ayame and Rikimaru..."

                        suzume "She's said to be the youngest Kunoichi in the history of any school, ever! She became a ninja at age six, and a Kunoichi at twelve."

                        suzume normal "The Void School is a very peculiar school. They teach no magic, instead focusing on physical feats, speed, and secret techniques. People say Void ninjas move so fast, you can only see their shadows."

                        suzume "Their Kunoichi is just a teenager, but already she's said to be one of the most accomplished Kunoichi in history. Not only that, but she won several 'Ninja Idol' contests."

                        suzume doubt "Because she's just a little younger, I was constantly compared to her when I was training - always falling short of the milestones she set."

                        suzume "Well, it's true that I wasn't very focused... But it's not my fault! There were birdies to chase after. Meow..."

                        you "A ninja prodigy, uh? And what is she doing here in Zan?"

                        suzume normal "According to my intel, she's only just reached the city. Probably lurking in the {b}Slums{/b}, outside the walls."

                        suzume "We need to catch her flat-footed before she has a chance to settle in..."

                    "Never mind":
                        you "Okay, enough about the Kunoichi."

                        $ suzume_loop_menu = False

            jump c2_suzume_morning_visit_menu

        "No more questions":
            pass

    suzume bend "So, you know everything."

    you "Wait a second... How am I supposed to catch these highly accomplished Kunoichi? Every one of them is a fierce fighter... Do I stand a chance?"

    suzume doubt "I'm not sure. Let me take a good look at you..."

    suzume normal "Nope."

    you "What do you mean, 'Nope'?"

    suzume "I mean you'll die in a heartbeat in a fair fight with any of them."

    you "B-But, I defeated you, didn't I?"

    suzume bend "That you did! But only because I'm a sex ninja, and that happens to be your natural strength."

    suzume normal "None of the other Kunoichi uses sex as a weapon... They just get their marks using old-fashioned weapons and magic. And this is where you'll fall short."

    you "So... It's hopeless, then."

    suzume "Unless..."

    you "Unless?"

    suzume shrewd "What if I told you there was a weapon that could put you on equal footing with any of those warriors?"

    you "A weapon?"

    suzume shrewd "Yes. A warhammer, to be precise."

    you "Tell me more."

    suzume "It's called..."

    play sound s_lightning
    with flash

    suzume "'The Hammer Of Light'." with vpunch

    you "The... What?"

    play sound s_lightning
    with doubleflash

    suzume bend "The Hammer Of Light!" with vpunch

    you "Did you have to make this so dramatic... *roll eyes*"

    you "What's this hammer? And where is it?"

    suzume normal "I shall tell you, of course... On my next visit."

    you "What? Why?" with vpunch

    suzume doubt "Well, you cannot expect me to simply reveal the location of such a precious and powerful artefact... I need to do some groundwork, cross-check sources, invoke wind spirits, read forgotten prophesies..."

    suzume normal "Also, I'm starving. And I could use a nap."

    you "Of course, have a fucking ball, it's only my life and the fate of the realm on the line... *sigh*"

    suzume bend "Oh, you know what else I could use? A bath!"

    you "What?"

    suzume "Look, I despise water, in general, but I do love me a scalding hot bath..."

    suzume "Say, do you have any hot springs here?"

    you "This is not the issue here! How does that relate to..."

    suzume "So, I'm looking forward to a good hot springs bath... Kukukuku..."

    play sound s_wind
    hide suzume with easeouttop

    you "HEY! Come back here!"

    "Suzume is gone, like the wind..."

    $ game.set_task("Get the onsen, and wait for Suzume.")
    $ daily_events.append(StoryEvent(label = "c2_suzume_onsen", chapter=2, room="onsen", date=calendar.time + 3))

    return


label c2_suzume_onsen(): # Happens at night when the player has an onsen and at least 3 days have passed

    "As the daylight dims and the red lanterns are lit, you stroll around [brothel.name], making sure everything is going well."

    you "Ah, seems like another peaceful night... Wait, what's that noise?"

    play sound s_crowd_cheer fadein 3.0
    show bg onsen at top with dissolve

    "You hear a commotion coming from the hot springs."

    you "Oh no, not another riot..."


    "Rushing towards the source of the noise, you reach the onsen pool. A crowd of cheering customers blocks your view."

    you "Excuse me..."

    "Elbowing your way forward, you spot the source of their excitement, and your jaw drops."

    show bg suzume_onsen at top with dissolve

    stop sound fadeout 1.0

    suzume normal "Oh, hello, [MC.name]!"

    you "Whaaaat?" with vpunch

    suzume "Aaaah, nothing better than a hot bath!"

    "Suzume seems blissfully uncaring about the dozen customers that surround her, howling."

    you "Suzume! What are you doing in my backyard pool, naked, and causing a riot?"

    suzume "Uh? You promised me a hot bath, remember? And your customers don't seem to mind..."

    you "No kidding..."

    suzume "Some of them got grabby, they thought I was one of your whores. Now they're nursing their bloody noses, and the rest are nice enough to give me some space."

    you "Giving you some space? They're touching themselves in front of you!"

    suzume "Well, if it makes them happy, to each their own. Why should I hide my body?"

    suzume doubt "I'd fuck the poor guys, but it would kill them... Sad."

    you "Okay, that's enough! Come out of the bath this instant."

    suzume "Aw, you're so square..."

    play sound s_wind

    "*WHOOSH*"

    play sound s_splash

    you "Aaaah!!!" with vpunch

    "Waving her hand, Suzume summons a gust of wind that shoves you right into the bath."

    play sound s_splash

    you "Gwaah!"

    play sound s_crowd_laugh

    "The crowd laughs as you flounder about in the hot water, wading towards Suzume."

    "When you finally reach her, you are feeling quite mad."

    you "YOU! Listen to me young lady, you're going to..."

    suzume "Bo-o-oring!"

    play sound s_punch
    with vpunch

    you "UGH!"

    "Suzume smacks you on the side of the head, and everything goes black."

    play sound s_splash
    scene black with circlein

    you "Ouch..."

    scene black
    show bg suzume_69
    with circleout

    "When you come back to your senses, you are surprised to feel something warm and wet wrapped around your cock."

    play sound s_sucking

    suzume "Nggh..."

    "You are surprised to find yourself naked, with Suzume's pussy an inch from your face."

    play sound2 s_crowd_cheer

    "The customers are cheering Suzume on. You should feel embarrassed, but you're feeling dizzy, and her technique is too good to focus on anything else."

    "Your instincts kick in, and you start licking her pussy."

    stop sound2 fadeout 2.0

    suzume "Aaah, finally, I prefer you like this..."

    "The little she-devil hungrily sucks you off as if your cock was the most delicious lollipop she had ever latched onto."

    suzume "Mmmmh..."

    "It isn't long before you feel the rush of an orgasm coming. You shove your tongue deep inside Suzume's drenched pussy, pushing her over the edge too."

    suzume "Aaaah! [emo_heart]" with vpunch

    with flash

    play sound s_orgasm_young

    "You cannot hold it anymore, and explode in Suzume's mouth. She cums hard as she feels your cum gushing down her throat."

    with doubleflash

    suzume "NGGGH!!!"

    with flash

    play sound s_crowd_cheer

    "The crowd is pleased with the spectacle you just gave them and cheer."

    scene black with fade

    "Seeing that the show is over, the customers scatter, some of them slipping you and Suzume a tip."

    play sound s_gold
    $ MC.gold += 350
    $ MC.change_prestige(2)

    "You have received 350 gold."

    show bg suzume_onsen at top with dissolve

    "Suzume washes herself as you gather your wet clothes and try to recover some dignity. You try to ignore the fact that she licks herself a lot."

    suzume "Aaaah... Now, that's what I call a relaxing time! I even got some warm milk... *purr*"

    show bg onsen at top with dissolve
    show suzume naked2 with dissolve

    you "Suzume..."

    you "What about your promise? You know, the magical warhammer, and so on?"

    with flash

    show suzume naked2 at jumping:
        yalign 1.0

    suzume "Oh! The Hammer Of Light?"

    you "Stop that. You know the one. Did you find out more?"

    suzume "Yeah, sure. I did some research."

    you "What can you tell me?"

    suzume "Well, the Hammer Of Light stands atop a fiery volcano that taps directly into the center of the earth..."

    suzume "The hellish temperature makes everything melt in a radius of a mile, and no living being can hope to reach it... Except the Great Dragon that lives there, who is a hundred thousand years old and can split a house in half with his paw."

    suzume "He has nigh-impenetrable armor, and a very nasty temper."

    suzume "But none of this matters, until you can reach the island where the volcano stands."

    suzume "It is surrounded by raging seas, with constant storms that wreck every ship that comes within a hundred miles of the island..."

    you "Okay, I get it..."

    suzume "Which is just as well, because the sea monsters... Oh, the sea monsters... You have no idea."

    you "Enough! So... This magical artefact is completely out of my reach?"

    suzume "That one? Yeah. But don't despair! I have another one right here."

    call receive_item(toy_hammer) from _call_receive_item_2

    you "Uh?"

    suzume "I found this at the Exotic Emporium today. Got it for 100 gold. A bargain!"

    you "..."

    you "This is a toy hammer."

    suzume "Not at all! This is a precious artefact from the dawn of civilization..."

    you "It's got bright, flashy colors..."

    suzume "This is the work of the Legendary One-Fingered Dwarven craftsmen, who hailed from the Dark Caves of Peril."

    you "...and it's a sloppy paint job, at that."

    suzume "Well of course - on account of them having just one finger, and living in dark caves..."

    you "And it's squishy. It makes a squeaking sound when you hit something."

    play sound s_boing

    suzume "Ha! You don't believe in the powers of the mighty Warhammer?"

    you "Not in the least."

    suzume "All right. Hit me, then. I will lay my life on the line for this."

    suzume "Go on. I'm ready."

    you "This is a toy hammer. It weighs about half a pound."

    suzume "Go on, I beseech you. If I die today, I shall not be remembered as a liar or a coward."

    you "This is not gonna... Oh, well."

    play sound s_boing
    with vpunch

    "You hit Suzume square on the top of the head."

    play sound s_scream
    suzume "AAAAH!" with vpunch

    play sound s_thunder
    with flash

    you "Uh?"

    hide suzume with dissolve

    "To your utter surprise, the hammer gives out a flash of lightning when it hits Suzume. She slips down to the floor like a ragdoll."

    you "Suzume!" with vpunch

    "Kneeling beside her, you cradle the girl in your arms."

    suzume "Aaaah... *drool*"

    you "Suzume! Are you all right?"

    suzume "Little birdies... Flying around my head... C'm'here, little birdy, let me eat you..."

    you "Delirium... I must have hit her head too hard..."

    suzume "Aw... You're such an idiot..."

    you "Suzume! You're okay!"

    suzume "I told you it was real, you id-i-ot!"

    "You feel relieved as she grabs your cheek and shakes your head back and forth."

    suzume "I know a magical artefact when I see one... Although it might be a cheap counterfeit, it still works."

    show suzume naked2 with dissolve

    "Suzume rises back on her feet, still shaking a little."

    you "Tell me about this weapon. What does it do?"

    suzume "Well, the Hammer is the bane of Kunoichi everywhere. It cuts us off from our base element, breaking our Ki's balance."

    suzume "This stuns us, and temporarily saps our physical energy and magic powers."

    you "Temporarily?"

    suzume "Well, the effect isn't long-lasting, not with this cheap black-market crap anyway."

    suzume "If it was the real deal... Legend has it, this weapon could cancel our powers permanently."

    you "Permanently?"

    suzume "Yes... Scary stuff. Fortunately, it sits atop a fiery volcano-"

    you "I remember."

    you "Well, even though the effect is temporary, it could be enough to give me an edge over the Kunoichi..."

    suzume "Yes. But don't forget - as soon as the effect wears off, they'll be able to kill you without batting an eye."

    you "Then I won't let it come to that."

    suzume "So, let's recap. You now have the Hammer of Light..."

    you "...which I will use to catch the Kunoichi..."

    suzume "...and you can find them in the city."

    you "That's right! The Earth School's Kunoichi is in the {b}Warehouse{/b} district..."

    suzume "And the Water School's Kunoichi is by the {b}Docks{/b}..."

    you "While the Void School's is in the {b}Slums{/b}. Gotcha."

    # suzume "But wait, aren't you forgetting something?"
    #
    # you "What?"
    #
    # play sound s_laugh
    #
    # suzume "My reward, of course... Kukukuku..."
    #
    # show suzume:
    #     linear 0.5 yanchor 0.85 zoom 1.3
    #
    # "Suzume moves closer, and slides her hand in your pants. It's not hard to guess what kind of reward she has in mind."
    #
    # you "Oh."
    #
    # scene black with fade
    #
    # "Many hours later..."
    #
    # show bg suzume_creampie1 at top with fade
    #
    # play sound s_orgasm_young
    # with flash
    #
    # suzume "AAAH!!! [emo_heart]"
    #
    # with doubleflash
    #
    # suzume "Aaaah... Another shot on goal... Amazing..."
    #
    # you "*pant* *pant*"
    #
    # suzume "It isn't often that I can say that I have had my fill... But you made me happy. [emo_heart]"
    #
    # you "N-No... No problem..."
    #
    # you "(My heart is going to burst, my cock is about to fall off, and my nuts are going to shrivel to raisin-size...)"

    suzume "Good. I'll be on my way, then... Let's meet up in the city to start hunting down my Kunoichi sisters!"

    you "Or die trying..."

    play sound s_laugh

    suzume "Or die trying! Yay!"

    you "(Aren't you cheerful about that...)"

    scene black with fade

    $ MC.change_prestige(2)
    $ game.set_task("Go hunt ninjas in the city.")

    # Init ninja hunt
    $ init_ninja_game()

    return


label ninja_hunt(loc):

    hide screen visit_location
    with Dissolve(0.15)

    if story_flags["ninja hunt"] == "start":

        scene black with fade
        show bg street at top with dissolve
        show suzume normal with dissolve

        suzume "All right! Now is the time to start hunting!"

        suzume "You got the Hammer ready?"

        you "Yes..."

        "The toy hammer weighs lightly in your hands, offering little reassurance as you are about to embark on a hunt for trained killers."

        suzume "Let me scout ahead. If I find them, I'll dislodge the Kunoichi from their hiding place. Then you'll act."

        suzume bend "If you see them, just whack 'em with the hammer!"

        you "I love how you make it sound so easy... *frown*"

        scene black with fade
        show expression selected_location.get_pic(config.screen_width, int(config.screen_height*0.8)) at top
        with dissolve

    $ MC.interactions -= 1
    $ story_flags["ninja hunt"] = calendar.time

    $ renpy.block_rollback()

    if loc == NPC_narika.loc:
        call ninja_game(NPC_narika) from _call_ninja_game

    elif loc == NPC_mizuki.loc:
        call ninja_game(NPC_mizuki) from _call_ninja_game_1

    elif loc == NPC_haruka.loc:
        call ninja_game(NPC_haruka) from _call_ninja_game_2

    else:
#汉化标签，未翻译的部分#
        $ no_ninja_loc_dict = {
                            "Spice market" : ["I didn't find any leads, but I did find a potent aphrodisiac I'd like you to try...", "不是现在, 云雀!"],
                            "Sewers" : ["So I went through the sewers all day... Garbage, monsters, rapists, the usual... But no signs of a Kunoichi.", "Thanks for the intel... Can you stand downwind, please?"],
                            "Farm" : ["I found nothing but a dead squirrel... Say, would you like me to drop it on your doorstep?", "没门!"],
                            "Watchtower" : ["A Kunoichi standing so close to the Guard tower would be bold indeed... But I haven't seen any signs of recent ninja activity.", "好吧，让我们继续找。"],
                            "Junkyard" : ["Nothing to see here. This is not the kind of junk I'm interested in...", "我明白了。"],
                            "Thieves guild" : ["She's not here this time... Sneaky brat.", "让我们去其他地方找找。"],

                            "Harbor" : ["Nothing smells fishy here... Except the fish. Kukukuku...", "Okay. I still think your career switch to stand-up comedy is ill-conceived."],
                            "Shipyard" : ["I haven't seen a single Kunoichi, but there was this boat that was shaped like a-", "Not interested, thank you."],
                            "Taverns" : ["So I told that seafarer... *hiccup* There are no Kunoichi here Sir! Not one! And don't call me that, I'm not worthy of the title... *sob* Turns out the guy was a bar stool with a sailor hat on it... *hiccup*", "Go home, Suzume... You're drunk."],
                            "Beach" : ["I thought we'd find her here again... But no dice.", "She must remain close to the water... After all, it's her element."],
                            "Seafront" : ["I've checked every single ship. Turns out, sailors are rowdy as hell, and there are no Kunoichi on board.", "Okay, thank you... Keep looking."],
                            "Exotic emporium" : ["You wouldn't believe the things I've seen here! They have everything... Except Kunoichi, I guess.", "We'll look elsewhere."],

                            "Stables" : ["There are no Kunoichi here, but the horses, hmmm... Did you know that their d-", "Not interested! Let's move on."],
                            "Plaza" : ["I've checked the roofs, alleys, food stalls, and the loo. No Kunoichi here.", "Okay. We'll keep looking."],
                            "Market" : ["I had to walk around the market all day, I've lost count of how many people tried to grab my ass and touch my boobies... But no Kunoichi, kukukuku.", "Why do you look happy about all this?"],
                            "Prison" : ["Not here this time... She must be surveying the Prison from a distance.", "Let's check other places around the district."],
                            "Gallows" : ["I've checked everything, even the hanged. Turns out they're actually dead.", "I am starting to doubt the quality of ninja education."],
                            "Arena" : ["So I checked the arena... Turns out there was a fight going on, I had to kick the asses of an entire gladiator team... And a couple of lions. No Kunoichi there, though.", "This must be the ninjas' legendary sense of discretion... *roll eyes*"],
                            }

        $ suzume(no_ninja_loc_dict[loc.name][0])

        $ you(no_ninja_loc_dict[loc.name][1])

        $ story_flags["ninja hunt hide " + loc.name] = True

    "You can only hunt ninjas once a day. Try again another time."

    return

label ninja_hunt_intro(): # Runs only once
    you "Suzume, wait! Where is she?"

    suzume "She moves from cover to cover... You must stay sharp!"

    you "But what should I do?"

    suzume "Easy! If you see her, hit her with the hammer."

    suzume "Also, avoid hitting any civilians in the area... We don't want any casualties."

    you "Casualties? This is a toy hammer..."

    "Hit the Kunoichi {b}three times{/b} within the time limit to stop her."

    $ story_flags["ninja hunt seen intro"] = True
    $ game.set_task("Meet the Earth Kunoichi.", "story")
    $ game.set_task("Meet the Water Kunoichi.", "story2")
    $ game.set_task("Meet the Void Kunoichi.", "story3")

    return

label ninja_hunt_begins(ninja): # Runs every time. Where ninja is an NPC object.

    if ninja.flags["hunt stage"] == 0:
        suzume "It's one of the Kunoichi! Quick, catch her!"

    elif ninja.name == "Narika":
        suzume "It's that little brat again, the Void Kunoichi! Get her!"

        if ninja.flags["hunt stage"] == 1:
            ninja.char "You got lucky once, but don't push your luck!"
        elif ninja.flags["hunt stage"] == 2:
            ninja.char "Fufufu, you are no match for me! Watch this!"
        elif ninja.flags["hunt stage"] == 3:
            ninja.char "Still want to eat dirt? Ha! You're never going to catch me!"

    elif ninja.name == "Mizuki":
        suzume "It's the weird lady with no smell! The Water Kunoichi! Don't let her get away!"

        if ninja.flags["hunt stage"] == 1:
            ninja.char "Oh, you're back. Are you suicidal?"
        elif ninja.flags["hunt stage"] == 2:
            ninja.char "*sigh* You again... Watch out for the calm before the storm."
        elif ninja.flags["hunt stage"] == 3:
            ninja.char "If you keep going, it will be your blood that rains..."

    elif ninja.name == "Haruka":
        suzume "It's the Earth Kunoichi, the serious one... After her, quickly!"

        if ninja.flags["hunt stage"] == 1:
            ninja.char "It's you, again? I have no time for this!"
        elif ninja.flags["hunt stage"] == 2:
            ninja.char "You're persistent, aren't you... Very well, I'll 'shake' you off!"
        elif ninja.flags["hunt stage"] == 3:
            ninja.char "You're testing my patience now. Watch that you don't get crushed!"

    return

label ninja_hunt_react(target): # Used when hit. Where ninja is an NPC object.

    if target.startswith("passerby"):
        $ suzume("Watch out! It's a civilian!", interact=False)

    elif target == "guest1":
        $ woman("Hey! Watch it, little man...", interact=False)

    elif target == "guest2":
        $ woman("Aw!!! S-Sir, do be careful...", interact=False)

    elif target == "guest3":
        $ woman("Stop waving that thing around, you'll break something!", interact=False)

    elif target == "ninja0":
        $ kunoichi("...", interact=False)

    else: # Target is a ninja
        $ ninja = {"ninja1" : NPC_narika, "ninja2" : NPC_mizuki, "ninja3" : NPC_haruka}[target]

        if ninja.flags["hunt stage"] == 2:
            if ninja.name == "Narika":
                narika "Too slow, loser! *blink*{w=0.5}{nw}"

            elif ninja.name == "Mizuki":
                you "She disappeared!{w=0.5}{nw}"

            elif ninja.name == "Haruka":
                haruka ninja "Back off! *tremor*{w=0.5}{nw}"

        else:
            if ninja.name == "Narika":
                $ narika("Ouch! Do that again and I'll kill you!", interact=False)

            elif ninja.name == "Mizuki":
                $ mizuki("Hey... Not bad.", interact=False)

            elif ninja.name == "Haruka":
                $ haruka("Ouch! I must be more careful...", interact=False)

    return target

label ninja_intercept(ninja, special): # Used when hunt successful (3 hits) or during special (locked). Where ninja is an NPC object

    stop music fadeout 3.0

    if special:
        play sound s_laugh
        ninja.char "Hmph... You are no match for me."
        $ lock_ninja_locations(ninja)

        if special == "fast":
            $ text1 = "Damn! She's just too fast... She dodges even perfect hits!"
            $ game.set_task("The Void Kunoichi: TO BE CONTINUED", "story3", 7)
            # $ game.set_task("Find a way to overcome the Void Kunoichi's uncanny speed.", "story3", 3)

        elif special == "rain":
            $ text1 = "It's a damn storm out here! I can't see a thing!"
            $ game.set_task("The Water Kunoichi: TO BE CONTINUED", "story2", 7)
            # $ game.set_task("Find a way to overcome the Water Kunoichi's storm protection.", "story2", 3)

        elif special == "quake":
            $ text1 = "My legs are giving out, and the district is about to crumble..."
            $ game.set_task("The Earth Kunoichi: TO BE CONTINUED", "story", 7)
            # $ game.set_task("Find a way to overcome the Earth Kunoichi's earthquake defense.", "story", 3)

        if not story_flags["c3 brothel unlocked"] and selected_district.rank == 2 and district.name != selected_district.name:
            call c2_unlock_next_brothel() from _call_c2_unlock_next_brothel
            $ story_flags["c3 brothel unlocked"] = True

        elif not story_flags["first ninja stuck"]:
            call ninja_first_lock(ninja) from _call_ninja_first_lock
            $ story_flags["first ninja stuck"] = True

        else:
            you "[text1]"

            suzume doubt "This won't work... We have to find a way to bypass her power somehow."

        if NPC_narika.flags["locked"] and NPC_mizuki.flags["locked"] and NPC_haruka.flags["locked"] and not story_flags["homura summoned"]:
            $ story_add_event("c3_suzume_hint")

    else:
        $ ninja.flags["hunt stage"] += 1

        call expression "intercept_" + ninja.name.lower() from _call_expression_6
        $ shuffle_ninja_location(ninja)

        if not story_flags["first ninja met"]:
            $ story_flags["first ninja met"] = True
            $ calendar.set_alarm(calendar.time+3, StoryEvent(label = "c2_homura_okiya2", type = "night"))

        if NPC_narika.flags["hunt stage"] >=1 and NPC_mizuki.flags["hunt stage"] >=1 and NPC_haruka.flags["hunt stage"] >=1:
            if not story_flags["all ninjas met"]:
                $ story_flags["all ninjas met"] = True
                $ calendar.set_alarm(calendar.time+2, StoryEvent(label = "c2_palace_visit1", type = "morning"))

        if NPC_narika.flags["hunt stage"] >=2 and NPC_mizuki.flags["hunt stage"] >=2 and NPC_haruka.flags["hunt stage"] >=2:
            if not story_flags["all ninjas met twice"]:
                $ story_flags["all ninjas met twice"] = True
                $ calendar.set_alarm(calendar.time+2, StoryEvent(label = "c2_palace_visit2", type = "morning"))
                $ calendar.set_alarm(calendar.time+2, StoryEvent(label = "c2_kosmo_new_recruit", type = "night"))

    return


## Narika ##

label intercept_narika():

    play music m_kunoichi fadein 3.0

    if ninja.flags["hunt stage"] == 1:

        play sound s_dodge
        pause 0.5
        play sound2 s_shatter

        kunoichi "Oops! Good thing I easily dodged that hit..."

        scene black with fade
        show bg narika intro at top with dissolve

        narika normal "Bet that stained glass craftsman will not be happy to find out what you did to his workshop, though."

        you "You... You're fast!"

        play sound s_laugh

        narika "Of course I am! Don't you know who you're messing with?"

        narika "Who am I kidding, of course you do! After all, everyone in Xeros has heard of me: Narika Shihoudou, the Legend!"

        $ narika_name = "Narika"

        menu:

            "Flatter her":
                $ renpy.block_rollback()
                you "Sure, I've heard of you. It seems the rumors about your skills were not overblown..."

                narika "Ha! You haven't seen anything yet."

                narika happy "But you're welcome to join the lo-o-ong line of my admirers. Maybe one day I'll let you shine my boots, if you're good."

                you "That's not... Whatever. Look, I just want to ask you some questions."

                narika sad "And why would I waste my time answering idle questions from a random fan... *sigh*"

                $ NPC_narika.love -= 1

            "Play dumb":
                $ renpy.block_rollback()
                you "Narufa Shilulu? Never heard of you."

                narika angry "NARIKA SHIHOUDOU!!!" with vpunch

                narika normal "Mark my name, punk, it may well be the last thing you hear!"

                you "Put that weapon down, will you? I just want to talk."

                narika "Oh, really? And what makes you think I want to talk to you?"

            "Put her down":
                $ renpy.block_rollback()
                you "Come on, don't push yourself. A Legend? You might be big in your local league, but..."

                narika angry "Whaaat?!? I'll have you know, I'm the greatest ninja that's ever existed, BAR NONE!" with vpunch

                narika "I'm the youngest, most-gifted pupil any ninja school has ever seen! I've won all the awards! I won Kunoichi Idol five times in a row! I..."

                you "Yawn. Look, I'm not interested in your boring pedigree. I have questions for you."

                narika sad "You impudent rat! Hmph."

                $ NPC_narika.love += 2

        you "Why are you here, in Zan?"

        suzume normal "Yes! Tell us who you're working for."

        narika normal "You..."

        "Her eyes narrow."

        narika "You're a Kunoichi as well! Let me browse my phenomenal memory... Judging by your looks, you must be..."

        "She concentrates for a moment."

        narika "Suzume! The Air School slut!"

        suzume normal "Hey!" with vpunch

        narika happy "Famed for your sexy-jutsu, if I remember correctly... But I always do."

        suzume "Sexy-jutsu is not a word."

        narika "Fufufu, I see what's going on here... You're jealous of me for being the best Kunoichi, and decided to come challenge me to a fight!"

        suzume "..."

        narika sad "...but because you're weak and you know it, you brought your needy toy boy here as backup! Ridiculous. I could take on both of you while blindfolded."

        suzume "Nope."

        narika normal "But I've gotta warn you, if I have to kill you, it will be in a fair fight. I don't partake in such despicable techniques as sexy-jutsu."

        suzume "Yeah, I bet... Because you're a virgin."

        narika angry "I'm not A VIRGIN!!!" with vpunch

        narika "I've had, uh... Sexy time... With many men! Sexy time like you couldn't believe!"

        suzume "Oh yeah? And who were those guys?"

        narika sad "They're... They're..."

        narika angry "I'm not telling!" with vpunch

        narika "They're tall and handsome and smart and have, er, perfect dance routines and I won't divulge their names because they're FAMOUS, okay! And they have fabulous hair!"

        suzume "Now you're just talking about your favorite boy band."

        narika "They all say I'm a sexy-time GODDESS, okay? I could beat you ten times over at sexy... Thingies... If I wanted to!"

        suzume "Now you're just talking out of your ass. Which, incidentally, you've never used for anything fun. But that's none of our concern."

        suzume "You're completely wrong, kiddo. I'm not a Kunoichi anymore, and I couldn't care less about besting you."

        narika normal "Not a Kunoichi? You mean you quit?"

        play sound s_evil_laugh

        narika "Bwahahahaha! And here I was, worried that you might have some dirty sexy-jutsu trick up your slutty skirt... But you're just a quitter. Pathetic."

        menu:
            "Defuse the situation":
                $ renpy.block_rollback()
                you "Please, ladies, let's just calm down. We are not here to fight you, Narika."

                narika sad "Like you could if you wanted to... Hmph."

            "Defend Suzume":
                $ renpy.block_rollback()
                you "Stop it. I'm sure Suzume could kick your butt if she had to. But let it not come to that."

                narika "Fufufufu, kick my butt? Keep dreaming, worm! I have no equal in a fight!"

                $ NPC_narika.love -= 1

            "Mock Narika":
                $ renpy.block_rollback()
                you "Look, we're not here to discuss Suzume's career choices, or the sad state of your virgin life..."

                narika angry "I'm NOT a VIRGIN!!!" with vpunch

                $ NPC_narika.love += 2

        you "Just tell us who you're working for. Is it the Masked Man?"

        narika sad "..."

        narika "What, you think I'd share the details of my assignment with the likes of you? Give me a break."

        you "Come on, we have you cornered. So you'd better talk."

        play sound s_evil_laugh

        narika "Oh, please. You think you've got me?"

        play sound s_crash

        scene black with flash

        narika ninja "Enmaku no jutsu!" with vpunch

        "Narika throws a smoke bomb at your feet, and you start tearing up and choking."

        suzume "She's escaping!"

        you "Where... *cough* *cough*... is she..."

        play sound s_punch

        "*BONK*" with vpunch

        "Something hits you on the side of the head, and you fall down in the dirt."

        "When you come back to your senses, the Kunoichi is gone."

        suzume "There there, you're going to be dizzy for a while, but you'll be okay."

        you "My head still rings..."

        suzume "Oh, that's nothing. She casually bumped you with the flat of her giant shuriken. She could have just as easily slit your throat."

        you "That doesn't make me feel any better."

        suzume doubt "She got the drop on us this time... But we'll run into her again. She's too bold to go into hiding."

        $ game.set_task("Meet the Void Kunoichi again.", "story3", 3)

        scene black with fade

    elif ninja.flags["hunt stage"] == 2:
        scene black with fade
        show expression selected_location.get_pic(wide=True) at top
        with dissolve
        show narika with dissolve

        narika angry "*puff*, *puff*"

        narika "Why am I so slow today... I can't believe I let you weaklings catch up with me..."

        suzume "You've been hit with the Hammer of Light! That's why!"

        you "Ahem, Suzume, thanks for divulging our secret..."

        narika "The Hammer of what? That thing?"

        narika sad "And here I thought you were wielding it around just trying to be cute..."

        narika normal "No matter, I'm the best ninja on the continent. I won't let you catch me!"

        narika normal "I just need to catch my breath, is all... *puff*"

        you "While you do that, why don't you answer a few questions?"

        narika "Grrr... I'm not saying anything to you!"

        menu:
            "What are you doing in Zan?":
                $ renpy.block_rollback()

                you "What are you doing here in Zan? Are you here on a contract?"

                narika angry "Of course, I'm here on a contract! I'm the best ninja in the whole of Xeros! My skills are always in demand..."

                narika happy "But mostly, I'm doing it for glory! Soon, the name 'Narika Shihoudou' will be the stuff of legends..."

                narika normal "Even more than it already is, I mean."

                menu:
                    extend ""
                    "Right, okay":
                        $ renpy.block_rollback()
                        you "Right, of course. You're the best ninja. I believe you've mentioned that a couple of times..."

                        narika happy "You bet! And in case anyone still has doubts, I'm going to prove it!"

                    "I don't think you're the best":
                        $ renpy.block_rollback()
                        you "Meh, I've heard of many ninjas who are better than you."

                        narika angry "Whaaat? Who! Tell me who! I'll beat them all to a pulp... Grrr." with vpunch

                        narika sad "Hmph, no matter. After this contract is done, they'll all be left in the dust."

                        $ NPC_narika.love += 1


            "Are you in league with the masked murderer?":
                $ renpy.block_rollback()
                you "Tell me now, who do you work with? Is it the masked murderer?"

                narika angry "Ha! I'm not going to reveal my connections to you..."

                narika "But many people are involved in this. This plan is big... Very big."

                narika normal "I wouldn't bother coming to this dunghole for anything less!"

                menu:
                    extend ""
                    "Offer to help":
                        $ renpy.block_rollback()
                        you "Why don't you let us in on your little plan? I'm sure we could help you out, too..."

                        narika "You? Don't make me laugh! I have no use for second-rate ninja hunters sporting toy hammers and loose clothing!"

                        suzume doubt "Psst, [MC.name]... She's right, you know, this shirt doesn't really fit you..."

                        you "I don't think she meant me."

                        $ NPC_narika.love -= 1

                    "Mock her":
                        $ renpy.block_rollback()
                        you "Of course you need help. You couldn't possibly pull off anything big like that by yourself. There must be a mastermind..."

                        narika angry "WHAT?" with vpunch

                        narika "I'm the mastermind, obviously!"

                        narika sad "I just delegate some minor tasks to others, like, er... Setting the objective and strategy... And planning..."

                        narika angry "But I'm the mastermind of punching people in the face!" with vpunch

                        suzume doubt "Is that what a mastermind is?"

            "Do you have a boyfriend?":
                $ renpy.block_rollback()
                $ NPC_narika.flags["boyfriend question"] = True

                you "Tell me now. Have you been seeing anyone lately?"

                play sound s_surprise

                narika angry "Uh? *blush*"

                suzume "Hem, [MC.name]... This question helps us, how?"

                narika blush "Such a... Such a bold question..."

                narika "(Narika, think. This boy may be about to ask you out...)"

                narika "(You shouldn't panic over this, we went over this scenario many times... You have to play 'hard to get'...)"

                suzume "I can hear your mumbling."

                narika "Shut up!"

                narika "Haha, hahaha... Of {i}course{/i} I have a boyfriend, silly! He's a tall handsome foreigner..."
                narika "We met, er, abroad far far away, and, he's not here at the moment, but... We communicate every day, by, uh..."

                narika "By carrier pigeons!" with vpunch

                you "Doesn't sound at all made-up to me..."

                suzume doubt "She can't even lie properly. Pathetic."

                narika angry "It's TRUE!" with vpunch

                menu:
                    extend ""

                    "I believe you":
                        $ renpy.block_rollback()
                        you "I believe you, Narika."

                        you "Such a cute girl must have a boyfriend..."

                        narika blush "You do? I mean, uh... Of course! Haha, hahaha..."

                        $ NPC_narika.love += 2

                    "Nah":
                        $ renpy.block_rollback()
                        you "So you're a virgin {i}and{/i} a mythomaniac? It gets better and better..."

                        narika angry "Screw you! I have a boyfriend, in fact, I'm engaged!" with vpunch

                        suzume normal "Oh yeah? What's his name?"

                        narika "It's... It's..."

                        narika "NONE OF YOUR DAMN BUSINESS!!!" with vpunch

                        suzume doubt "Weird name."

                        narika "Grrr..."

                        $ NPC_narika.love -= 1

        you "Let's go back to the reason for your presence here. Who hired you, and why?"

        narika normal "Ha! Did you think I'd spill the beans about my plans so easily?"

        narika "I won't tell you a thing! But believe me, this heist will make me the most legendary ninja in history!"

        you "'Heist'?"

        narika "*gulp*"

        narika blush "Who said anything about a heist, ahahaha... I said this height! Err... My height!"

        suzume doubt "But you're tiny..."

        narika "I'm still growing up, okay!" with vpunch

        you "A heist, uh..."

        narika "Forget it! I didn't say anything about a heist!"

        you "So you're not here as a ninja, but just as a mundane thief, then..."

        play sound s_surprise

        narika "A thief! A thief?" with vpunch

        narika "I'm a ninja! And not just any ninja, I'm the most legendary Kunoichi in Xeros history!" with vpunch

        narika normal "It just so happens that stealing is one of the skills a ninja needs to master, and I wouldn't be the best if I wasn't able to do it properly..."

        you "Doesn't sound like a legendary feat to me."

        narika normal "Ha! It all depends on what's stolen, of course!"

        "Her eyes are shining."

        narika "After this is done, no one will dare question my superiority anymore!"

        you "So people {i}do{/i} question it, uh?"

        narika sad "Hmph. Some will have you believe that others are my equals... Nonsense, of course."

        narika normal "There are some who whisper behind my back that some weird old lady from the Water school is the best, just because she's lived longer..."

        if NPC_mizuki.flags["hunt stage"]:
            you "You mean Mizuki?"

        else:
            suzume doubt "The Water Kunoichi..."

        narika "As if I could lose to an old granny! I'm ten times as fast as any prime-age ninja!"

        narika sad "Others talk about some chick from the Earth School... More serious competition, that one."

        if NPC_haruka.flags["hunt stage"]:
            you "You mean Haruka?"

        else:
            suzume doubt "We have yet to meet her..."

        narika angry "Ha! They put her up on a pedestal, just because she rebuilt her school from the ground up!"

        narika "But they forget why it burnt down: because she just couldn't defend it!"

        suzume doubt "Well, you were born with inherited abilities... While she worked hard every day to get where she is."

        narika "I know! Ridiculous, isn't it?" with vpunch

        narika "I never had to work hard for anything in my life! How come no one recognizes the superiority of natural talent over hard work?"

        "She is getting quite worked up now, her cheeks are becoming red."

        narika "Why should I respect a competitor with no talent that has to {i}work{/i} to get to a mediocre level? That's just stupid!"

        you "So, let me get this straight. You're here to show your rivals who the best ninja is, is that it?"

        narika sad "Why, it's obvious, isn't it? Why do you think those second-rate Kunoichi are heading to this dump of a city..."

        you "Because they have... Ninja stuff to do?"

        narika angry "Because they're all trying to upstage me, that's why!" with vpunch

        narika normal "But I'm going to turn the tables on them! Beat them on their own turf!"

        menu:
            extend ""
            "Makes perfect sense":
                $ renpy.block_rollback()
                you "I get it. You're going to show the world who's best? Am I right?"

                narika normal "Yes!"

                you "And in order to do that, you're going to pull off the most daring of heists!"

                narika "Exactly!" with vpunch

                you "..."

                narika "..."

                narika blush "I mean no! There is no heist! I meant, uh..."

            "This rivalry is silly":
                $ renpy.block_rollback()
                you "This is just silly. If you're the better ninja, you shouldn't need to prove it by playing petty games."

                narika angry "You don't know what you're talking about!" with vpunch

                narika "Kunoichi are natural born competitors! We fight until only one of us is left standing!"

                suzume doubt "No we don't..."

                narika "There can be only one!"

                $ NPC_narika.love -= 1

            "You're going to lose":
                $ renpy.block_rollback()
                you "I don't think you can hold a candle to any of those ninjas. They'll beat the crap out of you, kid."

                narika angry "How dare you!" with vpunch

                narika "They stand no chance against me!"

                narika "Besides, I'm not going to, hem, fight them, per se..."

                suzume doubt "Wait. So you're chickening out?"

                narika angry "Not at all!" with vpunch

                narika "I'm just going to surpass them with cunning, rather than strength."

                narika sad "I'm not going to risk getting any scar on my perfect-looking face."

                $ NPC_narika.love += 2

        you "What's going to happen next?"

        narika "Well, all the Kunoichi are here to try and become the best ninja..."

        suzume doubt "I don't think that's what the others are here for at all..."

        narika "Ha! You're just bitter because you dropped out of the competition."

        narika "We're all vying for the title of the best ninja! But only my name will be remembered by history!"

        you "How? Thanks to this heist-thing?"

        narika "You'll see, if you live that long. But now..."

        with flash

        play sound s_evil_laugh

        narika ninja "I can see my strength has returned in full! You won't be able to catch me again, let me tell you!"

        you "Damn! We ran out of time!"

        play sound s_sheath
        show speed_effect
        with dissolve

        show suzume ninja at ninja_move with easeinright

        play music m_suzume fadein 3.0
        suzume "Not so fast!"

        "Suzume leaps at Narika, throwing a shuriken at her face."

        play sound s_dodge

        pause 0.2

        play sound s_clang

        "She misses by a few inches. Narika laughs."

        play sound s_evil_laugh

        narika "Ha! You missed! I didn't even have to dodge!"

        narika "Take this, you moron!"

        play sound s_punch

        pause 0.05

        hide suzume with moveoutright

        "Narika effortlessly kicks Suzume out of the way, sending her crashing into a wall yards away."
        play sound2 s_crash
        you "Suzume!" with vpunch

        hide speed_effect with dissolve
        show narika ninja at center with dissolve

        narika "Such a clumsy attack! You call yourself a ninja? You're just pathetic."

        narika "So long, suckers! You can tell your grand-children you met the great Narika, and that she was merciful and let you live!"

        hide narika with dissolve

        "Narika zooms past you both, laughing like a schoolgirl as she quickly disappears into the distance."

        stop music fadeout 3.0

        "Suzume is crumpled in the dirt, lying under the half-broken mud wall."

        you "Suzume! Are you alright?"

        show suzume with dissolve

        suzume doubt "Ouch... That kick was no joke... I think I might have a couple of broken ribs."

        you "Looks like you're still in one piece, at least."

        suzume "Yeah... I've been through worse."

        you "Why on earth did you attack her? It was pointless!" with vpunch

        you "And we need her alive, anyway!"

        play sound s_laugh

        suzume shrewd "Pointless? Not at all, [MC.name]..."

        you "What do you mean?"

        suzume "Look."

        with fade

        "Taking you by the hand, Suzume walks to the place where Narika was standing, picking up something from the ground."

        you "What is that? Hair?"

        suzume "Yep. Her hair. I threw my shuriken at the right moment to cut some off... I knew she would be too vain to dodge."

        call receive_item(narika_hair) from _call_receive_item_3

        if MC.playerclass != "法师":
            you "But why? What can we possibly do with that?"
        else:
            you "I see where this is going..."

        suzume "Let's meet up tonight at your place. I'll explain everything."

        $ story_add_event("c2_narika_H1")

        $ game.set_task("Meet at the brothel with Suzume tonight.", "story3")

    elif ninja.flags["hunt stage"] == 4: # Stage 3 is unlocked through the story
        scene black with fade
        show narika
        "Stage 4 - Defeat"

    stop music fadeout 3.0

    hide narika
    hide bg
    return

label c2_narika_H1():

    scene black with fade
    show expression brothel.master_bedroom.get_pic() at top
    with dissolve

    play sound s_knocks

    "Later that night, you receive Suzume's visit."

    show suzume bend with dissolve

    suzume "Tadaa!!!" with vpunch

    you "..."

    you "You still have the energy to 'tadaa' me, broken ribs and all? You're a tough one..."

    suzume doubt "Oh, it's already healed, don't worry about that!"

    suzume normal "I've got a natural recovery ability, and years of training with spices and poisons to enhance it."

    you "Uh... Really? Good for you."

    suzume shrewd "But that spoiled brat will live to regret this... By the way, do you still have her lock of hair? Give it to me!"

    you "Sure, although I'm not sure what you intend to do with it."

    if narika_hair in MC.items:
        $ MC.items.remove(narika_hair)

    suzume "Oh, just a common ninja magical trick. A tracking spell..."

    if MC.playerclass == "法师":
        you "I thought that was what you'd be going for. I've already prepared a magic circle."

        suzume normal "Perfect! I'll let you lead the ritual, then... I'm, err, not the best with magic."

    else:
        you "Really? Can you do that?"

        suzume doubt "Well... I mean we were taught the basics in school... Although I may have been sleeping through most of the class... Kukuku..."

        suzume doubt "I, err, have a little tendency to cause catastrophes when I attempt magic..."

        you "Duh."

        suzume normal "But you're going to help me! Setting up the ritual can be done easily enough, then I'll leave the casting to you!"

    you "So I'm the one who should do the casting?"

    suzume "Yes, but it's simple enough. See..."

    with Fade(0.5, 1.0, 0.5)

    suzume normal "...and that should work."

    you "...so I should put my hands and feet in the circles of color... Got it."

    $ chal = renpy.call_screen("challenge_menu", challenges=[("Cast a tracking spell", "cast", 3)], cancel=("Forget it", False))
    $ renpy.block_rollback()

    if chal == "cast":

        you "Let's see. This should show us her current location, hopefully..."

        call challenge("cast", 3) from _call_challenge

        scene black with circlein

        if _return:
            play sound s_spell

            suzume "Check the looking glass! It's... It's working!"

            show bg library at top with circleout
            show narika school with dissolve

            narika "Here... Finally, a place where I can be alone."

            you "(This is Narika! What is this? Some sort of library?)"

            suzume doubt "(I'd say... It looks quite well stocked. Fancy, even...)"

            you "(More importantly... Why the hell is Narika wearing a school uniform?)"

            narika "Stupid students, and stupid teachers, bossing me around like I'm a damn child..."

            narika "I guess I should be thankful that my petite body allows me to pass for a student... Still..."

            narika "But I've got to keep this cover up at least a little longer... The prize is near."

            you "(It looks like she's infiltrated a... School?)"

            suzume "(I guess... What could she possibly want to steal there, though?)"

            narika "Okay, no one is looking... Time to do what I came here for."

            suzume "(Wait, something is about to happen!)"

            narika "All right, girl, let's move in for the kill..."

            you "(Did you hear that? She's making a move on her mark! Suzume?)"

            play sound s_dress
            suzume shrewd "(Hmm... It might not be what you think.)"

            scene black with fade

            you "Uh?"

            play sound s_sigh
            show bg narika_mast1 at top with fade

            narika blush "I've been holding it in all day... Aaah..."

            play sound s_ahaa

            narika "That fight with the weird stalker guy and his beast ninja... That got me all worked up... Hmmm..."

            you "('Weird stalker guy'???)"

            suzume "('Beast ninja'??? Grrr...)"

            narika "I need to release the tension... Oh, Narika, you're so naughty..."

            show bg narika_mast2 at top with dissolve

            "Narika starts touching herself, unaware that she is being watched through the looking glass."

            play sound s_sucking

            you "(Look, you can zoom in by pinching the mirror with two fingers. Handy.)"

            narika "You naughty, naughty girl..."

            narika sad "You can't help it if you're so perfect and beautiful, the boys are afraid to talk to you..."

            suzume "(Yeah, no, that's not it.)"

            you "(Is she really talking to herself in the second person?)"

            narika "You just, aah, need to wait for a charming gentleman to, hmmmm, take care of you..."

            play sound s_sucking

            "She now slides her fingers inside her wet pussy, making more obscene noises."

            narika "Oh, yes, a gallant prince will come... Rich, and strong, and beautiful, and... Rich..."

            narika "He'll take me inside his golden carriage, and then... Once there, he'll unsheathe his...."

            play sound s_moans

            narika "Ooh!" with hpunch

            show bg narika_mast3 at top with dissolve

            "Narika increases her pace, she's really into it now. The spell is now giving you a close-up view, and you wonder how it decides on an angle."

            you "(I'm going to use this spell. Every. Single. Day. From now on!)"

            narika "The prince will fall madly in love, of course, and then I'll be the first Kunoichi to become a Princess... And then a Queen..."

            narika "They'll write fairy tales about me... The other ninjas will worship me as a Saint... They'll grovel before me..."

            you "(I think that girl has issues.)"

            suzume "(She needs to get laid - that's what I think.)"

            narika "I will be the envy of, hmmm... The entire world... Oooh..."

            narika "I'm, I'm..."

            play sound s_scream
            with flash
            narika "Comiiiing!!!" with vpunch

            play sound s_orgasm_young
            show bg narika_mast4 at top with doubleflash

            you "(Wow...)"

            with flash

            suzume "(That girl can squirt! We might yet make something out of her.)"

            show bg narika_mast5 at top with dissolve
            narika "Aaah, aaah..."

            narika "That was good..."

            narika sad "Well, more like satisfactory."

            narika "I can do better than that..."

            narika blush "Where did I hide that damn thing... Ah, there."

            play sound s_vibro

            show bg narika_mast6 at top with dissolve

            narika blush "Now, this should be better! Just like a real man's... Thing."

            play sound s_vibro

            suzume "(Look! She's got some of the good stuff.)"

            you "(Woah. She's no naive school girl after all...)"

            narika "I've already done the prince fantasy... Think, Narika, you need something to dream about while you..."

            narika "Maybe... That weird stalker guy? I mean, he wasn't bad looking... He had some kind of rustic, magnetic charm, I guess..."

            you "(Rustic?!?)" with vpunch

            if NPC_narika.flags["boyfriend question"]:
                narika "That wretch! He had the nerve to ask me out..."

                narika "Well, he only asked if I had a boyfriend, but you know what that means."

                narika "He wants to marry us!" with vpunch

                you "(Us? No way, I'm not marrying crazy...)"

            else:
                narika "He was too shy to compliment me, but I know he was awestruck by my beauty, like they all are..."

            narika "I mean he's definitely old... But his body's fine. He'll do."

            you "(Me? Old?)" with vpunch

            suzume "(At least she said you have a good body... I'd have narrowed it down to your dick. The rest is nothing to write home about.)"

            you "(Hey!)" with vpunch

            play sound s_vibro
            show bg narika_mast7 at top with dissolve

            "*WHIZZ*"

            narika "That's it! Faster..."

            "Her love juice is sloshing out now, as she pushes the dildo into her tight virgin hole."

            "She plays with her nipples at the same time, biting her lips as the dildo inches deeper inside. Unknowingly she's giving you a hell of a peep show."

            narika "What would happen if this stranger got his filthy hands on me..."

            narika "He probably couldn't restrain himself, like the horny dog that he is... Uneducated boys are like that..."

            you "(Who is she calling uneducated...)" with vpunch

            suzume "(Well, on the plus side you don't have to do school cosplaying... I don't think a sailor uniform would suit you.)"

            play sound s_vibro
            show bg narika_mast8 at top with dissolve

            "*WHIIIZZ*" with hpunch

            play sound s_ahaa

            narika "Oooh yes! Maximum speed!"

            play sound s_moans

            narika "I bet he would do this to me... Then that... And even... That..."

            "She is furiously shaking the dildo around sideways, now, trying to stimulate every part of her cunt."

            "Love juice splashes around as she squeezes her breasts hard."

            narika "Nooooo!!! Don't do that to meeee!!! I'll... I'll..."

            play sound s_vibro
            "*WHIIIIIIZZ*" with hpunch

            play sound s_scream_loud

            show bg narika_mast9 at top with flash
            narika "Aaaaah... [emo_heart]"

            play sound s_orgasm_young
            with doubleflash

            narika "AAAAAAAAAH!!!" with vpunch

            "Narika squirts hard as she angles the dildo just right to hit her G-spot. Her love juice splashes out so hard that even on the other side of the mirror, you almost feel like dodging."

            show bg narika_mast10 at top with flash

            narika "So... Good..."

            narika "I feel spent, now... Ugh..."


            narika "It's odd though... I came a lot harder this time than when I think about Prince Charming."

            narika "I almost felt like... I was being watched by him..."

            you "(Oh, I hadn't noticed this.... What does this do?)"

            suzume "(No, don't touch that circle!!!)" with vpunch

            suzume "It's the mute command!"

            you "The mute what?"

            suzume doubt "Oops."

            play sound s_surprise
            show bg narika_mast10 at top with dissolve

            narika "Uh? Who's there?"

            you "What? She can hear us now?"

            play sound s_scream

            narika "AAAAH! There's a ghost here with me!" with vpunch

            suzume "Turn it back off, you idiot!"

            you "How?"

            suzume "Figure it out!"

            show bg narika_mast11 at top with dissolve

            narika "Wait a minute... I know these voices..."

            you "She's onto us! Do you think she knows we saw everything?"

            narika "You WHAAAAT?!?" with vpunch

            suzume "I'm cutting this off! Sorry, Narika, see youuu! [emo_heart]"

            play sound s_fizzle

            scene black with fade
            narika angry "UWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!!!!!!!!!!!" with vpunch

            $ NPC_narika.love += 1
            $ unlock_achievement("c2 narika")


        else:
            play sound s_fizzle

            you "...and nothing happened."

            suzume "Damn... That lock of hair wasn't enough to power the spell, I guess..."

            suzume "Or you're just too clumsy."

            you "You're the one to talk."

            suzume "We'll just have to catch her again... The old fashioned way."

    else:
        you "That's just too complicated. Let's focus on good old field work."

        suzume "Aw..."

    $ game.set_task("Meet the Void Kunoichi, yet again.", "story3", 3)

    return


## Mizuki ##

label intercept_mizuki():
    if ninja.flags["hunt stage"] == 1:

        "The ninja escapes you and flies off towards the beach. You frantically run after her, only to find her crouched in the water, calmly waiting for you."

        kunoichi "Whoever you are, I'm not running anymore."

        scene black with fade
        show bg mizuki intro at top with dissolve

        play sound s_mystery

        mizuki normal "What do you want?"

        suzume doubt "You got her! But wait... She's no old lady!"

        you "No shit... *pant*"

        mizuki "Me, an old lady? Aw... Now you've hurt my feelings."

        mizuki "So. I'm waiting. What is your business with me?"

        you "Err... My name is [MC.name]. This is Suzume. We only want to ask you some questions."

        mizuki "I'm Mizuki Ike. And I'm not usually in the business of giving answers."

        $ mizuki_name = "Mizuki"

        menu:
            "Flatter her":
                $ renpy.block_rollback()
                you "Look, you're a legendary ninja, reknowned for your cunning and subtlety..."

                you "We're sure you wouldn't be protecting small-time murderers..."

                mizuki "Sorry, dear. Who I'm in league with is none of your business."

            "Offer something in return":
                $ renpy.block_rollback()
                you "There's no need for grandstanding here. We could share information with you. You could name your price..."

                mizuki "My price? I don't think you could ever afford it, dear."

                you "Try me..."

                play sound s_laugh

                mizuki happy "Fufufu, aren't you optimistic... Cute."

                $ NPC_mizuki.love += 2

            "Threaten her":
                $ renpy.block_rollback()
                you "We've got you cornered here. Don't think of doing anything silly."

                mizuki "You think that I am cornered, here in the water, my natural element? Amusing."

                mizuki "They say you should judge oneself by the quality of the enemies one makes. You reflect rather poorly on me, I'm afraid."

                $ NPC_mizuki.love -= 1

        you "Let's not beat around the bush. What are you doing here, in Zan?"

        mizuki angry "What am I doing? What are {i}you{/i} doing, aside from running after respectable ladies, waving a hammer like a maniac?"

        you "Very well, I'll tell you. I'm after the masked murderer that is killing court officials."

        you "Are you working with him? If so, you're in a world of trouble..."

        "You try to sound menacing, but you're only too aware that brandishing a toy hammer is not helping your cause."

        play sound s_evil_laugh

        mizuki happy "A world of trouble? Oh, my poor boy... I've been courting trouble for longer than any man alive can know."

        mizuki normal "I'm going to give you a warning of my own... I don't indulge curiosity for curiosity's sake. And the people I find snooping do not tend to live long."

        mizuki "Remember that."

        menu:
            "I'll keep it in mind":
                $ renpy.block_rollback()
                you "I'll keep it in mind. I do not mean to fight you. But you and I aren't done talking..."

                mizuki "You're wise to heed my warning. But unless you have something to offer me, we are very much done."

                $ NPC_mizuki.love += 2

            "Don't be like that":
                $ renpy.block_rollback()
                you "Come on, don't be like that. I'm sure we could be fast friends..."

                mizuki "I don't do friends, dear. I work alone. Now leave me, I've got a lot on my plate."

            "You don't scare me":
                $ renpy.block_rollback()
                you "If you think you can scare me off so easily, you're in for a surprise. I'm tougher than you know!"

                mizuki "If I had a denar for every overconfident macho I've seen buried... You're in over your head, boy, and you don't even know it."

                mizuki angry "Go now, before I decide keeping you breathing is a waste of my time!"

                $ NPC_mizuki.love -= 1

        show bg mizuki intro1 at top with dissolve

        you "I'm not going anywhere. Look-"

        play sound s_splash

        pause 0.5

        play sound2 s_sheath

        show bg mizuki intro2 at top with flash

        suzume normal "Magic!" with vpunch

        "All of a sudden, Mizuki's eyes glow and water rises into the air around her, solidifying into an ice barrier."

        you "What is she doing? I can't see her!"

        scene black with fade

        if MC.playerclass == "法师":
            play sound s_fire
            "Conjuring a fire spell to turn your staff into a blowtorch, you start melting the thick ice. After you're done, you cannot see the Kunoichi anywhere."

        else:
            play sound s_clash
            "Hacking at the ice barrier, you slowly manage to break it down as the ice weakens. But once you're done, there is no trace of the Kunoichi."

        show bg beach at top with dissolve

        suzume doubt "She vanished... She just... vanished. I cannot sense her anymore."

        you "Damn it!"

        suzume "Well... We should keep patrolling around the district. She has a strong affinity with water... I'm sure we'll see her again, eventually."

        $ game.set_task("Meet the Water Kunoichi again.", "story2", 3)

    elif ninja.flags["hunt stage"] == 2:
        scene black with fade
        show expression selected_location.get_pic(wide=True) at top
        with dissolve

        "Mizuki runs towards the seaside, but you and Suzume get in her way before she has a chance to reach the water."

        show mizuki with dissolve

        mizuki normal "Phew... Normally I would have no problem blasting you two out of the way, but I feel my magic is all drained out..."

        mizuki "This hammer of yours must be more potent than it looks."

        suzume "(Told ya! [emo_heart])"

        you "You are at our mercy, so you'd better answer our questions."

        play sound s_evil_laugh

        mizuki happy "At your mercy! Don't overestimate your advantage. I have more tricks up my kimono sleeve."

        mizuki "But very well, I haven't had a proper challenge in a few decades. So I may indulge you."

        you "A few decades? How old are you, exactly? You can't be more than forty."

        play sound s_laugh

        mizuki "Oh, dear, how flattering..."

        suzume "I told you, the Water Kunoichi is an old lady! Everyone knows this."

        mizuki "Well, there's no denying I've been around a long time, although I don't want to think of myself as old... And I am not much of a lady either."

        you "How long?"

        mizuki "Let's just say I had already been around for a long time when you were still a suckling babe."

        you "Really? How did you not age?"

        mizuki "Why, sorcery, of course. I thought that was a given."

        if MC.playerclass == "法师":
            you "Magic can slow down aging, true... But not stop it completely."

            mizuki "There's more than one type of magic, dear."

        you "Anyway, what are you doing here in Zan? Are you involved with the masked murderer?"

        "She strikes a serious tone."

        mizuki sad "Have you ever heard the saying, 'Revenge is a dish best served cold'?"

        you "I don't know... I heard that about beer. Beer is best served cold."

        suzume "And sushi! I once ate raw fish that was left lying in the sun too long, and my tummy got all weird..."

        play sound s_sigh

        mizuki "You kids have no idea... I guess no one has ever wronged you."

        you "Well, perhaps, but we're not salty about it... Unlike pretzels, which by the way go nicely with cold beer."

        suzume "And fish!"

        mizuki normal "..."

        mizuki "I was starting to expose my sad backstory here. Do you mind?"

        you "Sorry. Go on."

        mizuki "So, revenge. I like mine ice-cold."

        menu:
            "You're right":
                $ renpy.block_rollback()
                $ MC.evil += 1

                you "You're right, of course. If you want respect, you can't let a slight slide in this world."

                mizuki angry "A 'slight'? You think I would care about a slight? *hiss*"

                mizuki "These people took away everything I had, everything I ever cared for, my former life... Turned my own blood against me."

                you "Oh..."

                mizuki "It's been so long, but I am finally here to end what began so long ago... And no one will rob me of my vengeance."

            "You're wrong":
                $ MC.good += 1
                $ NPC_mizuki.love -= 1
                you "Holding grudges is bad, you know. This is no way to live."

                "She scoffs."

                mizuki angry "Oh, aren't you Mister Goody-two-shoes! You have no idea what I've been through. None. *mad*"

                mizuki "What if someone destroyed your life, your family, your home, everything you've ever loved, and made you watch? Would you be so merciful then?"

                you "..."

            "I won't judge":
                $ MC.neutral += 1
                $ NPC_mizuki.love += 2
                you "Revenge can be petty, or necessary. I don't know your circumstances, so I won't judge you."

                play sound s_sigh

                mizuki sad "That's right. You don't know my circumstances. *sad*"

                mizuki normal "But if it makes you feel better, this is not about a petty dispute. These people destroyed everything I ever held dear."

                mizuki sad "There is no healing, no way out, no forgiveness. Not even time will help... Gods know I've tried."

        you "So this is it, then? You're after someone here in Zan? For revenge?"

        mizuki normal "You don't need to know the specifics. But know that some people - or rather a certain family - have badly wronged me. And I am here to repay them with extreme prejudice."

        you "A certain family... You mean the Royals?"

        mizuki "Let's leave it at that. I'm only going to tell you this: Do not get in my way."

        mizuki "These people {i}will{/i} die no matter what you do. And collateral damage be damned."

        menu:
            "We could kill them for you":
                $ renpy.block_rollback()
                $ MC.evil += 1

                you "Well, perhaps we could help you put an end those bastards, whoever they are. Provided you only intend to kill people we don't know or care about."

                suzume "Whaat?"

                play sound s_evil_laugh

                mizuki "And here I thought you were a naive, soft-hearted guy!"

                mizuki "I don't need anyone's help. This revenge is mine to carry out, and I will see it through."

                mizuki "All that matters is that we don't cross paths again... For your sake."

                you "But we're here now, and your magic is gone. So you'd better cooperate."

            "Let us share information":
                $ renpy.block_rollback()
                $ MC.good -= 1
                $ NPC_mizuki.love += 2
                you "I guess we could stay out of each other's way, share information... "

                mizuki "Information? You assume I don't have enough already?"

                you "I {i}know{/i} you don't have enough. Otherwise, these people would be dead already."

                mizuki happy "Nice theory. Perhaps I'm just biding my time."

                you "Either way, we could help you out, if you help us out. Our goals may be aligned."

                mizuki normal "There is one thing I need, but... You don't strike me as the right people to ask."

                you "You won't know until you try. Besides, your magic is depleted, you have nowhere else to go, so we're in for a long chat."

            "I won't let you get away with murder":
                $ renpy.block_rollback()
                $ MC.good += 1
                $ NPC_mizuki.love -= 1
                you "So you're a cold-blooded assassin. Not surprising really. But we won't let you get your way."

                "Her face hardens."

                mizuki "This is the second time I warn you. There won't be a third."

                you "Bold words, but you're helpless now, without your magic. We could just take you into custody, and let the Royal Knights handle it."

        mizuki happy "Fufufu... Magic isn't everything, my dear boy..."

        with dissolve

        "The air starts undulating, as if you were seeing a mirage."

        mizuki "Sometimes you think you're seeing something, but it's just an illusion..."

        hide mizuki with Dissolve(3.0)

        "Mizuki's body seems to dissolve, and the daylight gets weird. You blink, and suddenly she's gone."

        you "Mizuki... Mizuki?"

        play sound s_wind

        "The only thing left behind is her kimono, floating off like a kite in the ocean wind."

        suzume "She vanished!"

        you "What? How? She was just there!"

        suzume "I can still feel her Ki, but... It's getting weaker. She's getting away!"

        if MC.playerclass == "法师":
            you "No... She was definitely too weak to cast an invisibility spell..."

        else:
            you "Are you sure? But I thought her magic was drained!"

        play sound s_splash

        "Whilst you were talking, Mizuki's kimono got carried off by the strong seaside wind, and landed far away in the water."

        suzume "Look over there... It's her kimono! She must have shed it so she could escape faster."

        you "Uh... Really? Can we use it?"

        suzume "Nah... It's already floating away, and I don't do swimming."

        you "If I'm fast enough, maybe I could still reach it..."

        $ chal = renpy.call_screen("challenge_menu", challenges=[("Swim after it", "stamina", 3)], cancel=("Leave it", False))

        if chal == "stamina":
            $ renpy.block_rollback()

            "Quickly dropping off your equipment, you leap into the water and swim off after the floating kimono."

            call challenge("stamina", 3) from _call_challenge_64

            play sound s_splash

            if _return:
                "The sea is more treacherous than you imagined, and you are glad you are a good swimmer."

                "You reach the kimono before it gets too far away from the shore, and swim back, clutching it in your hand."

                show suzume bend with dissolve

                suzume "Wow, you've really got it! You were swimming like a fish!"

                suzume "Hmmm... Fish... *drool*"

                scene black with fade

                call receive_item(mizuki_kimono, msg="You have recovered %s.", use_article=False) from _call_receive_item_4

                $ calendar.set_alarm(calendar.time+7, StoryEvent(label = "mizuki_onsen", type = "night"))

            else:
                "You swim hard to reach the kimono, but it seems to stay ahead of you no matter what you do. Soon, you feel your stamina diminish."

                if MC.playerclass == "奸商":
                    you "I need to go back..."

                    "The current is against you, but you remember from your time as a child swimming in Borgo's harbor that it is useless to struggle against it."

                    "Swimming laterally and saving your strength, you eventually find a spot where the waves can carry you back towards the shore."

                    you "Phew... I made it."

                    scene black with fade

                    "You have lost track of the kimono, but at least you came back without adverse effects."

                else:
                    "Turning around, you realize the shore is a lot farther than you thought it would be. It seems the current is carrying you out to sea."

                    you "Damn it!"

                    "Attempting to swim back, you have a hard time making enough progress. Your forces are almost exhausted..."

                    you "I need to let go of some weight..."

                    "You realize you kept your purse with you. There is no choice but to let it go."

                    play sound s_gold
                    if MC.gold >= 350:
                        $ lost = 350
                    else:
                        $ lost = MC.gold

                    $ MC.gold -= lost

                    "You have lost [lost] gold."

                    you "I can make it... I can... *blub*"

                    play sound s_splash
                    scene black with circlein

                    "*SMOOCH*"

                    show bg beach at top with circleout
                    show suzume bend with dissolve

                    "When you come back to your senses, you are laying down on the sand, with Suzume standing by your side doing mouth-to-mouth resuscitation."

                    suzume "Hey! You survived!"

                    you "Nggh... I did, ugh... NGGGH! Do you have to use so much tongue?"

                    suzume "Hey! I'm a ninja, not a nurse. I've only seen this in movies."

                    you "Well, I'm pretty sure you don't need to hold my crotch either."

                    suzume "My bad! Kukukuku..."

                    scene black with fade

                    $ MC.interactions = 0

                    "You go back to the brothel, exhausted. You have lost all your actions for today."

        else:
            you "It's already out of reach. Damn, how can we catch someone that disappears at will?"

        $ game.set_task("Meet the Water Kunoichi, yet again.", "story2", 3)

    elif ninja.flags["hunt stage"] == 4: # Stage 3 is unlocked through the story
        scene black with fade
        show mizuki
        "Stage 4 - Defeat"

    hide mizuki
    hide bg
    return

label mizuki_onsen(): # Happens if the player has an onsen and got Mizuki's Kimono

    show bg onsen at top with fade

    show sill with dissolve

    sill happy "Now, this is the last of these towels, all perfectly folded and piled up in the neatest way!"

    sill "Phew, keeping this place together is such hard work..."

    you "Sill? What are you doing? There's a whole mess left in the kitchen!"

    sill sad "Aaargh..."

    you "Come on, get going, shoo!"

    hide sill with dissolve

    you "Hehe, still an hour before we open. I can have the bath all to myself now..."

    play sound s_splash
    with fade

    you "Aah! Nothing like a warm bath to soothe my tired muscles."

    you "I should get a break from all this whoring business... Maybe take a nice vacation somewhere..."

    you "But I need to sort this thing with the palace first. I wonder where to look next..."

    play sound s_splash

    "A noise at the other end of the pool takes you out of your reverie."

    you "Uh? Is anyone here?"

    "Your first thought is that some kind of animal may have entered the bath stealthily. You sure hope it isn't a dead raccoon carrying a dumb message."

    play sound s_laugh

    "Woman" "Fufufufu..."

    you "(Hmm... That didn't sound like a raccoon.)"

    "You clear your throat."

    you "Ahem, hello?"

    show bg mizuki_onsen1 with Dissolve(2.0)

    "Although it is hard to see through the onsen mist, it seems a woman is lazily bathing at the other end of the pool. She is quite naked, too."

    "Since you occasionally receive female customers, you assume she might be an early patron that managed to slip in."

    you "Sorry lady, we're closed..."

    play sound s_mystery
    show bg onsen at top with Dissolve(1.5)

    "You blink, and the lady is gone. Not quite believing your eyes, you slowly make your way around the spot where she was sitting."

    you "Nothing... And I haven't even had my first drink today..."

    play sound s_splash

    "Hearing a splashing sound behind you, you flip around, surprised."

    play sound s_mystery
    show bg mizuki_onsen1 with Dissolve(1.5)

    "The woman is now sitting right where you were moments before."

    you "You... Did you just swim past me? How? Who are you?"

    play sound s_laugh

    "Woman" "Fufufu... Why, don't you recognize me?"

    "Even though it's hard to see her through the mist, her voice sounds familiar."

    you "We've met before, haven't we... Although I guess we were both wearing clothes."

    you "(I'm bad with faces, but I'm sure I could recognize a nice pair of boobs.)"

    play sound s_mystery
    show bg onsen at top with Dissolve(2.0)

    you "Hey! She's gone, again... What's this trickery! Where are you?"

    "You splash around the pool looking for her, but fail to find her anywhere."

    "You are about to give up and call Sill, when suddenly you feel a presence behind you."

    play sound s_laugh
    "Woman" "Here... *whisper*"

    play sound s_mystery
    show bg mizuki_onsen2 at top with Dissolve(2.0)

    "The lady is standing right behind you, whispering in your ear."

    play sound s_laugh

    mizuki naked "Do you recognize me now?"

    "You would turn around to face her, but it turns out she has seized your cock in a tight grip."

    show bg mizuki_onsen3 at top with dissolve

    you "Wait a minute... You're the Water Kunoichi! Mizuki..."

    mizuki "Ike. Mizuki Ike. Good guess."

    mizuki "It's nice that we get to spend some time face-to-face, on a more equal footing..."

    you "Ahem... Face-to-face isn't really the right word... *sweat*"

    "You can feel her wet, large breasts shamelessly rubbing against your back."

    mizuki "Isn't it more comfortable like this, without your annoying toy hammer, and your pesky catgirl?"

    "Her grip on your cock is really tight, and your body feels strangely heavy and powerless."

    you "Would you mind, uh... Letting go?"

    play sound s_sigh

    mizuki "Why, I'm offended! This is not the reaction I expect when I make the first move on a man... *giggle*"

    "She squeezes your dick harder, and you can feel her trained ninja hands could just as easily crush it."

    "Despite the danger you're in, you can't help but feel oddly aroused by your predicament."

    mizuki "You know, I've mastered all the trades a Kunoichi needs to learn over the years... {i}All of them{/i}."

    mizuki "Your pet girl Suzume is not the only one that can kill with her bare body..."

    mizuki "Or make a penis explode!"

    you "*GULP*" with vpunch

    mizuki "So. Now that I have your attention..."

    mizuki "You have something of mine, and now... It seems I have something of yours."

    you "Something of yours? You mean... Your kimono?"

    mizuki "Precisely. A finely embroidered piece, that can withstand ninja moves and techniques while remaining stylish. It is a very rare and expensive thing, these days."

    mizuki "Mine was made by a great Master over a century ago. It is very dear to me.
    "
    you "W-Wait a minute... Why did you leave it behind, then?"

    mizuki "Well. It was expedient at the time, and expediency is what keeps good ninjas alive... But now I want it back."

    play sound s_sigh

    mizuki "It wouldn't do for a lady to move around the city naked, wouldn't you say?"

    "She squeezes your dick a little harder. You'd swear this should stop the blood flow, but instead your cock grows painfully larger."

    you "And... You'd keep your end of the bargain if I give it to you, right? You'd let me go?"

    mizuki "Well sure, I'll consider leaving your manhood intact if you return my kimono... Provided it hasn't got stains or holes, of course."

    you "N-No! Sill washed it very well, I swear... *sweat*"

    mizuki "Where {i}is{/i} it?"

    "She squeezes your dick harder still, but now you are starting to seriously get pleasure from it. You can feel the pain of your cock throbbing hard under her grip."

    you "..."

    "You think about your dick exploding, and wonder what would be in the coroner report. It's not a very appealing train of thought."

    you "Okay, okay... It's in my room, in the big chest. You can't miss it..."

    mizuki "Good. Your pulse tells me you aren't lying."

    you "Wait, how do you feel my pul-... Oh."

    you "I've told you where to find it. Will you let me go, now?"

    "You tried, and failed, not to sound whiny."

    play sound s_sigh

    mizuki "Hmm..."

    mizuki "Should I, though? We were just starting to have fun..."

    you "Hngh!" with hpunch

    "Without losing its tight grip, her hand suddenly starts moving, stroking the length of your shaft."

    you "Ha! what..."

    mizuki "You've been a good boy. The least I can do for you is lend you a hand..."

    you "Please, stop... This isn't... Uh..." with hpunch

    play sound s_laugh

    mizuki "Oh, am I supposed to believe you are not enjoying this? Look at how hard you got..."

    "You can't deny that your cock is now fully erect, in spite of the brutal squeeze from her iron-like hand."

    mizuki "And now, what do we have here? Something's leaking..."

    "Using her thumb, she toys with the pre-cum leaking from your urethra, teasing the head of your cock with her nail. It should feel bad, but it doesn't."

    you "Ugh..." with hpunch

    mizuki "Be honest with me now. You want this to continue, don't you?"

    you "I, uh..."

    with hpunch
    "She starts moving her wrist faster, and you can feel her plump nipples harden against your back. It is hard to resist her technique."

    you "..."

    mizuki "Say it."

    you "I..."

    you "I want you to continue..."

    mizuki "Mizuki-sama."

    you "..."

    you "I... Want it... Mizuki-sama..."

    play sound s_evil_laugh

    mizuki "Good boy! Good. You're being honest."

    mizuki "I shall reward you, then..."

    with hpunch

    "Her wrist starts jerking you in quick, painful but erotic bursts."

    "Her fingertips wrap around your cock's head, stroking erogenous zones you didn't know existed."

    mizuki "Did you know that a man's seed is 99 per cent water? And I'm a master of water magic..."

    with vpunch
    play sound s_spell

    "Suddenly, you feel a powerful rush build up inside you. Her hand closes into a fist around your cock, not letting anything come out."

    you "Nggh... It hurts..."

    "Your cock grows to abnormal proportions, throbbing extremely painfully with every heartbeat. For an instant, you think your cock might explode and you might die here."

    you "(So this is it... Live by the sword, die by the sword...)"

    mizuki "HA!" with vpunch

    show bg mizuki_onsen4 with doubleflash

    "Just before you pass out from the pain, Mizuki releases her hold on your dick, letting a veritable geyser of cum spurt out."

    "*SPURT* *SPURT*" with doubleflash

    "You grunt as your now released cock sprays loads into the air, your cum landing all over a pile of fresh towels."

    play sound s_surprise

    mizuki "My, such vitality! Oh, how I envy the youth."

    with flash

    "*SPURT*"

    show bg mizuki_onsen3 with dissolve

    "After the last of your cum is spent, you feel physically and emotionally drained."

    play sound s_laugh

    mizuki "Fufufu... Well, that was fun. Although I guess you got the better deal..."

    mizuki "I can see you have great untapped power, though... It must be why you gave the Air Kunoichi a run for her money."

    you "Aaarh... *drool*"

    mizuki "Well, as much as I enjoy your, er, gentlemanly conversation, I have a kimono to retrieve."

    $ MC.items.remove(mizuki_kimono)

    play sound s_laugh
    mizuki naked "Farewell, boy... Fufufu."

    $ NPC_mizuki.love += 1
    $ NPC_mizuki.flags["onsen"] = True
    $ unlock_achievement("c2 mizuki")

    scene black with fade
    show bg onsen at top with Dissolve(1.0)

    "You don't even see her leave, she seems to vanish into thin air in the same way she came."

    "It takes you a while to regain enough energy to even move out of the pool."

    you "Ugh..."

    show sill happy with dissolve

    sill "Master? Are you alright?"

    sill "W-Why are you naked... *blush*"

    you "Uh? It's nothing... But clean up this mess, will you? Those towels are all dirty and disgusting. Do you want our guests to feel like this place is a dump?"

    sill "Uh? The towels? B-But..."

    scene black with fade

    sill sad "UWAAAAAAAAAAAAAAAAAAAAAAH!!!" with vpunch

    "With Sill sobbing and raging, you beat a prudent retreat to your room - trying hard to ignore the customers' strange looks as you cross the brothel butt-naked."

    return

## Haruka ##

label intercept_haruka():
    if ninja.flags["hunt stage"] == 1:

        kunoichi "Stop right there!"

        scene black with fade
        show bg haruka intro at top with dissolve

        haruka normal "Do not come any closer, if you value your life!"

        suzume normal "You've got her!"

        you "Yeah, but she's got the higher ground..."

        you "Let's parley. My name is [MC.name], and this is Suzume."

        suzume "Yes! And we have questions for you."

        haruka "Suzume? I've heard your name. I'm Haruka Takamori."

        $ haruka_name = "Haruka"

        haruka "You're a Kunoichi as well, aren't you?"

        suzume doubt "A Kunoichi?"

        suzume normal "Oh yeah, I was! Now that you mention it."

        you "(You... You were a Kunoichi just a few days ago...)"

        suzume normal "But [MC.name] defeated me fair and square, and I have renounced my vows. I'm free now, baby!"

        haruka "He defeated you? This man?"

        haruka "And... You renounced your vows? Abandoned your school? Just like that?"

        "She frowns."

        haruka "How shameful. I had already heard you were liberal with your... Charms. But you truly have no honor."

        suzume doubt "Aw, sis, that's mean... *frown*"

        menu:
            "Agree with Haruka":
                $ renpy.block_rollback()
                you "Indeed, she has no honor or virtue to speak of. But that's how I like her."

                suzume "Was that a compliment? That didn't sound like a compliment."

                haruka "I shouldn't be surprised. Honorless thugs hang together. You won't even stick up for your partner."

                $ NPC_haruka.love -= 1

            "Defend Suzume":
                $ renpy.block_rollback()
                you "Who are you to trash-talk my friend? How can you lecture others about honor, when you're an assassin yourself?"

                haruka "..."

                haruka "This is a fair question. We Kunoichi live by our own tenets. Suzume has betrayed her school, and this is a grave crime."

                haruka "But she seems to have friends who stand by her, so she may not be hopeless. Even if those friends are lowlives."

                $ NPC_haruka.love += 2

            "Shrug":
                $ renpy.block_rollback()
                you "Are you finished with your squabbling? We did not come here to discuss honor."

                haruka "Hmpf, no surprise here. I'm sure petty thugs like you have no need for honor."

        you "Wait, are you calling me a thug?"

        haruka "Of course! You're a slaver and a pimp, aren't you? I caught a whiff of your hapless slaves' smell, as I was dodging your hits."

        "Her voice is bitter."

        haruka "It takes a honorless boor to do that kind of job. But I haven't got time to worry about all the petty criminals in Xeros. I have my own duties."

        you "And what are they, exactly? What takes you to Zan?"

        suzume "Yeah! Why are you skulking around the prison like a hungry crow!"

        haruka "Hmpf. Why would I tell you, of all people?"

        menu:
            "Offer to help":
                $ renpy.block_rollback()
                you "We could help you. Then you'd help us out."

                you "We want to know who's behind the recent spate of murders in town. You wouldn't have anything to do with that, by any chance?"

                haruka "We barely met each other, and you'd help me?"

                you "You seem honorable. I guess we can trust your word."

                haruka "You're trusting... And naive. I didn't expect that from a lowly pimp."

                $ NPC_haruka.love += 2

            "Give her money":
                $ renpy.block_rollback()
                you "Name your price. We could make a deal."

                haruka angry "You think I'd betray my duties for a pouch of gold? Ha! Think again."

                $ NPC_haruka.love -= 1

            "Threaten her":
                $ renpy.block_rollback()
                you "If you won't volunteer that information, we could force you. Don't make us hurt you."

                haruka angry "It's over, [MC.name]! I have the high ground!"

                you "You underestimate my power!"

                suzume "Don't try it."

        haruka normal "Forget it... I have too many things to do, and too little time. I've wasted enough with you already."

        haruka "HA!!!" with vpunch

        scene black at quake
        with fade

        "Haruka raises her hand, and the ground starts to shake violently. The pavement bursts from under you, sending you tumbling backwards."

        scene black

        suzume "She's getting away!"

        "Before you can get back up on trembling legs, the Kunoichi is already leaping from roof to roof, disappearing into the distance."

        you "She's gone."

        suzume doubt "Well, we lost for today... But she'll be back to the district eventually, the prison seems to be her target. Let's come back on another day."

        $ game.set_task("Meet the Earth Kunoichi again.", "story", 3)

    elif ninja.flags["hunt stage"] == 2:
        scene black with fade
        show expression selected_location.get_pic(wide=True) at top
        with dissolve
        "After a long, intense chase in Zan's streets, you finally corner Haruka in a dead end, overlooked by the grim grey walls of the prison in the distance."

        show haruka with dissolve

        suzume "Don't even think of jumping up on a roof! I have the upper ground this time."

        "You close in on Haruka. She takes a fighting stance but is panting, her strength drained after being grazed by the hammer."

        haruka surprise "My power is ebbing away... What treachery is this..."

        you "So we are on an equal footing. You can't run away, now is the time to talk."

        haruka angry "You can't... You can't capture me..."

        "She looks like a wounded beast, desperately looking for an escape. Her eyes look past you, as if reliving past memories."

        haruka "I won't lose... Not this time... No!"

        "Her voice is shaking, and she looks in a state of panic, gripping her blade tightly. You try to defuse the situation before you end up with a knife in the gut."

        menu:
            "I am not going to harm you":
                $ renpy.block_rollback()
                you "I mean you no harm. Information is all I want. You don't have to be afraid."

                play sound s_surprise

                haruka angry "Afraid! I am not... I am not afraid!"

                haruka normal "Never again..."

                "Her voice trails off. She seems to recover from her panic, and soon her face is back to her usual stony self."

                $ NPC_haruka.love += 2

            "I won't harm you if you answer my questions":
                $ renpy.block_rollback()
                you "You are in a tight spot, yes. But if you answer my questions, nothing bad will happen to you."

                play sound s_clang

                haruka "You think you can threaten me? Not a step closer!"

                "She emerges from her panic and now eyes you with fury."

                haruka "I've been through hell and worse. You can't push me around!"

                $ NPC_haruka.love -= 1

            "Be afraid":
                $ renpy.block_rollback()
                you "Look at me! You escaped me once, but this is the end of the road for you."

                you "No more ninja tricks! I will pry answers from you, and I'll use any means necessary!"

                "She looks at you for a moment with sheer terror. She quickly snaps out of it, though, gripping her weapon tight."

                haruka blush "N-No! You can't make me!"

        you "Let's not waste time. Tell me now, what brought you to Zan?"

        "Seeing that she is not in immediate danger, she relaxes her shoulders ever so slightly."

        haruka normal "Matters of honor. Nothing that you and your lackey would understand."

        suzume "Hey!"

        you "Don't take us for fools. We've seen you lurking around the prison."

        suzume "You are looking for someone inside, aren't you?"

        haruka angry "This is none of your business!"

        "Her voice shakes just a little, enough to confirm Suzume's suspicion. She isn't good at hiding her feelings."

        you "So you're interested in a criminal... Why, I wonder? Is it a murder assignment, or a rescue?"

        play sound s_surprise

        haruka angry "She's no criminal! How dare you!" with vpunch

        "She bites her lips, but too late."

        you "So the prisoner is a 'she', uh... And important to you. Definitely a rescue mission, then."

        haruka "Stop it!" with vpunch

        "Haruka looks lost in her thoughts for a moment."

        haruka sad "Subaru..."

        suzume "Subaru... I know that name..."

        haruka normal "Hmph, of course you do. Subaru was a legendary Kunoichi."

        you "'Was'?"

        haruka sad "Yes..."

        scene black with pixellate
        show bg dojo night with pixellate
        show subaru with dissolve

        haruka sad "Subaru was the master of our school, and our Kunoichi to boot. She was the best one among us."

        haruka "This was a time of peace, and prosperity. Our golden years... I was proud to call her 'sensei'."

        you "I don't understand. How could she be the Kunoichi? You're the Kunoichi. I thought every school had only one..."

        "Haruka's face becomes incredibly sad."

        haruka "I never should have become a Kunoichi. Subaru was and is our leader by every right. Fate forced my hand. The attack..."

        suzume "Oh! I heard about that..."

        you "What attack?"

        haruka normal "The Noroi. Our sworn enemies, a ninja clan of half-breed demons."

        you "Ninja demons? Is that a thing?"

        haruka "The Noroi are an ancient menace from the East. Our school has been at the forefront of the struggle to keep them from setting foot in Xeros."

        haruka "We were successful at first. They sent a handful of them to infiltrate, and Subaru easily managed to track them and hunt them down."

        haruka "Then came the raid..."

        scene black with fade

        play sound s_clash

        pause 0.2

        play sound s_clash

        pause 0.3

        play sound2 s_sheath

        pause 0.2

        play sound3 s_scream_loud

        "Subaru" "AGGGH!!!"

        play sound s_fire

        show bg haruka defeat1 at top with pixellate

        haruka "They cornered Subaru... She fought like a tiger, but she was grievously wounded. She fell..."

        you "You were there?"

        haruka "I was..."

        haruka " I was just a novice at the time... I couldn't do anything to save her. Or myself."

        haruka "Most of the pupils escaped, but I attempted to stay and fight. I was too weak! They captured me..."

        show bg haruka defeat2 at top with pixellate

        play sound s_scream

        haruka angry "Noooo! Let me go, you bastards!"

        "Noroi" "Hyark hyark hyark... Look at this dumb slu-u-ut. No one is coming to he-e-elp you..."

        "Noroi" "Why don't we impregnate her for r-e-e-ecruits, boss? She's got strong hi-i-ips..."

        "Noroi Leader" "No. Look at that wretch. She is weak and cowardly. We can't raise good stock from this one."

        "Noroi" "Sha-a-a-ame... Shall we just ki-i-ill her, then?"

        "Noroi Leader" "No. She might be of some use to us yet. I just thought of an easy way to keep our allies happy..."

        play sound s_sheath

        show bg haruka defeat3 at top with dissolve

        pause 0.2

        play sound2 s_scream_loud

        haruka surprise "HEEELP!!!"

        scene black with fade

        you "What happened then?"

        haruka sad "I can't... I won't talk about it."

        "Her eyes well up. She seems distraught."

        $ chal = renpy.call_screen("challenge_menu", challenges=[("Convince her", "charm", 3)], cancel=("Leave it", False))

        if chal == "charm":
            $ renpy.block_rollback()

            you "You've told us a lot already. You might as well finish your story..."

            call challenge("charm", 3) from _call_challenge_65

            if _return:

                you "I know we're just strangers, but it looks like you need to get this off your chest. We'll listen."

                play sound s_sigh

                haruka sad "..."

                "She ponders your words for a long moment."

                $ NPC_haruka.love += 1

                haruka "I had no idea what they'd do to me. I thought they'd just kill me on the spot, and I was resigned to that..."

                haruka "I was wrong."

                scene black with pixellate

                play sound s_crowd_cheer

                show bg haruka pillory1 at top with pixellate
                man "Hear hear, good people! Our new masters the Noroi are just and kind, so they made sure to share the spoils of their great victory with us!"

                play sound2 s_scream

                haruka surprise "Let me go! I'm from the ninja temple... We protect your village!"

                man "Shut up, bitch!"

                "He turned to address the crowd of raunchy men who assembled in the village plaza."

                man "Those haughty ninjas have lorded over us for too long, snatching our kids to their temple and imposing levies on us!"

                man "But when the time came to defend the village, they just threw down their arms and ran like jackals. Craven bastards!"

                play sound s_crowd_boos

                man "We were right to bend the knee before our Noroi masters, and gain the right to follow their raiding party."

                man "Tomorrow we'll leave this dump of a village for good, and take part in glorious adventure and plunder!"

                man "But before we do, the Noroi have decided to repay us for our loyalty..."

                man "Behold... This ninja slut is ours to do what we want!"

                play sound2 s_scream

                haruka "EEEK!"

                show bg haruka pillory2 at top with dissolve

                play sound s_moans

                man "This pussy is all mine! Bwahahahaha!"

                man "But don't worry, fellas, I'll share!"

                show bg haruka pillory3 at top with dissolve

                haruka blush "No! Noooo!"

                man "So this is what a ninja's pussy feels like... To think the bitches from your school wouldn't even give a passing look to us poor wretches. How times change, eh?"

                show bg haruka pillory4 at top with dissolve

                haruka "S-Stop..."

                man "What do you say, bitch? No one cares for the opinion of a weakling... You're such a worthless fighter, the Noroi didn't even want to keep you for breeding like your sisters-in-arms..."

                show bg haruka pillory5 at top with dissolve

                haruka "Nooo..."

                man "The only use for this broken body is as a public toilet! Am I right, fellas?"

                play sound2 s_crowd_laugh

                "The crowd bursts into laughter as Haruka sheds silent tears."

                man2 "Damn right, brother! And I'm not going to wait for my turn!"

                show bg haruka pillory6 at top with dissolve

                "Another man brusquely shoved his cock in Haruka's mouth. Broken by the slurs and soul-crushing words, she didn't even try to fight back."

                man2 "Oh, that mouth is nicely wet and slippery... Get ready for it, bitch, because I'm going all the way in!"

                "Haruka gagged as the man started to fuck her throat."

                show bg haruka pillory7 at top with dissolve

                man2 "Don't swallow your tongue, now, you little ninja bitch! Bwahahaha..."

                man2 "Where's your pride, now, you ninja slut? I bet you never dreamt your precious school would be burnt to ashes, while us rubes be ramming our cocks in your pussy and throat. Happy?"

                man "Man, look at that... Blood? Bro, I think she was a virgin! Isn't that perfect?"

                man2 "Bwahahah, you took this little's slut virginity by raping her in front of the whole village? Oh, that's just too good..."

                haruka surprise "Ngggh!!!!"

                man "Fucking a slutty, virgin pussy! I'm on fire now... Get ready, bitch!"

                man2 "I'm almost there myself... Uhnnngh..."

                show bg haruka pillory8 at top with flash

                man "UWAAH!" with vpunch

                play sound s_scream_loud

                "The first man exploded inside her pussy, laughing as he pumped her cunt full of cum."

                with doubleflash

                "The second man immediately came inside her mouth, ramming his cock deep."

                haruka "NGGGH!!!"

                show bg haruka pillory9 with dissolve

                man2 "Learn to enjoy the taste of cum, slut! You're going to get a lot more of it!"

                play sound s_maniacal_laugh

                man "Muhahahaha!"

                "Those two were the first of a long series..."

                $ unlock_achievement("c2 haruka")

            else:
                you "Tell us what happened next. I'm so curious!"

                play sound s_sigh

                haruka normal "No, I'm not going to tell you. This is my burden to bear."

                you "Aw..."

                $ NPC_haruka.love -= 1

        else:
            you "Whatever happened must have been traumatic for you. I won't pry."

            haruka sad "..."

            haruka "Thank you. For that."

            $ NPC_haruka.love += 1

        scene black with pixellate
        show expression selected_location.get_pic(wide=True) at top
        with dissolve
        show haruka with dissolve

        you "So... How did you escape?"

        haruka sad "I didn't. After a while, they got tired of abusing me, and threw me unconscious on a heap of garbage."

        haruka "Not all of the villagers had sided with the Noroi. After the raiding party left, some took pity on me and helped me, nursing me back to health."

        haruka "While recovering, I thought a lot about what the Noroi had said. They were right: I was weak, incapable of protecting myself and those I cared about."

        haruka "Days later, when I could walk again, I went up to the ninja temple to meet with the survivors."

        haruka sad "My intention was to quit then and there, to admit that I wasn't fit to be a ninja."

        haruka "But what I saw there..."

        haruka angry "Half of the temple had burnt down. Dead bodies were lying unburied in the rubble."

        haruka "Haggard survivors were limping around a makeshift camp, with untreated wounds, fever. Food was scarce and some of the surviving novices were fighting over it..."

        haruka "I couldn't bear to see that. Subaru would never have allowed it!"

        haruka normal "Before I knew, I was yelling orders, tending to the wounded and slapping bullies around, to try and sort this mess out."

        haruka "The surviving ninjas followed me out of stupor, they didn't even argue with me. After a day, we had managed to improve our situation and stop dying from disease and hunger."

        haruka "After a week, more survivors who had fled began to head back to our school. After a month, we had started building back."

        haruka "I never questioned my role in this. Things needed to get done, so I did them... I was taken aback when they asked me to be the new Kunoichi."

        suzume "But didn't you want to quit?"

        haruka "I did... And I do. I am not worthy of this title."

        menu:
            "Don't say that":
                $ renpy.block_rollback()
                you "Don't say that. Here you are, fighting to right the wrongs that were done to you."

                you "This is what honor is all about. This makes you worthy to be a Kunoichi!"

                "She looks at you, dumbfounded."

                haruka surprise "What... You..."

                "She blushes."

                haruka blush "I didn't expect a pimp would give me a speech about honor. These are definitely strange times."

                haruka "Your words are appreciated. But I still have a job to do."

                you "What do you mean?"

                $ NPC_haruka.love += 2

            "We understand":
                $ renpy.block_rollback()
                you "You're not so different from us, after all... I also left my former life behind."

                suzume doubt "And you criticized me for quitting the last time we met... But you're also about to run away from your life as a ninja!"

                haruka angry "I am nothing like you!" with vpunch

                haruka "It's true that I want to quit, but not before I have fulfilled my vows to my sister-in-arms! I will not run away from duty like you scum!"

                suzume "Hey!"

                $ NPC_haruka.love -= 1

            "So you're a quitter, eh?":
                $ renpy.block_rollback()
                you "So you're a quitter. The Noroi were right, after all, you're just weak."

                haruka sad "I... I..."

                you "That's right, just give up. You're obviously not cut out for this life. Let other people fight instead of you. Just become a tavern wench, or a club masseuse, or something."

                you "Hell, I'd hire you if you were willing to give a honest handjob..."

                haruka "Stop it..."

                you "But you're no fighter. Look how easily you crumble under pressure."

                haruka angry "I said 'stop'!" with vpunch

                haruka "I know I'm not cut out to be a ninja! I'm too weak, sensitive, insecure... I know that! But..."

        haruka angry "Before I give up, I must do one last thing as a ninja."

        haruka angry "I must free my Sensei, Subaru!" with vpunch

        you "Subaru... But why is she in a Zanic jail, of all places?"

        haruka defiant "I had to catch and bust the heads of more than a few of the traitors from the village to get this information. It took me years to track them down."

        haruka "Those damn Noroi snakes brought her here... Their cronies in the city made sure Subaru rots in a dank cell, waiting for whatever fate they have in mind for her."

        haruka "The Noroi are in league with a cabal of demon-worshippers, right here in this very city."

        haruka "They even spread their corruption to the very palace... And I am here to root it out!"

        you "The Palace! So it is you who is plotting against the Princess?"

        "She looks at you defiantly."

        haruka angry "What is it to you? Who do you work for, anyway, whoremonger? *angry*"

        with vpunch

        suzume "[MC.name]!"

        with vpunch

        you "What was that..."

#         hide expression selected_location.get_pic(wide=True)
        show bg prison behind haruka at quake

        "The ground starts shaking."

        suzume "Her power is back!"

        show bg prison behind haruka at quake with dissolve

        haruka "That's right! Out of my way! I must get to Subaru!"

        "Haruka suddenly picks up and runs towards you. You try to swing your hammer to hit her, but the tremor breaks your balance."

        show bg prison behind haruka at quake with dissolve

        "She leaps effortlessly above you."

        hide haruka with dissolve

        you "Haruka!"
        show bg prison behind haruka at quake with dissolve

        scene black with fade
        show bg prison behind haruka with dissolve

        "When the earthquake recedes, you and Suzume look for her everywhere, but you cannot find her trace."

        suzume "She escaped one more time... But she'll be back."

        you "She might be the link to our masked murderer! We must catch her!"

        $ game.set_task("Meet the Earth Kunoichi, yet again.", "story", 3)

    elif ninja.flags["hunt stage"] == 4: # Stage 3 is unlocked through the story
        scene black with fade
        show haruka
        "Stage 4 - Defeat"

    hide haruka
    hide bg
    return



label c2_palace_visit1(): # Happens after all Kunoichi have been met once

    scene black with fade
    show expression bg_bro at top
    with dissolve

    "As you finish breakfast, Sill brings you a letter bearing the royal seal."

    call screen letter(header = "Meeting request",
                       message = "Dear " + MC.name + ",\n\nI hope this letter finds you well, and that you have made some progress on our mutual subject of interest. Please meet me at the Palace for debriefing at your earliest convenience.",
                       signature = "Princess Kurohime")

    you "Another invitation from the Princess... She must be wondering how my investigation is going."

    show sill happy with dissolve

    sill "Master [MC.name], a carriage came with the messenger. They're waiting outside."

    you "Sounds like they want to make sure I get to the Palace in haste... Alright, let's go. Sill, you take care of the house."

    sill sad "O-Of course!"

    play sound s_close

    "You get inside the carriage and leave for the Palace."

    with fade

    sill "Why don't I ever get to visit the Palace with him... *grumble*"

    scene black with fade
    show bg palace corridor at top with dissolve

    play music m_palace fadein 3.0

    "Following your escort, you get to the Palace without trouble and are led to the Princess's antechambers."

    show bg palace room at top with fade
    show kenshin at right with dissolve
    show kuro at left with dissolve

    kuro "Ah, [MC.name]. Thank you very much for joining us."

    "Princess Kurohime and Knight Commander Uesugi are standing over a table, covered with maps of Zan and various folders thick with documents. You can tell the meeting has been going on since morning."

    kenshin "Y-Your Highness... Why is this man here?"

    "The knight looks less than pleased to see you."

    kuro "Be nice to our guest, Uesugi. And this time, try not to straddle him in the middle of doing your job..."

    "The biting remark makes Uesugi Kenshin blush bright red, as she remembers the humiliation of your first meeting."

    you "My ladies. If I am interrupting something..."

    kuro "Not at all. We are in need of fresh ideas."

    "She sounds tired."

    kuro "There were two more murders since we last spoke. Both close advisors of my father. People I grew up with..."

    "She is lost in her thoughts for a moment, then she raises her eyes and gazes at you, unflinching."

    kuro "We must put a stop to this, immediately. Tell me, what have you learnt?"

    you "Well, not much yet. But I've met all the Kunoichi that operate in the city."

    "The Princess's eyes narrow."

    kuro "The Kunoichi?"

    kenshin "Ninjas. Cold-blooded murderers, outsiders, not doubt hired by devious foreigners plotting against Your Majesty..."

    "She looks straight at you while she says this."

    kuro "So this killer is a ninja?"

    kenshin "No. The Kunoichi are all female. Your informant must be mistaken."

    you "I didn't say the killer was a Kunoichi. But I have reasons to believe one or several of them work for him."

    kuro "Interesting. But you said you had met them. What did you learn?"

    you "Not much, unfortunately, outside of their identity. They hail from three ninja schools: Earth, Water and Void."

    kenshin "Meaningless mystical mumbo-jumbo. Where are they now?"

    you "They got away. But I caught them once, so I can catch them again."

    kenshin "They got away, uh? That's convenient."

    kenshin "Your Highness, if I may, perhaps this task would be best handled by professional soldiers..."

    kuro "No more, Uesugi. You know as well as I do that our forces are stretched thin. And [MC.name], here, enjoys my complete trust."

    you "Thank you, Your Highness."

    kuro "Master [MC.name], please continue your investigation. You should learn about these foreign ninjas' motives. It must be linked to our problem in one way or another."

    you "Of course."

    kenshin "..."

    kuro "Look, it is past noon already. We mustn't skip the luncheon again today, or the courtiers will complain that we are poor hosts."

    kuro "Master [MC.name], why don't you join us? This is a boring affair, to be sure, but perhaps you can learn some new information."

    kenshin "Your Highness, this luncheon is reserved for knights and nobility..."

    kuro "Give us a break, Uesugi. Half the attendees are lowly upstarts that pay the courtiers for access, and the King, my dear father, hasn't joined an official reception in weeks."

    kenshin "..."

    kuro "Come, Master [MC.name], your presence will surprise no one. But for all intents and purposes, it is best if you act as if we'd never met."

    you "I see. Thank you, Your Highness."

    scene black with fade
    show bg palace reception at top with dissolve

    "For all of the Princess's criticism, the luncheon is a fancy affair. Well-dressed courtiers mingle with elegant maids and buttoned-up manservants, exchanging the latest gossip over plates of rare and expensive foodstuffs."

    "You gorge yourself on cocktail shrimps, only too happy to eat something other than the usual gruel. Checking the assembly, you wonder who you should start up a conversation with."

    $ i = 0
    $ joined = defaultdict(list)

    "The luncheon is getting started. Who do you wish to mingle with?"

    while i < 2:
        $ i += 1

        if i == 2:
            "The luncheon is almost over. Who do you want to join now?"

        menu:
            extend ""

            "The Princess and her entourage" if not joined["princess"]:
                $ renpy.block_rollback()

                $ joined["princess"] = True

                show kuro with dissolve

                "You approach the large group of courtiers surrounding the Princess, lavishing her with constant attention."

                "Noble man" "Your Highness, you are resplendent as the stars in the night sky, as always."

                "Noble woman" "Your Highness, have you met my son? He is {i}so{/i} eager to make your acquaintance..."

                "Foreign dignitary" "Please, Your Highness, you must pass on this important request to your father..."

                "Elder gentleman" "Your Highness, you know how lonely I've been since my poor wife passed away... But it's high time I remarry, as my children say. Did I mention how large my estate is?"

                play sound s_laugh

                "The Princess cordially answers everyone, smiling and laughing gently at the courtiers' overtures. You are astonished to see her in her courtly state, a long ways from the determined strong-willed woman you've come to know."

                "The procession of courtiers goes on forever, but finally it is your turn to pay your respects."

                "Seeing you, the Princess slightly raises an eyebrow. You remember you must pretend not to know her."

                you "Your Highness, I am but a humble business owner, I am honored to meet you."

                kuro "Ah, yes, business! It seems everyone's ventures are flourishing in this city, except the court's, of course..."

                kuro "Come, walk with me. If we are to discuss business, we must have some measure of privacy. Ladies and gentlemen, please excuse us."

                "Matter-of-factly, she places her hand on your forearm, pulling you towards the window. You hear audible gasps and jealous whispers as people question who you are to deserve such an honor."

                kuro "That will give them something to talk about. For the next couple of days, anyway."

                you "Is every day like this? Now I understand why you are weary..."

                kuro "[MC.name], thank you. You have no idea."

                kuro "How I envy the freedom of people like you... My royal birth is a curse, I tell you."

                you "It comes with a lot of privileges, though..."

                kuro "Ha! The privilege to be sold off and impregnated by an inbred simpleton, to deliver a snotty royal heir... Some privilege."

                "She seems quite bitter."

                you "This wedding thing again... Do you have any serious prospects?"

                kuro "Many, but fortunately I am able to stall for now... Until my father gets over his illness."

                you "Your father... The King is ill?"

                play sound s_sigh

                kuro "Yes, his health is getting frail, but we try to keep that information from spreading, we have enough problems already..."

                kuro "He's been skipping his official duties for over a month, though. I can only cover for him for so long."

                you "I see..."

                "A dignified servant interrupts."

                "Majordomo" "Your Highness, the Duke of Hazz-Aard is here."

                kuro "Ah, very well, tell him I shall join him shortly."

                play sound s_sigh

                kuro "Duty calls... Anyway, it was nice chatting with you."

                kuro "I look forward to hearing what you find once you've made progress on your investigation."

                you "Of course, Your Highness."

                hide kuro with dissolve

            "Commander Uesugi Kenshin" if not joined["kenshin"]:
                $ renpy.block_rollback()
                $ joined["kenshin"] = True

                show kenshin with dissolve

                "Uesugi is standing alone with her arms folded and her back to the wall, scanning the guests to make sure there's no trouble."

                you "Hey."

                kenshin "..."

                you "..."

                "You both stand in awkward silence for a moment."

                you "You don't like me much, do you?"

                kenshin "..."

                kenshin "Look, I know what the Princess said, but she's too kind and trusting."

                kenshin "We don't need your help, frankly. We can manage perfectly well on our own..."

                you "Please."

                you "This situation is obviously out of control, otherwise you would have put a stop to the murders. Why reject help?"

                kenshin "We don't need foreigners to help with our own affairs, okay!" with vpunch

                "Her voice rises and her face becomes flushed."

                you "Whoah... Why do you hate foreigners so much?"

                kenshin "Outsiders cannot be trusted, as has been shown time and time again. We must look after our own."

                kenshin "Zanic Knights have always stood by the King and his family, and always will."

                you "But look around you. Half the people here are plotting against the King."

                you "It doesn't seem to me like there are any less traitors among insiders."

                kenshin "..."

                kenshin "You wouldn't understand. You just arrived in this city, you don't know our ways."

                you "Oh, please..."

                "You can't get much more out of Kenshin, and eventually leave her to her stubborn pouting."

                hide kenshin with dissolve

            "Random courtiers" if not joined["courtiers"]:
                $ renpy.block_rollback()
                $ joined["courtiers"] = True

                "Trying to look inconspicuous, you drift alongside various groups of courtiers that are gossiping around the tables."

                "You quickly realize that they are a diverse bunch, with foreign merchants mingling with petty nobles, country officials and professional intriguants. It makes you feel less of an outsider."

                $ MC.rand_say(["wr: I've worked as a hired blade for many such arrogant pricks... They're all the same.", "wz: Just like the courts of the Westmarch swamp lords... With thankfully less mosquitoes.", "tr: It's a den of snakes, but knowing these people just might be advantageous for business..."])

                "Leaning in, you try to overhear some conversations."

                "Noble man" "How long has it been since we've last seen him? Six weeks?"

                "Guild member" "Yes. The old man is going to kick the bucket soon, I tell you."

                "Arios priest" "Hey! You're talking about the King! Show some respect!"

                "Merchant" "Some King he is, leaving the affairs of State to be handled by a girl..."

                "Noble man" "Don't disparage Princess Kurohime. She's doing a better job than the King ever did."

                "Merchant" "A woman is only fit for one kind of job, and that's blowjobs! Am I right?"

                play sound s_crowd_laugh

                "Arios priest" "How dare you! *mad*"

                with fade

                "You listen to many such conversations as you move around the room. It seems disdain for the royal family is barely hidden within this crowd."

            "The Palace staff" if not joined["staff"]:
                $ renpy.block_rollback()
                $ joined["staff"] = True

                "Sensing a good occasion to gather information {i}and{/i} devour a lot of tasty canapes, you strike up a conversation with several members of the staff. A group of young servants is especially talkative."

                "Valet" "...and let me tell you, I've only been here three months, but this place is mighty strange."

                "Manservant" "You bet. The castle's foundations were laid out by some elder civilization, I hear. Left without a trace, they did..."

                "Maid" "But I hear they left a whole network of tunnels and galleries that radiates from the Palace and criss-crosses Zan. Some secret passages are still in use, I just know it!"

                "Valet" "Oh, really?"

                "Maid" "Yes, or so the older staffers tell me. That would explain..."

                "Manservant" "Explain what?"

                "Maid" "Why, the assassin of course! He got into the castle, made it to the Princess's doorstep, didn't you hear?"

                "Maid" "I thought it was strange, because the security around here is {i}very{/i} tight. Commander Uesugi sees to that."

                "Valet" "But the secret passages might explain how he got in. Or maybe there's a traitor in the Palace..."

                "Manservant" "Speaking of Commander Uesugi, have you seen her? She's {i}so{/i} hot, isn't she? Too bad she's got such a stick up her arse."

                "Maid" "I'm sure you'd like to stick something else up her arse, you pig..."

                "Manservant" "You bet!"

                play sound s_crowd_laugh

                "The young staffers burst out laughing, safely assuming that the highborns around them do not pay any attention to their idle gossip."

    with fade

    stop music fadeout 3.0

    "Eventually, the Princess gets up to leave, and is quickly followed by the guests. Gathering some more leftover food in a bucket to snack on, you head back to your place, thinking about what you've learnt."

    return

label c2_homura_okiya2(): # Happens sometimes after the first Kunoichi has been met

    scene black
    show bg okiya at top
    with fade

    play music m_palace fadein 3.0

    "Homura comes to your place again tonight, she looks happy."

    show homura normal with dissolve

    homura "Good evening, Mister [MC.name]! I managed to slip away undetected again, so I thought I'd pay you a visit *wink*."

    sill sad "That woman again... She's stalking us..."

    play sound s_punch
    with vpunch
    # hide sill with easeoutright
    #
    # show homura at center with move

    "You elbow Sill out of the way and greet Homura with a smile."

    you "If it isn't my friend, Lady Homura! How are you today?"

    homura "Very fine, thank you! I feel like an adventurer, coming to the lower city and untangling mysteries..."

    you "Mysteries?"

    if NPC_homura.flags["divulged assignment"]:
        homura "Yes! You remember you told me about the female ninjas in town, right? The Kurochichi?"

        you "The Kunoichi."

        homura "Well, I am now certain they have a link to your killer... And the nobility. Some of Zan's most powerful players are plotting something and it involves them."

    else:
        homura "Yes! Listen, you won't believe it, but the nobility is scheming behind the Princess's back!"

        you "I will very much believe it."

    you "What do you know?"

    homura "Turns out there's not one, but several conspiracies at play. I am not clear exactly who or what is involved..."

    you "So... No specifics, then?"

    homura blush "Err, no."

    homura normal "But I'll get to the bottom of this! Please give me time."

    if NPC_homura.flags["divulged assignment"]:
        homura "What about you? Have managed to learn something?"

        you "Well, I tracked down one of the Kunoichi in town, and I know there are two others..."

        homura "Three Kunoichi... Yes, that fits with the information I heard. We're making progress! *smile*"

        you "But they're a slippery bunch, and I still don't know what they're up to."

        homura surprise "It cannot be anything good with that shadowy sort... Please be careful, don't take chances!"

        you "I will, thank you."

    else:
        homura "What about you? Are you finally going to tell me what the Princess requested you to do?"

        homura sad "I didn't manage to see her even once since we last spoke... She's growing distant. *sad*"

        homura normal "If it's something I can help you with, you should tell me. I can recoup that with my own intel!"

        menu:
            "Tell her about the Princess's request":
                $ renpy.block_rollback()
                $ NPC_homura.flags["divulged assignment"] = True
                you "Well, I guess it could be useful to share our information. I am looking after the killer who is terrorizing the court these days."

                homura "Oh, my! This is so thrilling!"

                you "And I managed to link this man to a group of female ninjas, the Kunoichi. I even met one of them."

                homura "The Kunoichi? I've heard about them..."

                homura "I'm sure they're linked to the noble plots somehow! Let us investigate together!"

            "Don't tell her":
                $ renpy.block_rollback()
                you "Sorry, but this is still a secret."

                homura sad "Aw, really? I see..."

    you "Anyway, we still have time before opening shop. Do you want to have a drink?"

    homura normal "Oh, well... Why not?"

    scene bg homura_okiya serious at top with fade

    homura blush "*cough* Whoah! What is that?"

    you "Sorry... I opened a bottle of sake, since we don't have tea."

    "(In fact, you asked Sill to make some, but she made a point of ignoring you.)"

    you "Do you want something else?"

    homura "No it's fine, don't worry... I'm not a big drinker, my father doesn't allow me to drink alcohol when I'm home."

    you "I see. You're an adult, though... Your father sounds like a strict man."

    homura "Oh, I'm sure he thinks he's protecting me. But I can handle myself, you know?"

    "She gulps a large sip, becoming visibly red but doing her best to keep a brave face."

    you "Haha, I know you are... Just don't wolf it down in one go, it wouldn't do if I had to carry you home..."

    homura "Haha no... Or I could stay here, you know? *blush*"

    you "Uh? Stay here?"

    homura "Hahaha, it was only a joke, hahahaha..."

    homura "My father is out of town, so for once I am not pressed for time."

    "You chat amiably for a long time. She's pleasant to talk to, and you try to think of a new conversation topic to broach."

    menu:
        you "So..."

        "What is it like to be a noble?":
            $ renpy.block_rollback()
            you "What is it like to be part of the Zanic nobility? You said your father is a powerful royal advisor..."

            show bg homura_okiya sad at top with dissolve

            homura sad "Oh... I guess many people see me only through that lense..."

            you "I didn't mean..."

            homura "It isn't fun, if that's what you meant. I feel like a bird in a cage, waiting to be married off to some powerful douche and give him heirs..."

            homura blush "Sorry, I'm being rude..."

            you "Don't worry about it."

            homura sad "Please forgive me, I don't like to talk about my family. *frown*"

            "You can feel she is being evasive, and quickly change subjects."

            $ NPC_homura.love -= 1

        "What do you like to do?":
            $ renpy.block_rollback()
            you "What are your passions?"

            show bg homura_okiya happy at top with dissolve

            homura normal "Well, I like adventures!"

            homura surprise "But that's not very specific, I realize."

            you "Sure."

            homura normal "I like to explore new areas by myself, discover the world, be like a fly on the wall... I like walking in nature and enjoy the peace and quiet..."

            homura blush "You could say I was born as the wrong person... Every step I take is watched by my father's guards, and I am stuck in the city. I rarely have time to simply be myself..."

            homura "Except around you, hahaha..."

            $ NPC_homura.love += 2

        "Do you have a boyfriend?":
            $ renpy.block_rollback()
            you "Let me ask you a blunt question: Do you have a boyfriend?"

            homura surprise "Whoah! Such a direct question! *blush*"

            homura "I'll answer you, but tell me first. Do you have a girlfriend? I-I mean, a real girlfriend, not... You know."

            menu:
                you "Well..."

                "I have a girlfriend (truth)" if MC.has_girlfriend():
                    $ renpy.block_rollback()
                    you "I'm seeing this girl in town. I guess you could say we're together..."

                    show bg homura_okiya sad at top with dissolve

                    homura sad "Oh. Of course... I should have guessed... Never mind."

                "I have a girlfriend (lie)" if not MC.has_girlfriend():
                    $ renpy.block_rollback()
                    you "I have a girlfriend, sure, of course... She's, a, away at the moment, but..."

                    show bg homura_okiya sad at top with dissolve

                    homura sad "Oh. Of course... I should have guessed... Never mind."

                "I don't have a girlfriend (lie)" if MC.has_girlfriend():
                    $ renpy.block_rollback()
                    you "Nope, I'm absolutely single, I have no one, cross my heart... Don't believe the people who say they see me with girls in town!"

                    homura "Really? Why would people say that?"

                    you "No reason! Haha..."

                    $ NPC_homura.love -= 1

                "I don't have a girlfriend (truth)" if not MC.has_girlfriend():
                    $ renpy.block_rollback()
                    you "Not at the moment, no. My work keeps me busy, but I have no serious relationship with anyone."

                    "You hear something from the kitchen, as if Sill was clearing her throat loudly, but pay it no mind."

                    show bg homura_okiya happy at top with dissolve

                    homura blush "Oh, that's good... I mean, no, of course, that's a shame... Haha..."

                    $ NPC_homura.love += 2

                "It's complicated":
                    $ renpy.block_rollback()
                    you "Well you know, what's commitment in this world, am I right? Girlfriends, boyfriends, pets, slaves... They come and go!"

                    homura blush "So you're a free spirit, uh? Well, I'm a little more traditional, but... I can respect that."

            you "So now tell me, what about you? Do you have someone?"

            homura surprise "Oh, I, uh... Yes, I mean, no, I mean... A long time ago..."

            homura blush "But it's all in the past. I'm alone now, I guess... Single, I mean."

            you "That was someone important to you, then?"

            "She looks into the distance, staying strangely quiet."

            homura sad "Yes."

            you "Did he... Share your feelings?"

            homura "I like to think he did, but... To be honest, I still don't know."

    show bg homura_okiya happy at top with fade

    "You talked for so long that [brothel.name] is now opened and the night is in full swing. Bawdy customers banter with your girls as they perform geisha displays."

    "The sake bottle now sits comfortably empty, and the room is now so full that Homura and you are pushed beside each other by the crowd."

    homura blush "Hey! Watch out! Sheesh, what a boor..."

    "She is now quite drunk, and you feel pleasantly warmed up. Suddenly, she leans in against you, resting her head on your shoulder."

    show bg homura_okiya serious at top with fade

    homura "Oh, [MC.name], the room is spinning..."

    you "Well... I think you had a drink too many. Better lie still for a while."

    homura "Thank you... I'm perfectly fine like that..."

    "Feeling her petite body resting against yours and her hair brush your face, you feel a bit aroused. You try to steal a glance at her cleavage, but her kimono is too well-fitted."

    "A little while goes by before she speaks again."

    homura "Say, [MC.name]?"

    you "Yes?"

    homura "Last time you gave me a tour of the premises..."

    you "Yes."

    homura "But there's one place you didn't show me..."

    you "Really? What..."

    "Turning her head, she whispers in your ear."

    homura "Your bedroom... *whisper*"

    "Taken aback, you blink and find yourself at a loss for words for an instant."

    menu:
        "You take your time to reply."

        "Sure, let's go":
            $ renpy.block_rollback()
            $ NPC_homura.flags["drunk sex"] = True
            $ NPC_homura.love -= 2

            you "That's right, I was remiss... Let's go right now! I have many things to... Show you..."

            show bg homura_okiya happy at top with fade

            "She locks eyes with you, looking seductive."

            homura "Take me there..."

            scene black with fade

            "She holds on to your arm, her pace unsteady as she walks with you towards your room."

            play sound s_door

            show expression brothel.master_bedroom.get_pic() at top
            with dissolve

            show homura blush with dissolve

            homura "So this is it..."

            play sound s_close

            "Homura takes a few steps in. You close the door behind you."

            homura "Do you... Sleep alone here?"

            if brothel.master_bedroom.girls:
                you "Well... I also use this room for training the girls. But don't worry, Sill gets everything cleaned up every morning..."

                homura "Training? You mean... *blush*"

                you "You know what I mean."

                homura "Oh... To think that I am standing here like one of your... Hmm..."

                "She looks at you with burning eyes, a mix of shame and anticipation."

            else:
                you "Yes, I sleep alone."

                homura "Really? I didn't expect it from a man like you..."

                you "Well, everyone needs their privacy."

                homura "Do you never need... Company?"

                you "Sometimes..."

                "You look her straight in the eyes, and she blushes, but she doesn't look down."

            homura "This is a nice bed... It looks comfy."

            "Without waiting for an invitation, Homura sits down on your bed, her face flushed. Her kimono loosens, giving you a glimpse of her legs, all the way up to her thighs."

            homura "Hey... I can see you staring..."

            you "Sorry..."

            homura "I don't mind... You can keep looking."

            call homura_mast() from _call_homura_mast

            call homura_bj() from _call_homura_bj

            "You blank out for a little while, feeling uncharacteristically spent."

            scene black with fade
            show expression brothel.master_bedroom.get_pic() at top
            with dissolve

            you "Wow... That was..."

            you "I didn't expect you to... I mean..."

            you "Homura, you know... Homura?"

            homura naked "Zzzzz..."

            "Lying down on the bed with her kimono in disarray and her face smeared with cum, Homura is snoring loudly."

            you "...and she's asleep."

            "She obviously was very drunk, so it's no wonder she passed out."

            with fade
            $ unlock_achievement("h homura")
            $ MC.change_prestige(2)

            "Eventually, Homura wakes up, looking hungover and confused."

            show homura naked with dissolve

            homura "What happened... Oh, [MC.name]... Why am I naked? What's this on my face?"

            homura "Did we..."

            homura "Oh."

            "It all comes back to her."

            homura "I-I'm sorry, I was too forward, I... We shouldn't have... Oh..."

            "You try to reassure her that there's nothing to worry about. Grabbing her clothes, she hurries towards the bathroom to fix herself."

            "When she comes out moments later, she meekly bows to you and wordlessly makes her exit, without looking you in the eye."

            "You follow her outside, trying to find something to say to her, but she is already rushing for the exit."

        "No, you're drunk":
            $ renpy.block_rollback()
            $ NPC_homura.love += 2

            you "Homura, I don't think it's a good idea... You've obviously drunk too much."

            show bg homura_okiya sad at top with dissolve

            homura sad "What's the matter... Am I not good enough for you?"

            you "Not at all, I didn't mean that..."

            you "But I wouldn't take advantage of someone under the influence of alcohol."

            "She looks at you pensively for a while, then nods."

            homura blush "I didn't expect you to be so... Gentle."

            homura "You're right, I'm tipsy, and I'm talking nonsense... I should go home."

            "She tries to get up, but stumbles and falls back into your arms."

            play sound s_laugh

            homura "Oh, I am {i}drunk{/i}. *giggle*"

            "Before getting up again, she kisses your cheek softly."

            homura "Goodbye, my dear [MC.name]..."

    "Your eyes trail her as she walks out of the brothel. Suddenly, your eyes meet Sill's, standing next to the door and burning with fury."

    you "Someone's in a bad mood..."

    play sound s_close

    "Sill goes to her room and slams the door so hard that a few drunk patrons fall over like bowling pins. You head back to your bedroom, sensing a headache coming."

    stop music fadeout 3.0

    return

label c2_palace_visit2(): # Happens after all Kunoichi have been met twice

    scene black with fade
    show expression bg_bro at top
    with dissolve

    play sound s_knock

    "You wake up to find a messenger bearing the royal seal knocking on your door."

    "Messenger" "Sir, I have been asked to take you to the Palace. Princess Kurohime's orders."

    you "*yawn* Arrh... Of course..."

    "You are getting used to the royal summons."

    scene black with fade
    show bg castle at top with dissolve

    "During the ride to the Palace, you reflect on what you've learnt."

    you "I've made some progress... But I'm no closer to finding out which Kunoichi is working with the masked man."

    you "What if it is all a big waste of time?"

    play music m_palace fadein 3.0

    scene black with fade
    show bg palace room at top with dissolve
    show kenshin at right with dissolve
    show kuro at left with dissolve

    "As you enter the room, you immediately feel tension in the air."

    kuro "Another murder this week! The chief executioner, no less! How can we manage a proper Kingdom without a chief executioner!" with vpunch

    kenshin "I'm sorry, Your Highness, my men are hunting this killer day and night..."

    kuro "I've just about had it with your 'men'. Those knights of yours cost an arm and a leg to house and train, and I find I get very little results in return..."

    "Kenshin's jaw visibly clenches, but she lowers her eyes and answers in a subdued voice."

    kenshin "I apologize. I take personal responsibility for this investigation. I won't disappoint you..."

    kuro "I hope you won't keep disappointing me, yes. Now, leave us, I have some important business to discuss with Master [MC.name]."

    "Kenshin looks at the Princess and you in turn, helplessly. She seems about to protest, but then she just bows her head and leaves."

    hide kenshin with dissolve

    play sound s_door_close

    kuro "I'm sorry you had to see that, Master [MC.name]."

    kuro "I was quite harsh on Commander Uesugi."

    menu:
        extend ""

        "Indeed":
            $ renpy.block_rollback()
            $ MC.good += 1

            you "Indeed. It's not like you to be so cold to her."

            play sound s_laugh

            kuro "Thank you, [MC.name], for thinking me so kind. But perhaps you have misjudged me. One does not rule a Kingdom without an iron fist, even if it is velvet-gloved."

            "She catches herself."

            kuro "I mean, my father is the ruler, of course... But as long as his illness continues, my duty is to step in."

            kuro "And sometimes it forces me to keep my cards close to the chest."

        "She had it coming":
            $ renpy.block_rollback()
            $ MC.good -= 1

            you "It was time to take her down a notch. Her pride seems to exceed her capacities."

            kuro "Perhaps. I hope this is mere incompetence. There is a more sinister explanation."

        "I won't judge":
            $ renpy.block_rollback()
            $ MC.neutral += 1

            you "I do not know the particulars of this case, so I won't judge her."

            kuro "You are wise indeed to withhold judgement. I makes me confident that you are the right person to handle something for me."

    you "What do you mean?"

    kuro "Look at this. A servant found this after the attack, under the window the murderer jumped from. My spies believe he dropped it while escaping from you."

    scene black
    show bg kenshin_pendant1 at truecenter
    with dissolve

    you "A locket? A trinket of the Arios Church, by the look of it?"

    kuro "Yes. Of the kind soldiers cherish, carrying them into battle for protection."

    you "It looks like it can be opened..."

    play sound s_equip

    show bg kenshin_pendant2 at truecenter with dissolve

    you "There's a picture... Oh!"

    "A tiny portrait adorns the inside of the pendant. Although the colors are faded, you immediately recognize the face of the beautiful, smiling woman."

    you "T-This is Kenshin! She looks different, but there's no mistaking her..."

    kuro "Yes. And no. You see, this miniature is a couple of decades old. I've had experts vouch for this."

    you "This means... It cannot be her. She would have been a child at the time."

    kuro "Indeed. But there is another possibility... Lady Sora, her mother."

    you "Her mother?"

    kuro "She passed a few years ago. She raised Kenshin all by herself. Her father, Lord Commander Uesugi, was... killed, when she was just a child."

    you "So you're saying this man, this murderer, was carrying a picture of Kenshin's mother on him? This doesn't make any sense."

    kuro "No, it doesn't. Or does it?"

    show bg palace room at top
    show kuro at left
    with dissolve

    you "You think... Kenshin is involved?"

    "You think back on the incident that day."

    you "She was the one who stopped me when I was about to go after him..."

    kuro "Yes. And she's been botching this investigation in more ways than one."

    you "This could be a mistake. Couldn't the pendant just be hers?"

    kuro "No. She didn't go anywhere near the scene during the chase. My men found it before she had a chance to."

    you "Strange, very strange..."

    kuro "Look, I can't just accuse the head of my knights with such anecdotal evidence. Uesugi and her family have been loyal servants of the royal family for as long as I can remember..."

    kuro "Besides, she commands great loyalty with my knights, perhaps more than I do. I am treading on thin ice."

    you "So you'd like me to investigate..."

    kuro "Sharp, as always, Mister [MC.name]."

    you "That's a lot to juggle already... Kunoichi, scheming lords, duplicitous knights..."

    kuro "I know. I am sorry I have to ask so much of you."

    menu:
        extend ""

        "I'm glad to help":
            $ renpy.block_rollback()
            you "I'm glad to help you, Princess... Your Highness."

            kuro "Please, no need to be formal."
            kuro "You can call me Princess Kurohime."

            you "Err, yes, Princess Kurohime."

            kuro "Your help is invaluable, but I do not take it for granted."

        "I hope the reward will be worth it":
            $ renpy.block_rollback()
            you "Indeed, I hope the reward matches the effort..."

            play sound s_sigh

            kuro "The reward, of course. *sigh*"

        "What a bummer":
            $ renpy.block_rollback()
            you "More investigative work? Sheesh... Look, Your Highness, I'm a busy man..."

            "She stiffens."

            kuro "Master [MC.name], I would like to remind you that you are a guest in {i}my{/i} city. I could just as well have you expelled with just the clothes on your back."

            you "*gulp*"

            "She sighs."

            kuro "I'm sorry, I don't want to be ungrateful. I do not forget that I'm in your debt. But please remember who you're talking to."

            kuro "But listen, I am ready to make it worth your while."

    if NPC_kuro.flags["occupation"] == "lie":
        kuro "I remember that you operate an orphanage, which is highly noble of you. You are an outstanding citizen."

        you "Err, yeah..."

        kuro "I'm sure when the time comes, you will need to move to a bigger place with your little pensioners."

    elif NPC_kuro.flags["occupation"] == "half-lie":
        kuro "I remember you operate some kind of theater. Surely some time in the future, you will consider moving to a bigger venue."

        you "Yes..."

    else:
        kuro "I know that your, err, business is growing... *blush*"

        you "Ahem, yes."

        kuro "I'm sure a time will come when you need to expand your business."

    kuro "You will need a license to operate in the upper city. Needless to say, I have the power to grant such a license... But you must demonstrate your loyalty to the crown."

    you "Oh! Thank you... This is a great opportunity."

    kuro "I will gladly help you with that. But you have to help me first..."

    you "I understand... Deal."

    kuro "Very well! I have a final request, then: Will you stay for lunch?"

    kuro "We have another one of these boring luncheons. My father is again skipping his duties..."

    menu:
        you "Well..."

        "Sure":
            $ renpy.block_rollback()
            "It isn't like you to skip a free meal."

            you "Sure, thank you."

            $ luncheon = True

        "I can't":
            $ renpy.block_rollback()
            you "Thank you for your offer, but I must decline. I have urgent business to attend to."

            kuro "I understand. So long, Master [MC.name]."

            you "Goodbye, Princess."

            $ luncheon = False

label c2_luncheon2:

    scene black with fade
    show bg palace corridor at top with dissolve

    show kenshin with dissolve

    "As you come out of the Princess's apartments, you bump into Knight Commander Kenshin. When she sees you, she... blushes?"

    you "Oh, here you are. Where's the guard?"

    kenshin "I... I told him I would relieve him. I'm perfectly capable of protecting the Princess myself."

    you "Of course..."

    if not luncheon:
        return

    you "I'm heading to the luncheon, and so is Her Majesty. Shall we go together?"

    kenshin "Uh? N-No, I'm fine with going separately..."

    "She looks away, avoiding your stare. You shrug and head for the reception hall."

    scene black with fade
    show bg palace reception at top with dissolve

    $ _choice = defaultdict(list)

    "The luncheon is getting started. Who do you wish to join?"

    $ i = 0

    while i < 2:
        $ i += 1

        if i == 2:
            "The luncheon is coming to an end soon, but you still have a little time to mingle. Who do you want to see now?" with fade

        menu:
            extend ""

            "The Princess" if not _choice["princess"]:
                $ renpy.block_rollback()
                $ _choice["princess"] = True

                show kuro with dissolve

                "It's hard for you to get noticed among the dozens of courtiers that vie for the Princess's attention, but eventually she nods to you and you step forward."

                "She takes your arm, once again raising eyebrows, and leads you away from the crowd."

                kuro "Here will do - although there are always more people within ear range than I would like."

                kuro "Was there something you wanted to tell me?"

                you "Well, I didn't get a chance to update you on my progress. I've met all three ninjas that I was looking for."

                kuro "This you told me before. Did you learn anything new?"

                you "Yes. After we caught them, each let slip some information about their true purpose."

                kuro "This is good news indeed. I need to know what they're up to."

                you "Well, one of them is trying to free a prisoner..."

                kuro "From the city prison? Good to know. I will have the security increased."

                if story_flags["c1_path"] != "evil":
                    kuro "After the disappearance of Captain Farah from her cell, we mustn't have another security lapse."

                you "Another one is planning a heist..."

                kuro "A heist? That's unexpected. I didn't expect those murders would be misdirection for theft... Unless what they're stealing is of the utmost importance."

                you "Finally, the last ninja is thirsting for revenge."

                kuro "Hmmm... This one certainly sounds like she could be behind the murders."

                kuro "Regardless of who is helping the killer... Tell me you have neutralized them."

                you "Err, no, unfortunately. They all managed to slip away."

                kuro "Oh, really? Disappointing. Ninjas tend to do that."

                you "Actually, I had a way to slow them down, but I need a way to catch them for good. I need more time to question them."

                kuro "Agreed. You had better ask around, see if you can think of something."

                you "Yes, I will. Thank you, your Highness."

                hide kuro with dissolve

            "Commander Uesugi Kenshin" if not _choice["kenshin"]:
                $ renpy.block_rollback()
                $ _choice["kenshin"] = True

                show kenshin with dissolve

                "Kenshin is still sulking in a corner, eyeing the assembly with distrust."

                you "Hey. Don't you get tired of chaperoning?"

                kenshin "Look. Let me make one thing clear. You are only just tolerated here."

                kenshin "Give me one excuse, and I'll have you thrown out of the palace."

                menu:
                    extend ""

                    "Remind her you are a guest":
                        $ renpy.block_rollback()
                        you "You seem to forget I am here at the Princess's request. I have as much a right to be here as anyone."

                        kenshin "You..."

                        play sound s_sigh

                        kenshin "Forget it. I won't waste my breath arguing with you. This is beneath me."

                    "Mock her":
                        $ renpy.block_rollback()
                        you "Oh, really? After your earlier display of incompetence, I think you're closer to getting the boot than I am."

                        "To your surprise, she doesn't take the bait. She only lowers her head in shame."

                        kenshin "On my honor as a knight, the killings will end... I'm this close to catching the culprit! You'll see."

                    "Apologize":
                        $ renpy.block_rollback()
                        you "You're on edge. I understand. I'm sorry if I upset you."

                        you "Let's not bicker between friends..."

                        "She looks at you with some surprise."

                        kenshin "Well, uh... I, uh..."

                        kenshin "I... I'm sorry I snapped at you. This is not becoming for a knight."

                "You both stay silent for a moment. You think back to your earlier conversation with Princess Kurohime. You need to fish for information."

                you "Can I ask you a personal question?"

                kenshin "Uh?"

                kenshin blush "A p-personal question? Why?"

                "She blushes. That makes her kind of cute."

                label luncheon2_kenshin_menu:

                    menu:
                        you "I wanted to ask you..."

                        "About your father" if not _choice["kenshin father"]:

                            $ _choice["kenshin father"] = True

                            you "So, I understand you grew up without your father?"

                            kenshin "Yes. I don't like to talk about it, but no doubt you've heard the gossip."

                            kenshin normal "The great Lord Commander Uesugi Maru abandoned duty and family one night, and just vanished."

                            kenshin "I was just a baby, I don't remember him. And it's better that way."

                            you "Any idea why he did that?"

                            kenshin "I don't know, and I don't care. Why do men bail on their family? Untrustworthy cowards, the lot of them."

                            you "Not all men are like that..."

                            kenshin "Really? Maybe. I don't care. A man can be weak. But a knight? This is unforgiveable."

                            you "But your father is out there somewhere... Don't you want to meet him?"

                            kenshin "Out there? Oh no, no he's not."

                            you "What do you mean?"

                            kenshin "Years later, they found his body in the forest. When I was 8 or 9. My mother pleaded and begged, but they wouldn't let us see it."

                            kenshin "Apparently he had been mauled by wild beasts. A fitting end for this animal."

                            "Her voice breaks."

                            kenshin "He was living like a pauper in some wood hut in the forest. Apparently, this was a better life for him than leading the Royal Knights, or tending to his family... To his only child..."

                            "Her eyes are shiny."

                            you "I'm sorry."

                            "She blinks her tears away, and her eyes look hard again."

                            kenshin "Sorry? Why would you be sorry? You didn't make my father into a filthy coward, he just was born like that. I'm better off without him."

                            kenshin "This was all for the best."

                            you "But you still decided to become a knight?"

                            kenshin "Of course! I picked up the mantle of a knight as soon as I could hold a sword."

                            kenshin "I won't let his stain on the honor of my family stand, even if I have to dedicate my whole life to atone for his sins."

                            you "I see."

                            jump luncheon2_kenshin_menu

                        "About your mother" if not _choice["kenshin mother"]:

                            $ _choice["kenshin mother"] = True

                            you "Describe in single words only the good things that come into your mind about... your mother."

                            kenshin normal "My mother?"

                            kenshin "Let me tell you about my mother..."

                            "For a second it looks as if she's going to shoot you, but she keeps talking."

                            kenshin "My mother was a Saint! She raised me all by herself, and made me the woman I am."

                            kenshin "Would that everyone had her strength and integrity."

                            you "She was... A single mother, then?"

                            kenshin "I don't like what you are implying. I was born in wedlock, just as a lady should."

                            kenshin "But it's no secret. My father ran away from us, when I was very young. My mother held the fort. She had to."

                            you "And all those years, she didn't have... You know... Lovers?"

                            kenshin blush "What? No way! My mother was no slut!" with vpunch

                            you  "You... You do know it's quite okay to take on lovers after your husband abandoned you, right?"

                            kenshin normal "No, my mother would never have had any of that. She kept saying my father would return... That he was honorable..."

                            kenshin "But she never got to see him again. After we learned of his fate, she was never the same again. Sorrow got the best of her, and she died before she was even forty."

                            jump luncheon2_kenshin_menu

                        "About your boyfriend" if not _choice["kenshin relationship status"]:
                            $ renpy.block_rollback()
                            $ _choice["kenshin relationship status"] = True

                            you "I want to ask you... About your boyfriend!"

                            you "So, who is he? Is he here? A noble, or a knight? Is he taller than me?"

                            play sound s_surprise

                            "She blushes bright red."

                            kenshin blush "S-Such a personal question! I-I won't... I can't..."

                            "She looks completely unbalanced all of a sudden, like a teenage girl caught in an embarrassing position by a teacher."

                            kenshin "I... You... We..."

                            kenshin normal "I have no b-boyfriend, or husband! No time for that, nor do I need one!"

                            "She gets heated, and it seems to you she protests too much."

                            you "I see... You like women, perhaps? Do you and the Princess..."

                            kenshin blush "WHAAAT?" with vpunch

                            kenshin "N-Nooo! Her Majesty... I would never... H-How could you... *blush*"

                            kenshin "I am a soldier, you bufoon, not a flimsy debutante! I have no time for men or women in my life!" with vpunch

                            "She's shaking, and she pumps her fist at you with righteous anger."

                            you "S-Sorry..."

                            "She suddenly realizes other people are staring at you both. She blushes again."

                            kenshin "I-I'm sorry, I shouldn't have said bad words. I, uh... It's embarrassing..."

                            hide kenshin with dissolve

                            "Without so much as bowing goodbye, she suddenly turns around, and she rushes out of the room."

                            you "Hey! Who's guarding the Princess now..."

                            you "I guess it's me, then. *sigh*"

                        "Never mind":
                            you "Well, look at the time. Forgive me, but I have to go."

                            kenshin "Yes. Don't let me keep you."

                            hide kenshin with dissolve

            "Random courtiers" if not _choice["courtiers"]:
                $ renpy.block_rollback()
                $ _choice["courtiers"] = True

                "The flow of courtiers of all stripes coming to greet the Princess is unceasing, but you also notice how other groups hang separately around other public figures. A handful of them draw almost as much attention to themselves as the Royal Heiress."

                you "I wonder who they are..."

                "An elderly lady with a face covered with boils overhears you."

                "Duchess" "My darling boy, you really don't know who they are, do you? You must be new to the Kingdom..."

                you "Well... Yes, I'm not from Zan, it's true."

                "Duchess" "A little country bumpkin, how adorable! A minor noble from one of the lesser cities in Xeros, no doubt... You must be starstruck to be standing among Zan's elite! This is the real deal!"

                you "Err... If you say so."

                "Duchess" "But you're in luck, because I know {i}everyone{/i} worth knowing in the City of Jade."

                "She nods towards an athletic gentleman with piercing blue eyes, having a quiet discussion with a group of courtiers."

                "Duchess" "This is Lord Dukal, one of the most influential men in the city. He commands a lot of loyalty within the young people of the upper class, and speaks for many of them at Court."

                you "Is he related to the King?"

                "She chuckles."

                "Duchess" "Oh no, far from it. He's one of the last survivors of the former dynasty."

                "Duchess" "A distant cousin of the ruling family, he was too young and unimportant at the time of the purge. And now, it's too late for King Pharo to correct this particular mistake... Not that he has the backbone anymore."

                you "The purge?"

                "Duchess" "Why, yes, has no one told you how the current dynasty came to power? There was a lot of bloodshed when King Pharo took the throne..."

                "Duchess" "Well, some would say 'usurped'. But I am not one to gossip... *wink*"

                you "What is he doing at court?"

                "Duchess" "Well, he's still old Zanic nobility. Some foolish people would even say he has as much right to the throne as Princess Kurohime, Arios bless her... Some even took to calling him 'Prince Dukal'."

                "Duchess" "A good way to end up with your tongue torn out in a torture cell, if you ask me."

                you "And this gentleman?"

                "You show her a tall, thin man in elegant black robes, with a long black beard with streaks of grey, surrounded by mages and scholars. He looks frail and sickly."

                "Duchess" "Why, this is Lord Henso, of course. A close advisor to the King, and the most skilled astronomer at Court. He was a most handsome man in his prime..."

                "She sighs."

                you "(Lord Henso... Rings a bell...)"

                "You suddenly remember Homura's last name: Lady Henso."

                you "Oh! I think I met... Someone from his family. We're, err... Friends."

                "Duchess" "Have you, now? No surprise here, this is one of the oldest and most respected families in the city."

                "Duchess" "Like all of the Magic Guild, they remained neutral during the upheaval, so they got through the change of dynasty unscathed."

                "Duchess" "Not to say that Lord Henso didn't have his share of heartache, though..."

                "Next, she points at a small, fat man by the buffet, in passionate discussion with a group of merchants."

                "Duchess" "And this is Lord Kosmo the Elder. He is probably the richest man in this room, although many despise him for how he made his fortune. There's no business too dirty for this man."

                you "Kosmo, you say?"

                "Duchess" "Yes. Not an old or respected name by any means, but money commands its own loyalty."

                "Duchess" "I hear his only son is acting up... Too bad, because he had plans for him. He thinks he could forge an alliance with the King..."

                you "An alliance? How?"

                "Duchess" "Why, marriage of course!"

                "Duchess" "The Princess is only the most coveted bachelorette in all of Xeros..."

                "Duchess" "But whichever fool ends up marrying her is in for a disappointment."

                you "What do you mean?"

                "She chuckles again."

                "Duchess" "Well, for starters, this girl Kurohime is likely to be as boring a bride as you could imagine... I know a frigid dove when I see one!"

                "Duchess" "I wasn't anything like her in my day... *wink*"

                "She has a worrysome glint in her eye, and you hope the old hag is not going to move on you."

                "Duchess" "But this is nothing worth mentioning. Only the plebs marry for lust or love."

                "Duchess" "What I meant is, whoever ends up marrying her is unlikely to keep the spoils for very long..."

                you "Why?"

                "Duchess" "Well, some say the Pharo dynasty will not survive its first King. Besides..."

                "She spots a knight walking towards you, and interrupts herself."

                "Duchess" "But look, my young lad, it was a pleasure talking to you. Now, I really need to talk to Lady Foozia about her new gardening book..."

                "Duchess" "We'll have a more private chat another time, right? *wink*"

                "She gives you pat on the buttocks as she goes, and you freeze. Fortunately, the old harpy doesn't push it and leaves, chuckling as she goes."

            "The Palace Staff" if not _choice["staff"]:
                $ renpy.block_rollback()
                $ _choice["staff"] = True

                "Heading towards the kitchen, you position yourself to be able to intercept both conversations and food platters."

                "Page" "... I don't care if you believe it or not, this is what the royal guard told me."

                "Manservant" "That doesn't make sense. He was in his cups."

                "Page" "'Course he was, otherwise he wouldn't have said anything... But he had no reason to lie. He said they had evidence."

                "Maid" "Evidence? Against Commander Uesugi? I can't believe that."

                "Page" "Well, the date doesn't fall far from the tree."

                "Manservant" "What do you mean?"

                "Maid" "Like father, like daughter..."

                "Page" "Her dad was Commander of the Knights too, but he deserted suddenly, abandoning King and family."

                "Maid" "Lady Kenshin was just a babe."

                "Manservant" "He ran away, just like that?"

                "Page" "Not just like that. I hear there was another woman..."

                "Maid" "Some said they saw him fleeing with a baby. His bastard, no doubt..."

                "Manservant" "A baby? So he left the little Lady alone as a babe, but he took his bastard with him?"

                "Page" "Ouch. That's gotta sting..."

                "Manservant" "It still doesn't have anything to do with Kenshin being a traitor."

                "Page" "Of course it does! Can't you see? She has traitor genes!"

                "Maid" "There's no such things as traitor genes..."

                "Page" "There is! Don't you remember the story about the wife of old Lord Wittol..."

                "You listen to the palace underlings bickering among themselves, until you get bored and eventually leave them to it."

    scene black with fade

    stop music fadeout 3.0

    "Yawning, the Princess gives the signal that she is ready to retire to her apartments. The crowd quickly clears out, and a knight escorts you down to a carriage that takes you back to the lower city."

    return

label c2_kosmo_new_recruit(): # Happens the night after the 2nd palace reception

    scene black with fade
    show bg mansion night at top with dissolve

    "That night."

    play music m_suspense

    show kosmo at right:
        zoom 0.9

    with dissolve

    kosmo "Brr, it's cold again. Where is that damn ninja?"

    show kunoichi reversed at left:
        xalign -0.2
    with blinds

    kunoichi "Here."

    kosmo angry "UWAH!!!" with vpunch

    kosmo "D-Don't scare me like that! Gee, you ninjas are all the same!"

    kunoichi "I wasn't going to go out in the open without first checking the perimeter. Is this your house?"

    kosmo laughing "It's called a {i}mansion{/i}! And yes, it's mine."

    kosmo happy "I earned it the hard way, too: my father gave it to me when I was 8."

    kosmo "I had to agree not to throw temper tantrums for a whole {i}week{/i}. Do you know how hard it is to do it at that age?"

    kunoichi "Hmm... Not very?"

    kosmo angry "Grrr..."

    kunoichi "Anyway. I was told you wanted to talk to me. You went to great lengths to find me..."

    kosmo happy "Why, yes, it cost me a huge sum to find you, that's for sure. I hear you're the best."

    kunoichi "Tell me why I'm here."

    kosmo "Well, there's this nuisance I want you to deal with. A man. Nothing, really, a nobody..."

    kunoichi "A nobody... Which is why you want to spend a fortune hiring the best assassin in the region?"

    kosmo angry "Err, I... Don't interrupt! His name is [MC.name], and..."

    play sound s_evil_laugh

    kosmo laughing "Why do you laugh?"

    kunoichi "[MC.name], you said? That's interesting... I believe I know him."

    kosmo "You do?"

    kunoichi "Tell me more."

    kosmo "Follow me inside..."

    hide kosmo
    hide kunoichi
    with dissolve

    $ story_flags["no kosmo"] = True

    return


label ninja_first_lock(ninja): # Happens after the MC reaches third hunting stage for the first time (except if it is the unlocking brothel districtç)

    show suzume doubt with dissolve

    suzume "Damn... Our usual techniques won't work against her. She's too strong. Even the makibishi wouldn't stop her."

    you "What happened?"

    suzume "I guess she got wise to our hunting techniques. I will be impossible to catch her, now that she is on her guard..."

    you "Come on, Suzume! There has to be a way!"

    suzume "I guess a direct confrontation won't do us any good. Maybe we could investigate, the old fashioned way... After all, we have some knowledge about her motivations."

    you "Not nearly enough to know what we should do next..."

    suzume "Let's keep our eyes and ears open. Maybe an opportunity will present itself?"
    #
    # $ calendar.set_alarm(calendar.time+2, StoryEvent(label = "c2_homura_okiya3", type = "night"))

    hide suzume with dissolve

    return


label c2_unlock_next_brothel(): # Happens in the rank 2 district where his brothel is NOT located, when MC reaches the 3rd hunting stage (blocked)

    scene black
    show bg empty_mansion at top
    with dissolve

    play sound s_crash

    with vpunch

    "After coursing the ninja all the way into a large, empty house, only for her to escape again, you collapse on the floor, exhausted."

    you "That's it, I'm spent... I can't run any longer..."

    show suzume with dissolve

    suzume "Come on! We need to give chase!"

    you "It's no use... I'm too tired..."

    you "Just let me die here alone..."

    hide suzume with dissolve

    you "Hey! Where are you going?!?"

    show suzume with Dissolve(0.3)

    suzume "You said I should let you die here alone."

    you "It was a figure of speech! Help me get up already!" with vpunch

    play sound s_sigh

    suzume "Sure, *sigh*..."

    play sound s_dress

    "You get up on your feet, brushing a large amount of dust from your clothes."

    you "What is this place, anyway? It's huge..."

    suzume doubt "I know... It looks like a wealthy merchant's house, or something? There must be at least a dozen rooms..."

    you "He must have had many wives..."

    suzume bend "Just like you, then!"

    you "Wives and whores are not the same thing... I told you many times."

    suzume doubt "So you keep saying, but I don't really get the difference."

    suzume bend "Think of all the new wives, er, whores you could have if you had a building like this!"

    you "I know... *sigh* A man can dream."

    suzume doubt "Still, half the rooms here are nearly collapsed. Getting this place back up and running would cost a pretty denar."

    you "It's a pity such a nice place is in such disrepair. Look at those cobwebs! I don't want to meet the spider that did that... *shiver*"

    you "Let's go."

    scene black with fade
    show bg brothel3 at top with dissolve

    $ dis = selected_district.name
    $ dis = "t" + dis[1:]

    "You head back outside, into the busy streets of [selected_district.name]."

    you "Nice building, and in a lively area, too. I wish we could talk to the owner."

    "Voice" "The owner? You wanna talk to Papa Freak!"

    you "Uh?"

    show gina with dissolve

    gina "Hello there! I overheard you. This is Papa Freak's old family house."

    if junkyard.action:
        you "Gina? What are you doing here?"

        gina "Why, I'm just coming out of Papa Freak's repair shop. It's right around the corner!"

    you "Who's that?"

    gina "Papa Freak is a brillant inventor! Not a genius like me, of course, but he knows more about old Cimerian machines than anyone in the city."

    gina "He owns the magical repair shop just around the corner. You can ask him about the house, he told me it was his family's."

    you "You were just there?"

    gina "Yeah! Papa Freak is awesome, he gives me candy, and Cimerian scrap, for free!"

    you "That's nice of him..."

    gina "All I have to do is lift up my skirt for him, and give him my old underwear for recycling... Isn't that great?"

    you "On second thought, not so nice."

    gina "You can go see him and tell him you know me. Perhaps if you give him your used underwear you'll get free stuff?"

    you "I doubt he'll be interested in {i}my{/i} underwear..."

    hide gina with dissolve

    "She leaves, whistling as she clutches a bag full of strange gizmos. You wonder how many panties it cost her."

    you "Very well, let's pay a visit to this 'Papa Freak'..."

label c2_meet_papa_freak():

    play sound s_chimes

    scene black with fade
    show bg papa_freak at top with dissolve

    "Following the girl's directions, you enter a small, congested workshop lit by a strange magical apparatus."

    "An old man is listening to a youngster explaining his plan."

    papa_apprentice "So if we cross the red and green wires, and send an impulse through the mithril core, we should be able to reactivate the techno-mojo..."

    papa "Interesting theory, my boy... But aren't you forgetting something? How will the ethereal current react to a sudden surge in saturated mojo?"

    papa_apprentice "Uh? Well..."

    papa_apprentice "Oh no... You're right, the polar condensator will melt... *embarrassed*"

    papa "It's okay, boy... It's always worth it coming at a problem from a new angle. Even if you fail, you can learn something new that will help you solve the puzzle."

    papa_apprentice "Aw... I was so close to figuring out how to make that robot sex doll work..."

    you "*clear throat*"

    papa "Oh, who do we have here? Welcome, good sir! I apologize for our rudeness, we were deep into a technical discussion."

    you "It's alright."

    if MC.playerclass == "法师":
        you "By the way, you should try and use a soul-charged derivator. That's how we did it at the Karkyr Academy."

        papa_apprentice "A derivator... Of course! Why didn't I think about that?"

        papa "Ah, a fellow scholar... Welcome, indeed. It's always a pleasure to meet a learned gentleman."

    papa "What brings you to my humble workshop? Do you have a Cimerian device to repair, perhaps?"

    you "Cimerian device?"

    papa "Why yes, the ruins of the old city are brimming with them... All the working ones have long been looted, though. But amateur tinkerers have been known to try and repair them."

    papa "That is what we try to do here, me and my apprentice. Keep a bit of the old Cimerian civilisation alive, so to say."

    you "So the Cimerians are an ancient civilisation?"

    papa "Oh yes, more ancient than any recorded history. They had a mastery of magic we cannot hope to match nowadays, incorporating it into every mundane device."

    papa_apprentice "Well, magic is not the right word..."

    "The old man heaves a sigh."

    papa "Yes, 'demonic energy', if you must use that term."

    papa "But this is a gross misrepresentation of what the Cimerians were doing, one that elicits rejection from common people and the Church to this day."

    papa "The Ancients were channeling energy from the demonic planes, yes, but they had such mastery of it that it hardly ever caused problems. It's like comparing a hearth and a wildfire: they both use the same element, but the comparison stops there."

    you "And the Cimerians created all of these gizmos?"

    papa "Oh yes, and indeed they were the first settlers of the city that became known as Zan..."

    papa_apprentice "They disappeared long ago. No one knows what caused it."

    papa_apprentice "I wish we could find out..."

    papa "Patience, my boy, patience. The clues must be hidden under our very feet."

    papa "But again, we digress. Tell me, dear visitor, to what do we owe..."

    papa_apprentice "Hey, but I know him! Papa, don't you recognize him?"

    papa "Recognize him? Should I?"

    "He squints, looking at you better."

    papa "You do seem familiar..."

    papa_apprentice "Of course he is! Remember [brothel.name]? He's the owner!"

    if MC.girls:
        $ girl1 = MC.girls[0].name

        if len(MC.girls) > 1:
            $ girl2 = MC.girls[1].name
        else:
            $ girl2 = "Susan"

    else:
        $ girl1 = "Linda"
        $ girl2 = "Susan"

    papa "[brothel.name]? The place where [girl1] works? With the juicy titties?"

    papa_apprentice "That's the place!"

    papa "Oh, and I remember, just a few days ago you had that hot chick give you a good, hem, 'massage'. What was her name, already?"

    papa_apprentice "[girl2]! I think... I had so much to drink that night... Papa, we have to go back!"

    papa "Well, maybe this week-end then... Sir, we are honored to meet you. Since you've opened shop in our city, we've spent many a night enjoying your hospitality!"

    you "Well, I'm glad to see some satisfied customers."

    papa "Can we get discounts?"

    you "Nope."

    papa_apprentice "Aw..."

    you "Anyway. I came here to ask you a question."

    papa "Of course, of course. Shoot."

    you "Do you own the big house in the nearby square?"

    papa "Own it? Well, the owner is really the Count of Eajib..."

    papa_apprentice "Papa, come on. You're the Count of Eajib."

    papa "My ancestor was. I have no interest in such titles."

    you "Wait, you're a count? And you have a big-ass house? Why do you stay in this small and crappy shop, then?"

    papa_apprentice "Hey! Show some respect for our House of Miracles..."

    papa "Haha, son, that's a fair question."

    papa "I haven't got an appetite for luxury. What coin I have is better spent on fine whores as far as I'm concerned. And..."

    you "And?"

    papa "The house is useless to me, anyway. Dreadful place."

    you "Uh? Why?"

    papa_apprentice "The house has elemental resonance."

    you "Meaning?"

    papa_apprentice "It messes up with Cimerian technology. Big time. Usually ends in an explosion."

    papa "The family used magic-infused materials to build the walls, protection against their rivals' curses, I guess."

    papa "It causes unpredictable variations in elemental and demonic magic. We can't have that."

    you "Elemental magic, you say?"

    papa "I've tried for years to insulate the place so that I could work properly there, spent huge amounts of money... But it just wasn't possible."

    papa_apprentice "That's why Papa Freak opened shop here. The house is now just a big dust nest."

    you "Why didn't you sell it?"

    papa "Well, I could, but I'm already quite well-off as the sole inheritor of the Eajib family's fortune. Plus, it's got sentimental value..."

    you "But what if you sold it to someone you know? Someone who would open the coolest brothel in town?"

    papa "Well... I don't think..."

    papa_apprentice "Think about it, Papa Freak! We could have those juicy whores just next door! And you'd give us a good price, right?"

    you "Sure."

    papa "I don't know... I mean..."

    papa_apprentice "Come on!"

    "Papa Freak thinks to himself for a moment."

    papa "Well, I would consider selling it to you, on one condition..."

    you "What is it?"

    papa "{size=-20}I want a night with your best whore.{/size}"

    you "I'm sorry, come again?"

    papa "{size=-14}I want a night with your best whore.{/size}"

    you "Sorry, can't hear you."

    papa "I want a night with your best whore!" with vpunch

    you "Oh..."

    you "A night with... Yes, that could be arranged."

    papa_apprentice "Yay!"

    papa "But I'll have you know I have standards."

    papa "Listen up, young man..."

    scene black with fade

    "Papa Freak then spends the better part of half-an-hour listing every service he expects in excruciating detail. You realize his request may harder to fulfill than you thought."

    "Papa Freak wants to meet a girl who has {b}at least 50 in Beauty, Body, Refinement and Charm{/b}, and is open to whoring."

    if selected_district.name == "The Docks":
        $ _loc = seafront
    else:
        $ _loc = gallows

    $ _loc.action = True

    "When you are ready, visit the {b}[_loc.name]{/b} to bring Papa Freak the girl of his dreams."

    $ game.set_task("Bring a whore with {b}at least 50 in Beauty, Body, Refinement and Charm{/b} to Papa Freak, by the [_loc.name].", "advance2")

    return

label visit_papa():

    play sound s_chimes

    if game.chapter == 2:

        if MC.girls:
            "Choose a girl from your brothel to bring with you (reminder: she must have at least 50 in Beauty, Body, Refinement and Charm, and be open to whoring)"
            $ girl = long_menu("Choose a girl", [(g.name, g) for g in MC.girls])
        else:
            "You cannot satisfy Papa Freak's requests, as you have no girls in your brothel."
            return

        scene black with fade
        show bg papa_freak at top with dissolve

        "You came back to see old Papa Freak, in an attempt to convince him to sell his large house to you."

        papa "Oh, hello my young friend. I trust you've come with good news?"

        you "Hello, Papa. I would like you to meet someone."

        call dialogue(girl, "girl introduction") from _call_dialogue_102

        papa "Oh my, what a cutie..."

        papa "May I?"

        you "Sure."

        "Papa Freak pats [girl.name] gently on the butt, looking her up and down. He's almost drooling."

        call dialogue(girl, "slave whining") from _call_dialogue_103

        papa "Calm down, my child, don't be shy."

        if girl.get_stat("beauty") < 50:
            papa "Hmm... I appreciate that you took the time to introduce this young lady..."

            papa "But she's not really my type."

            "[girl.fullname]'s {b}beauty{/b} is too low (50 minimum)."

        elif girl.get_stat("body") < 50:
            papa "Hmm... I appreciate that you took the time to introduce this young lady..."

            papa "I just wish she had more curves, you know?"

            "[girl.fullname]'s {b}body{/b} is too low (50 minimum)."

        elif girl.get_stat("charm") < 50:
            "[girl.name] squirms and grumbles excuses, and Papa Freak frowns."

            papa "Thank you for bringing this young lady to me, but I wish she was more charming."

            "[girl.fullname]'s {b}charm{/b} is too low (50 minimum)."

        elif girl.get_stat("refinement") < 50:
            "[girl.name] squirms and grumbles excuses, and Papa Freak frowns."

            papa "Thank you for bringing this young person to me, but she isn't really lady-like."

            "[girl.fullname]'s {b}refinement{/b} is too low (50 minimum)."

        else:

            "Papa Freak proceeds to squeeze her breasts, rubbing her nipples through the fabric."

            play sound s_surprise

            girl.char "Aaah!"

            papa "Oh, she is really lovely..."

            papa "So this is true, then? I could have her all to myself, all night long?"

            you "Yes, of course... In exchange for selling me the house. That was the deal."

            if girl.will_do("whore"):

                papa "Shall we do this, sweetie? You will be mine for the night?"

                girl.char "If Master [MC.name] says so..."

                papa "Off we go, then! Hahahahaha..."

                scene black with fade

                play sound s_moans_short

                $ act = rand_choice([a for a in all_sex_acts if girl.does[a]])

                show screen show_event(girl.get_pic(act, "service", "naked", "profile", not_tags=["cumshot"]), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with dissolve

                girl.char "Oh, aaah, oooh!!!"

                papa "Heaven! This is heaven!!!"

                girl.char "I'm a bad girl, Papa..."

                papa "I'm at my limit... Take this!"

                show screen show_event(girl.get_pic(act, "service", "naked", "profile", and_tags="cumshot"), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with flash

                play sound s_orgasm_fast

                girl.char "Aaaah!!!"

                with doubleflash

                hide screen show_event
                scene black
                with fade

                play sound s_rooster

                "The next morning..."

                show bg papa_freak at top with dissolve

                papa "Thank you, [MC.name], you are a true friend!"

                "His voice shakes and his eyes almost well up."

                papa "This was truly a magnificent night, thanks to young [girl.name]. I felt like a young man again."

                papa "I'm getting old, you know... I am well into my third century, and I fear my days of womanizing will soon be over."

                you "Wait, what? You're 300 years old?!?"

                papa "Well, 323, if you must know. But I'm still spry, [girl.name] can attest to that, when she wakes up!"

                you "This is amazing... How did you live this long?"

                papa "Well, I know a thing or two about magic, of course... And let's just say Cimerian technology helped."

                papa "But enough about me... Young man, how would you like to visit your new house?"

                you "Yay!" with vpunch

                papa "There's only a small matter to settle first..."

                scene black with fade

                "Papa Freak is happy to leave the house to you for a paltry sum, but there are repairs to do on the house. A {i}lot{/i} of repairs."

                $ cost = bro_cost[3]

                "You are a little shaken to learn that the total bill amounts to a whopping {b}[cost] denars{/b}."

                $ seafront.action = False
                $ gallows.action = False
                $ plaza.action = False
                $ story_flags["c3_advance"] = True
                $ game.set_task("Gather " + str(cost) + " gold to advance to the next chapter.", "advance2", 3)

            else:
                girl.char "Wait, what? Spend the night with this old man? No way!"

                "She recoils in disgust."

                you "[girl.name]! Behave!" with vpunch

                papa "Oh my... Leave her be, please. I am not one to force a young lady against her will..."

                you "But..."

                papa "Sorry, but no deal. Please bring me a willing girl next time."

                "[girl.fullname] needs to accept {b}whoring{/b} to do this task."

    # elif game.chapter == 3:
        # call c3_papa_cells()

    return

label c3_homura_okiya3(): # Happens the night after moving to chapter 3.

    "It is the last night at your old brothel. It wasn't much, but you feel a bit of nostalgia about the place."

    "That night, you spot a familiar face in the okiya, drinking alone among the customers."

    if NPC_homura.flags["drunk sex"]:
        show bg homura_okiya sad at top with fade
        homura blush "Oh... [MC.name]..."

    else:
        show bg homura_okiya happy at top with fade
        homura normal "Over here! [MC.name]!"

    play music m_palace fadein 3.0

    you "Hello, Homura!"

    "She nods at the empty seat next to her, and you join her."

    homura normal "So... I hear you are moving?"

    you "Yes. But I won't be going far. I'm just moving over to the next district, found a nice place there."

    homura "Will you have an okiya there too? I'll visit you if you do."

    you "Sure, I'll just need a little time to set things up. Sill has already started moving our stuff."

    you "Should take us a few days to get the place up and running."

    homura "I see. Good for you."

    "You notice that she is drinking tea this time."

    you "You're not having sake tonight?"

    homura blush "N-No, I don't want to be drunk like... Last time... *blush*"

    if NPC_homura.flags["drunk sex"]:
        homura "I'm so sorry... You must think I'm a slut..."

        you "Of course not! Why would you say that?"

        "She glances around, taking in the view of scantily-clad girls flirting with drunk and rowdy customers."

        homura sad "Well... I suppose working in a place like this, you might lose perspective on this..."

        "You both sit silent for an awkward moment. She pouts for a little while, staring at her drink, but after a while, she relaxes her shoulders a little and seems to let go."

        "You try to lighten up the mood by broaching a different subject."

    else:
        homura normal "I'm grateful you reacted like you did... You're a true gentleman."

        you "It's nothing. I'm glad you got back home safe."

        homura "Oh, don't worry about me, I have my methods... *smile*"

    you "It's been a while since you last came. Does it mean your father's goons are cutting you a little slack?"

    show bg homura_okiya serious at top with dissolve

    homura sad "Well, no, but I'm getting better at avoiding them. I have been feigning illness recently, so now I manage to sneak in and out without anyone noticing."

    you "What do you do with your newly found free time?"

    show bg homura_okiya happy at top with dissolve

    homura normal "Mostly, I walk around in the forest West of Zan by myself, enjoying nature..."

    you "Isn't it a little risky? There could be bandits, or wild animals..."

    homura "Come on, you sound like my father! I'm all right. I can take care of myself."

    you "Sorry. I should know you're not a fragile flower, unlike some other ladies..."

    if NPC_homura.flags["drunk sex"]:
        "You have a flashback to the night you spent together. She guesses your thoughts."

        homura blush "Err... Thank you for saying that? *blush*"

    else:
        homura "Thank you for saying that."

    homura "I'm an adult. I don't like to be treated like a child."

    homura normal "Just because I'm small doesn't mean I don't pack a punch!"

    "You both laugh and have a toast to that."

    show bg homura_okiya serious at top with dissolve

    if NPC_homura.flags["divulged assignment"]:
        homura surprise "Say, [MC.name], where do you stand on your secret investigation? Hunting the mysterious ninjas around the city?"

        you "I think I'm making progress. I've managed to corner one of them not once, but twice, and learn some valuable information."

    else:
        homura surprise "So, I hope your work for the Princess is going well... But I know better than to pry. You made it clear it's a secret."

        you "Yeah, sorry about that, but this is private business. I've been progressing fine, I suppose."

    homura normal "Well, if at any point you become stuck, you can rely on me. I hear a lot of gossip at court, and I can find various ways to help you."

    homura "You won't regret it, I promise!"

    if NPC_homura.flags["divulged assignment"]:
        homura normal "Those kudo-... kuro-... kunobichi... don't stand a chance against us! We're a team!"

        you "Yeah..."

    else:
        homura surprise "You don't even need to tell me what it's all about. If you need help I'll answer, no questions asked."

        you "It's very generous of you. Thank you."

    show bg homura_okiya happy at top with dissolve

    homura normal "Let's have another toast! To friendship!"

    menu:
        "To friendship!":
            $ renpy.block_rollback()
            you "To friendship! *laugh*"

            if NPC_homura.flags["drunk sex"]:
                you "(With benefits...)"

                homura normal "What was that?"

                you "Oh, nothing, hahaha..."

            else:
                homura normal "Yes..."

            $ NPC_homura.love -= 1

        "Friendship?":
            $ renpy.block_rollback()
            you "Friends? I thought we could be more than that..."

            "She blushes."

            homura blush "[MC.name]... What would you like it to be, then?"

            menu:
                "Lovers!":
                    $ renpy.block_rollback()
                    you "You know what I would want it to be..."

                    "Deliberately, you place your hand on her hand. She flinches slightly, but doesn't take it away."

                    homura blush "You know, I can't say that I wouldn't like it..."

                    $ NPC_homura.love += 1

                "Adventure buddies!":
                    $ renpy.block_rollback()
                    you "We could be... Adventure buddies!"

                    play sound s_laugh

                    homura normal "Hahahaha!"

                    "She laughs heartily."

                    homura "You and me, travelling around the world, facing insurmountable odds... I like that!"

                    "She grabs your arm."

                    homura "You can do the cooking, and I'll protect you from danger! We could have all kinds of adventures!"

                    you "Deal! *smile*"

                    $ NPC_homura.love += 2

    "You order some platters of food from the kitchen and eat together, chatting pleasantly."

    with fade

    you "My, you eat an awful lot for a Lady! You were so eager that you almost stuck your fork in my hand!"

    homura normal "I'm just hungry you know! I don't usually have such large meals!"

    you "Are they starving you in your dad's palace?"

    homura sad "Uh, no, of course not... But my father worries about my health constantly... He has me on a diet."

    if dice(3) + MC.get_charisma() > 6:
        "That answer sounded somewhat forced. You figure there must be more to it than this."

    you "You shouldn't eat too much either, you know, it's not healthy..."

    homura surprise "Hey! Were you about to call me 'fat'?"

    you "No, of course not..."

    "She leans back, nonchalantly giving you a good look at her figure."

    homura sad "Tell me the truth, am I fat?"

    you "You know very well you're not fat. You have a fine body."

    homura normal "Hahaha! You're being honest, I can tell..."

    "Stretching like a cat, she sighs contentedly."

    play sound s_sigh

    homura "That was a nice meal! Thank you, Mister [MC.name]."

    you "My pleasure. But it's getting late... Will you be going?"

    homura "Hmm..."

    "She looks at you with a playful smile. Her cheeks are red, even though she didn't drink."

    homura blush "No, I think not."

    you "Uh?"

    homura "I don't want to head back. I guess I'm staying the night."

    you "Really? Okay then, I'll have a room ready for you..."

    homura "There's no need, really. I'm staying in yours."

    if NPC_homura.flags["drunk sex"]:
        you "I see... Like last time, uh?"

        homura blush "Sure... But this time it won't be as easy for you as taking advantage of a drunk girl!"

        you "We'll see about that... *smile*"

    else:
        you "You're not... drunk, are you?"

        "You eye her tea suspiciously."

        homura normal "Not at all!"

        homura blush "I just know what I want... And I want it now..."

    stop music fadeout 3.0

label homura_sex(first=True):

    scene black with fade

    "Later, in your bedroom..."

    play sound s_dress

    show bg homura_naked1 at top with dissolve

    "Removing her kimono, Homura lies naked on your bed, blushing."

    if first:
        you "Is... Is this your first time?"

        play sound s_surprise

        homura naked "N-Not at all, believe it or not... But I guess I feel shy around you..."

        you "You are brave, coming into a man's room like that... Are you sure you can handle everything I throw at you?"

        homura "Depends... What do you plan on throwing?"

    play sound s_dress

    "You remove your clothes, and she gasps at the sight of your erect manhood."

    show bg homura_naked2 at top with dissolve

    if first:
        homura "You're big, bigger than... Will it really fit inside me?"

        you "There's only one way to find out..."

    "You kiss her passionately. She kisses you back, prudently at first, then with more fervor."

    play sound s_mmh

    homura naked "Ngh, ngh..."

    "Running your hands against her naked body, you trace the length of her slender arms, her shoulders, then cup her firm breasts."

    show bg homura_naked3 at top with dissolve

    play sound s_ahaa

    homura "Ahaa! [emo_heart]"

    "Rubbing your palms against her perky nipples, you enjoy watching her squirm and sigh as you play with her boobs. She is very sensitive."

    if first:
        you "Who would have thought that the young lady was such a sexy kitty..."

        homura "S-Stop teasing me..."

        you "Alright..."

    show bg homura_sex1 at top with dissolve

    play sound s_aah

    homura "Aaaah..."

    "You place one hand on her leg, pushing her thighs open."

    "You move in between her legs, taking a good look at her exposed pussy. In turn, she can't turn her gaze away from your large cock."

    homura "Wait, don't go too... Aaaah..."

    play sound s_sucking

    "Still playing with her boob, you start licking her smooth body all over."

    homura "Oh, this is good, oh..."

    you "*lick* *lick*"

    show bg homura_sex2 at top with dissolve

    "The room gets hot, and her body is getting covered in sweat and saliva. You move up and your cock brushes against her leg, then her inner thigh, then rubs against her pussy."

    "You can feel it getting moist now."

    if first:
        homura "You're driving me crazy..."

        you "This is just the beginning..."

    show bg homura_sex3 at top with dissolve

    "You push your dick inside her, slowly but firmly."

    play sound s_surprise

    homura "Ooh... I can't..."

    "Her pussy clutches your cock tight. You start moving."

    play sound s_scream

    homura "Oh, you're so big! Oh! OH!!!" with vpunch

    "Her cries echo through the brothel, matched by other muffled cries coming from other rooms."

    play sound s_moans

    "Your cock slides slowly in and out of Homura's pussy. She is very tight, and you guess it must be hurting, but she seems lost in the feeling and not minding it."

    homura "You're making me yours... It's amazing..."

    show bg homura_sex4 at top with dissolve

    "She dares to open her eyes, looking dreamily at where you two are joined. She breathes heavily with every thrust."

    you "Are you ready to go faster?"

    homura "Y-Yes... Yes."

    "You don't need to be told twice, and you increase your pace, fucking her more forcefully."

    play sound s_aah

    homura "Ah! AH! AAAH!" with vpunch

    "You feel like you are being too rough, but you can't help yourself. She doesn't seem to mind, on the contrary."

    "You notice how her petite body is perfectly shaped, thin and muscular, with not an ounce of fat outside of her protruding breasts. Just how you like it."

    you "(Young women are great...)"

    homura "Oh, [MC.name]... It's amazing... I think I will, aah... I will..." with vpunch

    "Unexpectedly, her pussy grips your hard cock really hard, and she explodes, bringing you over the top."

    play sound s_scream_loud

    homura "AAAAAAH!!!" with vpunch

    play sound s_orgasm

    show bg homura_sex5 at top with flash

    "Unable to stop yourself, you cum a huge load inside her, as her whole body shivers uncontrollably."

    with doubleflash

    homura "Aaaah..."

    if first:
        homura "You made me c-cum... It was so intense... And it's only our first time..."

        you "There's more where that's coming from..."

        homura "Oh, [MC.name]..."

    scene black with fade
    play sound s_orgasm_fast

    $ unlock_achievement("h homura")
    $ MC.change_prestige(2)

    "Laying in each other's arms, it isn't long before you are ready for round two. And three."

    "After you are both sated, you lie together in your bed, catching your breath."

    show bg homura_rest2 at top with fade

    if not first:
        "She sighs with contentment."

        play sound s_sigh
        homura naked "Aw... I could get used to this..."
        scene black with fade

        return

    elif NPC_homura.flags["drunk sex"]:
        homura naked "Just like last time... You're really something..."

    else:
        homura naked "I've pictured this moment... But I wasn't ready."

    homura "I can't believe it... We're crazy-compatible, it's like our bodies are made for each other..."

    menu:
        extend ""
        "I think so":
            $ renpy.block_rollback()
            you "I think so too... You look innocent and shy, but when we're in bed together... It's like fireworks!"

            homura "I-I know, right? I'm happy to hear you feel the same..."

            $ NPC_homura.love += 1

        "It's just me":
            $ renpy.block_rollback()
            you "Actually, It's like that with every girl I meet. I have a gift..."

            show bg homura_rest3 at top with dissolve

            homura "Oh. Way to ruin the mood. You could at least {i}pretend{/i} I'm special..."

            you "Sorry..."

            $ NPC_homura.love -= 1

    show bg homura_rest4 at top with dissolve

    homura "I'm getting sleepy... You don't mind if I spend the night here with you?"

    you "Not at all... I enjoy the company."

    show bg homura_rest2 at top with dissolve

    homura "Thank you. You're doing me a favor..."

    homura"Please don't forget I can help you too, okay?"

    # you "I guess, but... How can I contact you again? It's not like I can show up at your rich dad's mansion uninvited."
    #
    # homura "Oh, right. Here, take this. My blue ribbon."
    #
    # "She picks up the ribbon that tied her hair from the night stand, and hands it over to you."
    #
    # call receive_item(blue_ribbon, use_article=False)
    #
    # you "Your ribbon?"
    #
    # homura "Yes. When you need to see me, just tie this to the flag pole in the center of the Plaza... I'll know you want to see me, and I'll come visit as soon as I can."
    #
    # homura "But you'll need an okiya. Your other facilities are a bit too seedy for me..."
    #
    # you "Tie this to the flag pole at the Plaza, once I have an okiya... Got it. Thank you. "
    #
    # show bg homura_rest1 at top with dissolve
    #
    # homura "You're welcome... [MC.name]..."

    show bg homura_rest1 at top with dissolve

    homura "Zzzz..."

    you "And she's asleep..."

    "You look at her pensively."

    if MC.get_alignment() == "good":
        you "She's a nice girl... And I'm a brothel owner. I should be careful not to break her heart."
    elif MC.get_alignment() == "neutral":
        you "Look at me, just a few weeks back I was struggling to make ends meet in the Slums, and now I'm sleeping with nobility... Way to go, [MC.name]!"
    elif MC.get_alignment() == "evil":
        you "It's always nice to bang a noble girl for novelty, but it shouldn't make me lose track of the important stuff. Let's see how the brothel is doing."

    scene black with fade

    # $ plaza.action = True
    $ game.set_task(None, "advance2") # Clears advance2 goals
    $ NPC_homura.flags["H level"] = 1

    return

label homura_mast(first=True):

    "You gasp as she lays back on your bed, spreading her legs to give you a better view."

    scene black with fade
    show bg homura_mast1 at top with dissolve

    if first:
        homura naked "[MC.name]... I've been thinking about this moment since we first met... Hmm..."

        you "H-Have you?"

    play sound s_mmh

    homura naked "I've touched myself many times thinking about you... But..."

    play sound s_sucking

    homura "it's different when you are looking on... Hmmm..."

    "She starts playing with herself, still looking into your eyes. The room fills with wet noises as she toys with her moist pussy."

    homura "Am I giving you a good view? Aaaah..."

    you "Perfect..."

    show bg homura_mast2 at top with dissolve

    "Her juices start running from her wet pussy."

    homura "I know I have a small body, but... I hope you don't mind..."

    you "Not at all... *gulp*"

    show bg homura_mast3 at top with dissolve

    "She starts playing with her breasts and fingering herself, begging you to look at her. You can feel a bulge in your pants as your dick gets rock hard."

    homura "What's that? Is it your... Hmmm..."

    if first:
        you "Homura... I didn't know you were so naughty..."

        "She looks at you with an air of defiance."

        homura "Oh, you have no idea... I am no dove, you'll see... *wink*"

    "She fingers herself deep, now, splashing love juice over your bedsheets. Unable to resist, you slowly move closer to get a better look."

    if first:
        homura "Do you like the shape of my women parts, [MC.name]? What does an expert like you think... Hmmm..."

        you "It's beautiful, ahem..."

        homura "Come on... Look closer!"

        "You bring your face closer between her legs, until your face is only inches from her wet cunt."

    homura "Oh, I can feel your breath on my..."

    play sound s_ahaa

    homura "Aaaaah..."

    play sound s_aaah

    show bg homura_mast4 with flash

    homura "AAAAAH!!!"

    play sound s_orgasm

    with doubleflash

    "Love juice splashes everywhere as she cums unexpectedly, arching her back towards you. You look on with fascination."

    show bg homura_mast5 at top with dissolve

    homura "Oh, aah... I came already... I didn't expect this..."

    "She looks dreamy for a little while, almost as if she forgot your presence."

    if first:
        "Eventually, she looks back at you, her eyes burning with feverish intensity."

        homura "Oh, [MC.name]... There's one more thing I need to see."

    else:
        homura "That was intense... You gave me such an erotic look..."

    return

label homura_bj(first=True):

    scene black with fade

    if first:
        "Still tipsy, Homura crawls on all fours towards you, then proceeds to drop your pants."

        homura "Let me meet this bad boy..."

    show bg homura_bj1 at top with dissolve

    play sound s_surprise

    homura naked "Oh!"

    "Homura lets out a surprised scream as your cock pops out and nearly hits her."

    homura "Oh, my, you're so hard already... Is it because of me?"

    you "Of course..."

    "She looks flattered."

    homura "Well, poor dear, I can't leave you in that state... Let me help."

    play sound s_sucking

    "Homura starts licking the length of your shaft, shyly at first, then with increasing enthusiasm."

    homura "Hmm, nngh..."

    show bg homura_bj2 at top with dissolve

    if first:
        "Her cheeks flushed from arousal and alcohol, Homura doesn't hesitate before taking your dick in her mouth."

        homura "Nggh..."

    "She sucks on your cock with surprising strength, locking her lips around your shaft. She has some technique, you can tell it isn't her first time."

    homura "Nggh, ngggh..."

    "She even tingles your balls with her right hand, playfully squeezing them."

    you "Careful..."

    homura "Teeheehee..."

    show bg homura_bj3 at top with dissolve

    "You can't help but move further in, sliding your cock up and down her throat."

    homura "Nggh!"

    "Homura closes her eyes as you push your cock deeper inside her, yet she opens her mouth wide to accommodate you."

    homura "Ngggh... Nggh..."

    "She starts massaging your cock with her tits as well, which are bigger than you thought at first."

    play sound s_mmmh

    homura "Hmm... Aah..."

    "Her saliva drips down your cock as you slide up and down between her boobs. Her erotic moaning brings you closer to your limit."

    homura "Nggh... Hmmm... *suck*"

    "Homura looks up at you lewdly, while licking the sweat off your cock. Her erotic face is enough to bring you over the top."

    menu:
        "Cum on her face":
            $ renpy.block_rollback()
            show bg homura_bj1 at top with dissolve

            homura "Hmmm... Do you lik-"

            play sound s_surprise
            show bg homura_bj4 at top with flash
            homura "Whoah!"

            with doubleflash

            "Homura is surprised by your cum spurting out, landing on her face and hair."

            with flash

            homura "Oh, I wasn't expecting.... Hmmm..."

            "Holding your dick in her small hand, Homura strokes it slowly to make the last of your cum come out."

            homura "Hehehe, I'm so nasty... Hmmm..."

            "She spits out a bit of cum that landed in her mouth, then smiles mischievously."

        "Cum in her mouth":
            $ renpy.block_rollback()
            show bg homura_bj3 at top with dissolve
            homura "NGGGH!"

            "Homura is surprised as you grab her head and shove your cock back in."

            homura "Nggggh..."

            show bg homura_bj5 at top with flash

            "Your cum spurts out like a geyser, filling her mouth."

            homura "NGGH!!! *gulp* *cough*"

            "Homura struggles to keep your cock in her mouth, and ends up coughing and spitting cum on the bedsheets."

            homura "Ugh, hnngh... It's too much... Aaah..."

            "Watching Homura panting, with cum dripping down her expensive kimono, you wonder if you went too far."

    $ MC.change_prestige(2)

    return


#### END OF CHAPTER 2 EVENTS ####
