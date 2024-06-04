#### BK ITEMS AND FURNITURE ####
## Labels are used instead of Functions to make sure we are using global variables

## ITEM TYPES ##
init -2 python:
    IT_Weapon = ItemType("Weapon", usage = "wear", slot = "hands", filter = "weapon", sound = "sword sheath.mp3")
    IT_Dress = ItemType("Dress", usage = "wear", slot = "body", filter = "clothing", sound = "equip dress.ogg", adjectives = "dress")
    IT_Ring = ItemType("Ring", usage = "wear", slot = "finger", filter = "trinket", sound = "equip item.wav", adjectives = "ring")
    IT_Necklace = ItemType("Necklace", usage = "wear", slot = "neck", filter = "trinket", sound = "equip item.wav", adjectives = "necklace")
    IT_Accessory = ItemType("Accessory", usage = "wear", slot = "accessory", filter = "clothing", sound = "equip item.wav", adjectives = "dress")
    IT_Toy = ItemType("Toy", usage = "auto_rest", filter = "consumable", sound = "vibro.ogg")
    IT_Supplies = ItemType("Supplies", usage = "auto_work", filter = "consumable", sound = "spell.ogg")
    IT_Food = ItemType("Food", usage = "use", filter = "consumable", sound = "crunch.ogg", adjectives = "food") # Food effects may not stack
    IT_Gift = ItemType("Gift", usage = "give", sound = "uhm.mp3", adjectives = "misc")
    IT_Flower = ItemType("Flower", usage = "give", sound = s_surprise, adjectives = "misc", dir="Gift")
    IT_Misc = ItemType("Misc", usage = "use", sound = "spell.ogg", adjectives = "misc") # Misc effects may not stack
    IT_Story = ItemType("Misc", usage = None, sound = "spell.ogg", adjectives = "misc", sellable=False, giveable=False)
    IT_Passive = ItemType("Misc", usage = "wear", slot = "misc", sound = "equip item.wav", adjectives = "misc", sellable=False)

    all_equipement_types = ["weapon", "dress", "ring", "necklace", "accessory", "passive"]

## FURNITURE TYPES ##
# A tuple (type, description)

    furniture_types = [("Decoration", "为你的青楼吸引新类型的顾客"),
                       ("Furnishing", "开启更多吸引客户的选择"),
                       ("Utility", "协助广告、安全和维护"),
                       ("Comfort", "帮助女孩在青楼中过到更舒适"),
                       ("Windows", "影响女孩的喜好"),
                       ("Altars", "在这里祈祷并得到结果，仅此一次"),
                       ("Gizmos", "来自已逝科技时代的奇怪文物")
                       ]

## ITEMS ##

label init_items():
    python:

        # REGULAR ITEMS #

        all_items = [
                    Item(name = '短剑', target = 'MC', type = IT_Weapon, pic = 'Short sword.webp', rank = 1, rarity = 1, price = 250, effects = (Effect('change', 'strength', 1), ), description =  ""),
                    Item(name = '弯刀', target = 'MC', type = IT_Weapon, pic = 'Cutlass.webp', rank = 1, rarity = 2, price = 500, effects = (Effect('change', 'strength', 2), ), description =  "它不是一把匕首。它是一把弯刀。"),
                    Item(name = '斧头', target = 'MC', type = IT_Weapon, pic = 'Axe.webp', rank = 2, rarity = 2, price = 1000, effects = (Effect('change', 'strength', 2), Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = '长矛', target = 'MC', type = IT_Weapon, pic = 'Lance.webp', rank = 2, rarity = 2, price = 2500, effects = (Effect('change', 'strength', 3), Effect('change', 'charisma', 1), ), description =  ""),
                    Item(name = '长剑', target = 'MC', type = IT_Weapon, pic = 'Long sword.webp', rank = 2, rarity = 3, price = 3500, effects = (Effect('change', 'strength', 3), Effect('change', 'charisma', 1), Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = '刺剑', target = 'MC', type = IT_Weapon, pic = 'Rapier.webp', rank = 3, rarity = 3, price = 5000, effects = (Effect('change', 'strength', 4), Effect('change', 'charisma', 2), ), description =  ""),
                    Item(name = '战斧', target = 'MC', type = IT_Weapon, pic = 'Battle axe.webp', rank = 3, rarity = 3, price = 10000, effects = (Effect('change', 'strength', 5), Effect('change', 'spirit', 2), ), description =  ""),
                    Item(name = '战锤', target = 'MC', type = IT_Weapon, pic = 'Warhammer.webp', rank = 3, rarity = 4, price = 17500, effects = (Effect('change', 'strength', 5), Effect('change', 'charisma', 2), Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = '圣剑', target = 'MC', type = IT_Weapon, pic = 'Holy sword.webp', rank = 4, rarity = "U", price = 40000, effects = (Effect('change', 'strength', 6), Effect('change', 'spirit', 3), ), description =  "这把剑充满了力量。光线在它的剑上反射得如此明亮，以致于能使天使自己失明。"),
                    Item(name = '魔剑', target = 'MC', type = IT_Weapon, pic = 'Demon sword.webp', rank = 4, rarity = "S", price = 100000, effects = (Effect('change', 'strength', 8), Effect('change', 'charisma', 4), Effect('change', 'spirit', -2), ), description =  "剑刃随着被困在里面的恶魔的黑暗怒火而跳动。据说他吞噬了每一个被这把剑杀死的可怜的灵魂。"),
                    Item(name = '扫帚之杖', target = 'MC', type = IT_Weapon, pic = 'Broom staff.webp', rank = 1, rarity = 1, price = 250, effects = (Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = '树木之杖', target = 'MC', type = IT_Weapon, pic = 'Wooden staff.webp', rank = 1, rarity = 2, price = 500, effects = (Effect('change', 'spirit', 2), ), description =  ""),
                    Item(name = '地精之杖', target = 'MC', type = IT_Weapon, pic = 'Goblin staff.webp', rank = 2, rarity = 2, price = 1000, effects = (Effect('change', 'charisma', 1), Effect('change', 'spirit', 2), ), description =  ""),
                    Item(name = '青铜之杖', target = 'MC', type = IT_Weapon, pic = 'Bronze staff.webp', rank = 2, rarity = 2, price = 2500, effects = (Effect('change', 'strength', 1), Effect('change', 'spirit', 3), ), description =  ""),
                    Item(name = '呼风之杖', target = 'MC', type = IT_Weapon, pic = 'Wind staff.webp', rank = 2, rarity = 3, price = 3500, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 1), Effect('change', 'spirit', 3), ), description =  ""),
                    Item(name = '治愈之杖', target = 'MC', type = IT_Weapon, pic = 'Healing staff.webp', rank = 3, rarity = 3, price = 5000, effects = (Effect('change', 'charisma', 2), Effect('change', 'spirit', 4), ), description =  ""),
                    Item(name = '雷霆之杖', target = 'MC', type = IT_Weapon, pic = 'Thunder staff.webp', rank = 3, rarity = 3, price = 10000, effects = (Effect('change', 'strength', 2), Effect('change', 'spirit', 5), ), description =  ""),
                    Item(name = '碧玉之杖', target = 'MC', type = IT_Weapon, pic = 'Emerald staff.webp', rank = 3, rarity = 4, price = 17500, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 2), Effect('change', 'spirit', 5), ), description =  ""),
                    Item(name = '水晶之杖', target = 'MC', type = IT_Weapon, pic = 'Crystal staff.webp', rank = 4, rarity = 4, price = 40000, effects = (Effect('change', 'strength', 3), Effect('change', 'spirit', 6), ), description =  ""),
                    Item(name = '天使之杖', target = 'MC', type = IT_Weapon, pic = 'Angel staff.webp', rank = 4, rarity = 5, price = 100000, effects = (Effect('change', 'charisma', 2), Effect('change', 'spirit', 8), ), description =  ""),
                    Item(name = '飞刀', target = 'MC', type = IT_Weapon, pic = 'Throwing knife.webp', rank = 1, rarity = 1, price = 250, effects = (Effect('change', 'charisma', 1), ), description =  ""),
                    Item(name = '飞斧', target = 'MC', type = IT_Weapon, pic = 'Throwing axe.webp', rank = 1, rarity = 2, price = 500, effects = (Effect('change', 'charisma', 2), ), description =  ""),
                    Item(name = '弓箭', target = 'MC', type = IT_Weapon, pic = 'Bow.webp', rank = 2, rarity = 2, price = 1000, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 2), ), description =  ""),
                    Item(name = '华丽之弓', target = 'MC', type = IT_Weapon, pic = 'Ornate bow.webp', rank = 2, rarity = 2, price = 2500, effects = (Effect('change', 'charisma', 3), Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = '燧发枪', target = 'MC', type = IT_Weapon, pic = 'Flintlock.webp', rank = 2, rarity = 3, price = 3500, effects = (Effect('change', 'strength', 2), Effect('change', 'charisma', 3), ), description =  ""),
                    Item(name = '弓弩', target = 'MC', type = IT_Weapon, pic = 'Crossbow.webp', rank = 3, rarity = 3, price = 5000, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 4), Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = '连发枪', target = 'MC', type = IT_Weapon, pic = 'Repeater.webp', rank = 3, rarity = 3, price = 10000, effects = (Effect('change', 'strength', 2), Effect('change', 'charisma', 5), ), description =  ""),
                    Item(name = '霹雳枪', target = 'MC', type = IT_Weapon, pic = 'Blunderbuss.webp', rank = 3, rarity = 4, price = 17500, effects = (Effect('change', 'strength', 3), Effect('change', 'charisma', 5), ), description = "这个。是。我的火枪！"),
                    Item(name = '神圣手雷', target = 'MC', type = IT_Weapon, pic = 'Holy handgrenade.webp', rank = 4, rarity = 4, price = 40000, effects = (Effect('change', 'charisma', 6), Effect('change', 'spirit', 3), ), description =  ""),
                    Item(name = '死亡手枪', target = 'MC', type = IT_Weapon, pic = 'Death dispenser.webp', rank = 4, rarity = 5, price = 100000, effects = (Effect('change', 'strength', 4), Effect('change', 'charisma', 8), Effect('change', 'spirit', -2), ), description =  ""),
                    Item(name = '阿里奥斯护身符', target = 'MC', type = IT_Necklace, pic = 'Arios amulet.webp', rank = 1, rarity = "U", price = 25000, effects = (), description = "完成阿里奥斯骑士任务的独特奖励。"),
                    Item(name = '莎莉娅护身符', target = 'MC', type = IT_Necklace, pic = 'Shalia talisman.webp', rank = 1, rarity = "U", price = 25000, effects = (), description = "完成莎莉娅影子任务的独特奖励。"),
                    Item(name = '商人印章', target = 'MC', type = IT_Necklace, pic = 'Merchant sigil.webp', rank = 1, rarity = "U", price = 25000, effects = (), description = "完成商人公会任务的独特奖励。"),
                    Item(name = '皮草靴', target = 'MC', type = IT_Accessory, pic = 'Fur boots.webp', rank = 1, rarity = 1, price = 500, effects = (Effect('change', 'speed', 1), ), ),
                    Item(name = '皮革靴', target = 'MC', type = IT_Accessory, pic = 'Leather boots.webp', rank = 1, rarity = 2, price = 2000, effects = (Effect('change', 'speed', 2), ), ),
                    Item(name = '精灵靴', target = 'MC', type = IT_Accessory, pic = 'Elven boots.webp', rank = 2, rarity = 3, price = 10000, effects = (Effect('change', 'speed', 3), ), ),
                    Item(name = '马匹', target = 'MC', type = IT_Accessory, pic = 'Horse.webp', rank = 3, rarity = 4, price = 50000, effects = (Effect('change', 'speed', 4), ), ),
                    Item(name = '黑马', target = 'MC', type = IT_Accessory, pic = 'Dark horse.webp', rank = 4, rarity = 5, price = 150000, effects = (Effect('change', 'speed', 5), ), ),
                    Item(name = '龙蛋', target = 'MC', type = IT_Misc, pic = 'Dragon egg.webp', rank = 1, rarity = "S", charges = 1, price = 5000, effects = (Effect('gain', 'skill points', 1), ), description =  "“他并不是龙……”\n吃了这个，风险自负！", sound = "crunch.ogg", hidden_effect = True),
                    Item(name = '指虎', target = 'girl', type = IT_Weapon, pic = 'Knuckle duster.webp', rank = 1, rarity = 1, price = 50, effects = (Effect('change', 'defense', 1), ), ),
                    Item(name = '弯钩', target = 'girl', type = IT_Weapon, pic = 'Hook.webp', rank = 1, rarity = 1, price = 250, effects = (Effect('change', 'defense', 2), ), ),
                    Item(name = '剃刀', target = 'girl', type = IT_Weapon, pic = 'Shiv.webp', rank = 1, rarity = 2, price = 500, effects = (Effect('change', 'defense', 3), ), ),
                    Item(name = '小刀', target = 'girl', type = IT_Weapon, pic = 'Knife.webp', rank = 2, rarity = 2, price = 1000, effects = (Effect('change', 'defense', 4), ), ),
                    Item(name = '匕首', target = 'girl', type = IT_Weapon, pic = 'Dagger.webp', rank = 2, rarity = 2, price = 1750, effects = (Effect('change', 'defense', 5), ), ),
                    Item(name = '祭刀', target = 'girl', type = IT_Weapon, pic = 'Sacrificial knife.webp', rank = 2, rarity = 3, price = 2750, effects = (Effect('change', 'defense', 6), ), ),
                    Item(name = '棒槌', target = 'girl', type = IT_Weapon, pic = 'Mace.webp', rank = 3, rarity = 3, price = 5000, effects = (Effect('change', 'defense', 7), ), ),
                    Item(name = '皮鞭', target = 'girl', type = IT_Weapon, pic = 'Whip.webp', rank = 3, rarity = 4, price = 10000, effects = (Effect('change', 'defense', 8), ), ),
                    Item(name = '钢鞭', target = 'girl', type = IT_Weapon, pic = 'Steel whip.webp', rank = 4, rarity = 4, price = 25000, effects = (Effect('change', 'defense', 9), ), ),
                    Item(name = '魔刀', target = 'girl', type = IT_Weapon, pic = 'Magic blade.webp', rank = 4, rarity = 5, price = 60000, effects = (Effect('change', 'defense', 10), ), ),
                    Item(name = '按摩棒', target = 'girl', type = IT_Toy, pic = 'Dildo.webp', rank = 1, rarity = 2, charges = 8, price = 125, effects = (Effect('gain', 'sex', 1, 0.5), ), description = "休息时有机会提高性交（有限使用）。"),
                    Item(name = 'XL按摩棒', target = 'girl', type = IT_Toy, pic = 'XL dildo.webp', rank = 2, rarity = 3, charges = 8, price = 500, effects = (Effect('gain', 'sex', 2, 0.5), ), description = "休息时有机会提高性交（有限使用）。"),
                    Item(name = 'XXL按摩棒', target = 'girl', type = IT_Toy, pic = 'XXL dildo.webp', rank = 3, rarity = 4, charges = 8, price = 2500, effects = (Effect('gain', 'sex', 3, 0.5), ), description = "休息时有机会提高性交（有限使用）。"),
                    Item(name = '黑色按摩棒', target = 'girl', type = IT_Toy, pic = 'Black dildo.webp', rank = 4, rarity = 5, charges = 8, price = 10000, effects = (Effect('gain', 'sex', 5, 0.5), ), description = "休息时有机会提高性交（有限使用）。"),
                    Item(name = '肛塞', target = 'girl', type = IT_Toy, pic = 'Butt plug.webp', rank = 1, rarity = 2, charges = 8, price = 125, effects = (Effect('gain', 'anal', 1, 0.5), ), description = "休息时有机会改善肛门（有限使用）。"),
                    Item(name = '打气筒', target = 'girl', type = IT_Toy, pic = 'Butt pump.webp', rank = 2, rarity = 3, charges = 8, price = 500, effects = (Effect('gain', 'anal', 2, 0.5), ), description = "休息时有机会改善肛门（有限使用）。"),
                    Item(name = '肛门按摩棒', target = 'girl', type = IT_Toy, pic = 'Anal dildo.webp', rank = 3, rarity = 4, charges = 8, price = 2500, effects = (Effect('gain', 'anal', 3, 0.5), ), description = "休息时有机会改善肛门（有限使用）。"),
                    Item(name = '拉珠', target = 'girl', type = IT_Toy, pic = 'Anal beads.webp', rank = 4, rarity = 5, charges = 8, price = 10000, effects = (Effect('gain', 'anal', 5, 0.5), ), description = "休息时有机会改善肛门（有限使用）。"),
                    Item(name = '绳索', target = 'girl', type = IT_Toy, pic = 'Ropes.webp', rank = 1, rarity = 2, charges = 8, price = 125, effects = (Effect('gain', 'fetish', 1, 0.5), ), description = "休息时有机会改善皮绳愉虐（有限的使用）。"),
                    Item(name = '手铐', target = 'girl', type = IT_Toy, pic = 'Cuffs.webp', rank = 2, rarity = 3, charges = 8, price = 500, effects = (Effect('gain', 'fetish', 2, 0.5), ), description = "休息时有机会改善皮绳愉虐（有限的使用）。"),
                    Item(name = '口球', target = 'girl', type = IT_Toy, pic = 'Gag.webp', rank = 3, rarity = 4, charges = 8, price = 2500, effects = (Effect('gain', 'fetish', 3, 0.5), ), description = "休息时有机会改善皮绳愉虐（有限的使用）。"),
                    Item(name = '眼罩', target = 'girl', type = IT_Toy, pic = 'Blindfold.webp', rank = 4, rarity = 5, charges = 8, price = 10000, effects = (Effect('gain', 'fetish', 5, 0.5), ), description = "休息时有机会改善皮绳愉虐（有限的使用）。"),
                    Item(name = '催情凝胶', target = 'girl', type = IT_Toy, pic = 'Arousing gel.webp', rank = 1, rarity = 2, charges = 8, price = 125, effects = (Effect('gain', 'service', 1, 0.5), ), description = "休息时有机会改善性服务（有限的使用）。"),
                    Item(name = '跳蛋', target = 'girl', type = IT_Toy, pic = 'Egg vibrator.webp', rank = 2, rarity = 3, charges = 8, price = 500, effects = (Effect('gain', 'service', 2, 0.5), ), description = "休息时有机会改善性服务（有限的使用）。"),
                    Item(name = '长型振动棒', target = 'girl', type = IT_Toy, pic = 'Long vibrator.webp', rank = 3, rarity = 4, charges = 8, price = 2500, effects = (Effect('gain', 'service', 3, 0.5), ), description = "休息时有机会改善性服务（有限的使用）。"),
                    Item(name = '电动振动棒', target = 'girl', type = IT_Toy, pic = 'Arcanic vibrator.webp', rank = 4, rarity = 5, charges = 8, price = 10000, effects = (Effect('gain', 'service', 5, 0.5), ), description = "休息时有机会改善性服务（有限的使用）。"),
                    Item(name = '幸运护身符', target = 'girl', type = IT_Necklace, pic = 'Lucky charm.webp', rank = 1, rarity = 2, price = 1250, effects = (Effect('special', 'lucky', 1), ), description = "据说它能给它的主人带来好运。它的原主人兔子可能不同意……"),
                    Item(name = '皮质项圈', target = 'girl', type = IT_Necklace, pic = 'Leather choker.webp', rank = 1, rarity = 2, price = 750, effects = (Effect('boost', 'obedience tests', 0.2), ), ),
                    Item(name = '青铜护身符', target = 'girl', type = IT_Necklace, pic = 'Bronze amulet.webp', rank = 2, rarity = 3, price = 2500, effects = (Effect('boost', 'all regular skills gains', 0.05), ), ),
                    Item(name = '白银护身符', target = 'girl', type = IT_Necklace, pic = 'Silver amulet.webp', rank = 3, rarity = 4, price = 12500, effects = (Effect('boost', 'all regular skills gains', 0.1), ), ),
                    Item(name = '黄金护身符', target = 'girl', type = IT_Necklace, pic = 'Gold amulet.webp', rank = 4, rarity = 5, price = 25000, effects = (Effect('boost', 'all regular skills gains', 0.15), ), ),
                    Item(name = '怪物珍珠项链', target = 'girl', type = IT_Necklace, pic = 'Monster pearl necklace.webp', rank = 3, rarity = 5, price = 25000, effects = (Effect('boost', 'all sex skills gains', 0.1), ), description =  "它来自大海……"),
                    Item(name = '麦酒', target = 'girl', type = IT_Supplies, pic = 'Ale.webp', rank = 1, rarity = 1, charges = 10, price = 500, effects = (Effect('change', 'waitress results', 1), ), description =  "工作时使用。"),
                    Item(name = '按摩油', target = 'girl', type = IT_Supplies, pic = 'Massage oil.webp', rank = 1, rarity = 1, charges = 10, price = 500, effects = (Effect('change', 'masseuse results', 1), ), description =  "工作时使用。"),
                    Item(name = '日晒油', target = 'girl', type = IT_Supplies, pic = 'Tanning oil.webp', rank = 1, rarity = 1, charges = 10, price = 500, effects = (Effect('change', 'dancer results', 1), ), description =  "工作时使用。"),
                    Item(name = '竹扇', target = 'girl', type = IT_Supplies, pic = 'Fans.webp', rank = 1, rarity = 1, charges = 10, price = 500, effects = (Effect('change', 'geisha results', 1), ), description =  "工作时使用。"),
                    Item(name = '性感香水', target = 'girl', type = IT_Supplies, pic = 'Sensual perfume.webp', rank = 1, rarity = 3, charges = 10, price = 750, effects = (Effect('change', 'service results', 1), ), description =  "工作时使用。"),
                    Item(name = '润滑液', target = 'girl', type = IT_Supplies, pic = 'Gel.webp', rank = 1, rarity = 3, charges = 10, price = 750, effects = (Effect('change', 'sex results', 1), ), description =  "工作时使用。"),
                    Item(name = '灌肠剂', target = 'girl', type = IT_Supplies, pic = 'Enema.webp', rank = 1, rarity = 3, charges = 10, price = 750, effects = (Effect('change', 'anal results', 1), ), description =  "工作时使用。"),
                    Item(name = '低温蜡烛', target = 'girl', type = IT_Supplies, pic = 'Wax.webp', rank = 1, rarity = 3, charges = 10, price = 750, effects = (Effect('change', 'fetish results', 1), ), description =  "工作时使用。"),
                    Item(name = '飞龙蛋', target = 'girl', type = IT_Misc, pic = 'Wyvern egg.webp', rank = 1, rarity = "S", charges = 1, price = 15000, effects = (Effect('gain', 'perk', 1), ), description = "一道适合青楼女王的菜肴。", sound = "crunch.ogg"),
                    Item(name = '眼镜', target = 'girl', type = IT_Accessory, pic = 'Glasses.webp', rank = 1, rarity = 3, price = 1000, effects = (Effect('boost', 'xp gains', 0.1), ), ),
                    Item(name = '尾巴', target = 'girl', type = IT_Accessory, pic = 'Tail.webp', rank = 1, rarity = 3, price = 1000, effects = (Effect('boost', 'reputation gains', 0.2), ), ),
                    Item(name = '兔耳发饰', target = 'girl', type = IT_Accessory, pic = 'Bunny ears.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'waitress results', 1), ), ),
                    Item(name = '发簪', target = 'girl', type = IT_Accessory, pic = 'Hairpin.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'masseuse results', 1), ), ),
                    Item(name = '舞娘面纱', target = 'girl', type = IT_Accessory, pic = 'Nun veil.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'dancer results', 1), ), ),
                    Item(name = '能剧面具', target = 'girl', type = IT_Accessory, pic = 'Noh mask.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'geisha results', 1), ), ),
                    Item(name = '猫耳发饰', target = 'girl', type = IT_Accessory, pic = 'Cat ears.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'service results', 1), ), ),
                    Item(name = '护士长帽', target = 'girl', type = IT_Accessory, pic = 'Nurse hat.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'sex results', 1), ), ),
                    Item(name = '皮帽', target = 'girl', type = IT_Accessory, pic = 'Leather cap.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'anal results', 1), ), ),
                    Item(name = '女仆头带', target = 'girl', type = IT_Accessory, pic = 'Maid hat.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'fetish results', 1), ), ),
                    Item(name = '魔法笔记本', target = 'MC', type = IT_Passive, pic = 'Magic notebook.webp', template = False, rank = 1, rarity = "S", price = 0, effects = (Effect('special', 'notebook', 1), ), description = "这个方便的笔记本将储存你所知道的关于你的女孩的所有信息。它神奇地记录了你所有的想法。等等，不要想{i}那个{/i}……太晚了。", hidden_effect = True),
                    Item(name = '愈合粉', target = 'minion', type = IT_Misc, pic = 'healing powder.webp', template = False, rank = 1, rarity = "M", charges = 1, price = 100, effects = (Effect('special', 'heal minion', 1), ), description = "这种来自东方的神秘粉末可以治愈奴仆的伤口或修复神奇的工艺品。副作用可能包括头晕、好色、全身长出触角等。"),
                    Item(name = 'Cimerian废料', target = 'misc', type = IT_Misc, pic = 'Cimerian scrap.webp', sound=s_vibro, template = False, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 250, effects = (), description = "一件神秘的古代科技的垃圾。"),
                    Item(name = 'Cimerian文物', target = 'misc', type = IT_Misc, pic = 'Cimerian artefact.webp', sound=s_vibro, template = False, rank = 1, max_rank = 5, rarity = 4, charges = 1, price = 1000, effects = (), description = "一件神秘的古代机械。也是……垃圾……"),
                    Item(name = "避雷针", target = 'MC', type = IT_Story, pic = "lightning rod.webp", template=False, rank=2, max_rank = 5, rarity=3, price = 1000, effects = (), description = "防止闪电伤害你。在适当的情况下，它可以救你的命，尽管在青楼工作时被闪电击中的机会很低。梅毒棒可能更有用。"),

                    Item(name = '白色鲜花', target = 'girl', type = IT_Flower, pic = 'White flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'white', 1), ), description = "鲜花常被用作表达爱意的礼物。", hidden_effect = True),
                    Item(name = '黄色鲜花', target = 'girl', type = IT_Flower, pic = 'Yellow flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'yellow', 1), ), description = "鲜花常被用作表达爱意的礼物。", hidden_effect = True),
                    Item(name = '红色鲜花', target = 'girl', type = IT_Flower, pic = 'Red flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'red', 1), ), description = "鲜花常被用作表达爱意的礼物。", hidden_effect = True),
                    Item(name = '绿色鲜花', target = 'girl', type = IT_Flower, pic = 'Green flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'green', 1), ), description = "鲜花常被用作表达爱意的礼物。", hidden_effect = True),
                    Item(name = '蓝色鲜花', target = 'girl', type = IT_Flower, pic = 'Blue flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'blue', 1), ), description = "鲜花常被用作表达爱意的礼物。", hidden_effect = True),
                    Item(name = '橙色鲜花', target = 'girl', type = IT_Flower, pic = 'Orange flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'orange', 1), ), description = "鲜花常被用作表达爱意的礼物。", hidden_effect = True),
                    Item(name = '紫色鲜花', target = 'girl', type = IT_Flower, pic = 'Purple flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'purple', 1), ), description = "鲜花常被用作表达爱意的礼物。", hidden_effect = True),
                    Item(name = '粉色鲜花', target = 'girl', type = IT_Flower, pic = 'Pink flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'pink', 1), ), description = "鲜花常被用作表达爱意的礼物。", hidden_effect = True),
                    Item(name = '黑色鲜花', target = 'girl', type = IT_Flower, pic = 'Black flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'black', 1), ), description = "鲜花常被用作表达爱意的礼物。", hidden_effect = True),
                    ]


        # SPECIAL ITEMS AND FURNITURE #

        blueprint_item = Item(name = '古代的蓝图', target = 'MC', type = IT_Story, pic = 'scanner blueprint.webp', template = False, rank = 1, rarity = "S", price = 0, effects = [], description = "一张古老的蓝图写在一种轻而坚固的纸质材料上。说明书是外国的，无法解读，但一个熟练的工匠也许可以理解它。", hidden_effect = True)

        vitals_scanner = Furniture('Strange machine', type='Gizmos', pic='scanner.webp', rank=2, chapter=2, cost=[('wood', 20), ('dye', 20), ('leather', 20)], duration=4, effects=[Effect("special", "autorest", 1, scope="brothel")], base_description="这台神秘的机器闪烁着脉动的魔法能量。") #  It scans your girls automatically to make sure they are fit to work.

        billboard = Furniture('Clockwork billboard', type='Furnishing', pic='billboard.webp', rank=2, chapter=2, cost=[('wood', 40), ('dye', 25), ('leather', 10)], duration=5, effects=[Effect("special", "advanced advertising", 1, scope="brothel")], base_description="这个气势磅礴的广告牌肯定会吸引一些人的注意。解锁高级广告设置。") #  Unlocks advanced advertising settings

        bast_letter = Item("Bast的情书", "MC", type=IT_Story, pic="Scroll of etiquette.webp", template = False, rank = 1, rarity = "S", price = 0, effects = [], description = "Bast写给她以前的姘头的情书。包含有罪的信息。", hidden_effect = True)

        extractor_items = {"extractor1" : Item(name="萃取器MkI", target="MC", type=IT_Story, pic="extractor1.webp", template = False, rarity = "S", price = 5000, effects=[], description = "这个奇怪的蒸汽机可以让你自动收获木材、染料或皮革。在产地部署。"),
                           "extractor2" : Item(name="萃取器MkII", target="MC", type=IT_Story, pic="extractor2.webp", template = False, rarity = "S", price = 25000, effects=[], description = "这个奇怪的蒸汽机可以让你自动收获大理石、丝绸或矿石。在产地部署。"),
                            }

        magic_notebook = Item(name = '魔法笔记本', target = 'MC', type = IT_Passive, pic = 'Magic notebook.webp', template = False, rank = 1, rarity = "S", price = 0, effects = (Effect('special', 'notebook', 1), ), description = "这个方便的笔记本将储存你所知道的关于你的女孩的所有信息。它能神奇地写下你所有的想法。等等，不要想{i}那个{/i}……太晚了。", hidden_effect = True)

        mania_amulet = Item(name = "廉价的符咒", target = 'MC', type = IT_Story, pic = 'cheap charm.webp', template = False, rank = 1, rarity = "S", price = 10, description = "一个廉价的护身符，与一封神秘的信一起被发现，信中提到在公会区有一个叫“狂热”的俱乐部。", hidden_effect = True)

        toy_hammer = Item(name="光明之锤", target = 'MC', type = IT_Story, pic = 'toy hammer.webp', template = False, rank = 1, rarity = "S", price = 0, description = "一个用廉价材料制成的微型“战锤”。据说可以对付国士无双，但它看起来连一只鼹鼠都打不死。", hidden_effect = True)

        mizuki_kimono = Item(name = "Mizuki的和服", target = 'MC', type = IT_Story, pic = 'Kimono.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="dress", description = "神秘的大国师Mizuki留下的和服。", hidden_effect = True)

        makibishi = Item(name = "撒菱", target = 'MC', type = IT_Misc, pic = 'bronze makibishi.webp', template = False, rank = 1, rarity = "S", price = 500, description = "在猎杀女忍者的过程中自动抓到一个国师。", hidden_effect = True)
#                       Item(name = "Iron Makibishi", target = 'MC', type = IT_Story, pic = 'iron makibishi.webp', template = False, rank = 2, rarity = "S", price = 1000, description = "Slows down Kunoichi movements during ninja hunt (medium effect).", hidden_effect = True),
#                       Item(name = "Steel Makibishi", target = 'MC', type = IT_Story, pic = 'steel makibishi.webp', template = False, rank = 3, rarity = "S", price = 1500, description = "Slows down Kunoichi movements during ninja hunt (large effect).", hidden_effect = True),

        narika_hair = Item(name = "Narika的一绺头发", target = 'MC', type = IT_Story, pic = 'hair.webp', template = False, rank = 1, rarity = "S", price = 0, description = "一绺粉红色的头发，属于国术神童Narika Shihoudou。", hidden_effect = True)

        blue_ribbon = Item(name = "Homura的丝带", target = 'MC', type = IT_Story, pic = 'blue ribbon.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="necklace", description = "Henso女士给你的一条丝带。把它系在城市{b}广场{/b}的一个柱子上，让她知道你想见她。", hidden_effect = True)

        # TEMPLATE ITEMS #

        template_items =   [
                            Item(name = '偷来的内衣', target = 'MC', type = IT_Misc, pic = 'Stolen underwear.webp', template = True, rank = 1, max_rank = 5, rarity = "S", charges = 1, price = 500, effects = (Effect('gain', 'prestige', 2), ), description = "所以你对这些东西感兴趣，是吗？"),
                            Item(name = '浪漫小说', target = 'gift', type = IT_Gift, pic = 'Romantic novel.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'cute', 1), Effect('gift', 'book', 1), ), description =  "一个穿着闪亮盔甲的骑士。一位公主。一个水管工。通常的情况……", hidden_effect = True),
                            Item(name = '色情手册', target = 'gift', type = IT_Gift, pic = 'Erotic manual.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'erotica', 1), Effect('gift', 'book', 1), ), description =  "50个只有使用黑魔法才能实现的姿势。", hidden_effect = True),
                            Item(name = '金箔书籍', target = 'gift', type = IT_Gift, pic = 'Goldleaf book.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'precious', 1), Effect('gift', 'book', 1), ), description =  "它说的是什么？谁在乎呢！？它是闪亮的。", hidden_effect = True),
                            Item(name = '魔法调酒之书', target = 'gift', type = IT_Gift, pic = 'Book of magical cocktails.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'drinks', 1), Effect('gift', 'book', 1), ), description =  "警告：饮用这些药水可能会导致丧失记忆。还有尊严。", hidden_effect = True),
                            Item(name = '宠物', target = 'gift', type = IT_Gift, pic = 'Pet.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'cute', 1), Effect('gift', 'precious', 1), ), description =  "他不是很可爱吗？只要他不把你的手咬下来……", hidden_effect = True),
                            Item(name = '丝绸睡衣', target = 'gift', type = IT_Gift, pic = 'Silky nighties.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'cute', 1), Effect('gift', 'erotica', 1), ), description =  "光滑而又性感。", hidden_effect = True),
                            Item(name = '樱花清酒', target = 'gift', type = IT_Gift, pic = 'Sakura liquor.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'cute', 1), Effect('gift', 'drinks', 1), ), description =  "一种由蒸馏花瓣制成的微妙饮料。", hidden_effect = True),
                            Item(name = '性感高跟鞋', target = 'gift', type = IT_Gift, pic = 'Sexy high heels.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'erotica', 1), Effect('gift', 'precious', 1), ), description =  "有些女人会为了得到这双鞋而杀人。事实上，它们有点血迹斑斑。", hidden_effect = True),
                            Item(name = '香槟', target = 'gift', type = IT_Gift, pic = 'Champagne.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'drinks', 1), Effect('gift', 'precious', 1), ), description =  "“暴发户”：一种烈性饮料；也是一种声明，即你能买得起它。", hidden_effect = True),
                            Item(name = '催情剂', target = 'gift', type = IT_Gift, pic = 'Aphrodisiac.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'drinks', 1), Effect('gift', 'erotica', 1), ), description =  "肚子里有火，裤子里也有火……", hidden_effect = True),
                            Item(name = '漂亮的戒指', target = 'girl', type = IT_Ring, pic = 'Pretty ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 150, effects = (Effect('change', 'beauty', 5), ), ),
                            Item(name = '青铜戒指', target = 'girl', type = IT_Ring, pic = 'Bronze ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 150, effects = (Effect('change', 'body', 5), ), ),
                            Item(name = 'Zanic戒指', target = 'girl', type = IT_Ring, pic = 'Zanic ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 150, effects = (Effect('change', 'charm', 5), ), ),
                            Item(name = '白银戒指', target = 'girl', type = IT_Ring, pic = 'Silver ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 150, effects = (Effect('change', 'refinement', 5), ), ),
                            Item(name = '黄金戒指', target = 'girl', type = IT_Ring, pic = 'Gold ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'libido', 5), ), ),
                            Item(name = '玛瑙戒指', target = 'girl', type = IT_Ring, pic = 'Marine ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'sensitivity', 5), ), ),
                            Item(name = '刚铁戒指', target = 'girl', type = IT_Ring, pic = 'Iron ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 375, effects = (Effect('change', 'obedience', 5), ), ),
                            Item(name = '木头戒指', target = 'girl', type = IT_Ring, pic = 'Wooden ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'constitution', 5), ), ),
                            Item(name = '蓝色丝带', target = 'girl', type = IT_Necklace, pic = 'Blue ribbon.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 100, effects = (Effect('boost', 'beauty gains', 0.1), ), ),
                            Item(name = '珍珠项链', target = 'girl', type = IT_Necklace, pic = 'Pearl necklace.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 100, effects = (Effect('boost', 'body gains', 0.1), ), ),
                            Item(name = '月亮项链', target = 'girl', type = IT_Necklace, pic = 'Moon necklace.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 100, effects = (Effect('boost', 'charm gains', 0.1), ), ),
                            Item(name = '象牙项链', target = 'girl', type = IT_Necklace, pic = 'Ivory necklace.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 100, effects = (Effect('boost', 'refinement gains', 0.1), ), ),
                            Item(name = '项圈', target = 'girl', type = IT_Necklace, pic = 'Choker necklace.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('boost', 'libido gains', 0.1), ), ),
                            Item(name = '狗项圈', target = 'girl', type = IT_Necklace, pic = 'Dog collar.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('boost', 'obedience gains', 0.1), ), ),
                            Item(name = '白银项链', target = 'girl', type = IT_Necklace, pic = 'Silver chain.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('boost', 'sensitivity gains', 0.1), ), ),
                            Item(name = '匕首项链', target = 'girl', type = IT_Necklace, pic = 'Dagger necklace.webp', template = True, rank = 1, max_rank = 5, rarity = 2, price = 250, effects = (Effect('boost', 'constitution gains', 0.1), ), ),
                            Item(name = '金币袋子', target = 'girl', type = IT_Misc, pic = 'Gold bag.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 600, effects = (Effect('special', 'level', 5), ), description =  "瞬间提升等级。明智地使用它……", adjectives = "ring"),
                            Item(name = '珠宝袋子', target = 'girl', type = IT_Misc, pic = 'Jewel bag.webp', template = True, rank = 1, max_rank = 5, rarity = 3, charges = 1, price = 500, effects = (Effect('gain', 'skill points', 5), ), description =  "获得额外的技能点。"),
                            Item(name = '知识卷轴', target = 'girl', type = IT_Misc, pic = 'Knowledge scroll.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 400, effects = (Effect('gain', 'xp', 50), ), description =  "获得免费经验。", adjectives = "scroll"),
                            Item(name = '医疗包', target = 'girl', type = IT_Misc, pic = 'Medicine bag.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 250, effects = (Effect('instant', 'heal', 2), ), description =  ""),
                            Item(name = '补品', target = 'girl', type = IT_Misc, pic = 'Tonic.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 75, effects = (Effect('gain', 'energy', 20), ), description =  ""),
                            Item(name = '葡萄酒', target = 'girl', type = IT_Misc, pic = 'Wine.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 75, effects = (Effect('gain', 'mood', 10), ), description =  ""),
                            Item(name = '苹果', target = 'girl', type = IT_Food, pic = 'Apple.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 50, effects = (Effect('change', 'beauty', 5, duration=10), Effect('gain', 'heal', 1, 0.5)), description =  "每天一个苹果能让医生远离你。"),
                            Item(name = '香梨', target = 'girl', type = IT_Food, pic = 'Pear.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 50, effects = (Effect('change', 'body', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '蜜桃', target = 'girl', type = IT_Food, pic = 'Peach.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 50, effects = (Effect('change', 'charm', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '葡萄', target = 'girl', type = IT_Food, pic = 'Grapes.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 50, effects = (Effect('change', 'refinement', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '香肠', target = 'girl', type = IT_Food, pic = 'Sausage.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 75, effects = (Effect('change', 'libido', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '奶酪', target = 'girl', type = IT_Food, pic = 'Cheese.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 75, effects = (Effect('change', 'sensitivity', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '鸡肉', target = 'girl', type = IT_Food, pic = 'Chicken.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 90, effects = (Effect('change', 'obedience', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '烤肉', target = 'girl', type = IT_Food, pic = 'Roastbeef.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 75, effects = (Effect('change', 'constitution', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = '迷魂药', target = 'girl', type = IT_Misc, pic = 'Love potion.webp', template = True, rank = 1, max_rank = 6, rarity = 2, charges = 1, price = 100, effects = (Effect('gain', 'love', 2.5), ), description = "谁说金钱买不到爱情？"),
                            Item(name = '怪物汁液', target = 'girl', type = IT_Misc, pic = 'Monster juice.webp', template = True, rank = 1, max_rank = 6, rarity = 2, charges = 1, price = 60, effects = (Effect('gain', 'fear', 2.5), ), description = "你不会想知道这是从哪个怪物的身体部位来的。"),
                            Item(name = '粉红内裤', target = 'girl', type = IT_Accessory, pic = 'Pink panties.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 125, effects = (Effect('change', 'beauty', 5), ), ),
                            Item(name = '紧身短裤', target = 'girl', type = IT_Accessory, pic = 'Hot pants.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 125, effects = (Effect('change', 'body', 5), ), ),
                            Item(name = '超短裙', target = 'girl', type = IT_Accessory, pic = 'Lowcut panties.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 125, effects = (Effect('change', 'charm', 5), ), ),
                            Item(name = '蕾丝内裤', target = 'girl', type = IT_Accessory, pic = 'Lace panties.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 125, effects = (Effect('change', 'refinement', 5), ), ),
                            Item(name = '情趣内裤', target = 'girl', type = IT_Accessory, pic = 'Sexy panties.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'libido', 5), ), ),
                            Item(name = '透明内裤', target = 'girl', type = IT_Accessory, pic = 'Seethrough panties.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'sensitivity', 5), ), ),
                            Item(name = '贞操带', target = 'girl', type = IT_Accessory, pic = 'Chastity belt.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 350, effects = (Effect('change', 'obedience', 5), ), ),
                            Item(name = '丁字裤', target = 'girl', type = IT_Accessory, pic = 'Thong.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 175, effects = (Effect('change', 'constitution', 5), ), ),
                            Item(name = '兔子制服', target = 'girl', type = IT_Dress, pic = 'Bunny suit.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'body', 5), Effect('change', 'libido', 5), ), ),
                            Item(name = '警察制服', target = 'girl', type = IT_Dress, pic = 'Guard uniform.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'charm', 5), Effect('change', 'constitution', 5), ), ),
                            Item(name = '学生制服', target = 'girl', type = IT_Dress, pic = 'School uniform.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'beauty', 5), Effect('change', 'libido', 5), ), ),
                            Item(name = '比基尼', target = 'girl', type = IT_Dress, pic = 'Bikini.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'body', 5), Effect('change', 'constitution', 5), ), ),
                            Item(name = '和服', target = 'girl', type = IT_Dress, pic = 'Kimono.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 350, effects = (Effect('change', 'refinement', 5), Effect('change', 'obedience', 5), ), ),
                            Item(name = '泳装', target = 'girl', type = IT_Dress, pic = 'Swimsuit.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'beauty', 5), Effect('change', 'sensitivity', 5), ), ),
                            Item(name = '百褶连衣裙', target = 'girl', type = IT_Dress, pic = 'Frilly dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'charm', 5), Effect('change', 'sensitivity', 5), ), ),
                            Item(name = '皮衣', target = 'girl', type = IT_Dress, pic = 'Leather dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'constitution', 5), Effect('change', 'obedience', 5), ), ),
                            Item(name = '晚礼制服', target = 'girl', type = IT_Dress, pic = 'Evening gown.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 400, effects = (Effect('change', 'beauty', 5), Effect('change', 'charm', 5), Effect('change', 'refinement', 5), Effect('change', 'body', -5), ), ),
                            Item(name = '丝绸连衣裙', target = 'girl', type = IT_Dress, pic = 'Silk dress.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 400, effects = (Effect('change', 'libido', 5), Effect('change', 'sensitivity', 5), Effect('change', 'obedience', 5), Effect('change', 'constitution', -5), ), ),
                            Item(name = '绒布制服', target = 'girl', type = IT_Dress, pic = 'Pompom uniform.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 400, effects = (Effect('change', 'beauty', 5), Effect('change', 'charm', 5), Effect('change', 'body', 5), Effect('change', 'refinement', -5), ), ),
                            Item(name = '骑士制服', target = 'girl', type = IT_Dress, pic = 'Knight uniform.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 400, effects = (Effect('change', 'body', 5), Effect('change', 'constitution', 5), Effect('change', 'obedience', 5), Effect('change', 'libido', -5), ), ),
                            Item(name = '黑鳞比基尼', target = 'girl', type = IT_Dress, pic = 'Black slavekini.webp', template = True, rank = 1, max_rank = 6, rarity = "S", price = 750, effects = (Effect('change', 'beauty', 5), Effect('change', 'body', 5), Effect('change', 'charm', 5), Effect('change', 'refinement', 5), ), ),
                            Item(name = '蓝鳞比基尼', target = 'girl', type = IT_Dress, pic = 'Blue slavekini.webp', template = True, rank = 1, max_rank = 6, rarity = "S", price = 1000, effects = (Effect('change', 'libido', 5), Effect('change', 'sensitivity', 5), Effect('change', 'obedience', 5), Effect('change', 'constitution', 5), ), ),
                            Item(name = '红鳞比基尼', target = 'girl', type = IT_Dress, pic = 'Red slavekini.webp', template = True, rank = 1, max_rank = 6, rarity = "S", price = 2000, effects = (Effect('change', 'service', 5), Effect('change', 'sex', 5), Effect('change', 'anal', 5), Effect('change', 'fetish', 5), ), ),
                            Item(name = '吊带连衣裙', target = 'girl', type = IT_Dress, pic = 'Sunny dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 300, effects = (Effect('change', 'beauty', 10), ), ),
                            Item(name = '暴露制服', target = 'girl', type = IT_Dress, pic = 'Revealing dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 300, effects = (Effect('change', 'body', 10), ), ),
                            Item(name = '奇异制服', target = 'girl', type = IT_Dress, pic = 'Exotic dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 300, effects = (Effect('change', 'charm', 10), ), ),
                            Item(name = '祭司长袍', target = 'girl', type = IT_Dress, pic = 'Priestess robe.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 300, effects = (Effect('change', 'refinement', 10), ), ),
                            Item(name = '淫荡裙子', target = 'girl', type = IT_Dress, pic = 'Slutty dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 425, effects = (Effect('change', 'libido', 10), ), ),
                            Item(name = '透明连衣裙', target = 'girl', type = IT_Dress, pic = 'Seethrough dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 425, effects = (Effect('change', 'sensitivity', 10), ), ),
                            Item(name = '女仆制服', target = 'girl', type = IT_Dress, pic = 'Maid uniform.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 500, effects = (Effect('change', 'obedience', 10), ), ),
                            Item(name = '体操制服', target = 'girl', type = IT_Dress, pic = 'Gym uniform.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 425, effects = (Effect('change', 'constitution', 10), ), ),
                            Item(name = '祖母绿戒指', target = 'girl', type = IT_Ring, pic = 'Emerald ring.webp', template = True, rank = 1, max_rank = 5, rarity = 3, price = 500, effects = (Effect('change', 'service', 5), ), ),
                            Item(name = '红宝石戒指', target = 'girl', type = IT_Ring, pic = 'Ruby ring.webp', template = True, rank = 1, max_rank = 5, rarity = 3, price = 500, effects = (Effect('change', 'sex', 5), ), ),
                            Item(name = '琥珀色戒指', target = 'girl', type = IT_Ring, pic = 'Amber ring.webp', template = True, rank = 1, max_rank = 5, rarity = 3, price = 500, effects = (Effect('change', 'anal', 5), ), ),
                            Item(name = '蓝宝石戒指', target = 'girl', type = IT_Ring, pic = 'sapphire ring.webp', template = True, rank = 1, max_rank = 5, rarity = 3, price = 500, effects = (Effect('change', 'fetish', 5), ), ),
                            Item(name = '调酒之道卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of bartending.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'waitress jp', 10), ), adjectives = "scroll"),
                            Item(name = '旋转法门卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of whirling.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'dancer jp', 10), ), adjectives = "scroll"),
                            Item(name = '按摩技巧卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of rubbing.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'masseuse jp', 10), ), adjectives = "scroll"),
                            Item(name = '礼仪之道卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of etiquette.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'geisha jp', 10), ), adjectives = "scroll"),
                            Item(name = '推油秘法卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of Onan.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'service jp', 10), ), adjectives = "scroll"),
                            Item(name = '厄洛斯之卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of Eros.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'sex jp', 10), ), adjectives = "scroll"),
                            Item(name = '索多玛之卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of Sodom.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'anal jp', 10), ), adjectives = "scroll"),
                            Item(name = '蛾摩拉之卷轴', target = 'girl', type = IT_Misc, pic = 'Scroll of Gomorrah.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'fetish jp', 10), ), adjectives = "scroll"),
                            Item(name = '精灵制造的阴茎增大器', target = 'minion', type = IT_Misc, pic = 'enlarger.webp', template = True, rank = 1, max_rank = 5, rarity = "M", charges = 1, price = 120, effects = (Effect('gain', 'stallion xp', 10), ), description = "那不是我的。这种东西不是我的囊中之物，宝贝！"),
                            Item(name = '机器润滑油', target = 'minion', type = IT_Misc, pic = 'lubricant.webp', template = True, rank = 1, max_rank = 5, rarity = "M", charges = 1, price = 120, effects = (Effect('gain', 'machine xp', 10), ), description = "润滑脂是好东西。"),
                            Item(name = '奇怪的饲料', target = 'minion', type = IT_Misc, pic = 'feed.webp', template = True, rank = 1, max_rank = 5, rarity = "M", charges = 1, price = 120, effects = (Effect('gain', 'beast xp', 10), ), description = "喜欢他们抓着你的腿，上下摩擦自己吗？因为这个饲料肯定会让他们想这么做。"),
                            Item(name = '怪物的饼干', target = 'minion', type = IT_Misc, pic = 'cookie.webp', template = True, rank = 1, max_rank = 5, rarity = "M", charges = 1, price = 120, effects = (Effect('gain', 'monster xp', 10), ), description = "C是指公鸡的意思。（原名cookie  C is for cock-y.）", adjectives = "food"),
                            ]

        all_items += generate_template_items(template_items)

        item_dict = {it.name : it for it in all_items}

    return


## FURNITURE ##

label init_furniture():

    python:
        all_furniture = [
            Furniture('Cardboard', type='Decoration', pic='Cardboard box.webp', rank=0, chapter=0, cost=[], duration=0, effects=[Effect("allow", "beggars", 1, scope="brothel")], ),
            Furniture('Beer keg', type='Decoration', pic='Beer keg.webp', rank=0, chapter=0, cost=[], duration=0, effects=[Effect("allow", "thugs", 1, scope="brothel")], ),
            Furniture('Basic painting', type='Decoration', pic='Decorative painting.webp', rank=2, chapter=2, cost=[('wood', 1), ('dye', 1), ('leather', 1), ], duration=0, effects=[Effect("allow", "laborers", 1, scope="brothel")], ),
            Furniture('Model boat', type='Decoration', pic='Model boat.webp', rank=2, chapter=2, cost=[('wood', 2), ('dye', 2), ('leather', 2), ], duration=1, effects=[Effect("allow", "sailors", 1, scope="brothel")], ),
            Furniture('Hearth', type='Decoration', pic='Hearth.webp', rank=2, chapter=2, cost=[('wood', 4), ('leather', 4), ], duration=2, effects=[Effect("allow", "commoners", 1, scope="brothel")], ),
            Furniture('Fine painting', type='Decoration', pic='Fantasy painting.webp', rank=2, chapter=3, cost=[('wood', 4), ('dye', 12), ('leather', 4), ], duration=3, effects=[Effect("allow", "craftsmen", 1, scope="brothel")], ),
            Furniture('Wine cases', type='Decoration', pic='Wine cases.webp', rank=3, chapter=4, cost=[('wood', 6), ('dye', 6), ('silk', 4), ], duration=4, effects=[Effect("allow", "bourgeois", 1, scope="brothel")], ),
            Furniture('Model airship', type='Decoration', pic='Model airship.webp', rank=3, chapter=4, cost=[('dye', 14), ('silk', 4), ('ore', 4), ], duration=5, effects=[Effect("allow", "guild members", 1, scope="brothel")], ),
            Furniture('Master painting', type='Decoration', pic='Erotic painting.webp', rank=3, chapter=5, cost=[('wood', 6), ('dye', 6), ('silk', 8), ('ore', 4), ], duration=6, effects=[Effect("allow", "patricians", 1, scope="brothel")], ),
            Furniture('Sparkling fountain', type='Decoration', pic='Sparkling fountain.webp', rank=4, chapter=6, cost=[('leather', 6), ('marble', 12), ('ore', 4), ], duration=7, effects=[Effect("allow", "aristocrats", 1, scope="brothel")], ),
            Furniture('Armorial bearings', type='Decoration', pic='Armorial bearings.webp', rank=4, chapter=6, cost=[('dye', 6), ('marble', 6), ('silk', 12), ('diamond', 1), ], duration=8, effects=[Effect("allow", "nobles", 1, scope="brothel")], ),
            Furniture('Chapel', type='Decoration', pic='Chapel.webp', rank=5, chapter=7, cost=[('marble', 8), ('silk', 8), ('ore', 4), ('diamond', 2), ], duration=9, effects=[Effect("allow", "royals", 1, scope="brothel")], ),
            Furniture('Small bar counter', type='Furnishing', pic='bar counter1.webp', rank=2, chapter=2, cost=[('wood', 4), ('leather', 4), ], duration=1, effects=[Effect("allow", "waitress preference", 1, scope="brothel")], ),
            Furniture('Polished bar counter', type='Furnishing', pic='bar counter2.webp', rank=3, chapter=4, cost=[('wood', 4), ('dye', 4), ('leather', 4), ('marble', 4), ('ore', 2), ], duration=3, upgrade='Small bar counter', effects=[Effect("allow", "waitress preference", 2, scope="brothel")], ),
            Furniture('Varnished bar counter', type='Furnishing', pic='bar counter3.webp', rank=4, chapter=6, cost=[('wood', 6), ('marble', 6), ('ore', 12), ], duration=5, upgrade='Polished bar counter', effects=[Effect("allow", "waitress preference", 3, scope="brothel")], ),
            Furniture('Lacquered bar counter', type='Furnishing', pic='bar counter4.webp', rank=5, chapter=7, cost=[('marble', 5), ('ore', 10), ], duration=7, upgrade='Varnished bar counter', effects=[Effect("allow", "waitress preference", 5, scope="brothel")], ),
            Furniture('Small washroom', type='Furnishing', pic='washroom1.webp', rank=2, chapter=2, cost=[('dye', 8), ], duration=1, effects=[Effect("allow", "masseuse preference", 1, scope="brothel")], ),
            Furniture('Clean washroom', type='Furnishing', pic='washroom2.webp', rank=3, chapter=4, cost=[('wood', 4), ('dye', 4), ('leather', 4), ('marble', 6), ], duration=3, upgrade='Small washroom', effects=[Effect("allow", "masseuse preference", 2, scope="brothel")], ),
            Furniture('Hot washroom', type='Furnishing', pic='washroom3.webp', rank=4, chapter=6, cost=[('wood', 6), ('marble', 12), ('silk', 6), ], duration=5, upgrade='Clean washroom', effects=[Effect("allow", "masseuse preference", 3, scope="brothel")], ),
            Furniture('Luxurious washroom', type='Furnishing', pic='washroom4.webp', rank=5, chapter=7, cost=[('marble', 10), ('silk', 5), ], duration=7, upgrade='Hot washroom', effects=[Effect("allow", "masseuse preference", 5, scope="brothel")], ),
            Furniture('Small stage', type='Furnishing', pic='stage1.webp', rank=2, chapter=2, cost=[('wood', 4), ('dye', 4), ], duration=1, effects=[Effect("allow", "dancer preference", 1, scope="brothel")], ),
            Furniture('Amateur stage', type='Furnishing', pic='stage2.webp', rank=3, chapter=4, cost=[('leather', 12), ('marble', 4), ('ore', 2), ], duration=3, upgrade='Small stage', effects=[Effect("allow", "dancer preference", 2, scope="brothel")], ),
            Furniture('Theatre stage', type='Furnishing', pic='stage3.webp', rank=4, chapter=6, cost=[('leather', 6), ('marble', 6), ('silk', 12), ], duration=5, upgrade='Amateur stage', effects=[Effect("allow", "dancer preference", 3, scope="brothel")], ),
            Furniture('Opera stage', type='Furnishing', pic='stage4.webp', rank=5, chapter=7, cost=[('marble', 5), ('silk', 10), ], duration=7, upgrade='Theatre stage', effects=[Effect("allow", "dancer preference", 5, scope="brothel")], ),
            Furniture('Small tatami room', type='Furnishing', pic='tatami room1.webp', rank=2, chapter=2, cost=[('dye', 4), ('leather', 4), ], duration=1, effects=[Effect("allow", "geisha preference", 1, scope="brothel")], ),
            Furniture('Fancy tatami room', type='Furnishing', pic='tatami room2.webp', rank=3, chapter=4, cost=[('dye', 12), ('silk', 6), ], duration=3, upgrade='Small tatami room', effects=[Effect("allow", "geisha preference", 2, scope="brothel")], ),
            Furniture('Rare tatami room', type='Furnishing', pic='tatami room3.webp', rank=4, chapter=6, cost=[('dye', 6), ('silk', 12), ('ore', 6), ], duration=5, upgrade='Fancy tatami room', effects=[Effect("allow", "geisha preference", 3, scope="brothel")], ),
            Furniture('Unique tatami room', type='Furnishing', pic='tatami room4.webp', rank=5, chapter=7, cost=[('silk', 10), ('ore', 5), ], duration=7, upgrade='Rare tatami room', effects=[Effect("allow", "geisha preference", 5, scope="brothel")], ),
            Furniture('Candy dispenser', type='Furnishing', pic='dispenser1.webp', rank=2, chapter=3, cost=[('wood', 6), ('dye', 4), ('leather', 6), ], duration=2, effects=[Effect("allow", "service preference", 1, scope="brothel")], ),
            Furniture('Ice cream dispenser', type='Furnishing', pic='dispenser2.webp', rank=3, chapter=5, cost=[('wood', 10), ('leather', 5), ('marble', 8), ('ore', 10), ], duration=4, upgrade='Candy dispenser', effects=[Effect("allow", "service preference", 2, scope="brothel")], ),
            Furniture('Lollipop dispenser', type='Furnishing', pic='dispenser3.webp', rank=4, chapter=6, cost=[('leather', 6), ('marble', 8), ('ore', 12), ], duration=6, upgrade='Ice cream dispenser', effects=[Effect("allow", "service preference", 3, scope="brothel")], ),
            Furniture('Magic mint dispenser', type='Furnishing', pic='dispenser4.webp', rank=5, chapter=7, cost=[('marble', 8), ('ore', 10), ], duration=8, upgrade='Lollipop dispenser', effects=[Effect("allow", "service preference", 5, scope="brothel")], ),
            Furniture('Small erotica collection', type='Furnishing', pic='shelves1.webp', rank=2, chapter=3, cost=[('wood', 6), ('dye', 6), ('leather', 4), ], duration=2, effects=[Effect("allow", "sex preference", 1, scope="brothel")], ),
            Furniture('Curious erotica collection', type='Furnishing', pic='shelves2.webp', rank=3, chapter=5, cost=[('wood', 5), ('leather', 10), ('marble', 10), ('ore', 8), ], duration=4, upgrade='Small erotica collection', effects=[Effect("allow", "sex preference", 2, scope="brothel")], ),
            Furniture('Mysterious erotica collection', type='Furnishing', pic='shelves3.webp', rank=4, chapter=6, cost=[('wood', 6), ('marble', 12), ('ore', 8), ], duration=6, upgrade='Curious erotica collection', effects=[Effect("allow", "sex preference", 3, scope="brothel")], ),
            Furniture('Mindblowing erotica collection', type='Furnishing', pic='shelves4.webp', rank=5, chapter=7, cost=[('marble', 10), ('ore', 8), ], duration=8, upgrade='Mysterious erotica collection', effects=[Effect("allow", "sex preference", 5, scope="brothel")], ),
            Furniture('Painted venus', type='Furnishing', pic='venus1.webp', rank=2, chapter=3, cost=[('dye', 16), ], duration=2, effects=[Effect("allow", "anal preference", 1, scope="brothel")], ),
            Furniture('Marble venus', type='Furnishing', pic='venus2.webp', rank=3, chapter=5, cost=[('dye', 15), ('marble', 10), ('silk', 8), ], duration=4, upgrade='Painted venus', effects=[Effect("allow", "anal preference", 2, scope="brothel")], ),
            Furniture('Veiled venus', type='Furnishing', pic='venus3.webp', rank=4, chapter=6, cost=[('dye', 6), ('marble', 8), ('silk', 12), ], duration=6, upgrade='Marble venus', effects=[Effect("allow", "anal preference", 3, scope="brothel")], ),
            Furniture('Ardent venus', type='Furnishing', pic='venus4.webp', rank=5, chapter=7, cost=[('marble', 10), ('silk', 8), ], duration=8, upgrade='Veiled venus', effects=[Effect("allow", "anal preference", 5, scope="brothel")], ),
            Furniture('Toy wooden horse', type='Furnishing', pic='woodhorse1.webp', rank=2, chapter=3, cost=[('wood', 6), ('dye', 2), ('leather', 8), ], duration=2, effects=[Effect("allow", "fetish preference", 1, scope="brothel")], ),
            Furniture('Spiked wooden horse', type='Furnishing', pic='woodhorse2.webp', rank=3, chapter=5, cost=[('wood', 15), ('silk', 10), ('ore', 8), ], duration=4, upgrade='Toy wooden horse', effects=[Effect("allow", "fetish preference", 2, scope="brothel")], ),
            Furniture('Polished wooden horse', type='Furnishing', pic='woodhorse3.webp', rank=4, chapter=6, cost=[('wood', 6), ('silk', 12), ('ore', 8), ], duration=6, upgrade='Spiked wooden horse', effects=[Effect("allow", "fetish preference", 3, scope="brothel")], ),
            Furniture('Mobile wooden horse', type='Furnishing', pic='woodhorse4.webp', rank=5, chapter=7, cost=[('silk', 8), ('ore', 10), ], duration=8, upgrade='Polished wooden horse', effects=[Effect("allow", "fetish preference", 5, scope="brothel")], ),
            Furniture('Basic outfit', type='Utility', pic='Basic outfit.webp', rank=0, chapter=0, cost=[], duration=0, effects=[Effect("special", "advertising power", 1, scope="brothel")], ),
            Furniture('Shepherd outfit', type='Utility', pic='Shepherd outfit.webp', rank=2, chapter=2, cost=[('wood', 2), ('leather', 6), ], duration=0, upgrade='Basic outfit', effects=[Effect("special", "advertising power", 2, scope="brothel")], ),
            Furniture('Priestess outfit', type='Utility', pic='Priestess outfit.webp', rank=2, chapter=3, cost=[('dye', 8), ('leather', 12), ], duration=1, upgrade='Shepherd outfit', effects=[Effect("special", "advertising power", 3, scope="brothel")], ),
            Furniture('Skimpy outfit', type='Utility', pic='Skimpy outfit.webp', rank=3, chapter=4, cost=[('dye', 8), ('leather', 4), ('silk', 4), ], duration=2, upgrade='Priestess outfit', effects=[Effect("special", "advertising power", 4, scope="brothel")], ),
            Furniture('Slutty outfit', type='Utility', pic='Slutty outfit.webp', rank=3, chapter=5, cost=[('dye', 10), ('leather', 2), ('silk', 10), ('ore', 4), ], duration=2, upgrade='Skimpy outfit', effects=[Effect("special", "advertising power", 5, scope="brothel")], ),
            Furniture('Kimono outfit', type='Utility', pic='Kimono outfit.webp', rank=4, chapter=6, cost=[('dye', 6), ('silk', 18), ], duration=3, upgrade='Slutty outfit', effects=[Effect("special", "advertising power", 6, scope="brothel")], ),
            Furniture('Idol outfit', type='Utility', pic='Idol outfit.webp', rank=5, chapter=7, cost=[('silk', 12), ('ore', 4), ], duration=3, upgrade='Kimono outfit', effects=[Effect("special", "advertising power", 7, scope="brothel")], ),
            Furniture('Basic door', type='Utility', pic='Basic door.webp', rank=0, chapter=0, cost=[], duration=0, effects=[Effect("boost", "security", 0, scope="brothel")], ),
            Furniture('Fence', type='Utility', pic='Fence.webp', rank=2, chapter=2, cost=[('wood', 4), ('leather', 4), ], duration=0, upgrade='Basic door', effects=[Effect("boost", "security", 0.1, scope="brothel")], ),
            Furniture('Small traps', type='Utility', pic='Small traps.webp', rank=2, chapter=3, cost=[('leather', 20), ], duration=1, upgrade='Fence', effects=[Effect("boost", "security", 0.2, scope="brothel")], ),
            Furniture('Large traps', type='Utility', pic='Large traps.webp', rank=3, chapter=4, cost=[('wood', 8), ('leather', 4), ('ore', 4), ], duration=2, upgrade='Small traps', effects=[Effect("boost", "security", 0.3, scope="brothel")], ),
            Furniture('Alarm system', type='Utility', pic='Alarm system.webp', rank=3, chapter=5, cost=[('leather', 12), ('marble', 4), ('ore', 10), ], duration=2, upgrade='Large traps', effects=[Effect("boost", "security", 0.4, scope="brothel")], ),
            Furniture('Explosive traps', type='Utility', pic='Explosive traps.webp', rank=4, chapter=6, cost=[('leather', 6), ('ore', 18), ], duration=3, upgrade='Alarm system', effects=[Effect("boost", "security", 0.5, scope="brothel")], ),
            Furniture('Zap traps', type='Utility', pic='Zap traps.webp', rank=5, chapter=7, cost=[('marble', 4), ('ore', 12), ], duration=3, upgrade='Explosive traps', effects=[Effect("boost", "security", 0.6, scope="brothel")], ),
            Furniture('Basic broom', type='Utility', pic='Broom.webp', rank=0, chapter=0, cost=[], duration=0, effects=[Effect("boost", "maintenance", 0, scope="brothel")], ),
            Furniture('Buckets', type='Utility', pic='Buckets.webp', rank=2, chapter=2, cost=[('wood', 2), ('dye', 4), ('leather', 2), ], duration=0, upgrade='Basic broom', effects=[Effect("boost", "maintenance", 0.25, scope="brothel")], ),
            Furniture('Wheelbarrow', type='Utility', pic='Wheelbarrow.webp', rank=3, chapter=4, cost=[('wood', 4), ('dye', 4), ('leather', 4), ('ore', 4), ], duration=1, upgrade='Buckets', effects=[Effect("boost", "maintenance", 0.5, scope="brothel")], ),
            Furniture('Steam cart', type='Utility', pic='Steam cart.webp', rank=4, chapter=6, cost=[('leather', 6), ('marble', 6), ('silk', 6), ('ore', 6), ], duration=2, upgrade='Wheelbarrow', effects=[Effect("boost", "maintenance", 1, scope="brothel")], ),
            Furniture('Robot maid', type='Utility', pic='Robot maid.webp', rank=5, chapter=7, cost=[('silk', 6), ('ore', 10), ], duration=3, upgrade='Steam cart', effects=[Effect("boost", "maintenance", 1.5, scope="brothel")], ),
            Furniture('Wood statue', type='Decoration', pic='Bronze statue.webp', rank=2, chapter=2, cost=[('wood', 4), ('dye', 4), ], duration=1, effects=[Effect("change", "brothel reputation", 6, scope="brothel")], ),
            Furniture('Marble statue', type='Decoration', pic='Silver statue.webp', rank=3, chapter=4, cost=[('dye', 15), ('marble', 6), ], duration=2, upgrade='Wood statue', effects=[Effect("change", "brothel reputation", 12, scope="brothel")], ),
            Furniture('Gold statue', type='Decoration', pic='Gold statue.webp', rank=4, chapter=6, cost=[('dye', 6), ('ore', 20), ], duration=3, upgrade='Marble statue', effects=[Effect("change", "brothel reputation", 18, scope="brothel")], ),
            Furniture('Platinum statue', type='Decoration', pic='Platinum statue.webp', rank=5, chapter=7, cost=[('ore', 20), ('diamond', 1), ], duration=4, upgrade='Gold statue', effects=[Effect("change", "brothel reputation", 24, scope="brothel")], ),
            Furniture('Simple safe', type='Utility', pic='safe1.webp', rank=2, chapter=2, cost=[('wood', 4), ('dye', 2), ('leather', 4), ], duration=3, effects=[Effect("special", "safe", 3000, scope="brothel")]),
            Furniture('Locked safe', type='Utility', pic='safe2.webp', rank=3, chapter=4, cost=[('wood', 5), ('leather', 10), ('ore', 6), ], duration=5, upgrade='Simple safe', effects=[Effect("special", "safe", 6000, scope="brothel")]),
            Furniture('Secure safe', type='Utility', pic='safe3.webp', rank=4, chapter=6, cost=[('wood', 6), ('marble', 8), ('ore', 12), ('diamond', 1), ], duration=7, upgrade='Locked safe', effects=[Effect("special", "safe", 10000, scope="brothel")]),
            Furniture('Unbreakable safe', type='Utility', pic='safe4.webp', rank=5, chapter=7, cost=[('marble', 10), ('ore', 10), ('diamond', 2), ], duration=9, upgrade='Secure safe', effects=[Effect("special", "safe", 20000, scope="brothel")]),
            Furniture('Glass window', type='Windows', pic='glass1.webp', rank=2, chapter=3, cost=[('wood', 5), ('dye', 5), ('leather', 5), ], duration=3, effects=[Effect("boost", "naked preference increase", 0.25, scope="brothel")], ),
            Furniture('Persian window', type='Windows', pic='oriental1.webp', rank=2, chapter=3, cost=[('wood', 6), ('dye', 6), ('leather', 6), ], duration=3, effects=[Effect("boost", "service preference increase", 0.25, scope="brothel")], ),
            Furniture('Mirror', type='Windows', pic='mirror1.webp', rank=2, chapter=3, cost=[('wood', 7), ('dye', 7), ('leather', 7), ], duration=4, effects=[Effect("boost", "sex preference increase", 0.25, scope="brothel")], ),
            Furniture('Red curtains', type='Windows', pic='red curtains1.webp', rank=2, chapter=3, cost=[('wood', 6), ('dye', 10), ('leather', 6), ], duration=4, effects=[Effect("boost", "anal preference increase", 0.25, scope="brothel")], ),
            Furniture('Barred window', type='Windows', pic='barred1.webp', rank=2, chapter=3, cost=[('wood', 10), ('dye', 7), ('leather', 7), ], duration=4, effects=[Effect("boost", "fetish preference increase", 0.25, scope="brothel")], ),
            Furniture('Double window', type='Windows', pic='double window1.webp', rank=2, chapter=3, cost=[('wood', 12), ('dye', 6), ('leather', 6), ], duration=5, effects=[Effect("boost", "bisexual preference increase", 0.25, scope="brothel")], ),
            Furniture('Stained glass', type='Windows', pic='stainglass1.webp', rank=2, chapter=3, cost=[('wood', 10), ('dye', 8), ('leather', 8), ], duration=5, effects=[Effect("boost", "group preference increase", 0.25, scope="brothel")], ),
            Furniture('Glass window XL', type='Windows', pic='glass2.webp', rank=3, chapter=5, cost=[('wood', 5), ('dye', 10), ('marble', 6), ('silk', 6), ], duration=5, upgrade='Glass window', effects=[Effect("boost", "naked preference increase", 0.5, scope="brothel")], ),
            Furniture('Persian window XL', type='Windows', pic='oriental2.webp', rank=3, chapter=5, cost=[('wood', 10), ('leather', 5), ('marble', 5), ('silk', 10), ], duration=5, upgrade='Persian window', effects=[Effect("boost", "service preference increase", 0.5, scope="brothel")], ),
            Furniture('Mirror XL', type='Windows', pic='mirror2.webp', rank=3, chapter=5, cost=[('dye', 5), ('leather', 10), ('silk', 5), ('ore', 12), ], duration=6, upgrade='Mirror', effects=[Effect("boost", "sex preference increase", 0.5, scope="brothel")], ),
            Furniture('Red curtains XL', type='Windows', pic='red curtains2.webp', rank=3, chapter=5, cost=[('dye', 10), ('silk', 18), ], duration=6, upgrade='Red curtains', effects=[Effect("boost", "anal preference increase", 0.5, scope="brothel")], ),
            Furniture('Barred window XL', type='Windows', pic='barred2.webp', rank=3, chapter=5, cost=[('wood', 10), ('leather', 5), ('marble', 10), ('ore', 10), ], duration=6, upgrade='Barred window', effects=[Effect("boost", "fetish preference increase", 0.5, scope="brothel")], ),
            Furniture('Double window XL', type='Windows', pic='double window2.webp', rank=3, chapter=5, cost=[('leather', 15), ('marble', 10), ('silk', 6), ('ore', 6), ], duration=7, upgrade='Double window', effects=[Effect("boost", "bisexual preference increase", 0.5, scope="brothel")], ),
            Furniture('Stained glass XL', type='Windows', pic='stainglass2.webp', rank=3, chapter=5, cost=[('dye', 15), ('marble', 5), ('silk', 5), ('ore', 14), ], duration=7, upgrade='Stained glass', effects=[Effect("boost", "group preference increase", 0.5, scope="brothel")], ),
            Furniture('Washtub', type='Comfort', pic='Washtub.webp', rank=2, chapter=2, cost=[('wood', 4), ('dye', 4), ], duration=1, effects=[Effect("boost", "energy use", -0.1, scope="brothel")], ),
            Furniture('Bathtub', type='Comfort', pic='Bathtub.webp', rank=3, chapter=4, cost=[('dye', 15), ('marble', 6), ], duration=3, upgrade='Washtub', effects=[Effect("boost", "energy use", -0.2, scope="brothel")], ),
            Furniture('Royal bathtub', type='Comfort', pic='Royal bathtub.webp', rank=4, chapter=6, cost=[('dye', 8), ('marble', 15), ('silk', 15), ('diamond', 1), ], duration=5, upgrade='Bathtub', effects=[Effect("boost", "energy use", -0.3, scope="brothel")], ),
            Furniture('Steam jacuzzi', type='Comfort', pic='Steam jacuzzi.webp', rank=5, chapter=7, cost=[('marble', 20), ('silk', 20), ('ore', 20), ('diamond', 3), ], duration=7, upgrade='Royal bathtub', effects=[Effect("boost", "energy use", -0.4, scope="brothel")], ),
            Furniture('Simple bench', type='Comfort', pic='bench1.webp', rank=2, chapter=3, cost=[('wood', 25), ], duration=2, effects=[Effect("change", "job customer capacity", 1, scope="brothel")], ),
            Furniture('Large bench', type='Comfort', pic='bench2.webp', rank=3, chapter=5, cost=[('wood', 10), ('leather', 6), ('marble', 15), ('ore', 10), ], duration=4, upgrade='Simple bench', effects=[Effect("change", "job customer capacity", 2, scope="brothel")], ),
            Furniture('Comfortable sofa', type='Comfort', pic='sofa1.webp', rank=4, chapter=6, cost=[('leather', 10), ('silk', 20), ('diamond', 1), ], duration=6, upgrade='Large bench', effects=[Effect("change", "job customer capacity", 3, scope="brothel")], ),
            Furniture('Royal sofa', type='Comfort', pic='sofa2.webp', rank=5, chapter=7, cost=[('marble', 8), ('silk', 15), ('diamond', 2), ], duration=8, upgrade='Comfortable sofa', effects=[Effect("change", "job customer capacity", 4, scope="brothel")], ),
            Furniture('Comfortable bed', type='Comfort', pic='bed1.webp', rank=3, chapter=4, cost=[('wood', 12), ('leather', 10), ('silk', 6), ], duration=5, effects=[Effect("change", "whore customer capacity", 1, scope="brothel")], ),
            Furniture('Queen size bed', type='Comfort', pic='bed2.webp', rank=5, chapter=7, cost=[('marble', 10), ('silk', 20), ('diamond', 3), ], duration=10, upgrade='Comfortable bed', effects=[Effect("change", "whore customer capacity", 2, scope="brothel")], ),
            Furniture('Shoddy Altar of Mana', type='Altars', pic='mana altar1.webp', rank=2, chapter=2, cost=[('wood', 2), ('dye', 2), ('leather', 4), ], duration=2, effects=[Effect("change", "mana", 1, scope="brothel")], ),
            Furniture('Working Altar of Mana', type='Altars', pic='mana altar2.webp', rank=3, chapter=4, cost=[('leather', 15), ('marble', 3), ('silk', 2), ('ore', 1), ], duration=4, upgrade='Shoddy Altar of Mana', effects=[Effect("change", "mana", 2, scope="brothel")], ),
            Furniture('Powerful Altar of Mana', type='Altars', pic='mana altar3.webp', rank=4, chapter=6, cost=[('dye', 6), ('marble', 4), ('silk', 8), ('ore', 4), ('diamond', 1), ], duration=6, upgrade='Working Altar of Mana', effects=[Effect("change", "mana", 3, scope="brothel")], ),
            Furniture('Devastating Altar of Mana', type='Altars', pic='mana altar4.webp', rank=5, chapter=7, cost=[('marble', 6), ('silk', 6), ('ore', 6), ('diamond', 2), ], duration=8, upgrade='Powerful Altar of Mana', effects=[Effect("change", "mana", 4, scope="brothel")], ),
            Furniture('Weapon rack', type='Utility', pic='weapon rack1.webp', rank=2, chapter=2, cost=[('dye', 2), ('leather', 4), ], duration=1, effects=[Effect("change", "defense", 1, scope="brothel")], ),
            Furniture('Weapon rack XL', type='Utility', pic='weapon rack2.webp', rank=4, chapter=6, cost=[('wood', 6), ('marble', 10), ('ore', 12), ], duration=3, upgrade='Weapon rack', effects=[Effect("change", "defense", 2, scope="brothel")], ),
            Furniture('Small dressing', type='Comfort', pic='dressing1.webp', rank=2, chapter=2, cost=[('wood', 4), ('dye', 4), ('leather', 2), ], duration=2, effects=[Effect("boost", "upkeep", -0.05, scope="brothel")], ),
            Furniture('Fancy dressing', type='Comfort', pic='dressing2.webp', rank=3, chapter=4, cost=[('wood', 10), ('dye', 5), ('marble', 2), ('silk', 6), ], duration=4, upgrade='Small dressing', effects=[Effect("boost", "upkeep", -0.1, scope="brothel")], ),
            Furniture('Noble dressing', type='Comfort', pic='dressing3.webp', rank=4, chapter=6, cost=[('leather', 6), ('marble', 20), ('silk', 5), ], duration=6, upgrade='Fancy dressing', effects=[Effect("boost", "upkeep", -0.15, scope="brothel")], ),
            Furniture('Dim lights', type='Comfort', pic='dim.webp', rank=3, chapter=4, cost=[('wood', 5), ('leather', 10), ('silk', 4), ('ore', 2), ], duration=3, effects=[Effect("boost", "customer events", 0.5, scope="brothel"), Effect("boost", "crazy", 1, scope="brothel")], can_deactivate=True),
            Furniture('Bright lights', type='Comfort', pic='bright.webp', rank=3, chapter=4, cost=[('wood', 10), ('leather', 5), ('silk', 2), ('ore', 4), ], duration=3, effects=[Effect("boost", "customer events", -1, scope="brothel"), Effect("boost", "crazy", -0.5, scope="brothel")], can_deactivate=True),
            Furniture('Simple Bookcase', type='Comfort', pic='bookshelf1.webp', rank=2, chapter=2, cost=[('wood', 4), ('dye', 4), ('leather', 4), ], duration=3, effects=[Effect("set", "all skill max", 60, scope="brothel"), Effect("set", "all skill max", 60, scope="farm")], ),
            Furniture('Engraved Bookcase', type='Comfort', pic='bookshelf2.webp', rank=3, chapter=4, cost=[('wood', 15), ('leather', 10), ('marble', 5), ('ore', 5), ], duration=6, upgrade='Simple Bookcase', effects=[Effect("set", "all skill max", 115, scope="brothel"), Effect("set", "all skill max", 115, scope="farm")], ),
            Furniture('Opulent Bookcase', type='Comfort', pic='bookshelf3.webp', rank=4, chapter=6, cost=[('wood', 6), ('marble', 15), ('silk', 5), ('ore', 5), ('diamond', 2), ], duration=9, upgrade='Engraved Bookcase', effects=[Effect("set", "all skill max", 170, scope="brothel"), Effect("set", "all skill max", 170, scope="farm")], ),
            Furniture('Lavish Bookcase', type='Comfort', pic='bookshelf4.webp', rank=5, chapter=7, cost=[('marble', 15), ('silk', 5), ('ore', 5), ('diamond', 4), ], duration=12, upgrade='Opulent Bookcase', effects=[Effect("set", "all skill max", 225, scope="brothel"), Effect("set", "all skill max", 225, scope="farm")], ),

            ]

        furniture_dict = {}
        for furn in all_furniture:
            furniture_dict[furn.name] = furn

        get_starting_furniture(1)

    return

#### END OF BK ITEMS FILE ####
