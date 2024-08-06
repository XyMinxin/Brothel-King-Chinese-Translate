#### LABELS & EVENTS ####

## Common tricks ##

## Plan event for later

# $ calendar.set_alarm(calendar.time + delay, Event(label = "label_to_call"))

## Show current brothel as background

#    scene black with fade
#    show expression bg_bro at top
#    with dissolve

## Show master bedroom as background

#     scene black with fade
#     show expression brothel.master_bedroom.get_pic() at top
#     with dissolve

## Show girl bedroom as background

# WIP

## Show common room as background

#     scene black with fade
#     show bg onsen with dissolve

## Show random common room as background

#     scene black with fade

#     if brothel.get_common_rooms():
#         $ room = brothel.get_random_room_pic_path()
#     else:
#         $ room = "black"

#     show expression room at top
#     with dissolve

## Show random common room as background (alternative - doesn't work if there are no common rooms)

    # scene black with fade
    # $ room = rand_choice([room.name for room in brothel.get_common_rooms()])
    # show expression "bg " + room at top with dissolve

## Show current location as background

#     scene black with fade
#     show expression selected_location.get_pic(wide=True) at top
#     with dissolve

## Show letter
#     call screen letter(header = "Title",
#                        message = "Message",
#                        signature = "Sig")

## Show NPC body
# show expression npc.char.image_tag


## GAME UTILITY EVENTS

label before_main_menu(): # Will show before main menu (standard Ren'py label)

    ## MODS ##

    $ update_mods()

    ## GIRL PACKS ##

    python:

        # 'story' girl packs are reserved for events and excluded from the game mixes
        gpacks = [gp for gp in GirlFilesDict.get_paths() if read_init_file_generate_as(GirlFilesDict.get_ini(gp)) != "story"]
        # Warning: 'paths' have been changed to pack names. Some renaming is needed here (best left for Chris12 to look at)

        old_gp = []
        new_gp = []

        if persistent.girl_packs != gpacks:
            if persistent.girl_packs:
                for gp in persistent.girl_packs:
                    if gp not in gpacks:
                        old_gp.append(gp)
                for gp in gpacks:
                    if gp not in persistent.girl_packs:
                        new_gp.append(gp)

    if old_gp:
        if len(old_gp) == 1:
            $ text1 = "The girl pack {b}{color=[c_red]}" + old_gp[0] + "{/color}{/b} couldn't be found and will be removed from the mix."
        else:
            $ text1 = "The following girl packs couldn't be found: {b}{color=[c_red]}" + and_text(old_gp) + "{/color}{/b}. They will be removed from the mix."

        $ renpy.call_screen("OK_screen", message=text1)

        python:
            for mix in persistent.girl_mix.values():
                for gp in old_gp:
                    if gp in mix:
                        mix.remove(gp)

    if new_gp:
        if len(new_gp) == 1:
            $ text1 = "A new girl pack: {b}{color=" + c_green + "}" + new_gp[0] + "{/color}{/b} has been found! What would you like to do?"
        else:
            $ text1 = str(len(new_gp)) + " new girl packs have been found:{b}{color=" + c_green + "}" + and_text(new_gp) + "{/color}{/b}. What would you like to do?"

        if renpy.call_screen("yes_no", text1, "Update all girl mixes", "Don't update (update manually)"):
            python:
                for mix in persistent.girl_mix.values():
                    for gp in new_gp:
                        if gp not in mix:
                            mix.append(gp)
        else:
            "Go to {b}Girl packs/Girl mix{/b} from the main menu to manually edit your mix."

    if len(gpacks) == 0:
        show screen OK_screen(event_color["bad"] % "Cannot start game: Missing girl packs", "The game couldn't find any girl packs in the girlpack folder (default: 'game\\girls\\'). Without any girl pack installed, the game cannot run.\n\nHave you downloaded and installed girl packs?\nVisit [URL] to get your first girl packs. If you're unsure which one to pick, check the release thread for the 'base girl pack' which contains over 20 high-quality packs.\n\nClick 'OK' to close the game.")
        "{nw}"
        $ renpy.quit()

    $ persistent.girl_packs = list(gpacks)

    # Tracks pack information in a dictionary
    python:
        gpinfo_dict = {}
        for gp in gpacks:
            gpinfo_dict[gp] = {"creator" : read_init_file_field(GirlFilesDict.get_ini(gp), "identity", "creator", _default="Unknown", skip_checks=True),
                               "version" : read_init_file_field(GirlFilesDict.get_ini(gp), "identity", "version", _default="-", skip_checks=True),
                               "description" : read_init_file_field(GirlFilesDict.get_ini(gp), "identity", "description", _default="No description.", skip_checks=True),}

    if not persistent.girl_mix["default"]:
        $ persistent.girl_mix["default"] = list(gpacks)

    # Ignore 'story' mixes

    # Offer to remove empty mixes

    python:
        empty_mixes = []

        for mix, packs in persistent.girl_mix.items():
            if mix != "default" and not packs:
                empty_mixes.append(mix)

    if empty_mixes:
        if renpy.call_screen("yes_no", "The following girl mixes are empty: %s. Would you like to delete them?" % and_text(empty_mixes), "Delete", "Ignore (update manually)"):
            python:
                for mix in empty_mixes:
                    delete_mix(mix)

    if config.version.endswith("R"): # 'R' at the end of the version number means it's the release version
        call screen OK_screen("Warning", "You are running an {b}unpatched{/b} version of Brothel King.\n\nAs the game is still in alpha, it is very important that you install the latest patch to avoid bugs.\n\nPlease do not report any bugs on the HentHighSchool/BK Forum unless you have installed the latest patch.")

    return

label after_load: # Happens after a game state is loaded
    # if debug: #!
    #     call init_moons ()

    if not hasattr(game, 'version'):
        $ game.version = "Unknown"

    if not hasattr(game, 'goal_channels'):
        $ game.goal_channels = goal_channels

    # $ story_mode = True #!

    if game.version != config.version:
        menu:
            "{b}{color=[c_red]}WARNING{/color}{/b}: This saved game was created with another version of the game ([game.version]). You are running version [config.version]. Using older saved games with a new version of BK might cause unexpected crashes or game-breaking bugs. Are you sure you want to continue?"

            "Yes, and deactivate future warnings for this game/this version":
                $ game.version = config.version # quick and dirty

                $ game.version = config.version
            "Yes, but warn me again":
                pass

            "No":
                show screen load
                $ renpy.full_restart()

        call screen OK_screen("Loading old saved game", "You have chosen to continue with your old saved game.\nIf you encounter bugs, {b}please do not report them on the BK forum{/b}.")

    return

label teleport(): # Clears everything on the screen as well as the call stack before jumping to selected_destination label

    call hide_everything() from _call_hide_everything

    scene black

    # Clears call stack
    python:
        for i in xrange(renpy.call_stack_depth()):
            renpy.pop_call()

    jump expression selected_destination


label hide_details(): # Hides all pop-ups in the girls screen
    hide screen rank_level_details
    hide screen mood_details
    hide screen sex_details
    hide screen trait_details
    hide screen perk_details

    return

label hide_everything():

    hide screen overlay
    hide screen resource_tab
    hide screen tool
    hide screen goal_ttip
    hide screen close
    hide screen home
    hide screen right_menu
    hide screen girls
    hide screen girl_tab
    hide screen girl_profile
    hide screen girl_stats
    hide screen button_overlay
    hide screen rank_level_details
    hide screen mood_details
    hide screen sex_details
    hide screen schedule
    hide screen level
    hide screen perks
    hide screen girl_log
    hide screen notebook
    hide screen districts
    hide screen visit_district
    hide screen visit_location
    hide screen brothel
    hide screen brothel_options
    hide screen furniture
    hide screen show_event
    hide screen show_img
    hide screen show_sex_event
    hide screen item_tab
    hide screen farm_tab
    hide screen item_profile
    hide screen girl_select
    hide screen main_character
    hide screen magic_tab
    hide screen postings
    hide screen farm_tab
    hide screen dark_filter
    hide screen girl_interact
    hide screen free_girl_interact
    hide screen girl_fast_actions
    hide screen brothel_report
    hide screen matchmaking
    hide screen night_log
    hide screen previous_night_log
    hide screen trait_details
    hide screen perk_details
    hide screen inventory
    hide screen inventory
    hide screen contract_tab
    hide screen resource_exchange
    hide screen tax_tooltip
    hide screen tax_tab
    hide success
    hide failure
    hide screen mojo_bar
    hide screen power_deck
    hide screen power_draw
    hide screen power_hand
    hide screen power_target
    hide screen power_details

    $ choice_menu_girl_interact = False

    return


label effect_expired(char, effects): # Where eff is a list of effects
    python:
        char.remove_effects(effects)

        for e in effects:
            if isinstance(char, Girl) and char.current_food_effect[e.target] == e: # Disables food lock
                char.current_food_effect[e.target] = None

            debug_notify(char.name + "'s " + e.type + " " + e.target + " effect has expired")

    return

label new_moon():
    $ calendar.moon = moons[calendar.month]
    $ update_effects()

    scene black with fade
    $ renpy.show_screen("show_event", calendar.moon.pic, config.screen_width, config.screen_height, _layer = "master")
    with dissolve

    if calendar.moon.sound:
        play sound calendar.moon.sound

    "New moon" "{i}The [calendar.moon.name!t] is out.{/i} [calendar.moon.description!t]"

    return


label sill_checks(): # Returns False if the player doesn't proceed with 'end day'

    $ alerts = []

    if brothel.get_risk() >= 5 and brothel.security < brothel.max_help:
        $ alerts.append("security")

    $ cleanliness = brothel.get_cleanliness()
    if cleanliness in ("dirty", "disgusting", "fire"):
        $ alerts.append("maintenance")

    $ working_girls_score = sum([girl.rank for girl in MC.girls if girl.works_today()])
    if brothel.customer_count < working_girls_score and brothel.advertising < brothel.max_help:
        $ alerts.append("advertising")

    if not alerts:
        return True

    show bg sill_hold at top with dissolve

    if "security" in alerts:

        sill sad "Master [MC.name]!\n{color=[c_red]}The threat to [brothel.name] is high or worse!{/color} You should hire more security.\nDo you want to end the day anyway?" (interact=False) #!
        menu:
            "Continue":
                pass
            "Change your brothel settings":
                return False

    if "maintenance" in alerts:

        if cleanliness == "fire":
            $ cleanliness = "at risk of a fire"

        sill sad "Master [MC.name]!\n{color=[c_red]}[brothel.name] is [cleanliness]!{/color} You should hire more cleaners.\nDo you want to end the day anyway?" (interact=False) #!
        menu:
            "Continue":
                pass
            "Change your brothel settings":
                return False


    if "advertising" in alerts:

        sill sad "Master [MC.name]!\n{color=[c_lightred]}Only [brothel.customer_count] customers are expected at [brothel.name] tonight.{/color} You should raise advertising.\nDo you want to end the day anyway?" (interact=False) #!

        menu:
            "Continue":
                pass
            "Change your brothel settings":
                return False

    return True


label receive_item(it, msg="You have received %s.", use_article=True, equip=False, use_sound=True): # If 'msg' is provided, it must include '%s' once for the item name to be inserted

    $ MC.add_item(it, equip, use_sound=use_sound)

    if use_article:
        $ msg = msg % article("{b}" + it.name + "{/b}")
    else:
        $ msg = msg % ("{b}" + it.name + "{/b}")

    $ renpy.block_rollback()

    show screen receive_item(it, msg)
    with dissolve

    pause

    hide screen receive_item
    with dissolve

    return


label latest_customer_satisfaction:
    show screen dark_filter(False)

    call screen customer_satisfaction(*latest_sat_report)

    hide screen dark_filter

    return


## DIFFICULTY

label choose_difficulty():
    scene black with fade
    play music m_suspense fadein 3.0

    # Sanity check - Remove unavalaible girl mixes

    while True:
        show screen quick_start
        $ r = ui.interact()

        if r:
            hide screen quick_start
            if r == "edit mix":
                call girlpack_menu() from _call_girlpack_menu_1

            else: # CONFIRM
                $ unlocking_extras(final=True)

                if game.starting_gold:
                    $ MC.gold = int(game.starting_gold)

                $ game.init_mixes()

                stop music fadeout 3.0
                return


## CHAPTER TRANSITIONS

label chapter(chapter = None, silent=False, forced=False): ## Shows the chapter intro with text1 as chapter number and text2 as chapter title

    python:
        if not chapter:
            chapter = game.chapter
        else:
            game.chapter = chapter
        game.set_max_girl_level()

        if chapter <= 1:
            bg_bro = "bg brothel1"
            unlock_pic(bg_bro)

        elif 2 <= chapter <= 6:

            game.set_goals(chapter_goals[chapter])
            game.seen_goal_message = False

        elif chapter >= 7:

            game.set_goals(chapter_goals[chapter])

            if game.diff in ("normal", "hard", "insane"):
                unlock_achievement("win " + game.diff)

        lbl = None


        if game.chapter == 0:

            text1 = '序章'

            text2 = "阴暗之地行阴暗之事"

        elif game.chapter == 1:

            text1 = "第一章"

            text2 = "新起点"

        elif game.chapter == 2:

            text1 = "第二章"

            text2 = "暮色之刃"

            lbl = "chapter2"

        elif game.chapter == 3:

            text1 = "第三章"

            text2 = "危机四伏"

            if story_mode:
                lbl = "c3_homura_okiya3"

        elif game.chapter == 4:

            text1 = "第四章"

            text2 = "攀权附贵"

        elif game.chapter == 5:

            text1 = "第五章"

            text2 = "加官进爵"

        elif game.chapter == 6:

            text1 = "第六章"

            text2 = "青楼之王"

        else:

            text1 = "尾声"

            text2 = "后日谈"

    call hide_everything() from _call_hide_everything_38
    scene black with fade

    if not silent:

        play sound s_chapter

        $ text1 = Text((text1), size=50, yalign=0.4, xpos=0.5, drop_shadow=(2,2))

        $ text2 = Text((text2), size=64, yalign=0.6, xpos=0.5, drop_shadow=(2,2), font = "DejaVuSans.ttf")

        show expression text1
        with easeinleft

        show expression text2
        with easeinleft

        pause

        with flash

        stop sound fadeout 2.0

        hide expression text1
        with easeoutright

        hide expression text2
        with easeoutright

    $ renpy.block_rollback()

    if lbl:
        $ renpy.call(lbl)

    return



label chapter2:

    if not debug_mode:
        "You have reached a new chapter! There is a total of 6 chapters. With each chapter, you can move to a new brothel and develop your business."

        sill happy "You can now move this operation to a larger brothel. Go to the {b}city{/b} tab to set up your new quarters."

        call got_license (1) from _call_got_license

    $ story_add_event("meet_giftgirl")
    $ story_add_event("meet_twins")
    $ story_add_event("meet_gurigura")
    $ story_add_event("meet_ramias")
    $ story_add_event("meet_katryn")
    $ story_add_event("meet_riche")

    return


label rank_message:

    if game.chapter == 2 and not debug_mode:

        sill "You now hold a proper pimp license! It is time I told you about your girls' ranks and reputation."

        menu:
            sill "Would you like to learn about girl ranks and reputation?"

            "Yes":
                call help_rank_introduction from _call_help_rank_introduction_1

            "No":
                pass

    elif game.chapter in (4, 6, 7):

        if game.chapter == 4:
            call got_license(2) from _call_got_license_1
        elif game.chapter == 6:
            call got_license(3) from _call_got_license_2

        $ rk = rank_name[district.rank]

        "Your girls may now reach rank [rk]."

    return


label reached_goal():

    if game.seen_goal_message == False:
        if game.chapter == 1 and story_mode and not debug_mode:
            call c1_reached_goal() from _call_c1_reached_goal

        else:
            $ text1 = __("You have reached your current goal:\n") + __(game.get_goal_description()) + __("\n\nYou may now advance to the next chapter!")

            call screen OK_screen(__("Goal reached!"), text1, pic = Picture(path="UI/goal.webp"))

        $ game.seen_goal_message = True

    return

label advance_to_chapter(chapter, silent=False, free=False):

    hide screen home

    # Calculates auction price
    $ old_brothel_name = brothel.name
    $ old_brothel_auction_price = brothel.get_auction_value()

    $ renpy.call("chapter", chapter, silent)

    # Resets temp gossip
    $ temp_gossip = []

    # Resets time pressure from taxes
    $ NPC_taxgirl.time_pressure_modifier = 0.0

    if chapter >= 7:
        call auction_brothel() from _call_auction_brothel_1
        $ change_district(endless_district, free)
        $ change_brothel()
        $ renpy.block_rollback()

        call rank_message from _call_rank_message

        if not debug_mode:
            menu:
                sill "Do you want to rename your brothel for the occasion?"

                "Yes":
                    $ brothel.name = renpy.input("Change name:", default = brothel.name, length = 40)
                "No":
                    pass

        $ persistent.new_game_plus = True

        return

    else:
        show screen districts(context = "relocate")

        while True:

            $ renpy.block_rollback()

            $ chosen_district = None

            $ sill(__("You can now move to a larger brothel (maximum ")+ str(blist[chapter].get_maxbedrooms()) + __(" bedrooms).\nChoose a district to set up your new brothel."), interact = False)

            $ chosen_district = ui.interact()

            if isinstance(chosen_district, District):
                if chosen_district.name == district.name:
                    "[chosen_district.name] is the district where you are currently established. Please choose a different district."

                else:
                    "[chosen_district.description]"
                    if chosen_district.room == "free":
                        $ free_room_text = __("\nYou will receive a free room of your choice.")

                    elif chosen_district.room != []:
                        $ free_room_text =  __("\nYou will receive a {b}free ") + __(location_name_dict[chosen_district.room[0]]) + "{/b}."

                    else:
                        $ free_room_text = ""

                    $ textcn = location_name_dict[chosen_district.name]
                    if renpy.call_screen("yes_no", __("Do you really want to move your brothel to {b}[chosen_district.name]{/b}?\n\n{size=-2}This will reset all your room improvements, but you will keep your furniture and decorations.") + __(free_room_text)):
                        $ change_district(chosen_district, free)
                        $ renpy.block_rollback()

                        hide screen districts
                        with Fade(0.15, 0.3, 0.15)

                        if game.chapter > 2 or (game.chapter == 2 and not story_mode):
                            call auction_brothel() from _call_auction_brothel_2 # Chapter 2's auction is part of the intro event
                            $ change_brothel()
                        elif story_mode:
                            call c2_intro() from _call_c2_intro

                        call rank_message from _call_rank_message_1
                        call screen OK_screen(__("You have received a new goal"), __(game.get_goal_description(channel="advance")), pic = Picture(path="UI/goal.webp"))

                        if game.chapter == 2 and (debug_mode or not story_mode):
                            $ NPC_carpenter.active = True
                            $ unlocked_shops.append(NPC_stella)

                        if not debug_mode:
                            menu:
                                sill "Do you want to rename your brothel for the occasion?"

                                "Yes":
                                    $ brothel.name = renpy.input("Change name:", default = brothel.name, length = 40)
                                "No":
                                    pass

                        hide screen districts
                        return


label got_license(level):

    $ lic_name, lic_pic = license_dict[level]

    call screen OK_screen(__("New license available!"), __("You have received a brand new ") + __(location_name_dict[lic_name]) + __(". Good work!"), pic = Picture(lic_pic, "UI/" + lic_pic))

    return


## EVENT DISPLAY

label play_events(_type):

    $ ev_list = get_events(_type) # Get events checks which events happen for a given type
    call display_events(ev_list) from _call_display_events

    return


label display_events(ev_list):

    while ev_list:
        $ ev = ev_list.pop(0)

#        "Playing [ev.label] with type [ev.type]."

        $ ev.play()
        $ ev.happened = True

        stop music fadeout 3.0

        if ev.label:
            $ story_flags[ev.label] = True

    return


label show_night_event(ev, save=False):

    if persistent.skipped_events[ev.type]:
        $ renpy.notify("Skipping event...")
        return

    if isinstance(ev.changes, NightChangeLog):
        $ ev.changes.adjust_separators()

    if ev.pic:
        show screen show_img(ev.pic, ev.background)

    show screen night(ev.pic, event_bg=ev.background, changes=ev.changes)

    if ev.sound:
        play sound ev.sound

    if ev.with_st:
        with ev.with_st

    if ev.char:
        if count_lines(ev.text, 85) > 5:
            $ txt_sz = int(config.screen_height*0.0222)
        else:
            $ txt_sz = int(config.screen_height*0.025)
    else:
        if count_lines(ev.text, 100) > 5:
            $ txt_sz = int(config.screen_height*0.025)
        else:
            $ txt_sz = int(config.screen_height*0.0277)

    $ txt_sz = max(10, txt_sz)

    $ text_descript = "{size=%i}%s{/size}" % (txt_sz, ev.text)

    $ debug_night_text.append([ev.char, text_descript])
    $ debug_night_text.append(ev.changes)

    python:
        try:
            renpy.say(ev.char, text_descript)
        except:
            raise AssertionError("Error displaying text: %s. Farm debug log: %s" % (text_descript, str(debug_night_text)))

    if save:
        $ renpy.force_autosave(take_screenshot=True, block=True)
        $ renpy.block_rollback()

    hide screen show_img
    hide screen night
    hide screen night_ttip

    return

label debug_night_messages(i=0):

    while i < len(debug_night_text):
        if isinstance(debug_night_text[i], NightChangeLog):
            show screen night_right(debug_night_text[i])
            pause

        elif debug_night_text[i]:
            $ char, msg = debug_night_text[i]

            $ renpy.say(char, msg)

        $ i += 1

    return


## GIRL UTILITY EVENTS


label run_away(girl):

    $ renpy.block_rollback()

    sill sad "Master! [girl.fullname] has escaped!!!"

    $ unlock_achievement("runaway")

    if girl in farm.girls:
        $ farm.remove_girl(girl)

    if girl in MC.girls:
        $ MC.girls.remove(girl)

    if girl in brothel.master_bedroom.girls:
        $ brothel.master_bedroom.girls.remove(girl)

    $ MC.escaped_girls.append(girl)

    hide screen girl_profile
    hide screen girl_stats
    hide screen button_overlay

    with fade

    $ hunters = ""
    $ cost1 = 250 * district.rank
    $ cost2 = 100 * district.rank
    $ cost3 = 50 * district.rank

    menu:

        sill "What will you do?"

        "Hire bounty hunters":

            menu:

                "Choose which bounty hunters to send on her trail."

                "The sisterhood of the night ([cost1] gold)" if MC.has_gold(cost1):

                    $ MC.gold -= cost1

                    $ hunters = "sisters"
                    $ hunt_delay = dice(2)

                    $ renpy.block_rollback()

                    play sound s_gold

                    sill sad "It will be done."

                "The slavers guild ([cost2] gold)" if MC.has_gold(cost2):

                    $ MC.gold -= cost2

                    $ hunters = "slavers"
                    $ hunt_delay = dice(3)+1

                    $ renpy.block_rollback()

                    play sound s_gold

                    sill sad "It will be done."

                "The city guard ([cost3] gold)" if MC.has_gold(cost3):

                    $ MC.gold -= cost3

                    $ hunters = "guards"
                    $ hunt_delay = dice(3)+3

                    $ renpy.block_rollback()

                    play sound s_gold

                    sill sad "It will be done."

                "Change your mind and look for her yourself":

                    $ hunters = "you"
                    $ hunt_delay = dice(6)

                    $ renpy.block_rollback()

                    you "I will look for her myself."

                    "She might reappear in a few days, somewhere in the city. You should look around."


        "Look for her yourself":

            $ hunters = "you"
            $ hunt_delay = dice(6)

            $ renpy.block_rollback()

            you "I will look for her myself."

            "She might reappear in a few days, somewhere in the city. You should look around."

        "Let her go":

            you "I guess she didn't really belong here. Let her go."

            $ MC.good += 1

    if hunters:
        $ calendar.set_alarm(calendar.time + hunt_delay, Event(label = "found_runaway_girl", object = (girl, hunters), order = 1))

    return


label found_runaway_girl(obj):

    $ renpy.block_rollback()

    $ girl, hunters = obj

    if hunters == "you":

        ## After a delay, the girl will return to a random location to be found by the player

        $ girl.location = rand_choice(game.location_slots)

    else:
        $ unlock_achievement("caught NPC")
        if hunters == "sisters":

            "The sisters have brought you [girl.fullname] back."

            girl.char "..."

            "[girl.name] looks absent-minded. She hasn't been hurt, but has a strange bruise on her neck."

            $ girl.change_stat("obedience", 5)

        elif hunters == "slavers":
            "The slavers have brought you [girl.fullname] back."

            girl.char "I don't want to go back... *sob*"

            "The solemn guild henchmen ignore her plea and deliver her to you. She has been roughed up a little, but she'll be fine."

            $ girl.change_stat("obedience", 1)

        elif hunters == "guards":

            "The city guard have brought you [girl.fullname] back, kicking and screaming."

            girl.char "Let me go you brutes! Aw, I hate you all..."

            "The guards laugh and push her to the ground in front of the brothel. She is half naked and her body reeks of semen. It seems they raped her repeatedly before bringing her back."

            $ girl.change_fear(5)
            $ girl.pop_virginity("rape")


        if len(MC.girls) >= brothel.bedrooms:

            sill sad "Master! There's a problem. We don't have room for her in the brothel..."

            label found_runaway_girl_no_room:

                menu:
                    "What do you want to do?"

                    "Ask them to come back tomorrow":
                        $ come_back = 1

                    "Ask them to come back in a week":
                        $ come_back = 7

                    "Sell her":
                        $ come_back = 0
                        $ MC.gold += girl.get_price("sell")
                        $ MC.escaped_girls.remove(girl)
                        $ MC.neutral += 1
                        play sound s_cash

                    "Send her to the farm" if farm.active and farm.has_room():
                        $ come_back = 0

                        $ MC.escaped_girls.remove(girl)
                        $ farm.send_girl(girl, FarmProgram(girl))
                        $ girl.track_event("ran away")

                        "{b}[girl.fullname]{/b} has been sent to the farm."

                    "Let her go":
                        $ come_back = 0
                        $ MC.escaped_girls.remove(girl)
                        $ MC.good += 1

                if come_back:
                    $ calendar.set_alarm(calendar.time + come_back, Event(label = "found_runaway_girl_come_back", object = (girl, hunters), order = 1))

        else:

            $ MC.escaped_girls.remove(girl)

            $ MC.girls.append(girl)

            if not brothel.can_have(girl.job):
                "She couldn't go back to being a [girl.job], so she was set to rest."
                $ girl.set_job(None)

            $ girl.track_event("ran away")

            "{b}[girl.fullname]{/b} is back."

    return


label found_runaway_girl_come_back(obj):

    $ renpy.block_rollback()

    $ girl, hunters = obj

    "The [hunters] are back with [girl.fullname] in chains. She looks exhausted."

    you "We'll take it from here."

    if len(MC.girls) >= brothel.bedrooms:

        sill sad "Master! There's a problem. We don't have room for her in the brothel..."

        menu:
            "What do you want to do?"

            "Ask them to come back tomorrow":
                $ come_back = 1

            "Ask them to come back in a week":
                $ come_back = 7

            "Sell her":
                $ come_back = 0
                $ MC.gold += girl.get_price("sell")
                $ MC.escaped_girls.remove(girl)
                $ MC.neutral += 1
                play sound s_cash

            "Send her to the farm" if farm.active and farm.has_room():
                $ come_back = 0

                $ MC.escaped_girls.remove(girl)
                $ farm.send_girl(girl, FarmProgram(girl))
                $ girl.track_event("ran away")

                "{b}[girl.fullname]{/b} has been sent to the farm."

            "Let her go":
                $ come_back = 0
                $ MC.escaped_girls.remove(girl)
                $ MC.good += 1

        if come_back:
            $ calendar.set_alarm(calendar.time + come_back, Event(label = "found_runaway_girl_come_back", object = (girl, hunters), order = 1))

    else:

        $ MC.escaped_girls.remove(girl)

        $ MC.girls.append(girl)

        if not brothel.can_have(girl.job):
            "She couldn't go back to being a [girl.job], so she was set to rest."
            $ girl.set_job(None)

        "{b}[girl.fullname]{/b} is back."

    return


label found_escaped_girl(girl):

    $ renpy.block_rollback()

    if MC.interactions > 0:

        $ MC.interactions -= 1

        "On your way to the [girl.location], you see [girl.name], sitting in the dirt and trembling in her torn clothes. It seems she hasn't eaten in days."

        $ pic = girl.get_pic("hurt", "sad", and_tags=["profile"], soft=True)
        if not pic:
            $ pic = girl.get_pic("profile", soft=True)

        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        "She hasn't seen you yet."

        if len(MC.girls) >= brothel.bedrooms:
            you "Oh, but I haven't got enough room in the brothel to take her back."

            menu:
                "What do you do?"

                "Come back later":
                    you "Well, I'll try and catch her another day."

                    $ girl.location = rand_choice(game.location_slots)

                    "[girl.fullname] has moved to a new location."

                "Forget about her":
                    you "Forget it. I was never too fond of her anyway."
                    $ MC.escaped_girls.remove(girl)

            hide screen show_event
            with dissolve

            return

        menu:

            "What do you do?"

            "Persuade her to come back.":

                $ renpy.block_rollback()

                you "[girl.name]... It's me. Look, I know life at the brothel can be hard, but you should come back. We miss you."

                if (dice(100) + MC.charisma * 5 + girl.love - girl.fear) >= 67:

                    "Sobbing, she runs into your arms."

                    girl.char "I'm so sorry, Master... I'm sorry..."

                    "She cries on your shoulder for a while. Taking her by the hand, you take her back to the brothel."

                    with dissolve

                    $ girl.change_love(2)
                    $ girl.change_fear(-3)

                    $ MC.escaped_girls.remove(girl)

                    $ MC.girls.append(girl)

                    if not brothel.can_have(girl.job):
                        "She couldn't go back to being a [girl.job], so she was set to rest."
                        $ girl.set_job(None)

                    $ girl.track_event("ran away")

                    "{b}[girl.fullname]{/b} is back."
                    $ unlock_achievement("caught MC")

                else:

                    "Startled by your approach, she jumps to her feet and runs into an alley."

                    "You try calling after her, but it's too late. She's already gone."

                    $ girl.change_love(1)

                    $ girl.location = rand_choice(game.location_slots)

            "Threaten her.":

                $ renpy.block_rollback()

                you "There you are! Look at you... You're a wreck. At this rate, you will starve before the end of the week. You better come back, or else..."

                if (dice(100) + MC.charisma * 5 + girl.fear - girl.love) >= 67:

                    "She breaks down in tears."

                    girl.char "Stop... Enough, please... I've learned my lesson. I'll follow you."

                    "Yanking her to her feet, you push her forward and bring her back to the brothel."

                    with dissolve

                    $ girl.change_love(-1)
                    $ girl.change_fear(2)

                    $ MC.escaped_girls.remove(girl)

                    $ MC.girls.append(girl)

                    if not brothel.can_have(girl.job):
                        "She couldn't go back to being a [girl.job], so she was set to rest."
                        $ girl.set_job(None)

                    $ girl.track_event("ran away")

                    "{b}[girl.fullname]{/b} is back."
                    $ unlock_achievement("caught MC")

                else:

                    "She gives you a defiant look and hisses at you."

                    girl.char "Never!"

                    "With desperate strength, she leaps to her feet and darts away."

                    "You swear and curse after her as she disappears into a crowd."

                    $ girl.change_love(-1)
                    $ girl.change_fear(1)

                    $ girl.location = rand_choice(game.location_slots)


            "Force her to come back.":

                $ renpy.block_rollback()

                "Not saying anything, you approach her from behind, and grab her firmly by her hair."

                you "You're going to come with me, you bitch!"

                if fight(MC, girl):

                    "She gasps in surprise as you yank her to the side like a ragdoll and slap her senseless."

                    "Loading her on your shoulder, you bring her kicking and screaming back to the brothel."

                    with dissolve

                    $ girl.change_fear(MC.get_defense())
                    $ girl.change_love(-3)
                    $ girl.change_fear(3)

                    $ MC.escaped_girls.remove(girl)

                    $ MC.girls.append(girl)

                    if not brothel.can_have(girl.job):
                        "She couldn't go back to being a [girl.job], so she was set to rest."
                        $ girl.set_job(None)

                    $ girl.track_event("ran away")

                    "{b}[girl.fullname]{/b} is back."
                    $ unlock_achievement("caught MC")

                else:

                    "With uncanny speed, she turns toward you and bites your hand with all her strength."

                    "You scream in pain and let go as the blood runs down your fingers. Jumping aside, she bolts down the street like a frightened hare."

                    you "Damn you, you bitch!"

                    $ girl.change_love(-3)
                    $ girl.change_fear(-1)

                    $ girl.location = rand_choice(game.location_slots)

            "Forget her":
                you "Well, she's on her own now. It was her choice..."
                $ MC.escaped_girls.remove(girl)

            "Leave her for now":
                you "I haven't got time to deal with this now."

    hide screen show_event
    with dissolve

    return


label take_leave(girl, day_nb):

    $ plu = plural(day_nb)

    "[girl.fullname] is leaving. She will be back in [day_nb] day[plu]."

    $ girl.away = True
    $ girl.return_date = calendar.time + day_nb

    $ add_event("return_from_leave", call_args = [girl], date = calendar.time + day_nb)
#     $ calendar.set_alarm(calendar.time + day_nb, Event(label = "return_from_leave", object = girl))

    return

label return_from_leave(girl, silent=False):

    if not silent:
        sill happy "Master! [girl.fullname] has returned from her leave."

    $ girl.away = False

    return

label return_from_quest(girl, quest):

    $ renpy.block_rollback()

    python:
        girl.return_from(quest)
        title, description = quest.get_results(girl)

    play sound quest.sound

    call screen OK_screen(title, description, pic = girl.portrait)

    return


label job_up(obj): # This event describes the results of job ups

    python:

        girl, job, mylevel = obj

#        mylevel = girl.job_level[job]

        text1 = girl.fullname + __(" is now ") + article(__(rank_name[job + str(mylevel)]))

        primary, secondary, boost1, boost2 = job_up_dict[job]

        text2 = "\n" + __(primary.capitalize()) + " {color=[c_emerald]}+" + str(job_up_change[mylevel][0]) + "{/color}"
        text2 += "\n" + __(secondary.capitalize()) + " {color=[c_emerald]}+" + str(job_up_change[mylevel][1]) + "{/color}"

        if job_up_change[mylevel][2] != 0:

            text2 += "\n" + __(boost1.capitalize()) + " {color=[c_emerald]}+" + str(job_up_change[mylevel][2]) + "{/color}"
            text2 += "\n" + __(boost2.capitalize()) + " {color=[c_emerald]}+" + str(job_up_change[mylevel][2]) + "{/color}"

        text2 += __("\n\n Skill level +1 {image=img_star}")

    call screen OK_screen(text1, text2, pic = girl.portrait)

    return

label too_tired(girl):

    "[girl.fullname] has come to see you."

    $ score = girl.get_love() - girl.get_fear()

    if score >= 10:
        girl.char "Oh, Master [MC.name]... I'm so tired, I don't think I can work tomorrow... Would you give me a little break? [emo_heart]"

    elif score <= -10:
        girl.char "Master, I... Forgive me for saying this, but... I don't think I can work tomorrow, I feel very tired..."

    else:
        girl.char "Master [MC.name]. I'm too tired to work tomorrow, I can't go on like this... Please give me some rest."

    menu:
        extend ""
        "Give her the day off":
            if MC.get_alignment() == "evil":
                $ text1 = " You better work extra hard after this."
            else:
                $ text1 = ""

            you "Fine, take the day off if you need it.[text1]"

            $ girl.get_day_off(1)
            $ girl.change_fear(-1)
            $ girl.change_mood(2)

        "Refuse":
            you "No way. You've got a job to do, so do it."
            girl.char "Aw..."

            $ girl.change_fear(1)
            $ girl.change_mood(-2)

    return



label reset_workday(obj):

    $ girl, day, charge = obj

    $ girl.workdays[day] = charge

    $ girl.block_schedule = False

    return

label restore_upkeep(girl):

    $ girl.restore_upkeep()

    return


label show_relationship_change(girl1, girl2, old_status, new_status):

    with dissolve

    show screen night(girl1.profile)
    with dissolve

    if new_status == "friend":

        if girl1.is_("extravert"):
            girl1.char "Hey, [girl2.name]! Let's work together, it will be more fun!"
        elif girl1.is_("introvert"):
            girl1.char "Oh, [girl2.name]... *blush* Can you show me how you do this?"

        show screen night(girl2.profile)
        with dissolve

        girl2.char "Sure!"

        "[girl1.name] and [girl2.name] are now friends."

        $ girl1.change_mood(2)
        $ girl2.change_mood(2)

    elif new_status == "rival":

        if girl2.lastname:
            $ text1 = girl2.lastname
        else:
            $ text1 = girl2.fullname

        if girl1.is_("extravert"):
            girl1.char "Hey, [text1]! Why don't you get out of my way?"
        elif girl1.is_("introvert"):
            girl1.char "Oh, it's you, [text1]... I was just leaving, anyway."

        show screen night(girl2.profile)
        with dissolve

        if girl1.is_("extravert"):
            girl2.char "Who do you think you are, you stuck-up bitch?"
        elif girl1.is_("introvert"):
            girl2.char "That's just fine. I want nothing to do with you..."

        "[girl1.name] and [girl2.name] are now rivals."

        $ girl1.change_mood(-2)
        $ girl2.change_mood(-2)

    elif new_status == "normal":

        girl1.char "Oh, hi, [girl2.name]..."

        show screen night(girl2.profile)
        with dissolve
        girl2.char "Hi."

        "[girl1.name] and [girl2.name] are no longer [old_status]s."

    else:

        $ raise AssertionError("Status not found: " + new_status)

    hide screen night

    return

label random_relationship_event(glist):

    if len(glist) < 2:
        return

    $ girl1, girl2 = rand_choice(glist, 2)

    $ rel = girl1.get_friendship(girl2)

    if rel == "friend":

        show screen night(girl1.profile)
        with dissolve

        girl1.char "[girl2.name], you're so cool!"

        girl2.char "Thanks!"

        hide screen night

        $ girl1.change_mood(1)
        $ girl2.change_mood(1)

    elif rel == "rival":

        show screen night(girl1.profile)
        with dissolve

        if girl2.lastname:
            $ text1 = girl2.lastname
        else:
            $ text1 = girl2.fullname

        girl1.char "[text1]... Master hasn't got around to sell you yet?"

        girl2.char "Grrr..."

        hide screen night

        $ girl1.change_mood(-1)
        $ girl2.change_mood(-1)

    return


label auto_train(girl):

    if girl not in MC.girls:
        $ brothel.master_bedroom.remove_girl(girl)
        return

    call hide_everything() from _call_hide_everything_44

    scene black
    show expression brothel.master_bedroom.get_pic(x=config.screen_width, y=config.screen_height) at top
    with dissolve

    if girl.away or girl.farm:
        "[girl.fullname] is away and cannot be trained."
        return

    elif girl.MC_interact_counters["train"] >= 1:
        "[girl.fullname] has already trained today. She cannot train more than once per day."
        return

    elif girl.exhausted or girl.hurt > 0:
        "[girl.fullname] is exhausted or hurt, and unable to train tonight."
        return

    "[girl.fullname] is waiting for you in the bedroom for tonight's training."

label auto_train_menu():

    if MC.get_effect("special", "notebook"):
        $ selected_girl = girl
        $ choice_menu_girl_interact = True
#    show screen dark_filter
    show screen overlay

    menu:
        "[girl.fullname] is waiting for you in the bedroom for tonight's training."

        "Train her":
            if girl.MC_interact_counters["train"] >= 1:
                "[girl.fullname] has already trained today. She cannot train more than once per day."
            else:
                hide screen overlay
                call slave_interact(girl, free=True) from _call_slave_interact_2

        "Don't train her":
            pass

        "Remove her from your room":
            you "Go back to your bedroom now. I am done with you."

            $ brothel.master_bedroom.remove_girl(girl)

            "[girl.fullname] has left the master bedroom."

    $ choice_menu_girl_interact = False
    hide screen dark_filter
    hide screen overlay

    return




## RESOURCES AND FURNITURE

label resource_gained(resource, number): # Where resource is a string
    if resource_dict[resource].sound:
        play sound resource_dict[resource].sound
    show screen resource_gain(resource, number)
    with dissolve

    $ renpy.choice_for_skipping()
    $ renpy.pause(0.8, hard=True)

    hide screen resource_gain
    with dissolve

    return

label test_resources():

    $ resource = "diamond"
    $ number = 1
    $ MC.gain(resource, number)

    ""
    $ tt = show_tt("top_right")
    show screen resource_tab()

    "End"

    return

label furniture_built(furn):

    if furn == vitals_scanner:
        call vital_scanners_built() from _call_vital_scanners_built

    else:
        carpenter "Hey, boss! I've just finished work on the [furn.name]. I hope you like it."

    $ furn.build()
    $ brothel.current_building = None

    if furn.name == "Priestess outfit":
        call add_billboard() from _call_add_billboard

    return

label collect_wood():

    $ resource = "wood"

    if MC.get_items(name="采集者MkI型") and not auto_extractors[resource]: # When the player has an extractor in inventory and the location has none
        menu:
            "Do you want to set up a resource extractor in this location (cannot be undone)?"

            "Yes, set up a resource extractor Mk I in this location":
                play sound resource_dict[resource].sound
                $ MC.items.remove(MC.get_items(name="采集者MkI型")[0])
                $ resource_dict[resource].activate_extractor()
                return

            "No, collect resources instead":
                pass

            "Cancel":
                return

    if auto_extractors[resource + " ON"]: # When an extractor is ON
        menu:
            "You have an active resource extractor in this location. Do you want to turn if {b}OFF{/b}?"

            "Turn it OFF":
                play sound s_fiz
                $ auto_extractors[resource + " ON"] = False
                return

            "Just collect resources":
                pass

            "Cancel":
                return

    elif auto_extractors[resource]: # When an extractor is OFF
        menu:
            "You have an inactive resource extractor in this location. Do you want to turn if {b}ON{/b}?"

            "Turn it ON":
                play sound resource_dict[resource].sound
                $ auto_extractors[resource + " ON"] = True
                return

            "Just collect resources":
                pass

            "Cancel":
                return

    if MC.collect_resource(resource) == "KO":
        "You cannot collect wood more than once per day."
    return

label collect_leather():

    $ resource = "leather"

    if MC.get_items(name="采集者MkI型") and not auto_extractors[resource]: # When the player has an extractor in inventory and the location has none
        menu:
            "Do you want to set up a resource extractor in this location (cannot be undone)?"

            "Yes, set up a resource extractor Mk I in this location":
                play sound resource_dict[resource].sound
                $ MC.items.remove(MC.get_items(name="采集者MkI型")[0])
                $ resource_dict[resource].activate_extractor()
                return

            "No, collect resources instead":
                pass

            "Cancel":
                return

    if auto_extractors[resource + " ON"]: # When an extractor is ON
        menu:
            "You have an active resource extractor in this location. Do you want to turn if {b}OFF{/b}?"

            "Turn it OFF":
                play sound s_fiz
                $ auto_extractors[resource + " ON"] = False
                return

            "Just collect resources":
                pass

            "Cancel":
                return

    elif auto_extractors[resource]: # When an extractor is OFF
        menu:
            "You have an inactive resource extractor in this location. Do you want to turn if {b}ON{/b}?"

            "Turn it ON":
                play sound resource_dict[resource].sound
                $ auto_extractors[resource + " ON"] = True
                return

            "Just collect resources":
                pass

            "Cancel":
                return

    if MC.collect_resource(resource) == "KO":
        "You cannot trade leather more than once per day."
    return

label collect_dye():

    $ resource = "dye"

    if MC.get_items(name="采集者MkI型") and not auto_extractors[resource]: # When the player has an extractor in inventory and the location has none
        menu:
            "Do you want to set up a resource extractor in this location (cannot be undone)?"

            "Yes, set up a resource extractor Mk I in this location":
                play sound resource_dict[resource].sound
                $ MC.items.remove(MC.get_items(name="采集者MkI型")[0])
                $ resource_dict[resource].activate_extractor()
                return

            "No, collect resources instead":
                pass

            "Cancel":
                return

    if auto_extractors[resource + " ON"]: # When an extractor is ON
        menu:
            "You have an active resource extractor in this location. Do you want to turn if {b}OFF{/b}?"

            "Turn it OFF":
                play sound s_fiz
                $ auto_extractors[resource + " ON"] = False
                return

            "Just collect resources":
                pass

            "Cancel":
                return

    elif auto_extractors[resource]: # When an extractor is OFF
        menu:
            "You have an inactive resource extractor in this location. Do you want to turn if {b}ON{/b}?"

            "Turn it ON":
                play sound resource_dict[resource].sound
                $ auto_extractors[resource + " ON"] = True
                return

            "Just collect resources":
                pass

            "Cancel":
                return

    if MC.collect_resource(resource) == "KO":
        "You cannot brew dye more than once per day."
    return

label collect_marble():

    $ resource = "marble"

    if MC.get_items(name="采集者MkII型") and not auto_extractors[resource]: # When the player has an extractor in inventory and the location has none
        menu:
            "Do you want to set up a resource extractor in this location (cannot be undone)?"

            "Yes, set up a resource extractor Mk II in this location":
                play sound resource_dict[resource].sound
                $ MC.items.remove(MC.get_items(name="采集者MkII型")[0])
                $ resource_dict[resource].activate_extractor()
                return

            "No, collect resources instead":
                pass

            "Cancel":
                return

    if auto_extractors[resource + " ON"]: # When an extractor is ON
        menu:
            "You have an active resource extractor in this location. Do you want to turn if {b}OFF{/b}?"

            "Turn it OFF":
                play sound s_fiz
                $ auto_extractors[resource + " ON"] = False
                return

            "Just collect resources":
                pass

            "Cancel":
                return

    elif auto_extractors[resource]: # When an extractor is OFF
        menu:
            "You have an inactive resource extractor in this location. Do you want to turn if {b}ON{/b}?"

            "Turn it ON":
                play sound resource_dict[resource].sound
                $ auto_extractors[resource + " ON"] = True
                return

            "Just collect resources":
                pass

            "Cancel":
                return

    if MC.collect_resource(resource) == "KO":
        "You cannot mine marble more than once per day."
    return

label collect_ore():

    $ resource = "ore"

    if MC.get_items(name="采集者MkII型") and not auto_extractors[resource]: # When the player has an extractor in inventory and the location has none
        menu:
            "Do you want to set up a resource extractor in this location (cannot be undone)?"

            "Yes, set up a resource extractor Mk II in this location":
                play sound resource_dict[resource].sound
                $ MC.items.remove(MC.get_items(name="采集者MkII型")[0])
                $ resource_dict[resource].activate_extractor()
                return

            "No, collect resources instead":
                pass

            "Cancel":
                return

    if auto_extractors[resource + " ON"]: # When an extractor is ON
        menu:
            "You have an active resource extractor in this location. Do you want to turn if {b}OFF{/b}?"

            "Turn it OFF":
                play sound s_fiz
                $ auto_extractors[resource + " ON"] = False
                return

            "Just collect resources":
                pass

            "Cancel":
                return

    elif auto_extractors[resource]: # When an extractor is OFF
        menu:
            "You have an inactive resource extractor in this location. Do you want to turn if {b}ON{/b}?"

            "Turn it ON":
                play sound resource_dict[resource].sound
                $ auto_extractors[resource + " ON"] = True
                return

            "Just collect resources":
                pass

            "Cancel":
                return

    if MC.collect_resource(resource) == "KO":
        "You cannot negotiate ore more than once per day."
    return

label collect_silk():

    $ resource = "silk"

    if MC.get_items(name="采集者MkII型") and not auto_extractors[resource]: # When the player has an extractor in inventory and the location has none
        menu:
            "Do you want to set up a resource extractor in this location (cannot be undone)?"

            "Yes, set up a resource extractor Mk II in this location":
                play sound resource_dict[resource].sound
                $ MC.items.remove(MC.get_items(name="采集者MkII型")[0])
                $ resource_dict[resource].activate_extractor()
                return

            "No, collect resources instead":
                pass

            "Cancel":
                return

    if auto_extractors[resource + " ON"]: # When an extractor is ON
        menu:
            "You have an active resource extractor in this location. Do you want to turn if {b}OFF{/b}?"

            "Turn it OFF":
                play sound s_fiz
                $ auto_extractors[resource + " ON"] = False
                return

            "Just collect resources":
                pass

            "Cancel":
                return

    elif auto_extractors[resource]: # When an extractor is OFF
        menu:
            "You have an inactive resource extractor in this location. Do you want to turn if {b}ON{/b}?"

            "Turn it ON":
                play sound resource_dict[resource].sound
                $ auto_extractors[resource + " ON"] = True
                return

            "Just collect resources":
                pass

            "Cancel":
                return

    if MC.collect_resource(resource) == "KO":
        "You cannot weave silk more than once per day."
    return

label collect_diamond():
    if MC.collect_resource("diamond") == "KO":
        "You cannot look for diamonds more than once per day."
    return

label break_extractor(resource):

    play sound s_crash
    with vpunch
    "Your [resource] extractor has broken down."
    $ resource_dict[resource].deactivate_extractor()

    call receive_item(item_dict["席米亚科技废料"], msg="You were able to scavenge a piece of %s from the wreck.", use_article=False) from _call_receive_item_16

    return

label visit_exchange():

    # Before exchange is activated

    if not story_flags["resource exchange first visit"]:
        $ story_flags["resource exchange first visit"] = True

        call resource_exchange_intro() from _call_resource_exchange_intro

        return

    elif not story_flags["builder license"]:
        call exchange_come_back() from _call_exchange_come_back

        return

    # After exchange is activated

    if bast_letter in MC.items:
        call return_to_bast() from _call_return_to_bast
        return

    scene black
    show bg market at top
    with Fade(0.15, 0.3, 0.15)

    show bast with Dissolve(0.3)

    if story_flags["builder license"] < district.rank:
        call new_builder_license() from _call_new_builder_license
    else:
        bast "Welcome to the resource exchange. How may I help you?"

    if NPC_bast.love >= 30:
        menu:
            "Exchange resources":
                pass
            "Fool around":
                you "Hey Bast, do you want to have some fun?"

                "Bast looks around to make sure no one can hear you. She lowers her voice."

                bast "You mean... Like the last time?"

                you "Yes... I'm horny as hell..."

                if NPC_bast.flags["last fuck date"] >= calendar.time-2:
                    bast "You... You can't be serious... We only just did it!"

                    you "Aw... Okay."

                else:
                    "She bites her lip."

                    bast "Oh, [MC.name]... *blush*"

                    bast "*whisper* Follow me."

                    call bast_sex() from _call_bast_sex

                    $ MC.interactions -= 1
                    $ NPC_bast.flags["last fuck date"] = calendar.time

                    scene black
                    show bg market at top
                    with Fade(0.15, 0.3, 0.15)

                    show bast with Dissolve(0.3)

    show screen resource_exchange
    with Dissolve(0.3)

    while True:

        $ renpy.block_rollback() # Adding block_rollback everywhere to hopefully get rid of the double spend bug

        $ result = ui.interact()

        if result == "quit":
            hide screen resource_exchange
            return

        else:
            $ source, target, source_nb, target_nb = result

            if not MC.has_resource(source, source_nb):
                bast "You do not have [source_nb] [source] to buy this."

            elif renpy.call_screen("yes_no", "Are you sure you want to exchange [source_nb] [source] for [target_nb] [target]?"):
                $ x = 0 # this is for Bast events
                if source == "gold":
                    $ MC.gold -= source_nb
                else:
                    $ MC.resources[source] -= source_nb
                    $ x = source_nb
                $ renpy.block_rollback()

                if target == "gold":
                    play sound s_gold
                else:
                    play sound resource_dict[target].sound
                    if target_nb > x:
                        $ x = target_nb
                $ MC.gain_resource(target, target_nb, message=False)
                $ renpy.block_rollback()

                call trade_x_resources(x) from _call_trade_x_resources

                if _return:
                    return

    return

label wood_intro():

    with fade

    "Breathing in the fresh ocean breeze, and trying to ignore the smell of rotting fish, you take a walk around the shipyard."

    "Zan is a prime destination for trade from all over the known world, and its shipyard is always buzzing with activity from workmen, seamen, seagulls, moguls, bribe-givers, bribe-takers, bribe-agnostics, idlers and other riff-raff."

    "On one side of the harbor, new ships are being built on drydocks. On the other side, old ships are being refurbished or taken apart."

    "Because of its ever-growing population, Zan has stripped most of the surrounding country of its timber. Therefore, wood is a valuable commodity, so instead of letting it go to waste, some enterprising people dismantle old boats to make new ones."

    "You spend some time watching the workers as they go. It seems easy enough, although it takes some strength to rip away the rusty nails that hold the planks together."

    you "I think I've got the hang of it."

    scene black with fade

    "You may now collect {b}wood{/b} from the shipyard. Yield will depend on your {b}Strength{/b}."

    $ shipyard.action = True

    return

label dye_intro():

    with fade

    "As you take a walk down the beach, you notice it's more than just a place for swimmers."

    "Some industry also takes place alongside the leisure."

    "Dye-making is a particularly fascinating one. The women herbalists use simple spells to turn seaweed, seashells and other refuse from the ocean into bright dyes of every conceivable color."

    "You discuss the techniques with the eldest of the women, being particularly interested in how they make blue dye, a rarely occuring color in the natural world."

    you "I see... It's much easier than hunting a blue bear for its blood..."

    scene black with fade

    "You have learnt how to brew {b}dye{/b} from washed up material at the beach. Yield will depend on your {b}Spirit{/b}."

    $ beach.action = True

    return

label leather_intro():

    with fade

    "The stables are teeming with animals and people on any given day. Today, it's extra-crowded, given that a large party of foreign officials has just arrived in the city."

    you "Hey! Watch out!"

    "A careless noble and his steed nearly crushed you. You decide it's best to slip inside one of the buildings to let the crowd pass."

    you "Well, this is technically trespassing, but no one will mind if I just wait here a minute..."

    "A herd of cattle is already parked inside. The stink is almost unbearable, and you start looking for another way out."

    you "There's light that way... Maybe there's a store out front..."

    man "Arios be praised, you've come! You sure took your sweet time!" with vpunch

    "You are startled to hear someone call you, and turn around to see a diminutive old man with oversized spectacles, only to be whacked by his cane right on the shoulder."

    play sound s_punch

    with vpunch

    you "Ouch! Watch it, old man..."

    man "Don't you dare!"

    play sound s_punch

    with vpunch

    you "Aw!"

    "The geezer hits you again, and even though it's a weak strike, it still stings. For an instant, you wonder if you should fight back, but he's just a frail old man."

    man "Four hours I've been waiting! Four hours since I sent to the guild for help! While you were idling, no one was here to tend to the shop!"

    man "Stupid, unreliable guild officers... I told them there would be double payment today..."

    "He eyes you suspiciously through his nearly opaque glasses."

    man "Say, are you the same boy they usually send? You look tall for a 12-year old..."

    you "Look, pal, I... Wait, did you say 'double payment'?"

    man "Yeah, if you finally haul your ass to work! The shop is that way!"

    man "Man the store, dammit, I have to tend to the animals!"

    "The strange man shoves you out towards the store, before limping towards the animals who are waiting for food and drink."

    you "What have I got myself into..."

    play sound s_crowd_boos

    "The old man's store is full of grumbling people, waiting for someone to show up. They immediately gather around you, voicing their complaints and orders all at the same time."

    you "Not all at once, not all at once... You sir, what did you say you wanted again?"

    with fade

    stop sound fadeout 2.0

    you "Phew... It's finally finished..."

    "The old man is in charge of keeping animals safe for travellers who are set for a short stay in the city. Herding cattle around in the narrow streets of Zan is far from ideal."

    "The store job is pretty easy, as you only need to match the right owner with the right animals and update the logbook, but managing impatient customers requires some wit."

    man "There you are, kiddo! I hope nothing is amiss in the logbook, or I'll whip your teenage ass!"

    man "Well... Everything looks in order."

    you "(Can you even read anything in there?)"

    you "Now, about that payment you promised..."

    man "Ah, yes, the leather skins..."

    you "What??? The payment is in leather?"

    man "Why yes, of course... The payment is leather skins, as negotiated with the tanner's guild. But you knew that, of course?"

    you "O-Of course..."

    man "Well, I'm withholding your payment for today. That will teach you to show up late."

    you "Whaaat!!! That's unfair!" with vpunch

    man "But tell you what, kiddo, I like the way you handle the customers. Truly remarkable, for a boy your age."

    you "..."

    man "If you show up again to help with the shop, I'll pay you properly."


    scene black with fade

    "You can now earn {b}leather{/b} from helping at the stables. Yield will depend on your {b}Charisma{/b}."

    $ stables.action = True

    return

label marble_intro:


    with fade

    "The old ruins belonged to the non-human empire that first settled Zan's current location, Cimeria."

    "How it was built or what it was used for is unknown to all but the most reclusive scholars."

    "It's very easy to get lost in the maze of ruined structures, each very similar yet slightly different from the next."

    "Some people even claim the place changes over time, structures appearing and disappearing out of thin air... Those people are mad, of course."

    "One thing's for sure, though, the old ruins are a prime source for building materials."

    "Zan is always in need of new buildings, and the old ruins are so expansive that it never seems to run out of materials, no matter how many walls people dismantle."

    "The old palaces are especially reknowned for their Cimerian marble, a fancy stone that Zan's elite has a particular fondness for."

    "The only problem is, the ancient Cimerians knew how to build flawless architecture that stands the test of time, and Cimerian marble is extremely tough."

    "You watch a dozen men trying and failing to extract a block of marble from a weak-looking structure."

    "Only the strongest men can break their walls and extract that stone. Perhaps that's why the city still hasn't run out of Cimerian marble."

    "Not to mention there's a curse... Nah, forget about that."

    you "Anyway. Those guys are doing it all wrong. I bet I could recover some of those marble slabs if I did this..."

    scene black with fade

    "You have discovered how to extract {b}marble{/b} from the old ruins. Yield will depend on your {b}Strength{/b}."

    $ old_ruins.action = True

    return


label silk_intro():

    with fade

    "The hanging gardens are a wonderful place, tended by the magic guild's airmancers and extending high above Zan. The view is magnificent from here."

    "The trees are buzzing with magic energy and undulating strangely, connected to each other by complex networks of vines."

    "Creeping along those vines is a unique animal Zan is known all around Xeros for: the Zanic silkworm."

    "A silkworm is a fat, white worm that is typically a foot long, although the biggest can be the size of a large dog."

    "They are slow-paced, majestic animals. Silkworms are a delicacy for nobles around Zan, who like to eat a whole one roasted in butter for new year's eve, but very pricey."

    "That is because the silkworm's primary function makes them very valuable: patient enchanters can extract fine silk from the worm's body, using a process that takes a bit of magic skill, and is also pretty gross."

    you "Well, I could do that, I guess... The spell is not that difficult... But that elbow move is tricky. And do I really have to use my teeth for that?"

    scene black with fade

    "You have figured out how to weave {b}silk{/b} from the hanging gardens. Yield will depend on your {b}Spirit{/b}."

    $ hanging_gardens.action = True

    return

label ore_intro():

    with fade

    "The guild quarter hosts representatives from every possible trade in Zan, except for the Magic and Banking guilds that have their own separate quarter."

    "It is bustling with activity, traders of all kinds and origins negotiating all kinds of deals, large amounts of money changing hands at a dizzying speed."

    "The guild quarter is also where the mining activities are concentrated in Zan, as the guilds handle claims and stakes for the miners."

    "It is technically forbidden for miners to mine outside of their official claimed territory, but claim-jumping is still extremely common."

    "As you walk by one of the large mines, you hear someone whisper to you."

    man "Psst, Mister!"

    "Turning around, you notice a scrawny miner, taking a break near the protective fence that surrounds the ore mine."

    "Miner" "Sir, d'you have a minute? You're not a guildsman, right? No tattoos..."

    "Guildmembers wear complex tattoos indicating their trade and level. The miner's guild has especially spectacular tattoos, mining officials inking their face so it is black as coal. They are pretty easy to spot."

    you "No, I'm not."

    "You eye him suspiciously."

    you "Why? Are you in trouble with the guild?"

    "He spits."

    "Miner" "Shalia take 'em all! We work our asses off in the mine day and night, but at the end those bloody bureaucrats take a 70 percent cut just doin' nuthin'."

    you "That sucks. Can't you refuse their terms?"

    "Miner" "I wish... Some of the boys threatened to go on strike, so they had thugs beat 'em up and kick 'em out, only to replace 'em the next day."

    "Miner" "They say the next one to complain will go to the salt mines... Like a damn orc!"

    you "Well, seems like you've got no choice then..."

    "Miner" "Yeah, we're stuck here, we can't even go anywhere 'til we finish our weekly shift. It's like a fuckin' prison camp!"

    "Miner" "But me and the boys, we got an idea. See, a guy like you is free to come and go. We could make you a deal..."

    "He gives you a cunning look."

    you "Where are you going with this?"

    "Miner" "The guards here, they're extra lazy. They don't bother to check the perimeter outside of the main gate, ever."

    "Miner" "I could smuggle small amounts of ore through that hole in the fence, see? They'd be none the wiser."

    you "And give it to me? For what?"

    "Miner" "There are always some contacts at the black market that are looking to buy ore outside of the guild circuit. You'd need to haggle, we'd have to cut the price a bit... But it'd still be better than payin' the fuckin' guild tax, by a long shot."

    you "So I find some buyers and sell them your ore. What's in it for me? Do I get a share of the gold?"

    "Miner" "Nah, that wouldn't do. We need all the cash we can get up here. Booze and whores ain't cheap, ya know? And we need plenty of both to keep goin'."

    "Miner" "But listen. When you come back and give us our due, I'll give you some of the extra ore lying around for free. You can keep it or sell it, as you wish."

    you "I see... And how do you know I won't just sell your ore and steal your money?"

    "He chuckles."

    "Miner" "We've thought about that, of course... That's why I'm only ever going to give you small amounts of ore to sell, anyway."

    "Miner" "If you burn us, the deal is off, and you'd better never come back. Plus you might find yourself shanked in the back unexpectedly on a dark night..."

    "Miner" "But we could get a good workin' relationship. Whadaya say? Friends?"

    "He spits in his hand and holds it out for you to shake it. You look at his dirty paw with some disgust."

    you "I'll give it some thinking."

    "He smirks."

    "Miner" "Suit yerself, brother. Make up your mind quickly, though, before I offer the deal to someone else."

    scene black with fade

    "You have learnt how to help the miners smuggle {b}ore{/b} from the guild quarter. Yield will depend on your {b}Charisma{/b}."

    $ guild_quarter.action = True

    return

label diamond_intro():
    with fade

    play music m_water fadein 3.0

    "As you enjoy the sight of Zan's mighty waterfalls, you hear an eery noise that makes your hair stand."

    play sound s_mystery

    you "S-Spooky... Are there ghosts here?"

    "An old gentleman standing next to you notices your dismay, and addresses you with a friendly voice."

    "Old man" "Look alive, kid! This ain't no supernatural sound."

    you "It-It's not?"

    "Old man" "Hells no. It's just the wind running through the caves behind the waterfall."

    you "Caves, you say?"

    "Old man" "Oh, yes! There's a huge network of caves that starts there and runs through the whole mountain range. Some say it's many times bigger than Zan, and Zan is the largest city in the world!"

    you "Wow... Is it... Safe?"

    "The old man chuckles."

    "Old man" "Well, people get lost in there more often than not, and die alone in the darkness... Or not alone... But don't listen to those silly stories about the undead!"

    you "Un... Undead?"

    "Old man" "Yeah, ghouls, vampires, and worse... That's just rumors. It's just giant blood-sucking bats if you ask me."

    you "GIANT BLOOD-SUCKING BATS?"

    "Old man" "Oh, yes! Some are big as a pony!"

    you "Why would anyone ever go there!!!"

    "Old man" "Why, for the diamonds of course."

    you "Diamonds?"

    "Old man" "Yes... There are places in the caves where you can just pick them right up from the mud. Many adventurers try their luck there."

    you "How come the King or the nobles haven't got their hands on these diamonds first?"

    "Old man" "Oh, believe you me, they've tried! *chuckle* But it's no use sending an army in there, most passageways are only broad enough for a single man... And there are pockets with so little air to breathe, the large parties would just suffocate."

    "Old man" "So they are content to just buy their diamonds from careless adventurers like the rest of us sensible folks do."

    "Old man" "Not that I'd have the means to buy any, mind you... Say, young one, care to spare a denar?"

    you "*sigh*, here you go... Thanks for the information, though."

    scene black with fade

    $ MC.gold -= 50
    play sound s_gold

    "You paid the old man 50 gold. You have discovered that you can sometimes find {b}diamonds{/b} in the caves behind the waterfall."

    $ falls.action = True

    return



#### CHALLENGES ####

label challenge(name, diff, score=False, raw=False, bonus=0, opponent_bonus=0, _sound=True, score_limit=0, forced=False):

    $ diff = MC.challenges[name].adjust_diff(diff)

    $ result = MC.challenges[name].run(diff=diff, score=score, raw=raw, bonus=bonus, opponent_bonus=opponent_bonus, forced=forced)

    if MC.challenges[name].estimate_diff(diff=diff+score_limit, score=score, raw=raw, bonus=bonus, opponent_bonus=opponent_bonus, forced=forced) != "Safe":
        call screen challenge(name, diff+score_limit, raw=raw, bonus=bonus, opponent_bonus=opponent_bonus)

    $ define.move_transitions("easeol", 0.8, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp, layers=["myoverlay"])

    if (result and not score) or (result >= score_limit and score) or forced:
        if _sound:
            play sound s_success

        show success onlayer myoverlay with easeolinleft
        pause 0.5
        hide success onlayer myoverlay with easeoloutright

    else:
        if _sound:
            play sound s_crash

        show failure onlayer myoverlay with easeolinleft
        pause 0.5
        hide failure onlayer myoverlay with easeoloutright

    hide screen tool

    return result

label test_challenges():

    scene black
    $ renpy.show_screen("show_img", brothel.pic, _layer = "master")
    $ tt = show_tt("top_right")

    $ chal = renpy.call_screen("challenge_menu", challenges=[("Fight them", "fight", 5), ("Cast a spell", "cast", 5), ("Intimidate them", "bluff", 5)], cancel=("Run", False))

    if chal:
        call challenge(chal, diff=5) from _call_challenge_2

    else:
        "You ran away."

    hide screen show_img

    return


## SHOP RESTOCK INTRO

label shop_restock_intro():

    scene black with fade
    show bg shop at center with dissolve

    $ story_flags["shop restock"] = True

    shopgirl "Hello, handsome!"

    shopgirl "Say, I've noticed you come by often these days..."

    you "Well, yeah. I've got a business to run, and your items can be useful to me..."

    shopgirl "But I've noticed sometimes you come and leave empty-handed. That's just... *sad face*"

    you "Well, yeah, sometimes I just don't find what I want..."

    shopgirl "I see! Then, I have a solution for you. Hear me out. We could expand our... relationship."

    you "Business, or pleasure?"

    play sound s_laugh

    shopgirl "Business {i}is{/i} pleasure, darling... *giggle*"

    shopgirl "You see, if you cover parts of my expenses, I could {b}restock my inventory{/b} more regularly. It's costly of course, but useful, right?"

    shopgirl "I will only do it once a day, though. It's a lot of work..."

    you "Interesting. Go on."

    shopgirl "In addition, I am looking to {b}extend the shop counter{/b}, but I am missing some materials."

    shopgirl "If you provide me with the right resources, I could stock more items, increasing the choice for you!"

    you "That sounds good. What do you need?"

    shopgirl "Well, first, I'd need {b}5 pieces of wood{/b} to add a new shelf."

    you "Got it."

    "From now on, you can {b}restock{/b} any shop once a day for a hefty sum of gold."

    "You can also improve the main shop's {b}inventory size{/b} by spending resources."

    return



## RENZA/CAPTAIN SHOPS

label visit_thieves_guild:

    $ MC.interactions -=1

    scene black with fade
    show bg thieves_guild room at top with dissolve

    show renza at right with dissolve

    if NPC_renza.love >= 5 and dice(6) == 6:
        call renza_friend1 from _call_renza_friend1
        with fade
    elif game.chapter > 1 and NPC_renza.love >= 10 and not NPC_renza.flags["story1"]:
        $ NPC_renza.flags["story1"] = True
        call renza_friend2 from _call_renza_friend2
        with fade
    elif game.chapter > 1 and NPC_renza.love >= 15 and not NPC_renza.flags["story2"]:
        $ NPC_renza.flags["story2"] = True
        call renza_friend3 from _call_renza_friend3
        with fade
    elif NPC_renza.love >= 20 and not NPC_renza.flags["story3"]:
        $ NPC_renza.flags["story3"] = True
        $ calendar.set_alarm(calendar.time+1, Event(label = "renza_onsen1", order=-1))
    elif NPC_renza.love >= 30 and not NPC_renza.flags["story4"]:
        $ NPC_renza.flags["story4"] = True
        $ calendar.set_alarm(calendar.time+1, Event(label = "renza_onsen3", order=-1))

    renza "Oh, hi, [MC.name]. Come to check on my merchandise?"

    "You swallow hard as you take a good look at her juicy body."

    label thieves_guild_menu:

        menu:

            renza "Hey, it's rude to stare!"

            "Show me what you have":
                $ NPC_renza.love += 1
                jump thieves_guild_loop

            "What is it that you sell, again?":

                renza "I give you access to some of our merchandise. It's stuff that, err, fell off the back of a cart, so to speak."

                renza "As long as we understand each other and you keep your side of the deal, you can come here once a week. I'll have an item for sale, for a bargain price compared to regular item shops."

                renza "But you must understand and accept my rules"

                renza "You are never to tell anyone about me, or the location of this place. You mustn't brag about your connection to us,
                       or otherwise reveal it to anyone. The penalty for betrayal is... a dagger to the neck. Are we clear?"

                you "Yes."

                renza "Brilliant! Oh, and as long as we're dealing, you buy what's here at face value, and there is no refund.
                       I don't wanna hear any complaints, ok?"

                you "Fine."

                renza "Looking forward to doing business with you."

                renza "Oh, and don't forget... I am doing you a favour. I will expect it repaid some day."

                "You're not sure what she means by that."

                jump thieves_guild_menu

label thieves_guild_loop:

    if NPC_renza.items:

        $ owner = NPC_renza
        $ counterpart = MC

        show screen overlay("visit_location")
        show screen item_profile(NPC_renza.items[0])
        with dissolve


        while True:

            $ renza("这是本周的特价商品，是专为你准备的。", interact = False)

            $ result = ui.interact()

            if result[1] == "bargain":
                $ it = NPC_renza.items[0]
                $ price = it.get_price("bargain")

                if MC.has_gold(price):

                    $ result = renpy.call_screen("yes_no", "你确定要花[price]金币购买[it.name]吗？")

                    if result == True:
                        # $ MC.buy(NPC_renza, it, price)

                        hide screen item_profile

                        $ NPC_renza.love += 2
                        $ transact(it, NPC_renza, MC, price)
                        play sound s_gold

                        if dice(6) == 1:

                            "然而，当你从伦萨手中接过这件物品时，你立刻意识到它的质量非常糟糕。"

                            you "伦萨，这是什么..."

                            renza "货物售出概不退换!你知道规矩的。"

                            hide screen overlay
                            scene black with fade

                            if it.rank == it.min_rank:

                                "你被宰了。这东西一带回家就散架了。这是假货。"
                                $ MC.items.remove(it)
                            else:
                                $ it.transform(it.min_rank)
                                $ renpy.say("", "你被宰了。这不过是个" + article(it.name) + "。")

                            return

                        else:
                            renza "很高兴和你做买卖。"
                    else:
                        jump thieves_guild_loop

                else:
                    hide screen item_profile
                    you "该死，我现在没这么多钱..."
                    renza "兄弟，别浪费我的时间。"

                hide screen overlay
                scene black with fade
                return

            elif result == "leave":
                hide screen item_profile
                renza "哦，那真是太遗憾了，回见!"

                hide screen overlay
                scene black with fade
                return

    else:
        renza "本周我没有其他东西能卖给你了。你为什么不下周再来呢?货物到时候会从货车上掉下来的!"

        scene black with fade
        return


label visit_watchtower:

    $ MC.interactions -=1

    scene black with fade
    show bg captain_office at top with dissolve

    show captain at right with dissolve

    captain "嗨, [MC.name]! 你是来找我谈生意的，还是说想....找点乐子？"

    "她打招呼的同时，她那对漂亮的奶子在自然地跳动着。"

    "你试着集中注意力。"

    label watchtower_menu:

        menu:

            captain "它会是什么呢？"

            "让我看看你的货":

                jump watchtower_loop

            "我能从你这儿得到什么呢，又一次？":

                captain "为什么不呢，我的合作伙伴？*眨眼*"

                captain "这是我的金库，存放着我从贫民窟里不守规矩的苦工那里没收来的所有好东西。"

                captain "我会保留金子和闪闪发光的东西，但偶尔，一些不寻常的东西也会被没收。这个...对我没什么用。我可以给你一个优惠价。"

                captain "这就是我的最终定价了，要不要随你。一分钱一分货。"

                captain "另外，我每周只能允许你买一样东西，不能再多了。我不能让你整天在我的金库里进进出出。"

                jump watchtower_menu




label watchtower_loop:

    if NPC_captain.items:

        show bg vault at top with dissolve
        show screen item_profile(NPC_captain.items[0])
        show screen overlay("visit_location")
        with dissolve

        while True:

            $ captain("这是本周的特价商品，是专为你准备的。", interact = False)

            $ result = ui.interact()

            if result[1] == "bargain":
                $ it = NPC_captain.items[0]
                $ price = it.get_price("bargain")

                if MC.has_gold(price):

                    $ result = renpy.call_screen("yes_no", "你确定要花[price]金币购买[it.name]吗？")

                    if result == True:
                        $ MC.buy(NPC_captain, it, price)

                        play sound s_gold

                        hide screen item_profile

                        $ d = dice(6)

                        if d == 1:

                            "然而，当你从法拉手中接过这件物品时，你立刻意识到它的质量非常糟糕。"

                            you "法拉, 这是怎么一回事..."

                            captain "嘿，你自己弄坏的，真是可惜。你知道规矩的。"

                            hide screen overlay
                            scene black with fade

                            if it.rank == it.min_rank:

                                "你被宰了。这东西一带回家就散架了。这是假货。"
                                $ MC.items.remove(it)
                            else:
                                $ it.transform(it.min_rank)
                                $ renpy.say("", "你被宰了。这东西不过是个" + article(it.name) + "。")

                            return

                        elif d == 6:

                            "上尉数你的金币数的都要睡着了。"

                            captain "感谢惠顾..."

                            play sound s_laugh

                            "她用奇怪的眼神看着你。"

                            captain "[MC.name], 我可以给你展示它的另一种有趣的用法..."

                            "她把双手放在你的胸前，诱人地咬她的嘴唇。"

                            captain "为什么不去我的房间呢？"

                            menu:
                                "当然":
                                    call hide_everything() from _call_hide_everything_46

                                    show bg captain_office at top with dissolve
                                    $ pics = rand_choice([("captain sex1", "captain sex2"), ("bg captain sex3", "bg captain sex4")])

#                                    "pics are [pics]"

                                    play sound s_aah

                                    captain "Mmh... Let me relieve you of these useless clothes."

                                    hide captain with dissolve

                                    show expression pics[0] at top
                                    with fade

                                    play sound s_moans_short

                                    captain "That's it [MC.name]... Yes, go deeper..."

                                    captain "Oh... I'm... I'm cummmiiiing!!!"

                                    with flash

                                    play sound s_orgasm_fast

                                    show expression pics[1] at top
                                    with doubleflash

                                    captain "Oh, [MC.name] look at the mess you've made... All sticky and gross..."

                                    captain "I'll have to ask my maid to lick it all out..."

                                    play sound s_laugh

                                    $ MC.change_prestige(1)

                                "下次吧":
                                    you "对不起法拉,我得走了。"

                                    captain "哦，你是说...我想我得让我的一个奴隶帮你挠挠痒了..."

                        else:
                            captain "感谢惠顾。现在，你该离开了。"

                    else:
                        jump watchtower_loop

                else:
                    hide screen item_profile
                    you "该死，我没有那么多钱..."
                    captain "什么？没钱？没钱装什么大爷!!!"

                hide screen overlay
                scene black with fade
                return

            elif result == "leave":
                hide screen item_profile
                captain "好吧, 别再浪费我的时间了，滚吧。"

                hide screen overlay
                scene black with fade
                return

    else:
        captain "该死的[MC.name], 你把这当成菜市场一样每天想来就来想走就走？下周再来!"

        scene black with fade
        return



## FARM MERCHANTS AND EVENTS ##

# MERCHANTS

label visit_stella():
    call visit_merchant(NPC_stella) from _call_visit_merchant
    return

label visit_willow():
    call visit_merchant(NPC_willow) from _call_visit_merchant_1
    return

label visit_gina():

    if MC.get_items(name="席米亚"):
        scene black
        show expression selected_location.get_pic(config.screen_width, int(config.screen_height*0.8)) at top
        with fade
        show gina with dissolve

        gina "哦, [MC.name]。你帮我找到什么好东西了吗？"

        menu:
            "What would you like to do?"

            "买东西":
                pass

            "给她看你的发现":

                you "I think you were looking for Cimerian artefacts. I have found this. Can you tell me how much it's worth?"

                gina "Ooh, let me have a look! I hope it's good!"

                with fade

                gina "All right, this is what I'll pay for what you have."

                python:
                    ev_list = []

                    for it in MC.get_items(name="席米亚"):
                        if it.name == "席米亚科技废料":
                            price = 350
                            rv = 1
                        elif it.name == "席米亚科技产物":
                            price = 1500
                            rv = 5

                        ev_list.append((it, price, rv))

                while ev_list:

                    $ it, price, rv = ev_list.pop(0)

                    gina "I'll give you [price] gold for this [it.name]. Is that fair?"

                    menu:
                        extend ""

                        "接受":
                            play sound s_gold
                            gina "There you go."
                            $ MC.items.remove(it)
                            $ MC.gold += price

                        "送给她":
                            $ renpy.play(s_surprise, "sound")

                            gina "For me, really, for free? I... I don't know what to say... *blush*"

                            $ NPC_gina.love += rv
                            $ MC.items.remove(it)

                            if it.name == "席米亚科技产物":
                                gina "This is an amazing artefact... It must have cost you a fortune to get it... You really made my day. *blush*"

                        "拒绝":
                            you "No thanks."
                            $ rv = 0

                    if rv:
                        if not NPC_gina.flags["research"]:
                            $ NPC_gina.flags["research"] = rv
                            gina "Great! I can get started on some research right now. Who knows, I might even find something that would be useful to you... Then I can sell it back to you for a premium!"
                            you "Uh... Yay?"

                        else:
                            $ NPC_gina.flags["research"] += rv
                            gina "This will help with my research."

                if NPC_gina.flags["research"] >= 3 and not NPC_gina.flags["extractor1 unlock"]:
                    gina "I knew it! This fragment..."
                    you "What is it?"
                    gina "It's..."
                    gina "It's fucking useless!!!" with vpunch
                    you "Uh?"
                    gina "For flying! Useless! It's just a piece of some stupid machine..."
                    you "What machine?"
                    gina "The runes say something like... 'Resource extractor'. Whatever that means. That's just antique junk."
                    you "Let me have a look."
                    gina "It's in my inventory, you can buy it from me if you want. But I spent a lot of time researching this, so don't think I'll just give it away."
                    you "I thought you said it was junk..."
                    gina "{i}Antique{/i} junk!" with vpunch

                    $ NPC_gina.flags["extractor1 unlock"] = True
                    $ NPC_gina.items.append(extractor_items["extractor1"])

                elif NPC_gina.flags["research"] >= 8 and not (blueprint_item in MC.items or vitals_scanner in all_furniture):
                    gina "Wait a minute... I'm pretty sure I've seen a similar symbol somewhere..."
                    "Gina frantically rummages through her research papers."
                    gina "Here!" with vpunch
                    "She brandishes a strange schematics, glittering with strange runes and symbols."
                    you "Is this... Cimerian script? You understand it, right?"
                    gina "Of course I do! Unfortunately, this one is completely indecipherable. It was written by a Cimerian doctor."
                    you "Oh. I see."
                    gina "Judging from this symbol, it seems to be a medical station of sorts."
                    gina "At least the drawings seem to make some sense. Perhaps a resourceful craftsman could give it a try. The materials needed are common enough, apart from this energy core..."
                    you "And I suppose you're not giving it away for free?"
                    gina "What do you think! Ground-breaking research is a costly endeavor, you know!"
                    you "Speaking of 'ground-breaking', any more plans to fly off a cliff and crash down in the mud?"
                    gina "Why you... Grrr... *angry*"

                    call receive_item(blueprint_item, msg="You have acquired %s. Seek a skilled craftsman (or woman) to try and make sense of it.") from _call_receive_item_17

                elif NPC_gina.flags["research"] >= 15 and not NPC_gina.flags["extractor2 unlock"]:
                    gina "Wait, what do we have here? I think I know where this goes..."
                    you "Oh yeah? A new device?"
                    gina "I wish... But it's just one of those stupid extraction machines..."
                    gina "Except this one looks a lot more powerful. It uses two mana batteries..."
                    you "What does it do?"
                    play sound s_sigh
                    gina "*sigh* I don't know, and I don't care! This isn't getting us any closer to trans-continental flight!"
                    you "Trans-continental? How about you stick to gliding from a junk pile to another first?"
                    gina "Don't mock my scientific ambitions!!!" with vpunch
                    gina "Anyway. The device is in my inventory if you want to have a look. It's got lots of expensive parts, so expect to cough up a lot of gold for it."

                    $ NPC_gina.flags["extractor2 unlock"] = True
                    $ NPC_gina.items.append(extractor_items["extractor2"])

                else:
                    gina "Is this all?"

                    you "Yeah, that's all for now."

            "Never mind":
                return
    call visit_merchant(NPC_gina) from _call_visit_merchant_3
    return


label visit_goldie():

    scene black
    show expression selected_location.get_pic(config.screen_width, int(config.screen_height*0.8)) at top
    with fade
    show goldie with dissolve

#    if goldie.love >= 10:
#        jump goldie_dance

    menu:
        goldie "Oh, [MC.name]! It's so nice to see you. How may I help you?"

        "Buy something":
            call visit_merchant(NPC_goldie) from _call_visit_merchant_2
            return

        "Chat":
            label goldie_chat_menu():

                menu:
                    "How are things?":
                        you "How's business?"

                        goldie "Oh, business is good, thank you! Ever since you managed to lift that terrible curse, things have been looking up."

                        goldie "The animals are no longer afraid of the farm, and are no longer sick or afraid to reproduce."

                        goldie "They seem to be perpetually in heat, in fact. I have never seen them behave in such a way before..."

                        goldie "But I can't complain, because the ranch is flourishing! Soon I'll be able to hire more help, too."

                        jump goldie_chat_menu

                    "Can I come in?":

                        if MC.interactions <= 0:
                            "You do not have any actions left for today."
                            jump goldie_chat_menu

                        you "Hey, Goldie. Got a minute?"

                        goldie "Oh, [MC.name]... What can you possibly have in mind?"


                        menu:
                            "What do you want to do? (costs 1 AP)"
                            "Strip for me":
                                play sound s_mmmh
                                goldie "With pleasure..."
                                call goldie_strip from _call_goldie_strip_1

                            "Give me a titjob":
                                play sound s_laugh
                                goldie "Oh, you naughty boy..."
                                call goldie_titjob from _call_goldie_titjob_1


                            "Let's have sex":

                                if NPC_goldie.flags["fucked_" + str(calendar.time)]:
                                    goldie "Sorry, [MC.name], I'm spent... We can have some fun another day."
                                    jump goldie_chat_menu

                                play sound s_aaah
                                goldie "I thought you'd never ask..."
                                call goldie_sex from _call_goldie_sex_1
                                $ NPC_goldie.flags["fucked_" + str(calendar.time)] = True

                            "Never mind":
                                jump goldie_chat_menu

                        $ MC.interactions -= 1
                        scene bg farmland with fade
                        show goldie with dissolve
                        jump goldie_chat_menu

                    "Never mind":
                        jump visit_goldie

        "Never mind":
            return

    jump visit_goldie


# AUTOREST EVENTS

label add_vitals_scanner():

    scene black with fade
    show bg wagon at top with dissolve

    show carpenter with dissolve

    carpenter "Oh, heya boss."

    you "Hi, Iulia. I was wondering if you might take a look at this for me."

    "You hand Iulia the mysterious blueprint."

    carpenter "What's this? I ain't ever seen anythin' like it."

    you "I got it from Gina, the mad scientist from the junkyard. It's from an ancient civilization, or some such nonsense. What I want to know is if it's valuable..."

    carpenter "Well, only one way to find out. This would take quite a few resources..."

    you "But you could build it?"

    carpenter "Well... I guess I could give it a try. I think I understand the structure. And this layered seal around the hatch... Could be tricky, but I've seen it done before."

    you "Perfect."

    carpenter "There's a catch, though."

    you "Hm?"

    carpenter "See this glowing thingy right in the center of the design? Seems like an energy source."

    you "And?"

    carpenter "You'd have to procure it somehow. Perhaps your 'scientist' girlfriend could find one for you."

    "There is a hint of annoyance in her voice. Where is that coming from?"

    you "I'll make sure to ask her. But first, let's build this."

    carpenter "Sure thing, just order it when you're ready."

    scene black with fade

    $ MC.items.remove(blueprint_item)
    $ all_furniture.append(vitals_scanner)

    "You gave Iulia the ancient blueprint. You can now build a {b}Strange machine{/b} from the wagon menu."

    return

label vital_scanners_built():

    scene black with fade
    show bg wagon at top with dissolve

    show carpenter attack with dissolve

    play sound s_clash
    with vpunch

    carpenter "HA!"

    hide carpenter
    show carpenter
    with dissolve

    carpenter "Looky here, boss! I done built your strange machine."

    "The machine looks very similar to the picture you saw on the ancient blueprint. However, it stands lifeless, its many knobs and quadrants unresponsive."

    carpenter "It needs an energy source."

    gina "Of course it does! As luck would have it, I've got one right here."

    show carpenter at left with move
    show gina at right with dissolve

    you "Gina?"

    gina "Yeah, I've heard you were working on the Cimerian scanner, so I got curious."

    carpenter "So she's the nerdy girlfriend you were talking about... She looks the part, I reckon."

    play sound s_surprise

    gina "Who's that, [MC.name]? From her vulgar clothing, I would assume one of your whores, but what's with the hammer?"

    carpenter "Whaa!?!" with vpunch

    play sound s_sheath

    show carpenter attack with dissolve

    carpenter attack "You bitch! The hammer's gonna crush your whiny little..."

    you "Whoah, whoah, ladies... Let's focus, shall we?"

    show carpenter normal with dissolve

    carpenter "Grrr..."

    you "Gina, have you got something for us?"

    gina "Well, uh, I brought this energy core. Let's give it a try."

    play sound s_creak

    "Gina opens up a small hatch and plugs the energy core inside the strange contraption. The machine lights up, and starts humming like a beehive."

    play sound s_vibro
    with flash

    you "It's working! Thank you. That's nice of..."

    gina "It doesn't come for free, of course!"

    you "Duh."

    gina "I am here to enlist your help. For science."

    you "Err... My help?"

    gina "Well, not exactly. I want to test this machine on your girls. It seems to be tuned for female organs..."

    you "Organs? Wait a minute... What is this machine for? Is it dangerous?!?"

    gina "Of course not, dummy! It's some sort of medical apparatus. It measures vital signs."

    gina "But it needs to be calibrated. That's why we need some, err, volunteers..."

    you "All right then. Why don't you do it? You're female."

    gina "No way! It's too dan... I mean, I'll be too busy calibrating it!"

    gina "You, hammer-waving maniac. Get in here."

    carpenter "No way! I ain't gettin' paid to play guinea pig for your crazy-ass girlfriend."

    hide carpenter with dissolve
    show gina at center with move

    gina "My, such impertinence... Why do you put up with this fool?"

    you "*sigh*"

    you "Anyway. Sill, gather the girls here."

    if len(MC.girls) > 1:
        $ girl1, girl2 = rand_choice(MC.girls, 2)
    elif len(MC.girls) == 1:
        $ girl1 = girl2 = MC.girls[0]
    else:
        you "Ahem, I don't have any girls at the brothel right now..."

        gina "What?!? What kind of brothel owner are you!"

        you "I'll, uh... I'll just pick two random girls up from the street, how does that sound?"

        gina "Awful. But none of my concern, I guess. Quick, get me some testers!"

        $ girl1, girl2 = rand_choice(game.free_girls, 2)

    with fade

    gina "You, step forward and get in there."

    girl1.char "R-Really? Master, should I go in?"

    you "Well, sure, it's, uh, safe..."

    you "I mean it is, right, Gina?"

    gina "Of course, of course! Now get in there, and..."

    play sound s_lightning
    with flash

    pause 0.3

    play sound s_woman_scream
    with vpunch

    girl1.char "EEEEK!!!"

    "A big burst of energy runs through the machine, sending an electric shock through [girl1.name]'s body. She is hurt."

    $ girl1.get_hurt(2)

    gina "Oopsie."

    you "What the hell was that!"

    gina "I'm pretty sure I shouldn't have pressed that button. Or was it this knob?"

    you "[girl1.name] was hurt by your hellish contraption!"

    gina "Come on, it's just a minor setback in the grand scheme of things. Send in the next one."

    you "Why... No!"

    gina "It's fine this time, really. I got this."

    you "I said no!"

    gina "If we stop now, this machine will remain a useless piece of scrap. Is this what you want?"

    you "I... No..."

    gina "So, show some balls, and send someone else into harm's way."

    gina "Neeeext!"

    girl2.char "Wait, I'm scared, I..."

    gina "In you go!"

    "Gina shoves [girl2.name] inside the machine, slamming the hatch shut. She fiddles with knobs, before pulling a big lever."

    gina "And..."

    play sound s_fire
    with vpunch

    girl2.char "*cough* *cough*"

    gina "I... That wasn't supposed to happen."

    play sound s_surprise

    "[girl2.name] steps out of the machine, before crumbling on the floor, winded. She has become exhausted."

    $ girl2.change_energy(-1000)

    gina "Interesting... This seems to measure her vitality level... There was a feedback effect, though..."

    you "What the fuck, Gina!"

    gina "We're almost there, [MC.name]! Just a few more tests, and..."

    you "Damn..."

    with fade

    "Gina tries her machine on all your girls, completely messing up their energy levels."

    python:
        for girl in MC.girls:
            girl.energy = round_int(dice(6) * girl.energy / 4.0)

    gina "Tadaa!!!" with vpunch

    gina "It's working! The machine is calibrated!"

    "Your girls lie scattered around the machine in various states of undress, passed out or panting."

    you "You... I really hope this is worth it!"

    gina "Oh, ye of little faith! Let me show you."

    play sound s_spell

    gina "This knob lets you set up a value... And this part activates the scanner..."

    gina "With this, you can automatically check your girls' energy level every night. If you set this right, there is no longer a risk they will work until exhaustion if they are too tired."

    "You can now use the {b}autorest{/b} option from the {b}schedule screen{/b}."

    $ vitals_scanner.description += " Allows autorest to be set up from the Schedule screen."

    return

label visit_riche():
    call visit_merchant(NPC_riche) from _call_visit_merchant_4
    return

label visit_ramias():
    call visit_merchant(NPC_ramias) from _call_visit_merchant_5
    return

label visit_gurigura():
    call visit_merchant(NPC_gurigura) from _call_visit_merchant_6
    return

label visit_katryn():
    call visit_merchant(NPC_katryn) from _call_visit_merchant_7
    return

label visit_giftgirl():
    call visit_merchant(NPC_giftgirl) from _call_visit_merchant_8
    return

label visit_twins():
    call visit_merchant(NPC_twins) from _call_visit_merchant_9
    return


## FARM EVENTS

label send_to_farm(girl, duration=None, can_beg=True, can_cancel=True):

    $ girl2 = None

    ## Check entry conditions ##

    if girl.farm_lock:
        "You have promised [girl.name] not to send her to the farm. You cannot send her again today."

        $ sent_success = False

        return

    if not farm.has_room():
        if farm.get_pen_limit() > farm.pens:
            "There are no free pens in the farm right now."

            $ price = farm.get_pen_cost()

            gizel "Would you like to add a new pen to the farm for [price] gold?"

            $ sent_success, text1 = farm.add_pen()

            if sent_success:
                gizel happy "[text1]"
            else:
                if text1:
                    gizel upset "[text1]"
                return

        else:
            gizel "There are no free pens in the farm right now. You cannot add any more pens to the farm for the time being."

            menu:
                gizel "Would you like to swap [girl.fullname] with another girl currently in the farm?"

                "Yes":
                    $ menu_list = [(g.fullname, g) for g in farm.girls] + [("Cancel", False)]
                    $ girl2 = long_menu("Choose a girl from the farm", menu_list)

                    if girl2:
                        call farm_take_out(girl2, check_room=False, context="check") from _call_farm_take_out_1
                        if _return: # Checks if girl2 can be taken out
                            $ sent_success = True
                        else:
                            $ sent_success = False
                            return

                    else:
                        $ sent_success = False
                        return

                "No":
                    $ sent_success = False
                    return


    if duration:
        $ prog = FarmProgram(girl, fixed_duration=duration)
    else:
        $ prog = FarmProgram(girl)

label send_to_farm_menu():

    call screen farm_menu(prog, can_cancel)

    if _return == "back":
        return

    elif _return == "commit":
        $ prog.update()
    else:
        jump send_to_farm_menu

    ## Check girl begging and resisting ##

    $ forced = False

    # Girl dialogue

    if girl not in farm.girls:

        if girl.is_("very dom"):
            $ base_target = 70
        elif girl.is_("dom"):
            $ base_target = 50
        elif girl.is_("very sub"): # For text flavor, sub girls will not rebel
            $ base_target = 15
        elif girl.is_("sub"):
            $ base_target = 30

        if can_beg and girl.farm_beg_test():

            "[girl.name] breaks down and cries."

            play sound s_scream

            $ girl.say("refuse farm")

            menu:
                "What do you do?"

                "Ignore her":
                    you "I'm the one in charge here. Get yourself ready. Gizel will pick you up shortly."

                    play sound s_screams

                    girl.char "No, Master, noooo!!!"

                    $ MC.good -= 1
                    $ girl.change_love(-3)
                    $ girl.change_fear(3)

                    "[girl.fullname] now fears you more."

                    $ forced = True

                "Spare her":
                    you "Aw, come on, wipe your tears... I won't make you go... This time."

                    play sound s_surprise

                    girl.char "Oh, Master! Thank you, thank you!"

                    $ MC.evil -= 1

                    $ girl.change_fear(-2)
                    $ girl.change_stat("obedience", -1*dice(5))
                    $ girl.farm_lock = True

                    "[girl.fullname] now fears you less. She has become less obedient."

                    $ sent_success = False

                    return

        elif prog.target != "no training" and girl.get_stat("obedience") <= base_target*girl.rank: # May resist sex training
            if girl.is_(["very sub", "lewd"]) or girl.get_stat("libido") >= 40*girl.rank:
                $ girl.say("accept farm")
            elif girl.get_fear() + girl.get_stat("obedience") > base_target*girl.rank:
                $ girl.say("accept farm fear")
            else:
                play sound s_surprise
                $ girl.say("refuse farm")

                menu:
                    "[girl.fullname] is resisting. What do you do?"

                    "Force her":
                        you "You are going, and that's final!"
                        $ forced = True

                    "Send her to rest instead" if not can_cancel:
                        you "Fine, you'll just stay in your pen then."
                        $ prog.target = "no training"
                        $ prog.holding = "rest"
                        $ prog.installation = None

                    "Let her go with a warning" if can_cancel:
                        you "Humph. I'll let you off the hook this time... But don't test my patience!"

                        gizel upset "Why are you showing weakness! You are being ridiculous! *angry*"

                        $ girl.farm_lock = True
                        $ sent_success = False

                        return

                    "Give up" if can_cancel:
                        you "Okay, okay, no need to yell... Gee, slaves these days..."

                        gizel angry "Get a grip, you wimp!!! *mad*"

                        $ girl.farm_lock = True
                        $ sent_success = False

                        return
        else:
            $ girl.say("accept farm")

        # May resist MC

        $ renpy.block_rollback()

        if forced:
            call fight_attempt(girl, 3) from _call_fight_attempt_19

            if fight_happens:
                if _return:
                    "Gizel didn't lift a finger to help you."
                    play sound s_evil_laugh
                    gizel smirk "Fufufufu... You weakling... She got you good!"

                    $ sent_success = False

                    hide screen dark_filter
                    hide screen girl_stats
                    hide screen girl_profile
                    hide screen button_overlay
                    return
                else:
                    "Gizel watched the fight with amusement. She grabs [girl.fullname] by the hair."

        # $ pick_dialogue("gizel take girl to farm").say(gizel)

        if dice(6) >= 4:
            play sound s_moo
        else:
            play sound s_rooster

        $ farm.send_girl(girl, prog)

        if girl2:
            call farm_take_out(girl2, check_room=False, context="swap") from _call_farm_take_out_2
            "[girl.fullname] has been taken away to the farm, while [girl2.fullname] has been sent to [brothel.name]."

        $ farm.change_program(girl, prog)

        menu:
            "Follow her to the farm":
                $ selected_destination = "farm"
                jump teleport

            "Stay here":
                pass

    $ sent_success = True

    hide screen dark_filter
    hide screen girl_stats
    hide screen girl_profile
    hide screen button_overlay
    # with Fade(0.05, 0.1, 0.05)

    return

#         "No sexual training (hold her)":
#             $ prog.target = "no training"

label farm_max_skill(girl, skill):

    scene black with fade

    if brothel.get_common_rooms():
        $ room = brothel.get_random_room_pic_path()
    else:
        $ room = "black"

    $ cntext = girl_related_dict[skill]
    gizel normal "I have trained [girl.fullname]'s {b}[skill]{/b} skill to her current maximum."

    if girl in farm.girls and farm.programs[girl].act == act: # Will not ask if program was changed

        $ cntext = girl_related_dict[skill]
        menu:
            gizel "Would you like to change [girl.fullname]'s training?"

            "Change it":
                call farm_change_program(girl) from _call_farm_change_program_1

            "Keep training [skill]":
                gizel "Fine. Visit the farm if you want to change it later."

    return

label farm_max_pref(girl, act):

    scene black with fade

    if brothel.get_common_rooms():
        $ room = brothel.get_random_room_pic_path()
    else:
        $ room = "black"

    $ cntext = girl_related_dict[act]
    gizel normal "[girl.fullname] is now fascinated with {b}[act]{/b}. I can still train her a bit more, though... It would still increase her market value."

    if girl in farm.girls and farm.programs[girl].act == act: # Will not ask if program was changed

        $ cntext = girl_related_dict[act]
        menu:
            gizel "Would you like to change [girl.fullname]'s training?"

            "Change it":
                call farm_change_program(girl) from _call_farm_change_program_2

            "Keep training [act]":
                gizel "Fine. Visit the farm if you want to change it later."

    return

label farm_discovered_weakness(girl):
    $ prog = farm.programs[girl]

    scene black with fade

    if brothel.get_common_rooms():
        $ room = brothel.get_random_room_pic_path()
    else:
        $ room = "black"

    play sound s_crash

    show expression room at top

    show gizel normal
    with dissolve

    gizel "[MC.name]!" with vpunch

    you "This door is fragile, you know..."

    gizel "Good news! I have found {b}[girl.fullname]{/b}'s weakness! She is afraid of [girl.weakness]s! I can use this to train her faster. I can already imagine how much she'll squeal and squirm..."

    if girl in farm.girls:

        menu:
            "Yes, do that":
                $ prog.installation = farm_installations[farm_installations_dict[girl.weakness]] # farm_installations_dict[girl.weakness]
                $ prog.update()
                $ prog.avoid_weakness = False

                you "Good idea. Now, shouldn't you be busy training?"

                gizel upset "Hey! Don't you give me orders! Now, I'll go back to training... {i}Out of my own free will!{/i}"
                play sound s_close

            "No, spare her":
                $ prog.avoid_weakness = True
                you "I don't want you to do that, it will distress her. Keep her away from [girl.weakness]s."

                gizel angry "What!! Is this how you thank me for all my efforts?"
                play sound s_crash
                with vpunch

                you "Aw, now I think she actually broke the door..."

    hide gizel with dissolve
    return

label farm_resisted(girl, context):

    $ prog = farm.programs[girl]

    if prog.notification:
        return

    $ prog.notification = True

    if girl not in farm.girls: # May happen if she became broken
        return

    scene black with fade

    if brothel.get_common_rooms():
        $ room = brothel.get_random_room_pic_path()
    else:
        $ room = "black"

    play sound s_crash

    show expression room at top

    show gizel angry
    with dissolve

    "Gizel barges in early in the morning, slamming the door of your office open." with vpunch

    if context.startswith("rebel"):
        gizel angry "{b}[girl.fullname]{/b}! That slut! That little ungrateful bitch!{nw}"

        if context.endswith("runaway"):
            extend " She bailed on me!!! I'm going to pluck out her eyeballs and skullfuck her!"
            call run_away(girl) from _call_run_away_3
            gizel "When you find her, do me a favor, and rape that whore's ass with a tent pole!"
            you "Giz, calm down..."
            hide gizel with dissolve
            return

        elif context.endswith("minion hurt"):
            extend " She hurt my beautiful minion! I should flay her disgraceful skin and make a handbag!!!"

        elif context.endswith("girl hurt"):
            extend " She tried to attack me with her... her... fingernails! I could have been seriously scratched!"

        elif context.endswith("subdued"):
            extend " She refused my direct orders! I had to beat some sense into her thick head!"

    elif context == "refused":
        gizel upset "Look, {b}[girl.fullname]{/b} is a whiny little bitch, and refuses to train! You need to let me enforce harsher discipline with her..."

    elif context == "resisted":
        gizel upset "{b}[girl.fullname]{/b} has the nerve to complain about my training... I'll kick her silly ass to Westmarch and back!"


    if girl in farm.girls:
        menu:
            gizel "What are you gonna do about it?"

            "Review her training":
                call farm_change_program(girl) from _call_farm_change_program_3

            "Change training mode (gentle)" if prog.mode != "gentle":
                $ prog.mode = "gentle"
                gizel upset "What! You weakling! I should turn you into a toad and squash you with a deathroller!" with vpunch

                you "Gizel, we have a deal... Do as I say."

                gizel angry "*grumble* *grumble*"

            "Change training mode (tough)" if prog.mode != "tough":
                if prog.mode == "gentle":
                    gizel upset "It's time you got serious with that slut. We'll see how it goes."
                elif prog.mode == "hardcore":
                    gizel angry "No! Why are you giving up like a wimp! You know she needs discipline!"
                    you "That's my decision. Now, If you don't mind..."
                    gizel upset "*grumble*"
                $ prog.mode = "tough"

            "Change training mode (hardcore)" if prog.mode != "hardcore":
                $ prog.mode = "hardcore"
                gizel smirk "Yes! That's the spirit! I won't stop until her every hole is sore and she cries herself to sleep!"

                you "Yeah, but make sure you keep her intact, okay? I've got plans for her."

                gizel normal "Yes, don't worry. I have a reviving spell somewhere if things go too far."

                you "..."

            "Keep her current training mode ([prog.mode])":
                you "Just keep doing what you've been doing, and keep me out of it. Very well, now, shoo!"

                gizel upset "Err, what?"

                you "Nice seeing ya! Goodbye now!"

                play sound s_close

    hide gizel with dissolve
    return


label farm_change_program(girl):

#    gizel normal "Do you want to make changes to [girl.fullname]'s training program?"

    $ prog = farm.programs[girl]
    $ can_cancel = True

    call send_to_farm_menu() from _call_send_to_farm_menu

    hide screen dark_filter

    return

label farm_change_training_mode(girl):

    $ prog = farm.programs[girl]
    $ not_avoid = not prog.avoid_weakness

    menu:
        "Change current training mode ([prog.mode])":
            menu:
                "Change current training mode ([prog.mode])"

                "Gentle":
                    $ prog.mode = "gentle"
                    "In soft mode, she won't be forced to do something she doesn't want to."
                "Tough":
                    $ prog.mode = "tough"
                    "In hard mode, Gizel will overcome moderate resistance on her part."
                "Hardcore":
                    $ prog.mode = "hardcore"
                    "In this mode, Gizel will ignore all red lines and force her to do anything."

        "Use her weakness for [girl.weakness]s ([not_avoid])" if farm.knows["weakness"][girl]:
            menu:
                "Use her weakness for [girl.weakness]s ([not_avoid])"

                "Use it":
                    $ prog.avoid_weakness = False
                    $ prog.installation = farm_installations[farm_installations_dict[girl.weakness]]
                    $ prog.update()

                    "[girl.name] has been sent to the [prog.installation.name]."

                "Spare her":
                    $ prog.avoid_weakness = True
                    "You don't want to cause her too much distress. Gizel will separate [girl.name] from [girl.weakness]s whenever possible."
        "Cancel":
            pass

    return

label farm_take_out(girl, check_room=True, context="normal"): # Context can be 'normal', 'check' or 'swap'

    $ prog = farm.programs[girl]

    if girl in farm.girls:
        if prog.duration > 1 and prog.fixed_duration:
            gizel smirk "You can't take [girl.fullname] out of the farm for now. She is to be disciplined for another [prog.duration] days, remember?"

        elif prog.duration > 0 and prog.fixed_duration:
            gizel smirk "You can't take [girl.fullname] out of the farm for now. She is to be disciplined for 1 more day, remember?"

        elif check_room and len(MC.girls) >= brothel.bedrooms:
            gizel normal "And just where do you think you can put that wench? Your brothel is full."

        elif context == "check":
            return True

        elif context == "swap" or (context == "normal" and renpy.call_screen("yes_no", "Do you want to send [girl.fullname] back to the brothel?")):
            hide screen girl_stats
            hide screen girl_profile
            hide screen button_overlay
            $ farm.remove_girl(girl)
            $ girl_status_dict = load_girl_status(MC.girls + farm.girls)

            return True

    else:
        $ raise AssertionError(girl.fullname + " is not a farm girl.")

    return False

label exit_farm(girl, reason):

    $ prog = farm.programs[girl]


    show bg farm at top with fade
    show gizel at center with dissolve

    if len(MC.girls) >= brothel.bedrooms:
        gizel normal "I was going to return [girl.fullname] to you, but I see that you have no room for her."

        gizel smirk "Never mind, I'll keep her as my plaything for a bit longer! Come get her at the farm when you want her back."

        $ prog.duration = -1
        $ prog.fixed_duration = False

    elif reason == "time up":
        gizel normal "[MC.name]! [girl.fullname] has served her time at the farm. Would you like me to bring her back?"

        menu:
            gizel "[MC.name]! [girl.fullname] has served her time at the farm. Would you like me to bring her back?"

            "Sure":
                $ selected_girl = None
                $ farm.remove_girl(girl)

                if girl.job:
                    "[girl.fullname] is back to work at the brothel as a [girl.job]."
                else:
                    "[girl.fullname] is back at the brothel and is resting."

            "No, you keep her":
                $ prog.duration = -1
                $ prog.fixed_duration = False

                gizel "Fine. You can find her at the farm when you need her."

    elif reason == "condition met":
        if prog.target != "auto":
            if compare_preference(girl, prog.target, prog.condition):
                $ prep = {"indifferent" : " to", "interested" : " by", "fascinated" : " with"}[prog.condition]
                $ resist = False
                gizel "[MC.name], I brought you [girl.fullname] back. You asked me to train her until she was [prog.condition][prep] [prog.target] acts, well, there she is."
            else:
                $ resist = True
                gizel "[MC.name], I can't train [girl.fullname] for [prog.target] acts, she won't train anymore. Perhaps if you allowed me to go {i}really{/i} hard on her..."
        else:
            python:
                for act in extended_sex_acts:
                    if not girl.will_do_farm_act(act, prog.mode):
                        resist = True
                        renpy.say(gizel, MC.name + ", I have trained " + girl.fullname + " as far as I could, but there are things she refuses to do. Perhaps if you allowed me to go {i}really{/i} hard on her...")
                        break
                else:
                    prep = {"indifferent" : " to", "interested" : " by", "fascinated" : " with"}[prog.condition]
                    resist = False
                    renpy.say(gizel, MC.name + ", I brought you "+ girl.fullname + " back. You asked me to train her until she was " + prog.condition + prep + " with all sex acts, well, there she is.")

        menu:
            gizel "Would you like to have her back?"

            "Sure":
                $ selected_girl = None
                $ farm.remove_girl(girl)

                if girl.job:
                    "[girl.fullname] is back to work at the brothel as a [girl.job]."
                else:
                    "[girl.fullname] is back at the brothel and is resting."

            "No, keep her":
                $ prog.condition = "none"
                $ prog.fixed_duration = False
                gizel "Fine. You can find her at the farm when you need her."

            "No, keep her and change her training to 'tough'" if resist and prog.mode == "gentle":
                $ prog.mode = "tough"
                $ prog.fixed_duration = False
                gizel smirk "Finally, you see reason! I'll do that."

            "No, keep her and change her training to 'hardcore'" if resist and prog.mode != "hardcore":
                $ prog.mode = "hardcore"
                $ prog.fixed_duration = False
                gizel "Delightful... I'm gonna have a lot of FUN with this bitch!"

    return


## ADVERTISING INTRO

label advertising_intro():

    if brothel.advertising > 0:

        scene black with fade
        show expression bg_bro at top
        with dissolve

        sill happy "Master, you have used advertising girls for the first time! Would you like to know more about how advertising works?"

        menu:
            extend ""

            "Okay, sure":
                call help_advertising() from _call_help_advertising

                sill "One more thing, Master, if I may. Right now, your advertising girls are only wearing plain clothes. This is not very attractive to customers, I'm afraid..."

                sill "But don't worry! Here, I have sewn together some matching outfits for them to wear."

                you "I see... They look... homey?"

                sill sad "Aw... (Is this all you've got to say...)"

            "Nah, I'm fine":
                sill "Okay then. Ask me later if you need a refresher."

        call screen OK_screen("基础着装", "你从希露那里得到了供宣传人员换装用的 {b}基础着装{/b} 。 这是用 '%s' 剩下的布料缝制的凡品，但总比没有好。" % brothel.name, pic=Picture(path="items/furniture/Basic outfit.webp"))

        "你得到了一套宣传人员可以替换的衣服, 这增加了青楼的 {b}advertising power{/b} 。以后肯定还有办法弄到更加吸引人的装束。"

        $ story_remove_event("advertising_intro", "daily")

    return


## LEVEL UP INTRO

label zodiac_intro():

    # Tests if a girl has leveled

#    "zodiac check"

    python:
        leveled = None

        for girl in MC.girls:
            if girl.level >= 2:
                leveled = girl
                break

    if not leveled:
        return

    with vpunch

    sill happy "Master!"

    sill "Wait! Master [MC.name]!"

    you "Oh, Sill... What is it this time?"

    sill sad "Err, I'm sorry to bother you, Master... It's just..."

    you "Spit it out."

    sill "I read this thing in the Hooker Gazette, and..."

    sill happy "It's about the Eight legendary Zodiac saints! Would you like me to tell you about it?"

    menu:
        sill "It's about the Eight legendary Zodiac saints! Would you like me to tell you about it?"

        "Go on":
            you "Fine... Go on."

            sill "Oh, wonderful! Listen to this..."

            scene black with fade
            show bg zodiac at top with dissolve

            call help_zodiac() from _call_help_zodiac_1

            hide bg zodiac with dissolve

            sill "I think [leveled.fullname] is a little more experienced now. Maybe she's ready to learn a new zodiac sign, expand her cosmic mindset, open her chakras, you know?"

            you "Sill... You sound weird..."

            you "Tell me the truth. Are you on spice?"

            play sound s_surprise

            sill sad "What? No!!!" with vpunch

        "Nope":
            you "Yeah, but no thanks."

            sill sad "Oh. I see..."

    with fade

    $ daily_events.remove(event_dict["zodiac_intro"])

    return




## MAGIC BILLBOARD EVENTS

label add_billboard():

    scene black with fade
    show bg wagon at top with dissolve

    show carpenter at left with dissolve

    carpenter "Here you go, I've finished sewing up your girly suits... Not proper carpenter work, if you ask me."

    show sill happy at right with dissolve

    sill "That's great! Now, our advertising girls are sure to bring us some good business!"

    you "It's good, but I wish we could spread the word even farther..."

    carpenter "Well... I need some real woodwork for a change. How about I upgrade the roof with a billboard?"

    you "A billboard? Well, that could be useful..."

    carpenter "In fact..."

    play sound s_surprise

    "Iulia becomes animated."

    carpenter "Boss, what if it wasn't just any billboard! I could add some clock parts, with gears and pulleys..."

    "She starts drawing frantically on her work bench. You look at her blueprint with interest."

    you "A mechanical billboard?"

    carpenter "Yes! It's going to be unlike anything the world has ever seen!"

    you "And... It's going to show boobs? Right?"

    carpenter "..."

    "You stare at her like an eager puppy."

    play sound s_sigh

    carpenter "Yes, I suppose we {i}could{/i} have it display some... boobs... *sigh*"

    you "That's {b}great{/b}! Make me a list of what you'll need, and we'll get this built in no time!"

    $ all_furniture.append(billboard)

    "You can now build a {b}Clockwork Billboard{/b} from the wagon menu, to expand your advertising settings."

    return



## CONTRACT EVENTS

label first_contract():

    show bg town at top with dissolve
    show jobgirl with dissolve

    jobgirl "Hey, [MC.name]! Got a minute?"

    you "For you? Always... What is it?"

    jobgirl "I heard about your new license... Congrats!"

    you "Yeah, thanks... It's good to be inside the city."

    jobgirl "You bet. Hopefully, you'll get the dumpster smell off your clothes in no time..."

    you "..."

    jobgirl "Anyway, listen up! I've got some good news."

    you "You do? Do tell..."

    jobgirl "Now that you are legit, you can actually take on {b}Contracts{/b} from the rich and powerful."

    you "{b}Contracts{/b}?"

    jobgirl "Yup. They're like quests, except bigger."

    you "How does it work?"

    jobgirl "It's simple. As your agent, I am always looking for new business opportunities..."

    you "My agent? Since wh..."

    jobgirl "...so I found potential customers that would pay big denars for your slaves' services!"

    you "..."

    you "Awesome! I knew I was right to pick you as my agent."

    jobgirl "But you know, contracts are serious commitments. The slavers' guild is not an organization that tolerates failure."

    you "Where have I heard that before..."

    jobgirl "You are limited to one contract a month, guild rules for newbies. Also a good way to avoid too much competition for the guild elders, I guess."

    you "And what exactly are those contracts?"

    jobgirl "It's very simple. Every month, I will present you with a selection of contracts from the guild. You may choose one as your objective for the month."

    jobgirl "Each contract requires a girl completing one or more {b}tasks{/b}. Tasks require specific skills. It's up to you to choose the best girl for the job."

    jobgirl "After picking a contract, you will have until the end of the month (the 28th) to prepare. When the month ends, you will be able to send one of your girls to complete the contract."

    jobgirl "The contracts offer big payouts... As well as reputation for you and your girl. The customers may also pay extra, if they're happy."

    you "That's great! When do we start?"

    jobgirl "Right away! Here are some leads I found this month. Pick one."

    $ calendar.generate_contracts()

    while True:
        $ tt = show_tt("top_right")
        $ result = renpy.call_screen("contracts", calendar.contracts, free=True)

        if result == "back":
            jobgirl "Aw, come on, what's wrong with those contracts? You don't feel up for it?"

            menu:
                jobgirl "Aw, come on, what's wrong with those contracts? You don't feel up for it?"

                "I need to check some things first":
                    jobgirl "Okay. In that case, I'll come back this evening to get your answer."

                    jobgirl "But it's your last chance... You can't keep important customers waiting, you know."

                    $ add_event("first_contract_return", date=calendar.time, type="night")

                "None of my girls has the skills for this.":
                    jobgirl "I see... Well, you could always buy a new one? You'd have one month to train her..."

                    menu:
                        "Let me think about it.":
                            jobgirl "All right. I'll be back tonight. But it's your last chance! You can't keep important customers waiting."
                            $ add_event("first_contract_return", date=calendar.time, type="night")

                        "No, just come back next month.":
                            jobgirl "Humph, fine. I'll come back in a month. I hope your girls will be in better shape by then!"

            hide jobgirl
            hide bg town
            with dissolve

            return

        elif renpy.call_screen("yes_no", "{b}[result.title]{/b}\nAre you sure you want to apply for this contract?"):
            call contract_chosen(first=True) from _call_contract_chosen
            return

label contract_chosen(first=False):

    if first:
        jobgirl "Okay! Great choice!"

        jobgirl "I will tell the guild, then. You have until the end of the month to get ready."

        jobgirl "There's still the small matter of my fee..."

        you "Uh? What fee?"

        jobgirl "Yes, [result.base_value] gold. My {b}finder's fee{/b} for that contract."

        you "Hey! That wasn't the deal!"

        jobgirl "Come on! As your agent, I expect to get paid... *grumble*"

        jobgirl "Tell you what. Because it's your first contract, it will be on me, this time."

        jobgirl "But make sure to have the cash to pay me next time!"

        you "Okay... *sigh*"

        $ result.enroll(free=True)
        $ last_contract_result = None

    else:
        jobgirl "Great! I will tell the guild. Now, time to pay my finder's fee..."

        $ result.enroll(free=False)

    $ add_event("contract_warning_1week", day=21)
    $ add_event("contract_warning_1day", day=27)

    hide jobgirl
    hide bg town
    with dissolve

    return

label first_contract_return():

    jobgirl "I'm back!"

    jobgirl "Here are the contracts on offer. Choose carefully."

    while True:
        $ tt = show_tt("top_right")
        $ result = renpy.call_screen("contracts", calendar.contracts, free=True)

        if result == "back":
            jobgirl "That's too bad. I'll come back in a month, with new contract opportunities. Next time, I hope we can make a deal!"

            hide jobgirl
            hide bg town
            with dissolve
            return

        elif renpy.call_screen("yes_no", "{b}[result.title]{/b}\nAre you sure you want to apply for this contract?"):
            call contract_chosen(first=True) from _call_contract_chosen_1
            return

label new_contract():

    if not story_flags["first_contract"]:
        call first_contract from _call_first_contract
        $ story_flags["first_contract"] = True
        return

    show bg town at top
    show jobgirl
    with dissolve

    jobgirl "Hey, [MC.name]!"

    $ calendar.generate_contracts()

    if last_contract_result == "success":
        jobgirl "Seems like you did well on that last contract. The customer was pleased."
    elif last_contract_result == "failure":
        jobgirl "I heard that last contract was a failure. Too bad... I hope you'll do better next time!"

    $ renpy.block_rollback()

    jobgirl "Here are some new contract opportunities. Take a look!"

    while True:
        $ tt = show_tt("top_right")
        $ result = renpy.call_screen("contracts", calendar.contracts, free=True)

        if result == "back":
            menu:
                jobgirl "Need some time to think it over?"

                "Yeah, please come back later":
                    jobgirl "All right, then, I'll come back tonight. This will be your last chance to pick a contract for this month, so think carefully!"
                    $ add_event("new_contract_return", date=calendar.time, type="night")

                "No, I'll skip on contracts this month":
                    jobgirl "Aw, I went through all this trouble to find some suitable customers for you... Well, I hope you won't miss your chance next month!"

            return

        elif renpy.call_screen("yes_no", "{b}[result.title]{/b}\nAre you sure you want to apply for this contract (fee: [result.base_value] gold)?"):
            call contract_chosen() from _call_contract_chosen_2

            hide jobgirl
            hide bg town
            with dissolve
            return

label new_contract_return():

    if last_contract_result == "success":
        jobgirl "Seems like you did well on that last contract! The customer was pleased."
    elif last_contract_result == "failure":
        jobgirl "I heard that last contract was a failure. Too bad... I hope you'll do better next time!"
    else:
        jobgirl "I'm back!"

    jobgirl "Here are the contracts on offer. Choose carefully."

    while True:
        $ tt = show_tt("top_right")
        $ result = renpy.call_screen("contracts", calendar.contracts, free=False)

        if result == "back":
            jobgirl "That's too bad. I'll come back in a month, with new contract opportunities. Next time, I hope we can make a deal!"

            hide jobgirl
            hide bg town
            with dissolve
            return

        elif renpy.call_screen("yes_no", "{b}[result.title]{/b}\nAre you sure you want to apply for this contract (fee: [result.base_value] gold)?"):
            call contract_chosen() from _call_contract_chosen_3
            return


label run_contract():

    if not calendar.active_contract:
        return

    $ con = calendar.active_contract

    scene black with fade

    "[con.title]" "The time for the contract has come."

    # Picking girls (for now only one girl can go)

    $ available_girls = [g for g in MC.girls if con.can_contract(g)]

    if len(available_girls) < con.girl_number:
        if not available_girls:
            jobgirl "Unfortunately, none of your girls are available for this contract. You missed your chance this time..."
        else:
            jobgirl "Unfortunately, not enough of your girls are available for this contract. You missed your chance this time..."
        $ last_contract_result = "failure"
        $ calendar.active_contract = None
        return

    elif con.girl_number == 1:
        jobgirl "It's time to choose a girl to send to complete the contract."
    else:
        jobgirl "It's time to choose which girls to send to complete the contract."

    $ selected_girl = available_girls[0]

    while True:
        $ girls = [renpy.call_screen("pick_girl", available_girls, con.girl_number, contract=con)]

        # sanity check
        if not isinstance(girls[0], Girl):
            pass
        elif renpy.call_screen("yes_no", "Are you sure you want to send " + and_text([g.fullname for g in girls]) + " to complete this contract?"):
            jump run_contract_continue

    # Contract introduction

label run_contract_continue:

    python:
        for girl in girls:
            girl.away = True
            add_event("return_from_leave", call_args = [girl, True], date = calendar.time)

    show expression con.bg at top with dissolve

    call dialogue(con.char, "contract greeting", con.type) from _call_dialogue

    $ temp_girls = list(girls)

    while temp_girls:
        $ girl = temp_girls.pop(0)
        call dialogue(girl, "girl introduction") from _call_dialogue_1

    call dialogue(con.char, "contract intro", con.type) from _call_dialogue_2

    # Running contract

    $ con.run(girls) # con.result is stored as "success", "partial" or "failure"

    $ temp_tasks = list(con.tasks)

    scene black with fade

    if len(temp_tasks) == 1:
        $ tsk_text = "Your job"
    else:
        $ tsk_text = "Your first task"

    while temp_tasks: # Loop will be existed once a task fails
        $ tsk = temp_tasks.pop(0)

        call dialogue(con.char, "task intro", tsk.type) from _call_dialogue_3

        show screen show_event(tsk.get_pic(rand_choice(girls)), x=config.screen_width, y=int(config.screen_height*0.8))
        with dissolve

        call dialogue(narrator, "task description", tsk.name) from _call_dialogue_4

        with fade

        $ define.move_transitions("easeol", 0.8, _ease_time_warp, _ease_in_time_warp, _ease_out_time_warp, layers=["myoverlay"])

        if tsk.result:
            play sound s_success
            show success onlayer myoverlay with easeolinleft
            pause 0.5
            hide success onlayer myoverlay with easeoloutright

            if tsk.type == "fun":
                call dialogue(narrator, "task success1", tsk.name) from _call_dialogue_5
            else:
                call dialogue(con.char, "task success", tsk.name) from _call_dialogue_6

            if tsk.type == "fun":
                show screen show_event(tsk.get_pic(rand_choice(girls), and_tags=tsk.and_tags2), x=config.screen_width, y=int(config.screen_height*0.8))
                with doubleflash

                call dialogue(con.char, "task success2", tsk.name) from _call_dialogue_7

        else:
            play sound s_crash
            show failure onlayer myoverlay with easeolinleft
            pause 0.5
            hide failure onlayer myoverlay with easeoloutright

            call dialogue(con.char, "task failure", tsk.name) from _call_dialogue_8
            jump run_contract_end

        if len(temp_tasks) > 1:
            $ tsk_text = "Your next task"
        else:
            $ tsk_text = "Your final task"

label run_contract_end():

    # Displaying results
    hide screen show_event
    show expression con.bg at top
    with fade

    $ last_contract_result = con.result

    $ result_topic = "contract " + con.result
    if con.special_bonus > 1.0:
        $ result_topic += " special"

    call dialogue(con.char, result_topic, con.type) from _call_dialogue_9

    call screen contract_result(con)

    $ sold = False
    $ girl_names = and_text([girl.name for girl in girls])

    if con.result in ("success", "partial"):
        python:
            gold = con.get_value()
            MC.gold += gold
            brothel.change_rep(brothel.max_rep*(11-brothel.rank)/100.0) # Changes bro rep by 5-10% depending on rank
            for girl in girls:
                girl.change_rep(3*(2 ** (girl.rank-1)))
        play sound s_gold

        "Congratulations! You have received [gold] gold. The reputations of your brothel and [girl_names] have increased."

        if con.result == "success":
            $ game.track("completed contracts", 1)

        # Special buying event (if all tasks are successful and the special request has ben completed)

        if con.result == "success" and con.special_bonus > 1.0:
            $ girl = rand_choice(girls)
            $ multiplier = dice(3)+1
            $ gold_offer = girl.get_price("sell", raw=True) * multiplier

            "As you come to pick up [girl.fullname], your contact asks to have a private word with you."

            call dialogue(con.char, "contract buy offer", con.type) from _call_dialogue_10

            menu:
                con.char "Will you consider selling [girl.fullname] to us for [gold_offer] gold? It is [multiplier] times her market price..."

                "Accept":
                    call dialogue(con.char, "contract buy offer accept", con.type) from _call_dialogue_11

                    $ relinquish_girl(girl)
                    $ MC.change_gold(gold_offer)

                    "You have sold [girl.fullname] for [gold_offer] gold."

                    if girl.get_love() >= 90:
                        $ unlock_achievement("sell girl love")
                        call dialogue(girl, "sold love") from _call_dialogue_12
                    else:
                        call dialogue(girl, "sold") from _call_dialogue_13

                    $ sold = True
                    $ unlock_achievement("contract sale")

                "Refuse":
                    you "I'm sorry. [girl.name] is not for sale."

                    call dialogue(con.char, "contract buy offer refuse", con.type) from _call_dialogue_14


    else:
        if con.special_bonus > 1.0:
            play sound s_gold
            $ MC.gold += con.get_special_value()

            "[girl.name] performed poorly, but as she met the organizer's bonus requirement, they reluctantly agreed to refund your contract fee ([con.base_value] gold).\nNevertheless, your reputation suffered."
        else:
            "Because of [girl_names]'s poor performance, you have received no reward for this contract. Your brothel's reputation has suffered."

        $ brothel.change_rep(brothel.max_rep*(-4-brothel.rank)/100.0) # Changes bro rep by -5-10% depending on rank

    # Chance of special MC event

    if dice(6) >= 6 and not sold:

        call contract_MC_event() from _call_contract_MC_event


    # Clearing active contract
    $ calendar.active_contract = None

    return

label contract_MC_event(): # The MC challenge part is hardcoded for each contract type, for now

    scene black with fade
    show expression con.bg at top with dissolve

    if con.type == "meeting":
        "As you reach the meeting place to collect [girl_names], you hear a loud argument."
    else:
        "Upon entering the [con.venue] to collect [girl_names], you hear a large commotion."

    scene black
    show expression con.MC_event_pic at top
    with fade

    if con.type == "cruise":
        play sound s_crash

        con.char "Avast! Pirates! Pirates are attacking the boat!" with vpunch

        play sound3 s_crowd_riot

        "Before you can react, scores of ravenous pirates climb onto the deck. They have you and [girl_names] surrounded."

        # Challenge
        $ tt = show_tt("top_right")
        $ chal = renpy.call_screen("challenge_menu", challenges=[("Fight them off", "fight", district.rank+2), ("Cast a control spell", "control", district.rank+1)])

        $ renpy.block_rollback()

        if chal == "fight":
            play sound s_sheath
            "You unsheathe your weapons, readying yourself for a fight."
            call challenge(chal, district.rank+2) from _call_challenge_66 # result is stored in the _return variable
            $ r = _return

            if r:
                play sound s_clash
                pause 0.5
                play sound2 s_sheath

                "Roaring like a lion, you meet the pirates head on and cut them down one after the other."

                play sound s_sheath
                pause 0.2
                play sound s_wscream
                with vpunch

                "Inspired by your bravery, the defenders rally around you, and quickly recover the upper hand against the disorganised wretches."

            else:
                play sound s_clash
                pause 0.5
                play sound2 s_clash

                "You try to defend against the onslaught, but are quickly outnumbered and surrounded."

                play sound s_crash
                with vpunch

                "Swinging from a rope, a pirate kicks you in the back, sending you tumbling down on the deck. His comrades disarm you, laughing."

                show screen show_event(girl.get_pic("service", and_tags=["group"], hide_farm=True), x=config.screen_width, y=int(config.screen_height*0.8)) with dissolve

                "They have their fun with [girl_names] while you look on helplessly."

                play sound s_screams

                "They let them go when they are finished, sobbing."

                hide screen show_event with dissolve
        else:
            play sound s_mystery
            "Muttering secret words under your breath, you ready a control spell while maneuvering away from the scuffle."
            call challenge(chal, district.rank+1) from _call_challenge_29 # result is stored in the _return variable
            $ r = _return

            if r:
                play sound s_chimes

                "You cast a mind control spell on the pirates, convincing them that the deck is crawling with snakes."

                "Pirate" "Get away from me! Aaarh!!!"

                "One by one, the spellbound pirates abandon ship, screaming, and the rest of the fiends quickly turn tail."

            else:
                play sound s_fire

                "Dodging ropes and projectiles, you become disoriented and lose sight of your targets. In the meantime, a fire starts to spread in the cabins."

                play sound s_scream

                girls[0].char "Master!"

                "You finally reach [girl_names], nearly unconscious from inhaling the heavy smoke. You barely escape with your lives."

        if r:
            you "Yaaah!"

            play sound s_splash

            "The last attacker is pushed back overboard. The battle is won!"

            con.char "Ya've done it! What a hero!"

            "After the dust settles, the representative from [con.organizer] thanks you profusely for your help."

            "As a reward, he gives you access to a secret stash in the back, where they keep the smuggling goods."

            con.char "Spices from all over the world... This is some good shit, man. You can have a little. *inhale*"

            play sound s_drug

            "You prudently pass on the more hardcore stuff, but take a bag of focus-inducing drugs to share with your girls."

            play sound s_girls_laugh
            scene black with fade

            "{b}Spice up{/b}: Your girls will receive double amounts of JP for a week."
            $ MC.add_effects([Effect("boost", "all jp gains", 1.0, scope="brothel")], expires=calendar.time+8)

        else:

            scene black with fade
            "You finally make your way back to [brothel.name]. [girl_names]'s energy has taken a hit."

            python:
                for girl in girls:
                    girl.tire(50)
                    girl.change_mood(-10)

    elif con.type == "party":

        "Drunkard" "Come back, you dumb slut! I'll slash that pretty face of yours!"

        girl.char "No, leave me alone! Master, help!"

        "A drunk man is pursuing [girl.fullname]. He's holding a kitchen knife threateningly."

        # Challenge
        $ tt = show_tt("top_right")
        $ chal = renpy.call_screen("challenge_menu", challenges=[("Kick his ass", "force", district.rank+1), ("Threaten him", "bluff", district.rank+2)])

        $ renpy.block_rollback()

        if chal == "force":
            "As the man stumbles towards [girl.name], you grab a bar stool and fling it at his back."

            play sound s_dodge
            "WHOOSH!"

            call challenge(chal, district.rank+1) from _call_challenge_50 # result is stored in the _return variable
            $ r = _return

            if r:
                play sound s_punch

                "You hear a satisfying thud as the stool slams the man in the back of the head. He is knocked out by the blow."
            else:
                play sound s_dodge
                pause 0.3
                play sound2 s_shatter

                "Your aim was clumsy, and the man surprisingly nimble in spite of his level of inebriation. You broke the ballroom mirror."

                "Drunkard" "Wha' the hell wuz that, you sneaky weasel!"

                con.char "Nooo! This mirror was a century old!!!"

                "You have all the pain in the world to escape the drunk man's clumsy attempts to stab you while negotiating compensation for the damage with the angry woman."


        else:
            "Putting yourself between the man and [girl.name], you stand tall and talk with a commanding voice."

            you "Stop this at once! One more step, and you're a dead man!"

            call challenge(chal, district.rank+2) from _call_challenge_51 # result is stored in the _return variable
            $ r = _return

            if r:
                "Your eyes burn with fury, and your deadly stare strikes fear through the drunk man's thick skull."

                "Drunkard" "Wow, here, relax, fella... I wuzn't going to hurt nobdoy..."

                "Cowed, the man retreats in a corner, stumbling on a sofa. You can soon hear him snoring: danger averted."

            else:
                "Your threats only seem to make the man angrier."

                "Drunkard" "I am a Duke of royal blood, you scoundrel! This [con.venue] belongs to me! *hiccup*"

                "Drunkard" "Guaaaards!"

                "Before you can catch your breath, armed men surround you. They disarm you and march you to a cell in the basement."

                you "Listen, good men, we can come to an arrangement..."

                guard "*smirk*"

        if r:
            con.char "Finally, someone stopped that mad man! He slashed my most beautiful dress..."

            con.char "It's good you were here, or someone might have been seriously hurt. [con.organizer] would like you to have this."

            play sound s_gold

            $ bonus = (con.base_value*2) // 3
            $ MC.gold += bonus

            "She hands you a weighty purse with [bonus] gold in it."

            scene black with fade

        else:
            play sound s_gold
            $ cost = con.base_value // 2
            $ MC.gold -= cost

            scene black with fade
            "You emerge from this nightmare [cost] gold lighter. At least, [girl.fullname] is unharmed."

        $ girl.change_love(2)
        girl.char "Thank you, Master... *sob*"


    elif con.type == "ceremony":

        con.char "Oh no, the Head Nun... She has been possessed!"

        play music m_demons

        "Unholy light bathes the scene as the head nun stands naked in a trance, singing a psalm in a foreign tongue."

        play sound s_mystery

        "Demonic Voice" "{font=SFBurlingtonScript.ttf}Yog-Sothoth mgah'ehye n'ghftdrnn hup mgepogg fa'ch ymg' nilgh'ri...{/font}"

        play sound s_roar

        "Dark tentacles erupt from the floor and walls and start wrapping around the unsuspecting ceremony attendants. A massive eye sprouts out of the ground, taking in the scene."

        play sound s_scream

        girl.char "A monster! EEEEK!!!"

        # Challenge
        $ tt = show_tt("top_right")
        $ chal = renpy.call_screen("challenge_menu", challenges=[("Stab the eye", "fight", district.rank+1), ("Dispel the magic", "cast", district.rank+2)])

        $ renpy.block_rollback()

        if chal == "fight":

            play sound s_clash
            "You leap forward, slashing away at the tentacles, doing your best to reach the monstrous eye."

            call challenge(chal, district.rank+1) from _call_challenge_52 # result is stored in the _return variable
            $ r = _return

            if r:
                play sound s_sheath
                pause 0.3
                play sound s_sheath

                "Slicing off the tentacles in your way, you spot a heavy metal chandelier above the eye. You throw a dagger at the rope that holds it."

                play sound s_dodge
                pause 0.3
                play sound2 s_crash
                with vpunch
                pause 0.2
                play sound s_roar

                "The beast roars with pain as the chandelier hits it square in the eye. The lights flicker, and the tentacles retreat between the cracks in the stone."


            else:
                play sound s_sheath
                pause 0.3
                play sound s_punch

                with vpunch
                "Before you can reach your goal, a large tentacle hits you sideways, you are flung into the wall and the world becomes dark..."

                scene black with fade

        else:

            play sound s_mystery
            "Stepping up to the altar, you try to shake off the possession spell that links the demon and the hapless priestess."

            call challenge(chal, district.rank+2) from _call_challenge_53 # result is stored in the _return variable
            $ r = _return

            if r:
                play sound s_spell

                you "{font=SFBurlingtonScript.TTF}Nogephaii ahagl ymg' hup mgepnog, ars'hol!{/font}"

                "Your incantation works, and life slowly returns to the eyes of the poor woman. Suddenly, she gasps and she collapses, and the lights flicker."

                "The monster's image lingers for a few moments, fading out. You blink, and it's gone."

            else:
                you "{font=SFBurlingtonScript.TTF}Nogephaii ahagl ymg', err...{/font}\nC'm'on, lady, wake up!"

                play sound s_scream

                "You are interrupted by a scream. [girl.fullname] has been caught! You turn around, only to be hit in the face by a massive tentacle."

                play sound s_punch
                with vpunch
                scene black with fade

        if r:
            "After a few seconds, the light dissipates and the [con.venue] looks as if nothing happened, except for the unconscious nuns lying in pools of monster cum with their uniforms ripped off."

            con.char "Thank all that is Holy, you have arrived just in time... Something went wrong during the ceremony..."

            you "Uh... You think?"

            con.char "But rest assured, [con.organizer] will reward you. Here, take this jar of Holy Water, made by the high priestess herself."

            you "Err... What is it? What does it do?"

            con.char "Well, she uses juices from her... Ahem, never mind. Just know that it will replenish your strength."

            scene black with fade

            play sound s_potion

            python:
                for girl in MC.girls:
                    girl.change_energy(20)
                    girl.change_mood(10)

            "In spite of its doubtful origins, you nevertheless have the girls try the beverage back at the brothel. They actually like it, and receive a boost to their energy and morale."

        else:

            "When you come back to your senses, the monster roars in pain as the church knights are finally managing to fight it off."

            "You are relieved to find that your anus hasn't been defiled by the tentacle beast while you were out... [girl.fullname] wasn't so lucky."

            show screen show_event(girl.get_pic("anal", and_tags=["monster"]), x=config.screen_width, y=int(config.screen_height*0.8)) with dissolve

            play sound s_screams

            girl.char "*scream*"


            if girl.weakness == "monster":
                play sound s_orgasm

                "To your surprise, [girl.name] is drooling and screaming in ecstasy as the filthy demon ravages her ass. It seems that she has a thing for demons."

                if not farm.knows["weakness"][girl]:
                    $ narrator("You notice " + girl.name + " reacts strongly in the presence of monsters (" + event_color["fear"] % "weakness discovered" + ").")
                    $ farm.knows["weakness"][girl] = "monster"

            else:
                $ narrator("[girl.name] watches in helpless horror as the monster ravages her ass. This encounter will leave a mark (" + event_color["fear"] % "weakness discovered" + ").")
                $ girl.weakness = "monster"
                $ farm.knows["weakness"][girl] = "monster"

            hide screen show_event with dissolve
            scene black with fade

            "When the knights finally free [girl.name], you grab her and run away from this hellish place."

            $ girl.change_fear(10)
            $ girl.tire(50)


    elif con.type == "festival":

        con.char "Oh no!!! The prize animals have escaped! The rutting males are going on a rampage!!!"

        play sound s_scream

        girl.char "EEEK!!!"

        "[girl.fullname] fell down in the mud while trying to run away. A massive beast towers above her, drooling. It seems to have one thing on its mind..."

        # Challenge
        $ tt = show_tt("top_right")
        $ chal = renpy.call_screen("challenge_menu", challenges=[("Provoke the beast", "stamina", district.rank+2), ("Soothe the wild animal", "rally", district.rank+1)])

        $ renpy.block_rollback()

        if chal == "stamina":

            you "Why don't you come after me, you dumb animal?"

            play sound s_dodge
            pause 0.3
            play sound2 s_punch

            "You throw a stone at the wild beast's muzzle. It roars with fury."

            with vpunch
            play sound s_roar

            "You've managed to get his attention. But now, you must RUN!"

            play sound s_roar

            call challenge(chal, district.rank+2) from _call_challenge_54 # result is stored in the _return variable
            $ r = _return

            if r:
                "You dart towards an exit while the huge, pissed off beast charges after you."

                "It is quite fast in spite of its size, and you know you cannot keep up forever. You run full speed towards a large houseware stall, then abruptly roll out of the way as you reach it."

                with vpunch
                play sound s_crash
                pause 0.2
                play sound2 s_shatter

                "Unable to stop in time, the beast crashes head first into the stall, destroying everything in its path. When it emerges from a cloud of dust, its head is stuck in a large kettle."


            else:
                "You run away as fast as you can, yet soon you can feel the hot breath of the beast on your back. You start to wonder if it was all a good idea."

                play sound s_roar

                you "AAAAAH!!!"

                play sound s_wscream
                pause 0.2
                with vpunch
                play sound2 s_crash

                "The creature catches up with you and tramples you mercilessly. It soon turns its attention back to [girl.fullname], however."

        else:
            "Approaching the animal carefully, you whistle to get its attention."

            you "Here, little buddy, don't be afraid... It's just me..."

            call challenge(chal, district.rank+1) from _call_challenge_55 # result is stored in the _return variable
            $ r = _return

            if r:
                "The creature eyes you suspiciously, and you fear it might be about to attack. You keep talking, trying to sound non-threatening."

                you "Come here, pal, it's going to be all right... There, good boy..."

                "Little by little, you get closer, and you can feel the animal ease up. After patting it gently on the forehead, you lead it back to its enclosure."

            else:
                play sound s_roar

                "The animal looks pissed that someone interrupted it. Something tells you this wasn't the best idea."

                you "Sit! Bad boy, bad! Don't come any c..."

                play sound s_punch
                with vpunch

                "*SLAM*"

                play sound s_wscream

                you "Haaaaaa!!!"

                "The beast sends you flying yards away, before turning its attention back to [girl.fullname]."


        if r:
            play sound s_moo

            con.char "Good, you got the last of them!"

            con.char "You were very brave out there... Here, have this selection of prime food from the fair. It's all delicious!"

            $ it = [get_rand_item("rare", item_types="Food"), get_rand_item("common", item_types="Food"), get_rand_item("common", item_types="Food"), get_rand_item("common", item_types="Food")]
            $ MC.items += it

            scene black with fade

            "You have received 4 delicious foodstuffs."

        else:
            play sound s_screams

            show screen show_event(girl.get_pic("sex", and_tags=["beast"]), x=config.screen_width, y=int(config.screen_height*0.8)) with dissolve

            "The horny beast easily overpowers the poor girl, ripping her dress apart."

            girl.char "Aaaah! Nnnnh... No... Aaaah..."

            if girl.pop_virginity(origin="farm"):
                "She cries silent tears as her virginity is taken away by a dirty beast."

            if girl.weakness == "beast":
                play sound s_moans

                "Before long, however, [girl.fullname] is moaning with pleasure, unable to control herself. It seems being raped by a beast turns her on..."

                if not farm.knows["weakness"][girl]:
                    $ narrator("You notice " + girl.name + " reacts strongly in the presence of beasts (" + event_color["fear"] % "weakness discovered" + ").")
                    $ farm.knows["weakness"][girl] = "beast"

            else:
                $ narrator("[girl.name] struggles helplessly against the mighty beast, unable to stop the nightmare. This encounter will leave a mark (" + event_color["fear"] % "weakness discovered" + ").")
                $ girl.weakness = "beast"
                $ farm.knows["weakness"][girl] = "beast"

            "When the beast finally tires with [girl.name], it rolls over to the side and start snoring. Its handlers take advantage of this to finally catch it."

            hide screen show_event with dissolve
            scene black with fade

            "With smelly animal cum gushing out of her pussy, [girl.name] is unresponsive and unable to speak. You wrap her in a blanket and bring her home."

            $ girl.change_fear(10)
            $ girl.tire(50)

    elif con.type == "date":

        con.char "Alert!!! Thief! Thief!"

        girl.char "No! Let me go!!!"

        "The [con.venue] has been infiltrated by a shady thief. As soon as he is spotted, he takes out a dagger and holds [girl.fullname] hostage."

        play sound s_sheath

        thug3 "Nobody moves, or I'll slit her throat!"

        "Holding [girl.name] as a human shield, the thug retreats to the back door. He grabs a horse, forcing [girl.name] to mount with him."

        # Challenge
        $ tt = show_tt("top_right")
        $ chal = renpy.call_screen("challenge_menu", challenges=[("Run after him", "stamina", district.rank+2), ("Cast a spell", "cast", district.rank+1)])

        $ renpy.block_rollback()

        if chal == "stamina":

            "You reach the outside and start running after the horse carrying the thief and your girl."

            thug3 "Arh arh! You think you run faster than a horse?"

            call challenge(chal, district.rank+1) from _call_challenge_56 # result is stored in the _return variable
            $ r = _return

            if r:
                "However, the mount resists her unknown rider and is slowed by the weight of two people on its back. Meanwhile, you run like the wind, and soon manage to get side by side with the horse."

                thug3 "What kind of monster runner are you? Take that, you bastard!"

                play sound s_dodge

                "The thug tries to stab you with his dagger, but you grab his wrist and pull him off the saddle."

                play sound s_crash
                with vpunch

                thug3 "OUCH!!!"

                "[girl.fullname] manages to stop the frightened horse and ride back to you."

            else:
                "The mount struggles to pick up pace, and at some point it seems as though you could almost catch up, but the thug spurs it on and soon, it leaves you panting in the dust."

                girl.char "No, let me go!!! Master [MC.name]..."

                "Her voice trails off in the distance. The horse and its riders disappear from your sight. [girl.fullname] has been kidnapped!"

        else:

            you "Quick, I must stop them! What's the first spell that comes to mind..."

            call challenge(chal, district.rank+1) from _call_challenge_57 # result is stored in the _return variable
            $ r = _return

            if r:
                play sound s_spell

                "Chanting the secret words for a levitation spell, you make the horse hover a couple of feet above the ground."

                thug3 "Why is this animal not moving? Faster, faster!"

                "As the thug struggles to understand why his mount is standing in place, you leisurely walk up to him and shoot a fireball in his face point blank."

                play sound s_fire
                with flash
                pause 0.2
                play sound2 s_wscream

                $ girl.change_fear(2)

                girl.char "Hey! You almost hit me!"

                "[girl.name]'s eyebrows are a little burnt, but otherwise she is none the worse for wear."

            else:
                play sound s_fire

                "With not enough time to think clearly, you shoot a fireball at the running horse."

                you "(What am I doing... This could kill [girl.name]!)"

                play sound s_fizzle

                "At the last moment, you alter the trajectory of your fireball so it hits the ground harmlessly next to the horse."

                "Horse" "NEIGHHHH!"

                "Afraid of fire, the horse gallops even faster, carrying [girl.fullname] and her captor away from you. She has been kidnapped!"

        if r:

            $ girl.change_love(3)

            girl.char "Thank you, Master... You rescued me from that jerk!"

            con.char "More importantly, you caught the thief and we got back [con.organizer]'s family heirloom. You deserve a reward."

            call receive_item(get_rand_item("exceptional"), msg="The maid hands you a very expensive item for your trouble: %s.") from _call_receive_item_18

        else:
            scene black with fade

            you "Oh no... [girl.name]..."

            python:
                log.add_report("{color=[c_red]}Security alert! {b}" + kidnapped_girls[0].fullname + " was kidnapped!{/b}{/color}")
                MC.girls.remove(girl)
                game.kidnapped.append(girl)
                girl.kidnapper = "一个危险的小偷"
                girl.track_event("kidnapped", arg = "一个危险的小偷")

            security_breach "There is nothing you could do. Maybe someone in town can help you find out her whereabouts?"



#   - Special events:
#     - Pirates: Spi/Str
#     - Drunk assault: Str/Cha
#     - Demon summon: Str/Spi
#     - Beast: Cha/Str
#     - Kidnapper: Str/Spi
#     - Politics: Cha/Spi
#     - Spell battle: Spi/Cha
#     - Join fun

#汉化标签，待汉化的合同内容，对应描述在BKdialouge line378#
#     - Context: Boat cruise (JP), Lavish Party (gold), Religious ceremony (mood+energy), School festival (skill), Private Date (items),
#                Official Meeting (rep), Magic conference (double AP), Orgy (pref increase)

    elif con.type == "meeting":

        "Angry Noble" "Your position on [con.venue] is unacceptable and an insult to my people! If you refuse to yield, then this means WAR!"

        play sound s_crowd_boos

        "The negotiations have failed, and the major factions at the meeting are in open conflict."

        # Challenge
        $ tt = show_tt("top_right")
        $ chal = renpy.call_screen("challenge_menu", challenges=[("Avert conflict", "rally", district.rank+1), ("Use a mind control trick", "control", district.rank+2)])

        $ renpy.block_rollback()

        if chal == "rally":

            "You step in, in a last ditch attempt to help cooler heads prevail."

            call challenge(chal, district.rank+2) from _call_challenge_58 # result is stored in the _return variable
            $ r = _return

            if r:
                stop sound

                you "Ladies and Knights, please hear me out. This meeting has been convened in a spirit of friendship and cooperation. Surely we shall not let a last minute hurdle derail what we took months to build."

                man "He's right... Whoever he is!"

                woman "That makes sense..."

            else:
                you "People, people, don't listen to that crazy lady..."

                "Angry Noble" "WHAT?!? Men! Seize that [MC.playerclass]!"

                "Rival Noble" "He's right about one thing, you're crazy! How dare you bring armed men in here. Guards!"

                "Angry Noble" "So you had hidden men too? You snake!"

        else:
            "Trying to remain inconspicuous, you focus your attention on the leader of the troublemakers."

            "As you ready your spell, the protocol officer gives you a stern look. You cast it before she has a chance to stop you."

            call challenge(chal, district.rank) from _call_challenge_59 # result is stored in the _return variable
            $ r = _return

            if r:
                you "That should do the trick..."

                play sound s_spell
                you "*whispering a secret formula*"

                "The angry lady interrupts herself, blushing. She tries to talk, but her words are mixed with sighs and moans."

                play sound s_sigh

                "Angry Noble" "We will, uh... We will not stand, aaah... This aggression... Mmmh..."

                play sound s_mmmh
                "She becomes even more flustered, her nipples peaking under her dress."

                play sound s_surprise
                show screen show_img("NPC/encounters/impress1_5.webp") with dissolve

                "Angry Noble" "I can't help it! I'm so horny... Someone fuck me, NOW!"

                "The Lady rips her dress off, and grabs her rival's crotch. Before you know it, they are having rough sex on the strategy table, kicking away the maps and unit flags."

                play sound s_moans

                con.char "Well... That's an unorthodox way of solving conflicts if I ever saw one... But that worked, so... Well done?"

                you "I got this. A simple spell should be enough to make this lady calm down..."

                play sound s_vibro

                "A necklace around the noble's neck buzzes with magic energy."

                "Angry Noble" "Somebody is trying to use magic in this very room! ASSASSIN! To me, soldiers! ATTAAAACK!!!"

        if r:

            hide screen show_img
            scene black
            with fade

            con.char "Ladies and Gentlemen... The food is fresh, the hookers are hot, why don't you go back to the negotiations after a good bit of fun?"

            play sound s_crowd_cheer
            "*Roar of approval*"

            "The diplomat turns to you."

            con.char "The crisis is averted, thanks to your quick thinking. You have done us a good turn. [con.organizer] shall not forget this."

            $ MC.change_prestige(5*game.chapter)
            $ brothel.change_rep(100*game.chapter)

            "You have gained prestige and reputation."

        else:
            play sound s_sheath
            pause 0.2
            play sound2 s_crowd_riot

            "A big fight erupts, and you barely escape with your life."

            con.char "You! You ruined our perfectly prepared negotiations! We won't forget this! *mad*"

            $ brothel.change_rep(-75*game.chapter)

            "Your reputation has suffered."



    elif con.type == "magic":

        "Two witches are arguing loudly about which school of magic is the best."

        con.char "Oh no, those two were top of their class in Karkyr... They are extremely competitive..."

        play sound s_spell

        "The argument escalates further, and the witches start insulting each other, then casting spells and counterspells. Soon, magic bolts are flying around, and innocent bystanders are in danger of being hurt." with vpunch

        play sound s_fire
        with flash

        con.char "Watch out!"

        # Challenge
        $ tt = show_tt("top_right")
        $ chal = renpy.call_screen("challenge_menu", challenges=[("Cast a silence spell", "detect", district.rank+2), ("Defuse their feud", "charm", district.rank+1)])

        $ renpy.block_rollback()

        if chal == "detect":

            "Stepping up to the challenge, you prepare to battle two master sorceresses at once... By sneaking up on them."

            call challenge(chal, district.rank+2) from _call_challenge_60 # result is stored in the _return variable
            $ r = _return

            if r:
                you "By the secret last words of Archmage Azgathoros... SHUT THE FUCK UP, BITCHES!"
                play sound s_spell

                "The two women are too busy arguing to notice your silence spell until it's too late. Suddenly, their voices die down and they are prevented from causing further mayhem."

                "It takes more than that to stop their rivalry, however, and soon they step outside and start slapping each other, rolling down in the mud... All in complete silence."

                con.char "Wow, look at them go... I'll fetch some pop-corn."


            else:
                you "(They are too busy fighting each other to notice me, I'm sure...)"

                play sound s_surprise
                "Witches" "*together* WHO THE FUCK DARES INTERRUPT OUR FIGHT?!?" with vpunch

                play sound s_fizzle

                you "Oh crap."

                "Witches" "*together* MAGIC BACKLASH!!!"


        else:

            you "Ladies! Please... Hear me out!"

            "You spoke loudly, and the witches temporarily interrupt their yelling and hurling fireballs at each other to look at you. They seem none too pleased."

            "Blue witch" "What's with this interruption! Explain yourself."

            you "Why can't two beautiful and talented women like you work together to overcome your differences?"

            "Blue witch" "Are you mad? How could I befriend this slut? She couldn't even summon a minor demon to save her life, but she got ahead at school because she was fucking the Principal..."

            play sound s_surprise

            "Red witch" "Whaat? And you, you got ahead... By giving head!"

            "Blue witch" "I'll slaughter you!"

            "Red witch" "Bring it, fat cow!"

            call challenge(chal, district.rank+1, score=True) from _call_challenge_61 # result is stored in the _return variable
            $ r = _return

            if r > 0:

                you "No, no, no, stop... You two are tremendously talented, everyone can see that... Your success was obviously because of your skills, not your looks!"

                "Blue witch" "Are you calling us... unattractive?"

                "Red witch" "Yeah, you think we're too ugly to use our charms to get ahead? I {i}was{/i} fucking the Principal, I'll have you know!"

                you "Not at all. You are both stunning. In fact, I couldn't bear to watch you fight, lest you damage your perfect bodies..."

                if r >= 5:
                    "The witches give you a curious look."

                    "Blue witch" "Tell us..."

                    "Red witch" "...handsome one..."

                    "Blue witch" "...which one of us..."

                    "Red witch" "...is the fairest?"

                    you "Uh?"

                    "Blue witch" "C'm'on, simple question!"

                    "Red witch" "Which one of us would you like to {b}bone{/b}!"

                    you "..."

                    you "Both of you, of course!"

                    play sound s_surprise

                    "Witches" "*together* What kind of answer is that!" with vpunch

                    you "Well, it's... It's the truth!"

                    "Blue witch" "In such a scenario, you would find me far superior!"

                    "Red witch" "No way... I would give you the time of your life!"

                    "Blue witch" "Oh yeah? Bring it!"

                    "Red witch" "I'll make you eat your words... You, come here!"

                    scene black with fade
                    show bg witches2 at top with dissolve

                    play sound2 s_moans_quiet
                    pause 0.1
                    play sound s_moans

                    "Blue witch" "Oh, aaah..."

                    "Red witch" "Oh yes, oh yes..."

                    "Blue witch" "Keep going... I'm almost..."

                    "Red witch" "Oh, yes, oh, yes, oooh!!!"

                    with flash

                    "Witches" "*together* AAAAAAAH!!!"

                    play sound s_orgasm
                    pause 0.1
                    play sound s_orgasm_fast

                    show bg witches3 at top with doubleflash

                    "You cover both girls in sticky cum as they finally cum together."

                    "Blue witch" "Well, uh... Who... Who won?"

                    "Red witch" "It's, aah... It's a draw..."

                    "Blue witch" "No way..."

                    "Exhausted, both girls collapse into a deep sleep. You drag yourself out of here before they have a chance to recover some energy and resume their fighting."

                else:
                    play sound s_sigh
                    "Blue witch" "So that's why you interrupted our fight... Only a horny idiot that doesn't value his life could have done that... *thoughtful*"

                    "Red witch" "Well, it is true that I wouldn't want to get a scar on my cute face... I just spent a week at the spa to get my skin smoother..."

                    "Blue witch" "Stranger, it just occurred to me that I am too good to waste my time fighting with half-wits or entertaining stupid interruptions by the general public. I'm leaving this dumb summit."

                    "Red witch" "And {i}I{/i} just realized I had a priority appointment for a manicure. This is a much better use of my day than lowering myself to fight with the mentally-ill. I'm out!"

                    "Both witches leave the [con.venue] with their head up high. The party breathes a sigh of relief."

            else:
                you "No, listen... It doesn't matter if you were both high school sluts..."

                "Witches" "*together* WHAT DID YOU CALL US?" with vpunch

                you "No, I meant... I was merely repeating..."

                "Blue witch" "Now..."

                "Red witch" "...you..."

                "Blue witch" "DIE!!!" with vpunch

        if r:
            scene black with fade

            con.char "Thank you, you stopped this feud before it started... Knowing those two, they probably would have burnt the [con.venue] down."

            con.char "As a reward, let me cast an 'energy' spell for you... This is a must with our older gentlemen customers, but I'm sure you will find it useful also."

            $ MC.add_effects(Effect("boost", "AP", 1.0), expires=calendar.time+5)

            "You have received some extra energy! This will last for 5 days."

            play sound s_laugh

            con.char "I think this bulge in your pants means it's working... Teeheehee..."

        else:

            play sound s_lightning
            pause 0.2
            play sound2 s_wscream

            you "HYAAAAAAAH!!!" with vpunch

            scene black with fade

            con.char "Oh, man... I didn't think you would survive this."

            you "Gwaaah... *drooling*"

            con.char "You'll be all right... The shakes should disappear in a couple of days... Probably."

            $ MC.add_effects(Effect("boost", "AP", -0.5), expires=calendar.time+3)

            "Your nervous system has been nearly fried up. Your energy will be lower for the next 3 days."


    elif con.type == "orgy":

        con.char "Oh, [MC.name], is that you? Thank Arios you're here, the orgy was just getting started!"

        you "Well, I've come to pick up [girl.name]..."

        con.char "And [girl.name] needed a partner! Perfect! Take off your clothes, and join us!"

        "She doesn't really leave you any choice: her hand is already unzipping your pants."

        menu:
            "Choose what you want [girl.fullname] to do:"

            "Oral sex":
                $ act = "service"
                $ pic1 = girl.get_pic(["oral"], ["service"], hide_farm=True)
                $ pic2 = girl.get_pic(["cim"], ["cumshot"], and_tags=["oral"], hide_farm=True)

            "Regular sex":
                $ act = "sex"
                $ pic1 = girl.get_pic(["cowgirl"], ["sex"], hide_farm=True)
                $ pic2 = girl.get_pic(["cin"], ["cumshot"], and_tags=["sex"], hide_farm=True)

            "Butt sex":
                $ act = "anal"
                $ pic1 = girl.get_pic(["doggy"], ["anal"], and_tags=["anal"], hide_farm=True)
                $ pic2 = girl.get_pic(["cob"], ["cumshot"], and_tags=["anal"], hide_farm=True)

            "Kinky sex":
                $ act = "fetish"
                $ pic1 = girl.get_pic(["fetish"], and_tags=["sex"], hide_farm=True)
                $ pic2 = girl.get_pic(["cof"], ["cumshot"], and_tags=["fetish"], hide_farm=True)

            "Threesome":
                $ act = "bisexual"
                $ pic1 = girl.get_pic(["bisexual"], not_tags=["lesbian"], hide_farm=True)
                $ pic2 = girl.get_pic(["cumshot"], and_tags=["bisexual"], hide_farm=True)

            "Group sex":
                $ act = "group"
                $ pic1 = girl.get_pic(["sex"], and_tags=["group"], hide_farm=True)
                $ pic2 = girl.get_pic(["bukkake"], ["cumshot"], and_tags=["group"], hide_farm=True)

        scene black with fade
        show screen show_event(pic1, x=config.screen_width, y=int(config.screen_height*0.8)) with dissolve

        play sound s_moans

        girl.char "Oh, Master! Oh..."

        girl.char "Mmmh... Aaah..."

        play sound s_aah
        with flash

        girl.char "AAAAAH!"

        show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8)) with doubleflash

        if act in ("sex", "group"):
            if girl.pop_virginity("MC"):
                $ MC.prestige += 5

                "[girl.fullname] has lost her virginity to you during an orgy. Kinky!"

        "You kind of lose track of [girl.name] at some point during the orgy. When you finally find her, she is covered with a dozen men's cum."

        play sound s_ahaa
        show screen show_event(girl.get_pic(["creampie"], ["cum shower"], ["cumshot"], hide_farm=True), x=config.screen_width, y=int(config.screen_height*0.8)) with dissolve

        girl.char "Ahaa..."

        girl.char "Master [MC.name]..."

        hide screen show_event
        scene black
        with fade

        $ girl.raise_preference(act, bonus=3)

        "[girl.fullname]'s [act] preference has raised significantly."


    return

label contract_warning_1week():

    jobgirl "Reminder: You have an upcoming contract ([calendar.active_contract.title]) in 7 days."

    return

label contract_warning_1day():

    jobgirl "Reminder: You have an upcoming contract ([calendar.active_contract.title]) tomorrow!"

    return

## AUCTION ##

label auction_brothel(): # Where resource is a string

    $ MC.gold += old_brothel_auction_price
    $ renpy.block_rollback()

    play sound s_gold
    show screen auction_brothel(old_brothel_name, old_brothel_auction_price)
    with dissolve

    pause

    hide screen auction_brothel
    with dissolve

    return

## TAX EVENTS ##

label fade_tax_amount():

    show screen tax_tab(True)
    with dissolve

    $ _skipping = False
    $ renpy.pause(2, hard=True)
    $ _skipping = True

    hide screen tax_tab

    return

label tax_intro():

    "One morning, you are busy going over last night's accounts with Sill when you receive an unexpected visit."

    scene black with fade
    if brothel.get_common_rooms():
        $ room = brothel.get_random_room_pic_path()
    else:
        $ room = "black"

    show expression room at top
    with dissolve

    play sound s_chimes

    show taxgirl with dissolve

    taxgirl "..."

    you "Uh... Hello?"

    sill "My lady? Can we help you?"

    "The strange woman takes her time detailing every feature in the room, before arresting her eyes on Sill."

    taxgirl "You. You're a slave, aren't you?"

    taxgirl "I can feel it in your magical aura. Yet you seem quite powerful for a mere whore..."

    play sound s_surprise

    sill sad "Hey! I'm not a whore!" with vpunch

    sill "I'm sir [MC.name]'s personal assistant, I'll have you know..."

    "The woman gives Sill an impassible look."

    sill "Master! Tell this woman..."

    menu:
        you "Sill is..."

        "My valuable assistant":

            you "It's true. Sill is my valuable assistant, and I trust her with all of my personal and business matters."

            $ MC.good += 1
            $ NPC_sill.love += 1
            sill happy "Oh, Master! *blush*"

            taxgirl "Really? Odd, a pimp getting sentimental about a sex slave... Well, it takes all kinds."

        "My personal slave":

            you "It's true. Sill is no common whore, she is reserved for my personal use."

            $ MC.neutral += 1
            sill "Err... Well, I guess..."

            taxgirl "A sex slave is a sex slave. You make her feel special one day, then sell her the next day to a gang bang joint down the street..."

            sill "No!"

        "One of my cum dumps":
            $ MC.evil += 1
            $ NPC_sill.love -= 1

            you "Sill is just one of my many cum dumps. Perhaps when I tire of her, I'll let some vagrants use her as they see fit..."

            "Sill's jaw drops, and she becomes livid."

            taxgirl "Cold... I wonder if you mean it."

    "The woman moves closer to Sill, her gaze unflinching."

    sill "What do you..."

    play sound s_surprise

    sill "Aah!" with vpunch

    "The woman reaches under Sill's dress and squeezes her butt, hard."

    taxgirl "Firm, yet supple... Good thighs, youthful breasts..."

    taxgirl "It seems your wares are of better quality than this poor setting advertises."

    you "Enough! You barge in here, criticize my establishment, molest my, er, personal slave... Who are you, and what do you want?"

    taxgirl "Of course. Forgive me for not introducing myself, I'm not a big fan of pointless social niceties."

    taxgirl "I'm the local liaison officer for the Slavers' Guild. I'm going to handle your account."

    $ taxgirl_name = "Slavers' Guild Officer"

    you "Handle my... what? I don't understand..."

    "The woman looks unphased."

    if persistent.seen_tax_intro is None or not persistent.seen_tax_intro:
        $ persistent.seen_tax_intro = True
        menu:
            taxgirl "Do you need me to explain everything?"

            "Yes, explain yourself":
                pass
            "No, I get it":
                you "I get it. You'll come here on the 15th of every month, tell me how much money I owe, then come to collect on the 1st day of the next month. Oh joy."

                taxgirl "Seems like you know everything already. Very well. Our accountants tell me that this month's payment is going to be {b}[NPC_taxgirl.current_tax]{/b} denars. See you on the 1st."

                hide taxgirl with dissolve
                hide expression room with dissolve

                return

    taxgirl "Of course. Tell me, Mister [MC.name], how do you feel about taxes?"

    menu:
        you "Taxes? They're..."

        "A necessary evil":

            you "Well, I suppose they're a necessary evil. Someone has to fund all the public services that we enjoy, such as the Court torturers and executioners..."

            taxgirl "How sheepish of you. Nevertheless, I'm sure you're not eager to line the King's coffers with your hard-earned gold..."

            you "Well..."

        "An unacceptable powergrab":

            you "Taxes! Ha, I hate taxes! Who needs them? The thieving State, that's who!"

            taxgirl "Exactly! And what did the State ever do for us?"

            sill happy "Well..."

            sill "There's sanitation, medicine, education, foodbanks, public order, irrigation, roads, a fresh water system, public heal-"

            taxgirl "That's right, nothing! My point exactly!" with vpunch

            you "Exactly."

        "Not the fucking point":
            you "Taxes are... not the fucking point! What do you want?" with vpunch

            taxgirl "Easy. I have a proposal for you. A {i}business{/i} proposal."

    taxgirl "See, you're just another upstart in this city, fresh off the boat with a brand new licence. But as soon as you start making any real money, the King's tax collectors are going to flock to you like vultures on a smelly carcass."

    you "Nice image..."

    taxgirl "They'll drive you out of business in no time. But what if..."

    taxgirl "What if I told you there was a way to {i}avoid{/i} the King's taxes entirely?"

    you "Uh? You've got my attention."

    taxgirl "As a sex slave owner, you are entitled to the protection of the Slavers' Guild. And we cast a long shadow in this city. Perhaps you've heard of our leader, Cloud?"

    you "Maybe. Who's that, precisely?"

    taxgirl "Well, even I don't know his exact identity. Cloud is a very discreet man... or woman."

    taxgirl "But Cloud holds half the court under his or her thumb, and rumor has it, even the King himself. Enough to make all your tax worries disappear..."

    you "Great-"

    taxgirl "...provided you pay us protection money."

    you "Doh!" with vpunch

    you "Wait a minute... So in order to avoid the King's tax, I have to pay your Guild's... tax?"

    taxgirl "We really prefer the term 'progressive membership fee'. It gives you access to a range of services, such as the special business lounge at the harbor when waiting for your ship to arrive. There's lobster."
    #
    # taxgirl "You also get modest discounts on a range of things you'll never use..."

    you "*frown*"

    taxgirl "But listen: unlike the King's lackeys, we're not about to bleed you dry. We like our members to thrive, after all."

    you "*sigh* There's no escaping swindlers in this town, I see. I suppose now you're going to say that it's 'an offer that I can't refuse', aren't you?"

    taxgirl "It's an offer that you can't... Wait! That was my line."

    taxgirl "Anyway, only death and taxes are inevitable, my dear. And even so, we've got some very good necromancers these days... So maybe only taxes."

    you "But wait... I have questions."

    taxgirl "Of course."

label tax_intro_menu():

    menu:
        "How much do I have to pay":

            you "Okay, suppose I accept your deal. How would it work?"

            taxgirl "It's very simple. We'll place a magic seal in your accounting books, which will tell us your net income at the end of every month."

            taxgirl "Don't even think of tampering with it - it'll have a very powerful shrinking-dick curse attached with your name on it."

            you "*gulp*"

            taxgirl "I will announce the fee you owe us on the 15th of every month. It's a very simple formula involving 10 different progressive tax brackets, the district you're in, the weather over the last 47 days and in what mood I woke up on that particular morning."

            taxgirl "Also, there is a little bit of membership fee inflation. {b}The membership fee may increase every month.{/b} But this progression will be reset every time you move to a new district."

            you "Uh? Why?"

            taxgirl "Let's say it's a little nudge to keep you moving in the right direction. The guild takes an 'up or out' approach to its membership..."

            taxgirl "It's best to simply remember that {b}the higher your income, the more the 'membership fee' will cost{/b}."

            taxgirl "And also remember that {b}the more time passes in a district, the more it will cost{/b}. But don't worry, there's an upper limit we won't breach."

            jump tax_intro_menu

        "When do I have to pay":

            taxgirl "The fee will be announced on the 15th of every month."

            taxgirl "I will come to collect on {b}the 1st of the next month{/b}. Ample time to prepare the adequate sum."

            you "Grr..."

            jump tax_intro_menu

        "What if I refuse":

            you "Outrageous! And what if I refuse?"

            taxgirl "Oh, you're perfectly entitled to refuse."

            taxgirl "But without protection money, it's possible that a squad of goons headed by a one-eyed ogre called 'Gutspill' will visit your brothel at night, set fire to the place, and chop your manhood off..."

            taxgirl "Unless of course the King's collectors find you first because of an anonymous tip that you're hoarding some treasure, and decide to torture you to know where you stashed your cash."

            taxgirl "Those are all hypotheticals, of course. We wouldn't know anything about that. *smirk*"

            if MC.playerclass == "战士":
                you "Hmpf. I've seen worse in the war."

                taxgirl "You may be a good fighter, but eventually you'll let your guard down... Everyone has to sleep..."

            elif MC.playerclass == "法师":
                you "Oh really? I've got a range of spells I could use to prevent that..."

                taxgirl "Did I mention we have access to some of the best sorcerers in the city? I'm sure you'd hate it if a zombified whore accidentally bit off your manhood..."

            else:
                you "You think? I've got a pet dragon who might have a thing or two to say to that..."

                taxgirl "You shouldn't boast about it too much. Dragonscale boots are all the rage with Zan nobility these days... And monster hunters are a dime a dozen."

            you "Grrr... You're leaving me no choice, are you?"

            taxgirl "Everyone has a choice. You should just make the right one."

            jump tax_intro_menu

        "What happens if I can't pay":

            "Her eyes grow hard."

            taxgirl "Well, if you can't pay, bad things may happen. Exactly how bad will depend on my judgement."

            taxgirl "But know that I am {i}hard{/i} to please..."

            you "..."

            jump tax_intro_menu

        "Fine, I'll pay":
            pass

    you "Fine. I'll pay your fee... *sigh*"

    "She smiles for the first time. A wolfish smile."

    taxgirl "Very good. Then we're in business."

    taxgirl "Since your income is still very modest, we'll only require you to pay a token amount for now... Let's say {b}[NPC_taxgirl.current_tax] denars{/b}."

    you "{b}[NPC_taxgirl.current_tax] denars{/b}?"

    taxgirl "That's right."

    call fade_tax_amount() from _call_fade_tax_amount

    taxgirl "Make sure you have it ready {b}by the 1st of next month{/b}."

    "Tip" "You can check the Guild Fee amount at any time by hovering above the Gold counter."

    hide taxgirl with dissolve
    hide expression room with dissolve

    return



label tax_check(): # Happens on the morning of the 15th of every month starting from district rank 2. Taxgirl announces the tax amount

    $ tx = calculate_tax(NPC_taxgirl.MC_income)
    $ renpy.block_rollback()

    if not NPC_taxgirl.active:
        if tx > 0:
            call tax_intro from _call_tax_intro

            $ NPC_taxgirl.active = True

    else:
        play sound s_chimes

        show taxgirl with dissolve

        $ text1 = rand_choice(["Hello, [MC.name], remember me?", "Hi [MC.name]. It's that time of the month.", "Hi, it's your friendly neighborhood slaver guilder.", "Hello, dear.", "Hi. It's time to pay.", "Good morning."])

        $ taxgirl(text1)

        if tx <= 0:
            taxgirl "Well, it seems like you won't owe us any money for this month. How disappointing. See you next month, then."
            $ NPC_taxgirl.love -= 1

        else:
            if tx < 1000:
                $ text1 = "A trifle."
            elif tx < 5000:
                $ text1 = "A token contribution, as a show of goodwill."
            elif tx < 25000:
                $ text1 = "A modest show of support for our collective welfare."
            elif tx < 50000:
                $ text1 = "A decent effort, I hope you keep this going."
            elif tx < 100000:
                $ text1 = "A sizeable donation, for which the guild will be grateful."
                $ NPC_taxgirl.love += 1
            elif tx < 250000:
                $ text1 = "A valuable contribution to the greater good, for which I will be personally thankful."
                $ NPC_taxgirl.love += 3
            elif tx < 500000:
                $ text1 = "A great effort for our cause, which will place you among our top three contributors."
                $ NPC_taxgirl.love += 6
            else:
                $ text1 = "A King's ransom! No one is a bigger benefactor of the Guild than you. I will be very impressed if you pull this off."
                $ NPC_taxgirl.love += 12

            taxgirl "According to our accountants, you owe us {b}[tx] denars{/b} for last month. [text1]"

            call fade_tax_amount() from _call_fade_tax_amount_1

            taxgirl "Payable in full on the 1st, as usual. I trust you'll have the money ready. Goodbye!"

        hide taxgirl with dissolve


    return


label tax_payment(): # Happens in the evening of the 1st each month if taxes are due

    if NPC_taxgirl.active:
        scene black with fade

        if brothel.get_common_rooms():
            $ room = brothel.get_random_room_pic_path()
        else:
            $ room = "black"

        show expression room at top
        with dissolve

        if NPC_taxgirl.current_tax > 0:
            play sound s_chimes

            show taxgirl with dissolve

            $ text1 = rand_choice([__("Good evening."), __("Hello, ") + MC.name +"。", __("Hi, dear."), __("Knock knock."), __("Hey, ") + MC.name + "。", __("Hi.")])
            $ text1 += " " + __(rand_choice(["Here comes the guild collection.", "Your friendly neighborhood tax collector is here.", "Your guild membership fees are due.", "I hope you have my... the Guild's money ready.", "It's time to pay your dues.", "It's time for the slavers' guild to collect its due.", "I hope you have gathered enough money for protection."]))

            taxgirl "[text1!t]"

            taxgirl "As a reminder, you owe us [NPC_taxgirl.current_tax] denars for last month."

            if pay_tax():
                $ renpy.block_rollback()
                you "Hmph. Here you go."

                call tax_relationship_test from _call_tax_relationship_test

            else:
                $ renpy.block_rollback()
                you "Here is the... Oh."

                call tax_no_money from _call_tax_no_money

            hide taxgirl with dissolve

        else:
            show sill happy with dissolve

            sill happy "It's the 1st! Luckily, the nasty guild woman seems to have forgotten about us this month..."

            sill sad "Perhaps it's because we're broke?"

            hide sill with dissolve

    return


label tax_relationship_test():

    if not NPC_taxgirl.flags["relationship level"] and NPC_taxgirl.love >= 5:

        $ NPC_taxgirl.flags["relationship level"] = 1

        "As you hand the gold over to the guild woman, you feel a jolt of electricity between you and she moans in surprise."

        play sound s_surprise
        with flash

        taxgirl "Ah!"

        you "Uh? That was odd... Are you okay?"

        "She looks flustered, and your trained eye cannot help but notice that her nipples are perking through the thin fabric of her blouse."

        taxgirl "Sure... Give me a moment. It's just a side-effect..."

        you "Side-effect? Of what?"

        taxgirl "The magic. The powers I use to keep your accounts in check, count the gold..."

        taxgirl "You see, I wasn't born with the gift."

        if MC.playerclass == "法师":
            you "Yes, I could feel it in your aura. You're a conduit, aren't you?"

            taxgirl "Yes."

        taxgirl "When I was a kid, I was one of hundreds of street urchins that lurk in the dark alleys of the city."

        taxgirl "I was good at lifting purses... Until I got caught picking the pockets of a gentleman who turned out to be one of the Slavers' Guild's masters."

        taxgirl "By all rights, I should have ended up like them..."

        "She gestures towards the back rooms where your girls are preening themselves for the night."

        taxgirl "...but the master took a liking to me. Thank Shalia, he saw that I was smart, capable and ruthless - good qualities for a debt collector."

        taxgirl "So I rose through the ranks, and made it to senior by the time Cloud came along."

        you "Cloud? So he wasn't always the Guild master?"

        taxgirl "Not at all. He or she came about just a couple of years ago, seemingly out of nowhere."

        you "And he became Grand Master just like that? What of the other masters?"

        "Her lips tighten."

        taxgirl "Let us not discuss {i}that{/i}."

        taxgirl "Anyway. When Cloud became Grand Master, we were told things would change. We were to use magic to speed up the Guild's growth - which worked out splendidly, in hindsight, even though it was met with fierce opposition at the time."

        taxgirl "I volunteered to be made a conduit for Cloud's magical powers, as did most of the Guild's remaining senior officers."

        you "Only the most powerful sorcerers can channel their magic through a conduit..."

        taxgirl "Indeed. Let alone half-a-dozen. Cloud is by far the most powerful being I've ever met."

        you "So you met him? Her? It?"

        taxgirl "I must have, I guess... I was put into a ritual trance, as Cloud bestowed new powers on me. Or something. I don't recall any of it."

        taxgirl "But Cloud is known as something of a trickster, and all such gifts have strings attached. The magic comes with side-effects..."

        you "What side-effects exactly?"

        taxgirl "None that are of concern to you."

        taxgirl "Now, we've wasted enough time with idle chatting. I thank you for your contribution. See you in two weeks."

        you "Hmm..."

    elif NPC_taxgirl.flags["relationship level"] == 1 and NPC_taxgirl.love >= 20:

        $ NPC_taxgirl.flags["relationship level"] = 2

        "As you hand her the large bag of gold, you feel another strong jolt of electricity between you and the air cracks with magic."

        with doubleflash
        play sound s_scream

        show taxgirl:
            linear 0.5 yanchor 0.85 zoom 1.5

        taxgirl "Ahaaa!" with vpunch

        "The guild woman stumbles and clings to you, moaning."

        "You can see beads of sweat running down her forehead. You can't help but enjoy her sweet smell and the feeling of her breasts rubbing against your arm."

        you "Wow... what was that?"

        taxgirl "Aah... I told you... It's a side-effect of the magic I use..."

        you "Ah yes, the magic Cloud gave you, was it?"

        you "Pity, I thought my gold had the power to turn you on... A power I might have wielded irresponsibly."

        taxgirl "Don't be silly."

        "To your regret, she lets go of your arm and straightens up her dress, which was in imminent danger of a wardrobe malfunction."

        show taxgirl:
            linear 0.5 yanchor 1.0 zoom 1.0

        taxgirl "It's a trick on the part of my master, Cloud... A test of my resolve, if you will."

        you "I don't follow..."

        play sound s_sigh

        taxgirl "*sigh* You see, Cloud's magic changed something in me... Now, I can only get aroused by gold - large quantities of it."

        "She says that coldly and matter-of-factly, back to her usual collected self."

        you "You... What?!?" with vpunch

        taxgirl "My sex drive is gone. Instead, I can only get aroused by gold. I guess it's a subtle but effective way to make me work extra hard at my job... Ever since, it's true that I've been very focused."

        you "B-But... What about getting aroused... The traditional way?"

        taxgirl "Not a chance. I've tried all the usual techniques - and many of the less usual ones. To no avail."

        you "That's awful..."

        taxgirl "Yes, well, that ship has sailed. I got used to it. At least I get a pleasant, tingling feeling when you pay me."

        you "I've known a lot of girls that were into money, but not {i}that{/i} into money..."

        taxgirl "Anyway, enough about my libido - or lack thereof. Thank you for your contribution, it was my pleasure..."

        you "Literally."

        taxgirl "Shut up."

    elif NPC_taxgirl.flags["relationship level"] == 2 and NPC_taxgirl.love >= 50:

        $ NPC_taxgirl.flags["relationship level"] = 3

        with doubleflash
        play sound s_orgasm_fast

        show taxgirl:
            linear 0.5 yanchor 0.85 zoom 1.5

        taxgirl "AAAAHAAAH!!!" with vpunch

        with flash

        "As you hand her a massive bag of gold, the guild lady drops into your arms, shivering and screaming."

        you "Wow..."

        "She clings to your neck as she lets the wave of pleasure pass. You feel her erect nipples rubbing against your chest through her dress, and your dick begins to stiffen."

        play sound s_aaah

        taxgirl "Aaah..."

        "She stays in your arms for a minute, avoiding your gaze, catching her breath."

        taxgirl "Sorry about that..."

        you "No problem. I didn't know the gold could cause such a large reaction..."

        taxgirl "Side-effect."

        you "Yes."

        "She hesitates for a moment, then blushes lightly as she lifts her head to look into your eyes."

        taxgirl "Is that what I think it is? Rubbing against my belly?"

        you "Err, well... It's an impulse I can't control, and..."

        taxgirl "Help me."

        you "Uh?"

        taxgirl "Help me. It's been so long since I experienced pleasure... But I think now, I could..."

        you "You mean... Have sex?"

        taxgirl "No."

        "You feel a pang of disappointment."

        taxgirl "I want you to fuck my ass."

        "You feel a burst of hormones. Your cock gets so hard it threatens to pop out of your pants."

        you "What? Come again?"

        taxgirl "I can't... Unless you fuck my asshole."

        you "Whaaat? Why?" with vpunch

        taxgirl "I told you, I've tried many things to regain my libido... The closest I got was using my back hole."

        taxgirl "What can I say, I'm that kind of girl."

        you "Oh..."

        taxgirl "Will you do it?"

        "Instead of answering, you flip her over and lower her panties, placing your hard cock against her butt."

        taxgirl "Hmmm... So you'll do it."

        call taxgirl_anal() from _call_taxgirl_anal

        $ NPC_taxgirl.love += 3


    elif NPC_taxgirl.flags["relationship level"] == 3 and NPC_taxgirl.love >= 100:

        $ NPC_taxgirl.flags["relationship level"] = 4

        with flash
        play sound s_scream_loud

        taxgirl "AAAAH!!!" with vpunch

        with doubleflash

        "As you push a barrel of gold her way, the guild woman is hit by another strong orgasm, fainting on the spot."

        hide taxgirl with dissolve

        "You catch her before she hits the ground. You try and shake her, but she is completely out of it."

        you "Whoah, babe! Wake up!"

        "Picking her up, you bring her to a bed."

        show bg master room at top with dissolve

        "You can feel her heart racing fast, and her breathing is heavy."

        you "Look at you... These magic side-effects really played a number on you."

        "As you lay her down, you notice the love juices streaming down her thighs. Her panties are completely drenched."

        you "I better take these off, Sill will clean them..."

        "The girl moans and moves unconsciously as you remove her panties. As she squirms, her heavy breasts pop out of her tight dress, giving you quite a spectacle."

        you "Ooh... *drool*"

        "You stare absent-mindedly for a while, until you notice that she is awake, looking back at you with glassy eyes."

        taxgirl "Do... Do me."

        you "Uh?"

        taxgirl "Fuck me now, [MC.name]. Use my pussy, I don't care... I want it. Now."

        you "O..."

        you "Of course!!!" with vpunch

        call taxgirl_sex(first=True) from _call_taxgirl_sex

        taxgirl "I suppose I should do something for you too. Look, about the membership fee..."

        you "You're giving me free membership? Hurray!"

        taxgirl "Don't be silly. I can't do that. But I can make sure they remain reasonable."

        you "*sigh* Well, it's still something, I suppose."

        "Your guild membership has been reset, and you will no longer suffer from {b}fee inflation{/b}."

        $ NPC_taxgirl.love += 6

        $ NPC_taxgirl.time_pressure_modifier = 0.0
        $ NPC_taxgirl.flags["disable time pressure"] = True

        taxgirl "I can also give you some more... 'personal' advice, if you want. Just make sure to take care of my needs every once in a while, all right?"

        you "You got it..."

        $ NPC_taxgirl.unlock_trainer()

    elif NPC_taxgirl.flags["relationship level"] == 4:

        "The woman blushes bright red as you hand her the gold, and she doesn't even try to hide her pleasure as an orgasmic wave overcomes her."

        play sound s_aaah

        taxgirl "AAAH!!!" with flash

        "She stares at you with hunger in her normally cold eyes."

        menu:
            taxgirl "Would you... Would you fuck me again?"

            "Fuck her pussy":

                you "I'm not one to turn down a plea for help..."

                call taxgirl_sex() from _call_taxgirl_sex_1

            "Fuck her ass":

                you "Of course, we'll do it your favorite way. Bend over!"

                call taxgirl_anal() from _call_taxgirl_anal_1

            "Not today":

                you "Not today, sorry. I've got a lot on my plate."

    else:
        $ taxgirl(rand_choice(["Hmm, thanks. See you again soon. *smirk*", "Thank you. I'll be on my way then.", "It seems all the gold is, hmm... Accounted for. Nice. See you later, then.", "Hmm... Good, very good. I'll see you again soon.", "Seems like everything's here. Perfect."]))

    return

label taxgirl_anal():

    scene black with fade
    show bg taxgirl anal1 at top with dissolve

    "Pushing her dress aside, the guild woman says nothing as you grab her ass and spread her buttcheeks."

    taxgirl "Hurry up, while I'm still aroused from the magic backlash..."

    "Without further ado, you push your hard cock inside her. Her asshole welcomes you, betraying extensive use."

    show bg taxgirl anal2 at top with dissolve

    play sound s_scream

    taxgirl "Oh, yes..." with hpunch

    play sound s_moans

    "As you start moving back and forth, she seems to concentrate hard on the feeling in her asshole."

    taxgirl "It's good, Oh... Keep going..."

    "Encouraged by her reaction, you spit in her crack to make it slippery, and increase your pace."

    "Her large tits bounce every time you slam your cock inside her."

    taxgirl "Oh, aah, aaah!" with hpunch

    "Her trained asshole easily accommodates the full length of your shaft as you fuck her deeper."

    taxgirl "Oh yes... Faster... Faster!"

    "She moans wildly as you increase your pace again, mercilessly pounding her butt."

    taxgirl "Oh, aah, aah... AAAAAH!!!" with hpunch

    with flash

    play sound s_orgasm

    taxgirl "YYYESSS!!!"

    show bg taxgirl anal3 at top with doubleflash

    "You explode inside her ass, sending her over the edge. She trembles uncontrollably as your cock discharges inside her." with hpunch

    play sound s_mmh

    taxgirl "Oooh... Hmmm..."

    show bg taxgirl anal4 at top with flash

    "Popping your cock out, you spurt the last of your cum on her sexy thighs."

    "You look with satisfaction at the mess you've made."

    scene black with fade
    show bg master room at top with dissolve
    show taxgirl:
        linear 0.5 yanchor 1.0 zoom 1.0
    with dissolve

    taxgirl "Thank you. I hadn't felt like that... in a long time."

    "The woman uses a handkerchief to wipe herself, then quickly arranges her clothes back in order."

    "She is done in a moment, and it looks as if nothing at all happened."

    taxgirl "All right, I believe our business here is done... Thank you for the gold, and... your help with this... Other matter."

    you "Sure, anytime..."

    taxgirl "I shall see you again in two weeks."

    $ MC.change_prestige(5)
    $ unlock_achievement("h taxgirl")

    return

label taxgirl_sex(first=False):

    scene black with fade
    show bg taxgirl sex1 at top with dissolve

    "The guild woman spreads her legs and welcomes you, her pussy still dripping with love juice."

    play sound s_aaah

    taxgirl "Aaah!" with hpunch

    "You drive your cock inside her, and she moans softly as you do."

    play sound s_moans

    taxgirl "Ooh... It's been too long..."

    "She is surprisingly tight, considering how flexible you remember her asshole was, but her pussy is so wet that sliding inside her is no challenge at all."

    taxgirl "Oh yes...." with hpunch

    "You play with her tits and start sucking on her nipples as you fuck her, and she clings to you lovingly."

    taxgirl "I like that... Oh... [emo_heart]"

    taxgirl "Listen, today is a safe day... I want you to release it all inside..."

    "Your cock grows even harder, even though it hardly needed more stimulation."

    show bg taxgirl sex2 at top with dissolve

    taxgirl "Oh, yes! [emo_heart]" with hpunch

    "You are pounding her with abandon now, splashing love juice on the bedsheets, and she doesn't seem to mind at all."

    taxgirl "You are going so deep... Aaaah... Aaah!" with hpunch

    "In spite of the spell's backlash, or perhaps because of it, she seems extremely aroused. She arches her back as you pinch her nipples hard."

    taxgirl "Now! I'm, I'm..."

    show bg taxgirl sex3 at top with flash
    play sound s_orgasm

    taxgirl "AAAAHAAH!!!"

    with doubleflash

    "Her pussy clenches around your cock as she cums, sending you over the top. You burst your hot cum inside her."

    show bg taxgirl sex4 at top with flash

    taxgirl "Ahaaa..."

    taxgirl "This feeling... Perfect..."

    you "That was good..."

    taxgirl "Let's do it again. I can come again."

    you "Uh?"

    taxgirl "Please... Keep going!"

    scene black with fade

    "You both cum a couple more times before she is fully satisfied."

    show bg taxgirl sex3 at top with flash
    play sound s_orgasm

    taxgirl "Again! Aaaaah!!!"

    show bg taxgirl sex5 at top with doubleflash

    "As you cum one last time inside her, filling her up to the brim with hot cum, she grabs the bedsheets tight, looking lost in her feelings."

    play sound s_mmh

    taxgirl "Hmmm..."

    taxgirl "I haven't felt like this in a long, long time..."

    "As you both lay in bed, she looks at the cum dripping out of her belly absent-mindedly."

    taxgirl "You made me feel like a woman again today... I missed it..."

    "You are taken aback as she gives you a bright smile, something you didn't think she was capable of."

    taxgirl "Thank you."

    you "You're welcome. You know we can do this anytime..."

    $ MC.change_prestige(5)

    return

label tax_no_money():
    "The woman's eyes narrow."

    taxgirl "What's that? You haven't got the money?"

    you "I can explain..."

    if not NPC_taxgirl.flags["got second chance"]: # The first time it happens, the player will be given a second chance

        $ NPC_taxgirl.flags["got second chance"] = True
        $ NPC_taxgirl.flags["paid tax"] = False

        taxgirl "All right, I'll give you a chance to make this right. I'll give you a week to come up with the sum..."

        you "Thank y-"

        $ NPC_taxgirl.current_tax = int(NPC_taxgirl.current_tax*1.1)

        taxgirl "...with a ten percent late penalty. You now owe us [NPC_taxgirl.current_tax] denars. Also, you'll have to sign this deed."

        you "What deed?"

        "She hands you a piece of paper that says that if you fail to pay your membership fee in the future, the Guild will repossess your brothel."

        you "*gulp*"

        taxgirl "There is no other way."

        "Reluctantly, you sign the paper."

        taxgirl "I'll see you on the 8th. This better be the first and last time, though..."

        $ calendar.set_alarm(calendar.time + 7, StoryEvent(label="tax_payment", type="night"))

    elif not NPC_taxgirl.flags["paid tax"] or NPC_taxgirl.love < 5:

        "Her face becomes stone cold."

        taxgirl "I have given you a fair warning, but you've ignored it."

        if NPC_taxgirl.love >= 50:
            taxgirl "It breaks my heart that it has come to this, but... I will not betray the guild."

        elif NPC_taxgirl.love >= 20:
            taxgirl "I'm sorry. I thought we had a good relationship going. But business is business."

        taxgirl "You knew the stakes. Pack your stuff. We're keeping the brothel and the slaves."

        you "No! Wait!" with vpunch

        call game_over("Slavers") from _call_game_over_1

    else: # Love is >= 5
        $ NPC_taxgirl.flags["paid tax"] = False

        "She frowns."

        if NPC_taxgirl.love >= 50:

            taxgirl "Listen, you know I like you, but don't screw this up... Don't put me in an impossible situation. *cold*"

            taxgirl "I'll give you seven more days. Please find a way to come up with the money. I don't want to... You know."

        elif NPC_taxgirl.love >= 20:

            taxgirl "Okay, you've been a good boy so far, so I'm inclined to cut you some slack..."

            $ NPC_taxgirl.current_tax = int(NPC_taxgirl.current_tax*1.1)

            taxgirl "I'll give you seven more days, but with a ten percent penalty. You now owe us [NPC_taxgirl.current_tax] denars. Don't screw this up."

        else:
            taxgirl "Perhaps I've been too nice to you. I'll give you seven more days to pay up, but with a twenty percent penalty. You now owe us [NPC_taxgirl.current_tax] denars."

            $ NPC_taxgirl.current_tax = int(NPC_taxgirl.current_tax*1.2)

            taxgirl "Don't make me regret this."

        $ calendar.set_alarm(calendar.time + 7, StoryEvent(label="tax_payment", type="night"))
        $ NPC_taxgirl.love -= 3

    return

## Pet summons ##

label summon_pet(girl):

    if not story_flags["pet untimely demise"]:
        $ story_flags["pet untimely demise"] = 0

    $ story_flags["pet untimely demise"] += 1

    if story_flags["pet untimely demise"] >= 15: # Triggers pet armageddon on the fifteenth cast and more
        call pet_armageddon() from _call_pet_armageddon
        return

    "The portal crackles and wavers for a few seconds, before a form solidifies out of pure chaotic energy."

    $ pic = rand_choice(game_image_dict["Misc"]["pets"])

    scene black with fade
    show expression pic at top
    with dissolve

    "Coming back to her senses, [girl.name] notices the cute critter."

    play sound s_surprise

    call dialogue(girl, "meet cuddly pet") from _call_dialogue_253

    "The sweet little guy scampers out of the gate, looking joyfully at its surroundings."

    if story_flags["pet untimely demise"] == 1:
        gizel smirk "Really? You open a portal and you summon {i}that{/i}? Oh well... It is kind of cute."

        call pet_untimely_demise(story_flags["pet untimely demise"]) from _call_pet_untimely_demise

        gizel surprise "That's... Just... Ew."

    elif story_flags["pet untimely demise"] <= 3:
        gizel surprise "Oh, another pet? I hope it won't go like last time..."

        call pet_untimely_demise(story_flags["pet untimely demise"]) from _call_pet_untimely_demise_1

        gizel "What the... What are the odds?"

    elif story_flags["pet untimely demise"] <= 6:
        gizel surprise "Maybe, just maybe?"

        call pet_untimely_demise(story_flags["pet untimely demise"]) from _call_pet_untimely_demise_2

        gizel "Oh well."

    elif story_flags["pet untimely demise"] <= 8:
        gizel "Don't get your hopes too high..."

        call pet_untimely_demise(story_flags["pet untimely demise"]) from _call_pet_untimely_demise_3

        gizel "Did you know this was coming? You had to guess..."

    elif story_flags["pet untimely demise"] <= 11:
        gizel "Oh no, I don't want to look..."

        call pet_untimely_demise(story_flags["pet untimely demise"]) from _call_pet_untimely_demise_4

        gizel "You're doing this on purpose, aren't you?"

    elif story_flags["pet untimely demise"] <= 13:
        gizel "Ok, now this is getting ridiculous."

        scene black with pixellate

        play sound s_horn

        centered "Intervention!!!{w=3.0}{nw}"

        programmer "Hi, I am BK's programmer."

        programmer "You should know that if you proceed, this cute defenseless supernatural pet will die an excruciatingly painful death."

        menu:
            programmer "Surely, you don't want that?"

            "I do, and don't call me Shirley":
                $ MC.evil += 2

                you "Get out of the way, and leave that fourth wall alone!"

                show expression pic at top
                with dissolve

                call pet_untimely_demise(story_flags["pet untimely demise"]) from _call_pet_untimely_demise_5

                programmer "Does nobody care about the life of fictional pets anymore?"

            "Oh no":

                you "Oh no, I didn't know..."

                programmer "Fine, let us get that little critter to safety then... Oops, where did it go?"

                show expression pic at top
                with dissolve

                call pet_untimely_demise(story_flags["pet untimely demise"]) from _call_pet_untimely_demise_6

                programmer "Oh no... Well, at least you didn't intend to... You didn't, did you?"

    elif story_flags["pet untimely demise"] <= 14:
        gizel "Again??? You're truly heartless, even I have to admit..."

        centered "Intervention!!!{w=3.0}{nw}"

        programmer "OKAY NOW, FOR THE LAST TIME, WON'T YOU LEAVE THESE POOR CRITTERS ALONE?" with vpunch

        you "Too late, hehehe..."

        call pet_untimely_demise(story_flags["pet untimely demise"]) from _call_pet_untimely_demise_7

        you "What? You know it was going to happen anyway..."

        programmer "I bet you get a hard-on watching that Bambi scene..."

    $ MC.evil += 1 + story_flags["pet untimely demise"] // 3

    return

label pet_untimely_demise(nb):

    $ descriptions = [
                        ("You are all so taken with watching the little creature, that you forget about the brazier Gizel set up to warm up the room. The little guy bangs its head on the brazier, accidentally spilling burning coal on itself.",
                        s_fire, "Soon, its fur catches fire, and the poor beast burns itself to death before you have a chance to do anything.", flash),
                        ("The little guy heads straight outside, and your group starts following.",
                        s_crash, "Before you reach the top of the stairs, however, you hear a defeaning noise. The heavy stone lintel above the doorway mysteriously broke, crushing the hapless pet to a bloody pulp.", vpunch),
                        ("The little guy starts heading out, and you eye nervously the repaired lintel, but it holds well enough. You breathe a sigh of relief.",
                        s_thunder, "Oh no!!! Out of nowhere, a lightning strike hits the poor creature as it comes out, reducing it to cinders. How unusual in this season!", flash),
                        ("You have a sense of foreboding as the little creature heads outside. Hesitantly, you follow suit, but the creature is nowhere to be seen.",
                        s_splash, "Oh no!!! Somehow, it fell down the well! Unable to swim, it promptly drowns before you have a chance to rescue it.", vpunch),
                        ("You have a sense of foreboding as the little creature heads outside. Hesitantly, you follow suit, but the creature is nowhere to be seen.",
                        s_sheath, "Oh no!!! It found its way into the toolshed, where it somehow impaled itself on a sharp rake! You try to put it out of its misery with your boot, but only end up making its agony more painful.", vpunch),

                        ("You decide it's best to keep the little creature inside, where it's less dangerous.",
                        s_roar, "Alas, one of Gizel's pet monsters was roaming the hall, and it snatched the poor little critter to make it a snack.", vpunch),
                        ("The small critter stops dead in its track and looks at you in distress, gasping for air. It looks like something is very wrong.",
                        s_fizzle, "You realize the poor guy comes from a dimension where they don't breathe the same air as you do. It promptly suffocates before your very eyes.", None),
                        ("You decide it's best to keep the little creature inside, where it's less dangerous.",
                        s_dodge, "Unfortunately, the poor hapless pet ventured too close to a vent, and was snatched by a creepy tentacle, never to be seen again.", vpunch),
                        ("As the pet comes out of the basement and you brace for the worst, a gust of wind carries the surprisingly light weight animal into the air.",
                        s_gust, "It looks like the creature will be able to land safely, but at the last moment the wind drops and it falls headfirst amidst Gizel's private cactus collection. It dies shredded by cactus thorns, convulsing in pain.", vpunch),
                        ("As the pet comes out of your basement, you hear a sudden flutter of wings.",
                        s_roar, "A giant Roc swoops in and grabs the hapless pet, carrying back it to its nest, where you know it will devour its warm entrails alive.", vpunch),

                        ("The small critter stops in its track and looks at you in distress. It looks like something is very wrong.",
                        s_splat, "It seems the pet comes from a dimension where times flows a lot slower, meaning its lifetime in our dimension is mere seconds. It grows old and decays before your very eyes, before crumbling into a pile of mummified goo.", vpunch),
                        ("As the pet sniffs around the room, you wonder if it isn't a little too close to the large vat of acid you left lying around earlier.",
                        s_bubbling, "It was...", flash),
                        ("Today you have set up a nice layout to welcome the pet into your midst: there are coal braziers, swinging axes hanging from the ceiling, rat poison boxes on the floor and various sharp tools lying around.",
                        s_splat, "Fortunately, the little pet manages to find its way around these various instruments of death and finally reaches the stairs. Sadly, it misses the last step and falls down hard, breaking its neck.", vpunch),
                        ("{nw}",
                        s_sheath, "As soon as the small pet leaps out of the portal, you impale it on your sword.", vpunch),
    ]
    if len(descriptions) < nb:
        $ nb = nb % len(descriptions)
    $ desc1, snd, desc2, trans = descriptions[nb-1]

    "[desc1]"
    if snd:
        play sound snd
    if trans:
        with trans
    "[desc2]"

    hide expression pic with pixellate

    play sound s_scream
    girl.char "EEEEK!!!" with vpunch

    return

label pet_armageddon():

    gizel surprise "Really, again? Come on, you know the usual will happen..."

    play music m_evil

    you "NO... NOT THIS TIME!" with vpunch

    $ renpy.choice_for_skipping()

    if story_flags["pet armageddon"]:
        gizel shy "You're... looking all scary again..."
        play sound s_thunder

    else:
        play sound s_maniacal_laugh
        you "THIS TIME WILL BE... BIGGER!" with vpunch

        gizel shy "What... What's got into you..."

        "At first it seems like the portal isn't reacting, but everyone can feel their skin crawl as a massive well of dark energy builds up."

        play sound s_thunder

        "Distant thunder echoes through the cellar. Gizel and [girl.name] exchange a worried look."

    you "STEP OUTSIDE! NOW!" with vpunch

    hide bg with pixellate

    "Your voice sounds strange even to you. No one dares disobey your command."

    stop music fadeout 3.0

    play music m_rain fadein 3.0

    scene black with fade
    show bg farmland night tall at top with dissolve
    show rain

    "As you come out, you see the skies above are ripped open."

    play sound s_mystery

    if not story_flags["pet armageddon"]:
        you "They're coming for us... I can feel it..."

        "High above the clouds, you see the faint purple glow of a portal opening. Although it is very far, it still looks massive. What manner of beast will come out?"

        "[girl.name] and Gizel shudder in shared horror next to you, but you watch on with glee."

    play sound s_thunder
    with doubleflash

    you "BRACE YOURSELF! HERE THEY ARE!!!"

    "Out of thin air, dark shapes materialize near the portal, falling towards you. At first, you cannot distinguish their features, but soon..."

    $ falling_time = 5.0
    $ pets_on_fire = 0
    $ explode_pet = defaultdict(bool)

    show screen make_it_rain

    play sound s_surprise

    if not story_flags["pet armageddon"]:
        gizel surprise "By the seven hells... Are these... "

        extend "Pets?"

        girl.char "It's raining pets!"

        play sound s_maniacal_laugh

        you "Alleluyah!"

    "Dozens of pets have now appeared, falling down towards the ground. It is time to move forward with the next phase of your plan."

    play sound s_thunder
    with flash

    you "It's time to gather up the storm!"

    hide screen make_it_rain # This is necessary to reset pet count
    show screen make_it_rain

    show evil_lightning

    you "YOU... SHALL... NOT... PASS!!!"

    play sound3 s_scream
    girl.char "AAAAAH!!!"

    "Massive bolts of thunder start striking randomly around you, some hitting the hapless pets and setting them on fire."

    play sound s_meow

    "Magical pet" "AYAYA!!!"

    play sound s_wscream

    "Another magical pet" "AAAAARRRRH!!!"

    "You stand boldly in the eye of the storm, revelling in your dark powers."

    you "NO CUTE CUDDLY ANIMAL SHALL STAND BEFORE ME!!!"

    $ pets_on_fire = 35

    hide evil_lightning
    hide screen make_it_rain

    show bg farmland night tall:
        linear 3.0 yalign 1.0

    show screen make_it_rain(finish_em=True)

    "The girls watch in horror as the burning pets plummet to their deaths, the few surviving ones meeting a gruesome end as they hit the ground."

    play sound s_scream_loud
    girl.char "EEEEK!!!"

    "[girl.name] mercifully faints. Even Gizel is shaken, looking at you with something close to panic."

    "Soon, the ground is littered with the remains of your enemies. Once the scavengers are done with them, their bleached bones will serve as fertilizer for your crops."

    you "That will teach them a lesson!"

    play sound s_maniacal_laugh
    you "Actually... That won't teach them a lesson, BECAUSE THEY BE DEAD!!!" with vpunch

    you "MUHAHAHAHAHAHAHAHAHA!!!!"

    play sound2 s_thunder

    python:
        for i in range(50):
            renpy.hide_screen("pet%i" % i)

    hide screen make_it_rain
    hide bg
    with flash

    programmer "OK, FINE! We get it, you evil bastard! Here, take your evil points and stop it already!!!"

    $ MC.evil += 1000
    $ test_achievement("evil")
    $ test_achievement("evil") # Twice to unlock the second achievement if needed
    $ unlock_achievement("pet armageddon")
    $ story_flags["pet armageddon"] = True

    hide screen make_it_rain

    scene black with fade

    return

## Sanity events ##

label is_broken(girl):

    if not girl in MC.girls + farm.girls: # Avoids this event proc-ing several times (just in case)
        return


    "Gizel asked for you to come to the farm this morning. She said you'd better hurry."

    scene black with fade

    show bg pen with dissolve

    gizel upset "{nw}"

    with vpunch

    call dialogue(girl, "sanity broken") from _call_dialogue_254

    gizel upset "It seems using her to conduct evil powers have cost her the last of her {a=help:sanity}sanity{/a}... She's good for nothing now. She'll only harm herself."

    $ MC.rand_say(("gd: Oh no... Is she really gone? Isn't there something we can do?", "ne: Damn, that sucks... I never intended it to end that way...", "ev: That stupid cunt! How am I to recoup my investment now?"))

    gizel angry "Like I said, she's good for nothing at the brothel or even the farm in that state. You do have a few options, though."

    if not story_flags["broken first"]:
        $ story_flags["broken first"] = True

        label broken_explain_options():
            you "Please explain my options. Is there any way we could heal her mind?"

            gizel angry "Well, you could send her to a {b}lunatic asylum{/b}. That's what people do when their relatives go cuckoo. There's a small chance her mind will heal a little there, although it's just as likely they'll drive her even crazier. Either way, it's going to cost you a pretty denar."

            gizel smirk "Is that dumb slut [girl.name] really worth this much to you?"

            you "What are the other options?"

            gizel normal "Well, you could of course just {b}sell her{/b}. But in that state, good luck finding potential buyers. She's more likely to harm them or herself than be of any use as a slave. Only someone really desperate or ruthless would buy her."

            gizel "Either way, she won't fetch a good price at all."

            you "Anything else I could do?"

            gizel "Well, if you won't pay for her treatment or sell her, I guess you could just {b}put her on the street{/b}."

            gizel "She can whore herself out in an alley somewhere, finding her own customers, and we'll take a cut in exchange for some food and shelter."

            you "What, in her state? You said she was a danger to herself and others?"

            gizel "She'll probably be pretty terrible as a street whore, but she'll have to do it to survive. And no one will know she works for you, so if she snaps or harms a customer, your reputation won't suffer."

            gizel "I can just have her stay in the old barn, far from the other girls, and give her some of the minion's feed."

            $ MC.rand_say(("gd: Cold...", "ne: Tough, but... I guess I can see the advantages.", "ev: Ha! Perfect."))

            you "But I thought only licensed brothels were authorized in Zan?"

            gizel "Oh, sure, but she won't officially work for us. She will get caught eventually, or disappear, they all do. But by the time this happens, you will have made some money."

            gizel "By the way, the old barn could do with some repairs. If you can get a craftsman to do some improvements, it might improve her efficiency a bit."

            you "I see."

            gizel smirk "So here are your options: paying for the asylum, selling her, or putting her on the streets. What will you choose?"

    $ price = girl.get_price("sell", raw=True)
    $ asylum_cost = price // 2
    $ auction_min_price = price // 20

    label broken_menu:

        menu:
            extend ""

            "Send her to the asylum for 1 month (cost: {image=img_gold_24}[asylum_cost])":
                if renpy.call_screen("yes_no", "Do you want to send her to the lunatic asylum (small chance of recovering some sanity) for one month at the cost of %i gold?" % asylum_cost):

                    gizel angry "Fine, I'll have her sent there. Waste of money if you ask me, but it's your call."

                    play sound s_gold
                    $ MC.gold -= asylum_cost

                    # Dice is thrown when the alarm is set to discourage save scumming
                    $ relinquish_girl(girl)
                    $ calendar.set_alarm(calendar.time + 28, StoryEvent(label = "asylum_return", call_args = (girl, dice(100)), order = 1))

                    scene black with fade

                    "[girl.fullname] has been sent to the lunatic asylum for a month."

                    return

            "Sell her to the highest bidder (auction starting price: {image=img_gold_24}[auction_min_price])":
                if renpy.call_screen("yes_no", "Are you sure you want to sell her (starting auction price: %i gold)?" % auction_min_price):

                    $ gain = renpy.random.randrange(auction_min_price, auction_min_price*3)
                    $ MC.gold += gain
                    $ relinquish_girl(girl)
                    $ bidder = rand_choice(["a lonely drifter", "a spice addict", "a cruel slavedriver", "a perverted old man", "a down-on-his-luck nobleman", "a monstrous half-orc", "a stern priest", "a merciless pimp", "a shady criminal", "a fearful barbarian", "a disfigured soldier"])
                    $ motive = rand_choice(["He said he would have her live from scraps in his backyard.", "He gave you a dangerous look when you asked him what he intended to do with her.", "He said he would use her as a human toilet.", "He had madness in his eyes.", "He said she was a present for his dog.", "He said it was 'for a friend'.", "He said he would sedate her and use her in orgies.", "He laughed cruelly when you asked what he intended to do with her.", "He said she would be a slave to his other slaves.", "He said she was needed for 'an experiment'", "He said he would get her stuck in his wall, whatever that means.", "He said he wouldn't need her long anyway."])

                    $ renpy.block_rollback()

                    call screen increment_display("Auction girl", "You sold " + girl.fullname + " to " + bidder + " for %s gold.\n" + motive, "bg slave market11", "side slavegirl1", startv=auction_min_price, stopv = gain)

                    gizel "Right, let's just get rid of her now. A little money is still better than nothing."

                    scene black with fade

                    $ MC.evil += 1

                    "[girl.fullname] has been sold to the highest bidder."

                    return

            "Keep her as a street whore (small daily income)":
                if renpy.call_screen("yes_no", "Are you sure you want to turn her into a street whore? (she will live in the farm barn, generating a small daily income and no longer counting as one of your girls)"):

                    gizel "Fine. I'll keep her in the barn where she can't disturb anyone, for as long as she is able to work."

                    $ relinquish_girl(girl)
                    $ MC.street_girls.append(girl)

                    return

            "Explain my options again":
                jump broken_explain_options

        jump broken_menu


label asylum_return(girl, score):

    scene black with fade
    show bg asylum at top with dissolve

    "You received some news from the lunatic asylum."

    if score > 60: # Restored some sanity
        girl.char "M-Master? A-A-Am I free to go?"

        $ girl.full_rest()
        $ girl.sanity += dice(6, 2)

        "It seems [girl.fullname] is doing slightly better after spending some time in confinement. Her {b}{a=help:sanity}sanity{/a}{/b} has improved a little."

        nun "She is well-rested, but please be careful next time. Whatever ou have been doing to that poor slave, she was an inch from losing her mind."

        $ MC.rand_say(["ev: Hmph... *shrug*", "gd: I'm sorry. I will take good care of her.", "ne: Noted. Can we go, now?"])

        call acquire_girl(girl, context = "asylum") from _call_acquire_girl

    elif score > 20: # No change
        girl.char "Gwah... GWAHAHAH!!! Who are you?? Go away!!!" with vpunch

        nun "I'm sorry, we've tried all of the usual techniques but her sanity hasn't recovered. Perhaps if we keep trying, we could heal her mind?"

        $ price = girl.get_price("sell", raw=True)
        $ asylum_cost = price // 2
        $ auction_min_price = price // 20

        menu:
            "Keep her at the asylum for another month (cost: {image=img_gold_24} [asylum_cost])":
                play sound s_gold
                $ MC.gold -= asylum_cost

                nun "Fine, we'll keep her here to recover and heal. There are a few spells we could try..."

                # Dice is thrown when the alarm is set to discourage save scumming
                $ calendar.set_alarm(calendar.time + 28, StoryEvent(label = "asylum_return", call_args = (girl, dice(100)), order = 1))

                scene black with fade

                "[girl.fullname] will be kept in the lunatic asylum for another month."

            "Sell her cheap (starting price: {image=img_gold_24} [auction_min_price])":

                nun "Well, it's your prerogative as her Master... I don't expect many people will want her in that state, though."

                $ gain = renpy.random.randrange(auction_min_price, auction_min_price*3)
                $ MC.gold += gain
                $ bidder = rand_choice(["a lonely drifter", "a spice addict", "a cruel slavedriver", "a perverted old man", "a down-on-his-luck nobleman", "a monstrous half-orc", "a stern priest", "a merciless pimp", "a shady criminal", "a fearful barbarian", "a disfigured soldier"])

                $ renpy.block_rollback()

                call screen increment_display("Auction girl", "You sold " + girl.fullname + " to " + bidder + " for %s gold.", "bg slave market11", "side slavegirl1", startv=auction_min_price, stopv = gain)

                $ MC.evil += 1

                scene black with fade

                "[girl.fullname] has been sold to the highest bidder."

            "Free her":
                you "Just let her go. I have no need for her anymore."

                nun "But Sir... In that state, she will be a danger to herself and others..."

                you "Not my problem. You're welcome to give her room and board for free, if you care so much."

                nun "..."

                scene black with fade

                girl.char "W-Where am I going? What is going on? AAAH!!!" with vpunch

                "[girl.fullname] has been thrown onto the street. You won't hear about her any more."

                $ MC.evil += 2

    else: # Gone mad
        play sound s_roar
        girl.char "GYAAAARH!!! UWAAAARH! RAAAAH!! *drool*" with vpunch

        nun "That young lady has turned into one of the seven devils themselves! She has gone completely mad!"

        you "She did; that's what I'm paying you for."

        nun "No, I mean now she is completely out of control! There is nothing more we can do, the last shock spells have left her completely unhinged, she injured her handler."

        play sound s_shatter
        with vpunch

        nun "That's it, we're kicking her out. I'm sorry."

        you "..."

        scene black with fade

        "[girl.fullname] has gone stark raving mad and was thrown onto the street. You won't hear about her anymore."

        $ MC.good -= 1

    return

label asylum_no_room(girl):
    nun "I'm sorry but it seems you are unable to host her at the time. You could always extend her stay, but we will need you to cover the extra cost."

    menu:
        "Let her stay one more day (50 gold)":
            $ price = 50
            $ duration = 1

        "Let her stay three more days (150 gold)":
            $ price = 150
            $ duration = 3

        "Let her stay one more week (350 gold)":
            $ price = 350
            $ duration = 7

        "Free her":
            you "Just let her go. I have no need for her anymore."

            call dialogue(girl, "freed") from _call_dialogue_255

            return "freed"

    $ nun("Very well, we will keep her resting for %s more day%s." % (duration, plural(duration)))

    play sound s_gold
    $ MC.gold -= price
    $ calendar.set_alarm(calendar.time + duration, StoryEvent(label="asylum_return2", call_args=[girl], type="morning"))

    return False

label asylum_return2(girl):

    scene black with fade
    show bg asylum at top with dissolve

    nun "Have you come to take [girl.fullname] off our hands?"

    call acquire_girl(girl, context = "asylum") from _call_acquire_girl_1

    return

label girl_disappeared(girl):

    $ MC.street_girls.remove(girl)
    $ excuse = rand_choice(["she was abducted by an ogre party, or so I'm told.", "she was a spice addict and couldn't keep her habit in check.", "she was arrested by the guard and thrown into a dank cell to rot.", "she bought passage onto on a ship, never to return again.", "she dove into the sea, screaming. Her body was never found.", "she fell into a rip in spacetime.", "a horny demon abducted her into another dimension.", "she was last seen boarding the carriage of an excentric noble, never to be seen again", "she was kidnapped by a foreign diplomat who took her home with him.", "she joined a mysterious cult and vanished", "she had monstrous debt, and got kidnapped by the mob.", "she was taken by a group of thugs, who dragged her into the sewers.", "she bought a weapon and left on a quest.", "she won the royal lottery.", "she ran naked into the woods, never to be seen again.", "she roughed up a priest, and was taken away by Arios Knights.", "she stabbed a rich guy, and was thrown in jail for life.", "she became a nun and joined the crusade.", "she married a poor fool.", "a jealous sorceress turned her into a toad.", "she was abducted by imps, courtesy of some mage.", "she got in league with the wrong people.", "she was accused of seddition and conspiring against the crown.", "she was taken in by relatives.", "she got jumped by rogue slavers who rebranded her.", "she left Zan for good to bring her trade to a different city.", "she became a brothel owner of her own."])

    gizel normal "The street whore [girl.fullname] has disappeared tonight. It seems [excuse]. I guess we won't see her ever again."

    you "Oh well."

    return

label acquire_girl(girl, price=0, context="generic"):
    # Price set to zero means it is not a buying situation. Context can be: generic, free, slavemarket, asylum

    $ result = False

    # 1. Makes sure MC has money and room

    if isinstance(girl, Girl):
        if len(MC.girls) < brothel.bedrooms:
            if price:
                if MC.has_gold(price):
                    $ result = renpy.call_screen("yes_no", "Do you really want to buy [girl.fullname] for [price] gold?")
                else:
                    if context == "slavemarket":
                        slavegirl1 "Sorry Master, but you don't have enough gold to buy [girl.fullname]."
                    else:
                        you "Shoot, I don't have enough gold..."
            else:
                $ result = True

        else:
            sill sad "Sorry Master, I'm afraid you don't have room in your brothel for another girl."

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
                        pass
    else:
        $ raise AssertionError("[girl.name] is not a Girl object.")

    # 2. Transfer girl from giver to taker

    if result:
        $ MC.girls.append(girl)

        if context == "free":
            python:
                game.free_girls.remove(girl)
                game.track("free girl acquired")
                for loc in all_locations:
                    if girl in loc.girls:
                        loc.girls.remove(girl)

        elif context == "slavemarket":
            $ MC.gold -= price
            play sound s_gold

            $ slavemarket.girls.remove(girl)
            $ girl.original_price = price
            $ game.track("gold spent slavemarket", price)

            slavegirl1 "You just bought [girl.fullname]. I hope you will enjoy her."

            call dialogue(girl, "bought") from _call_dialogue_90

        $ renpy.block_rollback()

        if result == "farm":
            $ farm.programs[girl] = FarmProgram(girl)
            call send_to_farm(girl, can_beg=False, can_cancel=False) from _call_send_to_farm_4

        hide screen girl_profile
        hide screen girl_stats
        hide screen button_overlay

        python:
            girl.location = None
            girl.set_job(None)
            girl.set_workdays()
            girl.refresh_pictures()

            girl.log["acquired"] = calendar.time
            girl.track_event("acquired", arg=girl.name)

        $ test_achievements(["free girl acquired", "originals", "slaves", "naked", "rank B", "rank A", "rank S", "rank X"])

        $ selected_girl=None
        $ renpy.block_rollback()

    if not result and context == "asylum":
        call asylum_no_room(girl) from _call_asylum_no_room

    return result


label reset_room_capacity():
    python:
        for room in brothel.rooms.values():
            room.update_cust_limit(silent=True)
            notify(room.name.capitalize() + ": Room capacity reverted to normal")

    return

label exhaust_girl(girl, super, hurt_chance=1):
    scene black with fade

    play sound s_crash

    $ girl.energy = 0
    $ girl.exhausted = True
    $ girl.resting = True
    $ update_effects()

    "[girl.fullname] suddenly collapses from exhaustion."

    if super:
        if dice(6) >= hurt_chance:
            $ chg = girl.get_hurt(dice(3))

            if chg:
                "{color=[c_red]}Unfortunately, she hurt herself in the fall, and will need to rest for [chg] days.{/color}"

    return


## END OF BK EVENTS FILE ##
