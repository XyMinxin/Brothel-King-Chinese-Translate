#### BK SPELLS AND MOONS ####
## Labels are used instead of Functions to make sure we are using global variables

## SPELLS ##

label init_spells():

    python:


        # SPECIAL SPELLS AND SPELL EFFECTS #

        shield_effect = Effect("special", "shield", value = 1) #Individual shield, unused as of v0

        bshield_effect = Effect("special", "shield", value = 1, scope = "brothel")

        bshield_spell = Spell('Magic shield', 'shield.webp', type="shield", level=4, cost=2, effects=[bshield_effect], description="Protects your girls from external threats with a magic barrier. Stops the next act of aggression against one of your girls before it happens. Lasts until the next attack.")

        # REGULAR SPELLS #

        spellbook = {
                    "Warrior" : [
                            Spell('Heavy Lifting', 'strength.webp', level=2, effects=[Effect("gain", "strength", 1)], description="Pumping and Pimping."),
                            Spell('The Defender', 'defender.webp', type="passive", level=3, effects=[Effect("special", "defender", 1)], description="It's like you can be everywhere at once."),
                            Spell('Discipline', 'discipline.webp', type="discipline", level=4, cost=1, effects=[Effect("change", "train obedience target", -10, scope="brothel"), Effect("change", "job obedience target", -10, scope="brothel")], duration="turn", description="The pain of discipline is nothing like the pain of disappointment."),
                            Spell('Samurai Spirit', 'spirit.webp', level=6, effects=[Effect("gain", "spirit", 1)], description="You must see it through your mind's Eye."),
                            Spell('Summon Bloodhound', 'hound.webp', type="summon", level=8, cost=2, effects=[Effect("change", "fight challenges", 6, dice=True)], duration="turn", description="Summons a ghastly bloodhound to help you with individual fights."),
                            Spell('Secret technique', 'strength.webp', level=10, effects=[Effect("gain", "strength", 1)], description="I will find you, and I will kill you. Twice."),
                            Spell('Training Day', 'training.webp', type="training", level=12, cost=3, effects=[Effect("boost", "body gains", 0.05, scales_with="charisma", scope="brothel"), Effect("boost", "constitution gains", 0.05, scales_with="charisma", scope="brothel")], duration="turn", description="The more you sweat in training, the less you bleed in combat."),
                            Spell('Commanding Voice', 'charisma.webp', level=14, effects=[Effect("gain", "charisma", 1)], description="From the battlefield to the whorehouse, you've never lost that edge."),
                            Spell('Summon Phoenix', 'phoenix.webp', type="summon", level=16, cost=4, effects=[Effect("boost", "energy when resting", 0.25, scope="brothel")], duration="turn", description="Summons a magical bird whose soothing songs help your girls relax. "),
                            Spell('Eye Of The Tiger', 'strength.webp', level=18, effects=[Effect("gain", "strength", 1)], description="ADRIAAAAAN!!!"),
                            Spell('Summon Bear Spirit', 'bear.webp', type="summon", level=20, cost=5, effects=[Effect("change", "job customer capacity", 2, scope="brothel"), Effect("change", "whore customer capacity", 1, scope="brothel")], duration="turn", description="Summons a totemic beast that infuses your girls with supernatural power."),
                            Spell('Lightning Reflexes', 'speed.webp', level=22, effects=[Effect("gain", "speed", 1)], description="Swift like a cobra."),
                            Spell('Brothel Militia', 'militia.webp', type="passive", level=24, effects=[Effect("boost", "defense", 2, scope="brothel")], description="Man the battlestations! Err… Should it be 'Woman the battlestations'?"),
                            ],
                    "Trader" : [
                            Spell('Rogue', 'charisma.webp', level=2, effects=[Effect("gain", "charisma", 1)], description="Every day I'm hustling."),
                            Spell('The Haggler', 'haggler.webp', type="passive", level=3, effects=[Effect("boost", "buy", -0.02, scales_with="charisma"), Effect("boost", "sell", 0.02, scales_with="charisma")], description="'That's it. I'm walking away now...' Better prices for girls and items."),
                            Spell('Sign Of Influence', 'sign1.webp', type="sign", level=4, cost=1, effects=[Effect("boost", "love gains", 0.1, scope="brothel"), Effect("boost", "fear gains", 0.1, scope="brothel")], duration="turn", description="Trust is earned. Unless you know magic."),
                            Spell('Street Fighter', 'strength.webp', level=6, effects=[Effect("gain", "strength", 1)], description="The mean streets of Borgo have taught you all that there is to know about street fighting. Always stab from the back."),
                            Spell('Tall Tales', 'tale.webp', type="tales", level=8, cost=2, effects=[Effect("boost", "prestige", 0.1, scope="brothel")], duration="turn", description="Cool story bro."),
                            Spell('Adventurer', 'charisma.webp', level=10, effects=[Effect("gain", "charisma", 1)], description="You don't always adventure far from your bed, but at least you look the part."),
                            Spell('Sign Of Confidence', 'sign2.webp', type="sign", level=12, cost=3, effects=[Effect("boost", "charm gains", 0.05, scales_with="charisma", scope="brothel"), Effect("boost", "libido gains", 0.05, scales_with="charisma", scope="brothel")], duration="turn", description="You're gorgeous, you don't need validation from anyone, but here, have this spell just in case."),
                            Spell('Worldly', 'spirit.webp', level=14, effects=[Effect("gain", "spirit", 1)], description="I've spent months living among the amazon tribes of the Lankan Rainforest. Wanna know how they do it?"),
                            Spell('Silver Tongue', 'girl.webp', type="city", level=16, cost=4, effects=[Effect("boost", "love gains", 0.3, scope="city")], duration="turn", description="You can grab 'em by the pussy, you can do anything."),
                            Spell('Smooth Criminal', 'charisma.webp', level=18, effects=[Effect("gain", "charisma", 1)], description="You've been hit by, you've been struck by…"),
                            Spell('Sign Of Greed', 'sign3.webp', type="sign", level=20, cost=5, effects=[Effect("boost", "total upkeep", -0.2, scope="brothel")], duration="turn", description="Greed is good. At least my spellbook says so."),
                            Spell('Shadowrunner', 'speed.webp', level=22, effects=[Effect("gain", "speed", 1)], description="You're fast. You've got the ship that made the Westmarch Run in less than twelve parsecs… Somewhere."),
                            Spell('Fame', 'fame.webp', type="passive", level=24, effects=[Effect("change", "customers", 1, scales_with="charisma", scope="brothel")], description="Fame, makes a man take things over!"),

                            ],
                    "Wizard" : [
                            Spell('Inquisitive', 'spirit.webp', level=2, effects=[Effect("gain", "spirit", 1)], description="A beautiful mind. Pity about your face, though!"),
                            Spell('Minor Aura: Purity', 'aura1.webp', type="aura", level=2, cost=1, effects=[Effect("change", "beauty", 5, scope="brothel")], duration="turn", description="Looks aren't everything, but, hey, they sell. This aura makes your girls look nicer."),
                            Spell('Minor Aura: Provocation', 'aura4.webp', type="aura", level=2, cost=1, effects=[Effect("change", "body", 5, scope="brothel")], duration="turn", description="Shake your money-maker. Now with magic. This aura enhances your girl's body."),
                            Spell('Minor Aura: Mystery', 'aura2.webp', type="aura", level=2, cost=1, effects=[Effect("change", "charm", 5, scope="brothel")], duration="turn", description="The air of mystery around your girls keep the patrons coming back for more. This aura boosts your girls' charm."),
                            Spell('Minor Aura: Sophistication', 'aura3.webp', type="aura", level=2, cost=1, effects=[Effect("change", "refinement", 5, scope="brothel")], duration="turn", description="It takes a real magician to make uncouth slaves look sophisticated. This aura makes your girls more refined."),
                            Spell('The Sorcerer', 'sorcerer.webp', type="passive", level=3, effects=[Effect("boost", "mana", 1)], description="It's raining mana! Hallelujah."),
                            Spell('Magic shield', 'shield.webp', type="shield", level=4, cost=2, effects=[bshield_effect], description="Protects your girls from external threats with a magic barrier. Stops the next act of aggression against one of your girls before it happens. Lasts until the next attack."),
                            Spell('Minor Halo: Lust', 'halo1.webp', type="halo", level=5, cost=3, effects=[Effect("change", "libido", 5, scope="brothel")], duration="turn", description="It's getting hot in here… This halo boosts your girls' libido."),
                            Spell('Minor Halo: Servility', 'halo3.webp', type="halo", level=5, cost=3, effects=[Effect("change", "obedience", 5, scope="brothel")], duration="turn", description="On your knees, maggots! This makes your girls more obedient."),
                            Spell('Minor Halo: Sensuality', 'halo2.webp', type="halo", level=5, cost=3, effects=[Effect("change", "sensitivity", 5, scope="brothel")], duration="turn", description="Soft whispers echo into your girls' ears, making them shiver expectantly. Raises their sensitivity."),
                            Spell('Minor Halo: Endurance', 'halo4.webp', type="halo", level=5, cost=3, effects=[Effect("change", "constitution", 5, scope="brothel")], duration="turn", description="It's like solid energy is seeping through the brisk, fragrant air. Boosts your girl's constitution."),
                            Spell('Wise', 'charisma.webp', level=6, effects=[Effect("gain", "charisma", 1)], description="This is payback for all those times they called you a 'Wise guy'."),
                            Spell('Magic servants', 'servants.webp', type="spell", level=7, cost=3, effects=[Effect("instant", "dirt", -50, scales_with="spirit")], duration="turn", description="In the fairy tales, they don't have the dancing dildo cabinet."),
                            Spell('Healing mist', 'heal.webp', type="mist", level=8, cost=4, effects=[Effect("instant", "heal", 1, 0.5, scope="brothel", scales_with="spirit")], duration="turn", description="Medic! This mist has a chance to heal your girls fully."),
                            Spell('Major Aura: Purity', 'aura1b.webp', type="aura", level=9, cost=5, effects=[Effect("change", "beauty", 2, scales_with="spirit", scope="brothel")], duration="turn", description="Looks aren't everything, but, hey, they sell. This aura makes your girls look a lot nicer."),
                            Spell('Major Aura: Provocation', 'aura4b.webp', type="aura", level=9, cost=5, effects=[Effect("change", "body", 2, scales_with="spirit", scope="brothel")], duration="turn", description="Shake your money-maker. Now with magic. This aura enhances your girl's body greatly."),
                            Spell('Major Aura: Mystery', 'aura2b.webp', type="aura", level=9, cost=5, effects=[Effect("change", "charm", 2, scales_with="spirit", scope="brothel")], duration="turn", description="The air of mystery around your girls keep the patrons coming back for more. This aura gives a major boost to your girls' charm."),
                            Spell('Major Aura: Sophistication', 'aura3b.webp', type="aura", level=9, cost=5, effects=[Effect("change", "refinement", 2, scales_with="spirit", scope="brothel")], duration="turn", description="It takes a real magician to make uncouth slaves look sophisticated. This aura makes your girls a lot more refined."),
                            Spell('Creative', 'spirit.webp', level=10, effects=[Effect("gain", "spirit", 1)], description="Now, who would have thought of using a magic wand for that..."),
                            Spell('Enhanced senses', 'enhanced.webp', type="trance", level=11, cost=6, effects=[Effect("boost", "refinement gains", 0.05, scales_with="spirit", scope="brothel"), Effect("boost", "sensitivity gains", 0.05, scales_with="charisma", scope="brothel")], duration="turn", description="Now, did you know there is a 5th dimension? And a 6th, and a 7th, and a 13th?"),
                            Spell('Doll master', 'doll.webp', type="trance", level=11, cost=6, effects=[Effect("boost", "beauty gains", 0.05, scales_with="spirit", scope="brothel"), Effect("boost", "obedience gains", 0.05, scales_with="charisma", scope="brothel")], duration="turn", description="I saw people sticking a needle into a voodoo doll, but never {i}there{/i}…"),
                            Spell('Major Halo: Lust', 'halo1b.webp', type="halo", level=12, cost=8, effects=[Effect("change", "libido", 2, scales_with="spirit", scope="brothel")], duration="turn", description="It's getting hot in here… This halo gives a large boost to your girls' libido."),
                            Spell('Major Halo: Servility', 'halo3b.webp', type="halo", level=12, cost=8, effects=[Effect("change", "obedience", 2, scales_with="spirit", scope="brothel")], duration="turn", description="On your knees, maggots! This makes your girls a lot more obedient."),
                            Spell('Major Halo: Sensuality', 'halo2b.webp', type="halo", level=12, cost=8, effects=[Effect("change", "sensitivity", 2, scales_with="spirit", scope="brothel")], duration="turn", description="Soft whispers echo into your girls' ears, making them shiver expectantly. This raises their sensitivity a lot."),
                            Spell('Major Halo: Endurance', 'halo4b.webp', type="halo", level=12, cost=8, effects=[Effect("change", "constitution", 2, scales_with="spirit", scope="brothel")], duration="turn", description="It's like solid energy is seeping through the brisk, fragrant air. Major boost to your girl's constitution."),
                            Spell('Staff master', 'strength.webp', level=14, effects=[Effect("gain", "strength", 1)], description="If all else fails, you can still crack their skulls with it."),
                            Spell('Rejuvenation', 'hand.webp', type="mist", level=16, cost=9, effects=[Effect("gain", "energy", 5, scope="brothel", scales_with="spirit")], duration="turn", description="This soothing mist rests your girls, in addition to smelling peachy."),
                            Spell('Mad', 'spirit.webp', level=18, effects=[Effect("gain", "spirit", 1)], description="Utter madness and devastating power. Always a great combination."),
                            Spell('Fairy dust', 'fairy.webp', type="form", level=20, cost=9, effects=[Effect("special", "fairy form", 1)], duration="turn", description="You assume the mysterious, ethereal form of the fairy people. Your spirit is used instead of your charisma."),
                            Spell('Dragon soul', 'dragon.webp', type="form", level=20, cost=9, effects=[Effect("special", "dragon form", 1)], duration="turn", description="You assume a terrifying dragon form. Your spirit is used instead of your strength."),
                            Spell('Enchanted Brothel', 'ghost.webp', type="enchant", level=22, cost=10, effects=[Effect("increase satisfaction", "all jobs", 1, scope="brothel"), Effect("increase satisfaction", "all sex acts", 1, scope="brothel")], duration="turn", description="That's a kind of magic… Not the one your childhood fairy tales were referring to."),
                            Spell('Swift', 'speed.webp', level=22, effects=[Effect("gain", "speed", 1)], description="I've got magic in my pants. I mean, they make me run faster."),
                            Spell('The Eye', 'eye.webp', type="passive", level=24, effects=[Effect("special", "snake eyes", 1)], description="Learnt that trick from a guy named Sauron. A nice fella, if a bit obsessed about jewelry.\nHypnosis attempts will always succeed."),
                            Spell('Mindtrick', 'mindtrick.webp', type="trick", level=24, cost=10, duration="turn", effects=[Effect("boost", "job customer budget", 0.25, scope="brothel"), Effect("boost", "whore customer budget", 0.25, scope="brothel")], description="Learnt that trick from an old bum called Zobiwan. He was good at escorting druids, though."),
                            ],
                    }

    return


## MOONS ##

label init_moons():
    python:
        moons = {
                 1 : Moon("gold", effects=[Effect("boost", "income", value = 0.5, scope = "brothel")], description="A new year is just starting in Xeros! This is the most important holiday of the year. People are encouraged to spend a lot to show off their good fortune.", sound = s_gold),
                 2 : Moon("wolf", effects=[Effect("boost", "city rewards", 1, scope="brothel"), Effect("change", "city rewards", 1, scope="brothel"), Effect("boost", "resource extraction", 1, scope="brothel")], description="This month is the coldest of the year. It is said that adventurers that brave this tough season can reap the best rewards.", sound = s_wolf),
                 3 : Moon("blue", effects=[Effect("change", "customers", 2, scope="brothel", scales_with="district"), Effect("change", "mood modifier", -1)], description="On a blue moon, people feel depressed and lonely. Many look for company in the town's brothels.", sound = s_crowd_cheer),
                 4 : Moon("blood", effects=[Effect("boost", "crazy", 1, scope="brothel"), Effect("change", "threat", 2, scales_with = "district")], description="Something about this moon drives otherwise normal people crazy. Violent crimes always peak during this month.", sound = s_fire),
                 5 : Moon("honey", effects=[Effect("boost", "love gains", 1, scope="world"), Effect("boost", "fear gains", -0.5, scope="world")], description="A favorite month for lovers to elope together, their passion bright and short-lived as a spring flower.", sound = s_potion),
                 6 : Moon("dry", effects=[Effect("change", "job obedience target", -15, scope="brothel"), Effect("boost", "job customer budget", 0.1, scope="brothel"), Effect("change", "whore obedience target", 15, scope="brothel"), Effect("change", "train obedience target", 15, scope="brothel")], description="The dry moon is nothing special, quite boring really. People would rather tend to the task at hand than idly stare at this dull moon.", sound = s_sigh),
                 7 : Moon("hunter", effects=[Effect("boost", "quest rewards", 1, scope="brothel"), Effect("boost", "class results", 1, scope="brothel"), Effect("boost", "contract rewards", 0.5, scope="brothel"), Effect("boost", "income", -0.25, scope="brothel")], description="Hunting season is at its peak. This month was especially holy to the elder races.", sound = s_sheath),
                 8 : Moon("harvest", effects=[Effect("boost", "farm preference increase", 1, scope="farm"), Effect("boost", "all sex acts preference increase", -0.5, scope="brothel")], description="It's time for your girls to harvest your crops, tend to your cattle, and learn animal husbandry... with a twist!", sound = s_moo),
                 9 : Moon("silver", effects=[Effect("change", "mana", 1, scope="brothel", scales_with="spirit")], description="The silver moon is at its peak magical energy. Experienced spellcasters are careful to cast their most powerful spells and invocations on this month.", sound = s_spell),
                 10 : Moon("wet", effects=[Effect("change", "whore obedience target", -15, scope="brothel"), Effect("change", "train obedience target", -15, scope="brothel"), Effect("boost", "whore customer budget", 0.1, scope="brothel"), Effect("boost", "customer events", 1, scope="brothel"), Effect("boost", "dirt", 0.25)], description="The water spirits grant the moon a surreal quality this month. It is said to make everyone loosen up a little.", sound = s_mmh),
                 11 : Moon("hallow", effects=[Effect("boost", "threat", 0.3, scope="brothel"), Effect("boost", "crazy", 2, scope="brothel"), Effect("change", "customer defense", 2, scope="brothel")], description="This pagan holly month is the time of the year when monsters and spirits thrive, and the kids in Zan play 'Tricks or Tits'.", sound = s_maniacal_laugh),
                 12 : Moon("dark", effects=[Effect("boost", "love gains", -0.5, scope="world"), Effect("boost", "fear gains", 1, scope="world")], description="Under a dark moon, everything seems more frightening. This is the darkest of winter, only broken by the season festival Zan people call H-mas.", sound = s_mystery),
                }
    return

#### END OF BK SPELLS FILE ####
