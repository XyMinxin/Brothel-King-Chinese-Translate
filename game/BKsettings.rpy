####         SETTINGS           ####################################################
##    Those are the settings      ##################################################
##    that can be easily edited   ##################################################
##    by players in Bro King      ##################################################


init -4 python:

#### GIRLS FOLDER ####

    girl_directories = ["girls/", ] # You can specify one or more directories containg girl packs. The 'game' folder is the root folder

#### SCREEN RESOLUTION & PERFORMANCE ####

    ## These control the width and height of the screen.

    config.screen_width = 1366
    config.screen_height = 768

    ## Picture caching. Set lower values if you have memory problems. Use only one setting, comment the other out with the # symbol.

    config.image_cache_size = 128 # Set this higher for better performance (will use more RAM)
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
#### 翻译 ####

    ## Edit this dictionary to change the stat names that are displayed (change the right-hand text)

    ## 统计名词翻译 ##
    stat_name_dict = {
                        "Beauty" : "美貌",
                        "Body" : "身材",
                        "Charm" : "魅力",
                        "Refinement" : "优雅",
                        "Sensitivity" : "敏感",
                        "Libido" : "性欲",
                        "Constitution" : "体格",
                        "Obedience" : "服从",
                        "Service" : "性服侍",
                        "Sex" : "性交",
                        "Anal" : "肛交",
                        "Fetish" : "皮绳愉虐",
                        "Energy" : "耐力",
                    }

    ## 中文翻译 ##
    chinese_name = {
                    ## 职业名称 ##
                    "Waitress" : "服务员",
                    "waitress" : "服务员",
                    "Dancer" : "舞娘",
                    "dancer" : "舞娘",
                    "Masseuse" : "按摩师",
                    "masseuse" : "按摩师",
                    "Geisha" : "艺伎",
                    "geisha" : "艺伎",
                    "Whore" : "妓女",
                    "whore" : "妓女",

                    ## 性行为 ##
                    "Service" : "性服侍",
                    "service" : "性服侍",
                    "Sex" : "性交",
                    "sex" : "性交",
                    "Anal" : "肛交",
                    "anal" : "肛交",
                    "Fetish" : "皮绳愉虐",
                    "fetish" : "皮绳愉虐",
                    "Naked" : "露出",
                    "naked" : "露出",
                    "Group" : "群交",
                    "group" : "群交",
                    "Bisexual" : "百合",
                    "bisexual" : "百合",

                    ## 装备栏位 ##
                    "Hands" : "手持",
                    "hands" : "手持",
                    "Accessory" : "配饰",
                    "accessory" : "配饰",
                    "Misc" : "杂项",
                    "misc" : "杂项",
                    "Body" : "身体",
                    "body" : "身体",
                    "Finger" : "手",
                    "finger" : "手",
                    "Neck" : "颈部",
                    "neck" : "颈部",

                    ## 农场相关 ##
                    "Refused" : "拒绝",
                    "refused" : "拒绝",
                    "Resisted" : "抵制",
                    "resisted" : "抵制",
                    "Accepted" : "接受",
                    "accepted" : "接受",
                    "Soft" : "温和",
                    "soft" : "温和",
                    "Hard" : "努力",
                    "hard" : "努力",
                    "Hardest" : "强硬",
                    "hardest" : "强硬",
                    "Libido" : "照看仆役",
                    "libido" : "照看仆役",
                    "Sensitivity" : "服侍Gizel",
                    "sensitivity" : "服侍Gizel",
                    "Obedience" : "打扫农场",
                    "obedience" : "打扫农场",
                    "Constitution" : "锻炼身体",
                    "constitution" : "锻炼身体",
                    "Rest" : "休息",
                    "rest" : "休息",
                    "Conservative" : "保守",
                    "conservative" : "保守",
                    "Intensive" : "高强度",
                    "intensive" : "高强度",
                    "No rest" : "无休息",
                    "no rest" : "无休息",
                    "Reluctant" : "差强人意",
                    "reluctant" : "差强人意",
                    "Indifferent" : "淡然处之",
                    "indifferent" : "淡然处之",
                    "Interested" : "兴趣盎然",
                    "interested" : "兴趣盎然",
                    "Fascinated" : "神魂颠倒",
                    "fascinated" : "神魂颠倒",
                    "None" : "无",
                    "none" : "无",
                    "Auto" :"自动",
                    "auto" :"自动",
                    "种马棚" : "马厮",
                    "stables" : "马厮",
                    "兽栏" : "兽栏",
                    "pig stall" : "兽栏",
                    "怪物巢穴" : "怪兽巢穴",
                    "monster den" : "怪兽巢穴",
                    "车间" : "车间",
                    "workshop" : "车间",
                    "No training" : "未安排训练",
                    "no training" : "未安排训练",

                    ## 农场奴仆 ##
                    "Stallion" : "种马",
                    "stallion" : "种马",
                    "Beast" : "野兽",
                    "beast" : "野兽",
                    "Monster" : "怪物",
                    "monster" : "怪物",
                    "Machine" :"机器",
                    "machine" :"机器",

                    ## ##
                    "MC" : "玩家",
                    "Girl" : "女孩",
                    "girl" : "女孩",
                    "Minion" : "农场仆从",
                    "minion" : "农场仆从",
                    "Gift" : "礼物",
                    "gift" : "礼物",

                    ## 选项 ##
                    "Back" : "返回",
                    "back" : "返回",
                    "Hide" : "隐藏",
                    "hide" : "隐藏",
                    "Close" : "关闭",
                    "close" : "关闭",
                    "Next" : "下一个",
                    "next" : "下一个",

                    None : "（bug:chinese_name）没有值",
                    }

    ## 按钮名字 ##
    button_name_dict = {
                        "Chat" : "交谈",
                        "chat" : "交谈",
                        "Train" : "训练",
                        "train" : "训练",
                        "Magic" : "魔术",
                        "magic" : "魔术",
                        "React" : "行动",
                        "react" : "行动",
                        "Misc" : "杂项",
                        "misc" : "杂项",
                        }

    ## 初始创建界面 ##
    start_dict_name = {
                        ## 职业 ##
                        "Warrior" : "战士",
                        "Wizard" : "法师",
                        "Trader" : "奸商",

                        ## 信仰 ##
                        "Arios" : "阿里奥斯",
                        "Shalia" : "莎莉娅",

                        ## 玩家属性 ##
                        "Strength" : "力量",
                        "Spirit" : "法力",
                        "Charisma" : "魅力",
                        "Speed" : "耐力",

                        ## 难度 ##
                        "Very easy" : "非常容易",
                        "very easy" : "非常容易",
                        "Easy" : "容易",
                        "easy" : "容易",
                        "Normal" : "正常",
                        "normal" : "正常",
                        "Hard" : "困难",
                        "hard" : "困难",
                        "Insane" : "疯狂",
                        "lnsane" : "疯狂",
                        "Custom" : "定制",
                        "custom" : "定制",

                        None : "（bug:start_dict_name）没有值",
                        }

    ## 女孩偏好 ##
    girl_preference_name = {
                            "Refuses" : "抵制",
                            "refuses" : "抵制",
                            "Very reluctant" : "非常不情愿",
                            "very reluctant" : "非常不情愿",
                            "Reluctant" : "不情愿",
                            "reluctant" : "不情愿",
                            "A little reluctant" : "有点不情愿",
                            "a little reluctant" : "有点不情愿",
                            "Indifferent" : "不在意",
                            "indifferent" : "不在意",
                            "A little interested" : "有点感兴趣",
                            "a little interested" : "有点感兴趣",
                            "Interested" : "感兴趣",
                            "interested" : "感兴趣",
                            "Very interested" : "非常感兴趣",
                            "very interested" : "非常感兴趣",
                            "Fascinated" : "陶醉",
                            "fascinated" : "陶醉",
                            }


    room_dict_name = {
                    "Basic room" : "基本房间",
                    "+Basic room+" : "+基本房间+",
                    "*Basic room*" : "*基本房间*",
                    "Standard room" : "标准房间",
                    "+Standard room+" : "+标准房间+",
                    "*Standard room*" : "*标准房间*",
                    "Elegant room" : "优雅房间",
                    "+Elegant room+" : "+优雅房间+",
                    "*Elegant room*" : "*优雅房间*",
                    "Noble suite" : "贵族套房",
                    "+Royal suite+" : "+皇家套房+",
                    "*Imperial suite*" : "*帝国套房*",
                    }

    ## 互动界面 ##
    interact_dict_name = {
                        "Chat" : "交谈",
                        "chat" : "交谈",
                        "Train" : "训练",
                        "train" : "训练",
                        "Magic" : "魔术",
                        "magic" : "魔术",
                        "React" : "行动",
                        "react" : "行动",
                        "Misc" : "杂项",
                        "misc" : "杂项",
                        "Fun" : "乐趣",
                        "fun" : "乐趣",
                        "Flirt" : "调戏",
                        "flirt" : "调戏",
                        "Give" : "给予",
                        "give" : "给予",
                        "DEBUG" : "DEBUG",
                        }

    ## 设置 ##
    settings_name = {
                    ## 一般选项 ##
                    "Back" : "返回",
                    "back" : "返回",
                    "Hide" : "隐藏",
                    "hide" : "隐藏",
                    "Close" : "关闭",
                    "close" : "关闭",

                    ## 夜间活动设置 ##
                    "Normal" : "一般",
                    "Matchmaking" : "婚介",
                    "Customer" : "顾客",
                    "Level/Job/Rank up" : "等级/职业/品阶提升",
                    "Health/Security" : "健康/安全",
                    "Satisfaction report" : "满意报告",
                    "Farm" : "农场",
                    "Rest" : "休息",
                    }

#### BALANCE / CHEATS ####

    debug = False # Replace this with 'True' for additional cheats and information (recommended for testing)

    cheat_modifier = { # Set it at 1.0 for normal play
                        "gold" : 1.0,
                        "stats" : 1.0,
                        "xp" : 1.0,
                        "jp" : 1.0,
                        "rep" : 1.0,
                        "prestige" : 1.0
                     }

    ## STARTING TRAITS

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

    bro_cost = {1 : 0, 2 : 1000, 3: 5000, 4 : 7500, 5 : 15000, 6 : 25000, 7 : 100000}

    # Reputation cap affects the maximum number of customers that can come before advertising and special effects. Each customer costs 10 pts of reputation * rank
    bro_reputation_cap = {1 : 80, 2 : 320, 3 : 480, 4 : 1200, 5 : 1560, 6 : 3040, 7 : 5800}

    ## CHAPTER GOALS

    # Goal types can be: 'gold', 'ranked', 'reputation', 'prestige'

    chapter_goals = {
                     1 : [Goal("gold", bro_cost[2])],
                     2 : [Goal("gold", bro_cost[3])],
                     3 : [Goal("ranked", 2, 6), Goal("gold", bro_cost[4])],
                     4 : [Goal("ranked", 3, 8), Goal("gold", bro_cost[5])],
                     5 : [Goal("ranked", 3, 10), Goal("gold", bro_cost[6])],
                     6 : [Goal("ranked", 4, 12), Goal("gold", 100000)],
                     7 : [Goal(None, channel="other")],
                    }

    ## CUSTOMER CAPACITY

    # The formula for calculating customer capacity is: base_customer + (main_stat + constitution) // customer_points
    # Main stat is: Beauty, Body, Charm or Refinement for jobs, Libido for whores
    # This values are halved if the girl works half-time
    # You can edit those values here.

    job_base_customer = 2 #! Changed
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
                    "group bonus" : 0.75, # Applies to each customer
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
                    3 : "3 town brothel.jpg",
                    4 : "4 rich brothel.jpg",
                    5 : "5 rich brothel.jpg",
                    6 : "6 king brothel.webp",
                    7 : "7 endless brothel.jpg"
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
                "Double room" : "master/master1.jpg",
                "Small suite" : "master/master2.webp",
                "Luxury suite" : "master/master3.webp",
                "Royal suite" : "master/master4.jpg",
                "Royal harem" : "master/master5.webp",
                }

    night_pics = ["night.webp",]


    #! Temporary: New advertising pics will eventually be added
    advertising_pics = {1 : ["poster girls1.jpg", "poster girls2.jpg", "poster girls3.jpg", "poster girls4.jpg", "poster girls5.jpg",
                        "poster girls6.jpg", "poster girls7.jpg", "poster girls8.jpg", "poster girls9.jpg", "poster girls10.jpg",
                        "poster girls11.jpg"]}

    advertising_pics[2] = advertising_pics[3] = advertising_pics[4] = advertising_pics[5] = advertising_pics[1]

    pony_pics = ["ponygirls.jpg", "ponygirls (1).jpg", "ponygirls (2).jpg", "ponygirls (3).jpg", "ponygirls (4).jpg", "ponygirls (5).jpg", "ponygirls (6).jpg",]

    security_pics = {
                     "gooey monsters" : ["monster assault.jpg",],
                     "rogue mercenaries" :  ["merc assault (1).jpg", "merc assault (1).webp", "merc assault (2).jpg"],
                     "marauding ogres" : ["ogre assault (1).jpg", "ogre assault (3).webp", "ogre assault (2).jpg"],
                     "monster rape" : ["monster (1).jpg", "monster (1).webp", "monster (2).jpg", "monster (2).webp", "monster (3).jpg", "monster (4).jpg", "monster (5).jpg", "monster (6).jpg", "monster (7).jpg", "monster (8).jpg", "monster (9).jpg", "monster (10).jpg", ],
                     "thief" : ["thief (1).jpg", "thief (2).jpg", "thief (3).jpg", "thief (4).jpg", "thief (5).jpg", "thief (6).jpg"],
                     "brothel defense" : ["brothel defense (1).jpg", "brothel defense (2).jpg"],
                     "monster defense" : ["monster defense (1).jpg", "monster defense (2).jpg"],
                     "thief defense" : ["thief captured (1).jpg", "thief captured (2).jpg", "thief captured (3).jpg", "thief captured (4).jpg", "thief captured (5).jpg"],
                     "girl defense" : ["bar fight.webp"],
                     "girl shield" : ["shield.jpg"],
                     "default girl fight" : ["fight1.webp", "fight2.webp", "fight3.webp", "fight4.webp"],
                     "assassin defense" : ["assassin1.jpg", "assassin2.jpg", "assassin3.jpg", "assassin4.jpg", "assassin5.jpg", "assassin6.jpg"],
                     "assassin" : ["assassin7.webp", "assassin8.webp", "assassin9.jpg"],
                     "sword defense" : ["sword defense1.webp", "sword defense2.webp", "sword defense3.webp", "sword defense4.webp"],
                     "magic defense" : ["magic defense.webp"],
                     "dragon defense" : ["dragon defense.jpg"],
                     "brawl" : ["bar fight.webp", "brawl1.jpg", "brawl2.jpg", "brawl3.jpg"],
                     "siege" : ["siege1.jpg", "siege2.jpg", "siege3.jpg", "siege4.jpg", "siege5.jpg", "siege6.jpg", "siege7.webp"],
                     "hood" : ["hood.jpg"],
                     "dark street" : ["dark street1.jpg", "dark street2.jpg"],
                     "alert" : ["alert1.webp", "alert2.webp", "alert3.webp"],
                     }

    arson_pics = ["arson1.jpg", "arson2.jpg", "arson3.jpg", "arson4.jpg"]
    violent_pics = ["violent.jpg", "violent2.jpg"]

    treasure_pics = {"+++" : ["treasure_blonde (3).jpg", "treasure_pink (3).jpg"], "++" : ["treasure_blonde (2).jpg", "treasure_pink (2).jpg"], "+" : ["treasure_blonde (1).jpg", "treasure_pink (1).jpg"], "-" : ["treasure_blonde (0).jpg", "treasure_pink (0).jpg"]}
    no_girls_pics = ["harem.jpg",]

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

    playlist = ["553686_Emperors-Garden.mp3", "518978_Desert-Winds.mp3", "Cubis.mp3", "gnagna.mp3", "Guembriblues.mp3", "snake charmer.mp3", "Zurna.mp3",
                "Tibet.mp3", "Mimi.mp3", "infos-tapis.mp3", "Balkanissimo.mp3", "Balkano.mp3"]


    ## Channel declaration

    renpy.music.register_channel("music", mixer = "music", file_prefix = "music/")
    renpy.music.register_channel("sound", mixer = "sfx", file_prefix = "sounds/", loop = False)
    renpy.music.register_channel("sound2", mixer = "sfx", file_prefix = "sounds/", loop = False)
    renpy.music.register_channel("sound3", mixer = "sfx", file_prefix = "sounds/", loop = False)
    renpy.music.register_channel("video", mixer = "sfx")

    ## Music ## Shortcuts for music used in the game from the 'Game\Music' folder

    m_theme = "soaring dragon.mp3"
    m_oriental = "518978_Desert-Winds.mp3"
    m_market = "snake charmer.mp3"
    m_gizel = "Harp for the Devil.mp3"
    m_gio = "gnagna.mp3"
    m_jazz = "infos-tapis.mp3"
    m_rain = "light rain.mp3"
    m_mafia = "omerta.wav"
    m_suspense = "risky path.mp3"
    m_wind = "wind.wav"
    m_kosmo = "Zurna.mp3"
    m_freak = "Mimi.mp3"
    m_danger_loop = "538771_Your-Stalker.mp3"
    m_danger = "538771_Your-Stalker.mp3"
    m_knights = "595642_Realm-of-the-Forgot.mp3"
    m_tavern = "Abyss.mp3"
    m_evil = "Evil Ambiance-SoundBible.com-1774179982.mp3"
    m_nature = "Indian-Bird.mp3"
    m_satella = "Bonbon.mp3"
    m_shalia = "553759_Small-Moments.mp3"
    m_demons = "542049_Ravaged-By-Demons.mp3"
    m_disco = "579511_Real-Life-Disco-Loo.mp3"
    m_palace = "470178_Marching-Together.mp3"
    m_water = "waterfall.mp3"
    m_accordeon = "Balkano.mp3"
    m_zan = "553686_Emperors-Garden.mp3"
    m_action = "580741_Sunburn-Original-Mi.mp3"
    m_kenshin = "584589_Peaceful-Harmony.mp3"
    m_suzume = "587133_Shining-Star.mp3"
    m_kunoichi = "public enemy no1.mp3"

    ## Sounds ## Shortcuts for sound effects used in the game from the 'Game\Sounds' folder (warning: some sound effects paths are hard-coded, this will be cleaned up later)

    s_aah = "aah.mp3"
    s_aaah = s_aah
    s_sexy_sigh = "aaha.mp3"
    s_aaha = s_sexy_sigh
    s_ahaa = s_sexy_sigh
    s_sigh = "uhm.mp3"
    s_bubbling = "bubbling.ogg"
    s_potion = "bubbling.ogg"
    s_drug = "bubbling.ogg"
    s_cash = "cash.wav"
    s_chimes = "chimes.wav"
    s_click = "click.wav"
    s_crash = "crash.ogg"
    s_creak = "creak2.ogg"
    s_crunch = "crunch.ogg"
    s_dice = "dice roll.ogg"
    s_dodge = "dodge.ogg"
    s_door = "door opening.wav"
    s_open = "door opening.wav"
    s_door_close = "door closing.wav"
    s_close = "door closing.wav"
    s_dress = "equip dress.ogg"
    s_equip_dress = "equip dress.ogg"
    s_equip_item = "equip item.wav"
    s_equip = "equip item.wav"
    s_fire = "fire.wav"
    s_fizzle = "fizzle.ogg"
    s_fiz = "fizzle.ogg"
    s_knock = "knocks.mp3"
    s_knocks = "knocks.mp3"
    s_evil_laugh = "laugh.ogg"
    s_kind_laugh = "laugh nice.ogg"
    s_laugh = "laugh nice.ogg"
    s_girls_laugh = "laughs.ogg"
    s_gold = "gold.ogg"
    s_horn = "boing.ogg"
    s_boing = "boing.ogg"
    s_crowd_laugh = "laughs2.ogg"
    s_crowd_boo = "crowd boos.ogg"
    s_crowd_boos = "crowd boos.ogg"
    s_boos = "crowd boos.ogg"
    s_crowd_chant = "crowd chant.ogg"
    s_crowd_cheer = "crowd cheer.ogg"
    s_cheer = "crowd cheer.ogg"
    s_crowd_riot = "crowd riot.ogg"
    s_lightning = "lightning bolt.mp3"
    s_thunder = "lightning bolt.mp3"
    s_maniacal_laugh = "maniacal laugh.ogg"
    s_meow = "meow.ogg"
    s_mmh = "mmmh.wav"
    s_mmmh = "mmmh.wav"
    s_moans = "moans6.wav"
    s_moans_quiet = "moans7.wav"
    s_moans_short = "moans8.wav"
    s_moo = "moo.mp3"
    s_mystery = "mystery.ogg"
    s_orgasm = "orgasm.mp3"
    s_orgasm_young = "orgasm.wav"
    s_orgasm_fast = "orgasm2.mp3"
    s_pee = "pouring water.mp3"
    s_punch = "punch.wav"
    s_roar = "roar.mp3"
    s_rooster = "rooster.mp3"
    s_saw = "saw.ogg"
    s_scream = "scream1.wav"
    s_scream_loud = "scream2.wav"
    s_screams = "screams.wav"
    s_shatter = "shatter.wav"

    s_splash = "splash.mp3"
    s_spell = "spell.ogg"
    s_steps = "steps.wav"
    s_run = "steps.wav"
    s_stone = "stone.ogg"
    s_success = "success.ogg"
    s_sucking = "sucking.wav"
    s_surprise = "surprise.wav"
    s_sword_clash = "sword clash.mp3"
    s_clash = "sword clash.mp3"
    s_clang = "sword clash.mp3"
    s_sword_sheath = "sword sheath.mp3"
    s_sheath = "sword sheath.mp3"
    s_sheathe = "sword sheath.mp3"
    s_vibro = "vibro.ogg"
    s_wscream = "wilhelm.wav"
    s_wolf = "wolf.ogg"
    s_woman_scream = "woman scream.mp3"
    s_wind = "gust.ogg"
    s_wings = "wings.mp3"
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
                "model" : ("profile", "model"),
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
                "maid" : ("waitress", "maid"), # Maid is used in the farm (obedience training)

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
                "les" : ("lesbian", "bisexual"), # Lesbian pictures may not feature a male. The bisexual tag is added so that these pictures can proc during the appropriate sex act (the male protagonist is then assumed to be off-camera). Recommended for sexual events only (in BK)

                "beast" : "beast",
                "best" : "beast",

                "big" : "big",
                "stallion" : "big",

                "toy" : "toy", # Toy will be used inside and outside the farm (unless used with machine). Mostly used with service (masturbation) or fetish (administered by someone else).
                "machine" : "machine", # Machine will be excluded from regular events (except fetish) and should be used for heavier machinery such as the ones found on the farm.

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
                "cream" : ("creampie", "cumshot"),
                "cin" : ("cin", "cumshot"),
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

    URL = "{a=https://www.henthighschool.com/brothel-king/}{color=#9933FF}https://www.henthighschool.com/brothel-king/{/color}{/a}"

#### END OF BK SETTINGS ####
