####         SETTINGS           ####################################################
##    Those are the settings      ##################################################
##    that can be easily edited   ##################################################
##    by players in Bro King      ##################################################


init -10 python:

#### GIRLS FOLDER/GIRL PACKS ####

    girl_directories = ["girls/", ] # You can specify one or more directories containing girl packs. The 'game' folder is the root folder

#### CONFIG & PERFORMANCE ####

    ## Picture caching. Set lower values if you have memory problems. Use only one setting, comment the other out with the # symbol.

    config.image_cache_size = 144 # Set this higher for better performance (will use more RAM)
#     config.image_cache_size_mb = 500 # You may use this instead of config.image_cache_size. Set this higher for better performance (will use more RAM)

    refresh_memory_on_home_screen = False # Change to True if you want more frequent memory refresh. May help on lower-end computers

    ## Auto-save.

    config.has_autosave = True # Auto-save is enabled by default. The game will save every night before pressing end-day.
    config.autosave_frequency = 200 # The game will also auto-save after n messages have been shown (during long events)
    save_every_x_days = 2 # The frequency with which an end-day save is done (1=every day, 2=every 2 days, and so on)
    config.autosave_slots = 12
    config.autosave_on_choice = False
    config.autosave_on_quit = False

    config.developer = True

    # Maximum number of items shown (change this if you are having performance issues with large inventories)
    max_item_shown = 30

#### TRANSLATION OPTIONS ####

    ## Edit this dictionary to change the stat names that are displayed (change the right-hand text)

    stat_name_dict = {
                        "Beauty" : "Beauty",
                        "Body" : "Body",
                        "Charm" : "Charm",
                        "Refinement" : "Refinement",
                        "Sensitivity" : "Sensitivity",
                        "Libido" : "Libido",
                        "Constitution" : "Constitution",
                        "Obedience" : "Obedience",
                        "Service" : "Service",
                        "Sex" : "Sex",
                        "Anal" : "Anal",
                        "Fetish" : "Fetish",
                        "Energy" : "Energy",
                    }

#### BALANCE / CHEATS ####

    debug = True # Replace this with 'True' for additional cheats and information (recommended for testing)

    cheat_modifier = { # Set it at 1.0 for normal play
                        "gold" : 1.0,
                        "stats" : 1.0,
                        "xp" : 1.0,
                        "jp" : 1.0,
                        "rep" : 1.0,
                        "prestige" : 1.0
                    }

    ## STARTING TRAITS

    prefer_original_girls = False # Set this to True to always generate original (gold-trait) girls first. Default is False.

    use_ini_skills = True # If set to True, this will use values specified in _BK.ini files to generate skill values.
    use_ini_traits = True # If set to True, this will use values specified in _BK.ini files to generate trait values.
    use_ini_personality = True # If set to True, this will use values specified in _BK.ini files to generate personality values.
    use_ini_sex = True # If set to True, this will use values specified in _BK.ini files to generate sexual preferences values.

    starting_traits_gold = 0 # Original girls will receive this plus 1 gold trait(s)
    starting_traits_positive = 2 # Number of positive traits, except gold traits
    starting_traits_negative = 1

    ## SEX ACTS

    whore_test = 50 ## Minimum value of Obedience + Libido to become a whore

    sex_act_test = {
                    "service" : (("libido", 15), ("obedience", 15)), ## Minimum values to perform a given sex act (even if those values are reached, a girl should still be trained before whe will accept anything)
                    "sex" : (("libido", 25), ("obedience", 25),),
                    "anal" : (("libido", 35),),
                    "fetish" : (("obedience", 35),)
                    }

    bis_chance = 0.5 # This is the base chance for Bisexual to trigger, if active
    group_chance = 0.5 # This is the base chance for Group to trigger, if active

    ## BROTHEL SETTINGS
    # For each chapter: the first number between brackets is the minimum number of bedrooms (and therefore girls), the second number is max.
    bro_capacity = {1 : [1, 4], 2 : [4, 8], 3: [8, 12], 4 : [12, 16], 5 : [16, 20], 6 : [20, 24], 7 : [24, 32]}

    # For each chapter: the maximum number of helpers (for advertising, security, and maintenance)
    bro_helpers = {1 : 8, 2 : 16, 3 : 24, 4 : 32, 5 : 40, 6 : 48, 7 : 64}

    # Reputation cap affects the maximum number of customers that can come before advertising and special effects. Each customer costs 10 pts of reputation * rank
    bro_reputation_cap = {1 : 80, 2 : 320, 3 : 480, 4 : 1200, 5 : 1560, 6 : 3040, 7 : 5800}

    ## CHAPTER GOALS

    # Goal types can be: 'gold', 'ranked', 'reputation', 'prestige'

    bro_cost = {1 : 0, 2 : 1000, 3: 5000, 4 : 7500, 5 : 15000, 6 : 25000, 7 : 100000}

    chapter_goals = {
                    1 : [Goal("gold", bro_cost[2])],
                    2 : [Goal("gold", bro_cost[3])],
                    3 : [Goal("ranked", 2, 6), Goal("gold", bro_cost[4])],
                    4 : [Goal("ranked", 3, 8), Goal("gold", bro_cost[5])],
                    5 : [Goal("ranked", 3, 12), Goal("gold", bro_cost[6])],
                    6 : [Goal("ranked", 4, 12), Goal("gold", bro_cost[7])],
                    7 : [Goal(None, channel="other")],
                    }

    ## CUSTOMER CAPACITY

    # The formula for calculating customer capacity is: base_customer + (main_stat + constitution) // customer_points
    # Main stat is: Beauty, Body, Charm or Refinement for jobs, Libido for whores
    # This values are halved if the girl works half-time
    # You can edit those values here.

    job_base_customer = 2
    job_customer_points = 50

    whore_base_customer = 1
    whore_customer_points = 100


    ## CUSTOMER PREFERENCES

    customer_cap_multiplier = 3 # Multiplies customer difficulty to calculate customer max money (base modifier, advertising improves it)

    customer_base_preference = {
    # This is the base chance (in %) for a customer to want specific entertainment
                                "waitress" : 25,
                                "dancer" : 25,
                                "masseuse" : 25,
                                "geisha" : 25,

    # This is the base chance (in %) for a customer to want a specific sex act
                                "service" : 30,
                                "sex" : 35,
                                "anal" : 20,
                                "fetish" : 15,
                                }


    ## ADVERTISING ##

    # Advertising power is based in furniture level (outfits). Settings have been grouped here for ease of access.
    # 'reputation' is how many reputation points are earned every night per advertising girl.
    # 'customer attraction' is how many additional customer points are added every night per advertising girl.
    # 'customer budget' is by how much additional customer budget can be increased with the maximum number of advertising girls.



    advertising_settings = {
                            0 : {
                                "reputation" : 0.5,
                                "customer attraction" : 0.5, "min customer attraction" : 0.5, "max customer attraction" : 0.5,
                                "customer budget" : 0.5, "min customer budget" : 0.5, "max customer budget" : 0.5,
                                },
                            1 : {
                                "reputation" : 0.5,
                                "customer attraction" : 1, "min customer attraction" : 0.75, "max customer attraction" : 1.25,
                                "customer budget" : 1.0, "min customer budget" : 0.75, "max customer budget" : 1.25,
                                },
                            2 : {
                                "reputation" : 1,
                                "customer attraction" : 1.5, "min customer attraction" : 1, "max customer attraction" : 2,
                                "customer budget" : 2.0, "min customer budget" : 1.5, "max customer budget" : 2.5,
                                },

                            # Min/max settings involve trade-offs between customer attraction and customer budget. They become available at chapter 3.

                            3 : {
                                "reputation" : 1,
                                "customer attraction" : 2, "min customer attraction" : 1, "max customer attraction" : 4,
                                "customer budget" : 2.5, "min customer budget" : 1.0, "max customer budget" : 3.5,
                                },
                            4 : {
                                "reputation" : 1.5,
                                "customer attraction" : 2.5, "min customer attraction" : 1, "max customer attraction" : 5,
                                "customer budget" : 3.0, "min customer budget" : 1.0, "max customer budget" : 5.5
                                },
                            5 : {
                                "reputation" : 1.5,
                                "customer attraction" : 3, "min customer attraction" : 1, "max customer attraction" : 6,
                                "customer budget" : 3.5, "min customer budget" : 1.5, "max customer budget" : 7.5
                                },
                            6 : {
                                "reputation" : 2,
                                "customer attraction" : 4.0, "min customer attraction" : 1, "max customer attraction" : 8,
                                "customer budget" : 4.0, "min customer budget" : 1.5, "max customer budget" : 9.5
                                },
                            7 : {
                                "reputation" : 2.5,
                                "customer attraction" : 5, "min customer attraction" : 1, "max customer attraction" : 10,
                                "customer budget" : 5.0, "min customer budget" : 2.0, "max customer budget" : 12.0
                                },
                            }

    # Reputation decays faster at higher chapters
    reputation_decay = {1 : 0.0, 2 : -0.01, 3 : -0.02, 4 : -0.03, 5 : -0.04, 6 : -0.05, 7 : -0.06}

    ## GOLD ##

    starting_gold = 500

    # Tip formula (simplified): (tip_base * district.rank^2 + sum(customer difficulty)) * result_modifier * job_modifier * cheat_modifier

    tip_base = 10

    tip_result_modifier = {             # Whores have higher tips for good results, but lower for bad results
                "job very bad" : 0.75,
                "job bad" : 0.9,
                "job average" : 1.0,
                "job good" : 1.2,
                "job very good" :1.35,
                "job perfect" : 1.55,
                "whore very bad" : 0.35, # 0.6,
                "whore bad" : 0.7, # 0.8,
                "whore average" : 1.0,
                "whore good" : 1.25,
                "whore very good" :1.5,
                "whore perfect" : 1.75,
                }

    tip_act_modifier = {
                    "anal" : 1.15,
                    "sex" : 1.1,
                    "service" : 1.05,
                    "fetish" : 1.2,
                    "waitress" : 1.0,
                    "dancer" : 1.0,
                    "masseuse" : 1.0,
                    "geisha" : 1.0,
                    "naked bonus" : 1.05, # Bonus for when the girl is working naked (not whoring).
                    "bisexual bonus" : 0.85, # Applies to each girl
                    "group bonus" : 0.7, # Applies to each customer
                    }

    sell_girl_preference_boost = 0.01 / 100 # Girl sell price increases or decreases by 1% for every +/- 100 points of preference

    ## GUILD TAX ##

    tax_brackets = [(500, 0), (1000, 0.1), (2000, 0.15), (4000, 0.2), (8000, 0.25), (16000, 0.3), (32000, 0.35), (64000, 0.4), (128000, 0.45), (10**12, 0.5)] # For each (x, y): Up to x average daily net income, raw tax rate is y.

    tax_chapter_penalty = {1 : 0, 2 : 0.05, 3 : 0.075, 4 : 0.1,5 : 0.125, 6 : 0.15, 7 : 0.2} # Raw percentage is increased by this for each tax bracket except 0

    tax_time_pressure_maximum = 0.2 # The maximum time pressure tax modifier

    tax_random_range = 0.25 # The expected lump sum of money may vary by +/- this much every month

    ## XP ##

    xp_bonus_dict = {
            "very bad" : 0.5,
            "bad" : 0.75, #7.5,
            "average" : 1.0, #10,
            "good" : 1.25, #15,
            "very good" : 1.5, #20,
            "perfect" : 1.75 #35
            }


    ## SECURITY ##

    # The number next to each event type is the relative weight of a certain event happening at a given alert level
    security_events = {
                        1 : [("thief", 27), ("monster", 27), ("quiet", 6)],
                        2 : [("assassin", 27), ("brawl", 27), ("quiet", 6)],
                        3 : [("raid", 27), ("siege", 27), ("quiet", 6)],
                        }
    # Threshholds for events being blocked / reversed. These values might need some fine-tuning
    alert_limits1 = {1 : (5, 8), 2 : (6, 10), 3 : (8, 18), 4 : (10, 20), 5 : (12, 26), 6 : (14, 28), 7 : (18, 34)}
    alert_limits2 = {1 : (6, 10), 2 : (8, 12), 3 : (10, 20), 4 : (12, 22), 5 : (14, 28), 6 : (16, 30), 7 : (20, 36)}

    # Threshhold under which a girl may run away
    mood_runaway_limit = 10

    ## FREE GIRLS ##
    free_girls_per_district = 12 # The number of girls that will be generated per district unlocked


    ## SHOPS ##

    # Weekly shop item number is partly randomized. Shop inventory level can be improved with resources.

    shop_item_number = {
                        "shop" : {"junk" : "d3 + 3", "common" : "d6", "rare" : "d3", "exceptional" : "d3 + -2"}, # Negative numbers must be preceded by '+' to work properly
                        "city" : {"junk" : "d6", "common" : "d6 + 2", "rare" : "d3 + 1", "exceptional" : "d3 + -1"},
                        "minion" : {"minion" : "d5", "item" : "d4 + -1"},
                        }

    # Tweak costs and effects of restocking and upgrading inventory for each shop and chapter
    shop_restock_cost = {
                        "shop" : {2 : 500, 3 : 1000, 4 : 2000, 5 : 4000, 6 : 8000, 7 : 15000},
                        "city merchants" : {2 : 400, 3 : 800, 4 : 1600, 5 : 3200, 6 : 6400, 7 : 12000},
                        "minion merchants" : {2 : 400, 3 : 800, 4 : 1600, 5 : 3200, 6 : 6400, 7 : 12000},
                        }

    # Shop upgrades are stored with the following format: 'upgrade_order : [chapter, resource cost, additional stock]'
    shop_upgrades = {
                    1 : [2, ("wood", 5), ("junk", 2)],
                    2 : [2, ("dye", 10), ("common", 1)],
                    3 : [2, ("leather", 15), ("common", 1)],

                    4 : [3, ("dye", 20), ("rare", 1)],

                    5 : [4, ("ore", 10), ("junk", 2)],
                    6 : [4, ("silk", 15), ("common", 2)],
                    7 : [4, ("marble", 20), ("rare", 1)],

                    8 : [5, ("silk", 30), ("exceptional", 1)],

                    9 : [6, ("diamond", 5), ("rare", 1)],

                    10 : [7, ("diamond", 15), ("exceptional", 1)]
                    }

#### PICTURES #### Feel free to edit or add more

    nsfw = True # Warning: Turning this off is for debugging only; many pictures will remain uncensored, so watch out.

    stock_picture_threshold = 4 # Change this value to determine the limit under which stock pictures will be used alongside girl pack pictures (if the option is set in the H content menu)

    # Edit these weights to influence the related 'advanced training picture balance' preference settings
    fix_pic_balance_variety = {"act-based" : 0.5, "generic" : 0.5} # Generic pictures will be shown 50% of the time
    fix_pic_balance_accuracy = {"act-based" : 0.75, "generic" : 0.25} # Generic pictures will be shown 25% of the time

    brothel_pics = {1 : "1 slum brothel.webp",
                    2 : "2 town brothel.webp",
                    3 : "3 town brothel.webp",
                    4 : "4 rich brothel.webp",
                    5 : "5 rich brothel.webp",
                    6 : "6 king brothel.webp",
                    7 : "7 endless brothel.webp"
                    }

    room_pics = {
                # Common rooms
                "tavern" : "tavern.webp",
                "strip club" : "strip club.webp",
                "onsen" : "onsen.webp",
                "okiya" : "okiya.webp",
                # Bedrooms
                "Basic room" : "basic room1.webp",
                "+Basic room+" : "basic room2.webp",
                "*Basic room*" : "basic room3.webp",
                "Standard room" : "standard room1.webp",
                "+Standard room+" : "standard room2.webp",
                "*Standard room*" : "standard room3.webp",
                "Elegant room" : "rich room1.webp",
                "+Elegant room+" : "rich room2.webp",
                "*Elegant room*" : "rich room3.webp",
                "Noble suite" : "noble room1.webp",
                "+Royal suite+" : "noble room2.webp",
                "*Imperial suite*" : "noble room3.webp",
                # Master bedroom
                "Single room" : "master/master0.webp",
                "Double room" : "master/master1.webp",
                "Small suite" : "master/master2.webp",
                "Luxury suite" : "master/master3.webp",
                "Royal suite" : "master/master4.webp",
                "Royal harem" : "master/master5.webp",
                }

    night_pics = ["night.webp",]


    #! Temporary: New advertising pics will eventually be added
    advertising_pics = {1 : ["poster girls1.webp", "poster girls2.webp", "poster girls3.webp", "poster girls4.webp", "poster girls5.webp",
                        "poster girls6.webp", "poster girls7.webp", "poster girls8.webp", "poster girls9.webp", "poster girls10.webp",
                        "poster girls11.webp"]}

    advertising_pics[2] = advertising_pics[3] = advertising_pics[4] = advertising_pics[5] = advertising_pics[1]

    pony_pics = ["ponygirls.webp", "ponygirls (1).webp", "ponygirls (2).webp", "ponygirls (3).webp", "ponygirls (4).webp", "ponygirls (5).webp", "ponygirls (6).webp",]

    security_pics = {
                    "gooey monsters" : ["monster assault.webp",],
                    "rogue mercenaries" :  ["merc assault (1).webp", "merc assault (1).webp", "merc assault (2).webp"],
                    "marauding ogres" : ["ogre assault (1).webp", "ogre assault (3).webp", "ogre assault (2).webp"],
                    "monster rape" : ["monster (1).webp", "monster (1).webp", "monster (2).webp", "monster (2).webp", "monster (3).webp", "monster (4).webp", "monster (5).webp", "monster (6).webp", "monster (7).webp", "monster (8).webp", "monster (9).webp", "monster (10).webp", ],
                    "thief" : ["thief (1).webp", "thief (2).webp", "thief (3).webp", "thief (4).webp", "thief (5).webp", "thief (6).webp"],
                    "brothel defense" : ["brothel defense (1).webp", "brothel defense (2).webp"],
                    "monster defense" : ["monster defense (1).webp", "monster defense (2).webp"],
                    "thief defense" : ["thief captured (1).webp", "thief captured (2).webp", "thief captured (3).webp", "thief captured (4).webp", "thief captured (5).webp"],
                    "girl defense" : ["bar fight.webp"],
                    "girl shield" : ["shield.webp"],
                    "default girl fight" : ["fight1.webp", "fight2.webp", "fight3.webp", "fight4.webp"],
                    "assassin defense" : ["assassin1.webp", "assassin2.webp", "assassin3.webp", "assassin4.webp", "assassin5.webp", "assassin6.webp"],
                    "assassin" : ["assassin7.webp", "assassin8.webp", "assassin9.webp"],
                    "sword defense" : ["sword defense1.webp", "sword defense2.webp", "sword defense3.webp", "sword defense4.webp"],
                    "magic defense" : ["magic defense.webp"],
                    "dragon defense" : ["dragon defense.webp"],
                    "brawl" : ["bar fight.webp", "brawl1.webp", "brawl2.webp", "brawl3.webp"],
                    "siege" : ["hannies (5).webp", "siege2.webp", "siege3.webp", "siege4.webp", "siege5.webp", "siege6.webp", "siege7.webp"],
                    "hood" : ["hood.webp"],
                    "dark street" : ["dark street1.webp", "dark street2.webp"],
                    "alert" : ["alert1.webp", "alert2.webp", "alert3.webp"],
                    }

    arson_pics = ["arson1.webp", "arson2.webp", "arson3.webp", "arson4.webp"]
    violent_pics = ["violent.webp", "violent2.webp"]

    treasure_pics = {"+++" : ["treasure_blonde (3).webp", "treasure_pink (3).webp"], "++" : ["treasure_blonde (2).webp", "treasure_pink (2).webp"], "+" : ["treasure_blonde (1).webp", "treasure_pink (1).webp"], "-" : ["treasure_blonde (0).webp", "treasure_pink (0).webp"]}
    no_girls_pics = ["harem.webp",]

    playerclass_pics = {
                "Warrior" : "UI/warrior.webp",
                "Wizard" : "UI/wizard.webp",
                "Trader" : "UI/trader.webp"
                }

    god_pics = {
                "Arios" : "UI/arios.webp",
                "Shalia" : "UI/shalia.webp",
                None : "UI/none.webp"
                }

    alignment_pics = {
                "good" : "UI/al_good.webp",
                "evil" : "UI/al_evil.webp",
                "neutral" : "UI/al_neutral.webp"
                }


#### SOUND & MUSIC CHANNELS #### Defines music and sound directories

    ## The playlist can be freely edited. Make sure to drop the music in the 'Game\Music' folder

    playlist = ["553686_Emperors-Garden.ogg", "518978_Desert-Winds.ogg", "Cubis.ogg", "gnagna.ogg", "Guembriblues.ogg", "snake charmer.ogg", "Zurna.ogg",
                "Tibet.ogg", "Mimi.ogg", "infos-tapis.ogg", "Balkanissimo.ogg", "Balkano.ogg"]


    ## Channel declaration

    renpy.music.register_channel("music", mixer = "music", file_prefix = "music/")
    renpy.music.register_channel("sound", mixer = "sfx", file_prefix = "sounds/", loop = False)
    renpy.music.register_channel("sound2", mixer = "sfx", file_prefix = "sounds/", loop = False)
    renpy.music.register_channel("sound3", mixer = "sfx", file_prefix = "sounds/", loop = False)
    renpy.music.register_channel("video", mixer = "sfx")

    ## Music ## Shortcuts for music used in the game from the 'Game\Music' folder

    m_silence = "Silence.ogg"
    m_theme = "soaring dragon.ogg"
    m_theme_quiet = "drifting koi.ogg"
    m_oriental = "518978_Desert-Winds.ogg"
    m_market = "snake charmer.ogg"
    m_gizel = "Harp for the Devil.ogg"
    m_gio = "gnagna.ogg"
    m_jazz = "infos-tapis.ogg"
    m_rain = "light rain.ogg"
    m_mafia = "omerta.ogg"
    m_suspense = "risky path.ogg"
    m_short_suspense = "Tibet.ogg"
    m_wind = "wind.ogg"
    m_kosmo = "Zurna.ogg"
    m_freak = "Mimi.ogg"
    m_danger_loop = "538771_Your-Stalker.ogg"
    m_danger = "538771_Your-Stalker.ogg"
    m_knights = "595642_Realm-of-the-Forgot.ogg"
    m_tavern = "Abyss.ogg"
    m_evil = "Evil Ambiance-SoundBible.com-1774179982.ogg"
    m_nature = "Indian-Bird.ogg"
    m_satella = "Bonbon.ogg"
    m_shalia = "553759_Small-Moments.ogg"
    m_demons = "542049_Ravaged-By-Demons.ogg"
    m_disco = "579511_Real-Life-Disco-Loo.ogg"
    m_palace = "470178_Marching-Together.ogg"
    m_water = "waterfall.ogg"
    m_accordeon = "Balkano.ogg"
    m_zan = "553686_Emperors-Garden.ogg"
    m_action = "580741_Sunburn-Original-Mi.ogg"
    m_kenshin = "584589_Peaceful-Harmony.ogg"
    m_suzume = "587133_Shining-Star.ogg"
    m_kunoichi = m_narika = "public enemy no1.ogg"
    m_haruka = "Abyss.ogg"
    m_mizuki = "553759_Small-Moments.ogg"
    m_magicu = "Cubis.ogg"
    m_kids = "happy-114950.ogg"
    m_chaos = "Balkanissimo.ogg"

    ## Sounds ## Shortcuts for sound effects used in the game from the 'Game\Sounds' folder (warning: some sound effects paths are hard-coded, this will be cleaned up later)

    s_aah = "aah.ogg"
    s_aaah = s_aah
    s_sexy_sigh = "aaha.ogg"
    s_aaha = s_sexy_sigh
    s_ahaa = s_sexy_sigh
    s_sigh = "uhm.ogg"
    s_bubbling = "bubbling.ogg"
    s_potion = "bubbling.ogg"
    s_drug = "bubbling.ogg"
    s_cash = "cash.ogg"
    s_chapter = "chapter.ogg"
    s_chimes = "chimes.ogg"
    s_click = "click.ogg"
    s_crash = "crash.ogg"
    s_creak = "creak2.ogg"
    s_crunch = "crunch.ogg"
    s_dice = "dice roll.ogg"
    s_dodge = "dodge.ogg"
    s_door = "door opening.ogg"
    s_open = s_door
    s_door_close = "door closing.ogg"
    s_close = "door closing.ogg"
    s_dress = "equip dress.ogg"
    s_equip_dress = s_dress
    s_equip_item = "equip item.ogg"
    s_equip = s_equip_item
    s_fanfare = "fffanfare.ogg"
    s_fire = "fire.ogg"
    s_fizzle = "fizzle.ogg"
    s_fiz = "fizzle.ogg"
    s_knock = "knocks.ogg"
    s_knocks = s_knock
    s_evil_laugh = "laugh.ogg" # Female laugh
    s_kind_laugh = "laugh nice.ogg"
    s_laugh = s_kind_laugh
    s_girls_laugh = "laughs.ogg"
    s_gold = "gold.ogg"
    s_horn = "boing.ogg"
    s_boing = "boing.ogg"
    s_crowd_laugh = "laughs2.ogg"
    s_crowd_boo = "crowd boos.ogg"
    s_crowd_boos = s_crowd_boo
    s_boos = "crowd boos.ogg"
    s_crowd_chant = "crowd chant.ogg"
    s_crowd_cheer = "crowd cheer.ogg"
    s_cheer = "crowd cheer.ogg"
    s_crowd_riot = "crowd riot.ogg"
    s_lightning = "lightning bolt.ogg"
    s_thunder = "lightning bolt.ogg"
    s_maniacal_laugh = "maniacal laugh.ogg" # Male laugh
    s_meow = "meow.ogg"
    s_mmh = "mmmh.ogg"
    s_mmmh = s_mmh
    s_hmm = s_mmh
    s_moans = "moans6.ogg"
    s_moans_quiet = "moans7.ogg"
    s_moans_short = "moans8.ogg"
    s_moans_mature = "moans2.ogg"
    s_moans_mature_quiet = "moans1.ogg"
    s_moo = "moo.ogg"
    s_mystery = "mystery.ogg"
    s_orgasm = "orgasm.ogg"
    s_orgasm_young = "orgasm young.ogg"
    s_orgasm_fast = "orgasm fast.ogg"
    s_pee = "pouring water.ogg"
    s_punch = "punch.ogg"
    s_roar = "roar.ogg"
    s_rooster = "rooster.ogg"
    s_saw = "saw.ogg"
    s_scream = "scream1.ogg"
    s_scream_loud = "scream2.ogg"
    s_screams = "screams.ogg"
    s_shatter = "shatter.ogg"

    s_splash = "splash.ogg"
    s_splat = "splat.ogg"
    s_spell = "spell.ogg"
    s_steps = "steps.ogg"
    s_run = "steps.ogg"
    s_stone = "stone.ogg"
    s_success = "success.ogg"
    s_sucking = "sucking.ogg"
    s_surprise = "surprise.ogg"
    s_sword_clash = "sword clash.ogg"
    s_clash = "sword clash.ogg"
    s_clang = "sword clash.ogg"
    s_sword_sheath = "sword sheath.ogg"
    s_sheath = "sword sheath.ogg"
    s_sheathe = "sword sheath.ogg"
    s_slime = "tentacle.ogg"
    s_tentacle = "tentacle.ogg"
    s_vibro = "vibro.ogg"
    s_wscream = "wilhelm.ogg"
    s_wolf = "wolf.ogg"
    s_woman_scream = "woman scream.ogg"
    s_wind = "gust.ogg"
    s_gust = s_wind
    s_wings = "wings.ogg"
    s_whistle = "whistle.ogg"


#### TAG DICTIONARY : Converts old tag (strings found in picture filename) to new tag(s) (used in game)
    ## The old tag is discarded. Only the new tags are kept.
    ## All tags should be lower case (for performance reasons) and two characters or more.

    frequency_tags = {"freq_highest" : 900, "freq_high" : 300, "freq_low" : 30, "freq_lowest" : 10} # Base frequency is 100

    tag_dict = {
    # The key (left-hand side of the ':') is the string of characters BK looks for in the file name. The values (right-hand side) are the actual tags that will be added to the picture in-game.

                # Frequency tags

                "freq_highest" : "freq_highest",
                "freq_high" : "freq_high",
                "freq_low" : "freq_low",
                "freq_lowest" : "freq_lowest",

                # Old frequency tags (for retrocompatibility)

                "xq" : "freq_highest",
                "hq" : "freq_high",
                "lq" : "freq_low",

                # Portrait and profile tags (every girl should have at least one)

                "portrait" : "portrait",

                "profile" : "profile",

                # Specialized profile tags

                "market" : "market", # Used with preference to profile for the slavemarket
                "beauty" : ("profile", "model"), # Model is used for advertising pictures
                "card" : "profile",
#                "ent" : "profile", # Obsolete (conflicts with 'tent')
                "model" : ("profile", "model"), # Model is used for advertising pictures
                "advertise" : "model",
                "quest" : "profile",
                "shop" : "profile",
                "battle" : "fight",
                "fight" : "fight",
                "combat" : "fight",
                "hurt" : "hurt", # Use this instead of 'fight' if it shows her losing a fight

                "gallery" : "gallery", # Used as a background for the girl's CG gallery

                "happy" : "happy",
                "neutral" : "neutral",
                "sad" : "sad",
                "refuse" : "refuse",

                # Rest and work tags (highly recommended)

                "rest" : "rest",
                "ecchi" : ("rest", "libido"),

                "wait" : "waitress",
                "bunny" : ("waitress", "bunny", "cosplay"), # Bunny isn't used for now = cosplay
                "maid" : ("maid"), # Maid is used in the farm (obedience training)

                "danc" : ("dancer", "dance"), # Dancer is used for the job. Dance might be used in the future for classes and quests.
                "run" : ("constitution"), # Run is also used in the farm (constitution training)
                "sing" : ("dancer", "sing"), # Sing might be used in the future for classes and quests.
                "strip" : ("strip", "naked"), # Strip might be used in the future for classes and quests.

                "mass" : "masseuse",
                "swim" : ("swimsuit", "swim"), # Swimsuit might be used in the future for classes and quests. It is a fallback tag if no masseuse pic is found.

                "geisha" : "geisha",
                "etiquette" : "geisha",
                "kimono" : ("geisha", "kimono"), # kimono might be used in the future for classes and quests.
                "date" : "date", # Date is used for free girl interactions and court location profiles, and as a fallback tag for geisha

                "naked" : "naked", # Used in combination with other tags to make a girl appear naked
                "nude" : "naked",

                # Location tags (optional)

                "public" : "public", # The girl is in a publicly accessible place where there might be onlookers. Recommended for sexual events only (in BK)
                "beach" : ("public", "beach", "swimsuit", "swim"), # Beach pictures imply the swimsuit tag
                "nature" : ("public", "nature"), # The girl is in nature (except on a beach), such as in a garden, a forest or a field
                "town" : ("public", "town"), # The girl is in an urban environment, such as a street, a plaza or a market
                "city" : ("public", "town"),

                # Sexual tags (highly recommended)

                "virgin" : "virgin", # Used for images where the girl is losing her virginity

                # Note: Some service tags such as oral or handjob can have an effect on the text used in-game for flavor.

                "service" : "service",
                "mast" : ("mast"), # Most masturbating pics should be tagged service.
                "oral" : ("oral"), # Most oral pics should be tagged service.
                "blowjob" : ("oral"),
                "bj" : ("oral"),
                "cunnilingus" : ("cunni"), # Most cunnilingus pics should be tagged service.
                "hand" : ("handjob"),  # Most handjob pics should be tagged service.
                "titj" : ("titjob"), # Most titjob pics should be tagged service.
                "ttj" : ("titjob"),
                "tits" : ("titjob"),
                "titty" : ("titjob"),

                "sex" : "sex",
                "fuck" : "sex",
                "xxx" : ("sex", "XXX"), # XXX is used for XXX classes only, no need for it in girl packs

                "anal" : "anal",

                "fetish" : "fetish",
                "bdsm" : ("bondage"), # Bondage pics should be tagged fetish.
                "bondage" : ("bondage"),
                "hardcore" : ("fetish", "hardcore"), # hardcore is used for hardcore class stock pictures only, no need to use it in girl packs
                "foot" : ("footjob"), # Footjob pics should be tagged fetish (not service).
                "fj" : ("footjob"),

                # Optional tags: used for special sex acts and the farm. Can be mixed with regular sexual tags (necessary for the farm)

                "group" : "group",
                "bis" : "bisexual", # Bisexual pictures may feature up to one male
                "bisexual" : "bisexual", # This is needed to avoid 'bisexual' detecting the 'sex' tag
                "les" : ("lesbian", "bisexual"), # Lesbian pictures may not feature a male. The bisexual tag is added so that these pictures can proc during the appropriate sex act (the male protagonist is then assumed to be off-camera). Recommended for sexual events only (in BK)

                "beast" : "beast",
                "best" : "beast",

                "big" : "big",
                "stallion" : "big",

                "toy" : "toy", # Toy will be used inside and outside the farm (unless used with machine). Mostly used with service (masturbation) or fetish (administered by someone else).
                "machine" : "machine", # Machine will be excluded from regular events (except fetish if fuzzy tagging is on) and should be used for heavier machinery such as the ones found on the farm.

                "monster" : "monster",
                "tent" : "monster",

                "libido" : "libido", # For the farm: Girl tending to minions
                "obedience" : "obedience", # For the farm: Girl cleaning up the farm
                "sensitivity" : "sensitivity", # For the farm: Girl tending to Gizel
                "constitution" : "constitution", # For the farm: Girl running in the yard
#                "sports" : "constitution", # Disabled to avoid confusion with watersports

                # Fixation tags: Used for specific fixations (recommended)

                "cosplay" : "cosplay",
                "dild" : ("dildo", "toy"),
                "vibr" : ("vibrator", "toy"),
                "plug" : ("plug", "toy"),
                "dirty" : "dirty",
                "penis w" : ("handjob"), # Most handjob pics should be tagged service as well
                "penisw" : ("handjob"),
                "penis_w" : ("handjob"),
                "penis-w" : ("handjob"),
                "oil" : "wet",
                "wet" : "wet",
                "sub" : "sub",
                "humiliat" : "sub",
                "master" : "sub", # Some Internet packs apparently use this tag, included here to avoid conflict with mast (masturbate)
                "dom" : "dom",
                "gag" : "gag",
                "strap" : "strap-on",
                "role" : "cosplay", # roleplay has been deprecated to cosplay
                "bead" : ("beads", "toy"),

                "irru" : ("deep"), # irrumatio has been deprecated to deepthroat
                "deep" : ("deep"),
                "dt" : ("deep"),
                "double" : "double", # Will add the 'group' tag if not used with the beast/monster/machine tag (hardcoded)
                "finger" : "finger",
                "fist" : "fist",
                "insults" : ("sub"),
                "sixty" : ("69"),
                "watersp" : ("watersports"), # watersports means the girl peeing
                "enema" : ("enema"),
                "kiss" : "kiss",
                "spank" : ("spank"),
                "rim" : "rim",
                "grop" : "grope",
                "fondl" : "fondle",
                "lact" : "lactation",
                "doggy" : "doggy",
                "cowg" : "cowgirl",
                "pile" : "piledriver",
                "spoon" : "spoon",

                "cum" : "cumshot",
                "buk" : ("buk", "cumshot"),
                "cim" : ("cim", "cumshot"),
                "mouth" : ("cim", "cumshot"),
                "cif" : ("cof", "cumshot"),
                "cof" : ("cof", "cumshot"),
                "face" : ("cof", "cumshot"),
                "cih" : ("cih", "cumshot"),
                "coh" : ("cih", "cumshot"),
                "hair" : ("cih", "cumshot"),
                "cob" : ("cob", "cumshot"),
                "body" : ("cob", "cumshot"),
                "shower" : ("cum shower", "cumshot"),
                "swa" : ("cim", "cumshot"),
                "cream" : ("creampie", "cumshot"), # Creampie differs from cum inside in that the dick is shown outside
                "cin" : ("cin", "cumshot"), # Cum inside differs from creampie in that the dick is shown inside her
                "inside" : ("cin", "cumshot"),
                "orgasm" : "orgasm",
                "denied" : "denied",
                "squirt" : ("squirt", "orgasm"),


                # Unused tags: Used for pictures that are ignored by the 'Check untagged girl pics' cheat. Mostly ignore this.

                "death" : "unused",
                "preg" : "unused", # the pregnant tag might be used one day. One day...

                }

    # Pictures with NSFW tags will be ignored when nsfw is set to False.
    # Warning: Turning nsfw off is for debugging only; many pictures will remain uncensored, so watch out.

    nsfw_tags = ["naked", "service", "oral", "blowjob", "handjob", "titjob", "mast", "sex", "anal", "fetish", "bisexual", "group", "beast", "machine", "monster", "big"]

    # Pictures with forbidden tags will be completely ignored. Use this to disable unwanted content.

    forbidden_tags = ["unused"]


#### SUPPORT/CONTACT ####

    ## For feedback, bug report, constructive criticism, etc. Appears in help messages

    URL = "{a=https://www.henthighschool.net/brothel-king/}{color=#9933FF}https://www.henthighschool.net/brothel-king/{/color}{/a}"

#### END OF BK SETTINGS ####
