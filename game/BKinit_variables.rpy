####         INIT VARIABLES FOR B KING          ####################################################
##    Those are the init variables and lists      ##################################################
##    for B King                                  ##################################################
##                                                ##################################################

init -3:

    define persistent.new_game_plus = False
    define persistent.last_difficulty = "normal" # Either stores a stock difficulty name or a custom difficulty dictionary
    define persistent.seen_list = []
    define persistent.forbidden_tags = []
    define persistent.keep_firstname = False
    define persistent.keep_lastname = False
    define persistent.gp_name_customization = True
    define persistent.use_stock_pictures = defaultdict(bool)
    define persistent.show_girlpack_rating = None
    define persistent.skipped_events = defaultdict(bool)
    define persistent.mix_group_pictures = False
    define persistent.mix_bis_pictures = False
    define persistent.naked_girls_in_slavemarket = False
    define persistent.naked_girls_in_town = False
    define persistent.badges_on_portraits = False

    define persistent.show_girl_status = {"away": True, "farm": True, "rest": True, "scheduled": False, "half-shift": True, "master bedroom": True, "work&whore": True, "not work&whore": False, "naked": True, "not naked": False, "negative fixation": True}
    define persistent.cheats = False # Tracks if cheats are on in general (but the main setting is within the 'game' object)
    define persistent.girl_packs = []
    define persistent.girl_mix = {"default" : []}
    define persistent.active_mix = "default"
    define persistent.game_mixes = ["default"]
    define persistent.achievements = {} # Stores achievement levels with the following format: {target : level}. Workaround because Objects cannot be saved as persistent.
    define selected_achievement = None
    define latest_achievements = []

    define persistent.debug_pic_counter_dict = defaultdict(int) # Dictionary containing (pictures : count) when debug_pic_counter is on
    define persistent.debug_pic_counter = False

    define persistent.fix_pic_balance = fix_pic_balance_variety # Sets weights for the 'get_fix_pic()' Girl method

    define persistent.seen_tax_intro = False

init -3 python:

#### SYSTEM ####

    version_number = 0.2

    VIDEOFORMATS = (".webm", ".mkv", ".avi", ".mpg", ".mpeg") # Took out ".mp4" because of missing codecs
    IMGFORMATS = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp") + VIDEOFORMATS # animated gifs and .webp do not work in Ren'py for now

    config.layers.append("myoverlay")

    ## Change native ren'py keymap behavior ##

    try:
        config.keymap['game_menu'].remove('mouseup_3')
    except:
        pass
    # config.keymap['game_menu'].append('o')

    try:
        config.keymap['screenshot'].remove('s')
    except:
        pass
    config.keymap['screenshot'].append('shift_S')

    try:
        config.keymap['toggle_fullscreen'].remove('f')
    except:
        pass
    config.keymap['toggle_fullscreen'].append('shift_F')

    try:
        config.keymap['toggle_music'].remove('m')
    except:
        pass
    config.keymap['toggle_music'].append('shift_M') # This doesn't work for reasons unclear

    try:
        config.keymap['hide_windows'].remove('h')
    except:
        pass
    config.keymap['hide_windows'].append('shift_H')

    try:
        config.keymap['self_voicing'].remove('v')
    except:
        pass
    config.keymap['self_voicing'].append('shift_V')

    # config.keymap['inspector'].remove('i')
    # config.keymap['inspector'].append('shift_I')

    config.keymap['viewport_up'] += ('K_PAGEUP', 'repeat_K_PAGEUP')
    config.keymap['viewport_down'] += ('K_PAGEDOWN', 'repeat_K_PAGEDOWN')

    gallery_type = "ev"

    untagged_pics = []
    rating_dict = defaultdict(dict)

    test_event_name = ""

    choice_menu_girl_interact = False
    last_interact_menu = "chat"
    last_free_interact_menu = "chat"

    selected_view_mode = "Auto"

    read_ini_log = ""

#### GOALS ####

    goal_channels = ("story", "story2", "story3", "advance", "advance2", "contract", "other")
    goal_categories = {"story" : "STORY", "story2" : "STORY", "story3" : "STORY", "advance" : "ADVANCE", "advance2" : "ADVANCE", "contract" : "CONTRACT", "other" : "MISC"}
    goal_colors = {"STORY" : c_darkpurple, "ADVANCE" : c_magenta, "CONTRACT" : c_firered, "MISC" : c_darkgrey}
    goal_tb = {"STORY" : "tb story", "ADVANCE" : "tb advance", "CONTRACT" : "tb contract", "MISC" : "tb other"}

#### TAG LIST ####

    #<Chris12>
    for tag in tag_dict:
        if tag != tag.lower(): raise Exception("Illegal Tag " + tag + " in tag_dict! Only lowercase allowed.")
        if len(tag) <= 1: raise Exception("Illegal Tag " + tag + " in tag_dict! Tags must be at least 2 characters long.")
    tag_list_dict = {tag : make_list(tag_dict[tag]) for tag in tag_dict}
    sorted_tag_dict_keys = sorted(tag_dict.keys(), key = lambda x : len(x), reverse=True)
    sorted_tags_with_separator = [tag for tag in sorted_tag_dict_keys if " " in tag]
    ending_pattern = re.compile(r"(\(\d*\))?(\.\w{3,4})+$") # can match (and remove) the last part of a filename '(00001).jpg'.
    #</Chris12>

#### BADGES ####

    badge_pics = [f for f in renpy.list_files() if f.startswith("UI/badges/") and is_imgfile(f)]

#### DIFFICULTY ####

    diff_list = ["very easy", "easy", "normal", "hard", "insane"] # A list is needed to show the values in order

    diff_name = {"very easy" : "Gigolo", "easy" : "Hustler", "normal" : "Whorelord", "hard" : "Brothel Prince", "insane" : "Brothel King"}

    diff_description = {"very easy" : "No challenge at all. You're either here for the story, or the pretty pictures. {i}All achievements are locked.{/i}", "easy" : "A basic challenge for new players.", "normal" : "The classic experience.", "hard" : "Want more challenge? Hard has got you covered.", "insane" : "The ultimate challenge."}

    diff_settings = ["stats", "xp", "jp", "pref", "rep", "gold", "rewards", "resources", "prestige", "tax rate", "satisfaction"] # A list is needed to show the values in order

    diff_setting_name = {
                         "gold" : "收入",
                         "rewards" : "奖励",
                         "resources" : "资源",
                         "stats" : "女孩的技能",
                         "pref" : "性偏好",
                         "xp" : "经验",
                         "jp" : "职业经验",
                         "rep" : "女孩的声誉",
                         "prestige" : "声望",
                         "tax rate" : "公会费用抵消",
                         "satisfaction" : "客户满意度",
                        }

    diff_setting_description = {
                         "gold" : "影响青楼的{b}收入{/b}。",
                         "rewards" : "影响{b}任务、等级和合约{/b}的奖励。",
                         "resources" : "影响收集和交易中获得的{b}资源{/b}的数量。",
                         "stats" : "影响女孩的{b}技能{/b}的进展。",
                         "pref" : "影响女孩的{b}性偏好{/b}的进展。",
                         "xp" : "影响女孩的{b}经验{/b}的进展。",
                         "jp" : "影响女孩的{b}职业经验{/b}的进展。",
                         "rep" : "影响女孩的{b}声望{/b}的进展。",
                         "prestige" : "影响主角{b}声望{/b}的进展。",
                         "tax rate" : "增加或减少奴隶公会的{b}费用{/b}。",
                         "satisfaction" : "改变客户{b}满意度{/b}奖金。",
                        }

    diff_settings_range = {
                         "gold" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                         "rewards" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                         "resources" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                         "stats" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                         "pref" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                         "xp" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                         "jp" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                         "rep" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                         "prestige" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                         "tax rate" : {"min" : -0.3, "max" :  0.3, "pace" :  0.05},
                         "satisfaction" : {"min" : -3, "max" : 3, "pace" : 1},
                        }

    diff_dict = {
                 "very easy" : {"gold" : 1.5,
                            "rewards" : 1.5,
                            "resources" : 1.5,
                            "stats" : 1.5,
                            "pref" : 1.5,
                            "xp" : 1.5,
                            "jp" : 1.5,
                            "rep" : 1.5,
                            "prestige" : 1.5,
                            "tax rate" : -0.2,
                            "satisfaction" : 2,
                           },

                 "easy" :  {"gold" : 1.25,
                            "rewards" : 1.25,
                            "resources" : 1.5,
                            "stats" : 1.25,
                            "pref" : 1.25,
                            "xp" : 1.25,
                            "jp" : 1.25,
                            "rep" : 1.25,
                            "prestige" : 1.25,
                            "tax rate" : -0.1,
                            "satisfaction" : 1,
                           },
                 "normal" : {"gold" : 1.0,
                            "rewards" : 1.0,
                            "resources" : 1.0,
                            "stats" : 1.0,
                            "pref" : 1.0,
                            "xp" : 1.0,
                            "jp" : 1.0,
                            "rep" : 1.0,
                            "prestige" : 1.0,
                            "tax rate" : 0.0,
                             "satisfaction" : 0,
                            },

                 "hard" :  {"gold" : 0.8, #! Changed as per Chris12's suggestion (experimental)
                            "rewards" : 0.85,
                            "resources" : 0.85,
                            "stats" : 0.75,
                            "pref" : 0.75,
                            "xp" : 0.75,
                            "jp" : 0.75,
                            "rep" : 1.0,
                            "prestige" : 1.0,
                            "tax rate" : 0.1,
                            "satisfaction" : -1,
                           },
                 "insane" : {"gold" : 0.6, #! Changed as per Chris12's suggestion (experimental)
                            "rewards" : 0.6,
                            "resources" : 0.6,
                            "stats" : 0.5,
                            "pref" : 0.5,
                            "xp" : 0.5,
                            "jp" : 0.5,
                            "rep" : 0.75,
                            "prestige" : 0.75,
                            "tax rate" : 0.2,
                            "satisfaction" : -2,
                            },
    }


#### STARTING GAME VARIABLES AND OBJECTS ####

    ## INIT VARIABLES ##

#    global selected_girl
    selected_girl = None
    selected_sex_act = None
#    global selected_quest
    selected_item = None
    selected_quest = None
    selected_district = None
    selected_location = None
    selected_destination = None
    show_spellbook = False
    pers_showing = "personality"
#    vp_value = 0
    vp_adj = ui.adjustment()
    sched_adj = ui.adjustment()

    adjust_vp = True
    shake_count = 0
    always_show_brothel_report = False

    last_contract_result = None

    ## STORY GIRLS ##

    # girl_directories.append("NPC/Homura/") # girl_directories is initiated in BKsettings. Declare story girl paths here

#### RANDOM TIPS ####

    random_tips = [
                    "Zan是一个令人兴奋的地方...一定要经常探索!",
                    "你知道经营青楼有很多捷径对吧?你需要找到正确的方法...",
                    "漂亮的女孩是最好的按摩师。",
                    "按摩师应该具有{b}美貌{/b}与{b}敏感{/b}。当然{b}身材{/b}与{b}优雅{/b}也很重要。",
                    "一个身材好的女孩能成为一个伟大的舞蹈家。",
                    "舞娘应该具有{b}身材{/b}和{b}性欲{/b}。 当然{b}优雅{/b}和{b}魅力{/b}也很重要。",
                    "迷人的女孩当服务员会更好。",
                    "服务员需要{b}魅力{/b}和{b}体格{/b}。 如果是具有较高的{b}美貌{/b}，并且有一个不俗的{b}身材{/b}也不错。",
                    "艺妓应该是有教养的女孩，才能达到最好的效果。",
                    "艺妓应该是{b}优雅{/b}和{b}服从{/b}。 {b}美貌{/b}和{b}魅力{/b}也有助于成为一个完美的艺妓。",
                    "高级别的顾客很难满足，但他们给的小费会更多。",
                    "别忘了付青楼的安保费用。 否则会发生不好的事情。",
                    "每次女孩服务顾客后青楼就会变脏。 你应该要及时进行打扫，否则你最终会花费更多的钱。",
                    "如果你想招揽更多的顾客，可以尝试一下广告女郎。 不过宣传不要超出你的能力范围，不满意的顾客会降低你青楼的声誉。",
                    "不听话的女孩不太可能接受工作或培训。",
                    "性欲高的女孩更有可能同意和享受特殊服务，也可以为多个客户服务。",
                    "敏感的女孩善于让顾客开心，不管行为如何。",
                    "体质决定了一个女孩有多少精力，以及她能服务多少顾客。",
                    "魅力和敏感性使你的女孩在手交、口交和其他服务性行为方面做的更好。",
                    "当然，执行性服务需要良好的{b}性服务{/b}技能以及{b}敏感度{/b}。 {b}魅力{/b}和{b}皮绳愉虐{/b}技能也有帮助。",
                    "美貌和性欲对于正常的性行为很重要。",
                    "对于正常的性行为来说，{b}性交{/b}和{b}性欲{/b}技能越高越好。 {b}美容{/b}和{b}服务{/b}也有帮助。",
                    "身材和体质好的女孩可以很好地运用肛交。",
                    "肛交需要较高的{b}肛交{/b}技巧和良好的{b}体质{/b}。 {b}身体{/b}和{b}性交{/b}技能也有帮助。",
                    "优雅和服从对恋物性行为是有好处的。",
                    "一个女孩需要一个良好的{b}恋物{/b}和{b}服从{/b}的恋物性行为技能。 {b}优雅{/b}和{b}肛门{/b}技能也有帮助。",
                    "青楼报告中有很多关于青楼的有用信息。 如果你想了解某个女孩的信息，可以在女孩标签中查看她的统计数据。",
                    "工作时，女孩可以同时获得XP和JP。 XP允许一个女孩提高他们的统计数据和获得额外津贴，JP允许一个女孩在特定的工作或性行为中变得更好",
                    "顾客的口味在他们喜欢的娱乐和性行为上是不同的。 多样化是让所有顾客满意的关键。",
                    "每一个满意的客人都会增加青楼的名声。 但不满意的客人会诋毁你的青楼和你的女孩，所以要小心。",
                    "总的来说，顾客的满意来自两个因素:他们所得到的娱乐的服务质量，和你家女孩的品质。",
                    "女孩可能会变成双性恋，允许同一个顾客提供双飞服务。",
                    "女孩可以学习如何进行群交，允许她们同时服务两到三个顾客。",
                    "双飞和群交总是容易让顾客满意的。",
                    "保养对你的女孩来说很重要。 虽然心情好的女孩可能会暂时不计较，但如果她的保养费长期过低，她的情绪就会急剧下降。",
                    "虽然你的安全措施可以解决大多数问题，但是如果一个疯狂的顾客直接针对她们，你的女孩们最好好还是能有一些个人防卫措施。 不过要小心，你给她们任何武器都可能被用来对付你...",
                    "训练女孩房中术的最有效方法就是亲自上阵，但这很费时。 也许你可以找个人来帮你训练他们?",
                    "你遇到的一些人可以成为你女孩的教练。 一定要选一个最适合你管理风格的人。",
                    "在Zan中，善与恶的名声会产生很大的不同。 每一件好事或坏事都有后果。 当然，并非一切都是黑白分明的。 有些人喜欢在两者之间保持平衡...",
                    "我听说这个城市的各个地区都有道德败坏的女孩子。 你不会碰巧知道那件事吧?",
                    "商店里的那个女孩总是装模作样的卖弄风情......说实话我不喜欢她。 我希望我们能在城里找到别的地方购物。",
                    "你可以买到在奴隶市场受过训练的女孩。 这可以节省你的时间，尽管你永远不能百分百确定她们接受的训练质量。",
                    "通过和你的女孩的交谈，你可以了解她们，她们甚至可以告诉你她们的个人故事。",
                    "如果你善待她们，譬如让她们做自己喜欢的事，她们会更加容易爱上你。",
                    "如果你对她们太严厉，她们会害怕你，最好也不要强迫她们做不想做的事。",
                    "当所有所有的努力都失败时，你可以教训你的女孩以便她们能够接受训练。 此事唯一有用的就是你的魅力了。",
                    "你的力量决定了你在战斗中有多出色，或者决定了你在完成各种体能活动时有多出色。",
                    "你的精神决定了你在使用、探测和抵抗魔法方面的能力。",
                    "魅力对于所有的互动都很重要，无论是和你的女孩还是在外面的世界。",
                    "你的速度决定了你每天可以采取多少行动。 它很少用于其他用途。",
                    "不快乐的女孩可能会逃离你。 如果你雇不起赏金猎人，你最后的机会就是自己去探索这座城市。",
                    "别忘了升级青楼的卧室。 如果卧室质量低于标准，女孩和顾客的心情都会变糟，尤其是在提升了青楼等级之后。",
                    "普通房间只能接待有限数量的顾客。 确保你有足够的空间招待每个人。",
                    "当一个女孩加入你的青楼时，你必须为她事先准备一个房间。 否则，您可能要等到扩建后才能接收她。",
                    "有些人在城里到处卖稀奇古怪的东西，甚至是怪物或动物。 我不知道你需要它们做什么。",
                    "房中术(性技能)不能通过升级来提高。 唯一的途径就是用实战经验来提升它们。",
                    "课程有助于更快地提高女孩的低级技能。",
                    "每个女孩都有自己的声望，与你的青楼声望不同。 声望是一个女孩晋升品阶的关键。",
                    "提高女孩声望的最好方法是让她在外派任务中取得成功。",
                    "性奴隶获得来自奴隶工会的品阶评级。 品阶决定很多东西，包括最高等级和最高技能。",
                    "在品阶最低时，女孩的技能限制在50。 每增加一级，技能上限提高50点。",
                    "当一个女孩升级时，她会根据她当前的等级获得技能点。 而且，她每升两级就会获得额外奖励。",
                    "每升5级，就会有一个女孩获得额外的奖励点。",
                    "无论如何，一位女孩的等级不可能超过25级。",
                    "我听说过在奴隶公会里关于一个神秘品阶的谣言，它的评价甚至高于'S'。",
                    "求你了，主人，千万不要让你的账户变成负数!我听说有些人会在你欠债的时候用一些见不得人的交易来引诱你，但那只会给你带来更多的麻烦。",
                    "永远不要相信精灵。 别跟我说我没警告过你。",
                    "在更高级别的职位上，融入新的女孩获得工作上的认可可能会很困难。确保使用课程、物品、装扮和其他奖励来帮助新来的女孩迅速获得成功。",
                    "当你觉得你已经看过了所有的事件，你可以在游戏选项菜单中禁用一些夜间事件的展示。",
                    "不喜欢随机命名生成?您可以在游戏选项菜单中禁用它。",
                    "不想看到那些非常硬核的性的行为?在游戏选项菜单中禁用它们。",
                    "点击“Ctrl”可以跳过夜间事件或任何你已经看过的对话。",
                    "右键点击会让你后退一步。 右键单击主菜单将显示常规设置菜单。",
                    "在白天任何时候都可以用“H”键回到主屏幕。",
                    "按“E”键结束白天的工作，继续晚上的事件。",
                    "法术可以自动施法，使用你在一天结束时剩下的所有动作力。",
                    "按下“Esc”或“O”键将显示选项菜单",
                    "您可以使用“L”键返回最近访问的位置。",
                    "每当你或你的女孩发生性行为时，你就会获得个人声望。 声望会让你自己提升等级。",
                    "你的被动技能不会超过10个，但物品和魔法效果不受此限。",
                    "处女在失贞后会得到一种新的特质，这取决于发生这种特质的条件。",
                    "如果你的女孩心情不好，你一定要给她们足够的薪水，让她们的住宿足够舒适。"
                    "广告增加了每个客户的最大金额。 确保他们带个鼓鼓的钱包!",
                    "课程可能可以让女孩的技能超过她们的平均水平。 如果你有钱买的话很方便。",
                    "一段时间后，有经验的女孩很难提高更高的技能。 课程可以帮助你解决这个问题。",
                    "虽然工作和性行为依赖于几项主要技能，但拥有其他高技能通常可以稍微提升女孩的业绩。",
                    "即使识别一个裸体女孩应该很容易，但人们永远无法就'裸体'是什么达成一致! 你相信吗?",
                    "公开行为会令人困惑。 她是公开的，因为它在外面，还是因为其他人可以看到你? 我永远说不出来。",
                    "您可以使用 F5 快速保存并使用 F9 快速加载(当快捷键处于活动状态时)。 这是什么意思? 我不知道!",
                ]


    ## MC ##

    all_MC_stats = ["strength", "spirit", "charisma", "speed"]

    MC_playerclass_description = {
                                  "Warrior" : "你是个战士。你可能还年轻，但你经历过的血战不止这些。你在战斗和保护青楼中更强大.",
                                  "Wizard" : "你是个巫师。人们臣服于你的意志和魔法。你可以使用最多的法术.",
                                  "Trader" : "你是个奸商。你从年轻时混迹江湖开始就一直在努力。你可以做更好的交易，拿到最好的价格."
                                  }
    MC_stat_description = {
                            "strength" : "这是你角色的当前力量。 提高安全性并有助于个人战斗.",
                            "spirit" : "这是你角色的魔法强度。精神是你法力的来源，并在事件中提高法术效果.",
                            "charisma" : "这涵盖了你的角色个性，外表和演讲技巧。 在交互过程中改善结果.",
                            "speed" : "这是你角色的精力水平。 增加您可以执行的操作数量."
                            }

    god_description = {
                        "Arios" : "你崇拜阿里奥斯，光明之神和天使之主.",
                        "Shalia" : "你崇拜莎莉娅，阴影女神和夜晚的统治者.",
                        None : "你们不敬拜神，倒喜爱自然界的奇事."
                        }

    alignment_description = {
                            "good" : "你的行为表明你是个好人。与你的女孩之间基于爱的互动比基于恐惧的互动更成功.",
                            "evil" : "你是个邪恶的人，沉溺于自己的残忍。与女孩之间基于恐惧的互动比基于爱情的互动更成功.",
                            "neutral" : "你是中立的，宁愿在自己的利益和他人的利益之间保持平衡。基于爱和恐惧的互动同样成功."
                            }



    ## INVENTORY ##

    MC_inventory_slots = ["hands", "accessory", "misc"]
    girl_inventory_slots = ["hands", "body", "neck", "finger", "accessory", "misc"]
    inventory_filters = {
                         "base" : [None, "weapon", "clothing", "trinket", "consumable", "misc"],
                         "minion_merchant" : [None, "misc"],
                         "Accessory" : [None, "trinket"],
                         "Flower" : [None, "misc"],
                         "Weapon" : [None, "weapon"],
                         "Toy" : [None, "consumable"],
                         "Ring" : [None, "trinket"],
                         "Gift" : [None, "misc"],
                         "Dress" : [None, "clothing"],
                        }

    sorter_dict = {
                    "alpha" : ["A-z", "name", "名字"],
                    "badge" : ["徽章", "badge", "徽章"],
                    "price" : ["价值", "price", "价值"],
                    "type" : ["类型", "filter", "物品类型"],
                    "level" : ["等级", "level", "女孩的等级"],
                    "rank" : ["品阶", "rank", "奴隶的品阶"],
                    "job" : ["工作", "job_sort_value", "女孩的工作"],
                    "experience" : ["历练", "training_value", "性训练水平"],
                    }

    ## RESOURCES ##

    build_resources = ["wood", "leather", "dye", "marble", "ore", "silk", "diamond"]

    # Exchange rates are stored as fractions for display in the resource market tab

    resource_gold_value = {2 : Fraction(200, 1), 3 : Fraction(1000, 1), 4 : Fraction(4000, 1)} # This is the buy value. Sell value is 25% of buy value
    resource_sell_discount = 0.1 # Adjust this as necessary

    resource_base_exchange_rate = {
                                    2 : {2 : Fraction(1, 3), 3 : Fraction(1, 9), 4 : Fraction(1, 81)},
                                    3 : {2 : Fraction(1, 1), 3 : Fraction(1, 3), 4 : Fraction(1, 27)},
                                    4 : {2 : Fraction(12, 1), 3 : Fraction(4, 1), 4 : Fraction(1, 1)},
                                    }



    ## ALERTS ##

    seen_alerts = defaultdict(bool)


    ## LICENCES ##

    license_dict = {
                    0 : ("No license", "missing license.webp"),
                    1 : ("Pimp license", "license1.webp"),
                    2 : ("Whoremonger license", "license2.webp"),
                    3 : ("Brothelmaster license", "license3.webp")
                   }



    ## BROTHEL PICS AND ROOMS ##

init python:

    brothel_images = {1 : renpy.image("brothel1", im.Scale("brothels/" + brothel_pics[1], config.screen_width, config.screen_height)),
                      2 : renpy.image("brothel2", im.Scale("brothels/" + brothel_pics[2], config.screen_width, config.screen_height)),
                      3 : renpy.image("brothel3", im.Scale("brothels/" + brothel_pics[3], config.screen_width, config.screen_height)),
                      4 : renpy.image("brothel4", im.Scale("brothels/" + brothel_pics[4], config.screen_width, config.screen_height)),
                      5 : renpy.image("brothel5", im.Scale("brothels/" + brothel_pics[5], config.screen_width, config.screen_height)),
                      6 : renpy.image("brothel6", im.Scale("brothels/" + brothel_pics[6], config.screen_width, config.screen_height)),
                      7 : renpy.image("brothel7", im.Scale("brothels/" + brothel_pics[7], config.screen_width, config.screen_height)),
                      }

    # ROOMS #

    room_dict = {
                1 : Room("Basic room", 1),
                2 : Room("+Basic room+", 2),
                3 : Room("*Basic room*", 3),
                4 : Room("Standard room", 4),
                5 : Room("+Standard room+", 5),
                6 : Room("*Standard room*", 6),
                7 : Room("Elegant room", 7),
                8 : Room("+Elegant room+", 8),
                9 : Room("*Elegant room*", 9),
                10 : Room("Noble suite", 10),
                11 : Room("+Royal suite+", 11),
                12 : Room("*Imperial suite*", 12)
                }

    common_room_dict = {
                        "tavern" : Room("tavern", 0, "special", job = "waitress"),
                        "club" : Room("strip club", 0, "special", job = "dancer"),
                        "onsen" : Room("onsen", 0, "special", job = "masseuse"),
                        "okiya" : Room("okiya", 0, "special", job = "geisha"),
                        }

    master_bedrooms = {
                        0 : Room("Single room", level=0, type="master", cost=0),
                        1 : Room("Double room", level=1, type="master", cost=750),
                        2 : Room("Small suite", level=2, type="master", cost=2500),
                        3 : Room("Luxury suite", level=3, type="master", cost=7500),
                        4 : Room("Royal suite", level=4, type="master", cost=25000),
                        5 : Room("Royal harem", level=5, type="master", cost=75000),
                        }


#    all_common_rooms = [tavern, club, onsen, okiya]
    all_common_rooms = ["tavern", "club", "onsen", "okiya"]
    job_room_dict = {"waitress" : "tavern",
                     "dancer" : "club",
                     "masseuse" : "onsen",
                     "geisha" : "okiya",
                     "whore" : "bedroom"
                     }

    room_capacity_dict = {0 : 4, 1 : 4, 2 : 6, 3 : 8, 4 : 10, 5 : 12, 6 : 14, 7 : 16}

init -4 python:

    ## CITY BUTTONS

    location_tb = {"visit_willow" : "tb willow",
                             "visit_goldie" : "tb goldie",
                             "visit_watchtower" : "tb captain",
                             "visit_gina" : "tb gina",
                             "visit_thieves_guild" : "tb renza",
                             "visit_stella" : "tb stella",
                             "visit_giftgirl" : "tb giftgirl",
                             "visit_ramias" : "tb ramias",
                             "visit_gurigura" : "tb gurigura",
                             "visit_riche" : "tb riche",
                             "visit_katryn" : "tb katryn",
                             "visit_twins" : "tb twins",
                             "visit_bank" : "tb banker",
                             "visit_exchange" : "tb bast",
                             "visit_papa" : "tb papa",

                             "collect_wood" : "tb wood",
                             "collect_leather" : "tb leather",
                             "collect_dye" : "tb dye",
                             "collect_ore" : "tb ore",
                             "collect_marble" : "tb marble",
                             "collect_silk" : "tb silk",
                             "collect_diamond" : "tb diamond",
                            }

    ## FARM

    installation_price = {0: 100,
                          1: 250,
                          2: 500,
                          3: 1000,
                          4: 1750
                          }

    minion_xp_to_level = {0: 0,
                          1: 10,
                          2: 25,
                          3: 50,
                          4: 100,
                          5: 250
                          }

    minion_price = {0: 100,
                    1: 200,
                    2: 300,
                    3: 400,
                    4: 500,
                    5: 750
                    }

    minion_description = {"stallion" : "种马是血岛的男性性奴隶，魔法洗脑加上选择性地繁殖使它们拥有异常巨大的....",
                         "beast" : "野兽是Gizel在农场里养的各种各样的动物。更像是动物园，真的。",
                         "monster" : "怪物是不自然的恶魔，在克塞洛斯最黑暗的洞穴里爬行。它们有很多种形式，但有触角的总是最受欢迎。",
                         "machine" : "在Gizel的工作室里，机器或人工制品总是拥有众多用途，但实际上它们似乎只是为一件事而设计——性。"
                         }

    all_minion_types = ["stallion", "beast", "monster", "machine"]

    farm_pics = {"stallion" : [],
                 "beast" : [],
                 "monster" : [],
                 "machine" : []
                 }

    farm_holding_dict = {"libido" : "照看仆役\n{size=-24}     (+性欲){/size}",
                            "sensitivity" : "服侍Gizel\n{size=-24}     (+敏感){/size}",
                            "obedience" : "Cleaning up the farm (Ob)",
                            "constitution" : "Working outside (Con)",
                            "rest": "真的在休息",
                            }

    farm_description = {"stallion intro" : "%s在马厩和一匹悬挂得很好的种马过夜.",
                        "beast intro" : "%s 在兽栏里和一只肮脏下流的动物一起过夜.",
                        "monster intro" : "%s 和一个淫荡、恶心的家伙在怪物洞里过了一夜.",
                        "machine intro" : "%s 在车间里的一台又大又怪的机器旁过夜.",
                        "stallion intro plural" : "%s在马厩和%s匹悬挂得很好的种马过夜.",
                        "beast intro plural" : "%s在兽栏里和%s只肮脏下流的动物一起过夜.",
                        "monster intro plural" : "%s被%s个淫荡、恶心的怪物骚扰了一晚上.",
                        "machine intro plural" : "%s被绑在车间里在%s台又大又奇怪的机器边上过了一夜.",
                        "naked intro" : "Gizel示意%s在%s面前裸露身体.",
                        "service intro" : "Gizel把%s推倒在地，并示意她为%s服务.",
                        "sex intro" : "Gizel命令%s准备好让%s艹.",
                        "anal intro" : "Gizel要求%s把屁股抬高让%s走后门.",
                        "fetish intro" : "Gizel把墙上的链子拿给%s看， 说她会看着%s得逞的.",
                        "bisexual intro" : "Gizel决定加入%s和%s一起玩.",
                        "group intro" : "Gize命令%s今晚将要和一群%s发生群交行为.",

                        "stallion good" : " %s目不转睛地盯着种马那坚硬如铁的大屌. {color=[c_green]}她的训练进行得很顺利.{/color}",
                        "stallion average" : " %s看到种马的勃起的阴茎那么大，这让她印象深刻，还有些担心. {color=[c_white]}她的训练进行得很正常.{/color}",
                        "stallion bad" : " %s被种马的大鸡巴吓了一跳，她害怕地往后退缩. {color=[c_red]}她的训练进行得不顺利.{/color}",
                        "beast good" : " %s很好奇，被野兽生殖器奇怪的形状和气味所唤醒. {color=[c_green]}她的训练进行得很顺利.{/color}",
                        "beast average" : " %s在动物和它们奇怪的身体周围感到不舒服. {color=[c_white]}她的训练进行得很正常.{/color}",
                        "beast bad" : " %s简直不敢相信自己会被当作农场里的动物对待，于是她尽可能地远离野兽. {color=[c_red]}她的训练进行得不顺利.{/color}",
                        "monster good" : " %s对怪物散发的信息素产生了难以置信的兴奋感. {color=[c_green]}她的训练进行得很顺利.{/color}",
                        "monster average" : " %s味道怪物散发出来的奇怪的香味而感到虚弱和困惑. {color=[c_white]}她的训练进行得很正常.{/color}",
                        "monster bad" : " %s感到厌恶和恶心，只因为怪物散发出来的恶臭味. {color=[c_red]}她的训练进行得不顺利.{/color}",
                        "machine good" : " 金属的冰冷和橡胶弹性对皮肤触感使%s她兴奋不已. {color=[c_green]}她的训练进行得很顺利.{/color}",
                        "machine average" : " %s在一个满是稀奇古怪的性玩具的车间里，看着一个怪异的、振动着的性玩具让她感觉很奇怪. {color=[c_white]}她的训练进行得很正常.{/color}",
                        "machine bad" : " %s被机器刺眼的灯光和威胁性的外形吓坏了，完全无法放松. {color=[c_red]}她的训练进行得不顺利.{/color}",

#                        "naked result good" : "{color=[c_green]}%s was aroused by having her body on display before the %s, her nipples becoming visibly erect.{/color} Gizel pinched them hard, teasing her mercilessly.",
#                        "naked result average" : "{color=[c_white]}%s felt confused and ashamed, standing naked and exposed.{/color} She blushed as Gizel made her display every part of her body to the %s.",
#                        "naked result bad" : "{color=[c_lightred]}%s cowered and cried as she was made to stand naked in front of the %s.{/color}.Gizel commented harshly on her poor performance.",
#                        "service result good" : "{color=[c_green]}%s kneeled and starting working on the %s. She did her best to frown and hide her enjoyment, but Gizel could see she was getting wet.{/color}",
#                        "service result average" : "{color=[c_white]}%s did what she was asked, polishing the %s's strange dick with her lips and tongue.{/color}",
#                        "service result bad" : "{color=[c_lightred]}Tears ran down %s's cheeks as the %s forcefully fucked her throat.{/color}",
#                        "sex result good" : "{color=[c_green]}%s could hardly hide her sighs and screams of pleasure as the %s started fucking her mercilessly.{/color}",
#                        "sex result average" : "{color=[c_white]}%s shivered and moaned as the %s pumped its large, strange dick back and forth inside her tight pussy.{/color}",
#                        "sex result bad" : "{color=[c_lightred]}%s screamed in pain and fought weakly as the %s violently fucked her.{/color}",
#                        "anal result good" : "{color=[c_green]}%s yelled with pleasure as her ass got ravaged by the %s's large cock.{/color}",
#                        "anal result average" : "{color=[c_white]}%s moaned with a mix of pain and shameful pleasure as the %s violated her asshole.{/color}",
#                        "anal result bad" : "{color=[c_lightred]}%s screamed in pain and cried bitterly as the %s forced its large cock inside her tight asshole.{/color}",
#                        "fetish result good" : "{color=[c_green]}%s squirmed with confusion and pleasure, and quickly reached climax as the %s relentlessly violated her bound body.{/color}",
#                        "fetish result average" : "{color=[c_white]}%s screamed and moaned as the %s inflicted a strange mix of pain and pleasure on her weak body.{/color}",
#                        "fetish result bad" : "{color=[c_lightred]}%s shrieked with pain as the %s ruthlessly defiled her defenseless body.{/color}",
#                        "bisexual result good" : "{color=[c_green]}%s and Gizel strated licking and fingering each other's pussy, and soon forgot the %s as they passionately brought each other to climax.{/color} Gizel was very satisfied.",
#                        "bisexual result average" : "{color=[c_white]}Gizel forced %s to service both her and the %s.{/color} They both came forcefully on the poor girl's face. She was left confused by the whole ordeal.",
#                        "bisexual result bad" : "{color=[c_lightred]}%s was disgusted and tried to let out muffled screams as Gizel forcefully buried her pussy into her face, nearly choking her, while the %s tended to her other holes.{/color}",
#                        "group result good" : "{color=[c_green]}As %s and the %ss fucked in a variety of positions, she started enjoying herself and taking the lead, showing the minions which holes to use invitingly.{/color}",
#                        "group result average" : "{color=[c_white]}Grumbling, %s followed orders and used all of her holes to pleasure the %ss. However, she didn't seem to hate it as much as she was pretending to.{/color}",
#                        "group result bad" : "{color=[c_lightred]}%s cried and screamed as the %ss took turns violating her body.{/color} Gizel kept tauting her during the whole ordeal as she sobbed silently.",
                        "pen obedience": "%s回想起把她带到农场的不幸境遇和种种恶行。她觉得当时如果听话点，也许就不会惹麻烦了。{/color}",
                        "pen constitution": "即使她被锁在家里，%s也决心保持健康. {color=[c_green]}她做了一些腹肌锻炼和俯卧撑，变得更健康了.{/color}",
                        "pen sensitivity": "%s感到无聊，开始思考农场里那些奇怪的生物，以及它们更“不寻常”的特征。 {color=[c_green]}不久，她的脸就红了，而且莫名其妙地兴奋起来.{/color}",
                        "pen libido": "%s感到无聊和饥渴，所以她决定在农场听着那些奇怪的声音自慰一会儿. {color=[c_green]}她很享受这些.{/color}",
                        "holding obedience" : "Gizel派%s去打扫农场，告诉她要擦洗谷仓的每一个角落，清洗地板上的污渍。%s按照她的要求做了，而不是去面对魔法鞭笞的威胁.",
                        "holding constitution" : "Gizel命令%s在马道上绕着农行跑了一圈，每当她发现%s减速时，就狠狠地用鞭子抽她.",
                        "holding sensitivity" : "Gizel用%s作为她的私人仆人来追求她变态的幻想，强迫她舔身体，用各种各样的玩具玩弄那些饥饿的洞洞. 这很困难，但%s还是学到了新东西.",
                        "holding libido" : "Gizel要求%s照顾仆役：喂养它们，清洁它们，帮助它们“释放压力”。%s在她工作的过程中，她了解到很多关于仆役们独特的体征特点.",
                        "holding obedience good": "作为一个额外的挑战，Gizel让%s在她持续工作的时候穿上紧缚身体的绳子。 {color=[c_green]}粗糙的绳子以一种既不舒服又奇怪的方式摩擦着她的身体.{/color}",
                        "holding obedience bad": " {color=[c_lightred]}%s厌恶Gizel的仆役留下的所有污秽和体液.{/color}",
                        "holding constitution good": " Gizel认为在室外不穿衣服会让%s更加狂野，于是她让她光着身子跟动物一起跑。{color=[c_green]}在户外和动物一起裸体让她觉得自己的身心更愉悦.{/color}",
                        "holding constitution bad": " {color=[c_lightred]}当%s以创纪录的速度跑完一圈时，她轻蔑地看了Gizel一眼.{/color}",
                        "holding sensitivity good": " %s用熟练的舌头舔着Gizel勃起的阴蒂，给了她美妙的高潮。{color=[c_green]}她现在更熟悉如何取悦女人.{/color}",
                        "holding sensitivity bad": " Gizel把%s弄得筋疲力尽，气喘吁吁地倒在地上。{color=[c_lightred]}她的体格受到了影响.{/color}",
                        "holding libido good": " {color=[c_green]}花了几个小时照看各种仆从，让%s提高了她的技能.{/color}",
                        "holding libido bad": " {color=[c_lightred]}由于花了太多的时间去摆脱仆从的骚扰，%s的技能变得更差了.{/color}",
                        }

    farm_holding_stats = {"constitution" : ("naked", "obedience"), "obedience" : ("fetish", "libido"), "sensitivity" : ("bisexual", "constitution"), "libido" : ("service", "sensitivity")}

    farm_holding_tags = {"constitution" : ["run", "constitution"], "obedience" : ["obedience", "maid"], "sensitivity" : ["sensitivity"], "libido" : ["libido"]}

    pref_response = {
                    "modest refuses" : "我, %s? 不! ! !不! ! !别那样对我! *惊骇*",
                    "modest very reluctant" : "等等，%s? 这太离谱了! 太恶心了，太脏了.. .请停下! *吓坏*",
                    "modest reluctant": "不，不要这么看我... 不是的，%s... 我觉得太丢人了... *尴尬*",
                    "modest a little reluctant" : "我真的不想这样做，%s...错了...Ahaa! *害羞*",
                    "modest indifferent" : "Oh，又让我做%s... 你真是个变态... *脸红*",
                    "modest a little interested" : "嗯，好像我已经习惯了%s... 等等，我不是那个意思! *恐慌*",
                    "modest interested" : "Ah, %s... 还不赖... Mmmh... *脸红*",
                    "modest very interested" : "Oh，我想我喜欢%s... 我觉得自己像个荡妇... *呻吟*",
                    "modest fascinated" : "真不敢相信，%s感觉真好... 看看我! 我已经变成下流的婊子了! *喷射*",
                    "lewd refuses": "不,不要%s ! ! !别碰我，我讨厌!!!! *惊骇",
                    "lewd very reluctant": "我明明告诉过你我讨厌%s... 为什么我要一直这样做?啊! ! ! *羞愧*",
                    "lewd reluctant": "你知道我不喜欢%s... 别看着我... Ahaa! *窘迫*",
                    "lewd a little reluctant": "你又在对我做变态的事情，%s... 这让我感到奇怪... *害羞*",
                    "lewd indifferent": "Mmmh, %s... *脸红*",
                    "lewd a little interested": "Oh, %s, 这太棒了... *吻上她的嘴唇*",
                    "lewd interested": "Mmmh, %s... 我已经湿透了... *潮红*",
                    "lewd very interested": "Oh, %s, 它让我停不下来了... 我被人看的时候感觉挺舒服... Aaaah!!! *呻吟*",
                    "lewd fascinated": "Oh... 我要去了! Ahaaa, %s去了!!! *喷射*",
                    }

    minion_adjectives = {"stallion" : ["阴茎勃起的", "流着口水的", "好色的", "体态健美的", "喘着粗气的", "笨重的", "嘶鸣着的", "猥琐的"],
                         "beast" : ["流着口水的", "好色的", "满身污秽的", "肮脏的", "粗暴的", "兴奋的", "肥胖的"],
                         "monster" : ["好色的", "黏糊糊的", "满身污秽的", "肮脏的", "庞大的", "扭动的", "不可思议的", "怪异的", "猥琐的"],
                         "machine" : ["嗡嗡做响的", "怪异的", "不可思议的", "匪夷所思的", "着魔的", "复杂的", "隆起的"],
                         }

    minion_name_dict = {
                        "consonants" : ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"],
                        "vowels" : ["a", "e", "i", "o", "u", "y"],
                        "monster1" : ["gr", "kr", "le", "ry", "shr", "dr", "kz", "gz", "th", "bl", "kl", "wr", "qr", "mr", "sh"],
                        "monster2" : ["ck", "k", "rk", "rz", "rm", "xx", "uz", "oo", "hu", "qq", "tz", "zt", "rh", "th"],
                        }

    girl_name_dict = {"syllabs" : ["sha", "she", "shee", "shi", "wa", "ri", "ree", "ra", "ru", "ti", "ta", "ty", "ya", "yu", "sa", "so", "su", "se", "sy", "da", "de", "di", "do", "dy", "fa", "fe", "fio", "fia", "gi", "hu", "ha", "hyu", "ja", "ju", "ji", "ka", "ky", "ki", "kyo", "kyu", "la", "li", "le", "lo", "lu", "lyu", "lia", "lya", "lee", "loo", "za", "zi", "zu", "ze", "zee", "xa", "xy", "xe", "ca", "ce", "chi", "chu", "va", "vi", "vy", "ve", "bu", "be", "na", "ne", "ni", "nya", "nyu", "nee", "ma", "mu", "me", "mi", "myu", "mia", "mya"],
                      "fillers" : ["n", "r", "l", "s", "'", "", "", ""],
                      "enders" : ["n", "l", "nn", "a", "ya", "na", "ly", "", "", ""],
                      "last_syllabs" : ["jo", "sho", "to", "ya", "ma", "mi", "yo", "ko", "na", "ye", "yu", "ka", "ta", "fu", "ro", "sa", "shi", "ki", "no", "ra", "re", "tsu", "chi", "shi", "se", "n", "mu", "ne", "kyo", "ku"],
                      }


    farm_type_list = ["machine", "beast", "monster", "stallion"]
    farm_inst_list = ["stables", "pig stall", "monster den", "workshop"]
    farm_installations_dict = {"machine" : "workshop", "beast" : "pig stall", "monster" : "monster den", "stallion" : "stables"}


    ## CITY MERCHANTS

    merchant_dict = {"Stella" : "stallion", "Goldie" : "beast", "Willow" : "monster", "Gina" : "machine"}

    merchant_greetings = {
                          "Stella greeting" : "呦, 看谁来了。我希望你不要浪费我的时间.",
                          "Stella bought something" : "好吧，把金子给我，它就是你的了. 现在你可以走了，除非你还准备要买别的东西.{w=2.0}{nw}",
                          "Stella no money" : "你钱不够吧，伙计，离开这里.",

                          "Goldie greeting" : "我该如何帮助你",
                          "Goldie bought something" : "谢你！请小心轻放.{w=2.0}{nw}",
                          "Goldie no money" : "对不起，你现在好像没有钱.",

                          "Willow greeting" : "嘿，如果它不是我的友好邻居!你会惊奇地看到我刚刚抓到的东西.",
                          "Willow bought something" : "成交，就这样…你会玩得很开心的!{w=2.0}{nw}",
                          "Willow no money" : "哇, 这个小气鬼，想占我的便宜吗?你的袋子空了!",

                          "Gina greeting" : "Mmh, 如果我调整这个按钮…不，不是这样的……对不起。我能帮你什么忙吗?",
                          "Gina bought something" : "当然，反正我也不需要这个...{w=2.0}{nw}",
                          "Gina no money" : "先生，这些都是昂贵的设备. 除非你有钱买，否则不要碰它.",

                          "Riche greeting" : "噢,你好. *微笑*{w=2.0}{nw}",
                          "Riche bought something" : "谢谢你，希望下次再来!",
                          "Riche no money" : "哦,对不起... 但你还没拿到金币.",

                          "Ramias greeting" : "哦, 是你呀... 你好. *脸红*{w=2.0}{nw}",
                          "Ramias bought something" : "谢谢你！你不会失望的!",
                          "Ramias no money" : "嗯...看起来你的金币不太够.",

                          "Gurigura greeting" : "嗨~!!! *微笑*{w=2.0}{nw}",
                          "Gurigura bought something" : "谢谢，谢谢! Teeheehee.",
                          "Gurigura no money" : "嘿，等一下……先生，你的钱不够!",

                          "Katryn greeting" : "噢,你好. *微笑*{w=2.0}{nw}",
                          "Katryn bought something" : "多谢惠顾!",
                          "Katryn no money" : "对不起... 但你还没拿到金币.",

                          "Gift Shop Girl greeting" : "噢,你好. *微笑*{w=2.0}{nw}",
                          "Gift Shop Girl bought something" : "多谢惠顾!",
                          "Gift Shop Girl no money" : "对不起... 但你还没拿到金币。",

                          "Today greeting" : "嗨，大哥!我们能帮你什么忙? *微笑*{w=2.0}{nw}",
                          "Yesterday greeting" : "啊…你好... *脸红*{w=2.0}{nw}",
                          "Today bought something" : "谢谢你，大哥! *眨眼*",
                          "Yesterday bought something" : "谢谢.",
                          "Today no money" : "慢着，兄弟. 你好像没钱买这个.",

                          }


    shopgirl_comment = {"wood" : "新架子，太好了!",
                        "leather" : "太棒了!这个皮篮子很适合放在入口处.",
                        "dye" : "很好!这个新画的展览看起来很不错.",
                        "marble" : "哦，大理石柜台! 这将使所有其他店主感到嫉妒，耶!",
                        "ore" : "镀铜的柜台肯定会吸引一些人的注意. 非常漂亮.",
                        "silk" : "啊，终于有一些柔软光滑的丝绸来承载易碎物品了...揉我的脸!!",
                        "diamond" : "女孩最好的朋友…你很有风格，很帅!还有我的新镶钻显示器... ♥"}



    ## POPULATIONS ##

    pop_name_dict = {
                    "M beggars" : ("无赖", "穷酸男人", "乞丐", "流浪汉"),
                    "M thugs" : ("暴徒", "恶棍", "土匪", "小偷", "流氓", "窃贼"),
                    "M laborers" : ("劳工", "工人", "摊贩", "雇工", "农民"),
                    "M sailors" : ("海盗", "海员", "码头工", "大副", "海贼", "水手"),
                    "M commoners" : ("平民", "工头", "店员", "商人", "守卫", "建筑工", "助手"),
                    "M craftsmen": ("工匠", "技工", "铁匠", "木匠", "技师", "泥瓦匠"),
                    "M bourgeois" : ("操盘手", "簿记员", "草药医生", "店主", "客栈老板", "教士", "乡绅"),
                    "M guild members" : ("公会成员", "发明家", "魔术师", "奴隶贩子", "香料商人", "守卫队长"),
                    "M patricians" : ("航海家", "地主", "银行家", "市政府官员", "骑士", "主教"),
                    "M aristocrats" : ("贵族", "勋爵", "绅士", "宫廷巫师", "廷臣", "城主", "公会会长"),
                    "M nobles" : ("权贵", "伯爵", "名门家主", "骑士长", "大亨", "准伯爵", "子爵", "枢机主教"),
                    "M royals" : ("侯爵", "亲王", "总督", "公爵", "大主教", "苏丹"),

                    "F beggars" : ("女无赖", "衣衫褴褛的女人", "乞丐", "女流浪汉"),
                    "F thugs" : ("女暴徒", "女恶棍", "土匪夫人", "女贼", "女流氓", "老巫婆"),
                    "F laborers" : ("女劳工", "女工人", "女摊贩", "女佣", "女农民"),
                    "F sailors" : ("女海盗", "女海员", "码头女郎", "女船友", "船上的护士", "女水手"),
                    "F commoners" : ("女平民", "女工头", "女文员", "女商人", "女警卫", "尼姑"),
                    "F craftsmen": ("女工匠", "女技工", "女铁匠", "女木匠", "女泥瓦匠"),
                    "F bourgeois" : ("女操盘手", "女簿记员", "女药师", "女店主", "女老板", "女祭司", "乡绅夫人"),
                    "F guild members" : ("公会女成员", "女发明家", "女魔法师", "奴隶贩子", "香料女商人", "女警卫队长"),
                    "F patricians" : ("女航海家", "女地主", "女银行家", "女官员", "女骑士", "女主教"),
                    "F aristocrats" : ("贵族女士", "淑女", "女郎", "宫廷女巫", "闺秀", "女城主", "公会夫人"),
                    "F nobles" : ("贵族小姐", "女伯爵", "名门女士", "女祭司", "男爵夫人", "女子爵", "红衣主教女士"),
                    "F royals" : ("女佣人", "公主", "王妃", "公爵夫人", "母系氏族长", "苏丹娜")
                    }



    # Maximum difficulty for a given customer rank
    customer_rank_dict = {
                          1 : 40,
                          2 : 70,
                          3 : 110,
                          4 : 160,
                          5 : 1000,
                          }

    attract_pop_dict = {0 : "      ", 1 : "A few ", 2: "Some  ", 3 : "Many  ", 4 : "A lot ", 5 : "Loads "}

    # Encounters are tuples with label (used with prefix "city_") and probability. Tuples can be used with multiple labels

    encounters = (("none", 10), ("gossip", 30), ("ambush", 5), ("rob", 5), ("luck", 15), ("mob", 5), (("rape", "impress", "slave"), 10), (("gamble", "thief", "wrestle"), 10), (("cat", "secret", "gypsy"), 10))

    encounter_pics = {
                      "rape" : ("monster1.jpg", "monster2.jpg", "monster3.jpg", "monster4.jpg", "monster5.jpg", "monster6.jpg", "monster7.jpg", "monster8.jpg", "monster9.jpg", "monster10.jpg"),
                      "impress" : "impress0.jpg",
                      "impress1" : ("impress1_1.jpg", "impress1_2.jpg", "impress1_3.jpg", "impress1_4.jpg", "impress1_5.jpg", "impress1_6.jpg", "impress1_7.jpg", "impress1_8.jpg", "impress1_9.jpg", "impress1_10.jpg"),
                      "impress2" : ("impress2_1.jpg", "impress2_2.jpg"),
                      "impress3" : ("impress3_1.jpg", "impress3_2.jpg", "impress3_3.jpg"),
                      "impress4" : "impress4.jpg",
                      "slave" : ("slave1.jpg", "slave2.jpg", "slave3.jpg", "slave4.jpg", "slave5.jpg", "slave6.jpg", "slave7.jpg", "slave8.jpg", "slave9.jpg", "slave10.jpg"),
                      "slave_service" : (("slave service1.jpg","slave service2.jpg", "slave service3.jpg", "slave service4.jpg"), ("slave service5.jpg","slave service6.jpg", "slave service7.jpg", "slave service8.jpg")),
                      "slave_sex" : (("slave sex1.jpg","slave sex2.jpg", "slave sex3.jpg", "slave sex4.jpg"), ("slave sex5.jpg","slave sex6.jpg", "slave sex7.jpg", "slave sex8.jpg")),
                      "slave_anal" : (("slave anal1.jpg","slave anal2.jpg", "slave anal3.jpg", "slave anal4.jpg"), ("slave anal5.jpg","slave anal6.jpg", "slave anal7.jpg", "slave anal8.jpg")),
                      "slave_fetish" : (("slave fetish1.jpg","slave fetish2.jpg", "slave fetish3.jpg", "slave fetish4.jpg"), ("slave fetish5.jpg","slave fetish6.jpg", "slave fetish7.jpg", "slave fetish8.jpg")),
                      "slave_success" : ("slave service9.jpg","slave service10.jpg", "slave service11.jpg", "slave service12.jpg"),
                      "gamble" : (("gambler1_1.jpg", "gambler1_2.jpg", "gambler1_3.jpg"), ("gambler2_1.jpg", "gambler2_2.jpg", "gambler2_3.jpg"), ("gambler3_1.jpg", "gambler3_2.jpg", "gambler3_3.jpg"), ("gambler4_1.jpg", "gambler4_2.jpg", "gambler4_3.jpg"), ("gambler5_1.jpg", "gambler5_2.jpg", "gambler5_3.jpg"), ("gambler6_1.jpg", "gambler6_2.jpg", "gambler6_3.jpg"), ("gambler7_1.jpg", "gambler7_2.jpg", "gambler7_3.jpg"), ("gambler8_1.jpg", "gambler8_2.jpg", "gambler8_3.jpg"), ("gambler9_1.jpg", "gambler9_2.jpg", "gambler9_3.jpg")),
                      "thief" : ("thief1.jpg", "thief2.jpg", "thief3.jpg", "thief4.jpg", "thief5.jpg", "thief6.jpg"),
                      "wrestle" : ("arm wrestling1.jpg", "arm wrestling2.jpg", "arm wrestling3.jpg", "arm wrestling4.jpg", "arm wrestling5.jpg"),
                      "cat" : ("cat1.jpg", "cat2.jpg", "cat3.jpg", "cat4.jpg", "cat5.jpg", "cat6.jpg", "cat7.jpg", "cat8.jpg", "cat9.jpg", "cat10.jpg"),
                      "cat_found" : ("cat found.jpg",),
                      "cat_sex" : (("catsex1_1.jpg", "catsex1_2.jpg"), ("catsex2_1.jpg", "catsex2_2.jpg"), ("catsex3_1.jpg", "catsex3_2.jpg"), ("catsex4_1.jpg", "catsex4_2.jpg"), ("catsex5_1.jpg", "catsex5_2.jpg"), ("catsex6_1.jpg", "catsex6_2.jpg"), ("catsex7_1.jpg", "catsex7_2.jpg"), ("catsex8_1.jpg", "catsex8_2.jpg"), ("catsex9_1.jpg", "catsex9_2.jpg"), ("catsex10_1.jpg", "catsex10_2.jpg"), ("catsex11_1.jpg", "catsex11_2.jpg")),
                      "cat_duo" : (("catduo1_1.jpg", "catduo1_2.jpg", "catduo1_3.jpg", "catduo1_4.jpg"), ("catduo2_1.jpg", "catduo2_2.jpg", "catduo2_3.jpg", "catduo2_4.jpg"), ("catduo3_1.jpg", "catduo3_2.jpg", "catduo3_3.jpg", "catduo3_4.jpg")),
                      "secret" : ("secret1.jpg", "secret2.jpg", "secret3.jpg"),
                      "secret_empty" : ("secret empty1.jpg", "secret empty2.jpg", "secret empty3.jpg"),
                      "secret_girl" : ("secret girl1.jpg", "secret girl2.jpg", "secret girl3.jpg", "secret girl4.jpg", "secret girl5.webp", "secret girl6.jpg", "secret girl7.jpg", "secret girl8.jpg", "secret girl9.jpg", "secret girl10.jpg"),
                      "gypsy" : (("gypsy1_0.webp", "gypsy1_2.jpg", "gypsy1_3.jpg"), ("gypsy1_1.webp", "gypsy1_2.jpg", "gypsy1_3.jpg"), ("gypsy2_1.webp", "gypsy2_2.jpg", "gypsy2_3.jpg"), ("gypsy3_1.webp", "gypsy3_2.jpg", "gypsy3_3.jpg"), ("gypsy4_1.webp", "gypsy4_2.jpg", "gypsy4_3.jpg"), ("gypsy5_1.webp", "gypsy5_2.jpg", "gypsy5_3.jpg"), ("gypsy6_1.webp", "gypsy6_2.jpg", "gypsy6_3.jpg"), ("gypsy7_1.webp", "gypsy7_2.jpg", "gypsy7_3.jpg"), ("gypsy8_1.webp", "gypsy8_2.jpg", "gypsy8_3.jpg")),
                      "rob" : (("rob1_1.webp", "rob1_2.jpg"), ("rob2_1.webp", "rob2_2.jpg"), ("rob3_1.webp", "rob3_2.jpg"), ("rob4_1.webp", "rob4_2.jpg"), ("rob5_1.webp", "rob5_2.jpg"), ("rob6_1.webp", "rob6_2.jpg"), ("rob7_1.webp", "rob7_2.jpg"), ("rob8_1.webp", "rob8_2.jpg"), ("rob9_1.webp", "rob9_2.webp"), ("rob10_1.webp", "rob10_2.jpg")),
                      "ambush" : ("ambush1.jpg", "ambush2.jpg", "ambush3.jpg", "ambush4.jpg", "ambush5.jpg", "ambush6.jpg"),
                      "mob" : ("mob1.jpg", "mob2.jpg", "mob3.jpg"),
                      "mob_sex" : ("mob sex1.jpg", "mob sex2.jpg", "mob sex3.jpg"),
                      }


    ## WEEK DAYS ##

    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


    ## MC picture index

    MC_class_index = {"Warrior" : 0, "Wizard" : 3, "Trader" : 6}

    ## Roman numbers

    roman_numbers = {1 : "I", 2 : "II", 3 : "III", 4 : "IV", 5 : "V", 6 : "VI", 7 : "VII", 8 : "VIII", 9 : "IX", 10 : "X"}

    ## JOBS and SEX ACTS

    all_jobs = ["waitress", "dancer", "masseuse", "geisha"]
    all_sex_acts = ["service", "sex", "anal", "fetish"]
    extended_sex_acts = ["naked", "service", "sex", "anal", "fetish", "bisexual", "group"]
    farm_hardcore_acts = ["beast", "monster"]

    opposite_sex_acts = {"naked" : ["service", "sex", "anal", "fetish", "bisexual", "group"], # This is hardcoded for faster fixation picture search
                          "service" : ["sex", "anal", "fetish", "bisexual", "group"],
                          "sex" : ["service", "anal", "fetish", "bisexual", "group"],
                          "anal" : ["service", "sex", "fetish", "bisexual", "group"],
                          "fetish" : ["service", "sex", "anal", "bisexual", "group"],
                          "bisexual" : ["group"],
                          "group" : [],
                          None : [],
                        }

    normal_tags = ["profile", "portrait", "rest", "waitress", "dancer", "masseuse", "geisha"]
    all_farm_tags = ["big", "beast", "monster", "machine"]

    job_sort_value = {"whore" : 0, "waitress" : 10, "dancer" : 20, "masseuse" : 30, "geisha" : 40, None : 90, "hurt" : 80, "away" : 70, "farm" : 70}

    job_color = {"whore" : c_red, "waitress" : c_lightgreen, "dancer" : c_pink, "masseuse" : c_yellow, "geisha" : c_magenta, None : c_white, "hurt" : c_red, "away" : c_lightblue, "farm" : c_brown}


    ## STAT NAMES ##


    gstats_main = [
        "Charm",
        "Beauty",
        "Body",
        "Refinement",
        "Sensitivity",
        "Libido",
        "Constitution",
        "Obedience",
        ]

    gstats_sex = [
        "Service",
        "Sex",
        "Anal",
        "Fetish"
        ]


    ## STAT DESCRIPTION ##
    ## 统   计  描   述 ##

    gstats_dict = {
                    "Beauty" : "{b}美貌：{/b}她看上去真漂亮。影响按摩师的工作和性交效果. {p}目前作为按摩师的能力: {b}%s{/b}.",
                    "Body" : "{b}身材：{/b}她的身材多么匀称，多么结实。影响工作效果，如舞蹈和肛交行为. {p}目前作为舞者的能力: {b}%s{/b}.",
                    "Charm" : "{b}魅力：{/b}她有多少个性和风度。影响服务员和性服侍的工作效果. {p}目前作为服务员的能力: {b}%s{/b}.",
                    "Refinement" : "{b}优雅：{/b}她是多么的聪明博学，举止文雅。影响艺伎和皮绳愉虐性行为效果. {p}目前作为艺妓的能力: {b}%s{/b}.",
                    "Libido" : "{b}性欲：{/b}她是多么渴望性啊。影响性交效果，并增加她能与之发生性关系的顾客数量. {p}目前作为妓女的能力: {b}%s{/b}.",
                    "Sensitivity" : "{b}敏感：{/b}她对自己的身体和伴侣是多么的敏感。影响性服侍效果，提高顾客满意度.",
                    "Constitution" : "{b}体格：{/b}她有多大的耐力。影响肛交效果和提高她的最大精力.",
                    "Obedience" : "{b}服从：{/b}她多么能接受命令和奴役。影响皮绳愉虐性行为效果，降低她拒绝工作的机会.",
                    "Service" : "{b}性服侍：{/b}她做手交、口交和其他性服侍行为有多好.",
                    "Sex" : "{b}性交：{/b}她有多擅长性交行为.",
                    "Anal" : "{b}肛交：{/b}她有多擅长肛交行为.",
                    "Fetish" : "{b}皮绳愉虐：{/b}她对BDSM(绳缚与调教\支配与臣服\施虐与受虐)和其他不寻常的性行为有多在行."
                    }

    gstats_descript = {
                       "beauty" : "一个漂亮姑娘",
                       "body" : "一个身材火辣的姑娘",
                       "charm" : "一个迷人的姑娘",
                       "refinement" : "一个精致的女孩",
                      }

    gstat_job_skill = {
                        "Beauty" : "masseuse",
                        "Body" : "dancer",
                        "Charm" : "waitress",
                        "Refinement" : "geisha",
                        "Libido" : "whore",
                        }

    MC_stat_color = {
                    "strength" : "{color=[c_darkred]}%s{/color}",
                    "defense" : "{color=[c_darkred]}%s{/color}",
                    "spirit" : "{color=[c_darkblue]}%s{/color}",
                    "charisma" : "{color=[c_emerald]}%s{/color}",
                    "speed" : "{color=[c_lightblue]}%s{/color}",
                    }

    preference_color = {
                "refuses" : "{color=#F70000}%s{/color}",
#                 "extremely reluctant" : "{color=#FF2626}%s{/color}",
                "very reluctant" : "{color=#FF5353}%s{/color}",
                "reluctant" : "{color=#FF8E8E}%s{/color}",
                "a little reluctant" : "{color=#FFB5B5}%s{/color}",
                "indifferent" : "{color=[c_white]}%s{/color}",
                "a little interested" : "{color=#BDF4CB}%s{/color}",
                "interested" : "{color=#7CEB98}%s{/color}",
                "very interested" : "{color=#1FCB4A}%s{/color}",
                "fascinated" : "{color=[c_orange]}%s{/color}",
                None: "%s",
                }


    ## GIRL PERSONALITIES ##

#    base_interaction_limits = [-50, -15, 15, 50]

    alignment_bonus = {
                       "good_love" : 1.25,
                       "good_fear" : 0.75,
                       "neutral_love" : 1.0,
                       "neutral_fear" : 1.0,
                       "evil_love" : 0.75,
                       "evil_fear" : 1.25
                       }

    mood_description = {
                        "++++++" : "她感到幸福. 她的心情是{b}欣喜若狂{/b}.",
                        "+++++" : "她的心情是{b}兴高采烈{/b}.",
                        "++++" : "她的心情是{b}喜上眉梢{/b}.",
                        "+++" : "她的心情是{b}高兴{/b}.",
                        "++" : "她很满意.",
                        "+" : "她的心情是{b}满足{/b}.",
                        "0" : "她的心情是{b}平静{/b}.",
                        "-" : "她的心情是 {b}不满{/b}.",
                        "--" : "她的心情是{b}不满意.{/b}",
                        "---" : "她的心情是{b}不高兴{/b}.",
                        "----" : "她的心情是{b}非常不高兴{/b}.",
                        "-----" : "她的心情是{b}悲惨{/b}",
                        "------" : "她的生活是地狱. 她的心情是{b}糟透的{/b}.",

                        "change +++" : "她的情绪正在{b}迅速好转{/b}",
                        "change ++" : "她的情绪正在{b}改善{/b}",
                        "change +" : "她的情绪正在{b}开始改善{/b}",
                        "no change" : "她的情绪{b}稳定{/b}",
                        "change -" : "她的情绪正在{b}开始恶化{/b}",
                        "change --" : "她的情绪正在{b}恶化{/b}",
                        "change ---" : "她的情绪正在{b}迅速恶化{/b}",
                        }

    love_description = {
                        "++++++" : "你是她的一切。她崇拜你.",
                        "+++++" : "她非常喜欢你.",
                        "++++" : "她爱着你.",
                        "+++" : "她很喜欢你.",
                        "++" : "她喜欢你.",
                        "+" : "她认为你还行.",
                        "0" : "她不确定她对你的感觉.",
                        "-" : "她不太喜欢你.",
                        "--" : "她有点讨厌你.",
                        "---" : "她讨厌你.",
                        "----" : "她鄙视你.",
                        "-----" : "她非常讨厌你.",
                        "------" : "她认为你是最糟糕的。她想让你死.",
                        }

    fear_description = {
                        "++++++" : "她日夜生活在恐怖的世界里。她怕死你了.",
                        "+++++" : "你吓到她了.",
                        "++++" : "她很害怕你.",
                        "+++" : "她怕你.",
                        "++" : "她有点怕你.",
                        "+" : "她不信任你.",
                        "0" : "她对你很警惕.",
                        "-" : "她在你身边很紧张.",
                        "--" : "她在你身边很随和.",
                        "---" : "她在你身边很放松.",
                        "----" : "她觉得和你在一起很安全.",
                        "-----" : "她信任你.",
                        "------" : "她觉得自己受到了公主般的待遇。她完全信任你.",
                        "M++++++" : "她真正的位置是在你的脚下，在恐惧和欲望中颤抖.",
                        "M+++++" : "你越是伤害她，她就越开心.",
                        "M++++" : "看来她喜欢挨打。她想要更多.",
                        "M+++" : "她害怕你，但奇怪的是却被你吸引.",
                        "M---" : "她在你身边很放松，但感觉不太对劲.",
                        "M----" : "她觉得和你在一起很安全，但也很无聊.",
                        "M-----" : "她不明白你为什么对她这么好.",
                        "M------" : "她觉得这太过分了，她不应该得到这个。她似乎陷入困境.",
                        }




    # gpersonality_attributes = ("extravert", "introvert", "idealist", "materialist", "lewd", "repressed", "dom", "sub", "very extravert", "very introvert", "very idealist", "very materialist", "very lewd", "very repressed", "very dom", "very sub")

    personality_attributes = [("extravert", "introvert"), ("idealist", "materialist"), ("lewd", "modest"), ("dom", "sub")]

    attribute_score_dict = { # Note: very X and X boni/mali will add up
                            "very extravert" : {"very extravert" : 3, "extravert" : 1, "introvert" : -1, "very introvert" : -3},
                            "extravert" : {"very extravert" : 1, "extravert" : 1, "introvert" : 0, "very introvert" : -1},
                            "introvert" : {"very extravert" : -1, "extravert" : 0, "introvert" : 1, "very introvert" : 1},
                            "very introvert" : {"very extravert" : -3, "extravert" : -1, "introvert" : 1, "very introvert" : 3},

                            "very idealist" : {"very idealist" : 3, "idealist" : 1, "materialist" : -1, "very materialist" : -3},
                            "idealist" : {"very idealist" : 1, "idealist" : 1, "materialist" : 0, "very materialist" : -1},
                            "materialist" : {"very idealist" : -1, "idealist" : 0, "materialist" : 1, "very materialist" : 1},
                            "very materialist" : {"very idealist" : -3, "idealist" : -1, "materialist" : 1, "very materialist" : 3},

                            "very lewd" : {"very lewd" : 3, "lewd" : 1, "modest" : -1, "very modest" : -3},
                            "lewd" : {"very lewd" : 1, "lewd" : 1, "modest" : 0, "very modest" : -1},
                            "modest" : {"very lewd" : -1, "lewd" : 0, "modest" : 1, "very modest" : 1},
                            "very modest" : {"very lewd" : -3, "lewd" : -1, "modest" : 1, "very modest" : 3},

                            # The Dom/Sub table is reversed, this is on purpose

                            "very dom" : {"very dom" : -3, "dom" : -1, "sub" : 1, "very sub" : 3},
                            "dom" : {"very dom" : -1, "dom" : 0, "sub" : 1, "very sub" : 1},
                            "sub" : {"very dom" : 1, "dom" : 1, "sub" : 0, "very sub" : -1},
                            "very sub" : {"very dom" : 3, "dom" : 1, "sub" : -1, "very sub" : -3},
                            }

    gpersonalities_likes = {
                            "very extravert" :  {"cute" : 1, "book" : -3, "precious" : 0, "erotica" : -1, "drinks": 3},
                            "very introvert" :  {"cute" : -1, "book" : 3, "precious" : 0, "erotica" : 1, "drinks": -3},
                            "very idealist" :   {"cute" : 3, "book" : 1, "precious" : -3, "erotica" : 0, "drinks": -1},
                            "very materialist": {"cute" : -1, "book" : -3, "precious" : 3, "erotica" : 0, "drinks": 1},
                            "very lewd" :       {"cute" : -3, "book" : -1, "precious" : 0, "erotica" : 3, "drinks": 1},
                            "very modest" :     {"cute" : 3, "book" : 1, "precious" : 0, "erotica" : -3, "drinks": -1},
                            "very dom" :        {"cute" : -3, "book" : -1, "precious" : 1, "erotica" : 0, "drinks": 3},
                            "very sub" :        {"cute" : 1, "book" : 3, "precious" : -1, "erotica" : 0, "drinks": -3},

                            # "meek" :            {"cute" : 4, "book" : 2, "precious" : 0, "erotica" : -2, "drinks": 2},
                            # "nerd" :            {"cute" : 0, "book" : 4, "precious" : -2, "erotica" : 2, "drinks": 2},
                            # "pervert" :         {"cute" : -2, "book" : 0, "precious" : 2, "erotica" : 4, "drinks": 2},
                            # "rebel" :           {"cute" : 2, "book" : 0, "precious" : 2, "erotica" : -2, "drinks": 4},
                            # "superficial" :     {"cute" : 2, "book" : -2, "precious" : 4, "erotica" : 2, "drinks": 0},
                            # "cold" :            {"cute" : -2, "book" : 2, "precious" : 4, "erotica" : 0, "drinks": 2},
                            # "masochist" :       {"cute" : 0, "book" : 2, "precious" : -2, "erotica" : 4, "drinks": 2},
                            # "sweet" :           {"cute" : 4, "book" : 2, "precious" : 2, "erotica" : 0, "drinks": -2}
                            }

init python:
    gpersonalities = {
                        "pervert" : Personality(name="pervert", attributes=("very extravert", "very lewd"), description="Wild and 'no limit' kind of girl. Curious about all sorts of sexual acts, the more perverted the better. Doesn't care for romance."),
                        "rebel" : Personality(name="rebel", attributes=("very extravert", "very dom"), often_stories = ["slave_story5"], description="Always fighting and contradicting others, fiercely independent. Must do things of her own free will."),
                        "cold" : Personality(name="cold", attributes=("very materialist", "very introvert"), description="Cold and detached, she doesn't show her feelings easily. She seems strangely unconcerned about what goes on around her, and uninterested in the fate of others."),
                        "nerd" : Personality(name="nerd", attributes=("very introvert", "very idealist"), often_stories = ["slave_story8"], description="Quiet and bookish. Rather light-headed. Curious. Doesn't like physical effort."),
                        "masochist" : Personality(name="masochist", attributes=("very introvert", "very sub"), description="The lower the better. She likes to be at the bottom and secretly enjoys being mistreated. Gifts and loving gestures annoy her, she doesn't deserve them."),
                        "bimbo" : Personality(name="bimbo", attributes=("very materialist", "very lewd"), description="Vain, attention-craved, cares about status and wealth. Loves presents and compliments. She has no qualms about using her body to get those things, too."),
                        "meek" : Personality(name="meek", attributes=("very modest", "very sub"), often_stories = ["slave_story4"], rarely_stories = ["slave_story5","slave_story8"], description="Shy, easily swayed, will cry rather than resist. Doesn't like conflict."),
#                         "heartless" : Personality(name="heartless", attributes=("very materialist", "very dom"), description="Cold, calculating, domineering and selfish. Will always try to benefit at the expense of others."),
                        "sweet" : Personality(name="sweet", attributes=("very idealist", "very extravert"), description="Lovely and sunny personality. Always positive. Rather romantic. Doesn't like negativity."),

                        "superficial" : Personality(name="superficial", attributes=("very extravert", "very materialist"), description="Ever the socialite, cares about being seen, preferably in the most outstanding outfit and expensive jewelry. Some call her needy and craving for attention, but she knows they're just jealous of her new shoes..."),
                        "holy" : Personality(name="holy", attributes=("very extravert", "very modest"), never_stories = ["slave_story7","slave_story8"], description="A firebrand promoter of religion and morality, she prays every night for the salvation of her soul and tries to convert others to her beliefs. With little success so far, but she won't give up."),
                        "helper" : Personality(name="helper", attributes=("very extravert", "very sub"), description="Always ready to help her friends, places herself after others. Can be a bit nosy sometimes."),
                        "creep" : Personality(name="creep", attributes=("very introvert", "very lewd"), description="Shy and awkward around people, she is obsessed about all sorts of dirty topics that she researches in her own time. Get complaints for stalking, a lot."),
                        "repressed" : Personality(name="repressed", attributes=("very introvert", "very modest"), description="Raised in a very strict environment, she lives in fear of her own impulses and tries her hardest to suppress them."),
                        "schemer" : Personality(name="schemer", attributes=("very introvert", "very dom"), description="Likes nothing more than to scheme and make grand plans, ready to assert her dominance over all living beings... Some day. In the meantime, if she has to suck a dick... So be it."),
                        "prude" : Personality(name="prude", attributes=("very materialist", "very modest"), rarely_stories = ["slave_story7","slave_story8"], description="Affects to be a good, Arios-fearing girl at all times. Frowns on frivolity and amoral behavior. Some think she has dirty thoughts in secret, but if so, she hides them well."),
                        "princess" : Personality(name="princess", attributes=("very dom", "very materialist"), often_stories = ["slave_story6"], rarely_stories = ["slave_story1","slave_story2","slave_story3","slave_story5","slave_story7","slave_story8"], never_stories = ["slave_story4"], description="A figurative princess (or is she?), she thinks everyone ought to be at her service and deliver on her every whim. Can be cruel, but mostly she is naive."),
                        "pet" : Personality(name="pet", attributes=("very materialist", "very sub"), rarely_stories = ["slave_story5","slave_story8"], description="The teacher's pet. Always ready to please her master, likes nothing more than to live in comfort at his feet. Some despise her lack of independence, calling her unpleasant names behind her back."),
                        "easy" : Personality(name="easy", attributes=("very lewd", "very idealist"), description="It's not her fault, she has always attracted men, and never had the heart to turn them down. Although many call her easy, her sole purpose is to spread joy. Hopefully not STDs."),
                        "class president" : Personality(name="class president", attributes=("very modest", "very idealist"), often_stories = ["slave_story8"], description="Must always be on top, strives to be exemplary and despises every kind of misconduct. The high expectations she has of others mirror the harsh discipline whe puts herself through."),
                        "tsundere" : Personality(name="tsundere", attributes=("very idealist", "very dom"), description="Easy to anger, hard to please, she has a secret soft spot. Will put herself at risk to help others, then kick their butts for needing help in the first place."),
                        "loyal" : Personality(name="loyal", attributes=("very idealist", "very sub"), often_stories = ["slave_story2"], description="Always follows orders, out of a sense of duty more than fear. Thinks everyone must know their place, and do their best at whatever job they hold. Even whores."),
                        "yandere" : Personality(name="yandere", attributes=("very lewd", "very dom"), rarely_stories = ["slave_story3","slave_story7"], description="Very high on the hot and neurotic scale. Loving and devoted, but also firebatshit crazy. Ready to do anything to get her man and snuff out the competition, including... actually snuffing them out."),
                        "masochist2" : Personality(name="masochist", attributes=("very lewd", "very sub"), description="The lower the better. She likes to be at the bottom and enjoys all sorts of dirty things being imposed on her. Gifts and loving gestures annoy her, she doesn't deserve them."),
                        "stubborn" : Personality(name="stubborn", attributes=("very modest", "very dom"), description="Doesn't like people who don't share her principles and moral values, and doesn't like contradiction either. She's a lot of fun at parties, if you like parties that end with a tavern brawl."),
                     }

    gift_description = {
                        "cute" : "可爱的东西",
                        "book" : "书籍",
                        "precious" : "珍贵的东西",
                        "erotica" : "情趣用品",
                        "drinks" : "烈酒"
                        }


    gpersonalities_comment = {
                            "very extravert pos" : ("She's friendly.", "She's always ready to help.", "She's fun.", "She's lively."),
                            "very introvert pos" : ("She's nice.", "She's quiet.", "She doesn't gossip.", "She's soft-spoken."),
                            "very idealist pos" : ("She follows her dreams.", "She's smart.", "She knows a lot about everything.", "She's very clever."),
                            "very materialist pos" : ("She's down-to-earth", "She likes the finer things in life.", "She's ambitious.", "She has great taste."),
                            "very lewd pos" : ("She's open-minded.", "She's curious", "She knows how to party.", "She's a real party-girl."),
                            "very modest pos" : ("She's rational.", "She keeps her head cool.", "She's stable.", "She's pure."),
                            "very dom pos" : ("She's so confident.", "She's driven.", "She's very independent.", "She's fearless."),
                            "very sub pos" : ("She's humble.", "She's quiet.", "She's loyal.", "She's obedient."),

                            "very extravert neg" : ("She's self-absorbed.", "She's loud.", "She's self-centered.", "She won't shut up."),
                            "very introvert neg" : ("She's no fun.", "She's aloof.", "She's unfriendly.", "She's a bore."),
                            "very idealist neg" : ("She's nerdy.", "She's a snowflake.", "She's a snob.", "She's a nerd."),
                            "very materialist neg" : ("She's a nasty bitch.", "She's so superficial.", "She's selfish.", "She's a cold-hearted bitch."),
                            "very lewd neg" : ("She's a perv.", "She's depraved, even for a whore.", "She has no morals.", "She's a slut."),
                            "very modest neg" : ("She's boring.", "She thinks she's better than us.", "She's prissy.", "She's intolerant."),
                            "very dom neg" : ("She's arrogant.", "She's over-confident.", "She's a bully.", "She's manipulative."),
                            "very sub neg" : ("She's a pushover.", "She whines too much.", "She's a crybaby.", "She's a loser."),
                            }

    recent_event_templates = {  # Girl events given to the player for rewarding/punishing

                                # Rewardable events
                                "level up" : GirlRecentEvent(type="level up", action="获得一些经验", base_description="她变得更有经验了({color=[c_emerald]}等级%s{/color}).", discipline=False),
                                "rank up" : GirlRecentEvent(type="rank up", action="获得新的品阶", base_description="她已经到了{color=[c_emerald]}品阶%s{/color}.", discipline=False),
                                "job up" : GirlRecentEvent(type="job up", action="提升了工作技能", base_description="她增加了她的{color=[c_emerald]}%s{/color}技能.", discipline=False),
                                "good result" : GirlRecentEvent(type="good result", action="工作中表现良好", base_description="她在工作时的表现{color=[c_emerald]}%s{/color}(%s).", discipline=False),
                                "quest good result" : GirlRecentEvent(type="quest good result", action="任务中表现良好", base_description="%s", discipline=False),
                                "class good result" : GirlRecentEvent(type="class good result", action="培训中学习努力", base_description="%s", discipline=False),
                                "new act" : GirlRecentEvent(type="new act", action="尝试新事物", base_description="她第一次{color=[c_emerald]}接受了[act_description[%s]]训练{/color}.", discipline=False),
                                "helped" : GirlRecentEvent(type="helped", action="帮助朋友", base_description="", discipline=False), # Not implemented


                                # Neutral events
                                "exhausted" : GirlRecentEvent(type="exhausted", action="变得筋疲力尽", base_description="她把自己逼得太紧了，结果{color=[c_crimson]}筋疲力尽{/color}了."),
                                "sick" : GirlRecentEvent(type="sick", action="生病了", base_description="她 {color=[c_crimson]}生病{/color}了."),
                                "hurt" : GirlRecentEvent(type="hurt", action="受伤了", base_description="她被%sgeisha{color=[c_crimson]}强奸{/color}了."),
                                "defended" : GirlRecentEvent(type="defended", action="与客人争执", base_description="她{color=[c_emerald]}保护自己{/color}免于受到强奸."),


                                # Punishable events
                                "ran away" : GirlRecentEvent(type="ran away", action="Running away", base_description="She ran away, but you brought her back.", encourage=False),
                                "disobey" : GirlRecentEvent(type="disobey", action="Disobeying you", base_description="She {color=[c_crimson]}refused to work as a %s{/color}.", encourage=False),
                                "bad result" : GirlRecentEvent(type="bad result", action="Performing badly while working", base_description="She performed {color=[c_crimson]}%sly{/color} while working (%s).", encourage=False),
                                "quest bad result" : GirlRecentEvent(type="quest bad result", action="Performing badly on a quest", base_description="%s", encourage=False),
                                "class bad result" : GirlRecentEvent(type="class bad result", action="Not paying attention in school", base_description="%s", encourage=False),
                                "refused" : GirlRecentEvent(type="refused", action="Refusing training", base_description="She {color=[c_crimson]}refused to train (%s){/color}.", encourage=False),
                                "argued" : GirlRecentEvent(type="argued", action="Arguing with a rival", base_description="", encourage=False), # Not implemented

                                # Passive events (cannot be punished or rewarded=)
                                "acquired" : GirlRecentEvent(type="acquired", base_description="You have acquired %s.", encourage=False, discipline=False),
                                "MC met" : GirlRecentEvent(type="MC met", base_description="You have met %s.", encourage=False, discipline=False),
                                "MC friend" : GirlRecentEvent(type="MC friend", base_description="You and %s have become friends.", encourage=False, discipline=False),
                                "MC flower" : GirlRecentEvent(type="MC flower", base_description="You may now give %s flowers.", encourage=False, discipline=False),
                                "MC girlfriend" : GirlRecentEvent(type="MC friend", base_description="%s is now your girlfriend.", encourage=False, discipline=False),
                                "MC lover" : GirlRecentEvent(type="MC friend", base_description="%s is now your lover.", encourage=False, discipline=False),
                                "MC job" : GirlRecentEvent(type="MC job", base_description="You can now offer %s a job.", encourage=False, discipline=False),
                                "kidnapped" : GirlRecentEvent(type="kidnapped", base_description="She has been kidnapped by %s.", encourage=False, discipline=False),
                                }

    event_sounds = {
                    "perk 0" : s_surprise,
                    "perk 1" : s_ahaa,
                    "perk 2" : s_aaah,
                    "perk 3" : s_mmmh,
                    }



    base_reluctance = {"naked" : -375, "service" : -500, "sex" : -500,"anal" : -750, "fetish" : -750, "bisexual" : -750, "group" : -1000}

    preference_modifier =   {
                            "refuses" : 150, # preference <= 90% base_reluctance
#                            "extremely reluctant" : 100, # (obsolete)
                            "very reluctant" : 75, # preference <= 70% base_reluctance
                            "reluctant" : 50, # preference <= 50% base_reluctance
                            "a little reluctant" : 25, # preference <= 20% base_reluctance
                            "indifferent" : 0, # preference <= -20% base_reluctance
                            "a little interested" : -5, # preference = -50% base_reluctance
                            "interested" : -15, # preference <= -70% base_reluctance
                            "very interested" : -35, # preference <= -90% base_reluctance
                            "fascinated" : -75 # preference > -90% base_reluctance
                            }

    # Reminder: Base reluctance is negative

    preference_limit =  {
                            "refuses" : 3.0, # preference <= 90% base_reluctance
                            "very reluctant" : 0.9, # preference <= 70% base_reluctance
                            "reluctant" : 0.7, # preference <= 50% base_reluctance
                            "a little reluctant" : 0.5, # preference <= 20% base_reluctance
                            "indifferent" : 0.2, # preference <= -20% base_reluctance
                            "a little interested" : -0.2, # preference = -50% base_reluctance
                            "interested" : -0.5, # preference <= -70% base_reluctance
                            "very interested" : -0.7, # preference <= -90% base_reluctance
                            "fascinated" : -0.9 # preference > -90% base_reluctance
                            }

    experienced_description = {
                               "very experienced" : "Extensive",
                               "experienced" : "Advanced",
                               "average" : "Some",
                               "inexperienced" : "Basic",
                               "very inexperienced" : "None",
                               "very experienced ttip" : "{size=-1}{color=[c_orange]}A sex slave for years, she has known several masters and received extensive sexual training.{/color}",
                               "experienced ttip" : "{size=-1}{color=[c_green]}She has been a sex slave for many months now, and has received various forms of training.{/color}",
                               "average ttip" : "{size=-1}{color=[c_yellow]}She has been a sex slave for a few months already, and has received some sexual training.{/color}",
                               "inexperienced ttip" : "{color=[c_lightred]}She became a sex slave only recently, and still has a lot to learn.{/color}",
                               "very inexperienced ttip" : "{color=[c_red]}Fresh off the slave caravan, she has never been trained for sex. Who knows how she will react?{/color}",
                              }

    experienced_modifiers = {
                            "very experienced" : [250, 150, 75],
                            "experienced" : [150, 75, 25],
                            "average" : [75, 25, 0],
                            "inexperienced" : [25, 0, -25],
                            "very inexperienced" : [0, 0, -50],
                            }

    experienced_color = {
                           "very experienced" : c_orange,
                           "experienced" : c_green,
                           "average" : c_yellow,
                           "inexperienced" : c_lightred,
                           "very inexperienced" : c_red,
                          }

    sexual_training_value = {
                            "very experienced" : 1,
                            "experienced" : 2,
                            "average" : 3,
                            "inexperienced" : 4,
                            "very inexperienced" : 5,}

    long_act_description = {
                        "naked" : "being naked",
                        "service" : "giving service",
                        "sex" : "having sex",
                        "anal" : "anal sex",
                        "fetish" : "kinky sex",
                        "bisexual" : "sex with a woman",
                        "group" : "group sex",
                        "action naked" : "Nudity",
                        "action service" : "Service",
                        "action sex" : "Sex",
                        "action anal" : "Anal sex",
                        "action fetish" : "Fetish",
                        "action bisexual" : "Lesbian sex",
                        "action group" : "Group sex"
                        }

    # This filters choices for the training menu (OR clause)

    training_test_dict = {
                          "naked": [],
                          "service": [("naked", "reluctant"), ("service", "reluctant")],
                          "sex": [("naked", "indifferent"), ("service", "indifferent"), ("sex", "reluctant")],
                          "anal": [("sex", "indifferent"), ("anal", "reluctant")],
                          "fetish": [("anal", "indifferent"), ("service", "interested"), ("fetish", "reluctant")],
                          "fetish": [("anal", "indifferent"), ("service", "interested"), ("fetish", "reluctant")],
                          "bisexual": [("sex", "interested"), ("service", "interested"), ("bisexual", "indifferent")],
                          "group": [("anal", "interested"), ("sex", "fascinated"), ("group", "indifferent")],
                          }

    magic_training_test_dict = { # Suggestion training is easier
                          "naked": [],
                          "service": [],
                          "sex": [("naked", "reluctant"), ("service", "reluctant"), ("sex", "very reluctant")],
                          "anal": [("sex", "reluctant"), ("anal", "very reluctant")],
                          "fetish": [("anal", "reluctant"), ("service", "indifferent"), ("fetish", "very reluctant")],
                          "fetish": [("anal", "reluctant"), ("service", "indifferent"), ("fetish", "very reluctant")],
                          "bisexual": [("sex", "indifferent"), ("service", "indifferent"), ("bisexual", "reluctant")],
                          "group": [("anal", "a little interested"), ("sex", "very interested"), ("group", "a little reluctant")],
                          }

    ## MC interactions
    # The dictionary uses nested lists to retain choices order

    interact_dict = {
                    "chat" : ["GENERAL TOPICS", "PERSONAL TOPICS", "STORY"],
                    "GENERAL TOPICS" : [GirlInteractionTopic("chat", "chat", "Life as a slave", "slave_chat_slave_life"),
                                        GirlInteractionTopic("chat", "chat", "Life in the brothel", "slave_chat_brothel", condition="has_worked"),
                                        GirlInteractionTopic("chat", "chat", "Getting along with customers", "slave_chat_customers", condition="has_worked"),
                                        GirlInteractionTopic("chat", "chat", "Getting along with other girls", "slave_chat_other_girls", condition="other_girls"),
                                        ],
                    "PERSONAL TOPICS" : [
                                        GirlInteractionTopic("chat", "chat", "Her well-being", "slave_chat_well_being"),
                                        GirlInteractionTopic("chat", "chat", "Her feelings about you", "slave_chat_feelings"),
                                        GirlInteractionTopic("chat", "chat", "Her tastes", "slave_chat_tastes"),
                                        GirlInteractionTopic("chat", "chat", "Her origins", "slave_chat_origins"),
                                    ],
                    "STORY" : [GirlInteractionTopic("chat", "story", "Hear her story again", "slave_chat_story", AP_cost=0, condition = "story")],

                    "train" : ["SKILL TRAINING", "SEXUAL TRAINING", "SPECIAL TRAINING"],
                    "SKILL TRAINING" : [GirlInteractionTopic("train", "train", "Obedience training", "slave_train_obedience", act="obedience"),
                                        GirlInteractionTopic("train", "train", "Constitution training", "slave_train_constitution", act="constitution")],
                    "SEXUAL TRAINING" : [
                                        GirlInteractionTopic("train", "train", "Nude", "slave_train_sex_acts", act="naked", advanced=True),
                                        GirlInteractionTopic("train", "train", "Service", "slave_train_sex_acts", act="service", advanced=True),
                                        GirlInteractionTopic("train", "train", "Sex", "slave_train_sex_acts", act="sex", advanced=True),
                                        GirlInteractionTopic("train", "train", "Anal", "slave_train_sex_acts", act="anal", advanced=True),
                                        GirlInteractionTopic("train", "train", "Fetish", "slave_train_sex_acts", act="fetish", advanced=True),
                                        GirlInteractionTopic("train", "train", "Bisexual", "slave_train_sex_acts", act="bisexual", advanced=True),
                                        GirlInteractionTopic("train", "train", "Group", "slave_train_sex_acts", act="group", advanced=True),
                                    ],
                    "SPECIAL TRAINING" : [GirlInteractionTopic("train", "train", "Remove negative fixation", "slave_remove_fixation", condition="neg_fix")],

                    "magic" : ["MAGIC SKILL TRAINING", "MAGIC SEXUAL TRAINING", "CHOOSE METHOD"],
                    "CHOOSE METHOD" : [GirlInteractionTopic("magic", None, "Current method", "slave_hypnotize_method", AP_cost=0)], # None type excludes it from girl interaction count
                    "MAGIC SKILL TRAINING" : [
                                                GirlInteractionTopic("magic", "train", "Obedience training", "slave_magic", act="obedience", gold_cost=20),
                                                GirlInteractionTopic("magic", "train", "Sensitivity training", "slave_magic", act="sensitivity", gold_cost=20),
                                                GirlInteractionTopic("magic", "train", "Libido training", "slave_magic", act="libido", gold_cost=20),
                                                ],
                    "MAGIC SEXUAL TRAINING" : [
                                                GirlInteractionTopic("magic", "train", "Nude", "slave_magic", act="naked", advanced=True, gold_cost=20),
                                                GirlInteractionTopic("magic", "train", "Service", "slave_magic", act="service", advanced=True, gold_cost=40),
                                                GirlInteractionTopic("magic", "train", "Sex", "slave_magic", act="sex", advanced=True, gold_cost=50),
                                                GirlInteractionTopic("magic", "train", "Anal", "slave_magic", act="anal", advanced=True, gold_cost=60),
                                                GirlInteractionTopic("magic", "train", "Fetish", "slave_magic", act="fetish", advanced=True, gold_cost=70),
                                                GirlInteractionTopic("magic", "train", "Bisexual", "slave_magic", act="bisexual", advanced=True, gold_cost=80),
                                                GirlInteractionTopic("magic", "train", "Group", "slave_magic", act="group", advanced=True, gold_cost=100),
                                                ],

                    "react" : ["ENCOURAGE", "DISCIPLINE"],
                    "ENCOURAGE" : [
                                    GirlInteractionTopic("react", "reward", "Praise her", "slave_reward_praise"),
                                    GirlInteractionTopic("react", "reward", "Give her gold", "slave_reward_gold"),
                                    GirlInteractionTopic("react", "reward", "Give her a gift", "slave_reward_gift"),
                                    GirlInteractionTopic("react", "reward", "Pet her", "slave_reward_pet"),
                                    GirlInteractionTopic("react", "reward", "Give her a day off", "slave_reward_day"),
                                    GirlInteractionTopic("react", "reward", "Have sex with her", "slave_reward_sex"),
                                    ],
                    "DISCIPLINE" : [
                                    GirlInteractionTopic("react", "discipline", "Scold her", "slave_punish_scold"),
                                    GirlInteractionTopic("react", "discipline", "Remove upkeep", "slave_punish_upkeep"),
                                    GirlInteractionTopic("react", "discipline", "Force her to go naked", "slave_punish_naked"),
                                    GirlInteractionTopic("react", "discipline", "Beat her", "slave_punish_beat"),
                                    GirlInteractionTopic("react", "discipline", "Rape her", "slave_punish_rape"),
                                    GirlInteractionTopic("react", "discipline", "Send her to the farm", "slave_punish_farm", condition="farm"),
                                    ],
                    "misc" : ["CLOTHING", "MASTER BEDROOM", "DEBUG"],
                    "CLOTHING" : [
                                    GirlInteractionTopic("misc", None, "Tell her to go naked", "slave_clothing_naked", AP_cost=0, condition = "dressed"),
                                    GirlInteractionTopic("misc", None, "Tell her to get dressed", "slave_clothing_dressed", AP_cost=0, condition = "naked"),
                                    ],
                    "MASTER BEDROOM" : [
                                        GirlInteractionTopic("misc", None, "Send her to your bedroom", "slave_master_bedroom_add", AP_cost=0, condition = "master_bedroom_add"),
                                        GirlInteractionTopic("misc", None, "Remove her from your bedroom", "slave_master_bedroom_remove", AP_cost=0, condition = "master_bedroom_remove")
                                        ],
                    "DEBUG" : [GirlInteractionTopic("misc", None, "Cheat", "interaction_cheat_menu", AP_cost=0, condition="debug_mode"),
                        GirlInteractionTopic("misc", None, "Reset girl interactions", "interaction_cheat_girl", AP_cost=0, condition="debug_mode"),
                        GirlInteractionTopic("misc", None, "Reset MC interactions", "interaction_cheat_MC", AP_cost=0, condition="debug_mode"),
                        ],
                    }


    free_interact_dict = {
                            "chat" : ["GENERAL TOPICS", "PERSONAL TOPICS", "DEBUG"],
                            "GENERAL TOPICS" : [GirlInteractionTopic("chat", "chat", "Small talk", "free_chat_small_talk"),
                                                GirlInteractionTopic("chat", "chat", "Gossip", "free_chat_gossip"),
                                                GirlInteractionTopic("chat", "chat", "Life", "free_chat_life"),# love_test=5),
                                                GirlInteractionTopic("chat", "chat", "Love", "free_chat_love"),# love_test=5),
                                                ],
                            "PERSONAL TOPICS" : [
                                                GirlInteractionTopic("chat", "chat", "Her origins", "free_chat_origins", love_test=10),
                                                GirlInteractionTopic("chat", "chat", "Her hobbies", "free_chat_hobbies", love_test=10),
                                                GirlInteractionTopic("chat", "chat", "Likes", "free_chat_likes", love_test=10),
                                                GirlInteractionTopic("chat", "chat", "Dislikes", "free_chat_dislikes", love_test=10),
                                                ],
                            "fun" : ["JOKE", "TOUCH", "PLAY"],
                            "JOKE" : [
                                        GirlInteractionTopic("fun", "joke", "Harmless", "free_joke_harmless", love_test=15),
                                        GirlInteractionTopic("fun", "joke", "Adult", "free_joke_adult", love_test=15),
                                        GirlInteractionTopic("fun", "joke", "Dark", "free_joke_dark", love_test=15),
                                        GirlInteractionTopic("fun", "joke", "Mean", "free_joke_mean", love_test=15),
                                        ],
                            "TOUCH" : [
                                        GirlInteractionTopic("fun", "touch", "Hold her hand", "free_touch_hand", love_test=40),
                                        GirlInteractionTopic("fun", "touch", "Kiss", "free_touch_kiss", relationship_level=2),
                                        GirlInteractionTopic("fun", "touch", "Slap her ass", "free_touch_ass", love_test=55, relationship_level=3),
                                        GirlInteractionTopic("fun", "touch", "Touch her breasts", "free_touch_breasts", love_test=60, relationship_level=3),
                                        GirlInteractionTopic("fun", "touch", "Touch her pussy", "free_touch_pussy", love_test=65, relationship_level=3),
                                        ],
                            "PLAY" : [
                                        GirlInteractionTopic("fun", "play", "Get her naked", "free_play", act="naked", relationship_level=4),
                                        GirlInteractionTopic("fun", "play", "Ask for service", "free_play", act="service", relationship_level=4),
                                        GirlInteractionTopic("fun", "play", "Ask for sex", "free_play", act="sex", relationship_level=4),
                                        GirlInteractionTopic("fun", "play", "Ask for anal sex", "free_play", act="anal", relationship_level=4),
                                        GirlInteractionTopic("fun", "play", "Ask for fetish", "free_play", act="fetish", relationship_level=4),
                                        ],
                            "flirt" : ["COMPLIMENT", "SEXUAL TOPICS"],

                            "COMPLIMENT" : [
                                        GirlInteractionTopic("flirt", "compliment", "Compliment her beauty", "free_flirt_beauty", relationship_level=1),
                                        GirlInteractionTopic("flirt", "compliment", "Compliment her body", "free_flirt_body", relationship_level=1),
                                        GirlInteractionTopic("flirt", "compliment", "Compliment her mind", "free_flirt_mind", relationship_level=1),
                                        GirlInteractionTopic("flirt", "compliment", "Compliment her spirit", "free_flirt_spirit", relationship_level=1),
                                        ],
                            "SEXUAL TOPICS" : [
                                                GirlInteractionTopic("flirt", "chat about sex", "Her sexual experience", "free_flirt_sex_experience", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Her sexual tastes", "free_flirt_sex_tastes", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Nudity", "free_flirt_sex_act", act="naked", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Service", "free_flirt_sex_act", act="service", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Sex", "free_flirt_sex_act", act="sex", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Anal sex", "free_flirt_sex_act", act="anal", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Fetish acts", "free_flirt_sex_act", act="fetish", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Bisexuality", "free_flirt_sex_act", act="bisexual", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Group sex", "free_flirt_sex_act", act="group", love_test=55),
                                                ],
                            "give" : ["GIVE", "OFFER"],
                            "GIVE" : [
                                        GirlInteractionTopic("give", "gift", "Give her a present", "free_give_gift", love_test=20),
                                        GirlInteractionTopic("give", "gold", "Give her money", "free_give_gold", love_test=20),
                                        ],
                            "OFFER" : [GirlInteractionTopic("give", "offer", "Offer her a job", "free_offer_job", love_test=90, relationship_level=5),],
                            "DEBUG" : [GirlInteractionTopic("give", None, "Change love", "interaction_cheat_love", AP_cost=0, condition="debug_mode"),
                                        GirlInteractionTopic("give", None, "Reset girl interactions", "interaction_cheat_girl", AP_cost=0, condition="debug_mode"),
                                        GirlInteractionTopic("give", None, "Reset MC interactions", "interaction_cheat_MC", AP_cost=0, condition="debug_mode"),
                                        ],
                    }

    fix_description = {
                       "public acts description" : "doing it in public.",
                       "public acts action" : "Do it in public",
                       "public acts intro" : "You call in everyone from the brothel: girls, helpers, passersby... You tell %s that she must do it in public.",
                       "public acts pos_reaction" : "She blushes and you can see her nipples perking under her blouse. She is aroused by the thought of doing it in public.",
                       "public acts neg_reaction" : "She is indignant and complains that she can't do anything when people are watching. You ignore her.",

                       "cosplay description" : "wearing sexy and revealing outfits.",
                       "cosplay action" : "Wear a sexy outfit",
                       "cosplay intro" : "You give %s a choice of uniforms she can wear.",
                       "cosplay pos_reaction" : "She bites her lip, looking playful. She chooses a kinky uniform with holes for her tits, pussy and asshole.",
                       "cosplay neg_reaction" : "She chooses a rather conservative and boring uniform. She doesn't enjoy having to wear it.",

                       "dildos description" : "using sex toys while fucking.",
                       "dildos action" : "Use a dildo",
                       "dildos intro" : "You tell %s to use a dildo in her other hole while you're fucking her.",
                       "dildos pos_reaction" : "She easily slips the dildo in place. It looks like something she is used to doing a lot.",
                       "dildos neg_reaction" : "She hates it as she has to painfully force the dildo in. She doesn't enjoy it at all.",

                       "vibrators description" : "vibrators.",
                       "vibrators action" : "Use a vibrator",
                       "vibrators intro" : "You tell %s to use a vibrating egg while doing it.",
                       "vibrators pos_reaction" : "She wastes no time in using the egg on her ready clit, bringing herself to a state of heavy arousal.",
                       "vibrators neg_reaction" : "She is sensitive and uncomfortable using the egg, and complains that it feels weird.",

                       "dirty sex description" : "dirty sex",
                       "dirty sex action" : "Get down and dirty",
                       "dirty sex intro" : "You tell %s to get down in the dirt and get ready to be abused.",
                       "dirty sex pos_reaction" : "She seems happy to be on the ground, like a dirty bitch she is.",
                       "dirty sex neg_reaction" : "She hates dirt and complains that it is unhealthy.",

                       "penis worship description" : "worshiping dicks, especially large ones.",
                       "penis worship action" : "Make her rub your dick",
                       "penis worship intro" : "You tell %s that she has to rub oil on your dick and pay it proper respect.",
                       "penis worship pos_reaction" : "She takes a good look at your large, throbbing cock and seems happy and aroused that she can play with it. She plants a wet kiss right on the tip.",
                       "penis worship neg_reaction" : "She looks away from your erect dick, still uncomfortable around a man's cock.",

                       "bondage description" : "being tied up.",
                       "bondage action" : "Tie her up",
                       "bondage intro" : "Using tight ropes and your expert knowledge of bondage as a slave master, you tie %s up in an uncomfortable and embarrassing position.",
                       "bondage pos_reaction" : "She moans with pleasure as you tie her up, loving the feel of the ropes biting her skin.",
                       "bondage neg_reaction" : "She cries and squirms as you tie her up, feeling extremely uncomfortable.",

                       "oil description" : "being oiled-up.",
                       "oil action" : "Oil her up",
                       "oil intro" : "You give %s a bottle of body oil, insisting that she spreads it all over her naked body.",
                       "oil pos_reaction" : "She oils up every nook and cranny of her body for your pleasure, playfully massaging her glistening skin while you watch.",
                       "oil neg_reaction" : "She isn't comfortable with slippery and oily stuff, complaining that it stinks and feels revolting.",

                       "wet description" : "being wet.",
                       "wet action" : "Get her wet",
                       "wet intro" : "You ask Sill to fetch you a bucket of cold water, which you pour straight on %s's body.",
                       "wet pos_reaction" : "She loves being wet and moist, moaning as she slips her hands all over her body.",
                       "wet neg_reaction" : "She looks upset and miserable like a wet kitty. She hates water.",

                       "submission description" : "taking a humiliating pose.",
                       "submission action" : "Humiliate her",
                       "submission intro" : "You tell %s to get on her knees and beg for what's going to happen.",
                       "submission pos_reaction" : "She eagerly obeys your order, taking perverse pleasure in begging for you to abuse her.",
                       "submission neg_reaction" : "She refuses to beg and complains that it is beneath her.",

                       "femdom description" : "dominating her partner.",
                       "femdom action" : "Let her dominate",
                       "femdom intro" : "You tell %s to take the lead and dominate this encounter.",
                       "femdom pos_reaction" : "She is pleased to be given the leading role. She perversely enjoys giving orders and dominating her partner.",
                       "femdom neg_reaction" : "She hesitates, then awkwardly tries to give an order in an unconvincing voice. She almost immediately reverses herself and apologises. She doesn't enjoy taking the lead at all.",

                       "gags description" : "being gagged while having sex.",
                       "gags action" : "Gag her",
                       "gags intro" : "You order %s to wear a large ball gag, which leaves her mouth open at all times and makes it hard to talk.",
                       "gags pos_reaction" : "She seems oddly happy and excited as she puts on the gag and gives you a sheepish look.",
                       "gags neg_reaction" : "Unable to control her drooling and hardly able to talk, she gives you a furious look. She seems to hate it.",

                       "strap-ons description" : "fucking girls with a strap-on.",
                       "strap-ons action" : "Use a strap-on",
                       "strap-ons intro" : "You tell %s to fuck Sill using a strap-on dildo.",
                       "strap-ons pos_reaction" : "She looks triumphant as she puts on a huge black strap-on dildo, with one end up in her pussy and the other dangling in front of her. Sill gasps.",
                       "strap-ons neg_reaction" : "She grumbles as she puts it on, complaining that she isn't a man.",

                       "roleplay description" : "playing a role while fucking.",
                       "roleplay action" : "Make her play a role",
                       "roleplay intro" : "You tell %s that you are going to play roles: you are the city guard and she is a captured thief.",
                       "roleplay pos_reaction" : "She enjoys the idea of role-playing and makes a great show of being a repentant horny thief.",
                       "roleplay neg_reaction" : "She thinks it's stupid and distracting and doesn't get into it at all.",

                       "plugs description" : "wearing a plug inside her ass.",
                       "plugs action" : "Use anal plug",
                       "plugs intro" : "Taking out a large, glistening rubber plug, you tell %s to insert it in her ass.",
                       "plugs pos_reaction" : "She pushes the plug deep inside her ready asshole with delight, moaning seductively.",
                       "plugs neg_reaction" : "She inserts the plug with great difficulty, ashamed and in pain. It makes her very uncomfortable.",

                       "enemas description" : "getting an enema.",
                       "enemas action" : "Use an enema",
                       "enemas intro" : "You tell %s it's time to clean up.",
                       "enemas pos_reaction" : "As you insert the enema into her asshole and start filling her up with water, she begs you to go further and further. Soon, her belly is inflated and rounded like a balloon.",
                       "enemas neg_reaction" : "She cries with shame and horror as you fill her insides with cleansing water. She begs you to stop.",

                       "beads description" : "wearing anal beads.",
                       "beads action" : "Use anal beads",
                       "beads intro" : "You give %s a bead necklace and explain what she should do with it.",
                       "beads pos_reaction" : "She pushes the beads into her asshole one by one, clearly enjoying it and moaning as you watch.",
                       "beads neg_reaction" : "She cringes and whines as she painfully pushes one or two beads inside her ass. She tells you she hates it.",

                       "masturbation description" : "masturbating.",
                       "masturbation action" : "Make her masturbate",
                       "masturbation intro" : "You tell %s to play with herself while doing it.",
                       "masturbation pos_reaction" : "She enthusiastically starts playing with her clit and fingering her pussy while you watch her.",
                       "masturbation neg_reaction" : "She pretends to masturbate but isn't doing anything. She doesn't enjoy it at all.",

                       "fingering description" : "being fingered.",
                       "fingering action" : "Slide a finger inside her",
                       "fingering intro" : "You tell %s you will put your fingers inside her.",
                       "fingering pos_reaction" : "Her pussy welcomes you as you slide, one, then two, then three fingers inside her with ease. She moans with pleasure as you increase your pace, covering your fingers with her love juices.",
                       "fingering neg_reaction" : "Her pussy contracts and resists you as you push a single finger inside with great difficulty. Tears run down her face: she isn't enjoying this at all.",

                       "handjobs description" : "giving handjobs.",
                       "handjobs action" : "Give a handjob",
                       "handjobs intro" : "You order %s to give you a good handjob.",
                       "handjobs pos_reaction" : "She loves rubbing her hands up and down your dick, watching your throbbing, hard cock with fascination.",
                       "handjobs neg_reaction" : "She is mechanical and unenthusiastic. She doesn't like handjobs.",

                       "cunnilingus description" : "cunnilingus.",
                       "cunnilingus action" : "Cunnilingus",
                       "cunnilingus intro" : "You go down between %s's legs and spread her pussy lips.",
                       "cunnilingus pos_reaction" : "She moans wildly as you move your tongue deep inside her. Her love juices splash out, betraying her pleasure.",
                       "cunnilingus neg_reaction" : "She frowns and tries to close her legs, not feeling it. It seems like cunnilingus is not her thing.",

                       "oral description" : "giving oral.",
                       "oral action" : "Oral sex",
                       "oral intro" : "You tell %s to use her tongue and mouth to increase the pleasure.",
                       "oral pos_reaction" : "She loves licking and sucking her partner, and she makes sure to make eye contact with you as she does it.",
                       "oral neg_reaction" : "She gags at the taste and looks annoyed. She doesn't like giving oral.",

                       "irrumatio description" : "irrumatio.",
                       "irrumatio action" : "Irrumatio",
                       "irrumatio intro" : "Ordering %s to lay flat with her head hanging from the bed, you decide to fuck her mouth hard.",
                       "irrumatio pos_reaction" : "You shove your dick as deep and hard as you can into her mouth-pussy, and she takes it all in, seemingly enjoying having her throat raped.",
                       "irrumatio neg_reaction" : "She gags and coughs and cries and squirms, hating it, but you force-fuck her throat anyway.",

                       "deep throat description" : "deep throat.",
                       "deep throat action" : "Deep-throat",
                       "deep throat intro" : "You tell %s to get ready to deep-throat you.",
                       "deep throat pos_reaction" : "She has no gag reflexes and enjoys sucking your dick as far down her throat as she can.",
                       "deep throat neg_reaction" : "She gags and almost throws up, begging you to stop. You ignore her.",

                       "titjobs description" : "giving titjobs.",
                       "titjobs action" : "Give a titjob",
                       "titjobs intro" : "You order %s to use her tits to pleasure you.",
                       "titjobs pos_reaction" : "She wraps your dick completely between her gorgeous tits, licking the tip as she slides her soft mounds up and down your cock.",
                       "titjobs neg_reaction" : "She awkwardly tries to use her tits to rub your dick, but she is clumsy and uninterested.",

                       "footjobs description" : "giving footjobs.",
                       "footjobs action" : "Give a foot job",
                       "footjobs intro" : "You order %s to use her legs and feet to rub your dick.",
                       "footjobs pos_reaction" : "She loves playing with your dick with her feet, giving you a good upskirt view as she brings you to your limit.",
                       "footjobs neg_reaction" : "She hates it, only managing to crush your cock with her clumsy feet. You tell her to stop.",

                       "double penetration description" : "being fucked in both holes.",
                       "double penetration action" : "Double penetration",
                       "double penetration intro" : "You ask one of your security guys to join you and %s, telling him to fuck her ass as you take the front.",
                       "double penetration pos_reaction" : "She screams wildly as she gets both her front and back holes raped by fat dicks. She loves it.",
                       "double penetration neg_reaction" : "She is upset and bothered that two dicks are in her at the same time. It seems to be too much for her.",

                       "fisting description" : "being fisted.",
                       "fisting action" : "Fist her",
                       "fisting intro" : "Telling %s not to move, you decide to play around with her pussy using your bare fist.",
                       "fisting pos_reaction" : "She squeals with pleasure as you rape her wet pussy with your fist, eventually sending her into a massive squirting orgasm.",
                       "fisting neg_reaction" : "She screams with pain and begs you to stop as your fist bends her pussy in unnatural ways. She hates it.",

                       "insults description" : "being insulted.",
                       "insults action" : "Insult her",
                       "insults intro" : "You call %s names as you force her to perform, using language that would make a harbor whore blush.",
                       "insults pos_reaction" : "She seems to love being trashed and insulted, and after only a minute, you notice that she has got completely wet.",
                       "insults neg_reaction" : "She is shocked and unnerved by your words, unable to concentrate on what she's doing. It isn't helping.",

                       "69 description" : "69.",
                       "69 action" : "Do a 69",
                       "69 intro" : "You tell %s to get into a 69 position.",
                       "69 pos_reaction" : "She loves 69 and enjoys herself tremendously as she tends to her partner while her pussy gets licks.",
                       "69 neg_reaction" : "She looks unhappy as she seems to despise that position. In the end, it isn't enjoyable for anyone.",

                       "watersports description" : "watersports.",
                       "watersports action" : "Play watersports",
                       "watersports intro" : "You tell %s to get ready for some 'watersports'.",
                       "watersports pos_reaction" : "She loves peeing in front of people and being peed on. She doesn't find it shameful.",
                       "watersports neg_reaction" : "She is disgusted by bodily fluids and recoils with horror at the thought.",

                       "ass-to-mouth description" : "ass-to-mouth.",
                       "ass-to-mouth action" : "Go ass-to-mouth",
                       "ass-to-mouth intro" : "You decide to fuck %s in the ass before moving to her mouth.",
                       "ass-to-mouth pos_reaction" : "She accepts your dick readily and licks it clean for you, not caring that it was in her ass a second ago.",
                       "ass-to-mouth neg_reaction" : "She retches as you push your dick into her mouth, complaining that it is dirty and disgusting.",

                       "kissing description" : "kissing.",
                       "kissing action" : "Kiss her",
                       "kissing intro" : "You start kissing %s.",
                       "kissing pos_reaction" : "She responds enthusiastically to your kiss, mingling her tongue with yours. She doesn't let go until the very end.",
                       "kissing neg_reaction" : "She tries to avoid you and doesn't seem to enjoy kissing at all. She is relieved when you stop.",

                       "spanking description" : "spanking.",
                       "spanking action" : "Spank her",
                       "spanking intro" : "You tell %s that she's been a bad girl, and that she is going to get spanked hard.",
                       "spanking pos_reaction" : "She screams with pain and pleasure, crying tears of happiness as you give her a thorough spanking while fucking her.",
                       "spanking neg_reaction" : "You spank her and fuck her at the same time. She wriggles and tries to escape you, moaning in pain. She doesn't like it.",

                       "rimming description" : "rimming.",
                       "rimming action" : "Rimming",
                       "rimming intro" : "You tell %s to lick your asshole thoroughly.",
                       "rimming pos_reaction" : "She is very serious about licking you clean, pushing her tongue into your ass as she gives you a frantic handjob.",
                       "rimming neg_reaction" : "She is disgusted by the act and only timidly licks around your asshole. It tickles, but doesn't feel good in any way.",

                       "fondling her boobs description" : "being fondled.",
                       "fondling her boobs action" : "Fondle her boobs",
                       "fondling her boobs intro" : "You fondle her tits and play with her nipples as %s performs for you.",
                       "fondling her boobs pos_reaction" : "She loves it when you squeeze her tits and moans sexily as you rub her erect nipples.",
                       "fondling her boobs neg_reaction" : "She doesn't like to be touched there and tenses up, making the training less enjoyable.",

                       "groping her ass description" : "being groped.",
                       "groping her ass action" : "Grope her ass",
                       "groping her ass intro" : "You grope her ass and start fingering her asshole as %s performs for you.",
                       "groping her ass pos_reaction" : "She loves to be touched and groped and moans hornily as you shove two fingers up her butthole.",
                       "groping her ass neg_reaction" : "She doesn't like to be touched there and tenses up, making the training less enjoyable.",

                       "lactation description" : "lactation.",
                       "lactation action" : "Milk her",
                       "lactation intro" : "Groping %s's boobs, you take out a syringe filled with a strange liquid and plunge it into her nipple.",
                       "lactation pos_reaction" : "She gasps with astonishment as her tits grow larger in size. Soon, she begins to lactate uncontrollably, moaning as you milk her large breasts for all they're worth.",
                       "lactation neg_reaction" : "She yells and cries with pain as her boobs grow heavier and larger. The experience is too traumatic, however, and she fails to give you any milk.",

                       "doggy style description" : "doggy style.",
                       "doggy style action" : "Doggy style",
                       "doggy style intro" : "Pushing her on all fours, you start fucking %s from behind.",
                       "doggy style pos_reaction" : "She moans with pleasure as the length of your shaft run along her most sensitive parts. She cannot get enough of it.",
                       "doggy style neg_reaction" : "She grinds her teeth as she waits for you to be finished. She doesn't enjoy that position at all.",

                       "cowgirl description" : "cowgirl style.",
                       "cowgirl action" : "Cowgirl style",
                       "cowgirl intro" : "You make %s ride your dick.",
                       "cowgirl pos_reaction" : "She likes to be on top and lovingly bounces on your dick until you both get close to your limit.",
                       "cowgirl neg_reaction" : "She doesn't like to be on top and stays passive as you fuck her from below.",

                       "piledriver description" : "piledriver.",
                       "piledriver action" : "Piledriver",
                       "piledriver intro" : "Pushing %s on her back and lifting her legs in the air, you plunge your hard dick inside her.",
                       "piledriver pos_reaction" : "She is overwhelmed with lust and pleasure as the blood flows to her head while you pound her mercilessly.",
                       "piledriver neg_reaction" : "She is confused and bothered by this new position, telling you she doesn't like it at all.",

                       "spooning description" : "spooning.",
                       "spooning action" : "Spooning",
                       "spooning intro" : "Hugging %s from behind, you slowly slide into her while caressing her body.",
                       "spooning pos_reaction" : "She loves being cradled and fucked at the same time. She relaxes completely, moaning softly, soon ready to reach orgasm.",
                       "spooning neg_reaction" : "She stays passive as you fuck her from behind, looking bored.",

                       "bukkake description" : "bukkake.",
                       "bukkake action" : "Bukkake",
                       "bukkake intro" : "Calling a group of your security guards, you let them watch as you and Sill fuck %s. They start jerking off while watching her. As you reach your limit, you pull out and cum all over her face, quickly followed by the other men.",
                       "bukkake pos_reaction" : "She shakes with a massive orgasm as she experiences a shower of cum on her face, hair and body. She gorges up on leftover cum from everyone's dick.",
                       "bukkake neg_reaction" : "She tries to get away and whines as everyone cums on her face and hair. She bitterly complains about the smell and taste.",

                       "cum in mouth description" : "cum in her mouth.",
                       "cum in mouth action" : "Cum in her mouth",
                       "cum in mouth intro" : "You decide to use %s's mouth for a big finish.",
                       "cum in mouth pos_reaction" : "She looks entranced as you unload a wad of semen into her ready mouth. She plays with it on her tongue, enjoying the taste and texture.",
                       "cum in mouth neg_reaction" : "You cum a lot in her mouth, sending her into a fit of coughing. She spits it all out, complaining.",

                       "cum on face description" : "cumshots.",
                       "cum on face action" : "Cum on her face",
                       "cum on face intro" : "Popping your dick out, you shoot a load of semen all over %s's face.",
                       "cum on face pos_reaction" : "She sighs happily as she receives load after load of your cum. She uses her hands to spread the cum all over her face, then licks her fingers.",
                       "cum on face neg_reaction" : "She recoils with disgust as you shoot your load. She rushes to get a wet cloth and clean it up.",

                       "cum in hair description" : "cum in her hair.",
                       "cum in hair action" : "Cum in her hair",
                       "cum in hair intro" : "Popping your dick out, you decide to cum all over %s's soft, silky hair.",
                       "cum in hair pos_reaction" : "She moans as you wrap her hair around your dick and squeeze every last drop on her scalp. She enjoys being treated like a dirty cum dump.",
                       "cum in hair neg_reaction" : "She yells awfully as you shoot a load of semen on her hair, whining that it's gonna take ages to get it off.",

                       "cum on body description" : "cum on her body.",
                       "cum on body action" : "Cum on her body",
                       "cum on body intro" : "You decide to cum all over %s's body.",
                       "cum on body pos_reaction" : "She reaches her climax as you take out your dick and spill a load of white cum all over her soft skin.",
                       "cum on body neg_reaction" : "She squirms as you shoot cum all over her body, complaining that it is sticky and smelly.",

                       "cum shower description" : "getting showered with cum.",
                       "cum shower action" : "Shower her with cum",
                       "cum shower intro" : "Popping a special pill from the spice market, your dick starts bulging, ready to burst with huge amounts of cum. You tell %s to lay down and get ready to receive your seed.",
                       "cum shower pos_reaction" : "You cum and cum buckets, until she is covered with white, sticky semen. She is enthralled by the sensation.",
                       "cum shower neg_reaction" : "She squeals and cowers in fear as you cum buckets all over her body, disgusted by the smell and feel.",

                       "swallowing description" : "swallowing cum.",
                       "swallowing action" : "Make her swallow",
                       "swallowing intro" : "Shoving your dick deep into %s's mouth for the big finish, you shoot loads of cum deep down her throat.",
                       "swallowing pos_reaction" : "She gulps it all down with gusto, squeezing every last drop of cum out of your throbbing dick. She licks her lips sexily when you are finished.",
                       "swallowing neg_reaction" : "She gets tearful and gags, trying to spit it all out as you shoot load after load. She only partly succeeds, and looks unhappy at having to drink cum.",

                       "creampie description" : "receiving a creampie.",
                       "creampie action" : "Creampie",
                       "creampie intro" : "Taking your dick slowly out of %s, you shoot a thick load of white cum all over her ass and pussy.",
                       "creampie pos_reaction" : "She shakes with a massive orgasm as you spurt cum all over her holes. She seems to love it.",
                       "creampie neg_reaction" : "She covers her face and begs you to stop, saying that it's creepy and disgusting.",

                       "cum inside description" : "cum inside her.",
                       "cum inside action" : "Cum inside",
                       "cum inside intro" : "Not caring about the consequences, you decide to cum deep inside %s.",
                       "cum inside pos_reaction" : "She reaches a blinding orgasm, moaning wildly as you unload a wad of cum deep inside her.",
                       "cum inside neg_reaction" : "She screams for you to get out, but you ignore her, smearing her insides with thick, sticky cum. She cries with shame and disgust.",

                       "multiple orgasms description" : "having multiple orgasms.",
                       "multiple orgasms action" : "Give her multiple orgasms",
                       "multiple orgasms intro" : "Rubbing her clit with one hand, you keep the pace up until %s cannot but shake with a shattering orgasm. Giving her no moment to rest, you increase the build-up until she comes another time, and another time.",
                       "multiple orgasms pos_reaction" : "She loves it and loses her mind completely over the sensations washing over her, looking nothing but an obedient, adoring slave by the time you are finished.",
                       "multiple orgasms neg_reaction" : "She feels overtly sensitive and begs you to stop, almost in pain from excessive climaxing. She doesn't like it.",

                       "denied orgasm description" : "being denied orgasm.",
                       "denied orgasm action" : "Deny her orgasm",
                       "denied orgasm intro" : "You decide to tease %s to the limit, not letting her reach climax.",
                       "denied orgasm pos_reaction" : "She seems to love being teased and indefinitely denied orgasm, becoming incredibly horny and sensitive over time.",
                       "denied orgasm neg_reaction" : "She screams with frustration and begs you to let her climax. She is upset that you won't let her.",

                       "squirting description" : "squirting.",
                       "squirting action" : "Make her squirt",
                       "squirting intro" : "Pushing your hand inside %s's pussy, you start rubbing the walls of her pussy, looking for her sensitive G-spot. She looks overwhelmed by the sensation.",
                       "squirting pos_reaction" : "She squirts hard, showering the room with her juice. She climaxes so hard that she can’t even move afterwards.",
                       "squirting neg_reaction" : "She feels weird and gross, and begs you to take your hand out. She isn't into it at all.",

                       "stripping description" : "stripping.",
                       "stripping action" : "Make her strip",
                       "stripping intro" : "Telling %s to remove her clothes slowly and sexily, you look on as she does what she's told.",
                       "stripping pos_reaction" : "She moans as she feels the caress of her clothing rubbing against her soft skin. Looking straight into your eyes, she slowly removes her underwear last, inch by inch, making sure to give you a good show.",
                       "stripping neg_reaction" : "Whining and bitching, she reluctantly takes off her clothes, hiding her private parts in embarrassment. She looks angry and shameful.",

                       }

    fix_dict = {
                "stripping" : Fixation("stripping", acts=("naked", "sex", "bisexual"), step=1, attribute="modest", tag_list=(["strip"], ["naked", "dancer"])),
                "public acts" : Fixation("public acts", acts=("naked", "service", "sex", "group"), step=1, attribute="extravert", tag_list=(["public"]), not_list=["rest"]), # Location tags are allowed but display special flavor text
                "cosplay" : Fixation("cosplay", acts=("naked", "fetish", "bisexual"), step=1, attribute="extravert", tag_list=(["cosplay"], ["maid", "kimono"], ["swim", "waitress", "dancer"]), not_list=["naked"], cannot_have_neg=["roleplay"]),
                "dildos" : Fixation("dildos", acts=("sex", "anal", "bisexual"), step=1, attribute="introvert", tag_list=(["dildo"], ["toy"],)),
                "vibrators" : Fixation("vibrators", acts=("naked", "fetish", "bisexual"), step=1, attribute="introvert", tag_list=(["vibrator"], ["toy"],)),
                "dirty sex" : Fixation("dirty sex", acts=("sex", "fetish", "group"), step=1, attribute="sub", tag_list=(["dirty"],)),
                "penis worship" : Fixation("penis worship", acts=("service", "group"), step=1, attribute="sub", tag_list=(["handjob", "big"], ["service", "big"], ["handjob"],), cannot_have_neg=["handjob"]),
                "bondage" : Fixation("bondage", acts=("fetish", "naked"), step=1, attribute="sub", tag_list=(["bondage"],)),
                "oil" : Fixation("oil", acts=("group", "anal"), step=1, attribute="extravert", tag_list=(["wet"],)),
                "wet" : Fixation("wet", acts=("naked", "sex", "bisexual"), step=1, attribute="extravert", tag_list=(["wet"],)),
                "submission" : Fixation("submission", acts=("service", "fetish", "bisexual"), step=1, attribute="sub", tag_list=(["sub"],)),
                "femdom" : Fixation("femdom", acts=("bisexual", "sex", "service"), step=1, attribute="dom", tag_list=(["dom"],)),
                "gags" : Fixation("gags", acts=("fetish", "naked"), step=1, attribute="introvert", tag_list=(["gag"], ["bondage"],)),
                "strap-ons" : Fixation("strap-ons", acts=("bisexual", "group"), step=1, attribute="dom", tag_list=(["strap-on"], ["lesbian"], ["toy"],)),
                "roleplay" : Fixation("roleplay", acts=("naked", "sex", "fetish"), step=1, attribute="extravert", tag_list=(["cosplay"], ["maid", "kimono"], ["swim", "waitress", "dancer"]), cannot_have_neg=["cosplay"]),
                "plugs" : Fixation("plugs", acts=("naked", "anal"), step=1, attribute="modest", tag_list=(["plug"], ["toy"],)),
                "enemas" : Fixation("enemas", acts=("group", "anal"), step=1, attribute="materialist", tag_list=(["enema"], ["toy"],)),
                "beads" : Fixation("beads", acts=("anal"), step=1, attribute="introvert", tag_list=(["beads"], ["toy"],)),

                "masturbation" : Fixation("masturbation", acts=("service", "naked", "sex"), step=2, attribute="extravert", tag_list=(["mast"], ["naked"],)),
                "fingering" : Fixation("fingering", acts=("naked", "fetish", "bisexual", "group"), step=2, attribute="lewd", tag_list=(["finger"],)),
                "handjobs" : Fixation("handjobs", acts=("service", "group"), step=2, attribute="modest", tag_list=(["handjob"],)),
                "cunnilingus" : Fixation("cunnilingus", acts=("service", "bisexual"), step=2, attribute="introvert", tag_list=(["cunnilingus"],["finger"])),
                "oral" : Fixation("oral", acts=("service", "bisexual", "group"), step=2, tag_list=(["oral"],)),
                "irrumatio" : Fixation("irrumatio", acts=("fetish"), step=2, attribute="sub", tag_list=(["deep"], ["oral"],)),
                "deep throat" : Fixation("deep throat", acts=("service", "group"), step=2, attribute="sub", tag_list=(["deep"], ["oral"],), cannot_have_neg=["oral"]),
                "titjobs" : Fixation("titjobs", acts=("service", "group"), step=2, attribute="extravert", tag_list=(["titjob"],)),
                "footjobs" : Fixation("footjobs", acts=("service", "fetish"), step=2, attribute="dom", tag_list=(["footjob"],)),
                "double penetration" : Fixation("double penetration", acts=("group"), step=2, attribute="lewd", tag_list=(["double"],)),
                "fisting" : Fixation("fisting", acts=("fetish", "bisexual", "anal"), step=2, attribute="lewd", tag_list=(["fist"], ["finger"])),
                "insults" : Fixation("insults", acts=("fetish", "naked"), step=2, attribute="sub", tag_list=(["sub"],)),
                "69" : Fixation("69", acts=("service", "bisexual"), step=2, attribute="dom", tag_list=(["69"], ["oral"],), cannot_have_neg=["oral"]),
                "watersports" : Fixation("watersports", acts=("fetish", "sex"), step=2, attribute="sub", tag_list=(["watersports"], ["squirt"],)),
                "ass-to-mouth" : Fixation("ass-to-mouth", acts=("anal", "group"), step=2, attribute="sub", tag_list=(["cim"], ["oral"],), cannot_have_neg=["oral"]),
                "kissing" : Fixation("kissing", acts=("naked", "sex", "bisexual"), step=2, attribute="idealist", tag_list=(["kiss"],)),
                "spanking" : Fixation("spanking", acts=("fetish", "anal"), step=2, attribute="sub", tag_list=(["spank"], ["sub"],)),
                "rimming" : Fixation("rimming", acts=("service", "fetish"), step=2, attribute="sub", tag_list=(["rim"],)),
                "fondling her boobs" : Fixation("fondling her boobs", short_name = "fondling", acts=("naked", "sex", "bisexual", "group"), step=2, tag_list=(["fondle"],)),
                "groping her ass" : Fixation("groping her ass", short_name = "groping", acts=("naked", "anal", "bisexual", "group"), step=2, tag_list=(["grope"],)),
                "lactation" : Fixation("lactation", acts=("naked", "fetish"), step=2, attribute="extravert", tag_list=(["lactation"], ["titjob"],)),
                "doggy style" : Fixation("doggy style", acts=("sex", "anal"), step=2, attribute="lewd", tag_list=(["doggy"],)),
                "cowgirl" : Fixation("cowgirl", acts=("sex", "anal"), step=2, attribute="dom", tag_list=(["cowgirl"],)),
                "piledriver" : Fixation("piledriver", acts=("sex", "anal"), step=2, attribute="materialist", tag_list=(["piledriver"],)),
                "spooning" : Fixation("spooning", acts=("sex", "anal"), step=2, attribute="idealist", tag_list=(["spoon"],)),

                "bukkake" : Fixation("bukkake", acts=("bisexual", "group"), step=3, attribute="lewd", tag_list=(["buk"], ["cof"], ["cumshot"],), cannot_have_neg=["cum shower"]),
                "cum in mouth" : Fixation("cum in mouth", acts=("service", "anal", "bisexual"), step=3, attribute="lewd", tag_list=(["cim"], ["oral"],), cannot_have_neg=["oral"]),
                "cum on face" : Fixation("cum on face", acts=("service", "sex", "fetish"), step=3, attribute="sub", tag_list=(["cof"], ["buk"], ["cumshot"],)),
                "cum in hair" : Fixation("cum in hair", acts=("service", "fetish"), step=3, attribute="sub", tag_list=(["cih", "coh"], ["cof", "buk"], ["cumshot"],)),
                "cum on body" : Fixation("cum on body", acts=("sex", "anal", "service"), step=3, attribute="dom", tag_list=(["cob"], ["cumshot"],)),
                "cum shower" : Fixation("cum shower", acts=("bisexual", "group"), step=3, attribute="sub", tag_list=(["cum shower"], ["cob", "cih"], ["cumshot"],), cannot_have_neg=["bukkake"]),
                "swallowing" : Fixation("swallowing", acts=("service", "fetish"), step=3, attribute="materialist", tag_list=(["cim"], ["deep"], ["oral"],), cannot_have_neg=["oral", "cum in mouth"]),
                "creampie" : Fixation("creampie", acts=("sex", "anal", "group"), step=3, attribute="extravert", tag_list=(["creampie"], ["cin"],)),
                "cum inside" : Fixation("cum inside", acts=("sex", "anal"), step=3, attribute="introvert", tag_list=(["cin"], ["creampie"],)),
                "multiple orgasms" : Fixation("multiple orgasms", acts=("group", "bisexual"), step=3, attribute="lewd", tag_list=(["orgasm"],)),
                "denied orgasm" : Fixation("denied orgasm", acts=("anal", "fetish", "bisexual"), step=3, attribute="sub", tag_list=(["denied"],)),
                "squirting" : Fixation("squirting", acts=("service", "sex", "bisexual"), step=3, attribute="extravert", tag_list=(["squirt"], ["watersport", "orgasm"],)),
                }


    ## PERKS AND ARCHETYPES ##
init -4 python:
    archetype_list = ["The Maid", "The Player", "The Model", "The Courtesan", "The Escort", "The Fox", "The Slut", "The Bride"]

    archetype_description = {
                            "The Maid" : "Holding her head up high even in adversity, the {b}Maid{/b} succeeds through hard work and commitment. She is the patron saint of servants and menial workers.",
                            "The Player" : "Always ready to tell a compelling story or improvise a lavish dance, the {b}Player{/b} is admired for her party skills and charisma. She is the patron saint of singers, actors and other artists, accomplished or aspiring.",
                            "The Model" : "Blessed with perfect natural beauty and elegance, if a little vain, the {b}Model{/b} fascinates men and women alike. She is the patron saint of the young, the pretty, and the well endowed.",
                            "The Courtesan" : "The {b}Courtesan{/b} is a master of etiquette, seduction and politics, able to make anyone give in to her every whim. She is the patron saint of noble women, politicians, and other schemers.",

                            "The Escort" : "Using her body and skills to great advantage, the {b}Escort{/b} is an expert at leveraging her talents for profits. She is the patron saint of fancy prostitutes, merchants, and mercenaries.",
                            "The Fox" : "A mysterious figure which seems to always show on auspicious occasions, the {b}Fox{/b} is said to bring great luck to everyone she shares her bed with. She is the patron saint of travellers and hermits.",
                            "The Slut" : "A much revered figure, the {b}Slut{/b} delights in experienceing sex and pleasure in all its forms, rejecting laws and morals that do not suit her. She is the patron saint of street girls, thieves, libertines, and the occasional Arios priest.",
                            "The Bride" : "A harbinger of peace and prosperity, the {b}Bride{/b} is gentle and devoted. She is the patron saint of coming-of-age virgins, pregnant and married women, and widows."
                            }

    ## GOSSIP ##

    generic_gossip = [
                        "I don't understand how the magicians can carry on their experiments in broad daylight. The church of Arios zealots hate magic-users with a passion. But they haven't moved to shut them down...",
                        "Taxes on rice, grain, vegetables, meat... Soon they'll tax water from the puddles! What's a man to eat?",
                        "Zan has been consumed by lust, greed and corruption for as long as I can remember, but seems these days we've reached new lows.",
                        "Not everyone in the Guard is a flat-out jerk. I know a guy who's all right. They are few and far between, though.",
                        "The royals sit all high and mighty far away from us people. They let the guards rob us blind but when a thief shows up, she never gets caught. Where's the justice in that?",
                        "You'd think the thieves would leave poor folks like us alone. But no sir, if you have nothing, they'll still pry it from your cold dead hands.",
                        "The guards steal so much from us poor folks that there's hardly anything left for the thieves.",
                        "*lowering her tone* Heard of Shalia, the dark goddess? They say she's got a temple in the slums, in this very city. It gives me the creeps.",
                        "There's a temple to Shalia somewhere in the city. I expect it's hard to find, though, her supporters rarely come out in the open.",
                        "Arios damn that Shalia bitch and her secret temple! A vile goddess like her has no place in this city. We're upstanding folks of the Light, are we not?",
                        "I heard Shalia is not at all what she's cracked up to be. You hear of sacrifices, virgin blood... That's nonsense. Her followers like secrecy, but they're into much more mundane things, such as lifting your purse.",
                        "Shalia followers eat little children's hearts for breakfast. That's what my Ma' said.",
                        "With all the crooked politicians and scheming thieves crawling in this city, you'd wonder why they didn't build a Cathedra to Shalia instead!",
                        "When he was little, my brother was always lonely, brooding, plotting revenge on the kids who bullied him. We used to joke that he was our own little Shalia apostle!",
                        "Shalia is a craven goddess, that's what she is. A proper god has his followers out in the open.",
                        "Some say Shalia's beauty itself is a weapon she uses in her schemes...",
                        "People are dumb enough to believe Arios is better because he is the god of light. But who wants light to be shone on all their thoughts and secrets? Shalia has just as important a role...",
                        "Someone told me he's seen a Shalia shrine in the slums. But he wouldn't tell me where it is.",
                        "Zan is full of dirty secrets and dark corners. One must watch their step - it's easy to anger the wrong person, and hard to gain anyone's trust.",
                        "There are three ways to make people in Zan part with their money: pussy, spice, or a sharp knife.",
                        "I've seen an incredible fight at the arena! Cyntia's a slave, but she's got style.",
                        "I can't believe people enjoy watching fights to the death in the arena. If you needed further proof this place is barbaric, there, you have it.",
                        "I don't care about the deaths in the arena. Most of the time it's just monsters and slaves. All in good fun!",
                        "People bet heavily on the arena fights. There's some good money to be had, if you know who to support.",
                        "Lots of adventurers try their luck in the arena. Many end up cripples or worse after just a few fights. But Cyntia's endured.",
                        "I don't watch the fights, too gory. I just bet on them. But lately, I've been out of luck.",
                        "Someone told me he had a trick so that he'd always win his bets in the arena. I didn't believe him at first, but he won five fights in a row!",
                        "The gladiators of the arena in their shining gold armor, covering themselves with glory and blood! Isn't that a tremendous sight?",
                        "The league of adventurers draws champions and scum alike from faraway lands. I wouldn't trust any of them, that's for sure.",
                        "If you want a quick way to make money, you could do worse than throw your lot with the league of adventurers. They always have some juicy bounties for enterprising individuals, and not all of them require drawing your sword.",
                        "The league of adventurers prefers to advance their goals by maneuvering rather than violence, but they've been known to use both.",
                        "There is no head of the league of adventurers. The intendant only deals with the paperwork, but all members are considered equals.",
                        "How can the league of adventurers be leader-less? There must be someone pulling their strings from the shadows.",
                        "I'm offended that some of those upstarts at the league of adventurers are getting so rich, when so many of our own true blue-blooded nobles are facing ruin.",
                        "The league of explorers is shunned by many of the nobles and courtiers because it takes commoners in, but they have started some of the most profitable enterprises in the city.",
                        "Ever heard of the brotherhood? They say they'll defend the common people against the nobles and high-borns. Such nonsense.",
                        "I've heard of a secret political organization called the Brotherhood. I have no idea who they are or what they do, but they're rumored to have enormous power in the city.",
                        "Some crazy jerk got my friend all worked up about 'sticking it to the royals', and 'taking back what's rightfully ours'. I begged my friend not to listen to such drivel, but now she's been arrested by the king's guard, and they suspect me as well...",
                        "Brother, you should not toil and suffer so that a few high-born loafers can hold banquets and orgies all day and all night. If you joined the brotherhood, you could put an end to this... But hush, someone's coming.",
                        "This woman claimed the brotherhood will rise to help the little people. But I know the truth of it: within a few months, they'd put themselves and their relatives in all the powerful positions, and they'd be no better than King Pharo.",
                        "King Pharo is our rightful leader chosen by the gods themselves. It is heresy to question the place of our betters: let us talk no more of that so-called 'brotherhood'.",
                        "Magicians are vermin who deserve nothing but ruin. They spoil our beloved city with their godless experiments. I wish the King had enough sense to make them all hang.",
                        "What's wrong with a little magic? It's not perversion, or a scam. People are afraid of things they don't understand, that's all. I dabble in magic myself, did you know? Here's an ointment you could buy for cheap...",
                        "Magicians have long been established in Zan without too much trouble. But their conflict with the church of Arios is starting to pull at the seams.",
                        "A priest of Arios himself told me that wizards consort with demons and plot Zan's ruin. Something must be done.",
                        "Those magicians are just rich, spoiled brats toying with forces they don't understand. I don't like those bigots from the Cathedra, but they have a point.",
                        "Heresy of not, the mages are contributing good money to our city's finances. If every questionable practice was banned in this city, there wouldn't be much left of Zan.",
                        "Monsters have been spotted in Zan. I myself saw a three-headed wolf raping a young girl in a dark alley. What has this city come to?",
                        "Sorcerers are responsible for the monsters plague in this city, who else? They should throw the lot of them in a dark cell with their pets, and throw away the key.",
                        "I don't buy it. Wizards have enough trouble as it is with the Light priests. Why would they release monsters in the streets and make their situation worse?",
                        "Monsters roam the streets at night. No one should stay out late these days, especially young, beautiful girls.",
                        "An entire patrol wiped out near the Gardens? This monster problem is getting out of hand!",
                        "The Cathedra is a nice enough looking building from outside, but you wouldn't like what goes on inside, believe me.",
                        "The High Priestess has advocated for the complete removal of magic from the city. She'll have her way; she always does.",
                        "I remember the times before the war, when the Grandmaster was heading the Arios cult... These were gentler days, I tell you.",
                        "Ever since the Grandmaster left for the Holy war, the High Priestess has been consolidating her power in the city. I don't think she wants him to come back.",
                        "Heard any news from the war in the Holy lands? They told me it's not going well. The heretics are resisting us at every step, but surely Arios won't let his flock down.",
                        "The Arios priests want to impose their cult on the rest of the city, plain and simple. Don't be fooled by the bitch priestesses' righteous sermons.",
                        "A friend of mine became a nun of Arios, but she had a change of heart and ran away a week ago. I don't know what happened.",
                        "I can't stand those upright do-gooders from the Arios church. I'm sure they're hiding something.",
                        "They say a lot of Arios priestesses used to be hookers, before they converted. I don't know why. But it's kind of turning me on.",
                        "Arios is the god of Light and Strength. May His Light guide us towards good deeds, and His Strength support our arms when the time comes to strike down evil.",
                        "The true teachings of Arios are a thing of beauty. Don't listen to those priests, all they know how to do is spout nonsense. Find the Light of Arios within your heart.",
                        "They say demons roam the streets. I say it's nothing compared to what goes on at Court.",
                        "All the court nobles do is eat, drink, fuck, and plot against one another. I wish I had that kind of life.",
                        "This city is doomed. When the head is rotten, how can you save the body?",
                        "My sister is a maid at court. She had a glimpse of one of the ceremonies and wouldn't shut up about it. 'The dresses!', 'The lights!', 'The jewels!', 'The gold dishes!', and so on.",
                        "Every noble courtier has one or more courtesans in tow. That's how they call hookers there. Not that it stops them from visiting regular brothels, mind you.",
                        "The nobles of Zan are a curious breed. They suck their estates dry trying to make it at court and impress the King, but they all despise him and think him weak. They are the ones being played for fools.",
                        "At the beginning of his reign, 18 years ago, King Pharo was doing well enough. But his achievements have been unraveling one by one, and now the city has lost all direction.",
                        "I don't care what happened to the princess's mother, the King should have remarried. What if something happens to the princess?",
                        "No male heir spells disaster for any royal family. Why doesn't the King understand that?",
                        "Because King Pharo has no male heir, power will go to the princess's son, when and if she marries. I guess she would be regent in the interim.",
                        "Sure, King Pharo has a laissez-faire attitude to everything... But isn't that what makes Zan so great? Would you like to see a crackdown on whores, alcohol, spices, or even gambling?",
                        "The King is always brooding, his mood dark... He sure looks grim for someone whose courtiers throw so many parties.",
                        "The princess is a lovely thing, isn't she? All the knights and nobles are crazy in love with her.",
                        "Her delicate features and manners make the princess the sweetheart of all Zan, nobles and commoners alike.",
                        "The princess seems in a dark mood sometimes. Could such a blessed person have problems like all of us?",
                        "The King's knights are all sworn to protect him and his family. Their commander looks like Arios made flesh himself. He's a very zealous and devoted man.",
                        "I hear some big shot's been murdered a few days back in the castle. They are trying to keep the lid on it, but it seems like trouble is brewing.",
                        "Some ancient weapons hold tremendous power. I wonder how one can get a hold on one of those?",
                        "When people go to a whorehouse, they expect more than just a tryst... Good service is always appreciated.",
                        "So many young girls are turning into whoring slaves these days... Some even turn themselves in voluntarily. I guess it's one way to get food and shelter in these troubled times.",
                        "The girls are so glamorous there... I never knew being a slut was so rewarding. Makes me question my morals!",
                        "All travelers agree on one thing: the best thing about Zan is its sex slaves... Any kind of sexual fantasy can be fulfilled here. Many slaves take great pride in fulfilling their master's desires.",
                        "Girls in Zan are so easy. All it takes is showing up at the same place every day, chatting them up, and sooner or later they'll roll in the hay with you.",
                        "That merchant girl is so hot, man! I'd go there and buy stuff every day if I could convince her to fool around with me.",
                        "People who like unusual sex acts are less common, but they pay more money.",
                        "I came by this brothel the other day, and saw a pink-haired hottie... but was disappointed to find out she wasn't one of the working staff.",
                        "After a day's hard work, what's hotter than going to a club to be served by beautiful girls, then have one of them strip and go down on you? I understand the appeal.",
                        "Whores are like priestesses for the sex goddess, that's what my 'pa used to say. He was usually drunk as a skunk.",
                        "Some guy from Westmarch had trouble understanding what geishas are. He kept saying they're like regular hookers. I swear, it's impossible to educate these unrefined barbarians .",
                        "I went to this little establishment by the harbor, asking for a good massage. And I really got a good one, down there... Isn't it wonderful?",
                    ]

    chapter_gossip = {1 : [
                            "Have you seen the new Guard uniforms? They adorn their armor with fine silk, while the rest of us starve..., "
                            "I've heard some talk of a secret lair somewhere around the Slums... A haven for thieves and bandits. I shiver to think of it.",
                            "Captain Farah is one greedy bitch. Her men came yesterday to shake one of my friends down. Everyone hates her, but they say she's got protection in high places.",
                            "The head of the guards is Captain Farah. Best stay clear of them if you want my advice. Levies and taxes are all the guards care about. If you ask me, they just make them up as they go.",
                            "Some say the captain of the Guard is getting too greedy, even among her own men... There are some who say they'd do better. Maybe they mean they'd be better at not getting caught.",
                            "Thieves are getting bold these days. Or desperate. Doesn't look like the guards care to do anything about it, mind you.",
                            "My neighbor complained about the taxes, so they took him in, and no one's heard of him since. Better suck it up and stay alive, if you want my 2 denars.",
                            "The guards took everything from me, but what can I do? Only the King has higher authority, and he won't listen to a commoner.",
                            "Some say the thieves operate in an organized fashion, much like a guild. I don't buy this nonsense. Ever seen a thief with anything else than spice for brains?",
                            "People here like to blame a secret Shalia cabal for all their ills, but let me tell you: it's our good Arios-loving captain who's robbing us blind at the moment!",
                            "I keep hearing about this new brothel outside the city. I really have to check it out.",
                          ],
                      2 : [
                            "There has been a wave of murders in the city lately... And not just the usual rabble: they took out some pretty big shots.",
                            "People say the streets aren't safe at night, hired blades on the prowl... Many highborns won't go out anymore without an escort.",
                            "Somebody's been snuffing out the blue bloods one by one... It was about time someone started fighting for justice in this city!",
                            "A murderous killer is on the prowl... Some say he killed the high judge, and the royals could be next.",
                            "How dare someone threaten the life of our dear Princess? I hope they catch the motherfucker, and gouge his eyes out!",
                            "No one is safe in this city, not even the judges... Time to head for the country until things quiet down.",
                            "Don't worry about those killers. There are only after the bigwigs, no one is paying to assassinate small fry like you and me.",
                            "I've heard of a fearsome group of superhuman stealth warriors, on a quest for blood and revenge throughout the city... They call them {i}ninjas{/i}.",
                            "Ninjas? What a load of bull. They only exist in children's tales.",
                            "Ninjas are a secret society of bloodthristy assassins that has infiltrated Zan. Or so I hear.",
                            "Why would anyone threaten the Princess's life? She's the only one who doesn't wish us little people ill in this royal nest of vipers.",
                            "Noble families have paid a heavy toll in the latest wave of murders... Maybe this so-called revolution is coming after all?",
                            ],
                      3 : [],
                      4 : [],
                      5 : [],
                      6 : [],
                      7 : [
                          "Have you heard of [MC.name], the legendary Brothel Master? I bet he can turn your sister into a sex-crazed goddess.",
                          "[MC.name] is the best of the best. There was never a better Brothel Master in all of Zan, and there never will be.",
                          "Do you know about the King? I mean, the Brothel King? It's [MC.name], the legendary owner of [brothel.name]...",
                          "The best brothel in town? Where the hell did you come from? It's [brothel.name], of course! It's leagues ahead of every other whorehouse. The competitors just gave up.",
                          ],

                      # The following are added by the story

                      "c1_good" :   [
                                    "Captain Maya is really a godsend. She's going to clean up the Guard's act in no time, believe me.",
                                    "I was stopped by the guards the other day. I thought they would rob me like they usually do, but they were polite and they just let me go. Amazing.",
                                    "Many of the old guards have been kicked out of the force recently. It seems like the new captain is serious about fighting corruption.",
                                    "Don't ever tell him I said that, but it's obvious Roz has a crush on Maya. That big oaf doesn't stand a chance...",
                                    ],
                      "c1_neutral" :[
                                    "Is the new captain any better than the old one? Things will never change around here, no matter who's in charge.",
                                    "Captain Lydie seems just as shrewd as the old captain, but at least she keeps a low profile. Guild wars are bad for business.",
                                    "I've heard some talk of a secret lair somewhere around the Slums... A haven for thieves and bandits. I shiver to think of it.",
                                    "Thieves are getting bold these days. Or desperate. Doesn't look like the guards care to do anything about it, mind you.",
                                    "Some say the thieves operate in an organized fashion, much like a guild. I don't buy this nonsense. Ever seen a thief with anything else than spice for brains?",
                                    ],
                      "c1_evil" : [
                                    "Have you seen the new guard uniforms? They adorn their armor with fine silk, while the rest of us starve...",
                                    "Captain Farah is one greedy bitch. Her men came yesterday to shake one of my friends down. Everyone hates her, but they say she's got protection in high places.",
                                    "The head of the guards is Captain Farah. Best stay clear of them if you want my advice. Levies and taxes are all the guards cares about. If you ask me, they just make them up as they go.",
                                    "Some say the captain of the Guard is getting too greedy, even among her own men... There are some who say they'd do better. Maybe they mean they'd be better at not getting caught.",
                                    "My neighbor complained about the taxes, so they took him in, and no one's heard of him since. Better suck it up and stay alive, if you want my 2 denars.",
                                    "The guards took everything from me, but what can I do? Only the King has higher authority, and he won't listen to a commoner.",
                                    "People here like to blame a secret Shalia cabal for all their ills, but let me tell you: it's our good Arios-loving captain who's robbing us blind at the moment!",
                                    "Captain Farah is stronger than ever in the slums. She's completely unopposed now, our only choice is to pay her cronies. Do you want to hang?",
                                    "I thought things couldn't get worse with the Guard, but it did. They looted my shop and raped my wife and daughters. No one dared lift a finger...",
                                  ],

                      "c2_kunoichi" :[
                                    "Heard about the Kunoichi? A secret organization of female ninjas... That is so hot!",
                                    "I wish they'd catch those women devils, the Kunoichi. I hear they consort with demons.",
                                    "Don't believe what you hear about the Kunoichi. They're pure and noble warriors.",
                                    "I heard some kind of female ninja clan is going after a brothel owner in the city... Poor guy, he's dead meat.",
                                    "Female ninjas? I bet they wear very skimpy clothing... Hmm...",
                                    "I read the tale about female ninjas that can kill using only their vagina... Crazy, I know.",
                                    "When a baby gets abandoned, sometimes a ninja clan will adopt her... That's what I heard.",
                                  ],

                      "c2_kunoichi_hunt" :[
                                    "The {b}Thieves' guild{/b} quarter is already a dump... And now there are ninjas there, too???",
                                    "Ninjas in the {b}Thieves' guild{/b} quarter... The rogues ain't gonna like that.",
                                    "I told you I saw a child in the {b}Thieves' guild{/b} quarter... I was gonna help, but then I saw she had a huge ninja star, so I thought better of it.",
                                    "She did look like a lil' brat, but she was a ninja, I tells ya! Standin' atop the {b}Thieves' guild{/b}'s roof, no less.",

                                    "I was walking alongside the {b}Beach{/b} at night, when I saw a ghost! A beautiful, pale lady ghost. And she was walking over water. Like a ninja!"
                                    "I went to the {b}Beach{/b} at night to fish for trout, and I saw a beautiful lady taking a bath by the moonlight. When I tried to approach her, she disappeared like a ghost!",
                                    "There have been disappearances near the {b}Beach{/b}. Some blame ninjas, but that's childish nonsense.",
                                    "So the pretty lady waved her hand, and the water around her rose and shielded her from view. We couldn't see her from the {b}Beach{/b} anymore, and none of us dared venture into the sea.",

                                    "I'm telling you, she was a ninja! Who else could climb the {b}Prison{/b} walls like that?",
                                    "It was the most peculiar thing, the girl snapped her fingers, and it caused a tremor! The {b}Prison{/b} guards fell down on their asses.",
                                    "Why would a ninja stalk the {b}Prison{/b} quarter? Any criminal knows to steer clear of our good King's jails!",
                                    "Stop it, there are no such things as female ninjas flying above the {b}Prison{/b}! Now go clean up your room!",
                                  ],

                     }

    district_gossip = {"The Slums" : [
                                        "Thieves are everywhere in the slums, and guards are even worse. I can't wait to get out of this place. Other places can't possibly be this bad!",
                                        "The worst thing about the slums is the stench. Or second worst thing. Worse is, you can get your throat slit for a denar and never smell a thing, ever again.",
                                        "The people of Zan are wicked, depraved and degenerates, but they sure are industrious. The city grows by the day! And the slums are her underbelly.",
                                        "I saw this strange girl in the sewers, all by herself. I told her there were monsters about, but she just smiled and said 'I know.'",
                                        "The sewers are full of dirty critters and monsters... Some people even make a living hunting them.",
                                        "Have you met that strange girl, Willow? She's got odd ears, I wonder if she's fully human. She's cute, though.",
                                        "The farmland is haunted. Don't go there.",
                                        "There are always strange things going on in the country. I even hear some girls fuck animals there.",
                                        "Have you met Goldie at the farm? She's a sweet young woman. It's so sad, what happened to her family.",
                                        "I usually go and buy milk from Goldie at the farm. She gets it from her cows, but I'd rather milk her instead, if you catch my drift...",
                                        "If I wanted to buy animals, I'd go to the farm of course. But I hear some of them are behaving strangely.",
                                        "There's a crazy girl in the junkyard, sifting through the garbage to find Arios-knows-what. I tried to talk some sense into her, but she didn't even listen to me.",
                                        "I made a good deal last week, selling an old useless gizmo to the funny girl in the junkyard.",
                                        "Have you met Gina, the weird scientist in the junkyard? She buys and sells some weird machines. Gives me the creeps.",
                                        "A thieves guild, here, in the slums? Nonsense. The Guard captain would never allow it."
                                     ],
                       "The Docks" : ["The league of adventurers is located somewhere near the harbor. The smell of rotting fish isn't off-putting to those rogues.",
                                      "Why are there so many whorehouses close to the sea? Is it because it's wetter here?",
                                      "Why are there so many whorehouses in the Docks? Is it because it sounds like 'Dicks'?",
                                      "Where there are sailors, there are whores. That's just a fact of life.",
                                      "There's a woman selling gifts by the seafront. She's got those huge knockers...",
                                      "Have you seen that woman in red, selling gifts by the seafront? She's got gifts all right, a huge pair of tits...",
                                      "They sell those strange slaves by the harbor, mindless drones with horse-like cocks... My girlfriend thinks it's cool, but I find it creepy.",
                                      "There are slavemongers from the Blood Islands about in the harbor. They treat humans like cattle. It's awesome.",
                                      "Fancy ladies go to the harbor to buy some very special slaves... I hear they obey every order and they have huge... *whisper*",
                                      "Have you seen that fearsome slaver by the harbor, all clad in leather like a dominatrix? She turns me on... ",
                                     ],
                       "The Warehouse" : [],
                       "The Magic Gardens" : [],
                       "The Cathedra" : [
                                        "The Cathedra is the pride of Zan and the crown jewel of all Xeros. All rejoice in the glorious light of Arios!",
                                        "The Cathedra was a place for silent contemplation and prayer, but with all the filthy pilgrims who pour in now, day in, day out, I don't want to go there anymore.",
                                        "The waves of pilgrims heading to the Cathedra have been good for business, that's for sure.",
                                        "Judging by the fervor at the Cathedra, you'd think Arios was the one and only god... Many of us in this city are not followers of Arios; they seem to forget that all too easily.",
                                        ],
                       "The King's Hold" : [
                                            "The knights in the palace are all good Arios-loving folks. That warms my heart.",
                                            "I've been told of a secret swapping society in the King's Hold, where members exchange their wives and daughters in all-night orgies...",
                                            "The nobles roam the King's Hold, like a pack of vultures hovering, waiting for their next meal. They all think they can sire the next heir, or take power by other means when the King's gone...",
                                            ],
                       }




    ## JOKES ##

    jokes = {
             "harmless" : ("What's the hardest thing about being a Guard? Telling your parents you're gay!", "My dog used to run after everyone on a horse. It got so bad, I had to take his horse away.", "What's the difference between a snowman and a snowwoman? Snowballs!", "How do you catch a bra? With a booby trap."),
             "sex" : ("Why was the luth teacher arrested? For fingering a minor...", "What do the Court and pussies have in common? One slip of the tongue, and you're in deep shit.", "Know what I do in my garden? Get down and dirty with my hoes.", "What do you call the useless part around a dick? A man!", "What’s the difference between a wife and a job? After 5 years, your job will still suck."),
             "dark" : ("How do you make a girl scream twice? First, fuck her in the ass, then wipe your dick on her curtains!", "I like my women like my wine... Locked in the cellar!", "A doctor tells his patient:'I'm sorry, but you've only got about 10 left.'\nPatient:'10 what? Months, weeks?'\nDoctor:'Nine, eight...'", "What’s the best part about sex with twenty-eight-year-olds? There are 20 of them!", "How many male chauvinists does it take to refuel the lamp? None. Let her do the dishes in the dark."),
             "mean" : ("I like you. People say I've no taste, but I like you.", "Damn, you're hot, but you'd be a lot hotter if you just shut up.", "I like my women attractive, dumb, and bitchy. You seem to fit the bill quite nicely.", "I'd hire you as a whore, but my girls have class...")
            }


    ## COMPLIMENTS ##

    compliments =  {
                    "beauty" : ("%s, aren't you beautiful today...", "%s, you're so lovely...", "%s, I swear you have the cutest face.", "Your face lights up when you smile, %s."),
                    "body" : ("Wow, you've got such a hot body you know.", "Baby, you've got such an amazing ass...", "I love your knockers, honey, they look amazing without a bra.", "Look at that nice piece of ass...", "Wow, you're stunning, makes me really want to touch the merchandise!"),
                    "mind" : ("You're a bright girl, I like that about you.", "A beautiful mind... Haven't you got everything?", "You seem to know a lot... You definitely should get to know more about me!", "I love the conversations we're having, it's always enlightening."),
                    "spirit" : ("You're always spirited and lively; it's very nice.", "At last, someone with character. I don't like dull people.", "You're always passionate about everything. I like that!")
                    }


    ## GIRL BACKGROUND ##

    slave_stories = ["slave_story1", "slave_story2", "slave_story3", "slave_story4", "slave_story5", "slave_story6", "slave_story7", "slave_story8"]

    origins = ["Zan", "the border with the Holy Lands", "the Blood Islands", "Karkyr", "Westmarch", "the desert of Hokoma", "Borgo, the port city", "the Goliath desolations", "the Arik mountains"]

#     origin_description = {
#                           "Zan" : "I know the old streets of Zan like the back of my hand... I used to walk to the market with my %s, wondering what the strange houses with the red lanterns were... Now I know... *blush*",
#                           "the border with the Holy Lands" : "The Holy Lands are a place of war and suffering, always have been. Still, I remember a few peaceful moments. Walking with my %s across old battlefields, covered with red blooming flowers, watching nature reclaim its rights...",
#                           "the Blood Islands" : "The Blood Islands are a cruel place... I remember going to the arena with my %s and me, watching slaves being shredded to pieces by monsters... It was bloody and exciting. The arena here is very tame in comparison.",
#                           "Karkyr" : "Karkyr is a beautiful and fascinating city, ruled by the Archmage Council. Everything is magical, even the wells and the furniture can speak. It used to freak my %s out! There were also some spectacular incidents, of course, but that was part of the fun.",
#                           "Westmarch" : "The Westmarch Principalities, where I grew up, is a very unpredictable place. One day a city is flourishing, the next it descends into anarchy, and raiders loot and rape the town. I used to think danger was exciting, but my %s didn't like it one bit.",
#                           "the desert of Hokoma" : "The desert people are a quiet and wise sort. My %s know many secrets, and knew how to keep them. I miss the peace and quiet of nights in the desert.",
#                           "Borgo, the port city" : "There's no describing how busy and crowded Borgo is on most days, with sailors from all over the world selling everything you can imagine, and many other things, too. I loved to sit by the pier with my %s in the early hours, listenning to the waves.",
#                           "the Goliath desolations" : "The desolations are a cold, horrible place. Whether you are rich or poor, you have to work hard every day, just to barely survive. If I didn't have my %s to rely on, I don't know what I would have done.",
#                           "the Arik mountains" : "They say the Arik mountains are the highest in the world. The air is pure there, not full of filth and magic like here... My %s taught me how to love and respect the mountains.",
#                           }

    homes = ["palace", "hovel", "mansion", "shack", "hut", "big house", "small house", "temple", "shop", "old house", "tower", "church"]

    guardians = ["parents", "dad", "mom", "uncle", "grand-ma", "auntie", "grand-pa", "big brother", "big sister", "little brother", "little sister", "tutor"]

    hobbies = ["painting", "singing", "playing music", "hiking", "gambling", "shopping", "reading", "weaving", "swimming", "writing"]

    colors = ["white", "yellow", "red", "green", "blue", "purple", "orange", "pink", "black"]

    food = ["cake", "cream", "fish", "fruits", "meat", "cookies", "sweets", "chocolate", "bread", "rice"]

    drinks = ["milk", "sake", "wine", "beer", "apple juice", "lemon juice", "mango juice", "spice water"]


    ## MC interact counters ##

#    MC_interact_counters = {
#                            "chat" : 0, "gossip" : 0, "life" : 0, "love" : 0,
#                            "origins" : 0, "hobbies" : 0, "likes" : 0, "dislikes" : 0,
#                            "harmless" : 0, "adult" : 0, "dark" : 0, "mean" : 0,
#                            "present" : 0, "money" : 0,
#                            "beauty" : 0, "body" : 0, "mind" : 0, "spirit" : 0,
#                            "hand" : 0, "kiss" : 0, "ass" : 0, "breasts" : 0, "pussy" : 0,
#                            "service" : 0, "sex" : 0, "anal" : 0, "fetish" : 0,
#                            "offer" : 0,
#                            "well_being" : 0, "happiness" : 0, "job" : 0,
#                            "scold" : 0, "threaten" : 0, "beat" : 0, "torture" : 0,
#                            "charm_obedience" : 0, "charm_sensitivity" : 0, "charm_libido" : 0, "charm_love" : 0, "charm_fear" : 0
#                            }

    ## Results dictionaries

    roll_dict = {1 : "critical failure", 2 : "failure", 3 : "neutral", 4 : "neutral", 5 : "success", 6 : "critical success"}
    result_dict = {-999 : "very bad", 1 : "bad", 6 : "average", 9 : "good", 12 : "very good", 15 : "perfect"}
    result_colors = {"very bad" : c_red, "bad" : c_lightred, "average" : c_white, "good" : c_lightgreen, "very good" : c_green, "perfect" : c_orange}

    reversed_result_dict = {v: k for k, v in result_dict.items()}

#    result_value = {"very bad" : 0, "bad" : 1, "average" : 2, "good" : 3, "very good" : 4, "perfect" : 5}
#    roll_value = {"critical failure" : 0, "failure" : 1, "neutral" : 2, "success" : 3, "critical success" : 4}

#    result_names = {v: k for k, v in result_value.items()}
#    roll_names = {v: k for k, v in roll_value.items()}

    perform_job_dict = {
#                        "roll_critical failure" : "\n{color=[c_red]}%s wasn't trying hard today. She barely even paid attention to what she was doing.{/color}",
#                        "roll_failure" : "\n%s wasn't really into it.",
#                        "roll_neutral" : "\n%s went about her job as usual.",
#                        "roll_success" : "\n%s was really motivated today.",
#                        "roll_critical success" : "\n{color=[c_green]}%s did everything she could to please the customers.{/color}",

                        "waitress_stats" : (("charm", 6), ("constitution", 2), ("body", 1), ("beauty",1)),
                        "waitress_changes" : ((("charm",), 100, 3), (("constitution",), 25, 2), (("obedience", "body", "beauty"), 15, 1), (("sensitivity",), 15, -1)),

                        "waitress_init" : "%s served drinks to %s customers.",
                        "waitress_tags" : ["waitress"],
                        "waitress_tags2" : ["geisha"],

                        "dancer_stats" : (("body", 6), ("libido", 2), ("refinement", 1), ("charm",1)),
                        "dancer_changes" : ((("body",), 100, 3), (("libido",), 25, 2), (("constitution", "refinement", "charm"), 15, 1), (("obedience",), 15, -1)),

                        "dancer_init" : "%s danced sexily for %s customers.",
                        "dancer_tags" : ["dancer"],
                        "dancer_tags2" : ["profile", "fight"],

                        "masseuse_stats" : (("beauty", 6), ("sensitivity", 2), ("refinement", 1), ("body",1)),
                        "masseuse_changes" : ((("beauty",), 100, 3), (("sensitivity",), 25, 2), (("refinement", "body", "libido"), 15, 1), (("constitution",), 15, -1)),

                        "masseuse_init" : "%s gave a hot massage to %s customers.",
                        "masseuse_tags" : ["masseuse"],
                        "masseuse_tags2" : ["swim"],

                        "geisha_stats" : (("refinement", 6), ("obedience", 2), ("beauty", 1), ("charm",1)),
                        "geisha_changes" : ((("refinement",), 100, 3), (("obedience",), 25, 2), (("beauty", "charm", "sensitivity"), 15, 1), (("libido",), 15, -1)),

                        "geisha_init" : "%s entertained %s customers with a display of traditional arts.",
                        "geisha_tags" : ["geisha"],
                        "geisha_tags2" : ["waitress", "date"], # Date pictures can be used as substitutes for geisha

                        "waitress_very bad" : "\n{color=[c_red]}%s spilled drinks everywhere and didn't even apologize. The customers thought the service was terrible and complained.",
                        "waitress_bad" : "\n{color=[c_lightred]}%s was shy and clumsy. The customers grumbled that the service was bad.",
                        "waitress_average" : "\n%s served everyone and chatted with the customers. They thought she was ok.",
                        "waitress_good" : "\n{color=[c_lightgreen]}%s flirted with the customers as she served them drinks, making them feel welcome.",
                        "waitress_very good" : "\n{color=[c_green]}%s traded rowdy jokes with the customers, flashing her goods while serving. Everyone loved her.",
                        "waitress_perfect" : "\n{color=[c_orange]}%s worked without underwear today and used all of her charms to drive the customers wild. They completely fell over for her.",

                        "dancer_very bad" : "\n{color=[c_red]}%s has two left feet. Her dancing was embarrassingly bad and the customers booed and threw things at her.",
                        "dancer_bad" : "\n{color=[c_lightred]}%s's dance was awkward and uninteresting.",
                        "dancer_average" : "\n%s danced suggestively in front of the customers.",
                        "dancer_good" : "\n{color=[c_lightgreen]}The club heats up as %s dances around the stage, flashing her goods.",
                        "dancer_very good" : "\n{color=[c_green]}The crowd goes wild as %s dances and strips on stage, her skin glistening with sweat as she works that pole.",
                        "dancer_perfect" : "\n{color=[c_orange]}The customers cannot take their eyes off %s as she waves to the music, slowly and sexily stripping off, until she stands there naked and wet under their perverted gaze.",

                        "masseuse_very bad" : "\n{color=[c_red]}%s clumsily goes around giving back rubs, hurting some of them in the process. They grumble and tell her to go away.",
                        "masseuse_bad" : "\n{color=[c_lightred]}%s tries to give customers a relaxing rub. Her technique is lacking, and the customers are left unsatisfied.",
                        "masseuse_average" : "\n%s gives massages to customers in the onsen, helping them relax and feel more comfortable.",
                        "masseuse_good" : "\n{color=[c_lightgreen]}%s joins the customers in the onsen, wearing only a towel, and gives them a nice massage. The customers are visibly turned on after she's done.",
                        "masseuse_very good" : "\n{color=[c_green]}The towels slip off as %s gives customers a passionate body massage. She uses her hands and tongue to turn them on while they wait for their turn.",
                        "masseuse_perfect" : "\n{color=[c_orange]}%s goes naked into the onsen among the customers, rubbing her body against them until they come on her silky skin.",

                        "geisha_very bad" : "\n{color=[c_red]}%s completely lacks class and comes across as clumsy and dumb. The customers complain she is just a street girl dressed as a geisha.",
                        "geisha_bad" : "\n{color=[c_lightred]}%s keeps trying to act like a real geisha when serving tea; it's obvious to anyone that she's not the real thing, though, and the customers quickly lose interest.",
                        "geisha_average" : "\n%s plays a little shamisen and chats with the customers, helping them relax and forget their worries...",
                        "geisha_good" : "\n{color=[c_lightgreen]}%s holds a tea ceremony with the customers, exchanging pleasantries while she nonchalantly lets her kimono slide to the side, revealing some skin.",
                        "geisha_very good" : "\n{color=[c_green]}%s is the life of the party as she greets customers by their name and compliments them. Wearing a short, revealing kimono, she brushes against them, leaving them all turned on by her scent.",
                        "geisha_perfect" : "\n{color=[c_orange]}%s is the epitome of the geisha, being in turn sweet, gifted, witty, and sexy as hell. She wears a see-through kimono, kinkily displaying her cleavage and thighs to drive the customers wild.",

                        "flasher" : " A customer dared her to show her tits, and she proudly displayed them for everyone to see.",
                        "temptress" : " She convinced the customer%s to try something different.",
                        "catgirl" : " She purred as she eagerly drank all the customer's cum and licked his dick clean.",
                        "virgin" : " The customer was amazed that she was a virgin and paid extra.",
                        "virgin_group" : " The customers were amazed that she was a virgin and paid extra.",
                        "reroll" : " She barely avoided a catastrophe.",
                        "unlucky" : "",
                        "lucky" : "",
                        "random item" : " The customer%s left something valuable.",
                        "beauty bonus" : " The customer%s found her beauty stunning.",
                        "body bonus" : " The customer%s loved her curves.",
                        "charm bonus" : " The customer%s fell under her charm.",
                        "refinement bonus" : " The customer%s loved how refined she was.",
                        "libido bonus" : " The customer%s thought she was hot.",
                        "obedience bonus" : " The customer%s liked how she took orders.",
                        "constitution bonus" : " The customer%s thought she was fit.",
                        "sensitivity bonus" : " The customer%s loved how sensitive she was.",

                        "DT_group" : " The customers took turns sticking their dicks down her throat as deep as they could.",
                        "DT" : " The customer was amazed that he could stick his dick so far down her throat.",
                        "bukkake" : " She was fucked hard in her every hole, then the customers took turns coming all over her face.",
                        "creampie" : " He came all over her pussy and belly while she moaned with pleasure.",
                        "creampie_group" : " They took turns coming into her pussy until it dripped buckets of cum.",
                        "anal creampie" : " He fucked her ass hard then shot a huge load in her open asshole.",
                        "anal creampie_group" : " They took turns fucking and cumming in her ass until her belly was swollen with cum.",
                        "cum on face" : " He moaned and came loads all over her face and hair.",
                        "cum on face_group" : " They moaned, cumming loads all over her face and hair.",
                        "swallow" : " She eagerly swallowed the cum as it dripped down her throat.",
                        "irrumatio" : "",

                        "not satisfied" : " :Pron: was disappointed that she wouldn't do what :pron: wanted.",
                        "group not satisfied" : " She wouldn't do it, but they didn't mind because group %s is hot.",
                        "bisexual not satisfied" : " In the end :pron: got %s, but :pron: was happy to let the girls have their way.",

                        "roll_critical failure" : "\n{color=[c_red]}%s wasn't trying hard today. She barely even paid attention to what she was doing.{/color}",
                        "roll_failure" : "\n%s wasn't really into it.",
                        "roll_neutral" : "\n%s went about her job as usual.",
                        "roll_success" : "\n%s was really motivated today.",
                        "roll_critical success" : "\n{color=[c_green]}%s did everything she could to please.{/color}",

                        "bisexual_roll_critical failure" : "\n{color=[c_red]}%s weren't trying hard today. They weren't paying attention to what they were doing.{/color}",
                        "bisexual_roll_failure" : "\n%s weren't really into it.",
                        "bisexual_roll_neutral" : "\n%s went about their job as usual.",
                        "bisexual_roll_success" : "\n%s were really motivated and playful today.",
                        "bisexual_roll_critical success" : "\n{color=[c_green]}%s did everything they could to please the customers and each other.{/color}",

                        "anal_stats" : (("anal", 6), ("constitution", 2), ("body", 1), ("sex",1)),
                        "anal_changes" : ((("anal",), 100, 3), (("constitution",), 50, 2), (("libido", "obedience", "body"), 25, 1), (("sensitivity",), 25, -1)),
                        "anal_init" : " :Pron: wanted to fuck %s in the ass.",
                        "anal_tags" : ["anal"],

                        "sex_stats" : (("sex", 6), ("libido", 2), ("beauty", 1), ("service",1)),
                        "sex_changes" : ((("sex",), 100, 3), (("libido",), 50, 2), (("sensitivity", "constitution", "beauty"), 25, 1), (("obedience",), 25, -1)),
                        "sex_init" : " :Pron: wanted to have sex with %s.",
                        "sex_tags" : ["sex"],

                        "service_stats" : (("service", 6), ("sensitivity", 2), ("charm", 1), ("fetish",1)),
                        "service_changes" : ((("service",), 100, 3), (("sensitivity",), 50, 2), (("obedience", "libido", "charm"), 25, 1), (("constitution",), 25, -1)),
                        "service_init" : " :Pron: wanted %s to give service.",
                        "service_tags" : ["service"],

                        "fetish_stats" : (("fetish", 6), ("obedience", 2), ("refinement", 1), ("anal",1)),
                        "fetish_changes" : ((("fetish",), 100, 3), (("obedience",), 50, 2), (("constitution", "sensitivity", "refinement"), 25, 1), (("libido",), 25, -1)),
                        "fetish_init" : " :Pron: had some very special requests for %s.",
                        "fetish_tags" : ["fetish"],

                        "whore_init" : "%s came to your brothel and chose %s.",
                        "bisexual_tags" : ["bisexual"],
                        "group_tags" : ["group"],

                        "M anal_very bad" : "\n{color=[c_red]}%s had a hard time and didn't like it one bit. The customer quickly lost interest and left grumbling.",
                        "M anal_bad" : "\n{color=[c_lightred]}%s doesn't like it in the ass and it showed. She didn't enjoy herself and neither did the customer.",
                        "M anal_average" : "\n%s moans as the customer gets his way with her ass. She's growing to enjoy anal sex.",
                        "M anal_good" : "\n{color=[c_lightgreen]}%s takes it up the ass with moans of pleasure. The customer comes all over her butt with a delighted smile on his face.",
                        "M anal_very good" : "\n{color=[c_green]}Looks like this girl was made for anal. %s uses her ass to work the customer's dick until it's hard as a rock, inviting him to cum and fill her up.",
                        "M anal_perfect" : "\n{color=[c_orange]}%s is an anal sex goddess. She takes it up the ass with unbridled pleasure, crying out loud as the customer releases his seed deep into her belly.",

                        "M sex_very bad" : "\n{color=[c_red]}%s is a terrible lay, not enjoying it one bit as the customer violates her body. The customer thought she was awful and left complaining.",
                        "M sex_bad" : "\n{color=[c_lightred]}%s tries her best to give the customer a good time, but her fake cries are rather obvious. The customer left relieved but disappointed.",
                        "M sex_average" : "\n%s fucks with the customer and tries a few interesting positions. She is starting to enjoy herself and some of her moans were clearly not fake.",
                        "M sex_good" : "\n{color=[c_lightgreen]}After a quick bout of foreplay, %s and the customer have wild sex in various positions until he cums hard all over her body.",
                        "M sex_very good" : "\n{color=[c_green]}%s is amazing and works that dick like a succubus. She reaches orgasm and cries out as the customer pumps warm cum into her.",
                        "M sex_perfect" : "\n{color=[c_orange]}%s cannot get enough, screaming loudly as she enjoys being fucked through multiple orgasms and being covered in the customer's sticky cum.",

                        "M service_very bad" : "\n{color=[c_red]}The customer complains that %s doesn't know how to work a dick properly. The customer leaves, upset that she didn't even manage to finish him off.",
                        "M service_bad" : "\n{color=[c_lightred]}%s awkwardly tries to service the customer, but her technique is clearly lacking. He ends up masturbating while she looks on with shame.",
                        "M service_average" : "\n%s does her best to service the customer, slowly developing her own technique. After teasing the customer for a while, she smiles as he releases his load on her face.",
                        "M service_good" : "\n{color=[c_lightgreen]}%s uses her skills to make the customer cum quickly and repeatedly, covering her face and tits with bodily fluids.",
                        "M service_very good" : "\n{color=[c_green]}%s is already wet thinking of the customer's dick as she starts sucking and licking it. It isn't long until the customer comes hard in her mouth.",
                        "M service_perfect" : "\n{color=[c_orange]}%s offers the customer her body to play with and makes wet sounds as she expertly sucks him off. She savours the feeling of hot, sticky cum on her face and in her mouth, begging the customer for more.",

                        "M fetish_very bad" : "\n{color=[c_red]}%s is scared and tense under the customer's touch. She is not enjoying this at all and the customer leaves completely unsatisfied.",
                        "M fetish_bad" : "\n{color=[c_lightred]}%s shivers as the customer does new, weird things to her body. The customer watches her reactions with some interest at first, but the slow pace quickly bores him.",
                        "M fetish_average" : "\n%s moans a little as she is blindfolded and tied up. She seems more curious than scared about what's happening to her now, and the customer has fun playing with her for a while.",
                        "M fetish_good" : "\n{color=[c_lightgreen]}%s shivers with excitement as she feels the bite of the ropes in her skin. The customer teases her body until she is completely wet, begging to be fucked.",
                        "M fetish_very good" : "\n{color=[c_green]}%s enjoys the mix of pleasure and pain and begs submissively for more. The customer violates her as she's tied up, bringing her to climax as he cums hard all over her.",
                        "M fetish_perfect" : "\n{color=[c_orange]}%s enjoys everything the customer does to her, suggesting new, humiliating ways to tie herself up and get punished. She screams with pain and pleasure, cumming multiple times as her various holes are violated.",

                        "M bisexual_very bad" : "\n{color=[c_red]}%s were clumsy and uncooperative. The customer quickly got bored and left, grumbling about a refund.",
                        "M bisexual_bad" : "\n{color=[c_lightred]}It's obvious %s aren't really good at this and are just pretending. The customer fucks them one after the other, but there is no chemistry.",
                        "M bisexual_average" : "\n%s slowly finger their pussies while the customer looks on with lust. He soon joins them, and they do their best to make it a memorable time.",
                        "M bisexual_good" : "\n{color=[c_lightgreen]}%s are eagerly touching and teasing each other. They playfully try new ways to excite the customer, and he quickly cums as they play with each other's breasts and pussy.",
                        "M bisexual_very good" : "\n{color=[c_green]}%s love cock as much as they love each other. They both work the customer's dick using their hands, mouths and bodies, making him come all over them.",
                        "M bisexual_perfect" : "\n{color=[c_orange]}%s are perfect sex kittens, expertly licking each other's cunt while the customer fucks their every hole. They eagerly kiss and lick the cum from each other's mouth as he looks on with bliss.",

                        "group_very bad" : "\n{color=[c_red]}With too many customers to satisfy, %s seems at a loss and doesn't know what to do. The group leaves unsatisfied and complaining.",
                        "group_bad" : "\n{color=[c_lightred]}%s is kind of shy in a group. She tries to do her job but the customers find her performance rather underwhelming.",
                        "group_average" : "\nThe customers take turns fucking %s. She takes it all in stride.",
                        "group_good" : "\n{color=[c_lightgreen]}%s works hard to please every customer in the group, bringing them to a grand finish using her every hole. A moment they will not soon forget.",
                        "group_very good" : "\n{color=[c_green]}%s is fucked long and hard by the customers and it looks like she isn't ready to stop. It looks like no matter how many times they fuck her, she always wants another dick.",
                        "group_perfect" : "\n{color=[c_orange]}%s couldn't wait to have her every hole filled by the customers, not letting them rest until they have spurted their cum over every inch of her body.",

                        "F anal_very bad" : "\n{color=[c_red]}%s had a hard time and didn't like it one bit. The customer quickly lost interest and left grumbling.",
                        "F anal_bad" : "\n{color=[c_lightred]}%s doesn't like it in the ass and it showed. She didn't enjoy herself and neither did the customer.",
                        "F anal_average" : "\n%s moans as the customer gets her way with her ass. She's growing to enjoy anal sex.",
                        "F anal_good" : "\n{color=[c_lightgreen]}%s takes it up the ass with moans of pleasure. The customer pounds her butt with a delighted smile on her face.",
                        "F anal_very good" : "\n{color=[c_green]}Looks like this girl was made for anal. %s uses her ass to grind against the customer's pussy until it becomes very wet, inviting her to cum together with her.",
                        "F anal_perfect" : "\n{color=[c_orange]}%s is an anal sex goddess. She takes it up the ass with unbridled pleasure, crying out loud as the customer reaches her own intense orgasm.",

                        "F sex_very bad" : "\n{color=[c_red]}%s is a terrible lay, not enjoying it one bit as the customer violates her body. The customer thought she was awful and left complaining.",
                        "F sex_bad" : "\n{color=[c_lightred]}%s tries her best to give the customer a good time, but her fake cries are rather obvious. The customer left relieved but disappointed.",
                        "F sex_average" : "\n%s fucks with the customer and tries a few interesting positions. She is starting to enjoy herself and some of her moans were clearly not fake.",
                        "F sex_good" : "\n{color=[c_lightgreen]}After a quick bout of foreplay, %s and the customer have wild sex in various positions until they both cum hard.",
                        "F sex_very good" : "\n{color=[c_green]}%s is amazing and works that pussy like a succubus. She reaches orgasm and cries out as the customer gushes love juice all over her.",
                        "F sex_perfect" : "\n{color=[c_orange]}%s cannot get enough, screaming loudly as she enjoys being fucked through multiple orgasms and being covered in the customer's sticky love juice.",

                        "F service_very bad" : "\n{color=[c_red]}The customer complains that %s doesn't know how to work a pussy properly. She leaves, upset that she didn't even manage to finish her off.",
                        "F service_bad" : "\n{color=[c_lightred]}%s awkwardly tries to service the customer, but her technique is clearly lacking. The customer ends up masturbating while she looks on with shame.",
                        "F service_average" : "\nShe does her best to service the customer, slowly developing her own technique. After teasing the customer for a while, %s smiles as she receives the customer's splashing love juices all over her face.",
                        "F service_good" : "\n{color=[c_lightgreen]}%s uses her skills to make the customer squirt hard, covering her face and tits with bodily fluids.",
                        "F service_very good" : "\n{color=[c_green]}%s is already wet thinking of the customer's pussy as she starts fingering and licking it. It isn't long until the customer comes hard from her tongue work.",
                        "F service_perfect" : "\n{color=[c_orange]}%s offers the customer her body to play with and makes wet sounds as she expertly licks her out. She savours the feeling of hot, sticky love juice on her face and in her mouth, begging the customer for more.",

                        "F fetish_very bad" : "\n{color=[c_red]}%s is scared and tense under the customer's touch. She is not enjoying this at all and the customer leaves completely unsatisfied.",
                        "F fetish_bad" : "\n{color=[c_lightred]}%s shivers as the customer does new, weird things to her body. The customer watches her reactions with some interest at first, but the slow pace quickly bores her.",
                        "F fetish_average" : "\n%s moans a little as she is blindfolded and tied up. She seems more curious than scared about what's happening to her now, and the customer has fun playing with her for a while.",
                        "F fetish_good" : "\n{color=[c_lightgreen]}%s shivers with excitement as she feels the bite of the ropes in her skin. The customer teases her body until she is completely wet, begging to be fucked.",
                        "F fetish_very good" : "\n{color=[c_green]}%s enjoys the mix of pleasure and pain and begs submissively for more. The customer violates her as she's tied up, bringing her to climax as she cums hard with her.",
                        "F fetish_perfect" : "\n{color=[c_orange]}%s enjoys everything the customer does to her, suggesting new, humiliating ways to tie herself up and get punished. She screams with pain and pleasure, cumming multiple times as her various holes are violated.",

                        "F bisexual_very bad" : "\n{color=[c_red]}%s were clumsy and uncooperative. The customer quickly got bored and left, grumbling about a refund.",
                        "F bisexual_bad" : "\n{color=[c_lightred]}It's obvious %s aren't really good at this and are just pretending. The customer fucks them one after the other, but there is no chemistry.",
                        "F bisexual_average" : "\n%s slowly finger their pussies while the customer looks on with lust. She soon joins them, and they do their best to make it a memorable time.",
                        "F bisexual_good" : "\n{color=[c_lightgreen]}%s are eagerly touching and teasing each other. They playfully try new ways to excite the customer, and she quickly cums as they play with each other's breasts and pussies.",
                        "F bisexual_very good" : "\n{color=[c_green]}%s love pussy. They both work the customer's erogenous zones using their hands, mouths and bodies, making her come again and again.",
                        "F bisexual_perfect" : "\n{color=[c_orange]}%s are perfect sex kittens, expertly licking the customer's cunt and each other. They eagerly kiss and lick the love juice from each other's mouth as she looks on with bliss.",

                        }

    stat_increase_dict = {
                        "level" : "\n{color=[c_lightgreen]}LEVEL UP{/color}",
                        "stat" : "\n%s {color=[c_green]}+%s{/color}",
                        "stat_neg" : "\n%s {color=[c_red]}%s{/color}",
                        "xp" : "\nXP {color=[c_lightgreen]}+%s{/color}",
                        "xp_dark" : "\nXP {color=[c_darkgreen]}+%s{/color}",
                        "jp" : "\nJP {color=[c_orange]}+%s{/color}",
                        "gold+" : "\nGold {color=[c_darkgold]}+%s{/color}",
                        "gold-" : "\nGold {color=[c_darkgold]}%s{/color}",
                        "rep" : "\nRep. {color=[c_softpurple]}+%s{/color}",
                        "rep_neg" : "\nRep. {color=[c_red]}%s{/color}",
                        "job_up" : "\n{color=[c_orange]}JOB SKILL UP{/color}",
                        "rank" : "\n{color=[c_softpurple]}NEW RANK AVAILABLE{/color}"
                        }

    # Contrast colors are for lighter backgrounds
    event_color = {"special": "{color=[c_orange]}%s{/color}",
                   "good": "{color=[c_green]}%s{/color}",
                   "a little good": "{color=[c_lightgreen]}%s{/color}",
                   "average": "{color=[c_yellow]}%s{/color}",
                   "average contrast": "{color=[c_darkorange]}%s{/color}",
                   "a little bad": "{color=[c_lightred]}%s{/color}",
                   "a little bad contrast": "{color=[c_redpink]}%s{/color}",
                   "bad": "{color=[c_red]}%s{/color}",
                   "very bad": "{color=[c_crimson]}%s{/color}",
                   "fear": "{color=[c_purple]}%s{/color}",
                   "rep": "{color=[c_magenta]}%s{/color}",
                   "normal": "{color=[c_white]}%s{/color}",
                   "normal contrast": "{color=[c_black]}%s{/color}",
                   }

    log_event_dict = {
                        "level" : "{color=[c_orange]}%s has gained a new level.{/color}",
                        "job_up" : "{color=[c_orange]}%s has increased her %s skill.{/color}",
                        "rank" : "{color=[c_orange]}%s is ready to reach a new rank.{/color}"
                        }

    attraction_dict = {
                       "beauty_good" : "was very beautiful",
                       "body_good" : "had a perfect body",
                       "charm_good" : "had great charm",
                       "refinement_good" : "was really refined",
                       "beauty_bad" : "was ugly",
                       "body_bad" : "was plain looking",
                       "charm_bad" : "was a bore",
                       "refinement_bad" : "was clumsy"
                      }

    #### BROTHEL SERVICES ####

    maintenance_desc = {"clean" : "Your brothel is " + event_color["good"] % "{b}clean{/b}" + ".",
                    "clean enough" : "Your brothel is " + event_color["a little good"] % "{b}clean enough{/b}" + ".",
                    "dusty" : "Your brothel is getting " + event_color["average contrast"] % "{b}dusty{/b}" + ".",
                    "dirty" : "Your brothel is getting " + event_color["a little bad"] % "{b}dirty{/b}" + ".",
                    "disgusting" : "Warning! Your brothel is " + event_color["bad"] % "{b}disgusting{/b}" + "!",
                    "fire" : event_color["very bad"] % "Warning!!! Your brothel is at risk of a fire!"
                    }

    gold_threat_amount = {1 : 500, 2 : 1000, 3 : 2500, 4 : 10000, 5: 25000} # Gain 1 threat for every slice of X gold depending on DISTRICT RANK up to gold max

    gold_threat_max = {1 : 4, 2 : 12, 3 : 18, 4 : 24, 5: 30, 6 : 36, 7 : 52} # Max gold threat depending on CHAPTER



    #### ITEMS ####

    quality_prefix = {
                      "dress_0" : "Ragged ",
                      "dress_1" : "Worn ",
                      "dress_2" : "Simple ",
                      "dress_3" : "Fine ",
                      "dress_4" : "Fancy ",
                      "dress_5" : "Enchanted ",
                      "dress_6" : "Legendary ",

                      "necklace_0" : "Rusty ",
                      "necklace_1" : "Broken ",
                      "necklace_2" : "Small ",
                      "necklace_3" : "",
                      "necklace_4" : "Heavy ",
                      "necklace_5" : "Magical ",
                      "necklace_6" : "Legendary ",

                      "ring_0" : "Rusty ",
                      "ring_1" : "Fake ",
                      "ring_2" : "Small ",
                      "ring_3" : "Medium ",
                      "ring_4" : "Large ",
                      "ring_5" : "Magical ",
                      "ring_6" : "Legendary ",

#                      "gift_1" : "Cheap ",
#                      "gift_2" : "Common ",
#                      "gift_3" : "Fine ",
#                      "gift_4" : "Rare ",

                      "food_0" : "Rotten ",
                      "food_1" : "Spicy ",
                      "food_2" : "Tasty ",
                      "food_3" : "Juicy ",
                      "food_4" : "Organic ",
                      "food_5" : "Enchanted ",
                      "food_6" : "Legendary ",

#                      "accessory_1" : "Worn ",
#                      "accessory_2" : "Simple ",
#                      "accessory_3" : "Fine ",
#                      "accessory_4" : "Fancy ",
#                      "accessory_5" : "Enchanted ",

                      "scroll_0" : "Tattered ",
                      "scroll_1" : "Minor ",
                      "scroll_2" : "Lesser ",
                      "scroll_3" : "",
                      "scroll_4" : "Greater ",
                      "scroll_5" : "Ultimate ",

                      "misc_0" : "Worthless ",
                      "misc_1" : "Cheap ",
                      "misc_2" : "Common ",
                      "misc_3" : "Fine ",
                      "misc_4" : "Rare ",
                      "misc_5" : "Magical ",
                      "misc_6" : "Legendary "

                      }

    quality_modifier = { # High increase in cost for upper ranks (see how it behaves)
                        0 : 0.25,
                        1 : 1.0,
                        2 : 2.5, #!
                        3 : 5.0, #!
                        4 : 12.5, #!
                        5 : 25.0, #!
                        6 : 50.0 #!
                        }



    #### QUESTS & CLASSES ####

    ## PRICES ##

    special_quest_description = {
                                 "Cheap" : "This class is cheap. Enroll now and benefit from better prices!",
                                 "Masterclass" : "This class is taught by a master. Stats will increase faster than normal.",
                                 "High reward" : "The rewards for this quest are more important than usual.",
                                 "Notorious" : "This quest will bring extra reputation when completed."
                                 }

    quest_base_gold = { # This the gold value per stat point of requirement and per day
                        "normal" : 1,
                        "sex" : 2
                        }

    class_prices = {
                    1 : 100,
                    2 : 250,
                    3 : 500,
                    4 : 1000,
                    5 : 1000
                    }

    ## CLASS PREFIXES ##

    class_prefixes = {
                    1 : "Beginner ",
                    2 : "Regular ",
                    3 : "Advanced ",
                    4 : "Elite ",
                    5 : "Elite "
                    }


    #### MODIFIERS ####

    ## PRICE MODIFIERS ##

    price_modifiers = {
                            "buy" : 1.0,
                            "sell" : 0.6,
                            "bargain" : 0.75,
#                             "buy item" : 1.0,
#                             "sell item" : 0.6
                            }

#     price_modifiers_trader = {
#                             "buy girl" : 0.9,
#                             "sell girl" : 0.7,
#                             "buy item" : 0.9,
#                             "bargain item" : 0.75,
#                             "sell item" : 0.7
#                             }

    ## ROLL MODIFIERS ##

    stat_bonus = {"primary" :  (4, 2.5, 1.5, 0),
                  "secondary" : (2, 1.5, 1, 0),
                  "booster" : (1.5, 1, 0.5, 0)
                  }

    roll_modifier = {
                      "critical success" : 1.3,
                      "success" : 1.1,
                      "neutral" : 1.0,
                      "failure" : 0.9,
                      "critical failure" : 0.7
                      }

    ## TIP and REP ##

    helper_cost = {
                1 : 5,
                2 : 10,
                3 : 25,
                4 : 50,
                5 : 100
                }

    # max_upkeep = {
    #             1 : 75,
    #             2 : 250,
    #             3 : 500,
    #             4 : 1000,
    #             5 : 2000
    #             }



## XP and RANK ##


    ## LEVEL UP ##

    xp_to_levelup = {0 : 0}

    for i in range(1, 25):

        xp_to_levelup[i] = xp_to_levelup[i-1] + 10 * (i) ** 2

#        if i < 5:
#            xp_to_levelup[i] = xp_to_levelup[i-1] + 5 * (i + 1)

#        elif i < 10:
#            xp_to_levelup[i] = xp_to_levelup[i-1] + 15 * (i + 1)

#        elif i < 15:
#            xp_to_levelup[i] = xp_to_levelup[i-1] + 40 * (i + 1)

#        else:
#            xp_to_levelup[i] = xp_to_levelup[i-1] + 100 * (i + 1)


    ## MC LEVEL UP ##

    MC_xp_to_levelup = {0 : 0}

    for i in range(1, 26):

        MC_xp_to_levelup[i] = MC_xp_to_levelup[i-1] + 10 * i ** 2



    ## RANKS / JOB POINTS ##

    # Rank names #

    rank_name = {
                 1 : "C", #"{color=[c_white]}C{/color}",
                 2 : "B", #"{color=[c_yellow]}B{/color}",
                 3 : "A", #"{color=[c_lightblue]}A{/color}",
                 4 : "S", #"{color=[c_purple]}S{/color}",
                 5 : "X", #"{color=[c_gold]}X{/color}",
                 "waitress0": "Unskilled",
                 "waitress1": "Beginner Waitress",
                 "waitress2": "Competent Waitress",
                 "waitress3": "Skilled Barmaid",
                 "waitress4": "Expert Barmaid",
                 "waitress5": "Tavern Queen",
                 "dancer0": "Unskilled",
                 "dancer1": "Beginner Dancer",
                 "dancer2": "Competent Dancer",
                 "dancer3": "Skilled Stripper",
                 "dancer4": "Expert Stripper",
                 "dancer5": "Poledance Queen",
                 "masseuse0": "Unskilled",
                 "masseuse1": "Beginner Masseuse",
                 "masseuse2": "Competent Masseuse",
                 "masseuse3": "Skilled Massage girl",
                 "masseuse4": "Expert Massage girl",
                 "masseuse5": "Soapy Queen",
                 "geisha0": "Unskilled",
                 "geisha1": "Beginner Maiko",
                 "geisha2": "Competent Maiko",
                 "geisha3": "Skilled Geisha",
                 "geisha4": "Expert Geisha",
                 "geisha5": "Courtesan Queen",
                 "sex0" : "Unskilled",
                 "sex1" : "Beginner Prostitute",
                 "sex2" : "Competent Prostitute",
                 "sex3" : "Skilled Whore",
                 "sex4" : "Expert Whore",
                 "sex5" : "Brothel Queen",
                 "service0" : "Unskilled",
                 "service1" : "Beginner Wanker",
                 "service2" : "Competent Wanker",
                 "service3" : "Skilled Cocksucker",
                 "service4" : "Expert Cocksucker",
                 "service5" : "Blowjob Queen",
                 "anal0" : "Unskilled",
                 "anal1" : "Beginner Anal Slut",
                 "anal2" : "Competent Anal Slut",
                 "anal3" : "Skilled Butt Lover",
                 "anal4" : "Expert Butt Lover",
                 "anal5" : "Anal Queen",
                 "fetish0" : "Unskilled",
                 "fetish1" : "Beginner Servant",
                 "fetish2" : "Competent Servant",
                 "fetish3" : "Skilled Escort",
                 "fetish4" : "Expert Escort",
                 "fetish5" : "Bondage Queen"
                 }


    jp_to_level = {
                   -1 : 0,
                   0 : 50,
                   1 : 125,
                   2 : 250,
                   3 : 425,
                   4 : 650,
                   }

    job_up_dict = {
                   "waitress" : ("charm", "constitution", "beauty", "body"),
                   "dancer" : ("body", "libido", "charm", "refinement"),
                   "masseuse" : ("beauty", "sensitivity", "body", "refinement"),
                   "geisha" : ("refinement", "obedience", "charm", "beauty"),
                   "service" : ("service", "sensitivity", "charm", "fetish"),
                   "sex" : ("sex", "libido", "beauty", "service"),
                   "anal" : ("anal", "constitution", "body", "sex"),
                   "fetish" : ("fetish", "obedience", "refinement", "anal")
                   }

    job_up_change = {
                     1 : (5, 5, 0),
                     2 : (10, 5, 0),
                     3 : (15, 10, 5),
                     4 : (25, 15, 10),
                     5 : (40, 25, 15)
                     }

    rep_to_rank = {
                    0 : 0,
                    1 : 10,
                    2 : 25,
                    3 : 50,
                    4 : 100,
                    5 : 1000
                    }

    rep_gains_dict = { # Read as: For a given girl rank - 'cust.rank relative to girl.rank (e.g: 'higher' = The customer has a higher rank) : must get a result >= X to earn rep'
                     1 : {"higher" : "bad", "same" : "average"},
                     2 : {"higher" : "bad", "same" : "average", "lower" : "good"},
                     3 : {"higher" : "average", "same" : "good", "lower" : "very good"},
                     4 : {"higher" : "average", "same" : "good", "lower" : "very good"},
                     5 : {"same" : "good", "lower" : "perfect"}, # Made easier for now
                     }

    rep_loss_dict = { # Read as: 'must get a result < X to lose rep'. Being < to very bad is actually impossible
                     1 : {"higher" : "very bad", "same" : "bad"},
                     2 : {"higher" : "very bad", "same" : "bad", "lower" : "average"},
                     3 : {"higher" : "bad", "same" : "average", "lower" : "good"},
                     4 : {"higher" : "bad", "same" : "average", "lower" : "good"},
                     5 : {"same" : "average", "lower" : "very good"}, # Made easier for now
                     }

#     rep_gains_dict = {
#                      1 : 6, # average score or better raises reputation
#                      2 : 6, # average score or better raises reputation
#                      3 : 9, # good score or better raises reputation
#                      4 : 9, # good score or better raises reputation
#                      5 : 12 # very good or better score raises reputation
#                      6 : 15 # perfe score raises reputation
#                      }

#     rep_loss_dict = {
#                      1 : -1, # very bad score damages reputation
#                      2 : -1, # very bad score damages reputation
#                      3 : 5, # bad score or lower damages reputation
#                      4 : 5, # bad score or lower damages reputation
#                      5 : 8 # average score or lower damages reputation
#                      }

    rank_cost = {
                    1 : 25,
                    2 : 100,
                    3 : 250,
                    4 : 1000,
                    5 : 2500
                    }

    jp_result_modifier = {
                         "very bad" : -2,
                         "bad" : -1,
                         "average" : 0,
                         "good" : 1,
                         "very good" : 2,
                         "perfect" : 4
                         }

    jp_customer_rank_modifier = {
                                 1 : 1,
                                 2 : 2,
                                 3 : 3,
                                 4 : 4,
                                 5 : 5
                                 }

    jp_job_level_modifier = {# JP are harder to get as girls raise in level
                            0 : 0,
                            1 : -1,
                            2 : -2,
                            3 : -3,
                            4 : -4,
                            5 : -5
                            }



#### TRANSFORMS/EFFECTS ####

init:

    transform blink:
        on start:
            alpha 1.0
            linear 0.5 alpha 0.0
            linear 0.5 alpha 1.0
            pause 2.0
            repeat

    transform myalpha(a):
            alpha a

    transform totheleft:
        xalign 0.2
        yalign 1.0

    transform totheright:
        xalign 0.8
        yalign 1.0

    transform centertextbox:
        xalign 0.5
        yanchor 1.0
        ypos 0.8

    transform centerleft:
        xalign 0.0
        yalign 0.5

    transform centerright:
        xalign 1.0
        yalign 0.5

    transform move_to(start_pos=(0,0), new_pos=(0,0), duration=0.6):

        pos start_pos xanchor 0.5 yanchor 1.0

        ease duration pos new_pos xanchor 0.5

        linear .5 alpha 0.0


    transform ninja_move:

        xanchor 0.0 yanchor 0.5

        xalign 0.75 yalign 0.4

        choice:
            ease 0.33 xalign 0.8 yalign 0.45

        choice:
            ease 0.33 xalign 0.7 yalign 0.45

        choice:
            ease 0.33 xalign 0.8 yalign 0.35

        choice:
            ease 0.33 xalign 0.7 yalign 0.35

        ease 0.33 xalign 0.75 yalign 0.4

        repeat

#     transform quake:
#         linear 0.1 xoffset -2 yoffset 2
#         linear 0.1 xoffset 3 yoffset -3
#         linear 0.1 xoffset 2 yoffset -2
#         linear 0.1 xoffset -3 yoffset 3
#         linear 0.1 xoffset 0 yoffset 0
#         repeat

    $ quake = Move((0, 20), (20, -15), 0.05+renpy.random.random()*.15, bounce=True, repeat=True, delay=1.0)

    $ define.move_transitions("smove", 2.0)

    transform jumping:
        linear 0.1 yoffset -50
        linear 0.1 yoffset 0


    transform fadeinout(y_offset=0):
        xanchor 0.0
        yanchor 0.0
        xpos 1.0
        ypos 0 + y_offset
        alpha 0.0
        ease 2.5 xalign 1.0 alpha 1.0
        pause 2.0
        ease 2.5 xalign 1.5 alpha 0.0

    transform fademove(from_tup, to_tup): # Moves from coordinates from_tup to to_tup while fading

        on show:
            xanchor 0.5
            yanchor 0.5
            xalign from_tup[0]
            yalign from_tup[1]

            pause 1.0

            ease 1.5  xalign to_tup[0] yalign to_tup[1] alpha 0.0

    # Speed
    image speed_effect:
        im.Scale("transitions/speed.jpg", config.screen_width, config.screen_height)
        xpan 180
        xalign 0
        yalign 0
        linear 0.5 xpan -180
        xalign 0
        yalign 0
        repeat

    # Rain
    image rev_lightning = im.Flip("minigame/rain/lightning.png", horizontal=True)

    image rain:
        zoom 2.0

        "minigame/rain/heavyrain1.png"
        0.1
        "minigame/rain/rain1.png"
        0.1
        "minigame/rain/heavyrain2.png"
        0.1
        "minigame/rain/rain3.png"
        0.1
        "minigame/rain/rain2.png"
        0.1
        "minigame/rain/heavyrain3.png"
        0.1
        repeat

    image lightning:
        zoom 3.0
        yalign 0.0
        # choice:        #weight of choice is 1
        #     "rain/lightning.png"
        #     alpha  0.0
        #     1.2                 # show nothing for x seconds

        choice:   #weight of choice is 0.1
            "minigame/rain/lightning.png" with vpunch
            xalign 0.0
            alpha  0.0
            linear 0.6 alpha  1.0
            linear 0.6 alpha  0.0

        choice:
            "rev_lightning" with vpunch
            xalign 1.0
            alpha  0.0
            linear 0.6 alpha  1.0
            linear 0.6 alpha  0.0

        repeat

    image princess fucked: ## There really must be a shorter way to do this, but I've had no luck so far

        "NPC/Misc/princess/princess fucked1.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked2.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked3.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked4.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked5.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked6.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked7.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked8.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked9.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked10.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked11.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked12.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked13.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked14.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked15.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked16.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked17.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked18.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked19.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked20.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked21.gif"
        pause 0.03
        repeat



#### COLORS #### Shortcuts for color codes used in the game

init -5 python:

    c_white = "#FFFFFF"

    c_black = "#000000"

    c_grey = "#ADB9CC"

    c_lightgrey = "#D3D3D3"

    c_steel = "#4682B4"

    c_darkred = "#8B0000"

    c_darkblue = "#00008b"

    c_grey_blue = "#5d5ea0"

    c_darkgrey = "#1A2B47"

    c_hotpink = "#FF69B4"

    c_pink = "#FFC0CB"

    c_orange_pink = "#FF6666"

    c_gold = "#FFD700"

    c_darkgold = "#B8860B"

    c_blue = "#0000FF"

    c_lightblue = "#2B60DE"

    c_copper = "#CC3300"

    c_red = "#FF0000"

    c_lightred = "#F78181"

    c_redpink = "#cc0052"

    c_yellow = "#FFFF33"

    c_blonde = "#FCF3CF"

    c_cream = "#FDF1B8"

    c_brown = "#502F13"

    c_lightbrown = "#D2B48C"

    c_darkbrown = "#502F13"

    c_lightprune = "#a51a6a"

    c_prune = "#811453"

    c_magenta = "#A41CC6"

    c_lightmagenta = "#FF33FF"

    c_purple = "#9933FF"

    c_softpurple = "#9683EC"

    c_darkpurple = "#3D007A"

    c_orange = "#FF9900" # #FD9B1C

    c_lightorange = "#FFCC66"

    c_darkorange = "#D67229"

    c_emerald = "#009874"

    c_lightgreen = "#66FF99"

    c_darkgreen = "#003333"

    c_green = "#00B050"

    c_turquoise = "#30DADD"

    c_sapphire = "#0F52BA"

    c_azure = "#B7DBFF"

    c_crimson = "#DC143C"

    c_firered = "#B22222"

    c_violet = "#C71585"

    c_ui_unlocked = c_orange

    c_ui_sensitive = c_white

    c_ui_insensitive = c_lightgrey

    c_ui_dark = "#00000066" # "#000000CC" "#22222288"

    c_ui_darker = "#000000CC"

    c_ui_darkblue = "#000022AA"

    c_ui_brown = "#D2B48CCC"

    c_ui_light = "#FFECBFDD"

## COLOR DICTIONARY

    color_dict = {
                  "+++" : c_emerald,
                  "++" : c_green,
                  "+" : c_lightgreen,

                  "=" : c_white,

                  "---" : c_crimson,
                  "--" : c_red,
                  "-" : c_lightred,

                  "love +++" : c_hotpink,
                  "love ++" : c_hotpink,
                  "love +" : c_hotpink,
                  "love -" : c_red,

                  "fear +++" : c_softpurple,
                  "fear ++" : c_softpurple,
                  "fear +" : c_softpurple,
                  "fear -" : "#A6DEEE",

                  "special" : c_orange,
                  "average" : c_yellow,
                  "leveling" : c_steel,
                  "normal" : c_white,
                  }



## MODS ##

    detected_mods = {}

    if persistent.mods is None:
        persistent.mods = {}

    mod_traceback = ""
    updated_games = defaultdict(bool)


init -2 python:
    contract_level = {2 : [1], 3 : [1, 2], 4 : [2], 5 : [2, 3], 6 : [3, 4], 7 : [4]} # Picks randomized task number according to chapter
    contract_value = {2 : 250, 3 : 500, 4 : 625, 5 : 1000, 6 : 1250, 7 : 1600} # Base value for contract rewards. Min-Max payout is 2-4 times base value for each successful task (not taking Special bonuses into account)

    contract_skill_limit = {2 : {"easy" : 75, "hard" : 100}, 3 : {"easy" : 100, "hard" : 125}, 4 : {"easy" : 125, "hard" : 150},
                            5 : {"easy" : 150, "hard" : 175}, 6 : {"easy" : 175, "hard" : 225}, 7 : {"easy" : 225, "hard" : 275}}
    contract_sex_limit =   {
                            2: {"easy": "a little reluctant", "hard": "indifferent"},
                            3: {"easy": "indifferent", "hard": "a little interested"},
                            4: {"easy": "a little interested", "hard": "interested"},
                            5: {"easy": "interested", "hard": "very interested"},
                            6: {"easy": "very interested", "hard": "fascinated"},
                            7: {"easy": "very interested", "hard": "fascinated"},
                            }

    # ORG/org = Organizer, VEN/ven = venue, AVEN/aven = article + venue, LOC/loc = location, DIS/dis = district

    contract_description = {"cruise" : ":ORG: is organizing a nightly cruise tour of :dis: to thank its members for their hard work this year. :AVEN: will depart for a sightseeing tour of the bay at dusk, then moor next to the :LOC: for a night of entertainment.",
                            "party" : ":ORG: is throwing a lavish party in :aven: near the :LOC:. Everyone who is anyone in Zan is expected to attend and party until well after dawn.",
                            "ceremony" : ":ORG: chose :aven: near the :LOC: to celebrate one of their numerous holy days. In order to get closer to their deity, worshippers are expected to transcend both spirit and flesh by indulging in the most shameful pleasures, washing away their sins with large amounts of holy alcohol, conveniently sold on the premises by the Church.",
                            "festival" : ":ORG: is throwing a huge festival next month in :dis:, to celebrate a new season, a three-headed cow, the sun rising again, or some other redneck nonsense. Still, there will be a big feast at :aven: near the :LOC: complete with food, drinks, shows and of course, girls!",
                            "date" : ":ORG: has invited a few friends to :aven: next to the :LOC: for the night, and has requested some company. Well-groomed, well-behaved female servants are expected to tend to his every need.",
                            "meeting" : ":ORG: convened a meeting of like-minded nobles and diplomats to discuss :ven: in a discreet venue near the :LOC:. While the intricacies of this grave topic will occupy much of their time, they will also expect their hosts to provide top-notch service and ways of 'relieving' the tension.",
                            "magic" : ":ORG: summoned all arcane users to a night of fun and magic out in the :LOC:. Tended to by beautiful women, the guests will attend special events in :aven:, overlooking the magnificence of :DIS:.",
                            "orgy" : ":ORG: is happy to announce a long night of hedonism and erotic surprises in the :LOC:. Gathered in :aven:, the guests will enjoy forbidden pleasure with like-minded individuals and a hand-picked selection of elite sex slaves."}

init python:

    contract_templates = [Contract(type="cruise", district="The Docks", archetypes = ["The Player", "The Fox"],
                                   names=["A Night At Sea", "Touring Zan's Bay", "The Retired Sailor", "A Fancy Cruise"],
                                   organizers=["the rowdy sailor fraternity", "Zan's navy", "the flibusteer social club", "the Northern merchant navy"],
                                   venues=["refitted galleon", "private junk", "princely yacht", "fleet of small fishing boats", "large tour boat"],
                                   character=sailor,
                                   MC_event_pic="events/brawl3.jpg",
                                  ),
                          Contract(type="party", district="The Cathedra", archetypes = ["The Maid", "The Slut"],
                                   names=["Party Hard", "All-Nighter by The Cathedra", "Shameless Party", "From Dusk Till Dawn", "Blackjack Tables, and Hookers", "Dude, Where's My Cart?"],
                                   organizers=["a foreign dignitary", "a wealthy patrician family", "an interguild association", "a visiting High Mage of Karkyr", "a close advisor of the king", "a wealthy brothel master", "the House of Lannister"],
                                   venues=["abandonned church", "famous okiya", "fancy palace", "seedy tavern", "underground casino"],
                                   character=party_girl,
                                   MC_event_pic="events/violent2.jpg",
                                  ),
                          Contract(type="ceremony", district="The Cathedra", archetypes = ["The Model", "The Bride"],
                                   names=["A Holy Affair", "A Religious Festival", "The Saintly Ceremony", "A Most Holy Gathering", "After The Prayer"],
                                   organizers=["The Holy Church of Arios", "The Nuns of Saint Dil d'Oh", "The Enlightened Brothers", "The Pious Fraternity", "The Friends of Shalia", "The Ol' Gods Alliance", "The Worshippers of the Unspeakable Yog'Gluglu", "The Priestesses of Arios"],
                                   venues=["large convent", "venerable cathedral", "isolated monastery", "quiet retreat", "forgotten temple", "glorious church", "destitute orphanage"],
                                   character=nun,
                                   MC_event_pic="events/monster assault.jpg",
                                  ),
                          Contract(type="festival", district="The Slums", archetypes = ["The Player", "The Fox"],
                                   names=["The Moonlight Festival", "A Country Festival", "Season's Greetings", "The Countryside Fair", "The Farmers Market", "A Prized Tradition"],
                                   organizers=["The Bumpkin Pumpkins", "The Farmers Guild", "Zan's Country Club", "The Gardening Brotherhood", "The Landlords Cooperative", "Dirty hippies from the Valley", "The Union of Goat-Herders"],
                                   venues=["former junkyard", "large plaza", "market square", "city gate", "main roadside"],
                                   character=kimono_lady,
                                   MC_event_pic="default/farm/sex beast (7).jpg",
                                  ),
                          Contract(type="date", district="The Magic Gardens", archetypes = ["The Bride", "The Model"],
                                   names=["A Romantic Date", "The Lonely Gentleman", "The Lord's Penthouse", "Pretty Woman"],
                                   organizers=["Calif Bretznah", "High Priest Ronan", "Lord Nabukov", "Master Rhi-Seung", "Count Dicku", "The Pink Baron", "Duke Nukem", "Guild Master Felix"],
                                   character=young_maid,
                                   venues=["luxurious penthouse", "big country house", "old mansion", "family palace", "private temple", "popular resort"],
                                   MC_event_pic="NPC/encounters/thief4.jpg",
                                  ),
                          Contract(type="meeting", district="The Warehouse", archetypes = ["The Courtesan", "The Maid"],
                                   names=["A Strategic Meeting", "A Show of Power", "A Political Reunion", "A Momentous Occasion", "A Pompous Conference"],
                                   organizers=["The Zanic City Council", "The Rebel Alliance", "The government of His Majesty's King Pharo the 1st", "The Knights of the Oddly-Shaped Table", "The Blood-Island Coalition"],
                                   venues=["progress in the Holy War", "military cooperation", "freer sex slave trading", "new fishery regulations", "limits on magic weapon stockpiles", "lowering taxes for the noble-born", "raising taxes on the poor and destitute"], # Different use for venue for this particular contract
                                   character=diplomat,
                                   MC_event_pic="NPC/encounters/thief2.jpg", #impress1_5.jpg / quests/sex9.png
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
                                   MC_event_pic="NPC/encounters/ev_onsens2.jpg",
                                  ),
                                  ]

    contract_task_types_order = {"greet" : 1, "serve" : 2, "mingle" : 3, "event" : 4, "private show" : 5, "fun" : 6}
    contract_task_types_description = {"greet" : "Greet Guests", "serve" : "Serve Guests", "mingle" : "Socialize", "event" : "Participate In An Event", "private show" : "Deliver A Private Show", "fun" : "Have 'Fun'"}

    contract_tasks = [
                        ContractTask("clean", type="serve", requirements=["job waitress", "skill obedience", "skill constitution", ], tags=(["maid"], ["obedience"], ["waitress"], ["profile"])),
                        ContractTask("serve guests", type="serve", requirements=["job waitress", "skill beauty", "skill charm", "skill obedience", ], tags=(["waitress"], ["profile"])),
                        ContractTask("serve drinks", type="serve", requirements=["job waitress", "skill beauty", "skill charm", "skill constitution", ], tags=(["waitress"], ["profile"])),
                        ContractTask("feed guests", type="serve", requirements=["job waitress", "job geisha", "skill charm", "skill obedience", ], tags=(["waitress", "geisha"], ["profile"])),
                        ContractTask("onsen", type="mingle", requirements=["job masseuse", "skill beauty", "skill body", "skill charm", "skill obedience", "skill constitution", ], tags=(["masseuse"], ["swim"], ["profile"])),
                        ContractTask("swimming pool", type="mingle", requirements=["job masseuse", "skill beauty", "skill body", "skill charm", ], tags=(["swim"], ["masseuse"], ["profile"])),
                        ContractTask("swimming show", type="event", requirements=["job masseuse", "skill beauty", "skill body", "skill constitution", ], tags=(["swim"], ["profile"]), and_tags=["rest"]),
                        ContractTask("lingerie show", type="event", requirements=["job dancer", "skill body", "skill refinement", "skill libido", ], tags=(["profile"]), and_tags=["libido"]),
                        ContractTask("entice guests", type="greet", requirements=["job dancer", "skill beauty", "skill charm", "skill refinement", "skill libido", ], tags=(["model"], ["profile"]), and_tags=["libido"]),
                        ContractTask("dance show", type="private show", requirements=["job dancer", "skill body", "skill refinement", "skill constitution", ], tags=(["dance"], ["profile"])),
                        ContractTask("erotic show", type="private show", requirements=["job dancer", "skill body", "skill libido", "skill constitution", ], tags=(["dance"], ["profile"]), and_tags=["libido"]),
                        ContractTask("cosplay", type="mingle", requirements=["job waitress", "job dancer", "skill charm", "skill libido", ], tags=(["cosplay"], ["dance"], ["profile"])),
                        ContractTask("lap dance", type="private show", requirements=["job dancer", "skill body", "skill obedience", "skill libido", ], tags=(["dance"], ["profile"]), and_tags=["libido"]),
                        ContractTask("welcome massage", type="greet", requirements=["job masseuse", "skill beauty", "skill charm", ], tags=(["masseuse"], ["profile"])),
                        ContractTask("erotic massage", type="serve", requirements=["job masseuse", "skill beauty", "skill charm", "skill libido", ], tags=(["masseuse"], ["profile"]), and_tags=["libido"]),
                        ContractTask("conversation", type="mingle", requirements=["job geisha", "skill beauty", "skill charm", "skill refinement", ], tags=(["geisha"], ["profile"])),
                        ContractTask("protocol", type="greet", requirements=["job geisha", "skill charm", "skill refinement", "skill obedience", ], tags=(["geisha"], ["profile"])),
                        ContractTask("ceremony", type="mingle", requirements=["job geisha", "skill beauty", "skill refinement", ], tags=(["geisha"], ["profile"])),
                        ContractTask("welcome guests", type="greet", requirements=["job geisha", "skill charm", "skill obedience", ], tags=(["geisha"], ["profile"])),
                        ContractTask("kiss guests", type="greet", requirements=["skill beauty", "skill refinement", "skill libido", ], tags=(["kiss"], ["profile"])),
                        ContractTask("catwalk", type="event", requirements=["skill beauty", "skill refinement", ], tags=(["model"], ["dance"], ["profile"])),
                        ContractTask("catfight", type="event", requirements=["skill body", "skill constitution", ], tags=(["fight"], ["dance"], ["profile"])),
                        ContractTask("art model", type="mingle", requirements=["skill beauty", "skill refinement", "skill obedience", ], tags=(["model"], ["profile"])),
                        ContractTask("sub greeting", type="greet", requirements=["skill refinement", "skill obedience", ], tags=(["sub"], ["profile"])),
                        ContractTask("dom greeting", type="greet", requirements=["skill refinement", "skill libido", "skill constitution", ], tags=(["dom"], ["profile"])),
                        ContractTask("sports show", type="event", requirements=["skill body", "skill constitution", ], tags=(["constitution"], ["profile"])),
                        ContractTask("fondle", type="mingle", requirements=["job masseuse", "skill body", "skill charm", "skill libido", ], tags=(["fondle", "grope"], ["profile"])),
                        ContractTask("strip", type="private show", requirements=["skill beauty", "skill body", "skill refinement", "skill libido", ], tags=(["strip"], ["naked"]), soft="naked"),
                        ContractTask("nude help", type="mingle", requirements=["skill body", "skill charm", "skill obedience", ], tags=(["waitress"], ["geisha"], ["profile"]), and_tags=["naked"], soft="naked"),
                        ContractTask("naked", type="fun", requirements=["skill body", "skill libido", ], tags=(["naked"]), and_tags2 = ["cum shower"], soft="naked"),
                        ContractTask("masturbate", type="private show", requirements=["job service", "skill constitution", "skill service", "pref service", ], tags=(["service"], ["naked"]), and_tags=["mast"], soft=False),
                        ContractTask("barmaid blowjob", type="serve", requirements=["job waitress", "job service", "skill charm", "skill service", "pref service", ], tags=(["waitress"], ["service"], ["naked"]), and_tags=["service"], soft=False),
                        ContractTask("service", type="fun", requirements=["job service", "skill service", "pref service", ], tags=(["service"], ["naked"]), and_tags2 = ["cim"], soft=False),
                        ContractTask("cosplay sex", type="event", requirements=["job sex", "skill libido", "skill sex", "pref sex", ], tags=(["cosplay"], ["sex"], ["naked"]), and_tags=["sex"], soft=False),
                        ContractTask("full service massage", type="serve", requirements=["job masseuse", "job sex", "skill beauty", "skill sex", "pref sex", ], tags=(["masseuse"], ["sex"], ["naked"]), and_tags=["sex"], soft=False),
                        ContractTask("sex", type="fun", requirements=["job sex", "skill libido", "skill sex", "pref sex", ], tags=(["sex"], ["naked"]), and_tags2 = ["creampie"], soft=False),
                        ContractTask("cosplay anal", type="event", requirements=["job anal", "skill obedience", "skill constitution", "skill anal", "pref anal", ], tags=(["cosplay"], ["anal"], ["naked"]), and_tags=["anal"], soft=False),
                        ContractTask("anal dance", type="private show", requirements=["job dancer", "job anal", "skill constitution", "skill anal", "pref anal", ], tags=(["dancer"], ["anal"], ["naked"]), and_tags=["anal"], soft=False),
                        ContractTask("anal", type="fun", requirements=["job anal", "skill constitution", "skill anal", "pref anal", ], tags=(["anal"], ["naked"]), and_tags2 = ["cob"], soft=False),
                        ContractTask("toy", type="private show", requirements=["job fetish", "skill obedience", "skill fetish", "pref fetish", ], tags=(["fetish"], ["naked"]), and_tags=["toy"], soft=False),
                        ContractTask("geisha bondage", type="event", requirements=["job geisha", "job fetish", "skill refinement", "skill fetish", "pref fetish", ], tags=(["geisha"], ["fetish"], ["naked"]), and_tags=["fetish"], soft=False),
                        ContractTask("fetish", type="fun", requirements=["job fetish", "skill obedience", "skill fetish", "pref fetish", ], tags=(["fetish"], ["naked"]), and_tags2 = ["cof"], soft=False),
                        ContractTask("group sex", type="fun", requirements=["job sex", "skill libido", "skill sex", "pref sex", ], tags=(["sex"], ["group"], ["naked"]), and_tags=["group"], and_tags2 = ["group", "bukkake"], soft=False),
                        ContractTask("group anal", type="fun", requirements=["job anal", "skill constitution", "skill anal", "pref anal", ], tags=(["anal"], ["group"], ["naked"]), and_tags=["group"], and_tags2 = ["group", "cum shower"], soft=False),
                        ContractTask("bisexual service", type="fun", requirements=["job service", "skill service", "pref service", ], tags=(["service"], ["bisexual"], ["naked"]), and_tags=["bisexual"], and_tags2=["bisexual", "orgasm"], soft=False),
                        ContractTask("bisexual fetish", type="fun", requirements=["job fetish", "skill obedience", "skill fetish", "pref fetish", ], tags=(["fetish"], ["bisexual"], ["naked"]), and_tags=["bisexual"], and_tags2=["bisexual", "squirt"], soft=False),
]

    contract_specials = [("trait", 3), ("perk", 2), ("fix", 3), ("farm", 1), ("item", 1)]

    contract_stage_modifier = {1 : 1, 2 : 1.5, 3 : 3, 4 : 6}

init -1 python:
    init_galleries()

## END OF BK INIT VARIABLES FILE ##
