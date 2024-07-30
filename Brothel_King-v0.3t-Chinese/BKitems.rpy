#### BK ITEMS AND FURNITURE ####
## Labels are used instead of Functions to make sure we are using global variables

## ITEM TYPES ##
init -2 python:
    IT_Weapon = ItemType("Weapon", usage = "wear", slot = "hands", filter = "hands", sound = s_sheath)
    IT_Dress = ItemType("Dress", usage = "wear", slot = "body", filter = "body", sound = "equip dress.ogg", adjectives = "dress")
    IT_Ring = ItemType("Ring", usage = "wear", slot = "finger", filter = "finger", sound = s_equip_item, adjectives = "ring")
    IT_Necklace = ItemType("Necklace", usage = "wear", slot = "neck", filter = "neck", sound = s_equip_item, adjectives = "necklace")
    IT_Accessory = ItemType("Accessory", usage = "wear", slot = "accessory", filter = "accessory", sound = s_equip_item, adjectives = "dress")
    IT_Toy = ItemType("Toy", usage = "auto_rest", filter = "consumable", sound = "vibro.ogg")
    IT_Supplies = ItemType("Supplies", usage = "auto_work", filter = "consumable", sound = "spell.ogg")
    IT_Food = ItemType("Food", usage = "use", filter = "consumable", sound = "crunch.ogg", adjectives = "food") # Food effects may not stack
    IT_Gift = ItemType("Gift", usage = "gift", sound = s_sigh, adjectives = "misc")
    IT_Flower = ItemType("Flower", usage = "gift", sound = s_surprise, adjectives = "misc", dir="Gift")
    IT_Misc = ItemType("Misc", usage = "use", sound = "spell.ogg", adjectives = "misc") # Misc effects may not stack
    IT_Story = ItemType("Misc", usage = None, sound = "spell.ogg", adjectives = "misc", sellable=False, giveable=False)
    IT_Passive = ItemType("Misc", usage = "wear", slot = "misc", sound = s_equip_item, adjectives = "misc", sellable=False)

    all_equipement_types = ["weapon", "dress", "ring", "necklace", "accessory", "passive"]

## FURNITURE TYPES ##
# A tuple (type, description)

    furniture_types = [("Decoration", "吸引更多类型的顾客"),
                       ("Furnishing", "开启更多吸引客户的选择"),
                       ("Utility", "增加广告、安保和清洁的效果"),
                       ("Comfort", "提升女孩们在青楼中的生活质量"),
                       ("Windows", "影响女孩们的习惯和喜好"),
                       ("Altars", "在这里祈祷并获得祝福增益，仅限一次"),
                       ("Arcane", "对举行黑暗仪式有帮助"),
                       ("Gizmos", "来自远古时代的科技产物")
                       ]

## ITEMS ##

label init_items():
    python:

        # REGULAR ITEMS #

        all_items = [
                    Item(name = '短剑', target = 'MC', type = IT_Weapon, pic = 'Short sword.webp', rank = 1, rarity = 1, price = 250, effects = (Effect('change', 'strength', 1), ), description =  "短也有短的好处，你可以轻松地把它藏在身上的每一处。"),
                    Item(name = '弯刀', target = 'MC', type = IT_Weapon, pic = 'Cutlass.webp', rank = 1, rarity = 2, price = 500, effects = (Effect('change', 'strength', 2), ), description =  "它不是一把匕首。它是一把弯刀。"),
                    Item(name = '斧头', target = 'MC', type = IT_Weapon, pic = 'Axe.webp', rank = 2, rarity = 2, price = 1000, effects = (Effect('change', 'strength', 2), Effect('change', 'spirit', 1), ), description =  "斧子不止可以用来砍柴，还可以砍人。"),
                    Item(name = '长枪', target = 'MC', type = IT_Weapon, pic = 'Lance.webp', rank = 2, rarity = 2, price = 2500, effects = (Effect('change', 'strength', 3), Effect('change', 'charisma', 1), ), description =  "枪出如龙！"),
                    Item(name = '长剑', target = 'MC', type = IT_Weapon, pic = 'Long sword.webp', rank = 2, rarity = 3, price = 3500, effects = (Effect('change', 'strength', 3), Effect('change', 'charisma', 1), Effect('change', 'spirit', 1), ), description =  "一寸长，一寸强。"),
                    Item(name = '礼剑', target = 'MC', type = IT_Weapon, pic = 'Rapier.webp', rank = 3, rarity = 3, price = 5000, effects = (Effect('change', 'strength', 4), Effect('change', 'charisma', 2), ), description =  "来自远东岛国的武器，配合武技居合拔刀术可以发挥出极强的战斗力。"),
                    Item(name = '战斧', target = 'MC', type = IT_Weapon, pic = 'Battle axe.webp', rank = 3, rarity = 3, price = 10000, effects = (Effect('change', 'strength', 5), Effect('change', 'spirit', 2), ), description =  ""),
                    Item(name = '战锤', target = 'MC', type = IT_Weapon, pic = 'Warhammer.webp', rank = 3, rarity = 4, price = 17500, effects = (Effect('change', 'strength', 5), Effect('change', 'charisma', 2), Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = '圣剑', target = 'MC', type = IT_Weapon, pic = 'Holy sword.webp', rank = 4, rarity = "U", price = 40000, effects = (Effect('change', 'strength', 6), Effect('change', 'spirit', 3), ), description =  "这把剑嗡嗡地震动着。剑刃平滑如镜，剑柄湿哒哒的，剑之圣女用它做了什么?"),
                    Item(name = '魔剑', target = 'MC', type = IT_Weapon, pic = 'Demon sword.webp', rank = 4, rarity = "S", price = 100000, effects = (Effect('change', 'strength', 8), Effect('change', 'charisma', 4), Effect('change', 'spirit', -2), ), description =  "里面封印的恶魔发出怒吼。据说他会吞噬每一个刀下亡魂。"),
                    Item(name = '扫帚法杖', target = 'MC', type = IT_Weapon, pic = 'Broom staff.webp', rank = 1, rarity = 1, price = 250, effects = (Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = '朽木法杖', target = 'MC', type = IT_Weapon, pic = 'Wooden staff.webp', rank = 1, rarity = 2, price = 500, effects = (Effect('change', 'spirit', 2), ), description =  "常见的魔杖，适合法师学徒使用。"),
                    Item(name = '地精法杖', target = 'MC', type = IT_Weapon, pic = 'Goblin staff.webp', rank = 2, rarity = 2, price = 1000, effects = (Effect('change', 'charisma', 1), Effect('change', 'spirit', 2), ), description =  "哥布林法师被消灭后掉落的装备，据说哥布林用它施展催眠咒语。"),
                    Item(name = '黄铜法杖', target = 'MC', type = IT_Weapon, pic = 'Bronze staff.webp', rank = 2, rarity = 2, price = 2500, effects = (Effect('change', 'strength', 1), Effect('change', 'spirit', 3), ), description =  "比起木质法杖，金属法杖要更加稳定和可靠。"),
                    Item(name = '灵风法杖', target = 'MC', type = IT_Weapon, pic = 'Wind staff.webp', rank = 2, rarity = 3, price = 3500, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 1), Effect('change', 'spirit', 3), ), description =  "施展风系魔法可以让你的行动更加灵活。"),
                    Item(name = '治愈法杖', target = 'MC', type = IT_Weapon, pic = 'Healing staff.webp', rank = 3, rarity = 3, price = 5000, effects = (Effect('change', 'charisma', 2), Effect('change', 'spirit', 4), ), description =  ""),
                    Item(name = '雷霆法杖', target = 'MC', type = IT_Weapon, pic = 'Thunder staff.webp', rank = 3, rarity = 3, price = 10000, effects = (Effect('change', 'strength', 2), Effect('change', 'spirit', 5), ), description =  ""),
                    Item(name = '碧玉法杖', target = 'MC', type = IT_Weapon, pic = 'Emerald staff.webp', rank = 3, rarity = 4, price = 17500, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 2), Effect('change', 'spirit', 5), ), description =  ""),
                    Item(name = '水晶法杖', target = 'MC', type = IT_Weapon, pic = 'Crystal staff.webp', rank = 4, rarity = 4, price = 40000, effects = (Effect('change', 'strength', 3), Effect('change', 'spirit', 6), ), description =  ""),
                    Item(name = '天使法杖', target = 'MC', type = IT_Weapon, pic = 'Angel staff.webp', rank = 4, rarity = 5, price = 100000, effects = (Effect('change', 'charisma', 2), Effect('change', 'spirit', 8), ), description =  ""),
                    Item(name = '飞刀', target = 'MC', type = IT_Weapon, pic = 'Throwing knife.webp', rank = 1, rarity = 1, price = 250, effects = (Effect('change', 'charisma', 1), ), description =  ""),
                    Item(name = '飞斧', target = 'MC', type = IT_Weapon, pic = 'Throwing axe.webp', rank = 1, rarity = 2, price = 500, effects = (Effect('change', 'charisma', 2), ), description =  ""),
                    Item(name = '短弓', target = 'MC', type = IT_Weapon, pic = 'Bow.webp', rank = 2, rarity = 2, price = 1000, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 2), ), description =  ""),
                    Item(name = '华丽的弓', target = 'MC', type = IT_Weapon, pic = 'Ornate bow.webp', rank = 2, rarity = 2, price = 2500, effects = (Effect('change', 'charisma', 3), Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = '燧发枪', target = 'MC', type = IT_Weapon, pic = 'Flintlock.webp', rank = 2, rarity = 3, price = 3500, effects = (Effect('change', 'strength', 2), Effect('change', 'charisma', 3), ), description =  ""),
                    Item(name = '十字弩', target = 'MC', type = IT_Weapon, pic = 'Crossbow.webp', rank = 3, rarity = 3, price = 5000, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 4), Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = '惩罚者', target = 'MC', type = IT_Weapon, pic = 'Repeater.webp', rank = 3, rarity = 3, price = 10000, effects = (Effect('change', 'strength', 2), Effect('change', 'charisma', 5), ), description =  ""),
                    Item(name = '雷筒', target = 'MC', type = IT_Weapon, pic = 'Blunderbuss.webp', rank = 3, rarity = 4, price = 17500, effects = (Effect('change', 'strength', 3), Effect('change', 'charisma', 5), ), description = "这！就是！我的火枪！"),
                    Item(name = '神圣手雷', target = 'MC', type = IT_Weapon, pic = 'Holy handgrenade.webp', rank = 4, rarity = 4, price = 40000, effects = (Effect('change', 'charisma', 6), Effect('change', 'spirit', 3), ), description =  ""),
                    Item(name = '死亡射线', target = 'MC', type = IT_Weapon, pic = 'Death dispenser.webp', rank = 4, rarity = 5, price = 100000, effects = (Effect('change', 'strength', 4), Effect('change', 'charisma', 8), Effect('change', 'spirit', -2), ), description =  ""),
                    Item(name = '太阳神的祝福', target = 'MC', type = IT_Necklace, pic = 'Arios amulet.webp', rank = 1, rarity = "U", price = 25000, effects = (), description = "完成太阳神教骑士任务的独特奖励。"),
                    Item(name = '莎莉娅的凝视', target = 'MC', type = IT_Necklace, pic = 'Shalia talisman.webp', rank = 1, rarity = "U", price = 25000, effects = (), description = "完成黑暗女神莎莉娅任务的独特奖励。"),
                    Item(name = '商会的印章', target = 'MC', type = IT_Necklace, pic = 'Merchant sigil.webp', rank = 1, rarity = "U", price = 25000, effects = (), description = "完成商人公会任务的独特奖励。"),
                    Item(name = '皮草靴', target = 'MC', type = IT_Accessory, pic = 'Fur boots.webp', rank = 1, rarity = 1, price = 500, effects = (Effect('change', 'speed', 1), ), ),
                    Item(name = '皮革靴', target = 'MC', type = IT_Accessory, pic = 'Leather boots.webp', rank = 1, rarity = 2, price = 2000, effects = (Effect('change', 'speed', 2), ), ),
                    Item(name = '精灵长靴', target = 'MC', type = IT_Accessory, pic = 'Elven boots.webp', rank = 2, rarity = 3, price = 10000, effects = (Effect('change', 'speed', 3), ), ),
                    Item(name = '骏马', target = 'MC', type = IT_Accessory, pic = 'Horse.webp', rank = 3, rarity = 4, price = 50000, effects = (Effect('change', 'speed', 4), ), ),
                    Item(name = '汗血宝马', target = 'MC', type = IT_Accessory, pic = 'Dark horse.webp', rank = 4, rarity = 5, price = 150000, effects = (Effect('change', 'speed', 5), ), ),
                    Item(name = '龙蛋', target = 'MC', type = IT_Misc, pic = 'Dragon egg.webp', rank = 1, rarity = "S", charges = 1, price = 5000, effects = (Effect('gain', 'skill points', 1), ), description =  "'哪来的龙蛋...'\n弄坏了它后果自负!", sound = "crunch.ogg", hidden_effect = True),
                    Item(name = '指虎', target = 'girl', type = IT_Weapon, pic = 'Knuckle duster.webp', rank = 1, rarity = 1, price = 50, effects = (Effect('change', 'defense', 1), ), ),
                    Item(name = '弯钩', target = 'girl', type = IT_Weapon, pic = 'Hook.webp', rank = 1, rarity = 1, price = 250, effects = (Effect('change', 'defense', 2), ), ),
                    Item(name = '剃刀', target = 'girl', type = IT_Weapon, pic = 'Shiv.webp', rank = 1, rarity = 2, price = 500, effects = (Effect('change', 'defense', 3), ), ),
                    Item(name = '小刀', target = 'girl', type = IT_Weapon, pic = 'Knife.webp', rank = 2, rarity = 2, price = 1000, effects = (Effect('change', 'defense', 4), ), ),
                    Item(name = '匕首', target = 'girl', type = IT_Weapon, pic = 'Dagger.webp', rank = 2, rarity = 2, price = 1750, effects = (Effect('change', 'defense', 5), ), ),
                    Item(name = '祭刀', target = 'girl', type = IT_Weapon, pic = 'Sacrificial knife.webp', rank = 2, rarity = 3, price = 2750, effects = (Effect('change', 'defense', 6), ), ),
                    Item(name = '棍棒', target = 'girl', type = IT_Weapon, pic = 'Mace.webp', rank = 3, rarity = 3, price = 5000, effects = (Effect('change', 'defense', 7), ), ),
                    Item(name = '皮鞭', target = 'girl', type = IT_Weapon, pic = 'Whip.webp', rank = 3, rarity = 4, price = 10000, effects = (Effect('change', 'defense', 8), ), ),
                    Item(name = '钢鞭', target = 'girl', type = IT_Weapon, pic = 'Steel whip.webp', rank = 4, rarity = 4, price = 25000, effects = (Effect('change', 'defense', 9), ), ),
                    Item(name = '秘法之刃', target = 'girl', type = IT_Weapon, pic = 'Magic blade.webp', rank = 4, rarity = 5, price = 60000, effects = (Effect('change', 'defense', 10), ), ),
                    Item(name = '振动棒', target = 'girl', type = IT_Toy, pic = 'Dildo.webp', rank = 1, rarity = 2, charges = 8, price = 125, effects = (Effect('gain', 'sex', 1, 0.5), ), description = "休息时概率提升性交技术。 (使用次数有限)。"),
                    Item(name = '大号振动棒', target = 'girl', type = IT_Toy, pic = 'XL dildo.webp', rank = 2, rarity = 3, charges = 8, price = 500, effects = (Effect('gain', 'sex', 2, 0.5), ), description = "休息时概率提升性交技术。 (使用次数有限)。"),
                    Item(name = '超大号振动棒', target = 'girl', type = IT_Toy, pic = 'XXL dildo.webp', rank = 3, rarity = 4, charges = 8, price = 2500, effects = (Effect('gain', 'sex', 3, 0.5), ), description = "休息时概率提升性交技术。 (使用次数有限)。"),
                    Item(name = '黑人倒模肉棒', target = 'girl', type = IT_Toy, pic = 'Black dildo.webp', rank = 4, rarity = 5, charges = 8, price = 10000, effects = (Effect('gain', 'sex', 5, 0.5), ), description = "休息时概率提升性交技术。 (使用次数有限)。"),
                    Item(name = '肛塞', target = 'girl', type = IT_Toy, pic = 'Butt plug.webp', rank = 1, rarity = 2, charges = 8, price = 125, effects = (Effect('gain', 'anal', 1, 0.5), ), description = "休息时概率提升肛交技术。 (使用次数有限)。"),
                    Item(name = '打气筒', target = 'girl', type = IT_Toy, pic = 'Butt pump.webp', rank = 2, rarity = 3, charges = 8, price = 500, effects = (Effect('gain', 'anal', 2, 0.5), ), description = "休息时概率提升肛交技术。 (使用次数有限)。"),
                    Item(name = '肛门振动棒', target = 'girl', type = IT_Toy, pic = 'Anal dildo.webp', rank = 3, rarity = 4, charges = 8, price = 2500, effects = (Effect('gain', 'anal', 3, 0.5), ), description = "休息时概率提升肛交技术。 (使用次数有限)。"),
                    Item(name = '拉珠', target = 'girl', type = IT_Toy, pic = 'Anal beads.webp', rank = 4, rarity = 5, charges = 8, price = 10000, effects = (Effect('gain', 'anal', 5, 0.5), ), description = "休息时概率提升肛交技术。 (使用次数有限)。"),
                    Item(name = '麻绳', target = 'girl', type = IT_Toy, pic = 'Ropes.webp', rank = 1, rarity = 2, charges = 8, price = 125, effects = (Effect('gain', 'fetish', 1, 0.5), ), description = "休息时概率提升调教技术。 (使用次数有限)。"),
                    Item(name = '手铐', target = 'girl', type = IT_Toy, pic = 'Cuffs.webp', rank = 2, rarity = 3, charges = 8, price = 500, effects = (Effect('gain', 'fetish', 2, 0.5), ), description = "休息时概率提升调教技术。 (使用次数有限)。"),
                    Item(name = '口球', target = 'girl', type = IT_Toy, pic = 'Gag.webp', rank = 3, rarity = 4, charges = 8, price = 2500, effects = (Effect('gain', 'fetish', 3, 0.5), ), description = "休息时概率提升调教技术。 (使用次数有限)。"),
                    Item(name = '眼罩', target = 'girl', type = IT_Toy, pic = 'Blindfold.webp', rank = 4, rarity = 5, charges = 8, price = 10000, effects = (Effect('gain', 'fetish', 5, 0.5), ), description = "休息时概率提升调教技术。 (使用次数有限)。"),
                    Item(name = '催情凝胶', target = 'girl', type = IT_Toy, pic = 'Arousing gel.webp', rank = 1, rarity = 2, charges = 8, price = 125, effects = (Effect('gain', 'service', 1, 0.5), ), description = "休息时概率提升侍奉技术。 (使用次数有限)。"),
                    Item(name = '跳蛋', target = 'girl', type = IT_Toy, pic = 'Egg vibrator.webp', rank = 2, rarity = 3, charges = 8, price = 500, effects = (Effect('gain', 'service', 2, 0.5), ), description = "休息时概率提升侍奉技术。 (使用次数有限)。"),
                    Item(name = '线控跳蛋', target = 'girl', type = IT_Toy, pic = 'Long vibrator.webp', rank = 3, rarity = 4, charges = 8, price = 2500, effects = (Effect('gain', 'service', 3, 0.5), ), description = "休息时概率提升侍奉技术。 (使用次数有限)。"),
                    Item(name = '振动棒', target = 'girl', type = IT_Toy, pic = 'Arcanic vibrator.webp', rank = 4, rarity = 5, charges = 8, price = 10000, effects = (Effect('gain', 'service', 5, 0.5), ), description = "休息时概率提升侍奉技术。 (使用次数有限)。"),
                    Item(name = '幸运兔脚', target = 'girl', type = IT_Necklace, pic = 'Lucky charm.webp', rank = 1, rarity = 2, price = 1250, effects = (Effect('special', 'lucky', 1), ), description = "据说它能给主人带来好运。兔子表示纯属造谣……"),
                    Item(name = '皮革项圈', target = 'girl', type = IT_Necklace, pic = 'Leather choker.webp', rank = 1, rarity = 2, price = 750, effects = (Effect('boost', 'obedience tests', 0.2), ), ),
                    Item(name = '青铜护身符', target = 'girl', type = IT_Necklace, pic = 'Bronze amulet.webp', rank = 2, rarity = 3, price = 2500, effects = (Effect('boost', 'all regular skills gains', 0.05), ), ),
                    Item(name = '秘银护身符', target = 'girl', type = IT_Necklace, pic = 'Silver amulet.webp', rank = 3, rarity = 4, price = 12500, effects = (Effect('boost', 'all regular skills gains', 0.1), ), ),
                    Item(name = '黄金护身符', target = 'girl', type = IT_Necklace, pic = 'Gold amulet.webp', rank = 4, rarity = 5, price = 25000, effects = (Effect('boost', 'all regular skills gains', 0.15), ), ),
                    Item(name = '魔兽核项链', target = 'girl', type = IT_Necklace, pic = 'Monster pearl necklace.webp', rank = 3, rarity = 5, price = 25000, effects = (Effect('boost', 'all sex skills gains', 0.1), ), description =  "这是从深海沉船中打捞上来的……"),
                    Item(name = '精酿麦酒', target = 'girl', type = IT_Supplies, pic = 'Ale.webp', rank = 1, rarity = 1, charges = 10, price = 500, effects = (Effect('change', 'waitress results', 1), ), description =  "在工作中发挥效果"),
                    Item(name = '按摩油', target = 'girl', type = IT_Supplies, pic = 'Massage oil.webp', rank = 1, rarity = 1, charges = 10, price = 500, effects = (Effect('change', 'masseuse results', 1), ), description =  "在工作中发挥效果"),
                    Item(name = '防晒油', target = 'girl', type = IT_Supplies, pic = 'Tanning oil.webp', rank = 1, rarity = 1, charges = 10, price = 500, effects = (Effect('change', 'dancer results', 1), ), description =  "在工作中发挥效果"),
                    Item(name = '折扇', target = 'girl', type = IT_Supplies, pic = 'Fans.webp', rank = 1, rarity = 1, charges = 10, price = 500, effects = (Effect('change', 'geisha results', 1), ), description =  "在工作中发挥效果"),
                    Item(name = '秘制香水', target = 'girl', type = IT_Supplies, pic = 'Sensual perfume.webp', rank = 1, rarity = 3, charges = 10, price = 750, effects = (Effect('change', 'service results', 1), ), description =  "在工作中发挥效果"),
                    Item(name = '凝胶', target = 'girl', type = IT_Supplies, pic = 'Gel.webp', rank = 1, rarity = 3, charges = 10, price = 750, effects = (Effect('change', 'sex results', 1), ), description =  "在工作中发挥效果"),
                    Item(name = '灌肠剂', target = 'girl', type = IT_Supplies, pic = 'Enema.webp', rank = 1, rarity = 3, charges = 10, price = 750, effects = (Effect('change', 'anal results', 1), ), description =  "在工作中发挥效果"),
                    Item(name = '低温蜡烛', target = 'girl', type = IT_Supplies, pic = 'Wax.webp', rank = 1, rarity = 3, charges = 10, price = 750, effects = (Effect('change', 'fetish results', 1), ), description =  "在工作中发挥效果"),
                    Item(name = '飞龙蛋', target = 'girl', type = IT_Misc, pic = 'Wyvern egg.webp', rank = 1, rarity = "S", charges = 1, price = 15000, effects = (Effect('gain', 'perk', 1), ), description = "适合女性保持身材的佳肴。", sound = "crunch.ogg"),
                    Item(name = '眼镜', target = 'girl', type = IT_Accessory, pic = 'Glasses.webp', rank = 1, rarity = 3, price = 1000, effects = (Effect('boost', 'xp gains', 0.1), ), ),
                    Item(name = '假尾巴', target = 'girl', type = IT_Accessory, pic = 'Tail.webp', rank = 1, rarity = 3, price = 1000, effects = (Effect('boost', 'reputation gains', 0.2), ), ),
                    Item(name = '兔耳发饰', target = 'girl', type = IT_Accessory, pic = 'Bunny ears.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'waitress results', 1), ), ),
                    Item(name = '发簪', target = 'girl', type = IT_Accessory, pic = 'Hairpin.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'masseuse results', 1), ), ),
                    Item(name = '修女面纱', target = 'girl', type = IT_Accessory, pic = 'Nun veil.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'dancer results', 1), ), ),
                    Item(name = '艺伎面具', target = 'girl', type = IT_Accessory, pic = 'Noh mask.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'geisha results', 1), ), ),
                    Item(name = '猫耳发饰', target = 'girl', type = IT_Accessory, pic = 'Cat ears.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'service results', 1), ), ),
                    Item(name = '护士帽', target = 'girl', type = IT_Accessory, pic = 'Nurse hat.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'sex results', 1), ), ),
                    Item(name = '皮革帽', target = 'girl', type = IT_Accessory, pic = 'Leather cap.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'anal results', 1), ), ),
                    Item(name = '女仆头带', target = 'girl', type = IT_Accessory, pic = 'Maid hat.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'fetish results', 1), ), ),
                    Item(name = '魔法笔记本', target = 'MC', type = IT_Passive, pic = 'Magic notebook.webp', template = False, rank = 1, rarity = "S", price = 0, effects = (Effect('special', 'notebook', 1), ), description = "这个魔法笔记本将存储你知道的所有关于你的女孩的信息。它记录了你所有的想法。等等，别用它来{i}做那种事{/i}……太晚了吗。", hidden_effect = True),
                    Item(name = '愈合粉', target = 'minion', type = IT_Misc, pic = 'healing powder.webp', template = False, rank = 1, rarity = "M", charges = 1, price = 100, effects = (Effect('special', 'heal minion', 1), ), description = "这种来自东方的神秘粉末可以治愈仆从的伤口或修复魔工机械。但是副作用可能包括头晕，皮肤鳞片化，长出触手。"),
                    Item(name = '席米亚科技废料', target = 'misc', type = IT_Misc, pic = 'Cimerian scrap.webp', sound=s_vibro, template = False, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 250, effects = (), description = "一个神秘的古代科技残件。只是个垃圾。"),
                    Item(name = '席米亚科技产物', target = 'misc', type = IT_Misc, pic = 'Cimerian artefact.webp', sound=s_vibro, template = False, rank = 1, max_rank = 5, rarity = 4, charges = 1, price = 1000, effects = (), description = "一个神秘的古代科技器械，但还是坨废铁。"),
                    Item(name = "避雷针", target = 'MC', type = IT_Story, pic = "lightning rod.webp", template=False, rank=2, max_rank = 5, rarity=3, price = 1000, effects = (), description = "防止被雷劈。在某些场合，它可以救你一命，尽管在青楼工作时被闪电击中的几率非常低。有这钱买点安全套和避孕药可能更有用。"),

                    Item(name = '白色鲜花', target = 'girl', type = IT_Flower, pic = 'White flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'white', 1), ), description = "白色鲜花象征着纯洁的爱情，也可能是白浊的精液覆盖在花穴。", hidden_effect = True),
                    Item(name = '黄色鲜花', target = 'girl', type = IT_Flower, pic = 'Yellow flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'yellow', 1), ), description = "黄色鲜花带有今晚想要和你上床的暗示，送几朵做几次。", hidden_effect = True),
                    Item(name = '红色鲜花', target = 'girl', type = IT_Flower, pic = 'Red flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'red', 1), ), description = "红色鲜花常被用来告白和求婚，你们的关系已经到这一步了，或者更深？", hidden_effect = True),
                    Item(name = '绿色鲜花', target = 'girl', type = IT_Flower, pic = 'Green flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'green', 1), ), description = "绿色鲜花可以直接生吞，有时会有催情作用，悄悄地加在食物里也不错。", hidden_effect = True),
                    Item(name = '蓝色鲜花', target = 'girl', type = IT_Flower, pic = 'Blue flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'blue', 1), ), description = "蓝色鲜花代表孤独和忧郁，她需要你的安慰和满足。", hidden_effect = True),
                    Item(name = '橙色鲜花', target = 'girl', type = IT_Flower, pic = 'Orange flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'orange', 1), ), description = "橙色鲜花接触皮肤会让皮肤变得十分敏感，你想涂在哪里？", hidden_effect = True),
                    Item(name = '紫色鲜花', target = 'girl', type = IT_Flower, pic = 'Purple flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'purple', 1), ), description = "紫色鲜花暗示今晚你可以对她为所欲为，如果她接受的话。", hidden_effect = True),
                    Item(name = '粉色鲜花', target = 'girl', type = IT_Flower, pic = 'Pink flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'pink', 1), ), description = "粉色鲜花常会刺激女性的乳头和阴蒂变得肥大充满弹性。", hidden_effect = True),
                    Item(name = '黑色鲜花', target = 'girl', type = IT_Flower, pic = 'Black flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'black', 1), ), description = "黑色鲜花具有安神作用，催眠洗脑前闻一闻效果更佳哦。", hidden_effect = True),
                    ]


        # SPECIAL ITEMS AND FURNITURE #

        blueprint_item = Item(name = '古代蓝图', target = 'MC', type = IT_Story, pic = 'scanner blueprint.webp', template = False, rank = 1, rarity = "S", price = 0, effects = [], description = "一种画在轻而结实的纸状材料上的古代蓝图。上面的文字不像是你了解的语言，难以辨认，熟练的工匠也许能理解。", hidden_effect = True)

        vitals_scanner = Furniture('古怪的机器', type='Gizmos', pic='scanner.webp', rank=2, chapter=2, cost=[('wood', 20), ('dye', 20), ('leather', 20)], duration=4, effects=[Effect("special", "autorest", 1, scope="brothel")], base_description="这个神秘的机器散发着脉动的魔法能量。") #  It scans your girls automatically to make sure they are fit to work.

        billboard = Furniture('钟表广告牌', type='Furnishing', pic='billboard.webp', rank=2, chapter=2, cost=[('wood', 40), ('dye', 25), ('leather', 10)], duration=5, effects=[Effect("special", "advanced advertising", 1, scope="brothel")], base_description="这个雄伟的广告牌一定会吸引一些人的注意。解锁高级广告设置。") #  Unlocks advanced advertising settings

        bast_letter = Item("巴斯特的情书", "MC", type=IT_Story, pic="Scroll of etiquette.webp", template = False, rank = 1, rarity = "S", price = 0, effects = [], description = "巴斯特写给前男友的情书。包含违法信息。", hidden_effect = True)

        extractor_items = {"extractor1" : Item(name="采集者MkI型", target="MC", type=IT_Story, pic="extractor1.webp", template = False, rarity = "S", price = 5000, effects=[], description = "这台奇怪的机器可以自动采集木材、染色或皮革。你需要到现场部署。"),
                           "extractor2" : Item(name="采集者MkII型", target="MC", type=IT_Story, pic="extractor2.webp", template = False, rarity = "S", price = 25000, effects=[], description = "这台奇怪的机器可以自动采集大理石、丝绸或矿石。你需要到现场部署。"),
                            }

        magic_notebook = Item(name = '魔法笔记本', target = 'MC', type = IT_Passive, pic = 'Magic notebook.webp', template = False, rank = 1, rarity = "S", price = 0, effects = (Effect('special', 'notebook', 1), ), description = "这个魔法笔记本将存储你知道的所有关于你的女孩的信息。它记录了你所有的想法。等等，别用它来{i}做那种事{/i}……太晚了吗。", hidden_effect = True)

        mania_amulet = Item(name = "廉价的符咒", target = 'MC', type = IT_Story, pic = 'cheap charm.webp', template = False, rank = 1, rarity = "S", price = 10, description = "在公会总部发现的一个廉价的护身符，上面还有一封神秘的信，上面提到了一个名为“狂热”的俱乐部。", hidden_effect = True)

        toy_hammer = Item(name="玩具锤", target = 'MC', type = IT_Story, pic = 'toy hammer.webp', template = False, rank = 1, rarity = "S", price = 0, description = "由廉价材料制成的小型“战锤”。据说可以用来对付女忍者的，但看起来连只老鼠都打不了。", hidden_effect = True)

        mizuki_kimono = Item(name = "美月的和服", target = 'MC', type = IT_Story, pic = 'Kimono.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="dress", description = "神秘的女忍者美月遗失的和服。", hidden_effect = True)

        makibishi = Item(name = "蒺藜", target = 'MC', type = IT_Misc, pic = 'bronze makibishi.webp', template = False, rank = 1, rarity = "S", price = 500, description = "在狩猎忍者的过程中自动抓住忍者。", hidden_effect = True)
#                       Item(name = "Iron Makibishi", target = 'MC', type = IT_Story, pic = 'iron makibishi.webp', template = False, rank = 2, rarity = "S", price = 1000, description = "Slows down Kunoichi movements during ninja hunt (medium effect).", hidden_effect = True),
#                       Item(name = "Steel Makibishi", target = 'MC', type = IT_Story, pic = 'steel makibishi.webp', template = False, rank = 3, rarity = "S", price = 1500, description = "Slows down Kunoichi movements during ninja hunt (large effect).", hidden_effect = True),

        narika_hair = Item(name = "成香的一绺头发", target = 'MC', type = IT_Story, pic = 'hair.webp', template = False, rank = 1, rarity = "S", price = 0, description = "一绺粉红色的头发，属于女忍者四方堂-鸣香。", hidden_effect = True)

        blue_ribbon = Item(name = "焰的丝带", target = 'MC', type = IT_Story, pic = 'blue ribbon.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="necklace", description = "焰女士给予你的丝带. 把丝带绑在 {b}广场{/b} 的路灯上她就知道你想要见她。", hidden_effect = True)

        earth_rune = Item(name = "大地符石", target = 'MC', type = IT_Story, pic = 'earth rune.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="misc", description = "这块符石对土系魔法有很强的抑制作用，并使其使用者迷失方向。这能帮你对付土之忍者。", hidden_effect = True)
        water_rune = Item(name = "水之符石", target = 'MC', type = IT_Story, pic = 'water rune.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="misc", description = "这块符石对水系魔法有很强的抑制作用，并使其使用者迷失方向。这能帮你对付水之忍者。", hidden_effect = True)
        void_rune = Item(name = "虚空符石", target = 'MC', type = IT_Story, pic = 'void rune.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="misc", description = "这块符石对虚空魔法有很强的抑制作用，并使其使用者迷失方向。这能帮你对付虚空忍者。", hidden_effect = True)
        fire_rune = Item(name = "烈焰符石", target = 'MC', type = IT_Story, pic = 'fire rune.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="misc", description = "这块符石对火焰魔法有很强的抑制作用，并使其使用者迷失方向。但你不认识任何火焰魔法的使用者，这对你真的有用吗?", hidden_effect = True)

        # Chaos

        chaos_full_charge = Item(name = '暴走的魔剑', target = 'MC', type = IT_Weapon, sellable=False, giveable=False, pic = 'Demon sword.webp', rank = 4, rarity = "S", price = 0, effects = (Effect('change', 'strength', 4), Effect('change', 'charisma', 4), Effect('change', 'spirit', 4)), description = "剑刃随着封印在里面的恶魔的怒火颤动。它从和女孩们嬉戏中获得能量。它的能量已经溢满了。")
        chaos_high_charge = Item(name = '充能的魔剑', target = 'MC', type = IT_Weapon, sellable=False, giveable=False, pic = 'Demon sword.webp', rank = 4, rarity = "S", price = 0, effects = (Effect('change', 'strength', 3), Effect('change', 'charisma', 3), Effect('change', 'spirit', 3)), description = "剑刃随着封印在里面的恶魔的怒火颤动。它从和女孩们嬉戏中获得能量。它的能量恢复了许多。")
        chaos_low_charge = Item(name = '饥饿的魔剑', target = 'MC', type = IT_Weapon, sellable=False, giveable=False, pic = 'Demon sword.webp', rank = 4, rarity = "S", price = 0, effects = (Effect('change', 'strength', 2), Effect('change', 'charisma', 2), Effect('change', 'spirit', 2)), description = "剑刃随着封印在里面的恶魔的怒火颤动。它从和女孩们嬉戏中获得能量。它的能量得到了一些补充。")
        chaos_no_charge = Item(name = '虚弱的魔剑', target = 'MC', type = IT_Weapon, sellable=False, giveable=False, pic = 'Demon sword.webp', rank = 4, rarity = "S", price = 0, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 1), Effect('change', 'spirit', 1)), description = "剑刃随着封印在里面的恶魔的怒火颤动。它从和女孩们嬉戏中获得能量。它一点能量也没有。")

        # TEMPLATE ITEMS #

        template_items =   [
                            Item(name = '原味内裤', target = 'MC', type = IT_Misc, pic = 'Stolen underwear.webp', template = True, rank = 1, max_rank = 5, rarity = "S", charges = 1, price = 500, effects = (Effect('gain', 'prestige', 2), ), description = "原来你喜欢别人穿过的内裤？"),
                            Item(name = '言情小说', target = 'gift', type = IT_Gift, pic = 'Romantic novel.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'cute', 1), Effect('gift', 'book', 1), ), description =  "一个身穿闪亮盔甲的骑士，一位公主，一个水管工。一如既往。", hidden_effect = True),
                            Item(name = '工口读物', target = 'gift', type = IT_Gift, pic = 'Erotic manual.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'erotica', 1), Effect('gift', 'book', 1), ), description =  "50个只有使用黑魔法才能实现的姿势。", hidden_effect = True),
                            Item(name = '金箔笔记', target = 'gift', type = IT_Gift, pic = 'Goldleaf book.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'precious', 1), Effect('gift', 'book', 1), ), description =  "里面写了什么？谁在乎这些，看这闪亮的封面！", hidden_effect = True),
                            Item(name = '魔药大全', target = 'gift', type = IT_Gift, pic = 'Book of magical cocktails.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'drinks', 1), Effect('gift', 'book', 1), ), description =  "警告：饮用这些药水可能会导致丧失记忆。还有尊严。", hidden_effect = True),
                            Item(name = '宠物', target = 'gift', type = IT_Gift, pic = 'Pet.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'cute', 1), Effect('gift', 'precious', 1), ), description =  "他是不是很可爱？只要他不咬你的手……", hidden_effect = True),
                            Item(name = '轻纱睡衣', target = 'gift', type = IT_Gift, pic = 'Silky nighties.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'cute', 1), Effect('gift', 'erotica', 1), ), description =  "光滑而又性感。", hidden_effect = True),
                            Item(name = '樱花清酒', target = 'gift', type = IT_Gift, pic = 'Sakura liquor.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'cute', 1), Effect('gift', 'drinks', 1), ), description =  "一种由蒸馏花瓣制成的微妙的饮料。", hidden_effect = True),
                            Item(name = '高跟鞋', target = 'gift', type = IT_Gift, pic = 'Sexy high heels.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'erotica', 1), Effect('gift', 'precious', 1), ), description =  "有些女人会不顾一切得到这双鞋。说实话，它们有点血迹斑斑。", hidden_effect = True),
                            Item(name = '香槟酒', target = 'gift', type = IT_Gift, pic = 'Champagne.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'drinks', 1), Effect('gift', 'precious', 1), ), description =  "'暴发户': 一种烈性酒;这是一种声明，证明你买得起。", hidden_effect = True),
                            Item(name = '催情剂', target = 'gift', type = IT_Gift, pic = 'Aphrodisiac.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'drinks', 1), Effect('gift', 'erotica', 1), ), description =  "让你欲火焚身……", hidden_effect = True),
                            Item(name = '精美戒指', target = 'girl', type = IT_Ring, pic = 'Pretty ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 150, effects = (Effect('change', 'beauty', 5), ), ),
                            Item(name = '青铜戒指', target = 'girl', type = IT_Ring, pic = 'Bronze ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 150, effects = (Effect('change', 'body', 5), ), ),
                            Item(name = '财富之戒', target = 'girl', type = IT_Ring, pic = 'Zanic ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 150, effects = (Effect('change', 'charm', 5), ), ),
                            Item(name = '秘银戒指', target = 'girl', type = IT_Ring, pic = 'Silver ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 150, effects = (Effect('change', 'refinement', 5), ), ),
                            Item(name = '黄金戒指', target = 'girl', type = IT_Ring, pic = 'Gold ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'libido', 5), ), ),
                            Item(name = '海风指环', target = 'girl', type = IT_Ring, pic = 'Marine ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'sensitivity', 5), ), ),
                            Item(name = '精钢指环', target = 'girl', type = IT_Ring, pic = 'Iron ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 375, effects = (Effect('change', 'obedience', 5), ), ),
                            Item(name = '橡木指环', target = 'girl', type = IT_Ring, pic = 'Wooden ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'constitution', 5), ), ),
                            Item(name = '蓝色丝带', target = 'girl', type = IT_Necklace, pic = 'Blue ribbon.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 100, effects = (Effect('boost', 'beauty gains', 0.1), ), ),
                            Item(name = '珍珠项链', target = 'girl', type = IT_Necklace, pic = 'Pearl necklace.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 100, effects = (Effect('boost', 'body gains', 0.1), ), ),
                            Item(name = '新月项链', target = 'girl', type = IT_Necklace, pic = 'Moon necklace.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 100, effects = (Effect('boost', 'charm gains', 0.1), ), ),
                            Item(name = '象牙项链', target = 'girl', type = IT_Necklace, pic = 'Ivory necklace.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 100, effects = (Effect('boost', 'refinement gains', 0.1), ), ),
                            Item(name = '奴隶项圈', target = 'girl', type = IT_Necklace, pic = 'Choker necklace.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('boost', 'libido gains', 0.1), ), ),
                            Item(name = '母狗项圈', target = 'girl', type = IT_Necklace, pic = 'Dog collar.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('boost', 'obedience gains', 0.1), ), ),
                            Item(name = '银制项圈', target = 'girl', type = IT_Necklace, pic = 'Silver chain.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('boost', 'sensitivity gains', 0.1), ), ),
                            Item(name = '兄弟会项链', target = 'girl', type = IT_Necklace, pic = 'Dagger necklace.webp', template = True, rank = 1, max_rank = 5, rarity = 2, price = 250, effects = (Effect('boost', 'constitution gains', 0.1), ), ),
                            Item(name = '金币袋', target = 'girl', type = IT_Misc, pic = 'Gold bag.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 600, effects = (Effect('special', 'level', 5), ), description =  "立即升级。明智地使用它……", adjectives = "ring"),
                            Item(name = '珠宝袋', target = 'girl', type = IT_Misc, pic = 'Jewel bag.webp', template = True, rank = 1, max_rank = 5, rarity = 3, charges = 1, price = 500, effects = (Effect('gain', 'skill points', 5), ), description =  "获得额外的属性点。"),
                            Item(name = '知识卷轴', target = 'girl', type = IT_Misc, pic = 'Knowledge scroll.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 400, effects = (Effect('gain', 'xp', 50), ), description =  "免费获得经验值。", adjectives = "scroll"),
                            Item(name = '医疗包', target = 'girl', type = IT_Misc, pic = 'Medicine bag.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 250, effects = (Effect('instant', 'heal', 2), ), description =  ""),
                            Item(name = '营养品', target = 'girl', type = IT_Misc, pic = 'Tonic.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 75, effects = (Effect('gain', 'energy', 20), ), description =  ""),
                            Item(name = '葡萄酒', target = 'girl', type = IT_Misc, pic = 'Wine.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 75, effects = (Effect('gain', 'mood', 10), ), description =  ""),
                            Item(name = '苹果', target = 'girl', type = IT_Food, pic = 'Apple.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 50, effects = (Effect('change', 'beauty', 5, duration=10), Effect('gain', 'heal', 1, 0.5)), description =  "一天一苹果，医生远离我。"),
                            Item(name = '梨子', target = 'girl', type = IT_Food, pic = 'Pear.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 50, effects = (Effect('change', 'body', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '桃子', target = 'girl', type = IT_Food, pic = 'Peach.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 50, effects = (Effect('change', 'charm', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '葡萄', target = 'girl', type = IT_Food, pic = 'Grapes.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 50, effects = (Effect('change', 'refinement', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '香肠', target = 'girl', type = IT_Food, pic = 'Sausage.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 75, effects = (Effect('change', 'libido', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '奶酪', target = 'girl', type = IT_Food, pic = 'Cheese.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 75, effects = (Effect('change', 'sensitivity', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '烤鸡', target = 'girl', type = IT_Food, pic = 'Chicken.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 90, effects = (Effect('change', 'obedience', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '烤肉', target = 'girl', type = IT_Food, pic = 'Roastbeef.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 75, effects = (Effect('change', 'constitution', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '爱情魔药', target = 'girl', type = IT_Misc, pic = 'Love potion.webp', template = True, rank = 1, max_rank = 6, rarity = 2, charges = 1, price = 100, effects = (Effect('gain', 'love', 2.5), ), description = "谁说金钱买不来爱情？"),
                            Item(name = '怪物汁液', target = 'girl', type = IT_Misc, pic = 'Monster juice.webp', template = True, rank = 1, max_rank = 6, rarity = 2, charges = 1, price = 60, effects = (Effect('gain', 'fear', 2.5), ), description = "你不会想知道这是从哪个怪物的身体部位来的。"),
                            Item(name = '粉色内裤', target = 'girl', type = IT_Accessory, pic = 'Pink panties.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 125, effects = (Effect('change', 'beauty', 5), ), ),
                            Item(name = '超短热裤', target = 'girl', type = IT_Accessory, pic = 'Hot pants.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 125, effects = (Effect('change', 'body', 5), ), ),
                            Item(name = '低腰内裤', target = 'girl', type = IT_Accessory, pic = 'Lowcut panties.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 125, effects = (Effect('change', 'charm', 5), ), ),
                            Item(name = '蕾丝内裤', target = 'girl', type = IT_Accessory, pic = 'Lace panties.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 125, effects = (Effect('change', 'refinement', 5), ), ),
                            Item(name = '情趣内裤', target = 'girl', type = IT_Accessory, pic = 'Sexy panties.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'libido', 5), ), ),
                            Item(name = '透明内裤', target = 'girl', type = IT_Accessory, pic = 'Seethrough panties.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'sensitivity', 5), ), ),
                            Item(name = '贞操带', target = 'girl', type = IT_Accessory, pic = 'Chastity belt.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 350, effects = (Effect('change', 'obedience', 5), ), ),
                            Item(name = '丁字裤', target = 'girl', type = IT_Accessory, pic = 'Thong.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 175, effects = (Effect('change', 'constitution', 5), ), ),
                            Item(name = '兔女郎', target = 'girl', type = IT_Dress, pic = 'Bunny suit.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'body', 5), Effect('change', 'libido', 5), ), ),
                            Item(name = '女警制服', target = 'girl', type = IT_Dress, pic = 'Guard uniform.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'charm', 5), Effect('change', 'constitution', 5), ), ),
                            Item(name = '水手服', target = 'girl', type = IT_Dress, pic = 'School uniform.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'beauty', 5), Effect('change', 'libido', 5), ), ),
                            Item(name = '比基尼', target = 'girl', type = IT_Dress, pic = 'Bikini.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'body', 5), Effect('change', 'constitution', 5), ), ),
                            Item(name = '和服', target = 'girl', type = IT_Dress, pic = 'Kimono.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 350, effects = (Effect('change', 'refinement', 5), Effect('change', 'obedience', 5), ), ),
                            Item(name = '泳衣', target = 'girl', type = IT_Dress, pic = 'Swimsuit.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'beauty', 5), Effect('change', 'sensitivity', 5), ), ),
                            Item(name = '褶边礼裙', target = 'girl', type = IT_Dress, pic = 'Frilly dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'charm', 5), Effect('change', 'sensitivity', 5), ), ),
                            Item(name = '紧身皮衣', target = 'girl', type = IT_Dress, pic = 'Leather dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'constitution', 5), Effect('change', 'obedience', 5), ), ),
                            Item(name = '晚会礼服', target = 'girl', type = IT_Dress, pic = 'Evening gown.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 400, effects = (Effect('change', 'beauty', 5), Effect('change', 'charm', 5), Effect('change', 'refinement', 5), Effect('change', 'body', -5), ), ),
                            Item(name = '丝绸礼裙', target = 'girl', type = IT_Dress, pic = 'Silk dress.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 400, effects = (Effect('change', 'libido', 5), Effect('change', 'sensitivity', 5), Effect('change', 'obedience', 5), Effect('change', 'constitution', -5), ), ),
                            Item(name = '拉拉队服', target = 'girl', type = IT_Dress, pic = 'Pompom uniform.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 400, effects = (Effect('change', 'beauty', 5), Effect('change', 'charm', 5), Effect('change', 'body', 5), Effect('change', 'refinement', -5), ), ),
                            Item(name = '女骑士装束', target = 'girl', type = IT_Dress, pic = 'Knight uniform.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 400, effects = (Effect('change', 'body', 5), Effect('change', 'constitution', 5), Effect('change', 'obedience', 5), Effect('change', 'libido', -5), ), ),
                            Item(name = '黑色奴隶泳装', target = 'girl', type = IT_Dress, pic = 'Black slavekini.webp', template = True, rank = 1, max_rank = 6, rarity = "S", price = 750, effects = (Effect('change', 'beauty', 5), Effect('change', 'body', 5), Effect('change', 'charm', 5), Effect('change', 'refinement', 5), ), ),
                            Item(name = '蓝色奴隶泳装', target = 'girl', type = IT_Dress, pic = 'Blue slavekini.webp', template = True, rank = 1, max_rank = 6, rarity = "S", price = 1000, effects = (Effect('change', 'libido', 5), Effect('change', 'sensitivity', 5), Effect('change', 'obedience', 5), Effect('change', 'constitution', 5), ), ),
                            Item(name = '红色奴隶泳装', target = 'girl', type = IT_Dress, pic = 'Red slavekini.webp', template = True, rank = 1, max_rank = 6, rarity = "S", price = 2000, effects = (Effect('change', 'service', 5), Effect('change', 'sex', 5), Effect('change', 'anal', 5), Effect('change', 'fetish', 5), ), ),
                            Item(name = '透亮的衣服', target = 'girl', type = IT_Dress, pic = 'Sunny dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 300, effects = (Effect('change', 'beauty', 10), ), ),
                            Item(name = '暴露的衣服', target = 'girl', type = IT_Dress, pic = 'Revealing dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 300, effects = (Effect('change', 'body', 10), ), ),
                            Item(name = '花俏的衣服', target = 'girl', type = IT_Dress, pic = 'Exotic dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 300, effects = (Effect('change', 'charm', 10), ), ),
                            Item(name = '教会长袍', target = 'girl', type = IT_Dress, pic = 'Priestess robe.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 300, effects = (Effect('change', 'refinement', 10), ), ),
                            Item(name = '放荡的衣服', target = 'girl', type = IT_Dress, pic = 'Slutty dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 425, effects = (Effect('change', 'libido', 10), ), ),
                            Item(name = '透明的衣服', target = 'girl', type = IT_Dress, pic = 'Seethrough dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 425, effects = (Effect('change', 'sensitivity', 10), ), ),
                            Item(name = '女仆装', target = 'girl', type = IT_Dress, pic = 'Maid uniform.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 500, effects = (Effect('change', 'obedience', 10), ), ),
                            Item(name = '体操服', target = 'girl', type = IT_Dress, pic = 'Gym uniform.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 425, effects = (Effect('change', 'constitution', 10), ), ),
                            Item(name = '祖母绿戒指', target = 'girl', type = IT_Ring, pic = 'Emerald ring.webp', template = True, rank = 1, max_rank = 5, rarity = 3, price = 500, effects = (Effect('change', 'service', 5), ), ),
                            Item(name = '红宝石戒指', target = 'girl', type = IT_Ring, pic = 'Ruby ring.webp', template = True, rank = 1, max_rank = 5, rarity = 3, price = 500, effects = (Effect('change', 'sex', 5), ), ),
                            Item(name = '黄琥珀戒指', target = 'girl', type = IT_Ring, pic = 'Amber ring.webp', template = True, rank = 1, max_rank = 5, rarity = 3, price = 500, effects = (Effect('change', 'anal', 5), ), ),
                            Item(name = '蓝宝石戒指', target = 'girl', type = IT_Ring, pic = 'sapphire ring.webp', template = True, rank = 1, max_rank = 5, rarity = 3, price = 500, effects = (Effect('change', 'fetish', 5), ), ),
                            Item(name = '调酒秘方卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of bartending.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'waitress jp', 10), ), adjectives = "scroll"),
                            Item(name = '舞蹈窍门卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of whirling.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'dancer jp', 10), ), adjectives = "scroll"),
                            Item(name = '按摩技法卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of rubbing.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'masseuse jp', 10), ), adjectives = "scroll"),
                            Item(name = '礼仪之道卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of etiquette.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'geisha jp', 10), ), adjectives = "scroll"),
                            Item(name = '推油妙诀卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of Onan.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'service jp', 10), ), adjectives = "scroll"),
                            Item(name = '厄洛斯之卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of Eros.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'sex jp', 10), ), adjectives = "scroll"),
                            Item(name = '索多玛之卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of Sodom.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'anal jp', 10), ), adjectives = "scroll"),
                            Item(name = '蛾摩拉之卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of Gomorrah.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'fetish jp', 10), ), adjectives = "scroll"),
                            Item(name = '精灵制造的阴茎放大器', target = 'minion', type = IT_Misc, pic = 'enlarger.webp', template = True, rank = 1, max_rank = 5, rarity = "M", charges = 1, price = 120, effects = (Effect('gain', 'stallion xp', 10), ), description = "那不是我的。这种东西不是我的，宝贝！"),
                            Item(name = '机器润滑油', target = 'minion', type = IT_Misc, pic = 'lubricant.webp', template = True, rank = 1, max_rank = 5, rarity = "M", charges = 1, price = 120, effects = (Effect('gain', 'machine xp', 10), ), description = "润滑油是个好东西。"),
                            Item(name = '奇怪的饲料', target = 'minion', type = IT_Misc, pic = 'feed.webp', template = True, rank = 1, max_rank = 5, rarity = "M", charges = 1, price = 120, effects = (Effect('gain', 'beast xp', 10), ), description = "喜欢他们抓住你的腿，上下摩擦自己吗？因为这个饲料肯定会让他们想这么做。"),
                            Item(name = '怪物饼干', target = 'minion', type = IT_Misc, pic = 'cookie.webp', template = True, rank = 1, max_rank = 5, rarity = "M", charges = 1, price = 120, effects = (Effect('gain', 'monster xp', 10), ), description = "C is for cock-y.", adjectives = "food"),
                            ]

        all_items += generate_template_items(template_items)

        item_dict = {it.name : it for it in all_items}

    return


## FURNITURE ##

label init_furniture():

    python:
        all_furniture = [
            Furniture('纸箱', type='Decoration', pic='Cardboard box.webp', rank=0, chapter=0, cost=[], duration=0, effects=[Effect("allow", "beggars", 1, scope="brothel")], ),
            Furniture('啤酒桶', type='Decoration', pic='Beer keg.webp', rank=0, chapter=0, cost=[], duration=0, effects=[Effect("allow", "thugs", 1, scope="brothel")], ),
            Furniture('基础画作', type='Decoration', pic='Decorative painting.webp', rank=2, chapter=2, cost=[('wood', 1), ('dye', 1), ('leather', 1), ], duration=0, effects=[Effect("allow", "laborers", 1, scope="brothel")], ),
            Furniture('帆船模型', type='Decoration', pic='Model boat.webp', rank=2, chapter=2, cost=[('wood', 2), ('dye', 2), ('leather', 2), ], duration=1, effects=[Effect("allow", "sailors", 1, scope="brothel")], ),
            Furniture('温暖壁炉', type='Decoration', pic='Hearth.webp', rank=2, chapter=2, cost=[('wood', 4), ('leather', 4), ], duration=2, effects=[Effect("allow", "commoners", 1, scope="brothel")], ),
            Furniture('专业级画作', type='Decoration', pic='Fantasy painting.webp', rank=2, chapter=3, cost=[('wood', 4), ('dye', 12), ('leather', 4), ], duration=3, effects=[Effect("allow", "craftsmen", 1, scope="brothel")], ),
            Furniture('红酒酒柜', type='Decoration', pic='Wine cases.webp', rank=3, chapter=4, cost=[('wood', 6), ('dye', 6), ('silk', 4), ], duration=4, effects=[Effect("allow", "bourgeois", 1, scope="brothel")], ),
            Furniture('飞艇模型', type='Decoration', pic='Model airship.webp', rank=3, chapter=4, cost=[('dye', 14), ('silk', 4), ('ore', 4), ], duration=5, effects=[Effect("allow", "guild members", 1, scope="brothel")], ),
            Furniture('大师级画作', type='Decoration', pic='Erotic painting.webp', rank=3, chapter=5, cost=[('wood', 6), ('dye', 6), ('silk', 8), ('ore', 4), ], duration=6, effects=[Effect("allow", "patricians", 1, scope="brothel")], ),
            Furniture('音乐喷泉', type='Decoration', pic='Sparkling fountain.webp', rank=4, chapter=6, cost=[('leather', 6), ('marble', 12), ('ore', 4), ], duration=7, effects=[Effect("allow", "aristocrats", 1, scope="brothel")], ),
            Furniture('贵族纹章', type='Decoration', pic='Armorial bearings.webp', rank=4, chapter=6, cost=[('dye', 6), ('marble', 6), ('silk', 12), ('diamond', 1), ], duration=8, effects=[Effect("allow", "nobles", 1, scope="brothel")], ),
            Furniture('祷告室', type='Decoration', pic='Chapel.webp', rank=5, chapter=7, cost=[('marble', 8), ('silk', 8), ('ore', 4), ('diamond', 2), ], duration=9, effects=[Effect("allow", "royals", 1, scope="brothel")], ),
            Furniture('木质吧台', type='Furnishing', pic='bar counter1.webp', rank=2, chapter=2, cost=[('wood', 4), ('leather', 4), ], duration=1, effects=[Effect("allow", "waitress preference", 1, scope="brothel")], ),
            Furniture('抛光吧台', type='Furnishing', pic='bar counter2.webp', rank=3, chapter=4, cost=[('wood', 4), ('dye', 4), ('leather', 4), ('marble', 4), ('ore', 2), ], duration=3, upgrade='木质吧台', effects=[Effect("allow", "waitress preference", 2, scope="brothel")], ),
            Furniture('金漆吧台', type='Furnishing', pic='bar counter3.webp', rank=4, chapter=6, cost=[('wood', 6), ('marble', 6), ('ore', 12), ], duration=5, upgrade='抛光吧台', effects=[Effect("allow", "waitress preference", 3, scope="brothel")], ),
            Furniture('红木吧台', type='Furnishing', pic='bar counter4.webp', rank=5, chapter=7, cost=[('marble', 5), ('ore', 10), ], duration=7, upgrade='金漆吧台', effects=[Effect("allow", "waitress preference", 5, scope="brothel")], ),
            Furniture('狭窄的卫生间', type='Furnishing', pic='washroom1.webp', rank=2, chapter=2, cost=[('dye', 8), ], duration=1, effects=[Effect("allow", "masseuse preference", 1, scope="brothel")], ),
            Furniture('干净的卫生间', type='Furnishing', pic='washroom2.webp', rank=3, chapter=4, cost=[('wood', 4), ('dye', 4), ('leather', 4), ('marble', 6), ], duration=3, upgrade='狭窄的卫生间', effects=[Effect("allow", "masseuse preference", 2, scope="brothel")], ),
            Furniture('高级的卫生间', type='Furnishing', pic='washroom3.webp', rank=4, chapter=6, cost=[('wood', 6), ('marble', 12), ('silk', 6), ], duration=5, upgrade='干净的卫生间', effects=[Effect("allow", "masseuse preference", 3, scope="brothel")], ),
            Furniture('豪华的卫生间', type='Furnishing', pic='washroom4.webp', rank=5, chapter=7, cost=[('marble', 10), ('silk', 5), ], duration=7, upgrade='高级的卫生间', effects=[Effect("allow", "masseuse preference", 5, scope="brothel")], ),
            Furniture('临时舞台', type='Furnishing', pic='stage1.webp', rank=2, chapter=2, cost=[('wood', 4), ('dye', 4), ], duration=1, effects=[Effect("allow", "dancer preference", 1, scope="brothel")], ),
            Furniture('业余舞台', type='Furnishing', pic='stage2.webp', rank=3, chapter=4, cost=[('leather', 12), ('marble', 4), ('ore', 2), ], duration=3, upgrade='临时舞台', effects=[Effect("allow", "dancer preference", 2, scope="brothel")], ),
            Furniture('大型舞台', type='Furnishing', pic='stage3.webp', rank=4, chapter=6, cost=[('leather', 6), ('marble', 6), ('silk', 12), ], duration=5, upgrade='业余舞台', effects=[Effect("allow", "dancer preference", 3, scope="brothel")], ),
            Furniture('剧院舞台', type='Furnishing', pic='stage4.webp', rank=5, chapter=7, cost=[('marble', 5), ('silk', 10), ], duration=7, upgrade='大型舞台', effects=[Effect("allow", "dancer preference", 5, scope="brothel")], ),
            Furniture('小型包厢', type='Furnishing', pic='tatami room1.webp', rank=2, chapter=2, cost=[('dye', 4), ('leather', 4), ], duration=1, effects=[Effect("allow", "geisha preference", 1, scope="brothel")], ),
            Furniture('精装包厢', type='Furnishing', pic='tatami room2.webp', rank=3, chapter=4, cost=[('dye', 12), ('silk', 6), ], duration=3, upgrade='小型包厢', effects=[Effect("allow", "geisha preference", 2, scope="brothel")], ),
            Furniture('华美包厢', type='Furnishing', pic='tatami room3.webp', rank=4, chapter=6, cost=[('dye', 6), ('silk', 12), ('ore', 6), ], duration=5, upgrade='精装包厢', effects=[Effect("allow", "geisha preference", 3, scope="brothel")], ),
            Furniture('主题定制包厢', type='Furnishing', pic='tatami room4.webp', rank=5, chapter=7, cost=[('silk', 10), ('ore', 5), ], duration=7, upgrade='华美包厢', effects=[Effect("allow", "geisha preference", 5, scope="brothel")], ),
            Furniture('自助糖果机', type='Furnishing', pic='dispenser1.webp', rank=2, chapter=3, cost=[('wood', 6), ('dye', 4), ('leather', 6), ], duration=2, effects=[Effect("allow", "service preference", 1, scope="brothel")], ),
            Furniture('自助冰淇淋机', type='Furnishing', pic='dispenser2.webp', rank=3, chapter=5, cost=[('wood', 10), ('leather', 5), ('marble', 8), ('ore', 10), ], duration=4, upgrade='自助糖果机', effects=[Effect("allow", "service preference", 2, scope="brothel")], ),
            Furniture('自助爆米花机', type='Furnishing', pic='dispenser3.webp', rank=4, chapter=6, cost=[('leather', 6), ('marble', 8), ('ore', 12), ], duration=6, upgrade='自助冰淇淋机', effects=[Effect("allow", "service preference", 3, scope="brothel")], ),
            Furniture('魔力薄荷糖售货机', type='Furnishing', pic='dispenser4.webp', rank=5, chapter=7, cost=[('marble', 8), ('ore', 10), ], duration=8, upgrade='自助爆米花机', effects=[Effect("allow", "service preference", 5, scope="brothel")], ),
            Furniture('工口漫画书柜', type='Furnishing', pic='shelves1.webp', rank=2, chapter=3, cost=[('wood', 6), ('dye', 6), ('leather', 4), ], duration=2, effects=[Effect("allow", "sex preference", 1, scope="brothel")], ),
            Furniture('耻物手办模型', type='Furnishing', pic='shelves2.webp', rank=3, chapter=5, cost=[('wood', 5), ('leather', 10), ('marble', 10), ('ore', 8), ], duration=4, upgrade='工口漫画书柜', effects=[Effect("allow", "sex preference", 2, scope="brothel")], ),
            Furniture('限定的角色模型', type='Furnishing', pic='shelves3.webp', rank=4, chapter=6, cost=[('wood', 6), ('marble', 12), ('ore', 8), ], duration=6, upgrade='耻物手办模型', effects=[Effect("allow", "sex preference", 3, scope="brothel")], ),
            Furniture('绝版的工口藏品', type='Furnishing', pic='shelves4.webp', rank=5, chapter=7, cost=[('marble', 10), ('ore', 8), ], duration=8, upgrade='限定的角色模型', effects=[Effect("allow", "sex preference", 5, scope="brothel")], ),
            Furniture('维纳斯的画像', type='Furnishing', pic='venus1.webp', rank=2, chapter=3, cost=[('dye', 16), ], duration=2, effects=[Effect("allow", "anal preference", 1, scope="brothel")], ),
            Furniture('维纳斯的雕像', type='Furnishing', pic='venus2.webp', rank=3, chapter=5, cost=[('dye', 15), ('marble', 10), ('silk', 8), ], duration=4, upgrade='维纳斯的画像', effects=[Effect("allow", "anal preference", 2, scope="brothel")], ),
            Furniture('半脱的维纳斯', type='Furnishing', pic='venus3.webp', rank=4, chapter=6, cost=[('dye', 6), ('marble', 8), ('silk', 12), ], duration=6, upgrade='维纳斯的雕像', effects=[Effect("allow", "anal preference", 3, scope="brothel")], ),
            Furniture('发情的维纳斯', type='Furnishing', pic='venus4.webp', rank=5, chapter=7, cost=[('marble', 10), ('silk', 8), ], duration=8, upgrade='半脱的维纳斯', effects=[Effect("allow", "anal preference", 5, scope="brothel")], ),
            Furniture('木质三角马', type='Furnishing', pic='woodhorse1.webp', rank=2, chapter=3, cost=[('wood', 6), ('dye', 2), ('leather', 8), ], duration=2, effects=[Effect("allow", "fetish preference", 1, scope="brothel")], ),
            Furniture('电动三角马', type='Furnishing', pic='woodhorse2.webp', rank=3, chapter=5, cost=[('wood', 15), ('silk', 10), ('ore', 8), ], duration=4, upgrade='木质三角马', effects=[Effect("allow", "fetish preference", 2, scope="brothel")], ),
            Furniture('大功率三角马', type='Furnishing', pic='woodhorse3.webp', rank=4, chapter=6, cost=[('wood', 6), ('silk', 12), ('ore', 8), ], duration=6, upgrade='电动三角马', effects=[Effect("allow", "fetish preference", 3, scope="brothel")], ),
            Furniture('魔力三角马', type='Furnishing', pic='woodhorse4.webp', rank=5, chapter=7, cost=[('silk', 8), ('ore', 10), ], duration=8, upgrade='大功率三角马', effects=[Effect("allow", "fetish preference", 5, scope="brothel")], ),
            Furniture('站街小妹', type='Utility', pic='Basic outfit.webp', rank=0, chapter=0, cost=[], duration=0, effects=[Effect("special", "advertising power", 1, scope="brothel")], ),
            Furniture('巨乳牧女', type='Utility', pic='Shepherd outfit.webp', rank=2, chapter=2, cost=[('wood', 2), ('leather', 6), ], duration=0, upgrade='站街小妹', effects=[Effect("special", "advertising power", 2, scope="brothel")], ),
            Furniture('色情修女', type='Utility', pic='Priestess outfit.webp', rank=2, chapter=3, cost=[('dye', 8), ('leather', 12), ], duration=1, upgrade='巨乳牧女', effects=[Effect("special", "advertising power", 3, scope="brothel")], ),
            Furniture('透明泳衣', type='Utility', pic='Skimpy outfit.webp', rank=3, chapter=4, cost=[('dye', 8), ('leather', 4), ('silk', 4), ], duration=2, upgrade='色情修女', effects=[Effect("special", "advertising power", 4, scope="brothel")], ),
            Furniture('真空上阵', type='Utility', pic='Slutty outfit.webp', rank=3, chapter=5, cost=[('dye', 10), ('leather', 2), ('silk', 10), ('ore', 4), ], duration=2, upgrade='透明泳衣', effects=[Effect("special", "advertising power", 5, scope="brothel")], ),
            Furniture('堕落巫女', type='Utility', pic='Kimono outfit.webp', rank=4, chapter=6, cost=[('dye', 6), ('silk', 18), ], duration=3, upgrade='真空上阵', effects=[Effect("special", "advertising power", 6, scope="brothel")], ),
            Furniture('下海偶像', type='Utility', pic='Idol outfit.webp', rank=5, chapter=7, cost=[('silk', 12), ('ore', 4), ], duration=3, upgrade='堕落巫女', effects=[Effect("special", "advertising power", 7, scope="brothel")], ),
            Furniture('防盗门', type='Utility', pic='Basic door.webp', rank=0, chapter=0, cost=[], duration=0, effects=[Effect("boost", "security", 0, scope="brothel")], ),
            Furniture('围墙', type='Utility', pic='Fence.webp', rank=2, chapter=2, cost=[('wood', 4), ('leather', 4), ], duration=0, upgrade='防盗门', effects=[Effect("boost", "security", 0.1, scope="brothel")], ),
            Furniture('小型陷阱', type='Utility', pic='Small traps.webp', rank=2, chapter=3, cost=[('leather', 20), ], duration=1, upgrade='围墙', effects=[Effect("boost", "security", 0.2, scope="brothel")], ),
            Furniture('大型陷阱', type='Utility', pic='Large traps.webp', rank=3, chapter=4, cost=[('wood', 8), ('leather', 4), ('ore', 4), ], duration=2, upgrade='小型陷阱', effects=[Effect("boost", "security", 0.3, scope="brothel")], ),
            Furniture('安全警报', type='Utility', pic='Alarm system.webp', rank=3, chapter=5, cost=[('leather', 12), ('marble', 4), ('ore', 10), ], duration=2, upgrade='大型陷阱', effects=[Effect("boost", "security", 0.4, scope="brothel")], ),
            Furniture('爆炸陷阱', type='Utility', pic='Explosive traps.webp', rank=4, chapter=6, cost=[('leather', 6), ('ore', 18), ], duration=3, upgrade='安全警报', effects=[Effect("boost", "security", 0.5, scope="brothel")], ),
            Furniture('电击陷阱', type='Utility', pic='Zap traps.webp', rank=5, chapter=7, cost=[('marble', 4), ('ore', 12), ], duration=3, upgrade='爆炸陷阱', effects=[Effect("boost", "security", 0.6, scope="brothel")], ),
            Furniture('扫帚', type='Utility', pic='Broom.webp', rank=0, chapter=0, cost=[], duration=0, effects=[Effect("boost", "maintenance", 0, scope="brothel")], ),
            Furniture('水桶', type='Utility', pic='Buckets.webp', rank=2, chapter=2, cost=[('wood', 6), ('leather', 2), ], duration=0, upgrade='扫帚', effects=[Effect("boost", "maintenance", 0.25, scope="brothel")], ),
            Furniture('浴巾', type='Utility', pic='Towels.webp', rank=3, chapter=3, cost=[('dye', 5), ('leather', 5), ], duration=1, upgrade='水桶', effects=[Effect("boost", "maintenance", 0.35, scope="brothel")], ),
            Furniture('手推车', type='Utility', pic='Wheelbarrow.webp', rank=3, chapter=4, cost=[('wood', 4), ('dye', 4), ('leather', 4), ('ore', 4), ], duration=1, upgrade='水桶', effects=[Effect("boost", "maintenance", 0.5, scope="brothel")], ),
            Furniture('魔力扫帚', type='Utility', pic='magic broom.webp', rank=3, chapter=5, cost=[('wood', 10), ('leather', 6), ('silk', 6), ], duration=2, upgrade='手推车', effects=[Effect("boost", "maintenance", 1, scope="brothel")], ),
            Furniture('蒸汽货车', type='Utility', pic='Steam cart.webp', rank=4, chapter=6, cost=[('leather', 6), ('marble', 6), ('silk', 6), ('ore', 6), ], duration=2, upgrade='手推车', effects=[Effect("boost", "maintenance", 1.5, scope="brothel")], ),
            Furniture('机械女仆', type='Utility', pic='Robot maid.webp', rank=5, chapter=7, cost=[('silk', 6), ('ore', 10), ], duration=3, upgrade='蒸汽货车', effects=[Effect("boost", "maintenance", 3, scope="brothel")], ),
            Furniture('大理石雕像', type='Decoration', pic='Bronze statue.webp', rank=2, chapter=2, cost=[('wood', 4), ('dye', 4), ], duration=1, effects=[Effect("change", "brothel reputation", 6, scope="brothel")], ),
            Furniture('白银雕像', type='Decoration', pic='Silver statue.webp', rank=3, chapter=4, cost=[('dye', 15), ('marble', 6), ], duration=2, upgrade='大理石雕像', effects=[Effect("change", "brothel reputation", 12, scope="brothel")], ),
            Furniture('镀金雕像', type='Decoration', pic='Gold statue.webp', rank=4, chapter=6, cost=[('dye', 6), ('ore', 20), ], duration=3, upgrade='白银雕像', effects=[Effect("change", "brothel reputation", 18, scope="brothel")], ),
            Furniture('铂金雕像', type='Decoration', pic='Platinum statue.webp', rank=5, chapter=7, cost=[('ore', 20), ('diamond', 1), ], duration=4, upgrade='镀金雕像', effects=[Effect("change", "brothel reputation", 24, scope="brothel")], ),
            Furniture('储物柜', type='Utility', pic='safe1.webp', rank=2, chapter=2, cost=[('wood', 4), ('dye', 2), ('leather', 4), ], duration=3, effects=[Effect("special", "safe", 3000, scope="brothel")]),
            Furniture('带锁的箱子', type='Utility', pic='safe2.webp', rank=3, chapter=4, cost=[('wood', 5), ('leather', 10), ('ore', 6), ], duration=5, upgrade='储物柜', effects=[Effect("special", "safe", 6000, scope="brothel")]),
            Furniture('保险箱', type='Utility', pic='safe3.webp', rank=4, chapter=6, cost=[('wood', 6), ('marble', 8), ('ore', 12), ('diamond', 1), ], duration=7, upgrade='带锁的箱子', effects=[Effect("special", "safe", 10000, scope="brothel")]),
            Furniture('银行金库', type='Utility', pic='safe4.webp', rank=5, chapter=7, cost=[('marble', 10), ('ore', 10), ('diamond', 2), ], duration=9, upgrade='保险箱', effects=[Effect("special", "safe", 20000, scope="brothel")]),
            Furniture('玻璃窗', type='Windows', pic='glass1.webp', rank=2, chapter=3, cost=[('wood', 5), ('dye', 5), ('leather', 5), ], duration=3, effects=[Effect("boost", "naked preference increase", 0.25, scope="brothel")], ),
            Furniture('百叶窗', type='Windows', pic='oriental1.webp', rank=2, chapter=3, cost=[('wood', 6), ('dye', 6), ('leather', 6), ], duration=3, effects=[Effect("boost", "service preference increase", 0.25, scope="brothel")], ),
            Furniture('化妆镜', type='Windows', pic='mirror1.webp', rank=2, chapter=3, cost=[('wood', 7), ('dye', 7), ('leather', 7), ], duration=4, effects=[Effect("boost", "sex preference increase", 0.25, scope="brothel")], ),
            Furniture('红色窗帘', type='Windows', pic='red curtains1.webp', rank=2, chapter=3, cost=[('wood', 6), ('dye', 10), ('leather', 6), ], duration=4, effects=[Effect("boost", "anal preference increase", 0.25, scope="brothel")], ),
            Furniture('防盗窗', type='Windows', pic='barred1.webp', rank=2, chapter=3, cost=[('wood', 10), ('dye', 7), ('leather', 7), ], duration=4, effects=[Effect("boost", "fetish preference increase", 0.25, scope="brothel")], ),
            Furniture('双开玻璃窗', type='Windows', pic='double window1.webp', rank=2, chapter=3, cost=[('wood', 12), ('dye', 6), ('leather', 6), ], duration=5, effects=[Effect("boost", "bisexual preference increase", 0.25, scope="brothel")], ),
            Furniture('彩绘玻璃', type='Windows', pic='stainglass1.webp', rank=2, chapter=3, cost=[('wood', 10), ('dye', 8), ('leather', 8), ], duration=5, effects=[Effect("boost", "group preference increase", 0.25, scope="brothel")], ),
            Furniture('落地窗', type='Windows', pic='glass2.webp', rank=3, chapter=5, cost=[('wood', 5), ('dye', 10), ('marble', 6), ('silk', 6), ], duration=5, upgrade='玻璃窗', effects=[Effect("boost", "naked preference increase", 0.5, scope="brothel")], ),
            Furniture('彩色落地窗', type='Windows', pic='oriental2.webp', rank=3, chapter=5, cost=[('wood', 10), ('leather', 5), ('marble', 5), ('silk', 10), ], duration=5, upgrade='百叶窗', effects=[Effect("boost", "service preference increase", 0.5, scope="brothel")], ),
            Furniture('全身镜', type='Windows', pic='mirror2.webp', rank=3, chapter=5, cost=[('dye', 5), ('leather', 10), ('silk', 5), ('ore', 12), ], duration=6, upgrade='化妆镜', effects=[Effect("boost", "sex preference increase", 0.5, scope="brothel")], ),
            Furniture('王室窗帘', type='Windows', pic='red curtains2.webp', rank=3, chapter=5, cost=[('dye', 10), ('silk', 18), ], duration=6, upgrade='红色窗帘', effects=[Effect("boost", "anal preference increase", 0.5, scope="brothel")], ),
            Furniture('大号防盗窗', type='Windows', pic='barred2.webp', rank=3, chapter=5, cost=[('wood', 10), ('leather', 5), ('marble', 10), ('ore', 10), ], duration=6, upgrade='防盗窗', effects=[Effect("boost", "fetish preference increase", 0.5, scope="brothel")], ),
            Furniture('钢化玻璃窗', type='Windows', pic='double window2.webp', rank=3, chapter=5, cost=[('leather', 15), ('marble', 10), ('silk', 6), ('ore', 6), ], duration=7, upgrade='双开玻璃窗', effects=[Effect("boost", "bisexual preference increase", 0.5, scope="brothel")], ),
            Furniture('彩色玻璃', type='Windows', pic='stainglass2.webp', rank=3, chapter=5, cost=[('dye', 15), ('marble', 5), ('silk', 5), ('ore', 14), ], duration=7, upgrade='彩绘玻璃', effects=[Effect("boost", "group preference increase", 0.5, scope="brothel")], ),
            Furniture('木澡盆', type='Comfort', pic='Washtub.webp', rank=2, chapter=2, cost=[('wood', 4), ('dye', 4), ], duration=1, effects=[Effect("boost", "energy use", -0.1, scope="brothel")], ),
            Furniture('大浴缸', type='Comfort', pic='Bathtub.webp', rank=3, chapter=4, cost=[('dye', 15), ('marble', 6), ], duration=3, upgrade='木澡盆', effects=[Effect("boost", "energy use", -0.2, scope="brothel")], ),
            Furniture('贵族浴池', type='Comfort', pic='Royal bathtub.webp', rank=4, chapter=6, cost=[('dye', 8), ('marble', 15), ('silk', 15), ('diamond', 1), ], duration=5, upgrade='大浴缸', effects=[Effect("boost", "energy use", -0.3, scope="brothel")], ),
            Furniture('汗蒸浴池', type='Comfort', pic='Steam jacuzzi.webp', rank=5, chapter=7, cost=[('marble', 20), ('silk', 20), ('ore', 20), ('diamond', 3), ], duration=7, upgrade='贵族浴池', effects=[Effect("boost", "energy use", -0.4, scope="brothel")], ),
            Furniture('塑料板凳', type='Comfort', pic='bench1.webp', rank=2, chapter=3, cost=[('wood', 25), ], duration=2, effects=[Effect("change", "job customer capacity", 1, scope="brothel")], ),
            Furniture('舒适长椅', type='Comfort', pic='bench2.webp', rank=3, chapter=5, cost=[('wood', 10), ('leather', 6), ('marble', 15), ('ore', 10), ], duration=4, upgrade='塑料板凳', effects=[Effect("change", "job customer capacity", 2, scope="brothel")], ),
            Furniture('真皮沙发', type='Comfort', pic='sofa1.webp', rank=4, chapter=6, cost=[('leather', 10), ('silk', 20), ('diamond', 1), ], duration=6, upgrade='舒适长椅', effects=[Effect("change", "job customer capacity", 3, scope="brothel")], ),
            Furniture('按摩躺椅', type='Comfort', pic='sofa2.webp', rank=5, chapter=7, cost=[('marble', 8), ('silk', 15), ('diamond', 2), ], duration=8, upgrade='真皮沙发', effects=[Effect("change", "job customer capacity", 4, scope="brothel")], ),
            Furniture('席梦思', type='Comfort', pic='bed1.webp', rank=3, chapter=4, cost=[('wood', 12), ('leather', 10), ('silk', 6), ], duration=5, effects=[Effect("change", "whore customer capacity", 1, scope="brothel")], ),
            Furniture('天鹅绒', type='Comfort', pic='bed2.webp', rank=5, chapter=7, cost=[('marble', 10), ('silk', 20), ('diamond', 3), ], duration=10, upgrade='席梦思', effects=[Effect("change", "whore customer capacity", 2, scope="brothel")], ),
            Furniture('简易神像', type='Altars', pic='mana altar1.webp', rank=2, chapter=2, cost=[('wood', 2), ('dye', 2), ('leather', 4), ], duration=2, effects=[Effect("change", "mana", 1, scope="brothel")], ),
            Furniture('祝福神像', type='Altars', pic='mana altar2.webp', rank=3, chapter=4, cost=[('leather', 15), ('marble', 3), ('silk', 2), ('ore', 1), ], duration=4, upgrade='简易神像', effects=[Effect("change", "mana", 2, scope="brothel")], ),
            Furniture('权能神像', type='Altars', pic='mana altar3.webp', rank=4, chapter=6, cost=[('dye', 6), ('marble', 4), ('silk', 8), ('ore', 4), ('diamond', 1), ], duration=6, upgrade='祝福神像', effects=[Effect("change", "mana", 3, scope="brothel")], ),
            Furniture('至高神像', type='Altars', pic='mana altar4.webp', rank=5, chapter=7, cost=[('marble', 6), ('silk', 6), ('ore', 6), ('diamond', 2), ], duration=8, upgrade='权能神像', effects=[Effect("change", "mana", 4, scope="brothel")], ),
            Furniture('武器架', type='Utility', pic='weapon rack1.webp', rank=2, chapter=2, cost=[('dye', 2), ('leather', 4), ], duration=1, effects=[Effect("change", "defense", 1, scope="brothel")], ),
            Furniture('军火库', type='Utility', pic='weapon rack2.webp', rank=4, chapter=6, cost=[('wood', 6), ('marble', 10), ('ore', 12), ], duration=3, upgrade='武器架', effects=[Effect("change", "defense", 2, scope="brothel")], ),
            Furniture('简陋的更衣室', type='Comfort', pic='dressing1.webp', rank=2, chapter=2, cost=[('wood', 4), ('dye', 4), ('leather', 2), ], duration=2, effects=[Effect("boost", "upkeep", -0.05, scope="brothel")], ),
            Furniture('宽敞的更衣室', type='Comfort', pic='dressing2.webp', rank=3, chapter=4, cost=[('wood', 10), ('dye', 5), ('marble', 2), ('silk', 6), ], duration=4, upgrade='简陋的更衣室', effects=[Effect("boost", "upkeep", -0.1, scope="brothel")], ),
            Furniture('华丽的更衣室', type='Comfort', pic='dressing3.webp', rank=4, chapter=6, cost=[('leather', 6), ('marble', 20), ('silk', 5), ], duration=6, upgrade='宽敞的更衣室', effects=[Effect("boost", "upkeep", -0.15, scope="brothel")], ),
            Furniture('昏暗环境灯', type='Comfort', pic='dim.webp', rank=3, chapter=4, cost=[('wood', 5), ('leather', 10), ('silk', 4), ('ore', 2), ], duration=3, effects=[Effect("boost", "customer events", 0.5, scope="brothel"), Effect("boost", "crazy", 1, scope="brothel")], can_deactivate=True),
            Furniture('强光射灯', type='Comfort', pic='bright.webp', rank=3, chapter=4, cost=[('wood', 10), ('leather', 5), ('silk', 2), ('ore', 4), ], duration=3, effects=[Effect("boost", "customer events", -1, scope="brothel"), Effect("boost", "crazy", -0.5, scope="brothel")], can_deactivate=True),
            Furniture('图书角', type='Comfort', pic='bookshelf1.webp', rank=2, chapter=2, cost=[('wood', 4), ('dye', 4), ('leather', 4), ], duration=3, effects=[Effect("set", "all skill max", 60, scope="brothel"), Effect("set", "all skill max", 60, scope="farm")], ),
            Furniture('木质书架', type='Comfort', pic='bookshelf2.webp', rank=3, chapter=4, cost=[('wood', 15), ('leather', 10), ('marble', 5), ('ore', 5), ], duration=6, upgrade='图书角', effects=[Effect("set", "all skill max", 115, scope="brothel"), Effect("set", "all skill max", 115, scope="farm")], ),
            Furniture('藏书书柜', type='Comfort', pic='bookshelf3.webp', rank=4, chapter=6, cost=[('wood', 6), ('marble', 15), ('silk', 5), ('ore', 5), ('diamond', 2), ], duration=9, upgrade='木质书架', effects=[Effect("set", "all skill max", 170, scope="brothel"), Effect("set", "all skill max", 170, scope="farm")], ),
            Furniture('私人图书馆', type='Comfort', pic='bookshelf4.webp', rank=5, chapter=7, cost=[('marble', 15), ('silk', 5), ('ore', 5), ('diamond', 4), ], duration=12, upgrade='藏书书柜', effects=[Effect("set", "all skill max", 225, scope="brothel"), Effect("set", "all skill max", 225, scope="farm")], ),

            ]

        furniture_dict = {}
        for furn in all_furniture:
            furniture_dict[furn.name] = furn

        get_starting_furniture(1)

    return


## INVENTORY SCREENS ##

screen item_tab(context, left_party, right_party): # Where X_party are a list of inventory-holding characters

    zorder 5

    default show_search_left = False
    default show_search_right = False

    if right_focus:
        default display_stats = right_focus
    else:
        default display_stats = left_focus

    ## Add contextual UI elements

    use overlay(context)

    if context == "shop":
        if story_flags["shop restock"]:
            use restock_button(right_focus, upgrade=True)

    elif context == "visit_location": # Merchants
        if story_flags["shop restock"]:
            use restock_button(right_focus)

    key "mouseup_3" action (Return("back"))
    use close(Return("back"))
    use shortcuts()

    fixed:
        if left_focus:
            vbox xsize xres(255) xalign 0.0 ypos 0.1:
                hbox xfill True ysize yres(80) xalign 0.0:
                    use universal_selector(party=left_party, current=left_focus, var="left_focus", avoid=right_focus, sc_prefix="") id "sel1"
                hbox spacing xres(6) xalign 0.0:
                    frame xsize xres(38) ysize yres(20) xpadding 0 ypadding 0 xmargin 0 ymargin 0:
                        textbutton {True: "隐藏", False: "搜索"}[show_search_left] text_xalign 0.5 text_italic True text_color c_darkbrown text_size res_font(14) xpadding 0 ypadding 0 xalign 0.5 yalign 0.6 xsize xres(38) ysize yres(20) idle_background None action (ToggleScreenVariable("show_search_left"), SetField(MC, "active_text_filter", ""), SelectedIf(show_search_left))
                    use sorting_tab(context + " items", sort_target=left_focus.items, sorters=["type", "price", "alpha"]) id "st1"
                hbox xalign 0.0:
                    use item_list(items=left_focus.items, owner=left_focus, counterpart=right_focus, sc_prefix="noshift_", search=show_search_left) id "il1"
                    use item_filter() id "if1"
                    if left_focus.type in ("MC", "girl"):
                        use inventory(left_focus, counterpart=right_focus) id "inv1"

        if right_focus:
            vbox xsize xres(255) xalign 1.0 xanchor 1.0 ypos 0.1:
                hbox ysize yres(80) xalign 1.0:
                    use universal_selector(party=right_party, current=right_focus, var="right_focus", avoid=left_focus, sc_prefix="shift_") id "sel2"
                hbox xalign 1.0:
                    use sorting_tab(context + " items", sort_target=right_focus.items, sorters=["type", "price", "alpha"]) id "st2"
                hbox xalign 1.0:
                    if right_focus.type in ("MC", "girl"):
                        use inventory(right_focus, counterpart=left_focus) id "inv2"
                    use item_filter() id "if2"
                    use item_list(items=right_focus.items, owner=right_focus, counterpart=left_focus, sc_prefix="shift_") id "il2"

screen universal_selector:

    zorder 5

    $ previous = get_previous(party, current, loop=True, avoid=avoid)
    $ next = get_next(party, current, loop=True, avoid=avoid)

    # hbox xfill True ysize yres(80) xalign algn:
    if previous != current:
        textbutton "<" ysize yres(80) xalign 0.0 yalign 0.5:
            action (SetVariable(var, previous), Return((var, "cycle_left")))
            if sc_prefix == "shift_":
                tooltip "Use shift + left/right arrow keys to change the focused character."
            else:
                tooltip "Use left/right arrow keys to change the focused character."

        key sc_prefix + "K_LEFT" action (SetVariable(var, previous), Return((var, "cycle_left")))

    frame xalign 0.0 yfill True ypadding 0 ymargin 0:
        xfill True

        has hbox
        yalign 0.5
        spacing 12

        if current.type == "MC":
            $ por = Picture(path=playerclass_pics[MC.playerclass]).get()
        elif current.type == "girl":
            $ por = current.portrait.get()
        else: # NPC
            $ por = current.portrait

        # frame xsize yres(80) ysize yres(80) xfill True ypadding 0 ymargin 0 xalign 0.5 yalign 0.5:
        if por != None:
            fixed xsize yres(70) ysize yres(70) xalign 0.5 yalign 0.5:
                add por xalign 0.5 yalign 0.5 fit "contain"

                if current.type == "girl":
                    $ badge = current.get_badge()
                    if badge:
                        add ProportionalScale(badge, *res_tb(30)) xalign 0.9 yalign 0.1

        if current.type == "MC":
            $ text1 = "{b}%s{/b}\n" % current.name + MC.playerclass + " level " + str(current.level)
            $ col = c_steel
            $ sz = 20

        elif current.type == "girl":
            $ text1 = "{b}%s{/b}" % current.fullname + __("\nRank ") + rank_name[current.rank] + __(" - Level ") + str(current.level)
            $ col = c_brown
            $ sz = 16

            if current.job:
                $ text1 += "\n" + __(current.job.capitalize())
                if current.job in all_jobs and current.work_whore:
                    $ text1 += __("/Whore")
                $ sched = current.workdays[calendar.get_weekday()]

            else:
                $ text1 += __("\nNo job")
                $ sched = 0

            if current.away:
                $ text1 += __(" (away)")
            elif current.hurt > 0:
                $ text1 += __(" (hurt)")
            elif current.exhausted > 0:
                $ text1 += __(" (tired)")
            elif current.resting or sched == 0:
                $ text1 += __(" (resting)")
            elif sched == 50:
                $ text1 += __(" (half-shift)")
        else:
            $ text1 = "{b}%s{/b}\n" % capitalize(current.name) + merchant_title[current.name]
            $ col = c_darkpurple
            $ sz = 20

        text text1 size res_font(sz) xalign 0.0 yalign 0.1 yanchor 0.0 color col

    if next != current:
        key sc_prefix + "K_RIGHT" action (SetVariable(var, next), Return((var, "cycle_right")))

        textbutton ">" ysize yres(80) xalign 1.0 yalign 0.5:
            action (SetVariable(var, next), Return((var, "cycle_right")))
            if sc_prefix == "shift_":
                tooltip "Use shift + left/right arrow keys to change the focused character."
            else:
                tooltip "Use left/right arrow keys to change the focused character."


screen sorting_tab(context, sort_target=None, sorters=[]): # Sorters are defined in BKinit_variables.rpy

    zorder 5

    hbox xalign 0.5:
        for s in sorters:
            $ _caption, _attr, _ttip, _reverse = sorter_dict[s] # sorter format: [caption, attribute, tooltip, reverse order]
            if game.sorting_dict[context] and game.sorting_dict[context][1] == _attr and game.sorting_dict[context][3] == _reverse: # If the same sorting method is selected twice, reverses sorting order:
                $ _reverse = not _reverse

            frame xsize xres(38) ysize yres(20) xpadding 0 ypadding 0 xmargin 0 ymargin 0:

                textbutton _caption text_italic True text_color c_darkbrown text_size res_font(14) xpadding 0 ypadding 0 xalign 0.5 yalign 0.6 xsize xres(38) ysize yres(20) idle_background None:
                    action (Function(sort_target.sort, key=lambda x, s=_attr: getattr(x, s), reverse=_reverse), SetDict(game.sorting_dict, context, [_caption, _attr, _ttip, _reverse]))
                    tooltip __("点击根据") + __(_ttip) +"排序。"

screen item_list(items, owner, counterpart, sc_prefix, search=False): # May also accept Minions as 'items'

    default page = 1
    default line_nb = 7
    default page_offset = 0
    default page_button_nb = 8
    default old_filter = ""

    $ page_nb = round_up(len(items)/line_nb)
    if page_nb < page and page > 1:
        $ page = page_nb

    if MC.active_text_filter and MC.active_text_filter != old_filter: # There must be a better way to do this :(
        $ page = 1
        $ page_offset = 0

    if MC.active_text_filter:
        $ items = [it for it in items if MC.active_text_filter.lower() in it.name.lower()]
        $ old_filter = MC.active_text_filter
    elif MC.active_inv_filter:
        $ items = [it for it in items if it.filter in MC.active_inv_filter]

    $ page_index = line_nb * (page-1)

    vbox xsize xres(180):
        frame xfill True:
            if search:
                ysize yres(415)
            else:
                ysize yres(400)
            has vbox

            if search:
                hbox:
                    text "搜索: " size res_font(16) color c_brown
                    input size res_font(16) color c_darkorange changed(MC.add_text_filter)

            if items:

                for i in range(line_nb):
                    if page_index+i < len(items):
                        $ it = items[page_index+i]
                        $ acts = it.get_acts(owner, counterpart)

                        button style "girlbutton_blue" xpadding 6:
                            xfill True
                            action (Show("item_profile", it=it, transition = dissolve), SetVariable("selected_item", it), SetVariable("owner", owner), SetVariable("counterpart", counterpart), SelectedIf(selected_item==it))
                            if isinstance(it, Item):
                                hovered tt.Action(it.base_description)
                            tooltip it.description

                            hbox spacing 3:

                                frame yalign 0.5 xysize res_tb(55) ymargin 3:
                                    add it.pic.get(*res_tb(45)) xalign 0.5 yalign 0.5


                                vbox yalign 0.5:
                                    $ text1 = __(it.name)

                                    if isinstance(it, Item):
                                        if it.charges and it.charges > 1:
                                            $ text1 += " (" + str(it.charges) + ")"

                                        if it.equipped:
                                            $ text1 += __("\n{i}Equipped{/i}")

                                    elif isinstance(it, Minion):
                                        $ text1 +=  __("\nLevel ") + str(it.level)

                                    if "sell" in acts:
                                        $ text1 += "\n" + str(it.get_price("sell")) + "金币"

                                    if "buy" in acts:
                                        $ text1 += "\n" + str(it.get_price("buy")) + "金币"

                                    text __(text1) size res_font(14)

            else:
                if MC.active_inv_filter:
                    text "No items available (filters are on)." size res_font(14) color c_brown
                else:
                    text "No items available." size res_font(14) color c_brown

        if items:
            $ start = page_offset

            # No arrows required
            if page_nb <= page_button_nb:
                $ previous = None
                $ next = None
                $ finish = page_nb
            # More than one set of page numbers is needed
            else:
                if page_offset:
                    $ previous = page_button_nb-2
                else:
                    $ previous = None

                if page_nb-page_offset >= page_button_nb-1:
                    $ next = page_button_nb-2
                else:
                    $ next = None

                if next:
                    $ finish = start + next
                else:
                    $ finish = page_nb

            if page_nb > 1:
                if page > 1:
                    if renpy.version_tuple.major > 8 or (renpy.version_tuple.major == 8 and renpy.version_tuple.minor >= 1): # Only works in Ren'py 8.1.1 and above
                        $ my_key = [sc_prefix + "K_UP", sc_prefix + "mousedown_4"]
                    else:
                        if sc_prefix == "noshift_": # Workaround until a solution is found for shift+mousewheel
                            $ my_key = [sc_prefix + "K_UP", "mousedown_4"]
                        else:
                            $ my_key = sc_prefix + "K_UP"

                    key my_key capture True:
                        if page-1 <= start and previous:
                            action (SetLocalVariable("page", page-1), SetLocalVariable("page_offset", page_offset-previous))
                        else:
                            action SetLocalVariable("page", page-1)
                if page < page_nb:
                    if renpy.version_tuple.major > 8 or (renpy.version_tuple.major == 8 and renpy.version_tuple.minor >= 1): # Only works in Ren'py 8.1.1 and above
                        $ my_key = [sc_prefix + "K_DOWN", sc_prefix + "mousedown_5"]
                    else:
                        if sc_prefix == "noshift_": # Workaround until a solution is found for shift+mousewheel
                            $ my_key = [sc_prefix + "K_DOWN", "mousedown_5"]
                        else:
                            $ my_key = sc_prefix + "K_DOWN"

                    key my_key capture True:
                        if page+1 > finish and next:
                            action (SetLocalVariable("page", page+1), SetLocalVariable("page_offset", page_offset+next))
                        else:
                            action SetLocalVariable("page", page+1)

                hbox tooltip "Change item page":
                    if next:
                        xsize xres(180)
                    else:
                        xmaximum xres(180)

                    if previous:
                        textbutton "↑" style "UI_button":
                            xalign 0.0
                            xsize xres(22)
                            ysize yres(22)
                            action (SetLocalVariable("page_offset", page_offset-previous), SetLocalVariable("page", page_offset))
                            text_size res_font(14)
                            text_font "DejaVuSans.ttf"

                    for p in range(start, finish):
                        textbutton str(p+1) style "UI_button":
                            xalign 0.0
                            xsize xres(22)
                            ysize yres(22)
                            action SetLocalVariable("page", p+1)
                            text_size res_font(14)
                            text_selected_bold True

                            if sc_prefix == "shift_":
                                tooltip "Use shift + up/down arrows or mousewheel to cycle item pages."
                            else:
                                tooltip "Use up/down arrows or mousewheel to cycle item pages."

                    if next:
                        textbutton "↓" style "UI_button":
                            xalign 0.0
                            xsize xres(22)
                            ysize yres(22)
                            action (SetLocalVariable("page_offset", page_offset+next), SetLocalVariable("page", page_offset+next+1))
                            text_size res_font(14)
                            text_font "DejaVuSans.ttf"


screen item_profile(it):

    zorder 5

    $ acts = it.get_acts(owner, counterpart)

    if owner.type == "girl":
        default focused_char = owner
    elif counterpart and counterpart.type == "girl":
        default focused_char = counterpart
    else:
        default focused_char = None

    on "hide" action SetVariable("selected_item", None)

    frame:

        id "item_profile"

        background c_ui_darker

        xalign 0.5
        yalign 0.33
        xpadding 6
        ypadding 6
        xsize xres(300)
        xfill True
        yfill False

        has vbox

        if "bargain" not in acts:
            use close(Hide("item_profile"), name = "返回")
            key "mouseup_3" action Hide("item_profile")


        frame xalign 0.5 xfill True:
            add it.pic.get(*res_tb(100)) xalign 0.5

        frame xalign 0.5 xfill True:
            background None

            has vbox xfill True xalign 0.5

            $ text1 = __(it.name)

            if isinstance(it, Item):
                if it.charges and it.charges > 1 and it.usage == "use":
                    $ text1 += " (" + str(it.charges) + ")"

            text text1 xalign 0.5

            if it.target == "MC":
                $ col = c_steel
            elif it.target == "girl":
                $ col = c_pink
            elif it.target == "minion":
                $ col = c_purple
            else:
                $ col = c_orange

            text "" size res_font(8)

            if isinstance(type, ItemType):
                text "{color=[col]}" + __(it.type.name) + "{/color}" xalign 0.5 size res_font(18)
            else:
                text "{color=[col]}" + __(setting_name_dict[it.target.capitalize()]) + "{/color}" xalign 0.5 size res_font(18)

            if isinstance(it, Item):
                text __(it.base_description) size res_font(14) xalign 0.5
            text __(it.description) size res_font(14) xalign 0.5

            text ""

            if "buy" in acts:
                text str(it.get_price("buy")) + "金币" xalign 0.5
                text ""

            if "bargain" in acts:
                text str(it.get_price("bargain")) + "金币" xalign 0.5
                text ""

            if "sell" in acts:
                text str(it.get_price("sell")) + "金币" xalign 0.5
                text ""

            if isinstance(it, Item) and it in MC.items and not it.sellable:
                text "Unsellable" italic True xalign 0.5
                text ""

            hbox spacing 10 xalign 0.5:
                for act in acts:
                    textbutton __(button_name_dict[capitalize(act)]) action Return((it, act)) xalign 0.5:
                        if owner.type == "girl" and act in ("equip", "unequip", "use"):
                            hovered SetScreenVariable("focused_char", owner)
                        elif counterpart and counterpart.type == "girl":
                            hovered SetScreenVariable("focused_char", counterpart)
                            if owner.type == "girl":
                                unhovered SetScreenVariable("focused_char", owner)

                if "bargain" in acts:
                    textbutton __("跳过") action Return("leave") xalign 0.5

    if isinstance(it, Item) and focused_char and (it.can_wear("girl") or it.can_use("girl")):
        if focused_char == left_focus:
            use girl_stats_light(left_focus, panel="left")
        else:
            use girl_stats_light(right_focus, panel="right")

screen inventory(char, counterpart=None):
    frame:
        xalign 0.5
        yalign 0.0
        xfill False
        yfill False

        has vbox spacing 10 box_wrap True

        if char:
            for slot in char.slots:
                $ eq = None
                for it in char.equipped:
                    if it.slot == slot:
                        $ eq = it
                        $ acts = it.get_acts(char, counterpart)

                vbox:
                    text setting_name_dict[slot.capitalize()] size res_font(14) xalign 0.5 color c_brown

                    button xsize yres(60) ysize yres(60) xfill True yfill True xalign 0.5:
                        style "girlbutton_blue"
                        if eq:
                            add eq.pic.get(*res_tb(45)) xalign 0.5 yalign 0.5
                            action (Show("item_profile", it=eq, transition = dissolve), SetVariable("owner", char), SetVariable("counterpart", counterpart), SetVariable("selected_item", eq), SetField(MC, "active_inv_filter", [slot]), SelectedIf(slot in MC.active_inv_filter))
                            tooltip __(eq.description)
                        else:
                            text "空的" size res_font(12) italic True xalign 0.5 yalign 0.5
                            action (SetField(MC, "active_inv_filter", [slot]), SelectedIf(slot in MC.active_inv_filter))
                            tooltip "这个栏位没有装备物品。"


screen item_filter(filters=inventory_filters["base"]):

    if MC.active_inv_filter not in filters:
        $ active_inv_filter = []

    vbox xfill False yfill False spacing 3:
        for filter in filters:
            frame xsize xres(38) ysize yres(38) xpadding 0 xmargin 0:
                button xfill True yfill True xpadding 0 xmargin 0 idle_background None:

                    action (SetField(MC, "active_inv_filter", filter_list[filter]), Function(renpy.restart_interaction))

                    if filter:
                        if MC.active_inv_filter and MC.active_inv_filter[0] in filter_list[filter]:
                            add "filter_" + filter xalign 0.5 yalign 0.5
                        else:
                            add "filter_" + filter + "_unselect" xalign 0.5 yalign 0.5
                        tooltip __("Show %s items.") % __(setting_name_dict[filter])
                    else:
                        if not MC.active_inv_filter:
                            add "filter_all" xalign 0.5 yalign 0.5
                        else:
                            add "filter_all_unselect" xalign 0.5 yalign 0.5
                        tooltip "Show all items."


#### END OF BK ITEMS FILE ####
