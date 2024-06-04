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

    furniture_types = [("Decoration", "Attracts new kinds of customers to your brothel"),
                       ("Furnishing", "Unlocks more options for attracting customers"),
                       ("Utility", "Help with advertising, security and maintenance"),
                       ("Comfort", "Help your girls feel more comfortable in the brothel"),
                       ("Windows", "Influences your girl's preferences"),
                       ("Altars", "Pray here and get results, for once"),
                       ("Arcane", "Helps with dark rituals"),
                       ("Gizmos", "Strange artefacts from a bygone technological age")
                       ]

## ITEMS ##

label init_items():
    python:

        # REGULAR ITEMS #

        all_items = [
                    Item(name = 'Short sword', target = 'MC', type = IT_Weapon, pic = 'Short sword.webp', rank = 1, rarity = 1, price = 250, effects = (Effect('change', 'strength', 1), ), description =  ""),
                    Item(name = 'Cutlass', target = 'MC', type = IT_Weapon, pic = 'Cutlass.webp', rank = 1, rarity = 2, price = 500, effects = (Effect('change', 'strength', 2), ), description =  "It's not a knife. That's a knife."),
                    Item(name = 'Axe', target = 'MC', type = IT_Weapon, pic = 'Axe.webp', rank = 2, rarity = 2, price = 1000, effects = (Effect('change', 'strength', 2), Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = 'Lance', target = 'MC', type = IT_Weapon, pic = 'Lance.webp', rank = 2, rarity = 2, price = 2500, effects = (Effect('change', 'strength', 3), Effect('change', 'charisma', 1), ), description =  ""),
                    Item(name = 'Long sword', target = 'MC', type = IT_Weapon, pic = 'Long sword.webp', rank = 2, rarity = 3, price = 3500, effects = (Effect('change', 'strength', 3), Effect('change', 'charisma', 1), Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = 'Rapier', target = 'MC', type = IT_Weapon, pic = 'Rapier.webp', rank = 3, rarity = 3, price = 5000, effects = (Effect('change', 'strength', 4), Effect('change', 'charisma', 2), ), description =  ""),
                    Item(name = 'Battle axe', target = 'MC', type = IT_Weapon, pic = 'Battle axe.webp', rank = 3, rarity = 3, price = 10000, effects = (Effect('change', 'strength', 5), Effect('change', 'spirit', 2), ), description =  ""),
                    Item(name = 'Warhammer', target = 'MC', type = IT_Weapon, pic = 'Warhammer.webp', rank = 3, rarity = 4, price = 17500, effects = (Effect('change', 'strength', 5), Effect('change', 'charisma', 2), Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = 'Holy sword', target = 'MC', type = IT_Weapon, pic = 'Holy sword.webp', rank = 4, rarity = "U", price = 40000, effects = (Effect('change', 'strength', 6), Effect('change', 'spirit', 3), ), description =  "This sword hums with power. The light reflects so brightly on its blade it could blind the angels themselves."),
                    Item(name = 'Demon sword', target = 'MC', type = IT_Weapon, pic = 'Demon sword.webp', rank = 4, rarity = "S", price = 100000, effects = (Effect('change', 'strength', 8), Effect('change', 'charisma', 4), Effect('change', 'spirit', -2), ), description =  "The blade pulses with the dark fury of the demon trapped inside. They say he devours every poor soul that gets slain by this blade."),
                    Item(name = 'Broom staff', target = 'MC', type = IT_Weapon, pic = 'Broom staff.webp', rank = 1, rarity = 1, price = 250, effects = (Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = 'Wooden staff', target = 'MC', type = IT_Weapon, pic = 'Wooden staff.webp', rank = 1, rarity = 2, price = 500, effects = (Effect('change', 'spirit', 2), ), description =  ""),
                    Item(name = 'Goblin staff', target = 'MC', type = IT_Weapon, pic = 'Goblin staff.webp', rank = 2, rarity = 2, price = 1000, effects = (Effect('change', 'charisma', 1), Effect('change', 'spirit', 2), ), description =  ""),
                    Item(name = 'Bronze staff', target = 'MC', type = IT_Weapon, pic = 'Bronze staff.webp', rank = 2, rarity = 2, price = 2500, effects = (Effect('change', 'strength', 1), Effect('change', 'spirit', 3), ), description =  ""),
                    Item(name = 'Wind staff', target = 'MC', type = IT_Weapon, pic = 'Wind staff.webp', rank = 2, rarity = 3, price = 3500, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 1), Effect('change', 'spirit', 3), ), description =  ""),
                    Item(name = 'Healing staff', target = 'MC', type = IT_Weapon, pic = 'Healing staff.webp', rank = 3, rarity = 3, price = 5000, effects = (Effect('change', 'charisma', 2), Effect('change', 'spirit', 4), ), description =  ""),
                    Item(name = 'Thunder staff', target = 'MC', type = IT_Weapon, pic = 'Thunder staff.webp', rank = 3, rarity = 3, price = 10000, effects = (Effect('change', 'strength', 2), Effect('change', 'spirit', 5), ), description =  ""),
                    Item(name = 'Emerald staff', target = 'MC', type = IT_Weapon, pic = 'Emerald staff.webp', rank = 3, rarity = 4, price = 17500, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 2), Effect('change', 'spirit', 5), ), description =  ""),
                    Item(name = 'Crystal staff', target = 'MC', type = IT_Weapon, pic = 'Crystal staff.webp', rank = 4, rarity = 4, price = 40000, effects = (Effect('change', 'strength', 3), Effect('change', 'spirit', 6), ), description =  ""),
                    Item(name = 'Angel staff', target = 'MC', type = IT_Weapon, pic = 'Angel staff.webp', rank = 4, rarity = 5, price = 100000, effects = (Effect('change', 'charisma', 2), Effect('change', 'spirit', 8), ), description =  ""),
                    Item(name = 'Throwing knife', target = 'MC', type = IT_Weapon, pic = 'Throwing knife.webp', rank = 1, rarity = 1, price = 250, effects = (Effect('change', 'charisma', 1), ), description =  ""),
                    Item(name = 'Throwing axe', target = 'MC', type = IT_Weapon, pic = 'Throwing axe.webp', rank = 1, rarity = 2, price = 500, effects = (Effect('change', 'charisma', 2), ), description =  ""),
                    Item(name = 'Bow', target = 'MC', type = IT_Weapon, pic = 'Bow.webp', rank = 2, rarity = 2, price = 1000, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 2), ), description =  ""),
                    Item(name = 'Ornate bow', target = 'MC', type = IT_Weapon, pic = 'Ornate bow.webp', rank = 2, rarity = 2, price = 2500, effects = (Effect('change', 'charisma', 3), Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = 'Flintlock', target = 'MC', type = IT_Weapon, pic = 'Flintlock.webp', rank = 2, rarity = 3, price = 3500, effects = (Effect('change', 'strength', 2), Effect('change', 'charisma', 3), ), description =  ""),
                    Item(name = 'Crossbow', target = 'MC', type = IT_Weapon, pic = 'Crossbow.webp', rank = 3, rarity = 3, price = 5000, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 4), Effect('change', 'spirit', 1), ), description =  ""),
                    Item(name = 'Repeater', target = 'MC', type = IT_Weapon, pic = 'Repeater.webp', rank = 3, rarity = 3, price = 10000, effects = (Effect('change', 'strength', 2), Effect('change', 'charisma', 5), ), description =  ""),
                    Item(name = 'Blunderbuss', target = 'MC', type = IT_Weapon, pic = 'Blunderbuss.webp', rank = 3, rarity = 4, price = 17500, effects = (Effect('change', 'strength', 3), Effect('change', 'charisma', 5), ), description = "This. Is. My boomstick!"),
                    Item(name = 'Holy handgrenade', target = 'MC', type = IT_Weapon, pic = 'Holy handgrenade.webp', rank = 4, rarity = 4, price = 40000, effects = (Effect('change', 'charisma', 6), Effect('change', 'spirit', 3), ), description =  ""),
                    Item(name = 'Death dispenser', target = 'MC', type = IT_Weapon, pic = 'Death dispenser.webp', rank = 4, rarity = 5, price = 100000, effects = (Effect('change', 'strength', 4), Effect('change', 'charisma', 8), Effect('change', 'spirit', -2), ), description =  ""),
                    Item(name = 'Arios amulet', target = 'MC', type = IT_Necklace, pic = 'Arios amulet.webp', rank = 1, rarity = "U", price = 25000, effects = (), description = "Unique reward for completing the Arios knight quest."),
                    Item(name = 'Shalia talisman', target = 'MC', type = IT_Necklace, pic = 'Shalia talisman.webp', rank = 1, rarity = "U", price = 25000, effects = (), description = "Unique reward for completing the Shalia shadow quest."),
                    Item(name = 'Merchant sigil', target = 'MC', type = IT_Necklace, pic = 'Merchant sigil.webp', rank = 1, rarity = "U", price = 25000, effects = (), description = "Unique reward for completing the guild of merchants quest."),
                    Item(name = 'Fur boots', target = 'MC', type = IT_Accessory, pic = 'Fur boots.webp', rank = 1, rarity = 1, price = 500, effects = (Effect('change', 'speed', 1), ), ),
                    Item(name = 'Leather boots', target = 'MC', type = IT_Accessory, pic = 'Leather boots.webp', rank = 1, rarity = 2, price = 2000, effects = (Effect('change', 'speed', 2), ), ),
                    Item(name = 'Elven boots', target = 'MC', type = IT_Accessory, pic = 'Elven boots.webp', rank = 2, rarity = 3, price = 10000, effects = (Effect('change', 'speed', 3), ), ),
                    Item(name = 'Horse', target = 'MC', type = IT_Accessory, pic = 'Horse.webp', rank = 3, rarity = 4, price = 50000, effects = (Effect('change', 'speed', 4), ), ),
                    Item(name = 'Dark horse', target = 'MC', type = IT_Accessory, pic = 'Dark horse.webp', rank = 4, rarity = 5, price = 150000, effects = (Effect('change', 'speed', 5), ), ),
                    Item(name = 'Dragon egg', target = 'MC', type = IT_Misc, pic = 'Dragon egg.webp', rank = 1, rarity = "S", charges = 1, price = 5000, effects = (Effect('gain', 'skill points', 1), ), description =  "'He was no dragon...'\nEat this at your own risk!", sound = "crunch.ogg", hidden_effect = True),
                    Item(name = 'Knuckle duster', target = 'girl', type = IT_Weapon, pic = 'Knuckle duster.webp', rank = 1, rarity = 1, price = 50, effects = (Effect('change', 'defense', 1), ), ),
                    Item(name = 'Hook', target = 'girl', type = IT_Weapon, pic = 'Hook.webp', rank = 1, rarity = 1, price = 250, effects = (Effect('change', 'defense', 2), ), ),
                    Item(name = 'Shiv', target = 'girl', type = IT_Weapon, pic = 'Shiv.webp', rank = 1, rarity = 2, price = 500, effects = (Effect('change', 'defense', 3), ), ),
                    Item(name = 'Knife', target = 'girl', type = IT_Weapon, pic = 'Knife.webp', rank = 2, rarity = 2, price = 1000, effects = (Effect('change', 'defense', 4), ), ),
                    Item(name = 'Dagger', target = 'girl', type = IT_Weapon, pic = 'Dagger.webp', rank = 2, rarity = 2, price = 1750, effects = (Effect('change', 'defense', 5), ), ),
                    Item(name = 'Sacrificial knife', target = 'girl', type = IT_Weapon, pic = 'Sacrificial knife.webp', rank = 2, rarity = 3, price = 2750, effects = (Effect('change', 'defense', 6), ), ),
                    Item(name = 'Mace', target = 'girl', type = IT_Weapon, pic = 'Mace.webp', rank = 3, rarity = 3, price = 5000, effects = (Effect('change', 'defense', 7), ), ),
                    Item(name = 'Whip', target = 'girl', type = IT_Weapon, pic = 'Whip.webp', rank = 3, rarity = 4, price = 10000, effects = (Effect('change', 'defense', 8), ), ),
                    Item(name = 'Steel whip', target = 'girl', type = IT_Weapon, pic = 'Steel whip.webp', rank = 4, rarity = 4, price = 25000, effects = (Effect('change', 'defense', 9), ), ),
                    Item(name = 'Magic blade', target = 'girl', type = IT_Weapon, pic = 'Magic blade.webp', rank = 4, rarity = 5, price = 60000, effects = (Effect('change', 'defense', 10), ), ),
                    Item(name = 'Dildo', target = 'girl', type = IT_Toy, pic = 'Dildo.webp', rank = 1, rarity = 2, charges = 8, price = 125, effects = (Effect('gain', 'sex', 1, 0.5), ), description = "Chance to improve Sex when resting (limited uses)."),
                    Item(name = 'XL dildo', target = 'girl', type = IT_Toy, pic = 'XL dildo.webp', rank = 2, rarity = 3, charges = 8, price = 500, effects = (Effect('gain', 'sex', 2, 0.5), ), description = "Chance to improve Sex when resting (limited uses)."),
                    Item(name = 'XXL dildo', target = 'girl', type = IT_Toy, pic = 'XXL dildo.webp', rank = 3, rarity = 4, charges = 8, price = 2500, effects = (Effect('gain', 'sex', 3, 0.5), ), description = "Chance to improve Sex when resting (limited uses)."),
                    Item(name = 'Black dildo', target = 'girl', type = IT_Toy, pic = 'Black dildo.webp', rank = 4, rarity = 5, charges = 8, price = 10000, effects = (Effect('gain', 'sex', 5, 0.5), ), description = "Chance to improve Sex when resting (limited uses)."),
                    Item(name = 'Butt plug', target = 'girl', type = IT_Toy, pic = 'Butt plug.webp', rank = 1, rarity = 2, charges = 8, price = 125, effects = (Effect('gain', 'anal', 1, 0.5), ), description = "Chance to improve Anal when resting (limited uses)."),
                    Item(name = 'Butt pump', target = 'girl', type = IT_Toy, pic = 'Butt pump.webp', rank = 2, rarity = 3, charges = 8, price = 500, effects = (Effect('gain', 'anal', 2, 0.5), ), description = "Chance to improve Anal when resting (limited uses)."),
                    Item(name = 'Anal dildo', target = 'girl', type = IT_Toy, pic = 'Anal dildo.webp', rank = 3, rarity = 4, charges = 8, price = 2500, effects = (Effect('gain', 'anal', 3, 0.5), ), description = "Chance to improve Anal when resting (limited uses)."),
                    Item(name = 'Anal beads', target = 'girl', type = IT_Toy, pic = 'Anal beads.webp', rank = 4, rarity = 5, charges = 8, price = 10000, effects = (Effect('gain', 'anal', 5, 0.5), ), description = "Chance to improve Anal when resting (limited uses)."),
                    Item(name = 'Ropes', target = 'girl', type = IT_Toy, pic = 'Ropes.webp', rank = 1, rarity = 2, charges = 8, price = 125, effects = (Effect('gain', 'fetish', 1, 0.5), ), description = "Chance to improve Fetish when resting (limited uses)."),
                    Item(name = 'Cuffs', target = 'girl', type = IT_Toy, pic = 'Cuffs.webp', rank = 2, rarity = 3, charges = 8, price = 500, effects = (Effect('gain', 'fetish', 2, 0.5), ), description = "Chance to improve Fetish when resting (limited uses)."),
                    Item(name = 'Gag', target = 'girl', type = IT_Toy, pic = 'Gag.webp', rank = 3, rarity = 4, charges = 8, price = 2500, effects = (Effect('gain', 'fetish', 3, 0.5), ), description = "Chance to improve Fetish when resting (limited uses)."),
                    Item(name = 'Blindfold', target = 'girl', type = IT_Toy, pic = 'Blindfold.webp', rank = 4, rarity = 5, charges = 8, price = 10000, effects = (Effect('gain', 'fetish', 5, 0.5), ), description = "Chance to improve Fetish when resting (limited uses)."),
                    Item(name = 'Arousing gel', target = 'girl', type = IT_Toy, pic = 'Arousing gel.webp', rank = 1, rarity = 2, charges = 8, price = 125, effects = (Effect('gain', 'service', 1, 0.5), ), description = "Chance to improve Service when resting (limited uses)."),
                    Item(name = 'Egg vibrator', target = 'girl', type = IT_Toy, pic = 'Egg vibrator.webp', rank = 2, rarity = 3, charges = 8, price = 500, effects = (Effect('gain', 'service', 2, 0.5), ), description = "Chance to improve Service when resting (limited uses)."),
                    Item(name = 'Long vibrator', target = 'girl', type = IT_Toy, pic = 'Long vibrator.webp', rank = 3, rarity = 4, charges = 8, price = 2500, effects = (Effect('gain', 'service', 3, 0.5), ), description = "Chance to improve Service when resting (limited uses)."),
                    Item(name = 'Arcanic vibrator', target = 'girl', type = IT_Toy, pic = 'Arcanic vibrator.webp', rank = 4, rarity = 5, charges = 8, price = 10000, effects = (Effect('gain', 'service', 5, 0.5), ), description = "Chance to improve Service when resting (limited uses)."),
                    Item(name = 'Lucky charm', target = 'girl', type = IT_Necklace, pic = 'Lucky charm.webp', rank = 1, rarity = 2, price = 1250, effects = (Effect('special', 'lucky', 1), ), description = "It is said to bring luck to its owner. The rabbit it belonged to might disagree..."),
                    Item(name = 'Leather choker', target = 'girl', type = IT_Necklace, pic = 'Leather choker.webp', rank = 1, rarity = 2, price = 750, effects = (Effect('boost', 'obedience tests', 0.2), ), ),
                    Item(name = 'Bronze amulet', target = 'girl', type = IT_Necklace, pic = 'Bronze amulet.webp', rank = 2, rarity = 3, price = 2500, effects = (Effect('boost', 'all regular skills gains', 0.05), ), ),
                    Item(name = 'Silver amulet', target = 'girl', type = IT_Necklace, pic = 'Silver amulet.webp', rank = 3, rarity = 4, price = 12500, effects = (Effect('boost', 'all regular skills gains', 0.1), ), ),
                    Item(name = 'Gold amulet', target = 'girl', type = IT_Necklace, pic = 'Gold amulet.webp', rank = 4, rarity = 5, price = 25000, effects = (Effect('boost', 'all regular skills gains', 0.15), ), ),
                    Item(name = 'Monster pearl necklace', target = 'girl', type = IT_Necklace, pic = 'Monster pearl necklace.webp', rank = 3, rarity = 5, price = 25000, effects = (Effect('boost', 'all sex skills gains', 0.1), ), description =  "It came from the sea..."),
                    Item(name = 'Ale', target = 'girl', type = IT_Supplies, pic = 'Ale.webp', rank = 1, rarity = 1, charges = 10, price = 500, effects = (Effect('change', 'waitress results', 1), ), description =  "Used when working."),
                    Item(name = 'Massage oil', target = 'girl', type = IT_Supplies, pic = 'Massage oil.webp', rank = 1, rarity = 1, charges = 10, price = 500, effects = (Effect('change', 'masseuse results', 1), ), description =  "Used when working."),
                    Item(name = 'Tanning oil', target = 'girl', type = IT_Supplies, pic = 'Tanning oil.webp', rank = 1, rarity = 1, charges = 10, price = 500, effects = (Effect('change', 'dancer results', 1), ), description =  "Used when working."),
                    Item(name = 'Fans', target = 'girl', type = IT_Supplies, pic = 'Fans.webp', rank = 1, rarity = 1, charges = 10, price = 500, effects = (Effect('change', 'geisha results', 1), ), description =  "Used when working."),
                    Item(name = 'Sensual perfume', target = 'girl', type = IT_Supplies, pic = 'Sensual perfume.webp', rank = 1, rarity = 3, charges = 10, price = 750, effects = (Effect('change', 'service results', 1), ), description =  "Used when working."),
                    Item(name = 'Gel', target = 'girl', type = IT_Supplies, pic = 'Gel.webp', rank = 1, rarity = 3, charges = 10, price = 750, effects = (Effect('change', 'sex results', 1), ), description =  "Used when working."),
                    Item(name = 'Enema', target = 'girl', type = IT_Supplies, pic = 'Enema.webp', rank = 1, rarity = 3, charges = 10, price = 750, effects = (Effect('change', 'anal results', 1), ), description =  "Used when working."),
                    Item(name = 'Wax', target = 'girl', type = IT_Supplies, pic = 'Wax.webp', rank = 1, rarity = 3, charges = 10, price = 750, effects = (Effect('change', 'fetish results', 1), ), description =  "Used when working."),
                    Item(name = 'Wyvern egg', target = 'girl', type = IT_Misc, pic = 'Wyvern egg.webp', rank = 1, rarity = "S", charges = 1, price = 15000, effects = (Effect('gain', 'perk', 1), ), description = "A dish fit for a brothel queen.", sound = "crunch.ogg"),
                    Item(name = 'Glasses', target = 'girl', type = IT_Accessory, pic = 'Glasses.webp', rank = 1, rarity = 3, price = 1000, effects = (Effect('boost', 'xp gains', 0.1), ), ),
                    Item(name = 'Tail', target = 'girl', type = IT_Accessory, pic = 'Tail.webp', rank = 1, rarity = 3, price = 1000, effects = (Effect('boost', 'reputation gains', 0.2), ), ),
                    Item(name = 'Bunny ears', target = 'girl', type = IT_Accessory, pic = 'Bunny ears.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'waitress results', 1), ), ),
                    Item(name = 'Hairpin', target = 'girl', type = IT_Accessory, pic = 'Hairpin.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'masseuse results', 1), ), ),
                    Item(name = 'Nun veil', target = 'girl', type = IT_Accessory, pic = 'Nun veil.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'dancer results', 1), ), ),
                    Item(name = 'Noh mask', target = 'girl', type = IT_Accessory, pic = 'Noh mask.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'geisha results', 1), ), ),
                    Item(name = 'Cat ears', target = 'girl', type = IT_Accessory, pic = 'Cat ears.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'service results', 1), ), ),
                    Item(name = 'Nurse hat', target = 'girl', type = IT_Accessory, pic = 'Nurse hat.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'sex results', 1), ), ),
                    Item(name = 'Leather cap', target = 'girl', type = IT_Accessory, pic = 'Leather cap.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'anal results', 1), ), ),
                    Item(name = 'Maid hat', target = 'girl', type = IT_Accessory, pic = 'Maid hat.webp', rank = 1, rarity = 4, price = 2500, effects = (Effect('change', 'fetish results', 1), ), ),
                    Item(name = 'Magic notebook', target = 'MC', type = IT_Passive, pic = 'Magic notebook.webp', template = False, rank = 1, rarity = "S", price = 0, effects = (Effect('special', 'notebook', 1), ), description = "This handy notebook will store all the information you know about your girls. It magically records all your thoughts. Wait, don't think about {i}that{/i}... Too late.", hidden_effect = True),
                    Item(name = 'Healing powder', target = 'minion', type = IT_Misc, pic = 'healing powder.webp', template = False, rank = 1, rarity = "M", charges = 1, price = 100, effects = (Effect('special', 'heal minion', 1), ), description = "This mysterious powder from the East will heal a minion's wounds or repair a magical artefact. Side effects may include dizziness, horniness, tentacles sprouting all over body."),
                    Item(name = 'Cimerian scrap', target = 'misc', type = IT_Misc, pic = 'Cimerian scrap.webp', sound=s_vibro, template = False, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 250, effects = (), description = "A mysterious piece of ancient technological junk."),
                    Item(name = 'Cimerian artefact', target = 'misc', type = IT_Misc, pic = 'Cimerian artefact.webp', sound=s_vibro, template = False, rank = 1, max_rank = 5, rarity = 4, charges = 1, price = 1000, effects = (), description = "A mysterious piece of ancient machinery. Also, junk."),
                    Item(name = "Lightning Rod", target = 'MC', type = IT_Story, pic = "lightning rod.webp", template=False, rank=2, max_rank = 5, rarity=3, price = 1000, effects = (), description = "Prevents lightning bolts from hurting you. It could save your ass in the right situation, although the chance to be hit by lightning while working in a brothel is very low. A syphilis rod might be more useful."),

                    Item(name = 'White flower', target = 'girl', type = IT_Flower, pic = 'White flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'white', 1), ), description = "Flowers are often used as gifts for one's love interest.", hidden_effect = True),
                    Item(name = 'Yellow flower', target = 'girl', type = IT_Flower, pic = 'Yellow flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'yellow', 1), ), description = "Flowers are often used as gifts for one's love interest.", hidden_effect = True),
                    Item(name = 'Red flower', target = 'girl', type = IT_Flower, pic = 'Red flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'red', 1), ), description = "Flowers are often used as gifts for one's love interest.", hidden_effect = True),
                    Item(name = 'Green flower', target = 'girl', type = IT_Flower, pic = 'Green flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'green', 1), ), description = "Flowers are often used as gifts for one's love interest.", hidden_effect = True),
                    Item(name = 'Blue flower', target = 'girl', type = IT_Flower, pic = 'Blue flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'blue', 1), ), description = "Flowers are often used as gifts for one's love interest.", hidden_effect = True),
                    Item(name = 'Orange flower', target = 'girl', type = IT_Flower, pic = 'Orange flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'orange', 1), ), description = "Flowers are often used as gifts for one's love interest.", hidden_effect = True),
                    Item(name = 'Purple flower', target = 'girl', type = IT_Flower, pic = 'Purple flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'purple', 1), ), description = "Flowers are often used as gifts for one's love interest.", hidden_effect = True),
                    Item(name = 'Pink flower', target = 'girl', type = IT_Flower, pic = 'Pink flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'pink', 1), ), description = "Flowers are often used as gifts for one's love interest.", hidden_effect = True),
                    Item(name = 'Black flower', target = 'girl', type = IT_Flower, pic = 'Black flower.webp', template = False, rank = 1, max_rank = 5, rarity = "F", price = 75, effects = (Effect('flower', 'black', 1), ), description = "Flowers are often used as gifts for one's love interest.", hidden_effect = True),
                    ]


        # SPECIAL ITEMS AND FURNITURE #

        blueprint_item = Item(name = 'Ancient blueprint', target = 'MC', type = IT_Story, pic = 'scanner blueprint.webp', template = False, rank = 1, rarity = "S", price = 0, effects = [], description = "An ancient blueprint written on a light yet strong paper-like material. The instructions are foreign and indecipherable, but a skilled craftsman could perhaps make sense of it.", hidden_effect = True)

        vitals_scanner = Furniture('Strange machine', type='Gizmos', pic='scanner.webp', rank=2, chapter=2, cost=[('wood', 20), ('dye', 20), ('leather', 20)], duration=4, effects=[Effect("special", "autorest", 1, scope="brothel")], base_description="This mysterious machine glows with pulsating magical energy.") #  It scans your girls automatically to make sure they are fit to work.

        billboard = Furniture('Clockwork billboard', type='Furnishing', pic='billboard.webp', rank=2, chapter=2, cost=[('wood', 40), ('dye', 25), ('leather', 10)], duration=5, effects=[Effect("special", "advanced advertising", 1, scope="brothel")], base_description="This imposing billboard is sure to draw some attention. Unlocks advanced advertising settings.") #  Unlocks advanced advertising settings

        bast_letter = Item("Bast's love letter", "MC", type=IT_Story, pic="Scroll of etiquette.webp", template = False, rank = 1, rarity = "S", price = 0, effects = [], description = "A love letter written by Bast to her former paramour. Contains incriminating information.", hidden_effect = True)

        extractor_items = {"extractor1" : Item(name="Extractor Mk I", target="MC", type=IT_Story, pic="extractor1.webp", template = False, rarity = "S", price = 5000, effects=[], description = "This strange steam machine lets you harvest wood, dye or leather automatically. Deploy on site."),
                           "extractor2" : Item(name="Extractor Mk II", target="MC", type=IT_Story, pic="extractor2.webp", template = False, rarity = "S", price = 25000, effects=[], description = "This strange steam machine lets you harvest marble, silk or ore automatically. Deploy on site."),
                            }

        magic_notebook = Item(name = 'Magic notebook', target = 'MC', type = IT_Passive, pic = 'Magic notebook.webp', template = False, rank = 1, rarity = "S", price = 0, effects = (Effect('special', 'notebook', 1), ), description = "This handy notebook will store all the information you know about your girls. It magically writes down all your thoughts. Wait, don't think about {i}that{/i}... Too late.", hidden_effect = True)

        mania_amulet = Item(name = "Cheap charm", target = 'MC', type = IT_Story, pic = 'cheap charm.webp', template = False, rank = 1, rarity = "S", price = 10, description = "A cheap amulet found with a mysterious letter mentioning a club called 'Mania' in the guild quarter.", hidden_effect = True)

        toy_hammer = Item(name="Hammer Of Light", target = 'MC', type = IT_Story, pic = 'toy hammer.webp', template = False, rank = 1, rarity = "S", price = 0, description = "A diminutive 'warhammer' made of cheap materials. Supposed to work against the Kunoichi, but it looks like it couldn't even whack a mole.", hidden_effect = True)

        mizuki_kimono = Item(name = "Mizuki's Kimono", target = 'MC', type = IT_Story, pic = 'Kimono.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="dress", description = "A kimono left behind by Mizuki Ike, the mysterious eldest Kunoichi.", hidden_effect = True)

        makibishi = Item(name = "Makibishi", target = 'MC', type = IT_Misc, pic = 'bronze makibishi.webp', template = False, rank = 1, rarity = "S", price = 500, description = "Automatically catch a Kunoichi during ninja hunt.", hidden_effect = True)
#                       Item(name = "Iron Makibishi", target = 'MC', type = IT_Story, pic = 'iron makibishi.webp', template = False, rank = 2, rarity = "S", price = 1000, description = "Slows down Kunoichi movements during ninja hunt (medium effect).", hidden_effect = True),
#                       Item(name = "Steel Makibishi", target = 'MC', type = IT_Story, pic = 'steel makibishi.webp', template = False, rank = 3, rarity = "S", price = 1500, description = "Slows down Kunoichi movements during ninja hunt (large effect).", hidden_effect = True),

        narika_hair = Item(name = "Lock of Narika's hair", target = 'MC', type = IT_Story, pic = 'hair.webp', template = False, rank = 1, rarity = "S", price = 0, description = "A lock of pink hair, belonging to the Kunoichi prodigy Narika Shihoudou.", hidden_effect = True)

        blue_ribbon = Item(name = "Homura's ribbon", target = 'MC', type = IT_Story, pic = 'blue ribbon.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="necklace", description = "A ribbon given to you by Lady Henso. Tie it to a pole in the city {b}Plaza{/b} to let her know you want to see her.", hidden_effect = True)

        earth_rune = Item(name = "Earth Rune", target = 'MC', type = IT_Story, pic = 'earth rune.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="misc", description = "This runestone has a strong inhibitive effect on Earth magic and disorients their users. This could help you out against the Earth ninja.", hidden_effect = True)
        water_rune = Item(name = "Water Rune", target = 'MC', type = IT_Story, pic = 'water rune.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="misc", description = "This runestone has a strong inhibitive effect on Water magic and disorients their users. This could help you out against the Water ninja.", hidden_effect = True)
        void_rune = Item(name = "Void Rune", target = 'MC', type = IT_Story, pic = 'void rune.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="misc", description = "This runestone can manipulate time to slow down super fast people and objects, or something. This could help you out against the Void ninja.", hidden_effect = True)
        fire_rune = Item(name = "Fire Rune", target = 'MC', type = IT_Story, pic = 'fire rune.webp', template = False, rank = 1, rarity = "S", price = 0, pic_dir="misc", description = "This runestone has a strong inhibitive effect on Fire magic and disorients their users. You don't know any Fire magic users, so would that really be useful to you?", hidden_effect = True)

        # Chaos

        chaos_full_charge = Item(name = 'Full Power Chaos', target = 'MC', type = IT_Weapon, sellable=False, giveable=False, pic = 'Demon sword.webp', rank = 4, rarity = "S", price = 0, effects = (Effect('change', 'strength', 4), Effect('change', 'charisma', 4), Effect('change', 'spirit', 4)), description = "The blade pulses with the dark fury of the greater daemon trapped inside. It refills its energy from cavorting with girls, somehow. It is fully charged.")
        chaos_high_charge = Item(name = 'Mid Power Chaos', target = 'MC', type = IT_Weapon, sellable=False, giveable=False, pic = 'Demon sword.webp', rank = 4, rarity = "S", price = 0, effects = (Effect('change', 'strength', 3), Effect('change', 'charisma', 3), Effect('change', 'spirit', 3)), description = "The blade pulses with the dark fury of the greater daemon trapped inside. It refills its energy from cavorting with girls, somehow. It is well charged.")
        chaos_low_charge = Item(name = 'Low Power Chaos', target = 'MC', type = IT_Weapon, sellable=False, giveable=False, pic = 'Demon sword.webp', rank = 4, rarity = "S", price = 0, effects = (Effect('change', 'strength', 2), Effect('change', 'charisma', 2), Effect('change', 'spirit', 2)), description = "The blade pulses with the dark fury of the greater daemon trapped inside. It refills its energy from cavorting with girls, somehow. It is partially charged.")
        chaos_no_charge = Item(name = 'Depleted Chaos', target = 'MC', type = IT_Weapon, sellable=False, giveable=False, pic = 'Demon sword.webp', rank = 4, rarity = "S", price = 0, effects = (Effect('change', 'strength', 1), Effect('change', 'charisma', 1), Effect('change', 'spirit', 1)), description = "The blade pulses with the dark fury of the greater daemon trapped inside. It refills its energy from cavorting with girls, somehow. It is not charged.")

        # TEMPLATE ITEMS #

        template_items =   [
                            Item(name = 'Stolen underwear', target = 'MC', type = IT_Misc, pic = 'Stolen underwear.webp', template = True, rank = 1, max_rank = 5, rarity = "S", charges = 1, price = 500, effects = (Effect('gain', 'prestige', 2), ), description = "So you're into these, eh?"),
                            Item(name = 'Romantic novel', target = 'gift', type = IT_Gift, pic = 'Romantic novel.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'cute', 1), Effect('gift', 'book', 1), ), description =  "A knight in shining armor. A princess. A plumber. The usual.", hidden_effect = True),
                            Item(name = 'Erotic manual', target = 'gift', type = IT_Gift, pic = 'Erotic manual.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'erotica', 1), Effect('gift', 'book', 1), ), description =  "50 positions that you can only achieve using black magic.", hidden_effect = True),
                            Item(name = 'Goldleaf book', target = 'gift', type = IT_Gift, pic = 'Goldleaf book.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'precious', 1), Effect('gift', 'book', 1), ), description =  "What does it talk about? Who cares! It's shiny.", hidden_effect = True),
                            Item(name = 'Book of magical cocktails', target = 'gift', type = IT_Gift, pic = 'Book of magical cocktails.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'drinks', 1), Effect('gift', 'book', 1), ), description =  "Warning: consuming those potions may result in loss of memory. Also,  dignity.", hidden_effect = True),
                            Item(name = 'Pet', target = 'gift', type = IT_Gift, pic = 'Pet.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'cute', 1), Effect('gift', 'precious', 1), ), description =  "Isn't he adorable? As long as he doesn't bite your hand off...", hidden_effect = True),
                            Item(name = 'Silky nighties', target = 'gift', type = IT_Gift, pic = 'Silky nighties.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'cute', 1), Effect('gift', 'erotica', 1), ), description =  "Smooth and sexy.", hidden_effect = True),
                            Item(name = 'Sakura liquor', target = 'gift', type = IT_Gift, pic = 'Sakura liquor.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'cute', 1), Effect('gift', 'drinks', 1), ), description =  "A subtle drink made of distilled flower petals.", hidden_effect = True),
                            Item(name = 'Sexy high heels', target = 'gift', type = IT_Gift, pic = 'Sexy high heels.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'erotica', 1), Effect('gift', 'precious', 1), ), description =  "Some women would kill to get their hands on those shoes. Actually,  they're a little blood spattered.", hidden_effect = True),
                            Item(name = 'Champagne', target = 'gift', type = IT_Gift, pic = 'Champagne.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'drinks', 1), Effect('gift', 'precious', 1), ), description =  "'Le Nouveau Riche': A strong drink; also, a statement that you can afford it.", hidden_effect = True),
                            Item(name = 'Aphrodisiac', target = 'gift', type = IT_Gift, pic = 'Aphrodisiac.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 100, effects = (Effect('gift', 'drinks', 1), Effect('gift', 'erotica', 1), ), description =  "Fire in your belly,  fire in your pants...", hidden_effect = True),
                            Item(name = 'Pretty ring', target = 'girl', type = IT_Ring, pic = 'Pretty ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 150, effects = (Effect('change', 'beauty', 5), ), ),
                            Item(name = 'Bronze ring', target = 'girl', type = IT_Ring, pic = 'Bronze ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 150, effects = (Effect('change', 'body', 5), ), ),
                            Item(name = 'Zanic ring', target = 'girl', type = IT_Ring, pic = 'Zanic ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 150, effects = (Effect('change', 'charm', 5), ), ),
                            Item(name = 'Silver ring', target = 'girl', type = IT_Ring, pic = 'Silver ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 150, effects = (Effect('change', 'refinement', 5), ), ),
                            Item(name = 'Gold ring', target = 'girl', type = IT_Ring, pic = 'Gold ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'libido', 5), ), ),
                            Item(name = 'Marine ring', target = 'girl', type = IT_Ring, pic = 'Marine ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'sensitivity', 5), ), ),
                            Item(name = 'Iron ring', target = 'girl', type = IT_Ring, pic = 'Iron ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 375, effects = (Effect('change', 'obedience', 5), ), ),
                            Item(name = 'Wooden ring', target = 'girl', type = IT_Ring, pic = 'Wooden ring.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'constitution', 5), ), ),
                            Item(name = 'Blue ribbon', target = 'girl', type = IT_Necklace, pic = 'Blue ribbon.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 100, effects = (Effect('boost', 'beauty gains', 0.1), ), ),
                            Item(name = 'Pearl necklace', target = 'girl', type = IT_Necklace, pic = 'Pearl necklace.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 100, effects = (Effect('boost', 'body gains', 0.1), ), ),
                            Item(name = 'Moon necklace', target = 'girl', type = IT_Necklace, pic = 'Moon necklace.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 100, effects = (Effect('boost', 'charm gains', 0.1), ), ),
                            Item(name = 'Ivory necklace', target = 'girl', type = IT_Necklace, pic = 'Ivory necklace.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 100, effects = (Effect('boost', 'refinement gains', 0.1), ), ),
                            Item(name = 'Choker necklace', target = 'girl', type = IT_Necklace, pic = 'Choker necklace.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('boost', 'libido gains', 0.1), ), ),
                            Item(name = 'Dog collar', target = 'girl', type = IT_Necklace, pic = 'Dog collar.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('boost', 'obedience gains', 0.1), ), ),
                            Item(name = 'Silver chain', target = 'girl', type = IT_Necklace, pic = 'Silver chain.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('boost', 'sensitivity gains', 0.1), ), ),
                            Item(name = 'Dagger necklace', target = 'girl', type = IT_Necklace, pic = 'Dagger necklace.webp', template = True, rank = 1, max_rank = 5, rarity = 2, price = 250, effects = (Effect('boost', 'constitution gains', 0.1), ), ),
                            Item(name = 'Gold bag', target = 'girl', type = IT_Misc, pic = 'Gold bag.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 600, effects = (Effect('special', 'level', 5), ), description =  "Instant level up. Use it wisely...", adjectives = "ring"),
                            Item(name = 'Jewel bag', target = 'girl', type = IT_Misc, pic = 'Jewel bag.webp', template = True, rank = 1, max_rank = 5, rarity = 3, charges = 1, price = 500, effects = (Effect('gain', 'skill points', 5), ), description =  "Get extra skill points."),
                            Item(name = 'Knowledge scroll', target = 'girl', type = IT_Misc, pic = 'Knowledge scroll.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 400, effects = (Effect('gain', 'xp', 50), ), description =  "Get free xp.", adjectives = "scroll"),
                            Item(name = 'Medicine bag', target = 'girl', type = IT_Misc, pic = 'Medicine bag.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 250, effects = (Effect('instant', 'heal', 2), ), description =  ""),
                            Item(name = 'Tonic', target = 'girl', type = IT_Misc, pic = 'Tonic.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 75, effects = (Effect('gain', 'energy', 20), ), description =  ""),
                            Item(name = 'Wine', target = 'girl', type = IT_Misc, pic = 'Wine.webp', template = True, rank = 1, max_rank = 5, rarity = 1, charges = 1, price = 75, effects = (Effect('gain', 'mood', 10), ), description =  ""),
                            Item(name = 'Apple', target = 'girl', type = IT_Food, pic = 'Apple.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 50, effects = (Effect('change', 'beauty', 5, duration=10), Effect('gain', 'heal', 1, 0.5)), description =  "An apple a day keeps the doctor away."),
                            Item(name = 'Pear', target = 'girl', type = IT_Food, pic = 'Pear.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 50, effects = (Effect('change', 'body', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = 'Peach', target = 'girl', type = IT_Food, pic = 'Peach.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 50, effects = (Effect('change', 'charm', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = 'Grapes', target = 'girl', type = IT_Food, pic = 'Grapes.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 50, effects = (Effect('change', 'refinement', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = 'Sausage', target = 'girl', type = IT_Food, pic = 'Sausage.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 75, effects = (Effect('change', 'libido', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = 'Cheese', target = 'girl', type = IT_Food, pic = 'Cheese.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 75, effects = (Effect('change', 'sensitivity', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = 'Chicken', target = 'girl', type = IT_Food, pic = 'Chicken.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 90, effects = (Effect('change', 'obedience', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = 'Roastbeef', target = 'girl', type = IT_Food, pic = 'Roastbeef.webp', template = True, rank = 1, max_rank = 6, rarity = 1, charges = 1, price = 75, effects = (Effect('change', 'constitution', 5, duration=10), Effect('instant', 'heal', 1, 0.5)), ),
                            Item(name = 'Love potion', target = 'girl', type = IT_Misc, pic = 'Love potion.webp', template = True, rank = 1, max_rank = 6, rarity = 2, charges = 1, price = 100, effects = (Effect('gain', 'love', 2.5), ), description = "Who said money can't buy you love?"),
                            Item(name = 'Monster juice', target = 'girl', type = IT_Misc, pic = 'Monster juice.webp', template = True, rank = 1, max_rank = 6, rarity = 2, charges = 1, price = 60, effects = (Effect('gain', 'fear', 2.5), ), description = "You don't want to know from which monster body parts this came from."),
                            Item(name = 'Pink panties', target = 'girl', type = IT_Accessory, pic = 'Pink panties.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 125, effects = (Effect('change', 'beauty', 5), ), ),
                            Item(name = 'Hot pants', target = 'girl', type = IT_Accessory, pic = 'Hot pants.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 125, effects = (Effect('change', 'body', 5), ), ),
                            Item(name = 'Lowcut panties', target = 'girl', type = IT_Accessory, pic = 'Lowcut panties.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 125, effects = (Effect('change', 'charm', 5), ), ),
                            Item(name = 'Lace panties', target = 'girl', type = IT_Accessory, pic = 'Lace panties.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 125, effects = (Effect('change', 'refinement', 5), ), ),
                            Item(name = 'Sexy panties', target = 'girl', type = IT_Accessory, pic = 'Sexy panties.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'libido', 5), ), ),
                            Item(name = 'Seethrough panties', target = 'girl', type = IT_Accessory, pic = 'Seethrough panties.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 250, effects = (Effect('change', 'sensitivity', 5), ), ),
                            Item(name = 'Chastity belt', target = 'girl', type = IT_Accessory, pic = 'Chastity belt.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 350, effects = (Effect('change', 'obedience', 5), ), ),
                            Item(name = 'Thong', target = 'girl', type = IT_Accessory, pic = 'Thong.webp', template = True, rank = 1, max_rank = 6, rarity = 2, price = 175, effects = (Effect('change', 'constitution', 5), ), ),
                            Item(name = 'Bunny suit', target = 'girl', type = IT_Dress, pic = 'Bunny suit.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'body', 5), Effect('change', 'libido', 5), ), ),
                            Item(name = 'Guard uniform', target = 'girl', type = IT_Dress, pic = 'Guard uniform.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'charm', 5), Effect('change', 'constitution', 5), ), ),
                            Item(name = 'School uniform', target = 'girl', type = IT_Dress, pic = 'School uniform.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'beauty', 5), Effect('change', 'libido', 5), ), ),
                            Item(name = 'Bikini', target = 'girl', type = IT_Dress, pic = 'Bikini.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'body', 5), Effect('change', 'constitution', 5), ), ),
                            Item(name = 'Kimono', target = 'girl', type = IT_Dress, pic = 'Kimono.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 350, effects = (Effect('change', 'refinement', 5), Effect('change', 'obedience', 5), ), ),
                            Item(name = 'Swimsuit', target = 'girl', type = IT_Dress, pic = 'Swimsuit.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'beauty', 5), Effect('change', 'sensitivity', 5), ), ),
                            Item(name = 'Frilly dress', target = 'girl', type = IT_Dress, pic = 'Frilly dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'charm', 5), Effect('change', 'sensitivity', 5), ), ),
                            Item(name = 'Leather dress', target = 'girl', type = IT_Dress, pic = 'Leather dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 250, effects = (Effect('change', 'constitution', 5), Effect('change', 'obedience', 5), ), ),
                            Item(name = 'Evening gown', target = 'girl', type = IT_Dress, pic = 'Evening gown.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 400, effects = (Effect('change', 'beauty', 5), Effect('change', 'charm', 5), Effect('change', 'refinement', 5), Effect('change', 'body', -5), ), ),
                            Item(name = 'Silk dress', target = 'girl', type = IT_Dress, pic = 'Silk dress.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 400, effects = (Effect('change', 'libido', 5), Effect('change', 'sensitivity', 5), Effect('change', 'obedience', 5), Effect('change', 'constitution', -5), ), ),
                            Item(name = 'Pompom uniform', target = 'girl', type = IT_Dress, pic = 'Pompom uniform.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 400, effects = (Effect('change', 'beauty', 5), Effect('change', 'charm', 5), Effect('change', 'body', 5), Effect('change', 'refinement', -5), ), ),
                            Item(name = 'Knight uniform', target = 'girl', type = IT_Dress, pic = 'Knight uniform.webp', template = True, rank = 1, max_rank = 6, rarity = 1, price = 400, effects = (Effect('change', 'body', 5), Effect('change', 'constitution', 5), Effect('change', 'obedience', 5), Effect('change', 'libido', -5), ), ),
                            Item(name = 'Black slavekini', target = 'girl', type = IT_Dress, pic = 'Black slavekini.webp', template = True, rank = 1, max_rank = 6, rarity = "S", price = 750, effects = (Effect('change', 'beauty', 5), Effect('change', 'body', 5), Effect('change', 'charm', 5), Effect('change', 'refinement', 5), ), ),
                            Item(name = 'Blue slavekini', target = 'girl', type = IT_Dress, pic = 'Blue slavekini.webp', template = True, rank = 1, max_rank = 6, rarity = "S", price = 1000, effects = (Effect('change', 'libido', 5), Effect('change', 'sensitivity', 5), Effect('change', 'obedience', 5), Effect('change', 'constitution', 5), ), ),
                            Item(name = 'Red slavekini', target = 'girl', type = IT_Dress, pic = 'Red slavekini.webp', template = True, rank = 1, max_rank = 6, rarity = "S", price = 2000, effects = (Effect('change', 'service', 5), Effect('change', 'sex', 5), Effect('change', 'anal', 5), Effect('change', 'fetish', 5), ), ),
                            Item(name = 'Sunny dress', target = 'girl', type = IT_Dress, pic = 'Sunny dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 300, effects = (Effect('change', 'beauty', 10), ), ),
                            Item(name = 'Revealing dress', target = 'girl', type = IT_Dress, pic = 'Revealing dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 300, effects = (Effect('change', 'body', 10), ), ),
                            Item(name = 'Exotic dress', target = 'girl', type = IT_Dress, pic = 'Exotic dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 300, effects = (Effect('change', 'charm', 10), ), ),
                            Item(name = 'Priestess robe', target = 'girl', type = IT_Dress, pic = 'Priestess robe.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 300, effects = (Effect('change', 'refinement', 10), ), ),
                            Item(name = 'Slutty dress', target = 'girl', type = IT_Dress, pic = 'Slutty dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 425, effects = (Effect('change', 'libido', 10), ), ),
                            Item(name = 'Seethrough dress', target = 'girl', type = IT_Dress, pic = 'Seethrough dress.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 425, effects = (Effect('change', 'sensitivity', 10), ), ),
                            Item(name = 'Maid uniform', target = 'girl', type = IT_Dress, pic = 'Maid uniform.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 500, effects = (Effect('change', 'obedience', 10), ), ),
                            Item(name = 'Gym uniform', target = 'girl', type = IT_Dress, pic = 'Gym uniform.webp', template = True, rank = 0, max_rank = 6, rarity = 0, price = 425, effects = (Effect('change', 'constitution', 10), ), ),
                            Item(name = 'Emerald ring', target = 'girl', type = IT_Ring, pic = 'Emerald ring.webp', template = True, rank = 1, max_rank = 5, rarity = 3, price = 500, effects = (Effect('change', 'service', 5), ), ),
                            Item(name = 'Ruby ring', target = 'girl', type = IT_Ring, pic = 'Ruby ring.webp', template = True, rank = 1, max_rank = 5, rarity = 3, price = 500, effects = (Effect('change', 'sex', 5), ), ),
                            Item(name = 'Amber ring', target = 'girl', type = IT_Ring, pic = 'Amber ring.webp', template = True, rank = 1, max_rank = 5, rarity = 3, price = 500, effects = (Effect('change', 'anal', 5), ), ),
                            Item(name = 'Sapphire ring', target = 'girl', type = IT_Ring, pic = 'sapphire ring.webp', template = True, rank = 1, max_rank = 5, rarity = 3, price = 500, effects = (Effect('change', 'fetish', 5), ), ),
                            Item(name = 'Scroll of bartending', target = 'girl', type = IT_Misc, pic = 'Scroll of bartending.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'waitress jp', 10), ), adjectives = "scroll"),
                            Item(name = 'Scroll of whirling', target = 'girl', type = IT_Misc, pic = 'Scroll of whirling.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'dancer jp', 10), ), adjectives = "scroll"),
                            Item(name = 'Scroll of rubbing', target = 'girl', type = IT_Misc, pic = 'Scroll of rubbing.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'masseuse jp', 10), ), adjectives = "scroll"),
                            Item(name = 'Scroll of etiquette', target = 'girl', type = IT_Misc, pic = 'Scroll of etiquette.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'geisha jp', 10), ), adjectives = "scroll"),
                            Item(name = 'Scroll of Onan', target = 'girl', type = IT_Misc, pic = 'Scroll of Onan.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'service jp', 10), ), adjectives = "scroll"),
                            Item(name = 'Scroll of Eros', target = 'girl', type = IT_Misc, pic = 'Scroll of Eros.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'sex jp', 10), ), adjectives = "scroll"),
                            Item(name = 'Scroll of Sodom', target = 'girl', type = IT_Misc, pic = 'Scroll of Sodom.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'anal jp', 10), ), adjectives = "scroll"),
                            Item(name = 'Scroll of Gomorrah', target = 'girl', type = IT_Misc, pic = 'Scroll of Gomorrah.webp', template = True, rank = 1, max_rank = 5, rarity = 2, charges = 1, price = 150, effects = (Effect('gain', 'fetish jp', 10), ), adjectives = "scroll"),
                            Item(name = 'Elvish-made penis enlarger', target = 'minion', type = IT_Misc, pic = 'enlarger.webp', template = True, rank = 1, max_rank = 5, rarity = "M", charges = 1, price = 120, effects = (Effect('gain', 'stallion xp', 10), ), description = "That's not mine. This sort of thing ain't my bag, baby!"),
                            Item(name = 'Machine lubricant', target = 'minion', type = IT_Misc, pic = 'lubricant.webp', template = True, rank = 1, max_rank = 5, rarity = "M", charges = 1, price = 120, effects = (Effect('gain', 'machine xp', 10), ), description = "Grease is good."),
                            Item(name = 'Strange feed', target = 'minion', type = IT_Misc, pic = 'feed.webp', template = True, rank = 1, max_rank = 5, rarity = "M", charges = 1, price = 120, effects = (Effect('gain', 'beast xp', 10), ), description = "Like it when they hold onto your leg and rubs themselves up and down? Because this feed sure makes them wanna do that."),
                            Item(name = 'Monster cookie', target = 'minion', type = IT_Misc, pic = 'cookie.webp', template = True, rank = 1, max_rank = 5, rarity = "M", charges = 1, price = 120, effects = (Effect('gain', 'monster xp', 10), ), description = "C is for cock-y.", adjectives = "food"),
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
            Furniture('Buckets', type='Utility', pic='Buckets.webp', rank=2, chapter=2, cost=[('wood', 6), ('leather', 2), ], duration=0, upgrade='Basic broom', effects=[Effect("boost", "maintenance", 0.25, scope="brothel")], ),
            Furniture('Towels', type='Utility', pic='Towels.webp', rank=3, chapter=3, cost=[('dye', 5), ('leather', 5), ], duration=1, upgrade='Buckets', effects=[Effect("boost", "maintenance", 0.35, scope="brothel")], ),
            Furniture('Wheelbarrow', type='Utility', pic='Wheelbarrow.webp', rank=3, chapter=4, cost=[('wood', 4), ('dye', 4), ('leather', 4), ('ore', 4), ], duration=1, upgrade='Buckets', effects=[Effect("boost", "maintenance", 0.5, scope="brothel")], ),
            Furniture('Magic broom', type='Utility', pic='magic broom.webp', rank=3, chapter=5, cost=[('wood', 10), ('leather', 6), ('silk', 6), ], duration=2, upgrade='Wheelbarrow', effects=[Effect("boost", "maintenance", 1, scope="brothel")], ),
            Furniture('Steam cart', type='Utility', pic='Steam cart.webp', rank=4, chapter=6, cost=[('leather', 6), ('marble', 6), ('silk', 6), ('ore', 6), ], duration=2, upgrade='Wheelbarrow', effects=[Effect("boost", "maintenance", 1.5, scope="brothel")], ),
            Furniture('Mechanical maid', type='Utility', pic='Robot maid.webp', rank=5, chapter=7, cost=[('silk', 6), ('ore', 10), ], duration=3, upgrade='Steam cart', effects=[Effect("boost", "maintenance", 3, scope="brothel")], ),
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
                        textbutton {True: "Hide", False: "Search"}[show_search_left] text_xalign 0.5 text_italic True text_color c_darkbrown text_size res_font(14) xpadding 0 ypadding 0 xalign 0.5 yalign 0.6 xsize xres(38) ysize yres(20) idle_background None action (ToggleScreenVariable("show_search_left"), SetField(MC, "active_text_filter", ""), SelectedIf(show_search_left))
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
                    tooltip __("Click to sort by ") + __(_ttip) +"."

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
                    text "Search: " size res_font(16) color c_brown
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
                                        $ text1 += "\n" + str(it.get_price("sell")) + " gold"

                                    if "buy" in acts:
                                        $ text1 += "\n" + str(it.get_price("buy")) + " gold"

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
                            text_font "DejaVuSans.TTF"

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
                            text_font "DejaVuSans.TTF"


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
            use close(Hide("item_profile"), name = "hide")
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
                text "{color=[col]}" + __(it.target.capitalize()) + "{/color}" xalign 0.5 size res_font(18)

            if isinstance(it, Item):
                text __(it.base_description) size res_font(14) xalign 0.5
            text __(it.description) size res_font(14) xalign 0.5

            text ""

            if "buy" in acts:
                text str(it.get_price("buy")) + " gold" xalign 0.5
                text ""

            if "bargain" in acts:
                text str(it.get_price("bargain")) + " gold" xalign 0.5
                text ""

            if "sell" in acts:
                text str(it.get_price("sell")) + " gold" xalign 0.5
                text ""

            if isinstance(it, Item) and it in MC.items and not it.sellable:
                text "Unsellable" italic True xalign 0.5
                text ""

            hbox spacing 10 xalign 0.5:
                for act in acts:
                    textbutton __(capitalize(act)) action Return((it, act)) xalign 0.5:
                        if owner.type == "girl" and act in ("equip", "unequip", "use"):
                            hovered SetScreenVariable("focused_char", owner)
                        elif counterpart and counterpart.type == "girl":
                            hovered SetScreenVariable("focused_char", counterpart)
                            if owner.type == "girl":
                                unhovered SetScreenVariable("focused_char", owner)

                if "bargain" in acts:
                    textbutton __("Skip") action Return("leave") xalign 0.5

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
                    text slot.capitalize() size res_font(14) xalign 0.5 color c_brown

                    button xsize yres(60) ysize yres(60) xfill True yfill True xalign 0.5:
                        style "girlbutton_blue"
                        if eq:
                            add eq.pic.get(*res_tb(45)) xalign 0.5 yalign 0.5
                            action (Show("item_profile", it=eq, transition = dissolve), SetVariable("owner", char), SetVariable("counterpart", counterpart), SetVariable("selected_item", eq), SetField(MC, "active_inv_filter", [slot]), SelectedIf(slot in MC.active_inv_filter))
                            tooltip __(eq.description)
                        else:
                            text "Empty" size res_font(12) italic True xalign 0.5 yalign 0.5
                            action (SetField(MC, "active_inv_filter", [slot]), SelectedIf(slot in MC.active_inv_filter))
                            tooltip "No item is equipped to this slot."


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
                        tooltip __("Show %s items.") % __(filter)
                    else:
                        if not MC.active_inv_filter:
                            add "filter_all" xalign 0.5 yalign 0.5
                        else:
                            add "filter_all_unselect" xalign 0.5 yalign 0.5
                        tooltip "Show all items."


#### END OF BK ITEMS FILE ####
