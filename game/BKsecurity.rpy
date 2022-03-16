#### SECURITY EVENTS ####


label security(working_girls, ev_type=None): # Happens when the threat level overcomes the event threshhold. ev_type may be provided for debugging.

    $ renpy.notify("\n安全事件")
    $ game.track("security events", 1)

    #### HOW IT WORKS ####
    ## Threats builds up every night depending on total security, with a minimum of 1.
    ## The brothel starts at alert level 1. After threat reaches 10, 30 and 50, an event happens.
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

    ## ALERT LEVEL 3 ##

    # Because those events are more complex, they are not generated as regular night events

    if ev_type == "raid": # A raiding party blitzes the brothel, trying to kidnap one of your girls. 2-4 girls are targeted, you can only defend one yourself.

        python:
            attackers = rand_choice(("四处劫掠的巨魔", "粘糊糊的怪物", "流浪佣兵"))
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
            menu_list = [["选择一个女孩来保护", None]]

            for girl in target_girls:
                menu_list.append([girl.fullname.capitalize() + ", 等级 " + str(girl.level) + ", 防御 " + str_int(girl.get_defense()), girl])

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

        if attackers == "四处劫掠的巨魔":
            $ strength = 8
            $ magic = 5
            $ hit = "手中的那把巨斧"
            show ogre at totheleft as enemy with dissolve

        elif attackers == "粘糊糊的怪物":
            $ strength = 4
            $ magic = 7
            $ hit = "一条抖动的触手"
            show sewer_monster as enemy at truecenter with dissolve

        elif attackers == "流浪佣兵":
            $ strength = 6
            $ magic = 6
            $ hit = "手中的长剑"
            show masked_thug at totheleft as enemy with dissolve

        "You reach [girl.fullname] just in time to confront her attacker."

        if attackers == "四处劫掠的巨魔":
            show ogre at left as enemy with move

        elif attackers == "粘糊糊的怪物":
            show sewer_monster as enemy at centerleft with move

        elif attackers == "流浪佣兵":
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

                if attackers == "流浪佣兵":
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

            $ text1 = "当你在战斗的时候，其他袭击者在你的青楼里横冲直撞. "

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
            $ text1 = "当你昏倒的时候, [attackers]洗劫了你的青楼, {color=[c_red]}抢走了 [lost_gold] 金币。{/color} "

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
                text1 += and_text([g.fullname for g in defended_girls]) + "受伤了。\n"
                log.add_report("{color=[c_red]}安全警报！" + and_text([g.fullname for g in defended_girls]) + "受伤了。{/color}")
            elif len(hurt_girls) > 0:
                text1 += hurt_girls[0].fullname + "受伤了。\n"
                log.add_report("{color=[c_red]}安全警报！" + hurt_girls[0].fullname + "受伤了。{/color}")

            if kidnapped_girls:
                text1 += "{b}" + kidnapped_girls[0].fullname + "被绑架了！{/b}"
                log.add_report("{color=[c_red]}安全警报！{b}" + kidnapped_girls[0].fullname + "被绑架了！{/b}{/color}")

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

        $ brothel.alert_level = 1
        $ brothel.threat = 0


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
                enemy_g = "佣兵队长"
            elif enemy_general.has_trait("Caster"):
                enemy_g = "自由女巫"

            general_defeats = 0
            fatigue = -1

            allies_factor = brothel.get_effect("boost", "security")
            enemy_factor = 1.0


        $ log.add_report("{color=[c_red]}安全警报！" + str(enemies) +  "名佣兵在一名" + enemy_g + "的带领下包围了青楼。{/color}")

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
                $ MC.rand_say(["ev: 伙计们，准备好！！！！我们将在他们站立的地方屠杀他们！", "gd: 兄弟姐妹们! 我们没有选择挑起这场战争，但我们一定会结束它!", "ne: 伙计们，跟他们好好怼，努力战斗! 成为你所在街区第一个被公认的杀人王!"])
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

            $ renpy.say(security_breach, rand_choice(["有一枚榴弹你的队伍中爆炸，炸伤了 [damage] 个人。", "火雨向你的队伍倾盆而下，造成 [damage] 人受伤。", "炮弹炸死了 [damage] 个保安。", "一块巨大的石头砸到了你的队伍中，造成 [damage] 人受伤。"]))

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

            $ log.add_report("{color=[c_green]}战果：获得 " + str_int(loot) + " 金币。{/color}")

            if general_defeats > 0:
                $ it = get_rand_item("rare")

                $ item_name = "{b}" + article(it.name.lower()) + "{/b}"

                "Your men found something [enemy_general.fullname], the enemy general left behind. You have received [item_name]."
                $ MC.items.append(it)

                $ log.add_report("{color=[c_green]}战果：获得" + it.name + "。{/color}")

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

            $ security("{b}战役第四阶段{/b}\n剩下 [enemies] 个敌人在你的门前！你正遭受" + event_color["bad"] % "{b}战斗疲劳{/b}" + "的折磨，[fatigue]能暂时降低你的所有技能。你该怎么做？")

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

                            for i in xrange(protected):
                                if unprotected_girls:
                                    unprotected_girls.pop().add_shield()
                                else:
                                    rand_choice(fighting_girls).add_shield()

                "Encourage your girls to fight (use Charisma to boost your girls' fighting skill)":
                    $ renpy.block_rollback()
                    play sound s_roar
                    $ MC.rand_say(("振作起来！敌人就要来了，你知道该怎么办！", "ev: 好了，婊子们，准备好保卫你们悲惨的生活！最好不要让我失望！", "gd: 好了，各位，记住你们的训练，不要冒任何不必要的风险！", "ne: 宝贝们，就这样了。我就指望你了！"))
                    $ r = "rally"

                    call challenge(r, game.chapter, bonus=fatigue) from _call_challenge_42
                    $ result = _return

                    if result:
                        $ d = dice(6)
                        if d == 6:
                            $ narrator("你看着女孩们难以置信。她们正团结一致地面对敌人，互相支援，眼中闪烁着可怕的光芒。她们已经准备好了，将竭尽所能地与敌人作战。" + event_color["good"] % "所有女孩+3个人防御。")
                            $ girl_def_bonus += 3
                        elif d > 1:
                            $ narrator("你的演讲坚定了女孩们的决心。她们将更加努力地与敌人奋斗。" + event_color["good"] % "所有女孩+2个人防御。")
                            $ girl_def_bonus += 2
                        else:
                            $ narrator("你下达了最后的命令，帮其中一个女孩整了整皮背心，还提醒了一下另一个女孩的站位。她们是仆人，不是战士，但必须这样做。" + event_color["good"] % "所有女孩+1个人防御。")


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

                        for i in xrange(enemies):
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
                        $ security_breach("[enemies] 个敌人打败了你的女孩们。" + event_color["bad"] % and_text(hurt_girls) + "受伤了" + "。袭击者在离开前放了把火，导致青楼" + event_color["bad"] % "严重损坏 (+[dirt] 污垢)" + "。")
                    else:
                        $ security_breach("你的女孩们未作抵抗。袭击者在离开前放了把火, 导致青楼" + event_color["bad"] % "严重损坏 (+[dirt] 污垢)" + "。")

                    python:
                        burnt_furniture = rand_choice(brothel.furniture, dice(3)+1)

                        for furn in burnt_furniture:
                            if furn.rank > 0:
                                brothel.destroy_furniture(furn)

                    $ log.add_report("{color=[c_red]}安全警报！+" + str_int(dirt) + " 污垢，" + and_text(hurt_girls) + " 受伤。{/color}")

                else:
                    if hurt_girls:
                        $ dirt = int(brothel.change_dirt(200))
                        $ security_breach("[enemies] 个敌人攻击你的女孩们. " + event_color["bad"] % and_text(hurt_girls) + "在攻击者撤退之前受伤了" + "。战斗给你的青楼造成了一些损失 (" + event_color["bad"] % "+[dirt] 污垢" + ")")
                        $ log.add_report("{color=[c_red]}战果：+" + str_int(dirt) + " 污垢，" + and_text(hurt_girls) + " 受伤。{/color}")

                    else:
                        $ dirt = int(brothel.change_dirt(100))
                        $ security("你的女孩们竭尽全力保护自己，赶走了 [enemies] 个敌人. 他们试图在离开的时候放火烧你的妓院，造成了一点点伤害 (" + event_color["bad"] % "+[dirt] 污垢" + ")")
                        $ log.add_report("{color=[c_red]}战果：没有女孩受伤。+" + str_int(dirt) + " 污垢。{/color}")

                    $ MC.gold += loot
                    $ narrator("你和女孩们照料着伤员。在清理完战场后，你得到" + event_color["good"] % " [loot] 金币" + "作为战利品。")

                    $ log.add_report("{color=[c_green]}战果：" + str_int(loot) + " 金币。{/color}")

                    if general_defeats > 0:
                        $ it = get_rand_item("rare")

                        $ item_name = "{b}" + article(it.name.lower()) + "{/b}"

                        "Your girls found something the enemy general [enemy_general.fullname] left behind."

                        call receive_item(it) from _call_receive_item_15

                        $ log.add_report("{color=[c_green]}战果：获得" + it.name + "。{/color}")

            else:
                play sound s_gold
                $ MC.gold += loot
                $ narrator("你和女孩们照料着伤员。在清理完战场后，你得到" + event_color["good"] % " [loot] 金币" + "作为战利品。")

                $ log.add_report("{color=[c_green]}战果：敌方将领被俘！{/color}")

                play sound s_success

                "You have captured the enemy general, [enemy_general.fullname]!"

                $ unlock_achievement("general captured")
                $ log.add_report("{color=[c_green]}安全警报！" + str_int(loot) + " 金币。{/color}")

                play sound s_surprise

                enemy_general.char "W-What do you want to do with me? You bastard!"

                "She spits at you."

                $ price = enemy_general.get_price("buy")
                $ evil_price = price * 2

                show screen overlay
                $ tt = show_tt("top_right")
                show screen girl_stats(enemy_general, context="capture")
                with dissolve

                security "You have captured the enemy general, [enemy_general.fullname]!"

                menu:
                    "What do you want to do with her?"

                    "Keep her as a slave":
                        $ MC.girls.append(enemy_general)
                        you "I will now keep you as my pet. It's only fair that you work here to rebuild the damage you caused."

                        enemy_general.char "Me? A whore??? No!!!"

                        you "Sill, take her away and have her branded."

                        play sound s_woman_scream

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

        $ brothel.alert_level = 1
        $ brothel.threat = 0


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
                sec_text = ("{color=[c_green]}你的卫兵当场抓住了一个小偷！{/color} 他们整晚都在惩罚她。\n"
                             "他们的心情很好，愿意以平常一半的工资工作({b}" + str_int(bonus_gold) + " 金币{/b})。")

                log.add_report("{color=[c_green]}安全警报！没有损失金币。获得 " + str(bonus_gold) + " 金币。{/color}")

            elif guard_defense + MC_defense >= _max:
                sec_pic = "events/" + rand_choice(security_pics["thief defense"])
                sec_sound = s_surprise
                MC.change_prestige(district.rank)
                sec_text = ("{color=[c_green]}当你在巡逻时，你当场抓住了一个小偷！{/color} 她求你放了她, "
                                "所以你们达成了协议。\n你让她在地下室“玩”了一晚后离开。你赢得了{b}声望{/b}。")

                log.add_report("{color=[c_green]}安全警报！小偷造访，没有丢钱。赢得的声望。{/color}")

            elif guard_defense + MC_defense >= _min:
                sec_pic = "events/" + rand_choice(security_pics["thief"])
                sec_text = "{color=[c_lightgreen]}一名" + rand_choice(["大胆的", "鬼鬼祟祟的", "卑鄙的", "臭名昭著的", "娴熟的"]) + "小偷出现了，但你的保安把她赶走了！{/color}你没有损失金钱。"

                log.add_report("{color=[c_green]}安全警报！小偷造访，没有丢钱。{/color}")

            else:
                sec_char = security_breach
                sec_pic = "events/" + rand_choice(security_pics["thief"])
                sec_sound = s_evil_laugh
                lost_gold = round_int(MC.gold // 20)
                sec_text = ("{color=[c_red]}一名" + rand_choice(["大胆的", "鬼鬼祟祟的", "卑鄙的", "臭名昭著的", "娴熟的"]) + "小偷潜入了你的青楼并偷走了 {b}" + str_int(lost_gold) + "{/b} 金币！{/color}")

                log.add_report("{color=[c_red]}安全警报！小偷造访，损失 " + str(lost_gold) + " 金币。{/color}")

            brothel.threat = 0

        elif ev_type == "monster":

            _min, _max = alert_limits1[game.chapter]

            if guard_defense >= _max:
                sec_pic = "events/" + rand_choice(security_pics["monster defense"])
                sec_sound = s_clash
                for girl in working_girls:
                    girl.change_fear(-1)
                sec_text = "{color=[c_green]}你的一个守卫杀死了一只潜伏在黑暗角落里的怪物。{/color}\n你的女孩们放心了。"

                log.add_report("{color=[c_green]}安全警报！没有人受伤。恐惧降低。{/color}")

            elif guard_defense + MC_defense >= _max:
                sec_pic = "events/" + rand_choice(security_pics["sword defense"])
                sec_sound = s_clash
                for girl in working_girls:
                    girl.change_love(1)
                sec_text = ("{color=[c_green]}一个怪物从黑暗的角落里向你的女孩们扑来!{/color} 你快速的战斗反应救了你. "
                                "怪物毫无生气地躺在你的脚下。女孩们印象深刻。")

                log.add_report("{color=[c_green]}安全警报！没人受伤。爱情提高。{/color}")

            elif guard_defense + MC_defense >= _min:
                sec_pic = "events/" + rand_choice(security_pics["monster defense"])
                sec_text = "{color=[c_lightgreen]}" + rand_choice(["一个卑鄙的", "一个丑陋的", "一个肮脏的", "一个猥亵的", "一个惊慌的", "一个恶心的"]) + "怪物从阴影中爬了进来，但你的卫兵把它赶走了！{/color} 幸运的是，没有人受伤。"

                log.add_report("{color=[c_green]}安全警报！没人受伤。{/color}")

            else:
                girl = rand_choice([g for g in MC.girls])

                sec_char = security_breach
                sec_text = "{color=[c_red]}" + rand_choice(["一个卑鄙的", "一个丑陋的", "一个肮脏的", "一个猥亵的", "一个惊慌的", "一个恶心的"]) + "怪物从" + rand_choice(["阴影里", "一扇窗户", "下水道", "屋顶"]) + "爬了进来"

                if girl.test_shield():
                    sec_pic = "events/" + rand_choice(security_pics["girl shield"])
                    sec_sound = s_spell
                    sec_with = vpunch
                    sec_text += "并攻击了" + girl.fullname + "{/color}，但是{color=[c_lightgreen]}一个{b}魔法盾{/b}保护了她免受伤害{/color}，最后怪物跑开了。"

                    log.add_report("{color=[c_green]}安全警报！魔法盾保护了" + girl.fullname + "。{/color}")

                elif girl.get_defense() >= game.chapter:
                    sec_pic = girl.get_pic("fight", naked_filter=True, soft=True, strict=True)
                    sec_sound = s_clash
                    sec_with = vpunch
                    if not sec_pic:
                        sec_pic = girl.get_pic("fight", strict=True)
                        if not sec_pic:
                            sec_pic = "events/" + rand_choice(security_pics["default girl fight"])

                    sec_text += "并攻击了" + girl.fullname + "{/color}，只是\n" + event_color["good"] % rand_choice(["她一脚踢到那只浑身鳞片家伙的屁股，把它打发走了。", "她早就做好了自卫准备，最后她把它宰了。", "她的战斗训练得到了回报。", "她拿出早已准备好的武器，把它吓跑了。", "她把它伤得很重，它最终还是跑掉了。"])

                    log.add_report("{color=[c_green]}安全警报！"+ girl.fullname + " 保护了她自己。{/color}")

                else:
                    if is_censored("monster"):
                        sec_pic = girl.get_pic("hurt", "rest", "profile")
                    else:
                        sec_pic = girl.get_pic("monster", "beast")
                    if not sec_pic:
                        sec_pic = "events/" + rand_choice(security_pics["monster rape"])
                    sec_sound = s_roar
                    sec_with = vpunch
                    sec_text += "并且强奸了" + girl.fullname + ". {/color}\n你设法把它赶走了，但女孩们吓坏了。"

                    girl.change_fear(10)
                    girl.get_hurt(dice(3)+2)

                    if girl.hurt > 0:
                        girl.track_event("hurt", arg="邪恶的怪物.")
                        log.add_report("{color=[c_red]}安全警报！" + girl.fullname + "受伤了。{/color}")
                    else:
                        log.add_report("{color=[c_red]}安全警报！" + girl.fullname + "被强暴了。{/color}")

            brothel.threat = 0

        ## ALERT LEVEL 2 ##

        elif ev_type == "assassin": # An assassin targets one of your girl, crippling her permanently of X skill points unless you let her rest a long time. No upside.
            girl = rand_choice(target_girls)

            _min, _max = alert_limits2[game.chapter]

            sec_text = "一名" + rand_choice(["声名狼藉的", "鬼鬼祟祟的", "技艺娴熟的", "肆无忌惮的", "不可思议的", "暴戾的", "恶毒的"]) + "忍者试图危及" + girl.fullname + "的性命! "

            renpy.play(s_sheath, "sound")
            renpy.pause(0.5)

            if guard_defense >= _max:
                sec_pic = "events/" + rand_choice(security_pics["assassin defense"])
                sec_sound = s_clash
                sec_text += event_color["good"] % "幸运的是，你的保安在身边，迫使这个家伙逃跑了. "

                log.add_report("{color=[c_green]}安全警报！没有人受伤。{/color}")

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

                sec_text = ("一名" + rand_choice(["声名狼藉的", "鬼鬼祟祟的", "技艺娴熟的", "肆无忌惮的", "不可思议的", "暴戾的", "恶毒的"]) + "忍者试图危及" + girl.fullname + "的性命! "
                           + event_color["good"] % rand_choice(MC.filter_say(["wa: 幸运的是，你就在她身边，及时带她躲过了袭击，用眼镜蛇一样的反应及时拔出你的剑。", "wi: 幸运的是，你在最后一秒用魔法盾挡住了攻击。", "tr: 幸运的是，你的宠物龙卓耿嗅到了这个混蛋的味道，在他有机会攻击之前，它咆哮着冲向他。"])) + " 刺客逃走了。")

                log.add_report("{color=[c_green]}安全警报！没有人受伤。{/color}")

            elif guard_defense + MC_defense >= _min:
                sec_pic = "events/" + rand_choice(security_pics["assassin"])
                sec_sound = s_wscream
                sec_with = vpunch

                lost_gold = (99 + dice(101)) * game.chapter

                sec_text += (event_color["a little good"] % "幸运的是，你的保安就在身边. " + "一名保安不顾安危全力保护了她。\n"
                            + rand_choice(["你奖励了这名勇敢的保安 " + str(lost_gold) + " 金币。", "你为他的家庭支付一笔抚恤金 " + str(lost_gold) + " 金币来感谢他的忠诚服务。", "你为这名勇敢的保安支付了 " + str(lost_gold) + " 金币的治疗费用。"]))

                log.add_report("{color=[c_red]}安全警报！损失了 " + str(lost_gold) + " 金币。{/color}")

            else:
                sec_char = security_breach

                if girl.test_shield():
                    sec_pic = "events/" + rand_choice(security_pics["girl shield"])
                    sec_sound = s_spell
                    sec_with = vpunch
                    sec_text = event_color["bad"] % sec_text + event_color["a little good"] % "\n幸运的是，她受到了{b}魔法盾{/b}的保护而避免了伤害。"

                    log.add_report("{color=[c_green]}安全警报！魔法盾保护了" + girl.fullname + "。{/color}")

                elif girl.get_effect("special", "immune"):
                    sec_pic = "events/" + rand_choice(security_pics["girl shield"])
                    sec_sound = s_fizzle
                    sec_with = vpunch
                    sec_text = event_color["bad"] % sec_text + event_color["a little good"] % "\n幸运的是，她对物理伤害有{b}免疫{/b}，没有受到伤害。"

                    log.add_report("{color=[c_green]}安全警报！免疫保护了" + girl.fullname + "。{/color}")

                elif girl.get_defense() >= district.rank*2:
                    sec_pic = girl.get_pic("fight", naked_filter=True, soft=True, strict=True)
                    if not sec_pic:
                        sec_pic = girl.get_pic("fight", strict=True)
                        if not sec_pic:
                            sec_pic = "events/" + rand_choice(security_pics["default girl fight"])

                    sec_sound = s_clash
                    sec_with = vpunch
                    sec_text = event_color["bad"] % sec_text + event_color["a little good"] % "\n你的女孩用她的武器保护了自己，毫发无损地逃脱了。"

                    log.add_report("{color=[c_green]}安全警报！" + girl.fullname + "保护了她自己。{/color}")

                else:
                    sec_pic = girl.get_pic("hurt", not_tags=["rest"], naked_filter=True, soft=True, strict=True)
                    if not sec_pic:
                        sec_pic = girl.get_pic("hurt", not_tags=["rest"], strict=True)
                        if not sec_pic:
                            sec_pic = Picture(path="events/" + rand_choice(security_pics["assassin"]))
                    sec_sound = s_woman_scream
                    sec_with = vpunch

                    sec_text = event_color["bad"] % sec_text + "\n" + rand_choice(["她只被刺客的匕首擦伤，但很快就失去了知觉。", "她的胳膊被击中了，一直流血，看起来还有点发烧。", "她的大腿被割伤了，非常疼。", "她在胸前中一支飞镖，你担心她可能会中毒。"])
                    sec_text += "\n你把那个失去知觉的女孩带到里面，检查了一下受伤的地方. 看起来没有生命危险，只是伤口渗出了一些绿色物质. "

                    ev_list.append(Event(pic = sec_pic, sound = sec_sound, with_st = sec_with, text = sec_text, changes = "", type ="Health/Security"))

                    sec_pic = girl.get_pic("rest", and_tags=["hurt"], naked_filter=True, soft=True)
                    if not sec_pic:
                        sec.pic = girl.profile
                    sec_text = ""
                    sec_sound = None
                    sec_with = fade

                    eff, msg = rand_choice([("Beauty", "当她醒来时，她的脸上布满了难看的丘疹。他们应该用正确的药膏，但这要花很长时间才能恢复。\n" + event_color["bad"] % "她受伤需要休息%s天，她的美貌永久性地减少了%s。"),
                                        ("Body", "你注意到一些令人不安的事情。她的胸部和屁股看起来明显变小了。如此残忍的毒药!诅咒那些混蛋!\n" + event_color["bad"] % "她受伤需要休息%s天，她的身材永久性地减少了%s。"),
                                        ("Charm", "当她恢复知觉时，她似乎很冷淡，举止怪异，完全不像她自己。\n" + event_color["bad"] % "她受伤需要休息%s天，她的优雅永久性地减少了%s。"),
                                        ("Refinement", "当她最终醒来时，她开始咯咯地笑着看着你，好像她不明白自己的处境。她好像神志不清，表现得很幼稚。\n" + event_color["bad"] % "她受伤需要休息%s天，她的性欲永久性地减少了%s。"),
                                        ("Libido", "当她醒来的时候，她在你身边瑟瑟发抖，口中说着：“我……好……好冷……\n" + event_color["bad"] % "她受伤需要休息%s天，她的性欲永久性地减少了%s。"),
                                        ("Constitution", "在生死之间斗争了几个小时后，她的高烧最终消退，看来她会活下来。但是她仍然很虚弱。\n" + event_color["bad"] % "她受伤需要休息%s天，她的体格永久性地减少了%s。"),
                                        ("Obedience", "当她醒来的时候，她看起来很野性，几乎像一只野生动物。当你走近她时，差点被她咬到，你希望她的情况会随着时间的推移逐渐减弱。\n" + event_color["bad"] % "她受伤需要休息%s天，她的服从永久性地减少了%s。"),
                                        ("Sensistivity", "当她睁开眼睛时，她轻声说:“主人，我……我的感觉不到我的四肢……”。 她整晚都在与瘫痪作斗争，如果没有希尔的高级炼金术，她可能会变成残废。当她终于能站起来的时候，她仍然感觉麻木。" + event_color["bad"] % "她受伤需要休息%s天，她的敏感永久性地减少了%s。"),
                                        ("libido+", "当她醒来时，她看起来有点发烧，眼睛里有一种奇怪的神情。“主人……过来……”她低声说。当你靠近她的床时，她抓住你的肉棒，开始爱抚它。“主人的肉棒……Aaah……”她呻吟道。\n" + event_color["bad"] % "她受伤需要休息%s天" + "，神奇的是" + event_color["good"] % "她的性欲反而永久性地增长了%s。" + " 你在想你是不是应该感谢一下那位神秘的爱之忍者。"),
                                        ("personality", "当她终于起床时，她看起来完全变了个人。“你是谁？”。她好像撞到了头什么的。\n" + event_color["average"] % "她受伤需要休息%s天，她的{b}品味{/b}发生了改变。她的{b}喜好{/b}和{b}憎恶{/b}已经重置。"),
                                        ("naked", "过了一会儿，她睁开眼睛，慢慢地恢复了知觉。 突然，她尖叫了一声，把床单扔到了一边。 “不!它灼伤了我的皮肤!”,她喊道。看来她对任何布料都有恐惧症。\n" + event_color["bad"] % "她受伤需要休息%s天" + "，而且" + event_color["good"] % "%s。" + "你估计情况有可能会更糟。"),
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
                            sec_text += msg % (str_int(girl.hurt), "必须一直赤身裸体")
                        else:
                            sec_text += msg % (str_int(girl.hurt), "她获得了“裸体主义”特质")
                            girl.naked = True
                            girl.acquire_perk(naked_perk, forced=True)

                        if girl.preferences["naked"] < 200:
                            girl.preferences["naked"] = 200

                    log.add_report("{color=[c_red]}安全警报！" + girl.fullname + "受伤了。{/color}")

            brothel.alert_level = 1
            brothel.threat = 0

        elif ev_type == "brawl": # A brawl erupts in the tavern, causing some girls to get hurtin the fight and some damage (dirt) to the brothel. No upside.

            _min, _max = alert_limits2[game.chapter]

            sec_pic = "events/" + rand_choice(security_pics["brawl"])
            sec_sound = s_crowd_riot
            sec_with = vpunch

            sec_text = ("" + rand_choice(brothel.get_common_rooms()).name + "里爆发了一场争吵，原因是 "
                        + rand_choice(["一名客人把滚烫的烈酒洒在另一个人的裆部。",
                                       "两个顾客开始争夺同一个女孩。",
                                       "一个来自博尔格的著名女子乐队组合来开音乐会。",
                                       "一名遭人憎恨的政客带着他的亲信进来了。",
                                       "有人大喊着“免费啤酒！”。",
                                       "吸毒成瘾的人开始在这个地方乱窜。",
                                       "有人开了太多的“yo mamma”玩笑。",
                                       "一位女顾客露出了胸部。",
                                       "两名商业竞争中相互认出了对方。",
                                       "敌对帮派在里面相遇。",
                                       "有人想唱一首情歌。",
                                       "一名身穿黄色套头衫手持武士刀的家伙向人群发起挑战。",
                                       "一名没穿裤子，面容肃穆的老人走了进来。",
                                       "阿里奥斯崇拜者在讨论盐是不是有违宗教信仰。",
                                       "有人的胡子着火了。",
                                       "一名醉醺醺的贵族开始往空中扔金币。",
                                       "一名流氓船长对空开了一枪。",
                                       "有人带了一群山羊进来，它们开始在青楼里横冲直撞。",
                                       "来自另一个星系的星际异形撕裂了时空结构，也撕裂了一个女孩的内裤。",
                                      ]))

            if guard_defense >= _max:
                sec_text += event_color["good"] % "\n幸运的是，你的保安们已经做好了万全准备，他们在捣蛋鬼有机会造成严重损失之前就把他们赶了出去。"

                log.add_report("{color=[c_green]}安全警报！暴乱被制止。{/color}")

            elif guard_defense + MC_defense >= _max:
                if MC.playerclass == "Warrior":
                    sec_sound = s_punch
                elif MC.playerclass == "Wizard":
                    sec_sound = s_spell
                elif MC.playerclass == "Trader":
                    sec_sound = s_crowd_cheer

                sec_text += event_color["good"] % rand_choice(MC.filter_say(["wa: \n幸运的是，你就在附近，很快就用拳头让暴乱者清醒了。其他人很快就安静下来。",
                                                                            "wi: \n为了平息暴乱，你施展了魔法，把最出头的捣乱者变成了胆小鬼。在那之后，其余的人又回到了他们自己的位置。魅力在几个小时内就会消失，而被施法的客人也不会因为他们的麻烦而更糟，当然，除非他们在那之前去过厨房。",
                                                                            "tr: \n你知道如何摆平这种事，先是给每个人提供了一杯免费饮料，接着你和你的保安痛打了剩下的几个捣乱分子。"]))

                log.add_report("{color=[c_green]}安全警报！暴乱被制止。{/color}")

            elif guard_defense + MC_defense >= _min:

                dirt = brothel.change_dirt(25 * game.chapter)
                rep = brothel.change_rep(-10 * game.chapter)

                sec_text += ("\n当你的保安们开始加入战斗时，混乱随之而来。谢天谢地，在经过一个小时艰苦乱战之后，他们设法保护了你的女孩们，平息了暴乱。\n"
                             + event_color["a little bad"] % ("很遗憾, 青楼现在到处都是垃圾 (+" + str_int(dirt) + " 污垢) 并且还损失了 " + str_int(rep) + " 名声。"))

                log.add_report("{color=[c_red]}安全警报！+" + str_int(dirt) + " 污垢，-" + str(rep) + " 青楼名声。{/color}")

            else:
                dirt = brothel.change_dirt(50 * game.chapter)
                rep = brothel.change_rep(-25 * game.chapter)

                hurt_girls = rand_choice(target_girls, nb = game.chapter//2 + dice(3))
                if isinstance(hurt_girls, Girl):
                    hurt_girls = [hurt_girls]

                for girl in hurt_girls:
                    girl.fear += 10

                sec_char = security_breach
                sec_text += (" 暴动的客人压制了你的保安，开始抢劫你青楼，攻击你的女孩。\n"
                             + event_color["bad"] % (and_text([g.fullname for g in hurt_girls]) + "受伤了。\n")
                             + event_color["bad"] % ("青楼乱得像一团乱麻 (+" + str_int(dirt) + " 污垢) 并且还损失了 " + str_int(rep) + " 名声。"))

                log.add_report("{color=[c_red]}安全警报！+" + str_int(dirt) + " 污垢，-" + str_int(rep) + " 名声，" + and_text([g.fullname for g in hurt_girls]) + "受伤了。{/color}")

            brothel.alert_level = 1
            brothel.threat = 0


        ## ALERT LEVEL 3 --> NOT HANDLED HERE (see security label) ##

        ## QUIET ##

        elif ev_type == "quiet":
            game.track("security event", -1)
            sec_sound = s_chimes
            sec_pic = "backgrounds/castle night.webp"
            sec_text = "外面是一个宁静无云的夜晚。你觉得你的麻烦好像在减少。\n针对[brothel.name]的威胁降低了。"

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
            sec_text = rand_choice(["你听到顾客间令人不安的窃窃私语，", "有谣言说你和你的青楼居心不良，", "你的保安带来了一些令人不安的消息，", "你能感觉到夜晚空气中的紧张情绪，", "即使顾客蜂拥而至，附近也异常安静，"])

            sec_text += rand_choice(MC.filter_say(["wa: 你平时握剑的手在轻轻抽搐。", "wi: 你可以在夜空中看到不好的预兆。", "tr: 你情不自禁地觉得自己被欺骗了。", "ar: 对阿里奥斯再多的祈祷也不能让你安心。", "sh: 你想知道莎莉娅这次会不会偏袒你的敌人。", "ng: 你闻到了死亡的恶臭。"]))
            sec_text += rand_choice(["某些事情正在酝酿之中。", "有人在密谋对你不利。", "危险来了。", "看不见黑暗力量在起作用……"])

            brothel.alert_level += 1

            log.add_report("{color=[c_red]}安全警报！青楼的威胁级别提高。{/color}")

        elif ev_type == "escalate":
            game.track("security event", -1)
            sec_char = security_breach

            sec_text += "当你从青楼出来" + rand_choice(["呼吸新鲜空气", "检查周边", "嘘嘘", "看到风暴正袭来", "仰望夜空"]) + "的时候，你注意到一些奇怪的东西。\n"

            if brothel.alert_level == 1:
                sec_pic = "events/" + rand_choice(security_pics["hood"])
                sec_sound = s_wolf
                sec_text += ("一个蒙面的身影站在远处，看着你的青楼，一动不动。" + rand_choice(["你喊了它一声，它就转身", "你开始接近它，但是它马上就", "你试图看得更清楚，但它注意到你并转身"])
                             + "消失在黑夜里。")
                brothel.threat += 5

            else:
                sec_pic = "events/" + rand_choice(security_pics["dark street"])
                sec_sound = s_wolf
                sec_text += ("一具冰冷的尸体倒在墙边边. 你把它翻过来，认出他是你的一位保安，" + rand_choice(["一把匕首插在他的脖子上。", "一个手里剑从他的前额冒出头来。", "一把刀夹在他的肩膀之间。", "他的脸在一个未知的毒药引起的致命效果之下咧着嘴笑。", "他的身体被恶毒的咒语烧焦了", "他头上套着一个购物袋，脸因窒息而发青。", "他的头被图书馆里的烛台给开瓢了。"])
                             + "那个可怜的保安冻死了。当然，明天你就会找人替换他，但你不知道邪恶到底酝酿着什么。")
                brothel.threat += 10

            sec_text += "这是个不祥之兆。" + event_color["bad"] % "[brothel.name]的{b}威胁{/b}等级已经提高了。"

            brothel.alert_level += 1

            log.add_report("{color=[c_red]}安全警报！青楼的威胁级别提高。{/color}")

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
            girl.kidnapper = "流浪佣兵"

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
                $ MC.rand_say(["gd: 我很伤心，我永远失去了" + girl.name + "，我真希望她没事。", "ne: " + girl.fullname + "？已经过去了，我希望她，额，没事……", "ev: 她太弱了，活该被抓。也许她会解脱自己的，这已经不是我的事了。"])

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
                $ MC.rand_say(["gd: 我很伤心，我永远失去了" + girl.name + "，我真希望她没事。", "ne: " + girl.fullname + "？已经过去了，我希望她，额，没事……", "ev: 她太弱了，活该被抓。也许她会解脱自己的，这已经不是我的事了。"])

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
    $ chal = renpy.call_screen("challenge_menu", challenges=[("用力推开门", "force", selected_district.rank + 6), ("用魔法开锁", "detect", selected_district.rank+6)], cancel=("稍后再来", False))
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

        if len(MC.girls) < brothel.bedrooms:
            $ MC.girls.append(girl)
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

                "Send her to the farm" if farm.active and farm.has_room():
                    $ come_back = 0

                    $ farm.send_girl(girl, FarmProgram(girl))

                    "{b}[girl.fullname]{/b} has been sent to the farm."

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

    if len(MC.girls) < brothel.bedrooms:
        $ MC.girls.append(girl)
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

            "Send her to the farm" if farm.active and farm.has_room():
                $ come_back = 0

                $ farm.send_girl(girl, FarmProgram(girl))

                "{b}[girl.fullname]{/b} has been sent to the farm."

            "Free her":
                $ come_back = 0
                $ MC.good += 1

                you "I shall free you now. You have been through a lot."

                girl.char "Really? Oh, Master!!!"

                "{b}[girl.name] has been freed.{/b}"

        if come_back:
            $ calendar.set_alarm(calendar.time + come_back, Event(label = "girl_come_back", object = girl, order = 1))

    return
