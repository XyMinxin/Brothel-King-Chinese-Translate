####            INTRODUCTION                ####
##  This is the content of the game intro     ##
##                                            ##
####                                        ####


## INTRO START ##

label intro:

    $ persistent.seen_intro = True

    $ text1 = Text(('Once upon a time'), size=50, yalign=0.5, xpos=0.5, drop_shadow=(2,2), font="bk.ttf")
    $ text2 = Text(('In a far away realm'), size=50, yalign=0.5, xpos=0.5, drop_shadow=(2,2), font="bk.ttf")

    show expression text1
    with easeinleft

    pause 0.8

    hide expression text1
    with easeoutright

    pause 0.8

    show expression text2
    with easeinleft

    pause 0.8

    hide expression text2
    with easeoutright

    play music m_wind

    call init_game() from _call_init_game_1

    pause 0.8

    $ sill_name = "???"
    $ MC.name = "你"


    sill unknown "Master!"

    sill "Master... {w}Please wake up!"

    show bg sky dusk at top with circleout

    pause 0.5

    show sill happy with dissolve

    play sound s_chimes

    pause

    you "Sill?"



    $ sill_name = "希露"



    sill happy "Yes, Master! Finally, you're awake."

    sill "We are nearing the city limits. The farmers we passed said we should see the highest towers after we leave the valley."

    stop music fadeout 3.0

    scene black with fade

    show bg valley dusk at top with dissolve

    "It seems your long trip across Xeros is coming to an end."

    "On the other side of this valley is the city of Zan, jewel of the Eastern coast."
    "Already the most powerful city in Xeros by far, Zan grows by the day with the arrival of travelers and migrants from all over the continent, and beyond."

    "You are one of them, lured by stories of the riches and pleasures that can only be had in the 'City of Jade'..."
    "But you didn't set out to become just another faceless adventurer lost in the mean streets of the city-state."

    "You set out...{w=1.0} {b}{color=[c_darkred]}to become a King!{/color}{/b}{w=1.0}{nw}"

    play music m_theme

    $ title = Text(("Brothel King"), size=80, yalign=0.4, xpos=0.5, drop_shadow=(3,3), font="bk.ttf")

    show expression title #Note: Find a way to make the zoom slower and the title cooler
    with zoomin

    ""

    stop music fadeout 2.0

    scene black with fade



    $ renpy.call("chapter", 0)



    scene black with fade

    show sill past at truecenter with dissolve

    "Sill was your first slave."

    play music m_suspense

    hide sill
    show bg sill sold
    with fade

    "Her parents sold her to you with their last good horse to repay a gambling debt."

    scene black with fade

    show sill past at truecenter with dissolve

    "You trained her to follow your every whim and desire, and taught her about the world. You are the only family she has now."

    "You sold all of your slaves in a hurry before starting your journey, but somehow you couldn't let go of Sill."

    show sill past at centerleft with move

    menu:
        you "Why did I keep her already?"

        "I'm kind of fond of the girl.":
            $ MC.good += 1
            $ NPC_sill.love += 1
            $ norollback()
            you "Well, she is more than a simple slave. Roaming this land wouldn't be the same without her."

        "She's an investment.":
            $ MC.neutral += 1
            $ norollback()
            you "Sell her and what, do my own laundry? Obedient slaves are so hard to come by these days..."

        "Beats me. She's a waste of space.":
            $ MC.evil += 1
            $ NPC_sill.love -= 1
            $ norollback()
            you "Never cared for the little brat. But someone has to drive the carriage when I'm sleeping..."

    menu:
        you "Besides, we have some good memories... Like that time..."

        "The first night I trained her":
            $ MC.good += 1
            $ NPC_sill.love += 1
            $ norollback()
            jump sill_first_time

        "The time we did it in public":
            $ MC.neutral += 1
            $ norollback()
            jump sill_public

        "I spanked her silly":
            $ MC.evil += 1
            $ NPC_sill.love -= 1
            $ norollback()
            jump sill_spank


label sill_first_time:

    scene black
    show bg sill finger
    with fade

    play sound s_moans_quiet loop fadein 1.0

    sill past "Oh! Master! Oh!"

    sill "I feel so... Aaaah..."

    show bg sill sex with fade

    play sound s_moans_short

    sill "Oh, aaaah! Maaaster..."

    sill "Master, aaaah... I'm... I'm cumiiiiing!!!"

    play sound s_orgasm

    with flash

    jump resume_intro


label sill_public:

    scene black
    show bg sill bj
    with fade

    play sound s_sucking fadein 1.0

    sill past "Mahhher... Thehe ahe childhhen... Mmmh... coming..."
    you "Hahaha... Let them look!"
    you "I bet they've never seen a cock-hungry slave like you sucking a dick from up close!"
    sill "Mahher!!! Donh't..."

    play sound s_mmmh

    with flash

    jump resume_intro


label sill_spank:

    scene black
    show bg sill fetish
    with fade

    sill past "What's... What's going on?"

    with vpunch

    play sound s_scream

    sill "Ow!"

    you "Silence, whore! You will only talk when addressed."

    with vpunch

    play sound s_scream

    sill "AAAHA!"

    you "Since you cannot seem to get the basics of discipline through your thick skull, I'll beat it into you proper."

    you "But first, let's see if I can fit THIS into your slutty little hole."

    play sound s_scream_loud

    sill "Aaaah!!!"

    jump resume_intro


label resume_intro:

    stop music fadeout 2.0
    stop sound fadeout 2.0

    scene black with fade

    play music m_wind fadein 2.0

    sill happy "...and that's how the Pharo dynasty rose to power in Zan, or so the innkeeper said. Fascinating story, isn't it, Master?"

    show bg sky night at top with dissolve

    show sill happy with dissolve

    sill "..."

    sill sad "Master? Were you listening?"

    you "Uh... Well..."

    sill happy "Look, Master! We've reached the outer wall!"

    scene black with fade

    show bg outer wall at top with dissolve

    stop music fadeout 2.0

    "Zan is well protected from outside dangers by a series of moats, walls and garrisons."
    "The city has never fallen before any foe, even during the time of the Goliath invasion."
    "That is not to say that Zan is a peaceful city, however. Its rulers are constantly brought down by plots and internal strife."
    "A perfect place for an adventurous soul to make a fresh start..."

    show bg outer gate at top with fade

    show guard at center with dissolve

    "A guard is staring at you, frowning. He barely glanced at Sill."

    guard "Who goes there?"

    $ MC.name = renpy.input("我是...", default = MC_name, length = 20)

    guard "[MC.name]? Odd name, for sure."

    sill happy "I am but a slave, sir. My name is..."

    guard "Silence, slave! No one cares who you are." with vpunch

    guard "State your business, stranger."

    menu:
        you "I am..."

        "A warrior":
            $ MC.set_playerclass("Warrior")
            $ norollback()

            you "I am a fighter from the Northern armies."

            hide guard
            show bg battleground at top with fade
            "For years you have battled hordes of humans and monsters, far away North in the Holy Lands."
            "You fought side by side with great knights and lowly sellswords. In the heat of battle, peasants and highborns were comrades."
            "Battles were won, and battles were lost, always at a dear cost. Most of your friends ended up dead or missing."
            "You have grown tired of the constant fighting and senseless bloodshed. This is not your calling anymore."
            "Still, your set of skills is always in demand in Xeros. Time will tell if life in Zan will allow you to put your swords down for good..."

            show bg outer gate with fade
            show guard with dissolve

            guard "We have great respect for veterans here, Sir."
            guard "But do mind your manners while in town. Our quiet urban community is not to be 
                mistaken for a battleground."

            jump resume_intro2


        "A wizard":
            $ MC.set_playerclass("Wizard")
            $ norollback()

            you "I am a court mage from the Westmarch Principalities."

            hide guard
            show bg palace at top with fade

            "Educated with the best minds of Karkyr to become a battlemage, you used the gold from an inheritance to buy off your years of service, and set out for the Western territories for fame and fortune."
            "There, you found your place as the court wizard of one Prince Arkin, a powerful border lord."
            "The hundred warring Princes in Westmarch are always in need of a wizard for counsel enchants, and healing. And sometimes, for more underhanded duties as well... For the powers of life and death are woven into the fabric of magic itself, and a potent spellcaster can easily wield both."
            "The Prince had a beautiful wife... And a jealous, suspicious mind."
            "Somehow, he got it into his thick head that you had been sleeping with his wife, using spells to bypass the guards posted by her chambers."
            "You got word of this madness a few hours before he planned to have you arrested and burnt at the stake. You escaped swiftly with Sill and what little valuables you could carry."
            "Not forgetting to pay a last visit to the Princess on your way out, of course..."
            "Zan seems like a good place for you to lay low for a while, and leave that nasty business of stakes and pyres behind."

            show bg outer gate with fade
            show guard with dissolve

            guard "A wizard!"

            "He spits."

            guard "There is no shortage of self-proclaimed mages and witches in Zan. I won't stop you... But wherever your kind goes, trouble is sure to follow."
            guard "I'll keep my eye on you, wizard, so don't step out of line. Otherwise it'll be my pleasure to escort you out of the city... or to the pit."

            jump resume_intro2

        "A rogue trader":
            $ MC.set_playerclass("Trader")
            $ norollback()

            you "I am a proud member of the Xeros Traveling Merchant Guild."

            hide guard
            show bg caravan at top with fade

            "A native of Borgo, the harbor city, you grew up on the docks, buying and selling all kinds of legal and less legal merchandise from overseas for a profit."
            "Before long, you decided to venture into the wild world, to see for yourself the wonders sailors and travelers had been mumbling about in their cups."
            "You went to the furthest corners of Xeros and back, and even sailed the Blood Sea. But your latest trip was nearly your last."
            "Your party had set out for the legendary Southern land of Hokoma, roaming through scorching desert and sweltering jungles."
            "Your aim was to negotiate with native tribes for the rarest spices and magical ingredients, to exchange for cheap trinkets."
            "Amazingly, you made it to Hokoma with only a few casualties, and most of your wares still intact."
            "But on the way back through the jungles, as you were busy dreaming of the riches you 
            were sure to obtain back in Borgo, your party got ambushed and slaughtered by a ferocious headhunting tribe."
            "You and Sill barely made it out with your lives, losing all of your stock while escaping."
            "Returning to Borgo empty-handed to face your creditors didn't seem like the brightest idea. So instead, you decided to head for Zan, and use your business acumen to 
            rebuild from there."

            show bg outer gate with fade
            show guard with dissolve

            guard "A peddler, eh? You don't seem to have a lot of goods about. Seen better
                luck, haven't you?"
            guard "Well, any man can make it in the City of Jade, or so they say. But stay on the right
                side of the law, merchant, or you will have to deal with me."

            jump resume_intro2

label resume_intro2:

    guard "One more thing. Which god do you worship, [MC.playerclass]?"

    menu:
        you "Me?"

        "I am a servant of Arios, god of Light and Strength":
            $ MC.set_god("Arios")
            $ MC.good += 1
            $ norollback()
            guard "That is good, brother. I hope to see you often at the Cathedra to pray."

        "I worship Shalia, goddess of Shadows and Cunning":
            $ MC.set_god("Shalia")
            $ MC.evil += 1
            $ norollback()
            "He spits on the ground."
            guard "I knew you had that sneaky look about you... There are many shrines dedicated to
                the dark goddess in Zan, but I'm not the one to tell you where they are. Decent folks shouldn't meddle with the cursed one."

        "I serve none but myself":
            $ MC.set_god(None)
            $ MC.neutral += 1
            $ norollback()
            guard "What have we here, a free thinker? You must think oh so highly of yourself, not
                needing the protection of gods and all?"

    "Please take a moment to review your choices now. You won't be able to change them after this point."

    call choose_difficulty() from _call_choose_difficulty_1

    guard "All right, move along now. And be quiet. Good people are already asleep at this hour."

    hide guard with dissolve

    sill sad "Aw, what a bully..."

    "You lead the horses through the gate, and leave the carriage and animals at the nearby stables."

    "With Sill following you, you step forward decisively, into the dark streets of Zan."

    stop music fadeout 2.0

    scene black with fade

    with flash
    play sound s_lightning

    you "Oh no..."

    you "It's raining now."

    with flash
    play sound s_lightning

    scene bg dark street with fade
    play music m_rain

    you "Sill, hurry up! We have to find an inn."

    sill sad "Yes Master, *pants*, I'm doing the best I can... *pants*"

    "Sill is carrying all your equipment and luggage. She's never been too strong, so she is nearly
    crumbling under its weight."

    you "Hurry up now will you... What's that?"

    play sound s_woman_scream

    $ kuro_name = "陌生女人"

    kuro "Aaaaaaah!" with vpunch

    kuro "Help me!"

    "In a dark alley on the side of the plaza, a woman is standing with her back to the wall. Two
    men are blocking her way out."

    menu:
        "What do you do?"

        "Run to her rescue":

            $ MC.good += 1
            $ norollback()

            "Charging in the back alley without a moment of hesitation, you reach the men just as
            they're closing in on the helpless woman."

            you "What's going on here?"

            show kuro at right with dissolve:
                zoom 0.9

            kuro "Please, my good lord, please help me! These men are here to kill me!"

            show thug1 behind thug1 with dissolve:
                xalign 0.1
                yalign 1.0

            show thug2 behind thug1 with dissolve:
                xalign 0.3
                yalign 1.0


            thug1 "Now, now, citizen, don't you listen to that lying bitch. We're here on...
                official business."
            thug2 "Yeah, orficial..."
            thug1 "'n we're just takin' her to be... interrogated."
            thug2 "Yeah, in taro gated..."
            thug1 "So no cause for alarm, here, you see... Now be on your way, citizen, for your
                own sake."
            thug2 "Yeah, that's none of yer business! So back off, will ye."

            you "..."

            you "Did you think I'd fall for that, punks?"

            jump resume_intro3


        "Taunt her attackers":

            $ MC.neutral +=1
            $ norollback()

            you "Well, what do we have here?"

            show kuro at right with dissolve:
                zoom 0.9

            kuro "Please, my good lord, please help me! These men are here to kill me!"

            show thug1 behind thug1 with dissolve:
                xalign 0.1
                yalign 1.0

            show thug2 behind thug1 with dissolve:
                xalign 0.3
                yalign 1.0

            "You take a derisive look at the two henchmen."

            you "Two big men attacking a lone woman.."

            you "Such bravery! They'll sing songs about you!"

            thug2 "You..."
            thug1 "Careful boy... This is not your fight, so back off now!"

            you "So those are the faces of cowardice... Ugly faces, to be sure..."

            thug2 "Whaddaya mean by that, the feces of kawadice? Speak proper Xerossi, dammit!"

            you "It means you're a big, nasty piece of shit, and that I'll have to clean up my boot real good after I shove it in your face!"

            thug2 "Ya hear that cousin? He's ansultin' us! Let's take him!!!"

            jump resume_intro3


        "Ignore her plea":

            $ MC.evil += 1
            $ norollback()

            show kuro at right with dissolve:
                zoom 0.9

            kuro "Help me! These men are here to kill me!"

            you "This is none of my concern... Sill, let's go."

            kuro "Please, someone, anyone! Please help!"

            sill "But... Master..."

            you "Shut up, Sill, and move it. We're leaving this place."

            thug1 "Wait a minute!"

            show thug1 behind thug1 with dissolve:
                xalign 0.1
                yalign 1.0

            thug1 "What have we here?"

            thug1 "So you two little birds have been eavesdropping, uh?"

            you "Dammit."

            show thug2 behind thug1 with dissolve:
                xalign 0.3
                yalign 1.0

            thug2 "What were they droppin', cousin?"

            thug1 "Eavesdropping you idiot! It means they've been listening to us, and you know
                what the boss said... No witnesses."

            thug2 "Oh, that's right..."

            thug2 "Hey, cousin, did you see that lil' hotty, with the pink hair?"

            thug2 "I'm gonna have me some fun with her! After we're through with the noble
                bitch..."

            you "..."

            you "I don't think so."

            jump resume_intro3


label resume_intro3:

    thug1 "..."

    thug1 "All right, then... You just dug your own grave, you nosy bastard!"

    if MC.playerclass == "Warrior":
        you "Sill, fetch my swords."

    if MC.playerclass == "Wizard":
        you "Sill, hand me the staff."

    if MC.playerclass == "Trader":
        you "Sill, you know what to do."

    sill "Yes Master!"

    kuro "Watch out!"

    show thug1 attack

    show thug2 attack with flash

    play sound s_sheath

    thug1 "Now..."
    thug2 "You..."
    thug1 "DIE!"

    if MC.playerclass == "Warrior":

        you "Haa!"

        play sound s_sheath
        with hpunch

        thug1 "Aaaw!"

        play sound s_sheath
        with hpunch
        with flash


        "You dodge the first thug and shove him to the side, before slicing up and severing the arm
        of the second thug clean off."

        play sound s_wscream
        thug2 "Aaaaargh!!!"

        "Before he can recover from the pain, you plunge your second blade in his throat."

        play sound s_sheath
        with vpunch

        thug2 "Aaarh... Arrhhh..."

        "The bandit coughs bubbles of blood as life drains out of his eyes."

        hide thug2 with dissolve



    elif MC.playerclass == "Wizard":

        you "Shazam!"

        play sound s_lightning
        with flash

        show thug2 burnt with move:
            xalign 0.4
            time 0.5

        show thug1 attack with move:
            xalign 0.0
            time 0.5

        thug2 "AAAAAAAAARRRRRRRRHHHHHHHHH!!!"
        play sound s_wscream

        "A bolt of lightning thunders down from the dark skies, striking one thug and
        blinding the other one."

        thug1 "Cou... cousin?"

        hide thug2 with dissolve

        "The fool burnt to a crisp. He didn't stand a chance."



    elif MC.playerclass == "Trader": ##TO DO : have Drogon hover around

        play sound s_wings

        thug1 "What?"

        play sound s_roar
        drogon "Hyarrrrrrr!"
        play sound s_fire
        with flash

        "Before the thug could get close, he was engulfed in flames."

        play sound s_wscream

        show thug2 burnt with move:
            xalign 0.4
            time 0.5

        thug2 "AAAAARRRRRRGHHH!!!"

        hide thug2 with dissolve

        thug1 "Wh... What sorcery is this???"

        you "Haha! Meet Drogon, my pet."

        play sound s_roar
        drogon "Rrrr!"

        play sound s_wings loop
#        show drogon at truecenter with dissolve

        thug1 "A pet... Dragon???"

        you "Yes, a pet dragon! I acquired this one in the far East, all the way across the Blood
            Sea, when he was but an egg."

        you "I retrieved it from the funeral pyre of some petty nomad king, incinerated with his
            western bride and a slave witch, if you can believe it. But long story short..."

        you "Do you want to be his next snack so badly?"

        stop sound


    thug1 "You... Damn you!"



    play sound s_steps fadein 0.5 fadeout 0.5

    hide thug1 with dissolve

    "The surviving thug turns tail and runs for his life."


    scene bg dark street with fade

    stop sound

    show kuro at right with dissolve:
        zoom 0.9



    $ kuro_name = "贵族小姐"



    kuro "Thank you, my champion, you fought bravely."

    if MC.playerclass == "Trader":

        show sill drogon at left with dissolve

        sill "Well, Drogon did most of the work! Teehee..."

        play sound s_roar fadein 1.0 fadeout 1.0
        drogon "Rrrrh!"

        sill "You're tired now, aren't you? Poor little baby is too young to fight..."

        you "Shut up, you two!"

    else:

        show sill at left with dissolve

        sill happy "Yes! Master is the best!"

        you "Please. It was nothing."


    kuro "Thank you, from the bottom of my heart."

    kuro "Forgive me though, but I have to leave now. Others like them are on my trail, and I
        must make it to safety as quickly as I can."

    kuro "But you have saved my life, and my honor. I am in your debt."
    kuro "Seek the house of master Gio. He is a friend of my family, and he will reward you."

    sill "But wait, who..."

    hide kuro with dissolve
#    play sound s_steps fadein 0.5 fadeout 0.5

    "Without a word, the lady bows politely, and bolts past you and Sill, disappearing into the
    night."

    sill "I hope she'll be ok..."

    you "Well, she's out of our hands now. But let's check out that Gio fellow."

    sill "We can ask at the next inn."

    you "She looked like a high-born lady, and attractive to boot. This might be my lucky day..."

    stop music fadeout 2.0


    scene black with fade

    play sound s_knocks

    "*knock* *knock* *knock*"

    stop sound

    $ maid_name = "女人的声音"

    "..."

    maid "What is it?"

    you "I apologize for coming at such a late hour. I need to speak with master Gio."

    maid "..."

    maid "Yes, come in my lord."

    play sound s_door

    scene bg desk with fade

    show maid normal at center with dissolve

    $ maid_name = "女仆"

    maid "Welcome, my lord."
    maid "I will take you to master Gio."

    scene black with fade

    show bg office at top with dissolve

    show maid normal at right with dissolve

    maid "Master, your guest has arrived."

    show gio at center behind maid with dissolve

    gio "Ah, very well, Minako. You may leave us."

    $ maid_name = "美奈子"

    maid "Yes master."

    hide maid with dissolve

    you "Greetings, master Gio. My name is..."

    gio "I know who you are. [MC.name], the [MC.playerclass]. Sit down and relax, you're among
        friends."

    you "Wait... How?"

    gio "I am Gio Fratello, or Shady Gio, as they call me."

    gio "One of my jobs is to know about anyone unusual who comes and goes in this city. And that alone is a lot
        of work..."

    you "I see. Gio, I apologize for the late hour..."

    gio "Oh, don't sweat it. The Princess said you would come over, and I do most of my business at
        night, anyway."

    $ kuro_name = "公主"

    you "The Princess?"

    gio "Ah, yes of course, the Princess. Could it be you don't know who she is?"

    gio "You're from a faraway land, I forgot..."

    gio "Well, I'm not going to spoil the surprise here. I'm sure you'll meet her properly when the
        time is right."

    sill sad "Wait! Don't leave us hanging there!"

    gio "Hahahaha! I got where I am now by asking questions, not answering them, little girl."

    gio "Anyway, friend, I'm sure you're tired from your trip, and eager to get some rest."

    gio "But indulge me for a few moments, if you will, because we need to discuss your reward."

    you "I'm all ears."

    gio "The Princess mentioned a certain sum of money... {w}That I don't have available right now."

    gio "In fact, I don't expect to have such cash ready anytime soon."

    you "*frown*"

    gio "But wait... It is my understanding that you have come to the city to strike it rich, am I
        right?"

    you "..."

    gio "So I am ready to offer you something a lot better than petty cash... And of similar value to
        the reward the Princess wanted me to give you."

    you "Go on."

    gio "What do you know about power, young man?"

    you "Power?"

    gio "Yes. What is power?"

    you "Hmm."

    if MC.playerclass == "Warrior":
        you "Power... hangs at the tip of a sword."

    elif MC.playerclass == "Wizard":
        you "Power resides in magic."

    elif MC.playerclass == "Trader":
        you "Money is power."

    gio "Haha, it is true to some extent, my friend."

    gio "But even that is not 'true' power."

    you "Then what?"

    gio "Sex."

    you "Uh?"

    gio "Sex is where real power resides."

    sill "S... Sex?"

    gio "Yes, sex! Everything is about sex, sweetheart... Except sex."

    gio "Sex is about power."

    sill "..."

    you "Fascinating lecture, professor, but can we move on to the part about my reward?"

    gio "Ah yes, my impatient friend, of course. What do you think drives this city? Who do you
        think pulls the strings of our stupid king and his clique?"

    menu:
        "Who?"

        "The illuminati guild?":
            gio "*roll eyes*"

        "Kaizer Sauze?":
            gio "*roll eyes*"

        "Yo mamma?":
            gio "*facepalm*"

    gio "No! It's the {b}brothel masters{/b}."

    sill "The... Brothel masters?"

    play music m_mafia fadein 2.0 fadeout 2.0

    scene black with fade

    gio "Yes dear, the brothel masters. They're the power behind the throne, and everything else."

    show bg throne room day at top with dissolve

    gio "You see, nobles and their court..."

    show king at center

    $ renpy.transition(dissolve, layer="master")

    extend "{w=0.5}{nw}"

    show gknight behind king:
        xalign 1.4
        yalign 0.2

    $ renpy.transition(dissolve, layer="master")

    extend "{w=0.5}{nw}"

    show priest behind king:
        xalign 0.95
        yalign 0.15
        zoom 0.95

    $ renpy.transition(dissolve, layer="master")

    extend "{w=0.5}{nw}"

    show mage behind king, priest, princess2:
        xalign 0.5
        yalign 0.1
        zoom 0.9

    $ renpy.transition(dissolve, layer="master")

    extend "{w=0.5}{nw}"

    show princess2 behind king:
        xalign 0.1
        yalign 0.15
        zoom 0.95

    $ renpy.transition(dissolve, layer="master")

    extend "{w=0.5}{nw}"

    show princess1 behind king:
        xalign -0.4
        yalign 0.2

    $ renpy.transition(dissolve, layer="master")

    extend "{w=0.5}{nw}"

    gio "They're always acting all high and mighty during the day..."

    show bg throne room night with dissolve

    gio "But at night... When no one is looking..."

    hide gknight with dissolve
    hide priest with dissolve
    hide mage with dissolve
    hide princess2 with dissolve
    hide princess1 with dissolve
    hide king with dissolve

    scene black with fade

    show gknight fucked at topright with dissolve:
        zoom 0.8

    gio "They unleash their base instincts..."

    show priest fucked at topleft with dissolve:
        zoom 0.8

    gio "... not caring for gods or morals..."

    show mage fucked with dissolve:
        yalign 0.8
        zoom 0.8

    gio "...they revel in depravity with their willing servants..."

    show princess2 fucked with dissolve:
        xalign 1.0
        yalign 0.8
        zoom 0.8

    gio "...even sometimes, their own children and siblings..."

    show princess1 fucked with dissolve:
        xalign 0.5
        yalign 0.3

    gio "...but they can never fully sate their dirty appetites."

    scene black with fade

    show princess fucked at top with dissolve

    gio "That is why they need the brothel masters."

    show bm1 with dissolve:
        alpha 0.2
        xalign -0.2

    show bm1 with smove:
        alpha 0.8
        xalign 0.0

    show bm2 with dissolve:
        alpha 0.2
        xalign 1.2

    show bm2 with smove:
        alpha 0.8
        xalign 1.0

    gio "The brothel masters cater to the needs of Zan's privileged citizens, bringing them refined and perverse pleasures from out of this world."

    show princess fucked:
        alpha 0.8

    gio "They are men and women who work in the shadows, procuring nobles and rich citizens alike the
    vices they crave."

    gio "They can provide any kind of 'entertainment' if you have the gold: women, fairies, animals,
        even monsters... They can indulge your every possible fantasy."

    gio "This gives them {b}true{/b} power. They know every one of their customers' dirty secrets..."

    hide bm1 with easeoutleft

    hide bm2 with easeoutright

    hide princess with dissolve

    gio "They say even King Pharo I is the pawn of a powerful brothel master, a fellow by the
    name of 'Cloud'. {i}I{/i} have never met him, however. And I know {i}everyone{/i} in Zan. Almost."

    stop music fadeout 5.0

    gio "So, you see. In this city, to be powerful, you need to master and control the sex trade..."



label shortcut:

    scene black with fade

    show bg office at top with dissolve

    show gio with dissolve


    gio "And I... can help you. *grin*"

    you "You? How?"

    gio "You see, I decided to dabble in whore management myself."

    gio "But I'm more of a, err, creative type, not a micro-manager... I'm especially bad with accounting..."

    gio "So, long story short, I opened a cathouse last year and, hem, ran it into the ground."

    gio "All the girls left, but the house is still in order."

    gio "I've decided I'm not good at this racket, but you... You can take over the whorehouse if
        you want."

    gio "This will be your reward: this way, I get to fulfill my obligation to the Princess, and you
        get a place to stay and conduct your business. What do you think?"

    menu:
        "Well..."

        "Of course!":
            $ text1 = "Of course"
            jump resume_intro4

        "Sure!":
            $ text1 = "Well, sure"
            jump resume_intro4

        "Fuck yeah!":
            $ text1 = "Fuck yeah"
            jump resume_intro4

label resume_intro4:

    sill sad "Respectfully, Master, I don't think..."

    you "[text1] I'm interested! I just hope the brothel is in good condition and all..."

    gio "Well, of course, of course... Erm... *nervous*"

    gio "We'll discuss that tomorrow. Right now you must be tired from your trip and need to rest."

    gio "I'll have Minako prepare a room for you. Allow me to be your host tonight."

    gio "Speaking of which..."

    you "Yes?"

    gio "I've noticed you have brought with you a fine looking slave. Nice piece of ass really..."

    show sill sad at right with dissolve

    "He gets up and moves closer to Sill."

    sill "Ma... Master?"

    gio "Would you allow me to use her for the night? In exchange, you can have Minako. She's a very
         devoted little bitch, that one."

    play sound s_surprise

    "He starts fondling Sill's ass over her kimono."

    sill "Master!!!"

    menu:
        sill "He's... He's touching my butt!"

        "Stop it already!":
            $ gio_fucked_sill = False
            $ NPC_sill.love += 1
            $ MC.good += 1
            $ norollback()

            you "Stop it Gio! She's mine."

            you "You can't touch someone's slave without her master's consent."

            gio "Aw, come on, friend! Is this a way to treat your host?"

            you "Sorry, Gio, but that's final."

            gio "All right, then."

            "He looks pissed."

            gio "Minako!"

            show maid normal at left with dissolve

            maid "Yes Master?"

            gio "Take those two lovebirds to the guest room."

            "His voice is cold."

            gio "And come to my bedchambers after that, bringing the SM equipment. I need
                to blow off some steam."

            maid blush "Understood, Master."

            gio "Good night then."

            hide gio with dissolve

            "He leaves, almost slamming the door on his way out."

            maid blush "Master..."

            scene black with fade

            show bg room at top with dissolve

            show sill happy with dissolve

            sill "Thank you Master! Thank you thank you thank you!!!"

            you "Sill, don't overdo it."

            sill "But... Master Gio is old, fat and sleazy... I hated it when he touched me."

            sill "..."

            sill "But... I like it when we... You know..."

            show sill naked with fade

            sill "Master... Come..."

            hide sill with dissolve
            show bg nogiofuck1 with dissolve

            play sound s_moans_quiet loop

            sill naked "Master... Aaaah... You're always looking out for me..."

            show bg nogiofuck2 with dissolve

            sill "Even though... I'm just... Aahh... Your slave... Mmmh..."

            show bg nogiofuck3 with dissolve

            sill "But I... Uuuuhhh..."

            sill "I... Aaaaaah..."

            play sound s_moans_short loop

            show bg nogiofuck4 with dissolve

            sill "Ooooh yes Master... Yes..."

            sill "Master, you're so fast... Hnnn... Hnnnnn..."

            sill "Aaaaaaaah!!!"

            play sound s_orgasm

            with doubleflash

            stop sound fadeout 3.0

            pause 2.0

            show bg nogiofuck5 with fade

            play sound s_moans_short loop fadein 3.0

            sill "Master... We've been doing it... Aaaah... for hours..."

            sill "I think, aahhhh... We need to... mmmmh... rest, ah!"

            you "We'll rest... just... not... yet..."

            you "Raaah!!!"

            sill "Oh, aaah... Aaah!!!"

            show bg nogiofuck6 with dissolve

            play sound s_orgasm
            with flash
            sill "Aaaaaaahaaaaah!!!"

            $ unlock_achievement("h sill1")

            stop sound fadeout 3.0

            scene black with fade

            "And so went the rest of the night..."

            jump day1


        "Maybe another time, Gio...":
            $ gio_fucked_sill = ""
            $ MC.neutral += 1
            $ NPC_sill.love -= 1
            $ norollback()

            you "Look, Gio, it's tempting... But we're all tired."

            you "Sill won't be any good after such a long time on the road. She's dirty..."

            gio "I don't mind..."

            you "...and exhausted."

            you "Maybe next time, ok?"

            sill "Next... time??? But..."

            gio "I see..."

            gio "Yes, of course, you both need some rest."

            gio "I am looking forward to our next meeting, sweetie. *grin*"

            play sound s_surprise

            "He squeezes her breast before letting go."

            gio "Minako, where are you?"

            show maid normal at left with dissolve

            maid "Right here, Master."

            gio "Take our guests to their room, will you. Then, meet me in my room with the
                'toybox'."

            maid "Yes, Master."

            scene black with fade

            show bg desk at top with dissolve

            show sill sad with dissolve

            sill "Master... I don't want to sleep with that old man! He's sweaty and gross!"

            you "And you won't have to..."

            sill happy "..."

            you "...tonight."

            sill sad "Whaaat?"

            you "You need to learn to respect my wishes, Sill. You are my slave, and I'm the
                one calling the shots."

            sill "..."

            sill "Yes, master."

            you "Come on now, let's get some rest."

            sill happy "Finally..."

            scene black with fade

            show bg room at top with dissolve

            show sill sad with dissolve

            sill "Master! Can you hear???"

            play sound s_screams

            you "Come on Sill... I'm trying to sleep here... Let them have their fun."

            sill "Buuut..."

            "Ignoring her, you fall into a long, deep sleep..."

            play sound s_scream_loud

            scene black with fade

            jump day1


        "Sure, why not?":
            $ gio_fucked_sill = True
            $ MC.evil += 1
            $ NPC_sill.love -= 2
            $ norollback()

            you "Sounds fun! You can have her."

            sill "Whaaaat?"

            gio "Fantastic!"

            sill "Wait!!!"

            gio "Come with me my dear."

            play sound s_scream

            "He squeezes her butt and whispers in her ear."

            gio "You will be mine all night, sweetie..."

            sill "Nooo..."

            you "So, where's Minako?"

            show maid normal at left with dissolve

            maid "Yes Mister [MC.name]. You called?"

            gio "Minako, take him to the guest room. Make sure he feels... Very welcome."

            maid blush "..."

            maid blush "Of course, Master Gio."

            gio "Now dear, come with me."

            sill "But... But..."

            you "You heard the man, Sill, go with him. And make sure to give him a great time."

            sill "*sob*"

            hide sill with dissolve
            hide gio with dissolve

            maid "Follow me now, my lord."

            scene black with fade

            show bg room at top with dissolve

            show maid normal with dissolve

            maid "So..."

            maid blush "What do you request of me, Master [MC.name]?"

            menu:

                "Ask for a blowjob":

                    $ norollback()

                    maid "Of course my lord, please allow me to make you feel good..."

                    play sound s_sucking loop

                    hide maid
                    show bg gioblow1 with dissolve

                    maid blush "Hmmm... It's already hard, my lord... Were you waiting for this?"

                    show bg gioblow2 with dissolve

                    maid "It's bulging... Should I slide it deeper in my throat?"

                    maid "Just hhike hhat... Mmmmh..."

                    maid "Mmmmmhhh!"

                    play sound s_mmmh

                    with flash

                    show bg gioblow3 with dissolve

                    "You come all over her face and hair. She engulfs your shaft in her mouth as
                    you keep cumming, trying to make sure to drink some of it."

                    "She makes wet noises, swallowing your hot cum eagerly."

                    maid "Please, my lord... Allow me to clean you up..."

                    stop sound fadeout 3.0

                    jump maid_fuck


                "Fuck her where she stands":

                    $ norollback()

                    "Instead of answering, you push her hard against the wall."

                    play sound s_mmmh

                    maid "Ohh my lord... You're so forceful!"

                    "Ripping her panties aside, you lift her legs up and start fucking her raw."

                    hide maid
                    show bg giofuck1 with dissolve

                    play sound s_moans_mature_quiet loop
                    maid blush "Aaaaaah!"

                    maid "Master [MC.name]... is so hard!"

                    maid "You're... drilling me!!!"

                    "Even though you've just started shoving your dick in her, she is already
                     completely wet."

                    you "You're already wet, aren't you, you little slut?"

                    show bg giofuck2 with dissolve

                    maid "Aaaah, yes my lord... Yes..."

                    maid "I'm... a dirty... slut..."

                    play sound s_moans_mature loop

                    "You start fucking her faster and faster."

                    maid "Ooh, yes, oooooh!"

                    maid "My lord! My pussy... is yours... Fuck... Fuck it harder!"

                    show bg giofuck3 with dissolve

                    play sound s_orgasm_fast loop

                    maid "Oh yes, oooooh..."

                    you "I'm not done with you yet..."

                    stop sound fadeout 3.0

                    jump maid_fuck

label maid_fuck:

    scene black with fade

    play sound s_moans_mature_quiet loop

    show bg giofuck4 at top with dissolve

    maid blush "Ooooh my lord... You're so... big..."

    "It's hard to believe how wet she is. You can slide in and out of her with ease, even though
     she is very tight."

    maid "Oh yes, master [MC.name]! Do it like this..."

    maid "Hnnnnnnnn..."

    play sound s_moans_mature loop

    show bg giofuck5 with dissolve

    maid "Oh my lord... Ooooh..."

    maid "Ahhaaaaa!"

    maid "Yes, oh yes... I'm... I'm..."

    show bg giofuck6 with dissolve

    play sound s_orgasm_fast

    with doubleflash

    maid "CUMMIIIIIIIING!!!"

    show bg giofuck7 with dissolve

    maid "Aaaaaah..."

    maid "Master [MC.name]... It was so good..."

    maid "Would you... fill me up again?"

    stop sound fadeout 3.0

    scene black with fade

    "Meanwhile, in Gio's room..."

    play sound s_scream_loud

    sill naked "Ahaaaaaahh!!!"

    play sound s_moans_short

    show bg giofuck8 at top with dissolve

    with flash

    gio "Aaaaaaaarhhhh!"

    with doubleflash

#    play sound s_orgasm

    sill "AAAAAAHHHHH!!!"

    sill "..."

    sill "How... How many times can you come... you... monster..."

    gio "Hahaha! We're not even halfway done!"

    gio "Come on, bitch, now turn around and spread your buttcheeks for me."

    sill "But... But..."

    gio "Oh, yes... Exactly. *grin*"

    scene black with fade

    "And so the night went..."
    $ unlock_achievement("h maid")

    jump day1


label day1:

    scene black with fade

    pause 0.5
    
    if starting_chapter <= 1:
        $ renpy.call("chapter", 1)

    gio "Behold!"

    play music m_market fadein 3.0

    show bg slave market1 at top with fade

    gio "The Zan slave market."

    show bg slave market2 at top with fade

    "For centuries, slave traders from all of Xeros have converged on Zan to buy and sell the finest
     slaves on the continent."

    show bg slave market3 at top with fade

    "They are used for most everyday tasks and are expected to provide all kinds of
     services... They are what their masters want them to be."

    show bg slave market9 at top with fade

    "Slaves cannot address free people unless spoken to. And, most importantly, slaves can
     never raise a hand against their betters. This is a very grave offense."

    show bg slave market10 at top with fade

    "Which is why warriors are usually free men and women, except for some of the pitfighters
     who fight against monsters or other slaves."

    show bg slave market5 at top with fade

    "But of course the most sought after are the sex slaves."

    show bg slave market4 at top with fade

    "Girls from all over Xeros born, sold, or coerced into slavery, are trained to
     become perfect sex kittens."

    scene black with fade
    show bg slave market6 at topleft with dissolve:
        xalign 0.1
        yalign 0.0

    "Some are trained the hard way, until they're broken into submission."

    show bg slave market7 as bg2 with dissolve:
        xalign 0.9
        yalign 0.0

    extend "\nOthers learn to love their life as a slave, begging for their Master's attention."

    hide bg with dissolve
    hide bg2 with dissolve

    show bg slave market8 at top with dissolve

    "All learn to do their Master's bidding, no matter what."
    "It is a powerful bond: only the Master can set them free."

    scene black with fade

    "Zan has the most bustling slave market in all of Xeros..."

    show bg slave market11 at top with fade

    you "A good place to start my new life."

    gio "Aaaah, the slave market! The colors, the scents, the tastes!"

    sill sad "Master! Someone tried to grab my breast! Hey, I'm not for sale!"

    gio "The slave market is the place to buy slaves to have them work in your brothel."

    gio "You need at least one girl to start your new business. Here, have [starting_gold] denars."

    you "Why, thank you Master Gio..."

    gio "Oh, don't thank me! This is what I got from selling your horses and carriage this morning. You won't be needing them anyway..."

    with vpunch

    you "What!!! Why you... [starting_gold] denars! It was worth at least twice that!!!"

    gio "Oh, well, these are hard times... I'm afraid slaves are not the best quality at that price, but your training will make all the
         difference, I'm sure. Hehehe..."

    if starting_chapter == 1:
        call advance_to_chapter(starting_chapter, silent=True, start=True) from _call_advance_to_chapter_2
    else:
        $ slavemarket_firstvisit = False
        $ brothel_firstvisit = False
        $ girls_firstvisit = False

        call advance_to_chapter(starting_chapter, silent=False, start=True)

        jump main

    # # SET UP CALENDAR
    # $ calendar.updates()

    # # Create enemy general for the siege security event

    # if dice(2) == 1:
    #     $ enemy_general = get_girls(1, free=True, p_traits=["Warrior"])[0]
    # else:
    #     $ enemy_general = get_girls(1, free=True, p_traits=["Caster"])[0]

    # $ enemy_general.love = -50

    # if starting_chapter > 1:
    #     call debug_load_chapter(starting_chapter) from _call_debug_load_chapter_1

    jump slavemarket


label slavemarket_first_time:

    hide screen girl_tab
    hide screen girl_profile
    hide screen girl_stats
    hide screen button_overlay
    with dissolve

    gio "Good, you have now bought your first slave."

    sill happy "Ahem."

    gio "Ok, your second slave then."
    gio "Oh, by the way. Will you be using Sill as a whore?"

    if gio_fucked_sill:
        gio "As I know from personal experience, she's quite alright in the sack... *wink*"

    sill sad "Whaaaat? Master, no!!!"

    you "Hmmm..."

    if MC.get_alignment() == "good":
        you "No, Sill is my personal slave and I don't want to share her with all of Zan."
    elif MC.get_alignment() == "evil":
        you "She is a dumb slut, but her skills are lacking. Maybe I'll use her later, as a cum
             dump for unsatisfied customers."
        sill "Noooooo!!!"
    else:
        you "No, Sill will help with other tasks. I need someone to handle the reception,
             the accounting, the laundry, the groceries, the cooking, the cleaning..."
        "The list goes on and on and Sill looks aghast."

    ## TO DO: Implement Sill as a functioning working girl?

    gio "As you wish."

    "Gio starts inspecting the slave you just bought."

    "He fondles her butt and pinches her nipples."

    play sound s_surprise

    girl.char "Aaaaah!"

    if girl.get_stat("body") >= 20:
        gio "This girl has a good body. Look at those juicy boobs... Mmmmh."
    elif girl.get_stat("beauty") >= 20:
        gio "This girl is not bad looking. Even if she's useless in bed, she will still attract
             customers who want to fuck a pretty slut."
    elif girl.get_stat("charm") >= 20:
        "[girl.name] slaps Gio's hands off."
        girl.char "Come on now, keep your hands to yourself, granpa."
        gio "What the..."
        gio "Well, this girl has spirit. Customers like girls with personality."
    elif girl.get_stat("refinement") >= 20:
        gio "She looks quite ladylike, for a cocksucking slave. Maybe she will attract more than the usual rabble, I wonder?"
    else:
        gio "I don't really see what she's good for. But it's your choice, of course."


    you "Hmmm..."
    you "Anyway, stop babbling old man."
    you "It's time you showed us the house."

    gio "Yes, well..."

    $ slavemarket_firstvisit = False

    jump districts_first_time


label districts_first_time:

    scene black with fade

    gio "First, I must tell you some things about the city layout."

    show bg zan at top with fade

    gio "Zan is a huge city, with many different neighbourhoods called districts."

    show bg rich district with fade

    gio "Some districts are home to the aristocrats and the wealthy..."

    show bg poor district with fade

    gio "...others are home to the poor and humble who toil in the shadows."

    show bg zan with fade

    gio "Every district requires a specific license to open a business within the district limits."

    gio "To get a license, of course, you need to have the right political and business connections... Something which isn't easy to achieve."

    you "What are you trying to say..."

    gio "Well..."

    gio "I don't, err, have a proper license per se..."

    you "What?"

    gio "... so the only place I could open a brothel was..."

    show bg slum district with fade

    gio "... the slums."

    with vpunch

    you "Whaaat???"

    gio "But don't you worry, my young friend..."

    gio "You see, people living in the slums might not be very well off..."

    you "*evil stare*"

    gio "All right, most of them are drifters and beggars."

    gio "But like everyone in Zan, they need sex, and what little money they get, they spend on girls and spice."

    gio "So, while I didn't succeed in making the brothel business take off, I'm sure you will find a way to turn a profit. My instinct tells me so..."

    if MC.playerclass == "Trader":
        you "Well, I will have to rely on my legendary business acumen..."

    else:
        you "Yeah, whatever..."

    scene black with fade

    $ game.chapter = 0

    show screen districts("first visit")
    with dissolve

    gio "From here, you can see the various districts of Zan."

    gio "Right now, you can only open your brothel in the slums."

    gio "Later, you may unlock other districts if you have the proper license."

    $ game.chapter = 1

label districts_first_time_slums:

    $ narrator("Choose a district.", interact = False)

    $ ui.interact()

    "The Slums are located on the outskirts of Zan, beyond the defensive wall. It is home to the
     Zani rabble: new arrivals, refugees, paupers, spice addicts... It is also rumored to host
     the hideout of the Thieves Guild, and a temple of the Goddess Shalia."

    if not renpy.call_screen("yes_no", "Do you really want to choose the Slums to open your new brothel?"):
        jump districts_first_time_slums

    $ district_firstvisit = False
    $ norollback()

    stop music fadeout 3.0

    "This is a poor place to start a business, but Gio didn't leave you much of a choice."

    hide screen districts


label brothel_first_time:

    scene black with fade

    gio "Behold! Your new home."

    play music m_gio fadein 3.0

    show expression bg_bro at top with dissolve

    you "..."

    you "You've got to be kidding..."

    sill sad "What's... What's that smell?"

    gio "Oh, err... We are located downwind from the nearby junkyard."

    gio "Don't you worry, you'll get used to it in no time."

    you "..."

    if MC.playerclass == "Warrior":

        you "I'll rip your head off..."

    else:

        you "Are you crazy! This place is a dump!"

    gio "Calm down, my friend, calm down..."

    gio "I assure you, this is more than good enough for the rabble that lives in this district."

    sill "It looks... small and shabby."

    gio "Well... So do you, sweetheart, and still you've got some tricks up your skirt! *wink*"

    play sound s_surprise

    sill "Grrr..." with vpunch

    gio "This place is small, but there are bedrooms in the cellar downstairs."

    gio "Right now, only one is usable, though."

    gio "Also, you will need to entertain your customers in a common room while they wait their turn for more... private action."

    gio "Those common rooms serve as a front for the business, just in case the Guard becomes too nosy."

    gio "New girls will start working in the common rooms, until they are comfortable enough taking guests to the bedrooms."

    gio "Currently, all the common rooms are in disrepair."

    sill "Ew, I think this one was used by vagrants... As a toilet!"

    you "So... This brothel is useless as it is, then..."

    you "*hardcore evil stare*"

    if MC.playerclass == "Warrior":

        "Gio looks nervous as you start fiddling with your scabbard."

    elif MC.playerclass == "Wizard":

        "Gio looks nervous as you start muttering a curse."

    elif MC.playerclass == "Trader":

        "Gio looks nervous as you start eyeing your pet dragon."

    gio "I see that you are not quite pleased with my gift... so I'll throw in a bonus."

    gio "Craftsmen working for me will come this afternoon, and they'll repair one of the common rooms. This should get you started."

    gio "There are 4 types of common areas. You get to pick the one you like best."


    show bg waitress at top with fade

    gio "The {b}tavern{/b} will allow you to train your girls as {b}waitresses{/b}."

    gio "Waitresses with good {b}charm{/b} will keep the customers entertained."

    gio "With time, they will start wearing sexy uniforms and providing all kinds of 'entertainment' to the customers."

    show bg stripper at top with fade

    gio "The {b}strip club{/b} will allow you to train girls as {b}dancers{/b}."

    gio "You should pick girls with a good {b}body{/b} to be Dancers."

    gio "With time, they will remove more and more clothing, and take the customers to a room for a 'private dance'."

    show bg masseuse at top with fade

    gio "The {b}onsen{/b} will allow you to train girls as {b}masseuses{/b}."

    gio "Masseuses should be {b}beautiful{/b} girls, to attract customers to the onsen."

    gio "With time, they will give erotic massages to the customers, and eventually provide them with 'full service'."

    show bg geisha at top with fade

    gio "The {b}okiya{/b} will allow you to train girls as {b}geishas{/b}."

    gio "Geishas should be {b}refined{/b}, elegant and witty. Not that the riffraff around here knows anything about class, mind you... But that's the job description."

    gio "With time, they'll learn a thousand ways to please their customers, and how to take care of their more... 'special' requests."

    hide bg

    show expression bg_bro at top
    with fade

    gio "So now, choose carefully..."

    $ tt = show_tt("top_right")

    show screen brothel()
    with dissolve

    $ renpy.say(gio, "Which one of the common rooms do you want me to repair?", interact = False)

    $ mychoice = ""

    while not brothel.has_room():

        $ operation = ""
        $ room = None

        $ operation, room = ui.interact()

        if operation == "add_room":
            $ room.buy(forced=True)

            pass

    hide screen brothel
    hide screen tool
    with dissolve

    $ room = brothel.get_common_rooms()[0]

    gio "So, I see you've chosen the {b}[room.name]{/b}. A good choice, my friend!"

    gio "I will be back soon with the craftsmen. They will turn this place around in no time."

    scene black with fade

    play sound s_knocks

    $ brothel_firstvisit = False

    stop music fadeout 2.0

    jump main_first_time


label main_first_time:

    scene black with fade

    $ room = rand_choice(brothel.get_common_rooms())

    $ renpy.show("bg " + room.name, at_list = [top])
    with dissolve

    gio "Tadaaa!"

    gio "The [room.name] is in order now."

    gio "I'll leave you to it then. Don't forget to assign your girl to work there for the big
    opening tonight."

    $ unlock_achievement("intro")

    call chapter(1) from _call_chapter

    show sill happy with fade

    sill "Finally!"

    sill "That old, disgusting guy is gone!"

    you "Yes. Now what do we do?"

    sill "Master [MC.name], our first order of business is to find a name for your brothel."

    sill "Gio's old place was just called 'Cunts Galore'. Just goes to show his complete lack of class."

    sill "Oh, I know! How about, 'The Rose Garden'? That sounds more poetic, don't you think?"

    $ brothel.name = renpy.input("你想把青楼的名字改成什么?", default = brothel.name, length = 40)

    if brothel.name.lower() == "the rose garden":
        sill "Yay! I'm glad you liked it."
        $ NPC_sill.love += 1
    elif brothel.name.lower() == "cunts galore":
        sill sad "Ew! Master! Not that name again!"
        you "Shut up, Sill. I call the shots here."
        sill "Aw..."
        $ NPC_sill.love -= 1
    else:
        sill "Oh, well, that's a good name too, I suppose."

    sill happy "While the workers were busy, I went over the old accounting books."

    sill "The old geezer was as bad as he said he was at managing the business, but I think I got a rough
          idea of how things work."

    sill "Let us visit your girl, and I will explain."

    hide sill with dissolve

    $ main_firstvisit = False

    jump girls_first_time
