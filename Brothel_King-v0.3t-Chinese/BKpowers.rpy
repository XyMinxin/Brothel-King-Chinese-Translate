init python:

    def init_powers(): # Initiates all objects and values for evil powers
        global evpower_deck
        global evpower_list
        global evpower_super_list
        global evpower_dict
        global evpower_super_dict
        global evpower_color
        global evil_card_size

        evpower_list =  [
                            EvilPower(name='Summon cuddly pet', type='Platinum', power='chaos', target='MC', short_description='召唤一只非常可爱，十分正常和安全的宠物', mojo_cost=[('green', 2), ('blue', 2), ('red', 2), ('yellow', 2)], sanity_cost=2),
                            EvilPower(name='Ritual orgy', type='Platinum', power='ritual orgy', target='brothel', short_description='让青楼一夜暴富, 消耗大量理智', mojo_cost=[('green', 1), ('blue', 2), ('red', 2), ('yellow', 1)], sanity_cost=6),
                            EvilPower(name='Ritual bondage', type='Platinum', power='ritual bondage', target='all girls', effects=[Effect("gain", "obedience", 6, dice=1), Effect("gain", "libido", 6, dice=1)], short_description='消耗大量理智，立刻提升所有女孩的服从和性欲属性', mojo_cost=[('green', 2), ('blue', 1), ('red', 1), ('yellow', 2)], sanity_cost=6),
                            EvilPower(name='Ritual violence', type='Platinum', power='ritual violence', target='all girls', effects=[Effect("gain", "fear", 4, dice=1)], short_description='消耗大量理智，立刻提升所有女孩的恐惧值产出', mojo_cost=[('red', 6)], sanity_cost=6),
                            EvilPower(name='Forget', type='Platinum', power='perks', target='conduit', short_description='重置所有C阶及以上女孩的天赋', mojo_cost=[('green', 2), ('blue', 2), ('red', 2), ('yellow', 2)], sanity_cost=4),
                            EvilPower(name='Horror visions', type='Gold', power='fear boost', target='all girls', effects=[Effect("boost", "fear gains", 0.25, scope="brothel")], short_description='所有女孩的恐惧值增长更快', mojo_cost=[('yellow', 5)], sanity_cost=4, duration=5),
                            EvilPower(name='Soul change', type='Gold', power='personality', target='conduit', short_description='随机改变她的性格', mojo_cost=[('blue', 5)], sanity_cost=4),
                            EvilPower(name='Unholy stamina', type='Gold', power='customer capacity', target='brothel', effects=[Effect("change", "job customer capacity", 2, scope="brothel"), Effect("change", "whore customer capacity", 1, scope="brothel")], short_description='提升所有岗位的女孩服务客人的能力', mojo_cost=[('green', 5)], sanity_cost=3, duration=5),
                            EvilPower(name='Weak point', type='Gold', power='negative trait', target='conduit', short_description='把女孩的负面特质换成一个新的随机特质', mojo_cost=[('blue', 5)], sanity_cost=3),
                            EvilPower(name='Brand', type='Gold', power='slave', target='conduit', short_description='把她变成奴隶(仅能对自由女孩使用)', mojo_cost=[('green', 3)], sanity_cost=4),
                            EvilPower(name='Satisfaction guaranteed', type='Gold', power='customer satisfaction', target='brothel', effects=[Effect("increase satisfaction", "all jobs", 1, scope="brothel"), Effect("increase satisfaction", "all sex acts", 1, scope="brothel")], short_description="所有顾客满意度+1", mojo_cost=[('green', 1), ('blue', 1), ('red', 1), ("yellow", 1)], sanity_cost=4, duration=4),
                            EvilPower(name='Dynamo', type='Gold', power='energy', target='brothel', short_description='消耗她的精力来为所有妓院女孩恢复一些精力，', mojo_cost=[('red', 4)], sanity_cost=3),
                            EvilPower(name='Pain is the lesson', type='Gold', power='postings', target='conduit', effects=[Effect("boost", "quest rewards", 0.5), Effect("boost", "class results", 0.5)], short_description='她能从任务和培训课程中得到更多收益', mojo_cost=[('red', 1), ('yellow', 2)], sanity_cost=3, duration=7, activation_limit="girl"),
                            EvilPower(name='Frenzy', type='Silver', power='frenzy', target='conduit', effects=[Effect("special", "ignore energy", 1)], short_description='她可以不消耗精力工作一段时间，随后立刻精疲力竭', mojo_cost=[('green', 4)], sanity_cost=2, duration=3, activation_limit="girl"),
                            EvilPower(name='Warp farm', type='Silver', power='farm', target='conduit', effects=[Effect("boost", "farm preference increase", 1.0), Effect("boost", "farm fear generation", 1.0)], short_description='提高她的农场训练和恐惧产出效果', mojo_cost=[('green', 1), ('blue', 1), ('red', 1), ('yellow', 1)], sanity_cost=2, duration=7, activation_limit="girl"),
                            EvilPower(name='Leech reputation', type='Silver', power='leech rep', target='other girl', short_description='她的一些声望会转移到另一个阶级相同或更低的女孩身上', mojo_cost=[('blue', 2), ('red', 2)], sanity_cost=2),
                            EvilPower(name='Stigmata', type='Silver', power='hurt', target='other girl', short_description='让她来承受另一个女孩的伤痛并治愈她', mojo_cost=[('red', 3)], sanity_cost=3),
                            EvilPower(name='Dark fantasy: Bisexual', type='Silver', power='bisexual', target='conduit', short_description='增加她对双飞的接受能力', mojo_cost=[('green', 2), ('yellow', 2)], sanity_cost=2),
                            EvilPower(name='Dark fantasy: Group', type='Silver', power='group', target='conduit', short_description='增加她对群交的接受能力', mojo_cost=[('blue', 2), ('red', 2)], sanity_cost=2),
                            EvilPower(name='Blind obedience', type='Silver', power='obedience', target='conduit', effects=[Effect("change", "obedience target", -30), Effect("change", "sex acts requirements", -15)], short_description='她将更愿意接受工作和训练的安排', mojo_cost=[('yellow', 3)], sanity_cost=3, duration=3, activation_limit="girl"),
                            EvilPower(name='Leech xp', type='Silver', power='leech xp', target='all girls', short_description='把经验分给所有比她等级低的人', mojo_cost=[('green', 2), ('yellow', 2)], sanity_cost=2),
                            EvilPower(name='Leech jp', type='Silver', power='leech jp', target='all girls', short_description='把职业经验分给所有比她职业等级低的人', mojo_cost=[('blue', 2), ('red', 2)], sanity_cost=2),
                            EvilPower(name='Bad memories', type='Bronze', power='punish', target='all girls', effects=[Effect("boost", "punishment efficiency", 1, scope="brothel")], short_description='惩罚对其他女孩效果更好了', mojo_cost=[('yellow', 3)], sanity_cost=3, duration=7),
                            EvilPower(name='Apathy', type='Bronze', power='normalize fear', target='conduit', short_description='降低好感度和恐惧值等级，无论正负', mojo_cost=[('blue', 1), ('red', 1), ('yellow', 1)], sanity_cost=2),
                            EvilPower(name='Abduction', type='Bronze', power='kidnap', target='city girl', short_description='让她尝试绑架一个自由的女孩，她可能会在过程中受伤', description='She will go to the city at night and attempt capturing a free girl. Her chances improve with her defense level.', mojo_cost=[('yellow', 3)], sanity_cost=2),
                            EvilPower(name='Spread the love', type='Bronze', power='city love', target='location', short_description='抽取她所有的好感度，并提升特定地区的所有女孩的好感度', mojo_cost=[('blue', 3)], sanity_cost=2),
                            EvilPower(name='Change fixation', type='Bronze', power='negative fixation', target='conduit', short_description='将她的负面特质转化为另一个随机的负面特质', mojo_cost=[('yellow', 3)], sanity_cost=2),
                            EvilPower(name='Summon incubus', type='Bronze', power='prestige', target='conduit', short_description='召唤下级恶魔强奸她,随机提升一项性技能, 获得声望和经验值', mojo_cost=[('blue', 2)], sanity_cost=3),
                            EvilPower(name='Non Euclidean space', type='Bronze', power='room capacity', target='brothel', short_description='青楼的营业场所可以容纳更多的顾客', mojo_cost=[('red', 3)], sanity_cost=2, duration=5), # Effect is changed dynamically
                            EvilPower(name='Nature calls', type='Bronze', power='force naked', target='conduit', effects=[Effect("special", "naked", 1)], short_description='她将一直保持裸体', mojo_cost=[('green', 3)], sanity_cost=2, duration=5, activation_limit="girl"),
                            EvilPower(name='Vampire smile', type='Bronze', power='charisma', target='MC', effects=[Effect("change", "charisma", 1)], short_description='玩家魅力+1', mojo_cost=[('green', 3)], sanity_cost=2, duration=7),
                            EvilPower(name='Vampire swiftness', type='Bronze', power='speed', target='MC', effects=[Effect("change", "speed", 1)], short_description='玩家速度+1', mojo_cost=[('blue', 3)], sanity_cost=2, duration=7),
                            EvilPower(name='Vampire vigor', type='Bronze', power='strength', target='MC', effects=[Effect("change", "strength", 1)], short_description='玩家力量+1', mojo_cost=[('red', 3)], sanity_cost=2, duration=7),
                            EvilPower(name='Vampire mind', type='Bronze', power='spirit', target='MC', effects=[Effect("change", "spirit", 1)], short_description='玩家精神+1', mojo_cost=[('yellow', 3)], sanity_cost=2, duration=7),
                            EvilPower(name='Even out', type='Bronze', power='normalize skills BBCR', target='conduit', short_description="均匀分配她的部分属性 (外貌, 身材, 魅力和优雅)", description="Beauty, Body, Charm and Refinement skills converge on their average value", mojo_cost=[('green', 3)], sanity_cost=2),
                            EvilPower(name='Even out', type='Bronze', power='normalize skills LOCS', target='conduit', short_description="均匀分配她的部分属性 (性欲, 服从, 体质和敏感)", description="Libido, Obedience, Constitution and Sensitivity converge on their average value", mojo_cost=[('blue', 3)], sanity_cost=2),
                            EvilPower(name='Shuffle', type='Bronze', power='shuffle skills BBCR', target='conduit', short_description="随机分配她的部分属性 (外貌, 身材, 魅力和优雅)", description="Beauty, Body, Charm and Refinement skill values are shuffled randomly", mojo_cost=[('yellow', 3)], sanity_cost=2),
                            EvilPower(name='Shuffle', type='Bronze', power='shuffle skills LOCS', target='conduit', short_description="随机分配她的部分属性 (性欲, 服从, 体质和敏感)", description="Libido, Obedience, Constitution and Sensitivity skill values are shuffled randomly", mojo_cost=[('red', 3)], sanity_cost=2),
                            EvilPower(name='Mulligan', type='Bronze', power='mulligan', target='MC', short_description='重新抽取能力卡', mojo_cost=[('green', 2), ('blue', 2)], sanity_cost=1),
                            EvilPower(name='Mojo surge (yellow)', type='Regular', power='mojo yellow', target='MC', short_description='消耗大量理智换取2~6黄色魔力', mojo_cost=[('green', 1)], sanity_cost=3),
                            EvilPower(name='Mojo surge (red)', type='Regular', power='mojo red', target='MC', short_description='消耗大量理智换取2~6红色魔力', mojo_cost=[('yellow', 1)], sanity_cost=3),
                            EvilPower(name='Mojo surge (blue)', type='Regular', power='mojo blue', target='MC', short_description='消耗大量理智换取2~6蓝色魔力', mojo_cost=[('red', 1)], sanity_cost=3),
                            EvilPower(name='Mojo surge (green)', type='Regular', power='mojo green', target='MC', short_description='消耗大量理智换取2~6绿色魔力', mojo_cost=[('blue', 1)], sanity_cost=3),
                            EvilPower(name='Leech skills', type='Regular', power='leech service sex', target='other girl', short_description="将她的部分(侍奉和性交)经验转移给另一个女孩", description='Leeches some of her service and sex skills and transfers them to a girl of equal or lower rank', mojo_cost=[('green', 1), ('blue', 1)], sanity_cost=2),
                            EvilPower(name='Leech skills', type='Regular', power='leech anal fetish', target='other girl', short_description="将她的部分(肛交和调教)经验转移给另一个女孩", description='Leeches some of her anal and fetish skills and transfers them to a girl of equal or lower rank', mojo_cost=[('red', 1), ('yellow', 1)], sanity_cost=2),
                            EvilPower(name='Dark fantasy: Service', type='Regular', power='service', target='conduit', short_description='增加她对侍奉的接受能力', mojo_cost=[('green', 2)], sanity_cost=1),
                            EvilPower(name='Dark fantasy: Sex', type='Regular', power='sex', target='conduit', short_description='增加她对性交的接受能力', mojo_cost=[('blue', 2)], sanity_cost=1),
                            EvilPower(name='Dark fantasy: Anal', type='Regular', power='anal', target='conduit', short_description='增加她对肛交的接受能力', mojo_cost=[('red', 2)], sanity_cost=1),
                            EvilPower(name='Dark fantasy: Fetish', type='Regular', power='fetish', target='conduit', short_description='增加她对调教的接受能力', mojo_cost=[('yellow', 2)], sanity_cost=1),
                            EvilPower(name='Minion training', type='Regular', power='minion', target='minion', short_description='把经验分享给另一个人', mojo_cost=[('red', 1)], sanity_cost=1),
                            EvilPower(name='Connected minds', type='Regular', power='obedience link', target='other girl', short_description='选择一个女孩。降低她拒绝服从命令的概率', mojo_cost=[('green', 1), ('blue', 1)], sanity_cost=1, duration=5),
                            EvilPower(name='Leech skills', type='Regular', power='leech beauty body', target='other girl', short_description="将她的部分(外貌和身材)属性转移给另一个女孩", description='Leeches some of her beauty and body skills and transfers them to a girl of equal or lower rank', mojo_cost=[('blue', 1), ('red', 1)], sanity_cost=1),
                            EvilPower(name='Leech skills', type='Regular', power='leech charm refinement', target='other girl', short_description="将她的部分(魅力和优雅)属性转移给另一个女孩", description='Leeches some of her charm and refinement skills and transfers them to a girl of equal or lower rank', mojo_cost=[('green', 1), ('yellow', 1)], sanity_cost=1),
                            EvilPower(name='Leech skills', type='Regular', power='leech sensitivity constitution', target='other girl', short_description="将她的部分(敏感和体质)属性转移给另一个女孩", description='Leeches some of her sensitivity and constitution skills and transfers them to a girl of equal or lower rank', mojo_cost=[('green', 1), ('red', 1)], sanity_cost=1),
                            EvilPower(name='Leech skills', type='Regular', power='leech libido obedience', target='other girl', short_description="将她的部分(性欲和服从)属性转移给另一个女孩", description='Leeches some of her libido and obedience skills and transfers them to a girl of equal or lower rank', mojo_cost=[('blue', 1), ('yellow', 1)], sanity_cost=1),
                            EvilPower(name='Hallucination', type='Regular', power='hypnosis', target='conduit', effects=[Effect("change", "hypnosis", 3)], short_description='提高对她催眠的成功率', mojo_cost=[('yellow', 1)], sanity_cost=1, duration=5, activation_limit="girl"),
                            EvilPower(name='Fearful trade', type='Regular', power='mojo trade', target='MC', short_description='以2：1的比例将其他颜色魔力转换为紫色魔力', mojo_cost=[('green', 1)], sanity_cost=1),
                            EvilPower(name='Dark fantasy: Naked', type='Regular', power='naked', target='conduit', short_description='她会更容易接受裸体', mojo_cost=[('green', 1)], sanity_cost=1),
                            EvilPower(name='Oni', type='Regular', power='security', target='brothel', effects=[Effect("special", "demon security", 1, scope="brothel"), Effect("change", "security", 1, scope="brothel")], short_description='提升青楼安保效果', mojo_cost=[('red', 1)], sanity_cost=1, duration=5),
                            EvilPower(name='Haniwa', type='Regular', power='maintenance', target='brothel', effects=[Effect("special", "demon maintenance", 1, scope="brothel"), Effect("change", "maintenance", 1, scope="brothel")], short_description='提升青楼清洁效果', mojo_cost=[('yellow', 1)], sanity_cost=1, duration=5),
                            EvilPower(name='Demonette', type='Regular', power='advertising', target='brothel', effects=[Effect("special", "demon advertising", 1, scope="brothel"), Effect("change", "advertising", 1, scope="brothel")], short_description='提升青楼广告效果', mojo_cost=[('green', 1)], sanity_cost=1, duration=5),
                        ]

        evpower_super_list = [
                                EvilSuperPower(name='Summon cuddly pet', type='Platinum', power='chaos', target='MC', short_description='Summon this absolutely adorable and utterly HARMLESS not-at-all evil pet. Pinky swear.', mojo_cost=[('green', 5), ('blue', 5), ('red', 5), ('yellow', 5)], sanity_cost=666),
                                EvilSuperPower(name='Ritual orgy', type='Platinum', power='ritual orgy', target='brothel', short_description='Large gold generation for the brothel, instant loss of sanity.', mojo_cost=[('green', 2), ('blue', 3), ('red', 3), ('yellow', 2)], sanity_cost=666),
                                EvilSuperPower(name='Ritual bondage', type='Platinum', power='ritual bondage', target='all girls', effects=[Effect("gain", "obedience", 6, dice=2), Effect("gain", "libido", 6, dice=2)], short_description='Large gain of Obedience and Libido for all girls, instant loss of sanity.', mojo_cost=[('green', 3), ('blue', 2), ('red', 2), ('yellow', 3)], sanity_cost=666),
                                EvilSuperPower(name='Ritual violence', type='Platinum', power='ritual violence', target='all girls', effects=[Effect("gain", "fear", 4, dice=2)], short_description='Fear generation for all girls with a large mojo yield, instant loss of sanity.', mojo_cost=[('red', 10)], sanity_cost=666),
                                EvilSuperPower(name='Forget', type='Platinum', power='perks', target='conduit', short_description='Reset all perks and perk trees.', mojo_cost=[('green', 4), ('blue', 4), ('red', 4), ('yellow', 4)], sanity_cost=6),
                                EvilSuperPower(name='Horror visions', type='Gold', power='fear boost', target='all girls', effects=[Effect("boost", "fear gains", 0.25, scope="brothel"), Effect("special", "fear interactions", 1, scope="brothel")], short_description='Regular MC interactions generate Fear. Fear raises faster for all girls. Lasts 10 days.', mojo_cost=[('yellow', 10)], sanity_cost=5, duration=10),
                                EvilSuperPower(name='Soul change', type='Gold', power='personality', target='conduit', short_description='Alters her personality, you can influence the outcome.', mojo_cost=[('blue', 10)], sanity_cost=5),
                                EvilSuperPower(name='Unholy stamina', type='Gold', power='customer capacity', target='brothel', effects=[Effect("change", "job customer capacity", 2, scope="brothel"), Effect("change", "whore customer capacity", 1, scope="brothel")], short_description='Raises customer capacity for all working and whoring girls', mojo_cost=[('green', 10)], sanity_cost=5, duration=10),
                                EvilSuperPower(name='Weak point', type='Gold', power='negative trait', target='conduit', short_description='Girl swaps her negative Trait for a new one, you can influence the outcome', mojo_cost=[('blue', 10)], sanity_cost=5),
                                EvilSuperPower(name='Brand', type='Gold', power='slave', target='all girls', short_description='Turn all free girls in the brothel or farm into slaves', mojo_cost=[('green', 9)], sanity_cost=6),
                                EvilSuperPower(name='Satisfaction guaranteed', type='Gold', power='customer satisfaction', target='brothel', effects=[Effect("increase satisfaction", "all jobs", 2, scope="brothel"), Effect("increase satisfaction", "all sex acts", 2, scope="brothel")], short_description='+2 satisfaction for all customers', mojo_cost=[('green', 2), ('blue', 2), ('red', 2), ('yellow', 2)], sanity_cost=5, duration=7),
                                EvilSuperPower(name='Dynamo', type='Gold', power='energy', target='brothel', short_description='Restores her max energy level to all brothel girls, exhausts and hurts her', mojo_cost=[('red', 8)], sanity_cost=5),
                                EvilSuperPower(name='Pain is the lesson', type='Gold', power='postings', target='all girls', effects=[Effect("boost", "quest rewards", 0.5, scope="brothel"), Effect("boost", "class results", 0.5, scope="brothel")], short_description='All girls will receive more gains from classes and quests', mojo_cost=[('red', 2), ('yellow', 4)], sanity_cost=6, duration=7),
                                EvilSuperPower(name='Frenzy', type='Silver', power='frenzy', target='conduit', effects=[Effect("special", "ignore energy", 1)], short_description='She will be able to work without losing energy for a while, then get automatically exhausted', mojo_cost=[('green', 8)], sanity_cost=4, duration=7, activation_limit="girl"),
                                EvilSuperPower(name='Warp farm', type='Silver', power='farm', target='all girls', effects=[Effect("boost", "farm preference increase", 1.0, scope="farm"), Effect("boost", "farm fear generation", 1.0, scope="farm")], short_description='Farm training and fear generation will be more efficient for all girls', mojo_cost=[('green', 2), ('blue', 2), ('red', 2), ('yellow', 2)], sanity_cost=4, duration=7),
                                EvilSuperPower(name='Leech reputation', type='Silver', power='leech rep', target='other girl', short_description='All of her reputation will be transferred to another girl of lower or similar rank', mojo_cost=[('blue', 4), ('red', 4)], sanity_cost=4),
                                EvilSuperPower(name='Stigmata', type='Silver', power='hurt', target='all girls', short_description='She will absorb wounds from all girls and heal them', mojo_cost=[('red', 7)], sanity_cost=5),
                                EvilSuperPower(name='Dark fantasy: Bisexual', type='Silver', power='bisexual', target='conduit', short_description='Her Bisexual preference will increase (larger effect)', mojo_cost=[('green', 4), ('yellow', 4)], sanity_cost=3),
                                EvilSuperPower(name='Dark fantasy: Group', type='Silver', power='group', target='conduit', short_description='Her Group preference will increase (larger effect)', mojo_cost=[('green', 4), ('yellow', 4)], sanity_cost=3),
                                EvilSuperPower(name='Blind obedience', type='Silver', power='obedience', target='conduit', effects=[Effect("change", "obedience target", -70), Effect("change", "sex acts requirements", -35), Effect("special", "minimum preference", "very reluctant")], short_description='She is a lot less likely to refuse working, training or whoring', mojo_cost=[('yellow', 6)], sanity_cost=5, duration=3, activation_limit="girl"),
                                EvilSuperPower(name='Leech xp', type='Silver', power='leech xp', target='all girls', short_description='Share more XP with all girls of lesser level', mojo_cost=[('green', 4), ('yellow', 4)], sanity_cost=3),
                                EvilSuperPower(name='Leech jp', type='Silver', power='leech jp', target='all girls', short_description='Share more JP with all girls of lesser job level', mojo_cost=[('blue', 4), ('red', 4)], sanity_cost=3),
                                EvilSuperPower(name='Worse memories', type='Bronze', power='punish', target='all girls', effects=[Effect("boost", "punishment efficiency", 3, scope="brothel")], short_description='Punishment is a lot more efficient on all girls.', mojo_cost=[('red', 3), ('yellow', 3)], sanity_cost=4, duration=7),
                                EvilSuperPower(name='Apathy', type='Bronze', power='normalize fear', target='conduit', short_description='Love/Hate and Fear/Trust levels are set back to zero', mojo_cost=[('blue', 2), ('red', 2), ('yellow', 2)], sanity_cost=4),
                                EvilSuperPower(name='Abduction', type='Bronze', power='kidnap', target='city girl', short_description='Attempts to kidnap a free girl, may get hurt in the process. Higher success chances', description='She will go to the city at night and attempt capturing a free girl. Her chances improve with her defense level (supercharged: higher chance of success).', mojo_cost=[('yellow', 6)], sanity_cost=4),
                                EvilSuperPower(name='Spread the love', type='Bronze', power='city love', target='district', short_description='Leeches all of her Love and raises Love for all girls in the city', mojo_cost=[('blue', 6)], sanity_cost=4),
                                EvilSuperPower(name='Remove fixation', type='Bronze', power='negative fixation', target='conduit', short_description='Removes her negative fixation instantly. Exhausts her', mojo_cost=[('blue', 3), ('red', 3), ('yellow', 3)], sanity_cost=4),
                                EvilSuperPower(name='Summon incubus', type='Bronze', power='prestige', target='conduit', short_description='Summon large demon to fuck her, boosting two random sex skills, prestige and girl XP even more', mojo_cost=[('blue', 5)], sanity_cost=6),
                                EvilSuperPower(name='Non Euclidean space', type='Bronze', power='room capacity', target='brothel', short_description='Common rooms in the brothel can accomodate a lot more customers', mojo_cost=[('red', 6)], sanity_cost=4, duration=5),
                                EvilSuperPower(name='Nature calls', type='Bronze', power='force naked', target='conduit', effects=[Effect("special", "naked", 1), Effect("change", "beauty", 5), Effect("change", "body", 5), Effect("change", "charm", 5), Effect("change", "refinement", 5)], short_description='She will remain naked at all times. Temporary boost to main skills', mojo_cost=[('green', 6)], sanity_cost=3, duration=10, activation_limit="girl"),
                                EvilSuperPower(name='Vampire smile', type='Bronze', power='charisma', target='MC', effects=[Effect("change", "charisma", 2)], short_description='+2 to Main Character Charisma', mojo_cost=[('green', 6)], sanity_cost=3, duration=7),
                                EvilSuperPower(name='Vampire swiftness', type='Bronze', power='speed', target='MC', effects=[Effect("change", "speed", 2)], short_description='+2 to Main Character Speed', mojo_cost=[('blue', 6)], sanity_cost=3, duration=7),
                                EvilSuperPower(name='Vampire vigor', type='Bronze', power='strength', target='MC', effects=[Effect("change", "strength", 2)], short_description='+2 to Main Character Strength', mojo_cost=[('red', 6)], sanity_cost=3, duration=7),
                                EvilSuperPower(name='Vampire mind', type='Bronze', power='spirit', target='MC', effects=[Effect("change", "spirit", 2)], short_description='+2 to Main Character Spirit', mojo_cost=[('yellow', 6)], sanity_cost=3, duration=7),
                                EvilSuperPower(name='Even out', type='Bronze', power='normalize skills BBCR', target='conduit', short_description="Averages out some of her skills (Beauty, Body, Charm & Refinement), then receive a permanent skill boost", description="Beauty, Body, Charm and Refinement skills converge on their average value, then receive a permanent boost.", mojo_cost=[('green', 6)], sanity_cost=2),
                                EvilSuperPower(name='Even out', type='Bronze', power='normalize skills LOCS', target='conduit', short_description="Averages out some of her skills (Libido, Obedience, Constitution, Sensitivity), then receive a permanent skill boost", description="Libido, Obedience, Constitution and Sensitivity skills converge on their average value, then receive a permanent boost.", mojo_cost=[('blue', 6)], sanity_cost=2),
                                EvilSuperPower(name='Shuffle', type='Bronze', power='shuffle skills BBCR', target='conduit', short_description="Randomly shuffles the value of some of her skills (Beauty, Body, Charm & Refinement), receiving a permanent boost", description="Beauty, Body, Charm and Refinement skill values are shuffled randomly, receiving a permanent boost", mojo_cost=[('yellow', 6)], sanity_cost=2),
                                EvilSuperPower(name='Shuffle', type='Bronze', power='shuffle skills LOCS', target='conduit', short_description="Randomly shuffles the value of some of her skills (Libido, Obedience, Constitution, Sensitivity), receiving a permanent boost", description="Libido, Obedience, Constitution and Sensitivity skill values are shuffled randomly, receiving a permanent boost", mojo_cost=[('red', 6)], sanity_cost=2),
                                EvilSuperPower(name='Mulligan', type='Bronze', power='mulligan', target='MC', effects=[Effect("change", "evil power cards", 2)], short_description='Redraw all power cards + 2 extra cards', mojo_cost=[('green', 3), ('blue', 3)], sanity_cost=2),
                                EvilSuperPower(name='Mojo surge (yellow)', type='Regular', power='mojo yellow', target='MC', short_description='Receive 4-12 Yellow Mojo, very high sanity cost', mojo_cost=[('green', 2)], sanity_cost=5),
                                EvilSuperPower(name='Mojo surge (red)', type='Regular', power='mojo red', target='MC', short_description='Receive 4-12 Red Mojo, very high sanity cost', mojo_cost=[('yellow', 2)], sanity_cost=5),
                                EvilSuperPower(name='Mojo surge (blue)', type='Regular', power='mojo blue', target='MC', short_description='Receive 4-12 Blue Mojo, very high sanity cost', mojo_cost=[('red', 2)], sanity_cost=5),
                                EvilSuperPower(name='Mojo surge (green)', type='Regular', power='mojo green', target='MC', short_description='Receive 4-12 Green Mojo, very high sanity cost', mojo_cost=[('blue', 2)], sanity_cost=5),
                                EvilSuperPower(name='Leech skills', type='Regular', power='leech service sex', target='other girl', short_description="Leeches some of her skills (Service & Sex) to another girl (larger effect)", description='Leeches more of her service and sex skills and transfers them to a girl of equal or lower rank', mojo_cost=[('green', 2), ('blue', 2)], sanity_cost=3),
                                EvilSuperPower(name='Leech skills', type='Regular', power='leech anal fetish', target='other girl', short_description="Leeches some of her skills (Anal & Service) to another girl (larger effect)", description='Leeches more of her anal and fetish skills and transfers them to a girl of equal or lower rank', mojo_cost=[("red", 2), ('yellow', 2)], sanity_cost=3),
                                EvilSuperPower(name='Dark fantasy: Service', type='Regular', power='service', target='conduit', short_description='Her Service preference will increase (larger effect)', mojo_cost=[('green', 4)], sanity_cost=2),
                                EvilSuperPower(name='Dark fantasy: Sex', type='Regular', power='sex', target='conduit', short_description='Her Sex preference will increase (larger effect)', mojo_cost=[('blue', 4)], sanity_cost=2),
                                EvilSuperPower(name='Dark fantasy: Anal', type='Regular', power='anal', target='conduit', short_description='Her Anal preference will increase (larger effect)', mojo_cost=[('red', 4)], sanity_cost=2),
                                EvilSuperPower(name='Dark fantasy: Fetish', type='Regular', power='fetish', target='conduit', short_description='Her Fetish preference will increase (larger effect)', mojo_cost=[('yellow', 4)], sanity_cost=2),
                                EvilSuperPower(name='Minion training', type='Regular', power='minion', target='minion type', short_description='Shares XP with all minions of the same type', mojo_cost=[('blue', 1), ('red', 2)], sanity_cost=4),
                                EvilSuperPower(name='Connected minds', type='Regular', power='obedience link', target='other girl', short_description='Target another girl. She will have the same chances of accepting acts the conduit accepts', mojo_cost=[('green', 2), ('blue', 2)], sanity_cost=1, duration=5),
                                EvilSuperPower(name='Leech skills', type='Regular', power='leech beauty body', target='other girl', short_description="Leeches some of her skills (Beauty & Body) to another girl (larger effect)", description='Leeches more of her beauty and body skills and transfers them to a girl of equal or lower rank', mojo_cost=[('blue', 2), ('red', 2)], sanity_cost=1),
                                EvilSuperPower(name='Leech skills', type='Regular', power='leech charm refinement', target='other girl', short_description="Leeches some of her skills (Charm & Refinement) to another girl (larger effect)", description='Leeches more of her charm and refinement skills and transfers them to a girl of equal or lower rank', mojo_cost=[('green', 2), ('yellow', 2)], sanity_cost=1),
                                EvilSuperPower(name='Leech skills', type='Regular', power='leech sensitivity constitution', target='other girl', short_description="Leeches some of her skills (Sensitivity & Constitution) to another girl", description='Leeches more of her sensitivity and constitution skills and transfers them to a girl of equal or lower rank (larger effect)', mojo_cost=[('green', 2), ('red', 2)], sanity_cost=1),
                                EvilSuperPower(name='Leech skills', type='Regular', power='leech libido obedience', target='other girl', short_description="Leeches some of her skills (Libido & Obedience) to another girl (larger effect)", description='Leeches more of her libido and obedience skills and transfers them to a girl of equal or lower rank', mojo_cost=[('blue', 2), ('yellow', 2)], sanity_cost=1),
                                EvilSuperPower(name='Hallucination', type='Regular', power='hypnosis', target='all girls', effects=[Effect("change", "hypnosis", 3, scope="brothel")], short_description='All hypnosis attempts on all girls are more likely to succeed', mojo_cost=[('yellow', 3)], sanity_cost=2, duration=5),
                                EvilSuperPower(name='Fearful trade', type='Regular', power='mojo trade', target='MC', short_description='Swaps colored mojo to purple mojo at a rate of 3 for 2', mojo_cost=[('green', 3)], sanity_cost=2),
                                EvilSuperPower(name='Dark fantasy: Naked', type='Regular', power='naked', target='conduit', short_description='Her Naked preference will increase (larger effect)', mojo_cost=[('green', 2)], sanity_cost=2),
                                EvilSuperPower(name='Oni', type='Regular', power='security', target='brothel', effects=[Effect("special", "demon security", 1, scope="brothel"), Effect("change", "security", 1, scope="brothel")], short_description='Raises brothel security', mojo_cost=[('blue', 1), ('red', 1)], sanity_cost=2, duration=10),
                                EvilSuperPower(name='Haniwa', type='Regular', power='maintenance', target='brothel', effects=[Effect("special", "demon maintenance", 1, scope="brothel"), Effect("change", "maintenance", 1, scope="brothel")], short_description='Raises brothel maintenance', mojo_cost=[('blue', 1), ('yellow', 1)], sanity_cost=2, duration=10),
                                EvilSuperPower(name='Demonette', type='Regular', power='advertising', target='brothel', effects=[Effect("special", "demon advertising", 1, scope="brothel"), Effect("change", "advertising", 1, scope="brothel")], short_description='Raises brothel advertising', mojo_cost=[('green', 1), ('blue', 1)], sanity_cost=2, duration=10),
                            ]

        evpower_dict = {pow.power : pow for pow in evpower_list}

        evpower_super_dict = {pow.power : pow for pow in evpower_super_list}

        evpower_deck = EvilPowerDeck()

        evpower_color = {"platinum" : {True : c_gold, False : c_white}, "regular" : {True : c_darkpurple, False : c_black}}

        evil_card_size = 160

    class EvilPower(object):
        def __init__(self, name, type=None, power=None, target = "conduit", effects = None, short_description = "", description = "", pic = "", mojo_cost = None, sanity_cost=1, duration=None, activation_limit="once"):

            # Base information and Card layout
            self.name = name # The name that is displayed on the card
            self.type = type # Type can be: Platinum, Gold, Silver, Bronze or Regular
            self.super = False # Tracks if power is supercharged
            self.short_description = short_description # Displays on card
            if description:
                self.description = description # Displays on card tooltip screen
            else:
                self.description = short_description
            if power:
                self.pic = Picture(path="UI/Powers/cards/art/%s.webp" % power) # Displays on card
            else:
                self.pic = None
            self.sound = s_spell

            # Power effect
            self.power = power # Unique keyword that defines the power and its super equivalent
            self.target = target # Can be "conduit", "other girl", "city girl", "MC", "brothel", "district", "city", "minion type", "minion"
            if not effects: effects = []
            self.effects = effects
            self.active = False
            self.activation_limit = activation_limit # Can be 'once' (only one activation at a time) or 'girl' (once per girl)
            self.duration = duration

            # Power cost
            if not mojo_cost: mojo_cost = []
            self.mojo_cost = mojo_cost # mojo_cost is a list of tuples (color, value). Total mojo cost ranges from 1 (low) to 10+ (high)
            self.sanity_cost = sanity_cost # Sanity cost should range from 1 (mild) to 6 (very high)

            if self.sanity_cost >= 10:
                self.sanity_lvl = "Break"
            elif self.sanity_cost > 5:
                self.sanity_lvl = "Very high"
            elif self.sanity_cost > 3:
                self.sanity_lvl = "High"
            elif self.sanity_cost > 1:
                self.sanity_lvl = "Medium"
            else:
                self.sanity_lvl = "Low"

        def get(self, _super=False):
            if _super:
                return self.get_super()
            else:
                return self.get_regular()

        def get_regular(self):
            return self

        def get_super(self):
            return evpower_super_dict[self.power]

        def can_activate(self):
            if self.activation_limit == "once" and self.power in MC.active_powers:
                notify(event_color["a little good"] % ("%s is already active" % self.power.capitalize()))
                return False
            elif not MC.has_mojo(self.get_mojo_cost()):
                notify(event_color["a little bad"] % ("You do not have enough mojo to cast this power"))
                return False
            return True

        def activate(self, conduit):
            if self.power in MC.active_powers:
                if self.activation_limit == "once" or self.active == conduit:
                    raise AssertionError("Power activation failure: %s is already in the list of active powers" % self.power)

            if self.duration:
                MC.active_powers.append(self.power) # This avoids the power being cast or drawn again before it deactivates
                self.active = conduit
                calendar.set_alarm(calendar.time + self.duration, StoryEvent("deactivate_power", arg=self))

                notify(self.name + " is now active for %i day%s." % (self.duration, plural(self.duration)))

        def deactivate(self):
            if self.power not in MC.active_powers:
                debug_notify("Power deactivation failure: %s is not in the list of active powers" % self.power)
            MC.active_powers.remove(self.power)
            self.active = False
            notify(self.name + " is now inactive.")

        def get_mojo_cost(self, conduit=None):
            mod = 0
            if conduit:
                if isinstance(conduit, Girl):
                    mod = conduit.get_effect("change", "mojo cost")
            return [(col, v+mod) for col, v in self.mojo_cost]


    class EvilSuperPower(EvilPower): # Inherits from EvilPower

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.super = True # Indicates power is supercharged. Not to be mistaken with the super() function.

        def get_regular(self):
            return evpower_dict[self.power]

        def get_super(self):
            return self


    class EvilPowerDeck(object): # This class holds the power cards available to the player

        def __init__(self):
            self.powers = evpower_list
            self.super_powers = evpower_super_list
            self.draw_limit = 5
            self.update()

        def update(self):
            self.can_draw = True
            self.hand = []
            self.hand_size = self.draw_limit + MC.get_effect("change", "evil power cards")

        def draw_powers(self):

            if self.can_draw:
                self.can_draw = False
                # if debug_mode:
                #     self.hand = self.powers[-5:]
                #     self.can_draw = True
                #     return True
                if len(self.hand) < self.hand_size:
                    available_powers = [p for p in self.powers if p not in self.hand]
                    self.hand += renpy.random.sample(available_powers, self.hand_size-len(self.hand))
                return True
            else:
                renpy.notify("You cannot draw any more powers this week.")
                return False

        def play(self, power, conduit): # Returns actual spent points for possible refund
            self.hand.remove(power.get())
            return MC.spend_mojo(power.get_mojo_cost(conduit))


## POWERS LABELS ##

label farm_powers_init():
    $ farm.powers = "intro"

    play sound s_mystery
    show static

    you "Uh? What a strange feeling, all of a sudden..."

    hide static

    "You sense a dark presence tugging at the edge of your consciousness. You feel inexplicably drawn to the {b}farm{/b}."

    return


label update_power_canisters():
    python:
        for col in ["purple", "red", "yellow", "blue", "green"]:

            if MC.mojo[col] < 1:
                img = "%s canister %i" % (col, 0)
            elif MC.mojo[col] < 6:
                img = "%s canister %i" % (col, 1)
            elif MC.mojo[col] < 16:
                img = "%s canister %i" % (col, 2)
            elif MC.mojo[col] < 36:
                img = "%s canister %i" % (col, 3)
            else:
                img = "%s canister %i" % (col, 4)

            renpy.show(img, at_list=[top])
    with Dissolve(0.15)

    return


label draw_powers():
    $ start_at = len(evpower_deck.hand)
    $ evpower_deck.draw_powers()

    hide screen power_draw

    play sound s_spell
    show evil_deck at bounce

    pause 0.4

    show screen power_hand(evpower_deck.hand, context = "move", start_at = start_at)

    pause 0.8

    hide screen power_hand
    show screen power_hand(evpower_deck.hand, context = "flip", start_at = start_at)

    pause 0.8

    hide screen power_hand
    show screen power_hand(evpower_deck.hand)

    return


label burn_card(selected_power):

    show magic fire

    play sound s_fire

    show screen power_card(selected_power, "burn", x=0.5, y=0.5)
    hide screen power_card with burn_it
    hide magic with dissolve

    return

label deactivate_power(pow):
    $ pow.deactivate()
    return

# POWER LOOP

label farm_powers(): # The main game loop is handled here, the less logic we put in screens the better

    scene black
    show bg magic_cellar at top
    with Dissolve(0.15)

    call update_power_canisters() from _call_update_power_canisters

    if farm.powers == "intro":
        call powers_intro() from _call_powers_intro

    camera:
        perspective True

    show evil_deck:
        xpos 0.5075 ypos 0.425
        xanchor 0.5 yanchor 0.5

    if evpower_deck.can_draw:
        show evil_deck at jitter

        show evil_deck_fire behind evil_deck:
            align (0.5075, 0.425)
            xsize yres(150) ysize yres(150)

        show screen shortcuts()

        show screen power_draw()

label farm_powers_loop():

    # $ renpy.block_rollback()

    # STEP 1: CHOOSE POWER
    $ selected_power = conduit = other_girl = None

    show screen mojo_bar() # Displays mojo overlay

    if not evpower_deck.can_draw: # Shows hand if drawing is unavailable
        show screen power_hand(evpower_deck.hand)

    while True: # This loops until a card, conduit etc. are picked and casting is confirmed
        $ renpy.start_predict("supercharge")

        $ r = ui.interact() # This captures every return value from the current context

        if r == "back":
            call hide_everything() from _call_hide_everything_51
            jump farm

        # DRAWING CARDS
        elif r == "draw": # Moves cards in hand and flip newer ones
            call draw_powers() from _call_draw_powers

        # TOGGLING SUPERCHARGE
        elif r == "supercharge":
            $ renpy.restart_interaction()
            # "{nw}"
            show supercharge

            pause 0.8

            hide supercharge

        # SELECTING POWER
        elif isinstance(r, EvilPower):

            # if not MC.has_mojo(r.get_mojo_cost()):
            #     gizel upset "You don't have enough mojo to fuel this power."
            #     jump farm_powers_loop

            if not r.can_activate():
                jump farm_powers_loop

            hide evil_deck
            hide screen power_hand

            $ renpy.stop_predict("supercharge")

            $ selected_power = r

            $ renpy.block_rollback()

            # STEP 2: CHOOSE CONDUIT AND TARGET

            show screen power_target(selected_power)

            while True:
                $ r = ui.interact()

                if r == "back":
                    jump farm_powers_loop

                elif r:
                    if selected_power.target in ("other girl", "city girl"):
                        $ conduit, other_girl = r
                    else:
                        $ conduit, other_girl = r, None

                    # STEP 3: CONFIRM CASTING

                    $ renpy.block_rollback()

                    if renpy.call_screen("mojo_payment", pow=selected_power, conduit=conduit, other_girl=other_girl):
                        $ spent_mojo = evpower_deck.play(selected_power, conduit)

                        if not debug_mode:
                            $ renpy.block_rollback()

                        call burn_card(selected_power) from _call_burn_card

                        call power_use(selected_power, conduit, other_girl) from _call_power_use

                        jump farm_powers

                    else:
                        jump farm_powers_loop


label power_use(pow, girl, girl2):

    #### This label is where powers and their effects are activated ####

    ## 1. Set-up

    # "As soon as [girl.fullname] enters the sanctum, the evil card deck crackles with unholy energy and her eyes go completely white. In a dazed state, she walks in front of the portal and stands still. Satisfied, you give her the power card, which bursts into magic flames that engulf her."

    hide screen mojo_bar

    ## 2. Activate power

    play sound pow.sound
    $ pow.activate(conduit=girl)

    # Rituals

    if pow.power == "chaos":
        if pow.super:
            if story_flags["chaos"] == False:
                call chaos(girl) from _call_chaos
            else:
                "You cannot summon Chaos more than once."
                $ MC.refund_mojo(spent_mojo)
                return
        else:
            call summon_pet(girl) from _call_summon_pet

    elif pow.power.startswith("ritual"):

        "Today, you arranged for Gizel to gather some of her minions, and organize a unique show for some of your most select customers. Some of your girls are attending as well. You want that to be a lesson."

        $ witness = rand_choice(MC.girls)

        if pow.power.endswith("orgy"):
            play sound s_screams
            $ pic = girl.get_pic("group", and_tags=["big"])
            show screen show_img(pic, bg="black")
            with dissolve

            girl.char "Oh, aah, aaaah!!!" with vpunch

            "[girl.fullname] is fucked mercilessly in all positions by a large group of men and women, including some rather large stallions. They've decided to ruin all of her holes tonight, and you're not going to stop them."

            $ pop = {1 : laborer, 2 : craftsman, 3 : patrician, 4 : aristocrat, 5 : royal}[girl.rank]
            $ cust_nb = girl.get_max_interactions()

            if pow.super:
                $ cust_nb *= 2

            $ MC.change_gold(girl.get_tip("sex", "very good", [Customer(pop)]*cust_nb)[0])

        elif pow.power.endswith("bondage"):
            play sound s_surprise
            $ pic = girl.get_fix_pic("fetish", "bondage", and_tags=["monster"])
            show screen show_img(pic, bg="black")
            with dissolve

            girl.char "Aaaah!!!" with vpunch

            "[girl.fullname] struggles against her bonds, but only manages to make them tighter. Your customers laugh at her increasingly panicked attempts."

            if pow.super:
                "Gizel has filled the room with fearsome-looking utensils: the perverted customers will get to torture her all night with them."

            python:
                for g in MC.girls + farm.girls:
                    add_effects(g, pow.effects)

                notify("All girls: Libido and Obedience increased")

        elif pow.power.endswith("violence"):
            play sound s_scream_loud
            $ pic = girl.get_pic("hurt", "fetish", and_tags=["sad", "beast"], and_priority=False)
            show screen show_img(pic, bg="black")
            with dissolve

            girl.char "OUCH!!! Oh, it hurts!!!" with vpunch

            "Some of your sickest customers delight in inflicting pain to [girl.fullname] in a variety of ways. The only rule is not to leave any long-lasting damage... Physical damage, at any rate."

            python:
                for g in MC.girls + farm.girls:
                    add_effects(g, pow.effects)

                notify("All girls: Fear increased")

        "[witness.fullname] cannot avert her eyes."

        call dialogue(witness, "slave witness " + pow.power) from _call_dialogue_258

        if pow.super:
            $ brothel.change_rep(50)
        else:
            $ brothel.change_rep(20)

        hide screen show_img with dissolve

    # Demon helpers

    elif pow.power == "advertising":

        "A minor female demon steps out of the portal."

        scene black
        show bg succubi6 at top
        with dissolve

        demonette "Hello, Summoner... Hmmm..."

        hide bg with dissolve

        $ impact = round_int(0.15*brothel.max_help)

        "The demonette and her sisters will raise your brothel advertising by [impact] for [pow.duration] days."

        $ add_effects(MC, pow.effects, expires=calendar.time + pow.duration)

    elif pow.power == "security":

        "A towering figure rises from the portal in a puff of dark smoke."

        demon "Reporting for duty, Summoner."

        $ impact = round_int(0.15*brothel.max_help)

        "The Demon will raise your brothel security by [impact] for [pow.duration] days."

        $ add_effects(MC, pow.effects, expires=calendar.time + pow.duration)

    elif pow.power == "hannies":

        "A bunch of small figures leap out of the portal, stumbling over themselves."

        hanny "HANNYYYYY!!!"

        $ impact = round_int(0.15*brothel.max_help)

        "The hannies will raise your brothel maintenance by [impact] for [pow.duration] days."

        $ add_effects(MC, pow.effects, expires=calendar.time + pow.duration)

    elif pow.power == "prestige":

        $ possible_acts = list(all_sex_acts)

        if girl.has_trait("Virgin"):
            $ possible_acts.remove("sex")

        if pow.super:
            $ acts = rand_choice(possible_acts, 2)
            $ mod = 10
        else:
            $ acts = [rand_choice(possible_acts)]
            $ mod = 5

        python:
            for act in acts:
                girl.change_stat(act, dice(mod+1) + mod-1)
                # notify(act.capitalize() + ": +%i", pic=girl.portrait)

            girl.xp = 1.5*(mod*15)**1.1 # Emulating Girl.get_xp() formula, with a customer diff of 75 for lesser demon and 150 for larger one

            MC.prestige += mod // 2

        call incubus_scene(girl, large_demon=pow.super) from _call_incubus_scene

    # Preference raising

    elif pow.power in extended_sex_acts:
        if pow.super:
            $ chg, new_pref = girl.raise_preference(pow.power, type="fear", bonus = 5, status_change=True, use_effects=False)
        else:
            $ chg, new_pref = girl.raise_preference(pow.power, type="fear", bonus = 2.5, status_change=True, use_effects=False)

        # Changing preference text

        python:
            text_changes = __(pow.power.capitalize()) + ": "

            if chg > 0:
                text_changes += "{color=[c_green]}"
                for i in range(int(1 + chg//50)): text_changes += "+"
                text_changes += "{/color}"
            else:
                text_changes = "{i}No change.{/i}"

            if new_pref and new_pref != "refuses":
                if girl.is_("lewd"):
                    text1 = pref_response["lewd " + new_pref] % long_act_description[pow.power]
                else:
                    text1 = pref_response["modest " + new_pref] % long_act_description[pow.power]
            else:
                text1 = "Her %s preference has moderately increased." % pow.power

        $ pic = girl.get_pic("rest", and_tags = ["libido"])

        if new_pref and new_pref != "refuses":
            call show_night_event(Event(pic, char = girl.char, text = text1, changes = text_changes, sound = s_ahaa, type = "special")) from _call_show_night_event_9
            $ text1 = girl.fullname + " is now " + preference_color[new_pref] % new_pref + " with " + pow.power + " acts."

        call show_night_event(Event(pic, char = narrator, text = text1, changes = text_changes, type = "special")) from _call_show_night_event_10

    elif pow.power == "force naked":
        "Following your command, she absent-mindedly sheds all of her clothing until she stands naked before you. She doesn't seem to fully register the change."
        $ add_effects(girl, pow.effects, expires=calendar.time + pow.duration)
        $ girl.naked = True
        $ girl.refresh_pictures()

    elif pow.power == "negative fixation":
        $ neg_fix = [fix for fix in girl.neg_fixations if (girl.personality_unlock[fix.name])]

        if neg_fix:
            $ fix = menu([("选择要移除的负面癖好", None)] + [(f.name.capitalize(), f) for f in neg_fix] + [("取消", "返回")])

            if fix == "back":
                $ MC.refund_mojo(spent_mojo)
                return

            else:
                $ text1 = ""
                if not pow.super:
                    $ new_fix = girl.add_random_fixation(type="neg")[0] # Adding the new fixation first ensures the old one will not be randomly chosen
                    $ girl.personality_unlock[new_fix] = False
                    $ text1 = " She has received a new negative fixation."

                $ girl.remove_fixation(fix.name)

                "[girl.fullname] is no longer uncomfortable with [fix.name].[text1]"

                if pow.super:
                    call exhaust_girl(girl)

        else:
            "You must have discovered at least one of [girl.fullname]'s negative fixations before you can use this power."
            $ MC.refund_mojo(spent_mojo)
            return

    # Mojo and fear

    elif pow.power.startswith("mojo"):
            if pow.power == "mojo trade":
                if pow.super:
                    $ r = renpy.call_screen("mojo_trade", 3, 2)
                else:
                    $ r = renpy.call_screen("mojo_trade", 2, 1)

                if r == "back":
                    play sound s_fizzle
                    $ MC.refund_mojo(spent_mojo)
                    return

                else:
                    python:
                        for mcolor, chg in r.items():
                            MC.mojo[mcolor] += chg

            else:
                $ mojo_color = pow.power[5:]
                if pow.super:
                    $ points = dice(3, 4) # 4d3 points
                else:
                    $ points = dice(3, 2) # 2d3 points

                $ t = 0.15

                show screen mojo_bar

                $ notify("+%i" % points, pic = "mojo_" + mojo_color)

                while points:
                    $ MC.raise_mojo(mojo_color)
                    $ points -= 1
                    pause t

    elif pow.power == "fear boost":
        $ add_effects(MC, pow.effects, expires=calendar.time + pow.duration)
        $ add_effects(farm, pow.effects, expires=calendar.time + pow.duration)

        "An evil aura forms around you, putting fear in your girls' hearts."

    # Spells and hypnosis

    elif pow.power == "hypnosis":
        if pow.super:
            "You sap her will, strengthening your hypnotic powers for the next few days."
            $ add_effects(MC, pow.effects, expires=calendar.time + pow.duration)
        else:
            "You weaken her mind for the next few days, making her more receptive to suggestion."
            $ add_effects(girl, pow.effects, expires=calendar.time + pow.duration)

    elif pow.power in all_MC_stats:
        "You absorb some of her life energy, temporarily boosting your [pow.power]."
        $ add_effects(MC, pow.effects, expires=calendar.time + pow.duration)

    # Skill manipulation

    elif pow.power.startswith("normalize skills"):
        if pow.power.endswith("BBCR"):
            $ sk_list = gstats_main[:4]
        elif pow.power.endswith("LOCS"):
            $ sk_list = gstats_main[4:]

        if pow.super:
            $ mod = 1.2
        else:
            $ mod = 1.0

        $ girl.average_skills(sk_list, mod)

    elif pow.power.startswith("shuffle skills"):
        if pow.power.endswith("BBCR"):
            $ sk_list = gstats_main[:4]
        elif pow.power.endswith("LOCS"):
            $ sk_list = gstats_main[4:]

        if pow.super:
            $ mod = 1.2
        else:
            $ mod = 1.0

        $ girl.shuffle_skills(sk_list, mod)

    elif pow.power == "normalize fear":
        if pow.super:
            $ girl.love = 0
            $ girl.fear = 0
            "[girl.fullname] has forgotten all the feelings she had about you, positive or negative."
        else:
            $ girl.love = girl.love // 3
            $ girl.fear = girl.fear // 3
            "[girl.fullname] now feels a lot less strongly about you."

    # Punishment

    elif pow.power == "punish":
        $ add_effects(MC, pow.effects, expires=calendar.time + pow.duration)

        "Drawing power from [girl.fullname]'s past traumas, you inprint a healthy fear of punishment in all of your girls' mind."

    # Hurt/Tired

    elif pow.power == "frenzy":
        $ add_effects(girl, pow.effects, expires=calendar.time + pow.duration)
        $ calendar.set_alarm(calendar.time + pow.duration, StoryEvent(label="exhaust_girl", type="morning", order=2, call_args=[girl, pow.super, 4]))
        "[girl.fullname] suddenly rises up, bursting with dark energy. Without a word, she heads back to the farm and starts working on her chores."

    elif pow.power == "hurt":
        if pow.super:
            python:
                for girl2 in (MC.girls + farm.girls):
                    h = min(6, girl2.hurt) # Caps at 6 hurt
                    girl.get_hurt(h)
                    girl2.heal(h)
        else:
            $ h = min(6, girl2.hurt) # Caps at 6 hurt
            $ girl.get_hurt(h)
            $ girl2.heal(h)

    elif pow.power == "energy":
        "Drawing on your dark powers, you siphon as much energy out of [girl.fullname] as you dare."

        if pow.super:
            $ en = girl.get_stat_minmax("energy")[1] # conduit's max energy
        else:
            $ en = int(0.2 * girl.energy)

        python:
            for g in MC.girls + farm.girls:
                g.change_energy(en)

        call exhaust_girl(girl, pow.super) from _call_exhaust_girl

    # Leech effects

    elif pow.power.startswith("leech"):

        $ targets = pow.power[6:].split() # Returns a list of skills or stats to leech

        while targets:
            $ target = targets.pop(0)

            if target == "rep":
                if girl.rep < 1:
                    "This girl has no reputation to transfer."
                    play sound s_fizzle
                    $ MC.refund_mojo(spent_mojo)
                    return

                "Focusing your mind on [girl2.fullname], you begin the incantations to channel some of [girl.name]'s fame towards her."
                $ rep = girl.rep - rep_to_rank[girl.rank-1]
                $ _max = rep_to_rank[girl.rank] - rep_to_rank[girl.rank-1]

                if not pow.super:
                    $ _max /= 2

                $ rep = min(rep, _max)
                $ rep = max(rep, 1)

                $ chg = int(-girl.change_rep(-rep))
                $ girl2.change_rep(chg)

                "{b}[chg] reputation{/b} has been transferred from [girl.fullname] to [girl2.fullname]."

            elif target == "xp": # Targets all girls

                if girl.xp < 50:
                    "This girl's XP is too low to use that power."
                    play sound s_fizzle
                    $ MC.refund_mojo(spent_mojo)
                    return

                $ receiving_girls = [g for g in MC.girls + farm.girls if g != girl and g.level < girl.level]

                if not receiving_girls:
                    "No girls of lesser level could be found in the brothel or farm, so you decide not to cast the power."
                    play sound s_fizzle
                    $ MC.refund_mojo(spent_mojo)
                    return

                "You use the dark powers at your disposal to leech [girl.name]'s life memories, sharing them with your less experienced slaves."

                if pow.super:
                    $ total_xp = girl.xp // 2
                else:
                    $ total_xp = girl.xp // 4

                $ indiv_xp = total_xp // len(receiving_girls)

                python:
                    girl.change_xp(-total_xp, False, False)
                    for g in receiving_girls:
                        g.change_xp(indiv_xp, False, False)

                $ narrator("%i girl%s have received {b}%i xp{/b} each from %s (%s)." % (len(receiving_girls), plural(len(receiving_girls)), indiv_xp, girl.fullname, and_text([g.fullname for g in receiving_girls])))

            elif target == "jp": # Targets all girls
                python:
                    changes = ""
                    for job in all_jobs:
                        receiving_girls = [g for g in MC.girls + farm.girls if g != girl and g.job_level[job] <= girl.job_level[job]]

                        if receiving_girls:
                            if pow.super:
                                total_jp = girl.jp[job] // 2
                            else:
                                total_jp = girl.jp[job] // 4

                            indiv_jp = total_jp // len(receiving_girls)

                            girl.change_jp(-total_jp, job, False, False)
                            for g in receiving_girls:
                                g.change_jp(indiv_jp, job, False, False)

                            changes += "%i girl%s have received {b}%i %s jp{/b} each from %s (%s). " % (len(receiving_girls), plural(len(receiving_girls)), indiv_jp, job, girl.fullname, and_text([g.fullname for g in receiving_girls]))

                if not changes:
                    "No girls of a lesser job level could be found in the brothel or farm, so you decide not to cast the power."
                    play sound s_fizzle
                    $ MC.refund_mojo(spent_mojo)
                    return

                "You use the dark powers at your disposal to leech [girl.name]'s work memories, sharing them with your less experienced slaves."

                "[changes]"

            else: # Leeches a skill
                if pow.super:
                    $ chg = girl.get_stat(target, True) // 2
                else:
                    $ chg = girl.get_stat(target, True) // 4

                $ girl.change_stat(target, -chg, False, False)
                $ chg = int(girl2.change_stat(target, chg, False, False))

                if chg > 0:
                    "[girl.fullname] has transferred {b}[chg] [target]{/b} to [girl2.fullname]."

        if target == "other girl":
            scene black with fade
            "Back in her room, [girl2.fullname] wakes up abruptly from a feverish dream, not quite recognizing herself or the source of her newfound confidence."

    # Obedience

    elif pow.power == "obedience":
        $ add_effects(girl, pow.effects, expires=calendar.time + pow.duration)
        "[girl.fullname] has become temporarily more obedient."

    elif pow.power == "obedience link":
        $ add_effects(girl2, Effect("special", "link obedience", (girl, pow.super)), expires=calendar.time + pow.duration)
        "As your conduit falls into a trance, you focus the dark energies on your other girls, and quickly find your mark: [girl2.fullname]. Unbeknownst to her, she now shares a bond with [girl.fullname] and will be affected by her obedience and loyalty."

    # Farm powers

    elif pow.power == "farm":
        if pow.super:
            $ add_effects(MC, pow.effects, expires=calendar.time + pow.duration)
            "All girls will be more receptive to farm training for some time."
        else:
            $ add_effects(girl, pow.effects, expires=calendar.time + pow.duration)
            "[girl.fullname] will be more receptive to farm training for some time."

    elif pow.power == "minion":

        if girl.xp < 50:
            "This girl's XP is too low to cast that power."
            play sound s_fizzle
            $ MC.refund_mojo(spent_mojo)
            return

        "[girl.fullname] lies on the cold floor in a state of daze. Focusing your mind on the farm, you choose the target of your next power."

        $ mn_type = menu([("选择单位种类", None)] + [(mt.capitalize() + "s", mt) for mt in all_minion_types if farm.get_minions(mt)] + [("取消", "返回")])

        if mn_type == "back":
            $ MC.refund_mojo(spent_mojo)
            return

        $ girl.xp -= 50

        if pow.super:
            play sound s_spell
            python:
                for mn in farm.get_minions(mn_type):
                    mn.xp += girl.rank*5
                    if mn.level_up():
                        text1 = "仆从升级: %s (等级 " + str(mn.level) + ")" % mn.name
                        change_log.add(text1, color="special")
                        renpy.notify(text1)

        else:
            $ mn = menu([("选择具体单位", None)] + [(m.name.capitalize(), m) for m in farm.get_minions(mn_type)] + [("取消", "返回")])

            if mn == "back":
                $ MC.refund_mojo(spent_mojo)
                return

            play sound s_spell
            $ mn.xp += girl.rank*5

    # Mulligan

    elif pow.power == "mulligan":
        if pow.super:
            $ add_effects(MC, pow.effects, expires=calendar.time + 1)
        $ evpower_deck.update()

    # Customers and rooms

    elif pow.power == "room capacity":
        $ eff = Effect("boost", "room capacity", 0.5, scope="brothel") # Effect is generated dynamically for this power

        if not pow.super: # Choose one room
            $ room = menu([("选择一个经营场所", None)] + [(r.name.capitalize(), r) for r in brothel.rooms.values()] + [("取消", "返回")])

            if room == "back":
                $ MC.refund_mojo(spent_mojo)
                return

            $ eff.target = room.name + " room capacity"
            $ add_effects(MC, eff, expires=calendar.time + pow.duration)
            $ _val = room.update_cust_limit(silent=True)

            "The [room.name] can now accomodate [_val] more customers."
        else:
            $ add_effects(MC, eff, expires=calendar.time + pow.duration)
            python:
                for room in brothel.rooms.values():
                    _val = room.update_cust_limit(silent=True) # _val will be the same for each room
            "All common rooms in your brothel can now accomodate [_val] more customers."

        $ add_effects(MC, eff, expires=calendar.time + pow.duration)
        $ calendar.set_alarm(calendar.time + pow.duration, StoryEvent("reset_room_capacity", order=1))

    elif pow.power == "customer satisfaction":
        $ add_effects(MC, pow.effects, expires=calendar.time + pow.duration)
        "Her mind is now entirely focused on giving customers a good time."

    elif pow.power == "customer capacity":
        $ add_effects(MC, pow.effects, expires=calendar.time + pow.duration)
        "Some of her life energy will be used to sustain the other girls while they serve customers."

    # City powers

    elif pow.power == "city love":
        if girl.get_love() <= 6:
            "[girl.fullname] doesn't love you enough to use that power."
            $ MC.refund_mojo(spent_mojo)
            return

        $ love = girl.get_love() # Each girl will receive 15-30% of her love value
        $ girl.love = 0

        if pow.target == "location":
            $ dis = menu([("选择目标地点", None)] + [(d.name, d) for d in all_districts if d.chapter <= game.chapter] + [("取消", "返回")])

            if dis == "back":
                $ MC.refund_mojo(spent_mojo)
                return

            $ loc = menu([("选择具体位置", None)] + [(l.name, l) for l in location_dict[dis.name]] + [("取消", "返回")])

            if loc == "back":
                $ MC.refund_mojo(spent_mojo)
                return

            python:
                for g in game.free_girls:
                    if g.location == loc.name:
                        g.change_love(renpy.random.randint(round_down(0.15*love), round_up(0.3*love)))

        elif pow.target == "district":
            $ dis = menu([("选择目标地点", None)] + [(d.name, d) for d in all_districts if d.chapter <= game.chapter] + [("取消", "返回")])

            if dis == "back":
                $ MC.refund_mojo(spent_mojo)
                return

            python:
                for g in game.free_girls:
                    if location_dict[g.location].get_district() == dis:
                        g.change_love(renpy.random.randint(round_down(0.15*love), round_up(0.3*love)))


        elif pow.target == "city":
            python:
                for g in game.free_girls:
                    g.change_love(renpy.random.randint(round_down(0.15*love), round_up(0.3*love)))



        play sound s_spell

        "The girls in the [pow.target] now love you more."

    elif pow.power == "kidnap":
        "Using your powers, you place [girl.fullname] into a trance, until she is ready to obey your commands."

        you "Go to the city, and find [girl2.fullname]. Fly, my pretty!"

        "She will be back in the morning."
        $ farm.girls.remove(girl)
        $ MC.girls.append(girl)
        $ girl.away = True
        $ girl.return_date = calendar.time + 1

        $ calendar.set_alarm(calendar.time + 1, StoryEvent(label="kidnap_return", type="morning", order=2, call_args=[girl, girl2, pow.super]))

    elif pow.power == "slave":
        if pow.super:
            python:
                for g in MC.girls + farm.girls:
                    if g.free:
                        g.free = False
            "All your formerly free girls have forgotten they once weren't slaves."
        else:
            if girl.free:
                $ girl.free = False
                "[girl.fullname] has forgotten she once wasn't a slave."
            else:
                $ MC.refund_mojo(spent_mojo)
                "[girl.fullname] is not a former free girl, she is already fully enslaved."
                return

    # Postings

    elif pow.power == "postings":
        $ add_effects(girl, pow.effects, expires=calendar.time + pow.duration)
        if pow.super:
            "Quests and classes will bring more rewards to all girls."
        else:
            "Quests and classes will bring more rewards to her."

    # Personality, Traits and Perks

    elif pow.power == "personality":

        python:
            attr_change_list = []

            for a1, a2 in personality_attributes:
                if girl.is_(a1): attr_change_list.append(a2)
                if girl.is_(a2): attr_change_list.append(a1)

        if pow.super:
            $ attempt = 1
            $ changes = []

            while attempt <= 2:
                $ changes.append(menu([("Choose how to affect her personality ([attempt]/2):", None)] + [("Become more %s" % a, a) for a in attr_change_list if a not in changes]))
                $ attempt += 1

        else:
            $ changes = rand_choice(attr_change_list, 2)

        python:
            for attr in changes:
                old_attr = get_opposite_attribute(attr)

                if girl.is_("very " + old_attr): # Changes from "very X" to "X"
                    girl.attributes.remove("very " + old_attr)
                else: # Changes from "X" to opposite of "X"
                    girl.attributes.remove(old_attr)
                    girl.attributes.append(attr)

            girl.adjust_personality()

        call dialogue(girl, "slave confused") from _call_dialogue_259

        $ narrator("[girl.fullname] has become more %s and %s." % (changes[0], changes[1]))


    elif pow.power == "negative trait":
        python:
            trait_list = [] # A list of possible negative traits with a weight
            for trait in neg_traits:
                if trait in girl.traits:
                    old_neg = trait
                elif use_ini_traits and trait.name in girl.init_dict["base negative traits/never"]:
                    continue
                else:
                    for opp in trait.opposite:
                        if opp in girl.traits:
                            break
                    else:
                        if use_ini_traits and trait in girl.init_dict["base negative traits/often"]:
                            trait_list.append((trait, 4))
                        elif use_ini_traits and trait in girl.init_dict["base negative traits/rarely"]:
                            trait_list.append((trait, 1))
                        else:
                            trait_list.append((trait, 2))

            trait_list.sort(key=lambda tup: tup[1], reverse=True) # Sorts list of tuples by their second element (weight)

        if pow.super:
            $ menu_list = [(t.name, t) for t, w in trait_list[:3]] # Lists the first three traits
            $ new_neg = menu([("选择一个新特质来替代 %s:" % old_neg.name, None)] + menu_list)
        else:
            $ new_neg = weighted_choice(trait_list)

        $ girl.remove_trait(old_neg)
        $ girl.add_trait(new_neg, no_perks=True)

        "[girl.fullname] has received a new negative trait, replacing [old_neg.name]."

    elif pow.power == "perks":
        if pow.super:
            $ r = girl.refund_perks(0)

        else:
            $ r = girl.refund_perks(2)

        if r:
            "[girl.fullname] has let go of some of her past knowledge. [r] perk points have been refunded."
        else:
            "[girl.fullname] does not have any affected perks to refund."
            $ MC.refund_mojo(spent_mojo)
            return

    ## 3. Backlash on conduit

    if pow.power != "kidnap":
        call sanity_backlash(girl, pow)

    return

label sanity_backlash(girl, pow):

    $ narrator(girl.lose_sanity(pow.sanity_cost)) # Describes the state of her current sanity

    if pow.sanity_cost > 6:
        $ MC.evil += 3
    elif pow.sanity_cost > 3:
        $ MC.evil += 2
    elif pow.sanity_cost > 1:
        $ MC.evil += 1

    $ girl.last_power = calendar.time # Girls can only conduct powers once per day

    return

label incubus_scene(girl, large_demon=False):

    $ text1 = {False: "lesser", True: "large"}[large_demon]

    if girl.has_trait("Virgin"):
        $ pic = rand_choice(game_image_dict["Misc"]["demon service"])
    elif not large_demon:
        $ pic = rand_choice(game_image_dict["Misc"]["demon service"][:2] + game_image_dict["Misc"]["demon sex"][:1])
    else:
        $ pic = rand_choice(game_image_dict["Misc"]["demon service"][2:] + game_image_dict["Misc"]["demon sex"][1:])

    scene black with fade
    show expression pic at top with dissolve

    play sound s_screams
    girl.char "Oooh, aaah, aaaaaaaah!!!"

    "[girl.fullname]'s screams echo through the sanctum as she is abused mercilessly by a [text1] demon."

    hide expression pic with dissolve

    return


label kidnap_return(girl, girl2, _super):

    ## Return conduit home
    $ girl.away = False
    $ girl.return_date = -1
    $ MC.girls.remove(girl)
    $ farm.girls.append(girl)


    ## Test kidnapping success
    $ mod = 1 + girl2.rank - girl.rank

    if _super:
        $ mod -= 2
        $ pow = evpower_super_dict["kidnap"]
    else:
        $ pow = evpower_dict["kidnap"]

    if fight(girl, girl2, def_bonus=mod):

        scene black with fade

        play sound s_punch
        show screen show_event(girl.get_pic("fight"))
        with dissolve

        "[girl.fullname] was successful in kidnapping [girl2.fullname] and bringing her back. She drops her unconscious prey at your feet, before collapsing with exhaustion. You gesture for her to be taken to her room and instruct Sill to take charge of your new acquisition."

        $ girl.change_xp(50*girl.rank)
        $ notify("%s has gained XP." % girl.fullname)

        ## Acquire new girl
        call acquire_girl(girl2, context="free") from _call_acquire_girl_4

        if _return:
            show screen show_event(girl2.get_pic("market", "profile", and_tags=["sad"], and_priority=False))
            with dissolve

            play sound s_surprise

            girl2.char "Oh... My head... Where... Where am I?"

            $ MC.evil += 2

            if girl2.MC_interact:
                $ MC.evil += girl2.MC_relationship_level
                if girl2.MC_relationship_level > 0:
                    girl2.char "[MC.name]? But... I trusted you!!!" with vpunch
                    $ girl2.change_fear(15)
                else:
                    girl2.char "Wait, you're [MC.name]! What have you done to me?"
                    $ girl2.change_fear(10)
            else:
                $ girl2.change_fear(10)

            you "Listen carefully. You're mine now, and from now on I will be your master. Don't even think about escaping: we caught you once, we can catch you again."

        else:
            you "Damn, I should have thought of that before... Hmph, just tell the goons to dump her in the back alley, before she wakes up and makes a scene."

            "You have to let [girl2.fullname] go... this time."

    else:
        play sound s_crash
        show screen show_event(girl.get_pic("hurt", "fight", and_tags=["sad"], and_priority=False))
        with dissolve

        $ h = girl.get_hurt(max(1, dice(3) + girl2.rank - girl.rank))
        if h > 0:
            $ text1 = "She was hurt in the process (for %i day%s)." % (h, plural(h))

        "[girl.fullname]'s attempt to abduct [girl2.fullname] failed.[text1]"

    call sanity_backlash(girl, pow) # Backlash happens after the kidnapping attempt

    hide screen show_event
    with dissolve
    return

# Power intro #

label powers_intro():

    $ farm.powers = True

    show static

    "*Indistinct mumbling*"

    you "Gizel? Is that you?"

    stop music fadeout 2.0
    hide static with dissolve

    "A strange noise and light originate from the center of the room. Hesitantly, you approach the source."

    play sound s_mystery

    pause 1.0

    play sound2 s_surprise

    show gizel normal with moveinright:
        xalign 1.1
        yalign 1.0

    gizel "What's up?"

    you "Hyaah!!!" with vpunch

    gizel surprise "What?"

    you "You startled me!"

    gizel smirk "You look like you've seen a ghost... Even though I've driven the evil spirit out of this place. Or I thought I did, anyway."

    you "What do you mean?"

    gizel normal "See this room? It was here in the basement, abandoned for a long time. I had Bob excavate the entrance a while back."

    you "This doesn't look like it belongs in a farm."

    gizel smirk "Such sharp wits. That's what I like about you."

    gizel normal "Ever wonder how a simple farmhouse would become haunted?"

    gizel "This place is much more than it looks. It oozes with dark powers. And I'm thinking that it all started here, in this very basement."

    you "Why didn't you tell me about this place before?"

    gizel upset "I didn't see the need. Nothing was going on here, it was just a dark cellar full of dust and cobwebs!"

    you "But look at it! It's doing all kinds of weird lights, and buzzing with ungodly energy!" with vpunch

    gizel upset "Yes, but it only just started mere moments ago! When {b}you{/b} walked in, I might add!"

    you "Me?"

    gizel "Yes! You are the cause of this!" with vpunch

    $ MC.rand_say(["wz: 但我没有施任何咒语?我什么都没做!", "这怎么可能呢?"])

    gizel normal "I've been wondering about that myself, and I have a theory."

    gizel "It's the fear, you see!"

    you "The fear? What are you rambling about?"

    gizel "The fear that you have been causing people around you. It sticks with you. Around you."

    gizel "I can sense it... And this place can, too. The fear is strong with you."

    you "You're the one to talk..."

    gizel "This place also absorbs the fear I cause your girls... But it only seems to actively react to you."

    gizel smirk "Probably because you ordered me to do all those bad things, so you're the evil one."

    you "I did not... Hey!"

    gizel surprise "{nw}"

    play sound s_lightning
    show static
    show magic fire

    "*CRACK*"

    you "What... What was that?"

    play sound s_lightning
    hide static
    hide magic fire
    with flash

    gizel upset "Look!"

    show evil_deck behind gizel with dissolve:
        xpos 0.5075 ypos 0.425
        xanchor 0.5 yanchor 0.5
        linear 1.0 zoom 0.8
        linear 0.5 zoom 1.0
        repeat

    show evil_deck_fire behind evil_deck:
        align (0.5075, 0.425)
        xsize yres(150) ysize yres(150)

    with dissolve

    you "What on earth is that?"

    gizel normal "Hmm..."

    gizel "It appears to be a floating deck of cards."

    you "Such sharp wits. That's what I like about you..."

    play sound s_mystery

    gizel upset "Shut up! I think it's beckoning you. Come on, pick a card!"

    you "What, are you crazy?" with vpunch

    you "(What am I saying... Of course she's crazy.)"

    hide gizel with dissolve

    $ init_powers()

    # show screen power_draw()
    #
    # $ r = ui.interact()

    # if r == "draw":
    #     call draw_powers() from _call_draw_powers_1

    return


#### END OF BKpowers.rpy ####
