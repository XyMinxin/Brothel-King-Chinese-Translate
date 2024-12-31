# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

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

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

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

    # The background of the main menu.
    window:
        style "mm_root"

        text "版本: [config.version]" xalign 0.5 yalign 0.95 color "#003C78"
        text "此工具由Minxin汉化" xalign 0.5 yalign 0.98 color "#003C78"

    text "选定的人物包: {b}" + str(persistent.girl) color "#CC6600" xalign 0.5 yalign 0.05

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .5

        has vbox spacing 10

        textbutton _("选择人物包") action (SetVariable("mode", "select"), Start())
        textbutton _("编辑人物包") action (SetVariable("mode", "edit"), Start())
        textbutton _("浏览人物包") action (SetVariable("mode", "browse"), Start())
        textbutton _("人物包统计") action (SetVariable("mode", "stats"), Start())
        textbutton _("生成BK.ini") action (SetVariable("mode", "ini"), Start()) # <neronero & RudolfU - BK.ini generator>
        textbutton _("替换工具(快速替换标签)") action (SetVariable("mode", "replace"), Start())
        textbutton _("帮助") action Help()
#        textbutton _("Test") action Jump("mytest")
        textbutton _("导出人物数据CSV") action Jump("export_girlsdata")
        textbutton _("导出人物包状态") action Jump("export_currentstate")
        textbutton _("导入人物包状态") action (SetVariable("mode", "import_packstate"), Start())
        textbutton _("导出所有包状态") action Jump("export_allstates")
#        textbutton _("Export Debugdata") action Jump("export_debugdata")
        textbutton _("退出") action Quit(confirm=False)



init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("返回") action Return()
        textbutton _("选项") action ShowMenu("preferences")
        textbutton _("保存") action ShowMenu("save")
        textbutton _("加载") action ShowMenu("load")
        textbutton _("菜单") action MainMenu()
        textbutton _("帮助") action Help()
        textbutton _("退出") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("上一页"):
                action FilePagePrevious()

            textbutton _("自动"):
                action FilePage("auto")

            textbutton _("快速"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("下一页"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("空位。"))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


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
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


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

                label _("显示")
                textbutton _("窗口") action Preference("display", "window")
                textbutton _("全屏") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("过渡")
                textbutton _("全部") action Preference("transitions", "all")
                textbutton _("无") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("文字速度")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("控制杆...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("跳过")
                textbutton _("已读信息") action Preference("skip", "seen")
                textbutton _("全部信息") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("开始跳过") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("选择之后")
                textbutton _("停止跳过") action Preference("after choices", "stop")
                textbutton _("继续跳过") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("自动前进时间")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("等待声音") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("音乐音量")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("声音大小")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("测试"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("音量")
                    bar value Preference("voice volume")

                    textbutton _("声音持续") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("测试"):
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
        xmaximum 192
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

            textbutton _("是") action yes_action
            textbutton _("否") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

screen warning(message):

    modal True

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

            textbutton _("OK") action Return(True)

    # Right-click and escape answer "no".
    key "game_menu" action Return(False)


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

        textbutton _("返回") action Rollback()
        textbutton _("保存") action ShowMenu('save')
        textbutton _("Q.保存") action QuickSave()
        textbutton _("Q.加载") action QuickLoad()
        textbutton _("跳过") action Skip()
        textbutton _("F.跳过") action Skip(fast=True, confirm=True)
        textbutton _("自动") action Preference("auto-forward", "toggle")
        textbutton _("菜单") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

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

    key "mouseup_3" action (ToggleScreenVariable("show_ui"), SetVariable("cancelAction", True))

    if selected_pic:
        if show_ui and not selected_pic.video:
            $ ibg = img_bg
        else:
            $ ibg = None
        frame background ibg  xalign 0.45 yalign 0.2 padding (0,0)  margin (0,0) :
            # add selected_pic.get_std_displayable() xalign 0.5 yalign 0.3
            add ProportionalScale(selected_pic.file, 720, 540) xalign 0.5 yalign 0.2
    elif context == "edit":
        text "没有找到图片。" xalign 0.5 yalign 0.5
    elif context == "browse":
        text "没有找到图片。使用过滤器来显示或隐藏图片。" xalign 0.5 yalign 0.5

    if selected_pic:
        if selected_pic.delete:
            text "X" xalign 0.5 yalign 0.5 color "#FF003366" size 526

    if show_ui:
        use pic_ui(context)
        use pic_carousel(context)
        
screen pic_button(pic, context):
    default tt = Tooltip("pic_button")
    button:
        xalign 0.5
        ycenter 0.5
        xpadding 9
        ypadding 9
        xsize 220
        action Return("tips") hovered tt.Action("test") 
        vbox:
            spacing 10
            text pic.file_name xalign 0.5 yalign 0.5
            add ProportionalScale(pic.file, 180, 135) xalign 0.5 yalign 0.5

screen pic_carousel(context):
    $ global filtered_pics
    $ global selected_index
    $ global selected_pic
    
    default tt = Tooltip("pic_carousel")
    frame yalign 0.85 xfill True xalign 0.22 xsize 700 background None:
        has hbox spacing 20
        hbox:
            $ pics = filtered_pics[selected_index:selected_index+5]
            for pic in pics:
                use pic_button(pic, context)

screen pic_ui(context):
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
            $ text1 = "编辑"
            $ text2 = ""
        elif context == "browse":
            $ text1 = "浏览"

        default tt = Tooltip("[text1] [girl.dir]")
        text tt.value size 16

    frame yalign 0.93 xfill True xalign 0.45 xsize 800 background None:
        has hbox spacing 20

        hbox:
            textbutton "-100" text_size 14 action Return("cycle_previous_100") hovered tt.Action("向后跳过100张图片（快捷键：Ctrl+左箭头）") xalign 0.0 yalign 1.0 xsize 40 ysize 40 xfill True yfill True
            textbutton "-10" text_size 14 action Return("cycle_previous_10") hovered tt.Action("向后跳过10张图片（快捷键：Shift+左箭头）") xalign 0.0 yalign 1.0 xsize 40 ysize 40 xfill True yfill True
            textbutton "<" text_size 18 action Return("cycle_previous") hovered tt.Action("跳到上一张图片（快捷键：左箭头）") xalign 0.0 yalign 1.0 xsize 40 ysize 40 xfill True yfill True


        frame background None xalign 0.5 ysize 50 xsize 480:
            if selected_pic:
                $ text1 = "文件 (" + str(girl.pics.index(selected_pic)+1) + "/" + str(len(girl.pics)) + "): "
                $ if selected_pic.sub_dir != None : text1 += "{color=#FF964C}" + str(selected_pic.sub_dir) + "{/color} "
                $ text1 += selected_pic.file_name
                if selected_pic.file_name[:selected_pic.file_name.find("(")] != str(selected_pic.new_name)[:str(selected_pic.new_name).find("(")]:
                    $ text1 += "{color=#7fffd4} --> " + str(selected_pic.new_name) + " (新)"

                text text1 size 16 xalign 0.5 yalign 0.5 #color "#000"

        hbox:
            textbutton ">" text_size 18 action Return("cycle_next") hovered tt.Action("跳到下一张图片（快捷键：右箭头）") xalign 1.0 yalign 1.0 xsize 40 ysize 40 xfill True yfill True
            textbutton "+10" text_size 14 action Return("cycle_next_10") hovered tt.Action("向前跳过10张图片（快捷键：Shift+右箭头）") xalign 1.0 yalign 1.0 xsize 40 ysize 40 xfill True yfill True
            textbutton "+100" text_size 14 action Return("cycle_next_100") hovered tt.Action("向前跳过100张图片（快捷键：Ctrl+右箭头）") xalign 1.0 yalign 1.0 xsize 40 ysize 40 xfill True yfill True


    hbox xalign 0.4 yalign 0.98 xsize 0.6 xfill True:

        if context == "edit":

#            vbox yalign 1.0:
            hbox xalign 0.5 yalign 0.99:

                if persistent.optional_filter:
                    $ text1 = " (启用)"
                else:
                    $ text1 = " (关闭)"

                textbutton "保存更改" action Return("commit") hovered tt.Action("这将提交对当前人物包的所有修改，并重命名所有文件。") text_size 18 yminimum 50 xminimum 120
                # <Chris12 - Tagsets>
                if len(all_tagsets) > 1 :
                    textbutton "标签\n" + persistent.active_tagset action Return("cycle_active_tagset") hovered tt.Action("这将在不同的模式之间切换。") text_size 18 yminimum 50 xminimum 120 # <Chris12 - Tagsets />
                # </Chris12 - Tagsets>
                textbutton "过滤标签" + text1 action ToggleField(persistent, "optional_filter") hovered tt.Action("这将激活/停用标签过滤器。") text_size 18 yminimum 50 xminimum 120
                textbutton "清除标签" action Return("clear") alternate Return("clear_all") hovered tt.Action("这将清除该图片的所有有效标签。\n点击右键，清除人物包中所有图片的所有活动标签。") text_size 18 yminimum 50 xminimum 120
                textbutton "浏览模式" action Return("browse") hovered tt.Action("这将切换到标签浏览模式。") text_size 18 yminimum 50 xminimum 120
                textbutton "跳转模式" action Return("jump_to") hovered tt.Action("这将切换到标签跳转模式。") text_size 18 yminimum 50 xminimum 120
                textbutton "退出" action Return("quit") text_size 18 yminimum 50 xminimum 120

        elif context == "browse":

            hbox xalign 0.5 yalign 0.99:

                textbutton str(girl.count_pics(filters=active_filters, include_bk_autoadds=False)) + " pics found with active filters" xsize 250 text_size 16 text_text_align 0 yminimum 50
                # <Chris12 - Tagsets>
                if len(all_tagsets) > 1 :
                    textbutton "标签\n" + persistent.active_tagset action Return("cycle_active_tagset") hovered tt.Action("这将在不同的模式之间切换。") text_size 18 yminimum 50 xminimum 120
                # </Chris12 - Tagsets>
                textbutton "清除过滤" action Return("clear") hovered tt.Action("这将清除所有活动的过滤。") text_size 18 yminimum 50 xminimum 120
                textbutton "编辑模式" action Return("edit") hovered tt.Action("这将切换到标签编辑模式。") text_size 18 yminimum 50 xminimum 120
                textbutton "跳转模式" action Return("jump_to") hovered tt.Action("这将切换到标签跳转模式。") text_size 18 yminimum 50 xminimum 120
                textbutton "循环所有" action Return("cycle_all") hovered tt.Action("这将快速循环查看所有图像。") text_size 18 yminimum 50 xminimum 120
                textbutton "退出" action Return("quit") text_size 18 yminimum 50 xminimum 120


        if context == "edit" and selected_pic:
            button yalign 1.0 action Function(selected_pic.toggle_delete)  hovered tt.Action("这将标志着图片的删除（实际上并没有删除图片，只是在修改时将其重命名为‘_Trash*’）。快捷方式：Del"):
                add "UI/trash.png"




#    hbox xfill True yfill True:

    vbox spacing 4 xalign 0.02 ypos 0.01:

        frame background "#00000033":
            textbutton "主要标签" background None text_bold True action NullAction() hovered tt.Action("每张照片都应该有一些这样的标签。")

        frame:
            has vbox spacing 4

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

    vbox spacing 4 xalign 0.98 ypos 0.01:

        frame background "#00000033" xalign 1:
            textbutton "可选标签" background None text_bold True action NullAction() hovered tt.Action("只有在图片匹配的情况下，你才应该包括这些标签。使用可选的标签而不使用主要的标签，将导致在游戏中的可显示性受到限制。")

        frame xalign 1.0:
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
                        $ divider_size = 7
                        if len(show_tags) > 102 : # automatically scale font size if there are many tags. 102 is a 'magic number' that seems to work
                            $ divider_size = 7 * 102 / len(show_tags)
                        text "" size divider_size
                # </Chris12>

                $ last_order = tag_def.order

                if (context == "browse" and tag in active_filters) or (context == "edit" and selected_pic and tag in selected_pic.tags):
                    $ col = "#FF69B4"
                elif selected_pic and tag in selected_pic.tags:
                    $ col = "#FFFF33"
                else:
                    $ col = "#FFF"

                $ ttip = "该 {b}" + tag + "{/b} 标签在游戏中添加以下标签: " + and_text(list_associated_tags(tag))
                if tag in tag_special_help.keys():
                    $ ttip += "\n" + tag_special_help[tag]

                $ btn_text_size = 18
                if len(show_tags) > 102 : # automatically scale font size if there are many tags. 102 is a 'magic number' that seems to work
                    $ btn_text_size = 18 * 102 / len(show_tags)

                # textbutton tag_def.lbl text_size btn_text_size text_color col xsize 120 xfill True action Return(("tag", tag)) hovered tt.Action(ttip)
                textbutton tag_button2_dict[tag] text_size btn_text_size text_color col xsize 120 xfill True action Return(("tag", tag)) hovered tt.Action(ttip)


screen pack_stats(girl):

    modal True

    key "mouseup_3" action Return("quit")

    frame:
        xsize 1.0
        ysize 1.0

        has vbox spacing 20

        text girl.path bold True
        text "评级: " + get_girlpack_rating(girl)

        $ basic_stats = {}

        vbox spacing 20 box_wrap True:

            text "基本图片"

            for tag in ("profile", "portrait", "waitress", "dancer", "masseuse", "geisha", "rest"):
                $ basic_stats[tag + " naked"] = girl.count_pics([tag, "naked"])
                $ basic_stats[tag] = girl.count_pics([tag]) - basic_stats[tag + " naked"]

            grid 3 8 spacing 10:
                text ""
                text "普通" size 20
                text "裸体" size 20
                for tag in ("profile", "portrait", "waitress", "dancer", "masseuse", "geisha", "rest"):
                    text tag_button2_dict[tag] size 20
                    text format_stat(basic_stats[tag]) size 20
                    text format_stat(basic_stats[tag + " naked"]) size 20

            text "" size 20
            text "性爱图片"

            for tag in ("naked", "service", "sex", "anal", "fetish"):
                $ basic_stats[tag + " bisexual"] = girl.count_pics([tag, "bisexual"])
                $ basic_stats[tag + " group"] = girl.count_pics([tag, "group"])
                $ basic_stats[tag] = girl.count_pics([tag]) - basic_stats[tag + " bisexual"] - basic_stats[tag + " group"] + girl.count_pics([tag, "group", "bisexual"])

            grid 4 6 spacing 10:
                text ""
                text "普通" size 20
                text "百合" size 20
                text "群交" size 20
                for tag in ("naked", "service", "sex", "anal", "fetish"):
                    text tag_button2_dict[tag] size 20
                    text format_stat(basic_stats[tag]) size 20
                    if tag == "naked":
                        text "-" size 20
                        text "-" size 20
                    else:
                        text format_stat(basic_stats[tag + " bisexual"]) size 20
                        text format_stat(basic_stats[tag + " group"]) size 20


            text "" size 20
            text "" size 20
            text "" size 20
            text "" size 20
            text "农场图片"

            for tag in ("big", "beast", "monster", "machine"):
                for tag2 in ("naked", "service", "sex", "anal", "fetish", "bisexual", "group"):
                    $ basic_stats[tag, tag2] = girl.count_pics([tag, tag2])

            grid 8 5 spacing 10:
                text ""
                for tag in ("naked", "service", "sex", "anal", "fetish", "bisexual", "group"):
                    text tag_button2_dict[tag] size 20

                for tag in ("big", "beast", "monster", "machine"):
                    text tag_button2_dict[tag] size 20
                    for tag2 in ("naked", "service", "sex", "anal", "fetish", "bisexual", "group"):
                        text format_stat(basic_stats[tag, tag2]) size 20

            text "" size 20
            text "可选图片"

            $ tags = filter(lambda x: x.tagsets.issubset(get_tagset(STANDARD_TAGSET).all_names), optional_tags) # <Chris12 - Tagsets />
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
                ysize 0.4
                xpos 0.1
                xsize 0.9
                xfill False
                yfill False

                grid 9 y_coord yspacing 0 xfill False:
                    text ""
                    for tag in ("total", "naked", "service", "sex", "anal", "fetish", "bisexual", "group"):
                        text tag_button2_dict[tag] size 12

                    for tag_def in tags:
                        $ tag = tag_def.name
                        text tag_button2_dict[tag]  size 12
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

            text "标有'-'的组合不计入人物包等级。" size 14 xalign 4

            hbox spacing 20 xalign 0.9:
                textbutton "提示" action Return("tips")
                textbutton "退出" action Return("quit") xalign 0.9


screen change_log:

    frame:
        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            xfill False
            yfill False

            has vbox spacing 10

            text "排序更改"

            for old, new in persistent.change_log.items():
                text "重命名 {b}{color=#ff4d4d}" + old + "{/color}{/b} (旧) 为 {b}{color=#7fffd4}" + str(new) + "{/color}{/b} (新)" size 12

            text ""

            hbox spacing 50:
                textbutton "保存更改" action Return("commit")
                textbutton "放弃更改" action Return("discard")


screen rating_tips():

    frame xalign 0.5 xmaximum 0.9 xpadding 20 ypadding 50 yalign 0.5 background "#dcebff":

        has vbox spacing 20 xmaximum 0.9

        $ text1 = ("{b}了解评级{/b}\n\n"
                + "有两个分数: '覆盖分数' (从 A 到 F) 和 '多样性分数' (+, 0或-)。请注意, 代码中的计算方法略有不同, 但为了便于解释, 我尽量让它保持简单.\n\n{b}覆盖得分{/b}:"
                + "\n\n游戏首先会检查你是否拥有包含至少一张图片的各种游戏情境:\n- 覆盖每一种主要类型得10分 ('profile', 'portrait', 'rest', 'waitress', 'dancer', 'masseuse', 'geisha') 以及它的变种 (衣服/裸体):总共最多140分\n- 每涉及一张性图片就得10分 ('service', 'sex', 'anal', 'fetish') 以及它的变种 (vanilla/群交/百合): 总共最多120分\n- 覆盖每个农场标签得到4分 ('big', 'beast', 'monster', 'machine') 以及它的变种 ('naked', 'service', 'sex', 'anal', 'fetish', 'bis', 'group'): 总共最多112分\n- 你为每个固定标签和它的变化得到4分 (确切的数字取决于喜欢什么)。总共不超过524分.\n"
                + "\n\n'A' 的分数意味着你至少占了896分的85%。'B' 分数意味着你有70-85%的最大值。'F' 分数意味着你低于30%。如你所见, 包括可选标记 (farm and fixations) 关键是获得更高的分数。只涵盖基本的标签将使您获得D."
                + "\n\n{b}多样性得分{/b}:\n\n游戏继续寻找图片的多样性, 即你的包里每个标签有多少张照片。到目前为止, 它只对主要的图片类型这样做 (soft and sex) 及其变化。它不考虑可选图片的多样性 (farm and fixations)。"
                + "\n\n如果你有平均5个不同的图片为每个主要的图片类型或更多, 你会得到一个a '+'。如果小于3, 就得到a '-'。"
                )

        text text1 size 18 color "#000099"

        textbutton "关闭" action Return() xalign 0.9


screen input_button(context):

    hbox spacing 15 xpos 0.22 ypos 0.05 xsize 0.64 xfill True:

        textbutton "搜索" text_size 18:
            action Return("search")

        if search_words:
            text search_words size 18

        if search_words or copy_tags:
            textbutton "清除复制" text_size 18:
                action Return("clear_search")

        if context == "edit":
            if copy_tags:
                textbutton "粘贴标签" text_size 18:
                    action Return("paste_tags")
            else:
                textbutton "复制标签" text_size 18:
                    action Return("copy_tags")

        if selected_pic != None and selected_pic.file in img_resolutions :
            text img_resolutions[selected_pic.file] size 18
