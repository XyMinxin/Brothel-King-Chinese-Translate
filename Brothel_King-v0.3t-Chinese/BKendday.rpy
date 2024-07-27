####            END DAY ROUTINE                ####
##          Managing and displaying the          ##
##            different night events             ##
####                                           ####


#### DECLARATIONS ####

## DICE IMAGES ##

image img_dice1 = ProportionalScale("UI/dice1.webp", *res_tb(20))
image img_dice2 = ProportionalScale("UI/dice2.webp", *res_tb(20))
image img_dice3 = ProportionalScale("UI/dice3.webp", *res_tb(20))
image img_dice4 = ProportionalScale("UI/dice4.webp", *res_tb(20))
image img_dice5 = ProportionalScale("UI/dice5.webp", *res_tb(20))
image img_dice6 = ProportionalScale("UI/dice6.webp", *res_tb(20))

#### END DAY ####


init python:
    class NightChangeLog(object):

        def __init__(self, title="", col=c_white):
            self.entries = []
            self.add(title, "title", col)

        def add(self, *args, **kwargs):
            self.entries.append(NightChangeEntry(*args, **kwargs))

        def adjust_separators(self):

            self.entries[-1].separator = ""

            for i in range(len(self.entries) - 1):
                if self.entries[i].type == "list" and self.entries[i+1].type != "list":
                    self.entries[i].separator = ""

        def merge(self, change_log):
            self.entries += change_log.entries

        def has_changes(self):
            return len(self.entries) > 1

    class NightChangeEntry(object):
        def __init__(self, msg, type="normal", col=c_white, ttip_title="", ttip="", before_separator=None, separator=None):
            self.msg = msg
            self.type = type
            if col in result_colors:
                self.color = result_colors[col]
            elif col in event_color:
                self.color = event_color[col][6:12]
            else:
                self.color = col

            if not self.color.startswith("#"):
                raise AssertionError("Wrong color code. Error with entry %s, type %s, ttip_title: %s, ttip: %s, color: %s" % (msg, type, ttip_title, ttip, self.color))

            self.ttip_title = ttip_title
            self.ttip = ttip
            self.size = {"title" : res_font(24), "header" : res_font(18), "list" : res_font(14), "normal" : res_font(14)}[type]
            if before_separator:
                self.before_separator = before_separator
            else:
                self.before_separator = {"title" : "", "header" : "\n", "list" : "", "normal" : ""}[type]
            if separator:
                self.separator = separator
            else:
                self.separator = {"title" : "", "header" : "", "list" : ", ", "normal" : ""}[type]
            if type in ("title", "header"):
                self.bold = True
            else:
                self.bold = False

screen night_right(change_log):

    layer "screens"

    tag right_panel

    if change_log:
        viewport xsize 1.0 xalign 0.0 ysize 1.0:
            mousewheel True
            draggable True
            scrollbars "vertical"

            vbox:
                for entry in change_log.entries:
                    if entry.ttip:
                        button style "inv_no_padding" action NullAction():
                            hovered Show("night_ttip", title=entry.ttip_title, ttip=entry.ttip)
                            unhovered Hide("night_ttip")

                            text (entry.before_separator + entry.msg + entry.separator) size entry.size color entry.color bold entry.bold
                    else:
                        text (entry.before_separator + entry.msg + entry.separator) size entry.size color entry.color bold entry.bold

screen night_ttip(title="", ttip=""):

    layer "screens"

    zorder 10

    frame background c_ui_darkblue xmaximum 0.225 xalign 0.79 xanchor 1.0 yalign 0.1 yanchor 0.0 padding(xres(12), yres(12)):
        has vbox xalign 0.5 yalign 0.5

        if title:
            text title
            text "" size 16

        if is_string(ttip):
            text ttip size 20
        elif isinstance(ttip, NightChangeLog):
            use night_right(ttip)

screen night(event_pic = None, event_bg = None, changes = "", has_log = True): # event_pic can be an object or a string

    # layer "master" # This excludes this screen from being hidden when middle-click is used

    default show_log = False

    frame xfill True yfill True:
        background "black"

        hbox:

            spacing 6

            frame:
                xalign 0.0
                yalign 0.0
                xpadding 0
                ypadding 0

                if renpy.get_screen("say"):
                    xsize int(0.8*config.screen_width)
                    ysize yres(615)
                    if persistent.dark_night_UI:
                        background c_ui_darker
                else:
                    background None
                left_margin 6
                ymargin 2
                xfill True
                yfill True

                if show_log:
                    use night_log(log)

                else:
                    if renpy.get_screen("say"):
                        $ x = res_event_width
                        $ y = res_event_height
                    else:
                        $ x = config.screen_width
                        $ y = config.screen_height

                    use show_event(event_pic, x, y, bg=event_bg)

            if renpy.get_screen("say"):
                frame:

                    background c_ui_dark

                    xalign 1.0
                    yalign 0.0

                    ysize 0.8

                    right_margin 6
                    ymargin 6

                    xfill True
                    yfill True

                    has vbox spacing 10

                    xfill True

                    if has_log:

                        if show_log:
                            $ text1 = "隐藏日志"

                        else:
                            $ text1 = "显示日志"

                        textbutton text1 ymargin 10:
                            xalign 0.5
                            xsize xres(120)
                            text_size res_font(18)
                            action ToggleScreenVariable("show_log")

                    if isinstance(changes, NightChangeLog):
                        use night_right(changes)
                    else:
                        text "Results"
                        text changes size res_font(18)


screen night_old(event_pic = None, event_bg = None, changes = "", has_log = True): # event_pic can be an object or a string

    tag show_screen

    layer "master" # This excludes this screen from being hidden when middle-click is used

    # default show_ui = True
    #
    # if show_ui:
    #     key "mouseup_2" action ToggleScreenVariable("show_ui") capture False     #, ToggleScreen("say")), renpy.curried_call_in_new_context("_hide_windows"), HideInterface(), renpy.curried_invoke_in_new_context(ui.interact, suppress_overlay=False, suppress_window=True) all don't work
    # else:
    #     key "mouseup_2" action ToggleScreenVariable("show_ui") capture False     #, Function(renpy.get_reshow_say))


    if event_pic:
        key "K_BACKSPACE" action Function(toggle_ignore_pic, event_pic)
        on "show" action Function(unlock_pic, event_pic) # This is how the game tracks that this particular picture has been seen.


    default show_log = False

    hbox:

        spacing 6

        frame:
            xalign 0.0
            yalign 0.0

            if renpy.get_screen("say"):
                xsize int(0.8*config.screen_width)
                ysize yres(615)
            else:
                background None
            left_margin 6
            ymargin 2
            xfill True
            yfill True

            if show_log:
                use night_log(log)

            else:
                if renpy.get_screen("say"):
                    $ x = res_event_width
                    $ y = res_event_height
                else:
                    $ x = config.screen_width
                    $ y = config.screen_height

                if event_bg: # Adds a bg behind the main pic
                    fixed:
                        add event_bg.get(x, y) xalign 0.5
                        if is_string(event_pic):
                            add event_pic xalign 0.5
                        else:
                            add event_pic.get(x, y) xalign 0.5

                elif event_pic:
                    add event_pic.get(x, y) xalign 0.5 yalign 0.5

                    if debug_mode and renpy.get_screen("say"):
                        frame background c_ui_dark:
                            has vbox
                            text "Attempt: " + str(game.last_pic["attempts"]) size res_font(14)
                            text "Search tags: " + and_text(game.last_pic["tags"]) size res_font(14)
                            text "AND tags: " + and_text(game.last_pic["and_tags"]) size res_font(14)
                            text "AND NOT tags: " + and_text(game.last_pic["not_tags"]) size res_font(14)

        if renpy.get_screen("say"):
            frame:

                background c_ui_dark

                xalign 1.0
                yalign 0.0

                ysize 0.8

                right_margin 6
                ymargin 6

                xfill True
                yfill True

                has vbox spacing 10

                xfill True

                if has_log:

                    if show_log:
                        $ text1 = "隐藏日志"

                    else:
                        $ text1 = "显示日志"

                    textbutton text1 ymargin 10:
                        xalign 0.5
                        xsize xres(120)
                        text_size res_font(18)
                        action ToggleScreenVariable("show_log")

                if isinstance(changes, NightChangeLog):
                    use night_right(changes)
                else:
                    text "Results"
                    text changes size res_font(18)

screen night_log(log, use_filter=False):

    layer "screens"

    vbox spacing 10 ysize 0.85:
        text log.date color c_darkbrown bold True
        if use_filter:
            frame background c_ui_light xfill True:
                has hbox
                text "Filter: " size res_font(22) color c_brown
                input size res_font(22) color c_darkorange changed(log.filter)
        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"

            text log.get_filtered_report() size res_font(18) color c_brown


label end_day:

    $ debug_night_text = [] # Attempt to debug farm text bug

    call sill_checks() from _call_sill_checks

    if not _return:
        jump brothel

    hide screen home
    hide screen tool
    hide screen shortcuts
    with dissolve

    stop music fadeout 3.0

    ## Clear memory (as suggested by Jman)
    $ renpy.free_memory()

#### PLAYING CONDITIONAL EVENTS ####

    python:

        check_events = []

        for girl in MC.girls + farm.girls + game.free_girls:
            if girl.init_dict["background story/night_label"]:
                check_events.append((girl, girl.init_dict["background story/night_label"]))

        ## AUTO-TRAINING ##
        for girl in list(brothel.master_bedroom.girls): # Using list() so the 'for' loop doesn't break when removing a girl
            if girl in MC.girls:
                check_events.append((girl, "auto_train"))
            else:
                brothel.master_bedroom.girls.remove(girl)

    while check_events:
        $ girl, lbl = check_events.pop(0)

        if renpy.has_label(lbl): # Problem: Game will still crash if the label doesn't allow for the girl argument
            call expression lbl pass (girl=girl) from _call_expression_3
        else:
            "System" "Label: {color=[c_red]}[lbl]{/color} doesn't exist (Custom girl: {color=[c_red]}[girl.path]{/color})."

    call play_events(_type = "night") from _call_play_events


#### SHOWING NEW MOON ####

    $ renpy.block_rollback()

    if calendar.day == 1:
        call new_moon() from _call_new_moon

    scene black with Fade(0.15, 0.3, 0.15)

#### PREPARING GIRLS ####

    ## Prepare

    $ night_early = NightChangeLog(title="夜幕降临", col=c_lightorange)

    python:
        if not logs[calendar.time]:
            log = logs[calendar.time] = Log(calendar.time)
        else:
            log = logs[calendar.time]

        # Clears older logs after 30 day (garbage collection)
        if calendar.time-30 in logs:

            del logs[calendar.time-30]

        perform_events = []
        night_text = ""

        latest_ent_match = [[], [], [], "job"]
        latest_wh_match = [[], [], [], "whores"]

    ## Autocast spells (NIGHT)


        spell_success = []
        spell_fail = []

        for spell in MC.known_spells:

            res, cast_text = MC.autocast(spell, "night")

            if res:
                if res == "success":
                    spell_success.append(spell)
                else:
                    spell_fail.append(spell)

                log.add_report(cast_text)

        if spell_success or spell_fail:
            night_early.add("自动释放的法术", "header")

            if spell_success:
                for spell in spell_success:
                    night_early.add("Success: ")
                    night_early.add(spell.name, "list", col="good", ttip=spell.description)
            if spell_fail:
                night_early.add("Failed: ")
                night_early.add(spell.name, "list", col="bad", ttip=spell.description)

        update_effects()


    ## Get working girls


        # night_early.add("Activity Report:", "header")

        working_girls = []
        striking_girls = []
        resting_girls = []
        away_girls = []
        sick_girls = []

        job_girls = []
        whores = []

        for girl in MC.girls:
            if girl.works_today():

                ## Autorest check

                if girl.energy < autorest_limit:
                    log.add_report("{color=[c_red]}" + girl.fullname + " 的体力低于阈值，自动被安排去休息。{/color}")
                    resting_girls.append(girl)
                    girl.add_log("rest_days")

                ## Health check

                elif girl.health_check() == "sick":
                    sick_girls.append(girl)
                    girl.add_log("sick_days")

                else:
                    # Sanity check
                    if girl.job == "whore" and not girl.does_anything():
                        renpy.say("", "[girl.fullname] 不能做妓女，因为她拒绝做任何性行为。")
                        working_girls.remove(girl)
                        striking_girls.append(girl)
                        girl.add_log("work_days", -1)
                        girl.add_log("rest_days")

                    elif girl.obedience_check():
                        girl.add_log("work_days") # Add log is the function that traces girl activity for the statistics tab

                        working_girls.append(girl)

                        if girl.job == "whore":
                            whores.append(girl)
                            girl.add_log("whore_days")

                        elif girl.work_whore and girl.does_anything():
                            job_girls.append(girl)
                            whores.append(girl)
                            girl.add_log("work_whore_days")

                        else:
                            job_girls.append(girl)
                            girl.add_log(girl.job + "_days")

                    else:
                        striking_girls.append(girl)
                        girl.track_event("disobey", arg=girl.job)
                        girl.add_log("strike_days")

            elif girl.away:
                away_girls.append(girl)
                girl.add_log("away_days")

            else:
                if girl.farm or girl.job == "farm": # Catches farm girls that would erroneously end up in MC.girls (shouldn't happen)
                    girl.set_job(None)

                resting_girls.append(girl)
                girl.add_log("rest_days")

        renpy.random.shuffle(job_girls)
        renpy.random.shuffle(whores)















        sick_text = ""

        if sick_girls != []:
            if len(sick_girls) == 1:
                sick_text += "\n{color=[c_red]}%s 生病了。{/color}" % sick_girls[0].name
            else:
                sick_text += "\n{color=[c_red]}%s 生病了。{/color}" % and_text([g.name for g in sick_girls])

    ## Apply advertisement

        log.rep = brothel.rep

        if working_girls: # Open

            # Reputation change from advertisement

            old_rep = brothel.rep
            raw_rep, bonus_rep, decay_rep = brothel.get_adv_reputation()

            pony = 0
            adv_girls = []
            for girl in working_girls:
                if girl.get_effect("special", "ponygirl"):
                    pony += 2 * girl.rank
                elif girl.has_perk("Bunny Girl") or girl.has_perk("Rules of Attraction"):
                    adv_girls.append(girl)

            bonus_rep += pony
            rep_change = raw_rep + bonus_rep + decay_rep

            chg = round_int(brothel.change_rep_nightly(rep_change))

            if round_int(brothel.rep) != old_rep:
                rep_text = __("你的青楼名声从 %s 变为 %s。" % ('{:,}'.format(round_int(old_rep)), '{:,}'.format(round_int(brothel.rep))))
            else:
                rep_text = __("你的青楼名声保持不变 (") + '{:,}'.format(round_int(brothel.rep)) + ")。"

            night_early.add("青楼名声:\n%s (%s)" % (str_int(brothel.rep) + "/" + str_int(brothel.max_rep), plus_text(chg, color_scheme="rep")), "header", ttip_title = "青楼报告", ttip = rep_text)

            night_early.add("宣传效果: +%s" % str_dec(raw_rep))
            if bonus_rep >= 1:
                night_early.add("名声奖励: +%s" % str_dec(bonus_rep))
            if decay_rep <= -1:
                night_early.add("名声衰减: %s" % plus_text(decay_rep))

            log.add_report(event_color["rep"] % rep_text)

            ad_pic = None

            if dice(6) >= 6 and pony:
                ad_pic = "events/" + rand_choice(pony_pics)
                night_text += "{color=[c_pink]}今晚不醉不归!{/color}\n"

            elif brothel.get_effect("special", "demon advertising"):
                ad_pic = rand_choice(game_image_dict["Misc"]["succubi"])
                night_text += "{color=[c_softpurple]}你的恶魔盟友使用他们的超自然魅力吸引了更多的顾客来你的青楼。{/color}\n"

            elif adv_girls:
                adv_girl = rand_choice(adv_girls)
                ad_pic = adv_girl.get_pic("model", "profile", naked_filter=True, soft=True)
                night_text += "%s: {color=[c_pink]}'%s'{/color}\n" % (adv_girl.name, __(adv_girl.pick_dialogue("advertise").line))

            elif brothel.advertising > 0:
                night_text += __("{color=[c_pink]}'先生们!欢迎光临，要不要试试我们店里的特色~ *咯咯*'{/color}\n")

            if not ad_pic:
                if brothel.advertising > 0:
                    adv_index = min(int(math.ceil(brothel.advertising / (5.0+game.chapter))), 5)
                    ad_pic = "events/" + rand_choice(advertising_pics[adv_index])
                else:
                    ad_pic = "events/" + rand_choice(night_pics)

            night_text += sick_text

            # Working girls logging

        ## Alert if striking girls
        if farm.girls:
            night_early.add("女孩: %i" % len(MC.girls + farm.girls), "header", ttip = "你的青楼和农场里有 %i 个女孩." % len(MC.girls + farm.girls), ttip_title="女孩报告")
        else:
            night_early.add("女孩: %i" % len(MC.girls), "header", ttip = "你的青楼里有 %i 个女孩." % len(MC.girls), ttip_title="女孩报告")


        if working_girls:
            line = event_color["a little good"] % ("工作: %s" % len(working_girls))
            ttip = list_text([g.fullname for g in working_girls])
            night_early.add(line, ttip=ttip, ttip_title = event_color["a little good"] % "今天工作")

            for girl in working_girls:
                log.add_report(girl.fullname + __(" 今天的工作是 ") + __(girl_related_dict[girl.job]) + ".")

        if sick_girls:
            line = event_color["bad"] % ("生病的女孩: %s" % len(sick_girls))
            ttip = list_text([g.fullname for g in sick_girls])
            night_early.add(line, ttip=ttip, ttip_title = event_color["bad"] % "生病了")

        if striking_girls:
            line = event_color["bad"] % ("拒绝工作: %s" % len(striking_girls))
            ttip = list_text([g.fullname for g in striking_girls])
            night_early.add(line, ttip=ttip, ttip_title = event_color["bad"] % "拒绝工作")

            night_text += "\n{color=[c_red]}" + and_text([g.name for g in striking_girls]) + __(" 拒绝工作!{/color} ")
            log.add_report("{color=[c_red]}" + and_text([g.name for g in striking_girls]) + __(" 拒绝工作!{/color}"))

        if resting_girls:
            line = event_color["normal"] % ("休息: %s" % len(resting_girls))
            ttip = list_text([g.fullname for g in resting_girls])
            night_early.add(line, ttip=ttip, ttip_title = "休息")

        if away_girls:
            line = event_color["normal"] % ("离开: %s" % len(away_girls))
            ttip = list_text([g.fullname for g in away_girls])
            night_early.add(line, ttip=ttip, ttip_title = "离开")

        if farm.girls:
            ttip = list_text([g.fullname for g in farm.girls])
            night_early.add("Farm: %s" % len(farm.girls), ttip=ttip, ttip_title = event_color["fear"] % "在农场", col=c_purple)

        customers, cust_text, cust_nb_dict = generate_customers(brothel.rep, use_adv=len(working_girls)) # At least one customer is always guaranteed

    ## Close brothel if no girls are available

        if not working_girls:
            night_early.add("暂停营业", "header", col="bad")
            night_early.add("顾客被拒之门外: %s" % len(customers), ttip = get_customer_population_count(customers))

            ad_pic = "events/" + rand_choice(night_pics)
            night_text += __("青楼今晚暂停营业。")
            cust_text = brothel.name + __(" 今晚暂停营业，因为没有人上班。\n")

            if len(customers) > 5: # Lose rep for each customer that comes in vain
                old_rep = brothel.rep
                rep_loss = -sum(c.rank for c in customers)
                rep_loss = min(brothel.change_rep(rep_loss), 0)

                # cust_text += __("Some customers came and were disappointed. Your brothel's reputation has changed from ") + str_int(old_rep) + __(" to ") + str_int(brothel.rep) + " (" + event_color["bad"] % str_int(rep_loss) + ")."

                if rep_loss:
                    night_early.add("名声减少: %s" % plus_text(rep_loss))

        # night_text += cust_text

    ## Brothel maintenance (customers might turn away if the brothel is dirty)
        maint_text = ""

        # Checks brothel cleanliness

        cleanliness = brothel.get_cleanliness()
        turned_away = 0

        if cleanliness == "dusty":
            turned_away = (dice(2, district.rank)-1)
            maint_text = "\n你的青楼尘土飞扬。房间里都结蜘蛛网了。"

        elif cleanliness == "dirty":
            turned_away = dice(3, district.rank)
            maint_text = "\n你的青楼越来越脏了。老鼠都能把这里当窝了。"

        elif cleanliness == "disgusting":
            turned_away = dice(6, district.rank)
            maint_text = "\n这地方太恶心了。顾客们无法忍受，有些女孩甚至因此生病了!"

        if working_girls:
            # Turn away disgusted customers

            if turned_away > 0:
                if turned_away < len(customers): # Cuts down the customer list (it is shuffled in generate_customers)
                    customers, lost_customers = customers[turned_away:], customers[:turned_away]
                else:
                    lost_customers = list(customers)
                    customers = []

                rep_loss = -sum(c.rank for c in lost_customers)
                rep_loss = brothel.change_rep(rep_loss)
                if not customers:
                    text1 = "青楼脏臭不堪， %s 位顾客全都忍受不了离开了青楼 (%s 名声)" % (str(len(lost_customers)), str_int(rep_loss))
                else:
                    text1 = "有 %s 位顾客因为青楼看起来很脏而拒绝光顾 (%s 名声)"  % (str(len(lost_customers)), str_int(rep_loss))
                maint_text += "\n" + text1
                log.add_report(event_color["bad"] % text1)

                night_early.add("Dirtiness", "header")
                night_early.add("顾客被拒之门外: -%s" % len(lost_customers), col="bad", ttip = get_customer_population_count(lost_customers))
                cust_text += "\n转身离开: %s" % plus_text(-len(lost_customers))
                if rep_loss:
                    night_early.add("名声减少: %s" % plus_text(rep_loss))

            night_early.add("顾客: %s" % len(customers), "header", ttip = cust_text, ttip_title = "Customer report")

            for pop in all_populations:
                if cust_nb_dict[pop.name]:
                    night_early.add(capitalize(pop.name) + ": " + str_int(cust_nb_dict[pop.name]), ttip = "%i %s 来到了 %s" % (cust_nb_dict[pop.name], pop.name, brothel.name))

        night_text += maint_text

        # Log night event

        # if not isinstance(ad_pic, Picture): #?
        #     ad_pic = Picture(ad_pic, "events/" + ad_pic)

        perform_events.append(Event(pic = ad_pic, char = "", text = night_text, changes = night_early, type ="UI"))

    #### SECURITY EVENTS ####

    if brothel.get_effect("special", "demon maintenance"):
        call show_night_event(Event(pic=rand_choice(game_image_dict["Misc"]["hannies"]), char = "", text = "虽然比门把手还笨，但她们却很擅长抛光门把手。你的顽皮盟友帮你清理顾客留下的烂摊子，而且他们免费工作:有什么不喜欢的?", type="UI")) from _call_show_night_event_7

    if brothel.get_effect("special", "demon security"):
        call show_night_event(Event(pic=rand_choice(game_image_dict["Misc"]["oni"]), char = "", text = "你的恶魔盟友的大量出现加强了你的安全。今晚维持治安应该是轻而易举的事。", type="UI")) from _call_show_night_event_8

    if brothel.threat_build_up(): # Returns True if security event may proc
        call security(working_girls) from _call_security
        $ test_achievements(["security events"])

        python:
            for girl in working_girls:
                if girl.hurt or girl not in MC.girls: # Girl may be out of MC.girls if she has been kidnapped
                    working_girls.remove(girl)
                    girl.add_log("work_days", -1)

                    if girl.hurt:
                        girl.add_log("hurt_days")

                    if girl in job_girls:
                        job_girls.remove(girl)
                        girl.add_log(girl.job + "_days", -1)

                    if girl in whores:
                        whores.remove(girl)
                        girl.add_log("whore_days", -1)

                    if girl.work_whore:
                        girl.add_log("work_whore_days", -1)


#### CUSTOMERS AND GIRLS INTERACT ####

    ### ENTERTAINMENT ###

    python:
        job_crazy_dict = defaultdict(list) # Tracks crazy_customers for the matchmaking screen

        job_customers = list(customers) # Keeps track of the original state of 'customers' before jobs
        ent_dict, leftover_customers, job_cap, ticket_dict = job_matchmaking(job_girls, job_customers)

        perform_events.append("job_matchmaking")

        for girl in job_girls:
            if ent_dict[girl]:

                # Checks for crazy customers

                crazy_ev, crazy_cust = crazy_customer([girl], ent_dict[girl])

                if crazy_ev:
                    perform_events.append(crazy_ev)
                    customers.remove(crazy_cust)
                    ent_dict[girl].remove(crazy_cust)
                    job_crazy_dict[girl].append(crazy_cust)

                    if girl.hurt > 0: # Aborpts performance if girl got hurt
                        # Cancels remaining tickets for this girl
                        try:
                            ticket_dict[girl.rank, girl.job] = [t for t in ticket_dict[girl.rank, girl.job]  if t != girl]
                        except:
                            ticket_dict[girl.rank, girl.job] = []

                        # Runs matchmaking again for her remaining customers
                        ent_dict, leftover_customers2, job_cap, ticket_dict = job_matchmaking(job_girls, ent_dict[girl], ent_dict, job_cap)
                        leftover_customers += leftover_customers2

                        # Logs injury
                        girl.add_log("hurt_days")
                        girl.add_log("work_days", -1)
                        girl.add_log(girl.job + "_days", -1)
                        if girl.work_whore:
                            whores.remove(girl)
                            girl.add_log("work_whore_days", -1)

                        # Move on to the next girl without performing
                        continue

            # Perform entertainment if any customers are left

            if ent_dict[girl]:
                perform_events += perform(girl.job, [girl], ent_dict[girl])
            else:
                log.add_report(girl.name + " 今天没有顾客可供招待。.")

        if not leftover_customers:
            log.add_report(event_color["good"] % (__(" %s 位顾客全都被服务的很好。") % str_int(len(customers))))

        else:
            log.add_report(event_color["bad"] % (__("%s 位顾客被晾在一旁，十分不爽。") % str_int(len(leftover_customers))))

    $ renpy.block_rollback()

    ### WHORING ###

    python:
        # Sanity check
        for girl in whores:
            if not girl.does_anything():
                raise AssertionError(" " + girl.fullname + "没有激活的性行为。")

        wh_crazy_dict = defaultdict(list) # Tracks crazy_customers for the matchmaking screen

        # Matchmaking

        whore_customers = list(customers) # Keeps track of the state of 'customers' before the whoring phase
        wh_list, leftover_customers = wh_matchmaking(whores, whore_customers)

        perform_events.append("wh_matchmaking")

        # Interact with customers

        available_whores = list(whores)

#         for _girls, _customers, sex_act in wh_list: causes MEMORY ERROR when adding wh_list2

        # temp_wh_list = list(wh_list)
        # while temp_wh_list:

            # _girls, _customers, sex_act = temp_wh_list.pop(0)
            # copy_girls = list(_girls) # A copy is needed for the following wh_list.remove to work # Apparently not

        failed_interactions = []

        for _girls, _customers, sex_act in wh_list:
            # Removes hurt and incapacited girls
            for girl in [g for g in _girls if g.hurt > 0 or g.exhausted]:
                _girls.remove(girl)
                if girl in available_whores: # Won't happen if she has been removed before
                    available_whores.remove(girl)

            # Attempts to reassign customers if no girl is left
            if not _girls:
                wh_list2, leftover_customers2 = wh_matchmaking(available_whores, _customers)
                wh_list += wh_list2
                # temp_wh_list += wh_list2
                leftover_customers += leftover_customers2

            # Checks for crazy customers (who didn't trigger during entertainment phase)
            if _girls:
                crazy_ev, crazy_cust = crazy_customer(_girls, _customers)

                if crazy_ev:
                    perform_events.append(crazy_ev)
                    _customers.remove(crazy_cust)
                    customers.remove(crazy_cust)
                    wh_crazy_dict[_girls[0]].append(crazy_cust)

                    for hurt_girl in [g for g in _girls if g.hurt > 0]:
                        _girls.remove(hurt_girl)
#                         game.mm_log += "\n%s removed (hurt)" % girl

                        # Logs injury
                        hurt_girl.add_log("hurt_days")
                        hurt_girl.add_log("work_days", -1)
                        hurt_girl.add_log("whore_days", -1)
                        if hurt_girl.work_whore:
                            available_whores.remove(hurt_girl)
                            hurt_girl.add_log("work_whore_days", -1)

            # Perform whoring
            if _girls and _customers:
                perform_events += perform(sex_act, _girls, _customers)
            else:
                failed_interactions.append([_girls, _customers, sex_act]) # For removing outside of loop

        for failed in failed_interactions:
            wh_list.remove(failed)

    $ renpy.block_rollback()

    python:

        if not leftover_customers:
            log.add_report(event_color["good"] % (" %s 个嫖客中的每一位都能和姑娘们在床上一番云雨。" % str_int(len(customers))))

        else:
            night_no_girls = NightChangeLog(title="夜色渐深", col=c_lightorange)
            night_no_girls.add("白跑一趟的顾客", "header", col="bad")
            night_no_girls.add(get_customer_population_count(leftover_customers))

            if len(leftover_customers) == len(customers):
                text1 = __("No ")
            else:
                text1 = __("No more ")

            pic = rand_choice(no_girls_pics)

            ev = Event(Picture(pic, "events/" + pic), text = text1 + __("有 %s 名顾客失望地离开了。") % str_int(len(leftover_customers)), type ="UI", changes=night_no_girls)
            perform_events.append(ev)

            log.add_report(event_color["bad"] % (__("%s 名顾客没人伺候，失望地离开了。") % str(len(leftover_customers))))


    # Predict image for first event in Perform list
        predict_next_img([perform_events]) # DougTheC's suggestion

    ### Update girl relationships

        rel_changes = []

        for girl in working_girls:
            chg = girl.update_relationships()
            if chg:
                rel_changes.append(chg)


    ### Farm events

    python:
        if farm.active:
            farm_training_girls, farm_holding_girls, farm_resting_girls = farm.assign_girls(logging=True)

            # renpy.notify("Counting farm days")

            for girl in (farm_training_girls + farm_holding_girls):
                girl.add_log("farm_days")

        farm_events = []

        if farm.active:
            for inst in farm.installations.values():
                if inst.girls:
                    farm_events.append(inst.get_intro())

                for girl in inst.girls:
                    farm_events += farm.programs[girl].resolve("training")

            for girl in farm_holding_girls:
                farm_events += (farm.programs[girl].resolve("holding"))

            for girl in farm_resting_girls:
                farm_events += (farm.programs[girl].resolve("resting"))

    ### Rest your girls

        # Rest half-shift girls

        for girl in working_girls:

            if girl.workdays[calendar.get_weekday()] == 50:
                mod = 0.33 * girl.get_effect("boost", "half-shift resting bonus")
                girl.rest(mod=mod)

        # Resting girls

        resting_events = []

        for girl in striking_girls + resting_girls:

            resting_text, resting_changes = girl.rest()

            resting_text = "{size=" + str(int(config.screen_height*0.025)) + "}" + resting_text

            extra_text = ""
            extra_sound = None

            if girl.get_effect("special", "rest shield"):
                resting_changes.add("Spells", "header")
                if girl.get_effect("special", "shield"):
                    for g in girl.friends:
                        if not g.get_effect("special", "shield"):
                            g.add_effects(shield_effect)
                            extra_text = "\n" + girl.name + " 给她的闺蜜" + g.fullname + "施加了一层魔法护盾。"
                            resting_changes.add("Shield cast on " + g.fullname, col=c_lightblue)
                            extra_sound = s_spell
                            break
                else:
                    girl.add_effects(shield_effect)
                    extra_text =  "\n" + girl.name + " 给自己施加了一层魔法护盾。"
                    resting_changes.add("Shield cast on herself", col=c_lightblue)
                    extra_sound = s_spell

            # Use her toys

            used = []
            result = False

            for it in girl.items:
                if it.usage == "auto_rest":
                    # Limited scope: for toys only

                    if girl.get_stat("libido") > 40:

                        r, changes = girl.use_item(it, night=True)
                        used = it.name
                        if changes.has_changes():
                            extra_sound = s_spell

                        resting_changes.merge(changes)

                        break # Only one toy can be used at a time

                    else:
                        extra_text += __("\n她拒绝使用 ") + __(it.name) + "A."

            if used:
                extra_text += __("\n她使用那些小玩意儿玩得很开心 %s." % used)
                girl.add_log("used toy")

            resting_text += extra_text

            if used:
                pic = girl.get_pic("toy", "mast")
                if not pic:
                    pic = girl.get_pic("rest", "profile", and_tags = "naked", soft=True)
            else:
                pic = girl.get_pic("rest", "profile", not_tags=["mass", "waitress", "geisha", "swim"], naked_filter=True, soft=True)

            resting_events.append(Event(pic, char = girl.char, text = resting_text, changes = resting_changes, sound = extra_sound, type ="Rest"))



#### The events aren't played until the end of daily calculations to avoid the mess with rollbacks

#### SHOW INTERACTIONS ####

    # Stores latest matchmaking, for possible use during day (unused for now)
    $ latest_ent_match = [job_girls, job_customers, make_match_list_from_ent_dict(ent_dict, job_crazy_dict), "job"]
    $ latest_wh_match = [whores, whore_customers, make_match_list_from_wh_list(wh_list, wh_crazy_dict), "whore"]

    $ renpy.block_rollback()

    while perform_events:

        $ ev = perform_events.pop(0)
        $ predict_next_img([perform_events, farm_events, resting_events]) # Chris12's suggestion

        if ev == "job_matchmaking":
            if job_girls and not persistent.skipped_events["Matchmaking"]:
                $ tt = show_tt("top_right")

                call screen matchmaking(*latest_ent_match)

                hide screen tool

        elif ev == "wh_matchmaking":
            if whores and not persistent.skipped_events["Matchmaking"]:
                $ tt = show_tt("top_right")
                call screen matchmaking(*latest_wh_match)
                hide screen tool

        else:
            call show_night_event(ev) from _call_show_night_event


    ## Change Brothel Rep

    python:
        night_late = NightChangeLog("今日小结", col=c_lightorange)
        night_late.add("第 %i 年 %i 月 第 %i 天 %s" % (calendar.year, calendar.month, calendar.day, __(calendar.get_weekday())), "header")
        old_rep = brothel.rep

        served = sum(1 for c in customers if c.got_entertainment)
        entertained = sum(1 for c in customers if c.got_entertainment == c.wants_entertainment)
        laid = sum(1 for c in customers if c.got_sex_act)
        satisfied = sum(1 for c in customers if c.got_sex_act == c.wants_sex_act)

        night_late.add("顾客总数: %i" % len(customers), "header")
        night_late.add("普通顾客总数: %s" % (event_color["average"] % served), ttip="%i 名顾客中只有 %i 名顾客得到了服务。" % (len(customers), served ))
        night_late.add("嫖娼顾客总数: %s" % (event_color["average"] % laid), ttip="%i 名嫖客中只有 %i 名嫖客有姑娘伺候。" % (len(customers), laid))
        night_late.add("对服务满意的人数: %s" % (event_color["a little good"] % entertained), ttip="%i 名消费的顾客中有 %i 名顾客对服务表示满意。" % (served, entertained))
        night_late.add("对嫖娼满意的人数: %s" % (event_color["a little good"] % satisfied), ttip="%i 名嫖客中有 %i 名嫖客对姑娘们感到满意。" % (laid, satisfied))

        log.add_report(event_color["good"] % (str(len(customers)) + " 名顾客" + plural(len(customers)) + " 光顾了你的青楼。 " + str(served) + " 名顾客得到了服务 (" + str(entertained) + " 名顾客对服务感到满意), " + str(laid) + " 名顾客和姑娘们巫山云雨 (" + str(satisfied) + " 名顾客对姑娘们很满意)。"))

        rep_chg = sum(c.get_reputation_change() for c in customers)
        rep_chg = brothel.change_rep(rep_chg)

        night_late.add("名声: %s (%s)" % (str_int(brothel.rep) + "/" + str_int(brothel.max_rep), event_color["rep"] % (plus_text(rep_chg))), "header", ttip=plus_text(rep_chg) + " 客户的满意度提供的名声。")

        log.add_report(event_color["rep"] % ("青楼的名声从 %s 变为 %s (%s)" % (str_int(old_rep), str_int(brothel.rep), plus_text(round_int(rep_chg)))))

        log.track("served", served)
        log.track("entertained", entertained)
        log.track("laid", laid)
        log.track("satisfied", satisfied)
        log.track("new rep", brothel.rep)
        log.track("rep change", rep_chg)

    ## Customer satisfaction screen

    $ customers.sort(key=lambda x: x.reputation_change, reverse=True)

    $ renpy.say("", "客人离场，结束营业", interact=False)

    $ latest_sat_report = [customers, old_rep, rep_chg]

    if not persistent.skipped_events["Satisfaction report"]:
        call screen customer_satisfaction(*latest_sat_report)


### SHOW FARM EVENTS ####

    while farm_events:

        $ ev = farm_events.pop(0)
        $ predict_next_img([farm_events, resting_events]) # Chris12's suggestion

        call show_night_event(ev) from _call_show_night_event_1

#### SHOW RESTING GIRLS ####

    while resting_events:
        $ ev = resting_events.pop(0)
        $ predict_next_img([resting_events]) # Chris12's suggestion

        call show_night_event(ev) from _call_show_night_event_3

#### SHOW RELATIONSHIP CHANGES ####

    if rel_changes:
        while rel_changes:
            $ girl1, girl2, old_status, new_status = rel_changes.pop(0)
            $ debug_notify("Showing relationship event")
            call show_relationship_change(girl1, girl2, old_status, new_status) from _call_show_relationship_change

            if new_status == "friend":
                $ log.add_report(event_color["good"] % ("%s 和 %s 成为了好闺蜜。" % (girl1.fullname, girl2.fullname)))
            elif new_status == "rival":
                $ log.add_report(event_color["bad"] % ("%s 和 %s 成为了死对头。" % (girl1.fullname, girl2.fullname)))
            elif new_status == "normal":
                $ log.add_report("%s 和 %s 不再是 %s 。" % (girl1.fullname, girl2.fullname, old_status))

    elif len(working_girls) > 1:
        call random_relationship_event(working_girls) from _call_random_relationship_event



#### END NIGHT ####

    ## Reset interactions + Decrease spoiled and terrified points

    python:
        MC.reset_interactions()

        for girl in (MC.girls + game.free_girls + farm.girls + MC.escaped_girls): #!
            girl.reset_interactions()
            girl.refresh_spoil_terrify_points()

    ## Update mood

        for girl in (MC.girls + farm.girls):

            if girl not in (away_girls):
                girl.update_mood()

                # Fear and love slowly revert to mean

                if girl.get_love() > 0:
                    girl.change_love(-0.2)
                else:
                    girl.change_love(0.2)

                if girl.get_fear() > 0:
                    girl.change_fear(-0.2)
                else:
                    girl.change_fear(0.2)

                # Fear/Love regen traits
                girl.change_love(girl.get_effect("change", "love per day"))
                girl.change_fear(girl.get_effect("change", "fear per day"))

    ## Girl skill improvements

        catch_up_changes = []

        for girl in MC.girls: # farm girls are excluded from catch up effects
            if not girl.away or girl.hurt or girl.exhausted:
                if girl.get_effect("special", "skill catch up") and len(MC.girls) > 1: # Avoid infinite loop if she's alone
                    target_girls = rand_choice([g for g in MC.girls if g != girl], girl.rank)
                    girl_changes = []
                    for girl2 in target_girls:
                        girl2_changes = []
                        for stat in gstats_main + gstats_sex:
                            if girl.get_stat(stat, raw=True) >= girl2.get_stat(stat, raw=True) + 1:
                                if dice(250) > girl2.get_stat(stat, raw=True):  # Stats are harder to raise as they grow
                                    girl2.change_stat(stat, 1, silent=True)
                                    girl2_changes.append(stat)
                        if girl2_changes:
                            girl_changes.append([girl2, girl2_changes])
                    if girl_changes:
                        catch_up_changes.append([girl, girl_changes])

    ## Girl level up
        leveled = []
        jobbed = []

        for girl in MC.girls:
            if girl.ready_to_level():
                girl.level_up()
                leveled.append(girl)

            for act in [girl.job] + all_sex_acts:
                if girl.ready_to_job_up(act):
                    girl.job_up(act)
                    jobbed.append(girl)


        if leveled or MC.ready_to_level():
            night_late.add("Level up", "header")
            if MC.ready_to_level():
                night_late.add("* " + MC.name, col=c_steel)

            for girl in leveled:
                night_late.add("* " + girl.fullname, col="good")
        if jobbed:
            night_late.add("Job up", "header")
            for girl in jobbed:
                night_late.add("* " + girl.fullname, col=c_orange)

    ## Clean up the brothel

        chg = brothel.change_dirt(-1 * brothel.get_maintenance())

        night_late.add("卫生情况: %i (%s)" % (int(brothel.dirt), plus_text(log.dirt + chg)), "header", ttip="你的青楼 " + brothel.get_cleanliness())
        night_late.add("垃圾: %s" % plus_text(log.dirt))
        night_late.add("清洁: %s" % plus_text(chg))

    ## Pay the rent

        # Applies Sill trainer effect
        if MC.get_effect("special", "free upkeep"):
            free_girl = rand_choice(MC.girls)
        else:
            free_girl = None

        for girl in MC.girls:
            if girl == free_girl:
                pass
            else:
                log.upkeep += girl.upkeep * girl.get_effect("boost", "total upkeep")
                girl.add_log("upkeep", girl.upkeep * girl.get_effect("boost", "total upkeep"))

        for girl in farm.girls:
            log.upkeep += girl.get_med_upkeep() * girl.get_effect("boost", "total upkeep") // 4
            girl.add_log("upkeep", girl.get_med_upkeep() * girl.get_effect("boost", "total upkeep") // 4)

        # gold_text is displayed to the right-hand side. gold_recap is displayed in the renpy window
        gold_text = __("你支付了 ") + '{image=img_gold} ' + '{:,}'.format(round_int(log.upkeep)) + __(" 金币作为女孩的薪水。")

        if free_girl:
            gold_text += __(" (免费保养: ") + free_girl.name + ")"

        if working_girls:
            log.costs = brothel.get_adv_cost() + brothel.get_sec_cost() + brothel.get_maintenance_cost()
            gold_text += __(".\nY你支付了 ") + '{image=img_gold} ' + '{:,}'.format(round_int(log.costs)) + __(" 金币作为员工工资。")

        else:
            log.costs = brothel.get_maintenance_cost()
            gold_text += "。 " + brothel.name + __(" 暂停营业，所以你让保安和宣传人员回去了。你支付了 ") + '{:,}'.format(round_int(log.costs)) + __("金币作为青楼的开销。")

        loan_payment = MC.repay_loan()

        if loan_payment:
            log.costs += loan_payment
            gold_text += "\n你支付了 {image=img_gold} " + '{:,}'.format(round_int(loan_payment)) + "金币给外包人员。"

        gold_recap = "你支付了 {image=img_gold_24} " + event_color["a little bad"] % '{:,}'.format(round_int(log.upkeep+log.costs)) + " 金币给外包人员。"

    ## Katchiiing

        bonus = log.gold_made * min((brothel.get_effect("boost", "income")-1, 2.5)) # Maximum achievable income boost is hard-capped at +250%
        log.gold_made += bonus

        gold_recap += __("\n你的女孩赚到了 {image=img_gold_24} ") + event_color["a little good"] % '{:,}'.format(round_int(log.gold_made))

        if bonus > 0:
            gold_recap += " (" + (__("盈利: {image=img_gold_24} ") + event_color["a little good"] % '{:,}'.format(round_int(bonus))) + ")"
        elif bonus < 0:
            gold_recap += " (" + (__("亏损: {image=img_gold_24} ") + event_color["a little bad"] % '{:,}'.format(round_int(bonus))) + ")"

        # Bast trainer effect

        if brothel.get_effect("special", "resources as income"): # Taking into account the lost revenue, this is equivalent to a 50% discount on the cost of buying resources from the market
            resource_value = 0.5 * log.gold_made # 0.5 = 20% of initial income (25% of discounted income) * 2 (discount on base resource value). Yeah, it's complicated.

            if resource_value >= resource_gold_value[4]:
                resource = rand_choice(build_resources)
            elif resource_value >= resource_gold_value[3]:
                resource = rand_choice([r for r in build_resources if resource_dict[r].rank<=3])
            else:
                resource = rand_choice([r for r in build_resources if resource_dict[r].rank<=2])

            nb = resource_value//resource_gold_value[resource_dict[resource].rank]

            if nb > 0:
                MC.gain_resource(resource, nb, message=False)
                gold_recap += __("和") + str_int(nb) + " " + resource
                night_late.add("Resources", "header")
                night_late.add("+%i {image=tb %s}" % (nb, resource), col="good")

        # Street whores income

        street_gold = sum(g.whore_on_street() for g in MC.street_girls) # Running whore_on_street calculates tip and wears down girl skills
        log.gold_made += street_gold

        log.net = round_int(log.gold_made - log.upkeep - log.costs)

        ## Log changes for the right recap

        night_late.add("Income: " + "{image=img_gold_20} %s" % plus_text(log.net, "gold"), "header")

        night_late.add("Girls income: " + event_color["a little good"] % plus_text(log.gold_made-street_gold), ttip_title="Girl income", ttip=list_text(["%s: %s" % (capitalize(g.fullname), plus_text(g.get_log("total_gold", "today"))) for g in working_girls]))
        if street_gold:
            night_late.add("Street whores: " + event_color["a little good"] %  plus_text(street_gold), ttip_title="Street whores income", ttip=list_text(["%s: %s" % (capitalize(g.fullname), plus_text(g.today_street_tip)) for g in MC.street_girls]))

        night_late.add("Costs: "  + event_color["bad"] % str_int(-log.upkeep - log.costs), ttip = gold_text)

        night_late.add("* Upkeep: %i" % -log.upkeep, col="bad", ttip = list_text(["%s: %s" % (capitalize(g.fullname), plus_text(g.get_log("upkeep", "today"))) for g in (MC.girls+farm.girls)]))

        if working_girls:
            night_late.add("* Advertising: %i" % -brothel.get_adv_cost(), col="bad", ttip="%i advertising girls x %i = {image=img_gold} %i" % (brothel.advertising, helper_cost[district.rank], brothel.get_adv_cost()))

            night_late.add("* Security: %i" % -brothel.get_sec_cost(), col="bad", ttip="%i goons x %i = {image=img_gold} %i" % (brothel.security, helper_cost[district.rank], brothel.get_sec_cost()))

        night_late.add("* Maintenance: %i" % -brothel.get_maintenance_cost(), col="bad", ttip="%i maids x {image=img_gold} %i = {image=img_gold} %i" % (brothel.maintenance, helper_cost[district.rank], brothel.get_maintenance_cost()))

        if loan_payment:
            night_late.add("* Loan payment: %i" % loan_payment, col="bad")

        if bonus:
            night_late.add("Perks and special effects: %s" % plus_text(bonus, "standard"))

        MC.gold += log.net
        NPC_taxgirl.MC_income += (log.net * brothel.get_effect("boost", "taxable net income"))

        if log.net > 0:
            gold_recap += __(", 获得利润  {image=img_gold_24} {b}") + event_color["a little good"] % '{:,}'.format(log.net) + "{/b}金币。"
        elif log.net < 0:
            gold_recap += __(", 入不敷出。你亏损了 {image=img_gold_24} {b}") + event_color["a little bad"] % '{:,}'.format(-1*log.net) + "{/b}金币。"
        else:
            gold_recap += __("，收支平衡。你盈利了 {color=[c_red]}{b}0{/b} 金币{/color}。")

        if log.net > 2500:
            pic = rand_choice(treasure_pics["+++"])
        elif log.net > 500:
            pic = rand_choice(treasure_pics["++"])
        elif log.net > 0:
            pic = rand_choice(treasure_pics["+"])
        else:
            pic = rand_choice(treasure_pics["-"])
        if not nsfw:
            pic = rand_choice(night_pics)

        ev = Event(Picture(pic, "events/" + pic), text = gold_recap, changes = night_late, sound = s_cash, type ="UI")


#### SHOW NIGHT RECAP ####


## Catch up changes
    while catch_up_changes:
        $ girl, changes = catch_up_changes.pop(0)

        $ text1 = girl.fullname + "帮助"
        if len(changes) > 1:
            $ text1 += "其他女孩提升了她们的技能。\n{size=-6}("
        else:
            $ text1 += "另一个女孩提升了她的技能。\n{size=-6}("

        python:
            for girl2, stats in changes:
                text1 += girl2.fullname + ": " + (and_text([event_color["good"] % ("+" + s) for s in stats], separator = ", +"))

        girl.char "[text1]){/size}"

## Night recap
    $ renpy.block_rollback()
    if not persistent.can_skip_night_recap:
        $ renpy.choice_for_skipping()
    $ test_achievements(["income", "losses"])

    if calendar.time % save_every_x_days == 0:
        $ do_auto_save = True
    else:
        $ do_auto_save = False

    call show_night_event(ev, save=do_auto_save) from _call_show_night_event_5


############ Jman - Headhunter Mod ############
    if game.has_active_mod("Headhunter Mod"):
        $ game.headhunter_time -= 1
############ Jman - Headhunter Mod End ########


## Special treasure girl event

    if log.net >= 10000 and dice(6) >= 6:
        if pic.startswith("treasure_blonde") and not story_flags["blonde treasure event"]:
            call treasure_girl_sex("blonde", pic) from _call_treasure_girl_sex
        elif pic.startswith("treasure_pink") and not story_flags["pink treasure event"]:
            call treasure_girl_sex("pink", pic) from _call_treasure_girl_sex_1

#### And on to a new day... ####

    ## MC level up

    if MC.ready_to_level():
        $ MC.level_up()

    centered "Loading...{nw}"

    python:

        reset_alerts()

        MC.reset_spells()

        calendar.newday()

        today_weekday = calendar.get_weekday()

        daily_tip = rand_choice(random_tips)

    ## Placeholder in case random events are added
#        calendar.set_alarm(calendar.time, weighted_choice(rand_events)) # Chooses a random event for today (may not happen if prerequisites are not met)

    ## Autocast spells (MORNING)

        for spell in MC.known_spells:

            res, cast_text = MC.autocast(spell, "morning")

            if cast_text:
                log.add_report(cast_text)

    ## Auto-extract resources

        for res in build_resources: # Receives one free resource for each extractor
            if auto_extractors[res + " ON"]:
                MC.gain_resource(res, message=False)
                auto_extractors[res + " durability"] -= 1
                if dice(100) > auto_extractors[res + " durability"]:
                    calendar.set_alarm(calendar.time + 1, Event(label="break_extractor", object=res))


    # ## Displays brothel
    #
    # scene black
    # show expression bg_bro at top
    # with Dissolve(0.15)


    ## Check if girls ran away
    python:
        for girl in MC.girls:

            check = girl.run_away_check()

            if check == "runaway" and girl not in away_girls:
                girl.ran_away_counter = 0
                renpy.call("run_away", girl)
                girl.add_log("run_away", delay=-1)

            elif check == "warning":
                renpy.say (sill, "警告！! [girl.fullname] 一直很不开心，抱怨着要离家出走...")

    ## Check if girls are tired

        for girl in MC.girls:
            if girl.tired_check(): # Returns True if tired warning
                renpy.say (sill, "警告！! [girl.fullname] 太累了...")
                if dice(6) >= 6:
                    calendar.set_alarm(calendar.time, Event(label="too_tired", object=girl))

    ## Check if girls are ready to return from the farm

        exit_girls = []

        for girl in farm.girls:
            if farm.test_exit_conditions(girl):
                exit_girls.append(girl)

        while exit_girls:
            girl = exit_girls.pop(0)
            renpy.call("exit_farm", girl, farm.test_exit_conditions(girl))

    ## Degrades hurt minions health

        retired_minions = farm.hurt_minions()

        for mn in retired_minions:
            renpy.say(gizel, "一个等级 " + str(mn.level) + " 的" + farm_related_dict[mn.type] + " 因为受伤或损坏而被除名.")

    ## Update girl portraits and profiles

        for girl in MC.girls:
            girl.refresh_pictures(silent=True)

    ## Check if goal has been reached

    if game.goals_reached():
        call reached_goal from _call_reached_goal

#### PLAYING CONDITIONAL EVENTS

    call play_events(_type = "morning") from _call_play_events_1 # Note: Morning events are set with the new day's date: beware of the confusion

    $ test_achievements(["months", "friends", "rivals", "rep"])

#### CHECK FOR BANKRUPTCY ####

    if MC.gold < 0:
        $ calendar.set_alarm(calendar.time, StoryEvent(label="no_money"))

#### RETURN TO MAIN SCREEN ####

    jump main

#### END OF BK END DAY FILE ####
