#### CHAPTER 1 STORY EVENTS ####

label c1_gio_is_back:

    if debug_mode:
        return

    $ renpy.block_rollback()

    play music m_gio fadein 3.0

    play sound s_door

    scene black
    if brothel.get_common_rooms():
        $ room = brothel.get_random_room_pic_path()
    else:
        $ room = "black"

    show expression room at top
    with fade

    sill sad "Finally, Master, you're back!"

    gio "Hi there!" with vpunch

    show gio with dissolve

    gio "If it isn't my old buddy, [MC.name]..."

    sill sad "He's been here for an hour, helping himself to our food and drinks, and trying to molest me!"

    gio "Why, is that any way to welcome a guest? This slave of yours should be disciplined, you know."

    you "Come on Gio, what's your business here?"

    gio "I bring good tidings, friend! I have found a way to get you a proper brothel license."

    you "Go on..."

    gio "It will not exactly be easy, but I know this gal... Look, if you can raise {b}[game.goals[0].value] denars{/b},
         we should be able to afford a new place and bribe the city guard for our first license."

    sill "That's... That's a lot of money!"

    gio "Well, it is, but think of the great things we could do after leaving this dump! Our chances of getting bit by a rabid dog
         would be lower, for starters."

    you "Hmm."

    you "All right then, let's do this. Now scram, Gio, we have a lot to do."

    gio "Oh, how rude... Mind if I take that bottle with me? Oh, and those, they're tasty."

    you "Hey!"

    gio "See ya!"

    play sound s_door_close

    hide gio with dissolve

    sill sad "I don't like this..."

    stop music fadeout 2.0

    return


label c1_meet_kosmo:

    $ renpy.block_rollback()

    hide screen home
    hide screen tool

    stop music fadeout 2.0

    scene black with fade
    show expression bg_bro at top with fade

    show sill with dissolve

    sill sad "Master!"

    sill "Look out... There are some strange men lurking around the house..."

    hide sill with dissolve

    play music m_kosmo

    show kosmo with dissolve

    pause 1.0

    show henchman at right behind kosmo with dissolve

    pause 0.5

    show henchman as henchman2 at left behind kosmo with dissolve


    kosmo "..."

    kosmo "Look at this place! So this is '[brothel.name]'? It's pathetic!"

    "You step out to inquire about the stranger's business."

    kosmo "Oh, and this must be the sorry loser on whom Gio dumped this filthy hovel..."

    kosmo "Well, hello there, simpleton!"

    menu:

        "Who are you?":

            $ renpy.block_rollback()

            you "Who the hell are you?"

            kosmo "Oh, it speaks our language..."

        "Get out.":

            $ renpy.block_rollback()

            you "Hey, you!  Get the hell out of my property!"

            kosmo "Oh, believe me, I will... The stink alone is enough to make one want to avoid this place at all costs..."

            kosmo "I just wanted to have a look at this place before it's torn down... Bwahaha!"

            you "What? What do you mean???"

        "Yo mamma!":

            $ renpy.block_rollback()

            you "Well, this filthy hovel was good enough for your mamma... We made a killing yesterday thanks to her."

            kosmo angry "What? Why you... Grrr!"

            kosmo angry "..."

            kosmo happy "Anyway, no need to lose my temper over a worm like you."

        "SKIP (debug)" if debug_mode:
            return

    kosmo "You must be wondering why a gentleman like myself felt compelled to pay your dirty shack a visit..."

    you "No, not really."

    kosmo "My name is...{w=1.0}{nw}"

    extend "{b}Kosmo the Great{/b}!!!" with vpunch

    $ kosmo_name = "Kosmo"

    you "Who?"

    kosmo "I said {w=1.0}{nw}"

    extend "{b}Kosmo the Great{/b}!!!" with vpunch

    you "Uh? What was that again?"

    kosmo angry "{b}Kosmo the{/b}... Damnit, don't you know who I am?" with vpunch

    kosmo "Haven't you heard of {b}Kosmo the Magnificent{/b}, court entertainer extraordinaire?"

    you "Nope. Not that I'd really care to..."

    kosmo happy "Very well, since you ask, I shall tell you."

    kosmo "I am the world-renowned chairman of 'HʘʘKERS', the largest, fastest-growing, highest-grossing brothel chain in Zan!"

    you "You're gross, all right..."

    kosmo "...and I was knighted by King Pharo the 1st in person! Everyone in Zan knows me, of course, but I shouldn't have expected anything else from a filthy foreigner."

    kosmo "Anyway, I make it my duty to know about every competing business in town... So when I heard Gio's old operation re-opened, I had to see it with my own eyes."

    kosmo laughing "Not that this pig stall is any competition at all for HʘʘKERS! BWAHAHAHA!"

    menu:

        "Piss off":

            $ renpy.block_rollback()

            you "You've had your fun. Now fuck off. And don't come back."

            kosmo angry "Hey! You're addressing a Zan Lord! Don't forget your place, worm..." with vpunch

        "I'll kick your ass":

            $ renpy.block_rollback()

            if MC.playerclass == "Warrior":

                you "Good one. I wonder if you'll laugh as much with five inches of steel in your belly."

            elif MC.playerclass == "Wizard":

                you "Ok, now... Toad, or slug? Which one would you prefer I turn you into?"

            elif MC.playerclass == "Trader":

                you "Sill! Wake Drogon, will you?"

                you "I wonder if you'd make a good treat for my pet..."

                show kosmo angry

        "Yo mamma":

            $ renpy.block_rollback()

            you "Now, if you'll excuse me... Talking about pigs and sows, it's time to feed your mamma."

            kosmo angry "What!!! I'll... You..."

    kosmo angry "Grrr..."

    "The henchmen step forward menacingly. You inch your hand closer to your weapon."

    sill "Master [MC.name]! Are you all right?"

    hide henchman2
    show kosmo angry at left
    show henchman at center
    with move

    show sill sad at right with dissolve


    kosmo "Uh? Who is this?"

    kosmo "Beau...{w=1.0}{nw}"

    show kosmo laughing

    extend "Beautiful!!!" with vpunch

    sill "Uh?"

    you "What?"

    kosmo happy "Who is this gorgeous and delicate flower? Is she one of your girls?"

    you "Hey! She's Sill. Back off."

    sill "Master... I don't like the way he looks at me..."

    kosmo laughing "You! Pig farmer! How much for your sexy slave girl, right now? I'm buying!" with vpunch

    menu:

        "Sill's not for sale":
            $ renpy.block_rollback()
            $ MC.good += 1
            $ NPC_sill.love += 1
            you "Sill is mine, and I'm not ever selling her."
            sill happy "Oh, Master!"
            kosmo angry "Oh, really? We'll see about that."

        "I'm not selling to you":
            $ renpy.block_rollback()
            $ MC.neutral += 1
            you "Whatever, I'm not selling anyone or anything to the likes of you."
            sill "Please, don't sell me!"
            kosmo angry "Such arrogance!!!" with vpunch

        "How about 5000 gold":
            $ renpy.block_rollback()
            $ MC.evil += 1
            $ NPC_sill.love -= 1
            you "5000 gold will do."
            sill "Whaaaat?"
            kosmo angry "5000 gold... Are you crazy??? Even a high-rank girl isn't worth this much!" with vpunch

    kosmo "Trust me, I'm going to get her from you, one way or another..."

    kosmo happy "When your pitiful business dries up, you'll be so broke you'll end up in jail or a slave..."

    kosmo "When that happens, I'll be here. Ready to take her from you!"

    sill sad "No! Master will never leave me with you!"

    kosmo "Oh, really? Don't be so sure... I will break you, baby girl, I have my ways..."

    sill "No! You're disgusting!"

    kosmo angry "...I will make it slow, and agonizingly painful!" with vpunch

    sill "NO!!!"

    "You tighten your grip on your weapon's hilt. The henchmen take another step forward, eyeing their boss, unsure what to do."

    kosmo "..."

    kosmo happy "Humph. Anyway."

    kosmo "Leave this idiot alone, he's not worth the trouble."

    kosmo happy "I'm going now, mister pimp. Not because of your empty threats, mind you... But I find the stench of this place overwhelming!"

    kosmo laughing "Bwahahahaha!" with vpunch

    kosmo "Come on, men, let's head back to the marble palace... I need a clean, relaxing bath..."

    hide kosmo
    hide henchman
    hide henchman2
    with easeoutleft

    show sill sad at center with move

    sill "Oh, I hate this guy..."

    you "Yeah. I'm afraid we haven't seen the last of him..."

    scene black with fade

    $ calendar.set_alarm(calendar.time+7+dice(3), StoryEvent(label = "kosmo_returns", type = "morning"))

    return


label c1_ambush:

    hide screen home
    hide screen tool

    stop music fadeout 3.0

    $ renpy.block_rollback()

    scene black with fade

    "Sill was done with her work, so she decided to accompany you for a morning walk."

    play music m_suspense

    show bg ambush1 at top with dissolve

    "You head out, making your way through the slums and towards the food market."

    "The streets are eerily quiet today. You barely meet a few passersby, all apparently in a hurry to be somewhere else." #

    sill sad "The atmosphere is strange today, Master, don't you think?"

    you "Yes... Why isn't there anyone in the street?"

    "You walk down the deserted streets in oppressive silence."

    play sound s_steps

    "Suddenly, you hear muffled footsteps in all directions. Shadows emerge from nearby streets, blocking your path."

    show masked_thug as mthug1:
        xalign -0.1
        yalign 1.0

    with dissolve

    pause 0.8

    show masked_thug as mthug4:
        xalign 1.1
        yalign 1.0

    with dissolve

    pause 0.4

    show masked_thug as mthug2:
        xalign 0.2
        yalign 1.0

    with dissolve

    show masked_thug as mthug3:
        xalign 0.8
        yalign 1.0

    with dissolve

    pause 1.0

    show sergeant with dissolve

    pause 1.0

    sergeant "Halt!"

    "A stern, tough looking woman is standing in the middle of the street. She stares at you with cold eyes, detailing your features and equipment."

    sergeant "It's him."

    "She turns to the men in the shadows."

    sergeant "Men, this is our mark. Deal with it quickly, and meet me at the rendezvous point."

    sergeant "Oh, and take the girl alive."

    hide sergeant with dissolve

    sill "Take me? What?"

    play music m_danger_loop fadein 1.0

    show masked_thug as mthug1:
        xalign 0.15
        yalign 1.0
    show masked_thug as mthug2:
        xalign 0.3
        yalign 1.0

    show masked_thug as mthug3:
        xalign 0.6
        yalign 1.0
    show masked_thug as mthug4:
        xalign 0.85
        yalign 1.0

    with move

    show masked_thug as mthug5:
        xalign -0.1
        yalign 1.0

    with moveinleft

    show masked_thug as mthug6:
        xalign 1.1
        yalign 1.0

    with moveinright

    play sound s_sword_sheath
    pause 0.3
    play sound2 s_sword_sheath
    pause 0.2
    play sound3 s_sword_sheath

    you "Sill, get behind me! It's an ambush!" with vpunch

    "Half-a-dozen masked men are rushing towards you. Others are coming from the back. They are blocking all escape routes."

    if MC.playerclass == "Warrior":

        play sound s_sword_sheath

        you "En garde!"

        "You meet the first assaulters head on, and parry their attacks in a flurry of blows."

        play sound s_sword_clash

        with vpunch

        you "Let's see how good you are!"

        "You desperately defend yourself against the onslaught, painfully aware that the attackers at your back will reach you any second."

        play sound s_sword_clash
        with vpunch
        pause 0.2
        play sound2 s_sword_clash
        with vpunch

        "Every counter-attack you make is met with a parry, however."

        you "These men are no small-time thugs... They have training... *sweat*"

    elif MC.playerclass == "Wizard":


        play sound s_spell

        you "Barrier of Oznos!!"

        "You keep a protective amulet for emergencies. Clenching it, you cast a magic barrier around you and Sill."

        play sound s_punch
        with vpunch
        pause 0.2
        play sound2 s_punch
        with vpunch

        "All around you, the attackers strike at the barrier repeatedly. It doesn't seem like it can slow them down for very long."

        you "Hnnnn... *sweat*"

        play sound2 s_punch
        with vpunch

        "The amulet glows red hot in your hand as it absorbs more furious blows from your assailants."

        sill "Master! Look out!"

        "On a nearby roof, an attacker is arming a crossbow. Your barrier is starting to yield, and you know it won't be enough to stop bolts from passing through."

    elif MC.playerclass == "Trader":

        you "Sill! Where is Drogon!"

        sill "At... At home, Master!"

        you "Aarh! Follow me!"

        "Spotting a pile of half-rotten crates, you start climbing over them quickly, going for the roof of a nearby house."

        mthug "Quick! He's escaping!"

        "Desperate, you climb from crate to crate, almost reaching the top. Sill is following you the best she can."

        "You pull yourself up to the roof, and turn around to lend her a hand."

        "However, as Sill reaches the last crate, you hear an ill-fated sound."

        play sound s_crash

        "The crates give in, crumbling from under her. Sill falls back down into the street." with vpunch

        play sound s_scream_loud

        sill "Eeek!!!" with vpunch

        you "No!"

        "Sill gets back up, but she has her back to the wall as the attackers close in and surround her. You watch helplessly from your precarious hideout."

    play sound s_scream_loud

    sill "Hiii!!!!"

    you "This is it..."



    stop music fadeout 3.0

    play sound s_surprise

    maya "Hold on!!!" with vpunch

    hide mthug1
    hide mthug2
    hide mthug3
    hide mthug4
    hide mthug5
    hide mthug6
    show bg ambush2
    show maya
    with pushleft

    maya "What do you think you're doing here?"

    mthug "What?"

    maya "I'm talking to you, punk. What do you think you're doing?"

    mthug "What the... Piss off, bitch! Or you'll be in trouble!"

    maya "{b}'I'{/b} will be in trouble? We are the city guard, you moron!"

    mthug "Oh, really? And what are you gonna... Wait, did you say 'we'?"

    maya "Roz!"

    show maya:
        xalign 0.05
        yalign 1.0
    with move

    play sound s_dodge

    show roz at right with easeinright

    with vpunch

    "A huge warrior charges from a side street, coming from behind the girl."

    roz "Maya!"

    $ maya_name = "Maya"

    maya "Right on time. Let's show these brutes who's boss."

    roz "Of course!"

    roz "Hey! Come and face me! I'll gut you, maggots!" with vpunch

    mthug "It's... It's Roz!!! Run for your life!"

    roz "BWAAAAAAAAAAAAAAH!!!!" with vpunch

    "Your attackers break out and run. The giant warrior leaps after them, yelling taunts and insults."

    roz "Turn around and fight! Come on! You guys are no fun..."

    hide roz with dissolve

    play sound s_steps

    maya "Hey! Don't go too far, ok!"

    "She turns towards you."

    maya "You guys all right?"

    show sill at right with dissolve

    sill happy "Oh, thank you, Madam! You've saved us..."

    you "I had it under control... But thanks for showing up."

    maya "Of course, citizen. The city guard is here to help."

    you "Sure..."

    "She frowns."

    maya "Hey! I know that look."

    maya "I hope you will tell your friends that not all guards are a bunch of drunkards and cheats."

    maya "Anyway, do you have any idea what those thugs wanted from you?"

    you "No, they came out from nowhere... They had martial training. Those were not mere thieves..."

    sill "A woman was leading them, but we've never seen her before..."

    maya "Sounds like a contract killing. We have a lot of those, nowadays."

    maya "The streets of Zan are dangerous at the best of times. You should tread softly, and watch your back."

    sill "Yes Madam."

    hide sill with dissolve

    show roz at right with easeinright

    roz "Damn it, they were fast... *pant*"

    roz "I couldn't catch them. They scattered like rats, bwahahahaha!"

    maya "Well, at least we got here in time. Well done."

    roz "But Maya, there's something odd about those guys. One of them recognized me. Do you think..."

    maya "Not here, Roz."

    maya "Let's go."


    hide maya
    with dissolve
    hide roz
    with dissolve

    pause 1.0

    scene black with fade

    "You and Sill make it back safely to the brothel. You give instructions to tighten security."

    return


label c1_reached_goal:

    stop music fadeout 2.0

    $ renpy.block_rollback()

    play music m_gio

    scene black with fade
    show expression bg_bro at top with dissolve

    show sill at right with dissolve

    sill happy "Master! Great news! We now have the necessary gold, and we..."

    gio "Hello, ladies!" with vpunch

    show gio at totheleft behind sill with dissolve

    you "Gio! When did you..."

    gio "No matter, old friend! Hand over that gold, and we'll have us a proper license in no time!"

    sill sad "'We'?"

    you "Look, Gio... I would rather take care of this myself. What did you plan to do with this money?"

    gio "Well, err, I have a contact with the city guard... If we have the right amount,
         she promised to take care of the paperwork, so that we can get a real license and move into the city itself."

    gio "You can see her for yourself, of course... I'll send word. *nervous*"

    you "Yeah. We'll do that."

    scene black with fade

    "Go to the {b}watchtower{/b} and meet with the lieutenant."

    $ game.set_task(__("Bring %s gold to the lieutenant at the {b}watchtower{/b}.") % game.goals[0].value)

    $ story_flags["c1_goal_reached"] = True

    $ story_add_event("c1_visit_watchtower")

    return


label c1_visit_watchtower:

    ## Happens automatically when c1 goal reached and visiting location watchtower with 1000 gold

    $ renpy.block_rollback()

    scene black with fade

    stop music fadeout 3.0

    show bg guard_office at top with dissolve

    show lieutenant:
        xalign 0.5
        yalign 1.2

    with dissolve

    play sound s_knocks

    play music m_knights fadein 3.0

    lieutenant "Yes?"

    guard "Lieutenant, there is a petitioner here to see you, with his slave."

    lieutenant "I'm not having any visitors at the moment. Send them off."

    guard "They say they come on Gio's recommendation."

    lieutenant "That old leech? *sigh* Yes, I suppose I can receive them. Send them in."

    pause 1.0

    show lieutenant:
        xalign -0.2
        ypos 1.2
    with move

    show sill at right with dissolve

    sill happy "Greetings, my lady."

    you "Greetings."

    lieutenant "All right, I ain't got all day, let's get on with this. Gio told me you want to apply for a pimp license?"

    you "Yes."

    lieutenant "And you have the right amount of money?"

    sill "We do."

    lieutenant "All right, I'll send word to the city office. This should take about 3 days to process... You can give me the gold now."

    "You see a glint of greed in her eyes as she extends her hand expectantly."

    you "With all due respect, I would rather wait for the reply from the city office. Then I'll give you the gold."

    "Her lips tighten in frustration, and she withdraws her hand. She hesitates for a second, then sighs."

    lieutenant "As you wish. I will expect payment in full when we get word from the office."

    you "Of course."

    sill "Thank you, my lady."

    lieutenant "Leave me now. I shall send your demand immediately."

    you "Goodbye."

    sill "Farewell, my lady."

    hide sill with dissolve

    pause 1.0

    with fade

    play sound s_knocks

    pause 1.0

    lieutenant "Yes? Come in."

    show sergeant at right:
        zoom 0.9

    with dissolve

    pause 1.0

    play sound s_door

    sergeant "Lieutenant."

    lieutenant "Sergeant."

    $ sergeant_name = "Sergeant"

    sergeant "I saw some civilians leaving the tower, earlier. What was it all about?"

    lieutenant "Oh, nothing that you should concern yourself with. Just a foreigner applying for a business permit."

    sergeant "Nothing unusual about their request, then, I suppose?"

    lieutenant "No... Why do you ask?"

    "She looks at her subordinate suspiciously."

    sergeant "Oh, nothing, I just thought that man looked a bit like trouble."

    lieutenant "Ah, I forgot how much you cared about law and order..."

    lieutenant "Anyway, have a courier deliver this letter to the captain at the city office."

    sergeant "Oh, that won't be necessary. I am headed there this evening, I can take care of it myself."

    "The lieutenant gives her a cautious look."

    lieutenant "Why, that's awfully nice of you, sergeant."

    sergeant "My pleasure. *smirk*"

    "Shrugging, the lieutenant hands her the letter."

    stop music fadeout 3.0

    scene black with fade

    $ calendar.set_alarm(calendar.time+1, Event(label = "c1_guards_visit"))

    $ game.set_task("Wait for your license to be delivered.")

    return


label c1_guards_visit:

    if MC.gold < game.goals[0].value:
        sill happy "Today is the day we get our new license! You've got the gold, right?"

        you "Well, it's embarrassing... I seem to have misplaced it."

        sill sad "What??? We need that [game.goals[0].value] gold, fast!"

        $ calendar.set_alarm(calendar.time+1, Event(label = "c1_guards_visit"))

        return

    ## Happens after visiting watchtower

    $ renpy.block_rollback()

    scene black with fade

    stop music fadeout 3.0

    show expression bg_bro at top with dissolve

    play sound s_knocks

    "The next morning..."

    sill happy "Just a minute."

    show sill at right with dissolve

    sill "Yes?"

    show guard as guard1 at totheleft with dissolve

    guard "This is the city guard! Move aside, slave!"

    play music m_mafia fadein 3.0

    sill sad "Eek!" with hpunch

    hide sill with dissolve

    show guard as guard1 at totheright with move

    show guard as guard2 with easeinleft:
        xalign 0.5
        yanchor 1.0
        ypos 1.05

    show guard as guard3 behind guard2 at totheleft with easeinleft

    guard "Men, search the place."

    you "Hey! What's going on here?"

    guard "Citizen, we have received a report about unlawful and immoral activities being carried out in this place. Are you the owner?"

    you "I am. And I protest. You don't have..."

    guard "We are the law in Zan. We do as we please. Do you want to hang, citizen?"

    you "..."

    hide guard3 with dissolve

    ""

    "Other guard" "Boss, have a look! I found this." with vpunch

    "One of the guards comes back, holding Gio's registry."

    show guard as guard3 behind guard2 at totheleft with dissolve

    guard "Oh, what is that? Let me see..."

    guard "Well well... A registry detailing the unlawful activities going on in this place... Arios, you're quite organized for an upstart pimp!"

    guard "Well, this is all the proof we need. Serious violations of city edicts all over the place."

    if MC.playerclass == "Warrior":
            $ text1 = "illegal weapon possession"

    elif MC.playerclass == "Wizard":
            $ text1 = "possession of hazardous magical drugs"

    elif MC.playerclass == "Trader":
            $ text1 = "illegally importing an exotic pet"

    show black as black2 with fade

    pause 1.0

    hide black2 with fade

    guard "So, this is the final indictment: 5 counts of immorality, 3 counts of tax-dodging, 6 counts of hygiene violations, one count of [text1]. Oh, and your left window is broken."

    play sound s_punch
    pause 0.5
    play sound s_shatter

    "One of the guards rams the back of his lance through the window." with vpunch

    guard "This is gonna cost you..."

    you "Wait! We have a pending registration at the city office... The lieutenant said..."

    guard "Yeah, sure! They all say that... All right, time to pay for your crimes. It will be [game.goals[0].value] gold."

    sill "[game.goals[0].value] gold! But we need that money..." with vpunch

    guard "Shut up, slave! Pay now, or come with us to the dungeon. You choose."

    you "..."

    scene black with fade

    stop music fadeout 3.0

    "You end up paying the guards. They leave eventually, after turning [brothel.name] upside down, and roughing up some of your girls."

    $ MC.gold -= blist[2].cost
    "You have lost [game.goals[0].value] gold."

    with fade

    if brothel.get_common_rooms():
        $ room = brothel.get_random_room_pic_path()
    else:
        $ room = "black"

    show expression room at top
    with dissolve

    show sill sad at left with dissolve

    sill "This is a disaster..."

    you "..."

    play sound s_knocks

    you "What is it, this time?"

    sill "No, Master, don't open! What if it's the guards again!"

    "You sigh, and open the door. Gio barges into the room."

    play music m_gio fadein 3.0

    show gio at totheright with dissolve

    sill "Oh... It's even worse."

    gio "Hello friends!"

    gio "Phew, what a mess it is in here! Did you guys have fun last night?"

    you "Not now, Gio. We're in trouble. The Guard robbed us, and now we are broke again."

    gio "What? How did that happen? Did you go see the lieutenant as I had advised?"

    you "Yeah, a lot of good that did us. For all we know, she sent the Guard after us."

    gio "That's awful... Hot babes will be the end of old Gio, I swear..."

    gio "Anyway. Whether she betrayed us or not, I wouldn't recommend going back to the Guard outpost empty-handed.
         They'll just lock you up for wasting their time."

    you "Oh, that's just great."

    gio "I have an idea, but it's a little risky..."

    sill "An idea? Your ideas always land us in trouble!"

    you "*sigh* What is it?"

    gio "Well, I know for a fact that the good lieutenant has some dealings with the thieves guild... If you can find out more,
         it could give you some leverage in the upcoming negotiation."

    you "The thieves guild?"

    stop music fadeout 3.0

    gio "Yes. They..."

    man "Hey! Pimp guy! Where are you hiding!" with vpunch


    scene black
    show expression bg_bro at top
    with pushleft

    show kosmo with dissolve

    show henchman at right with dissolve

    you "Kosmo? What the hell do you want?"

    play music m_kosmo fadein 3.0

#    show gio at left with dissolve

    gio "What does he want, that conceited fuck..."

    kosmo laughing "Oh, what a gathering. Even old Gio is here... Is this a loser fest?"

    you "If it was, you'd be invited."

    kosmo angry "..." with vpunch

    kosmo happy "Pff, you're joking, but you should see that look on your face... You're in trouble, aren't you?"

    gio "That's none of your business."

    you "Yeah. We're doing fine. Now piss off."

    kosmo laughing "Fine? Well, that's an interesting way to describe it! The guards just took all of your money, didn't they?"

    "Your eyes narrow. You give Kosmo a murderous look."

    you "You... What do you know about it?"

    kosmo happy "Oh, nothing, nothing... I can only empathize with the 'concerned citizen' who reported this place, of course.
                 No one should have to come to this dump, when fantastic brothels from the HʘʘKERS chain are just a block away!"

    kosmo laughing "Bwahahahaha!!!" with vpunch

    you "Why you..."

    kosmo happy "Oh, you look angry... *grin*"

    kosmo "I guess I'll go now, it's been a pleasure watching you lose face, but I'm expected elsewhere."

    you "Grrr..."

    kosmo "And send my regards to your cute pink-haired slave... I'll be here soon to collect her!"

    "You reach for your weapon."

    you "Fuck you, you arrogant fuck! I'll gut you..." with vpunch

    show kosmo angry

    gio "Stop!" with vpunch

    gio "Don't, [MC.name]. We have other things to worry about than quarrelling with this dipshit."

    kosmo happy "Oh, yes, you do have a lot to worry about, friends... I'll be laughing all the way to the banking guild thinking about your demise!"

    hide kosmo
    hide henchman
    with dissolve

    pause 1.0

    show gio at center with dissolve

    gio "[MC.name]. We have to turn things around. Do you know the location of the thieves guild?"

    if thieves_guild.secret:
            you "No. Where is it?"

            gio "Well, I'm not privy to that secret. But it is somewhere in the Slums, for sure."

            gio "You might wanna ask around town. Eventually, you'll find it."

    else:
            you "As a matter of fact, I do."

            gio "Very well. You should pay them a visit."

    you "..."

    you "All right. It seems I have no other choice."

    scene black with fade

    "Go to the city to find the {b}thieves guild{/b}."

    $ game.set_task("Go to the city to find the {b}thieves guild{/b}.")
    $ story_flags["c1_robbed"] = True

    return


label c1_thieves_guild_tip:

    # 25% chance of happening any location any time during chapter1, disappears after spice market

    $ renpy.block_rollback()

    $ loc = selected_location.name.lower()

    "After exploring the [loc] area for a couple of hours, you stop in a nearby tavern to slake your thirst."

    play music m_tavern fadein 3.0

    scene black with fade

    play sound s_crowd_laugh

    man "Psst, [MC.name]. Why don't you join me for a beer and a chat?"

    show bg tavern_man at truecenter with dissolve

    "A shadowy man is standing in the corner of the tavern, gesturing to an empty seat in front of him."

    you "You... You know me?"

    man "Hehe... I know my way around every disreputable establishment in the city. So of course, I know [brothel.name], which means I know you."

    you "What do you want from me?"

    man "Oh, nothing, friend, just a little chat over a drink. But I might have something {i}you{/i} want."

    you "Is that so?"

    man "Yes. Information."

    man "For instance, I can set you on the right track to meet the thieves guild, if you're interested..."

    you "The thieves guild? What makes you think I'd be interested in that?"

    man "Well, it's always good for a businessman like yourself to stay on the guild's good side... And who knows, you might
         be able to arrange a little deal with them, you know... Grease some hands, smoke a few undesirables for you, supply you with
         some quality spices..."

    you "Mmh."

    man "50 denars for a little tip. What do you say?"

    menu:
        extend ""
        "Sure":
            $ renpy.block_rollback()
            you "Sure, I want that information."

            if MC.gold < 50:
                    you "But there is a little problem. I don't have the gold right now."

                    man "Really? Man, you're really broke. Whoremongering isn't what it used to be."

                    man "Say, I'll give you this one for free. Think of it as a goodwill gesture, 'til you get back on your feet."

                    you "Thanks."

            else:
                    $ MC.gold -= 50
                    you "Here's your gold."

            man "All right. Now listen up. There's this courier who acts as a proxy for the guild... Can be found at the spice market most days,
                       shaking down spice dealers for protection money."

            $ story_add_event("c1_spice_market")

            stop music fadeout 3.0

            scene black with fade

            "Go to the {b}spice market{/b} to find the thieves guild courier."

        "Not interested":
            $ renpy.block_rollback()

            you "50 gold is a bit steep for a piece of gossip. And I don't care about that guild, anyway."

            man "Whatever, man. Your loss."

            $ story_add_event("c1_spice_market_25")

            stop music fadeout 3.0

            scene black with fade


    return


label c1_spice_market:

    $ story_remove_event("c1_spice_market_25")
    $ story_remove_event("c1_spice_market")

    ## 25% chance of happening at location spice market (100% if tipped)

    $ renpy.block_rollback()

    scene black with fade

    play music m_oriental fadein 3.0

    show bg spice_market at top with dissolve

    "The Spice Market is the place where the more or less respectable citizens of Zan come to get their fix."

    "Here, all kinds of spices are exchanged, some coming from exotic lands as far as Hokoma, others cooked right here in the slums
     - in less than hygienic conditions."

    "Of course, a lot of the spices one can find at the market are highly illegal in Zan. But here, far from the policed streets of
     the city inner districts, very few rules are actively enforced."

    "Conveniently, the city guard turns a blind eye to most of the traffic going on at the spice market, provided they get their cut."

    "Wandering the busy alleys of the Spice Market, where the rebellious spawns of noble families rub elbows with street-dwelling junkies,
     you once again wonder about the corruption of the big city."

    if MC.get_alignment() == "good":

        you "This city is run entirely by vice and greed... I feel dirty just being here. Living in the wilderness had its advantages..."

    elif MC.get_alignment() == "neutral":

        you "A land of opportunity, indeed... With so much vice around, I should be able to turn a profit pretty quickly."

    elif MC.get_alignment() == "evil":

        you "Bah, this is nothing! I will show those jokers what real depravity looks like."

    "Standing around the central artery of the market for a little while, you start noticing a shady character acting strangely.
     Dressed in a bulky, dark burnous, his face is invisible under the hood."

    show stranger with dissolve

    "The stranger stops at each stall, and whispers something in the ear of the vendor. The vendor then discreetly hands over a purse,
     which appears to be full of gold."

    "The stranger slowly makes his way down the alley, repeating his little ploy with every stall owner."

    "Unbeknowst to him, however, you are watching him closely. It turns out you are not the only one."

    show stranger at right with move

    show guard as guard1 at left with dissolve:
        zoom 0.8

    show guard as guard2 behind guard1 at totheleft with dissolve:
        zoom 0.8

    stop music fadeout 2.0

    "A couple of guards show up at each end of the alley. You sense trouble."

    guard "You! Stay right where you are!" with vpunch

    play music m_danger_loop

    "The lively buzz of the market stops abruptly. Everyone gets their head down, and sellers rush to hide their goods under the stall tables."

    "Every pair of eyes turns to the mysterious stranger, as the guards advance cautiously towards him, spears in hand."

    show guard as guard1 at totheleft:
        zoom 0.8

    show guard as guard2 behind guard1 at center:
        zoom 0.8

    with move

    "The stranger hasn't moved an inch since the guards called him out."

    guard "You, yes, you, take down your hood! Show us your ugly thief mug."

    "The stranger tilts his head slightly, as if acknowledging the guards for the first time.
     Suddenly, without so much as a warning sign, he starts moving with blinding speed."

    with hpunch
    hide stranger with blinds


    guard "Hey! What the hell do you think you're doing!"

    show guard as guard1 at center

    show guard as guard2 at right

    with move

    show stranger at left with blinds

    "The stranger swiftly leaps over several stalls, spilling spices and weights over the indignant cries of the shop owners.
     The guards curse and start running after him."

    "You notice that the fugitive is running towards you."

    menu:

        "What do you do?"

        "Let him pass":
            $ renpy.block_rollback()
            $ MC.neutral += 1
            "Crossing your arms, you let the mysterious stranger run past you in a gust of dust and spice."

        "Bar his way":
            $ renpy.block_rollback()

            you "Wait a minute!"

            "Spreading your arms, you step in the middle of the stranger's way, barring access to his chosen escape route."

            hide stranger with blinds

            "Without so much as slowing down, the thief jumps up high into the air, completing a flip right over your head, and
             landing on his feet a couple of yards behind you." with vpunch

            show stranger at left with blinds

            $ story_flags["blocked thief path"] = True

    "As the thief passes next to you, you catch a whiff of sweet jasmin. A woman's perfume..."

    "Turning around, you see the thief jumping over a water fountain and crouching behind it."

    hide stranger with dissolve

    "The cloaked stranger doesn't reappear."

    stop music fadeout 3.0

    with fade

    show guard as guard1 at totheleft

    show guard as guard2 at center

    with move

    "Moments later, the guards reach you, cursing and sweating as they struggle to run in their armor."

    guard "Damn, where did that wretched thief guilder go?"

    if story_flags["blocked thief path"]:

        guard "Thank you for trying to stop that criminal, citizen. A good deed is rare in these parts. Why did you do it?"

        menu:
            guard "Thank you for trying to stop that criminal, citizen. A good deed is rare in these parts. Why did you do it?"

            "I wanted to do the right thing (Truth)":
                $ renpy.block_rollback()
                $ MC.good += 1

                you "I wanted to do the right thing. I don't like criminals any more than you do."

                "The guard looks at you suspiciously."

                guard "Well, that's good to hear. Stay on the right side of the law, citizen."

            "I wanted to do the right thing (Lie)":
                $ renpy.block_rollback()
                $ MC.evil += 1

                you "Oh, I'm an upstanding citizen of Zan, I was only doing my duty... You know. *grin*"

                "The guard looks at you suspiciously."

                guard "Sure... Anyway, where did that thief go? Anyone seen anything?"

                "You keep silent about what you know. You intend to use this information for your own benefit."

    hide guard2 with dissolve
    hide guard1 with dissolve

    you "Thief guilder, uh..."

    if story_flags["got_tip thieves guild"]:
        extend " This must be what the dodgy guy in the tavern was talking about."

    "Walking past the fountain where the thief disappeared, you spot a sewer grate. On it you can see a carved symbol."

    show symbol at truecenter with dissolve

    you "Uhm, interesting..."

    scene black with fade

    "Explore {b}the Sewers{/b} to learn more about the thieves guild."

    $ story_add_event("c1_sewers")

    return


label c1_sewers:

    ## 100% chance of happening at location Sewers after spice market

    stop music fadeout 3.0

    $ renpy.block_rollback()

    scene black with fade

    show bg sewers at top with dissolve

    you "Ew, that smell... I must be getting close."

    "Zan is renowned for its extensive sewer system, introduced nineteen centuries ago by the first non-human dwellers of the city."

    "The non-human empire used magic to carve a complex maze of galleries deep under the current city level. Since then, the
     successive rulers of Zan have made random additions to the system while abandoning or condemning older galleries."

    "Nowadays, no one knows exactly how expansive the sewers are and what kind of secrets and horrors lurk down there. One thing's
     for sure, however: the constant streams of waste and refuse all end up in one place. The Slums."

    you "This grate doesn't have the symbol... How about this one..."

    show symbol at truecenter with dissolve

    you "This! I know this marking."

    "You look around you, and you see no one. Cautiously lifting the grate, you notice that it is surprisingly easy to open."

    play sound s_creak

    you "Someone greased the joints recently. No traces of rust. I must be on the right track."

    "You crouch to enter the sewers, disappearing into darkness."

    play sound s_creak

    scene black with fade

    play music m_suspense

    you "Oh, that stink..."

    show bg inner_sewers at top with dissolve

    "It takes you a while to get over the smell. Burying your face in your scarf, you start moving."

    you "I'm looking for those guild symbols... Ah, here's one."

    "The sewers are a real maze of filthy streams and side galleries. Giant rats, cockroaches, and worse creep out of the light as you advance."

    "At every crossroad, you pause and look for the guild sign. Fortunately, you always manage to find it, even if it is sometimes hidden
     in the unlikeliest places."

    you "This is the worst treasure hunt I've ever been on."

    with fade

    play sound s_scream_loud

    "As you move your way through the dimly lit sewers, you suddenly hear a scream."

    play sound s_screams

    "It comes from a side gallery, a different direction from where you were heading."

    menu:
        "What do you do?"

        "Follow the screams":
            $ renpy.block_rollback()
            "Hastening pace, you step into the tunnel from which the screams came. You have to bend your back to avoid scraping your head on the ceiling."

            play sound s_scream_loud

            "The screams sound closer now, and you can also hear male voices."

            show bg cell at top with dissolve

            "You emerge in a storage room and see a group of men surrounding a naked girl."

            show sewer_woman naked at right with dissolve

            sewer_woman "Ngggh!"

            show sewer_rapist at left with dissolve

            man "Bwahahahaha! What are you trying to say, you stupid bitch? I thought we told you to be quiet!"

            "The girl is bound and gagged, her body covered in grime and semen. She is surrounded by a gang of half-naked men, thugs by the look of them."

            sewer_woman "Mmmmmngh!"

            man "What's that you were saying? That you love cock?"

            man "Oh, don't worry, there'll be plenty more cocks for you before we sell you to the fleet!"

            "Her eyes widen with fear."

            play sound s_scream_loud

            sewer_woman "Nnnnnghhh!"

            "You emerge from the tunnel and straighten up. The woman notices you as you step in the room."

            play sound s_scream

            sewer_woman "Hhhhpp mmmh!!!"

            "Following her gaze, the men turn around and notice you. Their leader gives you a furious look."

            man "Hey! Who the fuck are you? Can't you see we're busy!"

            you "..."

            # Pick challenge
            $ tt = show_tt("top_right")
            $ chal = renpy.call_screen("challenge_menu", challenges=[("Fight them", "fight", 4), ("Cast sleeping spell", "control", 4)], cancel=("Leave", False))
            hide screen tool

            if chal:
                $ renpy.block_rollback()
                $ MC.good +=3

                you "I'm the good guy coming to the rescue, that's who. I can't let you hurt this poor girl."

                man "Uh? What have we here? Some kind of sewer-dwelling errant knight? Boys, let's kick this wimp's ass!"

                "Hastily buttoning up their pants, the men grab a bunch of clubs and sticks, and advance threateningly towards you."

                if chal == "fight":

                    # Run challenge
                    call challenge(chal, 4) from _call_challenge_3 # result is stored in the _return variable
                    $ r = _return

                    if r:

                        you "Ha! Bring it on."

                        play sound s_punch

                        with vpunch

                        pause 0.5

                        play sound2 s_punch

                        with vpunch

                        "You kick the first attacker in the stomach, and punch the second one square in the face."

                        man "You bastard!!!"

                        play sound s_dodge

                        pause 0.5

                        play sound2 s_dodge

                        pause 0.5

                        play sound s_punch

                        "Easily dodging the next attacks, you knock out another of your opponents with a vicious elbow blow to the nose." with vpunch

                        "There are only a couple of opponents left now, and they quickly lose heart seeing the damage you've already done."

                        with vpunch

                        play sound s_punch

                        man "R... Run!!!"

                        hide sewer_rapist with dissolve

                        play sound s_steps

                        "The men that are still capable of standing quickly skedaddle through the various tunnels."

                        call c1_sewers_girl_protected() from _call_c1_sewers_girl_protected

                    else:

                        you "Bring it on!"

                        play sound s_punch

                        "You rush to meet your opponents, managing to knock the first one down." with vpunch

                        "The others are immediately behind him, however, and soon you find yourself sparring with a trio of thugs."

                        play sound s_sword_clash

                        pause 0.5

                        play sound2 s_sword_clash

                        "Your armor protects you from some of the blows, but one of the attackers sneaks from behind you and give you a hard whack on the helmet." with vpunch

                        play sound s_punch

                        "You crumble into the dirt, the remaining thugs ganging up on you. Soon, they kick you into unconsciousness."

                        man "What a dumb motherfucker! Bwhahahaha!!!"

                        man "Now, where were we?"

                        play sound s_scream_loud

                        sewer_woman "Nhhh!"

                        call c1_sewers_rape(with_MC = False) from _call_c1_sewers_rape

                        $ story_flags["c1_lost_in_sewers"] = True
                        $ story_add_event("c1_sewers_return")

                        return

                elif chal == "control":

                    # Run challenge
                    call challenge(chal, 4) from _call_challenge_4 # result is stored in the _return variable
                    $ r = _return

                    if r:

                        "Grabbing a handful of sand from your spellbag, you throw it right into the first attacker's face."

                        man "Raaah!!!"

                        "Reaching for more into your bag, you throw sand in the air as you cast a sleeping spell."

                        play sound s_spell

                        you "Enter sandman!"

                        with vpunch

                        "The next attackers stumble as they reach you, unable to keep their grip on their weapons."

                        "One by one, the thugs fall down to their knees, struggling to keep their eyes open."

                        "Soon, they all fall face flat in the dirt."

                        play sound s_crash

                        hide sewer_rapist with dissolve

                        "Heavy snoring echoes through the tunnels as you casually step over the sleeping thugs."

                        call c1_sewers_girl_protected() from _call_c1_sewers_girl_protected_1

                    else:

                        you "How dare you attack me! Prepare to feel the heat of my magic!"

                        "The bandits hesitate as you reach for your spell bag. Throwing sand into the air with an impressive arm gesture,
                         you yell an incantation with a booming voice."

                        you "ABRA..."

                        play sound s_fizzle

                        you "..."

                        you "Damn, what was it again?"

                        "Before you can remember the actual words of the spell, the thugs are upon you."

                        play sound s_punch

                        man "Take that!" with vpunch

                        play sound s_punch

                        pause 0.3

                        play sound2 s_punch

                        man "And that, and that!" with vpunch

                        "You fall down under the blows of half-a-dozen angry goons."

                        you "Aaaah! Not the face!!!"

                        play sound s_punch

                        man "That will teach you, you dumb fuck!" with vpunch

                        play sound s_crowd_laugh

                        "Leaving you passed out in the dirt, the men turn back to their initial target."

                        man "Forgive this interruption, me lady... We's gonna take good care of you now... Bwahahahah!!!"

                        play sound s_scream_loud

                        woman "Nhhhh!!!"

                        call c1_sewers_rape(with_MC = False) from _call_c1_sewers_rape_1

                        $ story_flags["c1_lost_in_sewers"] = True
                        $ story_add_event("c1_sewers_return")

                        return

            else:
                $ renpy.block_rollback()
                $ MC.evil += 1

                you "Oh, don't mind me. I was actually just passing by... I'll show myself out."

                man "Wait a minute!" with vpunch

                you "Err... What?"

                if MC.get_charisma() >= 4:

                    man "Don't you wanna join in? That slut could use an extra cock in the face."

                    play sound s_scream

                    sewer_woman "NGHH!!!"

                    you "Join you?"

                    menu:
                        you "Well..."

                        "No thanks":

                            $ renpy.block_rollback()

                            you "That's very generous of you, but I have other business to attend to... I don't even know why I came here, hahahaha..."

                            man "..."

                            man "All right, piss off then. You already wasted enough of our time."

                            you "S... Sure."

                            "You make yourself scarce, haunted by the helpless cries of the raped woman as you flee."

                            play sound s_screams

                        "Hell yeah":
                            $ MC.evil += 5
                            $ renpy.block_rollback()

                            you "I was hoping you'd say that."

                            man "Come on, then! The more the merrier!"

                            play sound s_scream_loud

                            sewer_woman "NGHHH! NGGGGGHHH!!!"

                            call c1_sewers_rape(with_MC = True) from _call_c1_sewers_rape_2
                            $ story_flags["c1_lost_in_sewers"] = True
                            $ story_add_event("c1_sewers_return")

                            return

                else:
                    man "How do we know you won't report us to the Guard?"

                    you "I just won't. This is none of my business."

                    "His pig-like eyes narrow as he frowns."

                    man "Really... Why don't I believe you?"

                    man "Get him!" with vpunch

                    you "Wait!"

                    "Three goons hastily buckle up their pants and start limping towards you. You turn around and run."

                    you "Dammit!"

                    scene black with fade

                    show bg inner_sewers at top with dissolve

                    "You run through the sewers, followed by the imprecations of your pursuers. After a long chase, you finally throw them off your track."

                    "By the time you lost them, however, you are well and completely lost."

                    you "Curse those gutter rats!"

                    "After hours wandering, you eventually find an exit. You have lost a lot of precious time."

                    scene black with fade

                    $ MC.interactions = 0
                    $ story_flags["c1_lost_in_sewers"] = True
                    $ story_add_event("c1_sewers_return")

                    "You have lost your remaining actions for the day."

                    return


        "Ignore them":
            $ renpy.block_rollback()
            $ MC.neutral += 1
            you "Whatever it is, this isn't in the right direction. I must stay focused."


label c1_sewers_return:
    $ story_flags["c1_lost_in_sewers"] = False

    # 100% chance of happenning if returning to sewers after c1_sewers

    stop music fadeout 3.0

    $ renpy.block_rollback()

    scene black
    show bg inner_sewers at top
    with fade

    "You head back to the path that you were following, going deeper into the sewers."

    "You look around for the secret guild sign every time you start getting lost. From here on, the trail is actually
     easy to follow, once you know where to look."

    with fade

    "Eventually, you reach a ladder leading up to the street. You have walked several miles from your starting point in order to get there."

    you "Let's see where this leads."

    show bg thieves_guild at top with fade

    you "Just an empty street..."

    "Disappointed, you look around you. Most of the houses are crumbling, with obstructed doors and broken windows."

    "However, you can see some smoke coming out of the chimney from one of the seemingly abandoned houses."

    show symbol at truecenter with dissolve

    "Moving closer to the house, you can see the thieves guild sign, carved onto an old, yet strong-looking oak door."

    $ thieves_guild.secret = False

    $ story_add_event("c1_thieves_guild_found")

    $ story_add_event("c1_ask_guild_for_help")

    scene black with fade

    "You have discovered the {b}thieves guild{/b}."

    return


label c1_sewers_girl_protected():

    play sound s_scream

    sewer_woman "Mmmmh!"

    "You turn to the girl, who lies naked and shaking in the middle of the room."

    "You lift her to her feet and free her of her bounds."

    you "Are you all right?"

    show sewer_woman naked at center with move

    sewer_woman "I.. I guess I am. Thanks to you."

    you "What happened to you?"

    sewer_woman "I was kidnapped..."

    sewer_woman "I work at the shipyard. As I was going home last night, those bastards ambushed me and
                 brought me here. They are part of some kind of slave smuggling operation."

    sewer_woman "They had me here all night..."

    "For a second she looks shaken up in recollection of the night's events, but she soon recovers her countenance."

    "She thanks you with a trembling voice."

    sewer_woman "I shudder to think what would have happened if you didn't show up... They wanted to brand me as a slave
                 and send me on the first ship to the Blood Islands."

    you "You have to leave this place... It's too dangerous to stay here."

    sewer_woman "I want nothing more... But I don't know my way around, and I have lost my clothes..."

    you "Well, it's not great, but you can wrap yourself in the shirt of one of those assholes. As for the exit, you can
         follow these symbols back from where I came. They will lead you to a safe exit."

    "You draw the guild symbol in the dust with a stick."

    sewer_woman "Thank you... I will never forget what you did for me. I shall repay you one day."
    $ unlock_achievement("sewer defender")

    hide sewer_woman with dissolve

    you "Now, let's go back on track."

    $ story_add_event("c2_sewer_girl_returns", type="day")

    return


label c1_sewers_rape(with_MC = False):

    scene black with fade

    "The men form a circle around the naked girl, stroking their dicks in anticipation."

    if with_MC:
        "Taking off your pants, you eagerly join them."
        $ MC.change_prestige(1)

    show bg sewers_rape1 at top with fade

    play sound s_scream

    sewer_woman naked "Nggh... *sob*"

    man "Let me remove this gag for you... We're going to use your mouth, after all..."

    "He unstraps the gag from her face. She drools and coughs, but before she can fully recover, the man slaps his hard dick across her face."

    play sound s_scream_loud

    sewer_woman "Aaaah!!! Dis... Disgusting!"

    man "C'm'on, bitch. Be nice. You don't want to make us angry!"

    "The fat gangster is half-mad and high on spice. Understanding the threat, the girl seems to resign to her fate."

    sewer_woman "Don't... Don't hurt me. I'll do what you ask."

    man "That's more like it. You can start by sucking on a fat dick."

    if with_MC:
        man "Why don't you give our guest a good blowjob, uh? He came all the way down here to see you, don't disappoint him."

        you "That's right. I want you to use that slutty mouth of yours to wipe my dick clean."

        "Not waiting for an answer, you push your dick into her face."

        "At first, she tries to keep her lips shut, but the brutish man gives her a warning look."

        "After a moment of hesitation, she seems to make up her mind, opening her mouth as you force your dick in."

    else:
        "The man forces his large, sweaty dick into the girl's mouth."

        "She makes a visible effort not to retch. After a few moments of hesitation, she starts moving up and down his cock, making dirty slurping noises."

    play sound2 s_sucking

    man "Wow, look at this bitch! She's a natural."

    "The men free her hands too so that she can jerk them off as she continues {nw}"

    if with_MC:
        extend "sucking your dick."

    else:
        extend "sucking the man's dick."

    play sound s_aaha

    sewer_woman "Mhhh... Ngggh..."

    "The woman blushes. She tries to remains passive as her throat is getting raped."

    man "Use your tongue, you lazy bitch!"

    if with_MC:
        man "You have to make him come fast, because you will be taking care of us next."

    else:
        man "I wanna shoot a big, fat load all over your slutty face..."

    play sound s_scream

    sewer_woman "Nnnnh!"

    "Surrounded, the girl can't see anything but stiff dicks. The men are rubbing their cocks on her body, pulling her hair and yanking at her
     tit rings, making her moan."

    play sound s_aah

    "She seems confused and dazed by her predicament. Her face is red with shame and anger, with a hint of arousal."

    man "I said 'use your fucking tongue', bitch!"

    if with_MC:
        "He pushes the back of her head towards your groin, until she's choking on your dick."

        play sound s_surprise

        "She gasps as you pull it out."

    else:
        "He forces his cock deep down her throat, leaving it deep inside for several seconds until she's gasping for air."

    play sound s_scream_loud

    sewer_woman "Gaaah!!!"

    man "Now suck it properly."

    "She starts using her tongue more, making the dick slide in and out of her throat
     with ease with her saliva."

    play sound s_aah

    sewer_woman "Aaaah!!"

    "Her face is bright red now, as she takes the ravaging of the fat dick in her mouth in stride."

    "She's just going along with it now, as if no longer aware of her situation."

    if with_MC:
        you "Mmmh... I can't hold it much longer..."

        man "You heard the man! Get ready to take a big, fat load of cum, bitch!"

        with flash

        you "AAAAH!"

    else:
        man "Well done, bitch... I'm going to give you... A present..."

        with flash

        man "RAAAAH!"

    show bg sewers_rape2 with doubleflash

    play sound s_scream_loud

    sewer_woman "Hiiiii!"

    if with_MC:
        "Taking your dick out of her wet mouth, you shoot your load all over her pretty face, covering her glasses with thick cum."
    else:
        "Ripping his dick out of her mouth, the man moans as he shoots a load of thick cum all over her pretty face."

    "Seeing this naughty scene, the other men quickly reach the tipping point."

    play sound s_scream

    with doubleflash

    sewer_woman "Haaa!"

    show bg sewers_rape3 with dissolve

    "Now covered in semen, the girl looks broken and absent-minded, as the men wipe their dirty dicks all over her body, face and hair."

    man "That-a-girl!"

    if with_MC:
        man "And don't forget to wipe him clean."

        "The girl reluctantly licks the cum from your still-erect shaft, coughing as you make her swallow some in the process."

    else:
        man "And don't forget to wipe me clean."

        "She doesn't even resist him as he forces his cock back into her mouth, making her squeeze it for every last drop of cum."

    man "That was fun... Now get ready, bitch, we're going to train your pussy and ass until you can't stand up anymore."

    play sound s_scream

    sewer_woman "Wait! No!"

    man "The night is young, and tomorrow you'll sail for the slave pens of the Blood Islands. So relax honey, and enjoy your last stay in Zan..."

    play sound s_screams

    sewer_woman "Noooooooooooo..."

    "Her screams echo through the sewers as the men push her to the floor and spread her legs wide open."

    if with_MC:

        scene black with fade

        "You spend hours raping the girl with your new pals. By the time you are finished, her mind and body are completely
         bent to your wishes."

        "You return to the brothel late, having spent all your energy, and no closer to finding the thieves guild."

        $ MC.interactions = 0
        $ unlock_achievement("c1 gang")

        "You have lost all remaining actions for the day."

    else:

        scene black with fade

        "While the brutes are busy raping the poor girl, you sneak your way out of the room and drag yourself to the exit."

        "You head back to the brothel to nurse your wounds, no closer to finding the elusive thieves guild."

        $ MC.interactions = 0

        "You have lost all remaining actions for the day."

    return


label c1_thieves_guild_found:

    # 100% chance of happening at location after sewer_return and not goal reached

    play music m_suspense fadein 3.0

    $ renpy.block_rollback()

    scene black with fade

    "You return to the crumbling house where the thieves guild is supposedly in hiding."

    show bg thieves_guild at top with fade

    "Upon reaching the house, you see no signs of activity."

    you "It's getting dark soon... I should wait a little."

    with fade

    "After waiting for about an hour, you start to think that you are wasting your time."

    you "Damn it, there's no one in this old ruin... I'll just go."

    "Dejected, you prepare to turn back and head for the brothel, when suddenly you see some lights flaring up inside the house."

    you "Wait, I didn't see anyone enter... Let's take a closer look."

    "As you move cautiously towards the house, you notice it isn't as deserted as you first thought."

    "A masked man is standing in the shadows near the entrance porch, leaning against the wall with his arms folded."

    "He manages to stay nearly invisible in spite of his heavy frame."

    "You can tell that he is ready to deal with trouble. You don't see a weapon at his side,
     but you're sure he has one or several at hand."

    "As you stand across the street, hesitating, you see a cloaked figure walking up to the man, muttering words you can't hear."

    "Without a word, the big man gives a quick nod to the door, and lets the stranger in."

    you "I suppose there's no harm in asking for directions..."

    "A little unnerved by the cloak and dagger atmosphere, you nonetheless decide to approach the masked man in the shadows."

    you "Hello there..."

    mthug "..."

    you "I... I own a house in town, [brothel.name]. I was told I could meet with the thieves guild, maybe start a good business relationship?"

    "The man doesn't acknowledge you or move an inch."

    you "Well, uh, I suppose you don't mind if I have a little look inside... It was nice meeting you..."

    "You take a step towards the entrance."

    play sound s_crash
    with vpunch

    "The man slams his beefy arm across the door, blocking your path."

    mthug "Get lost."

    you "Seems like small talk doesn't work with this guy..."

    menu:
        "What do you do?"

        "Kick his ass":
            $ renpy.block_rollback()
            you "All right, I see you're thicker than this oak door. Maybe after I mop the floor with your sorry ass,
                 you'll be more accommodating?"

            play sound s_sword_sheath

            "The man rises and looms menacingly as you reach for your weapon."

        "Neutralize him with magic":
            $ renpy.block_rollback()
            you "I'll be going, then... I guess I was mistaken, hahahaha..."

            "You walk a few steps down the alley, then swiftly turn around."

            you "I know just the spell to make you dance, you stupid goon..."

            "Your eyes burn bright as you prepare the words."

        "Negotiate":
            $ renpy.block_rollback()
            you "Friend, it seems we got off on the wrong foot here."

            you "Let me explain how we could make this situation work to our mutual advantage."

            you "You see..."

    play sound s_sword_sheath

    with vpunch

    "You are interrupted by the sound of steel coming from behind you. A gloved hand covers your mouth and yanks
     your head back as a sharp blade comes to rest against your throat."

    with vpunch

    "That's it. You're {b}{color=[c_red]}dead{/color}{/b}."

    extend ".. is what you thought, for a second. But the unknown assailant does not immediately slit your throat, to your temporary relief."

    "You raise your hands, away from your weapons."

    renza "Don't even think about moving."

    "A sweet perfume reaches your nostrils. You get a flashback from the spice market: this is the perfume of the stranger
     you ran into that day."

    "As the woman behind you pulls you even closer, you can feel something else. The soft, bouncy feel of a large pair
     of boobs pressing against your back."

    renza "Zak, disarm him."

    "The masked figure grunts and proceeds with taking away all your precious gear, down to the small knife you keep in your boot for emergencies."

    renza "Move inside the house. And don't try anything silly, or I'll bleed you like a goat on Arios day."

    "She pushes you inside the house and enters behind you, closely followed by the masked goon."

    scene black with fade

    show bg thieves_guild inside at top with dissolve

    "You enter a worn-out, empty hall which looks just like what you'd expect to find in an abandoned house."

    "Lit-up torches, however, and a conspicuous lack of dust and cobwebs tell you that this decrepit house is more than it appears."

    "Turning around, you see the face of your assailant for the first time."

    show renza at right with dissolve

    "A beautiful girl stands before you, all dressed in black. Her young, cute face and shapely figure are not what you expected from a master thief."

    "On her hip is a black-ink tattoo, resembling the sign you followed on your way from the sewers to the old house."

    renza "So, you wanted a little chat, I gather?"

    renza "Then talk, until I decide if your dead body is to be found floating in the river tomorrow."

    you "Are... Are you the thieves guild?"

    renza "That's none of your business... But since I might end up killing you anyway, I will indulge your curiosity."

    $ renza_name = "Renza"

    renza "My name is Renza, I am the current leader of the thieves guild. I do not normally deal with the rabble that comes here,
           so consider yourself lucky."

    "Unable to keep from staring at her generous shapes, you find yourself almost in agreement, in spite of your predicament."

    you "Well, my lady, I apologize for barging in like this... I was told about this place and wanted to meet with the guild for a deal."

    you "I swear my intentions were only about spying, stealing and robbing. Nothing dishonourable."

    renza "That's what you say... Who are you?"

    you "My name is [MC.name]. I'm the owner of [brothel.name], which I received from a guy named Gio..."

    renza "Gio? That old fart? I don't like to hear the name of a competitor in my own house... Maybe I should have slit your throat, after all."

    you "...Gio, that disgusting, annoying freeloader, of course. I disliked him at first sight, hahaha!"

    renza "That's more like it."

    renza "..."

    renza "So, you're a brothel owner, uh? This kind of connections can have its uses..."

    "She takes a closer look at you."

    if MC.playerclass == "Warrior":

        renza "A strong build, various scars, a keen eye for weapons..."

        renza "You're a warrior, aren't you?"

    elif MC.playerclass == "Wizard":

        renza "Dandy manners, hands that look like they've never gotten dirty, the smell of sulfur on your clothes..."

        renza "You're a mage, aren't you?"

    else:

        renza "A slick tongue, deft hands, a sneaky look about you..."

        renza "You're a camel dung salesman, aren't you?" with vpunch

        you "What?!?"

        renza "...or a trader of sorts."

    renza "And a somewhat handsome one, at that. *wink*"

    "If your situation wasn't so dire, you would be blushing."

    renza "Maybe we {i}could{/i} do business. But you must understand and accept my rules, first."

    you "Well, I've come this far..."

    renza "If I decide to let you live, you are never to tell anyone about me, or the location of this place. You mustn't brag about your connection to us,
           or otherwise reveal it to anyone."

    renza "The penalty for betrayal is a dagger to the neck. Are we clear?"

    you "... "

    you "Yes."

    renza "As long as we're doing business, you must understand the risks. The Guard is hunting us down, and if they catch you as an accomplice,
           you'll rot in a cell, be sent off to the pit, or worse."

    renza "I'm working to get them off our back, but trust me, it's hard. They don't like us treading on their own turf."

    you "I see."

    renza "In return, I'll give you access to some of our merchandise. It's stuff that, err, fell off the back of a cart, so to speak."

    renza "As long as we're dealing, you'll buy what's here at face value, and there is no refund. I don't wanna hear any complaints, understood?"

    you "Fine."

    "She seems to relax."

    renza "Very well, then. As long as we understand each other and you keep your side of the deal, you can come here once a week. I'll have an item
           for sale, for a bargain price compared to regular item shops."

    you "Sounds good."

    with vpunch

    renza "But don't even think about double-crossing me!"

    "She gives you a killer stare."

    you "No... No Ma'am!"

    renza "Perfect. Looking forward to doing business with you."

    you "Thank you, my lady."

    renza "Call me Renza. Oh, and don't forget... I am doing you a favour. I will expect it repaid some day."

    "You're not sure what she means by that."

    you "S... Sure."

    hide renza with dissolve

    show bg thieves_guild at top with dissolve

    "You leave the guild unharmed. Renza teaches you the password, so you can enter without causing a brawl, next time."

    you "That went well. Throat unslit, and all."

    you "Damn, that Renza is cute... A little scary, and a little bossy, but man, those boobs..."

    scene black with fade

    "You can now visit the {b}thieves guild{/b}."

    $ NPC_renza.met = True
    $ thieves_guild.secret = False
    $ thieves_guild.action = True

    return


label c1_ask_guild_for_help:

    $ story_remove_event("c1_thieves_guild_found")

    # 100% chance of happening at location if goal reached

    $ renpy.block_rollback()

    play music m_suspense fadein 3.0

    scene black with fade
    show bg thieves_guild at top with dissolve

    "Returning to the old house in the slum, you see the now familiar thieves symbol etched on the door."

    "After checking that no guards are lurking about, you cautiously walk up to the entrance."

    "You find the door solidly locked."

    menu:
        you "How should I go on about this?"

        "Force it open":
            $ renpy.block_rollback()
            you "To hell with discretion, I need answers."

            $ sneak = False

            "Grabbing a rusty iron bar from a pile of rubble, you use it as a lever to break the lock."

            you "HUUUMPH!"

            with vpunch

            play sound s_crash

            "Piling all your strength on the lever, you hear a satisfying crack as the lock snaps open."

            play sound s_door

            "The door hinges open, revealing the dark entrance hall of the old house."

            "With all the racket you made, you'd be surprised if no one heard you coming. You step in."

        "Sneak your way in":
            $ renpy.block_rollback()
            you "Running inside weapons blazing seems like a bad idea. Let's look for another entrance."

            $ sneak = True

            "After circling around the house, you finally notice a half-open skylight."

            you "Let's try to climb in through there."

            "Taking care not to make noise, you climb on top of the old house, taking advantage of the numerous cracks in the wall."

            play sound s_creak

            "Opening the skylight completely, you let yourself slide down to the floor of the old house, with as little noise as you can manage."

            scene black with fade

            play sound s_dodge

            with vpunch

            you "Alright, I'm in."

    show bg thieves_guild inside at top with dissolve

    "The house is dark, but as your eyes adjust to the darkness, you can see a ray of light filtering from a piece of flooring in the middle of the room."

    "Upon closer examination, you find a trapdoor, and you can hear the echo of voices coming from underneath."

    you "Let's go in."

    "Lifting the trapdoor, you see a ladder leading down to a torchlit basement."

    "There is no way but down. You sheath your weapon, and step down the ladder."

    show bg thieves_guild corridor at top with fade

    if sneak:

        "Reaching the bottom of the ladder without raising alarms, you hone in on the source of the voices."

        "At the end of the corridor is a door. Female voices can be heard on the other side."

        show bg thieves_guild room at top with pushleft

        show lieutenant:
            xalign -0.2
            ypos 0.2
        with dissolve

        lieutenant "Do you realize the risks I had to take to go this far? We must take action {b}now{/b}!"

        show renza at right:
            zoom 0.9
        with dissolve


        renza "I appreciate it, acolyte, I really do."

        you "(Acolyte???)"

        renza "But surely, you can't suggest we take over the Guard headquarters by storm... It will be a bloodbath, and I'm not sure we'd end up on the surviving side."

        lieutenant "I know! But we have the prisoners, surely we can use them to get some leverage. Captain Farah must have a weakness..."

        scene black
        show bg thieves_guild corridor at top
        with pushright

        you "(Are they plotting to take on the Guard captain? I can't hear well...)"

        "You move closer to the door, pressing your ear against it in an effort to hear better."

        play sound s_creak

        lieutenant "What was that?" with vpunch

        you "Shit!"

        "Stepping back from the door, you don't have time to think about an escape plan before it slams open."

        play sound s_crash
        with vpunch

        show lieutenant attack with dissolve

        lieutenant "You!"

        you "Wait! I can explain..."

        lieutenant "Shut up. Come with me."

    else:
        "You reach the bottom of the ladder, only to feel the cold point of a blade against your back."

        show lieutenant attack with dissolve

        lieutenant "Easy, there, pimp. Came to join the party?"

        "You turn around slowly."

        you "Lieutenant. I expected to find you in here."

        lieutenant "Is that so? Well, I certainly didn't expect to see {i}you{/i}."

        lieutenant "Come with me. You've got some explaining to do."

    scene black
    show bg thieves_guild room at top
    with fade

    show lieutenant:
        xalign -0.2
        ypos 0.2
    with dissolve

    show renza at right:
        zoom 0.9

    with dissolve

    if NPC_renza.met:

        renza "Master [MC.name]... So you're the one sneaking around my house. I thought you got the message the first time."

        "You don't like the way she is fingering her steel dagger while speaking."

    else:

        renza "Who the hell is this?"

        lieutenant "A small-time pimp from the slums. I have no idea what he's doing here, but I'm sure he's gonna tell us..."

        "She pushes her rapier against your back, just enough to bend the steel."

        lieutenant "Aren't you, pal?"

    you "All right, everyone, please relax. I came here looking for answers, not to cause trouble."

    renza "Oh, really? And what kind of answers would that be?"

    you "The guards raided my house, and grabbed all my money. I thought the lieutenant might be involved."

    lieutenant "Me? That's preposterous!" with vpunch

    lieutenant "I set you up for a license with the city office, like you asked me to. Someone must have ratted out on you."

    play sound s_sigh

    renza "It is a strange coincidence... We might have a common interest, after all."

    you "What do you mean?"

    if not NPC_renza.met:

        renza "Allow me to introduce myself. I'm Renza, head of the thieves guild."
        $ renza_name = "Renza"
        renza "I believe you already know Lieutenant Lydie."
        $ lieutenant_name = "Lydie"


    renza "As you probably know, the city guard and the thieves guild are at each other's throats."

    you "Of course. The age-old enmity between the law and the thieves..."

    renza "Ha! More like the age-old enmity between two rival gangs. I'd be lucky to steal and rob half as much as the Guard captain."

    lieutenant "The captain uses the city guard like a private army. The lion's share of the taxes and bribes goes to the captain's coffers,
                right under the King's nose."

    lieutenant "The slums are the Guard's private playground. No one within the city walls cares if a few peons are shaken down or disappear."

    you "Well, aren't you an officer with the guard? Why are you telling me this?"

    renza "Lydie is one of our best. We sent her to infiltrate the Guard and learn of its secrets, until the time
           was right to strike."

    $ lieutenant_name = "Lydie"

    you "To strike? You mean..."

    lieutenant "Yes. Take down Captain Farah."

    you "..."

    you "I really don't see how that helps me one way or another."

    play sound s_sigh

    renza "Oh, that will help, believe me. First of all, you'd get to keep your life."

    you "Ah, well, that sounds good for a start."

    renza "And with a change of management at the top of the city guard, getting you your brothel license should be a piece of cake."

    you "I like the sound of that... Wait, change of management?"

    renza "Of course... Why do you think I've been grooming the lieutenant here for the past two years?"

    you "You... You want to replace the Guard captain with one of your own? That's..."

    if MC.get_alignment() == "good":
        you "Despicable!" with vpunch
    elif MC.get_alignment() == "neutral":
        you "Clever!" with vpunch
    elif MC.get_alignment() == "evil":
        you "Wicked!" with vpunch

    renza "Why, thank you, you vile flatterer... *wink*"

    lieutenant "This is all still very far from happening. Renza, need I remind you of the situation?"

    you "The situation?"

    renza "Humph. We might as well bring you up to speed."

    renza "We've got a bit of a problem. Our good lieutenant's cover has been... compromised."

    you "What?"

    lieutenant "I was followed on my way here. Two guards were sent on my trail, and I didn't manage to lose them."

    renza "Fortunately, my men captured them before they could report back to the Guard office. But
           it's only a matter of time before someone notices their disappearance."

    lieutenant "And when they do... Whoever sent them will know that they were right to suspect me."

    you "Damn... You're in a tight spot."

    renza "We are... That's why I'd like to enlist your help."

    you "Me? What can I possibly do?"

    renza "We have captured the two officers. I want you to interrogate them."

    you "Wait... Why me?"

    renza "Well, you're an experienced [MC.playerclass], aren't you? I'm sure you have some tricks up your sleeve."

    renza "They haven't seen us together yet. We think it's better if they don't meet face to face with me or the lieutenant.
           We can still recover from this fiasco if we keep them in the dark as much as we can."

    renza "But I'll interrogate them myself if I have to... And then I'll turn them into corpses. I couldn't let them go
           after they've seen me."

    you "That's harsh."

    renza "Maybe. So why don't you give it a try, before I have to dirty my hands?"

    lieutenant "The two officers are sergeants in my squad."

    renza "We captured them separately. It's almost like they were working on distinct assignments."

    lieutenant "They're in the cells at the end of the corridor. Their names are Maya and Kashiv."

    $ sergeant_name = "Kashiv"

    you "Maya?"

    you "Wait a minute!"

    menu:
        renza "What?"

        "I know Maya, she's clean":
            $ renpy.block_rollback()
            you "I know Maya. No need to interrogate her. She's not involved in the Guard's corruption."

            $ MC.good += 1
            $ maya_protected = True

            lieutenant "Oh? And what makes you so sure?"

            you "She defended me with another guard when I was under attack by some street thugs. I'm pretty sure they were
                 corrupted guards in disguise. She's clean, she must be."

            lieutenant "It's true that she was always quite the righteous one..."

            renza "Anyway, she's still a security risk. I'll need to keep her locked up until the coast is clear."

            lieutenant "I guess we need to focus our efforts on Kashiv, then. I always knew that bitch was up to something."

            renza "Make sure to talk to Maya as well, though. She might know something."

            lieutenant "Use whatever means necessary to get Sergeant Kashiv to confess. We don't have time."

        "Uh, nothing":
            $ renpy.block_rollback()
            $ maya_protected = False

            renza "All right, it's settled, then. Go and question those bitch guards."

            lieutenant "You can use any means necessary. Time is of the essence..."

            you "Any means necessary?"

            renza "That's right. I don't care what you have to do to these sorry sluts. Ram a stick up their ass if you have to.
                   What the guards do when they catch one of our own is a hundred times worse."

    you "I see... Let me handle this."

    play music m_oriental fadein 3.0

    scene black with fade

    show bg thieves_guild corridor at top with dissolve

    "You head back to the main corridor in the thieves guild basement and walk down to the prisoner cells."

    "A thief guard is waiting for your orders."

    "It is time to interrogate the prisoners. What will you do first?"

    menu:
        "What will you do first?"

        "Visit Maya" if maya_protected:
            call c1_maya_interrogation from _call_c1_maya_interrogation

            scene black with fade

            show bg thieves_guild corridor at top with dissolve

            "Leaving Maya's cell, you tell the guard that you will now visit the sergeant."

            call c1_sergeant_interrogation from _call_c1_sergeant_interrogation


        "Interrogate Maya" if not maya_protected:
            call c1_maya_interrogation from _call_c1_maya_interrogation_1

            scene black with fade

            show bg thieves_guild corridor at top with dissolve

            "Exiting Maya's cell, you wipe the dust from your jacket. You tell the guard that you will now visit the sergeant."

            call c1_sergeant_interrogation from _call_c1_sergeant_interrogation_1

        "Interrogate Kashiv":

            call c1_sergeant_interrogation from _call_c1_sergeant_interrogation_2

            scene black with fade

            show bg thieves_guild corridor at top with dissolve

            "Exiting Sergeant Kashiv's cell, you wipe the dust from your jacket. You tell the guard that you will now visit Maya's."

            call c1_maya_interrogation from _call_c1_maya_interrogation_2

    call c1_interrogation_report from _call_c1_interrogation_report

    $ story_add_event("c1_satella_intro")

    "Rendezvous with Renza at the {b}thieves guild{/b}."

    $ game.set_task("Rendezvous with Renza at the {b}thieves guild{/b}.")
    return


label c1_maya_interrogation:

    $ renpy.block_rollback()

    "You tell the guard that you will visit Maya. He opens the door for you."

    play sound s_door

    show bg cell at top with fade

    show maya disarmed with dissolve

    you "Hello, Maya."

    maya "Have you come to torture me? You won't get anything from me, scum."

    maya "Wait, you look familiar..."

    play sound s_surprise

    maya "You're the one Roz and I defended in an alley, some days ago! You were travelling with your pink hair slave..."

    you "Your memory serves you well."

    maya "If I had known you were a filthy thief, I would have left you there to rot! Leave me alone, you bastard!"

    if maya_protected:

        you "Relax, I'm not here to hurt you. And I'm not with the thieves guild. For what it's worth, I defended you back there.
             Convinced them you were not a corrupted guard."

        "She scoffs."

        maya "A corrupted guard? What are you talking about? What do the thieves care about corruption?"

        menu:
            "Tell the truth":
                $ renpy.block_rollback()
                $ MC.good += 1

                you "The thieves have had enough with the Guard's harassment. They want to replace the current captain with one of their own."

                maya "The lieutenant..."

                you "Yes. You'd better keep it to yourself if you want to stay alive."

                play sound s_surprise

                maya "We must not allow this to happen!" with vpunch

                you "What do you mean? Are you supporting the captain now?"

                maya "Oh, Arios no. I know how bad things have become lately, and I know the Captain is behind this."

                maya "But a thieves guild puppet wouldn't be any better as a replacement."

                you "It's not like we have a lot of options here."

                play sound s_sigh

                maya "..."

                maya "Listen, I'm thankful that you told me the truth. I believe you when you say you're honest. So hear me out."

                you "I'm listening."

                maya "Play along with the thieves as long as necessary. Do what you must to bring Captain Farah down."

                maya "But when the time comes to choose a new captain, you must expose the lieutenant as a thief spy. Do not let her become the
                      head of the city guard."

                you "Mmh... That's a tall order. What's in it for me?"

                maya "To do the right thing? For the citizens of the Slums?"

                you "Mmh..."

                maya "And of course, you would get the Guard's support in your business endeavors. Get you a proper business license, perhaps?"

                you "That would help."

                maya "Promise me to think about it. And I'll tell you what I know."

                you "Okay, okay."

                call c1_maya_confession from _call_c1_maya_confession

                maya "Yes. Please, leave me now..."

                you "Fine. Stay put."

            "Stay vague":
                $ renpy.block_rollback()
                $ MC.neutral += 1

                you "Well... They didn't say. But they want to expose the corruption in the Guard, so I'm sure you could find some common ground with them, if you tried."

                maya "Common ground! With thieves! Have you come here to insult me!" with vpunch

                you "Calm down, it's not like that... Anyway, there is little you or I can do. They want information about the Guard's dealings. They suspect the captain."

                maya "Oh, how insightful of them. And this is all out of their good hearts, uh? *angry*"

                you "Help me out here, Maya. They are not patient people."

                maya "..."

                maya "Fine, I'll tell you what I know. It's mostly public knowledge, anyway."

                maya "Not like I care what happens to the damn captain."

                call c1_maya_confession from _call_c1_maya_confession_1

                maya "Yes... Please, leave me now... And think about what I said. Try to do the right thing."

                you "Fine. Stay put."


    else:
        you "Tall words, for someone in your situation. I've been sent here to make you talk."

        maya "You ungrateful bastard! I saved your ass!"

        you "I don't like your tone. Don't forget who's in charge now."

        maya "..."

        maya "I won't tell you anything. What are you going to do? Beat me? Torture me?"

        maya "Or..."

        "Her eyes widen with fear."

        maya "R... Rape me?"

        menu:
            "Of course not":
                $ MC.neutral += 1
                $ renpy.block_rollback()
                you "Don't be so melodramatic. I just want a little chat."

                "She looks relieved, but still wary."

                maya "You're wasting your time. I have nothing to tell you."

                you "What about the captain?"

                play sound s_surprise

                maya "The captain??? Why do you ask about the captain?"

                you "Come on, I know about the corruption gnawing at the Guard from the inside. And I believe that corruption starts from the head."

                maya "..."

                maya "You're not wrong. But that's got nothing to do with me."

                you "Talk, then. Nothing bad's going to happen to you... If you tell the truth."

                play sound s_sigh

                maya "Humph."

                maya "Very well, I shall tell you. I have no interest in protecting the corrupted in our midst."

                call c1_maya_confession from _call_c1_maya_confession_2


            "Rape you? Mmmh...":
                $ renpy.block_rollback()
                $ MC.evil += 1
                "You move in closer."

                you "Well, that sounds like an interesting idea."

                maya "Move away from me!"

                "Her tone is now completely panicked."

                you "Relax... I can make it worth your while..."

                play sound s_surprise

                "You pat her butt. She tries to slap you, but you grab her wrist." with vpunch

                "Giving her a dead serious look, you hiss your final threat."

                you "The captain. Tell me what's going on. Now. Or I'll rape your cunt and your ass right here in this dank cell."

                play sound s_scream

                maya "No! Please! Don't do it, I'll tell you... Please."

                you "I'm all ears."

                maya "This is what I know..."

                call c1_maya_confession from _call_c1_maya_confession_3

                maya "That's it, I've told you everything I know."

                you "Have you, now? I was expecting more useful information..."

                play sound s_surprise

                maya "I told you everything! Now leave me alone!"

                menu:
                    "Leave her alone":
                        $ renpy.block_rollback()
                        $ MC.neutral += 1
                        you "All right, all right. Thank you for your help. I will give Sergeant Kashiv your regards."

                        maya "I don't care about that bitch! She can rot in the seven hells!"

                    "Rape her anyway":
                        $ renpy.block_rollback()
                        $ MC.evil += 5
                        $ MC.good -= 5
                        $ MC.change_prestige(1)
                        $ NPC_maya.love -= 25
                        $ NPC_maya.raped = True

                        you "You've been helpful..."

                        maya "..."

                        you "But I don't think I can let you off the hook... Not just now."

                        play sound s_surprise

                        maya "What! You... You told me..."

                        you "I told you if you talked, I wouldn't rape your ass and pussy."

                        you "So, I'm just going to fuck your pussy now. Isn't that fair?"

                        play sound s_scream_loud

                        maya "No!!!" with vpunch

                        "Ignoring her cries, you push her to the side of the cell and bend her over."

                        scene black with fade

                        show bg maya sex1 with dissolve

                        play sound s_screams

                        maya "No! Let me go you brute! Aaaw..."

                        "Pushing her against the wall, you swiftly lower her pants, exposing her naked butt and pussy."

                        play sound s_scream

                        maya "Stop it! Stoooop!"

                        "Her clean-shaven pussy looks like a shiny apricot: tight, soft, and inviting. This sight alone makes you hard."

                        you "What a nice little pussy... I can see you've been taking care of it for me. I appreciate that."

                        play sound s_scream_loud

                        maya "Don't touch me! This is not for... Aaaah!!!"

                        "You place your erect cock into contact with her tight cunt, gently pressing inward."

                        play sound s_surprise

                        maya "Please! I will be good! Don't... Please!"

                        you "You're so tight, I bet you didn't get with a lot of men... I can't wait to pump your young pussy full of cum."

                        maya "Noooo... *sob*"

                        "Torturing her, you keep rubbing your hard cock against her pussy lips." with hpunch

                        "Even though she is ashamed and resisting you, your back and forth movements begin to have effects on her."

                        "Her pussy lips open slightly under pressure from your cock, and you are satisfied to feel a little dampness wet
                         the tip of your dick."

                        you "I love to fuck bitches with a holier-than-thou attitude like you... They make great pets once they realize
                             they're just cock-loving sluts."

                        play sound s_surprise

                        maya "Shut up! Don't go any further! Please..."

                        play sound s_scream_loud

                        maya "Haaaa!" with hpunch

                        "She cries out as you slowly push your hard cock inside her pussy."

                        "Her inside walls are so tight that they squeeze your cock hard, as if trying to smother it. The feeling
                         is nice, and you stop for a moment to indulge in raw pleasure."

                        maya "Nooooo..."

                        "This pause gives Maya a little time to adjust and catch her breath. It doesn't last long, though, and soon you start
                         giving her a good pounding."

                        play sound2 s_moans_quiet loop

                        maya "Ooh... Aaah!!! Aaah..." with hpunch

                        "Shoving your dick in and out of Maya's tight pussy, you make sure she feels every inch of cock raping her by hitting her cervix with every move."

                        "Blushing red, Maya has stopped protesting temporarily, probably aware that it is useless."

                        "She hangs on to the wall for dear life, trying to retain her balance, while you pound her little pussy into submission."

                        play sound s_scream_loud

                        maya "Aaaaah!!!" with hpunch

                        you "I can feel your pussy becoming looser... What's happening? Do you like being raped in a dark cell by a stranger?"

                        maya "Nooo... I'm not a whore! Leave me alone..."

                        play sound2 s_scream

                        maya "Haaa!" with hpunch

                        "You hasten the pace, pounding so hard into her pussy that her feet almost leave the ground."

                        "Using your hand, you rub her clit while fucking her hard."

                        play sound s_moans


                        maya "Ha! Haaa..." with hpunch

                        "For all her pride, Maya can hardly resist the attention given to her nether regions. She begins to moan in a not-entirely
                         painful kind of way."

                        you "Deep down inside, you're a little slut, and you know it... Look how much you're enjoying being viciously fucked from behind."

                        play sound s_surprise

                        maya "No! I don't!"

                        "Her weak protest is belied by the wetness in her cunt. She's being abused and fucked raw in a dark cell, but it does
                         seem to turn her on."

                        you "Oh, really? And what's that?"

                        "You hold your hand to her nose. It is covered with her juice, which you rub all over her face."

                        play sound s_scream

                        maya "No! Disgusting!!! Get that away from me!" with hpunch

                        "She squirms as she tries to avoid your hand, delightfully wriggling around your cock. You feel your climax approaching." with hpunch

                        you "Now... Time to see if you'd make a good cum dump..."

                        play sound s_scream_loud

                        maya "No!!! Don't come inside, don't!" with hpunch

                        play sound s_screams

                        maya "Noooooo!!!" with hpunch

                        show bg maya sex2 with flash

                        you "Haaa!" with hpunch

                        "Moaning and grunting, you shoot a huge load of cum inside Maya's pussy."

                        with doubleflash

                        play sound s_orgasm

                        maya "Hiiiiiiiiiiii!!!"


                        "She squeals as you release hot cum into her hole."

                        "Her mind goes blank at the feeling as you rip
                         your dick out of her and shoot the rest of your load on her white bum."

                        show bg maya sex3 with doubleflash

                        you "Mmmmh... That was a good fuck..."

                        you "I feel like we've made progress, here, Maya. Haven't we?"

                        maya "Go... To hell... You monster..."

                        "You slap your still erect cock across her ass."

                        play sound s_punch

                        pause 0.5

                        play sound2 s_scream

                        maya "Hii!!!" with vpunch

                        you "You're a feisty girl, aren't you? You should learn to like this. Because I'm sure the guards outside will want their share of
                             that sweet pussy..."

                        play sound2 s_scream_loud

                        maya "Nooooo!!!" with vpunch

                        you "All right, I'll leave you to it. I've got other... 'business' to attend to."

                        $ unlock_achievement("h maya")

    return

label c1_maya_confession:

    with fade

    "Maya starts to talk."

    maya "The captain is lining out the Guard's coffers with tax and extortion money. A large number of the guards are dirty, and they work
          together with the captain and some corrupt officers to fill their pockets."

    maya "There are some in the Guard, like me and Roz, who enlisted because of our ideals. We couldn't believe what this place had become when
          we came back from the Holy War. We had our own idea of justice, and we wouldn't give up on serving the people of this town."

    maya "I've been trying to expose the captain for some time and take my case to the Court, but I still lack hard evidence."

    maya "The captain doesn't like to be exposed, so dealings go through petty officers that work as accomplices, such as Sergeant Kashiv."

    you "Kashiv, uh..."

    maya "I thought the Lieutenant was involved in some way. That's why I decided to follow her. And then I ended up here... Roz must be so worried..."

    you "Is that all you know?"

    return


label c1_sergeant_interrogation:

    $ renpy.block_rollback()

    "You nod to the jailer to open the second cell."

    play sound s_door

    show bg cell at top with fade

    show sergeant with dissolve

    "Standing in the dark cell with her back to the wall is Sergeant Kashiv. Her hands and feet are bound. She gives you an indifferent look as you enter the room."

    sergeant "Ha! Another one of those snakes, coming here to gloat."

    you "Hey, wait a minute... I know you!"

    you "You attacked me with your henchmen, a while back in the slums!"

    "She gives you a cold stare."

    sergeant "If you say so. Anyway, it looks like it failed. If not, you wouldn't be here to question me."

    sergeant "Who are you really, and what do you want?"

    menu:
        "I'm [MC.name]":
            $ renpy.block_rollback()
            you "I'm [MC.name], a [MC.playerclass] from out of town. I have a small brothel operating here in the slums."

            you "What I don't have, is a lot of patience."

        "You don't need to know":
            $ renpy.block_rollback()
            you "And here I thought I was the one asking questions."

            you "My patience runs thin... So don't test me{nw}"

            if MC.get_alignment() == "good":
                extend ", sergeant."
            else:
                extend ", bitch."


        "Your worst nightmare":
            $ renpy.block_rollback()
            you "Who am I? Your worst nightmare. What do I want? Answers."

    "She sneers."

    sergeant "Are you playing tough with me, pimp?"

    sergeant "I used to question all the prisoners before sending them off to the pit. I practically invented every rule in the book."

    sergeant "I used to whip my male prisoners' testicles until they turned purple, just for the fun of it... A small time thug such as you is not going to make me lose my cool."

    you "Wow, that's really nasty... You're a naughty girl, aren't you?"

    sergeant "Oh, please. If we're playing a game of good guard, bad guard, just send in your partner already. Don't waste my time."

    you "Who said there was a good guard?"

    sergeant "!!!" with vpunch

    you "You're mine for the night, and I have a number of things in mind."

    sergeant "..."

    "You watch carefully for her reactions to your next words."

    you "We could either have a peaceful talk..."

    "She scoffs."

    you "...or I could beat the crap out of you..."

    sergeant "Ha! Bring it on!"

    you "...I could make you obey me with a spell..."

    "She looks at you with disdain, but she seems a little less self-assured. She's the warrior-type, and most warriors are uncomfortable around magic."

    you "...or I could just fuck your brains out."

    play sound s_surprise

    sergeant "What?!?"

    "She wasn't expecting that. For a fleeting moment, you could see real panic in her eyes, but she quickly got a hold of herself."

    you "What is it? Does the thought of a dick up your cunt make you uncomfortable?"

    sergeant "Grrr... That's disgusting! I would never..." with vpunch

    you "What's the matter, Sergeant? You're blushing... Don't tell me... Are you a virgin?"

    "Her face is bright red now. She snaps."

    sergeant "I'll kill you, motherfucker! I'll gut you like a fish! *mad*" with vpunch

    you "I see... My guess was right..."

    "She yanks forward, looking set to murder you with her bare hands. You're thankful for the chains holding her back."

    sergeant "I'll kill you!"

    you "You're in a position to do no such a thing. In fact, you may not be alive when the sun rises tomorrow... And you may no longer be a virgin..."

    sergeant "Die, you bastard! I'll slaughter you! Face me in a one-on-one fight!"

    $ use_wits = True
    $ use_strength = True
    $ use_magic = True


label c1_interrogate_menu:

    menu:

        "What will you do to get the truth out of her?"

        "Use your wits" if use_wits:
            $ renpy.block_rollback()
            you "Come on, no need to lose your temper here... I'm sure we can come to an agreement."

            sergeant "Drop dead."

            # Run challenge
            call challenge("bluff", 8) from _call_challenge_5 # result is stored in the _return variable
            $ r = _return

            if r:

                you "Aren't you curious to know how we got you here?"

                sergeant "Got me? Hmmpf, I was hot on the Lieutenant's trail, that scheming bitch... And I got careless. I should have brought men for backup. What of it?"

                you "Bwahaha, you're naive... That's very cute, coming from you."

                sergeant "What the fuck are you talking about? Free me and I'll show you who's cute, when you beg me to keep your body parts! Grrr..."

                you "You've been played for a fool, and you don't realize it. The captain set you up, you and the other officers."

                sergeant "What? You expect me to believe that crap?"

                you "We have you in custody, as well as the lieutenant and another sergeant... The lieutenant is being interrogated right now, and quite roughly, I must say."

                you "The other sergeant is rotting in a cell right next to yours. Her name is Maya. We'll deal with her soon."

                sergeant "You're lying! Why would the captain..."

                you "It's a purge, you idiot. The captain passed a deal with the thieves guild. They're going to work hand in hand from now on."

                you "But some of the officers in the Guard stood in the way of the captain's complete domination... So you were set up. A pretty clever plan, I must say."

                sergeant "That's... Impossible! I'm not like the others! I've always been loyal!"

                you "Loyal, but ambitious... Sooner or later you were going to want more power for yourself, weren't you?"

                sergeant "..."

                you "Weren't you?"

                "You take a false look of pity as she looks increasingly lost and confused."

                you "You were expendable, Kashiv. You always were. The captain thought nothing of betraying you, just like the others."

                "Real tears are flowing down her face, now. She looks hurt and vulnerable."

                sergeant "I believed... Every word... I..."

                you "It's the captain who sent you on this 'errand', after the lieutenant, isn't it?"

                "You can see you guessed right."

                sergeant "I don't believe this... For years I was the captain's right hand... I thought..."

                you "You gambled on the wrong horse, and you lost. There's nothing you can do now. Except..."

                "Looking up through her tears, she gives you an expectant look."

                sergeant "Except?"

                you "Well, you could get payback. I don't know if vengeance is your thing, but..."

                "She clenches her fists with rage."

                sergeant "Tell me. What can I do? I want payback. I {b}demand{/b} it!" with vpunch

                "You smile. It seems you have lost nothing of your ability to play people like cithars."

                you "Help me then. I'm looking for leverage against the Guard. Get some dirt on the captain, anything that could help."

                sergeant "What's it to you?"

                you "Well, I can't say I'm too happy about this alliance between the Guard and the thieves guild. As a businessman, having a strong, all-powerful overlord doesn't sit very well with me.
                     So I'm thinking of double-timing the guild."

                sergeant "Crooked and despicable. That sounds like you. But what are you gonna do with this information?"

                you "Blackmail. Arm-twisting. Perhaps, removing the captain altogether."

                sergeant "..."

                sergeant "I can help you. But you have to promise me one thing."

                you "What?"

                sergeant "Use this information to completely destroy the captain and the officers who betrayed me. Don't just kill them; drag their reputation through the mud, have their minds and their bodies broken, force them into slavery and hard labor..."

                sergeant "And when it's done, {b}I{/b} will find them, and I will kill them." with vpunch

                "Her anger and hatred is painful to watch. Still, you're happy that you managed to get her to talk."

                $ NPC_sergeant.flags["interrogation"] = "tricked"

            else:

                you "Look, there's no need to make a fuss about this. I can get you released quickly if you cooperate."

                sergeant "Bite my ass."

                you "You're not making it any easier for you, you know?"

                sergeant "Fuck off. You'll get nothing from me."

                "You argue and plead with her for long minutes, but you can't get anything out of her apart from threats and insults."

                $ use_wits = False

                jump c1_interrogate_menu




        "Beat her up" if use_strength:
            $ renpy.block_rollback()
            you "You're a piece of work, you know that? I'll have to make an example out of you."

            sergeant "I'm not scared of you! Bring it on!"

            if MC.get_alignment() == "good":

                you "I really don't want to hit a woman. But you leave me no choice."

            elif MC.get_alignment() == "neutral":

                you "All right, have it your way. Whatever it takes."

            elif MC.get_alignment() == "evil":

                you "Great. Kicking bitches around is what I do for fun anyway."

            $ MC.evil += 1

            # Run challenge
            call challenge("force", 9) from _call_challenge_6 # result is stored in the _return variable
            $ r = _return

            if r:

                play sound s_punch

                "Before she can hurl another insult at you, you punch her with a vicious uppercut to the stomach." with vpunch

                sergeant "Ouch... Grrr..."

                play sound s_punch
                with vpunch
                pause 0.5

                play sound2 s_punch
                with vpunch
                pause 0.3

                play sound s_punch

                "Giving her no respite, you hit her until she's down." with vpunch

                play sound2 s_scream

                sergeant "Aaarh!"

                play sound s_punch
                with vpunch
                pause 0.3

                play sound2 s_punch
                with vpunch
                pause 0.1

                play sound3 s_punch
                with vpunch
                pause 0.4

                play sound s_punch

                "You kick her repeatedly, using the metal cap of your boots for maximum damage."

                play sound s_punch
                with vpunch

                play sound2 s_scream_loud

                sergeant "Aaarh!"

                play sound s_punch
                with vpunch

                play sound2 s_scream

                sergeant "Ooooh..."

                "You keep going for long minutes, even after hearing the sound of her ribs cracking."

                you "Talk to me, now, sergeant! Talk to me!"

                sergeant "You bastard... Ooooh..."

                "She really is quite tough. But you have one last card to play."

                you "You're reaching the limits of my patience."

                "Pushing her against the wall, you draw your knife, bringing it against her face. You push the blade up her left nostril."

                you "Do you like your nose, Sergeant? This is the first body part you're going to lose tonight, but not the last, if you don't talk."

                if MC.get_alignment() == "good":

                    "You steel your resolve, giving her a hard look. She must not find out you're bluffing."

                elif MC.get_alignment() == "neutral":

                    "You hope she won't make you resort to this."

                elif MC.get_alignment() == "evil":

                    "You give her a mad look. It's obvious you'll do it, and worse."

                "She looks at you in the eye, through tears of pain and rage. What she sees give her pause."

                sergeant "..."

                sergeant "Stop."

                "She cries."

                sergeant "Stop it. I'll talk. Don't... Don't hurt me."

                "Well, well. Looks like the tough bully was really a big softy at heart. What a surprise."

                "You let her go, and she crumbles on the floor, sobbing. You give her a minute to pull herself together, and tell her in a cold voice."

                you "Now, tell me everything. And don't hold anything back."

                $ NPC_sergeant.flags["interrogation"] = "beaten"

            else:

                play sound s_punch

                "You punch her in the stomach as hard as you can, and she cowers as she registers the blow." with vpunch

                sergeant "..."

                "But soon, she raises her head, grinning."

                sergeant "Is that the best you can do... Wimp?"

                "Furious, you double up your blows."

                play sound s_punch
                with vpunch

                you "Take this!"

                play sound s_punch
                with vpunch
                pause 0.3
                play sound2 s_punch
                with vpunch

                you "And this! And this!"

                "You keep hitting her as hard as you can, and she keeps smiling, even when hearing the cracking of a broken rib."

                sergeant "You'll never get me to talk! Never!"

                "She spits blood at you while you keep on beating her."

                "After a few minutes, it's obvious you'll achieve nothing more with physical violence."

                $ use_strength = False

                jump c1_interrogate_menu

        "Hypnotize her with a spell" if use_magic:
            $ renpy.block_rollback()
            you "You think you're tough, I get it. But I don't need to face you in a fight. I can simply melt your brains from where I stand."

            sergeant "..."

            you "That's right, I know magic. You think you're something, but I have ways to make you talk. Hell, I can even make you my bitch, if I choose to."

            sergeant "You won't dare! I'm not your plaything! I'm a fierce fighter!"

            you "We'll see about that."

            # Run challenge
            call challenge("control", 3) from _call_challenge_7 # result is stored in the _return variable
            $ r = _return

            if r:

                "Grabbing a flask of a potent anesthetic from your bag, you impregnate a piece of cloth."

                sergeant "Get away from me! Don't touch me!"

                "She fights you as much as she can, but her bounds prevent her from doing much. You shove the cloth in her face, and after a few moments, she slips into unconsciousness."

                sergeant "I... Uh... Zzzzz...."

                you "Now, let's get to work."

                play sound s_spell

                "Forcing her eyes open with one hand, you hold a bright glowing gem to her face with the other."

                "The yellowish glow is reflected in the white of her eyes as her pupils roll away from the light."

                you "You are alone. You are trapped. No one can help you here, not even the captain. Nothing awaits you here, but pain, and death."

                "She squirms in her sleep, looking restless. Beads of sweat fall down her forehead, and she tries weakly to get away from you. You keep her in position with an iron grip."

                you "Everyone has forgotten you. No one loves you here. No one cares about you here. No one... Except me."

                "She keeps struggling unconsciously, moaning in her sleep. Your last words seem to have a calming effect, however."

                you "I am the only friend you have. I am the only hope you have. If you confide in me, everything will be all right. I will protect you."

                "Little by little, she stops struggling. By the time you are finished with your incantation, she slips back into a more peaceful sleep."

                you "Oh, and one more thing. When I snap my fingers, {nw}"

                if MC.get_alignment() == "good":

                        extend "you will return to normal, forgetting everything I just said."

                        $ NPC_sergeant.flags["charmed"] = "good"

                elif MC.get_alignment() == "neutral":

                        extend "you will return to normal, acting like you used to. But you will still be loyal to me, unable to hurt me."

                        $ NPC_sergeant.flags["charmed"] = "neutral"

                elif MC.get_alignment() == "evil":

                    $ MC.evil += 1

                    extend "you will become irrepressibly horny. You will feel the need to masturbate anywhere and display your disgraceful act to everyone."

                    $ NPC_sergeant.flags["charmed"] = "evil"

                "You are now finished. With gentle slaps, you wake the sergeant from her slumber."

                sergeant "Uh... Where... Where am I..."

                you "It's me. Your friend. You remember me?"

                "For a second it looks like she doesn't recognize you. Suddenly, it all seems to come back to her. Her eyes widen with worry, and she grabs your arm fearfully."

                sergeant "It is not safe here! We are in danger! Please, take me away from here!"

                you "Of course, my dear Kashiv, of course... But you must help me, so that I can help you."

                sergeant "H... Help you? S... Sure... I'll do anything, just get me out of here!"

                you "I will, you can trust me. I'm your {i}friend{/i}... I'm not like the {i}others{/i}."

                you "Now, tell me about the captain. Don't leave anything out."

                $ NPC_sergeant.flags["interrogation"] = "magic"


            else:

                "You take out a fancy looking mirror from your bag of tricks."

                you "This is a hypnotic mirror... It will make you obey my every order in no time."

                sergeant "Keep... Keep dreaming!"

                "Holding the mirror to her face, you start reciting the magic words."

                you "Mirror, mirror... Who's the tamest of them all... It's Kashiv, that's right, little Kashiv right over here..."

                "The mirror glows with ethereal light, and a halo of similar light brightens up the sergeant's face."

                sergeant "Uhn..."

                "The sergeant is struggling with all her might against the mirror's magical energies. You recite the words even louder as you bring the mirror closer to her face."

                you "You will obey... YOU WILL OBEY!"

                play sound s_scream

                sergeant "Aaaargh!!!" with vpunch

                "The sergeant looks in intense pain as she struggles to keep control over her thoughts. I looks like she is ready to give in any second now."

                sergeant "You'll... Never... Break... Me..."

                "You bring the mirror even closer to her face, now awash in magical lights."

                you "OBEY ME, you..."

                play sound s_punch

                pause 0.5

                play sound2 s_shatter

                "With her last bit of will the Sergeant headbutts the mirror right in the center. The mirror shatters,
                 and the magic light dissipates into thin air." with vpunch

                play sound s_sigh

                sergeant "*pant*, *pant*"

                you "Bitch! My magic mirror!!!"

                "The sergeant gives you a triumphant look as blood runs from a cut on her forehead."

                play sound s_evil_laugh

                sergeant "I told you! You can't control me! WIMP!"

                $ use_magic = False

                you "Damn it... Just you wait..."

                jump c1_interrogate_menu


        "Rape her":
            $ renpy.block_rollback()
            $ MC.evil += 3
            $ MC.change_prestige(1)

            you "I see you won't go down without a fight. Fine, I'll just focus on your weak point then."

            play sound s_surprise

            sergeant "What do you mean?"

            "You bring your hands to her breasts."

            play sound s_scream

            sergeant "No, get away from me!!!" with vpunch

            "Ignoring her, you pull at her clothes and pieces of armor. She tries to fight you, but you rip it all off her."

            scene black with fade

            show bg sergeant sex1 at top with dissolve

            "Leaving her wrists chained, you push her down to the floor of the little cell. You lift one of her legs in the air."

            if not use_strength:

                play sound s_scream_loud

                "She screams with pain because of her fractured rib."

            you "I've been patient with you, but this was all in vain. So I'll just fuck you raw until you tell me what I want to know,
                 or until you pass out..."

            sergeant "Get away from me!!! No! No!!!" with vpunch

            "She has some fight left in her, and she tries to kick you, but you ruthlessly spank her ass until it is red and sore."

            play sound s_punch
            with vpunch

            you "Stay put, bitch! You're getting what's coming to you."

            sergeant "I won't talk! Never!"

            you "Suit yourself."

            show bg sergeant sex2 at top with dissolve

            "You plunge your erect cock into her virgin hole."

            play sound s_scream_loud

            sergeant "Raaah!!!" with vpunch

            "She tries to resist you, but even the strong muscles in her thighs are not enough to stop your hard cock from pushing inside her."

            "Tears of rage run down her cheeks as you savage her tight pussy."

            "The pain and fear of having her virginity brutally taken away leaves her in shock, unable to protest for a moment.
             You take advantage of her newfound silence to abuse her as you fuck her."


            you "Well, I bet all those prisoners you whipped would be happy to see you in such a situation... Naked as the day you were born, fucked hard
                 in your virgin cunt down in the dirt and hay..."

            play sound s_moans

            sergeant "I'll get you... I'll get you for this... Aaaw..."

            "Ignoring her, you give her a furious pounding, oblivious to her struggle. You derive perverse enjoyment from seeing this
             high and mighty bitch being reduced to a bare-butt fuckdoll."

            you "Brace yourself... I'm cumming..."

            play sound s_scream_loud

            sergeant "Noooo!!!" with vpunch

            you "Raaaah!!!" with flash

            show bg sergeant sex3 with doubleflash

            play sound s_screams

            sergeant "It's coming out!!! Nooooo..."

            "You cum load after load over her tight, virgin pussy, and the rest of her naked body."

            play sound s_scream_loud

            "She screams with rage as she receives a shower of hot cum, seething with anger and humiliation."

            you "Phew... That was fun."

            "Sticky cum slowly runs down her white body as you spurt your last drops into her still gaping hole."

            $ unlock_achievement("h kashiv")

            "You let her body fall flat down into the dust. She is barely able to breathe through her tears."

            you "Now... You will talk to me, won't you?"

            sergeant "No!!! Never!!! You can't make me..."

            you "Oh, really? You think I went hard on you? Think again... Next time, I will fuck your ass..."

            sergeant "No!!!"

            you "...then, I'll call in the thieves who captured you. I'm sure they'll be more than happy to have their go."

            sergeant "Stop!"

            you "Oh, and I forgot... They have some strong, large guard dogs too. We'll make them fuck you too... Guard dogs fucking a bitch guard... Wouldn't that
                 be something?"

            play sound s_scream_loud

            sergeant "STOOOOP!!!" with vpunch

            "She yelled at the top of her lungs, completely losing her nerves."

            "You fall silent, awaiting her next words. For a long moment, only the sound of her heavy breathing and sobbing can be heard in the cell."

            "She finally starts talking again."

            sergeant "I..."

            sergeant "I will..."

            "She's getting there."

            sergeant "...talk."

            sergeant "I will talk. Just... Stop. Please."

            "Finally, you've broken her will."

            you "Fine. Let me hear what you have to say."

            $ NPC_sergeant.flags["interrogation"] = "raped"

    scene black with fade

    show bg cell at top with dissolve

    show sergeant with dissolve

    you "First, tell me about the captain."

    "The sergeant begins her confession, in a monotone voice."

    sergeant "The captain recruited me after I arrived in Zan, fleeing from the Westmarch principalities..."

    sergeant "I killed a nobleman back there, which is a terrible offense. But the city guard here provided me with shelter, and a
              new family, so to speak."

    sergeant "The captain took care of me and I grew to become a trusted confidant... But I was never promoted from sergeant, because
              I needed to keep an eye on the men."

    sergeant "Instead, that up and coming lieutenant slut grew to become her second in command... Pretending to be the captain's pet.
              But I knew I was the one that the captain really trusted."

    you "What kind of assignments did you carry out for the captain?"

    sergeant "Assassinations, robberies, extortion, phony arrests... You name it. The captain had a precise plan to take over the slums, and do away
              with anyone who opposed the Guard."

    sergeant "We also took requests from powerful citizens, in exchange for money."

    sergeant "That's how we got the order to take you out... Some rich business owner in town wanted you dead... He also wanted your slave for
              some reason, if I remember correctly. So he hired the Guard's help to get rid of you."

    you "Dammit, I knew it! Kosmo, that filthy bastard..."

    sergeant "He wasn't pleased that the attempt failed, or so I've heard. But I don't deal with the customers, I only carry out the operations."

    you "But how does stealing my money further the captain's plans?"

    sergeant "Oh, it doesn't. But one thing the captain can't resist is the lust for more gold."

    you "So... Do you have any hard evidence that implicates the captain?"

    sergeant "None. Orders are always given orally. If anything happens, the captain can always claim it was seditious elements in the Guard that
              did it. Protect the last link of the chain."

    you "I see. Clever."

    sergeant "But I suspect..."

    you "What?"

    "She hesitates."

    sergeant "Nothing."

    you "Tell me!!!"

    sergeant "Fine... I suspect someone higher up is giving the orders. The buck doesn't stop with the captain."

    you "And how do you know that?"

    sergeant "Well, with the amount of looting and stealing that the city guard gets away with, I always felt that we had a powerful patron
              covering up for us in the city... Someone at court, I would say."

    sergeant "But the captain is too smart to ever mention anything like this to me."

    you "So... How can we frame this captain of yours?"

    sergeant "You can't. The captain has no weaknesses, except loving gold, of course..."

    you "..."

    you "I have one final question. Where is my fucking money?"

    play sound s_surprise

    sergeant "W... What?"

    you "My money. The [game.goals[0].value] gold I saved to obtain a brothel license."

    you "Where is it???" with vpunch

    sergeant "Well... The captain gave the order to raid your house. I guess the money is in the Guard office vault by now."

    you "I see. Thank you for your... cooperation."

    if NPC_sergeant.flags["charmed"]:

        if NPC_sergeant.flags["charmed"] == "evil":

            "You snap your fingers."

            play sound s_surprise

            sergeant "Ha!"

            "The sergeant drops to her knees, squirming desperately."

            sergeant "What's... Happening to me... Aw, I'm so hot..."

            "She tears at her clothes desperately. Not even minding your presence, she exposes her crotch and starts rubbing her clit with her fingers."

            sergeant "I wanna cum! I wanna cum!!!"

            play sound s_orgasm_fast

            sergeant "Aaaaaaah!!!" with doubleflash

            "You leave her to her games. As you step out, you hear her scream."

            play sound s_moans

            sergeant "Come!!! Come watch me!!! I'm a dirty slut, aaah... Everyone come and watch me cum!!! AAAAAH!!!"

        else:

            "You snap your fingers. A veil comes over the sergeant's eyes... When it lifts, she gives you a blank stare."

            "She suddenly seems to notice you."

            sergeant "Ha! Another one of those snakes, coming here to gloat."

            you "I'll be going now..."

            sergeant "Uh?"

    return


label c1_interrogation_report:

    play sound s_door_close

    scene black with fade

    show bg thieves_guild corridor at top with dissolve

    "You step back into the corridor after interrogating the two women, reflecting on what you've learned."

    you "It is clear the Guard and its captain are behind all this... And responsible for robbing me, too. But how can we get back at them?"

    "You go back to Renza's room."

    play sound s_door

    show bg thieves_guild room at top with fade

    show renza at right:
        zoom 0.9

    show lieutenant:
        xalign -0.2
        ypos 0.2

    with dissolve

    renza "So?"

    lieutenant "What have you learned?"

    you "Well... I'm not sure it is very useful."

    renza "Spit it out!"

    you "Okay... Here it is."

    you "The captain has corrupted several officers and large swathes of the Guard..."

    lieutenant "Of course. We know that."

    you "...so a frontal attack is unlikely to succeed."

    renza "Yes."

    you "All orders are processed through the corrupted officers. Nothing is written down, so that no one can incriminate the captain."

    lieutenant "Damn it. We're screwed..."

    play sound s_sigh

    renza "Hmm..."

    you "Kashiv was tasked with carrying out the captain's dirty work, including requests from third parties, like wealthy citizens."

    you "Some bastard even sent the guards to steal my money!"

    renza "Hold on... Requests? Why did they take requests from others?"

    you "Well, the money mostly... The captain loves money. But there might be someone pulling the strings at court."

    lieutenant "I see. That would make sense..."

    renza "So the city guard has a powerful protector... And he's not going to let us take over without a reaction."

    lieutenant "So this is it. We're fucked."

    renza "Well, yes, we're fucked... Unless..."

    you "Yes?"

    renza "Unless..."

    play sound s_crash

    "She crashes her fist into the table, sending papers and spice flying in all directions." with vpunch

    lieutenant "Renza! What?"

    renza "[MC.name]! You said the captain loves money, right?"

    you "Well... Yeah. That's kind of obvious..."

    renza "And that Sergeant Kashiv is a trusted advisor, correct?"

    you "Yes... What are you getting at?"

    renza "While you were gone, we went through the sergeant's stuff. I found her seal and some messages she must have prepared for the captain,
           although no name appears on it."

    lieutenant "What about them?"

    renza "Well, as it turns out, I am an expert at forgery. I can write a fake letter of introduction for [MC.name]."

    you "Me? Why?" with vpunch

    renza "Think about it. You have been wronged, getting your hard-earned money stolen from you. So you want revenge."

    you "Oh, great plan. I'll go and threaten the captain with revenge. Then I'll get locked up for the rest of my days for my trouble."

    renza "No, hear me out. You don't want revenge against the city guard, they were just the middlemen. You want to bribe the guards to go after
           your rival! Give him a taste of his own medicine. And you can pay!"

    you "But... But... Even if that's what I wanted, I can't... I'm broke!"

    renza "Listen, I told you I'm an expert at forgery. I'll give you a letter of recommendation from the banking guild, placing your net worth at...
           a hundred thousand denars. It will look genuine."

    renza "You can then offer the captain a large sum to take care of your rival. For that amount of gold, you can demand a private audience..."

    renza "And Kashiv's letter will vouch for you. She might even imply that it would be a cost-effective way to cover up for their previous
           blunder, by making an unsatisfied customer... 'disappear'..."

    you "..."

    lieutenant "..."

    you "That's..."

    lieutenant "That's..."

    you "Wicked!!!"

    lieutenant "Mind-blowingly stupid!!! *mad*" with vpunch

    lieutenant "So [MC.name] gets a private audience. What good does it do to us? Do you want to send him as an assassin?"

    you "Hey! Hold on a minute!"

    play sound s_sigh

    renza "No, my friend, nothing as crude as that..."

    renza "Let me finish. We know that the captain won't commit to anything in writing. But oral instructions, on the other hand..."

    lieutenant "But what good is it? It's gonna be [MC.name]'s word against the captain of the city guard. A foreigner and a pimp... (Sorry, [MC.name]).
                That's not going to cut it."

    renza "I know. I am talking about much more direct evidence, that we could take directly to the public, and expose the captain's duplicity for all
           of Zan to see."

    renza "I'm thinking of... a voice crystal."

    lieutenant "A voice crystal?"

    if MC.playerclass == "Wizard":

        you "Wow, hold on a second. Voice crystals are very powerful magical devices. Only the ancient races knew how to make them."

        you "And even if we had one, they consume a crazy amount of magical energy."

    else:

        "You've heard rumors about such artefacts, but you thought they were long gone from the face of the earth."

        you "Wait, are you going to feed us some fairy tales?"

    renza "Listen to me. This is not as silly as it sounds. The ancients used to build those crystals. They called them 'Wyers'."

    renza "I know voice crystals are real... and I think I know where to get one. Charged."

    you "You've lost me. We would need very powerful, non-human magic..."

    lieutenant "Renza, you're not thinking..."

    renza "Her. I'm thinking of asking {i}her{/i}."

    lieutenant "You can't be serious."

    renza "I am. Dead serious."

    you "Ladies! Ladies. Who's 'her'?"

    lieutenant "..."

    renza "..."

    lieutenant "You tell him."

    renza "Okay..."

    renza "[MC.name], what do you know about Shalia?"

    you "Shalia? Goddess of darkness and deceit? I know her, of course."

    if MC.god == "Shalia":
        you "I am one of her worshippers. What about her?"

    else:
        you "I don't worship her, but I know of her sinister reputation. What about her?"

    you "You want to ask a {i}goddess{/i} for a magic crystal? You're more desperate than I thought."

    renza "Not a goddess, no. Not directly, anyway."

    you "Then who?"

    renza "As you must know, Shalia doesn't require a set place of worship. People who worship her, such as us thieves,
           are free to do it in the privacy of their homes, away from prying eyes."

    renza "However, it doesn't mean that Shalia doesn't have her temples. What god can do without a proper temple to stoke their vanity?"

    you "To the point, Renza!"

    renza "Fine. Every temple of Shalia is headed by a single priestess... More than a priestess, a favourite of Shalia, to whom she
           passed a fraction of her unmeasurable power..."

    renza "The {b}night mistress{/b}."

    you "The night mistress?"

    renza "Yes. I'm not surprised you haven't heard about it. I wouldn't know of it myself, a Shalia worshipper... If there wasn't a temple of Shalia
           right here, underneath the thieves guild."

    you "What???" with vpunch

    lieutenant "It is true. There is a temple here. It predates the guild by a long, long time."

    lieutenant "Very few know about it. And fewer dare venture down there."

    you "W... Why not?"

    renza "The night mistress is not fully human, you see... She's an avatar of Shalia, abducted as a babe and forged in the fires of the seven hells...
           To return as a night mistress."

    lieutenant "The night mistress is a bloodthirsty demon, preying on the souls of the Shalia cult's enemies and the unfaithful... She is also notoriously
                fickle, capable of dessicating a man for the smallest of slights, just by glancing at him."

    you "De... Dessicating?"

    renza "And we've all heard even worse stories. But we must request her help. Only a night mistress has enough power to create a voice crystal and fill
           it with godly energy."

    lieutenant "I'm not going down there. Not on my life."

    play sound s_sigh

    renza "*sigh* Fine. [MC.name], it's just you and me, then."

    you "Me? Why me? Can't you just..."

    renza "[MC.name], you're coming with me! End of discussion." with vpunch

    you "*sigh*"

    renza "Meet me here later. I will take you there."

    scene black with fade

    return

label c1_satella_intro():

    scene black with fade

    show bg thieves_guild corridor at top with dissolve

    show renza at right with dissolve

    renza "Follow me. And mind your step. It is very dark, and you don't want to fall down one of those pits."

    you "Pits? *gulp*"

    stop music fadeout 3.0

    play sound s_creak

    scene black with fade

    "You descend into darkness, following Renza's careful steps down a long, long staircase."

    you "Are we there yet?"

    renza "I wish you'd stop asking me this every ten seconds... Ah, here we are."

    play sound s_door

    play music m_demons fadein 3.0

    show bg shalia_temple at top with dissolve

    "You both enter into a dark hall, resembling a grotesque negative of a church of Arios."

    "Strange echoes fill the air, almost as if... voices... were whispering to you."

    "Crumbling benches layered with cobwebs await hypothetical worshippers."

    "Candles hardly shine any light on the walls, but you can see that they are covered with mysterious inscriptions and disturbing drawings. It seems black paint was used,
     or perhaps... Dried blood."

    "In the back of the hall stands an altar made of dark gold. It is covered with caked blood. Behind it, long and sharp
     sacrificial knives can be seen between piles of white skulls."

    you "Those are... from animals, right? Right?"

    renza "Err..."

    play sound s_door_close

    "As you walk down the aisle towards the grimy altar, you hear the doors close shut behind you. A look of terror comes to Renza's face."

    show bg satella_intro at top with fade

    "The sound of leather boots squeaking as someone walks slowly up the dusty carpet makes your blood stop cold in your veins. You feel a chill down your spine, as
     the demon voices mutter horrible things in your ear."

    "On the verge of losing your sanity, you make a tremendous effort of will, and turn around."

#    stop music fadeout 3.0

    show bg shalia_temple at top with fade

    show satella_standing with dissolve

    play sound s_evil_laugh

    satella "Oh, my, teeheehee! We have guests!"

    "You are shocked to see a diminutive teenage girl standing behind you, barely even sixteen."

    you "Oh."

    "She is dressed rather provocatively for her age, with a leather suit that leaves little of her young shapes to the
     imagination. She holds a crop in her hands, toying with it as she stops before you."

    you "Hello there, young lady."

    "Renza is too dumbstruck to talk. Evidently, she must be as shocked to see a teenager here as you are."

    you "You shouldn't be here, you know. Do your parents know you're here?"

    you "It's way past your bedtime."

    satella "W... What?"

    renza "[MC.name]..."

    you "Hush, Renza, let me talk to her. You have to know how to talk to teenagers, you know?"

    you "Listen, young lady. This is no place for you, and this is no way to dress at your age, I might add. If I were your father..."

    renza "*cough*, [MC.name]..."

#    show satella angry with dissolve

    "The girl seems to be angry that she is being talked down to."

    satella angry "How dare you! How dare you talk to me like this!" with vpunch

    you "Oh, I see, you think you're a big rebel, uh, talking back to adults like that. Be careful that I don't spank you myself, like your old man
         ought to do!"

    satella "WHAT!!!" with vpunch

    renza "[MC.name]! Stop!!! This is the night mistress!"

    you "Uh?"

    you "What? No, it can't be... You said the night mistress was a real woman, not some kid..."

    satella "A REAL WOMAN???" with vpunch

    renza "[MC.name]!!! For the love of Shalia, shut up!!!"

    you "..."

    play sound s_crash

    with vpunch
    with vpunch
    with vpunch

    satella "AAAAAAAAAAAAARRRRRRRRRRRRRRRRRRRRRHHHHHHHHHHHHH!!!!"

    play sound s_crash

    with vpunch
    with vpunch
    with vpunch

    play sound s_roar

    scene black with circlein

    "The ground shakes and demonic voices fill the air as all the candles in the room are blown out by hellish winds."

    stop music fadeout 2.0

    you "..."

    renza "..."

    you "Are we dead?"

    you "Are we... dessicating?"

    renza "Shut up."

    play sound s_fire

    show bg shalia_temple at top with circleout

    show satella at right with dissolve

    "The candles light up all at once. The night mistress is staring at you with a smile, looking like nothing just happened."

    play sound s_evil_laugh

    satella "Guests, teeheeeheehee! We haven't had guests in a long time, except..."

    "She gestures vaguely at the altar."

    $ satella_name = "Satella"

    satella "Anyway. We are happy to receive you. My name is Satella."

    satella "Oh, I know you! You came here with your mother. Renza, was it not?"

    renza "It's me, Mistress."

    satella "And who is your friend?"

    renza "Err, [MC.name], my lady. He's only recently arrived in Zan..."

    if MC.god == "Shalia":
        satella "Ah, [MC.name], yes, we know of him."

    satella "It's {b}so{/b} nice of you to come here. We were getting a bit lonely... Shall we offer you some tea?"

    renza "We are deeply honored, o night mistress, but we don't really have time..."

    play sound s_crash

    satella angry "TEA! TEA!!! MUST HAVE SOME TEA!!!" with vpunch

    renza "Oh course, night mistress, of course!!! We love tea! Don't we, [MC.name]!"

    you "Oh yes, we do! Tea is the best! Aha, ahaha..."

    play sound s_evil_laugh

    satella happy "Yay! Tea it is, for our new friends... Teeheeheehee!"

    satella "Just give me a minute! [emo_heart]"

    hide satella with dissolve

    "Satella runs to the back of the hall, and starts rummaging through a large chest."

    "You turn to Renza and whisper."

    you "Is {i}this{/i} the night mistress? I thought..."

    renza "Shut up, [MC.name], I implore you... You're gonna get us killed..."

    you "But look at her..."

    "The young girl is browsing through scores of alambics and potions, throwing them all around after inspecting them, making a terrible racket."

    satella "Ah! Here it is! Tea! Oh, and I forgot..."

    play sound s_spell

    "She claps her hands."

    play music m_satella fadein 3.0

    satella "Music for our guests!!! Yay [emo_heart] !"

    renza "..."

    renza "I'll admit it, she's a little strange for a half-goddess."

    show satella at right

    satella "What's that you say?" with vpunch

    play sound s_scream

    renza "AAH!!!"

    you "No... Nothing, night mistress, we just thought, uh... Nice music, by the way."

    satella "Teeheehee! Thank you! I like you!"

    "She pinches your cheeks and pulls them apart until it hurts." with vpunch

    satella "Smile, smile!!!"

    you "Ouch... Shtop..."

    satella "Anyway... Here's your tea."

    "She claps her hands, and the water in your cups boils instantly, sending a cloud of vapor into the air."

    "You look into the dark beverage with dread, not daring to ask what's in it. You can tell that Renza is feeling the same by the
     hopeless look on her face."

    "Closing your eyes and steeling your resolve, you take a sip."

    you "Mmh..."

    you "Mmh?"

    you "Mmh!!!"

    "It's actually really good black tea."

    satella "Like it?"

    you "S... Sure..."

    satella angry "YOU'RE NOT SAYING THAT JUST TO BE POLITE, RIGHT???" with vpunch

    you "N... No!!!"

    play sound s_sigh

    satella happy "Good! [emo_heart]"

    renza "Mistress, I hate to bother you with this, but... We have a request."

    satella "Oh, you do? [emo_heart]"

    "She bats her eyes innocently at you both."

    satella "What is it? I'm so curious!!!"

    you "Well, we're looking for a rare artefact..."

    renza "A crystal. Capable of recording a person's words, and playing it back..."

    you "A voice crystal."

    satella "Uhm, I know that thing you're speaking of... I used to have a bunch lying around here to sing my favorite songs into..."

    "You try not to picture this."

    satella "I broke most of them right off. They made my voice sound stupid."

    satella angry "AND IT DOESN'T!!!" with vpunch

    you "N... No, of course not!!!"

    renza "Not at all!!!"

    satella happy "Actually, you know how hard it is to find a good quality one? There's always some static, and I've tried to apply noise-reduction
             spells, but it never works very well... Also, people have a bad habit of speaking directly into the crystal. You shouldn't do that."

    satella angry "AND FOR FUCK'S SAKE PEOPLE, STOP SHOUTING INTO THE DAMN CRYSTAL! IT CAN HEAR YOU JUST FINE WITHOUT SHOUTING!!!" with vpunch

    you "We... We would never do that!"

    renza "Oh no, we wouldn't!"

    satella happy "Really? Then, I guess I can lend you one."

    renza "Really?"

    you "Really???"

    satella "Really."

    "You blow a sigh of relief."

    "Finally, things are starting to look up."

    satella "But of course, you will have to repay us, a favor for a favor..."

    "You knew it. You just knew this was coming."

    satella "My new friend [MC.name] here will be in my debt."

    you "*cough* Err, me? Well, this is as much a favor for Renza as it is for me, you know..."

    satella angry "{b}YOU{/b} WILL BE IN MY DEBT, OK!!!" with vpunch

    renza "Of course he will!"

    you "Uh... Understood..."

    you "So what... What do you want me to do?"

    satella happy "Oh, it's really no fun if I tell you now, is it? Teeheehee. We like to have our little secrets."

    you "*gulp*"

    satella "I'll let you know when it's time."

    satella "Now, do you care for some cookies? I'll bake them myself..."

    stop music fadeout 3.0

    scene black with fade

    "After exchanging many uneasy pleasantries with Satella, you and Renza finally manage to take your leave."

    show bg thieves_guild corridor at top with dissolve

    you "Phew... I thought we'd never make it out of there."

    renza "Tell me about it. At least I'm not the one who made a pact with a teenage demon..."

    you "What???" with vpunch

    renza "Uh, nothing! Anyway, we have the crystal now. We can set the next step of our plan in motion. Here's what I want you to do..."

    scene black with fade

    $ story_add_event("c1_captain_meeting")
    if MC.god == "Shalia":
        $ calendar.set_alarm(calendar.time+1, StoryEvent(label = "shalia1", type = "morning"))

    "Go to the {b}watchtower{/b} and confront the infamous captain of the city guard."

    $ game.set_task("Go to the {b}watchtower{/b} and confront the infamous captain of the city guard.")

    return


label c1_captain_meeting:

    #100% when going to location watchtower after guild scene

    play music m_knights fadein 3.0

    scene black with fade

    show bg watchtower at top with dissolve

    "Early in the morning, you head towards the Guard watchtower, grumbling about the wicked ways of women."

    you "How come I can never say no to a beautiful woman? *sigh*"

    "You are not sure about Renza's plan, but you agreed to carry it out anyway."

    "You had your own reasons."

    menu:
        "You had your own reasons."

        "I want my money":
            $ renpy.block_rollback()
            $ MC.neutral += 1

            you "I worked my ass off... Well, the girls' asses off, to get that money."

            you "It is mine by right, and I will get it back."

        "I want revenge":
            $ renpy.block_rollback()
            $ MC.evil += 1

            you "No one crosses me and lives to tell the tale."

            you "I'll get that captain. And when I'm done, I'll take care of Kosmo..."

        "I want justice":
            $ renpy.block_rollback()
            $ MC.good += 1

            you "The city guard is a menace, not just to myself but to all the slums' citizens."

            you "But today, I'm going to stop this. For justice!"

        "I'm firebatshit crazy":
            $ renpy.block_rollback()
            you "I have no idea why I agreed to this, but I don't care. I love risking it all on a whim!"

            you "And it looks like it's gonna be a fun ride..."

    scene black with fade

    show bg camp night at top with dissolve

    show lieutenant:
        xalign 0.0
        ypos 0.2
    with dissolve

    "When you reach the gates, the lieutenant is already there waiting for you."

    "She barely acknowledges you, not to arise suspicion, but she seems nervous."

    "She whispers as you pass her by."

    lieutenant "The captain got the letter. It seems to be going along as planned."

    lieutenant "A guard will take you upstairs. Good..."

    hide lieutenant with dissolve

    "You do not hear her last word. It must have been 'luck'. Or it could have been 'riddance', you're just not sure which."

    show guard with dissolve

    guard "Halt! State your name and business, citizen."

    you "I am [MC.name]. I requested an audience with Captain Farah."

    guard "..."

    guard "Yes, I can see that you did, and it has been granted. I will take you to the captain office."

    scene black with fade

    "You climb up to the very top of the tower, through a narrow circular staircase."

    "You can't help but think that should things turn sour, escaping will be very tricky..."

    "You also reflect on what you know about the captain. All the stories you've heard have been quite unnerving. Such a power-hungry, malevolent being..."

    guard "This is the captain's quarters. You may enter, I will wait for you here. You have twenty minutes."

    "That's it. You get ready to stare into the ugly face of evil."

    play sound s_knocks

    show bg captain_office at top with fade

    captain_voice "Yes?"

    play sound s_door

    "You enter the room. The guard closes the door behind you."

    play sound s_door_close

    you "Captain Farah?"

    show captain:
        xalign 0.5
        yalign 0.59
        yanchor 0.5


    with dissolve

    captain "Yes? It's me."

    you "B... B..."

    play sound s_horn

    show captain:
        ease 0.5 zoom 4.0 xoffset 300 yoffset -int(config.screen_height*0.25)
        pause 0.5
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    you "Boobs!"

    "Wow! You never expected this. The captain is a beautiful woman!"

    captain "I beg your pardon?"

    "She crosses the room towards you. Her every step makes her large tits bounce up and down."

    play sound s_horn

    show captain:
        ease 0.5 zoom 4.0 xoffset 300 yoffset -int(config.screen_height*0.1875)
        pause 0.5
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    you "*sweat*"

    captain "Are you ok, citizen? You look feverish. And, uh... It looks like you're drooling."

    you "Me? Oh, uh, sorry my lady."

    "You try to pull yourself together and keep your eyes level with her face."

    "Doing so, you can't help but notice that her womanly shapes are nicely complemented by her beautiful face. She has large, clear eyes. What a babe!"

    you "*gulp*"

    you "I... I am [MC.name] the merchant. I requested an audience because..."

    play sound s_sigh

    captain "Yes, I know why you're here. I got a letter from my subordinate."

    you "Ah... Good."

    captain "What you're asking for can be done... But it will be costly."

    captain "You see, taking someone out inside the city is more complicated than getting rid of some riffraff in the slums."

    captain "Here in the slums, I have complete dominion. I can have anyone arrested or killed on short notice."

    captain "But in the city, I must grease some hands, make sure some folks look the other way when necessary..."

    you "Is that so..."

    captain "So I can only do it for... Ten thousand denars. Take it or leave it."

    "She quoted the enormous sum matter-of-factly, awaiting for your reaction. You pretend not to be shocked by the outrageous amount."

    you "You are asking for a lot... But I can afford it."

    if MC.playerclass == "Warrior":
        you "Restoring my honor is more important to me than money."

    elif MC.playerclass == "Wizard":
        you "I can't let myself be outsmarted by a petty schemer from the city."

    elif MC.playerclass == "Trader":
        you "It's an investment. I will recoup it once I take over this man's business."

    captain "Oh, really?"

    "She takes a skeptical look at your attire and demeanor."

    captain "Forgive me, Master [MC.name], but you look a little young and inexperienced to be as wealthy as you claim to be..."

    captain "By the looks of you, I would take you for an adventurer who just arrived in town."

    "Her tone becomes overtly suspicious."

    captain "And why would a wealthy individual such as yourself feel the need to open a small, shabby brothel in the slums, of all places?"

    captain "Something doesn't add up."

    you "..."

    "She frowns."

    you "You're right."

    play sound s_surprise

    captain "What?"

    you "I wasn't born into money. I'm an adventurer, and I only recently came in town."

    captain "So, you have been wasting my time, then..."

    "The threat in her voice is razor-sharp. But you keep talking."

    you "I have come to Zan to meet my uncle, a rich banker from the guild."

    you "He told me to open a business, to prove that I could be a competent manager... So that one day, I could take over his loan-making business."

    captain "Did he, now..."

    you "Yes. So that's why I opened a small brothel in the slums, using nothing but my own money. However..."

    captain "What?"

    "She is losing patience."

    you "However, my uncle passed away last week, leaving me as his sole heir."

    you "I didn't have time to prove my worth as a manager... But I inherited a large amount of money, and I intend to put it to good use."

    captain "..."

    captain "Well, that is a nice story. And I suppose you can back it up with proof?"

    you "Of course."

    "You take out the forged documents that Renza made and hand them to the captain."

    captain "..."

    "You hope fervently that Renza is as good a forger as she said she was."

    captain "........."

    captain "It appears to be in order. Why, [MC.name], my good man, it seems that you have struck gold!"

    you "Well, my uncle passed away, and all..."

    captain "So your uncle croaked, big deal... You barely knew him anyway! But with that kind of money, you can do great things..."

    you "Well, sure..."

    captain "I have a feeling you and I are going to be fast friends. *wolfish smile*"

    "As she says that, she leans closer to you, giving you a seductive look."

    "You are getting hard just looking into her big green eyes... And the cleavage below."

    play sound s_horn

    show captain:
        ease 0.5 zoom 4.0 xoffset 300 yoffset -180
        pause 0.5
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0


    you "You... Err... Hem... Haven't you got money of your own, anyway?"

    play sound s_evil_laugh

    captain "Oh, I do, my dear, I do! But I can always use more. Let me show you something."

    "Turning around, she gestures softly for you to follow her."

    hide captain with dissolve

    "You take a good look at her well-rounded buttocks as she leads you to the back of the room."

    "There, she opens a large, steel door with three different locks."

    play sound s_creak

    show bg vault with fade

    captain "Tadaa!!!"

    you "Wow... What is this place?"

    captain "This is the vault, where I keep the fruits of the city guard's labor."

    you "The city taxes, you mean?"

    play sound s_evil_laugh

    captain "Ahahah! You could call it that... All the money that the wretches in the slums save patiently, denar by denar..."

    captain "The guards relieve them of their gold and send it all to me! ME!"

    "The glint of greed in her eyes has turned into a mad, feverish spark."

    captain "Taxes, fines, extortion, torture, I don't care how my men do it, as long as it all ends up here, in my vault!"

    you "So you get to keep the gold..."

    captain "And not just the gold! Look around you! I get the gems, the jewels, the family heirlooms, everything!"

    captain "And believe me, even the poorest beggar has something of value... You just have to beat him hard enough until he coughs it up. And if
             he doesn't... Well, no one will miss him, anyway."

    play sound s_evil_laugh

    captain "I am the queen of the outer city, now. The wretches in the slums are my subjects, working their asses off so that I can thrive!"

    you "But what do you do with all this money???"

    captain "Oh, come on! As a fellow rich person, you should understand this: you {i}always{/i} need more money."

    you "But with all these riches, you can already afford a lavish lifestyle..."

    captain "Oh, but I have expensive tastes! Do you think taking care of such a magnificient body comes cheap?"

    "She flaunts her assets right in front of your nose. You swallow hard and try to stay on topic."

    captain "Every day, I take a bath in a pool of the finest slave milk. I get five massages a day, by the best practitioners in the city.
             My hair is getting done every morning by my personal stylist. I also get a daily magic facial at the enchanted spa, and manicure at the
             fairy grove..."

    captain "I also like jewels, of course. I have thousands of them! Oh, and fine clothes and lingerie... Do you know how much they charge for Hokoman silk?
             The sky's the limit!"

    captain "And SHOES, of course. I have so many shoes!!! But I can never get enough... Shoes..."

    captain "I love SHOES!!!" with vpunch

    you "Wow."

    play sound s_sigh

    captain "There, you've done it. Now I just have to buy a fine pair of glass slippers first thing in the morning. *sigh*"

    you "I see. Looks like you have lots of legitimate uses for this gold."

    captain "Exactly!"

    you "But what I don't get is... This is technically tax money. Aren't you supposed to give it back to the city, or the crown?"

    play sound s_evil_laugh

    captain "Hahaha!!! This is a clever observation. But I have a deal... I have a powerful patron, someone high up inside the palace."

    captain "No one can touch me. They need someone to be in charge of the slums, as it serves their own ends in many ways. So they don't care if I keep the
             money, as long as I have the slums under control."

    you "They don't care about the money? What about the people of the slums?"

    play sound s_evil_laugh

    captain "Do you seriously think anyone at court is going to care about improving the life of the rabble in the slums?
             What are they gonna do, build roads and bridges? Please."

    captain "As far as they're concerned, I can spend all the tax money on clothes and shoes,
             and work the peons in the slums until they all starve. There are plenty more where they're coming from."

    captain "...And that suits me just fine."

    you "Wow, you're really something..."

    scene black with fade
    show bg captain_office at top with dissolve

    show captain with dissolve

    captain "Anyway, I will take care of your little problem. Your ten thousand denars will fit nicely in this vase next to my bed!"

    play sound s_mmmh

    captain "I will be able to let the gold run through my well-manicured hands for relaxation... Mmmmh..."

    you "Err, sure, whatever. So we have a deal."

    captain "When can you give me the gold?"

    "She cannot hide her impatience."

    you "Well, let us arrange an exchange soon... In a public place."

    play sound s_surprise

    captain "A public place, uh? I see, you don't trust me... I am pained."

    "She makes a show of having her feelings hurt."

    play sound s_sigh

    captain "Ah, Master [MC.name], and here I thought we were such good friends! But fine, we'll do it your way, if we must."

    you "Good."

    captain "Tomorrow is execution day. I will be overseeing the executions myself, with high ranking officials from the city."

    captain "I will get you an invitation to the tribune. We can talk safely during the morning hangings... Not many people will be paying attention."

    you "Perfect."

    captain "Good. Now, go."

    captain "And of course, keep everything you've seen here to yourself... No one would believe you if you tried to betray me, anyway. Are we clear?"

    you "Crystal clear. *smile*"

    captain "Good. Farewell now, my dear rich bachelor!"

    "She blows you a kiss, before shutting the door to your face."

    play sound s_door_close

    scene black with fade

    "Reaching into your pocket as you get down the stairs, you feel the reassuring warmth of the voice crystal."

    "You stop the recording spell by brushing off the appropriate rune, and put the stone back into your jacket."

    show bg watchtower at top with fade

    show stranger at right:
        zoom 1.2
        yanchor 0.8
    with dissolve

    "As you walk away from the tower, you notice a dark shadow, standing near a tree."

    you "Renza..."

    hide stranger

    show renza at right:
        zoom 0.8
    with blinds

    renza "Hi, [MC.name]."

    renza "How did it go?"

    "She is trying hard to hide the anxiety in her voice."

    you "As well as it could, I suppose. She swallowed the bait."

    renza "Oh, that's a relief... And the recording? You have it?"

    you "I do... Good thing she didn't know I was wearing a Wyer."

    renza "Perfect! [MC.name], you've been an amazing help..."

    you "Hehe... Don't make me blush."

    renza "We can now move on to the next phase of our plan... Did she agree to meet you in public?"

    you "Yes. Tomorrow, at the gallows, for execution day."

    renza "Oh, that's more than perfect... Many big shots will be there. We can finally fulfill our objective, and get rid of the captain!"

    renza "Are you ready for this?"

    menu:
        you "I'm ready..."


        "...to do anything for you, Renza":
            $ renpy.block_rollback()
            $ NPC_renza.love += 2

            you "You know I can't refuse you anything, Renza."

            "She blushes."

            renza "Oh, [MC.name]... Was that a compliment? Anyway, let's get ready!"

        "...to do the right thing":
            $ renpy.block_rollback()
            $ MC.good += 1
            you "I'm ready to do the right thing."

            "She looks a bit taken aback."

            renza "Uh, yeah, sure. Whatever you call it. Now, get ready."

        "...to get my money back":
            $ renpy.block_rollback()
            $ MC.neutral += 1
            you "I'm ready to do what it takes to get my fucking money back."

            "She smiles."

            renza "Always the pragmatist. Very well then, get yourself ready."

        "...to kick some ass":
            $ renpy.block_rollback()
            $ MC.neutral += 1
            you "I'm ready! Let's show those guard punks not to cross us!"

            "She laughs."

            "That's the spirit! Let no one get between you and your sweet revenge. Let's go!"

        "...to lie and manipulate people":
            $ renpy.block_rollback()
            $ NPC_renza.love -= 2
            $ MC.evil += 1

            you "I'm ready to lie and manipulate people until I get my way."

            "She laughs nervously."

            renza "Wow, how ruthless! Sometimes you scare even me, [MC.name]. Let's get ready!"

label c1_trial:

    stop music fadeout 3.0

    scene black with fade

    show bg street at top with dissolve

    play music m_suspense fadein 3.0

    "On the day of the public meeting, you make your way to the gallows."

    you "Damn, I'm nervous."

    if MC.playerclass == "Warrior":
        you "I hate these cloak and dagger intrigues. I long for a good head-on fight."
    elif MC.playerclass == "Wizard":
        you "Usually, when I dabble into politics, I don't risk ending with a rope around my neck."
    elif MC.playerclass == "Trader":
        you "I'm a businessman. I like to have other people handle the dirty business, not me!"

    if NPC_maya.raped:

        "You hear a commotion rip through the busy streets as you approach the plaza."

        roz "Have you seen this woman? You, have you seen her?"

        roz "Answer me!" with vpunch

        show roz at right with dissolve

        roz "You! Little man! I know you from somewhere!"

        "It's Roz, the guard who was accompanying Maya when she rescued you."

        you "Oh, we might have met... I'm not sure..."

        roz "We did! Me and my mate Maya, we saved your hide back there, when you were attacked by thugs!"

        you "Uhm, maybe, my memory is a little fuzzy..."

        roz "Listen!" with vpunch

        roz "Maya is missing, I've been searching for her high and low."

        roz "Have you seen her anywhere?"

        "You reflect that, at the moment, she's probably being gang-banged by a bunch of horny thieves. But you think it's best to keep it to yourself."

        you "I'm really sorry, Roz. I have no idea where your friend is. But I'm sure, err, she's fine."

        roz "Easy for you to say that!" with vpunch

        "Roz desperately turns to other strangers in the street, repeating his questions."

        roz "You, hey, you! Have you seen this woman? Blue hair, tanned skin..."

        hide roz with dissolve

        "You smile a crooked smile."

        you "Poor bastard... Hehe..."

    else:
        maya "Hey, [MC.name]!" with vpunch

        show maya at totheleft with dissolve

        roz "Maya! Don't go near that guy..."

        show roz at right behind maya with dissolve

        roz "Let me break his legs first!!!" with vpunch

        maya "Keep your cool, Roz. I told you he's not the one we have to worry about right now."

        you "Maya! What are you doing here? I thought..."

        roz "You thought she was rotting in her cell, uh, you jackass!!!" with vpunch

        maya "Roz, shut it! Let me handle this."

        "The large warrior seethes with righteous anger, but reluctantly holds back."

        if MC.get_alignment() == "evil":
            you "That's right, Roz. Be a good boy, stop tugging at your leash."

            "Roz gives you a murderous look."

        maya "Roz helped me escape from the thieves guild."

        maya "On the way out, we captured my jailer... That lecherous bastard. *angry*"

        maya "Anyway, Roz roughed him up a little, and he told us about the guild's plan. Exposing the captain, replacing her with the lieutenant...
              We know everything."

        roz "That's right, scumbag! We know of your friends' little plan..."

        maya "Please. I am appealing to your conscience here. The captain is the devil you know, but you don't know what the thieves guild is capable of."

        maya "They may be less brutal than the captain, but just as ruthless and greedy. The slums would be trading a master for another, and the people
              wouldn't be better off."

        menu:
            you "..."

            "You're right":
                $ renpy.block_rollback()
                $ MC.good += 1
                you "You're right. The way the people of the slums have been treated so far is unacceptable. I'm not going to pass this opportunity
                     to make things right."

            "You're wrong":
                $ MC.neutral += 1
                $ renpy.block_rollback()
                you "You're dreaming. The slums are the way they are because that's how the world works. It's not the thieves' fault if money trumps all."

                you "At least, the people of the slums will be robbed by just one gang instead of two."

            "I don't care":
                $ MC.evil += 1
                $ renpy.block_rollback()
                you "I don't have to explain myself to you. I'll do whatever I want."

                roz "The hell you will!" with vpunch

        maya "Please, listen. When the time comes, expose the lieutenant as a thief spy. Don't let her take over the Guard."

        you "Look, I really don't have time for a lecture now..."

        maya "Think about it, please."

        you "I have to go."

        maya "..."

        maya "All right. Go then."

        roz "Maya, you're not seriously..."

        maya "The die is cast. We'll be watching you, [MC.name]."

        hide maya with dissolve

#        show roz at center with move

        roz "..."

        roz "Listen, buster. I know the part you played in Maya's kidnapping. She may have forgiven you, but I haven't!" with vpunch

        roz "Watch your back..."

        hide roz with dissolve

        you "..."

    "Shrugging off the interruption, you hasten your pace towards the gallows."

    scene black with fade

    show bg gallows at top with dissolve

    "You reach the large plaza where the executions are carried out, close to the southern gate of the city."

    you "Here I am."

    "You spot the tribune where the high-ranking officials are seated. After showing your invitation to the guards, they let you
     climb the steps until you reach a seat next to the captain."

    show captain with dissolve

    captain "Oh, hi, [MC.name], lovely to see you... Please, have a seat."

    captain "Came to watch the show? Let's take a little break and enjoy ourselves, then we'll discuss business."

    hide captain with dissolve

    "Standing at the front of the tribune, the head judge is giving his final speech before the executions start."

    show judge with dissolve

    judge "Hem, hem."

    "Talking into a bullhorn, the judge addresses the massive crowd who gathered to witness the King's justice delivered."

    play sound s_crowd_cheer fadein 3.0

    judge "People of Zan!" with vpunch

    judge "Today, we gather to witness the just wrath of our good Lord and King, Pharo the 1st, exercised against the faithless rabble that
           acted against his divine will."

    judge "Those who stand before you have been rightly condemned after a vigilant and fair inquiry by our esteemed city guard, and stand to
           be executed for the vileness of their crimes."

    "The crowd roars in approval, hungry for blood."

    judge "Here is a sorry bunch of murderers, cattle and slave thieves, demon-worshippers, slaves who raised their hand against their master... All
           have been sentenced to the only penalty befitting their crime: Death!"

    play sound s_crowd_boos fadein 2.0

    "The crowd boos and jeers, slinging mud, rocks and rotten fruits at the hapless captives."

    "You reflect that many of the accused probably stand here because they happened to cross Captain Farah in one way or another."

    judge "Thus, we will proceed with the execution of these 42 unfortunate souls, before we move on to the main event of the day: quartering a
           necromancer!"

    play sound2 s_crowd_cheer fadein 3.0

    "The crowd roars with hurrahs and applause, chanting religious slogans of the church of Arios against necromancers and witches."

    play sound s_crowd_chant fadein 3.0

    "The judge basks in the adoration of the crowd. After a long pause, he proceeds with his speech."

    judge "Before we do, of course, I must first ask the ritual question."

    judge "Does anyone here wish to speak in favor of these poor wretches, before we send their souls to return to the one true Light, our glorious
           god Arios?"

    stop sound fadeout 2.0
    stop sound2 fadeout 2.0

    "A deathly silence falls over the crowd. No one hardly ever defends the condemned in Zan. They have been found guilty by gods and men,
     so surely they must deserve their punishment."

    judge "Very well, in that case..."

    play sound s_fire

    you "I DO!!!" with vpunch

    hide judge with dissolve

    "You stand vigorously, raising your voice louder than you thought you could."

    judge "You... What?"

    you "Let me speak. I have something to tell the people of Zan."

    captain "[MC.name]!!! What the hell do you think you're doing!!!"

    "You turn to the captain, and flash her a mischevious smile."

    you "Ever heard of voice crystals, captain?"

    "She is so shocked that she is rendered speechless. Suddenly, she understands what you mean."

    captain "A... voice crystal?"

    "The meaning of your words sink in. But it is too late. You are already moving down the stairs, towards the front of the tribune."

    captain "[MC.name]!!! Stop!!!"

    "The captain leaps to her feet, and desperately runs down the stairs to try and block your way."

    show captain:
        xalign 0.5
        yalign 0.59
        yanchor 0.5

    with dissolve

    captain "[MC.name]... Hear me out. Don't do this to me."

    you "..."

    captain "I don't know how much they paid you, but I can match it. Give me a chance. I will be the most powerful ally
             you'll have..."

    "She lowers her voice, and leans against you. Her ample breasts are bouncing, right under your nose."

    captain "I will make it worth your while, believe me..."

    play sound s_horn

    show captain:
        ease 0.5 zoom 4.0 xoffset 300 yoffset -180
        pause 0.5
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    ""

    "She flashes you her most seductive smile."

    captain "I know the hearts of men, [MC.name]... and the rest of them. I know how you look at me..."

    captain "Think about it. I'll let you do whatever you like, [MC.name]..."

    "She whispers into your ear as she mentions some things that make even you blush."

    captain "So, forget this stupid plan. Join me, instead..."

    you "Join you?"

    you "How would I know you're not going to stab me in the back the minute I agree to help you?"

    captain "Well... You have that crystal, and you can hold that as an insurance against me..."

    captain "And I like you, [MC.name]. You've managed to outwit me, and I can appreciate a good schemer. We have no reason to be enemies."

    you "Mmh..."

    menu:

        you "Mmh..."

        "All right":
            $ renpy.block_rollback()
            $ story_flags["c1_path"] = "evil"

            you "Fine. But I want my gold back, and the pimp license I required. Delivered by next morning."

            captain "You've got it."

            you "And I want perks. What can you offer me to make it worth my while? And I'm not talking about what happens between the sheets..."

            captain "Ok. Well, I can give you access to our inventory. Stuff we confiscate from merchants. I can't give it to you for free,
                     but I can give you a good price."

            you "Good. We have a deal, then."

            "She looks heavily relieved."

            captain "You've made the right choice."

            "She whispers in your ear."

            captain "And don't forget what I've said... Meet me in my chamber when this is all over."

            hide captain with dissolve

            show judge with dissolve

            judge "Ahem, hem."

            judge "What is it that you wanted to say, young man?"

            you "Me? Uh... Nothing! I thought I recognized that guy, over there, as the son of an Arios priest, but I was mistaken..."

            play sound s_crowd_boos

            judge "Wha... You're wasting our precious time, young man! *angry*"

            "The crowd is burning with impatience, waiting for the executions to resume."

            judge "Now, let us get back to justice-dispensing business... LET THEM HANG!!!"

            play sound2 s_crowd_cheer

            hide judge with fade

            "On your way down from the tribune, you find the lieutenant barring your way."

            show lieutenant attack:
                xpos 0.5
                ypos 0.2

            with dissolve

            play sound s_surprise

            lieutenant "[MC.name]! You traitor!!! What the fuck did you just do..."

            captain "Traitor?" with vpunch

            show captain at left:
                zoom 0.9

            with dissolve

            captain "Well, that's rich, coming from you."

            lieutenant "Captain? Don't... Don't listen to this man! He is a liar, and a fraud!"

            captain "Well, that makes two of you, then, lieutenant, wouldn't you say?"

            captain "Men!!! Arrest her!" with vpunch

            "Before the lieutenant can react, she is surrounded by armed guards."

            play sound s_woman_scream

            lieutenant "You... You've ruined everything!!!"

            captain "Take her away! I don't care what you do to her... But no one must ever hear of her again. You understand me?"

            guard "Yes, captain!"

            hide lieutenant with dissolve

            lieutenant "No!!! Damn you, [MC.name]! Renza will avenge me!!!"

            captain "And be on the lookout for this 'Renza'! Raid her precious guild, and do not give her a second of rest. You hear me?"

            guard "Yes, captain!" with vpunch

            show captain at center with move

            captain "You see? I told you we would be fast friends..."

            hide captain with dissolve


        "Not gonna happen":
            $ renpy.block_rollback()
            you "I'm sorry, Farah. But your reign of terror ends here."

            play sound s_scream

            captain "What?!?" with vpunch

            "She gasps."

            captain "How dare you! Then I'll just slit your throat, you bastard!"

            "She reaches for her dagger, but finds her scabbard empty."

            lieutenant "Looking for this?"

            show captain at right with move

            show lieutenant:
                xpos -0.1
                ypos 0.2
            with dissolve

            captain "Lieutenant? What the..."

            lieutenant "I've long waited for this day, captain..."

            "She holds the dagger to the captain's gut."

            captain "You are a part of this too? I knew you were hiding something from me... This is the day for traitors, I swear..."

            captain "Kashiv! Where is Sergeant Kashiv???" with vpunch

            lieutenant "It's a little late to ask this question, don't you think? She can't help you from where she is, you better believe it..."

            captain "Grrr..."

            hide lieutenant

            hide captain

            with easeoutleft

            show judge with easeinright

            judge "AHEM."

            judge "You wanted to make a statement, young man?"

            "Leaving the captain and the lieutenant to their stalemate, you step down to the front of the tribune."

            you "I do."

            judge "Then come forward. We are ready to listen to you. But make it quick..."

            "You step onto the platform, and take the bullhorn into your hands."

            "Turning to face the crowd, you address the people in a loud, clear voice, trying to hide your nervousness."

            you "People of Zan, I want you to listen... In fact, I am not the one who will be doing the talking."

            play sound s_crowd_boos

            judge "What?" with vpunch

            you "You are going to listen to the captain of the city guard, in her very own words."

            play sound s_spell fadein 1.0

            "Taking out the crystal from your pouch, you rub the proper rune. The crystal starts glowing a very bright light as the voice of the captain
             fills the air."

            captain_voice "...What you're asking for can be done... But it will be costly."

            "You play back the conversation you and the captain were having the day before."

            judge "What is this magic... This is impossible..."

            captain_voice "...Here in the slums, I have complete dominion. I can have anyone arrested or killed on short notice..."

            "The crowd listens religiously to the recording, in turns shocked, angry and bewildered by what they hear."

            captain_voice "...This is where I keep the fruits of the city guard's labor..."

            captain_voice "...All the money that the wretches in the slums save patiently, denar by denar..."

            captain_voice "...The guards relieve them of their gold and send it all to me! ME! And not just the gold..."

            play sound s_crowd_boos

            "At first, most people were incredulous. But it is unmistakenly the captain's voice, recognizable from her multiple public appearances."

            "The crowd roars with anger and indignation as the recording keeps playing."

            play sound2 s_crowd_boos

            "Your voice" "But what do you do with all this money???"

            captain_voice "...Oh, but I have expensive tastes... Shoes! I love SHOES!!!"

            "The crowd has had it. It's a riot down there. People are trying to rush to the tribune, pushing back the overwhelmed guards who try to keep them away."

            play sound3 s_crowd_riot

            captain_voice "Hahaha!!! That is a clever observation. But I have a deal... I have a powerful patron, someone high up inside the palace."

            play sound s_crash

            judge "ENOUGH!!! Enough!!!" with vpunch

            play sound s_punch

            "The judge rips the crystal from your hands, and grabs the bullhorn back."

            judge "Order!!! Order!!! Stand back!!!"

            play sound s_crowd_riot

            "The crowd mostly ignores the judge's yelling, continuing to push towards the tribune."

            judge "Young man, we have heard everything. Those are very serious allegations."

            judge "..."

            judge "Captain Farah, come forward."

            show judge at right with move

            show captain:
                xpos -0.1
                yalign 1.0

            with easeinleft

            play sound s_scream

            captain "Lies, these are all lies!!!" with vpunch

            judge "Captain Farah, do you deny that it was your voice that we could hear on that recording? Voice crystals always tell the truth."

            captain "I was tricked! I was duped! This man here forced me to do it."

            lieutenant "No he didn't." with vpunch

            hide captain
            hide judge
            with easeoutright
            show lieutenant at left with easeinleft

            lieutenant "I can vouch for these accusations. I have witnessed the captain's corruption firsthand while working with the city guard.
                        So have ten other guards, whose sworn testimony I hold at your honor's disposal."

            hide lieutenant with easeoutleft

            show judge at right

            show captain:
                xpos -0.1
                yalign 1.0

            with easeinright

            play sound s_scream_loud

            captain "She lies too!!! Listen to me..."

            "The judge looks embarrassed. He doesn't want the trouble, but a quick look back at the rabid crowd convinces him that he has no choice."

            judge "Captain Farah, I am placing you under arrest, pending further inquiry. Men, seize her."

            hide judge with dissolve

            show captain at center with move

            show guard as guard1 behind captain at left

            show guard as guard2 behind captain at right

            with dissolve

            play sound s_crowd_cheer

            "The crowd roars in approval as the lieutenant sends guards to take Farah away. She is livid with rage."

            captain "You!!! It's all because of YOU, [MC.name]!!! I will get you for this!!! I WILL GET YOU!!!"

            stop music fadeout 2.0

            play sound s_scream_loud

            captain "AAAAAARHHHH!!!" with vpunch

            play sound s_punch
            pause 0.3
            play sound2 s_punch

            hide guard1 with moveoutleft
            hide guard2 with moveoutright

            "The captain pushes back the guards who tried to rein her in."

            captain "You can't get me! You can't!" with vpunch

            captain "I am protected!!! I am protected!!! The Royal Family knows me !!! They..."

            kuro "THEY WHAT???" with vpunch

            play music m_palace fadein 2.0

            "Stupor strikes the whole plaza, as a clear, noble voice cuts through the chaos of the scene."

            hide lieutenant
            hide captain
            hide judge

            with easeoutleft


            show knight at left as knight1
            show knight at right as knight2
            show kuro at center
            with easeinright

            pause 1.0

            knight "Everyone!!! Bend the knee before the royal princess of Zan!!"

            "The crowd falls fervently to the ground before the princess and her knight escort."

            kuro "Is it true, Farah? Did you stoop down so low? Did you betray the trust of our people?"

            captain "Princess Kurohime!!! I... I..."

            kuro "And, as a final insult, did you just attempt to drag the good name of the royal family through the mud with yours?"

            captain "No, princess, no, I didn't mean..."

            knight "Do not talk back to the princess!" with vpunch

            kuro "It is lucky that I was passing by the execution plaza on my morning walk, and recognized that young man's voice.
                  I got to witness your lies and deception first hand."

            kuro "Judge!" with vpunch

            judge "Your... Your Highness?"

            kuro "As the first daughter of our beloved King, I order you to arrest this woman, and make an example of her. She is to be discharged immediately, as well as all of her accomplices in the city guard."

            judge "Y... Yes."

            kuro "And I thank you, young sir, for bringing this matter to the attention of the people of Zan."

            "She nods towards you."

            you "Your Highness... I am humbled..."

            judge "Let it be known that Captain Farah is hereby discharged, by order of the royal court. If no one objects, I therefore declare
                   our faithful lieutenant Lydie the new captain of the city guard."

            play sound s_crowd_cheer

            "The lieutenant beams with pride. The crowd erupts into applause."

            you "..."

            kuro "What is it, young sir? Is there something you would like to add?"


            if NPC_maya.raped:
                you "Nothing, Your Highness. Let us celebrate our new captain!!!"
                $ story_flags["c1_path"] = "neutral"

                "The crowd sings chants extolling the virtues of the new captain. You join the celebration with your new friends."

            else:
                menu:
                    you "Well..."

                    "Tell the truth about the lieutenant":
                        $ renpy.block_rollback()
                        $ story_flags["c1_path"] = "good"

                        you "There is one more thing."

                        play sound s_surprise

                        lieutenant "Uh?"

                        kuro "What is it?"

                        you "Your Highness, you shouldn't trust the lieutenant of the Guard either."

                        lieutenant "WHAT???" with vpunch

                        you "She is a spy, working for the thieves guild. I know this, because they tried to recruit me as one of their allies."

                        lieutenant "Shut up!!! You miserable worm!!!"

                        maya "This is true!!!"

                        hide knight1
                        hide knight2
                        hide kuro
                        with easeoutleft

                        show maya with easeinright

#                        show maya at left with dissolve

                        knight "Stand back!!!"

                        kuro "Who are you?"

                        maya "I am Sergeant Maya, your Highness. I served your father in the Holy Lands, before returning as a veteran to serve
                              in the city guard. I was at Kravni's Peak."

                        kuro "Then a right honourable fighter you must be. Not many of the King's men can claim to have seen that battle and live."

                        maya "I have witnessed first-hand the treachery of both the Guard captain and lieutenant. In fact, she had me kidnapped by her
                              friends in the guild. I don't know what cruel fate would have befell me if I didn't manage to escape in time."

                        "The lieutenant hisses."

                        lieutenant "We should have slit your throat when we had the chance, snake!!!" with vpunch

                        kuro "Judge! Arrest the corrupt lieutenant too."

                        play sound s_woman_scream

                        lieutenant "No!!! I was so close... So close!!! Let me go!!!" with vpunch

                        kuro "It seems to me that the ranking officers of the city guard were all corrupt beyond redemption. I do not trust any of them to take the helm now..."

                        kuro "You! Veteran fighter! What did you say your rank in the Guard was?"

                        maya "I... I am but a sergeant, your Highness."

                        kuro "That is good. Judge, bear witness to my royal command: you will make Sergeant Maya the Captain of the Guard, by order of the Crown."

                        judge "Of... Of course, your Highness!"

                        kuro "Captain, you are to root out all corruption from the city guard's midst."

                        maya "It... It is such an honor, your Highness!"

                        kuro "An honor that you didn't request, which is why I bestow it upon you. I will expect regular updates about your progress, captain.
                              Any wrongs you discover, I will see to it myself that they are righted."

                        maya "Your Highness... I will not disappoint you!"

                        play sound s_crowd_cheer

                        "The crowd cheers Maya's nomination."

                        stop music fadeout 2.0

                        with fade

                    "Nothing":
                        $ renpy.block_rollback()
                        $ story_flags["c1_path"] = "neutral"

                        you "Long live the new captain!"

                        "The crowd chants alongside you, cheering the new captain's promotion."

                        "You spot the lone figure of Maya in the crowd, looking at you with a disappointed look on her face."

                        "You shrug, and join the celebrations with your new friends."


    "You've made a powerful ally, today... And a powerful enemy. You hope it was the right choice."

    if story_flags["c1_path"] == "good":
        $ unlock_achievement("c1 good")
        $ MC.good += 5
        $ NPC_captain.love -= 100
        $ NPC_renza.love -= 10
        $ NPC_maya.love += 10
        $ new_captain = maya
        $ maya_name = "Cpt. Maya"
        $ captain_name = "Farah"
        $ thieves_guild.action = False
        $ story_gossip += chapter_gossip["c1_good"]
        call c1_ending_maya from _call_c1_ending_maya


    elif story_flags["c1_path"] == "neutral":
        $ unlock_achievement("c1 neutral")
        $ MC.neutral += 5
        $ NPC_captain.love -= 100
        $ NPC_renza.love += 10
        $ NPC_maya.love -= 10
        $ new_captain = lieutenant
        $ lieutenant_name = "Cpt. Lydie"
        $ captain_name = "Farah"
        $ thieves_guild.action = True
        $ story_gossip += chapter_gossip["c1_neutral"]
        call c1_ending_lieutenant from _call_c1_ending_lieutenant

    elif story_flags["c1_path"] == "evil":
        $ unlock_achievement("c1 evil")
        $ MC.evil += 5
        $ NPC_captain.love += 10
        $ NPC_renza.love -= 25
        $ NPC_maya.love -= 10
        $ new_captain = captain
        $ thieves_guild.action = False
        $ watchtower.action = True
        $ story_gossip += chapter_gossip["c1_evil"]
        call c1_ending_captain from _call_c1_ending_captain

    call c1_judge_fate() from _call_c1_judge_fate

    call advance_to_chapter(2) from _call_advance_to_chapter

    $ calendar.set_alarm(calendar.time+10, StoryEvent(label = "satella_letter", type = "morning"))

    return

label c1_ending_maya:

    scene black with fade

    show bg camp night at top with dissolve

    play sound s_crowd_laugh

    show guard party as guard1 at totheleft with dissolve

    guard "Hey, who are you?"

    play music m_disco fadein 15.0

    show guard party as guard2 at right with dissolve

    guard "Came to join the party?"

    you "Wow, you guys are enjoying yourself..."

    you "The name's [MC.name]. I came to see Maya."

    guard "Hey!" with vpunch
    guard "It's Captain Maya to you, punk!"

    roz "[MC.name]!"

    play sound s_punch

    pause 0.2

    play sound2 s_punch

    hide guard2 with moveoutright
    hide guard1 with moveoutleft

    show roz party at right with dissolve

    roz "Watch how you talk to my friend, rookies, or I'll have you clean the latrines 'til summer comes!"

    guard "Ouch! Y... Yes Lieutenant!"

    roz "[MC.name], my man! Nice of you to show up for the party."

    you "So she made you a lieutenant, uh?"

    roz "Of course! Who else could she trust in that position!"

    roz "Listen, ahem... I'm sorry I misjudged you earlier, [MC.name]. That was one hell of a public spanking you gave Captain Farrah! BWAHAHAHA!"

    you "Well, uh... Thanks..."

    roz "So, what are you doing here, [MC.name]? Eager to enlist with the rest of these rookies?"

    you "No, Roz. I'm looking for Maya. Rooting the corruption from the city guard is nice and all, but I still need a proper license for my business."

    roz "Oh, I see... Maya isn't much for parties, anyway. I think she's up in the captain office, planning the city guard's future, or some other similarly
         boring stuff..."

    you "Thanks, I'll show myself in, then. You... Enjoy whatever it is you're doing..."

    roz "Yay! Party time!"

    hide roz with dissolve

    stop music fadeout 3.0

    scene black with fade

    show bg captain_office at top with dissolve

    play sound s_knocks

    pause 1.0

    maya "Yes?"

    play sound s_door

    show maya disarmed flip with dissolve

    pause 1.0

    you "Hi, Maya. How are things going?"

    maya "Oh, it's you, [MC.name]. I've only started to make changes to the way things are run here..."

    you "I saw a lot of new faces downstairs."

    maya "Well, we fired all the officers and disciplined the men that were involved in the captain's schemes... Many of them had run away of
          their own, anyway."

    maya "We're in the process of drafting citizens from the slums to form the new city guard. We're looking for idealistic men and women
          who want to make a change... Turns out we found plenty of volunteers."

    maya "I seized all the assets that Farah had stolen and I gave half to the crown, which they were mighty happy about... Even though
          they are too conceited to show it."

    you "What about the other half?"

    maya "It's going to go back to the slums, in the form of community projects and long-awaited improvements... Sanitizing the river and sewers,
          fixing the roads, building a proper hospital..."

    you "Wow, you aren't losing any time..."

    maya "Of course! We have our work cut out for us before we can turn this place around."

    maya "Anyway, [MC.name]. There's something I ought to tell you..."

    you "What?"

    maya "I've ordered a raid on your friends at the thieves guild."

    "You're not sure how you're supposed to feel about this."

    you "Well, they weren't my friends exactly..."

    maya "Anyway, you might be relieved to know that we only found a couple of vagrants and bare rooms there. They were long gone by the time
          we got there. But if you see them again... Tell them to stay out of my way."

    you "Err, sure... Look, this is not why I came here."

    maya "Ah, yes, I know... You wanted to know about that license, right?"

    you "Yes. And my money. I've been through a lot to get this."

    maya "Fine. Just this time, I'll dispense with the standard process. Here is your gold, and I'll sign your license immediately. You will be authorized to work within
          the city walls."

    play sound s_gold

    $ MC.gold += blist[2].cost

    you "Thanks, that's great!"

    "You have got your [game.goals[0].value] gold back."

    you "Say, can't you throw in a little extra? Like, giving me access to the noble quarters, and the court?"

    maya "Hey, you're greedy! Spent too much time with the thieves guild, haven't you?"

    maya "I don't have the authority to handle access to the noble and royal quarters. This is beyond the city guard's jurisdiction."

    you "Aw... That sucks."

    maya "Perhaps you can make some new friends in high places? Having connections at court is sure to be useful for someone in your line of trade."

    you "I'll think about it..."

    play sound s_shatter

    with vpunch

    guard "You there! Stop!"

    play sound s_dodge

    pause 0.4

    play sound2 s_shatter

    with vpunch

    roz "Hey! Stop right here!"

    play sound s_punch
    with vpunch

    pause 1.0

    play sound2 s_punch

    guard "Damn you! Everyone, get her!" with vpunch

    play sound s_dodge

    pause 0.3

    play sound2 s_dodge

    pause 0.6

    play sound3 s_punch

    roz "There! I've got you..." with vpunch

    play sound s_crunch
    pause 0.4
    play sound2 s_wscream

    roz "HAAA!!! She bit me!!! That bitch!!!" with vpunch

    "Roz is a big guy, but it genuinely sounded like he was about to cry."

    play sound s_door

    "Maya opens the door and yells."

    maya "What the hell is going on down there???" with vpunch

    "You hear Roz's voice coming from the lower floor."

    roz "Maya, we've captured a spy! Shit, what a fury... Tie her up and bring her to the captain upstairs!"

    roz "AND DON'T LET HER OUT OF YOUR SIGHT FOR EVEN ONE MINUTE!"

    show maya disarmed flip at left with move

    show guard at right:
        ypos 1.05
    with dissolve

    guard "Captain! We have intercepted a spy as she was trying to reach your quarters."

    "The guard shoves a bound woman down on the suite floor."

    with vpunch

    show renza at center:
        zoom 0.85

    with dissolve

    renza "Let me go, you brute! I'm just an admirer of the captain... I wanted to pay my respects..."

    "She gives you and Maya an ingenuous look."

    maya "Humph..."

    "She turns to the guard."

    maya "Leave us."

    guard "But, Captain, Roz said..."

    maya "I said, 'Leave us'! She's tied up, what do you think is gonna happen? Get out." with vpunch

    guard "Yes, my Lady."

    hide guard with dissolve

    show renza at right with move

    maya "Renza, I presume?"

    renza "Ah... So you know my name? [MC.name] ratted me out, didn't he."

    you "I didn't."

    maya "No, he didn't have to... I've been conducting my own inquiry into the thieves guild for a long time, and I have a whole file
          on its infamous leader: Renza the Black."

    renza "Well, I'm flattered. And I suppose I should be grateful that [MC.name] didn't betray me all the way."

    "Maya scoffs."

    maya "Betray you? Oh, come on... You're going to make us cry. Surely as a thief, you didn't expect people
          to behave any differently than you always do?"

    renza "It's not like that!" with vpunch

    "Renza looks genuinely hurt."

    renza "I lowered my guard around [MC.name], that was silly, I know. I shouldn't have."

    renza "In fact, I wanted to have a word with him... That's why I came here."

    maya "A word with him! In the middle of a guard tower! That's rich."

    renza "Come on, Captain. You have me cornered. I only request a moment with [MC.name]."

    maya "Ha! You're under arrest in my own house, and I don't think I need to agree to any of your 'requests'."

    renza "But without me and my guild, you wouldn't be sitting where you are right now... At this very moment, you would be shining Farah's
           new pair of boots or something..."

    maya "Careful, Renza... *hiss*"

    you "Look, Maya, she's got a point..."

    renza "I'm only asking for a moment of privacy here. Compared to what I did for you, even unwillingly, it's a very small favor. Are you so dishonorable as to deny
           me this harmless request?"

    maya "Dishonorable?" with vpunch

    "Maya's face reddens. She hates to have her honor questioned. You can tell Renza is playing on her weakness."

    maya "Hmph! Fine! You have 5 minutes with your boyfriend. Then, I'll have you locked up in the darkest cell until I interrogate you myself."

    renza "Fine."

    "Maya turns towards you."

    maya "And YOU, [MC.name]. Don't make any trouble, you hear me?"

    you "S... Sure."

    hide maya with dissolve

    ""

    you "So... You came all the way here just to talk to me. I'm impressed."

    renza "Come on, don't flatter yourself, [MC.name]. I really came here to scout the captain's vault. I thought the party was a perfect occasion to infiltrate...
           Until I ran into this big, dumb guy."

    renza "Well, he's fast for his size, I'll give him that!"

    you "I've got bad news for you. The vault is empty now. Maya has already sent the gold away to improve life for people in the slums."

    renza "What?" with vpunch

    renza "Damn that tomboy do-gooder! She really did her best to foil all of my plans. And you, [MC.name]..."

    you "Oh come on, Renza, don't lecture me. I couldn't just let you take over the slums."

    you "People have had enough being robbed and threatened.
         Maya will help them. The slums and its inhabitants will be better for it."

    "Renza looks bitter."

    renza "Just my luck. I had to run into the one bleeding-heart pimp in the whole of Xeros!"

    you "Maya told me your people made it out before she raided the thieves guild. You haven't lost everything."

    renza "Ha! Did you think the thieves guild was that weak? Even if I fall, others will be lining up to take my place."

    "She lowers her voice."

    renza "But listen, [MC.name]. I'm not eager to end up locked in Maya's prison. I helped you, so you owe me."

    renza "Help me get out of here."

    you "What???" with vpunch

    renza "Please, [MC.name], pretty please? I helped you a great deal, then you wronged me. Ruined months of planning.
           Sent the poor Lydie to a dank cell, you did! Are you also going to send me to rot in jail until I'm old and grey?"

    you "But..."

    renza "If you help me now, I'll call us even. I'll even let you visit the thieves guild, for old times sake, in spite of all that happened.
           Clean slate. Think about it."

    you "..."

    menu:
        you "..."

        "Help her":
            $ renpy.block_rollback()
            you "Well, I suppose I owe you for trashing up your plans. But don't go backstabbing me for my trouble later on, okay?"

            play sound s_laugh

            renza "No, I won't. Thank you, [MC.name]. You're a gentleman."

            you "I don't know what the hell I am doing..."

            "You untie the bounds around Renza's arms and legs."

            renza "Thanks."

            play sound s_sheath

            "In a flash, Renza takes out her dagger and holds it to your throat." with vpunch

            you "Hey!!! I though we said, 'no backstabbing'!"

            renza "Well, technically this isn't your back..."

            "The cold blade feels chilling against your throat. Beads of sweat form on your forehead."

            you "Listen, Renza..."

            play sound s_punch

            with vpunch

            pause 0.5

            "Using the hilt of her dagger, Renza viciously punches you in the nose."

            you "Ouch! What was that for!"

            play sound s_evil_laugh

            "You hold your bloody nose as Renza sheathes her dagger, laughing."

            renza "That... was the price for betraying me. Also, this is your cover story, for when the guards break in."

            "Blowing you a kiss, she leaps to the nearest window and leans through it."

            play sound s_dodge

            hide renza with dissolve

            "Nursing your bleeding nose, you begrudgingly admire her fearlessness as she disappears from your sight,
             climbing her way down in spite of the heights."

            you "That Renza... She's a fierce one."

            play sound s_door

            show maya with dissolve

            play sound2 s_surprise

            maya "[MC.name]! What the hell happened... Where is Renza???"

            "She takes in the whole scene: the open window, the untied ropes on the floor, your bleeding face... She gives you a furious look."

            you "Look, she managed to free herself and attack me. I couldn't do anything..."

            maya "Oh, save it! *mad*" with vpunch

            maya "Men, stop partying and form a patrol! Go after her, all of you!"

            maya "Damn you, [MC.name]... I thought I could trust you!"

            hide maya with dissolve

            scene black with fade

            "You've managed to salvage a bit of your reputation with Renza and the thieves guild. Your reputation with the city guard has been damaged, however."

            $ thieves_guild.action = True
            $ NPC_renza.love += 10
            $ NPC_maya.love -= 15


        "Don't help her":
            $ renpy.block_rollback()
            you "Sorry Renza. I'll sleep better knowing you're behind bars."

            play sound s_scream

            renza "What! Fuck you, you bastard! I'll get you!" with vpunch

            play sound s_door

            show maya disarmed flip at left with dissolve

            maya "Come on, Renza, I thought you wanted a friendly talk..."

            play sound s_scream_loud

            renza "Damn you, [MC.name]! Damn you all to hell!!!" with vpunch

            maya "Mmmh... It looks like your little chat didn't go as well as you had planned. Men, take her."

            play sound s_screams

            renza "Arrrh!!!"

            hide renza with dissolve

            maya "I'm happy to see that you are not too cosy with the thieves, [MC.name]. Keep on walking in the light, and Arios will wash away your sins."

            scene black with fade

            "Your reputation with the city guard has increased. However, you have lost access to the thieves guild for good."

            $ NPC_renza.love += -25
            $ NPC_maya.love += 10

    play sound s_chimes
    $ NPC_maya.unlock_trainer()

    call c1_captain_fate from _call_c1_captain_fate

    return


label c1_ending_lieutenant:

    play music m_disco fadein 3.0

    scene black with fade

    show bg camp night at top with dissolve

    show guard party as guard1 at totheright with dissolve

    show guard party as guard2 at totheleft with dissolve

    guard "Hey! If it isn't [MC.name]. Came here to celebrate with us?"

    "You recognize many faces around the camp. You have seen those men hanging around the thieves guild. Even though they are now wearing
     guard uniforms, they look out of place somehow."

    you "Evening. I'm looking for lieuten... I mean, captain Lydie."

    guard "She's up in the captain suite, sampling some of Farah's fancy champagne reserve, no doubt!"

    you "Thanks."

    stop music fadeout 2.0

    scene black with fade

    show bg captain_office at top with dissolve

    play music m_knights fadein 3.0

    play sound s_knocks

    lieutenant "Yes?"

    show lieutenant:
        ypos 0.3
    with dissolve

    you "It's me."

    lieutenant "Oh, [MC.name]! How lovely of you to pay me a visit."

    lieutenant "I've just moved into my new quarters... And I must say, I love them!"

    you "It looks like you haven't changed the layout of the place much."

    lieutenant "Oh, but I won't! Farah was a jerk, but she knew how to enjoy the finer things in life. Now, it's going to be my turn..."

    lieutenant "Here, taste some of this wonderful champagne."

    "She hands you a crystal glass. You notice that the bottle is nearly empty already. Looks like she got a head start."

    you "Having fun by yourself?"

    lieutenant "I was, [MC.name]! But to tell you the truth, I am grateful for the company."

    lieutenant "You don't know how stressful the last few days were for me... Everything was hanging by a thread... But now that our triumph is complete,
                it's time to party!"

    you "Don't you have a lot on your mind though? Running the Guard is not going to be easy..."

    lieutenant "Oh, don't spoil the mood, [MC.name]. Most things will go on just like they did before."

    lieutenant "Most of the guards working under Farah I've been able to turn immediately. I've already got rid of the few troublesome elements
                I couldn't control, like this annoying blue-haired bitch and her bullheaded lapdog. Good riddance!"

    lieutenant "Things will work a lot more smoothly for the thieves guild now... We will benefit enormously from this new deal!"

    lieutenant "We're the only game in town now. Outside of the noble and royal quarters, of course."

    you "Why not there?"

    lieutenant "Don't you know? Those districts are outside the Guard's jurisdiction. The blue bloods prefer to keep the commoners at arm's length."

    you "I see... That sucks. I had a mind to settle there myself."

    lieutenant "I can only get you a license for the city. Rest assured, my friend, you will have it first thing in the morning.
                You more than deserved it. Also, here is your gold. I'm sure you'll be happy to have it back."

    play sound s_gold
    $ MC.gold += blist[2].cost

    "You have received [game.goals[0].value] gold."

    you "Thank you. After all I've been through, I was hoping for a little more..."

    play sound s_kind_laugh

    lieutenant "How greedy of you!"

    lieutenant "Well, I can't spare any more gold right now, but I can make sure to reward you in a more... personal way."

    "She gives you a playful look."

    you "Oh, really? What did you have in mind?"

    lieutenant "Did I tell you that the good captain had a queen-size bed with a giant dodo feather mattress? It's ridiculously comfortable..."

    you "Oh, really... Why don't you show me?"

    "Giving you an inviting smile, she takes you by the hand."

    lieutenant "Follow me..."

    scene black with fade

    show bg lieutenant sex1 at top with dissolve

    "You spent an enjoyable night in the company of Lydie, helping her relax after this eventful day."

    play sound s_kind_laugh

    lieutenant "Oh, [MC.name]... Do you like my little massage... *laugh*"

    play sound2 s_sucking

    "The captain rubs her tits alongside your body, while tugging on your hard cock."

    lieutenant "I feel something coming..."

    play sound s_surprise

    with flash

    scene black with fade

    pause 1.0

    show bg lieutenant sex2 at top with dissolve

    play sound s_moans

    "Hours later, you are still playing with Lydie, enjoying her fit body in a variety of positions."

    play sound s_laugh

    lieutenant "Aw, [MC.name]... Look at the mess you've made... *laugh*"

    "She licks her lips sexily."

    play sound2 s_ahaa

    lieutenant "Oh, [MC.name]..."

    "Spreading her legs to give you a good look of her gaping pussy, she pleads with her eyes for a good fucking."

    play sound s_mmmh

    lieutenant "I hope you're ready for another round..."

    scene black with fade

    "You leave in the early hours of the morning, after a night of wild sex."

    "You are now a distinguished friend of the thieves guild."

    $ NPC_lieutenant.love += 25
    $ MC.change_prestige(2)

    play sound s_chimes
    $ NPC_lieutenant.unlock_trainer()
    $ unlock_achievement("h lydie")

    call c1_captain_fate from _call_c1_captain_fate_1

    return

label c1_ending_captain:

    stop music fadeout 3.0

    scene black with fade

    show bg camp night at top with dissolve

    show guard at center with dissolve

    play music m_wind

    pause 1.0

    guard "Hey, you!" with vpunch

    guard "What do you think you're doing in the Guard camp so late?"

    you "Well, I..."

    show guard as guard2 at centerleft:
            zoom 0.9
    with dissolve

    "Second guard" "Leave him alone, man. He's with the captain."

    guard "He's... What?"

    "Second guard" "He's a guest, coming to see the captain. She told us he was coming. Let him pass, or she'll get you flogged for your trouble."

    guard "Oh."

    guard "I'm awfully sorry, sir, please forgive my rudeness."

    you "Ha! That's more like it. Take me to the captain quarters."

    guard "Yes Sir."

    you "And move it. I don't have all day."

    guard "..."

    guard "Yes Sir."

    hide guard with dissolve

    show guard as guard2 at truecenter with ease:
        zoom 0.9

    pause 1.0

    "Second guard" "Damn lucky bastard... Being summoned to the captain's chambers at this late hour, there can only be one reason..."

    hide guard2 with dissolve

    play music m_knights

    scene black with fade

    show bg captain_office at top with dissolve

    play sound s_knocks

    pause 1.0

    captain "Ah, [MC.name]. I've been expecting you."

    you "My lady."

    show captain with dissolve

    captain "I was anxious... you wouldn't show up."

    you "Well, here I am."

    captain "Yes. Please, sit down. The couch is very comfy. Want a drink?"

    you "Err, well, I'm fine..."

    captain "Please! Drink with me."

    "She hands you a glass of wine. You look at the beverage suspiciously."

    captain "You pulled quite a number on me today... For a second I thought I had lost everything."

    you "..."

    play sound s_laugh

    captain "It was quite a thrill, actually, let me tell you! I had forgotten what it was like to be on edge, having to do anything to survive."

    you "You almost sound like you were enjoying yourself..."

    captain "No, in fact I was rather hysterical... But danger is exciting... And now that we have successfully resolved this situation, I feel great."

    you "I was only doing what I had to do to get my money back..."

    captain "Of course you did. I don't blame you... But you've made the right choice in the end."

    "Her cold voice reflects an unmistakable threat. You toy nervously with your glass, trying to think of an excuse not to drink."

    captain "Here, have this! A first token of good will."

    play sound s_gold

    "She throws you a purse full of gold."

    captain "That should compensate you for the gold you lost."

    "You have received [game.goals[0].value] gold."

    $ MC.gold += blist[2].cost

    captain "You'll be happy to know that I haven't wasted time since this morning, [MC.name]..."

    you "How so?"

    captain "I left our friend the lieutenant at the hands of my most competent interrogators..."

    captain "Eventually, she talked... Or squealed, rather."

    captain "She gave us the location of the thieves guild and the identity of their leader... The woman called Renza."

    you "Ah, yes... I've heard of her."

    captain "I couldn't take any chances, so I had my men set fire to their hideout and the whole neighboring block of houses... Smoked the rats right out!"

    play sound s_evil_laugh

    captain "Many died in the fire, and we cut down the few that tried to escape."

    captain "The thieves guild is no more."

    captain "My sources say that Renza might have made it out, taking the first ship out of town, but it's only a matter of time before I learn of her whereabouts..."

    you "Wow... I'm happy there's no bad blood left between us, Farah."

    captain "Of course there isn't, my dear... Thanks to you, I got rid of a whole bag of snakes in one fell swoop. There's no one left to oppose me on this side of town."

    you "And on the other side?"

    captain "Well, the city guard still doesn't have jurisdiction over the noble and royal quarters of Zan, of course... Those stuck-up aristocrats don't want us around, on account of us being low-born commoners."

    "She looks frustrated."

    captain "But I'm a thousand times more deserving than all those snotty rich brats and bitchy princesses! I had to steal and murder my way to the top,
             I didn't get it all handed out to me because of my pedigree..."

    you "Yeah, you're something else..."

    captain "Did you know that I started out a slave in a military brothel when I was a teenager? I had to ruthlessly climb my way up the power ladder..."

    you "Wow, really? I'm impressed..."

    captain "And I'm not done yet. I aim for a ladyship, to show those pretentious assholes I can be one of them."

    you "That looks like an easier step than what you've already been through."

    play sound s_laugh

    captain "Anyway, [MC.name]. Let us drink together. To riches and wealth! To the death of our enemies!"

    "You raise your glass nervously, worried that she might have poisoned the wine."

    you "*sweat*"

    captain "Cheers!"

    "She drinks her glass in one go, then looks at you like a hungry she-wolf, licking her lips."

    you "*gulp*"

    "You take a sip of the fancy wine. Its fire warms your belly, but you detect no unpleasant taste."

    captain "I made the arrangement for your brothel license to be delivered tomorrow. You see, I abide by our deal..."

    "You start feeling a little feverish."

    captain "This will only allow you to operate in the commoner districts, however... To make it to the noble or royal quarters, I'm afraid
             you'll have to screw a princess or two."

    "You feel a strong fire growing in your belly. Something is wrong..."

    play sound s_laugh

    captain "What's the matter, [MC.name]? Are you not enjoying your wine?"

    you "You... You poisoned me..."

    play sound s_evil_laugh

    captain "I did spike your drink a little, [MC.name]..."

    you "You..." with vpunch

    play sound s_sigh

    captain "But poison? No, my dear [MC.name], it's not poison... I have something else in mind entirely."

    "Your entire body feels burning hot. You feel extremely light-headed, but also bursting with wild energy."

    you "Wh... What's happening to me?"

    "Surprisingly, your dick is sticking up and feels rock-hard. It even seems to grow larger than usual."

    captain "The wine is spiked with a powerful aphrodisiac used for breaking slave minds in the Blood Islands... I had some too, just for the fun of it."

    play sound s_ahaa

    captain "You didn't forget our little promise, did you? I have big plans for us tonight..."

    "She leans against you, pressing her large tits against your chest."

    captain "Here, finish your glass..."

    play sound s_mmmh

    "She whispers seductively in your ear as she pours the rest of the glass into your mouth."

    scene black with fade

    show bg captain sex3 at top with dissolve

    play sound s_laugh

    captain "Oh, my... This spice is known to make any cock larger, but you must naturally be quite well-endowed to become this huge..."

    "You can feel your cock throbbing and burning as she saddles you and presses her hot pussy on top of it."

    you "It's burning... What did you give me..."

    "Her skin is truly perfectly smooth and soft, making the touch of her hot body a heavenly feeling."

    "The excitement is almost too much to bear as she starts grinding your cock with her wet slit."

    captain "Normally, a few drops are enough... But I'm afraid I used the whole vial!"

    "Your cock and your balls hurt as you feel a tremendous build-up."

    captain "There's no way around it, you're going to have to release it all inside to get relief... Maybe seven, eight times, at a bare minimum..."

    play sound s_laugh

    captain "With this much serum inside you, we should be able to play all night... Don't expect to get any sleep!"

    you "Aw... You succubus..."

    "She purrs."

    captain "I'm gonna show you some of the tricks I learned when I was a sex slave... I was one of the best, you know..."

    "Her enormous boobs jiggle as she raises her hips, placing the tip of your cock against her wet hole."

    play sound s_scream

    captain "Aaaah!!!" with vpunch

    "Lowering her hips, she engulfs your throbbing cock deep into her moist pussy. Her tight vagina spreads little by little
     to accommodate your abnormally large cock."

    play sound s_moans

    captain "Oh, this is so good... It's like I'm fucking a horse..."

    "You moan as she starts riding you, your burning cock slamming in and out of her."

    play sound s_scream

    captain "Yes! Fuck me, [MC.name]! Make me a slave to your cock!"

    "Her bouncing boobs have a hypnotic effect on you as she keeps bouncing on your cock and talking dirty."

    play sound s_orgasm_fast

    captain "Oh, yes!!! Haaa, haaa!!!" with vpunch

    "A strong orgasm washes over her as you pound her cervix with all you've got."

    "The aphrodisiac is making you so horny that you can't even remember your own name."

    play sound s_mmmh

    captain "Oh, keep going, I'm gonna have another one!" with vpunch

    "The captain is truly a hungry slut. She bounces on and off your cock, shoving it ever deeper inside her with every move."

    "She seems to enjoy herself tremendously as she rides you to her climax."

    play sound s_scream

    captain "I'm coming again!"

    play sound s_orgasm_fast

    captain "Aaaaah!!!" with vpunch

    "Her pussy contracts around your pulsating cock, sending you right over the edge."

    you "Ohhh!!!" with vpunch

    show bg captain sex4 at top with flash

    play sound s_orgasm_fast

    captain "Yessss!!!" with doubleflash

    "You shoot an enormous amount of cum into her ready pussy, rocking her with a massive third orgasm."

    captain "Oh... I'm so full..."

    with flash

    you "Wh... What's happening?"

    with doubleflash

    you "It won't... It won't stop... Haaa!"

    with flash

    play sound s_screams

    captain "It's a side effect... Ahaaa! Of... the drug... Oooh!!!"

    "You keep cumming and cumming into her hot cunt, until you cannot take it anymore. You then rip your cock out, but it keeps spurting loads of cum on her
     white body." with flash

    play sound s_orgasm

    captain "Keep going, [MC.name]! Shoot it all over me, ahaaaa!!!"

    with doubleflash

    "She climaxes again as you shoot more cum on her boobs and belly. Looks like the rumors about the captain being a nymphomaniac aren't exaggerated
     after all..."

    captain "Aw... It was so good... And we're only getting started!"

    you "*sweat*"

    scene black with fade

    pause 1.0

    show bg captain sex4 at top with fade

    "You keep fucking the captain in all possible positions until the sun rises."

    play sound s_screams

    captain "Oh, [MC.name]... Oooh!!!"

    "You lost count of how many times you both came, but it must be some kind of record."

    $ unlock_achievement("h farah")

    play sound s_scream_loud

    scene black with fade

    show bg camp night at top

    "When the morning comes and Farah finally decides to let you go, you don't have a drop of liquid left in your body."

    "You stumble your way back to the brothel, looking more dead than alive. Then you sleep all day to recover."

    scene black with fade

    "You are now an ally of the city guard."

    $ NPC_captain.love += 5
    $ MC.change_prestige(2)


    play sound s_chimes
    $ NPC_captain.unlock_trainer()


    return

label c1_captain_fate:

    play music m_evil fadein 3.0

    scene black with fade

    "Meanwhile, deep down inside the dungeons of Zan's infamous Xotar prison."

    show bg cell at top with dissolve

    play sound s_mmmh

    captain "Mmmmh... Ngggh..."

    guard "That's right, Captain Slutface... Massage my cock with your hungry pussy..."

    show captain sex1 at top with dissolve

    play sound s_moans

    guard "I love to squeeze your big slutty tits while I fuck you bareback..."

    play sound s_scream

    with hpunch

    captain "Aah!!!"

    "Young guard" "Come on, bro... It's my turn!"

    guard "Shut up, kid! You're ruining the mood!"

    "Young guard" "You've been using her for half an hour already... Let me join in on the fun!"

    guard "No! I told you to keep watch."

    "Young guard" "Aw, it's unfair... I've also been dying to fuck that whore captain since the first day she ordered me to do her chores...
                   The bitch had me lashed for spilling one of her expensive skin products."

    guard "Wait for your turn... Just give me a minute... Mmmh..."

    play sound2 s_scream

    captain "Oh, aah!" with hpunch

    "Young guard" "I see a light down the corridor! Someone is coming! Hurry, bro..."

    guard "I'm almost there..."

    play sound s_scream_loud

    captain "Aaah!" with hpunch

    guard "Take that, you filthy whore!"

    with flash

    "The guard grunts noisily as he releases it all into Farah's tight pussy."

    with hpunch

    play sound s_screams

    show captain sex2 at top with doubleflash

    captain "Nghh!!! Aaah!!!"

    guard "Aaaaah..."

    "Young guard" "Pull yourself together, man! Hide her in the back! They're coming!"

    hide captain with fade

    play sound s_knocks

    ""

    show guard as guard1 at totheright with dissolve
    show guard as guard2 at totheleft with dissolve


    "Young guard" "Y... Yes! Just a minute."

    play sound s_door

    pause 2.0

    guard "Hey, you... Come out of the dark."

    play sound s_dodge

    "Young guard" "What? Wh... Who are you???"

    with flash

    play sound2 s_sheath

    with vpunch

    play sound s_wscream

    hide guard1 with pixellate

    "Older guard" "Stand back!!! Don't come near me!!! NOOO!!!"

    with flash

    play sound s_sheath

    with vpunch

    pause 0.1

    play sound2 s_sheath

    with vpunch

    play sound s_wscream

    hide guard2 with pixellate

    ""

    captain "What... What is going on?"

    captain "Who... Who is it???" with vpunch

    "Voice" "Farah... You have disappointed me deeply, my child."

    captain "It's {b}you{/b}!!! No, listen... I didn't say anything, I swear!!! Please, I won't tell anything to anyone!!! You must believe me!"

    "Voice" "Oh, I believe you... *dark laugh*"

    play sound2 s_woman_scream

    scene black with fade

    play sound s_sheath

    pause 0.5

    play sound2 s_sheath

    pause 0.2

    play sound3 s_sheath

    with flash

    return

label c1_judge_fate:

    stop music fadeout 3.0

    pause 2.0

    play music m_wind fadein 3.0

    scene black with fade

    show bg street night at top with dissolve

    "In the streets of the inner city, late at night."

    show judge at right with dissolve

    "The streets are dark and deserted. The judge is pacing back and forth, waiting for someone."

    judge "Damn this stupid informant... I'm not going to wait here all night."

    judge "..."

    judge "This is a waste of time. No one is coming."

    play sound s_shatter

    with vpunch

    "The judge is startled by a sudden noise."

    judge "Wh... What was that???"

    play sound2 s_meow

    pause 1.0

    judge "Humph. It's just a cat."

    judge "I've had enough. No one is coming at this stupid meeting. I'll just go home."

    "Turning around, the judge hides his face in his burnous. He starts heading towards the noble quarter."

    play sound s_mystery

    ""

    judge "Who's... Who's there?"

    mask unknown "..."

    "The judge starts walking faster, looking nervously over his shoulder."

    play sound s_chimes

    with fade

    "The judge breathes a sigh of relief as he sees the bright lights of the noble quarter, just a block away."

    judge "I swear, I'm getting old. I'm being spooked by nothing."

    play sound s_mystery

    pause 1.0

    mask "Nothing..." with vpunch

#    play sound2 s_wscream

    judge "HAAA!!!" with vpunch

    judge "Who... Who's there??? *trembling*"

    play sound s_mystery

    pause 1.0

    mask "No one... Or... Perhaps... You hear the souls of those you murdered, yearning for revenge..."

    judge "This is not funny! I am a high judge of the royal court! Leave now, or I shall call the Guard on you..."

    mask "..."

    "The wind blows through the empty street, sending shivers down the judge's spine. Eery silence answers his panicked call."

    judge "You're g-gone now... G-Good. And d-don't come back."

    "Running now, the judge presses for the safety of the noble district."

    play sound s_steps

    pause 1.0

    judge "*pant*, *pant*..."

    play sound s_mystery

    mask "What's the hurry, traitor?"

    play sound2 s_wscream

    judge "HAAAA!!!" with vpunch

    "The judge looks everywhere around him, his heart beating wild with panic."

    judge "Where... Where are you??? Sh... Show yourself!"

    mask "..."

    play sound s_mystery

    mask "BEHIND YOU."

    play sound2 s_crash

    show bg murder at top with dissolve

    play sound3 s_sheath

    with hpunch

    pause 0.5

    play sound2 s_wscream

    judge "AAAARRRRRH!!!"

    play sound s_sheath

    with flash
    hide judge with pixellate

    pause 1.0

    play sound s_crash

    show bg street night with dissolve

    pause 1.0

    stop music fadeout 3.0

    scene black with fade

    return


#### END OF CHAPTER 1 STORY EVENTS ####
