
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
                    text __("在青楼里的女孩有: {b}{size=+4}") + str(len(MC.girls)) + "{/size}{/b} /" + str(brothel.bedrooms) size res_font(12)
                    # Count of working girls
                    text __("今晚工作的女孩有: {b}{size=+4}") + str(sum(1 for g in MC.girls if g.works_today())) + "{/size}{/b} /" + str(len(MC.girls)) size res_font(12)
                    # Count of girls in farm
                    if farm.active:
                        text __("在农场里有: {b}{size=+4}") + str(len(farm.girls)) + "{/size}{/b} /" + str(farm.pens) size res_font(12)

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
                xanchor 1.0

                # Main character alert and button

                use right_menu_mc

                null height 20

                # Girls Alert and Button

                use right_menu_girls

                # Brothel Alert and Button

                use right_menu_brothel

                # Farm button

                use right_menu_farm

                # City Alert and Button

                use right_menu_city

                null height 20

                # Slavemarket Alert and Button

                use right_menu_slavemarket

                # Shop Alert and Button

                use right_menu_shop

                # Postings Alert and Button

                use right_menu_postings

                # Mods custom button display

                if mod_menu:
                    null height 20
                    textbutton "Mods" action Show("mod_menu_display", mod_menu=mod_menu) tooltip "Access options from your active mods."

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
                textbutton __("{b}当前目标{/b}\n{i}{size=-2}") + game.get_first_goal() style "invisible_no_padding" text_size res_font(14) text_color c_brown xalign 0.5 text_align 0.5:
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

            button style "rm_alert" action NullAction() tooltip "你的角色可以升级了." hovered SetDict(seen_alerts, "MC", True):
                add ProportionalScale("UI/news.webp", *res_tb(25)) xalign 1.0

                if not seen_alerts["MC"] and persistent.home_screen_notifications == 0:
                    at blink

        else:
            text ""

        # Define tool tip text for hover on MC button
        $ ttip = __("查看你的状态、装备的道具和已掌握的能力。\n你是一位 {color=[c_steel]}{b}等级 [MC.level]的 [MC.playerclass]{/b}{/color}") + __(". 你目前激活了 ")
        #$ ttip = __("Access your main character, items and spells.\nYou are a level ") + str(MC.level) + " " + __(MC.playerclass) + __(". You currently have ")
        $ active_spells = len([1 for s in MC.active_spells if s.type!="passive"])
        $ auto_spells = len([1 for s in MC.known_spells if s.auto])

        if active_spells:
            $ ttip += str(active_spells) + __(" 可用法术") + plural(active_spells)
        else:
            $ ttip += __("不可用法术")

        if auto_spells:
            $ ttip += __(" 和 ") + str(auto_spells) + __(" 自动施放的法术") + plural(auto_spells) + "."
        else:
            $ ttip += "."

        textbutton "{u}C{/u}角色状态" style_group "rm":
            ypadding 0.005
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

                if girl.perk_points or girl.can_spend_upgrade_points():
                    b = True
                    break

                if girl.ready_to_rank():
                    r = True
                    break

    hbox xalign 1.0 spacing 20:

        if b:
            $ ttip = "你有员工可以 {color=[c_yellow]}{b}升级{/b}{/color}."
            button style "rm_alert" action NullAction() tooltip ttip hovered (SetDict(seen_alerts, "girls", True)):
                add ProportionalScale("UI/status/levelup.webp", *res_tb(25)) xalign 1.0
                if not seen_alerts["girls"] and persistent.home_screen_notifications == 0:
                    at blink
        elif r:
            $ ttip = "你有员工可以 {color=[c_yellow]}{b}提升阶级.{/b}{/color}"
            button style "rm_alert" action NullAction() tooltip ttip hovered (SetDict(seen_alerts, "girls", True)):
                add ProportionalScale("UI/status/rankup.webp", *res_tb(25)) xalign 1.0
                if not seen_alerts["girls"] and persistent.home_screen_notifications == 0:
                    at blink

        else:
            text ""

        $ ttip = __("检查青楼里姑娘们的状态，和她们培养感情.\n你有 {color=[c_hotpink]}{b}") + str(len(MC.girls)) + __(" 个女孩{/b}{/color}在青楼 (最多 ") + str(brothel.bedrooms) + ").\n"
        $ working_girls = sum(1 for girl in MC.girls if girl.works_today())
        $ ttip += __("今晚有 ") + str(working_girls) + __(" 个女孩要工作.")

        textbutton "{u}女孩{/u}" style_group "rm":
            ypadding 0.005
            text_size res_font(20)

            action Return("girls")
            tooltip ttip

################
## Home - Right menu - Display Brothel alert and button
################

screen right_menu_brothel():

    hbox xalign 1.0 spacing 20:

        if NPC_carpenter.active and not brothel.current_building and brothel.can_build_anything() and persistent.home_screen_notifications != 2:
            button style "rm_alert" action NullAction() hovered (tt.Action("工匠已经准备好帮你升级设施了."), SetDict(seen_alerts, "carpenter", True)):
                add ProportionalScale("UI/carpenter.webp", *res_tb(25)) xalign 1.0
                if not seen_alerts["carpenter"] and persistent.home_screen_notifications == 0:
                    at blink

        else:
            text ""

        textbutton "{u}青楼{/u}" style_group "rm":
            ypadding 0.005
            text_size res_font(20)

            action Return("brothel")
            tooltip __(brothel.get_ASM_report(short=True))

################
## Home - Right menu - Display Farm alert and button
################

screen right_menu_farm():

    if farm.active:
        hbox xalign 1.0 spacing 20:
            text ""
            textbutton "{u}农场{/u}" style_group "rm":
                ypadding 0.005
                text_size res_font(20)
                action Return("farm")
                tooltip "前往奴隶农场，在那里训练你的女孩. 吉泽管理着 {color=[c_hotpink]}{b}" + str(len(farm.girls)) + " 个女孩{/b}{/color}和 {color=[c_softpurple]}{b}" + str(farm.count_minions()) + " 个仆从{/b}{/color}."


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

        textbutton "{u}访问城市{/u}" style_group "rm":
            ypadding 0.005
            text_size res_font(20)

            action Return("districts")
            tooltip "探索其他地区获得{b}资源{/b}，或是和美丽的{b}陌生姑娘{/b}搭讪来一次一夜情。"


################
## Home - Right menu - Display Slavemarket alert and button
################

screen right_menu_slavemarket():

    hbox xalign 1.0 spacing 20:
        if slavemarket.updated and persistent.home_screen_notifications != 2:
            button style "rm_alert" action NullAction() hovered SetDict(seen_alerts, "slavemarket", True):
                tooltip __("新的奴隶可以在市场上买到.")
                add ProportionalScale("UI/news.webp", *res_tb(25)) xalign 1.0
                if not seen_alerts["slavemarket"] and persistent.home_screen_notifications == 0:
                    at blink
        else:
            text ""

        textbutton "{u}奴隶市场{/u}" style_group "rm":
            ypadding 0.005
            if screen_is_wide:
                text_size res_font(20)
            else:
                text_size res_font(18)
            action Return("slavemarket")
            tooltip __("前往{b}奴隶市场{/b}. 无论是亡国公主，落魄千金，兽耳娘，清纯少女还是精液中毒的肉便器总有一款适合你。 目前有 {color=[c_hotpink]}{b}") + str(len(slavemarket.girls)) + __(" 个奴隶{/b}{/color}待售.")

################
## Home - Right menu - Display Shop alert and button
################

screen right_menu_shop():

    hbox xalign 1.0 spacing 20:
        if shop.updated and persistent.home_screen_notifications != 2:
            button style "rm_alert" action NullAction() hovered SetDict(seen_alerts, "shop", True):
                tooltip __("有新商品可以买.")
                add ProportionalScale("UI/news.webp", *res_tb(25)) xalign 1.0
                if not seen_alerts["shop"] and persistent.home_screen_notifications == 0:
                    at blink
        else:
            text ""

        textbutton "{u}商店{/u}" style_group "rm":
            ypadding 0.005
            text_size res_font(20)

            action Return("shop")
            tooltip __("逛逛{b}商店{/b}淘些好货，情趣内衣，武器护甲应有尽有.\n商店目前有 {color=[c_yellow]}{b}") + str(len(shop.items)) + __("件商品{/b}{/color}待售.")

################
## Home - Right menu - Display Postings alert and button
################

screen right_menu_postings():

    hbox xalign 1.0 spacing 20:
        if quest_board.updated and persistent.home_screen_notifications != 2:
            button style "rm_alert" action NullAction() tooltip "有新的任务和课程发布." hovered SetDict(seen_alerts, "postings", True):
                add ProportionalScale("UI/news.webp", *res_tb(25)) xalign 1.0
                if not seen_alerts["postings"] and persistent.home_screen_notifications == 0:
                    at blink
        else:
            text ""

        textbutton "{u}外派{/u}" style_group "rm":
            ypadding 0.005
            text_size res_font(20)

            action Return("postings")
            tooltip __("女孩们可以贴身服务他人，也可以接受他人的贴身指导.\n{color=[c_orange_pink]}{b}") + str(len(quest_board.classes)) + __(" 个培训班") + __("{/b}{/color} 和 {color=[c_orange_pink]}{b}") + str(len(quest_board.quests)) + __(" 个合同") + plural(len(quest_board.quests)) + __("{/b}{/color} 目前可用的.")


################
## Home - Right menu - Mod menu button and display
################

screen mod_menu_display(mod_menu):

    modal True

    key "mouseup_3" action Hide("mod_menu_display")

    frame background c_ui_dark xmaximum (config.screen_width - 220) ymaximum 0.7 xanchor 1.0 xalign 0.8 yanchor 1.0 yalign 0.7:
        has vbox box_wrap True ymaximum 0.7
        for mod in mod_menu:
            frame:
                has vbox box_wrap True
                text mod.name size res_font(14) bold True color c_prune
                for but in mod.home_rightmenu_add_buttons:
                    use expression but
        null
        textbutton "X" action Hide("mod_menu_display")


################
## Home - Right menu - Display End day button
################

screen right_menu_endday():

    hbox xalign 1.0 spacing 20:
        text ""

        textbutton "{u}E{/u}开始营业" style_group "rm":
            ypadding 0.005
            text_size res_font(20)

            action Return("end_day")
            tooltip "点击此按钮 {b}开始营业{/b} ，结束这一天."

################
## Home - Right menu - Display Advance button
################

screen right_menu_advance():

    if game.goals_reached():
        if game.chapter != 1 or not story_mode or debug_mode:
            hbox xalign 1.0 spacing 20:
                text ""

                textbutton "进入下一章" text_size res_font(20) style_group "rm":

                    xalign 1.0

                    at blink

                    if MC.has_gold(blist[game.chapter+1].cost):
                        action Return("advance")
                    else:
                        action Function(renpy.notify, "你没有足够的金币进入下一章.")

                    tooltip __("花费 %s 金币,进入到下一章.") % '{:,}'.format(blist[game.chapter+1].cost)



init -2:
    # Make all the right menu buttons be the same size.
    if screen_is_wide:
        style rm_button:
            size_group "rm"
            xsize xres(115)
    else:
        style rm_button:
            size_group "rm"

    style rm_alert:
        background None xalign 1.0 xmargin 0 xpadding 0 yalign 0.5
