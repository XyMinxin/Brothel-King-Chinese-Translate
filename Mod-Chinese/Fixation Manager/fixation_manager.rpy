
init -1 python:

    def addPosFixation(girl_id, fixName):
        girl_id.pos_fixations.append(fix_dict[fixName])
        
    def remPosFixation(girl_id, fixName):
        girl_id.pos_fixations = [fix for fix in girl_id.pos_fixations if fix.name != fixName]
    
    def addNegFixation(girl_id, fixName):
        girl_id.neg_fixations.append(fix_dict[fixName])
    
    def remNegFixation(girl_id, fixName):
        girl_id.neg_fixations = [fix for fix in girl_id.neg_fixations if fix.name != fixName]
    
    def addToDict(name, key, value):
        if key not in name.keys():
            name[key] = value
        else:
            if type(name[key]) is list:
                name[key].append(value)
    
    def magic_add_fix(girl, fix_name, type = None, magic_bonus = 0, difficulty_mod = 1, bad_outcomes = True):
        if type == "love":
            chance = int(40 * difficulty_mod) + magic_bonus + (girl.mood + girl.get_love() - girl.get_fear()) // 3
            lock_chance = 0
        elif type == "neutral":
            chance = 40
            lock_chance = 0
        elif type == "fear": # Fear gives a higher bonus and ignores mood but may lock a girl's negative fixation
            chance = int(50 * difficulty_mod) + magic_bonus + girl.get_fear()
            lock_chance = int(3 + magic_bonus // 10.0)

        if dice(100) < lock_chance:
            if bad_outcomes:
                girl.locked_fix.append(fix_name)
                return "locked"
            else:
                return magic_add_fix(girl, fix_name, type, magic_bonus, difficulty_mod, bad_outcomes)

        elif dice(100) < chance:
            girl.fix_level[fix_name] += 1

            if girl.fix_level[fix_name] < 4:
                return girl.fix_level[fix_name]

            else:
                addPosFixation(girl, fix_name)
                return "success"

        else:
            if bad_outcomes:
                return "fail"
            else:
                return magic_add_fix(girl, fix_name, type, magic_bonus, difficulty_mod, bad_outcomes)
    
    fm_template = Mod(

                ## Basic mod information (Important: Version is used to check for new versions of the mod. Failure to update the version number may lead to broken mods and saved games)
                name = "性癖管理器",
                folder = "Fixation Manager",
                creator = "Noones Beezwax",
                version = 0.2,
                description = """修改女孩的正面和负面性癖""",

                ## Mod option menu (access through the Help (click on '?') menu)
                help_prompts = [("显示菜单按钮", "fm_show"), ("隐藏菜单按钮", "fm_hide")],

                ## Init label: This will run when the mod is activated, allowing you to set some variables and events if necessary
                init_label = "fm_init",
                )
    

label fm_init():

    $ fm = fm_template
    
    default girl_id = None
    default fm_x = 95.0
    default fm_y = 95.0
    default fm_menu = 'options'
    default story_mode = True # Controls if cheat mode is on. When true cheat mode is disabled
    default difficulty = {
        'set': ['Normal', 1.0],
        'list': ['Very Easy','Easy', 'Normal', 'Hard', 'Very Hard'],
        'Very Easy': 2.4,
        'Easy': 1.5,
        'Normal': 1.0,
        'Hard': 0.5,
        'Very Hard': 0.1,
    }
    default can_fail = True # If hypnosis can fail
    default fix_dict_fm = {
        'all': [],
        'cat': ['naked', 'service', 'sex', 'anal', 'fetish', 'bisexual', 'group'],
        'cat_ext': ['naked', 'service', 'sex', 'anal', 'fetish', 'bisexual', 'group', 'cum'],
        'naked': [],
        'service': [],
        'sex': [],
        'anal': [],
        'fetish': [],
        'bisexual': [],
        'group': [],
        'cum': [],
        }
    default custom_cat = {
        'cum': ['bukkake', 'cum in mouth', 'cum on face', 'cum in hair', 'cum on body', 'cum shower', 'swallowing', 'creampie', 'cum inside'],
    }
    default sort_mode = 'all'
    python:
        addToDict(interact_dict, "MAGIC SKILL TRAINING", GirlInteractionTopic("magic", "train", "Fixation training", "slave_magic_fixation", gold_cost=100))
        for fix in fix_dict:
            fix_dict_fm['all'].append(fix_dict[fix])
            if fix in custom_cat['cum']:
                fix_dict_fm['cum'].append(fix_dict[fix])
            for act in fix_dict[fix].acts:
                fix_dict_fm[act].append(fix_dict[fix])
            
    
label fm_show():
    show screen fm_box
    return

label fm_hide():
    hide screen fm_box
    return

label slave_magic_fixation(girl):

    if not girl.magic_training:
        call slave_hypnotize_method(girl) from _call_slave_hypnotize_method_fm_1

    $ text1 = rand_choice(MC.filter_say(("ar: 太阳神的圣光啊{nw}", "sh: 潜藏于暗影中的莎莉娅啊{nw}", "五大元素啊{nw}", "ev: 地狱的黑暗力量啊{nw}", "gd: 我纯净的灵魂啊", "ne: 龙族的咆哮啊{nw}",
                   "ng: 时光之砂啊{nw}", "神秘的旋律啊{nw}", "死星的放射波动啊{nw}", "猩红之月的暗面啊{nw}", "无尽之海的深渊啊{nw}")))

    $ text1 += "，听我号令，"

    $ text1 += rand_choice(("跟着我的声音走进迷宫...", "脱离物质世界的禁锢...",
                           "陷入深深的沉睡...", "不要抵抗梦境的侵蚀...", "踏上遗忘之海的旅程...",
                           "忘记你是谁，忘记你躺在哪里...", "你是我故事中的角色..."))

    play sound s_spell

    "听到你的声音, [girl.name]好像听不清具体的内容。她伫立不动，茫然地望着远方，双目无神。"

    if girl.magic_training == "positive":
        "你温柔地和她交流。"
        $ bonus = (girl.get_love() - girl.get_fear())//10
        $ magic_type = "love"

    elif girl.magic_training == "negative":
        "你用言语威胁着她。"
        $ bonus = (girl.get_fear() - girl.get_love())//10
        $ magic_type = "fear"
        
    else:
        "你平静地和她交流。"
        $ bonus = 0
        $ magic_type = "neutral"

    $ bonus += girl.get_effect("change", "hypnosis")

    python:
        
        exist_fix = girl.neg_fixations + girl.pos_fixations
        
        pos_fix = [fix_dict[fix] for fix in fix_dict if fix_dict[fix] not in exist_fix]

        if len(pos_fix) == 1:
            fix = pos_fix[0]

            renpy.say(you, "今天，我想让你试着习惯[fix.short_name]。")

        else:
            menu_list = [] #[("Choose a fixation to work on", None)]
            if sort_mode == 'all':
                for fix in pos_fix:
                    if fix.name in girl.locked_fix:
                        menu_list.append(("{color=[c_lightgrey]}" + __(fix.name.capitalize()) + "(已锁定){/color}", fix))
                    else:
                        menu_list.append((__(fix.name.capitalize()), fix))
            else:
                for cat in fix_dict_fm[sort_mode]:
                    menu_list.append((cat.capitalize(), cat))
                cat = menu(menu_list)
                menu_list = []
                sub_menu = [fix for fix in fix_dict_fm[cat] if fix in pos_fix]
                for fix in sub_menu:
                    if fix.name in girl.locked_fix:
                        menu_list.append(("{color=[c_lightgrey]}" + __(fix.name.capitalize()) + "(已锁定){/color}", fix))
                    else:
                        menu_list.append((__(fix.name.capitalize()), fix))
            menu_list.append(("Go back", "back"))
            renpy.say(you, "今天，我想让你试着习惯...", interact=False)
            fix = long_menu('选择一个性癖', menu_list) # renpy.display_menu(menu_list)

    if fix == "back":
        $ inter.canceled=True
        return
    
    $ available_acts = []
    
    python:
        for act in fix.acts:
            if girl.will_do_sex_act(act):
                if not (girl.has_trait("Virgin") and act == "sex"):
                    available_acts.append(act)

    if not available_acts:
        "[girl.fullname]对任何必要的性行为都感到不适，无法培养性癖。"
        $ inter.canceled=True
        return
    if "naked" in available_acts:
        $ diff = 4
        $ act = "naked"
    elif "service" in available_acts:
        $ diff = 5
        $ act = "service"
    elif "sex" in available_acts:
        $ diff = 6
        $ act = "sex"
    elif "anal" in available_acts:
        $ diff = 7
        $ act = "anal"
    elif "fetish" in available_acts:
        $ diff = 8
        $ act = "fetish"
    elif "bisexual" in available_acts:
        $ diff = 9
        $ act = "bisexual"
    elif "group" in available_acts:
        $ diff = 10
        $ act = "group"
        
    if girl.is_("very dom"):
        $ diff += 1
    elif girl.is_("very sub"):
        $ diff -= 2
    elif girl.is_("sub"):
        $ diff -= 1

    # Run challenge
    if MC.get_effect("special", "snake eyes"):
        $ force_win = 3
    else:
        $ force_win = False

    call challenge("control", diff, bonus=bonus, score=True, forced=force_win) from _call_challenge_fm_1 # result is stored in the _return variable
    $ inter.score = _return

    $ d = MC.challenges["control"].d - MC.challenges["control"].d_op

    if d >= 3:
        "魔力之风效果强劲。你牢牢地控制住了她的灵魂。{nw}"
    elif d <= -3:
        "你对她思维的控制十分微弱。你得快点。 {nw}"
    else:
        "她的潜意识在抵抗你，但你努力地克服了它。{nw}"

    $ not_tags = prepare_not_tags(girl, inter.act, [fix.name])
    $ pic = girl.get_fix_pic(inter.act, fix, not_tags=not_tags)

    if not pic:
        if fix.step == 1:
            $ pic = girl.profile

        elif fix.step == 2:
            $ pic = girl.get_pic(inter.act, "naked", "rest", "profile", not_tags=not_tags, hide_farm=True, pref_filter=True)

        elif fix.step == 3:
            $ pic = girl.get_pic("rest", "profile", and_tags = "naked", not_tags=not_tags, hide_farm=True, pref_filter=True)


    call hide_everything() from _call_hide_everything_fm_1
    with fade

    $ renpy.say("", __(fix_description[fix.name + " intro"]) % girl.name)

    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
    with dissolve

    if inter.score > 0:
        $ girl.add_log("hypnotize success")
        
        play sound s_spell

        extend "[girl.name]双眼无神，似乎没有意识到你在做什么，只是盲目地听从你的命令。"
        
        $ inter.result = magic_add_fix(girl, fix.name, magic_type, d, difficulty['set'][1], can_fail)
        $ norollback()
        
        if inter.result == "success":
            girl.char "哦，主人..."
            play sound s_mmmh

            $ renpy.say("", __(fix_description[fix.name + " pos_reaction"]))

            $ renpy.say("", __("训练效果显著。") + event_color["special"] % (girl.fullname + __("现在喜欢上") + __(fix.name) + "了。"))
        
        elif inter.result == "fail":
            play sound s_fizzle
    #         girl.char "..."
            $ renpy.say("", fix_description[fix.name + " neg_reaction"])
            $ renpy.say("", event_color["a little bad"] % ("你的训练没有带来任何显著的进步。"))

        elif inter.result == "locked":
            play sound s_scream_loud
            girl.char "NO! Go away!!!"
            "[girl.name]把你推开，蜷缩起来，泪流满面。你不能再从她嘴里套出什么了。"

            $ renpy.say("", "你粗暴的训练让她有些吃不消了。" + event_color["bad"] % ("她现在一辈子都无法接受" + fix.name + "了。"))

        else:

            play sound s_spell

            if inter.result == 1:
                "[girl.name]她还是很不情愿，但你可以让她做一两个简单的操作。"
                $ renpy.say("",  __("训练成功了。") + event_color["good"] % (girl.name + __("的训练初见成效。")))
            elif inter.result == 2:
                $ text1 = fix_description[fix.name + " description"]

                "[girl.name]开始喜欢上[text1]了，她的进步令人鼓舞。"
                $ renpy.say("",  __("训练成功了。") + event_color["good"] % (girl.name + __("的训练进展迅速。")))
            elif inter.result == 3:
                $ text1 = __(fix.name).capitalize()
                "[girl.name]今天表现得非常好。她发现自己经常幻想着[text1]。"
                $ renpy.say("",  __("训练成功了。") + event_color["good"] % (girl.name + __("的训练突飞猛进。")))

    elif inter.score == 0 or MC.get_effect("special", "hypnosis no fail"):

        $ inter.result = "moderate"

        play sound s_spell

        extend "[girl.name]看起来晕头转向，满脸通红。她不服从你的命令，但你能感觉到她的反抗在减弱。"

        "几分钟后，你停止了实验，因为只取得了一点进展。"

    else:

        $ inter.result = "fail"
        $ girl.add_log("hypnotize failure")

        play sound s_fizzle

        extend ""

        call dialogue(girl, "slave magic failure") from _call_dialogue_fm_2

    return

screen fm_box:
    hbox:
        xalign fm_x/100.0
        yalign fm_y/100.0
        textbutton "性癖改造菜单" action Show("fm_main") text_size 18

screen fm_main():
    modal True
    frame:
        background '#aace'
        xsize 0.3
        yfill True
        has vbox
        hbox:
            textbutton '选择女孩':
                if story_mode:
                    action None
                else:
                    action [[SetVariable('fm_menu', 'girl'), SetVariable('girl_id', None)]]
            textbutton '设置' action SetVariable('fm_menu', 'options')
            textbutton '关闭' action Hide('fm_main')
        if fm_menu == 'options':
            use fm_options
        else:
            if not girl_id:
                use all_girls
            else:
                use girl_edit
        $ renpy.block_rollback()

screen all_girls:
    vbox:
        text '选择女孩'
        vpgrid:
            cols 1
            xfill True
            mousewheel True
            scrollbars "vertical"
            spacing 0
            for girl in MC.girls:
                textbutton "{}".format(girl.get_name()) action SetVariable("girl_id",girl) xfill True

screen girl_edit:

    viewport:
        mousewheel True
        draggable True
        scrollbars "vertical"
        xfill True
        yfill True
        spacing 5
        has vbox
        hbox:
            vbox xsize xres(100):
                text "负 面" color c_crimson
            vbox xsize xres(100) xalign 0.5:
                text "性癖列表"
            vbox xsize xres(100) xalign 1.0:
                text "  正 面" color c_emerald
                
        $ posfix = [girlfix.name for girlfix in girl_id.pos_fixations]
        $ negfix = [girlfix.name for girlfix in girl_id.neg_fixations]
        for fix in fix_dict:
            hbox:
                vbox xsize xres(75) xalign 0.5:
                    if fix in negfix:
                        textbutton "{b}厌恶{/b}":
                            action Function(remNegFixation, girl_id, fix)
                            text_color c_crimson
                    else:
                        textbutton "默认":
                            action [Function(remPosFixation, girl_id, fix), Function(addNegFixation, girl_id, fix)]
                vbox xsize xres(150) xalign 0.5:
                    text "{}".format(fix.capitalize()) layout "nobreak"
                vbox xsize xres(75) xalign 0.5:
                    if fix in posfix:
                        textbutton "{b}沉迷{/b}":
                            action Function(remPosFixation, girl_id, fix)
                            text_color c_emerald
                    else:
                        textbutton "默认":
                            action [Function(remNegFixation, girl_id, fix), Function(addPosFixation, girl_id, fix)]

screen fm_options:
    vbox:
        vbox:
            text "位置设置:" color "#33cccc"
            hbox:
                text "横坐标"
                bar:
                    xsize 200
                    value VariableValue("fm_x",100)
                text "{}".format(fm_x/100.0)
            hbox:
                text "纵坐标"
                bar:
                    xsize 200
                    value VariableValue("fm_y",100)
                text "{}".format(fm_y/100.0)
            textbutton '重置设置' action [SetVariable('fm_x', 95.0), SetVariable('fm_y', 95.0)]
        vbox:
            text "难度设置:" color "#33cccc"
            for diff in difficulty['list']:
                textbutton '{}'.format(diff) action SetVariable("difficulty['set']", [diff, difficulty[diff]])
        vbox:
            text "额外设置:" color "#33cccc"
            hbox:
                text '训练能否失败:'
                if can_fail:
                    textbutton '可失败' action SetVariable('can_fail', False)
                else:
                    textbutton '不会失败' action SetVariable('can_fail', True)
            hbox:
                text '剧情/自由模式:'
                if story_mode:
                    textbutton '剧情模式' action SetVariable('story_mode', False)
                else:
                    textbutton '自由模式' action SetVariable('story_mode', True)
        vbox:
            text "性癖排序方式:" color "#33cccc"
            textbutton '所有的' action SetVariable('sort_mode', 'all')
            textbutton '按照行为排序' action SetVariable('sort_mode', 'cat')
            textbutton '按照行为排序(扩展)' action SetVariable('sort_mode', 'cat_ext')