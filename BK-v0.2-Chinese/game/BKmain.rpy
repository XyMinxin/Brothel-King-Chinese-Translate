####            MAIN GAME LOOPS                ####
##      Running the different screens            ##
##                                               ##
####                                           ####

## As this is one of the first code I ever wrote, this script is especially terrible. You've been warned.


## SLAVE MARKET ##

label slavemarket:

    call hide_everything() from _call_hide_everything_19

    play sound "chimes.wav"

    if nsfw:
        scene black
        show bg slave market
        with Fade(0.15, 0.3, 0.15)

    if slavemarket_firstvisit:
        slavegirl1 "Greetings Master."

    slavegirl1 "Welcome to the slave pen!{w=1.0}{nw}"

    if slavemarket.updated:

#        $ renpy.start_predict_screen("girls")

        slavegirl1 "Fresh girls are available today, Master."

        $ slavemarket.updated = False

############ Jman - Headhunter Mod ############
    if game.has_active_mod("Headhunter Mod"):
        if (slavemarket_firstvisit or slavemarket_firstvisit2):
            show headhunter at centerhigh with dissolve
            play sound s_woman_scream
            headhunter "Ahoy, cap'n! We're off'ring a one-time discunt... *ahem* {i}discount{/i} to new customers!"
            play sound s_scream
            show headhunter strip1 at centerhigh with dissolve
            headhunter strip1 "Get [game.headhunter_discount] denars off yer first contract!"
            play sound s_aaha
            show headhunter strip1 at centerhigh with dissolve
            headhunter strip1 "Them cheapo slaves here won't work and always give ya lip!"
            play sound s_scream
            show headhunter strip1 at centerhigh with dissolve
            headhunter strip1 "A real shame, I tell ya! That ain't a problem with {i}our{/i} booty, mate!"
            play sound s_aaha
            show headhunter strip2 at centerhigh with dissolve
            headhunter strip2 "So don't ferget to cum... *cough*{i}come{/i} and visit me, arrh!"
            play sound s_evil_laugh
            hide headhunter strip2 with fade
            $ slavemarket_firstvisit2 = False
############ Jman - Headhunter Mod End ########

    $ tt = show_tt("top_right")

    $ girl_status_dict = load_girl_status(slavemarket.girls)
    $ focus_vp(slavemarket.girls)

    $ renpy.block_rollback()

############ Jman - Headhunter Mod ############
    if game.has_active_mod("Headhunter Mod"):
        if not slavemarket_firstvisit and slavemarket_firstvisit3:
            $ slavemarket_firstvisit3 = False
            if renpy.call_screen("yes_no", "去看看这些关于合同的计划是怎么回事？"):
                jump headhunter_main
############ Jman - Headhunter Mod End ########

    show screen girls(slavemarket.girls, context = "slavemarket")


label slavemarket_loop:

    while True:

############ Jman - Headhunter Mod ############
        if game.has_active_mod("Headhunter Mod"):
            if slavemarket_firstvisit:
                $ game.headhunter_button_enabled = 0
                python:
                    min_slave_price = 999999
                    for g in slavemarket.girls:
                        girl_price = g.get_price('buy')
                        if girl_price < min_slave_price:
                            min_slave_price = girl_price
                if min_slave_price > MC.gold:
                    you "How am I supposed to afford one of these slaves, Gio? You damn horse thief, did you even check the prices before peddling my belongings, huh?"
                    gio "Well, hehehe... I'm sure you'll figure something out. Now..."
                    call hide_everything() from _call_hide_everything_48
                    $ game.headhunter_button_enabled = 1
                    $ slavemarket_firstvisit = False
                    $ slavemarket_firstvisit2 = False
                    jump districts_first_time
                elif slavemarket_firstvisit3:
                    gio "Hmm, that hunter lass might be onto something. The cheap low-rank slaves they sell to newcomers like you aren't particularly obedient."
                    gio "And it's hard to make a proper slut out of one of these tarts. So your brothel might be lacking whores..."
                    gio "... unless you go take up that pirate gal's offer. That little tease flashed us!"
                    if renpy.call_screen("yes_no", "跳过购买奴隶，以后再来试试猎头的折扣？"):
                        call hide_everything() from _call_hide_everything_49
                        $ game.headhunter_button_enabled = 1
                        $ slavemarket_firstvisit = False
                        $ slavemarket_firstvisit2 = False
                        jump districts_first_time
############ Jman - Headhunter Mod End ########

        # Sorts slavemarket girls if sorting preferences exist
        $ game.sort(slavemarket.girls, context = "slavemarket")

        $ girl = None
        $ girl = ui.interact()


############ Jman - Headhunter Mod ############
        if game.has_active_mod("Headhunter Mod"):
            if girl and not game.interacting_with_headhunter:
                $ game.headhunter_button_enabled = 0

############ Jman - Headhunter Mod End ########


        if isinstance(girl, Girl):

            $ price = girl.get_price('buy')

            if len(MC.girls) < brothel.bedrooms:

                if MC.has_gold(price):

                    $ result = renpy.call_screen("yes_no", "你真的想用 [price] 金币购买[girl.fullname]吗？")

                else:
                    you "Shoot, I don't have enough gold..."
                    $ result = False

            else:
                sill sad "Sorry Master, I'm afraid you don't have room in your brothel for another girl."
                $ result = False

                if brothel.bedrooms < brothel.get_maxbedrooms() or (farm.active and farm.has_room()) or (farm.active and farm.pens < farm.get_pen_limit()):

                    $ price1 = brothel.get_room_price()
                    $ price2 = farm.get_pen_cost()

                    menu:
                        sill "Sorry Master, I'm afraid you don't have room in your brothel for another girl."

                        "Add a new room to your brothel ([price1] gold)" if brothel.bedrooms < brothel.get_maxbedrooms():
                            if brothel.add_room():
                                $ result = True

                        "Send her to the farm" if farm.active and farm.has_room():
                            $ result = "farm"

                        "Add a new pen to your farm ([price2] gold)" if farm.active and farm.pens < farm.get_pen_limit() and not farm.has_room():
                            $ res, text1 = farm.add_pen()

                            if res:
                                $ result = "farm"

                            if text1:
                                gizel normal "[text1]"

                        "Cancel":
                            $ result = False

            if result:

                if MC.has_gold(price):
                    $ MC.buy(slavemarket, girl, price)
                    $ girl.original_price = price
                    if result == "farm":
                        $ MC.girls.remove(girl)
                        $ farm.girls.append(girl)
                        $ farm.programs[girl] = FarmProgram(girl)

                    hide screen girl_profile
                    hide screen girl_stats
                    hide screen button_overlay

                    slavegirl1 "You just bought [girl.fullname]. I hope you will enjoy her."
                    call dialogue(girl, "bought") from _call_dialogue_90

                    if result == "farm":
                        call send_to_farm(girl, can_beg=False, can_cancel=False) from _call_send_to_farm_4

                    if slavemarket_firstvisit:
                        call hide_everything() from _call_hide_everything_45
                        jump slavemarket_first_time

############ Jman - Headhunter Mod ############
                        if game.has_active_mod("Headhunter Mod"):
                            $ game.headhunter_button_enabled = 1
############ Jman - Headhunter Mod End ########

                else:
                    slavegirl1 "Sorry Master, but you don't have enough gold to buy [girl.fullname]."

                $ selected_girl=None
                $ renpy.block_rollback()

############ Jman - Headhunter Mod ############
            if game.has_active_mod("Headhunter Mod"):
                $ game.headhunter_button_enabled = 1
############ Jman - Headhunter Mod End ########

## DISTRICT ##

label districts:

    call hide_everything() from _call_hide_everything_20

#    $ renpy.start_predict_screen("visit_district")

    $ tt = show_tt("top_right")

    scene black
    show screen districts()
    with Dissolve(0.3)

    while True:

        $ selected_district = ui.interact()

        if selected_district:
            jump visit_district


label visit_district:

    hide screen districts

#    $ renpy.start_predict_screen("visit_location")

    $ tt = show_tt("top_right")

    scene black
    show expression selected_district.get_pic(config.screen_width, res_event_height) at top
    show screen visit_district()
    with Dissolve(0.3)

    if not selected_district.pic in persistent.seen_list:
        $ persistent.seen_list.append(selected_district.pic)


    while True:

#        $ selected_location = None

        $ selected_location, r = ui.interact()

        if r == "go":

            if selected_location.secret:

                "You have not discovered this location yet."

            else:

                jump visit_location

        elif r == "special": # Special label
            hide screen visit_district
            $ renpy.call(selected_location.menu[1])
            jump visit_district


label visit_location():

    stop sound fadeout 2.0

    hide screen visit_district

    $ _previous = get_previous(location_dict[selected_district.name], selected_location, loop=True)
    if _previous.secret:
        $ _previous = get_previous(location_dict[selected_district.name], _previous, loop=True)
    $ _next = get_next(location_dict[selected_district.name], selected_location, loop=True)
    if _next.secret:
        $ _next = get_next(location_dict[selected_district.name], _next, loop=True)

#    $ renpy.start_predict_screen("visit_location", _previous)
#    $ renpy.start_predict_screen("visit_location", _next)

    scene black
    show expression selected_location.get_pic(config.screen_width, res_event_height) at top
    show screen visit_location()
    with Dissolve(0.3)

    $ tt = show_tt("top_right")

    if not selected_location.pic in persistent.seen_list:
        $ persistent.seen_list.append(selected_location.pic)

    while True:
        $ renpy.block_rollback()

        $ result = None

        $ result = ui.interact()

        if isinstance(result, Girl):

            $ selected_girl = result

            call free_girl_interact(result) from _call_free_girl_interact

        elif result == "visit":

            hide screen visit_location

            python:
                escaped_girl = None
                for girl in MC.escaped_girls:
                    if girl.location == selected_location.name:
                        escaped_girl = girl

            if escaped_girl: # Escaped girl events always have priority
                call found_escaped_girl(escaped_girl) from _call_found_escaped_girl

            else: # Story events have priority over mundane events

                python:
                    for ev in city_events: # Story events
                        if ev.happens():
                            renpy.hide_screen("visit_location")
                            renpy.hide_screen("overlay")
                            MC.interactions -= ev.AP_cost
                            renpy.call("display_events", [ev])
                            break

                    else:
                        if game.kidnapped and selected_location == taverns: # Get kidnap tip
                            renpy.call("kidnap_tip", rand_choice(game.kidnapped))

                        else: # Random city event
                            ev_type = weighted_choice(encounters)

                            if not isinstance(ev_type, basestring):

                                ev_type = rand_choice(ev_type)

                            MC.interactions -= 1

                            renpy.call("city_" + ev_type)

                if district.rank >= 2 and renpy.random.random() <= 0.12: # 8% chance of getting a resource, 4% Cimerian
                    $ renpy.say("", "在探索城市时，你发现了一些有用的东西。")
                    $ d = dice(6)

                    if dice(6) >= 5:
                        if game.chapter >= 3 and dice(6) >= 6:
                            call receive_item(search_items("Cimerian文物")[0], msg="你收到了一个罕见的 %s 。", use_article=False) from _call_receive_item
                        else:
                            call receive_item(search_items("Cimerian废料")[0], msg="你收到一个 %s 。", use_article=False) from _call_receive_item_1

                    else:
                        $ MC.gain_resource(number=dice(3), random=True)


            jump visit_location

        elif result == "special":
            hide screen visit_location
            $ renpy.call(selected_location.menu[1])

            jump visit_location

        elif result == "hunt":
            call ninja_hunt(selected_location) from _call_ninja_hunt

            jump visit_location



## BROTHEL ##

label brothel():

    hide screen home
    hide screen tool

#    $ renpy.start_predict_screen("furniture")

    scene black
    show expression bg_bro at top:
    $ tt = show_tt("top_right")

    show screen brothel()
    with Dissolve(0.3)

    $ brothel.update_customer_count()

label brothel_loop():

    while True:
        $ test_achievement("upgrades")

        $ mychoice = (None, None)

        $ mychoice = ui.interact()

        python:
            try:
                operation, obj = mychoice
            except (ValueError, TypeError):
                operation = mychoice

        if operation == "add_room":
            if obj.level == 0:
                $ obj.buy()
            else:
                $ obj.upgrade()

        elif operation == "clean up":

            $ result = brothel.clean_up()

            if result:
                sill happy "Yes Master, I will get some supplies and work on it right away!"
                "..."
                sill sad "*pant* *pant* It is done, Master... I'm so tired... *pant*"

        elif operation == "change name":

            $ brothel.name = renpy.input("更改名字：", default = brothel.name, length = 40)

        elif operation == "furniture":

            hide screen brothel

            if blueprint_item in MC.items:
                call add_vitals_scanner() from _call_add_vitals_scanner

            jump wagon

        elif operation == "open options":
            hide screen brothel
            show screen brothel_options
            with dissolve

        elif operation == "close options":

            python:
                for pop in all_populations:
                    if pop.weight > 0:
                        break
                else:
                    if not renpy.call_screen("yes_no", "警告！所有客户的人口都被设置为零。如果发生这种情况，今晚只有{b}乞丐{/b}会来。你确定你要继续吗？"):
                        renpy.jump("brothel_loop")

            hide screen brothel_options
            show screen brothel
            with dissolve

#        elif operation == "upgrade master bedroom":

label furniture():

    hide screen home
    hide screen tool

    scene black
    show bg wagon at top

    $ tt = show_tt("top_right")

    show screen furniture()
    with Dissolve(0.3)

    while True:
        $ result = ui.interact()

        if result == "quit":
            hide screen furniture
            jump brothel

        elif isinstance(result, Furniture):
            $ brothel.buy_furniture(result)
            $ renpy.block_rollback()

## FARM SCREEN ##

label farm():

    scene black

    show bg farm tall at top with Dissolve(0.3)

    if farm_firstvisit:
        call farm_first_visit() from _call_farm_first_visit
        $ farm_firstvisit = False

    $ show_hurt = True

    $ selected_girl = None

    $ girl_status_dict = load_girl_status(MC.girls + farm.girls) # Including brothel girls to avoid a bug 6TisWO6R ran into

label farm_loop():

    if farm.get_hurt_minions() and show_hurt:

        $ hurt = farm.get_hurt_minions()

        gizel upset "[MC.name]! One of your good-for-nothing sluts has hurt my babies! If you don't act quickly, I'm going to have to retire it."

        python:
            menu_list = [(str(len(hurt)) + " 个奴仆都受伤了。你打算怎么办？", None)]

            if MC.get_items(target="minion", name="愈合粉"):
                for mn in hurt:
                    menu_list.append(("对[mn.name] (等级 " + str(mn.level) + " 的 " + farm_related_dict[mn.type] + ") 使用愈合粉", ("heal", mn)))

            for mn in hurt:
                menu_list.append(("除名 [mn.name] (等级 " + str(mn.level) + " 的 " + farm_related_dict[mn.type] + ")", ("retire", mn)))

            menu_list.append(("暂时不考虑这个问题", ("ignore", None)))

        $ res, mn = menu(menu_list)
        $ xxx3 = farm_related_dict[mn.type]
        if res == "heal":
            gizel normal "Fine, let's use this to get the poor bastard back on its feet. Or tentacles. Whatever."

            $ MC.use_item(MC.get_items(target="minion", name="愈合粉")[0])
            $ mn.heal()

            play sound s_spell

            "[mn.name] (level [mn.level] [mn.type]) has been healed."

        elif res == "retire":
            gizel "It seems we have no choice, then... I'm gonna send it to a farm up-country... to retire."

            $ farm.remove_minion(mn)

            if dice(6) >= 6:

                you "You mean... You're gonna put it out of its misery, right? You're gonna kill it, aren't you?"

                play sound s_surprise

                gizel surprise "Whaaat??? My baby? No!!! I'm really sending it to a farm up-country, so they can rest in leisure! I wouldn't kill one of my sweet minions!!! Are you mad?"

                you "Oh... Ok."

            "[mn.name] (level [mn.level] [mn.type]) has been retired."

        elif res == "ignore":
            $ show_hurt = False

        jump farm_loop


    show screen farm_tab()
    $ tt = show_tt("top_right")
    with Dissolve(0.15)

    while True:

        $ game.sort(farm.girls, context = "farm")

        $ result = ui.interact()
        $ girl_status_dict = load_girl_status(MC.girls + farm.girls)

        python:
            try:
                res, obj = result
            except (ValueError, TypeError):
                res = None

        if res == "help":
            show screen dark_filter
            call help_farm_question from _call_help_farm_question
            hide screen dark_filter

        elif res == "change_name":
            $ girl = obj
            $ girl.name = renpy.input("你想改变她的名字吗？", default = girl.name)
            $ girl.char.name = girl.name
            $ girl.lastname = renpy.input("你想改变她的姓氏吗？", default = girl.lastname)

            menu:
                "Do you want to invert her first and last name?"

                "Yes":
                    $ girl.init_dict["identity/inverted_name"] = True
                "No":
                    $ girl.init_dict["identity/inverted_name"] = False

            $ girl.set_fullname()

            $ renpy.block_rollback()

        elif res == "rules": # This calls up the rules label
            call farm_set_default() from _call_farm_set_default

        elif res == "pen":

            $ result, text1 = farm.add_pen()

            if result:
                gizel happy "[text1]"
            elif text1:
                gizel upset "[text1]"

        elif res == "items": # This calls up the item menu (if available)

            if can_use_minion_item():

                show screen dark_filter

                python:
                    menu_list = [("你希望使用哪项物品？", None)]

                    # Healing powder

                    if MC.get_items(target="minion", name="愈合粉") and farm.get_hurt_minions():
                        for mn in farm.get_hurt_minions():
                            menu_list.append(["对[mn.name] (等级 " + str(mn.level) + " 的 " + farm_related_dict[mn.type] + ") 使用愈合粉", ("heal", mn, MC.get_items(target="minion", name="愈合粉")[0])])

                    # XP items

                    if MC.get_items(target="minion", effect_type="gain", effect_target="stallion xp") and farm.get_minions("stallion"):
                        minions = farm.get_minions("stallion")
                        for it in MC.get_items(target="minion", effect_type="gain", effect_target="stallion xp"):
                            xp_bonus = it.get_effect("gain", "stallion xp") // len(minions)
                            menu_list.append(["使用 " + it.name.lower() + " (+" + str(xp_bonus) + " 种马经验", ("gain xp", minions, it, xp_bonus)])

                    if MC.get_items(target="minion", effect_type="gain", effect_target="beast xp") and farm.get_minions("beast"):
                        minions = farm.get_minions("beast")
                        for it in MC.get_items(target="minion", effect_type="gain", effect_target="beast xp"):
                            xp_bonus = it.get_effect("gain", "beast xp") // len(minions)
                            menu_list.append(["使用 " + it.name.lower() + " (+" + str(xp_bonus) + " 野兽经验", ("gain xp", minions, it, xp_bonus)])

                    if MC.get_items(target="minion", effect_type="gain", effect_target="monster xp") and farm.get_minions("monster"):
                        minions = farm.get_minions("monster")
                        for it in MC.get_items(target="minion", effect_type="gain", effect_target="monster xp"):
                            xp_bonus = it.get_effect("gain", "monster xp") // len(minions)
                            menu_list.append(["使用 " + it.name.lower() + " (+" + str(xp_bonus) + " 怪物经验", ("gain xp", minions, it, xp_bonus)])

                    if MC.get_items(target="minion", effect_type="gain", effect_target="machine xp") and farm.get_minions("machine"):
                        minions = farm.get_minions("machine")
                        for it in MC.get_items(target="minion", effect_type="gain", effect_target="machine xp"):
                            xp_bonus = it.get_effect("gain", "machine xp") // len(minions)
                            menu_list.append(["使用 " + it.name.lower() + " (+" + str(xp_bonus) + " 机器经验", ("gain xp", minions, it, xp_bonus)])

                    menu_list.append(["算了", ("back")])

                $ res = menu(menu_list)

                if res == "back":
                    pass

                elif res[0] == "heal":

                    $ r, mn, it = res
                    $ xxx3 = farm_related_dict[mn.type]
                    $ MC.use_item(it)
                    $ mn.heal()

                    play sound s_spell

                    "[mn.name] (level [mn.level] [mn.type]) has been healed."

                elif res[0] == "gain xp":

                    $ r, minions, it, xp_bonus = res

                    play sound s_spell

                    $ renpy.say("", "你的 " + farm_related_dict[minions[0].type] + " 获得经验。")

                    $ MC.use_item(it)

                    python:
                        levelup = []

                        for mn in minions:
                            mn.xp += xp_bonus
                            if mn.level_up():
                                levelup.append(mn)

                    while levelup:
                        $ mn = levelup.pop()
                        $ renpy.say(gizel, mn.name + " 现在是等级 " + str(mn.level) + " 的 " + farm_related_dict[mn.type] + "。")

                hide screen dark_filter

            else:
                gizel normal "There are no items you can use on minions at the moment."

        elif res == "upgrade": # Where 'obj' is the targeted installation
            $ upgraded, text1 = farm.upgrade(obj)

            if upgraded:
                gizel happy "[text1]"
            elif text1:
                gizel upset "[text1]"

        elif res == "change program": # Where 'obj' is the targeted girl
            call farm_change_program(obj) from _call_farm_change_program
            $ girl_status_dict = load_girl_status(MC.girls + farm.girls)

#            show screen girl_profile(selected_girl, context="farm")
#            show screen girl_stats(selected_girl, context="farm")
#            show screen button_overlay(selected_girl, context="farm")

        elif res == "change mode": # Where 'obj' is the targeted girl
            call farm_change_training_mode(obj) from _call_farm_change_training_mode

        elif res == "take out": # Where 'obj' is the targeted girl
            call farm_take_out(obj) from _call_farm_take_out

        elif res == "equip": # Where 'obj' is the targeted girl
            $ girl = obj

            hide screen girl_stats
            hide screen girl_profile
            hide screen button_overlay
            hide screen farm_tab

            with Dissolve(0.15)

            show screen item_tab(MC, girl, "farm")

            while True:

                $ game.sort(MC.items, context = "MC items")
                $ game.sort(girl.items, context = "farm items")

                $ act = None

                python:
                    try:
                        it, act = ui.interact()
                    except:
                        act = None

                if act == "give":
                    if MC.give(selected_girl, it):
                        hide screen item_profile

                elif act == "take":
                    if it.equipped:
                        $ selected_girl.unequip(it)

                    $ MC.take(selected_girl, it)

                    hide screen item_profile

                elif act == "equip":
                    $ MC.equip(it)
                    play sound it.sound

                elif act == "unequip":
                    $ MC.unequip(it)
                    play sound it.sound

                elif act == "gift":
                    hide screen item_profile
                    $ MC.gift(selected_girl, it)
                    play sound it.sound

                elif act == "give_equip":
                    if it.equipped:
                        $ MC.unequip(it)
                        play sound it.sound

                    if MC.give(selected_girl, it):
                        $ selected_girl.equip(it)
                        hide screen item_profile

                elif act == "give_use":
                    if it.type.giveable:
                        if it.equipped:
                            $ MC.unequip(it)
                            play sound it.sound

                        $ r, c = selected_girl.use_item(it)
                        play sound it.sound

                        if r == "used_up":
                            $ MC.items.remove(it)
                            hide screen item_profile

                elif act == "g_equip":
                    $ selected_girl.equip(it)
                    play sound it.sound

                elif act == "g_unequip":
                    $ selected_girl.unequip(it)
                    play sound it.sound

                elif act == "g_use":
                    $ r, c = selected_girl.use_item(it)
                    play sound it.sound

                    if r == "used_up":
                        hide screen item_profile

                elif act == "back":
                    call hide_everything() from _call_hide_everything_21
                    jump farm

                elif not act:
                    # $ ui.close() #!
                    hide screen item_tab
                    jump farm_loop

        elif res == "sell": # Where 'obj' is the targeted girl
            $ girl = obj

            if not MC.can_sell(slavemarket, girl):
                gizel upset "You can't sell that girl again! The slavemarket won't allow it!"
                if renpy.call_screen("yes_no", "奴隶市场不会花钱购买她。你真的想不收取一分钱就出售[girl.fullname]吗？"):
                    $ farm.girls.remove(girl)

            else:
                $ price = girl.get_price("sell")

                $ result = renpy.call_screen("yes_no", "你真的想以 [price] 金币出售[girl.fullname]吗？")

                if result == True:
                    python:
                        relinquish_girl(girl)

                        MC.sell(slavemarket, girl, price)
                        game.track("sell girl gold", price)
                        test_achievement("sell girl gold")

                    if girl.get_love() >= 90:
                        $ unlock_achievement("sell girl love")
                        call dialogue(girl, "sold love") from _call_dialogue_15
                    else:
                        call dialogue(girl, "sold") from _call_dialogue_16

                    hide screen girl_profile
                    hide screen girl_stats
                    hide screen button_overlay

        elif res == "dismiss":

            $ girl = obj

            if renpy.call_screen("yes_no", "你真的不想要[girl.fullname]了吗？她将恢复自由，永远离开这个城市。"):

                python:
                    if girl.items: # Unequip all items before dismiss
                        for it in list(girl.items): # shallow copy of list since deleting from girl.items
                            if it.equipped:
                                girl.unequip(it)
                            MC.take(girl, it)
                            renpy.notify("\n" + girl.name + " 失去了 " + it.name)
                            renpy.pause(0.5)

                    farm.girls.remove(girl)

                call dialogue(girl, "freed") from _call_dialogue_17

                $ unlock_achievement("release free girl")

                hide screen girl_profile
                hide screen girl_stats
                hide screen button_overlay

        elif res == "badge":
            call screen girl_pick_badge(obj)

        $ renpy.block_rollback()

    jump farm_loop

## MAIN SCREEN ##


label main():

    # <Chris12 PredictImages - Predict just the portraits.
    # Profiles are not needed immediately on entering the girls screen. />
    $ predict_images(MC.girls + slavemarket.girls, predict_profiles = False)

#    $ renpy.start_predict_screen("girls", MC.girls, "girls")

    scene black with Dissolve(0.15)

    # Update mods (runs once per game session or after a mod has been activated/deactivated)

    $ update_list = []

    if not updated_games[game]:
        $ update_list = game.update_mods()

    # Custom 'update_label' will be called for mods that have it

    while update_list:
        $ lbl = update_list.pop(0)
        call expression lbl from _call_expression_5

    if not renpy.music.is_playing(channel='music'):

        $ newmusic = rand_choice(playlist)

        play music ["Silence.ogg", newmusic] fadein 3.0 fadeout 10.0 noloop

    if refresh_memory_on_home_screen:
        $ renpy.free_memory() # Included here after Jman's request

    if brothel.get_common_rooms():
        $ room = brothel.get_random_room_pic_path()
    else:
        $ room = "black"

    show expression room at top
    with Dissolve(0.3)

    $ calendar.play_alarms() # Also triggers "day" conditional events
    $ test_achievements(["gold"])
    $ brothel.update_customer_count()

    show expression room at top

    $ renpy.block_rollback()

    show screen home()

    $ tt = show_tt("top_right")
    with Dissolve(0.3)

############ Jman - Headhunter Mod ############
    if game.has_active_mod("Headhunter Mod"):
        if game.headhunter_girl:
            $ game.headhunter_button_enabled = 0
            if game.headhunter_time <= 0:
                $ game.interacting_with_headhunter = True
                "The headhunter is back with your prize!"
                hide screen brothel_report
                jump headhunter_delivers
                $ game.interacting_with_headhunter = False
############ Jman - Headhunter Mod End ########

    jump main_wait_for_input


label main_wait_for_input:

    while True:

        $ game.update_files_timestamp() #<Chris12 AutoRepair />

        $ result = None

        $ result = ui.interact()

        if result:
            if result == "advance":
                if renpy.call_screen("yes_no", "你真的想推进到下一章吗？\n\n{size=-2}这将重置你所有的房间改造，但你将保留你的家具和装饰品。\n这将花费 {b}" + str(blist[game.chapter+1].cost) + " 金币{/b}。"):
                    call advance_to_chapter(game.chapter+1) from _call_advance_to_chapter_1
                    jump brothel

            elif result != True:
                $ selected_destination = result

                jump teleport

    #        scene black with Fade(0.15, 0.3, 0.15)




## GIRLS ##


label girls_first_time:

#    $ renpy.start_predict_screen("girls", MC.girls, "girls")

    call hide_everything() from _call_hide_everything_39

    scene black
    show expression brothel.bedroom_type.pic_path at top:

#    $ renpy.show(brothel.bedroom_type.name, at_list = [top])

#     $ renpy.show_screen("show_img", brothel.get_bedroom_pic(config.screen_width, config.screen_height), _layer = "master")

    with dissolve

    show screen girls(MC.girls, "girls")
    $ tt = show_tt("top_right")

    $ renpy.block_rollback()

############ Jman - Headhunter Mod ############
    if game.has_active_mod("Headhunter Mod"):
        if len(MC.girls) <= 0:
            play sound s_hmm
            sill sad "We didn't buy any slaves, Master. Are you planning to have me do all the work?!"
            play sound s_erm
            sill sad "*shuffles away* I'll just leave you to it, Master. Please ask me later if you have any questions."
            "Press the '?' button in the top right corner to obtain information on the game or your current screen."
            $ girls_firstvisit = False

            jump girls
############ Jman - Headhunter Mod End ########

    sill happy "Let's meet your girl, and assign her to her new job."

    $ result = ""


    while True:

        $ result = None

        $ result = ui.interact()

        if result == "assign":

            $ girl = selected_girl

            menu:

                girl.char "What do you want me to do, Master?"

                "Rest":
                    $ girl.set_job(None)
                    $ renpy.block_rollback()

                "Work as a waitress" if brothel.has_room("tavern"):
                    $ girl.set_job("waitress")
                    $ renpy.block_rollback()

                "Work as a dancer" if brothel.has_room("club"):
                    $ girl.set_job("dancer")
                    $ renpy.block_rollback()

                "Work as a masseuse" if brothel.has_room("onsen"):
                    $ girl.set_job("masseuse")
                    $ renpy.block_rollback()

                "Work as a geisha" if brothel.has_room("okiya"):
                    $ girl.set_job("geisha")
                    $ renpy.block_rollback()

                "Work as a whore":
                    $ renpy.block_rollback()

                    if girl.will_do("whore"):
                        $ girl.set_job("whore")

                    else:
                        call dialogue(girl, "refuse whoring") from _call_dialogue_91

                        sill sad "You cannot make her a whore in her current state, you know. She'll run
                                  away or harm a customer."

                        if help_tips["whore"]:
                            sill happy "Would you like to learn more about training your girls to become whores?"

                            menu:
                                "Yes":
                                    call help_whores() from _call_help_whores
                                "No":
                                    pass
                                "Don't ask me again":
                                    $ help_tips["whore"] = False
                                    "You can access the help menu at any time by clicking the '?' button in the upper-right corner."

            if girl.job:

                call dialogue(girl, "accept job") from _call_dialogue_92
                sill "Very good! Your girl is now ready to work."
                sill "I think I'll leave you to it from now on, Master. Please ask if you have any question."
                "Press the '?' button in the top right corner to obtain information on the game or your current screen."
                $ girls_firstvisit = False

                jump girls

            else:

                call dialogue(girl, "rest") from _call_dialogue_93

#        pass

#       return



label girls():

    #<Chris12 PredictImages>
    $ predict_images(MC.girls, predict_portraits = False) # Portraits will be loaded directly, anyway. Also, they already get predicted in label main.
    #</Chris12 PredictImages>

#    $ renpy.start_predict_screen("girls", MC.girls, "girls")

    call hide_everything() from _call_hide_everything_22

    scene black
    show expression brothel.bedroom_type.pic_path at top

    if selected_girl not in MC.girls:
        $ selected_girl = None

    $ girl_status_dict = load_girl_status(MC.girls + farm.girls) # Including farm girls to avoid a bug 6TisWO6R ran into
    $ focus_vp(MC.girls)

    show screen girls(MC.girls, "girls")
    $ tt = show_tt("top_right")

    with Dissolve(0.3)

#    $ renpy.start_predict_screen("perks")

    $ renpy.block_rollback()

    $ result = ""


label girls_loop():

    while True:

        $ game.sort(MC.girls, context = "girls")

        $ girl_status_dict = load_girl_status(MC.girls) # Test to increase performance

        $ result = None

        $ result = ui.interact()

        if not result:
            pass

        elif result == "change_name":

            $ girl = selected_girl

            $ girl.name = renpy.input("你想改变她的名字吗？", default = girl.name)
            $ girl.char.name = girl.name
            $ girl.lastname = renpy.input("你想改变她的姓氏吗？", default = girl.lastname)

            menu:
                "Do you want to invert her first and last name?"

                "Yes":
                    $ girl.init_dict["identity/inverted_name"] = True
                "No":
                    $ girl.init_dict["identity/inverted_name"] = False

            $ girl.set_fullname()

            $ renpy.block_rollback()

        elif result == "assign":
            if not renpy.predicting():
                call hide_details()

            $ girl = selected_girl

            if girl.away or girl.hurt > 0 or girl.exhausted:
                if girl.away:
                    $ renpy.notify("\n%s正在外出，暂时不能分配新的工作。" % girl.name)
                elif girl.hurt > 0:
                    $ renpy.notify("\n%s受伤了，暂时不能被分配新的工作。" % girl.name)
                elif girl.exhausted:
                    $ renpy.notify("\n%s筋疲力尽，暂时不能分配新的工作。" % girl.name)
                jump girls_loop

            $ exit = False

            show screen assign_job(girl) with Dissolve(0.15)

            while True:
                $ renpy.block_rollback()

                $ r = ui.interact()

                if r == "cancel":
                    $ exit = "silent"

                elif r == "rest":
                    $ girl.set_job(None)
                    $ exit = "silent"

                elif r in all_jobs:
                    if brothel.has_room(job_room_dict[r]):
                        $ girl.set_job(r)
                        $ exit = True

                elif r == "whore":
                    $ r = girl.set_job("whore")

                    if r:
                        $ exit = True
                    else:
                        hide screen assign_job
                        with Dissolve(0.15)
                        call dialogue(girl, "refuse whoring") from _call_dialogue_94

                        sill sad "You cannot make her a whore in her current state, you know. She'll run
                                  away or harm a customer."

                        if help_tips["whore"]:

                            sill happy "Would you like to learn more about training your girls to become whores?"

                            menu:
                                "Yes":
                                    call help_whores() from _call_help_whores_5
                                "No":
                                    pass
                                "Don't tell me again":
                                    $ help_tips["whore"] = False
                                    "You can access the help menu at any time by clicking the '?' button in the upper-right corner."

                        show screen assign_job(girl) with Dissolve(0.15)

                elif r == "ww":
                    if not girl.work_whore and not girl.will_do("whore"):
                        sill "You cannot activate this option if she refuses to be a whore.{w=1.0}{nw}"
                    else:
                        $ girl.work_whore = not girl.work_whore

                elif r == "farm":
                    hide screen assign_job
                    with Dissolve(0.15)
                    call send_to_farm(girl) from _call_send_to_farm_3
                    hide screen dark_filter
                    # hide screen assign_job
                    # with Dissolve(0.15)
                    $ exit = "silent"

                elif r == "master bedroom":
                    hide screen assign_job
                    with Dissolve(0.15)
                    if girl in brothel.master_bedroom.girls:
                        call slave_master_bedroom_remove(girl) from _call_slave_master_bedroom_remove
                        # you "Go back to your bedroom now. I am done with you.{w=1.0}{nw}"
                        # $ brothel.master_bedroom.remove_girl(girl)
                        # $ renpy.notify("\n" + girl.fullname + " has left the master bedroom.")
                    elif girl.away:
                        "You cannot send her to the master bedroom because she is away on a [girl.assignment.type]."
                    elif brothel.master_bedroom.can_have_girl():
                        call slave_master_bedroom_add(girl) from _call_slave_master_bedroom_add
                        # you "Go to my room. You shall sleep there from now on.{w=1.0}{nw}"
                        # $ brothel.master_bedroom.add_girl(girl)
                        # $ renpy.notify("\n" + girl.fullname + " has joined the master bedroom.")
                    else:
                        "You cannot send her to your room, as it is full.{w=1.0}{nw}"
                    $ exit = "silent"

                if exit:
                    jump assign_job_exit

            label assign_job_exit():
                hide screen assign_job
                with Dissolve(0.15)

                if exit != "silent":
                    if girl.job in all_jobs and girl.get_effect("special", "workwhore"):
                        menu:
                            "Ask [girl.name] to work and whore at the same time?"

                            "Yes":
                                if not girl.will_do("whore"):
                                    call dialogue(girl, "refuse whoring") from _call_dialogue_95

                                    sill sad "You cannot make her a whore in her current state, you know. She'll run
                                              away or harm a customer."

                                    if help_tips["whore"]:

                                        sill happy "Would you like to learn more about training your girls to become whores?"

                                        menu:
                                            "Yes":
                                                call help_whores() from _call_help_whores_7
                                            "No":
                                                pass
                                            "Don't tell me again":
                                                $ help_tips["whore"] = False
                                                "You can access the help menu at any time by clicking the '?' button in the upper-right corner."

                                else:
                                    $ girl.work_whore = True

                            "No":
                                $ girl.work_whore = False

                    $ xxx3 = girl_related_dict[girl.job]
                    if girl.hurt > 0 and girl.job:
                        sill sad "Master, [girl.name] is still too weak and needs more rest. She will resume work as a {b}[girl.job]{/b} when she recovers."

                    elif girl.exhausted and girl.job:
                        call dialogue(girl, "exhausted") from _call_dialogue_96

                    elif girl.away and girl.job:
                        if girl.assignment:
                            sill happy "[girl.name] is away on a [girl.assignment.type]. She will resume work as a {b}[girl.job]{/b} after she comes back."
                        else:
                            sill happy "[girl.name] is away. She will resume work as a {b}[girl.job]{/b} after she comes back."

                    elif girl.job:
                        if girl.work_whore:
                            call dialogue(girl, "work_whore") from _call_dialogue_97
                        else:
                            call dialogue(girl, "accept job") from _call_dialogue_98

        elif result == "interact":

            if not renpy.predicting():
                call hide_details()

            $ girl = selected_girl

            call slave_interact(girl) from _call_slave_interact

        elif result == "sched":

            if not renpy.predicting():
                call hide_details()

            if MC.girls.index(selected_girl) > 9:
                $ sched_adj.change(MC.girls.index(selected_girl)*55)

#            $ renpy.transition(dissolve)

            call screen schedule(MC.girls)
            with Dissolve(0.15)

        elif result == "level_or_perks":

            if not renpy.predicting():
                call hide_details()

            $ girl = selected_girl

            $ renpy.transition(dissolve)

            $ tt = show_tt("top_right")

            if girl.can_spend_upgrade_points():

                show screen level(girl) #!

                with Dissolve(0.15)

            elif girl.perk_points > 0:

                $ girl = selected_girl

                call perks() from _call_perks

#               $ girl.check_combo_perks()

            $ renpy.block_rollback()

        elif result == "perks":

            if not renpy.predicting():
                call hide_details()

            $ girl = selected_girl

            call perks() from _call_perks_1

#            $ girl.check_combo_perks()

        elif isinstance(result, basestring) and result.startswith("up_stat"):

            $ girl = selected_girl
            $ stat = selected_stat

            if result == "up_stat":
                $ chg = 1
            elif result == "up_stat5":
                $ chg = 5
            elif result == "up_stat10":
                $ chg = 10
            elif result == "up_stat20":
                $ chg = 20
            elif result == "up_stat_all":
                $ chg = girl.get_max_stat_upgrade_points(stat)

            if girl.upgrade_points >= 1:

                $ r = girl.upgrade_stat(stat, chg) # Returns False if chg > maxed out stat

                if not r:
                    sill sad "Master, she cannot progress further until she ranks up."

        elif result == "sell":

            $ girl = selected_girl

            if not MC.can_sell(slavemarket, girl):
                slavegirl1 "You already sold us this girl once. You can't change your mind all the time. We're busy, you know."
                if renpy.call_screen("yes_no", "奴隶市场不会花钱购买她。你真的想不收取一分钱就出售[girl.fullname]吗？"):
                    $ MC.girls.remove(girl)

            else:
                $ price = girl.get_price("sell")

                $ result = renpy.call_screen("yes_no", "你真的想以 [price] 金币出售[girl.fullname]吗？")

                if result == True:

                    python:
                        relinquish_girl(girl)

                        MC.sell(slavemarket, girl, price)
                        game.track("sell girl gold", price)
                        test_achievement("sell girl gold")

                    if girl.get_love() >= 90:
                        $ unlock_achievement("sell girl love")
                        call dialogue(girl, "sold love") from _call_dialogue_18
                    else:
                        call dialogue(girl, "sold") from _call_dialogue_19

                    hide screen girl_profile
                    hide screen girl_stats
                    hide screen button_overlay

        elif result == "dismiss":

            $ girl = selected_girl

            if renpy.call_screen("yes_no", "你真的不想要[girl.fullname]了吗？她将恢复自由，永远离开这个城市。"):

                python:
                    if girl.items: # Unequip all items before dismiss
                        for it in list(girl.items): # shallow copy of list since deleting from girl.items
                            if it.equipped:
                                girl.unequip(it)
                            MC.take(girl, it)
                            renpy.notify("\n" + girl.name + " 失去了 " + it.name)
                            renpy.pause(0.5)

                    MC.girls.remove(girl)

                call dialogue(girl, "freed") from _call_dialogue_20

                hide screen girl_profile
                hide screen girl_stats
                hide screen button_overlay

        elif result == "equip":

            if not renpy.predicting():
                call hide_details()

            $ girl = selected_girl
            $ selected_item = None

            show screen dark_filter
            show screen item_tab(MC, girl, "girls")

            with Dissolve(0.15)


            while True:

                $ game.sort(MC.items, context = "MC items")
                $ game.sort(girl.items, context = "girls items")

                $ act = None

                $ res = ui.interact()

                python:
                    try:
                        it, act = res
                    except:
                        act = None

                if act == "give":
                    if it.equipped:
                        $ MC.unequip(it)
                        play sound it.sound

                    if MC.give(selected_girl, it):
                        hide screen item_profile

                elif act == "take":
                    if it.equipped:
                        $ selected_girl.unequip(it)

                    $ MC.take(selected_girl, it)

                    hide screen item_profile

                elif act == "equip":
                    $ MC.equip(it)
                    play sound it.sound
                    hide screen item_profile
                    $ MC.update_spells()

                elif act == "unequip":
                    $ MC.unequip(it)
                    play sound it.sound
                    hide screen item_profile
                    $ MC.update_spells()

                elif act == "gift":
                    hide screen item_profile
                    $ MC.gift(selected_girl, it)
                    play sound it.sound

                elif act == "give_equip":
                    if MC.give(selected_girl, it):
                        $ selected_girl.equip(it)
                        hide screen item_profile

                elif act == "give_use":
                    if it.equipped:
                        $ MC.unequip(it)
                        play sound it.sound

                    $ r, c = selected_girl.use_item(it)
                    play sound it.sound

                    if r == "used_up":
                        $ MC.items.remove(it)

                    hide screen item_profile

                elif act == "g_equip":
                    $ selected_girl.equip(it)
                    play sound it.sound
                    hide screen item_profile

                elif act == "g_unequip":
                    $ selected_girl.unequip(it)
                    play sound it.sound
                    hide screen item_profile

                elif act == "g_use":
                    $ r, c = selected_girl.use_item(it)
                    play sound it.sound

                    if r == "used_up":
                        hide screen item_profile

                elif act == "back":
                    call hide_everything() from _call_hide_everything_40
                    jump girls


        elif result == "rank":

            $ girl = selected_girl

            $ cost = rank_cost[girl.rank + 1]

            if MC.has_gold(cost):

                $ result = renpy.call_screen("yes_no", "你想花费 [cost] 金币为[girl.fullname]提升阶级吗？")

                if result == True:
                    $ girl.rank_up()
                    $ MC.gold -= cost

                    $ newrank = rank_name[girl.rank]

                    $ renpy.block_rollback()

                    call dialogue(girl, "rank up") from _call_dialogue_99
                    $ test_achievements(["rank B", "rank A", "rank S", "rank X"])

            else:
                sill "Master, you need [cost] gold to rank up this slave."

        elif result == "sex_act":

            $ girl = selected_girl
            $ sex_act = selected_sex_act

            $ r, reason = girl.toggle_sex_act(sex_act)

            if not r:
                call dialogue(girl, "refuse sex act") from _call_dialogue_100
                $ renpy.say("", reason)

        elif result == "stats":

            call screen girl_log() nopredict

            with Dissolve(0.15)

        elif result == "debug_pics":
            $ girl = selected_girl

            call screen debug_pics(girl) nopredict

        elif result == True: # Clicking anywhere on the dark filter screen
            hide screen notebook with Dissolve(0.1)

        elif result[0] == "badge":
            call screen girl_pick_badge(result[1])

        $ renpy.block_rollback()
        $ brothel.update_customer_count()


## PERKS ##

label perks(): # girl is passed by the previous label (girls)

    $ new_perks = []
    $ perk_points = girl.perk_points

    $ tt = show_tt("top_right")
    show screen perks(girl)
    with Dissolve(0.15)

    while True:
        $ result, obj = ui.interact() # bj is an archetype or perk

        if result == "unlock":
            if renpy.call_screen("yes_no", "你确定要花费2点特质点解锁{b}" + archetype_name_dict[obj] + "{/b}特质分支？"):

                play sound s_spell
                $ girl.unlock_archetype(obj)
                $ perk_points -= 2
                $ girl.perk_points -= 2

        elif result == "add":
            play sound s_spell
            $ new_perks.append(obj)
            $ perk_points -= 1
            $ renpy.restart_interaction()

        elif result == "commit":
            if new_perks:
                if renpy.call_screen("yes_no", "你确定要解锁 {b}" + str(len(new_perks)) + " 个新的特质吗{/b}?"):
                    play sound event_sounds["perk " + str(new_perks[-1].level)]

                    python:
                        for perk in new_perks:
                            r, msg = girl.acquire_perk(perk)
                            if not r:
                                renpy.say("", msg)

                    hide screen perks
                    return
            else:
                play sound s_click
                hide screen perks
                return

        elif result == "cancel":
            if new_perks:
                play sound s_fizzle
                jump perks
            else:
                play sound s_click
                hide screen perks
                return

        elif result == "leave":
            play sound s_click
            hide screen perks
            return


## SHOP ##

label shop:

    hide screen home
    hide screen tool

#    $ renpy.start_predict_screen("item_tab", MC, shop, "shop")

    if shop.love >= 10 and dice(100) > 98:
        call shop_bath_scene() from _call_shop_bath_scene

    scene black

    play sound "chimes.wav"


    show bg shop at center
    with Fade(0.15, 0.3, 0.15)

    if shop_firstvisit:
        shopgirl "Oh, a new customer! Lovely! And handsome at that, too..."

        shopgirl "Old man Gio told me you'd be coming soon. You and I are going to become the best of friends,
                  I'm sure... *wink*"

        shopgirl "We sell all kinds of mundane and rare items here, from all over Xeros. Come back
                  often, we have regular arrivals."

        $ shop_firstvisit = False

    if district.rank > 1 and not story_flags["shop restock"]:
        call shop_restock_intro() from _call_shop_restock_intro

    if shop.updated:
        $ shopgirl("A caravan has arrived, and we have new items. Check it out!")
        $ shop.updated = False

    else:
        $ shopgirl("Hi, handsome! Please take a look at my wares... *wink*{w=1.0}{nw}")

    show screen item_tab(MC, shop, "shop")
    $ tt = show_tt("top_right")


label shop_loop:

    $ game.sort(MC.items, context = "MC items")
    $ game.sort(shop.items, context = "shop items")

    $ renpy.block_rollback()

    $ r = ui.interact()

    python:
        try:
            it, act = r
        except:
            act = r

    if act == "buy":

        $ price = it.get_price("buy")

        if MC.has_gold(price):

#            $ result = renpy.call_screen("yes_no", "Do you really want to buy this [it.name] for [price] gold?")

#            if result == True:
            $ MC.buy(shop, it, price)

            play sound "cash.wav"

            hide screen item_profile

            shopgirl "You just bought the [it.name]. I'm sure you will put it to good use."

            $ shop.love += 1

        else:
            you "Shoot, I don't have enough gold..."

            jump shop_loop

    elif act == "sell":

        if not MC.can_sell(shop, it):
            shopgirl "You already sold this to me once! I'm sorry, but I'm not a pawn shop. You keep it now."
            if renpy.call_screen("yes_no", "商家不会花钱买回。你想不收取一分钱就去掉[it.name]吗？"):
                $ MC.items.remove(it)
                hide screen item_profile

        else:

            $ price = it.get_price("sell")

    #        $ result = renpy.call_screen("yes_no", "Do you really want to sell this [it.name] for [price] gold?")
    #        if result == True:

            if MC.sell(shop, it, price):
                play sound "cash.wav"
                hide screen item_profile

    elif act == "equip":

        $ MC.equip(it)
        play sound it.sound

    elif act == "unequip":

        $ MC.unequip(it)
        play sound it.sound

    elif act == "restock":
        if it:
            if renpy.call_screen("yes_no", "你确定要用 %s 金币来刷新商店吗？" % str(shop_restock_cost["shop"][game.chapter])):
                $ MC.gold -= shop_restock_cost["shop"][game.chapter]
                play sound s_gold
                $ shop.restock()
                jump shop
        elif shop.last_restock == calendar.time:
            shopgirl "You have already paid for a restock today.{w=0.8}{nw}"
        else:
            shopgirl "You do not have the necessary gold, sorry.{w=0.8}{nw}"


    elif act == "upgrade_shop":
        if it:
            $ chapter, cost, upgrade = shop_upgrades[shop.upgrade_level + 1]

            if renpy.call_screen("yes_no", "你确定要为商店升级%s %s吗？" % (str(cost[1]), cost[0])):
                $ shop.upgrade_shop(cost, upgrade)

                $ renpy.say(shopgirl, shopgirl_comment[cost[0]])

                shopgirl "Very good. I will have more items for you after the next inventory restock."

                if shop.can_upgrade():
                    shopgirl "If you bring me more materials, I may be able to expand my inventory again. Keep it up!"
        else:
            shopgirl "You do not have the necessary resources with you.{w=0.8}{nw}"

    elif act == "back":
        call hide_everything() from _call_hide_everything_41
        jump main


    jump shop_loop


## CITY MERCHANTS

label visit_merchant(merc):

    play sound s_chimes

    hide screen visit_location

    scene black

    show expression selected_location.get_pic(config.screen_width, int(config.screen_height*0.8)) at top

    with Fade(0.15, 0.3, 0.15)

    if merc == NPC_stella:
        show stella normal at center:
            yoffset 250
    elif merc == NPC_giftgirl:
        show giftgirl at center

    else:
        show expression merc.name.lower()

    with Dissolve(0.3)

    $ tt = show_tt("top_right")

    $ text1 = merchant_greetings[merc.name + " greeting"]

    merc.char "[text1]"

    if merc == NPC_twins:
        $ yesterday(merchant_greetings["Yesterday greeting"])

    if merc in minion_merchants:
        show screen item_tab(MC, merc, context="minion_merchant")

    else:
        show screen item_tab(MC, merc, context="city_merchant")

label visit_merchant_loop():

    while True:

        $ game.sort(MC.items, context = "MC items")

        if merc in city_merchants:
            $ game.sort(shop.items, context = "city_merchant items")
        elif merc in minion_merchants:
            $ game.sort(shop.items, context = "minion_merchant items")

        $ result = ui.interact()

        if result:

            python:
                try:
                    it, act = result
                except (ValueError, TypeError):
                    act = "ignore"

            if act == "ignore":
                pass

            if act == "restock":
                if it:
                    if merc in city_merchants:
                        $ restock_cost = shop_restock_cost["city merchants"][game.chapter]
                    elif merc in minion_merchants:
                        $ restock_cost = shop_restock_cost["minion merchants"][game.chapter]

                    if renpy.call_screen("yes_no", "你确定要用 %s 金币刷新商店吗？" % restock_cost):
                        $ MC.gold -= restock_cost
                        play sound s_gold
                        $ merc.restock()

                elif merc.last_restock == calendar.time:
                    merc.char "You have already paid for a restock today.{w=0.8}{nw}"

                else:
                    merc.char "You do not have the necessary gold.{w=0.8}{nw}"

            elif act == "sell":
                if not MC.can_sell(merc, it):
                    merc.char "You already sold this to me once! I'm sorry, but I'm not a pawn shop. You keep it now."
                    if renpy.call_screen("yes_no", "商家不会花钱买回。你想不收取一分钱就去掉[it.name]吗？"):
                        $ MC.items.remove(it)
                        hide screen item_profile

                else:
                    $ price = it.get_price("sell")

                    if MC.sell(merc, it, price):
                        play sound "cash.wav"
                        hide screen item_profile

            elif act == "buy":
                if MC.has_gold(it.get_price("buy")):
                    if isinstance(it, Minion):
                        $ res, text1 = farm.add_minion(it)
                        if res:
        #                    $ pic = it.pic
                            $ merc.items.remove(it)
                            $ MC.gold -= it.get_price("buy")

                            if not merc.flags["total value"]:
                                $ merc.flags["total value"] = it.get_price("buy")
                            else:
                                $ merc.flags["total value"] += it.get_price("buy")

                            play sound s_cash
                            hide screen item_profile
                            with dissolve
                            "[text1]"
                            $ test_achievements(["minions"])

                            if not story_flags["bought " + it.type]:
                                $ calendar.set_alarm(calendar.time+1, Event(label = "farm_first_" + it.type))
                                $ story_flags["bought " + it.type] = True

                        elif text1:
                            merc.char "[text1]"


                    else: # Items
                        $ MC.buy(merc, it, it.get_price("buy"))

                        if not merc.flags["total value"]:
                            $ merc.flags["total value"] = it.get_price("buy")
                        else:
                            $ merc.flags["total value"] += it.get_price("buy")

                        play sound s_cash
                        hide screen item_profile
                        with dissolve

                        $ text1 = merchant_greetings[merc.name + " bought something"]
                        merc.char "[text1]"

                        if merc == NPC_twins:
                            $ yesterday(merchant_greetings["Yesterday bought something"])
                else:
                    $ text1 = merchant_greetings[merc.name + " no money"]
                    merc.char "[text1]"

            elif act == "equip":

                $ MC.equip(it)
                play sound it.sound

            elif act == "unequip":

                $ MC.unequip(it)
                play sound it.sound

            elif act == "back":

                # Stella reward events
                call hide_everything() from _call_hide_everything_43

                if merc == NPC_stella:
                    if merc.flags["total value"] >= 1000 and not merc.flags["reward1"]:
                        $ merc.flags["reward1"] = True
                        call stella_reward1() from _call_stella_reward1
                    elif merc.flags["total value"] >= 2500 and not merc.flags["reward2"]:
                        $ merc.flags["reward2"] = True
                        $ merc.flags["new reward limit"] = 3500
                        call stella_reward2() from _call_stella_reward2
                    elif merc.flags["reward2"] and merc.flags["total value"] >= merc.flags["new reward limit"]:
                        $ merc.flags["new reward limit"] += 1000
                        call stella_reward3() from _call_stella_reward3

                jump visit_location

    return



## MAIN CHARACTER

label main_character:

    hide screen home
    hide screen tool

    scene black

    show bg armory at top
    show screen main_character
    show screen item_tab(left = None, right = MC, context = "MC")

    if show_spellbook:
        show screen spellbook

    with Dissolve(0.3)

    $ tt = show_tt("top_right")

#    $ MC.update_spells()

    $ renpy.block_rollback()
    $ test_achievements(["good", "neutral", "evil"])

    while True:

        $ game.sort(MC.items, context = "MC items")

        $ result = (None, None)

#        $ renpy.notify("resetting result")

        $ result = ui.interact()

        if result == "change_name":

            $ MC.name = renpy.input("你想改变自己的名字吗？", default = MC.name, length = 20)

            $ renpy.block_rollback()

        elif result == "previous_pic":

            $ MC.change_pic("previous")

        elif result == "next_pic":

            $ MC.change_pic("next")

        elif result == "raise_strength":
            $ r = MC.raise_stat("strength", 1)

            if r:
                $ MC.skill_points -= 1


        elif result == "raise_spirit":
            $ r = MC.raise_stat("spirit", 1)
            if r:
                $ MC.skill_points -= 1
                $ MC.update_spells()

        elif result == "raise_charisma":
            $ r = MC.raise_stat("charisma", 1)

            if r:
                $ MC.skill_points -= 1

        elif result == "raise_speed":
            $ r = MC.raise_stat("speed", 1)

            if r:
                $ MC.skill_points -= 1

        elif result[1] == "equip":
            $ MC.equip(result[0])
            play sound result[0].sound
            hide screen item_profile
            $ MC.update_spells()

        elif result[1] == "unequip":
            $ MC.unequip(result[0])
            play sound result[0].sound
            hide screen item_profile
            $ MC.update_spells()

        elif result[1] == "use":
            $ r = MC.use_item(result[0])
            play sound result[0].sound

            if r == "used_up":
                hide screen item_profile

        elif result[1] == "cast":
            $ MC.activate_spell(result[0])

        elif result[1] == "back":
            call hide_everything() from _call_hide_everything_42
            jump main

        $ test_achievements(["mc strength", "mc spirit", "mc charisma", "mc speed"])


## QUEST AND CLASSES POSTINGS ##

label postings:

    hide screen home
    hide screen tool

    scene black
    show bg town at top

    if postings_firstvisit:
        with Dissolve(0.3)

        show jobgirl with dissolve

        jobgirl "Hi there, friend!"

        jobgirl "You came looking for a job too?"

        you "Well, I'm not sure..."

        jobgirl "See this board over there? All kinds of people leave notes here for odd jobs and small tasks..."

        jobgirl "I use it every day to find work! There are also ads for various classes... That's how I learnt dancing!"

        jobgirl "But you have to be careful though... Some of those 'jobs' are posted by lecherous old men with only one thing in mind... Ew!"

        you "Lecherous old men... (An opportunity, perhaps?)"

        jobgirl "Well, I'll see you around. You look down on your luck. I hope you'll find some work soon!"

        hide jobgirl with dissolve

        you "Hey, wait!"

        you "She's gone..."

        $ quest_board.updated = False
        $ postings_firstvisit = False

    elif game.chapter >= 2 and not NPC_jobgirl.flags["stage"]: # jobgirl stage advances with every successive event
        call jobgirl_0() from _call_jobgirl_0
        $ quest_board.updated = False

    elif game.chapter >= 3 and NPC_jobgirl.flags["stage"] == 1: # jobgirl stage advances with every successive event
        call jobgirl_1() from _call_jobgirl_1
        $ quest_board.updated = False

    if quest_board.updated:
        jobgirl "Oh, it's you! Look, there are new tasks available."
        $ quest_board.updated = False

    if MC.girls == []:
        "You do not have any girl available at the moment."
        jump main

    if not selected_girl or selected_girl not in MC.girls:
        $ selected_girl = MC.girls[0]

    $ selected_quest = None

    $ qlist = quest_board.quests

    $ available_girls = MC.girls

    if quest_board.quests:
        $ selected_quest = quest_board.quests[0]

    $ selected_girl, available_girls = refresh_quest_girls(selected_girl, selected_quest)

    show screen postings(quest_board.quests)
    with Dissolve(0.3)
    $ tt = show_tt("top_right")

    $ renpy.block_rollback()

    while True:

        $ result = None
        $ result = ui.interact()

        if result == "classes":
            show screen postings(quest_board.classes)
            if quest_board.classes:
                $ selected_quest = quest_board.classes[0]
                $ selected_girl, available_girls = refresh_quest_girls(selected_girl, selected_quest)
            $ renpy.restart_interaction()

        elif result == "quests":
            show screen postings(quest_board.quests)
            if quest_board.quests:
                $ selected_quest = quest_board.quests[0]
                $ selected_girl, available_girls = refresh_quest_girls(selected_girl, selected_quest)
            $ renpy.restart_interaction()

        elif result == "change":
            $ selected_girl, available_girls = refresh_quest_girls(selected_girl, selected_quest)
            $ renpy.restart_interaction()

        elif result == "commit":
            if selected_quest.type == "class":
                $ t = "你确定要派" + selected_girl.name + "学习这个课程吗？将花费你 " + str(selected_quest.gold) + " 金币并且离开 " + str(selected_quest.duration) + " 天。"
            else:
                $ t = "你确定要派" + selected_girl.name + "执行这项任务吗？她将离开 " + str(selected_quest.duration) + " 天。"

            $ r = renpy.call_screen("yes_no", t)

            if r:
                call dialogue(selected_girl, "leave for " + selected_quest.type) from _call_dialogue_101
                $ selected_girl.commit(selected_quest)

                if selected_quest.type == "quest":
                    $ quest_board.quests.remove(selected_quest)
                    if quest_board.quests:
                        $ selected_quest = quest_board.quests[0]
                    else:
                        $ selected_quest = None
                    $ selected_girl, available_girls = refresh_quest_girls(selected_girl, selected_quest)

                elif selected_quest.type == "class":
                    $ MC.gold -= selected_quest.gold

                    if len(selected_quest.enrolled) >= selected_quest.capacity:
                        $ quest_board.classes.remove(selected_quest)
                        if quest_board.quests:
                            $ selected_quest = quest_board.quests[0]
                        else:
                            $ selected_quest = None
                        $ selected_girl, available_girls = refresh_quest_girls(selected_girl, selected_quest)
                        $ unlock_achievement("filled class")

                $ renpy.restart_interaction()

        elif result == "active_contract":
#             hide screen contract_tab
            call screen contract_tab(contract=calendar.active_contract, x=450, active=True)
            with Dissolve(0.5)


#### END BK MAIN FILE ####
