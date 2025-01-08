####            NEW SCREENS                 ####
##  Those are the screens specific to BKING   ##
##                                            ##
####                                        ####

## This script is long, redundant, and an utter mess. This is related to my severe lack of understanding of screen language in general, and especially styles. Sorry.


#### DECLARATIONS ####

image img_AP = ProportionalScale("UI/power.webp", *res_tb(16))
image img_AP_small = ProportionalScale("UI/power.webp", *res_tb(12))
image img_MP = ProportionalScale("UI/mana.webp", *res_tb(16))
image img_gold = ProportionalScale("UI/coin.webp", *res_tb(16))
image img_gold_18 = ProportionalScale("UI/coin.webp", *res_tb(18))
image img_gold_20 = ProportionalScale("UI/coin.webp", *res_tb(20))
image img_gold_24 = ProportionalScale("UI/coin.webp", *res_tb(24))
image img_star = ProportionalScale("UI/star.webp", *res_tb(16))
image img_empty_star = ProportionalScale("UI/star_empty.webp", *res_tb(16))
image img_lock = ProportionalScale("UI/lock.webp", *res_tb(80))
image img_cust = ProportionalScale("UI/customer.webp", *res_tb(22))
image img_girl = ProportionalScale(im.Crop("UI/girl_shadow.webp", (0, 0, 380, 350)), *res_tb(24))
image lines = ProportionalScale("perks/lines.webp", xres(800), yres(640))
image filter_all = ProportionalScale("UI/filters/all.webp", *res_tb(30))
image filter_weapon = ProportionalScale("UI/filters/weapon.webp", *res_tb(30))
image filter_clothing = ProportionalScale("UI/filters/clothing.webp", *res_tb(30))
image filter_trinket = ProportionalScale("UI/filters/trinket.webp", *res_tb(30))
image filter_consumable = ProportionalScale("UI/filters/consumable.webp", *res_tb(30))
image filter_misc = ProportionalScale("UI/filters/misc.webp", *res_tb(30))
image filter_all_unselect = ProportionalScale("UI/filters/all.webp", *res_tb(30), matrixcolor=SaturationMatrix(0))
image filter_weapon_unselect = ProportionalScale("UI/filters/weapon.webp", *res_tb(30), matrixcolor=SaturationMatrix(0))
image filter_clothing_unselect = ProportionalScale("UI/filters/clothing.webp", *res_tb(30), matrixcolor=SaturationMatrix(0))
image filter_trinket_unselect = ProportionalScale("UI/filters/trinket.webp", *res_tb(30), matrixcolor=SaturationMatrix(0))
image filter_consumable_unselect = ProportionalScale("UI/filters/consumable.webp", *res_tb(30), matrixcolor=SaturationMatrix(0))
image filter_misc_unselect = ProportionalScale("UI/filters/misc.webp", *res_tb(30), matrixcolor=SaturationMatrix(0))

# image filter_weapon_unselect = im.MatrixColor(ProportionalScale("UI/filters/weapon.webp", *res_tb(30)), im.matrix.desaturate())
# image filter_clothing_unselect = im.MatrixColor(ProportionalScale("UI/filters/clothing.webp", *res_tb(30)), im.matrix.desaturate())
# image filter_trinket_unselect = im.MatrixColor(ProportionalScale("UI/filters/trinket.webp", *res_tb(30)), im.matrix.desaturate())
# image filter_consumable_unselect = im.MatrixColor(ProportionalScale("UI/filters/consumable.webp", *res_tb(30)), im.matrix.desaturate())
# image filter_misc_unselect = im.MatrixColor(ProportionalScale("UI/filters/misc.webp", *res_tb(30)), im.matrix.desaturate())

image tb goal = ProportionalScale("UI/goal.webp", *res_tb(50))
image tb advance = ProportionalScale("NPC/Sill/portrait.webp", *res_tb(30))
image tb story = ProportionalScale("NPC/Kurohime/portrait.webp", *res_tb(30))
image tb other = ProportionalScale("NPC/Gio/portrait.webp", *res_tb(30))
image tb papa = ProportionalScale("NPC/Misc/freak portrait.webp", *res_tb(20))
image tb contract = ProportionalScale("NPC/Jobgirl/portrait.webp", *res_tb(30), xzoom = -1.0)

image tb rest = ProportionalScale("backgrounds/rest.webp", xres(100), yres(60))
image tb waitress = ProportionalScale("backgrounds/waitress.webp", xres(100), yres(60))
image tb dancer = ProportionalScale("backgrounds/stripper.webp", xres(100), yres(60))
image tb masseuse = ProportionalScale("backgrounds/masseuse.webp", xres(100), yres(60))
image tb geisha = ProportionalScale("backgrounds/geisha.webp", xres(100), yres(60))
image tb whore = ProportionalScale("backgrounds/whore.webp", xres(100), yres(60))
image tb farm = ProportionalScale("brothels/farm/farm.webp", xres(100), yres(60))

# image success = ProportionalScale("UI/challenges/success.webp", config.screen_width, config.screen_height)
# image failure = ProportionalScale("UI/challenges/failure.webp", config.screen_width, config.screen_height)


image girl_shadow = ProportionalScale("UI/girl_shadow.webp", *res_tb(75))

image tb wood = ProportionalScale("UI/fast buttons/wood.webp", *res_tb(40))
image tb wood grey = ProportionalScale("UI/fast buttons/wood.webp", *res_tb(40), matrixcolor=SaturationMatrix(0))
image tb leather = ProportionalScale("UI/fast buttons/leather.webp", *res_tb(40))
image tb leather grey = ProportionalScale("UI/fast buttons/leather.webp", *res_tb(40), matrixcolor=SaturationMatrix(0))
image tb dye = ProportionalScale("UI/fast buttons/dye.webp", *res_tb(40))
image tb dye grey = ProportionalScale("UI/fast buttons/dye.webp", *res_tb(40), matrixcolor=SaturationMatrix(0))
image tb silk = ProportionalScale("UI/fast buttons/silk.webp", *res_tb(40))
image tb silk grey = ProportionalScale("UI/fast buttons/silk.webp", *res_tb(40), matrixcolor=SaturationMatrix(0))
image tb marble = ProportionalScale("UI/fast buttons/marble.webp", *res_tb(40))
image tb marble grey = ProportionalScale("UI/fast buttons/marble.webp", *res_tb(40), matrixcolor=SaturationMatrix(0))
image tb ore = ProportionalScale("UI/fast buttons/ore.webp", *res_tb(40))
image tb ore grey = ProportionalScale("UI/fast buttons/ore.webp", *res_tb(40), matrixcolor=SaturationMatrix(0))
image tb diamond = ProportionalScale("UI/fast buttons/diamond.webp", *res_tb(40))
image tb diamond grey = ProportionalScale("UI/fast buttons/diamond.webp", *res_tb(40), matrixcolor=SaturationMatrix(0))

image tb renza = ProportionalScale("UI/fast buttons/renza.webp", *res_tb(40))
image tb renza grey = ProportionalScale("UI/fast buttons/renza.webp", *res_tb(40), matrixcolor=SaturationMatrix(0))
image tb captain = ProportionalScale("UI/fast buttons/captain.webp", *res_tb(40))
image tb captain grey = ProportionalScale("UI/fast buttons/captain.webp", *res_tb(40), matrixcolor=SaturationMatrix(0))

image tb banker = ProportionalScale("UI/fast buttons/banker.webp", *res_tb(40))
image tb bast = ProportionalScale("UI/fast buttons/bast.webp", *res_tb(40))
image tb giftgirl = ProportionalScale("UI/fast buttons/giftgirl.webp", *res_tb(40))
image tb gina = ProportionalScale("UI/fast buttons/gina.webp", *res_tb(40))
image tb goldie = ProportionalScale("UI/fast buttons/goldie.webp", *res_tb(40))
image tb gurigura = ProportionalScale("UI/fast buttons/gurigura.webp", *res_tb(40))
image tb katryn = ProportionalScale("UI/fast buttons/katryn.webp", *res_tb(40))
image tb papa = ProportionalScale("NPC/misc/freak portrait.webp", *res_tb(40))
image tb ramias = ProportionalScale("UI/fast buttons/ramias.webp", *res_tb(40))
image tb riche = ProportionalScale("UI/fast buttons/riche.webp", *res_tb(40))
image tb stella = ProportionalScale("UI/fast buttons/stella.webp", *res_tb(40))
image tb twins = ProportionalScale("UI/fast buttons/twins.webp", *res_tb(40))
image tb willow = ProportionalScale("UI/fast buttons/willow.webp", *res_tb(40))

image tb empty = ProportionalScale("UI/tb empty.webp", *res_tb(30))
image tb advertising = ProportionalScale("UI/tb advertising.webp", *res_tb(30))
image tb security = ProportionalScale("UI/tb security.webp", *res_tb(30))
image tb maintenance = ProportionalScale("UI/tb maintenance.webp", *res_tb(30))

image penta = ProportionalScale("UI/powers/pentagram.webp", *res_tb(100))
image magic fire = SnowBlossom("UI/powers/magic fire.webp", 100, xspeed=(-200, 200), yspeed=(-500, -1000), start=0)
image penta_fire = Crop((0, 0, yres(120), yres(120)), "magic fire")
image evil_deck_fire = Crop((0, 0, yres(160), yres(160)), "magic fire")
image evil_deck = ProportionalScale("UI/powers/evil deck.webp", *res_tb(150))
image mojo purple = ProportionalScale("UI/powers/orb_purple.webp", *res_tb(16))
image mojo green = ProportionalScale("UI/powers/orb_green.webp", *res_tb(16))
image mojo blue = ProportionalScale("UI/powers/orb_blue.webp", *res_tb(16))
image mojo red = ProportionalScale("UI/powers/orb_red.webp", *res_tb(16))
image mojo yellow = ProportionalScale("UI/powers/orb_yellow.webp", *res_tb(16))
image img_fear = ProportionalScale("UI/skull.webp", *res_tb(20))
image img_fear_x2 = ProportionalScale("UI/skull x2.webp", *res_tb(20))
image img_fear_x3 = ProportionalScale("UI/skull x3.webp", *res_tb(20))
image card_back = ProportionalScale("UI/powers/back.webp", xres(80), yres(120))
image card_front = ProportionalScale("UI/powers/front.webp", xres(80), yres(120))

image tb crystal = ProportionalScale("items/misc/misc.webp", *res_tb(18))
image misc = "items/misc/misc.webp"

image mike = Transform("NPC/Misc/Pets/pet1.webp", zoom=2.0)

image img_tavern = ProportionalScale("brothels/rooms/tavern.webp", xres(192), yres(108))
image img_strip club = ProportionalScale("brothels/rooms/strip club.webp", xres(120), yres(108))
image img_onsen = ProportionalScale("brothels/rooms/onsen.webp", xres(192), yres(108))
image img_okiya = ProportionalScale("brothels/rooms/okiya.webp", xres(192), yres(108))

## CUSTOM STYLES

init:
    # girl buttons ysize (hard-coded)
    $ girl_but_ysize = {"x4" : yres(125), "x12" : yres(100), "x24" : yres(80), "x40" : yres(60)}

    style hyperlink_text:
        hover_color c_orange
        idle_color c_pink
        hover_underline True

    style inv_no_padding: # For invisible buttons and frames
        background None
        xpadding 0
        ypadding 0
        xmargin 0
        ymargin 0

    style button:
        xpadding xres(6)
        ypadding yres(6)
        ymargin yres(2)
        idle_background Frame("darkorange_button", borders=gui.button_borders)
        selected_background Frame("orange_button", borders=gui.button_borders)
        hover_background Frame("lightblue_button", borders=gui.button_borders)
        selected_hover_background Frame("lightblue_button", borders=gui.button_borders)
        insensitive_background Frame("lightgrey_button", borders=gui.button_borders)
        activate_sound "sounds/click.ogg"

    style button_text is gui_text:
        properties gui.text_properties("button")
        # padding (xres(6), yres(3), xres(6), yres(3))
        yalign 0.5

    style contrast_button is button:
        selected_background Frame("lightblue_button", borders=gui.button_borders)

    # style contrast_button_text:
    #     idle_color c_brown

    style small_button is button:
        xpadding xres(3)
        ypadding yres(3)
        xmargin 0
        ymargin 0

    style small_button_text:
        size res_font(14)

    style girlbutton:
        idle_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_darkorange + "CC", "#000")), left=10, right=10)
        selected_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize("#298ed6CC", "#000")), left=10, right=10)
        hover_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize("#69b0e2", "#000")), left=10, right=10)

    style girlbutton_blue:
        idle_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_darkorange + "CC", "#000")), left=10, right=10)
        selected_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize("#298ed6CC", "#000")), left=10, right=10)
        hover_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize("#69b0e2", "#000")), left=10, right=10)

    style girlbutton_light:
        idle_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_ui_light, "#000")), left=10, right=10)
        selected_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_orange, "#000")), left=10, right=10)
        hover_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_lightorange, "#000")), left=10, right=10)

    style posting_button is button:
        selected_background Frame ("lightblue_button")

    style push_button:
        idle_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_lightgrey, "#000")))
        selected_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_darkpurple, "#000")))
        hover_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_softpurple, "#000")))

    style push_button_text:
        selected_color c_white
        hover_color c_white
        idle_color c_brown

    style farm_button:
        xpadding yres(18) # Using yres to maintain aspect in wide screen
        ypadding yres(9)
        idle_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_lightprune + "CC", "#000")), left=12, right=12)
        selected_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_prune, "#000")), left=12, right=12)
        hover_background Frame (
            im.MatrixColor(
                "UI/cry_box.webp",
                im.matrix.colorize(c_prune + "CC", "#000")), left=12, right=12)

    style farm_button_text:
        selected_color c_white
        hover_color c_white
        idle_color c_darkprune

## TOP OVERLAY (displays time, money, help button...)

screen tax_tooltip():
    zorder 10
    tag tax_tooltip

    if NPC_taxgirl.current_tax:
        use tax_tab()

    elif NPC_taxgirl.active:
        frame background c_ui_dark:
            xalign 0.5
            yalign 0.1

            hbox:
                spacing 10

                add ProportionalScale("NPC/taxgirl/portrait.webp", *res_tb(35)) yalign 0.5

                text "无需缴纳公会费用。" xalign 0.0 yalign 0.5 size res_font(14) color c_emerald


screen tax_tab(fade=False):
    zorder 10
    frame background c_ui_dark:

        if fade:
            at fademove([0.5, 0.5], [0.5, 0.0])
        else:
            xalign 0.5
            yalign 0.1

        hbox:

            spacing 10

            add ProportionalScale("NPC/taxgirl/portrait.webp", *res_tb(35)) yalign 0.5

            if calendar.day in (28, 7):
                $ due_date = "tomorrow"
            elif calendar.day in (1, 8):
                $ due_date = "tonight"
            elif calendar.day >= 15:
                $ due_date = "in %s days" % (29-calendar.day)
            else: # Tax due date has been extended by a week
                $ due_date = "in %s days" % (8-calendar.day)

            vbox:
                text "公会费" bold True size res_font(14)
                text "{image=img_gold} " + '{:,}'.format(round_int(NPC_taxgirl.current_tax)).replace(',', ' ') + " due %s." % due_date xalign 0.0 yalign 0.5 size res_font(14) color c_red


screen adv_tooltip():

    zorder 100

    $ ttip = GetTooltip()
    if ttip:
        nearrect:
            focus "tooltip"

            prefer_top False

            frame:
                if renpy.get_screen("home") and GetFocusRect("tooltip") and GetFocusRect("tooltip")[0] > config.screen_width - xres(150):
                    xoffset xres(-150)
                    yoffset yres(-30)
                else:
                    xoffset xres(10)
                    yoffset yres(2)
                xminimum xres(0)
                xmaximum xres(320)
                xpadding xres(10)
                ypadding yres(4)
                background c_ui_darker
                text ttip size res_font(15)


screen tool(x, y, w, h, bg = True, use_italic=False, char_limit=70, line_limit=3):

    tag ttip

    zorder 10

    $ text1 = ""

    if GetTooltip():
        use adv_tooltip()

    if tt.value != "":
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

            xmargin xres(6)
            ymargin yres(3)
            ypadding 0

            xfill True
            yfill True

            if count_lines(text1, char_limit) >= line_limit:
                add Text(text1, size= 14, justify=True, italic=use_italic) fit "contain"
            else:
                text text1 size res_font(14) xsize 1.0 justify True italic use_italic

            # if count_lines(text1, 40) <= 3:
            #     $ s = res_font(13)
            # elif count_lines(text1, 44) <= 3:
            #     $ s = res_font(12)
            # elif count_lines(text1, 50) <= 4:
            #     $ s = res_font(11)
            # elif count_lines(text1, 54) <= 4:
            #     $ s = res_font(10)
            # else:
            #     $ s = res_font(9)
            # text text1 yalign 0.0 size int(s*new_res_ratio) justify True


screen overlay(current_screen = None, kwargs=None, ttip=False):

    zorder 5

    frame:
        id "ol"

        background c_ui_dark
        xsize 1.0
        ysize int(0.075*config.screen_height)
        xpadding xres(12)
        ypadding 0

        has hbox

        xfill True
        yfill True
        yalign 0.5

        button background None xalign 0.0 yalign 0.5 action NullAction():

            tooltip ("%s\n今天是%s, 第%i年的%i月%i日" % (tl_cn(moons[calendar.month].short_description, moon_name_dict), tl_cn(calendar.get_weekday(), misc_name_dict), calendar.year, calendar.month, calendar.day))

            hbox:
                spacing xres(8)

                add moons[calendar.month].tb yalign 0.5

                null

                text "时间: 第[calendar.year]年" size res_font(18) yalign 0.5
                text "[calendar.month]月" size res_font(18) yalign 0.5
                text ("[calendar.day]日 (" + __(tl_cn(calendar.get_weekday(), misc_name_dict))[:3] + ")") size res_font(18) yalign 0.5

        hbox xalign 1.0 spacing xres(6):
            if MC.resource_tab_active:
                yalign 0.0
            else:
                yalign 0.5

            button background None xalign 0.0 yalign 0.5 action NullAction():
                tooltip "Your available gold."
                if game.chapter > 1:
                    hovered (Show("tax_tooltip", transition=Dissolve(0.15)))
                    unhovered (Hide("tax_tooltip", transition=Dissolve(0.15)))

                hbox:
                    spacing xres(6)
                    add ProportionalScale("UI/coin.webp", *res_tb(20)) yalign 0.5
                    text '{:,}'.format(round_int(MC.gold)).replace(',', ' ') xalign 0.0 yalign 0.5 size res_font(18)

            button background None xalign 0.0 yalign 0.5 tooltip __("AP: Your remaining actions for today.") action NullAction():

                has hbox

                spacing xres(3)

                add ProportionalScale("UI/power.webp", *res_tb(20)) yalign 0.5

                text str(round_int(MC.interactions)) xalign 0.0 yalign 0.5 size res_font(18)

            button background None xalign 0.0 yalign 0.5 tooltip __("MP: Your current mana.") action NullAction():

                has hbox

                spacing xres(3)

                add ProportionalScale("UI/mana.webp", *res_tb(20)) yalign 0.5

                text str(round_int(MC.mana)) xalign 0.0 yalign 0.5 size res_font(18)

        null width xres(200)

        textbutton "帮助" tooltip "Learn more about the current screen.":

            style "button"
            xalign 1.0
            yalign 0.5
            xysize res_tb(36)

            if current_screen and not slavemarket_firstvisit:
                # action renpy.curried_invoke_in_new_context(help, current_screen)
                action Call("help", scr=current_screen)

    if MC.resource_tab_active:
        use resource_tab(x=0.5, y = 0.055)

    if ttip:
        use tool(x = 0.93, y = 0.0, w = 0.32, h = 0.075, bg = False)



## GIRL TAB

screen girls(girls, context = "girls"): # context can be girls, slavemarket, farm

    tag girls

    default hovered_girl = selected_girl

    if not girls_firstvisit:
        key "mouseup_3" action (SetVariable("choice_menu_girl_interact", False), SetVariable("selected_destination", "main"), Jump("teleport"))
        use close((SetVariable("choice_menu_girl_interact", False), SetVariable("selected_destination", "main"), Jump("teleport")))
        use shortcuts()

#    if selected_girl:
#        text selected_girl.name color c_red

    use girl_tab(girls, context=context)

    if hovered_girl and hovered_girl in girls:
        use girl_stats(hovered_girl, context=context)

        use button_overlay(hovered_girl, context=context)

        use girl_profile(hovered_girl, context=context)

    elif selected_girl and selected_girl in girls:
        use girl_stats(selected_girl, context=context)

        use button_overlay(selected_girl, context=context)

        use girl_profile(selected_girl, context=context)


screen girl_tab(girls, context="girls"):

    zorder 0

    tag girl_tab

    default sort_view = "normal"

    if context == "slavemarket":

############ Jman - Headhunter Mod ############
        if game.has_active_mod("Headhunter Mod"):
            if game.headhunter_button_enabled:
                key "shift_K_h" action Jump("headhunter_main")
            $ textHH = "{u}H{/u}eadhunter" #

            $ textHH2 = "Order slaves with specific characteristics for increased cost."

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
        $ sorters = ["rank", "level", "job", "energy", "alpha", "badge"]

        if selected_girl:
            key "alt_K_UP" action [Function(move_up_list, girls, selected_girl)]
            key "alt_K_DOWN" action [Function(move_down_list, girls, selected_girl)]

    elif context == "farm":
        $ sorters = ["rank", "level", "alpha", "badge"]

    if selected_view_mode == "x40" or (selected_view_mode == "Auto" and len(girls) > 24):
        $ bsize = "x40"
        $ c = 4
        $ l = 10

    elif selected_view_mode == "x24" or (selected_view_mode == "Auto" and len(girls) > 12):
        $ bsize = "x24"
        $ c = 3
        $ l = 8

    elif selected_view_mode == "x12" or (selected_view_mode == "Auto" and len(girls) > 4):
        $ bsize = "x12"
        $ c = 2
        $ l = 6

    else:
        $ bsize = "x4"
        $ c = 1
        $ l = 4

    if len(girls) > 24:
        $ view_modes = ["x4", "x12", "x24", "x40", "Auto"]

    elif len(girls) > 12:
        $ view_modes = ["x4", "x12", "x24", "Auto"]

    elif len(girls) > 4:
        $ view_modes = ["x4", "x12", "Auto"]

    else:
        $ view_modes = ["x4", "Auto"]

    $ vp_adj.step = girl_but_ysize[bsize]
    $ y = int((girl_but_ysize[bsize]) * l)

    default lup_filter = False

    vbox:
        xalign 1.0
        ypos 0.075
        xsize xres(325)

        hbox xalign 0.1:
            if sort_view == "normal":
                use sorting_tab(context, girls, sorters)

                frame xsize yres(38) ysize yres(20) xpadding 0 ypadding 0 xmargin 0 ymargin 0:
                    textbutton "Sk." text_italic True text_color c_darkbrown text_selected_color c_emerald text_size res_font(14) xpadding 0 ypadding 0 xalign 0.5 yalign 0.6 xsize yres(38) ysize yres(20) idle_background None action SetLocalVariable("sort_view", "advanced") tooltip "Sort girls by specific skills."

                if view_modes:
                    $ _next = get_next(view_modes, selected_view_mode, True)

                    frame xsize yres(38) ysize yres(20) xpadding 0 ypadding 0 xmargin 0 ymargin 0:
                        textbutton selected_view_mode text_italic True text_color c_darkbrown text_size res_font(14) xpadding 0 ypadding 0 xalign 0.5 yalign 0.6 xsize yres(38) ysize yres(20) idle_background None:
                            action SetVariable("selected_view_mode", _next)
                            tooltip "Click to change view mode"
                
                frame xsize yres(38) ysize yres(20) xpadding 0 ypadding 0 xmargin 0 ymargin 0:
                    textbutton "L.Up" text_italic True text_color c_darkbrown text_selected_color c_emerald text_size res_font(14) xpadding 0 ypadding 0 xalign 0.5 yalign 0.6 xsize yres(38) ysize yres(20) idle_background None action ToggleLocalVariable("lup_filter"):
                        if lup_filter:
                            tooltip __("Filter girls that are ready to level up (filter ON)")
                        else:
                            tooltip __("Filter girls that are ready to level up (filter OFF)")

            
            elif sort_view == "advanced":
                use sorting_tab(context, girls, sorters = all_skills, use_stats=True, small=True)

                frame xsize yres(30) ysize yres(20) xpadding 0 ypadding 0 xmargin 0 ymargin 0:
                    textbutton "↑" text_font "1.ttf" text_italic True text_color c_darkbrown text_selected_color c_emerald text_size res_font(12) xpadding 0 ypadding 0 xalign 0.5 yalign 0.6 xsize yres(30) ysize yres(20) idle_background None action SetLocalVariable("sort_view", "normal") tooltip __("Go back to other filters.")



        frame:

            id "girl_tab"

            xmargin 3
            xpadding xres(3)
            ypadding 0
            if persistent.girls_display_mode == "pages":
                ysize y + yres(30)
            else:
                ysize y

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

                if persistent.girls_display_mode == "vp":

                    vpgrid:
                        cols c
                        allow_underfull True # necessary to avoid VPgrid crash when modifying children
                        draggable True
                        mousewheel True

                        scrollbars "vertical"

                        side_xalign 0.0
                        side_yalign 0.0
                        vscrollbar_ysize 0.98
                        vscrollbar_yalign 0.5
                        vscrollbar_xalign 1.0
                        vscrollbar_xanchor 1.0

                        xalign 1.0
                        xfill True
                        yfill True

                        spacing 0
                        yadjustment vp_adj

                        for girl in girls:
                            if not lup_filter or girl.upgrade_points >= 1 or girl.can_perk:
                                use girl_button(girl, bsize, status_list=girl_status_dict[girl], context=context, hovered_action=SetScreenVariable("hovered_girl", girl), unhovered_action=SetScreenVariable("hovered_girl", None)) id girl.fullname + str(girl.id)

                elif persistent.girls_display_mode == "pages":

                    default current_page = 1
                    default page_offset = 0 # Adds this to page numbers when there are more than 6
                    default page_button_nb = 14 # Number of tabs
                    $ nb = c*l
                    $ page_nb = round_up(len(girls) / nb)
                    $ first_girl_index = (current_page-1)*nb
                    $ last_girl_index = min((current_page)*nb, len(girls))

                    if lup_filter:
                        $ shown_girls = [g for g in girls if g.upgrade_points >= 1 or g.can_perk]
                    else:
                        $ shown_girls = girls

                    vbox:
                        fixed ysize y:
                            hbox box_wrap True spacing 0:
                                for girl in shown_girls[first_girl_index:last_girl_index]:
                                    if not lup_filter or girl.upgrade_points >= 1 or girl.can_perk:
                                        use girl_button(girl, bsize, status_list=girl_status_dict[girl], context=context, hovered_action=SetScreenVariable("hovered_girl", girl), unhovered_action=SetScreenVariable("hovered_girl", None)) id girl.fullname + str(girl.id)

                        $ start = page_offset

                        # No arrows required
                        if page_nb <= page_button_nb:
                            $ previous = None
                            $ next = None
                            $ finish = page_nb
                        # More than one set of page numbers is needed
                        else:
                            if page_offset:
                                $ previous = page_button_nb-2
                            else:
                                $ previous = None

                            if page_nb-page_offset >= page_button_nb-1:
                                $ next = page_button_nb-2
                            else:
                                $ next = None

                            if next:
                                $ finish = start + next
                            else:
                                $ finish = page_nb

                        if page_nb > 1:
                            if current_page > 1:
                                key "mousedown_4" capture True:
                                    if current_page-1 <= start and previous:
                                        action (SetLocalVariable("current_page", current_page-1), SetLocalVariable("page_offset", page_offset-previous))
                                    else:
                                        action SetLocalVariable("current_page", current_page-1)
                            if current_page < page_nb:
                                key "mousedown_5" capture True:
                                    if current_page+1 > finish and next:
                                        action (SetLocalVariable("current_page", current_page+1), SetLocalVariable("page_offset", page_offset+next))
                                    else:
                                        action SetLocalVariable("current_page", current_page+1)

                        hbox:

                            if previous:
                                textbutton "↑" style "UI_button":
                                    xalign 0.0
                                    xsize xres(22)
                                    ysize yres(22)
                                    action (SetLocalVariable("page_offset", page_offset-previous), SetLocalVariable("current_page", page_offset))
                                    text_size res_font(14)
                                    text_font "1.ttf"

                            for p in range(start, finish):
                                textbutton str(p+1) style "UI_button":
                                    xalign 0.0
                                    xsize xres(22)
                                    ysize yres(22)
                                    action SetLocalVariable("current_page", p+1)
                                    text_size res_font(14)
                                    text_selected_bold True

                                    tooltip __("Use mousewheel to cycle girls' pages.")

                            if next:
                                textbutton "↓" style "UI_button":
                                    xalign 0.0
                                    xsize xres(22)
                                    ysize yres(22)
                                    action (SetLocalVariable("page_offset", page_offset+next), SetLocalVariable("current_page", page_offset+next+1))
                                    text_size res_font(14)
                                    text_font "1.ttf"

            else:
                text _("{i}  No girl available  {/i}") size res_font(18) color c_brown


screen girl_pick_badge(girl):

    modal True
    key "mouseup_3" action Return()

    use dark_filter()

    frame xalign 0.5 yalign 0.5 xpadding 20 ypadding 20:
        has vbox

        text _("Choose a badge for [girl.fullname]") color c_darkorange

        text ""

        vpgrid xalign 0.5:
            cols 3
            spacing 5
            draggable True
            mousewheel True
            allow_underfull True

            for i in range(len(badge_pics)):
                button xsize yres(80) ysize yres(80):
                    if i == 0:
                        action (SetField(girl, "badge", ""), Return())
                        tooltip __("No badge")
                    else:
                        action (SetField(girl, "badge", badge_pics[i]), Return())
                        tooltip __("Pick this badge")
                    add ProportionalScale(badge_pics[i], *res_tb(60)) xalign 0.5 yalign 0.5


screen badge_button(girl, _size, t_size=20, active=True): # Where badge is a file name or ""
    $ badge = girl.get_badge()

    if not badge:
        if active:
            textbutton "+" xmargin 0 ymargin 0 xpadding 0 ypadding 0 background None xalign 0.9 yalign 0.1 text_size res_font(t_size) tooltip __("Add a custom badge to this girl. Custom badges do not do anything, they are for your own convenience."):
                action Return(("badge", girl))
                text_color c_white
                text_drop_shadow (1, 1)

    else:
        $ badge_name = badge.rsplit(".", 1)[0]
        button xmargin 0 ymargin 0 xpadding 0 ypadding 0 background None xalign 0.9 yalign 0.1 tooltip __("Current badge: {b}%s{/b}.\nClick to change the custom badge for this girl.") % badge_name:
            if active:
                action Return(("badge", girl))
            add ProportionalScale(badge, *res_tb(_size))


screen girl_button(girl, bsize="x4", status_list=[], context="girls", extra_action=None, custom_action=None, hovered_action=None, unhovered_action=None, custom_ttip=None):

    $ sel_col = c_emerald + "CC"
    $ use_badge = False

    if context == "girls" or context == "powers":
        if girl.job:
            $ text1 = __(girl.job.capitalize()) # text1 is displayed on the button next to girl name and portrait
            $ but_ttip = "{b}" + girl.fullname + "{/b} " + __("is a level {0} {1}.").format(__(str(girl.level)), __(girl.job))
        else:
            $ text1 = _("No job")
            $ but_ttip = "{b}" + girl.fullname + __("{/b} is resting.")
        $ text_col = job_color[girl.job]
        $ use_badge = True

    elif context == "free":
        $ text1 = girl.get_MC_relation().capitalize()
        if girl.MC_interact:
            $ but_ttip = girl.fullname + _(" is currently at the ") + girl.location + "."
        else:
            $ but_ttip = _("You haven't met this girl before.")
        $ text_col = c_white

    elif context == "farm":
        if farm.programs[girl].target != "no training":
            $ text1 = farm.programs[girl].target.capitalize()
            $ but_ttip = "{b}" + girl.fullname + _("{/b} is training (") + text1 + ")."
            $ text_col = c_orange
        else:
            $ text1 = farm.programs[girl].holding.capitalize()
            $ but_ttip = "{b}" + girl.fullname + _("{/b} is being held (") + text1 + ")."
            $ text_col = c_white
        $ use_badge = True

    elif context == "slavemarket":
        $ text1 = experienced_description[girl.sexual_experience]
        $ text2 = str(girl.get_price("buy")) + _(" gold")
        $ but_ttip = "{b}" + girl.fullname + "{/b}, " + text2 + __(". Click for details.")
        $ text_col = experienced_color[girl.sexual_experience]

    if context == "powers":
        $ text1 += "\n" + girl.get_sanity()

    if custom_ttip:
        $ but_ttip = custom_ttip

    if custom_action:
        $ but_action = custom_action
    else:
        $ but_action = [SetVariable("selected_girl", girl), SelectedIf(selected_girl==girl)]

    if extra_action: # extra_action must be a list
        $ but_action += extra_action

    if bsize == "x40":
        button:
            xsize xres(75)
            ysize girl_but_ysize[bsize]
            xalign 0.5
            yalign 0.5
            xpadding xres(3)
            ypadding yres(3)
            xmargin 0
            ymargin yres(3)
            style "girlbutton"
            action but_action
            tooltip but_ttip

            frame background None xsize yres(45) ysize yres(45) xmargin 0 ymargin 0 xpadding 2 yalign 1.0:

                has hbox yalign 0.5 xfill True yfill True

                fixed xalign 0.5 yalign 0.5:
                    add AlphaMask(girl.portrait.get(*res_tb(35)), Frame("GUI/edge_mask.png")) xalign 0.5 yalign 0.5

                    if use_badge:
                        use badge_button(girl, 20, 18, active=persistent.badges_on_portraits)

                button style "inv_no_padding" action but_action xalign 1.0 yalign 1.0:
                    if hovered_action:
                        hovered hovered_action

                    tooltip __("She has ") + str_int(girl.energy) + __(" energy left out of ") + str(int(girl.get_stat_minmax("energy")[1])) + "点"

                    vbar value girl.energy range girl.get_stat_minmax("energy")[1]:
                        thumb None
                        thumb_offset 0
                        top_gutter 0
                        left_bar Frame ("UI/cryvslider_empty.webp", 10, 0)
                        right_bar Frame ("UI/cryvslider_scale.webp", 10, 0)
                        xsize xres(6)
                        ysize yres(36)

            text text1[:3] bold True size res_font(11) color text_col drop_shadow (1, 1):
                xalign 0.05
                yalign 0.95

            hbox:
                spacing 3
                xalign 0.05

                hbox spacing 3 xalign 1.0:
                    text "阶级" size res_font(11)  drop_shadow (1, 1)
                    text rank_name[girl.rank] size res_font(14) bold True drop_shadow (1, 1)
                hbox spacing 3 xalign 1.0:
                    text "等级" size res_font(11)  drop_shadow (1, 1)
                    text str(girl.level) size res_font(14) bold True drop_shadow (1, 1)

            frame:
                background None
                xpos xres(40)
                yalign 1.0
                xmargin 1
                ymargin 2
                ypadding 0

                has vbox spacing 0 ymaximum 50 box_wrap True

                if context == "slavemarket":
                    text text2 size res_font(12) bold True

                else:
                    if len(status_list) > 3:
                        $ i = 2
                    else:
                        $ i = 3

                    for pic, ttip in status_list[:i]:
                        button style "inv_no_padding":
                            if hovered_action:
                                hovered hovered_action
                            action but_action
                            tooltip ttip
                            add ProportionalScale("UI/status/" + pic, *res_tb(16))

                    if i == 2:
                        text "..." size res_font(10) bold True xalign 0.5 yoffset -4 tooltip girl_status_dict[girl, "summary"]

    elif bsize == "x24":
        button:
            xsize xres(100)
            ysize girl_but_ysize[bsize]
            xalign 0.5
            yalign 0.5
            xpadding xres(3)
            ypadding yres(3)
            xmargin 0
            ymargin yres(3)
            style "girlbutton"
            action but_action
            tooltip but_ttip

            if hovered_action:
                hovered hovered_action
            if unhovered_action:
                unhovered unhovered_action

            frame background None xsize yres(70) ysize yres(70) xmargin 0 ymargin 0 xpadding 2 yalign 1.0:
                has hbox yalign 0.5 xfill True yfill True

                fixed xalign 0.5 yalign 0.5 fit_first True:
                    add AlphaMask(girl.portrait.get(*res_tb(55)), Frame("GUI/edge_mask.png")) xalign 0.5 yalign 0.5

                    if use_badge:
                        use badge_button(girl, 25, 20, active=persistent.badges_on_portraits)

                button style "inv_no_padding" action but_action xalign 1.0 yalign 0.5:
                    if hovered_action:
                        hovered hovered_action #! Does not work for girls that have the same exact name. Investigate.
                    # if unhovered_action:
                    #     unhovered unhovered_action
                    tooltip __("She has ") + str_int(girl.energy) + __(" energy left out of ") + str(int(girl.get_stat_minmax("energy")[1])) + "点"
                    vbar value girl.energy+1 range girl.get_stat_minmax("energy")[1]:
                        thumb None
                        thumb_offset 0
                        top_gutter 0
                        left_bar Frame ("UI/cryvslider_empty.webp", 10, 0)
                        right_bar Frame ("UI/cryvslider_scale.webp", 10, 0)
                        xsize xres(8)
                        ysize yres(42)

            text text1 bold True size res_font(12) color text_col drop_shadow (1, 1):
                xalign 0.05
                yalign 0.95

            hbox:
                spacing 3
                xalign 0.05

                hbox spacing 3 xalign 1.0:
                    text "阶级" size res_font(12)  drop_shadow (1, 1)
                    text rank_name[girl.rank] size res_font(16) bold True  drop_shadow (1, 1)
                hbox spacing 3 xalign 1.0:
                    text "等级" size res_font(12)  drop_shadow (1, 1)
                    text str(girl.level) size res_font(16) bold True  drop_shadow (1, 1)

            frame:
                background None
                xpos xres(64)
                yalign 1.0
                xmargin 1
                ymargin 2
                ypadding 0

                has vbox spacing 0 ymaximum yres(70) box_wrap True

                if context == "slavemarket":
                    text text2 size res_font(14) bold True

                else:
                    if len(status_list) > 3:
                        $ i = 2
                    else:
                        $ i = 3
                    for pic, ttip in status_list[:i]:
                        button style "inv_no_padding":
                            action but_action
                            if hovered_action:
                                hovered hovered_action
                            tooltip ttip
                            add ProportionalScale("UI/status/" + pic, *res_tb(20))

                    if i == 2:
                        text "..." size res_font(10) bold True xalign 0.5 yoffset -4 tooltip girl_status_dict[girl, "summary"]


    elif bsize == "x12":
        button:
            xsize xres(150)
            ysize girl_but_ysize[bsize]
            xalign 0.5
            yalign 0.5
            xpadding xres(6)
            ypadding yres(3)
            xmargin 0
            ymargin yres(3)
            style "girlbutton"
            action but_action
            tooltip but_ttip

            if hovered_action:
                hovered hovered_action
            if unhovered_action:
                unhovered unhovered_action

            frame background None xsize yres(90) ysize yres(90) xmargin 0 ymargin 0 yalign 1.0:
                has hbox spacing 0 yalign 0.5 xfill True yfill True

                fixed xalign 0.5 yalign 0.5 xysize res_tb(75):
                    add AlphaMask(girl.portrait.get(*res_tb(75)), Frame("GUI/edge_mask.png")) xalign 0.5 yalign 0.6

                    if use_badge:
                        use badge_button(girl, 30, 24, active=persistent.badges_on_portraits)

                button style "inv_no_padding" action but_action yalign 1.0:
                    if hovered_action:
                        hovered hovered_action
                    tooltip __("She has ") + str_int(girl.energy) + __(" energy left out of ") + str(int(girl.get_stat_minmax("energy")[1])) + "点"
                    vbar value girl.energy range girl.get_stat_minmax("energy")[1]:
                        thumb None
                        thumb_offset 0
                        top_gutter 0
                        left_bar Frame ("UI/cryvslider_empty.webp", 10, 0)
                        right_bar Frame ("UI/cryvslider_scale.webp", 10, 0)
                        xsize xres(10)
                        ysize yres(75)

            if context != "free" or girl.MC_interact:
                if len(girl.fullname) <= 10:
                    $ text3 = girl.fullname
                else:
                    $ text3 = girl.name[0] + ". " + girl.lastname
            else:
                $ text3 = "?"


            text text3 size res_font(16) drop_shadow (1, 1) font "DejaVuSans.ttf" xalign 0.05:
                if girl.original:
                    color c_yellow

            text text1 bold True size res_font(14) color text_col drop_shadow (1, 1):
                xalign 0.05
                yalign 0.95


            vbox:
                spacing 0
                xalign 0.95
                yalign 0.25

                hbox spacing 3 xalign 1.0:
                    text "阶级" size res_font(11)
                    text rank_name[girl.rank] size res_font(14) bold True drop_shadow (1, 1)
                hbox spacing 3 xalign 1.0:
                    text "等级" size res_font(11)
                    text str(girl.level) size res_font(14) bold True drop_shadow (1, 1)

            frame:
                background None
                xpos yres(100)
                yalign 1.0
                # xmargin xres(2)
                # ymargin yres(3)
                # xpadding 0
                # ypadding 0

                if context == "slavemarket":
                    text text2 size res_font(15) bold True

                else:
                    hbox spacing 1 box_wrap True xsize xres(50):

                        if len(status_list) > 4:
                            $ i = 3
                        else:
                            $ i = 4

                        for pic, ttip in status_list[:i]:
                            button style "inv_no_padding":
                                if hovered_action:
                                    hovered hovered_action
                                action but_action
                                tooltip ttip
                                add ProportionalScale("UI/status/" + pic, *res_tb(22))

                        if i == 3:
                            text "..." size res_font(11) bold True xalign 0.5 yoffset -4 tooltip girl_status_dict[girl, "summary"]


    elif bsize == "x4":
        button:
            xsize xres(300)
            ysize girl_but_ysize[bsize]
            xalign 0.5
            yalign 0.5
            xpadding xres(12)
            ypadding yres(12)
            xmargin xres(3)
            ymargin yres(3)
            style "girlbutton"
            action but_action
            tooltip but_ttip

            if hovered_action:
                hovered hovered_action
            if unhovered_action:
                unhovered unhovered_action

            fixed fit_first True:
                hbox xfill True spacing xres(12):
                    frame xsize yres(100) ysize yres(100) ymargin 3 yalign 1.0:
                        fixed fit_first True:
                            add AlphaMask(girl.portrait.get(), Frame("GUI/edge_mask.png")) yalign 0.5 fit "contain"

                        if use_badge:
                            use badge_button(girl, 40, 32, active=persistent.badges_on_portraits)

                        button style "inv_no_padding" action but_action xalign 1.0 yalign 1.0:
                            if hovered_action:
                                hovered hovered_action
                            tooltip __("She has ") + str_int(girl.energy) + __(" energy left out of ") + str(int(girl.get_stat_minmax("energy")[1])) + "点"
                            vbar value girl.energy range girl.get_stat_minmax("energy")[1]:
                                thumb None
                                thumb_offset 0
                                top_gutter 0
                                left_bar Frame ("UI/cryvslider_empty.webp", 10, 0)
                                right_bar Frame ("UI/cryvslider_scale.webp", 10, 0)
                                xsize xres(12)
                                ysize yres(85)

                    vbox xalign 0.0 ypos 0.2 xfill True xsize 0.5:
                        text text1 bold True size res_font(15) color text_col drop_shadow (1, 1) xalign 0.0

                        frame:
                            background None
                            xpadding 0
                            xalign 0.0
                            yalign 1.0
                            ymargin 3

                            has hbox

                            if context == "slavemarket":
                                text text2 size res_font(18) bold True

                            else:
                                if len(status_list) > 5:
                                    $ i = 4
                                else:
                                    $ i = 5

                                for pic, ttip in status_list[:i]:
                                    button style "inv_no_padding":
                                        if hovered_action:
                                            hovered hovered_action
                                        action but_action
                                        tooltip ttip
                                        add ProportionalScale("UI/status/" + pic, *res_tb(35))

                                if i == 4:
                                    text "..." size res_font(12) bold True xalign 0.5 yoffset -4 tooltip girl_status_dict[girl, "summary"]

                    vbox:
                        spacing 6
                        xalign 1.0
                        yalign 0.6

                        hbox spacing 6:
                            text "阶级" size res_font(14)
                            text rank_name[girl.rank] bold True drop_shadow (1, 1)
                        hbox spacing 6:
                            text "等级" size res_font(14)
                            text str(girl.level) bold True drop_shadow (1, 1)

                if context != "free" or girl.MC_interact:
                    $ text3 = girl.fullname
                else:
                    $ text3 = "?"

                text text3 drop_shadow (1, 1) font "DejaVuSans.ttf":
                    if girl.original:
                        color c_yellow


screen girl_fast_actions(girl, notebook=True, love_fear=True, schedule=True, customers=True, bg=None):

    frame:
        xalign 0.5
        ypos 1.0
        yanchor 0.0
        xminimum xres(180)
        xmaximum int(12 + config.screen_width // 2.8) # Makes it the same size as the girl profile pic
        ysize int(config.screen_height*0.0814)
        xmargin 0
        xpadding 6
        ymargin 0
        ypadding 0

        if bg:
            background bg

        has hbox spacing 5 xfill True yfill True

        if schedule:
            button yalign 0.5 xmargin 0 xpadding 3 ymargin 0 ypadding 3 action Return("sched") tooltip __("Open%s's schedule") % girl.fullname:
                at alpha_transform
                add "UI/calendar.webp" zoom 0.4 #idle_alpha 0.66 hover_alpha 1.0
        else:
            null

        if notebook:
            if MC.get_effect("special", "notebook"):
                button action Show("notebook") xmargin 0 xpadding 3 ymargin 0 ypadding 3 yalign 0.5 tooltip __("Open %s's entry in your magical notebook") % girl.fullname:
                    at alpha_transform
                    add "items/misc/magic notebook.webp" zoom 0.4 #idle_alpha 0.5 hover_alpha 1.0
        else:
            null

        if love_fear:
            hbox spacing 3 xsize xres(70) yalign 0.5: # 73
                use love_button(girl)
                use fear_button(girl)
        else:
            null
            null

        if customers and district.rank > 1:
            frame background c_ui_dark xmargin 0 xpadding 0 ymargin 0 ypadding 0 xfill False xalign 1.0 yalign 0.5:
                has hbox spacing 1 box_wrap True xmaximum xres(180) # previously 156
                for pop in all_populations:
                    if brothel.get_effect("allow", pop.name):
                        if girl.refused_populations[pop.name]:
                            $ X_text = "{b}X{/b}"
                            $ ttip = _("Click to allow ") + pop.description
                        else:
                            $ X_text = ""
                            $ ttip = _("Click to block ") + pop.description
                        button xsize xres(25) ysize yres(25) xmargin 0 xpadding 0 ymargin 0 ypadding 0 background None yalign 0.5:
                            at alpha_transform
                            action (ToggleDict(girl.refused_populations, pop.name), girl.customer_populations_safety_check(pop.name))
                            tooltip ttip
                            add pop.get_pic(*res_tb(25)) xalign 0.5 yalign 0.5
                            text X_text color c_crimson size res_font(24) xalign 0.5 yalign 0.5



screen girl_profile(girl, context = None): # context can be girls, slavemarket, farm, free

    tag girl_profile
    zorder 0

    if girl.profile != None:
        key ['K_DELETE'] action Function(toggle_ignore_pic, girl.profile)

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
                    yalign 1.0

                    text farm.programs[girl].name bold True size res_font(18) xalign 0.5 yalign 0.5 drop_shadow(1, 1)

                    # text "" size res_font(18)

                    if farm.programs[girl].target != "no training":

                        if farm.programs[girl].target in farm.knows["reaction"][girl] and farm.programs[girl].target != "auto":

                            $ reaction = girl.will_do_farm_act(farm.programs[girl].target)

                            if reaction == "accepted":
                                $ text1 = event_color["good"] % _("Gizel thinks she will accept this training without causing trouble.")
                            elif reaction == "resisted":
                                $ text1 = event_color["a little bad"] % _("Gizel thinks she will be reluctant to train this act and will take a little convincing (tough mode needed).")
                            elif reaction == "refused":
                                $ text1 = event_color["a little bad"] % _("Gizel thinks she will refuse this act unless she is beaten into submission (hardcore mode needed).")

                        else:
                            $ text1 = _("Gizel isn't sure how ") + girl.name + _(" will react to this training.")

                    else:
                        $ text1 = _("[girl.name] will never resist this.")

                    text text1 size res_font(14) italic True xalign 0.08 drop_shadow(1, 1) xsize 0.85

                    text "" size res_font(18)

                    if farm.programs[girl].target != "no training" or farm.programs[girl].holding != "rest":
                        hbox xalign 0.5 spacing xres(10):
                            textbutton "Training mode:" xsize xres(100) yalign 0.5 text_xalign 0.0 text_size res_font(14) background None text_color c_white action NullAction() tooltip "Decide if Gizel will force girls to train against their will."
                            textbutton farm.programs[girl].mode.capitalize() style "inv_no_padding" text_size res_font(14) yalign 0.5 text_bold True action NullAction() tooltip farm_ttip[farm.programs[girl].mode]

                            if farm.programs[girl].mode == "tough":
                                text "{image=img_fear}"
                            elif farm.programs[girl].mode == "hardcore":
                                text "{image=img_fear}{image=img_fear}"

                    if farm.programs[girl].target != "no training":
                        hbox xalign 0.5 spacing xres(10):
                            textbutton "Training facility:" xsize xres(100) yalign 0.5 text_xalign 0.0 text_size res_font(14) background None text_color c_white action NullAction() tooltip "Define which facility to use for her training (if any)."
                            textbutton farm.programs[girl].installation_name.capitalize() style "inv_no_padding" yalign 0.5 text_size res_font(14) text_bold True action NullAction():
                                if farm.programs[girl].installation:
                                    tooltip farm.programs[girl].installation.get_tooltip()
                                else:
                                    tooltip __("Gizel will choose an available facility automatically for her training.")

                            if farm.programs[girl].installation:
                                vbox:
                                    for mn in farm.get_minions(farm.programs[girl].installation.minion_type):
                                        button background None xalign 0.5 xpadding 0 xmargin 0 ypadding 0 ymargin 0 action NullAction() tooltip mn.get_tooltip() hovered tt.Action(mn.description):
                                            has hbox
                                            add mn.get_pic(*res_tb(20))

                                            vbox:
                                                text " " + mn.name + _(", Lv. ") + str(mn.level) size res_font(14):
                                                    if mn.hurt:
                                                        color c_red

                        if farm.knows["weakness"][girl]:
                            hbox xalign 0.5 spacing xres(10):
                                textbutton "Use Weakness:" xsize xres(100) text_xalign 0.0 text_size res_font(14) background None text_color c_white action NullAction() tooltip "Determines if Gizel will use her known weakness against her."
                                text {True: "No", False: "Yes"}[farm.programs[girl].avoid_weakness] size res_font(14) bold True

                    else:
                        hbox xalign 0.5 spacing 10:
                            textbutton "Holding mode:" xsize 0.5 xfill True text_xalign 0 text_size res_font(14) background None text_color c_white xpadding 0 xmargin 0.05 ypadding 0 ymargin 0 action NullAction() hovered tt.Action("Decide what the girl will do when not in training (work or rest).")
                            text farm.programs[girl].holding.capitalize() size res_font(14) bold True

                    # hbox xalign 0.5 spacing 10:
                    #     if farm.programs[girl].duration >= 0:
                    #         textbutton "Duration:" xsize 0.5 xfill True text_xalign 0 text_size res_font(14) background None text_color c_white xpadding 0 xmargin 0.05 ypadding 0 ymargin 0 action NullAction() hovered tt.Action("The duration of her stay.")
                    #         text str(farm.programs[girl].duration) + " days" size res_font(14) bold True

                    textbutton "Change program" text_size res_font(16) xalign 0.5 action Return(("change program", girl)) tooltip "Change " + girl.name + "'s current training program."

                    text "" size res_font(18)

            if (context == "girls" and not girls_firstvisit) or context == "free" or context == "farm":

                # if not girls_firstvisit or context == "free" or context == "farm":
                vbox xalign 0.0 yalign 0.0 spacing 6:

                    # if context == "girls":
                    #     key "d" action Return("sched")
                    #     #button background None xmargin 10 ymargin 10 xpadding 0 action Return("sched") tooltip "Open " + girl.fullname + "'s schedule (shortcut: {u}d{/u})":
                    #     button background None xmargin 10 ymargin 10 xpadding 0 action Return("sched") tooltip "Open %s's schedule (shortcut: {u}d{/u})" % girl.fullname:
                    #         add "UI/calendar.webp" zoom 0.5 idle_alpha 0.66 hover_alpha 1.0

                    if MC.get_effect("special", "notebook"):
                        key "noshift_K_n" action Show("notebook")
                        #button background None xmargin 10 xpadding 0 action Show("notebook") tooltip "Open " + girl.fullname + "'s entry in your magical notebook (shortcut: {u}n{/u})":
                        button background None xsize xres(80) ysize yres(80) xmargin 10 xpadding 0 action Show("notebook") tooltip __("Open %s's entry in your magical notebook (shortcut: {u}n{/u})") % girl.fullname:
                            at alpha_transform
                            add "items/misc/magic notebook.webp" fit "contain" # idle_alpha 0.66 hover_alpha 1.0 

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

                    textbutton "女孩评级 (" + capitalize(girl.path.split("/")[-1]) + "): " + rating background c_ui_darkblue text_size res_font(18) yalign 1.0 xmargin 10 ymargin 10 action NullAction() tooltip ttip


screen stat_bar(base_value, bonus, max_skill=100, max_cap=None, separator=50, bar_color=c_darkorange, pos_color=c_emerald, neg_color=c_crimson, color_scale=False): # All purpose stat bar, can be recolored

    # For now, proportionality using float is broken. So we use hardcoded values instead.
    default bar_xsize = xres(160)
    $ max_bar = max_skill

    if bonus > 0:
        $ bonus_offset = -xres(2) # int(max(xres(-6), xres(-base_value*50//max_skill))) # empirical
        $ max_bar = max_skill
    elif bonus < 0:
        $ bonus_offset = -xres(2) # int(max(xres(-6), xres(-(base_value+bonus)*50//max_skill))) # empirical
        $ max_bar = max_skill

    fixed fit_first True:
        fixed fit_first True xalign 1.0 xsize bar_xsize + xres(6) ypos -0.33:
            add AlphaMask(Solid(bar_color), Frame("GUI/bar/cryslider_empty.webp", left=xres(3), right=xres(3), top=0, bottom=0)) ysize yres(24)
            if color_scale: # Does not work with bonus/malus colors
                bar value base_value+bonus range max_cap thumb None left_bar Frame("GUI/bar/cryslider_scale.webp", left=xres(3), right=xres(3), top=3, bottom=3) xsize int(bar_xsize * max_cap/max_bar) + xres(4) ysize yres(24) right_bar None
            elif bonus > 0:
                add AlphaMask(Solid(bar_color), Frame("GUI/bar/cryslider_full.webp", left=xres(3), top=3, bottom=3)) xsize xres(160*base_value/max_bar + 6) ysize yres(24)

                fixed fit_first True xanchor 0.0 xoffset bonus_offset: # Don't ask me why, it works
                    xpos int(bar_xsize * base_value/max_bar)
                    xsize int(bar_xsize * bonus/max_bar) - bonus_offset
                    add AlphaMask(Solid(pos_color), Frame("GUI/bar/cryslider_full.webp", left=xres(3), right=xres(3), top=3, bottom=3)) xalign 0.0 xsize 1.0 ysize yres(24) # hover_alpha 1.0 idle_alpha 0.7
                    if base_value+bonus <= 0.8*max_bar: # Avoids visual glitch when stat is close to max
                        $ text1 = "+%i" % bonus
                    else:
                        $ text1 = "+%i\n" % bonus
                    text text1 xalign 0.5 yalign 1.0 hover_color c_white idle_color c_white + "00" size res_font(12)
            elif bonus < 0:
                add AlphaMask(Solid(bar_color), Frame("GUI/bar/cryslider_full.webp", left=xres(3), top=3, bottom=3)) xsize max(xres(160*(base_value+bonus)/max_bar + 6), 0) ysize yres(24)

                fixed fit_first True xanchor 0.0 xoffset bonus_offset: # Don't ask me why, it works
                    xpos max(int(bar_xsize * (base_value+bonus)/max_bar), 0)
                    xsize int(bar_xsize * -bonus/max_bar) - bonus_offset*3
                    add AlphaMask(Solid(neg_color), Frame("GUI/bar/cryslider_full.webp", left=xres(3), right=xres(3), top=3, bottom=3)) xalign 0.0 xsize 1.0 ysize yres(24) # idle_alpha 0.5 hover_alpha 1.0
                    if base_value <= 0.8*max_bar: # Avoids visual glitch when stat is close to max
                        text "%i" % bonus xalign 0.5 yalign 1.0 hover_color c_white idle_color c_white + "00" size res_font(12)
                    else:
                        text "%i\n" % bonus xalign 0.5 yalign 1.0 hover_color c_white idle_color c_white + "00" size res_font(12)
            else:
                add AlphaMask(Solid(bar_color), Frame("GUI/bar/cryslider_full.webp", left=xres(3), right=xres(3), top=3, bottom=3)) xsize xres(160*base_value/max_bar + 4) ysize yres(24)

        if separator:
            for x in range(max_bar//separator):
                if (x+1)*separator != max_bar:
                    text "{color=[c_brown]}I{/color}" xpos int(bar_xsize * ((x+1)*separator / max_bar)) xanchor 0.0 ypos -0.4 size res_font(10) bold True # xalign (x+1)*separator/max_skill

        if max_cap: # Adds a red bar to mark the artificial cap
            text "{color=[c_red]}I{/color}" xpos int(xres(6) + bar_xsize * max_cap/max_bar) xanchor xres(6) ypos -0.4 size res_font(24)

# screen stat_bar(base_value, bonus, max_skill=100, max_cap=None, separator=50, bar_color=c_darkorange, pos_color=c_emerald, neg_color=c_crimson, color_scale=False): # All purpose stat bar, can be recolored
#     # For now, proportionality using float is broken. So we use hardcoded values instead.
#     $ bar_xsize = xres(160)
#
#     if bonus > 0:
#         $ bonus_offset = int(max(xres(-7), xres(-base_value*50//max_skill))) # empirical
#     elif bonus < 0:
#         $ bonus_offset = int(max(xres(-7), xres(-(base_value+bonus)*50//max_skill))) # empirical
#
#     fixed fit_first True:
#         fixed fit_first True xalign 1.0 xsize bar_xsize + xres(6) ypos -0.33:
#             add AlphaMask(Solid(bar_color), Frame("GUI/bar/cryslider_empty.webp", left=6, right=6, top=3, bottom=3)) yoffset 0
#             if color_scale: # Does not work with bonus/malus colors
#                 bar value base_value+bonus range max_cap thumb None left_bar Frame("UI/cryslider_scale.webp", left=6, right=6, top=3, bottom=3) xpos xres(6) xsize int(bar_xsize * max_cap/max_skill) ysize yres(24) right_bar None
#             elif bonus > 0:
#                 add AlphaMask(Solid(bar_color), Frame("GUI/bar/cryslider_full.webp", left=xres(3), top=3, bottom=3)) xpos xres(6) xsize int(bar_xsize * base_value/max_skill) ysize yres(24)
#
#                 fixed fit_first True xanchor 0.0 xoffset bonus_offset: # Don't ask me why, it works
#                     xpos xres(6) + int(bar_xsize * base_value/max_skill)
#                     xsize int(bar_xsize * bonus/max_skill) - bonus_offset
#                     add AlphaMask(Solid(pos_color), Frame("GUI/bar/cryslider_full.webp", right=xres(3), top=3, bottom=3)) xalign 0.0 xsize 1.0 ysize yres(24) hover_alpha 1.0 idle_alpha 0.5
#                     if base_value+bonus <= 0.8*max_skill: # Avoids visual glitch when stat is close to max
#                         $ text1 = "+%i" % bonus
#                     else:
#                         $ text1 = "+%i\n" % bonus
#                     text text1 xalign 0.5 yalign 1.0 hover_color c_white idle_color c_white + "00" size res_font(12)
#             elif bonus < 0:
#                 add AlphaMask(Solid(bar_color), Frame("GUI/bar/cryslider_full.webp", left=xres(3), top=3, bottom=3)) xpos xres(6) xsize max(int(bar_xsize * (base_value+bonus)/max_skill), 0) ysize yres(24)
#
#                 fixed fit_first True xanchor 0.0 xoffset bonus_offset: # Don't ask me why, it works
#                     xpos xres(6) + max(int(bar_xsize * (base_value+bonus)/max_skill), 0)
#                     xsize int(bar_xsize * -bonus/max_skill) - bonus_offset
#                     add AlphaMask(Solid(neg_color), Frame("GUI/bar/cryslider_full.webp", right=xres(3), top=3, bottom=3)) xalign 0.0 xsize 1.0 ysize yres(24) idle_alpha 0.5 hover_alpha 1.0
#                     if base_value <= 0.8*max_skill: # Avoids visual glitch when stat is close to max
#                         text "%i" % bonus xalign 0.5 yalign 1.0 hover_color c_white idle_color c_white + "00" size res_font(12)
#                     else:
#                         text "%i\n" % bonus xalign 0.5 yalign 1.0 hover_color c_white idle_color c_white + "00" size res_font(12)
#             else:
#                 add AlphaMask(Solid(bar_color), Frame("GUI/bar/cryslider_full.webp", left=xres(3), right=xres(3), top=3, bottom=3)) xpos xres(6) xsize base_value/max_skill ysize yres(24)
#
#         if separator:
#             for x in range(max_skill//separator):
#                 if (x+1)*separator != max_skill:
#                     text "{color=[c_brown]}I{/color}" xpos xres(6) + int(bar_xsize * ((x+1)*separator / max_skill)) xanchor xres(6) ypos -0.4 size res_font(10) bold True # xalign (x+1)*separator/max_skill
#
#         if max_cap: # Adds a red bar to mark the artificial cap
#             text "{color=[c_red]}I{/color}" xpos int(xres(6) + bar_xsize * max_cap/max_skill) xanchor xres(6) ypos -0.33 size res_font(24)


# screen stat_bar(base_value, bonus, max_skill=100, max_cap=None, separator=50, bar_color=c_darkorange, pos_color=c_emerald, neg_color=c_crimson, color_scale=False): # All purpose stat bar, can be recolored
#
#     fixed fit_first True:
#         frame xalign 1.0 xsize 0.6 ypos -0.37 xpadding 0 ypadding 0:
#             background AlphaMask(Solid(bar_color), Frame("UI/cryslider_empty.webp", left=12, right=12, top=3, bottom=3))
#             hbox spacing max(xres(-7), xres(-base_value)): # Necessary to avoid glitch
#                 if color_scale: # Does not work with bonus/malus colors
#                     bar value base_value+bonus range max_cap thumb None left_bar Frame("UI/cryslider_scale.webp", left=6, right=6, top=6, bottom=6) xsize (base_value+bonus)/max_skill ysize yres(24) right_bar None
#                 elif bonus > 0:
#                     add AlphaMask(Solid(bar_color), Frame("UI/cryslider_full.webp", left=12, top=6, bottom=6)) xsize base_value/max_skill ysize yres(24)
#                     fixed fit_first True:
#                         add AlphaMask(Solid(pos_color), Frame("UI/cryslider_full.webp", right=12, top=6, bottom=6)) xsize bonus/(max_skill-base_value) ysize yres(24) idle_alpha 0.5 hover_alpha 1.0
#                         text "+%i" % bonus xalign 0.5 yalign 1.0 hover_color c_white idle_color c_white + "00" size res_font(12)
#                 elif bonus < 0:
#                     add AlphaMask(Solid(bar_color), Frame("UI/cryslider_full.webp", left=12, top=6, bottom=6)) xsize (base_value+bonus)/max_skill ysize yres(24)
#                     fixed fit_first True:
#                         add AlphaMask(Solid(neg_color), Frame("UI/cryslider_full.webp", right=12, top=6, bottom=6)) xsize -bonus/max_skill ysize yres(24) idle_alpha 0.5 hover_alpha 1.0
#                         text "%i" % bonus xalign 0.5 yalign 1.0 hover_color c_white idle_color c_white + "00" size res_font(12)
#                 else:
#                     add AlphaMask(Solid(bar_color), Frame("UI/cryslider_full.webp", left=12, right=12, top=3, bottom=3)) xsize base_value/max_skill ysize yres(24)
#
#         if separator:
#             for x in range(max_skill//separator):
#                 if (x+1)*separator != max_skill:
#                     text "{color=[c_brown]}I{/color}" xalign (x+1)*separator/max_skill xanchor 6 ypos -0.4 size res_font(10) bold True
#
#         if max_cap: # Adds a red bar to mark the artificial cap
#             text "{color=[c_red]}I{/color}" xalign max_cap/max_skill xanchor 6 ypos -0.375 size res_font(24)

screen custom_bar(labl = "Level 25", hov = None, unhov = None, val = 0, _max = 100, col = c_green, col2 = c_ui_light, x = xres(100), y = yres(6), txt_size = res_font(14)):
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
        if col:
            bar value val range _max thumb None thumb_offset 0 xfill True ysize y yalign 0.0 left_gutter 0 right_gutter 0: #top_gutter 1 bottom_gutter 0:
                # left_bar col right_bar col2
                left_bar AlphaMask(Solid(col), Frame("UI/cryslider_full.webp", left=12, right=12, bottom=0))
                right_bar AlphaMask(Solid(col2), Frame("UI/cryslider_empty.webp", left=12, right=12, bottom=0))

screen girl_stats(girl, context = "girls"): # context can be girls, slavemarket, farm, free, postings, contracts, capture, powers

    tag gst

    zorder 0

    if girl:
        frame:
            xalign 0.0

            if context not in ("postings"):
                ypos 0.1

            xmargin xres(6)
            xpadding xres(6)
            xfill True
            xsize xres(320)

            if context in ("farm", "powers"):
                background c_ui_dark
            else:
                background c_ui_darkblue

            vbox:

                spacing yres(3)

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
                        text_size res_font(20)
                        text_font "DejaVuSans.ttf"

                        if context == "girls":
                            action (SetVariable("selected_girl", girl), Return("change_name"))
                            tooltip __("Click to change her name")

                        elif context == "farm":
                            action Return(("change_name", girl))
                            tooltip __("Click to change her name")

                        xmargin 0
                        ymargin 0
                        xpadding xres(3)
                        ypadding 0


                    if context in ("girls", "farm"):

                        frame:

                            background None
                            xmargin 0
                            ymargin 0
                            xpadding 0
                            ypadding 0
                            xalign 1.0
                            yalign 1.0
                            xfill False

                            has hbox

                            spacing xres(6)
                            xfill False

                            # Add defense meter

                            $ defense = girl.get_defense()

                            if defense <= 0:
                                    $ ttip = __("{b}Helpless")
                            elif defense <= 3:
                                $ ttip = __("{b}Mostly harmless")
                            elif defense <= 6:
                                $ ttip = __("{b}Competent")
                            elif defense <= 9:
                                $ ttip = __("{b}Dangerous")
                            else:
                                $ ttip = __("{b}Deadly")

                            $ ttip += __("{/b}\nHow well she can defend herself. Raise this by giving her a weapon.")

                            button:

                                xmargin 0
                                ymargin 0
                                xpadding 0
                                ypadding 0
                                xsize yres(20)
                                ysize yres(20)
                                xalign 0.0
                                yalign 1.0
                                background None

                                action NullAction()
                                tooltip ttip

                                add ProportionalScale("UI/defense.webp", *res_tb(20)) xalign 0.5 yalign 0.5

                                text str(round_int(defense)) size res_font(12) xalign 0.5 yalign 0.5 color c_white


                            button background None action NullAction() hovered (Show("mood_details", girl=girl, transition=Dissolve(0.15)), tt.Action(girl.get_mood_description("mood"))) unhovered Hide("mood_details", transition=Dissolve(0.15)):

                                xalign 0.0
                                yalign 0.7
                                xmargin 0
                                ymargin 0
                                xpadding 0
                                ypadding 0

                                add ProportionalScale(girl.get_mood_picture(), *res_tb(16))

                    elif context == "powers":
                        text _("Sanity: ") + girl.get_sanity() size res_font(16)


                if context in ["girls", "farm", "contract", "postings", "powers"]:

                    ## Levels and rank info

                    button style "inv_no_padding":

                        xalign 0.0

                        if debug_mode:
                            action Function(girl.rank_up, forced = True)
                        else:
                            action NullAction()
                        hovered Show("rank_level_details", girl = girl, transition=Dissolve(0.15))
                        unhovered Hide("rank_level_details", transition=Dissolve(0.15))

                        has hbox
                        xfill True
                        spacing xres(6)

                        #Rank

                        $ rank_text = __("Rank ") + rank_name[girl.rank]

        #                $ rank_ttip = "Reputation: " + str(round_int(girl.rep)) + "/" + str(girl.get_rep_cap())

        #                if girl.rank >= str(district.rank):

        #                    $ rank_ttip += "{b}Max rank reached.{/b}\n"

        #                $ rank_ttip += "\nRank affects many aspects of the game, including maximum level and skill values."

                        use custom_bar(labl = rank_text, val = (girl.rep - rep_to_rank[girl.rank - 1]), _max = (girl.get_rep_cap() - rep_to_rank[girl.rank - 1]), col = c_softpurple, x = xres(70), y=yres(10))


                        #Level

                        $ level_text = __("Level ") + str(girl.level)

                        use custom_bar(labl = level_text, val = (girl.xp - xp_to_levelup[girl.level - 1]), _max = (girl.get_xp_cap() - xp_to_levelup[girl.level - 1]), col = c_lightgreen, x = xres(70), y=yres(10))


                        #JP

                        $ jp_show = False

                        if girl.away:
                            if girl.job in all_jobs:
                                $ job = girl.job
                                $ jp_show = True
                            $ jp_text = _("Away")

                        elif girl.hurt > 0:
                            if girl.job in all_jobs:
                                $ job = girl.job
                                $ jp_show = True
                            $ jp_text = _("Hurt (%id)") % int(girl.hurt)

                        elif girl.workdays[calendar.get_weekday()] == 0:
                            if girl.job in all_jobs:
                                $ job = girl.job
                                $ jp_show = True
                            $ jp_text = _("Resting")

                        elif girl.resting or not girl.job:
                            $ jp_text = _("Resting")

                        elif girl.job in all_jobs:
                            $ job = girl.job
                            $ jp_show = True

                        elif girl in farm.girls:
                            if farm.programs[girl].target == "no training":
                                if farm.programs[girl].holding == "rest":
                                    $ jp_text = _("Resting")
                                else:
                                    $ jp_text = _("Holding")
                            else:
                                $ jp_text = _("Training")

                        else: # Whore
                            $ job = None

                            $ best = -1
                            for act in all_sex_acts:
                                if girl.jp[act] > best and girl.does[act]:
                                    $ best = girl.jp[act]
                                    $ job = act
                                    $ jp_show = True

                        if jp_show:
                            $ jp_text = __(job.capitalize()) + " " + str(girl.job_level[job]) + " {image=img_star}"

                            $ jp_val = girl.jp[job]
                            $ jp_max = girl.get_jp_cap(job)
                            $ jp_col = c_orange

                            use custom_bar(labl = jp_text, val = (jp_val - jp_to_level[girl.job_level[job] - 1]), _max = (jp_max - jp_to_level[girl.job_level[job] - 1]), col = jp_col, x=xres(70), y=yres(10))

                        else:
                            use custom_bar(labl = jp_text, val = 0, _max = 0, col = None, col2 = None)


                if context != "capture":
                    null height yres(30)


                ## SKILLS LISTING

                text "主要属性" size res_font(18)

                vbox:
                    spacing 0

                    if context != "free" or girl.MC_relationship_level >= 1:

                        for stat in girl.stats:

                            $ total_value = girl.get_stat(stat.name)
                            $ maxrange = max(girl.get_stat_minmax(stat.name)[1], girl.rank*50)

                            if total_value > round_int(stat.value):
                                $ col = "good"
                            elif total_value < round_int(stat.value):
                                $ col = "bad"
                            else:
                                $ col = "normal"

                            button focus stat.name:
                                background None
                                if debug_mode:
                                    action Return(("debug change stat", stat))
                                else:
                                    action NullAction()
                                tooltip stat.get_description(total_value, girl.get_stat_minmax(stat.name)[1])
                                keyboard_focus False
                                yfill False
                                ysize yres(30)

                                if debug_mode:
                                    hovered tt.Action("value: %i, total_value: %i, bonus: %i, maxrange: %i" % (stat.value, total_value, total_value-round_int(stat.value), maxrange))

                                hbox:
                                    spacing 6
                                    use stat_bar(stat.value, total_value-round_int(stat.value), maxrange) id "bar_" + stat.name
                                    text stat_name_dict[stat.name] bold True layout "nobreak" size res_font(14) xpos 0.0 ypos -0.05 idle_color c_white + "CC"
                                text event_color[col] % ("%s/%s" % (str_int(total_value), girl.get_stat_minmax(stat.name)[1])) size res_font(12) yalign 0.1 xanchor 1.0 idle_color c_white + "CC" drop_shadow (1, 1):
                                    xpos 0.525

                        # Energy bar

                        $ girl_max = girl.get_stat_minmax("energy")[1]
                        $ rank_max = 50+50*girl.rank

                        if girl_max > rank_max:
                            $ rank_max = girl_max

                        button:
                            background None
                            if debug_mode:
                                action Return(("debug change all stats", 0))
                            else:
                                action NullAction()
                            tooltip __("She has {b}") + str_int(girl.energy) + __("{/b} energy remaining. Her maximum energy is {b}") + str_int(girl_max) + __("{/b} (increase constitution for higher energy).")
                            keyboard_focus False
                            yfill False
                            ysize yres(30)

                            hbox:
                                spacing 6
                                use stat_bar(girl.energy, bonus=0, max_skill=rank_max, max_cap=girl_max, color_scale=True, separator=False)  id "bar_energy"
                                text stat_name_dict["Energy"] bold True size res_font(14) xpos 0.0 ypos -0.05 idle_color c_white + "CC"

                            text "%s/%s" % (int(girl.energy), int(girl_max)) size res_font(12) yalign 0.1 xanchor 1.0 idle_color c_white + "CC":
                                xpos 0.525

                    else:
                        for stat in girl.stats[:4]:

                            $ total_value = girl.get_stat(stat.name)
                            $ maxrange = max(girl.get_stat_minmax(stat.name)[1], girl.rank*50)

                            if total_value > stat.value:
                                $ col = "good"
                            elif total_value < stat.value:
                                $ col = "bad"
                            else:
                                $ col = "normal"

                            button:
                                background None
                                action NullAction()
                                tooltip stat.get_description(total_value, girl.get_stat_minmax(stat.name)[1])
                                keyboard_focus False
                                ysize yres(30)

                                hbox:
                                    spacing 6

                                    use stat_bar(total_value, 0, maxrange) id "bar_" + stat.name
                                    text stat_name_dict[stat.name] bold True layout "nobreak" size res_font(14) xpos 0.0 ypos -0.05 idle_color c_white + "CC"
                                text event_color[col] % ("%s/%s" % (str_int(total_value), girl.get_stat_minmax(stat.name)[1])) size res_font(12) yalign 0.1 xanchor 1.0 idle_color c_white + "CC" drop_shadow (1, 1):
                                    xpos 0.525

                        for stat in girl.stats[4:]:
                            button:
                                background None
                                action NullAction()
                                tooltip __("You need to become her friend to see her level for this skill.")
                                keyboard_focus False
                                ysize yres(30)

                                fixed fit_first True:

                                    hbox:
                                        spacing 6

                                        use stat_bar(0, 0, 50) id "bar_" + stat.name
                                        text stat_name_dict[stat.name] bold True layout "nobreak" size res_font(14) xpos 0.0 ypos -0.05 idle_color c_white + "CC"

                                    text "???" xpos 75 size res_font(14)




                    # text "" size res_font(6)

                hbox spacing 14:
                    textbutton "性技能" style "inv_no_padding" text_size res_font(18) yalign 0.0 action NullAction() hovered Show("sex_details", girl=girl) unhovered Hide("sex_details")

                    for act in ("group", "bisexual"):

                        if girl.does[act]:
                            $ text1 = "{b}✓{/b}"
                        else:
                            $ text1 = ""

                        if girl.has_perk(act.capitalize()):

                            button xpadding 0 ypadding 0 xmargin 0 ymargin 0 yalign 1.0 background None action NullAction() hovered Show("sex_details", girl=girl) unhovered Hide("sex_details"):
                                hbox spacing 5:
                                    textbutton text1:
                                        text_font "1.ttf"
                                        text_size res_font(12)
                                        xsize yres(35)
                                        ysize yres(20)
                                        ypos -0.1
                                        if not girls_firstvisit:
                                            action (SetVariable("selected_girl", girl), SetVariable("selected_sex_act", act), Return("sex_act"))

                                        hovered (tt.Action(_("This will activate {b}") + act + _(" acts{/b} for this girl. At least one regular sex act muct be active as well.")), Show("sex_details", girl=girl))
                                        unhovered Hide("sex_details")
                                    text __(act.capitalize()) layout "nobreak": #preference_color[pref] % stat.name:
                                        size res_font(12)

                if context == "slavemarket":
                    $ ttip = __(experienced_description[girl.sexual_experience + " ttip"]) + __(" Prior training may make a girl more suitable for sex acts.")
                    textbutton __("Prior training received:   {color=") + experienced_color[girl.sexual_experience] + "}" + __(experienced_description[girl.sexual_experience]) + "{/color}" ymargin yres(3) ypadding 0 text_color c_white text_size res_font(14) background None action NullAction() tooltip ttip


                vbox:
                    spacing 0

                    if context != "free" or girl.MC_relationship_level >= 4:

                        for stat in girl.sex_stats:

                            $ total_value = girl.get_stat(stat.name)
                            $ maxrange = max(girl.get_stat_minmax(stat.name)[1], girl.rank*50)

                            if total_value > round_int(stat.value):
                                $ col = "good"
                            elif total_value < round_int(stat.value):
                                $ col = "bad"
                            else:
                                $ col = "normal"

                            button:
                                background None
                                if debug_mode:
                                    action Return(("debug change stat", stat))
                                else:
                                    action NullAction()
                                hovered Show("sex_details", girl=girl)
                                unhovered Hide("sex_details")
                                tooltip stat.get_description(total_value, girl.get_stat_minmax(stat.name)[1]) # stat.get_description(total_value, maxrange)
                                keyboard_focus False
                                ysize yres(30)

                                hbox:

                                    spacing 6

                                    use stat_bar(stat.value, total_value-round_int(stat.value), maxrange) id "bar_" + stat.name
                                    # use stat_bar(total_value, total_value - stat.value, maxrange)

                                    if context == "girls":

                                        if girl.does[stat.name.lower()]:
                                            $ text1 = "✓"
                                        else:
                                            $ text1 = ""

                                        $ result, reason = girl.will_do_sex_act(stat.name.lower(), True)

                                        if result:
                                            $ ttip = __("This will activate {b}") + __(stat_name_dict[stat.name]) + __("{/b} for this girl.")
                                        else:
                                            $ ttip = reason

                                        button xpadding 0 ypadding 0 xmargin 0 ymargin 0 background None action NullAction() hovered (Show("sex_details", girl=girl)) unhovered Hide("sex_details"):
                                            tooltip ttip
                                            textbutton text1:
                                                text_font "1.ttf"
                                                text_size res_font(12)
                                                xsize int(config.screen_height*0.0341)
                                                ysize yres(20)
                                                ypos -0.1
                                                if not girls_firstvisit and result:
                                                    action (SetVariable("selected_girl", girl), SetVariable("selected_sex_act", stat.name), Return("sex_act"))

                                                hovered (Show("sex_details", girl=girl))
                                                unhovered Hide("sex_details")
                                                tooltip ttip

                                    $ pref = girl.get_preference(stat.name)

                                    text stat_name_dict[stat.name] bold True layout "nobreak" size res_font(14) xpos 0.0 ypos -0.05 idle_color c_white + "CC"

                                text event_color[col] % ("%s/%s" % (str_int(total_value), girl.get_stat_minmax(stat.name)[1])) size res_font(12) yalign 0.1 xanchor 1.0 idle_color c_white + "CC" drop_shadow (1, 1):
                                    xpos 0.525

                    else:
                        for stat in girl.sex_stats:
                            button:
                                background None
                                action NullAction()
                                tooltip __("You need to become her lover to see her level for this skill.")
                                keyboard_focus False
                                ysize yres(30)

                                fixed fit_first True:

                                    hbox:
                                        spacing 6

                                        use stat_bar(0, 0, 50) id "bar_" + stat.name
                                        text stat_name_dict[stat.name] bold True size res_font(14) xpos 0.0 ypos -0.05 idle_color c_white + "CC"

                                    text "???" xpos 75 size res_font(14)

                    # text "" size res_font(3)


                ## TRAITS LIST ##
                textbutton "特质" text_color c_white text_size res_font(18) background None xpadding 0 ypadding 0 xmargin 0 ymargin 0:
                    action NullAction()
                    if context != "free" or girl.MC_relationship_level >= 3:
                        hovered Show("trait_details", girl=girl)
                        unhovered Hide("trait_details")

                viewport:
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    if len(girl.traits) > 3 or sum(len(t.name) for t in girl.traits) >= 27:
                        ysize yres(36)
                    else:
                        ysize yres(22)

                    if context != "free" or girl.MC_relationship_level >= 3:
                        hbox spacing xres(10) box_wrap True:
                            for trait in girl.traits:

                                $ ttip = trait.get_description(context)

                                textbutton trait.name:

                                    style "inv_no_padding"
                                    xalign 0.0
                                    yalign 0.5
                                    text_size res_font(14)
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
                            text_size res_font(14)
                            action NullAction()
                            tooltip __("You need to become her boyfriend to see her traits.")
                            keyboard_focus False

                if context == "girls":
                    text "" size res_font(3)

                    hbox spacing xres(10):
                        text _("Upkeep: ") size res_font(18)
                        text "{image=img_gold} %s" % str(round_int(girl.upkeep)):
                            size res_font(14)
                            yalign 1.0
                            if girl.get_upkeep_modifier() < 0:
                                color c_red

                            elif girl.get_upkeep_modifier() == 0:
                                color c_white

                            else:
                                color c_emerald


                    if girl.locked_upkeep:
                        text _("Her upkeep is currently withdrawn.") size res_font(14) italic True

                    else:
                        key "noshift_K_a" action (ToggleField(girl, "auto_upkeep"), SetField(girl, "upkeep_ratio", (girl.upkeep - girl.get_med_upkeep())/girl.rank), Play("sound", s_click))

                        hbox:
                            spacing xres(2)

                            $ minrange = girl.get_med_upkeep() // 4
                            $ maxrange = girl.get_med_upkeep() + 11 * girl.rank * 2 ** girl.rank # Simplify at some point

                            text "" size res_font(14)

                            bar style "slider" value FieldValue(girl, "upkeep", range=maxrange-minrange, offset=minrange, action=Function(girl.update_upkeep_ratio)):
                                if girl.get_upkeep_modifier() < 0:
                                    left_bar Frame("red_bar_left", gui.bar_borders, tile=gui.bar_tile)

                                elif girl.get_upkeep_modifier() == 0:
                                    left_bar Frame("lightorange_bar_left", gui.bar_borders, tile=gui.bar_tile)

                                else:
                                    left_bar Frame("green_bar_left", gui.bar_borders, tile=gui.bar_tile)

                                xsize 0.45
                                yalign 0.5
                                keyboard_focus False
                                tooltip __("You must pay upkeep every day. Higher-end girls will require higher upkeep. Keep it high to keep your girl happy.")

                            textbutton "-":
                                style "small_button"
                                xsize xres(25)
                                yalign 0.5
                                if girl.upkeep > minrange:
                                    action (SetField(girl, "upkeep", girl.upkeep-1), Function(girl.update_upkeep_ratio), Play("sound", s_click))
                                tooltip (_("Decrease her upkeep."))

                            textbutton "+":
                                style "small_button"
                                xsize xres(25)
                                yalign 0.5
                                if girl.upkeep < maxrange:
                                    action (SetField(girl, "upkeep", girl.upkeep+1), Function(girl.update_upkeep_ratio), Play("sound", s_click))
                                tooltip (_("Increase her upkeep."))

                            if girl.auto_upkeep:
                                $ text1 = __("Auto upkeep setting is {b}{color=[c_green]}on{/color}{/b} {i}(shortcut: {u}Shift+a{/u}){/i}")
                            else:
                                $ text1 = __("Auto upkeep setting is {b}{color=[c_red]}off{/color}{/b} {i}(shortcut: {u}Shift+a{/u}){/i}")

                            textbutton "自动":
                                if girl.auto_upkeep:
                                    text_bold True
                                    background Frame("lightblue_button", borders=gui.button_borders)

                                style "small_button"
                                xsize xres(25)
                                yalign 0.5
                                action (ToggleField(girl, "auto_upkeep"), SetField(girl, "upkeep_ratio", (girl.upkeep - girl.get_med_upkeep())/girl.rank), Play("sound", s_click))
                                tooltip "{size=+2}" + text1 + __("\nWhen this is turned on, current upkeep balance will 'lock', and upkeep will rise and fall automatically.") + "{/size=+2}"

                elif context == "farm":
                    text "" size res_font(3)
                    text _("Upkeep") size res_font(18)

                    hbox:
                        spacing 2

                        text "" size res_font(14)

                        text str(girl.get_med_upkeep() // 4) + _(" gold (fixed)") size res_font(14)


screen assign_job(girl):

    modal True
    tag assign_job

    key "mouseup_3" action (Return("cancel"))

    key "K_1" action (Return("rest"))
    key "K_2" action (Return("waitress"))
    key "K_3" action (Return("dancer"))
    key "K_4" action (Return("masseuse"))
    key "K_5" action (Return("geisha"))
    key "K_6" action (Return("whore"))
    if farm.active:
        key "K_7" action (Return("farm"))
    if brothel.master_bedroom.level >= 1:
        key "K_8" action (Return("master bedroom"))

    frame ypos 0.25 xfill False:

        grid 4 2:
            # xsize xres(450)
            xspacing xres(3)
            yspacing yres(3)

            button background None xpadding 2 ypadding 2:
                action Return("rest")
                tooltip __("Tell ") + girl.fullname + __(" to get some rest.")
                at alpha_transform
                fixed fit_first True:
                    add "tb rest" xalign 0.5 yalign 0.5 # alpha 0.6 hover_alpha 1.0 selected_hover_alpha 1.0 selected_idle_alpha 1.0
                    text _("Rest") selected_color c_green hover_bold True xalign 0.5 yalign 0.5 drop_shadow (1, 1) size res_font(14)
                    text "1" size res_font(12) xalign 0.05 yalign 0.95 drop_shadow (1, 1)

            for j in all_jobs + ["whore"]:
                button background None xpadding 2 ypadding 2 xalign 0:
                    if brothel.has_room(job_room_dict[j]):
                        action Return(j)
                        tooltip __("Ask ") + girl.fullname + __(" to work as a ") + __(j)
                        at alpha_transform
                        fixed fit_first True:
                            add "tb " + j xalign 0.5 yalign 0.5 # idle_alpha 0.66 selected_hover_alpha 1.0 selected_idle_alpha 1.0 hover_alpha 1.0
                            text __(j.capitalize()) selected_color c_yellow hover_bold True xalign 0.5 yalign 0.5 drop_shadow (1, 1) size res_font(14)
                            if j == "whore":
                                $ text1 = "6"
                            else:
                                $ text1 = str(all_jobs.index(j)+2)
                            text text1 size res_font(12) xalign 0.05 yalign 0.95 drop_shadow (1, 1)

                    else:
                        text __(j.capitalize()) + __("\n(unavailable)") selected_bold True xalign 0.5 yalign 0.5 drop_shadow (1, 1) size res_font(14)


            if farm.active:
                button background None xpadding 2 ypadding 2 xpos 0:
#                     selected girl.job=="farm" # What was this?
                    action Return("farm")
                    tooltip __("Send ") + girl.fullname + __(" to the farm.")
                    at alpha_transform
                    fixed fit_first True:
                        add "tb farm" xalign 0.5 yalign 0.5 # idle_alpha 0.66 selected_hover_alpha 1.0 selected_idle_alpha 1.0 hover_alpha 1.0
                        text _("Farm") selected_color c_green hover_bold True xalign 0.5 yalign 0.5 drop_shadow (1, 1) size res_font(14)
                        text "7" size res_font(12) xalign 0.05 yalign 0.95 drop_shadow (1, 1)
            else:
                null

            if brothel.master_bedroom.level >= 1:
                $ text1 = _("Auto-train ")
                if girl in brothel.master_bedroom.girls:
                    $ ttip = __("Remove ") + girl.fullname + __(" from your bedroom.")
                    $ text1 += _("(ON)")
                else:
                    $ ttip = __("Add ") + girl.fullname + __(" to your bedroom.")
                    $ text1 += _("(OFF)")

                button background None xpadding 2 ypadding 2 xpos 0:
                    action Return("master bedroom")
                    tooltip ttip
                    at alpha_transform
                    fixed fit_first True:
                        add brothel.master_bedroom.get_pic(xres(100), yres(60)) xalign 0.5 yalign 0.5 # idle_alpha 0.66 selected_hover_alpha 1.0 selected_idle_alpha 1.0 hover_alpha 1.0
                        text text1 selected_color c_green hover_bold True xalign 0.5 yalign 0.5 drop_shadow (1, 1) size res_font(14) text_align 0.5
                        text "8" size res_font(12) xalign 0.05 yalign 0.95 drop_shadow (1, 1)
            else:
                null





screen girl_stats_light(girl, x=0.5, y=0.85, panel="left"): # Used to display a condensed summary of a girl's stat and show the impact of item changes

    zorder 6

    if isinstance(girl, Girl):
        frame xalign x yalign y xsize xres(450) xpadding 10 ypadding 10:
            has vbox xfill True
            hbox spacing xres(48):
                if panel == "left":
                    xalign 0.0
                elif panel == "right":
                    xalign 1.0

                if panel == "left":
                    text "⟸" font "1.ttf" color c_darkorange bold True
                text girl.fullname color c_darkorange bold True
                if panel == "right":
                    text "⟹" font "1.ttf" color c_darkorange

            hbox spacing 10 xalign 0.5:
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

                        text stat_name_dict[stat.name] size res_font(13) bold True:
                            if change:
                                color c_darkorange
                            else:
                                color c_brown

                        text str_int(girl.get_stat(stat.name)) size res_font(14) color c_brown xalign 1.0:
                            if change:
                                bold True

                        if change:
                            text "  {font=1.ttf}➔{/font}  " + str_int(girl.get_stat(stat.name) + change) size res_font(14) bold True:
                                if change >= 0:
                                    color c_emerald
                                else:
                                    color c_red
                        else:
                            null

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

                        text stat_name_dict[stat.name] size res_font(13) bold True yalign 0.5:
                            if change:
                                color c_darkorange
                            else:
                                color c_brown
                        text str_int(girl.get_stat(stat.name)) size res_font(14) color c_brown xalign 1.0:
                            if change:
                                bold True

                        if change:
                            text "  {font=1.ttf}➔{/font}  " + str_int(girl.get_stat(stat.name) + change) size res_font(14):
                                if change > 0:
                                    color c_emerald
                                else:
                                    color c_red
                        else:
                            text "" size res_font(14)

                    text "" size res_font(14)
                    text "" size res_font(14)
                    text "" size res_font(14)

                    $ change = 0
                    if selected_item:
                        if selected_item.equipped:
                            $ change = -round_int(girl.get_effect("boost", selected_item.type.name.lower()) * (selected_item.get_effect("change", "defense") + (1 - selected_item.get_effect("boost", "defense"))*girl.get_stat("defense")))
                        else:
                            $ change = round_int(girl.get_effect("boost", selected_item.type.name.lower()) * (selected_item.get_effect("change", "defense") + (1 - selected_item.get_effect("boost", "defense"))*girl.get_stat("defense")))

                            for it in girl.equipped:
                                if it.slot == selected_item.slot:
                                    $ change -= round_int(girl.get_effect("boost", it.type.name.lower()) * (it.get_effect("change", "defense") + (1 - it.get_effect("boost", "defense"))*girl.get_stat("defense")))

                    text __("Defense") size res_font(13) color c_brown:
                        if change:
                            bold True
                    text str_int(girl.get_defense()) size res_font(14) color c_brown xalign 1.0:
                        if change:
                            bold True

                    if change:
                        text " -> " + str_int(girl.get_stat("defense") + change) size res_font(14):
                            if change > 0:
                                color c_emerald
                            else:
                                color c_red

                    else:
                        text "" size res_font(14)

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
                    text stat_name_dict["Energy"] size res_font(13) color c_brown:
                        if change:
                            bold True
                    text str_int(girl.energy) size res_font(14) color c_brown xalign 1.0:
                        if change:
                            bold True
                    if change:
                        if girl.energy + change > girl.get_stat_minmax("energy")[1]:
                            $ change = girl.get_stat_minmax("energy")[1] - girl.energy
                        text " -> " + str_int(girl.energy + change) size res_font(14):
                            if change > 0:
                                color c_emerald
                            else:
                                color c_red
                    else:
                        text "" size res_font(14)



screen button_overlay(girl, context="girls"):

    zorder 5

    if context == "slavemarket":

        frame:

            xalign 0.0
            xmargin 0.1
            xsize 0.3
            xfill True
            ypos 0.14
            background None

            has hbox

            xfill True

            $ text1 = str(girl.get_price('buy')) + " gold"

            text text1 xalign 0.0

            key "noshift_K_y" action Return(girl)

            textbutton "购买" xsize xres(60) text_size res_font(22) xalign 1.0 action Return(girl) tooltip __("Click to buy ") + girl.fullname + __(" for ") + text1

    elif context == "girls":

        key "noshift_K_j" action (SetVariable("selected_girl", girl), Return("assign"))


        if not (girls_firstvisit or girl.away): # Interaction menu can still be accessed when MC interactions=0 (to listen to her story again, for instance)
            key "noshift_K_i" action (SetVariable("selected_girl", girl), Return("interact"))
            key "noshift_K_t" action (SetVariable("selected_girl", girl), Return("equip"))
            if girl.free:
                key "K_BACKSPACE" action (SetVariable("selected_girl", girl), Return("dismiss"))
            else:
                key "K_BACKSPACE" action (SetVariable("selected_girl", girl), Return("sell"))

        frame:

            background None

            xalign 0.0
            yalign 0.2
            xmargin 6
            xpadding 3
            ypadding 6
            xsize xres(320)
            yfill False

            has hbox

            spacing 1
            box_wrap True


            if girl.away:
                $ text1 = _("Away")
                $ ttip = __("She is away on a class or assignment for %s more day%s.") % (girl.return_date - calendar.time, plural(girl.return_date - calendar.time))

            elif girl.hurt > 0:
                $ text1 = _("Hurt")
                if girl.hurt <= 1:
                    $ ttip = __("This girl is hurt and will need to rest for 1 more day until she is ready to do anything.")
                else:
                    $ ttip = __("This girl is hurt and will need to rest for ") + str(round_int(girl.hurt)) + __(" more days until she is ready to do anything.")

            elif girl.exhausted:
                $ text1 = _("Tired")
                $ ttip = __("This girl needs to be fully rested until she can work again.")

            elif girl.resting and girl.job:
                $ text1 = _("Resting")
                $ ttip = __("This girl has been set to rest today according with her schedule.")

            elif not girl.job:
                $ text1 = _("No {u}j{/u}ob")
                $ ttip = __("No job assigned. This girl has been set to rest until further instructions.")

            elif girl.work_whore:
                $ text1 = girl.job.capitalize()[:4] + "./卖淫"
                $ ttip = __("Working and whoring. Change this girl's job or let her rest.")

            else:
                $ text1 = girl.job.capitalize()
                $ ttip = __("Change this girl's job or let her rest.")

            textbutton text1 style "small_button" action (SetVariable("selected_girl", girl), Return("assign")) tooltip ttip + __(" ({i}shortcut: {u}j{/u}{/i})") selected False

            $ sched = girl.workdays[calendar.get_weekday()]

            if sched == 0:
                $ text1 = _("Resting")
            elif sched == 50:
                $ text1 = _("Half-Shift")
            elif sched == 100:
                $ text1 = _("Full shift")

            if not girls_firstvisit:
                key "noshift_K_d" action Return("sched")

            textbutton "排班表" style "small_button":
                tooltip "{i}今日排班情况: %s{/i}.\n点击查看%s的排班表。" % (text1, girl.fullname)
                if not girls_firstvisit:
                    action Return("sched") selected False

            button:
                style "inv_no_padding"

                textbutton "互动":
                    selected False
                    style "small_button"
                    hovered tt.Action(_("Interact with your girl. Costs actions."))

                    if MC.interactions > 0 and not (girls_firstvisit or girl.away):
                        action (SetVariable("selected_girl", girl), Return("interact"))

                if not (girls_firstvisit or girl.away):
                    action (SetVariable("selected_girl", girl), Return("interact"))
                else:
                    action NullAction()

                if MC.interactions <= 0:
                    tooltip __("You cannot take any more actions today.")

                elif girl.away:
                    tooltip __("You cannot interact with %s as she is away.") % girl.name

            textbutton "道具":
                selected False
                style "small_button"

                if not girls_firstvisit: # Available for away girls to avoid complications in the Equipment screen

                    action (SetVariable("selected_girl", girl), Return("equip"))

                    tooltip __("Change this girl's equipment.")

                # else:
                #     tooltip "[girl.fullname] is away on a class or assignment."

            if girl.free:
                textbutton "解雇":
                    selected False
                    style "small_button"
                    if not (girls_firstvisit or girl.away):
                        action (SetVariable("selected_girl", girl), Return("dismiss"))
                    tooltip __("Release this girl from your custody. ({i}shortcut: {u}Backspace{/u}{/i})")

            else:
                textbutton "出售":
                    selected False
                    style "small_button"
                    if not (girls_firstvisit or girl.away):
                        action (SetVariable("selected_girl", girl), Return("sell"))
                    tooltip __("Sell this girl for %s gold (original cost: %s gold). ({i}shortcut: {u}Backspace{/u}{/i})") % (str(girl.get_price("sell")), girl.original_price)


            if girl.upgrade_points >= 1 or girl.can_perk:
                key "noshift_K_u" action (SetVariable("selected_girl", girl), Return("level_or_perks"))
                key "noshift_K_k" action (SetVariable("selected_girl", girl), Return("perks"))
                textbutton "等级提升" style "small_button":
                    action (SetVariable("selected_girl", girl), Return("level_or_perks"))
                    alternate (SetVariable("selected_girl", girl), Return("perks"))
                    tooltip (__("You have ") + str (girl.perk_points) + __(" perk points to spend.\nRight-click to access perks."))
                    hovered Show("perk_details", girl=girl)
                    unhovered Hide("perk_details")

            else:
                if not girls_firstvisit:
                    key "noshift_K_k" action (SetVariable("selected_girl", girl), Return("perks"))

                textbutton "天赋":
                    selected False
                    style "small_button"
                    if not girls_firstvisit:
                        action (SetVariable("selected_girl", girl), Return("perks"))
                    tooltip __("Check her current perks")
                    hovered Show("perk_details", girl=girl)
                    unhovered Hide("perk_details")



            if girl.ready_to_rank():
                key "noshift_K_r" action (SetVariable("selected_girl", girl), Return("rank"))
                textbutton "阶级提升" text_size res_font(14) action (SetVariable("selected_girl", girl), Return("rank"))

            if not girls_firstvisit:
                key "noshift_K_a" action (SetVariable("selected_girl", girl), Return("stats"))

                textbutton "数据统计":
                    style "small_button"
                    selected False
                    action (SetVariable("selected_girl", girl), Return("stats"))
                    tooltip __("Click here for useful stats about your girl.")

            if debug_mode:
                textbutton "图片" style "small_button" action (SetVariable("selected_girl", girl), Return("debug_pics")) text_size res_font(14) tooltip "测试女孩包与游戏的图片生成。" selected False

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
                $ text1 = event_color["a little bad"] % _("Acquaintance")
            elif girl.MC_relationship_level == 1:
                $ text1 = event_color["average"] % _("Friend")
            elif girl.MC_relationship_level == 2:
                $ text1 = event_color["a little good"] % _("Love interest")
            elif girl.MC_relationship_level == 3:
                $ text1 = event_color["good"] % _("Girlfriend")
            elif girl.MC_relationship_level >= 4:
                $ text1 = event_color["special"] % _("Lover")

            text _("Current relationship: ") + text1 xalign 0.0 size res_font(14)

    elif context == "farm":

        frame:

            background None

            xalign 0.0
            yalign 0.19
            xmargin 6
            xpadding 3
            ypadding 6
            xsize xres(320)
            yfill False

            has hbox

            spacing 1
            box_wrap True

#            textbutton "Change program" text_size res_font(14) action Return(("change program", girl)) hovered tt.Action("Change " + girl.name + "'s current training program.")

            key "noshift_K_t" action Return(("equip", girl))
            key "noshift_K_a" action Return(("take out", girl))
            if girl.free:
                key "K_BACKSPACE" action Return(("dismiss", girl))
            else:
                key "K_BACKSPACE" action Return(("sell", girl))

            textbutton "道具":
                text_size res_font(14)
                if not girls_firstvisit:
                    action Return(("equip", girl))

                hovered tt.Action(_("Change this girl's equipment."))

            textbutton "离开农场" text_size res_font(14) action Return(("take out", girl)) hovered tt.Action("把 " + girl.name + " 送回青楼。")

            if girl.free:
                textbutton "解雇":
                    text_size res_font(14)
                    action Return(("dismiss", girl))
                    tooltip __("Release this girl from your custody. ({i}shortcut: {u}Backspace{/u}{/i})")
            else:
                textbutton "出售":
                    text_size res_font(14)
                    if not girls_firstvisit and not girl.broken:
                        action Return(("sell", girl))
                    tooltip __("Sell this girl for %s gold (original cost: %s gold). ({i}shortcut: {u}Backspace{/u}{/i})") % (str(girl.get_price("sell")), girl.original_price)

screen rank_level_details(girl):

    modal False

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
                text __("RANK") size res_font(12)

                $ text1 = rank_name[girl.rank]

                if girl.rank == district.rank:
                    $ text1 += _(" {size=12} (max){/size}")

                text text1 color c_softpurple

            vbox:
                text __("LEVEL") size res_font(12)
                text str(girl.level) + " {size=12} / " + str(girl.rank * 5) + "{/size}" color c_lightgreen

            vbox:
                text __("REPUTATION") size res_font(12)
                text str(int(girl.rep)) + " {size=12}/ " + str(int(girl.get_rep_cap())) + "{/size}" color c_softpurple

            vbox:
                text __("EXPERIENCE") size res_font(12)
                text str(int(girl.xp)) + " {size=12}/ " + str(girl.get_xp_cap()) + "{/size}" color c_lightgreen



        grid 3 10:

            text __("SKILLS") size res_font(12)

            text "" size res_font(12)

            text _("JP") size res_font(12)

            for job in all_jobs:

                text job.capitalize() yalign 0.5
                $ star_text = ""
                for i in range(girl.job_level[job]):
                    $ star_text += "{image=img_star}"

                text star_text yalign 0.5

                text str(round_int(girl.jp[job])) + " {size=12}/ " + str(girl.get_jp_cap(job)) + "{/size}" yalign 0.5 color c_orange

            null height yres(3)
            null height yres(3)
            null height yres(3)

            for job in ("service", "sex", "anal", "fetish"):

                text job.capitalize() yalign 0.5
                $ star_text = ""
                for i in range(girl.job_level[job]):
                    $ star_text += "{image=img_star}"

                text star_text yalign 0.5

                text str(round_int(girl.jp[job])) + " {size=12}/ " + str(girl.get_jp_cap(job)) + "{/size}" yalign 0.5 color c_orange


## SCHEDULE SCREEN

screen schedule(glist):

    modal True

    key "mouseup_3" action (Return())
    key "noshift_K_d" action Return()

    use dark_filter(False)

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
            ysize yres(22)
            xalign 1.0
            hbox:
                xsize xres(150)
                xfill True
                xalign 0.0
                yalign 1.0
                text _("Girl Schedule") color c_darkorange xsize xres(95) xalign 0.5 yalign 0.0 text_align 1.0 size res_font(20)

            for day in weekdays:

                frame xsize xres(88) ysize yres(20)  yalign 1.0 background None:
                    text misc_name_dict[day] size res_font(14) xalign 0.5 color c_brown xsize xres(90):
                        if day == calendar.get_weekday():
                            bold True

            null width xres(10)

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
                        xsize xres(150)
                        xfill True
                        xalign 1.0
                        yalign 0.5

                        button xsize xres(95) ysize yres(53) style "girlbutton" xpadding xres(6) ypadding yres(3) action (SetVariable("selected_girl", girl), Return()) tooltip __("Click here to check ") + girl.fullname + _("'s profile."):
                            has vbox

                            xalign 1.0
                            yalign 0.5

                            text girl.name size res_font(14) text_align 1.0 color c_brown xalign 1.0:

                                if selected_girl == girl:
                                    bold True
                                    color c_white

                            if girl.job:
                                $ text1 = girl.job.capitalize()
                                $ col = job_color[girl.job]
                            else:
                                $ text1 = _("No job")
                                $ col = c_white

                            text text1 size res_font(12) text_align 1.0 color col xalign 1.0

                            if girl.exhausted:
                                $ text1 = event_color["a little bad"] % _("Exhausted")
                            elif girl.hurt:
                                $ text1 = event_color["bad"] % (_("Hurt (") + str(round_int(girl.hurt)) + _(" days)"))
                            else:
                                $ en_max = girl.get_stat_minmax("energy")[1]

                                if girl.energy < en_max / 5:
                                    $ text1 = "{color=[c_red]}" + str(round_int(girl.energy)) + "{/color}/" + str(round_int(en_max))
                                else:
                                    $ text1 = str(round_int(girl.energy)) + "/" + str(round_int(en_max))

                            text text1 size res_font(12) text_align 1.0 color c_brown xalign 1.0

                        hbox:
                            xmaximum xres(50)
                            xfill True
                            xalign 1.0
                            yalign 0.5
                            spacing 20

                            fixed fit_first True xalign 0.5 yalign 0.5:
                                add girl.portrait.get(*res_tb(40)) xalign 0.5 yalign 0.5

                                $ badge = girl.get_badge()
                                if badge:
                                    add ProportionalScale(badge, *res_tb(20)) xalign 0.9 yalign 0.1

                    for day in weekdays:

                        if girl.workdays[day] == 100:
                            $ ttip = _("She will work to the maximum of her abilities.")

                        elif girl.workdays[day] == 50:
                            $ ttip = _("She will receive half the usual number of clients, saving some energy.")

                        elif girl.workdays[day] == 0:
                            $ ttip = _("She will rest and recover some energy.")

                        $ ttip += _("\n{i}Right-click to reverse cycle order.{/i}")

                        textbutton misc_name_dict[workshift_dict[girl.workdays[day]]] text_size res_font(14) xsize xres(90) ysize yres(40) yalign 0.5 tooltip ttip idle_background workshift_color[girl.workdays[day]] hover_background c_darkbrown + "CC":
                            if girl.block_schedule != day:
                                action Function(girl.cycle_workday, day) # renpy.curried_invoke_in_new_context(girl.cycle_workday, day)
                                alternate Function(girl.cycle_workday, day, True)
                            else:
                                action Function(notify, _("You cannot change her schedule as you gave her a day off."))
                                alternate Function(notify, _("You cannot change her schedule as you gave her a day off."))


                    vbox yalign 0.5:
                        textbutton "保存" text_size res_font(14) action ShowTransient("save_schedule", girl=girl, transition=Dissolve(0.15)) tooltip "Click here to save %s's schedule." % girl.fullname
                        textbutton "读取" text_size res_font(14) action ShowTransient("load_schedule", girl=girl, transition=Dissolve(0.15)) tooltip "Click here to load a schedule for %s." % girl.fullname

        text ""

        hbox spacing 10 xalign 1.0:
            if brothel.get_effect("special", "autorest"):
                textbutton "自动休息" xalign 1.0 action Show("autorest")
            textbutton "好的" action (Return())

screen save_schedule(girl):

    modal True

    key "mouseup_3" action Hide("save_schedule", transition=Dissolve(0.15))

    frame background c_ui_darkblue align(0.5, 0.5) xpadding xres(20) ypadding yres(20):

        vbox:
            text _("Save %s's schedule") % (event_color["special"] % girl.fullname) bold True color c_white size res_font(18) xalign 0.5
            null height yres(20)
            for i in range(10):
                button action (Function(game.save_schedule, girl, i), Hide("save_schedule", transition=Dissolve(0.15))) xsize xres(220) ysize yres(28):
                    hbox spacing xres(20) yalign 0.5:
                        textbutton str(i+1) xsize xres(20) xalign 0.5 background None
                        if game.saved_schedules[i]:
                            hbox align(0.5, 0.5):
                                for j in range(7):
                                    textbutton weekdays[j][0] xalign 0.5 background workshift_color[game.saved_schedules[i][j]]
                        else:
                            text "空" italic True size res_font(18)

            null height yres(10)
            textbutton "取消" action Hide("save_schedule", transition=Dissolve(0.15)) xalign 1.0

screen load_schedule(girl):

    modal True

    key "mouseup_3" action Hide("load_schedule", transition=Dissolve(0.15))

    frame background c_ui_darkblue align(0.5, 0.5) xpadding xres(20) ypadding yres(20):

        vbox:
            text _("Load a schedule for %s") % (event_color["special"] % girl.fullname) bold True color c_white size res_font(18) xalign 0.5
            null height yres(20)
            for i in range(10):
                button xsize xres(220) ysize yres(28):
                    if game.saved_schedules[i]:
                        action (Function(girl.load_schedule, game.saved_schedules[i]), Hide("load_schedule", transition=Dissolve(0.15)))
                    hbox spacing xres(20) yalign 0.5:
                        textbutton str(i+1) xsize xres(20) xalign 0.5 background None
                        if game.saved_schedules[i]:
                            hbox align(0.5, 0.5):
                                for j in range(7):
                                    textbutton weekdays[j][0] xalign 0.5 background workshift_color[game.saved_schedules[i][j]]
                        else:
                            text "空" italic True size res_font(18)

            null height yres(10)
            textbutton "取消" action Hide("load_schedule", transition=Dissolve(0.15)) xalign 1.0


screen autorest():
    modal True

    key "mouseup_3" action Hide("autorest")

    frame background c_ui_darkblue xalign 0.5 yalign 0.5 xpadding 10 ypadding 10:
        has vbox spacing 6

        text _("Autorest options") color c_white bold True xalign 0.5
        text ""
        add "items/furniture/scanner.webp" xalign 0.5
        text ""
        text "这台生命分析仪可以让你的女孩在精力过低时安排她自动休息。\n单击鼠标左键可增加阈值\n单击鼠标右键可降低阈值" italic True size res_font(14) color c_white xsize xres(360)
        text "" size res_font(18)
        if autorest_limit == 0:
            $ text1 = __("Autorest OFF")
        else:
            $ text1 = __("Autorest ON - Limit: ") + str(autorest_limit) + __(" energy")

        textbutton text1 action Function(change_autorest, "+") alternate Function(change_autorest, "-") xalign 0.5 xsize xres(360) ysize yres(40) text_size res_font(18)
        text "" size res_font(18)
        textbutton "好的" action Hide("autorest") xalign 1.0

## LEVEL & PERKS SCREEN

screen level(girl):

    modal True

    key "mouseup_3" action Hide("level")

    frame:

        background c_ui_light_solid

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

        $ text1 = girl.name + __(" is ready to level up.")

        text text1 color c_emerald xalign 0.5

        hbox:
            spacing 6
            xalign 0.5
            text __("Available points:") size res_font(14) color c_brown
            text str(round_int(girl.upgrade_points)) size res_font(14) color c_emerald

        text ""

        vbox:

            for stat in gstats_main:

                hbox spacing 3:

                    frame background None xsize xres(180):
                        hbox:
                            text "{b}" + __(stat_name_dict[stat]) + "{/b}" + ": " size res_font(14) color c_brown
                            text str(girl.get_stat(stat)) + " / " + str(girl.get_stat_minmax(stat)[1]) size res_font(14) color c_green

                    grid 4 1:
                        if girl.get_max_stat_upgrade_points(stat) >= 1:
                            textbutton "+1" xsize xres(50) ysize yres(25) text_size res_font(14) action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat"), Play("sound", s_click))
                        else:
                            null
                        if girl.get_max_stat_upgrade_points(stat) >= 5:
                            textbutton "+5" xsize xres(50) ysize yres(25) text_size res_font(14) action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat5"), Play("sound", s_click))
                        elif 5 > girl.get_max_stat_upgrade_points(stat) > 1 and girl.get_max_stat_upgrade_points(stat) not in (5, 10, 20):
                            textbutton "+" + str(int(girl.get_max_stat_upgrade_points(stat))) xsize xres(50) ysize yres(25) text_size res_font(14) action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat_all"), Play("sound", s_click))
                        else:
                            null
                        if girl.get_max_stat_upgrade_points(stat) >= 10:
                            textbutton "+10" xsize xres(50) ysize yres(25) text_size res_font(14) action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat10"), Play("sound", s_click))
                        elif 10 > girl.get_max_stat_upgrade_points(stat) > 5 and girl.get_max_stat_upgrade_points(stat) not in (5, 10, 20):
                            textbutton "+" + str(int(girl.get_max_stat_upgrade_points(stat))) xsize xres(50) ysize yres(25) text_size res_font(14) action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat_all"), Play("sound", s_click))
                        else:
                            null
                        if girl.get_max_stat_upgrade_points(stat) >= 20:
                            textbutton "+20" xsize xres(50) ysize yres(25) text_size res_font(14) action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat20"), Play("sound", s_click))
                        elif 20 > girl.get_max_stat_upgrade_points(stat) > 10 and girl.get_max_stat_upgrade_points(stat) not in (5, 10, 20):
                            textbutton "+" + str(int(girl.get_max_stat_upgrade_points(stat))) xsize xres(50) ysize yres(25) text_size res_font(14) action (SetVariable("selected_girl", girl), SetVariable("selected_stat", stat), Return("up_stat_all"), Play("sound", s_click))
                        else:
                            null

        text ""

        if girl.perk_points > 0:
            $ _next = "perks"
        else:
            $ _next = ""

        textbutton "好的" xalign 1.0 action (Hide("level"), Return(_next))


screen perks(girl):

    modal True

    default selected_archetype = "The Maid"
    default selected_perk = None

    default alpha_unhover = 0.6
    default alpha_hover = 1.0
    default alpha_dict = {k: 0.6 for k in archetype_list}

    key "mouseup_3" action Return(("commit", ""))

    use dark_filter(False)

    frame ypos 0.1 xalign 0.5 xpadding xres(20) ypadding yres(20):
        background c_ui_light_solid

        has vbox spacing 10 xalign 0.5

        text __("%s's perks") % girl.fullname color c_darkorange xalign 0.5

        hbox:
            for archetype in archetype_list:
                button xsize xres(100) xfill True background None action (SetScreenVariable("selected_archetype", archetype), SelectedIf(selected_archetype==archetype)):
                    hovered SetDict(alpha_dict, archetype, alpha_hover)
                    unhovered SetDict(alpha_dict, archetype, alpha_unhover)
                    vbox:
                        fixed:
                            fit_first True
                            if girl.archetypes[archetype].unlocked:
                                add girl.archetypes[archetype].get_pic(portrait=True).get(*res_tb(75)) alpha alpha_dict[archetype]
                            else:
                                add girl.archetypes[archetype].get_pic(portrait=True).get(*res_tb(75)) alpha alpha_dict[archetype] at desaturate
                                add "img_lock"  zoom 0.7 xalign 0.5 yalign 0.5 alpha alpha_dict[archetype]

                        text archetype size res_font(12) selected_bold True color c_darkgrey selected_color c_black

        frame background c_ui_dark xalign 0.5 yalign 0.5 ypadding 0 xpadding 0 xmargin 0:
            fixed fit_first True:
                add archetype_dict[selected_archetype].get_pic().get(yres(800), yres(640)) alpha 0.6

                if not girl.archetypes[selected_archetype].unlocked:
                    add "img_lock" xpos 0 ypos 0.03

                hbox xalign 1.0 xfill True yfill True:
                    fixed xalign 0.3 ypos 0.05 xsize yres(400) ysize yres(620) xfill True yfill True:
                        fit_first True

                        $ perks = archetype_dict[selected_archetype].get_perks()
                        $ pos_dict = {0: (yres(150), 0), 1: (0, yres(100)), 2: (yres(300), yres(100)), 3: (0, yres(250)), 4: (yres(300), yres(250)), 5: (yres(150), yres(350))}

                        add "lines" xalign 0.5 ypos 0.05 alpha 0.7 fit "contain"

                        for perk in perks:
                            $ perk_index = perks.index(perk)

                            button xpos pos_dict[perk_index][0] ypos pos_dict[perk_index][1] xsize yres(110) ysize yres(110) xfill True yfill True:

                                if girl.has_perk(perk.name) or perk in new_perks:
                                    background c_ui_unlocked
                                    add perk.get_pic().get(*res_tb(100)) xalign 0.5 yalign 0.5
                                    action NullAction()
                                    hovered (tt.Action(_("This perk has already been unlocked.")), SetScreenVariable("selected_perk", perk))
                                    unhovered SetScreenVariable("selected_perk", None)

                                elif girl.can_acquire_perk(perk, context="perk_screen")[0]:
                                    at alpha_transform
                                    background c_ui_sensitive + "DD"
                                    hover_background c_ui_sensitive
                                    add perk.get_pic().get(*res_tb(100)) xalign 0.5 yalign 0.5 # alpha 0.6 hover_alpha 1.0
                                    action Return(("add", perk))
                                    hovered (tt.Action(_("Acquire ") + perk.name + _(" for 1 perk point.")), SetScreenVariable("selected_perk", perk))
                                    unhovered SetScreenVariable("selected_perk", None)
                                else:
                                    background c_ui_insensitive + "AA"
                                    # button background None xsize xres(110) ysize yres(110) xfill True yfill True:
                                    add perk.get_pic().get(*res_tb(100)) xalign 0.5 yalign 0.5 at desaturate
                                    action NullAction()
                                    hovered (tt.Action(event_color["a little bad"] % girl.can_acquire_perk(perk, context="perk_screen")[1]), SetScreenVariable("selected_perk", perk))
                                    unhovered SetScreenVariable("selected_perk", None)

                    frame background c_ui_dark xsize xres(260) xalign 1.0 xfill True yfill True:
                        # vbox spacing yres(10) xfill True yfill True:

                            vbox xfill True spacing yres(10):

                                if selected_perk:
                                    $ title = selected_perk.name
                                    $ pic = selected_perk.get_pic()
                                    if selected_perk.min_rank:
                                        $ text1 = "Rank " + rank_name[selected_perk.min_rank] + " perk"
                                    else:
                                        $ text1 = "Rank C perk"
                                    $ text2 = selected_perk.get_description()

                                else:
                                    $ title = selected_archetype
                                    $ pic = archetype_dict[selected_archetype].get_pic()
                                    $ text1 = ""
                                    $ text2 = archetype_description[selected_archetype]

                                text __(title) size res_font(18) bold True yalign 0.0 xalign 0.5 drop_shadow 2,2

                                add pic.get(*res_tb(220)) xalign 0.5

                                if not selected_perk and not girl.archetypes[selected_archetype].unlocked:
                                    textbutton "解锁\n{size=-6}(消耗2天赋点){/size}" xalign 0.5 xpadding 6 ypadding 6:
                                        if perk_points >= 2:
                                            action Return(("unlock", selected_archetype))

                                text __(text1) size res_font(14) bold True yalign 0.0
                                text __(text2) size res_font(14) yalign 0.0

                            vbox yalign 1.0 xfill True:
                                text __("Perk points: ") + str(perk_points) color c_orange size res_font(20) xalign 0.5 drop_shadow 2,2
                                hbox xalign 0.5:
                                    textbutton "取消" action Return(("cancel", ""))
                                    textbutton "确认":
                                        if new_perks:
                                            action Return(("commit", ""))


screen trait_details(girl):

    tag trait_details

    default yadj = ui.adjustment()
    default t = 0

    if len(girl.traits+girl.perks) > 20:
        if yadj.value < len(girl.traits+girl.perks)*25:
            timer 0.1 repeat True action (SetScreenVariable("t", t + 0.1), Function(yadj.change, max(0, 25*(t-0.25)))) # Scrolls down after 0.25 seconds

    frame:
        background c_ui_darker
        xpos 0.31
        xanchor 0.0
        yalign 0.7
        xsize 0.45
        ymaximum 0.85

        viewport:
            yadjustment yadj
            yfill False

            has vbox

            spacing 3

            text __("%s's traits") % (girl.fullname) xalign 0.5 color c_orange

            text "" size res_font(6)

            for trait in girl.traits:
                hbox:
                    frame background None ypadding 0 xsize xres(150) xfill True xalign 0.0 yalign 0.0:
                        text trait.name xmaximum xres(150) yalign 0.0 size res_font(14) bold True:
                            if trait in gold_traits:
                                color c_orange
                            elif trait in pos_traits:
                                color c_emerald
                            elif trait in neg_traits:
                                color c_crimson
                    text trait.get_description(short=True) xfill True size res_font(14) xalign 0.0 yalign 0.0

            text "" size res_font(6)

            if girl.perks:

                text __("%s's perks") % girl.name xalign 0.5 color c_orange

                text "" size res_font(6)

                for perk in girl.perks:
                    hbox:
                        frame background None ypadding 0 xsize xres(150) xfill True xalign 0.0 yalign 0.0:
                            text perk.name xmaximum xres(150) yalign 0.0 size res_font(13) bold True
                        text perk.get_description(short=True) xfill True size res_font(13) xalign 0.0 yalign 0.0


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

            text  __("%s's active perks") % girl.name xalign 0.5 color c_orange

            text "" size res_font(6)

            for perk in girl.perks:
                hbox:
                    frame background None ypadding 0 xsize xres(150) xfill True xalign 0.0 yalign 0.0:
                        text perk.name xmaximum xres(150) yalign 0.0 size res_font(13) bold True
                    text perk.get_description(short=True) xmaximum xres(250) size res_font(13)





## GIRL LOG SCREEN ## Displays statistics about each girl

screen girl_log(): # Reminder: selected_girl is a Global variable that holds the currently selected girl

    modal True

    key "mouseup_3" action Return()

    use dark_filter(can_click=False)

#     $ girl = selected_girl
    $ log_dict = compile_girl_log(selected_girl) # Hands the screen a dictionary holding all calculations (to avoid refreshing calc with every frame)

    default days = 1

    $ biggest = res_font(24)

    $ big = res_font(18)

    $ average = res_font(14)

    $ small = res_font(12)

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

                textbutton "昨天" action SetScreenVariable("days", 1) xsize xres(200) background c_brown + "AA" text_color c_white selected_idle_background c_orange + "AA" selected_hover_background c_orange + "AA" hover_background c_orange + "55"

                textbutton "上周" action SetScreenVariable("days", 7) xsize xres(200) background c_brown + "AA" text_color c_white selected_idle_background c_orange + "AA" selected_hover_background c_orange + "AA" hover_background c_orange + "55"

                textbutton "上个月" action SetScreenVariable("days", 28) xsize xres(200) background c_brown + "AA" text_color c_white selected_idle_background c_orange + "AA" selected_hover_background c_orange + "AA" hover_background c_orange + "55"

                textbutton "总计" action SetScreenVariable("days", 0) xsize xres(200) background c_brown + "AA" text_color c_white selected_idle_background c_orange + "AA" selected_hover_background c_orange + "AA" hover_background c_orange + "55"


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
                            text "General" size average color c_prune

                            text "" size average

                            grid 5 2:

                                transpose True
                                spacing 3

                                text "{b}Days{/b}" color c_darkgrey size small xalign 0.5

                                if days == 0:
                                    text str(log_dict["age"]) size average color c_prune xalign 0.5

                                elif days > log_dict["age"]:
                                    text str(log_dict["age"]) size average color c_prune xalign 0.5

                                else:
                                    text str(days) size average color c_prune xalign 0.5

                                text "{b}Gold{/b}" color c_darkgold size small xalign 0.5

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

                                $ ttip = __("{b}Profit: {color=[c_white]}") + str_int(net) + "{/color}{/b}"
                                $ ttip += __("\nJobs: {color=[c_green]}") + str_int(j_gold) + "{/color}"
                                $ ttip += __("     Quests: {color=[c_green]}") + str_int(q_gold) + "{/color}"
                                $ ttip += __("\nUpkeep: {color=[c_red]}-") + str_int(upk) + "{/color}"

                                textbutton str_int(j_gold + q_gold) background None xpadding 0 ypadding 0 xmargin 0 ymargin 0 text_size average text_color c_prune xalign 0.5 action NullAction() tooltip ttip

                                text "{b}XP{/b}" color c_emerald size small xalign 0.5

                                text str_int(log_dict["total_xp"][days]) size average color c_prune xalign 0.5

                                text "{b}JP{/b}" color c_orange size small xalign 0.5

                                text str_int(log_dict["total_jp"][days]) size average color c_prune xalign 0.5

                                text "{b}Reputation{/b}" color c_purple size small xalign 0.5

                                text str_int(log_dict["total_rep"][days]) size average color c_prune xalign 0.5

                        vbox:
                            text "Activity" size average color c_prune

                            hbox:

                                spacing 20

                                grid 2 4:

                                    spacing 3

                                    text "" size small

                                    text "{b}Days{/b}" color c_darkgrey size small xalign 0.5

                                    text "{b}工作{/b}" color c_orange size small xalign 0.5

                                    $ ttip = __("Waitress: ") + str_int(log_dict["waitress_days"][days]) + __("              Dancer: ") + str_int(log_dict["waitress_days"][days]) + __("\nMasseuse: ") + str_int(log_dict["masseuse_days"][days]) + __("            Geisha: ") + str_int(log_dict["geisha_days"][days]) + __("\nWhore: ") + str_int(log_dict["whore_days"][days]) + __("                 Work/whore : ") + str_int(log_dict["work_whore_days"][days])

                                    textbutton str_int(log_dict["work_days"][days]) background None xpadding 0 ypadding 0 xmargin 0 ymargin 0 text_size average text_color c_brown xalign 0.5 action NullAction() hovered tt.Action(ttip)

                                    text "{b}休息{/b}" color c_green size small xalign 0.5

                                    text str_int(log_dict["rest_days"][days]) size average color c_brown xalign 0.5

                                    text "{b}外出{/b}" color c_blue size small xalign 0.5

                                    text str_int(log_dict["away_days"][days] + log_dict["farm_days"][days]) size average color c_brown xalign 0.5

                                grid 2 3:

                                    spacing 3

                                    text "" size small

                                    text "{b}Days{/b}" color c_darkgrey size small xalign 0.5

                                    text "{b}遇袭{/b}" color c_red size small xalign 0.5

                                    text str_int(log_dict["strike_days"][days]) size average color c_brown xalign 0.5

                                    text "{b}受伤/生病{/b}" color c_red size small xalign 0.5

                                    text str_int(log_dict["hurt_days"][days] + log_dict["sick_days"][days]) size average color c_brown xalign 0.5

#                                    text "{b}Sick{/b}" color c_red size small xalign 0.5

#                                    text str_int(log_dict["sick_days"][days]) size average color c_brown xalign 0.5

                    text "" size average

    #            vbox:

                    text "Jobs" size average color c_prune

#                    text "" size average

                    grid 7 6:

                        spacing 1

                        text "" size small

                        text "{b}Customers{/b}" color c_darkgrey size small xalign 0.5

                        text "{b}Gold{/b}" color c_darkgold size small xalign 0.5

                        text "{b}XP{/b}" color c_emerald size small xalign 0.5

                        text "{b}JP{/b}" color c_orange size small xalign 0.5

                        text "{b}Reputation{/b}" color c_purple size small xalign 0.5

                        text "{b}平均得分{/b}" color c_crimson size small xalign 0.5

                        for job in all_jobs:

                            text "{b}" + __(job.capitalize()) + "{/b}" color c_firered size small xalign 0.5

                            text str_int(log_dict[job + "_cust"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[job + "_gold"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[job + "_xp"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[job + "_jp"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[job + "_rep"][days]) size average color c_brown xalign 0.5

                            $ perf, ttip = log_dict[job + "_perf"][days]

                            if perf != "-":
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


                        text "{b}Whore{/b}" color c_firered size small xalign 0.5

                        text str(round_int(log_dict["whore_cust"][days])) size average color c_brown xalign 0.5

                        text str_int(log_dict["whore_gold"][days]) size average color c_brown xalign 0.5

                        text str_int(log_dict["whore_xp"][days]) size average color c_brown xalign 0.5

                        text str_int(log_dict["whore_jp"][days]) size average color c_brown xalign 0.5

                        text str_int(log_dict["whore_rep"][days]) size average color c_brown xalign 0.5

                        $ perf, ttip = log_dict["whore_perf"][days]

                        if perf != "-":
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

                    text "Sex Acts" size average color c_prune

#                    text "" size average

                    grid 7 5:

                        spacing 1

                        text "" size small

                        text "{b}Customers{/b}" color c_darkgrey size small xalign 0.5

                        text "{b}Gold{/b}" color c_darkgold size small xalign 0.5

                        text "{b}Xp{/b}" color c_emerald size small xalign 0.5

                        text "{b}JP{/b}" color c_orange size small xalign 0.5

                        text "{b}Reputation{/b}" color c_purple size small xalign 0.5

                        text "{b}Av. score{/b}" color c_crimson size small xalign 0.5

                        for act in all_sex_acts:

                            text "{b}" + __(act.capitalize()) + "{/b}" color c_firered size small xalign 0.5

                            text str_int(log_dict[act + "_cust"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[act + "_gold"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[act + "_xp"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[act + "_jp"][days]) size average color c_brown xalign 0.5

                            text str_int(log_dict[act + "_rep"][days]) size average color c_brown xalign 0.5

                            $ perf, ttip = log_dict[act + "_perf"][days]

                            textbutton str(perf) background None xpadding 0 ypadding 0 xmargin 0 ymargin 0 text_size average text_color c_prune xalign 0.5 action NullAction() hovered tt.Action(ttip)



## DISTRICT SCREEN ##

screen suzume_hints(contact_list):

    use dark_filter(False, True)

    key "mouseup_3" action (Return(False))

    frame background None xmargin xres(60) top_margin yres(120) bottom_margin(250):
        has vbox
        spacing 20

        hbox:
            box_wrap True

            for contact in contact_list:
                $ img, ttip, npc = contact

                button xsize xres(120) ysize yres(120) xpadding 6 ypadding 6:
                    if MC.interactions >= 1:
                        action Return(npc)
                    add img xalign 0.5 yalign 0.5 fit "contain"
                    if npc == NPC_suzume:
                        tooltip "Talk to {b}Suzume{/b} for general tips, or once you have unlocked all 3 tips for a given Kunoichi."
                    else:
                        tooltip "Ask Suzume to track {b}%s{/b}, for information on the Kunoichi. {b}Costs 1 {/b}{image=img_AP}." % ttip

            textbutton "返回" text_bold True xalign 0.5 yalign 0.5 xsize xres(120) ysize yres(120) xpadding 6 ypadding 6 action Return(False) # Note that 'None' is not a valid return value


        hbox spacing 50 xalign 0.5:
            text "Hints collected:" yalign 0.5 bold True

            for ninja in (NPC_narika, NPC_mizuki, NPC_haruka):
                if ninja.flags["hints"] >=3:
                    $ ttip = "You may now {b}talk to Suzume{/b} to devise a cunning action plan and finally catch her."
                else:
                    $ ttip = "You need to {b}gather 3 hints{/b} before you can attempt to catch her again."

                button background None xsize xres(160) ysize yres(80) xpadding 6 ypadding 6:
                    action NullAction()
                    tooltip "You have received %s tips on {b}%s{/b}. %s" % (str(ninja.flags["hints"]), ninja.name, ttip)
                    has hbox
                    add ninja.name.lower() yalign 0.5 fit "contain"
                    text "%s/3" % str(ninja.flags["hints"]) bold True xalign 0.5 yalign 0.5

        

screen districts(context = "visit"): # returns a chosen district. Context can be "first visit", "visit" or "relocate"

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

        xalign 0.5
        yalign 0.5

        vbox:
            xsize int(config.screen_width * 0.25)
            yalign 0.5
            ysize yres(400)
            yfill True

            if suzume_hints_active and context == "visit":
                frame background c_ui_dark xpadding 6 ypadding 6 xalign 0.35:
                    vbox:
                        text "The Hunt" size res_font(14) xalign 0.5 yalign 0.5
                        button xsize yres(120) ysize yres(120) xpadding 6 ypadding 6:
                            if MC.interactions >= 1:
                                action Call("c3_interrogate_contacts")
                            tooltip "Talk to Suzume to {b}talk to your contacts{/b} and discover {b}hints{/b} about the Kunoichi you are hunting."
                            has vbox
                            xalign 0.5
                            # text "Inquire" size res_font(14) xalign 0.5 yalign 0.5
                            add "side suzume" xalign 0.5 yalign 0.5 fit "contain"

            else:
                text "无照经营" xalign 0.5 yalign 0.0 size res_font(14) text_align 0.5 color c_darkgrey

            use district_button(district_dict["slum"], context) id "b1"


        vbox:
            yalign 0.5
            spacing 60
            xsize int(config.screen_width * 0.25)
            ysize yres(400)
            yfill True

            hbox:
                xalign 0.5
                spacing 10


                if game.chapter >= 2:

                    add ProportionalScale("UI/" + license_dict[1][1], *res_tb(50)) xalign 0.5

                else:

                    add ProportionalScale("UI/" + license_dict[0][1], *res_tb(50)) xalign 0.5

                text __(license_dict[1][0]) + "\n需要" xalign 0.5 yalign 0.0 size res_font(14) text_align 0.5 color c_darkgrey

            use district_button(district_dict["warehouse"], context) id "b2"
            use district_button(district_dict["docks"], context) id "b3"



        vbox:
            yalign 0.5
            spacing 60
            xsize int(config.screen_width * 0.25)
            ysize yres(400)
            yfill True

            hbox:
                xalign 0.5
                spacing 10

                if game.chapter >= 4:

                    add ProportionalScale("UI/" + license_dict[2][1], *res_tb(50))

                else:

                    add ProportionalScale("UI/" + license_dict[0][1], *res_tb(50))

                text __(license_dict[2][0]) + "\n需要" xalign 0.5 yalign 0.0 xsize xres(160) size res_font(14) text_align 0.5 color c_darkgrey

            use district_button(district_dict["gardens"], context)  id "b4"
            use district_button(district_dict["cathedra"], context)  id "b5"


        vbox:

            yalign 0.5
            xsize int(config.screen_width * 0.25)
            ysize yres(400)
            yfill True

            hbox:
                xalign 0.5
                spacing 10

                if game.chapter >= 6:

                    add ProportionalScale("UI/" + license_dict[3][1], *res_tb(50))

                else:

                    add ProportionalScale("UI/" + license_dict[0][1], *res_tb(50))

                text __(license_dict[3][0]) + "\n需要" xalign 0.5 yalign 0.0 xsize xres(150) size res_font(14) text_align 0.5 color c_darkgrey

            use district_button(district_dict["hold"], context)  id "b6"

    if context != "first visit":
        use overlay("districts")

    if context == "visit":
        use close((Hide("districts"), Hide("tool"), Jump("main")))




screen district_button(dis, context):

    button:
        xalign 0.5
        ycenter 0.5
        xpadding xres(9)
        ypadding yres(9)
        at alpha_transform

        if game.chapter >= dis.chapter:
            if context != "relocate":
                action Return(dis)
                tooltip "前往%s (按数字键 %s 前往此地点)。" % (dis.name, str(all_districts.index(dis) + 1))
            elif dis not in game.blocked_districts and district != dis:
                action Return(dis)
                tooltip "Choose %s to relocate your brothel." % dis.name
        vbox:

            spacing 10

            text dis.name size res_font(14) xalign 0.5 yalign 0.5

            fixed:
                fit_first True

                add dis.get_pic(xres(150), yres(100)) # alpha 0.66 insensitive_alpha 0.33 hover_alpha 1.0

                $ max_love = 0

                for loc in location_dict[dis.name]:
                    for girl in loc.girls:
                        if girl.love > max_love:
                            $ max_love = girl.love

                if max_love > 0:

                    $ h = 1 + max_love // 2

                    add ProportionalScale("UI/heart.webp", h, 50) xalign 0.5 yalign 0.4 # idle_alpha 0.66 hover_alpha 0.8

                text str(all_districts.index(dis) + 1) size res_font(14) xalign 0.05 yalign 0.95


screen visit_district():

    zorder 0

    key "mouseup_3" action (SetVariable("selected_destination", "districts"), Jump("teleport"))
    use close((SetVariable("selected_destination", "districts"), Jump("teleport")))
    use shortcuts()

    $ available_districts = [d for d in all_districts if d.chapter <= game.chapter]

    key "K_LEFT" action (SetVariable('selected_district', get_previous(available_districts, selected_district, loop=True)), Jump("visit_district"))
    key "K_RIGHT" action (SetVariable('selected_district', get_next(available_districts, selected_district, loop=True)), Jump("visit_district"))

    if len(available_districts) > 1:
        textbutton "<" xalign 0.05 ysize yres(120) yalign 0.4 action (SetVariable('selected_district', get_previous(available_districts, selected_district, loop=True)), Jump("visit_district")) tooltip "Visit the previous district (you can use arrow keys)."

        textbutton ">" xalign 0.95 ysize yres(120) yalign 0.4 action (SetVariable('selected_district', get_next(available_districts, selected_district, loop=True)), Jump("visit_district")) tooltip "Visit the next district (you can use arrow keys)."

    $ i = 1
    for loc in location_dict[selected_district.name]:
        key str(i) action Return([loc, "go"])

        # Shortcut added by Lokplart
        if loc.can_do_action():
            key "alt_K_" + str(i) action Return([loc, "special"])

        $ i += 1

    fixed:
        xysize (config.screen_width, int(config.screen_height*0.8))
        xfill True
        yfill True

        vbox focus None:

            xalign 0.5
            yalign 0.5

            text __(selected_district.name) xalign 0.5

            text ""
            text ""

            grid 3 2:

                spacing 50

                for location in location_dict[selected_district.name]:

                    button focus None:
                        xalign 0.5
                        yalign 0.33
                        xpadding xres(9)
                        ypadding yres(9)
                        at alpha_transform

                        action Return([location, "go"])

                        if location.secret:
                            tooltip "你还没有解锁这个区域。"
                        else:
                            tooltip "{b}" + __(location.name) + __("{/b}. Press ") + str(location_dict[selected_district.name].index(location) + 1) + __(" to visit this location.")

                        vbox:

                            spacing 10

                            if location.secret:

                                text "???" size res_font(14) xalign 0.5

                                add im.Scale("districts/locations/secret.webp", xres(150), yres(100)) # insensitive_alpha 0.33 idle_alpha 0.66 hover_alpha 1.0

                            else:
                                text location.name size res_font(14) xalign 0.5

                                fixed:
                                    fit_first True
                                    add location.get_pic(xres(150), yres(100)) # insensitive_alpha 0.33 alpha 0.66 hover_alpha 1.0

                                    $ max_love = 0

                                    for girl in location.girls:
                                        if girl.love > max_love:
                                            $ max_love = girl.love

                                    if max_love > 0:

                                        $ h = 1 + max_love // 2

                                        add ProportionalScale("UI/heart.webp", h, 50) xalign 0.5 yalign 0.4 # insensitive_alpha 0.33 idle_alpha 0.66 hover_alpha 0.8

                                    if location.action:
                                        button xsize xres(60) ysize yres(60) xpos xres(105) ypos yres(45) background None xmargin yres(5) ymargin yres(5) xpadding yres(5) ypadding yres(5) focus None:
                                            at alpha_transform
                                            if location.can_do_action() and location.menu[1] in location_tb.keys():
                                                add location_tb[location.menu[1]] fit "contain" # insensitive_alpha 0.33 alpha 0.66 hover_alpha 1.0
                                            elif location.menu[1] in location_tb.keys():
                                                add location_tb[location.menu[1]] + " grey" fit "contain" # insensitive_alpha 0.33 alpha 0.66 hover_alpha 1.0

                                            if location.menu_costs_AP and MC.interactions < 1:
                                                action NullAction()
                                                tooltip __(location.menu[0]) + __(". You cannot collect as you are out of AP.")
                                            else:
                                                action Return([location, "special"])
                                                if location.menu_costs_AP:
                                                    tooltip __(location.menu[0]) + __(". Costs 1 {image=img_AP}.")
                                                else:
                                                    tooltip __(location.menu[0]) + "."

                                    text str(location_dict[selected_district.name].index(location) + 1) size res_font(14)  xalign 0.05 yalign 0.95

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

    textbutton "<" xalign 0.05 ysize yres(120) yalign 0.4 action (SetVariable('selected_location', _previous), Jump("visit_location")) tooltip "前往上一个区域 (也可以用左方向键切换)。"

    textbutton ">" xalign 0.95 ysize yres(120) yalign 0.4 action (SetVariable('selected_location', _next), Jump("visit_location")) tooltip "前往下一个区域 (也可以用右方向键切换)。"

    frame:
        background None # loc.get_pic(config.screen_width, int(config.screen_height*0.8))
        xysize (config.screen_width, int(config.screen_height*0.8))
        xfill True
        yfill True

        has vbox
        xalign 0.5
        yalign 0.7
#        yfill True

        text selected_location.name xalign 0.5

        text ""
        text ""

        hbox xalign 0.5 ysize yres(280):

            spacing xres(30)

            for girl in selected_location.girls:

                button:
                    xalign 0.5
                    yalign 0.33
                    xpadding xres(18)
                    ypadding yres(18)
                    action Return(girl)
                    at alpha_transform

                    if girl.MC_interact:
                        tooltip "和" + girl.fullname + "打招呼。"
                    else:
                        tooltip "和这个陌生女孩搭讪，消耗 1 {image=img_AP}。"

                    vbox:

                        spacing yres(3)

                        if girl.MC_interact:
                            text girl.fullname size res_font(14) align 0.5, 0.5:
                                if girl.original:
                                    color c_yellow
                        else:
                            text "?" size res_font(14) align 0.5, 0.5

                        fixed:
                            fit_first True
                            xmaximum xres(240)
                            ymaximum yres(240)
                            xfill False
                            yfill False

                            add AlphaMask(girl.profile.get(*res_tb(240)), Frame("GUI/edge_mask.png")) xalign 0.5 # insensitive_alpha 0.33 idle_alpha 0.8 hover_alpha 1.0
                            # add girl.profile.get(*res_tb(240)) xalign 0.5 insensitive_alpha 0.33 idle_alpha 0.8 hover_alpha 1.0

                            if girl.love >= 5:

                                $ h = 5 + girl.love // 2

                                add ProportionalScale("UI/heart.webp", *res_tb(h)) xalign 0.97 yalign 0.03 # idle_alpha 0.66 hover_alpha 0.8

                            if persistent.show_girlpack_rating in ("In market and city", "Everywhere"):

                                $ rating, ttip = get_girlpack_rating(girl)

                                textbutton "女孩评级 (" + capitalize(girl.path.split("/")[-1]) + "): " + rating background c_ui_darkblue text_size res_font(18) yalign 1.0 xmargin 10 ymargin 10 action NullAction() tooltip ttip

        text ""
        text ""

        hbox:
            spacing 25
            xalign 0.5

            button:
                xsize xres(240)
                ysize yres(50)

                if MC.interactions > 0:
                    action Return("visit")
                    tooltip "探索这个区域。消耗1{image=img_AP}。"

                hbox xalign 0.5 yalign 0.5:
                    text "四处闲逛 (1 " size res_font(18)
                    text "{image=img_AP}" xalign 0.0 yalign 0.5
                    text ")" xalign 0.0 yalign 1.0 size res_font(18)

            if selected_location.action:
                button xsize xres(240) ysize yres(50) xpadding xres(18):
                    at alpha_transform
                    if selected_location.can_do_action():
                        action Return("special")
                        if selected_location.menu_costs_AP:
                            tooltip __(selected_location.menu[0]) + __(". Costs 1 {image=img_AP}.")
                        else:
                            tooltip __(selected_location.menu[0]) + __(" (free).")
                    hbox yalign 0.5 xfill True:
                        if selected_location.can_do_action() and selected_location.menu[1] in location_tb.keys():
                            add location_tb[selected_location.menu[1]] fit "contain" # insensitive_alpha 0.33 idle_alpha 0.66 hover_alpha 1.0
                        elif selected_location.menu[1] in location_tb.keys():
                            add location_tb[selected_location.menu[1]] + " grey" fit "contain" # insensitive_alpha 0.33 idle_alpha 0.66 hover_alpha 1.0

                        hbox spacing xres(10) xalign 0.0 yalign 0.5 box_wrap True:
                            text selected_location.menu[0] size res_font(18)
                            if selected_location.menu_costs_AP:
                                text "(1 {image=img_AP})" yalign 1.0 size res_font(16)

            if story_flags["ninja hunt"] and not story_flags["ninja hunt locked %s" % selected_district.name] and story_flags["ninja hunt"] != calendar.time and not story_flags["ninja hunt hide " + selected_location.name] and selected_district.rank <= 2:
                textbutton "追捕忍者" text_size res_font(18) xsize xres(240) ysize yres(50):

                    if MC.interactions > 0:
                        action Return("hunt")
                    tooltip "Hunt for ninjas dwelling in this location."

    use overlay("visit_location")
    use close((Hide("visit_location"), Jump("visit_district")))



## BROTHEL SCREEN ##

screen brothel():

    zorder 0
    use overlay("brothel")

    if not brothel_firstvisit:
        key "mouseup_3" action (Hide("brothel"), Jump("main"))
        use close ((Hide("brothel"), Jump("main")))
        use shortcuts()

        if MC.trainers:
            key "K_LEFT" action Function(MC.cycle_trainers, reverse = True)
            key "K_RIGHT" action Function(MC.cycle_trainers)

    if debug_mode: # Checks the UI with a different bg
        key "noshift_K_n" action (Function(brothel.cycle_pic))
        key "shift_K_n" action (Function(brothel.cycle_pic, reverse=True))

    frame background None xalign 0.9 yalign 0.125 ypadding 5 xsize 0.25:
        has vbox
        # if district.rank > 1:
        if story_flags["found wagon"]:
            $ text1 = "青楼改造" + "{size=%i}" % -res_font(4) #意译，直译为木匠的马车

            if brothel.current_building:
               # if len(brothel.current_building.name) > 15:
               #     $ text1 += "\n(" + __(brothel.current_building.name[:15]) + "。"
               # else:
                $ text1 += "\n(" + __(brothel.current_building.name) + " "
                $ max_dur = float(brothel.current_building.duration)
                $ leftover_dur = round_int(max_dur - (calendar.time - brothel.started_building))

                if leftover_dur/max_dur <= 0.25:
                    $ text1 += u"⏳"   #u"\u25d5"  原文本符号字体缺失，替换为emoji
                elif leftover_dur/max_dur <= 0.5:
                    $ text1 += u"⌛"   #u"\u25d1"
                else:
                    $ text1 += u"🔨"   #u"\u25d4"

                $ text1 += "剩余" + str(leftover_dur) + "天){/size}"
        else:
            $ text1 = "？？？"

        if game.chapter >= 2 or NPC_carpenter.active:
            textbutton text1 ysize yres(40) ypadding 5 xfill True action Return("furniture") text_size res_font(18) text_font "DejaVuSans.ttf" tooltip __("Build furniture to unlock various upgrades for the brothel.")

        if game.chapter >= 2:
            textbutton "经营策略" text_size res_font(18) ysize yres(40) xfill True action Return("open options") tooltip __("Fine-tune your brothel for various customer populations and preferences.")

    frame:
        background None
        xpadding xres(25)
        ypadding 0
        ymargin 0
        ypos 0.125
        ysize 0.7
        xfill True
        yfill True

        has vbox
        spacing yres(15)
        yfill True

        if not brothel_firstvisit:
            hbox xfill True xsize 0.66:
                $ bro_costs = round_int(brothel.get_adv_cost() + brothel.get_sec_cost() + brothel.get_maintenance_cost())
                $ bro_upk = round_int(sum(g.upkeep*g.get_effect("boost", "total upkeep") for g in MC.girls))
                $ farm_upk = round_int(sum(g.upkeep*g.get_effect("boost", "total upkeep")//2 for g in farm.girls))

                $ text1 = __("You must pay {b}") + '{:,}'.format(bro_costs) + __("{/b} gold for your brothel services. You must also pay {b}") + '{:,}'.format(bro_upk) + __("{/b} gold for your girls upkeep")

                if farm.active and farm.girls:
                    $ text1 += __(" and {b}") + '{:,}'.format(farm_upk) + __("{/b} gold for the girls in the farm")
                $ text1 += __(" (not accounting for special effects).")

                textbutton __("每日开销: ") + '{:,}'.format(bro_costs + bro_upk + farm_upk) + "金币" text_size res_font(18) text_xalign 0.0 xalign 0.0 background c_ui_dark xsize xres(300) ysize yres(36) action NullAction() tooltip text1

                textbutton brothel.name text_size res_font(24) xalign 0.5 ysize yres(40) action Return("change name") tooltip __("Click to change your brothel's name.")

            hbox:
                xalign 0.0
                xfill True

                vbox spacing 10 xalign 0.0:
                    text "{b}协助者{/b}" size res_font(18) yalign 0.0 drop_shadow (2, 2)

                    frame:
                        xsize xres(360)
                        ysize yres(220)
                        xalign 0.5
                        xpadding xres(20)
                        background c_ui_dark

                        has vbox yalign 0.5

                        hbox spacing 10 xalign 0.5:
                            if MC.trainers:
                                vbox spacing 0:
                                    button style "inv_no_padding" xsize xres(156) xmargin 0 xpadding 0 action NullAction():
                                        hovered tt.Action(__("Trainers help your girls learn new skills. Discover new trainers by meeting the people of Zan!"))
                                        add MC.current_trainer.portrait zoom 1.0 xalign 0.5 yalign 0.5

                                    if len(MC.trainers) == 1:
                                        $ text1 = "No other trainer available"
                                    else:
                                        $ text1 = "Trainers help your girls learning new skills. Discover new trainers by meeting the people of Zan!"

                                    button xmargin 0 xpadding 0 xsize xres(156) background None action NullAction() hovered tt.Action(text1):

                                        has hbox xfill True

                                        textbutton "<" xsize xres(75) xalign 0.0:
                                            if len(MC.trainers) > 1:
                                                action Function(MC.cycle_trainers, reverse = True)
                                                tooltip "上一个协助者"

                                        textbutton ">" xsize xres(75) xalign 1.0:
                                            if len(MC.trainers) > 1:
                                                action Function(MC.cycle_trainers)
                                                tooltip "下一个协助者"

                                vbox:
                                    text "{b}" + MC.current_trainer.name + "{/b}" size res_font(18) xalign 0.5
                                    text "\n" + MC.current_trainer.trainer_description size res_font(14) justify True

                            else:
                                textbutton "?" xsize xres(100) ysize yres(150)

                                text __("{i}Recruit a trainer to help your girls.{/i}") size res_font(14)

                vbox spacing 10 xalign 1.0:
                    text "{b}外包人员{/b}" size res_font(18) yalign 0.0 drop_shadow (2, 2)

                    frame:
                        xsize xres(580)
                        ysize yres(220)
                        xalign 1.0
                        background c_ui_dark

                        has vbox spacing 10 xalign 0.0 yalign 0.5

                        fixed yfill False ysize yres(120):

                            $ ttip = __("Your brothel's current reputation is {b}") + str(brothel.rep) + "{/b}."

                            textbutton "广告宣发" ypos 0.1 text_color c_white ypadding 4 text_size res_font(18) background None action NullAction() tooltip ttip text_align 0.0

                            bar:
                                xsize xres(200)
                                xpos 0.25
                                ypos 0.1
                                thumb Frame("tb advertising", xsize=xres(12), ysize=yres(24))
                                thumb_offset xres(3)
                                left_gutter xres(6)
                                right_gutter xres(6)
                                value FieldValue(brothel, "advertising", brothel.max_help, action=Function(brothel.update_customer_count))
                                hovered tt.Action(__("Pay hot chicks with revealing clothing to hang around your brothel, and tell would-be patrons about your establishment."))

                            $ adv_bonus = brothel.get_effect("change", "advertising")
                            if adv_bonus != 0:
                                $ text1 = " ({color=[c_green]}+" + str(adv_bonus) + __("{/color} from girls/effects)")
                            else:
                                $ text1 = ""
                            $ text2 = brothel.get_adv_cost()

                            textbutton "[brothel.advertising]  babes" + text1 background None text_size res_font(14) xpos 0.6 ypos 0.1 ypadding 6

                            $ ttip = __("Your brothel's current threat level is ") + brothel.estimate_threat_level() + "."

                            textbutton "安全等级" text_color c_white ypos 0.4 ymargin 0 ypadding 4 text_align 0.0  background None text_size res_font(18) action NullAction() tooltip ttip

                            bar:
                                xsize xres(200)
                                xpos 0.25
                                ypos 0.4
                                thumb Frame("tb security", xsize=xres(12), ysize=yres(24))
                                thumb_offset xres(3)
                                left_gutter xres(6)
                                right_gutter xres(6)
                                value FieldValue(brothel, "security", brothel.max_help)
                                hovered tt.Action(__("Pay some sellswords to keep unruly patrons and competitors at bay."))

                            $ sec_bonus = brothel.get_effect("change", "security")
                            if sec_bonus != 0:
                                $ text1 = " ({color=[c_green]}+" + str(sec_bonus) + __("{/color} from girls/effects)")
                            else:
                                $ text1 = ""
                            $ text2 = brothel.get_sec_cost()

                            textbutton "[brothel.security]  goons" + text1 background None text_size res_font(14) xpos 0.6 ypos 0.4 ypadding 6



                            $ ttip = __("Your brothel's current dirt level is {b}") + str(round_int(brothel.dirt)) + "{/b}."

                            textbutton "卫生状况" text_color c_white ypos 0.7 ymargin 0 ypadding 4 text_align 0.0 text_size res_font(18) background None action NullAction() tooltip ttip

                            bar:
                                xsize xres(200)
                                xpos 0.25
                                ypos 0.7
                                thumb Frame("tb maintenance", xsize=xres(12), ysize=yres(24))
                                thumb_offset xres(3)
                                left_gutter xres(6)
                                right_gutter xres(6)
                                value FieldValue(brothel, "maintenance", brothel.max_help)
                                hovered tt.Action(__("Pay a maintenance team to clean up your brothel. And boy, does it get messy in there..."))

                            $ maint_bonus= brothel.get_effect("change", "maintenance")
                            if maint_bonus != 0:
                                $ text1 = " ({color=[c_green]}+" + str(maint_bonus) + __("{/color} from girls/effects)")
                            else:
                                $ text1 = ""
                            $ text2 = brothel.get_maintenance_cost()

                            textbutton __("[brothel.maintenance]  cleaners") + text1 background None text_size res_font(14) xpos 0.6 ypos 0.7 ypadding 6

                        hbox xfill True spacing 10:

                            vbox spacing 6 xsize xres(180):
                                text "Estimated customers" size res_font(14)
                                textbutton "{image=img_cust} %i" % brothel.customer_count style "inv_no_padding" action NullAction() tooltip brothel.count_customers_description()

                            vbox spacing 6 xsize xres(150):
                                text "威胁等级" size res_font(14)
                                textbutton brothel.estimate_threat_level(caps=True) style "inv_no_padding" action NullAction() tooltip "青楼当前的威胁等级为" + brothel.estimate_threat_level() + "。威胁等级受保安和你的力量属性影响。"

                            vbox spacing 6 xsize xres(200):
                                hbox spacing 10:
                                    text "Dirt level" size res_font(14)
                                    textbutton "Clean up" xmargin 10 ymargin 0 ypadding 6 text_size res_font(14):
                                        if brothel.get_clean_up_cost() > 0:
                                            action Return(("clean up", ""))
                                        tooltip "购买清洁用品，叫希露和保洁把你的青楼清洁干净 (彻底清洁需要花费: %s 金币)" % str(brothel.get_clean_up_cost())
                                textbutton str(round_int(brothel.dirt)) + " {size=-4}(-" + str_int(brothel.get_maintenance()) + ")" style "inv_no_padding" action NullAction() tooltip maintenance_desc[brothel.get_cleanliness()] yoffset -12


        hbox:
            xalign 0.0
            yalign 1.0
            spacing xres(24)
            xfill True
            yfill False

            $ tb_x = 120 # Base thumbnail width for room buttons

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

                    hbox spacing xres(6):
                        text "{b}女孩卧室{/b}" size res_font(18) xalign 0.0 yalign 0.5 drop_shadow (2, 2)

                        $ ttip = __("Upgrade all your bedrooms for ") + str(brothel.get_room_upgrade_price(brothel.bedrooms)) + __(" gold. Upgraded bedrooms are more comfortable for girls and customers alike.")
                        textbutton "▲{image=img_gold}" text_font "1.ttf" ysize yres(24):
                            xalign 0.5
                            yalign 0.5
                            text_size res_font(14)
                            if brothel.bedroom_type.level < brothel.maxupgrade:
                                action renpy.curried_invoke_in_new_context(brothel.upgrade_bedrooms)
                            tooltip ttip

                    frame background c_ui_dark:

                        has vbox spacing 6

                        if brothel.bedrooms < brothel.get_maxbedrooms():
                            $ text1 = __("Add a new bedroom to your brothel for {b}") + str(brothel.get_room_price()) +  __(" gold{/b}. This brothel can only have a maximum of {b}") + str(brothel.get_maxbedrooms()) +  __(" bedrooms{/b}.")
                        elif district.rank < 5:
                            $ text1 = __("You cannot add any more bedrooms until you move to another brothel.")
                        else:
                            $ text1 = __("You have reached the maximum number of bedrooms.")

                        button style "inv_no_padding" action NullAction():
                            tooltip text1
                            button:
                                insensitive_background c_darkgrey + "E5"
                                at alpha_transform
                                tooltip text1

                                if brothel.bedrooms < brothel.get_maxbedrooms():
                                    action renpy.curried_invoke_in_new_context(brothel.add_room) ## PRAISE BE TO ASCEAI Never would have found this on my own

                                vbox:
                                    spacing 3

                                    fixed:
                                        fit_first True

                                        add brothel.get_bedroom_pic(xres(tb_x), yres(tb_x*3/4)) # idle_alpha 0.66 hover_alpha 1.0
                                        text "{image=img_girl}%i" % len(MC.girls) xalign 0.1 yalign 0.9

                                        if brothel.bedrooms < brothel.get_maxbedrooms():
                                            text "+" xalign 0.5 yalign 0.5 size res_font(36)

                                        text "[brothel.bedrooms]{size=-8}/" + str(brothel.get_maxbedrooms()) xalign 0.9 yalign 0.1

                                    text "[brothel.bedroom_type.name]" size res_font(14) xcenter 0.5

                frame:
                    background None
                    xalign 0.0
                    yalign 0.0
                    xfill False
                    yfill False

                    has vbox spacing 6

                    text "{b}私人卧室{/b}" size res_font(18) xalign 0.0 drop_shadow (2, 2)

                    frame background c_ui_dark:

                        has vbox spacing 6

                        button style "inv_no_padding" action NullAction():
                            tooltip brothel.master_bedroom.get_description()
                            at alpha_transform
                            button:
                                insensitive_background c_darkgrey + "E5"
                                tooltip brothel.master_bedroom.get_description()

                                if brothel.master_bedroom.level < brothel.rank:
                                    action renpy.curried_invoke_in_new_context(brothel.upgrade_master_bedroom)

                                vbox:
                                    spacing 3

                                    fixed:
                                        fit_first True

                                        add brothel.master_bedroom.get_pic(xres(tb_x), yres(tb_x*3/4), proportional=False) # idle_alpha 0.66 hover_alpha 1.0

                                        if brothel.master_bedroom.level:
                                            text "Lv. %i{size=-8}/%i" % (brothel.master_bedroom.level , brothel.rank) xalign 0.9 yalign 0.1
                                            hbox xalign 0.1 yalign 0.95:
                                                for girl in brothel.master_bedroom.girls:
                                                    button background c_white yalign 0.5 xmargin 2 ymargin 0 xpadding 1 ypadding 1:
                                                        action NullAction()
                                                        tooltip girl.fullname + __(" is currently assigned to the master bedroom.")
                                                        add girl.portrait.get(*res_tb(20)) alpha 1.0

                                        if brothel.master_bedroom.level < brothel.rank:
                                            text "+" xalign 0.5 yalign 0.5 size res_font(36)

                                    text brothel.master_bedroom.name size res_font(14) xcenter 0.5


            frame:
                background None
                xpadding 6
                ypadding 6
                xalign 0.5
                yalign 0.0
                xfill False
                yfill False

                has vbox
                spacing 6

                text "{b}营业场所{/b}" size res_font(18) xalign 0.0 drop_shadow (2, 2)

                frame:
                    background c_ui_dark
                    has hbox

                    for room_name in all_common_rooms:

                        $ room = brothel.rooms[room_name]

                        button action NullAction() tooltip room.get_description():
                            background None
                            xpadding 1
                            ypadding 1
                            button:
                                xpadding 6
                                ypadding 6
                                insensitive_background c_darkgrey + "E5"
                                at alpha_transform

                                if room.level < district.rank:
                                    action Return(("add_room", room))
                                    tooltip room.get_description()

                                vbox:
                                    spacing 3

                                    fixed:
                                        fit_first True
                                        add room.pic.get(xres(tb_x), yres(tb_x*3/4)) # idle_alpha 0.66 hover_alpha 1.0
                                        if not brothel_firstvisit:
                                            text "Lv. %i{size=-8}/%i" % (room.level, district.rank) xalign 1.0
                                        if room.level:
                                            text "{image=img_cust} %i" % room.cust_limit xalign 0.1 yalign 0.9
                                        if room.level < district.rank:
                                            text "+" xalign 0.5 yalign 0.5 size res_font(36)

                                    text __(room.name.capitalize()) size res_font(14) xcenter 0.5


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

        text "工 匠" bold True xalign 0 yalign 0

        hbox spacing 6 xfill True ysize yres(120):
            add "side carpenter" zoom 0.8 yalign 0.5

            if not brothel.current_building:
                $ text1 = __("Oh, hi. Got a new job for me?")
            else:
                $ text1 = __("I'm still working on that ") + __(brothel.current_building.name) + __(". You should come back later.")

            text text1 xsize 0.4 yalign 0.5 size res_font(18) justify True italic True

            vbox xsize 0.4 yfill True xalign 1.0:
                text "资源储备" drop_shadow (2, 2) size res_font(18)
                frame xfill True yfill True background c_ui_brown xpadding 0 ypadding 0:
                    use resource_tab(y=0.0, sz=24)

            vbox xsize 0.6 yfill True xalign 1.0:
                text "建筑序列" drop_shadow (2, 2) size res_font(18)
                frame xfill True yfill True background c_ui_brown:
                    if brothel.current_building:
                        $ dur = brothel.current_building.duration - (calendar.time - brothel.started_building)
                        button xfill False yfill False xalign 0.5 yalign 0.5 background None:
                            action NullAction()
                            tooltip (brothel.current_building.description + "\n" + str(dur) + __(" day(s) to complete."))
                            add brothel.current_building.pic.get(*res_tb(50)) xalign 0.5 yalign 0.5
                            text str(dur) + __("d") xalign 1.0 yalign 0.0 size res_font(18)
                    else:
                        text "没有正在建造或升级的设施。" italic True size res_font(14)

        text brothel.name + __("'s Decoration and Furniture") drop_shadow (2, 2) size res_font(18)

        if brothel.furniture:
            frame xfill True background c_ui_brown:
                has hbox spacing 6 box_wrap True
                for furn in brothel.furniture:
                    button background c_ui_brown action NullAction() tooltip furn.description xsize xres(52) ysize yres(44) xpadding 0 ypadding 0:
                        add furn.pic.get(xres(48), yres(40)) xalign 0.5 yalign 0.5

        text "设施菜单" drop_shadow (2, 2) size res_font(18)

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
                        text "{b}" + __(misc_name_dict[type.capitalize()]) + "{/b} - {i}" + __(description) size res_font(14)
                        frame xfill True background c_ui_brown:
                            hbox spacing 6 box_wrap True:
                                for furn in builds:
                                    if furn.duration < 2:
                                        $ text2 = __(furn.description) + " (" + str(furn.duration) + __(" day to complete).")
                                    else:
                                        $ text2 = __(furn.description) + " (" + str(furn.duration) + __(" days to complete).")
                                    button xsize xres(110) ysize yres(90) xpadding 2 ypadding 2:
                                        action Return(furn)
                                        tooltip text2
                                        at alpha_transform
                                        add furn.pic.get(xres(90), yres(70)) xalign 0.5 ypos 0.05 # hover_alpha 1.0 idle_alpha 0.8
                                        button xalign 0.5 yalign 1.0 xpadding 0 ypadding 0 background c_ui_brown xfill True:
                                            action Return(furn)
                                            tooltip text2
                                            use resource_tab(furn.cost, sp=1)
                                        text str(furn.duration) + __("d") xalign 0.95 yalign 0.05 size res_font(18)
#                        else:
#                            text "You have built every available " + type +"." size res_font(14) italic True
                    text "" size res_font(8)


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

        if NPC_carpenter.active:
            vbox xsize xres(320):
                text "{b}顾客占比{/b}" size res_font(18) yalign 0.0 drop_shadow (2, 2)

                frame xpadding xres(10) ypadding yres(10) xfill True yfill True:
                    has vbox
                    text "选择来青楼消费的顾客群体占比 (增加青楼的装饰吸引更多种类的客人)" size res_font(14) italic True color c_brown
                    null height yres(6)
                    vbox spacing yres(6):
                        for pop in all_populations:
                            hbox spacing 6:
                                button style "inv_no_padding" xalign 0.0 yalign 0.5:
                                    action NullAction()
                                    if brothel.get_effect("allow", pop.name):
                                        add pop.get_pic(*res_tb(40))
                                        tooltip pop.description
                                    else:
                                        add pop.get_pic(*res_tb(40)) at desaturate
                                        tooltip __("You must build new decoration at the Carpenter's Wagon to attract this population.")

                                if brothel.get_effect("allow", pop.name):
                                    vbox spacing yres(6):
                                        $ total_budget, ent_budget, wh_budget = pop.get_average_budgets(description=True)
                                        hbox spacing 6 xalign 0.0:
                                            bar thumb Frame("tb empty", xsize=xres(9), ysize=yres(18)) xsize xres(100) ysize yres(18) yalign 0.0 value FieldValue(pop, "weight", 5, action=Function(brothel.update_customer_count))
                                            text attract_pop_dict[pop.weight] color c_brown size res_font(14) yalign 1.0
                                        textbutton "平均预算: %s 金币" % total_budget xalign 0.0 yalign 1.0 xmargin 0 xpadding 0 ymargin 0 ypadding 0 background None text_color c_prune text_size res_font(14) action NullAction() tooltip "This is the average {b}maximum budget{/b} for %s. (%s for entertainment, %s for whoring)" % (misc_name_dict[pop.name], ent_budget, wh_budget)
            vbox xsize xres(320):
                text "{b}顾客设置{/b}" size res_font(18) yalign 0.0 drop_shadow (2, 2)
                frame xfill True xpadding xres(10) ypadding yres(10):
                    has vbox
                    text "改变客户对娱乐和性行为的偏好（升级更多设施以提升影响效果）" size res_font(14) italic True color c_brown
                    null height yres(6)

                    vbox spacing yres(6):
                        for target in (all_jobs, all_sex_acts):
                            vbox ysize 0.5 spacing 6:
                                for pref in target:
                                    hbox spacing 6:
                                        textbutton pref.capitalize() xsize xres(120) ypadding 5 text_size res_font(18) yalign 0.5:
                                            action NullAction()

                                            if brothel.get_effect("allow", pref + " preference"):
                                                tooltip __("Use this setting to change your customers' preference for ") + pref + __(" up to +") + str(50*brothel.get_effect("allow", pref + " preference")) + "%."
                                            else:
                                                background "#CCB8A0"
                                                text_color c_white
                                                tooltip __("You must build new furnishing at the Carpenter's Wagon to change ") + pref + __(" preference.")

                                        if brothel.get_effect("allow", pref + " preference"):

                                            bar thumb "tb empty" xsize xres(100) xpos 0 yalign 0.0 value DictValue(game.customer_preference_weight, pref, brothel.get_effect("allow", pref + " preference"), action=Function(brothel.update_customer_count))

                                            if game.customer_preference_weight[pref]:
                                                text percent_text(0.5*game.customer_preference_weight[pref]) color c_brown size res_font(14) yalign 0.5
                                            else:
                                                text "" size res_font(14) yalign 0.5

                text "" size res_font(22)
                text "{b}匹配设置{/b}" size res_font(18) yalign 0.0 drop_shadow (2, 2)

                frame ysize yres(150) xpadding xres(10) ypadding yres(10) xfill True:
                    has vbox spacing 6

                    text "选择女孩与顾客的匹配策略。" size res_font(14) italic True color c_brown

                    if game.matching_priority == "rank":
                        $ text1 = "顾客会尽可能地由符合他身份地位的女孩服务。"
                    elif game.matching_priority == "act":
                        $ text1 = "顾客会尽可能地由符合他兴趣或性癖的女孩服务。"

                    textbutton "根据 %s 匹配" % misc_name_dict[game.matching_priority] text_size res_font(18) xsize xres(100) action ToggleField(game, "matching_priority", true_value="rank", false_value="act")

                    text text1 size res_font(14) color c_prune


            vbox xsize xres(320):

                if [f for f in brothel.furniture if f.can_deactivate]:
                    text "{b}特殊设置{/b}" size res_font(18) yalign 0.0 drop_shadow (2, 2)

                    frame ysize yres(200) xpadding xres(10) ypadding yres(10) xfill True:
                        text "激活或关闭设施的特殊效果" size res_font(14) italic True color c_brown

                        hbox box_wrap True:
                            for furn in [f for f in brothel.furniture if f.can_deactivate]:

                                button xsize xres(56) ysize yres(56) action Function(furn.toggle) tooltip __("Click here to activate or deactivate %s.\n%s ({b}%s{/b})") % (furn.name, get_description("", furn.effects), {True: "active", False: "inactive"}[furn.active]):

                                    add furn.pic.get(*res_tb(50)) xalign 0.5 yalign 0.5

                                    if not furn.active:
                                        text "X" color c_crimson size res_font(48) xalign 0.5 yalign 0.5
                    text "" size res_font(22)

                # This will unlock with the 'billboard' upgrade
                if brothel.get_effect("special", "advanced advertising"):
                    text "{b}广告设置{/b}" size res_font(18) yalign 0.0 drop_shadow (2, 2)

                    frame ysize yres(200) xpadding xres(10) ypadding yres(10) xfill True:
                        has vbox

                        text "除了提高你的青楼声誉，广告女郎还能增加客流量和消费预算（收集更多服装，可以提高宣传效果）。" size res_font(14) italic True color c_brown
                        null height yres(6)
                        hbox spacing xres(3):
                            vbox xsize xres(100):
                                text "顾客" size res_font(14) bold True color c_brown yalign 1.0
                                text percent_text(brothel.get_adv_setting("attraction")) + " to customer attraction" size res_font(14) color c_brown
                            bar thumb "tb empty" xsize xres(100) xpos 0 yalign 0.0 value FieldValue(brothel, "advertising_setting", range=4, offset=-2, action=Function(brothel.update_customer_count)) tooltip __("Use this setting to adjust the focus between customer attraction (how many customers will come to the brothel) and customer budget (the maximum amount of gold each customer is able to spend).")
                            vbox xsize xres(100):
                                text "预算" size res_font(14) bold True color c_brown yalign 1.0
                                #text str(brothel.advertising_setting)
                                text percent_text(brothel.get_adv_setting("budget") / brothel.max_help) + __(" to customer budget") size res_font(14) color c_brown
                    text "" size res_font(22)

                text "{b}市场分析{/b}" size res_font(18) yalign 0.0 drop_shadow (2, 2)
                frame xfill True xpadding xres(10) ypadding yres(10):
                    has vbox spacing 12
                    text brothel.count_customers_description() color c_prune size res_font(14)
                    text brothel.count_budget_description() color c_prune size res_font(14)




## MATCHMAKING SCREENS

screen matchmaking(girls, customers, match_list, context="job"): # Where match list is a list of tuples (girl, customer)

    tag show_screen

    key "mouseup_1" action Return()
    key "mouseup_3" action Return()
    if persistent.can_skip_reports:
        key ['K_LCTRL', 'K_RCTRL', 'repeat_K_LCTRL', 'repeat_K_RCTRL'] action Return()
    use close(Return(), "next")

    default t = 0
    default n = 0
    default idle_customers = sorted(customers, key= lambda x : x.rank)
    default girl_customers = defaultdict(list)
    default job_customers = defaultdict(int)
    default cust_act = defaultdict(str)
    default load_txt = __(" (matching...)")

    if match_list:
        $ tick = min(1.5 / len(match_list), 0.2) # Takes maximum 1.5 seconds to display all customer matches

    frame background c_ui_dark:
        xalign 0.0
        yalign 0.05
        xsize int(0.95*config.screen_width)
        ysize yres(615)
        left_margin 6
        ymargin 2
        xfill True
        yfill True

        has vbox spacing 10

        if context == "job":
            $ text1 = __("Entertainment Phase")
        else:
            $ text1 = __("Whoring Phase")

        text "[text1!t]" + load_txt xalign 0.0 bold True drop_shadow (2, 2) #color c_prune

        frame xfill True ymaximum yres(160) right_margin 10:
            has hbox spacing 20
            add brothel.get_pic(*res_tb(100))

            vbox spacing 6:
                text __("Waiting customers ({image=img_cust} %i)/%i") % (len(idle_customers), len(customers)) size res_font(18) color c_brown

                if customers:
                    vpgrid rows 4 spacing 3 ymaximum yres(160):
                        mousewheel True
                        draggable True
                        scrollbars "horizontal"
                        allow_underfull True

                        if not idle_customers:
                            text __("All customers have been assigned.") size res_font(12) italic True yalign 0.5 color c_brown
                        else:
                            for cust in idle_customers:
                                button yalign 0.5 xmargin 0 xpadding 0 ymargin 0 ypadding 0 background None action NullAction() tooltip cust.get_description("idle " + context):
                                    if cust.crazy:
                                        add cust.get_pic(*res_tb(25)) at red_saturate
                                        at blink
                                    else:
                                        add cust.get_pic(*res_tb(25))

                else:
                    text __("No customers.") size res_font(12) italic True yalign 0.5 color c_brown



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
                                    add room.get_pic(*res_tb(100))

                                    vbox spacing 6:
                                        text __(room.name.capitalize()) + " ({image=img_cust} %i/%i)" % (job_customers[job], room.cust_limit) size res_font(18) color c_brown

                                        vbox spacing 3:
                                            for girl in [g for g in girls if g.job == job]:
                                                hbox ysize yres(25) yalign 0.5:
                                                    button xmargin 0 xpadding 0 ymargin 0 ypadding 0 xsize xres(45) yalign 0.5 background None action NullAction() tooltip  "{b}" + girl.fullname + ": " + girl.job.capitalize() + __(" (capacity: %s/%s).{/b}") % (str(len(girl_customers[girl])), str(girl.get_max_cust_served())):
                                                        add girl.portrait.get(*res_tb(25)) xalign 0.5 yalign 0.5

                                                    frame ysize yres(25) ymargin 0 ypadding 1 background c_ui_brown xfill True:
                                                        has hbox spacing 3 yalign 0.5
                                                        for cust in girl_customers[girl]:
                                                            button xmargin 0 xpadding 0 ymargin 0 ypadding 0 background None action NullAction() tooltip cust.get_description(job): #  xalign 0.0 yalign 0.5 yanchor 0.5
                                                                if cust.crazy:
                                                                    add cust.get_pic(*res_tb(22)) at red_saturate
                                                                    at blink
                                                                else:
                                                                    add cust.get_pic(*res_tb(22))
                                                        if not girl_customers[girl]:
                                                            text __("No customers.") size res_font(12) italic True yalign 0.5

            elif context == "whore":
                frame xfill True yfill False:
                    has vbox spacing 3
                    $ room = brothel.bedroom_type

                    text __("Bedrooms") + " ({image=img_cust} %i)" % job_customers["whore"] size res_font(18) color c_brown
                    hbox spacing 20:
                        add room.get_pic(*res_tb(100))

                        vbox spacing 3 box_wrap True:
                            for girl in girls:
                                hbox ysize yres(25) yalign 0.5:
                                    button xmargin 0 xpadding 0 ymargin 0 ypadding 0 xsize xres(45) yalign 0.5 background None action NullAction() tooltip "{b}" + girl.fullname + ": " + girl.job.capitalize() + __(" (interactions: %s/%s).{/b}") % (str(girl.get_max_interactions()-girl.interactions), str(girl.get_max_interactions())):
                                        add girl.portrait.get(*res_tb(25)) yalign 0.5

                                    frame ysize yres(25) ymargin 0 ypadding 1 background c_ui_brown xfill True xmaximum xres(220):
                                        has hbox spacing 3 yalign 0.5
                                        for cust in girl_customers[girl]:
                                            button xmargin 0 xpadding 0 ymargin 0 ypadding 0 background None action NullAction() tooltip cust.get_description(cust.got_sex_act): #  xalign 0.0 yalign 0.5 yanchor 0.5
                                                if cust.crazy:
                                                    add cust.get_pic(*res_tb(22)) at red_saturate
                                                    at blink
                                                else:
                                                    add cust.get_pic(*res_tb(22))
                                        if not girl_customers[girl]:
                                            text __("No customers.") size res_font(12) italic True yalign 0.5

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
        $ load_txt = __(" (done)")



screen customer_satisfaction(customers, old_rep, rep_chg):

    tag show_screen

    zorder 5

    default t = 0
    default displayed_rep = round_int(old_rep)
    default total_change = 0
    default displayed_customers = []

    key "mouseup_1" action Return()
    key "mouseup_3" action Return()
    if persistent.can_skip_reports:
        key ['K_LCTRL', 'K_RCTRL', 'repeat_K_LCTRL', 'repeat_K_RCTRL'] action Return()
    use close(Return(), "next")

    if persistent.dark_night_UI:
        $ tcolor = c_white
    else:
        $ tcolor = c_brown

    frame:
        xalign 0.0
        yalign 0.0
        xsize int(0.95*config.screen_width)
        ysize yres(615)
        left_margin 6
        ymargin 2
        if persistent.dark_night_UI:
            background c_ui_darker

        has vbox spacing 10

        $ text1 = __("Brothel reputation: %s") % displayed_rep

        if len(displayed_customers) == len(customers):
            $ text1 += " (%s)" % plus_text(total_change)
        else:
            timer 0.05 repeat True action SetScreenVariable("t", t + 0.05)

        # text text1 xalign 1.0 bold True color c_prune

        text "[text1!t]" xalign 0.0 bold True drop_shadow (2, 2)

        hbox spacing 10:
            textbutton __("Customer") style "inv_no_padding" xsize xres(80) text_bold True text_color tcolor text_size res_font(14)
            textbutton __("Satisfaction") style "inv_no_padding" xsize xres(100) text_bold True text_color tcolor text_size res_font(14)
            textbutton __("Rep.") style "inv_no_padding" xsize xres(100) text_bold True text_color tcolor text_size res_font(14)
            textbutton __("Comment") style "inv_no_padding" xsize xres(100) text_bold True text_color tcolor text_size res_font(14)

        viewport:
            mousewheel "change"
            draggable True
            scrollbars True
            xfill True
            yfill True

            vbox spacing 3:

                for cust in displayed_customers:
                    hbox spacing 10:
                        button xsize xres(80) xalign 0.5 xmargin 0 xpadding 0 ymargin 0 ypadding 0 background None action NullAction() tooltip cust.get_description("end"): #  xalign 0.0 yalign 0.5 yanchor 0.5
                            add cust.get_pic(*res_tb(25)) xalign 0.5

                        $ chg = cust.reputation_change

                        if chg > 0:
                            $ col = c_emerald
                        elif chg < 0:
                            $ col = c_crimson
                        else:
                            $ col = None

                        fixed fit_first True ypos -0.2 xsize xres(100):
                            bar xsize xres(100) value cust.base_rating range 8 thumb None ypos 0.4: # AnimatedValue(value=cust.base_rating, range=8, delay=1.0) Animated value doesn't work :/
                                if col:
                                    left_bar Frame(im.Twocolor("UI/cryslider_full.webp", col, col), 12, 0)
                                    right_bar Frame(im.Twocolor("UI/cryslider_empty.webp", col, col), 12, 0)

                            text "I" color c_brown size res_font(20) xpos xres(3) + (cust.rank-1)*xres(95/8) ypos 0.5

                        textbutton plus_text(chg) xsize xres(80) xalign 0.5 yalign 0.65 text_size res_font(14) text_color c_brown text_bold True

                        frame ysize yres(20) yalign 0.5 ymargin 0 ypadding 1 xsize xres(600):
                            if persistent.dark_night_UI:
                                background None
                            else:
                                background c_ui_brown
                            text "[cust.reputation_comment!t]" size res_font(14):
                                if persistent.dark_night_UI:
                                    color c_softpurple
                                else:
                                    color c_brown

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
                $ textHH = __("Headhunter")
                $ textHH2 = __("The headhunter is back with your prize!")

                if not game.interacting_with_headhunter:
                    textbutton textHH:
                        xalign 0.5
                        yalign 0.0825
                        text_size 36
                        text_font "CHOWFUN_0.TTF"
                        action Jump("headhunter_delivers")
                        hovered tt.Action(textHH2)

            else:
                $ textHH = __("Headhunter: [game.headhunter_time] days")
                $ textHH2 = __("The headhunter will be back in [headhunter_time] days.")

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

    button background None action (Hide("brothel_report"), ToggleVariable("always_show_brothel_report"), SelectedIf(always_show_brothel_report)) xalign 0.5 xmargin 25 ypos 0.1 :
        if not always_show_brothel_report:
            tooltip __("Click to keep the brothel report showing at all times.")
            hovered (Show("brothel_report"))
            unhovered Hide("brothel_report")
        else:
            tooltip __("Click to hide the brothel report.")

        hbox xalign 0.0 spacing 10:
            frame xalign 0.0 xsize xres(25) ysize yres(25):
                style "contrast_button"
                hover_background Frame("orange_button")
                selected_background Frame("darkorange_button")

                if always_show_brothel_report:
                    text "✓" font "1.ttf" size res_font(14) xalign 0.5 yalign 0.5
                else:
                    text " " size res_font(14) xalign 0.5
            text "Show brothel report" size res_font(14) xalign 0.0 yalign 0.5 drop_shadow (2, 2)


screen brothel_report():

    tag brothel_report

    if brothel.get_cleanliness() in ("disgusting", "fire"):
        default side_pic = "side sill sad"
        default shown_tip = "Master!!! " + brothel.name + " is very dirty... Please do something!"
    elif calendar.time == 1:
        default side_pic = "side sill happy"
        default shown_tip = "Welcome to your new brothel, Master! I'm sure you will be a great manager!"
    elif logs[calendar.time-1] and logs[calendar.time-1].net < 0:
        default side_pic = "side sill sad"
        default shown_tip = "主人!!! " + brothel.name + "正在亏损...我们该怎么办?"
    else:
        default side_pic = "side sill happy"
        default shown_tip = "{color=[c_lightblue]}你知道吗? {/color}%s" % daily_tip

    frame:
        xanchor 1.0
        if screen_is_wide:
            xalign 0.85
            xsize 0.7
        else:
            xalign 0.775
            xsize 0.75
        ypos 0.15
        ysize 0.8
        xpadding xres(10)
        ypadding yres(10)

        has vbox spacing yres(10) xfill True

        hbox spacing xres(10):
            add side_pic zoom 0.5 xalign 0.0 
            textbutton "下一个提示" text_size 18 xalign 0.0 yalign 0.5:
                if always_show_brothel_report:
                    action SetLocalVariable("shown_tip", "{color=[c_lightblue]}你知道吗? {/color}%s" % rand_choice(random_tips))
            text shown_tip xalign 0.0 yalign 0.5 size res_font(18) justify True italic True xsize 0.8 color c_brown
            #? Why does the textbutton 'dance' around when changing tips? Investigate

        hbox spacing xres(20) xfill True yfill False:

            vbox:
                xsize 0.4
                xfill True
                yfill False

                text "昨 天" color c_prune

                text "" size res_font(14)

                if calendar.time > 1 and logs[calendar.time-1]:
                    text logs[calendar.time-1].get_day_report() size res_font(14) color c_brown

                    textbutton "显示昨晚的报告" xsize xres(250) ypadding 5 text_size res_font(14) xalign 0.5:
                        if always_show_brothel_report:
                            action (Show("previous_night_log", log=logs[calendar.time-1]))
                    textbutton "显示满意度报告" xsize xres(250) ypadding 5 text_size res_font(14) xalign 0.5:
                        if always_show_brothel_report:
                            action Call("latest_customer_satisfaction")

                else:
                    text "没有可报告的事件" size res_font(14) italic True color c_brown

            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                xfill True
                yfill False

                has vbox
                xfill True
                yfill False

                text "今 天" color c_prune #关联NPC姓名，不作标记

                text "" size res_font(14)

                text get_next_day_report() size res_font(14) color c_brown

                text "" size res_font(14)

                text brothel.get_ASM_report() size res_font(14) color c_brown

                text "" size res_font(14)

                text get_warnings() size res_font(14) color c_brown

screen previous_night_log(log):
    modal True

    key "mouseup_3" action (Hide("previous_night_log"))

    use dark_filter

    frame ypos 0.1 xpadding 12 ypadding 12:
        use night_log(log, use_filter=True)

    use close(Hide("previous_night_log"))


## Yes / No Confirmation (used for buying, selling...)


screen yes_no(message, yes_caption="Yes", no_caption="No", col=c_white, bg=c_ui_darker):

    modal True
    zorder 10

    key "mouseup_3" action (Return(False))

    frame:
        style_group "yesno"

        xfill False
        xmaximum 0.8
        xpadding .05
        xalign 0.5
        yalign 0.5
        ypadding 25
        ymargin 10
        background bg

        has vbox:
            xalign .5
            yalign .5
            spacing 25

        label _(message):
            xalign 0.5
            text_size res_font(18)
            text_color col

        hbox:
            xalign 0.5
            spacing 100

            textbutton __(yes_caption) action Return(True)
            textbutton __(no_caption) action Return(False)


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
            allow_underfull True
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
                        add pic.get(*res_tb(200)) xalign 0.5

                    elif pic_size == "small":
                        add pic.get(*res_tb(60)) xalign 0.5

                text _(message):
                    xalign 0.5
                    size res_font(18)

                    if not dark:
                        color c_brown
                    else:
                        color c_white

        hbox:
            xalign 0.5
            spacing 100

            textbutton __("Ok") action Return(True)


# show_img, show_event and show_sex_event do basically the same thing and have finally been merged into show_event. Hurray!

screen show_img(img, bg=None): # Mostly used to show full screen pictures with no background, such as brothel pics

    layer "master" # Shown on master layer (watch out, no interactivity)

    use show_event(img, bg=bg, xs=1.0, ys=1.0, can_ignore=False)

    # tag show_screen
    #
    # if img:
    #     if isinstance(img, ProportionalScale):
    #         on "show" action Function(unlock_pic, img.imgname, _update_screens=False) # This is how the game tracks that this particular picture has been seen.
    #     elif is_string(img):
    #         on "show" action Function(unlock_pic, img, _update_screens=False) # This is how the game tracks that this particular picture has been seen.
    #
    #     add img

screen show_event(event_pic, x = None, y = None, proportional = True, bg = "black", xs = 1.0, ys = 0.8, xs_bg = None, ys_bg = None, can_ignore=True):

    # event_pic can be a Picture object, a ProportionalScale object, or a string
    # x and y refer to event_pic maximum size in pixels. Use xs and ys to specify a proportional size. x and y override xs and ys.
    # use xs_bg and ys_bg to specify a different size for the BG. By default it is the same as xs and ys

    tag show_screen

    zorder 0

    layer "master" # This excludes this screen from being hidden when middle-click is used

    # Shortcuts and show statements

    if can_ignore:
        key ['K_DELETE'] action Function(toggle_ignore_pic, pic=event_pic)

    on "show" action Function(unlock_pic, pic=event_pic) # This is how the game tracks that this particular picture path has been seen (gallery).

    # size calculations

    if not x:
        $ x = int(config.screen_width*xs)
    if not y:
        $ y = int(config.screen_height*ys)

    if not xs_bg:
        $ xs_bg = x
    if not ys_bg:
        $ ys_bg = y

    frame:
        style "inv_no_padding"
        if bg:
            if isinstance(bg, Picture):
                background bg.get(x=xs_bg, y=ys_bg, proportional=False)
            elif isinstance(bg, ProportionalScale):
                background Frame(bg)
            elif is_string(bg):
                background Frame(bg)
        xalign 0.5
        yalign 0.5
        xfill True
        yfill True
        xsize xs_bg
        ysize ys_bg

        if event_pic:
            fixed xsize x ysize y xalign 0.5 yalign 1.0:
                if isinstance(event_pic, Picture):
                    add event_pic.get() xalign 0.5 yalign 1.0 fit "contain"
                elif isinstance(event_pic, ProportionalScale):
                    add event_pic xalign 0.5 yalign 1.0 fit "contain"
                elif is_string(event_pic):
                    add event_pic xalign 0.5 yalign 1.0 fit "contain"

            if debug_mode:
                frame background c_ui_dark:
                    has vbox
                    text __("Attempt: ") + str(game.last_pic["attempts"]) size res_font(14)
                    text __("Search tags: ") + and_text(game.last_pic["tags"]) size res_font(14)
                    text __("AND tags: ") + and_text(game.last_pic["and_tags"]) size res_font(14)
                    text __("AND NOT tags: ") + and_text(game.last_pic["not_tags"]) size res_font(14)
                    # text "y: %i ys: %s ys_bg: %s" % (y, str_dec(ys), str_dec(ys_bg))


screen show_sex_event(event_pic, bg = c_ui_dark): # Mostly used for interactions, wide format.

    use show_event(event_pic, bg=bg, x=res_event_width, y=res_event_height, xs=1.0, ys=0.8)

    # key ['K_DELETE'] action Function(toggle_ignore_pic, event_pic.path)
    #
    # if event_pic:
    #     on "show" action Function(unlock_pic, event_pic.path) # This is how the game tracks that this particular picture has been seen.
    #
    #
    # zorder 0
    #
    # default show_log = False
    #
    #
    # frame:
    #     background bg
    #     xalign 0.0
    #     yalign 0.0
    #     xsize 1.0
    #     ysize 0.8
    #     left_margin 6
    #     ymargin 6
    #     xfill True
    #     yfill True
    #
    #     if event_pic:
    #         add event_pic.get(res_event_width, res_event_height) xalign 0.5
    #
    #         if debug_mode:
    #             frame background c_ui_dark:
    #                 has vbox
    #                 text "Attempt: " + str(game.last_pic["attempts"]) size res_font(14)
    #                 text "Search tags: " + and_text(game.last_pic["tags"]) size res_font(14)
    #                 text "AND tags: " + and_text(game.last_pic["and_tags"]) size res_font(14)
    #                 text "AND NOT tags: " + and_text(game.last_pic["not_tags"]) size res_font(14)



## Shortcuts

screen shortcuts():

    zorder 100

    # Note: some keys like 'f', 'h', 'm', 's', 'v' are used natively by Ren'py and have been remapped to Shift+* when necessary (see 'BKinit_variables')

    key "noshift_K_h" action (SetVariable("selected_destination", "main"), Jump("teleport"))
    key "noshift_K_c" action (SetVariable("selected_destination", "main_character"), Jump("teleport"))
    key "noshift_K_g" action (SetVariable("selected_destination", "girls"), Jump("teleport"))
    key "noshift_K_b" action (SetVariable("selected_destination", "brothel"), Jump("teleport"))
    key "noshift_K_v" action (SetVariable("selected_destination", "districts"), Jump("teleport"))
    key "noshift_K_s" action (SetVariable("selected_destination", "shop"), Jump("teleport"))
    key "noshift_K_t" action (SetVariable("selected_destination", "postings"), Jump("teleport"))
    key "noshift_K_e" action (SetVariable("selected_destination", "end_day"), Jump("teleport"))
    key "noshift_K_o" action (SetVariable("selected_destination", "customer_options"), Jump("teleport"))
    key "noshift_K_k" action (SetVariable("show_spellbook", True), SetVariable("selected_destination", "main_character"), Jump("teleport"))
    key "K_F5" action QuickSave() #Set the F5 key in your keyboard to Quicksave when pressed
    key "K_F9" action QuickLoad(confirm=False)  #Same for F9 key

    if slavemarket.active:
        key "noshift_K_m" action (SetVariable("selected_destination", "slavemarket"), Jump("teleport"))
    if NPC_carpenter.active:
        key "noshift_K_w" action (SetVariable("selected_destination", "furniture"), Jump("teleport"))
    if farm.active:
        key "noshift_K_f" action (SetVariable("selected_destination", "farm"), Jump("teleport"))
    if selected_location:
        key "noshift_K_l" action (SetVariable("selected_destination", "visit_location"), Jump("teleport"))
    if farm.powers:
        key "noshift_K_p" action (SetVariable("selected_destination", "farm_powers"), Jump("teleport"))

## Close button

screen close(act, name="返回", ttip="Click to go back (or use right-click)."):

    textbutton name:

        background None

        xalign 1.0
        yalign 0.075
        xfill False
        yfill False
        xmargin 3

        text_size res_font(14)
        text_align 1.0
        text_color c_lightred
        text_hover_color c_red
        action act
        tooltip ttip




## ITEMS

# Inventory screens are located in BKitems.rpy

screen receive_item(it, msg, col=c_emerald):

    tag receive_item

    zorder 10

    button background c_ui_darker:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20

        action Return()
        tooltip "{i}" + it.base_description + "{/i}\n\n" + it.description

        has vbox
        xalign 0.5
        yalign 0.5
        spacing 20

        add it.get_pic(*res_tb(100)) xalign 0.5

        text msg color col size res_font(16) xalign 0.5 yalign 0.5


screen restock_button(merc, upgrade=False):

    hbox spacing 20 xalign 0.5 ypos 0.08 yanchor 0.0:

        if merc in city_merchants:
            $ restock_cost = shop_restock_cost["city merchants"][game.chapter]
        elif merc in minion_merchants:
            $ restock_cost = shop_restock_cost["minion merchants"][game.chapter]
        else:
            $ restock_cost = shop_restock_cost["shop"][game.chapter]

        textbutton __("Restock inventory") text_size res_font(18) tooltip __("Restock this shop's inventory for %s gold (available once a day).") % restock_cost:
            if merc.last_restock != calendar.time and MC.has_gold(restock_cost):
                action Return((True, "restock"))
            else:
                action Return((False, "restock"))

        if upgrade == True and merc.can_upgrade():
            $ chapter, cost, upgrade = shop_upgrades[merc.upgrade_level + 1]

            $ ttip = __("Upgrade this shop's inventory (+%s %s item%s) for %s %s.") % (str(upgrade[1]), upgrade[0], plural(upgrade[1]), str(cost[1]), cost[0])

            textbutton __("Upgrade shop") text_size res_font(18) tooltip ttip:
                if MC.has_resource(*cost):
                    action Return((True, "upgrade_shop"))
                else:
                    action Return((False, "upgrade_shop"))


screen inventory_filter(filters=inventory_filters["base"]):

    if MC.active_inv_filter not in filters:
        $ active_inv_filter = []

    vbox xfill False yfill False spacing 3:
        for filter in filters:
            frame xsize xres(38) ysize yres(38) xpadding 0 xmargin 0:
                button xalign 0.5 yalign 0.6 ysize yres(30) xpadding 0 xmargin 0 idle_background None:

                    action (SetField(MC, "active_inv_filter", filter), Function(renpy.restart_interaction), SetScreenVariable("left_length", max_item_shown), SetScreenVariable("right_length", max_item_shown))

                    if filter:
                        if filter == MC.active_inv_filter:
                            add "filter_" + filter
                        else:
                            add "filter_" + filter + "_unselect"
                        tooltip __("Show %s items.") % __(misc_name_dict[filter])
                    else:
                        if filter == MC.active_inv_filter:
                            add "filter_all"
                        else:
                            add "filter_all_unselect"
                        hovered tt.Action(__("Show all items."))



## GIRL BROWSER

screen girl_select(girl_list, orange = False, no_sched=False, action_button=None):

    frame:

        id "girl_select"

        background None

        xalign 0.5
        yalign 0.1
        xpadding 6
        ypadding 6
        xsize 0.45
        ysize 0.15
        xfill True
        yfill False

        if girl_list:
            key "K_LEFT" action (Function(select_previous_girl, girl_list), Hide("item_profile"))
            key "K_RIGHT" action (Function(select_next_girl, girl_list), Hide("item_profile"))

        hbox spacing 5 xalign 0.5:

            textbutton "<" ysize yres(120) yalign 0.5:
                if girl_list:
                    action (Function(select_previous_girl, girl_list), Hide("item_profile"), SetVariable("selected_item", None))

            frame:
                xsize xres(300)
                ysize yres(120)
                xfill True
                xalign 0.5
                ymargin 3

                if orange:
                    background c_orange + "AA"

                if girl_list and selected_girl:
                    frame background None xsize xres(280) ysize yres(120) xfill True yfill True ypadding 0 ymargin 0:

                        has hbox
                        spacing 6

                        frame style "inv_no_padding" xsize xres(100) ysize yres(100) xfill True yalign 0.5:
                            if selected_girl.portrait != None:
                                fixed fit_first True xalign 0.5 yalign 0.5:
                                    add selected_girl.portrait.get(*res_tb(90)) xalign 0.5 yalign 0.5

                                    $ badge = selected_girl.get_badge()
                                    if badge:
                                        add ProportionalScale(badge, *res_tb(40)) xalign 0.9 yalign 0.1

                        $ text1 = selected_girl.fullname + __("\nRank ") + rank_name[selected_girl.rank] + __(" - Level ") + str(selected_girl.level)

                        if not no_sched:
                            if selected_girl.job:
                                $ text1 += "\n" + __(selected_girl.job.capitalize())
                                if selected_girl.job in all_jobs and selected_girl.work_whore:
                                    $ text1 += __("/Whore")
                                $ sched = selected_girl.workdays[calendar.get_weekday()]

                            else:
                                $ text1 += __("\nNo job")
                                $ sched = 0


                            if selected_girl.away:
                                $ text1 += __(" (away)")
                            elif selected_girl.hurt > 0:
                                $ text1 += __(" (hurt)")
                            elif selected_girl.exhausted > 0:
                                $ text1 += __(" (tired)")
                            elif selected_girl.resting or sched == 0:
                                $ text1 += __(" (resting)")
                            elif sched == 50:
                                $ text1 += __(" (half-shift)")

                        text text1 size res_font(14) xalign 0.0 yalign 0.5 color c_brown

                    if action_button:
                        $ _caption, _action, _ttip = action_button
                        textbutton _caption action _action tooltip _ttip xalign 1.0

                elif girl_list:
                    $ selected_girl = girl_list[0]
                    $ renpy.restart_interaction()

                else:
                    text __("{i}No girls are available for this task{/i}") color c_brown size res_font(14) xalign 0.5 yalign 0.5

            textbutton ">" ysize yres(120) yalign 0.5:
                if girl_list:
                    action (Function(select_next_girl, girl_list), Hide("item_profile"), SetVariable("selected_item", None))


## START SCREEN

screen quick_start(def_panel = "MC"):

    modal True

    default panel = def_panel
    default ngps = NGP_settings
    default total_crystals = count_achievements()
    $ spent_crystals = sum(s.get_used() for s in ngps)

    vbox xalign 0.5 yalign 0.5 xsize int(0.95*config.screen_width):
        hbox xfill True:
            textbutton "主角" xsize xres(160) ysize yres(48) text_size res_font(24) text_selected_bold True action SelectedIf(panel == "MC") hovered SetScreenVariable("panel", "MC") tooltip "Create your Main Character."

            textbutton "难度" xsize xres(160) ysize yres(48) text_size res_font(24) text_selected_bold True action SelectedIf(panel == "diff") hovered SetScreenVariable("panel", "diff") tooltip "Change difficulty settings."

            textbutton "女孩" xsize xres(160) ysize yres(48) text_size res_font(24) text_selected_bold True action SelectedIf(panel == "mix") hovered SetScreenVariable("panel", "mix") tooltip "Choose your girl mixes."

            if persistent.new_game_plus or debug:
                textbutton "新周目" xsize xres(160) ysize yres(48) text_size res_font(24) text_selected_bold True action SelectedIf(panel == "extras") hovered SetScreenVariable("panel", "extras") tooltip "Access NewGame+ settings."

            button background None xsize xres(320) ysize yres(52) xalign 1.0:
                if GetTooltip():
                    $ ttip = GetTooltip()
                else:
                    $ ttip = ""
                text ttip size res_font(13) color c_white justify True

        frame xpadding 20 ypadding 20 xfill True ysize int(0.8*config.screen_height):
            has vbox xfill True spacing 20
            if panel == "MC":

                hbox spacing 30 xalign 0.5:
                    label _("Name: ")
                    input value FieldInputValue(MC, "name") length 20 color c_main bold True
#                     text "Name: " color c_brown yalign 0.5
#                     textbutton "[MC.name]" ysize yres(40) text_color c_white text_bold True action Call("MC_change_name")

                hbox spacing 30 xalign 0.5:
                    frame: # background c_orange:
                        has vbox

                        text __("Class") xalign 0.5 size res_font(18) bold True color c_prune

                        hbox spacing 10:
                            for cl in ["Warrior", "Wizard", "Trader"]:
                                button yalign 0.5 xpadding 0 action Function(MC.set_playerclass, cl) tooltip MC_playerclass_description[cl]:
                                    if MC.playerclass != cl:
                                        background None

                                    add Picture(path=playerclass_pics[cl]).get(*res_tb(40)) yalign 0.5:
                                        if MC.playerclass == cl:
                                            alpha 1.0
                                        else:
                                            alpha 0.3
                                            # hover_alpha 1.0

                    frame: # background c_purple:
                        has vbox

                        text __("Religion") xalign 0.5 size res_font(18) bold True color c_emerald

                        hbox spacing 10:
                            for god in ["Arios", "Shalia", None]:
                                button yalign 0.5 xpadding 0 action Function(MC.set_god, god) tooltip god_description[god]:
                                    if MC.god != god:
                                        background None

                                    add Picture(path=god_pics[god]).get(*res_tb(40)) yalign 0.5:
                                        if MC.god == god:
                                            alpha 1.0
                                        else:
                                            alpha 0.3
                                            # hover_alpha 1.0

                    frame xalign 0.5 yalign 0.5 ysize yres(76):
                        grid 4 1 yalign 0.5:
                            for stat in all_MC_stats:
                                button background None action NullAction() tooltip MC_stat_description[stat]:
                                    vbox xsize xres(100):
                                        text MC_stat_color[stat] % __(tl_cn(stat.capitalize(), misc_name_dict)) size res_font(18) xalign 1.0
                                        text MC_stat_color[stat] % int(MC.get_stat(stat, raw=True) + NGP_settings_dict[stat].get()) size res_font(24) xalign 1.0

                # hbox spacing 20 xalign 0.5:


                hbox xalign 0.5 spacing 30:
                    textbutton "<" ysize yres(120) yalign 0.5:

                        action Function(MC.change_pic, "previous")
                        tooltip __("Change your Main Character's picture.")


                    frame:
                        xalign 0.5
                        yalign 0.3
                        xfill False
                        yfill False
                        add MC.current_pic.get(int(config.screen_width*0.5), int(config.screen_height*0.5))

                    textbutton ">" ysize yres(120) yalign 0.5:

                        action Function(MC.change_pic, "next")
                        tooltip __("Change your Main Character's picture.")

            elif panel == "diff":
                hbox spacing 60:
                    frame ysize yres(240):
                        has vbox spacing 10 xalign 0.5 yalign 0.5
                        style_group "diff"
                        for diff in diff_list:
                            textbutton diff_name[diff] xsize xres(220) ysize yres(36) action (Function(game.set_difficulty, diff), SelectedIf(game.diff == diff)) tooltip diff_description[diff] text_selected_bold True

                    vbox spacing 6 box_wrap True:

                        $ y = len(diff_settings)

                        grid 2 y:
                            for ds in diff_settings:
                                if ds == "satisfaction":
                                    textbutton __(diff_setting_name[ds]) + ": " + plus_text(game.get_diff_setting(ds)) text_color c_brown background None text_size res_font(18) action NullAction() tooltip diff_setting_description[ds]
                                else: # percentage description
                                    textbutton __(diff_setting_name[ds]) + ": " + percent_text(game.get_diff_setting(ds), False) text_color c_brown background None text_size res_font(18) action NullAction() tooltip diff_setting_description[ds]

                                hbox:
                                    textbutton "-" text_size res_font(18) xsize xres(24) action Function(game.change_diff_setting, ds, -diff_settings_range[ds]["pace"]) # Trying to go around the prediction problem
                                    textbutton "+" text_size res_font(18) xsize xres(24) action Function(game.change_diff_setting, ds, diff_settings_range[ds]["pace"])

            elif panel == "mix":
                $ available_mixes = update_available_mixes()

                vbox spacing 20 xalign 0.05:
                    textbutton __("Active Girl mixes: %s") % and_text(persistent.game_mixes) xpadding 0 xmargin 0 background None text_color c_darkorange action NullAction() tooltip __("{b}Warning{/b}: Your choice of active girl mixes cannot be changed after starting a game, although you can still add or remove girl packs from mixes.")

                    text __("Click on a girl mix to add or remove it from this game (you must choose at least one).") size res_font(14) italic True color c_brown

                    hbox spacing 30 xfill True xalign 0.05:
                        frame ysize 0.8:
                            has vbox spacing 12 yfill True xalign 0.5
                            vpgrid cols 1 xalign 0.5 draggable True mousewheel True scrollbars "vertical":

                                style_group "mix"

                                for mix in available_mixes:
                                    textbutton mix.capitalize() text_size res_font(18) xsize xres(220) xalign 0.5:
                                        if mix in persistent.game_mixes:
                                            background c_orange
                                            text_color c_white
                                            action RemoveFromSet(persistent.game_mixes, mix)
                                            tooltip __("Click to remove mix: {b}%s{/b} from this game's active mixes.") % mix.capitalize()
                                        else:
                                            background c_ui_insensitive
                                            text_color c_darkgrey
                                            action AddToSet(persistent.game_mixes, mix)
                                            tooltip __("Click to add mix: {b}%s{/b} to this game's active mixes.") % mix.capitalize()

                            textbutton "编辑女孩组合" xsize xres(220) ysize yres(36) xalign 0.5 yalign 1.0 action Return("edit mix") tooltip "Click here to edit your girl mixes."

                        $ selected_girlpacks = get_selected_girlpacks(persistent.game_mixes)

                        vpgrid cols 10 draggable True allow_underfull True mousewheel True scrollbars "vertical" xalign 1.0:
                            for gp in selected_girlpacks:
                                button background None xalign 0.5 yalign 0.5 xmargin 0 ymargin 0 action NullAction() tooltip get_name(gp, full=True) + __("{i} by %s{/i} (%s)") % (gpinfo_dict[gp]["creator"], gpinfo_dict[gp]["version"]):
                                    add fast_portrait(gp, *res_tb(30))


            elif panel == "extras":

                vbox xfill True spacing yres(20):
                    hbox xalign 0.05 spacing xres(12):
                        label "成就水晶:" text_size res_font(24) text_color c_purple yalign 1.0
                        use crystal_display(" %i/%i" % (spent_crystals, total_crystals), sz=24, prefix="")
                        null
                        text "使用水晶解锁游戏中的额外增幅。你可以通过解锁成就来获得水晶。" yalign 1.0 size res_font(14) italic True color c_purple

                    vbox spacing yres(12) box_wrap True xsize 0.7:
                        for s in ngps:
                            $ cost = s.get_cost()
                            $ refund = s.get_refund()

                            hbox spacing xres(10):
                                button xsize xres(160) yalign 0.5 style "inv_no_padding" left_margin xres(20)  action NullAction() tooltip s.ttip:
                                    label s.label text_size res_font(18)

                                button xsize xres(60) yalign 0.5 style "inv_no_padding" action NullAction() tooltip s.get_ttip():
                                    text s.read() size res_font(18):
                                        if s.index == 0:
                                            color c_grey
                                        else:
                                            color c_purple

                                if s.type == "bool":
                                    textbutton {0: "激活", 1: "禁用"}[s.index] xsize xres(48) ysize yres(24) text_size res_font(12):
                                        if s.can_lower():
                                            tooltip s.get_ttip("minus") % refund
                                            action Function(s._lower)
                                        elif s.can_raise(total_crystals-spent_crystals):
                                            tooltip s.get_ttip("plus") % cost
                                            action Function(s._raise)

                                else:
                                    hbox yalign 0.5:
                                        if s.index < len(s.values) or s.type == "gold":
                                            textbutton "+" xsize xres(24) ysize yres(24):
                                                if s.can_raise(total_crystals-spent_crystals):
                                                    tooltip s.get_ttip("plus") % cost
                                                    action Function(s._raise)

                                        if s.can_lower():
                                            textbutton "-" xsize xres(24) ysize yres(24):
                                                tooltip s.get_ttip("minus") % refund
                                                action Function(s._lower)

                        null height yres(10)

                        textbutton "重置新周目设置" text_size res_font(12) xalign 1.0 action Return("reset NGP") tooltip "Reset all settings to default value"



                # $ unlocking_extras()

                # vbox spacing 20:
                #     text "Note: Choosing any of these options will disable achievements for this game." size res_font(14) italic True color c_brown

                #     hbox:
                #         label "Starting gold: "
                #         input value FieldInputValue(game, "starting_gold") length 9 allow "0123456789" color c_darkgold bold True

                #     hbox spacing 10:
                #         text "Starting chapter: Chapter %s" % starting_chapter color c_brown

                #         hbox:
                #             textbutton "-":
                #                 if starting_chapter > 1:
                #                     action (SetVariable("starting_chapter", starting_chapter-1),)
                #             textbutton "+":
                #                 if starting_chapter < 7:
                #                     action (SetVariable("starting_chapter", starting_chapter+1),)

                #     if starting_chapter > 1:
                #         $ next_path = get_next(["good", "neutral", "evil"], c1_path, loop=True)

                #         textbutton "Chapter 1 ending: %s" % c1_path.capitalize() action SetVariable("c1_path", next_path)

                #     vbox:
                #         style_group "extras"
                #         textbutton "Farm: %s" % {True: "Unlocked", False: "Locked"}[extras_dict["farm"]] action (ToggleDict(extras_dict, "farm"))

                #         textbutton "Carpenter: %s" % {True: "Unlocked", False: "Locked"}[extras_dict["carpenter"]] action (ToggleDict(extras_dict, "carpenter"))

                #         textbutton "Locations: %s" % {True: "Unlocked", False: "Locked"}[extras_dict["locations"]] action (ToggleDict(extras_dict, "locations"))

                #         textbutton "Shops: %s" % {True: "Unlocked", False: "Locked"}[extras_dict["shops"] > 0]:
                #             if extras_dict["shops"]:
                #                 action (SetDict(extras_dict, "shops", False))
                #             else:
                #                 action (SetDict(extras_dict, "shops", 7))

                #         textbutton "Resources: %s" % {True: "Unlocked", False: "Locked"}[extras_dict["resources"] > 0]:
                #             if extras_dict["resources"]:
                #                 action (SetDict(extras_dict, "resources", False))
                #             else:
                #                 action (SetDict(extras_dict, "resources", 7))

                #         textbutton "Trainers: %s" % {True: "Unlocked", False: "Locked"}[extras_dict["trainers"]] action (ToggleDict(extras_dict, "trainers"))

                #         text "" size res_font(12)

                #         textbutton "Reset extras" action (SetVariable("extras_dict", {"farm" : False, "carpenter" : False, "locations" : False, "shops" : False, "trainers" : False, "resources" : False}), SetField(game, "starting_gold", str(starting_gold)))

        frame xfill True xsize int(0.95*config.screen_width) ysize int(0.1*config.screen_height):
            hbox xsize 0.7 xalign 0.95 spacing xres(12):
                add Picture(path=playerclass_pics[MC.playerclass]).get(*res_tb(50)) xalign 0.0 yalign 0.5
                add Picture(path=god_pics[MC.god]).get(*res_tb(50)) xalign 0.0 yalign 0.5

                vbox spacing 10 xalign 0.5 yalign 0.5:
                    text __("{b}%s, %s{/b} ({b}%s{/b}) - {b}%s{/b} difficulty") % (MC.name, __(tl_cn(MC.playerclass, misc_name_dict)), tl_cn(str(MC.god), misc_name_dict), __(tl_cn(game.diff.capitalize(), misc_name_dict))) color c_prune size res_font(18)
                    if game.achievements:
                        text __("Achievements will be enabled for this game.") italic True color c_emerald size res_font(18)
                    else:
                        text __("Achievements will be disabled for this game.") italic True color c_red size res_font(18)

                textbutton "确认" xalign 1.0 yfill True action Return(True) tooltip "Start a new game with these settings."

## MAIN CHARACTER SCREEN

screen main_character():

    use shortcuts()
    use overlay("MC")

    frame background None:

        xalign 0.0
        ypos 0.1
        xsize xres(200)
        ysize yres(520)
        xfill True
        yfill True

        has vbox

        spacing 3

        frame xpadding 3 ypadding 10 xfill True:
            has vbox
            textbutton MC.name background None text_color c_main action Return("change_name") hovered tt.Action(__("Click here to change your character's name"))
            textbutton (__("Level ") + str(MC.level) + " " + __(MC.playerclass)) background None text_size res_font(18) text_color c_darkgrey action NullAction() tooltip __("You need ") + str(int(MC_xp_to_levelup[MC.level])) + __(" prestige to level up.")

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
                    xsize xres(180)
                    ysize yres(30)

                    action NullAction()
                    tooltip MC_stat_description[stat]

                    text MC_stat_color[stat] % __(stat.capitalize()) size res_font(18)

                    text "{color=[col2]}" + str(int(MC.get_stat(stat))) + "{/color}" size res_font(18) xanchor 1.0 xpos 0.8

                    if MC.skill_points > 0 and MC.get_stat(stat, raw=True) < MC.get_stat_cap(stat):
                        textbutton "+" text_size res_font(14) xpos 0.85 xfill False xpadding xres(4) ypadding yres(2) action Return("raise_" + stat) tooltip __("Use a skill point to raise this attribute (max %i)") % MC.get_stat_cap(stat)

            text "" size res_font(8)

            vbox spacing 3:
                $ text1 = __("You earn prestige everytime you or your girls have sex, or when one of your girl earns a new level.")

                if MC.level == 25:
                    $ text1 += __("\nYou have reached the maximum level.")
                else:
                    $ text1 += __("\nYou need ") + str(int(MC_xp_to_levelup[MC.level])) + __(" prestige to level up.")

                button:
                    background None
                    action NullAction()
                    tooltip text1

                    text (str(int(MC.prestige)) + " prestige") size res_font(14) color c_brown

                button:
                    background None
                    action NullAction()
                    tooltip __("You get 1 skill point for every new level.")

                    text str(MC.skill_points) + __(" skill points") size res_font(14) color c_brown

        frame xpadding 3 ypadding 10 xfill True:
            has vbox
            hbox xalign 0.5:

                spacing 16

                button yalign 0.5 xpadding 0 action NullAction() tooltip MC_playerclass_description[MC.playerclass]:
                    add Picture(path=playerclass_pics[MC.playerclass]).get(*res_tb(40)) yalign 0.5

                button yalign 0.5 xpadding 0 action NullAction() tooltip god_description[MC.god]:
                    add Picture(path=god_pics[MC.god]).get(*res_tb(40)) yalign 0.5

                button yalign 0.5 xpadding 0 action NullAction() tooltip alignment_description[MC.get_alignment()] + "\n(%s: %s)" % (MC.get_alignment().capitalize(), plus_text(MC.get_alignment_delta(MC.get_alignment()))):
                    add Picture(path=alignment_pics[MC.get_alignment()]).get(*res_tb(40)) yalign 0.5

            text "" size res_font(10)

            textbutton __("{b}Current goal{/b}\n{i}{size=-2}") + game.get_first_goal() xalign 0.1 yalign 0.5 xsize xres(180) text_size res_font(14) text_color c_brown background None:
                action NullAction()
                hovered Show("goal_ttip", transition=Dissolve(0.15))
                unhovered Hide("goal_ttip", transition=Dissolve(0.15))

            text "" size res_font(8)

            textbutton __("Spellboo{u}k{/u}") xalign 0.5 action (Show("spellbook"), Function(norollback)) tooltip __("See all available spells and active talents")

    hbox xpos 0.2 ypos 0.8 yanchor 1.0 xsize 0.55 ysize 0.7 xfill True:
        textbutton "<"  ysize yres(120) xalign 0.0 yalign 1.0:

            action Return("previous_pic")
            tooltip __("Change your character's picture.")


        frame background None:
            xalign 0.5
            yalign 1.0
            xmaximum 0.9
            xfill False
            yfill False
            padding (0, 0, 0, 0)
            add AlphaMask(MC.current_pic.get(), Frame("GUI/edge_mask.png")) fit "contain" xalign 0.5

        textbutton ">" xalign 1.0 ysize yres(120) yalign 1.0:

            action Return("next_pic")
            tooltip __("Change your character's picture.")

screen active_spells():

    hbox:
        text "Active:" size res_font(14) color c_brown yalign 0.5
        for spell in MC.active_spells:
            button xpadding 0 ypadding 0 xsize xres(40) ysize yres(40) action NullAction() tooltip "{b}" + spell.name + "{/b}: " + spell.description: # get_description("", spell.effects):
                add spell.pic.get(*res_tb(30)) xalign 0.5 yalign 0.5


screen spellbook():

    modal True
    zorder 5

    key "mouseup_3" action (Hide("spellbook"), SetVariable("show_spellbook", False)) capture True

#    use dark_filter

    textbutton "%s的法术书" % MC.name yalign 0.1 xalign 0.5

    fixed xalign 0.5 yalign 0.5:
        fit_first True

        add "UI/spellbook.webp" fit "contain"

        frame xalign 0.95 yalign 0.05:
            use close((Hide("spellbook"), SetVariable("show_spellbook", False)))

        if MC.known_spells:
            frame xalign 0.5 yalign 0.05:
                text __("Right-click on a spell to set-up auto-cast") size res_font(14) color c_brown

            frame ypadding yres(66) xfill True yfill True background None:
                viewport:
                    xalign 0.5
                    yalign 0.0
                    xsize 0.95
                    ysize 0.95
                    mousewheel True
                    draggable True
                    scrollbars "vertical"

                    fixed xalign 1.0 ysize yres(80) * round_up(len(MC.known_spells)/2.0):

                        $ x = 0
                        $ y = 0
                        $ i = 0

                        for s in MC.known_spells:
                            if s.type != "passive":

                                if s in MC.active_spells and s.auto:
                                    $ col = c_darkpurple
                                    $ extra = __("(Auto-cast: ") + s.auto.capitalize() + __(")\n(Active)")

                                elif s.auto:
                                    $ col = c_firered
                                    $ extra = __("(Auto-cast: ") + s.auto.capitalize() + ")"

                                elif s in MC.active_spells:
                                    $ col = c_main
                                    $ extra = __("(Active)")

                                else:
                                    $ col = False
                                    $ extra = ""

                                button:
                                    xpos x + xres(80)
                                    ypos y
                                    xsize xres(220)
                                    ysize yres(80)
                                    xfill True
                                    xanchor 0.0
                                    xpadding 3
                                    xmargin 0

                                    if col:
                                        background col

                                    action Return((s, "cast"))

                                    alternate Function(MC.toggle_auto_spell, s) #ToggleField(s, "auto")

                                    tooltip s.description

                                    hbox spacing 3 xalign 0.0 yfill True:

                                        frame background None xsize xres(60) yfill True xmargin 6:
                                            add s.pic.get(*res_tb(50)) xalign 0.5 yalign 0.5


                                        vbox yalign 0.5:

                                            text s.name size res_font(14) bold True

                                            hbox:
                                                text str(s.get_cost()) size res_font(14)

                                                add ProportionalScale("UI/mana.webp", *res_tb(15))

                                                if s.duration == "turn":

                                                    text __("/night") size res_font(14)

                                            if extra:
                                                text extra size res_font(14)

                                if i%2:
                                    $ x = 0
                                    $ y += yres(80)
                                else:
                                    $ x = yres(500)

                                $ i += 1

        else:
            textbutton "{i}你还没有掌握任何法术。请去提升角色等级{/i}" xalign 0.5 yalign 0.5 xsize xres(250) text_size res_font(18)

    if MC.active_spells:
        frame xalign 0.5 yalign 0.95 xmaximum 0.85 xpadding 20:
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

        if selected_girl:
            use girl_stats(selected_girl, context = "postings")

        vbox:
            xsize 0.5


            frame:
                xsize int(0.5*config.screen_width)
                ysize 0.7

                xpadding 10

                has vbox

                spacing 3

                if selected_quest:

                    hbox:
                        spacing 0
                        xalign 0.0

                        if selected_quest.special:
                            textbutton "{image=img_star} " + __(selected_quest.special) + " {image=img_star}" xalign 0.0 yalign 0.5 ypadding 0 text_color c_orange background None action NullAction() hovered tt.Action(special_quest_description[selected_quest.special])

                        text selected_quest.name xalign 0.0 yalign 0.5 color c_prune

                    hbox:
                        spacing 10

                        frame:
                            xmaximum xres(360)
                            ysize yres(480)
                            background None

                            if selected_quest.pic:
                                add selected_quest.pic.get(xres(350), yres(480)) xalign 0.0 yalign 0.0

                        vbox xfill True:

                            text selected_quest.description size res_font(14) color c_brown

                            text "" size res_font(18)

                            text __("Duration") size res_font(18) color c_prune

                            text str(selected_quest.duration) + __(" days") size res_font(14) color c_brown

                            text "" size res_font(18)

                            if selected_quest.type == "class":

                                text __("Cost") size res_font(18) color c_prune

                                if not story_flags["postings free class"]:
                                    text str(int(selected_quest.gold)) + __(" gold") size res_font(14) color c_brown
                                else:
                                    text __("FREE") size res_font(14) color c_orange

                                text "" size res_font(18)

                                text __("Enrolled") size res_font(18) color c_prune

                                text str(len(selected_quest.enrolled)) + "/" + str(selected_quest.capacity) + __(" girls") size res_font(14) color c_brown

                                text "" size res_font(18)

                                text __("Gains") size res_font(18) color c_prune

                                for stat, _min, _max in selected_quest.bonuses:

                                    if _max >= 12:
                                        $ t = "+++"

                                    elif _max >= 6:
                                        $ t = "++"

                                    else:
                                        $ t = "+"

                                    text "[stat!t]" + " " + t size res_font(14) color c_brown

                                textbutton "\n最大属性: " + str(selected_quest.stat_cap) text_size res_font(14) text_color c_brown xalign 0.0 yalign 0.5 xpadding 0 ypadding 0 background None:
                                    tooltip __("Classes may cause a girl's skills to exceed their level cap.")


                            elif selected_quest.type == "quest":

                                text __("Reward") size res_font(18) color c_prune

                                text str(selected_quest.gold) + __(" gold") size res_font(14) color c_brown

                                text "" size res_font(18)

                                text __("Requirements") size res_font(18) color c_prune

                                for stat, val in selected_quest.requirements:

                                    text "[stat!t]" + " " + str(val) size res_font(14) color c_brown

                                text "" size res_font(18)

                                if selected_quest.pos_traits:

                                    text __("Desirable") size res_font(18) color c_prune

                                    text selected_quest.pos_traits[0].name + ", " + selected_quest.pos_traits[1].name size res_font(14) color c_emerald

                                    text "" size res_font(18)

                                if selected_quest.neg_trait:

                                    text __("Undesirable") size res_font(18) color c_prune

                                    text selected_quest.neg_trait.name size res_font(14) color c_crimson

                else:
                    text __("No task is currently available.") italic True color c_brown size res_font(18)

            fixed xalign 0.5:
                fit_first True

                if selected_quest:

                    $ available_girls = [g for g in MC.girls if selected_quest.test_eligibility(g)[0]]

                    if selected_quest and selected_girl:
                        $ r, ttip = selected_quest.test_eligibility(selected_girl)

                        if r: # or debug_mode:
                            use girl_select(available_girls, action_button = ("Commit", Return("commit"), ttip))
                        else:
                            use girl_select(available_girls, action_button = ("Commit", NullAction(), ttip))


        vbox:
            yalign 0.0
            xfill False
            yfill False


            frame:

                xalign 0.0
                yalign 0.0
                xmargin 3
                xpadding 6
                xfill False
                yfill False
                ysize int(0.7*config.screen_height)

                has vbox

                hbox:

                    textbutton "委托" text_size res_font(14) xsize xres(80) xfill True style "posting_button" action (Return("quests"), SelectedIf(qlist == quest_board.quests))
                    textbutton "培训" text_size res_font(14) xsize xres(80) xfill True style "posting_button" action (Return("classes"), SelectedIf(qlist == quest_board.classes))


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

                                    $ ttip = __("This task requires ") + __(and_text([stat for stat, v in quest.requirements])) + ".\n"
                                    $ ttip += str(quest.count_eligible_girls()) + __(" girls can complete this task.")

                                elif quest.type == "class":

                                    $ ttip = __("This class may improve {b}") + __(and_text([stat for stat, _min, _max in quest.bonuses])) + "{/b}.\n"
                                    $ ttip += str(len(quest.enrolled)) + "/" + str(quest.capacity) + " are enrolled in this class."

                                button:
                                    xsize xres(160)
                                    ysize yres(60)
                                    xmargin 0
                                    xpadding 0
                                    ypadding 0
                                    action (SetVariable("selected_quest", quest), Return("change"), SelectedIf(selected_quest == quest))
                                    tooltip ttip

                                    hbox spacing xres(5) xalign 0.0 yalign 0.5:

                                        fixed xsize xres(50) ysize yres(50) yalign 0.5:
                                            if quest.pic:
                                                add quest.pic.get(*res_tb(45)) xalign 0.5 yalign 0.5

                                        vbox xalign 0.0 yalign 0.5:
                                            if quest.special:
                                                $ text1 = "{image=img_star}"
                                            else:
                                                $ text1 = ""
                                            text text1 + "[quest.name!t]"  size res_font(13)
                                            if quest.type != "class" or not story_flags["postings free class"]:
                                                text str(int(quest.gold)) + " gold" size res_font(13)
                                            else:
                                                text __("FREE") size res_font(13)

                if calendar.active_contract:
                    text ""
                    text ""
                    button xfill True xpadding 6 ypadding 6 action Return("active_contract"): # hovered Show("contract_tab", contract=calendar.active_contract, x=450, active=True, transition=Dissolve(0.15)) unhovered Hide("contract_tab", transition=Dissolve(0.15)) tooltip "Show active contract (%s day%s left)." % (28-calendar.day, plural(28-calendar.day)):
                        vbox xfill True:
                            text __("Active contract") size res_font(14) color c_darkbrown xalign 0.5
                            add ProportionalScale("UI/" + license_dict[1][1], *res_tb(50)) xalign 0.5





screen dark_filter(can_click=True, covers_dialogue=True):

    tag dark_filter

    modal False

    zorder 0

    if covers_dialogue:
        $ y = int(0.925*config.screen_height)
    else:
        $ y = int(0.925*config.screen_height-res_portrait_size)

    button xfill True yfill True xpadding 0 xmargin 0 ypadding 0 ymargin 0 ypos 0.075 yanchor 0.0 ymaximum y background c_ui_darkblue activate_sound None:
        if can_click:
            action Return()


screen personality_screen():

    tag personality_screen

    frame xalign 0.51 yanchor 0.0 ypos 0.1 ysize yres(320) xfill True xpadding xres(10) ypadding yres(10) xmaximum xres(400) background Frame("UI/paper.webp"): #int(config.screen_width * 0.58):

        has vbox spacing 20

        if selected_girl:

            hbox xalign 0.0:
                textbutton "性格" xsize xres(85) text_size res_font(18) hovered SetVariable("pers_showing", "personality") action NullAction(), SelectedIf(pers_showing=="personality")
                textbutton "品味" xsize xres(85) text_size res_font(18) hovered SetVariable("pers_showing", "tastes") action NullAction(), SelectedIf(pers_showing=="tastes")
                textbutton "性癖" xsize xres(85) text_size res_font(18) hovered SetVariable("pers_showing", "sexual") action NullAction(), SelectedIf(pers_showing=="sexual")
                textbutton "事件" xsize xres(85) text_size res_font(18) hovered SetVariable("pers_showing", "recent") action NullAction(), SelectedIf(pers_showing=="recent")

            hbox spacing xres(6) xpos 0.01:

                $ badge = selected_girl.get_badge()
                button xmaximum yres(90) background None action NullAction():
                    if selected_girl in (MC.girls + farm.girls):
                        hovered (Show("mood_details", girl=selected_girl, transition=Dissolve(0.15)), tt.Action(selected_girl.get_mood_description("mood")))
                        unhovered Hide("mood_details", transition=Dissolve(0.15)) xpadding 0 ypadding 0 xmargin 0 ymargin 0 xsize xres(100) ysize yres(100)

                    fixed fit_first True:
                        add selected_girl.portrait.get(*res_tb(90))

                        # Add mood meter
                        if selected_girl in (MC.girls + farm.girls):
                            add ProportionalScale(selected_girl.get_mood_picture(), *res_tb(25)) xalign 0.95 yalign 0.05

                        if badge:
                            add ProportionalScale(badge, *res_tb(25)) xalign 0.95 yalign 0.05

                viewport xmaximum 0.95:
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    ysize yres(220)
                    text selected_girl.get_personality_description(pers_showing) size res_font(14) color c_brown


screen notebook():
    key "mouseup_3" action (Hide("notebook"), Hide("mood_details"))
    key "noshift_K_n" action (Hide("notebook"), Hide("mood_details"))
    use dark_filter()
    use close(Hide("notebook"))
    use personality_screen()



## FARM SCREEN ##

screen farm_menu(prog, can_cancel=True):

    modal True
    zorder 5

    default _warning = False
    $ available_installations = [farm.installations[farm_installations_dict[type]] for type in all_minion_types if farm.installations[farm_installations_dict[type]].rank > 0]

    use overlay("farm")
    use dark_filter(False)

    if can_cancel:
        key "mouseup_3" action (Return("back"))

    frame background c_ui_darker xsize yres(800) xalign 0.5 ypos 0.1 xpadding xres(10) ypadding yres(10): # Using yres to maintain proportions in wide screen

        has vbox

        hbox xpos 0.01 xfill True:
            hbox spacing xres(10):
                add girl.portrait.get(xres(40), yres(40))
                text girl.fullname bold True yalign 0.5
            text __("Farm Training Menu") bold True yalign 0.5
            if can_cancel:
                use close(Return("back"))

        text "" size 16

        # Warnings
        $ _warning = False

        if prog.target == "no training" and prog.holding=="rest":
            $ text1 = prog.girl.fullname + __(" will {b}Rest{/b} in her cell.")

        else:
            if prog.target == "no training":
                $ text1 = prog.girl.fullname + __(" will improve her {b}") + stat_name_dict[prog.holding.capitalize()] + __("{/b} from doing chores.")
            else:
                if prog.target == "auto":
                    $ text1 = prog.girl.fullname + __(" will receive {b}automatic training{/b}")
                else:
                    $ text1 = prog.girl.fullname + __(" will receive {b}") + prog.target.capitalize() + __(" training{/b}")

                if prog.auto_inst:
                    $ text1 += __(".\nI will assign her an {b}automatic facility{/b}, if there is room.")

                    $ _warning = __("There might not be enough free minions to take care of her in all your facilities.") # Reverse logic, because of the lack of for... else loops in screen language

                    for inst in available_installations:
                        # $ other_assigned_girls = [g for g in inst.return_assigned_girls() if g != prog.girl]
                        # $ av_min = len(inst.get_healthy_minions()) - len(other_assigned_girls)
                        if inst.count_busy_minions() <= len(inst.get_healthy_minions()): # (prog.target != "group" and av_min >= 1) or av_min >= 2:
                            $ _warning = False

                elif prog.installation:
                    $ text1 += __(" at the {b}") + capitalize(prog.installation.name) + __("{/b}.")

                    # $ other_assigned_girls = [g for g in inst.return_assigned_girls() if g != prog.girl]
                    $ free_m = len(prog.installation.get_healthy_minions()) - prog.installation.count_busy_minions()

                    if free_m < 0:
                        if prog.target == "group":
                            $ _warning = __("There may not be enough valid minions for group training. I may assign her to a different facility if other minions are available.")
                        else:
                            $ _warning = __("There are not enough valid minions in the %s, I may have to rotate this girl in and out of the facility.") % prog.installation.name

        if _warning:
            $ pic = "side gizel upset"
            $ text1 += event_color["very bad"] % (__("\n{b}Warning{/b}: ") + _warning)
        else:
            $ pic = "side gizel"

        hbox spacing xres(20):
            frame background Frame (
                im.MatrixColor(
                    "UI/cry_box.webp",
                    im.matrix.colorize(c_lightprune + "CC", "#000")), left=12, right=12) xfill True:
                has hbox
                spacing 10
                add pic zoom 0.6 yalign 0.5
                text text1 color c_prune text_align 0.0 xalign 0.0 yalign 0.5 size res_font(16) justify True

        text "" size 16

        textbutton "干农活" style "inv_no_padding" xalign 0.01 text_size res_font(18) text_drop_shadow (2, 2) action NullAction() tooltip "Work for Gizel on the farm. These activities do no require minions."

        textbutton "休息" style "farm_button" text_size res_font(18) xsize yres(780) action (SetField(prog, "target", "no training"), SetField(prog, "holding", "rest"), SetField(prog, "installation", None), SelectedIf(prog.target == "no training" and prog.holding=="rest")) tooltip "She will simply rest in her pen."

        null height yres(9)

        hbox:
            for stat in ("Libido", "Obedience", "Constitution", "Sensitivity"):
                textbutton stat_name_dict[stat] style "farm_button" text_size res_font(18) xsize yres(780//4):
                    if prog.target == "no training" and prog.holding==stat.lower():
                        action (SetField(prog, "target", "no training"), SetField(prog, "holding", "rest"), SetField(prog, "installation", None), SelectedIf(True))
                    else:
                        action (SetField(prog, "target", "no training"), SetField(prog, "holding", stat.lower()), SetField(prog, "installation", None), SelectedIf(False))
                    tooltip farm_ttip[stat.lower()]

        text "" size 16

        textbutton "性技训练" style "inv_no_padding" xalign 0.01 text_size res_font(18) text_drop_shadow (2, 2) action NullAction() tooltip "Go through Gizel's special training program. Sexual training requires available minions."

        hbox:
            for act in extended_sex_acts:
                $ ttip = __("Gizel will train her in %s acts using minions.") % tl_cn(act, girl_related_dict)

                if act == "group":
                    $ ttip += __("\nRequires 2 or 3 free minions at the same facility.")

                textbutton act.capitalize() style "farm_button" text_size res_font(18) xsize yres(780//7):
                    if prog.target==act:
                        action (SetField(prog, "target", "no training"), SetField(prog, "holding", "rest"), SetField(prog, "installation", None), SelectedIf(True))
                    else:
                        action (SetField(prog, "target", act), SelectedIf(False))

                    tooltip ttip

        null height yres(9)

        hbox:
            for cond in ("indifferent", "interested", "fascinated"):
                textbutton "全面训练 (%s)" % cond.capitalize() style "farm_button" text_size res_font(14) xsize yres(780//3) ysize yres(28):
                    action (SetField(prog, "target", "auto"), SetField(prog, "condition", cond), SelectedIf(prog.target=="auto" and prog.condition == cond))
                    tooltip __("She will be assigned sex acts automatically until she is at least %s.") % (preference_color[cond] % cond)

        text "" size 16

        textbutton "自动训练" style "inv_no_padding" xalign 0.01 text_size res_font(18) text_drop_shadow (2, 2) action NullAction() tooltip "Pick a facility with minions for training (sexual training only)."

        if prog.target == "no training":
            button style "farm_button" action SelectedIf(prog.target=="no training"):

                tooltip __("She will be held in her pen for this activity.")

                vbox:
                    spacing 3
                    fixed xalign 0.5 yalign 0.5:
                        fit_first True
                        add Picture(pic, "brothels/farm/pen.webp").get(yres(120), yres(120))
                    text __("Farm pen") size res_font(16) xcenter 0.5

        else:

            hbox xalign 0.0:
                button style "farm_button" action (SetField(prog, "auto_inst", True), SetField(prog, "installation", None), SelectedIf(prog.installation==None)):
                    at alpha_transform

                    tooltip __("Let Gizel assign a free minion to her automatically.")

                    vbox:
                        spacing 3
                        fixed xalign 0.5 yalign 0.5:
                            fit_first True
                            add Picture(pic, "brothels/farm/auto.webp").get(yres(120), yres(120)) # idle_alpha 0.66 hover_alpha 1.0
                        text __("Auto.") style "farm_button_text" size res_font(16) xcenter 0.5

                for inst in available_installations:
                    # $ other_assigned_girls = [g for g in inst.return_assigned_girls() if g != prog.girl]
                    $ inst_nb = inst.count_busy_minions()
                    $ ttip = __("It has %i healthy minion%s available.") % (len(inst.get_healthy_minions()), plural(len(inst.get_healthy_minions())))
                    # if prog.installation==inst:
                    #     $ inst_nb += 1

                    if farm.knows["weakness"][girl] and girl.weakness == inst.minion_type:
                        $ ttip += __("\nShe is weak to ") + girl.weakness + __("s. Training will be more efficient, but doing it against her will will increase fear and decrease mood faster.")
                    if len(inst.get_healthy_minions()) < 1:
                        $ ttip += event_color["bad"] % __("\nThere are no available minions in this facility.")

                    button style "farm_button":
                        if len(inst.get_healthy_minions()) >= 1:
                            action (SetField(prog, "auto_inst", False), SetField(prog, "installation", inst), SelectedIf(prog.installation==inst))
                        else:
                            hover_background Frame (
                                im.MatrixColor(
                                    "UI/cry_box.webp",
                                    im.matrix.colorize(c_lightprune + "CC", "#000")), left=12, right=12)
                            action NullAction()

                        vbox:
                            spacing 3
                            fixed xalign 0.5 yalign 0.5:
                                fit_first True
                                add inst.get_pic().get(yres(120), yres(120)) idle_alpha 0.66:
                                    if len(inst.get_healthy_minions()) >= 1:
                                        hover_alpha 1.0
                                text str(inst_nb) + "{size=-8}/" + str(len(inst.get_healthy_minions())) xalign 0.9 yalign 0.1

                            hbox xcenter 0.5 spacing xres(9):
                                text inst.name.capitalize() size res_font(16):
                                    if len(inst.get_healthy_minions()) >= 1:
                                        style "farm_button_text"
                                    else:
                                        color c_darkprune
                                if farm.knows["weakness"][girl] and girl.weakness == inst.minion_type:
                                    add "img_fear"

                        if prog.installation==inst:
                            tooltip __("She will be assigned to this facility. ") + ttip
                        else:
                            tooltip __("%s currently assigned to this facility. ") % (and_text([g.fullname for g in inst.return_assigned_girls()], if_none="No girls")) + ttip

        text ""

        if prog.target == "no training" and prog.holding=="rest":
            textbutton "送去农场(休息)" ypadding yres(9) text_color c_white text_size res_font(18) xsize yres(780//3) xalign 0.5 action Return("commit") tooltip "Send her to the farm to rest in a pen."

        else:
            hbox xalign 0.5:
                for train_mode in ("gentle", "tough", "hardcore"):
                    textbutton "训练 (%s)" % train_mode ypadding yres(9) text_color c_white text_size res_font(18) xsize yres(780//3) action (SetField(prog, "mode", train_mode), SelectedIf(prog.mode==train_mode), Return("commit")) tooltip farm_ttip[train_mode]




screen farm_tab():

    zorder 0

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
        key "noshift_K_u" action Return(("items", None))

        frame xsize int(0.625*config.screen_width) ysize yres(520) xfill True yfill True xalign 0.1 ypos 0.1 background None:

            has vbox xalign 0.5

            text "吉泽尔的奴隶农场" drop_shadow (2, 2) bold True xalign 0

            if farm.girls:
                $ text1 = "啊, [MC.name]! 要不要来看看我的宠物?"
                $ pic = "side gizel"
            else:
                $ text1 = "我的仆从们感到无聊...你打算什么时候给他们送来一些新的玩伴？"
                $ pic = "side gizel upset"

            if MC.street_girls:
                $ text1 += __("\n\n%i street whores are currently housed in the barn.") % len(MC.street_girls)

            hbox spacing 15:
                if farm.powers:
                    if farm.powers == "intro":
                        $ text1 = __("[MC.name], come! There is something you must see.")
                    button xmargin 6 ymargin 6 xpadding 6 ypadding 6 xysize res_tb(110):
                        text str_int(MC.mojo["purple"]) size res_font(18) drop_shadow (2, 2) xalign 0.5 yalign 0.0 color c_hotpink
                        text str_int(MC.mojo["green"]) size res_font(18) drop_shadow (2, 2) xalign 0.1 yalign 1.0 color c_lightgreen
                        text str_int(MC.mojo["blue"]) size res_font(18) drop_shadow (2, 2) xalign 0.0 yalign 0.3 color c_lightblue
                        text str_int(MC.mojo["red"]) size res_font(18) drop_shadow (2, 2) xalign 1.0 yalign 0.3 color c_red
                        text str_int(MC.mojo["yellow"]) size res_font(18) drop_shadow (2, 2) xalign 0.9 yalign 1.0 color c_yellow
                        action Return(("powers", None))
                        if farm.powers == "intro":
                            background None
                            tooltip __("Click here to head where Gizel is calling you.")
                        elif evpower_deck.can_draw:
                            background None
                            tooltip __("New cards are available! Click here to access the {b}Power Deck{/b}.")
                        else:
                            background Frame("UI/powers/pentagram.webp")
                            tooltip __("Click here to access the {b}Power Deck{/b}.")

                button xfill True xmargin 3 ymargin 3 xpadding 6 ypadding 6 tooltip __("Ask Gizel for help about the farm.") background c_ui_dark:
                    if farm.powers == "intro":
                        action Return(("powers", None))
                        tooltip __("Click here to head where Gizel is calling you.")
                    else:
                        action Return(("help", None))
                        tooltip __("Click here for help on using the farm.")
                    at alpha_transform

                    has hbox spacing 10
                    fixed fit_first True yalign 0.5 xysize res_tb(110):
                        add pic zoom 0.6 # idle_alpha 0.8 hover_alpha 1.0
                        if farm.powers:
                            add AlphaMask("static", pic) zoom 0.6 # idle_alpha 0.8 hover_alpha 1.0
                    text text1 yalign 0.5 size res_font(18) justify True italic True xmaximum 0.8

            hbox spacing 15:

                vbox:

                    text __("{b}Girl pens{/b}") size res_font(18) xalign 0.0 ypos 0.3 drop_shadow (2, 2)

                    text "" size res_font(6)

                    frame background c_ui_dark:

                        has vbox spacing 6

                        $ ttip = __("The farm can host one girl per pen.")

                        if farm.pens < farm.get_pen_limit():
                            $ ttip += __("\nClick here to add a new pen for ") + str(farm.get_pen_cost()) + __(" gold.")
                        elif brothel.rank == 5:
                            $ ttip += __("You cannot build any more pens.")
                        else:
                            $ ttip += __("Upgrade your brothel to be able to add more pens.")

                        $ ttip += __("\n(Currently available pens: ") + str(farm.pens - len(farm.girls)) + ")"

                        button:
                            xpadding 6
                            ypadding 6
                            action Return(("pen", None))
                            tooltip ttip
                            at alpha_transform

                            fixed:
                                fit_first True
                                add farm.pen_pic.get(xres(135), yres(135)) # idle_alpha 0.66 hover_alpha 1.0
                                if farm.pens < farm.get_pen_limit():
                                    text "+" xalign 0.5 yalign 0.5 size res_font(36)
                                text str(farm.pens) + "{size=-8}/" + str(farm.get_pen_limit()) xalign 0.9 yalign 0.1

                vbox:
                    text __("{b}Farm status{/b}") size res_font(18) ypos 0.3 drop_shadow (2, 2)
                    text "" size res_font(6)
                    frame background c_ui_dark xfill True:
                        has vbox
                        if farm.get_hurt_minions():
                            text __("Hurt minions: ") size res_font(14)
                            hbox box_wrap True:
                                for mn in farm.get_hurt_minions():
                                    button background None xalign 0.5 xpadding 0 xmargin 0 ypadding 0 ymargin 0 action NullAction() tooltip mn.get_tooltip():
                                        has hbox spacing xres(3)
                                        add mn.get_pic(*res_tb(20))
                                        text mn.name + ", Lv. " + str(mn.level) size res_font(14) color c_red yalign 0.5
                                        text "{color=[c_red]}✙{/color}" size res_font(14) font "1.ttf" yalign 0.5

                        else:
                            text "没有可报告的事件" size res_font(14)

            text ""

            hbox spacing 25:
                text __("{b}Facilities & Minions{/b}") size res_font(18) yalign 0.5 drop_shadow (2, 2)
                textbutton "使用道具" text_size res_font(18) action Return(("items", None)) tooltip "Use an item on your minions." yalign 0.5

            text "" size res_font(6)

            frame:
                background c_ui_dark
                xfill True

                has hbox spacing 25

                for type in all_minion_types:
                    $ inst = farm.installations[farm_installations_dict[type]]

                    vbox xsize xres(130):

                        button:
                            xpadding 6
                            ypadding 6
                            insensitive_background c_darkgrey + "E5"
                            at alpha_transform

                            if inst.can_upgrade():
                                action Return(("upgrade", inst))
                            else:
                                action NullAction()

                            tooltip inst.get_tooltip()

                            vbox:
                                spacing 3
                                fixed:
                                    fit_first True
                                    add inst.get_pic().get(xres(120), yres(120)) # idle_alpha 0.66 hover_alpha 1.0
                                    if inst.can_upgrade():
                                        text "+" xalign 0.5 yalign 0.5 size res_font(36)
                                    text str(inst.rank) + "{size=-8}/" + str(district.rank) xalign 0.9 yalign 0.1

                                if inst.rank > 0:
                                    text inst.name.capitalize() size res_font(14) xcenter 0.5
                                else:
                                    text "???" size res_font(14) xcenter 0.5

#            text "" size res_font(6)
            frame:
                background c_ui_dark
                xsize 0.99
                xfill True
                has hbox spacing 25
                for type in all_minion_types:

                    vbox xsize xres(130) xfill True:

                        if len(farm.get_minions(type)) > 0:
                            textbutton str(len(farm.get_minions(type))) + " " + type.capitalize() + plural(len(farm.get_minions(type))) style "inv_no_padding" text_size res_font(14) text_bold True xalign 0.5 action NullAction() tooltip minion_description[type]

                        text "" size res_font(6)

                        for mn in farm.get_minions(type):

                            button background None xalign 0.5 xpadding 0 xmargin 0 ypadding 0 ymargin 0 action NullAction() tooltip mn.get_tooltip() hovered tt.Action(mn.description):

                                has hbox spacing xres(3)
                                add mn.get_pic(*res_tb(20))

                                text mn.name + ", Lv. " + str(mn.level) size res_font(14) yalign 0.5:
                                    if mn.hurt:
                                        color c_red
                                if mn.hurt:
                                    text "{color=[c_red]}✙{/color}" size res_font(14) font "1.ttf" yalign 0.5


screen mood_details(girl):

    frame:
        background c_ui_darker
        xalign 0.5
        yalign 0.2
        xpadding 0.05
        ypadding 0.05
        xfill True
        xmaximum xres(350)
        ymaximum int(0.5*config.screen_height)

        has vbox

        xfill True

        spacing 6

        text __("%s's mood") % girl.name color c_orange xalign 0.5

        text "" size res_font(6)

        $ love_text, fear_text, mood_text, mood_change_text, mood_factors = girl.get_mood_description()

#        text love_text size res_font(14)

#        text fear_text size res_font(14)

#        text "" size res_font(6)

        text mood_text + mood_change_text size res_font(14)

        # text mood_change_text size res_font(14)

        text "" size res_font(6)

        text mood_factors size res_font(12) color c_white

        if persistent.sanity_display or girl in farm.girls:
            text __("Current sanity: ") + girl.get_sanity() size res_font(14)


screen love_button(girl):

    $ ttip = girl.get_mood_description("love")

    if debug_mode:
        $ ttip += "\n(" + str(round(girl.get_love(), 1)) + ")"

    button xmargin 0 xpadding 0 xalign 0.5 yalign 0.5:
        background None
        action NullAction()
        tooltip ttip
        at alpha_transform

        $ l = girl.get_love()

        if l >= 5:

            $ h = l // 2.5 + yres(10)

            add ProportionalScale("UI/heart.webp", h, h) xalign 0.5 yalign 0.5 # idle_alpha 0.66 hover_alpha 0.8

        elif l <= -5:
            $ h = l // -2.5 + yres(10)
            add ProportionalScale("UI/broken heart.webp", h, h) xalign 0.5 yalign 0.5 # idle_alpha 0.66 hover_alpha 0.8

        else:
            add ProportionalScale("UI/love question.webp", *res_tb(20)) xalign 0.5 yalign 0.5 # idle_alpha 0.66 hover_alpha 0.8


screen fear_button(girl):

    $ ttip = girl.get_mood_description("fear")

    if debug_mode:
        $ ttip += "\n(" + str(round(girl.get_fear(), 1)) + ")"

    button xmargin 0 xpadding 0 xalign 0.0 yalign 0.5:
        background None
        action NullAction()
        tooltip ttip
        at alpha_transform

        $ f = girl.get_fear()

        if f >= 5:

            $ h = f // 2.5 + yres(10)

            add ProportionalScale("UI/skull.webp", h, h) xalign 0.5 yalign 0.5 # idle_alpha 0.66 hover_alpha 0.8

        elif f <= -5:
            $ h = f // -2.5 + yres(10)

            add ProportionalScale("UI/droplet.webp", h, h) xalign 0.5 yalign 0.5 # idle_alpha 0.66 hover_alpha 0.8

        else:
            add ProportionalScale("UI/fear question.webp", *res_tb(20)) xalign 0.5 yalign 0.5 # idle_alpha 0.66 hover_alpha 0.8

screen sex_details(girl):

    frame:
        background c_ui_darker
        xalign 0.5
        yalign 0.8

        has vbox

        spacing 6

        text __("%s's sexual preferences") % girl.name xalign 0.5 color c_orange

        text "" size res_font(6)

        grid 4 8 spacing 6:

            text __("Act") size res_font(14) bold True
            text __("Preference") size res_font(14) bold True
            text __("Will train") size res_font(14) bold True xalign 0.5
            text __("Will work") size res_font(14) bold True xalign 0.5

            for act in extended_sex_acts:
                text act.capitalize() size res_font(14) bold True

                if debug_mode:
                    $ text1 = " (" + str(round_int(girl.preferences[act])) + ")"
                else:
                    $ text1 = ""

                if girl.personality_unlock[act]:
                    text preference_color[girl.get_preference(act)] % __(girl.get_preference(act).capitalize()) + text1 size res_font(14)
                else:
                    text __("Unknown") + text1 size res_font(14) italic True

                if girl.personality_unlock[act]:

                    $ tch = girl.get_training_chance(act)

                    text str(round_int(tch)) + "%" size res_font(14) xalign 0.5:
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
                    text "?" size res_font(14) xalign 0.5


                if act == "naked":
                    text "" size res_font(14) xalign 0.5

                elif girl.personality_unlock[act]:

                    if girl.will_do_sex_act(act):

                        $ wch = girl.get_working_chance(act)

                        text str(round_int(wch)) + "%"  size res_font(14) xalign 0.5:
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
                        text "0%" size res_font(14) xalign 0.5 color color_dict["---"]

                else:
                    text "?" size res_font(14) xalign 0.5


## CHALLENGE SCREENS ##

screen challenge_menu(header=__("What do you do?"), challenges=[], cancel=False):
    # challenges is a list of arrays (caption, challenge_type, base_diff) where caption is the text displayed on the button.
    # challenge_type must be an existing type in MC.challenges. base_diff is the lowest possible difficulty to achieve success.
    # cancel must be an array (caption, return_value) if the challenge can be avoided.

    tag challenge_menu

    modal True
    zorder 5

    use overlay()

    frame xalign 0.5 yalign 0.5:

        has vbox spacing 10

        text header xalign 0.5 color c_brown

        hbox:

            for title, challenge_type, diff in challenges:
                $ chal = MC.challenges[challenge_type]
                $ diff = chal.adjust_diff(diff)
                $ ttip = "{b}" + __(chal.name) + __(" challenge{/b}: This challenges your {b}") + __(chal.stat.capitalize()) + "{/b} (" + str_int(MC.get_stat(chal.stat)) + ")" + __(". Estimated difficulty: {b}") + __(chal.estimate_diff(diff=diff)) + "{/b}."

                button background None action(Return(challenge_type)):
                    vbox:
                        button:
                            ysize yres(132)
                            yfill True
                            xpadding 6
                            ypadding 6
                            insensitive_background "#1A2B47E5"
                            at alpha_transform
                            action(Return(challenge_type))
                            tooltip ttip

                            fixed yalign 0.5:
                                fit_first True
                                add chal.get_pic(xres(200), yres(120)) # idle_alpha 0.66 hover_alpha 1.0
                                text chal.estimate_diff(diff=diff) size res_font(12)
                                frame background None xpadding 10 xalign 0.5 yalign 0.5:
                                    text title size res_font(18) bold True

        if cancel:
            textbutton cancel[0] action Return(cancel[1]) xalign 0.5

screen challenge(name, diff, raw=False, bonus=0, opponent_bonus=0):

    tag challenge

    modal True
    zorder 5

    $ chal = MC.challenges[name]

    default phase = 0

    frame background Frame(chal.pic.get(int(0.5*config.screen_width), int(0.5*config.screen_height))) xalign 0.5 yalign 0.5 xsize int(0.5*config.screen_width) ysize int(0.4*config.screen_height) xfill True yfill True:

        has vbox

        frame xalign 0.5 xfill True background "#22222288":
            text __("Player challenge: ") + chal.name xalign 0.5

        text ""

        hbox xfill True spacing 10:

            frame background "#22222288" xfill True xsize xres(250) ysize yres(160) xpadding 10 ypadding 10:

                vbox:
                    text __("Player ") + __(misc_name_dict[chal.stat.capitalize()]) + ": " + str_int(MC.get_stat(chal.stat, raw=True)) size res_font(18)
                    text __("Active bonus: ") + str_int(bonus + MC.get_stat(chal.stat, raw) - MC.get_stat(chal.stat, raw=True) + MC.get_effect("change", name + " challenges")) size int(config.screen_height*0.0222)
                    text ""

                    if phase >= 1:
                        text __("Roll: ") + "{image=" + "img_dice" + str(chal.d) + "}" size res_font(18)
                        text ""

                        if phase >= 2:
                            text __("Final Result: ") + str(round_int(chal.score)) size res_font(18)

                    elif chal.opposed:
                        textbutton "判定" action (SetScreenVariable("phase", 1), Play("sound", s_dice))
                    else:
                        textbutton "判定" action (SetScreenVariable("phase", 2), Play("sound", s_dice))



            frame background "#22222288" xsize xres(250) xfill True ysize yres(160) xalign 1.0 xpadding 6 ypadding 6:
                has vbox

                if chal.opposed:
                    text __("Opponent ") + __(chal.stat.capitalize()) + ": " + str_int(diff + opponent_bonus) size res_font(18)
                    text "" size res_font(18)
                    text ""

                    if phase >= 2:
                        text __("Roll: ") + "{image=" + "img_dice" + str_int(chal.d_op) + "}" size res_font(18)
                        text ""
                        text __("Final Result: ") + str_int(chal.score_op) size res_font(18)
                    elif phase == 1:
                        textbutton __("Roll") action (SetScreenVariable("phase", 2), Play("sound", s_dice))
                else:
                    text __("Difficulty: ") + str_int(diff) size res_font(18)

        if phase >= 2:
            text ""
            textbutton "好的" xalign 0.5 action Return()


#### LETTER SCREEN ####

screen letter(header="", message="", signature = ""): # Returns True upon closing

    tag letter

    modal True
    zorder 5

    key "mouseup_3" action (Return(True))

    frame xalign 0.5 ypos 0.1 xsize 0.8 ysize 0.9 xfill True yfill True xpadding 50 ypadding 25 background Frame("UI/paper.webp"):

        has vbox
        xsize 0.75
        xalign 0.5
        yfill True

        hbox xfill True yalign 0.1:
            text header xalign 0.0 size res_font(32) font "DejaVuSans.ttf" color c_black
            fixed fit_first True xalign 1.0 yalign 0.5:
                use close(act=Return(True), name = "close")

        text ""
        text ""

        text message size res_font(40) font "DejaVuSans.ttf" color c_black yalign 0.5

        text ""
        text ""

        text signature size res_font(44) font "DejaVuSans.ttf" xalign 1.0 color c_black yalign 0.9


#### RESOURCES ####

screen resource_tab(rlist="MC", sz = yres(15), sp = 3, x=0.0, y=0.0, bg=None): # If provided, rlist must be a list of tuples (resource_name, number)

    if rlist == "MC":
        frame background bg xpadding sp ypadding sp xpos x ypos y xanchor 0.5 yanchor 0.5:
            has hbox spacing sp//2 xalign 0 box_wrap True

            for resource in [resource_dict[r] for r in build_resources]:

                if MC.resources[resource.name]>0:
                    button background None action NullAction() tooltip (resource.description + __(" You have ") + str(MC.resources[resource.name]) + " " + __(misc_name_dict[resource.name]) + __(" in store.")) xpadding sp ypadding sp:
                        has hbox spacing sp*2 yalign 0.5
                        add resource.pic.get(sz, sz) yalign 0.5
                        if MC.resources[resource.name] < 100:
                            text str(MC.resources[resource.name]) size res_font(12) yalign 0.5
                        else:
                            text "99+" size res_font(10) yalign 0.5
    else:
        frame background bg xpadding sp ypadding sp xalign x yalign y:
            has hbox xalign 0 box_wrap True

            for resource, nb in rlist:
                button background None action NullAction() xpadding sp*2 ypadding sp*2:
                    has hbox box_wrap True spacing sp*2
                    add resource_dict[resource].pic.get(sz, sz) yalign 0.5
                    text str(nb) size res_font(14) yalign 0.5:
                        if MC.has_resource(resource, nb):
                            color c_emerald
                        else:
                            color c_red


screen resource_gain(resource, number): # Where resource is a string

    tag resource_gain

    zorder 10

    button style "girlbutton_blue":
        xalign 0.5
        yalign 0.5
        xsize 0.6
        ysize 0.5
        xpadding 50

        has hbox
        xalign 0.5
        yalign 0.5
        spacing 25

        add resource_dict[resource].get_pic(*res_tb(100))
        text "+" + str(round_int(number)) + " " + resource size res_font(28) yalign 0.5


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

        frame xsize xres(250) yanchor 1.0 ypos 0.2:
            has vbox
            text __("Weekly trade information") size res_font(14) italic True color c_brown
            hbox spacing 3 box_wrap True:
                for r in calendar.scarce:
                    $ resource = resource_dict[r]
                    if resource.rank <= story_flags["builder license"]:
                        button background None action NullAction() tooltip __("There is a shortage of ") + misc_name_dict[r.capitalize()] + __(" this week. Value is going up."):
                            has hbox spacing 3
                            add resource.pic.get(*res_tb(20)) yalign 0.5
                            text "▲" size res_font(16) color c_emerald yalign 0.5 font "1.ttf"

                for r in calendar.discounted:
                    $ resource = resource_dict[r]
                    if resource.rank <= story_flags["builder license"]:
                        button background None action NullAction() tooltip misc_name_dict[r.capitalize()] + __(" is plentiful this week. Value is going down."):
                            has hbox spacing 3
                            add resource.pic.get(*res_tb(20)) yalign 0.5
                            text "▼" size res_font(16) color c_red yalign 0.5 font "1.ttf"



    # Left frame

        frame xsize xres(250) ypos 0.2:
            has vbox

#            text(str(t))

            text __("Your resources") size res_font(14) italic True color c_brown

            button xfill True ysize yres(60) action (SetScreenVariable("source", "gold"), SetScreenVariable("source_name", "gold"), SetScreenVariable("source_nb", 0), SelectedIf(source=="gold")) tooltip __("Use your gold to buy resources"):
                selected_background c_emerald
                has hbox xfill True yfill True spacing 10
                add ProportionalScale("UI/coin.webp", *res_tb(40)) yalign 0.5
                hbox spacing 6 xfill True yalign 0.5:
                    text __("Gold") size res_font(18)
                    text '{:,}'.format(round_int(MC.gold)) xalign 1.0 size res_font(16)


            for r in build_resources:
                $ resource = resource_dict[r]

                if resource.rank <= story_flags["builder license"]:

                    button xfill True ysize yres(60) action (SetScreenVariable("source", resource), SetScreenVariable("source_name", resource.name), SetScreenVariable("source_nb", 0), SelectedIf(source==resource)) tooltip (__("Trade your ") + misc_name_dict[r] + __(" for other resources")):
                        selected_background c_emerald
                        has hbox xfill True yfill True spacing 10
                        add resource.pic.get(*res_tb(40)) yalign 0.5
                        vbox xfill True spacing 6 yalign 0.5:
                            hbox spacing 3:
                                text resource.name.capitalize() size res_font(18)
                                if r in calendar.discounted:
                                    text "▼" size res_font(14) yalign 0.5 font "1.ttf"
                                elif r in calendar.scarce:
                                    text "▲" size res_font(14) yalign 0.5 font "1.ttf"
                            hbox spacing 6 xfill True:
                                text __("In storage: ") size res_font(14) yalign 1.0
                                text str(MC.resources[resource.name]) xalign 1.0 size res_font(16)

        # Right frame

        if source:

            frame xsize xres(250) xalign 1.0 ypos 0.2:
                has vbox

                text __("Market resources") size res_font(14) italic True color c_brown

                button xfill True ysize yres(60):
                    if "gold" != source:
                        action (SetScreenVariable("target", "gold"), SetScreenVariable("target_name", "gold"), SetScreenVariable("target_nb", 0), SelectedIf("gold"==target))
                        tooltip __("Sell your ") + source_name + __(" for gold")
                        selected_background c_emerald

                    hbox xfill True yfill True spacing 10:
                        add ProportionalScale("UI/coin.webp", *res_tb(40)) yalign 0.5
                        vbox xfill True spacing 6 yalign 0.5:
                            text __("Gold") size res_font(18)
                            if "gold" != source:
                                hbox spacing 6:
                                    $ rate = get_exchange_rate(source, "gold")
                                    if rate < 1:
                                        $ text2 = __("Get 1 for ") + str_dec(1/rate, 1)
                                    else:
                                        $ text2 = __("Get ") + str_dec(rate, 1) + __(" for 1")

                                    text text2 size res_font(14)
                                    add source.pic.get(*res_tb(16))

                for r in build_resources:
                    $ resource = resource_dict[r]

                    if resource.rank <= story_flags["builder license"]:

                        button xfill True ysize yres(60):
                            if resource != source:
                                action (SetScreenVariable("target", resource), SetScreenVariable("target_name", resource.name), SetScreenVariable("target_nb", 0), SelectedIf(resource==target))
                                tooltip __("Trade ") + r +__(" in exchange for your ") + source_name
                                selected_background c_emerald
                            hbox xfill True yfill True spacing 10:
                                add resource.pic.get(*res_tb(40)) yalign 0.5
                                vbox xfill True spacing 6 yalign 0.5:
                                    hbox spacing 3:
                                        text resource.name.capitalize() size res_font(18)
                                        if r in calendar.discounted:
                                            text "▼" size res_font(14) yalign 0.5 font "1.ttf"
                                        elif r in calendar.scarce:
                                            text "▲" size res_font(14) yalign 0.5 font "1.ttf"
                                    if resource != source:
                                        hbox spacing 6:
                                            $ rate = get_exchange_rate(source, resource)
                                            if rate < 1:
                                                $ text2 = __("Get 1 for ") + str(round_up(1/rate))
                                            else:
                                                $ text2 = __("Get ") + str(round_up(rate)) + __(" for 1")

                                            text text2 size res_font(14)
                                            if source == "gold":
                                                add ProportionalScale("UI/coin.webp", *res_tb(16))
                                            else:
                                                add source.pic.get(*res_tb(16))

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

        frame xalign 0.5 yalign 0.6 xsize xres(400) xpadding 20 ypadding 20 background c_ui_dark:

            has vbox xfill True

            hbox xfill True spacing 6 ysize yres(70):
                if source != "gold":
                    add source.pic.get(*res_tb(60))
                else:
                    add ProportionalScale("UI/coin.webp", *res_tb(65))

                text "[source_nb]" size res_font(32) xalign 0.0 yalign 0.5:
                    if source == "gold":
                        if MC.gold >= source_nb:
                            color c_white
                        else:
                            color c_red
                    elif MC.resources[source_name] >= source_nb:
                        color c_white
                    else:
                        color c_red


                text "➜" size 54 xalign 0.5 yalign 0.5 font "1.ttf"

                text "[target_nb]" size res_font(32) color c_white xalign 1.0 yalign 0.5

                if target != "gold":
                    add target.pic.get(*res_tb(60)) xalign 1.0
                else:
                    add ProportionalScale("UI/coin.webp", *res_tb(65)) xalign 1.0


            hbox xfill True:
                textbutton "-" xsize xres(65) ysize yres(65) text_size res_font(32):
                    if rate < 1 and target_nb > 1:
                        action (SetScreenVariable("target_nb", target_nb-1), SetScreenVariable("source_nb", round_up((target_nb-1)/rate)))
                    elif rate >= 1 and source_nb > 1:
                        action (SetScreenVariable("source_nb", source_nb-1), SetScreenVariable("target_nb", round_up((source_nb-1)*rate)))

                if source == "gold":
                    $ text1 = __("Buy")
                else:
                    $ text1 = __("Trade")

                textbutton text1 xalign 0.5 xsize 0.8 ysize yres(65):
                    if source == "gold" and MC.gold >= source_nb:
                        action Return(("gold", target_name, source_nb, target_nb))
                        tooltip __("Buy ") + str(target_nb) + " " + target_name + __(" for ") + str(source_nb) + " " + target_name
                    elif MC.resources[source_name] >= source_nb:
                        action Return((source_name, target_name, source_nb, target_nb))
                        tooltip __("Trade ") + str(source_nb) + " " + source_name + __(" for ") + str(target_nb) + " " + target_name

                textbutton "+" xsize xres(65) ysize yres(65) text_size res_font(32) xalign 1.0:
                    if rate < 1:
                        action (SetScreenVariable("target_nb", target_nb+1), SetScreenVariable("source_nb", round_up((target_nb+1)/rate)))
                    elif rate >= 1:
                        action (SetScreenVariable("source_nb", source_nb+1), SetScreenVariable("target_nb", round_up((source_nb+1)*rate)))



## MODAL INVISIBLE SCREEN ##

screen modal():

    modal True

screen invisible_button():

    zorder 20

    key "K_UP" action Function(renpy.notify, __("Your precious keyboard can't save you now!"))
    key "K_DOWN" action Function(renpy.notify, __("Your precious keyboard can't save you now!"))

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

    $ mod_list = list(detected_mods) # Creates a list of keys from the dictionary
    $ mod_list.sort() # Sorts mods by name

    use game_menu(_("Mods")):

        if mod_list:
            default selected_mod = detected_mods[mod_list[0]]
        else:
            default selected_mod = None

        frame xsize 0.82 xpadding xres(20) ypadding yres(20):

            hbox xfill True spacing xres(6):
                viewport xsize xres(155):
                    mousewheel True
                    scrollbars "vertical"

                    has vbox xfill False

                    text __("Mod List") color c_brown

                    # style_group "pref"

                    for mod_name in mod_list:
                        $ mod = detected_mods[mod_name]
                        if mod:
                            button xsize xres(140) action SelectedIf(selected_mod == mod) hovered SetScreenVariable("selected_mod", mod), SetField(mod, "seen", True):
                                if not mod.seen:
                                    at blink

                                text mod.name size res_font(18):
                                    if mod.active:
                                        bold True

                if selected_mod:
                    $ selected_mod.seen = True

                    hbox xfill True spacing xres(6):
                        frame xpadding xres(10) ypadding yres(10):
                            has vbox
                            text selected_mod.full_name size res_font(24) bold True color c_darkorange
                            if selected_mod.active:
                                text __("(Active)") color c_emerald
                            else:
                                text __("(Inactive)") color c_grey

                            null height yres(16)
                        
                            viewport xsize xres(480):
                                mousewheel True
                                draggable True
                                scrollbars "vertical"
                                
                                vbox xfill True:
                                    if selected_mod.pic:
                                        frame xsize xres(250) background None:
                                            add selected_mod.pic.get() fit "contain"

                                    null height yres(16)

                                    text selected_mod.description size res_font(14) color c_brown
                        
                        if selected_mod.active:
                            textbutton "禁用模组" action renpy.curried_invoke_in_new_context(selected_mod.deactivate) xalign 1.0 xsize xres(100) text_size res_font(24)
                        else:
                            textbutton "激活模组" action renpy.curried_invoke_in_new_context(selected_mod.activate) xalign 1.0 xsize xres(100) text_size res_font(24)

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
        xsize xres(325)
        ysize int(0.7*config.screen_height)
        xmargin 3
        xalign 1.0
        ypos 0.1

        has vbox spacing 3

        text __("City girl interactions") size res_font(18) bold True

        text "" size res_font(14)

        hbox box_wrap True:
            $ choices = ["chat", "give", "flirt", "fun"]

            for cap in choices:
                textbutton cap.capitalize() action SelectedIf(menu_choice == cap) hovered SetScreenVariable("menu_choice", cap) text_size res_font(14) xpadding 6 ypadding 6 text_selected_bold True xsize xres(60)

        for cat in free_interact_dict[menu_choice]:

            if [top for top in free_interact_dict[cat] if top.is_shown(girl)]:

                text "" size res_font(18)
                text cat size res_font(14)

            for topic in free_interact_dict[cat]:
                if topic.is_shown(girl):
                    $ text1 = " ([topic.AP_cost]{image=img_AP})"

                    textbutton __(topic.caption) + text1 background None ypadding yres(0) text_size res_font(16):
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
#            text "OTHER" size res_font(14)

#            python:
#                try:
#                    custom_caption, custom_option_label, custom_cost = girl.init_dict["background story/free_interact_prompt"]
#                except:
#                    custom_caption, custom_option_label = girl.init_dict["background story/free_interact_prompt"] # For backwards compatibility with older _BK.ini
#                    custom_cost = 0
#                topic = GirlInteractionTopic("misc", None, custom_caption, "slave_custom_option", AP_cost=custom_cost)

#            textbutton topic.caption + " ([topic.AP_cost]{image=img_AP})" background None text_size res_font(14):
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
        xsize xres(325)
        ysize int(0.7*config.screen_height)
        xmargin 0
        xalign 1.0
        ypos 0.1

        has vbox spacing 3

        text __("Girl interactions") size res_font(18) bold True
#        text "Every interaction costs 1 AP" size res_font(14) italic True
        text "" size res_font(14)

        hbox box_wrap True:
            if free:
                $ choices = ["train", "magic"]
                if menu_choice not in choices:
                    $ menu_choice = "train"
            else:
                $ choices = ["chat", "train", "magic", "react", "misc"]

            for cap in choices:
                textbutton tl_cn(cap.capitalize(), misc_name_dict) action SelectedIf(menu_choice == cap) hovered SetScreenVariable("menu_choice", cap) text_size res_font(14) xpadding 6 ypadding 6 text_selected_bold True xsize xres(60)

        vbox xpos xres(12):
            for cat in interact_dict[menu_choice]:

                if [top for top in interact_dict[cat] if top.is_shown(girl)]:

                    null height yres(16)
                    text cat size res_font(14) bold True

                for topic in interact_dict[cat]:
                    if topic.is_shown(girl):

                        if topic.advanced:
                            hbox spacing 0:

                                textbutton __(topic.caption) + get_act_weakness_symbol(girl, topic.act) background None text_layout "nobreak" text_size res_font(13) text_color c_white xsize xres(100) text_xalign 0.0 action NullAction():
                                    if girl.personality_unlock[topic.act]:
                                        #tooltip __("You know that [girl.name] has ") + __(girl.get_reaction_to_act(topic.act)) + __(" for ") + __(topic.act) + __(" acts.")  源代码，为了翻译改变了顺序
                                        tooltip "你知道[girl.name]对" + __(topic.act) + "感到" + __(girl.get_reaction_to_act(topic.act))
                                    else:
                                        tooltip "你不知道[girl.name]对" + __(topic.act) + "的态度。"
                                    hovered Show("sex_details", girl=girl)
                                    unhovered Hide("sex_details")

                                if topic.type == "train":
                                    textbutton "劝诱" background None text_size res_font(13):
                                        if topic.is_available(girl, "lecture", free)[0]:
                                            text_hover_underline True
                                            action Return([topic, "lecture"])
                                            tooltip "向[girl.name]介绍关于" + __(topic.act) + "的好处。\n消耗" + str(normal_cost) + "{image=img_AP}。"
                                        else:
                                            text_color c_grey
                                            action NullAction()
                                            tooltip topic.is_available(girl, "lecture", free)[1]

                                textbutton "训练" background None text_size res_font(13):
                                    if topic.is_available(girl, "train", free)[0]:
                                        text_hover_underline True
                                        action Return([topic, "train"])
                                        if topic.gold_cost:
                                            tooltip "让[girl.name]逐渐适应" + __(topic.act) + "。\n消耗" + str(normal_cost) + "{image=img_AP}以及" + str(topic.get_gold_cost()) + "{image=img_gold}。"
                                        else:
                                            tooltip "让[girl.name]逐渐适应" + __(topic.act) + "。\n消耗" + str(normal_cost) + "{image=img_AP}。"
                                    else:
                                        text_color c_grey
                                        action NullAction()
                                        tooltip topic.is_available(girl, "train", free)[1]

                                $ pos_reaction, neg_reaction = girl.test_weakness(topic.act)

                                if not (pos_reaction or neg_reaction):
                                    $ ttip = event_color["a little bad"] % __("进阶训练已启用，但她对这种行为并不是很敏感。")
                                else:
                                    $ ttip = "你可以在进阶训练中发现她的性癖，并利用它们来提高训练的效率。"

                                textbutton "进阶训练" background None text_size res_font(13):
                                    if topic.is_available(girl, "advanced", free)[0]:
                                        text_hover_underline True
                                        action Return([topic, "advanced"])
                                        if topic.gold_cost:
                                            tooltip ttip + "\n消耗" + str(adv_cost) + "{image=img_AP}以及" + str(topic.get_gold_cost()) + "{image=img_gold}。"
                                        else:
                                            tooltip ttip + "\n消耗" + str(adv_cost) + "{image=img_AP}。"
                                    else:
                                        text_color c_grey
                                        action NullAction()
                                        tooltip topic.is_available(girl, "advanced", free)[1]
                        else:
                            if topic.label == "slave_hypnotize_method":
                                $ text1 = ": " + __(str(girl.magic_training))
                            else:
                                $ text1 = ""

                            if free:
                                $ text1 += " (0{image=img_AP}"
                            else:
                                $ text1 += " ([topic.AP_cost]{image=img_AP}"
                            if topic.gold_cost:
                                $ text1 += ", " + str(topic.get_gold_cost()) + "{image=img_gold}"
                            $ text1 += ")"

                            textbutton __(topic.caption) + text1 background None ypadding yres(3) text_size res_font(16):
                                if topic.is_available(girl, free=free)[0]:
                                    action Return(topic)
                                    text_hover_underline True
                                else:
                                    text_color c_grey
                                    action NullAction()
                                tooltip topic.is_available(girl, free=free)[1]

            if menu_choice == "misc" and girl.init_dict["background story/interact_prompt"]:
                text ""
                text __("OTHER") size res_font(14)

                python:
                    custom_caption = girl.init_dict["background story/interact_prompt"][0]
                    try:
                        custom_cost = girl.init_dict["background story/interact_prompt"][2]
                    except:
                        custom_cost = 0 # For backwards compatibility with older _BK.ini

                    topic = GirlInteractionTopic("misc", None, custom_caption, "slave_custom_option", AP_cost=custom_cost)

                textbutton topic.caption + " ([topic.AP_cost]{image=img_AP})" background None text_size res_font(16):
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


screen debug_pics(girl):

    modal True

    default mode = "soft"
    default pic = girl.profile

    key "mouseup_3" action Return()

    use dark_filter
    use show_sex_event(pic)

    vbox xalign 1.0 xfill False:

        hbox:
            textbutton "温和" text_size res_font(18) action SetScreenVariable("mode", "soft")
            textbutton "强硬" text_size res_font(18) action SetScreenVariable("mode", "hard")
            textbutton "FARM（待翻译）" text_size res_font(18) action SetScreenVariable("mode", "farm")
            textbutton "FIX（待翻译）" text_size res_font(18) action SetScreenVariable("mode", "fix")

        viewport xalign 1.0 xsize xres(250):
            mousewheel True
            draggable True
            scrollbars "vertical"

            has vbox xalign 1.0 xfill False

            if mode == "soft":

                textbutton __("Portrait") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("portrait", "profile", not_tags=["naked"]))
                textbutton __("Portrait Naked") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("portrait", "profile", and_tags=["naked"]))
                textbutton __("Profile") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("profile", "portrait", not_tags=["naked"]))
                textbutton __("Profile Naked") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("profile", "portrait", and_tags=["naked"]))

                textbutton __("Rest") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("rest", "profile", not_tags=["naked"], soft=True))
                textbutton __("Rest Naked") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("rest", "profile", and_tags=["naked"], soft=True))
                textbutton __("Waitress") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["waitress_tags"], perform_job_dict["waitress_tags2"], not_tags=["naked", "monster", "beast"], soft=True))
                textbutton __("Waitress Naked") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["waitress_tags"], perform_job_dict["waitress_tags2"], and_tags=["naked"], not_tags=["monster", "beast"], soft=True))
                textbutton __("Dancer") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["dancer_tags"], perform_job_dict["dancer_tags2"], not_tags=["naked", "monster", "beast"], soft=True))
                textbutton __("Dancer Naked") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["dancer_tags"], perform_job_dict["dancer_tags2"], and_tags=["naked"], not_tags=["monster", "beast"], soft=True))
                textbutton __("Masseuse") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["masseuse_tags"], perform_job_dict["masseuse_tags2"], not_tags=["naked", "monster", "beast"], soft=True))
                textbutton __("Masseuse Naked") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["masseuse_tags"], perform_job_dict["masseuse_tags2"], and_tags=["naked"], not_tags=["monster", "beast"], soft=True))
                textbutton __("Geisha") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["geisha_tags"], perform_job_dict["geisha_tags2"], not_tags=["naked", "monster", "beast"], soft=True))
                textbutton __("Geisha Naked") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["geisha_tags"], perform_job_dict["geisha_tags2"], and_tags=["naked"], not_tags=["monster", "beast"], soft=True))

                for k, tags in farm_holding_tags.items():
                    textbutton k.capitalize() text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(farm_holding_tags[k], soft=True))

            elif mode == "hard":

                textbutton __("Naked") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("naked", "rest", "profile", not_tags=["monster", "beast", "machine", "group", "bisexual"]))
                textbutton __("Service") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["service_tags"], "naked", "rest", "profile", not_tags=["monster", "beast", "machine", "group", "bisexual"]))
                textbutton __("Sex") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["sex_tags"], not_tags=["monster", "beast", "machine", "group", "bisexual"]))
                textbutton __("Anal") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["anal_tags"], not_tags=["monster", "beast", "machine", "group", "bisexual"]))
                textbutton __("Fetish") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["fetish_tags"], not_tags=["monster", "beast", "group", "bisexual"]))
                textbutton __("Bisexual Service") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["bisexual_tags"], perform_job_dict["service_tags"], and_tags= ["service"], not_tags=["monster", "beast", "machine", "group"], and_priority=False))
                textbutton __("Bisexual Sex") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["bisexual_tags"], perform_job_dict["sex_tags"], and_tags= ["sex"], not_tags=["monster", "beast", "machine", "group"], and_priority=False))
                textbutton __("Bisexual Anal") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["bisexual_tags"], perform_job_dict["anal_tags"], and_tags= ["anal"], not_tags=["monster", "beast", "machine", "group"], and_priority=False))
                textbutton __("Bisexual Fetish") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["bisexual_tags"], perform_job_dict["fetish_tags"], and_tags= ["fetish"], not_tags=["monster", "beast", "group"], and_priority=False))
                textbutton __("Group Service") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["group_tags"], perform_job_dict["service_tags"], and_tags= ["service"], not_tags=["monster", "beast", "machine"], and_priority=False))
                textbutton __("Group Sex") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["group_tags"], perform_job_dict["sex_tags"], and_tags= ["sex"], not_tags=["monster", "beast", "machine"], and_priority=False))
                textbutton __("Group Anal") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["group_tags"], perform_job_dict["anal_tags"], and_tags= ["anal"], not_tags=["monster", "beast", "machine"], and_priority=False))
                textbutton __("Group Fetish") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(perform_job_dict["group_tags"], perform_job_dict["fetish_tags"], and_tags= ["fetish"], not_tags=["monster", "beast"], and_priority=False))

            elif mode == "farm":

                textbutton __("Stallion Naked") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("naked", and_tags = ["big"], not_tags=["monster", "beast", "machine"]))
                textbutton __("Stallion Service") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("service", and_tags = ["big"], not_tags=["monster", "beast", "machine"]))
                textbutton __("Stallion Sex") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("sex", and_tags = ["big"], not_tags=["monster", "beast", "machine"]))
                textbutton __("Stallion Anal") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("anal", and_tags = ["big"], not_tags=["monster", "beast", "machine"]))
                textbutton __("Stallion Fetish") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("fetish", and_tags = ["big"], not_tags=["monster", "beast"]))
                textbutton __("Stallion Bisexual") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("bisexual", and_tags = ["big"], not_tags=["monster", "beast", "machine"]))
                textbutton __("Stallion Group") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("group", and_tags = ["big"], not_tags=["monster", "beast", "machine"]))

                textbutton __("Beast Naked") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["naked"]))
                textbutton __("Beast Service") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["service"]))
                textbutton __("Beast Sex") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["sex"]))
                textbutton __("Beast Anal") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["anal"]))
                textbutton __("Beast Fetish") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["fetish"]))
                textbutton __("Beast Bisexual") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["bisexual"]))
                textbutton __("Beast Group") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("beast", and_tags = ["group"]))

                textbutton __("Monster Naked") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["naked"]))
                textbutton __("Monster Service") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["service"]))
                textbutton __("Monster Sex") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["sex"]))
                textbutton __("Monster Anal") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["anal"]))
                textbutton __("Monster Fetish") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["fetish"]))
                textbutton __("Monster Bisexual") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["bisexual"]))
                textbutton __("Monster Group") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic("monster", and_tags = ["group"]))

                textbutton __("Machine Naked") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["naked"]))
                textbutton __("Machine Service") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["service"]))
                textbutton __("Machine Sex") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["sex"]))
                textbutton __("Machine Anal") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["anal"]))
                textbutton __("Machine Fetish") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["fetish"]))
                textbutton __("Machine Bisexual") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["bisexual"]))
                textbutton __("Machine Group") text_size res_font(18) action SetScreenVariable("pic", girl.get_pic(["machine", "toy"], and_tags = ["group"]))

            elif mode == "fix":
                for fix in fix_dict.values():

                    for act in fix.acts:
                        if act != "group":
                            $ not_tags.append("group")
                        if act != "bisexual":
                            $ not_tags.append("bisexual")

                        textbutton fix.name.capitalize() + " " + tl_cn(act.capitalize(), girl_related_dict) text_size res_font(14) action SetScreenVariable("pic", girl.get_fix_pic(act, fix, not_tags=not_tags))


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

    default filter = ""
    default ttip = ""

    key "mouseup_3" action Return()

    $ shown_gp = sorted(persistent.girl_packs, key=lambda x: (-(x in persistent.girl_mix[persistent.active_mix]), x))

    hbox:
        frame xsize 0.7 yfill True:
            has vbox

            text "女孩包列表" bold True drop_shadow (1, 1) font "bk.ttf" xpos xres(6)

            hbox box_wrap True:
                for mix_name in sorted(persistent.girl_mix):
                    textbutton mix_name.capitalize()[:25] action (SetField(persistent, "active_mix", mix_name), SelectedIf(persistent.active_mix==mix_name)) text_size res_font(18) text_selected_bold True tooltip __("Click here to see the %s girl mix.") % mix_name.capitalize()
                textbutton "+" action renpy.curried_invoke_in_new_context(add_mix) text_size res_font(18) tooltip __("Click here to create a new girl mix.")

            text "" size res_font(12)
            text "点击一个女孩的立绘来添加或删除这个女孩包。\n你可以通过点击“+”创建一个新的女孩包组合。" size res_font(14) color c_brown xpos xres(6)

            text "" size res_font(12)

            frame background c_ui_light xfill True:
                has hbox
                text __("Filter: ") size res_font(18) color c_brown
                input value ScreenVariableInputValue("filter", returnable=False) size res_font(18) color c_darkorange

            text "" size res_font(12)

            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                ymaximum 0.77
                yfill False

                has vbox spacing 0

                for gp in shown_gp:
                    $ pack_name = get_name(gp, full=True)
                    $ ttip = __("{b}%s{/b} {i}by %s{/i}\n\nVersion: %s\n\nDescription: %s\n\n") % (pack_name, gpinfo_dict[gp]["creator"], gpinfo_dict[gp]["version"], gpinfo_dict[gp]["description"])

                    if filter.lower() in pack_name.lower():
                        if show_rating:
                            $ rating, rtg_text = get_girlpack_rating(path=gp)

                        hbox spacing 12:

                            button xfill True ysize yres(82) ymargin 0 ypadding 0:
                                if gp in persistent.girl_mix[persistent.active_mix]:
                                    action RemoveFromSet(persistent.girl_mix[persistent.active_mix], gp)
                                    tooltip ttip + __("{i}Click to remove this girl pack from the mix.{/i}")
                                else:
                                    idle_background None
                                    action AddToSet(persistent.girl_mix[persistent.active_mix], gp)
                                    tooltip ttip + __("{i}Click to add this girl pack to the mix.{/i}")

                                hbox spacing 12 yalign 0.5:
                                    frame xalign 0.0 yalign 0.5 xsize xres(80) background None:
                                        add fast_portrait(gp, *res_tb(70)) xalign 0.5 yalign 0.5

                                    vbox xsize xres(360) yalign 0.5:
                                        text pack_name drop_shadow (1, 1) font "bk.ttf" size res_font(18)
                                        text __("by ") + gpinfo_dict[gp]["creator"] drop_shadow (1, 1) size res_font(14) italic True
                                        if show_rating:
                                            text __("{size=14}Rating: {/size}") + rating size res_font(18) drop_shadow (1, 1) # drop_shadow_color c_white
                                    if show_rating:
                                        text rtg_text size res_font(14) yalign 0.5 color c_darkbrown
            text "" size res_font(14)

            hbox:
                textbutton "删除组合" text_size res_font(18):
                    if persistent.active_mix != "default":
                        action renpy.curried_invoke_in_new_context(delete_mix, persistent.active_mix)
                textbutton "全部添加" action Function(add_all_to_mix, persistent.active_mix) text_size res_font(18)
                textbutton "移除全部" action Function(remove_all_from_mix, persistent.active_mix) text_size res_font(18)
                textbutton "返回" action Return() text_size res_font(18)

        frame background c_darkorange xfill True yfill True:
            if GetTooltip():
                text GetTooltip() color c_white

## ACHIEVEMENT SCREENS ##

screen achievement_notification(achievement_list, replay=False):

    zorder 20

    vbox xalign 0.5 yalign 0.5 spacing 10:
        at fadeinout
        for achievement in achievement_list:
            if replay:
                $ achv, level = achievement # Unpacking tuple
            else:
                $ achv, level = (achievement, None)

            frame xsize xres(320) ysize yres(150) xpadding 10 ypadding 10 background c_lightorange:

                has hbox yfill True spacing 12
                frame xalign 0.5 yalign 0.5:
                    if achv.pic:
                        add achv.pic.get(*res_tb(100))
                    else:
                        text __("Not found") italic True color c_red

                vbox yalign 0.5:
                    hbox spacing xres(6) ysize yres(24):
                        text achv.get_title(force_level=level) xalign 0.0 size res_font(20) bold True color c_prune # font "DejaVuSans.ttf"
                        null width xres(10)
                        if persistent.new_game_plus:
                            use crystal_display(achv.multi, sz = 18)
                    text achv.get_description(force_level=level) xalign 0.0 size res_font(20) font "DejaVuSans.ttf" color c_brown
    timer 6.5 action Hide("achievement_notification")

screen crystal_display(v, sz=24, prefix=" x "):

    hbox yalign 0.5 ysize yres(sz):
        add "misc" fit "contain" yalign 0.0
        text "{color=#fff}%s{/color}%s" % (prefix, str(v)) size res_font(sz) color c_purple yalign 1.0 bold True font "1.ttf"

screen achievements(main=False):

    tag menu

    default confirm_reset = False
    default total_crystals = count_achievements()

    key "mouseup_3":
        if main:
            action ShowMenu("galleries")
        else:
            action Return()

    vbox:
        fixed ysize yres(160):
            frame xfill True xpadding xres(10) ypadding xres(10) background c_lightorange:
                if selected_achievement:
                    hbox yfill True spacing 12:
                        frame xalign 0.5 yalign 0.5:
                            add selected_achievement.pic.get(*res_tb(125))

                        vbox xsize xres(500) yalign 0.5:
                            if persistent.new_game_plus:
                                use crystal_display(selected_achievement.multi)
                            text selected_achievement.get_title() xalign 0.0 size res_font(20) bold True color c_prune
                            text selected_achievement.get_description() xalign 0.0 size res_font(20) font "DejaVuSans.ttf" color c_brown

                        if selected_achievement.level < selected_achievement.level_nb:
                            vbox yalign 0.5:
                                text __("Next unlock:") italic True size res_font(20)
                                text selected_achievement.get_description(_next=True) xalign 0.0 size res_font(20) font "DejaVuSans.ttf" color c_brown

            vbox xalign 1.0 yalign 0.0:
                hbox:
                    if persistent.new_game_plus:
                        use crystal_display(total_crystals)
                        null width xres(10)
                    if not confirm_reset:
                        textbutton "清空成就" text_size res_font(14) ysize yres(36) xalign 0.2 yalign 1.0:
                            action SetScreenVariable("confirm_reset", True)
                    else:
                        textbutton "清空成就 (%s)" % (event_color["bad"] % "CONFIRM") text_size res_font(14) ysize yres(36) xalign 0.0 yalign 0.0:
                            action (Function(reset_achievements), SetScreenVariable("confirm_reset", False))

                    textbutton "返回"  ysize yres(36):
                        if main:
                            action ShowMenu("galleries")
                        else:
                            action Return()

        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            xfill True

            frame xfill True background c_ui_darkblue:
                hbox:
                    xalign 0.5
                    spacing xres(6)
                    box_wrap True

                    for achv in achievement_list:
                        if achv.level > 0:
                            textbutton achv.get_title(_button=True) xsize xres(150) ysize yres(50) text_size res_font(12) action NullAction() hovered [SetVariable("selected_achievement", achv), SelectedIf(selected_achievement==achv)]
                        else:
                            textbutton "???" xsize xres(150) ysize yres(50)

                # if len(achievement_list) % 6 > 0:
                #     for _ in range(6 - len(achievement_list) % 6):
                #         null



## CONTRACT SCREENS ##

init:
    transform contract_result_transform:
        alpha 0.0
        linear 0.25 alpha 1.0

screen contracts(contracts, free=False):

    frame xalign 0.5 yalign 0.5:
        has vbox

        text __("Choose a contract") xalign 0.5 yalign 0.5 color c_brown

        text "" size res_font(14)

        hbox:
            for con in contracts:
                vbox:
                    # if not free:
                    frame xalign 0.5 xfill False yfill False:
                        text __("Fee: %s gold.") % str(con.base_value) size res_font(14) color c_brown bold True
                    button action Return(con) xpadding 6 ypadding 6:
                        use contract_tab(con)

        text "" size res_font(14)

        textbutton "跳过" action Return("back") xalign 0.5 yalign 0.5

screen contract_tab(contract, x=320, active=False):

    modal True
    if active:
        use dark_filter()
        key "mouseup_3" action Return()
        use close(Return(), "back")

    frame xalign 0.5 yalign 0.5 xsize xres(x) ysize yres(600) xpadding 10 ypadding 10:
        viewport:
            mousewheel True
            draggable False
            scrollbars "vertical"

            has vbox spacing 12

            vbox spacing 3:
                text __("The ") + contract.location.name drop_shadow (1, 1) font "bk.ttf" color c_brown
                text contract.title drop_shadow (1, 1) font "bk.ttf" color c_prune

            vbox spacing 3:
                add contract.location.get_pic(xres(200), yres(140)) insensitive_alpha 0.33 idle_alpha 0.66 hover_alpha 1.0

                text contract.description size res_font(12) color c_brown

            # text "" size res_font(14)

            vbox spacing 6:
                text __("Tasks") size res_font(16) bold True color c_prune

                for tsk in contract.tasks:
                    vbox spacing 3 xpos 0.02:
                        text tsk.title size res_font(13) bold True color c_prune
                        for req in tsk.get_requirements():
                            text req size res_font(13) color c_brown

            vbox spacing 3:
                text __("Bonus requirement") size res_font(16) bold True color c_prune
                text contract.get_special_description() size res_font(13) color c_brown

            hbox:
                text __("Reward: ") size res_font(16) bold True color c_prune
                text "%s gold" % str(contract.get_value()) size res_font(16) bold True color c_darkgold


screen pick_girl(girls, nb, contract=None):
    hbox spacing 20:
        use girl_stats(selected_girl, "postings")

        vbox:
            if contract:
                use contract_tab(contract, x=400)
            use girl_select(girls, True)
            textbutton "发送" action Return(selected_girl) xalign 0.85 ypos -0.25


screen contract_result(contract, x=450):

    default t = 0
    default earned_gold = contract.get_value()
    default displayed_gold = 0

    frame xalign 0.5 yalign 0.5 xsize xres(x) xpadding 10 ypadding 10:
        has vbox spacing 12

        vbox spacing 3:
            text __("The ") + contract.location.name drop_shadow (1, 1) font "bk.ttf" color c_brown
            text contract.title drop_shadow (1, 1) font "bk.ttf" color c_prune

        vbox spacing 3:
            add contract.location.get_pic(xres(200), yres(140)) insensitive_alpha 0.33 idle_alpha 0.66 hover_alpha 1.0

            text contract.description size res_font(12) color c_brown

        # text "" size res_font(14)

        vbox spacing 9:
            text __("Tasks") size res_font(16) bold True color c_prune

            for tsk in contract.tasks:
                hbox:
                    vbox xsize xres(320) spacing 3:
                        text tsk.title size res_font(13) bold True color c_prune
                        for req in tsk.get_requirements():
                            text req size res_font(13) color c_brown xpos 0.02
                    if t >= contract.tasks.index(tsk) + 1:
                        if tsk.result:
                            text str_int(tsk.value) + __(" gold") color c_darkgold yalign 0.5 size res_font(13) at contract_result_transform
                        else:
                            text __("{color=[c_red]}{i}Failed{/i}{/color}") yalign 0.5 size res_font(13) at contract_result_transform

        hbox:
            vbox xsize xres(320) spacing 3:
                text __("Bonus requirement") size res_font(16) bold True color c_prune
                text contract.get_special_description() size res_font(13) color c_brown
            if t >= len(contract.tasks) + 1:
                if contract.special_bonus != 1.0:
                    text str(contract.get_special_value()) + __(" gold") color c_darkgold yalign 0.5 size res_font(13) at contract_result_transform
                else:
                    text __("{i}Missing{/i}") color c_lightred yalign 0.5 size res_font(13) at contract_result_transform

        vbox spacing 6:
            text __("Score") size res_font(16) bold True color c_prune
            hbox:
                text ""
                for i in [tsk for tsk in contract.tasks if tsk.result]:
                    if t >= contract.tasks.index(i) + 1:
                        text "{image=img_star}" at contract_result_transform
                if t >= len(contract.tasks) + 1 and contract.special_bonus > 1.0:
                    text "{image=img_star}" at contract_result_transform

        hbox:
            text __("Reward: ") size res_font(16) bold True color c_prune

            text __("%s gold") % min(displayed_gold, earned_gold) size res_font(16) bold True:
                if earned_gold > 0:
                    color c_darkgold
                else:
                    color c_red

        textbutton "好的" action Return() xalign 0.5

    if t < len(contract.tasks) + 1:
        timer 0.8 action [SetScreenVariable("t", t + 1), Play("sound",s_spell)] repeat True

    if displayed_gold < earned_gold:
        timer 0.1 action [SetScreenVariable("displayed_gold", round_up((1 - 0.15) * displayed_gold + 0.15 * earned_gold)), Play("sound2",s_gold)] repeat True

screen increment_counter(startv = 0, stopv = 1000, duration = 3.0, _caption = "%s gold", _background = None, _size = 16, _color = c_white, _sound=s_gold): # Displays an incremental counter counting from startv to stopv

    default displayv = startv

    frame align (0.5, 0.5) background _background:
        has vbox
        text _caption % '{:,}'.format(displayv) color _color size res_font(_size) bold True

    if stopv > startv and displayv < stopv:
        timer 0.01 action [SetLocalVariable("displayv", displayv + round_up(max(1, min(displayv, stopv-displayv))/duration/10)), Play("sound2", _sound)] repeat True
    else:
        null # Needed to avoid graphical glitch

    if stopv < startv and displayv > stopv:
        timer 0.01 action [SetLocalVariable("displayv", displayv - round_up(max(1, min(displayv, startv-displayv))/duration/10)), Play("sound2", _sound)] repeat True
    else:
        null

screen increment_display(title="", _caption="%s gold", pic=None, side_pic=None, startv = 0, stopv = 1000, duration=3.0, _size = 16, _color = c_white, _sound=s_gold):

    modal True

    key "mouseup_3" action (Hide(), Return())

    frame xsize 0.33 align (0.5, 0.5) background c_ui_darkblue:
        has vbox spacing yres(10)

        text title xalign 0.5

        if pic:
            fixed xalign 0.5 xfill True fit_first True:
                add pic yalign 0.5 fit "contain"

        if side_pic:
            hbox:
                fixed xsize yres(120) ysize yres(120):
                    add side_pic yalign 0.5 fit "contain"
                use increment_counter(startv = startv, stopv = stopv, duration = duration, _caption = _caption, _size = _size, _color = _color, _sound=_sound)

        textbutton "好的" xalign 0.5 action (Hide(), Return())


screen auction_brothel(name, pic, price):

    # modal True

    tag brothel_auction

    zorder 10

    button:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20
        xsize 0.3
        ysize 0.4

        has vbox
        xalign 0.5
        yalign 0.5
        spacing 20

        add pic xalign 0.0 fit "contain"
        use increment_counter(0, price, _caption = __("Sold " + name + " for {b}%s{/b} {image=img_gold}"), _color = c_emerald)
        # text __("Sold %s for {b}%s{/b} {image=img_gold}") % (name, '{:,}'.format(price)) color c_emerald size res_font(16) xalign 0.5 yalign 0.5


screen goal_ttip():

    frame xalign 0.5 yalign 0.5 xsize 0.5 xpadding xres(20) ypadding yres(20) background c_ui_darkblue:
        has vbox spacing yres(10)
        text "{image=tb goal} 第%i章 - 主线目标" % game.chapter size res_font(28) color c_white bold True xalign 0.5
        text "" size res_font(14)

        for cat, goal_desc, tb in game.get_goals():
            vbox:
                hbox spacing 10:
                    add tb
                    text cat size res_font(18) bold True color goal_colors[cat] yalign 0.5
                text goal_desc size res_font(18) color c_white


## EVIL POWERS SCREENS ## Thanks to who designed these screens

## Overlay

# MC mojo points (topscreen)
screen mojo_bar:

    zorder 10

    use adv_tooltip()


    hbox xalign 0.5 spacing xres(30) ypos 0.02:
        for mcolor, mpoints in MC.mojo.items():
            hbox spacing xres(6):
                imagebutton:
                    idle "mojo_" + mcolor
                    action NullAction()
                    tooltip persistent.help_dict[mcolor + " mojo"]
                text "%i" % int(mpoints) bold True size res_font(16) yalign 0.5


## Cards

# Card detail (right side of screen)
screen power_detail(pow):

    frame xalign 1.0 xsize 0.2 ypos 0.1 xmargin xres(6) top_padding yres(6) bottom_padding yres(12) background c_ui_dark:
        vbox spacing yres(3):

            add pow.pic.get() xalign 0.5

            text pow.name + {True : " (S)", False : ""}[pow.super] size res_font(24) bold True
            text pow.description size res_font(14)

            text "魔力消耗:" size res_font(18) bold True
            hbox spacing xres(6):
                if conduit:
                    $ mod = conduit.get_effect("change", "mojo cost")
                else:
                    $ mod = 0
                for mcolor, mcost in pow.get_mojo_cost():
                    if mcost != 0:
                        fixed fit_first True:
                            add "UI/Powers/orb_[mcolor].webp" size (40, 40)
                            text "%i" % (mcost + mod) bold True size res_font(20) outlines [(1, "#000", 0, 0)] at truecenter:
                                if mod:
                                    color c_green

            text "理智消耗:" size res_font(18) bold True
            hbox spacing xres(3):
                add "UI/Powers/sanity_cost_[pow.sanity_lvl].webp" zoom 1.2
                text "[pow.sanity_lvl]" size res_font(14) yalign 0.4

            text "目标:" size res_font(18) bold True
            $ target = pow.target.capitalize()
            text target.capitalize() size res_font(14)

            if pow.duration:
                text "持续时间:" size res_font(18) bold True
                text "[pow.duration] days" size res_font(14)


# Card deck
screen power_draw(x=0.505, y=0.425): # Check if deck can be drawn must happen before the screen is shown

    key "mouseup_3" action Return("back")
    use close(Return("back"))

    button style "inv_no_padding" xsize yres(200) ysize yres(200) align (x, y):
        action (Return("draw"), Hide())

        text "抽一张牌" color c_white drop_shadow (2, 2) align (0.5, 0.5) at blink(_duration=0.5, _pause=0.5)

# Card hand
screen power_hand(hand, context="idle", start_at = 0, x=0.5, y=0.75):

    default selected_card = None
    default _super = False
    default _super_on = [SelectedIf(True), ToggleScreenVariable("_super")]
    default _super_off = [SelectedIf(False), ToggleScreenVariable("_super"), Return("supercharge")]

    if _super:
        key "keydown_K_LSHIFT" action _super_on
        key "keydown_K_RSHIFT" action _super_on
        key "keyup_K_LSHIFT" action _super_off
        key "keyup_K_RSHIFT" action _super_off
    else:
        key "keydown_K_LSHIFT" action _super_off
        key "keydown_K_RSHIFT" action _super_off
        key "keyup_K_LSHIFT" action _super_on
        key "keyup_K_RSHIFT" action _super_on

    key "mouseup_3" action Return("back")
    use close(Return("back"))

    $ card_space = (evil_card_size*1.15)/config.screen_width

    if not hand:
        text __("You have used all of your powers this week.") xalign 0.5 yalign 0.45 drop_shadow (1, 1) at blink

    for i in range(len(hand)):
        $ xc = x + (card_space * i) - card_space * len(hand)/2 + card_space/2
        $ pow = hand[i].get(_super)

        # Using conditions instead of a transform to avoid blur when zooming
        if pow == selected_card:
            $ size_boost = 1.15
        else:
            $ size_boost = 1.0

        if i >= start_at: # Only newly drawn cards will be flipped
            use power_card(pow, context, xc, y, size_boost)
        else:
            use power_card(pow, context, xc, y, size_boost, existing=True)

    if hand and context == "idle":
        button pos (0.675, 0.4) xsize yres(45) ysize yres(45) style "push_button":
            if _super:
                # at jitter
                action _super_on
                tooltip __("Click or hold shift to deactivate supercharge (boost powers for more mojo and sanity)")
                add "supercharge_card" xsize yres(40) ysize yres(40) xalign 0.5 yalign 0.5
            else:
                action _super_off
                tooltip __("Click or hold shift to activate supercharge (boost powers for more mojo and sanity)")
            text "S" size res_font(28) bold True xalign 0.5 yalign 0.5:
                if not _super:
                    color c_brown

    # Card detail (right side of screen)
    if selected_card:
        use power_detail(selected_card.get(_super))


screen power_card(pow, context = "idle", x = 0, y = 0, size_boost=1.0, existing=False):

    sensitive False

    $ xs = int(evil_card_size * size_boost)
    $ ys = int(xs * 1.6)

    if context == "move":
        frame style "inv_no_padding" xanchor 0.5 yanchor 1.0 at move_to(start_pos = (0.5, 0.45), new_pos = (x, y), fades=1.0):
            if existing: # Previously drawn cards show face up
                use power_card_content
            else:
                add "UI/Powers/cards/back.webp" size (xs, ys) perspective True

    elif context == "flip" and not existing: # Only newly drawn cards will be flipped
        frame style "inv_no_padding" xanchor 0.5 yanchor 1.0 xpos x ypos y:
            fixed fit_first True at flip_to_back:
                # Front face
                fixed fit_first True at reverse_horizontal:
                    use power_card_content
                # Back face
                fixed fit_first True at disappear_in(0.4):
                    add "UI/Powers/cards/back.webp" size (xs, ys) perspective True

    elif context == "burn":
        frame style "inv_no_padding" xanchor 0.5 yanchor 1.0 xpos x ypos y:
            fixed xsize xs ysize ys:
                fixed at disappear_in(0.8):
                    use power_card_content
                add burn_card(xs, ys)

    else:
        button style "inv_no_padding":
            xanchor 0.5 yanchor 1.0 xpos x ypos y
            hovered SetScreenVariable("selected_card", pow)
            unhovered SetScreenVariable("selected_card", None)
            action (SetScreenVariable("selected_card", pow), Return(pow), Hide())
            use power_card_content

screen power_card_content:

    zorder 0

    if pow.type == "Platinum":
        $ col = evpower_color["platinum"][pow.super]
    else:
        $ col = evpower_color["regular"][pow.super]

    fixed fit_first True xysize (xs, ys):
        if pow.super:
            add "UI/Powers/cards/front_[pow.type]_super.webp" perspective False fit "contain"
        else:
            add "UI/Powers/cards/front_[pow.type].webp" perspective False fit "contain"

        vbox xsize 0.98 xalign 0.5 spacing 0:

            # Display card art
            add pow.pic.get() fit "contain" #xoffset 1 yoffset 6

            # Display sanity cost (per level basis)
            add "UI/Powers/sanity_cost_[pow.sanity_lvl].webp" zoom size_boost - 0.15 xalign 0.5 yoffset -yres(16)

        if pow.super:
            add "supercharge_card" size (xs, ys) perspective False alpha 0.65

        frame xfill True xpadding int(xs/25) ypadding int(ys/25) ysize 0.33 xalign 0.5 yalign 1.0 background None:
            has vbox spacing yres(2) xfill True yfill True
            # Display name and short description
            text pow.name bold True color col xalign 0.5 yalign 0.0 size res_font(1+int(9 * size_boost)) text_align 0.5
            text pow.short_description color col xalign 0.5 yalign 0.0 size res_font(1+int(7 * size_boost)) text_align 0.5

        vbox align (0.05, 0.05) spacing yres(3):
            for mcolor, mcost in pow.get_mojo_cost():
                if mcost > 0:
                    fixed fit_first True:
                        add "mojo_[mcolor]" size res_tb(20)
                        text "[mcost]" size res_font(12) outlines [(1, "#000", 0, 0)] at truecenter

        if pow.duration:
            hbox align (0.95, 0.05):
                add "UI/Powers/timer_duration.webp" size res_tb(20)
                text str(pow.duration) size res_font(12) xalign 0.5 yalign 0.75 outlines [(1, "#000", 0, 0)]


# conduit and target selection

screen power_target(pow):

    modal True
    zorder 0

    key "mouseup_3" action [Return("back"), Hide()]

    default selected_conduit = None
    default selected_target = None
    default _selected = None
    default blocked = []
    default block_dict = {}

    if pow.target == "city girl" and _selected in game.free_girls:
        use girl_stats(_selected, context="free")
    else:
        use girl_stats(_selected, context="powers")
    use power_detail(pow)

    if selected_target and (selected_target == selected_conduit): # Cannot select the same target as conduit
        $ selected_target = None

    frame background c_ui_dark xpadding yres(25) ypadding yres(25) xmaximum 0.45 ysize 0.8 xalign 0.6 ypos 0.1:

        use close([Return("back"), Hide("power_target")])

        hbox spacing xres(25) xfill True:

            for girl in farm.girls:
                if not debug_mode:
                    if girl.last_power == calendar.time:
                        $ blocked.append(girl)
                        $ block_dict[girl] = __("This girl already conducted a power today.")
                    elif girl.broken:
                        $ blocked.append(girl)
                        $ block_dict[girl] = __("This girl's sanity is broken.")

            vbox xsize xres(200) ysize 0.9:
                hbox:
                    text __("Conduit: ") bold True
                    if isinstance(selected_conduit, Girl):
                        text selected_conduit.fullname bold True color c_yellow
                text ""
                use girl_vp_selector([("farm", farm.girls)], _selected, "selected_conduit", blocked=blocked, block_dict=block_dict)

            vbox xfill True ysize 0.9:
                hbox:
                    text __("Target: ") bold True
                    if isinstance(selected_target, Girl):
                        text selected_target.fullname bold True color c_yellow

                    elif pow.target == "conduit":
                        text __("Herself") bold True color c_pink
                    elif pow.target == "MC":
                        text MC.name bold True color c_main
                    else:
                        text pow.target.capitalize() bold True color c_yellow

                text ""

                if pow.target == "other girl":
                    if selected_conduit:
                        $ blocked.append(selected_conduit)
                        $ block_dict[selected_conduit] = __("You cannot choose the conduit as the target.")
                    if pow.power.startswith("leech"):
                        if selected_conduit:
                            $ glist1 = [g for g in MC.girls if g.rank <= selected_conduit.rank]
                            $ glist2 = [g for g in farm.girls if g.rank <= selected_conduit.rank]
                        else:
                            $ glist1 = glist2 = None
                    else:
                        $ glist1 = MC.girls
                        $ glist2 = farm.girls
                    use girl_vp_selector([("brothel", glist1), ("farm", glist2)], _selected, "selected_target", blocked=blocked, block_dict=block_dict)
                elif pow.target == "city girl":
                    use girl_vp_selector([("city", game.free_girls)], _selected, "selected_target", blocked=blocked, block_dict=block_dict)

        textbutton "提交" xalign 0.95 yalign 1.0 text_size res_font(24) text_bold True:
            if pow.target in ("other girl", "city girl") and selected_conduit and selected_target:
                action (Return((selected_conduit, selected_target)), Hide())
            elif pow.target not  in ("other girl", "city girl") and selected_conduit:
                action (Return(selected_conduit), Hide())
            elif not selected_conduit:
                text_color c_lightgrey
                action NullAction() tooltip __("Choose a conduit for your power first.")
            else:
                text_color c_lightgrey
                action NullAction() tooltip __("Choose a target for your power first.")

screen girl_vp_selector(girl_lists, _selected = None, return_value = "selected_target", blocked=None, block_dict=None): # girl_lists must be a list of tuples (title, glist)

    # Parent screen can pass a list of blocked girls. It should include a block_dict variable storing tooltips explaining why a girl is blocked.

    if blocked and _selected in blocked:
        $ _selected = None

    viewport xfill True:
        mousewheel True
        arrowkeys True
        pagekeys True
        scrollbars "vertical"
        xalign 0.0

        has vbox spacing yres(6)

        for title, glist in girl_lists:
            textbutton title.capitalize() style "inv_no_padding" text_bold True
            if glist:
                for girl in glist:
                    if title == "city":
                        use girl_button(girl, bsize="x12", context="free", custom_action=[SetScreenVariable("_selected", girl), SetScreenVariable(return_value, girl)], hovered_action=[SetScreenVariable("_selected", girl)], unhovered_action=[SetScreenVariable("_selected", None)], custom_ttip=None)
                    elif blocked and girl in blocked:
                        use girl_button(girl, bsize="x12", context="powers", custom_action=NullAction(), hovered_action=[SetScreenVariable("_selected", girl)], unhovered_action=[SetScreenVariable("_selected", None)], custom_ttip=block_dict[girl])
                    else:
                        use girl_button(girl, bsize="x12", context="powers", custom_action=[SetScreenVariable("_selected", girl), SetScreenVariable(return_value, girl)], hovered_action=[SetScreenVariable("_selected", girl)], unhovered_action=[SetScreenVariable("_selected", None)], custom_ttip=None)

            else:
                textbutton "无可用女孩" style "inv_no_padding" text_size res_font(16) text_italic True xsize xres(300)
            null



# Final screens

screen mojo_payment(pow, conduit, other_girl = None):
    modal True

    key "mouseup_3" action [Return(False), Hide()]

    use power_detail(pow)

    # add "#0005"

    frame:
        align (0.5, 0.2)
        xsize 0.3
        xpadding xres(25)
        top_padding xres(15)
        bottom_padding xres(25)
        background c_ui_dark

        vbox xfill True:
            spacing yres(12)
            use close([Return(False), Hide("mojo_payment")])

            # Confirmation info
            text pow.name bold True xalign 0.5
            null
            hbox xalign 0.5:
                vbox xalign 0.0 spacing yres(12):
                    text __("Supercharge: ") size res_font(14)
                    text __("Conduit: : ") size res_font(14)
                    text __("Target: ") size res_font(14)

                    # Reminder: The main loop checks that MC has enough to pay before this screen is shown
                    text __("Payment: ") size res_font(14)

                vbox xalign 0.0 spacing yres(12):
                    text {True : __("ON"), False : __("OFF")}[pow.super] size res_font(14) bold True
                    text conduit.fullname size res_font(14) bold True

                    if pow.target == "conduit":
                        text __("Herself") size res_font(14) bold True
                    elif pow.target == "MC":
                        text MC.name size res_font(14) bold True
                    elif pow.target in ("other girl", "city girl"):
                        text other_girl.fullname size res_font(14) bold True
                    else:
                        text pow.target.capitalize() size res_font(14) bold True

                    hbox xalign 0.5:
                        spacing xres(20)
                        $ mod = conduit.get_effect("change", "mojo cost")
                        $ purple_cost = MC.get_missing_mojo(pow.get_mojo_cost(conduit))

                        for mcolor, mpoints in (pow.get_mojo_cost() + [("purple", purple_cost)]):
                            if mpoints + mod > MC.mojo[mcolor]:
                                $ val = MC.mojo[mcolor]
                            else:
                                $ val = mpoints + mod

                            if mpoints > 0:
                                fixed fit_first True:
                                    add "mojo_[mcolor]" size res_tb(25) # Color
                                    text "%i" % val bold True size res_font(16) outlines [(1, "#000", 0, 0)] at truecenter: # Amount
                                        if mod:
                                            color c_green

            textbutton __("Cast"):
                text_bold True
                text_size res_font(18)
                xalign 0.5
                action (Return(True), Hide())


screen mojo_trade(sell_rate=2, buy_rate=1): # Returns a dict with changes to commit

    modal True

    default change_dict = {"purple" : 0, "green" : 0, "blue" : 0, "red" : 0, "yellow" : 0}

    key "mouseup_3" action [Return("back"), Hide()]

    frame background c_ui_darker:
        xpadding yres(30)
        ypadding yres(30)
        xalign 0.5
        yalign 0.5

        has vbox
        spacing yres(12)

        use close([Return("back"), Hide("mojo_trade")])

        text __("Current rate:\n{b}%i {image=mojo purple} for %i {image=mojo green}{image=mojo blue}{image=mojo red}{image=mojo yellow}{/b}") % (buy_rate, sell_rate) size res_font(16) xalign 0.5

        hbox:
            spacing xres(12)

            fixed fit_first True:
                align (0.5, 0.5)
                $ mpoints = MC.mojo["purple"]
                add "UI/Powers/orb_purple.webp" size res_tb(25)
                text "{b}%i{/b}" % (int(mpoints) + change_dict["purple"]) size res_font(16) outlines [(1, "#000", 0, 0)] at truecenter:
                    if change_dict["purple"]:
                        color c_green

            text "|" size res_font(20) yalign 0.5 color c_white + "AA"

            grid 2 2:
                spacing yres(20)
                for mcolor, mpoints in MC.mojo.items():
                    if mcolor != "purple":
                        hbox:
                            spacing xres(3)

                            if mpoints + change_dict[mcolor] >= sell_rate:
                                textbutton "+" xysize res_tb(20):
                                    action (SetDict(change_dict, mcolor, change_dict[mcolor]-sell_rate), SetDict(change_dict, "purple", change_dict["purple"]+buy_rate))
                                    yalign 0.5
                            else:
                                null width yres(20)

                            fixed fit_first True:
                                add "UI/Powers/orb_[mcolor].webp" size res_tb(30)
                                text "{b}%i{/b}" % (int(mpoints) + change_dict[mcolor]) size res_font(18) outlines [(1, "#000", 0, 0)] at truecenter:
                                    if change_dict[mcolor]:
                                        color c_red

                            if change_dict[mcolor]:
                                textbutton "-" xysize res_tb(20):
                                    action (SetDict(change_dict, mcolor, change_dict[mcolor]+sell_rate), SetDict(change_dict, "purple", change_dict["purple"]-buy_rate))
                                    yalign 0.5
                            else:
                                null width yres(20)

        hbox:
            xalign 0.5
            textbutton "{b}清除{/b}" text_size res_font(16) action SetLocalVariable("change_dict", {"purple" : 0, "green" : 0, "blue" : 0, "red" : 0, "yellow" : 0})
            textbutton "{b}提交{/b}" text_size res_font(16) action (Return(change_dict), Hide())


screen micro_transac():

    default x = ui.adjustment(100)

    add "micro_transac_rain"

    frame background c_ui_darkblue:
        xysize (0.66, 0.66)
        align (0.5, 0.5)


        vbox xfill True:
            viewport:
                xadjustment x
                draggable True
                ysize 0.1
                frame background c_ui_dark:
                    text __("                                                                                                  Buy Sill's 'Slutty Schoolgirl' outfit for only $29.99...                                                   Get the ultimate 'Hung like a horse' armor for just $149.99 (2 minutes remaining)...                                                 *SEXY* Recruit the exciting new character 'Lara Crotch' for only $49.99...                                                 *SPECIAL SALE* Don't miss out on our latest season pass 'Summer of a cocksucker' for only $69.99 (valid for 7 days)...                                                                                                                                                                                    ") layout "nobreak"

            hbox spacing xres(20) xalign 0.5:
                button xsize xres(200) yfill True action NullAction():
                    vbox xfill True yfill True:
                        vbox yalign 0.5 xfill True:
                            fixed align 0.5, 0.5 ysize 0.45:
                                add "misc" xalign 0.5
                                text __("Losers'\nchoice!") align 0.5, 0.5 outlines [(1, "#000", 0, 0)] size res_font(24) at blink(0.5, 0.5)
                            null height yres(10)
                            text __("x100 P2W Crystals") xalign 0.5 yalign 0.5 bold True font "1.ttf"
                        frame xfill True yalign 0.9 ysize yres(60) background Frame("orange_button", borders=gui.button_borders):
                            text "$14.99" font "1.ttf" align 0.5, 0.5 size res_font(32) bold True at repeat_bounce

                button xsize xres(200) yfill True action NullAction():
                    vbox xfill True yfill True:
                        vbox yalign 0.5 xfill True:
                            fixed align 0.5, 0.5 ysize 0.45:
                                add "misc" xalign 0.25
                                add "misc" xalign 0.75 ypos 0.1
                                text __("Popular\nchoice!!") align 0.5, 0.5 outlines [(1, "#000", 0, 0)] size res_font(24) at shake
                            null height yres(10)
                            text __("x1,000 P2W Crystals") xalign 0.5 yalign 0.5 bold True font "1.ttf"
                        frame xfill True yalign 0.9 ysize yres(60) background Frame("orange_button", borders=gui.button_borders):
                            text "$59.99" font "1.ttf" align 0.5, 0.5 size res_font(32) bold True at repeat_bounce

                button xsize xres(200) yfill True action NullAction():
                    vbox xfill True yfill True:
                        vbox yalign 0.5 xfill True:
                            fixed align 0.5, 0.5 ysize 0.45:
                                add "misc" xalign 0.15
                                add "misc" xalign 0.5 ypos 0.1
                                add "misc" xalign 0.85 ypos 0.2
                                text __("Best\nvalue!!!") align 0.5, 0.5 outlines [(1, "#000", 0, 0)] size res_font(24) at jitter
                            null height yres(10)
                            text __("x5,000 P2W Crystals") xalign 0.5 yalign 0.5 bold True font "1.ttf"
                        frame xfill True yalign 0.9 ysize yres(60) background Frame("orange_button", borders=gui.button_borders):
                            text "$149.99" font "1.ttf" align 0.5, 0.5 size res_font(32) bold True at repeat_bounce


    timer 0.001 repeat True:
        if x.value >= x.range:
            action Function(x.change, 0)
        else:
            action Function(x.change, x.value+3)


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
    textbutton "闲聊" xsize xres(75) xalign 0.09 yalign 0.25 action Jump("harem_" + MC.current_trainer.name.lower()) hovered tt.Action("Talk to " + MC.current_trainer.name + ".")

#### END OF BK SCREENS FILE ####
