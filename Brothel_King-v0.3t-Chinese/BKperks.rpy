#### BK PERKS ####
## Labels are used instead of Functions to make sure we are using global variables

init python:
        ## PERK ARCHETYPES ##
        archetype_dict = {"The Maid" : PerkArchetype("The Maid", "the maid.webp"),
                          "The Player" : PerkArchetype("The Player", "the player.webp"),
                          "The Model" : PerkArchetype("The Model", "the model.webp"),
                          "The Courtesan" : PerkArchetype("The Courtesan", "the courtesan.webp"),

                          "The Escort" : PerkArchetype("The Escort", "the escort.webp"),
                          "The Fox" : PerkArchetype("The Fox", "the fox.webp"),
                          "The Slut" : PerkArchetype("The Slut", "the slut.webp"),
                          "The Bride" : PerkArchetype("The Bride", "the bride.webp"),}

label init_perks():
    python:
        ## PERK DESCRIPTIONS ##

        perk_description = {
                             "女仆训练" : "'{i}我来为您做性处理了{/i}'",
                             "忠心耿耿" : "主人和仆人之间的纽带就是忠诚.",
                             "不辞辛劳" : "'{i}只要你全身心的投入，一切皆有可能.{/i}'",
                             "再接再厉" : "'{i}非常抱歉，让我再为您服务一次.{/i}'",
                             "劫后重生" : "她从地狱中归来, 为了满足主人她愿意奉献自己的肉体.",
                             "力臻完美" : "'{i}在主人射之前可不允许自己先高潮哦.{/i}'",

                             "兔装女郎" : "'{i}先生，你有我最爱吃的大萝卜吗?{/i}'",
                             "派对女郎" : "'{i}别急着走嘛，淫乱派对才刚刚开始...{/i}'",
                             "丰乳肥臀" : "这种性格的人很讨人喜欢，很容易就能哄到床上。",
                             "亲笔签名" : "追星族会为她的一切买单，穿过的丝袜，吃剩的蛋糕，还有洗澡水。",
                             "好出风头" : "全场的目光都集中在她身上，仿佛要撕碎她的衣服，她无比享受。",
                             "明星魅力" : "巨星登场，有人不远万里赶来只为了见她一面。",

                             "人体衣架" : "'{i}我必须得穿得这么羞耻吗?{/i}'",
                             "情爱磁场" : "她美丽的外表使她成为大众的宠儿，私下的配餐.",
                             "功成名就" : "潜规则而已，没有什么能阻止她成为赞城最好的模特.",
                             "眉目传情" : "在人们的面前忘记羞耻心，尽情展示你动人的身姿和肉体.",
                             "极致奢华" : "'{i}在天鹅绒大床和沙发上做爱，体验可是天上地下...{/i}'",
                             "选美皇后" : "她是大人物私下豢养的母狗，一切都不过是主人的任务罢了.",

                             "阿谀奉承" : "'{i}卡尔德兰伯爵刚刚来过...{/i}'",
                             "热情欢迎" : "'{i}你想不想要脱掉这些束缚... 更加舒服?{/i}'",
                             "品味高雅" : "'{i}更多，更多，你还能再来一发吗? 滴水之恩涌泉相报...{/i}'",
                             "五星消费" : "一分钱一分货，我保证让你物超所值.",
                             "天堂乐趣" : "'{i}我会让你体验从未有过的快乐...{/i}'",
                             "皇家待遇" : "'{i}今晚，你就是我的神明，让我为您献身...{/i}'",

                             "切实可用" : "{i}只要你能付得起价钱，我随时奉陪.{/i}",
                             "引人注目" : "{i}谁是一招鲜吃遍天的小母狗?{/i}",
                             "紧随其后" : "{i}就这点本事? 我还能再大战三百回合...{/i}",
                             "随叫随到" : "她还能再接一单，刚才那个很快就缴械投降了.",
                             "狂潮娇娃" : "'{i}嗯...你很持久嘛，试试这个姿势呢{/i}'",
                             "兢兢业业" : "对她来说不过是玩玩而已, 你不会动了真感情吧.",

                             "小狐狸精" : "'{i}别摸耳朵和尾巴，那里，嗯，不行！{/i}'",
                             "新鲜事物" : "'{i}听说在黑市有一种薄荷卖，它可以让猫娘瞬间发情...{/i}'",
                             "失物归还" : "'{i}他把一些珠宝落下了，他本来还想把这些塞进那里呢.{/i}'",
                             "不传之秘" : "她有独门绝技，人们都叫她榨汁机，她可以用尾巴缠住你的老二.",
                             "幸运冒险" : "她是幸运星，就算在危险期内射也不会怀孕...也许是生殖隔离？",
                             "招财福星" : "她就是青楼的财神!神仙的小穴滋味如何呢？",

                             "卖弄风骚" : "{i}想看看我不为人知的一面吗?{/i}",
                             "思想开放" : "'{i}不试试怎么知道你不喜欢呢?来陪人家玩一下嘛{/i}'",
                             "情迷意乱" : "'{i}你可以亲自给我指导一下吗?{/i}'",
                             "如狼似虎" : "'{i}每天都被肉棒顶到云端升仙!{/i}'",
                             "令人信服" : "'{i}今天给你特殊服务哦...{/i}'",
                             "一心二用" : "{i}吃完了简餐要来品尝品尝樱桃和鲍鱼吗？{/i}",

                             "新娘登场" : "我想把处女留给未来的丈夫，其他的不算失去贞洁.",
                             "助人为乐" : "'{i}有困难就来找我吧，我们都是好姐妹，除非你想和我抢这根肉棒.{/i}'",
                             "相互劝慰" : "'{i}好姐妹之间可没有秘密，来吧，脱下它让我们互相欣赏一下.{/i}'",
                             "以身作则" : "她可以给后辈指导各种方面，在浴缸里帮她们按摩.",
                             "医者之心" : "她把友情看的比生命还重要，为了朋友她什么都会做的",
                             "贞洁妓女" : "'{i}除了处女，我的一切都是您的... 我的心? 那就得看你能否征服我了...{/i}'",

                             "Naturist" : "这是...人体彩绘吗？能清楚的看到挺立的乳头和湿润的蜜穴，被人看到她就兴奋起来了",
                             "Ponygirl" : "她的身上只有项圈和尾巴. 尾巴是怎么固定住的... 可以免费宣传.",
                             "Bisexual" : "有时会和另一个姑娘在客人面前互相舔弄. 让客人更加满足，给更多小费, 还能缓解疲劳.",
                             "Group" : "三人行她也能搞定。可能会消耗额外的体力与最多两个客户发生性关系。",
                             "Orgy" : "真是个婊子!看来她想把每个洞都塞满。可能与最多三个顾客发生性关系，这将消耗更多的体力。",
                             }

        ## REGULAR PERKS ##

        perk_dict = {
                     "Maid Training" : Perk(name="女仆训练", type="level", perk_level=0, archetype="The Maid", effects=[Effect("change", "obedience", 5), Effect("change", "maintenance", 1, scope="brothel")], pic = "maid0.webp"),
                     "Loyalty" : Perk(name="忠心耿耿", type="level", perk_level=1, archetype="The Maid", effects=[Effect("change", "train obedience target", -10), Effect("change", "job obedience target", -10)], pic = "maid1_1.webp"),
                     "Hardworking" : Perk(name="不辞辛劳", type="level", perk_level=1, archetype="The Maid", effects=[Effect("boost", "upkeep", -0.15), Effect("boost", "waitress jp gains", 0.15)], pic = "maid1_2.webp"),
                     "Try Again" : Perk(name="再接再厉", type="level", perk_level=2, archetype="The Maid", effects=[Effect("reroll", "job critical failure", 1), Effect("boost", "xp gains", 0.05)], pic = "maid2_1.webp"),
                     "Survivor" : Perk(name="劫后重生", type="level", perk_level=2, archetype="The Maid", effects=[Effect("boost", "fear", 0.5), Effect("resist", "hurt", 3, dice=True)], pic = "maid2_2.webp"),
                     "Strive for Perfection" : Perk(name="力臻完美", type="level", perk_level=3, archetype="The Maid", effects=[Effect("boost", "all skill gains", 0.25), Effect("change", "brothel reputation", 5, scope="brothel", scales_with="rank")], pic = "maid3.webp"),

                     "Bunny Girl" : Perk(name="兔装女郎", type="level", perk_level=0, archetype="The Player", effects=[Effect("change", "body", 10), Effect("change", "advertising", 1, scope="brothel")], pic = "player0.webp"),
                     "Party Girl" : Perk(name="派对女郎", type="level", perk_level=1, archetype="The Player", effects=[Effect("change", "job customer capacity", 2), Effect("boost", "customer penalties", -0.5)], pic = "player1_1.webp"),
                     "Bimbo" : Perk(name="丰乳肥臀", type="level", perk_level=1, archetype="The Player", effects=[Effect("boost", "reputation gains", 0.15), Effect("boost", "dancer jp gains", 0.15)], pic = "player1_2.webp"),
                     "Autograph" : Perk(name="亲笔签名", type="level", perk_level=2, archetype="The Player", effects=[Effect("change", "tip", 1, scales_with="rep"), Effect("special", "job prestige", 1)], pic = "player2_1.webp"),
                     "Exhibitionist" : Perk(name="好出风头", type="level", perk_level=2, archetype="The Player", effects=[Effect("boost", "naked bonus", 0.15)], pic = "player2_2.webp"),
                     "Star Power" : Perk(name="明星魅力", type="level", perk_level=3, archetype="The Player", effects=[Effect("increase satisfaction", "all jobs", 1), Effect("increase satisfaction", "all sex acts", 1)], pic = "player3.webp"),

                     "Modeling 101" : Perk(name="人体衣架", type="level", perk_level=0, archetype="The Model", effects=[Effect("change", "beauty", 10), Effect("boost", "quest results", 0.2)], pic = "model0.webp"),
#                     "Rules of Attraction" : Perk(name="Rules of Attraction", type="level", perk_level=1, archetype="The Model", effects=[Effect("special", "BBCR bonus", 1, chance=0.25)], pic = "model1_1.webp"), # Shelving stat bonuses for now
                     "Rules of Attraction" : Perk(name="情爱磁场", type="level", perk_level=1, archetype="The Model", effects=[Effect("change", "customers", 3, dice=True, scope="brothel")], pic = "model1_1.webp"),
                     "Overachiever" : Perk(name="功成名就", type="level", perk_level=1, archetype="The Model", effects=[Effect("change", "all skill max", 10), Effect("boost", "masseuse jp gains", 0.15)], pic = "model1_2.webp"),
                     "Eye Contact" : Perk(name="眉目传情", type="level", perk_level=2, archetype="The Model", effects=[Effect("special", "lucky"), Effect("change", "brothel reputation", 50, chance=0.2, scope="brothel")], pic = "model2_1.webp"),
                     "Life of Luxury" : Perk(name="极致奢华", type="level", perk_level=2, archetype="The Model", effects=[Effect("special", "luxury"), Effect("change", "mood", 0.5, scales_with="equipped")], pic = "model2_2.webp"),
                     "Beauty Queen" : Perk(name="选美皇后", type="level", perk_level=3, archetype="The Model", effects=[Effect("change", "all main skills", 15), Effect("boost", "job customer budget", 1.0)], pic = "model3.webp"),

                     "Court relations" : Perk(name="阿谀奉承", type="level", perk_level=0, archetype="The Courtesan", effects=[Effect("change", "refinement", 10), Effect("increase satisfaction", "bisexual", 1)], pic = "courtesan0.webp"),
                     "Warm welcome" : Perk(name="热情欢迎", type="level", perk_level=1, archetype="The Courtesan", effects=[Effect("change", "first customer satisfaction", 1), Effect("boost", "half-shift resting bonus", 0.5)], pic = "courtesan1_1.webp"),
                     "Refined taste" : Perk(name="品味高雅", type="level", perk_level=1, archetype="The Courtesan", effects=[Effect("boost", "bisexual chance", 0.5), Effect("boost", "geisha jp gains", 0.15)], pic = "courtesan1_2.webp"),
                     "Five Stars" : Perk(name="五星消费", type="level", perk_level=2, archetype="The Courtesan", effects=[Effect("change", "total tip", 25, scales_with="customer satisfaction")], pic = "courtesan2_1.webp"),
                     "Heavenly Pleasures" : Perk(name="天堂乐趣", type="level", perk_level=2, archetype="The Courtesan", effects=[Effect("boost", "perfect result tip", 0.1), Effect("boost", "perfect result xp", 0.1), Effect("boost", "perfect result jp", 0.1)], pic = "courtesan2_2.webp"),
                     "Royal Treatment" : Perk(name="皇家待遇", type="level", perk_level=3, archetype="The Courtesan", effects=[Effect("boost", "first customer tip", 1.5), Effect("boost", "first customer rep", 2.5), Effect("boost", "whore customer budget", 1.0)], pic = "courtesan3.webp"),

                     "Available" : Perk(name="切实可用", type="level", perk_level=0, archetype="The Escort", effects=[Effect("change", "constitution", 5), Effect("increase satisfaction", "group", 1)], pic = "escort0.webp"),
#                     "Extras" : Perk(name="Extras", type="level", perk_level=1, archetype="The Escort", effects=[Effect("special", "LOCS bonus", 1, chance=0.25)], pic = "escort1_1.webp"), # Shelving stat bonuses for now
                     "Convincing" : Perk(name="令人信服", type="level", perk_level=1, archetype="The Escort", effects=[Effect("special", "temptress", 0.66)], pic = "slut2_2.webp"),
                     "On Call" : Perk(name="随叫随到", type="level", perk_level=1, archetype="The Escort", effects=[Effect("boost", "group chance", 0.5), Effect("change", "whore obedience target", -10)], pic = "escort2_1.webp"),
                     "Focus" : Perk(name="引人注目", type="level", perk_level=2, archetype="The Escort", effects=[Effect("special", "focus", 1)], pic = "escort1_1.webp"),
                     "Loves Sex" : Perk(name="如狼似虎", type="level", perk_level=2, archetype="The Escort", effects=[Effect("change", "all sex skills", 10)], pic = "slut2_1.webp"),
                     "Business and Pleasure" : Perk(name="兢兢业业", type="level", perk_level=3, archetype="The Escort", effects=[Effect("boost", "total tip", 0.01, scales_with="job cust nb"), Effect("boost", "total tip", 0.03, scales_with="whore cust nb"), Effect("change", "mood", 0.25, scales_with="cust nb")], pic = "escort3.webp"),

                     "Foxy Lady" : Perk(name="小狐狸精", type="level", perk_level=0, archetype="The Fox", effects=[Effect("change", "charm", 10), Effect("boost", "class results", 0.2)], pic = "fox0.webp"),
                     "Something New" : Perk(name="新鲜事物", type="level", perk_level=1, archetype="The Fox", effects=[Effect("boost", "xp gains", 1.0, chance=0.1), Effect("boost", "all jp gains", 1.0, chance=0.1)], pic = "fox1_1.webp"),
                     "Lost and Found" : Perk(name="失物归还", type="level", perk_level=1, archetype="The Fox", effects=[Effect("special", "random item", 1, chance=0.025)], pic = "fox1_2.webp", base_description = "'I'm sure he won't miss it.'"),
                     "Secret Admirers" : Perk(name="不传之秘", type="level", perk_level=2, archetype="The Fox", effects=[Effect("boost", "tip", 1, chance=0.2)], pic = "fox2_1.webp"),
                     "Tempting Fate" : Perk(name="幸运冒险", type="level", perk_level=2, archetype="The Fox", effects=[Effect("special", "effect chance", 1)], pic = "fox2_2.webp"),
                     "Stars Are Aligned" : Perk(name="招财福星", type="level", perk_level=3, archetype="The Fox", effects=[Effect("boost", "income", 1, chance=0.02, scope="brothel")], pic = "fox3.webp"),

                     "Teaser" : Perk(name="卖弄风骚", type="level", perk_level=0, archetype="The Slut", effects=[Effect("change", "libido", 5), Effect("gain", "positive fixation", 1)], pic = "slut0.webp"),
                     "Open mind" : Perk(name="思想开放", type="level", perk_level=1, archetype="The Slut", effects=[Effect("gain", "all sexual preferences", 250)], pic = "slut1_1.webp"),
                     "Bedroom Eyes" : Perk(name="情迷意乱", type="level", perk_level=1, archetype="The Slut", effects=[Effect("boost", "service jp bonus", 0.25), Effect("boost", "sex jp bonus", 0.25), Effect("boost", "anal jp bonus", 0.25), Effect("boost", "fetish jp bonus", 0.25)], pic = "slut1_2.webp"),
                     "Next" : Perk(name="紧随其后", type="level", perk_level=2, archetype="The Slut", effects=[Effect("change", "whore customer capacity", 1)], pic = "escort1_2.webp"),
                     "Work and Whore" : Perk(name="一心二用", type="level", perk_level=2, archetype="The Slut", effects=[Effect("special", "workwhore", 1)], pic = "slut3.webp"),
                     "Me So Horny" : Perk(name="狂潮娇娃", type="level", perk_level=3, archetype="The Slut", effects=[Effect("boost", "tiredness", -0.1)], pic = "escort2_2.webp"),

                     "Enter The Bride" : Perk(name="新娘登场", type="level", perk_level=0, archetype="The Bride", effects=[Effect("change", "sensitivity", 5), Effect("change", "security", 1, scope = "brothel")], pic = "bride0.webp"),
                     "Helping Hand" : Perk(name="助人为乐", type="level", perk_level=1, archetype="The Bride", effects=[Effect("change", "making friends", 1), Effect("boost", "mood gains from friendship", 0.5)], pic = "bride1_1.webp"),
                     "Confession" : Perk(name="相互劝慰", type="level", perk_level=1, archetype="The Bride", effects=[Effect("spillover", "xp", 0.2), Effect("spillover", "jp", 0.2)], pic = "bride1_2.webp"),
                     "Leading by Example" : Perk(name="以身作则", type="level", perk_level=2, archetype="The Bride", effects=[Effect("special", "skill catch up", 1)], pic = "bride2_1.webp"),
                     "The Healer" : Perk(name="医者之心", type="level", perk_level=2, archetype="The Bride", effects=[Effect("boost", "love gains", 0.5), Effect("change", "heal", 1, chance=0.33, scope="brothel")], pic = "bride2_2.webp"),
                     "The Virgin Whore" : Perk(name="贞洁妓女", type="level", perk_level=3, archetype="The Bride", effects=[Effect("boost", "virgin tip", 1), Effect("boost", "virgin rep", 1)], pic = "bride3.webp"),
                     }

        ## SPECIAL PERKS ##

        naked_perk = Perk("Naturist", type="sex", effects = [Effect("special", "naked", 1)])
        pony_perk = Perk("Ponygirl", type="sex", effects = [Effect("special", "ponygirl", 1.0, 0.5)])
        bis_perk = Perk("Bisexual", type="sex", effects = [Effect("special", "bisexual", 1.0, bis_chance)])
        group_perk = Perk("Group", type="sex", effects = [Effect("special", "group", 1.0, group_chance)])
        orgy_perk = Perk("Orgy", type="sex", effects = [Effect("special", "orgy", 1.0, 0.5)])



    return

#### END OF BK PERKS FILE ####
