###### Game settings menu (formerly H content) ######

#### Default values ####

default persistent.fix_pic_balance = fix_pic_balance_variety # Sets weights for the 'get_fix_pic()' Girl method

default persistent.forbidden_tags = []

default persistent.use_stock_pictures_missing = False
default persistent.use_stock_pictures_low = False

default persistent.show_girlpack_rating = None

default persistent.mix_group_pictures = False
default persistent.mix_bis_pictures = False

default persistent.naked_girls_in_slavemarket = False
default persistent.naked_girls_in_town = False

default persistent.fuzzy_tagging_jobs = True
default persistent.fuzzy_tagging_acts = True

default persistent.home_screen_notifications = 0 # 0 = default, 1 = no flashing, 2 = n notification

default persistent.show_girl_status = {"away": True, "farm": True, "rest": True, "scheduled": False, "half-shift": True, "master bedroom": True, "work&whore": True, "not work&whore": False, "naked": True, "not naked": False, "negative fixation": True}

default persistent.badges_on_portraits = False

default persistent.skipped_events = defaultdict(bool)
default persistent.can_skip_reports = False
default persistent.can_skip_night_recap = False

default persistent.keep_firstname = False
default persistent.keep_lastname = False
default persistent.gp_name_customization = False

default persistent.dark_night_UI = False

default persistent.sanity_display = False

default persistent.girls_display_mode = "pages"


#### Game menu creation ####

init python:
    class HMSetting(object):
        """A basic setting for the H menu"""

        def __init__(self, variable, captions=None, ttips=None, values=(False, True), range=2, special=False):
            self.variable = variable
            self.captions = captions or [("OFF"), ("ON")]
            self.ttips = ttips or [("OFF"), ("ON")]
            self.values = values
            self.range = range
            self.special = special

        def toggle(self):
            idx = self.get_index()

            if idx < self.range-1:
                setattr(persistent, self.variable, self.values[idx+1])
            else:
                setattr(persistent, self.variable, self.values[0])
            


            # if self.range == 2: # Persistent value is boolean
            #     setattr(persistent, self.variable, not self.get())
            # else: # persistent value is an index from 0 to range
            #     if self.get() < self.range-1:
            #         setattr(persistent, self.variable, self.get()+1)
            #     else:
            #         setattr(persistent, self.variable, 0)

            # if self.toggle_function:
            #     self.toggle_function(self.get())

        def get(self):
            return getattr(persistent, self.variable)

        def get_index(self):
            return self.values.index(self.get())

        def caption(self):
            return self.captions[self.get_index()]

        def tooltip(self):
            return self.ttips[self.get_index()]



default hm_sections = ["content", "pictures", "UI", "misc"]
default hm_section_titles = {"content": "内容设置", "pictures": "图片设置", "UI": "UI设置", "misc": "其他设置"}

# HM settings will be displayed in order for each section
default hm_settings = {
    "content" : [
            "激活或关闭不良内容（不会影响故事场景）。",
            HMSetting("forbidden_tags", special=True),
        ], 
        "pictures" : [
            "选择当一个女孩包缺少带有给定标签的图片时是否使用默认图片。",
            HMSetting("use_stock_pictures_missing", captions=["使用角色包中的其他图片", "使用默认图片"], ttips=["The game will pick a picture from the same girlpack with the closest possible tag (e.g. 'service' instead of 'handjob').", "The game will pick a default picture with the proper tag."]),

            "当一个女孩包在给定标签上的图片多样性低时，是否使用游戏预设图片 (少于 %s 张)。" % stock_picture_threshold,
            HMSetting("use_stock_pictures_low", captions=["只使用角色包内的图片", "将角色包图片与游戏预设图片混合"], ttips=["The game will use only the girlpack pictures that are in the pool, at the risk of repetition.", "The game will add some default pictures to the pool for variety."]),

            "在为高级培训生成图片时选择优先级。",
            HMSetting("fix_pic_balance", ["多样性高于准确性", "准确性高于多样性"], ttips=["The game will prioritize picture variety over accurate tagging.", "The game will prioritize accurate tagging over picture variety."], values=[fix_pic_balance_variety, fix_pic_balance_accuracy]),

            "选择双飞和群交恋图片的范围",
            HMSetting("mix_group_pictures", ["群交: 只使用含有群交标签的图片", "将群交图片与常规图片混合"], ttips=["The game will only pick pictures featuring a group.", "The game will sometimes pick normal pictures for variety."]),
            HMSetting("mix_bis_pictures", ["兽交: 只使用含有兽交标签的图片", "将兽交图片与常规图片混合"], ttips=["The game will only pick pictures featuring a group.", "The game will sometimes pick normal pictures for variety."]),

            "选择“女孩”选项卡之外的立绘图片设置。",
            HMSetting("naked_girls_in_slavemarket", ["奴隶市场: 不使用裸体标签图片作为立绘", "奴隶市场: 可以使用裸体标签图片作为立绘"], ttips=["The slavemarket may not display naked profile pictures.", "The slavemarket may display naked pictures."]),
            HMSetting("naked_girls_in_town", ["城市内: 不使用裸体标签图片作为立绘", "城市内: 可以使用裸体标签图片作为立绘"], ttips=["Free girls may not display naked profile pictures.", "Free girls may display naked pictures ('Naturist' trait)."]),

            "允许扩展工作和性行为标签的图片。",
            HMSetting("fuzzy_tagging_jobs", ["工作图片: 精准符合标签", "工作图片: 模糊符合标签"], ttips=["Job pictures will only look for accurate tags (e.g. 'masseuse' for masseuse).", "Job pictures will extend the search to 'close enough' tags (e.g. 'swimsuit' for masseuse)."]),
            HMSetting("fuzzy_tagging_acts", ["性爱图片: 精准符合标签", "性爱图片: 模糊符合标签"], ttips=["Sex pictures will only look for accurate tags (e.g. 'toy' for fetish).", "Job pictures will extend the search to 'close enough' tags (e.g. 'machine' for fetish)."]),
        ], 
        "UI" : [
            "在主界面按钮旁边显示“新闻”通知。",
            HMSetting("home_screen_notifications", ["通知闪烁", "不闪烁", "不通知"], ttips=["Display a flashing notification until you hover the mouse over it (default).", "Display a static notification.", "Display no notification."], range=3, values=range(3)),

            "使用可滚动屏幕或编号标签浏览“女孩”屏幕（标签可能会提高性能）。",
            HMSetting("girls_display_mode", ["Scroll girls", "Use tabs"], ttips=["Display girls on a signle scrollable screen (legacy mode: may decrease performance).", "Display girls with numbered tabs (may improve performance)."], range=2, values=["vp", "pages"]),

            "显示女孩档案的女孩包评级",
            HMSetting("show_girlpack_rating", ["永不显示", "仅在奴隶市场显示", "在奴隶市场和城市中显示", "始终显示"], ttips=["Never display girlpack rating on profile.", "Display rating on profile in slavemarket only.", "Display rating on profile in slavemarket and city.", "Always display rating on profile."], values = [None, "In slavemarket", "In market and city", "Everywhere"], range=4),

            "在女孩立绘上显示可选的状态图标。",
            HMSetting("show_girl_status", special=True),

            "在女孩的心情属性上显示理智。",
            HMSetting("sanity_display", ["仅在农场中显示", "始终显示"], ttips=["Sanity will only display when a girl is at the farm.", "Sanity will be displayed on the 'Mood' recap."]),

            "选择如何为你的女孩编辑徽章设置。",
            HMSetting("badges_on_portraits", ["只在头像上显示", "在立绘和头像上都显示"], ["Click on a badge in the girl's profile to change it.", "Click on a badge in the girl's profile or portrait to change it."]),

            "在“经营事件”循环中隐藏事件。",
            HMSetting("skipped_events", special=True),

            "允许在“经营事件”循环中跳过。",
            HMSetting("can_skip_reports", ["报告: 不可跳过", "报告: 可以跳过"], ttips=["Skipping matchmaking and satisfaction reports with 'Ctrl' is not possible.", "Skipping matchmaking and satisfaction reports with 'Ctrl' is possible."]),
            HMSetting("can_skip_night_recap", ["每晚回顾：不可跳过", "每晚回顾：可以跳过"], ttips=["Skipping the nightly recap with 'Ctrl' is not possible.", "Skipping the nightly recap with 'Ctrl' is possible."]),

            "选择“经营事件”事件（WIP）的显示模式。",
            HMSetting("dark_night_UI", ["明亮风格", "深色风格"], ttips=["End day events are presented in light mode.", "End day events are presented in dark mode."]),


        ], 
        "misc" : [
            "为非原创女孩（“克隆人”）定义姓名选项。",
            HMSetting("keep_firstname", ["随机角色名字", "保留角色名字"], ttips=["First name will be randomized for non-original girls.", "First name will be remain the same as the original for non-original girls."]),
            HMSetting("keep_lastname", ["随机角色姓氏", "保留角色姓氏"], ttips=["Last name will be randomized for non-original girls.", "Last name will be remain the same as the original for non-original girls."]),
            HMSetting("gp_name_customization", ["优先考虑女孩包设置", "优先考虑游戏设置"], ttips=["The girlpack's _BK.ini settings will take precedence over the settings above.", "The settings above will take precedence over the girlpack's _BK.ini settings."]),
        ]
        }

default hm_tag_captions = {"beast" : "兽交", "monster" : "怪物/触手", "machine" : "机械"}

default hm_girl_status_list = [("away", "away.webp", "外出完成委托或接受培训"), ("farm", "farm.webp", "在农场中训练或休息"), ("rest", "rest.webp", "正在休息"), ("scheduled", "scheduled.webp", "预定休息"), ("half-shift", "half.webp", "半班制。"), ("master bedroom", "master.webp", "接受私人指导。"), ("negative fixation", "negfix.webp", "发现负面性癖"), ("naked", "naked.webp", "现在一丝不挂。"), ("not naked", "not_naked.webp", "现在穿着衣服。"), ("work&whore", "ww.webp", "一边工作一边勾引客人。"), ("not work&whore", "not_ww.webp", "专心工作。")]

default hm_night_events = [("Normal", "Normal events"), ("Matchmaking", "Matchmaking reports"), ("Customer", "Customer special events"), ("Level/Job/Rank up", "Level up, Job up and Rank up notifications"), ("Health/Security", "Health and security events"), ("Satisfaction", "Customer satisfaction report"), ("Farm", "Farm events"), ("Rest", "Resting events")]

#### Game Settings Screen ####

screen hm_forbidden_tags():
    hbox:
        for _tag in ("beast", "monster", "machine"):
            if _tag in persistent.forbidden_tags:
                $ text1 = ": 禁用"
            else:
                $ text1 = ": 启用"
            
            textbutton _(hm_tag_captions[_tag] + text1):
                style "hm_button2"
                size_group "forbidden_tags"
                xpadding xres(18)
                xsize xres(190)

                if _tag in persistent.forbidden_tags:
                    action (RemoveFromSet(persistent.forbidden_tags, _tag), SelectedIf(False))
                    tooltip "游戏将尽量不显示这样的图片 (警告：这可能不是100%生效，也不会改变使用这些调教的故事事件。)"
                else:
                    action (AddToSet(persistent.forbidden_tags, _tag), SelectedIf(True))
                    tooltip "游戏会显示这样的图片。"

screen hm_girl_statuses():
    default current_status = ""

    hbox spacing xres(12):
        hbox box_wrap True spacing xres(6):
            style_group None
            for status, pic, ttip in hm_girl_status_list:
                button action ToggleDict(persistent.show_girl_status, status) tooltip ttip:
                    if persistent.show_girl_status[status]:
                        background Frame("lightblue_button", borders=gui.button_borders)
                        add ProportionalScale("UI/status/" + pic, *res_tb(30))

                    else:
                        background Frame("lightgrey_button", borders=gui.button_borders)
                        add ProportionalScale("UI/status/" + pic, *res_tb(30), matrixcolor=SaturationMatrix(0))

screen hm_skip_night_events():
    hbox box_wrap True:
        for ev_type, ttip in hm_night_events:
            textbutton _(ev_type) style "hm_button2" text_size res_font(16) xalign 0.0 action (ToggleDict(persistent.skipped_events, ev_type), SelectedIf(not persistent.skipped_events[ev_type])) tooltip ttip + {False: "将显示。", True: "将隐藏。"}[persistent.skipped_events[ev_type]]


screen h_content(): # H preferences and various game settings

    tag menu

    use game_menu(_("Game settings"), scroll="viewport"):

        frame xfill True style "pref_frame":
            has vbox xfill True
            style_group "hm"

            for section in hm_sections:
                label _(hm_section_titles[section]) text_bold True

                for setting in hm_settings[section]:
                    if is_string(setting):
                        text "\n" + setting
                    elif setting.special: # Custom buttons that do not behave as toggleable objects
                        # Forbidden_tags
                        if setting.variable == "forbidden_tags":
                            use hm_forbidden_tags()
                        elif setting.variable == "show_girl_status":
                            use hm_girl_statuses()
                        elif setting.variable == "skipped_events":
                            use hm_skip_night_events()
                    else:
                        textbutton _(setting.caption()) action (Function(setting.toggle), SelectedIf(setting.get_index())) tooltip _(setting.tooltip()) xsize 0.5

                null height yres(20)
    
    use adv_tooltip()
                

#### HM styles ####

style hm_button:
    selected_background Frame("lightblue_button", borders=gui.button_borders)

style hm_text color c_brown italic True size res_font(16)

style hm_button2 is hm_button:
    idle_background Frame("lightgrey_button", borders=gui.button_borders)
    selected_idle_background Frame("darkorange_button", borders=gui.button_borders)
    # selected_foreground "tb empty"

style hm_button_text size res_font(18)

style hm_button2_text is hm_button_text:
    idle_color c_darkgrey
    selected_color c_white
    xalign 0.0


#### Depreciated ###

# screen h_content_old(): # H preferences and various player settings

#     tag menu

#     use game_menu(_("Game settings"), scroll="viewport"):

#         frame xfill True style "pref_frame":
#             has vbox xfill True

#             label _("Content settings") text_bold True

#             # Objectionable content

#             text "\nActivate or deactivate objectionable content (won't affect story scenes)" color c_brown italic True size res_font(16)

#             if "beast" in persistent.forbidden_tags:
#                 $ text1 = "OFF"
#             else:
#                 $ text1 = "ON"

#             textbutton _("Bestiality: " + text1) text_size res_font(18) xalign 0.0 xsize 0.8 xfill True:
#                 if "beast" in persistent.forbidden_tags:
#                     action RemoveFromSet(persistent.forbidden_tags, "beast")
#                 else:
#                     action AddToSet(persistent.forbidden_tags, "beast")

#             if "monster" in persistent.forbidden_tags:
#                 $ text1 = "OFF"
#             else:
#                 $ text1 = "ON"

#             textbutton _("Monsters/Tentacles: " + text1) text_size res_font(18) xalign 0.0 xsize 0.8 xfill True:
#                 if "monster" in persistent.forbidden_tags:
#                     action RemoveFromSet(persistent.forbidden_tags, "monster")
#                 else:
#                     action AddToSet(persistent.forbidden_tags, "monster")

#             if "machine" in persistent.forbidden_tags:
#                 $ text1 = "OFF"
#             else:
#                 $ text1 = "ON"

#             textbutton _("Machines: " + text1) text_size res_font(18) xalign 0.0 xsize 0.8 xfill True:
#                 if "machine" in persistent.forbidden_tags:
#                     action RemoveFromSet(persistent.forbidden_tags, "machine")
#                 else:
#                     action AddToSet(persistent.forbidden_tags, "machine")

#             text ""

#             label _("Picture settings") text_bold True

#             # Missing Picture algorithm

#             text "\nChoose the behavior of stock (default) pictures and girl pack pictures" color c_brown italic True size res_font(16)

#             if persistent.use_stock_pictures["missing"]:
#                 $ text1 = "When a picture is missing:\nUse stock pictures"
#             else:
#                 $ text1 = "When a picture is missing:\nUse another picture from the girl pack"

#             if persistent.use_stock_pictures["low"]:
#                 $ text2 = "When the picture count is low:\nMix stock and girl pack pictures"
#             else:
#                 $ text2 = "When the picture count is low:\nOnly use girl pack pictures"

#             textbutton text1 text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action ToggleDict(persistent.use_stock_pictures, "missing")
#             textbutton text2 text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action ToggleDict(persistent.use_stock_pictures, "low")

#             # Advanced Picture algorithm

#             text "\nChoose the behavior of advanced training pictures" color c_brown italic True size res_font(16)
#             if persistent.fix_pic_balance == fix_pic_balance_variety:
#                 textbutton "Advanced training pictures: Better variety" text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action SetField(persistent, "fix_pic_balance", fix_pic_balance_accuracy)
#             else:
#                 textbutton "Advanced training pictures: Better accuracy" text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action SetField(persistent, "fix_pic_balance", fix_pic_balance_variety)

#             # Group/Bis Picture algorithm

#             text "\nChoose the behavior of group and bisexual pictures" color c_brown italic True size res_font(16)
#             textbutton {True: "Group sex: Mix group pictures with regular pictures", False: "Group sex: Only use group sex pictures"}[persistent.mix_group_pictures] text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "mix_group_pictures")
#             textbutton {True: "Bisexual sex: Mix bisexual pictures with regular pictures", False: "Bisexual sex: Only use bisexual pictures"}[persistent.mix_bis_pictures] text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "mix_bis_pictures")

#             # Naked girls' settings


#             text "\nChoose the behavior of slavemarket girls' pictures" color c_brown italic True size res_font(16)
#             textbutton {True: "Allow naked pictures in the slavemarket", False: "No naked pictures in the market"}[persistent.naked_girls_in_slavemarket] text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "naked_girls_in_slavemarket")

#             text "\nChoose the behavior of free girls' pictures" color c_brown italic True size res_font(16)
#             textbutton {True: "Allow naked pictures in the city (naturist trait)", False: "No naked pictures in the city"}[persistent.naked_girls_in_town] text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "naked_girls_in_town")

#             # Fuzzy tagging
#             text "\nAllow 'close enough' tags to be used (e.g. 'swimsuit' for masseuse events)" color c_brown italic True size res_font(16)

#             hbox xalign 0.0 xsize 0.8:
#                 textbutton "For jobs: %s" % ({True: "ON", False: "OFF"}[persistent.fuzzy_tagging_jobs]) text_size res_font(18) xsize xres(312) action ToggleField(persistent, "fuzzy_tagging_jobs")
#                 textbutton "For sex acts: %s" % {True: "ON", False: "OFF"}[persistent.fuzzy_tagging_acts] text_size res_font(18) xsize xres(312) action ToggleField(persistent, "fuzzy_tagging_acts")

#             text ""

#             label _("UI settings") text_bold True

#             # Pack ratings

#             text "\nDisplay pack rating on girl profiles" color c_brown italic True size res_font(16)

#             if persistent.show_girlpack_rating:
#                 $ text1 = persistent.show_girlpack_rating
#             else:
#                 $ text1 = "OFF"

#             textbutton "Show Girl Pack Rating: [text1]" text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action SetField(persistent, "show_girlpack_rating", get_next([None, "In slavemarket", "In market and city", "Everywhere"], persistent.show_girlpack_rating, loop=True))

#             # Use flashing notifications

#             text "\nDisplay notifications next to buttons on the home screen" color c_brown italic True size res_font(16)

#             default notif_state = {0: "Flashing notifications (default)", 1: "Static notifications", 2: "No notifications"}

#             textbutton notif_state[persistent.home_screen_notifications] text_size res_font(18) xalign 0.0 xsize 0.8 xfill True: #?
#                 if persistent.home_screen_notifications <= 1:
#                     action SetField(persistent, "home_screen_notifications", persistent.home_screen_notifications+1)
#                 else:
#                     action SetField(persistent, "home_screen_notifications", 0)

#             # Show/Hide girl status

#             text "\nDisplay girl status icons" color c_brown italic True size res_font(16)

#             default current_status = ""

#             hbox spacing xres(12):
#                 hbox box_wrap True spacing xres(6):
#                     style_group None
#                     for status in [("away", "away.webp"), ("farm", "farm.webp"), ("rest", "rest.webp"), ("scheduled", "scheduled.webp"), ("half-shift", "half.webp"), ("master bedroom", "master.webp"), ("work&whore", "ww.webp"), ("naked", "naked.webp"), ("negative fixation", "negfix.webp"), ("not naked", "not_naked.webp"), ("not work&whore", "not_ww.webp")]:

#                         if status:
#                             button action ToggleDict(persistent.show_girl_status, status[0]) hovered SetScreenVariable("current_status", status[0]) unhovered SetScreenVariable("current_status", ""):
#                                 if persistent.show_girl_status[status[0]]:
#                                     background Frame("lightblue_button", borders=gui.button_borders)
#                                     add ProportionalScale("UI/status/" + status[1], *res_tb(30))

#                                 else:
#                                     add ProportionalScale("UI/status/" + status[1], *res_tb(30), matrixcolor=SaturationMatrix(0))

#                 if current_status:
#                     text "%s\n(%s)" % (current_status.capitalize(), {True : "active", False : "inactive"}[persistent.show_girl_status[current_status]]) bold True size res_font(14) color c_prune yalign 0.5

#             # Badge settings

#             text "\nYour preferences for setting girl badges" color c_brown italic True size res_font(16)
#             textbutton {True: "Badges can be modified directly on girls' portraits", False: "Badges can only be modified on a girl's profile"}[persistent.badges_on_portraits] text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "badges_on_portraits")

#             # Night events settings

#             text "\nShow/Skip night events" color c_brown italic True size res_font(16)

#             for ev_type in ["Normal", "Matchmaking", "Customer", "Level/Job/Rank up", "Health/Security", "Satisfaction report", "Farm", "Rest"]:

#                 $ text1 = ev_type

#                 if ev_type != "Satisfaction report":
#                     $ text1 += " events"

#                 if persistent.skipped_events[ev_type]:
#                    $ text1 += ": OFF"
#                 else:
#                    $ text1 += ": ON"

#                 textbutton _(text1) text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action ToggleDict(persistent.skipped_events, ev_type)

#             textbutton "Block skipping on night reports: " + {True: "OFF", False: "ON"}[persistent.can_skip_reports] text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "can_skip_reports")
#             textbutton "Block skipping on final recap: " + {True: "OFF", False: "ON"}[persistent.can_skip_night_recap] text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "can_skip_night_recap")

#             text ""

#             label _("Misc") text_bold True

#             # Naming options for clones

#             text "\nChoose naming options for non-original girls" color c_brown italic True size res_font(16)

#             $ switch_caption = {True: "YES", False: "NO"}

#             textbutton "Keep First Name: %s" % switch_caption[persistent.keep_firstname] text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "keep_firstname")
#             textbutton "Keep Last Name: %s" % switch_caption[persistent.keep_lastname] text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "keep_lastname")
#             textbutton "Prioritize _BK.ini clone name settings (when available): %s" % switch_caption[persistent.gp_name_customization] text_size res_font(18) xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "gp_name_customization")

            # End of menu