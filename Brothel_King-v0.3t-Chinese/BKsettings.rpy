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
#### 翻译 ####

    ## Edit this dictionary to change the stat names that are displayed (change the right-hand text)

    ## 统计名词翻译 ##
    stat_name_dict = {
                        "Beauty" : "美貌",
                        "beauty" : "美貌",
                        "Body" : "身材",
                        "body" : "身材",
                        "Charm" : "魅力",
                        "charm" : "魅力",
                        "Refinement" : "优雅",
                        "refinement" : "优雅",
                        "Sensitivity" : "敏感",
                        "sensitivity" : "敏感",
                        "Libido" : "性欲",
                        "libido" : "性欲",
                        "Constitution" : "体格",
                        "constitution" : "体格",
                        "Obedience" : "服从",
                        "obedience" : "服从",
                        "Service" : "侍奉",
                        "service" : "侍奉",
                        "Sex" : "性交",
                        "sex" : "性交",
                        "Anal" : "肛交",
                        "anal" : "肛交",
                        "Fetish" : "调教",
                        "fetish" : "调教",
                        "Energy" : "精力",
                        "energy" : "精力",

                        "Brothel reputation" : "青楼声誉",
                        "brothel reputation" : "青楼声誉",

                        ## 玩家属性 ##
                        "Strength" : "力量",
                        "strength" : "力量",
                        "Spirit" : "法力",
                        "spirit" : "法力",
                        "Charisma" : "魅力",
                        "charisma" : "魅力",
                        "Speed" : "精力",
                        "speed" : "精力",
                    }

    ## 女孩相关 ##
    girl_related_dict = {
                        ## 统计名称 ##
                        "Beauty" : "美貌",
                        "beauty" : "美貌",
                        "Body" : "身材",
                        "body" : "身材",
                        "Charm" : "魅力",
                        "charm" : "魅力",
                        "Refinement" : "优雅",
                        "refinement" : "优雅",
                        "Sensitivity" : "敏感",
                        "sensitivity" : "敏感",
                        "Libido" : "性欲",
                        "libido" : "性欲",
                        "Constitution" : "体格",
                        "constitution" : "体格",
                        "Obedience" : "服从",
                        "obedience" : "服从",
                        "Service" : "侍奉",
                        "service" : "侍奉",
                        "Sex" : "性交",
                        "sex" : "性交",
                        "Anal" : "肛交",
                        "anal" : "肛交",
                        "Fetish" : "调教",
                        "fetish" : "调教",
                        "Energy" : "精力",
                        "energy" : "精力",

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
                        "Service" : "侍奉",
                        "service" : "侍奉",
                        "Sex" : "性交",
                        "sex" : "性交",
                        "Anal" : "肛交",
                        "anal" : "肛交",
                        "Fetish" : "调教",
                        "fetish" : "调教",
                        "Naked" : "露出",
                        "naked" : "露出",
                        "Group" : "群交",
                        "group" : "群交",
                        "Bisexual" : "百合",
                        "bisexual" : "百合",

                        ## 偏好 ##
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

                        ## 反应 ##
                        "ambivalent feelings" : "感到矛盾",
                        "a weakness" : "是她的弱点",
                        "a disgust" : "感到厌恶",
                        "no particular reaction" : "没什么特别的反应",

                        ## 癖好 ##
                        "Stripping" : "脱光衣服",
                        "stripping" : "脱光衣服",
                        "Public acts" : "公开play",
                        "public acts" : "公开play",
                        "Cosplay" : "穿着cosplay服装",
                        "cosplay" : "穿着cosplay服装",
                        "Dildos" : "使用假阳具",
                        "dildos" : "使用假阳具",
                        "Vibrators" : "使用跳蛋",
                        "vibrators" : "使用跳蛋",
                        "Dirty sex" : "就地性交",
                        "dirty sex" : "就地性交",
                        "Penis worship" : "服侍肉棒",
                        "penis worship" : "服侍肉棒",
                        "Bondage" : "麻绳束缚",
                        "bondage" : "麻绳束缚",
                        "Oil" : "精油按摩",
                        "oil" : "精油按摩",
                        "Wet" : "被淋湿",
                        "wet" : "被淋湿",
                        "Submission" : "羞辱",
                        "submission" : "羞辱",
                        "Femdom" : "女方主导",
                        "femdom" : "女方主导",
                        "Gags" : "戴上口塞",
                        "gags" : "戴上口塞",
                        "Strap-ons" : "穿戴阳具",
                        "strap-ons" : "穿戴阳具",
                        "Roleplay" : "角色扮演",
                        "roleplay" : "角色扮演",
                        "Plugs" : "使用肛塞",
                        "plugs" : "使用肛塞",
                        "Enemas" : "灌肠",
                        "enemas" : "灌肠",
                        "Beads" : "使用肛门拉珠",
                        "beads" : "使用肛门拉珠",

                        "Masturbation" : "自慰",
                        "masturbation" : "自慰",
                        "Fingering" : "手指插入",
                        "fingering" : "手指插入",
                        "Handjobs" : "手交",
                        "handjobs" : "手交",
                        "Cunnilingus" : "舔阴",
                        "cunnilingus" : "舔阴",
                        "Oral" : "口交",
                        "oral" : "口交",
                        "Irrumatio" : "强制口交",
                        "irrumatio" : "强制口交",
                        "Deep throat" : "深喉",
                        "deep throat" : "深喉",
                        "Titjobs" : "乳交",
                        "titjobs" : "乳交",
                        "Footjobs" : "足交",
                        "footjobs" : "足交",
                        "Double penetration" : "双穴插入",
                        "double penetration" : "双穴插入",
                        "Fisting" : "拳交",
                        "fisting" : "拳交",
                        "Insults" : "语言辱骂",
                        "insults" : "语言辱骂",
                        "69" : "69",
                        "Watersports" : "尿浴",
                        "watersports" : "尿浴",
                        "Ass-to-mouth" : "肛交后口交",
                        "ass-to-mouth" : "肛交后口交",
                        "Kissing" : "亲吻她",
                        "kissing" : "亲吻她",
                        "Spanking" : "打屁股",
                        "spanking" : "打屁股",
                        "Rimming" : "毒龙钻",
                        "rimming" : "毒龙钻",
                        "Fondling her boobs" : "抚弄乳房",
                        "fondling her boobs" : "抚弄乳房",
                        "Groping her ass" : "抚弄肛门",
                        "groping her ass" : "抚弄肛门",
                        "Lactation" : "强制泌乳",
                        "lactation" : "强制泌乳",
                        "Doggy style" : "后背位",
                        "doggy style" : "后背位",
                        "Cowgirl" : "骑乘位",
                        "cowgirl" : "骑乘位",
                        "Piledriver" : "抬单腿后背位",
                        "piledriver" : "抬单腿后背位",
                        "Spooning" : "侧身位",
                        "spooning" : "侧身位",

                        "Bukkake" : "多人颜射",
                        "bukkake" : "多人颜射",
                        "Cum in mouth" : "口暴",
                        "cum in mouth" : "口暴",
                        "Cum on face" : "颜射",
                        "cum on face" : "颜射",
                        "Cum in hair" : "射到头发上",
                        "cum in hair" : "射到头发上",
                        "Cum on body" : "射到身上",
                        "cum on body" : "射到身上",
                        "Cum shower" : "精子浴",
                        "cum shower" : "精子浴",
                        "Swallowing" : "深喉射",
                        "swallowing" : "深喉射",
                        "Creampie" : "外射",
                        "creampie" : "外射",
                        "Cum inside" : "内射",
                        "cum inside" : "内射",
                        "Multiple orgasms" : "多重高潮",
                        "multiple orgasms" : "多重高潮",
                        "Denied orgasm" : "禁止高潮",
                        "denied orgasm" : "禁止高潮",
                        "Squirting" : "潮吹",
                        "squirting" : "潮吹",

                        ## 杂项 ##
                        "Color" : "颜色",
                        "color" : "颜色",
                        "Food" : "食物",
                        "food" : "食物",
                        "Drink" : "饮料",
                        "drink" : "饮料",
                        None : "(girl_related_dict)没有值",
                        }

    ## 农场相关 ##
    farm_related_dict = {
                        ## 性行为 ##
                        "Service" : "侍奉",
                        "service" : "侍奉",
                        "Sex" : "性交",
                        "sex" : "性交",
                        "Anal" : "肛交",
                        "anal" : "肛交",
                        "Fetish" : "调教",
                        "fetish" : "调教",
                        "Naked" : "露出",
                        "naked" : "露出",
                        "Group" : "群交",
                        "group" : "群交",
                        "Bisexual" : "百合",
                        "bisexual" : "百合",

                        ## 农场奴仆 ##
                        "Stallion" : "种马",
                        "stallion" : "种马",
                        "Beast" : "野兽",
                        "beast" : "野兽",
                        "Monster" : "怪物",
                        "monster" : "怪物",
                        "Machine" : "机器",
                        "machine" : "机器",

                        ## 设施名称 ##
                        "Stables" : "种马马厮",
                        "stables" : "种马马厮",
                        "Pig stall" : "发情猪圈",
                        "pig stall" : "发情猪圈",
                        "Monster den" : "怪兽巢穴",
                        "monster den" : "怪兽巢穴",
                        "Workshop" : "机械工坊",
                        "workshop" : "机械工坊",

                        ## 反应 ##
                        "Refused" : "拒绝",
                        "refused" : "拒绝",
                        "Resisted" : "抵制",
                        "resisted" : "抵制",
                        "Accepted" : "接受",
                        "accepted" : "接受",

                        ## 训练态度 ##
                        "Soft" : "温和",
                        "soft" : "温和",
                        "Gentle" : "温和",
                        "gentle" : "温和",
                        "Hard" : "努力",
                        "hard" : "努力",
                        "Tough" : "强硬",
                        "tough" : "强硬",
                        "Hardest" : "强硬",
                        "hardest" : "强硬",
                        "Hardcore" : "硬核",
                        "hardcore" : "硬核",

                        ## 训练内容 ##
                        "Libido" : "照看仆役",
                        "libido" : "照看仆役",
                        "Sensitivity" : "服侍Gizel",
                        "sensitivity" : "服侍Gizel",
                        "Obedience" : "打扫农场",
                        "obedience" : "打扫农场",
                        "Constitution" : "外出工作",
                        "constitution" : "外出工作",
                        "Rest" : "休息",
                        "rest" : "休息",

                        ## 作息规则 ##
                        "Conservative" : "保守",
                        "conservative" : "保守",
                        "Intensive" : "高强度",
                        "intensive" : "高强度",
                        "No rest" : "无休息",
                        "no rest" : "无休息",

                        ## 行为反应 ##
                        "Reluctant" : "差强人意",
                        "reluctant" : "差强人意",
                        "Indifferent" : "淡然处之",
                        "indifferent" : "淡然处之",
                        "Interested" : "兴趣盎然",
                        "interested" : "兴趣盎然",
                        "Fascinated" : "神魂颠倒",
                        "fascinated" : "神魂颠倒",

                        ## 杂项 ##
                        "None" : "无",
                        "none" : "无",
                        "Auto" : "自动",
                        "auto" : "自动",
                        "No training" : "未安排训练",
                        "no training" : "未安排训练",
                        "Farm minion" : "农场奴仆",

                        "Service training" : "侍奉训练",
                        "service training" : "侍奉训练",
                        "Sex training" : "性交训练",
                        "sex training" : "性交训练",
                        "Anal training" : "肛交训练",
                        "anal training" : "肛交训练",
                        "Fetish training" : "调教训练",
                        "fetish training" : "调教训练",
                        "Naked training" : "露出训练",
                        "naked training" : "露出训练",
                        "Group training" : "群交训练",
                        "group training" : "群交训练",
                        "Bisexual training" : "百合训练",
                        "bisexual training" : "百合训练",
                        "Auto training" : "自动训练",
                        "auto training" : "自动训练",
                        }

    ## 结算界面 ##
    result_name_dict = {
                       ## 最终结果 ##
                       "very bad" : "非常糟糕",
                       "bad" : "糟糕",
                       "average" : "一般",
                       "good" : "不错",
                       "very good" : "非常好",
                       "perfect" : "完美",
                       }

    ## 按钮名字 ##
    button_name_dict = {
                        ## 一般选项 ##
                        "Back" : "返回",
                        "back" : "返回",
                        "Hide" : "隐藏",
                        "hide" : "隐藏",
                        "Close" : "关闭",
                        "close" : "关闭",
                        "Next" : "下一个",
                        "next" : "下一个",

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
    start_name_dict = {
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
                        }

    ## 特质树名称 ##
    archetype_name_dict = {
                          "The Maid" : "女仆",
                          "The Player" : "优伶",
                          "The Model" : "模特",
                          "The Courtesan" : "花魁",
                          "The Escort" : "伴游",
                          "The Fox" : "狐娘",
                          "The Slut" : "荡妇",
                          "The Bride" : "新娘"
                          }

    ## 互动界面 ##
    interact_name_dict = {
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

    ## 设置名称 ##
    setting_name_dict = {
                         ## 日期
                         "Monday" : "星期一",
                         "Tuesday" : "星期二",
                         "Wednesday" : "星期三",
                         "Thursday" : "星期四",
                         "Friday" : "星期五",
                         "Saturday" : "星期六",
                         "Sunday" : "星期天",

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

                         ## 状态名称 ##
                         "Away" : "离开",
                         "Farm" : "农场",
                         "Rest" : "休息",
                         "Scheduled" : "计划",
                         "Half-shift" : "半班制",
                         "Master bedroom" : "主人卧室",
                         "Work&whore" : "工作&妓女",
                         "Naked" : "裸体",
                         "Negative fixation" : "不良癖好",
                         "Not naked" : "非裸体",
                         "Not work&whore" : "没有工作",

                         ## 夜间活动设置 ##
                         "Normal" : "一般",
                         "Matchmaking" : "婚介",
                         "Customer" : "顾客",
                         "Level/Job/Rank up" : "等级/职业/阶级提升",
                         "Health/Security" : "健康/安全",
                         "Satisfaction report" : "满意报告",
                         "Farm" : "农场",
                         "Rest" : "休息",

                         ## 商店物品种类 ##
                         "MC" : "玩家",
                         "Mc" : "玩家",
                         "Girl" : "女孩",
                         "girl" : "女孩",
                         "Farm minion" : "农场奴仆",
                         "farm minion" : "农场奴仆",
                         "Minion" : "农场用品",
                         "minion" : "农场用品",
                         "Gift" : "礼物",
                         "gift" : "礼物",
                         "Decoration" : "饰品",
                         "decoration" : "饰品",
                         "Furnishing" : "家具",
                         "furnishing" : "家具",
                         "Utility" : "公用设施",
                         "utility" : "公用设施",
                         "Windows" : "窗户",
                         "windows" : "窗户",
                         "Comfort" : "慰藉用品",
                         "comfort" : "慰藉用品",
                         "Altars" : "祭坛",
                         "altars" : "祭坛",
                         "Gizmos" : "小玩意",
                         "gizmos" : "小玩意",

                         ## 排序名称 ##
                         "Weapon" : "武器",
                         "weapon" : "武器",
                         "Clothing" : "防具",
                         "clothing" : "防具",
                         "Trinket" : "饰品",
                         "trinket" : "饰品",
                         "Consumable" : "消耗品",
                         "consumable" : "消耗品",
                         "Misc" : "杂项",
                         "misc" : "杂项",

                         ## 客户群体 ##
                         "Beggars" : "乞丐类" ,
                         "beggars" : "乞丐类" ,
                         "Thugs" : "暴徒类",
                         "thugs" : "暴徒类",
                         "Laborers" : "劳工类",
                         "laborers" : "劳工类",
                         "Sailors" : "水手类",
                         "sailors" : "水手类",
                         "Commoners" : "平民类",
                         "commoners" : "平民类",
                         "Craftsmen": "工匠类",
                         "craftsmen": "工匠类",
                         "Bourgeois" : "中产阶级",
                         "bourgeois" : "中产阶级",
                         "Guild members" : "公会阶级",
                         "guild members" : "公会阶级",
                         "Patricians" : "骑士阶级",
                         "patricians" : "骑士阶级",
                         "Aristocrats" : "男爵阶级",
                         "aristocrats" : "男爵阶级",
                         "Nobles" : "伯爵阶级",
                         "nobles" : "伯爵阶级",
                         "Royals" : "国王阶级",
                         "royals" : "国王阶级",

                         ## 杂项 ##
                         "brothel" : "青楼",
                         "farm" : "农场",
                         "rank" : "阶级",
                         "act" : "工作",

                         "Mood" : "情绪",
                         "mood" : "情绪",
                         "Love" : "爱情",
                         "love" : "爱情",
                         "Fear" : "恐惧",
                         "fear" : "恐惧",
                         "Beauty" : "美貌",
                         "beauty" : "美貌",
                         "Body" : "身材",
                         "body" : "身材",
                         "Charm" : "魅力",
                         "charm" : "魅力",
                         "Refinement" : "优雅",
                         "refinement" : "优雅",
                         "Sensitivity" : "敏感",
                         "sensitivity" : "敏感",
                         "Libido" : "性欲",
                         "libido" : "性欲",
                         "Constitution" : "体格",
                         "constitution" : "体格",
                         "Obedience" : "服从",
                         "obedience" : "服从",
                         "Service" : "侍奉",
                         "service" : "侍奉",
                         "Sex" : "性交",
                         "sex" : "性交",
                         "Anal" : "肛交",
                         "anal" : "肛交",
                         "Fetish" : "调教",
                         "fetish" : "调教",
                         "Energy" : "精力",
                         "energy" : "精力",
                         }

    ## 访问城市界面 ##
    location_name_dict = {
                         ## 地区名称 ##
                         "The Slums" : "贫民窟",
                         "The Docks" : "码头区",
                         "The Warehouse" : "仓库区",
                         "The Magic Gardens" : "魔法花园",
                         "The Cathedra" : "教堂区",
                         "The King's Hold" : "国王城堡区",

                         "Spice market" : "香料市场",
                         "Sewers" : "下水道",
                         "Farm" : "农场",
                         "Watchtower" : "瞭望塔",
                         "Junkyard" : "垃圾场",
                         "Thieves guild" : "盗贼公会",

                         "Harbor" : "港口",
                         "Shipyard" : "船厂",
                         "Seafront" : "海滨",
                         "Beach" : "海滩",
                         "Taverns" : "酒馆",
                         "Exotic emporium" : "舶来品商场",

                         "Market" : "集市",
                         "Stables" : "牲畜棚",
                         "Plaza" : "广场",
                         "Gallows" : "绞刑架",
                         "Prison" : "监狱",
                         "Arena" : "竞技场",

                         "Botanical garden" : "植物园",
                         "Library" : "图书馆",
                         "Magic forest" : "魔法森林",
                         "Hanging gardens" : "空中花园",
                         "Guild quarter" : "公会区",
                         "Magic guild" : "魔法公会",

                         "Pilgrim road": "朝圣者之路",
                         "Banking quarter" : "银行区",
                         "Old ruins" : "古老的遗迹",
                         "Lakefront" : "湖畔",
                         "Training ground" : "训练场",
                         "Cathedra" : "教堂",

                         "Battlements" : "城垛",
                         "Keep" : "城堡主楼",
                         "Hall" : "门厅",
                         "Courtyard" : "庭院",
                         "Temple" : "庙宇",
                         "Waterfalls" : "瀑布",

                         ## 执照名称 ##
                         "No license" : "没有执照",
                         "Pimp license" : "皮条客执照",
                         "Whoremonger license" : "妓女贩执照",
                         "Brothelmaster license" : "青楼主执照",
                         }

    ## 特质名称 ##
    trait_name_dict = {
                       ## 黄金特质 ##
                       "Naughty" : "放荡不羁",
                       "Fascinating" : "得心应手",
                       "Lust" : "如狼似虎",
                       "Warrior" : "锐不可当",
                       "Skilled tongue" : "巧舌如簧",
                       "Always wet" : "欲壑难填",
                       "Tight ass" : "后门紧致",
                       "Playful" : "妙趣横生",
                       "Wild" : "桀骜不驯",
                       "Dirty mind" : "不知耻辱",
                       "Magnetic" : "财运亨通",
                       "Loose" : "肆无忌惮",
                       "Dedicated" : "兢兢业业",
                       "Provocative" : "妙语连珠",
                       "Fashionista" : "时尚达人",
                       "Perfectionist" : "精益求精",
                       "Elite" : "精明能干",
                       "Gifted" : "天赋异禀",
                       "Fast learner" : "举一反三",
                       "Caster" : "莫测高深",
                       "Driven" : "精力充沛",
                       "Country girl" : "乡下姑娘",
                       "Noble" : "大家风范",
                       "Naturist" : "返璞归真",
                       "Vicious" : "任情恣性",

                       ## 正面特质 ##
                       "Cute" : "率真可爱",
                       "Long legs" : "纤纤玉腿",
                       "Nice boobs" : "波涛汹涌",
                       "Juicy ass" : "蜂腰肥臀",
                       "Sweet" : "柔情蜜意",
                       "Exotic" : "异国风情",
                       "Polite" : "知书达理",
                       "Feminine" : "风姿绰约",
                       "Horny" : "天生媚骨",
                       "Resilient" : "精神焕发",
                       "Delicate" : "玉软花柔",
                       "Meek" : "温文尔雅",

                       "Pretty eyes" : "盈盈秋水",
                       "Firm tits" : "呼之欲出",
                       "Seductive" : "秀外慧中",
                       "Graceful" : "芳兰竟体",

                       "Beautiful" : "国色天香",
                       "Fit" : "长身玉立",
                       "Charming" : "妩媚多姿",
                       "Elegant" : "才望高雅",
                       "Slutty" : "天生媚骨",
                       "Athletic" : "刚劲有力",
                       "Sensitive" : "心细如发",
                       "Obedient" : "奴颜媚骨",

                       "Energetic" : "活力四射",
                       "Tough" : "钢筋铁骨",
                       "Sexy" : "人间尤物",
                       "Humble" : "戒奢宁俭",

                       "Virgin" : "白璧无瑕",
                       "Sharp" : "手不释卷",
                       "Loyal" : "心心相印",
                       "Brave" : "无所畏惧",
                       "Strong" : "身强力壮",
                       "Lucky" : "吉星高照",

                       "Deft" : "慧心灵性",
                       "Nimble" : "手脚麻利",
                       "Soft skin" : "肤如凝脂",
                       "Bright" : "如沐春风",
                       "Agile" : "眼明手捷",
                       "Brisk" : "身轻如燕",

                       "Rowdy" : "能言善辩",
                       "Powerful" : "搔首弄姿",
                       "Unhurried" : "从容不迫",
                       "Modest" : "典则俊雅",

                       "Sensual" : "声色犬马",
                       "Kinky" : "奇技淫巧",
                       "Pervert" : "自甘堕落",
                       "Thief" : "妙手空空",

                       ## 负面特质 ##
                       "Plain" : "臼头深目",
                       "Scars" : "遍体鳞伤",
                       "Mean" : "刁钻刻薄",
                       "Rude" : "鲁莽灭裂",
                       "Cold" : "冷若冰霜",
                       "Weak" : "瘦骨嶙峋",
                       "Rough" : "才短气粗",
                       "Defiant" : "目中无人",

                       "Scruffy" : "不修边幅",
                       "Plump" : "体态臃肿",
                       "Timid" : "烟视媚行",
                       "Vulgar" : "蛮横无理",
                       "Tame" : "百无聊赖",
                       "Frail" : "饱食终日",
                       "Jaded" : "多愁善感",
                       "Rebellious" : "顽冥不灵",

                       "Lazy" : "好吃懒做",
                       "Sickly" : "弱不禁风",
                       "Homely" : "相貌平平",
                       "Expensive" : "挥金如土",

                       "Slow" : "呆头呆脑",
                       "Distrustful" : "疑神疑鬼",
                       "Fearful" : "胆小如鼠",
                       "Vulnerable" : "不堪一击",
                       "Unlucky" : "命途多舛",

                       "All thumbs" : "笨手笨脚",
                       "Awkward" : "手忙脚乱",
                       "Brutal" : "揎拳捰袖",
                       "Dumb" : "拙嘴笨舌",
                       "Oafish" : "天生残疾",
                       "Clumsy" : "愚不可及",

                       "Prude" : "装腔作势",
                       "Naive" : "未经人事",
                       "Square" : "道貌岸然",

                       ## 特殊特质 ##
                       "Godless" : "敬而远之",
                       "Housebroken" : "恬不知耻",
                       "Teacher's pet" : "入室弟子",
                       "Trauma" : "黯然神伤",
                       "Farmgirl" : "农场之星",

                       ## 故事特质 ##
                       "Dynamo" : "Dynamo",
                       "Lolita" : "娇小玲珑",
                       "Ghost" : "野鬼孤魂",
                       "Stalwart" : "勇猛精进",

                       "Firebound" : "野火燎原",
                       "Voidbound" : "虚无缥缈",
                       "Waterbound" : "翻江倒海",
                       "Earthbound" : "地动山摇",
                       }

    ## 资源名称 ##
    resource_name_dict = {
                         "Gold" : "金币",
                         "gold" : "金币",
                         "Prestige" : "声望",
                         "prestige" : "声望",
                         "Action" : "行动力",
                         "action" : "行动力",
                         "Mana" : "魔法值",
                         "mana" : "魔法值",
                         "Wood" : "木头",
                         "wood" : "木头",
                         "Leather" : "皮革",
                         "leather" : "皮革",
                         "Dye" : "染料",
                         "dye" : "染料",
                         "Marble" : "大理石",
                         "marble" : "大理石",
                         "Ore" : "矿石",
                         "ore" : "矿石",
                         "Silk" : "丝绸",
                         "silk" : "丝绸",
                         "Diamond" : "钻石",
                         "diamond" : "钻石",
                         }

    ## 家具名称 ##
    furniture_name_dict = {
                          "Cardboard" : "纸板箱",
                          "Beer keg" : "啤酒桶",
                          "Basic painting" : "基础绘画",
                          "Model boat" : "船模",
                          "Hearth" : "壁炉",
                          "Fine painting" : "优秀的名画",
                          "Wine cases" : "酒箱",
                          "Model airship" : "模型飞船",
                          "Master painting" : "大师的画作",
                          "Sparkling fountain" : "气泡喷泉",
                          "Armorial bearings" : "纹章",
                          "Chapel" : "小礼拜堂",
                          "Small bar counter" : "小吧台",
                          "Polished bar counter" : "抛光吧台",
                          "Varnished bar counter" : "清漆吧台",
                          "Lacquered bar counter" : "镶边红漆吧台",
                          "Small washroom" : "小卫生间",
                          "Clean washroom" : "干净的卫生间",
                          "Hot washroom" : "有热水的卫生间",
                          "Luxurious washroom" : "豪华的卫生间",
                          "Small stage" : "小舞台",
                          "Amateur stage" : "业余舞台",
                          "Theatre stage" : "剧院舞台",
                          "Opera stage" : "歌剧舞台",
                          "Small tatami room" : "小席居",
                          "Fancy tatami room" : "花哨席居",
                          "Rare tatami room" : "华丽席居",
                          "Unique tatami room" : "雅致席居",
                          "Candy dispenser" : "糖果自助机",
                          "Ice cream dispenser" : "冰淇淋自助机",
                          "Lollipop dispenser" : "棒棒糖自助机",
                          "Magic mint dispenser" : "魔法薄荷自助机",
                          "Small erotica collection" : "小情色收藏架",
                          "Curious erotica collection" : "古怪的情色收藏架",
                          "Mysterious erotica collection" : "神秘的情色收藏架",
                          "Mindblowing erotica collection" : "激情四溢的情色收藏架",
                          "Painted venus" : "石膏维纳斯",
                          "Marble venus" : "大理石维纳斯",
                          "Veiled venus" : "戴面纱的维纳斯",
                          "Ardent venus" : "激情的维纳斯",
                          "Toy wooden horse" : "玩具木马",
                          "Spiked wooden horse" : "锯齿木马",
                          "Polished wooden horse" : "抛光的木马",
                          "Mobile wooden horse" : "活动木马",
                          "Basic outfit" : "基本套装",
                          "Shepherd outfit" : "牧羊女装束",
                          "Priestess outfit" : "祭司装束",
                          "Skimpy outfit" : "轻薄装束",
                          "Slutty outfit" : "性感装束",
                          "Kimono outfit" : "和服装束",
                          "Idol outfit" : "偶像装束",
                          "Basic door" : "普通门",
                          "Fence" : "栅栏",
                          "Small traps" : "小陷阱",
                          "Large traps" : "大陷阱",
                          "Alarm system" : "报警系统",
                          "Explosive traps" : "爆炸陷阱",
                          "Zap traps" : "即死陷阱",
                          "Basic broom" : "扫帚",
                          "Buckets" : "水桶",
                          "Wheelbarrow" : "手推车",
                          "Steam cart" : "汽车",
                          "Robot maid" : "机器人女仆",
                          "Wood statue" : "木头雕像",
                          "Marble statue" : "大理石雕像",
                          "Gold statue" : "黄金雕像",
                          "Platinum statue" : "白金雕像",
                          "Simple safe" : "简易保险箱",
                          "Locked safe" : "带锁的保险箱",
                          "Secure safe" : "坚固的保险箱",
                          "Unbreakable safe" : "牢不可破的保险箱",
                          "Glass window" : "玻璃窗",
                          "Persian window" : "波斯窗",
                          "Mirror" : "镜面窗",
                          "Red curtains" : "红色窗帘",
                          "Barred window" : "栅格窗",
                          "Double window" : "双视窗",
                          "Stained glass" : "彩色玻璃窗",
                          "Glass window XL" : "玻璃窗XL",
                          "Persian window XL" : "波斯窗XL",
                          "Mirror XL" : "镜面窗XL",
                          "Red curtains XL" : "红色窗帘XL",
                          "Barred window XL" : "栅格窗XL",
                          "Double window XL" : "双视窗XL",
                          "Stained glass XL" : "彩色玻璃窗XL",
                          "Washtub" : "洗澡盆",
                          "Bathtub" : "浴缸",
                          "Royal bathtub" : "皇家浴缸",
                          "Steam jacuzzi" : "蒸汽按摩浴缸",
                          "Simple bench" : "简陋长椅",
                          "Large bench" : "大长椅",
                          "Comfortable sofa" : "舒适的沙发",
                          "Royal sofa" : "皇家沙发",
                          "Comfortable bed" : "舒适的床",
                          "Queen size bed" : "皇后床",
                          "Shoddy Altar of Mana" : "简陋祭坛",
                          "Working Altar of Mana" : "运行的祭坛",
                          "Powerful Altar of Mana" : "神圣祭坛",
                          "Devastating Altar of Mana" : "死亡祭坛",
                          "Weapon rack" : "武器架",
                          "Weapon rack XL" : "武器架XL",
                          "Small dressing" : "小调味罐",
                          "Fancy dressing" : "精致的调味罐",
                          "Noble dressing" : "华贵的调味罐",
                          "Dim lights" : "暗光灯",
                          "Bright lights" : "强光灯",
                          "Simple Bookcase" : "简易的书架",
                          "Engraved Bookcase" : "精心雕刻的书架",
                          "Opulent Bookcase" : "富丽堂皇的书架",
                          "Lavish Bookcase" : "奢华阔气的书架",

                          "Strange machine" : "古怪的机器",
                          "Clockwork billboard" : "钟表广告牌",
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
                "零点酒吧" : "tavern.webp",
                "激情夜店" : "strip club.webp",
                "露天温泉" : "onsen.webp",
                "花坊剧场" : "okiya.webp",
                # Bedrooms
                "集体宿舍" : "basic room1.webp",
                "四人集宿" : "basic room2.webp",
                "单人宿舍" : "basic room3.webp",
                "标准客房" : "standard room1.webp",
                "复式套间" : "standard room2.webp",
                "商务套房" : "standard room3.webp",
                "豪华套房" : "rich room1.webp",
                "总统套房" : "rich room2.webp",
                "独栋别墅" : "rich room3.webp",
                "复式别墅" : "noble room1.webp",
                "花园洋楼" : "noble room2.webp",
                "公主寝宫" : "noble room3.webp",
                # Master bedroom
                "金屋藏娇" : "master/master0.webp",
                "一龙二凤" : "master/master1.webp",
                "三人成行" : "master/master2.webp",
                "淫乱派对" : "master/master3.webp",
                "皇室寝宫" : "master/master4.webp",
                "后宫三千" : "master/master5.webp",
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
    m_kunoichi = "public enemy no1.ogg"

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
    s_fire = "fire.ogg"
    s_fizzle = "fizzle.ogg"
    s_fiz = "fizzle.ogg"
    s_knock = "knocks.ogg"
    s_knocks = s_knock
    s_evil_laugh = "laugh.ogg"
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
    s_maniacal_laugh = "maniacal laugh.ogg"
    s_meow = "meow.ogg"
    s_mmh = "mmmh.ogg"
    s_mmmh = "mmmh.ogg"
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
