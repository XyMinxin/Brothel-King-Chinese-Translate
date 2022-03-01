
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
                    text "In brothel: {b}{size=+4}" + str(len(MC.girls)) + "{/size}{/b} /" + str(brothel.bedrooms) size 12
                    # Count of working girls
                    text "Working today: {b}{size=+4}" + str(sum(1 for g in MC.girls if g.works_today())) + "{/size}{/b} /" + str(len(MC.girls)) size 12
                    # Count of girls in farm
                    if farm.active:
                        text "In farm: {b}{size=+4}" + str(len(farm.girls)) + "{/size}{/b} /" + str(farm.pens) size 12

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
                    textbutton "Mods" action Show("mod_menu_display", mod_menu=mod_menu) tooltip "Access options from your active mods."

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
                    textbutton "{b}Current goal{/b}\n{i}{size=-2}" + game.get_first_goal() style "invisible_no_padding" text_size 14 text_color c_brown xalign 0.5 text_align 0.5:
                        action NullAction()
                        hovered Show("goal_ttip", transition=Dissolve(0.15))
                        unhovered Hide("goal_ttip", transition=Dissolve(0.15))

################
## Home - Right menu - Display main character alert and button
################

screen right_menu_mc():

    # Display alert for level up
    if MC.skill_points > 0:

        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action("Your character is ready to level up."), SetDict(seen_alerts, "MC", True)):
            add ProportionalScale("UI/news.webp", 25, 25) xalign 1.0

            if not seen_alerts["MC"]:
                at blink

    else:
        text ""

    # Define tool tip text for hover on MC button
    $ ttip = "Access your main character, items and spells.\nYou are a level " + str(MC.level) + " " + MC.playerclass + ". You currently have "
    $ active_spells = len([1 for s in MC.active_spells if s.type!="passive"])
    $ auto_spells = len([1 for s in MC.known_spells if s.auto])

    if active_spells:
        $ ttip += str(active_spells) + " active spell" + plural(active_spells)
    else:
        $ ttip += "no active spells"

    if auto_spells:
        $ ttip += " and " + str(auto_spells) + " auto-cast spell" + plural(auto_spells) + "."
    else:
        $ ttip += "."

    textbutton "{u}C{/u}haracter":

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
        $ ttip = "One of your girls is ready to level up."
        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action(ttip), SetDict(seen_alerts, "girls", True)):
            add ProportionalScale("UI/status/levelup.webp", 25, 25) xalign 1.0
            if not seen_alerts["girls"]:
                at blink
    elif r:
        $ ttip = "One of your girls is ready to rank up."
        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action(ttip), SetDict(seen_alerts, "girls", True)):
            add ProportionalScale("UI/status/rankup.webp", 25, 25) xalign 1.0
            if not seen_alerts["girls"]:
                at blink

    else:
        text ""

    $ ttip = "Interact with the girls in your brothel.\nYou have " + str(len(MC.girls)) + " girl" + plural(len(MC.girls)) + " in your brothel (max " + str(brothel.bedrooms) + ").\n"
    $ working_girls = sum(1 for girl in MC.girls if girl.works_today())
    $ ttip += str(working_girls) + " girl" + plural(working_girls) + " will be working tonight."

    textbutton "{u}G{/u}irls":

        action Return("girls")
        tooltip ttip

################
## Home - Right menu - Display Brothel alert and button
################

screen right_menu_brothel():

    if carpenter_active and not brothel.current_building and brothel.can_build_anything():
        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action("The carpenter stands ready to build new furniture for you."), SetDict(seen_alerts, "carpenter", True)):
            add ProportionalScale("UI/carpenter.webp", 25, 25) xalign 1.0
            if not seen_alerts["carpenter"]:
                at blink

    else:
        text ""

    textbutton "{u}B{/u}rothel":

        action Return("brothel")
        tooltip "Manage your brothel and upgrade rooms.\n" + brothel.get_ASM_report(short=True)

################
## Home - Right menu - Display Farm alert and button
################

screen right_menu_farm():

    if farm.active:
        text ""
        textbutton "{u}F{/u}arm":
            action Return("farm")
            tooltip "Visit the farm and train the girls there.\nGizel currently holds " + str(len(farm.girls)) + " girl" + plural(len(farm.girls)) + " and " + str(farm.count_minions()) + " minion" + plural(farm.count_minions()) + " at the farm."


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

    textbutton "{u}V{/u}isit City":

        action Return("districts")
        tooltip "Visit the city of Zan."


################
## Home - Right menu - Display Slavemarket alert and button
################

screen right_menu_slavemarket():

    if slavemarket.updated:
        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action("New slaves are available at the market."), SetDict(seen_alerts, "slavemarket", True)):
            add ProportionalScale("UI/news.webp", 25, 25) xalign 1.0
            if not seen_alerts["slavemarket"]:
                at blink
    else:
        text ""

    textbutton "Slave {u}M{/u}arket":
        action Return("slavemarket")
        tooltip "Visit the slavemarket to find the perfect slave. Or just a cheap one.\nThe slavemarket currently has " + str(len(slavemarket.girls)) + " girl" + plural(len(slavemarket.girls)) + " for sale."

################
## Home - Right menu - Display Shop alert and button
################

screen right_menu_shop():

    if shop.updated:
        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action("New items are available."), SetDict(seen_alerts, "shop", True)):
            add ProportionalScale("UI/news.webp", 25, 25) xalign 1.0
            if not seen_alerts["shop"]:
                at blink
    else:
        text ""

    textbutton "{u}S{/u}hop":

        action Return("shop")
        tooltip "Visit the shop to buy useful items.\nThe shop currently has " + str(len(shop.items)) + " item" + plural(len(shop.items)) + " for sale."

################
## Home - Right menu - Display Postings alert and button
################

screen right_menu_postings():

    if quest_board.updated:
        button background None xalign 1.0 xmargin 0 xpadding 0 action NullAction() hovered (tt.Action("New classes and tasks are available."), SetDict(seen_alerts, "postings", True)):
            add ProportionalScale("UI/news.webp", 25, 25) xalign 1.0
            if not seen_alerts["postings"]:
                at blink
    else:
        text ""

    textbutton "{u}P{/u}ostings":

        action Return("postings")
        tooltip "Learn about available classes and quests.\n" + str(len(quest_board.quests)) + " quest" + plural(len(quest_board.quests)) + " and " + str(len(quest_board.classes)) + " class" + plural(len(quest_board.quests), "es") + " are currently available."


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

    textbutton "{u}E{/u}nd Day":

        action Return("end_day")
        tooltip "End the day and move on to the night's events."

################
## Home - Right menu - Display Advance button
################

screen right_menu_advance():

    if game.goals_reached() and game.chapter != 1:
        text ""

        textbutton "Advance":

            xalign 1.0

            at blink

            if MC.has_gold(blist[game.chapter+1].cost):
                action Return("advance")
            else:
                action Function(renpy.notify, "\nYou do not have enough gold to advance.")

            tooltip "Advance to the next game chapter, at the cost of %s gold." % '{:,}'.format(blist[game.chapter+1].cost)



init -2:
    # Make all the right menu buttons be the same size.
    style rm_button:
        size_group "rm"
