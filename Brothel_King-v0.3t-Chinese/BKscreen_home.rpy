
########################
## Home - Right main menu
########################

screen right_menu():

    # Right click action
    key "mouseup_3" action (ShowMenu('save'), Hide("brothel_report"), Hide("previous_night_log"))

    # Set box for right menu
    vbox ypos 0.1 xalign 1.0 xfill False spacing 20:

        # Girls activities / information top box
        frame background c_ui_dark xalign 1.0 xmargin 6:
            if screen_is_wide:
                xsize 0.125
            else:
                xsize 0.2

            hbox:
                xalign 0.5
                add "girl_shadow"

                vbox spacing 6:
                    # Count of girls in Brothel
                    text __("In brothel: {b}{size=+4}") + str(len(MC.girls)) + "{/size}{/b} /" + str(brothel.bedrooms) size res_font(12)
                    # Count of working girls
                    text __("Working today: {b}{size=+4}") + str(sum(1 for g in MC.girls if g.works_today())) + "{/size}{/b} /" + str(len(MC.girls)) size res_font(12)
                    # Count of girls in farm
                    if farm.active:
                        text __("In farm: {b}{size=+4}") + str(len(farm.girls)) + "{/size}{/b} /" + str(farm.pens) size res_font(12)

        # Right menu frame

        frame:
            background c_ui_dark
            xalign 1.0
            if screen_is_wide:
                xsize 0.125
            else:
                xsize 0.2
            xmargin 6
            xpadding 9

            # Define number of rows based on actions button available on right menu

            $ rows = 11

            # Start by checking if any mods add their own home button

            python:

                mod_menu = []

                for mod in game.active_mods.values():
                    if mod.home_rightmenu_add_buttons and isinstance(mod.home_rightmenu_add_buttons, list):
                        mod_menu.append(mod)

            if farm.active:
                $ rows += 1
            if mod_menu:
                $ rows += 1
            if game.goals_reached() and (game.chapter != 1 or not story_mode or debug_mode):
                $ rows += 1


            # Generate a grid of 2 columns and x rows for the right menu

            vbox:
                spacing 6
                xalign 1.0

                # Main character alert and button

                use right_menu_mc

                null height 20

                # Girls Alert and Button

                use right_menu_girls

                # Brothel Alert and Button

                use right_menu_brothel

                # Farm button

                if farm.active:
                    use right_menu_farm

                # City Alert and Button

                use right_menu_city

                null height 20

                # Slavemarket Alert and Button

                if slavemarket.active:
                    use right_menu_slavemarket

                # Shop Alert and Button

                use right_menu_shop

                # Postings Alert and Button

                use right_menu_postings

                # Mods custom button display

                if mod_menu:
                    null height 20
                    textbutton "模组" action Show("mod_menu_display", mod_menu=mod_menu) tooltip "Access options from your active mods (%s)." % and_text([event_color["special"] % m.name for m in game.active_mods.values()])  text_size res_font(20) style_group "rm" xalign 1.0

                null height 20

                # End day Button

                use right_menu_endday

                # Advance Button

                use right_menu_advance

        # Goals Reached box

        if not game.goals_reached() or (story_mode and not debug_mode and game.chapter == 1):
            frame background Frame("UI/scroll.webp", left=10, right=10, top=15, bottom=15) xalign 1.0 xpadding xres(20) ypadding yres(30) xmargin xres(10):
                if screen_is_wide:
                    xsize 0.125
                else:
                    xsize 0.2
                textbutton "{b}当前目标{/b}\n{i}{size=-2}" + game.get_first_goal() style "invisible_no_padding" text_size res_font(14) text_color c_brown xalign 0.5 text_align 0.5:
                    action NullAction()
                    hovered Show("goal_ttip", transition=Dissolve(0.15))
                    unhovered Hide("goal_ttip", transition=Dissolve(0.15))

################
## Home - Right menu - Display main character alert and button
################

screen right_menu_mc():

    hbox xalign 1.0 spacing 20:
        # Display alert for level up
        if MC.skill_points > 0 and persistent.home_screen_notifications != 2:

            button style "rm_alert" action NullAction() tooltip __("Your character is ready to level up.") hovered SetDict(seen_alerts, "MC", True):
                add ProportionalScale("UI/news.webp", *res_tb(25)) xalign 1.0

                if not seen_alerts["MC"] and persistent.home_screen_notifications == 0:
                    at blink

        else:
            text ""

        # Define tool tip text for hover on MC button
        $ ttip = __("Access your main character, items and spells.\nYou are a {color=[c_main]}{b}Level [MC.level] [MC.playerclass]{/b}{/color}") + __(". You currently have ")
        #$ ttip = __("Access your main character, items and spells.\nYou are a level ") + str(MC.level) + " " + __(MC.playerclass) + __(". You currently have ")
        $ active_spells = len([1 for s in MC.active_spells if s.type!="passive"])
        $ auto_spells = len([1 for s in MC.known_spells if s.auto])

        if active_spells:
            $ ttip += str(active_spells) + __(" active spell") + plural(active_spells)
        else:
            $ ttip += __("no active spells")

        if auto_spells:
            $ ttip += __(" and ") + str(auto_spells) + __(" auto-cast spell") + plural(auto_spells) + "."
        else:
            $ ttip += "."

        textbutton "主角状态" style_group "rm":
            text_size res_font(20)

            action Return("main_character")
            tooltip ttip


################
## Home - Right menu - Display Girls alert and button
################

screen right_menu_girls():
    python:

        b = False
        r = False

        if persistent.home_screen_notifications != 2:
            for girl in MC.girls:

                if girl.can_perk or girl.can_spend_upgrade_points():
                    b = True
                    break

                if girl.ready_to_rank():
                    r = True
                    break

    hbox xalign 1.0 spacing 20:

        if b:
            $ ttip = _("One of your girls is ready to {color=[c_yellow]}{b}level up{/b}{/color}.")
            button style "rm_alert" action NullAction() tooltip ttip hovered (SetDict(seen_alerts, "girls", True)):
                add ProportionalScale("UI/status/levelup.webp", *res_tb(25)) xalign 1.0
                if not seen_alerts["girls"] and persistent.home_screen_notifications == 0:
                    at blink
        elif r:
            $ ttip = _("One of your girls is ready to {color=[c_yellow]}{b}rank up.{/b}{/color}")
            button style "rm_alert" action NullAction() tooltip ttip hovered (SetDict(seen_alerts, "girls", True)):
                add ProportionalScale("UI/status/rankup.webp", *res_tb(25)) xalign 1.0
                if not seen_alerts["girls"] and persistent.home_screen_notifications == 0:
                    at blink

        else:
            text ""

        $ ttip = __("Interact with the girls in your brothel.\nYou have {color=[c_hotpink]}{b}") + str(len(MC.girls)) + __(" girl") + plural(len(MC.girls)) + __("{/b}{/color} in your brothel (max ") + str(brothel.bedrooms) + ").\n"
        $ working_girls = sum(1 for girl in MC.girls if girl.works_today())
        $ ttip += str(working_girls) + __(" girl") + plural(working_girls) + __(" will be working tonight.")

        textbutton "青楼宿舍" style_group "rm":
            text_size res_font(20)

            action Return("girls")
            tooltip ttip

################
## Home - Right menu - Display Brothel alert and button
################

screen right_menu_brothel():

    hbox xalign 1.0 spacing 20:

        if NPC_carpenter.active and not brothel.current_building and brothel.can_build_anything() and persistent.home_screen_notifications != 2:
            button style "rm_alert" action NullAction() tooltip __("The carpenter stands ready to build new furniture for you.") hovered (SetDict(seen_alerts, "carpenter", True)):
                add ProportionalScale("UI/carpenter.webp", *res_tb(25)) xalign 1.0
                if not seen_alerts["carpenter"] and persistent.home_screen_notifications == 0:
                    at blink

        else:
            text ""

        textbutton "青楼设置" style_group "rm":
            action Return("brothel")
            tooltip __(brothel.get_ASM_report(short=True))

################
## Home - Right menu - Display Farm alert and button
################

screen right_menu_farm():
    hbox xalign 1.0 spacing 20:
        text ""
        textbutton "奴隶农场" style_group "rm":
            action Return("farm")
            tooltip __("Visit the farm and train the girls there. Gizel currently holds {color=[c_hotpink]}{b}") + str(len(farm.girls)) + "个女孩" + plural(len(farm.girls)) + "{/b}{/color}和{color=[c_softpurple]}{b}" + str(farm.count_minions()) + "个仆从" + plural(farm.count_minions()) + "{/b}{/color}。"


################
## Home - Right menu - Display City alert and button
################

screen right_menu_city():

#     if game.token > 0:
#         button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action("You are ready to move your brothel to a new district."), SetDict(seen_alerts, "district", True)):
#             add ProportionalScale("UI/news.webp", *res_tb(25)) xalign 1.0
#             if not seen_alerts["district"]:
#                 at blink
#     else:
    hbox xalign 1.0 spacing 20:
        text ""

        textbutton "探索城市" style_group "rm":
            action Return("districts")
            tooltip "探索泽恩的各个地区，与美丽的单身女性邂逅"


################
## Home - Right menu - Display Slavemarket alert and button
################

screen right_menu_slavemarket():

    hbox xalign 1.0 spacing 20:
        if slavemarket.updated and persistent.home_screen_notifications != 2:
            button style "rm_alert" action NullAction() hovered SetDict(seen_alerts, "slavemarket", True):
                tooltip __("New slaves are available at the market.")
                add ProportionalScale("UI/news.webp", *res_tb(25)) xalign 1.0
                if not seen_alerts["slavemarket"] and persistent.home_screen_notifications == 0:
                    at blink
        else:
            text ""

        textbutton "奴隶市场" style_group "rm":
            if screen_is_wide:
                text_size res_font(20)
            else:
                text_size res_font(18)
            action Return("slavemarket")
            tooltip __("Visit the {b}slavemarket{/b} to find the perfect slave. Or just a cheap one. The slavemarket currently has {color=[c_hotpink]}{b}") + str(len(slavemarket.girls)) + __(" girl") + plural(len(slavemarket.girls)) + __("{/b}{/color} for sale.")

################
## Home - Right menu - Display Shop alert and button
################

screen right_menu_shop():

    hbox xalign 1.0 spacing 20:
        if shop.updated and persistent.home_screen_notifications != 2:
            button style "rm_alert" action NullAction() hovered SetDict(seen_alerts, "shop", True):
                tooltip __("New items are available.")
                add ProportionalScale("UI/news.webp", *res_tb(25)) xalign 1.0
                if not seen_alerts["shop"] and persistent.home_screen_notifications == 0:
                    at blink
        else:
            text ""

        textbutton "杂货商店" style_group "rm":
            action Return("shop")
            tooltip __("Visit the {b}shop{/b} to buy useful items.\nThe shop currently has {color=[c_yellow]}{b}") + str(len(shop.items)) + __(" item") + plural(len(shop.items)) + __("{/b}{/color} for sale.")

################
## Home - Right menu - Display Postings alert and button
################

screen right_menu_postings():

    hbox xalign 1.0 spacing 20:
        if quest_board.updated and persistent.home_screen_notifications != 2:
            button style "rm_alert" action NullAction() tooltip __("New classes and tasks are available.") hovered SetDict(seen_alerts, "postings", True):
                add ProportionalScale("UI/news.webp", *res_tb(25)) xalign 1.0
                if not seen_alerts["postings"] and persistent.home_screen_notifications == 0:
                    at blink
        else:
            text ""

        textbutton "公告大厅" style_group "rm":
            action Return("postings")
            tooltip __("See available classes and quests.\n{color=[c_orange_pink]}{b}") + str(len(quest_board.classes)) + __(" class") + plural(len(quest_board.quests), __("es")) + __("{/b}{/color} and {color=[c_orange_pink]}{b}") + str(len(quest_board.quests)) + __(" quest") + plural(len(quest_board.quests)) + __("{/b}{/color} are currently available.")


################
## Home - Right menu - Mod menu button and display
################

screen mod_menu_display(mod_menu):

    modal True

    key "mouseup_3" action Hide("mod_menu_display")

    frame background c_ui_dark xmaximum 0.3 ymaximum 0.7 xanchor 1.0 xpos 0.8 yanchor 1.0 ypos 0.8:
        has vbox box_wrap True
        for _mod in mod_menu:
            vbox box_wrap True:
                text _mod.name size res_font(14) bold True color c_gold
                for _but in _mod.home_rightmenu_add_buttons:
                    use expression _but
        # null
        # textbutton "X" action Hide("mod_menu_display")


################
## Home - Right menu - Display End day button
################

screen right_menu_endday():

    hbox xalign 1.0 spacing 20:
        text ""

        textbutton "开始营业" style_group "rm":
            action Return("end_day")
            tooltip "点击这个按钮进入深夜，开始营业"

################
## Home - Right menu - Display Advance button
################

screen right_menu_advance():

    if game.goals_reached():
        if game.chapter != 1 or not story_mode or debug_mode:
            hbox xalign 1.0 spacing 20:
                text ""

                textbutton "推进剧情" text_size res_font(20) style_group "rm":

                    xalign 1.0

                    at blink

                    if MC.has_gold(blist[game.chapter+1].cost):
                        action Return("advance")
                    else:
                        action Function(renpy.notify, _("You do not have enough gold to advance."))

                    tooltip __("Advance to the next game chapter, at the cost of %s gold.") % '{:,}'.format(blist[game.chapter+1].cost)



init -2:
    # Make all the right menu buttons be the same size.
    if screen_is_wide:
        style rm_button:
            size_group "rm"
            xsize xres(115)
            ypadding 0.005
    else:
        style rm_button:
            size_group "rm"
            ypadding 0.005

    style rm_button_text:
        size res_font(20)

    style rm_alert:
        background None xalign 1.0 xmargin 0 xpadding 0 yalign 0.5
