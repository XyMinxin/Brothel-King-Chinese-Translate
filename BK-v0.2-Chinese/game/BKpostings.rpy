#### BK QUESTS AND CLASSES ####
## Labels are used instead of Functions to make sure we are using global variables

label init_postings():
    python:
        # QUESTS #

        quest_templates = [
                        Quest("quest", name = '模特需求', main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = "我是个艺术家，我告诉你，我是个艺术家！服装什么的不需要，我需要的是灵感。", sound = s_sigh),
                        Quest("quest", name = '私人舞者', main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = "寻找一个私人的，亲密的舞者……", sound = s_sigh),
                        Quest("quest", name = '招待我的客人', main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = "我的客人马上就到，什么也没准备好! 这是一场灾难! 我需要你的帮助！", sound = s_sigh),
                        Quest("quest", name = '陪同需求', main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = "我有一个重要的公会会议，我需要向他们展示我不是普通人. 寻找一个精英伴侣来打动那些势利小人.", sound = s_sigh),
                        Quest("quest", name = '回忆时光', main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'sex', description = "自从很多个月前我的鸡巴'睡过去'以来……我就非常期待一个女孩来帮我回忆起过去的时光……", sound = s_aaha),
                        Quest("quest", name = '创造纪录', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'anal', description = "我的目标是打破Long Dick Silver创造的记录，这需要长时间的练习……帮助我变得更强，更有力，这样我才有可能成功！", sound = s_aaha),
                        Quest("quest", name = '征求临时女友', main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'service', description = "我感到孤独……你能帮我忘记烦恼吗？", sound = s_aaha),
                        Quest("quest", name = '找帮手', main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = "我需要一个额外的女佣来帮忙打理这幢大厦。需要穿上一种非常特别的制服……", sound = s_aaha),
                        Quest("quest", name = '家庭教师', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'service', description = "我儿子已经21岁了，还没有结婚。说到女人，他就是个大笨蛋……你能帮他摆脱困境吗？", sound = s_mmmh),
                        Quest("quest", name = '无聊的瓒城', main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'sex', description = "我被困在这里，整天在当地的酒吧里喝啤酒。我烦死了。请给我找些“乐子”。", sound = s_mmmh),
                        Quest("quest", name = '后门男人', main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'anal', description = "男人们不知道，但小女孩都明白……", sound = s_mmmh),
                        Quest("quest", name = '地牢之夜', main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'fetish', description = "寻找小伙伴来帮助我们测试我们的新装置。来吧！会很有趣的！", sound = s_mmmh),
                        Quest("quest", name = '私人派对', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'group', description = "在我家接待一个庞大的代表团. 我需要女孩们用各种可能的方式招待我们的客人……", sound = s_aah),
                        Quest("quest", name = '女士之夜', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'group', description = "我们将在当地的会馆举行传统的“女士之夜”. 在观众面前找一个女孩和朋友一起玩……", sound = s_aah),
                        ]

        # CLASSES #

        class_templates = [
                            Quest("class", name = '造型培训', main_stat = 'Beauty', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'model', description = "学习秘诀，让自己在任何时候看起来美丽动人，拥有完美的头发！谁不想看起来更自然呢？", sound = s_sigh),
                            Quest("class", name = '舞蹈培训', main_stat = 'Body', second_stat = 'Constitution', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'dance', description = "Zomba! Bodyfighting! Aqua reggeaton!\n快点，别再编出更傻的名字了！", sound = s_sigh),
                            Quest("class", name = '服务培训', main_stat = 'Charm', second_stat = 'Obedience', other_stats = ("Beauty", "Body", "Refinement"), tags = 'waitress', description = "学习服务工作的基本知识……除非你愿意，否则你再也不会把杯子洒到顾客的胯部了！", sound = s_sigh),
                            Quest("class", name = '艺伎培训', main_stat = 'Refinement', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Charm"), tags = 'geisha', description = "掌握所有的传统艺术，包括茶道中的精确科学. 不要因为你的茶杯向左偏离了5度而看起来像个乡下姑娘!", sound = s_sigh),
                            Quest("class", name = '按摩培训', main_stat = 'Libido', second_stat = 'Sensitivity', other_stats = ("Beauty", "Body", "Refinement"), tags = 'masseuse', description = "和我们一起在温泉放松几天。那太棒了！至于教学……等等，什么教学？", sound = s_aaha),
                            Quest("class", name = '游泳培训', main_stat = 'Constitution', second_stat = 'Libido', other_stats = ("Body", "Charm", "Refinement"), tags = 'swim', description = "阳光照在裸露的身体上……水沿着撩人的曲线流淌……晒黑油在闪亮的皮肤上……然还有游泳。嗯。", sound = s_aaha),
                            Quest("class", name = '歌唱培训', main_stat = 'Sensitivity', second_stat = 'Obedience', other_stats = ("Beauty", "Charm", "Refinement"), tags = 'sing', description = "“哼，该死，要不我就扯掉你的脑袋，把粪塞到你脖子上！”歌唱课能有多糟糕？哦，你会见识到的……", sound = s_aaha),
                            Quest("class", name = '女仆培训', main_stat = 'Obedience', second_stat = 'Constitution', other_stats = ("Beauty", "Body", "Charm"), tags = 'maid', description = "“如果你想要学会正确地清理，你必须更多的弯下腰！更多……更多……嗯，那是更好的。”", sound = s_aaha),
                            Quest("class", name = '特殊服务培训', main_stat = 'Service', second_stat = 'Sex', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = "学会取悦男人……或者一个女人，如果你愿意的话. 为什么不两者都学呢？", sound = s_aah),
                            Quest("class", name = '性服务培训', main_stat = 'Sex', second_stat = 'Anal', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'XXX', description = "学会取悦男人……或者一个女人，如果你愿意的话. 为什么不两者都学呢？", sound = s_aah),
                            Quest("class", name = '恋物癖培训……', main_stat = 'Anal', second_stat = 'Fetish', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = "我们的工具不比五金店少，野兽比皇家动物园还多……当我们结束的时候，他们都会融入她的内心！", sound = s_scream),
                            Quest("class", name = 'SM……', main_stat = 'Fetish', second_stat = 'Service', other_stats = ("Libido", "Constitution", "Obedience", "Sensitivity"), tags = 'hardcore', description = "我们的工具不比五金店少，野兽比皇家动物园还多……当我们结束的时候，他们都会融入她的内心！", sound = s_scream),
                            ]

    return

#### END OF BK POSTINGS FILE ####
