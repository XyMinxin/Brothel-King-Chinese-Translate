######         BRO KING          ######

## The game starts here. ##

label start:

    stop music fadeout 3.0

    $ gp_gallery = {} # Empties gallery to save on memory in-game

    $ debug_mode = False
    $ story_mode = True
    $ starting_chapter = 1
    $ enemy_general = None
    $ unlocked_shops = []
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

            "No story mode (Test)":
                $ story_mode = False

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

            "No story mode (Test)" if persistent.new_game_plus:
                $ story_mode = False

    jump quick_start


label quick_start:

    call init_game(quick=True) from _call_init_game

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

    # Create enemy general for the siege security event

    if dice(2) == 1:
        $ enemy_general = get_girls(1, free=True, p_traits=["Warrior"])[0]
    else:
        $ enemy_general = get_girls(1, free=True, p_traits=["Caster"])[0]
    $ enemy_general.love = -50

    if starting_chapter > 1:
        call debug_load_chapter(starting_chapter) from _call_debug_load_chapter

    call chapter(starting_chapter, forced=True) from _call_chapter_1

    # SET UP CALENDAR
    $ calendar.updates()

    if debug_mode != "quick" and starting_chapter in (1, 6):

        menu:
            "What will you use as a front for your business?"

            "A tavern":
                $ brothel.add_room("tavern", forced=True)

            "A dance club":
                $ brothel.add_room("strip club", forced=True)

            "A bath house":
                $ brothel.add_room("onsen", forced=True)

            "An okiya (geisha house)":
                $ brothel.add_room("okiya", forced=True)

        $ brothel.free_room = False

    jump main



label init_game(quick=False):

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

        if quick:
            main_firstvisit = False
            district_firstvisit = False
            brothel_firstvisit = False
            shop_firstvisit = False
            slavemarket_firstvisit = False
            girls_firstvisit = False
            postings_firstvisit = False

        else:
            main_firstvisit = True
            district_firstvisit = True
            brothel_firstvisit = True
            shop_firstvisit = True
            slavemarket_firstvisit = True
            girls_firstvisit = True
            postings_firstvisit = True

        farm_firstvisit = True

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

        sill_name = "Sill"
        kuro_name = "Princess"
        maid_name = "Minako"
        gio_fucked_sill = ""
        kosmo_name = "Strange man"
        sergeant_name = "Woman"
        captain_name = "Captain Farah"
        lieutenant_name = "Lieutenant"
        maya_name = "Woman"
        maya_love = 0
        renza_name = "Woman"
        satella_name = "Girl"
        shalia_name = "Voice"
        mask_name = "Shadow"
        gizel_name = "Elf girl"
        stella_name = "Woman slaver"
        goldie_name = "Woman"
        willow_name = "Strange girl"
        gina_name = "Girl"
        carpenter_name = "Woman"
        bast_name = "Market girl"
        banker_name = "Mysterious woman"
        riche_name = "Sweet girl"
        ramias_name = "Tough girl"
        gurigura_name = "Wild girl"
        katryn_name = "Nerdy girl"
        today_name = "Happy tailor"
        yesterday_name = "Quiet tailor"
        jobgirl_name = "Freelancer"
        kenshin_name = "Female knight"
        homura_name = "Noble lady"
        suzume_name = "Blue-haired girl"
        taxgirl_name = "Elegant woman"
        narika_name = "Petite Kunoichi"
        mizuki_name = "Elegant Kunoichi"
        haruka_name = "Athletic Kunoichi"
        chaos_name = "Talking sword"

        # NPC OBJECTS / TRAINERS #

        NPC_sill = NPC(name = "Sill", portrait = "side sill happy", trainer_description = "'{i}Another cum stain? *sigh* Give me that.{/i}'\n\n{b}The Caretaker{/b}\nGrants free upkeep to a random girl every night.", effects = Effect("special", "free upkeep", 1, scope = "brothel"))
        NPC_sad_sill = NPC(name = "Sad Sill", portrait = "side sill sad", trainer_description = "bla", effects = Effect("change", "charm", 40, scope = "brothel"))
        NPC_gio = NPC()
        NPC_kosmo = NPC()
        NPC_sergeant = NPC()
        NPC_roz = NPC(name = "Roz", char = roz)
        NPC_maya = NPC(name = "Maya", portrait = "side maya", trainer_description = "'{i}I'd better check the perimeter. Again.{/i}'\n\n{b}Ever vigilant{/b}\nBrothel threat builds up 33% slower.", effects = Effect("boost", "threat build up", -0.33, scope = "brothel"))
        NPC_renza = NPC(name = "Renza", portrait = "side renza", bg = 'bg thieves_guild room', trainer_description = "'{i}This purse seems heavy. Let me relieve you...{/i}'\n\n{b}Sleight of hand{/b}\nAll girls can pick pockets. Girls with the {i}Thief{/i} trait never get caught.", effects = Effect("special", "pickpocket", 1, scope = "brothel"))
        NPC_satella = NPC(name = "Satella", portrait = "side satella", bg = "bg shalia_temple", trainer_description = "'{i}Isn't it fun to play in the shadows? Fufufu...{/i}'\n\n{b}Dark priestess{/b}\nFear increases faster.", effects = Effect("boost", "fear gains", 1, scope = "world"))
        NPC_captain = NPC(name = "Farah", portrait = "side captain", bg = 'bg vault', trainer_description = "'{i}If you wanna get on top, you must be ready to do anything. ANYTHING!{/i}'\n\n{b}Immoral{/b}\nGirls will grow used to anal and fetish acts faster.", effects = (Effect("change", "anal preferences changes", 25, scope = "brothel"), Effect("change", "fetish preferences changes", 25, scope = "brothel")))
        NPC_lieutenant = NPC(name = "Lydie", portrait = "side lieutenant", trainer_description = "'{i}Do you want me to make an example of you? I didn't think so.{/i}'\n\n{b}Harsh discipline{/b}\nGirls are less likely to refuse to work.", effects = Effect("boost", "obedience tests", 0.1, scope = "brothel"))
        NPC_gizel = NPC(name = "Gizel", defense = 3, portrait = "side gizel smirk", bg = 'bg farm', trainer_description = "'{i}I love the smell of despair in the morning.{/i}'\n\n{b}Bad mojo{/b}\nEarn more mojo from fear interactions in and out of the farm.", effects = Effect("boost", "all mojo gains", 0.5))
        NPC_banker = NPC(name = "Banker", portrait = "side banker", bg = 'bg banking_quarter')
        NPC_riche = NPC(name = "Riche", char=riche, portrait = "side riche", bg = 'bg botanical_garden', item_types=["Flower"])
        NPC_ramias = NPC(name = "Ramias", char=ramias, portrait = "side ramias", bg = 'bg arena', item_types=["Weapon"], trainer_description = "'{i}Stick 'em with the pointy end!{/i}'\n\n{b}Martial training{/b}\nAll girls receive +2 to their personal defense.", effects = Effect("change", "defense", 2, scope = "brothel"))
        NPC_gurigura = NPC(name = "Gurigura", char=gurigura, portrait = "side gurigura", bg = 'bg prison', item_types=["Toy", "Food", "Supplies"])
        NPC_katryn = NPC(name = "Katryn", char=katryn, portrait = "side katryn", bg = 'bg library', item_types=["Ring", "Necklace"])
        NPC_giftgirl = NPC(name = "Gift Shop Girl", char=giftgirl, portrait = "side giftgirl", bg = 'bg exotic_emporium', item_types=["Gift", "Misc"])
        NPC_twins = NPC(name = "Today", char=today, portrait = "side today", bg = 'bg pilgrim_road', item_types=["Dress", "Accessory"])
        NPC_stella = NPC(name="Stella", char=stella, portrait = "side stella", bg = 'bg harbor', minion_type="stallion", trainer_description = "'{i}Your weak training techniques are no match for the Blood Islands.{/i}'\n\n{b}Intensive Farming{/b}\nIncreases the efficiency of all Farm sexual training.", effects = Effect("boost", "farm preference increase", 0.5, scope = "farm"))
        NPC_goldie = NPC(name="Goldie", char=goldie, portrait = "side goldie", bg = 'bg farmland', minion_type="beast", trainer_description = "'{i}I read it in a book... *blush*{/i}'\n\n{b}Technique{/b}\nGirls will grow used to service and sex acts faster.", effects = (Effect("change", "service preferences changes", 25, scope = "brothel"), Effect("change", "sex preferences changes", 25, scope = "brothel")))
        NPC_willow = NPC(name="Willow", char=willow, portrait = "side willow", bg = 'bg sewers', minion_type="monster")
        NPC_gina = NPC(name="Gina", char=gina, portrait = "side gina", bg = 'bg junkyard', minion_type="machine")
        NPC_bast = NPC(name="Bast", char=bast, portrait = "side bast", bg = 'bg market', trainer_description = "'{i}Gold is only one of the many resources that can be traded in Zan.{/i}'\n\n{b}Resourceful{/b}\nPart of your brothel's income is converted to random resources.", effects = [Effect("special", "resources as income", 1.0, scope = "brothel"), Effect("boost", "income", -0.2, scope = "brothel")])
        NPC_jobgirl = NPC(name="Scarlet", char=jobgirl, bg = "bg town")
        NPC_kuro = NPC(name="Kurohime", char=kuro)
        NPC_homura = NPC(name="Homura", char=homura)
        NPC_taxgirl = NPC(name="Taxgirl", char=taxgirl, portrait = "side taxgirl", trainer_description = "'{i}Just expense the lobster and champagne... And give me some more.{/i}'\n\n{b}Tax Deductible{/b}\nShields part of your income against taxes every night.", effects = [Effect("boost", "taxable net income", -0.05, scope = "brothel")])

        # Chapter 2 Kunoichi
        NPC_suzume = NPC(name="Suzume", char=suzume, portrait = "side suzume", trainer_description = "'{i}Found another spy yesterday... He tried to stab me, it was hilarious! Kukukuku...{/i}'\n\n{b}Night Patrol{/b}\n33%% chance of twarting security events (does not reset threat level).", effects = [Effect("special", "security block", 1.0, 0.33, scope = "brothel")])
        NPC_narika = NPC(name="Narika", char=narika)
        NPC_mizuki = NPC(name="Mizuki", char=mizuki)
        NPC_haruka = NPC(name="Haruka", char=haruka)

        NPC_carpenter = NPC(name="Iulia", char=carpenter)
        NPC_freak = NPC(name="Papa Freak", char=papa)
        NPC_kenshin = NPC(name="Lady Kenshin", char=kenshin, portrait = "side kenshin", bg = "bg palace")

        MC.trainers.append(NPC_sill)
        MC.current_trainer = NPC_sill

        if debug_mode or not story_mode:
            MC.trainers.append(NPC_maya)
            MC.trainers.append(NPC_lieutenant)
            MC.trainers.append(NPC_captain)
            MC.trainers.append(NPC_renza)
            MC.trainers.append(NPC_satella)
            MC.trainers.append(NPC_bast)
            MC.trainers.append(NPC_stella)
            MC.trainers.append(NPC_gizel)
            MC.trainers.append(NPC_goldie)
            MC.trainers.append(NPC_taxgirl)
            MC.trainers.append(NPC_suzume)
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
                              "stables" : Installation(name = "stables", pic = "stables.webp", tags = ["big"], minions = [Minion("stallion", name="Bob")], minion_type = "stallion", skill = "libido", rank = 1),
                              "pig stall" : Installation(name = "pig stall", pic = "pig stall.webp", tags = ["beast"], minion_type = "beast", skill = "obedience"),
                              "monster den" : Installation(name = "monster den", pic = "monster den.webp", tags = ["monster"], minion_type = "monster", skill = "constitution"),
                              "workshop" : Installation(name = "workshop", pic = "workshop.webp", tags = ["machine", "toy"], minion_type = "machine", skill = "sensitivity"),
                              }
        farm = Farm()
        init_powers()

    #### DISTRICTS ####
    python:

        # POPULATIONS #

        beggar = Population("beggars", "beggar.webp", diff = 15, range = 10, rank=1, weight=5, base_description="An extremely unrefined and undemanding class of customers. After all, beggars can't be choosers.")
        thug = Population("thugs", "thug.webp", diff = 20, range = 10, rank=1, weight=3, effects=[Effect("boost", "crazy", 1)], base_description="Thug life comes with its share of bros and hoes. You're the bro that gets the hoes.")
        laborer = Population("laborers", "laborer.webp", 30, range = 20, rank=1, weight=2, base_description="Workers of the world, unite! Or, you know, get a girl for the night.")

        sailor = Population("sailors", "sailor.webp", 40, range = 20, rank=2, effects=[Effect("change", "waitress preference", 15), Effect("change", "anal preference", 15)], base_description="Sailors are famously randy when they come ashore. After a long voyage, seamen need some release.")
        commoner = Population("commoners", "commoner.webp", 50, range = 20, rank=2, effects=[Effect("change", "dancer preference", 15), Effect("change", "service preference", 15)], base_description="Common lives, common jobs, common wives... Seeing a commoner trying to escape all of this in a brothel is... common.")

        craftsman = Population("craftsmen", "craftsman.webp", 70, range = 30, rank=2, effects=[Effect("special", "horny", 1)], base_description="Craftsmen work with their hands, and when their hands get restless, they like to lay them on a pretty girl. Craftsmen are crafty.")

        bourgeois = Population("bourgeois", "bourgeois.webp", 90, range = 30, rank=3, effects=[Effect("change", "geisha preference", 15), Effect("change", "sex preference", 15)], base_description="When did 'down with the bourgeoisie' become 'get down with the bourgeoisie'? You sold out, man.")
        guildmember = Population("guild members", "guild member.webp", 110, range = 30, rank=3, effects=[Effect("change", "masseuse preference", 15), Effect("change", "fetish preference", 15)], base_description="Guild members are like craftsmen, but craftier.")

        patrician = Population("patricians", "patrician.webp", 110, range = 40, rank=3, effects=[Effect("special", "horny", 1), Effect("change", "satisfaction", -1)], base_description="Father figures to the community, ready to meet young girls with daddy issues.")

        aristocrat = Population("aristocrats", "aristocrat.webp", 135, range = 40, rank=4, effects=[Effect("boost", "crazy", 1.5), Effect("change", "satisfaction", -1)], base_description="Above the law. Entitled AF. Filthy rich. What's not to like?")
        noble = Population("nobles", "noble.webp", 160, range = 40, rank=4, effects=[Effect("change", "satisfaction", -2)], base_description="Nobles are easily bored. Living a life of privilege isn't all fun and games, it's also yawns.")

        royal = Population("royals", "royal.webp", 200, range = 50, rank=5, effects=[Effect("change", "satisfaction", -3)], base_description="People say royals are jaded, undeserving narcissistic parasites. No one gives them credit for how generous they are with their subjects' money. Sad.")

        all_populations = [beggar, thug, laborer, sailor, commoner, craftsman, bourgeois, guildmember, patrician, aristocrat, noble, royal]

        # LOCATIONS # Locations should have been in a dictionary from the start, but it's messy. Sorry.

        spice_market = Location("Spice market", pic = "Spice market.webp")
        sewers = Location("Sewers", pic = "Sewers.webp", menu = ("Visit the monster catcher", "visit_willow"), menu_costs_AP=False) # Monster merchant
        farmland = Location("Farm", pic = "farmland.webp", menu = ("Visit the rancher", "visit_goldie"), menu_costs_AP=False) # Beast merchant
        watchtower = Location("Watchtower", pic = "Watchtower.webp", menu = ("Browse the Captain's vault", "visit_watchtower"))
        junkyard = Location("Junkyard", pic = "Junkyard.webp", menu = ("Visit the scientist", "visit_gina"), menu_costs_AP=False) # Machine merchant
        thieves_guild = Location("Thieves guild", pic = "Thieves guild.webp", secret = True, menu = ("Browse the guild warehouse", "visit_thieves_guild"))

        harbor = Location("Harbor", pic = "Harbor.webp", menu = ("Visit the headmaster", "visit_stella"), menu_costs_AP=False) # Stallion merchant
        shipyard = Location("Shipyard", pic = "Shipyard.webp", menu = ("Collect wood", "collect_wood")) # Wood extraction
        taverns = Location("Taverns", pic = "Taverns.webp")
        seafront = Location("Seafront", pic = "Seafront.webp", menu = ("Visit Papa Freak", "visit_papa"), menu_costs_AP=False)
        beach = Location("Beach", pic = "Beach.webp", menu = ("Brew dye", "collect_dye")) # Dye
        exotic_emporium = Location("Exotic emporium", pic = "Exotic emporium.webp", menu = ("Visit gift shop", "visit_giftgirl"), menu_costs_AP=False) # Gift girl, gifts

        stables = Location("Stables", pic = "Stables.webp", menu = ("Get leather", "collect_leather")) # Leather
        plaza = Location("Plaza", pic = "Plaza.webp", menu = ("Contact Homura", "c3_contact_homura"), menu_costs_AP=False) # Homura, story
        market = Location("Market", pic = "Market.webp", menu = ("Visit the exchange", "visit_exchange"), action=True, menu_costs_AP=False) # Resource market
        gallows = Location("Gallows", pic = "Gallows.webp", menu = ("Visit Papa Freak", "visit_papa"), menu_costs_AP=False)
        prison = Location("Prison", pic = "Prison.webp", menu = ("Visit G's bazaar", "visit_gurigura"), menu_costs_AP=False) # Gurigura, toys
        arena = Location("Arena", pic = "Arena.webp", menu = ("Visit weapon shop", "visit_ramias"), menu_costs_AP=False) # Ramias, weapons

        botanical_garden = Location("Botanical garden", pic = "Botanical garden.webp", menu = ("Visit flower stall", "visit_riche"), menu_costs_AP=False) # Riche, flowers
        hanging_gardens = Location("Hanging gardens", pic = "Hanging gardens.webp", menu = ("Weave silk", "collect_silk")) # Silk
        library = Location("Library", pic = "Library.webp", menu = ("Visit trinket shop", "visit_katryn"), menu_costs_AP=False) # Katryn, trinkets
        guild_quarter = Location("Guild quarter", pic = "Guild quarter.webp", menu = ("Smuggle ore", "collect_ore")) # Ore
        magic_guild = Location("Magic guild", pic = "Magic guild.webp")
        magic_forest = Location("Magic forest", pic = "Magic forest.webp")

        pilgrim_road = Location("Pilgrim road", pic = "Pilgrim road.webp", menu = ("Visit tailor shop", "visit_twins"), menu_costs_AP=False) # Twins, dresses
        banking_quarter = Location("Banking quarter", pic = "Banking quarter.webp", menu = ("Visit Bank", "visit_bank"), action=True, menu_costs_AP=False)
        old_ruins = Location("Old ruins", pic = "Ruins.webp", menu = ("Extract marble", "collect_marble")) # Marble
        lake = Location("Lakefront", pic = "Lake.webp")
        training_ground = Location("Training ground", pic = "Training ground.webp")
        cathedra = Location("Cathedra", pic = "Cathedra.webp")

        battlements = Location("Battlements", pic = "Battlements.webp")
        keep = Location("Keep", pic = "Keep.webp")
        hall = Location("Hall", pic = "Hall.webp")
        courtyard = Location("Courtyard", pic = "Courtyard.webp")
        temple = Location("Temple", pic = "Temple.webp")
        falls = Location("Waterfalls", pic = "Falls.webp", menu = ("Look for diamonds", "collect_diamond")) # Diamonds

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

        # DISTRICT LIST #

        district_dict = {"slum" : District("The Slums", 1, 1, 15, ((beggar, 80), (thug, 20)), pic = "districts/slums.webp", description = "The Slums are located on the outskirts of Zan, beyond the defensive wall. It is home to the Zani rabble: new arrivals, refugees, paupers, spice addicts... It is also rumored to host the hideout of the Thieves Guild, who worship the Shadow Goddess Shalia."),
                 "docks" : District("The Docks", 2, 2, 40, ((thug, 10), (laborer, 10), (sailor, 40), (commoner, 25), (craftsman, 15)), room = ["tavern"], pic = "districts/docks.webp", description = "The docks are home to rowdy sailors and dodgy pirates sheltering from the treacherous seas. With seamen all around, no wonder there is a thriving market for cheap whores near the port."),
                 "warehouse" : District("The Warehouse", 2, 2, 40, ((thug, 10), (laborer, 20), (sailor, 20), (commoner, 30), (craftsman, 20)), ["strip club"], pic = "districts/warehouse.webp", description = "The warehouse is the industrial part of Zan, where all kinds of craftsmen and day laborer come to look for work. Its streets are buzzing with trade and activities during the day, but dodgy at night."),
                 "gardens" : District("The Magic Gardens", 4, 3, 100, ((commoner, 5), (craftsman, 15), (bourgeois, 30), (guildmember, 30), (patrician, 20)), ["onsen"], pic = "districts/gardens.webp", description = "The gardens are where the magic-wielding locals gather to soak up mana after a long night of dangerous experiments. It is said some of those experiments occasionally escape..."),
                 "cathedra" : District("The Cathedra", 4, 3, 100, ((commoner, 5), (craftsman, 10), (bourgeois, 20), (guildmember, 35), (patrician, 30)), ["okiya"], pic = "districts/cathedra.webp", description = "The Cathedra is the holy center of the Arios order. Pilgrims, knights and priests rub elbows during prayers and rituals, while savvy merchants and bankers make a killing providing them with expensive service."),
                 "hold" : District("The King's Hold", 6, 4, 150, ((patrician, 20), (aristocrat, 50), (noble, 30)), "free", pic = "districts/final castle night.webp", description = "This is the center of power in Zan, where courtiers compete for power and the King's support. Behind the veneer of respectability and privilege, however, daggers are drawn... Beware.")
                }

        endless_district = District("The King's Hold", chapter=7, rank = 5, diff = 200, pop = ((royal, 100),), room = ["tavern", "strip club", "onsen", "okiya"], pic = "districts/final castle.webp", description = "This is the center of power in Zan, where courtiers compete for power and the King's support. Behind the veneer of respectability and privilege, however, daggers are drawn... Beware.")

        all_districts = [district_dict[d] for d in ["slum", "warehouse", "docks", "gardens", "cathedra", "hold"]]
        # for d in ["slum", "warehouse", "docks", "gardens", "cathedra", "hold"]:
        #     all_districts.append(district_dict[d])

        # CREATE FIRST DISTRICT #

        district = district_dict["slum"]

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

        shop = NPC("shop", char=shopgirl, portrait = "side shopgirl", bg = "bg shop")
        unlocked_shops += [shop]
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

        #### NO STORY ####

        if debug_mode or not story_mode:
            farm.activate()
            farm_firstvisit = False
            gizel_name = "Gizel"

            harbor.action = True
            stella_name = "Stella"
            farmland.action = True
            goldie_name = "Goldie"
            sewers.action = True
            willow_name = "Willow"
            junkyard.action = True
            gina_name = "Gina"

            unlocked_shops += [NPC_goldie, NPC_willow, NPC_gina]

            thieves_guild.secret = False
            thieves_guild.action = True
            renza_name = "Renza"
            captain_name = "Farah"

            story_flags["found wagon"] = True
            story_flags["met carpenter"] = True
            carpenter_name = "Iulia"

            shipyard.action = True # Wood
            stables.action = True # Leather
            beach.action = True # Dye
            old_ruins.action = True # Stone
            hanging_gardens.action = True # Silk
            guild_quarter.action = True # Ore
            falls.action = True # Diamond


    #### QUESTS AND CLASSES ####

    call init_postings() from _call_init_postings

    # CREATE POSTING BOARD #
    python:
        quest_board = NPC()
        load_quest_pics()


    # CREATE MOONS

    call init_moons() from _call_init_moons

    # SELECT GOAL CHANNELS

    if story_mode:
        $ game.goal_channels = goal_channels
    else:
        $ game.goal_channels = goal_channels_no_story


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

        if not debug_mode and story_mode:
            # TUTORIAL #
            daily_events.append(event_dict["zodiac_intro"])

            # STORY #
            calendar.set_alarm(3, Event(label = "c1_gio_is_back"))
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
