# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what, side_image=False):
    style_prefix "say"
    zorder 5

    # The one window variant.
    window yalign 1.0 ysize res_portrait_size xpadding xres(6) ypadding yres(6) left_margin xres(10):
        id "window"

        has vbox:
            style "say_vbox"

        if who:
            text who id "who" # bold True

        text what id "what"

    # If there's a side image, display it above the text.

    if side_image: # This is for Girl.char objects
        fixed xsize res_portrait_size ysize res_portrait_size xalign 0.0 yalign 1.0:
            add side_image xalign 0.5 yalign 1.0

    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu

style window is default

style window:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize res_portrait_size

    #background Image("gui/textbox.png", xalign=0.0, yalign=0.0, yfill=True)
    background Frame("gui/textbox.png", left=0, top=0, right=0, bottom=0, tile=False)


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    modal True
    zorder 5

    ## This is an addition to the default menu in order to display the personality summary

    if choice_menu_girl_interact:
        use personality_screen

    window:
        style "menu_window"

        if choice_menu_girl_interact:
            yalign 0.5
            yanchor 0.0
        else:
            yalign 0.5

        xalign 0.5

        vbox:
            style "menu"
            spacing yres(2)

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear
        size res_font(22)

    style menu_choice_button is button:
        xminimum 0.75 # int(config.screen_width * 0.75)
        xmaximum 0.75 # int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

## This awesome input screen was made by OhWee

screen input(prompt):

    modal True

    frame xalign 0.5 yalign 0.5 xsize yres(420) ysize yres(290):
        background Frame("UI/Sill_Textbox.webp")
        has vbox xfill True

        text prompt style "input_prompt" xalign 0.5:
            if count_lines(prompt, 46) <= 2:
                size res_font(19)
            elif count_lines(prompt, 50) <= 3:
                size res_font(15)
            else:
                size res_font(13)

        input id "input" style "input_text" xsize 0.5 xpos 0.5 ypos yres(30) copypaste True
    #
    # use quick_menu

init:
    style input_prompt is default:
        xpos 100
        ypos 6
        xalign 0.0
        size res_font(19)
        color "#521"

    style input_text is default:
        # xanchor 0.0
        # yanchor 0.0
        size res_font(18)
        color "#931"
        background "UI/messagescroll_small.webp"

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # on "show" action Function(update_mods)

    # The background of the main menu.
    window:
        style "mm_root"

        background "black"

        if nsfw:
            add "bg title" yalign 0.5

            text "青楼之王" size res_font(128) xalign 0.5 yalign 0.35 drop_shadow (3,3) font "bk.ttf" color c_orange
            text "Brothel King" size res_font(64) xalign 0.5 yalign 0.5 drop_shadow (3,3) font "MATURASC.TTF" color c_orange

        text "For updates, bug reports, and discussion: [URL]" xalign 0.5 yalign 0.96 size res_font(14)

        vbox xalign 0.99 yalign 0.01:
            text "[renpy.version_string]" xalign 1.0 size res_font(12)
            text "BK [config.version]" xalign 1.0 size res_font(12)
            text "汉化 v20240828" xalign 1.0 size res_font(12)

        if debug:
            text mod_traceback xalign 0.01 yalign 0.01 size res_font(18)

    # The main menu buttons.
    frame background None:
        xalign .5
        yalign .75

        hbox spacing xres(20):
            frame yalign 0.5:
                style_group "mms"
                vbox:
                    textbutton _("Girl packs") action (Jump("girlpack_menu_restart"))
                    textbutton _("Mods"):
                        if detected_mods:
                            action ShowMenu("mods")
                    textbutton _("Extras") action (Function(init_galleries), ShowMenu("galleries"), Function(renpy.music.stop, fadeout=3.0))
            frame yalign 0.5:
                style_group "mm"
                vbox:
                    textbutton _("Start Game") text_color c_white action Start()
                    textbutton _("Load Game") text_color c_white action ShowMenu("load")
                    textbutton _("Quit") text_color c_white action Quit(confirm=False)
            frame yalign 0.5:
                style_group "mms"
                vbox:
                    textbutton _("Preferences") action ShowMenu("preferences")
                    textbutton _("Resolution") action Jump("pick_resolution")
                    textbutton _("Help") action Help()


label pick_resolution():
    hide screen main_menu

    menu:
        "Choose target resolution (currently [config.screen_width]x[config.screen_height])"

        "1920x1080 (16:9)":
            $ persistent.screen_width = 1920
            $ persistent.screen_height = 1080

        "1024x768 (4:3)":
            $ persistent.screen_width = 1024
            $ persistent.screen_height = 768

        "自定义分辨率":
            python:
                narrator("{color=%s}Warning: This feature is experimental. Please use at your own risks.{/color}" % c_red, interact=False)
                _stop = False

                x = renpy.input("Choose screen width", default=config.screen_width, length = 4)
                try:
                    x = int(x)
                except:
                    renpy.say(bk_error, "The width value you entered is not a valid number (%s)" % x)
                    _stop = True

                if not 800 <= x <= 3840:
                    renpy.say(bk_error, "The width value is too high or too low (%s)" % x)
                    _stop = True

                if not _stop:
                    narrator("{color=%s}Warning: This feature is experimental. Please use at your own risks.{/color}" % c_red, interact=False)
                    y = renpy.input("Choose screen height", default=config.screen_height, length = 4)
                    try:
                        y = int(y)
                    except:
                        renpy.say(bk_error, "The height value you entered is not a valid number (%s)" % y)
                        _stop = True

                    if not 600 <= y <= 2160:
                        renpy.say(bk_error, "The height value is too high or too low (%s)" % y)
                        _stop = True

                if x == persistent.screen_width and y == persistent.screen_height:
                    _stop = True

                if _stop:
                    renpy.full_restart()
                else:
                    persistent.screen_width = x
                    persistent.screen_height = y

        "取消":
            $ renpy.full_restart()

    $ centered("Restarting Brothel King...", interact=False)

    pause 0.01

    $ renpy.utter_restart()

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"
    style mms_button:
        size_group "mms"
    style diff_button:
        size_group "diff"
    style mix_button:
        size_group "mix"
    style extras_button:
        size_group "extras"

    style mm_button_text:
        size res_font(24)
    style mms_button_text:
        size res_font(20)



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # Enables right_clicking to exit
    key "mouseup_3" action Return()

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Game settings") action ShowMenu("h_content")
        textbutton _("Achievements") action ShowMenu("achievements")
        textbutton _("Mods") action ShowMenu("mods")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button is UI_button

    style gm_nav_button_text is UI_button_text

    # Basic UI button style
    style UI_button is button:
        xalign 0.5
        yalign 0.5
        selected_background AlphaMask(Solid(c_white), Frame("UI/cry_box.webp", left=0, right=0)) # Thanks go to anne O'nymous of f95 for this

    style UI_button_text is text:
        selected_color c_darkorange
        xalign 0.5
        yalign 0.5

    style UI_bar is bar:
        left_bar AlphaMask(Solid(c_darkorange), Frame("UI/cryslider_full.webp", left=12, right=12))
        right_bar AlphaMask(Solid(c_darkorange), Frame("UI/cryslider_empty.webp", left=12, right=12))

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

## These awesome save/load screens were made by OhWee

screen file_picker():

    fixed:
        xfill False

        fixed:
            #style "file_picker_frame"
            xalign 0.0
            #ypadding 10

            frame background Frame("UI/papersquare.webp", left=12, right=12, top=12, bottom=12):
                xmargin 3
                left_padding xres(12)
                right_padding xres(12)
                ypadding yres(60)

                xalign 0.0
                yalign 0.5

                yoffset 10


                grid 3 4:
                    #style_prefix "slot"

                    xspacing 0
                    yspacing 24

                    for i in range(12):

                        $ slot = i + 1

                        button xsize 0.27 ysize 0.2:
                            action FileAction(slot)
                            background None

                            has vbox spacing 0

                            if FileTime(slot) == "":
                                add "UI/SaveSlotEmpty.webp" selected_hover_alpha 1.0 hover_alpha 1.0 idle_alpha 0.8 selected_idle_alpha 0.8 insensitive_alpha 0.8 alpha 0.8 fit "contain"

                            else:
                                add FileScreenshot(slot) xalign 0.5 selected_hover_alpha 1.0 hover_alpha 1.0 idle_alpha 0.8 selected_idle_alpha 0.8 insensitive_alpha 0.8 alpha 0.8 fit "contain"

                            text FileTime(slot, format=_("{#file_time}%A, %B %d, %H:%M"), empty=_("empty slot")):
                                style "slottext"

                            text FileSaveName(slot):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)


            vbox:
                #style_group "file_picker_nav"
                xalign 1.0
                yfill False
                xoffset 10
                yoffset 30

                grid 2 2:
                    xalign 0.5
                    xoffset 0

                    textbutton _("Previous") style "UI_button":
                        action FilePagePrevious()
                        xalign 0.5
                        xoffset 16

                    textbutton _("Auto") style "UI_button":
                        action FilePage("auto")
                        xalign 0.5

                    textbutton _("Next") style "UI_button":
                        action FilePageNext()
                        xalign 0.5

                    textbutton _("Quick") style "UI_button":
                        action FilePage("quick")
                        xalign 0.5

                text "" size res_font(6)

                grid 3 7:
                    xalign 0.5
                    yspacing 2
                    xspacing -2

                    for i in range(21):
                        textbutton str(i+1) style "UI_button":
                            xsize xres(32)
                            ysize yres(22)
                            action FilePage(i+1)
                            text_size res_font(14)
                            text_selected_size res_font(17)
                            text_selected_bold True

                text "" size res_font(8)
                text "{i}Screen made\n by OhWee{/i}" size res_font(12) xalign 0.85 color "#521" text_align 1.0 line_spacing -2


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style slottext:
        size res_font(14)
        color "#521"
        xalign 0.5
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    size res_font(12)


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum xres(192)
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True
    zorder 20

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size res_font(12)
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
