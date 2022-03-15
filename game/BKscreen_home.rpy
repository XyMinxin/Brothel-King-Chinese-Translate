
########################
## Home - Right main menu
########################

screen right_menu():
    # <Chris12 PredictImages - Predict just the portraits.
    # Profiles are not needed immediately on entering the girls screen. />
    $ predict_images(MC.girls + slavemarket.girls, predict_profiles = False)

    # Right click action
    key "mouseup_3" action (ShowMenu('save'), Hide("brothel_report"), Hide("previous_night_log"))

    # Set box for right menu
    vbox ypos 0.1 xalign 1.0 xfill False spacing 20:

        # Girls activities / information top box
        frame background c_ui_dark xalign 1.0 xmargin 6 xsize 204:

            hbox:
                add "girl_shadow"

                vbox spacing 6:
                    # Count of girls in Brothel
                    text "拥有女孩: {b}{size=+4}" + str(len(MC.girls)) + "{/size}{/b} /" + str(brothel.bedrooms) size 12
                    # Count of working girls
                    text "今天工作: {b}{size=+4}" + str(sum(1 for g in MC.girls if g.works_today())) + "{/size}{/b} /" + str(len(MC.girls)) size 12
                    # Count of girls in farm
                    if farm.active:
                        text "在农场里: {b}{size=+4}" + str(len(farm.girls)) + "{/size}{/b} /" + str(farm.pens) size 12

        # Right menu frame

        frame:
            background c_ui_dark

            xsize 204
            xmargin 6
            xpadding 9

            style_group "rm"

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
            if game.goals_reached() and game.chapter != 1:
                $ rows += 1


            # Generate a grid of 2 columns and x rows for the right menu

            grid 2 rows:
                xspacing 20
                yspacing 6
                xalign 1.0
                xanchor 1.0

                # Main character alert and button

                use right_menu_mc

                null
                null

                # Girls Alert and Button

                use right_menu_girls

                # Brothel Alert and Button

                use right_menu_brothel

                # Farm button

                use right_menu_farm

                # City Alert and Button

                use right_menu_city

                null
                null

                # Slavemarket Alert and Button

                use right_menu_slavemarket

                # Shop Alert and Button

                use right_menu_shop

                # Postings Alert and Button

                use right_menu_postings

                # Mods custom button display

                if mod_menu:
                    null
                    textbutton "Mods" action Show("mod_menu_display", mod_menu=mod_menu) tooltip "从你的激活的MOD中获取选项."

                null
                null

                # End day Button

                use right_menu_endday

                # Advance Button

                use right_menu_advance

        # Goals Reached box

        if not game.goals_reached() or game.chapter == 1:
            frame:
                background c_ui_dark

                xsize 204
                xmargin 6

                frame background Frame("UI/scroll.webp") xalign 0.5 xsize 180 xpadding 20 ypadding 10:
                    textbutton "{b}当前目标{/b}\n{i}{size=-2}" + game.get_first_goal() style "invisible_no_padding" text_size 14 text_color c_brown xalign 0.5 text_align 0.5:
                        action NullAction()
                        hovered Show("goal_ttip", transition=Dissolve(0.15))
                        unhovered Hide("goal_ttip", transition=Dissolve(0.15))

################
## Home - Right menu - Display main character alert and button
################

screen right_menu_mc():

    # Display alert for level up
    if MC.skill_points > 0:

        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action("你的角色已经准备好升级了."), SetDict(seen_alerts, "MC", True)):
            add ProportionalScale("UI/news.webp", 25, 25) xalign 1.0

            if not seen_alerts["MC"]:
                at blink

    else:
        text ""

    # Define tool tip text for hover on MC button
    $ ttip = "查看你的角色、物品和法术.\n你等级是" + str(MC.level) + " " + MC.playerclass + ". 你目前"
    $ active_spells = len([1 for s in MC.active_spells if s.type!="passive"])
    $ auto_spells = len([1 for s in MC.known_spells if s.auto])

    if active_spells:
        $ ttip += "有 " + str(active_spells) + " 个激活的法术"
    else:
        $ ttip += "没有激活的法术"

    if auto_spells:
        $ ttip += "和 " + str(auto_spells) + " 个自动施法的法术."
    else:
        $ ttip += "."

    textbutton "角色":

        action Return("main_character")
        tooltip ttip


################
## Home - Right menu - Display Girls alert and button
################

screen right_menu_girls():
    python:

        b = False
        r = False

        for girl in MC.girls:

            if girl.upgrade_points >= 1:
                b = True
                break

            if girl.ready_to_rank():
                r = True
                break

    if b:
        $ ttip = "你的一个女孩已经准备好升级了."
        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action(ttip), SetDict(seen_alerts, "girls", True)):
            add ProportionalScale("UI/status/levelup.webp", 25, 25) xalign 1.0
            if not seen_alerts["girls"]:
                at blink
    elif r:
        $ ttip = "你的一个女孩已经准备好升阶了."
        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action(ttip), SetDict(seen_alerts, "girls", True)):
            add ProportionalScale("UI/status/rankup.webp", 25, 25) xalign 1.0
            if not seen_alerts["girls"]:
                at blink

    else:
        text ""

    $ ttip = "与你青楼中的女孩互动.\n你有 " + str(len(MC.girls)) + " 个女孩在青楼 (max " + str(brothel.bedrooms) + ").\n"
    $ working_girls = sum(1 for girl in MC.girls if girl.works_today())
    $ ttip += "今晚有 " + str(working_girls) + " 个女孩要工作."

    textbutton "女孩":

        action Return("girls")
        tooltip ttip

################
## Home - Right menu - Display Brothel alert and button
################

screen right_menu_brothel():

    if carpenter_active and not brothel.current_building and brothel.can_build_anything():
        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action("木匠随时准备为你打造新的家具."), SetDict(seen_alerts, "carpenter", True)):
            add ProportionalScale("UI/carpenter.webp", 25, 25) xalign 1.0
            if not seen_alerts["carpenter"]:
                at blink

    else:
        text ""

    textbutton "青楼":

        action Return("brothel")
        tooltip "管理你的青楼和升级房间.\n" + brothel.get_ASM_report(short=True)

################
## Home - Right menu - Display Farm alert and button
################

screen right_menu_farm():

    if farm.active:
        text ""
        textbutton "农场":
            action Return("farm")
            tooltip "参观农场并训练那里的女孩.\nGizel农场目前有 " + str(len(farm.girls)) + " 个女孩和 " + str(farm.count_minions()) + " 个仆从."


################
## Home - Right menu - Display City alert and button
################

screen right_menu_city():

#     if game.token > 0:
#         button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action("You are ready to move your brothel to a new district."), SetDict(seen_alerts, "district", True)):
#             add ProportionalScale("UI/news.webp", 25, 25) xalign 1.0
#             if not seen_alerts["district"]:
#                 at blink
#     else:
    text ""

    textbutton "访问城市":

        action Return("districts")
        tooltip "访问Zan."


################
## Home - Right menu - Display Slavemarket alert and button
################

screen right_menu_slavemarket():

    if slavemarket.updated:
        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action("市场上有新的奴隶."), SetDict(seen_alerts, "slavemarket", True)):
            add ProportionalScale("UI/news.webp", 25, 25) xalign 1.0
            if not seen_alerts["slavemarket"]:
                at blink
    else:
        text ""

    textbutton "奴隶市场":
        action Return("slavemarket")
        tooltip "访问奴隶市场，寻找完美的奴隶. 或者是一个便宜货.\n奴隶市场目前有 " + str(len(slavemarket.girls)) + " 个女孩在出售."

################
## Home - Right menu - Display Shop alert and button
################

screen right_menu_shop():

    if shop.updated:
        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action("有新的物品推出."), SetDict(seen_alerts, "shop", True)):
            add ProportionalScale("UI/news.webp", 25, 25) xalign 1.0
            if not seen_alerts["shop"]:
                at blink
    else:
        text ""

    textbutton "商店":

        action Return("shop")
        tooltip "访问商店购买有用的物品.\n商店目前有 " + str(len(shop.items)) + " 个物品在出售."

################
## Home - Right menu - Display Postings alert and button
################

screen right_menu_postings():

    if quest_board.updated:
        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action("有新的课程和任务."), SetDict(seen_alerts, "postings", True)):
            add ProportionalScale("UI/news.webp", 25, 25) xalign 1.0
            if not seen_alerts["postings"]:
                at blink
    else:
        text ""

    textbutton "外派":

        action Return("postings")
        tooltip "了解现有课程和任务的情况.\n目前有" + str(len(quest_board.quests)) + " 个任务和 " + str(len(quest_board.classes)) + " 个课程."


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
                text mod.name size 14 bold True color c_prune
                for but in mod.home_rightmenu_add_buttons:
                    use expression but
        null
        textbutton "X" action Hide("mod_menu_display")


################
## Home - Right menu - Display End day button
################

screen right_menu_endday():

    text ""

    textbutton "结束一天":

        action Return("end_day")
        tooltip "结束一天的工作，转入晚上的活动."

################
## Home - Right menu - Display Advance button
################

screen right_menu_advance():

    if game.goals_reached() and game.chapter != 1:
        text ""

        textbutton "进展":

            xalign 1.0

            at blink

            if MC.has_gold(blist[game.chapter+1].cost):
                action Return("advance")
            else:
                action Function(renpy.notify, "\n你没有足够的金币来升级.")

            tooltip "推进到下一个游戏章节，需要 %s 金币." % '{:,}'.format(blist[game.chapter+1].cost)



init -2:
    # Make all the right menu buttons be the same size.
    style rm_button:
        xsize 175
