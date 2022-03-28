####            NEW SCREENS                 ####
##  Those are the screens specific to BKING   ##
##                                            ##
####                                        ####

## This script is long, redundant, and an utter mess. This is related to my severe lack of understanding of screen language in general. Sorry.


#### DECLARATIONS ####

image img_AP = ProportionalScale("UI/power.webp", 16, 16)
image img_AP_small = ProportionalScale("UI/power.webp", 12, 12)
image img_MP = ProportionalScale("UI/mana.webp", 16, 16)
image img_gold = ProportionalScale("UI/coin.webp", 16, 16)
image img_star = ProportionalScale("UI/star.webp", 16, 16)
image img_empty_star = ProportionalScale("UI/star_empty.webp", 16, 16)
image img_lock = ProportionalScale("UI/lock.webp", 80, 80)
image img_cust = ProportionalScale("UI/customer.webp", 20, 20)
image lines = ProportionalScale("perks/lines.webp", 800, 640)
image filter_all = ProportionalScale("UI/filters/all.webp", 30, 30)
image filter_weapon = ProportionalScale("UI/filters/weapon.webp", 30, 30)
image filter_clothing = ProportionalScale("UI/filters/clothing.webp", 30, 30)
image filter_trinket = ProportionalScale("UI/filters/trinket.webp", 30, 30)
image filter_consumable = ProportionalScale("UI/filters/consumable.webp", 30, 30)
image filter_misc = ProportionalScale("UI/filters/misc.webp", 30, 30)
image filter_all_unselect = im.MatrixColor(ProportionalScale("UI/filters/all.webp", 30, 30), im.matrix.desaturate())
image filter_weapon_unselect = im.MatrixColor(ProportionalScale("UI/filters/weapon.webp", 30, 30), im.matrix.desaturate())
image filter_clothing_unselect = im.MatrixColor(ProportionalScale("UI/filters/clothing.webp", 30, 30), im.matrix.desaturate())
image filter_trinket_unselect = im.MatrixColor(ProportionalScale("UI/filters/trinket.webp", 30, 30), im.matrix.desaturate())
image filter_consumable_unselect = im.MatrixColor(ProportionalScale("UI/filters/consumable.webp", 30, 30), im.matrix.desaturate())
image filter_misc_unselect = im.MatrixColor(ProportionalScale("UI/filters/misc.webp", 30, 30), im.matrix.desaturate())
image tb goal = ProportionalScale("UI/goal.webp", 50, 50)
image tb advance = ProportionalScale("NPC/Sill/portrait.webp", 30, 30)
image tb story = ProportionalScale("NPC/Kurohime/portrait.webp", 30, 30)
image tb other = ProportionalScale("NPC/Gio/portrait.webp", 30, 30)
image tb contract = im.Flip(ProportionalScale("NPC/Jobgirl/portrait.webp", 30, 30), horizontal=True)

image tb rest = ProportionalScale("backgrounds/rest.jpg", 100, 60)
image tb waitress = ProportionalScale("backgrounds/waitress.jpg", 100, 60)
image tb dancer = ProportionalScale("backgrounds/stripper.jpg", 100, 60)
image tb masseuse = ProportionalScale("backgrounds/masseuse.jpg", 100, 60)
image tb geisha = ProportionalScale("backgrounds/geisha.jpg", 100, 60)
image tb whore = ProportionalScale("backgrounds/whore.jpg", 100, 60)
image tb farm = ProportionalScale("brothels/farm/farm.jpg", 100, 60)

image success = ProportionalScale("UI/challenges/success.webp", config.screen_width, config.screen_height)
image failure = ProportionalScale("UI/challenges/failure.webp", config.screen_width, config.screen_height)


image girl_shadow = ProportionalScale("UI/girl_shadow.webp", 75, 75)

image tb wood = ProportionalScale("UI/fast buttons/wood.webp", 40, 40)
image tb wood grey = im.MatrixColor(ProportionalScale("UI/fast buttons/wood.webp", 40, 40), im.matrix.desaturate())
image tb leather = ProportionalScale("UI/fast buttons/leather.webp", 40, 40)
image tb leather grey = im.MatrixColor(ProportionalScale("UI/fast buttons/leather.webp", 40, 40), im.matrix.desaturate())
image tb dye = ProportionalScale("UI/fast buttons/dye.webp", 40, 40)
image tb dye grey = im.MatrixColor(ProportionalScale("UI/fast buttons/dye.webp", 40, 40), im.matrix.desaturate())
image tb silk = ProportionalScale("UI/fast buttons/silk.webp", 40, 40)
image tb silk grey = im.MatrixColor(ProportionalScale("UI/fast buttons/silk.webp", 40, 40), im.matrix.desaturate())
image tb marble = ProportionalScale("UI/fast buttons/marble.webp", 40, 40)
image tb marble grey = im.MatrixColor(ProportionalScale("UI/fast buttons/marble.webp", 40, 40), im.matrix.desaturate())
image tb ore = ProportionalScale("UI/fast buttons/ore.webp", 40, 40)
image tb ore grey = im.MatrixColor(ProportionalScale("UI/fast buttons/ore.webp", 40, 40), im.matrix.desaturate())
image tb diamond = ProportionalScale("UI/fast buttons/diamond.webp", 40, 40)
image tb diamond grey = im.MatrixColor(ProportionalScale("UI/fast buttons/diamond.webp", 40, 40), im.matrix.desaturate())

image tb renza = ProportionalScale("UI/fast buttons/renza.webp", 40, 40)
image tb renza grey = im.MatrixColor(ProportionalScale("UI/fast buttons/renza.webp", 40, 40), im.matrix.desaturate())
image tb captain = ProportionalScale("UI/fast buttons/captain.webp", 40, 40)
image tb captain grey = im.MatrixColor(ProportionalScale("UI/fast buttons/captain.webp", 40, 40), im.matrix.desaturate())

image tb banker = ProportionalScale("UI/fast buttons/banker.webp", 40, 40)
image tb bast = ProportionalScale("UI/fast buttons/bast.webp", 40, 40)
image tb giftgirl = ProportionalScale("UI/fast buttons/giftgirl.webp", 40, 40)
image tb gina = ProportionalScale("UI/fast buttons/gina.webp", 40, 40)
image tb goldie = ProportionalScale("UI/fast buttons/goldie.webp", 40, 40)
image tb gurigura = ProportionalScale("UI/fast buttons/gurigura.webp", 40, 40)
image tb katryn = ProportionalScale("UI/fast buttons/katryn.webp", 40, 40)
image tb papa = ProportionalScale("NPC/misc/freak portrait.jpg", 40, 40)
image tb ramias = ProportionalScale("UI/fast buttons/ramias.webp", 40, 40)
image tb riche = ProportionalScale("UI/fast buttons/riche.webp", 40, 40)
image tb stella = ProportionalScale("UI/fast buttons/stella.webp", 40, 40)
image tb twins = ProportionalScale("UI/fast buttons/twins.webp", 40, 40)
image tb willow = ProportionalScale("UI/fast buttons/willow.webp", 40, 40)


## STYLES

init:
    style inv_no_padding:
        background None
        xpadding 0
        ypadding 0
        xmargin 0
        ymargin 0

    style girlbutton:
        idle_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_darkorange + "CC", "#000")))
        selected_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize("#298ed6CC", "#000")))
        hover_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize("#69b0e2", "#000")))

    style girlbutton_blue:
        idle_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_darkorange + "CC", "#000")))
        selected_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize("#298ed6CC", "#000")))
        hover_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize("#69b0e2", "#000")))

    style girlbutton_light:
        idle_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_ui_light, "#000")))
        selected_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_orange, "#000")))
        hover_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_lightorange, "#000")))


## TOP OVERLAY (displays time, money, help button...)

screen tax_tooltip():
    zorder 11
    tag tax_tooltip

    if NPC_taxgirl.current_tax:
        use tax_tab()

    elif NPC_taxgirl.active:
        frame background c_ui_dark:
            xalign 0.5
            yalign 0.1

            hbox:
                spacing 10

                add ProportionalScale("NPC/taxgirl/portrait.webp", 35, 35) yalign 0.5

                text "无需缴纳公会费用." xalign 0.0 yalign 0.5 size 14 color c_emerald


screen tax_tab(fade=False):
    zorder 11
    frame background c_ui_dark:

        if fade:
            at fademove([0.5, 0.5], [0.5, 0.0])
        else:
            xalign 0.5
            yalign 0.1

        hbox:

            spacing 10

            add ProportionalScale("NPC/taxgirl/portrait.webp", 35, 35) yalign 0.5

            if calendar.day in (28, 7):
                $ due_date = "tomorrow"
            elif calendar.day in (1, 8):
                $ due_date = "tonight"
            elif calendar.day >= 15:
                $ due_date = "in %s days" % (29-calendar.day)
            else: # Tax due date has been extended by a week
                $ due_date = "in %s days" % (8-calendar.day)

            vbox:
                text "公会费用" bold True size 14
                text "{image=img_gold} " + '{:,}'.format(round_int(NPC_taxgirl.current_tax)).replace(',', ' ') + " due %s." % due_date xalign 0.0 yalign 0.5 size 14 color c_red


screen overlay(current_screen = None, kwargs = None):

    zorder 11

    frame:
        id "ol"

        background c_ui_dark
        xsize 1.0
        ysize int(0.075*config.screen_height)
        xpadding 20

        has hbox

        xfill True
        yfill True

        button background None xalign 0.0 yalign 0.5 action NullAction():

            tooltip ("{size=-1}当前日期{/size}\n" + moons[calendar.month].short_description)

#             if calendar.moon:
#             else:
#                 tooltip "The current date."

            hbox:
                spacing 10

                text "[calendar.year]年" size 16
                text "[calendar.month]月" size 16
                text ("[calendar.day]日(" + setting_name_dict[calendar.get_weekday()][:3] + ")") size 16


        hbox:
            spacing 6
            xalign 0.15
            yalign 0.5

            button background None xalign 0.0 yalign 0.5 action NullAction():
                if game.chapter > 1:
                    tooltip "{size=-1}你可用金币. 其他资源:{/size}"
                    hovered (Show("resource_tab", x=0.625, y=0.025), Show("tax_tooltip", transition=Dissolve(0.15)))
                    unhovered (Hide("resource_tab"), Hide("tax_tooltip", transition=Dissolve(0.15)))
                else:
                    tooltip "你可用金币..."

                hbox:

                    spacing 10

                    add ProportionalScale("UI/coin.webp", 20, 20) yalign 0.5

                    text '{:,}'.format(round_int(MC.gold)).replace(',', ' ') xalign 0.0 yalign 0.5 size 18


            button background None xalign 0.0 yalign 0.5 tooltip "行动力: 今天剩余行动力." action NullAction():

                has hbox

                spacing 5

                add ProportionalScale("UI/power.webp", 20, 20) yalign 0.5

                text str(round_int(MC.interactions)) xalign 0.0 yalign 0.5 size 18

            button background None xalign 0.0 yalign 0.5 tooltip "魔法值: 今天剩余魔法值." action NullAction():

                has hbox

                spacing 5

                add ProportionalScale("UI/mana.webp", 20, 20) yalign 0.5

                text str(round_int(MC.mana)) xalign 0.0 yalign 0.5 size 18

        frame background None xsize 200

        textbutton "?" tooltip "了解更多关于当前屏幕的信息.":

            xalign 1.0
            yalign 0.5

            if current_screen:
                action renpy.curried_invoke_in_new_context(help, current_screen, kwargs) #renpy.call("help", scr = current_screen) #





## GIRL TAB

screen girls(girls, context = "girls"): # context can be girls, slavemarket, farm

    #<Chris12 PredictImages>
    if context != "farm":
        $ predict_images(girls, predict_portraits = False) # Portraits will be loaded directly, anyway. Also, they already get predicted in right_menu().
    #</Chris12 PredictImages>

    tag girls

    if not girls_firstvisit:
        key "mouseup_3" action (SetVariable("choice_menu_girl_interact", False), SetVariable("selected_destination", "main"), Jump("teleport"))
        use close((SetVariable("choice_menu_girl_interact", False), SetVariable("selected_destination", "main"), Jump("teleport")))
        use shortcuts()

#    if selected_girl:
#        text selected_girl.name color c_red

    use girl_tab(girls, context=context)

    if selected_girl in girls:
        use girl_stats(selected_girl, context=context)

        use button_overlay(selected_girl, context=context)

        use girl_profile(selected_girl, context=context)


screen girl_tab(girls, context="girls"):

    zorder -10

    tag girl_tab

    if context == "slavemarket":

############ Jman - Headhunter Mod ############
        if game.has_active_mod("Headhunter Mod"):
            if game.headhunter_button_enabled:
                key "shift_H" action Jump("headhunter_main")
            $ textHH = "猎头公司" #

            $ textHH2 = "订购具有特定特征的奴隶，以增加成本."

            if game.headhunter_button_enabled:
                textbutton textHH:
                    xalign 0.5
                    yalign 0.99
                    text_size 36
                    text_font "CHOWFUN_0.TTF"
                    action Jump("headhunter_main")
                    hovered tt.Action(textHH2)

            else:
                textbutton textHH:
                    xalign 0.5
                    yalign 0.99
                    text_size 36
                    text_font "CHOWFUN_0.TTF"
                    hovered tt.Action(textHH2)

############ Jman - Headhunter Mod End ########

        use overlay("slavemarket")
        $ sorters = ["rank", "experience", "alpha"]

    elif context == "girls":
        use overlay("girls")
        $ sorters = ["rank", "level", "job", "alpha", "badge"]

        if selected_girl:
            key "alt_K_UP" action [Function(move_up_list, girls, selected_girl)]
            key "alt_K_DOWN" action [Function(move_down_list, girls, selected_girl)]

    elif context == "farm":
        $ sorters = ["rank", "level", "alpha", "badge"]

    $ ylist = {"x40" : 65*10, "x24" : 85*8, "x12" : 105*6, "x4" : 133*4}

    if selected_view_mode == "x40" or (selected_view_mode == "Auto" and len(girls) > 24):
        $ bsize = "x40"
        $ c = 4

    elif selected_view_mode == "x24" or (selected_view_mode == "Auto" and len(girls) > 12):
        $ bsize = "x24"
        $ c = 3

    elif selected_view_mode == "x12" or (selected_view_mode == "Auto" and len(girls) > 4):
        $ bsize = "x12"
        $ c = 2

    else:
        $ bsize = "x4"
        $ c = 1

    if len(girls) > 24:
        $ view_modes = ["x4", "x12", "x24", "x40"]

    elif len(girls) > 12:
        $ view_modes = ["x4", "x12", "x24"]

    elif len(girls) > 4:
        $ view_modes = ["x4", "x12"]

    else:
        if selected_view_mode == "x4":
            $ view_modes = None
        else:
            $ view_modes = ["x4"]


    $ y = ylist[bsize]


    vbox:
        xalign 1.0
        ypos 0.075
        xsize 325
        if selected_view_mode != "Auto":
            ysize ylist[selected_view_mode]
        else:
            ysize y

        hbox xalign 0.1:
            use sorting_tab(context, girls, sorters)

            if view_modes:
                $ _next = get_next(view_modes, selected_view_mode, True)

                frame xsize 38 ysize 20 xpadding 0 ypadding 0 xmargin 0 ymargin 0:
                    textbutton selected_view_mode text_italic True text_color c_darkbrown text_size 14 xpadding 0 ypadding 0 xalign 0.5 yalign 0.6 xsize 38 ysize 20 idle_background None:
                        action SetVariable("selected_view_mode", _next)
                        tooltip "单击以更改视图模式"

        frame:

            id "girl_tab"

            xmargin 3
            xpadding 0
            xfill True
            yfill True

            if girls:
                if girls and not girls_firstvisit:
                    key "K_UP" action [Function(select_previous_girl, girls, False, pace=c), Hide("rank_level_details"), Hide("mood_details"), Hide("sex_details"), Hide("trait_details"), Hide("perk_details")]

                    key "K_DOWN" action [Function(select_next_girl, girls, False, pace=c), Hide("rank_level_details"), Hide("mood_details"), Hide("sex_details"), Hide("trait_details"), Hide("perk_details")]

                    key "repeat_K_UP" action [Function(select_previous_girl, girls, False, pace=c), Hide("rank_level_details"), Hide("mood_details"), Hide("sex_details"), Hide("trait_details"), Hide("perk_details")]

                    key "repeat_K_DOWN" action [Function(select_next_girl, girls, False, pace=c), Hide("rank_level_details"), Hide("mood_details"), Hide("sex_details"), Hide("trait_details"), Hide("perk_details")]

                    if c > 1:

                        key "K_LEFT" action [Function(select_previous_girl, girls, False), Hide("rank_level_details"), Hide("mood_details"), Hide("sex_details"), Hide("trait_details"), Hide("perk_details")]

                        key "K_RIGHT" action [Function(select_next_girl, girls, False), Hide("rank_level_details"), Hide("mood_details"), Hide("sex_details"), Hide("trait_details"), Hide("perk_details")]

                        key "repeat_K_LEFT" action [Function(select_previous_girl, girls, False), Hide("rank_level_details"), Hide("mood_details"), Hide("sex_details"), Hide("trait_details"), Hide("perk_details")]

                        key "repeat_K_RIGHT" action [Function(select_next_girl, girls, False), Hide("rank_level_details"), Hide("mood_details"), Hide("sex_details"), Hide("trait_details"), Hide("perk_details")]

                vpgrid:
                    cols c
                    draggable True
                    mousewheel True

                    scrollbars "vertical"

                    side_xalign 0.0
                    xalign 0.5
                    xfill True
                    yfill True

                    yadjustment vp_adj

                    for girl in girls:
                        use girl_button(girl, bsize, status_list=girl_status_dict[girl], context=context)
            else:
                text "{i}  没有女孩  {/i}" size 18 color c_brown


screen girl_pick_badge(girl):

    modal True
    key "mouseup_3" action Return()

    use dark_filter

    frame xalign 0.5 yalign 0.5 xpadding 20 ypadding 20:
        has vbox

        text "为[girl.fullname]选择一个徽章" color c_darkorange

        text ""

        vpgrid xalign 0.5:
            cols 3
            spacing 5
            draggable True
            mousewheel True

            for i in xrange(len(badge_pics)):
                button xsize 80 ysize 80:
                    if i == 0:
                        action (SetField(girl, "badge", None), Return())
                        tooltip "没有徽章"
                    else:
                        action (SetField(girl, "badge", badge_pics[i]), Return())
                        tooltip "挑选这个徽章"
                    add ProportionalScale(badge_pics[i], 60, 60) xalign 0.5 yalign 0.5


screen badge_button(girl, _size, t_size=20, active=True): # Where badge is a file name or None
    $ badge = girl.get_badge()

    if not badge:
        if active:
            textbutton "+" xmargin 0 ymargin 0 xpadding 0 ypadding 0 background None xalign 0.9 yalign 0.1 text_size t_size tooltip "为这个女孩添加自定义徽章. 定制徽章不做任何事情，它们是为了你自己的方便.":
                action Return(("badge", girl))
                text_color c_white
                text_drop_shadow (1, 1)

    else:
        $ badge_name = badge.rsplit(".", 1)[0]
        button xmargin 0 ymargin 0 xpadding 0 ypadding 0 background None xalign 0.9 yalign 0.1 tooltip "目前的徽章: {b}%s{/b}.\n点击改变该女孩的自定义徽章." % badge_name:
            if active:
                action Return(("badge", girl))
            add ProportionalScale(badge, _size, _size)


screen girl_button(girl, bsize="x4", status_list=[], context="girls", extra_action=[]):

    $ sel_col = c_emerald + "CC"

    if context == "girls":
        if girl.job:
            if girl.job:
                $ text1 = girl_related_dict[girl.job.capitalize()]
                $ but_ttip = "{b}" + girl.fullname + "{/b}是个等级" + str(girl.level) + "的" + girl_related_dict[girl.job.capitalize()] + "."
                if girl.job in all_jobs and girl.work_whore:
                    $ text1 += "\n{color=[c_red]}妓女{/color}"
                    $ but_ttip = "{b}" + girl.fullname + "{/b}是个等级" + str(girl.level) + "的" + girl_related_dict[girl.job.capitalize()] + "并兼职妓女."
        else:
            $ text1 = "无工作"
            $ but_ttip = "{b}" + girl.fullname + "{/b}正在休息."
        $ text_col = job_color[girl.job]

    elif context == "farm":
        if farm.programs[girl].target != "no training":
            $ text1 = farm_related_dict[farm.programs[girl].target.capitalize()]
            $ but_ttip = "{b}" + girl.fullname + "{/b}在农场训练(" + text1 + ")."
            $ text_col = c_orange
        else:
            $ text1 = farm_related_dict[farm.programs[girl].holding.capitalize()]
            $ but_ttip = "{b}" + girl.fullname + "{/b}在农场待机(" + text1 + ")."
            $ text_col = c_white

    elif context == "slavemarket":
        $ text1 = experienced_description[girl.sexual_experience]
        $ text2 = "{b}"+str(girl.get_price("buy")) + "{/b}{size=-4}金币{/size}"
        $ but_ttip = "购买{b}" + girl.fullname + "{/b}需要" + text2 + "."
        $ text_col = experienced_color[girl.sexual_experience]

    if bsize == "x40":
        button:
            xsize 75
            ysize 60
            xalign 0.5
            yalign 0.5
            xpadding 2
            ypadding 2
            style "girlbutton"
            action [SetVariable("selected_girl", girl), SelectedIf(selected_girl==girl)] + extra_action
            tooltip but_ttip

            # hovered ToggleLocalVariable("badge_but")
            # unhovered ToggleLocalVariable("badge_but")

            frame xsize 45 ysize 45 xmargin 0 ymargin 0 xpadding 2 yalign 1.0:

                has hbox yalign 0.5 xfill True yfill True

                fixed xalign 0.5 yalign 0.5:
                    add girl.portrait.get(36, 36) xalign 0.5 yalign 0.5

                    if context in ("girls", "farm"):
                        use badge_button(girl, 20, 18, active=persistent.badges_on_portraits)

                button style "inv_no_padding" action SetVariable("selected_girl", girl) xalign 1.0 yalign 1.0:
                    tooltip "她还有" + str_int(girl.energy) + "点精力，其当前精力上限是" + str(int(girl.get_stat_minmax("energy")[1])) + "."
                    vbar value girl.energy range girl.get_stat_minmax("energy")[1]:
                        thumb None
                        thumb_offset 0
                        top_gutter 0
                        left_bar Frame ("UI/cryvslider_empty.webp", 10, 0)
                        right_bar Frame ("UI/cryvslider_full.webp", 10, 0)
                        xsize 6
                        ysize 36

            text text1[:3] bold True size 11 color text_col drop_shadow (1, 1):
                xalign 0.05
                yalign 0.95

            hbox:
                spacing 3
                xalign 0.05

                hbox spacing 3 xalign 1.0:
                    text "阶级" size 11  drop_shadow (1, 1)
                    text rank_name[girl.rank] size 14 bold True drop_shadow (1, 1)
                hbox spacing 3 xalign 1.0:
                    text "等级" size 11  drop_shadow (1, 1)
                    text str(girl.level) size 14 bold True drop_shadow (1, 1)

            frame:
                background None
                xpos 40
                yalign 1.0
                xmargin 1
                ymargin 2
                ypadding 0

                has vbox spacing 0 ymaximum 50 box_wrap True

                if context == "slavemarket":
                    text text2 size 12 bold True

                else:
                    if len(status_list) > 3:
                        $ i = 2
                    else:
                        $ i = 3

                    for pic, ttip in status_list[:i]:
                        button style "inv_no_padding":
                            action SetVariable("selected_girl", girl)
                            tooltip ttip
                            add ProportionalScale("UI/status/" + pic, 15, 15)

                    if i == 2:
                        text "..." size 10 bold True xalign 0.5 yoffset -4 tooltip girl_status_dict[girl, "summary"]

    elif bsize == "x24":
        button:
            xsize 100
            ysize 80
            xalign 0.5
            yalign 0.5
            xpadding 3
            ypadding 3
            style "girlbutton"
            action [SetVariable("selected_girl", girl), SelectedIf(selected_girl==girl)] + extra_action
            tooltip but_ttip

            frame xsize 70 ysize 70 xmargin 0 ymargin 0 xpadding 2 yalign 1.0:
                has hbox yalign 0.5 xfill True yfill True

                fixed xalign 0.5 yalign 0.5 fit_first True:
                    add girl.portrait.get(56, 56) xalign 0.5 yalign 0.5

                    if context in ("girls", "farm"):
                        use badge_button(girl, 25, 20, active=persistent.badges_on_portraits)

                button style "inv_no_padding" action SetVariable("selected_girl", girl) xalign 1.0 yalign 0.5:
                    tooltip "精力：{b}" + str_int(girl.energy) + "{/b}/" + str(int(girl.get_stat_minmax("energy")[1]))
                    vbar value girl.energy+1 range girl.get_stat_minmax("energy")[1]:
                        thumb None
                        thumb_offset 0
                        top_gutter 0
                        left_bar Frame ("UI/cryvslider_empty.webp", 10, 0)
                        right_bar Frame ("UI/cryvslider_full.webp", 10, 0)
                        xsize 8
                        ysize 42

            text text1 bold True size 12 color text_col drop_shadow (1, 1):
                xalign 0.05
                yalign 0.95

            hbox:
                spacing 3
                xalign 0.05

                hbox spacing 3 xalign 1.0:
                    text "阶级" size 12  drop_shadow (1, 1)
                    text rank_name[girl.rank] size 16 bold True  drop_shadow (1, 1)
                hbox spacing 3 xalign 1.0:
                    text "等级" size 12  drop_shadow (1, 1)
                    text str(girl.level) size 16 bold True  drop_shadow (1, 1)

            frame:
                background None
                xpos 64
                yalign 1.0
                xmargin 1
                ymargin 2
                ypadding 0

                has vbox spacing 0 ymaximum 70 box_wrap True

                if context == "slavemarket":
                    text text2 size 14 bold True

                else:
                    if len(status_list) > 3:
                        $ i = 2
                    else:
                        $ i = 3
                    for pic, ttip in status_list[:i]:
                        button style "inv_no_padding":
                            action SetVariable("selected_girl", girl)
                            tooltip ttip
                            add ProportionalScale("UI/status/" + pic, 20, 20)

                    if i == 2:
                        text "..." size 10 bold True xalign 0.5 yoffset -4 tooltip girl_status_dict[girl, "summary"]


    elif bsize == "x12":
        button:
            xsize 150
            ysize 100
            xalign 0.5
            yalign 0.5
            xpadding 3
            ypadding 3
            style "girlbutton"
            action [SetVariable("selected_girl", girl), SelectedIf(selected_girl==girl)] + extra_action
            tooltip but_ttip

            frame xsize 90 ysize 90 xmargin 0 ymargin 0 yalign 1.0:
                has hbox yalign 0.5 xfill True yfill True

                fixed xalign 0.5 yalign 0.5:
                    add girl.portrait.get(75, 75) xalign 0.5 yalign 0.6

                    if context in ("girls", "farm"):
                        use badge_button(girl, 30, 24, active=persistent.badges_on_portraits)

                button style "inv_no_padding" action SetVariable("selected_girl", girl) xalign 1.0 yalign 1.0:
                    tooltip "精力：{b}" + str_int(girl.energy) + "{/b}/" + str(int(girl.get_stat_minmax("energy")[1]))
                    vbar value girl.energy range girl.get_stat_minmax("energy")[1]:
                        thumb None
                        thumb_offset 0
                        top_gutter 0
                        left_bar Frame ("UI/cryvslider_empty.webp", 10, 0)
                        right_bar Frame ("UI/cryvslider_full.webp", 10, 0)
                        xsize 10
                        ysize 75

            if len(girl.fullname) <= 10:
                $ text3 = girl.fullname
            else:
                $ text3 = girl.name[0] + ". " + girl.lastname

            text text3 size 16 drop_shadow (1, 1) font "maturasc.TTF" xalign 0.05

            text text1 bold True size 14 color text_col drop_shadow (1, 1):
                xalign 0.05
                yalign 0.95


            vbox:
                spacing 0
                xalign 0.95
                yalign 0.25

                hbox spacing 3 xalign 1.0:
                    text "阶级" size 11
                    text rank_name[girl.rank] size 14 bold True drop_shadow (1, 1)
                hbox spacing 3 xalign 1.0:
                    text "等级" size 11
                    text str(girl.level) size 14 bold True drop_shadow (1, 1)

            frame:
                background None
                xpos 90
                yalign 1.0
                xmargin 2
                ymargin 3
                xpadding 0
                ypadding 0

                has hbox spacing 1 box_wrap True xsize 50

                if context == "slavemarket":
                    text text2 size 16 bold True

                else:
                    if len(status_list) > 4:
                        $ i = 3
                    else:
                        $ i = 4

                    for pic, ttip in status_list[:i]:
                        button style "inv_no_padding":
                            action SetVariable("selected_girl", girl)
                            tooltip ttip
                            add ProportionalScale("UI/status/" + pic, 22, 22)

                    if i == 3:
                        text "..." size 11 bold True xalign 0.5 yoffset -4 tooltip girl_status_dict[girl, "summary"]


    elif bsize == "x4":
        button:
            xsize 310
            ysize 125
            xalign 0.5
            yalign 0.5
            xpadding 8
            style "girlbutton"
            action [SetVariable("selected_girl", girl), SelectedIf(selected_girl==girl)] + extra_action
            tooltip but_ttip

            frame xsize 120 ysize 120 ymargin 3 yalign 1.0:
                has hbox yalign 0.5 xfill True yfill True

                fixed xalign 0.5 yalign 0.5:
                    add girl.portrait.get(96, 96) yalign 0.5

                    if context in ("girls", "farm"):
                        use badge_button(girl, 40, 32, active=persistent.badges_on_portraits)

                button style "inv_no_padding" action SetVariable("selected_girl", girl) xalign 1.0 yalign 1.0:
                    tooltip "精力：{b}" + str_int(girl.energy) + "{/b}/" + str(int(girl.get_stat_minmax("energy")[1]))
                    vbar value girl.energy range girl.get_stat_minmax("energy")[1]:
                        thumb None
                        thumb_offset 0
                        top_gutter 0
                        left_bar Frame ("UI/cryvslider_empty.webp", 10, 0)
                        right_bar Frame ("UI/cryvslider_full.webp", 10, 0)
                        xsize 12
                        ysize 85

            text girl.fullname drop_shadow (1, 1) font "maturasc.TTF"

            text text1 bold True size 15 color text_col drop_shadow (1, 1):
                xpos 125
                yalign 0.4

            vbox:
                spacing 6
                xalign 1.0
                yalign 0.1

                hbox spacing 6:
                    text "阶级" size 14
                    text rank_name[girl.rank] bold True drop_shadow (1, 1)
                hbox spacing 6:
                    text "等级" size 14
                    text str(girl.level) bold True drop_shadow (1, 1)

            frame:
                background None
                xpos 125
                xpadding 0
                yalign 1.0
                ymargin 3


                has hbox

                if context == "slavemarket":
                    text text2 size 18 bold True

                else:
                    if len(status_list) > 5:
                        $ i = 4
                    else:
                        $ i = 5

                    for pic, ttip in status_list[:i]:
                        button style "inv_no_padding":
                            action SetVariable("selected_girl", girl)
                            tooltip ttip
                            add ProportionalScale("UI/status/" + pic, 36, 36)

                    if i == 4:
                        text "..." size 12 bold True xalign 0.5 yoffset -4 tooltip girl_status_dict[girl, "summary"]

screen girl_fast_actions(girl, notebook=True, love_fear=True, schedule=True, customers=True, bg=None):

    frame:
        xalign 0.5
        yalign 1.0
        yanchor 0.0
        xminimum 180
        xmaximum int(12 + config.screen_width // 2.8) # Makes it the same size as the girl profile pic
        ysize 62
        xmargin 0
        xpadding 6
        ymargin 0
        ypadding 0

        if bg:
            background bg

        has hbox spacing 5 xfill True yfill True

        if schedule:
            button yalign 0.5 xmargin 0 xpadding 3 ymargin 0 ypadding 3 action Return("sched") tooltip "Open " + girl.fullname + "'s schedule":
                add "UI/calendar.webp" zoom 0.4 #idle_alpha 0.66 hover_alpha 1.0
        else:
            null

        if notebook:
            if MC.get_effect("special", "notebook"):
                button action Show("notebook") xmargin 0 xpadding 3 ymargin 0 ypadding 3 yalign 0.5 tooltip "Open " + girl.name + "'s entry in your magical notebook":
                    add "items/misc/magic notebook.webp" zoom 0.4 #idle_alpha 0.5 hover_alpha 1.0
        else:
            null

        if love_fear:
            hbox spacing 3 xsize 73 yalign 0.5:
                use love_button(girl)
                use fear_button(girl)
        else:
            null
            null

        if customers and district.rank > 1:
            frame background c_ui_dark xmargin 0 xpadding 0 ymargin 0 ypadding 0 xfill False xalign 1.0 yalign 0.5:
                has hbox spacing 1 box_wrap True xmaximum 156
                for pop in all_populations:
                    if brothel.get_effect("allow", pop.name):
                        if girl.refused_populations[pop.name]:
                            $ X_text = "{b}X{/b}"
                            $ ttip = "单击允许" + pop.description
                        else:
                            $ X_text = ""
                            $ ttip = "单击阻止" + pop.description
                        button xsize 25 ysize 25 xmargin 0 xpadding 0 ymargin 0 ypadding 0 background None yalign 0.5:
                            action (ToggleDict(girl.refused_populations, pop.name), girl.customer_populations_safety_check(pop.name))
                            tooltip ttip
                            add pop.get_pic(25, 25) xalign 0.5 yalign 0.5
                            text X_text color c_crimson size 24 xalign 0.5 yalign 0.5



screen girl_profile(girl, context = None): # context can be girls, slavemarket, farm, free

    tag girl_profile
    zorder 0

    fixed:
        fit_first True
        xalign 0.5
        ypos 0.1
        xfill True
        yfill False

        if girl.profile != None:
            frame xpadding 6 ypadding 6 xalign 0.5 yfill False:
                add girl.profile.get(config.screen_width//2.8, config.screen_height*2//3) xalign 0.5

            if context == "farm":
                frame background c_ui_dark:
                    xmaximum int(12 + config.screen_width // 2.8) # Makes it the same size as the girl profile pic
                    yminimum int(0.4*config.screen_height)
                    ymaximum config.screen_height*2//3.5
                    yalign 1.0

                    has vbox
                    spacing 12
                    xfill True
                #
                #     #!
                #
                # hbox spacing 20 xfill True:
                #     if MC.get_effect("special", "notebook"):
                #         button background None action Show("notebook") xalign 0.0 xmargin 10 xpadding 0 hovered tt.Action("Open " + girl.name + "'s entry in your magical notebook"):
                #             add "items/misc/magic notebook.webp" zoom 0.5 idle_alpha 0.66 hover_alpha 1.0
                #
                #     text girl.fullname bold True size 18 xalign 0.0 yalign 0.5
                    #
                    # frame xalign 1.0 xmargin 10 ymargin 10:
                    #     has hbox spacing 6
                    #     use love_button(girl)
                    #     use fear_button(girl)
                #
                # text ""

                    text farm.programs[girl].name bold True size 18 xalign 0.5 yalign 0.5

                    text "" size 18

                    hbox xalign 0.5 box_wrap True:
                        textbutton "改变设定" text_size 16 action Return(("change program", girl)) tooltip "更改" + girl.name + "当前的训练设定."
                        if farm.programs[girl].target != "no training":
                            textbutton "改变模式" text_size 16 action Return(("change mode", girl)) hovered tt.Action("更改" + girl.name + "当前的训练模式.")

                    text "" size 18

                    if farm.programs[girl].target != "no training":
                        hbox:
                            textbutton "训练模式:" xsize 0.7 xfill True text_xalign 0 text_size 14 background None text_color c_white xpadding 0 xmargin 0.05 ypadding 0 ymargin 0 action NullAction() hovered tt.Action("决定Gizel是否会强迫女孩们违心地训练.")
                            text farm_related_dict[farm.programs[girl].mode.capitalize()] size 14 bold True

                        hbox:
                            textbutton "训练设施:" xsize 0.7 xfill True text_xalign 0 text_size 14 background None text_color c_white xpadding 0 xmargin 0.05 ypadding 0 ymargin 0 action NullAction() hovered tt.Action("决定她的培训要使用的设施(如果有).")
                            text farm_related_dict[farm.programs[girl].installation_name.capitalize()] size 14 bold True

                    else:
                        hbox:
                            textbutton "待机模式:" xsize 0.7 xfill True text_xalign 0 text_size 14 background None text_color c_white xpadding 0 xmargin 0.05 ypadding 0 ymargin 0 action NullAction() hovered tt.Action("决定女孩不训练(工作或休息)时会做什么.")
                            text farm_related_dict[farm.programs[girl].holding.capitalize()] size 14 bold True

                    hbox:
                        if farm.programs[girl].duration >= 0:
                            textbutton "持续时间:" xsize 0.7 xfill True text_xalign 0 text_size 14 background None text_color c_white xpadding 0 xmargin 0.05 ypadding 0 ymargin 0 action NullAction() hovered tt.Action("决定她的逗留期限.")
                            text str(farm.programs[girl].duration) + "天" size 14 bold True

                    text "" size 18

                    if farm.programs[girl].target != "no training":

                        if farm.programs[girl].target in farm.knows["reaction"][girl] and farm.programs[girl].target != "auto":

                            $ reaction = girl.will_do_farm_act(farm.programs[girl].target)

                            if reaction == "accepted":
                                $ text1 = event_color["good"] % "Gize认为她接受这个训练不会有任何问题."
                            elif reaction == "resisted":
                                $ text1 = event_color["a little bad"] % "Gizel认为她不愿意训练这种行为，需要一点说服力(需要强硬模式)."
                            elif reaction == "refused":
                                $ text1 = event_color["a little bad"] % "Gizel认为她会拒绝这种行为，除非她屈服(需要强硬模式)."

                        else:
                            $ text1 = "Gizel不确定" + girl.name + "会对这次训练有什么反应."

                    else:
                        $ text1 = "[girl.name]永远不会抗拒这一点."

                    text text1 size 14 italic True xalign 0.5

            if (context == "girls" and not girls_firstvisit) or context == "free" or context == "farm":

                # if not girls_firstvisit or context == "free" or context == "farm":
                vbox xalign 0.0 yalign 0.0 spacing 6:

                    if context == "girls":
                        key "d" action Return("sched")
                        button background None xmargin 10 ymargin 10 xpadding 0 action Return("sched") tooltip "打开" + girl.fullname + "的排班表(快捷键: {u}d{/u})":
                            add "UI/calendar.webp" zoom 0.5 idle_alpha 0.66 hover_alpha 1.0

                    if MC.get_effect("special", "notebook"):
                        key "n" action Show("notebook")
                        button background None xmargin 10 xpadding 0 action Show("notebook") tooltip "在你的笔记本中打开" + girl.fullname + "的相关内容(快捷键: {u}n{/u})":
                            add "items/misc/magic notebook.webp" zoom 0.5 idle_alpha 0.66 hover_alpha 1.0

                vbox xalign 1.0:
                    frame xmargin 10 ymargin 10:
                        has hbox spacing 6
                        use love_button(girl)
                        use fear_button(girl)

                    frame xalign 0.5 xmargin 10 ymargin 10 background None:
                        use badge_button(girl, 48, 40)

                if context == "girls" and district.rank > 1:
                    use girl_fast_actions(girl, notebook=False, love_fear=False, schedule=False, customers=True)

            if persistent.show_girlpack_rating:
                if context == "slavemarket" or persistent.show_girlpack_rating=="Everywhere":
                    $ rating, ttip = get_girlpack_rating(girl)

                    textbutton "女孩图片包评级(" + capitalize(girl.path.split("/")[-1]) + "): " + rating background c_ui_darkblue text_size 18 yalign 1.0 xmargin 10 ymargin 10 action NullAction() tooltip ttip


screen girl_stats(girl, context = "girls"): # context can be girls, slavemarket, farm, free, postings, contracts, capture

    tag gst

    zorder -9

    frame:
        xalign 0.0

        if context not in ("postings"):
            ypos 0.1

        xmargin 6
        xpadding 6
        xfill True
        xsize 320

        if context == "farm":
            background c_ui_dark
        else:
            background c_ui_darkblue

        vbox:

            spacing 3

            hbox:

                xfill True

                if len(girl.fullname) > 23:
                    $ text1 = girl.fullname[:20] + "..."
                else:
                    $ text1 = girl.fullname

                textbutton text1:
                    xalign 0.0
                    background None
                    text_color c_white

                    if context == "girls":

                        action (SetVariable("selected_girl", girl), Return("change_name"))
                        hovered tt.Action("单击此处更改她的名字")

                    elif context == "farm":
                        action Return(("change_name", girl))
                        hovered tt.Action("单击此处更改她的名字")

                    xmargin 0
                    ymargin 0
                    xpadding 3
                    ypadding 0


                if context in ("girls", "farm"):

                    frame:

                        background None
                        xmargin 0
                        ymargin 0
                        xpadding 0
                        ypadding 0
#                        xsize 45
                        xalign 1.0
                        yalign 1.0
                        xfill False

                        has hbox

                        spacing 6
                        xfill False

                        # Add defense meter

                        $ defense = girl.get_defense()

                        if defense <= 0:
                            $ ttip = "{b}无助"
                        elif defense <= 3:
                            $ ttip = "{b}羸弱"
                        elif defense <= 6:
                            $ ttip = "{b}胜任"
                        elif defense <= 9:
                            $ ttip = "{b}强力"
                        else:
                            $ ttip = "{b}致命"

                        $ ttip += "{/b}\n她的自卫能力有多强. 通过给她一件武器来提高这一点."

                        button:

                            xmargin 0
                            ymargin 0
                            xpadding 0
                            ypadding 0
                            xsize 20
                            ysize 20
                            xalign 0.0
                            yalign 1.0
                            background None

                            action NullAction()
                            hovered tt.Action(ttip)

                            add ProportionalScale("UI/defense.webp", 20, 20) xalign 0.5 yalign 0.5

                            text str(round_int(defense)) size 12 xalign 0.5 yalign 0.5 color c_white


                        button background None action NullAction() hovered (Show("mood_details", girl=girl, transition=Dissolve(0.15)), tt.Action(girl.get_mood_description("mood"))) unhovered Hide("mood_details", transition=Dissolve(0.15)):

                            xalign 0.0
                            yalign 0.7
                            xmargin 0
                            ymargin 0
                            xpadding 0
                            ypadding 0

                            add ProportionalScale(girl.get_mood_picture(), 16, 16)


            if context in ("girls", "farm", "contract", "postings"):

                # Levels and rank info

                button:

                    xalign 0.0

                    background None
                    action NullAction()
                    hovered Show("rank_level_details", girl = girl, transition = dissolve)
                    unhovered Hide("rank_level_details", transition = dissolve)

                    has hbox
                    xfill True
                    spacing 10

                    #Rank

                    $ rank_text = "阶级" + rank_name[girl.rank]

    #                $ rank_ttip = "Reputation: " + str(round_int(girl.rep)) + "/" + str(girl.get_rep_cap())

    #                if girl.rank >= str(district.rank):

    #                    $ rank_ttip += "{b}Max rank reached.{/b}\n"

    #                $ rank_ttip += "\nRank affects many aspects of the game, including maximum level and skill values."

                    use mybar(labl = rank_text, val = (girl.rep - rep_to_rank[girl.rank - 1]), _max = (girl.get_rep_cap() - rep_to_rank[girl.rank - 1]), col = c_softpurple, x = 65)


                    #Level

                    $ level_text = "等级"+ str(girl.level)
    #                $ level_ttip = "Xp: " + str(round_int(girl.xp)) + "/" + str(girl.get_xp_cap())
    #                $ level_ttip += "       Max level: {b}" + str(girl.rank * 5) + "{/b}"
    #                $ level_ttip += "\nLeveling allows your girl to choose perks and increase stats."

                    use mybar(labl = level_text, val = (girl.xp - xp_to_levelup[girl.level - 1]), _max = (girl.get_xp_cap() - xp_to_levelup[girl.level - 1]), col = c_lightgreen, x = 65)


                    #JP

    #                textbutton "+" text_size 14 xalign 0.0 yalign 0.5 xmargin 0 ymargin 3 xpadding 0 ypadding 0 action (SetVariable("selected_girl", girl), Return("job_levels")) hovered Show("rank_level_details", girl = girl, transition = dissolve) unhovered Hide("rank_level_details", transition = dissolve)



                    if girl.away:
                        if girl.job in all_jobs:
                            $ job = girl.job
                            $ jp_show = True
                        else:
                            $ jp_show = False
                        $ jp_text = "离开"

                    elif girl.hurt > 0:
                        if girl.job in all_jobs:
                            $ job = girl.job
                            $ jp_show = True
                        else:
                            $ jp_show = False
                        $ jp_text = "受伤"

                    elif girl.workdays[calendar.get_weekday()] == 0:
                        if girl.job in all_jobs:
                            $ job = girl.job
                            $ jp_show = True
                        else:
                            $ jp_show = False
                        $ jp_text = "休息中"

                    elif girl.resting or not girl.job:
                        $ jp_text = "休息中"
                        $ jp_show = False

                    elif girl.job in all_jobs:
                        $ job = girl.job
                        $ jp_show = True

                    elif girl in farm.girls:
                        $ jp_show = False
                        if farm.programs[girl].target == "no training":
                            if farm.programs[girl].holding == "rest":
                                $ jp_text = "休息中"
                            else:
                                $ jp_text = "待机中"
                        else:
                            $ jp_text = "训练中"

                    else: # Whore
                        $ job = None

                        $ best = -1
                        for act in all_sex_acts:
                            if girl.jp[act] > best and girl.does[act]:
                                $ best = girl.jp[act]
                                $ job = act

                        $ jp_show = True


                    if jp_show:
                        $ jp_text = girl_related_dict[job.capitalize()] + " " + str(girl.job_level[job]) + " {image=img_star}"

                        $ jp_val = girl.jp[job]
                        $ jp_max = girl.get_jp_cap(job)
                        $ jp_col = c_orange

                        use mybar(labl = jp_text, val = (jp_val - jp_to_level[girl.job_level[job] - 1]), _max = (jp_max - jp_to_level[girl.job_level[job] - 1]), col = jp_col, x = 100)

                    else:
                        use mybar(labl = jp_text, val = 0, _max = 0, col = None, col2 = None, x = 100)

                    text "" size 2

            if context != "capture":
                text ""

            text "" size 2

            text "主要技能" size 20 yalign 0.0 font "bk.ttf"

            vbox:
                spacing 0

                if context != "free" or girl.MC_relationship_level >= 1:

                    for stat in girl.stats:

                        $ total_value = girl.get_stat(stat.name)
                        $ maxrange = girl.get_stat_minmax(stat.name)[1]

                        button:
                            background None
                            action NullAction()
                            tooltip stat.get_description(total_value, maxrange)
                            keyboard_focus False
                            yfill False
                            ysize 30

                            hbox:
                                spacing 6

                                bar value total_value range maxrange thumb None thumb_offset 0 xalign 1.0 xsize 170 ypos -0.4
                                text stat_name_dict[stat.name] bold True size 14 xpos 0.0 ypos -0.05 idle_color c_white + "CC"
                            text "%s/%s" % (int(total_value), maxrange) size 12 xalign 0.575 yalign 0.1 xanchor 1.0 idle_color c_white + "CC"

                    # Energy bar

                    $ girl_max = girl.get_stat_minmax("energy")[1]
                    $ rank_max = 50+50*girl.rank

                    if girl_max > rank_max:
                        $ rank_max = girl_max

                    button:
                        background None
                        action NullAction()
                        tooltip "她还有{b}" + str_int(girl.energy) + "{/b}点精力。\n她的最大精力为{b}" + str_int(girl_max) + "{/b} (增加体格可以提高精力上限)"
                        keyboard_focus False
                        yfill False
                        ysize 30

                        hbox:
                            spacing 6

                            bar value girl.energy range rank_max thumb None thumb_offset 0 xalign 1.0 xsize 170 ypos -0.4
                            text stat_name_dict["Energy"] bold True size 14 xpos 0.0 ypos -0.05 idle_color c_white + "CC"

                        text "{color=[c_red]}I{/color}" xalign (0.6*girl_max / rank_max) ypos -0.2 size 20 ysize 20
                        text "%s/%s" % (int(girl.energy), int(girl_max)) size 12 xalign 0.575 yalign 0.1 xanchor 1.0 idle_color c_white + "CC"

                else:
                    for stat in girl.stats[:4]:

                        $ total_value = girl.get_stat(stat.name)
                        $ maxrange = girl.get_stat_minmax(stat.name)[1]

                        button:
                            background None
                            action NullAction()
                            tooltip stat.get_description(total_value, maxrange)
                            keyboard_focus False
                            ysize 30

                            hbox:
                                spacing 6

                                bar value total_value range maxrange thumb None thumb_offset 0 xalign 1.0 xsize 170 ypos -0.4
                                text stat_name_dict[stat.name] bold True size 14 xpos 0.0 ypos -0.05 idle_color c_white + "CC"
                            text "%s/%s" % (int(total_value), maxrange) size 12 xalign 0.575 yalign 0.1 xanchor 1.0 idle_color c_white + "CC"

                    for stat in girl.stats[4:]:
                        button:
                            background None
                            action NullAction()
                            tooltip "你需要成为她的朋友，才能看到她这个技能的等级。"
                            keyboard_focus False
                            ysize 30

                            fixed fit_first True:

                                hbox:
                                    spacing 6

                                    bar value 0 range 50 thumb None thumb_offset 0 xalign 1.0 xsize 170 ypos -0.4
                                    text stat_name_dict[stat.name] bold True size 14 xpos 0.0 ypos -0.05 idle_color c_white + "CC"

                                text "???" xpos 75 size 14




                # text "" size 6

            hbox spacing 14:
                text "性爱技能" size 20 yalign 0.0 font "bk.ttf"

                for act in ("group", "bisexual"):

                    if girl.does[act]:
                        $ text1 = "{b}{font=[gui.fuhao]}✓{/font}{/b}"
                    else:
                        $ text1 = ""

                    if girl.has_perk(act.capitalize()):

                        button xpadding 0 ypadding 0 xmargin 0 ymargin 0 yalign 1.0 background None action NullAction() hovered Show("sex_details", girl=girl) unhovered Hide("sex_details"):
                            hbox spacing 5:
                                textbutton text1:
                                    text_size 12
                                    xsize 35
                                    ysize 20
                                    ypos -0.1
                                    if not girls_firstvisit:
                                        action (SetVariable("selected_girl", girl), SetVariable("selected_sex_act", act), Return("sex_act"))

                                    hovered (tt.Action("这将激活这个女孩的{b}" + girl_cat_name[act] + "{/b}行为. 至少还有一项常规性行为需要被激活."), Show("sex_details", girl=girl))
                                    unhovered Hide("sex_details")
                                text girl_cat_name[act.capitalize()]: #preference_color[pref] % stat.name:
                                    size 12


            if context == "slavemarket":
                $ ttip = experienced_description[girl.sexual_experience + " ttip"] + "之前接受的培训可使女孩更适合该行为."
                textbutton "之前接受的培训:   {color=" + experienced_color[girl.sexual_experience] + "}" + experienced_description[girl.sexual_experience] + "{/color}" ymargin 3 ypadding 0 text_color c_white text_size 12 background None action NullAction() hovered tt.Action(ttip)


            vbox:
                spacing 0

                if context != "free" or girl.MC_relationship_level >= 4:

                    for stat in girl.sex_stats:

                        $ total_value = girl.get_stat(stat.name)
                        $ maxrange = girl.get_stat_minmax(stat.name)[1]

    #                    if debug_mode:
    #                        $ ttip += "\npref: " + str(girl.preferences[stat.name.lower()]) + " (" + girl.get_preference(stat.name) + ")"
    #                        if stat.name == "Service":
    #                            $ ttip += "\nnaked pref: " + str(girl.preferences["naked"]) + " (" + girl.get_preference("naked") + ")"
    #                        elif stat.name == "Sex":
    #                            $ ttip += "\nbisexual pref: " + str(girl.preferences["bisexual"]) + " (" + girl.get_preference("bisexual") + ")"
    #                        elif stat.name == "Anal":
    #                            $ ttip += "\ngroup pref: " + str(girl.preferences["group"]) + " (" + girl.get_preference("group") + ")"

                        button:
                            background None
                            action NullAction()
                            hovered Show("sex_details", girl=girl)
                            unhovered Hide("sex_details")
                            tooltip stat.get_description(total_value, maxrange)
                            keyboard_focus False
                            ysize 30

                            hbox:

                                spacing 6

                                bar value total_value range maxrange thumb None thumb_offset 0 xsize 170 ypos -0.4

                                if context == "girls":

                                    if girl.does[stat.name.lower()]:
                                        $ text1 = "{font=[gui.fuhao]}✓{/font}"
                                    else:
                                        $ text1 = ""

                                    $ result, reason = girl.will_do_sex_act(stat.name.lower())

                                    if result:
                                        $ ttip = "这将会为这个激活{b}" + stat_name_dict[stat.name] + "{/b}."
                                    else:
                                        $ ttip = reason

                                    button xpadding 0 ypadding 0 xmargin 0 ymargin 0 background None action NullAction() hovered (tt.Action(ttip), Show("sex_details", girl=girl)) unhovered Hide("sex_details"):
                                        textbutton text1:
                                            text_size 12
                                            xsize 35
                                            ysize 20
                                            ypos -0.1
                                            if not girls_firstvisit and result:
                                                action (SetVariable("selected_girl", girl), SetVariable("selected_sex_act", stat.name), Return("sex_act"))

                                            hovered (tt.Action(ttip), Show("sex_details", girl=girl))
                                            unhovered Hide("sex_details")

                                $ pref = girl.get_preference(stat.name)

                                text stat_name_dict[stat.name] bold True size 14 xpos 0.0 ypos -0.05 idle_color c_white + "CC"

                            text "%s/%s" % (int(total_value), maxrange) size 12 xalign 0.575 yalign 0.1 xanchor 1.0 idle_color c_white + "CC"

                else:
                    for stat in girl.sex_stats:
                        button:
                            background None
                            action NullAction()
                            tooltip "你需要成为她的爱人，才能看到她的这种技能水平."
                            keyboard_focus False
                            ysize 30

                            fixed fit_first True:

                                hbox:
                                    spacing 6

                                    bar value 0 range 50 thumb None thumb_offset 0 xalign 1.0 xsize 170 ypos -0.4
                                    text stat_name_dict[stat.name] bold True size 14 xpos 0.0 ypos -0.05 idle_color c_white + "CC"

                                text "???" xpos 75 size 14

                # text "" size 3


            ## TRAITS LIST ##
            textbutton "特质列表" text_font "bk.ttf" text_color c_white text_size 20 background None xpadding 0 ypadding 0 xmargin 0 ymargin 0:
                action NullAction()
                if context != "free" or girl.MC_relationship_level >= 3:
                    hovered Show("trait_details", girl=girl)
                    unhovered Hide("trait_details")

            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                if len(girl.traits) > 3 or sum(len(t.name) for t in girl.traits) >= 28:
                    ysize 36
                else:
                    ysize 22

                if context != "free" or girl.MC_relationship_level >= 3:
                    hbox spacing 0 box_wrap True:
                        for trait in girl.traits:

                            $ ttip = trait.get_description(context)

                            textbutton trait_name_dict[trait.name]:

                                background None
                                xalign 0.0
                                yalign 0.5
                                text_size 14
                                action NullAction()
                                tooltip ttip
                                hovered Show("trait_details", girl=girl)
                                unhovered Hide("trait_details")
                                keyboard_focus False

                                if trait in pos_traits:
                                    text_color c_emerald
                                elif trait in neg_traits:
                                    text_color c_crimson
                                elif trait in gold_traits:
                                    text_color c_orange
                                else:
                                    text_color c_softpurple

                else:
                    textbutton "???":
                        background None
                        xalign 0.0
                        yalign 0.5
                        text_size 14
                        action NullAction()
                        tooltip "你需要成为她的男朋友才能看到她的特质."
                        keyboard_focus False

            if context == "girls":
                text "" size 2
                text "保养费用" size 20 yalign 0.0 font "bk.ttf"

                if girl.locked_upkeep:
                    text "她的保养费目前已被收回." size 14 italic True

                else:
                    key "A" action (ToggleField(girl, "auto_upkeep"), SetField(girl, "upkeep_ratio", (girl.upkeep - girl.get_med_upkeep())/girl.rank), Play("sound", "click.wav"))

                    hbox:
                        spacing 2

                        $ minrange = girl.get_med_upkeep() // 4
                        $ maxrange = girl.get_med_upkeep() + 11 * girl.rank * 2 ** girl.rank # Simplify at some point

                        text "" size 14

                        bar value FieldValue(girl, "upkeep", range=maxrange-minrange, offset=minrange, action=Function(girl.update_upkeep_ratio)):
                            xsize 0.45
                            ypos -0.4
                            keyboard_focus False
                            hovered tt.Action("你必须每天支付保养费. 更高端的女孩将需要更高的费用. 保持高昂的费用可以让你的女孩开心.")

                        textbutton "-":
                            text_size 14
                            ypos -0.1
                            xsize 25
                            xpadding 0
                            if girl.upkeep > minrange:
                                action (SetField(girl, "upkeep", girl.upkeep-1), Function(girl.update_upkeep_ratio), Play("sound", "click.wav"))
                            hovered tt.Action("减少她的保养费.")

                        textbutton "+":
                            text_size 14
                            ypos -0.1
                            xsize 25
                            xpadding 0
                            if girl.upkeep < maxrange:
                                action (SetField(girl, "upkeep", girl.upkeep+1), Function(girl.update_upkeep_ratio), Play("sound", "click.wav"))
                            hovered tt.Action("增加她的保养费.")

                        if girl.auto_upkeep:
                            $ text1 = "自动保养设置为: {b}{color=[c_green]}开启{/color}{/b} {i}(快捷键: {u}Shift+a{/u}){/i}"
                        else:
                            $ text1 = "自动保养设置为: {b}{color=[c_red]}关闭{/color}{/b} {i}(快捷键: {u}Shift+a{/u}){/i}"

                        textbutton "A":
                            if girl.auto_upkeep:
                                text_bold True

                            text_size 14
                            ypos -0.1
                            xsize 25
                            xpadding 0
                            action (ToggleField(girl, "auto_upkeep"), SetField(girl, "upkeep_ratio", (girl.upkeep - girl.get_med_upkeep())/girl.rank), Play("sound", "click.wav"))
                            tooltip "{size=+2}" + text1 + "\n开启自动后，保养费用将会自动调节.{/size=+2}"

                        text " " + str(round_int(girl.upkeep)) + "金币":
                            size 14
                            if girl.get_upkeep_modifier() < 0:
                                color c_red

                            elif girl.get_upkeep_modifier() == 0:
                                color c_white

                            else:
                                color c_emerald

            elif context == "farm":
                text "" size 2
                text "保养费用" size 20 yalign 0.0 font "bk.ttf"

                hbox:
                    spacing 2

                    text "" size 14

                    text str(girl.get_med_upkeep() // 4) + "金币(固定)" size 14


screen assign_job(girl):

    modal True
    tag assign_job

    key "mouseup_3" action (Return("cancel"))

    key "1" action (Return("rest"))
    key "2" action (Return("waitress"))
    key "3" action (Return("dancer"))
    key "4" action (Return("masseuse"))
    key "5" action (Return("geisha"))
    key "6" action (Return("whore"))
    if farm.active:
        key "7" action (Return("farm"))
    if brothel.master_bedroom.level >= 1:
        key "8" action (Return("master bedroom"))

    frame ypos 0.25:

        grid 4 2:
            xsize 450
            spacing 1

            button xsize 110 ysize 60 background None xpadding 2 ypadding 2:
#                 selected girl.job == "rest" # What was this?
                action Return("rest")
                tooltip "安排" + girl.fullname + "去休息."
                add "tb rest" alpha 0.6 hover_alpha 1.0 selected_hover_alpha 1.0 selected_idle_alpha 1.0 xalign 0.5 yalign 0.5
                text "休息" selected_color c_green hover_bold True xalign 0.5 yalign 0.5 drop_shadow (1, 1) size 14
                text "1" size 12 xalign 0.05 yalign 0.95 drop_shadow (1, 1)

            for j in all_jobs + ["whore"]:
                button xsize 110 ysize 60 background None xpadding 2 ypadding 2 xalign 0:
                    if brothel.has_room(job_room_dict[j]):
#                         selected girl.job == j # What was this?
                        action Return(j)
                        tooltip "安排" + girl.fullname + "作为" + girl_related_dict[j] + "工作"
                        add "tb " + j idle_alpha 0.66 #selected_hover_alpha 1.0 selected_idle_alpha 1.0 hover_alpha 1.0 xalign 0.5 yalign 0.5
                        text girl_related_dict[j.capitalize()] selected_color c_yellow hover_bold True xalign 0.5 yalign 0.5 drop_shadow (1, 1) size 14
                        if j == "whore":
                            $ text1 = "6"
                        else:
                            $ text1 = str(all_jobs.index(j)+2)
                        text text1 size 12 xalign 0.05 yalign 0.95 drop_shadow (1, 1)

                    else:
                        text girl_related_dict[j.capitalize()] + "\n(不可用)" selected_bold True xalign 0.5 yalign 0.5 drop_shadow (1, 1) size 14


            if farm.active:
                button xsize 110 ysize 60 background None xpadding 2 ypadding 2 xpos 0:
#                     selected girl.job=="farm" # What was this?
                    action Return("farm")
                    tooltip "把" + girl.fullname + "送去农场."
                    add "tb farm" idle_alpha 0.66 selected_hover_alpha 1.0 selected_idle_alpha 1.0 hover_alpha 1.0 xalign 0.5 yalign 0.5
                    text "农场" selected_color c_green hover_bold True xalign 0.5 yalign 0.5 drop_shadow (1, 1) size 14
                    text "7" size 12 xalign 0.05 yalign 0.95 drop_shadow (1, 1)
            else:
                text ""

            if brothel.master_bedroom.level >= 1:
                $ text1 = "自动训练 "
                if girl in brothel.master_bedroom.girls:
                    $ ttip = "让" + girl.fullname + "离开你的房间."
                    $ text1 += "(开)"
                else:
                    $ ttip = "让" + girl.fullname + "去到你的房间."
                    $ text1 += "(关)"

                button xsize 110 ysize 60 background None xpadding 2 ypadding 2 xpos 0:
                    action Return("master bedroom")
                    tooltip ttip
                    add brothel.master_bedroom.get_pic(100, 60) idle_alpha 0.66 selected_hover_alpha 1.0 selected_idle_alpha 1.0 hover_alpha 1.0 xalign 0.5 yalign 0.5
                    text text1 selected_color c_green hover_bold True xalign 0.5 yalign 0.5 drop_shadow (1, 1) size 14 text_align 0.5
                    text "8" size 12 xalign 0.05 yalign 0.95 drop_shadow (1, 1)
            else:
                text ""





screen girl_stats_light(girl, x=0.5, y=0.9):

    frame xalign x yalign y xsize 450 xpadding 10 ypadding 10:

        has hbox spacing 10

        if girl:
            grid 3 8:
                for stat in girl.stats:
                    $ change = 0
                    if selected_item:
                        if selected_item.equipped:
                            $ change = -round_int(girl.get_effect("boost", selected_item.type.name.lower()) * (selected_item.get_effect("change", stat.name) + (1 - selected_item.get_effect("boost", stat.name))*girl.get_stat(stat.name)))
                        else:
                            $ change = round_int(girl.get_effect("boost", selected_item.type.name.lower()) * (selected_item.get_effect("change", stat.name) + (1 - selected_item.get_effect("boost", stat.name))*girl.get_stat(stat.name)))

                            for it in girl.equipped:
                                if it.slot == selected_item.slot:
                                    $ change -= round_int(girl.get_effect("boost", it.type.name.lower()) * (it.get_effect("change", stat.name) + (1 - it.get_effect("boost", stat.name))*girl.get_stat(stat.name)))

                            # Adjust Food bonuses
                            if selected_item.type.name == "Food":
                                python:
                                    for eff in selected_item.effects:
                                        if eff.target == stat.name.lower() and girl.current_food_effect[stat.name.lower()]:
                                            change -= girl.current_food_effect[stat.name.lower()].value

                    text stat_name_dict[stat.name] size 13 color c_brown:
                        if change:
                            bold True

                    text str_int(girl.get_stat(stat.name)) size 14 color c_brown xalign 1.0:
                        if change:
                            bold True
                    if change:
                        text " -> " + str_int(girl.get_stat(stat.name) + change) size 14 bold True:
                            if change >= 0:
                                color c_emerald
                            else:
                                color c_red
                    else:
                        text "" size 14

            grid 3 7:
                for stat in girl.sex_stats:
                    $ change = 0
                    if selected_item:
                        if selected_item.equipped:
                            $ change = -round_int(girl.get_effect("boost", selected_item.type.name.lower()) * (selected_item.get_effect("change", stat.name) + (1 - selected_item.get_effect("boost", stat.name))*girl.get_stat(stat.name)))
                        else:
                            $ change = round_int(girl.get_effect("boost", selected_item.type.name.lower()) * (selected_item.get_effect("change", stat.name) + (1 - selected_item.get_effect("boost", stat.name))*girl.get_stat(stat.name)))

                            for it in girl.equipped:
                                if it.slot == selected_item.slot:
                                    $ change -= round_int(girl.get_effect("boost", it.type.name.lower()) * (it.get_effect("change", stat.name) + (1 - it.get_effect("boost", stat.name))*girl.get_stat(stat.name)))

                    text stat_name_dict[stat.name] size 13 color c_brown:
                        if change:
                            bold True
                    text str_int(girl.get_stat(stat.name)) size 14 color c_brown xalign 1.0:
                        if change:
                            bold True

                    if change:
                        text " -> " + str_int(girl.get_stat(stat.name) + change) size 14:
                            if change > 0:
                                color c_emerald
                            else:
                                color c_red
                    else:
                        text "" size 14

                text "" size 14
                text "" size 14
                text "" size 14

                $ change = 0
                if selected_item:
                    if selected_item.equipped:
                        $ change = -round_int(girl.get_effect("boost", selected_item.type.name.lower()) * (selected_item.get_effect("change", "defense") + (1 - selected_item.get_effect("boost", "defense"))*girl.get_stat("defense")))
                    else:
                        $ change = round_int(girl.get_effect("boost", selected_item.type.name.lower()) * (selected_item.get_effect("change", "defense") + (1 - selected_item.get_effect("boost", "defense"))*girl.get_stat("defense")))

                        for it in girl.equipped:
                            if it.slot == selected_item.slot:
                                $ change -= round_int(girl.get_effect("boost", it.type.name.lower()) * (it.get_effect("change", "defense") + (1 - it.get_effect("boost", "defense"))*girl.get_stat("defense")))

                text "个人防御" size 13 color c_brown:
                    if change:
                        bold True
                text str_int(girl.get_defense()) size 14 color c_brown xalign 1.0:
                    if change:
                        bold True

                if change:
                    text " -> " + str_int(girl.get_stat("defense") + change) size 14:
                        if change > 0:
                            color c_emerald
                        else:
                            color c_red

                else:
                    text "" size 14

                $ change = 0
                if selected_item:
                    $ change = girl.get_effect("boost", selected_item.type.name.lower()) * (selected_item.get_effect("gain", "energy")*girl.get_effect("boost", "energy") + girl.get_effect("change", "energy"))

    #                if selected_item.equipped:
    #                    $ change = -round_int(girl.get_effect("boost", selected_item.type.name.lower()) * (selected_item.get_effect("change", "energy") + (1 - selected_item.get_effect("boost", "energy"))*girl.energy))
    #                else:
    #                    $ change = round_int(girl.get_effect("boost", selected_item.type.name.lower()) * (selected_item.get_effect("change", "energy") + (1 - selected_item.get_effect("boost", "energy"))*girl.energy))

    #                    for it in girl.equipped:
    #                        if it.slot == selected_item.slot:
    #                            $ change -= round_int(girl.get_effect("boost", it.type.name.lower()) * (it.get_effect("change", "energy") + (1 - it.get_effect("boost", "energy"))*girl.energy))
                text stat_name_dict["Energy"] size 13 color c_brown:
                    if change:
                        bold True
                text str_int(girl.energy) size 14 color c_brown xalign 1.0:
                    if change:
                        bold True
                if change:
                    if girl.energy + change > girl.get_stat_minmax("energy")[1]:
                        $ change = girl.get_stat_minmax("energy")[1] - girl.energy
                    text " -> " + str_int(girl.energy + change) size 14:
                        if change > 0:
                            color c_emerald
                        else:
                            color c_red
                else:
                    text "" size 14



screen button_overlay(girl, context="girls"):

    zorder -5

    if context == "slavemarket":

        frame:

            xalign 0.0
            xmargin 0.1
            xsize 0.3
            xfill True
            ypos 0.16
            background None

            has hbox

            xfill True

            $ text1 = str(girl.get_price('buy')) + "金币"

            text text1 xalign 0.0

            key "y" action Return(girl)

            textbutton "购买" xalign 1.0 action Return(girl) tooltip "点击为" + girl.fullname + "购买" + text1

    elif context == "girls":

        key "j" action (SetVariable("selected_girl", girl), Return("assign"))


        if not (girls_firstvisit or girl.away): # Interaction menu can still be accessed when MC interactions=0 (to listen to her story again, for instance)
            key "i" action (SetVariable("selected_girl", girl), Return("interact"))
            key "t" action (SetVariable("selected_girl", girl), Return("equip"))
            if girl.free:
                key "K_DELETE" action (SetVariable("selected_girl", girl), Return("dismiss"))
            else:
                key "K_DELETE" action (SetVariable("selected_girl", girl), Return("sell"))

        frame:

            background None

            xalign 0.0
            yalign 0.19
            xmargin 6
            xpadding 3
            ypadding 6
            xsize 320
            yfill False

            has hbox

            spacing 1
            box_wrap True


            if girl.away:
                $ text1 = "离开"
                $ ttip = "她因上课或任务而离开了%s天." % (girl.return_date - calendar.time)

            elif girl.hurt > 0:
                $ text1 = "受伤"
                if girl.hurt <= 1:
                    $ ttip = "这个女孩受伤了，需要休息1天，直到她准备好做任何事情."
                else:
                    $ ttip = "这个女孩受伤了，需要休息" + str(round_int(girl.hurt)) + "天，直到她准备好做任何事情."

            elif girl.exhausted:
                $ text1 = "疲倦"
                $ ttip = "这个女孩需要充分休息，直到她能再次工作."

            elif girl.resting and girl.job:
                $ text1 = "休息中"
                $ ttip = "这个女孩按日程表今天休息."

            elif not girl.job:
                $ text1 = "无工作"
                $ ttip = "未分配工作. 这名女孩已被安排休息，等待进一步的指示."

            elif girl.work_whore:
                $ text1 = girl_related_dict[girl.job.capitalize()][:4] + "./Wh."
                $ ttip = "工作和嫖娼. 改变这个女孩的工作或者让她休息."

            else:
                $ text1 = girl_related_dict[girl.job.capitalize()]
                $ ttip = "改变这个女孩的工作或让她休息."

            textbutton text1 text_size 14 action (SetVariable("selected_girl", girl), Return("assign")) tooltip ttip + " ({i}快捷键: {u}j{/u}{/i})"

            $ sched = girl.workdays[calendar.get_weekday()]

            if sched == 0:
                $ text1 = "休息日"
            elif sched == 50:
                $ text1 = "半班制"
            elif sched == 100:
                $ text1 = "全班制"

#            textbutton "Schedule" text_size 14 hovered tt.Action("Click to set up this girl's schedule."):

#                if not girls_firstvisit:
#                    action (SetVariable("selected_girl", girl), Return("sched"))


            button:
                background None
                xmargin 0
                ymargin 0
                xpadding 0
                ypadding 0

                textbutton "互动":
                    text_size 14
                    hovered tt.Action("与你的女孩互动. 需要消耗行动力.")

                    if MC.interactions > 0 and not (girls_firstvisit or girl.away):
                        action (SetVariable("selected_girl", girl), Return("interact"))

                if not (girls_firstvisit or girl.away):
                    action (SetVariable("selected_girl", girl), Return("interact"))
                else:
                    action NullAction()

                if MC.interactions <= 0:
                    tooltip "你今天不能再采取任何行动."

                elif girl.away:
                    tooltip "由于她不在，你无法与%s互动." % girl.name

            textbutton "物品":
                text_size 14

                if not (girls_firstvisit or girl.away):

                    action (SetVariable("selected_girl", girl), Return("equip"))

                    tooltip "改变这个女孩的装备."

                else:
                    tooltip "[girl.fullname]正在外出上课或执行任务."

            if girl.free:
                textbutton "解散":
                    text_size 14
                    if not (girls_firstvisit or girl.away):
                        action (SetVariable("selected_girl", girl), Return("dismiss"))
                    tooltip "把这个女孩从你的监护中释放出来. ({i}快捷键: {u}Delete{/u}{/i})"

            else:
                textbutton "出售":
                    text_size 14
                    if not (girls_firstvisit or girl.away):
                        action (SetVariable("selected_girl", girl), Return("sell"))
                    tooltip "将这个女孩以%s金币出售 (原始成本: %s金币). ({i}快捷键: {u}Delete{/u}{/i})" % (str(girl.get_price("sell")), girl.original_price)


            if girl.upgrade_points >= 1 or girl.perk_points:
                key "u" action (SetVariable("selected_girl", girl), Return("level_or_perks"))
                key "k" action (SetVariable("selected_girl", girl), Return("perks"))
                textbutton "升级" text_size 14:
                    action (SetVariable("selected_girl", girl), Return("level_or_perks"))
                    alternate (SetVariable("selected_girl", girl), Return("perks"))
                    tooltip ("你有" + str (girl.perk_points) + "可供消费的特质点数.\n右键点击进入查看特质.")
                    hovered Show("perk_details", girl=girl)
                    unhovered Hide("perk_details")

            else:
                if not girls_firstvisit:
                    key "k" action (SetVariable("selected_girl", girl), Return("perks"))

                textbutton "特质":
                    text_size 14
                    if not girls_firstvisit:
                        action (SetVariable("selected_girl", girl), Return("perks"))
                    tooltip "查看她目前的特技和特质"
                    hovered Show("perk_details", girl=girl)
                    unhovered Hide("perk_details")



            if girl.ready_to_rank():
                key "r" action (SetVariable("selected_girl", girl), Return("rank"))
                textbutton "升阶" text_size 14 action (SetVariable("selected_girl", girl), Return("rank"))

            if not girls_firstvisit:
                key "a" action (SetVariable("selected_girl", girl), Return("stats"))

                textbutton "统计数据":
                    text_size 14
                    action (SetVariable("selected_girl", girl), Return("stats"))

            if debug_mode:
                textbutton "图片" action (SetVariable("selected_girl", girl), Return("debug_pics")) text_size 14 tooltip "用游戏的图片生成测试女孩包."

    elif context == "free":

        frame:

            xalign 0.0
            xmargin 0.1
            xsize 0.3
            xfill True
            ypos 0.15
            background None

            has hbox

            xfill True

            if girl.MC_relationship_level <= 1:
                $ text1 = event_color["a little bad"] % "认识的人"
            elif girl.MC_relationship_level == 1:
                $ text1 = event_color["average"] % "朋友"
            elif girl.MC_relationship_level == 2:
                $ text1 = event_color["a little good"] % "恋爱中的人"
            elif girl.MC_relationship_level == 3:
                $ text1 = event_color["good"] % "女朋友"
            elif girl.MC_relationship_level >= 4:
                $ text1 = event_color["special"] % "恋人"

            text "当前关系: " + text1 xalign 0.0 size 14

    elif context == "farm":

        frame:

            background None

            xalign 0.0
            yalign 0.19
            xmargin 6
            xpadding 3
            ypadding 6
            xsize 320
            yfill False

            has hbox

            spacing 1
            box_wrap True

#            textbutton "Change program" text_size 14 action Return(("change program", girl)) hovered tt.Action("Change " + girl.name + "'s current training program.")

            key "t" action Return(("equip", girl))
            key "a" action Return(("take out", girl))
            if girl.free:
                key "K_DELETE" action Return(("dismiss", girl))
            else:
                key "K_DELETE" action Return(("sell", girl))

            textbutton "物品":
                text_size 14
                if not girls_firstvisit:
                    action Return(("equip", girl))

                hovered tt.Action("改变这个女孩的装备.")

            textbutton "离开农场" text_size 14 action Return(("take out", girl)) hovered tt.Action("Send " + girl.name + " back to the brothel.")

            if girl.free:
                textbutton "解散":
                    text_size 14
                    action Return(("dismiss", girl))
                    tooltip "把这个女孩从你的监护中释放出来. ({i}快捷键: {u}Delete{/u}{/i})"
            else:
                textbutton "出售":
                    text_size 14
                    if not girls_firstvisit:
                        action Return(("sell", girl))
                    tooltip "将这个女孩以%s金币出售 (原始成本: %s金币). ({i}快捷键: {u}Delete{/u}{/i})" % (str(girl.get_price("sell")), girl.original_price)

screen mybar(labl = "Level 25", hov = None, unhov = None, val = 0, _max = 100, col = c_green, col2 = c_ui_light, x = 100, y = 6, txt_size = 14):

    frame:

        xmaximum x
        xfill True
#        ysize y
        xmargin 0
        ymargin 0
        xpadding 0
        ypadding 0
        background None

        has vbox
        spacing 1

        text labl size txt_size xalign 0.0 yalign 0.0
        bar value val left_bar col right_bar col2 range _max thumb None thumb_offset 0 xfill True ysize y yalign 0.0 left_gutter 0 right_gutter 0 top_gutter 1 bottom_gutter 0 #xalign 1.0 xsize 170 ypos -0.4



#        action NullAction()

#        if hov:
#            hovered hov

#        if unhov:
#            unhovered unhov

screen rank_level_details(girl):

    frame:

        xpadding 10

        xfill False

        xalign 0.5
        yalign 0.5
        ypadding 25
        ymargin 10
        background c_ui_darkblue

        has vbox
        xalign .5
        yalign .5
        spacing 25

        text girl.fullname:
            xalign 0.5
            color c_orange

        grid 2 2:

            spacing 10

            vbox:
                text "阶级" size 12

                $ text1 = rank_name[girl.rank]

                if girl.rank == district.rank:
                    $ text1 += " {size=12} (max){/size}"

                text text1 color c_softpurple

            vbox:
                text "等级" size 12
                text str(girl.level) + " {size=12} / " + str(girl.rank * 5) + "{/size}" color c_lightgreen

            vbox:
                text "人气" size 12
                text str(int(girl.rep)) + " {size=12}/ " + str(girl.get_rep_cap()) + "{/size}" color c_softpurple

            vbox:
                text "经验" size 12
                text str(int(girl.xp)) + " {size=12}/ " + str(girl.get_xp_cap()) + "{/size}" color c_lightgreen



        grid 3 10:

            text "技能" size 16

            text "星级" size 16

            text "职业经验" size 16

            spacing 10

            for job in all_jobs:

                text girl_related_dict[job.capitalize()] yalign 0.5
                $ star_text = ""
                for i in range(girl.job_level[job]):
                    $ star_text += "{image=img_star}"

                text star_text yalign 0.5

                text str(round_int(girl.jp[job])) + " {size=12}/ " + str(girl.get_jp_cap(job)) + "{/size}" yalign 0.5 color c_orange

            text ""
            text ""
            text ""

            for job in ("service", "sex", "anal", "fetish"):

                text girl_related_dict[job.capitalize()] yalign 0.5
                $ star_text = ""
                for i in range(girl.job_level[job]):
                    $ star_text += "{image=img_star}"

                text star_text yalign 0.5

                text str(round_int(girl.jp[job])) + " {size=12}/ " + str(girl.get_jp_cap(job)) + "{/size}" yalign 0.5 color c_orange


## SCHEDULE SCREEN

screen schedule(glist):

    modal True

    key "mouseup_3" action (Return())
    key "d" action Return()

    use dark_filter()

    frame:
        ypos 0.08
        xmargin 20
#        ymargin 20
        xpadding 20
        ypadding 20

        has vbox

        spacing 3

        hbox:
            spacing 6
            xfill True
            ysize 22
            xalign 1.0
            hbox:
                xsize 150
                xfill True
                xalign 0.0
                yalign 1.0
                text "女孩的排班表" color c_darkorange xalign 0.5 yalign 0.0 text_align 1.0 size 20

            for day in weekdays:

                frame xsize 88 ysize 20  yalign 1.0 background None:
                    text day size 14 xalign 0.5 color c_brown xsize 90:
                        if day == calendar.get_weekday():
                            bold True

        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            ymaximum 0.8
            yfill False
            yadjustment sched_adj

            has vbox
            spacing 6

            for girl in glist:
                hbox:
                    spacing 6
                    xfill True
                    xalign 1.0

                    hbox:
                        xsize 150
                        xfill True
                        xalign 1.0
                        yalign 0.5

                        button xsize 95 style "girlbutton" xpadding 6 ypadding 3 action (SetVariable("selected_girl", girl), Return()) tooltip "单击此处查看" + girl.fullname + "的个人资料.":
                            has vbox

                            xalign 1.0
                            yalign 0.5

                            text girl.name size 14 text_align 1.0 color c_brown xalign 1.0:

                                if selected_girl == girl:
                                    bold True
                                    color c_white

                            if girl.job:
                                $ text1 = girl_related_dict[girl.job.capitalize()]
                                $ col = job_color[girl.job]
                            else:
                                $ text1 = "没有工作"
                                $ col = c_white
                            text text1 size 12 text_align 1.0 color col xalign 1.0

                            if girl.exhausted:
                                $ text1 = event_color["a little bad"] % "筋疲力尽"
                            elif girl.hurt:
                                $ text1 = event_color["bad"] % ("受伤(" + str(round_int(girl.hurt)) + "天)")
                            else:
                                $ en_max = girl.get_stat_minmax("energy")[1]

                                if girl.energy < en_max / 5:
                                    $ text1 = "精力：{color=[c_red]}" + str(round_int(girl.energy)) + "{/color}/" + str(round_int(en_max))
                                else:
                                    $ text1 = str(round_int(girl.energy)) + "/" + str(round_int(en_max))

                            text text1 size 12 text_align 1.0 color c_brown xalign 1.0

                        hbox:
                            xmaximum 50
                            xfill True
                            xalign 1.0
                            yalign 0.5
                            spacing 20

                            fixed fit_first True xalign 0.5 yalign 0.5:
                                add girl.portrait.get(x = 40, y = 40) xalign 0.5 yalign 0.5

                                $ badge = girl.get_badge()
                                if badge:
                                    add ProportionalScale(badge, 20, 20) xalign 0.9 yalign 0.1

                    for day in weekdays:

                        if girl.workdays[day] == 100:
                            $ t = "全班制"
                            $ ttip = "她将尽其所能地工作."
                            $ col1 = c_orange

                        elif girl.workdays[day] == 50:
                            $ t = "半班制"
                            $ ttip = "她将接待平时一半的顾客，节省一些精力."
                            $ col1 = c_prune
                        elif girl.workdays[day] == 0:
                            $ t = "休息日"
                            $ ttip = "她会休息以便恢复一些精力."
                            $ col1 = c_emerald

                        textbutton t text_size 14 xsize 90 ysize 40 yalign 0.5 hovered tt.Action(ttip) idle_background col1 hover_background c_darkbrown + "CC":
                            if girl.block_schedule != day:
                                action Function(girl.cycle_workday, day) # renpy.curried_invoke_in_new_context(girl.cycle_workday, day)
                            else:
                                action Function(renpy.notify, "\n你不能改变她的排班表，因为你给她放了一天假.")

                        # Disabled: alternate renpy.curried_invoke_in_new_context(girl.cycle_workday, day, True)
        text ""

        hbox spacing 10 xalign 1.0:
            if brothel.get_effect("special", "autorest"):
                textbutton "自动休息设置" xalign 1.0 action Show("autorest")
            textbutton "Ok" action (Return())

screen autorest():
    modal True

    key "mouseup_3" action Hide("autorest")

    frame xalign 0.5 yalign 0.5 xpadding 10 ypadding 10:
        has vbox spacing 6

        text "自动休息设置" color c_brown xalign 0.5
        text ""
        add "items/furniture/scanner.webp" xalign 0.5
        text ""
        text "这使你的女孩在精力过低时自动休息.\n左键点击可增加阈值\n右键点击可将其降低" italic True size 14 color c_brown xsize 360
        text "" size 18
        if autorest_limit == 0:
            $ text1 = "自动休息 已关闭"
        else:
            $ text1 = "自动休息 已开启 - 下限: " + str(autorest_limit) + "精力"

        textbutton text1 action Function(change_autorest, "+") alternate Function(change_autorest, "-") xalign 0.5 xsize 360 ysize 40 text_size 18
        text "" size 18
        textbutton "OK" action Hide("autorest") xalign 1.0

## LEVEL & PERKS SCREEN

screen level(girl):

    modal True

    key "mouseup_3" action Hide("level")

    frame:

        background c_ui_light

        xmargin 20
        ymargin 20
        xpadding 80
        ypadding 40
        xalign 0.5
        yalign 0.5
        xsize int(0.5*config.screen_width)
        xfill True

        has vbox

        spacing 3
        xalign 0.5

        $ text1 = girl.name + "准备好升级了."

        text text1 color c_orange xalign 0.5

        hbox:
            spacing 6
            xalign 0.5
            text "可用点数:" size 14 color c_orange
            text str(round_int(girl.upgrade_points)) size 14 color c_orange

        text ""

        vbox:

            for stat in gstats_main:

                hbox spacing 3:

                    frame background None xsize 180:
                        hbox:
                            text stat_name_dict[stat] + ": " size 14 color c_orange
                            text str(girl.get_stat(stat)) + " / " + str(girl.get_stat_minmax(stat)[1]) size 14 color c_green

                    grid 4 1:
                        if girl.get_max_stat_upgrade_points(stat) >= 1:
                            textbutton "+1" xsize 50 ysize 25 text_size 14 action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat"), Play("sound", "click.wav"))
                        else:
                            null
                        if girl.get_max_stat_upgrade_points(stat) >= 5:
                            textbutton "+5" xsize 50 ysize 25 text_size 14 action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat5"), Play("sound", "click.wav"))
                        elif 5 > girl.get_max_stat_upgrade_points(stat) > 1 and girl.get_max_stat_upgrade_points(stat) not in (5, 10, 20):
                            textbutton "+" + str(int(girl.get_max_stat_upgrade_points(stat))) xsize 50 ysize 25 text_size 14 action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat_all"), Play("sound", "click.wav"))
                        else:
                            null
                        if girl.get_max_stat_upgrade_points(stat) >= 10:
                            textbutton "+10" xsize 50 ysize 25 text_size 14 action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat10"), Play("sound", "click.wav"))
                        elif 10 > girl.get_max_stat_upgrade_points(stat) > 5 and girl.get_max_stat_upgrade_points(stat) not in (5, 10, 20):
                            textbutton "+" + str(int(girl.get_max_stat_upgrade_points(stat))) xsize 50 ysize 25 text_size 14 action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat_all"), Play("sound", "click.wav"))
                        else:
                            null
                        if girl.get_max_stat_upgrade_points(stat) >= 20:
                            textbutton "+20" xsize 50 ysize 25 text_size 14 action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat20"), Play("sound", "click.wav"))
                        elif 20 > girl.get_max_stat_upgrade_points(stat) > 10 and girl.get_max_stat_upgrade_points(stat) not in (5, 10, 20):
                            textbutton "+" + str(int(girl.get_max_stat_upgrade_points(stat))) xsize 50 ysize 25 text_size 14 action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat_all"), Play("sound", "click.wav"))
                        else:
                            null

        text ""

        if girl.perk_points:
            $ _next = "perks"
        else:
            $ _next = ""

        textbutton "Ok" xalign 1.0 action (Hide("level"), Return(_next))


screen perks(girl):

    modal True

    default selected_archetype = "The Maid"
    default selected_perk = None

    key "mouseup_3" action Return(("commit", ""))

    frame ypos 0.1 xsize 0.9 ysize 0.94 xalign 0.5 xfill False yfill False:
        background c_ui_light

        has vbox spacing 10

        text girl.fullname + "的特质树" color c_orange xalign 0.5

        hbox:
            for archetype in archetype_list:
                button xsize 100 xfill True background None hovered SetScreenVariable("selected_archetype", archetype) action SelectedIf(selected_archetype==archetype):
                    vbox:
                        fixed:
                            fit_first True
                            if girl.archetypes[archetype].unlocked:
                                add girl.archetypes[archetype].get_pic(portrait=True).get(75, 75) idle_alpha 0.6 selected_hover_alpha 1.0 selected_idle_alpha 1.0
                            else:
                                add im.MatrixColor(girl.archetypes[archetype].get_pic(portrait=True).get(75, 75), im.matrix.desaturate()) idle_alpha 0.6 selected_hover_alpha 1.0 selected_idle_alpha 1.0
                                add "img_lock"  zoom 0.7 xalign 0.5 yalign 0.5 alpha 0.8

                        text archetype_name_dict[archetype] size 28 selected_outlines [ (2, "#fff", 0, 0) ] color c_darkgrey selected_color c_black font "bk.ttf"

#        background girl.archetypes[selected_archetype].get_pic().get(800, 640)
        button background None xalign 0.5 yalign 0.5 xsize 800 yfill True ypadding 0 right_padding 0 right_margin 0 action NullAction():
            fixed:
                fit_first True
                add girl.archetypes[selected_archetype].get_pic().get(800, 640) alpha 0.6

                add "lines" xalign 0.5 yalign 0.5 alpha 0.7

                if not girl.archetypes[selected_archetype].unlocked:
                    add "img_lock" xpos 0 ypos 0.03

                hbox xalign 1.0 xfill True yfill True:

                    fixed xalign 0.3 ypos 0.05 xsize 550 ysize 620 xfill True yfill True:
                        fit_first True

                        $ perks = girl.archetypes[selected_archetype].get_perks()
                        $ pos_dict = {0: (150, 0), 1: (0, 100), 2: (300, 100), 3: (0, 250), 4: (300, 250), 5: (150, 350)}

                        for perk in perks:
                            $ perk_index = perks.index(perk)

                            button xpos pos_dict[perk_index][0] ypos pos_dict[perk_index][1] xsize 110 ysize 110 xfill True yfill True:

                                if girl.has_perk(perk.name) or perk in new_perks:
                                    background c_ui_unlocked
                                    add perk.get_pic().get(100, 100) xalign 0.5 yalign 0.5
                                    action NullAction()
                                    hovered (tt.Action("这个特质已经解锁了."), SetScreenVariable("selected_perk", perk))
                                    unhovered SetScreenVariable("selected_perk", None)

                                elif girl.can_acquire_perk(perk, context="perk_screen")[0]:
                                    background c_ui_sensitive + "DD"
                                    hover_background c_ui_sensitive
                                    add perk.get_pic().get(100, 100) xalign 0.5 yalign 0.5 alpha 0.6 hover_alpha 1.0
                                    action Return(("add", perk))
                                    hovered (tt.Action("Acquire " + perk.name + "获得1点特质点."), SetScreenVariable("selected_perk", perk))
                                    unhovered SetScreenVariable("selected_perk", None)
                                else:
                                    background c_ui_insensitive + "AA"
                                    # button background None xsize 110 ysize 110 xfill True yfill True:
                                    add im.MatrixColor(perk.get_pic().get(100, 100), im.matrix.desaturate()) xalign 0.5 yalign 0.5
                                    action NullAction()
                                    hovered (tt.Action(event_color["a little bad"] % girl.can_acquire_perk(perk, context="perk_screen")[1]), SetScreenVariable("selected_perk", perk))
                                    unhovered SetScreenVariable("selected_perk", None)


                    frame background c_ui_dark xsize 260 xalign 1.0 xfill True yfill True:

                        has vbox

                        xfill True
                        yfill True

                        if selected_perk:
                            text selected_perk.name size 18 bold True yalign 0.0

                            frame xpadding 0 xmargin 0 ypadding 0 ymargin 0 background None xsize int(0.25*config.screen_width) xfill True xalign 0.5 yalign 0.5:
                                add selected_perk.get_pic().get(220, 220)

                            frame xpadding 0 xmargin 0 ypadding 0 ymargin 0 background None xsize 220 xfill True xalign 0.5 yalign 0.5:
                                has vbox spacing 6

                                if selected_perk.min_rank:
                                    text "阶级 " + rank_name[selected_perk.min_rank] + " " size 14 italic True yalign 0.0
                                else:
                                    text "阶级 C " size 14 italic True yalign 0.0

                                text selected_perk.get_description() size 14 yalign 0.0

                        else:
                            vbox spacing 10:
                                text archetype_name_dict[selected_archetype] size 48 bold True yalign 0.0 font "bk.ttf"
                                text archetype_description[selected_archetype] size 16 yalign 0.0
                                text ""

                                if not girl.archetypes[selected_archetype].unlocked:
                                    textbutton "解锁\n{size=-6}(花费2个特质点){/size}" xalign 0.5 xpadding 6 ypadding 6:
                                        if perk_points >= 2:
                                            action Return(("unlock", selected_archetype))

                        vbox xalign 0.5 yalign 1.0:
                            text "特质点数: " + str(perk_points) color c_orange size 18 yalign 1.0 yfill True
                            hbox:
                                textbutton "取消" xalign 0.2 action Return(("cancel", ""))
                                textbutton "确定" xalign 0.8:
                                    if new_perks:
                                        action Return(("commit", ""))


screen trait_details(girl):

    tag trait_details

    default yadj = ui.adjustment()
    default t = 0

    if len(girl.traits+girl.perks) > 12 and yadj.value < len(girl.traits+girl.perks)*50:
        timer 0.1 repeat True action (SetScreenVariable("t", t + 0.1), Function(yadj.change, max(0, 50*(t-0.25)))) # Scrolls down after 0.25 seconds

    frame:
        background c_ui_darker
        xalign 0.5
        yalign 0.8
        xsize int(config.screen_width / 2.8)
        ymaximum int(config.screen_height*0.8)

        viewport:
            yadjustment yadj
            yfill False

            has vbox

            spacing 3

            text girl.name + "的特质列表" xalign 0.5 color c_orange

            text "" size 6

            for trait in girl.traits:
                hbox:
                    frame background None ypadding 0 xsize 150 xfill True xalign 0.0 yalign 0.0:
                        text trait_name_dict[trait.name] xmaximum 150 yalign 0.0 size 14 bold True:
                            if trait in gold_traits:
                                color c_orange
                            elif trait in pos_traits:
                                color c_emerald
                            elif trait in neg_traits:
                                color c_crimson
                    text trait.get_description(short=True) xmaximum 250 size 14

            text "" size 6

            if girl.perks:

                text girl.name + "的特质树" xalign 0.5 color c_orange

                text "" size 6

                for perk in girl.perks:
                    hbox:
                        frame background None ypadding 0 xsize 150 xfill True xalign 0.0 yalign 0.0:
                            text perk.name xmaximum 150 yalign 0.0 size 13 bold True
                        text perk.get_description(short=True) xmaximum 250 size 13


screen perk_details(girl):

    tag trait_details

    if girl.perks:
        frame:
            background c_ui_darker
            xalign 0.5
            yalign 0.8
            xsize int(config.screen_width / 2.8)
            ymaximum int(config.screen_height*0.8)

            has vbox spacing 3

            text girl.name + "已激活的特质树" xalign 0.5 color c_orange

            text "" size 6

            for perk in girl.perks:
                hbox:
                    frame background None ypadding 0 xsize 150 xfill True xalign 0.0 yalign 0.0:
                        text perk.name xmaximum 150 yalign 0.0 size 13 bold True
                    text perk.get_description(short=True) xmaximum 250 size 13





## GIRL LOG SCREEN ## Displays statistics about each girl

screen girl_log(): # Reminder: selected_girl is a Global variable that holds the currently selected girl

    modal True

    key "mouseup_3" action Return()

    use dark_filter(can_click=False)

#     $ girl = selected_girl
    $ log_dict = compile_girl_log(selected_girl) # Hands the screen a dictionary holding all calculations (to avoid refreshing calc with every frame)

    default days = 1

    $ biggest = 24

    $ big = 18

    $ average = 14

    $ small = 12

    frame:
        background None
        yalign 0.5
        ypadding 0
        ymargin 20

        has vbox

        frame:
            xmargin 40
            ymargin 0
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5

            yfill False
            xfill True

            has vbox

            use close(Return())
            use girl_select(MC.girls, orange = True)

            text "" size average
            text "" size average

            hbox:

                xfill True
                yfill False

                textbutton "昨天" action SetScreenVariable("days", 1) xsize 200 background c_brown + "AA" text_color c_white selected_idle_background c_orange + "AA" selected_hover_background c_orange + "AA" hover_background c_orange + "55"

                textbutton "最近7天" action SetScreenVariable("days", 7) xsize 200 background c_brown + "AA" text_color c_white selected_idle_background c_orange + "AA" selected_hover_background c_orange + "AA" hover_background c_orange + "55"

                textbutton "最近28天" action SetScreenVariable("days", 28) xsize 200 background c_brown + "AA" text_color c_white selected_idle_background c_orange + "AA" selected_hover_background c_orange + "AA" hover_background c_orange + "55"

                textbutton "所有时间" action SetScreenVariable("days", 0) xsize 200 background c_brown + "AA" text_color c_white selected_idle_background c_orange + "AA" selected_hover_background c_orange + "AA" hover_background c_orange + "55"


        frame:
            xmargin 40
            ymargin 0
            xpadding 40
            ypadding 20

            xalign 0.5
            yalign 0.5
            xfill False
            yfill False

            has vbox

            xfill True
            yfill False
            xalign 0.5

            hbox:
                vbox:
                    hbox:
                        spacing 150

                        vbox:
                            text "综述" size average color c_prune

                            text "" size average

                            grid 5 2:

                                transpose True
                                spacing 3

                                text "{b}天数{/b}" color c_darkgrey size small xalign 0.5

                                if days == 0:
                                    text str(log_dict["age"]) size average color c_prune xalign 0.5

                                elif days > log_dict["age"]:
                                    text str(log_dict["age"]) size average color c_prune xalign 0.5

                                else:
                                    text str(days) size average color c_prune xalign 0.5

                                text "{b}金币{/b}" color c_darkgold size small xalign 0.5

                                $ j_gold = log_dict["total_gold"][days]
                                $ q_gold = log_dict["quest_gold"][days]
                                $ upk = log_dict["upkeep"][days]
                                $ net = j_gold + q_gold - upk

                                if round_int(net) < 0:
                                    $ col1 = c_red
                                elif round_int(net) > 0:
                                    $ col1 = c_green
                                else:
                                    $ col1 = c_white

                                $ ttip = "{b}获利: {color=[c_white]}" + str_int(net) + "{/color}{/b}"
                                $ ttip += "\n工作: {color=[c_green]}" + str_int(j_gold) + "{/color}"
                                $ ttip += "     任务: {color=[c_green]}" + str_int(q_gold) + "{/color}"
                                $ ttip += "\n保养费: {color=[c_red]}-" + str_int(upk) + "{/color}"

                                textbutton str_int(j_gold + q_gold) background None xpadding 0 ypadding 0 xmargin 0 ymargin 0 text_size average text_color c_prune xalign 0.5 action NullAction() tooltip ttip

                                text "{b}经验{/b}" color c_emerald size small xalign 0.5

                                text str_int(log_dict["total_xp"][days]) size average color c_prune xalign 0.5

                                text "{b}职业经验{/b}" color c_orange size small xalign 0.5

                                text str_int(log_dict["total_jp"][days]) size average color c_prune xalign 0.5

                                text "{b}声望{/b}" color c_purple size small xalign 0.5

                                text str_int(log_dict["total_rep"][days]) size average color c_prune xalign 0.5

                        vbox:
                            text "活跃" size average color c_prune

                            hbox:

                                spacing 20

                                grid 2 4:

                                    spacing 3

                                    text "" size small

                                    text "{b}天数{/b}" color c_darkgrey size small xalign 0.5

                                    text "{b}已工作{/b}" color c_orange size small xalign 0.5

                                    $ ttip = "服务员: " + str_int(log_dict["waitress_days"][days]) + "              舞娘: " + str_int(log_dict["waitress_days"][days]) + "\n按摩师: " + str_int(log_dict["masseuse_days"][days]) + "            艺伎: " + str_int(log_dict["geisha_days"][days]) + "\n妓女: " + str_int(log_dict["whore_days"][days]) + "                 工作/卖淫 : " + str_int(log_dict["work_whore_days"][days])

                                    textbutton str_int(log_dict["work_days"][days]) background None xpadding 0 ypadding 0 xmargin 0 ymargin 0 text_size average text_color c_brown xalign 0.5 action NullAction() hovered tt.Action(ttip)

                                    text "{b}休息{/b}" color c_green size small xalign 0.5

                                    text str_int(log_dict["rest_days"][days]) size average color c_brown xalign 0.5

                                    text "{b}离开{/b}" color c_blue size small xalign 0.5

                                    text str_int(log_dict["away_days"][days] + log_dict["farm_days"][days]) size average color c_brown xalign 0.5

                                grid 2 3:

                                    spacing 3

                                    text "" size small

                                    text "{b}天数{/b}" color c_darkgrey size small xalign 0.5

                                    text "{b}罢工{/b}" color c_red size small xalign 0.5

                                    text str_int(log_dict["strike_days"][days]) size average color c_brown xalign 0.5

                                    text "{b}受伤{/b}" color c_red size small xalign 0.5

                                    text str_int(log_dict["hurt_days"][days] + log_dict["sick_days"][days]) size average color c_brown xalign 0.5

#                                    text "{b}Sick{/b}" color c_red size small xalign 0.5

#                                    text str_int(log_dict["sick_days"][days]) size average color c_brown xalign 0.5

                    text "" size average

    #            vbox:

                    text "工作" size average color c_prune

#                    text "" size average

                    grid 7 6:

                        spacing 1

                        text "" size small

                        text "{b}顾客{/b}" color c_darkgrey size small xalign 0.5

                        text "{b}金币{/b}" color c_darkgold size small xalign 0.5

                        text "{b}经验{/b}" color c_emerald size small xalign 0.5

                        text "{b}职业经验{/b}" color c_orange size small xalign 0.5

                        text "{b}声望{/b}" color c_purple size small xalign 0.5

                        text "{b}平均分值{/b}" color c_crimson size small xalign 0.5

                        for job in all_jobs:

                            text "{b}" + girl_related_dict[job.capitalize()] + "{/b}" color c_firered size small xalign 0.5

                            text str_int(log_dict[job + "_cust"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[job + "_gold"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[job + "_xp"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[job + "_jp"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[job + "_rep"][days]) size average color c_brown xalign 0.5

                            $ perf, ttip = log_dict[job + "_perf"][days]

                            if perf <= 2:
                                $ col1 = c_red
                            elif perf <= 5:
                                $ col1 = c_lightred
                            elif perf <= 8:
                                $ col1 = c_brown
                            elif perf <= 11:
                                $ col1 = c_lightgreen
                            elif perf <= 14:
                                $ col1 = c_green
                            else:
                                $ col1 = c_orange

                            textbutton str(perf) background None xpadding 0 ypadding 0 xmargin 0 ymargin 0 text_size average text_color col1 xalign 0.5 action NullAction() hovered tt.Action(ttip)


                        text "{b}妓女{/b}" color c_firered size small xalign 0.5

                        text str(round_int(log_dict["whore_cust"][days])) size average color c_brown xalign 0.5

                        text str_int(log_dict["whore_gold"][days]) size average color c_brown xalign 0.5

                        text str_int(log_dict["whore_xp"][days]) size average color c_brown xalign 0.5

                        text str_int(log_dict["whore_jp"][days]) size average color c_brown xalign 0.5

                        text str_int(log_dict["whore_rep"][days]) size average color c_brown xalign 0.5

                        $ perf, ttip = log_dict["whore_perf"][days]

                        if perf <= 2:
                                $ col1 = c_red
                        elif perf <= 5:
                            $ col1 = c_lightred
                        elif perf <= 8:
                            $ col1 = c_prune
                        elif perf <= 11:
                            $ col1 = c_lightgreen
                        elif perf <= 14:
                            $ col1 = c_green
                        else:
                            $ col1 = c_orange

                        textbutton str(perf) background None xpadding 0 ypadding 0 xmargin 0 ymargin 0 text_size average text_color col1 xalign 0.5 action NullAction() hovered tt.Action(ttip)


                    text "" size average

                    text "性行为" size average color c_prune

#                    text "" size average

                    grid 7 5:

                        spacing 1

                        text "" size small

                        text "{b}顾客{/b}" color c_darkgrey size small xalign 0.5

                        text "{b}金币{/b}" color c_darkgold size small xalign 0.5

                        text "{b}经验{/b}" color c_emerald size small xalign 0.5

                        text "{b}职业经验{/b}" color c_orange size small xalign 0.5

                        text "{b}声望{/b}" color c_purple size small xalign 0.5

                        text "{b}平均分值{/b}" color c_crimson size small xalign 0.5

                        for act in all_sex_acts:

                            text "{b}" + girl_related_dict[act.capitalize()] + "{/b}" color c_firered size small xalign 0.5

                            text str_int(log_dict[act + "_cust"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[act + "_gold"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[act + "_xp"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[act + "_jp"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[act + "_rep"][days]) size average color c_brown xalign 0.5

                            $ perf, ttip = log_dict[act + "_perf"][days]

                            textbutton str(perf) background None xpadding 0 ypadding 0 xmargin 0 ymargin 0 text_size average text_color c_prune xalign 0.5 action NullAction() hovered tt.Action(ttip)



## DISTRICT SCREEN ##

screen districts(context = "visit"): # returns a chosen district. Context can

    zorder 0

    if context == "visit":
        key "mouseup_3" action ((Hide("districts"), Hide("tool"), Jump("main")))
        use shortcuts()

    $ i = 1
    for dis in all_districts:
        if dis.chapter <= game.chapter:
            key str(i) action Return(dis)
            $ i += 1

    frame:
        background "bg zan"
        xysize (config.screen_width, int(config.screen_height*0.8))
        xfill True
        yfill True

        has hbox

#        spacing 60
        xalign 0.5
        yalign 0.5

        vbox:
            xsize int(config.screen_width * 0.25)
            yalign 0.5
            ysize 400
            yfill True

            text "要求\n没有执照" xalign 0.5 yalign 0.0 size 16 text_align 0.5 color c_darkgrey

            use district_button(district_dict["slum"], context) id "b1"


        vbox:
            yalign 0.5
            spacing 60
            xsize int(config.screen_width * 0.25)
            ysize 400
            yfill True

            hbox:
                xalign 0.5
                spacing 10


                if game.chapter >= 2:

                    add ProportionalScale("UI/" + license_dict[1][1], 50, 50) xalign 0.5

                else:

                    add ProportionalScale("UI/" + license_dict[0][1], 50, 50) xalign 0.5

                text "要求\n皮条客执照" xalign 0.5 yalign 0.0 size 16 text_align 0.5 color c_darkgrey

            use district_button(district_dict["warehouse"], context) id "b2"
            use district_button(district_dict["docks"], context) id "b3"



        vbox:
            yalign 0.5
            spacing 60
            xsize int(config.screen_width * 0.25)
            ysize 400
            yfill True

            hbox:
                xalign 0.5
                spacing 10

                if game.chapter >= 4:

                    add ProportionalScale("UI/" + license_dict[2][1], 50, 50)

                else:

                    add ProportionalScale("UI/" + license_dict[0][1], 50, 50)

                text "要求\n妓女贩执照" xalign 0.5 yalign 0.0 xsize 160 size 16 text_align 0.5 color c_darkgrey

            use district_button(district_dict["gardens"], context)  id "b4"
            use district_button(district_dict["cathedra"], context)  id "b5"


        vbox:

            yalign 0.5
            xsize int(config.screen_width * 0.25)
            ysize 400
            yfill True

            hbox:
                xalign 0.5
                spacing 10

                if game.chapter >= 6:

                    add ProportionalScale("UI/" + license_dict[3][1], 50, 50)

                else:

                    add ProportionalScale("UI/" + license_dict[0][1], 50, 50)

                text "要求\n青楼主执照" xalign 0.5 yalign 0.0 xsize 150 size 16 text_align 0.5 color c_darkgrey

            use district_button(district_dict["hold"], context)  id "b6"

    if context != "first visit":
        use overlay("districts")
    if context == "visit":
        use close((Hide("districts"), Hide("tool"), Jump("main")))


screen district_button(dis, context):

    button:
        xalign 0.5
        ycenter 0.5
        xpadding 6
        ypadding 6

        if game.chapter >= dis.chapter:
            if context != "relocate" or (dis not in game.blocked_districts and district != dis):
                action Return(dis)

        vbox:

            spacing 10

            text location_name_dict[dis.name] size 14 xalign 0.5

            fixed:
                fit_first True

                add dis.get_pic(150, 100) alpha 0.66 insensitive_alpha 0.33 hover_alpha 1.0

                $ max_love = 0

                for loc in location_dict[dis.name]:
                    for girl in loc.girls:
                        if girl.love > max_love:
                            $ max_love = girl.love

                if max_love > 0:

                    $ h = max_love // 2

                    add ProportionalScale("UI/heart.webp", h, 50) xalign 0.5 yalign 0.4 idle_alpha 0.66 hover_alpha 0.8

                text str(all_districts.index(dis) + 1) size 14  xalign 0.05 yalign 0.95


screen visit_district():

    zorder 0

    key "mouseup_3" action (SetVariable("selected_destination", "districts"), Jump("teleport"))
    use close((SetVariable("selected_destination", "districts"), Jump("teleport")))
    use shortcuts()

    $ available_districts = [d for d in all_districts if d.chapter <= game.chapter]

    key "K_LEFT" action (SetVariable('selected_district', get_previous(available_districts, selected_district, loop=True)), Jump("visit_district"))
    key "K_RIGHT" action (SetVariable('selected_district', get_next(available_districts, selected_district, loop=True)), Jump("visit_district"))

    textbutton "<" xalign 0.05 ysize 120 yalign 0.4 action (SetVariable('selected_district', get_previous(available_districts, selected_district, loop=True)), Jump("visit_district")) tooltip "Visit the previous district (you can use arrow keys)."

    textbutton ">" xalign 0.95 ysize 120 yalign 0.4 action (SetVariable('selected_district', get_next(available_districts, selected_district, loop=True)), Jump("visit_district")) tooltip "Visit the next district (you can use arrow keys)."

    $ i = 1
    for loc in location_dict[selected_district.name]:
        key str(i) action Return([loc, "go"])

        # Shortcut added by Lokplart
        if loc.can_do_action():
            key "alt_K_" + str(i) action Return([loc, "special"])

        $ i += 1

    frame:
        background None
        xysize (config.screen_width, int(config.screen_height*0.8))
        xfill True
        yfill True

        has vbox

        xalign 0.5
        yalign 0.5

        text location_name_dict[selected_district.name] xalign 0.5

        text ""
        text ""

        grid 3 2:

            spacing 50

            for location in location_dict[selected_district.name]:

                button:

                    xalign 0.5
                    yalign 0.33
                    xpadding 6
                    ypadding 6

                    action Return([location, "go"])

                    if location.secret:
                        tooltip "你还没有发现这个地点。"
                    else:
                        tooltip "{b}" + location_name_dict[location.name] + "{/b} 按下" + str(location_dict[selected_district.name].index(location) + 1) + "参观该地点。"

                    vbox:

                        spacing 10

                        if location.secret:

                            text "???" size 14 xalign 0.5

                            add im.Scale("districts/locations/secret.jpg", 150, 100) insensitive_alpha 0.33 idle_alpha 0.66 hover_alpha 1.0

                        else:


                            text location_name_dict[location.name] size 14 xalign 0.5

                            fixed:
                                fit_first True
                                add location.get_pic(150, 100) insensitive_alpha 0.33 idle_alpha 0.66 hover_alpha 1.0

                                $ max_love = 0

                                for girl in location.girls:
                                    if girl.love > max_love:
                                        $ max_love = girl.love

                                if max_love > 0:

                                    $ h = max_love // 2

                                    add ProportionalScale("UI/heart.webp", h, 50) xalign 0.5 yalign 0.4 insensitive_alpha 0.33 idle_alpha 0.66 hover_alpha 0.8

                                if location.action:
                                    button xsize 50 ysize 50 xpos 105 ypos 55 background None xmargin 0 ymargin 0 xpadding 0 ypadding 0:
                                        if location.can_do_action():
                                            add location_tb[location.menu[1]] insensitive_alpha 0.33 idle_alpha 0.66 hover_alpha 1.0
                                        else:
                                            add location_tb[location.menu[1]] + " grey" insensitive_alpha 0.33 idle_alpha 0.66 hover_alpha 1.0

                                        if location.menu_costs_AP and MC.interactions < 1:
                                            action NullAction()
                                            tooltip location.menu[0] + " 你不能进行采集，因为你没有行动点数。"
                                        else:
                                            action Return([location, "special"])
                                            if location.menu_costs_AP:
                                                tooltip location.menu[0] + " 费用1{image=img_AP}"
                                            else:
                                                tooltip location.menu[0] + ""

                                text str(location_dict[selected_district.name].index(location) + 1) size 14  xalign 0.05 yalign 0.95

    use overlay("visit_district")
    use close((Hide("visit_district"), Jump("districts")))


screen visit_location():

    zorder 0

    key "mouseup_3" action (SetVariable("selected_destination", "visit_district"), Jump("teleport"))
    use close((SetVariable("selected_destination", "visit_district"), Jump("teleport")))
    use shortcuts()

    # Note: won't work if two locations are secret next to each other (shouldn't happen)

    $ _previous = get_previous(location_dict[selected_district.name], selected_location, loop=True)
    if _previous.secret:
        $ _previous = get_previous(location_dict[selected_district.name], _previous, loop=True)
    $ _next = get_next(location_dict[selected_district.name], selected_location, loop=True)
    if _next.secret:
        $ _next = get_next(location_dict[selected_district.name], _next, loop=True)

    key "K_LEFT" action (SetVariable('selected_location', _previous), Jump("visit_location"))
    key "K_RIGHT" action (SetVariable('selected_location', _next), Jump("visit_location"))

    textbutton "<" xalign 0.05 ysize 120 yalign 0.4 action (SetVariable('selected_location', _previous), Jump("visit_location")) tooltip "访问该地区上一个的位置（您可以使用箭头键）."

    textbutton ">" xalign 0.95 ysize 120 yalign 0.4 action (SetVariable('selected_location', _next), Jump("visit_location")) tooltip "访问该地区下一个的位置（您可以使用箭头键）."

    frame:
        background None # loc.get_pic(config.screen_width, int(config.screen_height*0.8))
        xysize (config.screen_width, int(config.screen_height*0.8))
        xfill True
        yfill True

        has vbox
        xalign 0.5
        yalign 0.7
#        yfill True

        text location_name_dict[selected_location.name] xalign 0.5

        text ""
        text ""

        hbox xalign 0.5 ysize 280:

            spacing 30

            for girl in selected_location.girls:

                button:
                    xalign 0.5
                    yalign 0.33
                    xpadding 6
                    ypadding 6


                    action Return(girl)
                    if girl.MC_interact:
                        tooltip "与" + girl.fullname + "交谈."
                    else:
                        tooltip "跟未知女孩搭讪."

                    vbox:

                        spacing 10

                        if girl.MC_interact:
                            text girl.fullname size 14 xalign 0.5:
                                if girl.original:
                                    color c_yellow
                        else:
                            text "?" size 14 xalign 0.5

                        fixed:
                            fit_first True
                            xmaximum 240
                            ymaximum 240
                            xfill False
                            yfill False

                            add girl.profile.get(240, 240) insensitive_alpha 0.33 idle_alpha 0.8 hover_alpha 1.0 xalign 0.5

                            if girl.love > 0:

                                $ h = girl.love // 2

                                add ProportionalScale("UI/heart.webp", h, 50) xalign 0.99 yalign 0.01 idle_alpha 0.66 hover_alpha 0.8

                            if persistent.show_girlpack_rating in ("In market and city", "Everywhere"):

                                $ rating, ttip = get_girlpack_rating(girl)

                                textbutton "女孩图片包评级(" + capitalize(girl.path.split("/")[-1]) + "): " + rating background c_ui_darkblue text_size 18 yalign 1.0 xmargin 10 ymargin 10 action NullAction() tooltip ttip

        text ""
        text ""

        hbox:
            spacing 25
            xalign 0.5

            textbutton "环顾四周":
                text_size 18
                xsize 240
                ysize 50

                if MC.interactions > 0:
                    action Return("visit")
                    tooltip "浏览此位置."

            if selected_location.action:
                textbutton selected_location.menu[0] text_size 18 xsize 240 ysize 50:

                    if MC.interactions > 0 or not selected_location.menu_costs_AP:
                        action Return("special")

            if story_flags["ninja hunt"] and story_flags["ninja hunt"] != calendar.time and not story_flags["ninja hunt hide " + selected_location.name] and selected_district.rank <= 2:
                textbutton "狩猎忍者" text_size 18 xsize 240 ysize 50:

                    if MC.interactions > 0:
                        action Return("hunt")
                    tooltip "猎杀居住在这个地方的忍者."

    use overlay("visit_location")
    use close((Hide("visit_location"), Jump("visit_district")))



## BROTHEL SCREEN ##

screen brothel():

    zorder 0
    use overlay("brothel")

    if not brothel_firstvisit:
        key "mouseup_3" action (Hide("brothel"), Jump("main"))
        key "o" action Return("open options")
        use close ((Hide("brothel"), Jump("main")))
        use shortcuts()

        if MC.trainers:
            key "K_LEFT" action Function(MC.cycle_trainers, reverse = True)
            key "K_RIGHT" action Function(MC.cycle_trainers)

    if debug_mode: # Checks the UI with a different bg
        key "n" action (Function(brothel.cycle_pic))
        key "N" action (Function(brothel.cycle_pic, reverse=True))

    vbox xalign 0.9 yalign 0.1 xsize 0.25:
        if district.rank > 1:
            if story_flags["found wagon"]:
                $ text1 = "木匠马车{size=-2}"

                if brothel.current_building:
                    if len(brothel.current_building.name) > 15:
                        $ text1 += "\n(" + brothel.current_building.name[:15] + ". "
                    else:
                        $ text1 += "\n(" + brothel.current_building.name + " "

                    $ max_dur = float(brothel.current_building.duration)
                    $ leftover_dur = round_int(max_dur - (calendar.time - brothel.started_building))

                    if leftover_dur/max_dur <= 0.25:
                        $ text1 += u"\u25d5"
                    elif leftover_dur/max_dur <= 0.5:
                        $ text1 += u"\u25d1"
                    else:
                        $ text1 += u"\u25d4"

                    $ text1 += "" + str(leftover_dur) + "d){/size}"
            else:
                $ text1 = "???"

            textbutton text1 ypadding 5 xfill True action Return("furniture") text_size 18

#             if story_flags["found wagon"] and story_flags["met carpenter"]:
        textbutton "顾客选项" ypadding 5 xfill True action Return("open options") text_size 18

    frame:
        background None
        xpadding 25
        ypadding 0
        ypos 0.1
        ysize 0.7
        xfill True
        yfill True

        has vbox
        spacing 25
        yfill True

        if not brothel_firstvisit:
            hbox xfill True xsize 0.66:
                $ bro_cost = round_int(brothel.get_adv_cost() + brothel.get_sec_cost() + brothel.get_maintenance_cost())
                $ bro_upk = round_int(sum(g.upkeep*g.get_effect("boost", "total upkeep") for g in MC.girls))
                $ farm_upk = round_int(sum(g.upkeep*g.get_effect("boost", "total upkeep")//2 for g in farm.girls))

                $ text1 = "你必须为青楼维护服务支付{b}" + '{:,}'.format(bro_cost) + "{/b}金币. 你还必须付{b}" + '{:,}'.format(bro_upk) + "{/b}金币作为你的女孩们的保养费"

                if farm.active and farm.girls:
                    $ text1 += " 以及{b}" + '{:,}'.format(farm_upk) + "{/b}金币给农场里的女孩"
                $ text1 += " (不考虑特殊效果)."

                textbutton "日常开销: {font=[gui.fuhao]}" + '{:,}'.format(bro_cost + bro_upk + farm_upk) + "{/font}金币" text_size 18 text_xalign 0.0 xalign 0.0 background c_ui_dark xsize 300 ysize 36 action NullAction() tooltip text1
                textbutton brothel.name xalign 0.5 ypadding 5 action Return("change name") hovered tt.Action("单击此处可更改青楼的名称") #background "#00002277"

            hbox:
                xalign 0.5
                xfill True

                vbox spacing 10 xalign 0.0:
                    text "{b}培训师{/b}" size 18 yalign 0.0 drop_shadow (2, 2)

                    frame:
                        xsize 360
                        ysize 200
                        xalign 0.5
                        xpadding 20
                        ypadding 0
                        background c_ui_dark

                        has vbox spacing 10 yalign 0.5

                        hbox spacing 10 xalign 0.5:

                            if MC.trainers:

                                vbox:

                                    button xsize 156 background None xmargin 0 xpadding 0 action NullAction():
                                        hovered tt.Action("培训师帮助你的女孩学习新技能. 通过与Zan居民的交流发现新的培训师!")
                                        add MC.current_trainer.trainer_portrait zoom 1.0 xalign 0.5 yalign 0.5


                                    if len(MC.trainers) == 1:
                                        $ text1 = "没有其他培训师可用"
                                    else:
                                        $ text1 = "培训师帮助你的女孩学习新技能. 通过与Zan居民的交流发现新的培训师!"

                                    button xmargin 0 xpadding 0 xsize 156 background None action NullAction() hovered tt.Action(text1):

                                        has hbox xfill True

                                        textbutton "<" xsize 75 xalign 0.0:
                                            if len(MC.trainers) > 1:
                                                action Function(MC.cycle_trainers, reverse = True)

                                        textbutton ">" xsize 75 xalign 1.0:
                                            if len(MC.trainers) > 1:
                                                action Function(MC.cycle_trainers)

                                vbox:
                                    text "{b}" + MC.current_trainer.name + "{/b}" size 18 xalign 0.5
                                    text "\n" + MC.current_trainer.trainer_description size 14 justify True

                            else:
                                textbutton "?" xsize 100 ysize 150

                                text "{i}招募一名培训师来帮助你的女孩.{/i}" size 14



                vbox spacing 10 xalign 1.0:
                    text "{b}运维{/b}" size 18 yalign 0.0 drop_shadow (2, 2)

                    frame:
                        xsize 580
                        ysize 200
                        xalign 1.0
                        background c_ui_dark

                        has vbox spacing 10 xalign 0.0 yalign 0.5

                        fixed yfill False ysize 120:

                            $ ttip = "你的青楼现在的名声是{b}" + str(brothel.rep) + "{/b}."

                            textbutton "广告" ypos 0.1 text_color c_white ypadding 4 text_size 18 background None action NullAction() hovered tt.Action(ttip) text_align 0.0

                            bar:
                                xsize 200
                                xpos 0.25
                                ypos 0.1
                                value FieldValue(brothel, "advertising", brothel.max_help, action=Function(brothel.update_customer_count))
                                hovered tt.Action("付钱让穿着暴露的辣妹在你的青楼内外闲逛，用以告诉潜在的顾客宣传你的青楼.")

                            $ adv_bonus = brothel.get_effect("change", "advertising")
                            if adv_bonus != 0:
                                $ text1 = " ({color=[c_green]}+" + str(adv_bonus) + "{/color} 来自女孩们)"
                            else:
                                $ text1 = ""
                            $ text2 = brothel.get_adv_cost()

                            textbutton "[brothel.advertising]名辣妹" + text1 background None text_size 14 xpos 0.6 ypos 0.1 ypadding 6

                            $ ttip = "你的青楼目前的威胁等级是" + brothel.estimate_threat_level() + "."

                            textbutton "安全" text_color c_white ypos 0.4 ymargin 0 ypadding 4 text_align 0.0  background None text_size 18 action NullAction() hovered tt.Action(ttip)

                            bar:
                                xsize 200
                                xpos 0.25
                                ypos 0.4
                                value FieldValue(brothel, "security", brothel.max_help)
                                hovered tt.Action("雇佣佣兵(保安)来阻止不守规矩的顾客和竞争对手.")

                            $ sec_bonus = brothel.get_effect("change", "security")
                            if sec_bonus != 0:
                                $ text1 = " ({color=[c_green]}+" + str(sec_bonus) + "{/color} 来自女孩们)"
                            else:
                                $ text1 = ""
                            $ text2 = brothel.get_sec_cost()

                            textbutton "[brothel.security]名保安" + text1 background None text_size 14 xpos 0.6 ypos 0.4 ypadding 6



                            $ ttip = "你的青楼目前的肮脏程度是{b}" + str(round_int(brothel.dirt)) + "{/b}."

                            textbutton "维护" text_color c_white ypos 0.7 ymargin 0 ypadding 4 text_align 0.0 text_size 18 background None action NullAction() hovered tt.Action(ttip)

                            bar:
                                xsize 200
                                xpos 0.25
                                ypos 0.7
                                value FieldValue(brothel, "maintenance", brothel.max_help)
                                hovered tt.Action("雇一个临时保洁队伍来清理你的青楼. 天哪，里面会不会很乱...")

                            $ maint_bonus= brothel.get_effect("change", "maintenance")
                            if maint_bonus != 0:
                                $ text1 = " ({color=[c_green]}+" + str(maint_bonus) + "{/color}名来自女孩们)"
                            else:
                                $ text1 = ""
                            $ text2 = brothel.get_maintenance_cost()

                            textbutton "[brothel.maintenance]名保洁" + text1 background None text_size 14 xpos 0.6 ypos 0.7 ypadding 6

                        hbox xfill True spacing 10:

                            vbox spacing 6 xsize 180:
                                text "预计顾客" size 14
                                textbutton str(brothel.customer_count) + "{image=img_cust}" style "inv_no_padding" action NullAction() tooltip brothel.count_customers_description()

                            vbox spacing 6 xsize 150:
                                text "威胁等级" size 14
                                textbutton brothel.estimate_threat_level() style "inv_no_padding" action NullAction() tooltip "你的青楼目前威胁等级是 " + brothel.estimate_threat_level() + ". 青楼的威胁会受到青楼守卫和你的力量技能的影响."

                            vbox spacing 6 xsize 200:
                                hbox spacing 10:
                                    text "污垢等级" size 14
                                    textbutton "立刻清理" xmargin 10 ymargin 0 ypadding 6 text_size 14:
                                        if brothel.get_clean_up_cost() > 0:
                                            action Return(("clean up", ""))
                                        tooltip "花费" + str(brothel.get_clean_up_cost()) + "金币购买一些清洁材料，然后让希露和仆人把青楼打扫干净."
                                textbutton str(round_int(brothel.dirt)) + " {size=-4}(-" + str_int(brothel.get_maintenance()) + ")" style "inv_no_padding" action NullAction() tooltip maintenance_desc[brothel.get_cleanliness()] yoffset -12


        hbox:
            xalign 0.0
            yalign 1.0
            spacing 36
            yfill False

            if not brothel_firstvisit:
                frame:
                    background None
                    xpadding 6
                    ypadding 6
                    xalign 0.0
                    yalign 0.0
                    xfill False
                    yfill False

                    has vbox spacing 6

                    text "{b}女孩卧室{/b}" size 18 xalign 0.0 drop_shadow (2, 2)

                    frame background c_ui_dark:

                        has vbox spacing 6

                        if brothel.bedrooms < brothel.get_maxbedrooms():
                            $ text1 = "为你的青楼增加一间新的卧室需要" + str(brothel.get_room_price()) +  "金币. 青楼最多只能有 " + str(brothel.get_maxbedrooms()) +  " 间卧室."
                        elif district.rank < 5:
                            $ text1 = "在你搬到另一家青楼之前，你不能再增加任何卧室."
                        else:
                            $ text1 = "你已经达到了卧室数量的上限."

                        button background None xpadding 3 action NullAction():
                            tooltip text1
                            button:
                                xpadding 6
                                ypadding 6
                                insensitive_background c_darkgrey + "E5"
                                tooltip text1

                                if brothel.bedrooms < brothel.get_maxbedrooms():
                                    action renpy.curried_invoke_in_new_context(brothel.add_room) ## PRAISE BE TO ASCEAI Never would have found this on my own

                                vbox:
                                    spacing 3


                                    fixed:
                                        fit_first True

                                        add brothel.get_bedroom_pic(120, 80) idle_alpha 0.66 hover_alpha 1.0

                                        if brothel.bedrooms < brothel.get_maxbedrooms():
                                            text "+" xalign 0.5 yalign 0.5 size 36

                                        text "[brothel.bedrooms]{size=-8}/" + str(brothel.get_maxbedrooms()) xalign 0.9 yalign 0.1

                                    text "[brothel.bedroom_type.name]" size 14 xcenter 0.5


                    if brothel.bedroom_type.level < brothel.maxupgrade:
                        $ ttip = "改良你所有的卧室需要" + str(brothel.get_room_upgrade_price(brothel.bedrooms)) + "金币. 升级后的卧室对女孩和顾客来说都更加舒适."
                        textbutton "升级卧室":
                            xalign 0.5
                            text_size 18
                            action renpy.curried_invoke_in_new_context(brothel.upgrade_bedrooms)
                            tooltip ttip

                frame:
                    background None
                    xpadding 6
                    ypadding 6
                    xalign 0.0
                    yalign 0.0
                    xfill False
                    yfill False

                    has vbox spacing 6

                    text "{b}主人卧室{/b}" size 18 xalign 0.0 drop_shadow (2, 2)

                    frame background c_ui_dark:

                        has vbox spacing 6

                        button background None xpadding 3 action NullAction():
                            tooltip brothel.master_bedroom.get_description()
                            button:
                                xpadding 6
                                ypadding 6
                                insensitive_background c_darkgrey + "E5"
                                tooltip brothel.master_bedroom.get_description()

                                if brothel.master_bedroom.level < brothel.rank:
                                    action renpy.curried_invoke_in_new_context(brothel.upgrade_master_bedroom)

                                vbox:
                                    spacing 3

                                    fixed:
                                        fit_first True

                                        add brothel.master_bedroom.get_pic(120, 80, proportional=False) idle_alpha 0.66 hover_alpha 1.0

                                        if brothel.master_bedroom.level:
                                            text str(brothel.master_bedroom.level) xalign 0.9 yalign 0.1
                                            hbox xalign 0.1 yalign 0.95:
                                                for girl in brothel.master_bedroom.girls:
                                                    button background c_white yalign 0.5 xmargin 2 ymargin 0 xpadding 1 ypadding 1:
                                                        action NullAction()
                                                        tooltip girl.fullname + "目前被分配到主卧室."
                                                        add girl.portrait.get(20, 20) alpha 1.0


#                                             text str(len(brothel.master_bedroom.girls)) + "/{size=-8}" + str(brothel.master_bedroom.level) xalign 0.9 yalign 0.1


                                        if brothel.master_bedroom.level < brothel.rank:
                                            text "+" xalign 0.5 yalign 0.5 size 36

                                    text brothel.master_bedroom.name size 14 xcenter 0.5


            frame:
                background None
                xpadding 6
                ypadding 6
                xalign 1.0
                yalign 0.0
                xfill False
                yfill False

                has vbox
                spacing 6

                text "{b}一般房间{/b}" size 18 xalign 0.0 drop_shadow (2, 2)

                frame:
                    background c_ui_dark
                    xpadding 0
                    has hbox spacing 0

                    for room_name in all_common_rooms:

                        $ room = brothel.rooms[room_name]

                        vbox xfill False yfill False:
                            button background None action NullAction() hovered tt.Action(room.get_description()):
                                button:
                                    xpadding 6
                                    ypadding 6
                                    insensitive_background c_darkgrey + "E5"

                                    if room.level < district.rank:
                                        action Return(("add_room", room))
                                        hovered tt.Action(room.get_description())

                                    vbox:
                                        spacing 3

                                        fixed:
                                            fit_first True
                                            add room.pic.get(120, 80) idle_alpha 0.66 hover_alpha 1.0
                                            if not brothel_firstvisit:
                                                text str(room.level) + "{size=-8}/" + str(district.rank) xalign 1.0
                                            if room.level:
                                                text str(room.cust_limit) + "{image=img_cust}" xalign 0.1 yalign 0.9
                                            if room.level < district.rank:
                                                text "+" xalign 0.5 yalign 0.5 size 36

                                        text room.name.capitalize() size 14 xcenter 0.5


    # Additional button specifically for the harem mod

    if game.has_active_mod("Harem"):
        if MC.current_trainer.name in harem_mod.talkative_NPCs:
            use harem_button()


# BROTHEL SUBSCREENS

screen furniture():

    key "mouseup_3" action (Return("quit"))

    use overlay("wagon")
    use shortcuts()
    use close(Return("quit"))

    frame ypos 0.05 background None xmargin 20 ymargin 20:

        has vbox spacing 10

        text "木匠马车" bold True xalign 0 yalign 0

        hbox spacing 6 xfill True ysize 120:
            add "side carpenter" zoom 0.8 yalign 0.5

            if not brothel.current_building:
                $ text1 = "喔，嗨. 为我找了一份新工作?"
            else:
                $ text1 = "我还在努力制作" + brothel.current_building.name + ". 你应该晚点再来."

            text text1 xsize 0.4 yalign 0.5 size 18 justify True italic True

            vbox xsize 0.4 yfill True xalign 1.0:
                text "可用资源" drop_shadow (2, 2) size 18
                frame xfill True yfill True background c_ui_brown xpadding 0 ypadding 0:
                    use resource_tab(y=0.0, sz=24)

            vbox xsize 0.6 yfill True xalign 1.0:
                text "建筑队列" drop_shadow (2, 2) size 18
                frame xfill True yfill True background c_ui_brown:
                    if brothel.current_building:
                        $ dur = brothel.current_building.duration - (calendar.time - brothel.started_building)
                        button xfill False yfill False xalign 0.5 yalign 0.5 background None:
                            action NullAction()
                            tooltip (brothel.current_building.description + "\n还有 " + str(dur) + " 天完成。")
                            add brothel.current_building.pic.get(50, 50) xalign 0.5 yalign 0.5
                            text str(dur) + "d" xalign 1.0 yalign 0.0 size 18
                    else:
                        text "没有正在进行的建筑." italic True size 14

        text brothel.name + "的装饰和家具" drop_shadow (2, 2) size 18

        if brothel.furniture:
            frame xfill True background c_ui_brown:
                has hbox spacing 6 box_wrap True
                for furn in brothel.furniture:
                    button background c_ui_brown action NullAction() tooltip furn.description xsize 52 ysize 44 xpadding 0 ypadding 0:
                        add furn.pic.get(48, 40) xalign 0.5 yalign 0.5

        text "建筑模版" drop_shadow (2, 2) size 18

        frame background c_ui_dark:
            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                ysize 0.6
                yfill True

                has vbox

                for type, description in furniture_types:
                    $ builds = [f for f in all_furniture if f.type == type and f.can_build()]

                    if builds:
                        text "{b}" + setting_name_dict[type.capitalize()] + "{/b} - {i}" + description size 14
                        frame xfill True background c_ui_brown:
                            hbox spacing 6 box_wrap True:
                                for furn in builds:
                                    if furn.duration < 2:
                                        $ text2 = furn.description + " (" + str(furn.duration) + "天完成)"
                                    else:
                                        $ text2 = furn.description + " (" + str(furn.duration) + "天完成)"
                                    button xsize 110 ysize 90 xpadding 2 ypadding 2:
                                        action Return(furn)
                                        tooltip text2
                                        add furn.pic.get(90, 70) xalign 0.5 ypos 0.05 hover_alpha 1.0 idle_alpha 0.8
                                        button xalign 0.5 yalign 1.0 xpadding 0 ypadding 0 background c_ui_brown xfill True:
                                            action Return(furn)
                                            tooltip text2
                                            use resource_tab(furn.cost, sp=1)
                                        text str(furn.duration) + "天" xalign 0.95 yalign 0.05 size 18
#                        else:
#                            text "You have built every available " + type +"." size 14 italic True
                    text "" size 8


screen brothel_options():

    zorder 0
    use overlay("customers")

    key "mouseup_3" action (Return("close options"))
    use close(Return("close options"))
    use shortcuts()

    frame:
        background None
        xpadding 25
        ypadding 0
        ypos 0.1
        xfill True
        ysize 0.88

        has hbox spacing 10 yfill True

        if story_flags["found wagon"] and story_flags["met carpenter"]:
            vbox xsize 320:
                text "{b}顾客数量{/b}" size 18 yalign 0.0 drop_shadow (2, 2)

                frame xpadding 10 ypadding 10 xfill True yfill True:
                    has vbox spacing 6
                    text "选择吸引哪些顾客到你的青楼(建造装饰以吸引更多顾客)" size 14 italic True color c_brown

                    vbox xfill True spacing 4:
                        for pop in all_populations:
                            hbox spacing 6:
                                button background None xalign 0.0 yalign 0.5:
                                    action NullAction()
                                    if brothel.get_effect("allow", pop.name):
                                        add pop.get_pic(40, 40)
                                        tooltip (""+pop.description)
                                    else:
                                        add im.MatrixColor(pop.get_pic(40, 40), im.matrix.desaturate())
                                        tooltip "{size=-1}必须在木匠马车上建造新的装饰物来吸引这些顾客."

                                if brothel.get_effect("allow", pop.name):
                                    vbox spacing 0:
                                        $ total_budget, ent_budget, wh_budget = pop.get_average_budgets(description=True)
                                        hbox spacing 6 xalign 0.0:
                                            bar xsize 100 yalign 0.0 value FieldValue(pop, "weight", 5, action=Function(brothel.update_customer_count))
                                            text attract_pop_dict[pop.weight] color c_brown size 14 yalign 1.0
                                        textbutton "平均预算: %s金币" % total_budget xalign 0.0 yalign 1.0 xmargin 0 xpadding 0 ymargin 0 ypadding 0 background None text_color c_prune text_size 14 action NullAction() tooltip "这是%s的平均{b}最大预算{/b}. (用于娱乐的%s金币，用于嫖娼的%s金币)" % (setting_name_dict[pop.name], ent_budget, wh_budget)
            vbox xsize 320:
                text "{b}顾客偏好{/b}" size 18 yalign 0.0 drop_shadow (2, 2)

                frame xfill True xpadding 10 ypadding 10:
                    has vbox spacing 6
                    text "影响顾客对娱乐和性行为的偏好(建造家具以获得更大的提升)" size 14 italic True color c_brown

                    vbox spacing 12:
                        for target in (all_jobs, all_sex_acts):
                            vbox ysize 0.5 spacing 6:
                                for pref in target:
                                    hbox spacing 6:
                                        textbutton girl_related_dict[pref.capitalize()] xsize 120 ypadding 5 text_size 18 yalign 0.5:
                                            action NullAction()

                                            if brothel.get_effect("allow", pref + " preference"):
                                                tooltip "修改此设置可更改顾客对选择'" + girl_related_dict[pref] + "'服务的优先权提升" + str(50*brothel.get_effect("allow", pref + " preference")) + "%."
                                            else:
                                                background "#CCB8A0"
                                                text_color c_white
                                                tooltip "你必须在木匠的马车上做相应的装饰或家具才能修改顾客选择'" + girl_related_dict[pref] + "'服务的优先权."

                                        if brothel.get_effect("allow", pref + " preference"):

                                            bar xsize 100 xpos 0 yalign 0.0 value DictValue(game.customer_preference_weight, pref, brothel.get_effect("allow", pref + " preference"), action=Function(brothel.update_customer_count))

                                            if game.customer_preference_weight[pref]:
                                                text percentage_description(0.5*game.customer_preference_weight[pref]) color c_brown size 14 yalign 0.5
                                            else:
                                                text "" size 14 yalign 0.5

                text "" size 22
                text "{b}匹配偏好{/b}" size 18 yalign 0.0 drop_shadow (2, 2)

                frame ysize 150 xpadding 10 ypadding 10 xfill True:
                    has vbox spacing 6

                    text "选择如何将顾客与你的女孩进行匹配." size 14 italic True color c_brown

                    if game.matching_priority == "rank":
                        $ text1 = "在可能的情况下，顾客将被匹配到相同等级的女孩."
                    elif game.matching_priority == "act":
                        $ text1 = "在可能的情况下，顾客将被匹配到允许其首选工作或性行为的女孩."

                    textbutton "通过匹配%s" % setting_name_dict[game.matching_priority] action ToggleField(game, "matching_priority", true_value="rank", false_value="act")

                    text text1 size 14 color c_prune


        vbox xsize 320:

            if [f for f in brothel.furniture if f.can_deactivate]:
                text "{b}特殊选项{/b}" size 18 yalign 0.0 drop_shadow (2, 2)

                frame ysize 200 xpadding 10 ypadding 10 xfill True:
                    has vbox spacing 6

                    text "激活或停用特殊青楼家具." size 14 italic True color c_brown

                    hbox box_wrap True:
                        for furn in [f for f in brothel.furniture if f.can_deactivate]:

                            button xsize 56 ysize 56 action Function(furn.toggle) tooltip "点击这里激活或停用%s.\n%s ({b}%s{/b})" % (furniture_name_dict[furn.name], get_description("", furn.effects), {True: "激活", False: "停用"}[furn.active]):

                                add furn.pic.get(50, 50) xalign 0.5 yalign 0.5

                                if not furn.active:
                                    text "X" color c_crimson size 48 xalign 0.5 yalign 0.5

            # This will unlock with the 'billboard' upgrade

            if brothel.get_effect("special", "advanced advertising"):
                text "" size 22
                text "{b}高级设置{/b}" size 18 yalign 0.0 drop_shadow (2, 2)

                frame ysize 200 xpadding 10 ypadding 10 xfill True:
                    has vbox spacing 6

                    text "除了提高你的青楼声誉，广告女孩将增加客户的吸引力和客户预算，基于广告的力量 (创立新的服装以增加广告力量)." size 14 italic True color c_brown

                    hbox spacing 3:
                        vbox xsize 100:
                            text "Customers" size 14 bold True color c_brown yalign 1.0
                            text percentage_description(brothel.get_adv_setting("attraction")) + " to customer attraction" size 14 color c_brown
                        bar xsize 100 xpos 0 yalign 0.0 value FieldValue(brothel, "advertising_setting", range=4, offset=-2, action=Function(brothel.update_customer_count)) tooltip "使用此设置来调整客户吸引力（有多少客户会来青楼）和客户预算（每个客户能够花费的最大金币量）之间的倾向."
                        vbox xsize 100:
                            text "Budget" size 14 bold True color c_brown yalign 1.0
                            #text str(brothel.advertising_setting)
                            text percentage_description(brothel.get_adv_setting("budget") / brothel.max_help) + " to customer budget" size 14 color c_brown

            text "" size 22
            text "{b}来访预测{/b}" size 18 yalign 0.0 drop_shadow (2, 2)
            frame xfill True xpadding 10 ypadding 10:
                has vbox spacing 12
                text brothel.count_customers_description() color c_prune size 14
                text brothel.count_budget_description() color c_prune size 14




## MATCHMAKING SCREENS

screen matchmaking(girls, customers, match_list, context="job"): # Where match list is a list of tuples (girl, customer)

    tag show_screen

    key "mouseup_1" action Return()
    key "mouseup_3" action Return()
    use close(Return(), "next")

    default t = 0
    default n = 0
    default idle_customers = sorted(customers, key= lambda x : x.rank)
    default girl_customers = defaultdict(list)
    default job_customers = defaultdict(int)
    default cust_act = defaultdict(str)
    default load_txt = " (匹配中...)"

    if match_list:
        $ tick = min(1.5 / len(match_list), 0.2) # Takes maximum 1.5 seconds to display all customer matches


#     frame xalign 0.5 yalign 0.95 xsize 900 ysize 720:
    frame background c_ui_dark:
        xalign 0.0
        yalign 0.05
        xsize int(0.95*config.screen_width)
        ysize 615
        left_margin 6
        ymargin 2
        xfill True
        yfill True

        has vbox spacing 10

        if context == "job":
            $ text1 = "娱乐阶段"
        else:
            $ text1 = "嫖娼阶段"

        text text1 + load_txt xalign 0.0 xanchor 0.0 bold True drop_shadow (2, 2) #color c_prune

        frame xfill True ymaximum 160 right_margin 10:
            has hbox spacing 20
            add brothel.get_pic(100, 100)

            vbox spacing 6:
                text "闲置顾客: (%s {image=img_cust})" % (str(len(idle_customers)) + "/" + str(len(customers))) size 18 color c_brown

                if customers:
                    vpgrid rows 4 spacing 3 ymaximum 160:
                        mousewheel True
                        draggable True
                        scrollbars "horizontal"

                        if not idle_customers:
                            text "所有顾客都已被分配." size 12 italic True yalign 0.5 color c_brown
                        else:
                            for cust in idle_customers:
                                button yalign 0.5 xmargin 0 xpadding 0 ymargin 0 ypadding 0 background None action NullAction() tooltip cust.get_description("idle"):
                                    if cust.crazy:
                                        add im.MatrixColor(cust.get_pic(25, 25), im.matrix.desaturate() * im.matrix.tint(1.0, 0.0, 0.0))
                                        at blink
                                    else:
                                        add cust.get_pic(25, 25)

                else:
                    text "没有顾客." size 12 italic True yalign 0.5 color c_brown



        viewport:
            mousewheel True # "change"
            draggable False
            scrollbars "vertical"
            yfill True

            if context == "job":

                vbox spacing 10:
                    for job in all_jobs:
                        $ room = brothel.rooms[job_room_dict[job]]

                        if room.level > 0:
                            frame xfill True yfill False:
    #                             has vbox spacing 3

                                hbox spacing 20:
                                    add room.get_pic(100, 100)

                                    vbox spacing 6:
                                        text room.name.capitalize() + " (%s/%s {image=img_cust})" % (str(job_customers[job]), str(room.cust_limit)) size 18 color c_brown

                                        vbox spacing 3:
                                            for girl in [g for g in girls if g.job == job]:
                                                hbox ysize 25 yalign 0.5:
                                                    button xmargin 0 xpadding 0 ymargin 0 ypadding 0 xsize 45 yalign 0.5 background None action NullAction() tooltip  "{b}" + girl.fullname + ": " + girl_related_dict[girl.job.capitalize()] + " (能力: %s/%s){/b}" % (str(len(girl_customers[girl])), str(girl.get_max_cust_served())):
                                                        add girl.portrait.get(25, 25) xalign 0.5 yalign 0.5

                                                    frame ysize 25 ymargin 0 ypadding 1 background c_ui_brown xfill True:
                                                        has hbox spacing 3 yalign 0.5
                                                        for cust in girl_customers[girl]:
                                                            button xmargin 0 xpadding 0 ymargin 0 ypadding 0 background None action NullAction() tooltip cust.get_description(job): #  xalign 0.0 yalign 0.5 yanchor 0.5
                                                                if cust.crazy:
                                                                    add im.MatrixColor(cust.get_pic(22, 22), im.matrix.desaturate() * im.matrix.tint(1.0, 0.0, 0.0))
                                                                    at blink
                                                                else:
                                                                    add cust.get_pic(22, 22)
                                                        if not girl_customers[girl]:
                                                            text "没有顾客." size 12 italic True yalign 0.5

            elif context == "whore":
                frame xfill True yfill False:
                    has vbox spacing 3
                    $ room = brothel.bedroom_type

                    text "卧室" + " (%s {image=img_cust})" % str(job_customers["whore"]) size 18 color c_brown
                    hbox spacing 20:
                        add room.get_pic(100, 100)

                        vbox spacing 3 box_wrap True:
                            for girl in girls:
                                hbox ysize 25 yalign 0.5:
                                    button xmargin 0 xpadding 0 ymargin 0 ypadding 0 xsize 45 yalign 0.5 background None action NullAction() tooltip "{b}" + girl.fullname + ": " + girl_related_dict[girl.job.capitalize()] + " (interactions: %s/%s).{/b}" % (str(girl.get_max_interactions()-girl.interactions), str(girl.get_max_interactions())):
                                        add girl.portrait.get(25, 25) yalign 0.5

                                    frame ysize 25 ymargin 0 ypadding 1 background c_ui_brown xfill True xmaximum 220:
                                        has hbox spacing 3 yalign 0.5
                                        for cust in girl_customers[girl]:
                                            button xmargin 0 xpadding 0 ymargin 0 ypadding 0 background None action NullAction() tooltip cust.get_description(cust.got_sex_act): #  xalign 0.0 yalign 0.5 yanchor 0.5
                                                if cust.crazy:
                                                    add im.MatrixColor(cust.get_pic(22, 22), im.matrix.desaturate() * im.matrix.tint(1.0, 0.0, 0.0))
                                                    at blink
                                                else:
                                                    add cust.get_pic(22, 22)
                                        if not girl_customers[girl]:
                                            text "没有顾客." size 12 italic True yalign 0.5

    if match_list and len(match_list) > n:
        timer 0.05 repeat True action SetScreenVariable("t", t + 0.05)

        if t >= 0.3 + (tick * n):
            $ girl, cust, act = match_list[n]
            if cust in idle_customers:
                $ idle_customers.remove(cust)
            $ girl_customers[girl].append(cust)
            if act in all_sex_acts:
                $ job_customers["whore"] += 1
            else:
                $ job_customers[girl.job] += 1
            $ cust_act[cust] = act
            $ n += 1

            $ renpy.play(s_click, "sound")
    else:
        $ load_txt = " (done)"



screen customer_satisfaction(customers, old_rep, rep_chg):

    tag show_screen

    default t = 0
    default displayed_rep = old_rep
    default total_change = 0
    default displayed_customers = []

    key "mouseup_1" action Return()
    key "mouseup_3" action Return()
    use close(Return(), "next")

    frame:
        xalign 0.0
        yalign 0.0
        xsize int(0.95*config.screen_width)
        ysize 615
        left_margin 6
        ymargin 2

        has vbox spacing 10

        $ text1 = "青楼名声: %s" % displayed_rep

        if len(displayed_customers) == len(customers):
            $ text1 += " (%s)" % plus_text(total_change)
        else:
            timer 0.05 repeat True action SetScreenVariable("t", t + 0.05)

        # text text1 xalign 1.0 bold True color c_prune

        text text1 xalign 0.0 bold True drop_shadow (2, 2)

        hbox spacing 10:
            text "顾客" bold True color c_brown size 14
            text "满意度" bold True color c_brown size 14
            text "代表变化" bold True color c_brown size 14
            # text "Comment" bold True color c_brown size 14

        viewport:
            mousewheel "change"
            draggable True
            scrollbars True
            xfill True
            yfill True

            vbox spacing 3:

                for cust in displayed_customers:
                    hbox spacing 10:
                        button xsize 80 xalign 0.5 xmargin 0 xpadding 0 ymargin 0 ypadding 0 background None action NullAction() tooltip cust.get_description("end"): #  xalign 0.0 yalign 0.5 yanchor 0.5
                            add cust.get_pic(25, 25) xalign 0.5

                        $ chg = cust.reputation_change

                        if chg > 0:
                            $ col = c_emerald
                        elif chg < 0:
                            $ col = c_crimson
                        else:
                            $ col = None

                        fixed fit_first True ypos -0.2 xsize 100:
                            bar xsize 100 value cust.base_rating range 8 thumb None: # AnimatedValue(value=cust.base_rating, range=8, delay=1.0) Animated value doesn't work :/
                                if col:
                                    left_bar Frame(im.Twocolor("UI/cryslider_full.webp", col, col), 12, 0)
                                    right_bar Frame(im.Twocolor("UI/cryslider_empty.webp", col, col), 12, 0)

                            text "" size 20 xpos 3 + (cust.rank-1)*95/8 ypos 1.16 yanchor 1.0

                        textbutton plus_text(chg) xsize 100 xalign 0.5 yalign 0.65 text_size 14 text_color c_brown text_bold True

                        frame ysize 20 ymargin 0 ypadding 1 background c_ui_brown xsize 400:
                            text cust.reputation_comment size 14 color c_brown

    if t > 0.3 and len(displayed_customers) < len(customers):
        $ idx = min(int(len(customers) * (t - 0.3)), len(customers)) # Takes 1 second to display all customers
        if idx > 0:
            $ displayed_customers = customers[:idx]
            $ total_change = round_int(sum(c.reputation_change for c in displayed_customers))
            $ displayed_rep = min(max(round_int(old_rep + total_change), 0), brothel.max_rep)


## RIGHT MENU : this is the main menu on the main screen (not named main menu to avoid confusion with the standard Renpy screen)

screen home():

    tag menu
    use overlay("main")
    use right_menu
    use shortcuts()

############ Jman - Headhunter Mod ############
    if game.has_active_mod("Headhunter Mod"):
        if game.headhunter_girl:
            $ game.headhunter_button_enabled = 0
            if game.headhunter_time <= 0:
                $ textHH = "猎头公司"
                $ textHH2 = "猎头公司带着你的奖品回来了!"

                if not game.interacting_with_headhunter:
                    textbutton textHH:
                        xalign 0.5
                        yalign 0.0825
                        text_size 36
                        text_font "CHOWFUN_0.TTF"
                        action Jump("headhunter_delivers")
                        hovered tt.Action(textHH2)

            else:
                $ textHH = "猎头公司: [game.headhunter_time]天"
                $ textHH2 = "猎头公司将于[headhunter_time]天回来."

                textbutton textHH:
                    xalign 0.5
                    yalign 0.0825
                    text_size 36
                    text_font "CHOWFUN_0.TTF"
                    hovered tt.Action(textHH2)
        else:
            $ game.headhunter_button_enabled = 1
############ Jman - Headhunter Mod End ########

    if always_show_brothel_report:
        use brothel_report

    button background None action (Hide("brothel_report"), ToggleVariable("always_show_brothel_report")) xalign 0.0 xmargin 25 ypos 0.1 :
        if not always_show_brothel_report:
            hovered (Show("brothel_report"), tt.Action("点击显示青楼报告."))
            unhovered Hide("brothel_report")
        else:
            hovered (tt.Action("点击隐藏青楼报告."))

        hbox xalign 0.0 spacing 10:
            frame xalign 0.0 xsize 25 ysize 25:
                style "gui_button"

                if always_show_brothel_report:
                    text "{font=[gui.fuhao]}✓{/font}" size 14 xalign 0.5 yalign 0.5
                else:
                    text " " size 14 xalign 0.5
            text "显示青楼报告" size 14 xalign 0.0 yalign 0.5


screen brothel_report():

    tag brothel_report

    frame:
        xalign 0.1
        xsize 0.75
        ypos 0.15
        ysize 0.8
        xpadding 10
        ypadding 10

        has vbox spacing 10

        hbox spacing 10:
            if brothel.get_cleanliness() in ("disgusting", "fire"):
                add "side sill sad" zoom 0.5
                text "主人!!! " + brothel.name + "现在非常脏... 请做一些事情!" yalign 0.5 size 18 justify True italic True xmaximum 0.8 color c_brown
            elif calendar.time == 1:
                add "side sill happy" zoom 0.5
                text "欢迎来到你的新青楼，主人! 我相信你会成为一个伟大的管理者!" yalign 0.5 size 18 justify True italic True xmaximum 0.8 color c_brown
            elif logs[calendar.time-1].net >= 0:
                add "side sill happy" zoom 0.5
                text "{color=[c_lightblue]}你知道吗? {/color}" + daily_tip yalign 0.5 size 18 justify True italic True xmaximum 0.8 color c_brown
            else:
                add "side sill sad" zoom 0.5
                text "主人!!! " + brothel.name + "现在亏钱了... 发生了什么事了?" yalign 0.5 size 18 justify True italic True xmaximum 0.8 color c_brown


        hbox spacing 20 xfill True yfill False:

            vbox:
                xsize 0.4
                xfill True
                yfill False

                text "昨日" color c_prune

                # text "" size 14

                if calendar.time > 1:
                    text logs[calendar.time-1].get_day_report() size 14 color c_brown

                    textbutton "显示昨晚的日志" xsize 250 ypadding 5 text_size 14 xalign 0.5:
                        if always_show_brothel_report:
                            action (Show("previous_night_log", log=logs[calendar.time-1]))
                    textbutton "显示满意度报告" xsize 250 ypadding 5 text_size 14 xalign 0.5:
                        if always_show_brothel_report:
                            action Call("latest_customer_satisfaction")

                else:
                    text "没有什么可报告的" size 14 italic True color c_brown

            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                xfill True
                yfill False

                has vbox
                xfill True
                yfill False

                text "今天" color c_prune

                text "" size 14

                text get_next_day_report() size 14 color c_brown

                text "" size 14

                text brothel.get_ASM_report() size 14 color c_brown

                text "" size 14

                text get_warnings() size 14 color c_brown

screen previous_night_log(log):
    modal True

    key "mouseup_3" action (Hide("previous_night_log"))

    use dark_filter

    frame ypos 0.1:
        use night_log(log)

    use close(Hide("previous_night_log"))


## Yes / No Confirmation (used for buying, selling...)


screen yes_no(message, yes_caption="Yes", no_caption="No"):

    modal True

    key "mouseup_3" action (Return(False))

    frame:
        style_group "yesno"

        xfill False
        xpadding .05
        xalign 0.5
        yalign 1.0
        ypadding 25
        ymargin 10
        background c_grey + "CC"

        has vbox:
            xalign .5
            yalign .5
            spacing 25

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _(yes_caption) action Return(True)
            textbutton _(no_caption) action Return(False)


## Ok message (used for giving information...)


screen OK_screen(title="", message="", pic = None, pic_size = "large", dark=False, x=0.6, y=0.7, always_scrollbar=False):

    modal True

    key "mouseup_3" action (Return(True))

    frame:
        style_group "OK"

        xsize int(x*config.screen_width)
        ymaximum int(y*config.screen_height)

        xalign 0.5
        yalign 0.5
        xpadding 25
        ypadding 25
        ymargin 10
        if not dark:
            background c_ui_light
        else:
            background c_ui_darkblue

        has vbox spacing 25

        vpgrid:
            cols 1
            ymaximum 0.9
            mousewheel "change"
            draggable True
            if len(message) > 1250 or always_scrollbar:
                scrollbars "vertical"

            vbox spacing 25 yalign 0.5 xfill True yfill False:

                label _(title):
                    xalign 0.5
                    if not dark:
                        text_color c_darkred
                    else:
                        text_color c_hotpink
                    text_bold True

                if pic:
                    if pic_size == "large":
                        add pic.get(x = 200, y = 200) xalign 0.5

                    elif pic_size == "small":
                        add pic.get(x = 60, y = 60) xalign 0.5

                text _(message):
                    xalign 0.5
                    size 18

                    if not dark:
                        color c_brown
                    else:
                        color c_white

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Ok") action Return(True)


screen tool(x, y, w, h, bg = True):

    tag ttip

    zorder 10

    $ text1 = ""

    if GetTooltip():
        $ text1 = str(GetTooltip())

    elif tt.value != "":
        $ text1 = tt.value

    if text1:
        frame:

            if bg:
                background c_ui_dark

            else:
                background None

            xalign x
            yalign y

            xmaximum w
            ymaximum h

            xmargin 6
            ymargin 3
            ypadding 0

            xfill True
            yfill False

            if count_lines(text1, 44) <= 3:
                $ s = 13
            elif count_lines(text1, 46) <= 3:
                $ s = 12
            elif count_lines(text1, 50) <= 4:
                $ s = 11
            elif count_lines(text1, 54) <= 4:
                $ s = 10
            else:
                $ s = 9
            text text1 yalign 0.0 size s justify True


# show_img, show_event and show_sex_event do basically the same thing and should be merged at some point

screen show_img(img): # event_pic can be an object or a string

    tag show_screen

    if img:
        if isinstance(img, ProportionalScale):
            on "show" action Function(unlock_pic, img.imgname) # This is how the game tracks that this particular picture has been seen.
        else:
            on "show" action Function(unlock_pic, img) # This is how the game tracks that this particular picture has been seen.

        add img

screen show_event(event_pic, x = None, y = None, proportional = True, bg = c_ui_darkblue, ys = 0.8): # event_pic MUST be an object

    tag show_screen

    if event_pic:
        on "show" action Function(unlock_pic, event_pic.path) # This is how the game tracks that this particular picture has been seen.


    zorder 0

    frame:
        background bg
        xalign 0.0
        yalign 0.0
        xsize x
        ysize y
        xmargin 0
        ymargin 0
        xpadding 0
        ypadding 0
        xfill True
        yfill True

        if event_pic:
            add event_pic.get(x, y, proportional) xalign 0.5 yalign 0.0

            if debug_mode:
                frame background c_ui_dark:
                    has vbox
                    text "Attempt: " + str(game.last_pic["attempts"]) size 14
                    text "搜索标签: " + and_text(game.last_pic["tags"]) size 14
                    text "AND tags: " + and_text(game.last_pic["and_tags"]) size 14
                    text "AND NOT tags: " + and_text(game.last_pic["not_tags"]) size 14


screen show_sex_event(event_pic, bg = c_ui_dark): # event_pic MUST be an object

    tag show_screen

    if event_pic:
        on "show" action Function(unlock_pic, event_pic.path) # This is how the game tracks that this particular picture has been seen.


    zorder 0

    default show_log = False


    frame:
        background bg
        xalign 0.0
        yalign 0.0
        xsize 1.0
        ysize 0.8
        left_margin 6
        ymargin 6
        xfill True
        yfill True

        if event_pic:
            add event_pic.get(800, 590) xalign 0.5

            if debug_mode:
                frame background c_ui_dark:
                    has vbox
                    text "Attempt: " + str(game.last_pic["attempts"]) size 14
                    text "搜索标签: " + and_text(game.last_pic["tags"]) size 14
                    text "AND tags: " + and_text(game.last_pic["and_tags"]) size 14
                    text "AND NOT tags: " + and_text(game.last_pic["not_tags"]) size 14

screen night(event_pic = None, event_bg = None, changes = "", has_log = True): # event_pic can be an object or a string

    tag show_screen

    default show_ui = True

    if show_ui:
        key "mouseup_2" action (ToggleScreenVariable("show_ui"), Hide("say")) #, ToggleScreen("say")), renpy.curried_call_in_new_context("_hide_windows"), HideInterface(), renpy.curried_invoke_in_new_context(ui.interact, suppress_overlay=False, suppress_window=True) all don't work
    else:
        key "mouseup_2" action (ToggleScreenVariable("show_ui"), Function(renpy.get_reshow_say))


    if event_pic:
        if isinstance(event_pic, basestring):
            on "show" action Function(unlock_pic, event_pic) # This is how the game tracks that this particular picture has been seen.
        else:
            on "show" action Function(unlock_pic, event_pic.path) # This is how the game tracks that this particular picture has been seen.


    default show_log = False

    hbox:

        spacing 6

        frame:
            xalign 0.0
            yalign 0.0

            if show_ui:
                xsize int(0.8*config.screen_width)
                ysize 615
            else:
                background None
            left_margin 6
            ymargin 2
            xfill True
            yfill True

            if show_log:
                use night_log(log)

            else:
                if show_ui:
                    $ x = 800
                    $ y = 600
                else:
                    $ x = config.screen_width
                    $ y = config.screen_height

                if event_bg: # Adds a bg behind the main pic
                    fixed:
                        add event_bg.get(x, y) xalign 0.5 # TO DO: Replace 800, 600 with values relative to screen resolution
                        if isinstance(event_pic, basestring):
                            add event_pic xalign 0.5
                        else:
                            add event_pic.get(x, y) xalign 0.5

                elif event_pic:
                    add event_pic.get(x, y) xalign 0.5 yalign 0.5

                    if debug_mode and show_ui:
                        frame background c_ui_dark:
                            has vbox
                            text "Attempt: " + str(game.last_pic["attempts"]) size 14
                            text "搜索标签: " + and_text(game.last_pic["tags"]) size 14
                            text "AND tags: " + and_text(game.last_pic["and_tags"]) size 14
                            text "AND NOT tags: " + and_text(game.last_pic["not_tags"]) size 14

        if show_ui:
            frame:

                background c_ui_dark

                xalign 1.0
                yalign 0.0

                ysize 0.8

                right_margin 6
                ymargin 6

                xfill True
                yfill True

                has vbox

                spacing 10

                xfill True

                if has_log:

                    if show_log:
                        $ text1 = "隐藏日志"

                    else:
                        $ text1 = "显示日志"

                    textbutton text1:
                        xalign 0.5
                        xsize 120
                        text_size 18
                        action ToggleScreenVariable("show_log")

                    text ""

                text "绩效"

                text changes size 18

screen night_log(log):

    viewport:
        ysize int(0.85*config.screen_height)
        mousewheel True
        draggable True
        scrollbars "vertical"
        text log.report size 18 color c_brown

## Shortcuts

screen shortcuts():

    # Note: some keys like 'f', 'h', 'm', 's', 'v' are used natively by Ren'py and have been remapped to Shift+* when necessary (see 'BKinit_variables')

    key "h" action (SetVariable("selected_destination", "main"), Jump("teleport"))
    key "c" action (SetVariable("selected_destination", "main_character"), Jump("teleport"))
    key "g" action (SetVariable("selected_destination", "girls"), Jump("teleport"))
    key "b" action (SetVariable("selected_destination", "brothel"), Jump("teleport"))
    key "v" action (SetVariable("selected_destination", "districts"), Jump("teleport"))
    key "s" action (SetVariable("selected_destination", "shop"), Jump("teleport"))
    key "m" action (SetVariable("selected_destination", "slavemarket"), Jump("teleport"))
    key "p" action (SetVariable("selected_destination", "postings"), Jump("teleport"))
    key "e" action (SetVariable("selected_destination", "end_day"), Jump("teleport"))
    key "k" action (SetVariable("show_spellbook", True), SetVariable("selected_destination", "main_character"), Jump("teleport"))
    key "K_F5" action QuickSave() #Set the F5 key in your keyboard to Quicksave when pressed
    key "K_F9" action QuickLoad(confirm=False)  #Same for F9 key

    if story_flags["found wagon"] and story_flags["met carpenter"]:
        key "w" action (SetVariable("selected_destination", "furniture"), Jump("teleport"))
    if farm.active:
        key "f" action (SetVariable("selected_destination", "farm"), Jump("teleport"))
    if selected_location:
        key "l" action (SetVariable("selected_destination", "visit_location"), Jump("teleport"))

## Close button

screen close(act, name = "back"):

    textbutton button_name_dict[name]:

        background None

        xalign 1.0
        yalign 0.075
        xfill False
        yfill False
#        ysize 24
        xmargin 3
#        xpadding 3

        text_size 14
        text_align 1.0
        text_color c_lightred
        text_hover_color c_red
        action act




## ITEMS

screen receive_item(it, msg):

    tag receive_item

    zorder 11

    button:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20

        has vbox
        xalign 0.5
        yalign 0.5
        spacing 20

        add it.get_pic(100, 100) xalign 0.5

        text msg color c_emerald size 16 xalign 0.5 yalign 0.5


screen restock_button(merc, upgrade=False):

    hbox spacing 20 xalign 0.5 yalign 0.08 yanchor 0.0:

        if merc in city_merchants:
            $ restock_cost = shop_restock_cost["city merchants"][game.chapter]
        elif merc in minion_merchants:
            $ restock_cost = shop_restock_cost["minion merchants"][game.chapter]
        else:
            $ restock_cost = shop_restock_cost["shop"][game.chapter]

        textbutton "重置库存" text_size 18 tooltip "以%s金币的价格为这家商店补充存货 (每天一次)." % restock_cost:
            if merc.last_restock != calendar.time and MC.has_gold(restock_cost):
                action Return((True, "restock"))
            else:
                action Return((False, "restock"))

        if upgrade == True and merc.can_upgrade():
            $ chapter, cost, upgrade = shop_upgrades[merc.upgrade_level + 1]

            $ ttip = "升级这个商店的库存（+%s的%s项目）为%s %s." % (str(upgrade[1]), upgrade[0], str(cost[1]), cost[0])

            textbutton "升级商店" text_size 18 tooltip ttip:
                if MC.has_resource(*cost):
                    action Return((True, "upgrade_shop"))
                else:
                    action Return((False, "upgrade_shop"))


screen item_tab(left, right, context):

    default left_length = max_item_shown
    default right_length = max_item_shown

    if context == "shop":
        use overlay("shop") #, (left, right, context))
        if story_flags["shop restock"]:
            use restock_button(right, upgrade=True)

    elif context == "girls":
        $ right = selected_girl
        use overlay("girls", (left, right, context))
        use girl_select(MC.girls)
        use inventory(selected_girl, "take")
        use girl_stats_light(selected_girl)

    elif context == "MC":
        use overlay("MC", (left, right, context))
        use inventory(MC, "use")

    elif context in ("minion_merchant", "city_merchant"):
        use overlay("visit_location", (left, right, context))
        if story_flags["shop restock"]:
            use restock_button(right)

    elif context == "farm":
        $ right = selected_girl
        use overlay("farm", (left, right, context))
        use girl_select(farm.girls, no_sched = True)
        use inventory(selected_girl, "take")
        use girl_stats_light(selected_girl)

    key "mouseup_3" action (Return([0, "back"]))
    use close(Return([0, "back"]))

#    key "mouseup_3" action (Hide("item_tab"), Hide("item_profile"), Hide("main_character"), Hide("show_event"), Hide("button_overlay"), Hide("tool"), Hide("inventory"), Return([0, "back"]))
#    use close((Hide("item_tab"), Hide("item_profile"), Hide("main_character"), Hide("show_event"), Hide("button_overlay"), Hide("tool"), Hide("inventory"), Return([0, "back"])))
    use shortcuts()

    if left != None:

        if left == MC:
            $ sort_context = "MC items"
        else:
            $ sort_context = context + " items"

        vbox:
            xalign 0
            ypos 0.075
            use sorting_tab(sort_context, sort_target=left.items, sorters=["type", "price", "alpha"])

            hbox xfill False yfill False spacing 6:

                frame:

                    id "item_tab1"

                    if context in ("shop", "city_merchant"):
                        $ act = "sell"

                    elif context in ("girls", "farm"):
                        $ act = "give"

                    else:
                        $ act = None

    #                $ left.items.sort(key=operator.methodcaller('get_key'))

                    if not MC.active_inv_filter:
                        $ it_list1 = left.items
                    else:
                        $ it_list1 = [it for it in left.items if it.filter == MC.active_inv_filter]

                    if len(it_list1) > left_length:
                        $ it_list1 = it_list1[:left_length] + ["more_button"]

                    xmargin 3
                    xpadding 6
                    xfill True
                    xsize 200
                    ysize 520

                    viewport:
                        xalign 0.0
                        xfill True
                        mousewheel True
                        draggable True
                        scrollbars "vertical"

                        vbox:
                            spacing 2

                            if left == MC:
                                text "你" color c_brown
                            else:
                                text selected_girl.name color c_darkred

                            if it_list1 == []:

                                hbox xsize 180 xfill True:

                                    if MC.active_inv_filter:
                                        text "没有可供选择的物品 (筛选开启)." size 14

                                    else:
                                        text "没有可供选择的物品." size 14

                            for it in it_list1:
                                if it == "more_button":
                                    textbutton "显示更多物品" xsize 170 text_size 14 text_italic True action SetScreenVariable("left_length", left_length + max_item_shown)

                                else:
                                    $ ttip = it.description

                                    button:
                                        xsize 170
                                        yminimum 68
                                        action (Show("item_profile", it = it, act = act, transition = dissolve), SetVariable("selected_item", it))
                                        tooltip ttip

                                        hbox spacing 3:
                                            frame yalign 0.5 xsize 60 ysize 60 ymargin 3:

                                                $ p = it.pic

                                                add p.get(x = 50, y = 50) xalign 0.5 yalign 0.5


                                            vbox yalign 0.5:
                                                $ text1 = it.name

                                                if it.charges > 1 and it.usage != "buff":
                                                    $ text1 += " (" + str(it.charges) + ")"

                                                if it.equipped:
                                                    $ text1 += "\n{i}已装备{/i}"


                                                if act == "sell":
                                                    if it.type.sellable:
                                                        $ text1 += "\n" + str(it.get_price("sell")) + "金币"

                                                text text1 size 14



                use inventory_filter() id "if1"

    if right != None:

        if right == MC:
            $ sort_context = "MC items"
        else:
            $ sort_context = context + " items"

        vbox:
            xalign 1.0
            ypos 0.075
            use sorting_tab(sort_context, sort_target=right.items, sorters=["type", "price", "alpha"])
            hbox xfill False yfill False spacing 6:

                if context == "city_merchant": # Uses the first item type name in the list as key. A bit dirty, but does the job.
                    use inventory_filter(inventory_filters[merc.item_types[0]]) id "if2"
                elif context == "minion_merchant":
                    use inventory_filter(inventory_filters["minion_merchant"]) id "if2"
                else:
                    use inventory_filter() id "if2"

    #            if context not in ("shop", "minion_merchant"):
    #                $ right.items.sort(key=operator.methodcaller('get_key'))

                frame:

                    id "item_tab2"

                    if context in ("shop", "city_merchant", "minion_merchant"):
                        $ act = "buy"

                    elif context in ("girls", "farm"):
                        $ act = "take"

                    elif context == "MC":
                        $ act = "use"

                    if not MC.active_inv_filter:
                        $ it_list2 = right.items
                    else:
                        $ it_list2 = [it for it in right.items if it.filter == MC.active_inv_filter]

                    if len(it_list2) > right_length:
                        $ it_list2 = it_list2[:right_length] + ["more_button"]

                    xmargin 3
                    xpadding 6
                    xfill True
                    xsize 200
                    ysize 520

                    viewport:
                        xalign 0.0
                        xfill True
                        mousewheel True
                        draggable True
                        scrollbars "vertical"

                        vbox:
                            spacing 2

                            if context in ("shop", "city_merchant", "minion_merchant"):
                                text "商家" color c_brown

                            elif right == MC:
                                text "你的物品" color c_brown

                            else:
                                text right.name color c_darkred


                            if it_list2 == []:
                                hbox xsize 180 xfill True:
                                    if MC.active_inv_filter:
                                        text "没有可供选择的物品 (筛选开启)." size 14 color c_brown
                                    else:
                                        text "没有可供选择的物品." size 14 color c_brown

                            for it in it_list2:
                                if it == "more_button":
                                    textbutton "显示更多物品" xsize 170 text_size 14 text_italic True action SetScreenVariable("right_length", right_length + max_item_shown)

                                elif not it.equipped:

                                    $ ttip = it.description

                                    button:
                                        xsize 170
                                        yminimum 68

                                        action (Show("item_profile", it = it, act = act, transition = dissolve), SetVariable("selected_item", it))
                                        tooltip ttip

                                        hbox spacing 3:

                                            frame yalign 0.5 xsize 60 ysize 60 ymargin 3:

                                                add it.pic.get(x = 50, y = 50) xalign 0.5 yalign 0.5


                                            vbox yalign 0.5:
                                                $ text1 = it.name

                                                if isinstance(it, Item):
                                                    if it.charges > 1:
                                                        $ text1 += " (" + str(it.charges) + ")"

                                                    if it.equipped:
                                                        $ text1 += "\n{i}已装备{/i}"

                                                elif isinstance(it, Minion):
                                                    $ text1 +=  "\n等级" + str(it.level)

                                                if act == "buy":

                                                    $ text1 += "\n" + str(it.get_price("buy")) + "金币"

                                                text text1 size 14




screen item_profile(it, act):

    on "hide" action SetVariable("selected_item", None)

    frame:

        id "item_profile"

        background c_ui_dark

        xalign 0.5
        yalign 0.5
        xpadding 6
        ypadding 6
        xsize 300
        xfill True
        yfill False

        has vbox

        if act != "bargain":
            use close(Hide("item_profile"), name = "hide")
            key "mouseup_3" action Hide("item_profile")


        frame xalign 0.5 xfill True:

            add it.pic.get(100, 100) xalign 0.5

        frame xalign 0.5 xfill True:

            background None

            has vbox xfill True xalign 0.5

            $ text1 = it.name

            if isinstance(it, Item):
                if it.charges > 1 and it.usage == "use":
                    $ text1 += " (" + str(it.charges) + ")"

            text text1 xalign 0.5

            if it.target == "MC":
                $ col = c_steel
            elif it.target == "girl":
                $ col = c_pink
            elif it.target == "minion":
                $ col = c_purple
            else:
                $ col = c_orange

            text "" size 8

            if isinstance(type, ItemType):
                text "{color=[col]}" + setting_name_dict[it.type.name] + "{/color}" xalign 0.5 size 18
            else:
                text "{color=[col]}" + setting_name_dict[it.target.capitalize()] + "{/color}" xalign 0.5 size 18

            text ""

            text it.description size 14 xalign 0.5

            text ""

            if act == "buy":

                text str(it.get_price("buy")) + "金币" xalign 0.5

                text ""

                textbutton "买" action Return((it, "buy")) xalign 0.5

            if act == "bargain":

                text str(it.get_price("bargain")) + " gold" xalign 0.5

                text ""

                hbox spacing 10 xalign 0.5:
                    textbutton "买" action Return("buy") xalign 0.5
                    textbutton "跳过" action Return("leave") xalign 0.5

            if act == "sell":

                if it.type.sellable:
                    text str(it.get_price("sell")) + "金币" xalign 0.5
                else:
                    text "Unsellable" italic True xalign 0.5

                text ""

                hbox spacing 10 xalign 0.5:

                    textbutton "出售" xalign 0.5:
                        if it.type.sellable:
                            action Return((it, "sell"))

                    if it.can_wear("MC"):

                        if not it.equipped:

                            textbutton "装备" action Return((it, "equip")) xalign 0.5

                        else:

                            textbutton "卸下" action Return((it, "unequip")) xalign 0.5


            if act == "take":

                hbox spacing 10 xalign 0.5:

                    textbutton "取回" action Return((it, "take")) xalign 0.5

                    if it.can_wear("girl"):
                        if not it.equipped:
                            textbutton "装备" action Return((it, "g_equip")) xalign 0.5

                        else:
                            textbutton "卸下" action Return((it, "g_unequip")) xalign 0.5

                    if it.can_use("girl"):
                        textbutton "使用" action Return((it, "g_use")) xalign 0.5



            if act == "give":

                hbox spacing 10 xalign 0.5:

                    if it.usage == "give":
                        textbutton "礼物" action Return((it, "gift")) xalign 0.5

                    else:
                        textbutton "给与" action Return((it, "give")) xalign 0.5

                    if it.can_wear("MC"):

                        if not it.equipped:
                            textbutton "装备" action Return((it, "equip")) xalign 0.5
                        else:
                            textbutton "卸下" action Return((it, "unequip")) xalign 0.5

                    elif it.can_wear("girl"):
                        textbutton "让她装备" action Return((it, "give_equip")) xalign 0.5

                    if it.can_use("girl"):
                        textbutton "让她使用" action Return((it, "give_use")) xalign 0.5

            if act == "use":

                hbox spacing 10 xalign 0.5:

                    if it.can_wear("MC"):

                        if not it.equipped:

                            textbutton "装备" action Return((it, "equip")) xalign 0.5

                        else:

                            textbutton "卸下" action Return((it, "unequip")) xalign 0.5

                    elif it.can_use("MC"):

                        textbutton "使用" action Return((it, "use")) xalign 0.5


screen inventory(char, act):

    frame:
        background c_ui_dark

        xalign 0.5
        ypos 0.4
        xmaximum 1.0
        yfill False

        has hbox spacing 10 box_wrap True

        if char:
            for slot in char.slots:
                $ eq = None
                for it in char.equipped:
                    if it.slot == slot:
                        $ eq = it

                vbox:
                    text setting_name_dict[slot.capitalize()] size 14 xalign 0.5

                    button xsize 60 ysize 60 xfill True yfill True xalign 0.5:

    #                    default click_time = 0

                        if eq:
                            add eq.pic.get(45, 45) xalign 0.5 yalign 0.5

                            action (Show("item_profile", it = eq, act = act, transition = dissolve), SetVariable("selected_item", eq)) # Function("double_click_check", old_click_time = click_time, value = (eq, "unequip")), SetScreenVariable("click_time", time.time())

                            hovered tt.Action(eq.description)

                        else:
                            text "空" size 12 italic True xalign 0.5 yalign 0.5
                            action NullAction()
                            hovered tt.Action("此插槽没有装备任何物品.")



screen inventory_filter(filters=inventory_filters["base"]):

    if MC.active_inv_filter not in filters:
        $ active_inv_filter = None

    vbox xfill False yfill False spacing 3:
        for filter in filters:
            frame xsize 38 ysize 38 xpadding 0 xmargin 0:
                button xalign 0.5 yalign 0.6 xsize 30 ysize 30 xpadding 0 xmargin 0 idle_background None:

                    action (SetField(MC, "active_inv_filter", filter), Function(renpy.restart_interaction), SetScreenVariable("left_length", max_item_shown), SetScreenVariable("right_length", max_item_shown))

                    if filter:
                        if filter == MC.active_inv_filter:
                            add "filter_" + filter
                        else:
                            add "filter_" + filter + "_unselect"
                        hovered tt.Action("显示" + setting_name_dict[filter] + "物品.")
                    else:
                        if filter == MC.active_inv_filter:
                            add "filter_all"
                        else:
                            add "filter_all_unselect"
                        hovered tt.Action("显示所有物品.")

screen sorting_tab(context, sort_target=None, sorters=[]): # Sorters are defined in BKinit_variables.rpy
    hbox xalign 0.5:
        for s in sorters:
            $ sorter = sorter_dict[s]
            frame xsize 38 ysize 20 xpadding 0 ypadding 0 xmargin 0 ymargin 0:

                textbutton sorter[0] text_italic True text_color c_darkbrown text_size 14 xpadding 0 ypadding 0 xalign 0.5 yalign 0.6 xsize 38 ysize 20 idle_background None:
                    if not game.sorting_dict[context] or game.sorting_dict[context].endswith("reverse"):
                        action (Function(sort_target.sort, key=operator.attrgetter(sorter[1])), SetDict(game.sorting_dict, context, sorter[1]))
                    else:
                        action (Function(sort_target.sort, key=operator.attrgetter(sorter[1]), reverse=True), SetDict(game.sorting_dict, context, sorter[1] + " reverse"))
                    tooltip "点击左键按" + sorter[2] +"排序."



## GIRL BROWSER

screen girl_select(girl_list, orange = False, no_sched=False):

    frame:

        id "girl_select"

        background None

        xalign 0.5
        yalign 0.2
        xpadding 6
        ypadding 6
        xsize 400
        ysize 100
        xfill True
        yfill False

        if girl_list:
            key "K_LEFT" action (Function(select_previous_girl, girl_list), Hide("item_profile"))
            key "K_RIGHT" action (Function(select_next_girl, girl_list), Hide("item_profile"))

        hbox spacing 5:

            textbutton "<" ysize 120 yalign 0.5:
                if girl_list:
                    action (Function(select_previous_girl, girl_list), Hide("item_profile"), SetVariable("selected_item", None))

            frame:
                xsize 300
                ysize 120
                xfill True
                xalign 0.5
                ymargin 3

                if orange:
                    background c_orange + "AA"

                if girl_list and selected_girl:
                    frame background None xsize 280 ysize 120 xfill True yfill True ypadding 0 ymargin 0:

                        has hbox
                        spacing 6

                        frame xsize 100 ysize 100 xfill True ypadding 0 ymargin 0:
                            if selected_girl.portrait != None:
                                fixed fit_first True xalign 0.5 yalign 0.5:
                                    add selected_girl.portrait.get(x = 90, y = 90) xalign 0.5 yalign 0.5

                                    $ badge = selected_girl.get_badge()
                                    if badge:
                                        add ProportionalScale(badge, 40, 40) xalign 0.9 yalign 0.1

                        $ text1 = selected_girl.fullname + "\n阶级 " + rank_name[selected_girl.rank] + " - 等级 " + str(selected_girl.level)

                        if not no_sched:
                            if selected_girl.job:
                                $ text1 += "\n" + girl_related_dict[selected_girl.job.capitalize()]
                                if selected_girl.job in all_jobs and selected_girl.work_whore:
                                    $ text1 += "/妓女"
                                $ sched = selected_girl.workdays[calendar.get_weekday()]

                            else:
                                $ text1 += "\n没有工作"
                                $ sched = 0


                            if selected_girl.away:
                                $ text1 += " (离开)"
                            elif selected_girl.hurt > 0:
                                $ text1 += " (受伤)"
                            elif selected_girl.exhausted > 0:
                                $ text1 += " (疲劳)"
                            elif selected_girl.resting or sched == 0:
                                $ text1 += " (休息)"
                            elif sched == 50:
                                $ text1 += " (半班制)"

                        text text1 size 14 xalign 0.0 yalign 0.5 color c_brown

                else:
                    text "{i}没有女孩能胜任这项任务{/i}" size 14 xalign 0.5 yalign 0.5

            textbutton ">" ysize 120 yalign 0.5:
                if girl_list:
                    action (Function(select_next_girl, girl_list), Hide("item_profile"), SetVariable("selected_item", None))


## START SCREEN

screen quick_start():

    modal True

    default panel = "MC"

    vbox xalign 0.5 yalign 0.5 xsize int(0.95*config.screen_width):
        hbox xfill True:
            textbutton "角色创建" xsize 160 ysize 48 text_size 24 text_selected_bold True action SelectedIf(panel == "MC") hovered SetScreenVariable("panel", "MC") tooltip "创建你的主要角色."

            textbutton "难度选择" xsize 160 ysize 48 text_size 24 text_selected_bold True action SelectedIf(panel == "diff") hovered SetScreenVariable("panel", "diff") tooltip "改变难度设置."

            textbutton "女孩选择" xsize 160 ysize 48 text_size 24 text_selected_bold True action SelectedIf(panel == "mix") hovered SetScreenVariable("panel", "mix") tooltip "选择你的女孩组合."

            if persistent.new_game_plus or debug:
                textbutton "额外设置" xsize 160 ysize 48 text_size 24 text_selected_bold True action SelectedIf(panel == "extras") hovered SetScreenVariable("panel", "extras") tooltip "进入NewGame+设置."

            button background None xsize 320 ysize 52 xalign 1.0:
                if GetTooltip():
                    $ ttip = GetTooltip()
                else:
                    $ ttip = ""
                text ttip size 13 color c_white justify True

        frame xpadding 20 ypadding 20 xfill True ysize int(0.8*config.screen_height):
            has vbox xfill True spacing 20
            if panel == "MC":

                hbox spacing 30 xalign 0.5:
                    label "名字: "
                    input value FieldInputValue(MC, "name") length 20 color c_steel bold True
#                     text "Name: " color c_brown yalign 0.5
#                     textbutton "[MC.name]" ysize 40 text_color c_white text_bold True action Call("MC_change_name")

                hbox spacing 30 xalign 0.5:
                    frame: # background c_orange:
                        has vbox

                        text "职业" xalign 0.5 size 18 bold True color c_prune

                        hbox spacing 10:
                            for cl in ["Warrior", "Wizard", "Trader"]:
                                button yalign 0.5 xpadding 0 action Function(MC.set_playerclass, cl) tooltip MC_playerclass_description[cl]:
                                    if MC.playerclass != cl:
                                        background None

                                    add Picture(path=playerclass_pics[cl]).get(40, 40) yalign 0.5:
                                        if MC.playerclass == cl:
                                            alpha 1.0
                                        else:
                                            alpha 0.3
                                            # hover_alpha 1.0

                    frame: # background c_purple:
                        has vbox

                        text "信仰" xalign 0.5 size 18 bold True color c_emerald

                        hbox spacing 10:
                            for god in ["Arios", "Shalia", None]:
                                button yalign 0.5 xpadding 0 action Function(MC.set_god, god) tooltip god_description[god]:
                                    if MC.god != god:
                                        background None

                                    add Picture(path=god_pics[god]).get(40, 40) yalign 0.5:
                                        if MC.god == god:
                                            alpha 1.0
                                        else:
                                            alpha 0.3
                                            # hover_alpha 1.0

                    frame xalign 0.5 yalign 0.5 ysize 76:
                        grid 4 1 yalign 0.5:
                            for stat in all_MC_stats:
                                button background None action NullAction() tooltip MC_stat_description[stat]:
                                    vbox xsize 100:
                                        text MC_stat_color[stat] % start_name_dict[stat.capitalize()] size 18 xalign 1.0 bold True
                                        text MC_stat_color[stat] % int(MC.get_stat(stat, raw=True)) size 24 xanchor 1.0 xalign 1.0

                # hbox spacing 20 xalign 0.5:


                hbox xalign 0.5 spacing 30:
                    textbutton "<" ysize 120 yalign 0.5:

                        action Function(MC.change_pic, "previous")
                        tooltip "更改你的主角图片."


                    frame:
                        xalign 0.5
                        yalign 0.3
                        xfill False
                        yfill False
                        add MC.current_pic.get(int(config.screen_width*0.5), int(config.screen_height*0.5))

                    textbutton ">" ysize 120 yalign 0.5:

                        action Function(MC.change_pic, "next")
                        tooltip "更改你的主角图片."

            elif panel == "diff":
                hbox spacing 60:
                    frame ysize 240:
                        has vbox spacing 10 xalign 0.5 yalign 0.5
                        style_group "diff"
                        for diff in diff_list:
                            textbutton diff_name[diff] xsize 220 ysize 36 action (Function(game.set_difficulty, diff), SelectedIf(game.diff == diff)) tooltip diff_description[diff] text_selected_bold True

                    vbox spacing 6 box_wrap True:

                        $ y = len(diff_settings)

                        grid 2 y:
                            for ds in diff_settings:
                                if ds == "satisfaction":
                                    textbutton diff_setting_name[ds] + ": " + plus_text(game.get_diff_setting(ds)) text_color c_brown background None text_size 18 action NullAction() tooltip diff_setting_description[ds]
                                else: # percentage description
                                    textbutton diff_setting_name[ds] + ": " + percentage_description(game.get_diff_setting(ds), False) text_color c_brown background None text_size 18 action NullAction() tooltip diff_setting_description[ds]

                                hbox:
                                    textbutton "-" text_size 18 action Function(game.change_diff_setting, ds, -diff_settings_range[ds]["pace"]) # Trying to go around the prediction problem
                                    textbutton "+" text_size 18 action Function(game.change_diff_setting, ds, diff_settings_range[ds]["pace"])

            elif panel == "mix":
                $ available_mixes = update_available_mixes()

                vbox spacing 20 xalign 0.05:
                    textbutton "活跃的女孩组合: %s" % and_text(persistent.game_mixes) xpadding 0 xmargin 0 background None text_color c_darkorange action NullAction() tooltip "{b}警告{/b}: 在开始游戏后，你选择的活动女孩组合不能改变，尽管你仍然可以在组合中添加或删除女孩包."

                    text "点击一个女孩的组合，在这个游戏中添加或删除它." size 14 italic True color c_brown

                    hbox spacing 30 xfill True xalign 0.05:
                        frame ysize 0.8:
                            has vbox spacing 12 yfill True xalign 0.5
                            vpgrid cols 1 xalign 0.5 draggable True mousewheel True scrollbars "vertical":

                                style_group "mix"

                                for mix in available_mixes:
                                    textbutton mix.capitalize() text_size 18:
                                        if mix in persistent.game_mixes:
                                            background c_orange
                                            text_color c_white
                                            action RemoveFromSet(persistent.game_mixes, mix)
                                            tooltip "单击以删除组合: 禁用{b}%s{/b}在本次游戏的组合." % mix.capitalize()
                                        else:
                                            background c_ui_insensitive
                                            text_color c_darkgrey
                                            action AddToSet(persistent.game_mixes, mix)
                                            tooltip "单击以添加组合: 激活{b}%s{/b}在本次游戏的组合." % mix.capitalize()

                            textbutton "编辑女孩组合" xsize 220 ysize 36 xalign 0.5 yalign 1.0 action Return("edit mix") tooltip "点击这里编辑你的女孩组合."

                        $ selected_girlpacks = get_selected_girlpacks(persistent.game_mixes)

                        vpgrid cols 10 draggable True mousewheel True scrollbars "vertical" xalign 1.0:
                            for gp in selected_girlpacks:
                                button background None xalign 0.5 yalign 0.5 xmargin 0 ymargin 0 action NullAction() tooltip get_name(gp, full=True) + "{i} by %s{/i}" % creator_dict[gp]:
                                    add fast_portrait(gp, x = 30, y = 30)


            elif panel == "extras":

                $ unlocking_extras()

                vbox spacing 20:
                    text "注意事项: 选择这些选项中的任何一个都将禁用本游戏的成就." size 14 italic True color c_brown

                    hbox:
                        label "初始金币: "
                        input value FieldInputValue(game, "starting_gold") length 9 allow "0123456789" color c_darkgold bold True

                    hbox spacing 10:
                        text "起始章节: 章节 %s" % starting_chapter color c_brown

                        hbox:
                            textbutton "-":
                                if starting_chapter > 1:
                                    action (SetVariable("starting_chapter", starting_chapter-1),)
                            textbutton "+":
                                if starting_chapter < 7:
                                    action (SetVariable("starting_chapter", starting_chapter+1),)

                    if starting_chapter > 1:
                        $ next_path = get_next(["good", "neutral", "evil"], c1_path, loop=True)

                        textbutton "第一章结束: %s" % c1_path.capitalize() action SetVariable("c1_path", next_path)

                    vbox:
                        style_group "extras"
                        textbutton "农场: %s" % {True: "解锁", False: "锁定"}[extras_dict["farm"]] action (ToggleDict(extras_dict, "farm"))

                        textbutton "木匠: %s" % {True: "解锁", False: "锁定"}[extras_dict["carpenter"]] action (ToggleDict(extras_dict, "carpenter"))

                        textbutton "场所: %s" % {True: "解锁", False: "锁定"}[extras_dict["locations"]] action (ToggleDict(extras_dict, "locations"))

                        textbutton "商店: %s" % {True: "解锁", False: "锁定"}[extras_dict["shops"] > 0]:
                            if extras_dict["shops"]:
                                action (SetDict(extras_dict, "shops", False))
                            else:
                                action (SetDict(extras_dict, "shops", 7))

                        textbutton "资源: %s" % {True: "解锁", False: "锁定"}[extras_dict["resources"] > 0]:
                            if extras_dict["resources"]:
                                action (SetDict(extras_dict, "resources", False))
                            else:
                                action (SetDict(extras_dict, "resources", 7))

                        textbutton "培训师: %s" % {True: "解锁", False: "锁定"}[extras_dict["trainers"]] action (ToggleDict(extras_dict, "trainers"))

                        text "" size 12

                        textbutton "重置额外的内容" action (SetVariable("extras_dict", {"farm" : False, "carpenter" : False, "locations" : False, "shops" : False, "trainers" : False, "resources" : False}), SetField(game, "starting_gold", str(starting_gold)))

        frame xfill True xsize int(0.95*config.screen_width) ysize int(0.1*config.screen_height):
            hbox xfill True:
                vbox spacing 10 xalign 0.5 yalign 0.5:
                    text "{b}%s, %s{/b} ({b}%s{/b}) - {b}难度: %s{/b}" % (MC.name, start_name_dict[MC.playerclass], start_name_dict[str(MC.god)], start_name_dict[game.diff.capitalize()]) color c_prune size 18
                    if game.achievements:
                        text "本次游戏将启用成就." italic True color c_emerald size 18
                    else:
                        text "本次游戏将禁用成就." italic True color c_red size 18

                textbutton "确认" xalign 1.0 yfill True action Return(True) tooltip "用这些设置开始一个新的游戏."

## MAIN CHARACTER SCREEN

screen main_character():

    use shortcuts()
    use overlay("MC")

    frame background None:

        xalign 0.0
        ypos 0.1
        xsize 200
        ysize 520
        xfill True
        yfill True

        has vbox

        spacing 3

        frame xpadding 3 ypadding 10 xfill True:
            has vbox
            textbutton MC.name background None text_color c_steel action Return("change_name") hovered tt.Action("点击这里更改你的角色名称")
            textbutton ("等级" + str(MC.level) + " " + start_name_dict[MC.playerclass]) background None text_size 18 text_color c_darkgrey action NullAction() tooltip "你需要" + str(int(MC_xp_to_levelup[MC.level])) + "点威望值来提升等级."

        frame xpadding 3 ypadding 10 xfill True:
            has vbox spacing 6

            for stat in all_MC_stats:

                if MC.get_effect("change", stat) > 0:
                    $ col2 = c_emerald
                elif MC.get_effect("change", stat) < 0:
                    $ col2 = c_red
                else:
                    $ col2 = c_darkgrey

                button:

                    background None
                    xsize 180
                    ysize 30

                    action NullAction()
                    hovered tt.Action(MC_stat_description[stat])

                    text MC_stat_color[stat] % start_name_dict[stat.capitalize()] size 18

                    text "{color=[col2]}" + str(int(MC.get_stat(stat))) + "{/color}" size 18 xanchor 1.0 xalign 0.8

                    if MC.skill_points > 0 and MC.get_stat(stat, raw=True) < 10:
                        textbutton "+" text_size 14 xpos 0.82 xfill False action Return("raise_" + stat)

            text "" size 8

            vbox spacing 3:
                button:
                    background None
                    action NullAction()
                    hovered tt.Action(text1)

                    $ text1 = "每当你或你的女孩发生性关系时，或当你的一个女孩获得一个新的级别时，你都会获得威望."

                    if MC.level == 25:
                        $ text1 += "\n你已经达到了最高等级."
                    else:
                        $ text1 += "\n你需要" + str(int(MC_xp_to_levelup[MC.level])) + "点威望值来提升等级."

                    text (str(int(MC.prestige)) + " 威望点") size 14 color c_brown

                button:
                    background None
                    action NullAction()
                    hovered tt.Action("每升级你会得到1个技能点.")

                    text str(MC.skill_points) + " 技能点" size 14 color c_brown

        frame xpadding 3 ypadding 10 xfill True:
            has vbox
            hbox xalign 0.5:

                spacing 16

                button yalign 0.5 xpadding 0 action NullAction() tooltip MC_playerclass_description[MC.playerclass]:
                    add Picture(path=playerclass_pics[MC.playerclass]).get(40, 40) yalign 0.5

                button yalign 0.5 xpadding 0 action NullAction() tooltip god_description[MC.god]:
                    add Picture(path=god_pics[MC.god]).get(40, 40) yalign 0.5

                button yalign 0.5 xpadding 0 action NullAction() tooltip alignment_description[MC.get_alignment()]:
                    add Picture(path=alignment_pics[MC.get_alignment()]).get(40, 40) yalign 0.5

            text "" size 10

            textbutton "{b}当前目标{/b}\n{i}{size=-2}" + game.get_first_goal() xalign 0.1 yalign 0.5 xsize 180 text_size 14 text_color c_brown background None:
                action NullAction()
                hovered Show("goal_ttip", transition=Dissolve(0.15))
                unhovered Hide("goal_ttip", transition=Dissolve(0.15))

            text "" size 8

            textbutton "魔法书" xalign 0.5 action (Show("spellbook"), Function(renpy.block_rollback)) tooltip "查看所有可用的法术和有效的天赋"


    textbutton "<" xpos 0.2 ysize 120 yalign 0.5:

        action Return("previous_pic")
        hovered tt.Action("改变你的角色图片.")


    frame:
        xalign 0.5
        yalign 0.3
        xfill False
        yfill False
        add MC.current_pic.get(int(config.screen_width*0.50), int(config.screen_height*0.7))

    textbutton ">" xpos 0.76 ysize 120 yalign 0.5:

        action Return("next_pic")
        hovered tt.Action("改变你的角色图片.")

#     use item_tab(left = None, right = MC, context = "MC")

screen active_spells():

    hbox:
        text "已激活:" size 14 color c_brown yalign 0.5
        for spell in MC.active_spells:
            button xpadding 0 ypadding 0 xsize 40 ysize 40 action NullAction() hovered tt.Action("{b}" + spell.name + "{/b}: " + get_description("", spell.effects)):
                add spell.pic.get(30, 30) xalign 0.5 yalign 0.5


screen spellbook():

    modal True

    key "mouseup_3" action (Hide("spellbook"), SetVariable("show_spellbook", False))

#    use dark_filter

    textbutton MC.name + "的魔法书" yalign 0.1 xalign 0.5

    fixed xalign 0.5 yalign 0.5:
        fit_first True

        add "UI/spellbook.jpg"


        frame xalign 0.95 yalign 0.05:
            use close((Hide("spellbook"), SetVariable("show_spellbook", False)))

        if MC.known_spells:
            frame xalign 0.5 yalign 0.95:
                text "右键点击法术以设置自动施法" size 14 color c_brown



            frame left_padding 100 right_padding 35 ypadding 60 xfill True yfill True background None:
                viewport:
                    xalign 0.0
                    yalign 0.0
                    xfill True
                    yfill True
                    mousewheel True
                    draggable True
                    scrollbars "vertical"

                    fixed ysize 80 * round_up(len(MC.known_spells)/2.0):

                        $ x = 0
                        $ y = 0
                        $ i = 0

                        for s in MC.known_spells:
                            if s.type != "passive":

                                if s in MC.active_spells and s.auto:
                                    $ col = c_darkpurple
                                    $ extra = "(自动施法: " + s.auto.capitalize() + ")\n(已激活)"

                                elif s.auto:
                                    $ col = c_firered
                                    $ extra = "(自动施法: " + s.auto.capitalize() + ")"

                                elif s in MC.active_spells:
                                    $ col = c_steel
                                    $ extra = "(已激活)"

                                else:
                                    $ col = False
                                    $ extra = ""

                                button:
                                    xpos x
                                    ypos y
                                    xsize 220
                                    ysize 80
                                    xfill True
                                    xalign 0.0
                                    xpadding 3
                                    xmargin 0

                                    if col:
                                        background col

                                    action Return((s, "cast"))

                                    alternate Function(MC.toggle_auto_spell, s) #ToggleField(s, "auto")

                                    hovered tt.Action(s.description)

                                    hbox spacing 3 xalign 0.0 yfill True:

                                        frame background None xsize 60 yfill True xmargin 6:
                                            add s.pic.get(x = 50, y = 50) xalign 0.5 yalign 0.5


                                        vbox yalign 0.5:

                                            text s.name size 14 bold True

                                            hbox:
                                                text str(s.get_cost()) size 14

                                                add ProportionalScale("UI/mana.webp", 15, 15)

                                                if s.duration == "turn":

                                                    text "/n晚上" size 14

                                            if extra:
                                                text extra size 14

                                if i%2:
                                    $ x = 0
                                    $ y += 80
                                else:
                                    $ x = 350

                                $ i += 1

        else:
            textbutton "{i}你还不知道任何法术. 你必须提高你的等级.{/i}" xalign 0.5 yalign 0.5 xsize 250 text_size 18

    if MC.active_spells:
        frame xalign 0.5 yalign 0.9 xsize 0.85 xpadding 20:
            use active_spells()




## CLASSES AND QUESTS POSTINGS

screen postings(qlist):

    key "mouseup_3" action ((SetVariable("selected_destination", "main"), Jump("teleport")))
    use shortcuts()
    use close((SetVariable("selected_destination", "main"), Jump("teleport")))
    use overlay("postings")

    if qlist:
        key "K_UP" action SetVariable("selected_quest", get_previous(qlist, selected_quest))
        key "K_DOWN" action SetVariable("selected_quest", get_next(qlist, selected_quest))

    if not selected_quest and qlist:
        $ selected_quest = qlist[0]
    elif not qlist:
        $ selected_quest = None

    hbox:

        ypos 0.1
        yfill False

        use girl_stats(selected_girl, context = "postings")

        vbox:
            xsize int(0.5*config.screen_width)


            frame:
                xsize int(0.5*config.screen_width)
                ysize int(0.7*config.screen_height)

                xpadding 10

                has vbox

                spacing 3

                if selected_quest:

                    hbox:
                        spacing 0
                        xalign 0.0

                        if selected_quest.special:
                            textbutton "{image=img_star} " + selected_quest.special + " {image=img_star}" xalign 0.0 yalign 0.5 ypadding 0 text_color c_orange background None action NullAction() hovered tt.Action(special_quest_description[selected_quest.special])

                        text selected_quest.name xalign 0.0 yalign 0.5 color c_prune

                    hbox:
                        spacing 6

                        frame:
                            xsize 360
                            ysize 470
                            xfill True
                            background None

                            if selected_quest.pic:
                                add selected_quest.pic.get(x = 350, y = 465) xalign 0.0 yalign 0.0

                        vbox:

                            text selected_quest.description size 14 color c_brown

                            text "" size 18

                            text "持续" size 18 color c_prune

                            text str(selected_quest.duration) + "天" size 14 color c_brown

                            text "" size 18

                            if selected_quest.type == "class":

                                text "费用" size 18 color c_prune

                                text str(selected_quest.gold) + "金币" size 14 color c_brown

                                text "" size 18

                                text "报名" size 18 color c_prune

                                text str(len(selected_quest.enrolled)) + "/" + str(selected_quest.capacity) + "位女孩" size 14 color c_brown

                                text "" size 18

                                text "获得" size 18 color c_prune

                                for stat, _min, _max in selected_quest.bonuses:

                                    if _max >= 12:
                                        $ t = "+++"

                                    elif _max >= 6:
                                        $ t = "++"

                                    else:
                                        $ t = "+"

                                    text girl_related_dict[stat] + " " + t size 14 color c_brown

                                textbutton "\n最高技能: " + str(selected_quest.stat_cap) text_size 14 text_color c_brown xalign 0.0 yalign 0.5 xpadding 0 ypadding 0 background None:
                                    tooltip "课程可能导致女孩的技能超过等级上限."


                            elif selected_quest.type == "quest":

                                text "报酬" size 18 color c_prune

                                text str(selected_quest.gold) + "金币" size 14 color c_brown

                                text "" size 18

                                text "要求" size 18 color c_prune

                                for stat, val in selected_quest.requirements:

                                    text stat_name_dict[stat] + " " + str(val) size 14 color c_brown

                                text "" size 18

                                text "令人满意" size 18 color c_prune

                                text trait_name_dict[selected_quest.pos_traits[0].name] + ", " + trait_name_dict[selected_quest.pos_traits[1].name] size 14 color c_emerald

                                text "" size 18

                                text "不受欢迎" size 18 color c_prune

                                text trait_name_dict[selected_quest.neg_trait.name] size 14 color c_crimson

                else:
                    text "目前没有任何任务可用." italic True color c_brown size 18

            fixed xalign 0.5:
                fit_first True

                if selected_quest:

                    $ available_girls = [g for g in MC.girls if selected_quest.test_eligibility(g)[0]]

                    use girl_select(available_girls)

                    if selected_quest and selected_girl:

                        $ r, ttip = selected_quest.test_eligibility(selected_girl)

                        if r: # or debug_mode:
                            $ act = Return("commit")
                        else:
                            $ act = None

                        button xalign 0.9 xanchor 1.0 yalign 0.15 background None:
                            textbutton "提交" xalign 0.68 yalign 0.825 text_size 18 action act tooltip ttip

                            action NullAction()
                            tooltip ttip

        vbox:
            yalign 0.0
            xfill False
            yfill False


            frame:

                xalign 0.0
                ypos 0.0
                yalign 0.0
                xmargin 3
                xpadding 6
                xfill False
                yfill False
                ysize int(0.7*config.screen_height)

                has vbox

                hbox:

                    textbutton "任务" text_size 14 xsize 80 xfill True idle_background c_lightbrown hover_background c_darkbrown + "CC" selected_idle_background c_darkbrown action (Return("quests"), SelectedIf(qlist == quest_board.quests))
                    textbutton "课程" text_size 14 xsize 80 xfill True idle_background c_lightbrown hover_background c_darkbrown + "CC" selected_idle_background c_darkbrown action (Return("classes"), SelectedIf(qlist == quest_board.classes))


                if qlist:
                    viewport:
                        xalign 0.0
                        yalign 0.0
                        xfill False
                        mousewheel True
                        draggable True
                        scrollbars "vertical"

                        vbox xfill False:
                            spacing 1

                            for quest in qlist:

                                $ ttip = ""

                                if quest.type == "quest":

                                    $ ttip = "这个任务需要" + and_text([stat_name_dict[stat] for stat, v in quest.requirements]) + ".\n"
                                    $ ttip += str(quest.count_eligible_girls()) + "女孩可以完成这项任务."

                                elif quest.type == "class":

                                    $ ttip = "专门课程可能会提高" + and_text([stat_name_dict[stat] for stat, _min, _max in quest.bonuses]) + ".\n"
                                    $ ttip += str(len(quest.enrolled)) + "/" + str(quest.capacity) + "是这门课程的学生."

                                button:
                                    xsize 160
                                    ysize 60
                                    xpadding 4
                                    ypadding 0
                                    xmargin 0
                                    selected_background c_orange
                                    action (SetVariable("selected_quest", quest), Return("change"), SelectedIf(selected_quest == quest))
                                    hovered tt.Action(ttip)

                                    hbox spacing 2 xalign 0.0:

                                        frame background None xsize 60 ysize 60 yalign 0.5:
                                            if quest.pic:
                                                add quest.pic.get(x = 50, y = 50) xalign 0.5 yalign 0.5


                                        vbox yalign 0.5:
                                            if quest.special:
                                                $ text1 = "{image=img_star}"
                                            else:
                                                $ text1 = ""
                                            text text1 + quest.name  size 13
                                            text str(quest.gold) + "金币" size 13

                if calendar.active_contract:
                    text ""
                    text ""
                    button xfill True xpadding 6 ypadding 6 action Return("active_contract"): # hovered Show("contract_tab", contract=calendar.active_contract, x=450, active=True, transition=Dissolve(0.15)) unhovered Hide("contract_tab", transition=Dissolve(0.15)) tooltip "Show active contract (%s day%s left)." % (28-calendar.day, plural(28-calendar.day)):
                        vbox xfill True:
                            text "有效合同" size 14 color c_darkbrown xalign 0.5
                            add ProportionalScale("UI/" + license_dict[1][1], 50, 50) xalign 0.5





screen dark_filter(can_click=True):

    tag dark_filter

    modal False

    zorder 0

    button xfill True yfill True ypadding 0 ymargin 0 ypos 0.075 yanchor 0.0 ymaximum int(0.925*config.screen_height) background c_ui_darkblue:
        if can_click:
            action Return()

# screen dark_filter2():
#
#     tag dark_filter
#
#     modal False
#
#     zorder 0
#
#     frame xfill True yfill True ypadding 0 ymargin 0 ypos 0.075 yanchor 0.0 ymaximum int(0.925*config.screen_height) background c_ui_darkblue


screen personality_screen():

    tag personality_screen

    frame xalign 0.5 yanchor 0.0 yalign 0.1 ysize 320 xfill True xpadding 25 ypadding 10 xmaximum 420 background Frame("UI/paper.webp"): #int(config.screen_width * 0.58):

        has vbox spacing 20

        if selected_girl:

            hbox xalign 0.5 xfill True:
                textbutton "个性" text_size 18 hovered SetVariable("pers_showing", "personality") action NullAction(), SelectedIf(pers_showing=="personality")
                textbutton "品味" text_size 18 hovered SetVariable("pers_showing", "tastes") action NullAction(), SelectedIf(pers_showing=="tastes")
                textbutton "性趣" text_size 18 hovered SetVariable("pers_showing", "sexual") action NullAction(), SelectedIf(pers_showing=="sexual")
                textbutton "事件" text_size 18 hovered SetVariable("pers_showing", "recent") action NullAction(), SelectedIf(pers_showing=="recent")

            hbox spacing 20:

                $ badge = selected_girl.get_badge()
                button background None action NullAction():

                    add selected_girl.portrait.get(100,100)

                    # Add mood meter
                    if selected_girl in (MC.girls + farm.girls):
                        add ProportionalScale(selected_girl.get_mood_picture(), 25, 25) xalign 0.05 yalign 0.05
                        hovered (Show("mood_details", girl=selected_girl, transition=Dissolve(0.15)), tt.Action(selected_girl.get_mood_description("mood")))
                        unhovered Hide("mood_details", transition=Dissolve(0.15)) xpadding 0 ypadding 0 xmargin 0 ymargin 0 xsize 100 ysize 100

                    if badge:
                        add ProportionalScale(badge, 25, 25) xalign 0.95 yalign 0.05

                viewport:
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    ysize 220
                    text selected_girl.get_personality_description(pers_showing) size 14 color c_brown


screen notebook():
    key "mouseup_3" action (Hide("notebook"), Hide("mood_details"))
    key "n" action (Hide("notebook"), Hide("mood_details"))
    use dark_filter()
    use close(Hide("notebook"))
    use personality_screen()



## FARM SCREEN ##

screen farm_tab():

    zorder -11

    use close((SetVariable("selected_destination", "main"), Jump("teleport")))
    use shortcuts()
    use overlay("farm")

    use girl_tab(farm.girls, context="farm")

    if selected_girl and selected_girl in farm.girls:

        key "mouseup_3" action (SetVariable("selected_girl", None))

        use girl_stats(selected_girl, context="farm")

        use button_overlay(selected_girl, context="farm")

        use girl_profile(selected_girl, context="farm")


    else:

        key "mouseup_3" action (SetVariable("selected_destination", "main"), Jump("teleport"))
        key "u" action Return(("items", None))

        frame xsize int(0.625*config.screen_width) ysize 520 xfill True yfill True xalign 0.1 ypos 0.1 background None:

            has vbox xalign 0.5

            text "Gizel的农场" bold True xalign 0

            if farm.girls:
                $ text1 = "啊哈, [MC.name]! 来看看我的宠物?"
                $ pic = "side gizel"
            else:
                $ text1 = "我的奴仆最近很无聊... 你打算什么时候给他们送些新玩伴?"
                $ pic = "side gizel upset"

            button xfill True xmargin 3 ymargin 3 xpadding 6 ypadding 6 action Return(("help", None)) hovered tt.Action("向Gizel寻求帮助，了解农场的情况.") background c_ui_dark:
                has hbox spacing 10
                add pic zoom 0.6 yalign 0.5 idle_alpha 0.8 hover_alpha 1.0
                text text1 yalign 0.5 size 18 justify True italic True xmaximum 0.8

            hbox spacing 15:

                vbox:

                    text "{b}农场畜棚{/b}" size 18 xalign 0.0 ypos 0.3 drop_shadow (2, 2)

                    text "" size 6

                    frame background c_ui_dark:

                        has vbox spacing 6

                        $ ttip = "这个农场每个畜棚可以放置一个女孩."

                        if farm.pens < farm.get_pen_limit():
                            $ ttip += "\n点击这里添加一个新的畜棚花费" + str(farm.get_pen_cost()) + "金币."
                        elif brothel.rank == 5:
                            $ ttip += "你不能再建造任何畜棚."
                        else:
                            $ ttip += "升级你的青楼将可以添加更多的畜棚."

                        $ ttip += "\n(目前可用的畜棚: " + str(farm.pens - len(farm.girls)) + ")"

                        button:
                            xpadding 6
                            ypadding 6
                            action Return(("pen", None))
                            hovered tt.Action(ttip)

                            fixed:
                                fit_first True
                                add farm.pen_pic.get(135, 90) idle_alpha 0.66 hover_alpha 1.0
                                if farm.pens < farm.get_pen_limit():
                                    text "+" xalign 0.5 yalign 0.5 size 36
                                text str(farm.pens) + "{size=-8}/" + str(farm.get_pen_limit()) xalign 0.9 yalign 0.1

                vbox:
                    text "{b}农场状况{/b}" size 18 ypos 0.3 drop_shadow (2, 2)
                    text "" size 6
                    frame background c_ui_dark xfill True:
                        has vbox
                        if farm.get_hurt_minions():
                            text "受伤奴仆: " size 14
                            hbox box_wrap True:
                                for mn in farm.get_hurt_minions():
                                    button background None xalign 0.5 xpadding 0 xmargin 0 ypadding 0 ymargin 0 action NullAction() hovered tt.Action(mn.get_description()):
                                        has hbox
                                        add mn.get_pic(20, 20)
                                        vbox:
                                            text " " + mn.name + ", Lvl " + str(mn.level) size 14 color c_red
                                            text "{color=[c_red]}✙{/color}" size 14

                        else:
                            text "没有什么可报告的." size 14
                # vbox:
                #     text "{b}Farm rules{/b}" size 18 ypos 0.3 drop_shadow (2, 2)
                #     text "" size 6
                #     frame background c_ui_dark xfill True:
                #         has vbox
                #
                #         text "" size 6
                #         grid 2 3:
                #             transpose True
                #             spacing 6
                #             text "Training mode:" size 14
                #             text "Holding mode:" size 14
                #             text "Auto-resting:" size 14
                #             text farm.default_mode.capitalize() size 14 bold True
                #             text farm.default_holding.capitalize() size 14 bold True
                #             text farm.default_resting.capitalize() size 14 bold True
                #
                #         text "" size 10
                #         textbutton "Change rules" text_size 18 xalign 0.5 action Return(("rules", None)) hovered tt.Action("Define the default rules applicable to girls when they are sent to the farm (individual rules can be set for each girl).")

            text ""

            hbox spacing 25:
                text "{b}设施与奴仆{/b}" size 18 yalign 0.5 drop_shadow (2, 2)
                textbutton "使用物品" text_size 18 action Return(("items", None)) hovered tt.Action("对你的奴仆使用一个物品.") yalign 0.5

            text "" size 6

            frame:
                background c_ui_dark
                xfill True

                has hbox spacing 25

                for type in all_minion_types:
                    $ inst = farm.installations[farm_installations_dict[type]]

                    vbox xsize 130 xfill True:

                        button:
                            xpadding 6
                            ypadding 6
                            insensitive_background c_darkgrey + "E5"

                            if inst.can_upgrade():
                                action Return(("upgrade", inst))
                                if inst.rank > 0:
                                    hovered tt.Action("点击这里升级" + farm_related_dict[inst.name] + "的能力需要" + str(inst.get_price()) + "金币.")
                                else:
                                    hovered tt.Action("点击这里建造" + farm_related_dict[inst.name] +  "需要" + str(inst.get_price()) + "金币.")
                            else:
                                action NullAction()
                                if inst.rank < 5:
                                    hovered tt.Action("你无法升级" + farm_related_dict[inst.name] + "直到你获得更高的青楼执照.")
                                else:
                                    hovered tt.Action("你无法进一步升级" + farm_related_dict[inst.name] + "了.")

                            vbox:
                                spacing 3
                                fixed:
                                    fit_first True
                                    add inst.get_pic().get(120, 80) idle_alpha 0.66 hover_alpha 1.0
                                    if inst.can_upgrade():
                                        text "+" xalign 0.5 yalign 0.5 size 36
                                    text str(inst.rank) + "{size=-8}/" + str(district.rank) xalign 0.9 yalign 0.1

                                if inst.rank > 0:
                                    text farm_related_dict[inst.name.capitalize()] size 14 xcenter 0.5
                                else:
                                    text "???" size 14 xcenter 0.5

#            text "" size 6
            frame:
                background c_ui_dark
                xsize 0.99
                xfill True
                has hbox spacing 25
                for type in all_minion_types:

                    vbox xsize 130 xfill True:

                        if len(farm.get_minions(type)) > 0:
                            text str(len(farm.get_minions(type))) + " " + farm_related_dict[type.capitalize()] size 14 bold True xalign 0.5

                        text "" size 6

                        for mn in farm.get_minions(type):

                            button background None xalign 0.5 xpadding 0 xmargin 0 ypadding 0 ymargin 0 action NullAction() hovered tt.Action(mn.get_description()):

                                has hbox
                                add mn.get_pic(20, 20)

                                vbox:
                                    text " " + mn.name + ", Lvl " + str(mn.level) size 14:
                                        if mn.hurt:
                                            color c_red
                                    # if mn.hurt:
                                    #     text "{color=[c_red]}✙{/color}" size 14


screen mood_details(girl):

    frame:
        background c_ui_darker
        xalign 0.5
        yalign 0.2
        xpadding 0.05
        ypadding 0.05
        xfill True
        xmaximum 350
        ymaximum int(0.5*config.screen_height)

        has vbox

        xfill True

        spacing 6

        text girl.name + "的心情" color c_orange xalign 0.5

        text "" size 6

        $ love_text, fear_text, mood_text, mood_change_text, mood_factors = girl.get_mood_description()

#        text love_text size 14

#        text fear_text size 14

#        text "" size 6

        text mood_text size 14

        text "" size 12

        text mood_change_text size 14

        text "" size 6

        text mood_factors size 12 color c_white


screen love_button(girl):

    $ ttip = girl.get_mood_description("love")

    if debug_mode:
        $ ttip += "\n(" + str(round(girl.get_love(), 1)) + ")"

    button xmargin 0 xpadding 0 xalign 0.5 yalign 0.5:
        background None
        action NullAction()
        tooltip ttip

        $ l = girl.get_love()

        if l >= 5:

            $ h = l // 2.5 + 10

            add ProportionalScale("UI/heart.webp", h, h) xalign 0.5 yalign 0.5 idle_alpha 0.66 hover_alpha 0.8

        elif l <= -5:
            $ h = l // -2.5 + 10

            add ProportionalScale("UI/broken heart.webp", h, h) xalign 0.5 yalign 0.5 idle_alpha 0.66 hover_alpha 0.8

        else:
            add ProportionalScale("UI/love question.webp", 20, 20) xalign 0.5 yalign 0.5 idle_alpha 0.66 hover_alpha 0.8


screen fear_button(girl):

    $ ttip = girl.get_mood_description("fear")

    if debug_mode:
        $ ttip += "\n(" + str(round(girl.get_fear(), 1)) + ")"

    button xmargin 0 xpadding 0 xalign 0.0 yalign 0.5:
        background None
        action NullAction()
        tooltip ttip

        $ f = girl.get_fear()

        if f >= 5:

            $ h = f // 2.5 + 10

            add ProportionalScale("UI/skull.webp", h, h) xalign 0.5 yalign 0.5 idle_alpha 0.66 hover_alpha 0.8

        elif f <= -5:
            $ h = f // -2.5 + 10

            add ProportionalScale("UI/droplet.webp", h, h) xalign 0.5 yalign 0.5 idle_alpha 0.66 hover_alpha 0.8

        else:
            add ProportionalScale("UI/fear question.webp", 20, 20) xalign 0.5 yalign 0.5 idle_alpha 0.66 hover_alpha 0.8

screen sex_details(girl):

    frame:
        background c_ui_darker
        xalign 0.5
        yalign 0.8

        has vbox

        spacing 6

        text girl.name + "的性偏好" xalign 0.5 color c_orange

        text "" size 6

        grid 4 8 spacing 6:

            text "行为" size 14 bold True
            text "嗜好" size 14 bold True
            text "训练意向" size 14 bold True xalign 0.5
            text "工作意向" size 14 bold True xalign 0.5

            for act in extended_sex_acts:
                text girl_related_dict[act.capitalize()] size 14 bold True

                if debug_mode:
                    $ text1 = " (" + str(round_int(girl.preferences[act])) + ")"
                else:
                    $ text1 = ""

                if girl.personality_unlock[act]:
                    text preference_color[girl.get_preference(act)] % girl_related_dict[girl.get_preference(act).capitalize()] + text1 size 14
                else:
                    text "未知" + text1 size 14 italic True

                if girl.personality_unlock[act]:

                    $ tch = girl.get_training_chance(act)

                    text str(round_int(tch)) + "%" size 14 xalign 0.5:
                        if tch > 95:
                            color color_dict["+++"]
                        elif tch > 80:
                            color color_dict["++"]
                        elif tch > 66:
                            color color_dict["+"]
                        elif tch > 50:
                            color color_dict["normal"]
                        elif tch > 33:
                            color color_dict["-"]
                        elif tch > 20:
                            color color_dict["--"]
                        elif tch <= 5:
                            color color_dict["---"]

                else:
                    text "?" size 14 xalign 0.5


                if act == "naked":
                    text "" size 14 xalign 0.5

                elif girl.personality_unlock[act]:

                    if girl.will_do_sex_act(act)[0]:

                        $ wch = girl.get_working_chance(act)

                        text str(round_int(wch)) + "%"  size 14 xalign 0.5:
                            if wch > 95:
                                color color_dict["+++"]
                            elif wch > 80:
                                color color_dict["++"]
                            elif wch > 66:
                                color color_dict["+"]
                            elif wch > 50:
                                color color_dict["normal"]
                            elif wch > 33:
                                color color_dict["-"]
                            elif wch > 20:
                                color color_dict["--"]
                            elif wch <= 5:
                                color color_dict["---"]

                    else:
                        text "0%" size 14 xalign 0.5color color_dict["---"]

                else:
                    text "?" size 14 xalign 0.5


## CHALLENGE SCREENS ##

screen challenge_menu(header="你要怎么做?", challenges=[], cancel=False):
    # challenges is a list of arrays (caption, challenge_type, base_diff) where caption is the text displayed on the button.
    # challenge_type must be an existing type in MC.challenges. base_diff is the lowest possible difficulty to achieve success.
    # cancel must be an array (caption, return_value) if the challenge can be avoided.

    tag challenge_menu

    modal True

    use overlay()

    frame xalign 0.5 yalign 0.5:

        has vbox spacing 10

        text header xalign 0.5 color c_brown

        hbox:

            for title, challenge_type, diff in challenges:
                $ chal = MC.challenges[challenge_type]
                $ diff = chal.adjust_diff(diff)
                $ ttip = "{b}" + chal.name + " 挑战{/b}: 这是对你{b}" + chal.stat.capitalize() + "{/b} (" + str_int(MC.get_stat(chal.stat)) + ")" + ". 估计难度: {b}" + chal.estimate_diff(diff=diff) + "{/b}."

                button background None action(Return(challenge_type)):
                    vbox:
                        button:
                            ysize 132
                            yfill True
                            xpadding 6
                            ypadding 6
                            insensitive_background "#1A2B47E5"
                            action(Return(challenge_type))
                            hovered tt.Action(ttip)

                            fixed yalign 0.5:
                                fit_first True
                                add chal.get_pic(200, 120) idle_alpha 0.66 hover_alpha 1.0
                                text chal.estimate_diff(diff=diff) size 12
                                frame background None xpadding 10 xalign 0.5 yalign 0.5:
                                    text title size 18 bold True

        if cancel:
            textbutton cancel[0] action Return(cancel[1]) xalign 0.5

screen challenge(name, diff, raw=False, bonus=0, opponent_bonus=0):

    tag challenge

    modal True

    $ chal = MC.challenges[name]

    default phase = 0

    frame background Frame(chal.pic.get(int(0.5*config.screen_width), int(0.5*config.screen_height))) xalign 0.5 yalign 0.5 xsize int(0.5*config.screen_width) ysize int(0.4*config.screen_height) xfill True yfill True:

        has vbox

        frame xalign 0.5 xfill True background "#22222288":
            text "玩家的挑战: " + chal.name xalign 0.5

        text ""

        hbox xfill True spacing 10:

            frame background "#22222288" xfill True xsize 250 ysize 160 xpadding 10 ypadding 10:

                vbox:
                    text "玩家" + chal.stat.capitalize() + ": " + str_int(MC.get_stat(chal.stat, raw=True)) size 18
                    text "有效加成: " + str_int(bonus + MC.get_stat(chal.stat, raw) - MC.get_stat(chal.stat, raw=True) + MC.get_effect("change", name + " challenges")) size 18
                    text ""

                    if phase >= 1:
                        text "摇骰: " + "{image=" + "img_dice" + str(chal.d) + "}" size 18
                        text ""

                        if phase >= 2:
                            text "最终结果: " + str(round_int(chal.score)) size 18

                    elif chal.opposed:
                        textbutton "摇骰" action (SetScreenVariable("phase", 1), Play("sound", s_dice))
                    else:
                        textbutton "摇骰" action (SetScreenVariable("phase", 2), Play("sound", s_dice))



            frame background "#22222288" xsize 250 xfill True ysize 160 xalign 1.0 xpadding 6 ypadding 6:
                has vbox

                if chal.opposed:
                    text "对手 " + chal.stat.capitalize() + ": " + str_int(diff + opponent_bonus) size 18
                    text "" size 18
                    text ""

                    if phase >= 2:
                        text "摇骰: " + "{image=" + "img_dice" + str_int(chal.d_op) + "}" size 18
                        text ""
                        text "最终结果: " + str_int(chal.score_op) size 18
                    elif phase == 1:
                        textbutton "摇骰" action (SetScreenVariable("phase", 2), Play("sound", s_dice))
                else:
                    text "难度: " + str_int(diff) size 18

        if phase >= 2:
            text ""
            textbutton "OK" xalign 0.5 action Return()


#### LETTER SCREEN ####

screen letter(header="", message="", signature = ""): # Returns True upon closing

    tag letter

    modal True

    key "mouseup_3" action (Return(True))

    frame xalign 0.5 ypos 0.1 xsize 0.8 ysize 0.9 xfill True yfill True xpadding 50 ypadding 25 background Frame("UI/paper.webp"):

        has vbox
        xsize 0.75

        hbox xfill True:
            text header xalign 0.0 size 32 font "MATURASC.TTF" color c_black
            fixed fit_first True xalign 1.0 yalign 0.5:
                use close(act=Return(True), name = "close")

        text ""
        text ""

        text message size 20 font "bk.TTF" color c_black

        text ""
        text ""

        text signature size 24 font "bk.TTF" xalign 1.0 color c_black


#### RESOURCES ####

screen resource_tab(rlist="MC", sz = 15, sp = 3, x=0.0, y=0.0, bg=None): # If provided, rlist must be a list of tuples (resource_name, number)

    if rlist == "MC":
        frame background bg xpadding sp ypadding sp xalign x yalign y xanchor 0 yanchor 0:
            has hbox spacing sp//2 xalign 0 box_wrap True

            for resource in [resource_dict[r] for r in build_resources]:

                if resource.rank <= district.rank:
                    button background None action NullAction() tooltip (resource.description + " You have " + str(MC.resources[resource.name]) + " " + resource.name + " in store.") xpadding sp ypadding sp:
                        has hbox spacing sp*2 yalign 0.5
                        add resource.pic.get(sz, sz) yalign 0.5
                        if MC.resources[resource.name] < 100:
                            text str(MC.resources[resource.name]) size 12 yalign 0.5
                        else:
                            text "99+" size 10 yalign 0.5
    else:
        frame background bg xpadding sp ypadding sp xalign x yalign y:
            has hbox xalign 0 box_wrap True

            for resource, nb in rlist:
                button background None action NullAction() xpadding sp*2 ypadding sp*2:
                    has hbox box_wrap True spacing sp*2
                    add resource_dict[resource].pic.get(sz, sz) yalign 0.5
                    text str(nb) size 14 yalign 0.5:
                        if MC.has_resource(resource, nb):
                            color c_emerald
                        else:
                            color c_red


screen resource_gain(resource, number): # Where resource is a string

    tag resource_gain

    zorder 11

    button:
        xalign 0.5
        yalign 0.5
        xsize 0.6
        ysize 0.5
        xpadding 50

        has hbox
        xalign 0.5
        yalign 0.5
        spacing 25

        add resource_dict[resource].get_pic(100, 100)
        text "+" + str(round_int(number)) + " " + resource size 28 yalign 0.5


screen resource_exchange():

    tag exchange

    default source = None
    default target = None
    default source_name = None
    default target_name = None
    default source_nb = 0
    default target_nb = 0
    default t = 0

    use shortcuts()
    use overlay()
    use close(Return("quit"))

    key "mouseup_3" action Return("quit")

#    timer 0.5 repeat True action SetScreenVariable("t", int(100*renpy.random.random())/10.0)

    fixed ypos 0.1 xfill True yfill True:

    # Weekly deals

        frame xsize 250 yanchor 1.0 ypos 0.2:
            has vbox
            text "每周贸易信息" size 14 italic True color c_brown
            hbox spacing 3 box_wrap True:
                for r in calendar.scarce:
                    $ resource = resource_dict[r]
                    if resource.rank <= story_flags["builder license"]:
                        button background None action NullAction() tooltip "本周" + r.capitalize() + "缺货. 价值正在上升.":
                            has hbox spacing 3
                            add resource.pic.get(20, 20) yalign 0.5
                            text "▲" size 16 color c_emerald yalign 0.5

                for r in calendar.discounted:
                    $ resource = resource_dict[r]
                    if resource.rank <= story_flags["builder license"]:
                        button background None action NullAction() tooltip "本周" + r.capitalize() + "泛滥成灾. 价值正在下降.":
                            has hbox spacing 3
                            add resource.pic.get(20, 20) yalign 0.5
                            text "▼" size 16 color c_red yalign 0.5



    # Left frame

        frame xsize 250 ypos 0.2:
            has vbox

#            text(str(t))

            text "你的资源" size 14 italic True color c_brown

            button xfill True ysize 60 action (SetScreenVariable("source", "gold"), SetScreenVariable("source_name", "gold"), SetScreenVariable("source_nb", 0), SelectedIf(source=="gold")) tooltip "Use your gold to buy resources":
                selected_background c_emerald
                has hbox xfill True yfill True spacing 10
                add ProportionalScale("UI/coin.webp", 40, 40) yalign 0.5
                hbox spacing 6 xfill True yalign 0.5:
                    text "金币" size 18
                    text '{:,}'.format(round_int(MC.gold)) xalign 1.0 size 16


            for r in build_resources:
                $ resource = resource_dict[r]

                if resource.rank <= story_flags["builder license"]:

                    button xfill True ysize 60 action (SetScreenVariable("source", resource), SetScreenVariable("source_name", resource.name), SetScreenVariable("source_nb", 0), SelectedIf(source==resource)) tooltip ("Trade your " + r + " for other resources"):
                        selected_background c_emerald
                        has hbox xfill True yfill True spacing 10
                        add resource.pic.get(40, 40) yalign 0.5
                        vbox xfill True spacing 6 yalign 0.5:
                            hbox spacing 3:
                                text resource_name_dict[resource.name.capitalize()] size 18
                                if r in calendar.discounted:
                                    text "▼" size 14 yalign 0.5
                                elif r in calendar.scarce:
                                    text "▲" size 14 yalign 0.5
                            hbox spacing 6 xfill True:
                                text "库存: " size 14 yalign 1.0
                                text str(MC.resources[resource.name]) xalign 1.0 size 16

        # Right frame

        if source:

            frame xsize 250 xalign 1.0 ypos 0.2:
                has vbox

                text "市场资源" size 14 italic True color c_brown

                button xfill True ysize 60:
                    if "gold" != source:
                        action (SetScreenVariable("target", "gold"), SetScreenVariable("target_name", "gold"), SetScreenVariable("target_nb", 0), SelectedIf("gold"==target))
                        tooltip "卖掉你的" + source_name + "换取金币"
                        selected_background c_emerald

                    hbox xfill True yfill True spacing 10:
                        add ProportionalScale("UI/coin.webp", 40, 40) yalign 0.5
                        vbox xfill True spacing 6 yalign 0.5:
                            text "Gold" size 18
                            if "gold" != source:
                                hbox spacing 6:
                                    $ rate = get_exchange_rate(source, "gold")
                                    if rate < 1:
                                        $ text2 = "" + str(round_up(1/rate)) + "换1"
                                    else:
                                        $ text2 = "1换" + str(round_up(rate)) + ""

                                    text text2 size 14
                                    add source.pic.get(16, 16)

                for r in build_resources:
                    $ resource = resource_dict[r]

                    if resource.rank <= story_flags["builder license"]:

                        button xfill True ysize 60:
                            if resource != source:
                                action (SetScreenVariable("target", resource), SetScreenVariable("target_name", resource.name), SetScreenVariable("target_nb", 0), SelectedIf(resource==target))
                                tooltip "用" + r +"换取你的" + source_name
                                selected_background c_emerald
                            hbox xfill True yfill True spacing 10:
                                add resource.pic.get(40, 40) yalign 0.5
                                vbox xfill True spacing 6 yalign 0.5:
                                    hbox spacing 3:
                                        text resource_name_dict[resource.name.capitalize()] size 18
                                        if r in calendar.discounted:
                                            text "▼" size 14 yalign 0.5
                                        elif r in calendar.scarce:
                                            text "▲" size 14 yalign 0.5
                                    if resource != source:
                                        hbox spacing 6:
                                            $ rate = get_exchange_rate(source, resource)
                                            if rate < 1:
                                                $ text2 = "" + str(round_up(1/rate)) + "换1"
                                            else:
                                                $ text2 = "1换" + str(round_up(rate)) + ""

                                            text text2 size 14
                                            if source == "gold":
                                                add ProportionalScale("UI/coin.webp", 16, 16)
                                            else:
                                                add source.pic.get(16, 16)

    # Middle window

    if source and target and (source != target):

        $ rate = get_exchange_rate(source, target)

        if source_nb == 0 or target_nb == 0:
            if rate < 1:
                $ source_nb = round_up(1/rate)
                $ target_nb = 1

            elif rate >= 1:
                $ source_nb = 1
                $ target_nb = round_up(rate)

        frame xalign 0.5 yalign 0.6 xsize 400 xpadding 20 ypadding 20 background c_ui_dark:

            has vbox xfill True

            hbox xfill True spacing 6 ysize 70:
                if source != "gold":
                    add source.pic.get(60, 60)
                else:
                    add ProportionalScale("UI/coin.webp", 65, 65)

                text "[source_nb]" size 32 xalign 0.0 yalign 0.5:
                    if source == "gold":
                        if MC.gold >= source_nb:
                            color c_white
                        else:
                            color c_red
                    elif MC.resources[source_name] >= source_nb:
                        color c_white
                    else:
                        color c_red


                text "➜" size 54 xalign 0.5 yalign 0.5

                text "[target_nb]" size 32 color c_white xalign 1.0 yalign 0.5

#                add "UI/arrow.webp" xalign 0.5

                if target != "gold":
                    add target.pic.get(60, 60) xalign 1.0
                else:
                    add ProportionalScale("UI/coin.webp", 65, 65) xalign 1.0


            hbox xfill True:
                textbutton "-" xsize 65 ysize 65 text_size 32:
                    if rate < 1 and target_nb > 1:
                        action (SetScreenVariable("target_nb", target_nb-1), SetScreenVariable("source_nb", round_up((target_nb-1)/rate)))
                    elif rate >= 1 and source_nb > 1:
                        action (SetScreenVariable("source_nb", source_nb-1), SetScreenVariable("target_nb", round_up((source_nb-1)*rate)))

                if source == "gold":
                    $ text1 = "买"
                else:
                    $ text1 = "交换"

                textbutton text1 xalign 0.5 xsize 0.8 ysize 65:
                    if source == "gold" and MC.gold >= source_nb:
                        action Return(("gold", target_name, source_nb, target_nb))
                        tooltip "买" + str(target_nb) + "份" + target_name + "得到" + str(source_nb) + " " + target_name
                    elif MC.resources[source_name] >= source_nb:
                        action Return((source_name, target_name, source_nb, target_nb))
                        tooltip "交换" + str(source_nb) + "份" + source_name + "得到" + str(target_nb) + " " + target_name

                textbutton "+" xsize 65 ysize 65 text_size 32 xalign 1.0:
                    if rate < 1:
                        action (SetScreenVariable("target_nb", target_nb+1), SetScreenVariable("source_nb", round_up((target_nb+1)/rate)))
                    elif rate >= 1:
                        action (SetScreenVariable("source_nb", source_nb+1), SetScreenVariable("target_nb", round_up((source_nb+1)*rate)))



## MODAL INVISIBLE SCREEN ##

screen modal():

    modal True

screen invisible_button():

    zorder 99

    key "K_UP" action Function(renpy.notify, "你宝贵的键盘现在救不了你!")
    key "K_DOWN" action Function(renpy.notify, "你宝贵的键盘现在救不了你!")

    vbox:
        style "menu"
        xalign 0.5
        xfill True
        yalign 0.5
        yfill True

        textbutton "" xalign 0.5 background None:
            style "menu_choice_button"
        textbutton "" xalign 0.5 background None action NullAction() hovered Function(this_is_a_hentai_game_so_why_are_you_trying_to_act_classy_all_of_a_sudden):
            style "menu_choice_button"






## MOD SCREENS ##


screen mods():

    tag menu

    # Include the navigation.
    use navigation

    if detected_mods:
        default selected_mod = detected_mods.values()[0]
    else:
        default selected_mod = None

    frame xsize 0.9:
        style_group "pref"
        has vbox

        xfill True

        text "Mod安装" color c_brown

        hbox:
            viewport xsize 200:
                mousewheel True
                draggable True
                scrollbars "vertical"

                has vbox xfill False

#                button:
#                    xsize 160
#                    ysize 60
#                    xfill True
#                    xalign 0.0
#                    xpadding 4
#                    xmargin 0
#                    action NullAction()

                for mod in detected_mods.values():
                    if mod:
                        button xfill False action SelectedIf(selected_mod == mod) hovered SetScreenVariable("selected_mod", mod), SetField(mod, "seen", True):
                            if not mod.seen:
                                at blink

                            text mod.name size 18:
                                if mod.active:
                                    bold True



            frame xsize 0.7:
                has vbox
                xfill True

                if selected_mod:

                    $ selected_mod.seen = True

                    text selected_mod.full_name color c_brown
                    text ""
                    if selected_mod.pic:
                        add selected_mod.pic.get(320, 320)
                    text ""
                    if selected_mod.active:
                        text "已激活的Mod" bold True italic True color c_emerald
                    else:
                        text "未激活的Mod" italic True color c_darkgrey

                    text ""
                    text selected_mod.description size 14 color c_brown

                    text ""

                    hbox:
                        if selected_mod.active:
                            textbutton "解除激活Mod" action renpy.curried_invoke_in_new_context(selected_mod.deactivate)
                        else:
                            textbutton "激活Mod" action renpy.curried_invoke_in_new_context(selected_mod.activate)

                        # textbutton "Reset Mod" action renpy.curried_invoke_in_new_context(reset_mod, selected_mod)


### GIRL INTERACT SCREEN
screen free_girl_interact(girl):

    tag girl_interact

    use dark_filter()
    use overlay(current_screen = "location")
    use shortcuts()
    use girl_stats(girl, "free")
    use girl_profile(girl, "free")

    key "mouseup_3" action (Return("back"))
    use close(Return("back"))

    default menu_choice = last_free_interact_menu

    frame:
        background c_ui_darkblue
        xsize 325
        ysize int(0.7*config.screen_height)
        xmargin 3
        xalign 1.0
        ypos 0.1

        has vbox spacing 3

        text "城市女孩互动" size 28 font "bk.ttf"

        text "" size 4

        hbox box_wrap True:
            $ choices = ["chat", "give", "flirt", "fun"]

            for cap in choices:
                textbutton interact_name_dict[cap.capitalize()] action SelectedIf(menu_choice == cap) hovered SetScreenVariable("menu_choice", cap) text_size 16 xpadding 6 ypadding 6 text_selected_bold True xsize 60

        for cat in free_interact_dict[menu_choice]:

            if [top for top in free_interact_dict[cat] if top.is_shown(girl)]:

                text "" size 18
                text cat size 14

            for topic in free_interact_dict[cat]:
                if topic.is_shown(girl):
                    $ text1 = " ([topic.AP_cost]{image=img_AP})"

                    textbutton topic.caption + text1 background None text_size 14:
                        if topic.is_available(girl)[0]:
                            action Return(topic)
                            text_hover_underline True
                        else:
                            text_color c_grey
                            action NullAction()
                        if topic.is_available(girl)[1]:
                            tooltip topic.is_available(girl)[1]

# This code could be used for future custom city dialogue in _BK.ini

#        if menu_choice == "misc" and girl.init_dict["background story/free_interact_prompt"]:
#            text ""
#            text "OTHER" size 14

#            python:
#                try:
#                    custom_caption, custom_option_label, custom_cost = girl.init_dict["background story/free_interact_prompt"]
#                except:
#                    custom_caption, custom_option_label = girl.init_dict["background story/free_interact_prompt"] # For backwards compatibility with older _BK.ini
#                    custom_cost = 0
#                topic = GirlInteractionTopic("misc", None, custom_caption, "slave_custom_option", AP_cost=custom_cost)

#            textbutton topic.caption + " ([topic.AP_cost]{image=img_AP})" background None text_size 14:
#                if topic.is_available(girl)[0]:
#                    action Return(topic)
#                    text_hover_underline True
#                else:
#                    text_color c_grey
#                    action NullAction()
#                    tooltip topic.is_available(girl)[1]


screen girl_interact(girl, free=False):

    tag girl_interact

    use overlay(current_screen = "girls")
    use girl_stats(girl, "girls")
    use girl_profile(girl, "girls")

    if not free:
        use shortcuts()

    key "mouseup_3" action (Return("back"))
    use close(Return("back"))

    key "K_LEFT" action Return("previous")
    key "K_RIGHT" action Return("next")

    default menu_choice = last_interact_menu

    if free:
        $ normal_cost = 0
        $ adv_cost = 0
    else:
        $ normal_cost = 1
        $ adv_cost = 2

    frame:
        background c_ui_darkblue
        xsize 325
        ysize int(0.7*config.screen_height)
        xmargin 3
        xalign 1.0
        ypos 0.1

        has vbox spacing 2

        text "女孩互动" size 28 font "bk.ttf"
#        text "Every interaction costs 1 AP" size 14 italic True
        text "" size 4

        hbox box_wrap True:
            if free:
                $ choices = ["train", "magic"]
                if menu_choice not in choices:
                    $ menu_choice = "train"
            else:
                $ choices = ["chat", "train", "magic", "react", "misc"]

            for cap in choices:
                textbutton interact_name_dict[cap.capitalize()] action SelectedIf(menu_choice == cap) hovered SetScreenVariable("menu_choice", cap) text_size 16 xpadding 6 ypadding 6 text_selected_bold True xsize 60

        for cat in interact_dict[menu_choice]:

            if [top for top in interact_dict[cat] if top.is_shown(girl)]:

                text ""
                text cat size 14

            for topic in interact_dict[cat]:
                if topic.is_shown(girl):

                    if topic.advanced:
                        hbox spacing 0:

                            textbutton topic.caption + get_act_weakness_symbol(girl, topic.act) background None text_size 13 text_color c_white xsize 100 text_xalign 0.0 action NullAction():
                                if girl.personality_unlock[topic.act]:
                                    tooltip "你知道[girl.name]对" + girl_related_dict[topic.act] + girl_related_dict[girl.get_reaction_to_act(topic.act)] + "。"
                                else:
                                    tooltip "你不知道[girl.name]对" + girl_related_dict[topic.act] + "有什么反应。"

                            if topic.type == "train":
                                textbutton "谈话" background None text_size 13:
                                    if topic.is_available(girl, "lecture", free)[0]:
                                        text_hover_underline True
                                        action Return([topic, "lecture"])
                                        tooltip "给[girl.name]讲讲" + girl_related_dict[topic.act] + "有多美好.\n需要" + str(normal_cost) + "{image=img_AP}."
                                    else:
                                        text_color c_grey
                                        action NullAction()
                                        tooltip topic.is_available(girl, "lecture", free)[1]

                            textbutton "训练" background None text_size 13:
                                if topic.is_available(girl, "train", free)[0]:
                                    text_hover_underline True
                                    action Return([topic, "train"])
                                    if topic.gold_cost:
                                        tooltip "对[girl.name]的" + girl_related_dict[topic.act] + "进行训练.\n需要" + str(normal_cost) + "{image=img_AP} 和 " + str(topic.get_gold_cost()) + "{image=img_gold}."
                                    else:
                                        tooltip "对[girl.name]的" + girl_related_dict[topic.act] + "进行训练.\n需要 " + str(normal_cost) + "{image=img_AP}."
                                else:
                                    text_color c_grey
                                    action NullAction()
                                    tooltip topic.is_available(girl, "train", free)[1]

                            $ pos_reaction, neg_reaction = girl.test_weakness(topic.act)

                            if not (pos_reaction or neg_reaction):
                                $ ttip = event_color["a little bad"] % "可以进行高级培训，但她对这种性行为并不特别敏感."
                            else:
                                $ ttip = "你可以使用高级训练来找出更多关于她的定点，并利用它们进行更快的训练."

                            textbutton "高级训练" background None text_size 13:
                                if topic.is_available(girl, "advanced", free)[0]:
                                    text_hover_underline True
                                    action Return([topic, "advanced"])
                                    if topic.gold_cost:
                                        tooltip ttip + "\n需要 " + str(adv_cost) + "{image=img_AP} 和 " + str(topic.get_gold_cost()) + "{image=img_gold}."
                                    else:
                                        tooltip ttip + "\n需要 " + str(adv_cost) + "{image=img_AP}."
                                else:
                                    text_color c_grey
                                    action NullAction()
                                    tooltip topic.is_available(girl, "advanced", free)[1]
                    else:
                        if topic.label == "slave_hypnotize_method":
                            $ text1 = ": " + str(girl.magic_training)
                        else:
                            $ text1 = ""

                        if free:
                            $ text1 += " (0{image=img_AP}"
                        else:
                            $ text1 += " ([topic.AP_cost]{image=img_AP}"
                        if topic.gold_cost:
                             $ text1 += ", " + str(topic.get_gold_cost()) + "{image=img_gold}"
                        $ text1 += ")"

                        textbutton topic.caption + text1 background None text_size 14:
                            if topic.is_available(girl, free=free)[0]:
                                action Return(topic)
                                text_hover_underline True
                            else:
                                text_color c_grey
                                action NullAction()
                                tooltip topic.is_available(girl, free=free)[1]

        if menu_choice == "misc" and girl.init_dict["background story/interact_prompt"]:
            text ""
            text "其他" size 14

            python:
                custom_caption = girl.init_dict["background story/interact_prompt"][0]
                try:
                    custom_cost = girl.init_dict["background story/interact_prompt"][2]
                except:
                    custom_cost = 0 # For backwards compatibility with older _BK.ini

                topic = GirlInteractionTopic("misc", None, custom_caption, "slave_custom_option", AP_cost=custom_cost)

            textbutton topic.caption + " ([topic.AP_cost]{image=img_AP})" background None text_size 14:
                if topic.is_available(girl)[0]:
                    action Return(topic)
                    text_hover_underline True
                else:
                    text_color c_grey
                    action NullAction()
                    tooltip topic.is_available(girl)[1]


screen free_girl_stats(girl):

    modal True

    use girl_stats(girl, context="free")
    use button_overlay(girl, context="free")
    use close(Return())
    key "mouseup_3" action (Return())



#### BK Preference Screen ####

screen h_content():

    tag menu

    # Include the navigation.
    use navigation

    viewport xsize 0.8:
        mousewheel True
        draggable True
        scrollbars "vertical"

        frame:
            style_group "pref"
            has vbox xfill True

            label _("内容设置")

            # Objectionable content

            text "\n激活或停用令人反感的内容(不会影响故事场景)" color c_brown italic True size 16

            if "beast" in persistent.forbidden_tags:
                $ text1 = "OFF"
            else:
                $ text1 = "ON"

            textbutton _("兽交: " + text1) text_size 18 xalign 0.0 xsize 0.8 xfill True:
                if "beast" in persistent.forbidden_tags:
                    action RemoveFromSet(persistent.forbidden_tags, "beast")
                else:
                    action AddToSet(persistent.forbidden_tags, "beast")

            if "monster" in persistent.forbidden_tags:
                $ text1 = "OFF"
            else:
                $ text1 = "ON"

            textbutton _("怪物/触手: " + text1) text_size 18 xalign 0.0 xsize 0.8 xfill True:
                if "monster" in persistent.forbidden_tags:
                    action RemoveFromSet(persistent.forbidden_tags, "monster")
                else:
                    action AddToSet(persistent.forbidden_tags, "monster")

            if "machine" in persistent.forbidden_tags:
                $ text1 = "OFF"
            else:
                $ text1 = "ON"

            textbutton _("机器: " + text1) text_size 18 xalign 0.0 xsize 0.8 xfill True:
                if "machine" in persistent.forbidden_tags:
                    action RemoveFromSet(persistent.forbidden_tags, "machine")
                else:
                    action AddToSet(persistent.forbidden_tags, "machine")

            text ""

            label _("图片设置")

            # Missing Picture algorithm

            text "\n(默认)图片库和女孩图片包的选项" color c_brown italic True size 16

            if persistent.use_stock_pictures["missing"]:
                $ text1 = "找不到可用图片时: 使用默认图片库"
            else:
                $ text1 = "找不到可用图片时: 随机一位女孩图片包"

            if persistent.use_stock_pictures["low"]:
                $ text2 = "当图片数量太少时: 混合使用图库和女孩图片包"
            else:
                $ text2 = "当图片数量太少时: 只使用该女孩图片包"

            textbutton text1 text_size 18 xalign 0.0 xsize 0.8 xfill True action ToggleDict(persistent.use_stock_pictures, "missing")
            textbutton text2 text_size 18 xalign 0.0 xsize 0.8 xfill True action ToggleDict(persistent.use_stock_pictures, "low")

            # Advanced Picture algorithm

            text "\n高级培训图片的选项" color c_brown italic True size 16
            if persistent.fix_pic_balance == fix_pic_balance_variety:
                textbutton "高级培训图片: 种类更丰富" text_size 18 xalign 0.0 xsize 0.8 xfill True action SetField(persistent, "fix_pic_balance", fix_pic_balance_accuracy)
            else:
                textbutton "高级培训图片: 更好的精确度" text_size 18 xalign 0.0 xsize 0.8 xfill True action SetField(persistent, "fix_pic_balance", fix_pic_balance_variety)

            # Group/Bis Picture algorithm

            text "\n群体和百合图片的行为选项" color c_brown italic True size 16
            textbutton {True: "群交: 将群交图片与普通图片混合", False: "群交: 只使用群交图片"}[persistent.mix_group_pictures] text_size 18 xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "mix_group_pictures")
            textbutton {True: "百合: 将百合图片与普通图片混合", False: "百合: 只使用百合图片"}[persistent.mix_bis_pictures] text_size 18 xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "mix_bis_pictures")

            # Naked girls' settings


            text "\n奴隶市场女孩图片的行为选项" color c_brown italic True size 16
            textbutton {True: "允许奴隶市场上的裸体图片", False: "不允许奴隶市场上的裸体图片"}[persistent.naked_girls_in_slavemarket] text_size 18 xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "naked_girls_in_slavemarket")

            text "\n自由女孩图片的行为选项" color c_brown italic True size 16
            textbutton {True: "允许在城市中出现裸体图片(自然人特质)", False: "不允许在城市中出现裸体图片"}[persistent.naked_girls_in_town] text_size 18 xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "naked_girls_in_town")

            text ""

            label _("UI设置")

            # Pack ratings

            text "\n在奴隶市场或城市中显示女孩图片包等级" color c_brown italic True size 16

            if persistent.show_girlpack_rating:
                $ text1 = persistent.show_girlpack_rating
            else:
                $ text1 = "OFF"

            textbutton "显示女孩图片包等级: [text1]" text_size 18 xalign 0.0 xsize 0.8 xfill True action SetField(persistent, "show_girlpack_rating", get_next([None, "In slavemarket", "In market and city", "Everywhere"], persistent.show_girlpack_rating, loop=True))

            # Show/Hide girl status

            text "\n显示女孩状态图标" color c_brown italic True size 16

            default current_status = ""

            hbox spacing 6:
                hbox box_wrap True:
                    style_group None
                    for status in [("away", "away.webp"), ("farm", "farm.webp"), ("rest", "rest.webp"), ("scheduled", "scheduled.webp"), ("half-shift", "half.webp"), ("master bedroom", "master.webp"), ("work&whore", "ww.webp"), ("naked", "naked.webp"), ("negative fixation", "negfix.webp"), ("not naked", "not_naked.webp"), ("not work&whore", "not_ww.webp")]:

                        if status:
                            button action ToggleDict(persistent.show_girl_status, status[0]) hovered SetScreenVariable("current_status", status[0]) unhovered SetScreenVariable("current_status", ""):
                                if persistent.show_girl_status[status[0]]:
                                    add ProportionalScale("UI/status/" + status[1], 30, 30)

                                else:
                                    add im.MatrixColor(ProportionalScale("UI/status/" + status[1], 30, 30), im.matrix.desaturate())

                if current_status:
                    text "%s\n(%s)" % (setting_name_dict[current_status.capitalize()], {True : "开启", False : "关闭"}[persistent.show_girl_status[current_status]]) bold True size 14 color c_prune yalign 0.5

            # Badge settings

            text "\n女孩徽章选项" color c_brown italic True size 16
            textbutton {True: "徽章可以直接在女孩的立绘上修改", False: "徽章只能在女孩的个人资料中修改"}[persistent.badges_on_portraits] text_size 18 xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "badges_on_portraits")

            # Night events settings

            text "\n显示/跳过晚上活动消息" color c_brown italic True size 16

            for ev_type in ["Normal", "Matchmaking", "Customer", "Level/Job/Rank up", "Health/Security", "Satisfaction report", "Farm", "Rest"]:

                $ text1 = setting_name_dict[ev_type]

                if ev_type != "Satisfaction report":
                    $ text1 += "事件"

                if persistent.skipped_events[ev_type]:
                   $ text1 += ": OFF"
                else:
                   $ text1 += ": ON"

                textbutton _(text1) text_size 18 xalign 0.0 xsize 0.8 xfill True action ToggleDict(persistent.skipped_events, ev_type)

            text ""

            label _("杂项")

            # Naming options for clones

            text "\n为非原创的女孩选择命名方案" color c_brown italic True size 16

            $ switch_caption = {True: "YES", False: "NO"}

            textbutton "保留名字: %s" % switch_caption[persistent.keep_firstname] text_size 18 xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "keep_firstname")
            textbutton "保留姓氏: %s" % switch_caption[persistent.keep_lastname] text_size 18 xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "keep_lastname")
            textbutton "使用.ini名称设定(有条件时): %s" % switch_caption[persistent.gp_name_customization] text_size 18 xalign 0.0 xsize 0.8 xfill True action ToggleField(persistent, "gp_name_customization")

            # End of menu




screen debug_pics(girl):

    modal True

    default mode = "soft"
    default pic = girl.profile

    key "mouseup_3" action Return()

    use dark_filter
    use show_sex_event(pic)

    vbox xalign 1.0 xfill False:

        hbox:
            textbutton "SOFT" text_size 18 action SetScreenVariable("mode", "soft")
            textbutton "HARD" text_size 18 action SetScreenVariable("mode", "hard")
            textbutton "FARM" text_size 18 action SetScreenVariable("mode", "farm")
            textbutton "FIX" text_size 18 action SetScreenVariable("mode", "fix")

        viewport xalign 1.0 xsize 250:
            mousewheel True
            draggable True
            scrollbars "vertical"

            has vbox xalign 1.0 xfill False

            if mode == "soft":

                textbutton "头像" text_size 18 action SetScreenVariable("pic", girl.get_pic("portrait", "profile", not_tags=["naked"]))
                textbutton "头像(裸)" text_size 18 action SetScreenVariable("pic", girl.get_pic("portrait", "profile", and_tags=["naked"]))
                textbutton "立绘" text_size 18 action SetScreenVariable("pic", girl.get_pic("profile", "portrait", not_tags=["naked"]))
                textbutton "立绘(裸)" text_size 18 action SetScreenVariable("pic", girl.get_pic("profile", "portrait", and_tags=["naked"]))

                textbutton "休息" text_size 18 action SetScreenVariable("pic", girl.get_pic("rest", "profile", not_tags=["naked"], soft=True))
                textbutton "休息(裸)" text_size 18 action SetScreenVariable("pic", girl.get_pic("rest", "profile", and_tags=["naked"], soft=True))
                textbutton "服务员" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["waitress_tags"], perform_job_dict["waitress_tags2"], not_tags=["naked", "monster", "beast"], soft=True))
                textbutton "服务员(裸)" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["waitress_tags"], perform_job_dict["waitress_tags2"], and_tags=["naked"], not_tags=["monster", "beast"], soft=True))
                textbutton "舞娘" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["dancer_tags"], perform_job_dict["dancer_tags2"], not_tags=["naked", "monster", "beast"], soft=True))
                textbutton "舞娘(裸)" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["dancer_tags"], perform_job_dict["dancer_tags2"], and_tags=["naked"], not_tags=["monster", "beast"], soft=True))
                textbutton "按摩师" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["masseuse_tags"], perform_job_dict["masseuse_tags2"], not_tags=["naked", "monster", "beast"], soft=True))
                textbutton "按摩师(裸)" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["masseuse_tags"], perform_job_dict["masseuse_tags2"], and_tags=["naked"], not_tags=["monster", "beast"], soft=True))
                textbutton "艺妓" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["geisha_tags"], perform_job_dict["geisha_tags2"], not_tags=["naked", "monster", "beast"], soft=True))
                textbutton "艺妓(裸)" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["geisha_tags"], perform_job_dict["geisha_tags2"], and_tags=["naked"], not_tags=["monster", "beast"], soft=True))

                for k, tags in farm_holding_tags.items():
                    textbutton k.capitalize() text_size 18 action SetScreenVariable("pic", girl.get_pic(farm_holding_tags[k], soft=True))

            elif mode == "hard":

                textbutton "露出" text_size 18 action SetScreenVariable("pic", girl.get_pic("naked", "rest", "profile", not_tags=["monster", "beast", "machine", "group", "bisexual"]))
                textbutton "性服侍" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["service_tags"], "naked", "rest", "profile", not_tags=["monster", "beast", "machine", "group", "bisexual"]))
                textbutton "性交" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["sex_tags"], not_tags=["monster", "beast", "machine", "group", "bisexual"]))
                textbutton "肛交" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["anal_tags"], not_tags=["monster", "beast", "machine", "group", "bisexual"]))
                textbutton "皮绳愉虐" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["fetish_tags"], not_tags=["monster", "beast", "group", "bisexual"]))
                textbutton "百合 性服侍" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["bisexual_tags"], perform_job_dict["service_tags"], and_tags= ["service"], not_tags=["monster", "beast", "machine", "group"], and_priority=False))
                textbutton "百合 性交" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["bisexual_tags"], perform_job_dict["sex_tags"], and_tags= ["sex"], not_tags=["monster", "beast", "machine", "group"], and_priority=False))
                textbutton "百合 肛交" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["bisexual_tags"], perform_job_dict["anal_tags"], and_tags= ["anal"], not_tags=["monster", "beast", "machine", "group"], and_priority=False))
                textbutton "百合 皮绳愉虐" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["bisexual_tags"], perform_job_dict["fetish_tags"], and_tags= ["fetish"], not_tags=["monster", "beast", "group"], and_priority=False))
                textbutton "群交 性服侍" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["group_tags"], perform_job_dict["service_tags"], and_tags= ["service"], not_tags=["monster", "beast", "machine"], and_priority=False))
                textbutton "群交 性交" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["group_tags"], perform_job_dict["sex_tags"], and_tags= ["sex"], not_tags=["monster", "beast", "machine"], and_priority=False))
                textbutton "群交 肛交" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["group_tags"], perform_job_dict["anal_tags"], and_tags= ["anal"], not_tags=["monster", "beast", "machine"], and_priority=False))
                textbutton "群交 皮绳愉虐" text_size 18 action SetScreenVariable("pic", girl.get_pic(perform_job_dict["group_tags"], perform_job_dict["fetish_tags"], and_tags= ["fetish"], not_tags=["monster", "beast"], and_priority=False))

            elif mode == "farm":

                textbutton "种马 露出" text_size 18 action SetScreenVariable("pic", girl.get_pic("naked", and_tags = ["big"], not_tags=["monster", "beast", "machine"]))
                textbutton "种马 性服侍" text_size 18 action SetScreenVariable("pic", girl.get_pic("service", and_tags = ["big"], not_tags=["monster", "beast", "machine"]))
                textbutton "种马 性交" text_size 18 action SetScreenVariable("pic", girl.get_pic("sex", and_tags = ["big"], not_tags=["monster", "beast", "machine"]))
                textbutton "种马 肛交" text_size 18 action SetScreenVariable("pic", girl.get_pic("anal", and_tags = ["big"], not_tags=["monster", "beast", "machine"]))
                textbutton "种马 皮绳愉虐" text_size 18 action SetScreenVariable("pic", girl.get_pic("fetish", and_tags = ["big"], not_tags=["monster", "beast"]))
                textbutton "种马 百合" text_size 18 action SetScreenVariable("pic", girl.get_pic("bisexual", and_tags = ["big"], not_tags=["monster", "beast", "machine"]))
                textbutton "种马 群交" text_size 18 action SetScreenVariable("pic", girl.get_pic("group", and_tags = ["big"], not_tags=["monster", "beast", "machine"]))

                textbutton "野兽 露出" text_size 18 action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["naked"]))
                textbutton "野兽 性服侍" text_size 18 action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["service"]))
                textbutton "野兽 性交" text_size 18 action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["sex"]))
                textbutton "野兽 肛交" text_size 18 action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["anal"]))
                textbutton "野兽 皮绳愉虐" text_size 18 action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["fetish"]))
                textbutton "野兽 百合" text_size 18 action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["bisexual"]))
                textbutton "野兽 群交" text_size 18 action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["group"]))

                textbutton "怪物 露出" text_size 18 action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["naked"]))
                textbutton "怪物 性服侍" text_size 18 action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["service"]))
                textbutton "怪物 性交" text_size 18 action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["sex"]))
                textbutton "怪物 肛交" text_size 18 action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["anal"]))
                textbutton "怪物 皮绳愉虐" text_size 18 action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["fetish"]))
                textbutton "怪物 百合" text_size 18 action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["bisexual"]))
                textbutton "怪物 群交" text_size 18 action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["group"]))

                textbutton "机器 露出" text_size 18 action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["naked"]))
                textbutton "机器 性服侍" text_size 18 action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["service"]))
                textbutton "机器 性交" text_size 18 action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["sex"]))
                textbutton "机器 肛交" text_size 18 action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["anal"]))
                textbutton "机器 皮绳愉虐" text_size 18 action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["fetish"]))
                textbutton "机器 百合" text_size 18 action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["bisexual"]))
                textbutton "机器 群交" text_size 18 action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["group"]))

            elif mode == "fix":
                for fix in fix_dict.values():

                    for act in fix.acts:
                        if act != "group":
                            $ not_tags.append("group")
                        if act != "bisexual":
                            $ not_tags.append("bisexual")

                        textbutton fix.name.capitalize() + " " + act.capitalize() text_size 14 action SetScreenVariable("pic", girl.get_fix_pic(act, fix, not_tags=not_tags))


#### GIRL MIXES ####

label girlpack_menu:
    menu:
        "Girl pack mix":

            menu:
                "Would you like to see girl ratings (this may take some time if you have many girl packs)?"

                "Yes":
                    call screen girl_mix(True) nopredict
                "No":
                    call screen girl_mix(False)

        "Update packstates":
            call packstates_menu from _call_packstates_menu

        "Cancel":
            pass

    return

label girlpack_menu_restart:
    hide screen main_menu

    call girlpack_menu() from _call_girlpack_menu

    $ renpy.full_restart()

screen girl_mix(show_rating=False):

    modal True

    key "mouseup_3" action Return()

    $ shown_gp = sorted(persistent.girl_packs, key=lambda x: (-(x in persistent.girl_mix[persistent.active_mix]), x))

    frame xfill True yfill True:
        has vbox

        text "女生组合" bold True drop_shadow (1, 1) font "maturasc.TTF" xpos 6

        hbox box_wrap True:
            for mix_name in sorted(persistent.girl_mix):
                textbutton mix_name.capitalize()[:25] action (SetField(persistent, "active_mix", mix_name), SelectedIf(persistent.active_mix==mix_name)) text_size 18 text_selected_bold True
            textbutton "+" action renpy.curried_invoke_in_new_context(add_mix) text_size 18

        text "" size 12
        text "点击一个女孩的个人资料，以添加或删除这个女孩的组合.\n你可以通过点击'+'来创建一个新的组合" size 14 color c_brown xpos 6

        text "" size 12

        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            ymaximum 0.77
            yfill False

            has vbox spacing 0

            for gp in shown_gp:
                if show_rating:
                    $ rating, rtg_text = get_girlpack_rating(path=gp)

                hbox spacing 12:
                    button ysize 82 xsize 480 ymargin 0 ypadding 0:
                        if gp in persistent.girl_mix[persistent.active_mix]:
                            action RemoveFromSet(persistent.girl_mix[persistent.active_mix], gp)
                            $ cross = False
                        else:
                            idle_background None
                            action AddToSet(persistent.girl_mix[persistent.active_mix], gp)
                            $ cross = True

                        hbox spacing 12 yalign 0.5:
                            button xalign 0.0 yalign 0.5 xsize 80 background None:
                                add fast_portrait(gp, x = 70, y = 70) xalign 0.5 yalign 0.5
                                # if cross:
                                #     text "X" color c_crimson size 56 xalign 0.5 yalign 0.5
                                # else:
                                #     text "" color c_crimson size 56 xalign 0.5 yalign 0.5
                            vbox xsize 360 yalign 0.5:
                                text get_name(gp, full=True) drop_shadow (1, 1) font "maturasc.TTF" size 18
                                text "by " + creator_dict[gp] drop_shadow (1, 1) size 14 italic True
                                if show_rating:
                                    text "{size=14}评价: {/size}" + rating size 18 drop_shadow (1, 1) # drop_shadow_color c_white
                    if show_rating:
                        text rtg_text size 14 yalign 0.5 color c_darkbrown
        text "" size 14

        hbox:
            textbutton "删除组合" text_size 18:
                if persistent.active_mix != "default":
                    action renpy.curried_invoke_in_new_context(delete_mix, persistent.active_mix)
            textbutton "添加全部" action Function(add_all_to_mix, persistent.active_mix) text_size 18
            textbutton "删除全部" action Function(remove_all_from_mix, persistent.active_mix) text_size 18
            textbutton "返回" action Return() text_size 18


## ACHIEVEMENT SCREENS ##

screen achievement_notification(achievement_list, replay=False):

    zorder 99

    vbox xalign 0.5 yalign 0.5 spacing 10:
        at fadeinout
        for achievement in achievement_list:
            if replay:
                $ achv, level = achievement # Unpacking tuple
            else:
                $ achv, level = (achievement, None)

            frame xsize 320 ysize 150 xpadding 10 ypadding 10 background c_lightorange:

                has hbox yfill True spacing 12
                frame xalign 0.5 yalign 0.5:
                    add achv.pic.get(100, 100)

                vbox yalign 0.5:
                    text achv.get_title(force_level=level) xalign 0.0 size 20 bold True color c_prune # font "vivaldii.TTF"
                    text achv.get_description(force_level=level) xalign 0.0 size 20  color c_brown # font "vivaldii.TTF"
    timer 6.5 action Hide("achievement_notification")

screen achievements(main=False):

    tag menu

    default confirm_reset = False

    key "mouseup_3":
        if main:
            action ShowMenu("galleries")
        else:
            action Return()

    vbox:
        fixed ysize 160:
            frame xfill True xpadding 10 ypadding 10 background c_lightorange:
                if selected_achievement:
                    hbox yfill True spacing 12:
                        frame xalign 0.5 yalign 0.5:
                            add selected_achievement.pic.get(125, 125)

                        vbox xsize 500 yalign 0.5:
                            text selected_achievement.get_title() xalign 0.0 size 20 bold True color c_prune
                            text selected_achievement.get_description() xalign 0.0 size 20 color c_brown # font "vivaldii.TTF"

                        if selected_achievement.level < selected_achievement.level_nb:
                            vbox yalign 0.5:
                                text "下个解锁:" italic True size 20
                                text selected_achievement.get_description(_next=True) xalign 0.0 size 20 color c_brown # font "vivaldii.TTF"

            hbox xalign 1.0 yalign 0.0:

                if not confirm_reset:
                    textbutton "重置成就" text_size 14 ysize 36 xalign 0.2 yalign 1.0:
                        action SetScreenVariable("confirm_reset", True)
                else:
                    textbutton "重置成就 (%s)" % (event_color["bad"] % "CONFIRM") text_size 14 ysize 36 xalign 0.0 yalign 0.0:
                        action (Function(reset_achievements), SetScreenVariable("confirm_reset", False))

                textbutton "返回"  ysize 36:
                    if main:
                        action ShowMenu("galleries")
                    else:
                        action Return()
        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            xfill True

            frame background c_ui_darkblue:
                has hbox
                xfill True
                box_wrap True

                for achv in achievement_list:
                    if achv.level > 0:
                        textbutton achv.get_title(_button=True) xsize 150 ysize 50 text_size 12 action NullAction() hovered [SetVariable("selected_achievement", achv), SelectedIf(selected_achievement==achv)]
                    else:
                        textbutton "???" xsize 150 ysize 50



## CONTRACT SCREENS ##

init:
    transform contract_result_transform:
        alpha 0.0
        linear 0.25 alpha 1.0

screen contracts(contracts, free=False):

    frame xalign 0.5 yalign 0.5:
        has vbox

        text "选择合同" xalign 0.5 yalign 0.5 color c_brown

        text "" size 14

        hbox:
            for con in contracts:
                vbox:
                    # if not free:
                    frame xalign 0.5 xfill False yfill False:
                        text "费用: %s 金币" % str(con.base_value) size 14 color c_brown bold True
                    button action Return(con) xpadding 6 ypadding 6:
                        use contract_tab(con)

        text "" size 14

        textbutton "跳过" action Return("back") xalign 0.5 yalign 0.5

screen contract_tab(contract, x=320, active=False):

    modal True
    if active:
        use dark_filter()
        key "mouseup_3" action Return()
        use close(Return(), "back")

    frame xalign 0.5 yalign 0.5 xsize x ysize 600 xpadding 10 ypadding 10:
        viewport:
            mousewheel True
            draggable False
            scrollbars "vertical"

            has vbox spacing 12

            vbox spacing 3:
                text "" + contract.location.name drop_shadow (1, 1) font "maturasc.TTF" color c_brown
                text contract.title drop_shadow (1, 1) font "maturasc.TTF" color c_prune

            vbox spacing 3:
                add contract.location.get_pic(200, 140) insensitive_alpha 0.33 idle_alpha 0.66 hover_alpha 1.0

                text contract.description size 12 color c_brown

            # text "" size 14

            vbox spacing 6:
                text "任务" size 16 bold True color c_prune

                for tsk in contract.tasks:
                    vbox spacing 3 xpos 0.02:
                        text tsk.title size 13 bold True color c_prune
                        for req in tsk.get_requirements():
                            text req size 13 color c_brown

            vbox spacing 3:
                text "报酬要求" size 16 bold True color c_prune
                text contract.get_special_description() size 13 color c_brown

            hbox:
                text "报酬: " size 16 bold True color c_prune
                text "%s金币" % str(contract.get_value()) size 16 bold True color c_darkgold


screen pick_girl(girls, nb, contract=None):
    hbox spacing 20:
        use girl_stats(selected_girl, "postings")

        vbox:
            if contract:
                use contract_tab(contract, x=400)
            use girl_select(girls, True)
            textbutton "派出" action Return(selected_girl) xalign 0.85 ypos -0.25


screen contract_result(contract, x=450):

    default t = 0
    default earned_gold = contract.get_value()
    default displayed_gold = 0

    frame xalign 0.5 yalign 0.5 xsize x xpadding 10 ypadding 10:
        has vbox spacing 12

        vbox spacing 3:
            text "" + contract.location.name drop_shadow (1, 1) font "maturasc.TTF" color c_brown
            text contract.title drop_shadow (1, 1) font "maturasc.TTF" color c_prune

        vbox spacing 3:
            add contract.location.get_pic(200, 140) insensitive_alpha 0.33 idle_alpha 0.66 hover_alpha 1.0

            text contract.description size 12 color c_brown

        # text "" size 14

        vbox spacing 9:
            text "任务" size 16 bold True color c_prune

            for tsk in contract.tasks:
                hbox:
                    vbox xsize 320 spacing 3:
                        text tsk.title size 13 bold True color c_prune
                        for req in tsk.get_requirements():
                            text req size 13 color c_brown xpos 0.02
                    if t >= contract.tasks.index(tsk) + 1:
                        if tsk.result:
                            text str_int(tsk.value) + "金币" color c_darkgold yalign 0.5 size 13 at contract_result_transform
                        else:
                            text "{color=[c_red]}{i}失败{/i}{/color}" yalign 0.5 size 13 at contract_result_transform

        hbox:
            vbox xsize 320 spacing 3:
                text "报酬要求" size 16 bold True color c_prune
                text contract.get_special_description() size 13 color c_brown
            if t >= len(contract.tasks) + 1:
                if contract.special_bonus != 1.0:
                    text str(contract.get_special_value()) + "金币" color c_darkgold yalign 0.5 size 13 at contract_result_transform
                else:
                    text "{i}失踪{/i}" color c_lightred yalign 0.5 size 13 at contract_result_transform

        vbox spacing 6:
            text "分数" size 16 bold True color c_prune
            hbox:
                text ""
                for i in [tsk for tsk in contract.tasks if tsk.result]:
                    if t >= contract.tasks.index(i) + 1:
                        text "{image=img_star}" at contract_result_transform
                if t >= len(contract.tasks) + 1 and contract.special_bonus > 1.0:
                    text "{image=img_star}" at contract_result_transform

        hbox:
            text "报酬: " size 16 bold True color c_prune

            text "%s金币" % min(displayed_gold, earned_gold) size 16 bold True:
                if earned_gold > 0:
                    color c_darkgold
                else:
                    color c_red

        textbutton "OK" action Return() xalign 0.5

    if t < len(contract.tasks) + 1:
        timer 0.8 action [SetScreenVariable("t", t + 1), Play("sound",s_spell)] repeat True

    if displayed_gold < earned_gold:
        timer 0.1 action [SetScreenVariable("displayed_gold", round_up((1 - 0.15) * displayed_gold + 0.15 * earned_gold)), Play("sound2",s_gold)] repeat True


screen auction_brothel(name, price):

    # modal True

    tag brothel_auction

    zorder 11

    button:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20

        has vbox
        xalign 0.5
        yalign 0.5
        spacing 20

        add brothel.get_pic(320, 320) xalign 0.5
        text "出售%s给{b}%s{/b} {image=img_gold}" % (name, '{:,}'.format(price)) color c_emerald size 16 xalign 0.5 yalign 0.5


screen goal_ttip():

    frame xalign 0.5 yalign 0.5 xsize 0.5 xpadding 20 ypadding 20 background c_ui_brown:
        has vbox
        text "{image=tb goal} 你的目标" size 28 color c_darkbrown bold True
        text ""

        for cat, goal_desc in game.get_goals():
            hbox spacing 10:
                add goal_tb[cat]
                text cat size 18 bold True color goal_colors[cat] yalign 0.5
            text goal_desc size 18 color c_darkbrown
            text "" size 6

#<Chris12 PackState>
label packstates_menu :
    hide screen main_menu

    menu:
        "Welcome to the packstate feature (courtesy of {color=[c_magenta]}{b}Chris12{/b}{/color})"
        "Introduction to Packstates" :
            $ packdir = GirlFilesDict.get_packstate_directory()
            "Oftentimes, a Girlpack creator may wish to change some of the picture names to better fit Brothel King's tagging system. The packstate feature helps updating girlpacks without having to download hundreds of pictures all over again."
            "" "{b}Packstates{/b} contain all the necessary information to keep the tags of a Girlpack up to date. These files need to be put into the {color=[c_magenta]}/game/[packdir]{/color} directory and named exactly like the girlpack they are for."
            "" "During the renaming process, a {b}log file{/b} is created in the BrothelKing main directory\n({color=[c_magenta]}packstate_log.txt{/color}), showing in detail everything that was changed."
            "" "You can also do a {b}simulation{/b}. This creates the same log file, but without actually renaming any files. This lets you check which changes would be made, without any risk."
            "" "No files are actually deleted. Instead, unwanted files are tagged as {b}_TRASH{/b}. These files will not get used by BrothelKing, so you can safely just leave them there, or delete them for real. You may notice the duplicate tag on some _TRASH files - these are duplicates of existing images."
            "" "If you have added your own images, they will get tagged as {b}_UNRECOGNIZED{/b} by default. They will still get used by BrothelKing."
            "Please note that {b}duplicates{/b} only get detected for recognized images. You can change this behavior in the {b}packstates menu{/b} (Ignore will not even rename them, Hide will prevent them from showing in the game)."
            "" "That's all! Why not try a {b}simulation{/b} and see if the {color=[c_magenta]}/packstate_log.txt{/color} shows any useful changes?"
            jump packstates_menu

        "Unrecognized Images: [preferences.packstate_unrecognized]":
            menu:
                "Hide: Rename and don't show unrecognized images.\nRename: Rename unrecognized images, but show them.\nIgnore: Don't rename unrecognized images. Will also show them.\n   Removes any _UNRECOGNIZED tags again.\n(Renaming means adding _UNRECOGNIZED as tag to the filename)"
                "Hide":
                    $ preferences.packstate_unrecognized = "Hide"
                    jump packstates_menu
                "Rename":
                    $ preferences.packstate_unrecognized = "Rename"
                    jump packstates_menu
                "Ignore":
                    $ preferences.packstate_unrecognized = "Ignore"
                    jump packstates_menu
                "Back (don't change setting)":
                    jump packstates_menu

        "Simulation" :
            python:
                GirlFilesDict.import_packstates(simulate = True)
                # renpy.full_restart()

        "Apply packstate" :
            menu:
                "It is recommended that you backup your girls folder and run a simulation beforehand. There is no Undo operation!{fast}{nw}"
                "Continue" :
                    python:
                        GirlFilesDict.import_packstates(simulate = False) # if files get renamed, this will call renpy.utter_restart() on its own
                        # renpy.full_restart() # only gets called if no files are renamed
                "Back" :
                    jump packstates_menu
        "Back" :
            pass
    return
#</Chris12 PackState>


# This screen has been added for the specific needs of the Harem mod by maxxronoa

# This adds a 'Chat' button to certain trainers in the brothel screen when harem mode is activated

screen harem_button():
    textbutton "交谈" xsize 75 xalign 0.09 yalign 0.25 action Jump("harem_" + MC.current_trainer.name.lower()) hovered tt.Action("与" + MC.current_trainer.name + "交谈。")

#### END OF BK SCREENS FILE ####
