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
                         "gold" : "影响青楼的{b}收入{/b}. ",
                         "rewards" : "影响{b}任务、等级和合约{/b}的奖励. ",
                         "resources" : "影响收集和交易中获得的{b}资源{/b}的数量. ",
                         "stats" : "影响女孩的{b}技能{/b}的进展. ",
                         "pref" : "影响女孩的{b}性偏好{/b}的进展. ",
                         "xp" : "影响女孩的{b}经验{/b}的进展. ",
                         "jp" : "影响女孩的{b}职业经验{/b}的进展. ",
                         "rep" : "影响女孩的{b}声望{/b}的进展. ",
                         "prestige" : "影响主角{b}声望{/b}的进展. ",
                         "tax rate" : "增加或减少奴隶公会的{b}费用{/b}. ",
                         "satisfaction" : "改变客户{b}满意度{/b}奖金. ",
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
                    "漂亮的女孩是最好的按摩师. ",
                    "按摩师应该具有{b}美貌{/b}与{b}敏感{/b}. 当然{b}身材{/b}与{b}优雅{/b}也很重要. ",
                    "一个身材好的女孩能成为一个伟大的舞蹈家. ",
                    "舞娘应该具有{b}身材{/b}和{b}性欲{/b}.  当然{b}优雅{/b}和{b}魅力{/b}也很重要. ",
                    "迷人的女孩当服务员会更好. ",
                    "服务员需要{b}魅力{/b}和{b}体格{/b}.  如果是具有较高的{b}美貌{/b}，并且有一个不俗的{b}身材{/b}也不错. ",
                    "艺妓应该是有教养的女孩，才能达到最好的效果. ",
                    "艺妓应该是{b}优雅{/b}和{b}服从{/b}.  {b}美貌{/b}和{b}魅力{/b}也有助于成为一个完美的艺妓. ",
                    "高级别的顾客很难满足，但他们给的小费会更多. ",
                    "别忘了付青楼的安保费用.  否则会发生不好的事情. ",
                    "每次女孩服务顾客后青楼就会变脏.  你应该要及时进行打扫，否则你最终会花费更多的钱. ",
                    "如果你想招揽更多的顾客，可以尝试一下广告女郎.  不过宣传不要超出你的能力范围，不满意的顾客会降低你青楼的声誉. ",
                    "不听话的女孩不太可能接受工作或培训. ",
                    "性欲高的女孩更有可能同意和享受特殊服务，也可以为多个客户服务. ",
                    "敏感的女孩善于让顾客开心，不管行为如何. ",
                    "体质决定了一个女孩有多少精力，以及她能服务多少顾客. ",
                    "魅力和敏感性使你的女孩在手交、口交和其他服务性行为方面做的更好. ",
                    "当然，执行性服务需要良好的{b}性服务{/b}技能以及{b}敏感度{/b}.  {b}魅力{/b}和{b}皮绳愉虐{/b}技能也有帮助. ",
                    "美貌和性欲对于正常的性行为很重要. ",
                    "对于正常的性行为来说，{b}性交{/b}和{b}性欲{/b}技能越高越好.  {b}美容{/b}和{b}服务{/b}也有帮助. ",
                    "身材和体质好的女孩可以很好地运用肛交. ",
                    "肛交需要较高的{b}肛交{/b}技巧和良好的{b}体质{/b}.  {b}身体{/b}和{b}性交{/b}技能也有帮助. ",
                    "优雅和服从对恋物性行为是有好处的. ",
                    "一个女孩需要一个良好的{b}恋物{/b}和{b}服从{/b}的恋物性行为技能.  {b}优雅{/b}和{b}肛门{/b}技能也有帮助. ",
                    "青楼报告中有很多关于青楼的有用信息.  如果你想了解某个女孩的信息，可以在女孩标签中查看她的统计数据. ",
                    "工作时，女孩可以同时获得XP和JP.  XP允许一个女孩提高他们的统计数据和获得额外津贴，JP允许一个女孩在特定的工作或性行为中变得更好",
                    "顾客的口味在他们喜欢的娱乐和性行为上是不同的.  多样化是让所有顾客满意的关键. ",
                    "每一个满意的客人都会增加青楼的名声.  但不满意的客人会诋毁你的青楼和你的女孩，所以要小心. ",
                    "总的来说，顾客的满意来自两个因素:他们所得到的娱乐的服务质量，和你家女孩的品质. ",
                    "女孩可能会变成双性恋，允许同一个顾客提供双飞服务. ",
                    "女孩可以学习如何进行群交，允许她们同时服务两到三个顾客. ",
                    "双飞和群交总是容易让顾客满意的. ",
                    "保养对你的女孩来说很重要.  虽然心情好的女孩可能会暂时不计较，但如果她的保养费长期过低，她的情绪就会急剧下降. ",
                    "虽然你的安全措施可以解决大多数问题，但是如果一个疯狂的顾客直接针对她们，你的女孩们最好好还是能有一些个人防卫措施.  不过要小心，你给她们任何武器都可能被用来对付你...",
                    "训练女孩房中术的最有效方法就是亲自上阵，但这很费时.  也许你可以找个人来帮你训练他们?",
                    "你遇到的一些人可以成为你女孩的教练.  一定要选一个最适合你管理风格的人. ",
                    "在Zan中，善与恶的名声会产生很大的不同.  每一件好事或坏事都有后果.  当然，并非一切都是黑白分明的.  有些人喜欢在两者之间保持平衡...",
                    "我听说这个城市的各个地区都有道德败坏的女孩子.  你不会碰巧知道那件事吧?",
                    "商店里的那个女孩总是装模作样的卖弄风情......说实话我不喜欢她.  我希望我们能在城里找到别的地方购物. ",
                    "你可以买到在奴隶市场受过训练的女孩.  这可以节省你的时间，尽管你永远不能百分百确定她们接受的训练质量. ",
                    "通过和你的女孩的交谈，你可以了解她们，她们甚至可以告诉你她们的个人故事. ",
                    "如果你善待她们，譬如让她们做自己喜欢的事，她们会更加容易爱上你. ",
                    "如果你对她们太严厉，她们会害怕你，最好也不要强迫她们做不想做的事. ",
                    "当所有所有的努力都失败时，你可以教训你的女孩以便她们能够接受训练.  此事唯一有用的就是你的魅力了. ",
                    "你的力量决定了你在战斗中有多出色，或者决定了你在完成各种体能活动时有多出色. ",
                    "你的精神决定了你在使用、探测和抵抗魔法方面的能力. ",
                    "魅力对于所有的互动都很重要，无论是和你的女孩还是在外面的世界. ",
                    "你的速度决定了你每天可以采取多少行动.  它很少用于其他用途. ",
                    "不快乐的女孩可能会逃离你.  如果你雇不起赏金猎人，你最后的机会就是自己去探索这座城市. ",
                    "别忘了升级青楼的卧室.  如果卧室质量低于标准，女孩和顾客的心情都会变糟，尤其是在提升了青楼等级之后. ",
                    "普通房间只能接待有限数量的顾客.  确保你有足够的空间招待每个人. ",
                    "当一个女孩加入你的青楼时，你必须为她事先准备一个房间.  否则，您可能要等到扩建后才能接收她. ",
                    "有些人在城里到处卖稀奇古怪的东西，甚至是怪物或动物.  我不知道你需要它们做什么. ",
                    "房中术(性技能)不能通过升级来提高.  唯一的途径就是用实战经验来提升它们. ",
                    "课程有助于更快地提高女孩的低级技能. ",
                    "每个女孩都有自己的声望，与你的青楼声望不同.  声望是一个女孩晋升阶级的关键. ",
                    "提高女孩声望的最好方法是让她在外派任务中取得成功. ",
                    "性奴隶获得来自奴隶工会的阶级评级.  阶级决定很多东西，包括最高等级和最高技能. ",
                    "在阶级最低时，女孩的技能限制在50.  每增加一级，技能上限提高50点. ",
                    "当一个女孩升级时，她会根据她当前的等级获得技能点.  而且，她每升两级就会获得额外奖励. ",
                    "每升5级，就会有一个女孩获得额外的奖励点. ",
                    "无论如何，一位女孩的等级不可能超过25级. ",
                    "我听说过在奴隶公会里关于一个神秘阶级的谣言，它的评价甚至高于'S'. ",
                    "求你了，主人，千万不要让你的账户变成负数!我听说有些人会在你欠债的时候用一些见不得人的交易来引诱你，但那只会给你带来更多的麻烦. ",
                    "永远不要相信精灵.  别跟我说我没警告过你. ",
                    "在更高级别的职位上，融入新的女孩获得工作上的认可可能会很困难. 确保使用课程、物品、装扮和其他奖励来帮助新来的女孩迅速获得成功. ",
                    "当你觉得你已经看过了所有的事件，你可以在游戏选项菜单中禁用一些夜间事件的展示. ",
                    "不喜欢随机命名生成?您可以在游戏选项菜单中禁用它. ",
                    "不想看到那些非常硬核的性的行为?在游戏选项菜单中禁用它们. ",
                    "点击“Ctrl”可以跳过夜间事件或任何你已经看过的对话. ",
                    "右键点击会让你后退一步.  右键单击主菜单将显示常规设置菜单. ",
                    "在白天任何时候都可以用“H”键回到主屏幕. ",
                    "按“E”键结束白天的工作，继续晚上的事件. ",
                    "法术可以自动施法，使用你在一天结束时剩下的所有动作力. ",
                    "按下“Esc”或“O”键将显示选项菜单",
                    "您可以使用“L”键返回最近访问的位置. ",
                    "每当你或你的女孩发生性行为时，你就会获得个人声望.  声望会让你自己提升等级. ",
                    "你的被动技能不会超过10个，但物品和魔法效果不受此限. ",
                    "处女在失贞后会得到一种新的特质，这取决于发生这种特质的条件. ",
                    "如果你的女孩心情不好，你一定要给她们足够的薪水，让她们的住宿足够舒适. "
                    "广告增加了每个客户的最大金额.  确保他们带个鼓鼓的钱包!",
                    "课程可能可以让女孩的技能超过她们的平均水平.  如果你有钱买的话很方便. ",
                    "一段时间后，有经验的女孩很难提高更高的技能.  课程可以帮助你解决这个问题. ",
                    "虽然工作和性行为依赖于几项主要技能，但拥有其他高技能通常可以稍微提升女孩的业绩. ",
                    "即使识别一个裸体女孩应该很容易，但人们永远无法就'裸体'是什么达成一致! 你相信吗?",
                    "公开行为会令人困惑.  她是公开的，因为它在外面，还是因为其他人可以看到你? 我永远说不出来. ",
                    "您可以使用 F5 快速保存并使用 F9 快速加载(当快捷键处于活动状态时).  这是什么意思? 我不知道!",
                ]


    ## MC ##

    all_MC_stats = ["strength", "spirit", "charisma", "speed"]

    MC_playerclass_description = {
                                  "Warrior" : "你是个战士. 你可能还年轻，但你经历过的血战不止这些. 你在战斗和保护青楼中更强大.",
                                  "Wizard" : "你是个巫师. 人们臣服于你的意志和魔法. 你可以使用最多的法术.",
                                  "Trader" : "你是个奸商. 你从年轻时混迹江湖开始就一直在努力. 你可以做更好的交易，拿到最好的价格."
                                  }
    MC_stat_description = {
                            "strength" : "这是你角色的当前力量.  提高安全性并有助于个人战斗.",
                            "spirit" : "这是你角色的魔法强度. 精神是你法力的来源，并在事件中提高法术效果.",
                            "charisma" : "这涵盖了你的角色个性，外表和演讲技巧.  在交互过程中改善结果.",
                            "speed" : "这是你角色的精力水平.  增加您可以执行的操作数量."
                            }

    god_description = {
                        "Arios" : "你崇拜阿里奥斯，光明之神和天使之主.",
                        "Shalia" : "你崇拜莎莉娅，阴影女神和夜晚的统治者.",
                        None : "你们不敬拜神，倒喜爱自然界的奇事."
                        }

    alignment_description = {
                            "good" : "你的行为表明你是个好人. 与你的女孩之间基于爱的互动比基于恐惧的互动更成功.",
                            "evil" : "你是个邪恶的人，沉溺于自己的残忍. 与女孩之间基于恐惧的互动比基于爱情的互动更成功.",
                            "neutral" : "你是中立的，宁愿在自己的利益和他人的利益之间保持平衡. 基于爱和恐惧的互动同样成功."
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
                    "rank" : ["阶级", "rank", "奴隶的阶级"],
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
                1 : Room("基本房间", 1),
                2 : Room("+基本房间+", 2),
                3 : Room("*基本房间*", 3),
                4 : Room("标准房间", 4),
                5 : Room("+标准房间+", 5),
                6 : Room("*标准房间*", 6),
                7 : Room("高级房间", 7),
                8 : Room("+高级房间+", 8),
                9 : Room("*高级房间*", 9),
                10 : Room("贵族套房", 10),
                11 : Room("+皇家套房+", 11),
                12 : Room("*御庭套房*", 12)
                }

    common_room_dict = {
                        "tavern" : Room("酒馆", 0, "special", job = "waitress"),
                        "club" : Room("俱乐部", 0, "special", job = "dancer"),
                        "onsen" : Room("温泉", 0, "special", job = "masseuse"),
                        "okiya" : Room("置屋", 0, "special", job = "geisha"),
                        }

    master_bedrooms = {
                        0 : Room("单人房间", level=0, type="master", cost=0),
                        1 : Room("双人房间", level=1, type="master", cost=750),
                        2 : Room("小型套间", level=2, type="master", cost=2500),
                        3 : Room("豪华套间", level=3, type="master", cost=7500),
                        4 : Room("皇家套间", level=4, type="master", cost=25000),
                        5 : Room("王室后宫", level=5, type="master", cost=75000),
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
                         "beast" : "野兽是Gizel在农场里养的各种各样的动物. 更像是动物园，真的. ",
                         "monster" : "怪物是不自然的恶魔，在克塞洛斯最黑暗的洞穴里爬行. 它们有很多种形式，但有触角的总是最受欢迎. ",
                         "machine" : "在Gizel的工作室里，机器或人工制品总是拥有众多用途，但实际上它们似乎只是为一件事而设计——性. "
                         }

    all_minion_types = ["stallion", "beast", "monster", "machine"]

    farm_pics = {"stallion" : [],
                 "beast" : [],
                 "monster" : [],
                 "machine" : []
                 }

    farm_holding_dict = {"libido" : "照看奴仆{size=-6}(+性欲){/size}",
                            "sensitivity" : "服侍Gizel{size=-6}(+敏感){/size}",
                            "obedience" : "打扫农场{size=-6}(+服从){/size}",
                            "constitution" : "外出工作{size=-6}(+体格){/size}",
                            "rest": "休息",
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
                        "stallion bad" : " %s被种马的大阴茎吓了一跳，她害怕地往后退缩. {color=[c_red]}她的训练进行得不顺利.{/color}",
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
                        "pen obedience": "%s回想起把她带到农场的不幸境遇和种种恶行. 她觉得当时如果听话点，也许就不会惹麻烦了. {/color}",
                        "pen constitution": "即使她被锁在家里，%s也决心保持健康. {color=[c_green]}她做了一些腹肌锻炼和俯卧撑，变得更健康了.{/color}",
                        "pen sensitivity": "%s感到无聊，开始思考农场里那些奇怪的生物，以及它们更“不寻常”的特征.  {color=[c_green]}不久，她的脸就红了，而且莫名其妙地兴奋起来.{/color}",
                        "pen libido": "%s感到无聊和饥渴，所以她决定在农场听着那些奇怪的声音自慰一会儿. {color=[c_green]}她很享受这些.{/color}",
                        "holding obedience" : "Gizel派%s去打扫农场，告诉她要擦洗谷仓的每一个角落，清洗地板上的污渍. %s按照她的要求做了，而不是去面对魔法鞭笞的威胁.",
                        "holding constitution" : "Gizel命令%s在马道上绕着农行跑了一圈，每当她发现%s减速时，就狠狠地用鞭子抽她.",
                        "holding sensitivity" : "Gizel用%s作为她的私人仆人来追求她变态的幻想，强迫她舔身体，用各种各样的玩具玩弄那些饥饿的洞洞. 这很困难，但%s还是学到了新东西.",
                        "holding libido" : "Gizel要求%s照顾奴仆：喂养它们，清洁它们，帮助它们“释放压力”. %s在她工作的过程中，她了解到很多关于奴仆们独特的体征特点.",
                        "holding obedience good": "作为一个额外的挑战，Gizel让%s在她持续工作的时候穿上紧缚身体的绳子.  {color=[c_green]}粗糙的绳子以一种既不舒服又奇怪的方式摩擦着她的身体.{/color}",
                        "holding obedience bad": " {color=[c_lightred]}%s厌恶Gizel的奴仆留下的所有污秽和体液.{/color}",
                        "holding constitution good": " Gizel认为在室外不穿衣服会让%s更加狂野，于是她让她光着身子跟动物一起跑. {color=[c_green]}在户外和动物一起裸体让她觉得自己的身心更愉悦.{/color}",
                        "holding constitution bad": " {color=[c_lightred]}当%s以创纪录的速度跑完一圈时，她轻蔑地看了Gizel一眼.{/color}",
                        "holding sensitivity good": " %s用熟练的舌头舔着Gizel勃起的阴蒂，给了她美妙的高潮. {color=[c_green]}她现在更熟悉如何取悦女人.{/color}",
                        "holding sensitivity bad": " Gizel把%s弄得筋疲力尽，气喘吁吁地倒在地上. {color=[c_lightred]}她的体格受到了影响.{/color}",
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
                          "Stella greeting" : "呦！看谁来了。我希望你不要浪费我的时间。",
                          "Stella bought something" : "赶紧的，把金币给我，现在它就是你的了。你可以走了，除非你还准备要买别的东西。{w=2.0}{nw}",
                          "Stella no money" : "你钱不够吧，伙计，没钱赶紧离开这里。",

                          "Goldie greeting" : "有什么我可以帮到你的吗？",
                          "Goldie bought something" : "谢谢！小心轻放。{w=2.0}{nw}",
                          "Goldie no money" : "抱歉，你好像没有钱了。",

                          "Willow greeting" : "嘿，如果它不是我的友好邻居!你会惊奇地看到我刚刚抓到的东西.",
                          "Willow bought something" : "成交，就这样…你会玩得很开心的!{w=2.0}{nw}",
                          "Willow no money" : "哇, 这个小气鬼，想占我的便宜吗?你的袋子空了!",

                          "Gina greeting" : "Mmh, 如果我调整这个按钮…不，不是这样的……对不起. 我能帮你什么忙吗?",
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
                          "Gift Shop Girl no money" : "对不起... 但你还没拿到金币. ",

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
                    "M aristocrats" : ("贵族", "男爵", "绅士", "宫廷巫师", "廷臣", "城主", "公会会长"),
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

    attract_pop_dict = {0 : "", 1 : "些许", 2: "一些", 3 : "许多", 4 : "很多", 5 : "负载"}

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
    ##     统计描述     ##

    gstats_dict = {
                    "Beauty" : "{b}美貌：{/b}她看上去真漂亮。影响按摩师的工作和性交效果。{p}目前作为按摩师的能力: {b}%s{/b}",
                    "Body" : "{b}身材：{/b}她的身材多么匀称，多么结实。影响工作效果，如舞蹈和肛交行为。{p}目前作为舞者的能力: {b}%s{/b}",
                    "Charm" : "{b}魅力：{/b}她有多少个性和风度。影响服务员和性服侍的工作效果。{p}目前作为服务员的能力: {b}%s{/b}",
                    "Refinement" : "{b}优雅：{/b}她是多么的聪明博学，举止文雅。影响艺伎和皮绳愉虐性行为效果。{p}目前作为艺妓的能力: {b}%s{/b}",
                    "Libido" : "{b}性欲：{/b}她是多么渴望性啊。影响性交效果，并增加她能与之发生性关系的顾客数量。{p}目前作为妓女的能力: {b}%s{/b}",
                    "Sensitivity" : "{b}敏感：{/b}她对自己的身体和伴侣是多么的敏感。影响性服侍效果，提高顾客满意度。",
                    "Constitution" : "{b}体格：{/b}她有多大的精力。影响肛交效果和提高她的最大精力。",
                    "Obedience" : "{b}服从：{/b}她多么能接受命令和奴役. 影响皮绳愉虐性行为效果，降低她拒绝工作的机会。",
                    "Service" : "{b}性服侍：{/b}她做手交、口交和其他性服侍行为有多好。",
                    "Sex" : "{b}性交：{/b}她有多擅长性交行为。",
                    "Anal" : "{b}肛交：{/b}她有多擅长肛交行为。",
                    "Fetish" : "{b}皮绳愉虐：{/b}她对BDSM(绳缚与调教\支配与臣服\施虐与受虐)和其他不寻常的性行为有多在行。"
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
                        "++++++" : "你是她的一切. 她崇拜你.",
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
                        "------" : "她认为你是最糟糕的. 她想让你死.",
                        }

    fear_description = {
                        "++++++" : "她日夜生活在恐怖的世界里. 她怕死你了.",
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
                        "------" : "她觉得自己受到了公主般的待遇. 她完全信任你.",
                        "M++++++" : "她真正的位置是在你的脚下，在恐惧和欲望中颤抖.",
                        "M+++++" : "你越是伤害她，她就越开心.",
                        "M++++" : "看来她喜欢挨打. 她想要更多.",
                        "M+++" : "她害怕你，但奇怪的是却被你吸引.",
                        "M---" : "她在你身边很放松，但感觉不太对劲.",
                        "M----" : "她觉得和你在一起很安全，但也很无聊.",
                        "M-----" : "她不明白你为什么对她这么好.",
                        "M------" : "她觉得这太过分了，她不应该得到这个. 她似乎陷入困境.",
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
                        "pervert" : Personality(name="pervert", attributes=("very extravert", "very lewd"), description="野性和开放的女孩. 对各种色色的事情都很好奇，越变态越好. 不关心浪漫的事."),
                        "rebel" : Personality(name="rebel", attributes=("very extravert", "very dom"), often_stories = ["slave_story5"], description="总是与他人争吵和矛盾，有强烈的独立性. 必须按照她自己的意愿做事情."),
                        "cold" : Personality(name="cold", attributes=("very materialist", "very introvert"), description="冷漠和疏离，她不轻易表露自己的感情. 她似乎对周围发生的事情很不关心，对别人的命运也不感兴趣."),
                        "nerd" : Personality(name="nerd", attributes=("very introvert", "very idealist"), often_stories = ["slave_story8"], description="沉默寡言，喜欢读书. Rather light-headed. 好奇心. 不喜欢体力劳动."),
                        "masochist" : Personality(name="masochist", attributes=("very introvert", "very sub"), description="越卑微越好. 她喜欢呆在底层，并暗自享受被虐待的感觉. 礼物和关爱会让她恼火，她觉得自己不配拥有这些东西."),
                        "bimbo" : Personality(name="bimbo", attributes=("very materialist", "very lewd"), description="虚荣心强，渴望得到关注，关心地位和财富. 喜欢礼物和赞美. 她愿意出卖身体来获得这些东西."),
                        "meek" : Personality(name="meek", attributes=("very modest", "very sub"), often_stories = ["slave_story4"], rarely_stories = ["slave_story5","slave_story8"], description="害羞，容易动摇，会哭泣而不是反抗. 不喜欢发生冲突."),
#                         "heartless" : Personality(name="heartless", attributes=("very materialist", "very dom"), description="Cold, calculating, domineering and selfish. Will always try to benefit at the expense of others."),
                        "sweet" : Personality(name="sweet", attributes=("very idealist", "very extravert"), description="可爱和阳光的个性. 始终积极向上的. 颇为浪漫. 不喜欢消极情绪."),

                        "superficial" : Personality(name="superficial", attributes=("very extravert", "very materialist"), description="永远是社会名流，在意自己是否被人注意到，最好是穿着最出色的衣服和昂贵的珠宝. 有人说她渴望得到关注，但她知道他们只是嫉妒她的新鞋..."),
                        "holy" : Personality(name="holy", attributes=("very extravert", "very modest"), never_stories = ["slave_story7","slave_story8"], description="她是宗教和道德的倡导者，每晚都为自己的灵魂得救而祈祷，并试图让别人皈依她的信仰. 到目前为止没有什么成效，但她不会放弃."),
                        "helper" : Personality(name="helper", attributes=("very extravert", "very sub"), description="她总是为朋友着想，并且经常把别人事情放在第一位. 有时会有点多管闲事."),
                        "creep" : Personality(name="creep", attributes=("very introvert", "very lewd"), description="她在人前显得害羞而笨拙，对各种色色的话题都很着迷，她总在私下时间里进行研究. 因跟踪而被经常投诉."),
                        "repressed" : Personality(name="repressed", attributes=("very introvert", "very modest"), description="在一个非常严格的环境中长大，她生活在对自己冲动的恐惧中，并竭力压制它们. ."),
                        "schemer" : Personality(name="schemer", attributes=("very introvert", "very dom"), description="她最喜欢的是策划和制定宏伟的计划，总有一天对所有的生物进行统治...... 同时，如果她计划中必须吸吮一个肉棒...那就这样吧."),
                        "prude" : Personality(name="prude", attributes=("very materialist", "very modest"), rarely_stories = ["slave_story7","slave_story8"], description="在任何时候都要做一个敬畏阿里纳斯的好女孩. 不赞成轻浮和不道德的行为. 有人认为她暗地里有肮脏的想法，但如果是这样，她隐藏得很好."),
                        "princess" : Personality(name="princess", attributes=("very dom", "very materialist"), often_stories = ["slave_story6"], rarely_stories = ["slave_story1","slave_story2","slave_story3","slave_story5","slave_story7","slave_story8"], never_stories = ["slave_story4"], description="她外表看着像的公主（或者说她是？），她认为每个人都应该为她服务，满足她的每一个要求. 她可以很残忍，但大多数情况下她是天真无邪的."),
                        "pet" : Personality(name="pet", attributes=("very materialist", "very sub"), rarely_stories = ["slave_story5","slave_story8"], description="教师的宠物. 总是准备好取悦她的主人，喜欢在他脚下舒适地生活. 有些人看不起她的不独立，在背后骂她不讨好."),
                        "easy" : Personality(name="easy", attributes=("very lewd", "very idealist"), description="这不是她的错，她总是吸引男人，而且从来不忍心拒绝他们. 虽然很多人说她很容易相处，但她唯一的目的是传播快乐. 但愿不是传播性病."),
                        "class president" : Personality(name="class president", attributes=("very modest", "very idealist"), often_stories = ["slave_story8"], description="必须始终处于领先地位，努力成为模范，鄙视各种不当行为. 她对他人的高期望值反映了她对自己的严苛要求."),
                        "tsundere" : Personality(name="tsundere", attributes=("very idealist", "very dom"), description="易怒、难伺候，她有一个秘密的软肋. 为了帮助别人，时常让自己处于危险之中，然后因为他们需要帮助而踢他们的屁股. ."),
                        "loyal" : Personality(name="loyal", attributes=("very idealist", "very sub"), often_stories = ["slave_story2"], description="总是服从命令，出于责任感而不是恐惧. 认为每个人都必须清楚自己的位置，无论从事什么工作都要做到最好. 甚至是妓女."),
                        "yandere" : Personality(name="yandere", attributes=("very lewd", "very dom"), rarely_stories = ["slave_story3","slave_story7"], description="热情和神经质的程度非常高. 充满爱心和奉献精神，但也是个疯子. 为了得到她的男人并扼杀竞争对手，她准备做任何事情，包括......真正扼杀他们."),
                        "masochist2" : Personality(name="masochist", attributes=("very lewd", "very sub"), description="地位越低越好. 她喜欢在底层，享受各种强加在她身上的肮脏事情. 礼物和爱的姿态让她恼火，她觉得自己不配拥有这些东西."),
                        "stubborn" : Personality(name="stubborn", attributes=("very modest", "very dom"), description="不喜欢不认同她的原则和道德价值观的人，也不喜欢闹矛盾. 她在派对上很有趣，如果你喜欢以酒馆斗殴结束的派对的话."),
                     }

    gift_description = {
                        "cute" : "可爱的东西",
                        "book" : "书籍",
                        "precious" : "珍贵的东西",
                        "erotica" : "情趣用品",
                        "drinks" : "烈酒"
                        }


    gpersonalities_comment = {
                            "very extravert pos" : ("她很友善.", "她总是随时准备提供帮助.", "她很有趣.", "她很有活力."),
                            "very introvert pos" : ("她人很好.", "她很文静.", "她不爱说话.", "她说话很温柔."),
                            "very idealist pos" : ("她追随自己的梦想.", "她非常聪明.", "她对一切都很了解.", "她很机灵."),
                            "very materialist pos" : ("她很朴实", "她喜欢生活中美好的事物.", "她很有野心.", "她很有品味."),
                            "very lewd pos" : ("她思想开放.", "她很好奇", "她知道如何聚会.", "她是个真正的派对女孩."),
                            "very modest pos" : ("她很理性.", "她保持头脑清醒.", "她很稳重.", "她是纯洁的."),
                            "very dom pos" : ("她是如此自信.", "她是领导者.", "她是非常独立的人.", "她无所畏惧."),
                            "very sub pos" : ("她很卑微.", "她很沉默.", "她很忠诚.", "她很顺从."),

                            "very extravert neg" : ("她很自以为是.", "她很吵闹.", "她是以自我为中心的人.", "她不愿闭嘴."),
                            "very introvert neg" : ("她没有情趣.", "她很冷漠.", "她很不友善.", "她是一个无聊的人."),
                            "very idealist neg" : ("她是书呆子.", "她是一片雪花.", "她是个势利小人.", "她是一个书呆子."),
                            "very materialist neg" : ("她是个肮脏的婊子.", "她是如此肤浅.", "她很自私.", "她是个冷酷无情的婊子."),
                            "very lewd neg" : ("她是个变态.", "她很堕落，即使对一个妓女来说也是如此.", "她没有道德观念.", "她是个荡妇."),
                            "very modest neg" : ("她很乏味.", "她认为她比我们强.", "她是假正经的人.", "她不耐烦."),
                            "very dom neg" : ("她很嚣张.", "她过分自信.", "她是个恶霸.", "她很会操纵人."),
                            "very sub neg" : ("她是个软弱的人.", "她抱怨得太多了.", "她是个爱哭鬼.", "她是个失败者."),
                            }

    recent_event_templates = {  # Girl events given to the player for rewarding/punishing

                                # Rewardable events
                                "level up" : GirlRecentEvent(type="level up", action="获得一些经验", base_description="她变得更有经验了({color=[c_emerald]}等级%s{/color}).", discipline=False),
                                "rank up" : GirlRecentEvent(type="rank up", action="获得新的阶级", base_description="她已经到了{color=[c_emerald]}阶级%s{/color}.", discipline=False),
                                "job up" : GirlRecentEvent(type="job up", action="提升了工作技能", base_description="她增加了她的{color=[c_emerald]}%s{/color}技能.", discipline=False),
                                "good result" : GirlRecentEvent(type="good result", action="工作中表现良好", base_description="她在工作时的表现{color=[c_emerald]}%s{/color}(%s).", discipline=False),
                                "quest good result" : GirlRecentEvent(type="quest good result", action="任务中表现良好", base_description="%s", discipline=False),
                                "class good result" : GirlRecentEvent(type="class good result", action="培训中学习努力", base_description="%s", discipline=False),
                                "new act" : GirlRecentEvent(type="new act", action="尝试新事物", base_description="她第一次{color=[c_emerald]}接受了[long_act_description[%s]]训练{/color}.", discipline=False),
                                "helped" : GirlRecentEvent(type="helped", action="帮助朋友", base_description="", discipline=False), # Not implemented


                                # Neutral events
                                "exhausted" : GirlRecentEvent(type="exhausted", action="变得筋疲力尽", base_description="她把自己逼得太紧了，结果{color=[c_crimson]}筋疲力尽{/color}了."),
                                "sick" : GirlRecentEvent(type="sick", action="生病了", base_description="她 {color=[c_crimson]}生病{/color}了."),
                                "hurt" : GirlRecentEvent(type="hurt", action="受伤了", base_description="她被%sgeisha{color=[c_crimson]}强奸{/color}了."),
                                "defended" : GirlRecentEvent(type="defended", action="与客人争执", base_description="她{color=[c_emerald]}保护自己{/color}免于受到强奸."),


                                # Punishable events
                                "ran away" : GirlRecentEvent(type="ran away", action="曾经逃跑", base_description="她逃跑了，但你把她抓回来了.", encourage=False),
                                "disobey" : GirlRecentEvent(type="disobey", action="不服从你", base_description="她{color=[c_crimson]}拒绝以%s形式工作{/color}.", encourage=False),
                                "bad result" : GirlRecentEvent(type="bad result", action="工作中表现不佳", base_description="她在工作时表现{color=[c_crimson]}%s{/color}(%s).", encourage=False),
                                "quest bad result" : GirlRecentEvent(type="quest bad result", action="任务中表现不佳", base_description="%s", encourage=False),
                                "class bad result" : GirlRecentEvent(type="class bad result", action="培训中注意力不集中", base_description="%s", encourage=False),
                                "refused" : GirlRecentEvent(type="refused", action="拒绝训练", base_description="她{color=[c_crimson]}拒绝训练(%s){/color}.", encourage=False),
                                "argued" : GirlRecentEvent(type="argued", action="与对手争执", base_description="", encourage=False), # Not implemented

                                # Passive events (cannot be punished or rewarded=)
                                "acquired" : GirlRecentEvent(type="acquired", base_description="你已经获得了%s.", encourage=False, discipline=False),
                                "MC met" : GirlRecentEvent(type="MC met", base_description="你见过%s了.", encourage=False, discipline=False),
                                "MC friend" : GirlRecentEvent(type="MC friend", base_description="你和%s已经成为朋友.", encourage=False, discipline=False),
                                "MC flower" : GirlRecentEvent(type="MC flower", base_description="你现在可以给%s献花了.", encourage=False, discipline=False),
                                "MC girlfriend" : GirlRecentEvent(type="MC friend", base_description="%s现在是你女朋友.", encourage=False, discipline=False),
                                "MC lover" : GirlRecentEvent(type="MC friend", base_description="%s现在是你的爱人.", encourage=False, discipline=False),
                                "MC job" : GirlRecentEvent(type="MC job", base_description="现在你可以给%s提供一份工作.", encourage=False, discipline=False),
                                "kidnapped" : GirlRecentEvent(type="kidnapped", base_description="她被%s绑架了.", encourage=False, discipline=False),
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
                               "very experienced" : "特级",
                               "experienced" : "高级",
                               "average" : "中级",
                               "inexperienced" : "基础",
                               "very inexperienced" : "无",
                               "very experienced ttip" : "{size=-1}{color=[c_orange]}作为一名性奴，她认识几个主人并接受了广泛的性训练.{/color}",
                               "experienced ttip" : "{size=-1}{color=[c_green]}她做了好几个月的性奴，接受过各种形式的训练.{/color}",
                               "average ttip" : "{size=-1}{color=[c_yellow]}她已经做了几个月的性奴，并接受了一些性训练. .{/color}",
                               "inexperienced ttip" : "{color=[c_lightred]}她最近才成为性奴，还有很多东西要学.{/color}",
                               "very inexperienced ttip" : "{color=[c_red]}刚从奴隶商队出来，她从未受过性训练. 谁知道她会有什么反应?{/color}",
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
                        "naked" : "展现裸体",
                        "service" : "性服侍",
                        "sex" : "性交",
                        "anal" : "肛交",
                        "fetish" : "皮绳愉虐",
                        "bisexual" : "百合",
                        "group" : "群交",
                        "action naked" : "裸露",
                        "action service" : "性服侍",
                        "action sex" : "性交",
                        "action anal" : "肛交",
                        "action fetish" : "皮绳愉虐",
                        "action bisexual" : "百合",
                        "action group" : "群交"
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
                    "chat" : ["{font=[gui.yishu]}{size=18}一般话题{/font}", "{font=[gui.yishu]}{size=18}私人话题{/font}", "{font=[gui.yishu]}{size=18}女孩故事{/font}"],
                    "{font=[gui.yishu]}{size=18}一般话题{/font}" : [GirlInteractionTopic("chat", "chat", "作为奴隶的生活", "slave_chat_slave_life"),
                                        GirlInteractionTopic("chat", "chat", "在青楼里的生活", "slave_chat_brothel", condition="has_worked"),
                                        GirlInteractionTopic("chat", "chat", "与客户友好相处", "slave_chat_customers", condition="has_worked"),
                                        GirlInteractionTopic("chat", "chat", "与其他女孩相处", "slave_chat_other_girls", condition="other_girls"),
                                        ],
                    "{font=[gui.yishu]}{size=18}私人话题{/font}" : [
                                        GirlInteractionTopic("chat", "chat", "她的生活怎样", "slave_chat_well_being"),
                                        GirlInteractionTopic("chat", "chat", "她对你的感觉", "slave_chat_feelings"),
                                        GirlInteractionTopic("chat", "chat", "她的口味　　", "slave_chat_tastes"),
                                        GirlInteractionTopic("chat", "chat", "她的身世　　", "slave_chat_origins"),
                                    ],
                    "{font=[gui.yishu]}{size=18}女孩故事{/font}" : [GirlInteractionTopic("chat", "story", "再次聆听她的故事", "slave_chat_story", AP_cost=0, condition = "story")],

                    "train" : ["{font=[gui.yishu]}{size=18}技能训练{/font}", "{font=[gui.yishu]}{size=18}性爱训练{/font}", "{font=[gui.yishu]}{size=18}特别训练{/font}"],
                    "{font=[gui.yishu]}{size=18}技能训练{/font}" : [GirlInteractionTopic("train", "train", "服从训练", "slave_train_obedience", act="obedience"),
                                        GirlInteractionTopic("train", "train", "体格训练", "slave_train_constitution", act="constitution")],
                    "{font=[gui.yishu]}{size=18}性爱训练{/font}" : [
                                        GirlInteractionTopic("train", "train", "露出　　", "slave_train_sex_acts", act="naked", advanced=True),
                                        GirlInteractionTopic("train", "train", "性服侍　", "slave_train_sex_acts", act="service", advanced=True),
                                        GirlInteractionTopic("train", "train", "性交　　", "slave_train_sex_acts", act="sex", advanced=True),
                                        GirlInteractionTopic("train", "train", "肛交　　", "slave_train_sex_acts", act="anal", advanced=True),
                                        GirlInteractionTopic("train", "train", "皮绳愉虐", "slave_train_sex_acts", act="fetish", advanced=True),
                                        GirlInteractionTopic("train", "train", "百合　　", "slave_train_sex_acts", act="bisexual", advanced=True),
                                        GirlInteractionTopic("train", "train", "群交　　", "slave_train_sex_acts", act="group", advanced=True),
                                    ],
                    "{font=[gui.yishu]}{size=18}特别训练{/font}" : [GirlInteractionTopic("train", "train", "消除负面癖好", "slave_remove_fixation", condition="neg_fix")],

                    "magic" : ["{font=[gui.yishu]}{size=18}魔法技能训练{/font}", "{font=[gui.yishu]}{size=18}魔法性爱训练{/font}", "{font=[gui.yishu]}{size=18}选择方法{/font}"],
                    "{font=[gui.yishu]}{size=18}选择方法{/font}" : [GirlInteractionTopic("magic", None, "目前的方法", "slave_hypnotize_method", AP_cost=0)], # None type excludes it from girl interaction count
                    "{font=[gui.yishu]}{size=18}魔法技能训练{/font}" : [
                                                GirlInteractionTopic("magic", "train", "服从训练", "slave_magic", act="obedience", gold_cost=20),
                                                GirlInteractionTopic("magic", "train", "敏感培训", "slave_magic", act="sensitivity", gold_cost=20),
                                                GirlInteractionTopic("magic", "train", "性欲训练", "slave_magic", act="libido", gold_cost=20),
                                                ],
                    "{font=[gui.yishu]}{size=18}魔法性爱训练{/font}" : [
                                                GirlInteractionTopic("magic", "train", "露出　　", "slave_magic", act="naked", advanced=True, gold_cost=20),
                                                GirlInteractionTopic("magic", "train", "性服侍　", "slave_magic", act="service", advanced=True, gold_cost=40),
                                                GirlInteractionTopic("magic", "train", "性交　　", "slave_magic", act="sex", advanced=True, gold_cost=50),
                                                GirlInteractionTopic("magic", "train", "肛交　　", "slave_magic", act="anal", advanced=True, gold_cost=60),
                                                GirlInteractionTopic("magic", "train", "皮绳愉虐", "slave_magic", act="fetish", advanced=True, gold_cost=70),
                                                GirlInteractionTopic("magic", "train", "百合　　", "slave_magic", act="bisexual", advanced=True, gold_cost=80),
                                                GirlInteractionTopic("magic", "train", "群交　　", "slave_magic", act="group", advanced=True, gold_cost=100),
                                                ],

                    "react" : ["{font=[gui.yishu]}{size=18}鼓励{/font}", "{font=[gui.yishu]}{size=18}惩罚{/font}"],
                    "{font=[gui.yishu]}{size=18}鼓励{/font}" : [
                                    GirlInteractionTopic("react", "reward", "称赞她　　", "slave_reward_praise"),
                                    GirlInteractionTopic("react", "reward", "奖励她金币", "slave_reward_gold"),
                                    GirlInteractionTopic("react", "reward", "送给她礼物", "slave_reward_gift"),
                                    GirlInteractionTopic("react", "reward", "爱抚她　　", "slave_reward_pet"),
                                    GirlInteractionTopic("react", "reward", "给她一天假", "slave_reward_day"),
                                    GirlInteractionTopic("react", "reward", "与她做爱　", "slave_reward_sex"),
                                    ],
                    "{font=[gui.yishu]}{size=18}惩罚{/font}" : [
                                    GirlInteractionTopic("react", "discipline", "辱骂她　　", "slave_punish_scold"),
                                    GirlInteractionTopic("react", "discipline", "剥夺她工资", "slave_punish_upkeep"),
                                    GirlInteractionTopic("react", "discipline", "强迫她裸体", "slave_punish_naked"),
                                    GirlInteractionTopic("react", "discipline", "殴打她　　", "slave_punish_beat"),
                                    GirlInteractionTopic("react", "discipline", "强奸她　　", "slave_punish_rape"),
                                    GirlInteractionTopic("react", "discipline", "送她去农场", "slave_punish_farm", condition="farm"),
                                    ],
                    "misc" : ["{font=[gui.yishu]}{size=18}服装{/font}", "{font=[gui.yishu]}{size=18}主人卧室{/font}", "{font=[gui.yishu]}{size=18}DEBUG{/font}"],
                    "{font=[gui.yishu]}{size=18}服装{/font}" : [
                                    GirlInteractionTopic("misc", None, "让她脱光衣服", "slave_clothing_naked", AP_cost=0, condition = "dressed"),
                                    GirlInteractionTopic("misc", None, "让她穿上衣服", "slave_clothing_dressed", AP_cost=0, condition = "naked"),
                                    ],
                    "{font=[gui.yishu]}{size=18}主人卧室{/font}" : [
                                        GirlInteractionTopic("misc", None, "把她送到你的卧室", "slave_master_bedroom_add", AP_cost=0, condition = "master_bedroom_add"),
                                        GirlInteractionTopic("misc", None, "让她离开你的卧室", "slave_master_bedroom_remove", AP_cost=0, condition = "master_bedroom_remove")
                                        ],
                    "{font=[gui.yishu]}{size=18}DEBUG{/font}" : [GirlInteractionTopic("misc", None, "作弊", "interaction_cheat_menu", AP_cost=0, condition="debug_mode"),
                        GirlInteractionTopic("misc", None, "重置女孩的互动", "interaction_cheat_girl", AP_cost=0, condition="debug_mode"),
                        GirlInteractionTopic("misc", None, "重置玩家的互动", "interaction_cheat_MC", AP_cost=0, condition="debug_mode"),
                        ],
                    }


    free_interact_dict = {
                            "chat" : ["{font=[gui.yishu]}{size=18}一般话题{/font}", "{font=[gui.yishu]}{size=18}私人话题{/font}", "{font=[gui.yishu]}{size=18}DEBUG{/font}"],
                            "{font=[gui.yishu]}{size=18}一般话题{/font}" : [GirlInteractionTopic("chat", "chat", "闲聊", "free_chat_small_talk"),
                                                GirlInteractionTopic("chat", "chat", "八卦", "free_chat_gossip"),
                                                GirlInteractionTopic("chat", "chat", "生命", "free_chat_life"),# love_test=5),
                                                GirlInteractionTopic("chat", "chat", "爱好", "free_chat_love"),# love_test=5),
                                                ],
                            "{font=[gui.yishu]}{size=18}私人话题{/font}" : [
                                                GirlInteractionTopic("chat", "chat", "她的身世　　", "free_chat_origins", love_test=10),
                                                GirlInteractionTopic("chat", "chat", "她的爱好　　", "free_chat_hobbies", love_test=10),
                                                GirlInteractionTopic("chat", "chat", "她喜欢什么　", "free_chat_likes", love_test=10),
                                                GirlInteractionTopic("chat", "chat", "她不喜欢什么", "free_chat_dislikes", love_test=10),
                                                ],
                            "fun" : ["{font=[gui.yishu]}{size=18}笑话{/font}", "{font=[gui.yishu]}{size=18}接触{/font}", "{font=[gui.yishu]}{size=18}PLAY{/font}"],
                            "{font=[gui.yishu]}{size=18}笑话{/font}" : [
                                        GirlInteractionTopic("fun", "joke", "无关紧要", "free_joke_harmless", love_test=15),
                                        GirlInteractionTopic("fun", "joke", "成人", "free_joke_adult", love_test=15),
                                        GirlInteractionTopic("fun", "joke", "黑暗", "free_joke_dark", love_test=15),
                                        GirlInteractionTopic("fun", "joke", "刻薄", "free_joke_mean", love_test=15),
                                        ],
                            "{font=[gui.yishu]}{size=18}接触{/font}" : [
                                        GirlInteractionTopic("fun", "touch", "握住她的手　", "free_touch_hand", love_test=40),
                                        GirlInteractionTopic("fun", "touch", "亲吻她　　　", "free_touch_kiss", relationship_level=2),
                                        GirlInteractionTopic("fun", "touch", "拍打她的屁股", "free_touch_ass", love_test=55, relationship_level=3),
                                        GirlInteractionTopic("fun", "touch", "抚摸她的胸部", "free_touch_breasts", love_test=60, relationship_level=3),
                                        GirlInteractionTopic("fun", "touch", "触摸她的私处", "free_touch_pussy", love_test=65, relationship_level=3),
                                        ],
                            "{font=[gui.yishu]}{size=18}PLAY{/font}" : [
                                        GirlInteractionTopic("fun", "play", "让她脱光衣服", "free_play", act="naked", relationship_level=4),
                                        GirlInteractionTopic("fun", "play", "要求她性服侍", "free_play", act="service", relationship_level=4),
                                        GirlInteractionTopic("fun", "play", "要求她来做爱", "free_play", act="sex", relationship_level=4),
                                        GirlInteractionTopic("fun", "play", "要求进行肛交", "free_play", act="anal", relationship_level=4),
                                        GirlInteractionTopic("fun", "play", "要求她来SM　", "free_play", act="fetish", relationship_level=4),
                                        ],
                            "flirt" : ["{font=[gui.yishu]}{size=18}赞美{/font}", "{font=[gui.yishu]}{size=18}关于性的话题{/font}"],

                            "{font=[gui.yishu]}{size=18}赞美{/font}" : [
                                        GirlInteractionTopic("flirt", "compliment", "赞扬她的美貌", "free_flirt_beauty", relationship_level=1),
                                        GirlInteractionTopic("flirt", "compliment", "赞美她的身材", "free_flirt_body", relationship_level=1),
                                        GirlInteractionTopic("flirt", "compliment", "赞美她的心灵", "free_flirt_mind", relationship_level=1),
                                        GirlInteractionTopic("flirt", "compliment", "赞美她的精神", "free_flirt_spirit", relationship_level=1),
                                        ],
                            "{font=[gui.yishu]}{size=18}关于性的话题{/font}" : [
                                                GirlInteractionTopic("flirt", "chat about sex", "她的性经验", "free_flirt_sex_experience", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "她的性趣　", "free_flirt_sex_tastes", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "露出　　　", "free_flirt_sex_act", act="naked", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "性服侍　　", "free_flirt_sex_act", act="service", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "性交　　　", "free_flirt_sex_act", act="sex", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "肛交　　　", "free_flirt_sex_act", act="anal", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "皮绳愉虐　", "free_flirt_sex_act", act="fetish", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "百合　　　", "free_flirt_sex_act", act="bisexual", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "群交　　　", "free_flirt_sex_act", act="group", love_test=55),
                                                ],
                            "give" : ["{font=[gui.yishu]}{size=18}给予{/font}", "{font=[gui.yishu]}{size=18}提议{/font}"],
                            "{font=[gui.yishu]}{size=18}给予{/font}" : [
                                        GirlInteractionTopic("give", "gift", "送她礼物", "free_give_gift", love_test=20),
                                        GirlInteractionTopic("give", "gold", "给她金币", "free_give_gold", love_test=20),
                                        ],
                            "{font=[gui.yishu]}{size=18}提议{/font}" : [GirlInteractionTopic("give", "offer", "为她提供工作", "free_offer_job", love_test=90, relationship_level=5),],
                            "{font=[gui.yishu]}{size=18}DEBUG{/font}" : [GirlInteractionTopic("give", None, "修改爱情", "interaction_cheat_love", AP_cost=0, condition="debug_mode"),
                                        GirlInteractionTopic("give", None, "重置女孩的互动", "interaction_cheat_girl", AP_cost=0, condition="debug_mode"),
                                        GirlInteractionTopic("give", None, "重置玩家的互动", "interaction_cheat_MC", AP_cost=0, condition="debug_mode"),
                                        ],
                    }

    fix_description = {
                       "public acts description" : "在公共场合做",
                       "public acts action" : "进行公开play",
                       "public acts intro" : "你把青楼里的所有人都叫来：女孩、帮手、路人...... 你告诉%s，她必须在公开场合做.",
                       "public acts pos_reaction" : "她脸红了，你可以看到她的乳头在她的上衣下微微颤动. 一想到要在公共场合做，她就兴奋不已.",
                       "public acts neg_reaction" : "她愤愤不平，抱怨说被人们看着时，她什么也做不了. 你无视了她的抱怨.",

                       "cosplay description" : "穿上性感暴露的cosplay服装",
                       "cosplay action" : "穿着cosplay服装",
                       "cosplay intro" : "你让%s选择她穿的cosplay服装.",
                       "cosplay pos_reaction" : "她咬着嘴唇，看起来很俏皮. 她选择了一件开档露乳，看起来超淫荡的制服.",
                       "cosplay neg_reaction" : "她选择了一套相当保守和乏味的制服. 她不喜欢不得不穿上它.",

                       "dildos description" : "在做爱时使用性玩具",
                       "dildos action" : "使用假阳具",
                       "dildos intro" : "你告诉%s在你操她的时候在她的另一个洞里塞上假阳具.",
                       "dildos pos_reaction" : "她很容易就把假阳具塞到了合适的地方. 这看起来像是她经常做的事情.",
                       "dildos neg_reaction" : "她讨厌这样做，因为她不得不痛苦地把假阳具强行塞进去. 她一点都不享受.",

                       "vibrators description" : "跳蛋",
                       "vibrators action" : "使用跳蛋",
                       "vibrators intro" : "你告诉%s在做的时候要使用跳蛋.",
                       "vibrators pos_reaction" : "她在勃起的阴蒂上迅速地压下跳蛋，使自己处于一种强烈的兴奋状态.",
                       "vibrators neg_reaction" : "她用跳蛋时很敏感，极其不舒服，一直在抱怨那感觉怪怪的.",

                       "dirty sex description" : "肮脏的性爱",
                       "dirty sex action" : "就地性交",
                       "dirty sex intro" : "你告诉%s让她直接躺在烂泥里，准备接受你的'惩罚'.",
                       "dirty sex pos_reaction" : "她似乎很高兴直接躺在地上，像个下流的婊子.",
                       "dirty sex neg_reaction" : "她讨厌身上沾上灰尘，一直抱怨这样做不健康.",

                       "penis worship description" : "崇拜肉棒，尤其是大屌",
                       "penis worship action" : "服侍肉棒",
                       "penis worship intro" : "你告诉%s她必须在你的阴茎上擦油并给予适当的尊重. .",
                       "penis worship pos_reaction" : "她仔细看了看你那硕大的、跳动的阴茎，似乎很高兴、很兴奋，因为她马上就能和它一起玩. 她轻轻的在上面吻了一下.",
                       "penis worship neg_reaction" : "她把目光从你勃起的大屌上移开，仍然不习惯于直接面对一个男人的阴茎.",

                       "bondage description" : "捆绑游戏",
                       "bondage action" : "麻绳束缚",
                       "bondage intro" : "使用粗劣的麻绳加上你作为奴隶主的专业的束缚知识，你将%s绑成一个极度羞耻和尴尬的姿势.",
                       "bondage pos_reaction" : "当你把她捆起来时，她高兴地呻吟着，尤其喜欢那种麻绳摩擦皮肤的感觉.",
                       "bondage neg_reaction" : "当你把她捆起来时，她又哭又闹，看上去非常不舒服.",

                       "oil description" : "让身上涂上油",
                       "oil action" : "精油按摩",
                       "oil intro" : "你给了%s一瓶精油，坚持要她涂满全身.",
                       "oil pos_reaction" : "她在身体的每一个角落都涂上了油，供你取乐，在你的注视下，俏皮地按摩着她晶莹的皮肤.",
                       "oil neg_reaction" : "她对滑溜溜、油乎乎的东西感到不舒服，抱怨说它很臭，感觉很反感.",

                       "wet description" : "泼水弄湿她",
                       "wet action" : "弄湿她",
                       "wet intro" : "你让希露给你拿一桶冷水，直接倒在%s的身上.",
                       "wet pos_reaction" : "她喜欢湿淋淋的，当她的手滑过全身时，嘴里轻轻地呻吟着.",
                       "wet neg_reaction" : "她看起来又沮丧又痛苦，像只落水猫咪. 她讨厌水.",

                       "submission description" : "丢人现眼的姿势",
                       "submission action" : "羞辱她",
                       "submission intro" : "你让%s跪下来乞求即将发生的事情.",
                       "submission pos_reaction" : "她热切地服从你的命令，不顾一切地求你虐待她.",
                       "submission neg_reaction" : "她拒绝乞求，并抱怨说这是对她的侮辱.",

                       "femdom description" : "表现得像占主导地位的伙伴",
                       "femdom action" : "让她主导",
                       "femdom intro" : "你告诉%s这次由她去主导和支配.",
                       "femdom pos_reaction" : "她很高兴被赋予主导地位的角色. 她反常地喜欢发号施令和支配她的伴侣.",
                       "femdom neg_reaction" : "她犹豫了一下，然后尴尬地试图用不太令人信服的声音下达一个命令. 她几乎马上就改口道歉了. 她一点也不喜欢在这种事情上作为主导.",

                       "gags description" : "做爱时被塞住嘴",
                       "gags action" : "戴上口塞",
                       "gags intro" : "你命令%s戴上一个大的球型口塞，使她的嘴一直张着难以说话. .",
                       "gags pos_reaction" : "当她戴上口塞时给你一个羞涩的眼神，似乎很奇怪，她看起来既高兴又兴奋.",
                       "gags neg_reaction" : "她控制不住地流口水，几乎说不出话来，愤怒地看着你. 她似乎很讨厌这样.",

                       "strap-ons description" : "戴上假阴茎去干其他女孩",
                       "strap-ons action" : "戴上假阴茎",
                       "strap-ons intro" : "你让%s戴上假阳具干希露.",
                       "strap-ons pos_reaction" : "她戴上一个巨大的黑色带状假阳具, 一头插在她的小穴，另一头在她面前晃来晃去的时候，她看起来很得意. 希露喘着粗气看着那个东西.",
                       "strap-ons neg_reaction" : "她一边穿一边抱怨自己为什么不是个男人.",

                       "roleplay description" : "在做爱的时候扮演一个角色",
                       "roleplay action" : "玩角色扮演",
                       "roleplay intro" : "你告诉%s将扮演的角色：你是城市警卫，她是一个被捕的小偷.",
                       "roleplay pos_reaction" : "她喜欢角色扮演这个玩法，并努力表现出一个面带忏悔的好色小偷的样子.",
                       "roleplay neg_reaction" : "她认为这很愚蠢，很容易分心，根本就不参与其中.",

                       "plugs description" : "在她屁眼里塞上肛塞",
                       "plugs action" : "用肛塞",
                       "plugs intro" : "拿出一个大的、闪闪发光的橡胶塞，你告诉%s把它插入她的屁股里.",
                       "plugs pos_reaction" : "她高兴地将肛塞推入她准备好的屁眼深处时，发出了诱人地呻吟声.",
                       "plugs neg_reaction" : "她非常艰难地插入肛塞，感到异常羞愧和痛苦. 这让她感到非常不自在.",

                       "enemas description" : "进行灌肠.",
                       "enemas action" : "灌肠",
                       "enemas intro" : "你告诉%s是时候清理了.",
                       "enemas pos_reaction" : "当你把灌肠器插进她的屁眼里，开始往她身上灌满水时，她求你把水量再加大些. 很快，她的肚子像气球一样鼓起来了.",
                       "enemas neg_reaction" : "当你把清水灌满她的肚子时，她因羞愧和恐惧而哭泣不止. 她恳求你停下来.",

                       "beads description" : "使用肛门拉珠.",
                       "beads action" : "使用肛门拉珠",
                       "beads intro" : "你给%s一条好像巨大珠子串成的项链，并告诉她该怎么用.",
                       "beads pos_reaction" : "她把珠子一个接一个地塞进她的屁眼里，你在看的时候她一直在呻吟，显然很享受.",
                       "beads neg_reaction" : "当她痛苦地往屁股里塞进一两颗珠子的时候，她皱起眉头并轻声抽泣着. 她告诉你她讨厌这样.",

                       "masturbation description" : "让她手淫.",
                       "masturbation action" : "自慰",
                       "masturbation intro" : "你告诉%s在做这件事的时候自己玩.",
                       "masturbation pos_reaction" : "当你看着她时，她开始狂热地玩弄她的阴蒂，用手指抚弄她的阴户.",
                       "masturbation neg_reaction" : "她假装在自慰，但其实什么也没做. 她一点也不喜欢这样.",

                       "fingering description" : "把手指插进她体内.",
                       "fingering action" : "手指插入",
                       "fingering intro" : "你告诉%s你会把手指放进她体内.",
                       "fingering pos_reaction" : "当你的手指滑入的时候，她的阴道迎合着你的动作，一根，两根，然后三根手指都轻松地放到了里面. 当你加快抽插速度，淫水满覆你的手指时，她高兴地大声呻吟着.",
                       "fingering neg_reaction" : "当你很艰难地把一根手指插进去的时候，她的阴道剧烈收缩似乎想把你的手指挤出去. 眼泪从她脸上流下来：她一点也不喜欢这样.",

                       "handjobs description" : "让她为我打手枪.",
                       "handjobs action" : "手交",
                       "handjobs intro" : "你命令%s为你来一次美好撸管体验.",
                       "handjobs pos_reaction" : "她喜欢用手在你的鸡巴上下摩擦撸动，看着你跳动着，充满吸引力的坚硬的鸡巴.",
                       "handjobs neg_reaction" : "她机械呆板，缺乏热情. 她不喜欢做手交.",

                       "cunnilingus description" : "舔阴",
                       "cunnilingus action" : "舔阴",
                       "cunnilingus intro" : "你走到%s的两腿之间，分开她的'花瓣'.",
                       "cunnilingus pos_reaction" : "当你的舌头深入她的体内时，感觉到与平时不一样的触感让她止不住地呻吟起来. 随着爱液从小穴喷涌而出，她感到了极致的快感.",
                       "cunnilingus neg_reaction" : "她皱着眉头，试图闭上双腿，这并没有让她产生什么感觉. 似乎对于私处的按摩不是她的弱点.",

                       "oral description" : "口交",
                       "oral action" : "口交",
                       "oral intro" : "你告诉%s用她的舌头和嘴来增加快感.",
                       "oral pos_reaction" : "她喜欢舔弄和吮吸她的伴侣，她在做的时候一直保持和你有眼神交流.",
                       "oral neg_reaction" : "她对这种味道感到非常恶心，看上去很生气. 她不喜欢口交.",

                       "irrumatio description" : "强制口交",
                       "irrumatio action" : "强制口交",
                       "irrumatio intro" : "命令%s仰躺在床上把头靠在床边，你决定狠狠地操她的嘴.",
                       "irrumatio pos_reaction" : "你把坚硬的鸡巴尽可能深地往她的嘴里塞，她很配合地几乎把它全吞进去了，似乎很享受她的喉咙被强奸.",
                       "irrumatio neg_reaction" : "她恶心、咳嗽、哭泣、扭动，讨厌它，但你还是强行把鸡巴插进她的喉咙里.",

                       "deep throat description" : "深喉.",
                       "deep throat action" : "深喉",
                       "deep throat intro" : "你告诉%s准备好为你提供深喉服务.",
                       "deep throat pos_reaction" : "她没有呕吐反应，喜欢尽可能地把你的鸡巴吸进喉咙里.",
                       "deep throat neg_reaction" : "她不停哭闹着，差点吐了出来，求你停下来. 你没理她.",

                       "titjobs description" : "乳交",
                       "titjobs action" : "乳交",
                       "titjobs intro" : "你命令%s用她的奶子来取悦你.",
                       "titjobs pos_reaction" : "她把你的大鸡巴完全裹在她漂亮的奶子中间，一边伸出舌头舔弄着肉棒顶端，一边把用奶子使劲地上下撸动.",
                       "titjobs neg_reaction" : "她笨拙地试图用乳房摩擦你的鸡巴，但她始终笨手笨脚的，显得很不耐烦.",

                       "footjobs description" : "来一次足交",
                       "footjobs action" : "足交",
                       "footjobs intro" : "你命令%s用她的腿和脚来摩擦你的鸡巴.",
                       "footjobs pos_reaction" : "她喜欢用她的脚玩你的鸡巴，当她把你带到你的极限时，给了你一个很好的裙底视角.",
                       "footjobs neg_reaction" : "她讨厌这样，只是笨拙用她的脚踩了踩你的肉棒. 你叫她停下来.",

                       "double penetration description" : "两个洞同时插入",
                       "double penetration action" : "双穴插入",
                       "double penetration intro" : "你要求你的一个保安加入你和%s，告诉他干她的屁股，因为你在前面干她.",
                       "double penetration pos_reaction" : "她疯狂地大声尖叫着，因为她前后两个洞都插入了一根大鸡巴. 她喜欢这样.",
                       "double penetration neg_reaction" : "她心烦意乱，因为她身上同时有两个鸡巴. 对她来说似乎太多了.",

                       "fisting description" : "拳交",
                       "fisting action" : "拳交",
                       "fisting intro" : "告诉%s不要动，你决定用拳头插她的阴部.",
                       "fisting pos_reaction" : "当你用拳头强奸她湿漉漉的阴部时，她高兴地尖叫着，最终让她达到了巨大的喷射性高潮.",
                       "fisting neg_reaction" : "她痛苦地尖叫，乞求你停止，因为你的拳头用极不自然的方式插进了她的阴道里. 她讨厌这个.",

                       "insults description" : "用语言侮辱她",
                       "insults action" : "语言侮辱",
                       "insults intro" : "当你强迫她表演时，你用能让一个妓女脸红的语言叫着%s的名字.",
                       "insults pos_reaction" : "她似乎很喜欢被人欺辱，仅仅一分钟后，你就发现她浑身湿透了.",
                       "insults neg_reaction" : "她对你的话感到震惊和不安，无法集中精力在她正在做的事情上. 这完全没用.",

                       "69 description" : "69式相互口交",
                       "69 action" : "69",
                       "69 intro" : "你让%s摆出69式互相口交的姿势.",
                       "69 pos_reaction" : "她喜欢69式口交并非常享受其带来的快感，当她照顾她的伴侣的肉棒时，她也享受着私处被舔的感觉.",
                       "69 neg_reaction" : "她看起来很不高兴，因为她似乎很鄙视这种体位. 整个过程对双方来说都是不愉快的.",

                       "watersports description" : "尿浴.",
                       "watersports action" : "尿浴",
                       "watersports intro" : "你告诉%s准备好接受圣水洗礼.",
                       "watersports pos_reaction" : "她喜欢在人前撒尿和被人撒尿. 她不觉得这有什么可耻的.",
                       "watersports neg_reaction" : "她对尿液感到厌恶，一想到这些就感到恐惧.",

                       "ass-to-mouth description" : "肛交后口交",
                       "ass-to-mouth action" : "肛交后口交",
                       "ass-to-mouth intro" : "你决定先干%s的屁股再干她的嘴.",
                       "ass-to-mouth pos_reaction" : "她欣然接受了你的肉棒，并为你舔得干干净净，丝毫不顾它一秒钟前还在她的屁股里.",
                       "ass-to-mouth neg_reaction" : "当你把你的鸡巴塞进她的嘴里时，她感到反胃，抱怨说这是肮脏和恶心的.",

                       "kissing description" : "接吻",
                       "kissing action" : "亲吻她",
                       "kissing intro" : "你开始亲吻%s.",
                       "kissing pos_reaction" : "她热情地回应你的吻，将她的舌头与你的舌头交缠在一起. 她直到最后才松口.",
                       "kissing neg_reaction" : "她试图避开你，似乎根本不喜欢接吻. 当你放过她时，她松了一口气.",

                       "spanking description" : "打屁股",
                       "spanking action" : "打她屁股",
                       "spanking intro" : "你告诉%s她是个坏女孩，她会被狠狠打一顿.",
                       "spanking pos_reaction" : "当你在操她的时候狠狠地鞭打着她的屁股，她痛苦并快乐地尖叫着，眼中泛着幸福的眼泪.",
                       "spanking neg_reaction" : "你一边打她的屁股一边操她. 她扭动着身体，试图摆脱你，痛苦地呻吟着. 她不喜欢这样做.",

                       "rimming description" : "毒龙钻",
                       "rimming action" : "毒龙钻",
                       "rimming intro" : "你告诉%s要彻底舔你的屁眼.",
                       "rimming pos_reaction" : "她非常认真地把你舔干净，当把她的舌头伸进你的屁股里的时候，手上也没停下来一直在撸动着你的鸡巴.",
                       "rimming neg_reaction" : "她讨厌这种行为，只是怯懦地舔着你的屁眼. 有点痒痒的，但感觉一点也不好.",

                       "fondling her boobs description" : "被抚摸",
                       "fondling her boobs action" : "抚摸胸部",
                       "fondling her boobs intro" : "你抚摸%s的胸部，玩弄她的乳头.",
                       "fondling her boobs pos_reaction" : "她喜欢你捏她的奶子，当你揉搓她勃起的乳头时会发出性感的呻吟.",
                       "fondling her boobs neg_reaction" : "她不喜欢在那里被碰触，紧张的情绪使训练变得不那么愉快.",

                       "groping her ass description" : "被人摸来摸去",
                       "groping her ass action" : "抚摸她的屁股",
                       "groping her ass intro" : "你摸着%s的屁股，开始用手指抚弄她的屁眼.",
                       "groping her ass pos_reaction" : "她喜欢被抚摸，当你把两根手指塞进她的屁眼时，她会兴奋地呻吟.",
                       "groping her ass neg_reaction" : "她不喜欢在那里被触碰，紧张的情绪使训练变得不那么愉快.",

                       "lactation description" : "强制泌乳",
                       "lactation action" : "强制泌乳",
                       "lactation intro" : "摸着%s乳房，你拿出一个装满奇怪液体的注射器插入了她的乳头.",
                       "lactation pos_reaction" : "她惊讶地喘息着，因为她的乳房越来越大了. 很快她开始不受控制地泌乳，当你把她的大乳房挤得满满的时候，她发出了呻吟.",
                       "lactation neg_reaction" : "当她的胸部越来越重，越来越大时，她大喊大叫，痛哭流涕. 这一经历太过痛苦了，她没能给你分泌出任何东西出来.",

                       "doggy style description" : "后背位",
                       "doggy style action" : "后背位",
                       "doggy style intro" : "把她推倒，四肢着地，接着你开始从后面干%s.",
                       "doggy style pos_reaction" : "当你的阴茎长度沿着她最敏感的部位抽动时，她发出了愉悦的呻吟. 她对这种体位爱不释手.",
                       "doggy style neg_reaction" : "她一边磨牙一边等着你的做完. 她一点也不喜欢这个体位.",

                       "cowgirl description" : "骑乘位",
                       "cowgirl action" : "骑乘位",
                       "cowgirl intro" : "你让%s骑在你的身上.",
                       "cowgirl pos_reaction" : "她喜欢在上面，爱不忍释地在你的阴茎上上下抽动着，直到你们都筋疲力尽. .",
                       "cowgirl neg_reaction" : "她不喜欢在上面，在你从下面操她时保持被动.",

                       "piledriver description" : "抬单腿后背位",
                       "piledriver action" : "抬单腿后背位",
                       "piledriver intro" : "从背后把%s推倒并抬起她的腿，你把你坚硬的阴茎插入她的体内.",
                       "piledriver pos_reaction" : "当你无情地猛烈抽插她的时候，她被欲望和快乐完全淹没了.",
                       "piledriver neg_reaction" : "她对这个新体位感到困惑和烦恼，告诉你她一点也不喜欢.",

                       "spooning description" : "侧身位",
                       "spooning action" : "侧身位",
                       "spooning intro" : "从后面抱着%s，你的阴茎从侧面慢慢滑入她的小穴，时不时挑逗着她的身体.",
                       "spooning pos_reaction" : "她喜欢被人抱的同时被人干. 她完全放松下来，轻轻地呻吟着，很快就准备好达到高潮.",
                       "spooning neg_reaction" : "当你从后面操她时，她一直不为所动，看起来很厌烦.",

                       "bukkake description" : "多人颜射",
                       "bukkake action" : "多人颜射",
                       "bukkake intro" : "召集一群保安，让他们看着你和希露干%s. 他们开始边看边打手枪. 当你达到极限时，你把肉棒抽出来射在了她的脸上，其他男人也纷纷射到她的脸上.",
                       "bukkake pos_reaction" : "当她脸上、头发上和身体上经历了一场精液淋浴时，她在迎来激烈的高潮中颤抖. 她大口大口地吃着每个人肉棒上剩余的精液.",
                       "bukkake neg_reaction" : "她哀嚎着试图躲避，因为每个人都在她脸上和头发上喷射着精液. 她痛苦地抱怨着那种恶心的气味和味道.",

                       "cum in mouth description" : "在她嘴里射精",
                       "cum in mouth action" : "口暴",
                       "cum in mouth intro" : "你决定用%s的嘴来结束.",
                       "cum in mouth pos_reaction" : "当你把一大团滚烫精液射到她准备好的嘴里时，她看起来很陶醉. 她用舌头玩弄着它，享受它的味道和质地.",
                       "cum in mouth neg_reaction" : "你在她的嘴里射了很多，这让她在旁边一阵咳嗽. 她把这些东西都吐出来，不停地抱怨着.",

                       "cum on face description" : "颜射",
                       "cum on face action" : "颜射",
                       "cum on face intro" : "你把精液射在%s的脸上.",
                       "cum on face pos_reaction" : "当她接受你的精液时，她用手把精液缓缓涂抹在脸上，然后吮吸着手指上的剩余精液，问到浓厚精液的味道她高兴地喘息着.",
                       "cum on face neg_reaction" : "当你试图在她脸上喷射时，她厌恶地撇过脸去. 完事后她连忙拿一块湿布来试图马上擦干净.",

                       "cum in hair description" : "射到头发上",
                       "cum in hair action" : "射到头发上",
                       "cum in hair intro" : "你决定射在%s柔软如丝的头发上.",
                       "cum in hair pos_reaction" : "当你把她的头发缠在你的鸡巴上，在她的头皮上挤压最后一滴时，她呻吟起来. 她喜欢被当作一个肮脏的精液垃圾桶.",
                       "cum in hair neg_reaction" : "当你把精液射在她的头发上时，她大喊大叫，抱怨说要花很长时间才能把它弄下来.",

                       "cum on body description" : "射在她身上",
                       "cum on body action" : "射到身上",
                       "cum on body intro" : "你决定射在%s的身上.",
                       "cum on body pos_reaction" : "她达到了高潮，你拿出你的鸡巴，把白色的精液洒在她柔软的皮肤上.",
                       "cum on body neg_reaction" : "当你把满满的精液射在她的身体时，她扭动身体试图躲开，抱怨说这黏糊糊的还带有一股恶心的气味.",

                       "cum shower description" : "被精液浇灌.",
                       "cum shower action" : "精子浴",
                       "cum shower intro" : "服下从香料市场弄来的一种特殊的药丸，你的肉棒开始膨胀隆起，准备用大量的精液迸发. 你让%s躺下准备接受你的种子.",
                       "cum shower pos_reaction" : "你射了一次又一次直到她被白色粘稠的精液覆盖. 她被这种感觉迷住了.",
                       "cum shower neg_reaction" : "当你在她身上射出一次又一次的精液时，她害怕地尖叫着、畏缩着，对气味和感觉感到厌恶.",

                       "swallowing description" : "深喉射",
                       "swallowing action" : "深喉射",
                       "swallowing intro" : "你把你的肉棒深深地塞进%s的嘴里，为了能更爽，你把大量的精液射到她的喉咙深处.",
                       "swallowing pos_reaction" : "她大口大口地吞咽着，从你悸动的阴茎中挤出每一滴精液. 当你完事后，她性感地舔着嘴唇.",
                       "swallowing neg_reaction" : "她泪流满面，在你一次又一次的射精中试图把它全部吐出来. 她只是吐出来一点，而且看起来对不得不喝酒感到不高兴.",

                       "creampie description" : "外射",
                       "creampie action" : "外射",
                       "creampie intro" : "把你的鸡巴慢慢地从%s身体里拿出来，把你那浓浓的白色精液射在她的屁股和阴部.",
                       "creampie pos_reaction" : "当你把精液喷洒在她的洞里时，她在巨大的高潮中颤抖. 她似乎很喜欢这样.",
                       "creampie neg_reaction" : "她捂着脸，求你停下来，说这是令人毛骨悚然和恶心的.",

                       "cum inside description" : "在她体内射精",
                       "cum inside action" : "内射",
                       "cum inside intro" : "不顾后果，你决定在%s深处射精.",
                       "cum inside pos_reaction" : "她达到了令人炫目的高潮，当你在她体内射出一股股浓厚的精液时，她疯狂地呻吟着.",
                       "cum inside neg_reaction" : "她尖叫着拔你出去，但你没有理会她，用粘稠的精液填满她的深处. 她因羞愧和厌恶而哭泣不止.",

                       "multiple orgasms description" : "多重高潮",
                       "multiple orgasms action" : "多重高潮",
                       "multiple orgasms intro" : "你有节奏的揉搓着她的阴蒂，阴蒂带来的刺激不断让着%s的身体因反复的高潮而颤抖着. 为了不让她有休息的时间，你手一直不断的刺激着，直到她一次又一次的高潮.",
                       "multiple orgasms pos_reaction" : "她喜欢这样子完全失去了理智的感觉，在你停下手的动作后，她看起来只是一个顺从、崇拜、幸福的奴隶.",
                       "multiple orgasms neg_reaction" : "她感到过于敏感乞求你停手，几乎因为过度的高潮而痛苦晕倒过去. 她不喜欢这样做.",

                       "denied orgasm description" : "被拒绝的高潮",
                       "denied orgasm action" : "禁止高潮",
                       "denied orgasm intro" : "你决定逗%s到极限，不让她达到高潮.",
                       "denied orgasm pos_reaction" : "她似乎喜欢被挑逗又无法达到高潮的感觉，随着时间的推移，她变得无比饥渴和敏感.",
                       "denied orgasm neg_reaction" : "她痛苦地尖叫着，乞求你让她达到高潮. 她很不高兴你不让她去.",

                       "squirting description" : "潮吹",
                       "squirting action" : "潮吹",
                       "squirting intro" : "你把手指插进%s的阴部，开始摩擦她的阴道的内壁，并寻找着她那敏感的G点. 她似乎被这种感觉征服了.",
                       "squirting pos_reaction" : "她强烈的潮吹了，把淫水弄得房间里到处都是. 她的高潮是如此强烈，以至于之后都动弹不得了.",
                       "squirting neg_reaction" : "她觉得很奇怪很恶心，求你把手拿开. 她根本就不喜欢.",

                       "stripping description" : "脱光",
                       "stripping action" : "让她脱衣服",
                       "stripping intro" : "告诉%s慢慢地、性感地自己脱掉衣服，你看着她按要求脱.",
                       "stripping pos_reaction" : "当她感受到衣服与她柔软的皮肤摩擦的爱抚时，她呻吟起来. 她看着你的眼睛，一点一点地慢慢脱下她的内衣，确保给你一个好的展示.",
                       "stripping neg_reaction" : "抱怨和发牢骚，她不情愿地脱下衣服，尴尬地隐藏自己的私处. 她看起来很生气很羞愧.",

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
                            "The Maid" : "即使身处逆境，{b}女仆{/b}也能昂首挺胸，通过努力工作和承诺获得成功. 她是仆人和卑微工人的守护神.",
                            "The Player" : "{b}优伶{/b}总是准备好讲一个引人入胜的故事或即兴表演一个奢华的舞蹈，因她的派对技巧和魅力而受到赞赏. 她是歌手、演员和其他有成就或有抱负的艺术家的守护神.",
                            "The Model" : "拥有完美的自然美和优雅，如果有点虚荣的话，{b}模特{/b}会让男人和女人都着迷. 她是年轻人的守护神，美丽的人和富有的人.",
                            "The Courtesan" : "{b}花魁{/b}是礼仪、诱惑和政治方面的大师，她能让任何人对她的每一个念头都屈服. 她是高尚的妇女、政治家和其他阴谋家的守护神.",

                            "The Escort" : "利用她的身体和技能来获得巨大的优势，{b}伴游{/b}是一个善于利用自己的才能获取利润的专家. 她是花哨的妓女、商人和雇佣兵的守护神.",
                            "The Fox" : "{b}狐娘{/b}是一个神秘的人物，似乎总是在幸运的场合出现，据说她给和它同床的每个人带来好运. 她是旅行者和隐士的守护神.",
                            "The Slut" : "一个非常受人尊敬的人物，{b}荡妇{/b}以体验各种形式的性和快乐为乐，拒绝不适合她的法律和道德. 她是街头女孩、小偷、浪荡子的守护神，偶尔也是阿里奥斯的牧师.",
                            "The Bride" : "作为和平与繁荣的预兆，{b}新娘{/b}温柔而忠诚. 她是成年处女、孕妇、已婚妇女和寡妇的守护神."
                            }

    ## GOSSIP ##

    generic_gossip = [
                        "我不明白魔术师怎么能在光天化日之下进行实验. 阿里奥斯狂热者教会以极大的热情憎恨魔法使用者. 但他们并没有采取行动关闭它们...",
                        "对大米、谷物、蔬菜、肉类征税……很快他们就要对水坑里的水征税了!男人能吃的还剩什么?",
                        "从我记忆中起，Zan就一直被欲望、贪婪和腐败所吞噬，但这些天我们似乎又跌到了新低.",
                        "不是所有的护卫都是十足的混蛋. 我认识一个不错的人. 尽管如此，他们还是少之又少.",
                        "皇室成员都高高在上，离我们很远. 他们让卫兵盲目地抢劫我们，但当一个小偷出现时，她从来没有被抓住过. 正义何在?",
                        "你以为小偷会放过我们这样的穷人吗?不，先生，如果你什么都没有，他们还是会从你冰冷的死手上撬开的.",
                        "卫兵从我们这些可怜的人身上偷了那么多东西，几乎没给小偷留下什么.",
                        "*降低声调*听说过黑暗女神莎莉娅吗?他们说她在这个城市的贫民窟里有一座寺庙. 它让我毛骨悚然.",
                        "城里某处有一座莎莉娅的神庙. 不过，我想很难找到她的支持者，因为他们很少公开支持她.",
                        "阿里奥斯，该死的莎莉娅婊子和她的秘密神殿!像她这样卑鄙的女神在这个城市里没有立足之地. 我们是光明正大的人，不是吗?",
                        "我听说莎莉娅根本不是她所吹嘘的那种人. 你听说过牺牲，处女之血…这是无稽之谈. 她的追随者喜欢保守秘密，但他们喜欢更平凡的事情，比如偷你的钱包.",
                        "莎莉娅的追随者们早餐吃的是小孩子的心. 那是我妈妈说的.",
                        "这个城市里到处都是奸诈的政客和狡诈的小偷，你可能会奇怪，为什么他们不修建一座通往莎莉娅的教堂!",
                        "当我弟弟小的时候，他总是孤独，沉思，计划报复那些欺负他的孩子. 我们常开玩笑说，他是我们自己的小莎莉娅使徒!",
                        "莎莉娅是个胆小的女神，这就是她. 一个真正的上帝会有他的追随者居无定所？",
                        "有人说，莎莉娅的美貌本身就是她在自己的计划中使用的武器...",
                        "们愚蠢到相信阿里奥斯更好，因为他是光明之神. 但是，谁希望他们所有的思想和秘密都被照亮呢?莎莉娅也扮演着同样重要的角色...",
                        "有人告诉我他在贫民窟看到了一个莎莉娅圣地. 但是他不告诉我它在哪里.",
                        "Zan充满了肮脏的秘密和黑暗的角落. 一个人必须注意自己的言行——很容易激怒错误的人，也很难获得任何人的信任.",
                        "有三种方法可以让人在攒钱:阴部，香料，或锋利的刀.",
                        "我在竞技场看到了一场不可思议的比赛!辛西娅是个奴隶，但她很有风度.",
                        "我真不敢相信人们喜欢在竞技场里看格斗到死. 如果你想进一步证明这个地方野蛮，你有证据了.",
                        "我不在乎竞技场上的死亡. 大多数时候都是怪物和奴隶. 玩得很开心!",
                        "人们在竞技场上押下重金. 如果你知道该支持谁，就会有一笔不错的钱.",
                        "许多冒险家在竞技场里碰运气. 许多人在几次争吵后就会变得软弱甚至更糟. 但辛西娅忍住了.",
                        "我不看比赛，太血腥了. 我只是打赌. 但是最近，我运气不好.",
                        "有人告诉我他有个点子，总能在比赛中获胜. 起初我不相信他，但他连续赢了五场比赛!",
                        "竞技场里的角斗士们穿着闪闪发光的金色盔甲，用荣耀和鲜血覆盖着自己!这不是一个惊人的景象吗?",
                        "冒险家联盟吸引了来自遥远国度的冠军和渣滓. 我不会相信他们中的任何一个，这是肯定的.",
                        "如果你想要一个快速赚钱的方法，你可以做比把你的命运与联盟的冒险家. 他们总是有一些丰厚的奖金给有进取心的个人，并不是所有的都需要你拔剑.",
                        "冒险家联盟更喜欢通过机动而不是暴力来推进他们的目标，但众所周知他们两者都用.",
                        "没有冒险家联盟的头头. 管理者只处理文书工作，但所有成员都被认为是平等的.",
                        "冒险家联盟怎么可能没有领袖呢?一定有人在暗中操纵他们.",
                        "我很生气，那些冒险家联盟中的暴发户变得如此富有，而我们这些真正的贵族却面临着毁灭.",
                        "许多贵族和朝臣都避开冒险家联盟，因为它接纳平民，但他们已经开办了一些城里最赚钱的企业.",
                        "听说过兄弟会吗?他们说他们会保护平民不受贵族和贵族出身的影响. 这样的废话.",
                        "我听说过一个叫做兄弟会的秘密政治组织. 我不知道他们是谁，也不知道他们在做什么，但传言他们在这座城市拥有巨大的权力.",
                        "一个疯狂的混蛋让我的朋友为“忠于王室”和“收回我们应得的东西”而激动不已. 我请求我的朋友不要听这种胡言乱语，但是现在她被国王的卫兵逮捕了，他们也怀疑我...",
                        "弟兄们，你们不要劳苦，也不要受苦难，叫几个出身高贵的懒汉，昼夜宴乐. 如果你加入兄弟会，你可以结束这一切…嘘，有人来.",
                        "这位妇女声称兄弟会将会起来帮助这些小人物. 但我知道真相:几个月之内，他们就把自己和亲戚都推上了权力的宝座，他们不比法老强多少.",
                        "法罗国王是我们的合法神选领袖. 质疑比我们优越的人的地位是异端邪说:让我们不要再谈所谓的“兄弟情谊”了.",
                        "魔法师师是害群之马，他们只配受毁灭. 他们用不信神的实验破坏了我们心爱的城市. 我希望国王有足够的理智把他们都绞死.",
                        "一点点魔法有什么问题?这不是变态，也不是骗局. 人们害怕他们不理解的东西，仅此而已. 我自己也涉足魔法，你知道吗?这里有一种药膏，你可以便宜买到...",
                        "在Zan中会法术的人早已多如牛毛. 但他们与阿里奥斯教会之间的冲突已经开始出现裂痕.",
                        "阿里奥斯的一位牧师告诉我，巫师与恶魔为伍，密谋必然毁掉Zan. 必须做点什么.",
                        "那些魔法师只不过是些有钱的、被宠坏了的顽童，玩弄着他们不懂的魔法. 我不喜欢那些来自教堂的偏执狂，但他们是有道理的.",
                        "不是异端邪说，法师们为我们城市的财政贡献了很多钱. 如果这个城市禁止一切有问题的行为，Zan就没有多少剩余了.",
                        "Zan城可以看到怪物. 我亲眼看见一个三头狼在一条黑暗的小巷里强奸一个年轻女孩. 这个城市变成什么样子了?",
                        "魔法师要为这座城市的怪兽瘟疫负责，还有谁呢?他们应该把他们和他们的宠物一起扔在一个黑暗的牢房里，并扔掉钥匙.",
                        "我不相信. 巫师有足够的麻烦，因为它是光明祭司. 为什么他们要在街上放怪物，让他们的处境更糟?",
                        "晚上怪物在街上游荡. 现在任何人都不应该在外面呆得太晚，尤其是年轻漂亮的女孩.",
                        "整个巡逻队在花园附近被消灭了?这个可怕的问题已经失控了!",
                        "从外面看，大教堂是个不错的建筑，但你不会喜欢里面发生的事情，相信我.",
                        "高级女祭司主张将魔法从这座城市完全去除. 她总是用她自己的方式去做.",
                        "我还记得战前的那些日子，那时的特级大师正领导着对阿里奥斯的狂热崇拜……我告诉你，这算是比较平和的日子了.",
                        "自从特级大师去参加圣战以来，这位高级女祭司一直在巩固她在这座城市的权力. 我想她不希望他回来.",
                        "听到圣地战争的消息了吗?他们告诉我进展不顺利. 异教徒每一步都在反抗我们，但阿里奥斯肯定不会让他的羊群失望.",
                        "阿里奥斯的牧师想把他们的崇拜强加给城市的其他地方，简单明了. 不要被女祭司正义的说教所愚弄.",
                        "我的一个朋友成了阿里奥斯的修女，但她改变了主意，一周前出走了. 我不知道发生了什么.",
                        "我受不了阿里奥斯教堂那些正直的行善者. 我肯定他们在隐瞒什么.",
                        "他们说很多阿里奥斯的女祭司在皈依之前都是妓女. 我不知道为什么. 但这让我很兴奋.",
                        "阿里奥斯是光明和力量之神. 愿他的光引导我们行善. 愿他的能力扶持我们的膀臂.",
                        "阿里奥斯的真正教义是一种美. 别听那些牧师胡说八道，根本就没那回事. 在你的心中就能找到爱的光芒.",
                        "他们说恶魔在街上游荡. 我说这和法庭上发生的事情比起来简直是小巫见大巫.",
                        "宫廷贵族所做的就是吃喝嫖赌，彼此密谋陷害. 我希望我有那种生活.",
                        "这座城市注定要灭亡. 脑袋烂了，怎么能救身体?",
                        "我姐姐是宫廷的女仆. 她看了一眼其中一个仪式，就滔滔不绝地说个不停. 的礼服!”、“灯!”、“珠宝!、“金碟子!”，等等.",
                        "每个高贵的朝臣背后都有一个或多个交际花. 那就是他们叫妓女的方式. 注意了，这并不能阻止她们去普通的青楼.",
                        "赞的贵族是一个奇怪的品种. 他们把自己的土地吸干试图在宫廷中占有它并给国王留下深刻印象;他们却都藐视他，以为他是软弱的. 他们是其实也被愚弄的人.",
                        "18年前，法罗国王在他统治的初期做得还不错. 但他的成就正在一个接一个地瓦解，现在这座城市已经失去了所有方向.",
                        "我不管公主的母亲怎么了，国王应该再婚. 万一公主出事了怎么办?",
                        "没有男性继承人会给王室带来灾难. 为什么国王不明白呢?",
                        "因为法罗国王没有男性继承人，所以如果公主的儿子结婚，权力将归他所有. 我猜她在这期间会是摄政王.",
                        "当然，法罗国王对一切都采取放任的态度……但这不是让赞如此伟大的原因吗?你想看到对妓女、酒精、香料甚至赌博的打击吗?",
                        "王总是郁郁寡欢，情绪低落……对于一个朝臣们开那么多派对的人来说，他看起来确实很冷酷.",
                        "公主很可爱，不是吗?所有的骑士和贵族都疯狂地爱上了她.",
                        "她精致的容貌和举止使公主成为所有的赞，贵族和平民一样的心上人.",
                        "公主有时似乎心情不好. 这样一个受祝福的人会像我们所有人一样有烦恼吗?",
                        "国王的骑士们都发誓要保护他和他的家人. 他们的指挥官看起来像是阿里奥斯亲手造的. 他是一个非常热心和忠诚的人.",
                        "我听说城堡里有个大人物几天前被谋杀了. 他们正试图掩盖此事，但似乎麻烦正在酝酿之中.",
                        "有些古代武器威力巨大. 我不知道怎样才能搞到这些东西?",
                        "当人们去青楼时，他们期待的不仅仅是幽会……好的服务总是受到赞赏.",
                        "现在这么多年轻女孩都变成了妓女的奴隶……有些人甚至自愿自首. 我想这是在困难时期获得食物和住所的一种方法.",
                        "那里的女孩太迷人了……我从来不知道做荡妇有这么大的好处. 让我质疑自己的道德品质!",
                        "所有的游客都同意一件事:赞最好的地方是它的性奴隶……任何一种性幻想都可以在这里实现. 许多奴隶以满足主人的欲望为傲.",
                        "在Zan城的女孩都很容易相处. 每天都会出现在同一个地方，和她们聊天，迟早她们会和你在一起.",
                        "那个女商人太性感了，伙计!如果我能说服她和我鬼混，我每天都会去那里买东西.",
                        "喜欢不寻常的性行为的人不太常见，但他们会付更多的钱.",
                        "前几天我路过这家青楼，看到一个粉红色头发的辣妹……但令人失望的是，我发现她不是工作人员.",
                        "经过一天的辛苦工作，有什么比去一个美女俱乐部，然后让她们中的一个脱光衣服，倒在你身上更性感呢?我理解你们的想法.",
                        "妓女就像性女神的女祭司，这是我爸爸常说的. 他通常喝得烂醉如泥.",
                        "个从西三月来的家伙搞不懂艺伎是什么. 他一直说他们就像普通的妓女. 我发誓，教育这些野蛮人是不可能的 .",
                        "我去了港口附近的一家小旅馆，要求好好按摩. 我真的有一个相好在那里…是不是很精彩?",
                    ]

    chapter_gossip = {1 : [
                            "你看到新的守卫制服了吗?他们用精美的丝绸装饰盔甲，而我们却在挨饿... ",
                            "我听说贫民窟附近有个秘密巢穴……小偷和强盗的避风港. 我一想到它就不寒而栗.",
                            "法拉队长是个贪婪的婊子. 她的人昨天来拜访我的一个朋友. 每个人都讨厌她，但他们说她在高层得到了保护.",
                            "守卫队长是法拉上尉.  如果你需要我的建议，最好留意他们.  征税和税收都是警卫所关心的.  如果你问我，他们只是在他们去的时候补上.",
                            "有人说，即使面对她自己的男人，守卫队长也显得贪婪......有些人说他们会做得更好.  也许他们的意思是他们会更好地不被抓住.",
                            "这些天小偷越来越大胆了. 真让人绝望啊. 听说守卫们好像什么都不想做.",
                            "我的邻居抱怨税收太高，所以他们拘留了他，从那以后就没人听说过他. 如果你想赚我的2金币，最好忍着点活下去.",
                            "守卫拿走了我的一切，但我能做什么?只有国王有更高的权威，他不会听平民的.",
                            "有人说，盗贼的行为很有组织，很像行会. 我不相信这种无稽之谈. 你见过一个小偷，除了动脑筋，什么都不懂?",
                            "这里的人们喜欢把他们所有的痛苦都归咎于一个秘密的莎莉娅阴谋集团，但是让我的眼睛告诉你:现在是我们热爱阿里奥斯的好队长在抢劫我们!",
                            "我一直听说城外有一家新青楼. 有机会真的得去看看.",
                          ],
                      2 : [
                            "这个城市最近发生了一连串的谋杀案. 不只是普通的乌合之众，他们还干掉了一些大人物.",
                            "人们说夜晚的街道不安全，雇佣刀锋四处游荡……如果没有伴游，很多富贵人家的孩子就不会出去了.",
                            "有人一直在一个接一个地消灭贵族……是时候有人开始为这座城市的正义而战了!",
                            "一个杀人凶手正在潜行……有人说他杀了高级法官，王室成员可能是下一个.",
                            "有人竟敢威胁我们亲爱的公主的生命?我希望他们抓住那个混蛋，挖出他的眼睛!",
                            "在这个城市里没有人是安全的，连法官也不安全. 是时候去乡下了，直到一切平静下来.",
                            "别担心那些杀手. 只有在大人物之后，才会有人花钱去暗杀像你我这样的小人物.",
                            "我听说过一群可怕的超人类隐形战士，他们在城市里四处寻找血腥和复仇... 他们自称{i}忍者{/i}.",
                            "忍者?真是胡说八道. 它们只存在于儿童故事中.",
                            "忍者是一个渗透到赞的嗜血刺客的秘密组织. 至少我听说是这样.",
                            "为什么有人会威胁公主的生命？ 她是唯一一个不希望我们在这个皇家毒蛇巢中患病的人.",
                            "在最近的谋杀浪潮中，贵族家庭付出了沉重的代价. 也许这场所谓的革命终究还是会到来?",
                            ],
                      3 : [],
                      4 : [],
                      5 : [],
                      6 : [],
                      7 : [
                          "你听说过传说中的青楼老板[MC.name]吗?我打赌他能把你妹妹变成一个性欲旺盛的女神.",
                          "[MC.name]是最好中的最好. 在整个Zan，没有比这更好的青楼老板了，以后也不会有了.",
                          "你知道国王的事吗?我是说，青楼之王?他是[MC.name],传说中的[brothel.name]老板...",
                          "镇上最好的青楼?你到底从哪里来?当然是[brothel.name]了!它比任何其他青楼都要先进好几法里. 竞争者们都已经放弃了.",
                          ],

                      # The following are added by the story

                      "c1_good" :   [
                                    "玛雅队长真是天赐之物. 相信我，她马上就会纠正守卫的行为的.",
                                    "前几天我被守卫拦住了. 我以为他们会像往常一样抢劫我，但他们只是很有礼貌例行检查完就放了我. 太令人惊讶了.",
                                    "最近许多老守卫被开除出警队. 看来这位新队长是认真在打击腐败.",
                                    "别告诉他是我说的，但很明显罗兹喜欢玛雅. 那个大笨蛋一点希望都没有...",
                                    ],
                      "c1_neutral" :[
                                    "新队长比老队长好吗?不管谁来负责，这里的一切都不会改变.",
                                    "莉迪队长看起来和老队长一样精明，但至少她保持低调. 激战对生意不好.",
                                    "听说贫民窟附近有个秘密巢穴……小偷和强盗的避风港. 我一想到它就不寒而栗.",
                                    "这些天小偷越来越大胆了. 真让人绝望啊. 听说守卫们好像什么都不想做.",
                                    "有人说，盗贼的行为很有组织，很像行会. 我不相信这种无稽之谈. 你见过一个小偷，除了动脑筋，什么都不懂?",
                                    ],
                      "c1_evil" : [
                                    "你看到新的护卫制服了吗?他们用精美的丝绸装饰盔甲，而我们却在挨饿..., "
                                    "法拉队长是个贪婪的婊子. 她的人昨天来拜访我的一个朋友. 每个人都讨厌她，但他们说她在高层得到了保护.",
                                    "守卫队长是法拉上尉.  如果你需要我的建议，最好留意他们.  征税和税收都是警卫所关心的.  如果你问我，他们只是在他们去的时候补上.",
                                    "有人说，即使面对她自己的男人，守卫队长也显得贪婪......有些人说他们会做得更好.  也许他们的意思是他们会更好地不被抓住.",
                                    "我的邻居抱怨税收太高，所以他们拘留了他，从那以后就没人听说过他. 如果你想赚我的2金币，最好忍着点活下去.",
                                    "守卫拿走了我的一切，但我能做什么?只有国王有更高的权威，他不会听平民的.",
                                    "这里的人们喜欢把他们所有的痛苦都归咎于一个秘密的莎莉娅阴谋集团，但是让我的眼睛告诉你:现在是我们热爱阿里奥斯的好队长在抢劫我们!",
                                    "法拉队长在贫民窟中比以往任何时候都更强大.  她现在完全无人反对，我们唯一的选择是付她的亲信.  你想死吗？?",
                                    "我原以为守卫的情况不会更糟，但事实确实如此. 他们抢劫了我的商店，强奸了我的妻子和女儿. 没有人敢动他们一根手指...",
                                  ],

                      "c2_kunoichi" :[
                                    "听说过'Kunoichi'吗？一个由忍者组成的秘密组织... 这真是太热了!",
                                    "我希望他们能抓住那些女魔头，即Kunoichi. 我听说他们与恶魔交媾. ",
                                    "不要相信你所听到的关于Kunoichi的消息. 他们是纯洁和高尚的战士.",
                                    "我听说某个忍者家族正在追捕城里的一个青楼老板...可怜的家伙，他已经死了.",
                                    "忍者? 我敢打赌，他们穿的衣服布料一定很少... 嗯...",
                                    "我读过一个关于忍者的故事，她们只用阴道就能杀人...我知道这很疯狂.",
                                    "当一个婴儿被遗弃时，有时一个忍者家族会收养她... 这是我所听说的.",
                                  ],

                      "c2_kunoichi_hunt" :[
                                    "{b}盗贼公会{/b}已经是个垃圾场了. 而现在那里也有忍者？",
                                    "忍者在{b}盗贼公会{/b}... 流氓们不会喜欢这个的.",
                                    "我告诉你，我在{b}盗贼公会{/b}看到一个孩子... 我本来想帮忙的，但后来我看到她有一个巨大的忍者星，所以我想还是算了.",
                                    "她看起来确实像个小屁孩，但她是个忍者，我告诉你! 站在{b}盗贼公会{/b}的屋顶上，也不例外.",

                                    "晚上我在{b}海滩{/b}边散步，看到了一个鬼魂! 一个美丽、苍白的女鬼. 她在水面上行走. 像一个忍者一样!"
                                    "我晚上去{b}海滩{/b}钓鳟鱼，我看到一位美丽的女士在月光下洗澡. 当我试图接近她时，她就像幽灵一样消失了!",
                                    "在{b}海滩{/b}附近曾发生过失踪事件. 有些人指责忍者，但那是幼稚的胡言乱语.",
                                    "于是，这位漂亮的女士挥了挥手，她周围的水就上升了，把她挡住了. 我们在{b}海滩{/b}上再也看不到她了，我们没有人敢冒险下海.",

                                    "我告诉你，她是一个忍者! 还有谁能像这样爬上{b}监狱{/b}的墙壁?",
                                    "这是最奇特的事情，女孩打了个响指，就引起了一阵颤动! {b}监狱{/b}的看守们一屁股坐在了地上.",
                                    "忍者为什么要跟踪{b}监狱{/b}? 任何罪犯都知道要避开我们善良的国王的监狱!",
                                    "别说了，根本就没有忍者在{b}监狱{/b}上面飞的事情! 现在去清理你的房间!",
                                  ],

                     }

    district_gossip = {"The Slums" : [
                                        "贫民窟里到处都是小偷，而守卫更可怕. 我迫不及待地想离开这个地方. 其他地方不可能有这么糟糕的情况!",
                                        "贫民窟最糟糕的事情是臭气熏天. 或者说第二糟糕的事情. 更糟的是，你可能因为一两银子而被割喉，再也闻不到任何东西.",
                                        "Zan的人民是邪恶的、堕落的和退化的，但他们肯定是勤奋的. 城市日渐壮大! 贫民窟是她的软肋.",
                                        "我在下水道里看到一个奇怪的女孩，她独自一人在那里. 我告诉她周围有怪物，但她只是微笑着说'我知道'",
                                        "下水道里充满了肮脏的小动物和怪物... 有些人甚至以猎杀它们为生.",
                                        "你见过那个奇怪的女孩吗，薇洛? 她的耳朵很奇怪，我想知道她是否是人类. 尽管她很可爱.",
                                        "农田里闹鬼. 不要去那里.",
                                        "国内总是有一些奇怪的事情发生. 我甚至听说有些女孩在那里与动物做爱.",
                                        "你在农场见过戈尔迪吗? 她是个可爱的年轻女子. 太悲哀了，她的家人发生了什么事.",
                                        "我通常会去农场向戈尔迪买牛奶. 她从她的奶牛那里得到的，但我更愿意给她挤奶，如果你明白我的意思...",
                                        "如果我想买动物，我当然会去农场买. 但我听说有些人的行为很奇怪.",
                                        "垃圾场里有个疯丫头，在垃圾堆里翻找{i}阿里奥斯{/i}. 我试图对她说些道理，但她根本不听我的.",
                                        "上周我做了一笔好买卖，把一个没用的旧玩意卖给了废品站的搞笑女孩.",
                                        "你见过吉娜吗? 垃圾场里的古怪科学家? 她购买和出售一些奇怪的机械. 让我起鸡皮疙瘩.",
                                        "贫民窟里的盗贼行会?无稽之谈. 守卫队长决不会允许的."
                                     ],
                       "The Docks" : ["冒险者联盟位于港口附近的某处. 腐烂的鱼腥味对于那些流氓来说并不反感.",
                                      "为什么海边有这么多青楼?是因为这里更潮湿吗?",
                                      "为什么码头上有这么多青楼?是因为听起来像“Dicks”吗?",
                                      "哪里有水手，哪里就有妓女. 这是就是现实生活.",
                                      "有一个女人在海边卖礼物. 她有一对巨大的...",
                                      "你见过那个穿红衣服在海边卖礼物的女人吗?她有很多礼物，一对超大的秘咪咪...",
                                      "他们在港口卖掉那些奇怪的奴隶，有一种长着马阳具的没有自我意识的奴隶......我的女朋友认为这很酷，但我发现那东西太令人毛骨悚然.",
                                      "港口附近的血群岛上有一些奴隶贩子. 他们对待人就像对待牛一样. 这肯定超有意思.",
                                      "*耳语*时髦的女士去港口买一些非常特殊的奴隶…我听说他们服从每个命令，他们有巨大的…* *耳语"
                                      "你见过港口边那个可怕的奴隶贩子吗?她让我神魂颠倒... ",
                                     ],
                       "The Warehouse" : [],
                       "The Magic Gardens" : [],
                       "The Cathedra" : [
                                        "大教堂是赞的骄傲，是克塞洛斯王冠上的宝石. 所有人都在阿里奥斯的光辉中欢欣鼓舞!",
                                        "教堂是一个安静沉思和祈祷的地方，但是现在，每天都有肮脏的朝圣者涌入，我不想再去那里了.",
                                        "毫无疑问，前往教堂的朝圣者的浪潮对生意是有好处的.",
                                        "从大教堂的狂热来看，你会认为阿里奥斯是唯一的神……我们很多人都不是阿里奥斯的追随者;他们似乎太容易忘记这一点了.",
                                        ],
                       "The King's Hold" : [
                                            "宫殿里的骑士都是爱唱咏叹调的好人. 那温暖了我的心.",
                                            "我听说国王学校有一个秘密的交换社团，成员们通宵狂欢交换妻子和女儿...",
                                            "贵族们在国王的城堡里漫步，就像一群秃鹰在空中盘旋，等待着下一顿美餐. 他们都认为自己可以生养下一个继承人，或者在国王去世后通过其他方式掌权...",
                                            ],
                       }




    ## JOKES ##
    ##笑话##

    jokes = {
             "harmless" : ("当守卫最难的是什么?告诉你的父母你是同性恋!", "我的狗过常去每个追骑在马上的人. 情况变得如此糟糕，我不得不把他的马带走.", "雪人和女雪人的区别是什么?雪球!", "你是怎么抓到胸罩的？带着陷阱.（看不懂的笑话...）"),
             "sex" : ("为什么卢斯老师被捕了?因为猥亵未成年...", "法院和阴户有什么共同之处?一失言，你就有大麻烦了.", "知道我在花园里做什么吗?把我的锄头弄脏.", "你把鸡巴周围没用的部分叫什么?一个男人!", "妻子和工作的区别是什么?5年后，你的工作仍然很糟糕."),
             "dark" : ("你怎么能让一个女孩尖叫两次?先操她的屁股，然后在她的窗帘上擦你的鸡巴!", "我喜欢我的女人喜欢我的酒…锁在地窖里!", "一位医生对他的病人说:“对不起，你的生命只剩下10了.'\n患者:'什么10? 月？周?'\n医生:'9, 8...'", "What’s the best part about sex with twenty-eight-year-olds? There are 20 of them!（这笑话翻了就看不明白了）", "有多少大男子主义者会给这盏灯添油? 一个也没有. 让她在黑暗中洗碗."),
             "mean" : ("我喜欢你. 人们说我没有品味，但我喜欢你.", "该死的，你很性感，但如果你闭嘴，你会更性感.（我没看明白）", "我喜欢我的女人有魅力，愚蠢，恶毒. 你似乎很符合要求.", "I'd hire you as a whore, but my girls have class...\n（还是个没看明白的笑话）...")
            }


    ## COMPLIMENTS ##
    ##赞美##

    compliments =  {
                    "beauty" : ("%s，你今天真漂亮...", "%s, 你太可爱了...", "%s, 我发誓你有最可爱的脸.", "当你微笑时，你的脸就会亮起来, %s."),
                    "body" : ("哇，你的身材真火辣.", "宝贝，你的屁股太棒了...", "我喜欢你的大咪咪，亲爱的，不穿胸罩看起来棒极了.", "看那漂亮的屁股...", "哇，你太棒了，真想用手去感受一下...!"),
                    "mind" : ("你是个聪明的女孩，我喜欢你这一点.", "美丽心灵……你不是样样都有了吗?", "你似乎知道很多…你一定要多了解我一些!", "我喜欢我们之间的对话，总是很有启发性的"),
                    "spirit" : ("你总是精神抖擞，充满活力;这非常好.", "算是个...个性的人. 我不喜欢沉闷的家伙.", "你总是对一切充满激情. 我喜欢这个!")
                    }


    ## GIRL BACKGROUND ##
    ##女孩故事##

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

    homes = ["宫廷", "茅屋", "公馆", "棚屋", "茅舍", "大房子", "小房子", "寺庙", "商店", "老房子", "塔楼", "教会"]

    guardians = ["父母", "爸爸", "妈妈", "叔叔", "奶奶", "阿姨", "爷爷", "哥哥", "姐姐", "弟弟", "妹妹", "导师"]

    hobbies = ["画画", "唱歌", "演奏音乐", "远足", "赌博", "购物", "阅读", "编织", "游泳", "写作"]

    colors = ["白色", "黄色", "红色", "绿色", "蓝色", "紫色", "橙色", "粉色", "黑色"]

    food = ["蛋糕", "奶油", "鱼", "水果", "肉", "饼干", "糖果", "巧克力", "面包", "米饭"]

    drinks = ["牛奶", "清酒", "葡萄酒", "啤酒", "苹果汁", "柠檬汁", "芒果汁", "香料水"]


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

                        "waitress_init" : "%s为%s位客人提供了酒水.",
                        "waitress_tags" : ["waitress"],
                        "waitress_tags2" : ["geisha"],

                        "dancer_stats" : (("body", 6), ("libido", 2), ("refinement", 1), ("charm",1)),
                        "dancer_changes" : ((("body",), 100, 3), (("libido",), 25, 2), (("constitution", "refinement", "charm"), 15, 1), (("obedience",), 15, -1)),

                        "dancer_init" : "%s为%s位客人提供了热舞服务.",
                        "dancer_tags" : ["dancer"],
                        "dancer_tags2" : ["profile", "fight"],

                        "masseuse_stats" : (("beauty", 6), ("sensitivity", 2), ("refinement", 1), ("body",1)),
                        "masseuse_changes" : ((("beauty",), 100, 3), (("sensitivity",), 25, 2), (("refinement", "body", "libido"), 15, 1), (("constitution",), 15, -1)),

                        "masseuse_init" : "%s为%s位客人进行了热情的按摩.",
                        "masseuse_tags" : ["masseuse"],
                        "masseuse_tags2" : ["swim"],

                        "geisha_stats" : (("refinement", 6), ("obedience", 2), ("beauty", 1), ("charm",1)),
                        "geisha_changes" : ((("refinement",), 100, 3), (("obedience",), 25, 2), (("beauty", "charm", "sensitivity"), 15, 1), (("libido",), 15, -1)),

                        "geisha_init" : "%s为%s位客人展示传统艺术.",
                        "geisha_tags" : ["geisha"],
                        "geisha_tags2" : ["waitress", "date"], # Date pictures can be used as substitutes for geisha

                        "waitress_very bad" : "\n{color=[c_red]}%s把饮料洒得到处都是，甚至没有道歉. 客户抱怨服务很糟糕.",
                        "waitress_bad" : "\n{color=[c_lightred]}%s又害羞又笨手笨脚的. 顾客抱怨她没服务好.",
                        "waitress_average" : "\n%s为大家服务并与顾客聊天. 他们认为她还不错.",
                        "waitress_good" : "\n{color=[c_lightgreen]}%s给顾客端饮料时与他们调情，这让她在客人中很受欢迎.",
                        "waitress_very good" : "\n{color=[c_green]}%s和客人们开着粗俗下流的玩笑，一边服务一边不经意间露出她的'本钱'. 每个人都喜欢她.",
                        "waitress_perfect" : "\n{color=[c_orange]}%s她今天没穿内裤上班，用她所有的魅力让客人们抓狂. 他们完全被她迷住了.",

                        "dancer_very bad" : "\n{color=[c_red]}%s笨手笨脚的. 她的舞跳得很糟糕，让人尴尬，顾客们对她发出嘘声，还朝她扔东西.",
                        "dancer_bad" : "\n{color=[c_lightred]}%s的舞蹈笨拙而无趣.",
                        "dancer_average" : "\n%s在顾客面前挑逗地跳舞.",
                        "dancer_good" : "\n{color=[c_lightgreen]}当%s在舞台上翩翩起舞时，俱乐部开始活跃起来.",
                        "dancer_very good" : "\n{color=[c_green]}当%s在舞台上跳舞脱衣时，人群变得疯狂起来，她在钢管上舞动，皮肤上的汗水闪闪发光.",
                        "dancer_perfect" : "\n{color=[c_orange]}她随着音乐挥手，慢慢地性感地脱下衣服，直到她赤身裸体地站在他们变态的目光下，顾客们的目光无法从%s身上移开.",

                        "masseuse_very bad" : "\n{color=[c_red]}%s笨手笨脚地到处跌跌撞撞，在这个过程中弄伤了不少人. 他们抱怨着叫她走开.",
                        "masseuse_bad" : "\n{color=[c_lightred]}%s试着给客人一个放松的摩擦. 她的技巧不够，顾客不满意.",
                        "masseuse_average" : "\n%s在温泉为客人提供按摩服务，帮助客人放松身心，感觉更加舒适.",
                        "masseuse_good" : "\n{color=[c_lightgreen]}%s和客人们一起泡在温泉里，只穿了一条毛巾，并给他们一个舒服的按摩. 她做完后，顾客们显然很兴奋.",
                        "masseuse_very good" : "\n{color=[c_green]}当%s给顾客进行热情的全身按摩时浴巾滑落. 她用手和舌头的样子使他们兴奋起来，他们等待着期待下一个轮到自己.",
                        "masseuse_perfect" : "\n{color=[c_orange]}%s裸体走进温泉，在客人中间磨蹭着他们的身体，直到他们上手抚摸她那白皙的皮肤.",

                        "geisha_very bad" : "\n{color=[c_red]}%s完全没有经过培训，给人的印象是笨手笨脚的. 客人们抱怨她只是一个打扮成艺伎的街头女孩.",
                        "geisha_bad" : "\n{color=[c_lightred]}%s在上茶的时候尽量表现得像个真正的艺伎;然而，任何人都知道她不是真的，客人很快就失去了兴趣.",
                        "geisha_average" : "\n%s弹奏了一曲三味线，之后与客人们聊天，帮助他们放松，忘记烦恼...",
                        "geisha_good" : "\n{color=[c_lightgreen]}%s为客人们表演茶道，互相寒暄，而她则漫不经心地让和服滑到一边，露出了雪腻的皮肤.",
                        "geisha_very good" : "\n{color=[c_green]}%s是这场派对的中心人物，她记得每一个客人的名字用于称赞他们. 她穿着一件短小而暴露的和服，与他们擦身而过，让他们都被她的香味所吸引.",
                        "geisha_perfect" : "\n{color=[c_orange]}%s就是艺伎的缩影，优雅、甜美、有天赋、机智、性感得要命. 她穿着一件几乎透明和服，扭动着露出乳沟和大腿，让顾客们为之疯狂.",

                        "flasher" : " 一位顾客怂恿她展示胸脯，她自豪地把胸脯展示给大家看.",
                        "temptress" : "她说服客人%s做一些“不一样”的尝试.",
                        "catgirl" : " 她一边咕噜着，一边急切地喝完客人的精液，舔干净他的鸡巴.",
                        "Virgin" : " 客人很惊讶她还是处女，为此额外付了钱.",
                        "virgin_group" : " 客人们很惊讶她还是处女，为此都额外付了钱.",
                        "reroll" : " 她惊险的逃过了一场大祸.",
                        "unlucky" : "",
                        "lucky" : "",
                        "random item" : " 客人%s留下了贵重的东西.",
                        "beauty bonus" : "客人%s发现她的美丽令人惊叹.",
                        "body bonus" : " 客人%s喜欢她的玲珑曲线.",
                        "charm bonus" : " 客人%s被她的魅力迷住了.",
                        "refinement bonus" : "  客人%s喜欢她的优雅.",
                        "libido bonus" : " 客人%s认为她很火热.",
                        "obedience bonus" : " 客人%s喜欢她的乖巧.",
                        "constitution bonus" : "  客人%s认为她很健康.",
                        "sensitivity bonus" : " 客人%s喜欢她敏感的身子.",

                        "DT_group" : " 客人们轮流把他们的鸡巴尽可能深地塞进她的喉咙里.",
                        "DT" : " 客人很惊讶发现竟然能把他的鸡巴插到她的喉咙那么深的位置.",
                        "bukkake" : " 她的每个洞都被狠干了一番，然后客人们轮番射到她的脸上.",
                        "creampie" : " 他深深插进她的阴道甚至直达腹部，而她一直没停下那高亢地呻吟.",
                        "creampie_group" : " 他们轮流狠操着她的小穴，直到那儿不停地溢出一股股精液.",
                        "anal creampie" : " 他狠狠地操了她的屁股，然后在她的屁股来了一发.",
                        "anal creampie_group" : " 他们轮流操她的屁股，直到她的肚子被精液撑起来像是怀孕了...",
                        "cum on face" : " 他呻吟着，把她的脸和头发都弄得乱七八糟.",
                        "cum on face_group" : " 他们呻吟着，在她的脸上和头发上堆积了很多东西...",
                        "swallow" : " 她急切地吞下了顺着喉咙流下来的精液.",
                        "irrumatio" : "",

                        "not satisfied" : " :Pron:很失望，她不愿意做:pron:想做的事.",
                        "group not satisfied" : " 她不愿意做，但他们不介意，因为小组%s很火爆.",
                        "bisexual not satisfied" : " 最后:pron:得到了%s，但:pron:很高兴让女孩们有自己的方式.",

                        "roll_critical failure" : "{color=[c_red]}%s今天没有努力. 她几乎没有注意到自己在做什么.{/color}",
                        "roll_failure" : "%s并没有真正投入其中.",
                        "roll_neutral" : "%s照常开展工作.",
                        "roll_success" : "%s今天真的很有动力.",
                        "roll_critical success" : "{color=[c_green]}%s尽其所能取悦的取悦别人.{/color}",

                        "bisexual_roll_critical failure" : "{color=[c_red]}%s今天没有努力. 她们没有注意到她们在做什么.{/color}",
                        "bisexual_roll_failure" : "%s并没有真正投入其中.",
                        "bisexual_roll_neutral" : "%s像往常一样做她们的工作.",
                        "bisexual_roll_success" : "今天%s很有动力也很有趣.",
                        "bisexual_roll_critical success" : "{color=[c_green]}%s竭尽全力取悦客人和彼此.{/color}",

                        "anal_stats" : (("anal", 6), ("constitution", 2), ("body", 1), ("sex",1)),
                        "anal_changes" : ((("anal",), 100, 3), (("constitution",), 50, 2), (("libido", "obedience", "body"), 25, 1), (("sensitivity",), 25, -1)),
                        "anal_init" : " :Pron:想干%s的屁股.",
                        "anal_tags" : ["anal"],

                        "sex_stats" : (("sex", 6), ("libido", 2), ("beauty", 1), ("service",1)),
                        "sex_changes" : ((("sex",), 100, 3), (("libido",), 50, 2), (("sensitivity", "constitution", "beauty"), 25, 1), (("obedience",), 25, -1)),
                        "sex_init" : " :Pron:想和%s做爱.",
                        "sex_tags" : ["sex"],

                        "service_stats" : (("service", 6), ("sensitivity", 2), ("charm", 1), ("fetish",1)),
                        "service_changes" : ((("service",), 100, 3), (("sensitivity",), 50, 2), (("obedience", "libido", "charm"), 25, 1), (("constitution",), 25, -1)),
                        "service_init" : " :Pron:希望%s能提供服务.",
                        "service_tags" : ["service"],

                        "fetish_stats" : (("fetish", 6), ("obedience", 2), ("refinement", 1), ("anal",1)),
                        "fetish_changes" : ((("fetish",), 100, 3), (("obedience",), 50, 2), (("constitution", "sensitivity", "refinement"), 25, 1), (("libido",), 25, -1)),
                        "fetish_init" : " :Pron:对%s有一些非常变态的要求.",
                        "fetish_tags" : ["fetish"],

                        "whore_init" : "%s来到你的青楼，选择了%s.",
                        "bisexual_tags" : ["bisexual"],
                        "group_tags" : ["group"],

                        "M anal_very bad" : "\n{color=[c_red]}%s经历了一段艰难的时光，一点也不喜欢. 顾客很快就失去了兴趣，抱怨着离开了.",
                        "M anal_bad" : "\n{color=[c_lightred]}%s不喜欢肛交. 她玩得不开心，客人也不开心.",
                        "M anal_average" : "\n%s被客人插她的屁股时，她就会呻吟. 她正在成长，慢慢开始享受肛交.",
                        "M anal_good" : "\n{color=[c_lightgreen]}%s发出快乐的呻吟并掰开自己的屁股. 客人满脸笑容地齐根插进了她的肛门.",
                        "M anal_very good" : "\n{color=[c_green]}%s看来天生就是肛交的料. 她用她的屁股来磨蹭客人的鸡巴，直到它像岩石一样坚硬，接着邀请他插入并满满射入精华.",
                        "M anal_perfect" : "\n{color=[c_orange]}%s绝对是肛交女神. 她肆无忌惮的大喊大叫，亢奋地掰开屁股，直到客人把种子射进了她的肚子.",

                        "M sex_very bad" : "\n{color=[c_red]}%s是一个糟糕的外行.当客人侵犯着她的身体时，她一点也不配合. 客人觉得她技术太烂了，抱怨着离去.",
                        "M sex_bad" : "\n{color=[c_lightred]}%s尽力给客人一段美好的时光, 但她的呻吟“表演”太假了. 客户松了一口气，但很失望.",
                        "M sex_average" : "\n%s与客人做爱时一起尝试着一些有趣的姿势. 她自己也开始享受，她的一些呻吟显然不是假的.",
                        "M sex_good" : "\n{color=[c_lightgreen]}在经过一场快速的前戏后, %s和客人在不同的位置上都来了场疯狂的性交，直到他的鸡巴完全硬不起来.",
                        "M sex_very good" : "\n{color=[c_green]}%s像个欲火中烧的魅魔一般疯狂榨取着客人的鸡巴. 直到客人把火热的精液注入她体内时，她在大叫中达到了高潮.",
                        "M sex_perfect" : "\n{color=[c_orange]}%s大声尖叫着一直无法得到满足，因为她喜欢更多的高潮和被客人的精液完全填满.",

                        "M service_very bad" : "\n{color=[c_red]}客人抱怨%s不知道如何正常工作. 他离开了，因为她甚至没能摸到对方的手而难过.",
                        "M service_bad" : "\n{color=[c_lightred]}%s笨拙地试图为客人服务，但她的技巧显然是欠缺的. 当她羞愧地看着他时，他结束了手淫.",
                        "M service_average" : "\n%s尽力为客人服务，慢慢发展自己的技术. 在逗了客人一会儿之后，她笑了，因为他把精华全喷射到了她的脸上.",
                        "M service_good" : "\n{color=[c_lightgreen]}%s使用她的技巧使客人重复地高潮，直到精液完全覆盖她的脸和裸露的胸口.",
                        "M service_very good" : "\n{color=[c_green]}%s开始一边吮吸一边舔着客人坚硬的大屌时，他自己已经湿透了. 客人没坚持多久，直接在它口中爆发.",
                        "M service_perfect" : "\n{color=[c_orange]}%s一边把自己的身体给客人玩，一边熟练地吮吸，只听见从她嘴边传出些含糊湿濡的声音. 她品尝着脸上和嘴里滚烫的、黏糊糊的精液，乞求客人再多给她一些.",

                        "M fetish_very bad" : "\n{color=[c_red]}%s在客人的触摸下感到害怕和紧张. 她一点也不喜欢这样，客人完全不满意地离开了.",
                        "M fetish_bad" : "\n{color=[c_lightred]}当客人对她的身体做新奇的事情时，%s一直发抖. 客人起初饶有兴趣地看着她的反应，但这种呆板的节奏很快就使他厌烦了.",
                        "M fetish_average" : "\n%s蒙着眼睛，被绑起来，呻吟了一声. 她似乎更好奇而不是害怕发生在她身上的事情，和客户玩一会儿很开心.",
                        "M fetish_good" : "\n{color=[c_lightgreen]}当%s感觉到粗糙的麻绳在她皮肤上的勒咬时，她兴奋得发抖. 客人持续的挑逗她的身体，直到她完全湿透，乞求被操.",
                        "M fetish_very good" : "\n{color=[c_green]}%s享受快乐并痛苦着的混合感觉，而且还顺从地请求得到更多. 客人在她被绑成一个耻辱姿势的时候狠狠地侵犯了她，使她达到高潮.",
                        "M fetish_perfect" : "\n{color=[c_orange]}%s喜欢客人对她所做的一切，并不断提出更新颖、更耻辱的方法来捆绑她和惩罚她. 她痛苦并快乐的尖叫着，一直在高潮中，只因为她的所有洞都在不停被侵犯.",

                        "M bisexual_very bad" : "\n{color=[c_red]}%s笨手笨脚的，相互间一点也不合作. 客人很快就厌烦了，抱怨退款的事.",
                        "M bisexual_bad" : "\n{color=[c_lightred]}很明显%s并不擅长这个，只是假装做秀而已. 客人轮换着地操她倆，却一直没什么感觉.",
                        "M bisexual_average" : "\n%s慢慢地抚摸着彼此阴部，而客人却在一旁贪婪地欣赏着. 他很快加入了她们，他们一起竭尽全力让这段时间成为难忘的时刻.",
                        "M bisexual_good" : "\n{color=[c_lightgreen]}%s热切地互相抚摸和取笑. 她们嬉戏着尝试用新的方法来激发客人的兴趣，在她们玩弄彼此的乳房和阴部时，他很快就泄了.",
                        "M bisexual_very good" : "\n{color=[c_green]}%s爱鸡巴就像爱着彼此一样. 她们一起手、嘴和身体来对付客人的鸡巴，使他对她们俯首称臣.",
                        "M bisexual_perfect" : "\n{color=[c_orange]}%s是完美的性感小猫，当客人在忙着干她们的每个洞的时候，她俩抓住时机熟练地舔弄对方的阴户. 她们热切地相互亲吻着对方，吮渡着对方嘴里的精液，而客人则满怀喜悦地欣赏着这一切.",

                        "group_very bad" : "\n{color=[c_red]}由于有太多的客人无法满足，%s似乎不知所措，不知道该怎么办. 这群人只留下不满和抱怨相继离开了.",
                        "group_bad" : "\n{color=[c_lightred]}%s在这群人中有点害羞. 她努力做好自己的工作，但客人们觉得她的表现相当平庸.",
                        "group_average" : "\n客人们轮流操着%s. 她全力以赴应对着每一个客人.",
                        "group_good" : "\n{color=[c_lightgreen]}%s努力取悦这群客人中的每一个，她的每个洞让他们完美地完成释放. 相信他们应该不会很快忘记的那一刻的.",
                        "group_very good" : "\n{color=[c_green]}%s被客人操了好长时间，看起来她还没准备好停下来. 不管他们操她多少次，她总是想再要一个鸡巴.",
                        "group_perfect" : "\n{color=[c_orange]}%s迫不及待地想让她的每一个洞都被客人填满，直到他们把精液喷射到她身体的每一寸才让他们休息.",

                        "F anal_very bad" : "\n{color=[c_red]}%s经历了一段艰难的时光，一点也不喜欢它. 客人很快就失去了兴趣，开始抱怨起来.",
                        "F anal_bad" : "\n{color=[c_lightred]}%s不喜欢肛交. 她玩得不开心，客人也不开心.",
                        "F anal_average" : "\n%s被客人插她的屁股时，她就会呻吟. 她正在成长，慢慢开始享受肛交.",
                        "F anal_good" : "\n{color=[c_lightgreen]}%s发出快乐的呻吟并掰开自己的屁股. 客人满脸笑容地齐根插进了她的肛门.",
                        "F anal_very good" : "\n{color=[c_green]}%s看来天生就是肛交的料. 她用她的屁股来磨蹭客人的鸡巴，直到它像岩石一样坚硬，接着邀请他插入并满满射入精华.",
                        "F anal_perfect" : "\n{color=[c_orange]}%s绝对是肛交女神. 她肆无忌惮的大喊大叫，亢奋地掰开屁股，直到客人把种子射进了她的肚子.",

                        "F sex_very bad" : "\n{color=[c_red]}%s是一个糟糕的外行.当客人侵犯着她的身体时，她一点也不配合. 客人觉得她技术太烂了，抱怨着离去.",
                        "F sex_bad" : "\n{color=[c_lightred]}%s尽力给客人一段美好的时光, 但她的呻吟“表演”太假了. 客户松了一口气，但很失望.",
                        "F sex_average" : "\n%s与客人做爱时一起尝试着一些有趣的姿势. 她自己也开始享受，她的一些呻吟显然不是假的.",
                        "F sex_good" : "\n{color=[c_lightgreen]}在经过一场快速的前戏后, %s 和客人在不同的位置上都来了场疯狂的性交，直到他的鸡巴完全硬不起来..",
                        "F sex_very good" : "\n{color=[c_green]}%s像个欲火中烧的魅魔一般疯狂榨取着客人的鸡巴. 直到客人把火热的精液注入她体内时，她在大叫中达到了高潮. ",
                        "F sex_perfect" : "\n{color=[c_orange]}%s大声尖叫着一直无法得到满足，因为她喜欢更多的高潮和被客人的精液完全填满.",

                        "F service_very bad" : "\n{color=[c_red]}客人抱怨%s不知道如何正常工作. 他离开了，因为她甚至没能摸到对方的手而难过.",
                        "F service_bad" : "\n{color=[c_lightred]}%s笨拙地试图为客人服务，但她的技巧显然是欠缺的. 当她羞愧地看着他时，他结束了手淫.",
                        "F service_average" : "\n%s尽力为客人服务，慢慢发展自己的技术. 在逗了客人一会儿之后，她笑了，因为他把精华全喷射到了她的脸上.",
                        "F service_good" : "\n{color=[c_lightgreen]}%s使用她的技巧使客人重复地高潮，直到精液完全覆盖她的脸和裸露的胸口.",
                        "F service_very good" : "\n{color=[c_green]}%s开始一边吮吸一边舔着客人坚硬的大屌时，他自己已经湿透了. 客人没坚持多久，直接在它口中爆发.",
                        "F service_perfect" : "\n{color=[c_orange]}%s一边把自己的身体给客人玩，一边熟练地吮吸，只听见从她嘴边传出些含糊湿濡的声音. 她品尝着脸上和嘴里滚烫的、黏糊糊的精液，乞求客人再多给她一些.",

                        "F fetish_very bad" : "\n{color=[c_red]}%s在客人的触摸下感到害怕和紧张. 她一点也不喜欢这样，客人完全不满意地离开了.",
                        "F fetish_bad" : "\n{color=[c_lightred]}当客人对她的身体做新奇的事情时，%s一直发抖. 客人起初饶有兴趣地看着她的反应，但这种呆板的节奏很快就使他厌烦了.",
                        "F fetish_average" : "\n%s蒙着眼睛，被绑起来，呻吟了一声. 她似乎更好奇而不是害怕发生在她身上的事情，和客户玩一会儿很开心.",
                        "F fetish_good" : "\n{color=[c_lightgreen]}当%s感觉到粗糙的麻绳在她皮肤上的勒咬时，她兴奋得发抖. 客人持续的挑逗她的身体，直到她完全湿透，乞求被操.",
                        "F fetish_very good" : "\n{color=[c_green]}%s享受快乐并痛苦着的混合感觉，而且还顺从地请求得到更多. 客人在她被绑成一个耻辱姿势的时候狠狠地侵犯了她，使她达到高潮.",
                        "F fetish_perfect" : "\n{color=[c_orange]}%s喜欢客人对她所做的一切，并不断提出更新颖、更耻辱的方法来捆绑她和惩罚她. 她痛苦并快乐的尖叫着，一直在高潮中，只因为她的所有洞都在不停被侵犯.",

                        "F bisexual_very bad" : "\n{color=[c_red]}%s笨手笨脚的，相互间一点也不合作. 客人很快就厌烦了，抱怨退款的事.",
                        "F bisexual_bad" : "\n{color=[c_lightred]}很明显%s并不擅长这个，只是假装做秀而已. 客人轮换着地操她倆，却一直没什么感觉.",
                        "F bisexual_average" : "\n%s慢慢地抚摸着彼此阴部，而客人却在一旁贪婪地欣赏着. 他很快加入了她们，他们一起竭尽全力让这段时间成为难忘的时刻.",
                        "F bisexual_good" : "\n{color=[c_lightgreen]}%s热切地互相抚摸和取笑. 她们嬉戏着尝试用新的方法来激发客人的兴趣，在她们玩弄彼此的乳房和阴部时，他很快就泄了.",
                        "F bisexual_very good" : "\n{color=[c_green]}%s爱鸡巴就像爱着彼此一样. 她们一起手、嘴和身体来对付客人的鸡巴，使他对她们俯首称臣.",
                        "F bisexual_perfect" : "\n{color=[c_orange]}%s是完美的性感小猫，当客人在忙着干她们的每个洞的时候，她俩抓住时机熟练地舔弄对方的阴户. 她们热切地相互亲吻着对方，吮渡着对方嘴里的精液，而客人则满怀喜悦地欣赏着这一切.",
                        }

    stat_increase_dict = {
                        "level" : "\n{color=[c_lightgreen]}等级提升{/color}",
                        "stat" : "\n%s {color=[c_green]}+%s{/color}",
                        "stat_neg" : "\n%s {color=[c_red]}%s{/color}",
                        "xp" : "\n经验 {color=[c_lightgreen]}+%s{/color}",
                        "xp_dark" : "\n经验 {color=[c_darkgreen]}+%s{/color}",
                        "jp" : "\n职业经验 {color=[c_orange]}+%s{/color}",
                        "gold+" : "\n金币 {color=[c_darkgold]}+%s{/color}",
                        "gold-" : "\n金币 {color=[c_darkgold]}%s{/color}",
                        "rep" : "\n人气 {color=[c_softpurple]}+%s{/color}",
                        "rep_neg" : "\n人气 {color=[c_red]}%s{/color}",
                        "job_up" : "\n{color=[c_orange]}工作技能等级提升{/color}",
                        "rank" : "\n{color=[c_softpurple]}阶级可提升{/color}"
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
                        "level" : "{color=[c_orange]}%s达到了一个新等级.{/color}",
                        "job_up" : "{color=[c_orange]}%s增加了她的 %s 技能.{/color}",
                        "rank" : "{color=[c_orange]}%s已经准备好提升阶级.{/color}"
                        }

    attraction_dict = {
                       "beauty_good" : "有张倾国倾城的脸",
                       "body_good" : "拥有完美的身材",
                       "charm_good" : "极有魅力",
                       "refinement_good" : "真的很典雅",
                       "beauty_bad" : "丑陋无比",
                       "body_bad" : "外表平平",
                       "charm_bad" : "是个令人讨厌的人",
                       "refinement_bad" : "是个粗暴野蛮的家伙"
                      }

    #### BROTHEL SERVICES ####

    maintenance_desc = {"clean" : "你的青楼 " + event_color["good"] % "{b}一尘不染{/b}" + ".",
                    "clean enough" : "你的青楼 " + event_color["a little good"] % "{b}足够干净{/b}" + ".",
                    "dusty" : "你的青楼" + event_color["average contrast"] % "{b}尘土飞扬{/b}" + ".",
                    "dirty" : "你的青楼" + event_color["a little bad"] % "{b}乌七八糟{/b}" + ".",
                    "disgusting" : "警告！你的青楼" + event_color["bad"] % "{b}不堪入目{/b}" + "!",
                    "fire" : event_color["very bad"] % "警告！！！你的青楼有着火的危险！"
                    }

    gold_threat_amount = {1 : 500, 2 : 1000, 3 : 2500, 4 : 10000, 5: 25000} # Gain 1 threat for every slice of X gold depending on DISTRICT RANK up to gold max

    gold_threat_max = {1 : 4, 2 : 12, 3 : 18, 4 : 24, 5: 30, 6 : 36, 7 : 52} # Max gold threat depending on CHAPTER



    #### ITEMS ####

    quality_prefix = {
                      "dress_0" : "E级 ",
                      "dress_1" : "D级 ",
                      "dress_2" : "C级 ",
                      "dress_3" : "B级 ",
                      "dress_4" : "A级 ",
                      "dress_5" : "S级 ",
                      "dress_6" : "X级 ",

                      "necklace_0" : "E级 ",
                      "necklace_1" : "D级 ",
                      "necklace_2" : "C级 ",
                      "necklace_3" : "B级 ",
                      "necklace_4" : "A级 ",
                      "necklace_5" : "S级 ",
                      "necklace_6" : "X级 ",

                      "ring_0" : "E级 ",
                      "ring_1" : "D级 ",
                      "ring_2" : "C级 ",
                      "ring_3" : "B级 ",
                      "ring_4" : "A级 ",
                      "ring_5" : "S级 ",
                      "ring_6" : "X级 ",

#                      "gift_1" : "Cheap ",
#                      "gift_2" : "Common ",
#                      "gift_3" : "Fine ",
#                      "gift_4" : "Rare ",

                      "food_0" : "E级 ",
                      "food_1" : "D级 ",
                      "food_2" : "C级 ",
                      "food_3" : "B级 ",
                      "food_4" : "A级 ",
                      "food_5" : "S级 ",
                      "food_6" : "X级 ",

#                      "accessory_1" : "Worn ",
#                      "accessory_2" : "Simple ",
#                      "accessory_3" : "Fine ",
#                      "accessory_4" : "Fancy ",
#                      "accessory_5" : "Enchanted ",

                      "scroll_0" : "D级 ",
                      "scroll_1" : "C级 ",
                      "scroll_2" : "B级 ",
                      "scroll_3" : "A级 ",
                      "scroll_4" : "S级 ",
                      "scroll_5" : "X级 ",

                      "misc_0" : "E级 ",
                      "misc_1" : "D级 ",
                      "misc_2" : "C级 ",
                      "misc_3" : "B级 ",
                      "misc_4" : "A级 ",
                      "misc_5" : "S级 ",
                      "misc_6" : "X级 "

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
                                 "有折扣" : "这个课程很便宜. 立即注册并享受更优惠的价格!",
                                 "大师班" : "这个班是由一位大师教的. 数据将比正常情况下增长更快.",
                                 "高报酬" : "这种任务的回报比以往更多.",
                                 "臭名昭著" : "这个任务完成后会带来额外的声望."
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
                    1 : "初级 ",
                    2 : "常规 ",
                    3 : "高级 ",
                    4 : "精英 ",
                    5 : "专家 "
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
                 "waitress0": "缺乏技能",
                 "waitress1": "新手女服务员",
                 "waitress2": "称职的服务员",
                 "waitress3": "熟练的酒吧女招待",
                 "waitress4": "专家酒吧女招待",
                 "waitress5": "酒馆女王",
                 "dancer0": "缺乏技能",
                 "dancer1": "初学者舞娘",
                 "dancer2": "称职的舞娘",
                 "dancer3": "熟练的脱衣舞女",
                 "dancer4": "专家级脱衣舞女",
                 "dancer5": "钢管舞女王",
                 "masseuse0": "缺乏技能",
                 "masseuse1": "新手按摩师",
                 "masseuse2": "称职的按摩师",
                 "masseuse3": "熟练的按摩女",
                 "masseuse4": "专家级按摩女",
                 "masseuse5": "泡姬女王",
                 "geisha0": "缺乏技能",
                 "geisha1": "新手舞姬",
                 "geisha2": "称职的舞姬",
                 "geisha3": "熟练的艺伎",
                 "geisha4": "专家级艺伎",
                 "geisha5": "花魁女王",
                 "sex0" : "缺乏技能",
                 "sex1" : "新手妓女",
                 "sex2" : "称职的妓女",
                 "sex3" : "熟练的娼妇",
                 "sex4" : "专家级娼妇",
                 "sex5" : "青楼女王",
                 "service0" : "缺乏技能",
                 "service1" : "新手手淫者",
                 "service2" : "称职的手淫者",
                 "service3" : "熟练的口交者",
                 "service4" : "专家级口交者",
                 "service5" : "口交女王",
                 "anal0" : "缺乏技能",
                 "anal1" : "新手肛交荡妇",
                 "anal2" : "称职的肛交荡妇",
                 "anal3" : "熟练的肛交情人",
                 "anal4" : "专家级肛交情人",
                 "anal5" : "肛交女王",
                 "fetish0" : "缺乏技能",
                 "fetish1" : "新手女仆",
                 "fetish2" : "称职的女仆",
                 "fetish3" : "熟练的伴游",
                 "fetish4" : "专家级贴身保镖",
                 "fetish5" : "结绳女王"
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

    contract_description = {"cruise" : ":ORG:正在组织一次夜间巡游:dis:以感谢其成员今年的辛勤工作. :AVEN:将在黄昏时分出发前往海湾观光，然后停泊在:LOC:旁边，享受一个娱乐之夜.",
                            "party" : ":ORG:正在:aven:附近举办一个奢华的派对. 所有在Zan的人都要参加，并一直狂欢到天亮之后.",
                            "ceremony" : ":ORG:选择了:aven:靠近:LOC:来庆祝他们众多的圣日之一. 为了更接近他们的神，崇拜者要超越精神和肉体，沉浸在最可耻的快乐中，用大量的圣酒洗去他们的罪孽，教会在现场很方便地出售这些圣酒.",
                            "festival" : ":ORG:下个月将在:dis:举办一个巨大的节日，以庆祝新的季节、三头牛、太阳再次升起，或其他一些乡下人的胡话. 不过，在:Aven:靠近:LOC:的地方会有一场大的盛宴，有食物、饮料、表演，当然还有女孩!",
                            "date" : ":ORG:已经邀请了几个朋友到:aven:旁边的:LOC:过夜，并要求有人陪伴. 仪容整洁、举止得体的女仆被期望照顾他的每一个需求.",
                            "meeting" : ":ORG:召集志同道合的贵族和外交官开会，讨论:ven:在:LOC附近的一个隐秘的地点. 虽然这一严肃话题的复杂性将占据他们的大部分时间，但他们也希望主人能提供一流的服务和'缓解'紧张的方法.",
                            "magic" : ":ORG:召集所有的奥术师在:LOC:参加一个有趣的魔法之夜. 在美女们的照顾下，客人们将在:aven:参加特别活动，俯瞰:DIS的壮丽景色.",
                            "orgy" : ":ORG:很高兴地宣布，在:LOC中，有一个漫长的享乐主义和色情惊喜的夜晚. 聚集在:aven:，客人们将与志同道合的人和精心挑选的精英性奴一起享受禁忌的快乐."}

init python:

    contract_templates = [Contract(type="cruise", district="The Docks", archetypes = ["The Player", "The Fox"],
                                   names=["海上之夜", "游览Zan的港湾", "退役的水手", "梦幻般的巡游"],
                                   organizers=["水手协会", "Zan的海军", "弗利布斯特社交俱乐部", "北方商船"],
                                   venues=["经过改装的大帆船", "私人垃圾", "王室游艇", "小型渔船队", "大型观光船"],
                                   character=sailor,
                                   MC_event_pic="events/brawl3.jpg",
                                  ),
                          Contract(type="party", district="The Cathedra", archetypes = ["The Maid", "The Slut"],
                                   names=["艰难聚会", "通宵达旦的'大教堂'乐队", "无耻派对", "从黄昏到黎明", "21点桌和妓女", "伙计，我的车在哪?"],
                                   organizers=["一位外国贵宾", "富有的贵族家庭", "公会间的协会", "来访的卡尔基尔高等法师", "国王的亲信", "富有的青楼老板", "兰尼斯特家族"],
                                   venues=["废弃的教堂", "著名的大屋", "花花公馆", "肮脏的小酒馆", "地下赌场"],
                                   character=party_girl,
                                   MC_event_pic="events/violent2.jpg",
                                  ),
                          Contract(type="ceremony", district="The Cathedra", archetypes = ["The Model", "The Bride"],
                                   names=["神圣的事迹", "宗教节日", "圣洁的典礼", "最神圣的聚会", "祷告之后"],
                                   organizers=["阿里奥斯的神圣教堂", "圣迪尔德奥修女会", "启蒙兄弟", "虔诚的兄弟会", "莎莉娅之友会", "老神棍联盟", "不可说的Yog'Gluglu的信徒们", "阿里奥斯的女祭司"],
                                   venues=["大修道院", "庄严的大教堂", "孤立无邻的寺庙", "宁静的闭关", "忘忧寺", "辉煌的教堂", "贫困孤儿院"],
                                   character=nun,
                                   MC_event_pic="events/monster assault.jpg",
                                  ),
                          Contract(type="festival", district="The Slums", archetypes = ["The Player", "The Fox"],
                                   names=["月光庆典", "乡村节庆", "季节问候", "乡间集市", "农贸市场", "珍贵的传统"],
                                   organizers=["矮胖子南瓜", "农民协会", "Zan的乡村俱乐部", "园艺兄弟会", "房东合作社", "来自山谷的肮脏嬉皮士", "牧羊人联合会"],
                                   venues=["前废品站", "大广场", "集市广场", "城门", "马路边"],
                                   character=kimono_lady,
                                   MC_event_pic="default/farm/sex beast (7).jpg",
                                  ),
                          Contract(type="date", district="The Magic Gardens", archetypes = ["The Bride", "The Model"],
                                   names=["浪漫约会", "寂寞的绅士", "贵族的顶楼", "俏佳人"],
                                   organizers=["卡利夫-布雷兹纳", "大祭司罗恩", "纳布科夫阁下", "瑞祥大师", "迪库伯爵", "粉红男爵", "杜克-努克姆", "公会会长菲利克斯"],
                                   character=young_maid,
                                   venues=["豪华顶层公寓", "乡间大屋", "老宅子", "家庭宫殿", "私人寺院", "热门度假村"],
                                   MC_event_pic="NPC/encounters/thief4.jpg",
                                  ),
                          Contract(type="meeting", district="The Warehouse", archetypes = ["The Courtesan", "The Maid"],
                                   names=["战略会晤", "权力的展示", "政治重逢", "重要的场合", "夸夸其谈的会议"],
                                   organizers=["Zanic市委员会", "反叛者联盟", "法罗一世陛下的政府", "奇形怪状的桌子的骑士们", "血岛盟会"],
                                   venues=["圣战进展情况", "军事合作", "更自由的性奴交易", "新的渔业条例", "对魔法武器储备的限制", "降低贵族出身的税收", "对穷人和赤贫者加税"], # Different use for venue for this particular contract
                                   character=diplomat,
                                   MC_event_pic="NPC/encounters/thief2.jpg", #impress1_5.jpg / quests/sex9.png
                                  ),
                          Contract(type="magic", district="The Magic Gardens", archetypes = ["The Escort", "The Courtesan"],
                                   names=["魔术：集会", "巫师年会", "神奇的科学博览会", "在魔法协会的乐趣", "魔法学校对决", "巫师请"],
                                   organizers=["高等法师Windoss", "关心女巫联盟", "亡灵巫师社交俱乐部", "Karkyr的长老们", "友好邻里的黑暗崇拜者"],
                                   venues=["闹鬼的庄园", "恐怖的旧房子", "高塔", "地下洞府", "最近开辟的恶魔之路", "尘封的书房"],
                                   character=sorceress,
                                   MC_event_pic="NPC/encounters/witches (1).webp",
                                  ),
                          Contract(type="orgy", district="The King's Hold", archetypes = ["The Slut", "The Escort"],
                                   names=["狂欢之夜", "淫荡的派对", "准备好迎接新的挑战", "单身汉日", "肮脏的欢乐之夜"],
                                   organizers=["情妇斯穆特凯蒂(Mistress Smutty Kitty)", "青楼老板奎恩", "大祭司罗恩", "阿里奥斯修女合唱团", "The Gimp", "胡克尔贸易联盟", "匿名的皇室成员", "富商", "高贵的女士"],
                                   venues=["神秘的林中空地", "吉普赛营地", "黑暗地牢", "颓废的宫殿", "淫荡的酒馆", "隐蔽的地下室", "被遗忘的寺庙"],
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
