###############################
### FREE GIRLS INTERACTIONS ###
###############################

label free_girl_interact(girl):


    $ renpy.block_rollback()
    $ loc_pic = selected_location.get_pic(config.screen_width, int(config.screen_height*0.8))

    if MC.interactions > 0:

        if MC.get_effect("special", "notebook"):
            $ choice_menu_girl_interact = True

        $ city_label = girl.init_dict["background story/city_label"]

        if city_label:
            if renpy.has_label(city_label): # Problem: Game will still crash if the label doesn't allow for the girl argument
                call expression city_label pass (girl=girl) from _call_expression_4
            else:
                "System" "Label: {color=[c_red]}[city_label]{/color} doesn't exist (Custom girl: {color=[c_red]}[girl.path]{/color})."

        else:
            call free_girl_talk(girl) from _call_free_girl_talk

    else:
        "You do not have any interactions left for today."
    $ choice_menu_girl_interact = False

    hide screen dark_filter
    hide screen show_event
    hide screen free_girl_interact
    show screen visit_location()
    with dissolve

    return

label free_girl_talk(girl):

    if not girl.MC_interact:

        hide screen visit_location
        show screen show_event(girl.profile, x=config.screen_width, y=int(config.screen_height*0.8), bg=loc_pic)
        with fade

        $ choice_menu_girl_interact = False

        ## Greetings

        $ MC.interactions -= 1

        $ text1 = rand_choice(("As you walk around the %s, ", "On your way to %s, ", "Strolling around the %s absentmindedly, ")) % selected_location.name

        $ text1 += rand_choice(("you notice a pretty girl standing by herself.", " you nearly bump into a cute young woman.", " you spot a pretty little thing haggling with a peddler.", " you see a beautiful girl, looking lost."))

        "[text1]"

        menu:

            extend ""

            "Greetings":

                $ renpy.block_rollback()

                you "Greetings, my lady. They call me [MC.name], your humble servant. Is there anything I can do to help?"

                call dialogue(girl, "free_greetings_polite") from _call_dialogue_21


            "Hi there":

                $ renpy.block_rollback()

                you "Oh, hi there! I'm [MC.name]. Who are you?"

                call dialogue(girl, "free_greetings_casual") from _call_dialogue_22


            "Hey, sexy":

                $ renpy.block_rollback()

                if dice(6) < 6:
                    you "Well, what do we have here... Damn, you're hot! I'm [MC.name]. What's your name baby?"

                else:
                    $ you(rand_choice(("Is your dad a baker? 'Cause you've got some nice buns!", "I'm not staring at your boobs. I'm staring at your heart.", "Did we take a class together? I could've sworn we had chemistry.")))

                call dialogue(girl, "free_greetings_rude") from _call_dialogue_23

        $ girl.meet_MC()

        return

    elif girl.get_love() >= 25 and girl.MC_relationship_level == 0:
        hide screen visit_location

        show screen show_event(girl.profile, x=config.screen_width, y=int(config.screen_height*0.8), bg=loc_pic)
        with fade

        call free_girl_friend(girl) from _call_free_girl_friend

    elif girl.get_love() >= 50 and girl.MC_relationship_level == 1:
        hide screen visit_location

        show screen show_event(girl.profile, x=config.screen_width, y=int(config.screen_height*0.8), bg=loc_pic)
        with fade

        call free_girl_love_interest(girl) from _call_free_girl_love_interest

    elif girl.get_love() >= 75 and girl.MC_relationship_level == 3:
        hide screen visit_location

        show screen show_event(girl.get_pic("date", "profile", naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=loc_pic)
        with fade

        call free_girl_girlfriend(girl) from _call_free_girl_girlfriend

    elif girl.get_love() >= 90 and girl.MC_relationship_level == 4:
        hide screen visit_location

        show screen show_event(girl.get_pic("date", "profile", naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=loc_pic)
        with fade

        call free_girl_job_request(girl) from _call_free_girl_job_request

    else:
        call free_girl_interact_menu() from _call_free_girl_interact_menu
        return

    hide screen dark_filter
    hide screen show_event
    with fade

# Main interaction menu

label free_girl_interact_menu():

    ## Cannot go above a certain love level if girl doesn't have the right relationship level

    $ limit = {0 : 25, 1 : 50, 2 : 50, 3 : 75, 4 : 100, 5 : 100}

    if girl.love > limit[girl.MC_relationship_level]:
        $ girl.love = limit[girl.MC_relationship_level]

    hide screen visit_location
    show screen free_girl_interact(girl)
    with dissolve

    $ topic = ui.interact()

    if topic == "back":
        pass

    elif isinstance(topic, GirlInteractionTopic):
        $ last_free_interact_menu = topic.type

        show screen dark_filter
        with Dissolve(0.1)

        call free_try_interact(girl, topic.group) from _call_free_try_interact

        if isinstance(topic, GirlInteractionTopic): # This is because in rare cases (cheats), the UI may fail during the first call
            $ renpy.call(topic.label, girl)

        hide screen dark_filter
        hide screen show_event

        $ renpy.block_rollback()

        if MC.interactions >= 1:
            jump free_girl_interact_menu

    else:
        jump free_girl_interact_menu

    with Dissolve(0.1)

    return

label free_chat_small_talk(girl):

    $ girl.personality_unlock["EI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves


    $ text1 = rand_choice(("The weather's nice today, don't you think?", "I've heard it might rain later today...", "Last time I came here it was a lot more crowded.", "How have you been? Haven't seen you in a while.", "I saw you standing there, so well, uh... Thought I'd just talk to you.", "Don't you think this place is strange?", "This dog looks strange, doesn't it?"))

    you "[text1]"

    call dialogue(girl, "free_small_talk") from _call_dialogue_24

    return

label free_chat_gossip(girl):

    $ girl.personality_unlock["EI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    call dialogue(girl, "free_gossip") from _call_dialogue_25

    if girl.personality.name not in ("nerd", "sweet"):
        $ girl.char(get_gossip())

    return

label free_chat_life(girl):

    $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    you "What do you think about life, the universe, and everything?"

    call dialogue(girl, "free_chat_life") from _call_dialogue_26

    return

label free_chat_love(girl):

    $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    you "Love. What do you think about it?"

    call dialogue(girl, "free_chat_love") from _call_dialogue_27

    return

label free_chat_origins(girl):

    you "Where are you from?"

    call dialogue(girl, "free_chat_origins") from _call_dialogue_28 #, custom_arg=girl.origin)

    $ girl.personality_unlock["origin"] = True

    return

label free_chat_hobbies(girl):

    you "What do you like to do with your free time?"

    $ hobby = rand_choice(girl.hobbies)

    call dialogue(girl, "free_chat_hobbies") from _call_dialogue_29 #, custom_arg=h)

    $ girl.personality_unlock["hobby_" + hobby] = True

    return

label free_chat_likes(girl):

    $ thing, best = girl.talk_tastes("likes")

    you "What are your favorite things?"

    call dialogue(girl, "free_chat_likes") from _call_dialogue_30 #! , custom_arg=h)

    $ girl.personality_unlock["fav_" + thing] = True
    return

label free_chat_dislikes(girl):

    $ thing, worst = girl.talk_tastes("dislikes")

    you "Is there anything you dislike?"

    call dialogue(girl, "free_chat_dislikes") from _call_dialogue_31 #, custom_arg=(thing, worst))

    $ girl.personality_unlock["dis_" + thing] = True
    return



label free_joke_harmless(girl):

    $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ joke = rand_choice(jokes["harmless"])

    you "[joke]"

    call dialogue(girl, "free_joke_harmless") from _call_dialogue_32

    return

label free_joke_adult(girl):

    $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ joke = rand_choice(jokes["sex"])

    you "[joke]"

    call dialogue(girl, "free_joke_adult") from _call_dialogue_33

    return

label free_joke_dark(girl):

    $ girl.personality_unlock["EI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ joke = rand_choice(jokes["dark"])

    you "[joke]"

    call dialogue(girl, "free_joke_dark") from _call_dialogue_34

    return

label free_joke_mean(girl):

    $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ joke = rand_choice(jokes["mean"])

    you "[joke]"

    call dialogue(girl, "free_joke_mean") from _call_dialogue_35

    return


label free_touch_hand(girl):

    $ girl.personality_unlock["EI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    "You lightly grab her hand, brushing your fingers against her skin."

    call dialogue(girl, "free_touch_hand") from _call_dialogue_36

    return

label free_touch_kiss(girl):

    $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    "Bringing your face closer, you lean in to kiss her."

    call dialogue(girl, "free_touch_kiss") from _call_dialogue_37

    return

label free_touch_ass(girl):

    $ girl.personality_unlock["DS"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    play sound s_surprise
    "*smack*" with vpunch

    call dialogue(girl, "free_touch_ass") from _call_dialogue_38

    return

label free_touch_breasts(girl):

    $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    "You brush your hands against her tits, lightly touching her nipples."

    call dialogue(girl, "free_touch_breasts") from _call_dialogue_39

    return

label free_touch_pussy(girl):

    $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    "Pressing her body close, you lower your hand between her thighs."

    call dialogue(girl, "free_touch_pussy") from _call_dialogue_40

    return


label free_play(girl):
    $ act = topic.act

    if act == "naked":

        $ girl.personality_unlock["EI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

        $ text1 =  "Why don't you strip down for me babe?"

        $ snd = s_equip_dress

        $ pic = girl.get_pic("strip", "naked", "profile", soft=True, hide_farm=True)

    elif act == "service":

        $ girl.personality_unlock["DS"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

        $ diff = 76

        $ snd = "sucking.wav"

        $ pic = girl.get_pic("service", "naked", "profile", not_tags = ["group", "bisexual"], hide_farm=True)

        if pic.has_tag("mast"):
            $ text1 = "I want you to masturbate for me."
        elif pic.has_tag("titjob"):
            $ text1 = "I want to fuck those nice tits of yours."
        elif pic.has_tag("footjob"):
            $ text1 = "Why don't you jerk me off with your feet?"
        elif pic.has_tag("oral"):
            $ text1 = "I want you to suck my dick."
        elif pic.has_tag("handjob"):
            $ text1 = "I want you to jerk me off."
        else:
            $ text1 = "I want you to pleasure me."

#         $ dislikes = ("rebel", "nerd")


    elif act == "sex":

        $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

        $ diff = 78

        $ text1 = "Let me have you..."

        $ snd = "orgasm.wav"

        $ pic = girl.get_pic("sex", "naked", "profile", not_tags = ["group", "bisexual"], hide_farm=True)

#         $ likes = ("nerd", "sweet")

#         $ dislikes = ("masochist", "cold")


    elif act == "anal":

        $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

        $ diff = 80

        $ text1 = "I want to fuck your ass."

        $ snd = "orgasm2.mp3"

        $ pic = girl.get_pic("anal", "sex", "naked", "profile", not_tags = ["group", "bisexual"], hide_farm=True)

#         $ likes = ("masochist", "rebel")

#         $ dislikes = ("sweet", "superficial")


    elif act == "fetish":

        $ girl.personality_unlock["DS"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

        $ diff = 82

        $ text1 = "Bend over and get ready for a good whack."

        $ snd = "screams.wav"

        $ pic = girl.get_pic("fetish", "service", "naked", "profile", not_tags = ["group", "bisexual"], hide_farm=True)

#         $ likes = ("masochist", "cold")

#         $ dislikes = ("sweet", "meek")

    "Taking her by the hand, you lead her around a corner."

    you "Come here... [text1]"

    $ pref = girl.get_preference(act, bonus=girl.get_love() + MC.get_charisma()*10)

    if pref == "refuses":

        call dialogue(girl, "free_play refuses") from _call_dialogue_41

#         girl.char "No way! Get lost!!!"
#         $ girl.change_love(-1)

        $ girl.raise_preference(act, bonus=0.25) #!

    else:
        call dialogue(girl, "free_play " + pref) from _call_dialogue_42

        $ girl.raise_preference(act, "love", 1)

        show screen show_sex_event(pic, bg=loc_pic)
        with fade

        play sound snd

        girl.char "Mmmh... Aaah..."

        if not act == "naked":

            you "Ooooh..."

            with flash

        if act == "sex":
            if girl.pop_virginity(origin="MC"):
                show screen show_sex_event(girl.get_pic("virgin", "sex", "naked"), bg=loc_pic)
                with dissolve
                call dialogue(girl, "MC take virginity") from _call_dialogue_43
                "You have taken [girl.name]'s virginity... You earn extra prestige."
                $ MC.prestige += 3 * girl.rank

        hide screen show_sex_event
        with fade

        $ MC.change_prestige(girl.rank)

        stop sound fadeout 3.0

        $ girl.test_weakness(act, unlock=True, feedback=True)

        if compare_preference(girl, act, "a little interested", bonus=girl.get_love() + MC.get_charisma()*10):
            call dialogue(girl, "free_play interested after") from _call_dialogue_44
#             girl.char "I liked that... *blush*"
        else:
            call dialogue(girl, "free_play not interested after") from _call_dialogue_45
#             girl.char "Well... Are you satisfied now?"

    return

label free_flirt_beauty(girl):

    $ girl.personality_unlock["EI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ compliment = rand_choice(compliments["beauty"]) % girl.name

    you "[compliment]"

    call dialogue(girl, "free_flirt_beauty") from _call_dialogue_46

    return

label free_flirt_body(girl):

    $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ compliment = rand_choice(compliments["body"])

    you "[compliment]"

    call dialogue(girl, "free_flirt_body") from _call_dialogue_47

    return

label free_flirt_mind(girl):

    $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ compliment = rand_choice(compliments["mind"])

    you "[compliment]"

    call dialogue(girl, "free_flirt_mind") from _call_dialogue_48

    return

label free_flirt_spirit(girl):

    $ girl.personality_unlock["DS"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ compliment = rand_choice(compliments["spirit"])

    you "[compliment]"

    call dialogue(girl, "free_flirt_spirit") from _call_dialogue_49

    return


label free_flirt_sex_experience(girl):
    $ MC.rand_say(("Are you 'experienced'?", "Tell me the truth: have you been with many men before?", "Are you used to fooling around with boys much?", "Did you know many men before me?", "ev: Have you been passed around the harbor like a bag of spice?", "ne: Be honest: Have you had a lot of sex before?", "gd: Are you skilled in the art of love?"))

    call dialogue(girl, "free_flirt_sex_experience " + girl.sexual_experience) from _call_dialogue_50


    if girl.has_trait("Virgin"):
        call dialogue(girl, "free_flirt_sex_experience virgin") from _call_dialogue_51

    $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    girl.char "What about you? Have you known many girls?"

    menu:
        "What do you tell her?"

        "I'm waiting for the right person":
            $ renpy.block_rollback()
            you "It might sound silly, but I am waiting for the right person..."

            # Will she believe you?

            $ res = MC.get_charisma() + dice(6)

            if MC.get_alignment() == "good":
                $ res += 1
            elif MC.get_alignment() == "evil":
                $ res -= 1

            if res >= 10:
                call dialogue(girl, "free_flirt_sex_experience reply_waiting success") from _call_dialogue_52

            else:
                call dialogue(girl, "free_flirt_sex_experience reply_waiting failure") from _call_dialogue_53



        "I haven't been with many girls":
            $ renpy.block_rollback()
            you "Uh, well, no, not many..."

            # Will she believe you?

            $ res = MC.get_charisma() + dice(6)

            if MC.get_alignment() == "good":
                $ res += 1
            elif MC.get_alignment() == "evil":
                $ res -= 1

            if res >= 7:
                call dialogue(girl, "free_flirt_sex_experience reply_not_many success") from _call_dialogue_54

            else:
                call dialogue(girl, "free_flirt_sex_experience reply_not_many failure") from _call_dialogue_55


        "I've been around":
            $ renpy.block_rollback()
            you "Well, I've been around... You know."

            call dialogue(girl, "free_flirt_sex_experience reply_been_around") from _call_dialogue_56

        "I'm a sex god":
            $ renpy.block_rollback()
            you "Babe, I'm the best lay in town, believe me."

            # Will she believe you?

            $ res = MC.get_charisma() + dice(6)

            if MC.get_alignment() == "evil":
                $ res += 1
            elif MC.get_alignment() == "good":
                $ res -= 1

            if res >= 8:
                call dialogue(girl, "free_flirt_sex_experience reply_sex_god success") from _call_dialogue_57

            else:
                call dialogue(girl, "free_flirt_sex_experience reply_sex_god failure") from _call_dialogue_58

        "I'm a brothel owner, so..." if not girl.MC_lied:
            $ renpy.block_rollback()
            you "Well, I'm a brothel owner, so what do you expect... It's my job!"

            call dialogue(girl, "free_flirt_sex_experience reply_brothel_owner") from _call_dialogue_59

    return

label free_flirt_sex_tastes(girl):

    $ MC.rand_say(("What do you like in bed?", "Is there anything you like in the bedroom?", "Tell me what turns you on.", "What is your favorite sexual position?"))

    if dice(6) >= 4: #Describe positive acts and fixations

        $ fix = rand_choice(girl.pos_fixations)
        $ act = rand_choice(fix.acts)

        if girl.personality_unlock[act] and dice(6) >= 4:

            $ renpy.say(girl.char, "You know what fascinates me about %s?" % long_act_description[act])

            $ text1 = fix_description[fix.name + " description"].lower()

            play sound s_mmmh
            "She tells you that she is interested in [text1]"

            if not girl.personality_unlock[fix.name]:

                "You have discovered [girl.name]'s fixation with [fix.name]."

                $ girl.personality_unlock[fix.name] = True

        else:

            "She blushes as she whispers something to you."

            $ text1 = "Well, I've heard a lot about %s..." % long_act_description[act]

            $ girl.personality_unlock[act] = True
            $ girl.personality_unlock["LM"] += MC.get_charisma() + 15 + dice(10)
            $ girl.raise_preference(act, "love", 0.5)

            if girl.is_("modest"):
                girl.char "[text1] Do you think it's wrong?"
            else:
                girl.char "[text1] I think I'd like to try new things."

    else:

        $ fix = rand_choice(girl.neg_fixations)

        if fix:

            $ act = rand_choice(fix.acts)

            if girl.personality_unlock[act] and dice(6) >= 4:
                play sound s_sigh
                $ renpy.say(girl.char, "You know the one thing I really hate about %s?" % long_act_description[act])
                "She tells you that [fix.name] disturbs her. It creeps her out."

                if not girl.personality_unlock[fix.name]:

                    "You have discovered [girl.name]'s disgust for [fix.name]."

                    $ girl.personality_unlock[fix.name] = True

            else:
                $ text1 = "%s makes me uncomfortable..." % long_act_description[act]

                "She blushes as she whispers something to you."

                $ girl.personality_unlock[act] = True
                $ girl.personality_unlock["LM"] += MC.get_charisma() + 15 + dice(10)

                if girl.is_("modest"):
                    girl.char "[text1] I think it's dirty."
                else:
                    girl.char "[text1] There's something about it that bothers me."

        else:
            girl.char "I guess I'm comfortable with pretty much anything now."

    $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    if girl.is_("very lewd"):
        $ girl.change_love(3)
    elif girl.is_("lewd"):
        $ girl.change_love(2)
    elif not girl.is_("very modest"):
        $ girl.change_love(1)
    return

label free_flirt_sex_act(girl):
    $ act = topic.act

    if act == "naked":
        $ girl.personality_unlock["EI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
        $ MC.rand_say(("Tell me something: do you sleep naked at night?", "Do you like to expose yourself in front of people?", "How do you feel when other people look at you in your natural state?",
                        "ev: Do you like to expose your bare pussy like a horny bitch?", "ne: Do you like to show your body to strangers?", "gd: You have such a perfect body. Do you enjoy people looking at it?",
                        "ar: Do you agree that since Arios shines His light on everything, hiding your body under clothes is unnecessary?", "wr: Zonian she-warriors fight with nothing but a sword and a cat-tail stuck into their asshole. Would that turn you on?"))

    elif act == "service":
        $ girl.personality_unlock["DS"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
        $ MC.rand_say(("Do you masturbate a lot?", "Do you like oral?", "How do you like to go down on guys?", "ar: What do you know about Arios candle worship?", "ev: How would you like to choke on my dick?",
            "ne: I'm sure you can use those assets of yours to pleasure a man...", "gd: With a lovely mouth like yours, you must give the best blowjobs...", "tr: In all my travels, I have found that a skilled tongue is the best way to get what you want... It's even more true for pretty babes like you. Do you agree? *wink*"))

    elif act == "sex":
        $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
        $ MC.rand_say(("Are you a virgin?", "Ever done it with a man?", "ev: Do you like riding dicks? Come on, a bitch like you should love it.", "ne: Do you like sex, babe?", "gd: How do you like to make sweet love, darling?", "ng: Ever been to heaven with a man?", "wz: Many girls told me I can perform miracles with my magic wand. Would you like me to show you?"))

    elif act == "anal":
        $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
        $ MC.rand_say(("Ever used the back door?", "Do you like it from behind? You know...", "ev: You look like a butt slut. Are you?", "gd: Ever used your other love hole?", "ne: How do you like it up the ass?",
            "sh: Have you ever done it Shalia's way?", "wr: In war, it's always best to charge from behind. In love, it's the same, wouldn't you say?"))

    elif act == "fetish":
        $ girl.personality_unlock["DS"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
        $ MC.rand_say(("Do you like kinky sex?", "Do you like to do really naughty things in bed?", "Do you like pleasure mixed with pain?", "Do you own many sex toys?",
                       "ev: Would you like me to hurt you? Say it.", "ne: How far would you go with me? I know a trick or two...", "gd: Do you trust me? I could show you some fun and dirty tricks...",
                       "wz: Some girls like to use magic to spice up their sexual encounters. Should we try it together?"))

    elif act == "bisexual":
        $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
        $ MC.rand_say(("Ever done it with another girl?", "Do you like to be with another woman?", "Ever heard of sapphism? Did you give it a try?", "tr: In Borgo, fisherwomen like to polish each other's pearls. Do you?",
                        "Are you bisexual?", "Do you like girls?", "ev: It takes a bitch to know one. Ever tried fucking a girl?", "ne: Man, woman, does it matter to you?", "gd: You're lovely and caring, I'm sure women like you too. Don't they?", "sh: Worshipping a goddess is always more satisfactory than a god, wouldn't you say?",
                        ))

    elif act == "group":
        $ girl.personality_unlock["EI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
        $ MC.rand_say(("Ever been in an orgy?", "Do you like a threesome?", "gd: The more the merrier, wouldn't you say?", "ev: How many dicks can you take at the same time?",
                        "Do you like group sex?", "ne: How about fucking several people at once? Does that turn you on?", "ng: Wasting valuable time praying to fickle gods is stupid, when you could be having a decadent earthly orgy instead. Don't you agree?",
                        "wr: The best training a warrior can get is fighting many enemies at once. And since love is like a battlefield..."))

#     $ pref = girl.get_preference(act)

    call dialogue(girl, "free_flirt_sex_act " + girl.get_preference(act)) from _call_dialogue_60

    return

label free_give_gift(girl): # Interactions are deducted here for giving gold
    python:

        available_gifts = []

        for it in MC.items:

            if it.usage == "give":

                available_gifts.append(it)

    python:

        gift_list = []

        for it in available_gifts:

            gift_list.append((it.name, it))

        gift_list.append(("Go back", "back"))

        result = long_menu("Choose a present", gift_list)

    if result == "back":
        return

    $ MC.interactions -= 1
    $ girl.talked_to_date = calendar.time
    $ girl.MC_interact_counters["gift"] += 1
    $ renpy.block_rollback()
    $ MC.gift(girl, result)
    return

label free_give_gold(girl): # Interactions are deducted here for giving presents

    if district.rank == 1:
        $ tip_range = (10, 50, 100, 200)

    elif district.rank == 2:
        $ tip_range = (50, 250, 500, 1000)

    elif district.rank == 3:
        $ tip_range = (250, 1000, 2500, 5000)

    else:
        $ tip_range = (500, 2500, 5000, 10000)

    $ modifier = 0

    if girl.is_("materialist"):

        $ modifier = 10

    elif girl.is_("very idealist"):

        $ modifier = -10

    menu:

        you "I want you to have this."

        "[tip_range[0]] gold" if MC.gold >= tip_range[0]:

            $ tip = tip_range[0]

            $ diff = 75

        "[tip_range[1]] gold" if MC.gold >= tip_range[1]:

            $ tip = tip_range[1]

            $ diff = 50

        "[tip_range[2]] gold" if MC.gold >= tip_range[2]:

            $ tip = tip_range[2]

            $ diff = 25

        "[tip_range[3]] gold" if MC.gold >= tip_range[3]:

            $ tip = tip_range[3]

            $ diff = 0

        "Go back":
            $ choice_menu_girl_interact = False
            hide screen dark_filter
            return

    $ MC.gold -= tip

    $ MC.interactions -= 1
    $ girl.talked_to_date = calendar.time
    $ girl.MC_interact_counters["gold"] += 1

    $ renpy.block_rollback()

    $ result = dice(100) + modifier - diff

    $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    play sound s_gold

    if result >= 50:
        call dialogue(girl, "free_give_gold +++") from _call_dialogue_61


    elif result >= 25:
        call dialogue(girl, "free_give_gold ++") from _call_dialogue_62

    elif result >= 0:
        call dialogue(girl, "free_give_gold +") from _call_dialogue_63

    elif result >= -25:
        call dialogue(girl, "free_give_gold -") from _call_dialogue_64

    else:
        call dialogue(girl, "free_give_gold --") from _call_dialogue_65

    return

label free_offer_job(girl):

    you "[girl.name], I think I have found a solution to your problem."

    girl.char "What? You have?"

    you "Come and work for me."

    if not girl.MC_lied:

        girl.char "With you? At the brothel?"

        call dialogue(girl, "free_offer_job no_lie") from _call_dialogue_66

    else:

        if girl.MC_lied == "half":

            girl.char "Work for you? I thought you were a freelance [MC.playerclass]?"

            you "Well, this isn't the whole truth... You see, I also have a business on the side."

            girl.char "What... What do you mean?"

            you "Well I, uh, own a cathouse..."

            girl.char "A brothel? You're a brothel owner?"

            call dialogue(girl, "free_offer_job half_lie") from _call_dialogue_67

        else:

            girl.char "Work for you? Oh yes, I forgot, you're [girl.MC_lied]!"

            you "I..."

            girl.char "This is great! We can be together, and I will be safe, get money..."

            you "I'm afraid that it isn't so simple..."

            girl.char "I don't like that look... What do you mean?"

            you "I'm afraid I didn't tell you the truth. I'm not [girl.MC_lied], I'm a pimp. I own a brothel in town."

            call dialogue(girl, "free_offer_job lie") from _call_dialogue_68

    you "Of course. The sex trade is hard work, but it has its perks, you know... Flexible schedule, good money, round-the-clock protection..."

    you "You could also just be a waitress, or a dancer... It's not so bad."

    girl.char "Oh..."

    you "There's one more thing."

    girl.char "What?"

    if MC.get_alignment() == "good":

        $ text1 = "I will treat you well of course, taking good care of you."
        $ modifier = 2

    elif MC.get_alignment() == "neutral":

        $ text1 = "I will treat you fairly, and you have nothing to fear if you play by the rules."
        $ modifier = 0

    elif MC.get_alignment() == "evil":

        $ text1 = "I must also warn you that I'm a harsh master. You have to be ready for anything."
        $ modifier = -4

    you "You would have to sign a temporary slave contract. As you know, only sex slaves are allowed in the city's brothels. [text1]"

    you "So, what do you think?"

    girl.char "..."

    $ result = girl.get_love() + MC.get_charisma() + dice(6) + modifier

    $ renpy.block_rollback()

    if result > 95:

        call dialogue(girl, "free_offer_job success") from _call_dialogue_69

        you "It is decided then. Take your things and come with me. I will have you magically branded..."

        "[girl.fullname] has become one of your girls."

        $ girl.love /= 2

        $ acquire_girl(girl, free = True)
        $ selected_location.girls.remove(girl)

    elif result > 90:
        call dialogue(girl, "free_offer_job thinking") from _call_dialogue_70

    elif girl.MC_lied:
        call dialogue(girl, "free_offer_job failure lie") from _call_dialogue_71

    else:
        call dialogue(girl, "free_offer_job failure no_lie") from _call_dialogue_72

    $ girl.MC_lied = False

    $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
    return



label free_girl_friend(girl):

    $ girl.fear -= 5

    girl.char "We've known each other for a little while now. Let's be friends!"

    you "Okay, sure!"

    girl.char "But there's one thing I'd like to know... You never told me about your job. What do you do?"

    menu:

        "What do you tell her?"

        "Tell the truth":

            $ renpy.block_rollback()

            $ girl.MC_lied = False

            you "I own a brothel in town. I'm a pimp."

            call dialogue(girl, "free_friend no_lie") from _call_dialogue_73

        "Tell a half lie":

            $ renpy.block_rollback()

            $ girl.MC_lied = "half"

            you "Well, er, I'm a [MC.playerclass] freshly arrived in Zan. I'm considering a career change though..."

            call dialogue(girl, "free_friend half_lie") from _call_dialogue_74


        "Outright lying":

            $ renpy.block_rollback()

            $ lie = rand_choice(("a secret guild master", "an expert weaponsmith", "a professional circus athlete", "an Arios knight", "a famous Noh actor", "an international man of mystery"))

            $ girl.MC_lied = lie

            you "Me? Uh, I'm..."

            you "I'm {b}[lie]{/b}!"

            call dialogue(girl, "free_friend lie") from _call_dialogue_75


    $ girl.MC_relationship_level = 1
    $ girl.track_event("MC friend", arg=girl.name)

    with fade

    "You and [girl.fullname] are now friends."

    return


label free_girl_love_interest(girl):

    $ girl.fear -= 5

    girl.char "Oh, it's you..."

    $ season = calendar.get_season()

    call dialogue(girl, "free_love_interest") from _call_dialogue_76

    "She looks at you with some intensity, then turns her head away."

    girl.char "Anyway. Let's get out of here."

    with fade

    "You may now bring [girl.fullname] {b}flowers{/b} to express your interest."

    $ girl.MC_relationship_level = 2
    $ girl.track_event("MC flower", arg=girl.name)

    return


label free_girl_girlfriend(girl):

    call dialogue(girl, "free_girlfriend intro") from _call_dialogue_77

    $ passed = False

    $ d = dice(6)

    if d >= 5:

        girl.char "Do you remember my hobby?"

        python:

            hobby_list = []

            hobby_list.append(rand_choice(girl.hobbies))

            for i in range(4):

                h = rand_choice(hobbies)

                while h in hobby_list:

                    h = rand_choice(hobbies)

                hobby_list.append(h)

            renpy.random.shuffle(hobby_list)

            m = []

            m.append(("[girl.name]'s hobby is...", None))

            for h in hobby_list:

                m.append((h, h))

            m.append(("I don't know", "give up"))

            r = menu(items = m)

        $ renpy.block_rollback()

        if r in girl.hobbies:

            call dialogue(girl, "free_girlfriend right") from _call_dialogue_78

            $ passed = True

        elif r == "give up":

            you "I just don't know. Sorry."

            call dialogue(girl, "free_girlfriend give_up") from _call_dialogue_79

        else:
            call dialogue(girl, "free_girlfriend wrong") from _call_dialogue_80

    elif d >= 4:

        girl.char "Do you remember where I come from?"

        python:

            origin_list = []

            origin_list.append(girl.origin)

            for i in range(3):

                h = rand_choice(origins)

                while h in origin_list:

                    h = rand_choice(origins)

                origin_list.append(h)

            renpy.random.shuffle(origin_list)

            m = []

            m.append(("[girl.name] comes from...", None))

            for h in origin_list:

                m.append((h, h))

            m.append(("I don't know", "give up"))

            r = menu(items = m)

        $ renpy.block_rollback()

        if r == girl.origin:
            call dialogue(girl, "free_girlfriend right") from _call_dialogue_81

            $ passed = True

        elif r == "give up":

            you "I just don't know. Sorry."

            call dialogue(girl, "free_girlfriend give_up") from _call_dialogue_82

        else:
            call dialogue(girl, "free_girlfriend wrong") from _call_dialogue_83

    else:

        $ thing = rand_choice(("color", "food", "drink"))

        if dice(6) >= 4:

            $ type = "favorite"

        else:

            $ type = "least favorite"

        girl.char "Do you remember what is my [type] [thing]?"

        python:

            fav_list = []

            if type == "favorite":

                fav_list.append(girl.likes[thing])

            else:

                fav_list.append(girl.dislikes[thing])

            if thing == "color":

                base = colors

            elif thing == "food":

                base = food

            elif thing == "drink":

                base = drinks

            for i in range(3):

                h = rand_choice(base)

                while h in fav_list:

                    h = rand_choice(base)

                fav_list.append(h)

            renpy.random.shuffle(fav_list)

            m = []

            m.append(("[girl.name]'s [type] [thing] is...", None))

            for h in fav_list:

                m.append((h, h))

            m.append(("I don't know", "give up"))

            r = menu(items = m)

        $ renpy.block_rollback()

        if (type == "favorite" and r == girl.likes[thing]) or (type == "least favorite" and r == girl.dislikes[thing]):

            call dialogue(girl, "free_girlfriend right") from _call_dialogue_84

            $ passed = True

        elif r == "give up":

            you "I just don't know. Sorry."

            call dialogue(girl, "free_girlfriend give_up") from _call_dialogue_85

        else:

            call dialogue(girl, "free_girlfriend wrong") from _call_dialogue_86


    if passed:

        "She leans closer to you."

        girl.char "Don't you think... We need to know each other better?"

        $ pic = girl.get_pic("strip", "naked", and_tags=["libido"], soft=True)

        show screen show_sex_event(pic, bg=loc_pic)

        with fade

        $ girl.raise_preference("naked", "love", 1)

        if girl.get_effect("special", "naked"):

            call dialogue(girl, "free_girlfriend success naked") from _call_dialogue_87
            play sound s_laugh

        else:
            call dialogue(girl, "free_girlfriend success") from _call_dialogue_88
            play sound s_mmmh

        hide screen show_sex_event

        with fade

        "You may now have extra 'fun' with [girl.fullname]."

        $ girl.MC_relationship_level = 4
        $ girl.track_event("MC lover", arg=girl.name)

    else:

        you "Anyway... What was it you wanted to show me?"

        girl.char "Never mind... It doesn't matter."

    return


label free_girl_job_request(girl):

    "[girl.name] rushes to you, looking worried."

    call dialogue(girl, "free_job_request") from _call_dialogue_89

    if girl.personality.name == "pervert": # Pervert girls like group better to fit their dialogue
        $ girl.change_preference("group", 250)

    $ girl.MC_relationship_level = 5
    $ girl.track_event("MC job", girl.name)

    "You can now offer [girl.fullname] a job."

    return

label free_try_interact(girl, group):

    if not can_interact(girl, group, slave=False):

        if group == "gold":
            "You can only give a girl money once per day."

        elif group == "present":
            "You can only give a girl one present per day."

        elif group == "offer":
            if len(MC.girls) >= brothel.bedrooms:
                "You cannot offer her work as long as your brothel is full."

            elif girl.MC_interact_counters[group] >= 1:
                "You cannot offer her work again today."

        else:
            "You cannot do the same action with a girl more than 3 times a day."

        $ choice_menu_girl_interact = False

        hide screen dark_filter

        jump free_girl_interact_menu

    $ renpy.block_rollback()

    if group not in ("gold", "gift"): # Counters for giving gold and presents are handled in their own label
        $ girl.MC_interact_counters[group] += 1
        $ girl.talked_to_date = calendar.time
        $ MC.interactions -= 1

    return


#### END OF FREE GIRL INTERACTIONS FILE ####
