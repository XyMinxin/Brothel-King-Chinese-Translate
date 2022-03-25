####            CLASSES FOR B KING                    ####################################################
##   Those are the classes used with the game.          ##################################################
##   Girl class and functions are in separate files.    ##################################################
##                                                      ##################################################


init -2 python:
    #<Chris12 PackState>
    import hashlib
    import datetime
    #</Chris12 PackState>

## PRIMARY CLASSES ##

    class Game(object):

        """This class keeps track of various story related variables and methods."""

        def __init__(self):

            self.version = config.version
            self.started = False
            self.chapter = 1
            self.set_max_girl_level()
            self.starting_gold = str(starting_gold) # Must be a string to allow player input
            self.token = 0
            self.girl_id_generated = 0
            self.free_girls = []
            self.kidnapped = []
            self.goals = chapter_goals[1]
            # self.set_task(self.get_goal_description())
            self.seen_goal_message = False
            self.blocked_districts = []
            self.active_mods = {}
            self.track_dict = defaultdict(int)
            self.last_pic = {"tags": [], "and_tags": [], "not_tags": [], "attempts": 0}
            self.load_pics()
            self.effects = []
            self.effect_dict = defaultdict(list)
            self.customer_preference_weight = defaultdict(int)
            self.matching_priority = "rank"
#            self.set_difficulty("normal")
            self.__filesdict_timestamp = datetime.datetime.now() #<Chris12 AutoRepair />

            self.cheats = False
            self.achievements = True

            self.init_mixes()
#             for mix in persistent.game_mixes:
#                 self.mixes += [gp for gp in persistent.girl_mix[mix] if gp not in self.mix]

            self.set_difficulty(persistent.last_difficulty)

            self.sorting_dict = defaultdict(str) # Stores sorting preferences for girls and items.
            # Keys include 'MC items', 'shop items', 'girls', 'girls items', 'farm', 'farm items', 'slavemarket', 'minion_merchant items', 'city_merchant items'.
            # Values are suffixed with " reverse" if sorting is reversed.

        def get_all_girls(self): # returns a list of all generated girls (for quick fixes and such)
            g_list = MC.girls + farm.girls + game.free_girls + slavemarket.girls + MC.escaped_girls
            if isinstance(enemy_general, Girl):
                g_list += [enemy_general]

            return g_list

        def sort(self, target, context):

            try:
                sorter = self.sorting_dict[context]
            except: # Initializes dict if non-existent to avoid breaking saves
                self.sorting_dict = defaultdict(str)
                return

            if sorter:
                if sorter.endswith(" reverse"):
                    target.sort(key=operator.attrgetter(sorter[:-8]), reverse=True)
                else:
                    target.sort(key=operator.attrgetter(sorter))


        def init_mixes(self):
            self.mixes = list(persistent.game_mixes)

        # Cheats

        def activate_cheats(self):
            if renpy.call_screen("yes_no", "警告. 激活作弊器将禁用此游戏的成就. 这不会影响你已经拥有的成就. 这一决定不能被逆转.\n{b}你确定要激活这个游戏的作弊器吗？{/b}"):
                self.cheats=True
                self.achievements=False
            else:
                persistent.cheats = False

        # Difficulty

        def set_difficulty(self, diff): # Where diff is a string appearing in the 'diff_list' list

            if diff in diff_list:
                self.diff = diff
                self.diff_settings = copy.deepcopy(diff_dict[diff])

                if diff == "very easy" or self.cheats:
                    self.achievements = False
                else:
                    self.achievements = True

            else:
                self.diff = "custom"
                self.diff_settings = copy.deepcopy(diff)

                self.update_achievements()

        def get_diff_setting(self, setting):
            return self.diff_settings[setting]

        def change_diff_setting(self, setting, chg):
            self.diff = "custom"

            _min = diff_settings_range[setting]["min"]
            _max = diff_settings_range[setting]["max"]

            self.diff_settings[setting] += get_change_min_max(self.diff_settings[setting], chg, _min, _max)

            self.update_achievements()

        def update_achievements(self):

            self.achievements = True

            # Disables achievements if difficulty settings are not at least equal to easy mode.
            for k, v in self.diff_settings.items():
                if k == "tax rate":
                    if v <= diff_dict["easy"][k] - 0.05:
                        self.achievements = False
                        break

                elif v > diff_dict["easy"][k]:
                    self.achievements = False
                    break
            else:
                if self.cheats:
                    self.achievements = False
                else:
                    for k, v in cheat_modifier.items():
                        if v > 1.0:
                            self.achievements = False
                            break

        # Logging game stats

        def track(self, k, v=1):
            self.track_dict[k] += v
            if k in tracked_achievements:
                test_achievements(tracked_achievements)

        def check(self, k):
            return self.track_dict[k]

        # Effects (game effects also apply in the city and affect city girls)

        def get_effect(self, type, target, randomize=True):
            return get_effect(self, type, target, randomize=randomize)

        def add_effects(self, effects, apply_boost=False, spillover=False, expires = False):
            return add_effects(self, effects, apply_boost=apply_boost, spillover=spillover, expires=expires)

        def remove_effects(self, effects):
            remove_effects(self, effects)

        def load_pics(self): # Those are the default pics for the game

            # Resetting pictures

            self.pics = []

            # Creating pictures

            for file in [f for f in renpy.list_files() if f.startswith("default/") and is_imgfile(f)]:

                file_name = file.split("/")[-1]

                pic = Picture(file_name, file)

                self.pics.append(pic)

                # Tracing untagged pics for debugging

                if pic.tags == []:
                    untagged_pics.append(pic.path)

        def start_mods(self):
            # Init active mods (mods are stored within the game object, unless they get overwritten after an update)
            for mod in detected_mods.values():
                if mod.active:
                    self.activate_mod(mod)

        def update_mods(self): # Fun fact: renpy.call breaks python blocks, but not renpy.call_screen or renpy.say

            # Will return a list of custom calls to be made (if relevant)
            update_list = []

            # Checks if a saved game's mods have been deleted or changed

            for mod in self.active_mods.values():

                if mod.name not in detected_mods.keys():
                    if renpy.call_screen("yes_no", mod.full_name + "找不到。是否要为此游戏停用此MOD（推荐）？"):
                        self.deactivate_mod(mod)

                elif mod.check_for_updates():
                    renpy.say("Mod Update", "发现不同版本的mod: %s (%s)。" % (mod.name, str(mod.version)))

                    if not hasattr(mod, "update_label"): # Fix for older games
                        mod.update_label = ""

                    if mod.update_label:
                        update_list.append(mod.update_label) # Cannot call directly or would break the python block

                    elif renpy.call_screen("yes_no", "是否为此游戏重新设置MOD（推荐）？"):
                        self.deactivate_mod(mod)
                        self.activate_mod(detected_mods[mod.name])

                elif not persistent.mods[mod.name]["active"]:
                    if renpy.call_screen("yes_no", mod.full_name + " 已停用. 是否要为此游戏停用此mod？"):
                        self.deactivate_mod(mod)

            # Checks if a new mod has been activated

            for name, mod in detected_mods.items():
                if mod.active:
                    if name not in self.active_mods.keys():
                        if renpy.call_screen("yes_no", "一个新Mod已经被激活: " + mod.full_name + ". 是否为此游戏激活此MOD？"):
                            self.activate_mod(mod)

            updated_games[self] = True # To do: Check if it works or needs a function

            return update_list

        def activate_mod(self, mod):
            self.active_mods[mod.name] = mod

            if mod.night_label:
                daily_events.append(StoryEvent(label=mod.night_label, type="night", once=False))

            renpy.notify("\n" + mod.name + " 已经被激活。")

#            renpy.say("", str(self.active_mods[mod.name]))

            if mod.init_label:
#                try:
                renpy.call_in_new_context(mod.init_label) # Suggested fix by SometimesIsNotEnough
#                except:
#                    renpy.say("System", event_color["bad"] % ("Failure to start " + mod.name) + " (calling " + mod.init_label + " label failed).")


        def deactivate_mod(self, mod):
            try:
                del self.active_mods[mod.name]
            except:
                renpy.say("System", event_color["bad"] % ("停用失败 " + mod.name))

            if mod.night_label:
                for ev in daily_events:
                    if ev.name == mod.night_label:
                        daily_events.remove(ev)

            renpy.notify("\n" + mod.name + " 已停用。")



        def has_active_mod(self, name):
            if name in self.active_mods.keys():
                return True
            return False

        def list_free_girls(self):

            l = []

            for g in self.free_girls:
                l.append(g.name)

            return "自由女孩: " + and_text(l)

        def get_available_locations(self):
            loc_list = []

            for d in district_dict.values():
                if d.rank <= district.rank:
                    loc_list += location_dict[d.name]

            return loc_list

        def get_goal_description(self, channel="advance"):

            goals = [g.get_description() for g in self.goals if g.channel == channel]

            if goals:
                if channel == "advance":
                    return "{size=-1}进入下一章, " + and_text(goals) + ".{/size}"
                else:
                    return "{size=-1}" + and_text(goals) + "{/size}"
            else:
                return ""

        def get_goals(self):

            # if self.chapter == 7:
            #     return [("Endless", "You are now in endless mode, enjoy continuing the game!")]

            # Creates a list of active channels
            active_channels = [g.channel for g in self.goals if g.channel in goal_channels]

            goal_list = []
            for channel in goal_channels:
                if channel in active_channels:
                    goal_list.append((goal_categories[channel], self.get_goal_description(channel)))

            return goal_list

        def get_first_goal(self):
            return self.get_goals()[0][1]

        def get_task(self): # Old
            if self.chapter > 2:
                return self.get_goal_description()
            else:
                return self.task

        def set_task(self, val, channel="story", max_chapter=None): # Creates a story goal to match. Overwrites previous story goal on this channel.
            # Clears previous task
            self.goals = [g for g in self.goals if g.channel != channel]

            if val: # Simply clears previous task if no value is provided
                if not max_chapter: max_chapter = self.chapter # Some uncompleted story goals may still allow progress to the next chapter
                self.goals.append(Goal("story", val, channel=channel, max_chapter=max_chapter))

        def set_goals(self, goals, channel="advance"): # Adds chapter goals (usually on the advance channel). goals must be a list of Goal objects
            # Clears previous goals
            self.goals = [g for g in self.goals if g.channel != channel]

            if goals:
                self.goals += goals

        def goals_reached(self):
            for goal in self.goals:
                if not goal.reached():
                    return False

            return True

        #<Chris12 AutoRepair>
        # If there could be new images, checks if all girls still have their portraits and profiles.
        # Does not perform any missing_girls business, use the help menu for that
        def update_files_timestamp(self):
            newFiles = None
            try :
                newFiles = self.__filesdict_timestamp != GirlFilesDict.get_timestamp()
            except :
                newFiles = True # For old savegame compatibility

            if newFiles:
                self.__filesdict_timestamp = GirlFilesDict.get_timestamp()
                for girl in (MC.girls + slavemarket.girls + game.free_girls + MC.escaped_girls + farm.girls):
                    girl.check_pictures()
        #</Chris12 AutoRepair>

        def set_max_girl_level(self): # Random girls will not generate above that level. Increases every week.
            self.max_girl_rank = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 4, 7: 5}[self.chapter]
            self.max_girl_level = {0: 1, 1: 1, 2: 5, 3: 5, 4: 10, 5: 10, 6: 15, 7: 20}[self.chapter]

        def update_max_girl_level(self): # Weekly update in random girls max level
            if self.max_girl_level < self.max_girl_rank * 5:
                self.max_girl_level += 0.5 # One level unlocks every two weeks

    class Main(object): #Attributes: name, job, god, pictures, decisions, inventory, girl inventory, character

        """This class is for the main character."""

        def __init__(self):

            self.name = MC_name
            self.level = 1
            self.prestige = 0
            self.gold = 0
            self.loan = None
            self.resources = defaultdict(int)
            self.last_collected = defaultdict(int)

            self.good = 0
            self.neutral = 0
            self.evil = 0

            self.playerclass = "Warrior"
            self.god = "Arios"
            self.reset_stats()
            self.load_pics()

            self.girls = []
            self.escaped_girls = []
            self.trainers = []
            self.current_trainer = None
            self.items = []
            self.active_inv_filter = None
            self.effects = []
            self.effect_dict = defaultdict(list)
            self.equipped = []
            self.slots = MC_inventory_slots

            self.noble = False
            self.active_spells = []
            self.known_spells = []
            self.skill_points = 0

        ## Playerclass Init ## Everywhere in the code, player class names are written with a capitalized 1st letter.

        def set_playerclass(self, playerclass): # Only call this at the start of a new game: will reset MC stats

            self.playerclass = playerclass

            self.reset_stats()

            self.load_pics()

        def set_god(self, god): # Only call this at the start of a new game: will reset MC stats

            self.god = god

            self.reset_stats()

            self.load_pics()

        def reset_stats(self):
            if self.playerclass == "Warrior":

                self.strength = 2
                self.spirit = 1
                self.charisma = 0
                self.speed = 3

            elif self.playerclass == "Wizard":

                self.strength = 0
                self.spirit = 2
                self.charisma = 1
                self.speed = 3

            elif self.playerclass == "Trader":

                self.strength = 1
                self.spirit = 0
                self.charisma = 2
                self.speed = 3

            if self.god == "Arios":
                self.strength += 1

            elif self.god == "Shalia":
                self.spirit += 1

            else:
                self.charisma += 1

            self.interactions = self.speed
            self.mana = self.spirit

        ## Load pics

        def load_pics(self):

            # Loading files

            self.files = []

            for file in renpy.list_files():

                if file.startswith("MC/"):

                    file_parts = file.split("/")
                    file_name = file_parts[-1]

                    self.files.append(file)

            # Identifying image files

            imgfiles = [img for img in self.files if is_imgfile(img)]

            # Resetting pictures

            self.pics = []

            # Creating pictures

            for file in imgfiles:

                file_name = file.split("/")[-1]

                pic = Picture(file_name, file)

                self.pics.append(pic)

            # Choosing the best match

            god_dict = {"Arios" : "light", "Shalia" : "dark", None : "neutral"}

            idx = 0

            for pic in self.pics:
                if self.playerclass.lower() in pic.filename.lower() and god_dict[self.god].lower() in pic.filename.lower():
                    idx = self.pics.index(pic)
                    break
            else:
                for pic in self.pics:
                    if self.playerclass.lower() in pic.filename.lower():
                        idx = self.pics.index(pic)
                        break

            if not self.pics:
                raise AssertionError, "没有找到主角的照片. 请检查game/MC文件夹。"
            else:
                self.current_pic = self.pics[idx]

        def load_pics_old(self):

            # Loading files

            self.files = []

            for file in renpy.list_files():

                if file.startswith("MC/"):

                    file_parts = file.split("/")
                    file_name = file_parts[-1]

                    self.files.append(file)

            # Identifying image files

            imgfiles = [img for img in self.files if is_imgfile(img)]

            # Resetting pictures

            self.pics = []

            # Creating pictures

            for file in imgfiles:

                file_name = file.split("/")[-1]

                if self.playerclass.lower() in file_name.lower():

                    pic = Picture(file_name, file)

                    self.pics.append(pic)

            if not self.pics:
                raise AssertionError, "没有找到 " + MC.playerclass + " 类的图片. 请检查game/MC文件夹。"
            else:
                self.current_pic = self.pics[0]

        def change_pic(self, direction):
            if direction == "next":
                self.current_pic = get_next(self.pics, self.current_pic, loop=True)
            elif direction == "previous":
                self.current_pic = get_previous(self.pics, self.current_pic, loop=True)

        ## Reset interactions (daily)

        def reset_interactions(self):
            self.interactions = round_int(self.get_speed() * self.get_effect("boost", "AP") + self.get_effect("change", "AP"))
            self.mana = round_int(self.get_spirit() * self.get_effect("boost", "mana") + self.get_effect("change", "mana"))

        ## Banking

        def take_loan(self, loan):
            if not self.loan:
                self.loan = loan
                self.gold += loan.amount
                return True
            return False

        def repay_loan(self):
            if self.loan:
                cost = self.loan.repay()
                if self.loan.amount <= 0: # Loan repaid
                    calendar.set_alarm(calendar.time+1, Event(label = "loan_repaid"))
                return cost
            return False

        def repay_in_full(self):
            if self.loan:
                if self.gold >= self.loan.amount:
                    if renpy.call_screen("yes_no", "你确定要全额偿还贷款 " + str(self.loan.amount) + " 金币吗？"):
                        self.gold -= self.loan.amount
                        self.loan = None
                        return True
            return False


        ## Resources

        def has_gold(self, amount):

            if self.gold >= amount:
                return True

            else:
                return False

        def gain_resource(self, resource="", number=1, message=True, random=False): # Where resource is the resource name

            if random:
                resource = rand_choice([r for r in build_resources if resource_dict[r].rank <= district.rank])
                if resource == "diamond": # can never get more than 1 diamond from a random city event
                    number=1

#            renpy.say("", "gaining " + str(resource))

            if resource == "prestige":
                self.prestige += number
            elif resource in ("gold", "money", "denar"):
                resource = "gold"
                self.gold += number
            else:
                self.resources[resource] += number

            if message:
                renpy.call("resource_gained", resource, number)
            else:
                renpy.notify("+" + str(number) + " " + resource_name_dict[resource])

        def collect_resource(self, resource): # Where resource is the resource name

#            renpy.say("", "collecting " + str(resource))

            if self.last_collected[resource] == calendar.time:
                return "KO"

            self.last_collected[resource] = calendar.time
            self.interactions -= 1

            res = resource_dict[resource]

            if res.rank == 2:
                nb = dice(3, 1 + int(self.get_stat(res.stat)/2)) # + self.get_effect("change", "basic resource extraction")
            elif res.rank == 3:
                nb = dice(2, 1 + int(self.get_stat(res.stat)/3)) # + self.get_effect("change", "advanced resource extraction")
            elif res.rank == 4:
                if renpy.random.random() <= 0.33: # 33% chance of finding diamond
                    nb = 1 # + self.get_effect("change", "diamond extraction")
                else:
                    renpy.call_screen("OK_screen", message="你没有发现任何东西。")
                    return
            else:
                return

            # The boost is generic (moon effect)
            nb += 1 * self.get_effect("boost", "resource extraction") + self.get_effect("change", resource + " extraction")

            self.gain_resource(resource, number=round_int(nb * game.get_diff_setting("resources")))

            return

        def has_resource(self, resource, amount): # Where resource is the resource name
            if resource == "gold" and self.gold < amount:
                return False
            elif resource != "gold" and self.resources[resource] < amount:
                return False
            return True

        def spend_resource(self, resource, amount):
            self.spend_resources([(resource, amount)])

        def spend_resources(self, resources): # Where resources is a list of (resource, amount) tuples

            sounds = []

            for resource, amount in resources:
                if resource == "gold":
                    sounds.append(s_gold)
                    self.gold -= amount
                else:
                    self.resources[resource] -= amount
                    sounds.append(resource_dict[resource].sound)

            if sounds:
                renpy.play(rand_choice(sounds), "sound")

        def exchange(self, source="gold", target="gold", target_amount=0):

            cost = get_exchange_rate(source, target) * target_amount

            if not self.has_resource(source, cost):
                renpy.say(market_girl, "对不起，您没有足够的 " + source + " 来支付这笔开支。")

            else:
                renpy.play(resource_dict[target].sound, "sound")
                self.resources[source] -= cost
                self.resources[target] += amount


        ## Spells

        def has_spell(self, spl):

            for s in self.known_spells + self.active_spells:

                if s.name == spl.name:

                    return s

            return False

        def has_active_spell(self, spellname = None, spelltype = None):

            if spelltype:
                for s in self.active_spells:
                    if s.type == spelltype:
                        return True

            else:
                for s in self.active_spells:
                    if s.name == spellname:
                        return True

            return False

        def has_auto_spell(self, spelltype):

            for s in self.known_spells:
                if s.auto and s.type == spelltype:
                    return True

            return False


        def update_spells(self):

            for spl in spellbook[self.playerclass]:

                if spl.level <= self.level and not self.has_spell(spl):

                    self.learn(spl)

                elif spl.level > self.level and self.has_spell(spl): # Shouldn't be needed anymore

                    self.unlearn(self.has_spell(spl))
                    renpy.pause(0.5)

            self.known_spells.sort(key=lambda x: x.get_cost())
#            renpy.say("", "Known spells =" + str(len(self.known_spells)))

        def learn(self, spl):
            if spl.type == "passive":
                self.active_spells.append(spl)
                self.add_effects(spl.effects)

                renpy.call_screen("OK_screen", title = spl.name, message = self.name + " 获得了一种新的天赋.\n\n" + spl.description, pic = spl.pic, pic_size = "small")

            else:
                self.known_spells.append(spl)
                renpy.call_screen("OK_screen", title = spl.name, message = self.name + " 学会了一种新的魔法.\n\n" + spl.description, pic = spl.pic, pic_size = "small")

            spl.auto = False

        def unlearn(self, spl): # Obsolete with 0.14

            if spl in self.active_spells:
                self.deactivate_spell(spl)

            self.known_spells.remove(spl)
            spl.auto = False

            renpy.notify("\n{color=[c_crimson]}" + self.name + "已经遗忘掉" + spl.name + "{/color}")


        def activate_spell(self, spl):

            if spl in self.active_spells:
                renpy.notify("\n这个法术已经生效。")
                return False

            elif self.has_active_spell(spelltype = spl.type):
                renpy.notify("\n另一个 " + spl.type + "法术已经生效。")
                return False

            elif self.mana >= spl.cost:

                self.mana -= spl.cost
                self.active_spells.append(spl)
                self.add_effects(spl.effects)

                renpy.play(spl.sound, channel='sound2')
                renpy.notify("\n" + spl.name + "已经生效。")
                renpy.pause(0.5)

                return True

            else:

                renpy.notify("\n你没有足够的法力来施展这个法术。")

                return False

            return

        def autocast(self, spell, _time):

            msg = ""

            if spell.auto == _time and spell not in self.active_spells:
                if self.activate_spell(spell):
                    msg = "你成功施展了法术" + spell.name + "。"
                    sound = s_spell
                else:
                    msg = "你施展法术" + spell.name + "失败。"
                    sound = s_fizzle

                renpy.play(sound, "sound")
                renpy.notify(msg)
                renpy.pause(0.5)

            return msg


        def deactivate_spell(self, spl):

            self.active_spells.remove(spl)
            self.remove_effects(spl.effects)

            renpy.notify(spl.name + "已经失效")
            renpy.pause(0.5)

            return

        def reset_spells(self):
            for spell in [s for s in self.active_spells if s.duration == "turn"]:
                MC.deactivate_spell(spell)

        def toggle_auto_spell(self, spl):

            if spl.auto == "night":
                spl.auto = "morning"

            elif spl.auto == "morning":
                spl.auto = False

            elif self.has_auto_spell(spl.type):
                renpy.notify("\n只能有一个" + spl.type + "法术可以自动施展。")

            else:
                spl.auto = "night"


        ## Leveling

        def change_prestige(self, chg, apply_boost=True):
            if apply_boost:
                chg = chg * self.get_effect("boost", "prestige") + self.get_effect("change", "prestige")

            chg *= cheat_modifier["prestige"] * game.get_diff_setting("prestige")
            self.prestige += chg

            if MC.ready_to_level():
                MC.level_up()

            game.track("had sex")

            return chg

        def ready_to_level(self):
            if self.level < 25:
                if self.prestige >= MC_xp_to_levelup[self.level]:
                    return True

            return False

        def level_up(self, forced = False):

            if (self.ready_to_level() or forced) and self.level < 25:
                self.level += 1
                self.skill_points += 1
                test_achievements(["Warrior", "Wizard", "Trader"])
                self.update_spells()
                renpy.play(s_spell, "sound")
                return True

            else:
                return False

        def change_stat(self, stat, nb, apply_boost=True, spillover=False):

            if apply_boost:
                nb = nb * self.get_effect("boost", stat + " gains") + self.get_effect("change", stat + " gains")

            if stat == "strength":
                if self.strength + nb <= 10:
                    self.strength += nb
                    return True

            elif stat == "spirit":
                if self.spirit + nb <= 10:
                    self.spirit += nb
                    return True

            elif stat == "charisma":
                if self.charisma + nb <= 10:
                    self.charisma += nb
                    return True

            elif stat == "speed":
                if self.speed + nb <= 10:
                    self.speed += nb
                    return True

            return False

        def raise_stat(self, stat, nb): # Obsolete: rename to change_stat
            return self.change_stat(stat, nb)


        ## Get methods

        def get_stat(self, statname, raw=False):
            if statname.lower() in ("strength", "defense"):
                r = self.get_defense(raw=raw)

            elif statname.lower() == "spirit":
                r = self.get_spirit(raw=raw)

            elif statname.lower() == "charisma":
                r = self.get_charisma(raw=raw)

            elif statname.lower() == "speed":
                r = self.get_speed(raw=raw)

            return r

        def get_strength(self, fight=False, raw=False):
            return self.get_defense(fight, raw)


        def get_defense(self, fight=False, raw=False): # Raw affects item boosts but not spells

            defense = self.strength

            if not raw:
                defense += self.get_effect("change", "strength") + self.get_effect("change", "defense")

            if self.get_effect("special", "dragon form") > 0:

                defense = self.get_spirit()

            if fight and self.has_active_spell(spellname = "Summon bloodhound"):
                defense += dice(6)

            return defense


        def can_defend(self):
            if self.interactions > 0 or self.get_effect("special", "defender"):
                return True
            return False

        def get_spirit(self, raw=False):

            if raw:
                return self.spirit

            spirit = self.spirit

            spirit += self.get_effect("change", "spirit")

            return spirit


        def get_charisma(self, raw=False):

            char = self.charisma

            if not raw:
                char += self.get_effect("change", "charisma")

            if self.get_effect("special", "fairy form") > 0:

                char = self.get_spirit()

            return char


        def get_speed(self, raw=False):
            if raw:
                return self.speed

            spd = self.speed

            spd += self.get_effect("change", "speed")

            return spd

        def has_girlfriend(self):
            if get_known_free_girls(3):
                return True
            return False


        # Old, should be phased out in favor of challenges

        def test_defense(self, diff):

            your_score = self.get_defense(fight = True) + dice(6)
            enemy_score = diff + dice(6)

#            renpy.say("", "Rolled " + str(your_score) + "against " + str(enemy_score))

            if your_score >= enemy_score:
                return True

            else:
                return False

        def test_spirit(self, diff):

            if (self.get_spirit() + dice(6)) >= (diff + dice(6)):
                return True

            else:
                return False

        def test_charisma(self, diff):

            if (self.get_charisma() + dice(6)) >= (diff + dice(6)):
                return True

            else:
                return False

        def get_alignment(self):
            if self.good > self.evil + 2 and self.good > self.neutral:
                return "good"
            elif self.evil > self.good + 2 and self.evil > self.neutral:
                return "evil"
            else:
                return "neutral"


        ## Items


        def get_modifier(self, operation, raw=False):

            mod = price_modifiers[operation]

            if not raw:
                mod *= self.get_effect("boost", operation)

                # Hard cap on the Haggler talent
                if operation == "buy" and mod < 0.75:
                    mod = 0.75
                elif operation == "sell" and mod > 1.25:
                    mod = 1.25

            return mod

        def buy(self, seller, obj, price):

            self.gold -= price

            self.take(seller, obj)

            if obj.type == "girl":
                game.track("gold spent slavemarket", price)
            else:
                game.track("gold spent shops", price)

            renpy.block_rollback()

        def can_sell(self, buyer, obj):
            if not hasattr(self, "sold"):
                self.sold = defaultdict(list)
            elif obj in self.sold[buyer]:
                return False
            return True

        def sell(self, buyer, obj, price = None):

            if isinstance(obj, Item):
                if not obj.type.sellable:
                    renpy.notify("\n你不能出售这个物品。")
                    return False

                if obj.equipped:
                    self.unequip(obj)

            self.gold += price

            self.give(buyer, obj)
            self.sold[buyer].append(obj)

            renpy.block_rollback()
            return True


        def take(self, giver, obj): ## I know, girls are not objects...

            if obj.type == "girl":
                acquire_girl(obj)
                try:
                    giver.girls.remove(obj)
                except:
                    pass
            else:
                self.items.append(obj)
                try:
                    giver.items.remove(obj)
                except:
                    pass

            renpy.restart_interaction()


        def give(self, taker, obj):

            if obj.type == "girl":
                if obj in self.girls:
                    self.girls.remove(obj)
                elif obj in farm.girls:
                    farm.girls.remove(obj)
                taker.girls.append(obj)

            elif not obj.type.giveable:
                renpy.notify("\n你不能给这个物品。")
                return False

            elif taker:
                if obj.equipped:
                    self.unequip(obj)
                renpy.play(obj.sound, "sound")
                self.items.remove(obj)
                taker.items.append(obj)

            renpy.restart_interaction()
            return True

        def gift(self, taker, item):

            if item.type.giveable:
                self.items.remove(item)

                renpy.say("", "你把{b}" + article(item.name) + "{/b}给了" + taker.name +"。")

                renpy.block_rollback()

                result = taker.receive_gift(item)

                return result
            else:
                renpy.notify("\n你不能给这个物品。")
                return -1

        def equip(self, item):

            for i in self.equipped:

                if i.type.slot == item.type.slot:

                    self.unequip(i)

            self.equipped.append(item)
            self.add_effects(item.effects)
            item.equipped = True

            test_achievements(["mc strength", "mc spirit", "mc charisma", "mc speed"])

        def unequip(self, item):

            self.equipped.remove(item)
            self.remove_effects(item.effects)
            item.equipped = False

#         def upgrade(self, item_name, value): # upgradeable items must be stored in

#             for it in self.items:
#                 if it.name == item_name:
#                     MC.items.remove(it)
#                     MC.items.append(upgradeable_items[item_name + " " + str(value)])


        def use_item(self, item):

            used = True
            #
            # if item.usage == "buff":
            #
            #     self.add_effects(item.effects)
            #
            #     calendar.set_alarm(calendar.time + item.charges, Event(label = "effect_expired", object = (self, item.effects)))
            #
            #     self.items.remove(item)
            #
            #
            # else:

            for e in item.effects:

                if e.type == "gain":

                    if e.target in ("prestige"):
                        e.gain(self)

                        if MC.ready_to_level():
                            MC.level_up()

                    elif e.target in ("skills", "skill points"):
                        self.skill_points += e.value

                elif e.duration > 0:
                    self.add_effects(e, expires=calendar.time + e.duration)
                    used = True

                    # calendar.set_alarm(calendar.time + e.duration, Event(label = "effect_expired", call_args = (self, e)))


            if used:

                r = item.use_me()

                if r == "used_up":
                    self.items.remove(item)

                renpy.block_rollback()

            return r

        def has_item(self, it_name):

            for it in self.items:
                if it.name.lower() == it_name.lower():
                    return True

            return False

        def get_items(self, target="any", type="any", name="any", effect_type="any", effect_target="any"): # Where 'type' is a name, not an object

            items = []

            for it in self.items:
                if it.target == target or target == "any":
                    if it.type.name == type or type == "any":
                        if name in it.name or name == "any":
                            if effect_type != "any" or effect_target != "any":
                                if it.has_effect(effect_type, effect_target):
                                        items.append(it)
                            else:
                                items.append(it)
            return items

        ## Effects

        def get_effect(self, type, target, randomize=True):
            if type == "boost":
                return get_effect(self, type, target, randomize=randomize) * brothel.get_effect(type, target, randomize=randomize)
            else:
                return get_effect(self, type, target, randomize=randomize) + brothel.get_effect(type, target, randomize=randomize)

        def add_effects(self, effects, apply_boost=False, spillover=False, expires = False):
            return add_effects(self, effects, apply_boost=apply_boost, spillover=spillover, expires=expires)

        def remove_effects(self, effects):
            remove_effects(self, effects)


        ## Misc

        def cycle_trainers(self, reverse = False):

            index = self.trainers.index(self.current_trainer)

            if not reverse:
                index += 1
                if index > len(self.trainers)-1:
                    index = 0
            else:
                index -= 1
                if index < 0:
                    index = len(self.trainers)-1

            self.current_trainer = self.trainers[index]

            update_effects()

        def rand_say(self, sentences): # MC will say a random sentence in the list

            you(rand_choice(self.filter_say(sentences)))

            return

        def say(self, sentences): # Same as rand_say, just easier to manipulate
            return self.rand_say(sentences)

        def filter_say(self, sentences): # MC may say a random sentence in the list if and only if it checks out with his attributes

            d_list = []

            for it in sentences:

                if it.startswith("wr: ") or it.startswith("wa: "):
                    if self.playerclass == "Warrior":
                        d_list.append(it[4:])

                elif it.startswith("wz: ") or it.startswith("wi: "):
                    if self.playerclass == "Wizard":
                        d_list.append(it[4:])

                elif it.startswith("tr: "):
                    if self.playerclass == "Trader":
                        d_list.append(it[4:])

                elif it.startswith("gd: "):
                    if self.get_alignment() == "good":
                        d_list.append(it[4:])

                elif it.startswith("ne: "):
                    if self.get_alignment() == "neutral":
                        d_list.append(it[4:])

                elif it.startswith("ev: "):
                    if self.get_alignment() == "evil":
                        d_list.append(it[4:])

                elif it.startswith("ar: "):
                    if self.god == "Arios":
                        d_list.append(it[4:])

                elif it.startswith("sh: "):
                    if self.god == "Shalia":
                        d_list.append(it[4:])

                elif it.startswith("ng: "):
                    if self.god == None:
                        d_list.append(it[4:])

                else:
                    d_list.append(it)

            return d_list

    #### End of Main character class ####



    class NPC(): # Attributes: name, pictures, inventory, girl inventory, character

        """This class is for NPCs: story NPCs, shopkeeper and slave master, etc."""

        def __init__(self, name = "", char=None, defense=0, trainer_portrait = None, trainer_description = None, effects = None, item_types = "all", minion_type = None):
            self.name = name
            self.girls = []
            self.items = []
            self.love = 0
            self.hate = 0
            self.defense = defense
            self.met = False
            self.banged = False
            self.raped = False
            self.flags = defaultdict(bool)
            self.trainer_portrait = trainer_portrait
            self.trainer_description = trainer_description
            self.effects = make_list(effects, Effect)
            self.updated = False
            self.last_restock = 0
            self.item_types = item_types
            self.minion_type = minion_type
            self.upgrade_level = 0
            self.stock_modifiers = {"junk" : 0, "common" : 0, "rare" : 0, "exceptional" : 0, "minion" : 0, "item" : 0}

            if char:
                self.char = char
            else:
                self.char = Character(self.name)

        def get_defense(self, fight=False):
            return self.defense

        def unlock_trainer(self):
            if self not in MC.trainers:
                MC.trainers.append(self)
                unlock_achievement("trainer " + self.name.lower())

        def can_upgrade(self):
            if self.upgrade_level + 1 in shop_upgrades.keys():
                if shop_upgrades[self.upgrade_level + 1][0] <= game.chapter:
                    return True

            return False

        def upgrade_shop(self, cost, upgrade, forced=False): # Where cost and upgrades are tuples
            if forced or MC.has_resource(*cost):
                if not forced:
                    MC.spend_resource(*cost)
                self.upgrade_level += 1
                self.stock_modifiers[upgrade[0]] += upgrade[1]
            else:
                renpy.call_screen("OK_screen", "Missing resources", "你缺少此次升级所需的资源（%s %s）。" % (cost[1], cost[0]))
                return False

        def restock(self, once_a_day=True): # For shop NPCs

            self.items = []
            all_qualities = ["junk", "common", "rare", "exceptional"]

            if self == shop:
                shop_mix = [(qual, parse_dice_formula(shop_item_number["shop"][qual]) + self.stock_modifiers[qual]) for qual in all_qualities]

            elif self in city_merchants:
                shop_mix = [(qual, parse_dice_formula(shop_item_number["city"][qual]) + self.stock_modifiers[qual]) for qual in all_qualities]

            elif self in minion_merchants:
                shop_mix = [(typ, parse_dice_formula(shop_item_number["minion"][typ]) + self.stock_modifiers[typ]) for typ in ["minion", "item"]]

            # Item merchants

            if self == shop or self in city_merchants:
                for quality, number in shop_mix:
                    if number > 0:
                        for i in xrange(number):
                            it = get_rand_item(quality, item_types=self.item_types)
                            # sanity_check = 0 #! Should not be required

                            # Completes the inventory with lower rank items if none is available
                            while not (it or quality == "junk"):
                                quality = all_qualities[all_qualities.index(quality)-1]
                                it = get_rand_item(quality, item_types=self.item_types)

                                # sanity_check += 1
                                # if sanity_check == 4:
                                #     raise AssertionError, "Failed to find any item for types %s and quality %s" % (str(self.item_types), quality)

                            if it:
                                self.items.append(it)

                if self == shop: # The shop always has at least one flower
                    self.items.append(get_rand_item("F"))

                    if story_flags["ninja hunt"]: # May include ninja-hunting devices if the story is at the right stage
                        self.items += [makibishi]*(dice(3)+1)

                self.items.sort(key=lambda x: x.price)

            # Minion merchants

            elif self in minion_merchants:
                for typ, number in shop_mix:
                    if typ == "minion":
                        self.items += get_rand_minion(self.minion_type, nb=number)
                    else:
                        for i in xrange(number):
                            self.items.append(get_rand_item(rank="M"))

                if self.flags["extractor1 unlock"]:
                    if dice(6) >= 4:
                        self.items.append(extractor_items["extractor1"])

                if self.flags["extractor2 unlock"]:
                    if dice(6) >= 5:
                        self.items.append(extractor_items["extractor2"])

            # Track update
            self.updated = True

            if once_a_day:
                self.last_restock = calendar.time



#     class City(): # Note: Free girls should be transfered here from the game object

#         """This class is for the main city of Zan."""

#         def __init__():
#             self.effects = []
#             self.effect_dict = defaultdict(list)




    class District(): # Attributes: name, populations, brothels, competitors, vice, tooltip

        """This class covers the districts of the city, where each chapter of the game is played."""

        def __init__(self, name, chapter, rank, diff, pop, room = None, pic = None, locations = None, description = ""):

            self.name = name
            self.chapter = chapter
            self.rank = rank
            self.diff = diff
            self.pic = pic
            self.description = description
            self.quests_updated = -99
            if room:
                self.room = room
            else:
                self.room = []
            if locations:
                self.locations = locations
            else:
                self.locations = []

            self.items = defaultdict(list)

            self.no_reminder = -1 # storing the latest skipped day for the 'relocate/visit city' reminder

        def get_rand_pop(self):
            return weighted_choice([(p, p.weight) for p in all_populations])

        def get_pic(self, x, y):
            return im.Scale(self.pic, x, y)


    class Population():

        def __init__(self, name, pic, diff, range, rank=1, effects=None, weight=0, base_description = ""):

            self.name = name
            self.pic = Picture(pic, "UI/customers/" + pic)
            self.diff = diff
            self.range = range
            self.rank = rank
            if effects == None: effects = []
            self.effects = effects
            self.effect_dict = defaultdict(list)
            for effect in self.effects:
                self.effect_dict[effect.type, effect.target].append(effect)
            self.weight = weight
            self.description = "{b}" + setting_name_dict[self.name.capitalize()] + "{/b} (接待难度: " + self.get_difficulty() + "): " + get_description(base_description, effects)

        def get_rand_name(self, gender="M"):
            return rand_choice(pop_name_dict[gender + " " + self.name])

        def get_average_budgets(self, description=False): # For display in the Advertising UI
            base = self.diff + self.range//2
            ent_budget = int(base * self.get_effect("boost", "job customer budget") + self.get_effect("change", "job customer budget"))
            wh_budget = int(base * 3 * self.get_effect("boost", "whore customer budget") + self.get_effect("change", "whore customer budget"))
            total_budget = ent_budget + wh_budget

            if description:
                if ent_budget != base:
                    ent_budget = event_color["good"] % str(ent_budget)

                if wh_budget != base*3:
                    wh_budget = event_color["good"] % str(wh_budget)

            return total_budget, ent_budget, wh_budget

        def get_effect(self, type, target, randomize=False): # Turn randomize off for UI display

#             if type == "boost":
#                 r = 1 * brothel.get_effect(type, target)
#             else:
#                 r = 0 + brothel.get_effect(type, target)

#             for eff in self.effects:
#                 if eff.target.lower() == target.lower():
#                     if renpy.random.random() <= eff.chance:
#                         r += eff.value
            if type == "boost":
                return get_effect(self, type, target, randomize=randomize) * brothel.get_effect(type, target, randomize=randomize)
            else:
                return get_effect(self, type, target, randomize=randomize) + brothel.get_effect(type, target, randomize=randomize)

        def get_pic(self, x, y):
            return self.pic.get(x, y)

        def get_difficulty(self):

            if self.diff <= 25:
                return event_color["good"] % str(self.diff)
            elif self.diff <= 50:
                return event_color["a little good"] % str(self.diff)
            elif self.diff <= 90:
                return event_color["average"] % str(self.diff)
            elif self.diff <= 120:
                return event_color["a little bad"] % str(self.diff)
            elif self.diff <= 170:
                return event_color["bad"] % str(self.diff)
            else:
                return event_color["fear"] % str(self.diff)


    class Customer():

        """This class is for individual customers interacting with the girls."""

        def __init__(self, pop):

            if pop:
                self.pop = pop
            else:
                self.pop = beggar

            self.rank = self.pop.rank

            self.adjective = ""

            self.randomize()

            self.name = article(self.adjective + self.pop.get_rand_name()).capitalize()

            self.reason = ""
            self.satisfaction = self.get_effect("change", "overall customer satisfaction")
            self.service_dict = {"entertained" : 0, "laid" : 0, "both" : 0, "favorite entertainment" : 0, "favorite sex act" : 0, "extra" : 0} # Extra is earned with the right trait or bis/group sex
            self.got_entertainment = None
            self.got_sex_act = None
            self.group = False

            self.gender = "M"

#             self.got_service = False
#             self.entertained = False
#             self.got_laid = False
#             self.satisfied = False

            #<Chris Job Mod>
            if game.has_active_mod("chrisjobmod"):
                self.entertainment_score = unentertained_customer_score
            #</Chris Job Mod>

        def get_pic(self, x, y):
            return self.pop.get_pic(x, y)

        def receive_entertainment(self, entertainment):

            self.got_entertainment = entertainment
            self.service_dict["entertained"] = 1

            if entertainment == self.wants_entertainment:
                self.service_dict["favorite entertainment"] = 1

        def receive_sex_act(self, act):

            self.got_sex_act = act
            self.service_dict["laid"] = 1

            if act == self.wants_sex_act:
                self.service_dict["favorite sex act"] = 1

            if self.service_dict["entertained"] > 0:
                self.service_dict["both"] = 1

        def get_entertainment_bonus(self):
            r = self.get_effect("change", "job satisfaction") + self.get_effect("change", "satisfaction")

            if self.wants_entertainment != self.got_entertainment:
                return r - self.rank
            else:
                return r

        def get_sex_act_bonus(self, bis=False, group=False):
            r = self.get_effect("change", "whore satisfaction") + self.get_effect("change", "satisfaction")

            # Customers that haven't been entertained first get an additional penalty
            if not self.got_entertainment:
                r -= self.rank - 1

            # Customers will not complain about the sex act during group or bisexual
            if bis or group:
                self.service_dict["extra"] = 1
            elif self.wants_sex_act != self.got_sex_act:
                r -= self.rank - 1

            return r

        def get_reputation_change(self): # Returns change to brothel reputation at the end of the day

            # Rating will bring a positive change to rep if >= rank, will bring negative change if < rank-1
            self.base_rating = sum(v for v in self.service_dict.values())
            rating = self.base_rating + 1 - self.rank

            chg = min(2 ** self.rank, 2 ** rating - 1)

            if chg < 0:
                chg = 1 - 2 ** (-rating)

            self.reputation_change = chg
            self.reputation_comment = self.get_reputation_comment(chg)

            return chg

        def get_reputation_comment(self, chg):

            # Get random comment

            if self.base_rating == 0:
                comment = rand_choice(["我来这里是为了什么。", "我根本就没有参加。", "多么可耻的事情. 我在这里浪费了很多时间。", "没有人听我的. 浪费时间..。"])

                if chg < 0:
                    comment = event_color["bad"] % comment

            elif self.base_rating == 8:
                comment = event_color["special"] % rand_choice(["我度过了一生中最美好的时光。", "一切都是那么完美。", "有史以来最棒的夜晚! 我已经筋疲力尽了。", "这地方太神奇了. 五星级！"])

            else:
                pos_comments = []
                neg_comments = []

                if self.service_dict["entertained"] >= 2:
                    pos_comments.append("我看到了一个非常棒的表演。")
                elif self.service_dict["entertained"] == 1:
                    pos_comments += ["我得到一些娱乐。", "我在等待中得到了乐趣。", "一个女孩为我表演。"]
                    neg_comments.append("演艺人员可以做得更好一些。")
                else:
                    neg_comments += ["没有什么娱乐活动。", "我在等待时感到很无聊。", "没有娱乐. 烦人..。"]

                if self.service_dict["laid"] >= 2:
                    pos_comments.append("性爱真的很赞。")
                elif self.service_dict["laid"] == 1:
                    pos_comments += ["我有了新欢。", "一个妓女照顾了我。", "我有%s。" % self.got_sex_act]
                    neg_comments.append("性服务可以做得更好一些。")
                else:
                    neg_comments += ["没有妓女! 这是什么样的青楼？", "我找不到一个妓女. 太令人沮丧了。", "不能上床，该死！", "妓女们在哪里？人呢？"]

                if self.service_dict["both"] > 1:
                    pos_comments.append("我同时得到了性和娱乐。")

                if self.service_dict["favorite entertainment"] >= 1:
                    pos_comments.append("我在等待时得到了我最喜欢的娱乐。")
                else:
                    neg_comments.append("没有我最喜欢的娱乐活动。")

                if self.service_dict["favorite sex act"] > 1:
                    pos_comments.append("我得到了我最喜欢的性行为。")
                else:
                    neg_comments.append("没有我最喜欢的性行为。")

                if self.service_dict["extra"] > 1:
                    pos_comments.append("人多的时候，性爱会更精彩！")

                if chg > 0:
                    comment = event_color["good"] % rand_choice(pos_comments)
                elif chg < 0:
                    comment = event_color["bad"] % rand_choice(neg_comments)
                else:
                    comment = rand_choice(pos_comments+neg_comments)

            return comment


        def randomize(self):

            self.preference = weighted_choice([("beauty", 25 + self.get_effect("change", "beauty preference")), ("body", 25 + self.get_effect("change", "body preference")), ("charm", 25 + self.get_effect("change", "charm preference")), ("refinement", 25 + self.get_effect("change", "refinement preference"))])
            self.wants_entertainment = weighted_choice([(j, customer_base_preference[j]*(1 + 0.5*game.customer_preference_weight[j]) + self.get_effect("change", j + " preference")) for j in all_jobs])
            self.wants_sex_act = weighted_choice([(a, customer_base_preference[a]*(1 + 0.5*game.customer_preference_weight[a]) + self.get_effect("change", a + " preference")) for a in all_sex_acts])
            self.fetish = rand_choice(trait_dict.keys())

            self.diff = self.pop.diff + dice(self.pop.range + 1) - 1 ## Varies up to +10 to +40 (maximum rank)
            self.defense = 2 * (self.rank-2) + dice(self.rank+2) # from -1 to 13 defense depending on rank

            self.set_budgets()

            if dice(100) <= 2 * self.get_effect("boost", "crazy") + self.get_effect("change", "crazy"):
                self.crazy = rand_choice(["arsonist", "rapist", "violent"])
            else:
                self.crazy = False

        def get_defense(self, fight = False):
            return self.defense * self.get_effect("boost", "customer defense") + self.get_effect("change", "customer defense")

        def get_effect(self, type, target, randomize=True): # Keep randomize True so that random customer effects will proc
            return self.pop.get_effect(type, target, randomize)

        def get_description(self, act="idle"):

            pronoun = {"M": "他", "F": "她"}[self.gender]

            desc = ""

            if self.crazy:
                crz_text = "{color=" + c_red + "}%s疯狂般闯了{/color}" % pronoun
            else:
                crz_text = ""

            if act == "idle":
                return self.name + "%s进来青楼。%s希望得到一个{b}%s{/b}和喜欢{b}%s{/b}的人的招待。%s更喜欢%s的女孩。" % (crz_text, pronoun, girl_related_dict[self.wants_entertainment], girl_related_dict[self.wants_sex_act], pronoun, self.fetish.lower())

            elif act in all_jobs:
                desc += self.name + "%s进来青楼。\n%s希望得到一个{b}%s{/b}的娱乐。" % (crz_text, pronoun, girl_related_dict[self.wants_entertainment])
                if self.wants_entertainment != act:
                    desc += "，但最终还是选择了一个{b}%s{/b}" % girl_related_dict[act]
                return desc

            elif act in all_sex_acts:
                desc += self.name + "来的是{b}%s{/b}" % girl_related_dict[self.wants_sex_act]
                if self.wants_sex_act != act:
                    desc += ", 但却选择了{b}%s{/b}" % girl_related_dict[act]
                if self.group:
                    desc += (". %s加入了一个叫{color=" + c_purple + "}{b}%s的队伍{/b}{/color}") % (pronoun, self.group)
                return desc + "。" + crz_text

            elif act == "end":
                desc += self.name + "希望能得到一个{b}%s{/b}女孩的招待，" % girl_related_dict[self.wants_entertainment]
                if self.got_entertainment:
                    desc += "最终得到{b}%s{/b}。" % girl_related_dict[self.got_entertainment]
                else:
                    desc += "但却无人问津。"

                desc += "%s想要{b}%s{/b}，" % (pronoun, girl_related_dict[self.wants_sex_act])
                if self.got_sex_act:
                    desc += "最终得到{b}%s{/b}。" % girl_related_dict[self.got_sex_act]
                else:
                    desc += "但没有妓女可用。"

                return desc

        def set_budgets(self):
            d = dice(12)
            mod = 1.0

            if d == 12:
                self.adjective = "富有的"
                mod = 2.0
            elif d == 1:
                self.adjective = "贫穷的"
                mod = 0.5

            self.ent_budget = int((self.diff * mod  + self.get_effect("change", "job customer budget")) * self.get_effect("boost", "job customer budget") * brothel.get_adv_budget())
            self.wh_budget = int((self.diff * 3 * mod + self.get_effect("change", "whore customer budget")) * self.get_effect("boost", "whore customer budget") * brothel.get_adv_budget())

        def choose_girl(self, girls): # For xxx interactions: returns a girl and a reason for choosing her.

            chosen = None
            best_score = 0
            sex_act = self.wants_sex_act

            # Sanity check

            if not girls:
                raise AssertionError, "顾客无法找到可供选择的女孩。(%s)" % and_text([g.name for g in girls])

#             girls = [g for g in girls if g.does_anything()]

#             if not girls:
#                 raise AssertionError, "Customer could not find girls with an active sex act to choose from. (%s)" % and_text([g.name for g in girls])

            # Looks for the best girl

            for girl in girls:

                girl_score = 0
                reason = ""

                # 1. The customer looks for a particular trait (his fetish)

                if girl.has_trait(self.fetish):
                    girl_score += 250

                    if trait_dict[self.fetish].verb == "be":
                        reason = ":cust:来寻找一个" + self.fetish + "的女孩。:Pron::verb:欣喜遇见了:girl:。"
                    elif trait_dict[self.fetish].verb == "be a":
                        reason = ":cust:来寻找一个" + self.fetish + "。:Pron::verb:欣喜遇见了:girl:。"
                    elif trait_dict[self.fetish].verb == "have":
                        reason = ":cust:来寻找一个有" + self.fetish + "的女孩。:Pron::verb:欣喜遇见了:girl:。"
                    elif trait_dict[self.fetish].verb == "have a":
                        reason = ":cust:来寻找一个有" + self.fetish + "的女孩。:Pron::verb:欣喜遇见了:girl:。"

                # 2. The customer looks for a particular stat

                girl_score += girl.get_stat(self.preference) # Customers are looking for one stat in particular

                if not reason:
                    reason = ":cust:想找" + gstats_descript[self.preference] + "。"

                    if girl_score >= 50*self.rank:
                        reason += ":Pron::verb:欣喜遇见了:girl:。"
                    elif girl_score >= 35*self.rank:
                        reason += ":Pron::verb:欣然接受了:girl:。"
                    elif girl_score >= 20*self.rank:
                        reason += ":Pron:平静接受了:girl:。" # Special case handled with a try / except clause within the perform method
                    else:
                        reason += ":Pron::verb:失望遇到了:girl:。"

                # 3. The customer looks for the best performer

                if girl.does[self.wants_sex_act]:
                    girl_score += girl.get_stat(self.wants_sex_act)

                if girl.rank < self.rank: # Customers will favor girls with their rank or higher
                    girl_score -= 100 * (self.rank - girl.rank)
                elif self.rank < girl.rank:
                    girl_score -= 50 * (girl.rank - self.rank)

                # 4. Check score

                if girl_score > best_score:
                    chosen = girl
                    best_score = girl_score
                    self.reason = reason

                    if girl.does[self.wants_sex_act]:
                        sex_act = self.wants_sex_act
                    else:
                        sex_act = rand_choice([act for act in all_sex_acts if girl.does[act] == True])

            # Choose a random girl if no-one matches their tastes

            if not chosen:
                chosen = rand_choice(girls)
                if chosen.does[self.wants_sex_act]:
                    sex_act = self.wants_sex_act
                else:
                    sex_act = rand_choice([act for act in all_sex_acts if chosen.does[act] == True])
            if not self.reason:
                self.reason = ":cust:想找" + gstats_descript[self.preference] + "。:Pron:找不到合适的女孩。"

            return chosen, sex_act

#         def get_rep_change_old(self):
#             chg = 1 - self.rank

#             if self.got_entertainment:
#                 chg += 1
#                 if self.got_entertainment == self.wants_entertainment:
#                     chg += 1
#             if self.got_sex_act:
#                 chg += 1
#                 if self.got_sex_act == self.wants_sex_act:
#                     chg += 1

#             return chg



    ## The code for brothels and room is messy / redundant and should be cleaned up some time

    class Brothel(): #Attributes: name, rooms, reputation, advertisement, tooltip

        """This class is for available brothels that you can operate."""

        def __init__(self, rank, level, upgrades, max_rep, max_help):

            self.name = "The Rose Garden"
            self.rank = rank
            self.level = level
            self.cost = bro_cost[self.level]
            self.total_value = self.cost
            self.bedroom_type = room_dict[upgrades[0]]
            self.maxupgrade = upgrades[1]
            self.max_rep = max_rep
            self.max_help = max_help
            self.furniture = []
            self.rooms = {k: copy.copy(v) for k, v in common_room_dict.items()}
            self.effect_dict = defaultdict(list)

        # Set up Brothel

        def get_pic(self, x, y):
            return ProportionalScale("brothels/" + brothel_pics[self.pic_index], x, y)

        def setup(self, name, furniture=None, current_building=None, started_building=0, master_bedroom_girls=None, free_room=None): # Happens on a new chapter, and can be used anytime you need to reset the Brothel to 'factory settings'

            self.pic_index = self.level
            self.pic = self.get_pic(config.screen_width, int(config.screen_height*0.8))
            # Unlocks pics for gallery
            unlock_pic("brothels/" + brothel_pics[self.pic_index])
            unlock_pic(self.bedroom_type.pic_path)

            self.rep = 0
            self.advertising = 0
            self.advertising_setting = 0 # advertising_setting is a value from -2 to +2. -2 is max customer attraction, 0 is balanced, +2 is max customer budget

            self.maintenance = 0
#             self.maint_value = 1 # maint_value is antiquated
            self.dirt = 0

            self.security = 0
            self.threat = 0 # Threat builds up over time and causes security events to proc
            self.alert_level = 1 # Alert level determines the type of security events that can proc

            self.free_room = False
            if free_room:
                if free_room == "free":
                    self.free_room = True
                else:
                    for room in free_room:
                        self.rooms[room].buy(forced=True)

            self.bedrooms = bro_capacity[self.level][0]

            self.magic_shield = False

            self.name = name
            if furniture == None: furniture = []
            self.furniture = furniture
            self.current_building = current_building
            self.started_building = started_building

            self.master_bedroom = master_bedrooms[self.rank-1]
            if master_bedroom_girls == None:
                master_bedroom_girls = []
            elif len(master_bedroom_girls) > self.master_bedroom.level:
                master_bedroom_girls = master_bedroom_girls[:self.master_bedroom.level]
            self.master_bedroom.girls = master_bedroom_girls

            self.contract_modifier = -20

            self.customer_count = 0


        def get_maxbedrooms(self): # Replaces the old 'maxbedrooms' property
            return bro_capacity[game.chapter][1]

        def can_upgrade(self):
            if brothel.bedrooms < brothel.get_maxbedrooms():
                return True
            if self.bedroom_type.level < self.maxupgrade:
                return True
            if self.master_bedroom.level < self.rank:
                return True
            for room in self.rooms.values():
                if room.level < district.rank:
                    return True
            return False


        # Master bedroom
        #主卧室

        def upgrade_master_bedroom(self, target_level="auto"):
            if target_level == "auto":
                target_level = self.master_bedroom.level + 1

            if MC.has_gold(master_bedrooms[target_level].cost):
                if renpy.call_screen("yes_no", "你确定为升级主人房而花费 " + str(master_bedrooms[target_level].cost) + " 金币吗？"):
                    renpy.play(s_gold, "sound")
                    MC.gold -= master_bedrooms[target_level].cost
                    self.total_value += master_bedrooms[target_level].cost
                    temp_girls = self.master_bedroom.girls
                    self.master_bedroom.girls = []

                    self.master_bedroom = master_bedrooms[target_level]

                    self.master_bedroom.girls = temp_girls

#                     test_achievement("upgrades")

            else:
                renpy.say(sill, "对不起，主人，您没有足够的钱。")


        def can_have(self, job):
            if job == "farm":
                return False
            elif job not in all_jobs:
                return True
            elif self.rooms[job_room_dict[job.lower()]].level > 0:
                return True
            else:
                return False

        # Furniture
        #家具

        def can_build_anything(self, max_chapter=7):
            if [f for f in all_furniture if f.can_build() and f.chapter <= max_chapter]:
                return True
            return False

        def buy_furniture(self, furn):

            if self.current_building:
                renpy.say(carpenter, "对不起，老板，你需要的" + self.current_building.name + "还没有建好。")
                return False

            elif not furn.can_build():
                if furn.built:
                    renpy.say(carpenter, "你已经有了。我不认为你需要第二个。")
                renpy.say(carpenter, "目前还无法建造。我觉得你可能需要一个更大的地方。")
                return False

            for resource, amount in furn.cost:
                if not MC.has_resource(resource, amount):
                    renpy.say(carpenter, "听着，老板，在我开始工作之前你必须有足够的资源。")
                    break
            else:
                renpy.say(carpenter, "好的，看样子你已经拿到材料了，交给我。我马上就为'" + furn.name + "'开始准备。")
                if renpy.call_screen("yes_no", "您确定要为修'" + furn.name + "'而花费" + furn.describe_cost() + "吗？"):
                    MC.spend_resources(furn.cost)
                    renpy.block_rollback()
                    furn.start_building()
                    return True
            return False

        def activate_furniture(self, furn):
            return furn.activate()

        def deactivate_furniture(self, furn):
            return furn.deactivate()

        def toggle_furniture(self, furn):
            return furn.toggle()

        def destroy_furniture(self, furn):
            furn.destroy()


        # Effects

        def get_effect(self, type, target, randomize=True):

            return get_effect(self, type, target, randomize=randomize)

        def update_effects(self):

            update_effects()


        ## Important: Security, advertising and maintenance change effects are applied BEFORE boost effects

        def get_security(self):

            return ((self.security + self.get_effect("change", "security")) * self.get_effect("boost", "security"))


        # Advertising

        def update_customer_count(self): # customer count is not refreshed constantly to avoid UI lag
            self.avoid_no_population()
            self.customer_count, self.customer_count_dict = count_customers(self.rep, randomize=False)
            self.calculate_average_customer_budget()

        def avoid_no_population(self): # sanity check
            for pop in all_populations:
                if pop.weight > 0:
                    return
            all_populations[0].weight = 1

        def calculate_average_customer_budget(self):

            # Calculate average budget for active populations

            self.customer_budget_dict = defaultdict(int)
            total_ent = 0
            total_wh = 0
            weight = 0

            for pop in all_populations:
                total_budget, ent_budget, wh_budget = pop.get_average_budgets()
                total_ent += self.customer_count_dict[pop.name] * ent_budget
                total_wh += self.customer_count_dict[pop.name] * wh_budget
                weight += self.customer_count_dict[pop.name]

            if weight > 0:
                self.customer_budget_dict["ent budget"] = round_int(total_ent / weight)
                self.customer_budget_dict["wh budget"] = round_int(total_wh / weight)

            # Calculates advertising bonus

            self.customer_budget_dict["ent advertising"] = self.customer_budget_dict["ent budget"] * (brothel.get_adv_budget() - 1)
            self.customer_budget_dict["wh advertising"] = self.customer_budget_dict["wh budget"] * (brothel.get_adv_budget() - 1)

            self.customer_budget_dict["ent budget"] += self.customer_budget_dict["ent advertising"]
            self.customer_budget_dict["wh budget"] += self.customer_budget_dict["wh advertising"]

            # Calculates act bonus (for whoring-only unless BKsettings.rpy has been edited)

            act_boost = 0
            weight = 0

            for job in all_jobs:
                act_boost += tip_act_modifier[job] * (1 + 0.5*game.customer_preference_weight[job])
                weight += 1 + 0.5*game.customer_preference_weight[job]

            if weight > 0:
                self.customer_budget_dict["ent acts"] = round_int(self.customer_budget_dict["ent budget"] * (act_boost/weight - 1))

            act_boost = 0
            weight = 0

            for act in all_sex_acts:
                act_boost += tip_act_modifier[act] * (1 + 0.5*game.customer_preference_weight[act])
                weight += 1 + 0.5*game.customer_preference_weight[act]

            if weight > 0:
                self.customer_budget_dict["wh acts"] = round_int(self.customer_budget_dict["wh budget"] * (act_boost/weight - 1))

            self.customer_budget_dict["ent budget"] += self.customer_budget_dict["ent acts"]
            self.customer_budget_dict["wh budget"] += self.customer_budget_dict["wh acts"]


        def count_budget_description(self):
            try:
                base_ent_budget = self.customer_budget_dict["ent budget"] - self.customer_budget_dict["ent advertising"] - self.customer_budget_dict["ent acts"]
                base_wh_budget = self.customer_budget_dict["wh budget"] - self.customer_budget_dict["wh advertising"] - self.customer_budget_dict["wh acts"]
            except:
                self.calculate_average_customer_budget()
                base_ent_budget = self.customer_budget_dict["ent budget"] - self.customer_budget_dict["ent advertising"] - self.customer_budget_dict["ent acts"]
                base_wh_budget = self.customer_budget_dict["wh budget"] - self.customer_budget_dict["wh advertising"] - self.customer_budget_dict["wh acts"]

            # Entertainment budget description
            #娱乐预算说明

            des = "你的顾客的平均{b}娱乐的预算{/b}估计约为{b}%s金币{/b}。" % int(self.customer_budget_dict["ent budget"])

            if self.customer_budget_dict["ent budget"] != base_ent_budget:
                des += "\n("
                if self.customer_budget_dict["ent advertising"]:
                    des += event_color["good"] % ("+%s 来自广告吸引" % int(self.customer_budget_dict["ent advertising"]))
                    if self.customer_budget_dict["ent acts"]:
                        des += ", "
                if self.customer_budget_dict["ent acts"] > 0:
                    des += event_color["good"] % ("+%s 来自工作奖金" % int(self.customer_budget_dict["ent acts"]))
                elif self.customer_budget_dict["ent acts"] < 0:
                    des += event_color["bad"] % ("%s 来自工作奖金" % int(self.customer_budget_dict["ent acts"]))
                des += ")"

            des += "\n"

            # Whoring budget description
            #嫖娼预算说明

            des += "\n你的顾客的平均{b}嫖娼的预算{/b}估计约为{b}%s金币{/b}。" % int(self.customer_budget_dict["wh budget"])

            if self.customer_budget_dict["wh budget"] != base_wh_budget:
                des += "\n("
                if self.customer_budget_dict["wh advertising"]:
                    des += event_color["good"] % ("+%s 来自广告吸引" % int(self.customer_budget_dict["wh advertising"]))
                    if self.customer_budget_dict["wh acts"]:
                        des += ", "
                if self.customer_budget_dict["wh acts"] > 0:
                    des += event_color["good"] % ("+%s 来自性行为" % int(self.customer_budget_dict["wh acts"]))
                elif self.customer_budget_dict["wh acts"] < 0:
                    des += event_color["bad"] % ("%s 来自性行为" % int(self.customer_budget_dict["wh acts"]))
                des += ")"

            des += ""

            return des

        def count_customers_description(self, short=False):

            # cust_nb, adv_cust_nb, girl_cust_nb = self.customer_count, self.cust_nb_dict["advertising"], self.cust_nb_dict["special"]
            try:
                base_cust_nb = self.customer_count - self.customer_count_dict["advertising"] - self.customer_count_dict["special"]
            except:
                self.update_customer_count()
                base_cust_nb = self.customer_count - self.customer_count_dict["advertising"] - self.customer_count_dict["special"]

            if short:
                des = "{b}%s 位顾客{/b}的期望" % self.customer_count
            else:
                des = "{b}%s 位顾客{/b}预计今晚会来青楼" % self.customer_count

            if self.customer_count != base_cust_nb:
                des += "\n("

                if self.customer_count_dict["advertising"]:
                    if short:
                        des += event_color["good"] % ("广告: +%s" % str_int(self.customer_count_dict["advertising"]))
                    else:
                        des += event_color["good"] % ("+" + str_int(self.customer_count_dict["advertising"]) + " 来自广告吸引")
                    if self.customer_count_dict["special"]:
                        des += ", "
                if self.customer_count_dict["special"]:
                    if short:
                        des += event_color["good"] % ("其他: +%s" % str_int(self.customer_count_dict["special"]))
                    else:
                        des += event_color["good"] % ("+" + str_int(self.customer_count_dict["special"]) + " 来自女孩和青楼的影响")

                des += ")"

            return des # + "."

        def get_advertising(self, boost=True):

            r = self.advertising + self.get_effect("change", "advertising")

            if boost:
                return r * self.get_effect("boost", "advertising")
            else:
                return r

        def get_adv_reputation(self):
            return self.get_advertising() * advertising_settings[self.get_effect("special", "advertising power")]["reputation"]  * (1 - reputation_decay[game.chapter])

        def get_adv_setting(self, target):
            adv_lvl = self.get_effect("special", "advertising power")

            if target == "attraction":

                if self.advertising_setting == 0: # 0 is the neutral setting
                    r = advertising_settings[adv_lvl]["customer attraction"]

                # Custom advertising setting

                elif self.advertising_setting == 2: # 2 is the min setting
                    r = advertising_settings[adv_lvl]["min customer attraction"]
                elif self.advertising_setting == 1: # 1 is the low setting
                    r = (advertising_settings[adv_lvl]["customer attraction"] + advertising_settings[adv_lvl]["min customer attraction"]) / 2
                elif self.advertising_setting == -1: # -1 is the high setting
                    r = (advertising_settings[adv_lvl]["customer attraction"] + advertising_settings[adv_lvl]["max customer attraction"]) / 2
                elif self.advertising_setting == -2: # -2 is the max setting
                    r = advertising_settings[adv_lvl]["max customer attraction"]

            elif target == "budget":
                r = 1.0

                # Neutral advertising setting
                if self.advertising_setting == 0: # 0 is the neutral setting
                    r += advertising_settings[adv_lvl]["customer budget"]

                # Custom advertising setting

                elif self.advertising_setting == -2: # -2 is the min setting
                    r += advertising_settings[adv_lvl]["min customer budget"]
                elif self.advertising_setting == -1: # -1 is the low setting
                    r += (advertising_settings[adv_lvl]["customer budget"] + advertising_settings[adv_lvl]["min customer budget"]) / 2
                elif self.advertising_setting == 1: # 1 is the high setting
                    r += (advertising_settings[adv_lvl]["customer budget"] + advertising_settings[adv_lvl]["max customer budget"]) / 2
                elif self.advertising_setting == 2: # 2 is the max setting
                    r += advertising_settings[adv_lvl]["max customer budget"]

            return r

        def get_adv_attraction(self):

            # Customer attraction boost is proportional to advertising
            return self.get_adv_setting("attraction") * self.get_advertising()

        def get_adv_budget(self):

            # Customer budget boost is proportional to advertising/max_advertising ratio
            # Budget setting is expressed as a percentage increase to base budget, so we add 100% (same as 'boost' effects)
            return 1.0 + (self.get_adv_setting("budget") * self.get_advertising() / self.max_help)


        # Maintenance

        def get_maintenance(self):

            return (self.maintenance + self.get_effect("change", "maintenance")) * self.get_effect("boost", "maintenance")


        ## Brothel Threat

        def get_gold_threat(self):

            gt = (MC.gold - self.get_effect("special", "safe")) / gold_threat_amount[district.rank]

            if gt > gold_threat_max[game.chapter]:
                return gold_threat_max[game.chapter]
            else:
                return gt

        def get_threat(self): # Threat is influenced by district rank, gold (up to a maximum) and the number of working girls

            threat = district.rank + self.get_gold_threat() + sum(girl.rank/2.0 for girl in MC.girls if girl.works_today())

            return threat * self.get_effect("boost", "threat") + self.get_effect("change", "threat")

        def get_risk(self):
#            threat = self.get_threat()
#            defense = self.get_security() + MC.get_defense() MC defense no longer helps with security, but it matters during actual events

            return self.get_threat() - self.get_security()

        def estimate_threat_level(self, contrast=False):

            risk = self.get_risk()

            if risk >= 10:

                level = event_color["bad"] % "{b}非常高{/b}"

            elif risk >= 5:
                if contrast:
                    level = event_color["a little bad contrast"] % "{b}高{/b}"
                else:
                    level = event_color["a little bad"] % "{b}高{/b}"

            elif risk <= -10:

                level = event_color["good"] % "{b}非常低{/b}"

            elif risk <= -5:

                level = event_color["a little good"] % "{b}低{/b}"

            else:
                if contrast:
                    level = event_color["normal contrast"] % "{b}一般{/b}"
                else:
                    level = event_color["normal"] % "{b}一般{/b}"

            return level

        def threat_build_up(self): # Builds up threat every turn depending on active security, with a minimum of 1. Returns True if security event can proc.

            if self.get_risk() < 1:
                self.threat += 1 * self.get_effect("boost", "threat build up")
            else:
                self.threat += self.get_risk() * self.get_effect("boost", "threat build up")

            if self.threat >= 50 and self.alert_level == 3:
                return True
            elif self.threat >= 25 and self.alert_level == 2:
                return True
            elif self.threat >= 10 and self.alert_level == 1:
                return True

            return False


        def get_ASM_report(self, short=False):

            cust, extra = self.customer_count, self.customer_count_dict["special"]
            msg = ""

            if short:
                msg += "{b}广告报告{/b}: " + brothel.count_customers_description(short=True)

                msg += "\n{b}安全问题{/b}: 当前的危险等级是 " + self.estimate_threat_level(contrast=False) + ""

                msg += "\n{b}维护报告{/b}: " + maintenance_desc[self.get_cleanliness()]

            else:
                msg += "广告报告: " + brothel.count_customers_description()

#                 if extra:
#                     msg += " (including " + str_int(extra) + " from girl or brothel effects)"

                msg += ".\n安全报告: 你青楼当前的危险等级是 " + self.estimate_threat_level(contrast=True) + ""

                msg += "\n维修报告: " + maintenance_desc[self.get_cleanliness()]

            return msg


        def change_rep_nightly(self, chg):
            return self.change_rep(chg, raw=False)

        def change_rep(self, chg, raw=True): # Boost and change effects are only applied once nightly

            if not raw:
                chg = chg * reverse_if(self.get_effect("boost", "brothel reputation"), chg) + self.get_effect("change", "brothel reputation")

            chg = get_change_min_max(self.rep, chg, 0, self.max_rep)
            self.rep += chg

            return chg


        # ROOMS

        def upgrade_bedrooms(self):

            price = self.get_room_upgrade_price(self.bedrooms)

            text1 = "你确定为升级卧室而花费 " + str(price) + " 金币吗？"

            if self.bedroom_type.level < self.maxupgrade:

                if renpy.call_screen("yes_no", text1):

                    if MC.has_gold(price):

                        MC.gold -= price
                        self.total_value += price

                        self.bedroom_type = room_dict[self.bedroom_type.level+1]
                        unlock_pic(self.bedroom_type.pic_path)

#                         test_achievement("upgrades")

                        renpy.block_rollback()

                        renpy.restart_interaction()

                    else:
                        renpy.say(narrator, "你没有足够的钱。")

            else:
                renpy.say(sill, "你不能进一步升级这个青楼的房间。")

        def get_mood_modifier(self, rank): #Increases with bedroom type: Girls score higher with customers and their mood improves

            mood_modifier = self.bedroom_type.level + self.get_effect("change", "mood modifier") - (rank * 2)

            return mood_modifier


        def get_room_price(self, room = "bedroom"):

            if room == "bedroom":
                price = (100 * self.bedrooms)

                for lvl in range(self.bedroom_type.level):

                    price += 50 * lvl

                price *= district.rank #! Increased bedroom price

            else:
                if brothel_firstvisit or self.free_room:
                    price = 0
                else:
                    price = sum(room.level for room in self.rooms.values()) * (50 + 150*1.5**(game.chapter-1)) # (sum(room.level for room in self.rooms.values()) - 1) * (50 + 150*1.5**(game.chapter-1))

            return round_int(price)

        def get_room_upgrade_price(self, nb = 1):

            # This is the cost per bedroom
            price = 50 * self.bedroom_type.level * district.rank #! Increased room upgrade price

            return price * nb


        def add_room(self, room = "bedroom", forced=False):

            if room == "bedroom":

                price = self.get_room_price()

                text1 = "你想买一间新卧室而为此花费 " + str(price) + " 金币吗？"

                if self.bedrooms < self.get_maxbedrooms():

                    if renpy.call_screen("yes_no", text1):

                        if MC.has_gold(price):

                            MC.gold -= price
                            self.total_value += price

                            self.bedrooms += 1

                            test_achievement("upgrades")

                            renpy.block_rollback()

                            renpy.restart_interaction()

                            return True

                        else:
                            renpy.say(narrator, "你没有足够的钱。")
                            return False
                else:
                    renpy.say(sill, "你已经有了这个青楼的最大卧室数量。")
                    return False

            else:
                self.rooms[room].buy(forced)
#                 test_achievement("upgrades")

        def upgrade_room(self, room):
            self.rooms[room].upgrade()
#             test_achievement("upgrades")

        def has_room(self, room = "any"):

            if room == "bedroom":
                return True

            elif room != "any":

                if self.rooms[room.lower()].level > 0:
                    return True

                else:
                    return False

            else:
                if self.get_common_rooms():
                    return True
                return False

        def get_common_rooms(self):
            return [room for room in self.rooms.values() if room.level >0]

        def get_bedroom_pic(self, x, y):
            return self.bedroom_type.get_pic(x, y)

        def get_room_pic(self, type, x, y):
            if type == "bedroom":
                return self.get_bedroom_pic(x, y)
            elif type.lower() == "tavern":
                return tavern.get_pic(x, y)
            elif type.lower() in ("club", "strip club"):
                return club.get_pic(x, y)
            elif type.lower() == "onsen":
                return onsen.get_pic(x, y)
            elif type.lower() == "okiya":
                return okiya.get_pic(x, y)

        def get_random_room_pic_path(self, show_dirt=True):
            room = rand_choice(self.get_common_rooms()).pic_path[:-5]

            if show_dirt:
                room += {"clean" : "", "clean enough" : "", "dusty" : "_dusty", "dirty" : "_dirty", "disgusting" : "_verydirty", "fire" : "_verydirty"}[self.get_cleanliness()]

            return room + ".webp"


        def get_adv_cost(self):

            return self.advertising * helper_cost[district.rank]

        def get_sec_cost(self):

            return self.security * helper_cost[district.rank]

        def get_maintenance_cost(self):

            return self.maintenance * helper_cost[district.rank]

        def change_dirt(self, nb):

            boost = self.get_effect("boost", "dirt")

            boost = reverse_if(boost, nb)

            nb *= boost

            if self.dirt + nb < 0:
                nb = -self.dirt
                self.dirt = 0
            elif self.dirt + nb > 1000:
                nb = 1000 - self.dirt
                self.dirt = 1000
            else:
                self.dirt += nb

            return nb

        def get_cleanliness(self):

            if self.dirt < 10:
                return "clean"
            elif self.dirt < 25*district.rank:
                return "clean enough"
            elif self.dirt < 50*district.rank:
                return "dusty"
            elif self.dirt < 75*district.rank:
                return "dirty"
            elif self.dirt < 100*district.rank:
                return "disgusting"
            else:
                return "fire"

        def clean_up(self):

            price = self.get_clean_up_cost()

            if MC.has_gold(price):

                MC.gold -= price
                self.dirt = 0
                game.track("gold clean", price)
                renpy.block_rollback()

                return True

            else:
                renpy.say(narrator, "你没有足够的钱。")

                return False

        def get_clean_up_cost(self):

            return round_int(1.2 * (helper_cost[district.rank]*self.dirt)) #/self.maint_value))

        def get_auction_value(self):
            v = max(self.total_value - self.get_clean_up_cost(), 0)

            mod = (dice(7-district.rank) - 1) * 0.025 + (6-district.rank) * 0.05

            # 1 : 25-37.5 2 : 20-30 3 : 15-22.5 4: 10-15 5: 5-7.5

            return round_int(v * mod * game.get_diff_setting("gold"))

        def cycle_pic(self, reverse = False):

            if not reverse:
                self.pic_index += 1
                if self.pic_index > 7:
                    self.pic_index = 1
            else:
                self.pic_index -= 1
                if self.pic_index < 1:
                    self.pic_index = 7

            renpy.notify("\n循环..." + str(self.pic_index))

            self.pic = self.get_pic(config.screen_width, int(config.screen_height*0.8))

            renpy.jump("brothel")



#    class Competitor(): #Attributes: name, base_rep, girl_nb, av_girl_rep, tooltip

#        """This class is for competing brothels in the district."""


    class Calendar(object):

        """This class manages the game calendar, day/night cycle, and updates."""

        def __init__(self):

            self.time = 1
            self.day = 1
            self.month = 1
            self.year = 1
            self.moon = None
            self.alarms = {} # Events that proc on a particular day
            self.discounted = [] # Cheaper resources
            self.scarce = [] # More expensive resources
            self.contracts = []
            self.active_contract = None

        def get_date(self, _time):

            year_time = 1 + (_time-1) % (28*12)

            month = 1 + (year_time-1) // 28

            day = 1 + (year_time-1) % 28

            return str(month) + "/" + str(day)

        def newday(self, number = 1):

            for i in range(number):

                self.time +=1

                if self.day != 28:
                    self.day +=1

                else:
                    self.day = 1

                    if self.month != 12:
                        self.month += 1

                    else:
                        self.month = 1
                        self.year += 1

            if self.time % 7 == 1 :
                self.updates()


        def updates(self, new_district=False): #This is the place where weekly updates are handled

            weekly_updates(new_district)

            return


        def get_weekday(self):

            wd = self.day % 7 -1

            return weekdays[wd]


        def get_discount(self, source, target): # Where source, target are "gold" or a Resource object

            if source == "gold" and target.name in self.discounted:
                return 0.75
            elif source == "gold" and target.name in self.scarce:
                return 1.25
            elif target == "gold" and source.name in self.discounted:
                return 0.75
            elif target == "gold" and source.name in self.scarce:
                return 1.25
            else:
                rate = 1.0

                if source != "gold":
                    if source.name in self.discounted:
    #                    renpy.notify("found " + source + "in discounts 1")
                        rate *= 3/4.0
                    if source.name in self.scarce:
    #                    renpy.notify("found " + source + "in scarce 1")
                        rate *= 3/2.0
                if target != "gold":
                    if target.name in self.discounted:
    #                    renpy.notify("found " + source + "in discounts 2")
                        rate *= 3/2.0
                    if target.name in self.scarce:
    #                    renpy.notify("found " + source + "in scarce 2")
                        rate *= 3/4.0

                return rate

        def set_alarm(self, _time, _event):

            if isinstance(_event, StoryEvent):
                daily_events.append(_event)
                _event.date = _time

            else:
                if _time in self.alarms:
                    self.alarms[_time].append(_event)

                else:
                    self.alarms[_time] = [_event, ]

            if debug_mode:
                renpy.notify("\n警告设置 " + str(_time))


        def play_alarms(self, date=None):

            event_list = []

            if not date:
                date = self.time

            # Event objects

            if date in self.alarms:

                event_list = self.alarms[date]

                del self.alarms[date]

            # StoryEvent objects

            for ev in daily_events:
                if ev.happens(type="day"):
                    event_list.append(ev)

            if event_list:
                event_list.sort(key=lambda x: x.order)
                renpy.call("display_events", event_list)

        def get_season(self):

            if self.month <= 3:

                return "winter"

            elif self.month <= 6:

                return "spring"

            elif self.month <= 9:

                return "summer"

            elif self.month <= 12:

                return "fall"

        def generate_contracts(self):
            self.contracts = copy.deepcopy(rand_choice(contract_templates, 3))
            for con in self.contracts:
                con.randomize()





    class Log(object): # One log object is created each day to track various events

        def __init__(self, time):

            self.time = time
            self.cust = 0
            self.cust_served = 0
            self.gold_made = 0
            self.upkeep = 0
            self.costs = 0
            self.net = 0
            self.report = "{color=[c_white]}" + setting_name_dict[calendar.get_weekday()] + "，" + str(calendar.year) + "年" + str(calendar.month) + "月" + str(calendar.day) + "日{/color}\n"
            self.events = []
            self.changes = ""
            self.track_dict = defaultdict(int)

        def track(self, k, v=1):
            self.track_dict[k] += v

        def get_day_report(self):

#            net = round_int(self.gold_made - self.upkeep - self.costs)

            if self.net >= 0:
                msg = "昨晚利润：" + event_color["good"] % (str(round_int(self.net)) + " 金币") + "\n"
            else:
                msg = "昨晚亏损：" + event_color["bad"] % (str(round_int(self.net)) + " 金币") + "\n"

            msg += "{size=-2}" + "- 获得的金币: + " + event_color["good"] % str(round_int(self.gold_made)) + "\n"
            msg += "- 女孩的打赏: - " + event_color["bad"] % str(round_int(self.upkeep)) + "\n"
            msg += "- 青楼的维护: - " + event_color["bad"] % str(round_int(self.costs)) + "\n{/size}\n"

            msg += str(self.cust) + " 位客户来到了青楼\n"
            msg += "{size=-2}" + "- 招待人次 (正常): " + event_color["good"] % str(self.check("served")) + "/" + str(self.cust) + "\n"
            msg += "- 顾客满足 (正常): " + event_color["good"] % str(self.check("entertained")) + "/" + str(self.check("served")) + "\n"
            msg += "- 招待人次 (特殊): " + event_color["good"] % str(self.check("laid")) + "/" + str(self.cust) + "\n"
            msg += "- 顾客满足 (特殊): " + event_color["good"] % str(self.check("satisfied")) + "/" + str(self.check("laid")) + "\n{/size}\n"

            msg += str(self.check("work_days")) + " 位女孩在青楼工作"
##翻译
            if self.check("strike_days"):
                msg += event_color["bad"] % (str(self.check("strike_days")) + " 位女孩在当天罢工")
            if self.check("run_away"):
                    msg += event_color["bad"] % (str(self.check("run_away")) + " 位女孩在当天外出")

            msg += "\n{size=-2}" + "- 服务员: " + event_color["good"] % str(self.check("waitress_days")) + "\n"
            msg += "- 舞　娘: " + event_color["good"] % str(self.check("dancer_days")) + "\n"
            msg += "- 按摩师: " + event_color["good"] % str(self.check("masseuse_days")) + "\n"
            msg += "- 艺　伎: " + event_color["good"] % str(self.check("geisha_days")) + "\n"
            msg += "- 妓　女: " + event_color["good"] % str(self.check("whore_days")) + "\n{/size}"

            if self.check("rest_days") > 1:
                msg += str(self.check("rest_days")) + " 位女孩在青楼里休息"
            elif self.check("rest_days") > 0:
                msg += str(self.check("rest_days")) + " 位女孩在青楼里休息"

            if self.check("hurt_days") > 1:
                msg += event_color["bad"] % (str(self.check("hurt_days")) + " 位女孩在工作中受伤了")
            elif self.check("hurt_days") > 0:
                msg += event_color["bad"] % (str(self.check("hurt_days")) + " 位女孩在工作中受伤了")

            if self.check("exhausted"):
                msg += event_color["bad"] % (str(self.check("exhausted")) + " 位女孩工作到筋疲力尽")

            msg += "\n"

            if farm.active:
                msg += str(self.check("farm_days") + self.check("farm_rest_days")) + " 位女孩待在农场"

                if self.check("farm_resisted_training"):
                    msg += event_color["bad"] % (str(self.check("farm_resisted_training")) + " 位女孩抵制训练")

                if self.check("farm_run_away"):
                    msg += event_color["bad"] % (str(self.check("farm_run_away")) + " 位女孩在农场外出")

                if self.check("farm_hurt"):
                    msg += event_color["bad"] % (str(self.check("farm_hurt")) + " 位女孩反抗时受伤")

                if self.check("minion_hurt"):
                    msg += event_color["bad"] % (str(self.check("minion_hurt")) + " 位农场奴仆在战斗中受伤")

                msg += "\n{size=-2}" + "- 训　练: " + event_color["good"] % str(self.check("farm_training_days")) + "\n"
                msg += "- 待　机: " + event_color["good"] % str(self.check("farm_holding_days")) + "\n{/size}\n"

                if self.check("farm_rest_days") > 1:
                    msg += "{size=-2}- 休　息: " + event_color["good"] % str(self.check("farm_rest_days")) + "{/size} "
                elif self.check("farm_rest_days") > 0:
                    msg += "{size=-2}- 休　息: " + event_color["good"] % str(self.check("farm_rest_days")) + "{/size} "

            return msg

        def get_tonight_report(self):
            pass

        def check(self, k):
            return self.track_dict[k]

        def add_report(self, text):

            self.report += "\n" + text

        def add_event(self, event):

            self.events.append(event)

        def show_events(self):

            renpy.block_rollback()

            for event in self.events:

                renpy.checkpoint()

                if event == self.events[-1]:

                    renpy.choice_for_skipping()

                event.show_night()







### SECONDARY CLASSES ##

    class Event(object):

        """This class covers 2 kinds of events: Night events (run during working hours) and Day events (run when returning to the main screen). Day events should be phased out and replaced by Story Events"""

        def __init__(self, pic = None, background = None, char = None, text = "", changes = "", sound = None, with_st = None, type="Normal", label = None, object = None, order = 0, weight = 1):

            self.pic = pic
            self.background = background
            self.char = char
            self.text = text
            self.sound = sound
            self.with_st = with_st
            self.type = type
            self.changes = changes #+ "\n" + type
            self.label = label #For day events
            self.object = object #For day events
            self.order = order #For day events

        def show_night(self):

#            renpy.show_screen("night", self.pic)

            log.changes = self.changes

            if self.sound:
                renpy.play(self.sound, "sound")

            renpy.say(self.char, self.text)

        def happens(self):
            return True

        def play(self):

            if self.label:

                if self.object:
                    renpy.call(self.label, self.object)

                else:
                    renpy.call(self.label)

            else:

                if self.sound:
                    renpy.play(self.sound, "sound")

                renpy.say(self.char, self.text)


    class StoryEvent():

        def __init__(self, label, chapter=0, rank=0, date=0, year=0, month=0, day=0, weekday="", chance = 1.0, type="any", location = None, locations = None, seasons = None, min_gold = -999999999, condition = None, not_condition = None, condition_func=None, call_args=None, once = True, AP_cost = 1, order = 0, weight = 1, room = None):

            self.label = label
            self.chapter = chapter
            self.rank = rank
            self.date = date
            self.year = year
            self.month = month
            self.day = day
            self.weekday = weekday
            self.chance = chance
            self.type = type # Type can be: "any" (plays anytime), "city", "day" (plays on main screen), "night" (plays upon ending day), "morning" (plays after night events)
            self.location = location
            self.locations = locations # A list of locations
            self.seasons = seasons # A list of seasons
            self.min_gold = min_gold
            self.condition = condition
            self.not_condition = not_condition
            self.condition_func = condition_func # For complex conditions, this label is called with no arguments and must return a bool
            self.room = room
            if call_args == None: call_args = []
            self.call_args = call_args # call_args must be a list
            self.once = once
            self.AP_cost = AP_cost
            self.order = order
#            self.weight = weight

            self.happened = False
            self.mod = None

        def happens(self, type="any"): # Tests if happened, current chapter, chance of happening, location and custom story flags (optional)

            # renpy.say("checking", self.label)

            if type != "any" and self.type not in ("any", type):
                return False

            if self.happened and self.once:
                return False

            if game.chapter < self.chapter:
                return False

            if district.rank < self.rank:
                return False

            if calendar.time < self.date:
                return False

            if self.year and calendar.year != self.year:
                return False

            if self.month and calendar.month != self.month:
                return False

            if self.day and calendar.day != self.day:
                return False

            try:
                if self.weekday and calendar.get_weekday() != self.weekday:
                    return False
            except:
                self.weekday = None

            if self.min_gold > MC.gold:
                return False

            if renpy.random.random() > self.chance:
                return False

            if self.location:
                if self.location.lower() != selected_location.name.lower():
                    return False

            if self.locations:
                for loc in self.locations:
                    if loc.lower() == selected_location.name.lower():
                        break
                else:
                    return False

            if self.seasons:
                if calendar.get_season() not in self.seasons:
                    return False

            if self.condition:
                if self.mod:
                    if not self.mod.flags[self.condition]:
                        return False

                elif not story_flags[self.condition]:
                    return False

            if self.not_condition:
                if self.mod:
                    if self.mod.flags[self.not_condition]:
                        return False
                elif story_flags[self.not_condition]:
                    return False

            if self.room: # room must be spelled in lower case
                if not brothel.has_room(self.room):
                    return False

            if self.condition_func: # A custom function that must return 'True' or 'False'
                if not self.condition_func():
                    return False

            if self.mod:
                if self.mod not in game.active_mods.values():
                    return False

#            renpy.say("", self.label + "HAPPENS")

            return True

        def play(self):

            if self.once:
                r = story_remove_event(self.label)

                if not r:
                    if self.type == "city" and self in city_events:
                        city_events.remove(self)
                    elif self.type != "city" and self in daily_events:
                        daily_events.remove(self)

            renpy.call(self.label, *self.call_args)

            # Renpy probably doesn't reach those two command lines, so I have included them within the display_events label instead
            self.happened = True

            story_flags[self.label] = True

            return


    class Stat(object):

        """This class is for stats (skills with a value that can be changed)."""

        def __init__(self, name, type, parent, weight=0):

            self.name = name
            self.type = type
            self.parent = parent # For now, parent can be a Girl object only
            self.statmax = self.get_statmax()
            self.init_value(weight)
            self.lastvalue = self.value

        def get_description(self, total_value, maxrange):
            base_value = round_int(self.value)
            bonus = total_value - base_value
            bonus_text = ""

            if bonus > 0:
                bonus_text = " {color=[c_green]}(+" + str(bonus) + "){/color}"
            elif bonus < 0:
                bonus_text = " {color=[c_red]}(" + str(bonus) + "){/color}"

            description = "{b}" + str_int(total_value) + "/" + str(maxrange) + "{/b}" + bonus_text + "。" + gstats_dict[self.name]

            if self.name in gstat_job_skill.keys():
                return description % (self.parent.get_max_cust_served(gstat_job_skill[self.name]))

            return description

        def get_statmax(self):
            statmax = self.parent.rank * 50
            statmax += self.parent.get_effect("change", self.name.lower(), change_cap=True) + self.parent.get_effect("change", self.name.lower() + " max") + self.parent.get_effect("change", self.name + "all skill max")

            return statmax

        def init_value(self, weight): # Where weight is a number from 0 to 5

            if self.type != "sex": # REGULAR SKILLS

                # Skills have 5 levels of base proficiency from 1 (terrible) to 5 (superb)
                # Throws a dice if proficiency (weight) is not specified in init file

                if not weight: # Returns a random weight from 1 to 5
                    weight = weighted_choice([(5, 5), (4, 10), (3, 50), (2, 25), (1, 10)]) # The second number reads as a percentage chance (eg 25 = 25%)

                # This dict lists (a, b) for the skill maximum formula: a + lvl*b
                weight_dict = {5: (33, 7), 4 : (24, 6), 3 : (15, 5), 2 : (6, 4), 1 : (2, 3), 0 : (0, 0)}

                _min = weight_dict[weight-1][0] + self.parent.level * weight_dict[weight-1][1]
                _max = weight_dict[weight][0] + self.parent.level * weight_dict[weight][1]

                _max = min(_max, self.statmax) # Caps maximum according to rank and girl effects
                _min = min(_min, _max) # Minimum cannot exceed maximum

                self.value = renpy.random.randint(_min, _max)

            else: # SEX SKILLS

                # Sex skills are initiated depending on sexual preferences (generated first)
                # Checks preference

                pref = self.parent.get_preference(self.name.lower())

                weight = {"fascinated" : 8, "very interested" : 7, "interested" : 6, "a little interested" : 5, "indifferent" : 4, "a little reluctant" : 3, "reluctant" : 2, "very reluctant" : 1, "refuses" : 0}[pref]

                pref_dict = {8 : (33, 6), 7 : (24, 5), 6 : (20, 4), 5 : (16, 3), 4 : (11, 3), 3 : (7, 2), 2 : (2, 2), 1 : (0, 1), 0 : (0, 0), -1 : (0, 0)}

                _min = pref_dict[weight-1][0] + self.parent.level * pref_dict[weight-1][1]
                _max = pref_dict[weight][0] + self.parent.level * pref_dict[weight][1]

                _max = min(_max, self.statmax) # Caps maximum according to rank and girl effects
                _min = min(_min, _max) # Minimum cannot exceed maximum

                self.value = renpy.random.randint(_min, _max)

        def init_value_old(self, weight):

            if self.type == "sex":
                pref = self.parent.get_preference(self.name.lower())

                if pref == "refuses":
                    a = 0
                    b = -5
                elif pref in ("very reluctant", "reluctant"):
                    a = 1.5
                    b = 3.5
                elif pref in ("a little reluctant", "indifferent"):
                    a = 5
                    b = 10
                elif pref in ("a little interested", "interested"):
                    a = 7.5
                    b = 17.5
                elif pref in ("very interested", "fascinated"):
                    a = 12.5
                    b = 22.5
            else:

                # Loads the dice if specified in init file

                if weight == 5:
                    d = 100
                elif weight == 4:
                    d = 90
                elif weight == 3:
                    d = 50
                elif weight == 2:
                    d = 20
                elif weight == 1:
                    d = 0
                else:
                    d = dice(100)

                if self.type == "sex":

                    a = 0
                    b = -5

                elif d > 98: # Superb skill

                    a = 12.5
                    b = 22.5

                elif d > 85: # High skill

                    a = 7.5
                    b = 17.5

                elif d > 35: # Average skill

                    a = 5
                    b = 10

                elif d > 10: # Low skill

                    a = 1.5
                    b = 3.5

                else: # Terrible skill

                    a = 0
                    b = -5

            self.value = dice(5 + 5 * game.chapter) + a * game.chapter + b # Changed district.rank to game.chapter to allow for higher stats

            if self.value < 0:
                self.value = 0

            elif self.value > self.statmax:
                self.value = self.statmax


        def change(self, chg, _max = 250):

            # Will never decrease a stat when receiving a positive change
            if chg >= 0 and self.value > _max:
                _max = self.value

            if self.value + chg < 0:

                r = -self.value

                self.value = 0

                return r

            elif self.value >= _max:

                r = 0

                self.value = _max

                return r

            elif self.value + chg >= _max:

                r = _max - self.value

                self.value = _max

                return r

            else:
                self.value += chg

                return chg


    class Trait(object):

        """This class is for traits (skills with special effects that are either on or off)."""

        # eff1, eff2, eff3 are kept for backwards compatibility, until I clean up the code

        def __init__(self, name, verb, eff1 = None, eff2 = None, eff3 = None, effects = None, opposite = None, archetype = None, base_description = ""):

            self.name = name
            self.verb = verb

            self.effects = []

            if effects:
                self.effects = effects
            if eff1:
                self.effects.append(eff1)
            if eff2:
                self.effects.append(eff2)
            if eff3:
                self.effects.append(eff3)

            if opposite == None:
                self.opposite = []
            else:
                self.opposite = make_list(opposite)
            self.archetype = archetype

            self.base_description = base_description

#            renpy.say(self.name, str(len(self.effects)))

        def get_past_tense(self):

            if self.verb.startswith("be"):
                text1 = "已经"
            elif self.verb.startswith("have"):
                text1 = "已经"

            return self.add_article(text1) + " {b}" + self.name.lower() + "{/b}"

        def add_article(self, mytext):
            if self.verb.endswith("a"):
                mytext += "一个"
            elif self.verb.endswith("an"):
                mytext += "一个"

            return mytext

        def get_description(self, context=None, short=False):

            if short:
                return get_description("", self.effects)
            else:
                des = get_description(self.base_description, self.effects)

                if context in ("slavemarket", "free"):
                    if self.archetype:
                        des += "\n解锁{b}" + self.archetype + "{/b}特质分支。"

                return des

    class Perk(object):

        """This class is for all kinds of perks (used in the new perk system)"""

        def __init__(self, name, type, effects, archetype=None, pic = None, perk_level=0, min_rank=0, base_description = ""):
            self.name = name
            self.type = type
            self.effects = effects
            self.archetype = archetype
            self.level = perk_level
            self.min_rank = perk_level
            self.value = {0: 0, 1: 1, 2: 3, 3: 5}[perk_level]

            self.pic = pic
            if base_description:
                self.base_description = base_description
            else:
                self.base_description = perk_description[self.name]

        def get_pic(self):
            if self.pic:
                return Picture(self.pic, "perks/" + self.pic)
            else:
                return None

        def get_effect(self, type, target):
            for e in self.effects:
                if e.type.lower() == type.lower() and e.target.lower() == target.lower():
                    return True
            return False

        def get_description(self, short=False):
            if short:
                return get_description("", self.effects)
            else:
                return get_description("{i}" + self.base_description + "{/i}", self.effects)

    class PerkArchetype(object):

        """This class is for perk archetypes (used in the new perk system)"""

        def __init__(self, name, pic):

            self.name = name
            self.pic = pic
            self.unlocked = False
            self.base_description = archetype_description[self.name]

        def get_pic(self, portrait=False):
            if portrait:
                return Picture(self.pic[:-4] + " portrait" + self.pic[-4:], "perks/" + self.pic[:-4] + " portrait" + self.pic[-4:])
            else:
                return Picture(self.pic, "perks/" + self.pic)

        def get_perks(self, rank=None):
            if rank != None:
                return [perk for perk in perk_dict.values() if (perk.archetype == self.name and perk.level == rank)]
            else:
                mylist = [perk for perk in perk_dict.values() if (perk.archetype == self.name)]
                mylist.sort(key=lambda x: x.level)

                return mylist

        def get_description(self):
            return self.base_description


#        def init_perks(self):
#            self.slots = {}

#            for i in xrange(4):
#                self.slots[i] = archetype_perk_dict[self.name + " " + str(i)]


#        def has_effect(type, parameter): ## Syntax for effects is a tupple (type, parameter, value per level)

#            for eff in effects:
#                if eff(0) == type and eff(1) == parameter:
#                    return True
#            else:
#                return False

#        def get_effect(type, parameter):

#            value = 0

#            for eff in effects:
#                if eff(0) == type and eff(1) == parameter:
#                    value += eff(2)*self.level

#            return value


    class Effect():

        """This class is used for all effects applying to a character"""

         ## Type defines how the effect work

         # Boost applies a % increase (or decrease). Value is a float number
         # Change applies a fixed value change which is not limited by stat max. Change can be reversed. Value is a number.
         # Gain applies a one time permanent gain and is limited by stat max. Gain cannot be reversed. Value is a number.
         # Set replaces a base value with the new value
         # Allow unlocks a brothel option
         # Gift is the property of a gift item. I will have a different effect depending on a girl's tastes. Value is an int representing the gift bonus.
         # Flower is the property of a flower item. Value isn't used.
         # Special is hard-coded

         ## Value depends on the effect type. It is often used for checking the presence of an effect, so set it to 1 unless you need it to work differently

         ## Target defines what the effect affects

         ## Chance is the chance that the effect will happen. A float number.

         ## Scales_with is hard-coded for the moment and only concerns MC stats

         ## Scope is the scope of the effect: individual (None), brothel-wide ("brothel"), farm-wide ("farm"), free-girls ("city"), or "world" ("everywhere")

        def __init__(self, type, target = None, value = 0, chance = 1.0, scales_with = None, scope = None, dice=False, change_cap=True, duration=-1):
            self.type = type
            self.target = target
            self.value = value
            self.chance = chance
            self.scales_with = scales_with
            self.scope = scope
            self.source = None
            self.dice = dice
            self.change_cap = change_cap
            self.duration = duration # -1 duration = infinite. Duration is only used for buff effects

        def gain(self, thing, apply_boost=False, spillover=False):

            c = 0
            result = True

            #### APPLIES SCALING EFFECTS ####

            if self.scales_with:
                factor = get_scale_factor(thing, self.scales_with)
            else:
                factor = 1

            #### TEST EFFECT PROC CHANCE ####

            # Chance is tested here in case the gain is conditional
            if renpy.random.random() > self.chance:
                result=False

            #### APPLY EFFECT IF SUCCESSFUL ####

            # Instant cleaning (brothel)
            elif self.target == "dirt":
                c = brothel.change_dirt(factor*self.value)

            # Instant healing
            elif self.target == "heal":
                c = thing.heal(self.value)

            # Instant XP gain
            elif self.target in ("xp", "experience"):
                c = thing.change_xp(factor*self.value, apply_boost=apply_boost, spillover=spillover)

                while thing.ready_to_level():
                    thing.level_up()

            # Instant prestige gain
            elif self.target == "prestige":
                c = thing.change_prestige(factor*self.value, apply_boost=apply_boost)

                if thing.ready_to_level():
                    thing.level_up()

            # Instant JP gain
            elif self.target[-3:] == " jp":
                c = thing.change_jp(factor*self.value, self.target[:-3], apply_boost=apply_boost, spillover=spillover, announcement_delay=0)

            # Instant REP gain
            elif self.target in ("rep", "reputation"):
                c = thing.change_rep(self.value)

            # Instant perk points gain
            elif self.target in ("perk", "perks"):
                thing.perk_points += factor*self.value
                c = factor*self.value

            # Instant skill point gain
            elif self.target in ("skills", "skill points"):
                thing.upgrade_points += factor*self.value
                c = factor*self.value

            # Instant positive/negative fixation gain
            elif self.target.endswith(" fixation"):
                if self.value in fix_dict.keys():
                    c = thing.add_random_fixation(fixation=self.value, type=self.target[:3])
                else:
                    c = thing.add_random_fixation(type=self.target[:3])

                thing.personality_unlock[c] = False


            # Instant sex preference gain
            elif self.target == "all sexual preferences":
                for act in extended_sex_acts:
                    thing.change_preference(act, self.value)

            elif self.target.endswith(" preference"):
                thing.change_preference(self.target[:-11], self.value)

            # Permanent stat/skill gains
            else:
                c = thing.change_stat(self.target, factor*self.value, apply_boost=apply_boost, spillover=spillover)

            # Plays a sound when activating gain/instant
            if result:
                renpy.play(s_spell, "sound")
            else:
                renpy.play(s_fizzle, "sound")

            return c

        def get_description(self):

            value = self.value
            target = self.target
            text1 = ""

            if self.type in ("special", "personality"):

                if target == "naked":
                    text1 = "接受裸体"

                elif target == "level":
                    text1 = "+1等级 (等级上限: " + str(value) + ")"

                elif target == "virgin":
                    text1 = "她还是个处女。"

                elif target == "advertising power":
                    text1 = "增加你的广告女孩的力量 (对妓院的声誉、顾客的吸引和顾客的预算给予更高的提升)"

                elif target == "heal minion":
                    text1 = "治疗一个受伤的奴仆。"

                elif target == "workwhore":
                    text1 = "她将正常工作半天再特殊服务半天。"

                elif target == "lucky":
                    text1 = "在工作中(含特服)，获得重大成功的几率更高(不可叠加)"

                elif target == "unlucky":
                    text1 = "在工作中(含特服)，获得重大失败的几率更高"

                elif target == "temptress":
                    text1 = "可以说服不情愿的客人接受不同的特殊服务"

                elif target == "pickpocket":
                    text1 = "有机会从客户那里偷到10%的额外小费，如果被抓到就会降低声誉"

                elif target == "random item":
                    text1 = "顾客有很小的机会在她的照顾下'遗留'一件随机物品。"

                elif target == "BBCR bonus":
                    text1 = "可能会因为她的美貌、身材、魅力或优雅而提高客人的满意度"

                elif target == "LOCS bonus":
                    text1 = "可能会因为她的性欲、服从、体格或敏感而提高客人的满意度"

                elif target == "whore mood modifier":
                    text1 = "作为妓女而工作时心情变好"

                elif target == "job prestige":
                    text1 = "工作时能获得玩家声望"

                elif target == "skill catch up":
                    text1 += "每天晚上，她会帮助其他技能较低的女孩获得永久性的技能提升(每级一个女孩)"

                elif target == "effect chance":
                    text1 += "激活特权的基本几率翻倍(最多可以达到50%)"

                elif target == "defender":
                    text1 += "即使在没有AP的情况下，你也可以保卫青楼"

                elif target == "snake eyes":
                    text1 += "催眠永远不会失败"

                elif target == "safe":
                    text1 += "青楼的危险事件发生时候至少保留 " + str(value) + " 金币。"

                elif target == "focus":
                    text1 += "如果她只激活一个性行为，小费和声誉收益+25%(不包括百合和群交)"

                elif target == "rest shield":
                    text1 += "休息时，可对自己或朋友施放魔法盾牌，以保护其免受攻击"

                elif target == "ignore budgets":
                    text1 += "忽视客户的预算限制"
                text1 = "在作为妓女工作时接受群交(3P)行为" if target == "group" else text1
                text1 = "在作为妓女工作时接受百合(双飞)行为" if target == "bisexual" else text1
                text1 = "在任何时候包括平时都接受裸体" if target == "naked" else text1
                text1 = "在作为妓女工作时接受多人群交(狂欢)行为" if target == "orgy" else text1
                text1 = "顾名思义，接受扮演各种动物(比如马)的行为" if target == "ponygirl" else text1
                return text1

            elif self.type == "instant" and target == "heal":
                return "疗伤时间减少" + str(value) + "天。"

            if self.type == "set":
                target = "所有技能上限值" if target == "all skill max" else target
                text1 += "改变" + target + "到" + str(value)
                if self.scope:
                    text1 += "(%s)" % setting_name_dict[self.scope]
                return text1

            if self.type == "allow":
                if target.endswith("preference"):
                    target = "服务员偏爱" if target == "waitress preference" else target
                    target = "舞娘偏爱" if target == "dancer preference" else target
                    target = "按摩师偏爱" if target == "masseuse preference" else target
                    target = "艺妓偏爱" if target == "geisha preference" else target
                    target = "性服侍偏爱" if target == "service preference" else target
                    target = "性交偏爱" if target == "sex preference" else target
                    target = "肛交偏爱" if target == "anal preference" else target
                    target = "皮绳愉虐偏爱" if target == "fetish preference" else target
                    target = "群交偏爱" if target == "group preference" else target
                    target = "百合偏爱" if target == "bisexual preference" else target
                    target = "所有性行为偏爱" if target == "all sex acts preference" else target
                    text1 += "允许您增加客人的" + target + "到 +" + str(50*value) + "%"
                else:
                    text1 += "允许'" + setting_name_dict[target] + "'访问你的青楼"

                return text1

            if 0.75 <= self.chance < 1.0:
                text1 += "极高概率"

            elif 0.25 < self.chance < 0.75:
                text1 += "高概率"
            elif self.chance <= 0.25:
                text1 += "小概率"


            if self.type == "reroll":
                if text1:
                    text1 += "重掷中"
                else:
                    text1 += "重掷"

                if self.target == "job critical failure":
                    text1 += "当工作出现严重失误时"

                return text1

            if self.dice:
                text1 += "1-"

            elif value > 0:
                text1 += "+"

            if self.type in ("gain", "instant"): # Permanent x gain (xp, reputation...)
                try:
                    text1 += str(round_int(value)) + ""
                except:
                    text1 += str(value) + ""

                if self.target.endswith("preference") or self.target.endswith("preferences"):
                    text1 += ""

            elif self.type == "change": # Temporary x effect (can be removed)
#                 if value >= 1:
#                     text1 += str(round_int(value)) + " to "
#                 else:
                text1 += str(round_best(value, 2)) + ""
                if target.endswith("training obedience target"):
                    target = "作为训练时所需服从"
                if target.endswith("train obedience target"):
                    target = "作为训练时所需服从"
                if target.endswith("work obedience target"):
                    target = "作为工作时所需服从"
                if target.endswith("fight challenges"):
                    target = "挑战中战斗加成"
            elif self.type == "resist":
                text1 += str(round_int(value)) + "无效化"

            elif self.type == "spillover":
                percentage = round_int(value * 100)
                self.target = "经验" if self.target == "xp" else self.target
                self.target = "职业经验" if self.target == "jp" else self.target
                text1 += "每当获得" + self.target + "时，其他女孩也收获"+str(percentage) + "%的"

            elif self.type == "boost": # Temporary % effect (can be removed)

                percentage = round_int(value * 100)

                text1 += str(percentage) + "%"

            elif self.type == "gift":
                text1 += str(round_int(value)) + ""

            elif self.type == "increase satisfaction":
                text1 += str(round_int(value)) + "客户满意度限"

            if self.scope:
                #text1 += self.scope + ""
                #text1 += self.scope + " "
                scopexxx = ""
                if self.scope== "brothel":
                    scopexxx = "全青楼的"
                elif self.scope == "city":
                    scopexxx = "在城市中"
                else:
                    scopexxx = self.scope
                text1 += scopexxx + ""
            if target in ("rep", "reputation"):
                target="人气"

            ###替换掉中文注释造成的取值错误 strength,charisma,spirit,speed,"Charm","Beauty","Body","Refinement","Sensitivity","Libido","Constitution","Obedience","Service","Sex","Anal","Fetish"
            if target == "body":
                target = "身材"
            if target == "charisma":
                target = "玩家魅力"
            if target == "charm":
                target = "魅力"
            if target == "spirit":
                target = "玩家精神"
            if target == "strength":
                target = "玩家力量"
            if target == "speed":
                target = "玩家速度"
            if target == "beauty":
                target = "美貌"
            if target == "refinement":
                target = "优雅"
            if target == "sensitivity":
                target = "敏感"
            if target == "constitution":
                target = "体格"
            if target == "libido":
                target = "性欲"
            if target == "obedience":
                target = "服从"
            #替换extended_sex_acts = ["naked", "service", "sex", "anal", "fetish", "bisexual", "group"]
            if target == "naked":
                target = "露出"
            if target == "service":
                target = "性服侍"
            if target == "sex":
                target = "性交"
            if target == "anal":
                target = "肛交"
            if target == "fetish":
                target = "皮绳愉虐"
            if target == "bisexual":
                target = "百合"
            if target == "group":
                target = "群交"
            if target == "all jobs":
                target = "所有工作"
            if target == "all sex acts":
                target = "所有性行为"
            if target == "fear":
                target = "恐惧"
            if target == "love":
                target = "爱情"
            if target == "waitress":
                target = "服务员"
            if target == "dancer":
                target = "舞娘"
            if target == "masseuse":
                target = "按摩师"
            if target == "geisha":
                target = "艺伎"
            target = "舞娘职业经验收益" if target == "dancer jp gains" else target
            target = "按摩师职业经验收益" if target == "masseuse jp gains" else target
            target = "服务员职业经验收益" if target == "waitress jp gains" else target
            target = "艺伎职业经验收益" if target == "geisha jp gains" else target
            target = "肛交职业经验收益" if target == "anal jp gains" else target
            target = "性交职业经验收益" if target == "sex jp gains" else target
            target = "性服侍职业经验收益" if target == "service jp gains" else target
            target = "皮绳愉虐职业经验收益" if target == "fetish jp gains" else target
            target = "舞娘职业经验收益" if target == "dancer jp gains" else target
            target = "舞娘技能收益" if target == "dancer gains" else target
            target = "按摩师技能收益" if target == "masseuse gains" else target
            target = "服务员技能收益" if target == "waitress gains" else target
            target = "艺伎技能收益" if target == "geisha gains" else target
            target = "肛交技能收益" if target == "anal gains" else target
            target = "性交技能收益" if target == "sex gains" else target
            target = "性服侍技能收益" if target == "service gains" else target
            target = "皮绳愉虐技能收益" if target == "fetish gains" else target
            target = "经验收益" if target == "xp gains" else target
            target = "最大耐力" if target == "max energy" else target
            target = "收入" if target == "income" else target
            ###替换 strength,charisma,spirit,speed,"Charm","Beauty","Body","Body","Sensitivity","Libido","Constitution","Obedience","Service","Sex","Anal","Fetish"
            target = "魅力收益" if target == "charm gains" else target
            target = "美貌收益" if target == "beauty gains" else target
            target = "身材收益" if target == "body gains" else target
            target = "敏感收益" if target == "sensitivity gains" else target
            target = "性欲收益" if target == "libido gains" else target
            target = "体格收益" if target == "constitution gains" else target
            target = "服从收益" if target == "obedience gains" else target
            target = "优雅收益" if target == "refinement gains" else target
            target = "所有技能收益" if target == "all skill gains" else target
            target = "所有职业经验收益" if target == "all jp gains" else target

            target = "露出偏爱增加" if target == "naked preference increase" else target
            target = "肛交偏爱增加" if target == "anal preference increase" else target
            target = "性交偏爱增加" if target == "sex preference increase" else target
            target = "性服侍偏爱增加" if target == "service preference increase" else target
            target = "皮绳愉虐偏爱增加" if target == "fetish preference increase" else target
            target = "群交偏爱增加" if target == "group preference increase" else target
            target = "百合偏爱增加" if target == "bisexual preference increase" else target
            target = "所有性行为偏爱增加" if target == "all sex acts preference increase" else target

            target = "舞娘职业经验得分" if target == "dancer jp bonus" else target
            target = "按摩师职业经验得分" if target == "masseuse jp bonus" else target
            target = "服务员职业经验得分" if target == "waitress jp bonus" else target
            target = "艺伎职业经验得分" if target == "geisha jp bonus" else target
            target = "肛交职业经验得分" if target == "anal jp bonus" else target
            target = "性交职业经验得分" if target == "sex jp bonus" else target
            target = "性服侍职业经验得分" if target == "service jp bonus" else target
            target = "皮绳愉虐职业经验得分" if target == "fetish jp bonus" else target
            target = "舞娘职业经验" if target == "dancer jp" else target
            target = "按摩师职业经验" if target == "masseuse jp" else target
            target = "服务员职业经验" if target == "waitress jp" else target
            target = "艺伎职业经验" if target == "geisha jp" else target
            target = "肛交职业经验" if target == "anal jp" else target
            target = "性交职业经验" if target == "sex jp" else target
            target = "性服侍职业经验" if target == "service jp" else target
            target = "皮绳愉虐职业经验" if target == "fetish jp" else target
            target = "舞娘结果评价" if target == "dancer results" else target
            target = "按摩师结果评价" if target == "masseuse results" else target
            target = "服务员结果评价" if target == "waitress results" else target
            target = "艺伎结果评价" if target == "geisha results" else target
            target = "肛交结果评价" if target == "anal results" else target
            target = "性交结果评价" if target == "sex results" else target
            target = "性服侍结果评价" if target == "service results" else target
            target = "皮绳愉虐结果评价" if target == "fetish results" else target

            target = "破处获得的人气" if target == "virgin rep" else target
            target = "破处获得的小费" if target == "virgin tip" else target
            target = "每天第一位客人的满意度" if target == "first customer satisfaction" else target
            target = "完美结果时获得的小费" if target == "perfect result tip" else target
            target = "完美结果时获得的经验" if target == "perfect result xp" else target
            target = "完美结果时获得的职业经验" if target == "perfect result jp" else target
            target = "每天第一位客人的小费" if target == "first customer tip" else target
            target = "每天第一位客人获得的人气" if target == "first customer rep" else target
            target = "小费" if target == "tip" else target
            target = "所有技能上限值" if target == "all skill max" else target
            target = "所有技能属性" if target == "all skills" else target
            target = "外派任务效果" if target == "quest results" else target
            target = "外派培训效果" if target == "class results" else target
            target = "治疗效果" if target == "heal" else target
            target = "爱情得分" if target == "love bonus" else target
            target = "恐惧得分" if target == "fear bonus" else target
            target = "着迷性行为" if target == "positive fixation" else target
            target = "保安效果" if target == "security" else target
            target = "保洁效果" if target == "maintenance" else target
            target = "情绪收益" if target == "mood gains" else target
            target = "爱情收益" if target == "love gains" else target
            target = "情绪" if target == "mood" else target
            target = "广告效果" if target == "advertising" else target
            target = "客人数" if target == "customers" else target
            target = "普通工作时接客人数" if target == "job customer capacity" else target
            target = "个人防御" if target == "defense" else target
            target = "作为妓女时接客人数" if target == "whore customer capacity" else target
            target = "作为训练时所需服从" if target == "train obedience target" else target
            target = "作为工作时所需服从" if target == "job obedience target" else target
            target = "作为妓女时所需服从" if target == "whore obedience target" else target
            target = "耐力消耗" if target == "tiredness" else target
            target = "耐力消耗" if target == "energy use" else target
            target = "满足保养费时的效用" if target == "positive upkeep modifier" else target
            target = "怪物经验" if target == "monster xp" else target
            target = "野兽经验" if target == "beast xp" else target
            target = "机器经验" if target == "machine xp" else target
            target = "种马经验" if target == "stallion xp" else target
            target = "耐力恢复" if target == "energy" else target
            target = "经验" if target == "xp" else target
            target = "技能点" if target == "skill points" else target
            target = "玩家声望" if target == "prestige" else target
            target = "特质点" if target == "perk" else target
            target = "结交新朋友" if target == "making friends" else target
            target = "来自友谊而获得的心情收益" if target == "mood gains from friendship" else target
            target = "所有性行为偏好" if target == "all sexual preferences" else target
            target = "所有性行为技能" if target == "all sex skills" else target
            target = "性行为激活要求" if target == "sex act requirements" else target
            target = "所有常规技能" if target == "all main skills" else target
            target = "多给保养费的情绪增益影响" if target == "positive upkeep mood modifier" else target
            target = "少给保养费的情绪减益影响" if target == "negative upkeep mood modifier" else target
            target = "只工作半天时耐力回复量" if target == "half-shift resting bonus" else target
            target = "接客时客人因难以满足的扣分" if target == "customer penalties" else target
            target = "裸体进行常规工作时获得的小费" if target == "naked bonus" else target
            target = "接受工作或训练的可能性" if target == "obedience tests" else target
            target = "所有常规技能收益" if target == "all regular skills gains" else target
            target = "所有性行为技能收益" if target == "all sex skills gains" else target
            target = "青楼内污垢" if target == "dirt" else target
            target = "催眠效果" if target == "hypnosis result" else target
            target = "魔法值上限" if target == "mana" else target
            target = "农场偏好增加" if target == "farm preference increase" else target
            # target = "作为工作时所需服从" if target == "work obedience target" else target
            # target = "挑战中战斗加成" if target == "fight challenges" else target
            target = "购买价格" if target == "buy" else target
            target = "卖出价格" if target == "sell" else target

            target = "恐惧收益" if target == "fear gains" else target

            target = "总保养费用" if target == "total upkeep" else target
            target = "配饰增幅" if target == "accessory" else target
            target = "项链增幅" if target == "necklace" else target
            target = "戒指增幅" if target == "ring" else target

            target = "保养费" if target == "upkeep" else target
            target = "受伤损失" if target == "hurt" else target
            target = "人气收益" if target == "reputation gains" else target
            target = "舞娘职业经验收益" if target == "dancer jp gains" else target
            target = "舞娘职业经验收益" if target == "dancer jp gains" else target

            target = "名声" if target == "brothel reputation" else target
            target = "小费总额" if target == "total tip" else target
            target = "百合概率" if target == "bisexual chance" else target
            target = "群交概率" if target == "group chance" else target
            target = "作为工作时客户的预算" if target == "job customer budget" else target
            target = "作为妓女时客户的预算" if target == "whore customer budget" else target
            target = "客户活动 " if target == "customer events" else target
            target = "疯狂" if target == "crazy" else target
            target = "服务员偏爱" if target == "waitress preference" else target
            target = "舞娘偏爱" if target == "dancer preference" else target
            target = "按摩师偏爱" if target == "masseuse preference" else target
            target = "艺妓偏爱" if target == "geisha preference" else target
            target = "性服侍偏爱" if target == "service preference" else target
            target = "性交偏爱" if target == "sex preference" else target
            target = "肛交偏爱" if target == "anal preference" else target
            target = "皮绳愉虐偏爱" if target == "fetish preference" else target
            target = "群交偏爱" if target == "group preference" else target
            target = "百合偏爱" if target == "bisexual preference" else target
            target = "所有性行为偏爱" if target == "all sex acts preference" else target
            target = "满意度" if target == "satisfaction" else target
            target = "" if target == "" else target
            target = "" if target == "" else target
            target = "" if target == "" else target

            text1 += target


            if target == "hurt":
                text1 += "伤害"
            elif target in extended_sex_acts:
                text1 += "行为"
            elif target == "random item":
                text1 += "在工作时"

            if self.scales_with:

                if self.scales_with == "equipped":
                    text1 += "随装备数递增"

                elif self.scales_with == "cust nb":
                    text1 += "随客人数递增"
                elif self.scales_with == "job cust nb":
                    text1 += "针对为客人工作时"
                elif self.scales_with == "whore cust nb":
                    text1 += "针对为客人提供特殊服务时"
                elif self.scales_with == "customer satisfaction":
                    text1 += "随客户满意度递增"
                else:
                    #text1 += "" + self.scales_with

                    if self.scales_with == "strength":
                        scalesxxx="随主角力量递增"
                    elif self.scales_with == "spirit":
                        scalesxxx="随主角精神递增"
                    elif self.scales_with == "charisma":
                        scalesxxx="随主角魅力递增"
                    elif self.scales_with == "speed":
                        scalesxxx="随主角速度递增"
                    elif self.scales_with == "charisma":
                        scalesxxx="随主角魅力递增"
                    elif self.scales_with == "defense":
                        scalesxxx="随个人防御递增"
                    elif self.scales_with in ("rep", "reputation"):
                        scalesxxx="随个人名声递增"
                    elif self.scales_with == "rank":
                        scalesxxx="随阶级递增"
                    elif self.scales_with == "equipped": # Counts every piece of equipment
                        scalesxxx="随装备数递增"
                    elif self.scales_with == "district":
                        scalesxxx="随地区递增"
                    else:
                        scalesxxx=self.scales_with
                    text1 += scalesxxx

            if self.duration > 0:
                text1 += "(持续"

                if self.duration > 1:
                    text1 += str(self.duration) + "天-不叠加)"

                elif self.duration == 1:
                    text1 += "1天-不叠加)"

            return text1


    class Sexact(): #Attributes: name, description, contributing_stats, variants, results

        """This class is for specifying sex acts and the results they have."""


        def __init__(self, likelihood, bonus):

            self.likelihood = likelihood
            self.bonus = bonus



    class ItemType(object):

        """ This class covers common item types and their base properties """

        def __init__(self, name, usage = "wear", slot = None, filter = "misc", sound = None, adjectives = "misc", stackable = False, dir=None, sellable=True, giveable=True):

            self.name = name
            self.usage = usage
            self.slot = slot
            self.filter = filter
            self.sound = sound
            self.adjectives = adjectives
            if dir:
                self.dir = dir
            else:
                self.dir = self.name
            self.sellable = sellable
            self.giveable = giveable
#            self.stackable = stackable


    class Item(object):

        """This class is for inanimate objects that the MC or girls can own."""

        def __init__(self, name, target, type, pic = None, template = False, rank = 1, max_rank = 5, rarity = 1, charges = None, price = 10000, effects = None, description = "", adjectives = None, sound = None, hidden_effect = False, pic_dir = None):

            self.base_name = name
            self.name = name
            self.target = target
            self.type = type
            if pic_dir:
                self.pic_dir = pic_dir
            else:
                self.pic_dir = self.type.dir

            if pic:
                self.pic = Picture(pic, "items/" + self.pic_dir + "/" + pic)
            else:
                self.pic = Picture("misc.webp", "items/misc/misc.webp")

            self.template = template
            self.min_rank = rank
            self.rank = rank
            self.max_rank = max_rank
            self.rarity = rarity
            self.charges = charges
            self.base_price = price
            self.price = price
            if effects == None: effects = []
            self.base_effects = effects
            self.effects = effects
            self.equipped = False
            self.hidden_effect = hidden_effect

            ## Inherits properties from item type

            self.usage = self.type.usage
            self.slot = self.type.slot
            self.filter = self.type.filter
#            self.stackable = self.type.stackable

            ## An individual item can override type adjectives and sound if necessary

            if adjectives:
                self.adjectives = adjectives

            else:
                self.adjectives = self.type.adjectives

            if sound:
                self.sound = sound
            else:
                self.sound = self.type.sound

            self.base_description = description
            self.update_description()

        def get_pic(self, x = 50, y = 50):
            return self.pic.get(x = x, y = y)

        def get_key(self):
            return (self.type.name, self.rank, self.base_name, self.price)

        def has_effect(self, type="any", target="any"):
            for eff in self.effects:
                if (type in (eff.type, "any")) and (target in (eff.target, "any")):
                    return True
            return False

        def get_effect(self, type, target):
            return get_effect(self, type, target, iterate=True)

        def can_wear(self, type):

            if self.usage != "wear":

                return False

            elif self.target == type:
                return True

            else:
                return False


        def can_use(self, type):

            if self.usage not in ("use", "auto"):

                return False

            elif self.target == type:
                return True

            else:
                return False


        def use_me(self, nb = 1):

#            renpy.say("", self.name +  " has " + str(self.charges) + " charges")

            if self.charges >= nb:

                self.charges -= nb

                if self.charges <= 0:
                    return "used_up"

                else:
                    return self.charges

            else:

                renpy.say("", "没有足够的费用(" + str(self.charges) + ")")

                return "no charges"

            self.update_description()

        def get_price(self, operation):

            modifier = MC.get_modifier(operation)

            baseprice = self.price

            finalprice = round_int(baseprice * modifier)

            return finalprice


        def available_at_rank(self, rank): # Useless?

            if rank >= self.min_rank and rank <= self.max_rank:
                return True
            else:
                return False


        def transform(self, target_rank): # Transforms an item in a better or worse version of itself

            if self.template == True:
                self.name = quality_prefix[self.adjectives + "_" + str(target_rank)] + self.base_name.lower()
                self.price = round_int(quality_modifier[target_rank] * self.base_price)

                self.effects = []

                for eff in self.base_effects:
                    if target_rank > 0:
                        value = target_rank * eff.value
                    else:
                        value = eff.value / 2

                    self.effects.append(Effect(eff.type, eff.target, value))

                self.update_description()

                return self

            else:
                return None

        def generate_new_item(self, target_rank): # Creates new Item from this template item

            if self.template == True:

                new_it = copy.deepcopy(self)

                new_it.name = quality_prefix[self.adjectives + "_" + str(target_rank)] + self.base_name.lower()
                new_it.price = round_int(quality_modifier[target_rank] * self.base_price)

                if self.rarity in ("S", "U", "M"):
                    new_it.rarity = self.rarity
                else:
                    new_it.rarity = self.rarity + target_rank - self.min_rank

                new_it.effects = []

                for eff in self.effects:
                    eff = copy.deepcopy(eff)

                    if target_rank > 0:
                        eff.value = target_rank * eff.value
                    else:
                        eff.value = eff.value / 2

                    new_it.effects.append(eff)

                new_it.min_rank = max(target_rank - 2, 0)
                new_it.rank = min(target_rank, 6)

                new_it.update_description()

#                renpy.say(new_it.name, "Min rank:" + str(new_it.min_rank) + " Rank:" + str(new_it.rank) + " Rarity:" + str(new_it.rarity))

                return new_it


        def update_description(self):

            if self.hidden_effect:

                self.description = self.base_description

            else:

                self.description = get_description(self.base_description, self.effects)

                if self.usage in ("use", "auto"):

                    if self.charges > 1:
                        self.description += " (" + str(self.charges) + "用掉了.)"



#    class Inventory(): # Attributes: Type (girl or items), items, girls, money

#        """This class is for inventories both with items and girls."""




    class Room(object):

        """This class is for rooms in a brothel, normal (bedrooms) and special (commons)"""

        def __init__(self, name, level = 0, type = "bedroom", job = None, cost=0): # Level is used for price of special rooms

            self.name = name
            self.level = level # Should be replaced with rank
            self.type = type # bedroom or special
            self.cust_limit = 0
            self.pic_path = "brothels/rooms/" + room_pics[self.name]
            self.pic = Picture(path=self.pic_path)
            self.bg = renpy.image(self.name, im.Scale(self.pic_path, config.screen_width, config.screen_height))
            self.job = job
            self.cost = cost
            self.girls = [] # Used for the master bedroom

        def add_girl(self, girl): # Used for the master bedroom
            if len(self.girls) < self.level:
                self.girls.append(girl)
                return True
            else:
                return False

        def remove_girl(self, girl): # Used for the master bedroom
            if girl in self.girls:
                self.girls.remove(girl)
                return True
            return False

        def can_have_girl(self, number=1):
            if len(self.girls) + number <= self.level:
                return True
            return False

        def buy(self, forced=False):
            if forced:
                self.level = 1
                self.update_cust_limit(True)

            elif brothel.free_room:
                if renpy.call_screen("yes_no", "你真的想选择" + self.name + " 作为你的免费房间吗？"):
                    renpy.play(s_spell, "sound")
                    self.level = 1
                    self.update_cust_limit()
                    brothel.free_room = False

            elif self.get_price() >= MC.gold:
                renpy.say(sill, "对不起，主人，你没有足够的金币来修建这个房间。")


            elif renpy.call_screen("yes_no", "你确定要为建设" + self.name + "而花费 " + str(self.get_price()) + " 金币？"):
                MC.gold -= self.get_price()
                brothel.total_value += self.get_price()
                renpy.play(s_gold, "sound")
                self.level = 1
                self.update_cust_limit()

            unlock_pic(self.pic_path)

        def upgrade(self, forced = False):
            if forced:
                self.level += 1
                self.update_cust_limit(True)
            elif self.get_price() >= MC.gold:
                renpy.say(sill, "对不起，主人，你没有足够的金币来升级这个房间。")
            elif renpy.call_screen("yes_no", "你确定要为升级" + self.name + "而花费 " + str(self.get_price()) + " 金币？"):
                MC.gold -= self.get_price()
                brothel.total_value += self.get_price()
                renpy.play(s_gold, "sound")
                self.level += 1
                self.update_cust_limit()

        def get_pic(self, x=None, y=None, proportional=True):
            if not x:
                x = config.screen_width
            if not y:
                y = config.screen_height
            return self.pic.get(x, y, proportional)

        def get_price(self):
            if self.cost:
                return self.cost
            else:
                return brothel.get_room_price(self.type)

        def get_description(self):
            if self.type == "master":
                if self.level > 1:
                    desc = "{font=[style.default.font]}最多可容纳" + str(self.level) + " 位女孩进行训练. 进入主人房的女孩每天晚上都接受免费训练。"
                elif self.level == 1:
                    desc = "{font=[style.default.font]}最多可容纳1位女孩接受培训. 进入主人房的女孩每天晚上都接受免费训练。"
                else:
                    desc = "{font=[style.default.font]}你的单身房. 没有容纳其他女孩的空间。"

                # if self.level > 0:
                #     desc += "\nCurrently assigned: "
                #     if len(self.girls) >= 1:
                #         desc += and_text([g.fullname for g in self.girls])
                #     else:
                #         desc += "No girl assigned"

                if self.level < brothel.rank:
                    desc += "\n改善这个房间需要花费 " + str(master_bedrooms[self.level+1].cost) + " 金币。"
                elif self.level == 5:
                    desc += "\n{i}你不能再改善主人房了。{/i}"
                # else:
                #     desc += "\n{i}You need a new brothel license to improve this room further.{/i}"

                return desc

            if brothel_firstvisit:
                return "修建" + self.name + "用以练习" + girl_related_dict[self.job]
            elif self.level == 0:
                return "修建" + self.name + "需要 " + str(self.get_price()) + " 金币。"
            elif self.level < district.rank:
                return "每天晚上" + self.name + "可以接待" + str(self.cust_limit) + " 位客人。升级" + self.name + "需要 " + str(self.get_price()) + " 金币，以容纳更多的客户。"
            else:
                return "每天晚上" + self.name + "可以接待" + str(self.cust_limit) + " 位客人。"

        def update_cust_limit(self, silent=False):
            self.cust_limit = room_capacity_dict[game.chapter] * self.level

            #<Chris Job Mod>
            if game.has_active_mod("chrisjobmod"):
                self.cust_limit = round_int(self.cust_limit * act_max_customers_modifier[self.job])
            #</Chris Job Mod>

            if not silent:
                renpy.say(sill, "你现在可以接待" + str(self.cust_limit) + " 位客人使用" + self.name + "。{w=1.0}{nw}")



    class Quest(object):

        """This class is a template for quests and classes"""

        def __init__(self, type, name, main_stat, second_stat, other_stats, tags, description, sound = s_sigh, special_event = (None, 1.0)):

            self.type = type # "class" or "quest"
            self.name = name
            self.description = description
            self.tags = make_list(tags)
            self.sound = sound

            self.main_stat = main_stat
            self.secondary_stat = second_stat
            self.other_stats = other_stats

            self.enrolled = []
            self.special = None
            self.special_event = special_event[0] # To be implemented later
            self.special_event_chance = special_event[1] # To be implemented later

        def randomize(self, rank):

            self.enrolled = []
            self.rank = round_int(rank)

            ## Randomize picture

            self.pic = get_pic(quest_board, self.tags)


            ## Set duration

            self.duration = max(dice(2 + rank//2), rank//2) # Rank 1: 1-2d Rank 2: 1-3d Rank 3: 2-3d Rank 4: 2-4d Rank 5: 2-4d


            ## Test special status

            if dice(6) == 6:
                if self.type == "class":
                    self.special = rand_choice(("有折扣", "大师班"))
                elif self.type == "quest":
                    self.special = rand_choice(("高报酬", "臭名昭著"))
            else:
                self.special = None

            ## Set bonus and stat cap for classes

            if self.type == "class":

                self.bonuses = []

                #! Improved bonuses with rank
                self.bonuses.append([self.main_stat, self.duration*2 + rank, self.duration*4 + rank]) # Stores min/max bonuses to stat per day

                if rank > 1 and dice(100) < (rank-1) * 25: # Chance of adding second bonus at higher ranks
                    self.bonuses.append([self.secondary_stat, self.duration + rank//1.5, self.duration*3 + rank//1.5]) # Stores min/max bonuses to stat per day
                if rank > 3 and dice(100) < (rank-3) * 25: # Chance of adding third bonus at higher ranks
                    self.bonuses.append([rand_choice(self.other_stats), self.duration-1 + rank//2, self.duration*2 + rank//2]) # Stores min/max bonuses to stat per day

                self.stat_cap = 55 * rank #! Experimental

                self.capacity = 1 + dice(rank+1)


            ## Randomize stat requirements for quests

            if self.type == "quest":

                self.requirements = []

                # Normal stats have higher requirements than sx stats at earlier ranks then converge at rank 5
                if self.main_stat.capitalize() in gstats_main:
                    self.requirements.append([self.main_stat, 20 * rank + dice(40, rank)]) #!

                else:
                    self.requirements.append([self.main_stat, 4 * rank**2 + dice(40, rank)]) #!

                if dice(100) < (rank - 1) * 25: # Chance of adding second requirement at higher ranks

                    if self.main_stat.capitalize() in gstats_main:
                        self.requirements.append([self.secondary_stat, 20 * (rank-1) + dice(40, rank-1)]) #!

                    else:
                        self.requirements.append([self.secondary_stat, 4 * (rank-1)**2 + dice(40, rank-1)]) #!

                if dice(100) < (rank - 2) * 25: # Chance of adding third requirement at higher ranks

                    if self.main_stat.capitalize() in gstats_main:
                        self.requirements.append([rand_choice(self.other_stats), 20 * (rank-1) + dice(40, rank-1)]) #!

                    else:
                        self.requirements.append([rand_choice(self.other_stats), 4 * (rank-1)**2 + dice(40, rank-1)]) #!


            ## Add 2 positive + 1 negative traits

            self.pos_traits = rand_choice(gold_traits + pos_traits, 2)

            self.neg_trait = rand_choice(neg_traits)


            ## Calculate rewards and costs

            if self.type == "quest":

                self.gold = 25*rank**2
                self.xp = 0
                self.rep = 0

                # Values have yet to be play-tested to make sure nothing is broken

                for stat, value in self.requirements:

                    if stat in gstats_main:
                        self.gold += value * quest_base_gold["normal"]
                        self.rep += 2 ** (rank-1)

                    else:
                        self.gold += value * quest_base_gold["sex"]
                        self.rep += 2 * (2 ** (rank-1))

                    self.xp += value * rank

                # Apply duration bonus (long quests bring more cash, short quests are good for rep)

                self.gold *= self.duration + 0.05*(self.duration-1)
                self.rep *= 1 + 0.05*(self.duration-1)
                self.xp *= self.duration

                if self.special == "高报酬":
                    self.gold *= 1.5

                self.gold = round_int(self.gold * brothel.get_effect("boost", "quest rewards") * game.get_diff_setting("rewards"))
                self.rep = round_int(self.rep * brothel.get_effect("boost", "quest rewards") * game.get_diff_setting("rewards"))
                self.xp = round_int(self.xp * brothel.get_effect("boost", "quest rewards") * game.get_diff_setting("rewards"))

            elif self.type == "class":

                self.gold = 25*rank**2

                for stat, _min, _max in self.bonuses:
                    if stat in gstats_main:
                        self.gold += (_min+_max)/2 * 5
                    else:
                        self.gold += (_min+_max)/2 * 10

                self.xp = (10 * rank**2) * self.duration * game.get_diff_setting("rewards") #! Experimental
                self.rep = (1 + 0.05*(self.duration-1)) * 2**(rank-1) * game.get_diff_setting("rewards")

                if self.special == "有折扣":
                    self.gold = round_int(0.75*self.gold)

            self.energy = -5 * rank * self.duration


        def test_eligibility(self, girl, ignore_status = False): # Returns a tuple: bool + ttip

            if not ignore_status:
                if girl.hurt > 0 or girl.away or girl.exhausted:
                    return (False, "你的女孩目前无法工作或学习。")

            if self.type == "class":

                if MC.gold >= self.gold:

                    for stat, _min, _max in self.bonuses:
                        if girl.get_stat(stat, raw=True) < self.stat_cap:
                            return (True, "为%s注册所选的课程。" % girl.fullname)

                    return (False, "你女孩的技能太高了，不能从这门课中学到任何东西。")

                else:
                    return (False, "你没有足够的钱为女孩注册这门课程。")


            elif self.type == "quest":

                for stat, value in self.requirements:
                    if girl.get_stat(stat) < value:
                        return (False, "你的女孩不符合这项任务的要求。")
                return (True, "给%s布置任务。" % girl.fullname)

            raise AssertionError, "奇怪的是" + self.type

        def count_eligible_girls(self):

            eligible = sum(1 for girl in MC.girls if self.test_eligibility(girl, ignore_status=True)[0])

            return eligible

        def get_results(self, girl):
            #替换用词
            if self.type.capitalize()=="Class":
                title = "外出培训 已完成。"
                description = girl.fullname + " 已经自培训学校返回了。"
            elif self.type.capitalize()=="Quest":
                title = "外出任务 已完成。"
                description = girl.fullname + " 已经自任务地点返回了。"
            # title = self.type.capitalize() + " completed"
            # description = girl.fullname + " has returned from her " + self.type + ". "

            if self.type == "class":

                # Only mood affects learning for now (from +5 to -5)
                perf = dice(6, 2) + girl.mood // 20

                # Having friends in the class improves learning (tested twice: on enrollment and when results are delivered)
                #!

                for g in girl.friends:
                    if g in self.enrolled:
                        girl.class_friend_bonus = 2
                        break
                for g in girl.rivals:
                    if g in self.enrolled:
                        girl.class_friend_bonus = -1
                        break

                perf += girl.class_friend_bonus

                # Memories of rewards and punishment

                if girl.remembers("reward", "class good result"):
                    perf += 1
                if girl.remembers("punish", "class bad result"):
                    perf += 1

                if perf >= 12:
                    description += "她非常努力地学习，取得了非凡的进步。"
                    boost = 2.0

                    girl.track_event("class good result", arg="她在" + self.name  + "这门课程中学习很努力。")

                elif perf >= 9:
                    description += "她认真听老师讲课，取得了良好的进步。"
                    boost = 1.5

                    girl.track_event("class good result", arg="她在" + self.name + "这门课程中取得了良好的进步。")

                elif perf <= 2:
                    description += "她根本不关心功课，几乎没有进步。"
                    boost = 0.75

                    girl.track_event("class bad result", arg="她没有努力学习" + self.name + "这门课程。")

                elif perf <= 5:
                    description += "她几乎没有注意听老师讲课，这影响了她的进步。"
                    boost = 0.5

                    girl.track_event("class bad result", arg="她基本上没有学会" + self.name + "这门课程任何东西。")

                else:
                    description += "她取得了一些进步。"
                    boost = 1.0

                #!
                if girl.class_friend_bonus > 0:
                    description += "她很高兴能与朋友一起学习。"
                    girl.change_mood(10)
                elif girl.class_friend_bonus < -1:
                    description += "她不喜欢她和她的对手在同一个班级。"
                    girl.change_mood(-5)

                if self.special == "大师班":
                    boost *= 1.5

                boost *= girl.get_effect("boost", "class results") * game.get_diff_setting("rewards")

                changes = [(girl_related_dict[stat], round_int(girl.change_stat(stat, renpy.random.randint(_min, _max)*boost, custom_cap = self.stat_cap))) for stat, _min, _max in self.bonuses]

            elif self.type == "quest":

                # Only main stat affects result. Random variation from +6 to -6 times rank
                perf = girl.get_stat(self.main_stat) + girl.mood // 5 + dice(13, self.rank) - 7*self.rank - self.requirements[0][1]

                # Memories of rewards and punishment

                if girl.remembers("reward", "quest good result"):
                    perf += 1
                if girl.remembers("punish", "quest bad result"):
                    perf += 1

                if perf >= 20 * self.rank:
                    description += "{color=[c_orange]}她的表演令人惊叹。客户欣喜若狂!{/color}"
                    boost = 1.5

                    girl.track_event("quest good result", arg="她在任务中表现得{color=[c_emerald]}非常出色{/color}")

                elif perf >= 10 * self.rank:
                    description += "{color=[c_emerald]}她表演得很好。客户很开心。{/color}"
                    boost = 1.25

                    girl.track_event("quest good result", arg="她在任务中表现{color=[c_emerald]}良好{/color}")

                elif perf < 0:
                    description += "{color=[c_red]}她表演得很糟糕。客户很失望，拒绝全额付款。{/color}"
                    boost = 0.75
                    girl.track_event("quest bad result", arg="她在任务中表现{color=[c_crimson]}糟糕{/color}")

                else:
                    description += "她顺利完成了任务。"
                    boost = 1.0

                had = []

                for trait in self.pos_traits:
                    if girl.has_trait(trait.name):
                        had.append(trait.get_past_tense())
                        boost *= 1.5

                if had:
                    description += "客人为她感到兴奋" + and_text(had) + "。"

                if girl.has_trait(self.neg_trait.name):
                    description += "客人对她很生气" + self.neg_trait.get_past_tense() + "。"
                    boost /= 2.0

                boost *= girl.get_effect("boost", "quest results") # Note quest results boost is different from quest reward boost

                reward = round_int(self.gold*boost)
                self.rep = round_int(self.rep*boost)

                if self.special == "臭名昭著":
                    self.rep *= 2.0

                MC.gold += reward
                girl.add_log("quest_gold", reward, -1)

            xp = round_int(girl.change_xp(self.xp))
            rep = round_int(girl.change_rep(self.rep))
            energy, status = girl.change_energy(self.energy)

            if status == "exhausted":
                " 她已经{color=[c_red]}筋疲力尽{/color}，需要休息，直到她恢复。"

            description += "\n"

            girl.add_log("total_xp", xp, -1)

            if self.type == "class":
                girl.add_log("class_xp", xp, -1)

                for stat, value in changes:
                    description += stat_increase_dict["stat"] % (stat.capitalize(), value)

            elif self.type == "quest":
                girl.add_log("quest_xp", xp, -1)

                description += stat_increase_dict["gold+"] % reward

            description += stat_increase_dict["xp_dark"] % xp
            description += stat_increase_dict["rep"] % rep
            description += stat_increase_dict["stat_neg"] % ("耐力", round_int(energy))

            if girl.ready_to_level():
                girl.level_up()
                description += stat_increase_dict["level"]

            if girl.ready_to_rank():
                description += stat_increase_dict["rank"]

            return title, description


init -8 python:

    class Goal(object):

        def __init__(self, type, value = 0, target = 0, label = "", channel="advance", max_chapter=None):

            self.type = type
            self.value = value
            self.target = int(target)
            self.label = label
            self.channel = channel
            self.max_chapter = max_chapter
            self.description = self.get_description()

        def get_description(self):

            if self.type == "gold":
                return "需要获得 " + str(int(self.value)) + " 金币"

            elif self.type == "ranked":
                return "需要有 " + str(self.target) + " 位女孩阶级达到 " + rank_name[self.value]

            elif self.type == "reputation":
                return "需要达到 " + str(self.value) + " 点青楼名声"

            elif self.type == "prestige":
                return "需要获得 " + str(self.value) + " 点声望"

            elif self.type == "story":
                return self.value # value for story events must be text

            else:
                return "你现在处于无尽模式，尽情享受游戏吧！"

        def reached(self):

            if self.max_chapter and self.max_chapter > game.chapter:
                return True

            elif self.type == "gold":
                if MC.gold >= self.value:
                    return True

            elif self.type == "ranked":
                if len([g for g in MC.girls if g.rank >= self.value]) >= self.target:
                    return True

            elif self.type == "reputation":
                if brothel.rep >= self.value:
                    return True

            elif self.type == "prestige":
                if MC.prestige >= self.value:
                    return True

            elif self.type == "story":
                if story_flags[self.label]:
                    return True

            return False

init -2 python:

    class Location(object):

        """This class is used for locations you can visit in the various city districts"""

        def __init__(self, name, pic, has_girls = True, secret = False, action = False, menu = None, menu_costs_AP = True):

            self.name = name
            self.pic = "districts/locations/" + pic
            self.has_girls = has_girls
            self.secret = secret
            self.action = action
            self.menu = menu # Menu is a tuple: first is the button caption, second is the target label
            self.menu_costs_AP = menu_costs_AP
            self.girls = []
            self.runaways = []
#            self.bg = renpy.image("bg " + name.lower(), ProportionalScale(self.pic, config.screen_width, int(config.screen_height*0.8)))

        def get_pic(self, x=None, y=None, wide=False):
            if not x:
                x = config.screen_width
            if not y:
                y = config.screen_height
                if wide:
                    y = int(y*0.8)

            return im.Scale(self.pic, x, y)

        def list_girls(self):

            l = []

            for g in self.girls:

                l.append(g.name)

            return "这个地方有女孩: " + and_text(l)

        def clear_girls(self):

            del self.girls[:]

            return

        def can_do_action(self):
            if not self.action:
                return False
            if self.menu_costs_AP and MC.interactions < 1:
                return False
            if self.menu[1].startswith("collect_"):
                if MC.last_collected[self.menu[1][8:]] == calendar.time:
                    return False
            elif self.menu[1] == "visit_thieves_guild":
                if not NPC_renza.items:
                    return False
            elif self.menu[1] == "visit_watchtower":
                if not NPC_captain.items:
                    return False
            return True


    class Spell(object):

        """ This class covers spells used by the MC """

        def __init__(self, name, pic = "aura1.webp", type = "passive", level = 0, cost = 0, effects = None, duration = None, sound = "spell.ogg", description = "A basic spell."):

            self.name = name
            self.pic = Picture(pic, "spells/" + pic)
            self.type = type
            self.level = level
            self.cost = cost # Passive spells have a cost of zero
            if effects:
                self.effects = effects
            else:
                self.effects = []
#             self.instant = instant
            self.duration = duration
            self.sound = sound
            self.description = get_description(description, effects)
#            self.learnt = False
#            self.active = False
            self.auto = False

        def get_cost(self):
            return self.cost

#             cost = self.cost - MC.get_spirit()

#             if cost < 1:
#                 cost = 1

        def get_cost_description(self):
            if self.duration == "turn":
                return str_int(self.get_cost()) + " mana/turn"

            else:
                return str_int(self.get_cost()) + " mana"

    class Personality(object): # Personality archetype used to semi-randomize girl personality attributes and specific dialogue

        def __init__(self, name, attributes, personality_dialogue_only=None, dialogue_personality_weight=3, dialogue_attribute_weight=1, custom_dialogue_label=None, description="", often_stories=None, rarely_stories=None, never_stories=None):

            self.name = name
            self.attributes = attributes # 2 very strong attributes by default
#             self.generic_dialogue = generic_dialogue # Disabled. Bool, decides if this personality allows for generic dialogue or not. Custom dialogue should be provided for all relevant situations if set to False.
            if personality_dialogue_only == None: personality_dialogue_only = []
            self.personality_dialogue_only = personality_dialogue_only # A list of topics that will be limited to personality-based dialogue, not generic or attribute-based dialogue.
            self.dialogue_personality_weight = dialogue_personality_weight # Likelihood of using custom personality lines when available
            self.dialogue_attribute_weight = dialogue_attribute_weight # Likelihood of using custom attribute lines when available. Can be set to 0 to avoid all attribute dialogue.
            self.custom_dialogue_label = custom_dialogue_label # For more complex dialogue, a label must be specified. It will receive the 'girl' object and the dialogue 'topic' as arguments.

            if not often_stories: often_stories = []
            if not rarely_stories: rarely_stories = []
            if not never_stories: never_stories = []

            self.story_dict = {"often" : often_stories, "rarely" : rarely_stories, "never" : never_stories}

            self.description = description

            self.generate_gift_likes()

        def generate_gift_likes(self): # Determines gift likes for this personality archetype

            self.gift_likes = {"cute" : 0, "book" : 0, "precious" : 0, "erotica" : -0, "drinks": 0}

            for attr in self.attributes:
                for gift_type, v in gpersonalities_likes[attr].items():
                    self.gift_likes[gift_type] += v

        def generate_attributes(self, girl): # Adds 4 semi-randomized attributes to a girl

            attributes = []

            for attr in self.attributes:
                # Adds mandatory personality attributes
                attributes.append(attr)

                # Important note: for ease of code reasons, both 'very X' and 'X' attributes are added to a girl's attributes.
                if attr.startswith("very "):
                    attributes.append(attr[4:])

                # Checks every pairing and completes the girl's other attributes
                for tup in personality_attributes:
                    if tup[0] in attributes or tup[1] in attributes:
                        pass
                    else:
                        attributes.append(rand_choice(tup))

            return attributes



    # class Personality_old(object):
    #
    #     def __init__(self, name, description, attributes, allies, rivals):
    #
    #         self.name = name
    #         self.description = description
    #         self.attributes = attributes
    #         self.allies = allies
    #         self.rivals = rivals
    #
    #     def has_attributes(self, attr):
    #         if attr == None:
    #             return True
    #
    #         attr = make_list(attr)
    #
    #         for a in attr:
    #
    #             if a not in gpersonality_attributes:
    #                 raise Assertio$nError, "Attribute '" + a + "' not found"
    #
    #             if not (a in self.attributes or "very " + a in self.attributes):
    #                 return False
    #
    #         return True


    class Fixation(object):

        def __init__(self, name, acts, step, frequency = 12.0, tag_list = None, not_list = None, attribute = None, short_name="", cannot_have_neg=None):

            self.name = name
            if short_name:
                self.short_name = short_name
            else:
                self.short_name = self.name
            self.acts = make_list(acts)
            if not cannot_have_neg:
                cannot_have_neg = []
            self.cannot_have_neg = cannot_have_neg
            self.step = step
            self.frequency = frequency
            if not tag_list:
                tag_list = []
            self.tag_list = tag_list
            if not not_list:
                not_list = []
            self.not_list = not_list
            self.attribute = attribute

        def available(self, girl, act=None, type="pos"):

            # Checks if a specific act is covered
            if act and act not in self.acts:
                return False

            # Cannot assign positive fixation which is blocked in _BK.ini
            if type == "pos" and self.name in girl.init_dict["sexual preferences/never_fixations"]:
                return False

#             # Cannot assign positive fixation if girl doesn't have the related attribute
#             if type == "pos" and not girl.is_(self.attribute):
#                 return False

#             # Cannot assign negative fixation if girl has the related attribute
#             if type == "neg" and girl.is_(self.attribute):
#                 return False

            # Checks for incompatible positive/negative fixations
            if type == "neg":
                for pos_fix in girl.pos_fixations:
                    if self.name in pos_fix.cannot_have_neg: # cannot_have_neg is a list
                        return False

            # Cannot assign the same fixation twice
            if self.name in [f.name for f in (girl.pos_fixations + girl.neg_fixations)]:
                return False

            return True

        def get_weight(self, girl, type="pos"):

            freq = self.frequency

            if self.attribute:
                if girl.is_(self.attribute):
                    freq *= 3

            if self.name in girl.init_dict["sexual preferences/favorite_fixations"]:
                freq *= 3
            elif self.name in girl.init_dict["sexual preferences/disliked_fixations"]:
                freq /= 3
            else:
                for act in self.acts:
                    if act in girl.init_dict["sexual preferences/favorite_acts"]:
                        freq *= 2
                    elif act in girl.init_dict["sexual preferences/disliked_acts"]:
                        freq /= 2

            if type == "neg":
                freq = 144/freq # Probably no longer necessary to ensure weight is an integer with the changes to weighted_choice()

#            renpy.say("", str(freq))

            return int(freq)


    class GirlInteractionTopic(object):

        def __init__(self, type, group, caption, label, AP_cost=1, gold_cost=0, act=None, condition=None, advanced=False, love_test=None, relationship_level=0):

            self.type = type # Determines which tab the option belongs to in the interaction menu
            self.group = group # Determines which group the interaction is counted a part of (e.g. all training shares the 'train' group)
            self.caption = caption
            self.label = label
            self.AP_cost = AP_cost
            self.gold_cost = gold_cost
            self.act = act # For training and magic training
            self.advanced = advanced # Determines if advanced options are available
            self.condition = condition
            self.love_test = love_test
            self.relationship_level = relationship_level

        def get_gold_cost(self):
            return self.gold_cost*(district.rank ** 2)

        def is_shown(self, girl): # The option won't display unless the condition is True
            if self.love_test != None:
                if girl.get_love() + MC.get_charisma() >= self.love_test: # a value of 0 for love_test will be used in the test. Give love_test a 'None' value to ignore the test.
                    return True
                else:
                    return False

            if self.relationship_level:
                if girl.MC_relationship_level >= self.relationship_level:
                    return True
                else:
                    return False

            if not self.condition:
                return True
            elif self.condition == "has_worked" and girl.has_worked:
                return True
            elif self.condition == "other_girls" and len(MC.girls) >= 2:
                return True
            elif self.condition == "story" and girl.flags["story"] == 50: #! To do: Make it so that she can repeat earlier parts of the story
                return True
            elif self.condition == "neg_fix":
                neg_fix = [fix.name for fix in girl.neg_fixations if girl.personality_unlock[fix.name]]
                if neg_fix:
                    return True
            elif self.condition == "master_bedroom_add":
                if brothel.master_bedroom.level >= 1 and girl not in brothel.master_bedroom.girls:
                    return True
            elif self.condition == "master_bedroom_remove":
                if girl in brothel.master_bedroom.girls:
                    return True
            elif self.condition == "dressed":
                if girl.get_effect("special", "naked") and not girl.naked:
                    return True
            elif self.condition == "naked":
                if girl.naked:
                    return True
            elif self.condition == "farm":
                if farm.active:
                    return True
            elif self.condition == "debug_mode" and debug_mode:
                return True


            return False

        def is_available(self, girl, mode=None, free=False): # The option will display inactive if False. Returns a tuple with bool and a tooltip description.

            if girl.away:
                return False, "%s不在身边。你无法与她互动。" % girl.fullname

            if self.group == "train":
                if girl.exhausted:
                    return False, "你不能训练%s, 她已经筋疲力尽。" % girl.fullname

                elif girl.hurt > 0:
                    return False, "你不能训练%s, 因为她受伤了。" % girl.fullname

            if mode: # 'mode' is either 'lecture' (Talk), 'train' or advanced.
                if mode == "lecture":
                    pass
                elif mode in ("train", "advanced"):

                    text1 = ""

                    if self.type == "train":
                        if training_test_dict[self.act]:
                            for cond, pref in training_test_dict[self.act]:
                                if compare_preference(girl, cond, pref):
                                    break
                                if text1:
                                    text1 += " or "
                                text1 += cond + " (" + pref + ")"
                            else:
                                return False, "你还不能训练" + girl_related_dict[self.act] + "。要求: " + text1

                    elif self.type == "magic":
                        if magic_training_test_dict[self.act]:
                            for cond, pref in magic_training_test_dict[self.act]:
                                if compare_preference(girl, cond, pref):
                                    break
                                if text1:
                                    text1 += " or "
                                text1 += cond + " (" + pref + ")"
                            else:
                                return False, "你还不能训练" + girl_related_dict[self.act] + "。要求: " + text1

                    if mode == "advanced":
                        if MC.interactions < 2 and not free:
                            return False, "你没有足够的互动留给高级培训。"

                        if not girl.personality_unlock[self.act]:

                        #     pos_reaction, neg_reaction = girl.test_weakness(self.act)
                        #
                        #     if not (pos_reaction or neg_reaction):
                        #         return True, "no reaction"
                        #
                        # else:
                            return False, "你需要至少训练一个女孩一次，才能进入高级训练。"

                elif mode == "master_bedroom_add":
                    if not brothel.master_bedroom.can_have_girl():
                        return False, "主卧室已经满了。"

            if MC.interactions < 1 and self.AP_cost > 0 and not free:
                return False, "你今天已经不能互动了。"
            elif MC.interactions < self.AP_cost and not free:
                return False, "你没有足够的互动时间来做这件事。"
            elif self.get_gold_cost() and MC.gold < self.get_gold_cost():
                return False, "你没有足够的钱来支付这个训练的费用 (" + str(self.get_gold_cost()) + "{image=img_gold})。"
            elif self.group == "train" and girl.MC_interact_counters[self.group] >= 1:
                return False, "你每天只能训练一个女孩一次。"
            elif self.group in ("reward", "discipline") and girl.MC_interact_counters[self.group] >= 1:
                return False, "你每天只能奖励或惩罚一个女孩一次。"
            elif self.group in ("gold", "gift", "sex_reward", "rape", "offer") and girl.MC_interact_counters[self.group] >= 1:
                return False, "你每天只能做一次。"

#            elif self.label == "slave_reward_gold" and girl.MC_interact_counters["gold"] >= 1:
#                return False, "You cannot give her gold more than once per day."
#            elif self.label == "slave_reward_gift" and girl.MC_interact_counters["gift"] >= 1:
#                return False, "You cannot give her a gift more than once per day."
#            elif self.label == "slave_reward_sex" and girl.MC_interact_counters["sex"] >= 1:
#                return False, "You cannot give her a sexual reward more than once per day."
#            elif self.label == "slave_punish_rape" and girl.MC_interact_counters["rape"] >= 1:
#                return False, "You cannot rape her more than once per day."

            elif self.group == "offer" and len(MC.girls) >= brothel.bedrooms:
                return False, "你的青楼里没有空间容纳另一个女孩。"
            elif self.group and girl.MC_interact_counters[self.group] >= 3:
                return False, "你不能和一个女孩每天互动3次以上的" + self.group + "。"
            elif self.label == "slave_master_bedroom_add" and not brothel.master_bedroom.can_have_girl():
                return False, "主人卧室已经满了。"
            return True, ""



    class GirlInteraction(object):

        def __init__(self, girl, topic, mode=None, free=False):

            self.girl = girl
            self.topic = topic
            self.mode = mode
            self.free = free

            if self.free:
                self.cost = 0
            elif self.mode == "advanced":
                self.cost = 2
            else:
                self.cost = 1

            self.type = topic.type # This gets replaced by chat or react type in the course of the interaction (not stricly necessary, but easier to manipulate)
            self.act = topic.act # Can be any of the extended sex acts

            self.response = None # The girl's response. Can be: 'afraid' (failed fear test and too afraid to talk), 'begged', 'accepted' (obeyed request), 'resisted' (shows reluctance), 'refused' (flat-out rejection)
            self.MC_reaction = None # MC's reaction to the girl. Can be: 'love', 'neutral', 'fear' (when removing fixations), 'proceed', 'force', 'warning', 'give up' (if begged, refused or rejected), 'encourage' (chatting), 'discipline' (scold or punish her), 'praise friend', 'demean rival', 'break friendship', 'make peace'
            self.reason = None # Reason for Reward/Punishment. Can be: '', back', or any positive, neutral or negative reason from recent_event_templates
            self.pic = None
            self.score = 0
            self.result = None
            self.other_girl = None
            self.canceled = False

        def resolve(self):

#            renpy.say("", "RESOLVING")

            if self.canceled:
                return

            girl = self.girl

            if debug_mode:
                renpy.call_screen("OK_screen", girl.fullname + "- 互动决定", "群组: [inter.topic.group]\n类型: [inter.type]\n行动: [inter.topic.caption]\n原因: [inter.reason]\n回应: [inter.response]\n行动: [inter.act]\n结果: [inter.result]\n玩家行动: [inter.MC_reaction]")
            else:
                renpy.block_rollback()


            # Charging interactions

            if self.result in ("moderate", "fail") or self.MC_reaction == "give up": # Failed advanced training attempts only cost 1 AP
                MC.interactions -= 1
            else:
                MC.interactions -= self.cost

            # Tracking interaction count
            girl.MC_interact_counters[self.topic.group] += 1

            if topic.type == "react":
                girl.MC_interact_counters["react"] += 1

            # Creating local variables for the stat changes
            m = 0 # mood
            l = 0 # love
            f = 0 # fear
            p = 0 # prestige
            bea = 0 # beauty
            bod = 0 # body
            cha = 0 # charm
            ref = 0 # refinement
            ob = 0 # obedience
            lib = 0 # libido
            sen = 0 # sensitivity
            con = 0 # constitution
            sv = 0 # service
            sx = 0 # sex
            an = 0 # anal
            fe = 0 # fetish
            gd = 0 # good
            ev = 0 # evil
            ne = 0 # neutral
            brk = defaultdict(int) # preferences
            inter = 0 # interactions
            en = 0 # energy
            virgin = False

            if self.topic.type == "chat":

                # In case she is too afraid to talk

                if self.response != "afraid":

                    ## 1. Mood change

                    if self.MC_reaction != "discipline":

                        # Extravert people like chatting

                        if girl.is_("very extravert"):
                            m += 2
                        elif girl.is_("extravert"):
                            m += 1
                        elif girl.is_("very introvert"):
                            m -= 1

                        # Mood improves when chatting (except if punished)

                        m += 1

                    else: # Discipline

                        # Negative impact is stronger on dom girls

                        if girl.is_("very dom"):
                            m -= 2
                        elif girl.is_("dom"):
                            m -= 1
                        elif girl.is_("very sub"):
                            m += 1

                    ## 2. Personality unlocking

                    # Story unlocking, faster if chatting about personal stuff: First step unlocks at 4, then 10, then 20

                    if self.type in ("well_being", "feelings", "tastes", "origins"):
                        girl.personality_unlock["story"] += 1 + 0.1 * MC.get_charisma()
                    else:
                        girl.personality_unlock["story"] += 0.5 + 0.05 * MC.get_charisma()


                    ## 3. Love and fear

                    r = dice(6) + MC.get_charisma()

                    if self.MC_reaction == "encourage": # Idealist girls like to be encouraged

                        m += dice(3)

                        if r >= 6:
                            f -= 1

                        if r >= 9:
                            l += 1

                        if girl.is_("very idealist"):
                            l += 0.5
                            f -= 1
                        elif girl.is_("idealist"):
                            l += 0.25
                            f -= 0.5
                        elif girl.is_("materialist"):
                            f -= 0.25

                    elif self.MC_reaction == "discipline": # Dom girls dislike being disciplined

                        m -= dice(3)

                        if r < 6:
                            l -= 1

                        if r >= 9:
                            f += 1

                        if girl.is_("very sub"):
                            l += 0.5
                            f += 1
                        elif girl.is_("sub"):
                            l += 0.25
                            f += 0.5
                        elif girl.is_("very dom"):
                            l -= 0.5
                        elif girl.is_("dom"):
                            l -= 0.25


                    ## 4. Random skill increases

                    r = dice(6) + MC.get_charisma()

                    if self.type == "slave_life":
                        if r >= 9:
                            ob += 1

                    elif self.type == "brothel":
                        if r >= 9:
                            lib += 1

                    elif self.type == "customers":
                        if r >= 9:
                            sen += 1

                    elif self.type == "other_girls":
                        if r >= 9:
                            cha += 1

                    ## Impact other girls (if necessary)

                    if self.other_girl:

                        r = dice(6) + MC.get_charisma()

                        if self.MC_reaction == "praise friend": # Extraverts and idealists like to be encouraged in their relationships
                            m += dice(3)

                            if r >= 6:
                                f -= 1

                            if r >= 9:
                                l += 1

                            if girl.is_("very extravert"):
                                l += 0.5
                                f -= 1
                            elif girl.is_("extravert"):
                                l += 0.25
                                f -= 0.5
                            elif girl.is_("introvert"):
                                f += 0.5

                            if girl.is_("very idealist"):
                                l += 0.5
                            elif girl.is_("idealist"):
                                l += 0.25
                            elif girl.is_("materialist"):
                                l -= 0.5

                            self.other_girl.change_love(1 * (1+MC.get_charisma()/10))

                        elif self.MC_reaction == "demean rival": # Extraverts and materialists like to be encouraged in their feuds

                            m += dice(3)

                            if r >= 6:
                                f -= 1

                            if r >= 9:
                                l += 1

                            if girl.is_("very extravert"):
                                l += 0.5
                            elif girl.is_("extravert"):
                                l += 0.25
                            elif girl.is_("introvert"):
                                f += 0.5

                            if girl.is_("very materialist"):
                                l += 0.5
                            elif girl.is_("materialist"):
                                l += 0.25
                            elif girl.is_("idealist"):
                                l -= 0.5

                            self.other_girl.change_love(-1 * (1+MC.get_charisma()/10))

                        elif self.MC_reaction == "break friendship": # Extraverts and idealists hate to be discouraged in their relationships

                            m -= dice(6)

                            if r >= 6:
                                l -= 1

                            if r >= 9:
                                f += 1

                            if girl.is_("very extravert"):
                                l -= 2
                                f += 1
                            elif girl.is_("extravert"):
                                l -= 1
                                f += 0.5
                            elif girl.is_("introvert"):
                                l -= 0.5

                            if girl.is_("very idealist"):
                                l -= 2
                                f += 1
                            elif girl.is_("idealist"):
                                l -= 1
                                f += 0.5
                            elif girl.is_("materialist"):
                                f += 0.5

                            girl.change_relationship(self.other_girl, -1 * MC.get_charisma()/3)

                            self.other_girl.change_love(-1)

                        elif self.MC_reaction == "make peace": # Extraverts and materialists don't like to be discouraged in their feuds

                            m -= dice(3)

                            if r >= 6:
                                l -= 1

                            if r >= 9:
                                f += 1

                            if girl.is_("very extravert"):
                                l -= 1
                                f += 0.5
                            elif girl.is_("extravert"):
                                l -= 0.5
                            elif girl.is_("introvert"):
                                f -= 0.5

                            if girl.is_("very materialist"):
                                l -= 1
                                f += 0.5
                            elif girl.is_("materialist"):
                                l -= 0.5
                            elif girl.is_("idealist"):
                                l += 0.5

                            girl.change_relationship(self.other_girl, MC.get_charisma()/3)

                            self.other_girl.change_love(1)


            elif self.topic.type == "train" and self.mode != "lecture": # Non-magical training, excluding lectures

                ## In case she refused training

                r = dice(6) + MC.get_charisma()

                # MC gave up

                if self.MC_reaction == "give up":
                    f -= 1

                    if self.response == "begged":
                        gd += 1

                    elif self.response == "resisted":
                        ev -= 1 # MC gets less evil when not forcing

                        if r <= 6: # Girls may respect the player less
                            ob -= dice(3)

                    if self.response != "refused": # Repressed girls are more relieved when MC gives up
                        if girl.is_("very modest"):
                            l += 1
                            f -= 1
                        elif girl.is_("modest"):
                            l += 0.5
                            f += 0.5
                        else:
                            ob -= 1

                elif self.MC_reaction == "warning": # Warnings work better on sub girls
                    ev -= 1

                    if self.response == "begged":
                        ev -= 1

                    if girl.is_("very sub"):
                        f += 1
                        ob += 2
                    elif girl.is_("sub"):
                        f += 0.5
                        ob += 1
                    elif girl.is_("very dom"):
                        f -= 1
                        ob -= 2
                    elif girl.is_("dom"):
                        f -= 0.5
                        ob -= 1


                # MC got into a fight and lost

                elif self.response == "refused" and self.result == "fail":
                    ev += 1
                    l -= 5
                    f -= 5

                ## If she went on with the training

                else:
                    ## 1. Mood change

                    m -= 1

                    if girl.fear >= girl.love + 10: # She doesn't like interacting with MC
                        m -= 1
                    elif girl.love >= girl.fear + 10: # She likes the MC
                        m += 1

                    if self.MC_reaction == "encourage":
                        m += 1
                    elif self.MC_reaction == "discipline":
                        m -= 1

                    ## 2. Stat changes (normal training)

                    if self.act in ("obedience", "constitution", "lecture"):

                        r = dice(6) + MC.get_charisma()

                        if self.act == "obedience":
                            if self.result == "good":
                                ob += dice(6)
                            elif self.MC_reaction == "discipline": # Scolding her might have a good effect
                                if r >= 9:
                                    ob += dice(3)

                        elif self.act == "constitution":
                            if self.result == "good":
                                con += dice(6)
                            elif self.MC_reaction == "discipline": # Scolding her might have a good effect
                                if r >= 9:
                                    con += dice(3)

                    # 3. Love and fear (sexual training)

                    else:

                        r = dice(6) + MC.get_charisma()

                        if self.response == "accepted": # Lewd girls like consensual sex, repressed girls are reassured

                            f -= 0.5

                            if girl.is_("very lewd"):
                                l += 1
                            elif girl.is_("lewd"):
                                l += 0.5
                            elif girl.is_("very modest"):
                                f -= 1
                            elif girl.is_("modest"):
                                f -= 0.5

                        elif self.response == "resisted": # Dom and repressed girls hate being forced, sub and lewd girls don't mind too much
                            ne += 1

                            f += 1

                            if girl.is_("very dom"):
                                l -= 1
                            elif girl.is_("dom"):
                                l -= 0.5
                            elif girl.is_("very sub"):
                                l += 1
                            elif girl.is_("sub"):
                                l += 0.5

                            if girl.is_("very modest"):
                                f += 1
                            elif girl.is_("modest"):
                                f += 0.5
                            elif girl.is_("very lewd"):
                                f -= 1
                            elif girl.is_("lewd"):
                                f -= 0.5

                        elif self.response == "begged": # If MC ignored her begging
                            gd -= 1

                            if girl.is_("very sub"): # Reminder: Only sub girls may beg
                                l += 1.5
                                f += 1
                            elif girl.is_("sub"):
                                l += 0.5
                                f += 0.5

                            if girl.is_("very modest"):
                                f += 1
                            elif girl.is_("modest"):
                                f += 0.5
                            elif girl.is_("very lewd"):
                                f -= 1
                            elif girl.is_("lewd"):
                                f -= 0.5

                        elif self.response == "refused": # Dom and repressed girls hate being forced. Very sub and very lewd girls kind of like it
                            ev += 1

                            f += 3

                            if girl.is_("very dom"):
                                l -= 2
                            elif girl.is_("dom"):
                                l -= 1
                            elif girl.is_("very sub"):
                                l += 0.5

                            if girl.is_("very modest"):
                                f += 2
                            elif girl.is_("modest"):
                                f += 1
                            elif girl.is_("very lewd"):
                                f -= 1

                        # Obedience may increase during s. training

                        if r >= 9:
                            ob += dice(3)
                        elif r >= 6:
                            ob += 1

            elif self.topic.type == "magic": # Magical training

                if self.result == "success": # Note: stat changes and breaking handled with sex act results below

                    if girl.magic_training == "positive":
                        l += 1
                    elif girl.magic_training == "negative":
                        f += 1

                    if self.act == "obedience":
                        ob += dice(6)
                    elif self.act == "libido":
                        lib += dice(6)
                    elif self.act == "sensitivity":
                        sen += dice(6)

                elif self.result == "moderate": # Breaking handled here (no sex happens)

                    if girl.magic_training == "positive":
                        l += 0.5
                    elif girl.magic_training == "negative":
                        f += 0.5

                    if self.act == "obedience":
                        ob += dice(3)
                    elif self.act == "libido":
                        lib += dice(3)
                    elif self.act == "sensitivity":
                        sen += dice(3)
                    else:
                        if girl.magic_training == "positive":
                            brk[self.act] += girl.raise_preference(self.act, "love", 0.75)
                        elif girl.magic_training == "negative":
                            brk[self.act] += girl.raise_preference(self.act, "fear", 0.75)
                        else:
                            brk[self.act] += girl.raise_preference(self.act, None, 0.75)

                # Magic failure

                else:
                    if girl.is_("very dom"):
                        l -= 1
                    elif girl.is_("dom"):
                        l -= 0.5
                    elif girl.is_("very sub"):
                        f += 1
                    elif girl.is_("sub"):
                        f += 0.5

            elif self.topic.type == "react" and self.type in ("praise", "gold", "gift", "pet", "day off", "sex"):

                ## 1. Personality unlocking

#                 if self.type == "pet" or self.type == "day off":
#                     unlock = "DS"
#                 elif self.type == "sex":
#                     unlock = "LM"
#                 elif self.type == "praise" or self.type == "gold" or self.type == "gift":
#                     unlock = "MI"
#                 else:
#                     raise AssertionError, "Type not found. Type is " + str(self.type)

#                 girl.personality_unlock[unlock] += 15 + MC.get_charisma() + dice(10) # Temp, see how it behaves


                ## 2. Mood, love and fear changes: A score is calculated according to the impact and result of the interaction

                m += self.score
                l += self.score
                f -= self.score

                if self.score >= 1: # Fear diminishes faster for dom girls
                    if girl.is_("very dom"):
                        f -= 1
                    elif girl.is_("dom"):
                        f -= 0.5
                    elif girl.is_("very sub"):
                        f += 1
                    elif girl.is_("sub"):
                        f += 1

#                 if self.type == "praise": # More efficient for idealist girls
#                     if girl.is_("very idealist"):
#                         l += 1
#                     elif girl.is_("idealist"):
#                         l += 0.5
#                     elif girl.is_("very materialist"):
#                         l -= 1
#                     elif girl.is_("materialist"):
#                         l -= 0.5

#                 elif self.type == "gold": # More efficient for materialist girls
#                     if girl.is_("very materialist"):
#                         l += 1
#                     elif girl.is_("materialist"):
#                         l += 0.5
#                     elif girl.is_("very idealist"):
#                         l -= 1
#                     elif girl.is_("idealist"):
#                         l -= 0.5

                if self.type == "gift": # Good for all girls
                        l += 1

#                 elif self.type == "pet": # More efficient for sub girls
#                     if girl.is_("very sub"):
#                         l += 1
#                     elif girl.is_("sub"):
#                         l += 0.5
#                     elif girl.is_("very dom"):
#                         l -= 1
#                     elif girl.is_("dom"):
#                         l -= 0.5

#                 elif self.type == "day off": # More efficient for dom girls
#                     if girl.is_("very dom"):
#                         l += 1
#                     elif girl.is_("dom"):
#                         l += 0.5
#                     elif girl.is_("very sub"):
#                         l -= 1
#                     elif girl.is_("sub"):
#                         l -= 0.5

                else: # Sexual reward
#                     if self.response == "accepted":
#                         if girl.is_("very lewd"):
#                             l += 2
#                         elif girl.is_("lewd"):
#                             l += 1
#                         elif girl.is_("modest"):
#                             f -= 1

                    if self.response == "resisted":
                        ne += 1

#                         if girl.is_("very dom"):
#                             l -= 2
#                         elif girl.is_("dom"):
#                             l -= 1
#                         elif girl.is_("very sub"):
#                             l += 1
#                         elif girl.is_("sub"):
#                             l += 0.5

                        if girl.is_("very modest"):
                            l -= 1
                            f += 1
                        elif girl.is_("modest"):
                            l -= 0.5
                            f += 0.5

                    elif self.response == "refused": # (forced) --> Score is then set to zero
                        ev += 1

                        if girl.is_("very dom"):
                            l -= 2
                        elif girl.is_("dom"):
                            l -= 1
                        elif girl.is_("very sub"):
                            l += 0.5

                        if girl.is_("very modest"):
                            f += 3
                        elif girl.is_("modest"):
                            f += 2
                        else:
                            f += 1

                # Justify effect

                if self.reason: # Idealist girls like fairness
                    if girl.is_("very idealist"):
                        l += 1
                    elif girl.is_("idealist"):
                        l += 0.5
                    elif girl.is_("very materialist"):
                        l -= 0.5

                    ob += self.score

                else: # Materialist girls like to be rewarded for no reason
                    if girl.is_("very materialist"):
                        l += 1
                    elif girl.is_("materialist"):
                        l += 0.5
                    elif girl.is_("very idealist"):
                        l -= 0.5

                ## 3. Remember this

                girl.will_remember("reward", self.reason, self.score)

                ## 4. Spoil her

                if self.reason:
                    girl.spoil(self.score)
                else:
                    girl.spoil(3*self.score)


            elif self.topic.type == "react" and self.type in ("scold", "upkeep", "naked", "beat", "rape", "farm"):

                # This happens if a sub girl begs for mercy and MC complies
                if self.MC_reaction == "give up":
                    ev -= 1
                    f -= 1
                    ob -= dice(6)
                elif self.MC_reaction == "warning":
                    ne += 1
                    ob -= dice(3)
                else:
                    ## 1. Personality unlocking

                    if self.MC_reaction == "proceed": # Punishment is especially efficient is girl begged and was denied
                        self.score *= 1.5
                        ev += 1

#                     if self.type == "beat" or self.type == "farm":
#                         unlock = "DS"
#                     elif self.type == "naked" or self.type == "rape":
#                         unlock = "LM"
#                     elif self.type == "scold" or self.type == "upkeep":
#                         unlock = "MI"
#                     else:
#                         raise AssertionError, "Type not found. Type is " + str(self.type)

#                     girl.personality_unlock[unlock] += 15 + MC.get_charisma() + dice(10) # Temp, see how it behaves

                    ## 2. Mood, love and fear changes

                    m -= self.score
                    l -= self.score
                    f += self.score
                    ob += self.score

                    if self.score > 0: # Fear increases faster for sub girls
                        if girl.is_("very dom"):
                            f -= 1
                        elif girl.is_("dom"):
                            f -= 0.5
                        elif girl.is_("very sub"):
                            f += 1
                        elif girl.is_("sub"):
                            f += 1

#                     if self.type == "scold": # Idealist girls care more about it
#                         if girl.is_("very idealist"):
#                             f += 1
#                         elif girl.is_("idealist"):
#                             f += 0.5
#                         elif girl.is_("very materialist"):
#                             f -= 1
#                         elif girl.is_("materialist"):
#                             f -= 0.5

#                     elif self.type == "upkeep": # Hurts materialist girls more
#                         if girl.is_("very materialist"):
#                             f += 1
#                         elif girl.is_("materialist"):
#                             f += 0.5
#                         elif girl.is_("very idealist"):
#                             f -= 1
#                         elif girl.is_("idealist"):
#                             f -= 0.5

                    if self.type == "beat": # Scares sub girls more
                        gd -= 1

#                         if girl.is_("very sub"):
#                             f += 1
#                         elif girl.is_("sub"):
#                             f += 0.5
#                         elif girl.is_("very dom"):
#                             f -= 1
#                         elif girl.is_("dom"):
#                             f -= 0.5

#                     elif self.type == "naked": # Repressed girls care more
#                         if girl.is_("very modest"):
#                             f += 1
#                         elif girl.is_("modest"):
#                             f += 0.5
#                         elif girl.is_("very lewd"):
#                             f -= 1
#                         elif girl.is_("lewd"):
#                             f -= 0.5

                    elif self.type == "rape": # Sexual punishment (forced)

                        ev += 1

                        if girl.is_("very dom"):
                            l -= 2
                        elif girl.is_("dom"):
                            l -= 1
                        elif girl.is_("very sub"):
                            l += 0.5

#                         if girl.is_("very modest"):
#                             f += 3
#                         elif girl.is_("modest"):
#                             f += 2
#                         else:
#                             f += 1

#                         if self.result == "neg_fix":
#                             l -= 2
#                             f += 3
#                         elif self.result == "pos_fix":
#                             l += 1
#                             f -= 1

                    elif self.type == "farm": # More effective on dom girls, sub girls are somewhat less affected
                        gd -= 1

#                         if girl.is_("very dom"):
#                             f += 1
#                         elif girl.is_("dom"):
#                             f += 0.5
#                         elif girl.is_("very sub"):
#                             f -= 1
#                         elif girl.is_("sub"):
#                             f -= 0.5


                    ## 3. Justify effect

#                     if self.reason: # Idealist girls like fairness
#                         if girl.is_("very idealist"):
#                             f -= 1
#                             ob += 1
#                         elif girl.is_("idealist"):
#                             f -= 0.5
#                             ob += 0.5
#                         elif girl.is_("very materialist"):
#                             f += 0.5
#                             ob -= 0.5

#                     else: # Idealist girls hate to be punished for no reason
#                         if girl.is_("very idealist"):
#                             l -= 1
#                             ob -= 1
#                         elif girl.is_("idealist"):
#                             l -= 0.5
#                             ob -= 0.5
#                         elif girl.is_("very materialist"):
#                             l += 0.5
#                             ob += 0.5


                ## 4. Remembering and terrify effect (applies regardless of whether the punishment was given or not)

                # Remember this

                girl.will_remember("punish", self.reason, self.score)

                # Terrify her

                if self.reason:
                    girl.terrify(self.score)
                else:
                    girl.terrify(3*self.score)


            ## SEX STAT CHANGES

            # Random skill increases

            if self.act in extended_sex_acts:

                if self.mode == "lecture": # Results of lectures are handled here (not in sexual training)

                    # Mood and love change
                    if (girl.is_("very lewd") and compare_preference(girl, self.act, "a little reluctant")) or (girl.is_("lewd") and compare_preference(girl, self.act, "a little interested")):
                        l += 2
                        m += 2
                    elif (girl.is_("very lewd") and compare_preference(girl, self.act, "very reluctant")) or (girl.is_("lewd") and compare_preference(girl, self.act, "reluctant")):
                        m += 1
                    elif (girl.is_("very modest") and compare_preference(girl, self.act, "a little interested")) or (girl.is_("modest") and compare_preference(girl, self.act, "a little reluctant")):
                        m -= 1
                    elif (girl.is_("very modest") and compare_preference(girl, self.act, "reluctant")) or (girl.is_("modest") and compare_preference(girl, self.act, "very reluctant")):
                        l -= 2
                        m -= 2

                    if (girl.get_love() - girl.get_fear()) // 10 >= 0:
                        mod = "love"
                    else:
                        mod = "fear"

                    if self.score > 0:
                        brk[self.act] += girl.raise_preference(self.act, mod, 1.25)

                    elif self.score == 0:
                        brk[self.act] += girl.raise_preference(self.act, mod, 0.75)

                    else:
                        brk[self.act] += girl.raise_preference(self.act, mod, 0.25)

                elif self.topic.label == "slave_remove_fixation":
                    if not self.MC_reaction == "give up":
                        if self.result != "locked": # Modest break even if training fails
                            brk[self.act] + girl.raise_preference(self.act, self.MC_reaction, 0.5)
                        else: # Negative break if fix is locked
                            brk[self.act] + girl.raise_preference(self.act, self.MC_reaction, -1)

                        # Prestige

                        if self.act == "naked":
                            p += girl.rank / 2
                        else:
                            p += girl.rank


                else:

                    if not (self.MC_reaction in ("give up", "warning") or self.result in ("fail", "fled", "moderate")):
                        # All sex training costs energy

                        if self.act == "naked":
                            en = -5

                            lib += dice(6)

                            d = dice(6)

                            if d >= 6:
                                ob += dice(3)
                            elif d >= 5:
                                bea += dice(3)
                            elif d >= 4:
                                bod += dice(3)

                        elif self.act == "service":
                            en = -7

                            sv += dice(6)

                            d = dice(6)

                            if d >= 5:
                                sen += dice(3)
                            elif d >= 4:
                                cha += dice(3)

                        elif self.act == "sex":
                            en = -9

                            sx += dice(6)

                            d = dice(6)

                            if d >= 5:
                                lib += dice(3)
                            elif d >= 4:
                                bea += dice(3)

                        elif self.act == "anal":
                            en = -11

                            an += dice(6)

                            d = dice(6)

                            if d >= 5:
                                con += dice(3)
                            elif d >= 4:
                                bod += dice(3)

                        elif self.act == "fetish":
                            en = -13

                            fe += dice(6)

                            d = dice(6)

                            if d >= 5:
                                ob += dice(3)
                            elif d >= 4:
                                ref += dice(3)

                        elif self.act == "bisexual":
                            en = -9

                            if dice(6) >= 4:
                                sx += dice(6)
                            else:
                                sv += dice(6)

                            d = dice(6)

                            if d >= 5:
                                sen += dice(3)
                            elif d >= 4:
                                lib += dice(3)

                        elif self.act == "group":
                            en = -15

                            d = dice(6)

                            if d >= 5:
                                sv += dice(6)
                            elif d >= 3:
                                sx += dice(6)
                            else:
                                an += dice(6)

                            d = dice(6)

                            if d >= 5:
                                con += dice(3)
                            elif d >= 4:
                                ob += dice(3)

                        # Breaking (Warning: lecture breaking is handled above)

                        if self.topic.type == "magic": # Moderate magic results are handled above
                            if girl.magic_training == "positive":
                                brk[self.act] += girl.raise_preference(self.act, "love", 2)
                            elif girl.magic_training == "negative":
                                brk[self.act] += girl.raise_preference(self.act, "fear", 2)
                            else:
                                brk[self.act] += girl.raise_preference(self.act, None, 2)

                        elif self.response == "accepted":
                            brk[self.act] += girl.raise_preference(self.act, "love", 2)

                        elif self.response == "resisted":
                            if girl.is_("very sub"):
                                brk[self.act] += girl.raise_preference(self.act, "fear", 1.5)
                            elif girl.is_("sub"):
                                brk[self.act] += girl.raise_preference(self.act, "fear", 1)
                            elif girl.is_("very dom"):
                                brk[self.act] += girl.raise_preference(self.act, "fear", 0)
                            elif girl.is_("dom"):
                                brk[self.act] += girl.raise_preference(self.act, "fear", 0.5)

                        elif self.response == "refused":
                            if girl.is_("very sub"):
                                brk[self.act] += girl.raise_preference(self.act, "fear", 2.5)
                            elif girl.is_("sub"):
                                brk[self.act] += girl.raise_preference(self.act, "fear", 2)
                            elif girl.is_("very dom"):
                                brk[self.act] += girl.raise_preference(self.act, "fear", -2)
                            elif girl.is_("dom"):
                                brk[self.act] += girl.raise_preference(self.act, "fear", -1)

                        else:
                            brk[self.act] += girl.raise_preference(self.act, None, 2)

                        # Prestige

                        if self.act != "naked":
                            brk["naked"] += girl.raise_preference("naked", None, 1) # Naked acts rise with other sex acts
                            p += girl.rank
                            girl.add_log("perform " + self.act)

                        if self.act in ("sex", "group"):
                            if girl.pop_virginity(origin="MC"):
                                virgin = True
                                p += 3 * girl.rank


            ## Apply changes

            changes = [("mood", m), ("love", l), ("fear", f), ("beauty", bea), ("body", bod), ("charm", cha), ("refinement", ref), ("obedience", ob), ("sensitivity", sen), ("constitution", con), ("libido", lib), ("service", sv), ("sex", sx), ("anal", an), ("fetish", fe), ("energy", en)]

#            renpy.say("", "love value:" + str(l))

            text1 = "{size=-2}"
            text2 = ""

            for s, v in changes: # Charisma impacts all changes

                if s == "energy":
                    c = girl.change_stat(s, v)
                    shown = str(round_int(c))
                else:
                    c = girl.change_stat(s, v * (1 + (MC.get_charisma()/10)))
                    shown = get_plus_rating(c)

                if debug_mode: # Always show precise numbers in debug mode
                    shown = str(round_int(c))

                if v != 0 and c != 0:
                    text2 += "\n" + s.capitalize() + ": " + shown

                    if s in ("mood", "love", "fear"):
                        if s=="mood":
                            s="情绪"
                        if s=="love":
                            s="爱情"
                        if s=="fear":
                            s="恐惧"
                        text1 = "{b}" + s + "{/b}"
                    else:
                        text1 = "{b}" + s + "技能" + "{/b}"

                    if c >= 5:
                        renpy.say("", girl.name + "的" + text1 + "增加了很多。")

                    elif c >= 3:
                        renpy.say("", girl.name + "的" + text1 + "增加了。")

                    elif c >= 1:
                        renpy.say("", girl.name + "的" + text1 + "增加了一丢丢。")

                    elif c <= -5:
                        renpy.say("", girl.name + "的" + text1 + "降低了很多。")

                    elif c <= -3:
                        renpy.say("", girl.name + "的" + text1 + "减少了。")

                    elif c <= -1:
                        renpy.say("", girl.name + "的" + text1 + "降低了少许。")

            text2 += "\n"

            for a in brk.keys():
                if brk[a] != None:
                    if debug_mode:
                        shown = str(round_int(brk[a]))
                    else:
                        shown = get_plus_rating(brk[a], "pref")

                    text1 += "\n喜好: " + shown
                else:
                    raise AssertionError, "Unexpected breaking value for " + a + ". Please report this bug."

            if inter:
                text1 += "\n女孩的互动关系: " + str(inter)
                girl.interactions += inter

            if virgin:
                text1 += "\n" + girl.fullname + "的一血是你拿的哟。"

            text1 += "\n"

            if gd:
                MC.good += gd
                text2 += "\n善良: " + str(gd)
            if ne:
                MC.neutral += ne
                text2 += "\n中立: " + str(ne)
            if ev:
                MC.evil += ev
                text2 += "\n邪恶: " + str(ev)
            if p:
                MC.change_prestige(p)
                text2 += "\n声望: " + str(p)
                renpy.say("", "你赢得了声望。")

            if debug_mode:
                if gd:
                    text2 += "\n善良: " + str(gd)
                if ne:
                    text2 += "\n中立: " + str(ne)
                if ev:
                    text2 += "\n邪恶: " + str(ev)
            if p:
                MC.change_prestige(p)
                text1 += "\n声望: " + str(p)

            if not text2:
                text2 = "No 没有变化"
            renpy.call_screen("OK_screen", girl.fullname + " - 互动结果", text2, dark=True, pic=girl.portrait, always_scrollbar=True)

            return



    class GirlRecentEvent(object):

        def __init__(self, type, action=None, base_description="", encourage=True, discipline=True):

            self.type = type
            self.action = action
            self.base_description = base_description
            self.description = ""
            self.encourage = encourage
            self.discipline = discipline

            self.time = 0
            self.rewarded = 0
            self.punished = 0

        def reward(self, score):

            self.rewarded += score

            if self.rewarded > 10:
                self.rewarded = 10

        def punish(self, score):

            self.punished += score

            if self.punished > 10:
                self.punished = 10

        def refresh(self):
            if self.rewarded > 0:
                self.rewarded -= 1
            if self.punished > 0:
                self.punished -= 1


    class Mod(object):

        """This class is used to track external mods. Mods are declared in their respective rpy files, and automatically added to 'detected_mods' upon creation."""

        def __init__(self, name, folder, creator="Unknown", version= 1.0, pic=None, description="This is a mod for Brothel King.", help_prompts=None, init_label="", night_label = "", update_label = "", home_rightmenu_add_buttons=None, events=None):

            #### Init variables
            self.name = name
            self.path = "mods/" + folder + "/"
            self.creator = creator
            self.version = version
            if pic:
                self.pic = Picture(pic, self.path + pic)
            else:
                self.pic = None
            self.description = description
            self.full_name = name + " v" + str(self.version) + ", 作者:" + creator

            ## help_prompts is a list of tuples (name, label), each representing a menu prompt in the 'help/mod/mod options' menu.
            ## 'name' is the prompt message as it appears on the menu button, and 'label' is the target label it will call (not jump).
            ## Several actions can be added to the list by adding tuples (name, label) to the list, each separated by a comma
            self.help_prompts = []
            ## Adds [mod name] to prompt messages for clarity
            if help_prompts:
                for prompt in help_prompts:
                    self.help_prompts.append(("[[" + self.name + "] " + prompt[0], prompt[1]))

            ## Init label: This will run when the mod is started, allowing to set some variables and events if necessary
            self.init_label = init_label
            self.night_label = night_label
            self.update_label = update_label

            ## Event dictionary (all mod events must be declared here)
            if events == None: events = {}
            self.events = events

            ## Add home right menu buttons
            if home_rightmenu_add_buttons == None: home_rightmenu_add_buttons = []
            self.home_rightmenu_add_buttons = home_rightmenu_add_buttons

            #### Default variables
            self.flags = defaultdict(bool)

            for ev in self.events.values():
                ev.mod = self

            detected_mods[self.name] = self
            self.seen = False
            self.active = False

        def get_check(self): # Returns a list of values used for comparison
            return (self.version, self.path, self.init_label, len(self.events))

        def check_for_updates(self): # Checks a list of values used for comparison with existing mods

            global mod_traceback

            if self.get_check() != persistent.mods[self.name]["check"]:
#                mod_traceback += "Checked " + str(self.get_check()) + " against " + str(persistent.mods[self.name]["check"])
                return True
            return False

        def activate(self):
            if renpy.call_screen("yes_no", "是否要激活" + self.full_name + "？"):
                if not self.active or not persistent.mods[self.name]["active"]:
                    self.active = True
                    persistent.mods[self.name]["active"] = True
                    renpy.notify(self.name + "已经被激活。")
                    reset_updated_games()

                else:
                    renpy.notify(self.name + "已处于激活状态。")

        def deactivate(self):
            if renpy.call_screen("yes_no", "是否确实要停用" + self.full_name + "？这可能会对打开此mod时保存的游戏产生负面影响。"):
                if self.active or persistent.mods[self.name]["active"]:
                    self.active = False
                    persistent.mods[self.name]["active"] = False
                    renpy.notify(self.name + "已停用。")
                    reset_updated_games()
                else:
                    renpy.notify(self.name + "在激活的mod中找不到。")

        def add_event(self, event_name, type=None, date=None, delay=1, call_args=None): # event_name is the event label (not object). date is the exact calendar date. If not provided, current time + delay is used instead (D+1 by default).

            if call_args:
                self.events[event_name].call_args = call_args

            if type:
                self.events[event_name].type = type
            else:
                type = self.events[event_name].type

            if type == "alarm":
                if not date:
                    date = calendar.time + delay
                calendar.set_alarm(date, self.events[event_name])

                if date <= calendar.time:
                    renpy.say("System", "警告: 事件设置为过去的日期. 更改事件时间或延迟。")

            elif type in ("morning", "day", "night"):
                daily_events.append(self.events[event_name])

            elif type == "city":
                city_events.append(self.events[event_name])

        def set_condition(self, condition, value):
            self.flags[condition] = value

    class MC_challenge(object):
        """This class is used to run Player challenges and return a result."""

        def __init__(self, name, stat, opposed):

            self.name = name
            self.pic = Picture(name + ".jpg", "UI/challenges/" + name + ".jpg")
            self.stat = stat
            self.opposed = opposed
            self.d = 0 # stores the latest MC dice roll
            self.d_op = 0 # stores the latest opponent dice roll

            self.score = 0 # stores the latest MC score
            self.score_op = 0 # stores the latest opponent score

            self.result = 0 # stores the result of the latest challenge

        def get_pic(self, x, y):
            return self.pic.get(x, y)

        def get_score(self, diff, bonus=0, opponent_bonus=0, dice_faces=6, dice_nb = 1, raw=False):

            self.score = MC.get_stat(self.stat, raw=raw) + MC.get_effect("change", self.name + " challenges")

            self.d = dice(dice_faces, dice_nb)
            self.score += self.d + bonus

            if self.opposed:
                self.d_op = dice(dice_faces, dice_nb)
                self.score_op = diff + self.d_op + opponent_bonus

                result = self.score - self.score_op

            else:
                result = self.score - diff

            return result

        def adjust_diff(self, diff): # Adds 3 to difficulty if test is unopposed.
            if not self.opposed:
                return diff + 3
            return diff

        def run(self, diff, score=False, raw=False, bonus=0, opponent_bonus=0, dice_faces=6, dice_nb = 1, strict=False, forced=False): # Forced can be 'True' or an integer

            if forced:
                return forced
            elif not score:
                return self.run_pass(diff, bonus, opponent_bonus, dice_faces, dice_nb, raw, strict)
            else:
                return self.get_score(diff, bonus, opponent_bonus, dice_faces, dice_nb, raw)

        def run_pass(self, diff, bonus=0, opponent_bonus=0, dice_faces=6, dice_nb=1, raw=False, strict=False): # This test returns pass or fail. strict tests require a strictly superior result to succeed.

            self.result = self.get_score(diff, bonus, opponent_bonus, dice_faces, dice_nb, raw)

            if self.result > 0:
                return True
            elif self.result < 0:
                return False
            elif strict:
                return False
            else:
                return True

        def estimate_diff(self, diff, raw=False, score=False, bonus=0, opponent_bonus=0, strict=False, percentage=False, forced=False): # Returns difficulty as a qualifier or percentage

            if forced:
                return "Safe"

            differential = (diff + opponent_bonus) - (MC.get_stat(self.stat, raw) + bonus) + MC.get_effect("change", self.name + " challenges", randomize=False)

            if not strict:
                differential -= 1

            if not self.opposed:
                chance = 1.0 - (differential)/6.0
            else:
                for d, c in [(5, 0.0), (4, 0.03), (3, 0.08), (2, 0.17), (1, 0.28), (0, 0.42), (-1, 0.58), (-2, 0.72), (-3, 0.83), (-4, 0.92), (-99, 1.0)]:
                    if differential >= d:
                        chance = c
                        break
                else:
                    raise AssertionError("Couldn't process differential during MC challenge.")

            if percentage:
                return str(int(chance*100)) + "%"

            else:
                if chance >= 1.0 and not score:
                    return "不可能输"
                elif chance > 0.8:
                    return "非常容易"
                elif chance > 0.6:
                    return "容易"
                elif chance > 0.4:
                    return "一般"
                elif chance > 0.2:
                    return "困难"
                elif chance > 0.0:
                    return "非常困难"
                else:
                    return "不可能赢"

    class Resource(object):

        """Resources are sold at the market and extracted in the city. They serve primarily for furniture and city events."""

        def __init__(self, name, rank, stat=None, sound=s_gold, description="", location=None):
            self.name = name
            self.rank = rank
            self.stat = stat
            self.pic = Picture(name + ".webp", "UI/resources/" + name + ".webp")
            self.sound = sound
            self.description = description
            self.location = location

        def get_pic(self, x, y):
            return self.pic.get(x, y)

        def activate_extractor(self):
            auto_extractors[self.name] = True
            auto_extractors[self.name + " ON"] = True
            auto_extractors[self.name + " durability"] = 150
            self.location.menu = (self.location.menu[0] + " [[E]", self.location.menu[1])

        def deactivate_extractor(self):
            auto_extractors[self.name] = False
            auto_extractors[self.name + " ON"] = False
            self.location.menu = (self.location.menu[0][:-5], self.location.menu[1])


    class Furniture(object):

        """Furniture are upgrades for the brothel that provide permanent bonuses."""

        def __init__(self, name, type, pic=None, rank=2, chapter=2, cost=None, duration=0, effects=None, base_description="", upgrade=False, can_deactivate=False):
            self.name = name
            self.type = type
            if pic:
                self.pic = Picture(pic, "items/furniture/" + pic)
            else:
                self.pic = Picture("misc.webp", "items/misc/misc.webp")
            self.rank = rank # This is the rank at which the furniture becomes available
            self.chapter = chapter # This is the chapter at which the furniture becomes available (if not rank)
            if cost == None: cost = []
            self.cost = cost # Cost is a list of tuples (resource=str, amount=int)

            # Sort resources in same order
            self.cost.sort(key = lambda x: build_resources.index(x[0]))

            self.duration = duration
            if effects == None: effects = []
            self.effects = effects
            self.description = "{b}" + furniture_name_dict[self.name] + "{/b}" + ": " + get_description(base_description, effects)
            self.upgrade = upgrade
            self.built = False
            self.can_deactivate = can_deactivate
            self.active = False

        def get_pic(self, x, y):
            return self.pic.get(x, y)

        def can_build(self):
            if brothel.current_building == self:
                return False
            elif self.built or (self.rank > district.rank) or (self.chapter > game.chapter):
                return False
            elif self.upgrade:
                if not furniture_dict[self.upgrade].built:
                    return False
            return True

        def start_building(self):
            if self.duration:
                if not story_flags["carpenter first build"]:
                    calendar.set_alarm(calendar.time+1, StoryEvent(label="iulia1", type="morning"))
                    story_flags["carpenter first build"] = True
                calendar.set_alarm(calendar.time + self.duration, StoryEvent(label = "furniture_built", call_args=[self]))
                brothel.current_building = self
                brothel.started_building = calendar.time
                renpy.say(carpenter, "我会在" + str(self.duration) + "天内完成。我相信你会对结果满意的。")
            else:
                self.build()

        def build(self, message=True):
            self.built = True
            if self not in brothel.furniture:
                brothel.furniture.append(self)
            if self.upgrade:
                if furniture_dict[self.upgrade] in brothel.furniture:
                    brothel.furniture.remove(furniture_dict[self.upgrade])
                brothel.deactivate_furniture(furniture_dict[self.upgrade])
                if message:
                    renpy.call_screen("OK_screen", title = "家具升级", message = self.upgrade + "已经升级到" + self.name + "了。\n\n" + self.description, pic = self.pic, pic_size = "large")
            elif message:
                renpy.call_screen("OK_screen", title = "家具制造", message = "一个新的" + self.name + "已经建成了。\n\n" + self.description, pic = self.pic, pic_size = "large")
            self.activate()
            test_achievement("furniture")

        def destroy(self, message=True):
            self.built = False
            if self in brothel.furniture:
                brothel.furniture.remove(self)
            self.deactivate()
            if self.upgrade:
                brothel.furniture.append(furniture_dict[self.upgrade])
                brothel.activate_furniture(furniture_dict[self.upgrade])
                if message:
                    renpy.call_screen("OK_screen", title = "家具升级", message = self.name + "已被销毁并替换为" + self.upgrade, pic = self.pic, pic_size = "large")
            elif message:
                renpy.call_screen("OK_screen", title = "家具被毁", message = self.name + "已被销毁。", pic = self.pic, pic_size = "large")
            self.activate()

        def activate(self):
            if not self.active and self.built:
                self.active = True
                update_effects()
                return True
            return False

        def deactivate(self):
            if self.active:
                self.active = False
                update_effects()
                return True
            return False

        def toggle(self):
            if self.active:
                self.deactivate()
            else:
                self.activate()

        def describe_cost(self):
            dlist = [(str(amount) + " " + resource_name_dict[resource]) for resource, amount in self.cost]

            return and_text(dlist)


    class Moon(object):

        """A new Moon appears every month. They have an effect on gameplay."""

        def __init__(self, name, pic, effects=None, description="", sound=None):
            self.name = name.capitalize() + "月"
            self.pic = Picture(pic + ".webp", "backgrounds/moons/" + pic + ".webp")
            if effects == None: effects = []
            self.effects = effects
            self.short_description = get_description(self.name, self.effects, separator=": ")
            self.description = get_description(description, self.effects)
            self.sound = sound

        def get_pic(self, x, y):
            return self.pic.get(x, y)


    class Loan(object):

        """A loan is a sum that must be paid back to the banker, with or without interest"""

        def __init__(self, amount, interest=0, duration=10): # Where interest is a float (interest_rate)
            self.amount = amount
            self.initial_amount = amount
            self.interest = interest
            self.duration = duration
            self.total_cost = int(amount * (1+interest))
            self.daily_cost = int(self.total_cost / duration)

        def repay(self):
            amount_reimbursed = get_change_min_max(self.amount, -self.initial_amount/self.duration, 0)
            interest_reimbursed = amount_reimbursed * self.interest

            MC.gold += int(amount_reimbursed + interest_reimbursed)
            self.amount += amount_reimbursed

            return -int(amount_reimbursed + interest_reimbursed)


## Achievement and Contract classes

init -2 python:
    class Achievement(object):

        def __init__(self, title="我的成就:\n做得好，兄弟！", description="没有描述", pic="misc.webp", pic_path="UI/achievements/", level_nb=1, target="", requirements="default", requirements2=None): # {1 : C, 2 : B, 3 : A, 4 : S, 5 : X}

            self.title = title
            self.description = description
            if pic_path[-1] != "/": pic_path += "/"
            self.pic = Picture(path = pic_path + pic)
            self.level_nb = level_nb
            self.target = target
            if requirements == "default": requirements = {1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5}
            self.requirements = requirements
            self.requirements2 = requirements2

            try: # Value has been stored in persistent
                self.level = persistent.achievements[self.target]
            except: # Value doesn't exist
                self.level = 0
                persistent.achievements[self.target] = 0

        def test(self): # Checks if the achievement is unlocked according to its target and requirements

            if not game.achievements:
                return False

            if self.level >= self.level_nb:
                return False

            r = 0

            if self.target == "slaves":
                r = len(MC.girls) + len(farm.girls)

            elif self.target == "gold":
                r = MC.gold

            elif self.target == "rep":
                r = brothel.rep

            elif self.target == "income":
                try:
                    r = logs[calendar.time].net
                except:
                    r = 0

            elif self.target == "losses":
                try:
                    r = -1 * logs[calendar.time].net
                except:
                    r = 0

            elif self.target == "friends":
                r = sum(1 for girl in MC.girls + farm.girls if girl.friends)

            elif self.target == "rivals":
                r = sum(1 for girl in MC.girls + farm.girls if girl.rivals)

            elif self.target == "girlfriends":
                for girl in game.free_girls:
                    if girl.MC_relationship_level >= 3:
                        r += 1

            elif self.target == "originals":
                r = sum(1 for girl in MC.girls if girl.original)

            elif self.target == "furniture": #!
                if not brothel.can_build_anything(max_chapter=self.level+2): # Checks if furniture can be built one chapter at a time (from chapter 2 to chapter 7)
                    return self.unlock(game.chapter-1) # Unlocking capped by chapter (may be unnecessary)

            elif self.target == "upgrades":
                if not brothel.can_upgrade():
                    return self.unlock(game.chapter)

            elif self.target == "months":
                r = calendar.time // 28

            elif self.target in gstats_main + gstats_sex:
                for girl in MC.girls + farm.girls:
                    if girl.get_stat(self.target) >= self.requirements2[self.level+1]:
                        r += 1

            elif self.target == "ultimate":
                for girl in MC.girls + farm.girls:
                    for stat in gstats_main + gstats_sex:
                        if girl.get_stat(stat) < self.requirements2[self.level+1]:
                            break
                    else:
                        r += 1

            elif self.target == "pos fixations":
                for girl in MC.girls + farm.girls:
                    r = sum(1 for fix in girl.pos_fixations if (girl.personality_unlock[fix.name]))

            elif self.target == "neg fixations":
                for girl in MC.girls + farm.girls:
                    r = sum(1 for fix in girl.neg_fixations if (girl.personality_unlock[fix.name]))

            elif self.target == "minions":
                r = farm.count_minions()

            elif self.target in ("Warrior", "Wizard", "Trader"):
                if MC.playerclass == self.target:
                    r = MC.level

            elif self.target.startswith("mc "):
                if MC.get_stat(self.target[3:]) >= 10:
                    return self.unlock()

            elif self.target == "good":
                if MC.get_alignment() == self.target:
                    if MC.good > MC.neutral + 50 and MC.good > MC.evil + 50:
                        return self.unlock()

            elif self.target == "neutral":
                if MC.get_alignment() == self.target:
                    if MC.neutral > MC.good + 50 and MC.neutral > MC.evil + 50:
                        return self.unlock()

            elif self.target == "evil":
                if MC.get_alignment() == self.target:
                    if MC.evil > MC.good + 50 and MC.evil > MC.neutral + 50:
                        return self.unlock()

            elif self.target == "masochist":
                for girl in MC.girls + farm.girls:
                    if girl.personality.name == "masochist" and girl.personality_unlock["DS"] >= 100:
                        r += 1

            elif self.target == "naked":
                for girl in MC.girls + farm.girls:
                    if girl.naked:
                        r += 1

            elif self.target in ("bisexual", "group"):
                for girl in MC.girls + farm.girls:
                    if girl.will_do_sex_act(self.target):
                        r += 1

            elif self.target in ("hands", "body", "finger", "neck", "accessory"):
                for girl in MC.girls + farm.girls:
                    if girl.get_equipped(self.target):
                        r += 1

            elif self.target in tracked_achievements:
                r = game.check(self.target)

            elif self.target[:4] == "rank":
                _rank_dict = {"C" : 1, "B" : 2, "A" : 3, "S" : 4, "X" : 5}

                for girl in MC.girls + farm.girls:
                    if girl.rank >= _rank_dict[self.target[5]]:
                        r += 1

            elif self.target == "love":
                for girl in MC.girls + farm.girls:
                    if girl.get_love() >= self.requirements2[self.level+1]:
                        r += 1

            elif self.target == "fear":
                for girl in MC.girls + farm.girls:
                    if girl.get_fear() >= self.requirements2[self.level+1]:
                        r += 1

            elif self.target == "debug":
                self.level = 1
                return True

            if r >= self.requirements[self.level+1]:
                return self.unlock()

        def unlock(self, level_cap=99):
            if game.achievements and self.level < min(self.level_nb, level_cap):
                self.level += 1
                persistent.achievements[self.target] = self.level
                return True
            return False

        def get_title(self, _next=False, _button=False, force_level=None):
            if force_level:
                level = force_level
            else:
                level = self.level

            if self.level_nb == 1:
                return self.title
            elif _button:
                return self.title + " " + str(level) + "/" + str(self.level_nb)
            elif _next:
                return self.title + " " + roman_numbers[level+1]
            else:
                return self.title + " " + roman_numbers[level]

        def get_description(self, _next=False, force_level=None):
            if force_level:
                level = force_level
            else:
                level = self.level

            if self.level_nb == 1:
                return self.description

            else:
                if _next:
                    level += 1

                if self.requirements2:
                    return self.description % (str(self.requirements[level]), str(self.requirements2[level]))
                elif self.requirements:
                    return self.description % str(self.requirements[level])

    class Contract(object):

        # Contracts are a series of tasks (1-4) with a bonus special requirement (a given trait, perk, positive fixation, two girls (not ready), item type with minimum quality)

        def __init__(self, type, district, archetypes=None, names=None, organizers=None, venues=None, character="", MC_event_pic=None):
            self.type = type
            self.district = district
            if archetypes == None: archetypes = []
            self.archetypes = archetypes
            if names == None: names = []
            self.names = names
            if organizers == None: organizers = []
            self.organizers = organizers
            if venues == None: venues = []
            self.venues = venues
            self.character = character
            self.MC_event_pic = Picture(path=MC_event_pic).get(config.screen_width, int(config.screen_height*0.8))

            self.value = 0


        def randomize(self):

            self.result = False

            # Set level (from 1 to 4)

            self.level = rand_choice(contract_level[game.chapter])
            self.base_value = contract_value[game.chapter]
            self.special_bonus = 1.0
            self.girl_number = 1

            # Set description

            self.organizer = rand_choice(self.organizers)
            self.location = rand_choice(location_dict[self.district])
            self.char = self.character
            self.venue = rand_choice(self.venues)
            self.a_venue = article(self.venue)

            self.title = rand_choice(self.names)
            self.description = self.get_description(contract_description[self.type])
            self.bg = self.location.get_pic(config.screen_width, int(config.screen_height*0.8))

            # Set special requirement (bonus)

            spe = weighted_choice(contract_specials)

            if spe == "trait":
                self.special = (spe, rand_choice([t for t in pos_traits if t.archetype in self.archetypes], 2)) # Chooses two traits to match

            elif spe == "perk":
                self.special = (spe, rand_choice([p for p in perk_dict.values() if p.archetype in self.archetypes and p.level <= district.rank])) # Chooses a perk to match

            elif spe == "fix":
                self.special = (spe, rand_choice(fix_dict.values(), 3)) # Chooses three positive fixations to match

            elif spe == "farm":
                self.special = (spe, rand_choice(farm_type_list)) # Chooses one farm weakness to match (must be known to the player)

            elif spe == "item":
                self.special = (spe, rand_choice([IT_Dress, IT_Ring, IT_Necklace, IT_Accessory]))

            elif spe == "girls":
                self.special = (spe, 2)
                self.girl_number = 2

            # Assign 1 to 4 tasks according to rank

            if self.type == "orgy":
                tasks = rand_choice([tsk for tsk in contract_tasks if tsk.soft != True], self.level)
            else:
                tasks = rand_choice(contract_tasks, self.level)

            self.tasks = make_list(tasks, ContractTask) # No longer necessary with the changes to rand_choice
            self.tasks.sort(key=lambda x: contract_task_types_order[x.type])

            diff = 1
            hard_limit = 5

            for tsk in self.tasks: # Later tasks have more chances to be hard (and are worth more)
                if dice(6) < hard_limit:
                    tsk.randomize(self, "easy")
                else:
                    tsk.randomize(self, "hard")
                hard_limit -= 1

        def get_description(self, base_text): # can be called from outside the Contract object to convert any string (may not be necessary)
            desc = base_text.replace(":ORG:", capitalize(self.organizer))
            desc = desc.replace(":org:", self.organizer)
            desc = desc.replace(":DIS:", self.district)
            desc = desc.replace(":dis:", self.district.lower())
            desc = desc.replace(":LOC:", self.location.name)
            desc = desc.replace(":loc:", self.location.name.lower())
            desc = desc.replace(":VEN:", capitalize(self.venue))
            desc = desc.replace(":ven:", self.venue.lower())
            desc = desc.replace(":AVEN:", capitalize(self.a_venue))
            desc = desc.replace(":aven:", self.a_venue.lower())
            return desc

        def get_special_description(self):
            spe, target = self.special

            if spe == "trait":
                return "{b}特质{/b}: " + and_text([t.name for t in target], "或")

            elif spe == "perk":
                return "{b}奖励{/b}: " + target.name

            elif spe == "fix":
                return "{b}正面的固定性{/b}: " + and_text([f.name.capitalize() for f in target], "或")

            elif spe == "farm":
                return "{b}弱点{/b}: " + target.capitalize()

            elif spe == "item":
                return "{b}必须穿着{/b}: " + target.name

            elif spe == "girls":
                return "{b}派遣两个女孩{/b} (额外报酬)"

        def get_value(self, raw=False, no_special=False):
            r = self.base_value + sum(tsk.value for tsk in self.tasks)

            if not raw:
                r += brothel.get_effect("change", "contract rewards")
                r *= brothel.get_effect("boost", "contract rewards")

            if not no_special:
                r *= self.special_bonus

            return round_int(r)

        def get_special_value(self):
            if self.special_bonus != 1.0:
                if self.get_value(no_special=True) > 0:
                    return self.get_value() - self.get_value(no_special=True)
                else: # When refunding contract fee
                    return self.base_value
            else:
                return 0

        def enroll(self, free=False):
            calendar.active_contract = self

            task_desc = "{size=-1}"
            for tsk in self.tasks:
                task_desc += tsk.title + "\n"
                for req in tsk.get_requirements():
                    task_desc +=  req + "\n"
            game.set_task(task_desc + "{/size}", "contract", 7)

            if not free:
                MC.gold -= self.base_value
                renpy.play(s_gold, "sound")
            return

        def can_contract(self, girl):
            if girl.hurt > 0 or girl.away or girl.exhausted:
                return False
            return True

        def run(self, girls): # Result is True if not all tasks completed, False otherwise

            # Test Special requirement

            spe, target = self.special

            if spe == "girls":
                if len(girls) >= target:
                    self.special_bonus = 1.5

            elif spe == "trait":
                for t in target:
                    if girls[0].has_trait(t.name):
                        self.special_bonus = 1.4
                        break

            elif spe == "perk":
                if girls[0].has_perk(target.name):
                    self.special_bonus = 1.3

            elif spe == "fix":
                for f in target:
                    if girls[0].has_fixation("pos", f.name):
                        self.special_bonus = 1.5
                        break

            elif spe == "farm":
                if girls[0].weakness == target and farm.knows["weakness"][girls[0]]:
                    self.special_bonus = 1.5

            elif spe == "item":
                for it in girls[0].equipped:
                    if it.type.name == target.name:
                        self.special_bonus = 1.2
                        break

            # Test tasks

            self.failed_tasks = 0

            for tsk in self.tasks: # Failed tasks will earn zero and interrupt all remaining tasks
                if not tsk.run(self, girls):
                    self.failed_tasks += 1

            if not self.failed_tasks:
                self.result = "success"
            elif self.failed_tasks < len(self.tasks):
                self.result = "partial"
            else:
                self.result = "failure"

            game.set_task(None, "contract") # Clears contract from goal tooltip

            return


    class ContractTask(object):

        def __init__(self, name, type, requirements, tags, and_tags=None, and_tags2=None, soft=True): # and_tags2 is only used for 'fun' tasks.
            self.name = name # This is the handle used in the contract_task dictionary
            self.type = type # This is the category used to display the task name on the contract description, as well as generating the task intro text
            self.title = contract_task_types_description[self.type]
            self.base_requirements = requirements # List of possible requirements for this task (2 will be selected randomly). May start with 'job ', 'skill ' or 'pref ', followed by the stat name
            self.tags = make_list(tags) # These define the tags used for the task event
            if and_tags == None: and_tags = []
            self.and_tags = make_list(and_tags)
            if and_tags2 == None: and_tags2 = []
            self.and_tags2 = make_list(and_tags2)
            self.soft = soft # This activates/deactivates the soft filter. Special case: use of "naked"

        def get_pic(self, girl, and_tags=None): # and-tags overrides self.and_tags
            if self.soft:
                soft = True
                if self.soft == "naked":
                    naked_filter=False
                else:
                    naked_filter=True
            else:
                soft = False
                naked_filter=False

            if not and_tags:
                and_tags = self.and_tags

            not_tags = []

            for tag_list in self.tags + and_tags:
                if "group" in tag_list:
                    break
            else:
                not_tags.append("group")

            for tag_list in self.tags + and_tags:
                if "bisexual" in tag_list:
                    break
            else:
                not_tags.append("bisexual")

            if len(self.tags) == 4:
                return girl.get_pic(self.tags[0], self.tags[1], self.tags[2], self.tags[3], and_tags=and_tags, not_tags=not_tags, soft=soft, naked_filter=naked_filter, hide_farm=True)
            elif len(self.tags) == 3:
                return girl.get_pic(self.tags[0], self.tags[1], self.tags[2], and_tags=and_tags, not_tags=not_tags, soft=soft, naked_filter=naked_filter, hide_farm=True)
            elif len(self.tags) == 2:
                return girl.get_pic(self.tags[0], self.tags[1], and_tags=and_tags, not_tags=not_tags, soft=soft, naked_filter=naked_filter, hide_farm=True)
            elif len(self.tags) == 1:
                return girl.get_pic(self.tags[0], and_tags=and_tags, not_tags=not_tags, soft=soft, naked_filter=naked_filter, hide_farm=True)

        def randomize(self, contract, diff): # Sets limits and base gold value for the task

            self.value = round_int(contract.base_value * (0.9 + renpy.random.random()*0.2)) # +/-10% price variation
            self.result = False
            self.requirements = rand_choice(self.base_requirements, 2)
            self.limits = {}

            for req in self.requirements:
                if req.startswith("job"): # Easy is one job level under current maximum. Hard is current maximum
#                     name = req[4:]
                    if diff == "easy":
                        self.limits[req] = district.rank -1
                    else:
                        self.limits[req] = district.rank

                    if self.limits[req] <= 0: # Sanity check
                        raise AssertionError, "Contract requirement out of bounds: %s (current district: %s)" % (self.limits[req], district.rank)

                elif req.startswith("skill"): # Base skill limit is determined by game chapter and diff, +/- 15, with a -20 modifier then -10 for the first and second contract of each chapter.
                    mod = dice(31)-16
                    self.value += mod * game.chapter + brothel.contract_modifier
                    self.limits[req] = contract_skill_limit[game.chapter][diff] + mod

                elif req.startswith("pref"):
                    self.limits[req] = contract_sex_limit[game.chapter][diff]

            if diff == "easy":
                self.value *= 2 * game.get_diff_setting("rewards")
            elif diff == "hard":
                self.value *= 3 * game.get_diff_setting("rewards")


        def get_requirements(self):

            r = []

            for req in self.requirements:
                if req.startswith("job"):
                    r.append("{b}"+ req[4:].capitalize() + "{/b} %s or better" % ("{image=img_star}" * self.limits[req]))
                elif req.startswith("skill"):
                    r.append("{b}" + stat_name_dict[req[6:].capitalize()] +  " " + str(self.limits[req]) + "{/b} or better")
                elif req.startswith("pref"):
                    r.append("{b}" + req[5:].capitalize() + " preference: " + self.limits[req].capitalize() + "{/b} or better")

            return r

        def run(self, contract, girls):

            if contract.failed_tasks > 0: # Failed tasks will earn zero
                self.value = 0
                return False

            bonus = 0.0

            for girl in girls:
                for req in self.requirements:
                    target = self.limits[req]

                    if req.startswith("job"):
                        name = req[4:]
                        if girl.job_level[name] < target:
                            self.value = 0
                            return False
                        elif girl.job_level[name] > target: # bonus = 50% if job level above target
                            bonus += 0.5

                    elif req.startswith("skill"):
                        name = req[6:]
                        if girl.get_stat(name) < target:
                            # raise AssertionError, name + " is " + str(girl.get_stat(name)) + "vs target " + str(target)
                            self.value = 0
                            return False
                        else: # Bonus = 1% for each point of difference in stat value
                            bonus += (girl.get_stat(name) - target) / 100.0

                    elif req.startswith("pref"):
                        name = req[5:]
                        if not compare_preference(girl, name, target):
                            self.value = 0
                            return False
                        else: # Bonus = 1% for each point of difference in preference value
                            bonus += (girl.preferences[name] - get_preference_limit(name, target)) / 100.0

            if bonus > 1.0: # Bonus is capped
                bonus = 1.0

            self.result = True
            self.value += contract.base_value * bonus
            if brothel.contract_modifier < 0: # The first and second successful contracts for each chapter are easier for stat requirements, then revert to mean.
                brothel.contract_modifier += 10

            return True


## UTILITY CLASSES  ##

init -4 python:

    class Picture(object):

        """This class is for managing pictures and tags."""

        def __init__(self, filename="", path=""): # filename is antiquated, use path

            if filename:
                self.filename = filename
            elif path:
                file_parts = path.split("/")

                self.filename = file_parts[-1]

            if not path:
                raise AssertionError, "No path provided for the Picture() object"

            self.path = path

            #<Chris12 PackState>
            self.make_tags_from_filename()
            self.__hashcode = None
            self.__filesize = -1
            #</Chris12 PackState>

            # if self.filename.endswith(".webm"):
            #     self.video = True
            # else:
            #     self.video = False

            lowerExtension = self.filename[-5:].lower()
            self.video = any(lowerExtension.endswith(vid_ext) for vid_ext in VIDEOFORMATS)

        def get_old(self, x = None, y = None, proportional = True, side = False, profile = False): # Doesn't work with just x or y for now

            if self.video:
                return Movie(play=self.path, channel="video")

            if side:
                return ProportionalScale(self.path, 152, 152, yalign = 1.0)

            if profile:
                return ProportionalScale(self.path, config.screen_width//2.8, config.screen_height*2//3)

            if x and y:
                if proportional:
                    return ProportionalScale(self.path, x, y)
                else:
                    return im.Scale(self.path, x, y)
            else:
                return self.path

        ## FFUN VIDEO-COMPATIBLE GET METHOD

        def get(self, x = None, y = None, proportional = True, side = False, profile = False): # Doesn't work with just x or y for now
            image_path = self.path

            if side:
                if self.video :
                    return Movie(size=(152,152), play=image_path)
                else :
                    return ProportionalScale(image_path, 152, 152, yalign = 1.0)

            if profile:
                if self.video :
                    return Movie(size=(config.screen_width//2.8, config.screen_height*2//3), play=image_path)
                else:
                    return ProportionalScale(image_path, config.screen_width//2.8, config.screen_height*2//3)

            if x and y:
                if self.video :
                    return Movie(size=(x,y), play=image_path)
                if proportional:
                    return ProportionalScale(image_path, x, y)
                else:
                    return im.Scale(image_path, x, y)
            else:
                if self.video :
                    return Movie(play=image_path)
                else:
                    return image_path

        def has_tag(self, tag): # Single tag search
            return self.has_tags([tag])

        def has_tags(self, tags, and_tags = None, not_tags = None, old = False): # Multiple tag (OR) search. For performance reasons, has_tags should always receive tuples as arguments

            # Censorship (must be handled at the highest level)

            for tag in self.tags:
                if is_censored(tag):
                    return False

            if tags:
                for tag in tags:

                    if not tag: # Safety check in case a None value makes it into the tag list
                        continue

                    elif (nsfw == False and tag in nsfw_tags) or (tag in (persistent.forbidden_tags + forbidden_tags)):
                        pass

                    elif tag in self.tags or (old and tag in self.oldtags):
                        if not_tags:
                            for not_tag in not_tags:
                                if not not_tag:  # Safety check in case a None value makes it into the tag list
                                    continue
                                if not_tag in self.tags or (old and not_tag in self.oldtags):
                                    return False

                        if and_tags:
                            for and_tag in and_tags:
                                if not and_tag:  # Safety check in case a None value makes it into the tag list
                                    continue
                                if (nsfw == False and and_tag in nsfw_tags) or (and_tag in (persistent.forbidden_tags + forbidden_tags)):
                                    pass
                                elif not (and_tag in self.tags or (old and and_tag in self.oldtags)):
                                    return False
                            else:
#                                renpy.say("", "Found " + self.filename + " with tags among " + and_text(tags) + " and " + and_text(and_tags) + " but not " + and_text(not_tags))
                                return True
                        else:
#                            renpy.say("", "Found " + self.filename + " with tags among " + and_text(tags))
                            return True

            return False

        def get_weight(self, context=None):

            mod = 1.0

            if context:
                mod = persistent.fix_pic_balance[context]

            try:
                return self.base_weight * mod
            except:
                return self.update_weight() * mod


        def update_weight(self): # Base weight is 100

            for t in frequency_tags.keys():
                if self.has_tag(t):
                    self.base_weight = frequency_tags[t]
                    break
            else:
                self.base_weight = 100

            return self.base_weight


        #<Chris12 PackState>

        def make_tags_from_filename(self):
#             global tag_list_dict
#             global sorted_tag_dict_keys
#             global sorted_tags_with_separator
#             global ending_pattern

            # Initialization has been moved to BKinit_variables.rpy

            self.tags = []
            self.oldtags = []

            # This checks longest tags first. The second parameter allows filtered tag_lists to be used (for tags with spaces)
            def check_all_tags(filename, current_tag_list):
                old_len = len(filename)
                for tag in current_tag_list:
                    filename = filename.replace(tag, ' ')
                    new_len = len(filename)
                    if (new_len != old_len):
                        old_len = new_len
                        self.oldtags.append(tag)
                        self.tags += tag_list_dict[tag]

                return filename

            filename = self.filename.lower()
            self.is_trash = ("_trash" in filename)
            self.is_unrecognized = ("_unrecognized" in filename)
            filename = ending_pattern.sub(" ", filename) # removes extension and, if found, also (00001) at the end of the filename
            filename = check_all_tags(filename, sorted_tags_with_separator) # First look for tags with separators, e.g. 'cum shower'

            #after excluding all those tags, split the filename and look for exact matches
            parts = filename.split(' ')
            not_found = []
            for part in parts:
                if part.strip() != "":
                    tag_entry = tag_dict.get(part, None)
                    if tag_entry is not None: # tag was found
                        self.oldtags.append(part)
                        self.tags += tag_list_dict[part]
                    else:
                        not_found.append(part)

            if len(not_found) > 0:
                filename = ' '.join(not_found)
                check_all_tags(filename, sorted_tag_dict_keys)

            # Adding tag 'orgy' for bisexual and group pics, by popular demand
            if "group" in self.tags and "bisexual" in self.tags:
                self.tags.append("orgy")

            # Adding 'group' to double only for human partners (by popular demand)
            if "double" in self.tags and "beast" not in self.tags and "monster" not in self.tags and "machine" not in self.tags and "group" not in self.tags:
                self.tags.append("group")

        # calculates a checksum.
        # Has to be the same as the function in the picture namer, so that packstates work
        def get_hash(self):
            if self.__hashcode is None :
                BLOCKSIZE = 65536
                hasher = hashlib.sha256()
                with open(config.gamedir + "/" + self.path, 'rb') as afile:
                    buf = afile.read(BLOCKSIZE)
                    while len(buf) > 0:
                        hasher.update(buf)
                        buf = afile.read(BLOCKSIZE)
                self.__hashcode = hasher.hexdigest()
            return self.__hashcode

        # gets the filesize
        # lazily initialized because its only needed by packstate check, not during normal gameplay
        def get_filesize(self):
            if self.__filesize < 0:
                self.__filesize = os.path.getsize(config.gamedir + "/" + self.path)
            return self.__filesize

        # Based on Goldo's Picture Namer
        def get_new_name(self):
            # self.tags.sort(key=sort_tags)

            if self.filename[-5:] in (".jpeg", ".webp"):
                ending = self.filename[-5:]
            else:
                ending = self.filename[-4:]

            if self.is_trash:
                new_file_name = "_TRASH " + " ".join(self.oldtags) + " (%s)" + ending
            elif self.is_unrecognized:
                tag_as_unrecognized = preferences.packstate_unrecognized != "Ignore"
                if self.filename.startswith("_UNRECOGNIZED ") :
                    if tag_as_unrecognized :
                        new_file_name = self.filename # already has the tag
                    else :
                        new_file_name = self.filename[len("_UNRECOGNIZED "):] # remove the tag again
                else :
                    if tag_as_unrecognized :
                        new_file_name = "_UNRECOGNIZED " + self.filename
                    else :
                        new_file_name = self.filename # don't change the name if ignore
            elif self.oldtags:
                new_file_name = " ".join(self.oldtags) + " (%s)" + ending
            else:
                new_file_name = "_UNTAGGED" + " (%s)" + ending

            # When using old filename, put the (%s) into the new_file_name
            if "(" in new_file_name :
                new_file_name = new_file_name[:new_file_name.rfind("(")] + "(%s)" + ending
            else :
                new_file_name = new_file_name[:-len(ending)] + " (%s)" + ending
            return new_file_name

        # Based on Goldo's Picture Namer
        def commit_changes(self):

            i = 0
            new_file_name = self.get_new_name()

            # Compares file names up to the first parenthesis

            if new_file_name[:new_file_name.find("(")] != self.filename[:self.filename.find("(")]:

                while True :
                    if self.rename_file(new_file_name % str(i).zfill(5)):
                        return 1
                    else:
                        i += 1

            return 0

        # Based on Goldo's Picture Namer
        def rename_file(self, name):
            girlpath = self.path[:self.path.rfind("/")]
            os.chdir(config.gamedir + "/" + girlpath)

            try:
                os.rename(self.filename, name)
            except:
                return False

            self.filename = name
            self.path = girlpath + "/" + name

            return True

        #</Chris12 PackState>



## Not mine !       ##


    class ProportionalScale(im.ImageBase):
        '''Resizes a renpy image to fit into the specified width and height.
        The aspect ratio of the image will be conserved.'''
        def __init__(self, imgname, maxwidth, maxheight, bilinear=True, **properties):
            img = im.image(imgname)
            super(ProportionalScale, self).__init__(img, maxwidth, maxheight, bilinear, **properties)
            self.imgname = imgname
            self.image = img
            self.maxwidth = int(maxwidth)
            self.maxheight = int(maxheight)
            self.bilinear = bilinear

        def load(self):
            #<Chris12 NotFound>
            # Loads a neutral image instead of failing, in case an image does not exist
            try :
                child = im.cache.get(self.image)
            except IOError :
                # renpy.notify("Missing: " + self.imgname) # Commented out because it causes bugs in the CG gallery. Requires investigation
                child = im.cache.get(Image("backgrounds\not_found.webp"))
            #</Chris12 NotFound>

            width, height = child.get_size()

            ratio = min(self.maxwidth/float(width), self.maxheight/float(height))
            width = ratio * width
            height = ratio * height

            if self.bilinear:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.scale.smoothscale(child, (width, height))
                finally:
                    renpy.display.render.blit_lock.release()
            else:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.pgrender.transform_scale(child, (newwidth, newheight))
                finally:
                    renpy.display.render.blit_lock.release()
            return rv

        def predict_files(self):
            return self.image.predict_files()

#### END OF BK CLASSES ####
