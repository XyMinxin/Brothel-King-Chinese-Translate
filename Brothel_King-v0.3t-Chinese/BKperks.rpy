#### BK PERKS ####
## Labels are used instead of Functions to make sure we are using global variables

init python:
    ## PERK ARCHETYPES ##
    archetype_dict = {
                    "The Maid" : PerkArchetype(_("The Maid"), "the maid.webp"),
                    "The Player" : PerkArchetype(_("The Player"), "the player.webp"),
                    "The Model" : PerkArchetype(_("The Model"), "the model.webp"),
                    "The Courtesan" : PerkArchetype(_("The Courtesan"), "the courtesan.webp"),

                    "The Escort" : PerkArchetype(_("The Escort"), "the escort.webp"),
                    "The Fox" : PerkArchetype(_("The Fox"), "the fox.webp"),
                    "The Slut" : PerkArchetype(_("The Slut"), "the slut.webp"),
                    "The Bride" : PerkArchetype(_("The Bride"), "the bride.webp"),
                    }

label init_perks():
    python:
        ## PERK DESCRIPTIONS ##

        perk_description = {
                             "女仆之路" : "'{i}让我来侍奉您，主人{/i}'",
                             "主仆羁绊" : "主人和仆人之间的关系是神圣的",
                             "不辞辛劳" : "'{i}只要你全身心的投入，就不会感觉疲惫{/i}'",
                             "将功补过" : "'{i}非常抱歉，让我将功补过吧{/i}'",
                             "求生意志" : "在鬼门关里走过一遭后, 为了生存她愿意付出一切",
                             "完美主义" : "'{i}永远不要半途而废{/i}'",

                             "兔装女郎" : "'{i}谁能喂可怜的小兔子一根大胡萝卜?{/i}'",
                             "派对焦点" : "'{i}别急着走嘛，派对才刚刚开始...后面还有更刺激的{/i}'",
                             "丰乳肥臀" : "看她那前凸后翘的身材，衣服随时都会被撑开。",
                             "粉丝福利" : "在粉丝眼里她的一切都是完美的，她穿过的丝袜，吃剩的蛋糕，还有洗澡水都价值千金。",
                             "万众瞩目" : "她十分享受被人盯着的感觉，人越多她越兴奋，他们的目光就像触手一样在她身上缠绕。",
                             "天王巨星" : "巨星登场，有人不远万里赶来只为了见她一面。",

                             "人体衣架" : "'{i}我必须得穿这种暴露羞耻的衣服吗?{/i}'",
                             "大众情人" : "她美丽的外表使她成为大众的情人，宅男们都选她做配菜.",
                             "功成名就" : "只是被潜规则而已，没有什么能阻止她成为泽恩最好的模特.",
                             "暗送秋波" : "她的眼神望穿秋水，一个媚眼就能让小处男浑身颤抖，尽情展示她动人的身姿和肉体.",
                             "珠光宝气" : "'{i}你也想体验被富婆包养的感觉吗...{/i}'",
                             "选美冠军" : "在公众面前她是选美冠军，在背后她也只是某个大人物的玩物禁裔.",

                             "阿谀奉承" : "'{i}你看起来就像个贵族公子...{/i}'",
                             "宾至如归" : "'{i}来吧，让我们脱掉这些束缚，一起快活一下吧?{/i}'",
                             "品味高雅" : "'{i}别忘了喂饱我的姐妹，试试左右开弓，双管齐下...{/i}'",
                             "五星好评" : "一分钱一分货，可别吝啬你的消费哦.",
                             "飘飘欲仙" : "'{i}我会让你体验升天的快感...{/i}'",
                             "皇家体验" : "'{i}今晚，您就是我的国王陛下，让奴家好好伺候您...{/i}'",

                             "见钱眼开" : "{i}只要出得起钱，我就让你为所欲为.{/i}",
                             "引人注目" : "{i}所有人，都看着我，我要去了~啊~{/i}",
                             "欲海难填" : "{i}就这点本事? 我还能再大战三百回合...{/i}",
                             "随叫随到" : "她还能再接一单，刚才那个很快就缴械投降了.",
                             "淫娃荡妇" : "'{i}嗯...你很持久嘛，试试这个姿势呢{/i}'",
                             "乐在其中" : "对她来说不过是玩玩而已, 你不会动了真感情吧.",

                             "小狐狸精" : "'{i}别摸我的耳朵和尾巴，那里，嗯，不行！{/i}'",
                             "触类旁通" : "'{i}听说在黑市有一种神奇的薄荷叶，它可以让人瞬间发情...{/i}'",
                             "拾金有昧" : "'{i}他把一些珠宝落下了，他本来还想把这些塞进那里呢.{/i}'",
                             "不传之秘" : "这是她的独门绝技，人们都叫她榨汁姬，她可以用尾巴缠住你的肉棒.",
                             "幸运女神" : "她受幸运女神的庇佑，就算在危险期内射也不会怀孕...也许是生殖隔离？",
                             "招财进宝" : "她就是财富的象征!镀金的小穴滋味如何呢？",

                             "搔首弄姿" : "{i}想看看我不为人知的一面吗?{/i}",
                             "思想开放" : "'{i}要勇于尝试新鲜事物，不试试怎么知道呢？{/i}'",
                             "情迷意乱" : "'{i}你可以教教人家嘛?{/i}'",
                             "如狼似虎" : "'{i}啊!大肉棒！欧金金！快给我！{/i}'",
                             "巧舌如簧" : "'{i}今天给你特殊服务哦...{/i}'",
                             "一心二用" : "{i}吃完了甜点是不是该上主食了？{/i}",

                             "新娘修行" : "纯洁天真的少女更能勾起色狼的兴致",
                             "助人为乐" : "'{i}有困难就来找我吧，我们都是好姐妹{/i}'",
                             "同甘共苦" : "'{i}今日你我义结金兰，苟富贵，勿相忘{/i}'",
                             "以身作则" : "来，像我这样做，把手放到这里，嗯~没错",
                             "医者仁心" : "她把友情看的比生命还重要，为了朋友她什么都会做的",
                             "贞洁烈女" : "'{i}除了处女，我的一切都是您的... 您还想要我的心? 那就得看你的技术了...{/i}'",

                             "裸体主义" : "这是...人体彩绘吗？能清楚的看到挺立的乳头和湿润的蜜穴，这只会让她更加兴奋",
                             "雌牝母犬" : "她的身上只有项圈和尾巴. 尾巴是怎么固定住的... 可以起到免费的宣传效果",
                             "左拥右抱" : "有时会和另一个姑娘在客人面前互相舔弄. 让客人更加满足，给更多小费, 还能缓解疲劳.",
                             "前后夹击" : "三人行她也能搞定。可能会消耗额外的体力与最多两个客户发生性关系。",
                             "性欲旺盛" : "真是个婊子!看来她想把每个洞都塞满。可能与最多三个顾客发生性关系，这将消耗更多的体力。",
                             }

        ## REGULAR PERKS ##

        perk_dict = {
                        "Maid Training" : Perk(name=_("女仆之路"), type="level", perk_level=0, archetype="The Maid", effects=[Effect("change", "obedience", 5), Effect("change", "maintenance", 1, scope="brothel")], pic = "maid0.webp"),
                        "Loyalty" : Perk(name=_("主仆羁绊"), type="level", perk_level=1, archetype="The Maid", effects=[Effect("change", "train obedience target", -10), Effect("change", "job obedience target", -10)], pic = "maid1_1.webp"),
                        "Hardworking" : Perk(name=_("不辞辛劳"), type="level", perk_level=1, archetype="The Maid", effects=[Effect("boost", "upkeep", -0.15), Effect("boost", "waitress jp gains", 0.15)], pic = "maid1_2.webp"),
                        "Try Again" : Perk(name=_("将功补过"), type="level", perk_level=2, archetype="The Maid", effects=[Effect("reroll", "job critical failure", 1), Effect("boost", "xp gains", 0.05)], pic = "maid2_1.webp"),
                        "Survivor" : Perk(name=_("求生意志"), type="level", perk_level=2, archetype="The Maid", effects=[Effect("boost", "fear", 0.5), Effect("resist", "hurt", 3, dice=True)], pic = "maid2_2.webp"),
                        "Strive for Perfection" : Perk(name=_("完美主义"), type="level", perk_level=3, archetype="The Maid", effects=[Effect("boost", "all skill gains", 0.25), Effect("change", "brothel reputation", 5, scope="brothel", scales_with="rank")], pic = "maid3.webp"),

                        "Bunny Girl" : Perk(name=_("兔装女郎"), type="level", perk_level=0, archetype="The Player", effects=[Effect("change", "body", 10), Effect("change", "advertising", 1, scope="brothel")], pic = "player0.webp"),
                        "Party Girl" : Perk(name=_("派对焦点"), type="level", perk_level=1, archetype="The Player", effects=[Effect("change", "job customer capacity", 2), Effect("boost", "customer penalties", -0.5)], pic = "player1_1.webp"),
                        "Bimbo" : Perk(name=_("丰乳肥臀"), type="level", perk_level=1, archetype="The Player", effects=[Effect("boost", "reputation gains", 0.15), Effect("boost", "dancer jp gains", 0.15)], pic = "player1_2.webp"),
                        "Autograph" : Perk(name=_("粉丝福利"), type="level", perk_level=2, archetype="The Player", effects=[Effect("change", "tip", 1, scales_with="rep"), Effect("special", "job prestige", 1)], pic = "player2_1.webp"),
                        "Exhibitionist" : Perk(name=_("万众瞩目"), type="level", perk_level=2, archetype="The Player", effects=[Effect("boost", "naked bonus", 0.15)], pic = "player2_2.webp"),
                        "Star Power" : Perk(name=_("天王巨星"), type="level", perk_level=3, archetype="The Player", effects=[Effect("increase satisfaction", "all jobs", 1), Effect("increase satisfaction", "all sex acts", 1)], pic = "player3.webp"),

                        "Modeling 101" : Perk(name=_("人体衣架"), type="level", perk_level=0, archetype="The Model", effects=[Effect("change", "beauty", 10), Effect("boost", "quest results", 0.2)], pic = "model0.webp"),
                        #                     "Rules of Attraction" : Perk(name=_("Rules of Attraction"), type="level", perk_level=1, archetype="The Model", effects=[Effect("special", "BBCR bonus", 1, chance=0.25)], pic = "model1_1.webp"), # Shelving stat bonuses for now
                        "Rules of Attraction" : Perk(name=_("大众情人"), type="level", perk_level=1, archetype="The Model", effects=[Effect("change", "customers", 3, dice=True, scope="brothel")], pic = "model1_1.webp"),
                        "Overachiever" : Perk(name=_("功成名就"), type="level", perk_level=1, archetype="The Model", effects=[Effect("change", "all skill max", 10), Effect("boost", "masseuse jp gains", 0.15)], pic = "model1_2.webp"),
                        "Eye Contact" : Perk(name=_("暗送秋波"), type="level", perk_level=2, archetype="The Model", effects=[Effect("special", "lucky"), Effect("change", "brothel reputation", 50, chance=0.2, scope="brothel")], pic = "model2_1.webp"),
                        "Life of Luxury" : Perk(name=_("珠光宝气"), type="level", perk_level=2, archetype="The Model", effects=[Effect("special", "luxury"), Effect("change", "mood", 0.5, scales_with="equipped")], pic = "model2_2.webp"),
                        "Beauty Queen" : Perk(name=_("选美冠军"), type="level", perk_level=3, archetype="The Model", effects=[Effect("change", "all main skills", 15), Effect("boost", "job customer budget", 1.0)], pic = "model3.webp"),

                        "Court relations" : Perk(name=_("阿谀奉承"), type="level", perk_level=0, archetype="The Courtesan", effects=[Effect("change", "refinement", 10), Effect("increase satisfaction", "bisexual", 1)], pic = "courtesan0.webp"),
                        "Warm welcome" : Perk(name=_("宾至如归"), type="level", perk_level=1, archetype="The Courtesan", effects=[Effect("change", "first customer satisfaction", 1), Effect("boost", "half-shift resting bonus", 0.5)], pic = "courtesan1_1.webp"),
                        "Refined taste" : Perk(name=_("品味高雅"), type="level", perk_level=1, archetype="The Courtesan", effects=[Effect("boost", "bisexual chance", 0.5), Effect("boost", "geisha jp gains", 0.15)], pic = "courtesan1_2.webp"),
                        "Five Stars" : Perk(name=_("五星好评"), type="level", perk_level=2, archetype="The Courtesan", effects=[Effect("change", "total tip", 25, scales_with="customer satisfaction")], pic = "courtesan2_1.webp"),
                        "Heavenly Pleasures" : Perk(name=_("飘飘欲仙"), type="level", perk_level=2, archetype="The Courtesan", effects=[Effect("boost", "perfect result tip", 0.1), Effect("boost", "perfect result xp", 0.1), Effect("boost", "perfect result jp", 0.1)], pic = "courtesan2_2.webp"),
                        "Royal Treatment" : Perk(name=_("皇家体验"), type="level", perk_level=3, archetype="The Courtesan", effects=[Effect("boost", "first customer tip", 1.5), Effect("boost", "first customer rep", 2.5), Effect("boost", "whore customer budget", 1.0)], pic = "courtesan3.webp"),

                        "Available" : Perk(name=_("见钱眼开"), type="level", perk_level=0, archetype="The Escort", effects=[Effect("change", "constitution", 5), Effect("increase satisfaction", "group", 1)], pic = "escort0.webp"),
                        #                     "Extras" : Perk(name=_("Extras"), type="level", perk_level=1, archetype="The Escort", effects=[Effect("special", "LOCS bonus", 1, chance=0.25)], pic = "escort1_1.webp"), # Shelving stat bonuses for now
                        "Convincing" : Perk(name=_("引人注目"), type="level", perk_level=1, archetype="The Escort", effects=[Effect("special", "temptress", 0.66)], pic = "slut2_2.webp"),
                        "On Call" : Perk(name=_("欲海难填"), type="level", perk_level=1, archetype="The Escort", effects=[Effect("boost", "group chance", 0.5), Effect("change", "whore obedience target", -10)], pic = "escort2_1.webp"),
                        "Focus" : Perk(name=_("随叫随到"), type="level", perk_level=2, archetype="The Escort", effects=[Effect("special", "focus", 1)], pic = "escort1_1.webp"),
                        "Loves Sex" : Perk(name=_("淫娃荡妇"), type="level", perk_level=2, archetype="The Escort", effects=[Effect("change", "all sex skills", 10)], pic = "slut2_1.webp"),
                        "Business and Pleasure" : Perk(name=_("乐在其中"), type="level", perk_level=3, archetype="The Escort", effects=[Effect("boost", "total tip", 0.01, scales_with="job cust nb"), Effect("boost", "total tip", 0.03, scales_with="whore cust nb"), Effect("change", "mood", 0.25, scales_with="cust nb")], pic = "escort3.webp"),

                        "Foxy Lady" : Perk(name=_("小狐狸精"), type="level", perk_level=0, archetype="The Fox", effects=[Effect("change", "charm", 10), Effect("boost", "class results", 0.2)], pic = "fox0.webp"),
                        "Something New" : Perk(name=_("触类旁通"), type="level", perk_level=1, archetype="The Fox", effects=[Effect("boost", "xp gains", 1.0, chance=0.1), Effect("boost", "all jp gains", 1.0, chance=0.1)], pic = "fox1_1.webp"),
                        "Lost and Found" : Perk(name=_("拾金有昧"), type="level", perk_level=1, archetype="The Fox", effects=[Effect("special", "random item", 1, chance=0.025)], pic = "fox1_2.webp", base_description = "'I'm sure he won't miss it.'"),
                        "Secret Admirers" : Perk(name=_("不传之秘"), type="level", perk_level=2, archetype="The Fox", effects=[Effect("boost", "tip", 1, chance=0.2)], pic = "fox2_1.webp"),
                        "Tempting Fate" : Perk(name=_("幸运女神"), type="level", perk_level=2, archetype="The Fox", effects=[Effect("special", "effect chance", 1)], pic = "fox2_2.webp"),
                        "Stars Are Aligned" : Perk(name=_("招财进宝"), type="level", perk_level=3, archetype="The Fox", effects=[Effect("boost", "income", 1, chance=0.02, scope="brothel")], pic = "fox3.webp"),

                        "Teaser" : Perk(name=_("搔首弄姿"), type="level", perk_level=0, archetype="The Slut", effects=[Effect("change", "libido", 5), Effect("gain", "positive fixation", 1)], pic = "slut0.webp"),
                        "Open mind" : Perk(name=_("思想开放"), type="level", perk_level=1, archetype="The Slut", effects=[Effect("gain", "all sexual preferences", 250)], pic = "slut1_1.webp"),
                        "Bedroom Eyes" : Perk(name=_("情迷意乱"), type="level", perk_level=1, archetype="The Slut", effects=[Effect("boost", "service jp bonus", 0.25), Effect("boost", "sex jp bonus", 0.25), Effect("boost", "anal jp bonus", 0.25), Effect("boost", "fetish jp bonus", 0.25)], pic = "slut1_2.webp"),
                        "Next" : Perk(name=_("如狼似虎"), type="level", perk_level=2, archetype="The Slut", effects=[Effect("change", "whore customer capacity", 1)], pic = "escort1_2.webp"),
                        "Work and Whore" : Perk(name=_("巧舌如簧"), type="level", perk_level=2, archetype="The Slut", effects=[Effect("special", "workwhore", 1)], pic = "slut3.webp"),
                        "Me So Horny" : Perk(name=_("一心二用"), type="level", perk_level=3, archetype="The Slut", effects=[Effect("boost", "tiredness", -0.1)], pic = "escort2_2.webp"),

                        "Enter The Bride" : Perk(name=_("新娘修行"), type="level", perk_level=0, archetype="The Bride", effects=[Effect("change", "sensitivity", 5), Effect("change", "security", 1, scope = "brothel")], pic = "bride0.webp"),
                        "Helping Hand" : Perk(name=_("助人为乐"), type="level", perk_level=1, archetype="The Bride", effects=[Effect("change", "making friends", 1), Effect("boost", "mood gains from friendship", 0.5)], pic = "bride1_1.webp"),
                        "Confession" : Perk(name=_("同甘共苦"), type="level", perk_level=1, archetype="The Bride", effects=[Effect("spillover", "xp", 0.2), Effect("spillover", "jp", 0.2)], pic = "bride1_2.webp"),
                        "Leading by Example" : Perk(name=_("以身作则"), type="level", perk_level=2, archetype="The Bride", effects=[Effect("special", "skill catch up", 1)], pic = "bride2_1.webp"),
                        "The Healer" : Perk(name=_("医者仁心"), type="level", perk_level=2, archetype="The Bride", effects=[Effect("boost", "love gains", 0.5), Effect("change", "heal", 1, chance=0.33, scope="brothel")], pic = "bride2_2.webp"),
                        "The Virgin Whore" : Perk(name=_("贞洁烈女"), type="le)vel", perk_level=3, archetype="The Bride", effects=[Effect("boost", "virgin tip", 1), Effect("boost", "virgin rep", 1)], pic = "bride3.webp"),
                        }

        ## SPECIAL PERKS ##

        naked_perk = Perk("Naturist", type="sex", effects = [Effect("special", "naked", 1)])
        pony_perk = Perk("Ponygirl", type="sex", effects = [Effect("special", "ponygirl", 1.0, 0.5)])
        bis_perk = Perk("Bisexual", type="sex", effects = [Effect("special", "bisexual", 1.0, bis_chance)])
        group_perk = Perk("Group", type="sex", effects = [Effect("special", "group", 1.0, group_chance)])
        orgy_perk = Perk("Orgy", type="sex", effects = [Effect("special", "orgy", 1.0, 0.5)])



    return

#### END OF BK PERKS FILE ####
