###############################
### FREE GIRLS INTERACTIONS ###
###############################

label free_girl_interact(girl):


    $ norollback()
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

    if girl.location.lower() in beach_locations:
        $ use_locations = ["beach"]
    else:
        $ use_locations = []

    if not girl.MC_interact:

        hide screen visit_location
        show screen show_event(girl.profile, x=config.screen_width, y=int(config.screen_height*0.8), bg=loc_pic)
        with fade

        $ choice_menu_girl_interact = False

        ## Greetings

        $ MC.interactions -= 1

        $ text1 = rand_choice(("当你漫步在%s时，", "在你前往%s的途中, ", "当你心不在焉地在%s闲逛时，")) % __(uncapitalize(selected_location.name))

        $ text1 += rand_choice(("你发现一个孤身一人的漂亮的女孩。", "你差点撞到一个可爱的少女。", "你看到一个美丽的女孩在和一个小贩讨价还价。", "你看到一个美丽的女孩，看起来很迷茫。"))

        "[text1]"

        menu:

            extend ""

            "Greetings":

                $ norollback()

                you "Greetings, my lady. They call me [MC.name], your humble servant. Is there anything I can do to help?"

                call dialogue(girl, "free_greetings_polite") from _call_dialogue_21


            "Hi there":

                $ norollback()

                you "Oh, hi there! I'm [MC.name]. Who are you?"

                call dialogue(girl, "free_greetings_casual") from _call_dialogue_22


            "Hey, sexy":

                $ norollback()

                if dice(6) < 6:
                    you "Well, what do we have here... Damn, you're hot! I'm [MC.name]. What's your name baby?"

                else:
                    $ you(rand_choice(("你爸爸是面包师吗？因为你的小圆面包很诱人！", "我并不是盯着你的胸看。我盯着的是你的心灵。", "我们一起上过课吗？我发誓我们很来电。")))

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

        show screen show_event(girl.get_pic("date", "profile", and_tags=use_locations, naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=loc_pic)
        with fade

        call free_girl_girlfriend(girl) from _call_free_girl_girlfriend

    elif girl.get_love() >= 90 and girl.MC_relationship_level == 4:
        hide screen visit_location

        show screen show_event(girl.get_pic("date", "profile", and_tags=use_locations, naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=loc_pic)
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

        $ norollback()

        if MC.interactions >= 1:
            jump free_girl_interact_menu

    else:
        jump free_girl_interact_menu

    with Dissolve(0.1)

    return

label free_chat_small_talk(girl):

    $ girl.personality_unlock["EI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves


    $ text1 = rand_choice(("今天天气真不错，你觉得呢？", "我听别人说今天会下雨...", "上次我来这，可是人满为患呐。", "你最近在忙什么那，有阵子没见到你了。", "我看到你站在那，所以，呃... 我就来找你搭话了。", "你不觉得这地方怪怪的吗？", "这只狗看起来有点奇怪，你不觉得吗？"))

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

    $ thing_cn = tl_cn(thing, girl_related_dict)

    call dialogue(girl, "free_chat_likes") from _call_dialogue_30 #! , custom_arg=h)

    $ girl.personality_unlock["fav_" + thing] = True

    return

label free_chat_dislikes(girl):

    $ thing, worst = girl.talk_tastes("dislikes")

    you "Is there anything you dislike?"

    $ thing_cn = tl_cn(thing, girl_related_dict)

    call dialogue(girl, "free_chat_dislikes") from _call_dialogue_31 #, custom_arg=(thing, worst))

    $ girl.personality_unlock["dis_" + thing] = True

    return

label free_joke_harmless(girl):

    $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ joke = __(rand_choice(jokes["harmless"]))

    you "[joke]"

    call dialogue(girl, "free_joke_harmless") from _call_dialogue_32

    return

label free_joke_adult(girl):

    $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ joke = __(rand_choice(jokes["sex"]))

    you "[joke]"

    call dialogue(girl, "free_joke_adult") from _call_dialogue_33

    return

label free_joke_dark(girl):

    $ girl.personality_unlock["EI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ joke = __(rand_choice(jokes["dark"]))

    you "[joke]"

    call dialogue(girl, "free_joke_dark") from _call_dialogue_34

    return

label free_joke_mean(girl):

    $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ joke = __(rand_choice(jokes["mean"]))

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

        $ text1 =  "为什么你不把这些碍事的衣服都脱掉呢？"

        $ snd = s_equip_dress

        $ pic = girl.get_pic("strip", "naked", "profile", and_tags=use_locations, not_tags=all_jobs, soft=True, hide_farm=True)

    elif act == "service":

        $ girl.personality_unlock["DS"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

        $ diff = 76

        $ snd = s_sucking

        $ pic = girl.get_pic("service", "naked", "profile", and_tags=use_locations, not_tags= ["group", "bisexual"] + all_jobs, hide_farm=True)

        if pic.has_tag("mast"):
            $ text1 = "在这里自慰。"
        elif pic.has_tag("titjob"):
            $ text1 = "用你的奶子帮我撸。"
        elif pic.has_tag("footjob"):
            $ text1 = "为什么不用你的玉足帮我撸呢？"
        elif pic.has_tag("oral"):
            $ text1 = "过来嗦我的鸡巴。"
        elif pic.has_tag("handjob"):
            $ text1 = "用你的手帮我打飞机。"
        else:
            $ text1 = "尽力取悦我。"

#         $ dislikes = ("rebel", "nerd")


    elif act == "sex":

        $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

        $ diff = 78

        $ text1 = "让我好好品尝品尝你的小穴..."

        $ snd = s_orgasm

        $ pic = girl.get_pic("sex", "naked", "profile", and_tags=use_locations, not_tags= ["group", "bisexual"] + all_jobs, hide_farm=True)

#         $ likes = ("nerd", "sweet")

#         $ dislikes = ("masochist", "cold")


    elif act == "anal":

        $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

        $ diff = 80

        $ text1 = "我要用你的菊穴爽一爽。"

        $ snd = s_orgasm_fast

        $ pic = girl.get_pic("anal", "sex", "naked", "profile", and_tags=use_locations, not_tags= ["group", "bisexual"] + all_jobs, hide_farm=True)

#         $ likes = ("masochist", "rebel")

#         $ dislikes = ("sweet", "superficial")


    elif act == "fetish":

        $ girl.personality_unlock["DS"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

        $ diff = 82

        $ text1 = "把屁股撅起来，准备好接受调教。"

        $ snd = s_screams

        $ pic = girl.get_pic("fetish", "service", "naked", "profile", and_tags=use_locations, not_tags= ["group", "bisexual"] + all_jobs, hide_farm=True)

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

    $ compliment = __(rand_choice(compliments["beauty"])) % girl.name

    you "[compliment]"

    call dialogue(girl, "free_flirt_beauty") from _call_dialogue_46

    return

label free_flirt_body(girl):

    $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ compliment = __(rand_choice(compliments["body"]))

    you "[compliment]"

    call dialogue(girl, "free_flirt_body") from _call_dialogue_47

    return

label free_flirt_mind(girl):

    $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ compliment = __(rand_choice(compliments["mind"]))

    you "[compliment]"

    call dialogue(girl, "free_flirt_mind") from _call_dialogue_48

    return

label free_flirt_spirit(girl):

    $ girl.personality_unlock["DS"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    $ compliment = __(rand_choice(compliments["spirit"]))

    you "[compliment]"

    call dialogue(girl, "free_flirt_spirit") from _call_dialogue_49

    return


label free_flirt_sex_experience(girl):
    $ MC.rand_say(("你很有经验吗?", "告诉我实话：你以前和很多男人交往过吗？", "你经常和男孩子们鬼混吗？", "在我之前你认识很多男人吗？", "ev: 你是不是像一袋毒品一样在一群人中左手倒右手？", "ne: 说实话：你以前有过很多性生活吗？", "gd: 你精通做爱的艺术吗？"))

    call dialogue(girl, "free_flirt_sex_experience " + girl.sexual_experience) from _call_dialogue_50


    if girl.has_trait("Virgin"):
        call dialogue(girl, "free_flirt_sex_experience virgin") from _call_dialogue_51

    $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves

    girl.char "What about you? Have you known many girls?"

    menu:
        "What do you tell her?"

        "I'm waiting for the right person":
            $ norollback()
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
            $ norollback()
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
            $ norollback()
            you "Well, I've been around... You know."

            call dialogue(girl, "free_flirt_sex_experience reply_been_around") from _call_dialogue_56

        "I'm a sex god":
            $ norollback()
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
            $ norollback()
            you "Well, I'm a brothel owner, so what do you expect... It's my job!"

            call dialogue(girl, "free_flirt_sex_experience reply_brothel_owner") from _call_dialogue_59

    return

label free_flirt_sex_tastes(girl):

    $ MC.rand_say(("你喜欢在床上用什么姿势？", "有什么你喜欢的玩法吗？", "告诉我什么最让你兴奋。", "你最喜欢什么体位？"))

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

            $ text1 = __("Well, I've heard a lot about %s...") % __(long_act_description[act])

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
                $ renpy.say(girl.char, __("You know the one thing I really hate about %s?") % __(long_act_description[act]))
                "She tells you that [fix.name] disturbs her. It creeps her out."

                if not girl.personality_unlock[fix.name]:

                    "You have discovered [girl.name]'s disgust for [fix.name]."

                    $ girl.personality_unlock[fix.name] = True

            else:
                $ text1 = "%s让我感觉很不舒服..." % __(long_act_description[act])

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
        $ MC.rand_say(("告诉我，你晚上会光着身子睡觉吗？", "你喜欢在众人面前暴露自己吗？", "当别人看着你的自然状态时，你有什么感觉？",
                        "ev: 你喜欢暴露你赤裸的阴部像一个饥渴的婊子吗？", "ne: 你喜欢向陌生人展示你的身体吗？", "gd: 你有如此完美的身材。你喜欢别人看吗？",
                        "ar: 你是否同意既然阿里奥斯把他的光芒照在所有的东西上，把你的身体藏在衣服里就没有必要了？", "wr: 佐尼亚女战士战斗时除了一把剑和插在屁眼里的猫尾巴什么都没有。那会让你兴奋吗？"))

    elif act == "service":
        $ girl.personality_unlock["DS"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
        $ MC.rand_say(("你经常手淫吗？", "你喜欢口腔吗？", "你喜欢给男人口交吗？", "ar: 你对阿里奥斯的蜡烛崇拜了解多少？", "ev: 你想不想被我的老二噎死？",
            "ne: 我相信你可以用你的资产取悦一个男人...", "gd: 有你这么漂亮的嘴巴，你一定能给我最好的口交...", "tr: 在我所有的旅行中，我发现熟练的语言是得到你想要的东西的最好方法... 对于像你这样漂亮的宝贝来说更是如此。你同意吗？*眨眼*"))

    elif act == "sex":
        $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
        $ MC.rand_say(("你是处女吗？", "你和男人做过吗？", "ev: 你喜欢骑鸡巴吗？拜托，像你这样的婊子应该喜欢的。", "ne: 你喜欢性爱吗，宝贝？", "gd: 你喜欢怎样做爱，亲爱的？", "ng: 你曾经和一个男人一起去过天堂吗？", "wz: 许多女孩告诉我，我可以用我的魔杖创造奇迹。要我指给你看吗？"))

    elif act == "anal":
        $ girl.personality_unlock["LM"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
        $ MC.rand_say(("从后门走过吗？", "你喜欢从后面看吗？你知道...", "ev: 你看起来像个荡妇。是吗?", "gd: 曾经用过你的另一个爱洞吗？", "ne: 你喜欢屁股上的东西吗？",
            "sh: 你用过莎莉娅的方法吗？", "wr: 在战争中，最好从后面冲锋。爱情也是一样，你说呢？"))

    elif act == "fetish":
        $ girl.personality_unlock["DS"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
        $ MC.rand_say(("你喜欢刺激的性爱吗？", "你喜欢在床上做一些非常有趣的事情吗？", "你喜欢痛并快乐着吗？", "你喜欢用性玩具吗？",
                       "ev: 你想让我伤害你吗？说出来。", "ne: 你愿意和我试试吗？我新开发了一两招...", "gd: 你相信我吗？我可以给你表演一些有趣又下流的把戏...",
                       "wz: 有些女孩喜欢用魔法来增加性爱的情趣。我们一起试试好吗？"))

    elif act == "bisexual":
        $ girl.personality_unlock["MI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
        $ MC.rand_say(("你和别的女孩做过吗？", "你喜欢和别的女人在一起吗？", "你听说过蕾丝边吗？", "tr: 在博格，女人们喜欢磨豆腐。你呢?",
                        "你是女同吗？", "你对女孩有感觉吗？", "ev: 只有贱人才会知道。你试过操一个女孩吗？", "ne: 男人，女人，又有什么区别呢？", "gd: 你可爱又体贴，我相信女人也会爱上你。不是吗?", "sh: 侍奉女神总是比侍奉男神更令人愉悦，你说呢？",
                        ))

    elif act == "group":
        $ girl.personality_unlock["EI"] += 10 + MC.get_charisma() + dice(6) # Temp, see how it behaves
        $ MC.rand_say(("参加过派对吗？", "你喜欢三人行吗？", "gd: 独乐乐不如众乐乐，你说呢？", "ev: 你能同时吞下几根鸡巴？",
                        "你喜欢淫趴吗？", "ne: 同时被几个人上会让你兴奋吗？", "ng: 浪费宝贵的时间向善变的神祈祷是愚蠢的，人生苦短，及时行乐，享受堕落的尘世狂欢。你不这么认为吗？",
                        "wr: 情场如战场，同时应对多个敌人才能最好地磨练自己..."))

#     $ pref = girl.get_preference(act)

    call dialogue(girl, "free_flirt_sex_act " + girl.get_preference(act)) from _call_dialogue_60

    return

label free_give_gift(girl): # Interactions are deducted here for giving gold
    python:

        available_gifts = []

        for it in MC.items:

            if it.usage == "gift":

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
    $ norollback()
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

    $ norollback()

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

        $ text1 = "我当然会好好对待你，好好照顾你。"
        $ modifier = 2

    elif MC.get_alignment() == "neutral":

        $ text1 = "我会公平地对待你，如果你听我的话，那就没什么好担心的。"
        $ modifier = 0

    elif MC.get_alignment() == "evil":

        $ text1 = "事先声明，我是个严厉的主人。你得做好心理准备。"
        $ modifier = -4

    you "You would have to sign a temporary slave contract. As you know, only sex slaves are allowed in the city's brothels. [text1]"

    you "So, what do you think?"

    girl.char "..."

    $ result = girl.get_love() + MC.get_charisma() + dice(6) + modifier

    $ norollback()

    if result > 95:

        call dialogue(girl, "free_offer_job success") from _call_dialogue_69

        you "It is decided then. Take your things and come with me. I will have you magically branded..."

        "[girl.fullname] has become one of your girls."

        $ girl.love /= 2

        call acquire_girl(girl, context="free") from _call_acquire_girl_2 # Note: Checking for available space in the brothel is done before in the interaction menu

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

    if girl.love < 25:
        $ girl.love = 25

    $ girl.fear -= 5

    girl.char "We've known each other for a little while now. Let's be friends!"

    you "Okay, sure!"

    girl.char "But there's one thing I'd like to know... You never told me about your job. What do you do?"

    menu:

        "What do you tell her?"

        "Tell the truth":

            $ norollback()

            $ girl.MC_lied = False

            you "I own a brothel in town. I'm a pimp."

            call dialogue(girl, "free_friend no_lie") from _call_dialogue_73

        "Tell a half lie":

            $ norollback()

            $ girl.MC_lied = "half"

            you "Well, er, I'm a [MC.playerclass] freshly arrived in Zan. I'm considering a career change though..."

            call dialogue(girl, "free_friend half_lie") from _call_dialogue_74


        "Outright lying":

            $ norollback()

            $ lie = rand_choice(("一个神秘的公会会长", "一位武器专家", "一个职业马戏团演员", "一位太阳神教的圣骑士", "一位著名的话剧演员", "一个神秘的外国人"))

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

    if girl.love < 50:
        $ girl.love = 50

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

    if girl.love < 75:
        $ girl.love = 75

    call dialogue(girl, "free_girlfriend intro") from _call_dialogue_77

    $ passed = False

    $ d = dice(6)

    if d >= 5:

        girl.char "Can you name one of my hobbies?"

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

        $ norollback()

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

        $ norollback()

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
            $ _type = "favorite"
        else:
            $ _type = "least favorite"

        girl.char "Do you remember what is my [_type] [thing]?"

        python:

            fav_list = []

            if _type == "favorite":
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

            m.append(("[girl.name]'s [_type] [thing] is...", None))

            for h in fav_list:

                m.append((h, h))

            m.append(("I don't know", "give up"))

            r = menu(items = m)

        $ norollback()

        if (_type == "favorite" and r == girl.likes[thing]) or (_type == "least favorite" and r == girl.dislikes[thing]):

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

    if girl.love < 90:
        $ girl.love = 90

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

    $ norollback()

    if group not in ("gold", "gift"): # Counters for giving gold and presents are handled in their own label
        $ girl.MC_interact_counters[group] += 1
        $ girl.talked_to_date = calendar.time
        $ MC.interactions -= 1

    return


#### END OF FREE GIRL INTERACTIONS FILE ####
