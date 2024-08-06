#### BK Achievements ####

init python:
    achievement_list = [
                        Achievement("磨刀不误砍柴工", "观看新手教程。", pic="portrait.webp", pic_path="NPC/Sill/", target="intro"),

                        Achievement("新培训师：玛雅", "你已经解锁了玛雅。她可以提高女孩的自卫能力。", pic="portrait.webp", pic_path="NPC/Maya/", target="trainer maya"),
                        Achievement("新培训师：伦萨", "你已经解锁了伦萨。她可以把你的女孩训练成小偷。", pic="portrait.webp", pic_path="NPC/Renza/", target="trainer renza"),
                        Achievement("新培训师：萨特拉", "你已经解锁了萨特拉。她将使你的女孩们感到恐惧。", pic="portrait.webp", pic_path="NPC/Satella/", target="trainer satella"),
                        Achievement("新培训师：法拉", "你已经解锁了法拉。她训练的是比较辣的性行为。", pic="portrait.webp", pic_path="NPC/Captain/", target="trainer farah"),
                        Achievement("新培训师：莉迪", "你已经解锁了莉迪。她可以让你的女孩们更听话。", pic="portrait.webp", pic_path="NPC/Lieutenant/", target="trainer lydie"),
                        Achievement("新培训师：斯特拉", "你已经解锁了斯特拉。她可以提高你的农场训练效果。", pic="portrait.webp", pic_path="NPC/Stella/", target="trainer stella"),
                        Achievement("新培训师：贝斯特", "你已经解锁了贝斯特。她可以帮助你收集资源。", pic="portrait.webp", pic_path="NPC/Bast/", target="trainer bast"),
                        Achievement("新培训师：戈尔迪", "你已经解锁了戈尔迪。她可以对你的女孩进行软核技术培训。", pic="portrait.webp", pic_path="NPC/Goldie/", target="trainer goldie"),
                        Achievement("新培训师：公会职员", "你已经解锁了公会职员。她可以保护你的部分收入免于纳税。", pic="portrait.webp", pic_path="NPC/Taxgirl/", target="trainer taxgirl"),

                        Achievement("新的商户：戈尔迪", "你已经解锁了牧场，戈尔迪在这里出售野兽和相关物品。", pic="portrait.webp", pic_path="NPC/Goldie/", target="merchant goldie"),
                        Achievement("新的商户：斯特拉", "斯特拉出售种马和相关物品，如果你敢接近她。", pic="portrait.webp", pic_path="NPC/Stella/", target="merchant stella"),
                        Achievement("新的商户：薇洛", "薇洛出售她为生计而捕获的怪物，以及相关物品。", pic="portrait.webp", pic_path="NPC/Willow/", target="merchant willow"),
                        Achievement("新的商户：吉娜", "科学家吉娜销售机械小玩意，并研究飞行。", pic="portrait.webp", pic_path="NPC/Gina/", target="merchant gina"),
                        Achievement("新的商户：里奇", "里奇出售她在植物园里采摘的鲜花。", pic="portrait.webp", pic_path="NPC/Riche/", target="merchant riche"),
                        Achievement("新的商户：卡特林", "卡特林卖小饰品，脾气很暴躁。", pic="portrait.webp", pic_path="NPC/Katryn/", target="merchant katryn"),
                        Achievement("新的商户：古里古拉", "古里古拉卖玩具、食品和用品，当她不分心的时候。", pic="portrait.webp", pic_path="NPC/Gurigura/", target="merchant gurigura"),
                        Achievement("新的商户：拉米阿斯", "拉米阿斯卖武器，不受傻瓜和讨价还价的影响。", pic="portrait.webp", pic_path="NPC/Ramias/", target="merchant ramias"),
                        Achievement("新的商户：礼品店", "礼品店女孩卖的是....礼物。废话。", pic="portrait.webp", pic_path="NPC/Gift girl/", target="merchant giftgirl"),
                        Achievement("新的商户：双胞胎", "双胞胎，奥斯汀！双胞胎！", pic="body.webp", pic_path="NPC/Twins/", target="merchant twins"),

                        Achievement("第一章：狼狈为奸", "你帮助一帮暴徒在下水道里干一个无助的女人。", pic="portrait naked.webp", pic_path="NPC/Sewer girl/", target="c1 gang"),
                        Achievement("第一章：正义之友", "你已经完成了第一章，并且站在了玛雅那一边。", pic="portrait.webp", pic_path="NPC/Maya/", target="c1 good"),
                        Achievement("第一章：公会之友", "你已经完成了第一章，并且站在了伦萨那一边。", pic="portrait.webp", pic_path="NPC/Renza/", target="c1 neutral"),
                        Achievement("第一章：守卫之友", "你已经完成了第一章，并且站在了上尉那一边。", pic="portrait.webp", pic_path="NPC/Captain/", target="c1 evil"),

                        Achievement("第二章：狩猎忍者", "你已经抓到了你的第一个忍者。", pic="kunoichi portrait.webp", pic_path="NPC/kunoichi/", target="c2 kunoichi"),
                        Achievement("第二章：痛苦回忆", "你已经了解了春香悲伤的过去。", pic="portrait.webp", pic_path="NPC/kunoichi/haruka/", target="c2 haruka"),
                        Achievement("第二章：温泉幽灵", "你在温泉中与水木发生了奇怪的、令人激动的邂逅。", pic="portrait.webp", pic_path="NPC/kunoichi/mizuki/", target="c2 mizuki"),
                        Achievement("第二章：顽皮学生", "你偷看了成香的秘密会议。", pic="portrait.webp", pic_path="NPC/kunoichi/narika/", target="c2 narika"),

                        Achievement("宝藏猎人：金发女郎", "你和那个金发碧眼的女郎发生了关系。", pic="amber ring.webp", pic_path="items/ring/", target="h treasure blonde"),
                        Achievement("宝藏猎人：粉发女孩", "你和那个粉红头发的女孩发生了关系。", pic="amber ring.webp", pic_path="items/ring/", target="h treasure pink"),
                        Achievement("H：希露", "你与你的奴隶希露发生了火热的性关系。", pic="portrait2.webp", pic_path="NPC/Sill/", target="h sill1"),
                        Achievement("H：女仆", "你与吉欧的女佣发生了关系。", pic="portrait blush.webp", pic_path="NPC/Maid/", target="h maid"),
                        Achievement("H：银行家", "你与银行家发生了关系。", pic="portrait.webp", pic_path="NPC/Banker/", target="h banker"),
                        Achievement("H：上尉", "你与法拉发生了关系。", pic="portrait.webp", pic_path="NPC/Captain/", target="h farah"),
                        Achievement("H：中尉", "你与莉迪发生了关系。", pic="portrait.webp", pic_path="NPC/Lieutenant/", target="h lydie"),
                        Achievement("H：中士", "你与卡希夫发生了关系。", pic="portrait.webp", pic_path="NPC/Sergeant/", target="h kashiv"),
                        Achievement("H：守卫", "你与玛雅发生了关系.", pic="portrait.webp", pic_path="NPC/Maya/", target="h maya"),
                        Achievement("H：盗贼", "你与伦萨发生了关系.", pic="portrait.webp", pic_path="NPC/Renza/", target="h renza"),
                        Achievement("H：牧场主", "你与戈尔迪发生了关系。", pic="portrait.webp", pic_path="NPC/Goldie/", target="h goldie"),
                        Achievement("H：官员", "你与斯特拉发生了关系。", pic="portrait.webp", pic_path="NPC/Stella/", target="h stella"),
                        Achievement("H：将军", "你与卡发生了关系。", pic="ka portrait.webp", pic_path="NPC/Stella/", target="h ka"),
                        Achievement("H：上将", "你与泽发生了关系。", pic="zee portrait.webp", pic_path="NPC/Stella/", target="h zee"),
                        Achievement("H：猎人", "你与薇洛发生了关系。", pic="portrait.webp", pic_path="NPC/Willow/", target="h willow"),
                        Achievement("H：亲戚", "你与薇洛的亲戚发生了关系。", pic="portrait.webp", pic_path="NPC/Willow/", target="h relative"),
                        Achievement("H：猎人", "你与薇洛发生了关系。", pic="portrait.webp", pic_path="NPC/Willow/", target="h willow"),
                        Achievement("蟾蜍之战", "你作为蟾蜍发生了性关系，现在你永远不能告诉你的朋友。", pic="milkmaid.webp", pic_path="NPC/Misc/", target="h toad"),
                        Achievement("H：店主", "你与店主发生了关系。", pic="silky nighties.webp", pic_path="items/gift/", target="h shop"),
                        Achievement("H：夜色小姐", "你与萨特拉发生了关系。", pic="portrait.webp", pic_path="NPC/Satella/", target="h satella"),
                        Achievement("H：月亮女神", "你与女神莎莉娅发生了关系。", pic="portrait.webp", pic_path="NPC/Shalia/", target="h shalia"),
                        Achievement("H：会计", "你与你从下水道救出的女人发生了关系。", pic="portrait.webp", pic_path="NPC/Sewer girl/", target="h sewer"),
                        Achievement("H：圣洁筑者", "你与贝斯特发生了关系。", pic="portrait.webp", pic_path="NPC/Bast/", target="h bast"),
                        Achievement("H：游泳者", "你与阿妮卡发生了关系。", pic="anika portrait.webp", pic_path="NPC/Jobgirl/beach/", target="h anika"),
#                         Achievement("Bedded: The Adventurer", "You had sex with Scarlet.", pic="portrait.webp", pic_path="NPC/Jobgirl/", target="h jobgirl"), # Event not ready yet?
                        Achievement("H：女税务官", "你与奴隶主协会的女职员发生了关系。", pic="portrait.webp", pic_path="NPC/taxgirl/", target="h taxgirl"),
                        Achievement("H：气功忍者", "你与云雀发生了（多次）关系。", pic="portrait.webp", pic_path="NPC/suzume/", target="h suzume"),
                        Achievement("H：贵族千金", "你与焰发生了关系。", pic="portrait.jpg", pic_path="NPC/homura/", target="h homura"),


                        Achievement("城市：冒险家", "你与%s位女冒险家发生了关系。", pic="impress0.webp", pic_path="NPC/encounters/", target="h impress", level_nb=4),
                        Achievement("城市：训奴师", "你帮助训练一个女奴。", pic="slave2.webp", pic_path="NPC/misc/", target="h slavegirl"),
                        Achievement("城市：奴隶商", "你与奴隶市场的女孩发生了关系。", pic="slave1.webp", pic_path="NPC/misc/", target="h slavemarket"),
                        Achievement("城市：喵喵喵", "你与%s位猫娘发生了关系。", pic="cat found.webp", pic_path="NPC/encounters/", target="h catgirl", level_nb=2),
                        Achievement("城市：占卜师", "你与一个吉普赛人女孩发生了关系。", pic="gypsy1_1.webp", pic_path="NPC/encounters/", target="h gypsy"),
                        Achievement("城市：女飞贼", "你与一个被打败的强盗发生了关系。", pic="rob5_1.webp", pic_path="NPC/encounters/", target="h robber"),
                        Achievement("城市：女赌徒", "你与一个赌博女孩发生了关系。", pic="gambler4_1.webp", pic_path="NPC/encounters/", target="h gambler"),
                        Achievement("圣诞快乐", "你与一个神秘的冬季访客发生了关系。", pic="portrait.webp", pic_path="NPC/Hmas/", target="hmas"),


                        Achievement("崭露头角", "拥有 %s 位奴隶（不算希露）。", pic="slave1.webp", pic_path="NPC/Misc/", level_nb=5, target="slaves", requirements={1 : 4, 2 : 8, 3 : 16, 4 : 24, 5 : 32}),
                        Achievement("初试锋芒", "拥有 %s 位B级或以上的奴隶。", pic="slave2.webp", pic_path="NPC/Misc/", level_nb=5, target="rank B", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("群英荟萃", "拥有 %s 位A级或以上的奴隶。", pic="slave2.webp", pic_path="NPC/Misc/", level_nb=5, target="rank A", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("名震四方", "拥有 %s 位S级或以上的奴隶。", pic="slave2.webp", pic_path="NPC/Misc/", level_nb=5, target="rank S", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("仙女下凡", "拥有 %s 位X级或以上的奴隶。", pic="slave2.webp", pic_path="NPC/Misc/", level_nb=5, target="rank X", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("苦中作乐", "拥有 %s 位受虐狂奴隶。", pic="slave2.webp", pic_path="NPC/Misc/", level_nb=5, target="masochist", requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}),
                        Achievement("经年累月", "一局游戏中，你的女孩们在农场的训练时间加起来有 %s 天。", pic="beast2.webp", pic_path="NPC/Minions/", level_nb=5, target="farm_days", requirements={1 : 10, 2 : 30, 3 : 90, 4 : 180, 5 : 365}),
                        Achievement("玩物成瘾", "让你的女孩们在一局游戏中使用玩具的次数达到 %s 。", pic="black dildo.webp", pic_path="Items/Toy/", level_nb=5, target="used toy", requirements={1 : 1, 2 : 10, 3 : 100, 4 : 500, 5 : 2500}),
                        Achievement("正当防卫", "给 %s 位女孩配备武器。", pic="knife.webp", pic_path="Items/Weapon/", level_nb=5, target="hands", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("人靠衣装", "给 %s 位女孩配备衣服。", pic="frilly dress.webp", pic_path="Items/dress/", level_nb=5, target="body", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("宠物项圈", "给 %s 位女孩配备项链。", pic="dog collar.webp", pic_path="Items/necklace/", level_nb=5, target="neck", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("情比金坚", "给 %s 位女孩配备戒指。", pic="brass ring.webp", pic_path="Items/ring/", level_nb=5, target="finger", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("点睛之笔", "给 %s 位女孩配备饰品。", pic="lace panties.webp", pic_path="Items/accessory/", level_nb=5, target="accessory", requirements={1 : 2, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("自然主义", "有 %s 位女孩同时裸体。", pic="naked2.webp", pic_path="UI/status/", level_nb=5, target="naked", requirements={1 : 2, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("花好月圆", "有 %s 位女孩对双飞感到舒服。", pic="naked2.webp", pic_path="UI/status/", level_nb=5, target="bisexual", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("众星捧月", "有 %s 位女孩对群交感到舒服。", pic="naked2.webp", pic_path="UI/status/", level_nb=5, target="group", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),


                        Achievement("勇冠三军", "战士的等级达到 %s 级.", pic="warrior.webp", pic_path="UI/", level_nb=5, target="战士", requirements={1 : 5, 2 : 10, 3 : 15, 4 : 20, 5 : 25}),
                        Achievement("法力风暴", "法师的等级达到 %s 级.", pic="wizard.webp", pic_path="UI/", level_nb=5, target="法师", requirements={1 : 5, 2 : 10, 3 : 15, 4 : 20, 5 : 25}),
                        Achievement("唯利是图", "奸商的等级达到 %s 级.", pic="trader.webp", pic_path="UI/", level_nb=5, target="奸商", requirements={1 : 5, 2 : 10, 3 : 15, 4 : 20, 5 : 25}),
                        Achievement("与人为善", "成为正义的光辉榜样。也是一个青楼老板。为什么不呢?", pic="al_good.webp", pic_path="UI/", target="good"),
                        Achievement("大公无私", "你不偏袒任何一方，你只是收取你的奖金.", pic="al_neutral.webp", pic_path="UI/", target="neutral"),
                        Achievement("恶贯满盈", "变得异常邪恶。获得超过 %s 点邪恶点数.", pic="al_evil.webp", pic_path="UI/", level_nb=3, target="evil", requirements={1 : 10, 2 : 100, 3 : 1000}, custom_titles={1 : "Mother-In-Law", 2 : "Dr. Evil", 3 : "Palpatine"}),
                        Achievement("和平主义", "在这个游戏的制作过程中，没有任何超自然的动物受到伤害. {b}{i}真的是吗?{/i}{/b}", pic="pet1.webp", pic_path="NPC/Misc/Pets/", target="pet armageddon"),
                        Achievement("力大无穷", "力量达到10.", pic="warrior.webp", pic_path="UI/", target="mc strength"),
                        Achievement("百折不挠", "精神达到10.", pic="wizard.webp", pic_path="UI/", target="mc spirit"),
                        Achievement("貌若潘安", "魅力达到10。", pic="trader.webp", pic_path="UI/", target="mc charisma"),
                        Achievement("风驰电掣", "速度达到10。.", pic="Leather boots.webp", pic_path="items/accessory/", target="mc speed"),

                        Achievement("漫漫长夜", "一局游戏中，玩“青楼之王”的时间为 %s 游戏月。", pic="calendar.webp", pic_path="UI/", level_nb=5, target="months", requirements={1 : 1, 2 : 3, 3 : 6, 4 : 12, 5 : 24}),
                        Achievement("衣冠禽兽", "成功完成 %s 份合约。", pic=license_dict[1][1], pic_path="UI/", level_nb=5, target="completed contracts", requirements={1 : 1, 2 : 3, 3 : 6, 4 : 12, 5 : 24}),
                        Achievement("改弦更张", "在完美完成合约之后卖掉一个女孩。", pic="maid.png", pic_path="NPC/Misc/", target="contract sale"),
                        Achievement("任务达人", "完成 %s 份任务。", pic="portrait.webp", pic_path="NPC/Jobgirl/", level_nb=5, target="completed quest", requirements={1 : 5, 2 : 25, 3 : 50, 4 : 100, 5 : 250}),
                        Achievement("变态高中", "完成 %s 个课程。", pic="portrait.webp", pic_path="NPC/Jobgirl/", level_nb=5, target="completed class", requirements={1 : 5, 2 : 25, 3 : 50, 4 : 100, 5 : 250}),
                        Achievement("课业繁重", "用你的女孩塞满课程。", pic="portrait.webp", pic_path="NPC/Sewer girl/", target="filled class"),
                        Achievement("动物牧场", "获得 %s 位仆从。", pic="beast1.webp", pic_path="NPC/Minions/", level_nb=5, target="minions", requirements={1 : 2, 2 : 4, 3 : 8, 4 : 12, 5 : 20}),
                        Achievement("生财有道", "一局游戏中赚取 %s 金币。", pic="gold bag.webp", pic_path="items/misc/", level_nb=6, target="total_gold", requirements={1 : 1000, 2 : 10000, 3 : 100000, 4 : 1000000, 5 : 10000000, 6 : 100000000}),
                        Achievement("夜进斗金", "一夜之间赚取 %s 金币。", pic="coin.webp", pic_path="UI/", level_nb=5, target="income", requirements={1 : 100, 2 : 1000, 3 : 10000, 4 : 100000, 5 : 250000}),
                        Achievement("血本无归", "一夜之间损失 %s 金币。", pic="portrait.webp", pic_path="NPC/Kosmo/", level_nb=5, target="losses", requirements={1 : 100, 2 : 1000, 3 : 5000, 4 : 10000, 5 : 25000}),
                        Achievement("富甲一方", "累积 %s 金币。", pic="jewel bag.webp", pic_path="items/misc/", level_nb=5, target="gold", requirements={1 : 1000, 2 : 10000, 3 : 100000, 4 : 1000000, 5 : 10000000}),
                        Achievement("社交达人", "你的女孩中有 %s 个有朋友。", pic="heart.webp", pic_path="UI/", level_nb=5, target="friends", requirements={1 : 2, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("勾心斗角", "你的女孩中有 %s 个有竞争对手。", pic="broken heart.webp", pic_path="UI/", level_nb=5, target="rivals", requirements={1 : 2, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("久经沙场", "在 %s 个安全事件中幸存下来。", pic="shield.webp", pic_path="UI/", level_nb=5, target="security events", requirements={1 : 10, 2 : 25, 3 : 50, 4 : 125, 5 : 250}),
                        Achievement("擒贼擒王", "捕获一名敌方将军。", pic="portrait.webp", pic_path="NPC/Kenshin", target="general captured"),
                        Achievement("解救人质", "拯救一个被绑架的女孩。", pic="knight portrait.webp", pic_path="NPC/Misc/", target="rescued from kidnapping"),
                        Achievement("蠢蠢欲动", "在你的女孩身上发现 %s 个正面癖好。", pic="droplet.webp", pic_path="UI/", target="pos fixations", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 125, 5 : 250}),
                        Achievement("人无完人", "发现你的女孩身上有 %s 个负面癖好。", pic="skull.webp", pic_path="UI/", target="neg fixations", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 125, 5 : 250}),
                        Achievement("迎难而上", "从你的女孩中去除 %s 个负面癖好。", pic="droplet.webp", pic_path="UI/", target="neg fixation removed", level_nb=5, requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("阴差阳错", "过于努力成功锁定女孩的负面癖好。", pic="skull.webp", pic_path="UI/", target="neg fixation locked"),
                        Achievement("催眠大师", "成功催眠女孩 %s 次。", pic="droplet.webp", pic_path="UI/", target="hypnotize success", level_nb=5, requirements={1 : 1, 2 : 10, 3 : 50, 4 : 100, 5 : 250}),
                        Achievement("笨手笨脚", "催眠女孩失败 %s 次。", pic="droplet.webp", pic_path="UI/", target="hypnotize failure", level_nb=5, requirements={1 : 1, 2 : 5, 3 : 25, 4 : 50, 5 : 100}),

                        Achievement("情意绵绵", "有 %s 个女孩的爱情值有 %s 或更多。", level_nb=5, pic="heart.webp", pic_path="UI/", target="love", requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 25, 2 : 50, 3 : 75, 4 : 100, 5 : 125}),
                        Achievement("惊恐不安", "有 %s 个女孩的恐惧值有 %s 或更多。", level_nb=5, pic="skull.webp", pic_path="UI/", target="fear", requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 25, 2 : 50, 3 : 75, 4 : 100, 5 : 125}),
                        Achievement("倾国倾城", "有 %s 个女孩的美貌超过 %s 。", pic="portrait.webp", pic_path="NPC/Katryn/", target="Beauty", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}),
                        Achievement("身姿曼妙", "有 %s 个女孩的身材超过 %s 。", pic="portrait.webp", pic_path="NPC/Ramias/", target="Body", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}),
                        Achievement("风华绝代", "有 %s 个女孩的魅力超过 %s 。", pic="portrait.webp", pic_path="NPC/Gurigura/", target="Charm", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}),
                        Achievement("大家闺秀", "有 %s 个女孩的优雅超过 %s 。", pic="portrait.webp", pic_path="NPC/Riche/", target="Refinement", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}),
                        Achievement("荒淫无度", "有 %s 个女孩的性欲超过 %s 。", pic="portrait.webp", pic_path="NPC/Captain/", target="Libido", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}),
                        Achievement("唯命是从", "有 %s 个女孩的服从超过 %s 。", pic="portrait.webp", pic_path="NPC/Maid/", target="Obedience", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}),
                        Achievement("健步如飞", "有 %s 个女孩的体格超过 %s 。", pic="portrait.webp", pic_path="NPC/Jobgirl/", target="Constitution", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}),
                        Achievement("娇花似水", "有 %s 个女孩的敏感超过 %s 。", pic="portrait.webp", pic_path="NPC/Satella/", target="Sensitivity", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}),
                        Achievement("侍奉精通", "有 %s 个女孩的性服侍天赋超过 %s 。", pic="portrait.webp", pic_path="NPC/Willow/", target="Service", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}),
                        Achievement("性交精通", "有 %s 个女孩的性交天赋超过 %s 。", pic="portrait.webp", pic_path="NPC/Goldie/", target="Sex", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}),
                        Achievement("肛交精通", "有 %s 个女孩的肛交天赋超过 %s 。", pic="portrait.webp", pic_path="NPC/Kosmo/", target="Anal", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}),
                        Achievement("调教精通", "有 %s 个女孩的皮绳愉虐天赋超过 %s 。", pic="portrait.webp", pic_path="NPC/Stella/", target="Fetish", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}),
                        Achievement("登峰造极", "有 %s 个女孩的全部天赋超过 %s 。", pic="portrait.webp", pic_path="NPC/Sill/", target="ultimate", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}),
                        Achievement("奴隶贩子", "一局游戏中，出售女孩的总金额为 %s 金币。", pic="slave1.webp", pic_path="NPC/Misc/", target="sell girl gold", level_nb=5, requirements={1 : 500, 2 : 2500, 3 : 10000, 4 : 25000, 5 : 100000}),
                        Achievement("冷血无情", "出售一个爱你的女孩。", pic="spirit portrait.webp", pic_path="NPC/Misc/", target="sell girl love"),
                        Achievement("自由之翼", "让女孩重新获得自由。", pic="broken heart.webp", pic_path="UI/", target="release free girl"),
                        Achievement("强奸惯犯", "强奸你的女孩 %s 次。", pic="spirit portrait.webp", pic_path="NPC/Misc/", target="raped", level_nb=5, requirements={1 : 1, 2 : 5, 3 : 10, 4 : 25, 5 : 100}),
                        Achievement("家庭暴力", "殴打你的女孩 %s 次。", pic="spirit portrait.webp", pic_path="NPC/Misc/", target="beaten", level_nb=5, requirements={1 : 1, 2 : 5, 3 : 10, 4 : 25, 5 : 100}),
                        Achievement("小惩大诫", "惩罚你的女孩 %s 次。", pic="skull.webp", pic_path="UI/", target="punished", level_nb=5, requirements={1 : 5, 2 : 25, 3 : 100, 4 : 250, 5 : 500}),
                        Achievement("慷慨大方", "奖励你的女孩 %s 次。", pic="droplet.webp", pic_path="UI/", target="rewarded", level_nb=5, requirements={1 : 5, 2 : 25, 3 : 100, 4 : 250, 5 : 500}),
                        Achievement("养尊处优", "你对女孩奖励太多，以至于她被宠坏了。", pic="bun.webp", pic_path="items/food/", target="spoiled"),
                        Achievement("诚惶诚恐", "你对女孩的惩罚太多，以至于她很害怕。", pic="monster juice.webp", pic_path="items/misc/", target="terrified"),
                        Achievement("解锁农场", "你解锁了农场。", pic="beast2.webp", pic_path="NPC/Minions/", target="farm"),
                        Achievement("保持好运", "你解锁了木匠的马车。", pic="portrait.webp", pic_path="NPC/Carpenter/", target="wagon"),
                        Achievement("井盖骑士", "你在下水道里解救了囚犯。", pic="portrait naked.webp", pic_path="NPC/Sewer girl/", target="sewer defender"),
                        Achievement("没完没了", "科斯莫访问了你 %s 次。", pic="portrait.webp", pic_path="NPC/Kosmo/", target="kosmo", level_nb=4, requirements={1 : 1, 2 : 5, 3 : 10, 4 : 20}),

                        Achievement("风流浪子", "与女孩上床 %s 次。", pic="heart.webp", pic_path="UI/", level_nb=5, target="had sex", requirements={1 : 5, 2 : 25, 3 : 100, 4 : 250, 5 : 1000}),
                        Achievement("招兵买马", "在奴隶市场上花费 %s 金币。", pic="slave2.webp", pic_path="NPC/Misc/", target="gold spent slavemarket", level_nb=4, requirements={1 : 500, 2 : 2500, 3 : 10000, 4 : 25000, 5 : 100000}),
                        Achievement("挥金如土", "在商店里花费 %s 金币。", pic="portrait.webp", pic_path="NPC/Gift girl/", target="gold spent shops", level_nb=4, requirements={1 : 500, 2 : 2500, 3 : 10000, 4 : 25000, 5 : 100000}),
                        Achievement("知根知底", "一局游戏中听到 %s 位女孩的故事。", pic="empty heart.webp", pic_path="UI/", target="origin stories", level_nb=5, requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 24}),
                        Achievement("循循善诱", "说服 %s 位自由女孩加入你的青楼。", pic="empty heart.webp", pic_path="UI/", target="free girl acquired", level_nb=5, requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement("顶级海王", "同时拥有十个女朋友。", pic="heart.webp", pic_path="UI/", target="girlfriends", requirements={1 : 10}),
                        Achievement("原班人马", "在你的青楼里有 %s 位原始女孩。", pic="license2.webp", pic_path="UI/", target="originals", level_nb=5, requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),

                        Achievement("一掷千金：乞丐", "让一名乞丐在青楼里花光所有的钱。", pic="beggar.webp", pic_path="UI/customers/", target="broke beggars"),
                        Achievement("一掷千金：暴徒", "让一名暴徒在青楼里花光所有的钱。", pic="thug.webp", pic_path="UI/customers/", target="broke thugs"),
                        Achievement("一掷千金：劳工", "让一名劳工在青楼里花光所有的钱。", pic="Laborer.webp", pic_path="UI/customers/", target="broke laborers"),
                        Achievement("一掷千金：水手", "让一名水手在青楼里花光所有的钱。", pic="Sailor.webp", pic_path="UI/customers/", target="broke sailors"),
                        Achievement("一掷千金：平民", "让一名平民在青楼里花光所有的钱。", pic="Commoner.webp", pic_path="UI/customers/", target="broke commoners"),
                        Achievement("一掷千金：工匠", "让一名工匠在青楼里花光所有的钱。", pic="Craftsman.webp", pic_path="UI/customers/", target="broke craftsmen"),
                        Achievement("一掷千金：中产阶级", "让一名中产阶级在青楼里花光所有的钱。", pic="Bourgeois.webp", pic_path="UI/customers/", target="broke bourgeois"),
                        Achievement("一掷千金：公会阶级", "让一名公会成员在青楼里花光所有的钱。", pic="Guild Member.webp", pic_path="UI/customers/", target="broke guild members"),
                        Achievement("一掷千金：骑士阶级", "让一名骑士阶级在青楼里花光所有的钱。", pic="Patrician.webp", pic_path="UI/customers/", target="broke patricians"),
                        Achievement("一掷千金：男爵阶级", "让一名男爵阶级在青楼里花光所有的钱。", pic="aristocrat.webp", pic_path="UI/customers/", target="broke aristocrats"),
                        Achievement("一掷千金：伯爵阶级", "让一名伯爵阶级在青楼里花光所有的钱。", pic="Noble.webp", pic_path="UI/customers/", target="broke nobles"),
                        Achievement("一掷千金：国王阶级", "让一名国王阶级在青楼里花光所有的钱。", pic="Royal.webp", pic_path="UI/customers/", target="broke royals"),
                        Achievement("五星好评：乞丐", "让一名乞丐在青楼里达到最大的满足。", pic="beggar.webp", pic_path="UI/customers/", target="happy beggars"),
                        Achievement("五星好评：暴徒", "让一名暴徒在青楼里达到最大的满足。", pic="thug.webp", pic_path="UI/customers/", target="happy thugs"),
                        Achievement("五星好评：劳工", "让一名劳工在青楼里达到最大的满足。", pic="Laborer.webp", pic_path="UI/customers/", target="happy laborers"),
                        Achievement("五星好评：水手", "让一名水手在青楼里达到最大的满足。", pic="Sailor.webp", pic_path="UI/customers/", target="happy sailors"),
                        Achievement("五星好评：平民", "让一名平民在青楼里达到最大的满足。", pic="Commoner.webp", pic_path="UI/customers/", target="happy commoners"),
                        Achievement("五星好评：工匠", "让一名工匠在青楼里达到最大的满足。", pic="Craftsman.webp", pic_path="UI/customers/", target="happy craftsmen"),
                        Achievement("五星好评：中产阶级", "让一名中产阶级在青楼里达到最大的满足。", pic="Bourgeois.webp", pic_path="UI/customers/", target="happy bourgeois"),
                        Achievement("五星好评：公会阶级", "让一名公会成员在青楼里达到最大的满足。", pic="Guild Member.webp", pic_path="UI/customers/", target="happy guild members"),
                        Achievement("五星好评：骑士阶级", "让一名骑士阶级在青楼里达到最大的满足。", pic="Patrician.webp", pic_path="UI/customers/", target="happy patricians"),
                        Achievement("五星好评：男爵阶级", "让一名男爵阶级在青楼里达到最大的满足。", pic="aristocrat.webp", pic_path="UI/customers/", target="happy aristocrats"),
                        Achievement("五星好评：伯爵阶级", "让一名伯爵阶级在青楼里达到最大的满足。", pic="Noble.webp", pic_path="UI/customers/", target="happy nobles"),
                        Achievement("五星好评：国王阶级", "让一名国王阶级在青楼里达到最大的满足。", pic="Royal.webp", pic_path="UI/customers/", target="happy royals"),

                        Achievement("登峰造极：女仆", "在一名女孩上解锁女仆天赋树上的所有天赋分支。", pic="The Maid portrait.webp", pic_path="perks/", target="The Maid"),
                        Achievement("登峰造极：优伶", "在一名女孩上解锁优伶天赋树上的所有天赋分支。", pic="The Player portrait.webp", pic_path="perks/", target="The Player"),
                        Achievement("登峰造极：模特", "在一名女孩上解锁模特天赋树上的所有天赋分支。", pic="The Model portrait.webp", pic_path="perks/", target="The Model"),
                        Achievement("登峰造极：花魁", "在一名女孩上解锁花魁天赋树上的所有天赋分支。", pic="The Courtesan portrait.webp", pic_path="perks/", target="The Courtesan"),
                        Achievement("登峰造极：伴游", "在一名女孩上解锁伴游天赋树上的所有天赋分支。", pic="The Escort portrait.webp", pic_path="perks/", target="The Escort"),
                        Achievement("登峰造极：狐娘", "在一名女孩上解锁狐娘天赋树上的所有天赋分支。", pic="The Fox portrait.webp", pic_path="perks/", target="The Fox"),
                        Achievement("登峰造极：荡妇", "在一名女孩上解锁荡妇天赋树上的所有天赋分支。", pic="The Slut portrait.webp", pic_path="perks/", target="The Slut"),
                        Achievement("登峰造极：新娘", "在一名女孩上解锁新娘天赋树上的所有天赋分支。", pic="The Bride portrait.webp", pic_path="perks/", target="The Bride"),

                        Achievement("侍奉狂热", "让女孩进行性服侍 %s 次。", pic="egg vibrator.webp", pic_path="items/toy/", target="perform service", level_nb=5, requirements={1 : 1, 2 : 10, 3 : 100, 4 : 1000, 5 : 10000}),
                        Achievement("性爱狂热", "让女孩进行性交 %s 次。", pic="lace panties.webp", pic_path="items/accessory/", target="perform sex", level_nb=5, requirements={1 : 1, 2 : 10, 3 : 100, 4 : 1000, 5 : 10000}),
                        Achievement("肛交狂热", "让女孩进行肛交 %s 次。", pic="butt plug.webp", pic_path="items/toy/", target="perform anal", level_nb=5, requirements={1 : 1, 2 : 10, 3 : 100, 4 : 1000, 5 : 10000}),
                        Achievement("调教狂热", "让女孩进行皮绳愉虐 %s 次。", pic="ropes.webp", pic_path="items/toy/", target="perform fetish", level_nb=5, requirements={1 : 1, 2 : 10, 3 : 100, 4 : 1000, 5 : 10000}),
                        Achievement("双飞狂热", "让女孩进行双飞 %s 次。", pic="black dildo.webp", pic_path="items/toy/", target="perform bisexual", level_nb=5, requirements={1 : 1, 2 : 5, 3 : 25, 4 : 100, 5 : 250}),
                        Achievement("群交狂热", "让女孩进行群交 %s 次。", pic="beer keg.webp", pic_path="items/furniture/", target="perform group", level_nb=5, requirements={1 : 1, 2 : 5, 3 : 25, 4 : 100, 5 : 250}),
                        Achievement("明日之星", "达到 %s 声誉.", pic="star.webp", pic_path="UI/", target="rep", level_nb=5, requirements={1 : 100, 2 : 1000, 3 : 5000, 4 : 10000, 5 : 30000}),
                        Achievement("面面俱到", "在第 %s 章建造所有家具。", pic="steam jacuzzi.webp", pic_path="items/furniture/", target="furniture", level_nb=6, requirements={1 : 2, 2 : 3, 3 : 4, 4 : 5, 5 : 6, 6 : 7}),
                        Achievement("精益求精", "在第 %s 章建造所有升级。", pic="chapel.webp", pic_path="items/furniture/", target="upgrades", level_nb=7, requirements={1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7}),
                        Achievement("一尘不染", "在清洁上花费 %s 金币。", pic="broom.webp", pic_path="items/furniture/", target="gold clean", level_nb=5, requirements={1 : 250, 2 : 1000, 3 : 5000, 4 : 25000, 5 : 100000}),
                        Achievement("好借好还", "偿还银行贷款。", pic="portrait.webp", pic_path="NPC/Banker/", target="first loan"),
                        Achievement("越挫越勇", "输掉一次游戏。", pic="zap traps.webp", pic_path="items/furniture/", target="game over"),
                        Achievement("逃之夭夭", "一个女孩从你身边逃走了。", pic="skull.webp", pic_path="UI/", target="runaway"),
                        Achievement("天罗地网", "你的雇佣兵抓到了逃跑的女孩。", pic="guard portrait.webp", pic_path="NPC/Misc/", target="caught NPC"),
                        Achievement("插翅难逃", "你抓住了一个逃跑的女孩并把她带回来。", target="caught MC"),
                        Achievement("青楼王子", "在普通难度下达到无尽模式。", pic="bronze statue.webp", pic_path="items/furniture/", target="win normal"),
                        Achievement("青楼之王", "在困难难度下达到无尽模式。", pic="silver statue.webp", pic_path="items/furniture/", target="win hard"),
                        Achievement("青楼帝皇", "在最难难度下达到无尽模式。", pic="gold statue.webp", pic_path="items/furniture/", target="win insane"),

                        Achievement("十恶不赦", "施展 %s 种邪恶力量。", pic="evil deck.webp", pic_path="UI/powers/", target="powers", level_nb=5, requirements={1 : 1, 2 : 5, 3 : 25, 4 : 50, 5 : 100}), #!
                        Achievement("紫雨天降", "积累 %s 紫色 魔酒。", pic="purple mojo.webp", pic_path="UI/powers/", target="purple mojo", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 100, 5 : 500}), #!
                        Achievement("绿色园丁", "积累 %s 绿色 魔酒。", pic="orb_green.webp", pic_path="UI/powers/", target="green mojo", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 100, 5 : 500}), #!
                        Achievement("忧郁蓝调", "积累 %s 蓝色 魔酒。", pic="orb_blue.webp", pic_path="UI/powers/", target="blue mojo", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 100, 5 : 500}), #!
                        Achievement("红色警戒", "积累 %s 红色 魔酒。", pic="orb_red.webp", pic_path="UI/powers/", target="red mojo", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 100, 5 : 500}), #!
                        Achievement("黄色病毒", "积累 %s 黄色 魔酒。", pic="orb_yellow.webp", pic_path="UI/powers/", target="yellow mojo", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 100, 5 : 500}), #!
                        Achievement("万念俱灰", "让%s个女孩的心智崩溃。", pic="whip.webp", pic_path="Items/weapon/", target="broken", level_nb=5, requirements={1 : 1, 2 : 3, 3 : 10, 4 : 25, 5 : 50}), #!
                        Achievement("无情无义", "把一个心碎的女孩扔在街上。", pic="navThe Slums_idle.webp", pic_path="UI/", target="broken girl free"), #!
                        Achievement("心存善念", "把一个破碎的女孩送去精神病院。", pic="navThe Cathedra_idle.webp", pic_path="UI/", target="broken girl asylum"), #!
                        Achievement("人才妓妓", "有 %s 个妓女。", pic="brothelnavbutton_idle.webp", pic_path="UI/", target="broken girl street", level_nb=4, requirements={1 : 1, 2 : 3, 3 : 10, 4 : 20}), #!
                        Achievement("混乱无序", "解锁会说话的混沌魔剑。", pic="portrait.webp", pic_path="NPC/Chaos/", target="chaos"),
                        ]

    achievement_dict = {}

    for achv in achievement_list:
        achievement_dict[achv.target] = achv

    # List of achievement targets that are tested with a game.track() update
    tracked_achievements = ["used toy", "farm_days", "had sex", "completed quest", "completed class", "completed contracts", "total_gold", "security events", "neg fixation removed", "hypnotize success", "hypnotize failure", "sell girl gold", "raped", "beaten", "punished", "rewarded", "free girl acquired", "origin stories", "gold spent slavemarket", "gold spent shops", "gold clean", "kosmo"]

    def unlock_achievement(target, level_cap=99):
        if achievement_dict[target].unlock(level_cap):
            renpy.show_screen("achievement_notification", [achievement_dict[target]])
            memorize_achievement(target)

    def reset_achievements():
        global selected_achievement

        for achv in achievement_list:
            achv.level = 0
        persistent.achievements = {}
        selected_achievement = None
        latest_achievements = []

    def test_achievements(target_list):
        r = []
        for target in target_list:
            if achievement_dict[target].test():
                r.append(achievement_dict[target])
                memorize_achievement(target)

        renpy.show_screen("achievement_notification", r)

    def test_achievement(target):
        test_achievements([target])

    def memorize_achievement(target):
        global latest_achievements

        # Rotates the last 3 achievements
        if len(latest_achievements) >=3:
            latest_achievements = [[achievement_dict[target], achievement_dict[target].level]] + latest_achievements[0:2]
        else:
            latest_achievements = [[achievement_dict[target], achievement_dict[target].level]] + latest_achievements

#### END OF BK ACHIEVEMENTS FILE ####
