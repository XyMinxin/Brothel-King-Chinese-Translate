#### BK PERKS ####
## Labels are used instead of Functions to make sure we are using global variables

init python:
        ## PERK ARCHETYPES ##
        archetype_dict = {
                          "The Maid" : PerkArchetype("The Maid", "the maid.jpg"),
                          "The Player" : PerkArchetype("The Player", "the player.jpg"),
                          "The Model" : PerkArchetype("The Model", "the model.jpg"),
                          "The Courtesan" : PerkArchetype("The Courtesan", "the courtesan.jpg"),
                          "The Escort" : PerkArchetype("The Escort", "the escort.jpg"),
                          "The Fox" : PerkArchetype("The Fox", "the fox.jpg"),
                          "The Slut" : PerkArchetype("The Slut", "the slut.jpg"),
                          "The Bride" : PerkArchetype("The Bride", "the bride.jpg")
                          }

label init_perks():
    python:
        ## PERK DESCRIPTIONS ##

        perk_description = {
                             "女仆训练" : "'{i}我是来服务的.{/i}'",
                             "忠心耿耿" : "主人和仆人之间的关系是神圣的.",
                             "不辞辛劳" : "'{i}只要你用心去做，一切皆有可能.{/i}'",
                             "再接再厉" : "'{i}我很抱歉。让我来补偿你.{/i}'",
                             "劫后重生" : "她经历了地狱般的痛苦，她愿意付出一切.",
                             "力臻完美" : "'{i}不要半途而废.{/i}'",

                             "兔装女郎" : "'{i}主任!你有那胡萝卜给我吗?{/i}'",
                             "派对女郎" : "'{i}你想去哪儿?派对才刚刚开始……{/i}'",
                             "丰乳肥臀" : "拥有这些“资产”的人很容易成功.",
                             "亲笔签名" : "追星族是最好的小费来源.",
                             "好出风头" : "所有人的目光都集中在她身上，这就是她喜欢的.",
                             "明星魅力" : "一颗新星诞生了。人们从四面八方赶来只是为了看到她.",

                             "人体衣架" : "'{i}我真的要穿这个吗?{/i}'",
                             "情爱磁场" : "她天真的外表使她成为顾客的宠儿.",
                             "功成名就" : "没有什么能阻止她成为瓒城中最好的.",
                             "眉目传情" : "在这双眼睛里迷失自我，忘掉一切烦恼.",
                             "极致奢华" : "'{i}丝绸床单中的性爱总是更好……{/i}'",
                             "选美皇后" : "无人能比.",

                             "阿谀奉承" : "'{i}卡尔德兰伯爵就在这里……{/i}'",
                             "热情欢迎" : "'{i}你想不想来……放松一下?{/i}'",
                             "品味高雅" : "'{i}你能再给我一点吗?我知道如何感恩……{/i}'",
                             "五星消费" : "服务品质是有代价的.",
                             "天堂乐趣" : "'{i}我会给你从未体验过的快乐……{/i}'",
                             "皇家待遇" : "'{i}今晚，你将是我的国王……{/i}'",

                             "切实可用" : "{i}你具备所需的条件吗?我期待……{/i}",
                             "引人注目" : "{i}谁说我是个“一招鲜”?{/i}",
                             "紧随其后" : "{i}啊,完成了吗?我还可以接待更多的……{/i}",
                             "随叫随到" : "她有工作要做，而且做得很好.",
                             "狂潮娇娃" : "'{i}我爱你很久……{/i}'",
                             "兢兢业业" : "这都是她的工作。但是，天哪，她喜欢她的工作.",

                             "小狐狸精" : "'{i}见识过吗?{/i}'",
                             "新鲜事物" : "'{i}我在香料市场听说的……{/i}'",
                             "失物归还" : "'{i}也许我应该把它还给他，但我怎么才能找到他呢？可他已经在出口了.{/i}'",
                             "不传之秘" : "她有她的方式……她的常客很欣赏这一点.",
                             "幸运冒险" : "出生在幸运星下……",
                             "招财福星" : "她的存在是如此的有吸引力，她可以给整个青楼带来好运。紧紧抓住她!",

                             "卖弄风骚" : "{i}主人，你想多看看我吗?{/i}",
                             "思想开放" : "'{i}如果你从来没有尝试过，你怎么能说你不喜欢呢?{/i}'",
                             "情迷意乱" : "'{i}你能教我一些新东西吗?{/i}'",
                             "如狼似虎" : "'{i}我喜欢我所做的……整天被草根本不工作!{/i}'",
                             "令人信服" : "'{i}让我给你看一些特别的东西……{/i}'",
                             "一心二用" : "{i}让我们玩得开心!{/i}",

                             "新娘登场" : "代号:粉红色曼巴.",
                             "助人为乐" : "'{i}你可以随时依靠我。我们都是姐妹.{/i}'",
                             "相互劝慰" : "'{i}我们之间不应该有任何秘密.{/i}'",
                             "以身作则" : "她可以教其他女孩一两件事.",
                             "医者之心" : "她很关心别人，会尽她所能保护她爱的人",
                             "贞洁妓女" : "'{i}你可以对我做任何事，但这个地方是禁区……先生，你没事吧?都出汗了……{/i}'",

                             "Naturist" : "",
                             "Ponygirl" : "现在她只穿着一个暴露的马具和一条尾巴。猜猜它插在哪里……免费广告。",
                             "Bisexual" : "有时会为另一个双性恋女孩提供服务。极大地增加小费和客户满意度，减少疲劳。",
                             "Group" : "与客户进行三人行为对她来说不是什么难事。可能与最多两名客户发生性行为，代价是额外的疲劳。",
                             "Orgy" : "真是个荡妇！看起来她想要每个洞都填满。可能与最多三名客户发生性行为，代价是额外的疲劳。",
                             }



        # perk_name = {
        #     "Maid Training" : "女仆训练"
        # }
        ## REGULAR PERKS ##

        perk_dict = {
                     "Maid Training" : Perk(name="女仆训练", type="level", perk_level=0, archetype="The Maid", effects=[Effect("change", "obedience", 5), Effect("change", "maintenance", 1, scope="brothel")], pic = "maid0.jpg"),
                     "Loyalty" : Perk(name="忠心耿耿", type="level", perk_level=1, archetype="The Maid", effects=[Effect("change", "train obedience target", -10), Effect("change", "job obedience target", -10)], pic = "maid1_1.jpg"),
                     "Hardworking" : Perk(name="不辞辛劳", type="level", perk_level=1, archetype="The Maid", effects=[Effect("boost", "upkeep", -0.15), Effect("boost", "waitress jp gains", 0.15)], pic = "maid1_2.jpg"),
                     "Try Again" : Perk(name="再接再厉", type="level", perk_level=2, archetype="The Maid", effects=[Effect("reroll", "job critical failure", 1), Effect("boost", "xp gains", 0.05)], pic = "maid2_1.jpg"),
                     "Survivor" : Perk(name="劫后重生", type="level", perk_level=2, archetype="The Maid", effects=[Effect("boost", "fear", 0.5), Effect("resist", "hurt", 3, dice=True)], pic = "maid2_2.jpg"),
                     "Strive for Perfection" : Perk(name="力臻完美", type="level", perk_level=3, archetype="The Maid", effects=[Effect("boost", "all skill gains", 0.25), Effect("change", "brothel reputation", 5, scope="brothel", scales_with="rank")], pic = "maid3.jpg"),

                     "Bunny Girl" : Perk(name="兔装女郎", type="level", perk_level=0, archetype="The Player", effects=[Effect("change", "body", 10), Effect("change", "advertising", 1, scope="brothel")], pic = "player0.jpg"),
                     "Party Girl" : Perk(name="派对女郎", type="level", perk_level=1, archetype="The Player", effects=[Effect("change", "job customer capacity", 2), Effect("boost", "customer penalties", -0.5)], pic = "player1_1.jpg"),
                     "Bimbo" : Perk(name="丰乳肥臀", type="level", perk_level=1, archetype="The Player", effects=[Effect("boost", "reputation gains", 0.15), Effect("boost", "dancer jp gains", 0.15)], pic = "player1_2.jpg"),
                     "Autograph" : Perk(name="亲笔签名", type="level", perk_level=2, archetype="The Player", effects=[Effect("change", "tip", 1, scales_with="rep"), Effect("special", "job prestige", 1)], pic = "player2_1.jpg"),
                     "Exhibitionist" : Perk(name="好出风头", type="level", perk_level=2, archetype="The Player", effects=[Effect("boost", "naked bonus", 0.15)], pic = "player2_2.jpg"),
                     "Star Power" : Perk(name="明星魅力", type="level", perk_level=3, archetype="The Player", effects=[Effect("increase satisfaction", "all jobs", 1), Effect("increase satisfaction", "all sex acts", 1)], pic = "player3.jpg"),

                     "Modeling 101" : Perk(name="人体衣架", type="level", perk_level=0, archetype="The Model", effects=[Effect("change", "beauty", 10), Effect("boost", "quest results", 0.2)], pic = "model0.jpg"),
#                     "Rules of Attraction" : Perk(name="Rules of Attraction", type="level", perk_level=1, archetype="The Model", effects=[Effect("special", "BBCR bonus", 1, chance=0.25)], pic = "model1_1.jpg"), # Shelving stat bonuses for now
                     "Rules of Attraction" : Perk(name="情爱磁场", type="level", perk_level=1, archetype="The Model", effects=[Effect("change", "customers", 3, dice=True, scope="brothel")], pic = "model1_1.jpg"),
                     "Overachiever" : Perk(name="功成名就", type="level", perk_level=1, archetype="The Model", effects=[Effect("change", "all skill max", 10), Effect("boost", "masseuse jp gains", 0.15)], pic = "model1_2.jpg"),
                     "Eye Contact" : Perk(name="眉目传情", type="level", perk_level=2, archetype="The Model", effects=[Effect("special", "lucky"), Effect("change", "brothel reputation", 50, chance=0.2, scope="brothel")], pic = "model2_1.jpg"),
                     "Life of Luxury" : Perk(name="极致奢华", type="level", perk_level=2, archetype="The Model", effects=[Effect("special", "luxury"), Effect("change", "mood", 0.5, scales_with="equipped")], pic = "model2_2.jpg"),
                     "Beauty Queen" : Perk(name="选美皇后", type="level", perk_level=3, archetype="The Model", effects=[Effect("change", "all main skills", 15), Effect("boost", "job customer budget", 1.0)], pic = "model3.jpg"),

                     "Court relations" : Perk(name="阿谀奉承", type="level", perk_level=0, archetype="The Courtesan", effects=[Effect("change", "refinement", 10), Effect("increase satisfaction", "bisexual", 1)], pic = "courtesan0.jpg"),
                     "Warm welcome" : Perk(name="热情欢迎", type="level", perk_level=1, archetype="The Courtesan", effects=[Effect("change", "first customer satisfaction", 1), Effect("boost", "half-shift resting bonus", 0.5)], pic = "courtesan1_1.jpg"),
                     "Refined taste" : Perk(name="品味高雅", type="level", perk_level=1, archetype="The Courtesan", effects=[Effect("boost", "bisexual chance", 0.5), Effect("boost", "geisha jp gains", 0.15)], pic = "courtesan1_2.jpg"),
                     "Five Stars" : Perk(name="五星消费", type="level", perk_level=2, archetype="The Courtesan", effects=[Effect("change", "total tip", 25, scales_with="customer satisfaction")], pic = "courtesan2_1.jpg"),
                     "Heavenly Pleasures" : Perk(name="天堂乐趣", type="level", perk_level=2, archetype="The Courtesan", effects=[Effect("boost", "perfect result tip", 0.1), Effect("boost", "perfect result xp", 0.1), Effect("boost", "perfect result jp", 0.1)], pic = "courtesan2_2.jpg"),
                     "Royal Treatment" : Perk(name="皇家待遇", type="level", perk_level=3, archetype="The Courtesan", effects=[Effect("boost", "first customer tip", 1.5), Effect("boost", "first customer rep", 2.5), Effect("boost", "whore customer budget", 1.0)], pic = "courtesan3.jpg"),

                     "Available" : Perk(name="切实可用", type="level", perk_level=0, archetype="The Escort", effects=[Effect("change", "constitution", 5), Effect("increase satisfaction", "group", 1)], pic = "escort0.jpg"),
#                     "Extras" : Perk(name="Extras", type="level", perk_level=1, archetype="The Escort", effects=[Effect("special", "LOCS bonus", 1, chance=0.25)], pic = "escort1_1.jpg"), # Shelving stat bonuses for now
                     "Convincing" : Perk(name="令人信服", type="level", perk_level=1, archetype="The Escort", effects=[Effect("special", "temptress", 0.66)], pic = "slut2_2.jpg"),
                     "On Call" : Perk(name="随叫随到", type="level", perk_level=1, archetype="The Escort", effects=[Effect("boost", "group chance", 0.5), Effect("change", "whore obedience target", -10)], pic = "escort2_1.jpg"),
                     "Focus" : Perk(name="引人注目", type="level", perk_level=2, archetype="The Escort", effects=[Effect("special", "focus", 1)], pic = "escort1_1.jpg"),
                     "Loves Sex" : Perk(name="如狼似虎", type="level", perk_level=2, archetype="The Escort", effects=[Effect("change", "all sex skills", 10)], pic = "slut2_1.jpg"),
                     "Business and Pleasure" : Perk(name="兢兢业业", type="level", perk_level=3, archetype="The Escort", effects=[Effect("boost", "total tip", 0.01, scales_with="job cust nb"), Effect("boost", "total tip", 0.03, scales_with="whore cust nb"), Effect("change", "mood", 0.25, scales_with="cust nb")], pic = "escort3.jpg"),

                     "Foxy Lady" : Perk(name="小狐狸精", type="level", perk_level=0, archetype="The Fox", effects=[Effect("change", "charm", 10), Effect("boost", "class results", 0.2)], pic = "fox0.jpg"),
                     "Something New" : Perk(name="新鲜事物", type="level", perk_level=1, archetype="The Fox", effects=[Effect("boost", "xp gains", 1.0, chance=0.1), Effect("boost", "all jp gains", 1.0, chance=0.1)], pic = "fox1_1.jpg"),
                     "Lost and Found" : Perk(name="失物归还", type="level", perk_level=1, archetype="The Fox", effects=[Effect("special", "random item", 1, chance=0.025)], pic = "fox1_2.jpg", base_description = "'I'm sure he won't miss it.'"),
                     "Secret Admirers" : Perk(name="不传之秘", type="level", perk_level=2, archetype="The Fox", effects=[Effect("boost", "tip", 1, chance=0.2)], pic = "fox2_1.jpg"),
                     "Tempting Fate" : Perk(name="幸运冒险", type="level", perk_level=2, archetype="The Fox", effects=[Effect("special", "effect chance", 1)], pic = "fox2_2.jpg"),
                     "Stars Are Aligned" : Perk(name="招财福星", type="level", perk_level=3, archetype="The Fox", effects=[Effect("boost", "income", 1, chance=0.02, scope="brothel")], pic = "fox3.jpg"),

                     "Teaser" : Perk(name="卖弄风骚", type="level", perk_level=0, archetype="The Slut", effects=[Effect("change", "libido", 5), Effect("gain", "positive fixation", 1)], pic = "slut0.jpg"),
                     "Open mind" : Perk(name="思想开放", type="level", perk_level=1, archetype="The Slut", effects=[Effect("gain", "all sexual preferences", 250)], pic = "slut1_1.jpg"),
                     "Bedroom Eyes" : Perk(name="情迷意乱", type="level", perk_level=1, archetype="The Slut", effects=[Effect("boost", "service jp bonus", 0.25), Effect("boost", "sex jp bonus", 0.25), Effect("boost", "anal jp bonus", 0.25), Effect("boost", "fetish jp bonus", 0.25)], pic = "slut1_2.jpg"),
                     "Next" : Perk(name="紧随其后", type="level", perk_level=2, archetype="The Slut", effects=[Effect("change", "whore customer capacity", 1)], pic = "escort1_2.jpg"),
                     "Work and Whore" : Perk(name="一心二用", type="level", perk_level=2, archetype="The Slut", effects=[Effect("special", "workwhore", 1)], pic = "slut3.jpg"),
                     "Me So Horny" : Perk(name="狂潮娇娃", type="level", perk_level=3, archetype="The Slut", effects=[Effect("boost", "tiredness", -0.1)], pic = "escort2_2.jpg"),

                     "Enter The Bride" : Perk(name="新娘登场", type="level", perk_level=0, archetype="The Bride", effects=[Effect("change", "sensitivity", 5), Effect("change", "security", 1, scope = "brothel")], pic = "bride0.jpg"),
                     "Helping Hand" : Perk(name="助人为乐", type="level", perk_level=1, archetype="The Bride", effects=[Effect("change", "making friends", 1), Effect("boost", "mood gains from friendship", 0.5)], pic = "bride1_1.jpg"),
                     "Confession" : Perk(name="相互劝慰", type="level", perk_level=1, archetype="The Bride", effects=[Effect("spillover", "xp", 0.2), Effect("spillover", "jp", 0.2)], pic = "bride1_2.jpg"),
                     "Leading by Example" : Perk(name="以身作则", type="level", perk_level=2, archetype="The Bride", effects=[Effect("special", "skill catch up", 1)], pic = "bride2_1.jpg"),
                     "The Healer" : Perk(name="医者之心", type="level", perk_level=2, archetype="The Bride", effects=[Effect("boost", "love gains", 0.5), Effect("change", "heal", 1, chance=0.33, scope="brothel")], pic = "bride2_2.jpg"),
                     "The Virgin Whore" : Perk(name="贞洁妓女", type="level", perk_level=3, archetype="The Bride", effects=[Effect("boost", "virgin tip", 1), Effect("boost", "virgin rep", 1)], pic = "bride3.jpg"),
                     }

        ## SPECIAL PERKS ##

        naked_perk = Perk("Naturist", type="sex", effects = [Effect("special", "naked", 1)])
        pony_perk = Perk("Ponygirl", type="sex", effects = [Effect("special", "ponygirl", 1.0, 0.5)])
        bis_perk = Perk("Bisexual", type="sex", effects = [Effect("special", "bisexual", 1.0, bis_chance)])
        group_perk = Perk("Group", type="sex", effects = [Effect("special", "group", 1.0, group_chance)])
        orgy_perk = Perk("Orgy", type="sex", effects = [Effect("special", "orgy", 1.0, 0.5)])



    return

#### END OF BK PERKS FILE ####
