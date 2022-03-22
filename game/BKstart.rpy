######         BRO KING          ######

## The game starts here. ##

label start:

    stop music fadeout 3.0

    $ debug_mode = False
    $ starting_chapter = 1
    $ enemy_general = None
    $ extras_dict = {"farm" : False, "carpenter" : False, "locations" : False, "shops" : False, "trainers" : False, "resources" : False}
    $ c1_path = "good" # Only used for custom starts

    scene black with fade

    if persistent.seen_intro is None:
        jump intro

    elif debug:
        menu:
            "Choose a starting mode"

            "Normal mode - See intro":
                jump intro

            "Normal mode - No intro":
                pass

            "Debug mode - Fast":
                $ persistent.active_mix = "default"
                $ debug_mode = "quick"

            "Debug mode - Custom":
                $ debug_mode = "custom"

    else:
        menu:
            "Would you like to see the intro?"

            "Yes":
                jump intro

            "No":
                pass

    jump quick_start

# label choose_mix():

#     # Sanity check
#     python:
#         available_mixes = persistent.girl_mix.keys()

#         for mix in persistent.game_mixes:
#             if mix not in available_mixes:
#                 renpy.notify("Removing %s from game mixes" % mix)
#                 persistent.game_mixes.remove(mix)

#     # Choose girl mixes if several are available

#     if len(available_mixes) > 1:
#          # $ persistent.game_mixes.append(long_menu("{size=-4}Choose a girl mix to use for this game.\n{b}Warning{/b}: You will not be able to switch to a different girl mix after starting the game).{/size}", [(mix.capitalize(), mix) for mix in persistent.girl_mix.keys()]))

#          $ confirm = False

#          while not confirm:
#              $ text1 = and_text(persistent.game_mixes)

#              menu:
#                 "The following girl mixes will be used in the game: [text1]"

#                 "Add mix" if len(available_mixes) > len(persistent.game_mixes):
#                      $ persistent.game_mixes.append(long_menu("{size=-4}Choose a girl mix to use for this game.\n{b}Warning{/b}: You will not be able to switch to a different girl mix after starting the game).{/size}", [(mix.capitalize(), mix) for mix in available_mixes if mix not in persistent.game_mixes]))

#                 "Clear all mixes" if len(persistent.game_mixes) > 0:
#                      $ persistent.game_mixes = []

#                 "START" if len(persistent.game_mixes) > 0:
#                      $ confirm = True
#     else:
#         $ persistent.game_mixes = ["default"]

#     return

label quick_start:

    call init_game() from _call_init_game

    $ main_firstvisit = False
    $ district_firstvisit = False
    $ brothel_firstvisit = False
    $ shop_firstvisit = False
    $ slavemarket_firstvisit = False
    $ girls_firstvisit = False
    $ postings_firstvisit = False
    $ farm_firstvisit = True

    if debug_mode != "quick":
        call choose_difficulty() from _call_choose_difficulty

    else:
        $ MC.set_playerclass("Wizard")
        $ MC.girls = get_girls(24)
        $ MC.gold = 100000
        $ MC.speed = 30
        $ MC.reset_interactions()

        python:
            for room in brothel.rooms.values():
                room.buy(forced=True)

        $ farm_firstvisit = False
        $ farm.active = True
        $ gizel_name = "Gizel"
        $ story_flags["found wagon"] = True
        $ story_flags["met carpenter"] = True

        # # SET UP CALENDAR
        # $ calendar.updates()

    # Create enemy general for the siege security event

    if dice(2) == 1:
        $ enemy_general = get_girls(1, free=True, p_traits=["Warrior"])[0]
    else:
        $ enemy_general = get_girls(1, free=True, p_traits=["Caster"])[0]
    $ enemy_general.love = -50

    if starting_chapter > 1:
        call debug_load_chapter(starting_chapter) from _call_debug_load_chapter

#     elif debug_mode == "custom":

#         $ starting_girls = 0
#         $ events_on = False

#         label debug_custom_menu():

#             menu:
#                 "Choose starting game options"

#                 "Debug mode - ON" if debug_mode:
#                     $ debug_mode = False
#                     jump debug_custom_menu

#                 "Debug mode - OFF" if not debug_mode:
#                     $ debug_mode = "custom"
#                     jump debug_custom_menu

#                 "Starting chapter - [starting_chapter]":
#                     $ starting_chapter = int(renpy.input("Which chapter do you want to start at?", default=str(starting_chapter)))
#                     jump debug_custom_menu

#                 "Starting girls - [starting_girls]":
#                     $ starting_girls = int(renpy.input("How many girls do you want to start with?", default=str(starting_girls)))
#                     jump debug_custom_menu

#                 "Starting gold - [MC.gold]":
#                     $ MC.gold = int(renpy.input("How much gold do you want to start with?", default=str(MC.gold)))
#                     jump debug_custom_menu

#                 "Starting stats - Str. [MC.strength] / Spi. [MC.spirit] / Cha. [MC.charisma] / Spd [MC.speed]":
#                     $ MC.strength = int(renpy.input("Choose player's Strength", default=str(MC.strength)))
#                     $ MC.spirit = int(renpy.input("Choose player's Spirit", default=str(MC.spirit)))
#                     $ MC.charisma = int(renpy.input("Choose player's Charisma", default=str(MC.charisma)))
#                     $ MC.speed = int(renpy.input("Choose player's Speed", default=str(MC.speed)))
#                     jump debug_custom_menu

#                 "Events on - [events_on]":
#                     $ events_on = not events_on
#                     jump debug_custom_menu

#                 "Farm active - [farm.active]":
#                     $ farm.active = not farm.active
#                     jump debug_custom_menu

#                 "START":
#                     if events_on:
#                         call init_events() from _call_init_events

#                     if starting_chapter > 1:
#                         call debug_load_chapter(starting_chapter) from _call_debug_load_chapter_1

#                     $ MC.reset_interactions()
#                     $ MC.girls = get_girls(starting_girls)


    call chapter(starting_chapter, forced=True) from _call_chapter_1

    # SET UP CALENDAR
    $ calendar.updates()

    if debug_mode != "quick" and starting_chapter in (1, 6):

        menu:
            "What will you use as a front for your business?"

            "A tavern":
                $ brothel.add_room("tavern", forced=True)

            "A club":
                $ brothel.add_room("club", forced=True)

            "A bath house":
                $ brothel.add_room("onsen", forced=True)

            "An okiya (geisha house)":
                $ brothel.add_room("okiya", forced=True)

        $ brothel.free_room = False

    jump main



label init_game():

    scene black
    centered "Loading...{nw}"

    python:

    #### GAME ####

        game = Game()
        calendar = Calendar()

        # CHEATS #

        if persistent.cheats:
            game.activate_cheats()

        # STORY #

        logs = defaultdict(bool)
        story_flags = defaultdict(bool)
        city_events = []
        daily_events = [StoryEvent("random_night_events", type="night", chance=0.1, once=False, date=6),
                        StoryEvent("random_morning_events", type="morning", chance=0.2, once=False, date=6),
                        ] # Contains conditional night or morning events (not alarms)
        night_checks = [] # Used for custom lists [girl, label] that will be checked every night (currently only girls with a customized _BK.ini file)
        story_gossip = [] # Stores story-specific and custom gossip (permanent)
        temp_gossip = [] # Stores story-specific and custom gossip (cleared at the end of each chapter)

        # HELP FLAGS #

        help_tips = defaultdict(bool)
        help_tips["whore"] = True

        # FIRST TIME FLAGS #

        main_firstvisit = True
        district_firstvisit = True
        brothel_firstvisit = True
        shop_firstvisit = True
        slavemarket_firstvisit = True
        girls_firstvisit = True
        postings_firstvisit = True
        farm_firstvisit = True
        carpenter_active = False

        # UNIQUE IDS #

        girl_id_generated = 0
        minion_id_generated = defaultdict(int)

        # CUSTOM VARIABLE #

        last_set_duration = 3 # Used for the farm
        autorest_limit = 0 # Used for autorest (0 = deactivated)

    #### MAIN CHARACTER ####

        # CREATE MC #

        MC_name = "Nero"
        MC = Main()
        MC.char = you

        MC.challenges = {
                        "fight" : MC_challenge("Fight", stat="strength", opposed=True), # xxx
                        "force" : MC_challenge("Force", stat="strength", opposed=False), # xxx
                        "stamina" : MC_challenge("Stamina", stat="strength", opposed=False), # xx

                        "cast" : MC_challenge("Cast Spell", stat="spirit", opposed=False), # xxx
                        "control" : MC_challenge("Control", stat="spirit", opposed=True), # xxx
                        "detect" : MC_challenge("Detect Magic", stat="spirit", opposed=False), # xx

                        "rally" : MC_challenge("Rally", stat="charisma", opposed=False), # xxx
                        "charm" : MC_challenge("Charm", stat="charisma", opposed=False), # xxx
                        "bluff" : MC_challenge("Bluff", stat="charisma", opposed=True), # xx

                        "speed" : MC_challenge("Speed", stat="speed", opposed=False),
                        }


    #### NPCs #### Declare unique NPCs


        # DEFAULT NAMES #

        sill_name = "西里尔"
        kuro_name = "公主"
        maid_name = "美奈子"
        gio_fucked_sill = ""
        kosmo_name = "奇怪的人"
        sergeant_name = "女人"
        captain_name = "法拉上尉"
        lieutenant_name = "中尉"
        maya_name = "女人"
        maya_love = 0
        renza_name = "女人"
        satella_name = "女孩"
        shalia_name = "声音"
        mask_name = "阴影"
        gizel_name = "精灵女孩"
        stella_name = "女奴"
        goldie_name = "戈尔迪"
        willow_name = "奇怪的女孩"
        gina_name = "女孩"
        carpenter_name = "女人"
        bast_name = "商店女孩"
        banker_name = "神秘女郎"
        riche_name = "甜美女孩"
        ramias_name = "女强人"
        gurigura_name = "野性女孩"
        katryn_name = "书呆子女孩"
        today_name = "快乐的裁缝"
        yesterday_name = "安静的裁缝"
        jobgirl_name = "自由职业者"
        kenshin_name = "女骑士"
        homura_name = "高贵的女士"
        suzume_name = "蓝发女孩"
        taxgirl_name = "优雅的女士"
        narika_name = "娇小的忍者"
        mizuki_name = "优雅的忍者"
        haruka_name = "强壮的忍者"

        # NPC OBJECTS / TRAINERS #

        NPC_sill = NPC(name = "Sill", trainer_portrait = "side sill happy", trainer_description = "'{i}又一块精斑？ *叹气* 带我去吧。{/i}'\n\n{b}管理人{/b}\n每晚随机免除一位女孩的抚养费。", effects = Effect("special", "free upkeep", 1, scope = "brothel"))
        NPC_sad_sill = NPC(name = "Sad Sill", trainer_portrait = "side sill sad", trainer_description = "bla", effects = Effect("change", "charm", 40, scope = "brothel"))
        NPC_gio = NPC()
        NPC_kosmo = NPC()
        NPC_sergeant = NPC()
        NPC_roz = NPC(name = "Roz", char = roz)
        NPC_maya = NPC(name = "Maya", trainer_portrait = "side maya", trainer_description = "'{i}我最好检查一下周边的情况。再来。{/i}'\n\n{b}永远警惕{/b}\n对青楼的危险增长速度减慢33%。", effects = Effect("boost", "threat build up", -0.33, scope = "brothel"))
        NPC_renza = NPC(name = "Renza", trainer_portrait = "side renza", trainer_description = "'{i}他的钱包似乎很重。让我来帮你...{/i}'\n\n{b}巧妙手法{/b}\n所有女孩都会扒口袋。有{i}机灵{/i}特质的女孩永远不会被抓。", effects = Effect("special", "pickpocket", 1, scope = "brothel"))
        NPC_satella = NPC(name = "Satella", trainer_portrait = "side satella", trainer_description = "'{i}在阴暗处玩耍不是很有趣吗？库呼呼...{/i}'\n\n{b}暗黑祭司{/b}\n恐惧增加得更快。", effects = Effect("boost", "fear gains", 1, scope = "world"))
        NPC_captain = NPC(name = "Farah", trainer_portrait = "side captain", trainer_description = "'{i}如果你想上位，你必须准备好做任何事情。任何事情!{/i}'\n\n{b}伤风败俗{/b}\n女孩会更快地习惯肛门和变态行为。", effects = (Effect("change", "anal preferences changes", 25, scope = "brothel"), Effect("change", "fetish preferences changes", 25, scope = "brothel")))
        NPC_lieutenant = NPC(name = "Lydie", trainer_portrait = "side lieutenant", trainer_description = "'{i}你想让我给你做个榜样吗？我不这么认为。{/i}'\n\n{b}严苛纪律{/b}\n女孩不太可能拒绝工作。", effects = Effect("boost", "obedience tests", 0.1, scope = "brothel"))
        NPC_gizel = NPC(name = "Gizel", defense = 3, trainer_portrait = "side gizel", trainer_description = "", effects = None)
        NPC_banker = NPC(name = "Banker", trainer_portrait = "side banker")
        NPC_riche = NPC(name = "Riche", char=riche, trainer_portrait = "side riche", item_types=["Flower"])
        NPC_ramias = NPC(name = "Ramias", char=ramias, trainer_portrait = "side ramias", item_types=["Weapon"], trainer_description = "'{i}用尖尖的那头扎向他们！{/i}'\n\n{b}武术训练{/b}\n所有女孩都得到了 +2 的个人防御。", effects = Effect("change", "defense", 2, scope = "brothel"))
        NPC_gurigura = NPC(name = "Gurigura", char=gurigura, trainer_portrait = "side gurigura", item_types=["Toy", "Food", "Supplies"])
        NPC_katryn = NPC(name = "Katryn", char=katryn, trainer_portrait = "side katryn", item_types=["Ring", "Necklace"])
        NPC_giftgirl = NPC(name = "Gift Shop Girl", char=giftgirl, trainer_portrait = "side giftgirl", item_types=["Gift", "Misc"])
        NPC_twins = NPC(name = "Today", char=today, trainer_portrait = "side today", item_types=["Dress", "Accessory"])
        NPC_stella = NPC(name="Stella", char=stella, trainer_portrait = "side stella", minion_type="stallion", trainer_description = "'{i}你薄弱的训练技术无法与血岛相比。{/i}'\n\n{b}精耕细作{/b}\n提高了所有农场性训练的效率。", effects = Effect("boost", "farm sexual training", 0.5, scope = "farm"))
        NPC_goldie = NPC(name="Goldie", char=goldie, trainer_portrait = "side goldie", minion_type="beast", trainer_description = "'{i}我在一本书上读到过... *脸红*{/i}'\n\n{b}技术{/b}\n女孩会更快地习惯服务和性行为。", effects = (Effect("change", "service preferences changes", 25, scope = "brothel"), Effect("change", "sex preferences changes", 25, scope = "brothel")))
        NPC_willow = NPC(name="Willow", char=willow, minion_type="monster")
        NPC_gina = NPC(name="Gina", char=gina, minion_type="machine")
        NPC_bast = NPC(name="Bast", char=bast, trainer_portrait = "side bast", trainer_description = "'{i}金币只是可以在Zan交易的众多资源中的一种。{/i}'\n\n{b}资源丰富{/b}\n你的青楼的部分收入被转换为随机资源。", effects = [Effect("special", "resources as income", 1.0, scope = "brothel"), Effect("boost", "income", -0.2, scope = "brothel")])
        NPC_jobgirl = NPC(name="Scarlet", char=jobgirl)
        NPC_kuro = NPC(name="Kurohime", char=kuro)
        NPC_homura = NPC(name="Homura", char=homura)
        NPC_taxgirl = NPC(name="Taxgirl", char=taxgirl, trainer_portrait = "side taxgirl", trainer_description = "'{i}只需支出龙虾和香槟酒......再给我一些。{/i}'\n\n{b}偷税漏税{/b}\n每晚为你的部分收入提供免税保护。", effects = [Effect("boost", "taxable net income", -0.05, scope = "brothel")])

        # Chapter 2 Kunoichi
        NPC_narika = NPC(name="Narika", char=narika)
        NPC_mizuki = NPC(name="Mizuki", char=mizuki)
        NPC_haruka = NPC(name="Haruka", char=haruka)

        NPC_iulia = NPC(name="Iulia", char=carpenter)
        NPC_freak = NPC(name="Papa Freak", char=papa)
        NPC_kenshin = NPC(name="Lady Kenshin", char=kenshin)

        MC.trainers.append(NPC_sill)
        MC.current_trainer = NPC_sill

        if debug_mode:
            MC.trainers.append(NPC_maya)
            MC.trainers.append(NPC_lieutenant)
            MC.trainers.append(NPC_captain)
            MC.trainers.append(NPC_renza)
            MC.trainers.append(NPC_satella)
            MC.trainers.append(NPC_bast)
            MC.trainers.append(NPC_stella)
#            MC.trainers.append(NPC_sad_sill)


    #### BROTHELS ####

    # Bro cost and capacity are set in BKsettings.rpy for ease of access by casual players

        blist = {
                1 : Brothel(1, 1, upgrades = [1, 3], max_rep = 120, max_help = 8),
                2 : Brothel(2, 2, [2, 5], max_rep = 1150, max_help = 16),
                3 : Brothel(2, 3, [3, 6], max_rep = 1800, max_help = 24),
                4 : Brothel(3, 4, [3, 8], max_rep = 5800, max_help = 32),
                5 : Brothel(3, 5, [4, 9], max_rep = 8000, max_help = 40),
                6 : Brothel(4, 6, [5, 11], max_rep = 18500, max_help = 48),
                7 : Brothel(5, 7, [6, 12], max_rep = 33750, max_help = 64),
                }

    # CREATE FIRST BROTHEL

        brothel = blist[1]
        brothel.setup("The Rose Garden", furniture=[])
        old_brothel_auction_price = 0
        old_brothel_name = "The Rose Garden"


    #### FARM ####

        farm_installations = {
                              "stables" : Installation(name = "stables", pic = "stables.jpg", tags = ["big"], minions = [Minion("stallion", name="Bob")], minion_type = "stallion", skill = "libido", rank = 1),
                              "pig stall" : Installation(name = "pig stall", pic = "pig stall.jpg", tags = ["beast"], minion_type = "beast", skill = "obedience"),
                              "monster den" : Installation(name = "monster den", pic = "monster den.jpg", tags = ["monster"], minion_type = "monster", skill = "constitution"),
                              "workshop" : Installation(name = "workshop", pic = "workshop.jpg", tags = ["machine", "toy"], minion_type = "machine", skill = "sensitivity"),
                              }
        farm = Farm()


    #### DISTRICTS ####
    python:

        # POPULATIONS #

        beggar = Population("beggars", "beggar.webp", diff = 15, range = 10, rank=1, weight=5, base_description="这是一群极其粗俗、要求不高的顾客。毕竟，乞丐不能挑肥拣瘦。")
        thug = Population("thugs", "thug.webp", diff = 20, range = 10, rank=1, weight=3, effects=[Effect("boost", "crazy", 1)], base_description="暴徒生活伴随着它的兄弟和妓女。你是那个得到妓女的兄弟。")
        laborer = Population("laborers", "laborer.webp", 30, range = 20, rank=1, weight=2, base_description="世界上的工人们，团结起来! 或者，你知道的，找一个女孩过夜。")

        sailor = Population("sailors", "sailor.webp", 40, range = 20, rank=2, effects=[Effect("change", "waitress preference", 15), Effect("change", "anal preference", 15)], base_description="水手们上岸后是出了名的好色。经过长时间的航行，海员们需要放松一下。")
        commoner = Population("commoners", "commoner.webp", 50, range = 20, rank=2, effects=[Effect("change", "dancer preference", 15), Effect("change", "service preference", 15)], base_description="平民在每个方面都是令人沮丧的平凡。平凡的生活，平凡的工作，平凡的妻子...看到一个平民试图在妓院里逃避这一切，是......常见的。")

        craftsman = Population("craftsmen", "craftsman.webp", 70, range = 30, rank=2, effects=[Effect("special", "horny", 1)], base_description="工匠们用他们的双手工作，当他们的手不安分时，他们喜欢把它们放在一个漂亮女孩身上。工匠们都很狡猾。")

        bourgeois = Population("bourgeois", "bourgeois.webp", 90, range = 30, rank=3, effects=[Effect("change", "geisha preference", 15), Effect("change", "sex preference", 15)], base_description="什么时候“打倒资产阶级”变成了“达到资产阶级”？你出卖了自己，伙计。")
        guildmember = Population("guild members", "guild member.webp", 110, range = 30, rank=3, effects=[Effect("change", "masseuse preference", 15), Effect("change", "fetish preference", 15)], base_description="公会成员就像工匠，但更狡猾。")

        patrician = Population("patricians", "patrician.webp", 110, range = 40, rank=3, effects=[Effect("special", "horny", 1), Effect("change", "satisfaction", -1)], base_description="神父在社区中扮演着重要角色, 随时准备好与有恋父情节的年轻女孩见面。")

        aristocrat = Population("aristocrats", "aristocrat.webp", 135, range = 40, rank=4, effects=[Effect("boost", "crazy", 1.5), Effect("change", "satisfaction", -1)], base_description="凌驾于法律之上。名符其实的富人。富得流油。有什么不喜欢的呢？")
        noble = Population("nobles", "noble.webp", 160, range = 40, rank=4, effects=[Effect("change", "satisfaction", -2)], base_description="贵族们很容易感到无聊。享有特权的生活并不全是乐趣和游戏，他们也会无聊。")

        royal = Population("royals", "royal.webp", 200, range = 50, rank=5, effects=[Effect("change", "satisfaction", -3)], base_description="人们说，皇室成员都是颓废的、不配自恋的寄生虫。没有人因为他们对臣民的钱财如此慷慨而信任他们。悲哀。")

        all_populations = [beggar, thug, laborer, sailor, commoner, craftsman, bourgeois, guildmember, patrician, aristocrat, noble, royal]

        # LOCATIONS # Locations should have been in a dictionary from the start, but it's messy. Sorry.

        spice_market = Location("Spice market", pic = "Spice market.jpg")
        sewers = Location("Sewers", pic = "Sewers.webp", menu = ("访问怪物捕手", "visit_willow"), menu_costs_AP=False) # Monster merchant
        farmland = Location("Farm", pic = "farmland.jpg", menu = ("访问牧场主人", "visit_goldie"), menu_costs_AP=False) # Beast merchant
        watchtower = Location("Watchtower", pic = "Watchtower.jpg", menu = ("访问队长的地下室", "visit_watchtower"))
        junkyard = Location("Junkyard", pic = "Junkyard.webp", menu = ("访问科学家", "visit_gina"), menu_costs_AP=False) # Machine merchant
        thieves_guild = Location("Thieves guild", pic = "Thieves guild.jpg", secret = True, menu = ("访问公会仓库", "visit_thieves_guild"))

        harbor = Location("Harbor", pic = "Harbor.jpg", menu = ("访问种马贩子", "visit_stella"), menu_costs_AP=False) # Stallion merchant
        shipyard = Location("Shipyard", pic = "Shipyard.jpg", menu = ("收集木材", "collect_wood")) # Wood extraction
        taverns = Location("Taverns", pic = "Taverns.jpg")
        seafront = Location("Seafront", pic = "Seafront.jpg", menu = ("访问Papa Freak", "visit_papa"), menu_costs_AP=False)
        beach = Location("Beach", pic = "Beach.jpg", menu = ("酿造染料", "collect_dye")) # Dye
        exotic_emporium = Location("Exotic emporium", pic = "Exotic emporium.jpg", menu = ("访问礼品店", "visit_giftgirl"), menu_costs_AP=False) # Gift girl, gifts

        stables = Location("Stables", pic = "Stables.jpg", menu = ("获取皮革", "collect_leather")) # Leather
        plaza = Location("Plaza", pic = "Plaza.jpg", menu = ("联系Homura", "c3_contact_homura"), menu_costs_AP=False) # Homura, story
        market = Location("Market", pic = "Market.jpg", menu = ("访问交换所", "visit_exchange"), action=True, menu_costs_AP=False) # Resource market
        gallows = Location("Gallows", pic = "Gallows.jpg", menu = ("访问Papa Freak", "visit_papa"), menu_costs_AP=False)
        prison = Location("Prison", pic = "Prison.jpg", menu = ("访问G的集市", "visit_gurigura"), menu_costs_AP=False) # Gurigura, toys
        arena = Location("Arena", pic = "Arena.jpg", menu = ("访问武器店", "visit_ramias"), menu_costs_AP=False) # Ramias, weapons

        botanical_garden = Location("Botanical garden", pic = "Botanical garden.jpg", menu = ("访问花摊", "visit_riche"), menu_costs_AP=False) # Riche, flowers
        hanging_gardens = Location("Hanging gardens", pic = "Hanging gardens.jpg", menu = ("织造丝绸", "collect_silk")) # Silk
        library = Location("Library", pic = "Library.jpg", menu = ("访问饰品店", "visit_katryn"), menu_costs_AP=False) # Katryn, trinkets
        guild_quarter = Location("Guild quarter", pic = "Guild quarter.jpg", menu = ("走私矿石", "collect_ore")) # Ore
        magic_guild = Location("Magic guild", pic = "Magic guild.jpg")
        magic_forest = Location("Magic forest", pic = "Magic forest.jpg")

        pilgrim_road = Location("Pilgrim road", pic = "Pilgrim road.jpg", menu = ("访问裁缝店", "visit_twins"), menu_costs_AP=False) # Twins, dresses
        banking_quarter = Location("Banking quarter", pic = "Banking quarter.jpg", menu = ("访问银行", "visit_bank"), action=True, menu_costs_AP=False)
        old_ruins = Location("Old ruins", pic = "Ruins.webp", menu = ("开采大理石", "collect_marble")) # Marble
        lake = Location("Lakefront", pic = "Lake.jpg")
        training_ground = Location("Training ground", pic = "Training ground.jpg")
        cathedra = Location("Cathedra", pic = "Cathedra.jpg")

        battlements = Location("Battlements", pic = "Battlements.jpg")
        keep = Location("Keep", pic = "Keep.jpg")
        hall = Location("Hall", pic = "Hall.jpg")
        courtyard = Location("Courtyard", pic = "Courtyard.jpg")
        temple = Location("Temple", pic = "Temple.webp")
        falls = Location("Waterfalls", pic = "Falls.webp", menu = ("寻找钻石", "collect_diamond")) # Diamonds

        location_dict = {# Districts
                        "The Slums" : [spice_market, sewers, farmland, watchtower, junkyard, thieves_guild],
                        "The Docks" : [harbor, shipyard, seafront, beach, taverns, exotic_emporium],
                        "The Warehouse" : [market, stables, plaza, gallows, prison, arena],
                        "The Magic Gardens" : [botanical_garden, library, magic_forest, hanging_gardens, guild_quarter, magic_guild],
                        "The Cathedra" : [pilgrim_road, banking_quarter, old_ruins, lake, training_ground, cathedra],
                        "The King's Hold" : [battlements, keep, hall, courtyard, temple, falls],

                        # Locations (for easy reference)
                        "Spice market" : spice_market,
                        "Sewers" : sewers,
                        "Farm" : farmland,
                        "Watchtower" : watchtower,
                        "Junkyard" : junkyard,
                        "Thieves guild" : thieves_guild,

                        "Harbor" : harbor,
                        "Shipyard" : shipyard,
                        "Seafront" : seafront,
                        "Beach" : beach,
                        "Taverns" : taverns,
                        "Exotic emporium" : exotic_emporium,

                        "Market" : market,
                        "Stables" : stables,
                        "Plaza" : plaza,
                        "Gallows" : gallows,
                        "Prison" : prison,
                        "Arena" : arena,

                        "Botanical garden" : botanical_garden,
                        "Library" : library,
                        "Magic forest" : magic_forest,
                        "Hanging gardens" : hanging_gardens,
                        "Guild quarter" : guild_quarter,
                        "Magic guild" : magic_guild,

                        "Pilgrim road": pilgrim_road,
                        "Banking quarter" : banking_quarter,
                        "Old ruins" : old_ruins,
                        "Lakefront" : lake,
                        "Training ground" : training_ground,
                        "Cathedra" : cathedra,

                        "Battlements" : battlements,
                        "Keep" : keep,
                        "Hall" : hall,
                        "Courtyard" : courtyard,
                        "Temple" : temple,
                        "Waterfalls" : falls,
                         }

        town_locations = ["spice market", "taverns", "market", "plaza", "guild quarter", "pilgrim road", "banking quarter"]

        beach_locations = ["beach", "seafront", "lakefront", "waterfalls"]

        nature_locations = ["farm", "botanical garden", "magic forest", "hanging gardens", "old ruins", "courtyard"]

        court_locations = ["library", "magic guild", "cathedra", "keep", "hall", "temple"]

        all_locations = location_dict["The Slums"] + location_dict["The Docks"] + location_dict["The Warehouse"] + location_dict["The Magic Gardens"] + location_dict["The Cathedra"] + location_dict["The King's Hold"]


        if debug_mode:
            harbor.action = True
            farmland.action = True
            sewers.action = True
            junkyard.action = True
            thieves_guild.secret = False
            thieves_guild.action = True

            shipyard.action = True
            stables.action = True
            beach.action = True
            old_ruins.action = True
            hanging_gardens.action = True
            guild_quarter.action = True
            falls.action = True


        # DISTRICT LIST #

        district_dict = {"slum" : District("The Slums", 1, 1, 15, ((beggar, 50), (thug, 30), (laborer, 20)), pic = "districts/slums.jpg", description = "贫民窟位于Zan城墙外的郊区，。这里是诸多乌合之众的家园：移民、难民、贫民、香料瘾君子......据传闻，这里也是盗贼公会的藏身之处，他们崇拜影子女神莎莉娅。"),
                 "docks" : District("The Docks", 2, 2, 40, ((laborer, 10), (sailor, 40), (commoner, 30), (craftsman, 20)), room = ["tavern"], pic = "districts/docks.jpg", description = "码头是粗暴的水手和躲避险恶的大海的狡猾海盗的家园。周围徘徊的全是海员，难怪港口附近会有廉价妓女和充满异国情调的商场。"),
                 "warehouse" : District("The Warehouse", 2, 2, 40, ((laborer, 10), (sailor, 20), (commoner, 40), (craftsman, 30)), ["club"], pic = "districts/warehouse.jpg", description = "仓库是Zan的工业区，各种工匠和短工都来这里找工作。白天的街道上充斥着各种交易和商业活动，但晚上异常凶险。"),
                 "gardens" : District("The Magic Gardens", 4, 3, 100, ((commoner, 5), (craftsman, 15), (bourgeois, 30), (guildmember, 30), (patrician, 20)), ["onsen"], pic = "districts/gardens.jpg", description = "当地的法师们聚集在这里吸取法力，并进行着一个个漫长而危险的实验。据说某些实验偶尔也会失败..."),
                 "cathedra" : District("The Cathedra", 4, 3, 100, ((commoner, 5), (craftsman, 10), (bourgeois, 20), (guildmember, 35), (patrician, 30)), ["okiya"], pic = "districts/cathedra.jpg", description = "大教堂是阿里奥斯教团的圣地中心。朝圣者、骑士和牧师在祈祷和仪式中磨拳擦掌，而精明的商人和银行家则为他们提供昂贵的服务，赚取利润。"),
                 "hold" : District("The King's Hold", 6, 4, 150, ((patrician, 20), (aristocrat, 50), (noble, 30)), "free", pic = "districts/final castle night.webp", description = "这里是Zan的权力中心，朝臣们在这里争夺权力和国王的支持。然而在体面和特权的表象背后，却暗藏刀光剑影...... 请注意。")
                }

        endless_district = District("The King's Hold", chapter=7, rank = 5, diff = 200, pop = ((royal, 100),), room = ["tavern", "club", "onsen", "okiya"], pic = "districts/final castle.webp", description = "这里是Zan的权力中心，朝臣们在这里争夺权力和国王的支持。然而在体面和特权的表象背后，却暗藏刀光剑影...... 请注意。")

        all_districts = [district_dict[d] for d in ["slum", "warehouse", "docks", "gardens", "cathedra", "hold"]]
        # for d in ["slum", "warehouse", "docks", "gardens", "cathedra", "hold"]:
        #     all_districts.append(district_dict[d])

        # CREATE FIRST DISTRICT #

        district = district_dict["slum"]

#     #### ACTIVE EFFECTS DICTIONARY ####

#     active_effects_dict = defaultdict(list)

    #### SPELLS ####

    call init_spells() from _call_init_spells

    #### GIRLS ####

    # TRAITS & PERKS #

    call init_traits() from _call_init_traits
    call init_perks() from _call_init_perks


    # SEX ACTS #
    python:
        anal = Sexact(0.2, 1.25)
        sex = Sexact(0.5, 1.0)
        service = Sexact(0.4, 1.0)
        fetish = Sexact(0.1, 1.5)


    # CREATE SLAVEMARKET #

        slavemarket = NPC()


    #### ITEMS ####

    call init_items() from _call_init_items

    # FURNITURE

    call init_furniture() from _call_init_furniture

    #### RESOURCES ####

    python:
        resource_dict = {
                         "gold" : Resource("gold", rank=0, sound=s_gold),
                         "prestige" : Resource("prestige", rank=0, sound=s_chimes),
                         "action" : Resource("action", rank=0, sound=s_success),
                         "mana" : Resource("mana", rank=0, sound=s_spell),
                         "wood" : Resource("wood", rank=2, stat="strength", sound=s_saw, location=shipyard),
                         "dye" : Resource("dye", rank=2, stat="spirit", sound=s_bubbling, location=beach),
                         "leather" : Resource("leather", stat="charisma", rank=2, sound=s_equip_item, location=stables),
                         "marble" : Resource("marble", rank=3, stat="strength", sound=s_stone, location=old_ruins),
                         "silk" : Resource("silk", rank=3, stat="spirit", sound=s_dress, location=hanging_gardens),
                         "ore" : Resource("ore", rank=3, stat="charisma", sound=s_clash, location=guild_quarter),
                         "diamond" : Resource("diamond", rank=4, sound=s_success),
                        }

        auto_extractors = defaultdict(bool)

        # CREATE SHOPS #

        shop = NPC("shop")
        init_items()

        # City Merchants

        city_merchants = [NPC_riche, NPC_ramias, NPC_gurigura, NPC_katryn, NPC_giftgirl, NPC_twins]

        # Minion Merchants

        minion_merchants = [NPC_stella, NPC_goldie, NPC_willow, NPC_gina]

        # Equip magic notebook (temp)
        MC.items.append(magic_notebook)
        MC.equip(magic_notebook)


        # INIT TAXES

        init_tax()


    #### QUESTS AND CLASSES ####

    call init_postings() from _call_init_postings

    # CREATE POSTING BOARD #
    python:
        quest_board = NPC()
        load_quest_pics()


    # CREATE MOONS

    call init_moons() from _call_init_moons


    # EVENT DICTIONARY (Events need to be added to the game with 'story_add_event' in order to proc)

    $ event_dict = {
                  "zodiac_intro" : StoryEvent("zodiac_intro", type="day", once=False),
                  "new_contract" : StoryEvent("new_contract", rank=2, day=1, once=False, type="morning"),
                  "run_contract" : StoryEvent("run_contract", rank=2, day=28, once=False, type="night"),
                  "tax_check" : StoryEvent("tax_check", rank=2, day=15, once=False, type="morning"),
                  "tax_payment" : StoryEvent("tax_payment", rank=2, day=1, once=False, type="night"),
                  "advertising_intro" : StoryEvent("advertising_intro", once=False, type="morning"),
                  "bis_introduction" : StoryEvent("bis_introduction", condition="has_bis"),
                  "group_introduction" : StoryEvent("group_introduction", condition="has_group"),

                  "farm_meet_gizel" : StoryEvent(label = "farm_meet_gizel", chapter = 1, chance = 0.5, location = "spice market", condition = None, not_condition = None, once = True),
                  "farm_meet_gizel2" : StoryEvent(label = "farm_meet_gizel2", chapter = 1, chance = 1.0, location = "junkyard", condition = None, not_condition = None, once = True),
                  "farm_go_with_gizel" : StoryEvent(label = "farm_go_with_gizel", chapter = 1, chance = 1.0, location = "farm", condition = None, not_condition = None, once = True),
                  "farm_found_a_place" : StoryEvent(label = "farm_found_a_place", chapter = 1, chance = 1.0, location = "junkyard", condition = None, not_condition = None, once = True),
                  "farm_gizel_introduction" : StoryEvent(label = "farm_gizel_introduction", chapter = 1, chance = 1.0, location = "farm", condition = None, not_condition = None, once = True),
                  "farm_meet_goldie" : StoryEvent(label = "farm_meet_goldie", chapter = 1, chance = 0.5, location = "farm", condition = None, not_condition = None, once = True, order=1),
                  "farm_meet_stella" : StoryEvent(label = "farm_meet_stella", chapter = 2, chance = 1.0, location = "harbor", condition = None, not_condition = None, once = True, order=1),
                  "farm_meet_willow" : StoryEvent(label = "farm_meet_willow", chapter = 1, chance = 1.0, location = "sewers", condition = None, not_condition = None, once = True, order=1),
                  "farm_meet_gina" : StoryEvent(label = "farm_meet_gina", chapter = 1, chance = 1.0, location = "junkyard", condition = None, not_condition = None, once = True, order=1),
                  "farm_activate_goldie" : StoryEvent(label = "farm_activate_goldie", chapter = 1, chance = 1.0, location = "farm", condition = None, not_condition = None, once = True),
                  "farm_second_monster" : StoryEvent(label = "farm_second_monster", chapter = 1, chance = 1.0, location = "farm", condition = None, not_condition = None, once = True),

                  "c1_visit_watchtower" : StoryEvent(label = "c1_visit_watchtower", chapter = 1, chance = 1.0, location = "watchtower", condition = "c1_goal_reached", min_gold=1000, not_condition = None, once = True),
                  "c1_thieves_guild_tip" : StoryEvent(label = "c1_thieves_guild_tip", chapter = 1, type="city", chance = 0.25, not_condition = "c1_spice_market"),
                  "c1_spice_market_25" : StoryEvent(label = "c1_spice_market", chapter = 1, chance = 0.25, location = "spice market", condition = "c1_thieves_guild_tip"),
                  "c1_spice_market" : StoryEvent(label = "c1_spice_market", chapter = 1, chance = 1.0, location = "spice market", condition = "c1_thieves_guild_tip"),
                  "c1_sewers" : StoryEvent(label = "c1_sewers", chapter = 1, location = "sewers", condition = "c1_spice_market"),
                  "c1_sewers_return" : StoryEvent(label = "c1_sewers_return", chapter = 1, location = "sewers"),
                  "c1_thieves_guild_found" : StoryEvent(label = "c1_thieves_guild_found", chapter = 1, location = "thieves guild", not_condition = "c1_goal_reached"),
                  "c1_ask_guild_for_help" : StoryEvent(label = "c1_ask_guild_for_help", chapter = 1, location = "thieves guild", condition = "c1_robbed"),
                  "c1_satella_intro" : StoryEvent(label = "c1_satella_intro", chapter = 1, location = "thieves guild", condition = "c1_ask_guild_for_help"),
                  "c1_captain_meeting" : StoryEvent(label = "c1_captain_meeting", chapter = 1, location = "watchtower", condition = "c1_satella_intro"),

                "c2_sewer_girl_returns" : StoryEvent(label = "c2_sewer_girl_returns", chapter = 2),
                "c2_meet_carpenter" : StoryEvent(label = "meet_carpenter", location = "gallows"),
                # "c2_intro" : StoryEvent(label = "c2_intro", chapter=2),
                "c2_princess_visit1" : StoryEvent(label = "c2_princess_visit1", chapter=2, location = "stables", weekday="Saturday"),
                "c2_princess_visit2" : StoryEvent(label = "c2_princess_visit2", chapter=2, weekday="Monday"),
                "c2_gio_meeting" : StoryEvent(label = "c2_gio_meeting", chapter=2, location = "plaza"),
                "c2_suzume_forest1" : StoryEvent(label = "c2_suzume_forest1", chapter=2, location = "farm"),
                "c2_suzume_arena" : StoryEvent(label = "c2_suzume_arena", chapter=2, location = "arena"),
                "c2_suzume_forest2" : StoryEvent(label = "c2_suzume_forest2", chapter=2, location = "farm"),
                "c2_suzume_brothel" : StoryEvent(label = "c2_suzume_brothel", chapter=2, location = "seafront"),
                "c2_homura_okiya1" : StoryEvent(label = "c2_homura_okiya1", type="night", chapter=2, room="okiya", chance=0.3),
                "c2_narika_H1" : StoryEvent(label = "c2_narika_H1", type="night"),

                "c3_suzume_hint" : StoryEvent(label = "c3_suzume_hint", type="morning", chapter=3),

                "meet_gurigura" : StoryEvent(label = "meet_gurigura", location = "prison", order=1),
                "meet_ramias" : StoryEvent(label = "meet_ramias", location = "arena", order=1),
                "meet_katryn" : StoryEvent(label = "meet_katryn", location = "library", order=1),
                "meet_riche" : StoryEvent(label = "meet_riche", location = "botanical garden", order=1),
                "meet_giftgirl" : StoryEvent(label = "meet_giftgirl", location = "exotic emporium", order=1),
                "meet_twins" : StoryEvent(label = "meet_twins", location = "pilgrim road", order=1),

                "satella_first_visit" : StoryEvent(label = "satella_first_visit", location = "thieves guild", chapter = 2),
                "satella_visit" : StoryEvent(label = "satella_visit", location = "thieves guild", chapter = 2, once = False),

                "wood_intro" : StoryEvent(label = "wood_intro", location = "shipyard", order=1),
                "dye_intro" : StoryEvent(label = "dye_intro", location = "beach", order=1),
                "leather_intro" : StoryEvent(label = "leather_intro", location = "stables", order=1),
                "marble_intro" : StoryEvent(label = "marble_intro", location = "old ruins", order=1),
                "silk_intro" : StoryEvent(label = "silk_intro", location = "hanging gardens", order=1),
                "ore_intro" : StoryEvent(label = "ore_intro", location = "guild quarter", order=1),
                "diamond_intro" : StoryEvent(label = "diamond_intro", location = "waterfalls", order=1),

                "willow fight" : StoryEvent(label = "willow_fight", chance = 0.04, once = False, room="onsen"),
                "willow relative" : StoryEvent(label = "willow_relative", room="onsen"),
                "gina research" : StoryEvent(label = "gina_research", location="prison"),
                "jobgirl_beach" : StoryEvent(label = "jobgirl_beach", location="beach", once=False),

                "stella_invitation" : StoryEvent(label = "stella_invitation", chance = 0.05, chapter=4),
                "stella_secret1" : StoryEvent(label = "stella_secret1", location="guild quarter", condition_func=is_first_tuesday),
                "stella_secret2" : StoryEvent(label = "stella_secret2", location="guild quarter", condition_func=is_first_tuesday, once=False),

                "slave_beach_event" : StoryEvent(label = "slave_beach_event", locations=beach_locations, seasons=["spring", "summer"], condition_func=slave_beach_event_happens, once=False),

                 }

    # REGISTER EVENTS

    call init_events() from _call_init_events_1

    # START MODS

    $ game.start_mods()

    return


label init_events():

    # Reminder: story_add_event type can be either 'city' (default) or 'daily'

    python:
        # CONTRACTS #
        story_add_event("new_contract", "daily")
        story_add_event("run_contract", "daily")
        story_add_event("bis_introduction", "daily")
        story_add_event("group_introduction", "daily")
        story_add_event("advertising_intro", "daily")

        # TAXES #
        story_add_event("tax_check", "daily")
        story_add_event("tax_payment", "daily")

        # MISC #
        calendar.set_alarm(333, Event(label = "hmas"))
        story_add_event("slave_beach_event", "city")

        if not debug_mode:
            # TUTORIAL #
            daily_events.append(event_dict["zodiac_intro"])

            # STORY #
            calendar.set_alarm(2, Event(label = "c1_gio_is_back"))
            calendar.set_alarm(5, Event(label = "c1_meet_kosmo"))
            calendar.set_alarm(8, Event(label = "c1_ambush"))
            story_add_event("c1_thieves_guild_tip", "city")
            story_add_event("c2_meet_carpenter")
            story_add_event("farm_meet_gizel")
            story_add_event("farm_meet_goldie")

            # RESOURCES #
            for res in build_resources:
                story_add_event(res + "_intro")

    return

#### END OF BK START FILE ####
