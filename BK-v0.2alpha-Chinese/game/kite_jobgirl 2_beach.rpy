##################################################################
## Jobgirl events 2: beach
##################################################################

## This is the beach chain events for jobgirl
## First part: MC discovers where the girl goes on the beach
## Second part: MC meets her at the beach, where they will enjoy a great sunny day with her friend Anika
## Third part: MC can flirt with Anika
## Fourth part: MC gets a chance to have sex with Anika, his choice will influence future relationship with the two chars
## Fifth part: Mc spends some time on the beach alone with the jobgirl and something may happen...


#######################################################################################
########## PART ONE - 'Lifeguard exam'
#######################################################################################

label jobgirl_beach_1():

    stop music fadeout 3.0

    scene black with fade

    show expression bg_bro at top

    "You wake up early this morning; it is a hot sunny day, and you are in desperate need of fresh air."

    you "It's a perfect day to go for a swim... I could go to the beach, watch girls in their hot swimsuits..."

    "You suddenly remember something."

    you "Sill! Come over here!"

    play sound s_steps

    pause 0.5

    play sound2 s_door

    show sill with dissolve

    sill sad "Master, *pant*, I'm making breakfast, what do you need? *pant*"

    you "Get your lazy ass in here. You remember that task I had for you? Follow that adventurer chick and find out where she goes swimming?"

    sill "Uhm, yes, I remember..."

    sill happy "You said you wanted to make sure she wasn't going to drown, right? Don't worry, she's an excellent swimmer."

    you "Show me on the map, I better double check... It's for my, uh, volunteer lifeguard exam! Of course! Haha, haha, haha..."

    sill "Really, uh... Well, it was around here. Is that all, Master?"

    you "Wait! Ahem... Can you describe what she was wearing?"

    sill "What? How is that relevant to the lifeguard exam???"

    you "Well, uh, I have to, you know..."

    you "I must make sure she doesn't expose herself too much to the sun! She could get sunburns, and, uh, cancer, and you know... Sun sickness! Lifeguards have to care about those things!"

    sill "Oh..."

    sill sad "Master, that's terrible!!!"

    you "What?"

    sill "She's wearing very little! There's barely any fabric to protect her! Her skin is totally exposed... Her bikini is so tight that..."

    you "By the gods! This is terrible! I have to intervene right away!!!"

    play sound s_steps

    sill sad "Master! Hey! Master!"

    play sound s_door_close

    sill "He forgot his breakfast..."

    sill happy "Still, it's nice to see Master [MC.name] cares so much about his lifeguard exam."

    sill "He's quite the model citizen! *smile*"

    "('Lifeguard' duty: Visit the {b}beach{/b} to track the adventurer.)"

    $ story_add_event("jobgirl_beach")

    return


label jobgirl_beach():

    if NPC_jobgirl.flags["stage"] == 2:
#        $ NPC_jobgirl.flags["last event"] = calendar.time
        $ event_dict["jobgirl_beach"].date = calendar.time + 7
        call jobgirl_beach_2() from _call_jobgirl_beach_2

    elif NPC_jobgirl.flags["stage"] == 3:
        $ event_dict["jobgirl_beach"].date = calendar.time + 7
        call jobgirl_beach_3() from _call_jobgirl_beach_3

    elif NPC_jobgirl.flags["stage"] == 4:
        $ event_dict["jobgirl_beach"].date = calendar.time + 7
        call jobgirl_beach_4() from _call_jobgirl_beach_4

    elif NPC_jobgirl.flags["stage"] == 5:
        $ event_dict["jobgirl_beach"].date = calendar.time + 7
        call jobgirl_beach_5() from _call_jobgirl_beach_5

        $ story_remove_event("jobgirl_beach") # Change this line when the story advances further

    return


#######################################################################################
########## PART TWO - Meet Anika
#######################################################################################

label jobgirl_beach_2():

    scene black with fade

    show bg sky day at top

    "You head for the location indicated by Sill. You don't know what to expect once there, but you start fantasizing about the redhead adventurer. You still have in mind how things went when she asked for your help with that stupid riddle."

    you "(A bit crazy and obviously not a genius, but damn she's smoking hot! Her cleavage and buttocks almost gave me nosebleeds last time!)"

    you "(Now, I'm going to surprise her at the beach. She's wearing a skimpy bikini...)"

    you "(Oops, here comes the nosebleed again!)"

    "You think about her the whole time, until you arrive at the beach. You have to concentrate, otherwise you will not find the spot Sill showed you."

    "You start looking for the place where you expect to find the adventurer."

    you "(There she is... Oh, gods...)"

    show beach_arrival at top with fade

    you "(This is definitely my lucky day!)"

    "You approach her with a calm pace, in order to gather your thoughts, calm down and control your little friend that is threatening to pop out of your trunks."

    "Next to her, another girl is taking a sunbath. You give a fast look at her: black hair, fair skin, eyeglasses, gorgeous body..."

    you "(Based on what Sill told me, the two girls often come here together. It will be difficult to spend some time alone with her.)"

    you "(Nevermind, just seeing her in a bikini makes the trip worth the effort.)"

    "As you approach, the girl notices you and immediately jumps off her beach bed to greet you."

    hide beach_arrival with dissolve

    show bg beach at top
    show jobgirl_bikini with dissolve

    jobgirl "Hey there! [MC.name]! My favourite soft-hearted pimp who helps damsels in distress! *wink*"

    you "Hey! You shouldn't say what I do for a living so loudly, you know? People around may get embarrassed."

    jobgirl "Oh, really? I don't care. Half the girls on this beach are sluts, only they don't have the sense to get paid for it..."
    jobgirl "What brings you here by the way? It's quite a coincidence..."

    you "Smart girl. You know the answer, I've told you last time: you drive me crazy. No reason to hide it."

    jobgirl "Ew! A stalker? Still, I'm flattered, I guess. But now..."

    "She pushes you away gently, like last time."

    jobgirl "Let me introduce you to my dear friend Anika. Anika, this is [MC.name], the one and only. *winks at you*"

    hide jobgirl_bikini with dissolve

    show beach_friend_1 at left

    anika "Nice to meet you [MC.name], I was looking forward to see you in person, after all I've heard about you. *malicious smile*"

    you "Really? I hope you only heard good stuff..."

    anika "Yeah yeah, she wouldn't stop going on about you. How you're really smart and helpful, solved that ancient riddle in no time, and so on."

    "The redhead girl blushes intensely, her cheeks getting almost as red as her hair."

    you "That's... Good to know. Say, I wanted to ask you something: our friend here didn't tell me her true name yet, so I was wondering if you could solve {i}that{/i} riddle for me."

    anika "Her true name? Oh oh, I see, she didn't tell you, and I can guess why..."

    anika "Sorry [MC.name], but you have to wait until she is ready to tell you. That, or you can try and guess... Good luck with that."

    jobgirl "I won't tell you! Bleeeee! *makes a face*"

    you "So, am I supposed to call you Scarlet all the time?"

    jobgirl "Sure thing! We spoke about it before, right? Why are you insisting?"

    you "Well, because that's not your true name, it's just... how do I call it, an art name..."

    jobgirl "One day, perhaps, if we get more acquainted. Don't press it, ok?"

    you "Fine, I won't bother you anymore with it. So be it, I'm going to call you Scarlet all the time."

    jobgirl "Finally! *smile*"

    "She gives you a quick kiss on the cheek."

    jobgirl "Now time to take a swim! Let's gooooo!!"

    hide beach_friend_1 with fade

    "She runs for the sea like a hurricane, trampling everybody along the way. Anika shakes her head, then tries to catch up with her, apologizing to the bystanders for her friend's behavior."

    you "It's confirmed: she's really crazy... and hot."

    "You follow them to have a good time in the water."

    scene beach_friend_2 at top with dissolve

    play sound s_splash

    jobgirl "Yeeeeh! The water is great! Take this, Anika! *Splashes water*"

    anika "Heyyy, I wasn't ready for that! It's not fair!"

    "The girls enjoy swimming and playing in the water. Soon, water droplets shine over their skin, as the sunlight approaching noon intensifies. You are fascinated by their beauty."
    "On second inspection, Anika is just as hot as Scarlet, although a lot more subtle. Scarlet is so cute, energetic and carefree, but Anika has an even bigger rack, and she's got a perverted look about her. Maybe it's the glasses."
    "It would be hard for anyone to choose between them if asked to. They would choose both in an instant, if given the chance."
    "...at least, {i}you{/i} would!"

    anika "Payback time! Here comes the tickling!"

    jobgirl "Oh no! I hate it! NNuoahahah! Pleaseeahah stop! uhnaaahahah!! EEk! I'm losing my top!"

    you "(*huge nosebleed*)"

    scene black with fade

    "(Visit the {b}beach{/b} again after some time to progress your relationship.)"

    $ NPC_jobgirl.flags["stage"] = 3

    return

#######################################################################################
########## PART THREE - Drink event
#######################################################################################

label jobgirl_beach_3():

    scene black with fade

    show bg beach at top

    "Another day at the beach with Scarlet and Anika."
    "After an hour spent playing and swimming in the sea, you head back to the shore. The girls dry themselves and lay down their towels under the sun."

    show beach_friend_3 at top with dissolve

    you "(Damn, after witnessing such a view, a man can die happy!)"

    you "(Better focus on something else, otherwise I'll need to 'relieve' myself in the bathroom)."

    hide beach_friend_3 with dissolve

    show anika at left

    anika "Hey, you seem concerned about something. What could that be... *sarcastic look*"

    show beach_stand_1 at right

    jobgirl "Worried? After all the fun we got today? I don't think so!"

    "Before she can notice something is going on under your trunks, you take a towel and wrap it around your abdomen."

    you "Just some minor thoughts that business men have sometimes... Nothing to worry about... Do you girls want something to drink?"

    anika "Why not? There is a small kiosk over there, the owner uses magic to keep beverages cool; I'd like to have a fruit cocktail, if you don't mind bringing me one, dear..."

    jobgirl "Ani, are you okay? You shouldn't drink alcohol while sunbathing, it's dangerous..."

    anika "Oh come on, let's celebrate a new friendship! Alcohol is mandatory for a toast! Try one and stop complaining! For your best friend, please..."

    jobgirl "*heh* Alright, I'll join you this time, but don't make it a habit."

    anika "Sure thing!"

    hide anika with dissolve
    hide beach_stand_1 with dissolve

    "You take your coin purse and head towards the direction Anika indicated."
    "The kiosk for cool drinks is not so far; you order two cocktails for the girls."

    $ chosen_drink = menu([("你想喝什么？", None), ("浓烈的啤酒", 1),("和女孩一样", 2),("一种果汁", 3)])

    you "It's nice and fresh! Man, ice magic is really awesome..."

    show beach_friend_2 at top with fade

    if chosen_drink == 1:

        "You come back with the drinks, and when everyone has his own in hand you make a happy toast for the good day you're having. Anika looks pleased about the drink you chose for yourself, while Scarlet seems a little disappointed."

        $ NPC_jobgirl.love -= 1

    elif chosen_drink == 2:

        "You come back with the drinks, and when everyone has his own in hand you make a happy toast for the good day you're having. Both girls are happy you took the same cocktail for everyone."

    else:

        "You come back with the drinks, and when everyone has his own in hand you make a happy toast for the good day you're having. Anika looks a little displeased about the drink you chose for yourself, while Scarlet seems pleased you took her advice concerning alcohol."

        $ NPC_jobgirl.love += 1

    hide beach_friend_2 with dissolve

    "After the toast and some more fun in the water, you spend the rest of the day getting some more tan and chatting about various gossips."

    "Most of the conversations are about Scarlet's latest quests. You learn she lives right next to the posting board in order to get the best jobs first. But she also likes to help newbies getting jobs."

    show beach_stand_1 at right with dissolve

    jobgirl "I believe there is always a good quest for everyone, the secret is to know which skills are required for which job and how good you are with such skills. Then it's only a matter of finding a match!"

    "The time goes by, soon the sun starts setting over the horizon. You start packing your things and get ready to head home."

    jobgirl "When will we come back, Anika?"

    anika "Don't ask me, you're the one that has a job! I have plenty of free time."

    you "Seriously Anika? If you don't have a job, how do you get money for going out? That swimsuit alone is designer-made, it looks expensive..."

    anika "Uhuhuh, I thought you could have figured that out by yourself, Mister genius.. There are a lot of handsome men trying to conquer my heart every day, giving me many expensive gifts just to go out with me."

    you "Uhm, I see... You're definitely a man-eater, poor souls..."

    anika "Just kidding. I'm just really, really rich. Or rather, my family is."

    jobgirl "Sure, sure, and you get lots of presents from boys... *laughs*"

    anika "Hey,! As my best friend, you shouldn't badmouth me..."

    "Before you part with the girls, they promise you that you will soon spend another day together, as long as you let them know when you have free time again."

    "(Keep visiting the {b}beach{/b} to meet Scarlet and Anika again.)"

    scene black with fade

    $ MC.interactions = 0

    "You have spent all your actions for the day."

    "(Keep visiting the {b}beach{/b} after some time to meet the girls again.)"

    $ NPC_jobgirl.flags["stage"] = 4

    return


#######################################################################################
########## PART FOUR - Anika's move
#######################################################################################

label jobgirl_beach_4():

    stop music fadeout 3.0

    "This morning, you are ready for another day at the beach; Anika sent you a letter inviting you to join the girls again at the same place, writing they will wait for you."

    you "(As a gentleman, I must honor a hot girl's invitation!)"

    "You leave your instructions for the day with Sill, then head to the beach. You worked hard lately, so you feel you need and deserve a day off."

    "Soon, you arrive at your now usual place, where you find Anika. Scarlet is nowhere in sight."

    show bg beach at top with fade

    show friend_sunbathing at top with dissolve

    you "Hello Anika, nice to see you. Where's Scarlet?"

    anika "Mmmh, hi handsome, she's on an errand somewhere out of town, so I'm all alone today... or better say {i}we{/i} are..."

    "Anika is laying down on her belly; her huge tits are almost bursting out of her swimsuit. She seems to notice what you are looking at and smiles mischievously."

    anika "Let's see if I can get her out of your head for just a day."

    you "Excuse me?"

    anika "Now now, no need to hide it, you got a crush on her, like every man she encounters. Am I wrong?"

    you "Well, I must admit she's an interesting girl, one of a kind..."

    anika "Do you want to fuck her?"

    you "What?!?" with vpunch

    anika "My my, why are you so embarrassed? I thought that with your job, you'd be more open-minded. Who knows how many naughty things you could do with that girl..."

    hide friend_sunbathing with dissolve

    show friend_teasing1 at top

    "While talking she changes position on her chair, getting on all fours. You can clearly see her huge breasts waving back and forth. She raises her butt and shakes it seductively."
    "If not for her swimsuit, you could clearly see her cunt. You realize that she's teasing you, but you're not sure if she really wants it, or she's testing you. Maybe she's got ulterior motives."

    menu:
        "Why, yes, I'd like to fuck her":

            you "Damn right I wanna fuck her, she's so hot! Are you going to help me or put a stick in my wheel?"

        "Who, me? Nope!":

            you "I'm not so mean. I don't want to do what you said. Nor am I looking to do 'naughty things' right now. For now I just want to know her better."

    anika "Mmh, we'll see... come closer, I wanna show you something..."

    hide friend_teasing1 with dissolve

    show friend_teasing2

    play sound s_boing

    anika "Do you like them? You can touch if you want..."

    you "Damn Anika, if you act that way I can't guarantee I will stay a gentleman! As they say, don't mess with fire or you end up burnt!"

    anika "Actually I'm not afraid to be fucked by you. You're a decent guy, nice looking, and based on the size of your bulge, well equipped! *winks*"

    you "No man can stand such a view without having an erection. I must admit you know how to play your cards Anika, but I want to know what are your intentions. Do you try to fuck any man who approaches Scarlet? Is it a sort of fidelity test?"

    play sound s_kind_laugh

    anika "*smiles* Oh boy, nothing like that! Your fantasy is really something! What a perverse bitch did you take me for? I just want to have sex with you, darling."

    hide friend_teasing2 with dissolve

    show friend_boobs

    "She gets closer, flashing her boobs to you. You start sweating a lot, and not because of the sun."

    anika "What are you waiting for? I bet you want to cum on my tits... I'm waiting..."

    play sound s_mmh

    show friend_boobs:

        ease 0.75 zoom 2.0 xoffset 0 yoffset +200
        pause 0.5
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0
        pause 0.5
        ease 0.25 zoom 2.0 xoffset 0 yoffset +200
        pause 1
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0

    "What do you want to do?"

    menu:

        "Pull out your cock":

            $ NPC_jobgirl.flags["anika_sex"] = True

            "Staring at her tits you feel your cock getting harder and harder, even knowing you're in a public and open place, you can't resist anymore."

            you "Get ready, here it comes your 'cream beauty treatment'!"

            hide friend_boobs with dissolve

            show friend_cum_body1

            anika "Mmmh, as I figured, your manhood is remarkable. It's a pity we have too much company, I would've gladly given it a taste..."

            you "Well, you can still tell me how you would enjoy it in your mouth..."

            anika "Oh naughty boy, you want me to talk dirty, do you? I like it."

            "She smiles seductively and stares at your full erect cock, while you start stroking a few centimeters from her chest."

            play sound s_mmh

            anika "I would start licking the tip a little... my tongue would then feel its full length, slowly but firmly... up and down... up and down..."

            "You raise the pace of your strokes while you imagine the scene she describes. It almost feels like she's doing it for real!"

            anika "My lips would wrap around the tip very slowly, so much that you would beg me to swallow it at once, but I wouldn't listen to you. I would start sucking your glans, while my tongue was still tickling its tip."

            you "Damn I wish I could try it for real some day, if you're half as good as I think you are..."

            anika "You can bet I am... and the best is yet to come! While sucking the glans, I would start feeling your cock inch by inch, every time swallowing a little more, until your whole length is inside me."

            anika "At that point I would stop before you cum... You would ask me to continue, you'd be almost there... Then I would swallow it again, but this time straight into my throat, and you would use all your willpower to not cum too soon. You would feel in paradise..."

            "She's whispering in your ear, her voice is a natural aphrodisiac to you. You can't take it any longer, feeling you're almost ready to cum."

            you "Almost... there... cumming now... prepare yourself..."

            anika "Yes, cover my breasts with your semen... aaah!!"

            hide friend_cum_body1 with dissolve

            show friend_cum_body2

            you "Hun!" with vpunch

            you "Here!" with vpunch

            you "Take this!" with vpunch

            "You unload your semen all over her breasts; she moans a little when she feels it on her skin."

            play sound s_sexy_sigh

            anika "It's hot... mmmh... you too are hot, baby. Nice load."

            "You notice she got wet down there, she must have enjoyed the moment as much as you did. Then you realize her fingers are a little wet too: she masturbated while you were 'concentrated' without you even noticing that."

            hide friend_cum_body2 with dissolve

            show friend_stand1

            anika "Thank you very much [MC.name], I enjoyed our little moment very much. Now I need a good shower. Feel free to join me... if you want more..."

            "She heads to the showers, her sexy walk accentuating the beauty of her thighs and butt. Even though you came a few seconds ago, your bulge raises up again."

            you "I would follow that perfect ass everywhere! Hey wait for me!"

            hide friend_stand1 with dissolve

            "Anika dashes into the locker room, she seems very amused. And she's very fast too! You decide to take some more time to make her wait a bit, then you enter the room. By the sound of the running water, she must be taking her shower already."

            play sound s_door

            play music m_rain

            "In the steam of the hot water you find her gorgeous silhouette."

            show friend_shower

            "She stares at you, especially at your full erect cock after you take off your trunks. Her expression full of lust inviting you to join her immediately without saying a word."

            "You approach her quickly, then you put your hands on her hips and gently force her to bend over. Without wasting time your cock enters her pussy, without any resistance."

            hide friend_shower with dissolve

            show friend_doggy at top

            "She starts moaning at the pace of your strokes."

            play sound s_moans_friend

            anika "Mmhmaaah, aah, so rough... mmmh, like that! Yes! Ah! Ah! Mmmh..."

            "The squishing sound of your dick coming in and out her cunt stands even above the showering water falling on your bodies and the ground."

            "She moans louder when you start stimulating her sensitive spots inside her vagina."

            anika "Aaah! Y-yes, there! Oh my gods! Mmmmhhh!"

            you "You're squeezing my dick... urgh..."

            anika "I-I'm close... cumming... m-more! Gimme more! Ahn! Aahn!"

            play sound s_moans_short

            you "Get ready for something special then. Here we go!"

            "You feel her cunt wrapping tighter around your cock, feeling like she's sucking it with her pussy; you make a last effort to hit her cervix with your final thrusts."

            you "Uhn!" with vpunch

            anika "Oh gods!" with vpunch

            play sound s_moans_short

            you "So tight!" with vpunch

            anika "Yes! Yes! Deeper!" with vpunch

            play sound s_moans

            "With such strong stimulations, she can't take it anymore."

            anika "Oh gods! W-what are you- Ahn, ahn, d-doing... d-don't stop! Don't you dare stop now! Mmh aaah! I'm... I'm... Aaaahum! Ah!" with vpunch

            hide friend_doggy with dissolve

            show friend_orgasm

            play sound s_orgasm_fast

            anika "Aaaaahh... uhm... anf... uff... ah... I... came... s-so good..."

            you "Now it's my turn!"

            menu:

                "Cum inside":

                    anika "Are you going to fill me with your semen?"

                    you "Is it a problem for you?"

                    anika "Mmh not now, I should not be on my fertile period. Go on, I wanna feel how hot it is inside my little naughty pussy!"

                    you "Urgh!" with vpunch

                    play sound s_moans_short

                    anika "I... aaah... came again..."

                "Pull out":

                    "A few instants before you ejaculate, you pull your cock out of her, then shoot your load on her buttocks."

                    play sound s_mmh

                    anika "Uhmm, I can feel how hot it is despite us taking a hot shower..."

            with fade
            $ unlock_achievement("h anika")

            you "You're amazing... Best sex I've ever had under a shower... and I did it so many times!"

            "Anika takes a moment to recover, then she puts her swimsuit on. Her expression is quite unreadable."

            hide friend_orgasm with dissolve

            show anika

            you "Hey Anika, Is something wrong? Did I do anything that bothers you? You don't look satisified..."

            anika "Oh, don't take me wrong, I'm fully satisfied by your bed skills, in fact I haven't had such an orgasm in months..."

            you "So why do you look so grave now?"

            anika "To tell you the truth, I've put you to a test. It's something I did in the past for my friend, to see if the man of the moment would be good for her or not."

            you "I knew it! Damn, so I guess I've failed your test since we had sex, right?"

            anika "It's not that simple [MC.name], it's not up to me to judge you. I will tell her what we did here, plain and simple. Especially how good you are in bed."

            anika "Well, I suspect she already knows you have some skills in that field since it's your job. I guess I will just confirm her thoughts. Anyway..."

            you "What else?"

            anika "I can't blame you for having sex with me since you are not engaged to anyone right now, am I right? You're free, I'm free, we had some fun. That's all."

            you "Did you just use me like a toy then?"

            anika "Speaking of that, I think you do the same with the girls in your brothel. Consider it a fair retribution. *winks*"

            anika "For once it's been a girl using you for sex, not the other way around. How do you feel?"

            you "Can't argue with that; I had a good time, you've been amazing. But don't pull my leg more than this, ok?"

            anika "Don't worry, I don't plan to test you again, or do any more tricks. But today I had to act like this, for my friend's sake. Can you understand how much I'm worried for her?"

            you "Honestly not much. She seems to be able to take care of herself; I bet she has a lot of men around, so what's the problem?"

            anika "Indeed she gets a lot of attention, but try to understand what kind of people are hitting on her."

            "You reflect on Anika's words and imagine Scarlet spending her time at the posting corner, looking for a quest, or somewhere out in the countryside."

            "Then you realize that the average man she can meet in her life is the classic improvised adventurer, a guy who barely knows how to handle a weapon, less much how to deal with a woman."
            "This, when she's lucky; otherwise the choice is among bandits, ruffians and other infamous adventurers."

            anika "Look at your face! *smiles* You got my point then. Now you understand how much I was worried for her when she started talking about you: a man who can turn any girl into a slut at his service!"

            you "Hey, don't exaggerate, you're describing me like a monster!"

            anika "It's exactly how I thought you were. A danger to my friend. I couldn't let you take her and make her become your next brothel girl!"

            you "You mean you sacrificed yourself; what a good friend you are... but from my point of view you just wanted to be screwed by me since you laid eyes on me."

            anika "Umpf! That's a low blow... I can't deny you're a nice guy, good in bed and everything... so yes, I was curious to see how much I could have fun with you."

            you "And...?"

            anika "Oh come on, we had a good time, I told you I haven't felt that good for a while. What else should I say about it?"

            you "I just want to know if I ruined my chances to go out with your friend, that's all."

            anika "You must find it out later yourself. Go talk to her after I'm gone... In the meantime, take a shower, a cold one."

            "She stares at your crotch for a moment; you follow her eyes and see your little friend taking new vigor, almost ready for another round."

            you "Fine with me. I'll take that cold shower. I suppose you'll be gone when I'm finished, so let's say goodbye for now."

            "She kisses you passionately, making your bulge even harder."

            play sound s_mmh

            anika "Until next time... don't make me wait too long..."

            hide anika with dissolve

            "You take a long shower, lost in thoughts on what happened with Anika and what little you've learned about her redhead friend."

            you "(If Anika is so worried about her being with me, there must be more to it than she told me. She's not a child after all. Even if she only knows assholes, the fact I'm good at hitting on girls is not enough to be so worried!)"

            you "(Or it is just a trick and she wanted to fuck with me, then make me feel guilty so that she doesn't appear to be the slut she is. Mmh, maybe this is the truth...)"

            "After a while you leave the locker room and go back home. Without the two girls around, you find no reason to stay here longer."

            stop music fadeout 1.0

            play sound s_door_close


        "Don't indulge her":

            you "Are you serious? We barely know each other!"

            anika "I didn't think you were so shy, since you fuck your sluts every day I figured you could give me a ride on your cock without any problem."

            anika "Or maybe there is something else, mmmh? You don't want to do it in front of her, am I right?"

            you "Who knows... by the way you're a very attractive girl, your body is gorgeous and all, but really, I can't do it now, sorry. Nothing personal."

            play sound s_laugh

            anika "Eheh, this doesn't happen very often, to be rejected by a man..."

            you "I can imagine, with such a body I'm not surprised that men fall at your feet."

            hide friend_boobs with dissolve

            show friend_stand1

            anika "Eh, this time it didn't work. What a pity... you will never know what you have missed. *winks*"

            you "I guess so. But I made a choice before and I want to respect it."

            anika "I see.. and I'm happy. Really. Well, a bit disappointed because I really wanted to have some fun with a handsome guy today, but the important thing is you seem to be a good person."

            anika "She deserves the best, maybe you could fit the role after all."

            you "What are you talking about?"

            anika "Eheh, it's women only stuff. *winks*"

            anika "For now let's just say that she got the wrong man more than once, and she's not taking any risks anymore."

            you "You make it sound so mysterious."

            anika "Not my intention to do that, it's just that I'd prefer you hear the story from Scarlet, if she's willing to share it with you of course."

            anika "I know her since before we moved to Zan, so it's natural I care about her like a little sister."

            you "Yeah I can understand. But promise me this: don't try to seduce me any more!"

            anika "Eheh, sorry I can't. As long as you're not Scarlet's boyfriend I'll decide whether or not I try to hit on you."

            you "Damn... well, sorry if I don't feel honored by such attention."

            anika "Ahah! You're so funny!"

            hide friend_stand1

            "You stay for a while then take your leave. You're still a bit upset about how Anika tried to seduce you on the beach."

            you "(What a mess: two hot girls before my eyes; on one hand Anika would let me screw her anytime but she seems to be such a slut; on the other hand Scarlet would take a long time to fall for me, can I even make it?)"

            you "(Nevermind, let's see what happens next and how it ends.)"

            scene black with fade

            "You leave the beach and go home."

    "(Visit the {b}beach{/b} one more time.)"

    $ NPC_jobgirl.flags["stage"] = 5

    return

#######################################################################################
########## PART FIVE - Alone with Scarlet
#######################################################################################

label jobgirl_beach_5():

    stop music fadeout 3.0

    "You have some free time today, so you decide to head to the beach again; hopefully you will find Scarlet there, even if you didn't send her any message you bet she's enjoying the warm sun of this beautiful day."

    show bg beach at top

  ## if MC fucked Anika in part 4

    if NPC_jobgirl.flags["anika_sex"]:

        "Your guess was right. She's standing at the same place, looking in the distance. You spot in that direction Anika waving her hand to say goodbye."

        show beach_sit

        jobgirl "Hey look who's here! Ani just left a couple of minutes ago and I was about to leave too, but now I changed my mind!"

        you "So I came right on time. Glad to see you again. By the way, why did Anika leave so early?"

        "She makes an inquiring expression when you name her friend; but at the same time she seems amused by the situation. You don't have a good feeling about this, like a mouse being played by a cat before it's eaten."

        jobgirl "Anika told me you both had fun last time you met each other. A lot of fun."

        you "Are you angry with me?"

        jobgirl "Why should I be angry with you? Are we a couple? I barely know you... I don't even like you."

        you "Well, sure, we're not... just acquaintances... right..."

        jobgirl "Hey what's up? Are you disappointed? I'm the one who should be! You screwed my best friend practically in front of me - well, figuratively speaking, since I wasn't there, but it doesn't matter!"

        you "Ookay, you're right, but now try to calm down a little-"

        hide beach_sit

        show beach_stand_1

        "She suddenly stands up with a jump, visibly angry."

        jobgirl "CALM DOWN MY ASS! DON'T YOU DARE TELL ME TO CALM DOWN!" with vpunch

        "For a whole minute she beats you blind with words. At first, some people around you got curious to see what was going on, then they got afraid of her temper and ran away."

        "When she finally stops yelling at you, the beach around you is deserted. Finally you manage to talk to her."

        you "Have you finished?"

        jobgirl "..."

        you "I take it as a yes. So, what are you angry for? We're not a couple, as you stated so clearly before; we're in a public place full of people-"

        "You take a look around; nobody in sight."

        you "Well, it {i}was{/i} full of people before... so why are you yelling at me? Are you a little child who lost her toy?"

        jobgirl "..."

        you "Or maybe there's more to it. Your friend Anika played a dirty trick on me, first seducing me, then telling you who knows what shit to get you so mad about me."

        jobgirl "She just told me that-"

        you "I don't give a shit about what she told you! And now you listen to what I have to say: you're a pretty girl and I want to continue seeing you, if and only if you can accept that I'm free to screw every single woman in this world, unless you want to be engaged to me."

        jobgirl "*blushes* S-sorry..."

        you "Second thing: be sure that I can be a good guy: if by any chance you find yourself in trouble, I would come and rescue you with no hesitation, even leaving a dripping pussy in the middle of a good fuck!"

        jobgirl "*blushes even more* Y-you don't need to be so explicit, you know?..."

        you "Good, I think now you know me better. But this argument ruined my mood, so I think I'll leave. Better if you leave too, the sun is setting soon. Don't want you to get a cold..."

        "You grab a towel and cover her shoulders with it. Looking at her face, you bet her cheeks can't get any more red, and not for the sun: she is so embarrassed that you can feel her trembling."
        "You decide it is time to push it a little further and give her a sudden kiss."

        jobgirl "!!!" with vpunch

        "She doesn't put up any resistance but stays rigid, shocked by your audacity. You end the kiss before she can react. Better to only make a short step this time, you think to yourself."

        you "See you next time."

        hide beach_stand_1 with dissolve

        show beach_surprised

        "You turn around and leave; you look back a couple of times to see her reaction: at first she stays frozen where you left her, then her legs lose strength and she falls on her knees on the soft sand."

        "Now you are curious how your next meeting will be, and when..."

        $ NPC_jobgirl.love -= 5

        $ NPC_jobgirl.corruption += 5

  ## if in part 3 MC didn't have sex with Anika

    else:

        "You luckily find her sunbathing; when you approach she raises her hand to greet you loudly."

        show beach_sit with fade

        jobgirl "Over here! You're my savior today! I need help!"

        you "Hi Scarlet, what's up?"

        jobgirl "Ouch, my shoulders are starting to burn, I need to put on more sunscreen... would you... if you don't mind..."

        you "I don't mind at all! On the contrary, it will be my pleasure to help you. I'm also good at massages, you know? Want to try?"

        jobgirl "Sure, why not?"

        you "Fine, lay down and enjoy."

        hide beach_sit with fade

        show beach_lay_down

        "You start to massage her whole back from her neck to her spine."

        play sound s_mmh

        jobgirl "Mmmh... there... it's good..."

        you "Not to brag, but I have a lot of experience massaging. I teach my girls how to do it to our customers..."

        jobgirl "And are your clients always satisfied?"

        you "It depends on how much the girl has learned when she serves them, but they usually are happy about the service."

        jobgirl "I see... if you teach as well as you can massage... they'll learn fast. Mmmmhh...."

        you "Can I ask you something?"

        jobgirl "Mmmm yes... right now you can do everything to me... Uhm n-not in that sense! I-I mean a-ask anything!"

        you "Hey don't be so rigid all of a sudden, or the massage won't have any effect. Relax... relax... good, that way..."

        you "I was thinking about your reaction every time you have to deal with... sexual topics. Even now, when you thought about something naughty."

        play sound s_surprise

        jobgirl "N-naughty? Me? W-what are talking about? I didn't do anything like that!"

        you "What did you imagine I would have done to you, when you told me I could have done {i}anything{/i} to you?"

        "You can't see her face but you're sure you can feel the heat of her cheeks blushing."

        jobgirl "Umph! It's just that... I'm not at ease with such things... sex and all the rest. I... never... not yet..."

        you "Uhm, so you're shy because you never had any experience... you're still a virgin."

        jobgirl "Ehi, don't you dare spread the word around! I'll kill you if you even think to try!!"

        you "Relax, girl, and don't worry. It is something personal, I know and respect it. No one will ever hear it from me, I swear."

        jobgirl "Okay... thanks, I guess... You know what? Now that you know it I'm feeling a bit relieved. I don't know why."

        you "I'm just glad we learned more about each other. I like to be in your company. You're cute and smart."

        play sound s_sigh

        jobgirl "Oooh, stop that!"

        you "What about your feelings? What do you think about me?"

        jobgirl "About you? Let's see... you're a pimp who fucks his girls all day long... but you help damsels in distress, don't screw girls you just met on the beach, and your massage skills are superb."

        you "(Screwing girls on the beach? Could that be... damn Anika, she planned to tell her everything since the beginning! I must be on the lookout when she's around!)"

        jobgirl "And you're... uhm... handsome too..."

        you "Really? So you do like me after all..."

        jobgirl "I like you more, but don't think we're gonna be a couple yet. I want to know you more for now. And yes, I admit I start to feel good in your company. You're not an asshole like the many other men I know."

        you "It's good news then! And the massage is over now, thank you for choosing [MC.name]'s masseur service. Please come back again!"

        hide beach_lay_down with dissolve

        show beach_stand_1

        play sound s_kind_laugh

        jobgirl "Ahahah!"

        jobgirl "You're very funny! I like that!"

        you "That means you like me!"

        jobgirl "Hey not again!"

        you "Just joking."

        jobgirl "It's been a beautiful day here with you and Anika, I really needed to relax! Will we meet again?"

        you "Anytime you want, just give me a call and I'll be there with you!"

        jobgirl "Make sure not to disappear, otherwise you will lose all the points you scored today!"

        you "Are you taking note of my score with you? Really?"

        jobgirl "Naaah that's a joke! Hihihi!"

        "You keep talking more while you gather your things and leave the beach together, until you go separate ways to go back home."

        jobgirl "Thank you again, for everything. This is a little gift for you. But first close your eyes."

        "You do what she asks. Then you feel her soft lips touching yours, and slowly, she gives you a shy kiss."

        "You feel a lovely sensation, this innocent kiss is quite rare for you. Women you kiss usually put more passion, or even sluttyness in their kisses; this one is something completely different. Like pure water dropping from a mountain spring."

        "When she moves away, you still keep your eyes closed for a moment, lost in that sweet sensation."

        jobgirl "I have to go now. See you soon!"

        "She turns away and leaves."

        hide beach_stand_1 with fade

        you "(See you soon, sweetie.)"

        $ NPC_jobgirl.love += 5

        $ NPC_jobgirl.corruption -= 5

    scene black with fade

    return
