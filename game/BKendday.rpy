####            END DAY ROUTINE                ####
##          Managing and displaying the          ##
##            different night events             ##
####                                           ####


#### DECLARATIONS ####

## DICE IMAGES ##

image img_dice1 = ProportionalScale("UI/dice1.webp", 20, 20)
image img_dice2 = ProportionalScale("UI/dice2.webp", 20, 20)
image img_dice3 = ProportionalScale("UI/dice3.webp", 20, 20)
image img_dice4 = ProportionalScale("UI/dice4.webp", 20, 20)
image img_dice5 = ProportionalScale("UI/dice5.webp", 20, 20)
image img_dice6 = ProportionalScale("UI/dice6.webp", 20, 20)

#### END DAY ####

label end_day:

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

    call play_events(type = "night") from _call_play_events


#### SHOWING NEW MOON ####

    $ renpy.block_rollback()

    if calendar.day == 1:
        call new_moon() from _call_new_moon

    scene black with Fade(0.15, 0.3, 0.15)


#### PREPARING GIRLS ####

    ## Prepare

    python:
        if not logs[calendar.time]:
            log = logs[calendar.time] = Log(calendar.time)
        else:
            log = logs[calendar.time]

        perform_events = []
        night_text = ""

        latest_ent_match = [[], [], [], "job"]
        latest_wh_match = [[], [], [], "whores"]

    ## Autocast spells (NIGHT)

        for spell in MC.known_spells:

            cast_text = MC.autocast(spell, "night")

            if cast_text:
                log.add_report(cast_text)


    ## Update brothel effects (bonuses from girls and MC spells)

        brothel.update_effects()


    ## Get working girls

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
                    log.add_report("{color=[c_red]}" + girl.fullname + " was under the energy threshold and was set to rest automatically.{/color}")
                    resting_girls.append(girl)
                    girl.add_log("rest_days")

                ## Health check

                elif girl.health_check() == "sick":
                    sick_girls.append(girl)
                    girl.add_log("sick_days")

                else:
                    # Sanity check
                    if girl.job == "whore" and not girl.does_anything():
                        renpy.say("", "[girl.fullname] cannot work as a whore as she refuses to do any sex act.")
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


    ## Alert if sick girls

#         sick_girls = []

#         for girl in working_girls:
#             if girl.health_check() == "sick":
#                 sick_girls.append(girl)
#                 girl.add_log("sick_days")

#         for girl in sick_girls:
#             working_girls.remove(girl)

#             if girl in job_girls:
#                 job_girls.remove(girl)
#                 girl.add_log(girl.job + "_days", -1)

#             if girl in whores:
#                 whores.remove(girl)
#                 girl.add_log("whore_days", -1)

        sick_text = ""

        if sick_girls != []:
            if len(sick_girls) == 1:
                sick_text += "\n{color=[c_red]}%s has fallen sick.{/color}" % sick_girls[0].name
            else:
                sick_text += "\n{color=[c_red]}%s have fallen sick.{/color}" % and_text([g.name for g in sick_girls])

    ## Apply advertisement

        log.rep = brothel.rep

        if working_girls: # Open

            # Reputation change from advertisement

            old_rep = round_int(brothel.rep)
            rep_change = brothel.get_adv_reputation()
            pony = False
            adv_girls = []
            for girl in working_girls:
                if girl.get_effect("special", "ponygirl"):
                    rep_change += 2 * girl.rank
                    pony = True
                elif girl.has_perk("Bunny Girl") or girl.has_perk("Rules of Attraction"):
                    adv_girls.append(girl)

            chg = brothel.change_rep_nightly(rep_change)

            if round_int(brothel.rep) != old_rep:
                rep_text = "Your brothel's reputation has changed from " + '{:,}'.format(old_rep) + " to " + '{:,}'.format(round_int(brothel.rep)) + "."
            else:
                rep_text = "Your brothel's reputation remains stable (" + '{:,}'.format(round_int(brothel.rep)) + ")."

            log.add_report(event_color["rep"] % rep_text)

            ad_pic = None

            if dice(6) >= 6 and pony:
                ad_pic = rand_choice(pony_pics)
                night_text += "{color=[c_pink]}It's time for the ponygirl parade!{/color}\n"

            elif adv_girls:
                adv_girl = rand_choice(adv_girls)
                ad_pic = adv_girl.get_pic("model", naked_filter=True, soft=True)
                night_text += "%s: {color=[c_pink]}'%s'{/color}\n" % (adv_girl.name, adv_girl.pick_dialogue("advertise").line)

            elif brothel.advertising > 0:
                night_text += "{color=[c_pink]}'Mister! Would you like to come and have a look at our wares? *giggles*'{/color}\n"

            if not ad_pic:
                if brothel.advertising > 0:
                    adv_index = min(int(math.ceil(brothel.advertising / (5.0+game.chapter))), 5) # Returns an index from 1 to 5. The float is needed.
                    ad_pic = rand_choice(advertising_pics[adv_index])
                else:
                    ad_pic = rand_choice(night_pics)

            night_text += sick_text + rep_text

            # Working girls logging

        ## Alert if striking girls

        if striking_girls:
            night_text += "\n{color=[c_red]}" + and_text([g.name for g in striking_girls]) + " refused to work!{/color} "
            log.add_report("{color=[c_red]}" + and_text([g.name for g in striking_girls]) + " refused to work!{/color}")

        if working_girls:
            night_text += "\n" + str(len(working_girls)) + " girls are working today. "

            for girl in working_girls:
                log.add_report(girl.fullname + " is working today as a " + girl.job + ".")


#### CUSTOMERS ARRIVE ####

        customers, cust_text = generate_customers(brothel.rep, use_adv=len(working_girls)) # At least one customer is always guaranteed

    ## Close brothel if no girls are available

        if not working_girls:

            ad_pic = rand_choice(night_pics)
            # night_text += "The brothel was closed tonight"
            cust_text = brothel.name + " was closed tonight, because none of your girls were working.\n"

            if len(customers) > 5: # Lose rep for each customer that comes in vain
                old_rep = brothel.rep
                rep_loss = -sum(c.rank for c in customers)
                rep_loss = min(brothel.change_rep(rep_loss), 0)

                cust_text += "Some customers came and were disappointed. Your brothel's reputation has changed from " + str_int(old_rep) + " to " + str_int(brothel.rep) + " (" + event_color["bad"] % str_int(rep_loss) + ")."

        night_text += cust_text

    ## Brothel maintenance (customers might turn away if the brothel is dirty)
        maint_text = ""

        # Checks brothel cleanliness

        cleanliness = brothel.get_cleanliness()
        turned_away = 0

        if cleanliness == "dusty":
            turned_away = (dice(2, district.rank)-1)
            maint_text = "\nYour brothel is getting dusty. There are cobwebs in the rooms."

        elif cleanliness == "dirty":
            turned_away = dice(3, district.rank)
            maint_text = "\nYour brothel is getting dirty. Sill thinks she saw a rat."

        elif cleanliness == "disgusting":
            turned_away = dice(6, district.rank)
            maint_text = "\nThis place is a disgusting mess. Customers are turning away and girls are getting sick!"

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
                    text1 = "Your brothel was so dirty that all %s customers ran away (%s reputation)" % (str(len(lost_customers)), str_int(rep_loss))
                else:
                    text1 = "%s customers turned away because the brothel looked filthy (%s reputation)"  % (str(len(lost_customers)), str_int(rep_loss))
                maint_text += "\n" + text1
                log.add_report(event_color["bad"] % text1)

        night_text += maint_text

        # Log night event

        if not isinstance(ad_pic, Picture):
            ad_pic = Picture(ad_pic, "events/" + ad_pic)

        perform_events.append(Event(pic = ad_pic, char = "", text = night_text, changes = "", type ="UI"))

    #### SECURITY EVENTS ####

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
                log.add_report(girl.name + " had no customers to entertain today.")

        if not leftover_customers:
            log.add_report(event_color["good"] % ("All %s customers were attended to while waiting." % str_int(len(customers))))

        else:
            log.add_report(event_color["bad"] % ("%s customers didn't get attended to and got bored." % str_int(len(leftover_customers))))

    $ renpy.block_rollback()

    ### WHORING ###

    python:
        # Sanity check
        for girl in whores:
            if not girl.does_anything():
                raise AssertionError, "No sex act available from " + girl.fullname + "."

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
            log.add_report(event_color["good"] % ("All %s customers were able to sleep with a whore." % str_int(len(customers))))

        else:
            if len(leftover_customers) == len(customers):
                text1 = "No"
            else:
                text1 = "No more"

            pic = rand_choice(no_girls_pics)

            event = Event(Picture(pic, "events/" + pic), text = text1 + " girls were available for sex and %s customers left disappointed." % str_int(len(leftover_customers)), type ="UI")
            perform_events.append(event)

            log.add_report(event_color["bad"] % ("%s customers couldn't get laid and left disappointed." % str(len(leftover_customers))))


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

            renpy.notify("Counting farm days")

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

            resting_text = "{size=18}" + resting_text

            extra_text = ""
            extra_sound = None

            if girl.get_effect("special", "rest shield"):
                if girl.get_effect("special", "shield"):
                    for g in girl.friends:
                        if not g.get_effect("special", "shield"):
                            g.add_effects(shield_effect)
                            extra_text = "\n" + girl.name + " cast a protective shield on her friend " + g.fullname + "."
                            extra_sound = s_spell
                            break
                else:
                    girl.add_effects(shield_effect)
                    extra_text =  "\n" + girl.name + " cast a protective shield on herself."
                    extra_sound = s_spell

            # Use her toys

            used = []
            result = False

            for it in girl.items: # To do: track changes and display in right column

                if it.usage == "auto_rest":

                    # Limited scope: for toys only

                    if girl.get_stat("libido") > 40:

                        r, c = girl.use_item(it)

                        used.append(it.name)

                        if c > 0:
                            result = True
                            for eff in it.effects:
                                resting_changes += "\n" + stat_increase_dict["stat"] % (capitalize(eff.target), str_int(round_int(c)))

                    else:
                        extra_text += "\nShe refused to use the " + it.name + "."

            if used:
                extra_text += "\nShe had some fun with the " + and_text(used)
                if result:
                    extra_sound = s_spell
                    extra_text += ", and learned something new"
                extra_text += "."
                girl.add_log("used toy")

            resting_text += extra_text

            if used:
                pic = girl.get_pic("toy", "mast")
                if not pic:
                    pic = girl.get_pic("rest", "profile", and_tags = "naked", soft=True)
            else:
                pic = girl.get_pic("rest", "profile", naked_filter=True, soft=True)

            resting_events.append(Event(pic, char = girl.char, text = resting_text, changes = resting_changes, sound = extra_sound, type ="Rest"))



#### The events aren't played until the end to avoid the mess with rollbacks

#### SHOW INTERACTIONS ####

    # Stores latest matchmaking, for possible use during day (unused for now)
    $ latest_ent_match = [job_girls, job_customers, make_match_list_from_ent_dict(ent_dict, job_crazy_dict), "job"]
    $ latest_wh_match = [whores, whore_customers, make_match_list_from_wh_list(wh_list, wh_crazy_dict), "whore"]

    $ renpy.block_rollback()

    while perform_events:

        $ ev = perform_events.pop(0)
        $ predict_next_img([perform_events, farm_events, resting_events]) # Chris12's suggestion

        if ev == "job_matchmaking":
            if not persistent.skipped_events["Matchmaking"]:
                $ tt = show_tt("top_right")

                call screen matchmaking(*latest_ent_match)

        elif ev == "wh_matchmaking":
            if not persistent.skipped_events["Matchmaking"]:

                call screen matchmaking(*latest_wh_match)

        else:
            call show_night_event(ev) from _call_show_night_event

    ## Change Brothel Rep

    python:
        old_rep = brothel.rep

        served = sum(1 for c in customers if c.got_entertainment)
        entertained = sum(1 for c in customers if c.got_entertainment == c.wants_entertainment)
        laid = sum(1 for c in customers if c.got_sex_act)
        satisfied = sum(1 for c in customers if c.got_sex_act == c.wants_sex_act)

#         text1 = "{size=-2}" + str(len(customers)) + " customer" + plural(len(customers)) + " came to your brothel. " + str(served) + " got attended (" + str(entertained) + " entertained), " + str(laid) + " got laid (" + str(satisfied) + " satisfied)."

        log.add_report(event_color["good"] % (str(len(customers)) + " customer" + plural(len(customers)) + " came to your brothel. " + str(served) + " got attended (" + str(entertained) + " entertained), " + str(laid) + " got laid (" + str(satisfied) + " satisfied)."))

        rep_chg = sum(c.get_reputation_change() for c in customers)
        rep_chg = brothel.change_rep(rep_chg)

#         text1 += " Brothel reputation: " + str(round_int(brothel.rep)) + " (" + plus_text(round_int(rep_chg)) + ")"

        log.add_report(event_color["rep"] % ("Brothel reputation changed from %s to %s (%s)" % (str_int(old_rep), str_int(brothel.rep), plus_text(round_int(rep_chg)))))

        log.track("served", served)
        log.track("entertained", entertained)
        log.track("laid", laid)
        log.track("satisfied", satisfied)
        log.track("new rep", brothel.rep)
        log.track("rep change", rep_chg)

    ## Customer satisfaction screen

    $ customers.sort(key=lambda x: x.reputation_change, reverse=True)

    $ renpy.say("", "End of whoring phase", interact=False)

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
            if debug_mode:
                $ renpy.notify("Showing event")
            call show_relationship_change(girl1, girl2, old_status, new_status) from _call_show_relationship_change

            if new_status == "friend":
                $ log.add_report(event_color["good"] % ("%s and %s have become friends." % (girl1.fullname, girl2.fullname)))
            elif new_status == "rival":
                $ log.add_report(event_color["bad"] % ("%s and %s have become rivals." % (girl1.fullname, girl2.fullname)))
            elif new_status == "normal":
                $ log.add_report("%s and %s are no longer %ss." % (girl1.fullname, girl2.fullname, old_status))

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

    ## Girl skill improvements

        for girl in MC.girls: # farm girls are excluded from catch up effects
            if girl.get_effect("special", "skill catch up") and len(MC.girls) > 1: # Avoid infinite loop if she's alone
                i = 0
                while i < girl.rank:
                    girl2 = rand_choice(MC.girls)
                    if girl2 != girl:
                        for stat in gstats_main + gstats_sex:
                            if girl.get_stat(stat, raw=True) > girl2.get_stat(stat, raw=True) + 1:
                                if dice(250) > girl2.get_stat(stat, raw=True): # Stats are harder to raise as they grow
                                    girl2.change_stat(stat, 1)
                        i += 1

    ## Girl level up
        for girl in MC.girls:
            if girl.ready_to_level():
                girl.level_up()

            for act in [girl.job] + all_sex_acts:
                if girl.ready_to_job_up(act):
                    girl.job_up(act)



    ## Clean up the brothel

        brothel.change_dirt(-1 * brothel.get_maintenance())


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

        gold_text = "You paid " + '{:,}'.format(round_int(log.upkeep)) + " upkeep for your girls"

        if free_girl:
            gold_text += " (free upkeep: " + free_girl.name + ")"

        if working_girls:
            log.costs = brothel.get_adv_cost() + brothel.get_sec_cost() + brothel.get_maintenance_cost()
            gold_text += ". You paid " + '{:,}'.format(round_int(log.costs)) + " for your brothel services."

        else:
            log.costs = brothel.get_maintenance_cost()
            gold_text += ". " + brothel.name + " was closed, so you sent the security and advertising crews home. You paid " + '{:,}'.format(round_int(log.costs)) + " for maintenance."

        loan_payment = MC.repay_loan()

        if loan_payment:
            log.costs += loan_payment
            gold_text += " You paid " + str(round_int(loan_payment)) + " gold to the bank for your loan."

        bonus = log.gold_made * min((brothel.get_effect("boost", "income")-1, 2.5)) # Maximum achievable income boost is hard-capped at +250%
        log.gold_made += bonus

        gold_text += "\nYour girls brought in " + '{:,}'.format(round_int(log.gold_made)) + " gold"

        if bonus > 0:
            gold_text += " (" + event_color["a little good"] % ("income bonus: " + str_int(bonus)) + ")"
        elif bonus < 0:
            gold_text += " (" + event_color["a little bad"] % ("income penalty: " + str_int(bonus)) + ")"

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
                gold_text += " and " + str_int(nb) + " " + resource

        log.net = round_int(log.gold_made - log.upkeep - log.costs)

        MC.gold += log.net
        NPC_taxgirl.MC_income += (log.net * brothel.get_effect("boost", "taxable net income"))

        if log.net > 0:
            gold_text += ", netting you a profit of {color=[c_emerald]}{b}" + '{:,}'.format(log.net) + "{/b} gold{/color}."
        elif log.net < 0:
            gold_text += ", failing to make a profit. You lost {color=[c_red]}{b}" + '{:,}'.format(-1*log.net) + "{/b} gold{/color}."
        else:
            gold_text += ", breaking even. You made {color=[c_red]}{b}0{/b} gold.{/color}"

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

        ev = Event(Picture(pic, "events/" + pic), text = gold_text, changes = "\n{size=+12}Y" + str(calendar.year) + " M" + str(calendar.month) + " D" + str(calendar.day) + "\n" + calendar.get_weekday(), sound = s_cash, type ="UI")


#### SHOW NIGHT RECAP ####

    $ renpy.block_rollback()
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

            cast_text = MC.autocast(spell, "morning")

            if cast_text:
                log.add_report(cast_text)

    ## Auto-extract resources

        for res in build_resources: # Receives one free resource for each extractor
            if auto_extractors[res + " ON"]:
                MC.gain_resource(res, message=False)
                auto_extractors[res + " durability"] -= 1
                if dice(100) > auto_extractors[res + " durability"]:
                    calendar.set_alarm(calendar.time + 1, Event(label="break_extractor", object=res))

    ## Check if girls ran away

        for girl in MC.girls:

            check = girl.run_away_check()

            if check == "runaway" and girl not in away_girls:
                girl.ran_away_counter = 0
                renpy.call("run_away", girl)
                girl.add_log("run_away", delay=-1)

            elif check == "warning":
                renpy.say (sill, "Warning! [girl.fullname] is unhappy and grumbling about running away...")

    ## Check if girls are tired

        for girl in MC.girls:
            if girl.tired_check(): # Returns True if tired warning
                renpy.say (sill, "Warning! [girl.fullname] is getting tired...")
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
            renpy.say(gizel, "A level " + str(mn.level) + " " + mn.type + " has been retired because of wounds or damage it sustained.")

    ## Update girl portraits and profiles

        for girl in MC.girls:

            girl.refresh_pictures()

    ## Check if goal has been reached

    if game.goals_reached():
        call reached_goal from _call_reached_goal

#### PLAYING CONDITIONAL EVENTS

    call play_events(type = "morning") from _call_play_events_1 # Note: Morning events are set with the new day's date: beware of the confusion

    $ test_achievements(["months", "friends", "rivals", "rep"])

#### CHECK FOR BANKRUPTCY ####

    if MC.gold < 0:
        $ calendar.set_alarm(calendar.time, StoryEvent(label="no_money"))

#### RETURN TO MAIN SCREEN ####

    jump main

#### END OF BK END DAY FILE ####
