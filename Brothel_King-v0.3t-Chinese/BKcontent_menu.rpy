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
default hm_section_titles = {"content": "Content settings", "pictures": "Picture settings", "UI": "UI settings", "misc": "Other"}

# HM settings will be displayed in order for each section
default hm_settings = {
    "content" : [
            "Activate or deactivate objectionable content (won't affect story scenes).",
            HMSetting("forbidden_tags", special=True),
        ], 
        "pictures" : [
            "Choose what to do when a girlpack is missing pictures with a given tag.",
            HMSetting("use_stock_pictures_missing", captions=["Use another picture from the girl pack", "Use default pictures"], ttips=["The game will pick a picture from the same girlpack with the closest possible tag (e.g. 'service' instead of 'handjob').", "The game will pick a default picture with the proper tag."]),

            "Choose what to do when a girlpack has low picture variety on a given tag (less than %s)." % stock_picture_threshold,
            HMSetting("use_stock_pictures_low", captions=["Only use girl pack pictures", "Mix default and girl pack pictures"], ttips=["The game will use only the girlpack pictures that are in the pool, at the risk of repetition.", "The game will add some default pictures to the pool for variety."]),

            "Choose the priorities when generating pictures for advanced training.",
            HMSetting("fix_pic_balance", ["Variety over accuracy", "Accuracy over variety"], ttips=["The game will prioritize picture variety over accurate tagging.", "The game will prioritize accurate tagging over picture variety."], values=[fix_pic_balance_variety, fix_pic_balance_accuracy]),

            "Choose the behavior of group and bisexual pictures",
            HMSetting("mix_group_pictures", ["Group sex: Only use group pictures", "Mix group pictures with regular pictures"], ttips=["The game will only pick pictures featuring a group.", "The game will sometimes pick normal pictures for variety."]),
            HMSetting("mix_bis_pictures", ["Bisexual sex: Only use bisexual pictures", "Mix bisexual pictures with regular pictures"], ttips=["The game will only pick pictures featuring a group.", "The game will sometimes pick normal pictures for variety."]),

            "Choose the behavior of profile pictures outside of the 'Girls' tab.",
            HMSetting("naked_girls_in_slavemarket", ["Slavemarket: No naked pictures.", "Slavemarket: Allow naked pictures."], ttips=["The slavemarket may not display naked profile pictures.", "The slavemarket may display naked pictures."]),
            HMSetting("naked_girls_in_town", ["City: No naked pictures.", "City: Allow naked pictures."], ttips=["Free girls may not display naked profile pictures.", "Free girls may display naked pictures ('Naturist' trait)."]),

            "Allow extended tags for jobs and sex acts.",
            HMSetting("fuzzy_tagging_jobs", ["Jobs: Narrow tagging", "Jobs: Extended tagging"], ttips=["Job pictures will only look for accurate tags (e.g. 'masseuse' for masseuse).", "Job pictures will extend the search to 'close enough' tags (e.g. 'swimsuit' for masseuse)."]),
            HMSetting("fuzzy_tagging_acts", ["Sex acts: Narrow tagging", "Sex acts: Extended tagging"], ttips=["Sex pictures will only look for accurate tags (e.g. 'toy' for fetish).", "Job pictures will extend the search to 'close enough' tags (e.g. 'machine' for fetish)."]),
        ], 
        "UI" : [
            "Display 'news' notifications next the home screen's buttons.",
            HMSetting("home_screen_notifications", ["Flashing notifications", "Static notifications", "No notifications"], ttips=["Display a flashing notification until you hover the mouse over it (default).", "Display a static notification.", "Display no notification."], range=3, values=range(3)),

            "Use a scrollable screen or numbered tabs to browse the 'Girls' screen (tabs may improve performance).",
            HMSetting("girls_display_mode", ["Scroll girls", "Use tabs"], ttips=["Display girls on a signle scrollable screen (legacy mode: may decrease performance).", "Display girls with numbered tabs (may improve performance)."], range=2, values=["vp", "pages"]),

            "Display girlpack rating on girl profiles",
            HMSetting("show_girlpack_rating", ["Never", "In slavemarket", "In slavemarket/City", "Everywhere"], ttips=["Never display girlpack rating on profile.", "Display rating on profile in slavemarket only.", "Display rating on profile in slavemarket and city.", "Always display rating on profile."], values = [None, "In slavemarket", "In market and city", "Everywhere"], range=4),

            "Display optional status icons on girl portraits.",
            HMSetting("show_girl_status", special=True),

            "Display sanity with a girl's mood.",
            HMSetting("sanity_display", ["In farm only", "Everywhere"], ttips=["Sanity will only display when a girl is at the farm.", "Sanity will be displayed on the 'Mood' recap."]),

            "Choose how to edit badge settings for your girls.",
            HMSetting("badges_on_portraits", ["On profile only", "On profile and portrait"], ["Click on a badge in the girl's profile to change it.", "Click on a badge in the girl's profile or portrait to change it."]),

            "Hide events during the 'End Day' loop.",
            HMSetting("skipped_events", special=True),

            "Allow skipping during the 'End Day' loop.",
            HMSetting("can_skip_reports", ["Reports: Not skippable", "Reports: Skippable"], ttips=["Skipping matchmaking and satisfaction reports with 'Ctrl' is not possible.", "Skipping matchmaking and satisfaction reports with 'Ctrl' is possible."]),
            HMSetting("can_skip_night_recap", ["Nightly recap: Not skippable", "Nightly recap: Skippable"], ttips=["Skipping the nightly recap with 'Ctrl' is not possible.", "Skipping the nightly recap with 'Ctrl' is possible."]),

            "Choose display mode for 'End Day' events (WIP).",
            HMSetting("dark_night_UI", ["Light mode", "Dark mode"], ttips=["End day events are presented in light mode.", "End day events are presented in dark mode."]),


        ], 
        "misc" : [
            "Define naming options for non-original girls ('clones').",
            HMSetting("keep_firstname", ["Randomize first name", "Keep first name"], ttips=["First name will be randomized for non-original girls.", "First name will be remain the same as the original for non-original girls."]),
            HMSetting("keep_lastname", ["Randomize last name", "Keep last name"], ttips=["Last name will be randomized for non-original girls.", "Last name will be remain the same as the original for non-original girls."]),
            HMSetting("gp_name_customization", ["Prioritize girlpack settings", "Prioritize in-game settings"], ttips=["The girlpack's _BK.ini settings will take precedence over the settings above.", "The settings above will take precedence over the girlpack's _BK.ini settings."]),
        ]
        }

default hm_tag_captions = {"beast" : "Bestiality", "monster" : "Monsters/Tentacles", "machine" : "Machines"}

default hm_girl_status_list = [("away", "away.webp", "Away on a class or quest."), ("farm", "farm.webp", "Training/Resting at the farm."), ("rest", "rest.webp", "Resting"), ("scheduled", "scheduled.webp", "Scheduled to rest."), ("half-shift", "half.webp", "On a half-shift."), ("master bedroom", "master.webp", "Training in the Master's bedroom."), ("negative fixation", "negfix.webp", "Negative fixation discovered."), ("naked", "naked.webp", "Currently naked."), ("not naked", "not_naked.webp", "Currently not naked."), ("work&whore", "ww.webp", "Set to work and whore."), ("not work&whore", "not_ww.webp", "Not set to work and whore")]

default hm_night_events = [("Normal", "Normal events"), ("Matchmaking", "Matchmaking reports"), ("Customer", "Customer special events"), ("Level/Job/Rank up", "Level up, Job up and Rank up notifications"), ("Health/Security", "Health and security events"), ("Satisfaction", "Customer satisfaction report"), ("Farm", "Farm events"), ("Rest", "Resting events")]

#### Game Settings Screen ####

screen hm_forbidden_tags():
    hbox:
        for _tag in ("beast", "monster", "machine"):
            if _tag in persistent.forbidden_tags:
                $ text1 = ": OFF"
            else:
                $ text1 = ": ON"
            
            textbutton _(hm_tag_captions[_tag] + text1):
                style "hm_button2"
                size_group "forbidden_tags"
                xpadding xres(18)
                xsize xres(190)

                if _tag in persistent.forbidden_tags:
                    action (RemoveFromSet(persistent.forbidden_tags, _tag), SelectedIf(False))
                    tooltip "The game will attempt not to display such pictures (Warning: This may not be 100% successful and doesn't change story events that use these fetishes.)"
                else:
                    action (AddToSet(persistent.forbidden_tags, _tag), SelectedIf(True))
                    tooltip "The game will display such pictures."

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
            textbutton _(ev_type) style "hm_button2" text_size res_font(16) xalign 0.0 action (ToggleDict(persistent.skipped_events, ev_type), SelectedIf(not persistent.skipped_events[ev_type])) tooltip ttip + {False: " will be shown.", True: " will be hidden."}[persistent.skipped_events[ev_type]]


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