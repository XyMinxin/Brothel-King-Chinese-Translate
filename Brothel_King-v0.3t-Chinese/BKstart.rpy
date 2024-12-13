######         BRO KING          ######

## The game starts here. ##

# Order of operations:
# 1. start
# 2. intro (optional)
# 3. init_game
# 4. choose_difficulty
# 5. Advance to chapter

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
    $ notify_list = []
    $ notify_history = [] # Needed to avoid certain formating problems

    scene black with fade

    if not persistent.seen_intro:
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

    jump start_no_intro


label start_no_intro:

    call init_game(quick=True) from _call_init_game

    if debug_mode != "quick":
        call choose_difficulty() from _call_choose_difficulty

    call advance_to_chapter(starting_chapter, start=True) from _call_advance_to_chapter_3

    if debug_mode == "quick": # Base values for debugging
        $ MC.set_playerclass("Wizard")
        $ MC.girls = get_girls(24)
        $ MC.gold = 100000
        $ MC.speed = 30
        $ MC.reset_interactions()

        python:
            for room in brothel.rooms.values():
                room.buy(forced=True)

    # # SET UP CALENDAR
    # $ calendar.updates()

    jump main

## DIFFICULTY

label choose_difficulty():
    scene black with fade
    play music m_suspense fadein 3.0

    $ def_panel = "MC"

    # Recall previous NG+ settings

    python:
        for s in NGP_settings:
            s.recall()

    # Sanity check - Remove unavailable girl mixes

    while True:
        show screen quick_start(def_panel)
        $ r = ui.interact()

        if r:
            hide screen quick_start
            if r == "edit mix":
                call girlpack_menu() from _call_girlpack_menu_1
                $ def_panel = "mix"

            elif r == "reset NGP":
                python:
                    for s in NGP_settings:
                        s.reset()
                $ def_panel = "extras"

            else: # CONFIRM
                $ starting_chapter = NGP_settings_dict["starting chapter"].get()

                if starting_chapter > 1 and (NGP_settings_dict["free girl challenge"].get() or NGP_settings_dict["training challenge"].get()) and not debug_mode:
                    menu:
                        "You have activated a challenge. You cannot start at a later chapter if you want to complete the challenge."
                        "Do the challenge and start at chapter 1":
                            $ starting_chapter = 1

                        "Cancel the challenge":
                            $ NGP_settings_dict["free girl challenge"].reset()
                            $ NGP_settings_dict["training challenge"].reset()

                        "Change settings":
                            jump choose_difficulty

                stop music fadeout 3.0
                return

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
        brothel_secondvisit = True

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

        sill_name = _("Sill")
        kuro_name = _("Princess")
        maid_name = _("Minako")
        gio_fucked_sill = ""
        kosmo_name = _("Strange man")
        sergeant_name = _("Woman")
        captain_name = _("Captain Farah")
        lieutenant_name = _("Lieutenant")
        maya_name = _("Woman")
        maya_love = 0
        renza_name = _("Woman")
        satella_name = _("Girl")
        shalia_name = _("Voice")
        mask_name = _("Shadow")
        gizel_name = _("Elf girl")
        stella_name = _("Woman slaver")
        goldie_name = _("Woman")
        willow_name = _("Strange girl")
        gina_name = _("Girl")
        carpenter_name = _("Woman")
        bast_name = _("Market girl")
        banker_name = _("Mysterious woman")
        riche_name = _("Sweet girl")
        ramias_name = _("Tough girl")
        gurigura_name = _("Wild girl")
        katryn_name = _("Nerdy girl")
        today_name = _("Happy tailor")
        yesterday_name = _("Quiet tailor")
        jobgirl_name = _("Freelancer")
        kenshin_name = _("Female knight")
        homura_name = _("Noble lady")
        suzume_name = _("Blue-haired girl")
        taxgirl_name = _("Elegant woman")
        narika_name = _("Petite Kunoichi")
        mizuki_name = _("Elegant Kunoichi")
        haruka_name = _("Athletic Kunoichi")
        chaos_name = _("Talking sword")
        shizuka_name = _("Mage Girl")

        # NPC OBJECTS / TRAINERS #

        NPC_sill = NPC(name = _("Sill"), portrait = "side sill happy", trainer_description = __("'{i}Another cum stain? *sigh* Give me that.{/i}'\n\n{b}The Caretaker{/b}\nGrants free upkeep to a random girl every night."), effects = Effect("special", "free upkeep", 1, scope = "brothel"))
        NPC_sad_sill = NPC(name = _("Sad Sill"), portrait = "side sill sad") #, trainer_description = __("bla"), effects = Effect("change", "charm", 40, scope = "brothel"))
        NPC_gio = NPC()
        NPC_kosmo = NPC()
        NPC_sergeant = NPC()
        NPC_roz = NPC(name = _("Roz"), char = roz)
        NPC_maya = NPC(name = _("Maya"), portrait = "side maya", trainer_description = __("'{i}I'd better check the perimeter. Again.{/i}'\n\n{b}Ever vigilant{/b}\nBrothel threat builds up 33 per cent slower."), effects = Effect("boost", "threat build up", -0.33, scope = "brothel"))
        NPC_renza = NPC(name = _("Renza"), portrait = "side renza", bg = 'bg thieves_guild room', trainer_description = __("'{i}This purse seems heavy. Let me relieve you...{/i}'\n\n{b}Sleight of hand{/b}\nAll girls can pick pockets. Girls with the {i}Thief{/i} trait never get caught."), effects = Effect("special", "pickpocket", 1, scope = "brothel"))
        NPC_satella = NPC(name = _("Satella"), portrait = "side satella", bg = "bg shalia_temple", trainer_description = __("'{i}Isn't it fun to play in the shadows? Fufufu...{/i}'\n\n{b}Dark priestess{/b}\nFear increases faster."), effects = Effect("boost", "fear gains", 1, scope = "world"))
        NPC_captain = NPC(name = _("Farah"), portrait = "side captain", bg = 'bg vault', trainer_description = __("'{i}If you wanna get on top, you must be ready to do anything. ANYTHING!{/i}'\n\n{b}Immoral{/b}\nGirls will grow used to anal and fetish acts faster."), effects = (Effect("change", "anal preferences changes", 25, scope = "brothel"), Effect("change", "fetish preferences changes", 25, scope = "brothel")))
        NPC_lieutenant = NPC(name = _("Lydie"), char = lieutenant, bg = "bg guard_office", portrait = "side lieutenant", trainer_description = __("'{i}Do you want me to make an example of you? I didn't think so.{/i}'\n\n{b}Harsh discipline{/b}\nGirls are less likely to refuse to work."), effects = Effect("boost", "obedience tests", 0.1, scope = "brothel"))
        NPC_gizel = NPC(name = _("Gizel"), defense = 3, portrait = "side gizel smirk", bg = 'bg farm', trainer_description = __("'{i}I love the smell of despair in the morning.{/i}'\n\n{b}Bad mojo{/b}\nEarn more mojo from fear interactions in and out of the farm."), effects = Effect("boost", "all mojo gains", 0.5))
        NPC_banker = NPC(name = _("Banker"), portrait = "side banker", bg = 'bg banking_quarter')
        NPC_riche = NPC(name = _("Riche"), char=riche, portrait = "side riche", bg = 'bg botanical_garden', item_types=["Flower"])
        NPC_ramias = NPC(name = _("Ramias"), char=ramias, portrait = "side ramias", bg = 'bg arena', item_types=["Weapon"], trainer_description = __("'{i}Stick 'em with the pointy end!{/i}'\n\n{b}Martial training{/b}\nAll girls receive +2 to their personal defense."), effects = Effect("change", "defense", 2, scope = "brothel"))
        NPC_gurigura = NPC(name = _("Gurigura"), char=gurigura, portrait = "side gurigura", bg = 'bg prison', item_types=["Toy", "Food", "Supplies"])
        NPC_katryn = NPC(name = _("Katryn"), char=katryn, portrait = "side katryn", bg = 'bg magic_university', item_types=["Ring", "Necklace"])
        NPC_giftgirl = NPC(name = _("Gift Shop Girl"), char=giftgirl, portrait = "side giftgirl", bg = 'bg exotic_emporium', item_types=["Gift", "Misc"])
        NPC_twins = NPC(name = _("Today"), char=today, portrait = "side today", bg = 'bg pilgrim_road', item_types=["Dress", "Accessory"])
        NPC_stella = NPC(name=_("Stella"), char=stella, portrait = "side stella", bg = 'bg harbor', minion_type="stallion", trainer_description = __("'{i}Your weak training techniques are no match for the Blood Islands.{/i}'\n\n{b}Intensive Farming{/b}\nIncreases the efficiency of all Farm sexual training."), effects = Effect("boost", "farm preference increase", 0.5, scope = "farm"))
        NPC_goldie = NPC(name=_("Goldie"), char=goldie, portrait = "side goldie", bg = 'bg farmland', minion_type="beast", trainer_description = __("'{i}I read it in a book... *blush*{/i}'\n\n{b}Technique{/b}\nGirls will grow used to service and sex acts faster."), effects = (Effect("change", "service preferences changes", 25, scope = "brothel"), Effect("change", "sex preferences changes", 25, scope = "brothel")))
        NPC_willow = NPC(name=_("Willow"), char=willow, portrait = "side willow", bg = 'bg sewers', minion_type="monster")
        NPC_gina = NPC(name=_("Gina"), char=gina, portrait = "side gina", bg = 'bg junkyard', minion_type="machine")
        NPC_bast = NPC(name=_("Bast"), char=bast, portrait = "side bast", bg = 'bg market', trainer_description = __("'{i}Gold is only one of the many resources that can be traded in Zan.{/i}'\n\n{b}Resourceful{/b}\nPart of your brothel's income is converted to random resources."), effects = [Effect("special", "resources as income", 1.0, scope = "brothel"), Effect("boost", "income", -0.2, scope = "brothel")])
        NPC_jobgirl = NPC(name=_("Scarlet"), char=jobgirl, bg = "bg town")
        NPC_kuro = NPC(name=_("Kurohime"), char=kuro)
        NPC_homura = NPC(name=_("Homura"), char=homura)
        NPC_taxgirl = NPC(name=_("Taxgirl"), char=taxgirl, portrait = "side taxgirl", trainer_description = __("'{i}Just expense the lobster and champagne... And give me some more.{/i}'\n\n{b}Tax Deductible{/b}\nShields part of your income against taxes every night."), effects = [Effect("boost", "taxable net income", -0.05, scope = "brothel")])

        # Chapter 2 Kunoichi
        NPC_suzume = NPC(name=_("Suzume"), char=suzume, portrait = "side suzume", trainer_description = __("'{i}Found another spy yesterday... He tried to stab me, it was hilarious! Kukukuku...{/i}'\n\n{b}Night Patrol{/b}\n33%% chance of twarting security events (does not reset threat level)."), effects = [Effect("special", "security block", 1.0, 0.33, scope = "brothel")])
        NPC_narika = NPC(name=_("Narika"), char=narika)
        NPC_mizuki = NPC(name=_("Mizuki"), char=mizuki)
        NPC_haruka = NPC(name=_("Haruka"), char=haruka)

        NPC_carpenter = NPC(name=_("Iulia"), char=carpenter)
        NPC_freak = NPC(name=_("Papa Freak"), char=papa)
        NPC_kenshin = NPC(name=_("Lady Kenshin"), char=kenshin, portrait = "side kenshin", bg = "bg palace")


    #### BROTHELS ####

    # Bro cost, helpers and capacity are set in BKsettings.rpy for ease of access by casual players

        blist = {
                1 : Brothel(1, 1, upgrades = [1, 3], max_rep = 120),
                2 : Brothel(2, 2, [2, 5], max_rep = 1150),
                3 : Brothel(2, 3, [3, 6], max_rep = 1800),
                4 : Brothel(3, 4, [3, 8], max_rep = 5800),
                5 : Brothel(3, 5, [4, 9], max_rep = 8000),
                6 : Brothel(4, 6, [5, 11], max_rep = 18500),
                7 : Brothel(5, 7, [6, 12], max_rep = 33750),
                }

    #### FARM ####

        farm_installations = {
                            "stables" : Installation(name = _("stables"), pic = "stables.webp", tags = ["big"], minions = [Minion("stallion", name="Bob", start=True)], minion_type = "stallion", skill = "libido", rank = 1),
                            "pig stall" : Installation(name = _("pig stall"), pic = "pig stall.webp", tags = ["beast"], minion_type = "beast", skill = "obedience"),
                            "monster den" : Installation(name = _("monster den"), pic = "monster den.webp", tags = ["monster"], minion_type = "monster", skill = "constitution"),
                            "workshop" : Installation(name = _("workshop"), pic = "workshop.webp", tags = ["machine", "toy"], minion_type = "machine", skill = "sensitivity"),
                            }
        farm = Farm()
        init_powers()

    #### DISTRICTS ####
    python:

        # POPULATIONS #

        beggar = Population(_("beggars"), "beggar.webp", diff = 15, range = 10, rank=1, weight=5, base_description=__("An extremely unrefined and undemanding class of customers. After all, beggars can't be choosers."))
        thug = Population(_("thugs"), "thug.webp", diff = 20, range = 10, rank=1, weight=3, effects=[Effect("boost", "crazy", 1)], base_description=__("Thug life comes with its share of bros and hoes. You're the bro that gets the hoes."))
        laborer = Population(_("laborers"), "laborer.webp", 30, range = 20, rank=1, weight=2, base_description=__("Workers of the world, unite! Or, you know, get a girl for the night."))

        sailor = Population(_("sailors"), "sailor.webp", 40, range = 20, rank=2, effects=[Effect("change", "waitress preference", 15), Effect("change", "anal preference", 15)], base_description=__("Sailors are famously randy when they come ashore. After a long voyage, seamen need some release."))
        commoner = Population(_("commoners"), "commoner.webp", 50, range = 20, rank=2, effects=[Effect("change", "dancer preference", 15), Effect("change", "service preference", 15)], base_description=__("Common lives, common jobs, common wives... Seeing a commoner trying to escape all of this in a brothel is... common."))

        craftsman = Population(_("craftsmen"), "craftsman.webp", 70, range = 30, rank=2, effects=[Effect("special", "horny", 1)], base_description=__("Craftsmen work with their hands, and when their hands get restless, they like to lay them on a pretty girl. Craftsmen are crafty."))

        bourgeois = Population(_("bourgeois"), "bourgeois.webp", 90, range = 30, rank=3, effects=[Effect("change", "geisha preference", 15), Effect("change", "sex preference", 15)], base_description=__("When did 'down with the bourgeoisie' become 'get down with the bourgeoisie'? You sold out, man."))
        guildmember = Population(_("guild members"), "guild member.webp", 110, range = 30, rank=3, effects=[Effect("change", "masseuse preference", 15), Effect("change", "fetish preference", 15)], base_description=__("Guild members are like craftsmen, but craftier."))

        patrician = Population(_("patricians"), "patrician.webp", 110, range = 40, rank=3, effects=[Effect("special", "horny", 1), Effect("change", "satisfaction", -1)], base_description=__("Father figures to the community, ready to meet young girls with daddy issues."))

        aristocrat = Population(_("aristocrats"), "aristocrat.webp", 135, range = 40, rank=4, effects=[Effect("boost", "crazy", 1.5), Effect("change", "satisfaction", -1)], base_description=__("Above the law. Entitled AF. Filthy rich. What's not to like?"))
        noble = Population(_("nobles"), "noble.webp", 160, range = 40, rank=4, effects=[Effect("change", "satisfaction", -2)], base_description=__("Nobles are easily bored. Living a life of privilege isn't all fun and games, it's also yawns."))

        royal = Population(_("royals"), "royal.webp", 200, range = 50, rank=5, effects=[Effect("change", "satisfaction", -3)], base_description=__("People say royals are jaded, undeserving narcissistic parasites. No one gives them credit for how generous they are with their subjects' money. Sad."))

        all_populations = [beggar, thug, laborer, sailor, commoner, craftsman, bourgeois, guildmember, patrician, aristocrat, noble, royal]

        # LOCATIONS # Locations should have been in a dictionary from the start, but it's messy. Sorry.

        spice_market = Location(_("Spice market"), pic = "Spice market.webp")
        sewers = Location(_("Sewers"), pic = "Sewers.webp", menu = (_("Visit the monster catcher"), "visit_willow"), menu_costs_AP=False) # Monster merchant
        farmland = Location(_("Farm"), pic = "farmland.webp", menu = (_("Visit the rancher"), "visit_goldie"), menu_costs_AP=False) # Beast merchant
        watchtower = Location(_("Watchtower"), pic = "Watchtower.webp", menu = (_("Browse the Captain's vault"), "visit_watchtower"))
        junkyard = Location(_("Junkyard"), pic = "Junkyard.webp", menu = (_("Visit the scientist"), "visit_gina"), menu_costs_AP=False) # Machine merchant
        thieves_guild = Location(_("Thieves guild"), pic = "Thieves guild.webp", secret = True, menu = (_("Browse the guild warehouse"), "visit_thieves_guild"))

        harbor = Location(_("Harbor"), pic = "Harbor.webp", menu = (_("Visit the headmaster"), "visit_stella"), menu_costs_AP=False) # Stallion merchant
        shipyard = Location(_("Shipyard"), pic = "Shipyard.webp", menu = (_("Collect wood"), "collect_wood")) # Wood extraction
        taverns = Location(_("Taverns"), pic = "Taverns.webp")
        seafront = Location(_("Seafront"), pic = "Seafront.webp", menu = (_("Visit Papa Freak"), "visit_papa"), menu_costs_AP=False)
        beach = Location(_("Beach"), pic = "Beach.webp", menu = (_("Brew dye"), "collect_dye")) # Dye
        exotic_emporium = Location(_("Exotic emporium"), pic = "Exotic emporium.webp", menu = (_("Visit gift shop"), "visit_giftgirl"), menu_costs_AP=False) # Gift girl, gifts

        stables = Location(_("Stables"), pic = "Stables.webp", menu = (_("Get leather"), "collect_leather")) # Leather
        plaza = Location(_("Plaza"), pic = "Plaza.webp", menu = (_("Contact Homura"), "c3_contact_homura"), menu_costs_AP=False) # Homura, story
        market = Location(_("Market"), pic = "Market.webp", menu = (_("Visit the exchange"), "visit_exchange"), action=True, menu_costs_AP=False) # Resource market
        gallows = Location(_("Gallows"), pic = "Gallows.webp", menu = (_("Visit Papa Freak"), "visit_papa"), menu_costs_AP=False)
        prison = Location(_("Prison"), pic = "Prison.webp", menu = (_("Visit G's bazaar"), "visit_gurigura"), menu_costs_AP=False) # Gurigura, toys
        arena = Location(_("Arena"), pic = "Arena.webp", menu = (_("Visit weapon shop"), "visit_ramias"), menu_costs_AP=False) # Ramias, weapons

        botanical_garden = Location(_("Botanical garden"), pic = "Botanical garden.webp", menu = (_("Visit flower stall"), "visit_riche"), menu_costs_AP=False) # Riche, flowers
        hanging_gardens = Location(_("Hanging gardens"), pic = "Hanging gardens.webp", menu = (_("Weave silk"), "collect_silk")) # Silk
        # library = Location(_("Library"), pic = "Library.webp", menu = (_("Visit trinket shop"), "visit_katryn"), menu_costs_AP=False) # Katryn, trinkets
        magic_university = Location(_("Magic university"), pic = "magic_university.webp", menu = (_("Visit trinket shop"), "visit_katryn"), menu_costs_AP=False) # Katryn, trinkets
        guild_quarter = Location(_("Guild quarter"), pic = "Guild quarter.webp", menu = (_("Smuggle ore"), "collect_ore")) # Ore
        magic_guild = Location(_("Magic guild"), pic = "Magic guild.webp")
        magic_forest = Location(_("Magic forest"), pic = "Magic forest.webp")

        pilgrim_road = Location(_("Pilgrim road"), pic = "Pilgrim road.webp", menu = (_("Visit tailor shop"), "visit_twins"), menu_costs_AP=False) # Twins, dresses
        banking_quarter = Location(_("Banking quarter"), pic = "Banking quarter.webp", menu = (_("Visit Bank"), "visit_bank"), action=True, menu_costs_AP=False)
        old_ruins = Location(_("Old ruins"), pic = "Ruins.webp", menu = (_("Extract marble"), "collect_marble")) # Marble
        lake = Location(_("Lakefront"), pic = "Lake.webp")
        training_ground = Location(_("Training ground"), pic = "Training ground.webp")
        cathedra = Location(_("Cathedra"), pic = "Cathedra.webp")

        battlements = Location(_("Battlements"), pic = "Battlements.webp")
        keep = Location(_("Keep"), pic = "Keep.webp")
        hall = Location(_("Hall"), pic = "Hall.webp")
        courtyard = Location(_("Courtyard"), pic = "Courtyard.webp")
        temple = Location(_("Temple"), pic = "Temple.webp")
        falls = Location(_("Waterfalls"), pic = "Falls.webp", menu = (_("Look for diamonds"), "collect_diamond")) # Diamonds

        location_dict = {# Districts
                        "The Slums" : [spice_market, sewers, farmland, watchtower, junkyard, thieves_guild],
                        "The Docks" : [harbor, shipyard, seafront, beach, taverns, exotic_emporium],
                        "The Warehouse" : [market, stables, plaza, gallows, prison, arena],
                        "The Magic Gardens" : [botanical_garden, magic_university, magic_forest, hanging_gardens, guild_quarter, magic_guild],
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
                        "Magic university" : magic_university,
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

        court_locations = ["magic university", "magic guild", "cathedra", "keep", "hall", "temple"]

        all_locations = location_dict["The Slums"] + location_dict["The Docks"] + location_dict["The Warehouse"] + location_dict["The Magic Gardens"] + location_dict["The Cathedra"] + location_dict["The King's Hold"]

        # DISTRICT LIST #

        district_dict = {
                "slum" : District(_("The Slums"), 1, 1, 15, ((beggar, 80), (thug, 20)), pic = "districts/slums.webp", description = __("The Slums are located on the outskirts of Zan, beyond the defensive wall. It is home to the Zani rabble: new arrivals, refugees, paupers, spice addicts... It is also rumored to host the hideout of the Thieves Guild, who worship the Shadow Goddess Shalia.")),
                "docks" : District(_("The Docks"), 2, 2, 40, ((thug, 10), (laborer, 10), (sailor, 40), (commoner, 25), (craftsman, 15)), room = ["tavern"], pic = "districts/docks.webp", description = __("The docks are home to rowdy sailors and dodgy pirates sheltering from the treacherous seas. With seamen all around, no wonder there is a thriving market for cheap whores near the port.")),
                "warehouse" : District(_("The Warehouse"), 2, 2, 40, ((thug, 10), (laborer, 20), (sailor, 20), (commoner, 30), (craftsman, 20)), ["strip club"], pic = "districts/warehouse.webp", description = __("The warehouse is the industrial part of Zan, where all kinds of craftsmen and day laborer come to look for work. Its streets are buzzing with trade and activities during the day, but dodgy at night.")),
                "gardens" : District(_("The Magic Gardens"), 4, 3, 100, ((commoner, 5), (craftsman, 15), (bourgeois, 30), (guildmember, 30), (patrician, 20)), ["onsen"], pic = "districts/gardens.webp", description = __("The gardens are where the magic-wielding locals gather to soak up mana after a long night of dangerous experiments. It is said some of those experiments occasionally escape...")),
                "cathedra" : District(_("The Cathedra"), 4, 3, 100, ((commoner, 5), (craftsman, 10), (bourgeois, 20), (guildmember, 35), (patrician, 30)), ["okiya"], pic = "districts/cathedra.webp", description = __("The Cathedra is the holy center of the Arios order. Pilgrims, knights and priests rub elbows during prayers and rituals, while savvy merchants and bankers make a killing providing them with expensive service.")),
                "hold" : District(_("The King's Hold"), 6, 4, 150, ((patrician, 20), (aristocrat, 50), (noble, 30)), "free", pic = "districts/final castle night.webp", description = __("This is the center of power in Zan, where courtiers compete for power and the King's support. Behind the veneer of respectability and privilege, however, daggers are drawn... Beware."))
                }

        endless_district = District(_("The King's Hold"), chapter=7, rank = 5, diff = 200, pop = ((royal, 100),), room = ["tavern", "strip club", "onsen", "okiya"], pic = "districts/final castle.webp", description = __("This is the center of power in Zan, where courtiers compete for power and the King's support. Behind the veneer of respectability and privilege, however, daggers are drawn... Beware."))

        all_districts = [district_dict[d] for d in ["slum", "warehouse", "docks", "gardens", "cathedra", "hold"]]

        # # CREATE FIRST DISTRICT #

        # district = district_dict["slum"]

    #### SPELLS ####

    call init_spells() from _call_init_spells

    #### GIRLS ####

    # # TRAITS & PERKS # Moved to before_main_menu
    #
    # call init_traits() from _call_init_traits
    # call init_perks() from _call_init_perks


    # SEX ACTS #
    python:
        anal = Sexact(0.2, 1.25)
        sex = Sexact(0.5, 1.0)
        service = Sexact(0.4, 1.0)
        fetish = Sexact(0.1, 1.5)


    # CREATE SLAVEMARKET #
        slavemarket = NPC()
        slavemarket.active = True


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

        minion_merchants = [NPC_goldie, NPC_willow, NPC_gina, NPC_stella]

        # Equip magic notebook (temp)
        MC.items.append(magic_notebook)
        MC.equip(magic_notebook)


        # INIT TAXES

        init_tax()

        # #### NO STORY ####

        # if debug_mode or not story_mode:
        #     farm.activate()
        #     farm_firstvisit = False
        #     gizel_name = "Gizel"

        #     harbor.action = True
        #     stella_name = "Stella"
        #     farmland.action = True
        #     goldie_name = "Goldie"
        #     sewers.action = True
        #     willow_name = "Willow"
        #     junkyard.action = True
        #     gina_name = "Gina"

        #     unlocked_shops += [NPC_goldie, NPC_willow, NPC_gina]

        #     thieves_guild.secret = False
        #     if c1_path == "good":
        #         thieves_guild.action = False
        #     elif c1_path == "neutral":
        #         thieves_guild.action = True
        #     elif c1_path == "evil":
        #         thieves_guild.action = False
        #         watchtower.action = True

        #     renza_name = "Renza"
        #     captain_name = "Farah"

        #     story_flags["found wagon"] = True
        #     story_flags["met carpenter"] = True
        #     carpenter_name = "Iulia"

        #     shipyard.action = True # Wood
        #     stables.action = True # Leather
        #     beach.action = True # Dye
        #     old_ruins.action = True # Stone
        #     hanging_gardens.action = True # Silk
        #     guild_quarter.action = True # Ore
        #     falls.action = True # Diamond


    #### QUESTS AND CLASSES ####

    call init_postings() from _call_init_postings

    # CREATE POSTING BOARD #
    python:
        quest_board = NPC()
        load_quest_pics()

    # CREATE CONTRACT TEMPLATES

        contract_templates = [
                    Contract(type="cruise", district="The Docks", archetypes = ["The Player", "The Fox"],
                            names=["A Night At Sea", "Touring Zan's Bay", "The Retired Sailor", "A Fancy Cruise"],
                            organizers=["the rowdy sailor fraternity", "Zan's navy", "the flibusteer social club", "the Northern merchant navy"],
                            venues=["refitted galleon", "private junk", "princely yacht", "fleet of small fishing boats", "large tour boat"],
                            character=young_sailor,
                            MC_event_pic="events/brawl3.webp",
                            ),
                    Contract(type="party", district="The Cathedra", archetypes = ["The Maid", "The Slut"],
                            names=["Party Hard", "All-Nighter by The Cathedra", "Shameless Party", "From Dusk Till Dawn", "Blackjack Tables, and Hookers", "Dude, Where's My Cart?"],
                            organizers=["a foreign dignitary", "a wealthy patrician family", "an interguild association", "a visiting High Mage of Karkyr", "a close advisor of the king", "a wealthy brothel master", "the House of Lannister"],
                            venues=["abandonned church", "famous okiya", "fancy palace", "seedy tavern", "underground casino"],
                            character=party_girl,
                            MC_event_pic="events/violent2.webp",
                            ),
                    Contract(type="ceremony", district="The Cathedra", archetypes = ["The Model", "The Bride"],
                            names=["A Holy Affair", "A Religious Festival", "The Saintly Ceremony", "A Most Holy Gathering", "After The Prayer"],
                            organizers=["The Holy Church of Arios", "The Nuns of Saint Dil d'Oh", "The Enlightened Brothers", "The Pious Fraternity", "The Friends of Shalia", "The Ol' Gods Alliance", "The Worshippers of the Unspeakable Yog'Gluglu", "The Priestesses of Arios"],
                            venues=["large convent", "venerable cathedral", "isolated monastery", "quiet retreat", "forgotten temple", "glorious church", "destitute orphanage"],
                            character=nun,
                            MC_event_pic="events/monster assault.webp",
                            ),
                    Contract(type="festival", district="The Slums", archetypes = ["The Player", "The Fox"],
                            names=["The Moonlight Festival", "A Country Festival", "Season's Greetings", "The Countryside Fair", "The Farmers Market", "A Prized Tradition"],
                            organizers=["The Bumpkin Pumpkins", "The Farmers Guild", "Zan's Country Club", "The Gardening Brotherhood", "The Landlords Cooperative", "Dirty hippies from the Valley", "The Union of Goat-Herders"],
                            venues=["former junkyard", "large plaza", "market square", "city gate", "main roadside"],
                            character=kimono_lady,
                            MC_event_pic="default/farm/sex beast (7).webp",
                            ),
                    Contract(type="date", district="The Magic Gardens", archetypes = ["The Bride", "The Model"],
                            names=["A Romantic Date", "The Lonely Gentleman", "The Lord's Penthouse", "Pretty Woman"],
                            organizers=["Calif Bretznah", "High Priest Ronan", "Lord Nabukov", "Master Rhi-Seung", "Count Dicku", "The Pink Baron", "Duke Nukem", "Guild Master Felix"],
                            character=young_maid,
                            venues=["luxurious penthouse", "big country house", "old mansion", "family palace", "private temple", "popular resort"],
                            MC_event_pic="NPC/encounters/thief4.webp",
                            ),
                    Contract(type="meeting", district="The Warehouse", archetypes = ["The Courtesan", "The Maid"],
                            names=["A Strategic Meeting", "A Show of Power", "A Political Reunion", "A Momentous Occasion", "A Pompous Conference"],
                            organizers=["The Zanic City Council", "The Rebel Alliance", "The government of His Majesty's King Pharo the 1st", "The Knights of the Oddly-Shaped Table", "The Blood-Island Coalition"],
                            venues=["progress in the Holy War", "military cooperation", "freer sex slave trading", "new fishery regulations", "limits on magic weapon stockpiles", "lowering taxes for the noble-born", "raising taxes on the poor and destitute"], # Different use for venue for this particular contract
                            character=diplomat,
                            MC_event_pic="NPC/encounters/thief2.webp", #impress1_5.webp / quests/sex9.webp
                            ),
                    Contract(type="magic", district="The Magic Gardens", archetypes = ["The Escort", "The Courtesan"],
                            names=["Magic: The Gathering", "The Wizard Annual Convention", "The Magical Science Fair", "Fun at the Magic Guild", "Magic Schools Face-Off", "Witch Please"],
                            organizers=["High Mage Windzoss", "The Union of Concerned Sorceresses", "The Necromancer Social Club", "The Elders of Karkyr", "The Friendly Neighborhood Dark Cultists"],
                            venues=["haunted manor", "creepy old house", "high tower", "underground lair", "recently-opened demonic plane", "dusty library"],
                            character=sorceress,
                            MC_event_pic="NPC/encounters/witches (1).webp",
                            ),
                    Contract(type="orgy", district="The King's Hold", archetypes = ["The Slut", "The Escort"],
                            names=["Orgy Night", "Sleazy Party", "Ready To Mingle", "Bachelors Day Out", "A Night Of Dirty Fun"],
                            organizers=["Mistress Smutty Kitty", "Brothel Master Quinn", "High Priest Ronan", "The Arios Nun Choir", "The Gimp", "The Hooker Trade Union", "An anonymous member of the royal family", "A rich businessman", "A noble lady"],
                            venues=["mysterious forest clearing", "gipsy camp", "dark dungeon", "decadent palace", "smutty tavern", "hidden basement", "forgotten temple"],
                            character=naked_lady,
                            MC_event_pic="NPC/encounters/ev_onsens2.webp",
                            ),
                            ]


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
                "c3_narika_MU_class" : StoryEvent(label = "c3_narika_MU_class", type = "morning", once=False),
                "narika_break_test" : StoryEvent(label = "narika_break_test", type="night", once=False),
                "haruka_break_test" : StoryEvent(label = "haruka_break_test", type="morning", once=False),

                "meet_gurigura" : StoryEvent(label = "meet_gurigura", location = "prison", order=1),
                "meet_ramias" : StoryEvent(label = "meet_ramias", location = "arena", order=1),
                "meet_katryn" : StoryEvent(label = "meet_katryn", location = "magic university", order=1),
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
                "MU_jobgirl" : StoryEvent(label = "MU_jobgirl", location="Magic guild", once=False),

                "stella_invitation" : StoryEvent(label = "stella_invitation", chance = 0.05, chapter=4),
                "stella_secret1" : StoryEvent(label = "stella_secret1", location="guild quarter", condition_func=is_first_tuesday),
                "stella_secret2" : StoryEvent(label = "stella_secret2", location="guild quarter", condition_func=is_first_tuesday, once=False),

                "slave_beach_event" : StoryEvent(label = "slave_beach_event", locations=beach_locations, seasons=["spring", "summer"], condition_func=slave_beach_event_happens, once=False),

                }

    # # REGISTER EVENTS

    # call init_events() from _call_init_events_1


    # NG+ Settings init

    $ NGP_settings = [ # Types: gold, resources, int, bool, plus, boost, dispenser, item, pref, girl
        NGPSetting(_("starting chapter"), "int", label="Headstart", values = range(1, 8), cost=[10*i for i in range(2, 8)], ttip=__("The chapter you will start the game at. Not compatible with challenges such as the free girl challenge.")),

        NGPSetting(_("starting gold"), "gold", label="Savings", values = [5, 15, 100, 999], cost = [2, 3, 4, 5], ttip=__("The amount of money you will start the game with (default: {image=img_gold} [starting_gold]).")),
        NGPSetting(_("starting resources"), "resources", label="Resourceful", values= [20, 10, 5], cost = [15, 20, 25], ttip=__("Start the game with extra resources.")),
        NGPSetting(_("extractors Mk I"), "int", label="Capitalist I", values= range(1, 4), cost = [25, 50, 75], ttip=__("Start the game with resource extractors Mk I.")),
        NGPSetting(_("extractors Mk II"), "int", label="Capitalist II", values= range(1, 4), cost = [35, 70, 105], ttip=__("Start the game with resource extractors Mk II.")),

        NGPSetting(_("farm"), "bool", label="Farm key", cost = 10, ttip=__("Unlock Gizel and the Farm from the beginning of the game.")),
        NGPSetting(_("carpenter"), "bool", label="Carpenter wagon", cost = 10, ttip=__("Unlock Iulia the Carpenter from the beginning of the game.")),
        NGPSetting(_("minion merchants"), "bool", label="Merchant connections (minions)", cost = 25, ttip=__("Unlock Stella, Goldie, Willow and Gina from the beginning of the game.")),
        NGPSetting(_("item merchants"), "bool", label="Merchant connections (items)", cost = 100, ttip=__("Unlock Riche, Ramias, Gurigura, Katryn, the twins and the Giftshop girl from the beginning of the game.")),
        NGPSetting(_("all trainers"), "bool", label="All trainers", cost = 100, ttip=__("Unlock all trainers from the beginning of the game.")),

        NGPSetting(_("strength"), "plus", label="Strong", values= [1, 2, 3], cost = [15, 30, 45], ttip=__("Increase your character's Strength and Strength maximum beyond its base value (up to +3).")),
        NGPSetting(_("spirit"), "plus", label="Wise", values= [1, 2, 3], cost = [15, 30, 45], ttip=__("Increase your character's Spirit and Spirit maximum beyond its base value (up to +3).")),
        NGPSetting(_("charisma"), "plus", label="Funny", values= [1, 2, 3], cost = [15, 30, 45], ttip=__("Increase your character's Charisma and Charisma maximum beyond its base value (up to +3).")),
        NGPSetting(_("speed"), "plus", label="Quick", values= [1, 2, 3], cost = [30, 60, 90], ttip=__("Increase your character's Speed and Speed maximum beyond its base value (up to +3).")),

        NGPSetting(_("good alignment"), "bool", label="Nice guy", cost = 5, ttip=__("Start the game as a good person.")),
        NGPSetting(_("evil alignment"), "bool", label="Bad boy", cost = 5, ttip=__("Start the game as an evil person.")),
        # NGPSetting(_("polytheist"), "bool", label="Polytheist", cost = 15, ttip=__("Unlock all deities and atheist story lines.")),
        # NGPSetting(_("multiclass"))
        # NGPSetting(_("new events"))

        NGPSetting(_("love generation"), "boost", label="Gangster of love", values= [0.25, 0.5, 1.0], cost = [10, 25, 50], ttip=__("Gain love faster with slaves and free girls. Some people call you 'Maurice'.")),
        NGPSetting(_("fear generation"), "boost", label="Actual gangster", values= [0.25, 0.5, 1.0], cost = [5, 15, 30], ttip=__("Gain fear faster with slaves.")),
        NGPSetting(_("xp generation"), "boost", label="XP trainer", values= [0.25, 0.5, 1.0], cost = [5, 15, 45], ttip=__("Girls will gain XP faster.")),
        NGPSetting(_("jp generation"), "boost", label="JP trainer", values= [0.25, 0.5, 1.0], cost = [5, 10, 30], ttip=__("Girls will gain JP faster.")),
        NGPSetting(_("prestige generation"), "boost", label="Prestigious", values= [0.25, 0.5, 1.0], cost = [5, 15, 45], ttip=__("MC will earn Prestige faster.")),
        NGPSetting(_("training efficiency"), "boost", label="Experienced", values= [0.5, 1.0, 2.0], cost = [15, 30, 60], ttip=__("Train your girls significantly faster.")),

        NGPSetting(_("tax reduction"), "boost", label="Tax evasion", values= [0.15, 0.3, 0.5], cost = [50, 100, 150], ttip=__("Reduce your taxes thanks to the judicious application of offshore finance, political donations and elaborate voodoo curses.")),

        NGPSetting(_("free girl"), "dispenser", label="Young chemist", cost = [5, 20, 40], ttip=__("Produce Potions of Seduction (raises the relationship level with any free girl by one step).")),
        NGPSetting(_("virginity"), "dispenser", label="Young surgeon", cost = [10, 50, 100], ttip=__("Produce Balms of Restoration (restores a girl's virginity).")),
        NGPSetting(_("sanity"), "dispenser", label="Young therapist", cost = [10, 50, 100], ttip=__("Produce Incense of Bliss (restores some of a girl's sanity).")),
        NGPSetting(_("interactions"), "dispenser", label="Young drug lord", cost = [5, 20, 40], ttip=__("Produce Magic Powder (regain all AP).")),
        NGPSetting(_("perks"), "dispenser", label="Wyvern nest", cost = [25, 100, 250], ttip=__("Produce Wyvern eggs (+1 Perk points).")),

        NGPSetting(_("autorest"), "bool", label="Autorest", cost = 10, ttip=__("Receive a Vitals Scanner from the beginning of the game, allowing you to use autorest.")),
        NGPSetting(_("personality"), "item", label="Personality reader", cost = [10, 20], ttip=__("Receive additional information on a girl's personality in your journal.")),
        NGPSetting(_("taste"), "item", label="Taste reader", cost = [5, 15], ttip=__("Receive additional information on a girl's tastes in your journal.")),
        NGPSetting(_("fixation"), "item", label="Fixation reader", cost = [5, 25], ttip=__("Receive additional information on a girl's sexual preferences in your journal.")),

        NGPSetting(_("naturist frequency"), "boost", label="Hippie", values= [8, 16, 32], cost = [5, 10, 20], ttip=__("Increase the frequency of the 'Naturist' trait for all girls.")),
        # NGPSetting(_("portal"), "special", label="Portal", cost = 0, ttip=__("Unlock the girl portal early.")),
        NGPSetting(_("preferences1"), "pref", label="Naked/Service preferences", values= [125, 250, 500], cost = [5, 15, 30], ttip=__("Increase base sexual preferences for Naked and Service for all girls.")),
        NGPSetting(_("preferences2"), "pref", label="Sex/Anal preferences", values= [125, 250, 500], cost = [10, 25, 50], ttip=__("Increase base sexual preferences for Sex and Anal for all girls.")),
        NGPSetting(_("preferences3"), "pref", label="Fetish/Bisexual/Group preferences", values= [125, 250, 500], cost = [15, 35, 70], ttip=__("Increase base sexual preferences for Fetish, Bisexual and Group for all girls.")),

        NGPSetting(_("girl"), "girl rank", label="Starting girl", values= [2, 3, 4], cost = [50, 100, 200], ttip=__("Receive a free girl at the start with random stats.")),

        NGPSetting(_("free girl challenge"), "bool", label="Free girl challenge", cost = 50, ttip=__("Receive a new girl at the start of each month. The slavemarket will become inaccessible. Worth 100 crystals if you complete the game.")),
        NGPSetting(_("training challenge"), "bool", label="No training challenge", cost = 50, ttip=__("The Farm becomes much more efficient, but you can no longer personally train your girls. Worth 200 crystals if you complete the game.")),
        ]

    $ NGP_settings_dict = {v.name : v for v in NGP_settings}

    return


label init_events(chapter=1):

    # Reminder: story_add_event type can be either 'city' (default) or 'daily'

    python:
        ## 1. GENERIC EVENTS ##

        # CONTRACTS #
        story_add_event("new_contract", "daily")
        story_add_event("run_contract", "daily")
        story_add_event("bis_introduction", "daily")
        story_add_event("group_introduction", "daily")
        story_add_event("advertising_intro", "daily")

        # TAXES #
        story_add_event("tax_check", "daily")
        story_add_event("tax_payment", "daily")

        # RESOURCES #
        for res in build_resources:
            story_add_event(res + "_intro")

        # MISC #
        calendar.set_alarm(333, Event(label = "hmas"))
        story_add_event("slave_beach_event", "city")

        ## 2. CHAPTER EVENTS ##
        
        if story_mode and not debug_mode:
            # TUTORIAL #
            daily_events.append(event_dict["zodiac_intro"])
            
            if chapter <= 1:

                # STORY #
                calendar.set_alarm(3, Event(label = "c1_gio_is_back"))
                calendar.set_alarm(5, Event(label = "c1_meet_kosmo"))
                calendar.set_alarm(8, Event(label = "c1_ambush"))
                story_add_event("c1_thieves_guild_tip", "city")
                story_add_event("farm_meet_gizel")
                story_add_event("farm_meet_goldie")

            if chapter <= 2:
                story_add_event("c2_meet_carpenter")

    return

#### END OF BK START FILE ####
