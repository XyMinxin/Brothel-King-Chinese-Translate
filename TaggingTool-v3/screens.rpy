################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


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

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

# Edited and moved down
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900


# Above from renpy-8.3.4
# Below is new or edited



## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Select girl pack") action (SetVariable("mode", "select"), Start())
            textbutton _("Edit girl pack") action (SetVariable("mode", "edit"), Start())
            textbutton _("Browse girl pack") action (SetVariable("mode", "browse"), Start())
            textbutton _("Girl pack statistics") action (SetVariable("mode", "stats"), Start())
            # textbutton _("Generate BK.ini") action (SetVariable("mode", "ini"), Start()) # <neronero & RudolfU - BK.ini generator> not ported to 3 yet
            textbutton _("Replacing tool") action (SetVariable("mode", "replace"), Start())
    #        textbutton _("Test") action Jump("mytest")
            textbutton _("Export Girlsdata CSV") action Jump("export_girlsdata")

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        # textbutton _("Load") action ShowMenu("load")

        # textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


init -2:
    style quick_button:
        is default
        background None
        xpadding 5
        ypadding 3

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

screen show_pic(context="edit"):
    
    default show_ui = True
    default tt = Tooltip("[text1] [girl.dir]")
    
    key "mouseup_3" action (ToggleScreenVariable("show_ui"), SetVariable("cancelAction", True))
    
    if selected_pic:
        if show_ui and not selected_pic.video:
            $ ibg = img_bg
        else:
            $ ibg = None
        frame background ibg  xalign 0.45  yalign 0.15  padding (0,0)  margin (0,0) :
            # add selected_pic.get_std_displayable() xalign 0.5 yalign 0.5
            add ProportionalScale(selected_pic.file, 480, 360) xalign 0.5 yalign 0
    elif context == "edit":
        text "No picture found." xalign 0.5 yalign 0.5
    elif context == "browse":
        text "No picture found. Use filters to display or hide pictures." xalign 0.5 yalign 0.5
    
    if selected_pic:
        if selected_pic.delete:
            text "X" xalign 0.5 yalign 0.5 color "#FF003366" size 526
    
    if show_ui:
        use pic_ui(context, tt)
        use pic_carousel(context, tt)

screen pic_button(pic, tt):
    $ pic_name = pic.file_name
    $ global selected_pic_list
    $ select_text = " (Selected)" if pic in selected_pic_list else ""
    button:
        style "carousel_button"
        xalign 0.5 ycenter 0.5 xpadding 9 ypadding 9
        xsize 220 ysize 190
        action Return(("carousel_show", pic))
        selected (pic in selected_pic_list)
        key "K_SPACE" action Return(("carousel_toggle", pic))
        hovered tt.Action(pic_name + "%s\nMouse Left: Show Pic, Space: Toggle selection" % select_text)
        vbox xalign 0.5:
            spacing 10
            text pic_name + select_text size 12
            fixed xalign 0.5:
                fit_first True
                if pic.video:
                    add Movie(play=pic.file, size=[180,135]) xalign 0.5
                else:
                    add ProportionalScale(pic.file, 180, 135) xalign 0.5

screen pic_carousel(context, tt):
    $ global filtered_pics
    $ global selected_index
    $ global selected_pic
    
    frame yalign 0.75 xfill True xpos 0.14 xanchor 0 xsize 1100 background None:
        grid 5 2 spacing 6:
            $ pics = filtered_pics[selected_index:selected_index+10]
            for pic in pics:
                use pic_button(pic, tt)    
    
screen pic_ui(context, tt):
#    key "mouseup_3" action Hide("pic_ui")
    key "K_LEFT" action Return("cycle_previous")
    key "shift_K_LEFT" action Return("cycle_previous_10")
    key "ctrl_K_LEFT" action Return("cycle_previous_100")
    key "K_KP_4" action Return("cycle_previous")
    key "shift_K_KP_4" action Return("cycle_previous_10")
    key "ctrl_K_KP_4" action Return("cycle_previous_100")
    key "K_RIGHT" action Return("cycle_next")
    key "shift_K_RIGHT" action Return("cycle_next_10")
    key "ctrl_K_RIGHT" action Return("cycle_next_100")
    key "K_KP_6" action Return("cycle_next")
    key "shift_K_KP_6" action Return("cycle_next_10")
    key "ctrl_K_KP_6" action Return("cycle_next_100")

    # <Chris12 - Tagsets>
    # Replaced hotkeys with this, so that you can add_tag_hotkey
    for k, t in tag_hotkeys.items():
        key k action Return(("tag", t))
    # </Chris12 - Tagsets>
    key "K_DELETE" action Return("delete")
    key "K_KP_PERIOD" action Return("delete")
    
    # New shortcuts just for Leortha ;)
    key "shift_K_DELETE" action Return("delete and advance")
    key "K_HOME" action Return("cycle_home")
    key "K_END" action Return("cycle_end")
    
    use input_button(context)
    
#    text str(selected_pic.has_tag("inside")) color "#000000" xalign 0.5 yalign 0.5 xsize 0.5
    
    frame background None xsize 0.5 xalign 0.3:
        
        if context == "edit":
            $ text1 = "Editing"
            $ text2 = ""
        elif context == "browse":
            $ text1 = "Browsing"
        text tt.value size 16
    
    frame yalign 0.93 xfill True xalign 0.45 xsize 800 background None:
        has hbox spacing 20
        
        hbox:
            textbutton "-100" text_size 14 action Return("cycle_previous_100") hovered tt.Action("Skip 100 pictures back (shortcut: Ctrl+left arrow)") xalign 0.0 yalign 1.0 xsize 40 ysize 40 xfill True yfill True
            textbutton "-10" text_size 14 action Return("cycle_previous_10") hovered tt.Action("Skip 10 pictures back (shortcut: Shift+left arrow)") xalign 0.0 yalign 1.0 xsize 40 ysize 40 xfill True yfill True
            textbutton "<" text_size 18 action Return("cycle_previous") hovered tt.Action("Skip to previous picture (shortcut: left arrow)") xalign 0.0 yalign 1.0 xsize 40 ysize 40 xfill True yfill True
        

        frame background None xalign 0.5 ysize 50 xsize 480:
            if selected_pic:
                $ text1 = "File (" + str(girl.pics.index(selected_pic)+1) + "/" + str(len(girl.pics)) + "): "
                $ if selected_pic.sub_dir != None : text1 += "{color=#FF964C}" + str(selected_pic.sub_dir) + "{/color} "
                $ text1 += selected_pic.file_name
                if selected_pic.file_name[:selected_pic.file_name.find("(")] != str(selected_pic.new_name)[:str(selected_pic.new_name).find("(")]:
                    $ text1 += "{color=#7fffd4} --> " + str(selected_pic.new_name) + " (new)"

                text text1 size 16 xalign 0.5 yalign 0.5 #color "#000"
        
        hbox:
            textbutton ">" text_size 18 action Return("cycle_next") hovered tt.Action("Skip to next picture (shortcut: right arrow)") xalign 1.0 yalign 1.0 xsize 40 ysize 40 xfill True yfill True
            textbutton "+10" text_size 14 action Return("cycle_next_10") hovered tt.Action("Skip 10 pictures forward (shortcut: Shift+right arrow)") xalign 1.0 yalign 1.0 xsize 40 ysize 40 xfill True yfill True
            textbutton "+100" text_size 14 action Return("cycle_next_100") hovered tt.Action("Skip 100 pictures forward (shortcut: Ctrl+right arrow)") xalign 1.0 yalign 1.0 xsize 40 ysize 40 xfill True yfill True
        
    
    hbox xalign 0.4 yalign 0.98 xsize 0.6 xfill True:
        
        if context == "edit":
        
#            vbox yalign 1.0:
            hbox xalign 0.5 yalign 0.99:
                
                if persistent.optional_filter:
                    $ text1 = " (ON)"
                else:
                    $ text1 = " (OFF)"
                
                textbutton "COMMIT\nCHANGES" action Return("commit") hovered tt.Action("This will commit all changes to the current girl pack and rename all files.") text_size 18 yminimum 50 xminimum 120
                # <Chris12 - Tagsets>
                if len(all_tagsets) > 1 : 
                    textbutton "TAGSET\n" + persistent.active_tagset action Return("cycle_active_tagset") hovered tt.Action("This will switch between different Modes.") text_size 18 yminimum 50 xminimum 120 # <Chris12 - Tagsets />
                # </Chris12 - Tagsets>
                textbutton "FILTER\nTAGS" + text1 action ToggleField(persistent, "optional_filter") hovered tt.Action("This will activate/deactivate the contextual filter for tags.") text_size 18 yminimum 50 xminimum 120
                textbutton "CLEAR\nTAGS" action Return("clear") alternate Return("clear_all") hovered tt.Action("This will clear all active tags for this picture.\nRight-click to clear all active tags FOR ALL PICTURES IN THE GIRL PACK.") text_size 18 yminimum 50 xminimum 120
                textbutton "BROWSE\nMODE" action Return("browse") hovered tt.Action("This will switch to browsing mode.") text_size 18 yminimum 50 xminimum 120
                textbutton "JUMP\nTO" action Return("jump_to") hovered tt.Action("This will switch to tag edit mode.") text_size 18 yminimum 50 xminimum 120
                textbutton "QUIT" action Return("quit") text_size 18 yminimum 50 xminimum 120
        
        elif context == "browse":
            
            hbox xalign 0.5 yalign 0.99:
                
                textbutton str(girl.count_pics(filters=active_filters, include_bk_autoadds=False)) + " pics found with active filters" xsize 250 text_size 16 text_text_align 0 yminimum 50 background "#444" text_color "#ddd"
                # <Chris12 - Tagsets>
                if len(all_tagsets) > 1 : 
                    textbutton "TAGSET\n" + persistent.active_tagset action Return("cycle_active_tagset") hovered tt.Action("This will switch between different Modes.") text_size 18 yminimum 50 xminimum 120
                # </Chris12 - Tagsets>
                textbutton "CLEAR\nFILTERS" action Return("clear") hovered tt.Action("This will clear all active filters.") text_size 18 yminimum 50 xminimum 120
                textbutton "EDIT\nMODE" action Return("edit") hovered tt.Action("This will switch to tag edit mode.") text_size 18 yminimum 50 xminimum 120
                textbutton "JUMP\nTO" action Return("jump_to") hovered tt.Action("This will switch to tag edit mode.") text_size 18 yminimum 50 xminimum 120
                textbutton "CYCLE\nALL" action Return("cycle_all") hovered tt.Action("This will quickly cycle over all images.") text_size 18 yminimum 50 xminimum 120
                textbutton "QUIT" action Return("quit") text_size 18 yminimum 50 xminimum 120
        
        
        if context == "edit" and selected_pic:
            button yalign 1.0 action Function(selected_pic.toggle_delete)  hovered tt.Action("This will mark the picture for deletion (it does not actually delete the picture, but renames it to '_Trash*' when changes are commited). Shortcut: Del."):
                add "gui/trash.png"
    

    
    
#    hbox xfill True yfill True:
        
    vbox spacing 1 xalign 0.02 ypos 0.01 :
        
        frame background "#00000033":
            textbutton "MAIN TAGS" text_size 16 background None text_bold True action NullAction() hovered tt.Action("Every picture should have some of those tags.")
        
        frame background "#6496C8" :
            has vbox spacing 3
            
            # <Chris12 - Tagsets>
            # Filter tags based on tagsets
            # main_tags was replaced with a list of tuples [("profile", Tag()), ("portrait", Tag()), ...]
            $ show_tags = [tag for tag in main_tags if tag.tagsets.issubset(get_tagset(persistent.active_tagset).all_names) or (selected_pic and tag.name in selected_pic.tags)]
            # </Chris12 - Tagsets>
            for tag_definition in show_tags:
                
                if tag_definition and tag_definition.name != "":
                    $ tag = tag_definition.name
                    if (context == "browse" and tag in active_filters) or (context == "edit" and selected_pic and tag in selected_pic.tags):
                        $ col = "#FF69B4"
                        $ is_bold = True
                    elif selected_pic and tag in selected_pic.tags:
                        $ col = "#FFFF33"
                        $ is_bold = False
                    else:
                        $ col = "#FFF"
                        $ is_bold = False
                    
                    python:
                    
                        for tags, ttip in tag_main_help.items():
                            if tag in make_tuple(tags):
                                break
                        else:
                            ttip = "[text1] [girl.dir]."
                        
                    textbutton tag_button_dict[tag] text_color col xsize 195 xfill True action Return(("tag", tag)) hovered tt.Action(ttip) text_bold is_bold
                        
                else:
                    text "" size 10
        
    vbox spacing 1 xalign 0.98 ypos 0.01:
        
        frame background "#00000033" xalign 1:
            textbutton "OPTIONAL TAGS" text_size 16 background None text_bold True action NullAction() hovered tt.Action("You should only include those tags if the picture matches. Using optional tags without main tags will result in limited displayability in-game.")
        
        frame background "#6496C8" xalign 1.0:
            ysize 0.994
            has vbox ysize 0.99
            spacing 1
            box_wrap True
            xalign 1.0
            
            # <Chris12 - Tagsets>
            $ if get_tagset(persistent.active_tagset) is None: persistent.active_tagset = STANDARD_TAGSET # Just to be safe when a tagset.rpy got completely deleted
            
            # Sort the tags, then filter based on the active TagSet
            $ show_tags = [] # Filter showtags beforehand, so that len(show_tags) can help scaling the font_size
            for tag_def in optional_tags: # <Chris12 - Tagsets - now looping over variable show_tags />
                $ tag = tag_def.name
                if (selected_pic and tag in selected_pic.tags) or tag_def.tagsets.issubset(get_tagset(persistent.active_tagset).all_names):
                    if context == "browse" or not selected_pic or (tag in selected_pic.tags or tag_def.check_conditions(tag_list=selected_pic.tags) or not persistent.optional_filter):
                        $ show_tags.append(tag_def)                
            # </Chris12 - Tagsets>
            
            $ group = show_tags[0].order
            $ last_order = group
            
            for tag_def in show_tags: # <Chris12 - Tagsets - now looping over variable show_tags />
                $ tag = tag_def.name
                
                # <Chris12 - Moved this part into the if, so that there are never multiple spaces between two tags
                if tag_def.order != group:
                    $ group = tag_def.order
                    if group > last_order:
                        $ divider_size = 6
                        if len(show_tags) > 102 : # automatically scale font size if there are many tags. 102 is a 'magic number' that seems to work
                            $ divider_size = 6 * 102 / len(show_tags)
                        text "" size divider_size
                # </Chris12>

                $ last_order = tag_def.order

                if (context == "browse" and tag in active_filters) or (context == "edit" and selected_pic and tag in selected_pic.tags):
                    $ col = "#FF69B4"
                elif selected_pic and tag in selected_pic.tags:
                    $ col = "#FFFF33"
                else:
                    $ col = "#FFF"
                    if (context == "edit" and not persistent.optional_filter and not tag_def.check_conditions(tag_list=selected_pic.tags)):
                        $ col += "9"

                $ ttip = "The {b}" + tag + "{/b} tag adds the following tags in-game: " + and_text(list_associated_tags(tag))
                if tag in tag_special_help.keys():
                    $ ttip += "\n" + tag_special_help[tag]

                $ btn_text_size = tag_def.btn_text_size
                $ btn_ysize = 26
                if len(show_tags) > 102 : # automatically scale font size if there are many tags. 102 is a 'magic number' that seems to work
                    $ btn_text_size = btn_text_size * 102 / len(show_tags)
                    $ btn_ysize = btn_ysize * 102 / len(show_tags)

                textbutton tag_def.lbl text_size btn_text_size text_color col xsize 120 ysize btn_ysize xfill True action Return(("tag", tag)) hovered tt.Action(ttip)


screen pack_stats(girl):
    
    modal True
    
    key "mouseup_3" action Return("quit")
    
    frame background "#6496C8":
        xsize 1.0
        ysize 1.0
        
        has vbox spacing 20
        
        text girl.path bold True
        text "Rating: " + get_girlpack_rating(girl)

        $ basic_stats = {}

        hbox spacing 50:
        
            vbox spacing 60 box_wrap True:

                hbox spacing 68:

                    vbox spacing 20 box_wrap True:
            
                        text "BASIC PICTURES"

                        hbox spacing 10 :
                                        
                            for tag in ("profile", "portrait", "waitress", "dancer", "masseuse", "geisha", "rest"):
                                $ basic_stats[tag + " naked"] = girl.count_pics([tag, "naked"])
                                $ basic_stats[tag] = girl.count_pics([tag]) - basic_stats[tag + " naked"]
                            
                            grid 3 8 spacing 10:
                                text ""
                                text "Normal" size 20
                                text "Naked" size 20
                                for tag in ("profile", "portrait", "waitress", "dancer", "masseuse", "geisha", "rest"):
                                    text tag.capitalize() size 20
                                    text format_stat(basic_stats[tag]) size 20
                                    text format_stat(basic_stats[tag + " naked"]) size 20

                    vbox spacing 20 box_wrap True:
                        
                        text "SEX PICTURES"

                        hbox spacing 10 :
                            
                            for tag in ("naked", "service", "sex", "anal", "fetish"):
                                $ basic_stats[tag + " bisexual"] = girl.count_pics([tag, "bisexual"])
                                $ basic_stats[tag + " group"] = girl.count_pics([tag, "group"])
                                $ basic_stats[tag] = girl.count_pics([tag]) - basic_stats[tag + " bisexual"] - basic_stats[tag + " group"] + girl.count_pics([tag, "group", "bisexual"])
                            
                            grid 4 6 spacing 10:
                                text ""
                                text "Normal" size 20
                                text "Bisexual" size 20
                                text "Group" size 20
                                for tag in ("naked", "service", "sex", "anal", "fetish"):
                                    text tag.capitalize() size 20
                                    text format_stat(basic_stats[tag]) size 20
                                    if tag == "naked":
                                        text "-" size 20
                                        text "-" size 20
                                    else:
                                        text format_stat(basic_stats[tag + " bisexual"]) size 20
                                        text format_stat(basic_stats[tag + " group"]) size 20
                    
                vbox spacing 20 box_wrap True:
                
                    text "FARM PICTURES"
                    
                    for tag in ("big", "beast", "monster", "machine"):
                        for tag2 in ("naked", "service", "sex", "anal", "fetish", "bisexual", "group"):
                            $ basic_stats[tag, tag2] = girl.count_pics([tag, tag2])
                    
                    grid 8 5 spacing 10:
                        text ""
                        for tag in ("naked", "service", "sex", "anal", "fetish", "bisexual", "group"):
                            text tag.capitalize() size 20

                        for tag in ("big", "beast", "monster", "machine"):
                            text tag.capitalize() size 20
                            for tag2 in ("naked", "service", "sex", "anal", "fetish", "bisexual", "group"):
                                text format_stat(basic_stats[tag, tag2]) size 20

            vbox spacing 20 box_wrap True:

                text "OPTIONAL PICTURES"

                $ tags = [x for x in optional_tags if x.tagsets.issubset(get_tagset(STANDARD_TAGSET).all_names)] # <Chris12 - Tagsets />
                $ y_coord = 1+len(tags) 
                
                for tag_def in tags:
                    $ tag = tag_def.name
                    $ basic_stats[tag, "total"] = girl.count_pics([tag])
                    for tag2 in ("naked", "service", "sex", "anal", "fetish", "bisexual", "group"):
                        $ basic_stats[tag, tag2] = girl.count_pics([tag, tag2])
                
                viewport:
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    ysize 0.8
                    xpos 0.1
                    xsize 0.9
                    xfill False  
                    yfill False            
                    
                    grid 9 y_coord yspacing 0 xfill False:
                        text ""
                        for tag in ("total", "naked", "service", "sex", "anal", "fetish", "bisexual", "group"):
                            text tag.capitalize() size 12

                        for tag_def in tags:
                            $ tag = tag_def.name
                            text tag.capitalize()  size 12
                            text format_stat(basic_stats[tag, "total"]) size 12
                            for tag2 in ("naked", "service", "sex", "anal", "fetish", "bisexual", "group"):
                                if tag in ("happy", "neutral", "sad", "maid", "kimono", "swim", "sing", "fight", "libido", "sensitivity", "obedience", "constitution"):
                                    text "-" size 12
                                elif tag in fix_dict.keys() and tag2 not in fix_dict[tag].acts:
                                    text "-" size 12
                                elif optional_tag_dict[tag].fix_name and tag2 not in fix_dict[optional_tag_dict[tag].fix_name].acts:
                                    text "-" size 12
                                else:
                                    text format_stat(basic_stats[tag, tag2]) size 12
            
                text "Combinations marked with '-' do not count towards the girl pack rating." size 14 xalign 0.5
                    
                hbox spacing 20 xalign 0.9:
                    textbutton "Tips" action Return("tips")
                    textbutton "Quit" action Return("quit") xalign 0.9


screen change_log:
    
    frame:
        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            xfill False  
            yfill False
            
            has vbox spacing 10
            
            text "Queued changes"
            
            for old, new in persistent.change_log.items():
                text "Rename {b}{color=#ff4d4d}" + old + "{/color}{/b} (old) to {b}{color=#7fffd4}" + str(new) + "{/color}{/b} (new)" size 12
            
            text ""
            
            hbox spacing 50:
                textbutton "COMMIT CHANGES" action Return("commit")
                textbutton "DISCARD CHANGES" action Return("discard")


screen rating_tips():
    
    frame xalign 0.5 xmaximum 0.9 xpadding 20 ypadding 50 yalign 0.5 background "#dcebff":
        
        has vbox spacing 20 xmaximum 0.9
        
        $ text1 = ("{b}UNDERSTANDING THE RATING{/b}\n\n"
                + "There are two scores: a 'cover score' (from A to F) and a 'diversity score' (+, nothing or -). Please note that the math in the code is a little different, but I have tried to keep it simple for the sake of explaining.\n\n{b}Cover score{/b}:"
                + "\n\nThe game first checks if you have various game situations covered with at least one picture:\n- You get 10 points for covering each soft type ('profile', 'portrait', 'rest', 'waitress', 'dancer', 'masseuse', 'geisha') and its variations (clothed/naked): A total of 140 points max\n- You get 10 points for covering each sex act ('service', 'sex', 'anal', 'fetish') and its variations (vanilla/group/bisexual): A total of 120 points max\n- You get 4 points for covering each farm tag ('big', 'beast', 'monster', 'machine') and each its variations ('naked', 'service', 'sex', 'anal', 'fetish', 'bis', 'group'): A total of 112 points max\n- You get 4 points for each fixation tag and its variations (exact number depends on the fixation). A total of 524 points max.\n"
                + "\n\nAn 'A' score means you have at least 85% of the 896 total possible points. A 'B' score means you have 70-85% of that maximum. An 'F' score means you are below 30%. As you can see, covering optional tags (farm and fixations) well is key to get the higher scores. Only covering the basic tags will net you a D."
                + "\n\n{b}Diversity score{/b}:\n\nThe game next looks for picture diversity, ie how many pictures of each you have in your pack. As of now, it only does that for main picture types (soft and sex) and their variations. It does not take into account optional pictures variety (farm and fixations)."
                + "\n\nIf you have an average of 5 different pictures for each main picture type or more, you get a '+'. If you have less than 3, you get a '-'."
                )
        
        text text1 size 18 color "#000099"
        
        textbutton "Close" action Return() xalign 0.9
        
        
screen input_button(context):
    
    hbox spacing 15 xpos 0.22 ypos 0.09 xsize 0.64 xfill True:
        
        textbutton "Search" text_size 18:
            action Return("search")
        
        if search_words:
            text search_words size 18
        
        if search_words or copy_tags:
            textbutton "Clear" text_size 18:
                action Return("clear_search")
        
        if context == "edit":
            if copy_tags:
                textbutton "Paste Tags" text_size 18:
                    action Return("paste_tags")
            else:
                textbutton "Copy Tags" text_size 18:
                    action Return("copy_tags")
        
        if selected_pic != None and selected_pic.file in img_resolutions :
            text img_resolutions[selected_pic.file] size 18
