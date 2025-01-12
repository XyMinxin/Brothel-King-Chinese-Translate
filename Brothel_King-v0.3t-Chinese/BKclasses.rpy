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

            self.seen_goal_message = False
            self.blocked_districts = []
            self.active_mods = {}
            self.track_dict = defaultdict(int)
            self.last_pic = {"tags": [], "and_tags": [], "not_tags": [], "attempts": 0}
            self.load_pics()
            self.effects = []
            self.world_effect_dict = defaultdict(list)
            self.effect_dict = defaultdict(list)
            self.customer_preference_weight = defaultdict(int)
            self.matching_priority = "rank"
#            self.set_difficulty("normal")
            self.__filesdict_timestamp = datetime.datetime.now() #<Chris12 AutoRepair />

            self.cheats = False
            self.achievements = True
            self.trainers = []

            self.init_mixes()



            self.set_difficulty(persistent.last_difficulty)

            self.sorting_dict = defaultdict(str) # Stores sorting preferences for girls and items.
            # Keys include 'MC items', 'shop items', 'girls', 'girls items', 'farm', 'farm items', 'slavemarket', 'minion_merchant items', 'city_merchant items'.
            # Values are suffixed with " reverse" if sorting is reversed.

            self.saved_schedules = [None]*10

        def save_schedule(self, girl, slot):
            self.saved_schedules[slot] = girl.get_schedule()

        def get_all_girls(self): # returns a list of all generated girls (for quick fixes and such)
            g_list = MC.girls + farm.girls + game.free_girls + slavemarket.girls + MC.escaped_girls
            if isinstance(enemy_general, Girl):
                g_list += [enemy_general]

            return g_list

        def sort(self, target, context):

            try:
                sorter = self.sorting_dict[context] # Sorter format is [caption, attribute, tooltip, reverse order, use_stats]
            except: # Initializes dict if non-existent to avoid breaking saves
                self.sorting_dict = defaultdict(str)
                return

            if sorter:
                if sorter[4]:
                    target.sort(key=lambda x, s=sorter[1]: x.get_stat(s), reverse=sorter[3])
                else:
                    target.sort(key=lambda x, s=sorter[1]: getattr(x, s), reverse=sorter[3])

        def init_mixes(self):
            self.mixes = list(persistent.game_mixes)

        # Cheats


        def activate_cheats(self):
            if renpy.call_screen("yes_no", "警告。激活作弊菜单将无法在本局游戏内解锁成就。这不会影响你已经解锁的成就，作弊菜单一旦激活就无法撤回了。\n{b}你确定要激活作弊菜单吗？{/b}"):
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

        def start_mods(self, early=False):
            # Init active mods (mods are stored within the game object, unless they get overwritten after an update)
            for mod in detected_mods.values():
                if mod.active:
                    self.activate_mod(mod, early)

        def update_mods(self): # Fun fact: renpy.call breaks python blocks, but not renpy.call_screen or renpy.say

            # Will return a list of custom calls to be made (if relevant)
            update_list = []

            # Checks if a saved game's mods have been deleted or changed

            for mod in list(self.active_mods.values()):

                if mod.name not in detected_mods.keys():
                    if renpy.call_screen("yes_no", mod.full_name + "文件无法识别，你想停用这个mod吗 (推荐)?"):
                        self.deactivate_mod(mod)

                elif mod.check_for_updates():
                    renpy.say("Mod更新", "MOD: %s有新的版本可用 (%s)。" % (mod.name, str(mod.version)))

                    if not hasattr(mod, "update_label"): # Fix for older games
                        mod.update_label = ""

                    if mod.update_label:
                        update_list.append(mod.update_label) # Cannot call directly or would break the python block

                    elif renpy.call_screen("yes_no", "你想重置这个Mod吗 (推荐)?"):
                        self.deactivate_mod(mod)
                        self.activate_mod(detected_mods[mod.name])

                elif not persistent.mods[mod.name]["active"]:
                    if renpy.call_screen("yes_no", mod.full_name + " has been deactivated. Would you like to deactivate this mod for this game?"):
                        self.deactivate_mod(mod)

            # Checks if a new mod has been activated

            for name, mod in list(detected_mods.items()):
                if mod.active:
                    if name not in self.active_mods.keys():
                        if renpy.call_screen("yes_no", "A new mod has been activated: " + mod.full_name + ". Would you like to activate this mod for this game?"):
                            self.activate_mod(mod)

            updated_games[self] = True # To do: Check if it works or needs a function

            return update_list

        def activate_mod(self, mod, early=False):

            self.active_mods[mod.name] = mod

            if early:
                if mod.early_label:
                    renpy.call_in_new_context(mod.early_label)
                    debug_notify("\n" + mod.name + ": early activation.")

                return

            if mod.night_label:
                daily_events.append(StoryEvent(label=mod.night_label, type="night", once=False))

            renpy.notify("\n" + mod.name + " has been activated.")


            if mod.init_label:
#                try:
                renpy.call_in_new_context(mod.init_label) # Suggested fix by SometimesIsNotEnough
#                except:
#                    renpy.say("System", event_color["bad"] % ("Failure to start " + mod.name) + " (calling " + mod.init_label + " label failed).")


        def deactivate_mod(self, mod):
            try:
                del self.active_mods[mod.name]
            except:
                renpy.say("System", event_color["bad"] % ("Failure to deactivate " + mod.name))

            if mod.night_label:
                for ev in daily_events:
                    if ev.name == mod.night_label:
                        daily_events.remove(ev)

            renpy.notify("\n" + mod.name + " has been deactivated.")



        def has_active_mod(self, name):
            if name in self.active_mods.keys():
                return True
            return False

        def list_free_girls(self):

            l = []

            for g in self.free_girls:
                l.append(g.name)

            return "Free girls: " + and_text(l)

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
                    return __("{size=-1}To advance to the next chapter, ") + and_text(goals) + ".{/size}"
                else:
                    return "{size=-1}" + and_text(goals) + "{/size}"
            else:
                return ""

        def get_goals(self):

            # if self.chapter == 7:
            #     return [("Endless", "You are now in endless mode, enjoy continuing the game!")]

            # Creates a list of active channels
            active_channels = [g.channel for g in self.goals if g.channel in self.goal_channels]

            goal_list = []
            for channel in self.goal_channels:
                if channel in active_channels:
                    goal_list.append((goal_categories[channel], self.get_goal_description(channel), goal_tb[channel]))

            return goal_list

        def get_first_goal(self):
            return self.get_goals()[0][1]

        def get_task(self): # Old
            if self.chapter > 2:
                return self.get_goal_description()
            else:
                return self.task

        def set_task(self, val, channel="story", max_chapter=None, blocking=True): # Creates a story goal to match. Overwrites previous story goal on this channel.
            # Clears previous task
            self.goals = [g for g in self.goals if g.channel != channel]

            if val: # Simply clears previous task if None value is provided
                if not max_chapter: max_chapter = self.chapter # Some uncompleted story goals may still allow progress to the next chapter
                self.goals.append(Goal("story", val, channel=channel, max_chapter=max_chapter, blocking=blocking))

        def set_goals(self, goals, channel="advance"): # Adds chapter goals (usually on the advance channel). goals must be a list of Goal objects
            # Clears previous goals
            self.goals = [g for g in self.goals if g.channel != channel]

            if goals:
                self.goals += goals

            if self.chapter < 7:
                self.seen_goal_message = False

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
            self.max_girl_level = {0: 1, 1: 1, 2: 4, 3: 6, 4: 9, 5: 12, 6: 16, 7: 20}[self.chapter]

        def update_max_girl_level(self): # Weekly update in random girls max level
            if self.max_girl_level < self.max_girl_rank * 5:
                self.max_girl_level += 0.5 # One level unlocks every two weeks

    class Main(object): #Attributes: name, job, god, pictures, decisions, inventory, girl inventory, character

        """This class is for the main character."""

        def __init__(self):

            self.type = "MC"
            self.name = MC_name
            self.level = 1
            self.prestige = 0
            self.gold = 0
            self.loan = None
            self.resources = defaultdict(int)
            self.last_collected = defaultdict(int)
            self.resource_tab_active = False

            self.good = 0
            self.neutral = 0
            self.evil = 0

            self.mojo = {"purple" : 0, "green" : 0, "blue" : 0, "red" : 0, "yellow" : 0}
            self.powers = []

            self.playerclass = "Warrior"
            self.god = "Arios"

            self._interactions = self.interactions = 0

            self.reset_stats()
            self.load_pics()

            self.girls = []
            self.escaped_girls = []
            self.street_girls = []
            self.trainers = []
            self.current_trainer = None
            self.items = []
            self.active_inv_filter = []
            self.active_text_filter = ""
            self.effects = []
            self.effect_dict = defaultdict(list)
            self.equipped = []
            self.slots = MC_inventory_slots

            self.noble = False
            self.active_spells = []
            self.known_spells = []
            self.active_powers = []
            self.skill_points = 0
            self.training = True

        # Interactions property
        @property
        def interactions(self):
            return self._interactions

        @interactions.getter
        def interactions(self):
            return self._interactions

        @interactions.setter
        def interactions(self, _value):
            # debug_notify("New value is %s" % _value)
            if self._interactions > _value:
                notify("-%s AP" % (self._interactions - _value), pic = "img_AP", col=c_white)

            self._interactions = _value


        ## Fear Points (mojo)

        def refund_mojo(self, cost_list): # Where cost_list is a list of tuples (mojo color, cost)

            for col, nb in cost_list:
                self.mojo[col] += nb

            return True

        def raise_mojo(self, mojo_color, mojo=1, raw=False):
            if mojo <= 0:
                return 0

            if not raw:
                mojo = mojo * self.get_effect("boost", mojo_color + " mojo gains") * self.get_effect("boost", "all mojo gains") + self.get_effect("change", mojo_color + " mojo gains") + self.get_effect("change", "all mojo gains")

            self.mojo[mojo_color] += mojo

            game.track(mojo_color + " mojo", mojo)

            if not story_flags["farm powers initiated"]:
                if farm.active and not farm.powers and self.mojo["purple"] >= 5 and game.chapter >= 3:
                    # 2 days buffer to avoid overlap with chapter change events
                    calendar.set_alarm(calendar.time + 2, StoryEvent(label="farm_powers_init", type="morning"))
                    story_flags["farm powers initiated"] = True

            return mojo

        def spend_mojo(self, cost_list, use_purple=True): # Where cost_list is a list of tuples (mojo color, cost)
            # Returns the list of spent mojo points (for possible refund)

            if not self.has_mojo(cost_list, use_purple=use_purple):
                raise AssertionError("MC mojo is insufficient (%s vs %s)" % (self.mojo, cost_list))
                return False

            spent_list = []
            spent_purple = 0

            for col, nb in cost_list:
                if nb > self.mojo[col]:
                    spent_list.append((col, self.mojo[col]))
                    spent_purple = nb - self.mojo[col]
                    self.mojo[col] = 0
                else:
                    spent_list.append((col, nb))
                    self.mojo[col] -= nb

            if spent_purple:
                spent_list.append(("purple", spent_purple))
                self.mojo["purple"] -= spent_purple

            return spent_list

        def has_mojo(self, cost_list, use_purple=True):
            missing_mojo = self.get_missing_mojo(cost_list)
            if not use_purple or missing_mojo > self.mojo["purple"]:
                return False
            return True

        def get_missing_mojo(self, cost_list):
            missing_mojo = 0
            for col, nb in cost_list:
                if self.mojo[col] < nb:
                    missing_mojo += nb - self.mojo[col]

            return missing_mojo

        ## Playerclass Init ## Everywhere in the code, player class names are written with a capitalized 1st letter.

        def set_playerclass(self, playerclass): # Only call this at the start of a new game: will reset MC stats

            self.playerclass = playerclass

            self.reset_stats()

            self.load_pics()

        def set_god(self, god): # Only call this at the start of a new game: will reset MC stats

            self.god = god

            self.reset_stats()

            self.load_pics()

        def swear(self):
            return rand_choice({"Arios": ["Arios", "我对太阳神发誓", "我对光明使者发誓", "我对光明之主发誓"], "Shalia": ["我对黑暗女神发誓", "我对莎莉娅发誓", "我对天发誓", "我对夜之女帝发誓"], None: ["我对魔鬼发誓", "我对恶魔发誓", "我对见鬼的牧师发誓", "我对十八层地狱发誓"]}[self.god])

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
            self.stat_ceil = {s.lower(): 10 for s in all_MC_stats}

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
                raise AssertionError("No picture found for the Main Character. Check the game/MC folder.")
            else:
                self.current_pic = self.pics[idx]

        # def load_pics_old(self):

        #     # Loading files

        #     self.files = []

        #     for file in renpy.list_files():

        #         if file.startswith("MC/"):

        #             file_parts = file.split("/")
        #             file_name = file_parts[-1]

        #             self.files.append(file)

        #     # Identifying image files

        #     imgfiles = [img for img in self.files if is_imgfile(img)]

        #     # Resetting pictures

        #     self.pics = []

        #     # Creating pictures

        #     for file in imgfiles:

        #         file_name = file.split("/")[-1]

        #         if self.playerclass.lower() in file_name.lower():

        #             pic = Picture(file_name, file)

        #             self.pics.append(pic)

        #     if not self.pics:
        #         raise AssertionError("No picture found for the " + MC.playerclass + " class. Check the game/MC folder.")
        #     else:
        #         self.current_pic = self.pics[0]

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
                    if renpy.call_screen("yes_no", "Are you sure you want to repay your loan in full for " + str(self.loan.amount) + " gold?"):
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

        def change_gold(self, amount): # should phase out hard-coded gains and losses progressively

            if amount !=0:
                self.gold += amount
                renpy.play(s_gold, "sound")
                notify("Gold: " + plus_text(amount, color_scheme="gold", decimals=0), pic="img_gold_24", col=c_gold)

        def gain_resource(self, resource="", number=1, message=True, _random=False): # Where resource is the resource name

            if _random:
                resource = rand_choice([r for r in build_resources if resource_dict[r].rank <= district.rank])
                if resource == "diamond": # can never get more than 1 diamond from a random city event
                    number=1

            if resource == "prestige":
                self.prestige += number
            elif resource in ("gold", "money", "denar"):
                resource = "gold"
                self.gold += number
            else:
                self.resources[resource] += number
                self.resource_tab_active = True

            if message:
                renpy.call("resource_gained", resource, number)
            else:
                renpy.notify("+" + str(number) + " " + __(resource))

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
                    renpy.call_screen("OK_screen", message="You failed to find anything.")
                    return
            else:
                return

            # The boost is generic (moon effect)
            nb += 1 * self.get_effect("boost", "resource extraction") + self.get_effect("change", resource + " extraction")

            self.gain_resource(resource, number=round_int(nb * game.get_diff_setting("resources")))

            return

        def has_resource(self, resource, amount=1): # Where resource is the resource name or "any"
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
                renpy.say(market_girl, "I'm sorry, you just don't have enough " + source + " to pay for this.")

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

                # elif spl.level > self.level and self.has_spell(spl): # Shouldn't be needed anymore. #? Check if it solves the 'forgotten spell when levelling' issue

                #     self.unlearn(self.has_spell(spl))
                #     renpy.pause(0.5)

            self.known_spells.sort(key=lambda x: x.get_cost())
#            renpy.say("", "Known spells =" + str(len(self.known_spells)))

        def learn(self, spl):
            if spl.type == "passive":
                self.active_spells.append(spl)
                self.add_effects(spl.effects)

                renpy.call_screen("OK_screen", title = spl.name, message = self.name + __(" has learnt a new talent.\n\n") + __(spl.description), pic = spl.pic, pic_size = "small")

            else:
                self.known_spells.append(spl)
                renpy.call_screen("OK_screen", title = spl.name, message = self.name + __(" has learnt a new spell.\n\n") + __(spl.description), pic = spl.pic, pic_size = "small")

            spl.auto = False

        def unlearn(self, spl): # Obsolete with 0.14

            if spl in self.active_spells:
                self.deactivate_spell(spl)

            if spl in self.known_spells:
                self.known_spells.remove(spl)
            spl.auto = False

            renpy.notify("{color=[c_crimson]}" + self.name + " has forgotten " + spl.name + "{/color}")


        def activate_spell(self, spl):

            if spl in self.active_spells:
                renpy.notify("%s: This spell is already active." % spl.name)
                return False

            elif type != "passive" and self.has_active_spell(spelltype = spl.type):
                renpy.notify("Another " + spl.type + " spell is already active.")
                return False

            elif self.mana >= spl.cost:

                self.mana -= spl.cost
                self.active_spells.append(spl)
                self.add_effects(spl.effects)

                renpy.play(spl.sound, channel='sound2')
                renpy.notify(spl.name + " has been activated.")
                renpy.pause(0.5)

                return True

            else:

                renpy.notify("%s: You do not have enough mana to cast this spell." % spl.name)

                return False

            return

        def autocast(self, spell, _time):

            msg = ""
            result = False

            if spell.auto == _time and spell not in self.active_spells:
                if self.activate_spell(spell):
                    msg = __("You have cast ") + __(spell.name) + "."
                    result = "success"
                    _sound = s_spell
                else:
                    msg = __("You failed to cast ") + __(spell.name) + "."
                    result = "fail"
                    _sound = s_fizzle

                renpy.play(_sound, "sound")
                notify(msg)
                # renpy.pause(0.5)

            return result, msg


        def deactivate_spell(self, spl):

            self.active_spells.remove(spl)
            self.remove_effects(spl.effects)

            renpy.notify(__(spl.name) + __(" has expired"))
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
                renpy.notify("Only one " + spl.type + " spell can be automated.")

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

            p = round_up(chg/2)

            notify("Prestige " + "+"*p, pic=self.current_pic, debug_txt="(%s)" % str_int(chg))

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

        def get_stat_cap(self, stat):
            return 10 + self.get_effect("change", stat + " max")

            # try:
            #     return self.stat_ceil[stat]
            # except:
            #     self.stat_ceil = {s.lower(): 10 for s in all_MC_stats}
            #     return 10


        def change_stat(self, stat, nb, apply_boost=True, spillover=False, silent=False):

            stat = stat.lower()

            if stat not in all_MC_stats:
                debug_notify("Unknown MC skill: %s" % stat)
                return False

            cap = self.get_stat_cap(stat)

            if apply_boost:
                nb = nb * self.get_effect("boost", stat + " gains") + self.get_effect("change", stat + " gains")

            if stat == "strength":
                nb = min(cap-self.strength, nb)
                self.strength += nb

            elif stat == "spirit":
                nb = min(cap-self.spirit, nb)
                self.spirit += nb

            elif stat == "charisma":
                nb = min(cap-self.charisma, nb)
                self.charisma += nb

            elif stat == "speed":
                nb = min(cap-self.speed, nb)
                self.speed += nb

            if nb > 0:
                if not silent:
                    notify("%s's %s: +%i" % (self.name, stat, int(nb)))
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

                if self.get_effect("special", "dragon form"):
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

            if not raw:
                spirit += self.get_effect("change", "spirit")

            return spirit


        def get_charisma(self, raw=False):

            char = self.charisma

            if not raw:
                char += self.get_effect("change", "charisma")

                if self.get_effect("special", "fairy form"):
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

        ## Alignment

        def get_alignment(self):
            if self.good > self.evil + 2 and self.good > self.neutral:
                return "good"
            elif self.evil > self.good + 2 and self.evil > self.neutral:
                return "evil"
            else:
                return "neutral"

        def get_alignment_delta(self, alignment):
            if alignment == "good":
                return min(MC.good - MC.evil, MC.good - MC.neutral)
            elif alignment == "evil":
                return min(MC.evil - MC.good, MC.evil - MC.neutral)
            else:
                return min(MC.neutral - MC.good, MC.neutral - MC.evil)


        def is_good(self):
            return self.get_alignment() == "good"

        def is_neutral(self):
            return self.get_alignment() == "neutral"

        def is_evil(self):
            return self.get_alignment() == "evil"

        ## Playerclass

        def is_warrior(self):
            return self.playerclass == "Warrior"

        def is_wizard(self):
            return self.playerclass == "Wizard"

        def is_trader(self):
            return self.playerclass == "Trader"

        ## Items

        def add_text_filter(self, text_filter):
            self.active_text_filter = text_filter.lower()
            self.active_inv_filter = []
            renpy.restart_interaction()

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

        def buy(self, seller, obj, price, counterpart=None):

            self.gold -= price

            if counterpart:
                counterpart.take(seller, obj)
            else:
                self.take(seller, obj)

            if obj.type == "girl":
                game.track("gold spent slavemarket", price)
            else:
                game.track("gold spent shops", price)

            norollback()

        def can_sell(self, buyer, obj):
            if not hasattr(self, "sold"):
                self.sold = defaultdict(list)
            elif obj in self.sold[buyer]:
                return False
            return True

        def sell(self, buyer, obj, price = None, owner=None):
            if isinstance(obj, ItemInstance):
                if not obj.sellable:
                    renpy.notify("%s: You cannot sell this item." % obj.name)
                    return False

            self.gold += price

            if owner:
                owner.give(buyer, obj)
            else:
                self.give(buyer, obj)

            self.sold[buyer].append(obj)

            norollback()
            return True


        def take(self, giver, obj): ## I know, girls are not objects...
            if isinstance(obj, Item):
                renpy.say(bk_error, "Warning: This item is not instantiated (%s)." % obj.name)

            if obj.type == "girl":
                try:
                    giver.girls.remove(obj)
                except:
                    pass
                renpy.call("acquire_girl", obj)

            else:
                self.items.append(obj)
                try:
                    giver.items.remove(obj)
                except:
                    pass

            renpy.restart_interaction()


        def give(self, taker, obj):
            if isinstance(obj, Item):
                renpy.say(bk_error, "Warning: This item is not instantiated (%s)." % obj.name)

            if obj.type == "girl":
                if obj in self.girls:
                    self.girls.remove(obj)
                elif obj in farm.girls:
                    farm.girls.remove(obj)
                taker.girls.append(obj)

            elif taker != MC and not obj.giveable:
                renpy.notify("%s: You cannot give this item." % obj.name)
                return False

            elif taker:
                if obj in self.items and obj.equipped:
                    self.unequip(obj)
                renpy.play(obj.sound, "sound")
                self.items.remove(obj)
                taker.items.append(obj)

            # renpy.restart_interaction()
            return True

        def gift(self, taker, item): #? Probably doesn't work #! TEST THIS
            if not isinstance(item, ItemInstance):
                renpy.say(bk_error, "Warning: This item is not instantiated (%s)." % item.name)

            if item.giveable:
                self.items.remove(item)
                renpy.say("", __("You give ") + taker.name + " {b}" + __(article(item.name)) + "{/b}.")
                result = taker.receive_gift(item)
                if not result:
                    renpy.notify("%s: You cannot give this item to this person." % item.name)
                    self.items.append(item)
                    return -1
                norollback()

                return result
            else:
                renpy.notify("%s: You cannot give this item." % item.name)
                return -1

        def equip(self, item):
            if not isinstance(item, ItemInstance):
                renpy.say(bk_error, "Warning: This item is not instantiated (%s)." % item.name)

            for i in self.equipped:
                if i.type.slot == item.type.slot:
                    self.unequip(i)

            self.equipped.append(item)
            self.add_effects(item.effects)
            item.equipped = True

            test_achievements(["mc strength", "mc spirit", "mc charisma", "mc speed"])

        def unequip(self, item):
            if not isinstance(item, ItemInstance):
                renpy.say(bk_error, "Warning: This item is not instantiated (%s)." % item.name)

            self.equipped.remove(item)
            self.remove_effects(item.effects)
            item.equipped = False

        def remove_item(self, it, unequip=True, use_sound=True):
            if not isinstance(it, ItemInstance):
                renpy.say(bk_error, "Warning: This item cannot be removed, it is not instantiated (%s)." % it.name)
            if it in self.items:
                if unequip and it.equipped:
                    self.unequip(it)
                self.items.remove(it)
                if use_sound:
                    renpy.play(it.sound, "sound")

        def add_item(self, it, equip=False, use_sound=True):
            if not isinstance(it, ItemInstance):
                renpy.say(bk_error, "Warning: This item cannot be added, it is not instantiated (%s)." % it.name)
            self.items.append(it)
            if equip:
                self.equip(it)
            if use_sound:
                renpy.play(it.sound, "sound")

        def use_item(self, item):
            if not isinstance(item, ItemInstance):
                renpy.say(bk_error, "Warning: This item is not instantiated (%s)." % item.name)

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

                elif e.type == "special":
                    # AP restoration
                    if e.target == "MC interactions":
                        self.reset_interactions()

            if used:

                r = item.use_me()

                if r == "used_up":
                    self.items.remove(item)

                norollback()

            return r

        def has_item(self, it_name):

            for it in self.items:
                if it.name.lower() == it_name.lower():
                    return True

            return False

        def get_items(self, target="any", type="any", name="any", effect_type="any", effect_target="any", strict=False): # Where 'type' is a name, not an object. Use strict to avoid naming errors (such as Extractor MKI being mistaken with MKII)

            items = []

            for it in self.items:
                if not isinstance(it, ItemInstance):
                    renpy.say(bk_error, "Warning: This item is not instantiated (%s)." % it.name)
                if it.target == target or target == "any":
                    if it.type.name == type or type == "any":
                        if name == it.name or (name in it.name and not strict) or name == "any":
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

        def rand_say(self, *sentences): # MC will say a random sentence in the list
            # Can take either a single list of strings, or several strings as arguments.

            if len(sentences) == 1 and not is_string(sentences):
                sentences = sentences[0]
            you(rand_choice(self.filter_say(sentences)))

            return

        def say(self, sentences): # Same as rand_say, just easier to manipulate
            return self.rand_say(sentences)

        def filter_say(self, sentences): # MC may say a random sentence in the list if and only if it checks out with his attributes

            d_list = []

            for it in sentences:

                if it.startswith("wr: ") or it.startswith("wa: "):
                    if self.is_warrior():
                        d_list.append(it[4:])

                elif it.startswith("wz: ") or it.startswith("wi: "):
                    if self.is_wizard():
                        d_list.append(it[4:])

                elif it.startswith("tr: "):
                    if self.is_trader():
                        d_list.append(it[4:])

                elif it.startswith("gd: "):
                    if self.is_good():
                        d_list.append(it[4:])

                elif it.startswith("ne: "):
                    if self.is_neutral():
                        d_list.append(it[4:])

                elif it.startswith("ev: "):
                    if self.is_evil():
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

        def __init__(self, name = "", char=None, defense=0, portrait = None, trainer_description = None, effects = None, item_types = "all", minion_type = None, bg = "bg_bro"):
            self.type = "NPC"
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
            self.active = False # Used for carpenter and slavemarket for now
            self.portrait = portrait
            self.bg = bg
            self.location = None

            if effects: # This NPC is also a potential trainer
                self.trainer_description = trainer_description
                self.effects = make_list(effects, Effect)
                game.trainers.append(self) # Updates the list of all available trainers
            self.updated = False
            self.last_restock = 0
            self.item_types = item_types
            self.minion_type = minion_type
            self.upgrade_level = 0
            self.stock_modifiers = {"junk" : 0, "common" : 0, "rare" : 0, "exceptional" : 0, "minion" : 0, "item" : 0}

            if char:
                self.char = char
            else: # imports renpy character if available
                try:
                    self.char = getattr(store, self.name.lower()) #?
                except:
                    self.char = Character(self.name)

        def get_bg(self):
            global bg_bro
            if self.bg == "bg_bro":
                return bg_bro
            else:
                return self.bg

        def take(self, giver, obj):
            if isinstance(obj, Item):
                renpy.say(bk_error, "Warning: This item is not instantiated (%s)." % obj.name)

            self.items.append(obj)
            if obj.equipped:
                giver.unequip(obj)
            try:
                giver.items.remove(obj)
            except:
                pass

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
                renpy.call_screen("OK_screen", "Missing resources", "You are missing the resources needed for this upgrade (%s %s)." % (cost[1], cost[0]))
                return False

        def restock(self, once_a_day=True, update_flag = True): # For shop NPCs

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
                        if self == NPC_giftgirl and dice(100) <= 10: # Gift girl has 10% chance of having a Wyvern egg
                            self.items.append(wyvern_egg.get_instance())

                        for i in range(number):
                            it = get_rand_item(quality, item_types=self.item_types)
                            # sanity_check = 0

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
                        for _ in xrange(dice(3)+1):
                            self.items.append(makibishi.get_instance())
                        # self.items += [makibishi.get_instance()]*(dice(3)+1) # This doesn't work because it creates several references to the same object

                self.items.sort(key=lambda x: x.price)


            elif self in minion_merchants:
                for typ, number in shop_mix:
                    if typ == "minion":
                        self.items += get_rand_minion(self.minion_type, nb=number)
                    else:
                        for i in range(number):
                            self.items.append(get_rand_item(rank="M"))

                if self.flags["extractor1 unlock"]:
                    if dice(6) >= 4:
                        self.items.append(extractor_items["extractor1"].get_instance())

                if self.flags["extractor2 unlock"]:
                    if dice(6) >= 5:
                        self.items.append(extractor_items["extractor2"].get_instance())

            # Track update
            if update_flag:
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
                self.locations = location_dict[self.name]

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
            self.description = "{b}" + misc_name_dict[self.name.capitalize()] + "{/b}服务难度:" + self.get_difficulty() + "):" + get_description(base_description, effects)

        def get_rand_name(self, gender="M"):
            return rand_choice(pop_name_dict[gender + " " + self.name])

        def get_average_budgets(self, description=False):
            base = (self.diff + self.range//2) * game.get_diff_setting("budget")
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

            self.name = article(__(self.adjective) + __(self.pop.get_rand_name())).capitalize()

            self.reason = ""
            self.satisfaction = self.get_effect("change", "overall customer satisfaction")
            self.service_dict = {"entertained" : 0, "laid" : 0, "both" : 0, "favorite entertainment" : 0, "favorite sex act" : 0, "extra" : 0} # Extra is earned with the right trait or bis/group sex
            self.got_entertainment = None
            self.got_sex_act = None
            self.group = False

            self.gender = "M"

            self.reputation_change = 0

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
                return r - self.rank, False # Didn't get the entertainment they wanted
            else:
                return r, True # Got the entertainment they wanted

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
                comment = rand_choice([__("I came here for nothing."), __("I didn't get attended at all."), __("What a disgrace. I wasted my time here."), __("No one attended me. Such a waste of time...")])

                if chg < 0:
                    comment = event_color["bad"] % comment

            elif self.base_rating == 8:
                comment = event_color["special contrast"] % rand_choice([__("I had the time of my life."), __("Everything was perfect."), __("Best night ever! I'm spent."), __("This place is amazing. Five stars!")])

            else:
                pos_comments = []
                neg_comments = []

                if self.service_dict["entertained"] >= 2:
                    pos_comments.append(__("I saw a really great performance."))
                elif self.service_dict["entertained"] == 1:
                    pos_comments += [__("I got some entertainment."), __("I was entertained while waiting."), __("A girl performed for me.")]
                    neg_comments.append(__("The entertainer could have been better."))
                else:
                    neg_comments += [__("There was no entertainment."), __("I was bored while waiting."), __("No entertainment. Boooring...")]

                if self.service_dict["laid"] >= 2:
                    pos_comments.append(__("The sex was really awesome."))
                elif self.service_dict["laid"] == 1:
                    pos_comments += [__("I got laid."), __("A whore took care of me."), __("I had %s.") % __(self.got_sex_act)]
                    neg_comments.append(__("The sex could have been better."))
                else:
                    neg_comments += [__("No whores! What kind of brothel is this?"), __("I couldn't find a whore. So frustrating."), __("Couldn't get laid, damn it!"), __("Where are the whores? Hello?")]

                if self.service_dict["both"] > 1:
                    pos_comments.append(__("I got both sex and entertainment."))

                if self.service_dict["favorite entertainment"] >= 1:
                    pos_comments.append(__("I got my favorite entertainment while waiting."))
                else:
                    neg_comments.append(__("My favorite entertainment was unavailable."))

                if self.service_dict["favorite sex act"] > 1:
                    pos_comments.append(__("I got my favorite sex act."))
                else:
                    neg_comments.append(__("My favorite sex act was unavailable."))

                if self.service_dict["extra"] > 1:
                    pos_comments.append(__("Sex is better with more people!"))

                if chg > 0:
                    comment = event_color["good"] % __(rand_choice(pos_comments))
                elif chg < 0:
                    comment = event_color["bad"] % __(rand_choice(neg_comments))
                else:
                    comment = rand_choice(pos_comments+neg_comments)

            return comment


        def randomize(self):

            self.preference = weighted_choice([("beauty", 25 + self.get_effect("change", "beauty preference")), ("body", 25 + self.get_effect("change", "body preference")), ("charm", 25 + self.get_effect("change", "charm preference")), ("refinement", 25 + self.get_effect("change", "refinement preference"))])
            self.wants_entertainment = weighted_choice([(j, customer_base_preference[j]*(1 + 0.5*game.customer_preference_weight[j]) + self.get_effect("change", j + " preference")) for j in all_jobs])
            self.wants_sex_act = weighted_choice([(a, customer_base_preference[a]*(1 + 0.5*game.customer_preference_weight[a]) + self.get_effect("change", a + " preference")) for a in all_sex_acts])
            self.fetish = rand_choice(trait_dict)

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

            pronoun = {"M": "He", "F": "She"}[self.gender]

            desc = ""

            if self.crazy:
                crz_text = " {color=" + c_red + __("}%s is crazy!{/color}") % __(pronoun)
            else:
                crz_text = ""

            if act == "idle job" or act in all_jobs:
                return self.name + __(" came in.%s %s wanted to be entertained by a {b}%s{/b}. %s prefers %s girls.") % (crz_text, __(pronoun), __(girl_related_dict[self.wants_entertainment]), __(pronoun), __(self.fetish))

            elif act == "idle whore":
                return self.name + __("%s %s likes {b}%s{/b}. %s prefers %s girls.") % (crz_text, __(pronoun), __(girl_related_dict[self.wants_sex_act]), __(pronoun), __(self.fetish))

            # elif act in all_jobs:
            #     desc += self.name + __(" came in.%s\n%s wanted to be entertained by a {b}%s{/b}") % (crz_text, __(pronoun), __(self.wants_entertainment))
            #     if self.wants_entertainment != act:
            #         desc += __(", but settled for a {b}%s{/b}") % __(act)
            #     return desc

            elif act in all_sex_acts:
                desc += self.name + __("%s %s likes {b}%s{/b}. %s prefers %s girls.") % (crz_text, __(pronoun), __(girl_related_dict[self.wants_sex_act]), __(pronoun), __(self.fetish))
                if self.wants_sex_act != act:
                    desc += __(", but settled for {b}%s{/b}") % __(girl_related_dict[act])
                if self.group:
                    desc += __(". %s joined a {color=" + c_purple + "}{b}group of %s{/b}{/color}") % (pronoun, self.group)
                return desc + "." + crz_text

            elif act == "end":
                desc += self.name + " wanted to be entertained by a {b}%s{/b}, " % girl_related_dict[self.wants_entertainment]
                if self.got_entertainment:
                    desc += "and got {b}%s{/b}. " % girl_related_dict[self.got_entertainment]
                else:
                    desc += "but was left unattended. "

                desc += "%s wanted {b}%s{/b}, " % (pronoun, girl_related_dict[self.wants_sex_act])
                if self.got_sex_act:
                    desc += "and got {b}%s{/b}. " % self.got_sex_act
                else:
                    desc += "but no whore was available. "

                return desc

        def set_budgets(self):
            d = dice(12)
            mod = 1.0

            if d == 12:
                self.adjective = __("rich ")
                mod = 2.0
            elif d == 1:
                self.adjective = __("poor ")
                mod = 0.5

            self.ent_budget = int((self.diff * mod  + self.get_effect("change", "job customer budget")) * self.get_effect("boost", "job customer budget") * brothel.get_adv_budget())
            self.wh_budget = int((self.diff * 3 * mod + self.get_effect("change", "whore customer budget")) * self.get_effect("boost", "whore customer budget") * brothel.get_adv_budget())

        def choose_girl(self, girls): # For xxx interactions: returns a girl and a reason for choosing her.

            chosen = None
            best_score = 0
            sex_act = self.wants_sex_act

            # Sanity check

            if not girls:
                raise AssertionError("Customer could not find girls to choose from. (%s)" % and_text([g.name for g in girls]))

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
                        reason = __(":cust: came looking for a ") + __(self.fetish) + __(" girl. :pron: :verb: elated to meet :girl:.")
                    elif trait_dict[self.fetish].verb == "be a":
                        reason = __(":cust: came looking for a ") + __(self.fetish) + __(". :pron: :verb: elated to meet :girl:.")
                    elif trait_dict[self.fetish].verb == "have":
                        reason = __(":cust: came looking for a girl with ") + __(self.fetish) + __(". :pron: :verb: elated to meet :girl:.")
                    elif trait_dict[self.fetish].verb == "have a":
                        reason = __(":cust: came looking for a girl with a ") + __(self.fetish) + __(". :pron: :verb: elated to meet :girl:.")

                # 2. The customer looks for a particular stat

                girl_score += girl.get_stat(self.preference) # Customers are looking for one stat in particular

                if not reason:
                    reason = __(":cust: wanted to meet ") + __(gstats_descript[self.preference]) + ". "

                    if girl_score >= 50*self.rank:
                        reason += __(":pron: :verb: elated to meet :girl:.")
                    elif girl_score >= 35*self.rank:
                        reason += __(":pron: :verb: pleased to meet :girl:.")
                    elif girl_score >= 20*self.rank:
                        reason += __(":pron: settled for :girl:.") # Special case handled with a try / except clause within the perform method
                    else:
                        reason += __(":pron: :verb: disappointed to meet :girl:.")

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
                self.reason = __(":cust: wanted to meet ") + __(gstats_descript[self.preference]) + __(". :pron: couldn't find a suitable girl.")

            return chosen, sex_act






    ## The code for brothels and room is messy / redundant and should be cleaned up some time

    class Brothel(): #Attributes: name, rooms, reputation, advertisement, tooltip

        """This class is for available brothels that you can operate."""

        def __init__(self, rank, level, upgrades, max_rep):

            self.name = "The Rose Garden"
            self.rank = rank
            self.level = level
            self.cost = bro_cost[self.level]
            self.total_value = self.cost
            self.bedroom_type = room_dict[upgrades[0]]
            self.maxupgrade = upgrades[1]
            self.max_rep = max_rep
            self.furniture = []
            self.rooms = {k: copy.copy(v) for k, v in common_room_dict.items()}
            self.effect_dict = defaultdict(list)
            self.reset_threat()

        # Set up Brothel

        def get_pic(self, x, y):
            return ProportionalScale("brothels/" + brothel_pics[self.pic_index], x, y)

        def get_bg(self):
            return "bg brothel%s" % self.pic_index

        def setup(self, name, furniture=None, current_building=None, started_building=0, master_bedroom_girls=None, free_room=None):

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
            self.max_help = bro_helpers[self.level]

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

        def upgrade_master_bedroom(self, target_level="auto"):
            if target_level == "auto":
                target_level = self.master_bedroom.level + 1

            if MC.has_gold(master_bedrooms[target_level].cost):
                if renpy.call_screen("yes_no", "Are you sure you want to upgrade your room for " + str(master_bedrooms[target_level].cost) + " gold?"):
                    renpy.play(s_gold, "sound")
                    MC.gold -= master_bedrooms[target_level].cost
                    self.total_value += master_bedrooms[target_level].cost
                    temp_girls = self.master_bedroom.girls
                    self.master_bedroom.girls = []

                    self.master_bedroom = master_bedrooms[target_level]

                    self.master_bedroom.girls = temp_girls

#                     test_achievement("upgrades")

            else:
                renpy.say(sill, "Sorry Master, you do not have enough money.")


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

        def can_build_anything(self, max_chapter=7):
            if [f for f in all_furniture if f.can_build() and f.chapter <= max_chapter]:
                return True
            return False

        def buy_furniture(self, furn):

            if self.current_building:
                renpy.say(carpenter, "Sorry boss, I still have work to do on that " + self.current_building.name + " you ordered.")
                return False

            elif not furn.can_build():
                if furn.built:
                    renpy.say(carpenter, "You've got it already. I don't think you need a second one.")
                renpy.say(carpenter, "Cannot build that for now, I'm 'fraid. You'd need a larger place.")
                return False

            for resource, amount in furn.cost:
                if not MC.has_resource(resource, amount):
                    renpy.say(carpenter, "Look, boss, you gotta have the right amount of resources before I can start the job.")
                    break
            else:
                renpy.say(carpenter, __("A'right, looks like you've got the goods. Hand them over, and I'll get started on that ") + __(furn.name) + __(" right away."))
                if renpy.call_screen("yes_no", __("Are you sure you want to build a ") + __(furn.name) + __(" for ") + __(furn.describe_cost()) + "?"):
                    MC.spend_resources(furn.cost)
                    norollback()
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

        # def update_effects(self):
        #
        #     update_effects()


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

            des = __("Your customers' average {b}entertainment budget{/b} is estimated to be around {b}%s gold{/b}") % int(self.customer_budget_dict["ent budget"])

            if self.customer_budget_dict["ent budget"] != base_ent_budget:
                des += " ("
                if self.customer_budget_dict["ent advertising"]:
                    des += event_color["good"] % ("+%s from advertising" % int(self.customer_budget_dict["ent advertising"]))
                    if self.customer_budget_dict["ent acts"]:
                        des += ", "
                if self.customer_budget_dict["ent acts"] > 0:
                    des += event_color["good"] % ("+%s from job bonuses" % int(self.customer_budget_dict["ent acts"]))
                elif self.customer_budget_dict["ent acts"] < 0:
                    des += event_color["bad"] % ("%s from job bonuses" % int(self.customer_budget_dict["ent acts"]))
                des += ")"

            des += ".\n"

            # Whoring budget description

            des += __("\nYour customers' average {b}whoring budget{/b} is estimated to be around {b}%s gold{/b}") % int(self.customer_budget_dict["wh budget"])

            if self.customer_budget_dict["wh budget"] != base_wh_budget:
                des += " ("
                if self.customer_budget_dict["wh advertising"]:
                    des += event_color["good"] % ("+%s from advertising" % int(self.customer_budget_dict["wh advertising"]))
                    if self.customer_budget_dict["wh acts"]:
                        des += ", "
                if self.customer_budget_dict["wh acts"] > 0:
                    des += event_color["good"] % (__("+%s from sex acts") % int(self.customer_budget_dict["wh acts"]))
                elif self.customer_budget_dict["wh acts"] < 0:
                    des += event_color["bad"] % (__("%s from sex acts") % int(self.customer_budget_dict["wh acts"]))
                des += ")"

            des += "。"

            return des

        def count_customers_description(self, short=False, col=c_lightblue):


            try:
                base_cust_nb = self.customer_count - self.customer_count_dict["advertising"] - self.customer_count_dict["special"]
            except:
                self.update_customer_count()
                base_cust_nb = self.customer_count - self.customer_count_dict["advertising"] - self.customer_count_dict["special"]

            if short:
                des = __("{color=" + col + "}{b}%i位顾客%s{/b}{/color}今晚会来消费") % (self.customer_count, plural(self.customer_count))
            else:
                des = __("{b}%i位顾客%s{/b}今晚会来消费") % (self.customer_count, plural(self.customer_count))

            if self.customer_count != base_cust_nb:
                des += " ("

                if self.customer_count_dict["advertising"]:
                    if short:
                        des += event_color["good"] % ("广告: +%s" % str_int(self.customer_count_dict["advertising"]))
                    else:
                        des += event_color["good"] % ("有" + str_int(self.customer_count_dict["advertising"]) + "个顾客是被广告吸引而来")
                    if self.customer_count_dict["special"]:
                        des += ", "
                if self.customer_count_dict["special"]:
                    if short:
                        des += event_color["good"] % ("其他: +%s" % str_int(self.customer_count_dict["special"]))
                    else:
                        des += event_color["good"] % ("+" + str_int(self.customer_count_dict["special"]) + " from girls and brothel effects")

                des += ")"

            return des + "。"

        def get_advertising(self, boost=True):

            r = self.advertising + self.get_effect("change", "advertising")

            if boost:
                return r * self.get_effect("boost", "advertising")
            else:
                return r

        def get_adv_reputation(self):
            raw_adv = self.advertising
            bonus_adv = self.get_advertising() - raw_adv

            raw_adv *= advertising_settings[self.get_effect("special", "advertising power")]["reputation"]
            bonus_adv *= advertising_settings[self.get_effect("special", "advertising power")]["reputation"]
            decay = (raw_adv + bonus_adv) * reputation_decay[game.chapter]

            return raw_adv, bonus_adv, decay

        def get_adv_setting(self, target):
            adv_lvl = self.get_effect("special", "advertising power")

            if target == "attraction":

                # Neutral advertising setting
                if self.advertising_setting == 0:
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

            return self.get_threat() - self.get_security()

        def estimate_threat_level(self, contrast=False, caps=False):

            risk = self.get_risk()

            if risk >= 10:
                level =  "very high"
                col = "bad"

            elif risk >= 5:
                level =  "high"
                if contrast:
                    col = "a little bad contrast"
                else:
                    col = "a little bad"

            elif risk <= -10:
                level =  "very low"
                col = "good"

            elif risk <= -5:
                level = "low"
                col = "a little good"

            else:
                level = "normal"
                if contrast:
                    col = "normal contrast"
                else:
                    col = "normal"

            if caps:
                level = capitalize(level)

            return "{b}%s{/b}" % event_color[col] % level

        def threat_build_up(self): # Builds up threat every turn depending on active security, with a minimum of 1. Returns True if security event can proc.

            if self.security_grace_period > 0: # Goes down one tick every day if the grace period is active. The grace period restarts after a security event happens.
                self.security_grace_period -= 1
                return False

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

        def reset_threat(self):
            self.alert_level = 1
            self.threat = 0
            self.security_grace_period = game.get_diff_setting("security")

        def get_ASM_report(self, short=False):

            cust, extra = self.customer_count, self.customer_count_dict["special"]
            msg = ""

            if short:
                msg += __("Advertising: ") + brothel.count_customers_description(short=True)

                msg += __("\nSecurity: The threat level is ") + self.estimate_threat_level(contrast=False) + "."

                msg += __("\nMaintenance: ") + __(maintenance_desc[self.get_cleanliness()])

            else:
                msg += __("Advertising report: ") + brothel.count_customers_description()

                msg += __(".\n\nSecurity report: The threat to your brothel is ") + self.estimate_threat_level(contrast=True) + "."

                msg += __("\n\nMaintenance report: ") + __(maintenance_desc[self.get_cleanliness()])

            return msg


        def change_rep_nightly(self, chg):
            return self.change_rep(chg, raw=False, silent=True)

        def change_rep(self, chg, raw=True, silent=False): # Boost and change effects are only applied once nightly

            if not raw:
                chg = chg * reverse_if(self.get_effect("boost", "brothel reputation"), chg) + self.get_effect("change", "brothel reputation")

            chg = get_change_min_max(self.rep, chg, 0, self.max_rep)
            self.rep += chg

            notify("%s: reputation: %s" % (brothel.name, plus_text(chg, color_scheme="rep")))

            return chg


        # ROOMS

        def upgrade_bedrooms(self):

            price = self.get_room_upgrade_price(self.bedrooms)

            text1 = "你确定要花" + str(price) + "金币升级房间吗？"

            if self.bedroom_type.level < self.maxupgrade:

                if renpy.call_screen("yes_no", text1):

                    if MC.has_gold(price):

                        MC.gold -= price
                        self.total_value += price

                        self.bedroom_type = room_dict[self.bedroom_type.level+1]
                        unlock_pic(self.bedroom_type.pic_path)


                        norollback()

                        renpy.restart_interaction()

                    else:
                        renpy.say(narrator, "你没有足够多的金币。")

            else:
                renpy.say(sill, "你无法继续升级青楼的房间了。")

        def get_mood_modifier(self, rank): #Increases with bedroom type: Girls score higher with customers and their mood improves

            mood_modifier = self.bedroom_type.level + self.get_effect("change", "mood modifier") - (rank * 2)

            return mood_modifier


        def get_room_price(self, room = "bedroom"):

            if room == "bedroom":
                price = (100 * self.bedrooms)

                for lvl in range(self.bedroom_type.level):

                    price += 50 * lvl

                price *= district.rank #? Increased bedroom price

            else:
                if brothel_firstvisit or self.free_room:
                    price = 0
                else:
                    price = sum(room.level for room in self.rooms.values()) * (50 + 150*1.5**(game.chapter-1)) # (sum(room.level for room in self.rooms.values()) - 1) * (50 + 150*1.5**(game.chapter-1))

            return round_int(price)

        def get_room_upgrade_price(self, nb = 1):
            # This is the cost per bedroom
            price = 50 * self.bedroom_type.level * district.rank #? Increased room upgrade price
            return price * nb

        def add_room(self, room = "bedroom", forced=False):

            if room == "bedroom":

                price = self.get_room_price()

                text1 = "你想花" + str(price) + "金币扩建一间卧室吗？"

                if self.bedrooms < self.get_maxbedrooms():

                    if renpy.call_screen("yes_no", text1):

                        if MC.has_gold(price):

                            MC.gold -= price
                            self.total_value += price

                            self.bedrooms += 1

                            test_achievement("upgrades")

                            norollback()

                            renpy.restart_interaction()

                            return True

                        else:
                            renpy.say(narrator, "你没有足够多的金币。")
                            return False
                else:
                    renpy.say(sill, "你的青楼已经没有更多的空间扩建卧室了。")
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
            return [room for room in self.rooms.values() if room.level > 0]

        def get_bedroom_pic(self, x=None, y=None):
            return self.bedroom_type.get_pic(x, y)

        def get_room_pic(self, type, x, y):
            if type == "bedroom":
                return self.get_bedroom_pic(x, y)
            elif type.lower() == "tavern":
                return tavern.get_pic(x, y)
            elif type.lower() == "strip club":
                return club.get_pic(x, y)
            elif type.lower() == "onsen":
                return onsen.get_pic(x, y)
            elif type.lower() == "okiya":
                return okiya.get_pic(x, y)

        def get_random_room_pic_path(self, show_dirt=True):
            if show_dirt:
                return rand_choice(self.get_common_rooms()).get_bg(self.get_cleanliness())

            return rand_choice(self.get_common_rooms()).get_bg()

        def get_random_room_pic(self, show_dirt=True):
            if show_dirt:
                return rand_choice(self.get_common_rooms()).get_bg(self.get_cleanliness())

            return rand_choice(self.get_common_rooms()).get_bg()

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

        def clean_up(self, factor = 1.0):

            price = round_int(self.get_clean_up_cost() * factor)

            if MC.has_gold(price):

                MC.gold -= price
                self.dirt = self.dirt - self.dirt * factor
                game.track("gold clean", price)
                norollback()

                return True

            else:
                renpy.say(narrator, "You don't have enough money.")

                return False

        def get_clean_up_cost(self):
            rank_factor = {1: 0.05, 2: 0.1, 3: 0.2, 4: 0.3, 5: 0.4}

            return round_int((1.0 + rank_factor[district.rank]) * (helper_cost[district.rank]*self.dirt))

        def get_auction_value(self):
            v = max(self.total_value - self.get_clean_up_cost(), 0)

            mod = (dice(7-district.rank) - 1) * 0.025 + (6-district.rank) * 0.05


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

            debug_notify("Cycling..." + str(self.pic_index))

            self.pic = self.get_pic(config.screen_width, int(config.screen_height*0.8))

            renpy.jump("brothel")






    class Calendar(object):

        """This class manages the game calendar, day/night cycle, and updates."""

        def __init__(self):

            self.time = 1
            self.day = 1
            self.month = 1
            self.year = 1
            self.moon = None
            self.alarms = {}
            self.discounted = []
            self.scarce = []
            self.contracts = []
            self.active_contract = None

        def get_today(self, get_year=False):
            return self.get_date(self.time, get_year)

        def get_date(self, _time, get_year=False):

            year = 1 + (_time-1) // (28*12)

            year_time = 1 + (_time-1) % (28*12)

            month = 1 + (year_time-1) // 28

            day = 1 + (year_time-1) % 28

            if get_year:
                return str(year) + "/" + str(month) + "/" + str(day)
            else:
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


        def updates(self, change_district=False): #This is the place where weekly updates are handled

            weekly_updates(change_district)

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

            # Story Events

            if is_string(_event): # Creates generic event on the fly if needed. Does not take arguments.
                _event = StoryEvent(label=_event, date=_time)
                daily_events.append(_event)

            elif isinstance(_event, StoryEvent):
                daily_events.append(_event)
                _event.date = _time

            # Old-style Events

            elif _time in self.alarms:
                self.alarms[_time].append(_event)

            else:
                self.alarms[_time] = [_event, ]

            debug_notify("Alarm set for %i (%s)" % (_time, _event.label))


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
            self.dirt = 0
            self.upkeep = 0
            self.costs = 0
            self.net = 0
            self.date = tl_cn(calendar.get_weekday(), misc_name_dict) + ", " + str(calendar.year) + "年 " + str(calendar.month) + "月 " + str(calendar.day) + "日"
            self.report = ""
            self.events = []
            self.changes = ""
            self.track_dict = defaultdict(int)

        def track(self, k, v=1):
            self.track_dict[k] += v

        def filter(self, filter_text):
            if not filter_text:
                self.filtered_report = self.report
            else:
                renpy.notify("filtering")
                report_lines = self.report.splitlines()
                filtered_report_lines = [line for line in report_lines if filter_text.lower() in line.lower()]
                self.filtered_report = "\n".join(filtered_report_lines)

        def get_filtered_report(self):
            try:
                return self.filtered_report
            except:
                return self.report

        def get_day_report(self):
            return get_day_report(self)

        def get_tonight_report(self):
            pass

        def check(self, k):
            return self.track_dict[k]

        def add_report(self, text):

            self.report += "\n" + text

        def add_event(self, event):

            self.events.append(event)

        def show_events(self):

            norollback()

            for event in self.events:

                renpy.checkpoint()

                if event == self.events[-1]:

                    renpy.choice_for_skipping()

                event.show_night()







### SECONDARY CLASSES ##

    class Event(object):

        """This class covers 2 kinds of events: Night events (run during working hours) and Day events (run when returning to the main screen). Day events should be phased out and replaced by Story Events"""

        def __init__(self, pic = None, background = None, char = None, text = "", changes = "", sound = None, with_st = None, type="Normal", label = None, object = None, order = 0, weight = 1, debug_id=0):

            self.pic = pic
            self.background = background
            self.char = char
            self.text = text
            self.sound = sound
            self.with_st = with_st
            self.type = type
            self.changes = changes
            self.label = label
            self.object = object
            self.order = order
            self.debug_id = debug_id

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

        def __init__(self, label, chapter=0, rank=0, date=0, year=0, month=0, day=0, weekday="", chance = 1.0, type="any", location = None, locations = None, seasons = None, min_gold = -999999999, condition = None, not_condition = None, condition_func=None, call_args=None, arg=None, once = True, AP_cost = 1, order = 0, weight = 1, room = None):
            # Use arg to transmit a single argument, call_args for several arguments ordered in a list. Don't use both.

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
            self.location = location # location must be the location's name
            self.locations = locations # A list of location names
            self.seasons = seasons # A list of seasons
            self.min_gold = min_gold
            self.condition = condition
            self.not_condition = not_condition
            self.condition_func = condition_func # For complex conditions, this function is called with no arguments and must return a bool
            self.room = room
            if arg:
                call_args = [arg]
            elif call_args == None:
                call_args = []
            self.call_args = call_args # call_args must be a list
            self.once = once
            self.AP_cost = AP_cost
            self.order = order # Base order is 0. Lower values will fire first.

            self.happened = False
            self.mod = None

        def happens(self, type="any"): # Tests if happened, current chapter, chance of happening, location and custom story flags (optional)

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
            col = "normal"

            if bonus:
                if bonus > 0:
                    col = "good"
                elif bonus < 0:
                    col = "bad"
                bonus_text = " (%s)" % plus_text(bonus, color_scheme="standard")

            description = event_color[col] % ("{b}%s/%s{/b}" % (int(total_value), maxrange)) + "%s. " % (bonus_text) + __(gstats_dict[self.name])

            if self.name in gstat_job_skill.keys():
                return description % (self.parent.get_max_cust_served(gstat_job_skill[self.name]), plural(self.parent.get_max_cust_served(gstat_job_skill[self.name])))

            return description

        def get_statmax(self):
            statmax = self.parent.rank * 50
            statmax += self.parent.get_effect("change", self.name.lower(), change_cap=True) + self.parent.get_effect("change", self.name.lower() + " max") + self.parent.get_effect("change", "all skill max")

            return statmax

        def set(self, val): # Forces a stat to raw value val, ignoring random generation and caps
            self.value = val

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

        # def init_value_old(self, weight):
        #
        #     if self.type == "sex":
        #         pref = self.parent.get_preference(self.name.lower())
        #
        #         if pref == "refuses":
        #             a = 0
        #             b = -5
        #         elif pref in ("very reluctant", "reluctant"):
        #             a = 1.5
        #             b = 3.5
        #         elif pref in ("a little reluctant", "indifferent"):
        #             a = 5
        #             b = 10
        #         elif pref in ("a little interested", "interested"):
        #             a = 7.5
        #             b = 17.5
        #         elif pref in ("very interested", "fascinated"):
        #             a = 12.5
        #             b = 22.5
        #     else:
        #
        #         # Loads the dice if specified in init file
        #
        #         if weight == 5:
        #             d = 100
        #         elif weight == 4:
        #             d = 90
        #         elif weight == 3:
        #             d = 50
        #         elif weight == 2:
        #             d = 20
        #         elif weight == 1:
        #             d = 0
        #         else:
        #             d = dice(100)
        #
        #         if self.type == "sex":
        #
        #             a = 0
        #             b = -5
        #
        #         elif d > 98: # Superb skill
        #
        #             a = 12.5
        #             b = 22.5
        #
        #         elif d > 85: # High skill
        #
        #             a = 7.5
        #             b = 17.5
        #
        #         elif d > 35: # Average skill
        #
        #             a = 5
        #             b = 10
        #
        #         elif d > 10: # Low skill
        #
        #             a = 1.5
        #             b = 3.5
        #
        #         else: # Terrible skill
        #
        #             a = 0
        #             b = -5
        #
        #     self.value = dice(5 + 5 * game.chapter) + a * game.chapter + b # Changed district.rank to game.chapter to allow for higher stats
        #
        #     if self.value < 0:
        #         self.value = 0
        #
        #     elif self.value > self.statmax:
        #         self.value = self.statmax


        def change(self, chg, _max = 250):

            # Will not revert to cap if value is already higher
            if self.value > _max:
                _max = self.value

            if self.value + chg < 0:

                r = -self.value

                self.value = 0

                return r

            elif self.value + chg > _max:

                r = _max - self.value

                self.value = _max

                return r

            else:
                self.value += chg

                return chg


    class Trait(object):

        """This class is for traits (skills with special effects that are either on or off)."""

        # eff1, eff2, eff3 are kept for backwards compatibility, until I clean up the code

        def __init__(self, name, verb = "be", eff1 = None, eff2 = None, eff3 = None, effects = None, opposite = None, archetype = None, base_description = "", public=True):
            # Setting 'public' to True means any girl can generate with this trait. False means it can only be generated through code or _BK.ini

            self.name = name
            self.verb = verb

            self.effects = []

            if effects:
                self.effects = make_list(effects, Effect)
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
            self.public = public

#            renpy.say(self.name, str(len(self.effects)))

        def get_past_tense(self):

            if self.verb.startswith("be"):
                text1 = "was"
            elif self.verb.startswith("have"):
                text1 = "had"

            return self.add_article(text1) + " {b}" + self.name.lower() + "{/b}"

        def add_article(self, mytext):
            if self.verb.endswith("a"):
                mytext += " a"
            elif self.verb.endswith("an"):
                mytext += " an"

            return mytext

        def get_description(self, context=None, short=False):

            if short:
                return get_description("", self.effects)
            else:
                des = get_description(self.base_description, self.effects)

                if context in ("slavemarket", "free"):
                    if self.archetype:
                        des += __("\nUnlocks {b}") + __(self.archetype) + __("{/b} zodiac sign.")

                return des

    class Perk(object):

        """This class is for all kinds of perks (used in the new perk system)"""

        def __init__(self, name, type, effects, archetype=None, pic = None, perk_level=0, min_rank=0, base_description = ""):
            self.name = name
            self.type = type
            self.effects = make_list(effects, Effect)
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
                return get_description("\n{i}" + __(self.base_description) + "\n\n" + "{/i}", self.effects)

    class PerkArchetype(object):

        """This class is for perk archetypes (used in the new perk system)"""

        def __init__(self, name, pic):

            self.name = name
            self.pic = pic
            self.unlocked = False
            self.base_description = archetype_description[self.name]

        def get_pic(self, portrait=False):
            if portrait:
                return Picture(self.pic[:-5] + " portrait" + self.pic[-5:], "perks/" + self.pic[:-5] + " portrait" + self.pic[-5:])
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








#            value = 0


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

        def __init__(self, type, target = None, value = 0, chance = 1.0, scales_with = None, scope = None, dice=False, change_cap=True, duration=-1, source=None):
            self.type = type
            self.target = target
            self.value = value
            self.chance = chance
            self.scales_with = scales_with
            self.scope = scope
            self.source = source
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
                factor = 1.0

            if not self.target.endswith(" fixation"):
                v = factor*self.value

            #### APPLIES DICE EFFECT ####

            if self.dice:
                try:
                    v = dice(round_int(v), self.dice) # New: dice property can be an integer
                except:
                    v = dice(round_int(v))

            #### TEST EFFECT PROC CHANCE ####

            # Chance is tested here in case the gain is conditional
            if renpy.random.random() > self.chance:
                result=False

            #### APPLY EFFECT IF SUCCESSFUL ####

            # Instant cleaning (brothel)
            elif self.target == "dirt":
                c = brothel.change_dirt(v)

            elif self.target == "love": # Instant love
                c = thing.change_love(v, silent=True)

            elif self.target == "fear": # Instant fear
                c = thing.change_fear(v, silent=True)

            # Instant healing
            elif self.target == "heal":
                c = thing.heal(v)

            # Instant XP gain
            elif self.target in ("xp", "experience"):
                c = thing.change_xp(v, apply_boost=apply_boost, spillover=spillover, silent=True)

                while thing.ready_to_level():
                    thing.level_up()

            # Instant prestige gain
            elif self.target == "prestige":
                c = thing.change_prestige(v, apply_boost=apply_boost)

                if thing.ready_to_level():
                    thing.level_up()

            # Instant JP gain
            elif self.target[-3:] == " jp":
                c = thing.change_jp(v, self.target[:-3], apply_boost=apply_boost, spillover=spillover, announcement_delay=0, silent=True)

            # Instant REP gain
            elif self.target in ("rep", "reputation"):
                c = thing.change_rep(v, silent=True)

            # Instant perk points gain
            elif self.target in ("perk", "perks"):
                thing.perk_points += v
                thing.update_can_perk()
                c = v

            # Instant skill point gain
            elif self.target in ("skills", "skill points"):
                thing.upgrade_points += v
                c = v

            # Instant positive/negative fixation gain
            elif self.target.endswith(" fixation"):
                if not self.value:
                    raise AssertionError("Did not provide value for %s" % self.target)
                if self.value in fix_dict.keys():
                    c = thing.add_random_fixation(fixation=self.value, type=self.target[:3])[0] # because add_random_fixation returns a list
                else:
                    for i in range(self.value):
                        c = thing.add_random_fixation(type=self.target[:3])[0] # because add_random_fixation returns a list

                for fix in c:
                    thing.personality_unlock[c] = False

            # Instant sex preference gain
            elif self.target == "all sexual preferences":
                for act in extended_sex_acts:
                    thing.change_preference(act, v, silent=True)

            elif self.target.endswith(" preference"):
                thing.change_preference(self.target[:-11], v, silent=True)

            # Permanent stat/skill gains
            else:
                # debug_notify(factor*self.value)
                c = thing.change_stat(self.target, v, apply_boost=apply_boost, spillover=spillover, silent=True)

            # Plays a sound when activating gain/instant
            if result:
                renpy.play(s_spell, "sound")
            else:
                renpy.play(s_fizzle, "sound")

            return c

        def get_description(self):
            val = self.value
            target = self.target
            text1 = ""
            text2 = ""
            text3 = ""
            
            target_dict = {
                "body": "身材",
                "charisma": "玩家魅力",
                "charm": "魅力",
                "spirit": "玩家精神",
                "strength": "玩家力量",
                "speed": "玩家速度",
                "beauty": "美貌",
                "refinement": "优雅",
                "sensitivity": "敏感",
                "constitution": "体格",
                "libido": "性欲",
                "obedience": "服从",
                #替换extended_sex_acts = ["naked", "service", "sex", "anal", "fetish", "bisexual", "group"]
                "naked": "露出",
                "service": "侍奉",
                "sex": "性交",
                "anal": "肛交",
                "fetish": "调教",
                "bisexual": "双飞",
                "group": "群交",
                "all jobs": "所有工作",
                "all sex acts": "所有性行为",
                "fear": "恐惧值",
                "love": "好感度",
                "waitress": "女服务员",
                "dancer": "脱衣舞娘",
                "masseuse": "按摩技师",
                "geisha": "表演艺伎",
                "dress": "衣着加成"
            }

            if self.type in ("special", "personality"):

                if target == "naked":
                    text1 = "十分乐意裸体"

                elif target == "level":
                    text1 = "+1等级 (最高等级: " + str(val) + ")"

                elif target == "advertising power":
                    text1 = "提高广告的效果 (提高青楼的声望增速,客流量和顾客的预算)。"

                elif target == "heal minion":
                    text1 = "治疗一个受伤的单位。"

                elif target == "workwhore":
                    text1 = "她可以一边正常的工作，一边勾引客人上床。"

                elif target == "lucky":
                    text1 = "工作或卖淫时提高判定大成功的概率 (骰出5-6都视为大成功)"

                elif target == "unlucky":
                    text1 = "工作或卖淫时提高判定大失败的概率 (骰出1-2都视为大失败)"

                elif target == "temptress":
                    text1 = "能说服不情愿的顾客接受另一种性行为"

                elif target == "pickpocket":
                    text1 = "有25%机会从顾客那里偷取额外10%的小费，但有15%的概率降低自身和青楼的声望"

                elif target == "random item":
                    text1 = "顾客有2.5%的概率“遗漏”随机物品"

                elif target == "BBCR bonus":
                    text1 = "如果她的外貌、身材、魅力或优雅等级足够高，可能会提高客户的满意度"

                elif target == "LOCS bonus":
                    text1 = "如果她的性欲，服从，体质或敏感等级足够高，可能会提高客户的满意度"

                elif target == "whore mood modifier":
                    text1 = "卖淫时，情绪+1"

                elif target == "job prestige":
                    text1 = "普通工作也能让主角获得声望"

                elif target == "skill catch up":
                    text1 += "每天晚上，她会帮助其他属性比她低的女孩获得永久的属性提升 (每升一阶多帮助一人)"

                elif target == "effect chance":
                    text1 += "使天赋生效的基础几率加倍 (最多50%)"

                elif target == "defender":
                    text1 += "即使你没有行动力了你也可以保护青楼（把力量属性计入青楼安全）"

                elif target == "snake eyes":
                    text1 += "催眠永远不会失败"

                elif target == "safe":
                    text1 += "使 " + str(val) + " 金币不被计入青楼的威胁值。"

                elif target == "focus":
                    text1 += "如果女孩在营业时专精于一种性行为，+25%小费和声望收益 (不包括双飞和群交行为)"

                elif target == "rest shield":
                    text1 += "她在休息时，可以对自己或她的朋友施放一层魔法护盾，保护其免受攻击"

                elif target == "ignore budgets":
                    text1 += "顾客将会超出预算透支消费"

                elif target == "ignore energy":
                    text1 += "每次互动都有概率不消耗精力"

                text1 = "在作为妓女工作时接受群交行为" if target == "group" else text1
                text1 = "在作为妓女工作时接受双飞行为" if target == "bisexual" else text1
                text1 = "在任何时候包括平时都保持裸体" if target == "naked" else text1
                text1 = "在作为妓女工作时接受激烈的多人群交" if target == "orgy" else text1
                text1 = "在作为妓女工作时戴上装饰扮演兽耳娘" if target == "ponygirl" else text1

                return __(text1)

            elif self.type == "instant" and target == "heal":
                return "疗伤时间减少 " + str(val) + "天。"

            if self.type == "set":
                target = "所有技能上限值" if target == "all skill max" else target
                text1 += "改变" + target + __("到") + str(val)
                if self.scope:
                    text1 += " (%s)" % tl_cn(self.scope, misc_name_dict)
                return text1

            if self.type == "allow":
                if target.endswith("preference"):
                    target = "享受服务倾向" if target == "waitress preference" else target
                    target = "观看舞蹈倾向" if target == "dancer preference" else target
                    target = "接受按摩倾向" if target == "masseuse preference" else target
                    target = "观摩表演倾向" if target == "geisha preference" else target
                    target = "侍奉倾向" if target == "service preference" else target
                    target = "性交倾向" if target == "sex preference" else target
                    target = "肛交倾向" if target == "anal preference" else target
                    target = "调教倾向" if target == "fetish preference" else target
                    target = "群交倾向" if target == "group preference" else target
                    target = "双飞倾向" if target == "bisexual preference" else target
                    target = "所有性行为倾向" if target == "all sex acts preference" else target
                    text1 += "允许您增加客人的' " + target + " 最多 +" + str(50*val) + "%。"
                else:
                    text1 += "现在" + tl_cn(target, misc_name_dict) + "也会光顾你的青楼了。"

                return text1

            if 0.75 <= self.chance < 1.0:
                text2 = "高概率(>75%)" + text2
            elif 0.25 < self.chance < 0.75:
                text2 = "有概率(>25%)" + text2
            elif self.chance <= 0.25:
                text2 = "小概率(<25%)" + text2


            if self.type == "reroll":
                if text1:
                    text1 += "再掷一次... "
                else:
                    text1 += __("reroll")

                if self.target == "job critical failure":
                    text1 += __(" a critical failure when working")

                return text1

            if self.dice:
                text1 += "1-"

            elif is_string(val):
                pass

            elif val > 0:
                text2 += "+"

            if self.type in ("gain", "instant"): # Permanent x gain (xp, reputation...)
                try:
                    text2 += __(str(round_int(val))) + " "
                except:
                    text2 += __(str(val)) + " "
                # 中文不需要介词
                #if self.target.endswith("preference") or self.target.endswith("preferences"):
                #    text1 += __(" to ")

            elif self.type == "change": # Temporary x effect (can be added or removed)
                # text1 += str(round_best(val, 2)) + __("到")
                text1 += str(round_best(val, 2))
                if target.endswith("training obedience target"):
                    target = "训练时所需服从"
                if target.endswith("train obedience target"):
                    target = "训练时所需服从"
                if target.endswith("work obedience target"):
                    target = "工作时所需服从"
                if target.endswith("fight challenges"):
                    target = "挑战中战斗加成"
                if target.endswith("max"):
                    which = target.replace(" max", "")
                    if which in target_dict:
                        target = target_dict[which] + "属性上限"
                if target.endswith("requirements"):
                    which = target.replace(" requirements", "")
                    if which in target_dict:
                        target = target_dict[which] + "激活要求"
                        
            elif self.type == "resist":
                text1 += str(round_int(val)) + __(" negated {#1}")

            elif self.type == "spillover":
                percentage = round_int(val * 100)
                self.target = "经验" if self.target == "xp" else self.target
                self.target = "职业经验" if self.target == "jp" else self.target
                text1 += "每当获得" + self.target + "时，其他女孩也收获"+str(percentage) + "%"
                # text1 += str(percentage) + "% " + target + __(" 赚钱的时候分给其他女孩 ")

            elif self.type == "boost": # Temporary % effect (can be removed)

                percentage = round_int(val * 100)

                text1 += str(percentage) + __("%")

            elif self.type == "gift":
                text1 += str(round_int(val)) + " "

            elif self.type == "increase satisfaction":
                # text2 = __(" to customer satisfaction for ") + str(round_int(val)) + text2
                text2 = "的顾客满意度" + text2 + str(round_int(val))

            if self.scope and not target.startswith(self.scope): # The second part handles the 'brothel rep' special case, although renaming brothel reputation to something different to avoid confusion with girl reputation would be a good long-term fix
                #text1 += __(self.scope) + " "
                # text1 += __("{0} {1}").format(__(self.scope), __(target))
                scopexxx = ""
                if self.scope== "brothel":
                    scopexxx = "全青楼的"
                elif self.scope == "city":
                    scopexxx = "在城市中"
                else:
                    scopexxx = __("{0} {1}").format(__(self.scope), __(target))
                text1 += scopexxx + ""
            # else:
            #     text1 += __(target)
            if target in ("rep", "reputation"):
                target="人气"

            ###替换掉中文注释造成的取值错误 strength,charisma,spirit,speed,"Charm","Beauty","Body","Refinement","Sensitivity","Libido","Constitution","Obedience","Service","Sex","Anal","Fetish"
            if target in target_dict:
                target = target_dict[target]
                
            target = "脱衣舞娘职业经验收益" if target == "dancer jp gains" else target
            target = "按摩技师职业经验收益" if target == "masseuse jp gains" else target
            target = "女服务员职业经验收益" if target == "waitress jp gains" else target
            target = "表演艺伎职业经验收益" if target == "geisha jp gains" else target
            target = "肛交职业经验收益" if target == "anal jp gains" else target
            target = "性交职业经验收益" if target == "sex jp gains" else target
            target = "侍奉职业经验收益" if target == "service jp gains" else target
            target = "调教职业经验收益" if target == "fetish jp gains" else target
            target = "舞娘职业经验收益" if target == "dancer jp gains" else target
            target = "脱衣舞娘技能收益" if target == "dancer gains" else target
            target = "按摩技师技能收益" if target == "masseuse gains" else target
            target = "女服务员技能收益" if target == "waitress gains" else target
            target = "表演艺伎技能收益" if target == "geisha gains" else target
            target = "肛交技能收益" if target == "anal gains" else target
            target = "性交技能收益" if target == "sex gains" else target
            target = "侍奉技能收益" if target == "service gains" else target
            target = "调教技能收益" if target == "fetish gains" else target
            target = "经验收益" if target == "xp gains" else target
            target = "最大精力" if target == "max energy" else target
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

            target = "露出倾向增加" if target == "naked preference increase" else target
            target = "肛交倾向增加" if target == "anal preference increase" else target
            target = "性交倾向增加" if target == "sex preference increase" else target
            target = "侍奉倾向增加" if target == "service preference increase" else target
            target = "调教倾向增加" if target == "fetish preference increase" else target
            target = "群交倾向增加" if target == "group preference increase" else target
            target = "双飞倾向增加" if target == "bisexual preference increase" else target
            target = "所有性行为倾向增加" if target == "all sex acts preference increase" else target

            target = "舞娘职业经验得分" if target == "dancer jp bonus" else target
            target = "按摩师职业经验得分" if target == "masseuse jp bonus" else target
            target = "服务员职业经验得分" if target == "waitress jp bonus" else target
            target = "艺伎职业经验得分" if target == "geisha jp bonus" else target
            target = "肛交职业经验得分" if target == "anal jp bonus" else target
            target = "性交职业经验得分" if target == "sex jp bonus" else target
            target = "侍奉职业经验得分" if target == "service jp bonus" else target
            target = "调教职业经验得分" if target == "fetish jp bonus" else target
            target = "舞娘职业经验" if target == "dancer jp" else target
            target = "按摩师职业经验" if target == "masseuse jp" else target
            target = "服务员职业经验" if target == "waitress jp" else target
            target = "艺伎职业经验" if target == "geisha jp" else target
            target = "肛交职业经验" if target == "anal jp" else target
            target = "性交职业经验" if target == "sex jp" else target
            target = "侍奉职业经验" if target == "service jp" else target
            target = "调教职业经验" if target == "fetish jp" else target
            target = "舞娘结果评价" if target == "dancer results" else target
            target = "按摩师结果评价" if target == "masseuse results" else target
            target = "服务员结果评价" if target == "waitress results" else target
            target = "艺伎结果评价" if target == "geisha results" else target
            target = "肛交结果评价" if target == "anal results" else target
            target = "性交结果评价" if target == "sex results" else target
            target = "侍奉结果评价" if target == "service results" else target
            target = "调教结果评价" if target == "fetish results" else target

            target = "处女时获得的人气" if target == "virgin rep" else target
            target = "处女时获得的小费" if target == "virgin tip" else target
            target = "每天第一位客人的满意度" if target == "first customer satisfaction" else target
            target = "完美结果时获得的小费" if target == "perfect result tip" else target
            target = "完美结果时获得的经验" if target == "perfect result xp" else target
            target = "完美结果时获得的职业经验" if target == "perfect result jp" else target
            target = "每天第一位客人打赏的小费" if target == "first customer tip" else target
            target = "每天第一位客人给予的评价" if target == "first customer rep" else target
            target = "小费" if target == "tip" else target
            target = "所有技能上限值" if target == "all skill max" else target
            target = "所有技能属性" if target == "all skills" else target
            target = "外派任务效果" if target == "quest results" else target
            target = "外派培训效果" if target == "class results" else target
            target = "治疗效果" if target == "heal" else target
            target = "爱情得分" if target == "love bonus" else target
            target = "恐惧得分" if target == "fear bonus" else target
            target = "沉迷性行为+" if target == "positive fixation" else target
            target = "保安效果" if target == "security" else target
            target = "保洁效果" if target == "maintenance" else target
            target = "情绪收益" if target == "mood gains" else target
            target = "好感收益" if target == "love gains" else target
            target = "情绪" if target == "mood" else target
            target = "宣传效果" if target == "advertising" else target
            target = "客人数量" if target == "customers" else target
            target = "普通工作时接客人数" if target == "job customer capacity" else target
            target = "个人防御" if target == "defense" else target
            target = "作为妓女时接客人数" if target == "whore customer capacity" else target
            target = "训练时所需服从" if target == "train obedience target" else target
            target = "任意工作时所需服从" if target == "job obedience target" else target
            target = "作为妓女时所需服从" if target == "whore obedience target" else target
            target = "精力消耗" if target == "tiredness" else target
            target = "精力消耗" if target == "energy use" else target
            target = "满足保养费时的效用" if target == "positive upkeep modifier" else target
            target = "怪物经验" if target == "monster xp" else target
            target = "野兽经验" if target == "beast xp" else target
            target = "机器经验" if target == "machine xp" else target
            target = "种马经验" if target == "stallion xp" else target
            target = "精力恢复" if target == "energy" else target
            target = "经验" if target == "xp" else target
            target = "属性点" if target == "skill points" else target
            target = "玩家声望" if target == "prestige" else target
            target = "天赋点" if target == "perk" else target
            target = "结交新朋友修正" if target == "making friends" else target
            target = "来自友谊而获得的心情收益" if target == "mood gains from friendship" else target
            target = "所有性行为偏好" if target == "all sexual preferences" else target
            target = "所有性行为技能" if target == "all sex skills" else target
            target = "性行为激活要求" if target == "sex act requirements" else target
            target = "所有常规技能" if target == "all main skills" else target
            target = "多给保养费的情绪增益影响" if target == "positive upkeep mood modifier" else target
            target = "少给保养费的情绪减益影响" if target == "negative upkeep mood modifier" else target
            target = "只工作半天时精力回复量" if target == "half-shift resting bonus" else target
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
            target = "配饰加成" if target == "accessory" else target
            target = "项链加成" if target == "necklace" else target
            target = "戒指加成  " if target == "ring" else target

            target = "保养费" if target == "upkeep" else target
            target = "受伤天数" if target == "hurt" else target
            target = "人气收益" if target == "reputation gains" else target
            target = "卖淫收益" if target == "aconstitution gains" else target
            target = "舞娘职业经验收益" if target == "dancer jp gains" else target
            target = "舞娘职业经验收益" if target == "dancer jp gains" else target

            target = "名声" if target == "brothel reputation" else target
            target = "小费总额" if target == "total tip" else target
            target = "双飞概率" if target == "bisexual chance" else target
            target = "群交概率" if target == "group chance" else target
            target = "工作时客户的预算" if target == "job customer budget" else target
            target = "作为妓女时客户的预算" if target == "whore customer budget" else target
            target = "客户活动 " if target == "customer events" else target
            target = "疯狂" if target == "crazy" else target
            target = "服务员倾向" if target == "waitress preference" else target
            target = "舞娘倾向" if target == "dancer preference" else target
            target = "按摩师倾向" if target == "masseuse preference" else target
            target = "艺妓倾向" if target == "geisha preference" else target
            target = "侍奉倾向" if target == "service preference" else target
            target = "性交倾向" if target == "sex preference" else target
            target = "肛交倾向" if target == "anal preference" else target
            target = "调教倾向" if target == "fetish preference" else target
            target = "群交倾向" if target == "group preference" else target
            target = "双飞倾向" if target == "bisexual preference" else target
            target = "所有性行为倾向" if target == "all sex acts preference" else target
            target = "满意度" if target == "satisfaction" else target
            target = "每日爱情" if target == "love per day" else target
            target = "每日恐惧" if target == "fear per day" else target
            target = "理智消耗" if target == "sanity loss" else target
            target = "魔力消耗" if target == "mojo cost" else target
            target = "" if target == "" else target

            text1 = target + text2 + text1

            if target == "hurt":
                text1 += __(" damage{#1}")
            elif target in extended_sex_acts:
                text1 += __(" acts{#1}")
            elif target == "random item":
                text1 += "在工作时"

            if self.scales_with:

                if self.scales_with == "equipped":
                    text1 += __(" for each equipped item")

                elif self.scales_with == "cust nb":
                    text1 += __(" for each customer")
                elif self.scales_with == "job cust nb":
                    text1 += __(" for each customer when working")
                elif self.scales_with == "whore cust nb":
                    text1 += __(" for each customer when whoring")

                else:
                    # text1 += __("对于每点的") + __(self.scales_with)

                    if self.scales_with == "strength":
                        scalesxxx="（随主角力量递增）"
                    elif self.scales_with == "spirit":
                        scalesxxx="（随主角精神递增）"
                    elif self.scales_with == "charisma":
                        scalesxxx="（随主角魅力递增）"
                    elif self.scales_with == "speed":
                        scalesxxx="（随主角速度递增）"
                    elif self.scales_with == "charisma":
                        scalesxxx="（随主角魅力递增）"
                    elif self.scales_with == "defense":
                        scalesxxx="（随个人防御递增）"
                    elif self.scales_with in ("rep", "reputation"):
                        scalesxxx="（随个人名声递增）"
                    elif self.scales_with == "rank":
                        scalesxxx="（随阶级递增）"
                    elif self.scales_with == "equipped": # Counts every piece of equipment
                        scalesxxx="（随装备数递增）"
                    elif self.scales_with == "district":
                        scalesxxx="（随地区递增）"
                    else:
                        scalesxxx=self.scales_with
                    text1 += scalesxxx


            if self.duration > 0:
                text1 += " (持续时间: "

                if self.duration > 1:
                    text1 += str(self.duration) + " 次 - 效果不可叠加)"

                elif self.duration == 1:
                    text1 += "1次 - 效果不可叠加)"

            return __(text1)


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


    # class Item(object):
    #
    #     """This class is for inanimate objects that the MC or girls can own."""
    #
    #     def __init__(self, name, target, type, pic = None, template = False, rank = 1, max_rank = 5, rarity = 1, charges = None, price = 10000, effects = None, description = "", adjectives = None, sound = None, hidden_effect = False, pic_dir = None, sellable="type", giveable="type", usage="type"):
    #
    #         self.base_name = name
    #         self.name = name
    #         self.target = target
    #         self.type = type
    #         if pic_dir:
    #             self.pic_dir = pic_dir
    #         else:
    #             self.pic_dir = self.type.dir
    #
    #         if pic:
    #             self.pic = Picture(pic, "items/" + self.pic_dir + "/" + pic)
    #         else:
    #             self.pic = Picture("misc.webp", "items/misc/misc.webp")
    #
    #         self.template = template
    #         self.min_rank = rank
    #         self.rank = rank
    #         self.max_rank = max_rank
    #         self.rarity = rarity
    #         self.charges = charges
    #         self.base_price = price
    #         self.price = price
    #         if effects == None: effects = []
    #         self.base_effects = effects
    #         self.effects = effects
    #         self.equipped = False
    #         self.hidden_effect = hidden_effect
    #
    #         ## Inherits properties from item type
    #
    #         if usage == "type":
    #             self.usage = self.type.usage
    #         else:
    #             self.usage = usage
    #
    #         if self.usage in ("use", "auto") and not self.charges:
    #             self.charges = 1
    #
    #         self.slot = self.type.slot
    #         self.filter = self.type.filter
    #
    #         if sellable == "type":
    #             self.sellable = self.type.sellable
    #         else:
    #             self.sellable = sellable
    #         if giveable == "type":
    #             self.giveable = self.type.giveable
    #         else:
    #             self.giveable = giveable
    #
    #         ## An individual item can override type adjectives and sound if necessary
    #
    #         if adjectives:
    #             self.adjectives = adjectives
    #
    #         else:
    #             self.adjectives = self.type.adjectives
    #
    #         if sound:
    #             self.sound = sound
    #         else:
    #             self.sound = self.type.sound
    #
    #         self.base_description = description
    #         self.update_description()
    #
    #     def update_description(self): # self.description stores the effect description only (to split the tooltips)
    #
    #         if self.hidden_effect:
    #             self.description = ""
    #
    #         else:
    #             self.description = get_description("", self.effects, final_dot=False)
    #
    #             if self.usage in ("use", "auto"):
    #                 if self.charges > 1:
    #                     self.description += " (" + str(self.charges) + " uses left)"
    #
    #         if self.usage == "gift":
    #             if self.description:
    #                 self.description += ", Gift"
    #             else:
    #                 self.description += "Gift"
    #
    #     def get_pic(self, x = int(config.screen_height*0.0694), y = int(config.screen_height*0.0694)):
    #         return self.pic.get(x = x, y = y)
    #
    #     def get_key(self):
    #         return (self.type.name, self.rank, self.base_name, self.price)
    #
    #     def has_effect(self, type="any", target="any"):
    #         for eff in self.effects:
    #             if (type in (eff.type, "any")) and (target in (eff.target, "any")):
    #                 return True
    #         return False
    #
    #     def get_effect(self, type, target):
    #         return get_effect(self, type, target, iterate=True)
    #
    #     def can_wear(self, type):
    #
    #         if self.usage != "wear":
    #
    #             return False
    #
    #         elif self.target == type:
    #             return True
    #
    #         else:
    #             return False
    #
    #
    #     def can_use(self, type):
    #
    #         if self.usage not in ("use", "auto"):
    #
    #             return False
    #
    #         elif self.target == type:
    #             return True
    #
    #         else:
    #             return False
    #
    #
    #     def use_me(self, nb = 1):
    #
    #
    #         if self.charges >= nb:
    #
    #             self.charges -= nb
    #
    #             if self.charges <= 0:
    #                 return "used_up"
    #
    #             else:
    #                 return self.charges
    #
    #         else:
    #
    #             renpy.say("", "Not enough charges (" + str(self.charges) + ")")
    #
    #             return "no charges"
    #
    #         self.update_description()
    #
    #     def get_acts(self, owner, counterpart):
    #         possible_acts = []
    #
    #         if owner.type == "NPC":
    #             if owner in (NPC_renza, NPC_captain):
    #                 possible_acts.append("bargain")
    #             else:
    #                 possible_acts.append("buy")
    #                 if counterpart:
    #                     if self.can_wear(counterpart.type):
    #                         possible_acts.append("buy and equip")
    #
    #         if counterpart and counterpart.type == "NPC":
    #             if self.sellable:
    #                 possible_acts.append("sell")
    #
    #         if owner.type in ("MC", "girl"):
    #             if self.can_use(owner.type):
    #                 possible_acts.append("use")
    #             if self.can_wear(owner.type):
    #                 if not self.equipped:
    #                     possible_acts.append("equip")
    #                 else:
    #                     possible_acts.append("unequip")
    #             if counterpart and counterpart.type == "girl":
    #                 if self.usage == "gift":
    #                     possible_acts.append("gift")
    #                 else:
    #                     possible_acts.append("give")
    #                     if self.can_wear("girl"):
    #                         possible_acts.append("give and equip")
    #                     if self.can_use("girl"):
    #                         possible_acts.append("use on her")
    #
    #         if owner.type == "girl":
    #             if counterpart and counterpart.type == "MC":
    #                 possible_acts.append("take")
    #
    #
    #
    #         return possible_acts
    #
    #
    #     def get_price(self, operation):
    #
    #         modifier = MC.get_modifier(operation)
    #
    #         baseprice = self.price
    #
    #         finalprice = round_int(baseprice * modifier)
    #
    #         return finalprice
    #
    #
    #     def available_at_rank(self, rank): # Useless?
    #
    #         if rank >= self.min_rank and rank <= self.max_rank:
    #             return True
    #         else:
    #             return False
    #
    #
    #     def transform(self, target_rank): # Transforms an item in a better or worse version of itself
    #
    #         if self.template == True:
    #             self.name = __("{0} {1}").format(__(quality_prefix[self.adjectives + "_" + str(target_rank)]), __(self.base_name.lower()))
    #
    #             self.price = round_int(quality_modifier[target_rank] * self.base_price)
    #
    #             self.effects = []
    #
    #             for eff in self.base_effects:
    #                 if target_rank > 0:
    #                     value = target_rank * eff.value
    #                 else:
    #                     value = eff.value / 2
    #
    #                 self.effects.append(Effect(eff.type, eff.target, value))
    #
    #             self.update_description()
    #
    #             return self
    #
    #         else:
    #             return None
    #
    #     def generate_new_item(self, target_rank): # Creates new Item from this template item
    #
    #         if self.template == True:
    #
    #             new_it = copy.deepcopy(self)
    #
    #             new_it.name = __("{0} {1}").format(__(quality_prefix[self.adjectives + "_" + str(target_rank)]), __(self.base_name.lower()))
    #             new_it.price = round_int(quality_modifier[target_rank] * self.base_price)
    #
    #             if self.rarity in ("S", "U", "M"):
    #                 new_it.rarity = self.rarity
    #             else:
    #                 new_it.rarity = self.rarity + target_rank - self.min_rank
    #
    #             new_it.effects = []
    #
    #             for eff in self.effects:
    #                 eff = copy.deepcopy(eff)
    #
    #                 if target_rank > 0:
    #                     eff.value = target_rank * eff.value
    #                 else:
    #                     eff.value = eff.value / 2
    #
    #                 new_it.effects.append(eff)
    #
    #             new_it.min_rank = max(target_rank - 2, 0)
    #             new_it.rank = min(target_rank, 6)
    #
    #             new_it.update_description()
    #
    #
    #             return new_it



    class Room(object):

        """This class is for rooms in a brothel, normal (bedrooms) and special (commons)"""

        def __init__(self, name, level = 0, type = "bedroom", job = None, cost=0): # Level is used for price of special rooms

            self.name = name
            self.level = level # Should be replaced with rank
            self.type = type # bedroom or special
            self.cust_limit = 0
            self.job = job
            self.cost = cost
            self.girls = [] # Used for the master bedroom
            self.build_pics()

        def build_pics(self):
            self.pic_path = "brothels/rooms/" + room_pics[self.name]
            self.pic = Picture(path=self.pic_path)
            self.bg = {}
            self.bg["clean"] = "bg " + self.name

            if self.type == "special":
                self.bg["clean"] = "bg " + self.name
                root = "bg " + self.name

                for dirt_state in ("clean enough", "dusty", "dirty", "disgusting", "fire"):
                    name = root + {"clean enough" : "", "dusty" : " dusty", "dirty" : " dirty", "disgusting" : " verydirty", "fire" : " verydirty"}[dirt_state]
                    #renpy.image(self.name + " " + dirt_state, ProportionalScale(path, config.screen_width, config.screen_height))
                    self.bg[dirt_state] = name
            else:
                renpy.image("bg " + self.name, ProportionalScale(self.pic_path))

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
                if renpy.call_screen("yes_no", __("Do you really want to choose the ") + __(self.name) + __(" as your free room?")):
                    renpy.play(s_spell, "sound")
                    self.level = 1
                    self.update_cust_limit()
                    brothel.free_room = False

            elif self.get_price() >= MC.gold:
                renpy.say(sill, "Sorry Master, you do not have enough gold to build this room.")


            elif renpy.call_screen("yes_no", __("Are you sure you want to build the ") + __(self.name) + __(" for ") + str(self.get_price()) + " gold?"):
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
                renpy.say(sill, "Sorry Master, you do not have enough gold to upgrade this room.")
            elif renpy.call_screen("yes_no", __("Are you sure you want to upgrade the ") + __(self.name) + __(" for ") + str(self.get_price()) + " gold?"):
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

        def get_bg(self, dirt_state="clean"):
            if self.type == "special":
                return self.bg[dirt_state]
            else:
                return self.bg["clean"]

        def get_price(self):
            if self.cost:
                return self.cost
            else:
                return brothel.get_room_price(self.type)

        def get_description(self):
            if self.type == "master":
                if self.level > 1:
                    desc = "可以容纳最多{b}" + str(self.level) + "个女孩{/b}。 女孩们每天晚上都可以在你的房间里接受免费的{b}私人指导{/b}。"
                elif self.level == 1:
                    desc = "只能容纳{b}一个女孩{/b}。 女孩们每天晚上都可以在你的房间里接受免费的{b}私人指导{/b}。"
                else:
                    desc = "你的房间太小了，无法让女孩在房间里接受私人指导。"

                if self.level < brothel.rank:
                    desc += "花费{b}" + str(master_bedrooms[self.level+1].cost) + "金币{/b}扩建你的卧室。"
                elif self.level == 5:
                    desc += " {i}你的卧室已经达到了最高等级{/i}"

                return desc

            if brothel_firstvisit:
                return "修建一个{b}" + self.name + "{/b}让{b}" + girl_related_dict[self.job] + "{/b}服务客人。"
            elif self.level == 0:
                return "修建一个{b}" + self.name + "{/b}需要花费{b}" + str(self.get_price()) + "金币{/b}。"
            elif self.level < district.rank:
                return "现在{b}" + self.name + "{/b}可以容纳" + str(self.cust_limit) + "位顾客。扩建" + self.name + "需要花费{b}" + str(self.get_price()) + "金币{/b}以容纳更多顾客。"
            else:
                return "现在{b}" + self.name + "{/b}可以容纳" + str(self.cust_limit) + "位顾客。"

        def update_cust_limit(self, silent=False): # Returns value if changed
            _old = self.cust_limit
            self.cust_limit = room_capacity_dict[game.chapter] * self.level + brothel.get_effect("change", "room capacity") + brothel.get_effect("change", self.name + " room capacity")
            self.cust_limit = round_int(self.cust_limit * brothel.get_effect("boost", "room capacity") * brothel.get_effect("boost", self.name + " room capacity"))

            #<Chris Job Mod>
            if game.has_active_mod("chrisjobmod"):
                self.cust_limit = round_int(self.cust_limit * act_max_customers_modifier[self.job])
            #</Chris Job Mod>

            if self.cust_limit != _old:
                if not silent:
                    renpy.say(sill, "You may now entertain " + str(self.cust_limit) + " customers in the " + self.name + ". {w=1.0}{nw}")

            return self.cust_limit - _old

    class Quest(object):

        """This class is a template for quests and classes"""

        def __init__(self, type, name, main_stat, second_stat, other_stats, tags, description, sound = s_sigh, special_event = (None, 1.0), commit_label=None, return_label=None):

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
            self.commit_label = commit_label
            self.return_label = return_label

        def set_to(self, rank, pic, duration, special, requirements, pos_traits=None, neg_trait=None, gold=0, xp=0, rep=0):
            self.rank = round_int(rank)
            self.pic = pic
            self.duration = duration
            self.special = special
            self.requirements = requirements
            self.pos_traits = pos_traits or []
            self.neg_trait = None
            self.gold = gold
            self.xp = xp
            self.rep = rep
            self.energy = -5 * rank * self.duration

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
                    self.special = rand_choice(("Cheap", "Masterclass"))
                elif self.type == "quest":
                    self.special = rand_choice(("High reward", "Notorious"))
            else:
                self.special = None

            ## Set bonus and stat cap for classes

            if self.type == "class":

                self.bonuses = []

                #? Improved bonuses with rank
                self.bonuses.append([self.main_stat, self.duration*2 + rank, self.duration*4 + rank]) # Stores min/max bonuses to stat per day

                if rank > 1 and dice(100) < (rank-1) * 25: # Chance of adding second bonus at higher ranks
                    self.bonuses.append([self.secondary_stat, self.duration + rank//1.5, self.duration*3 + rank//1.5]) # Stores min/max bonuses to stat per day
                if rank > 3 and dice(100) < (rank-3) * 25: # Chance of adding third bonus at higher ranks
                    self.bonuses.append([rand_choice(self.other_stats), self.duration-1 + rank//2, self.duration*2 + rank//2]) # Stores min/max bonuses to stat per day

                self.stat_cap = 55 * rank #? Experimental

                self.capacity = 1 + dice(rank+1)


            ## Randomize stat requirements for quests

            if self.type == "quest":

                self.requirements = []

                # Normal stats have higher requirements than sx stats at earlier ranks then converge at rank 5
                if self.main_stat.capitalize() in gstats_main:
                    self.requirements.append([self.main_stat, 20 * rank + dice(40, rank)])

                else:
                    self.requirements.append([self.main_stat, 4 * rank**2 + dice(40, rank)])

                if dice(100) < (rank - 1) * 25: # Chance of adding second requirement at higher ranks

                    if self.main_stat.capitalize() in gstats_main:
                        self.requirements.append([self.secondary_stat, 20 * (rank-1) + dice(40, rank-1)])

                    else:
                        self.requirements.append([self.secondary_stat, 4 * (rank-1)**2 + dice(40, rank-1)])

                if dice(100) < (rank - 2) * 25: # Chance of adding third requirement at higher ranks

                    if self.main_stat.capitalize() in gstats_main:
                        self.requirements.append([rand_choice(self.other_stats), 20 * (rank-1) + dice(40, rank-1)])

                    else:
                        self.requirements.append([rand_choice(self.other_stats), 4 * (rank-1)**2 + dice(40, rank-1)])


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

                if self.special == "High reward":
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

                self.xp = (10 * rank**2) * self.duration * game.get_diff_setting("rewards") #? Experimental
                self.rep = (1 + 0.05*(self.duration-1)) * 2**(rank-1) * game.get_diff_setting("rewards")

                if self.special == "Cheap":
                    self.gold = round_int(0.75*self.gold)

            self.energy = -5 * rank * self.duration


        def test_eligibility(self, girl, ignore_status = False): # Returns a tuple: bool + ttip

            if not ignore_status:
                if girl.hurt > 0 or girl.away or girl.exhausted:
                    return (False, "Your girl is unable to work or study at the moment.")

            if self.type == "class":

                if MC.gold >= self.gold:

                    for stat, _min, _max in self.bonuses:
                        if girl.get_stat(stat, raw=True) < self.stat_cap:
                            return (True, "为%s报名这个培训班。" % girl.fullname)

                    return (False, "Your girl's skills are too high to learn anything from this class.")

                else:
                    return (False, "You do not have enough money to register a girl for this class.")


            elif self.type == "quest":

                for stat, value in self.requirements:
                    if girl.get_stat(stat) < value:
                        return (False, "Your girl doesn't meet the requirements for this assignment.")
                return (True, __("Send %s on this assignment.") % girl.fullname)

            raise AssertionError("Something is weird with " + self.type)

        def count_eligible_girls(self):

            eligible = sum(1 for girl in MC.girls if self.test_eligibility(girl, ignore_status=True)[0])

            return eligible

        def get_results(self, girl):

            title = __(self.type.capitalize()) + __(" completed")
            description = girl.fullname + __(" has returned from her ") + __(self.type) + ". "

            if self.type == "class":

                # Only mood affects learning for now (from +5 to -5)
                perf = dice(6, 2) + girl.mood // 20

                # Having friends in the class improves learning (checked twice: on enrollment and when results are delivered)

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

                perf += girl.remembers("reward", "class good result")
                perf += girl.remembers("punish", "class bad result")

                if perf >= 12:
                    description += __("She studied very hard and made exceptional progress.")
                    boost = 2.0

                    girl.track_event("class good result", arg=__("She studied really hard for her ") + __(self.name)  + __(" class."))

                elif perf >= 9:
                    description += __("She listened carefully to her teacher and made good progress.")
                    boost = 1.5

                    girl.track_event("class good result", arg=__("She made good progress during her ") + __(self.name) + __(" class."))

                elif perf <= 2:
                    description += __("She was distracted and didn't pay much attention to her teacher, hindering her progress.")
                    boost = 0.75

                    girl.track_event("class bad result", arg=__("She didn't study hard during her ") + __(self.name) + __(" class."))

                elif perf <= 5:
                    description += __("She didn't care about the lessons at all, making almost no progress.")
                    boost = 0.5

                    girl.track_event("class bad result", arg=__("She didn't study at all for her ") + __(self.name) + __(" class."))

                else:
                    description += __("She made some progress with the help of her teacher.")
                    boost = 1.0

                if girl.class_friend_bonus > 0:
                    description += __(" She was happy to study alongside friends.")
                    girl.change_mood(10)
                elif girl.class_friend_bonus < -1:
                    description += __(" She didn't like that she was in the same class as her rival.")
                    girl.change_mood(-5)

                if self.special == "Masterclass":
                    boost *= 1.5

                boost *= girl.get_effect("boost", "class results") * game.get_diff_setting("rewards")

                changes = [(girl_related_dict[stat], round_int(girl.change_stat(stat, renpy.random.randint(_min, _max)*boost, custom_cap = self.stat_cap))) for stat, _min, _max in self.bonuses]

            elif self.type == "quest":

                # Only main stat affects result. Random variation from +6 to -6 times rank
                perf = girl.get_stat(self.main_stat) + girl.mood // 5 + dice(13, self.rank) - 7*self.rank - self.requirements[0][1]

                # Memories of rewards and punishment

                perf += girl.remembers("reward", "quest good result")
                perf += girl.remembers("punish", "quest bad result")

                # Story override #
                if self.tags == "Story":
                    perf = 0

                if perf >= 20 * self.rank:
                    description += __("{color=[c_orange]}Her performance was amazing. The customer was ecstatic!{/color}")
                    boost = 1.5

                    girl.track_event("quest good result", arg=__("She performed {color=[c_emerald]}amazingly well{/color} on a quest"))

                elif perf >= 10 * self.rank:
                    description += __("{color=[c_emerald]}She performed well. The customer was happy.{/color}")
                    boost = 1.25

                    girl.track_event("quest good result", arg=__("She performed {color=[c_emerald]}well{/color} on a quest"))

                elif perf < 0:
                    description += __("{color=[c_red]}She performed poorly. The customer was disappointed and refused to pay in full.{/color}")
                    boost = 0.75
                    girl.track_event("quest bad result", arg=__("She performed {color=[c_crimson]}badly{/color} while on a quest"))

                else:
                    description += __("She completed the assignment without incident.")
                    boost = 1.0

                had = []

                for trait in self.pos_traits:
                    if girl.has_trait(trait.name):
                        had.append(trait.get_past_tense())
                        boost *= 1.5

                if had:
                    description += __(" The customer was excited that she ") + __(and_text(had)) + "."

                if self.neg_trait:
                    if girl.has_trait(self.neg_trait.name):
                        description += __(" The customer was upset that she ") + __(self.neg_trait.get_past_tense()) + "."
                        boost /= 2.0

                boost *= girl.get_effect("boost", "quest results") # Note quest results boost is different from quest reward boost

                reward = round_int(self.gold*boost)
                self.rep = round_int(self.rep*boost)

                if self.special == "Notorious":
                    self.rep *= 2.0

                MC.gold += reward
                girl.add_log("quest_gold", reward, -1)

            xp = round_int(girl.change_xp(self.xp))
            rep = round_int(girl.change_rep(self.rep))
            energy, status = girl.change_energy(self.energy)

            if status == "exhausted":
                " She is {color=[c_red]}exhausted{/color} and will need to rest until she recovers."

            description += "\n"

            girl.add_log("total_xp", xp, -1)

            if self.type == "class":
                girl.add_log("class_xp", xp, -1)

                for stat, value in changes:
                    description += stat_increase_dict["stat"] % (__(stat.capitalize()), value)

            elif self.type == "quest":
                girl.add_log("quest_xp", xp, -1)

                description += stat_increase_dict["gold+"] % reward

            description += stat_increase_dict["xp_dark"] % xp
            description += stat_increase_dict["rep"] % rep
            description += stat_increase_dict["stat_neg"] % (__("Energy"), round_int(energy))

            if girl.ready_to_level():
                girl.level_up()
                description += stat_increase_dict["level"]

            if girl.ready_to_rank():
                description += stat_increase_dict["rank"]

            return title, description


init -10 python:

    class Goal(object):

        def __init__(self, type, value = 0, target = 0, label = "", channel="advance", max_chapter=None, blocking=True):

            self.type = type
            self.value = value
            self.target = int(target)
            self.label = label
            self.channel = channel
            self.max_chapter = max_chapter
            self.blocking = blocking
            self.description = ""

        def get_description(self):
            if not self.description:
                if self.type == "gold":
                    self.description = "你需要积攒" + str(int(self.value)) + "金币"

                elif self.type == "ranked":
                    self.description = "你需要拥有至少" + str(self.target) + "个" + rank_name[self.value] + "阶的奴隶" #修改了源代码使翻译通畅

                elif self.type == "reputation":
                    self.description = "你的青楼需要拥有" + str(int(self.value)) + "点声望"

                elif self.type == "prestige":
                    self.description = "你的角色需要拥有" + str(int(self.value)) + "点声望"

                elif self.type == "story":
                    self.description = self.value # value for story events must be text

                else:
                    self.description = "你已经进入了无尽模式, 请尽情享受游戏吧!"

            return self.description

        def reached(self):

            if not self.blocking:
                return True

            elif self.max_chapter and self.max_chapter > game.chapter:
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
                if story_flags[self.label] or not story_mode:
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

        def get_district(self): # Returns the location's parent district
            for d in ["slum", "warehouse", "docks", "gardens", "cathedra", "hold"]:
                if self in location_dict[district_dict[d].name]:
                    return district_dict[d]
            return None

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

            return "This location has girls: " + and_text(l)

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

        def __init__(self, name, pic = "aura1.webp", type = "passive", level = 0, cost = 0, effects = None, duration = None, sound = s_spell, description = "A basic spell."):

            self.name = name
            self.pic = Picture(pic, "spells/" + pic)
            self.type = type
            self.level = level
            self.cost = cost # Passive spells have a cost of zero
            if effects:
                self.effects = effects
            else:
                self.effects = []

            self.duration = duration
            self.sound = sound
            self.description = get_description(description, self.effects)

            self.auto = False

        def get_cost(self):
            return self.cost

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
                    attributes.append(attr[5:])

                # Checks every pairing and completes the girl's other attributes
                for tup in personality_attributes:
                    if tup[0] in attributes or tup[1] in attributes:
                        pass
                    else:
                        attributes.append(rand_choice(tup))

            return attributes





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
            if use_ini_sex and type == "pos" and self.name in girl.init_dict["sexual preferences/never_fixations"]:
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

            if use_ini_sex and self.name in girl.init_dict["sexual preferences/favorite_fixations"]:
                freq *= 3
            elif use_ini_sex and self.name in girl.init_dict["sexual preferences/disliked_fixations"]:
                freq /= 3
            else:
                for act in self.acts:
                    if use_ini_sex and act in girl.init_dict["sexual preferences/favorite_acts"]:
                        freq *= 2
                    elif use_ini_sex and act in girl.init_dict["sexual preferences/disliked_acts"]:
                        freq /= 2

            if type == "neg":
                freq = 144/freq # Probably no longer necessary to ensure weight is an integer with the changes to weighted_choice()

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
            elif self.condition == "has_worked":
                if girl.has_worked:
                    return True
            elif self.condition == "other_girls":
                if len(MC.girls) >= 2:
                    return True
            elif self.condition == "story":
                if girl.flags["story"] == 50: #! To do: Make it so that she can repeat earlier parts of the story
                    return True
            elif self.condition == "neg_fix":
                neg_fix = [fix.name for fix in girl.neg_fixations if girl.personality_unlock[fix.name]]
                if neg_fix:
                    return True
            elif self.condition == "free-form":
                if girl.will_do_sex_act("naked") and len(girl.get_trainable_sex_acts()) >= 3:
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
            elif self.condition == "debug_mode":
                if debug_mode:
                    return True

            else: # Other conditions should be strings that will be tested as a boolean flag (start flag name with ! to test for False)
                if self.condition.startswith("!") and not girl.flags[self.condition[1:]]:
                    return True
                elif girl.flags[self.condition]:
                    return True

            return False

        def is_available(self, girl, mode=None, free=False): # The option will display inactive if False. Returns a tuple with bool and a tooltip description.

            if girl.away:
                return False, "%s is away. You cannot interact with her." % girl.fullname

            if self.group == "train":
                if girl.exhausted:
                    return False, "You cannot train %s, because she is exhausted." % girl.fullname

                elif girl.hurt > 0:
                    return False, "You cannot train %s, because she is hurt." % girl.fullname

                elif not MC.training:
                    return False, "Training is disabled due to NewGame+ challenge"

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
                                    text1 += __(" or ")
                                text1 += girl_related_dict[cond] + " (" + girl_related_dict[pref] + ")"
                            else:
                                return False, __("You cannot train ") + girl_related_dict[self.act] + __(" yet. Requirements: ") + text1

                    elif self.type == "magic":
                        if magic_training_test_dict[self.act]:
                            for cond, pref in magic_training_test_dict[self.act]:
                                if compare_preference(girl, cond, pref):
                                    break
                                if text1:
                                    text1 += __(" or ")
                                text1 += girl_related_dict[cond] + " (" + girl_related_dict[pref] + ")"
                            else:
                                return False, __("You cannot train ") + girl_related_dict[self.act] + __(" yet. Requirements: ") + text1

                    if mode == "advanced":
                        if MC.interactions < 2 and not free:
                            return False, "你的行动力不足以使用进阶训练。"

                        if not girl.personality_unlock[self.act]:
                            return False, __("You need to train a girl at least once before you can access advanced training.")

                elif mode == "master_bedroom_add":
                    if not brothel.master_bedroom.can_have_girl():
                        return False, "私人指导名额已经满了。"

            if MC.interactions < 1 and self.AP_cost > 0 and not free:
                return False, "你今天没有行动次数了。"
            elif MC.interactions < self.AP_cost and not free:
                return False, "你没有足够的行动力来做这个。"
            elif self.get_gold_cost() and MC.gold < self.get_gold_cost():
                return False, "你没有足够的钱来报名培训 (" + str(self.get_gold_cost()) + "{image=img_gold})."
            elif self.group == "train" and girl.MC_interact_counters[self.group] >= 1:
                return False, "一天只能训练一个女孩一次。"
            elif self.group in ("reward", "discipline") and girl.MC_interact_counters[self.group] >= 1:
                return False, "一天只能奖励或惩罚一个女孩一次。"
            elif self.group in ("gold", "gift", "sex_reward", "rape", "offer") and girl.MC_interact_counters[self.group] >= 1:
                return False, "一天只能做一次。"
            elif self.group == "offer" and len(MC.girls) >= brothel.bedrooms:
                return False, "你的青楼满了，容不下另一个女孩。"
            elif self.group and girl.MC_interact_counters[self.group] >= 3:
                return False, "一天最多和一个女孩" + self.group + "3次。"
            elif self.label == "slave_master_bedroom_add" and not brothel.master_bedroom.can_have_girl():
                return False, "私人指导名额已经满了。"

            if self.condition == "free-form":
                return True, "在自由形式的训练中，你将能够在她感到舒服的不同的性行为之间切换。只有{b}最后选择的性行为{/b}才会真正接受训练。"

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
                renpy.call_screen("OK_screen", girl.fullname + "-Interaction resolving", "Group: [inter.topic.group]\nType: [inter.type]\nAction: [inter.topic.caption]\nReason: [inter.reason]\nResponse: [inter.response]\nAct: [inter.act]\nResult: [inter.result]\nMC Reaction: [inter.MC_reaction]")
            else:
                norollback()


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

            if girl.get_effect("special", "fear interactions"): # Evil power effect
                f += 1

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

                            lib += dice(5)

                            d = dice(6)

                            if d >= 6:
                                ob += dice(3)
                            elif d >= 5:
                                bea += dice(3)
                            elif d >= 4:
                                bod += dice(3)

                        elif self.act == "service":
                            en = -7

                            sv += dice(3)

                            d = dice(6)

                            if d >= 5:
                                sen += dice(3)
                            elif d >= 4:
                                cha += dice(3)

                        elif self.act == "sex":
                            en = -9

                            sx += dice(3)

                            d = dice(6)

                            if d >= 5:
                                lib += dice(3)
                            elif d >= 4:
                                bea += dice(3)

                        elif self.act == "anal":
                            en = -11

                            an += dice(3)

                            d = dice(6)

                            if d >= 5:
                                con += dice(3)
                            elif d >= 4:
                                bod += dice(3)

                        elif self.act == "fetish":
                            en = -13

                            fe += dice(3)

                            d = dice(6)

                            if d >= 5:
                                ob += dice(3)
                            elif d >= 4:
                                ref += dice(3)

                        elif self.act == "bisexual":
                            en = -9

                            if dice(6) >= 4:
                                sx += dice(3)
                            else:
                                sv += dice(3)

                            d = dice(6)

                            if d >= 5:
                                sen += dice(3)
                            elif d >= 4:
                                lib += dice(3)

                        elif self.act == "group":
                            en = -15

                            d = dice(6)

                            if d >= 5:
                                sv += dice(3)
                            elif d >= 3:
                                sx += dice(3)
                            else:
                                an += dice(3)

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
                    text1 += "\n" + __(misc_name_dict[s.capitalize()]) + ": " + shown

            text1 += "\n"

            for a in brk.keys():
                if brk[a] != None:
                    if debug_mode:
                        shown = str(round_int(brk[a]))
                    else:
                        shown = get_plus_rating(brk[a], "pref")

                    text1 += "\n" + __(a.capitalize()) + "喜好: " + shown
                else:
                    raise AssertionError("Unexpected breaking value for " + a + ". Please report this bug.")

            if inter:
                text1 += "\n女孩的互动: " + str(inter)
                girl.interactions += inter

            if virgin:
                text1 += "\n" + girl.fullname + "把她的处女献给了你。"

            text1 += "\n"

            if gd:
                MC.good += gd
            if ne:
                MC.neutral += ne
            if ev:
                MC.evil += ev

            if debug_mode:
                if gd:
                    text1 += "\n善良: " + str(gd)
                if ne:
                    text1 += "\n中立: " + str(ne)
                if ev:
                    text1 += "\n邪恶: " + str(ev)
            if p:
                MC.change_prestige(p)
                text1 += "\n声望: " + str(p)

            if not text2:
                text1 = "没有变化"
            renpy.call_screen("OK_screen", __("[girl.fullname] - 互动结果"), text1, dark=True, pic=girl.portrait, always_scrollbar=True)

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

        def __init__(self, name, folder, creator="Unknown", version= 1.0, pic=None, description="This is a mod for Brothel King.", help_prompts=None, init_label="", night_label = "", update_label = "", home_rightmenu_add_buttons=None, events=None, early_label=""):

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
            self.full_name = name + " v" + str(self.version) + ", from " + creator

            ## help_prompts is a list of tuples (name, label), each representing a menu prompt in the 'help/mod/mod options' menu.
            ## 'name' is the prompt message as it appears on the menu button, and 'label' is the target label it will call (not jump).
            ## Several actions can be added to the list by adding tuples (name, label) to the list, each separated by a comma
            self.help_prompts = []
            ## Adds [mod name] to prompt messages for clarity
            if help_prompts:
                for prompt in help_prompts:
                    self.help_prompts.append(("[[" + self.name + "] " + prompt[0], prompt[1]))

            ## Early init label: This will run after the game is started, before the district and brothel is set-up.
            self.early_label = early_label

            ## Init label: This will run after the game is started, after the district and brothel is set-up.
            self.init_label = init_label
            self.night_label = night_label
            self.update_label = update_label
            self.chapter_labels = {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None} # Stores a label to be called for a specific chapter

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
            if renpy.call_screen("yes_no", "你想要激活" + self.full_name + "模组吗？"):
                if not self.active or not persistent.mods[self.name]["active"]:
                    self.active = True
                    persistent.mods[self.name]["active"] = True
                    try:
                        game.activate_mod(self)
                    except:
                        pass
                    reset_updated_games()

                else:
                    renpy.notify(self.name + " is already active.")

        def deactivate(self):
            if renpy.call_screen("yes_no", "Do you really want to deactivate " + self.full_name + "? This might negatively affect games saved while this mod was on."):
                if self.active or persistent.mods[self.name]["active"]:
                    self.active = False
                    persistent.mods[self.name]["active"] = False
                    try:
                        game.deactivate_mod(self)
                    except:
                        pass
                    reset_updated_games()
                else:
                    renpy.notify(self.name + " couldn't be found among active mods.")

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
                    renpy.say("System", "Warning: Event set to a past date. Change the event time or delay.")

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
            self.pic = Picture(name + ".webp", "UI/challenges/" + name + ".webp")
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
                    return "Safe"
                elif chance > 0.8:
                    return "Very easy"
                elif chance > 0.6:
                    return "Easy"
                elif chance > 0.4:
                    return "Fair"
                elif chance > 0.2:
                    return "Hard"
                elif chance > 0.0:
                    return "Very hard"
                else:
                    return "Impossible"

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
            if self.location:
                self.base_description = self.location.menu[0]

        def get_pic(self, x, y):
            return self.pic.get(x, y)

        def activate_extractor(self, first=True):
            auto_extractors[self.name] = True
            auto_extractors[self.name + " ON"] = True
            if first:
                auto_extractors[self.name + " durability"] = 150
            self.location.menu = (self.base_description + " [[Extractor ON]", self.location.menu[1])

        def deactivate_extractor(self, final=True):
            auto_extractors[self.name + " ON"] = False
            if final:
                auto_extractors[self.name] = False
                self.location.menu = (self.base_description, self.location.menu[1])
            else:
                self.location.menu = (self.base_description + " [[Extractor OFF]", self.location.menu[1])


    class Furniture(object):

        """Furniture are upgrades for the brothel that provide permanent bonuses."""

        def __init__(self, name, type, pic=None, rank=2, chapter=2, cost=None, duration=0, effects=None, base_description="", upgrade=False, can_deactivate=False, hidden_effect=False):
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
            if hidden_effect:
                self.description = "{b}" + tl_cn(self.name,furniture_name_dict) + "{/b}" + ": " + base_description
            else:
                self.description = "{b}" + tl_cn(self.name,furniture_name_dict) + "{/b}" + ": " + get_description(base_description, effects)
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
                renpy.say(carpenter, __("I'll be finished in ") + str(self.duration) + __(" days. I'm sure you'll be happy with the result."))
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
                    renpy.call_screen("OK_screen", title = __("Furniture Upgraded"), message = __(self.upgrade) + __(" has been upgraded to a ") + __(self.name) + ".\n\n" + __(self.description), pic = self.pic, pic_size = "large")
            elif message:
                renpy.call_screen("OK_screen", title = __("Furniture Built"), message = __("A new ") + __(self.name) + __(" has been built.\n\n") + __(self.description), pic = self.pic, pic_size = "large")
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
                    renpy.call_screen("OK_screen", title = "Furniture destroyed", message = self.name + " has been destroyed and replaced with " + self.upgrade, pic = self.pic, pic_size = "large")
            elif message:
                renpy.call_screen("OK_screen", title = "Furniture destroyed", message = self.name + " has been destroyed.", pic = self.pic, pic_size = "large")
            self.activate()

        def activate(self):
            if not self.active and self.built:
                self.active = True
                update_effects()
                for e in self.effects:
                    if e.type == "event": # For events tied to the furniture
                        calendar.set_alarm(calendar.time, StoryEvent(e.target, arg=e.value))
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
            dlist = [(str(amount) + " " + __(misc_name_dict[resource])) for resource, amount in self.cost]

            return and_text(dlist)


    class Moon(object):

        """A new Moon appears every month. They have an effect on gameplay."""

        def __init__(self, name, effects=None, description="", sound=None):
            self.name = name.capitalize() + " Moon"
            self.pic = Picture(name + ".webp", "backgrounds/moons/" + name + ".webp")
            self.tb = ProportionalScale("backgrounds/moons/%s tb.webp" % name, *res_tb(25))
            if effects == None: effects = []
            self.effects = effects
            self.short_description = get_description("%s" % self.name, self.effects, separator=": ")
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

        def __init__(self, title="My cool achievement:\nWell done, bro!", description="No description", pic="misc.webp", pic_path="UI/achievements/", level_nb=1, target="", requirements="default", requirements2=None, custom_titles=None, multi=1): # {1 : C, 2 : B, 3 : A, 4 : S, 5 : X}

            self.title = title
            self.description = description
            if pic_path[-1] != "/": pic_path += "/"
            self.pic = Picture(path = pic_path + pic)
            self.level_nb = level_nb #
            self.target = target
            if requirements == "default": requirements = {1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5}
            self.requirements = requirements
            self.requirements2 = requirements2
            self.custom_titles = custom_titles # custom_titles should be a dictionary {level : custom_title}
            self.multi = multi # Number of crystals unlocked by achievement level

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

            elif self.target == "furniture": #?
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
                if MC.get_stat(self.target[3:], raw=True) >= 10:
                    return self.unlock()

            elif self.target == "good":
                if MC.get_alignment() == self.target:
                    if MC.get_alignment_delta("good") > 50:
                        return self.unlock()

            elif self.target == "neutral":
                if MC.get_alignment() == self.target:
                    if MC.get_alignment_delta("neutral") > 50:
                        return self.unlock()

            elif self.target == "evil":
                if MC.get_alignment() == self.target:
                    r = MC.get_alignment_delta("evil") # Smallest gap between evil and neutral/good points

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

            elif self.target.startswith("perform"):
                r = game.check(self.target)

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
            elif self.custom_titles:
                return self.custom_titles[level]
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
                    if isinstance(self.requirements[level], int):
                        return self.description % '{:,}'.format(self.requirements[level])
                    else:
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
                return "{b}特质{/b}: " + and_text([t.name for t in target], " 或 ")

            elif spe == "perk":
                return "{b}天赋{/b}: " + target.name

            elif spe == "fix":
                return "{b}正面癖好{/b}: " + and_text([tl_cn(f.name.capitalize(), girl_related_dict) for f in target], " 或 ")

            elif spe == "farm":
                return "{b}弱点{/b}: " + tl_cn(target.capitalize(), farm_related_dict)

            elif spe == "item":
                return "{b}衣着要求{/b}: " + tl_cn(target.name, misc_name_dict)

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
                task_desc += "{b}{i}" + tsk.title + "{/i}{/b}\n"
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
                        raise AssertionError("Contract requirement out of bounds: %s (current district: %s)" % (self.limits[req], district.rank))

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
                    r.append("{b}"+ __(girl_related_dict[req[4:].capitalize()]) + "{/b} %s及以上" % ("{image=img_star}" * self.limits[req]))
                elif req.startswith("skill"):
                    r.append("{b}" + __(stat_name_dict[req[6:].capitalize()]) +  " " + str(self.limits[req]) + "{/b}及以上")
                elif req.startswith("pref"):
                    r.append("{b}" + __(girl_related_dict[req[5:].capitalize()]) + "性癖: " + girl_related_dict[self.limits[req].capitalize()] + "{/b}及以上")

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


    class NGPSetting(object):

        """A class holding a single NGP setting."""

        def __init__(self, name, type, label=None, values=None, cost=0, ttip=""):
            self.name = name
            self.type = type
            self.label = label or name.capitalize() # The label used in the NG+ menu
            self.costs = make_list(cost)

            # Manual value setting
            if values:
                if type == "gold" or self.name == "starting chapter": # gold option works differently because it is not a finite list
                    self.values = values
                else: # settings with finite lists add 'option 0' at the beginning to represent deactivated status
                    self.values = [0] + values

            # Automatic value setting
            elif self.type == "bool":
                self.values = [0, 1]
            elif self.type == "dispenser":
                self.values = [None, "once", "monthly", "weekly"]
            else: # As many ranks as are provided for the cost
                self.values = range(0, len(self.costs)+1)

            try:
                self.index = persistent.NGPsettings[name]
            except:
                self.index = persistent.NGPsettings[name] = 0

            self.ttip = ttip

        def get(self):
            if self.type == "gold": # gold is a multiple of 100g
                return (self.index*100)

            return self.values[self.index]

        def read(self): # Apply display format to 'get' value. # Types: gold, resources, int, bool, plus, boost, dispenser, item, pref, girl
            if self.type == "gold":
                return '{:,}'.format(starting_gold + self.get())
            elif self.type == "int":
                return '{:,}'.format(self.get())
            elif self.type == "bool":
                return {0: "Off", 1: "On"}[self.index]
            elif self.type in ("item", "resources"):
                return {0: "None", 1: "Basic", 2: "Advanced", 3: "Master"}[self.index]
            elif self.type == "plus":
                return "+%i" % self.get()
            elif self.type in ("boost", "pref"):
                return {0: "None", 1: "Moderate", 2: "Strong", 3: "Strongest"}[self.index]
            elif self.type == "girl rank":
                return {0: "None", 2: "B rank", 3: "A rank", 4: "S rank"}[self.get()]
            return str(self.get()).capitalize()

        def get_used(self):
            if self.type == "gold":
                s = 0
                for i in range(self.index):
                    s+= self.get_cost(-i-1)
                return s
            return sum(self.costs[:self.index])

        def can_raise(self, budget):
            if self.index >= len(self.values)-1 and self.type != "gold":
                return False
            elif debug_mode:
                return True
            elif self.get_cost() > budget:
                return False
            elif self.type == "gold": # No ceiling for gold
                return True
            return True

        def _raise(self):
            if self.index < len(self.values)-1 or self.type == "gold":
                self.index += 1

        def can_lower(self):
            if self.index == 0:
                return False
            return True

        def _lower(self):
            if self.index > 0:
                self.index -= 1

        def reset(self):
            self.index = 0
            self.record()

        def get_cost(self, mod=0): # self.costs[i] is the cost to raise to level i+1
            level = self.index + mod

            if debug_mode:
                return 0
            elif self.type == "gold": # values for gold are tresholds
                for i in range(len(self.values)):
                    if self.index+mod < self.values[i]:
                        return self.costs[i]
            elif self.index+mod < len(self.values)-1:
                return self.costs[self.index+mod]
            return 0

        def get_refund(self):
            if self.index > 0:
                return self.get_cost(-1)
            return 0

        def get_ttip(self, context = "base"): # type can be "base", "plus" or "minus"
            if context == "base":
                if self.type == "resources" and self.index > 0:
                    return self.ttip + " Will receive " + and_text(["+%i of each rank %i resource" % (self.values[i+1], i+1) for i in range(self.index)]) + "."
                elif context == "girl" and self.index > 0:
                    return self.ttip + " A Rank %i girl will join your brothel on Day 1." % self.get()
                return self.ttip

            elif context == "plus":
                if self.type == "bool":
                    return "Activate " + self.name + " for {image=tb crystal} %i."
                elif self.type == "boost":
                    return "Boost " + self.name + " for {image=tb crystal} %i."
                elif self.type == "dispenser":
                    return "Increase rate of production of this item for {image=tb crystal} %i."
                elif self.type == "item":
                    if self.get():
                        return "Increase your magic notebook's capacities for {image=tb crystal} %i (full information)."
                    else:
                        return "Increase your magic notebook's capacities for {image=tb crystal} %i (partial information)."
                elif self.type == "pref":
                    return "Increase base sexual preferences for all girls for {image=tb crystal} %i."
                else:
                    return "Increase " + self.name + " for {image=tb crystal} %i."

            elif context == "minus":
                if self.type == "bool":
                    return "Deactivate " + self.name + " and refund {image=tb crystal} %i."
                elif self.type == "boost":
                    return "Reduce " + self.name + " boost and refund {image=tb crystal} %i."
                elif self.type == "dispenser":
                    return "Decrease rate of production of this item and refund {image=tb crystal} %i."
                elif self.type == "item":
                    if (self.get()-1):
                        return "Decrease your magic notebook's capacities and refund {image=tb crystal} %i (partial information)."
                    else:
                        return "Decrease your magic notebook's capacities and refund {image=tb crystal} %i (no information)."
                elif self.type == "pref":
                    return "Decrease base sexual preferences for all girls and refund {image=tb crystal} %i."
                else:
                    return "Decrease " + self.name + " and refund {image=tb crystal} %i."

        def record(self):
            persistent.NGPsettings[self.name] = self.index

        def recall(self):
            self.index = persistent.NGPsettings[self.name]


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
                raise AssertionError("No path provided for the Picture() object")

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
                return ProportionalScale(self.path, int(config.screen_height*0.2111), int(config.screen_height*0.2111), yalign = 1.0)

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
                    return ProportionalScale(image_path, int(config.screen_height*0.2), int(config.screen_height*0.2), yalign = 1.0)

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

            if self.path in persistent.pic_ignore_list:
                return False

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
                for _tag in current_tag_list:
                    filename = filename.replace(_tag, ' ')
                    new_len = len(filename)
                    if (new_len != old_len):
                        old_len = new_len
                        self.oldtags.append(_tag)
                        self.tags += tag_list_dict[_tag]

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
            if self._m1_BKclasses__hashcode is None :
                BLOCKSIZE = 65536
                hasher = hashlib.sha256()
                with open(config.gamedir + "/" + self.path, 'rb') as afile:
                    buf = afile.read(BLOCKSIZE)
                    while len(buf) > 0:
                        hasher.update(buf)
                        buf = afile.read(BLOCKSIZE)
                self._m1_BKclasses__hashcode = hasher.hexdigest()
            return self._m1_BKclasses__hashcode


        # gets the filesize
        # lazily initialized because its only needed by packstate check, not during normal gameplay
        def get_filesize(self):
            if self._m1_BKclasses__filesize < 0:
                self._m1_BKclasses__filesize = os.path.getsize(config.gamedir + "/" + self.path)
            return self._m1_BKclasses__filesize


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


    class ProportionalScale(renpy.Displayable):
        '''Resizes a renpy image to fit into the specified width and height.
        The aspect ratio of the image will be conserved.'''
        def __init__(self, imgname, maxwidth=None, maxheight=None, **properties):
            super(ProportionalScale, self).__init__()
            self.imgname = imgname # Stores the image's relative path for unlocking the gallery
            self.width = maxwidth or config.screen_width
            self.height = maxheight or config.screen_height
            if not renpy.exists(imgname):
                imgname = "backgrounds/not_found.webp"
            self.image = Transform(imgname, size=(self.width, self.height), fit="contain", **properties)

        def render(self, width, height, st, at): # Used for rendering
            return renpy.render(self.image, self.width, self.height, st, at)

        def visit(self): # Used for predicting
            return [ self.image ]

        def per_interact(self): # Used for rollback
            renpy.redraw(self, 0)

    # class ProportionalScale(im.ImageBase):
    #     '''Resizes a renpy image to fit into the specified width and height.
    #     The aspect ratio of the image will be conserved.'''
    #     def __init__(self, imgname, maxwidth=None, maxheight=None, bilinear=True, **properties):
    #         img = im.image(imgname)
    #         super(ProportionalScale, self).__init__(img, maxwidth, maxheight, bilinear, **properties)
    #         self.imgname = imgname # Stores relative path from the 'game/' folder
    #         self.image = img
    #         if maxwidth: # Set maxwidth as None to ignore
    #             self.maxwidth = int(maxwidth)
    #         else:
    #             self.maxwidth = config.screen_width
    #         if maxheight: # Set maxheight as None to ignore
    #             self.maxheight = int(maxheight)
    #         else:
    #             self.maxheight = config.screen_height
    #         self.bilinear = bilinear
    #
    #     def load(self):
    #         #<Chris12 NotFound>
    #         # Loads a neutral image instead of failing, in case an image does not exist
    #         try :
    #             child = im.cache.get(self.image)
    #         except IOError :
    #             # renpy.notify("Missing: " + self.imgname) # Commented out because it causes bugs in the CG gallery. Requires investigation
    #             child = im.cache.get(Image("backgrounds/not_found.webp"))
    #         #</Chris12 NotFound>
    #
    #         width, height = child.get_size()
    #
    #         ratio = min(self.maxwidth/float(width), self.maxheight/float(height))
    #         width = ratio * width
    #         height = ratio * height
    #
    #         if self.bilinear:
    #             try:
    #                 renpy.display.render.blit_lock.acquire()
    #                 rv = renpy.display.scale.smoothscale(child, (width, height))
    #             finally:
    #                 renpy.display.render.blit_lock.release()
    #         else:
    #             try:
    #                 renpy.display.render.blit_lock.acquire()
    #                 rv = renpy.display.pgrender.transform_scale(child, (newwidth, newheight))
    #             finally:
    #                 renpy.display.render.blit_lock.release()
    #         return rv
    #
    #     def predict_files(self):
    #         return self.image.predict_files()

#### END OF BK CLASSES ####
