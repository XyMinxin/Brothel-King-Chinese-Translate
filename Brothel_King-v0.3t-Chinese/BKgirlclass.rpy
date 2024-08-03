####            GIRL CLASS FOR B KING             ####################################################
##        This is the girl class.                   ##################################################
##         Others classes and functions are         ##################################################
##             in separate files.                   ##################################################


init -2 python:


## GIRLS GIRLS GIRLS! ##


    class Girl(object): #Attributes: name, lastname, age, description, pictures, stats, status, inventory, character

        """This class is for free and working girls in the game. This should probably inherit from the NPC
        class, but I'm not using inheritance."""


## CONSTRUCTOR METHODS

        def __init__(self): # Note: Init is not finalised until the randomize method is called

            self.type = "girl"

            # Placeholder information (changed after girl creation)
            self.id = 0 # Changed externally when creating the girl (create_girl() / get_girls() functions)
            self.pack_name = ""
            self.path = ""
            self.ini = None
            self.portrait = None
            # self.files = [] # <Chris12 PackState - moved to GirlFilesDict />
            # self.pics = [] # <Chris12 PackState - moved to GirlFilesDict />

            # Experience and rep
            self.rank = 1
            self.level = 1
            self.xp = 0
            self.rep = 0
            self.defense = 0
            self.upgrade_points = 0
            self.perk_points = 4
            self.original_price = 0
            self.jp = {
                       "waitress" : 0,
                       "dancer" : 0,
                       "masseuse" : 0,
                       "geisha" : 0,
                       "service" : 0,
                       "sex" : 0,
                       "anal" : 0,
                       "fetish" : 0
                       }
            self.job_level = {
                       "waitress" : 0,
                       "dancer" : 0,
                       "masseuse" : 0,
                       "geisha" : 0,
                       "service" : 0,
                       "sex" : 0,
                       "anal" : 0,
                       "fetish" : 0
                       }
            self.log = {} # Dictionary including all girl logged stats

            # Traits, Perks, Items and effects
            self.traits = []
            self.perks = []
            self.archetypes = copy.copy(archetype_dict) # Perk archetypes (as defined in BKperks.rpy)

            self.items = []
            self.equipped = []
            self.slots = girl_inventory_slots

            self.effects = []
            self.effect_dict = defaultdict(list)
            self.current_food_effect = defaultdict(bool)

            # Job and statuses
            self.resting = False # Forces a resting status on the girl regardless of schedule
            self.job = None # Girl's assigned job. She will still rest or quest according to her schedule
            self.old_job = None # To be phased out, kept here for possible backwards compatibility

            self.has_worked = False
            self.farm = False # Farm girls should be in 'farm.girls'. This shouldn't be needed: to be deleted if useless
            self.away = False # Indicates that the girl is away from the Brothel and unaffected by any brothel event or effect
            self.assignment = None
            self.street_days = 0

            self.exhausted = False # Indicates the girl is exhausted and cannot return to work until her energy is fully recovered
            self.hurt = 0 # If > 0, indicates the number of days the girl will stay incapacitated (before effects are applied)
            self.ran_away_counter = 0

            self.work_whore = False
            self.block_schedule = False
            self.farm_lock = False
            self.job_sort_value = 100
            self.workdays = {"Monday" : 100, "Tuesday" : 100, "Wednesday" : 100, "Thursday" : 100, "Friday" : 100, "Saturday" : 100, "Sunday" : 100} # Changed upon randomization

            self.badge = ""
            self.refused_populations = defaultdict(bool)

            # Interactions
            self.love = 0
            self.fear = 10 # Girls fear you at the beginning
            self.mood = 0

            self.MC_interact = False
            self.MC_interact_counters = defaultdict(int)
            self.MC_relationship_level = 0 # 0: stranger, 1: friend, 2: love interest, 3: girlfriend, 4: lover, 5: job offer
            self.MC_lied = None
            self.promised = False

            self.has_trained = []
            self.training_days = defaultdict(bool)
            self.magic_training = "balanced"

            self.spoiled = False
            self.spoil_points = 0
            self.terrified = False
            self.terrify_points = 0

            self.friends = []
            self.rivals = []
            self.g_compatibility = defaultdict(bool)

            self.custom_dialogue_label = None

            # Sexuality
            self.naked = False
            self.pos_fixations = []
            self.neg_fixations = []

            # Background
            self.location = ""
            self.origin = None
            self.hobbies = []
            self.likes = {"color" : None, "food" : None, "drink" : None}
            self.dislikes = {"color" : None, "food" : None, "drink" : None}

            self.flags = defaultdict(bool)

        def randomize(self, free=False, p_traits=None, n_trait=None, perks=None, force_original=False, level=1, personality=None):

            t0 = time.perf_counter()
            game.func_time_log2 = "\nstart: %s" % t0

            # 1. INIT GIRL

            self.free = free

            # Has a chance to generate original if it doesn't exist, otherwise creates a clone:
            # 'original' attribute stores the source for debugging

            if force_original:
                self.original = "forced original"
            elif self.init_dict["cloning options/unique"]:
                self.original = "unique"
            elif self.free and dice(100)<=15 and not self.count_occurences("all", original=True):
                self.original = "random free"
            elif not free and dice(100)<=5 and not self.count_occurences("all", original=True):
                self.original = "random slave"
            else:
                self.original = False

            if not self.original and self.ini:
                self.init_dict = clone_init_dict(self.init_dict)

            self.set_name()
            self.activation_date = calendar.time
            self.talked_to_date = None
            self.recent_events = defaultdict(list)
            self.relations = defaultdict(int)

            t1 = time.perf_counter()
            game.func_time_log2 += "\ninit: %s" % (t1 - t0)

            # 2. PERSONALITY

            self.generate_personality(personality)

            t2 = time.perf_counter()
            game.func_time_log2 += "\npersonality: %s" % (t2 - t1)

            t3 = self.generate_background(t2)

            # 3. LEVEL AND REGULAR SKILLS

            self.adjust_level(level)
            self.generate_stats()

            t4 = time.perf_counter()
            game.func_time_log2 += "\nstats: %s" % (t4 - t3)

            # 4. TRAITS AND PERKS

            self.generate_traits(p_traits, n_trait)

            if perks:
                for perk in perks:
                    self.acquire_perk(perk, forced=True)

            t5 = time.perf_counter()
            game.func_time_log2 += "\ntraits: %s" % (t5 - t4)

            # 5. ADJUSTMENTS

            self.auto_upkeep = True
            self.upkeep = -1
            self.upkeep_ratio = 1.0
            self.locked_upkeep = None
            self.generate_preferences()
            t6 = time.perf_counter()
            game.func_time_log2 += "\npreferences: %s" % (t6 - t5)

            self.upkeep = self.get_med_upkeep()
            self.energy = self.get_stat_minmax("energy")[1]
            self.init_sanity() # Used as a limit on farm powers (degrades over time, unrecoverable)
            self.last_power = 0
            self.broken = False
            self.streetdays = 0
            self.interactions = 0
            self.reset_interactions()

            # 6. PICTURES AND CHAR

            self.refresh_pictures(silent=True)

            t7 = time.perf_counter()
            game.func_time_log2 += "\nrefresh pictures: %s" % (t7 - t6)

            # Creating girl character (for talking)

            self.create_char()

            t8 = time.perf_counter()
            game.func_time_log2 += "\nchar creation: %s" % (t8 - t7)

            game.func_time_log2 += "\nend: %s" % t8
            game.func_time_log2 += "\ntotal time: %s" % (t8 - t0)

        ## Sanity (fuels evil farm powers before becoming broken) ##
        def init_sanity(self): # Sanity increases with rank and certain personality attributes
            if self.is_("very dom"):
                mod = 7
            elif self.is_("dom"):
                mod = 5
            else:
                mod = 4

            self.sanity = dice(11, self.rank) + mod * self.rank # Generates 5-15 sanity points per rank (+1/+3 for dom/vdom girls)

        def rank_up_sanity(self): # Sanity increases with rank and certain personality attributes
            if self.is_("very dom"):
                mod = 7
            elif self.is_("dom"):
                mod = 5
            else:
                mod = 4

            self.sanity += dice(11) + mod # Generates 5-15 sanity points per rank (+1/+3 for dom/vdom girls)

        def lose_sanity(self, cost): # Returns a message to display as narrator dialogue
            self.sanity -= cost*self.get_effect("boost", "sanity loss") - self.get_effect("change", "sanity loss")

            if self.sanity <= 0:
                self.broken = True

            return self.sanity_warning()

        def get_sanity(self):
            if self.broken:
                san = event_color["very bad"] % __("彻底玩坏")

            elif self.sanity < 5:
                san = event_color["very bad"] % __("接近崩溃")

            elif self.sanity < 10:
                san = event_color["bad"] % __("任人宰割")

            elif self.sanity < 20:
                san = event_color["a little bad"] % ("意志薄弱")

            elif self.sanity < 50:
                san = event_color["a little bad"] % ("有些动摇")

            else:
                san = event_color["a little bad"] % ("精神稳定")

            if debug_mode:
                san += " (%i)" % self.sanity

            return san


        def sanity_warning(self): # Returns a message to display as narrator dialogue
            if self.broken:
                calendar.set_alarm(calendar.time+1, StoryEvent("is_broken", arg=self, type = "morning"))
                renpy.play(s_scream_loud, "sound")
                return event_color["fear"] % (" %s 发出刺耳的尖叫声，让你全身都起了鸡皮疙瘩, 她吓得脸色苍白，浑身发抖。看起来效果很糟糕..." % self.name)

            elif self.sanity < 5:
                return event_color["very bad"] % ("%s 她的眼神中充满了绝望，她不由自主地颤抖着。如果你再靠近她一点，她就会像受伤的小动物一样呻吟。你可以看出，现在只要再推一把，就能把她的理智推向崩溃的边缘。" % self.name)

            elif self.sanity < 10:
                return event_color["bad"] % ("%s 她惊慌地抱着胸口，环顾四周，眼神中充满了恐惧。如果你坚持对她使用你的能力，她的心智最终会崩溃" % self.name)

            elif self.sanity < 20:
                return event_color["a little bad"] % ("%s 看起来很困惑，不知道发生了什么事。渐渐地，她的意识开始模糊。" % self.name)

            elif self.sanity < 50:
                if self.is_("dom"):
                    return event_color["a little bad"] % ("%s 似乎被刚刚发生的事吓到了，但还是装出一副镇定的样子。尽管她经历了这么多，她还是显得很不服气。" % self.name)
                else:
                    return event_color["a little bad"] % ("%s 她似乎被刚刚发生的事吓坏了，但她不想告诉别人。她把目光从你身上移开，努力忍住泪水。" % self.name)

            else:
                 return ("当 %s 恢复正常时，她似乎几乎没有察觉到刚刚发生在她身上的事情，但你知道她的潜意识里已经深受影响。" % self.name)


        def set_name(self): ## This creates the full name with or without lastname

            first, last = get_name(self.path)

            if self.original:
                if self.ini:
                    self.name = self.init_dict["identity/first_name"]
                    self.lastname = self.init_dict["identity/last_name"]
                    if not self.name and not self.lastname:
                        self.name, self.lastname = first, last
                else:
                    self.name, self.lastname = first, last

            else: # Clones will either receive _BK.ini settings as priority or option settings depending on option choice
                new_name = generate_name("girl")

                if persistent.gp_name_customization and self.init_dict["identity/first_name"] != "?rand" and self.init_dict["identity/first_name"]: # If _BK.ini has priority
                    self.name = self.init_dict["identity/first_name"] # Automatically set to "?rand" if unspecified in _BK.ini
                elif persistent.keep_firstname:
                    self.name = first
                elif self.init_dict["identity/first_name"] != "?rand" and self.init_dict["identity/first_name"]:
                    self.name = self.init_dict["identity/first_name"] # Automatically set to "?rand" if unspecified in _BK.ini
                else:
                    self.name = new_name[0]

                if persistent.gp_name_customization and self.init_dict["identity/last_name"] != "?rand": # If _BK.ini has priority
                    self.lastname = self.init_dict["identity/last_name"] # Automatically set to "?rand" if unspecified in _BK.ini
                elif persistent.keep_lastname:
                    self.lastname = last
                elif self.init_dict["identity/last_name"] != "?rand":
                    self.lastname = self.init_dict["identity/last_name"] # Automatically set to "?rand" if unspecified in _BK.ini
                else:
                    self.lastname = new_name[1]

            if self.name == "?rand" or not self.name:
                self.name = generate_name("girl")[0]

            if self.lastname == "?rand":
                self.lastname = generate_name("girl")[1]

            elif not self.lastname:
                self.lastname = ""

            self.set_fullname()

        def set_fullname(self):

            if self.init_dict["identity/inverted_name"]:
                self.fullname = self.lastname
                if self.name:
                    if self.fullname:
                        self.fullname += " "
                    self.fullname += self.name
            else:
                self.fullname = self.name
                if self.lastname:
                    if self.fullname:
                        self.fullname += " "
                    self.fullname += self.lastname

        def random_rename(self):
            self.name, self.lastname = generate_name("girl")
            self.set_fullname()

#             if self.lastname != "":
#                 self.fullname += " " + self.lastname

        def get_badge(self): # Returns the picture file name or None
            if not hasattr(self, 'badge') or self.badge not in badge_pics: # Sanity check
                self.badge = ""

            return self.badge

        def set_workdays(self): #Value is a percentage (0% = resting, 50% = working at half capacity, 100% = full capacity)

            i = calendar.day % 7

            self.workdays[weekdays[i-2]] = 0
            self.workdays[weekdays[i-3]] = 0

        def cycle_workday(self, day, reverse = False):

            if reverse:
                dict = {100 : 50, 50 : 0, 0 : 100}
            else:
                dict = {100 : 0, 50 : 100, 0 : 50}

            self.workdays[day] = dict[self.workdays[day]]

            renpy.restart_interaction()


        def update_files(self):
            #<Chris12 PackState>
            #Moved to GirlFilesDict - Should no longer be necessary
            return len(GirlFilesDict.get_pics(self.path)) > 0
            #</Chris12 PackState>


        def load_ini(self, search_for=None, skip_checks=False):

            self.init_dict = defaultdict(list)

            self.ini = GirlFilesDict.get_ini(self.path)

            if self.ini is not None:
                self.init_dict = read_init_file(self.ini, search_for=search_for, skip_checks=skip_checks)

        def read_ini(self, section=None, key=None): # Debug function

            if section and key:
                return self.init_dict[section + "/" + key]
            elif section:
                return [[k, v] for k, v in self.init_dict.items() if k.startswith(section)]
            elif key:
                return [[k, v] for k, v in self.init_dict.items() if k.endswith(key)]
            elif self.ini:
                return self.init_dict
            else:
                return "No init file"

        def load_pics(self):
            #<Chris12 PackState>
            #Moved to GirlFilesDict - Should no longer be necessary
            #</Chris12 PackState>
            pass

        def evaluate_girlpack(self): # Evaluate girl pack metrics to use for the girl pack rating

            start = datetime.datetime.now()
            main_cover_score, main_div_score, op_cover_score, op_div_score = 0.0, 0.0, 0.0, 0.0

            # Check pictures with 'Main' tags (including naked variations)

            for tag in normal_tags:
                currentList = get_pic_list(self, [tag], not_tags=["naked"], weighted=False)
                if len(currentList): main_cover_score += 1
                main_div_score += min(10, len(currentList)) # Only the first 10 pictures will count towards diversity average to avoid skewing pack rating

                currentList = get_pic_list(self, [tag], and_tags=["naked"], weighted=False)
                if len(currentList) : main_cover_score += 1
                main_div_score += min(10, len(currentList)) # Only the first 10 pictures will count towards diversity average to avoid skewing pack rating

            for tag in all_sex_acts:
                currentList = get_pic_list(self, [tag], not_tags=["group", "bisexual", "machine", "beast", "monster"], weighted=False)
                if len(currentList) : main_cover_score += 1
                main_div_score += min(10, len(currentList)) # Only the first 10 pictures will count towards diversity average to avoid skewing pack rating

                for tag2 in ("group", "bisexual") :
                    currentList = get_pic_list(self, [tag2], and_tags=[tag], not_tags=["machine", "beast", "monster"], weighted=False)
                    if len(currentList) :  main_cover_score += 1
                    main_div_score += min(10, len(currentList)) # Only the first 10 pictures will count towards diversity average to avoid skewing pack rating

            main_cover_score_total = len(normal_tags)*2 + len(all_sex_acts)*3
            timingResult = str(datetime.datetime.now() - start) + "\n"

            # Check pictures with optional tags (including all act variations)

            extended_sex_acts_tuples = [make_list(tag) for tag in extended_sex_acts]
            for tag in all_farm_tags:
                unfiltered = get_pic_list(self, [tag], weighted=False)
                for tag2 in extended_sex_acts_tuples:
                    currentList = list(filter(lambda pic : pic.has_tag(tag2), unfiltered))
                    if len(currentList) :  op_cover_score += 1
                    op_div_score += min(5, len(currentList)) # Only the first 5 pictures will count towards diversity average to avoid skewing pack rating

            for fix in fix_dict.values():
                unfiltered = get_pic_list(self, fix.tag_list[0], and_tags=[], not_tags=fix.not_list, weighted=False)
                for atag in fix.acts:
                    atagTuple = make_list(atag)
                    currentList = list(filter(lambda pic : pic.has_tags(atagTuple), unfiltered))
                    if len(currentList) :  op_cover_score += 1
                    op_div_score += min(5, len(currentList)) # Only the first 5 pictures will count towards diversity average to avoid skewing pack rating

            op_cover_score_total = len(all_farm_tags)*len(extended_sex_acts) + sum(len(fix.acts) for fix in fix_dict.values())
            timingResult += str(datetime.datetime.now() - start) + "\n"

            # Store result of evaluation

            if main_cover_score:
                main_av_pics = main_div_score/main_cover_score
            else:
                main_av_pics = 0

            if op_cover_score:
                op_av_pics = op_div_score/op_cover_score
            else:
                op_av_pics = 0

#            renpy.say(self.path, "main_cover_score_total " + str(main_cover_score_total) + ", op_cover_score_total " + str(op_cover_score_total) + ", main_cover_score " + str(main_cover_score) + ", op_cover_score " + str(op_cover_score) + ", main div " + str(main_div_score) + ", op div " + str(op_div_score) + ", main_av_pics " + str(main_av_pics) + ", op_av_pics " + str(op_av_pics))

#            with open(config.gamedir[:config.gamedir.rfind("/")] + "/ratinglog_" + self.name + ".txt", "wt") as log_file :
#                log_file.write(self.path + " (" + str(len(GirlFilesDict.get_pics(self.path))) + " images)\n" + timingResult + "\n\n" + " ".join(traceback.format_stack()))

            return {"main cover score" : main_cover_score/main_cover_score_total,
                    "main diversity average" : main_av_pics,
                    "optional cover score" : op_cover_score/op_cover_score_total,
                    "optional diversity average" : op_av_pics}


        def refresh_pictures(self, force_default=False, silent=False): # Every girl folder MUST have at least one pic with the 'profile' tag to be displayed properly

            if not silent:
                debug_notify("Refreshing pictures for %s" % self.fullname, pic=self.portrait)

            if force_default:
                self.portrait = get_pic(game, "portrait", "profile")
                self.profile = get_pic(game, "profile", "portrait")

            elif self in slavemarket.girls:
                self.portrait = self.get_pic("portrait", "profile", naked_filter = True, and_priority=False, soft=True)
                if self.naked:
                    self.profile = self.get_pic("market", "profile", "portrait", and_tags=["naked"], and_priority=False, not_tags=["beach", "nature", "date"], soft=True)
                elif persistent.naked_girls_in_slavemarket:
                    self.profile = self.get_pic("market", "profile", "portrait", not_tags=["beach", "nature", "date"], soft=True)
                else:
                    self.profile = self.get_pic("market", "profile", "portrait", not_tags=["naked", "beach", "nature", "date"], soft=True)

            elif self in game.free_girls: # Free girls will never be naked (unless activated in H menu). Profile picture changes according to current location
                if persistent.naked_girls_in_town and self.naked:
                    _and_tags = ["naked"]
                    _not_tags = ["masseuse", "waitress", "dancer"] # Reminder: not tags are dropped from right to left when unavailable
                else:
                    _and_tags = []
                    _not_tags = ["naked", "masseuse", "waitress", "dancer"] # Reminder: not tags are dropped from right to left when unavailable

                self.portrait = self.get_pic("portrait", "profile", and_tags=_and_tags, not_tags=_not_tags, and_priority=False, soft=True)
                if self.location.lower() in town_locations: # Reminder: self.location contains location name (string)
                    self.profile = self.get_pic("profile", "portrait", and_tags=_and_tags+["town"], not_tags = _not_tags+["beach", "nature"], soft=True)
                elif self.location.lower() in beach_locations:
                    self.profile = self.get_pic("profile", "portrait", and_tags=_and_tags+["beach"], not_tags = _not_tags+["town", "nature"], soft=True)
                elif self.location.lower() in nature_locations:
                    self.profile = self.get_pic("profile", "portrait", and_tags=_and_tags+["nature"], not_tags = _not_tags+["town", "beach"], soft=True)
                elif self.location.lower() in court_locations:
                    self.profile = self.get_pic("date", "geisha", "profile", and_tags=_and_tags+["profile"], not_tags = _not_tags+["beach", "nature"], soft=True)
                else:
                    self.profile = self.get_pic("profile", "portrait", and_tags=_and_tags, not_tags=_not_tags, soft=True)

            else: # Brothel girls
                not_tags =  ["rest", "wet", "beach", "public"] + [j for j in all_jobs if j != self.job]
                # edit: This suggested by darkzerotor, a lot of packs have too many pics that tag "profile" that dont make sense

                self.portrait = self.get_pic("portrait", "profile", naked_filter = True, and_priority=False, soft=True)
                self.profile = self.get_pic("profile", "portrait", not_tags=not_tags, naked_filter = True, soft=True)

            if not self.profile:
                #<Chris12 AutoRepair>
                # Use not_found.webp. No longer needs to renpy.quit(), since it has some image to show
                renpy.say("", event_color["bad"] % ("找不到以下女孩的头像或肖像照片: " + self.path + "。") + "\n请至少重命名她的一张照片，包括“个人资料”或“肖像”字样\n(e.g.: 'profile3.webp')\n完全删除她的目录，重新启动游戏，然后去帮助菜单和“修理女孩/MC图片”删除她。")
                self.profile = Picture(path="backgrounds/not_found.webp")
                # renpy.say("", "Exiting Ren'Py...{w=1}{nw}")
                # renpy.quit()
                #<Chris12 AutoRepair>

            if not self.portrait : self.portrait = Picture(path="backgrounds/not_found.webp") #<Chris12 AutoRepair - Use not_found />

            # Auto-unlocks CG for the gallery upon generating a profile and portrait as a convenience for the player (no need to interact with every girl)

            unlock_pic(self.portrait.path, silent=True)
            unlock_pic(self.profile.path, silent=True)

            self.create_char() # <Chris12 AutoRepair - Use the new portrait/>

        def create_char(self):

            if self.portrait != None:
                self.char = Character(self.name, color = c_pink, window_left_padding=int(res_portrait_size), show_side_image = self.portrait.get(side = True))
            else:
                self.char = Character(self.name, color = c_pink)

        #<Chris12 AutoRepair>
        # Checks if portrait and profile are still valid pictures
        # refreshes them if they are not
        def check_pictures(self):
            if self.portrait == None or not GirlFilesDict.contains_file(self.path, self.portrait.path):
                # renpy.notify(self.path + ": Portrait not found, updating images")
                self.refresh_pictures(silent=True)
            elif self.profile == None or not GirlFilesDict.contains_file(self.path, self.profile.path):
                # renpy.notify(self.path + ": Profile not found, updating images")
                self.refresh_pictures(silent=True)
        #</Chris12 AutoRepair>


        def generate_stats(self, sex=False): # regular stats are generated first, sx stats are generated after fixations

            if not sex:
                self.stats = []

                for stat in gstats_main:
                    if use_ini_skills:
                        self.stats.append(Stat(stat, "main", self, weight=self.init_dict["base skills/" + stat]))
                    else:
                        self.stats.append(Stat(stat, "main", self))
            else:
                self.sex_stats = []
                self.does = defaultdict(bool)

                for stat in gstats_sex:
                    self.sex_stats.append(Stat(stat, "sex", self))

        def adjust_level(self, level):
            self.level = level

            # Adjust rank
            while self.rank * 5 < self.level:
                self.rank += 1

            # Adjust XP and REP

            self.xp = xp_to_levelup[self.level-1]
            self.rep += rep_to_rank[self.rank-1]

            # Get perk points

            self.perk_points += (self.level-1) + self.level // 5

            #! No skill points are distributed for now, see if it works

        def will_do_farm_act(self, act, mode=None): # Returns 'accepted', 'resisted', 'refused' unless a specific mode is chosen, in which case it returns a boolean

            if not act:
                raise AssertionError("No act found for training")

            mod = self.get_sex_act_modifier(act) # Not in use for the moment

            score = self.preferences[act] + self.get_stat("obedience") + self.get_stat("libido")//2 + self.get_love()//2 + self.get_fear() # Love has less impact than fear

            if self.is_("very dom"):
                score -= 100
            elif self.is_("dom"):
                score -= 50
            elif self.is_("very sub"):
                score += 50

            if self.is_("very modest"):
                score -= 100
            elif self.is_("modest"):
                score -= 50
            elif self.is_("very lewd"):
                score += 50

            if score > 0:
                res = "accepted"
            elif score > -250:
                res = "resisted"
            else:
                res = "refused"

            # Generic case
            if not mode:
                return res

            # Specific mode selected
            elif mode == "gentle" and res == "accepted":
                return True
            elif mode == "tough" and res in ("resisted", "accepted"):
                return True
            elif mode == "hardcore":
                return True
            else:
                return False

        def will_rebel_in_farm(self, train_mode, reaction):

            if train_mode == "gentle":
                return False

            if self.is_("very dom"):
                diff = 200
            elif self.is_("dom"):
                diff = 100
            elif self.is_("very sub"):
                diff = 0
            elif self.is_("sub"):
                diff = 50

            if train_mode == "tough":
                diff -= 25
            elif train_mode == "hardcore":
                diff += 25

            if reaction == "accepted":
                diff -= 25
            elif reaction == "refused":
                diff += 25

            if dice(100) < (diff - self.get_love()//2 - self.get_fear() - self.get_stat("obedience")): # Fear impacts rebel chances more than love
                return True
            return False

        def farm_beg_test(self): # Determines if the girl will beg not to go to the farm
            r = dice(10)

            r -= self.get_stat("obedience") // 50

            if self.is_("very sub"):
                r += 2
            elif self.is_("sub"):
                r += 1
            elif self.is_("very dom"):
                r -= 1

            if self.is_("very modest"):
                r += 2
            elif self.is_("modest"):
                r += 1
            elif self.is_("very lewd"):
                r -= 1

            if farm.knows["weakness"][self]:
                r += 1

            if dice(10) >= 10:
                return True
            else:
                return False


        def will_do_sex_act(self, sex_act, use_desc=False):

            sex_act = sex_act.lower()

            if sex_act in all_sex_acts:
                tests = sex_act_test[sex_act]

                modifier = self.get_sex_act_modifier(sex_act)

                for stat, target in tests:
                    target += modifier

                    if self.get_stat(stat) < target:
                        if use_desc:
                            return False, girl_related_dict[sex_act.capitalize()] + " 无法激活。\n" + event_color["a little bad"] % ("她的 {b}" + girl_related_dict[stat.lower()] + "{/b} 属性太低了 (min: " + str(target) + ")。")
                        return False

            if self.get_effect("special", "minimum preference", raw=True):
                min_pref = self.get_effect("special", "minimum preference", raw=True) # Must return a string corresponding to a preference
            else:
                min_pref = "reluctant"

            if not compare_preference(self, sex_act, min_pref): # Means the girl is very reluctant or worse
                if use_desc:
                    return False, girl_related_dict[sex_act.capitalize()] + " 无法激活。\n" + event_color["a little bad"] % ("她对 {b}" + girl_related_dict[sex_act.lower()] + "{/b} 的接受能力太低了。她需要训练来适应。")
                return False

            if use_desc:
                return True, ""
            return True

        def toggle_sex_act(self, sex_act):

            sex_act = sex_act.lower()

            if self.does[sex_act]:
                self.does[sex_act] = False
                if not self.has_activated_sex_acts() and self.job == "whore":
                    self.set_job(None)
                    renpy.say("", self.fullname + " 如果你禁止所有的性行为，她就不能继续做妓女了。")
                return True, ""

            else:

                result, reason = self.will_do_sex_act(sex_act, True)

                if result:

                    self.does[sex_act] = True

                return result, reason


        def does_anything(self): ## Tests if the girl has any activated sex act. She will be excluded from whoring if she isn't.

            for act in all_sex_acts:
                if self.does[act]:
                    return True

            return False

        def will_do_anything(self): ## Tests if the girl is open to a sex act. She will be excluded from the whore job if she isn't.

            for act in all_sex_acts:
                if self.will_do_sex_act(act):
                    return True

            return False

        def count_available_sex_acts(self, discovered=True, extended=True): # unused
            if extended:
                acts = extended_sex_acts
            else:
                acts = all_sex_acts

            if discovered:
                return sum(1 for act in acts if (self.will_do_sex_act(act) and self.personality_unlock[act]))
            return sum(1 for act in acts if self.will_do_sex_act(act))

        def get_trainable_sex_acts(self):
            available_acts = []
            _debug = ""

            for act in extended_sex_acts:
                if training_test_dict[act]:
                    for cond, pref in training_test_dict[act]:
                        if compare_preference(self, cond, pref) and self.personality_unlock[act] != 0:
                            _debug += act + ": No cond "
                            available_acts.append(act)
                            break
                        elif not compare_preference(self, cond, pref):
                            _debug += act + ": %s is not %s " % (cond, pref)
                        elif not self.personality_unlock[act]:
                            _debug += act + ": No unlock "
                        else:
                            _debug += act + ": ???"
                else:
                    _debug += act + ": No cond "
                    available_acts.append(act)

            return available_acts

        def count_activated_sex_acts(self):
            return sum(1 for act in all_sex_acts if self.does[act])

        def has_activated_sex_acts(self): # Checks if the girl has any sex acts activated
            for act in all_sex_acts:
                if self.does[act]:
                    return True

            return False

        def refresh_sex_acts(self): # Ensures unavailable sex acts don't stay ticked
            for sex_act in all_sex_acts:
                if self.does[sex_act] and not self.will_do_sex_act(sex_act):
                    self.does[sex_act] = False
                    notify(self.fullname + " 不能再继续" + girl_related_dict[sex_act] + "了。", pic=self.portrait)


        def activate_sex_act(self, sex_act):

            sex_act = sex_act.lower()

            if self.will_do_sex_act(sex_act):
                self.does[sex_act] = True
                return True
            else:
                return False

        def deactivate_sex_act(self, sex_act):

            sex_act = sex_act.lower()

            self.does[sex_act] = False

            if not self.has_activated_sex_acts() and self.job == "whore":
                renpy.say("", self.fullname + " 如果你禁止所有的性行为，她就不能继续做妓女了。")
                self.set_job(None)
            return True


        def get_sex_act_modifier(self, sex_act = "all"):

            modifier = self.get_effect("change", "sex acts requirements")

            return modifier


        def generate_traits(self, p_traits=None, n_trait = None): # Where p_traits is a list of gold or positive trait names, n_trait is a negative trait name

            ## Calculate traits ##

            gold_traits_nb = starting_traits_gold
            pos_traits_nb = starting_traits_gold + starting_traits_positive
            neg_traits_nb = starting_traits_negative

            ## Trait King hooks ##

            #<Trait King: Modify number of traits>
            if game.has_active_mod("traitking"):

                ## Trait King: Randomize number of traits to assign

                d = dice(100)

                if d > traitking_t1_chance:   # very rare 1
                    gold_traits_nb = traitking_t1_gold
                    pos_traits_nb = traitking_t1_positive
                    neg_traits_nb = traitking_t1_regular

                elif d > traitking_t2_chance:            # very rare 2
                    gold_traits_nb = traitking_t2_gold
                    pos_traits_nb = traitking_t2_positive
                    neg_traits_nb = traitking_t2_regular

                elif d > traitking_t3_chance:            # rare 1
                    gold_traits_nb = traitking_t3_gold
                    pos_traits_nb = traitking_t3_positive
                    neg_traits_nb = traitking_t3_regular

                elif d > traitking_t4_chance:            # rare 2
                    gold_traits_nb = traitking_t4_gold
                    pos_traits_nb = traitking_t4_positive
                    neg_traits_nb = traitking_t4_regular

                elif d > traitking_t5_chance:            # uncommon 1
                    gold_traits_nb = traitking_t5_gold
                    pos_traits_nb = traitking_t5_positive
                    neg_traits_nb = traitking_t5_regular

                elif d > traitking_t6_chance:            # uncommon 2
                    gold_traits_nb = traitking_t6_gold
                    pos_traits_nb = traitking_t6_positive
                    neg_traits_nb = traitking_t6_regular

                else:                   # common
                    gold_traits_nb = traitking_t7_gold
                    pos_traits_nb = traitking_t7_positive
                    neg_traits_nb = traitking_t7_regular

            #</Trait King>

            ## Generating gold and positive traits (default = 2) ##

            new_traits = [] # A list of trait names

            # Step 1: Adding mandatory positive traits
            if p_traits: # Used for enemy generals
                new_traits = p_traits

            # Step 2: Adding 'always' positive traits from _BK.ini

            if use_ini_traits and self.init_dict["base positive traits/always"]:
                renpy.random.shuffle(self.init_dict["base positive traits/always"])
                for trait_name in self.init_dict["base positive traits/always"]:
                    if trait_name not in new_traits:
                        new_traits.append(trait_name)

            # Step 3: Adds a gold trait if girl is original
            if self.original:
                gold_traits_nb += 1

            # Step 4: Assigns gold traits
            # Removes gold traits if they have already been assigned

            for trait_name in new_traits: # Checks if a gold trait has already been assigned
                if trait_name in gold_trait_dict.keys():
                    gold_traits_nb -= 1

            while gold_traits_nb > 0 and len(new_traits) < pos_traits_nb:
                gold_list = []

                for trait in gold_traits:
                    if trait.name in new_traits:
                        continue
                    elif trait.name in self.init_dict["base positive traits/never"]:
                        continue
                    elif trait.name in self.init_dict["base positive traits/often"]:
                        gold_list.append((trait.name, 4))
                    elif trait.name in self.init_dict["base positive traits/rarely"]:
                        gold_list.append((trait.name, 1))
                    else:
                        gold_list.append((trait.name, 2))

                new_traits.append(weighted_choice(gold_list))

                gold_traits_nb -= 1

            # Step 5: Then, adds random positive traits until there are maxed
            while len(new_traits) < pos_traits_nb:
                trait_list = []

                for trait in pos_traits:
                    if trait.name in new_traits:
                        continue
                    elif use_ini_traits and trait.name in self.init_dict["base positive traits/never"]:
                        continue
                    for opp in trait.opposite:
                        if opp in new_traits:
                            break
                    else:
                        if use_ini_traits and trait.name in self.init_dict["base positive traits/often"]:
                            trait_list.append((trait.name, 4))
                        elif use_ini_traits and trait.name in self.init_dict["base positive traits/rarely"]:
                            trait_list.append((trait.name, 1))
                        else:
                            trait_list.append((trait.name, 2))

                new_traits.append(weighted_choice(trait_list))

            # Sanity check: Crops the positive traits if there are too many
            if len(new_traits) > pos_traits_nb:
                new_traits = new_traits[:pos_traits_nb]

            ## Generating negative trait(s) ##

            # Step 1: Adding mandatory negative trait
            if n_trait:
                new_traits.append(n_trait)

            # Step 2: Adding 'always' negative traits from _BK.ini
            elif use_ini_traits and self.init_dict["base negative traits/always"]:
                new_traits.append(rand_choice(self.init_dict["base negative traits/always"]))

            # Step 3: Adding random trait otherwise
            while len(new_traits) - pos_traits_nb < neg_traits_nb:
                trait_list = []

                for trait in neg_traits:
                    if trait.name in new_traits:
                        continue
                    elif use_ini_traits and trait.name in self.init_dict["base negative traits/never"]:
                        continue
                    else:
                        for opp in trait.opposite:
                            if opp in new_traits:
                                break
                        else:
                            if use_ini_traits and trait.name in self.init_dict["base negative traits/often"]:
                                trait_list.append((trait.name, 4))
                            elif use_ini_traits and trait.name in self.init_dict["base negative traits/rarely"]:
                                trait_list.append((trait.name, 1))
                            else:
                                trait_list.append((trait.name, 2))

                new_traits.append(weighted_choice(trait_list))

            ## ADDING TRAITS ##

            for trait_name in new_traits:
                self.add_trait(trait_dict[trait_name], forced=True) # 'forced' will cause _BK.ini specified traits to bypass opposite-checking



## Get methods

        def get_name(self):
            return self.fullname

        def get_pic(self, tags, alt_tags1 = None, alt_tags2 = None, alt_tags3 = None, and_tags = None, not_tags = None, strict = False, and_priority=True, naked_filter=False, attempts=0, soft=False, hide_farm=False, pref_filter=False, allow_lesbian=False, always_stock=False):

            # First looks for a pic with 'tags', then 'alt_tags1' if no pic is found, then 'alt_tags2'...
            # The 'and' and 'not_tags' apply to every set of tags.
            # NEW: and_tags and not_tags should be listed from the most important to the least important (they will be dropped in reverse order)
            # If 'strict' is on, a False value is returned if no picture can be found with the and/not_tags conditions
            # If 'and_priority' is on, the 'and' and 'not' clause will only be dropped after the search list has been exhausted
            # allow_lesbian is overridden by bisexual/group or using lesbian tag

#            if debug_mode: renpy.notify("Looking for pic " + and_text(tags))


            tags = make_list(tags)
            if and_tags:
                and_tags = make_list(and_tags)
            else:
                and_tags = []
            if not_tags:
                not_tags = make_list(not_tags)
            else:
                not_tags = []

            ## Priority filters: These tag filters take precedence over provided not_tags, in ascending order of importance

            # 'naked_filter' automatically adds the naked and_tags or not_tags tag (use only with profile, rest, or work pics. Will cause problems with sex events, use sparingly)

            if naked_filter and "naked" not in (tags + and_tags + not_tags): # Direct tag orders take precedence over naked_filter
#                renpy.say("", "Girl - Naked filter ON")
                if self.naked:
                    and_tags.append("naked")
                elif not self.naked:
                    not_tags.insert(0, "naked") # Places "naked" at the begining of the not_tags list

            # 'Soft' automatically excludes sexual tags from the research tags. It does not exclude 'naked' or farm tags, provided they don't come with a sexual tag. Soft not_tags are removed last

            if soft: # Inserts soft filters at the begining of the not_tags list
                not_tags = [ntag for ntag in (all_sex_acts + ["group", "bisexual"]) if ntag not in not_tags] + not_tags

            # Lesbian pics will be excluded unless it is explicitely requested or the context is bisexual/group

            if not allow_lesbian and "lesbian" not in (tags + and_tags + not_tags) and "bisexual" not in (tags + and_tags) and "group" not in (tags + and_tags):
                not_tags.insert(0, "lesbian") # Places "lesbian" at the begining of the not_tags list

            # 'Virgin' girls will never have pictures displaying sex shown unless the act is explicitely 'sex' or 'group'

            if self.has_trait("Virgin"):
                if not "sex" in (tags + and_tags + not_tags) and not "group" in (tags + and_tags):
                    not_tags.insert(0, "sex") # Places "sex" at the begining of the not_tags list

            # 'Hide_farm' excludes hardcore farm acts. It takes precedence over everything else in the not_tags list
            if hide_farm:
                if not persistent.fuzzy_tagging_acts: # Disables machine and big for all non farm picture search
                    not_tags.insert(0, "machine") # Places "machine" at the begining of the not_tags list
                    not_tags.append("big")
                elif "fetish" not in (tags + and_tags):
                    not_tags.insert(0, "machine") # Places "machine" at the begining of the not_tags list
                not_tags = farm_hardcore_acts + not_tags

            ## Non-priority filters (will be added at the end of the not_tags list)

            # 'portrait' may not show unless specifically requested

            if "portrait" not in (tags + and_tags + not_tags):
                not_tags.append("portrait")

            # 'pref_filter' filters out unintended sex acts if she isn't at least indifferent to them (e.g. : 'sex fetish' pic will only show during sex if she is indifferent to fetish)

            if pref_filter:
                not_tags += [a for a in all_sex_acts if (not a in (tags + and_tags + not_tags) and not compare_preference(self, a, "indifferent"))]

            # Additional filters (libido/mood)

            if self.get_stat("libido") < 75 and "libido" not in (tags + and_tags + not_tags): # Libido tags won't happen if girl's libido is too low
                not_tags.append("libido")
            if self.mood > 0 and self.get_love() - self.get_fear() > 0 and "sad" not in not_tags: # Sad tags won't happen if girl is happy and loving
                not_tags.append("sad")
            if self.mood < 0 or self.get_love() - self.get_fear() < 0 and "happy" not in not_tags: # Happy tags won't happen if girl is sad or in fear
                not_tags.append("happy")
            if self.mood >= 15 or self.mood <= -15 or self.get_love() - self.get_fear() >= 15 or self.get_love() - self.get_fear() <= -15: # Neutral tags won't happen if girl is happy or sad or in love or in fear
                if "neutral" not in not_tags:
                    not_tags.append("neutral")

            return get_pic(self, tags=tags, alt_tags1=alt_tags1, alt_tags2=alt_tags2, alt_tags3=alt_tags3, and_tags=and_tags, not_tags=not_tags, strict=strict, and_priority=and_priority, attempts=attempts, always_stock=always_stock)


        def get_pic_not_tags(self, tags, alt_tags1 = None, alt_tags2 = None, alt_tags3 = None, and_tags = None, not_tags = None, strict = False, and_priority=True, naked_filter=False, attempts=0, soft=False, hide_farm=False, pref_filter=False, allow_lesbian=False, always_stock=False):

            # First looks for a pic with 'tags', then 'alt_tags1' if no pic is found, then 'alt_tags2'...
            # The 'and' and 'not_tags' apply to every set of tags.
            # NEW: and_tags and not_tags should be listed from the most important to the least important (they will be dropped in reverse order)
            # If 'strict' is on, a False value is returned if no picture can be found with the and/not_tags conditions
            # If 'and_priority' is on, the 'and' and 'not' clause will only be dropped after the search list has been exhausted
            # allow_lesbian is overridden by bisexual/group or using lesbian tag

        #            if debug_mode: renpy.notify("Looking for pic " + and_text(tags))


            tags = make_list(tags)
            if and_tags:
                and_tags = make_list(and_tags)
            else:
                and_tags = []
            if not_tags:
                not_tags = make_list(not_tags)
            else:
                not_tags = []

            ## Priority filters: These tag filters take precedence over provided not_tags, in ascending order of importance

            # 'naked_filter' automatically adds the naked and_tags or not_tags tag (use only with profile, rest, or work pics. Will cause problems with sex events, use sparingly)

            if naked_filter and "naked" not in (tags + and_tags + not_tags): # Direct tag orders take precedence over naked_filter
        #                renpy.say("", "Girl - Naked filter ON")
                if self.naked:
                    and_tags.append("naked")
                elif not self.naked:
                    not_tags.insert(0, "naked") # Places "naked" at the begining of the not_tags list

            # 'Soft' automatically excludes sexual tags from the research tags. It does not exclude 'naked' or farm tags, provided they don't come with a sexual tag. Soft not_tags are removed last

            if soft: # Inserts soft filters at the begining of the not_tags list
                not_tags = [ntag for ntag in (all_sex_acts + ["group", "bisexual"]) if ntag not in not_tags] + not_tags

            # Lesbian pics will be excluded unless it is explicitely requested or the context is bisexual/group

            if not allow_lesbian and "lesbian" not in (tags + and_tags + not_tags) and "bisexual" not in (tags + and_tags) and "group" not in (tags + and_tags):
                not_tags.insert(0, "lesbian") # Places "lesbian" at the begining of the not_tags list

            # 'Virgin' girls will never have pictures displaying sex shown unless the act is explicitely 'sex' or 'group'

            if self.has_trait("Virgin"):
                if not "sex" in (tags + and_tags + not_tags) and not "group" in (tags + and_tags):
                    not_tags.insert(0, "sex") # Places "sex" at the begining of the not_tags list

            # 'Hide_farm' excludes hardcore farm acts. It takes precedence over everything else in the not_tags list
            if hide_farm:
                if not persistent.fuzzy_tagging_acts: # Disables machine and big for all non farm picture search
                    not_tags.insert(0, "machine") # Places "machine" at the begining of the not_tags list
                    not_tags.append("big")
                elif "fetish" not in (tags + and_tags):
                    not_tags.insert(0, "machine") # Places "machine" at the begining of the not_tags list
                not_tags = farm_hardcore_acts + not_tags

            ## Non-priority filters (will be added at the end of the not_tags list)

            # 'portrait' may not show unless specifically requested

            if "portrait" not in (tags + and_tags + not_tags):
                not_tags.append("portrait")

            # 'pref_filter' filters out unintended sex acts if she isn't at least indifferent to them (e.g. : 'sex fetish' pic will only show during sex if she is indifferent to fetish)

            if pref_filter:
                not_tags += [a for a in all_sex_acts if (not a in (tags + and_tags + not_tags) and not compare_preference(self, a, "indifferent"))]

            # Additional filters (libido/mood)

            if self.get_stat("libido") < 75 and "libido" not in (tags + and_tags + not_tags): # Libido tags won't happen if girl's libido is too low
                not_tags.append("libido")
            if self.mood > 0 and self.get_love() - self.get_fear() > 0 and "sad" not in not_tags: # Sad tags won't happen if girl is happy and loving
                not_tags.append("sad")
            if self.mood < 0 or self.get_love() - self.get_fear() < 0 and "happy" not in not_tags: # Happy tags won't happen if girl is sad or in fear
                not_tags.append("happy")
            if self.mood >= 15 or self.mood <= -15 or self.get_love() - self.get_fear() >= 15 or self.get_love() - self.get_fear() <= -15: # Neutral tags won't happen if girl is happy or sad or in love or in fear
                if "neutral" not in not_tags:
                    not_tags.append("neutral")

            return and_text(not_tags)

        def get_pic_by_name(self, filename): # Where filename must NOT include the path to any subfolder. Doesn't include ignored folders for now.
            return GirlFilesDict.get_pic_by_name(self.path, filename)

        def get_fix_pic(self, act=None, fix=None, and_tags=None, not_tags=None, hide_farm=True, naked_filter=False, pref_filter=True, attempts=0, allow_lesbian=False, always_stock=False, strict=False):
            # Where act is a string but fix is an object (important). hide_farm is on by default. allow_lesbian is overridden by bisexual/group or using lesbian tag
            # Strict works differently for this method

            if is_string(fix): # Failsafe
                fix = fix_dict[fix]

            ## 0. Sanity check

            if not fix:
                raise AssertionError("No fixation provided for picture.")

            debug_output = False
            if debug_output: BkLog.info("\nLooking for " + self.path + "picture - act: " + str(act) + " fix:" + fix.name)

            ## 1. Preparing and and not tags

            if and_tags:
                and_tags = make_list(and_tags)
            else:
                and_tags = []
            if not_tags:
                not_tags = make_list(not_tags)
            else:
                not_tags = []

            if hide_farm:
                not_tags += farm_hardcore_acts
                if not persistent.fuzzy_tagging_acts: # Disables machine and big for all non farm picture search
                    not_tags.append("big")
                    not_tags.append("machine")
                elif act != "fetish":
                    not_tags.append("machine")

            if act not in ("bisexual", "group"):
                not_tags += ["bisexual", "group"]
            elif act == "bisexual":
                not_tags.append("group")

            if act == "naked":
                not_tags += all_sex_acts

            # Lesbian pics will be excluded unless it is explicitely requested or the context is bisexual/group, or forced on with 'allow_lesbian'

            if not allow_lesbian and act not in ("bisexual", "group") and "lesbian" not in (and_tags + not_tags):
                not_tags.append("lesbian")

            not_tags.extend(ntag for ntag in fix.not_list if ntag not in not_tags)

            ## 2. Picking a fixation picture according to Preferences (as suggested by Chris12)

            # The game may randomly pick either a fixation picture fit for the sex act or a stand-alone fixation picture that doesn't conflict with the sex act.
            # e.g. when looking for 'doggy anal': 'doggy anal.jpg' works. 'doggy anal sex.jpg' works. 'doggy.jpg' works. 'doggy sex.jpg' does NOT work.

            and_not_settings = []

            if act:
                # PIC 1 - Looks for a fixation picture AND featuring the requested sex act
                and_not_settings.append(["act-based", list(and_tags) + [act], list(not_tags)])

                # PIC 2 - Looks for a fixation picture NOT featuring incompatible sex acts (except for the 'public' fixation)
                if fix.name != "public acts":
                    and_not_settings.append(["generic", list(and_tags), list(not_tags) + opposite_sex_acts[act]])

            else:
                and_not_settings.append(["generic", list(and_tags), list(not_tags)])

            pics = [] # Primary pool: uses tuples (pic, weight).
            pics_second = [] # Second rate pictures, if not all conditions can be satisfied.

            for _context, _and_tags, _not_tags in and_not_settings:
                for tags in fix.tag_list:
                    _tags = make_list(tags)
                    if debug_output: BkLog.info("Looking for " + " ".join(tagslist) + " +" + " +".join(and_tags1) + " -" + " -".join(not_tags1))
                    pic = self.get_pic(_tags, and_tags=_and_tags, not_tags=_not_tags, strict=True, naked_filter=naked_filter, pref_filter=pref_filter, always_stock=always_stock)
                    if pic:
                        if debug_output: BkLog.info("    Found: " + pic.filename + " (" + _context + ")")
                        # Pic weight is affected by the fix_pic_balance setting
                        pics.append((pic, pic.get_weight(_context)))
                        break
                else: # Drops the 'strict' argument if no picture is found
                    if debug_output: BkLog.info("Not Found " + fix.name + "! (" + _context + ")")

                    for tags in fix.tag_list:
                        attempts += 1
                        pic = self.get_pic(tags, and_tags=_and_tags, not_tags=_not_tags, attempts=attempts, naked_filter=naked_filter, pref_filter=pref_filter, always_stock=always_stock)
                        if pic:
                            if debug_output: BkLog.info("Found non strict:" + pic.filename)
                            pics_second.append((pic, pic.get_weight()))

            attempts = game.last_pic["attempts"] # This is necessary to properly count all attempts

            if pics:
                return weighted_choice(pics)
            elif strict: # Aborpts
                return None
            elif pics_second:
                return weighted_choice(pics_second)
            elif act: # Gets an act picture if no fixation picture is found, then a naked picture, then a profile pic if all else fails
#                renpy.say("", "Fix - Looking for " + act)
                if act in extended_sex_acts and fix.name != "cosplay":
                    pic = self.get_pic(act, "naked", "profile", and_tags=and_tags, not_tags=not_tags, attempts=attempts, naked_filter=False, pref_filter=pref_filter, always_stock=always_stock)
                else:
                    pic = self.get_pic(act, "profile", and_tags=and_tags, not_tags=not_tags, attempts=attempts, naked_filter=naked_filter, pref_filter=pref_filter, always_stock=always_stock)

                if pic:
                    if debug_output: BkLog.info("No fixation picture found: Reverted to %s or naked picture (%s)" % (act, pic.filename))
                    return pic

            if debug_output: BkLog.info("No picture found: Reverted to profile picture (%s)" % pic.filename)
            return self.get_pic("profile", and_tags=and_tags, not_tags=not_tags, attempts=attempts, naked_filter=naked_filter) # Probably unnecessary


        def test_fix(self, name, unlock=False, feedback=False):

            r = self.check_fix(name)

            if r == "pos":
                if unlock:
                    if not self.personality_unlock[name]:
                        self.personality_unlock[name] = True
                        if feedback:
                            renpy.play(s_aaah, "sound")
                            renpy.say("", "你发现 " + self.name + "对 " + girl_related_dict[name] + "有些迷恋。")
                return "pos"
            elif r == "neg":
                if unlock:
                    if not self.personality_unlock[name]:
                        self.personality_unlock[name] = True
                        if feedback:
                            renpy.play(s_surprise, "sound")
                            renpy.say("", "你发现 " + self.name + "对 " + girl_related_dict[name] + "有些厌恶。")
                return "neg"
            else:
                return False

        def check_fix(self, fix_name):
            if fix_name in [fix.name for fix in self.pos_fixations]:
                return "pos"
            elif fix_name in [fix.name for fix in self.neg_fixations]:
                return "neg"
            else:
                return False

        def get_sex_attitude(self, act=None, fix=None): # Measures how much a girl enjoys a particular sex act or fixation

            # Where fix is a String, not an Object

            score = self.get_stat("libido")

            if act:
                score += self.preferences[act]
                if act in all_sex_acts:
                    score += self.get_stat(act)

            else: # When there's no sex act, such as kissing or groping
                score += self.get_stat("obedience") - 75

            if fix:

                fix = make_list(fix)

                for fix_name in fix:
                    if fix_name in [fix.name for fix in self.pos_fixations]:
                        score += self.get_stat("sensitivity") // 2
                    elif fix_name in [fix.name for fix in self.neg_fixations]:
                        if self.is_("dom"):
                            score -= self.get_stat("sensitivity")
                        elif self.is_("very sub"):
                            score += self.get_stat("sensitivity") // 2
                        elif self.is_("sub"):
                            score += self.get_stat("sensitivity") // 4
            return score


        def get_price(self, operation, raw=False):

            modifier = MC.get_modifier(operation, raw)

            #<Trait King: Modify girl price>
            if game.has_active_mod("traitking"):

                traitking_modifier = 1.0

                if not hasattr(self, 'valuation'):

                    self.valuation = 100

                traitking_valuation = self.valuation + self.get_effect("change", "valuation")

                traitking_modifier *= max(10, traitking_valuation) / 100.0

                modifier *= traitking_modifier

            #</Trait King>

            # Originals are 15% more expensive

            if self.original:
                modifier *= 1.15

            statsum = sum(s.value for s in self.stats + self.sex_stats)

            baseprice = rank_cost[self.rank] + statsum * (2 * self.rank) #? Changed, see how it goes

            # Vanilla: Price increases by 1% for every x points of preference raised (50 by default)

            # pref_boost = 1 + sum((self.preferences[act]-base_reluctance[act])/2500.0 for act in self.preferences.keys()) # Old formula
            pref_boost = 1 + sum((sell_girl_preference_boost*(self.preferences[act]-base_reluctance[act])) for act in self.preferences.keys())

            finalprice = round_int(baseprice * pref_boost * modifier)

            return finalprice


        def get_med_upkeep(self):

            eff = self.get_effect("boost", "upkeep")

            av_stat = (sum(s.value for s in self.stats) + sum(s.value for s in self.sex_stats)) // (len(self.stats) + len(self.sex_stats))

            return round_int(av_stat * eff * (2 ** (self.rank-1))) # Testing upkeep formula suggested by Chris12 (exponential upkeep growth) #! Change from 1.5 to 2


        def adjust_upkeep(self):

            if self.upkeep > 0: # 0 upkeep happens when she is punished.
                self.upkeep = round_int(self.get_med_upkeep() + self.upkeep_ratio*self.rank)

            return

        def update_upkeep_ratio(self):
            self.upkeep_ratio = (self.upkeep - self.get_med_upkeep())/float(self.rank)

        def get_upkeep_modifier(self):

            m = self.get_med_upkeep()

            if self.upkeep >= (m + 10 * self.rank * 2 ** self.rank):
                modifier = +5

            elif self.upkeep >= (m + 8 * self.rank * 2 ** self.rank):
                modifier = +4

            elif self.upkeep >= (m + 6 * self.rank * 2 ** self.rank):
                modifier = +3

            elif self.upkeep >= (m + 4 * self.rank * 2 ** self.rank):
                modifier = +2

            elif self.upkeep >= (m + 2 * self.rank * 2 ** self.rank):
                modifier = +1

            # Higher mood penalties for negative upkeep

            elif self.upkeep <= (m - 15 * self.rank * 2 ** self.rank):
                modifier = -20

            elif self.upkeep <= (m - 10 * self.rank * 2 ** self.rank):
                modifier = -10

            elif self.upkeep <= (m - 8 * self.rank * 2 ** self.rank):
                modifier = -8

            elif self.upkeep <= (m - 6 * self.rank * 2 ** self.rank):
                modifier = -4

            elif self.upkeep <= (m - 4 * self.rank * 2 ** self.rank):
                modifier = -2

            elif self.upkeep <= (m - 2 * self.rank * 2 ** self.rank):
                modifier = -1

            else:
                modifier = 0

            if modifier > 0:
                modifier += self.get_effect("change", "positive upkeep mood modifier")
            elif modifier < 0:
                modifier += self.get_effect("change", "negative upkeep mood modifier")

            return modifier




## Items

        def equip(self, item):

            for it in self.equipped:
                if it.slot == item.slot:
                    self.unequip(it)

            self.equipped.append(item)

            boost = self.get_effect("boost", item.type.name.lower())

            if boost != 1.0:
                for eff in item.effects:
                    eff.value *= boost

            self.add_effects(item.effects)
            item.equipped = True

            self.refresh_sex_acts() # Checks if sex_acts can still be done

            test_achievements(["hands", "body", "finger", "neck", "accessory"])

        def unequip(self, item):

            self.equipped.remove(item)

            boost = self.get_effect("boost", item.type.name.lower())

            if boost != 1.0:
                for eff in item.effects:
                    eff.value /= boost

            self.remove_effects(item.effects)
            item.equipped = False


        def get_equipped(self, slot):

            for it in self.equipped:
                if it.slot == slot:
                    return it
            return False

        def use_item(self, item, night=False):
            changes = NightChangeLog(title=item.name)

            debug_notify("Using " + item.name + " on " + self.fullname, pic=self.portrait)

            used = False
            r = ""

            for e in item.effects:
                if e.type == "gain":
                    c = self.add_effects(e)
                    if c:
                        changes.add(e.target.capitalize() + ": %s" % plus_text(c))
                    used = True

                elif e.type == "change": # In case of direct usage, the change will last only for one turn or the item duration
                    if item.type.name == "Food": # Prevents stacking food effects for the same stat
                        if self.current_food_effect[e.target]:
                            changes.add("%s: %s (expired)" % (self.current_food_effect[e.target].target.capitalize(), plus_text(-self.current_food_effect[e.target].value)))
                            self.remove_effects(self.current_food_effect[e.target])

                        self.current_food_effect[e.target] = e # Stores the object used to remove the effect in case another food is absorbed

                    if e.duration > 0:
                        c = self.add_effects(e, expires = calendar.time + e.duration)
                        if c:
                            changes.add("%s: %s (duration: %s days)" % (e.target.capitalize(), plus_text(c), e.duration))
                    else:
                        c = self.add_effects(e, expires = calendar.time + 1)
                        if c:
                            changes.add("%s: %s" % (e.target.capitalize(), plus_text(c)))

                    used = True

                elif e.type in ("special", "instant"):
                    if e.target == "level":
                        if self.level < e.value:
                            self.xp = self.get_xp_cap()
                            self.level_up()
                            changes.add("Level: +1", col=c_orange)
                            used = True
                        else:
                            notify("这个道具只能使用到 " + str(e.value), pic=self.portrait)

                    elif e.target == "heal":
                        if not self.can_heal_from_item() and not night:
                            renpy.say("", "每天只能使用一次治疗物品。")

                        elif self.hurt > 0:
                            c, _ = self.heal(e.value, from_item=True)
                            if c:
                                changes.add("Healing", "header")
                                changes.add("Healed: %s" % plus_text(c))
                                if self.hurt <= 0:
                                    changes.add("(fully healed)", col="good")
                                    if not night:
                                        renpy.say("", self.name + " 已经完全康复。")
                                elif not night:
                                    renpy.say("", self.name + " 得到了治疗但还需要几天恢复。")
                                used = True
                        else:
                            notify(self.name + " 恢复健康了。", pic=self.portrait)

            if used:
                r = item.use_me()

                if r == "used_up" and item in self.items:
                    self.items.remove(item)
                    changes.add("(used up)", col="bad")

                renpy.block_rollback()

            if night:
                return r, changes
            return r

        def take(self, giver, obj):
            self.items.append(obj)
            if obj.equipped:
                giver.unequip(obj)
            try:
                giver.items.remove(obj)
            except:
                pass

        def get_MC_relation(self):
            if self in MC.girls + farm.girls:
                return "slave"

            elif girl in game.free_girls:
                if self.MC_relationship_level == 0:
                        return "stranger"

                elif self.MC_relationship_level == 1:
                        return "friend"

                elif self.MC_relationship_level == 2:
                        return "love interest"

                elif self.MC_relationship_level == 3:
                        return "girlfriend"

                elif self.MC_relationship_level == 4:
                        return "lover"

                elif self.MC_relationship_level == 5:
                        return "lover"

            return "unknown"

        def receive_gift(self, item):

            flower = False

            score = 1
            mod = 1.0

            for e in item.effects:
                if e.type == "gift":
                    score += self.personality.gift_likes[e.target]
                    mod = e.value

                elif e.type == "flower":
                    flower = True
                    break

            if flower:
                if e.target == self.likes["color"]:
                    score += 4
                    self.personality_unlock["fav_color"] = True
                    renpy.say(self.char, "哦，你还记得我喜欢什么颜色! 你真浪漫...")

                elif e.target == self.dislikes["color"]:
                    score += 0
                    self.personality_unlock["dis_color"] = True
                    renpy.say(self.char, "Emmm，谢谢你, 但我不喜欢这个颜色, 总之还是感谢你的花。")

                else:
                    score += 2
                    renpy.say(self.char, "花! 给我的吗! 真是个惊喜...")

                if self.MC_relationship_level == 2:
                    renpy.say(self.char, "你好浪漫... 你想要我怎么奖励你?")

                    r = menu(items = (("实际上...", None), ("约她开房", True), ("别在意", False)))

                    if r:
                        renpy.block_rollback()
                        self.MC_relationship_level = 3
                        self.track_event("MC girlfriend", arg=self.name)
                        test_achievement("girlfriends")
                        self.say("free_ask_out")
#                         renpy.say(you, self.name + ", I like you. Let's be together.")
#                         renpy.say(self.char, "You want me... to be your girlfriend?")
#                         renpy.say(you, "That's right.")
#                         renpy.say(self.char, "Why, finally you ask! Of course!")
#                         renpy.say("", "She throws herself into your arms and gives you a long, deep kiss.")
#                         renpy.say(self.char, "I have to go for now... See you around, handsome! *wink*")


                    else:
                        renpy.block_rollback()
                        renpy.say(you, "嗯，不，不完全是。")
                        renpy.say(self.char, "哦... 我知道了。")
            else:
                if score >= 4:
                    renpy.say(self.char, "这是？!!!你怎么知道我喜欢这个!")

                elif score >= 2:
                    renpy.say(self.char, "真不错! 谢谢你还没把我忘了。")

                elif score >= 0:
                    renpy.say(self.char, "emmm, 谢了. 看起来挺有趣的... 虽然我不知道它是什么。")

                else:
                    renpy.say(self.char, "这是? 呕, 带着你的东西滚开，离我远点!")

            if score >= 0:
                score *= mod

            self.change_love(score)
            self.change_mood(score)

            return score


        def test_say(self):
            renpy.say(self.char, "让我们测试一下这些方法是否会中断流动。")
            self.change_love(200)
            renpy.say(self.char, "我的好感度提高了吗? 现在的关系： %s" % self.love)
            self.say("free_ask_out")
            self.change_love(-200)
            renpy.say(self.char, "我的好感度下降了吗? 现在的关系： %s" % self.love)
            return


## Jobs

        def will_do(self, job, silent=False):

            if job == "whore":

                modifier = self.get_sex_act_modifier()

                if self.get_stat("obedience") + self.get_stat("libido") >= (whore_test / cheat_modifier["stats"]) + modifier:
                    if self.will_do_anything():
                        return True
                    elif not silent:
                        notify("性技能水平太低了", pic=self.portrait)
                elif not silent:
                    notify("性欲/服从太低了", pic=self.portrait)
                return False

            else:
                return True

        def set_job(self, job, forced=False):

            if self.will_do(job):

                self.old_job = self.job # Obsolete

                self.job = job

                if job == "whore" or (job in all_jobs and self.work_whore):
                    if not self.has_activated_sex_acts():
                        for stat in gstats_sex:
                            self.activate_sex_act(stat)

                self.job_sort_value = job_sort_value[job]

                if not job or job == "rest":
                    self.resting = True
                    self.work_whore = False
                    if forced:
                        self.away = False # For the 'force rest' cheat
                else:
                    self.resting = False

                return True

            else:
                return False

        def set_rest(self):

            if self.resting:
                return False

            self.resting = True

            self.job_sort_value = job_sort_value[job]

            return True


        def works_today(self, check_autorest=False):

            day = calendar.get_weekday()

            if self.job and not (self.resting or self.away or self.farm or self.exhausted or self.hurt > 0):
                if self.workdays[day] > 0:
                    if not check_autorest or self.energy >= autorest_limit:
                        return self.workdays[day]

            return False

        def get_schedule(self): # Returns a list of values for the seven days of the week
            return [self.workdays[d] for d in weekdays]

        def load_schedule(self, schedule):
            i = 0
            for day in weekdays:
                self.workdays[day] = schedule[i]
                i += 1

        def get_status(self): # Returns a list of tuples (picture name, tooltip)
            status_list = []

            # #! Temp fix for older patches
            # try:
            #     _ = persistent.show_girl_status["scheduled"]
            # except:
            #     persistent.show_girl_status = {"away": True, "farm": True, "rest": True, "scheduled": False, "half-shift": True, "master bedroom": True, "work&whore": True, "not work&whore": False, "naked": True, "not naked": False, "negative fixation": True}
            # #!


            if self.away and persistent.show_girl_status["away"]:
                status_list.append(["away.webp", self.fullname + " 要{b}出门{/b}花 %s 天来完成委托或参加培训"  % (self.return_date - calendar.time)])

            elif self in farm.girls and persistent.show_girl_status["farm"]:
                try:
                    if farm.programs[self].target == "no training":
                        if farm.programs[self].holding == "rest":
                            status_list.append(["rest.webp", self.fullname + " 今天在她的牢房里{b}休息{/b}。"])
                        else:
                            status_list.append(["farm.webp", self.fullname + " 在{b}农场{/b} (接受" + farm_related_dict[farm.programs[self].holding] + "训练)。"])
                    else:
                        status_list.append(["farm.webp", self.fullname + " 在{b}农场{/b} (接受" + farm_related_dict[farm.programs[self].target] + "训练)。"])
                except:
                    farm.programs[self] = FarmProgram(self)

            elif (self.resting or not self.job or not self.works_today()) and not self.exhausted:
                if self.workdays[calendar.get_weekday()] > 0 and persistent.show_girl_status["scheduled"]:
                    status_list.append(["scheduled.webp", self.fullname + " 排班表安排她今天{b}休息{/b}。"])
                elif persistent.show_girl_status["rest"]:
                    status_list.append(["rest.webp", self.fullname + " 今天{b}休息{/b}。"])

            elif self.energy < autorest_limit:
                status_list.append(["autorest.webp", self.fullname + " 体力透支了. 她将自动被安排去{b}休息{/b}。"])

            elif self.works_today() == 50 and persistent.show_girl_status["half-shift"]:
                status_list.append(["half.webp", self.fullname + " 今天只上{b}半个夜班{/b} "])

            if self in brothel.master_bedroom.girls and persistent.show_girl_status["master bedroom"]:
                status_list.append(["master.webp", self.fullname + " 今晚要来你的卧室接受{b}私人指导{/b}。"])

            if self.ready_to_rank():
                status_list.append(["rankup.webp", self.fullname + " 可以晋升{b}阶级{/b}。"])

            if self.perk_points or self.can_spend_upgrade_points():
                status_list.append(["levelup.webp", self.fullname + " 可以提升{b}等级{/b}。"])

            if self.hurt > 0:
                if self.hurt <= 1:
                    status_list.append(["hurt.webp", self.fullname + " 因为{b}生病或受伤{/b}她需要再休息一天才能回到最佳状态，否则她什么也做不了。"])
                else:
                    status_list.append(["hurt.webp", self.fullname + " 因为{b}生病或受伤{/b}她需要再休息 " + str(round_int(self.hurt)) + " 天才能回到最佳状态，否则她什么也做不了。"])

            elif self.exhausted:
                status_list.append(["tired.webp", self.fullname + " 感觉{b}体力透支{/b}需要彻底的休息才能回来工作。"]) # Replaced exhausted.webp

            if self.work_whore and persistent.show_girl_status["work&whore"]:
                status_list.append(["ww.webp", self.fullname + " 今天{b}一边服务一边勾引客人{/b}。"])

            if not self.work_whore and persistent.show_girl_status["not work&whore"]:
                status_list.append(["not_ww.webp", self.fullname + " 无法{b}一边服务一边勾引客人{/b}。"])

            if self.naked and persistent.show_girl_status["naked"]:
                if self.get_effect("special", "naked"):
                    status_list.append(["naked.webp", self.fullname + " 将{b}一丝不挂{/b}的展示给所有人看。"])
                else:
                    status_list.append(["naked2.webp", self.fullname + " 今天一整天都将保持{b}全裸{/b}。"])

            if not self.naked and persistent.show_girl_status["not naked"]:
                status_list.append(["not_naked.webp", self.fullname + " 不处于{b}裸体{/b} (这对你来说显然是个难题)。"])

            if [fix.name for fix in self.neg_fixations if self.personality_unlock[fix.name]] and persistent.show_girl_status["negative fixation"]:
                status_list.append(["negfix.webp", "你发现 " + self.fullname + " 有一个{b}负面的癖好{/b}。"])

            return status_list


        def get_status_summary(self):
            r = ""

            if self.ready_to_rank():
                r += "准备好 {b}晋升{/b}"
            if self.perk_points or self.can_spend_upgrade_points():
                if r:
                    r += ", "
                r += "准备好 {b}升级{/b}"

            if self.hurt > 0:
                if r:
                    r += ", "
                r += "{b}受伤{/b}  %s 天" % round_up(self.hurt)

            elif self.exhausted:
                if r:
                    r += ", "
                r += "{b}筋疲力尽{/b}"

            if self.away:
                if r:
                    r += ", "
                r += "{b}外出{/b} 完成委托或培训 %s 天" % (self.return_date - calendar.time)
            elif self in farm.girls:
                if r:
                    r += ", "
                r += "在{b}农场训练{/b}"
            elif self.resting or not self.job or not self.works_today():
                if r:
                    r += ", "
                r += "{b}休息中{/b}t"
            elif self.works_today() == 50:
                if r:
                    r += ", "
                r += "上 {b}半个夜班{/b}"

            if self.work_whore:
                if r:
                    r += ", "
                r += "{b}工作和卖淫{/b}"

            if self.naked:
                if r:
                    r += ", "
                r += "{b}裸体{/b}"

            if [fix.name for fix in self.neg_fixations if self.personality_unlock[fix.name]]:
                if r:
                    r += ", "
                r += "有一个{b}负面习惯{/b}"

            return "当前状态: " + r + "。"


        def get_max_cust_served(self, job="current"):

            if job == "current":
                job = self.job

            # Unavailable (returns 0 if she can't have any more interactions)
            if not job or job == "rest" or self.away or self.hurt > 0:
#                renpy.say(self.char, "My capacity is zero (" + self.fullname + ")")
                return 0

            if job == "whore":
                cust_cap = self.get_max_interactions()

            else:
                stats = perform_job_dict[job + "_stats"]

                main_stat, weight = stats[0]

                cust_cap = job_base_customer + ((self.get_stat(main_stat) + self.get_stat("constitution")) / float(job_customer_points)) + self.get_effect("change", "job customer capacity")

                #<Chris Job Mod: >
                if game.has_active_mod("chrisjobmod"):
                    cust_cap *= act_max_customers_modifier[job]
                    if cust_cap < job_base_customer:
                        cust_cap = job_base_customer
                #</Chris Job Mod>

            # Reduce capacity if the girl is working half shift

            cust_cap = round_int(cust_cap * self.workdays[calendar.get_weekday()] / 100.0)

            # Halves capacity if girl is working and whoring

            if self.work_whore:
                cust_cap = round_int(cust_cap / 2)

            if cust_cap < 1:
                cust_cap = 1

#            renpy.say(self.char, "My capacity is " + str(cust_cap) + " for " + job + " (" + self.fullname + "")

            return cust_cap

        def get_max_interactions(self):
            inter = whore_base_customer + round_int((self.get_stat("libido") + self.get_stat("constitution")) / float(whore_customer_points) + self.get_effect("change", "whore customer capacity"))

            # At least 1 interaction is guaranteed
            return max(inter, 1)

        def get_interaction_modifer(self): # Spent interactions are multiplied by this number (higher modifier=less interactions)

            mod = 100 // self.workdays[calendar.get_weekday()]

            if self.work_whore and self.job in all_jobs:
                mod = mod * 2

            return mod

        def reset_interactions(self):

            self.old_interactions = self.interactions # Used for triggering the libido event

            self.interactions = self.get_max_interactions()

            self.MC_interact_counters = defaultdict(int)

            # Updates memories of rewards and punishments

            self.forgets()

            # Resets naked status to False, except if girl has the naturist perk

            if not self.get_effect("special", "naked"):
                self.naked = False

            # Resets farm promise

            self.farm_lock = False


        def estimate_performance(self, sex_act):

            if self.will_do_sex_act(sex_act):

                stats = perform_job_dict[sex_act + "_stats"]
                score = 0
                totalw = 0

                for tup in stats:

                    stat, weight = tup

                    score += self.get_stat(stat) * weight
                    totalw += weight

                score /= float(totalw)

                return score

            else:
                return -1


        def get_xp(self, act, result, customers): # Boosting effects are applied elsewhere (change_xp)

            cust_diff = round_int(sum(c.diff for c in customers))

            if act in all_jobs:
                xp = xp_bonus_dict[result] * cust_diff ** 1.1 / 2

            elif act in all_sex_acts:
                xp = (xp_bonus_dict[result] * cust_diff) ** 1.1 / len(customers) # Gives a small advantage to group over normal

            xp_ttip = "Base XP vs Difficulty: %s" % event_color["xp"] % (str_int(xp) + " XP")

            # Result boost effect
            boost = self.get_effect("boost", result + " result xp")
            if boost != 1.0:
                xp = xp * boost
                
                xp_ttip += "\nPerks & special effects: x%s" % percent_text(boost, False)

            #<Chris Job Mod>
            if game.has_active_mod("chrisjobmod"):
                xp /= act_max_customers_modifier[self.job]
                xp_ttip += "\nJob Mod modifier: x%s" % percent_text(1.0/act_max_customers_modifier[self.job], False)
            #</Chris Job Mod>

            xp = max(xp * cheat_modifier["xp"] * game.get_diff_setting("xp"), 1) # 1 XP is always guaranteed
            xp_ttip += "\n\nDifficulty modifier: x%s" % percent_text(cheat_modifier["xp"] * game.get_diff_setting("xp"), False)

            return xp, xp_ttip


        def get_jp(self, act, result, customers, silent=False): # Boosting effects are applied elsewhere (change_jp)

            cust_rank = round_int(sum(c.rank for c in customers) / len(customers))

            if act in all_jobs: # Changed from dice(6, 2)
                jp = dice(3, len(customers)) # Gives 1-3 JP per customer
            else:
                jp = dice(3, 1+len(customers)) # Gives 2-6 JP + 1-3 per extra customer

            jp_ttip = "Base JP vs customers: %s" % event_color["jp"] % (str_int(jp) + " JP")

            jp += jp_job_level_modifier[self.job_level[act]] + jp_customer_rank_modifier[cust_rank] + jp_result_modifier[result]

            jp_ttip += "\nGirl rank vs Customer rank: %s\n" % plus_text(jp_job_level_modifier[self.job_level[act]] + jp_customer_rank_modifier[cust_rank], color_scheme="jp")
            jp_ttip += result.capitalize() + " result: %s" % plus_text(jp_result_modifier[result], color_scheme="jp")

            # Result boost effect
            boost = self.get_effect("boost", result + " result jp")
            if boost != 1.0:
                jp = jp * boost
                jp_ttip += "\nPerks & special effects: x%s" % percent_text(boost, False)

            #<Chris Job Mod>
            if game.has_active_mod("chrisjobmod"):
                jp /= act_max_customers_modifier[self.job]
                jp_ttip += "\nJob Mod modifier: x%s" % percent_text(1.0/act_max_customers_modifier[self.job], False)
            #</Chris Job Mod>

            jp_ttip += "\n\nDifficulty modifier: x%s" % percent_text(cheat_modifier["jp"] * game.get_diff_setting("jp"), False)

            jp *= cheat_modifier["jp"] * game.get_diff_setting("jp")

            return jp, jp_ttip

        def get_rep(self, score, customers, first_customer=False): # Boosting effects are applied elsewhere (change_rep)

            cust_rank = round_int(sum(c.rank for c in customers)/float(len(customers)))

            # Reputation gains now depend on relative rank between girl and customer

            if cust_rank + 1 < self.rank: # No reputation changes for customers two ranks lower or more
                rep_ttip = "信誉没有变化：客户等级太低。"
                return 0, rep_ttip

            elif cust_rank < self.rank: # Girls serving lower rank customers gain reputation less easily
                relative_rank = "lower"
                pos_rep = 0.25
                neg_rep = -0.75 # Made rep loss easier on the player for now

            elif cust_rank == self.rank: # Balanced gains if serving same-rank customers
                relative_rank = "same"
                pos_rep = 1
                neg_rep = -0.5 # Made rep loss easier on the player for now

            elif cust_rank > self.rank: # Girls serving higher rank customers gain reputation more easily
                relative_rank = "higher"
                pos_rep = 1
                neg_rep = -0.25

            # Comparing result and threshold for improving/lowering reputation

            if score >= (reversed_result_dict[rep_gains_dict[self.rank][relative_rank]] + self.get_effect("special", "score_to_rep")):
                pos_rep *= dice(len(customers))
                rep_ttip = "声誉提升：+%s" % str_dec(pos_rep, 1)
                # First customer effect
                if first_customer:
                    first_rep_boost = self.get_effect("boost", "first customer rep")
                    if first_rep_boost != 1.0:
                        pos_rep *= first_rep_boost
                        rep_ttip += "\n第一位顾客：x%s" % percent_text(self.get_effect("boost", "first customer rep"), False)
                return pos_rep, rep_ttip

            elif score < (reversed_result_dict[rep_loss_dict[self.rank][relative_rank]] - self.get_effect("special", "score_to_rep")):
                neg_rep *= dice(len(customers))
                rep_ttip = "声誉下降：%s" % str_dec(neg_rep)
                return neg_rep, rep_ttip

            else:
                return 0, "没有变化。"

        def get_tip(self, act, result, customers, final_tip_change=0, first_customer=False, specials = []):

            # Modifiers that are related to the performance are handed by the perform() function

            ## 1. Base tip depends on customer and girl rank ##

            cust_rank = ((sum(c.diff for c in customers)/float(len(customers)))/10.0) ** 0.5 # Testing this formula suggested by Chris12: rank = squareroot of ('customer average difficulty' / 10)

            tip = tip_base * cust_rank * self.rank

            # Tip increases with customer difficulty and perk-related bonuses

            tip += sum(cust.diff for cust in customers)

            # Sanity check, although impossible for tip to be this low in vanilla
            tip = max(10, tip)

            if "lost virginity" in specials:
                tip += 100
                gold_ttip = "Base tip: {image=img_gold}%i(失去童贞: {image=img_gold}+100)\n" % tip
            else:
                gold_ttip = "Base tip: {image=img_gold}%i\n" % tip

            ## 2. Generic multipliers apply to the base tip ##

            tip_multiplier = 1.0

            # Work tip is higher if the girl is naked
            if self.naked and act in all_jobs:
                tip_multiplier *= tip_act_modifier["naked bonus"] * self.get_effect("boost", "naked bonus")
                gold_ttip += "\nNaked bonus: x%s" % percent_text(tip_act_modifier["naked bonus"] * self.get_effect("boost", "naked bonus"), False)

            if "bisexual" in specials:
                tip_multiplier *= tip_act_modifier["bisexual bonus"]
                gold_ttip += "\nBisexual bonus: %s" % tip_act_modifier["bisexual bonus"]

            # Group sex
            if act in all_sex_acts and len(customers) > 1:
                tip_multiplier *= tip_act_modifier["group bonus"] * len(customers) #? As diff already increases base tip for groups, this might be too much of an advantage
                gold_ttip += "\nGroup bonus: x%s" % percent_text(tip_act_modifier["naked bonus"] * self.get_effect("boost", "naked bonus"), False)

            # Result boost
            if act in all_jobs:
                tip_multiplier *= tip_result_modifier["job " + result] * self.get_effect("boost", result + " result tip")
                gold_ttip += "\nResult bonus: x%s" % percent_text(tip_result_modifier["job " + result] * self.get_effect("boost", result + " result tip"), False)
            else:
                tip_multiplier *= tip_result_modifier["whore " + result] * self.get_effect("boost", result + " result tip")
                gold_ttip += "\nResult bonus: x%s" % percent_text(tip_result_modifier["whore " + result] * self.get_effect("boost", result + " result tip"), False)

            ## 3. Perk multipliers and other special effects apply (additive) ##

            # Boost effects
            perk_tip_multiplier = self.get_effect("boost", "tip")

            if "focus" in specials:
                perk_tip_multiplier += 0.25

            if "virgin tip" in specials:
                perk_tip_multiplier += self.get_effect("boost", "virgin tip") - 1

            # First customer effect
            if first_customer: # Reduces the boost by the number of customers to achieve the first customer effect
                perk_tip_multiplier += (self.get_effect("boost", "first customer tip") - 1) / len(customers)

            # Business & pleasure perk
            if act in all_jobs:
                perk_tip_multiplier += self.get_effect("boost", "total tip", custom_scale=("job cust nb", len(customers))) - 1
            elif act in all_sex_acts:
                perk_tip_multiplier += self.get_effect("boost", "total tip", custom_scale=("whore cust nb", self.get_log("whore_cust", "today"))) - 1

            if perk_tip_multiplier != 1.0:
                gold_ttip += "\nPerks and special effects: x%s" % percent_text(perk_tip_multiplier, False)

            tip_multiplier *= perk_tip_multiplier

            # Sanity check: final tip_multiplier cannot go below 10% or above 500%
            if tip_multiplier > 5.0:
                gold_ttip += "\n{i}Total modifier cannot exceed x5.0{/i}"
            tip_multiplier = min(5.0, max(0.1, tip_multiplier))

            tip *= tip_multiplier

            #<Chris Job Mod>
            if game.has_active_mod("chrisjobmod"):
                tip /= act_max_customers_modifier[self.job]
                gold_ttip += "\nJob Mod modifier: x%s" % percent_text(1.0/act_max_customers_modifier[self.job], False)
            #</Chris Job Mod>

            ## 4. Extra flat tip is added ##

            # Most tip changes now apply last. Some perks may need rebalancing (to be tested)
            extra = self.get_effect("change", "tip") + final_tip_change

            tip += extra
            if extra:
                gold_ttip += "\n\nExtra tip: {image=img_gold}%s" % plus_text(extra)
                if final_tip_change:
                    gold_ttip += " (Five stars perk: {image=img_gold}%s" % plus_text(final_tip_change)

            ## 5. Difficulty and cheat modifiers multiply everything ##

            # Difficulty/Cheats
            tip *= cheat_modifier["gold"] * game.get_diff_setting("gold")
            gold_ttip += "\n\nDifficulty modifier: x%s" % percent_text(cheat_modifier["gold"] * game.get_diff_setting("gold"), False)

            # A final (unneeded) sanity check is applied
            tip = max(10, round_int(tip))

            gold_ttip += "\n\n= {image=img_gold}%i" % tip

            return tip, gold_ttip

        def get_street_tip(self): # Returns average tip value for street whores
            return max(self.get_price("sell") // 100, tip_base) * cheat_modifier["gold"] * game.get_diff_setting("gold")

        def whore_on_street(self): # Runs every night a broken girl is on the street. Returns tip value.

            # 1. Get tip
            min_tip = self.get_street_tip() // 2

            tip = renpy.random.randrange(min_tip, min_tip*3) * self.get_effect("boost", "street whore tip")

            # 2. Degrade stats (Street whores erode their stats over time)
            for s in self.stats + self.sex_stats:

                eff = self.get_effect("change", "street whore skill erosion") # May be -1 or -2

                if self.get_stat(s.name) > 150:
                    chg = 1-dice(6+eff) # 0 to -5
                elif self.get_stat(s.name) > 75:
                    chg = 1-dice(5+eff) # 0 to -4
                elif self.get_stat(s.name) > 25:
                    chg = 1-dice(4+eff) # 0 to -3
                else:
                    chg = 1-dice(3+eff) # 0 to -2

                if chg:
                    self.change_stat(s.name, chg, silent=True)

            # 3. Chance of disappearance

            grace_period = 14 # Girls will not disappear during the grace period

            if self.streetdays < grace_period:
                pass
            elif self.street_roll <= 1 + (self.streetdays - grace_period)/10: # After the grace period, increasing chance of disappearance
                calendar.set_alarm(calendar.time + 1, StoryEvent("girl_disappeared", arg=self, type = "morning"))

            # Roll is generated the day prior to discourage save scumming. Boost values can be 3.0, 9.0, 27.0
            self.street_roll = dice(100 * self.get_effect("boost", "street whore security"))

            # 4. Counter and log
            self.street_days += 1
            self.today_street_tip = tip

            return tip


        def get_energy_color(self):
            max_en = self.get_stat_max("energy")

            if self.energy >= 0.8 * max_en:
                return c_green
            elif self.energy >= 0.6 * max_en:
                return c_lightgreen
            elif self.energy >= 0.4 * max_en:
                return c_yellow
            elif self.energy >= 0.2 * max_en:
                return c_lightred
            else:
                return c_red

        def get_energy_ttip(self):
            max_en = self.get_stat_max("energy")

            if self.energy >= 0.8 * max_en:
                ttip = "她精力充沛。"
            elif self.energy >= 0.6 * max_en:
                ttip = "她充满活力。"
            elif self.energy >= 0.4 * max_en:
                ttip = "她有点累了。"
            elif self.energy >= 0.2 * max_en:
                ttip = "她摇摇欲坠。"
            else:
                ttip = event_color["bad"] % "警告! 她已经非常累了。"

            return ttip

        def tire(self, x): # Where x is a positive number (important)

            # Frenzy effect
            if self.get_effect("special", "ignore energy"):
                return "\n{color=[c_purple]}" + self.name + "不知疲倦地工作.{/color}", 0

            chg = x * self.get_effect("boost", "tiredness") + self.get_effect("change", "tiredness")

            # This is a test: reduce tiredness by 15% per rank

            chg *= self.get_effect("boost", "energy use") # (1 - (self.rank-1)*0.15)

            r, _case = self.change_energy(-chg)

            text1 = ""
            text2 = plus_text(round_int(r), "standard")

            if _case == "exhausted":
                text1 += "\n{color=[c_red]}" + self.name + "累倒在地，无法继续工作了.{/color}"

                if self.hurt:
                    text1 += "\n{color=[c_red]}" + "她生病了，必须休养" + str(round_int(self.hurt)) + "天.{/color}"

                self.add_log("exhausted")
                self.track_event("exhausted")

            return text1, r


        def get_hurt(self, x):

            if self.get_effect("special", "immune"):
                notify("%s 对受伤免疫。" % self.name, pic=self.portrait)
                return 0

            chg = round(x * self.get_effect("boost", "hurt") + self.get_effect("change", "hurt") - self.get_effect("resist", "hurt"))

            self.hurt += chg

            if self.hurt > 0:
                self.interactions = 0
            elif self.hurt < 0:
                self.hurt = 0

            update_effects()

            if chg >= 1:
                notify("%s 需要 %i 天疗伤。" % (self.fullname, chg), pic=self.portrait)

            return chg

        def health_check(self):

            d = dice(100) + self.get_stat("constitution") - brothel.dirt

            if d < -50:
                self.get_hurt(dice(5))
            elif d < -25:
                self.get_hurt(dice(3))
            elif d < -5:
                self.get_hurt(dice(2))

            if d < 0 and self.hurt > 0:
                self.track_event("sick")
                return "sick"

            return "healthy"


        def change_energy(self, x):

            _min, _max = self.get_stat_minmax("energy")

            boost = reverse_if(self.get_effect("boost", "energy"), x) ## Reverses boost if decreasing stat

            r = get_change_min_max(self.energy, x*boost + self.get_effect("change", "energy"), _min, _max)

            if self in farm.girls:
                farm.exhaust_girl(self, energy=self.energy+r)

            self.energy += r

            if self.energy <= 0:
                if not self.exhausted:
                    self.exhausted = True
                    self.resting = True
                    update_effects()
                return r, "exhausted"

            elif self.energy >= _max:
                if self.exhausted:
                    self.exhausted = False
                    self.resting = False
                    update_effects()
                    return r, "recovered"

            return r, ""


        def can_heal_from_item(self):
            if not hasattr(self, "last_healing_item"):
                self.last_healing_item = 0

            if self.last_healing_item < calendar.time:
                return True
            else:
                return False

        def heal(self, chg = 1, from_item=False):

            chg = chg * self.get_effect("boost", "heal") + self.get_effect("change", "heal")

            self.hurt = max(self.hurt-chg, 0)

            if from_item:
                self.last_healing_item = calendar.time

            if self.hurt > 0:
                return chg, "sick"
            else:
                update_effects()
                notify(self.fullname + "已经痊愈了", pic=self.portrait)
                return chg, "healthy"

        def full_rest(self):
            self.hurt = 0
            self.energy = self.get_stat_minmax("energy")[1]

        def rest(self, context=None, mod=1):

            if context == "farm":
                resting_changes = NightChangeLog(title="Holding")
                resting_text = self.fullname + " 在地牢里休息。"
            else:
                resting_changes = NightChangeLog(title="Resting")
                resting_text = self.fullname + " 在房间里休息。"

            if self.hurt > 0:
                r, case = self.heal(1)

                resting_changes.add("\n{color=[c_green]}Health{/color}: %s" % plus_text(r, color_scheme="standard"))

                if case == "healthy":
                    resting_changes.add("(full recovery)", "header", col="good", separator="\n")
                    if context == "farm":
                        resting_text += "\n{color=[c_emerald]}她已经完全康复，可以回去工作或者接受训练了.{/color}"
                    elif self.job:
                        resting_text += "\n{color=[c_emerald]}她已经完全康复，可以继续作为 " + girl_related_dict[self.job] + "工作了.{/color}"
                    else:
                        resting_text += "\n{color=[c_emerald]}她已经完全康复，并继续在房间里休息.{/color}"

            x = (25 + self.get_stat("constitution")/4) * self.get_effect("boost", "energy when resting") + self.get_effect("change", "energy when resting")

            if self.hurt > 0: # Hurt girls recover half as fast
                x = x//2

            x *= mod

            r, case = self.change_energy(x)

            max_en = self.get_stat_max("energy")

            if self.energy >= 0.8 * max_en:
                col = c_green
            elif self.energy >= 0.6 * max_en:
                col = c_lightgreen
            elif self.energy >= 0.4 * max_en:
                col = c_yellow
            elif self.energy >= 0.2 * max_en:
                col = c_lightred
            else:
                col = c_red

            resting_changes.add("体力: %s/%i (%s)" % ("{color=%s}%i{/color}" % (col, self.energy), max_en, plus_text(r)), "header")

            if case == "recovered":
                resting_changes.add("(fully rested)", "header", col="good", separator="\n")
                if context == "farm":
                    resting_text += "\n{color=[c_emerald]}她已经完全休息好了，可以继续训练了.{/color}"
                elif self.job:
                    resting_text += "\n{color=[c_emerald]}她已经完全休息好了，可以继续作为" + girl_related_dict[self.job] + "工作了.{/color}"
                else:
                    resting_text += "\n{color=[c_emerald]}她已经完全休息好了，正在等待分配工作.{/color}"

            return resting_text, resting_changes


## Stats, Traits, Perks

        def find_stat(self, stat_name): # Returns the Stat object for a given stat name
            for s in (self.stats+self.sex_stats):
                if s.name.lower() == stat_name.lower():
                    return s
            return False

        def get_stat(self, stat_name, raw = False):

            result = None

            if stat_name in ("defense", "strength"):
                return self.get_defense()

            elif stat_name == "energy":
                return self.energy

            if raw:
                eff = 0
            else:
                eff = self.get_effect("change", stat_name) + self.get_effect("change", "all skills") # Adds changes to stats

                if stat_name.capitalize() in gstats_main:
                    eff += self.get_effect("change", "all main skills")
                elif stat_name.capitalize() in gstats_sex:
                    eff += self.get_effect("change", "all sex skills")

            stat = self.find_stat(stat_name)

            if stat == False: # wrong stat name
                raise AssertionError(stat_name + " 不是一个有效的属性/技能名称. 正确的: " + and_text(["defense", "strength", "energy"] + [s.name.lower() for s in (self.stats+self.sex_stats)]))

            result = stat.value + eff

            if result > 0:
                return round_int(result)

            else:
                return 0


        def get_xp_cap(self):

            if self.level < self.rank * 5:
                cap = xp_to_levelup[self.level]
            else:
                cap = xp_to_levelup[self.rank * 5 - 1]

            return cap


        def get_jp_cap(self, job = "all"):

            if job == "all":

                cap = jp_to_level[self.rank - 1]

            elif self.job_level[job] < self.rank:

                cap = jp_to_level[self.job_level[job]]

            else:

                cap = jp_to_level[self.rank - 1]

            return cap


        def get_rep_cap(self):

            if self.rank < district.rank:

                cap = rep_to_rank[self.rank]

            else:

                cap = rep_to_rank[district.rank]

            return cap


        def has_trait(self, name):

            for t in self.traits:
                if t.name.lower() == name.lower():
                    return True

            else:
                return False


        def has_perk(self, name): # Where name is a string, not the perk object

            if name == None:
                return True

            for p in self.perks:

                if p.name.lower() == name.lower():
                    return True

            else:
                return False


        def add_trait(self, trait, _pos=None, forced=False, no_perks=False): # Where 'trait' is an object (important)

#            renpy.say("", "Adding " + trait.name)

            if not forced:
                for t in self.traits:
                    if t.name in trait.opposite:
                        return False

            if _pos:
                self.traits.insert(_pos, trait)
            else:
                self.traits.append(trait)

            self.add_effects(trait.effects)

            if trait.archetype and self.perk_points > 0 and not no_perks:
                if self.archetypes[trait.archetype].unlocked:
                    self.acquire_perk(self.archetypes[trait.archetype].get_perks(0)[0], forced=True)
                    self.perk_points -= 1
                else:
                    self.unlock_archetype(trait.archetype)
                    self.perk_points -= 2

                # Sanity check: Perk points cannot go lower than 0 (for mods that add more Traits)
                self.perk_points = max(0, self.perk_points)

            return True


        def remove_trait(self, trait):

            self.traits.remove(trait)

            self.remove_effects(trait.effects)


        def list_effects(self):
            msg = ""
            for eff in self.effects:
                msg += eff.type + " " + eff.target + ", "

            return msg

        def get_effect(self, type, target, raw=False, custom_scale=("factor", 0), change_cap=False):
            # raw=True means no additional brothel or world effects will be included. MUST if you expect to get a string value
            # custom_scale is a tuple 'factor name', 'value' which is used for some perks
            # Change_cap will only return Effects with the change_cap attribute as True (which means it affects stat min and max)

            # Only brothel effects are currently in use

            r = get_effect(thing=self, type=type, target=target, custom_scale=custom_scale, change_cap=change_cap)

            if not raw:
                if type == "boost":
                    if self in MC.girls:
                        r *= get_effect(brothel, type, target, change_cap=change_cap)
                    elif self in farm.girls:
                        r *= get_effect(farm, type, target, change_cap=change_cap)
                    elif self in game.free_girls:
                        r *= get_effect(game, type, target, change_cap=change_cap)

                else:
                    if self in MC.girls:
                        r += get_effect(brothel, type, target, change_cap=change_cap)
                    elif self in farm.girls:
                        r += get_effect(farm, type, target, change_cap=change_cap)
                    elif self in game.free_girls:
                        r += get_effect(game, type, target, change_cap=change_cap)

            return r


        def add_effects(self, effects, apply_boost=False, spillover=False, expires = False):
            return add_effects(self, effects, apply_boost=apply_boost, spillover=spillover, expires=expires)

        def remove_effects(self, effects):
            remove_effects(self, effects)
            self.refresh_sex_acts() # Checks if sex_acts can still be done


        def get_defense(self, fight = False):

            defense = self.get_effect("change", "defense") * self.get_effect("boost", "defense")

            return defense

        def add_shield(self):
            self.add_effects(shield_effect)

        def test_shield(self):

            # Shield code to be fixed later

            if self.get_effect("special", "shield", raw=True):

                self.remove_effects(shield_effect)
                notify(self.name + " 被魔法护盾保护着", pic=self.portrait)
                renpy.pause(0.5)

                return True

            elif brothel.get_effect("special", "shield"):

                spl = MC.has_spell(bshield_spell)

                notify(self.name + " 被魔法护盾保护着", pic=self.portrait)
                renpy.pause(0.5)

                if spl:
                    MC.deactivate_spell(spl)

                return True

            return False



        def average_stats(self, stats): #Unused with the new system

            ## Tests the weighted average of all stats

            score = 0
            totalw = 0

            for tup in stats:

                stat, weight = tup

                score += self.get_stat(stat) * weight
                totalw += weight

            score /= float(totalw)

            return score


        def test_stats(self, stats, diff):

            stat_list = [(stats[0][0], "primary"), (stats[1][0], "secondary"), (stats[2][0], "booster"), (stats[3][0], "booster")]

            score = 0

            for stat, type in stat_list:

                if self.get_stat(stat) - diff >= 40: # Reduced the pos threshold for stats for now
                    score += stat_bonus[type][0]

                elif self.get_stat(stat) - diff >= 20: # Reduced the pos threshold for stats for now
                    score += stat_bonus[type][1]

                elif self.get_stat(stat) - diff >= 10:
                    score += stat_bonus[type][2]

                elif self.get_stat(stat) - diff >= 0:
                    score += stat_bonus[type][3]

                elif type != "booster":
                    if self.get_stat(stat) - diff <= -40: # Reduced the neg threshold for stats for now
                        score -= stat_bonus[type][0]

                    elif self.get_stat(stat) - diff <= -20: # Reduced the neg threshold for stats for now
                        score -= stat_bonus[type][1]

                    elif self.get_stat(stat) - diff <= -10:
                        score -= stat_bonus[type][2]

                    else:
                        score -= stat_bonus[type][3]

            return round_int(score)


        def raise_stats(self, stats, silent=False):

            changes = []

            # Stat increases are stored as tuples (stat_name, %chance, max increase/decrease)

            for s, chance, value in stats:

                if dice(100) <= chance:

                    stat = rand_choice(s)

                    if value > 0: # A dice is rolled from 1 to value
                        if dice(250) > self.get_stat(stat, raw=True): # A skill check makes it harder to raise a stat the higher it gets
                            r = self.change_stat(stat, dice(value) * cheat_modifier["stats"] * game.get_diff_setting("stats"), silent=silent)
                            changes.append((stat, r))

                    elif value < 0:
                        if dice(250) < self.get_stat(stat, raw=True): # A skill check makes it harder to lower a stat the lower it gets
                            r = self.change_stat(stat, value / cheat_modifier["stats"], silent=silent) # Diff setting modifier only applies to stat gains
                            changes.append((stat, r))

            return changes

        def can_upgrade_stat(self, stat): # Where stat is an object

            _min, _max = self.get_stat_minmax(stat.name, raw = True)

            if stat.value >= _max:
                return False
            return True

        def upgrade_stat(self, stat, chg, silent=True):
            r = self.change_stat(stat, chg, apply_boost = False, silent=silent)

            self.upgrade_points -= r

            if r < chg:
                return False
            else:
                return True

        def get_max_stat_upgrade_points(self, stat):
            result = self.get_stat_minmax(stat, raw = True)[1] - self.get_stat(stat, raw = True)
            if result > 0:
                if result > self.upgrade_points:
                    result = self.upgrade_points
                return round_int(result)
            else:
                return 0

        def get_stat_max(self, stat_name, raw = False, custom_cap=None):
            return self.get_stat_minmax(stat_name, raw, custom_cap)[1]

        def get_stat_minmax(self, stat_name, raw = False, custom_cap=None):

            if stat_name in ("love", "fear"):
                _min = -125
                _max = 125

            elif stat_name == "mood":

                _min = -125
                _max = 125

            elif stat_name in ("rep", "reputation"):

                _min = rep_to_rank[self.rank-1]
                _max = self.get_rep_cap()

            elif stat_name == "energy":

                _min = 0

                eff = self.get_effect("boost", "max energy")

                base = self.get_stat("constitution")+50

                _max = round(base * eff)

            elif stat_name == "xp":

                _min = 0
                _max = xp_to_levelup[self.rank * 5 - 1]

            elif stat_name == "jp":

                _min = 0
                _max = self.get_jp_cap()

            elif stat_name.capitalize() in gstats_main + gstats_sex:

                _min = 0

                max_eff = self.get_effect("change", stat_name.lower() + " max") + self.get_effect("change", "all skill max")

                if custom_cap: # Can set cap to a different value (for classes)
                    _max = custom_cap
                else: # Max cannot be be lower than current stat value
                    _max = max(self.rank * 50 + max_eff, self.get_effect("set", "all skill max"), self.get_stat(stat_name, raw=True))

                    if not raw:
                        eff = self.get_effect("change", stat_name.lower(), change_cap=True) + self.get_effect("change", "all skills", change_cap=True)

                        if stat_name.capitalize() in gstats_main:
                            eff += self.get_effect("change", "all main skills")
                        elif stat_name.capitalize() in gstats_sex:
                            eff += self.get_effect("change", "all sex skills")

                        _max += eff


            else:
                raise AssertionError(stat_name + " min/max not found.")

            return _min, round_int(_max)

        def stat_spillover(self, stat, chg, job=None): # Job must be specified for JP
            eff = self.get_effect("spillover", stat)

            if eff:
                # Targetting girls

                target_list = []

                if self in MC.girls:
                    if stat == "jp":
                        target_list = [g for g in MC.girls if g.job == job]
                    else:
                        target_list = MC.girls

                elif self in farm.girls:
                    target_list = farm.girls

                # Applying spillover effect

                if len(target_list) > 1:
                    chg = chg / (len(target_list) - 1)

                    for g in target_list:
                        if g != self:
                            if stat == "jp":
                                g.change_jp(chg*eff, job, apply_boost=False, spillover=False, silent=True) # spillover=False is needed to avoid an infinite feedback loop
                            else:
                                g.change_stat(stat, chg*eff, apply_boost=False, spillover=False, silent=True) # spillover=False is needed to avoid an infinite feedback loop


        def change_stat(self, stat, chg, apply_boost = True, spillover=True, custom_cap=None, silent=False): # custom_cap applies to stats only (for classes)

            if stat == "mood":
                return self.change_mood(chg)

            elif stat == "love":
                return self.change_love(chg, silent=silent)

            elif stat == "fear":
                return self.change_fear(chg, silent=silent)

            elif stat == "energy":
                return self.change_energy(chg)[0]

            elif stat in ("rep", "reputation"):
                return self.change_rep(chg, silent=silent)

            elif stat == "xp":
                return self.change_xp(chg, spillover=spillover, silent=silent)

            elif stat == "jp":
                return self.change_jp(chg, self.job, spillover=spillover, silent=silent)

            elif stat.endswith(" jp"):
                return self.change_jp(chg, stat[:-3], spillover=spillover, silent=silent)

            elif stat.endswith(" preference"):
                return self.change_preference(stat[:-11], chg, silent=silent)

            else:

                # Stat spillover (not currently used)
                if spillover:
                    self.stat_spillover(stat, chg)

                _min, _max = self.get_stat_minmax(stat, raw = True, custom_cap=custom_cap) # custom_cap can set maximum to a different value (for classes) - Experimental

                boost = 1.0

                if apply_boost:
                    boost = self.get_effect("boost", stat + " gains") * self.get_effect("boost", "all skill gains")

                for s in self.stats:
                    if s.name == stat.capitalize():
                        if apply_boost:
                            boost *= self.get_effect("boost", "all regular skills gains")

                            boost = reverse_if(boost, chg) ## Reverses boost if decreasing stat

                        r = s.change(chg*boost, _max)

                        if self.auto_upkeep:
                            self.adjust_upkeep()

                        if stat in ("obedience", "libido"):
                            self.refresh_sex_acts() # Checks if sex_acts can still be done

                        if not silent and r:
                            notify(stat_name_dict[s.name] + ": %s" % plus_text(r, color_scheme="stat"), pic=self.portrait) # Experimental

                        return r

                for s in self.sex_stats:
                    if s.name == stat.capitalize():
                        if apply_boost:
                            boost *= self.get_effect("boost", "all sex skills gains")

                            boost = reverse_if(boost, chg) ## Reverses boost if decreasing stat

                        r = s.change(chg*boost, _max)

                        if self.auto_upkeep:
                            self.adjust_upkeep()

                        test_achievements(gstats_main + gstats_sex + ["ultimate"])

                        if not silent and r:
                            notify(stat_name_dict[s.name] + ": %s" % plus_text(r, color_scheme="stat"), pic=self.portrait) # Experimental

                        return r

        def set_stat(self, stat, val): # Forces a stat to raw value val, ignoring random generation and caps. Only for girl skills (for now)
            for s in self.stats + self.sex_stats:
                if s.name == stat.capitalize():
                    s.set(val)
                    return

        def average_skills(self, sk_list, mod=1.0):

            t = 0

            for sk in sk_list:
                t += self.get_stat(sk, raw=True)

            avg = t / len(sk_list)

            avg *= mod

            # Total variation is limited to -20% from average
            change_dict = {sk: 0.8*avg for sk in sk_list}

            # The remaining points (0.2 * sk_nb * avg) are spread out randomly
            remaining_points = 0.2 * len(sk_list) * avg

            while remaining_points > 0: # May give an additional skill point depending on rounding (in favor of the player)
                change_dict[rand_choice(sk_list)] += 1
                remaining_points -= 1

            for sk in sk_list:
                self.set_stat(sk, change_dict[sk])

        def shuffle_skills(self, sk_list, mod=1.0):

            t = 0

            for sk in sk_list:
                t += self.get_stat(sk, raw=True)

            # The points are spread out randomly in rounds (producing more pronounced variation)
            change_dict = {sk: 0 for sk in sk_list}

            while t > len(sk_list)*10:
                change_dict[rand_choice(sk_list)] += 10
                t -= 10

            while t > len(sk_list)*5:
                change_dict[rand_choice(sk_list)] += 5
                t -= 5

            while t > 0:
                change_dict[rand_choice(sk_list)] += 1
                t -= 1

            for sk in sk_list:
                self.set_stat(sk, change_dict[sk])

## XP, rank and Level up

        def change_xp(self, value, apply_boost = True, spillover=True, silent=False):

            # XP spillover (Bride perk: confession) - Boosts don't apply
            if spillover:
                self.stat_spillover("xp", value)

            _min, _max = self.get_stat_minmax("xp")

            if apply_boost:

                boost = self.get_effect("boost", "xp gains")

                boost += 0.05 * self.remembers("reward", "level up") # Boosts XP is she was rewarded before

                boost = reverse_if(boost, value) ## Reverses boost if decreasing stat

            else:
                boost = 1.0

            change = value * boost

            if _min > self.xp + change:

                change = _min - self.xp
                self.xp = _min

            elif _max < self.xp + change:

                change = _max - self.xp
                self.xp = _max

            else:
                self.xp += change

            if change and not silent: notify("经验: %s" % plus_text(change, color_scheme="xp"), pic=self.portrait) # Experimental

            return change


        def change_jp(self, value, job, apply_boost = True, spillover=True, announcement_delay=1, silent=False):

            # JP spillover (Bride perk: confession) - Boosts don't apply
            if spillover:
                self.stat_spillover("jp", value, job=job)

            _min, _max = self.get_stat_minmax("jp")

            if apply_boost:

                boost = self.get_effect("boost", "all jp gains") * self.get_effect("boost", job + " jp gains")

                boost += 0.05 * self.remembers("reward", "job up") # Boosts JP is she was rewarded before

                boost = reverse_if(boost, value)

            else:

                boost = 1.0

            change = value * boost

            if _min > self.jp[job] + change:

                change = _min - self.jp[job]
                self.jp[job] = _min

            elif _max < self.jp[job] + change:

                change = _max - self.jp[job]
                self.jp[job] = _max

            else:
                self.jp[job] += change

            while self.ready_to_job_up(job):
                self.job_up(job, announcement_delay=announcement_delay)

            if change and not silent: notify(job.capitalize() + " 职业经验: %s" % plus_text(change, color_scheme="jp"), pic=self.portrait) # Experimental

            return change


        def level_up(self, forced = False):

            if self.ready_to_level() or forced:

                if forced:
                    self.xp = self.get_xp_cap()

                if self.level < 25: # Hard-coded level cap
                    self.level += 1

                    self.upgrade_points += 5 + 5 * self.rank

                    if self.level%5 == 0:
                        self.perk_points += 2
                    else:
                        self.perk_points += 1

                    # MC earns prestige when a girl levels up
                    MC.prestige += self.rank

                    self.track_event("level up", arg=self.level)

                    return True

            return False

        def debug_auto_level(self, chapter):
            if chapter > 6:
                ranks = 3
                levels = 20
            elif chapter > 4:
                ranks = 2
                levels = 15
            elif chapter > 2:
                ranks = 1
                levels = 10
            elif chapter > 1:
                ranks = 0
                levels = 5
            else:
                ranks = 0
                levels = 0

            for i in range(levels):
                # Simulates gained skills
                self.upgrade_points += 10*self.rank

                # Auto level and rank up
                self.auto_level_up(True)
                if self.level % 5 == 0 and ranks:
                    self.rank_up(True)
                    ranks -= 1


        def auto_level_up(self, forced = False):

            if self.level_up(forced):
                for stat in self.stats:
                    self.upgrade_stat(stat.name, self.upgrade_points/8.0)

        def rank_up(self, forced = False):

            if self.ready_to_rank() or forced:
                if forced:
                    self.rep = rep_to_rank[self.rank]

                if self.rank < 5:
                    self.rank += 1
                    self.rank_up_sanity()

                if self.auto_upkeep:
                    self.adjust_upkeep()

                self.track_event("rank up", arg=rank_name[self.rank])

                #ADD rank up animation


        def job_up(self, job, forced = False, announcement_delay=0):

            if self.ready_to_job_up(job) or forced:

                if self.job_level[job] < 5:
                    self.job_level[job] += 1

                    primary, secondary, add1, add2 = job_up_dict[job]

                    self.change_stat(primary, job_up_change[self.job_level[job]][0], apply_boost = False)
                    self.change_stat(secondary, job_up_change[self.job_level[job]][1], apply_boost = False)
                    self.change_stat(add1, job_up_change[self.job_level[job]][2], apply_boost = False)
                    self.change_stat(add2, job_up_change[self.job_level[job]][2], apply_boost = False)

                    self.track_event("job up", arg=job)

                    calendar.set_alarm(calendar.time + announcement_delay, Event(label = "job_up", object = (self, job, self.job_level[job])))


        def ready_to_level(self):

            if self.level < self.rank * 5:

                if self.xp >= self.get_xp_cap():

                    return True

            return False

        def can_spend_upgrade_points(self):
            if self.upgrade_points >= 1:
                for stat in self.stats:
                    if self.can_upgrade_stat(stat):
                        return True
            return False


        def ready_to_rank(self):

            if self.rank < district.rank:

                if self.rep >= rep_to_rank[self.rank] * self.get_effect("boost", "新的等级声望要求") and self.level >= self.rank * 5:

                    return True

            return False


        def ready_to_job_up(self, job):

            if job in (all_jobs + all_sex_acts):

                mylevel = self.job_level[job]

                if mylevel == 5:

                    return False

                elif self.jp[job] >= jp_to_level[mylevel] and mylevel < self.rank:

                    return True

            return False


        def unlock_archetype(self, archetype_name):
            if not self.archetypes[archetype_name].unlocked:
                self.archetypes[archetype_name].unlocked = True
                return True
            else:
                return False

        def can_acquire_perk(self, perk, context=None): # add_list is the list of perks in waiting

            if context == "perk_screen":
                points = perk_points
                perks = self.perks + new_perks
            else:
                points = self.perk_points
                perks = self.perks

            val = sum(1 for p in perks if p.archetype == perk.archetype)

            message = ""

            if not self.archetypes[perk.archetype].unlocked:
                message += translate_cn(perk.archetype, archetype_name_dict) + "暂时是锁定的。\n"
            elif val < perk.value:
                message += str(perk.value) + " 更多的等级必须先解锁。\n"
            elif self.rank < perk.min_rank:
                message += self.name + " 必须达到 " + rank_name[perk.min_rank] + "阶级,在她解锁这个天赋之前。\n"
            elif points < 1:
                message = self.name + " 没有足够的天赋点。"
            else:
                return True, ""

            return False, message


        def acquire_perk(self, perk, forced=False): ## Where perk is an object
            if perk not in self.perks:
                if not forced:
                    if self.can_acquire_perk(perk)[0]:
                        self.perk_points -= 1
                    else:
                        return self.can_acquire_perk(perk, self.perk_points)

                self.perks.append(perk)
                self.add_effects(perk.effects)
                self.reset_sex_acts(first=False)

                if perk.level == 3:
                    unlock_achievement(perk.archetype)


            return True, ""

        def refund_perks(self, min_level=0): # all perks above or equal to min_level will be refunded. Use min_level=0 to refund archetypes
            perk_points = 0

            for perk in self.perks:
                if perk.level >= min_level:
                    self.perks.remove(perk)
                    self.remove_effects(perk.effects)
                    self.reset_sex_acts(first=False)

                    perk_points += 1

            if min_level <= 0:
                for arch in archetype_dict.keys():
                    if self.archetypes[arch].unlocked:
                        self.archetypes[arch].unlocked = False
                        perk_points += 2

            self.perk_points += perk_points

            return perk_points



        def check_combo_perks(self):

            for p in combo_perks:
                if not self.has_perk(p.name) and self.has_prerequisites(p):
                    self.perks.append(p)
                    self.add_effects(p.effects)

                    renpy.call_screen("OK_screen", title = p.name, message = self.name + " 学会了一个新的组合! " + p.description)



        def has_prerequisites(self, perk):

            if perk.prerequisite != None:

                for pre in perk.prerequisite:
                    if not self.has_perk(pre):
                        return False

            return True


        def get_perk(self, perk): ## Where perk is an object (important)

            for p in self.perks:
                if p.name == perk.name:
                    return p
            else:
                return False


        def get_perk_level(self, perk): ## Where perk is an object (important)

            p = self.get_perk(perk)

            if p:
                return p.level

            else:
                return 0

        def change_rep(self, chg, silent=False):

            _min, _max = self.get_stat_minmax("rep")

            boost = self.get_effect("boost", "reputation gains") * game.get_diff_setting("rep")

            boost += 0.05 * self.remembers("reward", "rank up") # Boosts REP is she was rewarded before

            boost = reverse_if(boost, chg)

            chg = get_change_min_max(self.rep, chg*boost, _min, _max)
#            renpy.say("", "Changing rep by " + str(chg))

            self.rep += chg

            if not silent: notify("声誉: %s" % plus_text(int(chg)), col="rep", pic=self.portrait)

            return chg




## For MC / Girl interactions

        def generate_personality(self, personality=None, change=False): # Where personality is a string if provided. Use change=True to change her existing personality

            if use_ini_personality and self.init_dict["custom personality/custom_personality"] and not change: #? Warning: check if changing personality doesn't break some custom-made girlpacks
                self.personality = Personality(
                                                name=self.init_dict["custom personality/personality_name"],
                                                attributes=self.init_dict["custom personality/attributes"],
#                                                 generic_dialogue=self.init_dict["custom personality/generic_dialogue"],
                                                personality_dialogue_only=self.init_dict["custom personality/personality_dialogue_only"],
                                                dialogue_personality_weight=self.init_dict["custom personality/dialogue_personality_weight"],
                                                dialogue_attribute_weight=self.init_dict["custom personality/dialogue_attribute_weight"],
                                                description=self.init_dict["custom personality/description"],
                                                )

            elif use_ini_personality and self.init_dict["base personality/always"] and not change: # If a specific personality is provided in the init file
                self.personality = gpersonalities[rand_choice(self.init_dict["base personality/always"])]

            elif personality and (personality not in self.init_dict["base personality/never"] or not use_ini_personality): # If a specific personality is provided as an argument (will not override init setting depending on use_ini_personality)
                self.personality = gpersonalities[personality]

            else: # Random personality
                personalities = []

                for pers in gpersonalities.values(): # In this case, pers is an Object
                    if pers in self.init_dict["base personality/never"] or (change and self.personality == pers):
                        pass
                    elif pers in self.init_dict["base personality/often"]:
                        personalities.append((pers, 4))
                    elif pers in self.init_dict["base personality/rarely"]:
                        personalities.append((pers, 1))
                    else:
                        personalities.append((pers, 2))

                self.personality = weighted_choice(personalities)

            # Receives custom dialogue if applicable
            if use_ini_personality and self.init_dict["custom personality/custom_dialogue_label"]:
                self.custom_dialogue_label = self.init_dict["custom personality/custom_dialogue_label"]

            # Receives a list of attributes from its parent personality
            self.attributes = self.personality.generate_attributes(self)
            self.gift_likes = self.personality.gift_likes

        def adjust_personality(self): # Use if her personality attributes have changed

            adjust = False

            # Checks if her defining attributes are still there
            for attr in self.personality.attributes:
                if attr.startswith("very"):
                    if not self.is_(attr[5:]):
                        adjust = True
                        break
                elif not self.is_(attr):
                    adjust = True
                    break

            # If not, looks for a matching personality
            if adjust:
                new_pers = None
                best_score = 0

                for pers in random.sample(gpersonalities, len(gpersonalities)): # Shuffles a copy of the gpersonalities list
                    score = 0
                    for attr in pers.attributes:
                        if self.is_(attr):
                            score += 3
                        elif self.is_(attr[5:]):
                            score += 1
                    if score > best_score:
                        new_pers = pers

                self.personality = new_pers
                self.gift_likes = self.personality.gift_likes


        def generate_background(self, t2=0):
            if self.init_dict["tastes/hobbies"]:
                self.hobbies = self.init_dict["tastes/hobbies"]
            else:
                self.hobbies = rand_choice(hobbies, 2)

            # self.hobbies.append(rand_choice(hobbies))
            # self.hobbies.append(hobbies[hobbies.index(self.hobbies[0]) - dice((len(hobbies)-1))])

            if self.init_dict["background story/origin"] and self.init_dict["background story/origin"] != "random":
                self.origin = self.init_dict["background story/origin"]
            else:
                self.origin = rand_choice(origins)

            if self.init_dict["background story/story_label"]:
                self.story = self.init_dict["background story/story_label"]
            else:
                # generates random slave story
                if self.init_dict["background story/always_slave_story"]:
                    self.story = rand_choice(self.init_dict["background story/always_slave_story"])
                else:
                    available_stories = []
                    for story in slave_stories:
                        if story not in (self.init_dict["background story/never_slave_story"] + self.personality.story_dict["never"]):
                            # _BK.ini settings take precedence over personality settings
                            if story in self.init_dict["background story/often_slave_story"]:
                                w = 4
                            elif story in self.init_dict["background story/rarely_slave_story"]:
                                w = 1
                            elif story in self.personality.story_dict["often"]:
                                w = 4
                            elif story in self.personality.story_dict["rarely"]:
                                w = 1
                            else:
                                w = 2
                            available_stories.append((story, w))
                    self.story = weighted_choice(available_stories)

            self.story_profession = rand_choice([pop for pop in all_populations if pop.name != "royals"]).get_rand_name("M")
            self.story_profession_article = article(self.story_profession)
            self.story_home = rand_choice(homes)
            self.story_home_article = article(self.story_home)
            self.story_guardian = rand_choice(guardians)
            self.flags["story"] = 4 # Used in combination with personality unlock["story"] to check when unlocking a new part of the girl's background story
            self.personality_unlock = defaultdict(int)
            self.personality_unlock["likes"] = []
            self.personality_unlock["loves"] = []
            self.personality_unlock["hates"] = []

            if self.init_dict["tastes/favorite_color"]:
                self.likes["color"] = self.init_dict["tastes/favorite_color"]
            else:
                self.likes["color"] = rand_choice(colors)
            if self.init_dict["tastes/favorite_food"]:
                self.likes["food"] = self.init_dict["tastes/favorite_food"]
            else:
                self.likes["food"] = rand_choice(food)
            if self.init_dict["tastes/favorite_drink"]:
                self.likes["drink"] = self.init_dict["tastes/favorite_drink"]
            else:
                self.likes["drink"] = rand_choice(drinks)

            if self.init_dict["tastes/disliked_color"]:
                self.dislikes["color"] = self.init_dict["tastes/disliked_color"]
            else:
                self.dislikes["color"] = colors[colors.index(self.likes["color"]) - dice((len(colors)-1))] # Avoids picking the color she likes
            if self.init_dict["tastes/disliked_food"]:
                self.dislikes["food"] = self.init_dict["tastes/disliked_food"]
            else:
                self.dislikes["food"] = food[food.index(self.likes["food"]) - dice((len(food)-1))] # Avoids picking the color she likes
            if self.init_dict["tastes/disliked_drink"]:
                self.dislikes["drink"] = self.init_dict["tastes/disliked_drink"]
            else:
                self.dislikes["drink"] = drinks[drinks.index(self.likes["drink"]) - dice((len(drinks)-1))] # Avoids picking the color she likes

            t3 = time.perf_counter()
            game.func_time_log2 += "\nbackground: %s" % (t3 - t2)

            return t3

        def change_relationship(self, other_girl, chg):

            self.relations[other_girl] += chg

            if self.relations[other_girl] > 3 and other_girl not in self.friends:
                self.friends.append(other_girl)
                if other_girl in self.rivals:
                    self.rivals.remove(other_girl)

            elif self.relations[other_girl] <= 3 and other_girl in self.friends:
                self.friends.remove(other_girl)

            elif self.relations[other_girl] >= -3 and other_girl in self.rivals:
                self.rivals.remove(other_girl)

            elif self.relations[other_girl] < -3 and other_girl not in self.rivals:
                self.rivals.append(other_girl)
                if other_girl in self.friends:
                    self.friends.remove(other_girl)

            return self.get_friendship(other_girl)

        def get_compatibility(self, other_girl): # Calculates a score to see if the girl is an ally or a rival. Relationship scores are stored in a dictionary for faster processing
            if self.g_compatibility[other_girl] == False:
                pass
            else: # Calculates a score if none exists for this pairing
                self.g_compatibility[other_girl] = 0

                for attr in self.attributes:
                    for k, v in attribute_score_dict[attr].items():
                        if other_girl.is_(k):
                            self.g_compatibility[other_girl] += v

            if self.g_compatibility[other_girl] >= 4:
                return "good"
            elif self.g_compatibility[other_girl] <= -4:
                return "bad"
            else:
                return None

        def update_relationships(self): # Returns a list of all changed relationships

            if len(MC.girls) < 2:
                return None

            other_girl = rand_choice(MC.girls)

            while other_girl == self:
                other_girl = rand_choice(MC.girls)

            old_status = self.get_friendship(other_girl)

            if self.get_compatibility(other_girl) == "good":
                mod = 1
            elif self.get_compatibility(other_girl) == "bad":
                mod = -1
            else:
                mod = 0

            if self.get_effect("change", "making friends"):
                mod += self.get_effect("change", "making friends")
            if other_girl.get_effect("change", "making friends"):
                mod += other_girl.get_effect("change", "making friends")

            r = dice(6, 2) + mod

            if r >= 11:
                new_status = self.change_relationship(other_girl, 1)
                other_girl.change_relationship(self, 1)

            elif r <= 3:
                new_status = self.change_relationship(other_girl, -1)
                other_girl.change_relationship(self, -1)

            else:
                new_status = old_status

            if new_status != old_status:
                change = [self, other_girl, old_status, new_status]
            else:
                change = None

            return change


        def get_friendship(self, other_girl):

            if other_girl == self:
                return "self"
            elif self.relations[other_girl] > 3:
                return "friend"
            elif self.relations[other_girl] < -3:
                return "rival"
            else:
                return "normal"


        def generate_preferences(self):

            # Set basic reluctance

            self.preferences = copy.copy(base_reluctance)

#             self.preferences = {}

#             for act, rel in base_reluctance.items():
#                 self.preferences[act] = base_reluctance[act]

            # Get pos/neg acts and fixations

            self.fix_level = defaultdict(int)
            self.locked_fix = []

            # Each girl receives 2 positive fixations (+ 1-2 for lewd girls) and 1 negative fixation (+ 1-2 for modest girls)

            pos_fix_nb = 2 # Changed to 2
            neg_fix_nb = 1

            if self.is_("very modest"):
                neg_fix_nb += 2
            elif self.is_("modest"):
                neg_fix_nb += 1
            elif self.is_("very lewd"):
                pos_fix_nb += 2
            elif self.is_("lewd"):
                pos_fix_nb += 1

            # 'Always' fixations from the .ini file are added first

            if use_ini_sex and self.init_dict["sexual preferences/always_fixations"]:
                if len(self.init_dict["sexual preferences/always_fixations"]) <= pos_fix_nb:
                    self.pos_fixations = [fix_dict[fix] for fix in self.init_dict["sexual preferences/always_fixations"]]
                else:
                    self.pos_fixations = [fix_dict[fix] for fix in rand_choice(self.init_dict["sexual preferences/always_fixations"], nb=pos_fix_nb)]

                pos_fix_nb -= len(self.pos_fixations)

#             for i in range(pos_fix_nb):
            if pos_fix_nb >= 1:
                self.add_random_fixation(type="pos", nb=pos_fix_nb)

            if self.personality.name == "masochist":
                self.add_random_fixation(act="fetish")

            if use_ini_sex and self.init_dict["sexual preferences/always_negative_fixations"]:
                if len(self.init_dict["sexual preferences/always_negative_fixations"]) <= neg_fix_nb:
                    self.neg_fixations = [fix_dict[fix] for fix in self.init_dict["sexual preferences/always_negative_fixations"]]
                else:
                    self.neg_fixations = [fix_dict[fix] for fix in rand_choice(self.init_dict["sexual preferences/always_negative_fixations"], nb=neg_fix_nb)]

                neg_fix_nb -= len(self.neg_fixations)

#             for i in range(neg_fix_nb):
            if neg_fix_nb >= 1:
                self.add_random_fixation(type="neg", nb=neg_fix_nb)

            # Init positive and negative sex acts

            self.reset_sex_acts()

            # Get farm weakness

            if use_ini_sex and self.init_dict["sexual preferences/farm_weakness"] in farm_type_list:
                self.weakness = self.init_dict["sexual preferences/farm_weakness"]
            else:
                self.weakness = rand_choice(farm_type_list)

            # Randomize preferences

            if use_ini_sex and self.init_dict["sexual preferences/sexual_experience"] in ["very experienced", "experienced", "average", "inexperienced", "very inexperienced"]:
                self.sexual_experience = self.init_dict["sexual preferences/sexual_experience"]
                self.training_value = sexual_training_value[self.sexual_experience] # For sorting purposes

            else:

                # This varies according to the girl's type (free or slave)

                d = dice(6, 2)

                if self.free: # Lewd free girls are more likely to have sexual experience
                    if self.is_("very lewd"):
                        d += 2
                    elif self.is_("lewd"):
                        d += 1
                    elif self.is_("very modest"):
                        d -= 2
                    elif self.is_("modest"):
                        d -= 1

                else: # Dom girls have less chance to endure long training than sub girls (but it is still possible)
                    if self.is_("very sub"):
                        d += dice(3)-1
                    elif self.is_("sub"):
                        d += dice(2)-1
                    elif self.is_("very dom"):
                        d -= -1 * dice(3) + 1
                    elif self.is_("dom"):
                        d -= -1 * dice(2) + 1


                # Bonuses grow higher with a higher district rank

                if d >= 12: # Very experienced girl
                    self.sexual_experience = "very experienced"
#                     pos_bonus = 250
#                     av_bonus = 150
#                     neg_bonus = 75
                elif d >= 10: # Experienced girl
                    self.sexual_experience = "experienced"
#                     pos_bonus = 150
#                     av_bonus = 75
#                     neg_bonus = 25
                elif d >= 5: # Average girl
                    self.sexual_experience = "average"
#                     pos_bonus = 75
#                     av_bonus = 25
#                     neg_bonus = 0
                elif d >= 3: # Unexperienced girl
                    self.sexual_experience = "inexperienced"
#                     pos_bonus = 25
#                     av_bonus = 0
#                     neg_bonus = -25
                else: # Completely unexperienced girls
                    self.sexual_experience = "very inexperienced"
#                     pos_bonus = 0
#                     av_bonus = 0
#                     neg_bonus = -50

                self.training_value = sexual_training_value[self.sexual_experience] # For sorting purposes

            pos_bonus, av_bonus, neg_bonus = experienced_modifiers[self.sexual_experience]

            if self.free:
                # Free girls are 'broken' according to their tastes

                for act in self.preferences.keys():

                    if act in self.pos_acts and not act in self.neg_acts:
                        if pos_bonus:
                            self.change_preference(act, pos_bonus * district.rank + dice(pos_bonus, district.rank), fast=True, silent=True)
                    elif act in self.neg_acts and not act in self.pos_acts:
                        if neg_bonus > 0:
                            self.change_preference(act, neg_bonus * district.rank + dice(neg_bonus, district.rank), fast=True, silent=True)
                        elif neg_bonus < 0:
                            self.change_preference(act, neg_bonus * district.rank - dice(-1*neg_bonus, district.rank), fast=True, silent=True)
                    else:
                        if av_bonus:
                            self.change_preference(act, av_bonus * district.rank + dice(av_bonus, district.rank), fast=True, silent=True)

            else:

                # Slave girls are 'broken' randomly (depending on their previous owner's taste)

                for act in self.preferences.keys():
                    d = dice(6)

                    if d >= 5:
                        if pos_bonus:
                            self.change_preference(act, pos_bonus * district.rank + dice(pos_bonus, district.rank), fast=True, silent=True)
                    elif d < 2:
                        if neg_bonus > 0:
                            self.change_preference(act, neg_bonus * district.rank + dice(neg_bonus, district.rank), fast=True, silent=True)
                        elif neg_bonus < 0:
                            self.change_preference(act, neg_bonus * district.rank - dice(-1*neg_bonus, district.rank), fast=True, silent=True)
                    else:
                        if av_bonus:
                            self.change_preference(act, av_bonus * district.rank + dice(av_bonus, district.rank), fast=True, silent=True)

            # Generate x skills according to preferences

            self.generate_stats(sex=True)

            ## Regulations (sanity check)

            # Naturist girls are at least comfortable about being naked
            if self.get_effect("special", "naked"):
                if self.preferences["naked"] < 0:
                    self.preferences["naked"] = 0

            # Virgin girls cannot be experienced with sx or group
            if self.has_trait("Virgin"):
                self.preferences["sex"]=base_reluctance["sex"]
                self.preferences["group"]=base_reluctance["group"]
                self.change_stat("sex", -250, silent=True)

            # Add limits to group and boosts to nkd?


            return


        def add_random_fixation(self, act=None, fixation=None, type="pos", nb=1): # When provided, fixation is the name (string), not the object

            # Returns False or a list of fixation names (may be only one)

            fixations = []

            if fixation:
                if fix_dict[fixation].available(self):
                    fixations.append(fixation)
                    return [fixation]
                else:
                    return False

            if act:
                available_fix = [(fix.name, fix.get_weight(self, type)) for fix in fix_dict.values() if fix.available(self, act, type)]
            else:
                available_fix = [(fix.name, fix.get_weight(self, type)) for fix in fix_dict.values() if fix.available(self, type=type)]

            if available_fix:
                fixations = weighted_choice(available_fix, nb) # always returns a list
            else:
                debug_notify("No " + type + " fixations found for " + self.fullname)
                return False

            if not fixations and debug_mode:
                raise AssertionError("Couldn't find %s %s fixations among available list: %s" % (nb, type, available_fix))

            if len(fixations) < nb and debug_mode:
                raise AssertionError("Couldn't find %s %s fixations among available list: %s" % (nb, type, available_fix))

            if type == "pos":
                self.pos_fixations += [fix_dict[f] for f in fixations]
            elif type == "neg":
                self.neg_fixations += [fix_dict[f] for f in fixations]

            return fixations # Returns a list of fixation names

        def reset_sex_acts(self, first=True):
            self.pos_acts = []
            self.neg_acts = []

            for fix in self.pos_fixations:
                self.pos_acts += [a for a in fix.acts if a not in self.pos_acts]


            for fix in self.neg_fixations:
                self.neg_acts += [a for a in fix.acts if a not in self.neg_acts]

            if first:
                for act in self.pos_acts:
                    eff = Effect("change", act + " preferences changes", 25)
                    self.effects.append(eff) # Removed add_effects to improve performance
                    self.effect_dict[(eff.type, eff.target)].append(eff)

                for act in self.neg_acts:
                    eff = Effect("change", act + " preferences changes", -50)
                    self.effects.append(eff) # Removed add_effects to improve performance
                    self.effect_dict[(eff.type, eff.target)].append(eff)

                # update_effects() # Shouldn't be needed here

        def raise_preference(self, act, type = None, bonus = 1, status_change=False, silent=False, use_effects=True): # Type is fear, love, or None. Bonus depends on the training act (MC, farm or normal play)

            # WARNING: raise_preference is badly named as it can got up of down depending on a girl's fixation modifiers. Set use_effects to False to enforce a positive result

            # Checks current preference

            _old = self.get_preference(act)

            # Test: adding libido to the result

            change = self.get_stat("obedience")//2 + self.get_stat("libido")

            if use_effects:
                change += self.get_effect("change", act + " preferences changes") + self.get_effect("change", "all preferences changes") # preferences changes effects can be negative

            if type == "love":
                change += self.get_love()
            elif type == "fear":
                change += self.get_fear()

            change *= bonus

            if change != 0:
                change = self.change_preference(act, change)

                if change > 0 and use_effects: # Only happens if use_effects is on (normal case)
                    if act not in ("naked", "service"): # All sex acts other than service influence naked preference a little
                        change2 = self.change_preference("naked", 0.25*change)

            _new = self.get_preference(act)

            # Returns new preference if there was a change in status

            if status_change:
                if _old != _new:
                    return change, _new
                else:
                    return change, False
            else:
                return change


        def change_preference(self, act, nb, fast=False, silent=False): # Fast disables some checks for performance

            if fast:
                boost = 1.0
            else:
                boost = self.get_effect("boost", act + " preference increase") * self.get_effect("boost", "all sex acts preference increase") * game.get_diff_setting("pref")

                if self in farm.girls:
                    boost *= self.get_effect("boost", "farm preference increase")

                boost = reverse_if(boost, nb)

            nb = get_change_min_max(self.preferences[act], nb*boost, -1000, 1000)

            self.preferences[act] += nb

            if not fast:
                if act == "bisexual" and compare_preference(self, "bisexual", "a little interested"):
                    story_flags["has_bis"] = True
                    if not bis_perk in self.perks:
                        self.acquire_perk(bis_perk, forced=True)
                        test_achievement("bisexual")

                if act == "group" and compare_preference(self, "group", "a little interested"):
                    story_flags["has_group"] = True
                    if not group_perk in self.perks:
                        self.acquire_perk(group_perk, forced=True)
                        test_achievement("group")
                    if compare_preference(self, "group", "very interested"):
                        if not orgy_perk in self.perks:
                            self.acquire_perk(orgy_perk, forced=True)

            if not silent:
                debug_notify("改变" + girl_related_dict[act] + "偏好(%s)，值：%i" % (self.fullname, nb), pic=self.portrait)

            return nb


        def get_preference(self, act, bonus=0):

            act = act.lower()
            pref = self.preferences[act] + bonus

            # Reminder: Base reluctance is negative

            for res in ("fascinated", "very interested", "interested", "a little interested", "indifferent", "a little reluctant", "reluctant", "very reluctant", "refuses"):
                if self.preferences[act] + bonus > get_preference_limit(act, res):
                    return res

## Girl moods

        def get_love(self):

            love = self.love

            love += self.get_effect("change", "love")
            if love > 0:
                love *= self.get_effect("boost", "love")
            elif love < 0:
                love *= self.get_effect("boost", "hate")

            return love

        def get_fear(self):

            fear = self.fear

            fear += self.get_effect("change", "fear")
            if fear > 0:
                fear *= self.get_effect("boost", "fear")
            elif fear < 0:
                fear *= self.get_effect("boost", "trust")

            return fear


        def change_love(self, amount, min_cap = None, max_cap = None, silent=False): # Cap is the limit above which love won't go with this action (used for free girls only)

            if self in game.free_girls:
                if not min_cap:
                    min_cap = 0
                if not max_cap:
                    max_cap = 100
            else:
                if not min_cap:
                    min_cap = self.rank*-25
                if not max_cap:
                    max_cap = self.rank*25

            # Charisma bonus = 10% per stat point, good/bad alignment = +/- 25%
            if self in MC.girls:
                boost = self.get_effect("boost", "love gains") * alignment_bonus[MC.get_alignment() + "_love"] * (1 + MC.get_charisma()*0.1)
            elif self in game.free_girls:
                boost = self.get_effect("boost", "love gains") * MC.get_effect("boost", "free girl love gains") * alignment_bonus[MC.get_alignment() + "_love"] * (1 + MC.get_charisma()*0.1)
            else:
                boost = 1.0

            boost = reverse_if(boost, amount) ## Reverses boost if decreasing love

#            renpy.say("", "Boost: " + str(boost))

            change = get_change_min_max(self.love, amount*boost, min_cap, max_cap, enforce_boundaries=False) # enforce_boundaries=False means the love value will not be reset to min or max cap if it exceeds them.
            self.love += change

            # if self in game.free_girls:
            #     change = get_change_min_max(self.love, change, -100, cap, enforce_boundaries=False)
            #     self.love += change
            # else:
            #     change = get_change_min_max(self.love, change, self.rank*-25, self.rank*25)
            #     self.love += change

            if not silent:
                if change > 0.5:
                    notify("好感度上升", pic=self.portrait, debug_txt="(%s)" % str(change))

                elif change < -0.5:
                    notify("好感度降低", pic=self.portrait, debug_txt="(%s)" % str(change))

            test_achievement("love")

            return change

        def change_fear(self, amount, min_cap = None, max_cap = None, mojo_color = "purple", silent=False):

            if not min_cap:
                min_cap = self.rank*-25
            if not max_cap:
                max_cap = self.rank*25

            # Charisma bonus = 10% per stat point, good/bad alignment = +/- 25%
            if self in MC.girls:
                boost = self.get_effect("boost", "fear gains") * alignment_bonus[MC.get_alignment() + "_fear"] * (1 + MC.get_charisma()*0.1)
            elif self in game.free_girls:
                boost = self.get_effect("boost", "fear gains") * MC.get_effect("boost", "free girl fear gains") * alignment_bonus[MC.get_alignment() + "_fear"] * (1 + MC.get_charisma()*0.1)
            else:
                boost = 1.0

            boost = reverse_if(boost, amount) ## Reverses boost if decreasing fear

            change = get_change_min_max(self.fear, amount*boost, min_cap, max_cap, enforce_boundaries=False) # enforce_boundaries=False means the fear value will not be reset to min or max cap if it exceeds them.
            self.fear += change

            # mojo generation (only if fear gained is positive)

            if change > 0:
                if mojo_color == "purple": # Regular fear gains
                    MC.raise_mojo(mojo_color, mojo = change / NORMAL_MOJO_VALUE)
                else: # Farm fear gains
                    MC.raise_mojo(mojo_color, mojo = change / FARM_MOJO_VALUE)

            if not silent:
                if change > 0.5:
                    notify("恐惧值上升", pic=self.portrait, debug_txt="(%s)" % str(change))

                elif change < -0.5:
                    notify("恐惧值减少", pic=self.portrait, debug_txt="(%s)" % str(change))

            test_achievement("fear")

            return change


        def get_obedience_check_target(self, act=None, train=False):

            if self.job == "whore" or act == "whore":
                coeff = 70
                if self.has_activated_sex_acts():
                    # Only the average modifier is kept
                    coeff += sum(preference_modifier[self.get_preference(act)] for act in self.does if self.does[act]) / sum(1 for act in self.does if self.does[act])

                    # Cannot completely offset mod (mood, obedience...)
                    if coeff < 30:
                        coeff = 30
                else: # Can no longer work as a whore
                    if self.job == "whore":
                        self.job = None
                        notify("%s 不能再当妓女了。" % self.fullname, pic=self.portrait)

                    # raise AssertionError("No sex act activated")

            elif act and act != "whore":
                coeff = 70

                # Checks modifier according to girl's preference/reluctance
                coeff += preference_modifier[self.get_preference(act)]

            else: # Regular job
                coeff = 35

            coeff += self.get_effect("change", "obedience target")

            if train:
                coeff += self.get_effect("change", "train obedience target")
            elif self.job == "whore" or act == "whore":
                coeff += self.get_effect("change", "whore obedience target")
            else:
                coeff += self.get_effect("change", "job obedience target")

            if train:
                if self.get_love() > self.get_fear(): # Dominant emotion is used if training.
                    mod = self.get_stat("obedience") + self.get_love() + self.mood//4
                else:
                    mod = self.get_stat("obedience") + self.get_fear() + self.mood//4
            else:
                mod = self.get_stat("obedience") + self.get_fear() + self.mood//4 - (self.get_stat_minmax("energy")[1] - self.energy)//10

            target = (0.96 ** mod) * coeff # Make 0.96 higher to increase difficulty

            ## Obedience link effect ##

            if self.get_effect("special", "link obedience", raw=True):
                girl2, is_super = self.get_effect("special", "link obedience", raw=True)

                if is_super:
                    target = min(target, girl2.get_obedience_check_target(act=act, train=train))
                else:
                    target = min(target, (target + girl2.get_obedience_check_target(act=act, train=train))/2)

            return target


        def obedience_check(self, act=None): # Will check if the girl will accept to work tonight

            target = self.get_obedience_check_target(act, train=False)

            result = renpy.random.randrange(100) * self.get_effect("boost", "obedience tests")

            # Boost to training check if girl remembers being rewarded or punished (Dom girls don't like punishment)

            if self.remembers("punish", "disobey"):
                if self.is_("very dom"):
                    result -= 5
                elif self.is_("dom"):
                    result += 0
                elif self.is_("very sub"):
                    result += 6 * self.remembers("punish", "disobey")
                elif self.is_("sub"):
                    result += 3 * self.remembers("punish", "disobey")

            self.last_obedience_check = str(result) + "/" + str(round_int(target))

            if result > target:
                return True

            else:
                return False

        def training_check(self, act):

            target = self.get_obedience_check_target(act, train=True)
            result = renpy.random.randrange(100) * self.get_effect("boost", "obedience tests")

            # Boost to training check if girl remembers being rewarded or punished (Dom girls don't like punishment)

            if self.remembers("reward", act):
                if self.is_("very materialist"):
                    result += 9 * self.remembers("reward", "act")
                elif self.is_("materialist"):
                    result += 6 * self.remembers("reward", "act")
                elif self.is_("very idealist"):
                    result += 0
                elif self.is_("idealist"):
                    result += 6 * self.remembers("reward", "act")

            if self.remembers("punish", act):
                if self.is_("very dom"):
                    result -= 5
                elif self.is_("dom"):
                    result += 0
                elif self.is_("very sub"):
                    result += 6 * self.remembers("punish", "act")
                elif self.is_("sub"):
                    result += 3 * self.remembers("punish", "act")

            if result > target:
                return "accepted"

            elif result > (target - 25):
                return "resisted"

            else:
                return "refused"

        def run_away_check(self): # Will check if the girl attempts to run away in the morning

            result = False

            if self.mood < mood_runaway_limit and self.ran_away_counter >= 5 and not (self.away or self.farm): # Girls only attempt to run away if their last failed attempt was more than 5 working days before

                if self.remembers("punish", "ran away"):
                    if self.is_("very dom"):
                        mod = 5
                    elif self.is_("dom"):
                        mod = 0
                    elif self.is_("very sub"):
                        mod = -6 * self.remembers("punish", "ran away")
                    elif self.is_("sub"):
                        mod = -3 * self.remembers("punish", "ran away")
                else:
                    mod = 0

                if dice(100) > 100 - (mood_runaway_limit - self.mood):
                    if dice(25*self.rank) + mod*self.rank >= (self.get_stat("obedience") + self.get_fear() + brothel.get_security()):
                        result = "runaway"

                if not result:
                    if 25*self.rank + mod*self.rank >= (self.get_stat("obedience") + self.get_fear() + brothel.get_security()):
                        result = "warning"

            self.ran_away_counter += 1

            return result


        def get_working_chance(self, act):

            chance = 100 - self.get_obedience_check_target(act)

            return get_change_min_max(0, chance, 0, 100)

        def get_training_chance(self, act): # Chance to accept training
            chance = 100 - self.get_obedience_check_target(act, train=True)

            return get_change_min_max(0, chance, 0, 100)

        def update_mood(self):

            self.change_mood(self.get_mood_modifier())


        def change_mood(self, chg):

            _min, _max = self.get_stat_minmax("mood")

            chg = get_change_min_max(self.mood, chg, _min, _max)

            self.mood += chg

            return chg

        def get_mood_modifier(self, love_text="", fear_text="", description=False):

            ## Lists active mood modifiers
            mood_factors = ""

            # Love and Fear
            l = self.get_love()
            f = self.get_fear()

            if self.personality.name != "masochist":
                mood_change = (l - f)/10
                if l >= 1:
                    mood_factors += "+" + str(round_best(l/10)) + ": " + love_text + "\n"
                elif l <= -1:
                    mood_factors += str(round_best(l/10)) + ": " + love_text + "\n"
                if f >= 1:
                    mood_factors += str(round_best(-f/10)) + ": " + fear_text + "\n"
                elif f <= -1:
                    mood_factors += "+" + str(round_best(-f/10)) + ": " + fear_text + "\n"
            else:
                mood_change = (l + f)/20
                if l >= 2:
                    mood_factors += "+" + str(round_best(l/20)) + ": " + love_text + "\n"
                elif l <= -2:
                    mood_factors += str(round_best(l/20)) + ": " + love_text + "\n"
                if f >= 2:
                    mood_factors += "+" + str(round_best(f/20)) + ": " + fear_text + "\n"
                elif f <= -2:
                    mood_factors += str(round_best(f/20)) + ": " + fear_text + "\n"

            # Farm girls

            if self in farm.girls:
                if farm.programs[self].target == "no training" and farm.programs[self].holding == "rest":
                    mood_change += 1
                    mood_factors += "+1: 她在农场休息。\n"
                else:
                    mood_change -= 1
                    mood_factors += "-1: 她在农场训练。\n"

            else: # Working girls
                w = 0
                if self.works_today():
                    if self.job == "whore" and self.get_effect("special", "whore mood modifier"):
                        w += 1
                        mood_factors += "+1: 她是个妓女而她性爱成瘾。\n"
                    elif self.workdays[calendar.get_weekday()] == 100:
                        w = -1
                        mood_factors += "-1: 她今天要工作一整晚。\n"
                    else: # Half shift
                        w = -0.5
                        mood_factors += "-0.5: 她今天要工作半宿。\n"
                elif self.assignment:
                    if self.assignment.type == "quest":
                        w = -1
                        mood_factors += "-1: 她正在外出完成委托。\n"
                    else: # Classes
                        w = -0.5
                        mood_factors += "-0.5: 她正在外出参加培训。\n"
                else:
                    w = 2
                    mood_factors += "+2: 她今天休息，在床上自慰。\n"

                up = self.get_upkeep_modifier()
                fr = (len(self.friends) - len(self.rivals)) * self.get_effect("boost", "mood gains from friendship")
                roo = brothel.get_mood_modifier(self.rank) # Uses room type modifier (between -7 and +10)
                bro = self.get_effect("change", "mood gains")

                mood_change += up + roo + bro + w + fr

                if up > 0:
                    mood_factors += "+" + str(up) + ": 她觉得她的薪水很优渥。\n"

                elif up < 0:
                    mood_factors += str(up) + ": 她对她的薪水很不满意。\n"

                if fr > 0:
                    mood_factors += "+" + str(round_best(fr)) + ": 她有闺蜜陪伴。\n"
                elif fr < 0:
                    mood_factors += str(round_best(fr)) + ": 她有死对头在。\n"

                if roo > 4:
                    mood_factors += "+" + str(round_best(roo)) + ": 她对她的房间很满意。\n"
                elif roo > 0:
                    mood_factors += "+" + str(round_best(roo)) + ": 她喜欢她的房间。\n"
                elif roo < -4:
                    mood_factors += str(round_best(roo)) + ": 她有些嫌弃她的房间。\n"
                elif roo < 0:
                    mood_factors += str(round_best(roo)) + ": 她的房间令她作呕。\n"

                # Change this later if more mood gain effects are added
                if bro > 1:
                    mood_factors += "+" + str(bro) + ": 姐妹们帮她开导放松。\n"
                elif bro > 0:
                    mood_factors += "+" + str(bro) + ": 有一个姐妹帮她开导放松。\n"

            # Life of Luxury perk
            mood_eff = self.get_effect("change", "mood")
            if mood_eff:
                mood_change += mood_eff
                if self.has_perk("Life of Luxury"):
                    mood_factors += plus_minus(mood_eff) + ": 她喜欢她的衣服(奢侈的生活)。\n"
                else:
                    mood_factors += plus_minus(mood_eff) + ": 其他效果影响。\n"


            if description:
                return mood_change, mood_factors

            else: # The following effects are not described in the mood tooltip

                # Business and Pleasure perk
                mood_change += self.get_effect("change", "mood", custom_scale=("cust nb", self.get_log("total_cust", 1)))

                boost = self.get_effect("boost", "mood gains")
                # reverses boost if negative change
                return mood_change * reverse_if(boost, mood_change)

        def get_mood_description(self, filter=None): # This returns text for the mood help screen

            l = self.get_love()

            if l > 90:
                love_text = "{color=" + color_dict["love +++"] + "}" + love_description["++++++"] + "{/color}"
            elif l > 70:
                love_text = "{color=" + color_dict["love +++"] + "}" + love_description["+++++"] + "{/color}"
            elif l > 50:
                love_text = "{color=" + color_dict["love ++"] + "}" + love_description["++++"] + "{/color}"
            elif l > 30:
                love_text = "{color=" + color_dict["love ++"] + "}" + love_description["+++"] + "{/color}"
            elif l > 15:
                love_text = "{color=" + color_dict["love +"] + "}" + love_description["++"] + "{/color}"
            elif l >= 5:
                love_text = "{color=" + color_dict["love +"] + "}" + love_description["+"] + "{/color}"
            elif l > -5:
                love_text = "{color=" + color_dict["normal"] + "}" + love_description["0"] + "{/color}"
            elif l >= -15:
                love_text = "{color=" + color_dict["love -"] + "}" + love_description["-"] + "{/color}"
            elif l >= -30:
                love_text = "{color=" + color_dict["love -"] + "}" + love_description["--"] + "{/color}"
            elif l >= -50:
                love_text = "{color=" + color_dict["love -"] + "}" + love_description["---"] + "{/color}"
            elif l >= -70:
                love_text = "{color=" + color_dict["love -"] + "}" + love_description["----"] + "{/color}"
            elif l >= -90:
                love_text = "{color=" + color_dict["love -"] + "}" + love_description["-----"] + "{/color}"
            else:
                love_text = "{color=" + color_dict["love -"] + "}" + love_description["------"] + "{/color}"

            f = self.get_fear()

            if self.personality.name != "masochist":
                if f > 90:
                    fear_text = "{color=" + color_dict["fear +++"] + "}" + fear_description["++++++"] + "{/color}"
                elif f > 70:
                    fear_text = "{color=" + color_dict["fear +++"] + "}" + fear_description["+++++"] + "{/color}"
                elif f > 50:
                    fear_text = "{color=" + color_dict["fear ++"] + "}" + fear_description["++++"] + "{/color}"
                elif f > 30:
                    fear_text = "{color=" + color_dict["fear ++"] + "}" + fear_description["+++"] + "{/color}"
                elif f > 15:
                    fear_text = "{color=" + color_dict["fear +"] + "}" + fear_description["++"] + "{/color}"
                elif f > 5:
                    fear_text = "{color=" + color_dict["fear +"] + "}" + fear_description["+"] + "{/color}"
                elif f >= -5:
                    fear_text = "{color=" + color_dict["normal"] + "}" + fear_description["0"] + "{/color}"
                elif f >= -15:
                    fear_text = "{color=" + color_dict["fear -"] + "}" + fear_description["-"] + "{/color}"
                elif f >= -30:
                    fear_text = "{color=" + color_dict["fear -"] + "}" + fear_description["--"] + "{/color}"
                elif f >= -50:
                    fear_text = "{color=" + color_dict["fear -"] + "}" + fear_description["---"] + "{/color}"
                elif f >= -70:
                    fear_text = "{color=" + color_dict["fear -"] + "}" + fear_description["----"] + "{/color}"
                elif f >= -90:
                    fear_text = "{color=" + color_dict["fear -"] + "}" + fear_description["-----"] + "{/color}"
                else:
                    fear_text = "{color=" + color_dict["fear -"] + "}" + fear_description["------"] + "{/color}"

            else:
                if f > 90:
                    fear_text = "{color=" + color_dict["fear +++"] + "}" + fear_description["M++++++"] + "{/color}"
                elif f > 70:
                    fear_text = "{color=" + color_dict["fear +++"] + "}" + fear_description["M+++++"] + "{/color}"
                elif f > 50:
                    fear_text = "{color=" + color_dict["fear ++"] + "}" + fear_description["M++++"] + "{/color}"
                elif f > 30:
                    fear_text = "{color=" + color_dict["fear ++"] + "}" + fear_description["M+++"] + "{/color}"
                elif f > 15:
                    fear_text = "{color=" + color_dict["fear +"] + "}" + fear_description["++"] + "{/color}"
                elif f > 5:
                    fear_text = "{color=" + color_dict["fear +"] + "}" + fear_description["+"] + "{/color}"
                elif f >= -5:
                    fear_text = "{color=" + color_dict["normal"] + "}" + fear_description["0"] + "{/color}"
                elif f >= -15:
                    fear_text = "{color=" + color_dict["fear -"] + "}" + fear_description["-"] + "{/color}"
                elif f >= -30:
                    fear_text = "{color=" + color_dict["fear -"] + "}" + fear_description["--"] + "{/color}"
                elif f >= -50:
                    fear_text = "{color=" + color_dict["fear -"] + "}" + fear_description["M---"] + "{/color}"
                elif f >= -70:
                    fear_text = "{color=" + color_dict["fear -"] + "}" + fear_description["M----"] + "{/color}"
                elif f >= -90:
                    fear_text = "{color=" + color_dict["fear -"] + "}" + fear_description["M-----"] + "{/color}"
                else:
                    fear_text = "{color=" + color_dict["fear -"] + "}" + fear_description["M------"] + "{/color}"

            m = self.mood

            if m > 90:
                mood_text = "{color=" + color_dict["+++"] + "}" + mood_description["++++++"] + "{/color}"
            elif m > 70:
                mood_text = "{color=" + color_dict["+++"] + "}" + mood_description["+++++"] + "{/color}"
            elif m > 50:
                mood_text = "{color=" + color_dict["++"] + "}" + mood_description["++++"] + "{/color}"
            elif m > 30:
                mood_text = "{color=" + color_dict["++"] + "}" + mood_description["+++"] + "{/color}"
            elif m > 15:
                mood_text = "{color=" + color_dict["+"] + "}" + mood_description["++"] + "{/color}"
            elif m >= 5:
                mood_text = "{color=" + color_dict["+"] + "}" + mood_description["+"] + "{/color}"
            elif m >= -5:
                mood_text = "{color=" + color_dict["normal"] + "}" + mood_description["0"] + "{/color}"
            elif m >= -15:
                mood_text = "{color=" + color_dict["-"] + "}" + mood_description["-"] + "{/color}"
            elif m >= -30:
                mood_text = "{color=" + color_dict["-"] + "}" + mood_description["--"] + "{/color}"
            elif m >= -50:
                mood_text = "{color=" + color_dict["--"] + "}" + mood_description["---"] + "{/color}"
            elif m >= -70:
                mood_text = "{color=" + color_dict["--"] + "}" + mood_description["----"] + "{/color}"
            elif m >= -90:
                mood_text = "{color=" + color_dict["---"] + "}" + mood_description["-----"] + "{/color}"
            else:
                mood_text = "{color=" + color_dict["---"] + "}" + mood_description["------"] + "{/color}"

            chg, mood_factors = self.get_mood_modifier(love_text, fear_text, description=True)

            if chg > 3:
                mood_change_text = mood_description["change +++"] + " {color=" + color_dict["+++"] + "}(+"
            elif chg > 1:
                mood_change_text = mood_description["change ++"] + " {color=" + color_dict["++"] + "}(+"
            elif chg > 0:
                mood_change_text = mood_description["change +"] + " {color=" + color_dict["+"] + "}(+"
            elif chg == 0:
                mood_change_text = mood_description["no change"] + " {color=" + color_dict["normal"] + "}("
            elif chg >= -1:
                mood_change_text = mood_description["change -"] + " {color=" + color_dict["-"] + "}("
            elif chg >= -3:
                mood_change_text = mood_description["change --"] + " {color=" + color_dict["--"] + "}("
            else:
                mood_change_text =  mood_description["change ---"] + " {color=" + color_dict["---"] + "}("

            mood_change_text += str(round_best(chg)) + "){/color}."

            if filter == "love":
                return love_text
            elif filter == "fear":
                return fear_text
            elif filter == "mood":
                return mood_text + mood_change_text + "\n精神状态: " + self.get_sanity()
            else:
                return love_text, fear_text, mood_text, mood_change_text, mood_factors



        def get_mood_picture(self): # returns picture path

            if self.mood >= 25:
                pic = "UI/mood good"
            elif self.mood <= -25:
                pic = "UI/mood bad"
            else:
                pic = "UI/mood normal"

            mod = self.get_mood_modifier()

            if mod > 0:
                pic += " up.webp"
            elif mod < 0:
                pic += " down.webp"
            else:
                pic += ".webp"

            return pic



## Commit girl to external job or class

        def commit(self, quest):
            self.away = True
            self.assignment = quest
            quest.enrolled.append(self)
            self.return_date = calendar.time + quest.duration
            add_event("return_from_quest", call_args = [self, quest], date = self.return_date)
            self.class_friend_bonus = 0
            for g in self.friends:
                if g in quest.enrolled:
                    self.class_friend_bonus = 2
                    break
            for g in self.rivals:
                if g in quest.enrolled:
                    self.class_friend_bonus = -1
                    break

            #             calendar.set_alarm(calendar.time + quest.duration, Event(label = "return_from_quest", object = (self, quest)))
            renpy.block_rollback()

        def return_from(self, quest):
            if self in quest.enrolled:
                quest.enrolled.remove(self)
            self.away = False
            self.assignment = None
            self.return_date = -1

            if quest.type == "quest":
                self.add_log("completed quest")
            elif quest.type == "class":
                self.add_log("completed class")


## LOG ACTIONS - Note: The various logs and stats are really messy and should be reworked from the grounds up

        def add_log(self, root, v = 1, _delay = 0):
            global temp_log

            k = root + str(calendar.time + _delay)

            ## Creates or increment daily log

            if k in self.log:
                self.log[k] += v
            else:
                self.log[k] = v

            ## Girl log garbage collection (attempt to improve performance)

            _old = root + str(calendar.time - 30)
            if _old in self.log:
                # Deletes entries 30 days prior
                del self.log[_old]

            ## Adds value to all time total

            if root in self.log:
                self.log[root] += v
            else:
                self.log[root] = v

            ## Tracking total game stats
            game.track(root, v)

            ## Tracking day stats
            if logs[calendar.time + _delay]:
                logs[calendar.time + _delay].track(root, v)
            else:
                logs[calendar.time + _delay] = Log(calendar.time + _delay)


        def get_log(self, root, days = 0): # If days = 0, get all time stats

            if days == 0:
                if root in self.log:
                    return self.log[root]
                else:
                    return 0

            elif days == "today":
                if (root + str(calendar.time)) in self.log:
                    return self.log[root + str(calendar.time)]
                else:
                    return 0

            else:

                total = 0

                for i in range(days):

                    if calendar.time - 1 - i > 0:
                        k = root + str(calendar.time - 1 - i)

                        if k in self.log:
                            total += self.log[k]
                        else:
                            total += 0

                    else:
                        break

                return total


        def get_average_performance(self, root, days):

            if self.get_log(root + "_score_base", days) != 0:

                perf = float(self.get_log(root + "_score", days)) / float(self.get_log(root + "_score_base", days))

                details = {}


                for r in ("perfect", "very good", "good", "average", "bad", "very bad",):

                    details[r] = str(round_int((100.0 * self.get_log(root + "_" + r, days) / self.get_log(root + "_score_base", days))))

                ttip = "完美：" + details["perfect"] + "%" + "           平均：" + details["average"] + "%" + "\n非常不错：" + details["very good"] + "%" + "      糟糕：" + details["bad"] + "%" + "\n不错：" + details["good"] + "%" + "              非常糟糕：" + details["very bad"] + "%"

                return round(perf, 1), ttip

            else:

                return "-", "这个女孩在选定的时间段内没有执行这个动作。"

        # Personality traits

        # def is_old(self, attr): # Attr can be a string or a tuple. If several attributes are requested, an 'and' clause is used
        #
        #     return self.has_attributes(attr)

        def is_(self, attributes, type="and"): # Checks if the girl has one or several attributes. Note: A girl with 'very X' will also be 'X'.

            attributes = make_list(attributes)

            if type == "and":
                for a in attributes:
                    if not a in self.attributes: # or "very " + a in self.attributes):
                        return False
                return True

            elif type == "or":
                for a in attributes:
                    if a in self.attributes: # or "very " + a in self.attributes:
                        return True
                return False

        def get_personality_description(self, show="personality"):

            des = "{b}" + self.fullname + " "

            if show == "personality":
                des += "的个性{/b}{size=-1}\n\n"

                ei = self.personality_unlock["EI"]
                mi = self.personality_unlock["MI"]
                lm = self.personality_unlock["LM"]
                ds = self.personality_unlock["DS"]

#                ei = 100
#                mi = 100
#                lm = 100
#                ds = 100

                des += self.name + " 是一个"

                if self.free and self in MC.girls + farm.girls:
                    des += "曾经自由的女孩"
                elif self.free:
                    des += "自由的女孩"
                else:
                    des += "奴隶"

                if self.personality_unlock["origin"]:
                    des += " 来自 " + self.origin

                des += "。"

                if self.flags["story"] < 10:
                    des += "你对她一无所知。"
                elif self.flags["story"] < 20:
                    des += "你对她有了初步的了解。"
                elif self.flags["story"] < 50:
                    des += "你对她的情况有些了解。"
                elif self.flags["story"] < 100:
                    des += "她告诉了你她的故事, 但你无动于衷。"
                elif self.flags["MC refused story"]:
                    des += "你很了解她的身世。"
                else:
                    des += "你很了解她的身世, 并为此做了一些事情。"

                des += "\n\n"

                if ei < 100 and mi < 100 and lm < 100 and ds < 100 and not always_show_personality[self]:
                    des += "你对她的性格一无所知。"


                if ei >= 100 or always_show_personality[self]:

                    if self.is_("very extravert"):
                        des += "她简直就是个 {b}社交恐怖分子{/b}。\n"
                    elif self.is_("extravert"):
                        des += "她很 {b}外向{/b}。\n"
                    elif self.is_("very introvert"):
                        des += "她很 {b}文静羞涩{/b}。\n"
                    elif self.is_("introvert"):
                        des += "她有一点 {b}害羞{/b}。\n"

                if mi >= 100 or always_show_personality[self]:
                    if self.is_("very materialist"):
                        des += "她非常 {b}自私贪婪{/b}, 如果有人妨碍她她会毫不留情地除掉他。\n"

                    elif self.is_("materialist"):
                        des += "她很 {b}肤浅和物质主义{/b}。\n"

                    elif self.is_("very idealist"):
                        des += "她很有 {b}梦想{/b},盼望着世界和平。\n"

                    elif self.is_("idealist"):
                        des += "她很 {b}关心他人{/b}。\n"

                if ds >= 100 or always_show_personality[self]:
                    if self.is_("very dom"):
                        des += "她 {b}积极向上意志坚定{/b} 希望别人能从她的角度看问题。\n"
                    elif self.is_("dom"):
                        des += "她知道自己想要什么,她是个 {b}独立女性{/b}。\n"
                    elif self.is_("very sub"):
                        des += "她很 {b}顺从{/b} 总是把自己摆在最后一位。\n"
                    elif self.is_("sub"):
                        des += "她很 {b}谦让{/b}, 她总是尽可能避免冲突。\n"

                if lm >= 100 or always_show_personality[self]:
                    if self.is_("very modest"):
                        des += "她非常保守并对性爱感到 {b}反感{/b}。\n"
                    elif self.is_("modest"):
                        des += "她遵循自己的 {b}道德准则{/b}, 对淫荡的行为感到不齿。\n"
                    elif self.is_("very lewd"):
                        des += "她只想要 {b}愉悦{/b}自己, 不在乎世俗偏见。\n"
                    elif self.is_("lewd"):
                        des += "她 {b}思想开放 没有底线{/b}。\n"

            # Add tastes

            elif show == "tastes":

                des += "的喜好{/b}{size=-1}\n\n"

                taste_text = ""

                if self.personality_unlock["fav_color"] or always_show_personality[self]:
                    taste_text += "她最爱的颜色是 {b}" + self.likes["color"] + "{/b}。"

                if self.personality_unlock["fav_food"] or always_show_personality[self]:
                    taste_text += "她最爱的食物是 {b}" + self.likes["food"] + "{/b}。"

                if self.personality_unlock["fav_drink"] or always_show_personality[self]:
                    taste_text += "她最爱的饮品是 {b}" + self.likes["drink"] + "{/b}。"

                if (self.personality_unlock["hobby_" + self.hobbies[0]] and self.personality_unlock["hobby_" + self.hobbies[1]]) or always_show_personality[self]:
                    taste_text += "她喜欢 {b}" + self.hobbies[0] + " 和 " + self.hobbies[1] + "{/b}。"

                elif self.personality_unlock["hobby_" + self.hobbies[0]]:
                    taste_text += "她喜欢 {b}" + self.hobbies[0] + "{/b}。"

                elif self.personality_unlock["hobby_" + self.hobbies[1]]:
                    taste_text += "她喜欢 {b}" + self.hobbies[1] + "{/b}。"

                if taste_text:
                    taste_text += "\n\n"

                if self.personality_unlock["dis_color"] or always_show_personality[self]:
                    taste_text += "她最讨厌的颜色是 {b}" + self.dislikes["color"] + "{/b}。"

                if self.personality_unlock["dis_food"] or always_show_personality[self]:
                    taste_text += "她最讨厌的食物是 {b}" + self.dislikes["food"] + "{/b}。"

                if self.personality_unlock["dis_drink"] or always_show_personality[self]:
                    taste_text += "她最讨厌的饮品是 {b}" + self.dislikes["drink"] + "{/b}。"


                if taste_text:
                    taste_text += "\n\n"

                if self.personality_unlock["loves"]:
                    taste_text += "她爱 {color=[c_emerald]}" + and_text([gift_description[luv] for luv in self.personality_unlock["loves"]]) + "{/color}。"
                    prior = "同时"
                    prior2 = "然而她"

                else:
                    prior = ""
                    prior2 = "她"

                if self.personality_unlock["likes"]:
                    taste_text += "她" + prior + "喜欢 {color=[c_orange]}" + and_text([gift_description[lik] for lik in self.personality_unlock["likes"]]) + "{/color}。"
                    prior2 = "然而她"

                if self.personality_unlock["hates"]:
                    taste_text += prior2 + "讨厌 {color=[c_crimson]}" + and_text([gift_description[hat] for hat in self.personality_unlock["hates"]]) + "{/color}。"

                # if debug_mode:
                #     taste_text += "She loves {color=[c_emerald]}" + and_text([gift_description[luv] for luv in [k for k, v in self.personality.gift_likes.items() if v >= 3]]) + "{/color}. "
                #     taste_text += "She likes {color=[c_orange]}" + and_text([gift_description[lik] for lik in [k for k, v in self.personality.gift_likes.items() if 3 > v >= 0]]) + "{/color}. "
                #     taste_text += "She hates {color=[c_crimson]}" + and_text([gift_description[hat] for hat in [k for k, v in self.personality.gift_likes.items() if v <= -2]]) + "{/color}. "

                if taste_text:
                    des += taste_text
                else:
                    des += "你对她的品位一无所知。"

            elif show == "sexual":

                des += "的性癖{/b}\n\n"

                sex_text = ""

                pos_unlocked = []
                amb_unlocked = []
                neg_unlocked = []

                for act in self.pos_acts:
                    if self.personality_unlock[act] or always_show_personality[self]:
                        if act in self.neg_acts:
                            amb_unlocked.append(girl_related_dict[act])
                        else:
                            pos_unlocked.append(girl_related_dict[act])

                for act in self.neg_acts:
                    if (self.personality_unlock[act] and act not in self.pos_acts) or always_show_personality[self]:
                        neg_unlocked.append(girl_related_dict[act])

                if pos_unlocked:
                    sex_text += "她有些喜欢 {color=[c_emerald]}" + and_text(pos_unlocked) + "{/color} 行为"

                    if neg_unlocked:
                        sex_text += ", 但她"
                    else:
                        sex_text += "。"

                if neg_unlocked:
                    if not sex_text:
                        sex_text += "她"
                    sex_text += "不喜欢 {color=[c_crimson]}" + and_text(neg_unlocked) + "{/color} 行为。"

                if amb_unlocked:
                    sex_text += "她对 {color=[c_yellow]}" + and_text(amb_unlocked) + "{/color} 行为感到迷茫。"

                if sex_text:
                    sex_text += "\n\n"

                pos_fix = [girl_related_dict[fix.name] for fix in self.pos_fixations if (self.personality_unlock[fix.name] or always_show_personality[self])]
                neg_fix = [girl_related_dict[fix.name] for fix in self.neg_fixations if (self.personality_unlock[fix.name] or always_show_personality[self])]

                if pos_fix:
                    sex_text += "她痴迷于 {color=[c_emerald]}" + and_text(pos_fix) + "{/color}。"
                if neg_fix:
                    sex_text += "她对 {color=[c_crimson]}" + and_text(neg_fix) + "{/color}感到恶心。"

                if sex_text:
                    des += sex_text
                else:
                    des += "你不太了解她的性癖。"

                if farm.knows["weakness"][self]:
                    des+= "\n她对农场的 %s 十分敏感" % self.weakness

            elif show == "recent":

                if self.free:
                    day_number = 84
                else:
                    day_number = 7

                des += "近期事件{/b}\n\n" + self.get_recent_events_description(day_number) + ""

            return des



        def track_event(self, type, arg=None):

            # Only the latest occurence of an event type is kept in the list

            if not self.recent_events[type]: # copies the template event once if it doesn't exist
                self.recent_events[type] = copy.copy(recent_event_templates[type])

            # Updates time and description

            self.recent_events[type].time = calendar.time

            if arg:
                self.recent_events[type].description = self.recent_events[type].base_description % arg
            else:
                self.recent_events[type].description = self.recent_events[type].base_description

            debug_notify("Tracking " + type + "...", pic=self.portrait)

            return


        def get_recent_events(self, day_number = 7, filter = None): # Events are returned with a tuple: Type, description, date

            event_list = []

            if self.recent_events:

                for type in self.recent_events.keys():
                    if self.recent_events[type]:
                        if self.recent_events[type].time in range(calendar.time - day_number, calendar.time+1):
                            if not filter or type == filter:
                                event_list.append(self.recent_events[type])

            event_list.sort(key = lambda x: x.time, reverse = True)

            return event_list # Returns a list sorted by date


        def get_recent_events_description(self, day_number = 7):

            description = ""
            events = self.get_recent_events(day_number)

#            renpy.notify(str(len(events)))

            if events:
                for ev in events:
                    description += calendar.get_date(ev.time) + ": " + ev.description
                    if self.remembers("reward", ev.type):
                        description += "{color=[c_emerald]} *奖励* :){/color}"

                    if self.remembers("punish", ev.type):
                        description += "{color=[c_crimson]} *惩罚* :({/color}"

                    description += "\n"


                if len(events) > 5:
                    description = "{size=-1}" + description + "{/size}"
            else:
                description = calendar.get_date(calendar.time) + ": 没有事件可以报告"

            return description

        def will_remember(self, context, type, score):

            if self.recent_events[type]:

                if context == "reward":
                    self.recent_events[type].reward(score)

                elif context == "punish":
                    self.recent_events[type].punish(score)

        def remembers(self, context, type): # Remembering is more effective when the memory is fresh
            if self.recent_events[type]:
                if context == "reward":
                    if self.recent_events[type].rewarded > 0:
                        return self.recent_events[type].rewarded * self.get_effect("boost", "reward efficiency")
                elif context == "punish":
                    if self.recent_events[type].punished > 0:
                        return self.recent_events[type].punished * self.get_effect("boost", "punishment efficiency")

            return 0

        def forgets(self):
            for type in self.recent_events.keys():
                if self.recent_events[type]:
                    self.recent_events[type].refresh()

        def test_weakness(self, act, unlock=False, feedback=False):

            _pos = False
            _neg = False

            if act in self.pos_acts:
                _pos=True

            if act in self.neg_acts:
                _neg=True

            if unlock:
                if not self.personality_unlock[act]:
                    self.personality_unlock[act] = True # Testing weakness unlocks the act for the personality screen

                    if feedback:
                        if _pos and _neg:
                            renpy.play(s_ahaa, "sound")
                            renpy.say("", "你注意到 " + self.name + " 对 " + long_act_description[act] + "既感觉快乐又感觉不适. 她似乎对此有矛盾的感觉。")
                        elif _pos:
                            renpy.play(s_mmh, "sound")
                            renpy.say("", "你注意到 " + self.name + " 对 " + long_act_description[act] + "感到享受。")
                        elif _neg:
                            renpy.play(s_scream, "sound")
                            renpy.say("", "你注意到 " + self.name + " 对 " + long_act_description[act] + "感到恶心。")

            return _pos, _neg

        def get_reaction_to_act(self, act):

            pos_reaction, neg_reaction = self.test_weakness(act)

            if pos_reaction and neg_reaction:
                return "ambivalent feelings"
            elif pos_reaction:
                return "a weakness"
            elif neg_reaction:
                return "a disgust"
            else:
                return "no particular reaction"

        def get_day_off(self, day_nb):

            if self.works_today():

                day = calendar.get_weekday()
                charge = self.workdays[day]
                self.workdays[day] = 0
                self.block_schedule = day
                calendar.set_alarm(calendar.time + day_nb, Event(label =  "reset_workday", object = (self, day, charge)))

                return True

            else:
                return False

        def tired_check(self):
            if self.works_today():
                # Tiredness = 5/customer (regular jobs), 10/interaction (whoring)

                if self.job in all_jobs:
                    if self.get_max_cust_served() * 5 >= self.energy:
                        return True
                else:
                    if 10 * self.interactions >= self.energy:
                        return True

            return False

        def cut_upkeep(self, day_nb):

            self.locked_upkeep = self.upkeep
            self.upkeep = 0
            calendar.set_alarm(calendar.time + 1, Event(label = "restore_upkeep", object = self))

        def restore_upkeep(self):
            if self.locked_upkeep:
                self.upkeep = self.locked_upkeep
                self.locked_upkeep = None

        def refresh_spoil_terrify_points(self):

            self.spoil_points = max(self.spoil_points-1, 0)

            if self.spoil_points == 0:
                self.spoiled = False

            self.terrify_points = max(self.terrify_points-1, 0)

            if self.terrify_points == 0:
                self.terrified = False

            return

        def spoil(self, nb):

            self.spoil_points += nb

            if dice(6) + 2 < self.spoil_points:
                self.spoiled = True

            return

        def terrify(self, nb):

            self.terrify_points += nb

            if dice(6) + 2 < self.terrify_points:
                self.terrified = True

            return

        def pop_virginity(self, origin="brothel"):

            for trait in self.traits:
                if trait.name == "Virgin":
                    self.remove_trait(trait)

                    if origin == "brothel":
                        self.add_trait(housebroken_trait, _pos=1, no_perks=True)
                    elif origin == "farm":
                        self.add_trait(farmgirl_trait, _pos=1, no_perks=True)
                    elif origin == "MC" and self.get_love() > self.get_fear():
                        self.add_trait(t_pet_trait, _pos=1, no_perks=True)
                    elif origin == "MC" and self.get_love() <= self.get_fear():
                        self.add_trait(trauma_trait, _pos=1, no_perks=True)
                    elif origin == "rape":
                        self.add_trait(trauma_trait, _pos=1, no_perks=True)
                    elif origin == "chaos":
                        self.add_trait(chaos_trait, _pos=1)

                    return True

            else:
                return False

        def count_occurences(self, context="all", original=False):

            i = 0

            if context == "all":
                mylist = MC.girls + farm.girls + game.free_girls + slavemarket.girls + MC.escaped_girls
                if isinstance(enemy_general, Girl):
                    mylist += [enemy_general]

            elif context == "player":
                mylist = MC.girls + farm.girls + MC.escaped_girls

            for g in mylist:
                if original:
                    if g.original and g.pack_name == self.pack_name:
                        i += 1
                elif g.pack_name == self.pack_name:
                    i += 1

            return i

        def talk_tastes(self, type):

            if type == "likes":
                mylist = ["color", "food", "drink"]
                renpy.random.shuffle(mylist)

                for thing in mylist:
                    if not self.personality_unlock["fav_" + thing]:
                        break
                else:
                    thing = rand_choice(mylist)
                return thing, self.likes[thing]

            elif type == "dislikes":
                mylist = ["color", "food", "drink"]
                renpy.random.shuffle(mylist)

                for thing in mylist:
                    if not self.personality_unlock["dis_" + thing]:
                        break
                else:
                    thing = rand_choice(mylist)
                return thing, self.dislikes[thing]

            elif type == "loves":
                best_replies = []
                all_replies = []

                for k in [k for k, v in self.personality.gift_likes.items() if v >= 3]:
                    if not k in self.personality_unlock["loves"]:
                        best_replies.append(("loves", k))
                    all_replies.append(("loves", k))

                for k in [k for k, v in self.personality.gift_likes.items() if 3 > v >= 0]:
                    if not k in self.personality_unlock["likes"]:
                        best_replies.append(("likes", k))
                    all_replies.append(("likes", k))

                if best_replies:
                    return rand_choice(best_replies)
                elif all_replies:
                    return rand_choice(all_replies)
                else:
                    return "indifferent", False

            elif type == "hates":
                best_replies = []
                all_replies = []

                for k in [k for k, v in self.personality.gift_likes.items() if v <= -2]:
                    if not k in self.personality_unlock["hates"]:
                        best_replies.append(("hates", k))
                    all_replies.append(("hates", k))

                if best_replies:
                    return rand_choice(best_replies)
                elif all_replies:
                    return rand_choice(all_replies)
                else:
                    return "indifferent", False


        def try_to_remove_fix(self, fix_name, type=None):

            if type == "love":
                chance = 40 + (self.mood + self.get_love() - self.get_fear()) // 3
                lock_chance = 0
            elif type == "neutral":
                chance = 40
                lock_chance = 0
            elif type == "fear": # Fear gives a higher bonus and ignores mood but may lock a girl's negative fixation
                chance = 50 + self.get_fear()
                lock_chance = 3

            if dice(100) < lock_chance:
                self.locked_fix.append(fix_name)
                return "locked"

            elif dice(100) < chance:
                self.fix_level[fix_name] += 1

                if self.fix_level[fix_name] < 4:
                    return self.fix_level[fix_name]

                else:
                    self.remove_fixation(fix_name)
                    return "success"

            else:
                return "fail"

        def remove_fixation(self, fix_name):

            for fix in self.pos_fixations:
                _type = "pos"
                if fix.name == fix_name:
                    self.pos_fixations.remove(fix)
                    # Resets farm
                    if fix in farm.knows["pos_fix"][self]:
                        farm.knows["pos_fix"][self].remove(fix)

            for fix in self.neg_fixations:
                _type = "neg"
                if fix.name == fix_name:
                    self.neg_fixations.remove(fix)
                    # Resets farm
                    if fix in farm.knows["neg_fix"][self]:
                        farm.knows["neg_fix"][self].remove(fix)

            self.reset_sex_acts(first=False)

            # Removes fixation preference bonuses/penalties
            for act in fix.acts:
                if type == "pos" and act not in self.pos_acts:
                    self.remove_effects([Effect("change", act + " preferences changes", 25)])
                if type == "neg" and act not in self.neg_acts:
                    self.remove_effects([Effect("change", act + " preferences changes", -50)])

        def has_fixation(self, type="pos", fix_name=None):
            if type == "pos":
                for fix in self.pos_fixations:
                    if fix.name == fix_name:
                        return True

            if type == "neg":
                for fix in self.neg_fixations:
                    if fix.name == fix_name:
                        return True

        def meet_MC(self):
            self.MC_interact = True
            self.track_event("MC met", arg=self.name)
            self.activation_date = calendar.time
            self.talked_to_date = calendar.time


        def pick_dialogue(self, topic): # Picks a random dialogue object that matches the girl's personality

            if topic in self.personality.personality_dialogue_only:
                if dialogue_dict[topic][self.personality.name]:
                    return get_dialogue(topic, self.personality.name)
                else:
                    return Dialogue(event_color["bad"] % topic + " <PERSONALITY DIALOGUE NOT FOUND: " + self.personality.name + ">")

            available_dialogue = []

            # Looks for dialogue tailored to her personality and attributes

            if dialogue_dict[topic][self.personality.name]:
                available_dialogue += [(d, self.personality.dialogue_personality_weight) for d in get_dialogue(topic, self.personality.name)]

            for attr in self.attributes:
                if dialogue_dict[topic][attr]:
                    available_dialogue += [(d, self.personality.dialogue_attribute_weight) for d in get_dialogue(topic, attr)]

            # Looks for dialogue according to her higher stats

            for stat in self.stats + self.sex_stats:
                if dialogue_dict[topic][stat] and self.get_stat(stat) >= 40*self.rank:
                    available_dialogue += [(d, 1) for d in get_dialogue(topic, stat)]

            # Adds generic dialogue if no other dialogue is available

            if not available_dialogue and dialogue_dict[topic]["generic"]:
                available_dialogue += [(d, 1) for d in get_dialogue(topic, "generic")]

            # Sanity check
            available_dialogue = [d for d in available_dialogue if d]

            # Returns randomly picked dialogue

            if not available_dialogue:
                return Dialogue(event_color["bad"] % topic + " <DIALOGUE NOT FOUND>")
            else:
                return weighted_choice(available_dialogue)

        def say(self, topic, custom_label=True, custom_arg=False, nw=False, narrator_mode=False):
            # If custom_label is active, the game will always call _BK.ini's custom_dialogue_label instead of using normal dialogue
            # See Boa Hancock by Goldo for an example of implementation

            if not hasattr(self, "custom_dialogue_label"):
                self.custom_dialogue_label = None

            if custom_label and self.custom_dialogue_label:
                if renpy.has_label(self.custom_dialogue_label):
                    renpy.call(self.custom_dialogue_label, girl=self, topic=topic)
                    return # Probably unnecessary, but better to be safe
                else:
                    renpy.say(event_color["bad"] % "System", "Label: {color=[c_red]}%s{/color} doesn't exist (Custom girl: {color=[c_red]}%s/_BK.ini{/color})." % (self.custom_dialogue_label, self.path))

            dial = self.pick_dialogue(topic)

            dial.apply_changes(self)

            if narrator_mode:
                dial.say(narrator, custom_arg, nw)
            else:
                dial.say(self.char, custom_arg, nw)

        def customer_populations_safety_check(self, current_pop): # Where current_pop is a population name
            for pop, refused in self.refused_populations.items():
                if brothel.get_effect("allow", pop) and not refused:
                    break
            else:
                self.refused_populations[current_pop] = False
                notify("You must activate at least one customer population for this girl.", pic=self.portrait)

            return



#<Chris12 PackState>

####          FILES DICTIONARY FOR B KING                  ####################################################
##   Helper class for girl files and pictures.             ##################################################
##   Saves them in a global variable so that they          ##################################################
##     are only read once without getting saved by Renpy.  ##################################################
##   Also handles packstates.                              ##################################################
##                                                         ##################################################

default preferences.packstate_unrecognized = "Rename"

init -2 python:
    import datetime
    import bisect


    class GirlFilesDict(NoRollback):

        def __init__(self):
            self.__load_files()

        def __load_files(self): # Goldo: Changed to use get_girl_path() to establish the root folder
            start = datetime.datetime.now()
            self.__pathset = set()
            self.__pathtuple = list() # Start with changeable set
            self.__path_dict = defaultdict(str)
            self.__filetuple_dict = dict()
            self.__pictuple_dict = dict()
            self.__ini_dict = dict()
            self.__packstates = list()
            self.__timestamp = datetime.datetime.now()
            self.__totalcount = 0

            for file in renpy.list_files():
                if file.startswith(GirlFilesDict.get_packstate_directory()): # Packstate folder
                    self.__packstates.append(file.lower())
                else: # Other folders
                    girlpack_name, girlpack_path, file_name = get_girl_path(file) # get_girl_path only returns values if it is a confirmed girlpack path

                    if girlpack_name: # get_girl_path may return None if the file is not path is hidden
                        if girlpack_name in self.__pathset: # Controls for duplicate girlpack folders
                            if girlpack_path != self.__path_dict[girlpack_name]:
                                raise AssertionError("Two girl packs with the name '%s' were found:\n%s\n%s\n重命名其中一个以避免冲突。" % (girlpack_name, self.__path_dict[girlpack_name], girlpack_path))
                                renpy.say("", "Exiting Ren'Py...{w=1}{nw}")
                                renpy.quit()

                        else: # __pathset/tuple should be renamed something else since path isn't used anymore
                            self.__pathset.add(girlpack_name)
                            self.__pathtuple.append(girlpack_name)
                            self.__path_dict[girlpack_name] = girlpack_path
                            self.__filetuple_dict[girlpack_name] = list() # Start changeable
                        self.__filetuple_dict[girlpack_name].append(file)
                        if file.endswith("_BK.ini"): self.__ini_dict[girlpack_name] = file
                        self.__totalcount += 1

            # Switch to unchangeable, sorted tuple
            self.__pathtuple.sort()
            self.__pathtuple = tuple(self.__pathtuple)

            for girlpath in self.__pathtuple:
                self.__filetuple_dict[girlpath].sort() # Important! Binary search only works if sorted!
                self.__filetuple_dict[girlpath] = tuple(self.__filetuple_dict[girlpath]) # Switch to unchangeable
                self.__load_pics(girlpath)

            self.__init_duration = datetime.datetime.now() - start

        def __load_pics(self, girlpath): # Where girlpath is the root folder

            # Resetting pictures

            self.__pictuple_dict[girlpath] = list() # Start changeable

            if girlpath not in self.__pathset : return

            # Identifying image files

            imgfiles = [img for img in self.__filetuple_dict[girlpath] if is_imgfile(img)]

            # Creating pictures

            for file in imgfiles:
                pic = Picture(path=file)

                self.__pictuple_dict[girlpath].append(pic)

                # Tracing untagged pics for debugging
                if pic.tags == []:
                    untagged_pics.append(pic.path)

            self.__pictuple_dict[girlpath] = tuple(self.__pictuple_dict[girlpath]) # Switch to unchangeable

        @staticmethod
        # Just to be safe, in case some changes need to be made.
        # The first singleton approach did not work out, since it then got saved by Renpy.
        # (Which made the game use old GirlFilesDicts without updated files & pics)
        def __get():
            #if GirlFilesDict.__singleton is None:
            #    GirlFilesDict.__singleton = GirlFilesDict()
            #return GirlFilesDict.__singleton
            return globalFilesDict

        @staticmethod
        # The directory where the packstates are located in.
        # You only have to change it here.
        # Please make sure it ends with a /
        def get_packstate_directory():
            return "gpackstates/"

        @staticmethod
        # returns the duration of the init.
        # mostly for debugging
        # you can check this in the console with "GirlFilesDict.get_init_duration()"
        def get_init_duration():
            return GirlFilesDict.__get().__init_duration

        @staticmethod
        # returns the total number of files managed by the dictionary
        # mostly for debugging
        # you can check this in the console with "GirlFilesDict.get_totalcount()"
        def get_totalcount():
            return GirlFilesDict.__get().__totalcount

        @staticmethod
        # Returns the _BK.ini for a girlpack, or None if no such file exists
        def get_ini(girlpath):
            try:
                return GirlFilesDict.__get().__ini_dict[girlpath]
            except:
                return None

        @staticmethod
        # Returns the paths of all available girls. Useful for end_of_week stuff.
        def get_paths():
            return GirlFilesDict.__get().__pathtuple

        @staticmethod
        def get_path_dict():
            return GirlFilesDict.__get().__path_dict

        @staticmethod
        # Returns all files for a specific girl.
        # To check if a file exists, use contains_file() instead, it uses a fast binary search.
        def get_files(girlpath):
            return GirlFilesDict.__get().__filetuple_dict[girlpath]

        @staticmethod
        # Looks if a file exists, using fast binary search
        # (Roughly speaking, Binary Search is how you'd look for a name in a phonebook)
        def contains_file(girlpath, file): # Goldo: Changed to use a file's complete path instead.
            instance = GirlFilesDict.__get()
            if girlpath not in instance.__filetuple_dict :
                return False
            else :
                files = instance.__filetuple_dict[girlpath]
                idx = bisect.bisect_left(files, file)
                return idx != len(files) and files[idx] == file

        @staticmethod
        # Gets all pics for a specific girl.
        # Initialized lazy at the first request
        def get_pics(girlpath):
            instance = GirlFilesDict.__get()
            if not girlpath in instance.__pictuple_dict:
                instance.__load_pics(girlpath)
            return instance.__pictuple_dict[girlpath]

        @staticmethod
        # Gets a certain pic for a specific girl. Not using binary search yet.
        # Initialized lazy at the first request
        def get_pic_by_name(girlpath, pic_name):
            pic_name = pic_name.lower()
            instance = GirlFilesDict.__get()
            if not girlpath in instance.__pictuple_dict:
                instance.__load_pics(girlpath)
            for pic in instance.__pictuple_dict[girlpath] :
                if pic.filename == pic_name:
                    return pic
            return None

        @staticmethod # Goldo #
        # The GirlFilesDict timestamp is initialized at Renpy startup
        # Used by AutoRepair to check if there could be new images
        def reload_files():
            GirlFilesDict.__get().__load_files()

        @staticmethod
        # The GirlFilesDict timestamp is initialized at Renpy startup
        # Used by AutoRepair to check if there could be new images
        def get_timestamp():
            instance = GirlFilesDict.__get()
            return instance.__timestamp

        @staticmethod
        # Imports packstates for all girls
        # If simulate = True, only creates a logfile without any renames
        def import_packstates(simulate = False):
            all_results = list()
            total_changes = 0

            for girlpack_name in GirlFilesDict.__get().get_paths():
                result, changes = GirlFilesDict.__import_tags(girlpack_name, simulate)
                renpy.say("Checking", girlpack_name + "{fast}{nw}")
                all_results.append(result)
                total_changes += changes

            with open(config.gamedir + "\\packstate_log.txt", "wt") as log_file :
                log_file.write("\n".join(all_results))

            if (total_changes > 0) :
                if simulate :
                    GirlFilesDict.__get().__load_files() # Revert tags
                    renpy.say("", str(total_changes) + " file(s) would be renamed. See {a=call_in_new_context:invoke_packstate_log}{color=[c_magenta]}packstate_log.txt{/color}{/a} in the 'game' directory for details.")
                else :
                    renpy.say("", str(total_changes) + " file(s) were renamed. See {a=call_in_new_context:invoke_packstate_log}{color=[c_magenta]}packstate_log.txt{/color}{/a} for details.\nRestarting Renpy. This may take a few seconds.{fast}{nw}")
                    renpy.utter_restart()
            else :
                renpy.say("", "No files were renamed. See {a=call_in_new_context:invoke_packstate_log}{color=[c_magenta]}packstate_log.txt{/color}{/a} for details.")

        @staticmethod
        # The workhorse of the packstates import
        def __import_tags(girlpack_name, simulate):

            packStateFilePath = GirlFilesDict.get_packstate_directory() + girlpack_name + ".txt" #?

            if packStateFilePath.lower() not in GirlFilesDict.__get().__packstates :
                return (girlpack_name + ": No packstate\n", 0)

            counterChanges = 0
            try :
                with open(config.gamedir + "/" + packStateFilePath, "r") as packStateFile :
                    import_result = ""
                    counterImageStates = 0
                    counterFileChecked = 0
                    counterDuplicates = 0
                    all_renames = list()


                    groupedBySize = dict()
                    # trash needs to come last, or the duplicates would alternate every time
                    for skip_trash in (True, False) :
                        for pic in GirlFilesDict.get_pics(girlpack_name) :
                            if pic.is_trash == skip_trash : continue
                            filesize = pic.get_filesize()
                            if filesize in groupedBySize:
                                groupedBySize[filesize].append(pic)
                            else:
                                groupedBySize[filesize] = [ pic ]
                            pic.is_unrecognized = True

                    filesize = packStateFile.readline()
                    while (len(filesize) != 0) :
                        filesize = int(filesize.strip())
                        hash = packStateFile.readline().strip()
                        tag_filename = packStateFile.readline().strip().lower()
                        tagsSet = set(tag_filename.split())
                        alreadyFound = False
                        counterImageStates += 1
                        if filesize in groupedBySize:
                            for pic in groupedBySize[filesize] :
                                duplicateCheck = (len(groupedBySize[filesize]) > 1)

                                # use set to make the check indifferent to tag order
                                picNeedsRenaming = (set(pic.filename[:pic.filename.find("(")].lower().split()) != tagsSet)
                                if (duplicateCheck or picNeedsRenaming) :
                                    # only get the hash if there are potential duplicates or if the image would need renaming
                                    if (pic.get_hash() == hash) :
                                        pic.is_unrecognized = False
                                        counterFileChecked += 1
                                        if alreadyFound :
                                            counterDuplicates += 1

                                        if picNeedsRenaming or alreadyFound :
                                            pic.is_trash = alreadyFound or tag_filename.startswith("_trash")
                                            pic.oldtags = [] # using oldtags, refresh them later
                                            if alreadyFound : pic.oldtags.append("duplicate")
                                            for tag in tag_filename.split() :
                                                if tag != "_trash" : pic.oldtags.append(tag)

                                            new_name = pic.get_new_name()
                                            if pic.filename[:pic.filename.find("(")] != new_name[:new_name.find("(")]:
                                                counterChanges += 1
                                                if simulate :
                                                    all_renames.append(pic.filename + " -> " + new_name)
                                                else :
                                                    old_filename = pic.filename
                                                    pic.commit_changes()
                                                    all_renames.append(old_filename + " -> " + pic.filename)
                                            pic.make_tags_from_filename() # refresh tags

                                        alreadyFound = True

                                else :
                                    # This part does not rely on the hash for performance reasons
                                    # If both filesize and tags matched, it's reasonably safe to assume that it is the correct image.
                                    # Otherwise, you'd have to calculate the hashes of ALL files EVERY TIME.
                                    pic.is_unrecognized = False

                        filesize = packStateFile.readline()

                counterUnrecognized = 0
                for pic in GirlFilesDict.get_pics(girlpack_name) :
                    if pic.is_unrecognized :
                        if pic.filename.lower().startswith("_untagged") :
                            continue # no need for "_UNRECOGNIZED _UNTAGGED"

                        counterFileChecked += 1
                        new_name = pic.get_new_name()
                        if pic.filename[:pic.filename.find("(")] != new_name[:new_name.find("(")]:
                            counterChanges += 1
                            if simulate :
                                all_renames.append(pic.filename + " -> " + new_name)
                            else :
                                old_filename = pic.filename
                                pic.commit_changes()
                                all_renames.append(old_filename + " -> " + pic.filename)
                            pic.make_tags_from_filename() # refresh tags
                            counterUnrecognized += 1

                import_result = girlpack_name + ": packstate contained " + str(counterImageStates) + " image states.\n"

                if counterFileChecked > 0 :
                    import_result += "  " + str(counterFileChecked) + " file(s) needed to be checked, "
                    if counterChanges > 0:
                        import_result += "and " + str(counterChanges) + " were renamed.\n"
                    else :
                        import_result += "but none had to be changed. Everything's up to date.\n"

                    if counterDuplicates > 0 :
                        import_result += "  Of those, " + str(counterDuplicates) + " were duplicates and marked for deletion (tagged as _TRASH).\n"
                    if counterUnrecognized > 0 :
                        import_result += "  " + str(counterUnrecognized) + " were unrecognized. Those images will be used depending on your game settings.\n"
                    if counterChanges > 0 :
                        import_result += "    " + "\n    ".join(all_renames)
                else :
                    import_result += "  No files were found that had to be changed. Everything's up to date.\n"

            except IOError as e:
                errno, strerror = e.args
                import_result = "I/O error({0}): {1}".format(errno, strerror)
                pass
            except :
                raise
            return (import_result, counterChanges)

    # Global Object Initialized in Python Init -> skips renpy save process
    # So it will always have the newest files when you restart the game
    globalFilesDict = GirlFilesDict()

#</Chris12 PackState>

#### END OF BK GIRLCLASS FILE ####
