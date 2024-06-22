#### Farm classes ####

init -2 python:
    class Installation(object):

        def __init__(self, name, pic, tags, minion_type, skill, rank=0, minions=None):
            self.name = name
            self.pic = Picture(pic, "brothels/farm/" + pic)
            self.tags = tags
            self.minion_type = minion_type
            self.skill = skill
            self.rank = rank
            if minions:
                self.minions = minions
            else:
                self.minions = []
            self.girls = []

        def get_tooltip(self):

            ttip = "农场 %s 可以容纳 %i 单位 (目前: %i).\n" % (farm_related_dict[self.name], self.rank, len(self.minions))

            if self.can_upgrade():
                if self.rank > 0:
                    ttip += "点击升级设施, 这将花费" + str(self.get_price()) + " 金币"
                else:
                    ttip += "点击建造设施, 这将花费" + str(self.get_price()) + " 金币"

            elif self.rank < 5:
                ttip += "在你得到更高级的营业执照前, 该设施无法升级"

            else:
                "设施已达到最大等级"

            return ttip

        def has_room(self, type="minion", nb=1):
            if nb <= self.rank - len(self.minions):
                return True
            return False

        def return_assigned_girls(self): # Ignores auto assignments
            return [g for g in farm.girls if farm.programs[g].installation == self]

        def count_busy_minions(self):
            mn_nb = 0
            for girl in self.return_assigned_girls():
                prog = farm.programs[girl]
                if prog.target == "group":
                    mn_nb += 2
                else:
                    mn_nb += 1

            return mn_nb

        def count_free_minions(self):
            return sum(1 for mn in self.minions if mn.free and not mn.hurt)

        def get_free_minions(self, nb=1): # Will only return a list if the required number of minions is available

            min_list = []

            if self.count_free_minions() >= nb:
                min_list = rand_choice([mn for mn in self.minions if mn.free and not mn.hurt], nb)

                for mn in min_list:
                    mn.free = False

            return min_list

        def get_healthy_minions(self):
           return [min for min in self.minions if not min.hurt]

        def get_hurt_minions(self):
            return [mn for mn in self.minions if mn.hurt]

        def add_minion(self, mn):
            if mn.type != self.minion_type:
                return False, "你无法添加一个 " + farm_related_dict[mn.type] + " 到 " + farm_related_dict[self.name] + " (错误的仆从类型)."
            elif self.has_room():
                self.minions.append(mn)
                renpy.play(s_moo, "sound")
#                renpy.say ("", "Adding to " + self.name)
                return True, mn.name + ", 一个等级 " + str(mn.level) + " 的" + farm_related_dict[mn.type] + ", 已经加入到 " + farm_related_dict[self.name] + "."
            elif self.can_upgrade():
                if self.rank > 0:
                    renpy.say("", "农场的 " + farm_related_dict[self.name] + " 现在满员了.")
                else:
                    renpy.say("", "你必须先建造一个 " + farm_related_dict[self.name] + " 才行.")
                if renpy.call_screen("yes_no", "你想升级 " + farm_related_dict[self.name] + " 到 " + str(self.rank+1) + " 阶吗？这将花费 " + str(self.get_price()) + " 金币"):
                    if MC.gold < self.get_price() + mn.get_price("buy"):
                        return False, "你没有足够多的钱去升级 " + farm_related_dict[self.name] + " 并购买仆从"
                    MC.gold -= self.get_price()
                    self.rank += 1
                    self.minions.append(mn)
                    return True, "农场的 " + farm_related_dict[self.name] + " 已经扩大了，一个等级 " + str(mn.level) + " 的 " + farm_related_dict[self.minion_type] + mn.name + " 加入了."
                else:
                    return False, ""
            else:
                return False, "这不可能，农场的 " + farm_related_dict[self.name] + " 已满并且不能再升级了。"

        def assign_minions(self): # Returns excess girls to be assigned elsewhere automatically

            for mn in self.minions:
                mn.free = True

            rejected = []

            # 'Group' girls get assigned first
            for girl in [g for g in self.girls if farm.programs[g].act == "group"]:
                min_list = self.get_free_minions(2)
                if min_list:
                    farm.programs[girl].minions = min_list
                else:
                    rejected.append(girl)

            # 'Single' girls are assigned next
            for girl in [g for g in self.girls if farm.programs[g].act != "group"]:
                min_list = self.get_free_minions(1)

                if min_list:
                    farm.programs[girl].minions = min_list
                else:
                    rejected.append(girl)

            # Adds a third minion to groups if possible

            for girl in [g for g in self.girls if farm.programs[g].act == "group"]:
                if girl not in rejected:
                    min_list = self.get_free_minions(1)
                    if min_list:
                        farm.programs[girl].minions += min_list

            for girl in rejected:
                self.girls.remove(girl)

            return rejected

        def get_price(self):
            if self.rank >= 5:
                return 0
            return installation_price[self.rank]

        def get_pic(self):
            return self.pic

        def upgrade(self):
            if MC.gold < self.get_price():
                return False, "你没有足够的钱去扩大" + farm_related_dict[self.name] + "！别再浪费我的时间！"
            elif self.rank >= 5:
                return False, "这个" + farm_related_dict[self.name] + "无法再扩大了"
            elif self.rank >= district.rank:
                return False, "继续扩大" + farm_related_dict[self.name] + "会引来许多不必要的麻烦，什么时候等你有更高级的营业执照，再来找我谈扩张的事吧"
            elif renpy.call_screen("yes_no", "你真的想要升级" + farm_related_dict[self.name] + "吗？这将花费" + str(self.get_price()) + "金币"):
                MC.gold -= self.get_price()
                self.rank += 1
                renpy.play(s_gold, "sound")
                unlock_pic(self.pic.path)
                return True, "这个" + farm_related_dict[self.name] + "已经扩张完毕，现在它可以同时容纳" + str(self.rank) + " 个 " + farm_related_dict[self.minion_type] + "."
            else:
                return False, ""

        def can_upgrade(self):
            if self.rank >= district.rank:
                return False
            else:
                return True

        def get_intro(self): # Returns the introduction event if there are girls in the installation, an error instead

            if self.girls:
                if len(self.minions) <= 1:
                    text1 = farm_description[self.minion_type + " intro"] % and_text([g.name for g in self.girls])
                else:
                    text1 = farm_description[self.minion_type + " intro plural"] % (and_text([g.name for g in self.girls]), str(len(self.minions)))

                log.add_report(text1)

                return Event(self.get_pic(), char = narrator, text = text1, changes = "", type = "UI")
            else:
                raise AssertionError("这个设施里没有女孩.")

        def refresh(self):
            self.girls = []
            for mn in self.minions:
                mn.free = True

    class Minion(object):

        def __init__(self, type, level = 0, name = ""):
            self.type = type
            self.level = level
            if name:
                self.name = name
            else:
                self.name = generate_name(type)
            self.target = "Farm minion"
            self.filter = "misc"
            self.equipped = False
            self.xp = minion_xp_to_level[level]
            self.description = minion_description[type]
            self.pic = self.get_random_pic()
            self.free = True
            self.hurt = False
            self.hp = 4

        def get_acts(self, owner, counterpart): # Returns a list all available acts for this minion based on current parties
            possible_acts = []

            if owner.type == "NPC":
                possible_acts.append("buy")

            return possible_acts

        def get_key(self):
            return (self.level, self.name)

        def get_pic(self, x, y):
            return self.pic.get(x, y)

        def get_random_pic(self):

            d = str(dice(3))

            pic = Picture(self.type + d + ".webp", "NPC/minions/" + self.type + d + ".webp")

            return pic

        def get_price(self, operation="buy"):
            return round_int(minion_price[self.level] * MC.get_modifier(operation))

        def ready_to_level_up(self):
            if self.level < 5 and self.xp >= minion_xp_to_level[self.level+1]:
                return True
            return False

        def level_up(self, forced=False):
            if self.ready_to_level_up() or forced:
                self.level += 1
                return True
            else:
                return False

        def get_tooltip(self):

            des = "等级 %i %s" % (self.level, farm_related_dict[self.type])

            if self.level >= 5:
                des += " (满级)"
            else:
                des += " (XP: %i/%i)" % (self.xp, minion_xp_to_level[self.level+1])


            if self.hurt:
                if self.type == "machine":
                    des += event_color["bad"] % ("\n" + farm_related_dict[self.name] + " 已经损坏，我得花 " + str(self.hurt) + " 天来修复它 ")
                else:
                    des += event_color["bad"] % ("\n" + farm_related_dict[self.name] + " 严重受伤，它得休息 " + str(self.hurt) + " 天来养伤 ")

            return des

        def heal(self):
            self.hurt = False
            self.hp = 4

        def use_item(self, it):
            if it.target == "minion":
                for eff in it.effects:
                    if eff.type == "gain":
                        if eff.target == self.type + " xp":
                            self.xp += eff.value
                            return eff.value
            return 0


    class FarmProgram(object):
        def __init__(self, girl, fixed_duration=False): # name, type, mode, target, auto=False, duration=None, minion_nb=1, minion_type=["stallion", "beast", "monster", "machine"], pop_v=False):

            self.girl = girl
            self.name = ""
            self.target = "no training" # Reminder: target is the training type, use act to check which sex act is actually assigned
            self.act = None
            self.mode = "tough"
            self.holding = farm.default_holding
            self.resting = "intensive"
            self.tired = False
            self.inst_full = False
            self.refused = False
            self.duration = -1
            self.condition = "none"
#            self.minion_types = minion_types
            self.minions = []
            self.auto_inst = True
            self.installation_name = "auto"
            self.installation = None # An object (important)
            self.fixed_duration = fixed_duration
            if fixed_duration:
                self.duration = fixed_duration

            self.avoid_weakness = False
            self.notification = False # Whether or not the player has been shown the girl's reaction to this training program

        def update(self):
            if self.target != "no training":
                self.name = "{color=[c_orange]}" + farm_related_dict[self.target.capitalize()] + "训练"  + "{/color}"
            elif self.holding == "rest":
                self.name = "{color=[c_lightgreen]}" + farm_holding_dict[self.holding] + "{/color}"
            else:
                self.name = "{color=[c_cream]}" + farm_holding_dict[self.holding] + "{/color}"

            if self.installation:
                self.installation_name = self.installation.name
            else:
                self.installation_name = "auto"

            self.notification = False

        def refresh(self):
            self.act = None
            self.minions = []
            self.tired = False
            self.inst_full = False
            self.refused = False

            if self.auto_inst:
                self.installation = None

        def resolve(self, type):

            girl = self.girl
            descript = "" # "{size=" + str(res_font(14)) + "}"
            changes = defaultdict(int)
            pic = None
            pic_bg = None
            change_log = NightChangeLog()
            farm_events = []
            ev_sound = None

#            girl.add_log("farm_days")


            if not isinstance(girl, Girl):
                return farm_events

            #### RESOLVE TRAINING ####

            if type == "training": # For training of sexual preferences

                pic_bg = inst.get_pic() #!

                ## Sanity checks

                if not self.act:
                    raise AssertionError("No act found")
                if not self.installation:
                    raise AssertionError("No installation found")

                ## Init variables

                training_stop = False
                run_away = False
                training_modifier = 0 # Increases or lowers stat change depending on situation
                min_type = self.minions[0].type

                ## REACTION - Checks girl reaction to training - Reaction is how negatively or positively she views the act. It is not the same as rebellion. ##

                reaction = girl.will_do_farm_act(self.act) # Will return 'accepted', 'resisted' or 'refused'

                if reaction == "accepted":
                    if self.mode == "gentle": # Using gentle mode is not evil
                        MC.evil -= 0.3
                    log.add_report(girl.fullname + " 在农场接受训练.")

                elif reaction == "resisted":
                    training_modifier -= 1
                    changes["fear"] += 1

                    MC.good -= 0.3 # Pushing something she doesn't like is not nice

                    if not girl.is_(["very sub", "lewd"]):
                        changes["mood"] -= 2

                elif reaction == "refused":
                    training_modifier -= 2
                    changes["fear"] += 2

                    if self.mode == "hardcore":
                        MC.evil += 0.3 # Using hardcore mode is *evil*

                    if girl.personality.name not in ("masochist"):
                        changes["mood"] -= 3

                else: # Sanity check
                    raise AssertionError("Reaction " + reaction + " not recognized.")

                # Additional mode impact on Fear

                if self.mode == "tough":
                    changes["fear"] += dice(3) - 1
                elif self.mode == "hardcore":
                    changes["fear"] += dice(3)

                ## REBELLION attempts

                if girl.will_rebel_in_farm(self.mode, reaction):
                    girl.add_log("farm_resisted_training")
                    training_stop = True

                    changes["obedience"] -= 1

                    d = dice(6)

                    if girl.is_("very dom"):
                        mod = +2
                    elif girl.is_("dom"):
                        mod = +1
                    elif girl.is_("very sub"):
                        mod = -1
                    else:
                        mod = 0

                    if d + mod >= 6: # Fight!

                        fight_res = fight(girl, NPC_gizel, advantage=None)

                        if fight_res == "tie":
                            pic = Picture(path="NPC/gizel/whip1.webp")
                            # pic_bg = inst.get_pic()
                            descript += event_color["a little bad"] % (girl.name + " " + reaction + " 攻击了吉泽！她不得不使用魔法让她老实点.\n")
                            ev_sound = s_fire

                            if dice(6) >= 4:
                                girl.get_hurt(dice(5))
                                changes["obedience"] -= dice(3)
                                changes["fear"] += girl.hurt
                                descript += event_color["bad"] % (girl.name + " 受伤了，她必须接受治疗，这将花费 " + str(round_int(girl.hurt)) + " 天时间.")
                                girl.add_log("farm_hurt")

                                calendar.set_alarm(calendar.time+1, StoryEvent(label="farm_resisted", type="morning", call_args=[girl, "rebel girl hurt"]))
                            else:
                                mn = rand_choice(self.minions)
                                mn.hurt = True
                                if mn.type == "machine":
                                    descript += event_color["bad"] % (mn.name + " (等级 " + str(mn.level) + " 的" + farm_related_dict[mn.type] + ") 在搏斗中损坏了. 在你修好它之前它只能吃灰了.")
                                else:
                                    descript += event_color["bad"] % (mn.name + " (等级 " + str(mn.level) + " 的" + farm_related_dict[mn.type] + ") 在搏斗中受伤了. 在你治好它之前它只能歇着了.")
                                changes["obedience"] -= dice(3)
                                changes["fear"] -= dice(3)
                                girl.add_log("minion_hurt")

                                calendar.set_alarm(calendar.time+1, StoryEvent(label="farm_resisted", type="morning", call_args=[girl, "rebel minion hurt"]))

                        elif fight_res: # Girl wins
                            pic = "gizel whip struggling" # Picture(path="NPC/gizel/whip3.webp")
                            # pic_bg = inst.get_pic()
                            descript += event_color["bad"] % (girl.name + " " + farm_related_dict[reaction] + "攻击了吉泽, 在她吟唱魔法时就一脚将她踢翻在地!\n")
                            ev_sound = s_crash

                            if dice(6) >= 4:
                                descript += event_color["bad"] % (girl.name + " 在深夜中潜逃了.")
                                run_away = True
                                changes["obedience"] -= dice(3) + 2
                                changes["fear"] -= dice(3) + 2
                                girl.add_log("farm_run_away")

                                # calendar.set_alarm(calendar.time+1, Event(label="run_away", object=girl))
                                calendar.set_alarm(calendar.time+1, StoryEvent(label="farm_resisted", type="morning", call_args=[girl, "rebel runaway"]))

                            else:
                                mn = rand_choice(self.minions)
                                mn.hurt = True
                                if mn.type == "machine":
                                    descript += event_color["bad"] % (mn.name + " (等级 " + str(mn.level) + " 的" + farm_related_dict[mn.type] + ") 在搏斗中损坏了. 在你修好它之前它只能吃灰了.")
                                else:
                                    descript += event_color["bad"] % (mn.name + " (等级 " + str(mn.level) + " 的" + farm_related_dict[mn.type] + ") 在搏斗中受伤了. 在你治好它之前它只能歇着了.")
                                changes["obedience"] -= dice(3) + 2
                                changes["fear"] -= dice(3) + 1
                                girl.add_log("minion_hurt")

                                calendar.set_alarm(calendar.time+1, StoryEvent(label="farm_resisted", type="morning", call_args=[girl, "rebel minion hurt"]))

                        else: # Gizel wins
                            pic = "gizel whip happy" # Picture(path="NPC/gizel/whip2.webp")
                            # pic_bg = inst.get_pic()
                            descript += event_color["good"] % (girl.name + " " + farm_related_dict[reaction] + " 想要还击, 但是吉泽随便用了个捆绑术就把她制服了.\n")
                            ev_sound = s_punch

                            if dice(6) >= 4:
                                descript += event_color["fear"] % ("她强烈刺激了 " + girl.name + "的内心, 让她瑟瑟发抖.")
                                changes["fear"] += dice(3) + 2
                                changes["obedience"] += dice(3)

                            else:
                                descript += event_color["fear"] % ("她用魔法强制让 " + girl.name + " 摆出屈辱的姿势.")
                                changes["fear"] += dice(3)
                                changes["obedience"] += dice(3) + 2

                            calendar.set_alarm(calendar.time+1, StoryEvent(label="farm_resisted", type="morning", call_args=[girl, "rebel subdued"]))

                    else:
                        descript += event_color["a little bad"] % (girl.name + " " + farm_related_dict[reaction] + " 训练，并且不服从吉泽.\n")

                        if dice(6) >= 3:
                            pic = "gizel whip angry"# Picture(path="NPC/gizel/whip1.webp")
                            # pic_bg = inst.get_pic()
                            ev_sound = s_punch
                            descript += event_color["fear"] %  ("吉泽被她的傲慢激怒了，狠狠地抽了她一顿.")
                            changes["fear"] += dice(3)
                            changes["obedience"] += dice(3)
                            changes["energy"] -= 10

                        else:
                            pic = farm.pen_pic
                            descript += event_color["a little bad"] % ("吉泽尔很生气，对她失去了耐心，让她在笼子里自生自灭.")
                            changes["obedience"] -= 1
                            changes["energy"] += 10
                            farm.locked_girls.append(girl)

                        calendar.set_alarm(calendar.time+1, StoryEvent(label="farm_resisted", type="morning", call_args=[girl, "rebel subdued"]))

                    log.add_report(descript)

                elif self.installation: # sanity check
                    if reaction == "accepted":
                        descript += girl.name + " 被送进 " + farm_related_dict[self.installation.name] + " 接受训练时没有抱怨."
                    elif reaction == "resisted":
                        descript += girl.name + " 又哭又闹, 但吉泽一边嘲讽着一边把她踢进 " + farm_related_dict[self.installation.name] + " 接受训练."
                        calendar.set_alarm(calendar.time+1, StoryEvent(label="farm_resisted", type="morning", call_args=[girl, "resisted"]))
                    elif reaction == "refused":
                        descript += girl.name + " 哀求着不要, 但吉泽一边怒吼着一边把她踢进 " + farm_related_dict[self.installation.name] + "."
                        calendar.set_alarm(calendar.time+1, StoryEvent(label="farm_resisted", type="morning", call_args=[girl, "refused"]))

                # Learn from interaction

                if not self.act in farm.knows["reaction"][girl]:
                    farm.knows["reaction"][girl].append(self.act)

                # Stops here and return event if girl fought or resisted successfully

                if training_stop:
                    change_log = self.apply_changes(girl, changes)
                    farm_events.append(Event(pic = pic, background = pic_bg, char = girl.char, text = descript, changes = change_log, sound = ev_sound, type = "Health/Security"))

                    if self.duration > 0: # Antiquated
                        self.duration -= 1

                    return farm_events

                ## TRAINING continues if the girl didn't successfully rebel

                girl.add_log("farm_training_days")

                descript += " "

                if self.act == "group":
                    descript += farm_description[self.act + " intro"] % (girl.fullname, str(len(self.minions)) + " " + rand_choice(minion_adjectives[min_type]) + " " + min_type)
                else:
                    descript += farm_description[self.act + " intro"] % (girl.fullname, article(rand_choice(minion_adjectives[min_type])) + " " + min_type)

                ## Calculates roll modifier

                # Add minion level/group bonus

                training_modifier += sum(mn.level for mn in self.minions) // len(self.minions)

                if len(self.minions) >= 3:
                    training_modifier += 1

                # Test minion weakness

                if self.minions[0].type == girl.weakness or girl.get_effect("special", "all farm weaknesses"):
                    training_modifier += 1
                    weak = True

                    if not farm.knows["weakness"][girl]:
                        descript += " 吉泽注意到 " + girl.name + " 在 " + self.minions[0].type + "面前有强烈的反应 (" + event_color["fear"] % "weakness discovered" + ")."
                        farm.knows["weakness"][girl] = farm_installations_dict[girl.weakness]

                        calendar.set_alarm(calendar.time+1, StoryEvent(label="farm_discovered_weakness", call_args=[girl]))

                    else:
                        MC.evil += 0.2 # Knowingly using weaknesses is evil
                        changes["fear"] += 1

                        if girl.get_effect("special", "all farm weaknesses"):
                            descript += " 吉泽发现 " + girl.name + " 会 " + event_color["fear"] % "对所有的仆从都感到恐惧" + ", 利用她的弱点来训练她."
                        else:
                            descript += " 吉泽发现 " + girl.name + " 对 " + event_color["fear"] % ("这些 " + girl.weakness + "感到害怕") + ", 利用她的弱点来训练她."
                else:
                    weak = False

                # Checks act and fix weaknesses

                if self.act in girl.pos_acts and self.act in girl.neg_acts: # Ambivalent act
                    changes["sensitivity"] += 1
                    if reaction != "accepted":
                        changes["mood"] -= 1

                    if not self.act in farm.knows["amb_acts"][girl]:
                        ev_sound = s_spell
                        descript += " " + girl.name + " 非常紧张和困惑. " + event_color["average"] % ("吉泽发现她对 " + long_act_description[self.act] + "感到矛盾.")
                        girl.personality_unlock[self.act] = True
                        farm.knows["amb_acts"][girl].append(self.act)
                    else:
                        descript += " " + girl.name + " 十分矛盾, 她也不知道自己到底有什么样的感觉 " + long_act_description[self.act] + "."

                elif self.act in girl.pos_acts: # Positive act
                    changes["libido"] += 1
                    if reaction != "refused":
                        changes["mood"] += 1

                    if not self.act in farm.knows["pos_acts"][girl]:
                        ev_sound = s_spell
                        descript += " " + girl.name + " 面色潮红，呼吸急促, 她的乳头勃起得像葡萄. " + event_color["good"] % ("吉泽发现她喜欢 " + long_act_description[self.act] + ".")
                        girl.personality_unlock[self.act] = True
                        farm.knows["pos_acts"][girl].append(self.act)
                    else:
                        descript += " " + girl.name + " 在训练 " + self.act + " 时十分满足, 她乐在其中."
                    training_modifier += 1

                elif self.act in girl.neg_acts: # Negative act
                    if reaction != "accepted":
                        changes["mood"] -= 2
                    else:
                        changes["mood"] -= 1
                    if not self.act in farm.knows["neg_acts"][girl]:
                        ev_sound = s_spell
                        descript += " " + girl.name + " 一直紧张和抗拒, 在整个训练过程中都十分害怕. " + event_color["a little bad"] % ("吉泽发现她讨厌 " + long_act_description[self.act] + ".")
                        girl.personality_unlock[self.act] = True
                        farm.knows["neg_acts"][girl].append(self.act)
                    else:
                        descript += " " + girl.name + " 对 " + self.act + " 感到不适, 所以她还是对此紧张和抗拒."

                    training_modifier -= 1

                fix = rand_choice(get_fix_list(self.act))

                if fix.name in [f.name for f in girl.pos_fixations]:
                    training_modifier += 1
                    ev_sound = s_mmmh
                    if reaction != "refused":
                        changes["mood"] += 1
                    changes["libido"] += 1
                    if not fix in farm.knows["pos_fix"][girl]:
                        descript += " 训练过程中, 吉泽发现了一个 " + girl.name + "的爱好 (" + event_color["good"] % fix.name + ")!"
                        girl.personality_unlock[fix.name] = True
                        farm.knows["pos_fix"][girl].append(fix)
                        test_achievement("pos fixations")
                    else:
                        descript += " 训练效果比想象中的更好, 因为吉泽利用了 " + girl.name + " 对 " + event_color["good"] % fix.name + " 的痴迷来训练她."

                elif fix.name in [f.name for f in girl.neg_fixations]:
                    training_modifier += 1
                    ev_sound = s_surprise
                    if reaction != "accepted":
                        changes["mood"] -= 1
                        changes["fear"] += 1
                    if not fix in farm.knows["neg_fix"][girl]:
                        descript += " 在训练时，吉泽发现 " + girl.name + " 真的非常讨厌 (" + event_color["fear"] % fix.name + ")."
                        girl.personality_unlock[fix.name] = True
                        farm.knows["neg_fix"][girl].append(fix)
                        test_achievement("neg fixations")
                    else:
                        descript += " 训练效果比想象中的更好, 因为吉泽利用了 " + girl.name + "对 " + event_color["fear"] % fix.name + " 的恐惧来训练她."

                # Determines result (= boost to preference unlocking)

                roll = dice(6) + training_modifier # Substract girl rank?

                if roll >= 5:
                    final_result = 2.5 #!
                    descript += farm_description[self.minions[0].type + " good"] % girl.name
                elif roll >= 3:
                    final_result = 1.5 #!
                    descript += farm_description[self.minions[0].type + " average"] % girl.name
                else:
                    final_result = 0.5 #!
                    descript += farm_description[self.minions[0].type + " bad"] % girl.name

                base_result = 1 + round_int(final_result) # base_result is used below with dice() and should always be an integer

                if girl.is_("very sub"):
                    final_result += 1
                elif girl.is_("dom"):
                    final_result -= 0.5
                elif girl.is_("very dom"):
                    final_result -= 1

                if reaction == "accepted":
                    brk, new_pref = girl.raise_preference(self.act, type=None, bonus=final_result, status_change=True)
                else:
                    brk, new_pref = girl.raise_preference(self.act, type="fear", bonus=final_result, status_change=True)


                # Pop Virginity

                if self.act in ("sex", "group"):
                    if girl.pop_virginity(origin="farm"):
                        changes["obedience"] += 2 + dice(6)
                        descript += "\n{color=[c_lightred]}" + girl.name + " 把处女献给了 " + article(rand_choice(minion_adjectives[self.minions[0].type])) + " " + self.minions[0].type + "!{/color}"
                        log.add_report("{color=[c_lightred]}" + girl.fullname + " 把处女献给了 " + article(rand_choice(minion_adjectives[self.minions[0].type])) + " " + self.minions[0].type + "!{/color}")


                ## Stat changes

                # Installation and Sex skills

                changes[self.installation.skill] += dice(base_result) - 1

                if self.act in all_sex_acts:
                    changes[self.act] += dice(base_result) - 1
                elif self.act == "naked":
                    changes[rand_choice(["obedience", "libido", "beauty", "body"])] += dice(base_result) - 1
                elif self.act == "bisexual":
                    changes[rand_choice(["service", "sensitivity", "sex", "libido"])] += dice(base_result) - 1
                elif self.act == "group":
                    changes[rand_choice(["service", "sex", "anal", "constitution"])] += dice(base_result) - 1

                # BBCR skills degrade over time at the farm

                d = dice(6) # 1: -1 stats, 2-4: -0.5 stat, 5-6: nothing
                if 1 < d < 5:
                    changes[rand_choice(["beauty", "body", "charm", "refinement"])] -= 0.5
                elif d <= 1:
                    changes[rand_choice(["beauty", "body", "charm", "refinement"])] -= 0.5
                    changes[rand_choice(["beauty", "body", "charm", "refinement"])] -= 0.5

                ## Generate event(s)

                change_log = self.apply_changes(girl, changes)

                # Alarm set if stat maxed out

                if self.act in all_sex_acts:
                    if girl.get_stat(self.act, raw=True) >= girl.get_stat_minmax(self.act, raw = True)[1]:
                        calendar.set_alarm(calendar.time+1, StoryEvent(label="farm_max_skill", type="morning", call_args=[girl, self.act]))

                if girl.get_preference(self.act) == "fascinated" and prog.condition == "none":
                    calendar.set_alarm(calendar.time+1, StoryEvent(label="farm_max_pref", type="morning", call_args=[girl, self.act]))

                # Energy changes (not rebelled)

                t = 5 + dice(10)

                if len(self.minions) > 1:
                    t += 5 + dice(10)

                text1, chg = girl.tire(t) #!

                descript += text1
                change_log.add("Energy: %s/%i (%s)" % ("{color=%s}%i{/color}" % (girl.get_energy_color(), girl.energy), girl.get_stat_max("energy"), plus_text(chg, color_scheme="standard", decimals=1)), before_separator="\n")

                # Minion level

                for mn in self.minions:
                    mn.xp += girl.rank
                    if mn.level_up():
                        change_log.add("仆从升级 (等级 " + str(mn.level) + ")", col="special")

                # Breaking text

                text_changes = __(self.act.capitalize()) + ": "

                if brk > 0:
                    _col = c_green
                    for i in range(int(1 + brk//50)):
                        text_changes += "+"
                        if i > 3:
                            break
                elif brk < 0:
                    _col = c_red
                    text_changes += "-"

                if brk:
                    change_log.add(text_changes, col=_col)

                # Determines training pic

                not_tags = prepare_not_tags(girl, self.act, farm=True) # Reminder: group and bisexual pics are not filtered for the farm

                if self.installation.name == "stables": # May use regular sex pictures for stallions (act > installation.tags)
                    if not pic:
                        pic = girl.get_pic(self.act, and_tags = self.installation.tags, not_tags=not_tags, hide_farm=True, pref_filter=True) # Will exclude beast, monster and machine tags (unless used with fetish act for the latter)

                        if not pic: # Happens if some pictures are disabled
                            attempts = game.last_pic["attempts"]
                            pic = girl.get_pic(self.act, "sex", "naked", attempts=attempts, pref_filter=True)

                else: # May not use regular pictures for monsters, beasts and machines (installation.tags > act)
                    if not pic:
                        pic = girl.get_pic(self.installation.tags, and_tags = self.act, not_tags=not_tags, strict=True, pref_filter=True)

                        if not pic:
                            if self.act != "naked": # Avoids displaying hardcore picture from the girl pack for naked acts
                                attempts = game.last_pic["attempts"]
                                pic = girl.get_pic(self.installation.tags, and_tags = self.act, not_tags=not_tags, attempts=attempts, pref_filter=True)

                            if not pic: # Farm default pictures will always have a 'safe' naked option
                                attempts = game.last_pic["attempts"]
                                pic = farm.get_pic(self.installation.tags, and_tags = self.act, not_tags=not_tags, attempts=attempts)

                ## Adds main event

                log.add_report(girl.fullname + "在" + farm_related_dict[self.installation.name] + "中训练了" + girl_related_dict[self.act] + "。")

                farm_events.append(Event(pic, background = pic_bg, char = girl.char, text = descript, changes = change_log, sound = ev_sound, type = "Farm"))

                # Adds another event if change of preference status

                if new_pref and new_pref != "refuses":
                    if girl.is_("lewd"):
                        text1 = "lewd"
                    else:
                        text1 = "modest"

                    farm_events.append(Event(pic, background = pic_bg, char = girl.char, text = (pref_response[text1 + " " + new_pref] % long_act_description[self.act]), changes = change_log, sound = s_ahaa, type = "special"))

                    text1 = girl.fullname + "现在对" + girl_related_dict[self.act] + "行为一副" + preference_color[new_pref] % girl_related_dict[new_pref] + " 的模样。"
                    log.add_report(text1)

                    farm_events.append(Event(pic, background = pic_bg, char = narrator, text = "\n" + text1, changes = change_log, sound = s_spell, type = "special"))


            ## RESOLVE RESTING ##

            elif type == "resting" or self.holding == "rest":

                girl.add_log("farm_rest_days")

                if self.tired:
                    if girl.hurt > 0:
                        descript += event_color["bad"] % (girl.fullname + " 受伤了，今天不得不在牢房里休息.\n")
                    elif girl.energy <= 0:
                        descript += event_color["bad"] % (girl.fullname + " 今天累坏了，今天不得不在牢房里休息.\n")
                    descript += event_color["average"] % (girl.fullname + " 看起来疲惫不堪, 所以吉泽让她在牢房里休息 (auto-resting: " + farm_related_dict[self.resting] + ").\n")

                elif self.inst_full:
                    descript += event_color["a little bad"] % ("我们没有更多的仆从来训练她, 所以 " + girl.fullname + " 在牢房里休息了一天.\n")

                elif self.refused:
                    descript += event_color["bad"] % (girl.fullname + " 今天拒绝训练, 所以吉泽只能把她丢在牢房里") + " (训练模式: {i}" + farm_related_dict[self.mode] + "{/i}).\n"

                stat = ""
                text1, change_log = girl.rest(context="farm")
                descript += text1

                changes["mood"] += dice(2)

                if dice(6) >= 5: # Random chance of event
                    stat = rand_choice(("constitution", "obedience", "sensitivity", "libido"))
                    descript += "\n" + farm_description["pen " + stat] % girl.name
                    changes[stat] += dice(2)

                if stat == "libido":
                    pic = girl.get_pic("mast", "libido", and_tags=["dirty", "hurt"], and_priority=False, not_tags=["group", "bisexual", "sex", "anal"])
                    if not pic:
                        attempts = game.last_pic["attempts"]
                        pic = girl.get_pic("rest", "profile", and_tags = "naked", attempts=attempts)
                else:
                    pic = girl.get_pic("rest", "profile", and_tags=["dirty", "hurt"], and_priority=False, naked_filter=True)

                change_log.merge(self.apply_changes(girl, changes))

                log.add_report(girl.fullname + " 在牢房里休息了一天.")

                farm_events.append(Event(pic, background = "bg pen", char = girl.char, text = descript, changes = change_log, type = "Farm"))

            ## RESOLVE HOLDING ##

            else: # Holding

                girl.add_log("farm_holding_days")

                if self.inst_full:
                    descript += event_color["a little bad"] % ("我们没有更多的仆从来训练她, 所以 " + girl.fullname + " 今天在农场干了一天的活")

                elif self.refused:
                    descript += event_color["bad"] % (girl.fullname + " 今天拒绝训练, 所以吉泽让她在农场干了一天的活 ") + "(训练模式: {i}" + farm_related_dict[self.mode] + "{/i})"

                else:
                    descript += girl.fullname + "今天就在农场休息"

                log.add_report(descript + ", " + farm_holding_dict[self.holding].lower() + ".")

                descript += ".\n" + farm_description["holding %s %s" % (self.mode, self.holding)] % (girl.name, girl.name)
                act, decreased = farm_holding_stats[self.holding]

                if self.mode == "gentle":
                    if dice(250) > girl.get_stat(self.holding, raw=True):
                        changes[self.holding] += dice(2)

                elif self.mode == "tough":
                    if dice(250) > girl.get_stat(self.holding, raw=True):
                        changes[self.holding] += dice(4)

                    changes["fear"] += dice(3) - 1

                    MC.good -= 0.15 # Pushing something she doesn't like is not nice

                    if not girl.is_(["very sub", "lewd"]):
                        changes["mood"] -= 1

                elif self.mode == "hardcore":
                    if dice(250) > girl.get_stat(self.holding, raw=True):
                        changes[self.holding] += dice(4) + 1

                    changes["fear"] += dice(3)

                    MC.evil += 0.15 # Using hardcore mode is *evil*

                    if girl.personality.name not in ("masochist"):
                        changes["mood"] -= 2

                d = dice(6)

                if d == 1:
                    if dice(250) < girl.get_stat(decreased, raw=True):
                        changes["mood"] -= 2
                        changes["fear"] += 1
                        changes[decreased] -= 1
                        descript += farm_description["holding " + self.holding + " bad"] % girl.name
                elif d == 6:
                    changes["mood"] += 2
                    changes["fear"] -= 1
                    changes[self.holding] += 1
                    brk, new_pref = girl.raise_preference(act, status_change=True)
                    pic = girl.get_pic(act, not_tags=all_sex_acts+["group"])
                    descript += farm_description["holding " + self.holding + " good"] % girl.name
                    text_changes = __(girl_related_dict[act.capitalize()]) + ": "

                    if brk > 0:
                        text_changes += "{color=[c_green]}"
                        for i in range(int(1 + brk//50)): text_changes += "+"
                        text_changes += "{/color}"
                    elif brk < 0:
                        text_changes += "{color=[c_red]}-{/color}"

                    if brk:
                        change_log.add(text_changes)

                # BBCR skills degrade over time at the farm

                d = dice(6) # 1: -2 stats, 2-4: -1 stat, 5-6: nothing

                if d < 5:
                    changes[rand_choice(["beauty", "body", "charm", "refinement"])] -= 1
                    if d == 1:
                        changes[rand_choice(["beauty", "body", "charm", "refinement"])] -= 1

                change_log.merge(self.apply_changes(girl, changes))

                if girl.get_stat(self.holding, raw=True) >= girl.get_stat_minmax(self.holding, raw = True)[1]:
                    calendar.set_alarm(calendar.time+1, StoryEvent(label="farm_max_skill", type="morning", call_args=[girl, self.holding]))

                text1, chg = girl.tire(dice(4)+2)
                descript += text1
                change_log.add("Energy: %s/%i (%s)" % ("{color=%s}%i{/color}" % (girl.get_energy_color(), girl.energy), girl.get_stat_max("energy"), plus_text(chg, color_scheme="standard", decimals=1)), before_separator="\n")

                if not pic:
#                    renpy.say("", "Searching girl pic for " + and_text(farm_holding_tags[self.holding]))
                    attempts = game.last_pic["attempts"]
                    pic = girl.get_pic(farm_holding_tags[self.holding], attempts=attempts, soft=True)
                if not pic:
#                    renpy.say("", "Searching farm pic")
                    attempts = game.last_pic["attempts"]
                    pic = farm.get_pic(farm_holding_tags[self.holding], attempts=attempts)

                farm_events.append(Event(pic, background="bg farm", char = girl.char, text = descript, changes = change_log, type = "Farm"))

            # Updates duration

            if self.duration > 0:
                self.duration -= 1

            # Returns final list of events

            return farm_events


        def apply_changes(self, girl, changes):

            change_log = NightChangeLog(girl.fullname)

            for stat, chg in changes.items():

                # Generates mojo
                if stat == "fear":
                    if self.target == "no training":
                        mojo_color = rand_choice(mojo_act_dict[self.holding])
                    else:
                        mojo_color = rand_choice(mojo_act_dict[self.act])

                    changes[stat] = girl.change_fear(chg*reverse_if(girl.get_effect("boost", "farm fear generation"), chg), mojo_color=mojo_color)

                    if changes[stat] >= 1:
                        change_log.add("{image=img_fear}" * min(3, round_int(changes[stat]/2))) # Adds one to three fear icons

                changes[stat] = girl.change_stat(stat, chg)

                if stat not in ("mood", "fear", "love"):
                    change_log.add("%s: %i/%i (%s)" % (__(girl_related_dict[stat.capitalize()]), girl.get_stat(stat), girl.get_stat_max(stat), plus_text(changes[stat], color_scheme="standard")))

            return change_log


    class Farm(object):

        def __init__(self):
            self.pens = 1
            self.installations = farm_installations
            self.girls = []
            self.default_mode = "tough"
            self.default_holding = "rest"
            self.default_resting = "intensive"

            self.programs = {}
            self.knows = {"weakness" : defaultdict(bool), "reaction" : defaultdict(list), "pos_acts" : defaultdict(list), "amb_acts" : defaultdict(list), "neg_acts" : defaultdict(list), "pos_fix" : defaultdict(list), "neg_fix" : defaultdict(list)}
            self.active = False
            self.powers = False

            self.pen_pic = Picture("pen.webp", "brothels/farm/pen.webp")
            unlock_pic(self.pen_pic.path)
            self.load_pics()

            self.effects = []
            self.effect_dict = defaultdict(list)

        def activate(self):
            self.active = True
            renpy.play(s_moo, "sound")
            notify("Farm unlocked!", pic="tb farm", col=c_softpurple)

        # Effects (farm effects apply to farm girls only)

        def get_effect(self, type, target):
            return get_effect(self, type, target)

        def add_effects(self, effects, apply_boost=False, spillover=False, expires = False):
            return add_effects(self, effects, apply_boost=apply_boost, spillover=spillover, expires=expires)

        def remove_effects(self, effects):
            remove_effect(self, effects)


        def load_pics(self):
            self.pics = []

            imgfiles = [file for file in renpy.list_files() if (file.startswith("default/farm/") and is_imgfile(file))]

            # Attaching each picture to the list with appropriate tags

            for file in imgfiles:

                file_name = file.split("/")[-1]

                self.pics.append(Picture(file_name, file))

        def get_pic(self, tags, alt_tags1 = None, alt_tags2 = None, alt_tags3 = None, and_tags = None, not_tags = None, strict = False, attempts=0):
            return get_pic(self, tags=tags, alt_tags1=alt_tags1, alt_tags2=alt_tags2, alt_tags3=alt_tags3, and_tags=and_tags, not_tags=not_tags, strict=strict, attempts=attempts)

        def get_pen_limit(self):
            return brothel.get_maxbedrooms() // 2

        def get_pen_cost(self):
            return 100 * self.pens

        def has_room(self):
            if len(self.girls) < self.pens:
                return True
            return False

        def add_pen(self):
            if self.pens >= self.get_pen_limit():
                return False, "你无法再扩大农场了. 上面会注意到我们的..."
            elif MC.gold < self.get_pen_cost():
                return False, "你没有足够多的金币! 别再浪费我的时间."
            elif renpy.call_screen("yes_no", "你确定要为农场加盖一间牢房吗？这将花费 " + str(farm.get_pen_cost()) + " 金币."):
                MC.gold -= self.get_pen_cost()
                self.pens += 1
                renpy.play(s_gold, "sound")
                return True, "你为奴隶农场加盖了一间牢房.现在农场可以再多容纳一个女孩."
            else:
                return False, ""

        def upgrade(self, inst): # Where inst is an object
            return inst.upgrade()

        def send_girl(self, girl, program):
            girl.work_whore = False
            if girl in MC.girls:
                MC.girls.remove(girl)
                if MC.girls:
                    selected_girl = MC.girls[0]
                else:
                    selected_girl = None
            if girl in brothel.master_bedroom.girls:
                brothel.master_bedroom.remove_girl(girl)
            if girl not in self.girls:
                self.girls.append(girl)
            self.change_program(girl, program)

        def remove_girl(self, girl):
            if girl not in MC.girls:
                MC.girls.append(girl)
            if girl in self.girls:
                self.girls.remove(girl)
#             del self.programs[girl]
            self.assign_girls()

        def reset(self): # Resets all programs to default and 'evicts' girls that don't belong

            self.programs = {}

            for girl in self.girls:
                if girl in MC.girls:
                    self.remove_girl(girl)
                else:
                    self.programs[girl] = FarmProgram(girl)
                    self.programs[girl].update()

            self.assign_girls()

        def change_program(self, girl, program):
            program.update()
            self.programs[girl] = program
            self.assign_girls()

        def refresh(self):
            self.locked_girls = []
            self.unassignable = []
            self.refused = []
            self.tired = []
            for inst in self.installations.values():
                inst.refresh()
            for prog in self.programs.values():
                prog.refresh()

        def test_exit_conditions(self, girl): # returns reason if girl is ready to exit
            prog = self.programs[girl]
            if prog.duration == 0:
                return "time up"
            elif prog.condition != "none" and prog.target != "no training":
                if prog.target == "auto":
                    available_acts = [act for act in extended_sex_acts if girl.will_do_farm_act(act, prog.mode) and not compare_preference(girl, act, prog.condition)]
                    if not available_acts:
                        return "condition met"
                else:
                    if not girl.will_do_farm_act(prog.target, prog.mode) or compare_preference(girl, prog.target, prog.condition):
                        return "condition met"
            return False

        def test_resting_conditions(self, girl): # returns True if girl must rest
            if self.programs[girl].resting == "conservative":
                if self.programs[girl].act == "group" and girl.energy <= 30:
                    return True
                elif girl.energy <= 15:
                    return True

            elif self.programs[girl].resting == "intensive":
                if self.programs[girl].act == "group" and girl.energy <= 20:
                    return True
                elif girl.energy <= 10:
                    return True

            elif girl.energy <= 0:
                return True

            elif girl.hurt > 0:
                return True

            return False

        def exhaust_girl(self, girl, energy): # May hurt a girl if her energy is too low
            if energy <= -10:
                girl.get_hurt(dice(5))
            elif energy < 0:
                girl.get_hurt(dice(3))

#        def recover_girl(self, girl):

        def assign_girls(self, logging=False): # Send girls to the appropriate facility, returns 3 girl lists: training, holding (work), resting

            self.refresh()

            training_girls = []
            holding_girls = []
            resting_girls = []

            unassigned = []

            debug_report = ""

            # first round of assignation

            for girl in self.girls:

                prog = self.programs[girl]

                # Auto-resting test

                if farm.test_resting_conditions(girl):
                    prog.tired = True
                    resting_girls.append(girl)
                    if logging: log.add_report(girl.fullname + " 疲惫不堪，吉泽把她送去休息了 (作息规则: " + self.programs[girl].resting + ").")
#                    renpy.say(girl.name + " is too tired")

                # Holding girls

                elif prog.target == "no training" and prog.holding == "rest":
                    resting_girls.append(girl)

                elif prog.target == "no training":
                    holding_girls.append(girl)

                # Training girls

                else:

                    # Assign training

                    if self.assign_training(girl):

                        # Assign preferred facility if exists

                        if prog.installation and not prog.auto_inst:
                            prog.installation.girls.append(girl)
                            if logging: log.add_report("根据她的训练计划，" + girl.fullname + "被指派到" + farm_related_dict[prog.installation.name])
                        elif prog.avoid_weakness: # Assigns to another installation if has been ordered to by the player
                            for inst in renpy.random.sample(list(self.installations.values()), len(self.installations.values())):
                                if inst != self.installations[self.knows["weakness"][girl]] and inst.count_free_minions() > 0:
                                    prog.installation = inst
                                    inst.girls.append(girl)
                                    break
                            else:
                                unassigned.append(girl)
                        elif self.knows["weakness"][girl] and not girl.get_effect("special", "all farm weaknesses"):
                            # Assigns to an installation corresponding to her weakness if known and auto on
#                            renpy.say("", "Farm knows " + girl.name + " is weak to " + self.knows["weakness"].name)
                            prog.installation = self.installations[self.knows["weakness"][girl]]
                            self.installations[self.knows["weakness"][girl]].girls.append(girl)
                            if logging: log.add_report(girl.fullname + " 被送去 " + farm_related_dict[prog.installation.name] + " 训练。因为吉泽知道她害怕 " + self.knows["weakness"][girl] + "s.")
                        else:
#                            renpy.say("", "Farm doesn't know " + girl.name + " 's weakness.")
                            unassigned.append(girl)

                    # Refused training

                    elif prog.holding == "rest":
                        resting_girls.append(girl)
                        if logging: log.add_report(girl.fullname + " 拒绝训练并被安排去休息.")
                    else:
                        holding_girls.append(girl)
                        if logging: log.add_report(girl.fullname + " 拒绝训练并被安排去工作.")

            for inst in self.installations.values():
                excess_girls = inst.assign_minions() # Returns excess girls to be assigned elsewhere automatically

                if logging:
                    for girl in excess_girls:
                        log.add_report(girl.fullname + " 无法在 " + farm_related_dict[self.name] + " 训练，因为没有更多的仆从.")

                unassigned += excess_girls

#            debug_report += "Unassigned: " + and_text([g.name for g in unassigned])

            # Second round of assignation

            renpy.random.shuffle(unassigned)
            available_installations = list(self.installations.values())
            renpy.random.shuffle(available_installations)

            for girl in unassigned:
                prog = self.programs[girl]
                for inst in available_installations:
                    if inst.count_free_minions() > 0 and prog.act != "group":
                        prog.installation = inst
                        inst.girls.append(girl)
                        inst.assign_minions()
                        if logging: log.add_report(girl.fullname + " 被安排在 " + farm_related_dict[self.name] + "训练.")
                        break
                    elif inst.count_free_minions() > 1:
                        prog.installation = inst
                        inst.girls.append(girl)
                        inst.assign_minions()
                        if logging: log.add_report(girl.fullname + " 被安排在 " + farm_related_dict[self.name] + "训练.")
                        break

            for inst in self.installations.values():
                for girl in inst.girls:
                    training_girls.append(girl)

            # Final assignation

            for girl in self.girls:
                prog = self.programs[girl]

                if girl not in (training_girls + holding_girls + resting_girls):

                    prog.inst_full = True

                    if prog.holding == "rest":
                        resting_girls.append(girl)
                        if logging: log.add_report(girl.fullname + " 无法在设施里训练，被安排去休息.")
                    else:
                        holding_girls.append(girl)
                        if logging: log.add_report(girl.fullname + " 无法在设施里训练，被安排去工作.")

#            if debug_mode:
#                debug_report += "\nIn training: " + and_text([g.name for g in training_girls]) + "\nHolding: " + and_text([g.name for g in holding_girls]) + "\nResting: " + and_text([g.name for g in resting_girls])
#                renpy.say("", debug_report)

            return training_girls, holding_girls, resting_girls

        def assign_training(self, girl): # Assigns an 'act' to train for the night. Returns False if impossible.

#            renpy.say("", "Assigning training to " + girl.name)

            prog = self.programs[girl]

            if prog.target == "no training":
                prog.act = None
                if debug_mode:
                    renpy.say("", "WRONG: not in training")
                return False
            elif prog.target != "auto":
                prog.act = prog.target
                return True
            else: # Auto assign
                available_acts = []
                maybe = []

                for act in extended_sex_acts:
                    if girl.will_do_farm_act(act, self.programs[girl].mode):

                        # Checks if has already reached condition (the act then becomes less of a priority)

                        if self.programs[girl].condition == "none":
                            available_acts.append(act)
                        else:
                            if compare_preference(girl, act, self.programs[girl].condition):
                                maybe.append(act)
                            else:
                                available_acts.append(act)

                if available_acts:
                    self.programs[girl].act = rand_choice(available_acts)
                    return True
                elif maybe:
                    self.programs[girl].act = rand_choice(maybe)
                    return True
                else:
                    self.programs[girl].act = None
                    prog.refused = True
                    debug_notify("%s refused all training" % girl.fullname, pic=girl.portrait)
                    return False

        def count_minions(self):
            _min = 0
            for inst in self.installations.values():
                _min += len(inst.minions)

            return _min

        def get_minions(self, type):

            return self.installations[farm_installations_dict[type]].minions

        def get_hurt_minions(self):

            minions = []

            for inst in self.installations.values():
                minions += inst.get_hurt_minions()

            return minions

        def hurt_minions(self): # Runs every turn to reduce minions health until they retire

            retired = []

            for inst in self.installations.values():
                for mn in inst.get_hurt_minions():
                    mn.hp -= 1

                    if mn.hp <= 0:
                        inst.minions.remove(mn)
                        retired.append(mn)

            return retired

        def remove_minion(self, mn):
            self.installations[farm_installations_dict[mn.type]].minions.remove(mn)

#         def add_girl(self, girl):

#             if len(self.girls) < self.pens and girl not in self.girls:
#                 self.girls.append(girl)

#                 if not gisele.knows[girl]:
#                     gisele.knows[girl] = defaultdict(bool)

#             else:
#                 renpy.say(gizel, "Well, it seems that all the pens are full at the moment.")

#                 if len(self.pens) < self.pen_limit:
#                     if self.add_pen() and girl not in self.girls:
#                         self.add_girl(girl)

#             return False

#        def remove_girl(self, girl):

#            if girl in self.girls:
#                self.girls.remove(girl)
#                return True
#            else:
#                raise AssertionError(girl.name + " not found in farm")
##                return False

        def add_minion(self, minion):
            inst = self.installations[farm_installations_dict[minion.type]]
            return inst.add_minion(minion)

        def remove_minion(self, minion):
            for installation in self.installations.values():
                if minion in installation.minions:
                    installation.minions.remove(minion)
                    return True
            else:
                raise AssertionError(minion.name + " not found in farm")
                return False

#        def get_free_minions(self):

#            free_minions = [mn for mn in self.minions if mn.free]

#            return free_minions

#        def get_available_minion(self, program, type=None):

#            # Get the best available minion (if provided, a given type is chosen)

#            free_minions = self.get_free_minions()

#            if free_minions:
#                free_minions.sort(key = lambda x: x.score_me(program, type), reverse = True)
#                return free_minions[0]

#            return None

#### END OF BK FARM FILE ####
