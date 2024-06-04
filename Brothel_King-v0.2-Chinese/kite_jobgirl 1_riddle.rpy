##################################################################
## Jobgirl events 1: How I met your Scarlet
##################################################################

## First chat between you and the adventurer
## the riddle is a simple quest requiring any particular effort from you to be solved


#######################################################################################
########## PART ONE - Introducing Scarlet
#######################################################################################

label jobgirl_0():

    $ NPC_jobgirl.love = 0 # This replaces the 'NPC_jobgirl.love' variable
    $ NPC_jobgirl.corruption = 0 # This replaces the 'NPC_jobgirl.corruption' variable
    $ NPC_jobgirl.flags["anika_sex"] = False # This replaces the 'anika_sex' variable. There is no real need to init this value to False as every NPC flag is set to False by default, but I have kept it here for clarity.

    scene black with fade
    show bg town at top
    show jobgirl with dissolve

    jobgirl "Hey there!"

    jobgirl "Looking for another quest? I noticed you come here often, you must be a busy adventurer!"

    you "Err, not exactly. The quests are not really for me; I have a group of, hem, workers, sometimes I get a job request here for one of them."

    jobgirl "Oh, really? I could have sworn you were the adventurous type of guy..."

    you "Well, I can assure you that my life is not lacking in adventures at all! *wink*"

    play sound s_kind_laugh

    jobgirl "Ahah! Well, at least you have a sense of humor. So, which kind of job are you looking for your subordinates?"

    you "Sorry but... It's private business. We don't even know each other!"

    jobgirl "Oh sure, sorry I forgot to introduce myself... Call me Scarlet."

    you "Scarlet?"

    $ jobgirl_name = "Scarlet"

    jobgirl "Yeah, it's my battle name. We adventurers must defend our true identities to prevent the evil we fight from harming our beloved ones..."

    jobgirl "And some girls not working on the 'adventuring' side like to use fake names too, lest their dad finds out..."

    you "I'm sure they do."

    you "Well, my name is [MC.name]. Scarlet, was it? Wait, how did you come up with such a nickname? Did you get it from a fairy tale?"

    jobgirl "Hey!!!" with vpunch

    jobgirl "What's wrong with my nickname? My hair is red, so I chose 'Scarlet' as my personal battle name!"

    you "Oh. I was hoping it would come with a better story."

    jobgirl "Shut up! It's a cool name, and I like it."

    you "Ok, ok, don't get mad! I won't bug you anymore about your name."

    jobgirl "Good, and it would be even better if you promise to stop being rude in general."

    jobgirl "Do you always treat girls like that? I bet you're still single, aren't you?"

    you "Uhm, actually... Now that you mention it, I must admit I'm not into any romantic relationship. My job keeps me busy..."

    jobgirl "I see... I guess you chose your job over women, haven't you?"

    you "Well, I wouldn't say that... Women are the most important part of my trade. They need constant training and management..."

    you "A brothel doesn't run itself, you know?"

    play sound s_surprise

    jobgirl "A brothel? So you're a pimp, right?"

    you "Well..."

    jobgirl "Ahahah, that's why you cannot find a girl!"

    you "On the other hand, I do have an active sexual life, just to inform you. So many girls from which I can choose to bring in bed with me."

    jobgirl "You may feel lucky, being surrounded by so many girls, but how many of them are special to you? Are there any girls you don't want to share with clients? Special ones?"

    ## choice menu 1) yes 2) no
    menu:
        "My slave Sill":

            you "There is one, my first slave, Sill; I don't let anyone put their hands on her, she's mine only!"

            jobgirl "I see. So, even a pimp can have a heart after all. Interesting..."

            $ NPC_jobgirl.corruption += 2

        "I wish I had one":

            you "I deal with pretty girls on a daily basis, but you can guess how my job is a great obstacle for a true relationship."
            you "Some people consider slavery and whoring immoral, others just don't want to have any sort of business with a guy like me. Furthermore, I think I haven't encountered the right girl for me yet."
            you "I'd like to have a girlfriend, I'm human after all..."

            jobgirl "I see. Your feelings are sincere, I can see it. I hope you're going to find her very soon."

            $ NPC_jobgirl.love += 2


    you "Now, what about you? Do you have a boyfriend?"

    jobgirl "Me? Mmh, well, let's say that my job doesn't really make me an ideal homemaker."

    "You both laugh. You feel more relaxed and spend some time chatting."

    "You learn that Scarlet lives here in Zan, in a tiny house near the plaza. She spends a lot of time running short quests."

    jobgirl "Small quests are easy and don't take much time, so I do a lot of them, having more fun and less risks than doing a single, difficult one. Plus, in this way I can help more people! Isn't it perfect?"

    you "I guess so. You don't seem bored at all, always smiling around."

    "One hour passes by while your conversation with Scarlet goes on."

    you "Oh shit, I have to hurry! Sorry Scarlet, business calls. It's been cool to know you better, I hope we can meet and talk again."

    jobgirl "Sure [MC.name], I enjoyed our time together too. You know where to find me *winks*. See ya!"

    you "(I must admit it, that girl is impressive.)"

    hide jobgirl with dissolve

#     "(Visit the {b}posting board{/b} to see her again)"

    $ NPC_jobgirl.flags["stage"] = 1

    return

#######################################################################################
########## PART TWO - The riddle
#######################################################################################

label jobgirl_1():

    stop music fadeout 3.0

    scene black

    show bg town at top

    with fade

    show jobgirl with dissolve

    "You reach the posting board plaza looking for some more quests for your girls, when you notice Scarlet sitting on a bench nearby."
    "She's totally absorbed in reading what seems to be an old scroll. "

    jobgirl "Hey, [MC.name], glad to see you around again! What brings you here today? Business as usual?"

    you "Hi Scarlet. That's right, I've come to see if there's any good quest for my girls. And you? What's that scroll?"

    jobgirl "Ah, this. It's a request from a client, a scholar who was trying to decipher it. I found it a few days ago and sold it to the guy, then he asked me to find a way to translate it."
    jobgirl "But I'm no scholar. I only managed to get a raw translation but it's not enough to understand its meaning!"

    you "A scroll, uh?"

    jobgirl "Yeah, an ancient one. The more I try to figure out what's written on it, the more my head hurts!"
    jobgirl "It's very difficult. Would you mind giving a hand to a damsel in distress? *winks at you*"

    you "Yeah sure, whatever... Let me see what's distressing you, little damsel..."

    play sound s_kind_laugh

    jobgirl "*laughs* You're a funny guy, has anybody ever told you that?"

    hide jobgirl

    show jobgirl_riddle at top with fade

    "She hands the scroll to you. The paper seems very old, the text is written in an old form of Xeros's common language, something you can handle easily."

    you "Let's see... Mmmh... This could be that, so this word can mean... and this one, should mean..."

    jobgirl "*anxious* Sooo, did you get any hints? A translation?"

    you "This is... a riddle?!" with vpunch

    play music m_jobgirl_1_suspence fadein 3.0 # It's better to use fadein when starting a music. I usually set it up for 3 seconds

    play sound s_dress

    call screen letter(header = "{font=[gui.yishu]}神秘信件{/font}", message = "　　王子啊，你要知道\n在那几年之间亚特兰蒂斯沉没和金碧辉煌的城市\n谢罗斯之子崛起的岁月，在太阳升起时站在四边，在众多星星下站在三边……\n汝应命名为继任者")

    play sound s_dress

    jobgirl "A riddle, uh? Interesting. It makes sense, since I found it in the Alikr desert, under a statue of a strange monster."

    you "A winged lion with a human face?"

    play sound s_surprise

    jobgirl "H-how did you know that?" with vpunch

    you "I'm just lucky to know the legend of the Sphinx, an ancient monster who loved to trap travellers and dared them to solve her riddles. Those who fail her trial are devoured."

    jobgirl "Eew, I hope I won't ever meet one in my lifetime!"

    you "Don't worry, it's just a myth, nobody has ever found such a creature as far as I know."

    jobgirl "Good to know. Soo, what's the riddle's solution?"

    you "You want me to solve it too? What if I get the wrong answer? Will you devour me?"

    jobgirl "Gross! I'm not a monster, you know?"

    you "Ahah, I know... I was teasing. You're just a cute, innocent girl..."

    jobgirl "*blushes* D-don't mock me now... idiot... Anyway, the scholar is generous, so I don't mind sharing the pay If you want."

    you "Ok, let's see then..."

    $ answer = renpy.display_menu([("免费提供答案", 1),("索要金币", 2),("取笑她……只是有点", 3)])

    $ renpy.block_rollback()

    if answer == 1:

        you "This riddle is quite ancient, did you know that?"

        jobgirl "Really? I've never heard of it before. However, it explains why it's written in such a weird way..."

        you "Good point. Now the solution is-"

        jobgirl "Wait, are you giving me the answer without asking for a reward?"

        you "A reward? Do people usually demand damsels in distress a reward for rescuing them?"

        jobgirl "*smiles* Hihi, I guess they don't... Anyway, thank you very much!"

        "The girl approaches your face and gives you a soft kiss on the cheek."

        $ NPC_jobgirl.love += 10

        jobgirl "This is just to let you know that damsels in distress appreciate their savior's help. *winks*"

        you "Ehrm, thank you, I guess... So, as I was saying, the solution is..."

    elif answer == 2:

        you "Aren't you forgetting something babe? Since this is a help request, there should also be a reward, am I right?"

        jobgirl "Wait, are you asking to be compensated for {i}this{/i}? Seriously?"

        you "Try to understand, I'm a businessman and this is just another job. If it was this easy, you would have done it yourself. How about a hundred coins?"

        jobgirl "(*stares at you from head to feet*) Did they ever tell you that you're as cold as an iron bar? Are you sure you have a beating heart in your chest?"

        you "There's no need to say such things, you know? I'm not asking for the moon, just a small reward for a small task, that's all!"

        jobgirl "Yeah, whatever. Fine. I'll pay you."

        "She gives you a small bag of coins."

        play sound s_gold

        $ MC.gold += 100

        $ NPC_jobgirl.love -= 5

        jobgirl "Happy now?"

        you "Deal. So, here's the solution..."

    elif answer == 3:

        you "You really got it a few days ago and didn't get the solution yet?"

        play sound s_surprise

        jobgirl "Hey, what are you blabbing about!!! I'm not stupid, you know?" with vpunch

        you "Don't get narky darling, didn't mean any offense, it is just... well, the riddle is quite simple, it's also quite old and famous, don't you know?"

        "She stares at you, giving you the impression she's a bit resentful, so you wield your best smile, hoping she'll calm down a little and forgive you."

        jobgirl "Ok, ok, I'll let it slide this time, but don't be mean to me again or I'll make you pay..."

        jobgirl "Now tell me what the answer is, or I'll never be able to sleep again!" with vpunch

        "Now that she mentions it you notice she looks tired and drowsy. She probably hasn't slept since getting the scroll, trying to solve the riddle!"

        you "Right, no more jokes, I promise. Now, let's see, the solution should be..."

## riddle menu loop

    $ riddle_loop = 1

    while riddle_loop == 1:

        $ solution = renpy.display_menu([("A Protoceratops", 1),("Molise", 2),("Man", 3)])

        if solution == 1:

            "You don't want her to be mad at you, right? Try again!"

        elif solution == 2:

            "Don't you know it? Molise doesn't exist! Try again!"

        elif solution == 3:

            $ riddle_loop = 0

## riddle menu loop off

    stop music fadeout 3.0

    hide jobgirl_riddle with fade

    show jobgirl

    you "Man."

    play sound s_surprise

    jobgirl "Which one?" with vpunch

    you "Mankind in general, doofus..."

    you "I can explain the solution if you want."

    "She doesn't look very convinced."

    jobgirl "Nah... Not now, at least. I'll give it to the client to get my reward! *smiles happily*"

    you "Alright then. So, how much will he pay you?"

    jobgirl "The guy is very rich, he'll pay me a thousand coins for this job!"

    you "Wow, not bad!"

    play sound s_sigh

    jobgirl "I'm so relieved... Now I don't have to worry about my outgoings for a long time!"

    you "Congratulations. What will you do with all that money?"

    jobgirl "I definitely want to spend a small sum for fun! Gonna plan a trip to the beach as soon as possible. Ooh my, I need a new bikini, and a lot of exercises to get fit for it!"

    hide jobgirl_riddle
    show jobgirl
    with fade

    "Lost for a moment in her thoughts and plans, she suddenly sprints to take her leave, but..."

    show jobgirl

    with dissolve

    play sound s_dodge

    show jobgirl:
        linear 1.0 zoom 1.5 ypos 1.3

    "She miscalculated the distance between you and her. She ends up falling right in your arms."

    play sound2 s_punch
    with vpunch

    "You almost fall back but manage to stand; she's light but quite energetic." with vpunch

    play sound s_surprise

    jobgirl "Ooh, sorry, uhm... *blushes*"

    "You look at her beautiful blue eyes, down to her pink lips and white skinned neck, until you stare at her cleavage. Can't avoid to look at her breasts since the feeling of them pushing on your chest is raising your heartbeat."

    $ hug_action = renpy.display_menu([("你现在想怎么做？", None), ("浪漫一点", 1),("评论她的乳沟", 2),("等待她的反应", 3)])

    if hug_action == 1:

        you "Holding you in my arms is the best thing I could ever hope for... I wish I could catch you again soon."

        "The girl is so embarrassed that she can't help but stare down. She blushes so much that her face seems about to catch fire."

        $ NPC_jobgirl.love += 10

        jobgirl "Thank you, gallant knight... You do know how to speak to a woman. My mom always said I was a catch, I guess you just proved it! *wink*"

        you "Don't mention it. And please let me know if you need my help again, it will be my pleasure to come to the rescue again."

        play sound s_dodge

        show jobgirl:
            linear 0.5 zoom 1.0 yalign 1.0

    elif hug_action == 2:

        you "I see... I think you're ready for the bikini test right now! I know very few girls more fit than you... And even less girls with such a good figure!"

        "She leaves your arms and steps back a little."

        play sound s_dodge

        show jobgirl:
            linear 0.5 zoom 1.0 yalign 1.0

        jobgirl "Really? Do you think I'm in good shape?"

        you "I dare say fantastic shape. You can definitely wear any bikini, with such eyes no man will be able to keep his stare away from you!"

        "At your words she looks at her cleavage and naively pulls her top down a little."

        hide jobgirl

        show teasing_cleavage with dissolve

        jobgirl "What, these?"

        play sound s_horn

        you "Wow!" with vpunch

        jobgirl "Are they really as beautiful as you are sayin-"
        jobgirl "EH! Don't stare!" with vpunch

        hide teasing_cleavage

        show jobgirl with dissolve

        you "I don't want to be rude, but... I really enjoyed the view!"

        play sound s_laugh

        jobgirl "Yeah, I'm sure you did. You'd better cherish that memory, because there won't be another one!"

        you "Oh, don't be shy, we both know you liked it, admit it..."

        "She blushes a little."

        jobgirl "N-no way!..."

        $ NPC_jobgirl.corruption += 10

        you "Anyway, feel free to ask for my help again, anytime."

    elif hug_action == 3:

        "Without saying a word, you look at her while gently holding her close to you."

        "After a long moment she timidly steps away, a little embarrassed."

        play sound s_dodge

        show jobgirl:
            linear 0.5 zoom 1.0 yalign 1.0

        jobgirl "You've saved me a second time today. You're very useful, you know?"

        you "I just like to be helpful, that's all."

        jobgirl "You say so, but in this city, most people think helping someone else is a waste of time. Especially those in your field. You are quite the whitefly. *smile*"

        "You look at each other for a long moment."

        $ NPC_jobgirl.love += 5
        $ NPC_jobgirl.corruption += 5

        you "I have to go now, my business needs my attention. Come and see me anytime, if you want. You'll be welcome."

    jobgirl "Thank you, really! If it wasn't for you, I'd still be on that stupid riddle! See ya!"

    you "Bye!"

    hide jobgirl with dissolve

#     "(Wait a few days for a new morning event.)"

    $ current_season = calendar.get_season()

    if current_season in ("summer", "spring"):
        $ x = 2
    elif current_season == "winter":
        $ x = 28 * (4 - calendar.month) # Waits until spring
    elif current_season == "fall":
        $ x = 28 * (12 - calendar.month + 4) # Waits until spring

    $ calendar.set_alarm(calendar.time + x, StoryEvent(label = "jobgirl_beach_1", type = "morning"))
    $ NPC_jobgirl.flags["stage"] = 2

    return
