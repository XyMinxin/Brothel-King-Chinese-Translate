#### SECURITY EVENTS ####


label security(working_girls, ev_type=None): # Happens when the threat level overcomes the event threshhold. ev_type may be provided for debugging.

    $ debug_notify("Security event")
    $ game.track("security events", 1)

    #### HOW IT WORKS ####
    ## Threats builds up every night depending on total security, with a minimum of 1.
    ## The brothel starts at alert level 1. After threat reaches 10, 30 and 50, an event happens.
    ## Depending on difficulty, there is a 'grace' period at the start of a game and after a security event, where threat doesn't build-up.
    ## Some events cause escalation to a higher alert level. There are 3 alert levels.
    ## After a security event happens (not escalating), threat is reset to 0.

    ## Pick targets for attacks

    if working_girls:
        $ target_girls = working_girls
    elif MC.girls:
        $ target_girls = MC.girls
    else: # In the unlikely case a player has no girls in the brothel when a security event procs
        return

    ## Get event type

    $ ev_type_list = security_events[brothel.alert_level]

    # Escalating events get added if the alert level is below maximum
    if district.rank > brothel.alert_level and brothel.alert_level < 3:
        $ ev_type_list += [("ramp up", 30), ("escalate", 10)]

    if not ev_type:
        $ ev_type = weighted_choice(ev_type_list)

    if ev_type != "quiet" and brothel.get_effect("special", "security block"): # Applies trainer effect
        $ notify("Suzume prevented a security breach.", pic="NPC/Suzume/roof.webp")
        return

    ## ALERT LEVEL 3 ##

    # Because those events are more complex, they are not generated as regular night events

    if ev_type == "raid": # A raiding party blitzes the brothel, trying to kidnap one of your girls. 2-4 girls are targeted, you can only defend one yourself.

        python:
            attackers = rand_choice(("marauding ogres", "gooey monsters", "rogue mercenaries"))
            if attackers == "gooey monsters" and is_censored("monster"):
                attackers = "rogue mercenaries"

            pic1 = "events/" + rand_choice(security_pics["brothel defense"])
            pic2 = "events/" + rand_choice(security_pics[attackers])

            target_girls = rand_choice(target_girls, 1 + dice(3))
            kidnap_target = rand_choice(target_girls)
            girl_nb = len(target_girls)

            defended_girls = []
            hurt_girls = []
            kidnapped_girls = []

        show expression pic1 at top as bg with dissolve

        play sound s_crowd_riot

        security "{color=[c_red]}[brothel.name] is being raided by [attackers]!{/color}\nYou rush outside with the defenders."

        play sound s_clash
        pause 0.2
        play sound2 s_clash

        security "Your first assault breaks their line and they quickly scatter. That's when you hear a scream."

        play sound s_woman_scream
        ev_girl1 "EEEEK!" with vpunch

        hide bg
        show expression bg_bro at top
        with dissolve

        security "Some of the attackers have sneaked out the back of [brothel.name] while the security guards were distracted! You rush back to the brothel to help.\n{color=[c_red]}[girl_nb] of your girls are under attack, but you can only help one!{/color}"

        python:
            menu_list = [["Choose a girl to defend", None]]

            for girl in target_girls:
                menu_list.append([girl.fullname.capitalize() + ", Level " + str(girl.level) + ", Defense " + str_int(girl.get_defense()), girl])

        $ girl = menu(menu_list)

        python:
            for g in target_girls:
                if girl == g:
                    g.love += 5
                else:
                    g.love -= 5

        hide bg_bro
        $ renpy.show_screen("show_event", girl.profile, x=config.screen_width, y=int(config.screen_height*0.8), _layer = "master")
#        show screen show_event(girl.profile, x=config.screen_width, y=int(config.screen_height*0.8))
        with dissolve

        play sound s_scream_loud
        girl.char "EEEEK!!! Master, help me!" with vpunch

        if attackers == "marauding ogres":
            $ strength = 8
            $ magic = 5
            $ hit = "the handle of his giant axe"
            show ogre at totheleft as enemy with dissolve

        elif attackers == "gooey monsters":
            $ strength = 4
            $ magic = 7
            $ hit = "a whipping tentacle"
            show sewer_monster as enemy at truecenter with dissolve

        elif attackers == "rogue mercenaries":
            $ strength = 6
            $ magic = 6
            $ hit = "the flat of his sword"
            show masked_thug at totheleft as enemy with dissolve

        "You reach [girl.fullname] just in time to confront her attacker."

        if attackers == "marauding ogres":
            show ogre at left as enemy with move

        elif attackers == "gooey monsters":
            show sewer_monster as enemy at centerleft with move

        elif attackers == "rogue mercenaries":
            show masked_thug at left as enemy with move

        # Pick challenge
        $ tt = show_tt("top_right")
        $ chal = renpy.call_screen("challenge_menu", challenges=[("Fight", "fight", strength), ("Fire a spell", "cast", magic)])
        hide screen tool

        if chal == "fight":
            $ renpy.block_rollback()

            play sound s_sheath

            call challenge(chal, strength) from _call_challenge_34 # result is stored in the _return variable
            $ r = _return

            if r:
                play sound s_sheath

                with vpunch

                play sound2 s_crash

                hide enemy with pixellate

                "With righteous fury, you cut down your opponent before he has a chance to react.\n{color=[c_green]}[girl.name] is safe.{/color}"

            else:
                play sound s_punch

                with vpunch

                "Your opponent strikes the air out of you with a mighty blow from [hit]. You are sent flying backwards. Your head hits something hard."


        elif chal == "cast":
            $ renpy.block_rollback()

            play sound s_spell

            call challenge(chal, magic) from _call_challenge_35 # result is stored in the _return variable
            $ r = _return

            if r:
                play sound s_lightning
                with flash

                if attackers == "rogue mercenaries":
                    show thug2 burnt as enemy with move:
                        xalign 0.4
                        time 0.5

                hide enemy with pixellate

                "The assailant is pulverized by a mighty bolt of lightning from your staff. {color=[c_green]}[girl.name] is safe.{/color}"

            else:
                play sound s_fizzle

                "As you try to cast a spell, you realize too late your opponent is protected by a magic ward. He hits you hard with [hit], sending you crumbling on the floor."

                play sound s_punch
                with vpunch

        if r:

            $ target_girls.remove(girl)
            $ defended_girls.append(girl)

            $ text1 = "While you were fighting, the other attackers rampaged through your brothel. "

        else:
            if girl.test_shield():
                play sound s_spell
                $ sec_pic = "events/" + rand_choice(security_pics["girl shield"])

                hide screen show_event
                show screen show_event(Picture(path=sec_pic), x=config.screen_width, y=int(config.screen_height*0.8))
                with dissolve

                "[girl.fullname] is left alone, but her magic shield blinded her attacker and protected her from harm."

                $ target_girls.remove(girl)
                $ defended_girls.append(girl)

            elif girl.get_defense() + dice(6) >= strength:
                play sound s_sheath

                python:
                    sec_pic = girl.get_pic("fight", strict=True, naked_filter=True, soft=True)
                    if not sec_pic:
                        sec_pic = girl.get_pic("fight", strict=True)
                        if not sec_pic:
                            sec_pic = Picture(path="events/" + rand_choice(security_pics["default girl fight"]))

                hide screen show_event
                scene black with fade
                show screen show_event(sec_pic, x=config.screen_width, y=int(config.screen_height*0.8))
                with dissolve

                "[girl.fullname] is left to fend alone for herself, but she is far from defenseless. Attacking from behind while your opponent is busy pummeling you, she stabs him in the back repeatedly, and he runs away squealing."

                $ target_girls.remove(girl)
                $ defended_girls.append(girl)

            else:
                play sound s_woman_scream

                python:
                    sec_pic = girl.get_pic("hurt", not_tags=["rest"], naked_filter=True, soft=True, strict=True)
                    if not sec_pic:
                        sec_pic = girl.get_pic("hurt", not_tags=["rest"], strict=True)
                        if not sec_pic:
                            sec_pic = Picture(path="events/" + rand_choice(security_pics["assassin"]))

                hide screen show_event
                scene black with fade
                show screen show_event(sec_pic, x=config.screen_width, y=int(config.screen_height*0.8))
                with dissolve

                "[girl.fullname] is left to fend alone for herself. She tries to grab a stick for defense, but her opponent swipes it away effortlessly."

                girl.char "Nooo!!!" with vpunch

            $ lost_gold = int(MC.gold * 0.15)
            $ MC.gold -= lost_gold
            $ text1 = "While you were passed out, the [attackers] ransacked your brothel, {color=[c_red]}taking off with [lost_gold] gold.{/color} "

        python:

            for girl in target_girls:
                if girl.test_shield():
                    defended_girls.append(girl)
                elif girl.get_defense() + dice(6) >= strength + dice(6):
                    defended_girls.append(girl)
                elif girl == kidnap_target:
                    kidnapped_girls.append(girl)
                    MC.girls.remove(girl)
                    game.kidnapped.append(girl)
                    girl.kidnapper = attackers
#                    text2 += "\n{color=[c_red]}" + girl.fullname + " has been kidnapped!{/color}"
                    girl.track_event("kidnapped", arg = attackers + ".")
                else:
                    girl.get_hurt(1+dice(4))
                    if girl.hurt > 0:
                        hurt_girls.append(girl)
                        girl.track_event("hurt", arg = attackers + ".")


            if len(defended_girls) > 1:
                text1 += and_text([g.fullname for g in defended_girls]) + " defended themselves. {color=[c_red]}"
            elif len(defended_girls) > 0:
                text1 += defended_girls[0].fullname + " defended herself. {color=[c_red]}"

            if len(hurt_girls) > 1:
                text1 += and_text([g.fullname for g in defended_girls]) + " were hurt.\n"
                log.add_report("{color=[c_red]}Security alert! " + and_text([g.fullname for g in defended_girls]) + " were hurt.{/color}")
            elif len(hurt_girls) > 0:
                text1 += hurt_girls[0].fullname + " was hurt.\n"
                log.add_report("{color=[c_red]}Security alert! " + hurt_girls[0].fullname + " was hurt.{/color}")

            if kidnapped_girls:
                text1 += "{b}" + kidnapped_girls[0].fullname + " was kidnapped!{/b}"
                log.add_report("{color=[c_red]}Security alert! {b}" + kidnapped_girls[0].fullname + " was kidnapped!{/b}{/color}")

        hide screen show_event
        scene black

        if hurt_girls:
            show expression pic2 at top
        else:
            show expression pic1 at top
        with fade

        if kidnapped_girls or hurt_girls:
            $ renpy.say(security_breach, text1)
        else:
            $ renpy.say(security, text1)

        $ brothel.reset_threat()


    elif ev_type == "siege": # A sieging party assaults the brothel, forcing your guards and girls to defend themselves. You confront their leader. Str helps with the leader fight, Spi protects some of your girl, Cha increases guards fighting value. Winning against the leader earns a rare item

        python:
            pic = "events/" + rand_choice(security_pics["siege"])

            allies = brothel.security

            if game.chapter == 4:
                enemies = 16 + dice(6)
                war_machines = 1 + dice(2)
            elif game.chapter == 5:
                enemies = 21 + dice(8)
                war_machines = 1 + dice(3)
            elif game.chapter == 6:
                enemies = 28 + dice(10)
                war_machines = 2 + dice(3)
            elif game.chapter == 7:
                enemies = 42 + dice(12)
                war_machines = 3 + dice(3)
            else: # for debugging
                enemies = 8 + dice(4)
                war_machines = 2

            loot = enemies * 150 + war_machines * 600

            if enemy_general.has_trait("Warrior"):
                enemy_g = "mercenary captain"
            elif enemy_general.has_trait("Caster"):
                enemy_g = "freelance sorceress"

            general_defeats = 0
            fatigue = -1

            allies_factor = brothel.get_effect("boost", "security")
            enemy_factor = 1.0


        $ log.add_report("{color=[c_red]}Security alert! " + str(enemies) +  " mercenaries led by a " + enemy_g + " besieged the brothel.{/color}")

        show expression bg_bro at top

        "You're standing on the doorstep of your brothel, ready to greet customers. Long minutes pass... But still, no one comes. You have a bad feeling about this."

        play sound s_surprise

        sill sad "Master! Look!"

        hide bg_bro
        show expression pic at top
        with dissolve

        "First a couple silhouettes emerge on the horizon, then three, then four, and suddenly a large force of soldiers and monsters is massing in the streets facing your brothel."

        "A security guard comes running towards you as if firehounds from the seven hells were on his heels."

        guard "Boss! I counted [enemies] of them. And they also have [war_machines] war machines! They are led by [enemy_general.fullname], a renowned [enemy_g]."

        you "Damn it, mercenaries! They're besieging us! Quick, get the girls inside, gather everyone, and get in battle formation!"

        menu:
            security "{b}Battle Phase 1{/b}\nYou must defend the Brothel! What do you do?"

            "Charge into the fray (use Strength to fight the enemy)":
                $ renpy.block_rollback()
                play sound s_sheath
                you "To battle!!!" with vpunch
                $ r = "fight"

            "Destroy their war machines (use Spirit to cast a spell on them)":
                $ renpy.block_rollback()
                play sound s_spell

                if dice(6) == 6:
                    you "C'm'on baby, light my fire!"
                else:
                    you "Let's see how well those machines burn!"
                $ r = "cast"

            "Lead from behind (use Charisma to improve your troops' morale)":
                $ renpy.block_rollback()
                play sound s_sheath
                $ MC.rand_say(["ev: Men, get ready!!! We will slaughter them where they stand!", "gd: Brothers and sisters! We didn't choose to start this fight, but we will surely end it!", "ne: Men, fight them smart, fight them hard! Be the first one on your block to get a confirmed kill!"])
                $ r = "rally"

                call challenge(r, game.chapter) from _call_challenge_36
                $ result = _return

                if result:
                    $ d = dice(6)
                    if d == 6:
                        play sound s_crowd_cheer
                        "Your speech galvanizes your troops and they raise their swords as one in defiance. Their morale is {b}very high{/b}."
                        $ allies_factor += 0.3
                    elif d > 1:
                        "Your troops are energized by your speech. Their morale is {b}high{/b}."
                        $ allies_factor += 0.2
                    else:
                        "Your speech helps a little, but you can see your troops are nervous in the face of battle. Morale improved slightly."
                        $ allies_factor += 0.1


            "Challenge their leader (use Strength to attack the [enemy_g])" if enemy_general.has_trait("Warrior"):
                $ renpy.block_rollback()
                play sound s_sheath
                you "Leave their general to me... I will end this!" with vpunch
                $ r = "duel"

            "Challenge their leader (use Spirit to attack the [enemy_g])" if enemy_general.has_trait("Caster"):
                $ renpy.block_rollback()
                play sound s_dress
                you "Leave the magic user to me... I will deal with her!" with vpunch
                $ r = "duel"

        # War Machines phase

        if r == "cast":
            "Rushing up the stairs, you run for the brothel battlements."

            you "To say they called me crazy when I insisted the brothel needed battlements! Ha!"

            "Reaching atop the battlements, you get a field view of the battle. The siege engines are getting ready to fire at your troops. You lift your staff into the air and ready a spell."


            if dice(6) == 6:
                you "Burn, burn, yes ya gonna burn!"
            else:
                you "You think you're safe uphill? Ha! PYROBLAST!" with vpunch

            with vpunch
            play sound s_fire

            # Challenge
            call challenge(r, 0, score=True, score_limit=3) from _call_challenge_37# result is stored in the _return variable (MC Spirit + d6 - 3)
            $ score = round_int(_return)

            if score < 3:
                security_breach "Your fireball hits the ground near the war machines and sets fire to the grass. However, some of the mercenaries stand ready with water buckets and they quickly extinguish the fire."

                you "Damn!"

                security_breach "{b}Battle Phase 2{/b}\nThe war machines get ready to fire."

            else:
                $ destroyed = score // 3
                if destroyed > war_machines:
                    $ destroyed = war_machines
                $ war_machines -= destroyed

                play sound s_fire
                pause 0.2
                play sound2 s_fire
                with doubleflash

                security "Your fireball hits right into the midst of the war machines, sending [destroyed] of them up in flames."

                if war_machines:
                    security_breach "{b}Battle Phase 2{/b}\nThe remaining war machines get ready to fire."
                else:
                    security "{b}Battle Phase 2{/b}\nNo war machines are left to fire."

        else:
            security_breach "{b}Battle Phase 2{/b}\nThe war machines get ready to fire."

        if war_machines:
            $ damage = dice(3, int(war_machines))
            if damage > allies:
                $ damage = allies
            $ allies -= damage

            play sound s_fire
            pause 0.5
            play sound2 s_fire

            with vpunch

            $ renpy.say(security_breach, rand_choice(["Shrapnel bursts among your troops, wounding [damage] of them.", "Fire rains down on your troops, wounding [damage].", "Cannonballs mow down [damage] of your security guards.", "A huge stone crashes among your troops, wounding [damage]."]))

        # Enemy charge

        if enemies > allies:
            security_breach "{b}Battle Phase 3{/b}\nThere are [enemies] enemies facing your [allies] remaining guards. They have the advantage, and they know it."
            $ enemy_factor = 1.1
            play sound s_crowd_riot
            with vpunch
            enemy_general.char "CHAAAARGE!!!"

        elif enemies < allies:
            security "{b}Battle Phase 3{/b}\nThere are [enemies] enemies facing your [allies] remaining guards. You have the advantage, and their lines seem to falter."
            $ enemy_factor = 0.9
            play sound s_crowd_riot
            with vpunch
            you "CHAAAARGE!!!"
        else:
            security "{b}Battle Phase 3{/b}\nThere are [enemies] enemies facing your [allies] remaining guards. Your forces are evenly matched."
            play sound s_crowd_riot
            with vpunch
            guard "CHAAAARGE!!!"

        $ allies_damage = round_int(allies * allies_factor) + dice(6) - 3
        $ enemy_damage = round_int(enemies * enemy_factor) + dice(6) - 3

        play sound2 s_clash
        pause 0.5
        play sound2 s_clash

        if r == "duel":
            "The first lines of battle crash together. Ignoring the fighting around you, you force your way towards the enemy general."

            python:
                g_pic = enemy_general.get_pic("fight", soft=True, strict=True)
                if not g_pic:
                    g_pic = Picture(path="events/" + rand_choice(security_pics["default girl fight"]))

            hide pic
            show screen show_event(g_pic, x=config.screen_width, y=int(config.screen_height*0.8))
            with dissolve

            "She appears before you, and you yell a challenge."

            you "You! [enemy_general.name]! Prepare to be defeated!"

            play sound s_surprise

            enemy_general.char "Ha! Fancy yourself a fighter, pimp boy?"

            play sound s_clash

            if enemy_general.has_trait("Warrior"):
                "The mercenary draws out her weapon and rises to meet you."
                call challenge("fight", game.chapter + 1) from _call_challenge_38
                $ result = _return

                if result:
                    play sound s_crash
                    with vpunch
                    "You first hit bashes her shield hard, splitting it. She defends against your furious onslaught, parrying with her sword, but it is clear she is outmatched."

                    enemy_general.char "Men! Help me!"

                    play sound s_sheath
                    pause 0.3
                    play sound s_sheath
                    with vpunch

                    "Two of her bodyguards leap to her defense, but before long, they lay inert at your feet. The [enemy_g] took advantage of the distraction to run away."
                    $ allies_damage += 2
                    $ general_defeats = 1

                else:
                    play sound s_clash
                    pause 0.3
                    play sound2 s_clash

                    with vpunch

                    "She answers your attacks blow for blow, and you feel she is no small time fighter. Little by little, you lose ground."

                    you "Damn, she's strong. Men! To me!"

                    play sound s_sheath
                    pause 0.3
                    play sound s_sheath
                    with vpunch

                    "Two of your guards intervene, but she quickly disposes of them. Before you have a chance to attack her again, you are engulfed into the fray of battle."
                    $ enemy_damage += 2
                    $ fatigue = -2

            elif enemy_general.has_trait("Caster"):
                "The sorceress begins an incantation. You must stop her, fast!"
                call challenge("control", game.chapter + 1) from _call_challenge_39
                $ result = _return

                if result:
                    play sound s_spell
                    with flash
                    "You easily dispel her magic barrier, and raise your weapon to hit her. She barely has time to raise her staff in defense, and you break it in two."

                    enemy_general.char "Demons! Familiar! Help me!"

                    play sound s_fire
                    pause 0.3
                    play sound s_fire
                    with doubleflash

                    "A couple of strange, impish creatures leap to her defense, but you fry them with a firebolt. When the smoke dissipates, the [enemy_g] has retreated out of your reach."
                    $ allies_damage += 2
                    $ general_defeats = 1

                else:
                    play sound s_lightning

                    with flash

                    "A bolt of lightning hits at your feet, sending you flying backwards. When you come back to your senses, the sorceress is looming over you, muttering a spell, ready to deal the killing blow."

                    you "Men! Attack her! Quick! *frantic*"

                    "A couple of your guards run at her, but she blows them to smithereens with her spell. Using the distraction, you crawl back behind your line of battle before she has a chance to ready an attack again."
                    $ enemy_damage += 2
                    $ fatigue = -2

        elif r == "fight":

            "The first lines of battle crash together. You stand at the forefront, slashing at enemies left and right."

            call challenge(r, game.chapter - 1, score=True) from _call_challenge_40
            $ score = round_int(_return)

            if score < 0:
                play sound s_clash
                pause 0.3
                play sound2 s_clash

                security_breach "In spite of your fighting skills, you are not achieving much, and soon you find yourself surrounded by five enemies. As you try to defend yourself, one of them slams your leg with a warhammer and you fall down flat in the mud. He gets ready for the killing blow, but your men counter-charge and one brings you inside the brothel to safety."
                $ fatigue = -3
            else:
                play sound s_sheath
                pause 0.3
                play sound2 s_sheath

                with hpunch

                security "You deal mighty blows to the enemies, grievously wounding one of their champions and routing [score] of his followers."
                $ allies_damage += 1 + score

        if allies_damage > enemies:
            $ allies_damage = enemies
        if enemy_damage > allies:
            $ enemy_damage = allies

        $ allies -= enemy_damage
        $ enemies -= allies_damage

        # Finish fight

        if allies and enemies:
            security "[enemy_damage] of your allies and [allies_damage] of your enemies have fallen. There are [enemies] enemies remaining against your [allies] standing guards."

            if enemies < allies:
                $ d = dice(3) + game.chapter
                $ enemies += d
                security_breach "The enemies have brought [d] reinforcements! There are now [enemies] enemies against your [allies] guards."

            while allies and enemies:

                if enemies > allies:
                    extend "\nThey have the advantage, and they know it. Their morale improves."
                    $ enemy_factor = 1.1
                    enemy_general.char "All right, men! Finish the job!"

                elif enemies < allies:
                    extend "\nYou have the advantage, and it seems they hesitate to attack again."
                    $ enemy_factor = 0.9
                    you "Let's end this."
                else:
                    extend "\nYour forces are evenly matched."
                    guard "For honor, glory, and a fair and regulated competitive environment for all lawful pleasure businesses!"
                    $ enemy_factor = 1.0

                $ allies_damage = round_int(allies * allies_factor)
                $ enemy_damage = round_int(enemies * enemy_factor)

                if allies_damage > enemies:
                    $ allies_damage = enemies
                if enemy_damage > allies:
                    $ enemy_damage = allies

                $ allies -= enemy_damage
                $ enemies -= allies_damage

                security "Your forces clash again with the enemy."

                if allies and enemies:
                    security "[enemy_damage] of your men fall, while [enemy_damage] foes are defeated. They are now [enemies] enemies left and [allies] standing guards."

        if not enemies:
            security "[enemy_damage] of your allies and [allies_damage] of your enemies have fallen. All the enemies are wounded or routed. You {b}win{/b} this battle."
            $ round2 = False
        elif not allies:
            security_breach "The enemy has wiped out your security guards. You take refuge inside the brothel with your girls and try to organize what little defenses you have."
            $ round2 = True

        # End of round 1

        if not round2:
            $ MC.gold += loot
            $ ("You let the surviving guards loot the battlefield, getting your share of " + event_color["good"] % "[loot] gold" + ".")

            $ log.add_report("{color=[c_green]}Battle results: " + str_int(loot) + " gold recovered.{/color}")

            if general_defeats > 0:
                $ it = get_rand_item("rare")

                $ item_name = "{b}" + article(it.name.lower()) + "{/b}"

                "Your men found something [enemy_general.fullname], the enemy general left behind. You have received [item_name]."
                $ MC.items.append(it)

                $ log.add_report("{color=[c_green]}Battle results: " + it.name + " recovered.{/color}")

        else:
            # Round 2 is inside the brothel

            hide screen show_screen
            scene black
            with fade
            show expression bg_bro at top with dissolve

            $ fighting_girls = [g for g in MC.girls if g.hurt <= 0]
            $ hurt_girls = []
            $ random.shuffle(fighting_girls)
            $ girl_def_bonus = 0

            $ security("{b}Battle Phase 4{/b}\nThe enemy's [enemies] remaining soldiers are at your gates! You are suffering from " + event_color["bad"] % "{b}battle fatigue{/b}" + ", temporarily reducing all your skills by [fatigue]. What do you do?")

            menu:
                extend ""

                "Defend your girls (use Strength to fight the enemy)":
                    $ renpy.block_rollback()
                    play sound s_sheath
                    you "Bring it on!"
                    $ r = "fight"

                "Protect your girls (use Spirit to shield some of your girls)":
                    $ renpy.block_rollback()
                    play sound s_spell
                    you "Every one, get inside the pentagram!"
                    $ r = "cast"

                    call challenge(r, 3, score=True, bonus=fatigue) from _call_challenge_41 # result is stored in the _return variable (MC Spirit + d6 - 3)
                    $ score = round_int(_return)

                    if score >= 0:
                        $ protected = 1 + score
                        "You cast a protective shield over [protected] of your girls."

                        python:
                            unprotected_girls = [g for g in fighting_girls if not g.get_effect("special", "shield", raw=True)]

                            for i in range(protected):
                                if unprotected_girls:
                                    unprotected_girls.pop().add_shield()
                                else:
                                    rand_choice(fighting_girls).add_shield()

                "Encourage your girls to fight (use Charisma to boost your girls' fighting skill)":
                    $ renpy.block_rollback()
                    play sound s_roar
                    $ MC.rand_say(("Brace yourself! The enemy is coming, you know what to do!", "ev: All right, bitches, prepare to defend your miserable lives! You'd better not disappoint me!", "gd: All right everyone, remember your training, and don't take any unnecessary risks!", "ne: Babes, this is it. I'm counting on you!"))
                    $ r = "rally"

                    call challenge(r, game.chapter, bonus=fatigue) from _call_challenge_42
                    $ result = _return

                    if result:
                        $ d = dice(6)
                        if d == 6:
                            $ narrator("You look at your girls and cannot believe what you see. They are awaiting the enemy as one, supporting each other, with a fearsome glint in their eye. They are ready, and will fight the enemy with all they have. " + event_color["good"] % "+3 to all girls defense.")
                            $ girl_def_bonus += 3
                        elif d > 1:
                            $ narrator("Your speech steels your girls's resolve. They will be fighting harder against the enemy. " + event_color["good"] % "+2 to all girls defense.")
                            $ girl_def_bonus += 2
                        else:
                            $ narrator("You give your last orders, helping a girl don a leather vest, commenting on another girl's footing. They are servants, not fighters, but this will have to do. " + event_color["good"] % "+1 to all girls defense.")


                "Intercept their leader (use Strength to attack the [enemy_g])" if enemy_general.has_trait("Warrior"):
                    $ renpy.block_rollback()
                    play sound s_sheath
                    "You leave your girls to fend for themselves and exit the brothel from a side door, determined to take out the enemy leader."
                    $ r = "duel"

                "Intercept their leader (use Spirit to attack the [enemy_g])" if enemy_general.has_trait("Caster"):
                    $ renpy.block_rollback()
                    play sound s_dress
                    "You leave your girls to fend for themselves and exit the brothel from a side door, determined to take out the enemy leader."
                    $ r = "duel"

            # Enemy attack

            "The enemy is battering on the brothel's door, and it almost looks as it will hold. However, after long seconds of anxious waiting, a massive hit blasts the doors open."

            play sound s_crash
            with vpunch

            if r == "fight":
                "When the dust settles, the enemy troops find you blocking their way, weapons drawn. They charge."

                call challenge("fight", game.chapter, score=True, bonus=fatigue) from _call_challenge_43
                $ score = round_int(_return)

                if score < 0:
                    play sound s_clash
                    pause 0.3
                    play sound2 s_punch
                    with vpunch

                    security_breach "The [enemies] remaining enemies come at you all at once, and their combined assault sends you falling backwards, only to be trampled upon as they keep on charging your girls, ignoring you as you lie defeated in the dust."

                    play sound s_crowd_riot

                else:
                    play sound s_clash
                    pause 0.3
                    play sound2 s_clash
                    with hpunch

                    $ damage = 1 + score
                    if damage > enemies:
                        $ damage = enemies
                    security "The enemy shock troopers rush through the door, but you are ready for them. You fight [damage] of them simultaneously, keeping them from attacking your girls."
                    $ enemies -= damage

                    you "You shall not pass!!!"

                    if enemies > 0:
                        "The [enemies] remaining enemies run past you into the brothel and engage your girls."
                        play sound s_crowd_riot
                    else:
                        play sound s_sheath
                        pause 0.3
                        play sound2 s_sheath
                        pause 0.2
                        play sound3 s_wscream

                        with vpunch

                        "The enemy troopers fall one by one. Hacking and slashing, you sever the last mercenary's sword-hand off, and he runs away screaming. Their general is nowhere to be seen. You {b}win{/b} this battle."

            else:
                "The enemies pour into the brothel and engage your girls."

                play sound s_crowd_riot

            if r == "duel":
                "Ignoring the fighting, you sneak past their front line, spotting [enemy_general.fullname], their general, giving orders from the back. {nw}"
                if enemy_general.has_trait("Warrior"):
                    play sound s_sheath
                    extend "Jumping out of hiding, you charge the enemy general with a war cry."

                    call challenge("fight", game.chapter + 1, bonus=fatigue, opponent_bonus=-general_defeats) from _call_challenge_44
                    $ result = _return

                    if result:
                        if general_defeats == 1:
                            play sound s_clash
                            with vpunch
                            "Before [enemy_general.name] can react, you strike her weapon from her hand and point your sword right at her throat."

                            you "Yield."

                            enemy_general.char "Damn you..."
                            $ general_defeats = 2

                            "Seeing their leader defeated, the rest of the mercenaries break their attack and scatter. You {b}win{/b} this battle."

                        else:
                            play sound s_crash
                            with vpunch
                            "She barely has time to raise her shield in time to block your attack. Her shield is split, and she recoils from the shock of your assault."

                            play sound s_surprise
                            enemy_general.char "You! Damn you!"

                            "She takes out a pouch from her vest, and throws it at your feet. Reflexively, you jump backwards."

                            play sound s_fire
                            with flash

                            "The pouch bursts open and lets out a heavy smoke cloud. When you manage to get past it, coughing, you see the enemy general is gone."

                            $ general_defeats = 1

                    else:
                        play sound s_clash
                        pause 0.3
                        play sound2 s_clash

                        with vpunch

                        "She turns to face you, and swiftly parries your attack. Her counter-attack is fast and deadly, and you do your best to defend yourself against a flurry of sword blows as she pushes you back."

                        play sound s_evil_laugh
                        enemy_general.char "Hahahaha! You are no match for me!"

                        play sound s_punch
                        with vpunch
                        "Taking advantage of your confusion, she kicks you hard in the groin with her steel greave. You cower from the pain, and when you lift your head up to try and see the next blow, she hits you square in the face with a mailed fist. You fall down in the mud, knocked out of your senses."

                elif enemy_general.has_trait("Caster"):
                    extend "Readying a spell, you come out of your hiding, aiming at her."
                    call challenge("control", game.chapter + 1, bonus=fatigue, opponent_bonus=-general_defeats) from _call_challenge_45
                    $ result = _return

                    if result:
                        if general_defeats == 1:
                            "Sensing your attack, the [enemy_g] turns around, reflexively looking for her battle staff, only to remember you broke it moments before."

                            play sound s_spell
                            with vpunch
                            "Your sleeping spell catches her unprepared, and she struggles as she tries to keep her eyelids open."

                            enemy_general.char "Y...You... Damn... You..."

                            "She falls down flat on her face and remains inert, slipping into unconsciousness. Seeing their boss defeated, the mercenaries break their attack and scatter. You {b}win{/b} this battle."
                            $ general_defeats = 2
                        else:
                            "Sensing your attack, the [enemy_g] turns around, lifting her magic staff in protection."

                            play sound s_lightning
                            with flash

                            "She barely manages to parry your lightning bolt, and her staff implodes to smithereens under the blow."

                            enemy_general.char "Impossible! *scared*"

                            play sound s_fire

                            "Grasping at an amulet she wears around her neck, she mutters a magic formula. She becomes translucent and vanishes into thin air as your second bolt hits the ground where she stood. Teleport magic!"

                            $ general_defeats = 1

                    else:
                        play sound s_spell
                        pause 0.3
                        play sound2 s_fire

                        with flash

                        "Detecting you before you have a chance to strike, she casts a firewall spell between you and her, cutting you off from the brothel and the battle. You can only watch, helpless, as the attack on [brothel.name] continues."

            if general_defeats < 2:

                python:
                    damage = 0

                    while enemies > 0 and fighting_girls:

#                        narrator(str(enemies) + " vs " + and_text([g.name for g in fighting_girls]))

                        for i in range(enemies):
                            if not fighting_girls:
                                break

                            if i < len(fighting_girls):
                                girl = fighting_girls[i-1]
                            else:
                                girl = fighting_girls[i % len(fighting_girls) - 1]

                            if girl.test_shield():
                                pass
                            elif girl.get_defense() + girl_def_bonus + dice(6) >= game.chapter - 1 + dice(6):
                                damage += 1
                            else:
                                girl.get_hurt(2+dice(4))
                                if girl.hurt > 0:
                                    hurt_girls.append(girl.fullname)
                                    fighting_girls.remove(girl)

                        enemies -= damage

                if enemies:
                    $ dirt = int(brothel.change_dirt(100*enemies))
                    if hurt_girls:
                        $ security_breach("[enemies] enemies overwhelmed your girls. " + event_color["bad"] % and_text(hurt_girls) + " were hurt" + ". The attackers set fire to your brothel before leaving, causing " + event_color["bad"] % "heavy damage (+[dirt] dirt)" + ".")
                    else:
                        $ security_breach("Your girls opposed no resistance to the enemy. The attackers set fire to your brothel before leaving, causing " + event_color["bad"] % "heavy damage (+[dirt] dirt)" + ".")

                    python:
                        burnt_furniture = rand_choice(brothel.furniture, dice(3)+1)

                        for furn in burnt_furniture:
                            if furn.rank > 0:
                                brothel.destroy_furniture(furn)

                    $ log.add_report("{color=[c_red]}Security alert! +" + str_int(dirt) + " dirt, " + and_text(hurt_girls) + " hurt.{/color}")

                else:
                    if hurt_girls:
                        $ dirt = int(brothel.change_dirt(200))
                        $ security_breach("[enemies] enemies attacked your girls. " + event_color["bad"] % and_text(hurt_girls) + " were hurt" + " before the attackers retreated. The fighting caused some damage to your brothel (" + event_color["bad"] % "+[dirt] dirt" + ")")
                        $ log.add_report("{color=[c_red]}Battle results: +" + str_int(dirt) + " dirt, " + and_text(hurt_girls) + " hurt.{/color}")

                    else:
                        $ dirt = int(brothel.change_dirt(100))
                        $ security("Your girls defended themselves tooth and nail and drove the [enemies] enemies away. They tried to set fire to your brothel as they were leaving, causing minimal damage (" + event_color["bad"] % "+[dirt] dirt" + ")")
                        $ log.add_report("{color=[c_red]}Battle results: No girls hurt. +" + str_int(dirt) + " dirt.{/color}")

                    $ MC.gold += loot
                    $ narrator("You and your girls tend to the wounded. After cleaning up the battlefield, you recover" + event_color["good"] % " [loot] gold" + " as loot.")

                    $ log.add_report("{color=[c_green]}Battle results: " + str_int(loot) + " gold recovered.{/color}")

                    if general_defeats > 0:
                        $ it = get_rand_item("rare")

                        $ item_name = "{b}" + article(it.name.lower()) + "{/b}"

                        "Your girls found something the enemy general [enemy_general.fullname] left behind."

                        call receive_item(it) from _call_receive_item_15

                        $ log.add_report("{color=[c_green]}Battle results: " + it.name + " recovered.{/color}")

            else:
                play sound s_gold
                $ MC.gold += loot
                $ narrator("You and your girls tend to the wounded. After cleaning up the battlefield, you recover" + event_color["good"] % " [loot] gold" + " as loot.")

                $ log.add_report("{color=[c_green]}Battle results: Enemy general captured!{/color}")

                play sound s_success

                "You have captured the enemy general, [enemy_general.fullname]!"

                $ unlock_achievement("general captured")
                $ log.add_report("{color=[c_green]}Security alert! " + str_int(loot) + " gold recovered.{/color}")

                play sound s_surprise

                enemy_general.char "W-What do you want to do with me? You bastard!"

                "She spits at you."

                $ price = enemy_general.get_price("buy")
                $ evil_price = price * 2

                show screen overlay
                $ tt = show_tt("top_right")
                show screen girl_stats(enemy_general, context="capture")
                with dissolve

                label enemy_general_captured():
                    security "You have captured the enemy general, [enemy_general.fullname]!"

                    menu:
                        "What do you want to do with her?"

                        "Keep her as a slave":

                            you "I will now keep you as my pet. It's only fair that you work here to rebuild the damage you caused."

                            enemy_general.char "Me? A whore??? No!!!"

                            call acquire_girl(enemy_general) from _call_acquire_girl_5

                            if _return:

                                you "Sill, take her away and have her branded."

                                play sound s_woman_scream

                            else:
                                you "Hmph, it's a shame, but it seems I can't take you right now."
                                jump enemy_general_captured

                        "Sell her as a slave for [price] gold":
                            $ MC.neutral += 1
                            you "I have no use for the likes of you. I'm sure you'll be an excellent slave to... Somebody."

                            enemy_general.char "Wait, no!!!"

                            $ MC.gold += price
                            play sound s_gold

                        "Sell her as sacrifice fodder for the blood islands for [evil_price] gold":
                            $ MC.evil += 2

                            you "Well well... A woman with such spirit would be a perfect sacrifice for the demon lords of the blood islands..."

                            play sound s_woman_scream

                            enemy_general.char "No!!! You can't be serious! *panic*"

                            you "Oh, but I am. Sill, take her to the blood slavers' galley. I never want to hear from that bitch again."

                            $ MC.gold += evil_price
                            play sound s_gold

                        "Make her swear an oath never to cross you again and let her go":
                            $ MC.good += 2

                            you "I'll let you go with a warning: leave town, and never come back."

                            play sound s_surprise

                            enemy_general.char "You... Really? Can I go?"

                            you "Yes, if you promise not to cause more trouble."

                            enemy_general.char "Very well, then, you have my word. I will leave Zan."

                    hide screen girl_stats
                    hide screen tool
                    hide screen overlay
                    with dissolve

                # Create new enemy general for the siege security event

                if dice(2) == 1:
                    $ enemy_general = get_girls(1, free=True, p_traits=["Warrior"])[0]
                else:
                    $ enemy_general = get_girls(1, free=True, p_traits=["Caster"])[0]
                $ enemy_general.love = -50

        $ brothel.reset_threat()


    ## ALERT LEVELS 1&2 ##

    else:
        $ ev_list = get_security_event(ev_type, target_girls)

        while ev_list:
            $ ev = ev_list.pop(0)
            call show_night_event(ev) from _call_show_night_event_6

    hide screen show_event
    hide screen night
    scene black
    with fade
    stop sound fadeout 3.0

    # Show security introduction

    if not story_flags["first security event"]:
        call security_introduction() from _call_security_introduction
        $ story_flags["first security event"] = True

    return

init -3 python:
    def get_security_event(ev_type, target_girls): # Returns a list of events to add to initial event list (alert levels 1 and 2 only)

        ev_list = []

        sec_char = security
        sec_pic = None
        sec_text = ""
        sec_changes = []
        sec_sound = None
        sec_with = None

        lost_gold = 0
        bonus_gold = 0
        hurt_girls = []

        # Check active defenses

        if MC.interactions > 0 or MC.get_effect("special", "defender"):
            MC_defense = MC.get_strength()
        else:
            MC_defense = 0

        guard_defense = brothel.get_security() / district.rank # For security events, guards bring less to the fight than MC and girl defense


        ## ALERT LEVEL 1 ##

        if ev_type == "thief":

            _min, _max = alert_limits1[game.chapter]

            if guard_defense >= _max:
                sec_pic = "events/" + rand_choice(security_pics["thief defense"])
                sec_sound = s_surprise
                bonus_gold = brothel.get_sec_cost()/2
                sec_text = (__("{color=[c_green]}Your guards caught a thief red-handed!{/color} They have their way with her all night as punishment.\nThey're in such good spirits that they accept to work for half the usual amount ({b}") + str_int(bonus_gold) + " gold{/b}).")

                log.add_report(__("{color=[c_green]}Security alert! No gold lost. ") + str(bonus_gold) + " gold recovered.{/color}")

            elif guard_defense + MC_defense >= _max:
                sec_pic = "events/" + rand_choice(security_pics["thief defense"])
                sec_sound = s_surprise
                MC.change_prestige(district.rank)
                sec_text = (__("{color=[c_green]}As you were patrolling, you caught a thief red-handed!{/color} She begged you to release her, so you came to an arrangement.\nYou let her go after a night of 'fun' in your basement. You have earned {b}prestige{/b}."))

                log.add_report(("{color=[c_green]}Security alert! No gold lost. Prestige earned.{/color}"))

            elif guard_defense + MC_defense >= _min:
                sec_pic = "events/" + rand_choice(security_pics["thief"])
                sec_text = __("{color=[c_lightgreen]}A ") + rand_choice([__("bold"), __("sneaky"), __("dirty"), __("notorious"), __("skilled")]) + __(" thief showed up, but your guards drove her away!{/color} You didn't lose any money.")

                log.add_report("{color=[c_green]}Security alert! No gold lost.{/color}")

            else:
                sec_char = security_breach
                sec_pic = "events/" + rand_choice(security_pics["thief"])
                sec_sound = s_evil_laugh
                lost_gold = round_int(MC.gold // 20)
                sec_text = (__("{color=[c_red]}A ") + rand_choice([__("bold"), __("sneaky"), __("dirty"), __("notorious"), __("skilled")]) + __(" thief managed to infiltrate your brothel and make away with {b}") + str_int(lost_gold) + "{/b} gold!{/color}")

                log.add_report("{color=[c_red]}Security alert! " + str(lost_gold) + " gold lost.{/color}")

            brothel.reset_threat()

        elif ev_type == "monster":

            _min, _max = alert_limits1[game.chapter]

            if guard_defense >= _max:
                sec_pic = "events/" + rand_choice(security_pics["monster defense"])
                sec_sound = s_clash
                for girl in working_girls:
                    girl.change_fear(-1)
                sec_text = __("{color=[c_green]}One of your guard slew a night beast they found lurking in a dark corner.{/color}\nYour girls are relieved.")

                log.add_report("{color=[c_green]}Security alert! No was one hurt. Fear lowered.{/color}")

            elif guard_defense + MC_defense >= _max:
                sec_pic = "events/" + rand_choice(security_pics["sword defense"])
                sec_sound = s_clash
                for girl in working_girls:
                    girl.change_love(1)
                sec_text = (__("{color=[c_green]}A monster leapt at your girls from a dark corner!{/color} Your quick combat reflexes saved you. The beast now lies lifeless at your feet. Your girls are impressed."))

                log.add_report("{color=[c_green]}Security alert! No one was hurt. Love raised.{/color}")

            elif guard_defense + MC_defense >= _min:
                sec_pic = "events/" + rand_choice(security_pics["monster defense"])
                sec_text = "{color=[c_lightgreen]}" + rand_choice([__("A vile"), __("An ugly"), __("A dirty"), __("A filthy"), __(" A scary"), __("A disgusting")]) + __(" monster crawled in from the shadows, but your guards drove it away!{/color} Fortunately, no one got hurt.")

                log.add_report("{color=[c_green]}Security alert! No one was hurt.{/color}")

            else:
                girl = rand_choice([g for g in MC.girls])

                sec_char = security_breach
                sec_text = "{color=[c_red]}" + rand_choice([__("A vile"), __("An ugly"), __("A dirty"), __("A filthy"), __("A scary"), __("A disgusting")]) + __(" night creature crawled in from ") + rand_choice([__("the shadows"), __("a window"), __("the sewers"), __("the roof")])

                if girl.test_shield():
                    sec_pic = "events/" + rand_choice(security_pics["girl shield"])
                    sec_sound = s_spell
                    sec_with = vpunch
                    sec_text += __(" and attacked ") + girl.fullname + __("{/color}, but {color=[c_lightgreen]}a {b}magic shield{/b} protected her from harm{/color} and the beast ran away.")

                    log.add_report("{color=[c_green]}Security alert! Shield protected " + girl.fullname + ".{/color}")

                elif girl.get_defense() >= game.chapter:
                    sec_pic = girl.get_pic("fight", naked_filter=True, soft=True, strict=True)
                    sec_sound = s_clash
                    sec_with = vpunch
                    if not sec_pic:
                        sec_pic = girl.get_pic("fight", strict=True)
                        if not sec_pic:
                            sec_pic = "events/" + rand_choice(security_pics["default girl fight"])

                    sec_text += __(" and attacked ") + girl.fullname + __("{/color}, but\n") + event_color["good"] % rand_choice([__("she kicked the critter's scaly ass and sent it packing."), __("she was ready to defend herself and butchered it."), __("her combat training paid off."), __("she had a weapon ready and scared it off."), __("she wounded it badly and it ran off.")])

                    log.add_report(__("{color=[c_green]}Security alert! ")+ girl.fullname + __(" defended herself.{/color}"))

                else:
                    if is_censored("monster"):
                        sec_pic = girl.get_pic("hurt", "rest", "profile")
                    else:
                        sec_pic = girl.get_pic("monster", "beast")
                    if not sec_pic:
                        sec_pic = "events/" + rand_choice(security_pics["monster rape"])
                    sec_sound = s_roar
                    sec_with = vpunch
                    sec_text += __(" and raped ") + girl.fullname + __(". {/color}\nYou manage to drive it away, but the girl is in shock.")

                    girl.change_fear(10)
                    girl.get_hurt(dice(3)+2)

                    if girl.hurt > 0:
                        girl.track_event("hurt", arg="an evil night monster.")
                        log.add_report(__("{color=[c_red]}Security alert! ") + girl.fullname + __(" was hurt.{/color}"))
                    else:
                        log.add_report(__("{color=[c_red]}Security alert! ") + girl.fullname + __(" was raped.{/color}"))

            brothel.reset_threat()

        ## ALERT LEVEL 2 ##

        elif ev_type == "assassin": # An assassin targets one of your girl, crippling her permanently of X skill points unless you let her rest a long time. No upside.
            girl = rand_choice(target_girls)

            _min, _max = alert_limits2[game.chapter]

            sec_text = __("A ") + rand_choice([__("shady"), __("sneaky"), __("skilled"), __("deadly"), __("mysterious"), __("rogue"), __("vicious")]) + __(" ninja made an attempt on ") + girl.fullname + __("'s life! ")

            renpy.play(s_sheath, "sound")
            renpy.pause(0.5)

            if guard_defense >= _max:
                sec_pic = "events/" + rand_choice(security_pics["assassin defense"])
                sec_sound = s_clash
                sec_text += event_color["good"] % __("Fortunately, your security was on hand, and forced the scoundrel to run away. ")

                log.add_report(__("{color=[c_green]}Security alert! No was one hurt.{/color}"))

            elif guard_defense + MC_defense >= _max:
                if MC.playerclass == "Warrior":
                    sec_pic = "events/" + rand_choice(security_pics["sword defense"])
                    sec_sound = s_clash
                elif MC.playerclass == "Wizard":
                    sec_pic = "events/" + rand_choice(security_pics["magic defense"])
                    sec_sound = s_spell
                elif MC.playerclass == "Trader":
                    sec_pic = "events/" + rand_choice(security_pics["dragon defense"])
                    sec_sound = s_roar

                sec_text = ("A " + rand_choice([__("shady"), __("sneaky"), __("skilled"), __("deadly"), __("mysterious"), __("rogue"), __("vicious")]) + __(" ninja made an attempt on ") + girl.fullname + __("'s life! ")
                           + event_color["good"] % rand_choice(MC.filter_say([__("wa: Fortunately, you were right next to her and parried the attack, unsheathing your sword right on time with cobra-like reflexes."), __("wi: Fortunately, you blocked the attack at the last second with a magical barrier."), __("tr: Fortunately, your pet dragon Drogon smelled the bastard and swooped right at him roaring before he had a chance to attack.")])) + __(" The assassin ran away."))

                log.add_report(__("{color=[c_green]}Security alert! No was one hurt.{/color}"))

            elif guard_defense + MC_defense >= _min:
                sec_pic = "events/" + rand_choice(security_pics["assassin"])
                sec_sound = s_wscream
                sec_with = vpunch

                lost_gold = (99 + dice(101)) * game.chapter

                sec_text += (event_color["a little good"] % __("Fortunately, your security was on hand. ") + __("A guard threw himself into harm's way and took the hit.\n")
                            + rand_choice([__("You gave the brave soul ") + str(lost_gold) + __(" gold for his trouble."), __("You gave the poor sod's family ") + str(lost_gold) + __(" gold and thanks for his loyal services."), __("You paid ") + str(lost_gold) + __(" gold for the courageous man medical expenses.")]))

                log.add_report(__("{color=[c_red]}Security alert! ") + str(lost_gold) + __(" gold lost.{/color}"))

            else:
                sec_char = security_breach

                if girl.test_shield():
                    sec_pic = "events/" + rand_choice(security_pics["girl shield"])
                    sec_sound = s_spell
                    sec_with = vpunch
                    sec_text += event_color["bad"] % sec_text + event_color["a little good"] % __("\nFortunately, she was protected by a {b}magic shield{/b} and escaped harm.")

                    log.add_report(__("{color=[c_green]}Security alert! Shield protected ") + girl.fullname + ".{/color}")

                elif girl.get_effect("special", "immune"):
                    sec_pic = "events/" + rand_choice(security_pics["girl shield"])
                    sec_sound = s_fizzle
                    sec_with = vpunch
                    sec_text += event_color["bad"] % sec_text + event_color["a little good"] % __("\nFortunately, she is {b}immune{/b} to physical damage and escaped harm.")

                    log.add_report(__("{color=[c_green]}Security alert! Immunity protected ") + girl.fullname + ".{/color}")

                elif girl.get_defense() >= district.rank*2:
                    sec_pic = girl.get_pic("fight", naked_filter=True, soft=True, strict=True)
                    if not sec_pic:
                        sec_pic = girl.get_pic("fight", strict=True)
                        if not sec_pic:
                            sec_pic = "events/" + rand_choice(security_pics["default girl fight"])

                    sec_sound = s_clash
                    sec_with = vpunch
                    sec_text = event_color["bad"] % sec_text + event_color["a little good"] % __("\nYour girl used her weapons to defend herself and escaped unscathed by a thread.")

                    log.add_report(__("{color=[c_green]}Security alert! ") + girl.fullname + __(" defended herself.{/color}"))

                else:
                    sec_pic = girl.get_pic("hurt", not_tags=["rest"], naked_filter=True, soft=True, strict=True)
                    if not sec_pic:
                        sec_pic = girl.get_pic("hurt", not_tags=["rest"], strict=True)
                        if not sec_pic:
                            sec_pic = Picture(path="events/" + rand_choice(security_pics["assassin"]))
                    sec_sound = s_woman_scream
                    sec_with = vpunch

                    sec_text = event_color["bad"] % sec_text + "\n" + rand_choice([__("She was only grazed by the assassin dagger, but she immediately lost consciousness."), __("She was hit in the arm, she's bleeding and looks feverish."), __("Her thigh got slashed and she is in pain."), __("She caught a dart in her chest, you worry it might be poisoned.")])
                    sec_text += __("\nYou bring the unconscious girl inside and take a look at the damage. It doesn't look life threatening, but some green substance is seeping from the wound. ")

                    ev_list.append(Event(pic = sec_pic, sound = sec_sound, with_st = sec_with, text = sec_text, changes = "", type ="Health/Security"))

                    sec_pic = girl.get_pic("rest", and_tags=["hurt"], naked_filter=True, soft=True)
                    if not sec_pic:
                        sec.pic = girl.profile
                    sec_text = ""
                    sec_sound = None
                    sec_with = fade

                    eff, msg = rand_choice([("Beauty", __("When she wakes up, her face is covered with ugly pimples. They should go away with the right ointment, but it will take a long time.\n") + event_color["bad"] % __("She is hurt for %s days, and her beauty has decreased by %s permanently.")),
                                        ("Body", __("You notice something disturbing. Her boobs and ass seem noticeably smaller. Such a cruel poison! Curse the bastards!\n") + event_color["bad"] % __("She is hurt for %s days, and her body has decreased by %s permanently.")),
                                        ("Charm", __("When she comes to her senses, she seems aloof and behaves strangely, altogether not like herself.\n") + event_color["bad"] % __("She is hurt for %s days, and her charm has decreased by %s permanently.")),
                                        ("Refinement", __("When she finally wakes up, she starts giggling and looks at you as if she didn't understand the situation she's in. It seems her mind wandered and she is acting all childish.\n") + event_color["bad"] % __("She is hurt for %s days, and her refinement has decreased by %s permanently.")),
                                        ("Libido", __("When she wakes up, she shivers and cowers from you. 'I'm s-s-so cold...', she says.\n") + event_color["bad"] % __("She is hurt for %s days, and her libido has decreased by %s permanently.")),
                                        ("Constitution", __("After struggling between life and death for a few hours, her fever eventually recesses, and it looks like she will survive. She is still very weak, however.\n") + event_color["bad"] % __("She is hurt for %s days, and her constitution has decreased by %s permanently.")),
                                        ("Obedience", __("When she comes through, she seems wild, almost feral. She nearly bites you when you come near. You hope the effect will recess with time.\n") + event_color["bad"] % __("She is hurt for %s days, and her obedience has decreased by %s permanently.")),
                                        ("Sensistivity", __("When she opens her eyes, she whispers faintly 'Master, I... I can't feel my limbs...'. She fights against paralysis all night, and without Sill's advanced alchimist skills, she would have become crippled. When she is finally able to get up, she still feels numb.") + event_color["bad"] % __("She is hurt for %s days, and her sensitivity has decreased by %s permanently.")),
                                        ("libido+", __("When she wakes up, she looks feverish, with a strange look in her eye. 'Master... Come over here...', she whispers. As you approach her bed, she grabs your dick and starts fondling it. 'Master's dick... Aaah...', she moans.\n") + event_color["bad"] % __("She is hurt for %s days") + __(", but ") + event_color["good"] % __("her libido has increased by %s permanently.") + __(" You wonder if you should thank the mysterious love ninja.")),
                                        ("personality", __("When she finally gets up, she looks like a different person. 'W-Who are you?'. It seems like she hit her head or something.\n") + event_color["average"] % __("She is hurt for %s days, and her {b}personality{/b} has changed. Her {b}love{/b} and {b}fear{/b} have been reset.")),
                                        ("naked", __("After a while, she opens her eyes and slowly comes to her senses. Suddenly, she shrieks, and throws the linen sheet to the side. 'No! It burns my skin!', she yells. It seems she has developped a phobia for cloth of any kind.\n") + event_color["bad"] % __("She is hurt for %s days") + __(", and ") + event_color["good"] % "%s." + __(" You guess it could really be worse.")),
                                        ])

                    girl.get_hurt(3+dice(6))

                    if eff in gstats_main:
                        chg = round_int(girl.change_stat(eff, -9 * (district.rank - 1) - dice(6)))
                        sec_changes.append((eff, chg))

                        try:
                            sec_text += msg % (str_int(girl.hurt), -chg)
                        except:
                            renpy.say("", msg)

                    elif eff == "libido+":
                        chg = round_int(girl.change_stat("libido", 4 * (district.rank - 1) + dice(6)))
                        sec_changes.append((eff, chg))

                        sec_text += msg % (str_int(girl.hurt), chg)

                    elif eff == "personality":
                        girl.love = 0
                        girl.fear = 0
                        girl.personality = rand_choice(gpersonalities.values())

                        sec_text += msg % str_int(girl.hurt)

                    elif eff == "naked":
                        if girl.get_effect("special", "naked"):
                            sec_text += msg % (str_int(girl.hurt), __("must remain naked at all times"))
                        else:
                            sec_text += msg % (str_int(girl.hurt), __("she has received the 'Naked' perk"))
                            girl.naked = True
                            girl.acquire_perk(naked_perk, forced=True)

                        if girl.preferences["naked"] < 200:
                            girl.preferences["naked"] = 200

                    log.add_report(__("{color=[c_red]}Security alert! ") + girl.fullname + __(" was hurt.{/color}"))

            brothel.reset_threat()

        elif ev_type == "brawl": # A brawl erupts in the tavern, causing some girls to get hurtin the fight and some damage (dirt) to the brothel. No upside.

            _min, _max = alert_limits2[game.chapter]

            sec_pic = "events/" + rand_choice(security_pics["brawl"])
            sec_sound = s_crowd_riot
            sec_with = vpunch

            sec_text = (__("A brawl erupted in the ") + __(rand_choice(brothel.get_common_rooms()).name) + __(" after ")
                        + __(rand_choice(["a customer spilled his boiling-hot grog on another man's crotch.",
                                       "two customers starting fighting over the same girl.",
                                       "a famous girls band from Borgo came to do a concert.",
                                       "a hated politician came in with his cronies.",
                                       "someone yelled 'free beer'.",
                                       "spiced-up junkies started thrashing the place.",
                                       "someone made one 'yo mamma' joke too-many.",
                                       "a female customer flashed her boobs.",
                                       "two rivals recognized each other.",
                                       "rival gangs met each other inside.",
                                       "someone attempted to sing a love song.",
                                       "a chick with a yellow jumper and a katana challenged the crowd to a fight.",
                                       "an old man came in with no pants and an attitude.",
                                       "Arios-worshippers were served salt against their religion.",
                                       "someone's beard caught fire.",
                                       "a drunk nobleman started throwing gold coins into the air.",
                                       "a rogue ship captain shot first.",
                                       "someone brought a herd of goats in and they started rampaging through the brothel.",
                                       "interdimensional aliens from another galaxy ripped the fabric of spacetime, as well as a girl's panties.",
                                      ])))

            if guard_defense >= _max:
                sec_text += event_color["good"] % __("\nFortunately, your guards were ready, and they threw the troublemakers out before they had a chance to do any serious damage.")

                log.add_report("{color=[c_green]}Security alert! Riot prevented.{/color}")

            elif guard_defense + MC_defense >= _max:
                if MC.playerclass == "Warrior":
                    sec_sound = s_punch
                elif MC.playerclass == "Wizard":
                    sec_sound = s_spell
                elif MC.playerclass == "Trader":
                    sec_sound = s_crowd_cheer

                sec_text += event_color["good"] % rand_choice(MC.filter_say([__("wa: \nFortunately, you were around and promptly beat some sense into the worst offenders. The others quickly went quiet."),
                                                                            __("wi: \nIn order to quell the riot, you cast a spell and turned the worst troublemakers into chicken. After that, the rest went back to their business. The charm should wear off in a few hours, and the cursed customers should be no worse off for their trouble, unless they ended up in the kitchen before then, of course."),
                                                                            __("tr: \nKnowing how to work the crowd, you offered everyone a free drink, and you and your guards beat up the few remaining troublemakers.")]))

                log.add_report("{color=[c_green]}Security alert! Riot prevented.{/color}")

            elif guard_defense + MC_defense >= _min:

                dirt = brothel.change_dirt(25 * game.chapter)
                rep = brothel.change_rep(-10 * game.chapter)

                sec_text += (__("\nChaos and confusion ensued as your guards joined the fray. Thankfully, after an hour of fighting and with great difficulty, they managed to protect your girls and quell the riot.\n")
                             + event_color["a little bad"] % (__("Unfortunately, the brothel is now littered with trash (+") + str_int(dirt) + __(" dirt) and has lost ") + str_int(rep) + __(" reputation.")))

                log.add_report("{color=[c_red]}Security alert! +" + str_int(dirt) + " dirt, -" + str(rep) + " reputation.{/color}")

            else:
                dirt = brothel.change_dirt(50 * game.chapter)
                rep = brothel.change_rep(-25 * game.chapter)

                hurt_girls = rand_choice(target_girls, nb = game.chapter//2 + dice(3))
                if isinstance(hurt_girls, Girl):
                    hurt_girls = [hurt_girls]

                for girl in hurt_girls:
                    girl.fear += 10

                sec_char = security_breach
                sec_text += (__(" The rioting customers overwhelmed your security guards and started looting your brothel's supplies and assaulting your girls.\n")
                             + event_color["bad"] % (and_text([g.fullname for g in hurt_girls]) + __(" were hurt.\n"))
                             + event_color["bad"] % (__("The brothel is just one big mess (+") + str_int(dirt) + __(" dirt) and has lost ") + str_int(rep) + __(" reputation.")))

                log.add_report("{color=[c_red]}Security alert! +" + str_int(dirt) + " dirt, -" + str_int(rep) + " reputation, " + and_text([g.fullname for g in hurt_girls]) + " were hurt.{/color}")

            brothel.reset_threat()


        ## ALERT LEVEL 3 --> NOT HANDLED HERE (see security label) ##

        ## QUIET ##

        elif ev_type == "quiet":
            game.track("security event", -1)
            sec_sound = s_chimes
            sec_pic = "backgrounds/castle night.webp"
            sec_text = __("It is a quiet, cloudless night out there. You feel as if your troubles are lifting.\nThe threat to [brothel.name] has decreased.")

            if brothel.alert_level == 1:
                brothel.threat -= 10
            elif brothel.alert_level == 2:
                brothel.threat -= 15
            elif brothel.alert_level == 2:
                brothel.threat -= 20

        ## ESCALATION ##

        elif ev_type == "ramp up":
            game.track("security event", -1)
            sec_sound = s_mystery
            sec_pic = "events/" + rand_choice(security_pics["alert"])
            sec_text = rand_choice([__("You hear disturbing whispers among the customers, "), __("There are rumors of ill-intent towards you and your brothel, "), __("Your guards have brought some rather disturbing reports, "), __("You can feel electricity in the night's air, "), __("Even as the customers pour in, the neighbourhood is eerily quiet, ")])

            sec_text += rand_choice(MC.filter_say([__("wa: and your sword arm is twitchy. "), __("wi: and you can read bad omens in the night skies. "), __("tr: and you can't help but feel like you are being crossed. "), __("ar: and no amount of praying to Arios seems to put your mind at ease. "), __("sh: and you wonder if Shalia might favor your enemies this time. "), __("ng: and you smell the stench of death in the night. ")]))
            sec_text += rand_choice([__("Something is afoot."), __("Someone is plotting against you."), __("Danger is coming."), __("Dark forces are at work, unseen...")])

            brothel.alert_level += 1

            log.add_report("{color=[c_red]}Security alert! Brothel alert level increased.{/color}")

        elif ev_type == "escalate":
            game.track("security event", -1)
            sec_char = security_breach

            sec_text += __("As you come out of the brothel to ") + rand_choice([__("breathe some fresh air"), __("check the perimeter"), __("take a leak"), __("watch the storm"), __("watch the night skies")]) + __(", you notice something odd.\n")

            if brothel.alert_level == 1:
                sec_pic = "events/" + rand_choice(security_pics["hood"])
                sec_sound = s_wolf
                sec_text += (__("A hooded silhouette is standing in the distance, watching your brothel, unmoving. ") + rand_choice([__("You hail it, but it "), __("You start approaching it, but it "), __("You try to get a better look at it, but it notices you and ")])
                             + __("disappears into the night."))
                brothel.threat += 5

            else:
                sec_pic = "events/" + rand_choice(security_pics["dark street"])
                sec_sound = s_wolf
                sec_text += (__("An inert body is lying on the pavement. You flip it around, and recognize one of your guards, ") + rand_choice([__("a dagger stuck inside his neck."), __("a shuriken protuding from his forehead."), __("a knife lodged between his shoulders."), __("his face grinning in a mortal rictus caused by an unknown poison"), __("his body charred by a nasty spell"),__ ("his face blue from suffocating with a grocery bag placed over his head"), __("his head split open with a candlestick, in the library.")])
                             + __("The poor henchman is stone-cold dead. You will have him replaced by tomorrow, of course, but you wonder what evil is afoot."))
                brothel.threat += 10

            sec_text += __("This is a bad sign of things to come. ") + event_color["bad"] % __("The {b}threat{/b} to [brothel.name] has escalated.")

            brothel.alert_level += 1

            log.add_report(__("{color=[c_red]}Security alert! Brothel alert level and threat increased.{/color}"))

        if lost_gold:
            MC.gold -= lost_gold
            sec_changes.append(("gold", -lost_gold))
        if bonus_gold:
            MC.gold += bonus_gold
            sec_changes.append(("gold", bonus_gold))

        text_chg = "\n\n" + get_change_text(sec_changes)

        if not sec_pic:
            renpy.say("", ev_type + " picture missing: " + str(sec_pic))
        elif not isinstance(sec_pic, Picture):
            sec_pic = Picture(path=sec_pic)

        ev_list.append(Event(pic = sec_pic, char = sec_char, sound = sec_sound, text = sec_text, with_st = sec_with, changes = text_chg, type ="Health/Security"))

        return ev_list


label kidnap_tip(girl): # Happens at the taverns location if a girl has been kidnapped

    $ price = (girl.rank ** 2) * 100
    $ rk = rank_name[girl.rank]
    $ tip = False

    # This is to avoid breaking saves

    python:
        try:
            k = girl.kidnapper
        except:
            girl.kidnapper = "rogue mercenaries"

    play music m_tavern fadein 3.0

    scene black with fade

    play sound s_crowd_laugh

    show bg tavern_man at truecenter with dissolve

    if not story_flags["kidnap tip " + girl.fullname]:

        man "Psst, Captain!"

        "A dodgy man is calling you from the shadows of the tavern where you stopped to get a quick drink."

        you "Sorry mate, I'm not recruiting... Not the likes of you, anyway."

        man "Arr, but ye'll be sorry if ye don't listen. Remember sweet little [girl.fullname]?"

        "You stop in your tracks and give him a chilling look."

        man "Hey, no need to give me {i}that{/i} look. I ain't with the fellas that took her."

        you "Good for you... Speak then, if you know something."

        man "I will, I will, but there's this terrible thirst in my throat... Plus this small coin I owe the red sea pirates, a trifle really, but they's pretty pissed about it..."

        you "*sigh* How much?"

        man "Well, we's talking about a rank [rk] chick here... Let's say [price] denars. A bargain for such information."
        menu:
            extend ""
            "All right (pay [price] gold)" if MC.gold >= price:
                "Frowning, you throw the shady man a bag of coins."

                play sound s_gold
                $ MC.gold -= price

                $ tip = True

            "Maybe later (come back later)":
                you "I don't have the coin right now. Stay put."

                man "Well... You know where to find me."

            "Forget it ([girl.fullname] will be lost forever)":
                $ MC.rand_say(["gd: It breaks my heart, but " + girl.name + " is lost for good now. I hope she'll be ok.", "ne: " + girl.fullname + "? That ship has sailed. I hope she's, uh, fine...", "ev: She was weak. Serves her right for being captured. Maybe she'll free herself, it's not my business any more."])

                man "Well, I wouldn't count on that... Have it your way, friend."

                $ MC.good -= 1

                if girl in game.kidnapped:
                    $ game.kidnapped.remove(girl)

        $ story_flags["kidnap tip " + girl.fullname] = True

    else:
        man "I have information about [girl.fullname] for [price] gold. Interested?"
        menu:
            extend ""

            "All right (pay [price] gold)" if MC.gold >= price:
                "Frowning, you throw the shady man a bag of coins."

                play sound s_gold
                $ MC.gold -= price

                $ tip = True

            "Maybe later (come back later)":
                you "I don't have the coin right now. Stay put."

                man "Well... You know where to find me."

            "Forget it ([girl.fullname] will be lost forever)":
                $ MC.rand_say(["gd: It breaks my heart, but " + girl.name + " is lost for good now. I hope she'll be ok.", "ne: " + girl.fullname + "? That ship has sailed. I hope she's, uh, fine...", "ev: She was weak. Serves her right for being captured. Maybe she'll free herself, it's not my business any more."])

                man "Well, I wouldn't count on that... Have it your way, friend."

                $ MC.good -= 1

                if girl in game.kidnapped:
                    $ game.kidnapped.remove(girl)

    if tip:
        man "Thank you, kind sir!"

        man "Right then. [girl.name] was captured by [girl.kidnapper]. I know where their lair is..."

        scene black with fade

        $ loc = rand_choice(game.get_available_locations())
        $ city_events.append(StoryEvent(label = "kidnap_rescue", call_args = [girl], location = loc.name))

        "The man showed you where to find [girl.fullname] near the {b}[loc.name]{/b}."

    return


label kidnap_rescue(girl):

    $ loc = selected_location.name.lower()

    "You reach the [loc]. This is where [girl.fullname] is being held."

    menu:
        "Do you want to try and rescue [girl.fullname] now?"

        "Yes":
            pass
        "No":
            $ city_events.append(StoryEvent(label = "kidnap_rescue", call_args = [girl], location = selected_location.name))
            $ MC.interactions += 1 # Refund AP
            return

    "Following your informer's directions, you start looking for the entrance of the lair where [girl.fullname] is being held."

    hide screen visit_location

    hide screen overlay

#    stop music fadeout 2.0

    scene black with dissolve

    $ renpy.show_screen("show_event", Picture(path="NPC/encounters/" + rand_choice(encounter_pics["secret_empty"])), _layer="master")

    with dissolve

    play sound s_aaha

    "Hearing a muffled woman voice, you head towards the source of the moans."

    play sound s_moans_quiet

    "Sneaking in the shadows, you arrive in front of a locked door. The muffled cries are coming from the other side of the door."

    "Approaching the door, you take a look through the keyhole."

    hide screen show_event
    with dissolve

    if girl.kidnapper == "marauding ogres":
        $ pic = girl.get_pic("sex", and_tags = ["big"])
        if not pic:
            $ pic = farm.get_pic("sex", and_tags = ["big"])

        $ renpy.show_screen("show_event", pic, _layer="master")

        "An ogre is fucking [girl.fullname] mercilessly, his huge cock messing up her insides."

    elif girl.kidnapper == "gooey monsters":
        $ pic = girl.get_pic("monster", and_tags = ["anal"])
        if not pic:
            $ pic = farm.get_pic("monster", and_tags = ["anal"])

        $ renpy.show_screen("show_event", pic, _layer="master")

        "A revolting demon is fucking [girl.fullname] in the ass, spurting gooey monster semen in her back hole."

    else:
        $ pic = girl.get_pic("machine", and_tags = ["group"])
        if not pic:
            $ pic = farm.get_pic("machine", and_tags = ["group"])

        $ renpy.show_screen("show_event", pic, x=config.screen_width, y=config.screen_height, _layer="master")

        "A guard is laughing and taunting [girl.fullname] as she is being teased and fucked by a strange apparatus."

    play sound s_moans

    "The enemy is distracted. If you can get past that door, you have a chance of ending this quickly."

#    "{b}Warning{b}\nIf you try and fail to rescue [girl.fullname], she will be lost forever."

    # Pick challenge
    $ tt = show_tt("top_right")
    $ chal = renpy.call_screen("challenge_menu", challenges=[("Force the door open", "force", selected_district.rank + 6), ("Unlock with magic", "detect", selected_district.rank+6)], cancel=("Come back later", False))
    hide screen tool

    $ renpy.block_rollback()

    if chal:
        # Run challenge
        call challenge(chal, selected_district.rank + 3) from _call_challenge_46 # result is stored in the _return variable
        $ r = _return

    if chal == "force":
        if r:
            "Taking a step back you charge and bash open the door with a well-placed kick."

            play sound s_crash
            with vpunch
            if girl.kidnapper == "marauding ogres":
                "Ogre" "Duh?"
                play sound s_sheath
                pause 0.2
                play sound2 s_roar

                with vpunch

                "Bursting throught the door, you impale the ogre on your sword, slashing through his innards. His eyes have a look of dumbfound surprise as he loudly falls backwards in the dust, dead."

            elif girl.kidnapper == "gooey monsters":
                "Monster" "Grrr..."
                play sound s_sheath
                pause 0.2
                play sound3 s_sheath
                pause 0.2
                play sound2 s_roar

                with vpunch

                "Slicing left and right, you hack at the monster until it lies defeated at your feet."

            else:
                man "What?!?"
                play sound s_sheath
                pause 0.2
                play sound2 s_wscream

                with vpunch

                "Striking from behind, you stab the thug in the neck, throwing his lifeless corpse to the side as you rush to free [girl.name] from her bonds."

        else:
            play sound s_punch
            with vpunch
            "You slam at the door but only manage to hurt your shoulder. The noise alerted your enemies, and you can hear muffled screams as [girl.fullname] is being dragged away."

    elif chal == "detect":
        if r:
            play sound s_spell
            pause 0.3
            play sound2 s_creak

            "Using a lockpicking spell, you silently open the door, placing yourself behind your opponent."

            you "Booh."

            if girl.kidnapper == "marauding ogres":
                "Ogre" "Uh?"
                play sound s_lightning
                pause 0.2
                play sound2 s_roar

                with flash

                "You strike the ogre with a bolt of lightning, briefly seeing the outline of his skeleton as he is fried dead. You girl escapes just in time, her hair standing on end from static electricity."

            elif girl.kidnapper == "gooey monsters":
                "Monster" "Rrrh!!!"
                play sound s_fire
                pause 0.2
                play sound2 s_roar

                with flash

                "You cast a fireball at what you guess is the creature's head, roasting it good. The monster falls lifeless in the dust."

            else:
                man "*whistle* Uh?"
                play sound s_lightning
                pause 0.2
                play sound2 s_wscream

                with flash

                "You casually strike down the guard with a lightning spell, turning him into an arty lamppost for a few seconds. He falls to ashes as you deliver [girl.name] from her bonds."

        else:
            play sound s_fizzle

            "Your spell fizzles, and you fiddle with the lock desperate to find another way to open the door."

            if girl.kidnapper == "marauding ogres":
                play sound s_roar
                "You have been discovered! A large ogre roars as he spots you. You run for your life as [girl.fullname] is being dragged away."

            elif girl.kidnapper == "gooey monsters":
                play sound s_roar
                "The monster has sensed your presence! You hear [girl.fullname]'s screams as she is being taken away."

            else:
                play sound s_sheath

                man "Intruder! Get him!" with vpunch

                "You have been found! You run away from the guard patrol. Gods know where they'll be taking [girl.fullname] now."

    else: # Leave for now
        $ city_events.append(StoryEvent(label = "kidnap_rescue", call_args = [girl], location = selected_location.name))

        "You will come back when you are ready. Sorry, [girl.name]..."

        hide screen show_event
        with dissolve

        return

    if r:
        $ unlock_achievement("rescued from kidnapping")
        play sound s_scream
        girl.char "Master [MC.name]! It's you!!!"

        "She sobs in your arms."

        girl.char "Oh, Master... Thank you, thank you..."

        $ MC.good += 1
        $ girl.love += 10

        "[girl.name] is overjoyed that her trial is over. She is very grateful to you."

        if girl.pop_virginity(origin="rape"):
            $ girl.fear += 10
            "[girl.name] has been raped repeatedly by her captors and is no longer a virgin."

        if girl in game.kidnapped:
            $ game.kidnapped.remove(girl)

        call acquire_girl(girl) from _call_acquire_girl_6

        if _return == "farm":
            "{b}[girl.fullname]{/b} has been sent to the farm."
        elif _return:
            "{b}[girl.name] is back to [brothel.name].{/b}"
        else:
            $ price = girl.get_price("sell")

            menu:
                "You do not have enough room to welcome [girl.fullname] back to the brothel."

                "Let her stay in an inn until tomorrow for 50 gold":
                    $ come_back = 1
                    $ MC.gold -= 50
                    play sound s_cash

                "Let her stay in an inn for a week for 250 gold":
                    $ come_back = 7
                    $ MC.gold -= 250
                    play sound s_cash

                "Sell her for [price] gold":
                    $ come_back = 0
                    $ MC.gold += price
                    $ MC.neutral += 1
                    play sound s_cash

                "Free her":
                    $ come_back = 0
                    $ MC.good += 1

                    you "I shall free you now. You have been through a lot."

                    girl.char "Really? Oh, Master!!!"

                    "{b}[girl.name] has been freed.{/b}"

            if come_back:
                $ calendar.set_alarm(calendar.time + come_back, Event(label = "girl_come_back", object = girl, order = 1))

    else:
        play sound s_woman_scream

        "{b}[girl.fullname] has been abducted to a different location.{/b}"

    return


label girl_come_back(girl):

    "[girl.fullname] returned to [brothel.name] as you ordered."

    call acquire_girl(girl) from _call_acquire_girl_7

    if _return == "farm":
        "{b}[girl.fullname]{/b} has been sent to the farm."
    elif _return:
        "There is now room for [girl.fullname] in your brothel.\n{b}[girl.name] is back to [brothel.name].{/b}"
    else:
        $ price = girl.get_price("sell")

        menu:
            "[girl.fullname] returns today. You do not have enough room to welcome her back to the brothel."

            "Let her stay in an inn until tomorrow for 50 gold":
                $ come_back = 1
                $ MC.gold -= 50
                play sound s_cash

            "Let her stay in an inn for a week for 250 gold":
                $ come_back = 7
                $ MC.gold -= 250
                play sound s_cash

            "Sell her for [price] gold":
                $ come_back = 0
                $ MC.gold += price
                $ MC.neutral += 1
                play sound s_cash

            "Free her":
                $ come_back = 0
                $ MC.good += 1

                you "I shall free you now. You have been through a lot."

                girl.char "Really? Oh, Master!!!"

                "{b}[girl.name] has been freed.{/b}"

        if come_back:
            $ calendar.set_alarm(calendar.time + come_back, Event(label = "girl_come_back", object = girl, order = 1))

    return
