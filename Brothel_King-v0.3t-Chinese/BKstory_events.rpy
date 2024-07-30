##### GENERIC STORY EVENTS (NOT CHAPTER-SPECIFIC) #####

## StoryEvent condition functions

init -2 python:

    def is_first_tuesday():
        if calendar.day <= 7 and calendar.get_weekday() == "Tuesday":
            return True
        return False


## HMAS

label hmas:

    $ renpy.block_rollback()

    stop music fadeout 2.0

    scene black with fade

    play sound s_chimes
    pause 0.2
    play sound2 s_chimes
    pause 0.2
    play sound3 s_chimes

    "One magical winter night..."

    "Loud voice" "HO HO HO..."

    "You wake up from your sleep with a jolt."

    you "Uh? Did someone say 'Hoes'?"

    "Looking around you, you find nothing out of place in your room. Sill is sleeping naked on her cot at the foot of your bed, exhausted after the vicious
     pounding you gave her last night."

    you "Did I just dream this? It sounded so... strange..."

    "Unable to go back to sleep, you get up and go down to the main hall."

    if brothel.get_common_rooms():
        $ room = brothel.get_random_room_pic_path()
    else:
        $ room = "black"

    $ renpy.show(room, at_list = [top])
    with dissolve

    "Nothing is moving in the sleepy brothel. All your girls are fast asleep, exhausted by the hard work they had to pull last night."

    play sound s_creak

    "Suddenly, you hear some noise coming from the maintenance room."

    you "This is strange... That room is locked, and there is no other entrance... Except maybe the old chimney?"

    "Opening the door as silently as you can with your spare key, you prepare to confront the intruder."

    you "Whoever is in here... Show yourself!"

    play sound s_door

    scene black with fade

    show bg hmas1 at top with dissolve

    play sound s_spell



    if story_flags["seen_hmas"] == 1:

        hmas_girl "Hi, [MC.name]..."

        "You recognize the strange girl from last year."

        you "Oh, it's you again..."

        hmas_girl "I've come to see you with a new present..."

        you "Really? What is it?"

        play sound s_laugh

        if MC.get_alignment() == "good":
            hmas_girl "You're such a good boy... So you deserve something new."

        elif MC.get_alignment() == "neutral":
            hmas_girl "You're a greedy one aren't you... So I'm sure you cannot be satisfied with just one hole..."

        elif MC.get_alignment() == "evil":
            hmas_girl "You're such a naughty boy... I'm sure you've thought about taking things to the next level."

        hmas_girl "So this time, I want you to fuck my ass..."

        you "*gulp*"

        "She reaches inside your pants, cupping your balls in her warm, soft hands."

        hmas_girl "I'm sure you're ready for this... Aren't you?"

        call hmas_sex("anal") from _call_hmas_sex

        $ story_flags["seen_hmas"] = 2

    elif story_flags["seen_hmas"] == 2:

        hmas_girl "[MC.name]... I was waiting for you..."

        "You had a feeling it would be her."

        hmas_girl "I'm already so wet... What are you waiting for..."

        "She reaches into your pants with both hands, rubbing and massaging your shaft. You get rock-hard in no time."

        hmas_girl "How do you want your present this year, {nw}"

        if MC.get_alignment() == "good":
            extend "my sweet boy?"

        elif MC.get_alignment() == "neutral":
            extend "working boy?"

        elif MC.get_alignment() == "evil":
            extend "naughty boy?"

        menu:
            "Choose your present"

            "干她的小穴":
                call hmas_sex("sex") from _call_hmas_sex_1

            "干她的菊穴":
                call hmas_sex("anal") from _call_hmas_sex_2

    else:
        "You are stunned to see an unknown lady changing inside the maintenance room."

        hmas_girl "Ah, you arrive just in time. Help me button this up, will you?"

        "The girl is young and beautiful. She wears a strange and sexy costume that leaves little to the imagination."

        you "*gulp*"

        "She has long, sharp ears, which place her as an elf or a member of the fairy people. However, you also notice that she has... horns. That's definitely
         not an elven feature."

        you "Wh... Who are you? How do you know me?"

        hmas_girl "Me? I am your present!"

        you "My... Present?"

        hmas_girl "Yes... I am a gift from the winter father."

        you "The winter father?"

        hmas_girl "Yes... He's been watching you all year, trying to find the right present."

        if MC.get_alignment() == "good":
            hmas_girl "You've been a very good boy this year... So I am your reward."

        elif MC.get_alignment() == "neutral":
            hmas_girl "You've been very busy this year. All work and no play makes [MC.name] a dull boy... So why don't you play with me?"

        elif MC.get_alignment() == "evil":
            hmas_girl "I heard you've been a very naughty boy... That's what I like about you."

        "Before you have time to object, she grabs your hand and places it on her breast."

        hmas_girl "Look, give it a try... Doesn't it feel nice? *squeeze*"

        you "*sweat*"

        hmas_girl "Here, pinch my nipple gently..."

        play sound s_aah

        hmas_girl "Ahaa... That's so good."

        "Her hand reaches for your crotch. She starts caressing your cock through the fabric of your pants."

        play sound s_mmmh

        hmas_girl "Hmmm, you're so hard already..."

        "She tugs at her skimpy costume, showing you her pink, erect nipples."

        hmas_girl "Come here, [MC.name]... Let me give you your present."

        call hmas_sex("sex") from _call_hmas_sex_3

        $ story_flags["seen_hmas"] = 1

    scene black with fade

    $ MC.change_prestige(5)

    "You wake up in your bed, alone. It's late morning already."

    "Was that all a dream?"

    play sound s_chimes

    $ calendar.set_alarm(calendar.time + 336, Event(label = "hmas"))
    $ unlock_achievement("hmas")

    return

label hmas_sex(act):

    $ renpy.block_rollback()

    show bg hmas2 at top with fade

    "Wasting no time, you shove her skimpy clothes aside to expose her ample breasts and tight holes."

    play sound s_surprise

    hmas_girl "Oh!" with vpunch

    hmas_girl "You're forceful... I like that..."

    play sound s_mmmh

    hmas_girl "Rub this hard dick of yours... Mmmmh... On my pussy..."

    play sound s_sucking

    "Her juices start to leak out as you slowly rub your shaft along her soft slit."

    you "You're already wet..."

    "You play with her ass and tits, squeezing them hard and enjoying her little cries of ecstasy as you do."

    play sound s_moans

    hmas_girl "Oh, [MC.name]..."

    if act == "anal":
        "Raising her leg higher, you poke the entrance of her tiny anus with your burning hard dick."

    elif act == "sex":
        "Her pussy lips spread nicely as she gets wetter and wetter with your every thrust."

    "She relishes the feeling of your hands as you continue fondling her private parts."

    play sound s_aah

    hmas_girl "[MC.name]... It's time..."

    if act == "sex":

        show bg hmas sex1 with fade

        "Your dick slides deep into her wet pussy in one smooth shove, well lubed with the hot juices that continue to pour out of her."

        play sound s_aaha

        hmas_girl "Aaaha..."

        "Giving her no time to rest, you forcefully pump in and out of her eager cunt, holding her in place with a hand on her ass,
         the other digging in her breast."

        play sound s_moans_short

        hmas_girl "Ooh... Aaah..." with hpunch

        you "This is... the best... present ever..."

        hmas_girl "Oh, [MC.name]... Fuck your present girl..."

        play sound s_scream

        hmas_girl "Aaah! Do me harder!!!" with hpunch

        "Fulfilling her wish, you push her against a wall, slamming your dick in and out of her with abandon."

        play sound s_moans

        hmas_girl "Yes! Oh, yes!!!" with hpunch

        "The harder you fuck her, the more excited she gets. She fondles her own ass hard with one hand, holding on to you with the other."

        play sound s_scream_loud

        hmas_girl "Ooooh!" with hpunch

        "She stares into your eyes with a look of rapture on her face."

        hmas_girl "Are you... Ooh! Are you going... to cum?"

        play sound s_scream

        hmas_girl "I'm... almost... there..." with hpunch

        you "Oooh..."

        with flash

        play sound s_scream_loud

        hmas_girl "HAAAAA!!!"

        play sound s_orgasm

        show bg hmas sex2 at top with doubleflash

        "You release a flood of semen into her tight pussy. She screams in ecstasy as you fill her up with your warm cum."

    elif act == "anal":

        show bg hmas anal1 with fade

        "She cannot hold her scream as you penetrate her tight butthole."

        play sound s_scream

        hmas_girl "Haaa!" with vpunch

        "Her asshole is tight but somewhat elastic, and it enlarges to accommodate the width of your cock."

        "The girl might not be one of the elf people, but she seems to share their infamous sex drive."

        play sound s_aah

        hmas_girl "It's going deep inside me... So deep..."

        "Her juices keep leaking out and lubricating your dick as you start pumping in and out of her ass."

        play sound s_ahaa

        hmas_girl "Oooh... I feel strange..."

        "You try to go slowly at first, but the pleasure from fucking her tight ass is so intense that you can't hold your measured pace much longer."

        play sound s_moans_short

        hmas_girl "Aaah! You're fucking me so deep! Aaaah!!!" with vpunch

        "Every time you slam your hard dick into her asshole, you also rub along the length of her pussy. You can feel her slowly losing her mind over
         the sensation."

        play sound s_moans

        hmas_girl "Your dick... is in my ass... Aaaah! And it's rubbing me... Ooooh!!!"

        "Grabbing her ass harder, you sink your fingers into her soft flesh. You caress the rim of her anus while continuing to pump in and out of her."

        play sound s_scream

        hmas_girl "This is so good! So good!!! Aaaah! I'm..."

        with flash

        play sound s_scream_loud

        "She cums hard as you push your cock all the way into her ass."

        play sound s_orgasm

        with doubleflash

        show bg hmas anal2 with dissolve

        "Her tight asshole twitching around your dick sends you over the edge. You shoot a load of warm cum into her welcoming butt."

    play sound s_mmmh

    hmas_girl "Oh... [MC.name]... It was so good..."

    "The girl watches with fascination as your cum drips out of her."

    hmas_girl "You really filled me up to the brim, didn't you..."

    play sound s_laugh

    "Scooping semen out of her hole with her fingers, she hungrily laps it up."

    hmas_girl "Ah... Delicious... I love the taste of warm cum..."

    play sound s_sucking

    "Dropping to her knees, she starts licking and sucking the last drops of cum out of your throbbing dick."

    play sound2 s_mmmh

    hmas_girl "Sho good... Hmmm..."

    "When she is finished, she looks up at you with a mischievous smile."

    stop sound

    hmas_girl "I'll see you next year, naughty boy..."

    play sound s_laugh

    return


## Renza events ##

label renza_friend1: # L >= 5 and dice(6) = 6

    renza "Oh, hi, [MC.name]! Seems like you've been coming here often. I'm beginning to think you have a crush on me. *wink*"

    menu:

        "确实如此":

            $ renpy.block_rollback()

            you "Well, maybe I do..."

            play sound s_laugh

            "She laughs."

            renza "Hey! Don't go thinking I'm as easy as the girls you spend all your time with."

            renza "You're not going to get to me with cheap compliments... But keep trying."

            $ NPC_renza.love += 1

        "你记错了":

            $ renpy.block_rollback()

            you "Nah, I'm only here to check your junk... Wait. That came out wrong."

            play sound s_laugh

            renza "Well, I'm a little disappointed. *wink*"

            renza "But you're right. Let's get on with business."

    return

label renza_friend2: # Chapter 1 must be done + L=15 + not NPC_renza.flags[story1]

    "You find Renza with a frown on her face, looking at a mess of papers scattered all across the table."

    you "Hi, Renza."

    renza "Hmm? Oh, hi, [MC.name]. Sorry, I was lost in my thoughts."

    you "What's on your mind?"

    play sound s_sigh

    renza "Well, a lot actually..."

    if story_flags["c1_path"] == "neutral":

        renza "Business has been good since Lydie took over the city guard, and we have expanded our network ten-fold. I get reports every day from all corners of Zan, and even the rest of Xeros."

        renza "It's a lot to wrap my mind around... I barely leave the office anymore, and I barely have time to sleep."

        you "But... Don't you have help?"

        renza "Of course I do, but you know, thieves are not the most loyal breed... Many would like to take my place, so I cannot show any weakness."

        renza "There are things I can only handle myself. But sometimes, the responsibilities feel crushing... It's a lonely job."

        renza "Mom would have known how to do it. I'm not sure I can."

    else:

        renza "Well, since we lost our mole in the city guard thanks to a certain someone... We have had to find new avenues for growth. I've increased business with out of town freelancers, but it's a lot to keep track of."

        you "I see. I guess stealing other people's shit is hard work, after all."

        renza "You're joking, but it is a stressful job. Every day I have to make decisions about who to trust... Most of the people I deal with would as soon stick a dagger in my back as shake my hand."

        you "Thieving Is a dog-eat-dog world, it seems. Who would have thought?"

        renza "In this occupation, you take one misstep, and you end up in jail... or dead in a ditch. I often ask myself what my mother would do..."

    you "Your mother?"

    renza "Anyway, enough chatting. Came to have a look at my wares?"

    you "Always so business-like. Do you ever do something for fun?"

    "She seems to be reminiscing for a second, and her mood darkens."

    play sound s_sigh

    renza "No... Not anymore. Every once in a while, I go to the onsen to relax my body and clear my mind... But I'm afraid with this job, my days of wild partying are over."

    if brothel.has_room("onsen"):

        you "Well, you're in luck. It just so happens that I have a private onsen at home. Come check it out!"

        play sound s_laugh

        renza "Oh, I don't know about that! I'd be worried about you peeping. *grin*"

        you "Me? Why, I would never..."

    else:
        you "I see."

    return

label renza_friend3: # NPC_renza.flags[story1] + L=20 + not NPC_renza.flags[story2]

    renza "Ah, if it isn't my favorite brothel-owner... What can I do for you?"

    you "Hmm. We're talking business, right?"

    play sound s_laugh

    renza "Haha, you're forward! Just remember, I have a sharp dagger, and twenty years of training in using it."

    "You frown as you make some complicated calculations."

    you "Twenty years? Why, you don't look that old to me..."

    renza "Oh, but I started very early! You can say I was born into this."

    you "Were you? You mentioned something about your mother..."

    renza "Oh."

    "Her mood darkens."

    you "Come on, Renza, tell me something about you. We're friends now, aren't we?"


label renza_friend3_menu:

    menu:

        "你是怎么走上这一行的?" if not NPC_renza.flags["told_origin_story1"]:

            renza "Well... I was born right here, in Zan. Some say I was delivered in the temple of Shalia itself. It's not like I really remember, but I play along with the rumors."

            renza "The thieves trained me from a very young age, and I learnt all the necessary skills: Picking locks and pockets, forging papers and coins, self-defense..."

            renza "But I wasn't much interested in their lessons, you know. As a teenager, I spent all my time away from the guild, fooling around with boys and getting in trouble..."

            you "Really? You look so serious and business-like to me..."

            play sound s_laugh

            "She laughs."

            renza "Oh, you would have been surprised! But sooner than I thought, I had to learn how to deal with responsibilities..."

            $ NPC_renza.flags["told_origin_story1"] = True

        "你是怎么爬到首领的地位的?" if NPC_renza.flags["told_origin_story1"] and not NPC_renza.flags["told_origin_story2"]:

            "A shadow comes across her face. She turns her head."

            renza "It is a painful memory."

            if MC.get_alignment() == "good":
                you "I'm sorry. I shouldn't have asked..."

                play sound s_sigh

                renza "No, it's alright. It is on my mind every day, anyway, so I might as well tell you."

            else:
                you "Come on, tell me the story. Please?"

                play sound s_sigh

                renza "Fine."

            renza "I was in my eighteenth year, spending most of my days and nights drinking and gambling with some bad people from all over the world in the harbor's taverns..."

            renza "My mom had warned me that as her only daughter, I was always a target, but I didn't believe her, or I didn't care. I don't know what I was thinking, really."

            renza "That night, I sneaked out of the guild just like I usually did, this time with a young acolyte who had joined us recently."

            you "I thought you said you weren't easy?"

            renza "Shut up. He was strong, witty and handsome... But he was also a spy for a rival gang. He brought me to an abandoned warehouse by the docks, where I was greeted by a dozen armed thugs."

            you "Oops."

            renza "Yes. They locked me up, and sent a message to my mom. She was to bring a very large sum of money, alone, or they'd rape and kill me. Just your typical kidnapping ploy."

            you "What did you do?"

            "She looks down in shame."

            renza "Well... Nothing. I was young and stupid, I kept raging at my captors and cursing them... All I could think about was how unfair it all was, and that it was somewhat my mother's fault. I was so selfish."

            you "..."

            renza "So the day came, and my mother went to their hideout, carrying a large bag of gold. Alone, like they asked. I will never forget how she looked that day. Red-eyed, and sick with worry."

            renza "When she saw me with my captors, she was both relieved and scared that something would happen to me. She knew the danger, but I know she would have given anything for a chance to save me."

            renza "That's why..."

            "Her voice breaks."

            you "Wh... What happened?"

            renza "That's why..."

            renza "That's why she didn't even fight it when it happened."

            renza "They asked her to put all of her weapons down. Then, the gang leader gave her a long lecture about how he was going to be the new boss in town... That arrogant fuck."

            renza "And then..."

            "She looks at you with teary eyes. You can tell she is reliving the moment."

            renza "Then he slit her throat."

            you "..."

            renza "It's such a strange thing, you know... My mother was the most formidable fighter you'd ever know. She could take on five or six guards with just a dagger and come out on top."

            renza "But when her time came, she didn't put up a fight, and in less than a minute, she was gone."

            "Tears are freely running down her face now."

            renza "I watched it all happen. That's all I could do. Watch."

            you "..."

            $ NPC_renza.flags["told_origin_story2"] = True

        "发生什么事了?" if  NPC_renza.flags["told_origin_story2"] and not NPC_renza.flags["told_origin_story3"]:

            you "How... How did you escape the gang that killed your mother?"

            renza "Well... When he was done with my mom, the fucking asshole turned to me. He was looking at me with his pig-like eyes, and his stare was a pure evil one."

            you "What... What did he want from you?"

            renza "Well, what do you think? Fuck me, of course!"

            renza "The bastard was reveling in his 'victory', and he thought he could make me his, because I was just young and stupid. Which I was."

            renza "But I was also a trained killer..."

            renza "He told his men to move back, and he started to rip my clothes off. But I had already found a way out of my bounds... So instead of him sticking me with his stupid prick, I stuck a dagger in his loins."

            you "You... You had a dagger???"

            renza "I did. I had a dagger the whole time."

            you "But..."

            renza "I know."

            "With rage, she wipes her tears with her hand."

            renza "I had that dagger THE WHOLE TIME! But I thought, you know, I thought nothing would really happen. I thought it was some kind of game."

            renza "I was so sure my mom would get me out of this, and that the next day I would be hitting the streets again like nothing happened."

            renza "But that's not how it all went down..."

            you "You must have been so mad."

            renza "I was. Mad at myself."

            renza "But I was also an angry, confused teenager. I couldn't keep all of this anger focused on myself. So I took it out on them."

            you "Oh."

            renza "After I shanked their leader, I turned my rage on them. There must have been ten of them, but none made it out alive. You better believe it."

            "She has a murderous spark in her eye."

            you "I... I do."

            renza "Then I went back to the guild, and I rallied my mom's followers to hit back at what was left of the gang."

            renza "That didn't sit well with some in the guild, however. Leadership over the thieves guild is not a birthright, they said. And many complained that I was risking the guild's resources to carry out my personal vendetta."

            renza "So they stood against me. But I was mad, angry, angrier than I've ever been. I would have done anything to get revenge."

            renza "So I used every trick in the book, everything I had learnt. I cajoled, threatened and bribed. I murdered, even, when I had to. Before six months had passed, I was the uncontested leader of the guild."

            renza "Eventually, with the help of my people, I tracked down every last member of the gang which killed my mother. Every one of them met his end, even if I had to send assassins all the way to a Hokoman hut to get him."

            you "Wow."

            renza "When they were all gone, I was still filled with anger and rage. It took time for me to realize that I was really mad at myself."

            you "So you've been beating your chest about this all this time."

            renza "Almost. But taking care of the guild's business eats up a lot of my time and energy, you know, and I know that eventually, I have to move on."

            you "Yes."

            renza "But some days... Some days are harder than others."

            "Tears creep back into her eyes."

            $  NPC_renza.flags["told_origin_story3"] = True

        "你的母亲是...?" if not  NPC_renza.flags["told_origin_story4"]:

            renza "My mother... My mother was magnificent."

            renza "Stealing, fighting, bargaining, plotting... She was a master in all the arts, and the guild is still buzzing with the stories of her feats and accomplishments."

            renza "She robbed the King's Hold not once, not twice, but {i}six{/i} times... Every time, they would devise a new security system, and every time she would find a way around it. It was like a game to her. She was a natural."

            you "Hey, you're not bad yourself."

            "She looks down."

            play sound s_sigh

            renza "Would that I had a tenth of her talent..."

            renza "In the end, the King even took to leaving notes in the palace vault, pleading with the 'thieves queen' to spare this or that jewel for the young princess... They say that my mother took everything else, but she left those untouched!"

            you "She was really something..."

            renza "She became the leader of the thieves guild around the time she was carrying me. She was spending way more energy than was reasonable for a woman in her position to take care of me, but somehow, she always found the time."

            renza "I should have appreciated her more..."

            $  NPC_renza.flags["told_origin_story4"] = True

        "那你的父亲呢?" if NPC_renza.flags["told_origin_story4"]:

            renza "My father? Oh, my father was a brave man..."

            renza "So brave that he sailed away to wherever, the night after my mother told him she was pregnant."

            renza "With skills like hers, I'm sure she could have easily tracked him down and brought him back bound and chained... But she wasn't the vengeful type."

            renza "I, on the other hand, would not have been so forgiving. *sneer*"

            "You wonder if it was meant as a warning."

            $  NPC_renza.flags["told_origin_story5"] = True

        "介意我问一下你的纹身吗?":

            "You look at her tattoo, trying to pretend you're only interested in the artful drawing and not the juicy, fleshy hip underneath."

            "It represents a mythical snake, eating its own tail."

            renza "This? It's a coming of age tattoo, nothing really... We all get one."

            you "I see."

            renza "I had it done when I became the guild leader. In time, it became our unofficial symbol."

            renza "It means..."

            "She looks thoughtful."

            renza "Well, nothing really. It's just an old symbol."

            $  NPC_renza.flags["told_origin_story6"] = True

    if not NPC_renza.flags["told_origin_story5"] and not NPC_renza.flags["told_origin_story6"]:
            jump renza_friend3_menu


    you " Thanks for telling me the story. I'm sorry I brought back some painful memories."

    renza "It's alright. I have to revisit this from time to time. It keeps me on edge."

    you "Take care, Renza."

    renza "Thank you."

    return

label renza_onsen1: # NPC_renza.flags[story2] + L=25 + not NPC_renza.flags[story3]

    scene black with fade
    show expression bg_bro at top
    with dissolve

    "That night, as you stand by the main entrance greeting customers, you spot a familiar face among the rowdy crowd."

    show renza with dissolve

    renza "Hi, [MC.name]."

    you "Renza, hi! This is an honor. What can I do for you?"

    "She blushes a little, a rare sight for Renza."

    renza "Well... I came to check your onsen. Provided you have a legitimate use for it, of course."

    you "Of course, of course!"

    "You yell."

    you "Make way! Sill!"

    hide renza with dissolve

    "With Sill's help, you push patrons and girls away from one of the pools, paying no attention to their complaints."

    scene black
    show bg onsen at top
    with fade

    you "We have a VIP! Sill, wipe this place clean, will you!"

    sill sad "Ye-e-es... Yes Master..."

    renza "Thanks! Hey, I'm sorry for causing such a commotion."

    you "Nah, you're welcome. After all, you're my guest..."

    menu:

        "You think to yourself."

        "我应该取悦我的合作伙伴":
            $ renpy.block_rollback()
            $ MC.good += 1

            you "(I'm happy Renza came. I want her to be comfortable. Plus, she's hot.)"

        "这对我的生意很有帮助":
            $ renpy.block_rollback()
            $ MC.neutral += 1

            you "(Having the infamous leader of the thieves guild as a guest will surely drive business up. Plus, she's hot.)"

        "我只是想大饱眼福":
            $ renpy.block_rollback()
            $ MC.good -= 1

            you "(Just you wait. I'm going to get an eyeful...)"

    renza "Thank you, [MC.name]. Now, if I could have some privacy..."

    you "Of course, of course! Enjoy, and relax, my lady. I hope you'll have a great time. *grin*"

    "You have your slaves move some screens around the pool, and manhandle a few customers pretending to busy themselves around Renza's pool for a chance to get an eyeful."

    "In the process, you couldn't help but notice a small opening left between some of the screens. This could be your chance to peep..."

    menu:

        "What do you do?"

        "偷窥伦萨":
            jump renza_onsen2

        "不偷窥":

            you "This isn't right. Renza's my friend. A very hot friend, for sure..."

            "For a second, you think about the smooth curves of her toned body, and how nice the round shapes of her boobs look under her outfit."

            "You swallow hard."

            menu:
                "偷窥伦萨":
                    jump renza_onsen2

                "不，还是算了":
                    you "I must be strong. I'm an upstanding citizen."

                    if MC.god == "太阳神":

                        you "Remember what Arios says. 'Temptation is a dark tit'... Pit. Pit, I meant pit."

                    else:

                        you "And Renza is my friend, to boob... To boot. Boot, I meant boot!"

                    show screen invisible_button

                    menu:
                        "偷窥伦萨":
                            pass

                        "绝对不能偷看":
                            "You have decided not to peep on Renza."
                            "Or..."
                            "Or have you? You are feeling a little confused right now."

                    hide screen invisible_button
                    scene black with fade
                    jump renza_onsen2


label renza_onsen2:

    play sound s_sigh

    renza "Aaah... this feels so good..."

    show bg renza_onsen at top with fade

    "Through the peephole, you can see Renza entering the bath. To your disappointment, she is wearing a bath towel, but you can see her large nipples perk through the wet fabric."

    you "(Oh, it's nice...)"

    renza "Mmmmh... This is relaxing..."

    you "(I'm sure she's gonna drop the towel any second now...)"

    "Renza moves further into the bath, letting the hot water rise against her thighs."

    play sound s_mmmh

    renza "Oh, I love it..."

    you "(Damn, there's too much mist... It's hard to see anything...)"

    you "(Come on... I wanna see more...)"

    play sound s_surprise

    sill happy "Master!" with vpunch

    you "(W-What???)"

    sill happy "Master! Where are you?"

    "You see Sill entering the onsen space, looking for you. Leaving your hideout, you rush towards her, trying to prevent her from exposing you."

    you "*whispering* Damn you, Sill!!! Now is not the right time..."

    sill "*loud* Oh, Master! One of the customers got so drunk, he started running naked around the-ouaaaaaaaaah!!!"

    play sound s_scream

    "Grabbing Sill by the ear, you drag her out of the bath area as quickly as you can."

    scene black
    show bg tavern at top
    with fade

    show sill sad with dissolve

    sill sad "Master, it hurts! Aaaw..."

    you "Are you fucking crazy!!! You just ran in on me while I was, uh, arranging the room for our guest... She's a trained killer, she hates being disturbed! She could have stabbed us both!"

    sill "I'm sorry, Master, I thought..."

    you "Well don't think! And shut the fuck up! I don't want anyone hearing about this, all right?"

    sill "Y-Yes, Master..."

    "You hear some noise coming from the onsen. Renza might be coming."

    you "Aaaaah!!! Quick, pretend we are doing something important!"

    with fade

    show sill sad at left with move

    show renza at right with dissolve

    you "...and then, I want you to ask the laundry guy for ten new sets of lace underwear..."

    sill "Y-Yes, Master [MC.name]..."

    renza "Oh, [MC.name]! Thank you so much for letting me use the onsen. It was very refreshing."

    sill happy "Thank you for your custom! Sorry for the int..."

    play sound s_punch

    sill sad "Ouch!!!" with vpunch

    you "She meant, sorry for the interior design, it could really do with an improvement! Hahahaha!"

    renza "Oh... Never mind that, I didn't really notice. No need to hit your slave over that..."

    you "Nah, it's okay, she likes it..."

    sill "I don't..."

    renza "Anyway. Thank you so much. I love your onsen! I could become a regular."

    you "Always a pleasure to have you."

    scene black with fade

    "After Renza leaves, you realize watching her gave you a raging hard on. You decide to take it out on Sill, as she's sort of the cause of your current predicament."

    show bg nogiofuck5 at top with dissolve

    play sound s_moans

    sill "Ah, Master! Aaaaah!!!"

    $ MC.rand_say(("gd: I'm not stopping until you come! This is your punishment!", "ne: This is for your Master's good! You better please me!", "ev: You stupid bitch slave! I'll teach you some manners!"))

    play sound s_orgasm_young

    scene black with fade

    return

label renza_onsen3: # NPC_renza.flags[story3] and L=35 and not NPC_renza.flags[story4]

    "Late at night, you politely escort out the few lingering customers..."

    scene black with fade

    show bg tavern at top with dissolve

    you "Phew, tonight was busy... I feel pretty tired."

    show sill at center with dissolve

    sill happy "I'm going to sleep. I'm exhausted..."

    sill "Good night, Master..."

    you "Night, Sill..."

    hide sill with dissolve

    "It's always strange when the brothel falls silent, after a night of heavy drinking and partying."

    you "I guess I'll have a drink on the house before hitting the sack."

    "You start going around the bar, looking for a non-empty bottle."

    play sound s_creak

    you "Wait, what was that?"

    "You heard a noise coming from the onsen. Perhaps the brothel is not as empty as you think?"

    you "The security guards are all on break at this hour... I'll go and check it out."

    scene black with fade

    show bg onsen at top with dissolve

    "You enter the onsen cautiously, wary about running into some angry drunkard."

    "Soon, however, you spot an open window, creaking under a gentle breeze. That was the source of the noise you heard."

    play sound s_door_close

    "You close it."

    you "Well, that was nothing."

    "You feel very sore and tired all of a sudden, and the warm mist of the onsen looks inviting."

    you "I've had a long day... Why don't I go for a little bath before going to sleep? This will do me a lot of good."

    "Shedding your clothes, you sleepily enter the warm bath."

    you "Aaaah... This is so good..."


    woman "Uh? Is anyone here?"

    scene black
    show bg renza_onsen at top with fade

    you "Aaaah!!!" with vpunch


    renza "[MC.name]?"

    "It seems Renza had been enjoying the bath you've entered. No doubt she is going to kill you now."

    you "I, uh, I mean... I didn't know..."

    "Your whole life flashes before your eyes. There's an awful lot of fucking various girls, but not nearly as much as you would have liked."

    if MC.god:
        you "[MC.god], guard my soul..."
    else:
        you "I've had a good run... The game is over now..."

    "Renza starts moving towards you, and you can do nothing but raise your arms above your head, trying to protect yourself."

    you "Not the face, please! Not the face! I'm sorry!"

    renza "..."

    renza "What are you doing?"

    you "..."

    you "You're... You're not mad?"

    renza "Mad? No... Not really... I'm the one who broke in for a late bath, after all. This place is big enough for the both of us."

    you "You... You mean I can stay?"

    renza "Sure, of course... It's your house, after all. Why don't you keep me company?"

    "Renza seems to be pretty comfortable with her body, and doesn't mind sharing the bath with you."

    renza "Come over here... Don't be shy."

    "You settle for a spot a few yards apart from her. You two start chatting, barely seeing each other through the mist. You gradually ease into the situation, even though you are doing your best to conceal
     a raging hard-on under the steamy water."

    you "So, you've had a rough night too?"

    renza "I did... Survived another assassination attempt, from a close associate... Then I had to go into the city to break a couple of my men out of jail...
           And on the way back, I hit a rich
           merchant's house. Just for the fun of it."

    you "Wow... Your life isn't lacking for excitement..."

    "She looks sad."

    renza "Excitement... I wouldn't describe it that way..."

    you "What's wrong?"

    renza "I don't... I don't feel like I deserved any of this..."

    renza "I only became the guild leader because I wanted to avenge Mom. I had no plan beyond that, I wasn't thinking about the long run... Now, what should I do?"

    renza "She was the rightful guild leader. I'm just a joke, pretending to be tough just to survive another day..."

    you "No... You're not..."

    renza "You know what I want? What I really want?"

    renza "I want my mum back. I want my life back. I want to be stupid and innocent again. I want to erase this terrible mistake."

    you "..."

    renza "But it doesn't matter how much power I have, how much riches I steal... Nothing can bring her back."

    renza "So what's the meaning of my life, since the only thing I really want is forever out of reach?"

    you "..."

    menu:
        "大家可都指望着你":
            $ renpy.block_rollback()
            $ MC.good += 1

            you "You don't have to be alone and miserable. You have people counting on you, people who care about you..."

            you "I care about you."

            renza "..."

            renza "[MC.name], you're sweet... Even if it's just flattery, it makes me feel better."

            you "It's not... You're a great person. Don't let one mistake define you."

        "你可以纪念她":
            $ renpy.block_rollback()
            $ MC.good += 1

            if MC.god:
                you "Your mom is watching with the gods. She sees what you're going through. You can live your life in a way that would make her proud."
            else:
                you "Your mom was an amazing person, and she cannot be replaced. But you can live your life in a way that would make her proud."

            renza "..."

            renza "You're right. I must be strong, to honor her memory. She didn't raise a weak girl."

            renza "She raised me as a fighter. So I will fight on. To preserve her legacy to the guild."

        "过去的事就让它过去吧":
            $ renpy.block_rollback()
            $ MC.neutral += 1

            you "You cannot live your life fully until you let go. Your mother is gone, she won't come back.
                 The sooner you accept it, the sooner you can do something meaningful with your life."

            renza "..."

            renza "Deep inside me, I know you're right. I just need a little time..."

            you "Time will help, but you must also change your mind. Come here as often as you like, and try to leave the past behind."

            renza "Thank you. I understand."


        "没必要沉浸在过去的伤痛中":
            $ renpy.block_rollback()
            $ MC.neutral += 1

            you "The responsibilities of a guild leader are smothering you. This is not the life you'd have chosen for yourself.
                 Why don't you free yourself from this?"

            renza "But my mom... She worked so hard, to achieve so much... I can't just let that fall apart."

            you "Maybe, but she didn't mean to make you a slave to her legacy. You need a fresh start. Staying with the guild is only making you more bitter."

            renza "..."

            renza "You might be right... I can't say the idea of quitting hasn't occured to me before... But I need time to think."

            you "Please do. I hate to see you wither away like that."

            renza "Thank you, [MC.name]..."

        "停下你无谓的抱怨吧":
            $ renpy.block_rollback()
            $ MC.evil += 1

            you "Oh come on, when did you become such a crybaby?"

            you "Your mom's dead, and she isn't coming back. Yes, it's your fault. No, you can't do anything about it. So just suck it up,
                 and show some sand for Shalia's sake!"

            renza "Why you..."

            renza "..."

            renza "You're right, of course."

            renza "I didn't mean to show such weakness. I'm pathetic."

            you "Only when you act like a quitter. But the Renza I know, she wouldn't give up on a fight so easily, would she?"

            renza "It's a nice way to put it, I guess... But no. I won't give up."

            you "Good."

            renza "I appreciate the tough love, [MC.name]."

            you "You're welcome."

    "She remains lost in her thoughts for a minute."

    renza "What about you, [MC.name]? What's your goal in life?"

    menu:

        "为了扬名立万，出人头地":
            $ MC.neutral += 1

            you "I want to rise in Zan and make a name for myself. I want to become as famous as the King himself."

        "为了富甲天下，酒池肉林":
            $ MC.neutral += 1

            you "I want to become filthy rich, and live a lavish lifestyle..."

        "为了权倾朝野，掌控一切":
            $ MC.evil += 1

            you "I want to be all powerful, to force the world to do my bidding..."

        "为我的朋友两肋插刀":
            $ MC.good += 1

            you "I want to do right by my friends, and remain loyal."

        "让我的敌人一败涂地":
            $ MC.evil += 1

            you "I want to crush my enemies, see them driven before me, and hear the lamentation of their women... While I fuck them!"

            you "While I fuck the women, I mean, not the enemies... Unless the enemies are women... But then, uh... Err..."

        "我要和所有美女做爱":
            $ MC.neutral += 1

            you "I want to fuck all the girls in Zan. It's a tough job, but someone's got to do it."

        "我喜欢走一步算一步":

            you "There's no such thing as a goal in life. We're only here for a fleeting instant... So all we can do is enjoy the ride. And I intend to enjoy it."

    $ renpy.block_rollback()

    play sound s_laugh

    renza "Wow, you're amazing!"

    renza "At least, you don't want to become the head of the thieves guild... That's a relief."

    you "Haha..."

    renza "It's always good to talk to you, [MC.name]. It takes my mind off my sorrows..."

    "She falls silent."

    "You don't really know what to say, so you both stay in silence for a few minutes."

    "The situation is starting to feel embarrassing, and your hard-on refuses to recede. You start to think about a way to excuse yourself."

    renza "[MC.name]?"

    you "Renza?"

    "She moves closer to you. Suddenly, you feel her soft hair against your skin. She rests her head on your shoulder."

    you "Renza..."

    renza "Would you... Would you hold me?"

    "You are disarmed by her candid request. She seems lost and vulnerable, unlike the Renza you know."

    "Reflexively, you take her into your arms. She holds you close, with her head against your chest."

    renza "I want to feel safe... I want to feel warm... I want to feel human... Just for a few seconds..."

    you "..."

    "You hold her close without thinking. However, embarrassingly, you suddenly feel your erect member brush against her naked thigh."

    renza "Wow... Is that what I think it is?"

    you "Err, ahem, I mean, it's the onsen and all... It has some rejuvenating properties, or so they say, you know?"

    play sound s_laugh

    renza "It has, hasn't it? I too feel a little light-headed... Mmmh..."

    "She hugs you closer. You do not dare to move a muscle, but your dick is still pressed against her body. It is throbbing painfully now."

    renza "..."

    "Renza lowers her hands and caresses your back. Slowly, she reaches for your buttock, lightly touching it."

    you "Renza..."

    "Before you know what is happening, her slender hand is running the length of your shaft. She starts toying with the tip of your cock,
     squeezing it between her fingers."

    play sound s_mmmh

    renza "Hmmm... What are we going to do about this?"

    "You cannot hold back anymore. Pushing Renza against the edge of the bath, you start caressing her naked thighs and buttocks."

    play sound s_surprise

    renza "Oh, [MC.name]! Aaah!"

    show bg renza_sex1 at top with fade

    play sound s_sucking loop

    "*lick* *lick*"

    renza "Oooh... [MC.name]... It's so good..."

    "Spreading Renza's legs apart, you slowly lick along the pink lips of her pussy."

    play sound2 s_ahaa

    renza "I like it... Aaaaah..."

    "You start fondling her bare ass as you inch your way up to her clit."

    play sound2 s_aaah

    renza "Oh, there... There..."

    "Renza flushes lovingly as she feels the build-up from your skilled tongue-working amidst the heat of the onsen bath."

    renza "I feel so light-headed... Oooh..."

    "Noisily sucking on her clit, still playing with her ass, you grab a hold of her towel with your free hand."

    you "Show me this juicy body..."

    "You tug suddenly at her towel, fully exposing her body."

    show bg renza_sex2 at top with dissolve

    play sound s_aaah

    renza "Aaah!!!"

    play sound s_orgasm_fast

    "The mixed feelings of excitement and embarrassment prove too much for Renza, who comes noisily as you stick your tongue up her slit."

    renza "AAAAH!!! It's so good!!!" with flash

    with doubleflash

    renza "AAAAAAAAAH!!!"

    show bg renza_sex3 at top with fade

    renza "Aw... I'm spent... You really know your stuff, don't you..."

    you "Hehe... We are not done yet."

    "You stand in front of Renza, your erect cock standing upright, bulging with excitement."

    renza "Oh... That's right... We need to do something about this..."

    scene black with fade

    show bg renza_sex4 at top with dissolve

    play sound s_mmmh

    renza "Wow... I'm really wet, still, it's hard to slip it all in..."

    you "I've been horny for far too long... This is the result..."

    renza "It can't be helped, then, I must take responsibility for this... Aaaah..."

    "Slowly sliding into her, you are surprised at how tight she is. Your foreplay left her very wet and willing, however, and her pussy soon expands to accommodate
     the whole length of your cock."

    renza "I could get used to this... It's nicely filling me up..."

    you "I'm going to start moving now... Ready?"

    renza "Give it to me, [MC.name]..."

    show bg renza_sex5 at top with fade

    play sound s_moans

    renza "Yes, oh, yes..."

    "You push your dick all the way up her hungry cunt, then slowly slide it out inch by inch, until you're almost out of her. Then you plow into her again."

    renza "Aaah... Fuck me, [MC.name]... I want your cock..."

    "Renza gives you a naughty look as you fuck her harder and harder. She gives you a great view of her ample tits as she plays with her hair."

    renza "I love it... You're fucking me so deep, oh, yes..."

    "Renza's pussy feels so good that you cannot help but feel close to your limit."

    you "I'm... I'm going to come..."

    renza "Today is safe... Stay inside me, please... I want to feel you..."

    "No longer thinking clearly, you grab her large tits and start kneading them, pinching her nipples and watching with fascination as they twist and expand between your fingers."

    play sound2 s_surprise

    renza "[MC.name], if you do that, I will... Aaah!!!"

    you "I can't hold back any longer..."

    play sound s_mmmh

    renza "Aaaaaah!!! [MC.name]!!!"

    show bg renza_sex6 with flash

    you "RAAAH!!!"

    with doubleflash

    "You both climax simultaneously as you pour a load of hot, thick cum into her waiting pussy."

    play sound s_orgasm

    renza "Ah, [MC.name]! I can feel it... You're cumming so much, aw..."

    "Falling on top of her, you push your dick deeper inside as the last drops of cum squeeze out into her."

    renza "It feels so good... Mmmmh..."

    "Renza holds you gently, and you both spend some time in each other's arms, not quite coming to terms with what just happened."

    $ unlock_achievement("h renza")

    with fade

    play sound s_mmmh

    renza "Wow, I haven't felt so good in a long, long time..."

    you "I had a great time too..."

    play sound s_laugh

    renza "I have to say, I must recommend the service in your establishment! *laugh*"

    you "You're welcome. *smile*"

    "You gently fondle her tits, while she plays with your hair. Neither of you want to break the embrace just yet."

    "Running your hands down her soft, toned body, you notice again her black hip tattoo, glistening with hot water."

    you "Say, can I ask you something?"

    renza "Sure..."

    you "What about this tattoo? What does it mean?"

    renza "..."

    renza "It's a snake eating its own tail. It's an ancient symbol of Shalia."

    renza "It also represents the young, feeding on the old... Like a child murdering his parent."

    you "..."

    you "You chose this, because it represents how you feel about your mother's death? Because you think it's your fault?"

    renza "Yes..."

    you "I see... Renza, it's obvious your grief is running deep... But you have to get over it someday..."

    "She looks at you with newfound resolve."

    renza "I know. I will."

    "She kisses you on the cheek."

    renza "Thanks for giving me the strength to carry on..."

    you "You're welcome..."

    renza "I had a great time tonight... Bye, [MC.name]."

    you "My lady."

    "Breaking from your embrace, Renza dreamily steps away from the bath, giving you one last view of her wonderful, naked body."

    "As she puts her clothes on, she turns to blow you a kiss."

    renza "Goodbye, [MC.name]... *wink*"

    you "Bye, Renza."

    "You blink, and she is gone. It's almost as if it was all a dream."

    scene black with fade

    you "Phew, now {i}I'm really{/i} spent. Let's go to bed..."

    $ MC.change_prestige(5)

    "You have earned prestige."


    play sound s_chimes
    $ NPC_renza.unlock_trainer()

    return


## Farm story events

label farm_meet_gizel(): # Location: spice market

    play music m_oriental fadein 3.0

    scene black
    show bg spice_market at top

    with fade

    if MC.playerclass == "战士":
        $ text1 = "anti-rust lotion"
    elif MC.playerclass == "法师":
        $ text1 = "magic herbs"
    elif MC.playerclass == "奸商":
        $ text1 = "dragon feed"

    "Walking around the market, looking for [text1], you notice an exotic figure looking at the wares of a nearby spice merchant."

    show gizel with dissolve

    gizel "No, that won't do..."

    "A young lady in a strange attire, a teenager by the looks of her, is checking the properties of various spices, sampling some with a thoughtful look on her face."

    "There's something odd about her. Her hair is bleached blond, almost white, and her skin is extremely pale."

    "She cuts an unusal figure even here in the slums, where
     all nations and races rub elbows - as well as other body parts."

    gizel "And whatever is this? Fireroot, perhaps? Hmm, no..."

    "Staring at the slender young girl, it finally hits you: she is not a human, but an elf. That would explain her exotic looks and mysterious behavior."

    "You ponder the meaning of this for a second. Elves are very rare in Zan, and much-maligned, because of their role in the ongoing war in the Holy Lands.
     To say that they are being frowned upon in the streets of Zan would be an understatement."

    you "Well, I suppose there's all sorts of people living in the slums... I wonder where this young elf came from? And what of her kin? Is she by herself?"

    hide gizel with dissolve

    "You stop for a moment, thinking about what you know about the fairy people."

    scene black
    show bg elves
    with fade

    "Graceful, distant, with a fondness for nature and older gods, the elves count expert craftsmen, druids and magicians among their ranks. They are also fierce warriors and archers."

    "There are far more females than males among the fairy people, meaning most roles in elvish society are filled by women, from merchants to war commanders."

    "Although they have walked among other races for centuries, their civilisation and history go back a lot longer than most. Some say their natural lifespan can extend for centuries, although because of the war, violent deaths have become all too common nowadays."

    "This brings you to your personal experience of elves."

    menu:
        "How do you feel about elves?"

        "我和他们无冤无仇":
            $ MC.rand_say(("I don't hate them. Wars come and go, and it wasn't they who started this one...", "ar: Although the Arios church denounces the elves, I do not think they are bad. They can be brought back to the light.", "wr: I have fought enough elves on the battlefield to respect their grit and abilities. They are worthy opponents.", "wz: I do enjoy a good conversation with an elf from time to time. They know a great deal of secrets, though they don't share them very willingly."))
            $ story_flags["elves"] = "like"

        "我恨他们":
            $ MC.rand_say(("I despise these pointy-eared rats. The only good elf is a dead elf, I always say.", "ar: Those spawns of hell show no respect to the true Light, and occupy the Holy Lands against the will of men and Gods. I hate them.", "wr: The damn elves took the lives of many of my comrades on the battlefield. I shan't forgive them."))
            $ story_flags["elves"] = "dislike"

        "我也不知道":
            $ MC.rand_say(("I can't say I have met many elves, much less talked to them. So I reserve my judgement.", "ng: I don't really know. The Arios Church hates them I guess, but I have no time for phony gods and their minions.", "wz: Elves know many things, and I'm sure one could learn a lot from them... If they weren't like to pelt you with poison arrows whenever you come near them.", "tr: I've traded with elves quite a bit in the past. They are good on their word, I guess, although they won't win any popularity contest."))
            $ story_flags["elves"] = "neutral"

    man "Make way!"

    scene black
    show bg spice_market at top
    with fade

    "Hearing a commotion behind you, you move aside to let a guard patrol move through the market crowd."

    show initiate at left
    show templar
    show initiate at right as initiate2
    with dissolve

    "As the armed guards pass by, you notice they are escorting a heavily armored knight, sporting the Arios crest on his tunic. A templar."

    hide initiate
    hide templar
    hide initiate2
    with dissolve

    you "We see more and more of them in the streets every day... Shouldn't they be on the battlefield?"

    "You turn around to glance at the elf girl."

    "She's vanished."

    you "Well, good for her..."

    "Feeling a little curious, you walk over to the stall to see what she was browsing."

    you "'Bernard's love charms and aphrodisiacs', uhm..."

    stop music fadeout 3.0

    $ story_add_event("farm_meet_gizel2")

    scene black with fade

    return

label farm_meet_gizel2():

    play music m_suspense fadein 3.0

    scene bg junkyard with fade

    "The junkyard is a dreadful place to take a walk around on most days, thanks to the smell and noise, but today, it seems eerily quiet."

    you "This silence... I'm not about to fall into another one of those stupid ambushes, am I?"

    "The junkyard is located in the lowest part of the slums. It seems almost empty today."

    "You know for a fact that you aren't alone here, however, as crumbling shanty houses line the scrapyard. They're populated with all sorts of
     rabble and outcasts, who make a living sorting through other people's trash, or simply hiding from the law."

    you "I guess the guard patrols are too scared of the smell and diseases to come down here..."

    "Still, today is an unusually quiet day. Perhaps it's the harsh sun, which mercilessly sheds its burning light on this shadowless place,
     or some vague sense of menace in the air? But what could be fouler than the normal smell of this place?"

    "Sitting on the top of a large trash hill, you look around you, trying to peer into some of the roughly built shacks, hoping to get a peek into the
     everyday life of its inhabitants."

    you "..."

    you "Damn, I'm bored."

    "You had just about enough of this little game, when you spot a familiar figure walking among the crumbling sheds."

    show gizel with dissolve

    you "Hey! Wait a minute... Isn't it that girl elf?"


    you "That's her..."


    "The pale teenage elf you saw at the spice market is pacing up a narrow alley, walking up to one of the huts into which she promptly enters."

    hide gizel with dissolve

    you "So, maybe she lives here, then? That's unexpected for an elf. Still, not a bad place if you want to avoid attention..."

    "Pondering this little piece of information, you turn around and start climbing down from your vantage point. That's when you hear the distinct clanging of armored feet echoing through the junkyard."

    play sound s_clash

    you "Damn... What's this?"

    "A hand on the hilt of your weapon, you hide yourself behind a pile of rubbish, trying to get a glimpse of the party advancing through the junkyard."

    show templar with dissolve

#    pause 0.1

    show initiate as initiate1 at right

#    pause 0.1

    show initiate behind templar as initiate2 at left
    with dissolve

    "A patrol of Arios church warriors is making its way through the scrapyard, armored for battle."

    you "Templars... Here, of all places?"

    "You pause to think."

    if story_flags["elves"] == "like":
        you "This must mean they are after this young girl... I should warn her!"

        if MC.get_alignment() != "good":
            you "Although, to be sure, this is none of my business..."

        menu:
            "What do you do?"
            "警告那个女精灵":
                $ result = "warn"
                $ MC.good += 1
            "袖手旁观吃瓜看戏":
                $ result = "wait"
                $ MC.good -= 1

    elif story_flags["elves"] == "dislike":
        you "This is an unexpected opportunity. If I deliver that bitch elf to them, I might get rewarded."

        if MC.get_alignment() == "good":
            you "Although that does sound cowardly, even though she's just an elf."

        menu:
            "What do you do?"
            "检举精灵的藏身之处":
                $ result = "denounce"
                $ MC.evil += 1
            "袖手旁观吃瓜看戏":
                $ result = "wait"
                $ MC.neutral -= 1

    else:
        you "They must be looking for that girl. After all, Arios templars are tasked with hunting elves..."

        menu:
            "What do you do?"
            "警告那个女精灵":
                $ result = "warn"
                $ MC.good += 1
            "检举精灵的藏身之处":
                $ result = "denounce"
                $ MC.evil += 1
            "袖手旁观吃瓜看戏":
                $ result = "wait"
                $ MC.neutral += 1

    $ renpy.block_rollback()

    if result == "warn":

        hide templar
        hide initiate2
        hide initiate1
        with dissolve

        "Moving silently through the scrapyard, you make your way towards the shanty house where the girl entered, without being seen."

        you "It must be this one..."

        scene black with fade

        "Lifting the thick curtain that covers the entrance of the small hut, you slip in quietly."

        play sound s_dress

        show bg gizel_room at top with dissolve

        "The hut seems surprisingly well-built and comfortable for such a lowly area of the slums."

        "Looking around the room, you see it is littered with strange apparatuses and mysterious elixirs. Hardly the dwelling of a simple beggar."

        "Half-hidden by a shelf, you see a set of stairs leading down. You hear a muffled sound coming from down there... Neighing?"

        show gizel surprise at center with dissolve

        play sound s_surprise

        gizel "Uh?"

        gizel "Who... Who are you?"

        "She recoils from you as she sees your weapons."

        gizel shy "I have nothing of value, mister... I'm just a poor girl. Please, leave me be..."

        you "Uh, me? Don't worry, I'm just a friend. I came to warn you."

        gizel surprise "W... Warn me?"

        you "There's this party of templars outside, and I think they're looking for you."

        "You hear that muffled sound again coming from downstairs."

        you "Wait a minute... What exactly are you doing here?"

        gizel upset "That's none of your... "

        gizel surprise "Wait, what did you just say? Templars???"

        "You hear a strong, commanding voice coming from just outside."

        man "If our information is correct, it must be around here."

        man "Men, search every house!" with vpunch

        gizel upset "Demons!"

        "Jumping to her feet, the girl runs out of the house, only to bump right into one of the armored initiates."

        play sound s_punch

        gizel "Ouch!" with vpunch

        initiate "Hey!"

        show initiate at right with dissolve

        initiate "Brother knight! Look what I just found!"

#        show templar at left with dissolve

        templar "Well, well... What do we have here?"

        gizel shy "Mister, I don't understand..."

        templar "Seize her! And bring her accomplice too!"

        you "Hey! I'm not..."

        initiate "Shut up. You're coming with us."

        play sound s_sheath

        "The initiates disarm you and shove you out of the hut following the elf girl."

    elif result == "denounce":

        "Walking up to the group of armored templars, you salute the head knight, bowing as low as you can."

        you "Hello, my lord, please allow me to introduce myself..."

        templar "What in Arios's name do you want? We're busy."

        you "Busy, yes, I can see that. Then you wouldn't be interested in the whereabouts of a local elf, would you?"

        templar "No, now..."

        templar "Wait, what?" with vpunch

        templar "Speak."

        you "A weird elf girl, young and slender, with pale hair and white skin. A spy, no doubt. I could show you the location of her hideout..."

        templar "That fits her description, all right. Take us there."

        you "Of course, of course... I trust I will be rewarded well for my trouble?"

        templar "..."

        templar "Humph. All in due time, citizen. You will get your due."

        you "Fine! Follow me then."

        play sound s_dress

        scene black
        show bg gizel_room at top
        with fade

        show gizel at center with dissolve

        gizel surprise "W... What the hell?"

        templar "There she is!!! Men, seize her."

        play sound s_surprise

        "The elf squeals with surprise as the knights pour into the small hut, surrounding her."

        show initiate at right behind gizel with dissolve

        templar "You're ours, now, you devil witch."

        gizel "There must be some mistake! I'm just a maid..."

        templar "Save your breath, freak."

        "The men escort the elf girl out."

    else:

        "Remaining concealed, you look on as the party spreads out among the makeshift huts of the shantytown."

        hide initiate2 with dissolve

        pause 0.2

        hide initiate1 with dissolve

        pause 0.1

        hide templar with dissolve

        you "They are going towards her hiding spot..."

        "Remaining under cover, you silently move closer, until you hear the men shouting orders."

        templar "Storm the house!" with vpunch

        play sound2 s_shatter

        "You hear noise coming from the elf girl's house, followed shortly by a woman's scream." with vpunch

        play sound s_scream

        templar "There she is! Men, seize her."

        "After a few moments, you see the men emerge from an alley, holding the captive young elf between them."


    scene bg junkyard with fade
    show gizel shy with dissolve

    gizel shy "Let me go! Please, let me go..."

    show initiate behind gizel as initiate1 at left
    show initiate as initiate2 at right
    with dissolve

    "The guards shove the young elf forward, bringing her to the center of a clearing amidst the garbage piles."

    if result == "warn":
        "You are forcefully brought along the girl elf and made to stand a few yards back."
        you "Gentlemen, this is a misunderstanding..."
        initiate "Shut it."
    elif result == "denounce":
        "You follow the group a few steps back, hoping to get your reward once it is all done."
        you "I hope this templar is good on his word... Men of the cloth have a way of shrugging off their commitments when it suits them."
    else:
        "You keep watching from a safe distance, making sure you remain unseen."
        you "This doesn't bode well for the girl..."

    templar "Stop here! This place will do."

    gizel shy "What do you want from me? I'm just a poor beggar, I swear..."

    templar "Silence, demon!" with vpunch

    initiate1 "Is she... Is she truly the witch of the North?"

    initiate2 "Is that really her? I mean, she doesn't look like much..."

    templar "Quiet."

    templar "We know who you are, witch. We will serve justice to you, just like we do to the rest of your evil kin."

    gizel "I don't understand... I have done you no wrong, sir..."

    templar "Do you deny that you are Gizel, the evil witch of the North?"

    gizel surprise "Uh???"

    $ gizel_name = "Gizel"

    gizel shy "Gizel is my name, sir, but I am no witch... I'm just a teenage beggar, come to Zan to make a few denars..."

    "The templar silently takes a long look at her, pondering the situation."

    initiate1 "Well, she's awfully young to be a witch... I mean, witches should be old and creepy, with a wart on their nose and all, shouldn't they?"

    initiate2 "But she's an elf, there's no telling how old she is... And she could be assuming this form with magic, just to throw us off..."

    initiate1 "That sounds stupid. Why in the world would she assume the form of an elf?"

    initiate1 "If she was a witch, she'd have turned you into a toad already."

    initiate1 "Although she might have, for all we know. I'm not sure we'd be able to tell the difference..."

    templar "Quiet!" with vpunch

    templar "Quit your yammering, initiates, it is unfit for devouts of Arios."

    templar "Witch or not, at least it is obvious that she is an elf. There's no denying that she deserves her fate, on account of that alone."

    templar "Arios wastes no mercy on pointy-eared fiends."

    gizel "What... What are you going to do to me?"

    templar "Witch or spy, there is only one way to properly wash away your sin. You shall burn at the stake."

    play sound s_scream

    gizel surprise "B... Burn!" with vpunch

    templar "Yes."

    gizel shy "Oh no... *sob*"

    "The girl starts to cry. You feel a surge of pity."

    if result == "warn":
        you "Wh... What about me?"
        templar "Of course, it is only proper that your accomplice will join you on the pyre."
        you "What?!?"

    if story_flags["elves"] == "dislike":
        $ reaction = "wait"
        you "Come on, that will be one less elf. No need to lose sleep over that."
    elif result == "denounce":
        you "Wow, that's a little harsh, isn't it? I mean, maybe there should be a trial..."

        templar "Quit your meddling, citizen, or you'll be joining her."

        you "..."

    if not story_flags["elves"] == "dislike":
        menu:
            "What do you do?"

            "正当防卫" if result == "warn":
                $ reaction = "fight"

                you "You think I'd fall to a bunch of braindead bigots like you? I can crush you with my bare hands!"

                hide gizel with dissolve
                show templar with dissolve

                templar "What?"

                play sound s_sheath
                pause 0.2
                play sound s_sheath
                pause 0.1
                play sound2 s_sheath

            "袖手旁观"  if result == "warn":
                $ reaction = "wait"

                you "Damn, I'm unarmed and defenseless... There's nothing I can do for now..."

            "掩护她" if not result == "warn":
                $ reaction = "fight"
                $ MC.good += 1

                if result == "wait":
                    "Leaving the safety of your hideout, you show yourself, moving towards the group of warriors."

                "Taking a step forward, you challenge the head templar with a powerful voice."

                you "You! Leave the young elf alone! I won't let you bully a defenseless woman before me."

                hide gizel with dissolve
                show templar with dissolve

                "The templars turn to face you. Their leader puts his hand on the hilt of his sword."

                templar "Are you out of your mind?"

                you "Templar! Face me in a honourable duel, one on one. If I defeat you, you shall let us go."

                templar "..."

                templar "Ha! I don't think so. Men, get him."

                play sound s_sheath
                pause 0.2
                play sound s_sheath
                pause 0.1
                play sound2 s_sheath

                you "Uh-oh."

            "继续观察" if not result == "warn":
                $ reaction = "wait"
                $ MC.neutral += 1
                you "There doesn't seem to be anything I can do. After all, discretion is the better part of valor. Let us see how it all unfolds..."

    $ renpy.block_rollback()

    if reaction == "fight":
        menu:
            "What will you do?"

            "与他们正面对抗":
                jump templar_fight

            "用魔法攻击他们":
                jump templar_magic

    else:
        jump gizel_rape

label templar_fight:

    $ renpy.block_rollback()

    if result == "warn":
        $ diff = 6
        $ raw = True

    else:
        $ diff = 4
        $ raw = False


    # Run challenge
    call challenge("fight", diff, raw=raw) from _call_challenge_32 # result is stored in the _return variable
    $ r = _return

    if r:

        "Swift like a cobra, you hit the nearest guard through the slit of his helmet."

        play sound s_punch

        initiate "Gurgh!!!" with hpunch

        "Before he has a chance to recover from the blinding pain, you wrestle his weapon off just in time to parry an incoming blow."

        you "I've faced twice as many men in battle and still won! Let me show you how it's done!"

        play sound s_clash

        pause 0.3

        play sound2 s_sheath

        pause 0.1

        play sound s_sheath

        hide initiate1 with pixellate

        "Aiming with fearful precision at the joints in the initiate armors, you use the stolen weapon to sever the tendons of a couple of them,
         sending them crumbling into the dust with pathetic cries."

        templar "Damn this man, he fights with the strength of a demon! Get him!"

        play sound s_sheath

        pause 0.3

        play sound2 s_wscream

        hide initiate2 with pixellate

        "Soon, another initiate bites the dust, and the others begin to back away from you. You turn to face their leader."

        you "Now, if you don't mind, I will have this duel."

        templar "Ugh..."

        "Silence falls over the field of battle for a short instant. Suddenly, a high-pitched, wicked laugh bursts behind you."

        play sound s_evil_laugh

        gizel smirk "MUHAHAHAHAHAHAHA!!!" with vpunch

        "The elf girl lets out a cruel, maniacal laugh, totally out of character from how she was behaving before."

        you "What?"

        jump gizel_attack

    else:

        play sound s_dodge

        "The nearest initiate tries to stab you, and you nimbly jump out of the way."

        show initiate behind initiate1 as initiate3 at left:
            xpos -0.15
        with dissolve

        you "Uh-oh..."

        show initiate as initiate4 at right:
            xpos 0.9

        with dissolve

        "You are quickly surrounded."
        play sound s_sheath

        pause 0.2

        play sound s_sheath

        pause 0.2

        play sound2 s_dodge

        you "That... That was close... *sweat*"

        templar "Surrender, now! Or we'll gut you!"

        "Taking a desperate look around you, you see half-a-dozen armored warriors closing in from all directions. There's no way you can win this."

        you "Fine, I surrender."

        "You raise your hands."

        play sound s_punch

        you "OUCH!!!" with vpunch

        "Coming from behind you, one of the initiate hits you in the back of the head with a mailed fist. You see stars, and fall on your knees."

        templar "Stay on your knees, wretch. You have more than earned your right to join the witch on the pyre."

        jump gizel_rape

label templar_magic:

    $ renpy.block_rollback()

    if result == "warn":
        $ raw = True

    else:
        $ raw = False

    # Run challenge
    call challenge("control", 4, raw=raw) from _call_challenge_33 # result is stored in the _return variable
    $ r = _return

    if r:

        play sound s_spell

        "A gust of wind engulfs the clearing, blowing dust in the face of the warriors."

        play music m_wind

        initiate "Ah!!!"

        you "Feel the wrath of the harem shake!!!"

        "The ground rumbles as the warrior are shaken like dry leaves in the wind, unable to fight or move."

        templar "What foul sorcery is this!"

        "Keeping the spell up, you think about your next move."

        you "If I lower my guard to cast an offensive spell, they'll attack me again..."

        "Trying to move in spite of the quaking ground and stormy wind, the templar creeps towards you with his sword drawn."

        you "Quick, think of something..."

        stop sound fadeout 3.0

        play sound2 s_evil_laugh

        gizel smirk "MUHAHAHAHAHAHAHA!!!" with vpunch

        "The elf girl lets out a cruel, maniacal laugh, totally out of character from how she was behaving before."

        you "Uh... What?"

        jump gizel_attack

    else:

        "Raising both hands towards the skies, you start your incantation."

        you "By the powers of the heavens..."

        templar "He's a magic user! Stop him!"

        "Reaching for a dagger at his side, the knight sends it swirling towards you."

        play sound s_dodge

        pause 0.4

        play sound s_punch

        you "OUCH!!!" with vpunch

        "The hilt of the dagger hits you square in the forehead, making you fall over in the dust, and forget all the words of the spell you were casting."

        "When you come back to your senses, half-a-dozen blades are pointing at you from all directions."

        templar "Tie the sorcerer up! He'll join his kin on the pyre."

        jump gizel_rape

label gizel_rape():

    stop music fadeout 3.0

    play music m_gizel fadein 3.0

    $ NPC_gizel.raped = True

    if reaction == "fight":
        hide templar
        hide initiate3
        hide initiate4
        with fade

        show gizel shy with dissolve

    gizel shy "So... You're going to burn me at the stake? *shiver*"

    templar "Absolutely. This is what Arios commands."

    gizel soft "I see... Don't you need, uh, firewood, then?"

    templar "Hem. That's a good point."

    templar "Men! Gather some firewood, on the double."

    initiate1 "B-but, brother knight... We didn't bring any..."

    initiate2 "And the closest forest is at least five miles away..."

    templar "Arios damn you useless scum!"

    templar "Fine, we'll just burn her on a garbage pile, then."

    gizel shy "Oh..."

    initiate1 "But boss, think of the smell... I can hardly stand it now and nothing is burning..."

    initiate2 "Yeah, it will take months to wash it away from our clothes! We might even have to {i}{b}take a bath{/b}{/i}!"

    templar "Damn, I didn't think about that."

    templar "Fine! We'll just hang the witch, then."

    initiate1 "Aye, sir, good idea."

    initiate2 "Yeah, I guess that'll do."

    gizel shy "Err, sorry, mister... But I think there's going to be a problem."

    templar "You speak again! What is it this time?"

    gizel soft "Well, uh... This is the junkyard... There isn't a tree to hang me from for at least a couple of miles."

    gizel shy "And my feet hurt..."

    templar "Damn you evil woman! Only a witch could have chosen a place where one cannot find a honest branch to hang her from!"

    templar "Fine! Then we'll just stick a sword through your innards and be done with it! Initiate!"

    initiate1 "Well, uh... Isn't it bad luck to strike the killing blow against a witch?"

    initiate1 "I mean, er, why don't you do it? The honor should be yours, brother knight."

    templar "Er... Ahem... Well, I, uh, I just had my sword oiled, so... I don't want to dirty it, you know..."

    gizel shy "Actually... Don't you think such a death lacks panache?"

    gizel soft "This isn't fit for a glorious witch killing, don't you think? If I were a witch, I mean, which I most certainly am not..."

    initiate2 "She speaks the truth... I ain't never heard of a witch being killed with a sword to the gut..."

    templar "You initiates are driving me crazy!!! What in Arios's name do you suggest we do to kill that devil she-elf, then?"

    initiate1 "Well, uh, we could stone her..."

    initiate1 "But, uh... I've never been really good at aiming, though."

    initiate2 "Oh, I know! We could quarter her! That's always some good fun!"

    initiate1 "Right! Do we have any horses?"

    initiate2 "Well, uh, no... But I saw a couple donkeys on the way here..."

    initiate1 "Donkeys? Are you daft? No one's ever heard of a witch being quartered by donkeys!"

    initiate2 "Well, she's got a small body, so... Besides, you never know until you try!"

    initiate1 "I swear, you must be glad Arios has a fondness for the dimwitted, that makes you one of his favorites I'm sure..."

    initiate2 "Nothing I suggest is ever good enough for you, is it?"

    initiate1 "That's just because everything you suggest is so damn dumb!"

    gizel shy "Gentlemen, stop quarrelling, please..."

    initiate1 "Oh, shut it, lass!"

    initiate2 "Yeah, have some dignity here. It's yer own death we are discussing."

    play sound s_sigh

    gizel "I know, ser, I know... But..."

    gizel shy "Well, I don't care what you do to me."

    gizel soft "At least it won't be as bad as in the Old Days..."

    initiate1 "The... The Old Days?"

    gizel shy "Aye... In those days, witch hunters were rough, feral men from the Western marches... They weren't much for talking or debating..."

    gizel "Whenever they caught a witch, they did the most horrible things imaginable to her..."

    initiate2 "What... What was that?"

    gizel blush "Well, since you ask..."

    gizel shy "They had their way with her, all together at the same time, raping her mercilessly until she died from exhaustion..."

    initiate1 "They did that?"

    gizel "Oh, yes... Not only did they ravish her pussy, but they also violated her throat and asshole as well... Or so I heard."

    gizel "They wouldn't stop until she was completely broken and left her to die from thirst and exhaustion..."

    initiate1 "*gulp*"

    play sound s_sigh

    gizel blush "It must be said that those men also had very large cocks, much larger than those found today among city-dwellers... Being raped by those men must have been excruciatingly painful... Hmm..."

    play sound s_ahaa

    gizel shy "So, all in all, I'm happy that you are not anything like those men, and that you will simply burn or quarter me..."

    initiate2 "You are?"

    gizel "Well, I sure am..."

    gizel blush "I will die knowing that my precious virginity is left untouched, and that my tight, virgin, teenage pussy has never been fucked by anyone..."

    "Someone coughs."

    gizel blush "And it's just as well that no one has ever rubbed their dirty, dirty dicks upon my fair, smooth virgin skin..."

    initiate "*g-gulp*"

    gizel "... or shot their disgusting cum all over my fair, silky hair..."

    "All the men are staring at her intensely now, detailing her petite, scantily-clad elf body..."

    play sound s_mmmh

    gizel shy "And no one will ever squeeze my small teenage tits until my nipples stand erect and pinch them, mmmh... It's for the best really, they're so sensitive..."

    "Having been silent and brooding for some time now, the head templar suddenly lifts his head."

    templar "Men, I think I just got an idea."

    initiate1 "Me too..."

    initiate2 "I think I did too... Wait, what are we talking about?"

    templar "We are going to rape this elf spy-witch to death."

    initiate1 "Aye aye, sir!"

    initiate2 "We... Really?"

    templar "Why, yes... We are only doing it for the eternal glory of Arios, of course."

    initiate1 "Of course."

    initiate2 "We are?"

    play sound s_surprise

    gizel surprise "What? Noooo!"

    gizel shy "How... However did you get that idea, I wonder..."

    templar "Muhahaha!"

    templar "Your evil tongue betrayed you, you foolish witch! Now, let us put that tongue to better use..."

    if result == "denounce":
        you "Wait! When are we gonna discuss my reward, templar?"

        templar "Shut up, citizen, and stand back. This is divine business, and must be properly attended to by men of the true faith. It does not concern you."

        scene bg gizel_rape1 with fade

        "Rolling your eyes, you stand back with your arms folded as the men take out their dicks and rush to undress the elf girl."

    else:

        scene bg gizel_rape1 with fade

        "Unable to do anything, you just watch as the poor girl is pushed to the ground and the men gather around her, taking their dicks out."

    play sound s_scream_loud

    gizel upset "Nooo!!!"

    "The girl yells as the men tear apart her minimal clothing, revealing her small tits and perky nipples."

    play sound s_scream

    gizel "Hnnn! Aaah!"

    "Some of the men hold her down in the dirt, while another starts playing with her erect nipples, pulling and twisting them."

    play sound s_scream

    gizel "Aaaah! Stop!!!"

    "An initiate positions himself under her, another one on top of her. Together, they take turns running their shafts along the silky fabric of her panties, rubbing her pussy in the process."

    initiate "Hold this for me will ya?"

    "Another initiate forces her to grab his dick and jerk him."

    play sound s_scream_loud

    gizel "Noooo!!! Let me go!!!"

    templar "The lady protests too much, methinks."

    scene bg gizel_rape2 with dissolve

    "Holding the elf girl's head back, the templar shoves his hard, bulging cock into her mouth, muzzling her."

    play sound s_sucking

    gizel "Ngggh!!!"

    templar "Muhahahaha!"

    templar "Just like I always suspected... The true purpose of all elven sluts is to be a man's cockholder."

    initiate2 "Hey, brother knight, you're having all the fun to yerself!"

    initiate1 "Yeah, let us have some too."

    gizel "NGGGGGGHHH!!!"

    scene bg gizel_rape3 with hpunch

    "Gizel squirms and tries to scream in vain as the initiates take off her panties, and immediately proceed to force their hard dicks into her pussy and asshole simultaneously."

    initiate1 "Ooooh, that's good..."

    initiate2 "Her little asshole is sooo tight..."

    play sound s_scream

    gizel "Not my ashhhole... Ngh..."

    "Not to be undone, the rest of the guards start rubbing their dicks on Gizel's exposed body and smooth hair."

    play sound s_scream

    gizel "Hmmmpf!!!" with hpunch

    play sound s_moans_quiet

    "In spite of her situation, Gizel is blushing visibly. Her pussy and ass seem to expand to accommodate the men's dicks without any problems too,
     although she is so thin, you can see a bump in her belly every time the cock in her pussy thrusts forward."

    you "This must be the legendary sex drive of the fairy people..."


    "After a few minutes, it seems the pressure is building up as the warriors are turned on by the young elf's cries of pain and pleasure."

    scene bg gizel_rape4 with dissolve

    "Pulling Gizel's head backward, shoving his cock deeper and deeper into her throat, the templar is the first to reach his limits."

    templar "Take that, you dirty witch slut! Drink every last drop of mine holy cum!"

    play sound s_moans

    scene bg gizel_rape5 with doubleflash

    gizel "NGGGGGHHH!!!"

    with flash

    "The templar explodes into the young girl's mouth, shooting a huge load of sticky cum. With his dick firmly lodged deep down her throat,
     Gizel has no choice but to gulp it all down."

    gizel "NGGGH... NGAH... *cough* *cough*"

    "Seeing the girl with cum overspilling out of her mouth and even nostrils, the other guards aren't long behind their boss."

    with flash

    initiate "HAAAAAAA!!!"

    play sound s_orgasm_young

    with doubleflash

    gizel "AHAAAA!!!"

    scene bg gizel_rape6 with dissolve

    "One after the other, the Arios worshippers reach their limit and shoot their load, inside and all over the elf girl's sweet body."

    initiate "I'll blow this load into your mouth, bitch!"

    scene bg gizel_rape7 with flash

    gizel "NGGGH!"

    initiate "Aaah! Swallow it, slut!" with doubleflash

    gizel "*gulp* *gulp* *cough*"

    scene bg gizel_rape6 with dissolve

    "After the initiate takes out his cock, Gizel is left panting and gasping for air, her pale, petite body utterly defiled by the cum of half-a-dozen men."

    play sound2 s_aaah

    gizel blush "Aaaah..."

    "At this very instant, you are puzzled to see the look on her face. She looks... Happy? Serene?"

    initiate1 "Oh... I feel so... lightheaded..."

    initiate2 "Me too..."

    templar "What is it... My... My head..."

    play sound s_evil_laugh

    gizel smirk "Muhahahaha! Men are such despicable, predictable animals..."

    you "Wh-What?" with vpunch

label gizel_attack():

    stop music fadeout 3.0

    play sound s_crash
    scene black with flash

    "A flash of light blinds you for a second, and a gust of ghoulish energy sweeps you off your feet."

    play music m_danger_loop fadein 3.0

    play sound s_crash
    with vpunch

    show bg gizel_attack1 with circleout

    you "What... What's going on???"

    "Gizel is hovering into mid-air, in the middle of a sphere of dark energy whose crackling is making your hair stand up on end."

    "The shy, girly persona you witnessed before is no more. Instead, she sports a domineering, confident sneer on her face."

    play sound s_evil_laugh

    gizel smirk "You weak and pathetic humans, you are fools, just like all those who came before you! Prepare to vanish into the nothingness you should never have escaped from..."

    templar "I... I can't move..."

    initiate "What is... happening..."

    play sound s_crash loop
    show bg gizel_attack1 at quake

    gizel angry "KAAAAA..."

    show bg gizel_attack2 at quake with dissolve

    gizel "MEEEEE..."

    you "What... What's this?"

    show bg gizel_attack3 at quake with dissolve

    gizel "HAAAAAA..."

    if MC.get_spirit() >= 3:
        you "It's a vampiric spell! I must run!!!"

    else:
        you "It's... Magical mumbo-jumbo! I must run!!!"

    show bg gizel_attack3 at quake with dissolve

    gizel "MEEEEEEEE..."

    you "AAAAH!"

    "Bolting away, you desperately duck behind the wreckage of an old carriage."

    "The Arios worshippers make pathetic efforts to get up and follow you, but it's like they have no energy left..."

    templar "No..."

    show bg gizel_attack4 with dissolve

    play sound s_lightning

    gizel "BOOM!" with vpunch

    play sound s_wscream

    pause 0.2

    play sound2 s_wscream

    pause 0.1

    play sound3 s_wscream

    with vpunch

    play sound s_spell

    "Terrible screams come out of the men as their souls are sucked out of them by the dark spell. Their bodies shrivel and dessicate, leaving only
     empty armors and dry bones where the warriors once laid."

    "All the while, you keep cowering behind your precarious cover, with your hands on your ears, in an attempt to block out the pathetic screams."

    "When the dark winds finally settle, and your senses return, you find Gizel standing before you."

    stop music fadeout 3.0

    scene bg junkyard with fade
    show gizel smirk with dissolve

    gizel smirk "Ah, a survivor... What should I do with this one?"

    if result == "warn":
        gizel "You're the one who tried to warn me, aren't you? You're not one of those Arios bigots.
                      Your heart was bleeding for a poor little elf, was it?"

        you "Well, uh, yes... I was only trying to help..."

        gizel angry "Shut up! Do-gooders make me sick!"

    elif result == "denounce":
        gizel angry "You're the one who denounced me to those pigs, aren't you?"

        you "Err..."

        gizel smirk "Mmmh, you've got a cold heart, I'll give you that."

    elif reaction == "fight":
        gizel normal "You're the one who tried to defend me, aren't you? Your heart was bleeding for a poor little elf, was it?"

        you "Well, uh, yes... I was only trying to help..."

        gizel angry "Shut up! Do-gooders make me sick!"

    you "..."

    gizel smirk "Anyway. It is rude to prolong your meaningless existence for much longer. I'm sure you'll understand, after the mess you witnessed, I can hardly let you live."

    play music m_danger_loop fadein 3.0
#    show gizel angry with dissolve

#    gizel "Goodbye."

    hide gizel

    show bg gizel_attack1 at quake
    with dissolve

    gizel smirk "KAAAA..."

    show bg gizel_attack2 at quake

    gizel smirk "MEEEEE..."

    scene black
    stop music fadeout 3.0

    you "Wait!!!" with vpunch

    show bg junkyard
    show gizel upset
    with dissolve

    play sound s_sigh

    gizel "What is it again?"

    you "You... You don't wanna do that!"

    gizel smirk "Oh, really? And why is that?"

    menu:
        you "Because..."

        "你不会想和我战斗的":

            you "My name is [MC.name]. I'm a lot tougher than those clowns out there. You don't want to start a fight you can't win."

            $ MC.rand_say(("wr: Before I was a brothel owner, I was a soldier in the war. I killed more elven mages than I can count.",
                           "wz: I'm not just a brothel owner, I'm also a powerful mage, top of my class in Karkyr. You won't have the upper hand in this fight.",
                           "tr: I'm not just a lowlife pimp, okay? I've got a pet dragon. That's right. And he's like, twenty feet tall."))

            if NPC_gizel.raped:
                if reaction == "fight":
                    gizel smirk "Yeah, I noticed how powerful you were, getting your ass handed to you by those dumb Arios cultists... Stop wasting my time!"
                else:
                    gizel smirk "Well, considering you've spent this whole battle hiding behind a pile of garbage, I don't think it will give me too much of a sweat."

                hide gizel
                show bg gizel_attack1 at quake
                with dissolve

                play music m_danger_loop fadein 1.0

                gizel angry "And now, for the big finish!"

                you "AAAAAH!!! Mommy!"

                gizel "KAAAA!!!"

                gizel "..."

                stop music fadeout 3.0

                show bg junkyard at top
                show gizel normal
                with dissolve

                play sound s_fizzle

                gizel normal "Wait, did you say you were a brothel owner?"

            else:
                gizel angry "Hmmm... It's true you fought well..."

                gizel upset "But what do I have to gain from an alliance with you!"

        "我对你还有些用处":

            you "Look, I can be useful to you. I am not one of those Arios bigots. My name is [MC.name], I'm a business man, I own a brothel in town..."

            you "This is Zan, not the wilderness. You need friends who have your back, am I right?"

            gizel shy "F... Friends?"

            you "With benefits. I mean, I'm sure I can get you what you need... Whatever that is?"

#    show bg junkyard with dissolve

    gizel angry "A brothel owner, uh? Let me think..."

    gizel "..."

    gizel "......"

    gizel "........."

    you "Are you done?"

    gizel "Quiet!" with vpunch

    gizel angry "..."

    gizel normal "All right, you're correct. I hate to admit it, but I do need a thrall to do my bidding."

    you "Well, er, I didn't say..."

    gizel angry "KAAA..." with vpunch

    you "Of course, sure, haha, whatever you say!"

    gizel smirk "That's better."

    gizel normal "Then, I have a task for you. It is of the utmost importance that you don't fail me."

    gizel upset "If you do..."

    you "I won't, I won't, don't worry! Haha..."

    gizel normal "Good."

    gizel angry "Those damn templars have found my hideout once. It's only a matter of time before they come back with reinforcements."

    gizel "This place is no longer safe."

    gizel normal "So, in exchange for your life, you will find me a secure hideout."

    gizel "I need somewhere private, away from prying eyes... I have too many neighbours here, and I can't change them all into slugs."

    play music m_gizel fadein 5.0

    menu:
        gizel "Do that for me, and you may live."

        "Can I ask you a few questions?":

            play sound s_sigh
            gizel upset "If you must."

            label gizel_questions_menu():
                menu:
                    "还未请教姑娘芳名?":

                        you "Who are you?"

                        gizel normal "Why, I'm Gizel, of course."

                        gizel "You might also know me as the White Witch of the North, the Deathly Bride, or Gizelinde the man-eater."

                        gizel "I don't actually eat man meat though."

                        gizel smirk "Or rather, I do, but not in {i}{b}that{/b}{/i} way... *smirk*"

                        you "Never heard of you."

                        gizel upset "Humph. That's just a testament to your appalling cluelessness and ignorance!"

                        gizel normal "I have roamed this world for a very long time, lived a longer life than you could ever dream..."

                        you "Well, it is true that elves have longer lifespans..."

                        play sound s_evil_laugh

                        gizel smirk "Elves? Don't make me laugh."

                        gizel angry "I despise my cutesy relatives, what with their tree-hugging lifestyle and their syrupy morals! I hate the little fuckers."

                        gizel "I am a Drut, a pale elf, last of a breed that vanished centuries ago."

                        gizel smirk "I have no more in common with those moronic wood elves than a white shark with a goldfish."

                        gizel normal "No, if I have lived to be this old, never-aging, the reason is much more elegant and simple: sorcery."

                        you "Oh... H... How?"

                        gizel smirk "Well, it's quite simple really. A bath every fortnight in virgin blood does the trick quite well."

                        you "V-virgin blood???" with vpunch

                        play sound s_evil_laugh

                        gizel smirk "Ha! You should see the look on your face!"

                        gizel normal "Come on, I'm fucking with you. Do you know how {i}{b}rare{/b}{/i} real virgins are in Xeros?
                                     I wouldn't have lasted a year at this rate."

                        jump gizel_questions_menu

                    "你在泽恩做什么?":

                        you "What are you doing here in Zan?"

                        gizel normal "For centuries, I stuck to the wilderness outside of city walls, and it suited me just fine...
                                      After all, my kin used to live high in what you call the Arik mountains, and it was pretty much inaccessible."

                        gizel "But I didn't stay there long. I had my reasons... Anyway."

                        gizel angry "After the fall of the old races, humans began to multiply and spread like roaches... It was harder and harder to find a
                               quiet place to live and feed."

                        gizel upset "And now, there's the damn war. Arios bigot crusaders swarm the land, eager to find elves to string up and villages to loot on the way to the front line,
                               trying to delay real fighting for as long as possible..."

                        gizel normal "Life in the country went from being hard to impossible. I thought I might as well hide in plain sight, in the big city..."

                        gizel angry "That didn't work out so well."

                        jump gizel_questions_menu

                    "你对他们做了什么?":

                        you "What... What did you just do to those men out there?"

                        gizel normal "Well, I just used the Kamehame-boom, an ancient bolt of doom technique taught to me by my master..."

                        gizel smirk "Beginner's stuff, really."

                        if NPC_gizel.raped:
                            you "No, I mean, you did something to them before that... They couldn't move or think."

                            gizel smirk "Oh, that? I was just feeding off their life energy..."

                            you "Feeding? *gulp*"

                            gizel smirk "Yes, of course! That's how I keep my youthful good looks..."

                            gizel blush "I feed off other creatures' sexual energy, by absorbing their bodily fluids."

                            you "You mean... Like a succubus?"

                            gizel upset "Don't compare me to those crass, unrefined bimbos!"

                            gizel angry "I know better than to kill my prey from exhaustion, unless I want to."

                            gizel blush "I drained those assholes empty because it served my ends... But I could just as easily have taken only a little bit of energy from them,
                                          and they wouldn't have noticed a thing."

                            gizel "I've got centuries of practice."

                            you "But... If you're so good, why did you let them catch you in the first place?"

                            play sound s_evil_laugh

                            gizel smirk "Oh, come on! It's because it was more {i}{b}fun{/b}{/i} that way, of course!"

                            you "F... Fun? You like being raped?"

                            gizel blush "They are so many things I like, you have no idea..."

                            gizel blush "But anyway, I feel so refreshed now! Nothing beats a good shower of fresh cum in the morning."

                            you "Wait a minute. You were able to live for centuries just by having sex?"

                            gizel smirk "Why, sure. All I need to do is to have sex every day, and plenty of it."

                            you "Isn't that hard?"

                            play sound s_evil_laugh

                            gizel smirk "Absolutely not! You'd think it would get boring, but it only gets better and better... You just have to be a little creative."

                            you "I see... I think."

                            you "Could you..."

                            you "Could you teach me how to live forever by having sex every day?" with vpunch

                            gizel normal "No."

                            you "Aw..."

                            jump gizel_questions_menu

                    "没有要问的了":
                        pass

        "Fine":
            pass

    you "Fine, I'll help you find a place to lay low."

    if story_flags["farm found"]:
        you "In fact, I think I know just the place."

        gizel surprise "What? You do?"

        you "An old farm. It's deserted, it's quiet, it's in a beautiful setting in the country, yet close to the city. There's only one small problem..."

        gizel upset "What is it?"

        you "It's haunted. A powerful spirit, soul-eating and all."

        play sound s_evil_laugh

        gizel smirk "Oh, it's just {i}{b}that{/b}{/i}! Hahaha!"

        gizel normal "You scared me for a second. I thought there were cockroaches."

        you "You think you can take care of it?"

        gizel smirk "Don't insult me. I've summoned, killed, tamed and fucked more demons than you can shake a tentacle at."

        you "Fine. I'll show you the way, then. We can meet there later."

        stop music fadeout 3.0

        scene black with fade

        $ story_add_event("farm_go_with_gizel")

        "Meet with Gizel at the farm."

    else:

        gizel upset "You better. Or I'll be moving to your brothel, and turn you into wyrm food!"

        you "Aw..."

        gizel smirk "See you soon, then."

        stop music fadeout 3.0

        scene black with fade

        $ story_flags["gizel met"] = True

        "Find a quiet place for Gizel to stay at."

    return

label farm_found_a_place():

    scene bg junkyard with fade

    "You came back to the junkyard to meet with Gizel the witch."

    play music m_gizel fadein 3.0

    scene black
    show bg gizel_room at top
    with fade

    show gizel normal at center with dissolve

    gizel "Ah, it's you."

    gizel upset "I was beginning to lose patience... Actually, I was about to cast a little spell to make you hurry, such as Eldrich's Curse of the Crippling Blue Balls..."

    you "No need for that, hahahaha..."

    you "Listen, I found the perfect place for you to lay low."

    gizel surprise "Really? You did?"

    you "An old farm. It's deserted, it's quiet, it's in a beautiful setting in the country, yet close enough to the city."

    you "There's only one small, minor problem..."

    gizel upset "Uh? What is it?"

    you "Well, er... It's haunted. A powerful spirit, soul-eating and all."

    play sound s_evil_laugh

    gizel smirk "Oh, it's just {i}{b}that{/b}{/i}! Hahaha!"

    gizel normal "You scared me for a second. I thought there were roaches."

    you "Oh. You think you can take care of it?"

    gizel smirk "Don't insult my talent. I've summoned, banished, tamed and fucked more demons than you can shake a tentacle at."

    you "If you say so... I'll show you the way, then. We can meet there later."

    stop music fadeout 3.0

    scene black with fade

    "Meet with Gizel at the farm."

    $ story_add_event("farm_go_with_gizel")

    return

label farm_meet_goldie():

    stop music fadeout 3.0

    "Needing to escape from the sounds and fury of Zan for a moment, you decide to take a relaxing stroll across the farmlands outside the wall."

    play music m_nature fadein 3.0

    scene bg farmland with fade

    you "Finally, some peace and quiet."

    "As you cross the village, you see an old stone road leading to a remote corner of the farmlands."

    you "I'll go up this old road. Should be even nicer and quieter there."

    "As you progress along the road, farmhouses become few and far between. Eventually, you end up around a visibly neglected and decrepit area."

    you "It's like there's no one around here... Is it all abandoned?"

    "You fail to meet anyone for a long while. As you think about turning back, you finally notice a couple of figures standing inside an unkempt garden, looking sadly at each other."

    scene bg goldie_hug with fade

    man "Sister, I am so sorry."

    goldie "It's not your fault, little brother. I understand completely."

    man "I have failed you, and I have failed father..."

    goldie "Don't say that. Father wouldn't have wanted you to live your life miserable and unhappy."

    goldie "Go out into the world, and become the man you want to be..."

    man "But what about you, sister? How will you manage here, all by yourself?"

    goldie "Where there's a will, there's a way... Remember what father used to say? Besides, it will be easier to feed just the one of us with what little money I can get from the ranch..."

    goldie "Don't you worry about me. I'll be fine."

    man "Goldie..."

    $ goldie_name = "Goldie"

    man "You're always so brave. I wish I was, too..."

    "He sighs."

    man "But I can't stand this place anymore. I have to go."

    goldie "I know."

    goldie "Godspeed, brother."

    man "Take care of yourself, big sister."

    "The man wipes his tears. After hugging his sister one last time, he turns and rushes past you without looking back. He's carrying a worn rucksack which seems to contain all his belongings."

    scene bg farmland

    show goldie at center
    with dissolve

    goldie "And there he goes... He was the last of them."

    "Although she was putting on a strong face before, the woman seems about to burst into tears now. Something about her disturbs you, and you decide to talk to her."

    you "I'm sorry to interrupt, I couldn't help but overhear. Are you all right, my lady?"

    "The woman barely registers your presence, but responds as if talking to herself."

    goldie "Here goes my little brother, who was the last to help me on the ranch..."

    goldie "It's just me and the animals now, and at the rate they're dying off, soon it will just be me."

    "Trailing off, she seems to notice you for the first time."

    $ menu_answers = defaultdict(bool)

label farm_meet_goldie_menu():

    menu:

        goldie "What is it?"

        "你的弟弟为什么离开了?":

            you "Why is your brother leaving?"

            goldie "He couldn't take it anymore. The hard work, the poverty, and above all, the constant fear, the nightmares..."

            goldie "I don't blame him."

            you "Nightmares?"

            goldie "Yes. And worse. It's the curse, you see..."

            $ menu_answers["curse"] = True

        "你不能雇佣帮工吗?":

            you "Can't you just hire more people?"

            goldie "I don't have the coin. Besides..."

            you "What?"

            goldie "They'd run away. Just like the others. They all did."

            you "Away from what?"

            goldie "The terrible curse that struck this place."

            $ menu_answers["curse"] = True

        "你的动物为什么会死?":

            you "Your animals are dying? Why?"

            goldie "All the animals have taken ill. Pig, cow, chicken, it matters not. Even cats and dogs know to avoid this area."

            you "What's going on with them?"

            goldie "They are restless and terrified, and they won't go one step towards the old farmhouse."

            goldie "Their milk turns sour. They have stopped reproducing, and all those that were pregnant miscarried."

            goldie "Some died in the night, from sudden heart attacks. The doctor said they died of fright."

            goldie "I have sold all of the animals that were still healthy... Now I am left with a few sickly ones that might soon succumb to this evil."

            play sound s_sigh

            goldie "At this rate, I won't have any livestock left by the end of the season."

            $ menu_answers["farm"] = True

        "诅咒?" if menu_answers["curse"]:

            you "What was that about a curse?"

            goldie "It's the old farm. A terrible place, forsaken by the gods."

            goldie "After my father passed away, we discovered it belonged to our family on some old, parched document. My eldest brother thought we had struck gold."

            goldie "But the property had been locked shut and tight for as long as anyone could remember."

            goldie "My big brother wouldn't heed the superstitious warnings of some of the older servants. One night, he took an axe and broke in."

            goldie "I don't know what he found in there. After an hour, he ran out, his eyes wild, raving like a mad man. His hair had turned completely white."

            you "Wow..."

            goldie "We couldn't get anything out of him, only that the place was cursed. He grabbed a barrel of lantern oil, and before anyone could stop him, he ran away into the night."

            goldie "He perished in the fire that engulfed the farm that night. I can still hear his screams echoing in the night, chilling our whole family to the bone."

            you "..."

            goldie "The next day, the farm was still standing. The grass outside was thoroughly burned, but the building was left untouched."

            you "Magic..."

            goldie "Foul magic at work, for sure. Since then, the few that have dared enter it haven't returned, or came out frightened out of their mind."

            goldie "We would have been content to leave this cursed place alone like we did before... But {i}{b}something{/b}{/i} stirred when my brother cracked it open... And it's been
                    a blight on the crops and cattle around the farm ever since."

            goldie "Even humans fall victims to it. The night terrors, the hallucinations..."

            goldie "Several of my people went insane. The rest ran off when they got too scared, or when I couldn't pay them anymore."

            you "But you remain?"

            goldie "This is my father's land. I am the head of this family now. What would I do out there? Become a beggar, or a whore?"

            goldie "No way."

            goldie "I'll keep working twice as hard. Things could improve. I have to keep hope."

            $ menu_answers["farm"] = True
            $ menu_answers["help"] = True

        "这间农场怎么了?" if menu_answers["farm"]:

            you "What is this 'farm' you speak of?"

            goldie "It's the large compound behind me. You can see it in the distance, across the fields."

            goldie "It is home to something so dark and evil that it is felt even from here. The land is dying from it."

            you "Dying?"

            goldie "Men and animals lose their minds around here. Most people have run off to take their chances elsewhere, like my little brother just did. Perhaps I should run too..."

            you "But who lives there? Who built it?"

            goldie "It's been standing for as long as anyone could remember, really. There were always stories, though..."

            goldie "The old folks didn't like this area. Forbade us kids to go near it."

            goldie "As for who or what lives there, your guess is as good as mine."

            you "Hmm."

        "也许我可以帮到你?" if menu_answers["help"]:

            you "What if I helped you lift this curse?"

            goldie "Well... Many have tried before."

            goldie "Months ago, I advertised that I would give the farm and its surrounding area to anyone who could lift the curse."

            goldie "For a time, that brought all sorts of adventurers here, who wanted to try their luck. For a time..."

            goldie "But I've run out of adventurers. And the curse still stands."

            if MC.get_alignment() == "good":
                you "I will give it a try. I don't need a reward. I've got a weak spot for damsels in distress."

                goldie "Will you? Then, I will make you the same offer. It's only fair."

                you "Let's not get ahead of ourselves. First we have to solve your problem."

            elif MC.get_alignment() == "neutral":
                you "Not true. You still have me... Would you cut me the same deal if I tried?"

                goldie "You? Why, of course."

                goldie "Provided you manage to drive this curse away, which I doubt... Sorry."

                you "We won't know until we try."

            else:
                you "Risking one's hide and mind for a run-down piece of rubble isn't really worth it, in my opinion."

                goldie "But... I have naught else to give..."

                you "Hmm... We'll see about that."

                "You take a long, appreciative look at her well-rounded shapes, making her squirm uncomfortably."

            goldie "Anyway, how do you expect to solve the mystery of this place?"

            $ MC.rand_say(("wr: There's nothing that can't be solved with a few inches of steel in the gut, I always say. Let me take care of it.",
                           "wz: I took a class in 'curse and debuff management' at Karkyr University, back in the day... I know my way around these things.",
                           "tr: I talk my way around tricky situations all day... If there's something in that farm, perhaps I can cut a deal with it?"))

            goldie "I hope you're right..."

            goldie "I am Goldie, by the way."

            you "I am [MC.name]."

            stop music fadeout 3.0

            goldie "[MC.name], the farm is this way. Please, stay safe."

            call farm_exorcism_attempt() from _call_farm_exorcism_attempt

            return

    jump farm_meet_goldie_menu


label farm_exorcism_attempt():

    scene black
    show bg haunted_farm at top
    with fade

    play sound s_creak

    you "This place {i}{b}is{/b}{/i} creepy."

    "The farm's insides are full of dust and cobwebs. You expected as much."

    "Walking slowly through the rubble, you see the remnants of the farm's facilities: a large pig stall, stables and pens for the animals, an old toolshed..."

    you "Nothing out of the ordinary, I guess. Wait... What's this?"

    play sound s_mystery

    "A large hole is gaping in the ground. You can't say that this was bored with any human tools."

    you "It's like something... Bored through the earth and burst out here..."

    "You take a look into the dark hole, trying to shed some light on what's inside with your torch. A strong, musky stench is emanating from the hole."

    you "Weird..."

    "The strange hole seems to lead to a lower cave... Inside, the walls seem to be bulging and oozing some king of sirupy liquid, although the flickering of your torch could be playing tricks on your imagination."

    play sound s_maniacal_laugh

    "???" "Muhahahaha"

    play music m_demons fadein 3.0

    you "What... What was that?"

    "???" "Ah... At last... A visitor..."

    you "Sh... Show yourself!"

    show spirit at top:
        alpha 0.8
    with blinds

    spirit "Booh."

    play sound s_wscream

    you "Aaah!" with vpunch

    you "Who... What... Who the fuck are you?"

    spirit "I am Varnoshi the soul-eater..."

    spirit "I am the hungry catcher, escaped from the seventh hell, spawn of Wargagath..."

    play sound s_maniacal_laugh

    spirit "Careless stranger... Prepare to be my next meal!"

    you "Dream on!" with vpunch

    menu:
        "What do you do?"

        "拿出武器攻击它":

            play sound s_sheath

            you "En garde!"

            play sound s_dodge

            with hpunch

            pause 0.5

            play sound s_dodge

            with vpunch

            "Striking the spirit with precision, you are dismayed to see your blade pass right through it, without doing any damage."

            spirit "Muhahaha, worm! You can't hope to defeat me with your petty mortal weapons!"

        "吟唱咒语攻击它":

            play sound s_spell

            you "Eat that, spawn of whatsisname!"

            play sound s_fire

            "Casting a powerful fireball right into the spirit's face, you are dismayed to see it dissipate around the fiend without doing any damage."

            spirit "Fool! I exist in an ethereal plane that you cannot hope to reach with your amateurish powers..."

    $ MC.rand_say(("sh: Shalia guard me...", "ar: Arios, guide me into the light...", "ng: Fuck."))

    play sound s_maniacal_laugh

    spirit "Now, let me start my snacking..."

    "You feel a wave of anguish and terror wash over you as a sickening feeling overwhelms you. It is as if an invisible hand was slowly crawling through your insides."

    spirit "Hmm, a strong soul you have... I shall feast on it."

    "You feel as if something is tearing at your very core, trying to sip on your life energy."

    you "NO!!!" with vpunch

    "Overcome by terror and reverting to your animal self, you let your survival instincts kick in."

    you "AAAARH!!!" with vpunch

    "Pushing back at the alien power with all of your remaining strength, you fend off the fiend's attack for a split second."

    "This is barely enough, but it is enough. Flipping around like a frightened deer, you start running for your life."

    spirit "NOOO!!! Come back here!" with vpunch

    stop music fadeout 3.0

    scene bg farmland dusk with fade

    "Bolting out of the farm, you keep running through the field, not slowing down until you reach the relative safety of the village."

    play sound s_maniacal_laugh

    "The evil laugh seems to follow you all the way to the village."

    "Collapsing behind a wall, panting, you take a moment to compose yourself."

    show goldie at center with fade

    goldie "[MC.name]! Are you all right?"

    "Goldie finds you curled up on the ground, still shaking with fear."

    you "I'm... I'm ok. But... I've failed."

    goldie "I guessed as much. Well, at least you tried, and you're back in one piece. That's what matters."

    you "Listen. Just stay put a little longer. I will find a way to put an end to this."

    goldie "Would that you could..."

    you "I promise, ok?"

    $ MC.rand_say(("gd: I'll come back to save you.", "ev: I {i}{b}want{/b}{/i} that farm even more, now.", "ne: A deal is a deal. I'll help."))

    goldie "Really?"

    you "Yes. Meanwhile, keep your head up high."

    scene bg goldie_promise1 with dissolve

    "At first, she doesn't know what to say."

    "She looks at you. She seems to see something in you."

    "And then, she smiles. It's the first time you've seen her smile."

    scene bg goldie_promise2 with dissolve

    goldie "Thanks, [MC.name]. I believe you."

    "She takes your hand."

    goldie "A promise is a promise, ok? Pinky swear."

    you "Haha... Sure."

    goldie "I'll wait for you, then... Come back soon."

    $ story_flags["farm_discovered"] = True

    stop music fadeout 3.0

    scene black with fade

    you "What could possibly lift this curse... Or who?"

    "Find a way to lift the curse on the old farm."

    if story_flags["gizel met"]:
        $ story_add_event("farm_found_a_place")
    else:
        $ story_flags["farm found"] = True

    return

label farm_go_with_gizel():

    stop music fadeout 3.0

    scene bg farmland with fade

    show goldie at right with dissolve

    play sound s_surprise

    goldie "[MC.name]! You have returned!"

    goldie "I'm so glad you didn't forget about me."

    play music m_gizel fadein 3.0

    show gizel at left with dissolve

    gizel normal "So, [MC.name], who's the nerd with the curly hair? One of your girlfriends?"

    goldie "*blush* I'm not..."

    gizel smirk "My, look at her rack! She must put her milkcows to shame..."

    you "Her name is Goldie. She's the one who requested our aid. See that old farm over there?"

    gizel smirk "{i}{b}See{/b}{/i} it? I could feel it a mile from here... It's bustling with dark energy."

    gizel upset "Mortal senses are so blunt! Can't you tell this is a place of power?"

    goldie "A place of power?"

    gizel normal "Yes, my dear cow-loving bimbo... A place of demonic power that exists in several planes at once, home to creatures beyond your wildest imagination..."

    gizel smirk "This is not saying much, of course."

    you "All right, Gizel, enough chatting. Let's move on to the task at hand."

    gizel normal "Humph, sure, why not. Follow me."

    play music m_demons fadein 3.0

    scene black
    show bg haunted_farm at top
    with fade

    show gizel with dissolve

    gizel "You might want to stand back. I can feel the demon that dwells in this place is quite powerful indeed..."

    you "Be careful. He tried to devour my soul the last time I went in there. *shiver*"

    gizel smirk "Don't worry your pretty, empty head about it. I can easily handle it."

    hide gizel with dissolve

    you "I hope she knows what she's doing..."

    scene black with fade

    "Minutes pass, when suddenly you hear a familiar, creepy laugh."

    scene black
    show bg haunted_farm at top
    with fade

    play sound s_maniacal_laugh

    spirit "Ooooh, a cute little she-elf... Let me take a bite off your sweet, innocent soul..."

    gizel shy "Oh, mister demon... What... What kind of nasty things are you going to do to me?"

    spirit "You shall be my next snack... Let me take a little peek at that delicious soul of yours..."

    play sound s_surprise

    gizel blush "Oh no, mister demon-guy... It tickles..."

    spirit "Stay put a minute will ya. Uh?"

    play sound s_mmmh

    gizel smirk "Oh, mister demon, why do you have such a big..."

    stop music fadeout 3.0

    spirit "Wait, what is this? Who are you???" with vpunch

    gizel "Come here... I wanna say hi..."

    pause 0.5

    play sound s_crash

    with vpunch

    pause 0.3

    play sound s_dodge

    with hpunch

    pause 0.5

    play sound s_shatter

    with vpunch

    spirit "Hey! Stay away from me! What... What are you doing?!?"

    play sound s_mmmh

    gizel "Come on, don't be so shy, demon-boy... Show it to me!"

    spirit "Lady, I must protest, we haven't been properly introduced..."

    play sound s_kind_laugh

    gizel blush "Why don't you try me on for size, big boy?"

    spirit "S... S... Stop it already! I said no!"

    play sound s_aaah

    gizel "Oh, come on, don't be a bore... What if I do this?"

    play sound s_roar

    spirit "EEEEEEEK!!!" with vpunch

    "A dark cloud seems to lift from the farm, whirling towards you until a silhouette forms back in front of you."

    show spirit at top:
        alpha 0.8
    with dissolve

    spirit "You!" with vpunch

    spirit "What in the seven fucking hells! And I should know... I've been there!"

    spirit "For thousands of years, I have haunted wild and uncouth places all around Xeros, but this... This is an outrage!"

    spirit "Never has a honest demon such as myself witnessed such... depravity!" with vpunch

    you "Really..."

    spirit "Sir, I do not commend you on your choice of friends!!! This is appalling!"

    you "Well, er, Gizel and I are not, uh, close friends, you know..."

    spirit "I don't care for your silly excuses, I'm out of here! I'm not even going to eat your dirty soul, that's how angry I am!" with vpunch

    spirit "I may be an evil demon, but I have feelings too, you know..."

    you "Well, uh, sorry..."

    spirit "Ha! You may win today, but don't think you will get off this easy!!!"

    spirit "Remember the words of the ancient prophecy... "

    play sound s_maniacal_laugh

    extend "{i}Lutaneth Mot Garazoth!!{/i}" with vpunch

    $ calendar.set_alarm(calendar.time + 1, Event(label = "bitches_be_crazy"))

    you "Old Valyrian... Strange..."

    show gizel at left with dissolve

    gizel "Ah, there you are."

    hide spirit with blinds

    spirit "BWAAAH!!!" with vpunch

    gizel upset "Hey! Come back here!!!"

    gizel "That's no fun!!! Since when are demons so {i}{b}square{/b}{/i}!"

    gizel angry "Humph. Poser..."

    you "Ahem. Gizel?"

    gizel upset "Yes, what?"

    you "You did it! You drove the evil spirit away!"

    gizel angry "Oh, yeah, that."

    you "Cheer up! We have freed this place of a great evil!"

    gizel upset "How is that supposed to cheer me up???"

    gizel "But wait..."

    gizel blush "We succeeded, right? So I now own this place!!!"

    you "Well, technically, I own it, since I made that deal..."

    gizel angry "What???" with vpunch

    play sound s_crash

    "Gizel's body starts radiating waves of dark energy."

    you "But of course, you can stay here as long as you like, free of charge, ahahaha! It will be my pleasure. *sweat*"

    "The dark energy recedes."

    gizel smirk "Well, of course I will. I wasn't even going to ask you."

    you "..."

    gizel normal "Anyway, enough useless blabbering. Let's take a look around, shall we?"

    play music m_gizel fadein 3.0

    with fade

    you "The place is quite run down..."

    gizel "Well, nothing that a little magic can't fix."

    gizel "Minimal comfort for now, but I can tap into the vortex of dark energy as much as I want, so I could turn that place around in short order..."

    gizel "We'd still need the materials, though."

    you "Well, maybe I can provide that. Most of the estate is in utter disrepair, but parts of the stables and animal pens should still be usable I think."

    you "Are you planning to raise some animals?"

    play sound s_evil_laugh

    gizel smirk "Ha! Animals! You're funny."

    gizel normal "But I do have plans for this place..."

    gizel blush "And I know just how you can help me."

    you "Er..."

    gizel normal "But first, I need to recover my 'stuff' from the junkyard. Why don't you come back tomorrow, give me some time to settle down?"

    you "Sure."

    gizel blush "When you return... I might have a proposal that would benefit the both of us."

    "You wonder what she means by that."

    gizel normal "Anyway, you can go now. Oh, and tell Goldilocks to leave me the fuck alone."

    gizel angry "Tell her that if she ever disturbs me here, I'll have her fuck a whole family of bears!"

    you "Oh..."

    $ story_add_event("farm_gizel_introduction")

    play music m_nature fadein 3.0

    scene bg farmland dusk with fade

    show goldie at center with dissolve

    goldie "[MC.name]!!! You're back! How did it go?"

    you "It went well. The evil spirit has been driven off, and the curse is lifted. You and your animals can rest easy."

    play sound s_surprise

    goldie "Oh, [MC.name]!" with vpunch

    "Overcome with enthusiasm, she jumps into your arms, hugging you close against her."

    "You get a tingly feeling in your crotch as her massive breasts press hard against your chest."

    you "Well, uh, technically I didn't do much..."

    play sound s_laugh

    goldie "You're too modest! {i}{b}You{/b}{/i} did this! You came to my rescue, like you promised!"

    you "Well, uh... I suppose you could say I did it, then... I mean, I came up with this idea, so..."

    play sound s_ahaa

    goldie "Oh, you're the best! You saved my life, and my father's ranch..."

    you "Haha... Well, yeah, that's right... I did it, I saved the day, all by myself, hahaha..."

    "She gives you a warm smile, reluctantly letting you go."

    goldie "Say, [MC.name], why don't you stay for dinner tonight?"

    goldie "It's the least I can do for you... And, frankly, I need the company."

    you "Well, of course then."

    goldie "Splendid! Let me get everything ready..."

    call goldie_dinner() from _call_goldie_dinner

    return

label goldie_dinner():

    stop music fadeout 3.0

    scene bg farmland night with Fade(0.5, 1.0, 0.5)

    show goldie at center with dissolve

    goldie "Thank you so much for coming to dinner, [MC.name]."

    you "No, I should thank you. That roasted pork on a spit was the most delicious I've ever had. You're a real chef."

    goldie "Thank you! People used to say I was very good at handling meat."

    goldie "It's all in the wrist, you know..."

    you "That Romandian wine was also exquisite..."

    goldie "Yes... It made me a little tipsy, though."

    you "Well, Goldie... It's been a great night. I'd best be going, though."

    goldie "Oh, [MC.name], do you have to? Won't you stay with me a little longer?"

    you "Well, uh... I mean... I could..."

    goldie "Come inside for a minute. There's something I'd like to show you."

    scene black with fade

    you "Goldie? What did you..."

    you "Oh."

    goldie "Ah! There it is..."

    call goldie_strip(first=True) from _call_goldie_strip

    goldie "Here, let me make you feel good too."

    call goldie_titjob(first=True) from _call_goldie_titjob

    goldie "My, you're still very hard... Could it be you want more?"

    call goldie_sex(first=True) from _call_goldie_sex

    scene bg farmland night with fade

    $ MC.interactions = 0

    "You have a good time with Goldie. It is very late when you finally get back to [brothel.name]."

    $ NPC_goldie.unlock_trainer()

    return

label farm_activate_goldie():

    scene bg farmland with Fade(0.5, 1.0, 0.5)

    play sound s_rooster

    show goldie with dissolve

    play music m_nature

    goldie "[MC.name]! I'm so glad you dropped me a visit..."

    you "Always a pleasure, Goldie. Seen Gizel around lately?"

    goldie "The nutc... Gizel? Well, she keeps to herself, most of the time."

    goldie "But some days I hear these terrible, chilling screams of agony, coming from the farm... I worry the farm might be haunted again!"

    goldie "Once, I tried to go over there, to inquire if she was all right... Let me tell you, she didn't like it one bit."

    goldie "Now I just leave her alone. I'm sure she can take care of herself."

    you "Yes, you'd better stay clear of the old farm. Gizel is kind of, err, an eccentric, and she doesn't enjoy the company of people."

    goldie "Yes, I could see that... Hey, that gives me an idea!"

    you "What?"

    goldie "She must be feeling lonely, all by herself in this big farm. Why don't you get her a pet?"

    you "A pet?"

    goldie "Sure. In fact, my animals are back to full health, and they have been pretty energetic recently. I could sell you one for a good price."

    goldie "I can only sell you male ones though. I need the females for breeding. Regardless, I'm sure your friend would enjoy their company!"

    you "You might be right about that..."

    stop music fadeout 3.0

    scene black with fade

    $ farmland.action = True
    $ unlocked_shops.append(NPC_goldie)

    "You may now buy {b}beasts{/b} at the farm."
    $ unlock_achievement("merchant goldie")

    return

label goldie_strip(first=False):

    scene bg goldie_strip1 with fade

    goldie "Do you... like what you see?"

    you "Goldie... Wow..."

    if first:

        goldie "You really helped me out there... My people had abandoned me, but you came through for me."

        goldie "I really oughta show you my thanks..."

        you "I really like how you decided to show me your... thanks..."

        goldie "Perhaps you would like to see a little more of them, then?"

    play sound s_dress

    scene bg goldie_strip2 with dissolve

    play sound2 s_mmmh

    goldie "Come, take a closer look."

    you "Wow..."

    goldie "Do you like my tits?"

    you "I do... They're so... Bouncy..."

    goldie "My brothers used to tease me when I was younger, telling me those tits made me look like a cow..."

    goldie "But I've grown to like them. They're really sensitive, you know..."

    play sound s_ahaa

    goldie "Touch them."

    you "Lucky me..."

    "You start fondling Goldie's ample tits, burying your fingers into her soft flesh."

    play sound s_mmmh

    goldie "Mmmmh..."

    "Her puffy nipples grow even larger under your touch, rubbing pleasantly against your palm."

    play sound s_aaah

    goldie "Oooh... [MC.name]... That feels really good..."

    $ NPC_goldie.love += 1

    return

label goldie_titjob(first=False):

    if NPC_goldie.flags["swimsuit"] and dice(6) >= 4:
        $ scenes = ["bg goldie_titjob3", "bg goldie_titjob4"]
    else:
        $ scenes = ["bg goldie_titjob1", "bg goldie_titjob2"]

    scene expression scenes[0] with fade

    play sound2 s_sucking

    goldie "It's so big..."

    "After freeing your dick from your pants, Goldie wraps her large boobs around it."

    you "Wow... Your tits feel so soft and nice..."

    "Immersed in the feeling, you start moving back and forth, your cock buried in the flesh of her enormous boobs."

    goldie "Mmmh, that's nice..."

    "Whenever your cock emerges from her cleavage, Goldie gives you a little lick on the tip."

    goldie "Oh, the salty taste of pre-cum... It's driving me crazy..."

    if first:
        you "Where... Where did you learn all that..."

        play sound s_laugh

        goldie "What can I say, I'm a bad girl... I've been very lonely here at the ranch, with nothing to do but work. But I had books, the right kind... Lots of them..."

    you "Oh, keep doing this, it's great..."

    goldie "You seem to have built up a lot of stress, poor [MC.name]..."

    goldie "It's alright, just come whenever you want... Don't worry, I've got glasses. *wink*"

    you "Oh, you dirty girl..."

    with flash

    play sound s_orgasm_fast

    goldie "Haaa!"

    scene expression scenes[1] with doubleflash

    "The soft rub of her gorgeous tits proves too much for you. You come unexpectedly, your rock-hard cock spurting cum all over Goldie's face."

    "She gives you a dreamy look from behind her soiled glasses."

    play sound s_mmmh

    goldie "Hmmm... You came a lot... You must have been saving this load just for me..."

    "Goldie massages her boobs in a circular fashion, spreading your cum all over them."

    you "Ugh..."

    $ NPC_goldie.love += 1

    return

label goldie_sex(first=False):

    scene black with fade

    "Pushing Goldie on all fours, you lower her panties, taking a good look at her naughty pussy."

    play sound s_sucking

    "Sliding a couple of fingers inside her, you find her already dripping wet."

    goldie "Oh, [MC.name]... I'm so horny right now... I'm ready for you..."

    if first:
        "Your dick is still rock-hard."

    scene bg goldie_sex1 with dissolve

    "Placing your erect shaft against her loose pussy, you slide into her with ease." with hpunch

    play sound s_aaah

    goldie "[MC.name]! Your dick... It's amazing!!!"

    "Pacing yourself, you start moving slowly, enjoying rubbing the whole length of your shaft against her insides." with hpunch

    play sound s_ahaa

    goldie "You're going so deep! Aaaaah..."

    play sound s_moans

    scene bg goldie_sex2 with dissolve

    goldie "Oh, [MC.name]!"

    "Increasing your pace, you fuck Goldie's dripping pussy harder and deeper. She seems lost in the feeling."

    goldie "You're driving me... crazy... Aaah..."

    if first:

        "Noticing her pinkish little asshole, you decide to give it some attention."

        play sound2 s_surprise

        scene bg goldie_sex1 with dissolve

        goldie "What... What are you doing?"

        "Still wet with her pussy juice, you slide a finger deep inside her asshole."

        play sound2 s_scream

        goldie "AAAH!!!"

        play sound s_moans

        scene bg goldie_sex2 with dissolve

        goldie "Oh, right there! Right there!"

    "Goldie moans like a bitch in heat as you ravage her insides." with hpunch

    "Her slippery pussy tightens around your dick, as if to entice it further inside." with hpunch

    play sound s_scream

    goldie "[MC.name]! I'm... I'm..."

    play sound s_scream_loud

    "Overcome by lust, Goldie's perverted body is rocked by a powerful orgasm." with flash

    play sound s_orgasm

    scene bg goldie_sex3 with doubleflash

    goldie "AAAAH!"

    "Her screams of pleasure are enough to send you over the top. You come deep inside her wet pussy."

    with flash

    goldie "You came inside... So much..."

    "Cum drips out of Goldie's pussy and runs down her thighs. She doesn't care. She just lays there with her legs spread out, looking at you, smiling."

    play sound s_aaah

    goldie "Oh, [MC.name]..."

    $ unlock_achievement("h goldie")

    scene black with fade

    $ NPC_goldie.love += 1

    if first:
        $ MC.change_prestige(1)
        "You have earned prestige. All your remaining actions have been spent."
    else:
        $ MC.change_prestige(1)
        "You have earned prestige."

    return

label farm_meet_gina():

    scene bg junkyard with fade

    "The junkyard. A foul place, where all the refuse from the mean streets of Zan gets piled up, to be burned or forgotten."

    "Seen from here, the City of Jade seems to be more worthy of the name 'City of rubbish'. As the largest city in the whole of Xeros,
     it produces enough waste every day to create a landscape of garbage mounds, spreading as far as the eye can see."

    if MC.god:
        $ text1 = MC.god + " forsaken"
    else:
        $ text1 = "disgusting"

    you "Remind me again, why the hell did I come to that [text1] place? I have trouble understanding my own decisions, sometimes..."

    "As you ponder your own fickleness, your eye is caught by a shiny reflection. It came from the top of the highest garbage pile in the junkyard,
     a monstrous column standing a good thirty feet tall."

    you "Wait, what's that? There's something there."

    play music m_wind

    scene black
    show bg gina_standing
    with fade

    "A girl is standing on top of the rubbish mound, with an absent look on her face. You move in to get a closer look."

    you "What is this girl doing? It looks like..."

    "The girl takes a step back, staring at the void beneath her. She takes a deep breath."

    you "It looks like..."

    you "She's going to jump!" with vpunch

    menu:
        "What do you do?"

        "伸出援手":
            $ MC.good += 1

            you "Lady, wait!!!"

            "Unable to hear you, the girl takes a run-up, and leaps into the air."

            scene bg gina_falling at quake with dissolve

            gina "AAAAAAAH!!!"

            "Running at the top of your speed, you try to meet her as she falls like a stone."

            gina "EEEEEK!!!"

            you "I'll save you!!!"

            scene black

            play sound s_crash

#            with vpunch

#            play sound2 s_punch


            you "OUCH!" with vpunch

            scene bg gina_fallen1 with fade

            gina "Aaah... My butt hurts... Good thing I landed on some soft terrain..."

            you "Err... *drool*"

            gina "Oh, there's someone here! Mister, are you hurt?"

            you "Panties... Panties flying... In the skies..."

            gina "He's got a concussion, poor guy."

            gina "Here, try to sit down, very slowly. I'll find you something for your head."

            you "Ahhh..."

        "袖手旁观":
            $ MC.good -= 1

            you "I would help her, I would. But it's too damn far."

            you "Too bad. Wouldn't want to be the one who has to clean this up..."

            "You cannot help but watch, fascinated, as the girl takes a run-up, and leaps high into the air."

            show bg gina_jump at top with dissolve

            gina "And... WING POWER!!!" with vpunch

            play sound s_clash


            "You notice small, metallic appendices that seem to shine a bright, blue light behind the girl's shoulders."

            "And then, amazingly, she starts to {i}fly{/i}."


            gina "I'M FLYIIIING!!! YES!!!" with vpunch

            you "More like gliding, actually."

            you "Uh, wait, more like falling... She's picking up speed..."

            play sound s_fizzle

            "The bright blue light recedes, and the girl seems to lose control of her flight."

            scene bg gina_falling at quake with dissolve

            gina "AAAAAAH!!!"

            play sound s_crash

            with vpunch

            scene black with vpunch

            you "Oopsie."

            scene bg gina_fallen2 with fade

            gina "Awww... My head..."

            "You walk over to the girl. You can't help but notice her panties are exposed as she lays there helpless."

            you "Hey there, sister, are you hurt?"

            gina "I think... Uh..."

            gina "I'll be all right..."

            "It seems that her 'wings' broke her fall at least a little."

            you "She must be tougher than she looks..."


    scene bg junkyard with fade
    show gina with dissolve

    you "Hey, you! Are you fucking out of your mind?"

    gina "Uh... Beg your pardon?"

    you "Jumping up from on high like that! Are you trying to die!"

    gina "Uh? Of course not, silly!"

    gina "It's all part of a grand scientific experiment, way too complicated to understand..."

    you "You're trying to fly, aren't you."

    play sound s_surprise

    gina "YES!" with vpunch

    gina "How did you guess? Are you perhaps a fellow scientist?"

    you "Uh, no... I don't see the appeal of jumping to your death using failing technology..."

    gina "Failing technology? FAILING TECHNOLOGY?" with vpunch

    gina "Are you mad! Look at these composite wings! They're a thing of beauty, aren't they? It's Cimerian tech!"

    "You take a closer look at the roundish appendices floating above the girl's shoulders. It's unlike anything you've ever seen.
     Definitely not man-made technology, as far as you can tell."

    you "You... You made this?"

    "She stands up, beaming with pride."

    gina "I sure did!"

    gina "Well, uh..."

    gina "Actually, {i}recycled{/i} might be a better word... But in layman's terms, sure, I {i}{b}made{/b}{/i} it. Isn't it awesome?"

    you "Well, it would be... If it actually allowed you to fly..."

    gina "What? Didn't you notice? I {i}{b}soared{/b}{/i}! I mean, sure, I fell, but for a moment, it worked, and I was flying! That's right! FLYING!"

    you "Well, I don't think people will be very interested in wings that only work for a split-second before they let you fall down to your death."

    gina "Humph! How short-sighted of you. I can see that you are completely lacking in scientific spirit."

    "You take a skeptical look at her flapping metal-wings."

    you "Say, why don't you make those wings larger? Maybe you could keep gliding longer if they were larger?"

    gina "Larger wings? LARGER WINGS? HA!"

    gina "HA!"

    play sound s_evil_laugh

    gina "HAHAHAHA!"

    you "What's so funny?"

    gina "Oh, my, you're so ignorant of basic scientific principles..."

    gina "Think for a minute. Larger wings mean more {b}weight{/b}. More weight means it's harder to {b}fly{/b}!"

    gina "It's obvious to anyone that's ever studied the question that to properly fly, you need very tiny, light wings. The tinier the better."

    you "Really?"

    gina "Of course! Think of the animal kingdom. What is the most magnificent flying animal you know?"

    you "Well, uh... There's the royal eagle... Griffins... Dragons..."

    play sound s_laugh

    gina "Nonsense!!! I'm talking about the mosquito!"

    you "The mosquito?"

    gina "Of course, dummy!"

    gina "The mosquito is the most perfect, wonderful creation of the gods, it's so tiny, and yet flies so beautifully, in all directions..."

    gina "You can spend a whole night trying to swat it, and it will always elude you!"

    gina "The mosquito is a wondrous creature indeed... Its buzzing sound is the very sound of {i}progress{/i}!"

    you "Ahem, well... I had certainly never seen mosquitos in that way..."

    gina "You can thank me later. For now, I need to repair those composite wings..."

    gina "But damn if I haven't run out of Cimerian components. These repeated crashes have taken a toll..."

    you "Repeated?"

    gina "And now, all I've got is a dozen stupid crates, full of perverted machines..."

    you "Uh? Perverted machines?"

    gina "Yes... Magically infused apparatuses, thrown away after they burnt some Karkyr enchantress at the stake..."

    gina "I recovered it. I used to dismantle them and re-use the components for my experiments..."

    gina "It's great if you need pistons. For some reason, they're chockfull of those."

    you "Really..."

    gina "What am I gonna do? Cimerian scrap is so expensive these days..."

    you "Well..."

    you "Listen. I might be able to offer you a deal."

    gina "A deal? What deal?"

    you "What if you sold me some of those, er, useless sex machines on the cheap... Er, I mean, at market value for the junk it is, haha..."

    gina "You'd buy them?"

    you "Sure."

    gina "Why, ok, I can do that!"

    you "Fantastic. We're in business, then!"

    gina "Deal! My name is Gina. Come by here anytime, and I'll fix some of those machines for you. So you can, uh, enjoy yourself."

    $ gina_name = "Gina"

    you "I'm [MC.name]. And, uh, it's not for me, it's for a friend..."

    gina "Yeah, yeah, sure. Whatever floats your boat, pal..."

    gina "But listen. If you ever run into Cimerian technology, anything you can find, I'm buying, and I will pay well. Seriously."

    you "I'll remember that."

    stop music fadeout 3.0

    scene black with fade

    $ junkyard.action = True
    $ unlocked_shops.append(NPC_gina)

    "You may now buy {b}machines{/b} at the junkyard."
    $ unlock_achievement("merchant gina")

    return


label gina_research():

    hide screen visit_location
    with fade

    "Curiosity finally gets the better of you, and you decide to visit Gina the Scientist in the Warehouse district."

    you "Willow gave me this address... This building looks like a ruin... It must be abandoned."

    you "Maybe I should just..."

    "Girl's voice" "Heeeeey! [MC.name]!!!"

    you "Uh?"

    "Looking up, you see Gina, standing precariously on edge of the building's fourth floor."

    you "Gina! Don't jump!"

    gina "This is not that kind of experiment, silly. Get up here."

    with fade

    show gina with dissolve

    gina "So, here you are! I've been waiting a long time!"

    you "Uh, hi. Why did you call me..."

    you "UWAAAH!!!"

    "In the corner of the derelict room, a gooey, vaguely translucid monster is wobbling. It looks like a blob of brownish jelly."

    you "Monster!" with vpunch

    gina "Cut it out..."

    gina "This is not a 'monster'. This is a {i}lubricus plugginus{/i}. I call him 'Test Subject #1'."

    you "That's not very, err, personal..."

    gina "Shut up, Test Subject #2. We have much to do."

    you "I don't like this..."

    gina "Yeah yeah, grab the book behind you will you?"

    "She gestures towards a dusty leatherbound tome on a workbench nearby. You try to decipher its title."

    you "Ne... Cro... No... Mi-con. What gibberish is this?"

    gina "It's a book about ancient science and magic. Apparently it was translated many times over from its original Cimerian. I use it for my most advanced research."

    gina "It is said it holds the key to meeting the Great Old Ones..."

    gina "And who wouldn't want to meet them? They're {b}Great{/b}, right?"

    you "Uh..."

    if MC.playerclass == "法师":
        you "(Didn't they teach us to stay clear of this in Conjuring 101? Damn, I don't know, I was too busy checking out the teacher's cleavage...)"

    gina "Go to page 666 and find my notes. You must read me the exact words as I handle Test Subject #1 with care."

    you "All right... I hope you know what you're doing."

    you "<The elusive {i}lubricus plugginus{/i} is a wondrous creature, much sought after for its magically infused extract.>"

    you "<It must be handled with care as it is both fragile, slippery, and vengeful.>"

    you "I'm glad you're the one handling it."

    gina "Yeah, don't think I'd let you mess with such a precious research subject. Keep reading."

    you "<To proceed with the extraction, locate the creature's flexible appendage...>"

    gina "That must be it... Come on, little guy, take it easy..."

    gina "It's resisting..."

    you "Try pulling harder."

    gina "I am..."

    play sound s_punch

    gina "Uwaah!" with vpunch

    scene black with fade
    scene bg gina research1 at top with dissolve

    "Gina is surprised as a large appendage separates from the monster's bulk and starts wiggling around."

    gina "It's moving... Give me a hand!"

    you "Well, uh, sorry, but... I need both hands to hold the book... Besides, the view is nicer from over here..."

    gina "Aah, it's really slippery... What should I do now?"

    you "<Once you locate the central appendage, or 'noodlix', you must use both hands to rub it back and forth vigorously.>"

    gina "R-Really? Like that?"

    "Gina starts awkwardly moving her hands over the creature's 'noodlix'. It doesn't look too happy."

    "Monster" "*whines plaintively*"

    you "You're doing it wrong..."

    gina "I'm doing my best! What the hell do you know!"

    you "Look, you need to use both hands, and rub it continuously, caressing but firm..."

    gina "H-How the hell did you come up with this advice! Just read from the book!"

    "Even though she is yelling at you, she follows your suggestion reluctantly, rubbing and tugging the monster's appendage as it wiggles in her face."

    you "<Gradually, the noodlix should become hard to the touch...>"

    gina "It is! It's working!"

    you "<Some of the extract may leak out from the noodlix tip as you proceed, brown at first...>"

    gina "It is! I can see some liquid spurting out of the appendage! It smells fishy..."

    you "<After a while, you may feel the noodlix throb harder... You must then increase the pace.>"

    gina "I feel it! I feel it!"

    "Monster" "*low grunt*"

    gina "It's grunting! What is it grunting for? And why is the noodlix pointing at my face?"

    you "Oh, it's written here! <When the creature starts grunting, it means...>"

    play sound s_roar

    scene black with flash

    play sound s_scream

    gina "EEEEK!!!"

    you "<...it is ready for extraction.>"

    show bg gina research2 at top with doubleflash

    play sound s_surprise

    gina "It blew up in my face!!! All the extract just spurted out!"

    you "Well... Wasn't it the desired result?"

    gina "Nooo! I was supposed to save it for further research..."

    gina "Some of it even got in my mouth... Ew... *munch*"

    gina "*munch* Actually... It's not unpleasant. Salty, but very rich..."

    gina "I need to run tests on this. Maybe it could be an efficient food source? So I don't need to order take-out food every night?"

    "Her face is still dripping with monster extract, but Gina seems absorbed in her scientific reflexions. She looks into her messy lab for a test tube."

    gina "I'll need three different samples..."

    you "Wait, it says here: <You can renew the operation several times a day, especially in the morning.>"

    "She turns to you."

    gina "[MC.name]! Help me get some more extract! You've seen how to do it..."

    you "Oh, ahem, I just remembered, I really need to go because, er... I have an important meeting with the Princess of, err... Somewheristan..."

    gina "Waaait! Come back here!!!"

    scene black with fade

    "You flee Gina's lab before your evening gets even weirder. You never got to find out what it is she was trying to do in the first place, and feel all the better for it."

    return


label farm_meet_stella():

    $ weekday = calendar.get_weekday()

    play music m_tavern fadein 3.0

    scene black
    show bg harbor at top
    with fade

    "The harbor is a noisy and raunchy place on any given day, but it's even worse today. [weekday]s are market days, and merchants from all corners of the world flaunt their merchandise, fresh off the boat."

    "You are intrigued by an especially large crowd, gathered in front of a large and lavishly decorated galleon."

    "From the intricate carvings and statues adorning the ship, depicting naked women, men and other creatures engaged in a variety of naughty sex acts, you guess it came all the way from the Blood Islands, the slavers' isles."

    "As you move closer to see what the fuss is all about, you see a stern-looking woman, standing in front of a group of tightly bound slaves."

    show bg ambush1 at top with fade
    show stella at center with dissolve:
        yoffset yres(350)

    "The woman has an exotic look about her. She is wearing a revealing attire, typical of the Blood Islands' slavers."

    "She speaks with an authoritative voice, with a business-like tone, as if she was delivering a keynote speech."

    stella "People of Zan, come and rejoice! Blood Orange Inc. has brought to you the finest slaving technology, straight from the Blood Islands." with vpunch

    stella "A brand new generation of slaves awaits, ready to give you the greatest pleasures..."

    show stella at right with move

    show mare at left with dissolve

    "One of the bound slaves steps forward. The young girl is blinfolded and gagged. She stands ready at attention, not even moving a muscle."

    stella "As you all know, slaves from the Blood Islands are the most sought-after in the Western hemisphere."

    stella "Our slaves are of the highest quality, born and raised on an island sex farm."

    stella "There, our ranchers select only the best breeds, with high obedience, and an even higher sex drive."

    stella "Then, our mages use their spells to enhance their natural capabilities, and shape them into the perfect sex slaves."

    "Man" "Exactly how obedient are they?"

    stella "Perfectly obedient. If you're worried about them rebelling against orders, or running off like a vulgar Zan street girl, don't be."

    stella "All of our slaves are subjected to magical lobotomy to prevent them from acquiring independent thoughts or a sense of self."

    "Man" "You mean... They're like... Things? They're like products on a shelf?"

    stella "We do not think about our slaves as mere things..."

    stella "We prefer to call them 'devices'."

    stella "We don't think of ourselves as being in the business of selling products, either."

    stella "What we want is to bring to our customers a 'complete erotic experience' tailored to their most intimate needs."

    stella "Let me demonstrate one of the 'features' we have added to our next generation of devices."

    stella "Our mind-bending engineers call this: 'Hands-free mode'."

    man "Hands-free... mode?"

    stella "For this demonstration, I have set up one of our young mares right here on stage. Barely sixteen, but she's already been completely broken."

    stella "Our engineers have tuned her to my mental wave-length, just as they would for her rightful master."

    stella "Watch what happens as I think about something... Say, what if I think about her having an orgasm..."

    stella "Orgasm. Now."

    "For a long moment, nothing seems to happen."

    stella "Orgasm?"

    "The mare stays totally frozen and silent. Someone coughs."

    stella "Well, uh, there must be some lag..."

    stella "It's... It's always embarrassing when something like that happens... It was working only yesterday..."

    stella "Orgasm, dammit!!!" with vpunch

    play sound s_surprise

    "Slave girl" "Oh..."

    play sound s_screams

    hide bg
    show bg mare_orgasm at quake
    with dissolve

    "Slave girl" "AAAAAAH!!!"

    play sound s_moans_short

    "Suddenly, a wave of pleasure washes over the slave girl, making her body quiver with invisible pleasure."

    play sound s_orgasm_fast

    "The pleasure intensifies, and the girl's body is rocked by an intense orgasm. She squirms and moans through her gag, drooling like an animal."

    "Slave girl" "Ngggh!!!"

    hide bg
    show bg ambush1 behind stella at top
    with dissolve


    stella "Hands-free mode works with a whole range of thoughts and emotions, of course... We can also order pain, love, or fear, from a distance. "

    stella "As we continue to expand on our range of personal devices, we strive to fulfill our company's motto: making the world a better..."

    "Angry man" "HERESY!!!" with vpunch

    stella "Uh?"

    "Angry man" "You're an abomination! A heretic! You defile those poor souls! Because of your evil tampering, they have become blind to the light of Arios!"

    stella "Sir, I can assure you all our business here is perfectly legal. The treaty passed between the Blood Islands and King Pharo states that..."

    "Angry man" "You cannot hide behind the laws of men, when you are offending the gods! You cannot treat their flock that way!" with vpunch

    stella "Let me assure you, we have excellent shepherds. Our slaves are bred for their sex-drive and servility, so I'm sure they actually enjoy..."

    "Angry man" "Don't insult my intelligence, whore!" with vpunch

    show stella crossed with dissolve

    "The woman's eyes narrow. You can almost feel the thoughts racing through her mind."

    stella "Get ready!"

    hide bg
    show bg mare_attack
    with dissolve

    play sound s_sheath

    "With lightning speed, the slave girl draws two guns from seemingly nowhere, aiming straight at the man's chest. His jaw drops."

    "The woman grins fiercely."

    stella "Now, as you can see, I can simply order my slave to move into defense mode with a simple thought..."

    stella "Ordering her to shoot is just as easy."

    "Scared man" "No, please... Don't..."

    stella "Of, course, I can just as easily order her to maim or neutralize a specific body part..."

    play sound s_dodge

    "The slave girl mechanically lowers her arms, now aiming straight at the man's crotch."

    "Scared man" "My lady please! H-have... Have mercy!"

    "The woman licks her lips, staring at the terrified man, shaking in his boots at the sight of the two guns aimed straight at his cock."

    stella "Oh, my, you seem to have just wet your pants..."

    "Scared man" "I beg you, please... *sob*"

    stella "Scram."

    play sound2 s_wscream

    "Scared man" "Aaaahhh!!!"

    play sound s_steps

    "The man runs away as if the hounds of hell were at his heels."

    play sound s_sheath

    hide bg
    show bg ambush1 behind stella at top
    with dissolve

    "With uncanny speed, the slave girl holsters her guns, and returns to her submissive position."

    stella "Now, where were we..."

    scene black with fade

    "The sale is a big success. All of the slave dolls are sold to some rich nobles for extravagant prices."

    show bg ambush1 at top
    show stella at center with dissolve:
        yoffset yres(350)

    "After the big show, you linger to talk a little with the slave merchant."

    stella "Can I help you? You don't look like you can afford a ten thousand denar custom sex slave..."

    you "Well, actually, I already have my own slaves. I'm a brothel owner."

    you "But I'm looking for special slaves..."

    stella "Of course you are. Provided you have the coin, we can arrange anything."

    you "Well, you called your female slaves 'mares'... If I'm not mistaken, the Blood Islands also breed stallions? Male slaves with abnormally large dicks?"

    stella "Ah, I see what you're into. Those are definitely cheaper, the older models at least."

    you "Can you sell some to me?"

    stella "Well, sure, I can fix you up. *wink*"

    you "Well, I mean, it's not for me, of course, it's for a friend of mine..."

    stella "Yeah, sure, they all say that... *wink* *wink*"

    you "No, I mean, there's this friend, she's an elf, but no one can see her, and... Oh, forget it."

    stella "My name is Stella. Come visit me any time if you want to buy stallions. I'll have new arrivals every week."

    $ stella_name = "Stella"

    scene black with fade

    $ harbor.action = True
    $ unlocked_shops.append(NPC_stella)

    "You may now buy {b}stallions{/b} at the harbor."
    $ unlock_achievement("merchant stella")

    return

label stella_reward1(): # Activates when the player has spent a combined 1000 denars at the store

    hide screen visit_location
    with fade

    show stella at center with dissolve:
        yoffset yres(350)

    stella "You! Come back here!"

    "The merchant yells a cutting order as you are about to leave."

    you "M-Me?"

    stella "Yes, you."

    "She spoke with her usual cold and martial tone."

    you "I just paid for this..."

    stella "I know. This is why I'm calling you back here."

    "She sounds displeased."

    show stella crossed at center with dissolve:
        yoffset yres(350)

    stella "Our records here show that you have just spent 1000 gold at the store. See?"

    you "Is that so? Well..."

    stella "It is so. I {i}never{/i} make a mistake."

    you "O-Of course..."

    stella "Spending this much money can only mean one thing..."

    show stella at center with dissolve:
        yoffset yres(350)

    stella "You are eligible for our {i}customer loyalty{/i} program!!!" with vpunch

    you "Oh..."

    you "(Why do you make it sound so scary?)"

    stella "As per article 144 paragraph 6 of our licensing agreement, all customers that pay 1000 gold or more for our services MUST join our loyalty program..."

    you "Well, it's really nice, but I'm not really..."

    show stella crossed at center with dissolve:
        yoffset yres(350)

    stella "Shut up. Believe me, you do {i}not{/i} want to be a disloyal customer."

    you "*gulp*"

    stella "We are merciless in dealing with those. Now, as per section 3 of chapter 21, I am to administer your 'reward' myself, effective immediately."

    you "Ad-Administer? Well, uh... I suddenly remembered I've got an appointment with, er... Some guy... Maybe next time?"

    stella "Are you deaf? I said EFFECTIVE IMMEDIATELY!" with vpunch

    you "Eeeek!"

    "Grabbing you by the arm, the fierce woman drags you to her ship."

    scene black with fade

    play sound s_creak

    "Stella throws you on the cold floor of a slave holding cell."

    show stella at center with dissolve:
        yoffset yres(350)

    stella "Strip off your clothes. You've got 2 minutes."

    play sound s_door_close

    "Not finding a way out of your predicament, you passively follow her orders."

    play sound s_dress

    stella "Are you done?"

    you "Yes..."

    play sound s_punch

    stella "CALL ME MISTRESS!!! Or I'll bust your balls open with my heels!!!" with vpunch

    you "Uwah!"

    you "Y-Yes, mistress..."

    stella "Good. You must behave like a loyal and trustworthy customer. Now, you shall get your 'reward'."

    scene black with fade

label stella_handjob():


    play sound s_punch

    "*grab*" with vpunch

    show bg stella handjob1 at top with dissolve

    "Nailing you to the floor, Stella wraps her thighs around your head, locking you in place."

    stella "Now, don't move. No reason to make it harder than it should be."

    "Stella pulls your dick up."

    you "(Oh no... She's going to rip it off...)"

    stella "What a useless flacid piece of flesh... I should have known not to expect much."

    "Even as she is abusing you, she starts tugging at your cock."

    you "Hey!"

    "She has the hard, strong hands of a killer... But she's also pretty deft."

    stella "Come on, get hard already. I mustn't be away from the store too long."

    "She tickles your balls with her gloved fingers."

    you "Uwah..."

    "She increases her pace, and it almost feels as if she is going to rip off your cock with her bare hands."

    "At the same time, she is putting a lot of pressure on all the right places. Soon, your body reacts despite your fears."

    stella "Well, look at this..."

    "Your cock now stands rock hard. She spits on it and keeps running her hand up and down your shaft."

    stella "Finally, we've got something to work with. I will now proceed with delivering your reward."

    "Shoving her crotch in your face, Stella makes sure to muffle your cries. She starts jerking you even harder and faster."

    you "NGGH!!!"

    "As you are almost going to cum, she suddenly slows down."

    stella "Not so fast. A good customer must be patient."

    "She teases you for long minutes, alternating between fast and hard tugging and slow rubbing, tickling your balls with her fingertips."

    you "Nggh..."

    "She squeezes you so hard between her thighs that you are running out of breath. At the same time, she jerks you off even harder, bringing you once again to your limit."

    you "Nggggh!!!" with vpunch

    show bg stella handjob2 at top with flash

    "You finally cum, spurting white semen on Stella's cleavage."

    show bg stella handjob3 at top  with doubleflash

    "Instead of being mad, Stella smirks at she watches the hot cum dripping between her boobs."

    with flash

    stella "Good. You came. I was worried you would waste more of my time."

    you "..."

    "Almost passed out, you take a moment to breathe."

    stella "But this is not enough."

    you "Uh?!?"

    stella "As per Galactic Empire Order 66, I am to make sure to drain you completely dry. But it seems to me that you still have a lot more in store..."

    you "!!!"

    "*grab*"

    show bg stella handjob4 at top with flash

    "Grabbing you even harder than before, Stella starts pumping you dry."

    "Even though it hurts, your body responds in spite of yourself, and soon she brings you to another orgasm."

    stella "HAAA!!!" with vpunch

    show bg stella handjob5 at top with flash

    you "NGGGH!!!"

    with doubleflash

    stella "More!"

    with doubleflash

    "Milking your cock dry, Stella has you come 3 more times, until your balls are completely drained."

    show bg stella handjob6 with fade

    "..."

    stella "Phew. You gave me quite a work-out."

    you "Gwaaaah..."

    "You feel completely drained and miserable."

    stella "Well, I am looking forward to see you remain a loyal and obedient customer. You are now to spend a lot more money at the store."

    stella "Are we clear?"

    you "Y-Yes..."

    stella "YES WHO!!!" with vpunch

    you "Y-Yes, Mistress, Lady Sir!!!"

    stella "Humph."

    "Throwing you your clothes as you whimper on the floor, Stella finally lets you go."

    scene black with fade

    $ MC.interactions = 0
    $ MC.change_prestige(2)

    "You go back to your brothel, feeling dizzy. You cannot bear to think about sex any more today, and just head to bed."

    "You have lost your remaining actions for the day."

    $ story_add_event("stella_invitation")

    return


label stella_reward2(): # Activates when the player has spent a combined 2500 denars at the store

    hide screen visit_location
    with fade

    show stella at center with dissolve:
        yoffset yres(350)

    stella "You! Come back here!"

    you "*gulp*"

    "Before you can make your escape, Stella calls you back to her stall with an icy voice."

    you "W-What have I done..."

    stella "What have you done? WHAT HAVE YOU DONE???" with vpunch

    you "..."

    show stella crossed at center with dissolve:
        yoffset yres(350)

    stella "You have reached PLATINUM status, that's what!"

    you "Uh?"

    stella "Congratulations on becoming an even more loyal customer. It says here you've just spent {b}2500{/b} gold in our esteemed establishment."

    you "Oh no... That means..."

    stella "That means... YOU GET ANOTHER REWARD!!!" with vpunch

    you "AAAH!!!"

    stella "Here, have this. It's a Blood Islands fridge magnet."

    you "No!!! I... Oh."

    you "Wait, just a fridge magnet? That's a relief... Also, what is a fridge? And what's a magnet?"

    stella "Never mind that. I'll also throw in another reward..."

    stella "I shall proceed to FUCK YOUR BRAINS OUT!!!" with vpunch

    you "GWAAAAAAAH!!!" with vpunch

    stella "It isn't part of the loyalty program, but I just feel like it."

    stella "Come back here!!!" with vpunch

    scene black with fade

    "You tried to run, but to no avail. Soon, Stella drags you down to her quarters."

label stella_sex():

    play sound s_aaah

    show bg stella sex1 at top with dissolve

    "Before you have a chance to catch your breath, she rips your clothes off as if they were paper."

    "Pushing you upside down, she lifts your legs in the air with impressive strength."

    "Shoving her panties to the side, Stella starts rubbing her already dripping pussy on your shaft."

    stella "Let's put it in..."

    show bg stella sex2 at top with dissolve

    "Riding you in a reverse piledriver, Stella swallows your dick hungrily as if it was nothing."

    you "Whoah!"

    stella "I have total control over my body. Years of training as a... a merchant... Anyway."

    stella "Fuck me now... You'd better not disappoint me!"

    play sound s_moans

    "Bouncing up and down your cock, Stella takes pleasure in locking you in a humiliating pose, flaunting her breasts and her hard nipples."

    stella "Yes, grovel before me like a dog..."

    play sound s_punch

    with vpunch

    "She slaps your ass with her leather glove, hard enough to leave a mark."

    stella "You are not to cum before your Mistress does. GOT IT?"

    you "Y-yes... Mistress..."

    "Riding you harder, Stella is bending your dick in an impossible shape, making sure it reaches her deepest parts."

    play sound2 s_mmmh

    stella "It's... It's good, worm..."

    stella "Keep, aah... Keep doing it... Mmmh..."

    "In spite of your predicament, your dick is feeling rock hard and enjoys slamming inside her wet pussy. Soon, both of you are moaning like wild animals."

    play sound s_moans_short

    stella "Guh... Fuck me, dog... FUCK ME!!!"

    "It feels as if your hips are about to break, but you endure as Stella brings herself to her limit."

    stella "UWAAH!!!"

    with flash

    "Stella's body tenses up as she feels electricity rocking through her body."

    play sound s_orgasm_fast

    show bg stella sex3 at top with doubleflash

    "You cum hard inside her, filling her with semen as she clings to you with her muscular pussy."

    stella "Good doggy... Hmmm..."

    play sound s_mmmh
    show bg stella sex4 at top with dissolve

    "As you try to withdraw, something is blocking you."

    stella "Not so fast!"

    "Stella contracts her pussy, squeezing your cock hard inside, not letting you escape."

    you "Uh?!?"

    stella "Did you think we were finished here? That was only a warm-up!"

    you "Uwah!!!"

    show bg stella sex5 at top with dissolve

    "Not giving you a moment's rest, Stella rides you harder and harder until the day turns to night."

    with flash

    play sound s_orgasm

    stella "CUMMIIIIIING!!!!"

    show bg stella sex6 at top with doubleflash

    "Stella makes sure to drain every last drop of cum from your sorry body until you are just an empty husk with a near-broken back, whimpering on the floor."

    show bg stella sex7 at top with flash

    "Stella licks her lips with satisfaction as she finally relaxes her grip on your shrinking dick."

    play sound s_evil_laugh

    stella "So much warm cum... I do feel like this was a proper reward... *smile*"

    "Spreading her pussy lips open with two fingers, she watches with interest as a seemingly endless stream of semen pours out of her body."

    stella "Once again, you've proved yourself a worthy customer. I hope you remember this little 'private session' every time you stare at this magnificient fridge magnet..."

    $ unlock_achievement("h stella")

    scene black with fade

    $ MC.interactions = 0
    $ MC.change_prestige(4)

    "Stumbling back home, you put your cock in a bucket of cold water to make it stop burning, and throw the magnet in the fire."

    "You have lost all of your remaining actions for today."

    return

label stella_reward3(): # Activates when the player has spent another 1000 denars at the store

    show stella at center with dissolve:
        yoffset yres(350)

    stella "Not so fast!!!" with vpunch

    you "*gulp*"

    stella "You have spent another {b}1000{/b} gold with us. You are eligible for a reward..."

    menu:
        stella "What do you choose?"

        "用你的小手撸我的肉棒":
            scene black with fade
            call stella_handjob from _call_stella_handjob

        "趴在那里掰开你的小穴":
            scene black with fade
            call stella_sex from _call_stella_sex

        "火速逃离这里":
            you "Look behind you! A three-headed monkey!!!"

            stella "What?!?" with vpunch

            stella "Where is it? Does it have three cocks?"

            "Your ruse worked, Stella turned around. You use that time to get the hell out, running as fast as you can until you can hide inside your barricaded room."

    return


label stella_invitation():

    $ loc = selected_location.name.lower()

    "Walking through a small alley leading to the [loc], you spot something on the pavement."

    stop music fadeout 2.0

    hide screen visit_location

    hide screen overlay

    show bg letter at top with dissolve

    you "What's this? A letter?"

    "Strange glyphs are written on the envelope. There is no recognizable name or address."

    $ MC.rand_say(("gd: I really shouldn't pry, but if I don't open it, I won't be able to bring it to its rightful recipient.", "ev: Great! Hopefully, I can use this to blackmail somebody.", "ne: Well, if someone is going to open this and make away with the content, it might as well be me..."))

    "Slicing the envelope open with your dagger, you are somewhat disappointed to find only a small piece of paper tucked inside, alongside a small charm amulet. It's the cheap kind you can find for a denar a dozen on Pilgrim Road."

    "Ignoring the amulet for now, you turn your attention to the piece of paper. A short message is scribbled on it."

    play sound s_dress

    call screen letter(header = "Burn after reading", message = "The merchandise is brought to the guild quarter on the first Tuesday of every month. Look for a private club called 'Mania', and show them the amulet.\n\nDon't expect any more intel from me, this is getting too dangerous. My cover is nearly blown, I'm out.",
                          signature = "DT")

    you "How mysterious... Merchandise? A private club? A cheesy charm? Who wrote this..."

    call receive_item(mania_amulet) from _call_receive_item_5

    "Shrugging, you pocket the envelope and its content."

    you "It doesn't make sense. Maybe if I drop by the {b}Guild Quarter{/b}, I'll investigate."

    $ story_add_event("stella_secret1")

    return

label stella_secret1():

    stop music fadeout 2.0

    "Fiddling in your pocket, you find the strange envelope you recovered from a dark alley."

    hide screen visit_location

    hide screen overlay

    play music m_oriental fadein 3.0

    you "'The merchandise is brought to the Guild Quarter on the first Tuesday of every month...'"

    you "Right, we are on the first Tuesday of the month. The letter said to look for a club called Mania..."

    "You ask a bunch of people, but no one seems to know or even have heard of the club."

    you "Strange..."

    "As you wander around the shabbier streets of the guild quarter, you notice half-a-dozen strong, well-built men, waiting in front of a two-story building."

    you "(Maybe I'll ask those guys the way...)"

    you "Ahem, mister?"

    "Hulk" "Grrrmmm... *grunt*"

    "Upon closer inspection, you can see that all the men lined up are larger than life: tall, muscular, with a brutish look about them. They stand here doing nothing, not chatting or anything. The silence is only broken when one farts or masticates loudly."

    you "Sir, do you know..."

    play sound s_moo

    "Large man" "Ngggh... *neigh*"

    you "(It's useless... None of them even speaks...)"

    "You are about to turn around and try your luck elsewhere, when you glimpse something hanging around the neck of the closest apeman."

    you "(Wait! I've seen this amulet before...)"

    "Looking at each of them in turn, you find that each one of them is wearing the same amulet. They seem unbothered by your curiosity."

    "Looking back at the large patriarchal house in front of which they are lining up, you notice a single word, etched in the sandstone above the doorstep."

    you "'Mania'..."

    play sound s_creak

    "The creaking sound of a key entering the doorlock surprises you. Someone is opening the door."

    you "(Quick, I need to do something!)"

    "Squeezing yourself in-between two grunts, you put the strange amulet around your neck, then try your best to look like a drooling idiot."

    play sound s_door
    scene black with fade

    "The door opens, but you cannot see anything inside."

    "Female voice" "This way. Come on in, pricks-for-brains..."

    "Moving as one, the big men enter the house, shuffling their feet. You do your best to imitate them."

    play sound s_vibro

    "*BUZZ*" with vpunch

    "As you pass the doorstep, you feel the small amulet vibrate. It isn't as cheap and useless as it looks."

    you "(Some kind of expensive security system... What have I got myself into?)"

    "Before you have a chance to reconsider your hasty decision, the metal door slams shut behind you."

    play sound s_crash
    with vpunch

    stop music fadeout 3.0

    with fade

    "..."

    show bg cell at top with dissolve

    "Following the herd, you find yourself in an empty room, and another door shuts down behind you."

    play sound s_close

    you "And now there's no way out... *gulp*"

    "The other men seem completely unfazed. Suddenly, they start removing their shirts as if prompted by a silent voice."

    you "Err... Folks?"

    "Then the hulks drop their pants, followed by their underwear. You can see their imposing manhoods are already erect."

    you "Guys, slow down, we've only just met..."

    "They pay no attention to you. Reflexively, some of the men start jerking their cocks, grunting loudly."

    you "Hahaha... Guys, guys can we {i}talk{/i} about this? I'm not rea-..."

    play sound s_open

    "The sound of the door opening catches you by surprise. You are the only one still dressed."

    you "Wha-..."

    play sound s_surprise

    "Female voice" "?!?"

    "Female voice" "YOU!!!" with vpunch

    play sound s_punch
    scene black with fade

    "An iron hand grips you by the neck and slams your back to the wall."

    play sound s_crash
    with vpunch

    show bg stella_wall1 at top with dissolve

    stella uniform "WHAT THE FUCK ARE YOU DOING HERE?!?"

    "Terrified after being caught, you can barely see your assailant. As you struggle to breathe, you eventually recognize a familiar face."

    you "S-Stella?"

    stella "SHUT THE FUCK UP! Why are you here, you prick?!?"

    you "I..."

    you "I found an unnamed envelope, and..."

    stella "WHAT? No... They were supposed to send... Not YOU, at least!" with vpunch

    you "I don't understand..."

    stella "Of course you don't! Shut up and let me think..."

    play sound s_creak

    "The sound of the main entrance door opening echoes from outside the room, and you hear voices. Stella looks panicked."

    stella "Damn you! They're here... Shut your damn mouth, and get naked, if you want to live!"

    you "Uh... What?"

    stella "GET YOUR ASS NAKED! NOW!!!" with vpunch

    scene black with fade
    show bg cell at top with dissolve
    show stella uniform at right with dissolve

    "You rip your clothes off frantically as the voices grow closer. You barely have time to get in line with the other naked men before two uniformed women enter the room."

    play sound s_door

    show blood1 at center with dissolve

    blood1 "Ah, Lieutenant. You're already here."

    show blood2 at left with dissolve

    stella "General Ka."

    blood2 "Dear Lieutenant Stella. Punctual, as always."

    stella "Thank you, Admiral Zee..."

    "Stella looks nervous. You've never seen her like this. She always looks like the one in charge."

    blood1 "I can see you brought us some entertainment... Some fine stallions you've got here..."

    "She squeezes the hard dick of the first man appreciatively. He doesn't flinch."

    blood1 "Good, strong men for the night... I was looking forward to it..."

    blood2 "By blood and secrets, you sure have a one-track mind..."

    play sound s_surprise

    blood1 "What is that?!?" with vpunch

    "The general spots you, and her eyes narrow."

    blood1 "What the hell is this? Are you raising midget stallions now?"

    stella "I, err... *frown*"

    stella "It's a... A new model... Some consumers requested a lighter, more portable version so we came out with a new design..."

    stella "We call it the... the Stallion 'XS'."

    you "..."

    "The general eyes you suspiciously."

    blood1 "What kind of wench would want a man with such a small dick and frail body? Are people really paying top denar for that?"

    stella "Oh, they do, General. I'm told it's quite a fad among Zanic nobility these days..."

    blood1 "I should have guessed... Decadent Zanic cunts."

    blood2 "My, General, don't be so harsh. To each their own."

    blood2 "Remember the homeland's saying: 'Every new vice is another chance to make money'."

    blood1 "..."

    blood2 "Look at this tiny stallion, he's adorable... He's like a... a pony!"

    stella "That's right, hahaha..."

    you "..."

    blood1 "He doesn't look like a stallion to me. For all we know, he could be a spy!"

    stella "Woah, General, I assure you, this isn't a spy... Hahaha... *nervous*" with vpunch

    "Stella gets a sudden burst of inspiration."

    stella "I mean, look into his eyes! Does that look like a sentient being to you?"

    blood1 "... *stares intensely*"

    blood1 "..."

    play sound s_sigh

    blood1 "You're right, of course. He's got the look of a complete dim-witted idiot."

    you "(Hey...)"

    stella "I assure you, he's dumb enough to eat his own dick."

    you "(Hey!)" with vpunch

    blood2 "He's obviously brainwashed. There's not a single spark of intelligence in there."

    blood1 "Yeah... I've seen goats with a cleverer look about them."

    you "(Stop it, already!!!)" with vpunch

    "You manage to retain your composure even as the insults pile up. And yet somehow, being abused by women in uniform turns you on."

    blood1 "Well, at least he looks like he has some potential down there..."

    "The blonde woman squeezes your dick so hard it hurts. You do your best not to show any reaction, but your cock gets harder."

    blood1 "So, are we gonna have this party now?"

    blood2 "Not yet! We have much to discuss first."

    stella "True. Let's move this to the command room."

    scene black with fade

    "The women lead the way, followed passively by the stallions. You do your best to imitate their behavior. After climbing a flight of stairs, you reach an office of some kind."

    show bg office at top with dissolve

    show blood1 at center
    show stella uniform at right
    show blood2 at left
    with dissolve

    play music m_mafia fadein 3.0

    blood1 "So. Can we hear the monthly report?"

    stella "Certainly, General."

    stella "We have made contacts with two new families. Our alliance now includes nearly a third of the nobles closest to the King."

    blood1 "What about you, Admiral Zee, how is the invasion planning going?"

    blood2 "The fleet is gathering, only a few vessels at a time... We don't want Zan's spies to get suspicious."

    blood2 "The ships are mooring in several friendly ports. When the time comes, we can gather them on a day's notice."

    blood1 "Is that enough to penetrate their defences? Zan's navy is not to be taken lightly..."

    blood2 "More than enough. I've got infiltrators in the ranks of the navy. They will make sure the large ships are rigged with firetraps, ready to blow when the time is right."

    blood2 "With the larger ships blocking the waterway, we can end the fight before it even begins. The element of surprise will be key."

    blood1 "What about the ground troops?"

    stella "Zan's forces are mostly comprised of sellswords and mercenaries. We can buy them off or break their morale easily."

    stella "The only force to be reckoned with are the knights. They have good training, good equipment, and a loyal and capable leader."

    blood1 "Our sorcerers can make short work of them."

    stella "Yes. The other factions bear no love for the King. We can win most of them over, and crush the rest."

    blood1 "Splendid. It seems to me the preparations are coming along well."

    stella "Yes."

    blood1 "Is it time to strike, then?"

    stella "Not yet. We are expecting more support among the highest levels of the court's advisors. Such schemes take a while to negotiate."

    stella "Also, we need a catalyzer. Some spectacular event that would allow us to move our pawns more quickly..."

    blood1 "So the powder keg is in place, but we are waiting for the spark?"

    stella "Precisely."

    blood1 "I shall report that to the council. They are content to bide their time for now... But we will only get one shot at this."

    stella "Yes, General."

    blood2 "Of course."

    stop music fadeout 2.0

    blood1 "Now..."


    blood1 "I believe someone mentioned a party? [emo_heart]"

    play sound s_laugh

    blood2 "Yes! *laugh*"

    stella "Of course..."

    blood1 "Let us have a drink to celebrate!"

    blood2 "Certainly! I am sooo thirsty!"

    "Stella turns to you with a mischievous smile."

    stella "Why don't we try a little pony juice?"

    blood2 "Oh, yes! I'm curious!"

    blood1 "Really? I was going to go for stronger stuff, but... okay."

    stella "Here here, little buddy..."

    scene black with fade

    play sound s_dodge

    "*SQUEEZE*" with vpunch

    show bg stella_wall2 with dissolve

    "Stella comes straight at your dick with her gloved hands."

    play sound s_crash
    with vpunch

    "You recoil and hit the wall. There is nowhere to go, and you cannot let yourself panic and blow your cover."

    stella "(That'll serve you right, you nosy prick!)"

    "Shoving her thigh between your legs, rubbing your balls, Stella pins you to the wall. Her hand grabs your cock as she produces a drinking glass."

    stella "Now, let's test this new Stallion XS... Let's get some man milk out of him."

    blood2 "Oh, yes!"

    blood1 "Hmm..."

    "You do your best to remain passive as she starts jerking you off with her customary brutality."

    play sound s_sucking

    "*plit* *plit*"

    "Your erect cock makes obscene sounds as she rubs your cock hard with her leather glove."

    stella "Ha! Enjoying yourself now, aren't you?"

    "You are aroused in spite of yourself as the rough treatment makes you experience a mix of pleasure and pain."

    play sound s_dodge

    "*spit*"

    "Stella spits on your cock to make it more slippery. Her grip tightens, and you feel closer to your limit."

    stella "Now, you better fill up that cup, or I'll cut your worthless balls off."

    you "Ngh..."

    "Stella wanks you harder and harder, rubbing her thigh harder. Finally, you feel a hot wave flow through you."

    you "Aaaah!"

    show bg stella_wall3 with flash

    "*SPURT*"

#    show bg stella_wall4 with doubleflash

    "You cum hard inside the glass, and Stella makes sure she catches every drop of semen."

    with flash

    "*SPURT* *SPURT*"

    show bg stella_wall4 with flash

    "You shoot more thick cum inside the glass, and Stella watches with perverted fascination as she squeezes the last drops out of you."

    play sound s_sigh

    stella "Hmmm..."

    show bg stella_wall5 with dissolve

    "When you are finally finished, Stella brings the glass to her lips without hesitation, and takes a sip. She plays with it in her mouth for a few seconds before gulping it down."

    play sound s_ahaa

    stella "Nicely salty, strong with a hint of spice... What do you know, this isn't half-bad."

    play sound s_surprise

    blood2 "Gimme some, gimme some! I want a taste."

    blood1 "What's wrong with you two? Did you forget I'm the ranking officer here?"

    "The blonde woman grabs the glass from Stella's hands and brings it to her lips."

    blood1 "*gulp* *gulp*"

    blood2 "Hey! You're drinking everything!!!"

    "Stella watches them with an amused face, licking the remaining semen from her glove."

    blood1 "Haaa... That was good."

    blood2 "You drank everything! What about me!"

    stella "Come on, Admiral, there's more where that came from... And I'll have you taste the others as well."

    blood2 "Yay! Cum-tasting night!"

    blood1 "Good, I'm still in need of a drink. I haven't had proper man juice since I left the homeland."

    stella "Another glass, then?"

    play sound s_girls_laugh

    "Girls" "Yes!!!" with vpunch

    scene black with fade

    "The partying women keep jerking more 'juice' out of you, until you are nearly passed out."

    "When the officers finally leave, Stella kicks you out in the street, barely giving you time to gather your clothes. She ignores all of your questions."

    play sound s_close

    you "What the fuck did I just get myself into..."

    $ MC.interactions = 0
    $ MC.change_prestige(4)

    "You have earned prestige. You have lost all your remaining actions for the night."

    $ story_add_event("stella_secret2")
    $ event_dict["stella_secret2"].date = calendar.time + 7

    $ NPC_stella.unlock_trainer()

    return

label stella_secret2():

    "Today is the first Tuesday of the month. You remember it is time for the officer meeting at the underground club, Mania."

    play music m_jazz fadein 3.0 fadeout 2.0

    "As it happens, you pass through the club's street, and notice a group of stallion-men are already lining up in front."

    menu :
        you "(Should I join them again, like the last time?)"

        "Infiltrate the club":
            you "Well... I'm too curious. I have to see what those women are up to."

            you "They might use my body as their toy again... But, err..."

            you "I'm totaly not enjoying this, but that's a risk I'll have to take... For... For Zan!"

            you "(Maybe they'll torture and spank me hard...)"

            "Embarrassingly, it looks like you have a boner already."

        "Ignore it":
            you "I don't have time to play S&M games with those crazy bitches."
            stop music fadeout 2.0

            return

    scene black with fade

    play sound s_vibro
    "Amulet" "*BUZZ*" with vpunch

    "Just like the last time, you follow the stallions inside as Stella opens the door."

    play sound s_surprise

    stella uniform "You..."

    "Stella looks at you with a mixture of defiance and amusement."

    stella "So you came back for more, uh? Kinky..."

    "She lets you in, but she hisses in your ear."

    stella "Don't you dare blow our cover, punk. Before you have a chance to compromise me, I'll silence you for good."

    you "*gulp*"

    show bg office at top with fade

    show blood1 at center
    show blood2 at left
    show stella uniform at right
    with dissolve

    "The officers meet up again around a set of maps and intelligence reports, but you cannot catch any meaningful information."

    "After they are finished, they turn to the group of stallions you are hiding in."

    blood2 "Look at that! The tiny one is back!"

    blood1 "Is he now? I guess his kind doesn't really fly off the shelf..."

    stella "Don't be mean-spirited, general. We're making a killing with the pocket-stallions. Anyway, ladies, pick your poison..."

    blood1 "Dibs on the largest dick! I want a hunk in my bed tonight... But wait... Shouldn't I pick a second one, as a side order?"

    blood2 "Hmm, which one should I choose..."

    stella "Sure, help yourself."

    "The women are picking stallions to join them in the bedrooms. This might be your chance to get closer."

    menu:
        "Stumble towards..."

        "Ka将军":
            "Trying to remain zombie-like, you stumble towards the lady-in-red."

            blood1 "Hey! The scrawny one is coming at me... Creepy!"

            blood2 "Aw, how adorable... It looks like it took a shine to you..."

            play sound s_sigh

            blood1 "Once again, I am the victim of my magnetic charisma. The night is long, I guess I can have him as an appetizer. But save Mr 12-inches for me!"

            call blood1_bj from _call_blood1_bj
            $ unlock_achievement("h ka")

        " Zee上将":
            "Pretending to be drifting aimlessly, you bump into Admiral Zee."

            play sound s_horn

            with vpunch

            blood2 "Hey!"

            play sound s_laugh

            blood2 "Look at this... It seems to be attracted to my titties..."

            "She pats your head."

            blood2 "You're just like a little kid, obsessed with mommy's boobs aren't you? Come here, Mamma's gonna take care of you."

            call blood2_tj from _call_blood2_tj
            $ unlock_achievement("h zee")

        "斯特拉中尉":
            "You gravitate little by little towards Stella."

            stella "Shhh! Bad boy! Go away!"

            "Playing dumb, you start rubbing against her leg."

            play sound s_laugh

            stella "S-Stop... It tickles! Aw, you stupid dog..."

            "She feels the length of your hard shaft against her thigh, and seems to think of something."

            stella "Horny, are you... I'm going to make sure you learn your lesson."

            call stella_bj from _call_stella_bj
            $ unlock_achievement("h stella")

    scene black with fade

    "..."

    with fade

    "When the women finally leave, you wait for a while then make your escape. Exhausted, you stumble out in the street."

    $ MC.interactions = 0
    $ MC.change_prestige(4)

    "You have earned prestige. You have lost all your remaining actions for the night."

    $ event_dict["stella_secret2"].date = calendar.time + 7 # Ensures one week will pass before the event pops again

    return


label blood1_bj():
    stop music fadeout 3.0

    $ renpy.block_rollback()

    scene black with fade
    show bg ka1 at top with dissolve

    blood1 "Well well well... This little guy is standing to attention, isn't he?"

    "She twists your cock around, looking at it from different angles."

    blood1 "You have to admire the know-how of the homeland, engineering such sex beasts... Even the tiny ones are impressive."

    you "..."

    blood1 "Let's see if I can make this miniature prick feel good."

    "Tapping your shaft lightly against her lips and breathing in, General Ka seems to enjoy your manly smell."

    show bg ka2 at top with dissolve

    "Taking your cock inside her mouth, Ka starts sucking on it noisily."

    play sound s_sucking

    blood1 "Hmmm, nghh..."

    "The feeling of being sucked off by a powerful military leader from a foreign country is amazing, and your dick gets harder as pre-cum starts leaking from it."

    blood1 "Twitching already... Not so fast... Ngggh..."

    "Taking out a leather strap from a bag, the general starts wrapping your cock tightly."

    play sound2 s_dress

    show bg ka3 at top with dissolve

    you "(Oh no! A cockblock!)"

    blood1 "There. Now I can take my time. You'll come when - and if - I say you can."

    "She starts licking the tip of your cock again, tingling your balls."

    you "(Nggh...)"

    "Your cock grows larger and the pain increases as the leather bites into your sensitive flesh."

    "General Ka enjoys watching as you struggle with your bonds."

    blood1 "It seems like you're about to burst... I'm going to torture you for a while."

    "Sucking harder on your cock, General Ka starts giving you deep throat. The feeling is amazing and you feel your cock is ready to explode."

    blood1 "Hahahaha... And what if I do this?"

    "Running her gloved fingers against your balls, she makes sure to tickle them to bring you past your limit."

    play sound2 s_evil_laugh

    blood1 "Muhahaha... Uh?"

    show bg ka4 at top with hpunch

    "Amazingly, the leather is starting to stretch, and the strap seems about to burst."

    blood1 "(Such a strong aura... Around his cock...)"

    with hpunch

    "The leather stretches even further, threatening to break any second now."

    blood1 "F-Fine, you can cum! Don't go and break my tools, now, you idiot!"

    play sound s_dress

    "She unties the cock-block bound in one skilled move."

    show bg ka5 at top with flash

    "*SPURT*"

    "As soon as General Ka releases the bindings, you shoot a bucketload of cum inside her mouth."

    play sound s_surprise
    with doubleflash

    blood1 "Nggh! Hnggg... *gulp* *gulp*"

    "Surprised as she is, Ka doesn't let a drop of cum slip away from her hungry mouth."

    with flash

    blood1 "*gulp* *gulp*... Haaa..."

    show bg ka5 at top with dissolve

    "Licking her lips, Ka looks at your still-erect cock appreciatively."

    play sound s_mmh

    blood1 "Hmmm... Delishioush..."

    with flash

    blood1 "(Wow!!! There's still more...) *gulp*"

    "Some semen trickles down her chin as she savors the taste of fresh, stinky cum in her mouth. She swallows it naughtily."

    play sound s_mmmh

    blood1 "This first course sure raised my appetite... I think I'm going to hold on to this little guy a while longer."

    play sound s_dodge

    "*GRIP*" with vpunch

    scene black with fade

    "Grabbing you by the cock, the general drags you to a side room. You emerge only hours later, squeezed dry..."

    return


label blood2_tj():
    stop music fadeout 3.0

    $ renpy.block_rollback()

    scene black with fade

    "Unbuttoning her shirt, Admiral Zee lets her massive boobs pop out of her tight uniform."

    show bg zee1 at top with dissolve

    blood2 "So you'd like a taste of Mamma's tits... I feel a maternal duty to oblige..."

    "Placing your hard cock between her mounds, Zee presses them together. You do your best not to squeal at the marvelous sensation of so much flesh encasing your dick."

    you "Nggh..."

    blood2 "What's the matter, my little pony? Feeling a little tense?"

    "Placing her gloved hands over your chest, Admiral Zee starts pinching your nipples between her fingers."

    you "Nghh!!" with vpunch

    play sound s_laugh

    blood2 "Look at that! Baby boy is really sensitive here..."

    "Zee starts moving slowly, gently rubbing your cock between her big tits. You can feel her soft skin rub against your dick."

    you "(Oooh...)"

    show bg zee2 at top with dissolve

    play sound s_sigh

    blood2 "Oh..."

    blood2 "What's that... Something is leaking from my baby boy's weenie..."

    "Pre-cum starts running down the curve of her breast."

    show bg zee3 at top with dissolve

    blood2 "How convenient... Natural lube for Mamma's tits..."

    "Spreading your pre-cum all over her tits, Zee makes her cleavage all slippery, increasing the pace of her titfuck."

    "*PLIT*"

    blood2 "Mamma feels good feeling her baby's juice against her skin... Can you give Mamma some more?"

    with hpunch

    "Waving her boobs from left to right, Zee makes sure to increase the sensation in your dick as she pinches your nipples playfully."

    play sound s_aaah

    blood2 "Mamma wants it... Give it to Mamma..."

    "The pressure becomes too much for you to endure, and you do your best to keep yourself from screaming as you feel a powerful orgasm build up."

    "Pressing her chest down, Zee squeezes your cock deeply between her mounds."

    blood2 "Gimme some love juice, baby boy..."

    show bg zee4 at top with flash

    "*SPURT*"

    play sound s_surprise

    blood2 "Aah! [emo_heart]"

    play sound s_ahaa
    with doubleflash

    blood2 "Ahaa... So much..."

    show bg zee5 at top with flash

    "Admiral Zee's tits are smeared with your thick cum. She gently squeezes her boobs together, milking the last drops of semen out of you."

    with flash

    blood2 "Oh my... My bra is completely soaked with smelly pony cum now..."

    play sound s_laugh

    blood2 "I love it! [emo_heart]"

    blood2 "Now, little darling, will you make Mamma's panties smell like that too? *purr*"

    scene black with fade

    "Admiral Zee keeps playing with you until you are completely drained."

    return


label stella_bj():
    stop music fadeout 3.0

    $ renpy.block_rollback()

    scene black with fade

    "*clink*"

    show bg stella_wall2 at top with dissolve

    "Pinning you to the wall, Stella grabs a glass... And your dick."

    stella "You know what's coming, don't you... Don't make it hard on yourself."

    "Jerking you off with rough and efficient moves, Stella wastes no time bringing you off a first time."

    show bg stella_wall3 at top with flash

    you "Ha! *grunt*"

    show bg stella_wall4 at top with doubleflash

    "You keep cumming hard into the glass, and Stella keeps jerking you, giving you no respite until you cum a second time."

    you "NGGGGH... *moan*"

    stella "Boy... I didn't know you had it in you. Looks like you filled that glass proper."

    show bg stella_wall5 at top with flash

    "Making sure she doesn't drop any, Stella puts the glass down on a night table."

    stella "I'm saving this one for later. I like a glass of man milk before going to bed..."

    you "..."

    "Tired, you start looking around for a way to make your exit."

    play sound s_surprise

    stella "Hey!"

    "Stella yells at you in a commanding voice, startling you."

    stella "You puny little creature, don't even think that we're done here."

    you "!!!"

    show bg stella_bj1 at top with fade

    "Squatting before you, Stella brings her face only an inch from your dirty, smelly cock. You can feel her silky hair caress your shaft lightly."

    stella "Let's see how far I can bring you this time..."

    "*PLIC*" with vpunch

    "Licking her gloved finger, Stella pushes it straight inside your butthole."

    you "Hey!!!" with vpunch

    "She teases your anus, moving her finger in a circle."

    stella "What's the matter, you're a brainwashed stallion, remember? Surely you won't object to your mistress doing whatever she wants to you?"

    stella "Or should I tell the others who you are..."

    you "*gulp*"

    stella "I told you. I'm going to push things further..."

    "She licks her lips."

    stella "Come here."

    show bg stella_bj2 at top with fade

    "Taking your dick in her mouth, Stella slides her finger deeper inside you."

    you "NGGH!!!"

    "The sensation is overwhelming, but it's hard to complain as she noisily laps up your cock with her wet tongue."

    play sound s_mmmh

    stella "Hmmm... The tashte of shemen always turns me on..."

    play sound s_sucking

    "Pulling you towards her using her finger as a hook, she pushes your cock deeper inside her throat."

    stella "Nggh, ngh, nggggh..."

    "Moving her finger inside you, raping your ass, Stella covers your cock with her wet saliva."

    stella "More... Hmmmm..."

    "Stella swallows the whole length of your shaft, your cock hitting the walls of her throat. She has no gag reflexes whatsoever."

    play sound s_aaah

    stella "Ngggh... Aaah..."

    "The obscene noises of your juices mixing with her saliva is enough to push you over the edge, as she increases her fingering movement and sucks really hard on your throbbing cock."

    you "*GRUNT*" with vpunch

    show bg stella_bj3 at top with flash

    "You didn't think it was possible, but you come - again."

    with doubleflash

    "*SPURT* *SPURT*"

    stella "Ngggh... *suck* *gulp*"

    "Stella welcomes the thick cum oozing in her mouth and swallows it noisily."

    stella "There's sho much... Nggh..."

    "She lets the cum drip down her throat, looking into your eyes as you finish shooting your load."

    show bg stella_bj4 at top with fade

    "When she finally lets your cock pop out of her mouth, cum is still dripping from her lips. She licks it naughtily."

    stella "What do you know... Maybe you'd make a good stallion after all... A pity your training started so late."

    play sound s_ahaa

    stella "Hmmm... There was a lot... I feel almost full."

    stella "Look at it go... It's still rock-hard..."

    "Her finger is still feeling inside your butt. Cupping your balls, she takes one in her mouth."

    stella "Ngggh... Let's shee how much is left in there..."

    play sound s_aaah

    scene black with fade

    "Stella torments you with various techniques until you don't have a drop of semen left."

    return


label farm_meet_willow():

    play music m_suspense fadein 3.0

    scene black
    show bg inner_sewers at top
    with fade

    you "Damn, I'm completely lost..."

    "Once again, you curse your own stupidity."

    you "What was I thinking, coming down into these dark, stinky tunnels?"

    scene black
    with Pixellate(2.0, 5)

    "You hark back to the reason you ended up in these filthy sewers."

    show bg sewers at top
    show sill at center
    with Pixellate(2.0, 5)

    sill happy "Master! Isn't nice to have some time to take a walk together?"

    sill "It's almost as if we were... Mmmh."

    sill "Although I wish we'd gone to a nicer place... Maybe the lake, or the gardens, or the beach? Oh, I wanna swim in the ocean!"

    you "What are you rambling about again, Sill?"

    you "We have errands to run, remember? Lots of heavy stuff to carry. That's why I brought you."

    sill sad "Aw, don't remind me..."

    sill happy "Oh, Master! Look, what's this?"

    "Standing behind a makeshift stall, a peddler is displaying various items of jewelry."

    sill "Oh, Master, look at this one! Isn't it beautiful?"

    you "Uh, yeah, sure..."

    "Sill lifts a silver armlet from the display, putting it on her wrist."

    sill "Master, it suits me really well, don't you think?"

    sill "Can I... Can I have it?"

    you "Sill..."

    sill sad "Pleaaaaaaaaaaase..."

    "Sill is looking at you with shiny puppy eyes. She's good at this."

    menu:
        sill "Master, please, can I have it?"

        "当然了(50金币)":
            you "All right, I guess with all your hard work, you deserve a present from time to time."
            $ MC.good += 1
            $ NPC_sill.love += 1

            play sound s_gold
            $ MC.gold -= 50

            $ bought = True


        "你得自己买单":
            you "You can buy it with your own pocket money. I'm not your boyfriend."
            $ MC.neutral += 1

            sill "Aw..."

            sill "It's so expensive... But it's so pretty..."

            sill "All right... I'll just eat white rice for the next two weeks, then."

            sill happy "I'm buying this, old man!"

            $ bought = True

        "当然不行了":
            you "Absolutely not. As a slave, you don't get to choose what you wear. I do."
            $ MC.evil += 1
            $ NPC_sill.love -= 1

            sill sad "Master! Please!"

            you "Sill, stop whining. We've got stuff to do. Put this armlet back where it was and let's go."

            $ bought = False

    $ renpy.block_rollback()

    if bought:

        with fade

        "Sill springs alongside you, beaming as she admires her new item."

        sill happy "Oh, Master, I love it so much..."

        you "That's nice, that's nice..."

        you "Say, isn't it a little too large for your arm?"

        sill "It's not! Look, it doesn't go away, I can even shake my arm like this..."

        with vpunch

        play sound s_dodge

        pause 0.2

        sill sad "AAAH!!!"

        "Slipping from her wrist, the roundish armlet falls on the ground and starts rolling away from her."

        play sound s_scream

        sill "NOOOOOOO!!!" with vpunch

        "Before you have a chance to react, the bracelet rolls straight past a cast-iron grate, falling down into the sewers."

        "Sill runs to the grate, looking down into the darkness. The armlet is nowhere to be seen."

        you "Sill, you clumsy fool!" with vpunch

        "Sill turns around towards you, and her eyes fill with tears."

        sill "..."

        sill "......"

        sill "UWAAAAAAAH!!!" with vpunch

        "Sill starts crying like a fountain, her wailing so loud people from the other end of the street turn to look at you two disapprovingly."

        sill "I'm so dumb... UWAAAAAH!!!" with vpunch

        "You struggle to find words to calm her down."

        you "Come on, Sill, it's not the end of the world..."

        sill "B-b-but... This was the best thing I have ever owned... It was a memory of the time I was enjoying a walk with Master..."

        you "Err, technically it wasn't a very old memory..."

        sill "Now it's gone FOREVER... UWAAAAH!!!"

        you "Come on, it's not like that..."

        sill "IT IS! UWAAAH!!!"

        you "Look, uh, it probably didn't fall far, anyway. I could have a look if you really wanted..."

        show sill sad at jumping

        "Sill instantly interrupts her wailing and looks at you with gigantic, mirror-like puppy eyes."

        sill "M-Master... You would do that for me? Go down and take a look?"

        you "Well, I mean, we don't really have time..."

        sill "UWAAAH!!!" with vpunch

        you "...but sure, sure, don't cry, I'll have a look, ok? Now stop!"

        sill "Oh, Master..."

    else:

        "Looking defeated, Sill moves to place the armlet back on the stall."

        play sound s_surprise

        sill sad "Ah!" with vpunch

        "Unfortunately, she didn't notice the uneven pavement in front of her. She stumbles."

        play sound s_dodge

        "Slipping from her hand, the armlet falls on the ground, rolling straight into a sewer grate."

        play sound s_surprise

        sill "Oh no!"

        you "Sill, you imbecile!!!" with vpunch

        you "Damn..."

        "Peddler" "Hey, you!" with vpunch

        you "Curses..."

        "Peddler" "You're going to pay for this, aren't you?"

        you "Come on, my good man, I'm sure it didn't fall far..."

        "Peddler" "Oh yeah? Then you go and look for it. I'm not going down into this stinking, haunted shithole."

        you "*grumble* Young lady, when I come back, you're gonna get a good talking to!"

        sill "Aw... *gulp*"

    scene black with Pixellate(2.0, 5)

    "And that's how you ended up in these stupid sewers."

    show bg inner_sewers at top with Pixellate(2.0, 5)

    $ MC.rand_say(("ev: It's all Sill's damn fault!", "ne: Serves me right for trying to help.", "gd: Sill can be so clumsy sometimes..."))

    "After you came down into the sewers, you couldn't find the armlet close by after all."

    "But you found a trail of sorts. Some kind of critter attracted to shiny objects might have taken it, like a rat or something."

    you "It looks like... Slime... Ew..."

    "After following the slimy tracks for long minutes, you kind of lost sense of where you were."

    you "Damn..."

    you "It's not worth going through all this trouble for a 50 denar trinket. I'm out of here."

    "As you turn around, though, you find it impossible to remember where you actually came from."

    "You try to look for the tracks that led you here, but your torchlight is waning."

    you "This isn't good..."

    play sound s_mystery

    "That's when you hear a slurpy sound, coming from behind you."

    you "Uh?"

    play music m_danger_loop fadein 3.0

    show sewer_monster at truecenter
    with dissolve

    "Sewer monster" "GOOOOH..."

    you "HAAA!" with vpunch

    you "What... What the fuck is that?"

    play sound s_fizzle

    show sewer_monster:
        linear 0.5 xoffset -xres(100) yoffset yres(75)

    "A slimy, spooky creature is moving towards you, waving its weird antennas back and forth."

    "Sewer monster" "GOOH...    "

    "The monster seems poised to attack you. It's time to defend yourself."

    menu:
        "The monster seems poised to attack you. It's time to defend yourself."

        "和怪物战斗":
            show sewer_monster as sewer_monster2 at truecenter:
                xoffset -xres(100) yoffset yres(75)
            play sound s_sheath

            you "I'll slice your slimy butt in half!"

            play sound s_dodge

            you "DAAAH!" with vpunch

            "Your blow cuts the creature neatly into two halves."

            show sewer_monster at totheleft with move:
                yoffset -yres(150)
                linear 1.0 zoom 0.65
            show sewer_monster as sewer_monster2 at totheright with move:
                yoffset -yres(150)
                linear 1.0 zoom 0.65

            you "Uh... What?"

            "It isn't enough to stop it, however. Both halves of the monster keep moving."

            you "What... What is this bullshit?"

            play sound s_fizzle

            show sewer_monster at center with move
            show sewer_monster as sewer_monster2 at center with move
            hide sewer_monster2
            show sewer_monster at center:
                linear 1.0 yoffset yres(50) zoom 1.5

            "Both halves regroup and reform as a whole."

        "念动咒语":

            play sound s_spell

            you "Eat this, you degenerate slimeball..."

            play sound s_fire

            you "Fire in the hole!" with vpunch

            "You cast a mighty fireball straight into the monster's face."

            with flash

            play sound s_fizzle

            you "Uh?"

            play sound s_fizzle

            show sewer_monster at truecenter:
                linear 1.0 zoom 1.5
#                linear 1.0 zoom 1.0

            "The monster opens his maw wide, mouthing your fireball in just one gulp. It then grows even larger than before."

            you "HAAAA!"

            $ story_flags["willow fight cast fire"] = True

        "调头就跑":

            you "I'm not about to risk my life for a bloody trinket. I'm out of here!"

            "Flipping around, you start running as fast as you can from the slimy creature."

            "It is quite slow, anyway, so you have no problems outpacing it."

            you "So long, sucker..."

            extend " HAAA!" with vpunch

            "Slipping, you fall flat on the ground."

            "You realize it is covered with slippery slime."

            you "What the..."

            "Trying desperately to get up, you keep slipping and falling again. It's like the ground is covered in grease..."

            "Sewer monster" "GOoOoOH..."

            you "NO!!!" with vpunch

    "The monster approaches."

    play sound s_fizzle

    show sewer_monster:
        linear 0.5 xalign 1.1 yalign 1.0 zoom 1.9

    "You find yourself with your back to the wall as the creature's antennas reach forward, almost touching your face..."

    you "Get away from me!!!"

    play sound s_fizzle

    show sewer_monster:
        linear 0.5 xalign 0.0 yalign 0.5 zoom 3.0

    "Is this it? Are you going to meet your end here, devoured by a nasty slimeball?"

    willow "Hey!"

    show willow behind sewer_monster with dissolve:
        xalign 0.0 yalign 1.0

    "Sewer monster" "GOOOH?"

    "A girl appears behind the monster. She talks to you with a commanding voice."

    willow "Duck!"

    scene bg willow_cast with dissolve

    "Following her orders, you throw yourself to the side, slipping away from the monster's grasp at the last instant."

    willow "Watch out..."

    play sound s_spell

    willow "SOUL FIRE!!!" with vpunch

    if story_flags["willow fight cast fire"]:
        you "Wait! Fire doesn't..."
    else:
        you "Yes! Kill it with..."

    play sound s_fire
    pause 0.2
    play sound2 s_fire
    pause 0.1
    play sound3 s_fire

    "Before you have a chance to finish your sentence, the tunnel is engulfed in complete inferno." with flash

    play sound s_fire
    pause 0.2
    play sound2 s_fire
    scene bg willow_fire with doubleflash

    you "Aaah!!!" with vpunch

    play sound s_laugh

    willow "Hahahaha!"

    scene black
    show bg inner_sewers at top
    show sewer_monster at truecenter:
        xoffset -xres(100) yoffset yres(75)
    with dissolve

    play sound s_roar

    "Sewer monster" "GOOOOooOooH!!!"

    stop music fadeout 3.0
    hide sewer_monster with pixellate

    you "It... It worked..."

    you "Wait... What?"

    show sewer_monster happy at truecenter with pixellate:
        xoffset -xres(100) yoffset yres(75)

    "Instead of burning in the flames, the monster takes on a pinkish glow."

    "It looks like... It's smiling?"

    you "Watch out!"

    show sewer_monster happy at truecenter with move:
        xoffset xres(100) yoffset 0

    show willow at left with dissolve

    play music m_suspense fadein 3.0

    willow "Oh, how interesting... A slimochu..."

    willow "Are you all right?"

    you "I am, thanks..."

    willow "I wasn't talking to you."

    "The girl opens her arms, giving the slimy creature a warm smile."

    willow "Come here, sweety. Willow loves you... Willow is going to find you a good home."

    $ willow_name = "Willow"

    play sound s_fizzle

    show sewer_monster happy at truecenter with move:
        xoffset -xres(50) yoffset yres(50)

    you "Wait, what?"

    "The woman pats the monster's slimy head with her hand, soothing the creature."

    "You can almost hear it... Purring."

    you "What the hell, lady? You didn't kill it?"

    willow "What, kill it? Are you crazy?"

    willow "I just cast a soul bonding spell."

    willow "A slimochu is way too valuable these days... They are an endangered species!"

    you "Well... I'm kind of glad to hear that."

    willow "My, look at you... You're covered in slime. You're going to need a good bath!"

    you "Indeed..."

    "You take a good look at your rescuer."

    "She seems like a young girl, but there are some strange things about her."

    "She sports a pair of animals ears on top of her head. They're probably just accessories, but you could swear you saw them move, as if by her own volition."

    "Also, her front teeth are really pointy."

    you "You... Who are you?"

    willow "I'm Willow. I'm a monster catcher."

    you "A... Monster catcher?"

    willow "Yes. I catch live monsters, and sell them for a good price. The sewers are a perfect hunting ground, what with all the creatures living down here..."

    you "You mean... People actually buy monsters?"

    willow "Oh, yes... Magicians need them for their experiments, of course, and other people for their, er, leisure."

    you "Leisure?"

    play sound s_laugh

    willow "Yes. It doesn't concern me what they do with them, as long as they pay well. *giggle*"

    you "I see..."

    "You think about this for a minute. Gizel... The farm..."

    you "Actually, I think I know someone who might be interested. Would you sell me some monsters?"

    willow "Provided you have the coin, sure, why not?"

    you "That's great. Err... You wouldn't happen to know the way out of here, now, would you?"

    willow "Follow me. I'll show you where my house is on the way out."

    hide willow with dissolve

#    "She pinches her nose."

#    willow "And... You could definitely use that bath."

    if bought:

        play sound s_fizzle

        show sewer_monster happy:
            linear 1.0 zoom 1.5 xalign 0.5 yalign 1.0

        "As you prepare to leave, you feel a tap on your shoulder."

        "Friendly sewer monster" "GoOooOoh..."

        "The monster extends an antenna towards you. On it, you see the silver armlet Sill dropped earlier on."

        you "There it is! Thanks, little fella."

        "You notice the armlet is glowing with a strange light."

        you "It's all slimy and weird, now... Anyway. Sill will be thrilled to have it back."

    stop music fadeout 3.0

    scene black with fade

    $ sewers.action = True
    $ unlocked_shops.append(NPC_willow)

    "You may now buy {b}monsters{/b} at the sewers."
    $ unlock_achievement("merchant willow")

    return

label willow_fight(): # This event will happen somewhere in the city after a monster has been captured for Willow.

    if not junkyard.action: # Gina must have met the MC for this series of events to proc
        return

    hide screen visit_location
    with fade

    $ loc = selected_location.name.lower()

    "Exploring the outskirts of the [loc], you notice something strange."

    you "Uh? What's this?"

    "You spot some slimy traces on the ground, leading away from your location through a narrow and dark side path."

    menu:
        "What do you do?"

        "循迹而行":
            you "I wonder where this leads..."

        "无视它们":
            you "Yeah, no."

            return

    "The slime trail continues all the way to a gaping opening in a nearby wall. A stone path descends into darkness."

    if not NPC_willow.flags["seen fight"]: # First scene

        you "It's probably a good idea to go down this dark path alone, without knowing what's inside. After all, there might be treasure, and I wouldn't want to share."

        "You step inside confidently, igniting a torch to light your way."


        scene black with fade
        show bg cave at top with dissolve


        "You keep descending below the surface along the stone path, still seeing traces of slime on the ground and walls as you go deeper. You start having an uneasy feeling."

        play sound s_mystery

        you "Uh... Hello?"

        you "..."

        play sound s_roar

        pause 1.0

        play sound2 s_surprise

        you "!?!"

        "This time, you distinctly heard something."

        "Moved by curiosity, you turn a corner, and..."

    else:

        you "This looks familiar. Let's take a look..."

        scene black with fade
        show bg cave at top with dissolve


        play sound s_roar

        "Monster sound" "ROAAAAR!!!" with vpunch

        play sound s_evil_laugh

        "Girl voice" "Come back here you stupid critter! You're mine!"

        you "Another monster... And I guess Willow is down there."

        "Curiosity getting the best of you, you descend into darkness..."

        with fade

    show tentacle_monster at right with dissolve
    show willow at left with dissolve

    if not NPC_willow.flags["seen fight"]: # First scene

        willow "Look buddy, I just want to capture you... It doesn't need to be a big deal..."

        play sound s_roar
        with vpunch

        "Slimy monster" "*roar*"


        willow "*sigh* Have it your way."

        hide willow
        hide tentacle_monster
        show bg willow_cast at top
        with dissolve

        willow "I'M GOING TO BLAST YOUR FACE OFF..."

        extend "... WITH A PACIFYING SPELL!!!" with vpunch

        "You were expecting fireworks. That's a letdown."

        willow "Take that... Uh?"

        play sound s_surprise

        "As she was focussing her spell, Willow didn't notice a tentacle creeping from behind her."

        play sound s_dodge

        "Before she can react, the tentacle wraps firmly around her leg."

        willow "Hey, no fair! Let it go!"

        play sound s_dodge

        pause 0.5

        play sound s_crash
        with vpunch

        hide bg
        show bg cave
        with dissolve
        show tentacle_monster at right with dissolve
        show willow at left with dissolve

        willow "UWAAAH!"

        hide willow with easeoutleft

        "The tentacle yanks Willow backwards, and she falls flat on the ground, unable to cast her spell."

    else:
        play sound s_surprise
        willow "I got you now! Uh?"

        play sound s_crash
        with vpunch

        "Willow didn't see the tentacles creeping from behind and got caught by the monster."

        play sound s_dodge
        hide willow with easeoutleft

        $ MC.rand_say(["Again? Really?", "Oh no, not again...", "Again! What kind of monster hunter {i}are{/i} you?!?"])

    "Effortlessly, the monster lifts Willow in the air, with her head upside down and her skirt overturned. You catch a good view of her panties."

    you "Hmm... Pink."

    "Other tentacles start wrapping around Willow's limbs, preventing her from escaping. She is in a precarious position."

    willow "Err, easy boy! I'm sure we can come to an agreement!"

    "A probing tentacle crawls up her leg with a squishy sound, reaching inside her panties."

    play sound s_woman_scream

    willow "EEK!!!"

    menu:
        "What do you do?"

        "火速支援":
            $ MC.evil -= 1

            you "Damsel in distress! I got this!"

            "Stepping out of the tunnel's shadows, you challenge the foul beast."

            you "Hold on, Willow! I've got your back!"

            play sound s_roar

            "The monster doesn't seem happy at all about the interruption. Half a dozen tentacles leap out to meet you."

            # Pick challenge
            $ tt = show_tt("top_right")
            $ chal = renpy.call_screen("challenge_menu", challenges=[("Fight the monster", "fight", 5), ("Blast it with a spell", "cast", 7)])
            hide screen tool

            if chal == "fight":

                play sound s_sheath
                "Drawing your weapon, you fend off the first tentacle attacks."

                # Run challenge
                call challenge(chal, 5) from _call_challenge_47 # result is stored in the _return variable
                $ r = _return
                play sound s_dodge

                pause 0.2

                if r:
                    play sound2 s_sheath
                    with flash

                    "Evading the clumsy appendages, you aim at the tentacles holding Willow and slice them off."

                    play sound s_crash
                    with vpunch

                    willow "Ouch!"

                    play sound s_roar

                    "The monster roars in pain and fury. It takes a moment to recover."

                else:
                    play sound s_dodge

                    "You dodge the first few tentacles but soon, half a dozen more are coming for you."

                    you "Willow!"

                    play sound s_clash

                    pause 0.4

                    play sound2 s_clash

                    "You parry the attacks with difficulty, as the monster forces you on the defensive."


            elif chal == "cast":

                play sound s_dodge
                "Taking a step back to keep the tentacles at bay, you start preparing a battle spell."

                # Run challenge
                call challenge(chal, 7) from _call_challenge_48 # result is stored in the _return variable
                $ r = _return

                if r:
                    play sound s_thunder
                    with flash

                    "A flash of lightning illuminates the tunnel, slicing through a bunch of monster tentacles."

                    play sound s_roar

                    pause 0.3

                    play sound s_punch
                    with vpunch

                    willow "Ouch! Hey!"

                    "The monster roars in pain and lets go of Willow. Your spell has stunned the beast for a fleeting moment."

                else:
                    play sound s_fizzle

                    "The constant lashing of tentacles forces you to stay focused on your footwork, unable to finish your spell."

                    play sound s_dodge

                    pause 0.2

                    play sound2 s_dodge

                    you "Damn it... *dodging*"

            if r:

                "Willow frees herself from the cut off tentacles, throwing out the one in her panties with disgust. She regains her footing and joins you."

                show willow at left with dissolve

                willow "[MC.name]! It's good you came."

                you "You bet... Let's finish this thing."

                play sound s_surprise

                willow "No! It's the eye of the deflowerer, a rare and valuable monster. We need to capture it."

                play sound s_roar

                you "Nonsense! It will tear us to pieces..."

                willow "Have a little faith. I just need you to pin it down a minute. Please don't do any more damage to it though. It loses value with every tentacle you slice."

                play sound s_dodge

                you "*dodging* You think it's that easy!"

                willow "Aw, please, do it for me okay?"

                play sound s_clash

                you "*grumbling* I hope you know what you're doing..."

                play sound s_dodge

                "Dodging another attack, you decide to rush your opponent to buy Willow some time."

                you "DAAAH!!!"

                play sound s_punch
                with vpunch

                "Leaping at your target while avoiding its tentacles, you bash into the creature's squishy core, sending it and you tumbling down in the tunnel."

                play sound s_crash
                with vpunch

                you "Ouch..."

                "Before you can get back on your feet, a tentacle wraps around your throat and starts choking you."

                play sound s_punch

                you "Aargh... *choking*" with hpunch

                you "(Is this how it ends?)"

                "Another tentacle creeps out from behind you and starts poking your butt."

                if MC.god:
                    you "[MC.god]!!!" with vpunch
                else:
                    you "What the f...!!!" with vpunch

                "The tentacle tries to find its way inside your pants."

                you "Is THIS how it ends?!? *panic*"

                you "Wait! I never signed up for that! Tentacle rape should {i}not{/i} involve the hero!!!"

                scene black with fade

                play sound s_evil_laugh

                show bg willow upskirt at top with dissolve

                "With your head upside down, you catch a glimpse of Willow as she prepares a spell."

                willow "PACIFYING BLAST... EXPLOSION OF PEACE!!!" with vpunch

                play sound s_fire

                "*WOOSH*" with flash

                play sound s_crash
                with vpunch

                "A bolt of white light hits you and the monster. The shock blasts you out of consciousness."

                scene black with fade

                call willow_recovery() from _call_willow_recovery

                $ NPC_willow.love += 3

            else:
                play sound s_scream

                willow "Aaah!"

                "The monster sends still more tentacles your way. Willow takes advantage of the distraction to free one of her arms."

                willow "Take this, you dumb critter!"

                play sound s_fire
                with flash

                "Willow blasts the monster with a firebolt and the smell of burnt monster flesh reaches your nostrils." with vpunch

                play sound s_roar

                "The burn hurts the monster and it growls in pain, letting Willow go."

                play sound2 s_crash
                with vpunch

                willow "Ouch!"

                play sound s_roar
                hide tentacle_monster with dissolve

                "Roaring defiantly, the monster retreats into the dark tunnel. You and Willow are too battered to give chase."

                show willow with dissolve

                you "Hey, Willow! are you all right?"

                play sound s_surprise

                willow "No..."

                you "Where are you hurt?"

                willow "My pride..."

                you "Oh. That's not usually lethal."

                willow "I was so close! I tracked this one for days..."

                willow "It's going to be weeks before it surfaces again... All this work for nothing..."

                you "Well... At least we are in one piece."

                willow "Yes. I owe you thanks."

                willow "You really saved my ass out here... Literally, I suspect."

                willow "Let's get out of here. And get a drink or ten. It's on me."

                scene black with fade

                "You spend a couple of hours getting drunk with Willow. You have used all your remaining actions for today.\nBut, hey, the booze was free."

                $ NPC_willow.love += 1

        "吃瓜看戏":
            $ MC.good -= 1
            $ see_ev = True

            if is_censored("monster"):
                menu:
                    "Skip event? (monster)"

                    "是":
                        $ see_ev = False
                    "否":
                        pass

            if see_ev:
                you "(This ain't my fight. But I'll just stay and keep watch... In case something interesting happens.)"

                "While Willow struggles powerlessly against the tentacle monster, you look on comfortably from a corner."

                "You watch in anticipation as the monster tears Willow's clothes off and spreads her legs apart, exposing her soft body to its hungry tentacles."

                scene black with fade
                show bg willow rape at top with dissolve

                if not NPC_willow.flags["seen rape"]: # First scene

                    $ NPC_willow.flags["seen rape"] = True

                    willow "B-Bastard! Get off me!"

                    "More tentacles converge on Willow, their wriggling, rough texture coarsely touching her exposed skin."

                    willow "Let me gooo... Ugh!!!"

                    "Another tentacle wraps around her neck, holding her tightly and cutting her rant off. At first, you worry it might be strangling her."

                    "But instead, it seems to be holding her head up, as if the creature wants her to see what comes next."

                    play sound s_scream_loud

                    willow "N-No... *cough*"

                    "Lifting her legs in the air, the creature spreads them wide, while the tentacle wriggling inside her panties slowly pulls them off."

                    willow "Nggh..."

                    "Willow's protestations are weak. She understands what she's in for."

                    "A thick tentacle covered with smaller tendrils lifts between her legs and places itself at the entrance of her cunt."

                    willow "P-Please... *cough* No!!!"

                    play sound s_scream

                    "Ignoring her plea, the beast pokes her vagina, while a tendril latches onto her clit."

                    play sound s_screams

                    willow "Oh! Ah! Aaah!"

                    play sound s_sucking

                    "The tendril makes a wet noise as it rubs over her mound. Willow is starting to lose it."

                    willow "What... are... you... doing... Aaaah..."

                    "Taking advantage of Willow's weakened state, the monster greedily pushes his thick tentacle inside her tiny pussy."

                    play sound s_scream_loud
                    with hpunch

                    willow "AAAAAH!!! You're tearing me apart!"

                    with hpunch
                    "Willow screams and her eyes widen, but the tentacle keeps coming, oddly fitting its bulky length inside the girl's tiny pussy."

                    "Her belly inflates in a grotesque way as the squishy tentacle fills all available space."

                    with hpunch
                    willow "Uhng! AAH!!!"

                    "Willow's eyes roll backwards as she takes the tentacle deeper and deeper."

                    "As the thick tentacle starts pumping in and out of Willow, smaller tentacles hover over her, oozing with a thick and slimy white substance."

                    "Eventually, Willow is covered with the monster's juice, which seems to slowly dissolve the clothes it touches, even though it doesn't seem to hurt her."

                    play sound s_moans

                    "As Willow is being noisily fucked by the monster, a longer and thinner tentacle rears its head unnoticed by Willow, aiming for her pink anus."

                    play sound2 s_scream

                    willow "AAAAAH!!!" with hpunch

                    "Caught completely by surprise, Willow screams as the second tentacle forces its way inside her ass, spurting juice inside as a way of lubrifying her tiny hole."

                    willow "Nggggh!!!" with hpunch


                else:

                    you "(Damn, I should have brought a beer.)"

                    play sound s_screams
                    with hpunch

                    "As such beasts are wont to do, the monster then proceeds with mercilessly raping Willow's exposed pussy and ass for over an hour, only briefly pausing to spurt a wad of monster cum somewhere on her delicate white body."

                    "Willow endures as best she can, and something tells you it's not be the first time she ends up on the losing side of a fight with a sleazy monster."

                    "Her pussy and ass take a good beating, until she is driven to complete exhaustion. You still wonder if she isn't somewhat enjoying it."

            scene bg cave with fade

            "After fucking her for well over an hour, the monster eventually seems sated."

            "He unceremoniously drops Willow in a pool of gooey semen, and slowly creeps back into the lower tunnels. You could almost swear you heard it whistling as it went."

            willow "Ughh..."

            "Willow is left by herself on the soiled floor, hardly breathing, monster cum oozing from her every hole. You take pity on her."

            if MC.get_alignment() == "evil":
                you "I'd better get her back. Otherwise, who is going to sell me new monsters?"
            else:
                you "Poor thing. I should at least get her safely home."

            "You go to Willow and help her clean up with the remains of her torn clothing, before taking her on your back like a sack of turnips and bringing her back to the surface."

            willow "You..."

            willow "You were there the whole time... I know!"

            willow "You could have helped..."

            "She sounds more exhausted than angry."

            you "Hey, it's not my job to fight monsters. This is supposed to be your thing."

            willow "Aw... I know... I'm such a failure... *sob*"

            "Willow whines and wallows in self-pity the whole way, until you drop her off at her house near the sewers. She promptly falls into a deep slumber."

            you "Tough luck, kiddo..."

            $ NPC_willow.love -= 3

    $ NPC_willow.flags["seen fight"] = True

    return

label willow_recovery():

    "..."

    "<Fever. Dream.>"

    if not NPC_willow.flags["first recovery"]:
        $ NPC_willow.flags["first recovery"] = True

        "<Blood like... molten lava... in your veins... Pulse throbbing.>"

        "<A city full of... ripe, young females...>"

        "<You must... mate...>"

        "<Blood flows to your... appendage...>"

        "Wait, did you say appendage? You meant your dick, of course..."

        "<Flashes of... naked women bodies. Screams of... fear. Sighs of... pleasure.>"

        play sound s_roar

        you "(Don't be... afraid... I will make you... feel good...)"

        you "Don't be afraid..."

        play sound s_laugh

        "Woman voice" "Man, you're really out of it..."

        you "That voice..."

        "Woman voice" "Hey, [MC.name]! Wake up!"

        "Your name stirs up memories. You are not a tentacle monster... You are a human being."

        you "I am not an animal! I am a human being!"

        willow "Damn, wake up already."

        "Someone shakes you. You feel a weight on your body."

        you "Gah... Ugh... Where am I?"

        show bg willow on_top at top with circleout

        willow "Finally! I thought you were a goner... Sill would have gone berserk on me!"

        you "..."

        you "W... Willow?"

        willow "Yeah, you dummy. You can thank me, I recovered your sorry ass from a pool of monster slime..."

        you "What the..."

        you "WHERE AM I? WHAT HAPPENED?" with vpunch

        you "More importantly, WHY ARE YOU WEARING NOTHING BUT MY SHIRT?!?" with vpunch

        willow "Hey, cool it off... Like I said, I recovered your sorry ass from a pool of monster slime. The pacifying effect makes the monster, err... discharge..."

        "You try not to think too hard about the implications."

        willow "It was a messy business. So I brought you back to the brothel, and I asked your slave Sill to clean our clothes. I don't want to risk the side effects rubbing off..."

        you "Side effects?"

        play sound s_laugh

        willow "Don't worry, they aren't so bad... Fever, and superhuman arousal, mostly. Some random skin color changes. Nothing to worry about."

        "For the first time, you notice that you are sporting a rock-solid hard-on. The bulge in your pants is unmistakable."

        "It doesn't seem to bother Willow, who is bouncing up and down cheerfully. It occurs to you that she is really wearing {i}nothing{/i} under your shirt."

        play sound s_scream
        sill sad "MASTEEEER!!!"

        scene black
        show expression brothel.master_bedroom.get_pic(x=config.screen_width, y=config.screen_height) at top
        with dissolve

        show sill sad at right with dissolve

        sill "You are all right! Oh, praise the gods!!!"

        "Sill rushes to your side, shoving Willow out of the way."

        play sound s_surprise

        willow "Hey! Watch it!"

        sill "I was so worried!"

        you "Ugh... Yeah... I'm fine..."

        sill happy "Oh, it is such a relief..."

        play sound s_knocks

        sill "Uh?"

        show gina at left with dissolve

        gina "Ahem... Excuse me?"

        gina "I was informed I could find Mister [MC.name] in this, err, establishment..."

        willow "Gina? Hey, what's up!"

        gina "Oh. So you're here too. And, uh... Naked?!?"

        willow "I'm not naked! Look, I found a nice shirt!"

        you "It's MY shirt!" with vpunch

        gina "Am I... interrupting something?"

        you "Actually..."

        sill "Not at all!"

        sill "Sit down and make yourself at home. I'll make some tea."

        scene black with fade

        "..."

        show bg willow tea at top with fade

        gina "So that's your adventure... I'm glad you found that monster a new home."

        "Willow beams with joy."

        you "(I wish you had snuffed the fucker out...)"

        gina "Speaking of which..."

        gina "Have you got the 'special delivery' I requested?"

        you "Uh?"

        willow "Ah, I see... So that's why you came all the way out here. I thought you were just looking for entertainment."

        play sound s_scream

        gina "Uh, what??? No!!! *blush*"

        gina "I'm a scientist! I have no time to partake in vulgar mating rituals!!!"

        gina "I came here to enlist your help. Both of you, actually."

        willow "What for?"

        gina "Well, the first step is my 'special delivery'. Is it ready?"

        willow "Yes. I put it in a safehouse in the warehouse district, near the Prison."

        gina "Great. That's where [MC.name] comes in."

        you "I... I do?"

        gina "I need your help. For science."

        you "Right! Sounds cool."

        gina "I would like to use you as a live test subject."

        you "Wrong! Not cool. Count me out."

        gina "You're in, then? Fantastic!"

        you "I just said..."

        gina "Meet me at the Prison when you're ready. I'll have you sign a number of waivers... You're not afraid of heights?"

        you "No way! Read my lips! I'm N-O-T C-O-M-I-N-G." with vpunch

        gina "That's great, then. I'll see you there."

        "Smiling, Gina waves at you, pats Willow's head, and takes her leave."

        willow "Look, I ain't going to tell you how to live your life, but... I'd avoid the {b}Prison{/b}, if I were you."

        you "You don't have to tell me!" with vpunch

        you "*sigh* Those girls..."

        $ story_add_event("gina research")

        scene black with fade

        show expression brothel.master_bedroom.get_pic(x=config.screen_width, y=config.screen_height) at top
        with dissolve

        "..."

        show willow with dissolve

        willow "Hey, [MC.name]!"

        you "Duh?"

        "You were napping. The bulge in your pants has barely receded, and now you have a massive case of the blue balls. Some girl will taste your fury tonight."

        willow "Sill cleaned my clothes. They've never been so fresh! That girl's a miracle."

        willow "Here your shirt."

        play sound s_dodge

        you "Thanks..."

        you "Hey! It's completely wet!" with vpunch

        willow "Oh, yeah... I used the onsen to clean up. I couldn't find a towel, and I couldn't very well go naked with all those lecherous old men..."

        you "What?"

        willow "Although it did get transparent quickly... It is a white shirt, after all. I had to turn one of the perverts to stone when he tried to grab my butt. Then the rest left me alone."

        you "You turned a customer to {i}stone{/i}?!?" with vpunch

        willow "Yeah, well, relax. It's only temporary."

        you "Oh. That's a relief..."

        willow "Give it twelve to fifteen months and he'll be back to normal, as if nothing had happened."

        willow "In the meantime, I put him in the garden. People will think it's a statue. The pigeons sure seem fooled already..."

        you "You brat... Grrr..."

        willow "Come on, don't get angry. Did I ever tell you the story of how I turn people to stone?"

        you "..."

        willow "Anyway, this onsen of yours is a real wonder. I feel like a million denars."

        willow "Do you mind if I recommend it to my family?"

        you "..."

        you "Do you have, per chance, some hot sisters with a nicer temperament?"

        willow "What do you mean, nicer temperament? Never mind, I'll let that slide."

        willow "I was thinking of my great-grand-auntie. She is feeling her age, and has trouble with her joints, you know..."

        you "Ugh..."

        play sound s_surprise

        willow "Puh-leaaaase!!!" with vpunch

        with hpunch

        "Willow grabs you and shakes you."

        with hpunch

        you "Stop iiiit!!!"

        play sound s_evil_laugh

        with hpunch
        with hpunch

        you "All right, all right! They can come! But they'll have to pay!"

        willow "Great! Thank you!"

        willow "But don't let any of those pervs lay their hands on my old relatives... Some of them are sick people that fantasize on grannies, I'm sure! I'd hold you responsible."

        you "*gulp*"

        # The relative will come after 1-2 weeks
        $ calendar.set_alarm(calendar.time + 6 + dice(8), event_dict["willow relative"])

        scene black with fade

    elif NPC_willow.love >= 5:
        "<Complete darkness. Burning lust.>"

        "<Fire in your crotch.>"

        "<Getting bigger and bigger. Must... Find... Release...>"

        play sound s_laugh

        "Woman voice" "My, look at you..."

        "<A huge... tower. Looming over the horizon.>"

        "<A large, red-haired... beast... is clinging to the tower. Looming.>"

        "Woman voice" "I guess it cannot be helped..."

        "<It starts licking the tower.>"

        play sound s_sucking

        you "(Wait... Licking?)"

        show bg willow bj1 at top with circleout

        you "..."

        you "W-Willow?"

        willow "Ah, so you're awake... *lick*"

        "Willow is sitting on your bed. She is stroking and licking your massively oversized cock."

        you "Wh-What... What are you doing?!?"

        willow "What doesh it looksh like I'm doing? *slurp*"

        "Willow is enthusiastically sucking on your cock, placing your oversized tip in her drooling mouth, stretching her jaw to its limit."

        willow "It doeshn't fit... Nggh..."

        show bg willow bj2 with dissolve

        willow "It'sh my fault you ended up like thish... I'm only helping you release the stressh... *slurp*"

        you "What... What's going on with me..."

        willow "The monster juice was too strong... If we don't do anything, your genitals might burst."

        you "This... This is horrible!" with vpunch

        willow "Yesh... *slurp* That's why you need my help... *lick*"

        you "Oh... I feel like I'm going to burst..."

        willow "Don't fight it, just let go... *slurp*"

        you "Oh..."

        play sound s_mmh

        willow "Ngh... Hmmm..."

        with flash

        you "AAH!!!"

        show bg willow bj3 at top with doubleflash

        "*SPURT* *SPURT*"

        willow "Uwah!"

        "Erupting like a volcano, your cock shoots unnatural amounts of cum all over the bedroom and a surprised Willow."

        with doubleflash

        "*SPURT* *SPURT*"

        willow "Incredible... It doesn't stop!"

        with flash

        show bg willow bj4 at top with doubleflash

        "Your orgasm lasts for long moments, your cock totally out of control."

        "When it is finally over, Willow looks at you and gently scolds you."

        willow "Look at the mess you've made... My face is covered with a gallon of cum... And it's going to take hours to clean up this bed..."

        willow "Well, I'm sure Sill will be all up to it. Siiiill!"

        you "She's going to be mad..."

        willow "In the meantime, I know what you and I can do..."

        scene black with fade
        show bg willow fuck at top with dissolve

        "Willow drags you to the private bath, where she proceeds to clean up."

        willow "Gee, you can't do anything for yourself in this situation... I guess I'll have to rub it for you... [emo_heart]"

        "You spend hours in the bath playing with her. She has impressive stamina... and technique, for a girl her size."

        willow "I told you it won't fit... Aw..."

        willow "B-But... I guess we can give it another try..."

        play sound s_mmmh

        $ unlock_achievement("h willow")
        scene black with fade

        $ MC.change_prestige(4)

        "When you emerge from the bath, completely drained, your dick is slowly going back to normal."

        "As you exit the bath, Sill is giving you murderous looks. Doing your best to avoid her, you head straight to your bedroom and fall asleep like a stone."

        $ story_remove_event("willow fight")


    else:
        "<Villages set on fire. People running in terror.>"

        "<Women.>"

        "<Juicy women...>"

        "<You can smell them...>"

        you "*sniff* *sniffff*"

        play sound s_laugh

        willow "Hey!!! Stop it!"

        you "*sniff* Girl smell..."

        willow "I'm ticklish! Stop it!"

        show bg willow on_top at top with circleout

        "You open your eyes, and see Willow."

        you "My shirt... Not again..."

        "You have a raging hard-on... And you are paralyzed. You look at Willow's teenage body with burning lust."

        you "I... I can't move..."

        willow "Ah, yeah, I guess that's a side effect... Hehehe..."

        you "You... Just you wait..."

        willow "Aw, you're just as bad-tempered as usual. Be grateful I saved your ass!"

        you "Grr..."

        willow "Sill should be finished shortly with my clothes, and I'll be on my way."

        you "..."

        you "Well, you know, have a ball, it's not like it's my house or anything."

        willow "Well then, see yaaaa!"

        willow "And don't worry. The paralysis will wear out in an hour or so."

        you "That damn monster..."

        willow "Uh? Monster?"

        willow "Oh yeah! Hahaha... The, err, {i}monster{/i} cast a paralyzing spell on you, so you would stop rubbing up and down on her in your sleep! Hehehe... That's totally what happened."

        you "..."

        willow "Well, gotta go! See ya! [emo_heart]"

        scene black with fade


    $ MC.interactions = 0

    "You have lost all your remaining actions for today."

    return


label willow_relative():

    scene black
    show expression bg_bro at top
    with fade

    show sill with dissolve

    sill happy "Masteeeer!!!"

    you "Sill? What is it?"

    sill "I wanted to tell you, but..."

    you "Spit it out."

    sill "There is a visitor from outside town. A relative of Willow the crazy monster catcher, apparently."

    you "Damn! It must be her creepy old great-great-auntie or something. The old coot will scare the customers away..."

    sill "Well... She said she wanted to use the scented onsen, so..."

    you "Oh, really? I hope she paid top denar to use that onsen. I don't operate a damn charity hospice..."

    sill "Actually, she didn't pay... I thought..."

    you "SHE DIDN'T PAY???" with vpunch

    sill sad "No, but..."

    you "Hot damn!!!" with vpunch

    you "This is going too far! I going to shake the money off this old sack of bones!"

    sill "Master, wait..."

    scene black with fade
    show bg onsen at top with dissolve

    "Charging inside the onsen past groups of baffled customers, you head straight for the outside bathing area."

    play sound s_splash

    you "WHERE IS WILLOW'S RELATIVE! SHOW YOURSELF!"

    play sound s_surprise

    "Voice" "Yes?"

    you "YOU!!! WHAT DO YOU THINK YOU..." with vpunch


    show bg willow relative1 at top with dissolve

    relative "Yes? [emo_heart]"

    you "..."

    relative "Is something wrong? Mister?"

    relative "Hello?"

    play sound s_horn

    "A beautiful young lady is standing in the bath, a wet towel barely concealing her shapes."

    you "Heeeeeelloooo there!!!" with vpunch

    relative "You wanted something to do with me?"

    you "I... I just wanted to say, we are delighted to have such a distinguished guest in our elite establishment..."

    you "I mean... You can stay here as long as you like, of course! It's on the house! Haha, hahaha..."

    relative "Oh, my, this is awfully nice of you..."

    relative "My little Willow told me you had no class, but I can see she was just joking..."

    you "(Grrr... The little brat...) *mad*"

    you "Hahaha, of course, she was, er, joking... But she never told me she had a sister with such... I mean, such... Uh..."

    relative "Teehee, you flatterer... I'm not Willow's sister... I'm her great-great auntie."

    you "Ah yeah, you're... "

    extend "YOU'RE WHAT?!?" with vpunch

    relative "Her great-great-auntie... Her great-granma is my big sister..."

    you "But... How... You're just so... Young?"

    relative "Haha, I guess you're unfamiliar with our kind... We age a lot slower than humans."

    relative "I'm actually 150 years old... A mature woman by our standards."

    relative "But bathing in this sweet onsen, I feel like a spry young woman! It's like I'm 75 all over again!"

    you "But, Willow... She looks human... You look human... I mean..."

    "The woman's ears twitch as she smiles. For the first time, you think that they might not be accessories after all."

    relative "Well, I take it you've never met our people. Unsurprising, we are mostly keeping to ourselves these days..."

    relative "We call ourselves the {i}Kemono{/i} people."

    you "The Kemono?"

    relative "We are one with the fairy people, although our particular tribe dwells far away from the Holy lands, thankfully."

    relative "Humans fear us, especially these days with the war, so we try to remain inconspicuous."

    relative "Except Willow, of course, she's always been brazen... But what do you expect from a kid who just turned 50?"

    you "Well... She certainly doesn't look her age..."

    relative "Anyway, I am very thankful that you are friends with her and that your establishment doesn't discriminate."

    you "So... You're one of the animal people?"

    "She looks pained."

    relative "Aw, please, don't call us that... We are the Kemono. We are not animals."

    you "I'm sorry. I just heard folks refering to your people that way..."

    relative "Yes... Those people are wrong. They spread rumors that we descend from sinning human females, mating with animals."

    you "What are your origins, then?"

    relative "When Xeros was young, the first sentient tribes worshipped nature, and natural forms. The gods that we know today didn't exist, but there were spirits. Magical entities, born of nature and the primal chaos."

    relative "It is said that each tribe had a totem guardian, and as a mark of devotion, the first tribes took some of their attributes from the spirits."

    relative "This is how the fairy people now referred to as the Kemono were created."

    you "So... They didn't actually mate with animals?"

    relative "Well, they might have, but that's beside the point. I'm talking about spirituality here."

    you "Right. Are there many tribes like yours?"

    relative "No one knows exactly... There are many surviving tribes, but even more were lost over the ages. We still have bird people, dog people, elephant people, pony people, nine-tail fox people..."

    relative "And cat people, of course. They're everywhere... Probably because they make such good thieves... and lovers."

    relative "Also, people like to share their memes - whatever that is."

    relative "But the panda-people have long disappeared... As well as the sloth-people, the dinosaur-people, the dodo-people..."

    you "Sad."

    relative "Yes. So many lost cultures, with a rich, unique take on life... And their very own smells..."

    you "..."

    relative "Although I'm personally glad the roach-people are not around anymore."

    you "Fascinating..."

    relative "But my, look at the time... I have to be on my way."

    relative "I really enjoyed your hospitality. I look forward to coming back to see you, and enjoy this wonderful onsen next month."

    you "Why, of course! You will always be welcome!"

    relative "Thank you. [emo_heart]"

    scene black with fade

    "Watching her juicy curves as she steps out of the bath and heads towards the shower, rocking her hips, you are not even upset that you just agreed to give her free onsen for life."

    you "This will pay for itself... With a body like this, she'll be dragging in a bunch of customers."

    # Willow's relative will come back in one month
    $ calendar.set_alarm(calendar.time + 28, Event("willow_relative_returns"))

return


label willow_relative_returns():

    scene black with fade
    show bg onsen at top with dissolve

    "Willow's great-great-auntie came back to soak in the onsen tonight."

    show bg willow relative1 at top with dissolve

    "Sill made sure to give her a private pool to keep the lusty customers at bay."

    menu:
        you "Should I go talk to her?"

        "和她打招呼":

            if not NPC_willow.flags["chat relative"]:

                $ NPC_willow.flags["chat relative"] = True

                you "Helloooo my lady..."

                relative "Oh, Master [MC.name]! Nice to see you."

                you "Are you comfortable? Is there anything you need?"

                relative "Well... I guess I could use company. Why don't you get a fresh towel and hop in?"

                "Taking a hot bath with an even hotter guest... This is a no-brainer."

                with fade

                "Grabbing a towel, a wooden platter and a bottle of sake, you join Willow's relative inside the hot springs."

                you "It's pretty hot in here... I brought us some refreshments. Can I interest you in a cup of sake?"

                "She eyes you with a little suspicion, but she politely accepts."

                relative "Sure, I need to unwind... This place is a long way from the countryside; I've been walking all day."

                you "So, last time, you were telling me about the customs of your people. I would like to know more."

                relative "Why, sure, I'm always glad to help strangers understand us better."

                relative "Our tribes lived in the forests and other natural sites of Xeros long before humans came around."

                relative "We lived side by side with elves, nature spirits, even dwarves, although I'm not sure which race came first. Our stories don't mention it."

                relative "Most of them have disappeared now..."

                relative "Still, we get along well enough with humans. We never had as much trouble fitting in their civilizations and cities as the other fairy people do."

                you "Yet I don't see a lot of you around..."

                relative "Oh, you'd be surprised. Some of us hide our 'animal' features pretty well..."

                relative "And some just hide in plain sight, like my great-great-niece, Willow."

                you "Yeah..."

                relative "It was a lot easier before that stupid war started. The so-called 'Holy war' spread distrust and ill-will between our people."

                if MC.god == "太阳神":
                    you "Well, surely you cannot blame Arios the all-mighty for these troubles? A righteous light must be shone on the Pagans..."

                    "She shakes a head disapprovingly."

                    relative "Oh, please, spare me the sermon. The fairy people were living in peace before your kind brought the war to our doorstep."

                    you "But... This is Arios's will..."

                    "The debate quickly runs out of steam. Willow's relative politely excuses herself and escapes the awkward conversation."

                    you "Such a hot woman... Pity she doesn't understand the one True religion..."

                    return

                elif MC.god == "莎莉娅":

                    you "Yeah, I get you. Arios and his followers are a nuisance. I prefer the Goddess of the night..."

                    relative "Oh, the one you call Shalia?"

                    relative "No offense, but the night isn't a Goddess. It is a part of nature, and thus is composed of many spirits..."

                    you "But... Shalia is the night incarnate... Surely she is no mere spirit..."

                    play sound s_sigh

                    relative "*sigh* Humans... Your people always need a simple explanation for everything..."

                    "You agree to disagree, and quickly change the topic."

                    $ mod = -2

                else:

                    you "Yeah. I cannot stand all of this religious mumbo-jumbo."

                    relative "Right? Humans just love these make-believe stories..."

                    you "Yeah, but I think it's a waste of time. I think respecting nature, like you do, is a much better way to live."

                    play sound s_ahaa

                    relative "Oh, I'm so glad you said that! [emo_heart]"

                    "The conversation goes on cheerfully."

                    $ mod = 2

            else:
                relative "Oh, hello, [MC.name]!"

                "The woman invites you to join her, and you bring alcohol to the party."

                you "Long time no see..."


            with fade

            "You keep talking for a long while, pleasantly relaxing in the bath."

            you "Do you want more sake?"

            relative "*tipsy* I... I really shouldn't... It's already pretty late..."

            you "Come on, don't leave me here drinking by myself..."

            # Run challenge
            call challenge("charm", 5, bonus=mod) from _call_challenge_49 # result is stored in the _return variable
            $ r = _return

            if r:
                "You give her a charming smile, and she yields to your request."

                relative "All right, but just one more..."

                with fade

                "An hour later, you are still drinking and talking."

                "You are beginning to feel quite drunk, and are unsure how you ended up right next to her in the bath."

                "As you peek down at her ample bossom, you see her towel is getting loose and catch a glimpse of her nipples."

                relative "[MC.name]? Are you listening to me?"

                "Ashamed, you start to look away, but instead of being angry, you notice the woman is blushing, staring at your crotch."

                "*bulge*"

                "It's pretty obvious your cock is bulging beneath your towel."

                play sound s_sigh

                "The woman licks her lips, pouring herself another drink."

                relative "It's awfully hot in here, isn't it? *blush*"

                play sound s_dress

                pause 0.3

                show bg willow relative2 at top with dissolve

                relative "Oopsy..."

                "Carelessly shedding her towel, Willow's relative drinks another cup of sake clumsily. Some of the alcohol trickles down on her hot body."

                you "*gulp*"

                "Standing up, you let your towel slip away in the hot water..."

                play sound s_mmmh

                relative "Mmmh..."

                "She takes an appreciative look at your manhood."

                relative "There is one more thing you should know about the Kemono..."

                you "And that is?"

                relative "Just like the rest of the fairy people... We have a very strong sex drive!"

                "*PULL*"

                play sound s_splash
                scene black with fade

                show bg willow relative3 at top with fade

                play sound s_aaah

                relative "Ah yes, aaaah!!!"

                play sound s_moans

                "Just like wild animals, you start fucking right here in the onsen, oblivious to the people that might be peeking."

                you "(Wow... This pussy is 150 years old! But she's tighter than a 20-year old human...)"

                "The pleasant feeling of the hot water and the cool air breeze while you fuck with abandon is enough to bring both of you to the edge."

                relative "Oh, yes! Fuck me... Fuck me!"

                you "I'm... Close..."

                relative "Oh, yes! Give it to me! Aaaah!!!"

                with flash

                play sound2 s_orgasm

                "The stimulation is too much, and you cum right inside her. She seems to relish the feeling of your hot cum filling her up."

                show bg willow relative4 at top with doubleflash

                relative "So good... Aaaah!"

                play sound s_splash

                "You made a mess of the bath area, and caused quite a bit of commotion."

                "The Kemono woman seems unfazed by it, and you're drunk, so you just shrug it off."

                "After a while spent making out and fondling each other in the hot water, she finally breaks out of her spell."

                relative "I really have to go... Thank you... for everything. *wink*"

                relative "I'll be seeing you next month..."

                "Blowing you a kiss, she slips out of the bath, naked, and heads back to the changing room."

                scene black with fade

                $ MC.interactions = 0
                $ MC.change_prestige(3)
                $ unlock_achievement("h relative")

                "You spend a good amount of time staring up at the stars before heading to bed."

            else:
                relative "Sorry, I really have to go. But thank you, I had a nice time..."

                you "I see. Goodbye, then..."

                relative "Goodbye..."


        "没空搭讪":

            you "Nah, I'm too busy."

    # Willow's relative will come back in one month (unless the MC is an Arios-worshipper: She doesn't like that.)
    $ calendar.set_alarm(calendar.time + 28, Event("willow_relative_returns"))

    return





label farm_gizel_introduction():

    stop music fadeout 3.0

    scene bg farmland with fade

    play sound s_rooster

    "You came back today to see how Gizel is doing with her new place."

    scene black
    show bg farm at top
    with fade

    you "Wh... What???"

    "Just yesterday, the farm was nothing but a rubble in the middle of a barren swamp."

    "Today, however, it has been mostly rebuilt and refurbished."

    play sound s_moo

    you "I guess this place's magic is as powerful as Gizel says it is..."

    "As you reach the farmhouse, you pause for a moment."

    you "What was that?"

    "You hear some muffled sounds coming from inside. Judging by the sounds, it's like there are some animals in there."

    you "Maybe Gizel is a pet-lover?"


    scene black with fade

    play sound s_moans_quiet

    gizel soft "Come on boy, don't be shy... Come to mamma..."

    play sound2 s_door

    scene bg gizel_big1_1 with dissolve

    you "What... What's going on in here???"

    "A hulk of a man, nearly seven feet tall, is standing next to Gizel, who is crawling on the floor."

    "The girl elf looks tiny and powerless next to the giant behind her."

    gizel shy "Do... Do it..."

    "The giant gives you a placid look, not seeming bothered or even intrigued by your presence."

    "You notice the man's pants are lowered to his knees."

    "You notice something else. What you mistook at first for a pink anaconda is in fact the man's huge dick."

    you "Holy shit! It must be at least a foot long."

    gizel "What are you waiting for... Do it already!"

    scene bg gizel_big1_2 with dissolve

    gizel angry "Damn this stupid horse... Don't you understand orders?"

    gizel "BOB!" with vpunch

    "As if snapping from a daydream, the giant looks down at Gizel with a puzzled look."

    "Man" "*grunt*" with vpunch

    "The man drools as he looks upon Gizel's petite butt."

    "He starts grinding his giant dick against her tiny ass."

    "After a few moments, his dick grows even larger, leaking what seems to you like a gallon of pre-cum on her bare butt."

    gizel blush "That's right, that's my boy..."

    play sound s_roar
    "Suddenly, the man starts growling like a wild beast. Pushing Gizel's head down, he places the tip of his huge dick at the entrance of her tiny pussy."

    you "Hey, wait! I don't think..."

    play sound2 s_scream_loud

    scene bg gizel_big1_3 with dissolve

    "Ignoring your interruption, the giant shoves his huge cock inside Gizel with inhuman strength. You think her insides will be destroyed by the man's violent thrust." with hpunch

    play sound s_screams

    gizel angry "RAAAAAAH!!!" with hpunch

    "Gizel's eyes roll backwards as the huge man pumps his cock in and out of her, sending her frail body rocking like a skiff in a killer storm." with hpunch

    you "Hey, punk! What do you think you're doing to my friend!"

    play sound s_surprise

    gizel surprise "AAAH! [MC.name], aaaah, it's you, AAAHAAA!!!" with hpunch


    you "Gizel! What the hell is going on?"

    play sound s_aaah

    gizel "Oh, nothing, aaah... Please wait a minute, I won't be long... AHAAAA!!!" with hpunch

    play sound s_scream_loud

    scene bg gizel_big1_4 with dissolve

    "The giant increases his pace, lifting Gizel's butt high into the air with each thrust." with hpunch

    "It seems impossible that his huge manhood can fit inside the fragile pussy of the little she-elf, but somehow it does."

    you "Err, Gizel... Is this man bothering you?"

    play sound s_moans_short

    gizel shy "M-Man? Ahhaa..." with hpunch

    gizel "Bob... is... no man... Raaaah..."

    you "What?"

    play sound s_roar

    pause 0.2

    play sound2 s_scream_loud

    gizel blush "Oh, I can feel it, I can feel it... Almost there..."

    play sound s_moans

    gizel angry "Fuck me you beast! FUCK ME HARDER! OH, YESSS!!!"

    play sound2 s_roar

    scene bg gizel_big1_5 with doubleflash

    gizel blush "AAAAAAAAH!!!"

    play sound s_orgasm_young

    with flash

    "Gizel is shaken like a ragdoll as she is rocked by a shattering orgasm." with vpunch

    with flash

    "The giant shoots bucket after bucket of cum inside Gizel's wide open pussy, splashing semen all over her lower body."

    play sound s_aaah

    gizel "So good! So good..."

    "You are starting to feel a bit left out."

    "You clear your throat."

    you "Ahem..."

    gizel surprise "Uh?"

    gizel shy "Oh, [MC.name]... You're still here."

    gizel normal "Wait for me outside. I won't be long."

    gizel shy "..."

    gizel upset "Bob! Get off of me, you muppet! Go back to the barn."

    play music m_gizel fadein 3.0

    scene black
    show bg farm at top
    with fade

    show gizel blush with dissolve

    gizel "Ah..."

    gizel "I feel so refreshed!"

    gizel normal "Anyway..."

    gizel upset "Do you have a good reason for interrupting my breakfast?"

    you "Well, uh... You told me to come back here, so I did. But you know, I'm actually busy, so..."

    gizel "Stay here!" with vpunch

    gizel normal "Actually, I have a business proposal for you."

    you "Business?"

    gizel "That's right. You own a brothel, don't you?"

    you "Well... I sure do, but..."

    gizel upset "Listen."

    gizel smirk "I have a long experience dealing with all sorts of exotic creatures. And I've been especially interested in human females lately."

    you "You have?"

    gizel normal "That's right."

    gizel "On the surface, human females seem completely useless, much more fragile than beast people, much less sensitive than elves..."

    gizel smirk "But after extensive research, I have become convinced that there is more to human females than meets the dick.
                 In fact, I believe their sexual compatibility is highest among all the races..."

    gizel normal "They would just need proper training."

    you "Training?"

    gizel "That's right. In particular, I think they should be exposed to various creatures, both natural and supernatural. This would go a long way towards
           unlocking their potential."

    you "And you're telling me all this, because...?"

    gizel "Well..."

    gizel blush "[MC.name], I have a favor to ask. [emo_heart]"

    you "Uh..."

    gizel surprise "LET ME RUN SOME EXPERIMENTS ON YOUR GIRLS, RIGHT HERE AT THE FARM!!!" with vpunch

    you "What? Why would I do that!" with vpunch

    gizel upset "Come on!"

    gizel normal "Listen to me. First of all, I promise I will not damage your merchandise, ok? Or I won't damage their looks, anyway..."

    gizel blush "But more importantly, my training can make your slaves a lot more obedient..."

    gizel "And I can teach them so many tricks... Eons of experience. With my training, they'll be ready to fulfill your customers' darkest fantasies..."

    you "Hmm..."

    you "Wait a minute."

    you "You said something about 'natural and supernatural' creatures? What was that all about?"

    gizel normal "Well... You remember Bob, right?"

    you "Mr Anaconda?"

    gizel smirk "Himself. Bob is a stallion, I brought it with me when I came to Zan."

    you "A... Stallion?"

    play sound s_sigh

    gizel upset "You really need to be told everything, don't you?"

    gizel normal "Stallions are a peculiar kind of slaves, bred in the Blood Islands."

    you "B... Bred?"

    gizel smirk "That's right. The mages there are truly evil... I love it. They raise stallions as sex slaves from birth, breeding them selectively for their
                 unnaturally large cocks."

    gizel "Using spells and coercion, they help them grow into hulking sex beasts by the time they reach adulthood... Ready to serve their masters blindly."

    you "So Bob is a stallion. He doesn't... talk much, does he?"

    play sound s_evil_laugh

    gizel "Of course not! Stallions are magically lobotomized... They are incapable of independent thought."

    gizel "They serve their master or mistress blindly and faithfully for the whole of their pathetic, short life."

    you "That sounds cruel... *shiver*"

    gizel blush "Well, doesn't sound that bad to me. They are free from the angst and shame of ordinary slaves, forever ready and willing to fulfill their one and only purpose: fucking."

    gizel normal "Beautiful, mindless, mean fucking machines..."

    gizel smirk "You wish you were useful as a stallion!"

    you "*grumble*"

    gizel blush "Anyway. Bob is just the first of my mindless minions. Actually, he's the second, you're the first. I wouldn't want you to feel insulted."

    you "Hey!"

    gizel normal "Anyway. Thrall, your next task will be to help me renovate the farm, and gather some fellow minions to train your girls."

    gizel "If we renovate the facilities here, we could host a variety of creatures..."

    gizel blush "Think about it. You help me with the repairs, I get to run my experiments, and I can feed off everyone's sexual energy."

    gizel "As for you, you can get your girls trained for free. And I can hold them here at your convenience when your brothel is full."

    you "Hmm..."

    gizel angry "Also, I won't change you into a giant toad."

    gizel "Maybe."

    you "..."

    gizel normal "So, what do you think?"

    you "Fine, we have a deal. But if I set some conditions for the girls' training, you will respect them, right?"

    gizel angry "Grrr..."

    gizel upset "Fine. But you get to pay for all the repairs."

    you "Whaaat? I..." with vpunch

    gizel blush "Perfect. We have a deal, then, see ya! [emo_heart]"

    hide gizel with dissolve

    you "What mess did I just get myself into..."

    stop music fadeout 3.0

    scene black with fade

    $ farm.activate()
    $ story_add_event("farm_activate_goldie")
    $ story_add_event("farm_meet_stella")
    $ story_add_event("farm_meet_willow")
    $ story_add_event("farm_meet_gina")

    "You can now send girls to the {b}Farm{/b} to access some special training options."

    $ unlock_achievement("farm")

    return


label farm_first_visit():

    gizel normal "Ah, [MC.name], you've come to visit! How nice of you."

    gizel "I guess I should explain to you how things work around here, right?"

    menu:
        gizel "I guess I should explain to you how things work around here, right?"

        "请告诉我":
            pass

        "没有必要":
            gizel "All right then. Call me if you need me."
            "Click on Gizel's portrait if you need help with the farm."
            return

    gizel "You can send some girls to the farm for holding or training, in the same way you assign them a job."

    gizel "They will be held in the {b}pens{/b} out back. You can rebuild more pens if you have the money."

    gizel "While at the farm, I can do one of two things with your girls: {b}holding{/b} or {b}training{/b}."

    gizel "In {b}holding{/b} mode, I will simply keep them around the farm until you need them back. They will either work on the farm or rest, you choose."

    gizel "When working, girls may improve some of their basic skills."

    gizel "In {b}training{/b} mode, I will use my considerable skills to train them for their one and only purpose: {b}sex{/b}."

    gizel smirk "I can train them for all sorts of sex acts, which will reduce their reluctance in the long run."

    gizel upset "However, some girls might rebel against training, especially disobedient or untrained ones."

    gizel angry "If that happens, I will punish the bitches. Harshly. Unless you tell me to go soft on them..."

    gizel upset "But where's the fun in that?"

    gizel normal "Finally, I should talk to you about {b}minions{/b} and {b}facilities{/b}."

    gizel blush "{b}Minions{/b} are my babies, like sweet sweet Bob over there..."

    gizel normal "I need minions to properly train your girls for sex."

    gizel smirk "After all, I am not 'equipped' for some of the most 'involved' training... Although I know a spell or two."

    gizel "Right now, the only available minion is Bob. I'm told you can buy more varied minions in the city, but I'm not sure where."

    gizel normal "Which type of minion to use for training is down to personal preference, but some girls are especially sensitive to specific minions."

    gizel smirk "Once we find out which minion a girl is vulnerable to, I will be sure to use this information for training... *evil grin*"

    gizel "Before we do, though, we must improve the farm {b}facilities{/b}."

    gizel "Facilities are where my minions dwell. Build or improve facilities to improve the number and variety of minions the farm can hold."

    gizel "Finally, I should note that there is a limit to how much we can grow the farm without attracting too much attention. Things will get better once
           you obtain a higher brothel license, which will give you more influence."

    "Click on Gizel's portrait if you need more help with the farm."

    return


label farm_first_beast():

    stop music fadeout 3.0

    scene black with fade

    "You decide to pay a visit to Gizel, to check on her new pensioner."

    if is_censored("beast"):
        menu:
            "Skip event? (bestiality)"

            "是":
                return
            "否":
                pass

    play sound s_rooster

    show bg farm at top with dissolve

    you "Hello?"

    play music m_gizel

    show gizel with dissolve

    gizel normal "Oh, [MC.name]!"

    gizel "Come in, come in! This is so fun!"

    "You haven't seen Gizel this excited in a long time. She leads you into the barn."

    scene bg farm_stables with fade

    show gizel with dissolve

    gizel "Sit down!"

    "She points to a wooden table and some stools, and you both sit down."

    "You notice a sorry-looking burnt pie and a bottle of cheap cider on the table. She shoves a slice of the strange pie and a glass of cheap cider in front of you."

    "You take a suspicious look at the food. This cake gives new meanning to the word 'crumble'."

    you "Did you bake this? It looks... Strange."

    gizel upset "Hey! Don't be rude!" with vpunch

    gizel "I've been too busy in the past few centuries to learn cooking, ok?"

    you "Er... I'm not so hungry, you know... But thanks."

    you "Are we... celebrating something?"

    gizel normal "Of course!"

    "She gestures towards the pig stall, from where muffled grunts can be heard."

    if debug_mode and not farm.get_minions("beast"):
        $ farm.add_minion(Minion("beast"))

    $ name = farm.get_minions("beast")[0].name

    gizel "We just welcomed [name] at the farm, our first {i}real{/i} animal, and I'm so excited to have it!"

    you "I see... What do you plan to do with it anyway?"

    gizel blush "Animals are FUN! They have such a strange anatomy, you know..."

    you "I see where this is going..."

    gizel normal "And they don't mind getting down and dirty. They just do whatever they want, you know, they just don't give a fuck..."

    you "Kind of reminds me of somebody..."

    gizel "Of course, I have to use a few spells on them to make things more interesting..."

    gizel "But after a few adjusments, they'll be just as happy mounting your stupid slave girls as they would be a female of their own species."

    gizel "I can even transform them from one species to another according to my whims, did you know that? Just using a few common ingredients..."

    you "Fascinating. But don't overdo it. My slaves are not capable of mating with an elephant..."

    gizel "No they aren't... Yet."

    gizel smirk "But believe me, after a few nightly sessions here, they'll learn to {b}{i}truly{/i}{/b} love animals..."

    you "If you... *burp* ... say so..."

    you "Say, this cider... *burp* ...tastes really strange..." with vpunch

    gizel blush "My, you look awfully pale... Greenish, even..."

    play sound s_knocks

    you "Did... You... *burp*"

    gizel normal "Well, if you'll excuse me. Someone's here. Right on time, if I may say so."

    gizel soft "Come in, dear friend!"

    show gizel soft at right with move
    show milkmaid at left with dissolve

    milkmaid "Hello, mistress Gizel!"

    milkmaid "I've brought you the cart of milk you asked me, and..."

    play sound s_surprise

    "She seems to notice you for the first time."

    milkmaid "W... What's this?"

    "She looks surprised to see you."

    "You understand her confusion; you are surprised to find yourself lying on the floor. Somehow, you slipped off the stool where you were sitting."

    "Giving her an apologetic smile, you slowly try to stand yourself upright."

    you "Oh..."

    menu:
        "对不起，夫人，还没自我介绍呢":
            pass

        "别介意，我刚才在打盹。":
            pass

        "嘿,宝贝。想不想和我到床上打滚呢?":
            pass

    you "Rrr..."

    "Somehow, you really struggle to form a sentence."

    you "RRRRR..."

    "It's like words just won't come out of your mouth."

    you "RRRI..."

    milkmaid "Uh?"

    you "RRRIBBIT!!!" with vpunch

    gizel smirk "Oh, how boorish of me. Allow me to introduce you to [MC.name]."

    milkmaid "Is he... Is he your pet?"

    you "(Pet?)"

    menu:
        "你一定是弄错了...":
            you "Ribbit..." with vpunch
        "我可不是畜生！你瞎了吗?":
            you "Ribbit!!! Ribbit?" with vpunch
        "你管谁叫动物呢，小丫头?":
            you "Ribbibbibibit?" with vpunch

    "Come to think of it, the sounds you are making sound awfully animalistic."

    gizel "Yes, he's my pet. Good boy, [MC.name], good boy..."

    you "Ribbit!" with vpunch

    "The milkmaid looks at you with a frown of disgust."

    milkmaid "I've never seen this kind of... pet... Anywhere..."

    gizel "Oh, it's quite rare. One of a kind, really."

    hide gizel with dissolve

    "Gizel goes behind you and pushes you forward. As she does, her hands bury themselves in the flesh of your back in a strange way, as if you had no backbone."

    play sound s_punch
    with vpunch

    show milkmaid at left:
        linear 0.5 zoom 1.2

    "Still dizzy, you stumble towards the milkmaid."

    show milkmaid at left:
        linear 0.5 zoom 1.0

    "She recoils in fear, but you now stand between her and the exit."

    gizel "Come on, dear, touch it! It loves a little pat."

    you "Ribbit!" with vpunch

    milkmaid "Uh, well... I don't think I should, really... I don't even know what this is..."

    gizel "It's a rare species of {i}batrachius hornus giganticus{/i}. But laypeople just call it a 'giant horny toad'."

    you "Ribbit?"

    gizel blush "Do you know why it's called a horny toad, my dear?"

    milkmaid "Err, I don't know... Because it's got... horns?"

    gizel "Wrong."

    play sound s_punch

    "Gizel viciously kicks you in the back, sending you bouncing straight into the milk girl." with vpunch

    play sound2 s_scream_loud

    scene black with fade
    milkmaid "EEEEK!" with vpunch

    scene bg gizel_toad1 with fade

    "Your mind blanks for a second. When you come back to your senses, you are laying on top of the milk girl, crushing her under your weight."

    menu:
        "哦，对不起!":
            you "Ri, ribbit!"
        "我不是故意的...":
            you "Ribbbit..."
        "呱~呱~呱!":
            you "I'm awfully sorry..."
            play sound s_scream
            milkmaid "It... It spoke!" with vpunch
            play sound s_evil_laugh
            gizel normal "Nonsense. Toads don't talk."

    "Trying desperately to get back up, you wave your flaccid members in all directions, with very little results."

    you "(Why are my arms and legs so... squishy?)"

    play sound s_screams

    milkmaid "Help me!!!" with vpunch

    "Your confused flailing has only served to completely rip her dress. She now finds herself with her large tits exposed."

    you "(Wh... What's this?)"

    "There's something else. Your cock has been rubbing all across her thighs and panties, and is beginning to harden."

    you "(My clothes... What happened?)"

    play sound s_scream

    scene bg gizel_toad2 with dissolve

    milkmaid "Please, mistress Gizel... Your pet is acting weird..." with vpunch

    "You feel a burning hot sensation building up in your erect toad-dick, both alien and familiar."

    you "(Can't... Think... Straight...)"

    "Your cock grows even larger, poking the girl's slit through the thin fabric of her panties."

    play sound s_scream_loud

    milkmaid "Wait!" with vpunch

    "Your mind going completely blank, you start bouncing, rubbing yourself against the girl with increased intensity."

    play sound s_boing

    with vpunch

    scene bg gizel_toad1 with dissolve

    milkmaid "D-Do something! It's... Rubbing me!!!" with vpunch

    gizel blush "Oh, interesting... I think it likes you, dear..."

    "Opening you mouth wide to breathe better, you are only mildly surprised at this point to see a long, lizard-like tongue come out of your mouth. It starts flailing around, then wraps itself around one of the girl's exposed nipples."

    play sound s_scream

    milkmaid "Hey!!!"

    scene bg gizel_toad3 with dissolve

    "Using your strange, pointy animal dick, you force the girl's panties aside, finally ripping them off."

    play sound s_scream_loud

    milkmaid "It's... Nooo!!!"

    gizel "My, look at this... It barely fits in... You lucky girl."

    milkmaid "No, you don't mean... AAAH!!!"

    play sound s_moans

    "The girl tries pushing you away, but her weak punches bounce off inoffensively."

    milkmaid "HAAAAAA!!!" with hpunch

    "Shoving your erect rubbery cock deeper inside her tight pussy, you can feel some strange liquid starting to pour out almost immediately."

    milkmaid "Something... Aah... Something's leaking inside..."

    "The strange, sticky liquid acts as lube, allowing you to slide in and out of her with surprising ease in spite of the large size of your strange cock."

    play sound s_scream_loud

    milkmaid "It's hitting my womb... Aaaah..." with hpunch

    "The intense fucking is beginning to tear away at the girl's resistance, and she now lays back more passively than before, turning her head away from you and moaning."

    gizel "How is it? You're enjoying this, aren't you?"

    play sound s_scream

    milkmaid "No!"

    play sound s_moans

    "In spite of her protest, her pussy seems to ease up and the walls of her womb move apart to better accommodate your dick."

    "Soon, you are able to slide the whole of your cock inside her."

    play sound2 s_scream

    milkmaid "Hiiii!!!" with hpunch

    "The girl is going wild as your well-lubed dick repeatedly hits the mouth of her womb."

    gizel "Wonderful!"

    "The girl clings to you desperately as you feel a flash of white heat burn through you."

    with flash

    you "RIBBIIIIIITTT!!!" with vpunch

    scene bg gizel_toad4 with doubleflash

    with flash

    play sound s_screams

    milkmaid "UHAAAAAA!!!"

    play sound s_orgasm_fast

    "Something much thicker than cum is erupting through your toad-dick, filling the girl's womb to the brim."

    gizel "Go, [MC.name], go!"

    milkmaid "Im... Impossible... Aaaah..."

    "The girl came so hard as you were filling her womb that she cannot move a muscle."

    scene bg gizel_toad5 with dissolve

    "Popping your giant dick out of her ravaged pussy, you spot something round and squishy on the verge of coming out of her."

    milkmaid "Wh..."

    you "Ribbit..." with vpunch

    gizel "Look at this! It's pouring out!"


    play sound s_sucking

    milkmaid "No! I... Aah... AAAAAAH!!!"

    scene bg gizel_toad6 with flash

    "The girl is overwhelmed as more strange toad eggs begin to pour of of her with grotesque squishy sounds, and she climaxes loudly."

    with doubleflash

    play sound2 s_orgasm

    milkmaid "Aaaah, aaah, mmh..."

    "You feel completely exhausted, as if your body was weighing a ton."

    gizel "Good boy, [MC.name]..."

    "You need to rest..."

    scene black with circlein

    pause 2.0

    scene bg farm_stables with circleout

    pause 2.0

    show gizel with dissolve

    gizel smirk "Ah, coming back to your senses, I see..."

    "It seems a few hours have come and gone since you passed out."

    you "You..."

    "Feeling a wave of panic, you flail your arms and legs around, gasping for air."

    "To your immense relief, they are normal, human members now."

    "Slowly getting up, you find your balance has more or less returned."

    you "What a weird dream I just had..."

    play sound s_evil_laugh

    gizel "Dream? That was no dream!"

    you "Uh?"

    gizel "I just used one of my animal philters on you, before I test it on my beloved minion. I keep it in that old cider bottle..."

    gizel normal "I am strongly against animal testing, don't you know?"

    "You step forward menacingly."

    you "Why you..."

    "Gizel looks at you slyly."

    gizel smirk "Come on, don't try and give me the tough guy crap."

    gizel "I'm sure you enjoyed yourself, trying something new... And so did she. I bet she's going to masturbate to this memory every day from now on!"

    gizel normal "But I think I'll need to find somebody new to deliver milk here... She's unlikely to come back."

    you "Don't ever do anything like this to me again, you crazy bitch!" with vpunch

    play sound s_evil_laugh

    gizel smirk "Hey, fighting spirit! I like that in a pet."

    gizel "What's the matter, [MC.name]? Can't you enjoy a little prank? *wink*"

    gizel normal "Talking about pets, it's high time I tended to [name]... You know the way, you can show yourself out."

    you "Grrr..."

    stop music fadeout 3.0

    $ unlock_achievement("h toad")

    scene black with fade

    "You leave the farm and head back to the brothel. You feel all right now, except for a fierce, inexplicable urge to eat houseflies."

    "You didn't get any prestige, because you didn't want {b}{i}anyone{/i}{/b} to know you were turned into a giant toad."

    return

label farm_first_monster():

    stop music fadeout 3.0

    scene black with fade

    "You decide to pay a visit to Gizel to check on her new pensioner."

    if is_censored("monster"):
        menu:
            "Skip event? (monster)"

            "是":
                return
            "否":
                pass

    play sound s_rooster

    show bg farm at top with fade

    you "Hello!"

    play music m_gizel

    show gizel upset with dissolve

    gizel "[MC.name]?"

    you "Hi there, Gizel."

    gizel angry "What do you want? I'm kind of busy."

    you "Are you now?"

    gizel angry "Of course! I don't sit on my ass all day and play pretend brothel owner, not like some people I know!"

    you "Woke up on the wrong side of bed today, uh... What's with the short temper?"

    if debug_mode and not farm.get_minions("monster"):
        $ farm.add_minion(Minion("monster"))

    $ monster = farm.get_minions("monster")[0]

    gizel "Humph! I've been busy trying to domesticate our new resident, [monster.name] the demon."

    you "So what? Doesn't it like the monster den we've set up?"

    gizel "Oh no, it likes it just fine... In fact, it's taken over the whole place."

    you "Taken over?"

    gizel upset "Yes! Come, I'll show you."

    scene bg farm_monster_den with fade

    "You and Gizel are standing next to the large hole in the ground leading to the monster den."

    "Bending over to take a look, you notice a bulging mass of flesh and tentacles, huddling in a corner."

    gizel angry "Watch out. It's quite aggressive."

    you "What's wrong?"

    gizel normal "I've been trying to get it to follow orders, but it doesn't respond to my usual spells."

    you "And?"

    gizel "That mean I cannot control it. It's very dangerous. Who knows what it will do?"

    you "Have you tried approaching it?"

    gizel "No, not until I get a sense of its weaknesses and I am sure I can control it. Believe me, I know these things..."

    menu:
        "同意她的观点":
            $ renpy.block_rollback()
            you "Well... I guess it's better to be safe than sorry."

            gizel angry "Yeah, yeah. Spare me the wise guy bullshit."

            you "What are you gonna do?"

            gizel "I guess I'll ask the monster catcher girl for a replacement."

            you "Can she do that?"

            gizel angry "She will, once you've given me 50 denars to give her for her trouble."

            you "Once I what?"

            gizel upset "Fork the cash over, dumbass!"

            you "Gee, you're impossible today... Fine, here's your gold."

            play sound s_gold

            $ MC.gold -= 50

            gizel normal "I'm going to return this monster. Visit me later, I'll let you know how it is going."

            $ farm.remove_minion(monster)
            $ farm.add_minion(Minion("monster"))
            $ monster2 = farm.get_minions("monster")[0]
            $ story_add_event("farm_second_monster")

            scene black with fade

            "Gizel has returned the tentacle demon to Willow and exchanged it for [monster2.name] the one-eyed monster."

            return

        "不同意她的观点":
            $ renpy.block_rollback()
            you "Come on, I thought you were a powerful witch and all! The wicked witch of the North or some such nonsense."

            gizel angry "Shut up!"

            gizel upset "I am the great white witch of the North! And I didn't live to the ripe age of seven-hundred-fifty by taking unnecessary risks with unknown demons."

            you "All I can see is that you are shaking in your heels at the idea of facing a small-time monster from the Zan sewers."

            you "I don't think they'll spin tales about you around the campfires for that one."

            play sound s_scream

            gizel "Shut up!!!"

            you "I mean, Willow the monster catcher managed to catch this monster single-handedly, and she's  just a teenager... Maybe you should work a little on your fighting techniques!"

            gizel "GRRR..." with vpunch

            "Gizel looks really mad now."

            gizel "I'LL SHOW YOU FIGHTING TECHNIQUES!!!" with vpunch

            "Blind with fury, Gizel rushes to strangle you."

            if MC.playerclass == "战士":
                "You take a step aside, easily dodging her attack."
                gizel "Hey!"
                "Flipping around, Gizel gets ready to leap at your throat."

                gizel "HAAA!!!" with vpunch

                gizel "Uh?"

                "Attracted by the noise and screams, the monster has sneaked a couple of tentacles behind the unsuspecting elf."

                play sound s_crash

                gizel upset "OUCH!" with vpunch

            elif MC.playerclass == "法师":
                "Reaching two fingers to her forehead, you cast a calming spell before she can reach you."

                "She seems to lose all aggressivity and stumbles on her knees."

                gizel soft "Ooooh..."

                you "There, this should relax you, and... "

                you "Uh?"

                "You see a wad of tentacles creeping out ot the gaping hole, probing around. You back off quickly."

                you "Gizel! Don't just stay there!"

                gizel soft "Uh? Where... Where am I..."

                play sound s_surprise

                gizel surprise "Eeek!"

                play sound s_crash

                gizel upset "OUCH!" with vpunch

            elif MC.playerclass == "奸商":

                "You yell, pointing at something behind her."

                you "Watch out! A three headed monkey!"

                play sound s_evil_laugh

                gizel angry "Hahaha! You think I'd fall for such a simple trick?"

                "She mutters something, her hands pulsing with creepy energy. You cower in fear."

                you "Let us work things out!"

                "As she readies her spell, however, a dark shadow rises above her. The monster is leaving its den, looming over Gizel."

                you "Gizel! Behind you!"

                gizel smirk "I told you, that won't work! Prepare to..."

                play sound s_crash

                gizel "Eeek!" with vpunch

        "把她推下去":
            $ renpy.block_rollback()
            $ MC.evil += 1
            you "Oh my... What's that?"

            gizel "What?"

            you "Have you seen what the monster is doing? It's strange..."

            gizel "No, what?"

            you "Bend over, you'll see better."

            gizel "I don't... "

            play sound s_scream_loud

            extend "AAAAH!" with vpunch

            "Giving her a little shove, you send Gizel tumbling down the monster hole."

            you "Hehe..."

            play sound s_crash

            gizel upset "OUCH!" with vpunch

            play sound s_scream_loud

            gizel angry "Why you... EEEEK!!!"

            you "What's the matter Gizel? Don't you enjoy a little prank? *wink*"

    play sound s_roar

    scene black with fade
    show bg gizel_monster1_1 with dissolve

    "Wrapping one of his thick tentacles around her leg, the monster trips Gizel, pulling her towards him."

    play sound s_scream
    gizel "What the... Aah!"

    "The probing tentacles creep all over Gizel's body, while she is firmly held in place by the bigger tentacle, thick as a tree trunk."

    "A mouth-like appendage sticks out a thick tongue that wriggles around Gizel's face, licking her cheek repeatedly with a squishy sound, leaving a trace of gooey liquid."

    gizel soft "So this is what you want, uh..."

    scene bg gizel_monster1_2 with dissolve

    "Gizel looks pissed, but she cannot do anything as the monster keeps probing her body with his inquisitive tentacles."

    play sound s_mmmh

    gizel upset "Hmmm!"

    "One of the thicker tentacles pushes against Gizel's panties, rubbing her slit hard through the thin fabric."

    gizel "AAAH..."

    "For all her display of resistance, Gizel is quickly turned on by the situation, enjoying the slimy monster's attentions."

    scene bg gizel_monster1_3 with dissolve

    "Wriggling its large tongue into the elf girl's mouth, the monster also busies itself attacking the rest of her body."

    play sound2 s_sucking

    gizel blush "NGGGH..."

    "With a flip of its tentacle, the monster rips away her tiny panties, revealing her wet cunt."

    scene bg gizel_monster1_4 with dissolve

    play sound s_surprise

    gizel surprise "Nghh!"

    "Bringing another thick tentacle in play, the monster starts playing harder with Gizel's soft mound and pussy lips."

    play sound s_moans_quiet

    gizel "Mmmmh..."

    "She doesn't even pretend not to like it anymore. She squirms, trying to increase the pressure on her slit and clit."

    gizel "Don't fohget... Ngh... My assh..."

    "As if moving in sync with Gizel's wishes, the monster pokes Gizel's tiny pink asshole with another large tentacle."

    gizel "Nggh!!!" with hpunch

    "Gizel is completely enthralled by the sensations now, and she looks expectantly at the tentacles swirling around her, waiting for the monster's next move."

    scene bg gizel_monster1_4 with dissolve

    play sound s_scream

    gizel "AAAAH!!!"

    "Gizel screams with pleasure as the monster arches one of his tentacles against her tiny pussy, abruptly shoving the tip inside."

    "The other tentacle quickly follows suit, penetrating her cunt with the help of the sticky lube the monster constantly oozes out."

    play sound s_moans_quiet

    gizel "Nggggh..."

    "You watch with interest as Gizel surrenders to the feeling, tentacles being pumped repeatedly in and out of her deformed pussy."

    "The pacing of the monster increases, as if answering Gizel's secret wishes."

    play sound s_moans

    "The thick tentacles keeping Gizel in place seem to tighten around her, almost crushing her frail body. She seems even more turned on by this."

    "The oozing tentacles make lewd sounds as they fuck the little elf mercilessly, each thrust deforming her body in a grotesque way."

    play sound s_screams

    gizel "NGGGGGGH!!!"

    "Gizel cries tears of pleasure and pain as the monster continuously ravages her small body."

    "The monster tongue retreats from the girl elf's mouth, instead holding her head backwards as the tentacles increase their furious pace."

    scene bg gizel_monster1_5 with dissolve

    play sound s_aaah

    gizel "NGGGH!!! *gasp*" with vpunch

#    "Gizel struggles as the tentacle spurts a wad of thick monster cum deep down her throat, forcing her to swallow it all in order not to choke."

#    gizel "Nggh... *gulp* *gulp*"

    "Gizel's love juices mix with the monster's pre-cum and start dripping out of her ravaged pussy. The tentacles in her pussy are completely messing up her insides."

    play sound s_screams

    with flash

    gizel "RAAAAAAH!!!"

    play sound s_orgasm_young
    scene bg gizel_monster1_7 with doubleflash

    "Squeezing gizel like a broken toy, the monster pumps her full of his thick semen, his tentacles shaking uncontrollably as he pours his load."

    "Gizel cannot take it anymore. She is rocked by multiple, continuous orgasms as the monster spits out its cum inside her willing pussy." with flash

    play sound2 s_aaah

    gizel "Aaaah..."

    "Popping its tentacles out, the monster seems to pause for a minute, as if contemplating the result of its handiwork."

    scene black with fade

    "Looking at you with glassy eyes, all fight knocked out of her, Gizel implores you to help her out."

    scene bg farm_monster_den

    gizel shy "It's readying itself for the next round..."

    gizel "Let's get out now... Help... Me..."

    "Gizel cannot even stand up and walk. You'll have to help her up."

    menu:
        "帮助她":
            $ renpy.block_rollback()

            "Carefully going around the resting monster, you reach Gizel and help her up."

            show gizel shy with dissolve

            you "Here, let's leave."

            "With what little strength she has left, Gizel stumbles along with you, thick monster cum still dripping down her legs as she walks out."

            scene black with fade
            show bg farm at top with dissolve

            show gizel soft at center with dissolve

            gizel soft "..."

            you "Are you all right?"

            gizel soft "Well..."

            gizel blush "I'm fine, actually!"

            you "Uh?"

            gizel normal "It seems [monster.name] will be a fine addition to my minions, if a little wild. We can start using it to train your girls."

            you "Oh... Good, then. I guess."

            you "Say..."

            you "You're not mad, are you?"

            gizel smirk "Me, mad? No..."

            play sound s_evil_laugh

            gizel "I'm not mad at all... You'll see... Muhaha..."

            you "'Muhaha'? What are you muhahahing me for?"

            play sound s_evil_laugh

            gizel "Oh, nothing, MUHAHAHAHAHAHA!!!"

            you "Stop that!!!"

            scene black with fade

        "甩下她":
            $ renpy.block_rollback()
            $ MC.evil += 1

            you "What's this? I thought I heard something."

            "Slowly stepping back from Gizel, you pretend not to hear her plea."

            you "Oh, my, look at the time."

            you "I've got a business to run, gotta go back to the brothel! See ya, Gizel!"

            gizel surprise "Wait!!!"

            you "Have fun! I'll see you later! *wink*"

            gizel "[MC.name]!"

            play sound s_punch

            gizel "AAAH!" with vpunch

            "A tentacle grabbing her leg, Gizel is pulled back towards the monster den."

            gizel "WAAAAAAAIT!!!"

            "Ignoring her, you step out of the building, whistling a popular tune, 'Mary had a little womb'."

            scene black with fade

            "You later learn that [monster.name] the monster had fun with Gizel all night, until she could finally get it under control. Although Gizel was pretty mad, she decided to keep [monster.name] for its undeniable raping skills."

            play sound s_spell

            $ monster.level_up(forced=True)

            "Thanks to all this training, [monster.name] has become a level [monster.level] monster."

    return

label farm_second_monster():

    stop music fadeout 3.0

    play sound s_rooster

    scene black
    show bg farm at top with fade

    "You came back to the farm to check on Gizel's progress."

    if is_censored("monster"):
        menu:
            "Skip event? (monster)"

            "是":
                hide bg with dissolve
                return
            "否":
                pass

    you "Hi, Gizel! Gizel? Where are you?"

    you "She must be inside..."

    play sound s_chimes

    scene bg gizel_monster2_1 with fade

    you "Gizel?"

    you "Wh... What are you doing?"

    gizel surprise "Ah, [MC.name]... Help me out here, will you?"

    you "Wh... What's this?"

    if debug_mode and not farm.get_minions("monster"):
        $ farm.add_minion(Minion("monster"))

    $ name = farm.get_minions("monster")[0].name

    gizel soft "It's [name], the new monster I got from the monster catcher."

    gizel "It's an 'one-eyed giant monster', a peculiar type of demon."

    gizel "It's supposed to stare straight into your soul, but all it's been staring at all along is my pussy."

    you "Well, I don't believe you have a soul... But if you had, that's certainly where I'd expect it to be."

    gizel angry "Stop joking! It's, err... What?"

    play sound s_surprise

    gizel surprise "[MC.name], do something! It's looking at me closer!"

    you "Ah, Gizel, I knew you had bedroom eyes, but this?"

    you "Well, it seems to like you..."

    play sound s_scream

    scene bg gizel_monster2_2 with dissolve

    gizel "Aaaah!"

    "Inching closer, the strange creature now starts to rub its giant eye against Gizel's panties."

    gizel "It's weird, aaah!"

    you "He's giving you the stink eye, I think."

    gizel "Why is it... rubbing... like that..."

    play sound s_surprise

    scene bg gizel_monster2_3 with dissolve

    "The monster's big eye oozes a strange liquid which seems to dissolve the fabric of Gizel's tiny panties."

    gizel "What... Ah... What is it doing???"

    play sound s_moans_short

    you "It's a real eye-opener, I guess."

    gizel "Hmmm... It's rubbing me... There..."

    "The monster doesn't seem to want to stop there, however."

    "Tightening the muscles of its neck, the monster pushes hard against Gizel's pussy."

    scene bg gizel_monster2_4 with dissolve

    "Eased in by the mix of his secretions and Gizel's juices, the monster slides his head inside whole."

    play sound s_screams

    gizel "HAAAAA!!!" with vpunch

    you "Wow."

    play sound s_moans

    gizel "It's... It's inside!!! It's moving!"

    "The monster's head bobs up and down, as if looking all around the insides of Gizel's cunt."

    "She takes it all in surprising stride. It must be true that elves are a lot more flexible than humans."

    scene bg gizel_monster2_5 with dissolve

    gizel "It's messing me up!!! Aaaah!!!" with vpunch

    you "I honestly don't know what it sees in you. Literally, I don't."

    gizel "Sh... Shut up!!! AAAH!!!" with vpunch

    you "Come on, don't tell me you don't like the way it's eyeing you?"

    "The monster's head seems to inflate even further, enlarging Gizel's frail pussy even more."

    play sound s_scream_loud

    gizel "HAAAA!!! It's too much!!!"

    play sound s_screams

    with doubleflash

    gizel "I'm CUMMIIIIING!!!" with vpunch

    play sound s_orgasm

    scene bg gizel_monster2_6 with flash

    "The monster's head pops out with an obscene sound as Gizel erupts into a powerful orgasm."

    play sound2 s_aaah

    gizel "AAAAH!!!"

    "Gizel starts squirting like a fountain, spurting her wet juices all around, showering the monster's eye."

    "The strange creature doesn't blink, still looking straight at Gizel's pussy. It seems satisfied with the results of its inspection."

    "Losing interest, it finally crawls away towards the monster den, waddling oddly past you."

    scene bg farm_monster_den with fade

    "Gizel just lays there panting, still reeling in the aftermath of her massive orgasm."

    you "Well, it seems you and [name] are getting along. That's good."

    you "All right, I'll leave you to it then. You better get some shut-eye. *wink wink*"

    gizel angry "Grrrr..."

    scene black with fade

    return


label farm_first_machine():

    stop music fadeout 3.0

    scene black with fade

    "You decide to pay a visit to Gizel, to see how she is doing with her new acquisition."

    if is_censored("machine"):
        menu:
            "Skip event? (machine)"

            "是":
                return
            "否":
                pass

    play sound s_rooster

    show bg farm at top with fade

    you "Gizel?"

    you "..."

    you "Gizel!"

    "No one answers."

    you "Strange, she doesn't seem to be in today."

    you "She's not really the type for going out... I wonder where she went?"

    "Frustrated to have come all the way here for nothing, you decide to take a last look in the backyard before leaving."

    play sound s_ahaa

    you "Gizel?"

    you "That came from the old workshop..."

    scene black with fade

    show bg gizel_machine1 at top with dissolve

    play sound s_surprise

    gizel surprise "Aw, [MC.name]..."

    "Gizel is dangling from a strange array of machinery, ensnared in what looks like a strange mix beween bondage chains and dildos."

    you "What are you playing at?"

    gizel upset "Help me get this untangled, please!"

    you "What's this?"

    if debug_mode and not farm.get_minions("machine"):
        $ farm.add_minion(Minion("machine"))

    $ name = farm.get_minions("machine")[0].name

    gizel angry "It's [name], the artefact you bought! I was trying to set it up for training, but it seems to have a mind of its own..."

    gizel shy "I tried to follow the instructions manual, but... I'm not good with these things, you know?"

    you "I forget, you're ten times older than my own grandam..."

    you "Grandmammy never could quite get the hang of cutting-edge technology. I showed her like twenty times how to use an oil lantern..."

    gizel upset "Quit your rambling and help me! That thing is moving!" with vpunch

    show bg gizel_machine2 with dissolve

    play sound s_aaah

    gizel shy "Oooh..."

    you "Well, I don't know... Aren't you curious to see how it works?"

    gizel upset "Get me untangled first! Then I can figure it out just fine."

    you "Yeah... Say, where are those instructions?"

    gizel "Behind you! Find how to turn that thing off."

    "You spot a dusty old tome on a nearby table."

    you "Let's see, hmm..."

    "It's written in old Valyrian, a language you haven't been able to brush up on since elementary school."

    you "Err... This will be difficult."

    gizel upset "Come on! Just find the release rune, damn it!" with vpunch

    you "Give me a second..."

    "You spot something that looks like the release rune. Definitely, it must be it."

    you "There it is! {i}Habith, karzawat!{/i}"

    play sound s_spell

    show bg gizel_machine3 with dissolve

    play sound s_scream

    gizel angry "[MC.name], you idiot!!!" with vpunch

    play sound3 s_vibro

    gizel blush "It's moving now... Inside me... Aaah..."

    you "Oops."

    play sound3 s_vibro

    gizel "What are you doing! Find a solution!" with vpunch

    you "I guess I must have been mistaken, haha..."

    "Flipping through the pages, you search for some combination of symbols you can understand."

    you "Here, let's try this. {i}Zortawort, mazeltov...{/i}"

    play sound s_boing

    show bg gizel_machine3 with vpunch

    play sound s_scream_loud

    gizel "HAAAA!!!" with vpunch

    you "Nope, definitely not that."

    $ screaming = MC.name + MC.name[-1] * 3

    gizel "Damn you, [MC.name]!!!" with vpunch

    you "My bad, I read that wrong. Just hold on a second, I'll find something..."

    play sound s_moans

    gizel "Hurry, damn it!!! Haaaa!!!"

    you "I think this means, uh... Hard mode?"

    play sound s_scream_loud

    gizel surprise "Don't, don't use that!"

    you "I know, I won't, don't worry... It's too hard to pronounce, anyway. {i}glorktazuh wladernock{/i}, or some such..."

    play sound s_sheath

    show bg gizel_machine4 with dissolve

    "Bumping spikes protrude out of the buzzing dildos, increasing the pressure on Gizel's soft body."

    play sound s_screams

    gizel upset "EEEEEK!!! STOP FUCKING AROUND!!!" with vpunch

    you "Wow, look at that! My pronunciation isn't that bad, after all! To think that head teacher Klint kept saying that I would never amount to anything..."

    play sound s_moans

    gizel angry "I'll... Ahhh... Kill you... Aaaah... You bastard..." with hpunch

    you "Now now, don't be so melodramatic. I think I'm getting the hang of this."

    play sound s_ahaa

    gizel blush "Do... Aaah... Something..."

    play sound s_moans_short

    you "That's it, I found it!" with vpunch

    you "That rune! It's 'release'! I know it!"

    gizel "Are you... Sure... Ngggh..."

    you "{i}Cumath Anh Pussieth{/i}! Release!"

    play sound s_scream_loud

    show bg gizel_machine5 with doubleflash

    "Buzzing with unholy power, the machine starts releasing a powerful electric current with a crackling of energy, sending Gizel over the edge."

    play sound s_vibro

    with flash

    play sound s_scream

    gizel blush "Hnnnnn!!!"

    play sound s_orgasm_fast

    gizel "It's too much, I'm... I'm..."

    with flash

    play sound s_screams

    gizel "CUMMIIIIIIIIING!!!" with vpunch

    with doubleflash

    play sound s_orgasm

    "Gizel screams and squirts love juices everywhere as the torture machine sends her into a hard climax."

    you "Wow, would you look at that!"

    show bg gizel_machine6 with flash

    play sound s_mmmh

    gizel shy "Ahhh...."

    you "This big red button, on the machine! I hadn't seen it. It says: 'OFF'. Maybe we should try it?"

    play sound s_vibro

    "Pressing the button, the machine stops whirring and falls inert."

    you "That did it!"

    gizel "..."

    play sound s_ahaa


    gizel angry "You fucking asshole!!!"

    you "Come on, show a little more appreciation for my help, will you?"

    gizel "I'll... I'll kill you..."

    you "All right. I can see you're tired, I'll leave you to rest."

    you "Don't worry, you can thank me later. I'm not mad."

    gizel "What???" with vpunch

    gizel "Hey! Come, come back here! I'll... Hey!" with vpunch

    scene black with fade

    "Thanks to your invaluable help, Gizel has learned from first-hand experience how [name] works. You saved the day once again. Well done!"

    return

label farm_first_stallion():

    stop music fadeout 3.0

    scene black with fade

    "Today's perfect weather is great for enjoying a little stroll in the countryside. You decide to pay Gizel a visit."

    play sound s_rooster

    show bg farm at top with fade

    you "Hello? Is anyone here?"

    play sound s_moans_quiet

    "Coming from inside the building, you hear familiar muffled sounds."

    play sound s_door

    scene black with fade
    show bg gizel_big2_1 with dissolve

    you "Uh, hello?"

    play sound s_moans

    gizel blush "Mmmmh, aaah..."

    "You clear your throat."

    you "Ahem."

    play sound s_mmmh

    gizel blush "Oh, [MC.name]... Hi..."

    gizel "Make yourself comfortable. I'll be a minute..."

    you "Uh, really?"

    "The huge man who is busy grinding his fat dick against Gizel's pussy turns his muscular neck and gives you an empty stare."

    you "Hi there, big fella... Bob, was it?"

    $ name = farm.get_minions("stallion")[-1].name

    play sound s_moans

    gizel "That's not Bob! It's [name], the new slave you bought... Mmmmh, aaah..."

    play sound s_mmmh

    show bg gizel_big2_2 with dissolve

    gizel "Oh, that's it, big boy, give it to me..."

    you "Err, I'll give you two some space all right?"

    gizel "Yes... Push it inside!"

    you "Ahem."

    "Looking away with embarrassment, you see a nice-looking brochure, left out on a table."

    you "'Welcoming your first stallion in the family, a friendly guide' from Blood Orange Inc., sponsored by the Blood Islands' Tourist Office."

    you "I'll just read this if you don't mind?"

    show bg gizel_big2_3 with dissolve

    play sound s_moans_short

    gizel "YES! Fuck me! Harder! Fuck me, you beast!" with hpunch

    you "I think she doesn't mind."

    with hpunch

    "Fancy Brochure" "Congratulations on acquiring your first stallion. It will be a perfect addition to the family, providing endless pleasure to everyone from your daughters to your old grandam."

    you "I'd better not picture that."

    with hpunch

    "Fancy Brochure" "Stallions are raised in the safety of the Blood Islands' magic ranches, where they are free to roam around their eco-friendly metal cage."

    "Fancy Brochure" "Don't listen to the naysayers who argue that it is cruel to keep them in dark, dank and narrow spaces: those cages are not tiny, they are {b}cozy{/b}."

    "Fancy Brochure" "Generations of stallion-breeders have achieved great success in selecting the best breeds for dick-size and sex drive, literally bringing you the most {b}bang{/b} for your buck."

    play sound s_screams

    show bg gizel_big2_4 with dissolve

    gizel "Ah, ah, oh, keep at it!!! Ravage me inside!" with hpunch

    "Fancy Brochure" "Submitted to a wide range of totally safe and ethical magical rituals from the youngest age, our stallions' sex drive and obedience are increased to dizzying levels by the great work of our mind-bending engineers."

    "Fancy Brochure" "Of course, generations of in-breeding, and the side-effects of magical lobotomy, make our stallions a little 'simple', shall we say."

    "Fancy Brochure" "But simple as they are, we can assure you that they love their mistresses and masters with the same passion and commitment that 'Blood Orange Inc.' loves its bottom line."

    play sound s_screams

    gizel "YES!!! I'm cumming! Fill me up to the brim, you fucking bastard!!!" with vpunch

    "Fancy Brochure" "Warning: Because our stallions produce as much semen in a week as a regular human male in a year, we strongly advise that you 'milk' them at least once a day. They are too stupid to masturbate."

    with flash

    play sound s_screams

    show bg gizel_big2_5 with doubleflash

    gizel "AAAH!!!" with vpunch

    play sound s_orgasm

    "Fancy Brochure" "We at 'Blood Orange Inc.' hope that your stallion will give you a wonderful time over the upcoming weeks or months. While we are sorry that our legal team doesn't allow us to give you any kind of warranty, do not believe the rumors about 'planned obsolescence' and limp dick malfunctions."

    "Fancy Brochure" "Just make sure you upgrade your stallion to a new model every year, and everything will be {b}just fine{/b}*!\n\n{size=-12}*: non-contractual{/size}"

    play sound s_moans_quiet

    gizel "Aaah, mmmhh..."

    play sound s_mmmh

    you "Well, it seems that the new guy is fitting right in, doesn't it?"

    gizel "He sure was..."

    you "Now, if you're quite finished..."

    gizel "It's getting hard again! Look!"

    you "But wait..."

    gizel upset "Fuck me again! Fuck me more, you wild beast!" with vpunch

    you "Not again..."

    scene black with fade

    "You give up on talking to Gizel for today. She's having way too much fun."

    return


label bitches_be_crazy():

    scene black
    show bg armory at top
    with fade

    "This morning, you asked Sill to fetch your old Valyrian dictionary."

    show sill happy at center

    sill "Master! Here it is."

    you "Look for those words: {i}Lutaneth Mot Garazoth{/i}. I wanna know what it means."

    sill "It means, err..."

    you "What?"

    sill sad "'Bitches be crazy'."

    you "Oh."

    "It turns out the ancient Valyrians didn't usurp their reputation for great wisdom, after all."

    scene black with fade

    return


#### SHOP SCENE ####

label shop_bath_scene(): # Has a 1% chance of happening when visiting the shop after you bought 10 items

    scene black with fade

    play sound s_chimes

    you "Ahem... Hello?"

    "The shop seems empty. You hear some muffled sounds in the back."

    play sound s_splash

    you "..."

    you "Hello??"

    play sound s_surprise

    shopgirl "Yes?"

    shopgirl "[MC.name], is that you? Come over here, I'm in the back."

    show bg shop bath with fade

    play sound s_laugh

    "You find the shopkeeper relaxing in her bath. She gives you a playful look, making no effort to hide her body."

    you "Oh... I... I'm sorry, I didn't mean to interrupt..."

    shopgirl "Come on, stay, don't be shy. I'll just be a minute."

    you "Ahem... I'll wait for you outside, then..."

    play sound s_surprise

    shopgirl "Wait."

    shopgirl "Wait a minute... Won't you give me a little back rub? *purr*"

    play sound s_sigh

    you "Well... *gulp*"

    scene black with fade

    play sound s_splash

    shopgirl "Oh, I like that..."

    play sound s_laugh

    shopgirl "Keep going... Down... Down... Yes..."

    play sound s_mmmh

    $ unlock_achievement("h shop")
    with fade

    $ MC.change_prestige(1)

    "You have earned prestige."

    return


## SATELLA EVENTS ##

label satella_letter(): # Occurs some time after Chapter 1 is complete. Then occurs again every month.

    if story_flags["shalia_visit"]: # Does not happen if the Shalia path has been completed
        return

    play sound s_knocks

    scene black
    show bg master room at top
    with fade

    "Early in the morning, you hear a weak knock on your window. Curious to see where it comes from, you approach the window cautiously, a hand on your dagger."

    if not story_flags["satella_letter"]: # This happens the first time you receive the letter
#         $ story_flags["satella_letter"] = True # story_flags is a defaultdict (default=False) used to store all story variables

        play sound s_creak

        you "What do you... Uh?"

        "You are surprised to see a raccoon standing on the ledge in a stiff pose, his head tilted in an unnatural way."

        raccoon "..."

        you "My, would you look at that... A dead raccoon. Nice prank, motherfuckers!"

        "You look around, but see no one. You notice the raccoon has something in his mouth."

        you "A... A letter? For me?"

        play sound s_roar

        "Suddenly opening its mouth, the raccoon lets out a chilling, uncanny snarl, dropping the letter on the ledge. You jump backwards."

        play sound s_wscream

        you "AAAH!!! UNDEAD RACCOON!!!"

        "After growling defiantly for a few more seconds, the raccoon stops, and drops flat on his face. That's when you notice the smell."

        you "Ew... DEAD RACCOON!"

        "Grabbing the letter, you yell for a maid to clean up the mess."

        you "What the... Anyway, let's have a look at this letter."

        play sound s_dress

        call screen letter(header = "Urgent invitation", message = "Dear " + MC.name + ",\n\nIt's been a while since you last visited me. I'm disappointed. After all, you and I are best friends, aren't we?\nDon't {b}disappoint{/b} me. That makes me angry.\nWhen I'm angry, I break things. And people.\nPlease visit me soon, I have, uh, something urgent to tell you.\n\nCome! It will be fun!",
                          signature = "Night Mistress Satella {font=[style.default.font]}{size=-18}[emo_heart]")

        you "Oh... Satella is summoning me to Shalia's temple... It must be important."

        you "I mean... It must be, right?"

        $ story_add_event("satella_first_visit")

        "Visit Satella at the {b}Thieves Guild{/b}."

    else:
        play sound s_creak

        raccoon "..."

        you "Oh. Another dead raccoon, holding another letter. How original."

        raccoon "*yap*"

        you "Screw you, zombie raccoon. You stink."

        raccoon "*pained growl*"

        "The raccoon drops dead. Again."

        you "Let's see that letter."

        play sound s_dress

        call screen letter(header = "紧急事态", message = "亲爱的 " + MC.name + ",\n\n我需要马上见到你。事实上，你昨天就该来我这了。\n你昨天跑去哪鬼混了???\n不要背信弃义，叛徒往往都没有好下场。\n立刻来公会见我。",
                          signature = "你的秘密情人 Satella {font=[style.default.font]}{size=-18}[emo_heart]")

        you "I've got a bad feeling about this."

        $ story_add_event("satella_visit")

        "Visit Satella at the {b}Thieves Guild{/b}."

    return


label satella_first_visit(): # Happens when visiting the thieves guild after the letter event is complete

    stop music fadeout 3.0

    scene black with fade

    "After some trial and error, you eventually find the dark staircase beneath the Thieves Guild that leads to Shalia's shrine."

    you "Careful now, I don't want to fall down one of the pits Renza was talking about..."

    you "Here we are..."

    play sound s_creak

    play music m_demons fadein 3.0

    show bg shalia_temple at top with dissolve

    you "Hello?"

    with flash

    play sound s_thunder

    you "Aaaah!!!"

    show satella_standing with dissolve

    play sound s_evil_laugh

    stop music fadeout 3.0

    satella "Teeheehee! I scared you!"

    play music m_satella fadein 3.0

    you "Oh, it's you... I almost had a heart attack!"

    play sound s_evil_laugh

    satella "I know, awesome, right?"

    you "Grr..."

    satella "Anyway, you're not dead yet."

    satella "If you were, I could reanimate you with the leftovers of my necromantic ketchup, but your skin would fall off, and the smell would be horrible."

    satella "Want some?"

    you "Err, no thanks. I just came to visit because you said it was urgent..."

    play sound s_surprise

    satella "Uh?"

    you "The letter. The undead raccoon. It came to me."

    satella "Oh, that! Teeheehee..."

    satella "I was bored, so I sent one to everyone I know in town. I have many dead raccoons, that's one of the perks...."

    satella "Anyway. It's good you came, though! We can have a game night!"

    you "..."

    you "I came all the way down here, nearly stumbling into pitfalls, almost having a heart attack..."

    satella "Yeah, yeah, don't thank me! But we can have even more fun!"

    satella "Puh-lea-se... [MC.name]... [emo_heart]"

    "She looks very excited."

    "You look at her small, juicy teenage body, squeezed by her tight leather suit. You wonder what kind of 'fun' she has in mind. Perhaps..."

    play sound s_surprise

    satella "Let's play cards!" with vpunch

    you "Duh."

    "Satella gestures wildly towards the altar at the back of the shrine. You notice it's been covered with green felt, cards and poker chips strewn out everywhere. Stilted figures are sitting in the shadows by the improvised game table."

    satella "It's going to be fun!!! Let me introduce you to our regular players."

    hide satella_standing with dissolve

    show blue_demon at right with dissolve

    satella "This is Akuma. He is not so good at this game, but he is persistent. I must warn you though, he is a sore loser."

    "From all accounts, Akuma seems to be a wooden statue. Cards have been awkwardly stuffed in his hands, but half of them have fallen out on the table."

    hide blue_demon with dissolve
    show red_demon at left with dissolve

    satella "Next, there is Gouki. Gouki is quite the joker, always pulling pranks and making fun of Akuma. You're gonna love him."

    "Gouki seems to be another wooden statue, looking at the table with an empty stare."

    satella "Finally, our guest of honor..."

    hide red_demon with dissolve
    show skeleton at centertextbox with dissolve

    satella "Rodrigo!"

    you "Uh..."

    satella "Rodrigo was a templar of Arios, and he was very naughty. He tried to destroy our shrine, can you believe it?"

    satella "But he's a lot nicer since he's dead, honest. We're like, best friends forever now! Right, Rodrigo?"

    rodrigo "..."

    satella "See?"

    you "Err, Lady Night Mistress..."

    satella "Come on! My name is Satella. But you can call me Shirley."

    you "Shirley, I mean, Satella... I don't think the players around this table can actually play..."

    satella "Oh, don't be like that. I know they're not hot, semi-pro gamblers like you and me, but you don't have to rub it in their face..."

    you "No, I mean, they're statues, you see? And this one... This one is a corpse!"

    rodrigo "..."

    satella "Don't say that! You'll hurt Rodrigo's feelings, you know. He prefers the term 'post-living person'."

    you "*sigh*"

    hide skeleton with dissolve

    satella "Very well, you're in! Let's do a pretend round. I won't get mad if I lose, haha."

    "Satella gathers the cards around the table and start shuffling them. Half of them are still face up, and she seems unbothered that she forgot about a dozen cards on the floor."

    satella "This is a game called Blood Poker. You know it?"

    you "Well... No."

    satella "Good! Me neither! Rodrigo is going to explain the rules."

    rodrigo "..."

    satella "That makes sense! All right, here we go."

    "Satella begins dealing the cards around, with no apparent method to her madness. After starting over a few times, she eventually manages to deal five cards to every player."

    "You take a look at your hand."

    you "(Wow! A royal flush!!!)" with vpunch

    "You can't believe your luck. You take a peek at your opponents."

    "Satella is struggling to arrange her cards, seemingly intensely concentrated on her hand with her tongue sticking out."

    "The other 'players', being made of wood and bone, sit silently in front of the heap of cards in front of them."

    play sound s_laugh

    satella "Teeheehee..."

    gouki "..."

    rodrigo "..."

    akuma "..."

    you "So... Who goes first?"

    play sound s_punch

    satella "I DO! I DO!" with vpunch

    you "All right..."

    satella "I have..."

    play sound s_surprise

    extend "THREE OF A CARD!" with vpunch

    "Satella slaps her hand on the table, with three cards facing backwards."

    you "Ahem... It's 'three of a kind'... And actually, you are looking at the wrong side of the cards, that's why they have the same design..."

    satella "Oh! Right!"

    satella "I didn't know that rule. You're good!!! Well, ok. How about that? I have..."

    "Satella slams her hand on the altar."

    play sound s_punch

    satella "A PAIR OF 7s!!!" with vpunch

    you "Ah... Yes... Actually, you do."

    satella "AAAAALL IN!!!" with vpunch

    you "Uh?"

    satella "I yell 'ALL IN'! That's part of the game!"

    you "Well, uh, I know... But... It means you are betting all your chips on this hand, and you've got, er... A pair of 7s."

    satella "Exactly!"

    you "Are... Are you sure?"

    play sound s_punch

    satella "AAAAAAAAAAAALL IIIIIIIIIIIIIIIIN!!!" with vpunch

    play sound s_evil_laugh

    "She lets out a maniacal laugh."

    you "All right then... Suit yourself..."

    satella "Now, it's Gouki's turn."

    show red_demon at left with dissolve

    gouki "..."

    satella "Come on buddy, don't be shy, show us your hand... A pair of 5s!!!"

    play sound s_evil_laugh

    satella "BOOOOH!!!"

    satella "YOU SUCK BALLS, AMIGO!!!" with vpunch

    "It seems Satella is a little bit too intense about this game."

    hide red_demon with dissolve

    satella "All right, it's Rodrigo's turn. Rodrigo?"

    show skeleton at centertextbox with dissolve

    rodrigo "..."

    satella "You think you're some big shot, uh, trying to fool us with your poker face? All right, show us your hand..."

    "Satella turns Rodrigo's cards over. He's got four aces."

    satella "One, two, three... Four... Hey! He's got four of a card!"

    you "Of a kind... {size=-6}(Also, how are there 5 aces in this deck??){/size}"

    satella angry "B-But... I've got 7s, and he's got only 1s, so... I win, right?"

    you "Well... I'm sorry, Satella, but you lost... A four of a kind beats a pair, in all of the poker versions I know..."

    "Satella's eyes start to well up with tears."

    satella "B-But... I... I said 'ALL IN'..."

    you "Well... It's just a practice round anyway..."

    satella "Uh... "

    stop music fadeout 3.0

    extend "Uwaaaah!!!"

    with hpunch

    with hpunch

    play music m_demons fadein 3.0

    "Satella starts wailing and the lights flicker. The ground starts to shake."

    satella "UWAAAAAAH!!! RODRIGO!!! YOU BIG MEANIE!!!" with hpunch

    you "Satella... Uh, Shirley... Calm down..."

    scene black with dissolve

    satella angry "RODRIGO! I saw you... YOU CHEATED!!!"

    play sound s_mystery

    satella "WHAT DO YOU HAVE TO SAY FOR YOURSELF?"

    rodrigo "..."

    stop music fadeout 3.0

    play sound s_spell

    scene black
    show bg satella casting at quake

    satella "DIE, YOU FUCKING BONEBAG BACKSTABBER!!!"

    with vpunch

    play sound s_fire

    scene black
    show bg shalia_temple at top
    show skeleton at centertextbox
    with dissolve

    pause 0.5

    play sound2 s_fire

    pause 0.2

    play sound3 s_fire

    pause 0.3

    play sound s_fire

    "Blinding ethereal light is radiating from Satella's body. The skeleton bursts into pink flames."

    play sound s_crash

    hide skeleton with pixellate

    "The influx of dark power blows the skeleton to smithereens, sending burning bone fragments everywhere. Both wooden statues catch fire, while you try desperately to stop your clothing from burning."

    play sound s_wscream

    you "Aaaaah!!!"

    satella "GRRRR..."

    stop music fadeout 3.0

    "The dust settles, and the lighting returns to normal. There is a long silence, only broken by the crackling sound of the burning statues."

    "Satella seems to have cooled off. She returns to her cheerful personality."

    play music m_satella

    show satella with dissolve

    satella "Ok then! Let's move on with the game. [emo_heart]"

    satella "Rodrigo's been excluded because he is a bad, bad cheater. BOOH!"

    "A brief flicker of fiery rage passes through Satella's eyes."

    satella "Now. It's your turn, Akuma. What's your play?"

    hide satella with dissolve
    show blue_demon at right with dissolve

    akuma "..."

    play sound s_fire

    pause 0.3

    play sound s_crash

    hide blue_demon with pixellate

    "The burning statue crumbles, turning to ashes before your eyes."

    satella "Oh."

    satella "He's folding. Look at him sulk... I told you he was a sore loser. Very well, that's just you and me now! Can you beat a pair of 7s?"

    "You look down at your royal flush. It doesn't look like such a lucky streak now."

    satella "So? Can you beat me?"

    satella angry "CAN YOU MOTHERFUCKER, UH, CAN YOU???" with vpunch

    "Satella's voice distorts, and pink flames start to burn in her eyes."

    you "Err... I... Uh..."

    you "I fold!" with vpunch

    you "You win!"

    you "Haha, haha, hahahaha... *sweat heavily*"

    satella happy "I... I did?"

    satella "YAY!" with vpunch

    satella "I BEAT YOU! I BEAT YOU! I'M THE BEST!"

    satella "I RULE GAME NIGHT!!!"

    you "Ugh..."

    play sound s_laugh

    satella "Oh, man, you really suck at this game... *giggle* You're lucky it was a practice run!"

    satella angry "I get really serious when it's for real..."

    satella happy "So, who's up for a rematch?"

    show red_demon at left with dissolve

    gouki "..."

    play sound s_fire

    pause 0.3

    play sound s_crash

    hide red_demon with pixellate

    "Gouki falls apart in a cloud of ashes."

    satella "Come on Gouki, where's your sense of humor?"

    satella "Well, Gouki and Akuma are out, Rodrigo is a dirty cheater, and you suck."

    satella "It seems we ran out of players..."

    you "Oh my, look at the time... Ahem."

    satella "I guess that will be all for tonight, then. Come back next time! We'll play a different game!"

    you "..."

    satella "Oh, and have this. It was Rodrigo's money, but I am taking it away, because he is a dirty cheater. AREN'T YOU, RODRIGO?"

    "She yells at the pile of ash and bone dust that used to be Rodrigo. Shrugging, you pocket the money and get the hell out of here."

    stop music fadeout 3.0

    scene black with fade

    play sound s_gold

    $ MC.gold += 300

    "You have received 300 gold."

    $ story_remove_event("satella_first_visit")
    $ calendar.set_alarm(calendar.time+14, StoryEvent(label = "satella_letter", type = "morning"))

    if MC.god == "莎莉娅":
        $ calendar.set_alarm(calendar.time+1, StoryEvent(label = "shalia2", type = "morning"))

    return

label satella_visit(): # Happens on all subsequent visits to Satella (visiting thieves guild after receiving a letter)

    $ story_remove_event("satella_visit") # Avoids the event proc-ing again without receiving a new letter

    $ calendar.set_alarm(calendar.time+14, StoryEvent(label = "satella_letter", type = "morning"))

    stop music fadeout 3.0

    scene black with fade

    "The way to Shalia's shrine is familiar to you now. You find the hidden steps and begin the long descent into darkness."

    you "I should take a turn after the next crumbling skeleton... Ah, there it is."

    play sound s_creak

    show bg shalia_temple at top with dissolve

    you "..."

    show satella_standing with dissolve

    play music m_satella fadein 3.0

    you "Hi, Satella."

    play sound s_surprise

    if NPC_satella.love < 50:

        satella "Oh! [MC.name]! What's up?"

        you "I've received another summon through the raccoon-express, telling me you had to see me, and that it was urgent..."

        satella "Oh, yes! Very urgent! But you made it in time... In time for... "

    else:

        satella "Oh! [MC.name]... *blush*"

        "Satella looks embarrassed."

        you "Are you ok?"

        satella "Well, uh... I, er..."

        you "Yes?"

        satella angry "Did... Did anything happen last time? I mean... during game night?"

        you "Well... Er... I don't recall... *sweat*"

        satella "Because I cannot remember anything, except I passed out... I felt... Very strange..."

        you "Oh, haha, well... I think you had a bit too much of that magical tea, I guess, hahaha... *sweat* *sweat*"

        satella "Right..."

        satella happy "I do drink a bit too much tea, it's true! It makes me pee a lot, you know? Maybe that explains..."

        "She trails off for a moment."

        satella "Anyway. Thanks for coming. You are just in time for..."

    play sound s_thunder

    with flash

    satella "GAME NIGHT!" with vpunch

    you "Err... I'd feel more comfortable without the doomsday lightning and the thunder special effects..."

    satella "Come on, don't spoil the mood!"

    satella "Game night hasn't been the same since Rodrigo left us. Ungrateful bastard, he is."

    satella angry "Grrr..."

    you "Wasn't it you that blew him up..."

    "Satella starts to tap her foot impatiently."

    $ game_type = rand_choice(["tag", "the guessing game", "rock scissor paper"])

    satella happy "Boooring!!! Come on! Let's play [game_type]!" with vpunch

    you "*sigh* If we must..."

    call satella_game(game_type) from _call_satella_game

    return


label satella_game(game_type="the guessing game"):

    if game_type == "tag":
        satella "So, we're playing tag... You have to find me!"

        you "But... We're in the middle of a temple to the Goddess... And there are no places to hide, anyway..."

        satella "That's why! That's why we play tag... In the {b}dark{/b}!"

        you "Uh?"

        stop music fadeout 3.0

        play sound s_fire

        hide bg with dissolve

        "The Night Mistress claps her hands, and all the candles are blown out. You both remain in complete darkness."

        you "Oh..."

        satella "You're it! Try and catch us!"

        you "Uh... Us?"

        satella "Of course! My friends are playing too!"

        play sound s_mystery

        satella "They don't like to get out in the light, you see... See ya! [emo_heart]"

        hide satella_standing with dissolve

        play music m_demons fadein 3.0

        you "Is... Someone else in there?"

        play sound s_mystery

        you "..."

        play sound s_maniacal_laugh

        "An evil laugh echoes from the depths of the old temple."

        you "AAAH!"

        "Heavy stomping and nasty creeping sounds echo from the corner of the temple. You cannot see anything in the pitch black darkness."

        you "Well, uh, Satella... Satella?"

        you "Satella!"

        $ r = dice(6)

        "Wandering awkwardly, you try to retreat from the blood-curling sounds. Suddenly, you feel a presence next to you. {i}Someone{/i} is here."

        you "Haha..."

        play sound s_punch

        you "Satella! I've got you!"

        if r <= 4:

            $ renpy.say("", rand_choice(("Reaching in the dark, you grab a handful of hair. It's awfully thick and coarse.", "Reaching in the dark, your hand meets a viscous, moist surface. It feels like frog-skin. An awfully large frog.", "Reaching in the dark, you grab something that feels like a large horn. Or is that a tooth?")))

            you "Sat... Satella?"

            play sound s_roar

            "Thing in the darkness" "*mad roar*" with vpunch

            play sound s_punch

            pause 0.3

            play sound2 s_wscream

            you "AAAAAAH!!!" with vpunch

            play sound s_mystery

            stop music fadeout 3.0

            scene black with fade

            show bg thieves_guild at top with dissolve

            "When you wake up, you are lying in the gutter outside the thieves guild. You feel like a ragdoll after being played with by a very large dog."

            you "Ouch... My head..."

            $ MC.interactions = 0

            "You have lost all of your remaining actions for the day."

        else:

            stop music fadeout 3.0

            you "Gotcha!" with vpunch

            play sound s_horn

            "Your hand grabs something soft and squishy."

            play sound s_scream_loud

            satella angry "EEEK!"

            "Unsure if you got her or not, you squeeze the soft part again."

            play sound s_horn

            pause 0.5

            play sound2 s_scream

            satella "UWAAAAAH!!!"

            you "Satella?"

            play sound s_scream

            satella "HOW DARE YOU!!! GRRRR..."

            you "Oops."

            call satella_thunderbolt() from _call_satella_thunderbolt

    elif game_type == "the guessing game":

        play sound s_creak

        "Satella opens an old chest and takes out two giant bone dice."

        satella "Behold! Those dice are made of Juggernaut ivory, polished with dragon stomach acid. They have stood at the bottom of the ocean for a thousand millenia, crushed by unimaginable pressure."

        you "Wow..."

        satella "Also, they're loaded."

        you "Those relics must be priceless..."

        satella "Well, they would be, if they weren't cursed. The person who wields them usually dies eaten by supernatural horrors within a week."

        you "Ew! Get them away from me!"

        satella "I can't tell you how many supernatural horrors I have to crush every week just to keep those. It's tiresome, although I relish the company."

        satella "Also, they're shiny. I like that."

        you "What... What are you going to do with these relics?"

        satella "Why, play of course! We can play a guessing game."

        you "..."

        satella "I'll throw the dice into this giant seashell. You can ask me three 'yes or no' questions. Then try to guess the exact number. Got it?"

        label satella_game_guess_menu():

            menu:
                extend ""

                "来玩两把吧":
                    satella "Very well, I shall roll the dice... Hmmpf!"

                    play sound s_dice
                    pause 0.1
                    play sound2 s_dice

                    $ d1, d2 = dice(6), dice(6)
                    $ tries = 1

                    satella "Okay! We've got a number. Remember, you've got three questions!"

                "如果我赢了会我能得到什么?":
                    satella "Well... I have some junk items in the back. I can let you have one of them, if you guess right."
                    jump satella_game_guess_menu

                "如果我输了会发生什么事?":
                    play sound s_evil_laugh
                    satella "Bwahaha!!! I'll fry your guts, just like all the other losers! How do you think I got all those items in the first place?"
                    you "*gulp*"
                    jump satella_game_guess_menu

            while tries <= 3:

                label satella_game_guess_loop():

                    $ renpy.block_rollback()

                    if tries == 1:
                        satella "This is your first question. Go ahead."
                        $ answers = ""
                    elif tries == 2:
                        satella "Second question. "

                    else:
                        satella "Last question. You'd better guess right! "

                    menu:
                        extend "\n{i}[answers]{/i}"

                        "数字大于...":
                            $ r = renpy.input("Is the number above...", default="7")

                            python:
                                try:
                                    r = int(r)

                                    if r < 2 or r > 12:
                                        renpy.say("", "Please choose a number between 2 and 12.")
                                        renpy.jump('satella_game_guess_loop')

                                except:
                                    renpy.say("", "Please choose a number between 2 and 12.")
                                    renpy.jump("satella_game_guess_loop")

                            if d1+d2 > r:
                                satella "Yes!"

                                $ answers += "\nThe total is above " + str(r) + ". "

                            else:
                                satella "No..."

                                $ answers += "\nThe total is below " + str(r+1) + ". "


                        "数字小于...":
                            $ r = renpy.input("Is the number below...", default="7")

                            python:
                                try:
                                    r = int(r)

                                    if r < 2 or r > 12:
                                        renpy.say("", "Please choose a number between 2 and 12.")
                                        renpy.jump("satella_game_guess_loop")

                                except:
                                    renpy.say("", "Please choose a number between 2 and 12.")
                                    renpy.jump("satella_game_guess_loop")

                            if d1+d2 < r:
                                satella "Yes!"

                                $ answers += "\nThe total is below " + str(r) + ". "

                            else:
                                satella "No..."

                                $ answers += "\nThe total is above " + str(r-1) + ". "

                        "你掷出的点数是...":
                            $ r = menu([("Did you roll a...", None), ("One", 1), ("Two", 2), ("Three", 3), ("Four", 4), ("Five", 5), ("Six", 6)])

                            if d1 == r or d2 == r:
                                satella "Yes!"

                                $ answers += "\nSatella rolled a " + str(r) + ". "

                            else:
                                satella "Nope. Try again."

                                $ answers += "\nSatella didn't roll a " + str(r) + ". "

                        "两个骰子点数相同吗？":

                            if d1 == d2:
                                satella "I did! Aw, you're good!"
                                $ answers += "\nSatella rolled twice the same number. "
                            else:
                                satella "Haha, no!"
                                $ answers += "\nSatella rolled different numbers. "

                        "骰子点数之和是奇数吗？":

                            if (d1+d2) % 2 != 0:
                                satella "That's right! Aw, I hope you didn't peek..."
                                $ answers += "\nSatella rolled an odd number. "

                            else:
                                satella "Wrong... [emo_heart]"
                                $ answers += "\nSatella rolled an even number. "

                        "骰子点数之和是偶数吗？":

                            if (d1+d2) % 2 == 0:
                                satella "That's right! Aw, I hope you didn't peek..."
                                $ answers += "\nSatella rolled an even number. "

                            else:
                                satella "Wrong... Bwahahahaha [emo_heart]"
                                $ answers += "\nSatella rolled an odd number. "

                    $ tries += 1

            satella "All right... It's time for you to make a guess! Choose well!"

            $ r = 0

            while r == 0:

                $ r = renpy.input("Guess the total of Satella's dice{i}" + answers + "{/i}")

                python:
                    try:
                        r = int(r)

                        if r < 2 or r > 12:
                            renpy.say("", "Please choose a number between 2 and 12.")
                            r = 0

                    except:
                        renpy.say("", "Please choose a number between 2 and 12.")
                        r = 0

            if r == (d1 + d2):

                satella angry "What... No... That's impossible!"

                you "You better believe it... "

                extend "I won!" with vpunch

                "Satella looks defeated."

                satella "Aw... You're good..."

                satella happy "Well, a promise is a promise. I'll give you some old junk from my stack."

                call receive_item(get_rand_item(quality="common")) from _call_receive_item_6

                satella "Well, that was fun. Make sure to come back next time... This time I'll win!"

            else:

                you "I'm right! Right?"

                satella "..."

                you "Right...?"

                play sound s_evil_laugh

                satella "Muhaha..."

                satella "MUHAHAHAHAHA!" with vpunch

                you "Uh oh..."

                satella "YOU ARE WRONG! IT'S PUNISHMENT TIME!!! *maniacal laugh*"

                call satella_thunderbolt() from _call_satella_thunderbolt_1

    else:
        you "Isn't that game a little... Childish?"

        satella angry "Whaaaat???"

        "Tears well up in Satella's eyes. You've hurt her feelings."

        with vpunch
        with vpunch
        with vpunch
        play sound s_crash

        satella "It's not! It's not! I wanna play ROCK SCISSOR PAPER!!! Uwaaah!!!"

        you "All right, all right... Calm down..."

        satella happy "So, you will play? *happy*"

        you "I guess so... What are the stakes?"

        satella "Yay!!! Well, let's see... If you win, you can grab something from my stash of curious items."

        you "And if I lose?"

        play sound s_evil_laugh

        satella "If you lose? Well... You will suffer! Teeheehee..."

        you "*gulp*"

        satella "Ok, are you ready?"

        you "Well..."

        label satella_game_rock_menu():

            satella "Fine! Hands behind your back! One..."

            satella "Two..."

            satella "Threeeeee..."

            $ her_choice = rand_choice(("paper", "scissor", "rock"))

            menu:
                extend ""

                "布!":
                    $ r = "paper"

                "剪刀!":
                    $ r = "scissor"

                "石头!":
                    $ r = "rock"

            $ renpy.block_rollback()

            if r == her_choice:
                $ you(r.capitalize() + "!")
                $ satella(her_choice.capitalize() + "!")

                satella "Hey! That was my play..."

                you "Let's try again."

                jump satella_game_rock_menu

            elif (r, her_choice) in [("rock", "scissor"), ("scissor", "paper"), ("paper", "rock")]:

                if dice(6) >= 5: # Satella cheats

                    satella "..."

                    satella "THUNDER!!!" with vpunch

                    you "Uh?"

                    satella "THUNDER! Thunder burns the paper, cracks the rock and electrocutes the scissor-wielder. I WON!!!"

                    play sound s_evil_laugh

                    you "..."

                    you "There's no such thing as 'thunder' in this game. It's not called 'Rock scissor thunder' for a reason!"

                    play sound s_surprise

                    satella "What?"

                    you "You can't use thunder! It doesn't exist!"

                    satella angry "It does!"

                    you "It does not!"

                    satella "IT. DOES." with vpunch

                    you "IT. DOES. NOT... "

                    satella "GRRRR..."

                    play sound s_thunder

                    with vpunch

                    you "OUCH!"

                    call satella_thunderbolt() from _call_satella_thunderbolt_2

                else:
                    $ you(r.capitalize() + "!")
                    $ satella(her_choice.capitalize() + "!")

                    satella "I WON!!! WOOHOO!!!"

                    you "Err... No, you lost."

                    play sound s_surprise

                    satella angry "I... I lost?"

                    you "Yep."

                    satella "Aw... You beat me... You're a meanie..."

                    you "Don't be a sore loser. Cough up the item."

                    satella "All right... Take this, then... *sad*"

                    call receive_item(get_rand_item(quality="common")) from _call_receive_item_7

                    satella happy "Well, that was fun. Make sure to come back next time... This time I'll win!"

            else:
                $ you(r.capitalize() + "!")
                $ satella(her_choice.capitalize() + "!")

                satella "I WON!!! WOOHOO!!!"

                you "No, you... Oh, damn. You did."

                play sound s_evil_laugh

                satella "BWAHAHAHA! You lost! You lost! You lost!"

                you "Yeah, all right... I get it..."

                satella "YOU MUST BE PUNISHED!!!" with vpunch

                you "I, uh... I... M-must I?"

                satella "YES! It's PUNISHMENT TIME!"

                you "No, wait, I... AAAAH!!!"

                call satella_thunderbolt() from _call_satella_thunderbolt_3

    return

label satella_thunderbolt():

    stop music fadeout 3.0

    play sound s_crash

    scene black with fade
    show bg satella casting with dissolve

    "Oh no! Satella is getting ready to cast a nasty spell."

    show bg satella casting at quake

    $ reaction = False

    if MC.get_items(name="Lightning Rod") or MC.get_spirit() > 5:
        menu:
            "使用避雷针" if MC.get_items(name="Lightning Rod"):
                you "I knew this day would come... {i}Lightning rod{/i}! Lend me your power!"

                "Holding the lightning rod by the rubbery part, you brandish it as Satella completes her casting."

                $ reaction = True

            "使用反击咒语" if MC.get_spirit() > 5:
                $ r = MC.get_spirit() + dice(6)

                if r >= 10:
                    you "{i}Magic mirror{/i}!"

                    "Right as Satella is casting her spell, a reflective mirror forms around you, making you immune to magic bolts."

                    $ reaction = True

                else:
                    you "You are not getting me this time! {i}Metal Skin{/i}!!!"

                    "You cast a spell that makes your body as hard as dwarf-forged durasteel."

                    "Unfortunately, you forgot -again- that metal is conductive to electricity. You really shouldn't have skipped all those physics classes."

            "坐以待毙":
                pass

    $ renpy.block_rollback()

    with flash
    play sound s_thunder

    pause 0.3

    with flash
    play sound2 s_thunder
    pause 0.1
    with flash
    play sound3 s_thunder

    scene black with dissolve

    "A wave of magical energy radiates from Satella's body, and pink light bolts form in the air, aiming right at you."

    if reaction:

        play sound s_spell

        pause 0.5

        play sound2 s_scream

        satella "EEK!" with vpunch

        with doubleflash

        "You deflect Satella's thunderbolts and send them right back to her. She screams as her body is rocked by high-voltage magical electricity."

        call satella_lost() from _call_satella_lost

    else:

        play sound3 s_thunder
        with flash

        play sound s_punch
        with vpunch
        pause 0.3
        play sound2 s_punch
        with vpunch
        pause 0.2
        play sound3 s_punch
        with vpunch
        pause 0.1
        play sound s_punch
        with vpunch

        "You are hit by a salvo of magic projectiles, sending you flying into the air, then crashing and rolling around the center aisle of the temple."

        play sound s_wscream

        you "AAAAAH!!!" with vpunch

        play sound s_evil_laugh

        satella "Muhahahaha!"

        you "Aaargh... You crazy b..."

        call satella_won() from _call_satella_won

    return

label satella_won():

    scene black
    show bg satella sit1
    with fade

    "Satella is sitting on top of you, looking triumphant."

    satella "Hahahaha... My magic bolts were like *pew* *pew*, and you were like *aw*, *ouch*, *not my face*, it was so cool!"

    you "Ouch... Arrgh..."

    satella "You're not dead though! I'm glad. That means we can do this again!"

    you "*sob*"

    satella "Pay your respects to the Night Mistress! You're like, my bitch now!"

    you "You're crushing me... Also, language..."

    play sound s_evil_laugh
    satella "Muhahaha..."

    if NPC_satella.love >= 10:
        "You decide to fight back, the only way you know how."

        show bg satella sit2 with dissolve

        play sound s_surprise

        satella angry "Aah!"

        "You grab Satella's thighs, sinking your trembling fingers into her young flesh."

        satella "What... What are you doing!"

        "Satella's skin is still crackling with magical energy, making her especially sensitive."

        satella "S-Stop..."

        "Pushing your advantage, you start fondling her thigh, inching up towards her panties."

        satella "You're... Making me feel weird... Stop..."

        if NPC_satella.love >= 25:

            "Before she has a chance to gather her thoughts, you use your other hand to grab her ass."

            show bg satella sit3 with dissolve

            play sound s_surprise

            satella "Ahaaa! My butt!!!"

            "It seems her butt is especially sensitive. She moans as you start pinching her buttcheek."

            play sound s_ahaa

            satella "N-no... Stop..."

            "You have the upper hand now. Your left hand creeps towards her sensitive spot, rubbing the fabric of her panties."

            play sound s_aaah

            satella "Aaah! Aaaaah!!!"

            "Being super-sensitive because of the magical current coursing through her, Satella is defenseless before your assault."

            satella "Ngh... Nghhh..."

            "You rub the surface of her panties with your finger, feeling the mound of her clit and her wet slit through the thin fabric."

            play sound s_scream

            satella "Aaah!!! Not there!!!"

            with flash

            play sound s_scream_loud

            satella "WHAT'S THIS... AAAAAAH!!!"

            play sound s_orgasm_young

            with doubleflash

            "As you squeeze Satella's butt, sliding your fingers inside her panties, it gets too much for her, and she cums unexpectedly."

            satella "Aw, aaah... What's this... I've never..."

            you "This is nothing... I'll teach you another kind of 'game'."

            play sound s_surprise

            satella "Oh?"

            "You recover surprisingly fast from the beating you just took. Satella is too light-headed to resist you as you push her on the ground."

            if NPC_satella.love == 25:
                call satella_virgin_sex() from _call_satella_virgin_sex

            else:
                call satella_sex() from _call_satella_sex

        else:
            $ NPC_satella.love = 25

            if MC.god == "莎莉娅" and not story_flags["shalia3"]:
                $ calendar.set_alarm(calendar.time+1, StoryEvent(label = "shalia3", type = "morning"))

            you "Come on, it's just a little massage... Let yourself go..."

            play sound s_mmmh

            satella "Be... Gentle... Aaaah... [emo_heart]"

            satella "..."

            satella "(What... What am I doing?)"

            satella "What... The..."

            satella "Fuck!"

            show bg sit2 at quake

            you "Uh oh."

            "Satella opens her eyes, and they are red with fury."

            satella "UWAAAAH!!! *enraged*"

            you "Aaaaah!!! Wait, that was just a..."

            with flash

            play sound s_thunder

            you "OUCH!"

            with doubleflash

            play sound s_thunder

            pause 0.3

            play sound2 s_thunder

            scene black with fade

            play sound s_thunder

            pause 0.2

            play sound2 s_thunder

            pause 0.3

            play sound2 s_thunder

            pause 0.2

            play sound s_thunder

            "Satella makes you pay dearly for your boldness."

            "When she finally lets you go, you crawl outside and pass out. When you come back to your senses, it is almost dawn, and a stray dog is gnawing at your boot."

            $ MC.interactions = 0

            "You have lost all of your remaining actions for the day."

    else:
        "You feel wretched as Satella taunts and torments you. After a while, she gets tired of it, and you crawl out of the temple to nurse your wounds."

        $ NPC_satella.love = 10
        $ MC.interactions = 0

        scene black with fade

        "You have lost all of your remaining actions for the day."

    return

label satella_lost():

    stop music fadeout 3.0

    scene black
    show bg satella stunned1
    with fade

    "Overwhelmed by the magical backlash, Satella falls down on the dusty floor, her body crackling with dark electricity."

    satella angry "Aw... What happened..."

    show bg satella stunned2 with dissolve

    you "Bwahahaha..."

    satella "Wait... What... What do you..."

    "Satella is defenseless as you loom above her. You decide it's time to teach her a lesson."

    play sound s_thunder

    with vpunch

    show bg satella stunned3 with dissolve

    "Using the element of surprise, you poke Satella's ass, hard."

    play sound s_scream_loud

    satella "Ha!!!" with vpunch

    "Because Satella's body is saturated with magic, she is feeling especially sensitive."

    satella "You can't... Ha!!!"

    "Ignoring her complaints, you continue poking her ass, burying your finger deeper into the flesh of her exposed buttock. She moans, unable to move."

    you "Hmm... That young girl's ass is juicy..."

    show bg satella stunned4 with dissolve

    "Grabbing Satella's ass, you start kneading it, rubbing your fingers against her exposed skin. Crackling electricity bursts from her sensitive body."

    play sound s_scream_loud

    satella "Aaah!!! It's too much! Stop!"

    play sound s_ahaa

    "Even though she complains, she is clearly feeling it, blushing bright red as she shakes her little butt weakly in a futile attempt to escape you."

    you "Let you go, uh..."

    "After squeezing her butt hard, you let go."

    show bg satella stunned5 with dissolve

    play sound s_scream

    satella "Aw... *pant* *pant*"

    play sound s_punch
    show bg satella stunned6 with vpunch

    you "Surprise!"

    "You grab Satella's ass again, this time rubbing your fingers over her pussy as well. She is in shock."

    play sound s_screams

    satella "AAAAH! NO! Let me go, aaaaaah..."

    play sound s_moans

    "Satella is in full sensory overload as you play with her magic-infused body, roughing up her sensitive parts."

    satella "Aaaaah... What's... What's happening to meeeee..."

    with flash

    play sound s_scream_loud

    satella "AAAAAAAH!!!"

    play sound s_orgasm_young

    show bg satella stunned7 with doubleflash

    "You reach for Satella's small boobs, squeezing one of her tits. This is too much for her and she cums hard, wetting her panties and shaking like she's having a fit."

    satella "Aaaah... Ooooh..."

    "Satella's mind seems almost gone as she struggles to contain the spasms from her magically-enhanced orgasm."

    you "Wow, girl, looks like you had fun..."

    satella "Arrh..."

    if NPC_satella.love < 25:
        $ NPC_satella.love = 25

        if MC.god == "莎莉娅" and not story_flags["shalia3"]:
            $ calendar.set_alarm(calendar.time+1, StoryEvent(label = "shalia3", type = "morning"))

        "You feel like you have come a bit too far already. You leave before Satella has a chance to recover and fry your balls."

        scene black with fade

    else:

        you "Now, it's my turn..."

        "You point at your trousers. There's a big bulge at the level of your crotch."

        satella "*gasp*"

        if NPC_satella.love == 25:
            call satella_virgin_sex() from _call_satella_virgin_sex_1
        else:
            call satella_sex() from _call_satella_sex_1

    return


label satella_virgin_sex():

    $ NPC_satella.love = 50

    show bg satella sex1_1 with dissolve

    satella angry "Aw... Wait..."

    "Wasting no time, you pull down her brassiere, revealing her small but firm breasts."

    play sound s_scream

    satella "Eek!"

    "Satella's eyes widen as you take out your cock from your pants. She blushes bright red."

    satella naked "What... Is that a man's... Oh!"

    "Sliding her leather suit aside, you reveal her wet pussy, placing your cock against it."

    play sound s_ahaa

    satella "Ah! It tickles! Aaah!!!"

    you "You are still nice and wet... I think we can dispense with the preliminaries..."

    satella "Wait, what do you... *blush*"

    play sound s_scream_loud

    show bg satella sex1_2 with dissolve

    satella "No way! It's going inside... Aaaah!" with hpunch

    "Satella's eyes widen with shock as you push your hard cock inside her tight, moist pussy."

    satella "Ow!!!"

    "You meet with some resistance, and you feel her hymen break as you push your cock further inside."

    satella "It's painful... Stop..." with hpunch

    you "Wow... I took the Night Mistress's virginity!"

    "You wonder how much suffering Satella would impose on you if she went back to her usual self. However, you're too far gone now,
    so you have to make the most of it."

    satella "Aaah, aaah..." with hpunch

    satella "I feel so strange... Aaah... I've never felt this before..."

    "Although Satella's young pussy is very tight, she is soaking herself with love juice, helping your cock slide in and out with ease."

    play sound s_moans

    satella "Aaaah... Aaaah..." with hpunch

    "Satella's body is still infused with dark magic, producing a nice tickling sensation for you both, as you fuck her virgin pussy faster and faster."

    satella "It's burning... Inside... Me... Aaaah..." with hpunch

    "Surprisingly for such a frail girl, she is still able to accommodate your cock whole now, grinding her teeth as she gets lost in the feeling of having sex for the first time."

    satella "It's so big... It's ruining my pussy... Aaaaaah!!!" with hpunch

    play sound s_scream_loud

    with flash

    "Her tight cunt squeezes your cock hard, and you cannot resist anymore. You shoot a load of cum deep inside her virgin pussy."

    play sound s_orgasm_young

    show bg satella sex1_3
    with doubleflash

    "She cries with pleasure as she feels the hot cum pour inside her."

    satella "Aaaah... *drool*"

    $ unlock_achievement("h satella")

    "The new feelings were too intense for Satella, and she completely passes out on the floor, warm cum and love juice gushing out of her with obscene, wet sounds."

    "You feel it is more prudent to leave quickly, before she comes back to her senses."

    scene black with fade

    $ MC.change_prestige(2)

    "You have earned prestige."

    if MC.god == "莎莉娅":
        $ calendar.set_alarm(calendar.time+1, StoryEvent(label = "shalia4", type = "morning"))

    $ NPC_satella.unlock_trainer()

    return


label satella_sex():

    $ NPC_satella.love = 75

    show bg satella sex2_1 with dissolve

    "Emboldened by Satella's weakness, you tug at her kinky leather suit, exposing her naked pussy and breasts."

    play sound s_scream

    satella naked "Ah!!!"

    you "I like that you wear no bra... You're such a perverted young girl..."

    satella "Don't... Don't say that..."

    you "Did you really forget the last time we had fun together? I'm disappointed..."

    "Taking out your cock, you start grinding it against her panties."

    play sound s_surprise

    satella "Eeeek!!! Gross!!! Get that off me!"

    you "Why? We're only getting started..."

    "Rubbing against her, you can feel her underwear become wet with her love juice."

    you "Wow... Your body is very sensitive... No wonder you pass out easily when having sex..."

    play sound s_aah

    satella "I don't... know what you mean... Aaaah..."

    show bg satella sex2_2 with dissolve

    play sound s_scream_loud

    satella "Aaah!" with hpunch

    "Her erotic moans are enough to make you rock-hard. Unable to wait any longer, you rip her panties off, plunging your cock deep into Satella's tight vagina."

    show bg satella sex2_3 with dissolve

    play sound s_moans

    satella "Nooo... Aaaah..." with hpunch

    "In spite of her weak complaints, Satella's pussy welcomes your cock, gushing out love juice as you slide in and out of her."

    you "You're so nice and tight... Hmmm..."

    satella "No, please... You're making me feel weird... Aaaaah..."

    play sound s_scream_loud

    satella "AAAAH!!!" with hpunch

    show bg satella sex2_2 with dissolve

    "Satella cries out as you increase your pace, giving her a serious pounding. Nevertheless, she moans with pleasure rather than pain, her wet pussy hungry for more."

    satella "Stop it! I'm losing my mind... Stop it... Aaaahaaaaah... What's... What's happening to meeeee..."

    with flash

    play sound s_screams

    satella "AAAAAH! AHAAAAH!!!"

    show bg satella sex2_4 with doubleflash

    play sound s_orgasm_young

    "Satella cums hard as you shoot your load deep inside her, filling up her insides with hot cum."

    satella "Ooooh! I feel so... Aaaah... AAAAH!"

    show bg satella sex2_5 with flash

    play sound s_screams

    "As you pop your dick out and shoot the rest of your load all over her petite body, Satella has another loud orgasm, before falling back on the floor and passing out."

    you "Phew... What a rollercoaster..."

    you "I better clean up and go home before she comes back to her senses."

    scene black with fade

    $ MC.change_prestige(2)

    "You have earned prestige."

    if MC.god == "莎莉娅":
        $ calendar.set_alarm(calendar.time+3, StoryEvent(label = "shalia_visit", type = "morning"))

    return


## SHALIA EVENTS ##

label shalia1(): # Happens in the morning after meeting Satella in Chapter 1. All the Shalia events will only happen if the player worships Shalia.

    stop music fadeout 3.0

    scene black with fade

    "As you fall into a deep sleep, a peculiar dream comes to you."

    play sound s_chimes

    show bg stars at top with fade

    play music m_shalia

    "Voice" "[MC.name]... *whisper*"

    you "..."

    "Voice" "[MC.name]... *eery whisper*"

    you "Who's... Who's there?"

    play sound s_spell
    with doubleflash

    show shalia5 with dissolve

    $ shalia_name = "Strange woman"

    shalia "Welcome, my child."

    you "..."

    you "Mom?!?" with vpunch

    you "Wow... You're younger and cuter than I remembered..."

    shalia "Don't be silly."

    shalia "I am not your mother, although I do know her dirtiest secrets..."

    you "What... Ew."

    you "Who... Who are you, then? Why are you in my dreams?"

    shalia "Don't you know me? I am one with the shadows..."

    scene black
    show bg shalia1
    with fade

    you "You are..."

    you "Sh..."

    you "Shalia!" with vpunch

    $ shalia_name = "莎莉娅"

    "She is the Goddess herself. You are awestruck. You try to bow or take a knee, only to fail embarrassingly, as you are just a disembodied spirit floating in space."

    you "Lady Shalia, I apologize wholeheartedly... I didn't know..."

    play sound s_laugh

    "Shalia laughs. Her laugh is surprisingly girly and sweet for a dark goddess."

    shalia "Most of my followers won't recognize me. This is a useful trick for the Goddess of mischief."

    "Shalia doesn't look at all like what you imagined reading the scriptures as a kid. She is a lot less threatening, with a bookish look about her."

    shalia "I know what you're thinking... The Goddess looks pretty harmless, right?"

    shalia "Well... Looks can be deceiving... *frown*"

    "You wonder if that was a threat."

    you "*gulp*"

    shalia "But the truth is, I {i}am{/i} quite easygoing. *smile*"

    you "But... What about the darkness... The plots... The assassinations..."

    shalia "I have no interest in violence. It is a crude instrument best left to the simple-minded, the followers of the serious boring gods, like Arios."

    shalia "Violence is the last resort, and there are other ways. I favor the smart and witty. Are you smart and witty?"

    you "Uh, I, er..."

    shalia "Well... One cannot just pick and choose her followers. Anyway."

    you "B-But... Why me? Why do you visit me now?"

    shalia "Oh, that."

    shalia "I didn't do it on purpose, you see. We must have had some kind of connection. Have you perhaps met one of my avatars?"

    you "The... The Night Mistress! Satella!"

    shalia "Right! That must be it. You must have somehow struck her fancy, because she's thinking about you now. That's why you can see me."

    you "Lady Shalia, I am honored, I don't know what to say..."

    shalia "Well, it is best to shut up then."

    you "..."

    shalia "I will leave you with a piece of advice, follower."

    shalia "Appearances can be deceiving. Do not forget that as you navigate the politics of Zan."

    you "..."

    play sound s_spell

    scene black with fade

    "You wake up abruptly, covered in a sweat. A ray of light is coming through your window: it is morning already."

    return

label shalia2: # Happens in the morning the day after Satella's first 'game night'

    stop music fadeout 3.0

    scene black with fade

    "You spend the night dreaming feverishly about long-forgotten realms and battlefields, feeling yourself struggle against unspeakable entities."

    "As you enter another mysterious place sinking into pitch black darkness, a feeling of calm and contemplation overcomes your anxiety."

    play sound s_chimes
    show bg stars at top with fade

    you "(Where... Where am I?)"

    you "(I know this place...)"

    play sound s_laugh

    show shalia2 with dissolve

    shalia "Hahaha... [MC.name]... We meet again."

    you "Sh... Shalia?"

    "The Goddess is standing before you. Something odd is happening, however... It seems she is missing the top of her dress!"

    you "*gulp*"

    shalia "What? Even as in your ethereal form, I can feel you staring. Have I got something on my nose?"

    you "L-Lady Shalia... Your dress... Ahem..."

    play sound s_surprise

    show bg shalia2 with fade

    shalia "Oh! Am I missing a clothing item? How embarrassing..."

    shalia "It must be my wicked little Satella. She feels more comfortable around you now, and she is lowering her guard."

    shalia "Oh well. We gods are well above petty human feelings like shame and self-consciousness."

    shalia "But I guess you're lucky to get to see your Goddess in a sexy attire..."

    you "My Lady, I... *gulp*"

    shalia "Even the mightiest have their weakness... Remember this lesson. It will open the door to many an opportunity."

    shalia "I'll see you around, follower... Dawn is coming."

    play sound s_spell

    scene black with fade

    "Shalia's image blurs into darkness, and you open your eyes, waking up. You are not likely to forget this sight."

    return

label shalia3(): # Happens in the morning the day after Satella's love reaches 25

    scene black with fade

    "You are sleeping a dreamless sleep, when a crystal-like voice starts echoing inside your head."

    play sound s_laugh

    "Voice" "Teeheehee..."

    play sound s_chimes

    show bg stars at top with fade

    shalia "So... You like this guy?"

    shalia "Come on, you can tell me. It will be our secret..."

    shalia "Aw, you're impossible..."

    shalia "Hush, someone is coming. I'll get back to you."

    play sound s_spell

    show shalia3 with dissolve

    shalia "Ah, [MC.name]. I've been expecting you."

    you "You... You have?"

    shalia "Why, yes. I know you've been playing Satella's little games... She's my avatar, remember? What she sees, I see."

    you "I... I see..."

    shalia "You look confused. Why is that?"

    you "Well, uh..."

    you "Your dress... *blush* You're not... Wearing any..."

    show bg shalia3 with fade

    shalia "Oh, that again? Unbelievable... Satella must be feeling pretty close to you now."

    shalia "That's rare. Actually, that's never happened. You must be special."

    you "Hem... Thanks..."

    you "Lady Shalia... One question, if I may."

    shalia "You may, follower, you may."

    you "Why did you choose Satella to be your night mistress? You are like... Polar opposites!"

    play sound s_laugh

    shalia "Hahaha... That's what you think, maybe. Women are complicated, goddesses even more so..."

    shalia "But Satella is my daughter. So, we have more in common than you realize..."

    shalia "Did I tell you the story of Satella?"

    you "Satella? No..."

    scene black
    show bg stars at top
    with fade

    show shalia3 with dissolve

    shalia "I have many avatars, and they are all my daughters, but Satella is special."

    shalia "Satella was born to no man. She was sired by a dragon."

    you "*gasp* A dragon?"

    if MC.playerclass == "奸商":
        shalia "Yes, a dragon. Not a common worm like your pet Drogon, no offense, but one of the old ones. One of the oldest. Axiom was his name."
    else:
        shalia "Yes, one of the oldest, born before the continents spread apart. Axiom was his name."

    menu:
        extend ""

        "史黛拉是龙的后裔?":
            you "A human, born from a dragon?"

            shalia "Not a human, not quite... But the old dragons were shapeshifters. There's a lot more to that story."

            shalia "Suffice to say that Satella grew up without a mother."

        "等等，你上了一头龙?":
            you "Wait a minute... Satella is your daughter..."

            you "You... You had sex with a dragon?!?" with vpunch

            play sound s_surprise

            shalia "Hey! *frown*"

            shalia "This is none of your business."

            shalia "Let us just say that Satella had to grow up without a mother."

    shalia "Although Axiom was protecting our daughter fiercely, he was not much for conversation, or parenting."

    shalia "Satella grew up alone, making friends with spirits, demons and the occasional inanimate object. That's why she has some... Rough edges."

    you "I've noticed that."

    shalia "During this time, she was sweet and innocent as can be. Alas, it wasn't meant to stay that way."

    shalia "Axiom's reputation and treasure attracted dragonslayers from all realms, eager to conquer the beast."

    shalia "One fateful day, a small gang of greedy adventurers finally slaughtered the old dragon in his sleep..."

    scene black
    show bg satella dragon
    with fade

    shalia "Only to find a little girl instead of a treasure."

    shalia "A very pissed little girl... And a night mistress at that."

    you "Oh."

    shalia "No one saw the adventurers again. Satella remained there for some time, protecting her father's remains."

    shalia "But new rogues kept coming, lured by the promise of treasure."

    scene black
    show bg stars at top
    show shalia3
    with dissolve

    shalia "So, I took Satella away, guiding her somewhere safe."

    you "In Zan? Safe?"

    shalia "Yes. It is easier to hide among the many, than the few. Let this be your lesson for today."

    play sound s_spell
    scene black with fade

    you "Wait..."

    "Shalia's image fades into the darkness, and you open your eyes. Sunlight is beaming through the window."

    return

label shalia4(): # Happens in the morning the day after Satella's love reaches 50 (virgin sex)

    "Your sleep is restless tonight. You see the faces and bodies of all the women you slept with, whizzing past you into a blur. One of them stays with you, though. A young woman with fiery hair."

    you "..."

    show bg stars at top with fade

    "A dark silhouette comes up, against a starry background. It feels familiar."

    play sound s_chimes

    you "Satella..."

    show shalia4 with dissolve

    "Shalia appears before you, wearing no clothes. She stares at you in silence."

    you "Shalia?"

    "You try to pinch yourself to check if you're dreaming, fail to do so, then remember: you {i}are{/i} dreaming."

    shalia "Welcome, follower. We meet again."

    you "You... You're..."


    shalia "Naked? Yes, it appears so. I take it your relationship with Satella has reached an unprecedented level, then?"

    "Her eyes narrow."

    shalia "You have {i}tricked{/i} my sweet, innocent Satella into having sex with you, have you not? *frown*"

    you "I, er... I can explain..."

    play sound s_evil_laugh

    "Shalia laughs before flashing you a radiant smile."

    shalia "Oh, please, cut it off. It was brilliant, really! I am the Goddess of tricks and traps. I love your cunning, follower."

    you "You... You're not mad?"

    shalia "Why would I be? You got what you wanted, and in a way, so did she. Satella couldn't remain a child her whole life..."

    shalia "I knew a lover would come into the picture sooner or later. I didn't expect it to be you. That was bold, follower, bold."

    you "Well... Thanks?"

    shalia "Anyway, it is time for me to impart some words of wisdom to you..."

    show bg shalia4 with fade

    play sound s_aaah

    shalia "Aaaah..."

    you "Aaah? Is that a place?"

    play sound s_ahaa

    shalia "Listen, I, uh, aaaah..."

    you "I beg your pardon?"

    shalia "You, ngh... You must not... Nggh..."

    play sound s_mmh

    "Shalia's face becomes flushed, and her nipples erect. You can see her godly pussy glistening with something."

    shalia "Oh no... Satella... What are you doing... You bad girl..."

    play sound s_moans_quiet

    "You watch with astonishment as the Goddess struggles to maintain her composure, moaning softly."

    play sound s_surprise

    shalia "Aaah!!! Not there! Oh, Satella, you're so naughty   ..."

    play sound s_scream
    with flash

    shalia "Ooooh, aah, aaaah..."

    with doubleflash

    play sound s_screams

    shalia "AAAH!!!"
    play sound s_orgasm

    "Speechless, you see the goddess's body being rocked back and forth wildly by invisible forces, before cumming with a cry."

    "Shalia takes a while to recover from the waves of pleasure. Eventually, she calms down, and turns back towards you."

    scene black
    show bg stars at top
    show shalia4
    with fade

    shalia "I apologize, follower. It seems Satella was... enjoying herself, while thinking about you. You have made quite the impression on her."

    you "Wow..."

    shalia "I told you I get to experience everything my avatars go through. And I mean, {i}everything{/i}."

    shalia "There is something important I wanted to tell you. You must not tr..."

    play sound s_spell
    scene black with fade

    "Before Shalia can finish her sentence, however, light flushes out the darkness, and you find yourself awake in your bed, with an embarrassingly large hard-on."

    return

label shalia_visit(): # Happens in the morning a week after Satella's love reaches 75 (second sex). After this event, game night invitations will stop being sent

    "After a long night, as the last customers are leaving the brothel, you get back to your room to get some hard-earned sleep."

    scene black
    show bg master room at top
    with fade

    you "Phew... I'm quite tired. Time to hit the..."

    play sound s_mystery

    you "Uh? Who's there?"

    play sound s_mystery

    "A petite silhouette is standing in the shadows of your room."

    you "S-Satella?"

    play sound s_laugh

    show shalia with dissolve

    "The woman steps out of the shadows. From your dreams, you recognize the Goddess Shalia, standing right here in the flesh."

    shalia "It's me, silly."

    you "Lady Shalia!"

    "Awestruck, you drop to your knees. The sharp pain as your kneecaps hit the hardwood floor confirms that you are not dreaming this time."

    shalia "Rise, you idiot. You know I despise protocol and empty formalities."

    you "Ahem, you are here in the flesh, my Lady? Is this an illusion? Am i drunk? Did someone put spice in my beer?"

    hide shalia
    show satella_standing:
        xalign 0.45
        yalign 1.05
    with Dissolve(0.005)
    hide satella_standing
    show shalia
    with Dissolve(0.005)
    hide shalia
    show satella_standing:
        xalign 0.45
        yalign 1.05
    with Dissolve(0.005)
    hide satella_standing
    show shalia
    with Dissolve(0.005)

    you "Uh? Satella?"

    hide shalia
    show satella_standing:
        xalign 0.45
        yalign 1.05
    with Dissolve(0.005)
    hide satella_standing
    show shalia
    with Dissolve(0.005)
    hide shalia
    show satella_standing:
        xalign 0.45
        yalign 1.05
    with Dissolve(0.005)
    hide satella_standing
    show shalia
    with Dissolve(0.005)

    shalia "We have come to see you, yes. I am using Satella's body as a vessel."

    shalia "I thought it best to change her form to something more to my taste."

    shalia "I can hardly let a scantily-clad dragon girl with a temper loose in Zan at night, after all. The streets are dangerous enough as it is..."

    you "I... I am honored... To what do I owe the pleasure..."

    shalia "Oh, shut it already. We don't have time for that: the night is short, and we have much to do."

    you "We do?"

    shalia "Yes. Now, get naked."

    you "Uh?"

    shalia "Get naked, on the double!"

    you "I don't... understand..."

    play sound s_thunder

    hide shalia
    show satella_standing:
        xalign 0.45
        yalign 1.05
    with Dissolve(0.005)
    hide satella_standing
    show shalia
    with Dissolve(0.005)
    hide shalia
    show satella_standing:
        xalign 0.45
        yalign 1.05
    with Dissolve(0.005)
    hide satella_standing
    show shalia
    with Dissolve(0.005)

    shalia "GET YOUR FUCKING CLOTHES OFF! I command thee!" with vpunch

    "Shalia's voice booms, filling the air with dark vibrations. You dare not disobey."

    play sound s_dress

    you "S-Sure... Right away..."

    shalia "Sorry about that. When I take over Satella's body, some of her short temper rubs off on me, I'm afraid. *smile*"

    "You stand naked in front of your Goddess. She takes an appreciative look at your body, lowering her gaze from the top, until she pauses at the level of your crotch."

    shalia "Not bad, not bad..."

    "She bites her lip."

    play sound s_sigh

    shalia "I need you to be in top physical condition, though. Sit down."

    you "Okay..."

    "Sitting down, you stay there, exposed to Shalia's inquisitive gaze."

    play sound s_dress

    "Shalia sits down in front of you, muttering something in an unknown language."

    you "Why are you taking your shoes off... Ah!"

    show bg shalia fj1 with fade

    "Unexpectedly, Shalia brings her legs up, reaching for your cock with her feet."

    play sound s_mmmh

    shalia "Hmmm..."

    you "My... My Lady... What are you..."

    shalia "Hush! I need to concentrate."

    scene bg shalia fj2 with dissolve

    play sound s_ahaa

    "You gasp as Shalia starts rubbing her feet over your dick, a strange and magical tickling sensation radiating from her body."

    shalia "Since you are a mortal, I cannot touch you directly. This would suck out your soul, or some other unpleasant side-effect. But the stockings are just fine for our purpose."

    show bg shalia fj1 with dissolve

    you "It tickles... Aaah..."

    "Blood flows to your crotch, and soon your penis is hard and erect."

    play sound s_sucking

    shalia "Nice. The magic is working..."

    show bg shalia fj2 with dissolve

    "Shalia increases her pace, using her toes to stimulate your cock's head with surprising agility. Her technique is faultless, true to her godly nature."

    you "Aaaah... My Lady, I can't..."

    shalia "Hush, child... The incantation is almost over..."

    show bg shalia fj1 with dissolve

    "The influx of magic from Shalia's feet intensifies, entering your body throughout your sensitive cock. It feels amazing, and gradually your energy gets restored to the maximum."

    shalia "Yes... I can feel the energy building up."

    "Your eyes widen as you see your cock starting to expand beyond its natural size, your balls inflating until it hurts."

    you "What's... going on..."

    show bg shalia fj2 with dissolve

    "Shalia wraps one foot behind your cock, caressing the tip with her toes, while using her other foot to rub the front of your cock harder and faster."

    you "Ugh... Wait... My cock is going to explode..."

    "You feel your cock is about to burst. Your mind is filled with lust, and you cry like an animal as Shalia massages your cock expertly with her godly feet."

    play sound s_wscream

    show bg shalia fj3 with flash

    you "AAAAAAHHH!!!"

    "Your cock is almost double its normal size now, and suddenly you start cumming hard, shooting a huge wad of cum from your inflated balls all over your Goddess."

    play sound s_aaah

    show bg shalia fj4 with doubleflash

    "Shalia sighs contendedly as she keeps massaging your cock, helping you release all of your built-up semen."

    shalia "Nice... Wow, you really messed this body up... There's even some on my breasts."

    shalia "Maybe I went a little overboard... It isn't the time to waste all of your newfound energy."

    you "Oooh..."

    "Even though you came an incredible amount, smearing Shalia's body and covering the floor with your gooey semen, you watch in amazement as your cock starts growing erect again."

    "Your balls fill up as well, and soon you feel hyper sensitive and about to burst."

    shalia "Well, you are recovering nicely. Let us not waste this opportunity. Come."

    play sound s_spell

    scene black with fade
    show shalia with dissolve

    "Shalia snaps her fingers, and everything goes dark around you both."

    you "Where... are we...?"

    play sound s_spell

    show bg stars at top behind shalia with fade

    shalia "I am taking you to a special place. Only a few mortals have ever visited this place, none of them alive."

    shalia "This is an immense privilege, follower."

    play sound s_spell

    show bg other dimension behind shalia with fade
    "The stars blink and fade around you, and suddenly you find yourself standing in the middle of a mysterious clearing. The lights and flora look totally alien to your world."

    you "Wow... Where is this?"

    shalia "We are entering the Nether... Realm of the gods. This is the place I call home."

    hide shalia

    "You look around you in complete amazement. You are standing there with your own mortal body, breathing the air and stomping the grass of another dimension."

    if MC.playerclass == "战士":
        you "This is unnatural... I must be dreaming..."
    elif MC.playerclass == "法师":
        you "Fascinating... I only read about that place in books..."
    elif MC.playerclass == "奸商":
        you "Wow... No one is going to believe {i}that{/i} tale."

    play sound s_spell

    show shalia6
    with dissolve

    shalia "We have arrived. We must now discuss our next course of action."

    you "Why are you... What do you need me to..."

    shalia "Not you."

    hide shalia6
    show satella naked:
        xalign 0.55
        yalign 0.7
    with Dissolve(0.005)
    hide satella naked
    show shalia6
    with Dissolve(0.005)
    hide shalia6
    show satella naked:
        xalign 0.55
        yalign 0.7
    with Dissolve(0.005)
    hide satella naked
    show shalia6
    with Dissolve(0.005)

    play sound s_chimes

    you "What?"

    hide shalia6
    show satella naked:
        xalign 0.55
        yalign 0.7
    with Dissolve(0.005)
    hide satella naked
    show shalia6
    with Dissolve(0.005)
    hide shalia6
    show satella naked:
        xalign 0.55
        yalign 0.7
    with Dissolve(0.005)
    hide satella naked
    show shalia6
    with Dissolve(0.005)

    play sound s_spell

    show satella naked behind shalia6 with flash

    show shalia6 at left:
        xoffset -0.3*config.screen_width
    show satella naked at left:
        xoffset +0.3*config.screen_width
    with move

    "Shalia's image blurs for a second, and a bright light forces you to close your eyes. When you open them again, Satella is standing beside you."

    play sound s_surprise

    satella "Uh?"

    satella "Where am I... [MC.name]? Mother? Why are you naked... Why am I naked?!?"

    shalia "Satella, my child. It is time."

    shalia "I have brought you a suitor. I chose [MC.name]."

    play sound s_surprise

    satella "[MC.name]? *blush*"

    "Satella looks at your naked body, blushing."

    shalia "But wait, daughter. It is your choice and yours alone. Will you have [MC.name]?"

    shalia "I can bring you anyone else, just say the word."

    satella "I see... *blush*"

    "Satella smiles."

    satella "[MC.name]... I am happy with your choice, Mother. I'm ready. *shy smile*"

    satella "[MC.name]?"

    you "Yes?"

    satella "I want you to father my child."

    you "You... What???" with vpunch

    shalia "This is how new night mistresses are born. I choose suitable mates for my daughters, in order to impregnate them, and father my children."

    you "Wait... Me? A father?"

    shalia "I am one with my avatars. Sex with Satella is like having sex with me, a Goddess. Your seed will sire a godly child. It is a great honor I bestow upon you."

    "You look at Shalia's enigmatic face with awe."

    you "I... I don't know what to say."

    shalia "Do not say anything, then. We have had enough talk already."

    shalia "Satella, I present you with my gift: a strong partner, to impregnate you with my next child."

    satella "Mother, I accept it gladly."

    shalia "Follower, you may now fuck my daughter."

    shalia "I will feel everything she feels. Make me proud."

    you "..."

    scene black with fade
    show bg satella sex3_1 at top with dissolve

    "You pull Satella against you. She doesn't resist, and hugs you shyly."

    "Your cock is massive, still infused with magical energy. Satella sits on it, her pussy grinding against the length of your shaft."

    play sound s_surprise

    satella naked "Ha, aaah..."

    "You can feel her pussy pressing against your cock, already very wet. Her body is incredibly sensitive."

    play sound s_mmmh

    shalia "Mmmh..."

    satella "Mother..."

    satella "I can't... [MC.name] is too big..."

    shalia "Trust me, daughter, he is just the perfect size for you. I'm your mother, I know what's best."

    play sound s_ahaa

    satella "Ahaa..." with hpunch

    "You keep grinding back and forth against satella's clit and pussy, releasing more and more of her love juice, until your dick is well lubricated."

    you "Here I come..."

    satella "Wait, aah..."

    play sound s_scream_loud

    show bg satella sex3_2 at top with dissolve

    satella "AAAAH!" with hpunch

    "You lift Satella's hips into the air, landing her straight on your erect cock. Your shaft enters her easily, reaching her deepest parts."

    satella "Ah, aaah..."

    shalia "Mmmmh... Aaaah..."

    "Shalia leans back against one of the tree-like crystals that litter the place, the Goddess's body feeling the heat as you start fucking Satella."

    play sound s_moans

    satella "Ah... It's so big... Aaaaah..."

    you "Are you all right?"

    satella "..."

    satella "Yes. Continue..."

    show bg satella sex3_3 at top with dissolve

    "Being careful not to hurt Satella with your extra-large cock, you start pulling her soft butt up and down, sliding your cock back and forth inside her tight pussy."

    satella "Oooh... Aaaah..." with hpunch

    "Shalia is moaning too, feeling every thrust as you fuck Satella."

    shalia "Mmh... Ngh..."

    "Feeling the magical energy course through your body, you can barely contain your lust."

    satella "Aah, aaah... It's so deep..." with hpunch

    shalia "Faster! Faster!"

    play sound s_scream_loud

    show bg satella sex3_2 at top with dissolve

    satella "AAAH!" with hpunch

    "Unable to resist the urge, you start fucking Satella like a wild animal, messing up her insides as you impale her harder and harder on your rock-hard cock.."

    play sound s_moans

    shalia "Aaaaah! Yes!"

    satella "Oooh, aaah, aaaaaaaah..." with hpunch

    show bg satella sex3_4 at top with dissolve

    "Even though you are fucking her mercilessly, Satella seems to be taking it in stride, panting and moaning as you push your cock deep inside her petite body."

    satella "It's so good... Aaah... *drool*" with hpunch

    shalia "Oh, yes... Oh, yessss..."

    with flash

    play sound s_screams

    satella "AAAAAAAAH!!!"

    show bg satella sex3_5 with doubleflash

    "You cum like a volcano, filling Satella's pussy to the brim with burning cum."

    satella "So much... Seed... AAAAAAH!!!"

    play sound s_orgasm_young
    with flash

    "Feeling your hot cum pouring deep inside her and impregnating her, Satella cums as well, screaming."

    shalia "Aaah, aaah... I can't..."

    show bg shalia5 with flash

    shalia "AAAAAAAH!!!"

    with doubleflash

    "Shalia reaches her climax too, spurting love juice at a surprising distance. Her orgasm lasts for a long time, her body shaking wildy as she squirts everywhere."

    show bg satella sex3_5 at top with dissolve

    you "Wow..."

    "Satella holds you lovingly, her face nested against your chest."

    $ unlock_achievement("h shalia")

    satella "I am pregnant with your baby, [MC.name]... I can feel it..."

    show bg shalia5 at top with dissolve

    shalia "Mmmmh, aaaah..."

    "Shalia takes a moment to recover her godly composure."

    scene black
    show bg other dimension
    show shalia6 at left:
        xoffset -0.3*config.screen_width
    show satella naked at left:
        xoffset +0.3*config.screen_width
    with fade

    shalia "It is done. You have done well, follower. Your delicious seed will let a new night mistress grow inside Satella's body."

    shalia "Did I say delicious? I meant, hmm..."

    shalia "Anyway. Dawn is upon us back in Xeros, and your work here is done. You will not see us for some time. We need to tend to Satella's pregnancy."

    you "..."

    shalia "Goodbye for now..."

    "Shalia snaps her fingers."

    play sound s_spell
    scene black
    show bg master room at top
    with fade

    "You wake up late in the morning, feeling sore and utterly exhausted. Your dick is at its normal size, which you feel vaguely disappointed about."

    you "Was it all a dream?"

    scene black with fade

    $ MC.change_prestige(20)

    "You have earned a lot of prestige."

    return


## KOSMO EVENTS ##

label kosmo_returns(): # Happens 7-9 days after meeting Kosmo

    if story_flags["no kosmo"]:
        return

    stop music fadeout 3.0

    scene black with fade

    $ renpy.show_screen("show_img", img=brothel.pic, _layer = "master")

    if debug_mode:
        call stop_debug from _call_stop_debug

    with dissolve

    show sill sad with dissolve

    play sound s_surprise

    sill sad "Master! Come, quick! The strange, creepy man is back again..."

    hide sill with dissolve

    show kosmo with dissolve
    show henchman at left behind kosmo with dissolve

    play music m_kosmo fadein 3.0

    kosmo "Well, well, look who's here... If it isn't my old foe, [MC.name]..."

    you "Uh... Do I know you?"

    kosmo angry "What?!? I'm Kosmo! {b}Kosmo the Great{/b}!!!" with vpunch

    you "Nope. Doesn't ring a bell."

    kosmo "GRRRR..." with vpunch

    kosmo happy "I see what you're doing. Trying to play mind games by refusing to acknowledge my obvious star power."

    kosmo "Everyone knows and respects me, the chairman of HʘʘKERS™! I am the center of everyone's attention!" with vpunch

    kosmo "Isn't that right, random henchman #42?"

    "Henchman" "..."

    kosmo "Right?"

    "Henchman" "Uh? You talkin' to me, boss?"

    "Henchman" "Sorry. I wasn't payin' attention."

    kosmo angry "WHAT!?! GRRR..."

    kosmo "I was saying..."

    "Henchman" "Hey! Isn't that a puppy, over there? Come here, you li'l cute, furry critter..."

    hide henchman with dissolve

    kosmo "Come back! Come back here! Come..."

    kosmo "..."

    kosmo happy "Anyway."

    kosmo "I won't let you spoil my mood today, in spite of all your sabotage efforts."

    you "I did nothing. You seem to sabotage yourself well enough."

    kosmo laughing "Words of a desperate man, I can hear it in your voice!"

    you "Whatever."

    kosmo happy "I'm sure you're wondering why I came all the way to this dirty hovel. Well, I was on my way back from the slave market, and..."

    you "The slave market is on the other side of town."

    kosmo angry "..."

    kosmo "I thought I'd take a stroll! I happened to pass this place, RANDOMLY! I totally didn't go out of my way to come here!"

    show henchman behind kosmo at left with dissolve

    "Henchman" "You did, boss, don't you remember? You said..."

    kosmo "WHY THE FUCK ARE YOU STILL HERE? GO CHASE A PUPPY, OR SOMETHING!" with vpunch

    "Henchman" "Aw, someone's in a bad mood..."

    kosmo "GET LOST!!!" with vpunch

    hide henchman with dissolve

    kosmo "..."

    kosmo happy "Like I said, I was on the way back from the slave market, took a slight detour, happened to pass this Arios-forsaken place randomly and decided to let you see my latest acquisition..."

    kosmo "I just wanted to show you how inferior you were to me and why you should close shop immediately."

    kosmo laughing "Behold, my {b}new slave{/b}!"

    kosmo happy "..."

    kosmo angry "Slave! Where is she?"

    play sound s_surprise

    ev_girl2 "Uh?"

    show kosmo angry at left with move
    show kosmo_girl_captive at right with dissolve

    "Standing in the background, you see a girl on a leash tied to the gate to [brothel.name]."

    kosmo "What the... What are you doing tied up there? Where is henchman #42???"

    ev_girl2 "You told him to scram, so he left me here."

    kosmo "What! But... I..."

    kosmo "GRRRRRRR..." with vpunch

    kosmo "..."

    kosmo happy "Anyway."

    kosmo "Look at that, [MC.name]! She's going to be the new star of HʘʘKERS™! A virgin, no less! I bought her for a hefty sum..."

    ev_girl2 "Err, sorry boss... I am not a virgin."

    kosmo "Yes, exactly, and..."

    kosmo angry "WHAT?!?" with vpunch

    ev_girl2 "I am not a virgin. My old master used to rape me at least once a day, and I've had over a hundred men. Didn't he tell you?"

    kosmo "But... But... He said... And I paid..."

    kosmo "RAAAAAH!!!" with vpunch

    kosmo "You fucking slut! I'm going to have you fuck my guard dogs!"

    ev_girl2 "Hey, hold on a second! It's not my fault if you suck at negotiating. Also, you paid way too much to throw me to the dogs."

    kosmo "Grrrr..." with vpunch

    kosmo "You! [MC.name]! You may have bested me this time, but I will have my revenge!"

    you "Again, I did nothing."

    kosmo happy "We'll see who gets the last laugh!"

    kosmo "Haha... Haha..."

    play sound s_maniacal_laugh

    kosmo laughing "MUHAHAHAHAHAHAHA!!!" with vpunch

    you "You should do something about these sudden mood swings..."

    kosmo happy "Now, you have wasted my precious time long enough. I shall go. Come, slavegirl #87."

    ev_girl2 "I can't. I'm tied up."

    kosmo "..."

    kosmo "Right. Fine, I'll just untie this knot..."

    kosmo "..."

    kosmo angry "Nggh... *fails to untie knot*" with hpunch

    kosmo "NGGGGGH!!! *pulls with all his strength, making the knot even tighter*" with hpunch

    kosmo "DAMN THIS FUCKING KNOT! Henchman! Where are you!!!" with vpunch

    you "Look, I've got stuff to do. See you around."

    kosmo "GRRRR!" with vpunch

    scene black with fade

    "You and Sill move back inside. From time to time, you peer through the window to see what Kosmo is up to."

    "It takes him a couple of hours to finally untie the knot and stop cursing."

    sill sad "That guy..."

    $ calendar.set_alarm(calendar.time+6+dice(3), StoryEvent(label = "kosmo_returns2", type = "morning"))
    $ game.track("kosmo")
#     $ unlock_achievement("kosmo", level_cap=1)

    return


label kosmo_returns2(): # Happens every 7-9 days (yes, Kosmo IS annoying)

    if game.chapter > 2: # Kosmo events stop happening after the events of chapter 2
        return

    stop music fadeout 3.0

    scene black with fade

    $ renpy.show_screen("show_img", brothel.pic, _layer = "master")
    with dissolve

    play sound s_knocks

    "Once again, Kosmo has come to gloat."

    show kosmo laughing with dissolve
    show henchman at left behind kosmo with dissolve

    play music m_kosmo fadein 3.0

    kosmo laughing "Hahahaha! [MC.name]! You have to see this."

    you "It's you again... What do you want?"

    kosmo happy "Behold! There's a slave I want you to meet."

    $ girl = rand_choice(["kosmo_girl_magic", "kosmo_girl_ninja", "kosmo_girl_daughter", "kosmo_girl_wife", "kosmo_girl_pirate", "kosmo_girl_scientist", "kosmo_girl_machine", "kosmo_girl_machine2", "kosmo_girl_noble", "kosmo_girl_rogue", "kosmo_twins"])

    hide henchman
    show kosmo happy at totheleft
    with easeoutleft
    show expression girl at right with dissolve

    if girl == "kosmo_girl_magic":
            kosmo "This chick came from a magical kingdom or some shit like this."

            kosmo "I offered to pay for her scholarship in Zan, but didn't tell her I charge a 200 percent interest rate."

            kosmo laughing "So I had to repossess her whole body! BWAHAHAHA!"

            kosmo happy "She had a bunch of useless magical shit for use in her studies."

            kosmo "I had my personal wizard tinker with it to make it suited to her new life as a cumdump."

            kosmo "Now she's dumb as a doorknob, but magically horny 24/7!"

            kosmo laughing "BWAHAHAHAHA!" with vpunch

            scene black with fade

            sill sad "Oh, what an unpleasant man..."

    elif girl == "kosmo_girl_ninja":
            kosmo "Have you heard about the Kunoichi clans? They're a bunch of female ninjas."

            kosmo "This one tried to take my life, can you believe it? But my security is top notch. I have 20 guards in my bedroom alone."

            $ MC.rand_say(("Yes, I'm sure you love to jerk off in front of 20 dudes...", "Cool. That should give you the audience you need when you're bouncing on your boy's dick."))

            kosmo angry "WHAT? Shut up! One day, I'll be the one to send ninjas after you! GRRRR..." with vpunch

            kosmo happy "Anyway."

            kosmo "They captured the ninja bitch, and I've been keeping her high on spice ever since, just to be on the safe side..."

            kosmo "Now her pussy is the one that gets infiltrated all night!"

            kosmo laughing "BWAHAHAHAHAHA!!!" with vpunch

            scene black with fade

            sill sad "Such cheesy jokes... I hate that guy..."

    elif girl == "kosmo_girl_daughter":
            kosmo "I have a lot of wealthy customers, because, of course, they want the best quality they can get."

            kosmo laughing "They wouldn't want to be caught dead in a cesspool like your pathetic whorehouse!"

            kosmo happy "Of course, we do everything to get them addicted..."

            kosmo "We even rub spice inside the girl's pussy. It shortens their lifespan, but it makes the customers hooked."

            kosmo "This is the daughter of one of my most loyal customers. When he had no money to pay, I took his youngest daughter instead."

            kosmo "You should have seen him grovel on the floor and beg! Now, his daughter is being used as a honey pot for others like him."

            kosmo laughing "BWAHAHAHAHA!!!" with vpunch

            scene black with fade

            sill sad "This man is as evil as he is stupid... *alarm*"

    elif girl == "kosmo_girl_wife":
            kosmo "I have faced much bigger and fiercer competitors than you, [MC.name]... You're just small fry."

            kosmo laughing "This is all because of my {b}legendary{/b} business acumen!" with vpunch

            "Henchman" "But boss, didn't your 'pa leave his enormous fortune to you?"

            kosmo angry "Shut the fuck up, henchman #33!!!"

            kosmo happy "Like I said, my legendary business acumen allowed me to be born into the wealthiest family in the city! I was a millionaire before I could even walk!"

            you "That would be at the age of 12, I guess?"

            kosmo angry "GRRR!" with vpunch

            kosmo happy "Don't be jealous because you come from the gutter, while my daddy was super rich."

            you "Yeah, but he never loved you."

            kosmo angry "How did you... Grrr..." with vpunch

            kosmo happy "Anyway. I like to think of myself as a self-made man. When I took over my father's brothel empire, we had  only 10 branches, and now..."

            kosmo "We have 12!" with vpunch

            you "Ok. That's... Impressive?"

            kosmo laughing "Bwahahaha! You bet it is!"

            you "Impressively stupid."

            kosmo angry "What?!?" with vpunch

            kosmo happy "Have fun while you still can, little man. See that milf over here?"

            "Kosmo points at his slave."

            kosmo "She was the wife of my biggest competitor..."

            kosmo "I drove him out of business after his brothels spontaneously burst into flames, which I had nothing to do with, of course."

            kosmo "I sent him to the galleys, and enslaved his beloved wife... Now she's my whore, and her job is to jerk off every single one of my henchmen every morning..."

            play sound s_surprise

            sill sad "That's horrible! Why do that?"

            kosmo "That's one of the perks. it helps a lot with recruiting."

            kosmo "Don't worry, little girl... When you're mine, I'll find a much better use for you..."

            kosmo "I can use you to clean my dick up every morning! I bet you'll like it!"

            kosmo laughing "Bwahahahaha!!!"

            play sound s_scream

            sill "Ew! Get lost, you pervert! Master..."

            kosmo angry "How dare you! You're just a slave! I'll whip you..."

            you "Get the fuck out of here, Kosmo. Sill's mine. No one is allowed to trespass on my property."

            kosmo "I'll be back, [MC.name]! I'll get your pink-haired slut eventually, and when the day comes..."

            sill "Go AWAY!"

            scene black with fade

            sill sad "Master, thank you for defending me..."

    elif girl == "kosmo_girl_pirate":
            kosmo "Did I tell you the story of when my personal yacht was attacked by pirates?"

            kosmo "It was a fierce fight, I can tell you that..."

            kosmo "We had many dead and wounded but thanks to my courageous leadership, we prevailed!"

            you "You were involved in the battle?"

            kosmo "Well, not technically, as I was sleeping in my feather bed in Zan while the yacht crew was running errands for me in pirate-infested waters... I get sea-sick."

            kosmo "But my incomparable leadership is so impressive, I can win a battle without even knowing about it!"

            you "Given the number of things you don't know about, that's a real talent..."

            kosmo laughing "Thank you! Bwahahahaha!!!"

            you "..."

            kosmo happy "Anyway. Thanks to my bravery, my men captured the pirate leader."

            kosmo "She tried to escape a few times, so I've given orders for her to be fitted around the clock with a vibrating dildo."

            play sound s_moans

            "Pirate girl" "Aaah, aaah, oooh..."

            kosmo "She's only allowed to take it off when fucking a customer. But most of them prefer to do her in the ass, so she doesn't get to take it off very often."

            kosmo laughing "Needless to say, she is too spent to run anywhere now! Bwahahahaha!!!" with vpunch

            kosmo happy "I'm asking the artisans to prepare a bigger dildo now... At least four times the size."

            kosmo "We'll test it on her first, but when the time comes, I will use it on your slave Sill!"

            kosmo laughing "BWAHAHAHAHA!!!" with vpunch

            scene black with fade

            sill sad "Master... Please don't let me fall into his clutches... *worried*"

    elif girl == "kosmo_girl_scientist":
            kosmo "This will come as a surprise to you, but even though my family paid the best educators in Xeros to teach me, I wasn't doing that well in school."

            you "Nope. No surprise there."

            kosmo "Given how bright I am, the failure of my educators to properly teach me infuriated me to no end."

            kosmo angry "I wanted them all lynched, because they were preventing my genius from shining, and I seemed to be the only one aware of it."

            you "I bet."

            kosmo "But my parents would have none of this, and even went so far as to suggest that my failure at all exams was somehow my fault..."

            kosmo "I especially hated maths! Oh, I hated it! Just as sure as two and two make five!"

            you "Actually..."

            kosmo angry "And now, it continues, that's why the accountants won't let me near the books..."

            kosmo happy "But eventually, I got my revenge!"

            kosmo "I posted an ad for a math and science teacher at the job posting corner in Zan..."

            kosmo "Then, I kidnapped the damn teacher! And now, she's whoring for me!"

            kosmo laughing "BWAHAHAHA!!! Take that, maths!" with vpunch

            you "You know that maths isn't a thinking entity, and doesn't actually... Oh, well. *sigh*"

            kosmo happy "The dear professor got a PhD, but now she only gets the D!"

            kosmo laughing "BWAHAHAHAHAHA!!!"

            scene black with fade

            sill sad "What a moron..."

    elif girl in ("kosmo_girl_machine", "kosmo_girl_machine2"):
            show expression girl at quake
            play sound s_vibro

            "*buzzing sound*"

            play sound s_moans

            "Girl" "Oh, aah, aaaaaah!!!"

            show expression girl at right

            "A girl is imprisoned in a sort of machine, a mess of cables and gizmos buzzing with magical energies. The device is attached directly to her pussy."

            kosmo "Behold! My engineers have dubbed this... The Fuck'o'drome!"

            you "..."

            kosmo "But I dub it... The... The..."

            kosmo laughing "THE FUCK'O'DROME!!!" with vpunch

            you "It's the same."

            kosmo angry "I know it's the same! But I've decided to call it that! It was like, how do they say... A yoo-ree-kah moment!"

            you "You just said your engineers came up with it."

            kosmo "Because they got their inspiration from me, of course!"

            kosmo happy "When I heard the name, I knew it was a name that I could totally have come up with. So it's like, my idea, really."

            you "..."

            play sound s_vibro

            "*intensifying buzz sound*"

            play sound s_orgasm

            "Girl" "Aaah aaaaaaah, aaahaaaaa!!!"

            "The girl climaxes loudly. A counter on the side of the strange machine moves up one digit to reach 115."

            kosmo "We use this to train our new girls to be complete sluts. A few days on this machine will break the mind and pussy of any girl."

            kosmo "Organic whoring using ancient techniques like your pathetic brothel are going extinct! Battery whoring is the future!"

            kosmo laughing "No more time wasted training and catering for girls! It's all going to be automated, and we're going to cut costs a hundredfold!!!"

            you "..."

            play sound s_vibro

            pause 0.5

            play sound s_vibro

            "The machine starts buzzing wildly."

            play sound2 s_vibro

            "Girl" "Oooh, aaah, aaaah..."

            play sound s_crash

            with vpunch

            "The machine grinds down to a halt with a nasty sound."

            kosmo "..."

            kosmo angry "What's this! Machine, why aren't you working anymore?"

            "Machine" "..."

            kosmo angry "Answer me!" with vpunch

            play sound s_punch

            "Kosmo hits the machine hard with his fist, only to hurt his hand pretty bad."

            kosmo "Ouch! Aw, aw, ouch!!! *mad*"

            kosmo "I hate you, you fucking bag of bolts! Why don't you work!"

            "Henchman" "Err, boss, perhaps we should call a mechanic..."

            kosmo "Shut up! How dare this machine defy me, Kosmo the Great!"

            kosmo happy "I'll just open the control panel. I've seen the engineers do it, it can't be that hard..."

            play sound s_creak

            kosmo "Here! I'll just touch this..."

            play sound s_thunder

            kosmo angry "AAAAAAh!!!"

            play sound s_wscream

            hide kosmo with dissolve

            "Henchman" "Boss... Boss?"

            you "I think he's out of it."

            "Henchman" "He's all passed out. His hair is on fire."

            you "Oh, that. Don't worry, I'll put it out."

            play sound s_pee

            you "*whistle*"

            "Henchman" "Ahem... I think I should get him back. He looks awfully crispy."

            you "Yeah, you do that. "

            if farm.active and farm.installations["workshop"].has_room():
                    extend "I'll just get this gizmo off... He's not going to need it anymore, I'm sure."

                    play sound s_ahaa
                    hide expression girl with dissolve

                    $ r, msg = farm.add_minion(Minion("machine"))

                    "[msg]"

            scene black with fade

            sill sad "I hope we never see him again..."

            you "Don't count on it."

    elif girl == "kosmo_girl_noble":
            kosmo "I'm back! I'm sure you expected my return."

            you "Expected, no. Dreaded, yes."

            kosmo "And why wouldn't you! As always, I have brought my latest prize..."

            kosmo "When you see this one, you will just give up and hand all your assets over to me! I guarantee it."

            play sound s_maniacal_laugh

            kosmo laughing "BWAHAHAHAHA!!!" with vpunch

            you "The only thing I'm going to give you is a good kick in the..."

            kosmo happy "BEHOLD!!!"

            kosmo "Lady Norra!" with vpunch

            kosmo "Or, as I call her now, Lady Nobra."

            kosmo "Lady Norra is from the House of Gagaryen... You must have heard of it."

            you "Yeah, I'm not all up to date on the genealogy of Zan's noble inbreds..."

            kosmo "Of course you aren't! Because you're a filthy peasant!"

            kosmo "But for a lord of my standing, I have to be aware of that..."

            kosmo "Listen to this... Lady Norra is a princess. She is...."

            kosmo "Wait for it..."

            kosmo "The second cousin of the grand-daughter of the brother of the squire who married the chambermaid of the sister-in-law of Lady Zagrub..."

            kosmo "...who is friends with the lover of the stunt-double of {i}Princess Kurohime herself{/i}!!!" with vpunch

            you "..."

            you "So?"

            kosmo "Don't you get it? She's almost royalty! She is 657th in line for the throne!!!"

            kosmo "And she is my whore now! BWAHAHAHAHA!" with vpunch

            you "..."

            kosmo "Lady Norra tried to run away with her lover, a mere baker who was a filthy commoner."

            kosmo "They got caught, and he was quartered for his troubles."

            kosmo "She brought shame on her family. I am a good friend of her elder brother, so I convinced him to let me have her, and make the problem disappear."

            kosmo "I paid him a hefty sum, of course. But here I am, having a true-blooded princess in my brothel!"

            kosmo "We try to dress her up as princess Kurohime to fulfill the fantasy most people have."

            kosmo "Of course, they don't really look alike much, so I've had limited success."

            kosmo "But it will come!"

            kosmo laughing "You can count the days before foreclosure! BWAHAHAHAHA!!!" with vpunch

            scene black with fade

            sill sad "Poor girl..."

    elif girl == "kosmo_girl_rogue":
            kosmo "I know you won't believe it, but some people have the nerve to stand up against me."

            you "I'm surprised anyone gives you as much as the time of day..."

            kosmo "Take this rogue girl, for example. She had the gall to try to steal from {i}my{/i} very own property!"

            kosmo "I had a stash of a couple hundred-thousand bananas for my guests... And she stole {i}one{/i}!"

            you "She stole a hundred thousand bananas?"

            kosmo angry "Of course not, you idiot! She stole one banana. What a shameless, dirty thief..."

            kosmo "She pretended she did it because she was starving! But I know the truth! She did it because she wanted my ruin!"

            you "I think I can add 'paranoia' to the list of your defining qualities."

            kosmo happy "So, I fed her a lot of bananas, all right... UP HER ASS AND PUSSY!!!"

            play sound s_maniacal_laugh

            kosmo laughing "BWAHAHAHAHA!!!" with vpunch

            kosmo "HAHAHAHA..." with vpunch

            kosmo "HAHA..."

            kosmo happy "HA..."

            kosmo "... *cough*"

            you "Are you done?"

            kosmo "Wait, I'm catching my breath."

            kosmo "*inhales deeply*"

            play sound s_maniacal_laugh

            kosmo laughing "BWAAAHAAAHAAAHAAHAAHAAHAAHAHAHA..." with vpunch

            scene black with fade

            "You head back inside and close all the doors and shutters. Kosmo is still laughing."

            sill sad "That man really has issues..."

    elif girl == "kosmo_twins":

        kosmo "Twins, [MC.name]. TWINS!"

        you "..."

        you "They look different."

        kosmo angry "..."

        kosmo "Well, uh... Of course they do! They're not {i}identical{/i} twins, you see..."

        kosmo "Do you have any idea how expensive it is to get real twin whores these days!!!"

        kosmo happy "But they are sisters nonetheless... All right, cousins. We advertise them as real twins, and the customers have been paying good money to fuck them both ever since they came of age..."

        you "Isn't that, like, false advertising? Aren't you deceiving your loyal customers?"

        kosmo "Exactly..."

        kosmo laughing "BWAHAHAHAHA!!!" with vpunch

        you "Forcing young teenage girls into a life of rape and slavery is one thing..."

        you "But deceiving your customers? That's low, even for you."

        kosmo happy "What can I say? It's a natural born talent."

        kosmo "Come on, twins! I've got a bunch of gullible customers who want to fuck you this afternoon..."

        hide kosmo
        hide expression girl
        hide henchman
        with dissolve

        show sill sad

        sill sad "Such a dishonorable man..."

        scene black with fade

    $ calendar.set_alarm(calendar.time+6+dice(3), StoryEvent(label = "kosmo_returns2", type = "morning"))
    $ game.track("kosmo")
#     $ unlock_achievement("kosmo")

    return


## BANKING EVENTS ##

label no_money():

    # When the player runs out of money, the banker will show up
    # The banker will offer a loan to bail out the player
    # If the player runs out of money again before repaying the loan, his property will be reposessed, and it is game over
    # If the player runs out of money after repaying the loan, the banker will offer a loan again
    # Loan amount, cost and duration increases with district rank
    # When the player unlocks the bank, he becomes able to take loans of various amounts and duration. He can also repay any outstanding loan in full
    # The first H scene will unlock when the player repays his third loan
    # The bank will offer the special loan: extra costly, but unlocks final H scene

    if MC.gold >= 0: # Ignores this event if for any reason MC is back in the black
        return

    if MC.loan: # Bankrupcy
        "{color=[c_red]}You do not have enough money to pay interest on your loan.{/color}"
        jump game_over_bank

    elif NPC_banker.flags["first loan"]:
        "{color=[c_red]}You ran out of money again before you could pay the banker back.{/color}"
        jump game_over_bank

    elif NPC_banker.flags["TJB special"]:
        "{color=[c_red]}You ran out of money while going for the TJB special challenge.{/color}"
        jump game_over_bank

    elif not story_flags["no money first time"]:

        scene black with fade

        $ renpy.show_screen("show_img", brothel.pic, _layer = "master")
        with dissolve

        $ story_flags["no money first time"] = True

        "You get up in the morning with your stomach growling."

        "As you wander around, looking for breakfast, you run into Sill. She looks completely panicked."

        show sill sad with dissolve

        sill sad "Oh no, Master! We ran out of money... What are we going to do?"

        you "Well, I don't know... Can it wait 'til after breakfast?"

        sill "Breakfast? There isn't any food left! We have outstanding bills for the grocer, the butcher..."

        you "No food? This is a disaster!!!" with vpunch

        sill happy "Well... We still have this half-eaten carrot. I saved it for you."

        "Your stomach growls even louder."

        you "Oh no... What are we-"

        with flash

        play sound s_fire

        "*PUFF*"

        "Before you have a chance to think, a cloud of smoke puffs out in the middle of the hall."

        sill sad "Eeeek!"

        hide sill with dissolve
        play sound s_spell
        show banker appears happy with dissolve

        you "What the... *cough* *cough*"

        play music m_jazz fadein 3.0

        "A beautiful woman, clad in a fancy, revealing dress, steps out of the magic smoke. She wears a cunning smile."

        you "Who... Who the hell are you?"

        "The woman takes in her surroundings, paying no attention to your angry looks."

        banker "So this is the place, uh... I figured it would be run down, but still..."

        you "Hey! Stop measuring the place for drapes! I'm talking to you."

        play sound s_sigh

        banker "Hmm?"

        "The woman turns to face you. You notice she has some magical features, resembling a dark fox."

        "She must be one of the forest people... Although she looks very worldly."

        sill "She's one of the Inari... The fox people... Watch out, Master, maybe she is cursed! *whisper*"

        banker "Hey. I can hear you, you know?"

        sill "Aaaah!!!" with vpunch

        "Sill runs away scared to cower in her room. Waiting for an explanation for this interruption, you stand your ground and point an accusing finger."

        you "What's wrong with you, barging into someone's property like this! And interrupting breakfast, no less!"

        banker "Ah, you must be the owner, [MC.name], isn't it?"

        you "Yes... How do you know my name?"

        banker "I was sent by one of my clients. I came to offer you a deal."

        "She gives you a wolfish smile."

        you "Clients?"

        banker "Yes. I am from the banking guild. See?"

        "Carelessly, she points to the side of her left breast, revealing a small banking guild tatoo."

        you "*gulp*"

        $ banker_name = "Banker"

        banker "Let me cut to the chase. I hear you are in a dire financial situation right now."

        you "No, err, we're doing fine..."

        "She looks skeptical. She sees the half-eaten carrot on the table."

        banker "Oh really... Is that your 'breakfast'?"

        "*GROOOWL*" with vpunch

        "Your stomach betrays you."

        play sound s_laugh

        "She giggles."

        banker "I am a partner at TJB, a small but elite banking operation. I have a solution to all of your problems."

        you "Oh, really?"

        banker "One of my wealthy clients is willing to buy your business for a small sum... Enough to leave this city, and start over in the countryside."

        banker "He would take the brothel and all your slaves, naturally. He was particularly interested in the pink-haired one, for some reason."

        you "..."

        you "Tell him to get lost. I'm not selling."

        banker "Ah. I see. But how will you manage your financial predicament, then?"

        "You try to sound confident."

        you "We'll figure something out, I'm sure."

        "She frowns."

        banker appears mad "This is a setback... I came all the way here for nothing."

        "She takes a second look at you. She looks thoughtful."

        banker appears happy "Unless..."

        you "What?"

        "Her smile is back again."

        banker "I have another idea. Aside from managing the business of my wealthier clients, I also handle loans at TJB."

        you "A loan shark, uh..."

        banker "Please, I am no such thing. I simply extend a helping hand to people in need... For a price."

        you "Oh, I see now. A loan shark."

        banker "Aw... I am pained, you misjudge me."

        "She makes a show of feeling hurt."

        banker "I will show you how generous I am. As this is your first time with TJB, I will give you a loan, free of interest."

        you "I'm not int... Wait, free loan?"

        banker "Sure."

        you "Wow!!! Amazing!"

        "She looks at you the way a fox looks at a hen."

        banker "A loan that should bring you back in the black... With 250 gold."

        you "Oh."

        banker "If you want to borrow more, you will be charged interest, of course."

        you "Of course..."

        banker "So what's it going to be? Take my offer, or leave it?"

        you "..."

        "Your stomach growls again. You think of all the delicacies you could buy for 250 gold."

        you "All right. Deal."

        "She smiles at you, all teeth."

        banker "Let's shake hands, then."

        you "Yeah..."

        "Her silky, skin-tight glove is nice and soft to the touch. Her tits bounce up and down as you shake her hand, and you can barely keep your gaze at eye-level."

        banker "Splendid, then! Here you go."

        "Even though her dress covers very little, she still manages to extract a small purse from somewhere beneath, exposing more skin as she rummages for it."

        play sound s_gold

        $ loan_amount = NPC_banker.flags["first loan"] = int(-MC.gold + 250)
        $ MC.gold = 250

        "You have received [loan_amount] gold."

        you "Thank you..."

        banker "I'll see you in 10 days for payment. I expect to get the [loan_amount] gold back in full."

        you "Oh... Okay."

        banker "A word of warning, though. I never give another loan until the first one is repaid."

        banker "If you run out of money again, or if you fail to repay me..."

        banker "The bank will seize all of your property, and throw you out. You'll get nothing. [emo_heart]"

        "She sounds almost cheerful as she spells out your financial doom."

        you "That's... Harsh. *gulp*"

        banker "Come on. You run a brothel, you know the ways of the world..."

        banker "Anyway. It was nice to meet you. Gotta go now, bye."

        you "Wait, I..."

        with flash

        play sound s_fire
        hide banker with dissolve

        "*PUFF*"

        you "*cough* *cough*"

        you "Damn... She's gone."

        scene black with fade

        "You have borrowed [loan_amount] gold. You must give it back in 10 days."

        $ calendar.set_alarm(calendar.time+10, StoryEvent(label = "banker_repaid_first", type = "morning"))

    else: # New loan proposition

        "The banker visits you again today."

        play music m_jazz fadein 3.0
        show banker with dissolve

        banker "Oh, my... It looks like you've run out of money again. How careless."

        you "Well, uh... It's not my fault..."

        banker "But don't worry. We at TJB are always ready to help a suck... I mean, a customer out."

        you "You are? Wow, I'm lucky."

        banker "Sure! We offer the best rates in the city... Give or take a few dozen percent."

        you "Well, uh... I'm not too good with maths... How much is that?"

        $ loandict = {1 : Loan(250, 0.4, 10), 2 : Loan(500, 0.4, 10), 3 : Loan(1000, 0.4, 14), 4 : Loan(2500, 0.4, 14), 5 : Loan(5000, 0.4, 20), 6 : Loan(10000, 0.4, 20), 7 : Loan(25000, 0.4, 25),}

        $ MC.take_loan(loandict[game.chapter])

        banker "Here is the deal. I will lend you [MC.loan.amount] gold for [MC.loan.duration] days. You must repay [MC.loan.daily_cost] gold per day. The total cost will be [MC.loan.total_cost] gold. Sounds fair?"

        you "I see... That sounds a bit steep. What if..."

        banker "Or you could just go bankrupt, lose everything you own and be branded a debtor slave. I hear working on a galley can be real fun... While it lasts."

        you "Ahem. In that case, I gladly accept your generous offer."

        play sound s_laugh

        banker "Splendid! I thought you might. *smile*"

        play sound s_gold
        "You have received [MC.loan.amount] gold as a loan from the Banker."

        banker "All right, time is money, see you in [MC.loan.duration] days! Don't forget to pay me or I'll seize all your goo-oods! [emo_heart]"

        "She blows you a kiss and disappears."

        you "Damn... I need to make some money, fast."

    stop music fadeout 3.0
    scene black with fade

    return


label banker_repaid_first():

    play sound s_knocks

    "This morning, you receive the visit of the girl from the banking guild."

    play music m_jazz fadein 3.0
    show banker with dissolve

    banker "Oh, hello, [MC.name]."

    you "Hello. You came to get your money back, I presume?"

    banker "Yes. That was the deal. I'm sure you remember."

    if MC.gold >= NPC_banker.flags["first loan"] :
        you "Yes... *sigh*"

        $ you("Here, your " + str(NPC_banker.flags["first loan"]) + " gold, back in full.")

        play sound s_gold
        $ MC.gold -= NPC_banker.flags["first loan"]

        $ narrator("You have repaid " + str(NPC_banker.flags["first loan"]) + " gold.")

        $ NPC_banker.flags["first loan"] = False

        $ unlock_achievement("first loan")

        play sound s_sigh

        banker "Fantastic. You're not as clueless as I first assumed... *mutter*"

        you "What?!?"

        banker "You're good, you're good, a good manager! That's what I said... Hem."

        banker "Anyway. Now that we're in business, I can offer you loans next time you are running low on gold... But this time, I'll charge interest, of course."

        you "Of course..."

        banker "And make sure to pay me a visit if you come by the banking guild. TJB is always pleased to receive a valuable customer."

        you "Okay."

        banker "Okay, gotta go now... Time is money, you know!"

        play sound s_spell
        hide banker with dissolve

        you "All r-"

        you "And... She's gone."

        you "I wanted to ask her about her bank, though, TJB was it?"

        you "TJB... Well, the B stands for 'bank'."

        you "But what does TJ stand for?"

        you "TJ... Well, it's a mystery. We may never know."

        stop music fadeout 3.0
        scene black with fade

    else:
        "{color=[c_red]}You do not have enough gold to pay the banker.{/color}"

        stop music fadeout 3.0

        jump game_over_bank

    return


label visit_bank():

    show banker with dissolve

    banker "Oh! A customer."

    play music m_jazz fadein 3.0

    if not story_flags["bank visited"]:

        $ story_flags["bank visited"] = True
        $ banker_name = "Banker"


        banker "Welcome to TJB. As a partner, I am delighted to welcome you to the finest banking establishment in the city."

        "You look around the place. It is actually pretty small, and the woman seems to be the only one working here."

        you "Say, don't you have staff to work here? The other partners are on leave, perhaps?"

        banker "You see, we are a small and efficient operation, not like our big name competitors. That's why I'm the one and only partner here at TJB."

        you "..."

        banker "And staff means too much overhead costs, not to mention labor disputes. I handle all the accounts myself."

        you "I see... Speaking of accounts... I don't see any accounting books?"

        banker "Haha, a common misconception. Accounting gets in the way of creative banking practices, not to mention they can be seized by the courts, err..."

        banker "I keep all accounting information very secure, locked away from improper scrutiny. In my head."

        you "In your head... In your head?"

        banker "Sure. That's the best way to ensure your personal data is safe."

        you "Well..."

        you "That makes sense. I guess."

        banker "Of course. Now, what can I do for you?"

        banker "I think you already know about our emergency loan service... But here I can offer you more options if you would like to take a loan."

        you "That sounds good. What do you have?"

    if NPC_banker.flags["first loan"]:
        banker "We're getting ahead of ourselves: First of all, you should repay your first loan."

    elif MC.loan:
        banker "Ah, [MC.name]. You still have [MC.loan.amount] gold to repay on your current loan."

        banker "If you wish, you can pay cash and settle your account right now. I will charge no interest, but you won't get a loyalty point either."

        menu:
            banker "Would you like to repay your loan early?"

            "是的，我想现在就结清[MC.loan.amount]金币的债务。":
                if MC.repay_in_full():
                    play sound s_gold
                    "You have repaid your loan in full. You are now free to take a new loan."

                jump visit_bank

            "不，我要继续贷款，继续支付利息":
                pass

            "不，我宁愿和你到床上谈业务" if NPC_banker.flags["sex"]:

                banker "Hungry for more, are you? I must say I was looking forward to it, too. Give me a second."

                hide banker with dissolve

                play sound s_dress

                show banker cheerleader with dissolve

                "Voila! [emo_heart]"

                call banker_special2() from _call_banker_special2

    elif NPC_banker.flags["TJB special"]:
        banker "You are still going for the TJB special challenge. I won't lend you any money until it is finished."


    else:
        python:
            menu_options = [("Do you want to take a personal loan?", None),]
            loans = [Loan(250, 0.4, 10), Loan(500, 0.4, 10), Loan(1000, 0.4, 14), Loan(2500, 0.4, 14), Loan(5000, 0.4, 20), Loan(10000, 0.4, 20), Loan(25000, 0.4, 25),]

            for l in loans:
                if game.chapter - 4 <= loans.index(l) <= game.chapter - 1:
                    menu_options.append(("Borrow " + str(l.amount) + " gold for " + str(l.duration) + " days (total cost: " + str(l.total_cost) + ")", l))

            if NPC_banker.love >= 25:
                menu_options.append(("TJB Special", "special"))

            if NPC_banker.flags["sex"]:
                menu_options.append(("I want sex", "sex"))

            menu_options.append(("No thanks", "back"))

        $ r = menu(menu_options)

        if r == "back":
            pass

        elif r == "sex":

            you "Actually, I came for sex."

            play sound s_surprise

            banker "Uh? How bold! *blush*"

            play sound s_ahaa

            banker "Well... You know I won't say no... We're having too much fun together..."

            banker "Just give me a second to slip into something more... kinky."

            play sound s_dress

            hide banker with dissolve

            "Paying no mind to you or other potential onlookers, she undresses to her panties before you, before picking an outfit from a closet."

            play sound s_dress

            show banker cheerleader with dissolve

            play sound2 s_laugh

            banker "Teeheehee... I'm ready! [emo_heart]"

            call banker_special2() from _call_banker_special2_1


        elif r == "special":
            you "TJB special, uh? What is that?"

            "The woman gives you a beaming, hungry smile."

            banker "Ah, the TJB special! No one has asked me about it in a long time... *purr*"

            "You wonder if it's really appropriate to purr when discussing a financial proposal."

            banker "The TJB special is the most {i}extreme{/i} loan we have on offer here at TJB... Only the most fearless businessmen can hope to take that loan and repay it..."

            you "Uh?"

            banker "A hundred men have tried their hand at the TJB special, a hundred men have gone bankrupt... Leaving all their estates to me..."

            you "That doesn't sound like a great deal. I think I'll pass."

            banker "But the rewards are truly awesome, enough to drive all men crazy..."

            you "All right, all right: tell me about the special loan."

            banker "It's very simple. First, I take all your money away - as collateral."

            you "You take... Whaaaat?"

            banker "Then, you will have {b}a week to make a hundred thousand gold{/b}."

            you "WHAAAAAT?!?" with vpunch

            banker "If you can make it, I will give you your money back with ten percent interest, as well as five diamonds..."

            you "That's it? That doesn't sound so great..."

            banker "In addition... You will get the exclusive privilege... Of spending the night with your favorite banker... Me."

            "She leans close to you, putting her hands against your chest."

            play sound s_ahaa

            banker "We could do {i}anything{/i}... Remember the loyalty card? *purr*"

            you "Anything... Anything?"

            play sound s_mmh

            banker "Oh, yes..."

            banker "Rest assured, I have no decency in business, and even less in the bedroom..."

            "She leans even closer against you. Her tits are rubbing against your chest... You can feel her puffy nipples perking through her thin silk dress."

            banker "So, what do you say?"

            if renpy.call_screen("yes_no", "Do you want to take the ultimate loan, the 'TJB special'? All your money will be taken away, and you must make 100 000 gold back in 7 days, or lose everything."):
                you "I'm in. And I will be {i}in{/i}, if you catch my drift."

                "The banker throws her arms around you with excitement."

                play sound s_laugh

                banker "Oh, I can't wait!"

                banker "No other customer has ever succeeded at the TJB special, but you're not like every other customer..."

                banker "Either way, I'm in for a lot of fun! [emo_heart]"

                play sound s_gold

                "The banker swiftly takes away your [MC.gold] gold."

                $ NPC_banker.flags["TJB special"] = True
                $ NPC_banker.flags["MC money"] = MC.gold
                $ MC.gold = 0

                "She whispers in your ear with a soft, erotic voice, pressing her boobs against your chest."

                banker "I'll see you in 7 days... Don't disappoint me! [emo_heart]"

                $ calendar.set_alarm(calendar.time + 7, StoryEvent(label = "tjb_special", type = "morning"))


        else:
            if renpy.call_screen("yes_no", "Are you sure you want to take a loan for " + str(r.amount) + " gold? (daily cost: " + str(r.daily_cost) + " gold)"):
                $ MC.take_loan(r)
                play sound s_gold

                banker "All right, here is your [r.amount] gold advance. I expect payment in [r.duration] days."

                banker "See you! [emo_heart]"
            else:
                jump visit_bank

    stop music fadeout 3.0
    scene black with fade

    return

label tjb_special():

    $ NPC_banker.flags["TJB special"] = False

    if MC.gold < 100000: # Failure

        play sound s_fire
        show banker appears happy with dissolve

        banker "Tadaaa! [emo_heart]"

        banker "It's the TJB special grand finale!"

        banker "So, did you succeed in gathering 100 000 gold?"

        play sound s_fizzle

        you "Well, er... No..."

        play sound s_sigh

        banker appears mad "Aw, come on... You suck!"

        "She seems genuinely disappointed."

        banker "Well, you leave me no choice..."

        banker "As you failed the TJB special challenge, I shall keep your gold. That's too bad."

        "She doesn't seem too sad about {i}that{/i}, though."

        you "Oh no..."

        banker appears happy "But don't despair! You can try the TJB special challenge again! *wink*"

        banker "Maybe you will get lucky this time? I'll be waiting... [emo_heart]"

        play sound s_fire
        hide banker with dissolve

        "*PUFF*"

        you "Aw..."

    else:
        show banker cheerleader with dissolve

        banker "A-MA-ZING! [emo_heart]"

        banker "Congratulations! You have succeeded! You have overcome the TJB special challenge!"

        you "I did, didn't I?"

        banker "The hardest, meanest, baddest loan in the whole financial universe!"

        you "...not to mention, one that doesn't make any sense..."

        banker "As TJB's one and only partner, it is my pleasure to present you with your earnings..."

        banker "First, you get all your money back, with 10 per cent interest."

        play sound s_gold
        $ r = int(NPC_banker.flags["MC money"] * 1.1)
        $ MC.gold += r

        "You have received [r] gold back."

        banker "Next, you shall receive 5 diamonds. Enjoy!"

        $ MC.gain_resource("diamond", 5)

        banker "And last, but not least..."

        "She gives you a hungry smile, licking her lips as she steps closer to you."

        play sound s_mmmh

        banker "You get... ME!"

        call banker_special2() from _call_banker_special2_2

    return



label loan_repaid():

    show banker appears happy with dissolve

    play music m_jazz fadein 3.0

    banker "So, it seems you have repaid your debt in full."

    $ MC.loan = None

    if NPC_banker.love >= 15:
        banker "That's good, I wouldn't want to put my favorite customer in debtor prison! [emo_heart]"
    elif NPC_banker.love >= 5:
        banker "Thanks! [emo_heart]"
    else:
        banker "I didn't think you could do it. Color me impressed."

    banker "Here, have a stamp on your TJB card."

    menu:
        extend ""

        "TJB会员卡是什么?":
            you "A TJB card? What is that?"

            banker "It's a customer loyalty card. As soon as you complete 5 loans with our bank, you will get a special service that we only offer our best customers at TJB."

            you "Oh, really, what is that? A magazine subscription? A gift card?"

            play sound s_laugh

            banker "Let's just say this has something to do with the name of our bank..."

            you "T-J-B... TJ... Nope. I really don't see what this could stand for."

        "太棒了!":
            you "Yay! Being in debt is fun!"

            banker "That's the spirit."

    "The banker stamps your loyalty card."

    $ NPC_banker.love += 5

    if NPC_banker.love // 5 == 5:
        banker "Wow! 5 points! You have completed your loyalty card!"

        call banker_special1 from _call_banker_special1

    else:
        $ renpy.say(banker, "That makes it " + str_int(NPC_banker.love // 5) + " points. Only " + str_int(5 - NPC_banker.love // 5) + " more to go!")

    hide banker with dissolve

    stop music fadeout 3.0
    return


label banker_special1():

    banker "Very well... As a loyal TJB customer, you are entitled to a special gift..."

    you "Really? Do I get a cashback?"

    banker "Cash? Oh my, no!!!"

    banker "But I trust you will enjoy our special loyalty program."

    scene black with fade

    you "!?!"

    show bg banker titjob1 at top with dissolve

    "Before you have a chance to object, the woman tugs at her clothes, freeing her ample breasts from her top."

    you "Wow!"

    "Licking her lips like a hungry wolf, she pushes you down on the bed, swiftly pulling your pants down."

    "You are already rock hard from watching her huge tits, lightly bouncing back and forth."

    "As she wraps them around your cock, your mind goes completely blank."

    banker "Dear customer, allow me to administer your TJ reward..."

    you "Ugh..."

    "As she starts moving her breasts up and down, she lets out some saliva on your cock to lubricate it. The feeling is amazing as she squeezes your hard dick between her fleshy mounds."

    play sound s_mmmh

    banker "It's twitching... Mmmh..."

    play sound s_sucking

    show bg banker titjob2 at top with dissolve

    "Sticking her tongue out, she starts licking the tip of your erect cock as it pokes between her tits, tasting pre-cum."

    play sound2 s_ahaa

    banker "It's strong and salty... My favorite! [emo_heart]"

    "Before long, she starts sucking on your cock, all the while massaging your dick energtically with her tits."

    banker "Ngggh... It'sh sho good..."

    "Her technique is amazing, reminding you that forest people are reknowned for their sexual prowess."

    banker "I can feel it grow bigger in my mouth... It'sh burning hot..."

    "She sucks your cock harder with loud slurping noises, taking it deeper inside her throat."

    "At the same time, her huge, soft tits are pressing down against your shaft and balls, making you feel closer and closer to the finish line."

    "The woman looks you straight in the eyes with her fox-like stare. She is almost purring."

    banker "Let it out, let it all out... I want to see you cum..."

    "As she takes the length of your cock deep in her throat once more, you reach a noisy climax."

    with flash

    you "AAAAH!!!"

    show bg banker titjob3 at top with doubleflash

    play sound s_surprise

    "You cum really hard inside her mouth, and she gives out a muffled sound as she struggles to contain it all inside."

    "You pop your cock out, still erupting with semen. She moans erotically as you cover her face and body with shot after shot of sticky cum."

    play sound s_moans

    banker "So much cum! Aaaah... You're showering me with it..."

    "After your cock finally stops spurting out, you lay there panting while the banker grins at you with a satisfied look."

    banker "As I suspected, you have a lot of hidden resources... *lick*"

    "She laps the last drops of cum running down your shaft."

    banker "Very well, then... It was nice seeing you."

    "She stands, doing minimal effort to fix her attire before heading for the door. She doesn't seem to mind that her face, body and hair are covered with your dirty semen."

    banker "Here... TJB hopes for your continued business!"

    "She rips the old loyalty card, and hands over a new one."

    banker "Five more stamps, and you can go at it again! *wink*"

    scene black with fade

    "You take a moment to recover after she leaves. Something keeps bugging you out."

    you "One thing I still can't figure though... What does the 'TJ' in TJ Bank mean?"

    you "Guess we'll never find out..."

    return

label banker_special2():

    scene black with fade

    play sound s_dress

    pause 0.5

    play sound2 s_ahaa

    show bg banker sex1 at top with dissolve

    banker "Ahaaa..."

    "Pushing her down on the bed, you quickly shove aside her skimpy clothes to reveal her heaving breasts and pink pussy."

    banker "Mmmh... You look at me like a wolf in heat... I like that."

    "Her pussy is becoming visibly moist under your gaze, and your hard cock sticks out."

    you "I've always had a thing for cheerleaders..."

    "Freeing your dick from your pants, you let him loom over the banker's pussy. She licks her lips expectantly."

    banker "Oh my... It looks like you have a lot of savings... As your banker, I recommend you make a {i}very{/i} large deposit."

    you "Indeed. I couldn't help but notice your ample assets. I have a sudden influx of... capital... I need to release."

    banker "Very well. Would you like to check my spread?"

    "She opens up her legs even more. Her pussy is dripping with love juice now as she devours your cock with her eyes."

    you "Nice... Can you go even wider?"

    play sound s_mmmh

    "She moans erotically."

    banker "I will make your capital grow even further... Mmmh, I can't wait to receive your seed investment..."

    show bg banker sex2 at top with dissolve

    "Unable to resist financial foreplay, you plunge your erect cock straight into her gaping pussy. She takes it all in stride, welcoming your hot shaft inside her."

    play sound s_moans

    banker "This is so good... Aaaah..."

    "Her pussy is twitching. It seems to have a mind of its own as it wraps tightly around your cock. The sensation is quite new to you."

    you "Hmmm... Your pussy walls are moving..."

    banker "This is my special technique, that's why I'm the best in Zan... Not that many customers can experience it, though."

    "She pouts."

    banker "I guess I made the TJB special too hard, because of that, I don't see a lot of action... That is, until you came around. *smile*"

    "Her pussy feels amazing, and you cannot help but increase your pace."

    "She is very wet, however, and her pussy has no problem swallowing you whole."

    banker "You can pound me as hard as you want... Harder than I compound interest..."

    "Her technical talk excites you, and you take her word for it."

    "Even though you hammer down her pussy harder and harder, nailing her to the bed, she doesn't seem to mind it at all. In fact, her love juice is splashing around in large quantities, and she moans in your ear as she holds you even closer."

    banker "It's time... For the big liquidity event..."

    "Her pussy contracts against the length of your cock, inviting you even deeper inside her. As you squeeze her boobs hard, she cums with a scream."

    with flash

    play sound s_screams

    show bg banker sex3 at top with doubleflash
    banker "Aaah, AAAAH!!!"

    "Her body shakes hard as she pulls you in, and suddenly you reach your limit too."

    play sound s_orgasm

    banker "Oh, fuck yes!!! YES!!!"

    "You spill out a huge amount of cum, filling her to the brim with hot semen."

    banker "Aaah..."

    "Still, her hungry pussy doesn't let you go until you've spent every last drop."

    you "Uggh..."

    banker "Aw... So good..."

    banker "[MC.name]... You will come back, won't you?"

    you "S-Sure..."

    "She looks happy. She purrs with satisfaction."

    banker "Good. I'll be happy to service your d... Your debt. Anytime..."

    banker "But the night is still young... Come here! [emo_heart]"

    scene black with fade

    play sound s_aaah

    "You have spent all of your, err, capital, and actions, for the day."
    $ MC.interactions = 0

    if not NPC_banker.flags["sex"]:
        "You can now have sex with the banker."
        $ NPC_banker.flags["sex"] = True

    return

label game_over_bank():

    play sound s_fire

    show banker appears mad with dissolve

    if dice(6) == 6:
        banker "All right, time is up! Where is the money, [MC.name]ski? WHERE'S THE FUCKING MONEY?"
    else:
        banker "All right, time is up! Where is the money, [MC.name]?"

    you "No! Wait! I can repay you later... I can explain!"

    sill sad "Please! Be merciful!"

    banker "No way! You know the rules! The bank always wins... *frown*"

    call game_over("Banker") from _call_game_over

label game_over(antagonist):

    scene black with fade

    play music m_wind
    show bg sky dusk at top with dissolve

    "The [antagonist] repossessed your brothel and everything in it. Your slaves were sold to the highest bidder."

    show sill past with dissolve

    pause 1.0

    hide sill with dissolve

    "Even Sill was taken from you. There was nothing you could do to prevent the slaver's guild from carrying her away."

    "You now find yourself on the road again, alone and destitute. A sad end for a..."

    $ unlock_achievement("game over")

    play music m_theme

    $ title = Text(("Brothel King"), size=80, yalign=0.4, xpos=0.5, drop_shadow=(3,3), font="DejaVuSans.ttf")

    show expression title #Note: Find a way to make the zoom slower and the title cooler
    with zoomin

    ""

    stop music fadeout 2.0

    scene black with fade

    centered "{color=[c_red]}{b}GAME OVER{/b}{/color}"

    $ renpy.full_restart()


## TREASURE GIRL EVENTS ##

label treasure_girl_sex(who, pic):

    scene black with dissolve

    if who == "blonde" and not story_flags["blonde treasure event"]: # Blonde girl event
        $ story_flags["blonde treasure event"] = True
        $ col = c_blonde

    elif who == "pink" and not story_flags["pink treasure event"]: # Pink-haired girl event
        $ story_flags["pink treasure event"] = True
        $ col = c_hotpink

    else:
        return

    you "You! What the hell do you think you're doing!" with vpunch

    play sound s_surprise

    "{color=[col]}Girl{/color}" "Uh?!?"

    you "Yes, you!"

    show screen show_event("events/" + pic, ys=1.0)
    with dissolve

    you "Do you think you can fool around naked in my treasure room every night without suffering the consequences?"

    you "Come over here!"

    play sound s_scream
    "{color=[col]}Girl{/color}" "Aaah!!!"

    hide screen show_event


    if who == "blonde":

        show bg treasure_blonde sex1 at top with dissolve

        "You shove the girl on the floor, spreading her legs apart."

        you "You've been dangling that juicy pussy before me for too long! Prepare to get fucked!"

        show bg treasure_blonde sex2 at top with dissolve

        play sound s_surprise

        "{color=[col]}Girl{/color}" "W-Wait..."

        you "Take this!"

        play sound s_scream_loud

        show bg treasure_blonde sex3 at top with hpunch

        "Not giving her any time to recover from her surprise, you force your hard cock right inside her pussy. It slips in surprisingly easily."

        play sound s_moans

        you "You're already wet, I see... I guess you're an all-out pervert, playing around naked every night in my brothel..."

        "{color=[col]}Girl{/color}" "D-Don't... I..."

        "{color=[col]}Girl{/color}" "Aaaah!!!" with hpunch

        "You start moving inside her, lifting her hips and spreading her legs even wider so that you can reach deep inside her cunt."

        "{color=[col]}Girl{/color}" "Aaah, aaaah!!! Aaaah!!!" with hpunch

        you "Look how easy it is to move inside you... What a loose pussy, I bet you were dying to get fucked!"

        "{color=[col]}Girl{/color}" "N-No... Aaaah!!!" with hpunch

        "You keep pounding her defenseless pussy, splashing her love juice around with wet, naughty noises."

        you "Well, it looks like I'm ready to cum first... Get ready to be creamed!"

        "{color=[col]}Girl{/color}" "Aaah! Stop, it's dangerous-"

        with flash

        play sound s_screams

        scene black with doubleflash

        "A while later..."

        show bg treasure_blonde sex4 at top with fade

        "{color=[col]}Girl{/color}" "You... You monster... How long have you been fucking me..."

        you "Only a few hours! You are getting what you deserve. You had it coming."

        "{color=[col]}Girl{/color}" "AHAAA!!!" with hpunch

        play sound s_moans

        "You've been fucking her hard for hours, filling her up with your hot cum. You lost count of the number of times you both came."

        you "I'm reaching my limit again..."

        "{color=[col]}Girl{/color}" "Don't! If you do, I'll... I'll..."

        with flash

        play sound s_scream_loud

        "{color=[col]}Girl{/color}" "AAAAAAAH!!!!" with hpunch

        show bg treasure_blonde sex5 at top with doubleflash

        "You shoot another load right into her cervix."

        play sound s_screams

        "{color=[col]}Girl{/color}" "AAAAAAH!!!"

        "The girl reaches her climax too, shaking and squeezing your cock hard inside her pussy, pulling you in."

        play sound s_orgasm

        "{color=[col]}Girl{/color}" "Amazing... Aaaah..."

        show bg treasure_blonde sex6 at top with fade

        "As you pop your cock out of her, a wad of cum starts overflowing out of her pussy."

        "{color=[col]}Girl{/color}" "Aaah, ah, aw... My belly is full of cum... You ruined my pussy..."

        you "Well, I did cum a lot... But you can take it."

        play sound s_mmmh

        "{color=[col]}Girl{/color}" "Aah... It's leaking out... Aw... *drool*"


    elif who == "pink":

        show bg treasure_pink sex1 at top with dissolve

        "Lifting the girl's frail body in the air, you spread her legs in front of your bedroom mirror."

        you "Look at that fresh, pink pussy... I bet you must be fed up with pleasuring yourself alone."

        you "You need a good, fat cock inside of you."

        "{color=[col]}Girl{/color}" "W-Wait!"

        play sound s_surprise

        "{color=[col]}Girl{/color}" "Aaaah!!!" with hpunch

        "You start rubbing your erect cock alongside her slit and clit, while licking her neck and ear."

        play sound s_mmh

        "{color=[col]}Girl{/color}" "Y-You... You make me feel strange... Aaaaah..."

        with hpunch

        play sound s_ahaa

        "{color=[col]}Girl{/color}" "My p-pussy... Feels strange... Ahaa..."

        "The girl is looking at her obscene reflexion in the mirror as you keep grinding your dick between her pussy lips. Her pussy is getting really wet."

        play sound s_surprise

        "{color=[col]}Girl{/color}" "Wait... Aaah!" with vpunch

        show bg treasure_pink sex2 at top with dissolve

        "Unable to wait any longer, you lift her hips into the air, landing her straight on your erect cock."

        play sound s_moans

        "{color=[col]}Girl{/color}" "Aaah, ah, aaah!!! It's too big!!!" with vpunch

        you "Hmmm, young girls like you are really tight... It's great..."

        "Not skipping a beat, you start fucking her, bouncing her petite body on and off your cock."

        "{color=[col]}Girl{/color}" "Ooh, it's too much! Oh! Oooh!!!" with vpunch

        "The girl moans wildly as you nail her mercilessly. She cannot hide her pleasure, however, as her pussy is overflowing with love juice."

        you "What a narcissistic, pervert bitch... You love being fucked in front of a mirror, don't you?"

        "{color=[col]}Girl{/color}" "It's not, ah, true, aaaah..." with vpunch

        you "Very well... Let's try a different position, then."

        play sound s_scream

        scene black with fade

        show bg treasure_pink sex3 at top with dissolve

        "Putting her upside down, you start pounding her pussy even harder."

        play sound s_screams

        "{color=[col]}Girl{/color}" "AAAAH!!!" with vpunch

        play sound s_moans

        "Her pussy makes hot, squishy noises as her love juice splashes around every time you shove your cock inside."

        you "It seems you like to be fucked hard... Maybe you want me to ruin your pussy tonight..."

        "{color=[col]}Girl{/color}" "N-No, aaaaah!!!" with vpunch

        "The girl blushes visibly, and her nipples harden. It seems she loves being talked down to, or maybe she loves the idea of being fucked senseless."

        you "Your pervert pussy doesn't lie... I'm going to fill you up with my sticky semen, prepare to receive it!"

        "{color=[col]}Girl{/color}" "W-What? Do you mean... Oooh..."

        play sound s_screams

        "{color=[col]}Girl{/color}" "Aah! Aaaah!!!" with vpunch

        "The girl tenses up as you fuck her harder and faster, watching your cock pounding in and out of her helpless pussy."

        with flash

        play sound s_scream_loud

        "{color=[col]}Girl{/color}" "AAAAAH!!!" with vpunch

        show bg treasure_pink sex4 at top with doubleflash

        "You cum hard inside her, filling her tight pussy with warm cum."

        play sound s_screams

        "{color=[col]}Girl{/color}" "Ah, ah, AAAAAAAAAH!!!"

        play sound s_orgasm

        with flash

        "She cums again hard, moaning as your semen starts overflowing out of her pussy."

        you "Man, what a horny bitch... It seems you got what you came for."

    $ unlock_achievement("h treasure " + who)

    scene black with fade

    $ MC.change_prestige(5)

    "You have earned prestige."

    return


## CARPENTER EVENTS ##

label meet_carpenter():

    $ story_flags["met carpenter"] = True

    scene black with fade

    show expression gallows.get_pic(config.screen_width, int(config.screen_height*0.8)) at top with dissolve

    $ text1 = season_text({"winter" : "to escape the chilling wind of winter", "spring" : "to go back to the lighter mood of spring", "summer" : "to escape the scorching heat of summer", "fall" : ", running from the sinister cries of eager crows"})

    "Passing by the gallows with your head tucked between your shoulders, you are only too happy to turn into a side street [text1]."

    "As you do so, you almost run headfirst into a girl, standing in front of a store."

    show carpenter with dissolve

    man "Get out of here, you ungrateful brat! Don't you ever come back!"

    play sound s_door_close

    "*SLAM*"

    play sound s_surprise

    carpenter "If I ever come back, it will be to gut you, you fucking pig!"

    play sound s_crash
    with vpunch

    "Pissed off, the girl hits the closed door with a vengeful kick."

    carpenter "Damn the ol' bastard..."

    you "*clear your throat*"

    carpenter "..."

    you "Ahem, it's none of my business, but... What's going on here?"

    carpenter "What's going on? That old fart who calls himself a master carpenter took me as an apprentice a month ago. And now, I quit! Screw him."

    you "Why did you quit?"

    carpenter "Well aside from the fact that he couldn't keep his hands to himself, which was bad enough, I just found out what kind of 'work' he's really doing here..."

    you "What work?"

    carpenter "He made me saw planks all day, and for what? It turns out he's making caskets for the prison guard. For the hangings!"

    $ MC.say(["gd: That's terrible.", "ne: Well, that's unfortunate, but a job is a job, isn't it?", "ev: So what. What's your problem with that?"])

    carpenter "I won't be part of this! It's bad enough that the guard is harassing everyone and that justice is in the hands of corrupt puppets..."

    carpenter "But the gallows? It's the worst. How many innocents have they hanged by the neck for nothing? How many petty criminals have they sent to their deaths while they're rolling in bribe money?"

    "The woman's face is flushed. She is clearly indignant."

    carpenter "Fuck that!"

    "Although her manners are coarse, she is very pretty. She's got a nice pair of knockers too, which you're trying to get a better look at."

    carpenter "I'm Iulia, by the way... Who are ya?"

    $ carpenter_name = "Iulia"

    "She eyes you a bit suspiciously."

    you "I'm [MC.name]. Nice to meet you. I've only arrived in Zan recently, so I'm not well acquainted with the politics of this place..."

    "She seems relieved to hear you are not a part of Zanic society."

    you "What are you going to do now?"

    play sound s_sigh

    carpenter "Well, wasn't much of an apprenticeship really... But I need to find a new place to work."

    "She looks at you with hopeful eyes."

    carpenter "Ya wouldn't happen to have a job for me, would you?"

    you "Well, sure! I have a brothel in town, and we're always hiring. How well can you suck a dick?"

    carpenter "Whaaaat?!?" with vpunch

    "She blushes bright red."

    carpenter "No, not that kind of job! You misunderstood me!!!"

    carpenter "I need to use my skills... I mean my {i}woodworking{/i} skills... Wait, that came out wrong!"

    carpenter "My building skills. I can work with all kinds of material, not just wood. I like to think of myself as a kind of Renaissance artist, ya know."

    you "Er... No, I don't..."

    carpenter "'nyway. I can build and fix things, I can make myself useful anywhere. But I won't be sucking dicks."

    you "That's a shame... {nw}"

    if story_flags["found wagon"]:
        extend "But I might have another opportunity for you."

        carpenter "Oh, really?"

        you "Let me explain..."

        call hire_carpenter() from _call_hire_carpenter_1

    else:
        extend "I'll let you know if I hear of any job opening for a carpenter. That's not exactly my line of business, though."

        carpenter "Yeah, thanks. I live down the street, if you need to find me."

        carpenter "Anyway, I'm sure I'll be able to get a job in no time, hahaha..."

        "Her boast lacks confidence."

        you "I'll see you around, then."

        carpenter "Sure. Now if ya'll excuse me, I'm just going to fling a rock into that asshole's window. You might not want to stay here."

        scene black with fade

        play sound s_shatter

        you "That woman sure got a temper. She is a looker, though..."

    return


label wagon():
    if not story_flags["found wagon"]:
        call wagon_first_visit() from _call_wagon_first_visit
    elif not story_flags["met carpenter"]:
        "You have no use for this old wagon right now. You must find a carpenter first."
    else:
        jump furniture

    jump brothel


label wagon_first_visit():

    $ story_flags["found wagon"] = True

    scene black with fade
    show expression bg_bro at top
    with dissolve

    play music m_nature fadein 3.0

    "Today, you take Sill out to explore your new backyard."

    you "Wow, it's a jungle out here... Look how tall that grass is."

    you "Uh? Look, Sill, there's something over there!"

    "You notice some kind of carriage, half-buried in the vegetation."

    hide expression bg_bro
    show bg wagon at top with dissolve

    you "Uh? What is this..."

    show sill with dissolve

    sill happy "It's an old wagon... Maybe left over by gypsies?"

    you "Well, it looks like it's been abandoned for a while. I don't think they'll come back for it."

    sill "It's on your premises anyway, Master, so that makes you the owner!"

    you "Great, just what I needed... An old decrepit wagon, what the hell could I do with it?"

    "Suddenly, you're overrun with a strange thought. What if you were diagnosed with cancer, and you needed to make money fast?
    Maybe you could use your chemical knowledge to make crystal-spice out of that old trailer."

    "But then you would run into some Kroxican gangsters and have to get rid of the bodies..."

    sill "Master?"

    "Sill interrupts your pointless revery."

    sill "Its not so run down... Look inside, Master!"

    "Carefully, you open the wagon's door, half expecting to find some dead Kroxicans on the floor. You are relieved to find cramped living quarters and a kind of workbench instead."

    you "There are some tools here... Crude ones. It must have been used by a craftsman of some sort."

    sill "That makes sense. Craftsmen usually roam the land, looking for customers."

    sill "When we found this place, Gio told us it belonged to a retired workman. Maybe that's where he used to practice?"

    you "Maybe. Those look like woodworking tools... There are others, I don't know what they're for."

    sill "Hmm... Master, what should we do?"

    you "Without horses, it's going to be a pain to move this. I must give it some thinking."

    hide bg
    hide sill

    if brothel.get_common_rooms():
        $ room = brothel.get_random_room_pic_path()
    else:
        $ room = "black"

    show expression room at top
    with dissolve

    stop music fadeout 3.0

    "Moving back into the brothel, you keep thinking about what to do with the old wagon."

    you "What should we do with an empty craftsman trailer?"

    "Pondering this, you sit absentmindedly on an old rocking chair."

    play sound s_creak

    you "I could design a pimpmobile... Let me think..."

    play sound s_creak

    you "It would need hydraulic suspensions, of course... And... Uh?"


    play sound s_crash

    with vpunch

    "*CRACK*"

    sill sad "Master! Are you ok?"

    show sill with dissolve

    you "Ouch! Damn it!"

    "The rocking chair crumbled from under you, and you hit your butt hard on the dusty floor."

    you "Man, this place sucks... All the furniture is shitty! *frown*"

    sill "Did you hurt yourself?"

    you "No, but it's a pain in the butt... Literally."

    you "Hehe."

    you "Get it? A pain in the butt! Hahahaha!!!"

    sill "Are you sure you didn't hit your head instead?"

    sill happy "Your jokes are even more terrible than usual..."

    you "Hey..."

    sill "Master, you know, I think this place really needs some new furniture."

    you "Shut up, Sill! Let me think... I'm on the verge of having an idea..."

    you "I know what we must do!" with vpunch

    you "What this place needs is... {w=1.0}{b}new furniture{/b}!!!"

    sill sad "I just said that..."

    you "Come on, I know you're upset you couldn't come up with it yourself. But stick around with me, and you'll learn."

    sill "..."

    you "We could buy some from the furniture market..."

    sill sad "More things to buy? But Master, we don't have the money... I still have to pay the water bill..."

    you "The water bill? We have running water?"

    sill happy "That's right! Isn't it a big improvement?"

    you "I don't know... All this modern technology sounds like a fad to me."

    you "Our grandparents never had any of this fancy running water, and they didn't complain... Apart from the occasional plague, but they always exaggerated these things."

    sill "Master, I've got an idea!"

    you "Again? I hope it's better than your last one! Your stupid furniture idea was going to ruin us!"

    sill sad "B-b-but..."

    sill happy "Master, listen."

    sill "We have a worksman's wagon parked outside, right?"

    you "Yes... I hope you're not going to suggest DIY. I hate DIY."

    sill happy "I've heard that you can find many building resources in the city, did you know that?"

    if story_flags["discovered resources"]:

        you "Uh? Oh yes, I did. As a matter of fact, I found some the other day: look."

        sill "Oh, wonderful!"

    else:

        you "Building resources?"

        sill "Yes, there are places in town where a honest worker can harvest building resources relatively easily."

        you "A honest worker? I've heard the term, yes... I'm not terribly familiar with it..."

    sill "Anyway. If we gather enough resources, I'm sure we could have some custom-made decoration built on the cheap!"

    you "Hmm... Maybe. But we don't have the skillset! Do you know how to make furniture?"

    sill sad "Well, uh, no..."

    sill "If only we knew a skilled craftsman... We could offer to rent the wagon and tools to him in exchange for free help..."

    you "A woodworker of some sort... Maybe a carpenter..."

    you "A carpenter... Hmm..."

    if story_flags["met carpenter"]:
        you "I know just the one! I met her near the gallows. She was in need of a job."

        sill happy "Well, that's great! Maybe she's still there!"

        you "I'll go and check on her. I can't wait to get started on upgrading this place!"

        sill "Me too! Aw, I hope she'll accept..."

        call hire_carpenter from _call_hire_carpenter

    else:
        sill "There must be someone willing. In a city this big..."

        you "I'll have to keep my eyes opened for one."

        "You sigh, unsure you want a big, scruffy workman to move into your backyard, ogling your girls."

    scene black with fade

    return


label hire_carpenter():

    scene black with fade
    show bg wagon at top with dissolve

    you "This is the place."

    show carpenter at totheright with dissolve

    carpenter "Oh... I was expecting something... Bigger?"

    you "Yeah, I get that a lot... Ahem."

    you "Anyway. Take a look inside, see what you can do with it. It's surprisingly comfy for its size."

    "You are only half-lying. The wagon does look bigger on the inside."

    carpenter "Hmm, there are quite a few tools I could use. They've seen better days, but they look sturdy."

    you "That's cool."

    carpenter "So, tell me about your offer again?"

    you "Stay here with us. You can sleep here and eat with the girls for free."

    you "In exchange, you can build some items for us with the spare resources I find. Much more rewarding than making caskets."

    carpenter "I see... But how do I make a living? Free lodging is good, but I still need to make money..."

    you "You can sell your stuff to the customers when they visit the brothel. There are always plenty of them every night."

    "She frowns."

    you "I don't mean selling your stuff in {i}that{/i} way! Whatever extra furniture and trinkets you make can be sold."

    play sound s_sigh

    carpenter "Hmm..."

    "Iulia seems lost in her thoughts, giving your offer some consideration."

    carpenter "A' right, seems fair enough. I'll move in with you guys."

    you "Yes!"

    "There was something a little too enthusiastic about your response."

    carpenter "But on one condition."

    you "Yes?"

    carpenter "I want to be on equal terms with you. I won't be molested again."

    carpenter "So, pimp or not, you better keep your hands where they belong, or I'll smash your head in."

    you "*gulp* Fair enough..."

    "Having just threatened to kill you, she gives you a big smile."

    carpenter "It's a deal, then! I'll move in immediately!"

    you "Welcome aboard!"

    scene black with fade

    "Iulia has moved into your brothel. You may now build various types of furniture at the {b}carpenter's wagon{/b}."

    show expression bg_bro at top with dissolve
    show sill with dissolve

    sill "Master! Welcome back!"

    sill "I've found a few pieces of decoration that could still be useful... You might want to have a look."

    scene black with fade

    "You have received some furniture. New {b}brothel options{/b} are accessible."

    # $ carpenter_active = True
    $ NPC_carpenter.active = True
    $ unlock_achievement("wagon")

#    $ calendar.set_alarm(calendar.time+1, StoryEvent(label="iulia1", type="morning"))

    return


label iulia1():

    scene black with fade

    "You wake up in the early morning, hearing some distant clanging sounds."

    "Opening your back window, you see Iulia is hard at work on the furniture you ordered."

    show bg wagon at top with dissolve

    show carpenter attack with dissolve

    play sound s_clash

    "*CLANG*"

    play sound s_clash

    "*CLANG*"

    "Iulia is banging on some rivets with a very large hammer, looking genuinely happy about her work."

    play sound s_clash

    carpenter "HA!!!"

    "She waves the hammer like it weighs nothing. You wouldn't suspect such strength in such a pretty woman."

    carpenter "Lalalala..."

    "She's even... Singing?"

    "But what really holds your attention however, is that she is working... In her underwear!"

    # Add special effect

    you "*GULP*"

    carpenter "Lala... Oh, hello, [MC.name]? How are ya this morning?"

    you "I'm... Good... Thank you. It seems I'm really hard- I mean, you're really hard at work, hahaha..."

    carpenter "Yeah, I always get too hot when I work up a sweat. I figured since this place is a brothel anyway, no one would mind me working in my underwear."

    "She takes a towel and wipes beads of sweat that are running between her big tits. You gasp audibly."

    carpenter "But if that's a problem, I can dress more properly if you want."

    you "N-no, it's fine, really... It's just, hem, some of our customers are a bit wild. Aren't you worried someone will get the wrong idea and assault you?"

    play sound s_laugh

    carpenter "Nah, of course not! I'd crush their balls with my hammer if they even try."

    you "*gulp*"

    "You remember you promised Iulia never to molest her. Given her skill with a hammer, it's probably for the best."

    scene black with fade

    return


## BAST EVENTS ##

label resource_exchange_intro():

    scene black
    show bg market at top
    with fade

    play music m_market fadein 3.0

    "As you visit the colorful maze of the Zan general market, you notice a large building overlooking the main square."

    "Curious, you make your way towards the building and see that it is an exchange of sorts. Carts and animals loaded
    with goods come in and out of the building in a steady flow."

    play sound s_crowd_riot

    "As you step inside, rubbing elbows with shouting traders and busy haulers, you notice a worried-looking girl in a guild uniform,
    overseeing the whole mess."

    show bast with dissolve

    bast "Sir! You cannot park your donkey here. And you! Marble is stored in the back, you can't leave it here!"

    "The girl has a powerful voice, and everyone seems to begrudgingly follow her orders. She seems to be in charge."

    bast "All right people, BREAK!!!"

    stop sound fadeout 2.0

    "As soon as the girl announces a break, the crowd disperses and heads for nearby food and spice stalls."

    "As the noise dies down, the girl looks relieved and starts going through a wad of paperwork. She doesn't notice you standing right in front of her."

    you "*clear throat* Excuse me..."

    bast "Yes? Are you a trader? This is break time, come back in one hour..."

    if MC.playerclass == "奸商":
        "She goes back to her paperwork, thinking you are one more merchant to be dealt with later."

        you "Sorry to interrupt, really. I had a few questions."

        "She lifts her head again, sighing."

    else:
        "She gives you a second look, and notices you don't look anything like a trader. She frowns."

    play sound s_sigh

    bast "What do you want?"

    $ NPC_bast.met = True

label resource_exchange_menu():

    menu:
        bast "What do you want?"

        "你是什么人?":
            you "Who are you?"

            bast "I'm Bast. I'm the quartermaster here. Or, quartermistress. Whichever floats your boat."

            you "I'll... I'll just call you Bast."

            $ bast_name = "Bast"

            bast "Sure, whatever."

            you "Are you with a guild of some sort?"

            bast "Of course. I'm a holy builder."

            you "A... Holy builder?"

            bast "Yeah. Never heard of us?"

            you "Nope."

            bast "We used to be a secret society among builders. Builders are a tight-knit community, and we prefer to handle our own affairs."

            bast "We haven't got much use for traditional religion, but we value experience and craftsmanship."

            bast "We elect holy builders among our rank to manage our day-to-day business, settle disputes, and conduct the service every Tuesday and Friday."

            you "I see... More or less."

            you "So you've been elected by your peers? Nice, you must be popular..."

            bast "Not exactly. Holy builders have to deal with all the chores... No one wants to do it. I was the only one running."

            you "Oh. Why did you run, then?"

            bast "I was made to... You see, I was young and inexperienced, and I screwed up, badly. This was the only way to atone for it."

            you "Really? What happened?"

            "Her mood darkens."

            bast "Well... Nothing you need to be concerned with. *frown*"

            bast "Anyway, you didn't come here only to chat?"

        "这里是什么地方?":

            bast "This is the resource exchange! The biggest one of its kind in Zan, and maybe the world. I wouldn't know about that."

            you "What do you do here?"

            bast "We exchange a wide range of building goods for the convenience of builders in the city."

            bast "If you have too much of one resource, not enough of another, or simply want to buy or sell resources with hard cash, this is the place."

            you "Resources?"

            bast "Building resources. Wood, leather, that sort of thing."

            you "Are the rates good?"

            bast "Well, they're good enough, I guess. Trading here is better than selling and buying resources for gold, that's for sure."

            bast "But we do take our cut, of course."

            bast "That said, price depends on supply and demand... It changes every week."

            bast "Sometimes, prices are driven up for a given resource when we have a shortage. Sometimes they are driven down, when the resource is plentiful."

            you "I see..."

            bast "Is that all?"

        "我可以在这里和别人交易吗?" if not story_flags["builder license"]:

            you "I want to trade resources here. Can I?"

            bast "Why, sure."

            you "Yay!"

            bast "There's just the small matter of registration..."

            you "Uh? Registration?"

            bast "Yes. A holy builder has to grant you a proper license before you can trade resources here."

            you "A holy builder? That means... You?"

            bast "Yep."

            you "All right! Can I get one? Please?"

            bast "Sure, but not for free."

            you "Damn. I figured you might say that."

            bast "You need to contribute to our emergency stockpile before I can give you a basic builder license."

            bast "That would be 5 bundles of wood, 5 wads of leather, and 5 batches of dye."

            you "I see..."

            if MC.has_resource("wood", 5) and MC.has_resource("leather", 5) and MC.has_resource("dye", 5):
                if renpy.call_screen("yes_no", "Do you want to get a basic builder license for 5 wood, 5 leather and 5 dye?"):
                    $ MC.resources["wood"] -= 5
                    $ MC.resources["leather"] -= 5
                    $ MC.resources["dye"] -= 5
                    $ story_flags["builder license"] = 2

                    bast "...three, four, five... Alright. Thanks. Here is your builder license."

                    "You have received a {b}basic builder license{/b}."

                    bast "You can now trade common resources like wood, leather and dye here."
            else:
                bast "It doesn't seem like you have those resources with you now. Come back later, maybe?"

        "没事了":
            you "Ok, I'll leave you to... whatever it is you're doing."

            bast "Yeah. See ya."

            hide bast with dissolve
            scene black with fade

            $ bast_name = "Bast"

            return

    jump resource_exchange_menu


label exchange_come_back():

    scene black
    show bg market at top
    with fade

    show bast with dissolve

    bast "Oh, it's you again. Did you have any more questions?"

    call resource_exchange_menu() from _call_resource_exchange_menu

    return


label new_builder_license():

    bast "Hi! I have a new builder license to offer, if you're interested."

    menu:
        bast "Do you want an upgraded builder license?"

        "告诉我详细信息":
            you "Upgrade my license? What for?"

            if story_flags["builder license"] == 2:

                bast "Right now, you can only trade common resources at the exchange."

                bast "But if you subscribe to an advanced builder license, you can deal with rarer and more expensive resources, like marble, silk and ore."

                you "I see."

                bast "The cost is 5 blocks of marble, 5 rolls of silk, and 5 chunks of ore."

                if MC.has_resource("marble", 5) and MC.has_resource("silk", 5) and MC.has_resource("ore", 5):
                    if renpy.call_screen("yes_no", "Do you want to get an advanced builder license for 5 marble, 5 silk and 5 ore?"):
                        $ MC.resources["marble"] -= 5
                        $ MC.resources["silk"] -= 5
                        $ MC.resources["ore"] -= 5
                        $ story_flags["builder license"] = 3

                        bast "...three, four, five... Alright. Thanks. Here is your builder license."

                        "You have received an {b}advanced builder license{/b}."

                        bast "You can now trade rare resources like marble, ore and silk."

            elif story_flags["builder license"] == 3:

                bast "If you want to trade diamonds, the most valuable building resource, you will need a master builder license."

                bast "It's quite costly... I require 2 diamonds."

                you "Two diamonds! *cough* *cough*"

                bast "Yep. But diamond traders make the most money. Consider this an investment."

                if MC.has_resource("diamond", 2):
                    if renpy.call_screen("yes_no", "Do you want to get a master builder license for 2 diamonds?"):
                        $ MC.resources["diamond"] -= 2
                        $ story_flags["builder license"] = 5

                        play sound s_sigh

                        bast "Ooh... Shiny! Thanks. Here is your builder license."

                        "You have received a {b}master builder license{/b}."

                        bast "You can now trade diamonds at the resource exchange."

        "我确实很想":
            you "I want to upgrade my license."

            if story_flags["builder license"] == 2:

                bast "The cost is 5 blocks of marble, 5 rolls of silk, and 5 chunks of ore."

                if MC.has_resource("marble", 5) and MC.has_resource("silk", 5) and MC.has_resource("ore", 5):
                    if renpy.call_screen("yes_no", "Do you want to get an advanced builder license for 5 marble, 5 silk and 5 ore?"):
                        $ MC.resources["marble"] -= 5
                        $ MC.resources["silk"] -= 5
                        $ MC.resources["ore"] -= 5
                        $ story_flags["builder license"] = 3

                        bast "...three, four, five... Alright. Thanks. Here is your builder license."

                        "You have received an {b}advanced builder license{/b}."

                        bast "You can now trade rare resources like marble, ore and silk."

            elif story_flags["builder license"] == 3:

                bast "It will cost you 2 diamonds. I don't wanna know how you get them..."

                if MC.has_resource("diamond", 2):
                    if renpy.call_screen("yes_no", "Do you want to get a master builder license for 2 diamonds?"):
                        $ MC.resources["diamond"] -= 2
                        $ story_flags["builder license"] = 5

                        play sound s_sigh

                        bast "Ooh... Shiny! Thanks. Here is your builder license."

                        "You have received a {b}master builder license{/b}."

                        bast "You can now trade diamonds at the resource exchange."


        "不必了，我只是来做交易的":
            pass

    return


label trade_x_resources(x):

    if NPC_bast.flags["last event"] == calendar.time:
        pass
    elif x >= 10 and not NPC_bast.flags["bast 10 resources"]:
        call trade_10_resources from _call_trade_10_resources
        $ NPC_bast.flags["bast 10 resources"] = True
        $ NPC_bast.flags["last event"] = calendar.time
        return True
    elif x >= 25 and not NPC_bast.flags["bast 25 resources"]:
        call trade_25_resources from _call_trade_25_resources
        $ NPC_bast.flags["bast 25 resources"] = True
        $ NPC_bast.flags["last event"] = calendar.time
        return True
    elif x >= 50 and not NPC_bast.flags["bast 50 resources"]:
        call trade_50_resources from _call_trade_50_resources
        $ NPC_bast.flags["bast 50 resources"] = True
        $ NPC_bast.flags["last event"] = calendar.time
        return True
    elif x >= 100 and not NPC_bast.flags["bast 100 resources"]:
        call trade_100_resources from _call_trade_100_resources
        $ NPC_bast.flags["bast 100 resources"] = True
        $ NPC_bast.flags["last event"] = calendar.time
        return True

    return False

label trade_10_resources():

    hide screen resource_exchange

    bast "8, 9, 10... Well, that's a bunch."

    bast "Good to see you are using your license."

    menu:
        "赞美她":
            $ renpy.block_rollback()

            you "Well, to be honest, I mostly come here to see you..."

            bast "Uh? What do you mean?"

            you "Well, obviously, you're super hot. And your guild uniform... I have a thing for uniforms."

            "She looks at you, unimpressed."

            bast "Well, if that's your reason for coming and doing business here, I'm not going to argue with that."

            bast "But don't get your hopes too high. I get hit on all the bloody time, and I have no patience for it. *frown*"

            $ NPC_bast.love -= 1

        "问一些私人话题":
            $ renpy.block_rollback()

            you "You said you were a Holy Builder, correct?"

            bast "Yes."

            you "You mentioned something about being elected to atone for your mistake... Can you tell me what happened?"

            bast "What's it to you?"

            you "Well... Curiosity, I guess. I just wanted to know you better."

            bast "That's not a topic I want to talk about."

            $ NPC_bast.love += 1

        "请求优惠":
            $ renpy.block_rollback()

            you "So, I've been a good customer, eh..."

            you "Can I get a rebate?"

            bast "No."

            you "Please?"

            bast "No."

            you "What if I traded more with you?"

            bast "Sure, why don't you do that first."

    play sound s_chimes

    bast "Hey, you! Where do you think that camel is going!"

    bast "Sorry, I'm busy. Catch you later."

    return

label trade_25_resources():

    hide screen resource_exchange

    bast "Over 25 resources... That's a lot to trade in one go! Well done."

    you "Yes. It's like we've reached a new stage in our relationship."

    bast "Err... Yes. Our {i}business{/i} relationship."

    you "I think I deserve a reward."

    menu:
        "让她给你一个香吻":
            $ renpy.block_rollback()

            you "Why not give me a big kiss to celebrate our friendship? Come to daddy..."

            bast "One step closer and I'll stab you."

            you "*gulp*"

            $ NPC_bast.love -= 1

        "让她说说她的过往":
            $ renpy.block_rollback()

            you "Look, I know you don't like to talk about your past..."

            bast "I don't. Piss off..."

            you "Wait, wait, I'm not going to ask about that. But I was wondering if you could tell me more about you... Maybe something about your duties? As a Holy Builder?"

            "Bast relaxes a little."

            bast "You're pretty damn curious, aren't you?"

            bast "Well..."

            bast "The elders like to say that Holy Builders are the cornerstone of our community, but that's just a load of bullcrap. We're essentially a bunch of menial servants, always willing to do the odd jobs no else wants."

            bast "At least that's how it goes in Zan, where I've been the one and only Holy Builder for the past 5 years. Maybe other Holy Builders have it better. I don't know."

            you "But... These 'elders' of yours... What do they do?"

            play sound s_evil_laugh

            "She laughs harshly."

            bast "Why, they just sit on their ass, sleeping during service, boozing the rest of the time..."

            bast "But they do remember to collect all the money I make every Sunday, of course... Not that I would have any use for it. The Order provides food and shelter, at least."

            you "You seem very bitter. Why stay?"

            bast "Well, I..."

            play sound s_sigh

            bast "I'm sorry, that sounded too harsh. I owe a lot to the Order. I shouldn't bad-mouth the elders. Please forget it."

            you "You're still not going to tell me what happened to put you in this situation?"

            bast "Nah. I barely know you. Maybe another time."

            $ NPC_bast.love += 2

        "获得一些免费物资":
            $ renpy.block_rollback()

            you "As I am such a good customer, perhaps I should be rewarded?"

            bast "A reward, uh?"

            bast "Well, I've got some leftovers from the last caravan. You can pick what's useful to you. Saves me the trouble of cleaning up."

            $ MC.gain_resource("wood", dice(6) + 2)
            $ MC.gain_resource("dye", dice(6) + 2)
            $ MC.gain_resource("leather", dice(6) + 2)

    bast "Now, if you'll excuse me, I've got some traders from Borgo to attend to."

    return

label trade_50_resources:

    hide screen resource_exchange

    bast "50 resources exchanged at once... Color me impressed. You've come pretty far."

    you "I have a lot of hidden resources..."

    bast "I didn't think so at first, but now I'm inclined to believe you."

    menu:

        "约她出去":
            $ renpy.block_rollback()

            you "I think we should celebrate. Why don't you take some time off and join me for drinks, or dinner?"

            "She looks at you warily."

            bast "I don't like to be hit on on the job..."

            you "Come on, I'm just asking you to take off from work for a little while. Just a night out. No strings attached."

            bast "..."

            if NPC_bast.love > 0:

                "Bast looks around at the busy marketplace, hesitating. She looks old beyond her years. She seems exhausted."

                you "Let someone else take care of business for today. Give yourself a break."

                bast "Well..."

                bast "I guess this place can survive without me for a few hours. All right, where do you want to go? I never take a break, so I wouldn't know any trendy place..."

                you "Let us check this little tavern by the docks..."

                scene black with fade

                "..."

                show bg street night with fade

                show bast with dissolve

                bast "Well, it was nice. I rarely catch a break from work."

                you "So it seems. This Holy Builder position seems like a chore..."

                bast "It is. But I brought it on myself, so I have no reason to complain."

                you "Have you, now? You still haven't told me the story."

                "Her mood darkens, and she stays silent for a while. Just when you think you should move on to another topic, she starts talking."

                play sound s_sigh

                bast "Well... *sigh*"

                bast "I joined the order of builders as a teenager. I knew nothing about life, but I was good with my hands, so I was very enthusiastic about joining."

                bast "The builders are like a tight-knit family... For me, a street orphan, it was a wonderful and new experience."

                bast "I didn't have any experience with men either..."

                "She stops for a while and looks up at the night sky."

                bast "I met a guy one market day, he was quite the talker. He was a trader of sorts, and he started complimenting me on my boobs."

                bast "At first I was shocked, but then I started enjoying the attention. I had gotten looks from some of the brothers, but someone approaching me so directly was a breath of fresh air."

                bast "I let him court me... I was aware he was good with words, and a womanizer, but I didn't really care... I liked how he made me feel."

                bast "So we started dating, and it was... wild. Intense. Physically speaking. Like, we were having sex everywhere, all the time..."

                you "Okay, okay. I get it."

                bast "Days went by, and he was asking me questions. Lots of questions, about my order, my brothers and sisters, the location of our buildings..."

                bast "I was completely blind. I felt so close to him that I didn't even see what was wrong. I just told him whatever he wanted to know."

                bast "One day, I woke up alone. I came in to work, to find our main warehouse had been raided during the night, just after the biggest caravan of the year had come into town."

                bast "We lost tens of thousands of denars worth of merchandise... Worst of all, we quickly discovered my lover was the one who did it."

                bast "He vanished with his booty, and I've never seen or heard from him since."

                bast "I confessed my mistakes to the order, and I was scolded harshly, rightly so."

                bast "But the brothers and sisters took pity on me, as I was heartbroken and hopeless... So they made me the Holy Builder as a punishment."

                bast "I've been doing it for 5 years straight now. Thinking about it, this must be the first time I took half a day off."

                you "You've been driving yourself way too hard..."

                bast "It was a way to dull the pain..."

                bast "After all these years, you know what hurts the most?"

                bast "It's not the lying, the betrayal, the thought that I have been used..."

                bast "But he didn't say goodbye. He didn't leave a note, or make up an excuse that he had to go. Not even a handkerchief left to remember him by..."

                you "That's cruel..."

                bast "It's been five years, and I'm trying to convince myself that I am over him. But that part will always hurt."

                you "..."

                "Not knowing what to do, you simply move towards Bast and start hugging her."

                bast "..."

                "She tenses up at first, but she doesn't fight you. You can feel her large chest pressing against you and struggle to repress an erection."

                "Ignoring your body's reaction, she relaxes gradually. After a while she breaks the embrace. You can see her cheeks are wet."

                bast "Oh, my, look at the time... I must go prepare the schedule for tomorrow's deliveries."

                bast "I had a nice time. Thank you."

                you "I'm glad you did."

                bast "I'll see you around at the market."

                you "Don't work yourself too hard, okay?"

                "For the first time since you've known her, she smiles."

                "She looks at you for a moment, as if thinking about something new."

                bast "..."

                bast "You're an all right guy. Take care."

                "She waves you a quick goodbye, turns around and leaves abruptly."

                $ NPC_bast.love += 3

            else:
                bast "Sorry, but I don't know you. I try to watch the company I keep."

                you "Ouch..."

                $ NPC_bast.love += 1


        "摸摸她的胸部":
            $ renpy.block_rollback()

            you "As my reward, I choose... Fondling your juicy boobies!"

            play sound s_surprise

            you "Come here... *drool*"

            play sound2 s_punch
            with vpunch

            "Matter-of-factly, Bast grabs you by the shoulders and knees you right in the balls."

            play sound s_wscream

            you "AAAHOOYAOUCH!!!" with vpunch

            scene black
            with Fade(0.15, 0.3, 0.15)
            show bg bast titjob0 at top with dissolve

            "Through tears of pain, you still manage to catch a glimpse of her cleavage, peeking at her ample bosom and her perky nipples, rubbing against her white tunic."

            scene black with circlein

            you "Worth... it... *pass out*"

            show bg market at top
            with circleout

            "You wake up crumpled in the dust in front of the market. You crawl back home, your nuts hurting like hell."

            $ NPC_bast.love -= 1

        "免费的高级物资":
            $ renpy.block_rollback()

            you "I'd like some advanced resources as a reward. I'm sure you can spare some."

            play sound s_sigh

            bast "I knew you would try and bargain... *sigh*"

            bast "Fine. There's a bunch of resources left from a caravan whose owner got busted by the knights for dealing spice in the upper quarters."

            bast "Take only what you need. I don't expect to see the fella again, but I don't want you to attract attention."

            $ MC.gain_resource("marble", dice(6) + 2)
            $ MC.gain_resource("silk", dice(6) + 2)
            $ MC.gain_resource("ore", dice(6) + 2)

            "Bast lets you leave by a side gate, carrying the extra resources in a covered cart."

    $ calendar.set_alarm(calendar.time, StoryEvent(label = "bast_informant", type = "night"))

    return

label bast_informant():

    scene black with fade
    show expression bg_bro at top with dissolve

    "As you approach [brothel.name], you hear a voice whisper to you."

    show expression "events/" + security_pics["hood"][0] at top:
        zoom 1.025

    with dissolve

    "A hunchbacked stranger in dirty travelling garb emerges from the shadows and grabs you, his bony hands digging in your arm like claws."

    "As he is about to speak, a fit of coughing makes his voice croak."

    "Stranger" "Listen-n-n... *cough* *cough*"

    "Horrified, you realize the man suffers from the desert pox, a terrible disease common among spice addicts."

    "The man is still holding you. Between coughs and the wheezing sound of his difficult breathing, he manages to slip out a few words."

    "Stranger" "You... *cough* You're interested in the market girl's past... *cough* *cough*"

    "Stranger" "C-c-correct? *cough*"

    "You are desperate to see him go, but his words stop you in your tracks. Is he talking about Bast?"

    you "Let go of my arm. I'm listening."

    "A croaking sound comes from under the man's hood. A laugh of sorts."

    "Stranger" "I knew it! *cough* The bitch is still as hot as ever... *cough*"

    "Stranger" "Here, I have some information about her that's worth a lot to her. You could ruin her with this... *cough*"

    "You give him a skeptical look."

    you "And how did you come across such important information? Why not take it to her directly, if it's so valuable?"

    "Stranger" "*cough* I wasn't always like this... Bast and I had... Had a falling out of sorts."

    "Stranger" "I was once strong, and handsome... Look at me now..."

    "The voice of the degenerate becomes high-pitched as he whines about his wasted life."

    "Stranger" "I ne-e-e-d spice... I need more... Give me the coin! Q-q-quick... I'll give you the letter!"

    you "You have it with you?"

    "Stranger" "Y-y-yes... 1000 denars, no less... And the bitch is y-y-yours... *cough*"

    menu:
        "What do you do?"

        "接受提议(1000 gold)":
            $ renpy.block_rollback()
            $ MC.gold -= 1000

            play sound s_gold

            "You give the man {b}1000 gold{/b}."

            you "This is a hefty price. The information has better be good."

            "Stranger" "Oh yes, my prince, yesss... *cough* Gimme, gimme the g-g-gold..."

            "His rapacious hands are shaking as he grabs the gold purse you hand him with a disgusted frown."

            "He takes out an old, crumpled envelope. Just before giving it to you, he seems to hesitate for a second, but then grunts and lets it go."

            "Stranger" "Gold, oh brother, I got me some g-g-gold..."

            "You catch a glimpse of his bloodshot eyes as he grins foolishly."

            "Stranger" "Spice! Quick, I want spice... Oh, poor Billy needs the spice..."

            "The man stumbles away in a side street, heading towards the spice market."

            if MC.get_alignment() == "good":
                you "Poor soul..."
            elif MC.get_alignment() == "neutral":
                you "Sick bastard..."
            else:
                you "Dirty dog. I should have cut his arm off."

        "拒绝请求":
            $ renpy.block_rollback()

            you "Whatever information you think you have, I won't pay you."

            "Stranger" "B-b-but..."

            you "Leave me the fuck alone. Find someone else to do your dirty deals."

            "Stranger" "F-fine! I'll find someone who's interested in this... I don't need you!"

            "He spits at your feet, and stumbles in a side street, out of view."

            if MC.get_alignment() == "good":
                you "Poor guy's only a month from the grave, by the looks of him... *shiver*"
            elif MC.get_alignment() == "neutral":
                you "Good riddance. At the rate he's going, he'll be dead before he can find a buyer anyway."
            else:
                you "Filthy son of a... I should have killed him when I had the chance."

            return

        "杀人灭口":
            $ renpy.block_rollback()
            $ MC.evil += 3

            you "All right then."

            "After making sure no one is around, you reach for something under your cloak. The man inches closer, his hands shaking with greed."

            play sound s_sheath

            with flash

            pause 0.2

            play sound2 s_sheath

            "Grabbing his neck, you plunge a dagger between his ribs."

            play sound s_crash
            with vpunch

            "Death catches the man instantly, and he falls inert in the dirt with a surprised look on his pox-ridden face."

            "Using a clean cloth, you wipe the blood from your dagger carefully, before searching the man's coat."

            "You find an old envelope, a woman's writing still visible under the grime."

            you "This must be it."

            $ NPC_bast.flags["killed_bast_ex"] = True

    scene black with fade
    show expression brothel.master_bedroom.get_pic(x=config.screen_width, y=config.screen_height) at top
    with dissolve

    "Back in your room, you carefully open the old letter."

    play sound s_dress

    call screen letter(header = "Love letter", message = "Dear Bill,\n\nI haven't slept or eaten since you've left me. I am so alone in this world.\nYou've left me with so many questions. Did you ever love me?\nI will be punished for what you did, but it's punishment I will gladly accept, because I love you. All I want is for you to give me a sign. I'll betray the Order if I have to. I'll steal for you if I must.\n\nDon't leave me, my love. I will do anything.",
                          signature = "Yours forever, Bastia {font=[style.default.font]}{size=-18}")

    you "Well... Sounds like she was quite taken with the guy..."

    "You think about the dying wreck of a spice junkie you saw earlier."

    you " Could it be that he..."

    you "Anyway."

    "Thinking about the letter, you realize how important its content is for Bast."

    you "She even wrote that she would betray the builders guild for him..."

    you "She was just a lovelorn girl, I guess. but in the wrong hands, this information could prove very damaging..."

    call receive_item(bast_letter, use_article=False) from _call_receive_item_8

    return


label return_to_bast():

    hide screen resource_exchange

    scene black
    show bg market at top
    with fade

    "You wait for a break in trading before you approach Bast."

    "You find her at her desk, conscientiously writing down the latest inventory."

    show bast with dissolve

    you "*clear throat*"

    bast "Uh?"

    bast "Oh, it's you [MC.name]."

    bast "I'm pretty busy. Can you come back later..."

    you "Sorry, no, Bast. There's something I need to discuss with you."

    bast "Is that so? What is it?"

    you "Listen... I know about the letter."

    bast "The... The letter?"

    you "The letter you wrote to a guy named Bill, 5 years ago..."

    "Her face becomes as white as if she had seen a ghost."

    bast "Wh... What... How... Where?!?"

    you "Don't worry, the letter is in a safe place. No one has seen it yet."

    bast "How... How much do you want for it?"

    menu:
        extend ""

        "不要求报酬":
            $ renpy.block_rollback()
            $ MC.good += 1

            you "You misunderstood me. I will give it back to you."

            bast "G-give? Why?"

            you "I can't stand a beautiful, hard-working girl like you being bullied. I've got your back."

            "She blushes."

            bast "I... Aw..."

            bast "..."

            "You give her the old letter. She takes it hesitantly, looking at it in disbelief."

            bast "You've... You've done me a kindness."

            "She looks at you straight in the eye."

            bast "I won't forget it."

            you "No sweat at all... *smile*"

            $ NPC_bast.love += 2

        "我想要1000金币":
            $ MC.neutral += 1

            you "Well, considering the guy I got it from wanted 1000 gold for it, it's only fair that you compensate me I think..."

            bast "Really? You're not looking to make money from this?"

            you "No. I just thought you should have it. It seemed... right."

            bast "Well... Thank you."

            play sound s_gold
            $ MC.gold += 1000

            "You have received {b}1000 gold{/b}."

            "You give her the old letter. She takes it hesitantly, looking at it in disbelief."

            $ NPC_bast.love += 1

        "我想要2000金币":
            $ renpy.block_rollback()
            $ MC.good -= 1

            you "I'm sure this letter is worth a lot to you... Am I right?"

            "She tenses up."

            bast "How. Much."

            you "2000 gold for my trouble. Seems like a reasonable price to keep your so-called little 'family' of builders together, am I right?"

            bast "You... Bastard..."

            you "Hey, at least I came to you first. Not sure your former boyfriend would have been so considerate..."

            "Her eyes fill with tears. Without a word, she opens her desk, and takes out several bags of coins."

            play sound s_gold
            $ MC.gold += 2000

            "You have received {b}2000 gold{/b}."

            you "There... Pleasure doing business with you."

            "You hand over the letter. She immediately tosses it into the fire."

            $ NPC_bast.love -= 2

        "我想要点别的奖励...":
            $ renpy.block_rollback()
            $ MC.evil += 1

            you "You seem to want this letter very badly... Am I right?"

            bast "..."

            you "I've read its content, you know... Not very pretty."

            bast "......"

            you "Threatening to betray your Order for a spice-addict lover?"

            bast "........."

            you "What were you thinking? Your last bit of respectability hangs on this letter. You acted like a bitch in heat..."

            bast "Stop."

            "Tears are running down her face."

            bast "I know how stupid I was."

            bast "Just give me the letter. Name your price. I'll pay you anything..."

            you "Ah, but it's not the money I'm after."

            bast "Uh?"

            "You move closer to her, until you are breathing down her neck."

            you "{i}This{/i} is what I want..."

            play sound s_surprise

            "She gasps as you reach for her chest and squeeze one of her boobs sharply."

            bast "Wh-what?!?"

            you "I've been dying to fuck those huge tits of yours... I love how your nipples perk through your uniform..."

            play sound s_scream

            "You pinch her nipple through her tunic, and she squeals. She is red with shame, but she seems paralysed."

            bast "Is... Is this the price I have to pay?"

            you "Yes. Give me what I want, and you can have your letter back."

            you "Fair?"

            bast "..."

            "She looks like she is dying with shame, but she steels her resolve."

            bast "I... I will endure anything to get this letter back."

            "Smiling, you keep fondling her breasts. She looks away, but she doesn't stop you."

            you "Sounds like we've got a deal, then."

            play sound s_dress

            call bast_titjob() from _call_bast_titjob

            $ NPC_bast.love -= 5

    if bast_letter in MC.items:
        $ MC.items.remove(bast_letter)

    "You are about to leave, when she stops you."

    bast "What about... him?"

    you "Him?"

    bast "That man... Bill... Is he...?"

    menu:
        "What do you tell her?"

        "他还活着(坦白)" if not NPC_bast.flags["killed_bast_ex"]:
            $ renpy.block_rollback()

            you "He's alive. He's not... doing so well. It is best you don't seek him out."

            bast "Oh..."

            "She says nothing, but you wonder if telling her was the right choice."

        "他还活着(撒谎)" if NPC_bast.flags["killed_bast_ex"]:
            $ renpy.block_rollback()

            you "He's uh, just fine and dandy, you know! I think he went... On an adventure! To a far, far away land, upstate..."

            bast "Really?"

            bast "So he's still out there..."

            "She looks lost. You wonder if you should have just shut up."

            $ NPC_bast.love -= 1

        "他已经死了 (坦白)" if NPC_bast.flags["killed_bast_ex"]:
            $ renpy.block_rollback()

            you "He's dead."

            bast "Oh..."

            "She seems truly shaken by the news."

            "After a while, however, she regains her composure."

            bast "I suppose it was his fate... Maybe it means I can finally move on..."

        "他已经死了 (撒谎)" if not NPC_bast.flags["killed_bast_ex"]:
            $ renpy.block_rollback()

            you "He's dead. Definitely. Yup."

            bast "Oh no..."

            "She seems truly shaken by the news."

            "After a while, however, she regains her composure."

            bast "I feel horrible, but... Maybe it means I can finally move on..."

            "You wonder if lying was the right course, but you hope it can give her closure."

        "我也不知道 (半真半假)":
            $ renpy.block_rollback()

            you "Well... I don't know."

            bast "..."

            you "But it shouldn't matter to you, really."

            you "It's high time you moved on."

            bast "..."

            bast "You're right."

            bast "I don't care what happens to the bastard. He's ruined my life more than enough already."

            you "That's the spirit."

            $ NPC_bast.love += 1

    "Leaving Bast to her melancholy, you head back to the market streets."

    return


label trade_100_resources():

    hide screen resource_exchange

    if NPC_bast.love >= 5:
        "On a busy market day, you find Bast cheerfully orchestrating the apparent chaos of dozens of camels, oxen and ponies carrying all kinds of materials in and out of the exchange."

        bast "To the right, Samuel! No, Donna, leave the cart here, I'll do the rest. Reggar! Watch it!"

        "She calls every trader by their name and has a kind word for everybody. You've never seen her quite like this."

        bast "[MC.name]! It's you! I was hoping you'd come. *smile*"

        bast "Your operation this morning is the talk of the market! 100 resources, all at once! Not even the King moves so much all at once!"

        bast "Are you building your own palace?"

        you "Well, uh, no... I guess I'm just the hoarding type."

        bast "Anyway. I have waited for a chance to talk to you for a while. I wanted to say thank you."

        you "Thank you?"

        bast "Yes... For 5 years, I've been living in the past. I see that now."

        bast "Thanks to you, I realized... I'd rather live with regret for what I did, than for what I didn't do."

        you "Word."

        bast "I think I'm ready to move on now."

        you "But your order is still working you to death, though."

        bast "Not so. I've squabbled with the elders, I even threatened to resign... So they named two holy builder initiates to assist me."

        bast "I now delegate a lot more, and I'm thinking big... Opening one or two other exchanges in the Zan area within the next 2 years, then thinking about more integration with the continental trade routes..."

        bast "Anyway. My work life, my personal life, no matter how I think of it, I'm doing better, and it's all thanks to you."

        you "I'm glad I could be of service."

        bast "There's... One more thing... *blush*"

        "She looks shy, which is out of character for her. She bites her lip."

        you "Yes?"

        bast "I have no right to ask more of you... You've helped me so much already..."

        bast "But..."

        bast "Would you... "

        extend "have sex with me?" with vpunch

        you "Of cours... Whaaat?"

        bast "Look, I'm not asking you for commitment, or a relationship... I'm not ready..."

        bast "But... It's been 5 years... I'm still young, and... I want to live a normal life. But there's this cloud that hangs over me..."

        bast "You're the only one I can trust with this. Besides, I... Err..."

        "Her voice lowers to a whisper."

        bast "I think you're considerate, and handsome and... I wouldn't mind if you... *blush*"

        menu:
            you "Well..."

            "当然!":
                you "Of course!"

            "那还用说!":
                you "You bet!"

            "太棒了!":
                you "FUCK YEAH!!!"

        play sound s_dress

        call bast_sex() from _call_bast_sex_1

        scene black with fade

        $ NPC_bast.love += 25
        $ NPC_bast.flags["last fuck date"] = calendar.time
        $ NPC_bast.unlock_trainer()

    return

label bast_titjob():

    stop music fadeout 3.0

    scene black with fade
    show bg bast titjob1 at top with dissolve

    "Taking Bast's top off, you expose her heavy, round tits and savor the moment."

    you "Finally... I was dying to see your naked tits..."

    bast "..."

    "Bast looks away with shame, but seems resigned to her fate. Her eyes widen a little as you lower your pants, revealing your stiff manhood."

    you "You're going to make those big knockers of yours useful..."

    bast "Do you want me to... rub it? *blush*"

    you "Yes. I want you to give me a great titjob. Don't mess it up, or I'll make you start all over again."

    bast "..."

    play sound s_mmmh

    "Grabbing her tits, you wrap them around your dick. The soft, silky touch of her skin is almost enough to bring you off instantly."

    "You take a moment to recover your cool."

    you "Hmm..."

    you "Ok, now, move. Do it yourself."

    bast "..."

    bast "Okay..."

    play sound s_sucking

    "Moving hesitantly at first, Bast starts massaging your dick with her big soft boobs."

    "You try hard to control yourself. You want to fully enjoy this."

    bast "Like this?"

    "Unsure of what to do at first, Bast seems to slowly set up a pace. Her mounds bounce up and down, wrapping your cock in soft flesh."

    you "That's... good..."

    you "This is not enough, though."

    bast "Uh?"

    you "Of course... The tip needs some attention too..."

    you "Why don't you use your tongue to lick it?"

    bast "Lick it? But... Ew..."

    "Raising your hips, you poke her chin with your dick, pre-cum oozing from the tip."

    you "Come on, lick it. If you don't satisfy me, I'll make you start over as many times as necessary."

    bast "Aw..."

    "She frowns as you hover your cock an inch from her lips, a string of pre-cum still hanging from her chin."

    show bg bast titjob2 at top with dissolve

    play sound s_sigh

    bast "Fine... *grumble*"

    play sound s_sucking

    "Sticking her pink tongue out, Bast starts licking the head of your cock."

    bast "Ew... Salty..."

    "She grumbles as she tastes your pre-cum, but she licks your hole clean just the same."

    "Her face is flushed and she still looks embarrassed, but you can feel that the stimulation of her boobs is having an effect on her."

    you "What's the matter, Bast? Are you getting in the mood?"

    play sound s_surprise

    bast "N-No, what the hell are you saying!"

    "In spite of her show of indignation, you notice her puffy nipples are getting harder, and she squirms as she rubs her thighs together."

    you "I don't believe this... You are getting aroused by being blackmailed into sex... What a whore..."

    bast "Sh-shut up already... Just come..."

    show bg bast titjob3 at top with dissolve

    play sound s_sucking

    "She increases her pace, furiously squeezing your dick between her tits as she licks the sides of your cock."

    "She is giving it her all now, using her breasts and tongue to make you feel good. An outside observer would think you were lovers."

    you "Oh, my... You really want my cum, don't you?"

    bast "S-Stop it... I just want this to be over..."

    you "Come on, I can see through you... You are a slut at heart... Say it..."

    bast "What the hell are you saying... I told you to stop..."

    you "Say it. Say you want my cum."

    bast "I... D-Don't make me..."

    "You take out the old letter, waving it just outside of her reach."

    you "I will give you the letter. But you must say you want it... I want you to beg for a cumshot."

    bast "..."

    "Bast seems revulsed by your request, but she cannot take her eyes off the letter."

    "With your cock wrapped between her exposed boobs and covered with her saliva, she realizes how far she's come already."

    bast "All... All right..."

    you "Good girl."

    "You pinch her nipples hard, and she squeals."

    play sound s_scream

    bast "Aaah!"

    you "Say it!"

    bast "I..."

    bast "I want it..."

    you "What?"

    bast "Your..."

    bast "Cum..."

    you "Louder!"

    bast "CUM! I WANT YOUR CUM!!!"

    bast "I want you to shoot it all over my dirty face and body!!!"

    bast "I'm a worthless sow, I deserve this!"

    bast "COVER ME WITH DIRTY SEMEN, I BEG OF YOU!"

    you "(Oh... Wow...)"

    "This is all too much for you. You can no longer contain your lust."

    with flash

    you "UWAAAAAH!!!"

    show bg bast titjob4 at top with doubleflash

    play sound s_orgasm

    bast "AAAAAAH!!!"

    "Erupting like a volcano, your cock shoots hot cum everywhere, exploding in Bast's face."

    with doubleflash

    "There seems to be no end in sight as you unload wads of thick cum onto her face, her hair and her boobs."

    show bg bast titjob5 at top with flash

    bast "Aaah..."

    "With a blank stare, Bast keeps squeezing your cock between her boobs until the last drop comes out. She doesn't even seem aware she's doing it."

    you "Muhahaha... That was good..."

    "You came so hard even the letter in your hand is stained with cum."

    you "Here, you've been a good, obedient slut... You can get your letter back."

    "Cum still dripping from her face and body, Bast barely seems to register your words."

    "After a long moment, she seems to break out of her spell."

    bast "The letter... Oh!"

    "You give Bast the cum-stained letter."

    you "Something to remember me by."

    "She looks as if nothing matters to her anymore. She takes the letter, and slips it inside her tunic."

    scene black with fade
    show bg market at top
    with fade
    show bast with dissolve

    $ MC.change_prestige(district.rank)

    return

label bast_sex():

    stop music fadeout 3.0

    scene black with fade
    show bg bast sex1 at top with dissolve

    "In a heartbeat, you move Bast's clothes and underwear out of the way, exposing her heavy tits and toned body."

    bast "W-wow... Wait!"

    you "I'm already on fire..."

    "Bast looks fearfully at your crotch which has swelled to an uncomfortable size."

    bast "I don't know if this is a good idea... I..."

    you "Come on... We've come too far already."

    "Whipping out your rock-hard cock, you stand ready for attention as she looks on."

    play sound s_surprise

    bast "It's so big... Will it really fit?"

    "She looks at your hard dick with a mix of curiosity and apprehension."

    bast "It's been a while, so... Be gentle, okay? *blush*"

    "Smiling reassuringly, you start rubbing the outside of her slit with your erect cock."

    play sound s_mmmh

    bast "Aaah!"

    "Stimulating her clit and slit with the length of your shaft, you start kneading her big soft tits as well."

    play sound s_ahaa

    bast "Ahaa..."

    you "What a hot body you have... It's really a shame it went unfucked for so long..."

    play sound s_surprise

    bast "Hey! You're terrible... *blush*"

    if NPC_bast.love < 50: # First time having sex

        you "Tell me, how does it feel to be with a man after so long?"

        bast "It's... It's somewhat different... I mean, not in a bad way..."

        "Your lower body parts make wet sounds as you keep rubbing her vagina. She starts moaning."

        play sound s_sucking

        you "Your body reacts in a nice way, though... You're getting very wet..."

        bast "I, aah... Of course it reacts that way... I haven't, aah... been stimulated for so long..."

        you "Oh, really? Don't you even masturbate?"

        bast "Hey... That's none of your... Aaah..."

        you "Look at your wet, hungry pussy... I can't believe you left it alone for this long..."

        bast "I... *blush* I do masturbate from time to time, of course..."

        you "Haha, I like when you're honest. I think you deserve a reward... Ready?"

        bast "You mean..."

        you "Yes."

    show bg bast sex2 at top with dissolve

    "Placing the tip of your cock at the entrance of her vagina, you push it slowly inside her."

    play sound s_scream

    bast "AAAHAA!!!"

    "She starts to freak out, but you keep pushing your dick in. She watches in amazement as her hungry pussy swallows it whole."

    you "See? That was easy. You are well lubricated..."

    bast "O-Ooh.."

    play sound s_moans

    "Slowly moving back and forth, you watch closely for her reaction."

    bast "Aah... Aaah..."

    show bg bast sex3 at top with dissolve

    "She seems lost in her thoughts, memories perhaps, as she looks intensely at the place where your bodies are connected."

    you "I will start moving, okay?"

    bast "Uhn..."

    "She nods absent-mindedly."

    "Picking up your pace gradually, you start rocking your hips back and forth, probing her insides with your dick."

    show bg bast sex2 at top with dissolve

    bast "Aaaah!"

    "She closes her eyes as she feels your every move, trying to keep the sensations from becoming overwhelming."

    you "Come on, don't hold back... I can tell you feel good."

    "Bending forward, you pinch her puffy nipples and twist them a little, making her squeal."

    bast "Eek! No..."

    you "You don't like it?"

    bast "I..."

    show bg bast sex3 at top with dissolve

    "She blushes, feeling the heat build up inside her."

    bast "Go ahead..."

    "Pulling on her nipples, you increase your pace, making obscene sounds as her pussy leaks out love juice."

    play sound s_moans

    bast "Aaaah..."

    you "Can I go faster?"

    bast "..."

    bast "Yes..."

    show bg bast sex4 at top with dissolve

    "Fucking her harder, you look at her pretty face, her blue eyes reflecting a mix of shame and lust that intensifies with every thrust."

    with hpunch

    you "Such a hungry pussy... It's like it was waiting for me all this time."

    bast "D-Don't... *blush*"

    play sound s_moans_short

    "Bast seems lost in the moment, however, and she quickly forgets what she was about to say. Instead, she digs her fingers into the bedsheets, arching her back to get more sensations."

    you "Yes, show me your hot, naked body... More..."

    "Your dirty talk seems to have an effect, and love juice is now gushing out of her pussy, making your dick extra-slippery."

    bast "Aaaah... Ahaaa..."

    "You feel her body tensing up. You are both close to cumming."

    with hpunch

    bast "Aaah!"

    you "Uwah!" with hpunch

    "Fucking her harder and harder, you give it all you've got. Her muffled screams become louder."

    play sound s_scream

    bast "AAH!" with hpunch

    play sound s_scream_loud

    bast "AAAAAAAH!!!" with hpunch

    play sound s_screams

    with hpunch

    bast "AAAH! AAAAAAH! AAAAAAAAAAAH!!!" with flash

    show bg bast sex5 at top with doubleflash

    "Erupting inside her, you shoot a heavy load right inside her pussy. She screams and squirms as the feeling of hot cum inside her sends her into another orgasm."

    play sound s_orgasm

    bast "AAAH, AHAAAAAAA!!!" with flash

    show bg bast sex6 at top with dissolve

    "Cum slowly gushes out of her gaping pussy, giving you the magnificent spectacle of a perfect creampie."

    you "..."

    $ unlock_achievement("h bast")

    "Bast is glassy-eyed, still recovering from her powerful orgasms. She does not even make an effort to close her legs as you watch your handiwork."

    bast "You came inside... so much..."

    you "Well, you seemed to enjoy it as well."

    bast "..."

    bast "Yes..."

    you "Look, if this is uncomfortable for you..."

    bast "No... I didn't say that."

    "You give her a quizzing look."

    bast "I still have to get used to it, that's all... You were... very helpful."

    bast "Thank you."

    you "Well... Thank {i}you{/i}."

    bast "Will you... come back to... practice with me again?"

    you "Why, of course!"

    "She smiles."

    bast "That's nice. Come find me whenever you're ready, then."

    "Pulling you toward her, she gives you a shy kiss, before sending you on your way."

    $ MC.change_prestige(district.rank)

    return


label meet_gurigura():

    play sound s_chimes

    hide screen visit_location

    scene black

    show expression selected_location.get_pic(config.screen_width, int(config.screen_height*0.8)) at top

    with dissolve

    "The atmosphere feels unexpectedly cheerful near the prison today. You spot an unusual gathering by one of the prison walls. As you approach, you hear a high pitched call."

    gurigura "HIIIII!!!"

    show gurigura with dissolve

    gurigura "Customers, customers! YAY! Welcome!!! [emo_heart]"

    "You recognize the young girl you saw travelling with her friends the other day. She is standing behind a workbench covered with cardboard boxes, some of them open."

    "Old Priest" "Hello, my dear girl! What are you selling? *gentle smile*"

    gurigura "Welcome, Mister! I sell toys... TOYYYS!!!"

    "Old Priest" "By Arios, that's nice! Maybe I'll buy a few for the children of the orphanage..."

    gurigura "Sure thing, Mister! I am just beginning to open those boxes of toys I ordered. Please pick whatever you want!"

    "Old Priest" "Well, sure, child, oh, uhm..."

    "Rummaging through one of the boxes, the old man randomly pulls out a toy from the box. One look at the toy, however, is enough to wipe the smile from his face."

    "Old Priest" "What the..."

    "The old priest is holding a huge, black dildo, covered with rubber barbs."

    "Old Priest" "This is outrageous!!! What in Arios' name is this!!!"

    gurigura "Well, it said toy on the order form... But what is it for? You like this, Mister?"

    "Old Priest" "GWAAAAAAAH!" with vpunch

    "Passerby" "Hey, nice dildo, Father!"
    "Other passerby" "So that's what those ample robes are hiding..."

    "Old Priest" "UWAAAAAAAAH!!!" with vpunch

    "Something in the priest's mind snaps and he runs away screaming, somehow still waving the black dildo in his hand."

    play sound s_surprise

    gurigura "Hey!!! Come back here!!! You didn't pay for this!"

    play sound s_sigh

    gurigura "Well... He did say it was for orphans, so... Maybe I can let it slide..."

    "The girl notices you standing there, grinning."

    gurigura "Oh, hello, Mister! *smile*"

    if NPC_gurigura.love > 0:
        gurigura "I know you! We said 'hi' at the house where women lose!"

        gurigura "I asked Katryn about it but she said it's grown-up stuff... I guess it's like this 'tax' thing."

    you "Well, hello! Nice, uh, 'toys' you have here..."

    gurigura "Wanna have a look at my toys? I also sell supplies, and foodstuff."

    you "Well no, I mean, yes... It's only for work, you see..."

    gurigura "Work? Do you work in a toy store?"

    you "Err, not exactly... But never mind, show me what you have."

    gurigura "Teehee! Look at this! *smile*"

    gurigura "Here's a free sample! Enjoy!"

    call receive_item(get_rand_item(item_type=IT_Toy, quality="common"), msg="Gurigura gives you a random %s from the open box.", use_article=False) from _call_receive_item_9

    you "(She's not going to make much money if she gives everything away for free...)"

    $ prison.action = True
    $ unlocked_shops.append(NPC_gurigura)

    scene black with fade

    "You can now buy toys, food and supplies from Gurigura's store at the {b}Prison{/b}."
    $ unlock_achievement("merchant gurigura")

    return

label meet_ramias():

    play sound s_chimes

    hide screen visit_location

    scene black
    show expression selected_location.get_pic(config.screen_width, int(config.screen_height*0.8)) at top
    with dissolve

    "The wide open space in front of the Arena is a pleasant break from the crowded and bustling streets of the Warehouse district."

    play sound s_clash

    "The clanging of metal against metal, too close to be from inside the massive building, puts you on your guard."

    thug3 "Here you go, lady."

    "A few suspicious men are unloading a bunch of weapons on a nearby stall. Battle axes, swords, clubs, daggers... Enough for a small army."

    show ramias with dissolve

    ramias "Show me."

    ramias "..."

    "You recognize the white-haired warrior you saw entering town with her friends a while ago."

    ramias "I'll take this one."

    "The woman points at a small knife next to the heap of big weapons."

    thug3 "What?"

    ramias "The steel is pure, it looks well-balanced, and there's no hint of rust near the hilt. I like it."

    thug3 "B-But... What about the rest? I brought a load of the best weapons..."

    ramias "Oh, these? No, they're crap. I don't need them."

    ramias "I'm only going to sell the best quality here..."

    thug3 "Now, listen lady. *irritated*"

    thug3 "Me and the lads didn't come all the way here to sell you just a knife."

    thug3 "You're going to have to reconsider..."

    ramias "I'm sorry I didn't make myself clear..."

    ramias "I will buy the knife. I won't buy the rest."

    ramias "Take your business elsewhere if you're not happy with it..."

    "The rough man becomes visibly angrier."

    thug3 "All right, seems like you need a lesson about fair trade practices... Let us show you how good these weapons are."

    play sound s_sheath

    "The man grabs a sword from the heap, and his friends take up clubs. They step forward menacingly."

    thug3 "We'll take what's in your purse, for starters... Then we'll have some fun with those huge knockers of yours. Been driving me crazy for a while..."

    ramias "I see. So that's how you're going to play it, eh?"

    thug3 "Don't try to be a hero now... Hand over your cash..."

    play sound s_sheath

    show ramias attack with flash

    pause 0.3

    play sound2 s_clash

    play sound3 s_shatter

    with vpunch

    "With lightning speed, Ramias takes out her weapons and hits the thug's sword at the hilt, snapping the blade clean off. The thug gasps."

    ramias "Rust near the hilt. I told you..."

    thug3 "Get her! *panicking*" with vpunch

    play sound s_sheath

    show ramias attack at jumping

    pause 0.3

    play sound2 s_crash

    pause 0.1

    play sound3 s_wscream

    with vpunch

    "The two henchmen leap forward, but before they have a chance to strike, Ramias hits one right between the legs with her lance. You cringe and reflexively grab your privates as you hear the poor fella squeal."

    play sound3 s_punch

    pause 0.2

    play sound s_crash

    with vpunch

    "Ramias bashes her shield into the second attacker, breaking his nose and sending him rolling into the gutter. The disarmed thug turns around and runs away, screaming."

    thug3 "Curse you! That woman is the devil!"

    ramias "Hey! You forgot something!"

    play sound s_sheath

    pause 0.2

    play sound2 s_dodge

    "Ramias picks up the small knife and throws it in one swift move. The thug is already about twenty yards away, but the precisely aimed knife flies just a couple of inches past his ear to lodge itself firmly in a nearby signpost."

    play sound3 s_boing

    pause 0.2

    play sound s_wscream

    thug3 "GWAAAAAAAH!!!" with vpunch

    "White with fear, the thug tumbles into a nearby alley and crawls away from sight."

    hide ramias
    show ramias
    with dissolve

    play sound s_sigh

    ramias "Humph, he left me all this crap..."

    ramias "I can't decently sell this. I guess I could give it away for a good cause... The orphanage might need some swords and warhammers?"

    "Although she is a fearsome fighter, she doesn't seem to be very practical."

    you "Ahem..."

    ramias "Yes? Are you buying?"

    if NPC_ramias.love > 0:
        ramias "Oh... I know you. Aren't you the dodgy [MC.playerclass] that was checking out my boobs the other day?"

        you "Well, as a matter of fact, I'm checking them now... I mean, I'm checking your wares."

        you " Your wares, of course, haha..."

    if MC.playerclass == "战士":

        ramias "You look familiar... And you have the build of a soldier. Have I met you somewhere in battle?"

        you "I served up North for several years. Special forces. Prince Elliot's battalion."

        "Her face becomes visibly pale, as if she had seen a ghost."

        ramias "I see... I probably saw you there..."

        you "You were in the war, too?"

        ramias "..."

        ramias "It's all in the past, now. I am retired. I'm happy to be just a merchant."

        $ NPC_ramias.love += 3

    ramias "I sell blades, hammers, odds and ends... I try to select mostly good-quality stuff, but if you want the shitty, rusty ones here, you can have them for cheap."

    ramias "Just don't come complaining to me about the quality if I haven't handpicked it myself."

    you "Interesting... I might have a look."

    ramias "You can even have one of these crappy weapons for free... I don't want you to tell everyone you meet that I ripped you off. *shrug*"

    call receive_item(get_rand_item(item_type=IT_Weapon), "Ramias hands you a rusty %s.", use_article=False) from _call_receive_item_10

    $ arena.action = True
    $ unlocked_shops.append(NPC_ramias)

    scene black with fade

    "You can now buy weapons from Ramias's store at the {b}Arena{/b}."
    $ unlock_achievement("merchant ramias")

    return


label meet_riche():

    hide screen visit_location

    scene black
    show expression selected_location.get_pic(config.screen_width, int(config.screen_height*0.8)) at top
    with dissolve

    "Leaving the noise and agitation of Zan's wealthy districts behind, you enter the botanical garden for a relaxing stroll."

    "Here, gardeners and magicians join forces to maintain a large variety of plants from all over the world, using weather spells to create the right climate for each."

    riche "Dragon tulips, red sunflowers, carnivorous dandelions..."

    riche "Where are they?"

    show riche with dissolve

    "You recognize the cute blonde girl you saw before visiting the city with her friends. She is absorbed with her task, checking off items from a list."

    you "*clear throat*... Hi."

    riche "Uh?"

    "She is startled by your approach and looks at you for a moment before she recognizes you."

    riche "You... I saw you before..."

    if NPC_ramias.love > 0:
        riche "You were looking at me... *blush*"

    you "Ah, yes... We haven't been properly introduced. My name is [MC.name]."

    "She seems hesitant to reply. Her cheeks are red."

    riche "I, uh, I remember seeing you near the... the..."

    you "Ah, yes. The brothel?"

    "Blood rushes to her cheeks. Her face is completely flushed."

    riche "I'm sorry... I..."

    you "It's just a business like anything else, nothing remarkable about it really. It's far from the only one of its kind in Zan..."

    riche "You're... You're right I guess. I've just never met... a bro... brothel owner before."

    "Regaining her composure a little, she looks at you with a mix of apprehension and curiosity."

    "She seems to struggle not to run away, but eventually she gives you an awkward smile."

    riche "My name is... Riche. Is there something I... I could do for you?"

    you "Well, I saw you gathering plants, and I was wondering what you were doing."

    "She visibly relaxes as you switch to a more appropriate topic."

    riche "Oh, these? They are necessary for my studies. I am doing some research on the healing properties of flowers, and this is the best place to get them."

    riche "Also, I just like to gather flowers. It soothes my mind..."

    you "I see... So, you're doing some research? Are you a botanist?"

    riche "Me? Well, no... I'm from the House of Eden, one of the oldest noble families in Xeros. I am not supposed to work, but... I don't like to remain idle."

    riche "I've seen enough suffering in the war, and now I want to dedicate my time to helping alleviate it."

    you "Well, that's... noble of you. No pun intended."

    you "But wait, did you say you were in the war?"

    riche "Yes, I just came back from the front lines with my companions."

    you "You seem awfully young and cute to be in the war..."

    riche "C-cute?!? *blush*"

    "She seems embarrassed by your compliment and looks away, biting her lip."

    riche "I am a mage. I was studying in Karkyr, up until last year. Top of my class..."

    riche "But I was tired of being sheltered, so after I graduated, I decided to join the war effort."

    if MC.playerclass == "法师":
        you "Karkyr? What a coincidence! I was studying there too. I must have been a few years your senior..."

        you "I was also top of my class, what a coincidence... I mean, definitely in the top 50, at least..."

        riche "Were you? Now that you mention, your name sounds familiar... [MC.name]..."

        riche "Oh, yes! I heard all about you!!!"

        you "Well, I'm not surprised, I was quite popular in my day..."

        riche "[MC.name] the underwear thief! You were like a legend in school!"

        you "Uh, hem, what? Why do people even remember this???" with vpunch

        riche "They say you stole a dozen girls' panties in just one night! We were warned about you on our first day!!!"

        $ NPC_riche.love += 3

        you "Borrowing is not stealing!!! And... And..."

        you "ANYWAY!" with vpunch

        you "What about your time in the war? You were saying?"

    else:
        you "Really? That must have been tough."

    riche "The war..."

    riche "I always knew I would use my magic to heal, not to fight... Yet, after seeing so much bloodshed, I couldn't take it anymore. None of us could."

    you "Your friends as well?"

    riche "Yes. We got discharged, and banded up together to come back here."

    riche "But what I saw during the war still haunts me. I want to be a force for good."

    menu:
        "你真是心地善良":
            you "It's nice of you to place others before yourself."

            riche "Well... It's the least I can do..."

            riche "We noble people ought to give back a little, don't you think?"

            you "I do. But few actually care to..."

            $ MC.good += 1

        "你真是蠢到家了":
            you "It's stupid. In this world, trying to alleviate other people's suffering is a fool's errand. You're better off thinking about yourself."

            "She blushes."

            riche "I know it sounds pointless... But I also do this for selfish reasons. I want to feel better about myself."

            you "Now, you're being honest."

            $ MC.evil += 1

        "你真是太性感了":
            you "Baby, just laying eyes on your sweet body is enough to nurse a dying man back to health..."

            "She blushes bright red and is at a loss for words."

            riche "Aah..."

            riche "(Arios, a man is complimenting me! What should I do!)"

            $ MC.neutral += 1

            $ NPC_riche.love += 2

    with fade

    "You chat a little with Riche as you help her gather more flowers."

    riche "All right, that's it. Now, I just need to find some gold..."

    you "Why do you need gold?"

    riche "I need to rent the lab and some magic equipment for my research... It adds up to a real budget."

    "She blushes."

    riche "The thing is... I have to ask my family for money. It's humiliating. I don't like to depend on them too much. But since I can't work..."

    "You briefly consider offering her a job, but her innocent look makes you reconsider."

    you "Well, I guess there's not much you can do..."

    "As you say that, you spot a couple on a bench."

    "The man gives the woman a bunch of flowers. She gasps, gives him a beaming smile, and starts kissing him passionately."

    you "Look! I have an idea!"

    riche "Wh... A kissing couple?"

    "She blushes bright red."

    riche "(Aah, but we only just met... I've never even been on a date before... *blush*)"

    you "You could sell some of your flowers. Boys give them to girls they like. I'm sure they're willing to pay good money for it."

    riche "Oh, that's what you meant... Haha, hahaha..."

    riche "Well, that's an idea worth considering. Selling flowers is not really 'work', I guess. And it could help pay for my research..."

    riche "Thank you, [MC.name]. I'm glad you stopped by to chat. *smile*"

    you "My pleasure..."

    riche "Here, have one of these. I gathered more than enough, thanks to you."

    call receive_item(get_rand_item(quality="F"), "Riche gave you a free %s.", use_article=False) from _call_receive_item_11

    scene black with fade

    "You can now buy flowers from Riche at the {b}Botanical Garden{/b}"
    $ unlock_achievement("merchant riche")
    $ botanical_garden.action = True
    $ unlocked_shops.append(NPC_riche)

    return

label meet_katryn():

    hide screen visit_location

    scene black
    show expression selected_location.get_pic(config.screen_width, int(config.screen_height*0.8)) at top
    with dissolve

    $ d = calendar.get_weekday()

    "Today is a peaceful [d] in the Magic Gardens district, and you decide to grab a book to while away the hours."

    you "No, last time I checked there was a section for ero-mangas... Ah! There it is."

    with fade

    play sound s_fire

    with vpunch

    play sound2 s_crash

    you "What???"

    "A loud explosion rings across the quiet library, startling you and making you drop your current read to the floor."

    you "Damn... I was getting to the part where the hero was about to take a bath with his step-sister..."

    "Alarmed by the explosion, you follow the billows of smoke and reach a service aisle you have never visited before."

    katryn "*cough* *cough*..."

    show katryn with dissolve

    "A young woman is standing in the middle of a storage room full of burnt and broken furniture, coughing inside a cloud of heavy black smoke."

    you "Come over here! Quick!"

    "Grabbing the girl by the shoulders, you escort her out of the smoky room. She struggles to catch her breath."

    katryn "*cough* Damn this stupid fossil fuel engine! I should have known such a stupid technology has no chance to work... *cough*"

    "She grumbles to herself, barely aware that you are still holding her. Suddenly, she seems to notice you."

    katryn "Who... Who are you? Why are you touching me?"

    if NPC_katryn.love > 0:

        play sound s_surprise
        katryn "AAH!" with vpunch

        katryn "You're the p-p-pervert from the other day..."

        "She recognizes you: you met in front of your brothel as she was arriving in town with her friends."

        play sound s_woman_scream

    katryn "Let me go!!!" with vpunch

    you "S-sorry..."

    katryn "Don't you dare touch me with your gross manly hands! I'm not one of those girls!!!"

    you "I was just trying to help... You could have suffocated in there."

    katryn "In there? Oh, yes, I suppose I could have... But I was busy trying to figure out the cause of the explosion..."

    you "How is that more important than breathing!" with vpunch

    katryn "Stop yelling. I'm thinking."

    katryn "(The conveyor belt can only withstand a maximum friction equal to the square root of pi multiplied by the number of yards from the boiler to the tank divided by 11...)"

    you "Ahem."

    katryn "What? Gee, it's impossible to concentrate with your constant interruptions!"

    you "Your coat is on fire."

    play sound s_surprise

    katryn "GWAAAAH!!!" with vpunch

    with fade

    you "...Anyway, what's that strange machine supposed to do?"

    katryn "Humph, it's painfully easy. You would have guessed it all by yourself if you had an ounce of smarts to yourself..."

    you "I wonder if rescuing you from that fire was a good move..."

    katryn "It's an automated assembly line. Automatons replicate the various processes necessary to mold rare metals into fine, if unoriginal jewelry."

    you "Why not ask a jeweller to make it?"

    katryn "Ha! Jewellers charge outrageous costs to make even simple accessories like rings, and they stop working to sleep, eat, have sex, and other base animal tasks."

    katryn "In contrast, my automatons work 24/7 with no pay and require no down time. This is the way of the future."

    you "Except your automatons are all blown up..."

    katryn "There are a few drawbacks. But hey, Zan wasn't built in a day. Do you think the first man to invent the ship renounced sailing when his first boat sank?"

    you "Well, he might have drowned on the spot..."

    katryn "Quit arguing with me. With just a few tweaks, the assembly line will soon work perfectly."

    "You give a skeptical look to the burned-out storage room."

    katryn "Before it exploded, it even had time to process this one item..."

    katryn "Here, it's a little melted on both ends, but you can keep it as a reminder of the glorious future that awaits."

    call receive_item(get_rand_item(item_type=IT_Necklace), "Katryn gave you a slightly burnt %s.", use_article=False) from _call_receive_item_12

    you "Why did you set up your operation in the Great Library, of all places?"

    katryn "This place has got all the books I need to complete my experiments! It's a lot more efficient this way."

    katryn "Until someone invents a way to share knowledge over long distance using some kind of personal terminals that can compute data or something, this has to be the best way."

    katryn "But everyone knows this is just a pipe dream: the second you'd invent that, it would be overloaded with porn and penis enlargement ads...."

    you "That's, uh... An oddly specific statement..."

    katryn "I have a lot of work here, so I'd appreciate it if you scrammed. Come back when the assembly line is working, and I may sell you more trinkets."

    $ library.action = True
    $ unlocked_shops.append(NPC_katryn)

    scene black with fade

    "You may now buy trinkets from Katryn at the {b}Library{/b}."
    $ unlock_achievement("merchant katryn")

    return

label meet_giftgirl():

    hide screen visit_location

    scene black
    show expression selected_location.get_pic(config.screen_width, int(config.screen_height*0.8)) at top
    with dissolve

    "The emporium is one of the main attractions in Zan. There are many markets in the City of Jade, but the emporium, together with the sex slave market, is the most popular."

    "Here, ships from the seven seas unload their most exotic cargo from all corners of the known world."

    "This is a place of choice for antique brokers, eccentrics and collectors. Just don't expect to find anything remotely useful..."

    giftgirl "Welcome, Mister!"

    show giftgirl with dissolve

    "A smiling beauty is calling you, motioning for you to come closer. You enter her shop, drawn by curiosity and willing to give a closer look at her ample bosom."

    play sound s_chimes

    giftgirl "Here we sell all kinds of gifts and curiosities..."

    you "I see... *gulp*"

    giftgirl "Are you ok, Mister? Is everything all right? You're not looking me in the eyes..."

    play sound s_boing
    show giftgirl:

        ease 0.5 zoom 4.0 xoffset xres(150) yoffset yres(1000)
        pause 0.5
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    you "I'm perfectly fine, thank you... *drool*"

    giftgirl "Good! I'd be happy to serve you however I can... *smile*"

    giftgirl "Here, keep this. It's on the house. My gift to a new customer!"

    call receive_item(get_rand_item(item_type=IT_Gift), "The woman gave you a free %s.", use_article=False) from _call_receive_item_13

    $ exotic_emporium.action = True
    $ unlocked_shops.append(NPC_giftgirl)

    scene black with fade

    "You can now buy gifts and miscellaneous items from the Gift Store at the {b}Exotic Emporium{/b}."
    $ unlock_achievement("merchant giftgirl")

    return

label meet_twins():

    hide screen visit_location

    scene black
    show expression selected_location.get_pic(config.screen_width, int(config.screen_height*0.8)) at top
    with dissolve

    "Pilgrim Road is an iconic street in Zan, a long avenue that crosses the city all the way from the Slums to the magnificent Arios Cathedra."

    "Incessant flows of pilgrims come up and down the road, some of them walking the whole way on their knees and elbows, other walking backwards or blindfolded as a sign of worship. {nw}"

    if MC.god == "太阳神":
        extend "Although you empathize with their fervor, it is no less annoying to have to dodge clumsy pilgrims every step of the way."
    else:
        extend "You are annoyed at the Arios fanatics that threaten to bump into you every step of the way."

    "Spotting a big store flashing with bright colors, you decide to take refuge inside for a change of pace."

    play sound s_chimes

    scene black with fade
    show bg twins at top with dissolve

    today "Hiiii!"

    "The store is a tailor workshop, and you are greeted by two pretty girls wearing a traditional kimono, simple yet stylish."

    you "T... Twins..."

    today "Welcome! Are you a pilgrim? Can I interest you in monk robes?"

    you "Well... No. I'm not a tourist. I live here."

    today "Oh, that's a relief! I'm so tired of selling religious garb!"

    today "My sister here makes all sorts of fine dresses: simple dresses, cocktail dresses, night dresses... Even some very kinky ones, if you're into it. Right, sis'?"

    yesterday "..."

    today "As a matter of fact, take this sample dress. It's on us. I'm sure you'll be impressed with the quality."

    call receive_item(get_rand_item(item_type=IT_Dress), "The twins let you have a sample %s.", use_article=False) from _call_receive_item_14

    today "But most people on Pilgrim Road only care about looking good for religious ceremonies, so I'm afraid they don't sell..."

    yesterday "... *frown*"

    you "What about you? Aren't you Arios worshippers?"

    today "Well, kind of, but we're just initiates... Every merchant on Pilgrim Road must be affiliated with the church somehow, as you know."

    today "But it's not like we have taken any vow of celibacy, or anything like that... Right, sis'? *wink*"

    yesterday "... *blush*"

    today "I'm Today! Pleased to meet you. My sister here is Yesterday."

    $ today_name = "Today"
    $ yesterday_name = "Yesterday"

    yesterday "Hi."

    today "They say I'm the talkative one, I'm not sure why. Sis' here is the real noisy one - you should hear her drone on about her dresses. Go figure."

    yesterday '...'

    you "Wait a second... Your names are Today and Yesterday?"

    today "That's right! What's yours?"

    you "Well, I'm [MC.name]. But I mean, your names are uncommon... As in: 'I've never heard such names, ever.'"

    today "As uncommon as [MC.name]? Meh, I don't think so. Ever heard the name [MC.name], sis'?"

    yesterday "..."

    yesterday "No."

    today "See! Your name is the one that's weird. Right, sis'?"

    yesterday "Uhn."

    you "Anyway. I was wondering if I could browse your wares."

    today "Sure! We have a whole shipment of accessories that came in yesterday..."

    yesterday "Yes?"

    today "I'm not talking to you. I was saying, yesterday..."

    yesterday "Yes?"

    today "I am NOT talking to you!" with vpunch

    today "The shipment came yesterday..."

    yesterday "No, today."

    today "What?"

    yesterday "Today, the shipment came... Today."

    today "Yes I know it came! Yesterday!"

    yesterday "What?"

    you "Look, girls, don't fight, it's easy."

    you "{b}Today{/b} said the shipment came yesterday but {b}Yesterday{/b} thinks the shipment came today."

    today "But yesterday, Yesterday said the shipment would come 'today' which means it actually came yesterday as today would have been tomorrow at the time..."

    yesterday "Our cousin, Tomorrow? What about her?"

    today "AAAARRH!!! Forget it!!!" with vpunch

    "The twins keep arguing while you browse the store."

    $ pilgrim_road.action = True
    $ unlocked_shops.append(NPC_twins)

    scene black with fade

    "You can now buy dresses and accessories from the twins' tailor shop on {b}Pilgrim Road{/b}."
    $ unlock_achievement("merchant twins")

    return

## NINJA GUEST EVENTS ##

label ninja_guest1: # Warrior event
    # "Guest event Warrior"

    with vpunch
    "*BONK*"

    scene black with fade
    show bg thieves_guild corridor at top with dissolve

    show hokoma_warrior with dissolve

    play sound s_surprise

    hokoma_warrior "MOO!" with vpunch

    "While chasing after the Kunoichi, you unexpectedly bump into a fearsome woman."

    hokoma_warrior "You! Watch where you're going!"

    you "S-Sorry..."

    "The first thing that strikes you is a that she looks like a mighty warrior, sporting an exotic-looking claw on her arm."

    "Actually, make that the second thing. The {i}first{/i} thing that strikes you is her plump body and her enormous rack, only protected by a loose loincloth that lives little to the imagination."

    you "(B... Boobs...)"

    hokoma_warrior "Hey! I'm talking to you!"

    hokoma_warrior "I see you're wielding a hammer. You came here to challenge me? To cross sword with the elite captain of the Gwanaian tribe?"

    if MC.playerclass == "战士":
        "You know that Hokoma's tribes have fierce female warriors, all following a myriad local traditions and superstitions that allow them to recognize each other, while being impenetrable to outsiders."

    you "N-No, that's a mistake, my Lady, I didn't mean to hit you..."

    hokoma_warrior "Moo, that's a pity. I was looking for a good work out."

    you "I'll be going, now, if you don't mind..."

    hokoma_warrior "WAIT!!!" with vpunch

    "You freeze in your steps, as the massive woman looms closer over you."

    hokoma_warrior "Let me take a look at you..."

    "She bends forward and... {i}sniffes{/i} you."

    hokoma_warrior "Well, he's scrawny, but he could do... *sniff*"

    "You start to notice she actually has animal features. She must be a descendant of the fairy people. As she looks at you with a wolfish smile, you start wondering what the Southern tribes eat..."

    hokoma_warrior "Hey! Come here!"

    play sound s_wscream

    you "Eeek!!!" with vpunch

    play sound s_crash

    scene black with fade

    "She pins you down on the floor with her free hand, ripping your clothes off with a lightning fast strike of her claw."

    you "AAAH!!! Don't eat meeee!!!" with vpunch

    "You start panicking, wondering if she's about to rip your dick off, but instead she just gives you a mad, feverish look while shoving aside her clothing."

    play sound s_dress

    show bg guest1_sex1 at top with fade

    hokoma_warrior "Moo, let's fuck, little man! I'm in heat!"

    you "Whoah!"

    "Not giving you any choice in the matter, she impales herself on your dick, which out of old habit was ready for it before you were."

    play sound s_orgasm

    you "Uwah!"

    hokoma_warrior "Oh, this is the stuff... This is just what I needed..." with vpunch

    you "Ugh..." with vpunch

    hokoma_warrior "Your timing was perfect, little man. I get so horny when I'm pregnant."

    you "You... You what? You're pregnant?"

    hokoma_warrior "Of course, moo! I get impregnated by the men of my tribe every year. This is a key part of our war rituals..."

    hokoma_warrior "The women of my people are the best fighters. And they fight the hardest when they're pregnant."

    you "That's crazy..."

    hokoma_warrior "Don't believe me? Take a look, moo!" with vpunch

    show bg guest1_sex2 at top with dissolve

    "The warrior lady start massaging her massive tits, which quickly start spurting out milk."

    play sound s_aaah

    hokoma_warrior "Moo! This feels so good!" with vpunch

    you "Oh... This is so naughty..."

    "She keeps playing with her tits, lactating while riding your cock. Soon, this becomes too much for you to handle."

    you "Uuuh..."

    show bg guest1_sex3 at top with flash

    you "UWAAH!!!"

    with doubleflash

    play sound s_orgasm

    "You cum hard inside here, filling her up to the brim with hot cum. Enough to make her pregnant twice over."

    show bg guest1_sex4 at top with flash

    hokoma_warrior "So good! So good! Moo... More!"

    "Not skipping a beat, she keeps riding you, squeezing your sensitive cock with her pussy until it is back in business."

    play sound s_sucking

    hokoma_warrior "Let us not waste so much milk... Mmmmh..." with vpunch

    show bg guest1_sex5 at top with dissolve

    "She starts sucking on her nipples, drinking her own milk hungrily."

    you "Ohh..."

    "She then turns to you and forcibly kisses you with a mouthful of warm milk and saliva, making you drink it."

    you "Ngh... *swallow*"

    show bg guest1_sex4 at top with dissolve

    hokoma_warrior "Oh, little man! I feel it now! I feel it!" with vpunch

    play sound s_scream

    hokoma_warrior "Mooo!!! I'm cuuuming!!!!" with vpunch

    show bg guest1_sex6 at top with doubleflash

    play sound s_orgasm

    "Unable to control yourself, you cum inside her again while she splashes your face with milk."

    with flash

    hokoma_warrior "Aaaah! [emo_heart]"

    show bg guest1_sex7 at top with doubleflash

    you "Ohhh..."

    play sound s_ahaa

    hokoma_warrior "Aaah... Thank you, little man... That was good and satisfying."

    hokoma_warrior "I shall not wash your seed from my body, for good luck in battle."

    you "..."

    scene black with fade

    "It takes you a while to recover and find your way back onto the street. The Kunoichi is long gone, of course."

    return

label ninja_guest2: # Magician event
    # "Guest event Magical girl"

    play sound s_crash
    "*CRASH*" with vpunch

    scene black with fade
    show bg magic_cellar at top with dissolve

    "As you run through an abandonned house in an attempt to corner the Kunoichi, the floor gives way, sending you crashing down into a cellar."

    you "Ouch!" with vpunch

    "Fortunately, something cushions your fall."

    play sound s_crash
    show magical_girl with vpunch

    magical_girl "Abracadabr- AW!"

    "It happens to be a frail girl wearing a strange outfit, that you just send tumbling backwards onto the dusty floor."

    magical_girl "OUCH! My butt! What is this interruption?" with vpunch

    you "Err, sorry lady, I didn't mean to..."

    magical_girl "My ritual! You interrupted me! And now I have to..."

    magical_girl "Uh-oh."

    "She looks down at her feet. You follow her worried stare and see a magical pentagram drawn on the floor and slightly glowing."

    "She is standing right in the middle."

    magical_girl "Oh no!!! I am standing inside the Faustian Gate! You know what this means, don't you?"

    you "A Faustian..."

    if MC.playerclass == "法师":
        you "So you were trying to summon something from another plane, but now you are the one who will be sent away to some other dimension?"
    else:
        you "I don't know... It means you screwed up bad?"

    magical_girl "Please, help me! I can't pass that magical barrier! I will be transported to a demonic plane in mere moments!"

    you "Wait a second... You were trying to summon a demon?"

    magical_girl "We have no time for that now! Help me!" with vpunch

    you "Lady, I'd love to help you, but I'm not an expert on demonic summoning..."

    you "And I'm pretty sure I should be doing something safer with my time, such as chasing down crazy murderous female ninjas."

    magical_girl "You ruined my ritual, and put my life and soul in jeopardy! Figure something out!" with vpunch

    "She looks at you with pleading eyes, and she's also kind of cute."

    you "*sigh*"

    you "All right, what do you know about this ritual? Is there any way we can breach that magical barrier?"

    magical_girl "Well... I was trying to summon a, err... Ahem."

    you "Spit it out! Your life is at stake, remember?"

    magical_girl "A-All right... I was trying to summon an incubus..."

    if MC.playerclass == "法师":
        you "An incubus? Wait a second... That is a sexual demon! What did you want to do with that?"

        magical_girl "This is, err, ehm... Private business..."

    else:
        you "An incubus? Wait a second... Isn't that a nu-metal band from a long time ago?"

        magical_girl "No, you simpleton! It's a, erm... Male demon..."

    you "What did you expect from a male demon? Don't tell me... You're having sex with demons?"

    magical_girl "N-N-No! I was just going to ask it questions, I swear! *blush*"

    magical_girl "Maybe have him show me something... From afar! But no touching! Ew!" with vpunch

    you "All right, all right, no need to yell... You won't get kink-shaming from me."

    magical_girl "Stop it! And help me!"

    you "Well, so you were trying to summon a demon from a sexual plane... Do they have any kind of weaknesses?"

    magical_girl "Well, I mean, they feed on sexual energy, so... Perhaps it could saturate the barrier, but..."

    "She blushes bright red."

    you "Sexual energy? Then I think I know just what to do..."

    scene black with fade

    show bg guest2_sex1 at top with dissolve # prep vag see-thru

    magical_girl "A-Are you quite sure?"

    you "Quick! There's no time! Follow my instructions, and we can get you out of here!"

    magical_girl "(So now he's an expert, uh...)"

    magical_girl "I took the position you told me. What do I do now?"

    you "Come on, you're not that hopeless. You know what to do! You have to touch yourself."

    magical_girl "Touch myself? Down... Here?"

    you "Yes. Get going, we ain't got all day."

    magical_girl "B-But, do you have to watch, though? It's too embarrassing..."

    you "It's quite important that, er, I watch everything, to know if, erm, if the ritual is going as planned. Spread your legs more. More!"

    magical_girl "Aw... *blush*"

    show bg guest2_sex2 at top with dissolve # mast through fabric

    play sound s_sucking

    "Reluctantly, the girl starts carressing her clit and slit through the fabric of her suit. The wet white cloth quickly becomes translucid, giving you quite the erotic view."

    magical_girl "Ah, aah... Am I doing it right?"

    you "Yes, you're doing great. Pull on your suit a bit more, so that it bites into it... Nice."

    "Blushing bright red, the girl continues touching herself following your encouragement."

    magical_girl "Oh, aah, aaah..."

    "Although clearly inexperienced, she is getting in the mood quickly. Her moans become deeper as her love juice starts running down her thighs."

    you "You're doing great. Keep going!"

    magical_girl "I feel, ah, strange... My head is dizzy..."

    magical_girl "Uhn... Ah... Aaah..."

    show bg guest2_sex3 at top with flash # mast through fabric org + magic reaction

    magical_girl "AAAAH!!!"

    with doubleflash

    "Suddenly, she comes loudly, arching her back as her love juice spurts out."

    you "It's working! The pentagram is reacting!"

    magical_girl "B-But... The magical barrier is still in place... It is barely weakened..."

    you "Damn... We're on the right track, but something's missing..."

    "Noticing you got a raging hard-on from watching her come, it gives you an idea."

    you "I guess we have no choice. Let me come inside with you."

    magical_girl "What? But you'll be trapped also!"

    you "Trust me. And more importantly, get your suit out of the way and spread your pussy lips."

    magical_girl "L-Like that?"

    "Surprisingly, she complies almost immediately with your request, perhaps a bit too sheepishly. Maybe she enjoys being bossed around."

    you "More, show me more... Great. Here I come."

    show bg guest2_sex4 at top with dissolve # x + open psy + scream

    play sound s_moans

    magical_girl "Wait, aaaaaah!"

    with vpunch

    "Because time is of the essence, you ignore her cries and plunge your dick deep inside her."

    magical_girl "OH! AAH!" with vpunch

    "She is tight but also extremely wet, so it is still easy to move inside."

    magical_girl "W-What am I doing... What's going on... It feels so... So..."

    "Her pussy walls are nicely gripping your cock as you pound her deeper and deeper, hitting her cervix."

    magical_girl "Ohh... Ohhh..." with vpunch

    "The light coming from the pentagram starts to flicker. You can feel something powerful building up inside you."

    magical_girl "It's reacting! The Faustian Gate! It's almost there!"

    you "Then it's time to put an end to this..."

    you "UWAH!" with vpunch

    show bg guest2_sex5 at top with flash # cin + open psy + scream

    play sound s_scream_loud

    magical_girl "AAAAAAH!!!"

    with doubleflash

    "You cum hard inside her, spurting a huge load inside her small pussy."

    play sound s_orgasm_young

    "The feeling of hot cum filling her up is too much to bear, and she cums like crazy, yelling at the top of her lungs."

    show bg guest2_sex6 at top with flash # cpie + open psy + blush

    magical_girl "Oh, ah, aah... *pant*"

    "The light of the pentagram recedes and it seems like an invisibe veil has lifted."

    magical_girl "The magical barrier... It's gone... And the pentagram is inert, forever."

    you "Hurray!"

    you "Although I guess that means you won't be able to summon your incubus now. Sorry..."

    magical_girl "The... Incubus? Oh... I, uh, I... It won't be necessary..."

    you "Really? What do you mean?"

    magical_girl "Ah, uh, nothing... Nothing at all! *blush*"

    magical_girl "I-I have to go now. Have, uh, have a nice day!"

    scene black with fade

    "She darts off, barely taking the time to fix her clothes."

    you "And... She's gone. Phew."

    you "Oh well. Good thing that the Hero was here to save the day, once again."

    "You wonder if you should stop referring to your cock as 'the Hero'."

    return

label ninja_guest3: # Scientist event
    # "Guest event Scientist"

    scene black with fade
    show bg_rooftop at top with dissolve

    you "Now... I gotcha!!!"

    play sound s_boing

    girl_scientist "UWAH!!!" with vpunch

    "You saw something move on the roof, and you pounced. Turns out it is not a ninja, though."

    show girl_scientist with dissolve

    girl_scientist "What are you doing! Let me go!!! Aaah!" with vpunch

    "The woman you just grabbed is dressed more like a lab rat than a ninja. She is holding on to some strange apparatus that looks very fragile."

    play sound s_shatter
    with vpunch

    you "(Uh-oh. I hope I didn't break anything...)"

    girl_scientist "Oh no! You just broke EVERYTHING!!!" with vpunch

    you "W-Wait! What did I... And what are you doing up here on the roof, anyway?"

    girl_scientist "Why, I'm a doctor studying under the great Katryn Lapusel. I also moonlight as a contractor for the Slavers' Guild. My research is invaluable to them."

    you "Really? I know the Slaveres' Guild, and I didn't pick them to be science guys."

    girl_scientist "This machinery that you just broke is a state-of-the-art intercourse lidar. It is invaluable to them!"

    you "Really? What does it do?"

    girl_scientist "Why, it detects sexual intercourse, of course! We can then match it with the city land registry, to discover the most sexually active buildings in the city."

    you "Really? Where are they?"

    girl_scientist "74 times out of 100, these are brothels! The rest are mostly noble parties."

    girl_scientist "Either way, this is useful intel for the Guild. And it's a great way to spot all of the illegal brothels that don't pay their fair share."

    you "*gulp* I didn't know they had access to such advanced technology..."

    girl_scientist "But now it's ruined! And also, there's the additional hazard of... Uh oh."

    "She takes out another gizmo from one of her numerous pockets and places it over her wrist."

    play sound s_surprise

    girl_scientist "Oh no... It's even worse than I've thought..."

    you "Uh?"

    girl_scientist "The vacuum chamber has depressurized! All the pent up sexual mojo stored inside has been released, and we've been exposed!"

    you "We?"

    girl_scientist "You and me both! This is a disaster..."

    girl_scientist "Quick! Follow me to the lab!"

    scene black with fade
    show bg lab at top with dissolve

    girl_scientist "Oh... I'm not feeling well..."

    "On the way to her lab, the lady scientist has become feverish. She stumbles down on the floor of the lab, panting."

    girl_scientist "Quick! I need what in that drawer! Give it to me!"

    "Making your way through heaps of paper and machinery, you reach the designated drawer."

    you "Let's see... Is it the drugs? The red or blue pills?"

    girl_scientist "No!"

    you "Okay... The syringes?"

    girl_scientist "No!!! Not that!" with vpunch

    you "Then what? There's nothing else here, apart from that giant pink dildo!"

    girl_scientist "YES! The fuschia reticulated penetrator! Give it to me!"

    you "Uh? You want the dild-..."

    play sound s_dodge
    with vpunch

    "Before you have a chance to finish your sentence, she rips the device from your hands."

    "Ignoring your puzzled look, the girl immediately starts putting it to good use."
    show bg guest3_sex1 at top with dissolve # open blouse + no bottom + bend on lab floor + dild psy+A wet

    play sound s_vibro

    girl_scientist "F-Finally..."

    girl_scientist "What? What are you looking at?"

    you "I don't know... What are you doing?"

    girl_scientist "What does it look like I'm doing? I must remove the pent up sexual energy... Aaah... So that it doesn't saturate my system... Ohhh..."

    play sound s_sucking

    you "Wow, it looks like you really know what you're doing..."

    "You look on appreciatively as she uses the dildo to stimulate both of her holes. She's more experienced with it than many of your girls."

    you "I like your style... How did you get so good?"

    girl_scientist "Oh, please. Bodily needs only get in the way of studying. It is a simple matter to figure out how to deal with them swiftly, so that one can return to serious matters.."

    play sound s_aah

    girl_scientist "Aah..."

    girl_scientist "Ah yes, I can feel release is coming... It's... It's..."

    play sound s_scream

    show bg guest3_sex2 with flash # org + sqrt

    girl_scientist "Aaah!"

    play sound s_orgasm_fast

    with doubleflash

    girl_scientist "AAAAH!!!! *squirt*"

    "Angling the dildo so as to hit all of her weak spots at once, the scientist cums loudly, leaking love juice onto the lab floor."

    show bg guest3_sex3 with flash # rest

    girl_scientist "Oh, aah..."

    you "Wow... Well, thanks for having me... I'm' grateful for the free peep show."

    girl_scientist "No, wait... This isn't right..."

    you "Uh? What do you mean?"

    show bg guest3_sex4 with dissolve # take out dild & spread juice on floor

    play sound s_vibro

    "She spreads her buttcheeks, popping the dildo out as her pussy drips fluid onto the floor."

    girl_scientist "I... I received a very high dose of sexual mojo... Way higher than in all those previous lab incidents!"

    you "(So this happens a lot, uh...)"

    girl_scientist "The reticulated penetrator is not working! What should I do?!?"

    you "Well, err..."

    girl_scientist "Do something!!!" with vpunch

    "She waves her butt in your face, begging you to come up with a solution."

    show bg guest3_sex5 with dissolve # fing psy + thumb in A

    "Seeing her distress, you move forward without thinking."

    girl_scientist "M-Manual stimulation? Are you sure?"

    you "Well, we don't have many other choices, do we."

    girl_scientist "I-I guess it's too late to send for heavy equipment. Hmm... Let's try it your way then..."

    "Carefully using her love juice to lubricate her nether regions, you start fingering her pussy, while pushing your thumb inside her asshole."

    "She starts moving her hips back and forth, grinding against your hand."

    girl_scientist "Hmm yes... I think we are getting a reaction..."

    show bg guest3_sex6 with dissolve # wet + squeal

    play sound s_ahaa

    girl_scientist "Ahaaa! [emo_heart]" with vpunch

    play sound s_sucking

    "Increasing your pace, you feel her body reacting nicely. Using your free hand, you start kneading her butt."

    girl_scientist "Keep going... Ohhh..."

    "You continue for a while, but she stays on the brink of orgasm, not quite getting there."

    girl_scientist "I don't know... I don't think it's working... I feel hotter and hotter..."

    girl_scientist "We're gonna need a bigger boat."

    you "Well... I think I have just the thing."

    show bg guest3_sex7 with fade # x

    play sound s_moans

    girl_scientist "Aaaah yes!!! [emo_heart]" with vpunch

    "She squeals with pleasure as you push your erect cock inside her slimy wet pussy, still twitching your thumb inside her tight asshole."

    girl_scientist "This experiment is quite, aah... Unorthodox... But it just... Hmmm... Might work!" with vpunch

    "She grinds her hips against you, making sure your cock reaches as deep as possible inside her."

    girl_scientist "I think the mojo is about to release! It's w-w-working..." with vpunch

    play sound s_scream_loud
    show bg guest3_sex8 with flash # cin

    girl_scientist "UWAAAAAH!!!" with vpunch

    play sound s_orgasm

    with doubleflash

    "Slamming your dick inside her once more while grabbing her ass, you shoot your load into her wet pussy."

    girl_scientist "OH, AH, AAH!!!"

    show bg guest3_sex9 with flash

    "Taking your cock out, you spurt the rest of your semen all over her, even smearing the wall."

    girl_scientist "A-Amazing... So much mojo has been extracted. You must have a natural affinity for it..."

    you "..."

    girl_scientist "I feel the worse of the reaction is over by now. I will be able to recover..."

    girl_scientist "But wait, one thing is strange..."

    girl_scientist "You've been exposed to a burst of pent-up mojo too, you must be feeling very ill right now?"

    you "Ill? No. I'm feeling perfectly normal."

    girl_scientist "Really? H-How? The mojo should have made you horny as hell!"

    you "..."

    you "I don't understand... I'm always horny as hell!"

    girl_scientist "Interesting... *grumble* The subject has developped a natural immunity to mojo exposure..."

    girl_scientist "L-let me get my notes."

    scene black with fade

    "She bombards you with questions about your sexual habits and history. It is a long time before you can escape back onto the street."

    return

## CHAOS ##

label chaos_update():

    scene black with fade
    show expression bg_bro at top with dissolve

    chaos "It's that time of the month... I'm HUNGRY!!!"

    if not story_flags["first chaos refill"]:

        you "Wait, what was it you wanted already?"

        chaos "Girls! All I really want is girls!"

        chaos "I can fool around with up to four girls, or a single virgin would do me nicely..."

        $ story_flags["first chaos refill"] = True

    $ virgins = [g for g in MC.girls + farm.girls if g.has_trait("Virgin")]

    $ calendar.set_alarm(calendar.time+28, "chaos_update")

label chaos_update_menu():

    menu:
        "Choose which girls to share with Chaos. This will cost them some enery and sanity (and possibly their virginity)."

        "给他一个处女 (完全充能)" if virgins:
            $ prompt = "Choose a girl for Chaos (she will lose her virginity)"
            $ girl_list = virgins
            $ girl_nb = 1

        "给他四个女孩 (完全充能)" if len(MC.girls + farm.girls) >= 4:
            $ prompt = "Choose girls for Chaos (costs energy and sanity)"
            $ girl_list = MC.girls + farm.girls
            $ girl_nb = 4

        "给他三个女孩 (能量充足)" if len(MC.girls + farm.girls) >= 3:
            $ prompt = "Choose girls for Chaos (costs energy and sanity)"
            $ girl_list = MC.girls + farm.girls
            $ girl_nb = 3

        "给他两个女孩 (能量不足)" if len(MC.girls + farm.girls) >= 2:
            $ prompt = "Choose girls for Chaos (costs energy and sanity)"
            $ girl_list = MC.girls + farm.girls
            $ girl_nb = 2

        "这个月不行":
            scene black
            show bg chaos no girl
            with dissolve

            play sound s_sheathe
            chaos "What??? Am I supposed to go a whole month without feasting?" with vpunch

            you "I think you've been having enough fun lately."

            chaos "Why you... When I finally get back to my Daemon Prince form, I'll track down your reincarnation {size=-2} and then I'll pluck your nose hair one by one  {/size}{size=-4} and...{/size} *mufled noises*" with vpunch

            hide bg with circlein

            you "Good thing I bought that thick leather sash to wrap that sword in. It muffles that annoying sword's babbling mouth nicely."

            chaos "*muffled curses*"

            call chaos_swap(chaos_no_charge) from _call_chaos_swap

            return

    $ girls = multiple_choice_menu("Choose girls", [(g.fullname, g) for g in girl_list] + [("Back", "back")], nb = girl_nb)

    if girls == "back":
        jump chaos_update_menu

    if len(girls) == 1:
        $ girl = girls[0]

        scene black
        show bg chaos virgin
        with fade

        play sound s_moans_quiet

        girl.char "What... is happening to me... I feel strange..."

        play sound2 s_maniacal_laugh
        chaos "FUFUFUFUFUFU!!!"

        play sound s_orgasm_fast

        girl.char "Aaaaah!!!"

        $ girl.pop_virginity("chaos")

        call chaos_swap(chaos_full_charge) from _call_chaos_swap_1

    else:
        $ girl1, girl2 = rand_choice(girls, 2)

        scene black
        show bg chaos girls at top
        with fade

        chaos "Come here, my pretties!"

        play sound s_girls_laugh

        girl1.char "Oh, my, Mister Sword, you're so... Big..."

        play sound s_orgasm_young

        girl2.char "Oooh, aaah, aaaaah!!!"

        python:
            for girl in girls:
                if girl.exhausted: # Exhausted girls become hurt
                    girl.get_hurt(dice(3))
                else:
                    girl.tire(50)

                girl.lose_sanity(3)

        if len(girls) >= 4:
            call chaos_swap(chaos_full_charge) from _call_chaos_swap_2
        elif len(girls) >= 3:
            call chaos_swap(chaos_high_charge) from _call_chaos_swap_3
        elif len(girls) >= 2:
            call chaos_swap(chaos_low_charge) from _call_chaos_swap_4

    scene black
    with circlein

    return

label chaos_swap(it):

    python:
        for _old in (chaos_no_charge, chaos_low_charge, chaos_high_charge, chaos_full_charge):
            if _old in MC.items:
                MC.remove_item(_old)

    call receive_item(it, equip=True, use_article=False) from _call_receive_item_24

    return

label chaos(girl): # Called upon unlocking the 'Chaos' evil power (girl is the conduit)
    scene black
    show bg magic_cellar at top
    with dissolve

    "[girl.fullname]'s eyes go white and she collapses on the cold hard floor, completely drained."

    "Pulses of dark energy radiate from the center of the portal, where a strange shape begins to materialize."

    show bg magic_cellar at quake

    "At first it looks like a man, then it morphes into a towering beast-like figure."

    play sound s_thunder
    show bg chaos chained at top with doubleflash

    "Then it morphes again, and it finally settles on the shape of a long sword, chained by some sort of outlandish metal links."

    play sound s_thunder

    chaos "I... I have AWOKEN!!!" with doubleflash

    you "A talking sword... Fancy that."

    chaos "Who is this? Ah, a mortal cultist, I see..."

    chaos "Untie me, cultist, so I can run my dark blade through your puny human heart and feast in your blood..."

    you "No thanks."

    chaos "What did you say, cultist???"

    chaos "You dare question the will of your god, the mighty CHAOS?" with vpunch

    $ chaos_name = "Chaos"

    if MC.god:
        you "I follow [MC.god], you idiot. And last time I checked, {i}I{/i} was the one who summoned you in the first place."
    else:
        you "God? I bow down to no god, you fool. And last time I checked, {i}I{/i} was the one who summoned you in the first place."

    you "I'm [MC.name], by the way. And I am no cultist of yours"

    chaos "You arrogant little insect! I SHALL DEVOUR YOUR SOUL RAW, WITH JALAPENOS ON THE SIDE!!!" with vpunch

    chaos "..."

    chaos "......"

    chaos "........."

    you "So? Weren't you about to devour my soul, or something?"

    chaos "Well... It's a bit embarrassing. It seems I materialized as a sword. {i}Again{/i}."

    chaos "I wanted the Daemon Prince form damn it! The DAEMON PRINCE!" with vpunch

    you "You're not making any sense    ."

    chaos "Ahem, you see, as a Daemon Prince I could have easily devoured you whole, but as a sword I am more limited in my movements. I need a wielder."

    chaos "Could you please assist me? It's very simple, you just have to remove me from these pesky adamantium chains, and wield me, and then..."

    play sound s_maniacal_laugh

    chaos "FUFUFUFUFUFUFU..."

    you "What was that?"

    chaos "What?"

    you "That evil laugh you just did, FUFUFUFUFU."

    chaos "Was that an evil laugh? I was just clearing my throat."

    you "Okay then..."

    play sound s_maniacal_laugh

    chaos "FUFUFUFUFU..."

    you "You just did it again!"

    chaos "It's very damp here! I was just clearing my throat!"

    you "But... You're a sword... Do swords have throats?"

    chaos "My METAPHORICAL throat, you simpleton! Now do it, draw me!"

    you "*sigh*, what the hell..."

    play sound s_shatter
    show bg magic_cellar with dissolve
    call receive_item(chaos_full_charge, use_article=False, use_sound=False) from _call_receive_item_25

    "Drawing the sword with your right hand, you free it surprisingly easily from its bonds, which seem to break down of their own accord."

    play sound s_maniacal_laugh

    chaos "FUFUFUFUFU!!! I AM NOW FREE! LET ME REPAY YOU WITH DEATH, PEASANT!" with vpunch

    chaos "..."

    chaos "....."

    you "What is it this time..."

    chaos "I... You... Well..."

    chaos "Aw, it's embarrassing. I'm going to need your help again. It's very simple, would you be so kind as to impale yourself on my blade, pretty please?"

    you "No way! Why would I do that???"

    chaos "Well, if you tried to impale yourself on my hilt it wouldn't work very well, would it? Not with your puny human strength, at least..."

    you "I am not impaling myself on anything! I'm not that kind of guy!"

    chaos "It's very strange. I should have taken over your mind right now, leaving you an empty husk of yourself, ready to do my bidding."

    chaos "But it seems your mind is resisting me. And you don't even seem like you're putting in much effort."

    you "I'm not."

    chaos "I don't understand... I may be a little out of practice, but I should overcome your willpower with ease... Are you a mere mortal, peasant?"

    you "Look, sorry to interrupt your incoherent rambling, but you are in no position to dictate anything to me."

    you "I wield you now! It is {i}you{/i} who gets to serve me, not the other way around!"

    chaos "WHAT??? That is preposterous! I, a millenia-old greater daemon, serve a puny little mortal like you? I refuse!" with vpunch

    you "Fine. If I have no use for you then, I'll just throw you out in the junkyard."

    chaos "HA! You fool! I would soon be picked up by a random scavenger, and possess him. Then I'll come for you, and cut off your nose, ears and balls!"

    you "Okay, then I'll just take a rowboat and throw you down in the harbor. Happy?"

    chaos "What... You..."

    chaos "(Wait, being stuck in that stupid sword body for centuries... again? At the bottom of the ocean? I hate salty water, it makes me all rusty...)"

    chaos "Okay, okay, mortal, you've made your point. Perhaps we can strike a bargain."

    you "I'm all ears."

    chaos "{i}If{/i} I were to enter into a... {i}partnership{/i}, with you, what would it entail?"

    $ MC.rand_say(["wa: Well, a magic sword's always nice to have in a fight. I assume you have powers?", "wz: It's always interesting to study supernatural beings, I guess. I assume you are a master in dark magic?", "tr: Well I'm sure I could sell you for a pretty penny, unless of course you have something better to offer me?"])

    chaos "Of course! I am very capable, believe me. But there is one thing... To replenish my power, I need to feast. And you shall help me with that."

    you "Whoah, feast on blood and souls? You want me to slay people to fill your lust?"

    chaos "Ugh, blood and souls, come on, these are much too common... No, I want something truly rare... I want virgins!"

    you "Beg your pardon?"

    chaos "Virgins, [MC.name]. Give me a virgin, and can replenish my powers fully. Give me other girls, and I can still replenish some of my powers..."

    you "You want the blood of virgins?" with vpunch

    chaos "Nothing so crude, no! I will do them no physical harm, if this is what you're asking. In fact, they might just find it... Intensely pleasurable."

    you "And other harm?"

    chaos "Well, I guess their weak mind may frail a little, but I'm sure you've seen worse..."

    you "But I don't understand. You're a sword. What do you need girls for? You don't have a..."

    "You gesture vaguely at where you guess the sword's crotch is."

    chaos "That's none of your damn business, okay! I can manage perfectly fine!" with vpunch

    chaos "*silent sob*"

    you "Okay, okay..."

    chaos "So? Do you think this can be arranged? I need to replenish my powers, on a monthly basis."

    you "Well... I guess it shouldn't be too hard. After all, I am a brothel owner..."

    chaos "A brothel owner? Oh, but that's just perfect!"

    chaos "You can get me my monthly dose of sweet girls, and I can help you defend yourself among other benefits..."

    you "Well, these girls are hardly virgins, just so you know..."

    chaos "Oh well. Virgins are better, but if all you've got are loose women, so be it."

    chaos "(Nice catch, a brothel owner! He can send plenty of chicks my way, and I will hardly need to work at all! After all, how dangerous can a brothel owner's life be?)"

    you "I can hear you when you're mumbling, you know."

    chaos "*clears metaphorical throat*, ahem, I believe we have a deal. For this month, I'll just power myself using this wench's energy."

    "The sword's three eyes focus on [girl.name]."

    scene black with fade

    "Chaos provides a boost to your personal skills when wielded. The bonus depends on how many girls you provide him to play with at the beginning of the month (Chaos can instantly charge with a virgin, but she will be deflowered)."

    $ calendar.set_alarm(calendar.time+28, "chaos_update")

    $ unlock_achievement("chaos")

    return




#### END OF STORY EVENTS ####
