#### BK SPELLS AND MOONS ####
## Labels are used instead of Functions to make sure we are using global variables

## SPELLS ##

label init_spells():

    python:


        # SPECIAL SPELLS AND SPELL EFFECTS #

        shield_effect = Effect("special", "shield", value = 1) #Individual shield, unused as of v0

        bshield_effect = Effect("special", "shield", value = 1, scope = "brothel")

        bshield_spell = Spell('魔法盾', 'shield.webp', type="shield", level=4, cost=2, effects=[bshield_effect], description="用一个神奇的屏障保护你的女孩免受外部威胁。阻止下一次侵犯你女孩的行为发生。持续到下一次攻击。")

        # REGULAR SPELLS #

        spellbook = {
                    "战士" : [
                            Spell('举重训练', 'strength.jpg', level=2, effects=[Effect("gain", "strength", 1)], description="力量就是一切."),
                            Spell('守护者', 'defender.webp', type="passive", level=3, effects=[Effect("special", "defender", 1)], description="你可以无处不在。"),
                            Spell('纪律', 'discipline.webp', type="discipline", level=4, cost=1, effects=[Effect("change", "train obedience target", -10, scope="brothel"), Effect("change", "job obedience target", -10, scope="brothel")], duration="turn", description="纪律的痛苦与失望的痛苦完全不同。"),
                            Spell('武士精神', 'spirit.webp', level=6, effects=[Effect("gain", "spirit", 1)], description="必须通过你心眼去正视他。"),
                            Spell('召唤血猎犬', 'hound.webp', type="summon", level=8, cost=2, effects=[Effect("change", "fight challenges", 6, dice=True)], duration="turn", description="召唤一只可怕的猎犬来帮助你作战。"),
                            Spell('秘诀', 'strength.jpg', level=10, effects=[Effect("gain", "strength", 1)], description="我会找到你，再干掉你。两次。"),
                            Spell('训练日', 'training.webp', type="training", level=12, cost=3, effects=[Effect("boost", "body gains", 0.05, scales_with="charisma", scope="brothel"), Effect("boost", "constitution gains", 0.05, scales_with="charisma", scope="brothel")], duration="turn", description="平时多流汗，战时少流血。"),
                            Spell('威风凛凛', 'charisma.jpg', level=14, effects=[Effect("gain", "charisma", 1)], description="从战场到青楼，你从未失去过这种气势"),
                            Spell('召唤凤凰', 'phoenix.webp', type="summon", level=16, cost=4, effects=[Effect("boost", "energy when resting", 0.25, scope="brothel")], duration="turn", description="召唤一只神奇的小鸟，它舒缓的歌声能帮助你的女孩放松。"),
                            Spell('虎视眈眈', 'strength.jpg', level=18, effects=[Effect("gain", "strength", 1)], description="ADRIAAAAAN！！！"),
                            Spell('召唤野兽图腾', 'bear.webp', type="summon", level=20, cost=5, effects=[Effect("change", "job customer capacity", 2, scope="brothel"), Effect("change", "whore customer capacity", 1, scope="brothel")], duration="turn", description="召唤一个野兽图腾，给你的女孩注入超自然的力量。"),
                            Spell('闪电反射', 'speed.jpg', level=22, effects=[Effect("gain", "speed", 1)], description="如眼镜蛇一般敏捷。"),
                            Spell('青楼卫队', 'militia.webp', type="passive", level=24, effects=[Effect("boost", "defense", 2, scope="brothel")], description="男人的战场! 呃……或者叫“女人的战场”？"),
                            ],
                    "奸商" : [
                            Spell('地痞流氓', 'charisma.jpg', level=2, effects=[Effect("gain", "charisma", 1)], description="我一天来一回，你记住了吗？"),
                            Spell('讨价还价', 'haggler.jpg', type="passive", level=3, effects=[Effect("boost", "buy", -0.02, scales_with="charisma"), Effect("boost", "sell", 0.02, scales_with="charisma")], description="“算了，我换家看看……” 只为了更好的价格。"),
                            Spell('信任符咒', 'sign1.webp', type="sign", level=4, cost=1, effects=[Effect("boost", "love gains", 0.1, scope="brothel"), Effect("boost", "fear gains", 0.1, scope="brothel")], duration="turn", description="信任是靠赢得的。除非你懂魔法。"),
                            Spell('街头霸王', 'strength.jpg', level=6, effects=[Effect("gain", "strength", 1)], description="博尔格卑鄙的街道让你了解了所有关于街头斗殴的知识：总是从背后捅刀子。"),
                            Spell('天方夜谭', 'tale.webp', type="tales", level=8, cost=2, effects=[Effect("boost", "prestige", 0.1, scope="brothel")], duration="turn", description="故事不错，兄弟。"),
                            Spell('冒险家', 'charisma.jpg', level=10, effects=[Effect("gain", "charisma", 1)], description="你并不总是远离你的床去冒险，但至少你看起来很适合。"),
                            Spell('信心符咒', 'sign2.webp', type="sign", level=12, cost=3, effects=[Effect("boost", "charm gains", 0.05, scales_with="charisma", scope="brothel"), Effect("boost", "libido gains", 0.05, scales_with="charisma", scope="brothel")], duration="turn", description="你是完美的，你不需要任何人的验证，但在这里，可以用这个咒语以防万一。"),
                            Spell('处世导师', 'spirit.webp', level=14, effects=[Effect("gain", "spirit", 1)], description="我在兰坎雨林的亚马逊部落生活了几个月。想知道他们是怎么做的吗?"),
                            Spell('花言巧语', 'girl.webp', type="city", level=16, cost=4, effects=[Effect("boost", "love gains", 0.3, scope="city")], duration="turn", description="你可以通过嘴巴抓住他们的心，你可以凭借这达到任何目的。"),
                            Spell('犯罪高手', 'charisma.jpg', level=18, effects=[Effect("gain", "charisma", 1)], description="害你的凶手是一个……"),
                            Spell('贪婪符咒', 'sign3.webp', type="sign", level=20, cost=5, effects=[Effect("boost", "total upkeep", -0.2, scope="brothel")], duration="turn", description="贪婪是好事。至少我的魔法书是这么说。"),
                            Spell('暗影行者', 'speed.jpg', level=22, effects=[Effect("gain", "speed", 1)], description="你跑得很快。你有一艘威斯特玛号，能在不到十二秒的时间里航行的船……在某个地方。"),
                            Spell('名扬四海', 'fame.webp', type="passive", level=24, effects=[Effect("change", "customers", 1, scales_with="charisma", scope="brothel")], description="名声，让人掌控一切！"),

                            ],
                    "法师" : [
                            Spell('好奇', 'spirit.webp', level=2, effects=[Effect("gain", "spirit", 1)], description="A beautiful mind. Pity about your face, though!"),
                            Spell('小光环:纯洁', 'aura1.webp', type="aura", level=2, cost=1, effects=[Effect("change", "beauty", 5, scope="brothel")], duration="turn", description="外表不能代表一切，但是，嘿，他们很有卖点。这种气质让你的女孩看起来更漂亮。"),
                            Spell('小光环:激发', 'aura4.webp', type="aura", level=2, cost=1, effects=[Effect("change", "body", 5, scope="brothel")], duration="turn", description="依靠摇动赚钱的人.现在有了魔力。这个光环增强了你的女孩的身材。"),
                            Spell('小光环:神秘', 'aura2.webp', type="aura", level=2, cost=1, effects=[Effect("change", "charm", 5, scope="brothel")], duration="turn", description="你女孩的周围散发着神秘气氛让顾客们回来了。 这种光环增强了女孩的魅力。"),
                            Spell('小光环:老练', 'aura3.webp', type="aura", level=2, cost=1, effects=[Effect("change", "refinement", 5, scope="brothel")], duration="turn", description="一个真正的魔法师才能使粗野的奴隶看起来老练。这个光环让你的女孩更优雅。"),
                            Spell('魔法之祖', 'sorcerer.webp', type="passive", level=3, effects=[Effect("boost", "mana", 1)], description="下魔力之雨了!哈利路亚。"),
                            Spell('魔法盾', 'shield.webp', type="shield", level=4, cost=2, effects=[bshield_effect], description="用魔法屏障保护你的女孩免受外部威胁。阻止下一个侵犯你姑娘的行为发生。持续到下一次攻击。"),
                            Spell('小光环: 淫欲', 'halo1.webp', type="halo", level=5, cost=3, effects=[Effect("change", "libido", 5, scope="brothel")], duration="turn", description="这里越来越热了……这个光环增强了姑娘们的性欲。"),
                            Spell('小光环: 卑屈', 'halo3.webp', type="halo", level=5, cost=3, effects=[Effect("change", "obedience", 5, scope="brothel")], duration="turn", description="跪下来，蛆虫们!这让姑娘们更听话。"),
                            Spell('小光环: 通感', 'halo2.webp', type="halo", level=5, cost=3, effects=[Effect("change", "sensitivity", 5, scope="brothel")], duration="turn", description="温柔的低语回荡在你女儿的耳边，让她们期待地颤抖。增加了他们的敏感性。"),
                            Spell('小光环: 坚忍', 'halo4.webp', type="halo", level=5, cost=3, effects=[Effect("change", "constitution", 5, scope="brothel")], duration="turn", description="就好像能量正从清新的空气中渗出。小幅提高姑娘们的体质。"),
                            Spell('聪明', 'charisma.jpg', level=6, effects=[Effect("gain", "charisma", 1)], description="这是对那些叫你“聪明人”的人的回报。"),
                            Spell('魔法仆役', 'servants.webp', type="spell", level=7, cost=3, effects=[Effect("instant", "dirt", -50, scales_with="spirit")], duration="turn", description="在童话故事中，他们没有会跳舞的假阳具柜子。"),
                            Spell('治愈之风', 'heal.webp', type="mist", level=8, cost=4, effects=[Effect("instant", "heal", 1, 0.5, scope="brothel", scales_with="spirit")], duration="turn", description="医生!这雾有机会完全治愈你的姑娘们。"),
                            Spell('光环: 纯洁', 'aura1b.webp', type="aura", level=9, cost=5, effects=[Effect("change", "beauty", 2, scales_with="spirit", scope="brothel")], duration="turn", description="外表不能代表一切，但是，他们确实有卖点。这种气质会让你的女孩看起来更漂亮。"),
                            Spell('光环: 激发', 'aura4b.webp', type="aura", level=9, cost=5, effects=[Effect("change", "body", 2, scales_with="spirit", scope="brothel")], duration="turn", description="让你的摇钱树动起来。现在通过魔力，这种光环会极大地增强你的女孩的身材。"),
                            Spell('光环: 神秘', 'aura2b.webp', type="aura", level=9, cost=5, effects=[Effect("change", "charm", 2, scales_with="spirit", scope="brothel")], duration="turn", description="你女孩的周围散发着神秘气氛让顾客们回来了。这种氛围会大大提升你的女孩的魅力。"),
                            Spell('光环: 老练', 'aura3b.webp', type="aura", level=9, cost=5, effects=[Effect("change", "refinement", 2, scales_with="spirit", scope="brothel")], duration="turn", description="一个真正的魔法师才能使粗野的奴隶看起来老练。这个光环让你的女孩更优雅。"),
                            Spell('创意', 'spirit.webp', level=10, effects=[Effect("gain", "spirit", 1)], description="现在，谁会想到用魔杖来做这件事……"),
                            Spell('强化感官', 'enhanced.webp', type="transe", level=11, cost=6, effects=[Effect("boost", "refinement gains", 0.05, scales_with="spirit", scope="brothel"), Effect("boost", "sensitivity gains", 0.05, scales_with="charisma", scope="brothel")], duration="turn", description="现在，你知道有第五维度吗？第六，第七，第十三？"),
                            Spell('人形师', 'doll.webp', type="transe", level=11, cost=6, effects=[Effect("boost", "beauty gains", 0.05, scales_with="spirit", scope="brothel"), Effect("boost", "obedience gains", 0.05, scales_with="charisma", scope="brothel")], duration="turn", description="我看见人们把针扎进巫毒娃娃里，但从来没有人在{i}那儿{/i}扎过针……"),
                            Spell('光环: 淫欲', 'halo1b.webp', type="halo", level=12, cost=8, effects=[Effect("change", "libido", 2, scales_with="spirit", scope="brothel")], duration="turn", description="这个光环给了你的女孩们很大的动力。"),
                            Spell('光环: 卑屈', 'halo3b.webp', type="halo", level=12, cost=8, effects=[Effect("change", "obedience", 2, scales_with="spirit", scope="brothel")], duration="turn", description="“跪下来，蛆虫们！”，这会让姑娘们更听话。"),
                            Spell('光环: 通感', 'halo2b.webp', type="halo", level=12, cost=8, effects=[Effect("change", "sensitivity", 2, scales_with="spirit", scope="brothel")], duration="turn", description="温柔的低语回荡在你女儿的耳边，让她们期待地颤抖。这大大提高了她们的敏感。"),
                            Spell('光环: 坚忍', 'halo4b.webp', type="halo", level=12, cost=8, effects=[Effect("change", "constitution", 2, scales_with="spirit", scope="brothel")], duration="turn", description="就好像能量正从清新的空气中渗出。大幅提高姑娘们的体质。"),
                            Spell('执杖大师', 'strength.jpg', level=14, effects=[Effect("gain", "strength", 1)], description="如果所有这些都失败了，你仍然可以用它敲碎他们的头骨。"),
                            Spell('回春', 'hand.webp', type="mist", level=16, cost=9, effects=[Effect("gain", "energy", 5, scope="brothel", scales_with="spirit")], duration="turn", description="这舒缓的薄雾让你的女儿们得到了舒缓，除了桃色的香味这么点算不上副作用的情况。"),
                            Spell('疯狂', 'spirit.webp', level=18, effects=[Effect("gain", "spirit", 1)], description="完全的疯狂和毁灭性的力量，他们总是很好的组合。"),
                            Spell('魔尘', 'fairy.webp', type="form", level=20, cost=9, effects=[Effect("special", "fairy form", 1)], duration="turn", description="你扮演着神秘、空灵的仙人。依靠你的精神而不是你的魅力。"),
                            Spell('龙魂', 'dragon.webp', type="form", level=20, cost=9, effects=[Effect("special", "dragon form", 1)], duration="turn", description="你呈现出一种可怕的龙形。用你的精神代替你的力量。"),
                            Spell('极乐世界', 'ghost.webp', type="enchant", level=22, cost=10, effects=[Effect("increase satisfaction", "all jobs", 1, scope="brothel"), Effect("increase satisfaction", "all sex acts", 1, scope="brothel")], duration="turn", description="那是一种魔法……不是你童话里说的那种魔法."),
                            Spell('极速', 'speed.jpg', level=22, effects=[Effect("gain", "speed", 1)], description="我裤子里有魔法. 我是说，它们能让我跑得更快。"),
                            Spell('魔眼', 'eye.webp', type="passive", level=24, effects=[Effect("special", "snake eyes", 1)], description="从一个叫索伦的家伙那里学来的。一个不错的小伙子。催眠的尝试总是会成功。"),
                            Spell('精神控制', 'mindtrick.webp', type="trick", level=24, cost=10, effects=[Effect("boost", "job customer budget", 0.25, scope="brothel"), Effect("boost", "whore customer budget", 0.25, scope="brothel")], description="从一个叫欧比万的老流浪汉那里学会了这个把戏。不过他擅长护送德鲁伊。"),
                            ],
                    }

    return


## MOONS ##

label init_moons():
    python:
        moons = {
                 1 : Moon("金", pic="gold", effects=[Effect("boost", "income", value = 0.5, scope = "brothel")], description="新的一年在Xeros刚刚开始! 这是一年中最重要的节日。人们被鼓励花大钱来炫耀他们的好运气。", sound = s_gold),
                 2 : Moon("狼", pic="wolf", effects=[Effect("boost", "city rewards", 1, scope="brothel"), Effect("change", "city rewards", 1, scope="brothel"), Effect("boost", "resource extraction", 1, scope="brothel")], description="这个月是一年中最冷的时候。据说勇敢面对这个艰难季节的冒险家可以收获最好的回报。", sound = s_wolf),
                 3 : Moon("蓝", pic="blue", effects=[Effect("change", "customers", 2, scope="brothel", scales_with="district"), Effect("change", "mood modifier", -1)], description="在蓝色的月光映照下，人们感到沮丧和孤独。许多人在镇上的青楼寻找同伴。", sound = s_crowd_cheer),
                 4 : Moon("血", pic="blood", effects=[Effect("boost", "crazy", 1, scope="brothel"), Effect("change", "threat", 2, scales_with = "district")], description="这个月亮的某种神秘力量能让正常人发疯。暴力犯罪总是在这个月达到高峰。", sound = s_fire),
                 5 : Moon("密", pic="honey", effects=[Effect("boost", "love gains", 1, scope="world"), Effect("boost", "fear gains", -0.5, scope="world")], description="恋人最喜欢在这个月一起私奔，他们的激情像春天的花朵一样明亮而短暂。", sound = s_potion),
                 6 : Moon("枯", pic="dry", effects=[Effect("change", "job obedience target", -15, scope="brothel"), Effect("boost", "job customer budget", 0.1, scope="brothel"), Effect("change", "whore obedience target", 15, scope="brothel"), Effect("change", "train obedience target", 15, scope="brothel")], description="暗淡的月亮没有什么特别之处，真的相当无聊。人们宁可倾向于手头的工作，而不是闲着无聊地盯着这轮无趣的月亮。", sound = s_sigh),
                 7 : Moon("狩", pic="hunter", effects=[Effect("boost", "quest rewards", 1, scope="brothel"), Effect("boost", "class results", 1, scope="brothel"), Effect("boost", "contract rewards", 0.5, scope="brothel"), Effect("boost", "income", -0.25, scope="brothel")], description="狩猎季节正处于高峰期。这个月对长寿种族来说特别神圣。", sound = s_sheath),
                 8 : Moon("农", pic="harvest", effects=[Effect("boost", "farm preference increase", 1, scope="farm"), Effect("boost", "all sex acts preference increase", -0.5, scope="brothel")], description="现在是时候收获你的庄稼，照料你的牛，找到一个伙伴，并狠狠抽她一顿", sound = s_moo),
                 9 : Moon("银", pic="silver", effects=[Effect("change", "mana", 1, scope="brothel", scales_with="spirit")], description="银色的月亮正处于魔法能量的顶峰。有经验的施法者会在这个月小心翼翼地施展他们最强大的法术和召唤。", sound = s_spell),
                 10 : Moon("水", pic="wet", effects=[Effect("change", "whore obedience target", -15, scope="brothel"), Effect("change", "train obedience target", -15, scope="brothel"), Effect("boost", "whore customer budget", 0.1, scope="brothel"), Effect("boost", "customer events", 1, scope="brothel"), Effect("boost", "dirt", 0.25)], description="水精灵在这个月赋予月亮一种超现实的特质。据说这能使每个人都放松一些。", sound = s_mmh),
                 11 : Moon("皎", pic="hallow", effects=[Effect("boost", "threat", 0.3, scope="brothel"), Effect("boost", "crazy", 2, scope="brothel"), Effect("change", "customer defense", 2, scope="brothel")], description="这个异教徒赞美的皎月是一年中怪兽和精灵繁盛的时节。此外，也是瓒城的孩子玩“小把戏还是乳头”节目的好日子。", sound = s_maniacal_laugh),
                 12 : Moon("暗", pic="dark", effects=[Effect("boost", "love gains", -0.5, scope="world"), Effect("boost", "fear gains", 1, scope="world")], description="在黑暗的月光下，一切都显得更加可怕。这这是最黑暗的冬天，只有一个瓒城当地人专门为破除这个季节应运而生的节日，叫H-mas。", sound = s_mystery),
                }
    return

#### END OF BK SPELLS FILE ####
