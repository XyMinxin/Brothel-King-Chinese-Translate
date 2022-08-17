# <neronero & RudolfU - BK.ini>
# <Minxin 汉化>
label generate_ini():

    if not persistent.girl:

        call select_girl_pack() from _call_select_girl_pack_ini

        if result == "quit":
            return

        $ girl = result
        $ persistent.girl = girl.path

    else:
        python:

            for girl in girl_list:
                if girl.path == persistent.girl:
                    break
            else:
                renpy.say("", "无法找到女孩路径'persistent.girl'。")
                persistent.girl = None
                renpy.jump("generate_ini")

    menu:
        "这将在所选女孩的文件夹中生成一个名为{b}_BK.ini{/b}的文件。警告: 如果这个文件已经存在，它将被覆盖。"
        "继续":
            $ ini_header = "#### " + persistent.girl[len("images/"):] + " - BK.ini 由标签工具生成 #### \n"
            $ ini_header += "## 此可选文件包含有关特定女孩的高级配置数据, 不需要的变量可以删除。\n"
            $ ini_header += "## 该文件应命名为\"_BK.ini\"并放入相关的女孩文件夹中。\n"
            $ ini_header += "## 全行注释需要在开头使用双井号(##)引入。\n"
            $ ini_header += "## 同一行注释必须使用空格加分号(;)来添加。\n\n\n"


            $ ini_identity = "[identity] \n\n"

            $ ini_identity += "first_name = \"" + str(renpy.input("这个女孩的名字是什么？: ", default=persistent.girl[len("images/"):])) + "\" ; 名字 - 如果没有或为空，名字将被随机。\n"
            $ ini_identity += "last_name = \"" + str(renpy.input("这个女孩的姓氏是什么？: ", default=persistent.girl[len("images/"):])) + "\" ; 姓氏 - 如果没有或为空，将不使用姓氏。\n"
            $ ini_identity += "inverted_name = " + str(renpy.call_screen("yesno_prompt", "她的名字和姓氏是否按相反顺序显示？ (东亚风格)", Return(True), Return(False))) + " ; 如果为True，全名将在名字之前显示姓氏，否则False。\n"
            $ ini_identity += "creator = \"" + str(renpy.input("在这里输入你的名字，以便我们知道是谁制作了这个人物包:", default="Anon")) + "\" ; 制作人 - 在这里输入你的名字，以便知道是谁制作了这个人物包。\n\n \n"


            $ ini_skills = "[base skills] \n\n"

            $ ini_skills += "## 初始技能 - 从1到5的排名初始技能 (1是可怕的, 3是平均的, 5是精湛的。游戏会增加一些变化。) 设置为0时随机技能级别\n"

            "{i}接下来我们将确定女孩的起始技能。游戏中会增加一些轻微的变化。{/i}"

            $ ini_skills += "charm = "

            menu:
                "{b}魅力{/b} - 她的个性和存在感。影响了作为{b}服务员{/b}和{b}性服侍{/b}的工作。"
                "可怕的(1)":
                    $ ini_skills += "1"
                "较差的(2)":
                    $ ini_skills += "2"
                "一般的(3)":
                    $ ini_skills += "3"
                "不错的(4)":
                    $ ini_skills += "4"
                "精湛的(5)":
                    $ ini_skills += "5"
                "\n随机(0)\n":
                    $ ini_skills += "0"

            $ ini_skills += " ; 魅力 - 服务员/性服侍\n"
            $ ini_skills += "beauty = "

            menu:
                "{b}美貌{/b} - 她看起来多么漂亮。影响了作为{b}按摩师{/b}和{b}性交{/b}的工作。"
                "可怕的(1)":
                    $ ini_skills += "1"
                "较差的(2)":
                    $ ini_skills += "2"
                "一般的(3)":
                    $ ini_skills += "3"
                "不错的(4)":
                    $ ini_skills += "4"
                "精湛的(5)":
                    $ ini_skills += "5"
                "\n随机(0)\n":
                    $ ini_skills += "0"

            $ ini_skills += " ; 美貌 - 按摩师/性交\n"
            $ ini_skills += "body = "

            menu:
                "{b}身材{/b} - 她的身材有多好，有多结实。影响了作为{b}舞娘{/b}和{b}肛交{/b}的工作。"
                "可怕的(1)":
                    $ ini_skills += "1"
                "较差的(2)":
                    $ ini_skills += "2"
                "一般的(3)":
                    $ ini_skills += "3"
                "不错的(4)":
                    $ ini_skills += "4"
                "精湛的(5)":
                    $ ini_skills += "5"
                "\n随机(0)\n":
                    $ ini_skills += "0"

            $ ini_skills += " ; 身材 - 舞娘/肛交\n"
            $ ini_skills += "refinement = "

            menu:
                "{b}优雅{/b} - 她是多么聪明和世俗。影响了作为{b}艺伎{/b}和{b}皮绳愉虐{/b}的工作。"
                "可怕的(1)":
                    $ ini_skills += "1"
                "较差的(2)":
                    $ ini_skills += "2"
                "一般的(3)":
                    $ ini_skills += "3"
                "不错的(4)":
                    $ ini_skills += "4"
                "精湛的(5)":
                    $ ini_skills += "5"
                "\n随机(0)\n":
                    $ ini_skills += "0"

            $ ini_skills += " ; 优雅 - 艺妓/皮绳愉虐\n"
            $ ini_skills += "sensitivity = "

            menu:
                "{b}敏感{/b} - 她的身体有多敏感。影响{b}按摩师{/b}，{b}性服侍{/b}和提高顾客的{b}满意度{/b}。"
                "可怕的(1)":
                    $ ini_skills += "1"
                "较差的(2)":
                    $ ini_skills += "2"
                "一般的(3)":
                    $ ini_skills += "3"
                "不错的(4)":
                    $ ini_skills += "4"
                "精湛的(5)":
                    $ ini_skills += "5"
                "\n随机(0)\n":
                    $ ini_skills += "0"

            $ ini_skills += " ; 敏感 - 性服侍/满意度\n"
            $ ini_skills += "libido = "

            menu:
                "{b}性欲{/b} - 她对性的渴望程度。影响了{b}舞者{/b}、{b}性交{/b}和{b}嫖客上限{/b}。"
                "可怕的(1)":
                    $ ini_skills += "1"
                "较差的(2)":
                    $ ini_skills += "2"
                "一般的(3)":
                    $ ini_skills += "3"
                "不错的(4)":
                    $ ini_skills += "4"
                "精湛的(5)":
                    $ ini_skills += "5"
                "\n随机(0)\n":
                    $ ini_skills += "0"

            $ ini_skills += " ; 性欲 - 性交/顾客\n"
            $ ini_skills += "constitution = "

            menu:
                "{b}体格{/b} - 她的精力。影响{b}服务员{/b}、{b}肛交{/b}、提高她的{b}精力{/b}上限，使她能为{b}更多顾客{/b}服务。"
                "可怕的(1)":
                    $ ini_skills += "1"
                "较差的(2)":
                    $ ini_skills += "2"
                "一般的(3)":
                    $ ini_skills += "3"
                "不错的(4)":
                    $ ini_skills += "4"
                "精湛的(5)":
                    $ ini_skills += "5"
                "\n随机(0)\n":
                    $ ini_skills += "0"

            $ ini_skills += " ; 体格 - 肛交/精力\n"
            $ ini_skills += "obedience = "

            menu:
                "{b}服从{/b} - 她对命令和奴役的接受程度。影响{b}艺妓{/b}、{b}皮绳愉虐{/b}和接受{b}工作{/b}或{b}培训{/b}的机会。"
                "可怕的(1)":
                    $ ini_skills += "1"
                "较差的(2)":
                    $ ini_skills += "2"
                "一般的(3)":
                    $ ini_skills += "3"
                "不错的(4)":
                    $ ini_skills += "4"
                "精湛的(5)":
                    $ ini_skills += "5"
                "\n随机(0)\n":
                    $ ini_skills += "0"

            $ ini_skills += " ; 服从 - 皮绳愉虐/服从\n\n \n"
            $ ini_positive_traits = "[base positive traits] \n\n"

            "{i}女孩通常初始拥有2个正面特质和1个负面特质。你可以确定某些特质在你的女孩身上出现的可能性。{/i}"

            $ ini_positive_traits += "## 正面特质 - 注意，一个女孩只能有2个正面特质。稀有特质被认为是正面的。特质名称必须在引号之间。特质名称的列表详见\"BKstart.rpy\"。\n"
            $ text11 = "正面特质 - 注意，一个女孩只能有2个正面特质。稀有特质被认为是正面的。特质名称必须在引号之间。特质名称的列表详见\"BKstart.rpy\"。\n\n"
            $ text22 = "选择女孩{b}固定{/b}拥有的稀有和正面特质。我们建议留空，因为它使女孩的生成非常可预测。(最多可有nb个特质)"
            # $ renpy.say(narrator, "选择女孩{b}固定{/b}拥有的稀有和正面特质。我们建议留空，因为它使女孩的生成非常可预测。(最多可有nb个特质)")
            call screen positive_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_positive_traits += "always = [" + str(txt) + "] ; 始终拥有这些特质。(最多 nb 个特质)\n"

            $ text22 = "选择女孩{b}经常{/b}拥有的稀有和正面特质。"
            # $ renpy.say(narrator, "选择女孩{b}经常{/b}拥有的稀有和正面特质。")
            call screen positive_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_positive_traits += "often = [" + str(txt) + "] ; 经常拥有这些特质\n"

            $ text22 = "选择女孩{b}很少{/b}拥有的稀有和正面特质。"
            # $ renpy.say(narrator, "选择女孩{b}很少{/b}拥有的稀有和正面特质。")
            call screen positive_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_positive_traits += "rarely = [" + str(txt) + "] ; 很少拥有这些特质\n"

            $ text22 = "选择女孩{b}不会{/b}拥有的稀有和正面特质。"
            # $ renpy.say(narrator, "选择女孩{b}不会{/b}拥有的稀有和正面特质。")
            call screen positive_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_positive_traits += "never = [" + str(txt) + "] ; 不会拥有这些特质\n"


            $ ini_positive_traits += "\n"
            $ ini_negative_traits = "[base negative traits] \n\n"


            $ ini_negative_traits += "## 负面特质 - 注意，一个女孩可能只有1个负面特质。特质名称必须在引号之间。特质名称的列表详见\"BKstart.rpy\"。\n"
            $ text11 = "负面特质 - 注意，一个女孩可能只有1个负面特质。特质名称必须在引号之间。特质名称的列表详见\"BKstart.rpy\"。\n\n"
            $ text22 = "选择女孩{b}固定{/b}拥有的负面特质。我们建议留空，因为它使女孩的生成非常容易预测。"
            # $ renpy.say(narrator, "选择女孩{b}固定{/b}拥有的负面特质。我们建议留空，因为它使女孩的生成非常容易预测。")
            call screen negative_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_negative_traits += "always = [" + str(txt) + "] ; 始终拥有这些特质。(最多 nb 个特质)\n"

            $ text22 = "选择女孩{b}经常{/b}拥有的的负面特质。"
            # $ renpy.say(narrator, "选择女孩{b}经常{/b}拥有的的负面特质。")
            call screen negative_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_negative_traits += "often = [" + str(txt) + "] ; 经常拥有这些特质\n"

            $ text22 = "选择女孩{b}很少{/b}拥有的负面特质。"
            # $ renpy.say(narrator, "选择女孩{b}很少{/b}拥有的负面特质。")
            call screen negative_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_negative_traits += "rarely = [" + str(txt) + "] ; 很少拥有这些特质\n"

            $ text22 = "选择女孩{b}不会{/b}拥有的负面特质。"
            # $ renpy.say(narrator, "选择女孩{b}不会{/b}拥有的负面特质。")
            call screen negative_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_negative_traits += "never = [" + str(txt) + "] ; 不会拥有这些特质\n"

            hide screen ini_negative_traits_list

            $ ini_negative_traits += "\n"
            $ ini_personality = "[base personality] \n\n"

            show screen ini_personality_list()

            "{i}女孩的性格决定了她对玩家的行为的反应，包括在对话和游戏性方面。{/i}"

            $ ini_personality += "## 一个女孩只能有一种性格。游戏中共有23种性格类型: pervert, rebel, cold, nerd, masochist, meek, sweet, superficial, bimbo, holy, helper, creep, repressed, schemer, prude, princess, pet, easy, class president, tsundere, loyal, yandere, stubborn\n"
            $ text11 = "性格 - 每一个女孩只能有一种性格。游戏中共有23种性格类型。\n\n"
            $ text22 = "选择女孩{b}固定{/b}出现的性格。我们建议留空，因为它使女孩的生成非常容易预测。"
            # $ renpy.say(narrator, "选择女孩{b}固定{/b}出现的性格。我们建议留空，因为它使女孩的生成非常容易预测。")
            call screen personality_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_personality += "always = [" + str(txt) + "] ; 固定出现，它使女孩的生成非常容易预测\n"

            $ text22 = "选择女孩{b}经常{/b}出现的性格。"
            # $ renpy.say(narrator, "选择女孩{b}经常{/b}出现的性格。")
            call screen personality_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_personality += "often = [" + str(txt) + "] ; 经常出现\n"

            $ text22 = "选择女孩{b}很少{/b}出现的性格。"
            # $ renpy.say(narrator, "选择女孩{b}很少{/b}出现的性格。")
            call screen personality_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_personality += "rarely = [" + str(txt) + "] ; 很少出现\n"

            $ text22 = "选择女孩{b}从不{/b}出现的性格。"
            # $ renpy.say(narrator, "选择女孩{b}从不{/b}出现的性格。")
            call screen personality_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_personality += "never = [" + str(txt) + "] ; 从不出现\n\n"

            hide screen ini_personality_list

            $ ini_personality += "\n"
            $ ini_custom_personality = "[custom personality] \n\n"

            $ ini_custom_personality += "## 自定义的性格 - 你可以为你的女孩加入一个自定义的性格。这需要在你的人物包中加入一个.rpy文件，其中包括她的对话台词。\n\n"

            $ ini_custom_personality += "custom_personality = False" + " ; 是否启用自定义性格\n"
            $ ini_custom_personality += "personality_name = \"\"" + " ; 自定义性格名称\n"
            $ ini_custom_personality += "attributes = (\"\",\"\")" + "\n"
            $ ini_custom_personality += "generic_dialogue = True" + " ; 通用对话\n"
            $ ini_custom_personality += "personality_dialogue_only = []" + " ; 自定义性格对话\n"
            $ ini_custom_personality += "dialogue_personality_weight = 3" + " ; 自定义性格对话的权重\n"
            $ ini_custom_personality += "dialogue_attribute_weight = 1" + "\n"
            $ ini_custom_personality += "description = \"\"" + " ; 描述\n"
            $ ini_custom_personality += "custom_dialogue_label = \"\"" + " ; 自定义对话标签\n\n"

            $ ini_custom_personality += "\n"
            $ ini_sexual_preferences = "[sexual preferences] \n\n"

            "{i}我们现在将转到女孩的性偏好。首先通过了解她最喜欢的性行为类别和固定性偏好。{/i}"

            $ ini_sexual_preferences += "## 积极或消极的行为 - 你可以选择积极或消极的行为，这些行为会更频繁地为这个女孩产生。可能的选择是: \"naked\", \"service\", \"sex\", \"anal\", \"fetish\", \"bisexual\", \"group\".\n"
            $ text11 = "积极或消极的行为 - 你可以选择积极或消极的行为，这些行为会更频繁地为这个女孩产生。\n\n"
            $ text22 = "对这个女孩来说，哪些{b}积极行为{/b}会经常地产生？"
            # $ renpy.say(narrator, "对这个女孩来说，哪些{b}积极行为{/b}会经常地产生？")
            call screen act_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "favorite_acts = [" + str(txt) + "] ; 积极行为\n"

            $ text22 = "对这个女孩来说，哪些{b}消极行为{/b}会经常产生？"
            # $ renpy.say(narrator, "对这个女孩来说，哪些{b}消极行为{/b}会经常产生？")
            call screen act_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "disliked_acts = [" + str(txt) + "] ; 消极行为\n\n"


            $ ini_sexual_preferences += "## 积极的性趣 - 你可以选择积极的性趣, 女孩将会对这个产生更频繁的关注。名称可在\"BKinit_variables.rpy\"文件中找到。\n"
            $ text11 = "积极的性趣 - 你可以选择积极的性趣, 女孩将会对这个产生更频繁的关注。名称可在\"BKinit_variables.rpy\"文件中找到。\n\n"
            $ text22 = "选择女孩{b}固定{/b}出现的积极的性趣。我们建议留空，因为它使女孩的生成非常可预测。"
            # $ renpy.say(narrator, "选择女孩{b}固定{/b}出现的积极的性趣。我们建议留空，因为它使女孩的生成非常可预测。")
            call screen fixation_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "always_fixations = [" + str(txt) + "] ; 固定出现，它使女孩的生成非常容易预测\n"

            $ text22 = "选择女孩{b}经常{/b}出现的积极的性趣。"
            # $ renpy.say(narrator, "选择女孩{b}经常{/b}出现的积极的性趣。")
            call screen fixation_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "favorite_fixations = [" + str(txt) + "] ; 经常出现\n"

            $ text22 = "选择女孩{b}很少{/b}出现的积极的性趣。"
            # $ renpy.say(narrator, "选择女孩{b}很少{/b}出现的积极的性趣。")
            call screen fixation_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "disliked_fixations = [" + str(txt) + "] ; 很少出现\n"

            $ text22 = "选择女孩{b}从不{/b}出现的积极的性趣。"
            # $ renpy.say(narrator, "选择女孩{b}从不{/b}出现的积极的性趣。")
            call screen fixation_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "never_fixations = [" + str(txt) + "] ; 从不出现\n\n"

            $ ini_sexual_preferences += "## 消极的性趣 - 你可以选择消极的性趣, 女孩将会对这个产生更加厌恶的情绪。固定名称可在\"BKinit_variables.rpy\"文件中找到。\n"
            $ text11 = "消极的性趣 - 你可以选择消极的性趣, 女孩将会对这个产生更加厌恶的情绪。固定名称可在\"BKinit_variables.rpy\"文件中找到。\n\n"
            $ text22 = "选择女孩{b}固定{/b}出现的消极的性趣。我们建议留空，因为它使女孩的生成非常可预测。"
            # $ renpy.say(narrator, "选择女孩{b}固定{/b}出现的消极的性趣。我们建议留空，因为它使女孩的生成非常可预测。")
            call screen fixation_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "always_negative_fixations = [" + str(txt) + "] ; 固定出现，它使女孩的生成非常容易预测\n"

            $ text22 = "选择女孩{b}从不{/b}出现的消极的性趣。"
            $ renpy.say(narrator, "选择女孩{b}从不{/b}出现的消极的性趣。")
            call screen fixation_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "never_negative_fixations = [" + str(txt) + "] ; 从不出现\n\n"


            "{i}接下来我们将确定女孩的性经验和她的农场弱点。{/i}"

            $ ini_sexual_preferences += "## 性经验 - 在遇到玩家之前，她有多少性经验。你可以在以下方面进行选择: \"very experienced\", \"experienced\",  \"average\", \"inexperienced\", \"very inexperienced\", \"random\"。\n"
            $ ini_sexual_preferences += "sexual_experience = "

            menu:
                "{b}性经验{/b} - 女孩在遇到玩家之前有多少性经验？"
                "非常有经验":
                    $ ini_sexual_preferences += "\"very experienced\""
                "有经验":
                    $ ini_sexual_preferences += "\"experienced\""
                "一般":
                    $ ini_sexual_preferences += "\"average\""
                "没有经验":
                    $ ini_sexual_preferences += "\"inexperienced\""
                "非常缺乏经验":
                    $ ini_sexual_preferences += "\"very inexperienced\""
                "\n随机\n":
                    $ ini_sexual_preferences += "\"random\""

            $ ini_sexual_preferences += " ; 如果没有或空白，将随机选择性经验。\n\n"

            $ ini_sexual_preferences += "## 农场弱点 - 在以下数值中选择: \"stallion\", \"beast\", \"monster\", \"machine\", \"random\"\n\n"
            $ ini_sexual_preferences += "farm_weakness = "

            menu:
                "{b}农场弱点{/b} - 为这个女孩选择一个农场的弱点。"
                "种马":
                    $ ini_sexual_preferences += "\"stallion\""
                "野兽":
                    $ ini_sexual_preferences += "\"beast\""
                "怪物":
                    $ ini_sexual_preferences += "\"monster\""
                "机器":
                    $ ini_sexual_preferences += "\"machine\""
                "\n随机\n":
                    $ ini_sexual_preferences += "\"random\""

            $ ini_sexual_preferences += "\n\n"

            $ ini_sexual_preferences += "\n"
            $ ini_background = "[background story] \n\n"

            "{i}快要完成了！最后一些问题是关于她的背景和克隆选项。{/i}"

            $ ini_background += "## 自由 - 女孩可以设置为 \"全部(all)\" 或限制为 \"自由(free)\" 或 \"奴隶(slave)\"。\n"
            $ ini_background += "generate_as = "

            menu:
                "{b}自由{/b} - 这个女孩是否都存在自由女孩和奴隶，或者限制为只有自由女孩或奴隶？"
                "限制她只能以奴隶女孩的身份出现 (在奴隶市场)":
                    $ ini_background += "\"slave\""
                "限制她只能以自由女孩的身份出现 (在城市)":
                    $ ini_background += "\"free\""
                "同时允许":
                    $ ini_background += "\"all\""

            $ ini_background += "\n\n"

            $ ini_background += "## 自定义起源 - 你可以提供一个自定义的起源，或者只是\"随机(random)\"。(如果使用自定义起源, 请确保在下面包含起源描述)\n\n"
            menu:
                "{b}起源{/b} - 你是否愿意写一句对话，给这个女孩定制一个起源故事吗？"
                "是":
                    $ ini_background += "origin = \"" + str(renpy.input("{b}起源名称{/b} - 说明她被抚养的地点。", default="")) + "\" ; 起源名称 - 说明她被抚养的地点\n"
                    $ ini_background += "origin_description = \"" + str(renpy.input("{b}起源描述{/b} - 为你的女孩写下一段对话，在对话中她谈到了她的出生地。", default="")) + "\" ; 起源描述 - 必须用女孩第一人称描写。为你的女孩写下一段对话，在对话中她谈到了她的出生地\n"

                "否，让游戏为她生成一个起源故事":
                    $ ini_background += "origin = \"random\"\n## origin_description = None\n"

            $ ini_background += "## 如果提供，在随机化之后创建一个具有此模板的女孩时，调用此函数。\n## 它必须以'girl'作为参数。它必须不中断游戏流程。(只限于python，没有ren'py调用或跳转)\n## 在_events.rpy或另一个自定义的.rpy文件的init块中写入该函数。\n"
            $ ini_background += "## init_function = None ; 提供一个自定义的函数名称，在女孩创建后被调用。(在引号之间)\n\n"

            $ ini_background += "## 如果提供，这个标签将被调用，而不是正常的城市互动。它必须以'girl'作为参数。\n## 通过使用'call free_girl_talk(girl)'，可以从这个自定义标签中调用常规对话选项。\n"
            $ ini_background += "## city_label = \"\" ; 提供自定义标签名称。(在引号之间)\n\n"

            $ ini_background += "## 如果提供，这个标签将被调用，而不是一个随机的背景故事。它必须以'girl'作为参数。\n## 参见BKinteractions.rpy中的'slave_story'标签，以了解它如何工作的例子。(请随意以非常不同的方式设置事件)\n"
            $ ini_background += "## story_label = None ; 提供自定义标签名称。(在引号之间)\n\n"

            $ ini_background += "## 如果提供，这个标签将每晚被调用。它必须接受'girl'参数。这对于递增一些数值、运行一些测试或重置交互是有用的。\n## 建议这类标签默默地运行，必要时添加一个StoryEvent。\n"
            $ ini_background += "## night_label = None ; 提供自定义标签名称。(在引号之间)\n\n"

            $ ini_background += "## 这将在常规的互动菜单中添加一个自定义按钮。如果你不使用它，请使用None或空括号。\n"
            $ ini_background += "## interact_prompt = (\"Interact text\", \"interact_label\", 1) ; 第一个字符串指的是按钮的标题。第二个是点击按钮时将被调用的标签。整数是AP成本 (仅用于UI显示，它不会从你的标签代码之外的MC动作中扣除，以获得灵活性)。它必须以'girl'作为参数。\n\n"

            $ ini_background += "\n"
            $ ini_cloning = "[cloning options] \n\n"

            menu:
                "{b}独特{/b} - 你是否希望限制为这个女孩创造克隆人？"
                "是，只允许她作为原版出现":
                    $ ini_cloning += "unique = True ; 如果为True，将不会生成克隆，只生成原始女孩，并且所有其他克隆选项都将无效\n"
                    $ ini_cloning += "keep_first_name = True ; 如果为True，克隆将保持相同的名字\n"
                    $ ini_cloning += "keep_last_name = False ; 如果为True，克隆将保持相同的姓氏\n"
                    $ ini_cloning += "keep_inverted = False ; 如果为True，克隆将保持相同的倒置名称选项\n"
                    $ ini_cloning += "keep_skills = False ; 如果为True，克隆将保持相同的基本技能分配\n"
                    $ ini_cloning += "keep_traits = True ; 如果为True，克隆将保持相同的基本特质选项\n"
                    $ ini_cloning += "keep_personality = False ; 如果为True，克隆将保持相同的性格选项\n"
                    $ ini_cloning += "keep_sex = True ; 如果为True，克隆将保持相同的性偏好和经验\n\n"

                    $ ini_cloning += "keep_generate_as = False ; 如果为False，克隆将被生成为奴隶和自由女孩，而不考虑原始设置。\n"
                    $ ini_cloning += "keep_init = False ; 如果为True，克隆将保持相同的初始函数\n"
                    $ ini_cloning += "keep_background = False ; 如果为True，克隆将保持相同的起源和背景故事\n"
                    $ ini_cloning += "keep_interactions = True ; 如果为True，克隆将保持相同的互动选项 (城市和互动菜单选项)\n\n\n"

                    $ ini_cloning += "#### END OF FILE ####"

                "否，允许克隆":
                    $ ini_cloning += "unique = False ; 如果为True，将不会生成克隆，只生成原始女孩，并且所有其他克隆选项都将无效\n"

                    menu:
                        "{b}克隆的名字{/b} - 她的克隆应该如何命名？"
                        "保留她的名字":
                            $ ini_cloning += "keep_first_name = True ; 如果为True，克隆将保持相同的名字\n"
                        "随机选择她的名字":
                            $ ini_cloning += "keep_first_name = False ; 如果为True，克隆将保持相同的名字\n"

                    menu:
                        "{b}克隆的姓氏{/b} - 她的克隆应该如何命名？"
                        "保留她的姓氏":
                            $ ini_cloning += "keep_last_name = True ; 如果为True，克隆将保持相同的姓氏\n"
                        "随机选择她的姓氏":
                            $ ini_cloning += "keep_last_name = False ; 如果为True，克隆将保持相同的姓氏\n"

                    menu:
                        "{b}克隆的名字倒置{/b} - 克隆是否应该遵循你为倒置的名字所选择的相同选项？"
                        "是":
                            $ ini_cloning += "keep_inverted = True ; 如果为True，克隆将保持相同的倒置名称选项\n\n"
                        "否":
                            $ ini_cloning += "keep_inverted = False ; 如果为True，克隆将保持相同的倒置名称选项\n\n"

                    menu:
                        "{b}克隆的技能{/b} - 克隆是否保持相同的基本技能？ (美貌、身材、魅力、等等...)"
                        "是":
                            $ ini_cloning += "keep_skills = True ; 如果为True，克隆将保持相同的基本技能分配\n"
                        "否，允许有更多的变化":
                            $ ini_cloning += "keep_skills = False ; 如果为True，克隆将保持相同的基本技能分配\n"

                    menu:
                        "{b}克隆的特质{/b} - 克隆是否保持相同的特质选项和限制？"
                        "是":
                            $ ini_cloning += "keep_traits = True ; 如果为True，克隆将保持相同的基本特质选项\n"
                        "否，允许有更多的变化":
                            $ ini_cloning += "keep_traits = False ; 如果为True，克隆将保持相同的基本特质选项\n"

                    menu:
                        "{b}克隆的性格{/b} - 克隆是否保持相同的性格选择和限制？"
                        "是":
                            $ ini_cloning += "keep_personality = True ; 如果为True，克隆将保持相同的性格选项\n"
                        "否，允许有更多的变化":
                            $ ini_cloning += "keep_personality = False ; 如果为True，克隆将保持相同的性格选项\n"

                    menu:
                        "{b}克隆的性偏好{/b} - 克隆是否在性经验和偏好方面保持同样的选择和限制？"
                        "是":
                            $ ini_cloning += "keep_sex = True ; 如果为True，克隆将保持相同的性偏好和经验\n\n"
                        "否，允许有更多的变化":
                            $ ini_cloning += "keep_sex = False ; 如果为True，克隆将保持相同的性偏好和经验\n\n"

                    menu:
                        "{b}克隆的自由{/b} - 克隆在自由/奴隶地位方面是否保持任何限制？"
                        "是":
                            $ ini_cloning += "keep_generate_as = True ; 如果为False，克隆将被生成为奴隶和自由女孩，而不考虑原始设置。\n"
                        "否，允许有更多的变化":
                            $ ini_cloning += "keep_generate_as = False ; 如果为False，克隆将被生成为奴隶和自由女孩，而不考虑原始设置。\n"

                    $ ini_cloning += "## keep_init = False ; 如果为True，克隆将保持相同的初始函数\n"
                    menu:
                        "{b}克隆的背景故事{/b} - 克隆是否保持相同的背景和起源？"
                        "是":
                            $ ini_cloning += "keep_background = True ; 如果为True，克隆将保持相同的起源和背景故事\n"
                        "否，允许有更多的变化":
                            $ ini_cloning += "keep_background = False ; 如果为True，克隆将保持相同的起源和背景故事\n"

                    $ ini_cloning += "keep_interactions = True ; 如果为True，克隆将保持相同的互动选项 (城市和互动菜单选项)\n\n\n"

                    $ ini_cloning += "#### END OF FILE ####"
            python:

                txtFile = open(config.gamedir + "/" + persistent.girl + "/_BK.ini", "w")

                txtFile.writelines(ini_header + ini_identity + ini_skills + ini_positive_traits + ini_negative_traits + ini_personality + ini_custom_personality + ini_sexual_preferences + ini_background + ini_cloning)

                txtFile.close()

        "返回菜单":
            return

    return # </neronero & RudolfU - BK.ini>



# ----------------------------- SCREENS -----------------------------


screen ini_positive_traits_list():

    frame xalign 0.5 xmaximum 0.9 xpadding 20 ypadding 50 yalign 0.5 background "#002244":

        has vbox spacing 20 xmaximum 0.9

        $ text_positive = "{b}Gold Traits{/b}\n"
        $ gold_traits_list = ["Naughty", "Fascinating", "Lust", "Warrior", "Skilled tongue", "Always wet", "Tight ass", "Playful", "Wild", "Dirty mind", "Magnetic", "Loose", "Dedicated", "Provocative", "Fashionista", "Perfectionist", "Elite", "Gifted", "Fast learner", "Caster", "Driven", "Country girl", "Noble", "Naturist", "Vicious"]

        $ positive_traits_list = ["Cute", "Long legs", "Nice boobs", "Juicy ass", "Sweet", "Exotic", "Polite", "Feminine", "Horny", "Resilient",  "Delicate", "Meek", "Pretty eyes", "Firm tits", "Seductive", "Graceful", "Beautiful", "Fit", "Charming", "Elegant", "Slutty", "Athletic", "Sensitive", "Obedient", "Energetic", "Tough", "Sexy", "Humble", "Virgin", "Sharp", "Loyal", "Brave", "Strong", "Lucky", "Deft", "Nimble", "Soft skin", "Bright", "Agile", "Brisk", "Rowdy", "Powerful", "Unhurried", "Modest", "Sensual", "Kinky", "Pervert", "Thief"]

        python:
            for trait in gold_traits_list:
                text_positive += "\"" + trait + "\", "

            text_positive += "\n\n{b}Positive Traits{/b}\n"

            for trait in positive_traits_list:
                text_positive += "\"" + trait + "\", "

        text text_positive size 18 color "#ffffff"

screen ini_negative_traits_list():

    frame xalign 0.5 xmaximum 0.9 xpadding 20 ypadding 50 yalign 0.5 background "#002244":

        has vbox spacing 20 xmaximum 0.9

        $ text_negative = "{b}Negative Traits{/b}\n"
        $ negative_traits_list = ["Plain", "Scars", "Mean", "Rude", "Cold", "Weak", "Rough", "Defiant", "Scruffy", "Plump", "Timid", "Vulgar", "Tame", "Frail", "Jaded", "Rebellious", "Lazy", "Sickly", "Homely", "Expensive", "Slow", "Distrustful", "Fearful", "Vulnerable", "Unlucky", "All thumbs", "Awkward", "Brutal", "Dumb", "Oafish", "Clumsy", "Prude", "Naive", "Square"]

        python:
            for trait in negative_traits_list:
                text_negative += "\"" + trait + "\", "

        text text_negative size 18 color "#ffffff"

screen ini_personality_list():

    frame xalign 0.5 xmaximum 0.9 xpadding 20 ypadding 50 yalign 0.5 background "#002244":

        has vbox spacing 20 xmaximum 0.9

        $ text_personality = "{b}性格简介{/b}\n"
        $ personalities_list = ["{b}\"变态\"{/b} - 野性和'无限制'的那种女孩。对各种性行为都很好奇，越变态越好。不关心浪漫的事。",
        "{b}\"叛逆\"{/b} - 总是与他人争吵和抵触，激烈地独立。必须按照她自己的意愿做事。",
        "{b}\"冰冷\"{/b} - 她冷漠而疏离，不轻易表达自己的感情。她似乎对周围发生的事情感到奇怪，对他人的命运也不感兴趣。",
        "{b}\"书呆子\"{/b} - 沉默寡言，喜欢读书。头重脚轻。好奇心强。不喜欢体力劳动。",
        "{b}\"受虐狂\"{/b} - 越底层越好。她喜欢处于底层，并暗自享受被虐待的感觉。礼物和爱的姿态让她恼火，她不配得到这些。",
        "{b}\"温顺\"{/b} - 害羞，容易被动摇，会哭而不反抗。不喜欢冲突。",
        "{b}\"甜美\"{/b} - 可爱和阳光的个性。总是很积极。相当浪漫。不喜欢消极的东西。",
        "{b}\"肤浅\"{/b} - 她一直是个社会名流，关心自己的形象，最好是穿着最出色的衣服，戴着昂贵的珠宝。有些人说她有需求，渴望得到关注，但她知道他们只是嫉妒她的新鞋......",
        "{b}\"荡妇\"{/b} - 虚荣心强，渴望得到关注，关心地位和财富。喜欢礼物和赞美。她也毫无顾忌地利用自己的身体来获得这些东西。",
        "{b}\"圣洁\"{/b} - 她是宗教和道德的倡导者，每天晚上都会为自己的灵魂祈祷，并试图让别人皈依她的信仰。到目前为止，几乎没有成功，但她不会放弃。",
        "{b}\"热心\"{/b} - 总是准备帮助她的朋友，把自己放在别人后面。有时会有点多管闲事。",
        "{b}\"害羞\"{/b} - 她在人前害羞而笨拙，对各种肮脏的话题都很痴迷，在自己的时间里研究。因盯梢而被投诉，很多。",
        "{b}\"压抑\"{/b} - 她在一个非常严格的环境中长大，生活在对自己冲动的恐惧中，并竭力压制它们。",
        "{b}\"谋士\"{/b} - 她最喜欢的是策划和制定宏伟的计划，准备对所有的生物进行统治......直到那一天的到来。在此期间，如果她不得不吸吮一个家伙... 那就这样吧。",
        "{b}\"傲慢\"{/b} - 在任何时候都要做一个善良的、敬畏阿里奥斯的女孩。不喜欢轻浮和不道德的行为。有人认为她暗地里有肮脏的想法，但如果是这样，她也隐藏得很好。",
        "{b}\"公主\"{/b} - 她是一位形象化的公主 (或者她是吗？) ，她认为每个人都应该为她服务，满足她的每一个要求。她可能很残忍，但大多数情况下，她很天真。",
        "{b}\"宠物\"{/b} - 老师的宠物。总是准备取悦她的主人，最喜欢的就是在他脚下舒适地生活。有些人鄙视她缺乏独立性，在她背后叫她难听的名字。",
        "{b}\"安逸\"{/b} - 这不是她的错，她总是吸引男人，而且从来没有心思拒绝他们。虽然很多人说她很容易，但她的唯一目的是传播快乐。但愿不是性病。",
        "{b}\"班长\"{/b} - 必须永远处于领先地位，努力成为模范，鄙视各种不当行为。她对他人的高期望值反映了她对自己的严苛管教。",
        "{b}\"傲娇\"{/b} - 她很容易被激怒，很难取悦，她有一个秘密的软肋。她会冒着危险帮助别人，然后因为他们需要帮助而踢他们的屁股。",
        "{b}\"忠诚\"{/b} - 总是服从命令，出于责任感多于恐惧。认为每个人都必须知道自己的位置，并在他们所担任的任何工作中尽职尽责。即使是妓女。",
        "{b}\"病娇\"{/b} - 在热辣和神经质的尺度上非常高。充满爱心和奉献精神，但同时也是个疯子。为了得到她的男人并扼杀竞争者，她准备做任何事情，包括......真的扼杀他们。",
        "{b}\"顽固\"{/b} - 不喜欢不认同她的原则和道德价值观的人，也不喜欢矛盾。她在派对上很有趣，如果你喜欢以酒馆斗殴结束的派对的话。"]

        python:
            for personality in personalities_list:
                text_personality += personality + "\n"

        text text_personality size 16 color "#ffffff"

screen ini_fixations_list():

    frame xalign 0.5 xmaximum 0.9 xpadding 20 ypadding 50 yalign 0.5 background "#002244":

        has vbox spacing 20 xmaximum 0.9

        $ text_fixations = "{b}Fixations{/b}\n"
        $ fixations_list = ["stripping",  "public acts", "cosplay", "dildos", "vibrators", "dirty sex", "penis worship", "bondage", "oil", "wet", "submission", "femdom", "gags", "strap-ons", "roleplay", "plugs", "enemas", "beads",  "masturbation", "fingering", "handjobs", "cunnilingus", "oral", "irrumatio", "deep throat", "titjobs", "footjobs", "double penetration", "fisting", "insults", "69",  "watersports", "ass-to-mouth", "kissing", "spanking", "rimming", "fondling her boobs", "groping her ass", "lactation", "doggy style", "cowgirl", "piledriver", "spooning", "bukkake", "cum in mouth", "cum on face", "cum in hair", "cum on body", "cum shower", "swallowing", "creampie", "cum inside", "multiple orgasms", "denied orgasm", "squirting"]

        python:
            for fixation in fixations_list:
                text_fixations += "\"" + fixation + "\", "

        text text_fixations size 18 color "#ffffff"


# Make sure you check RenPy documentation.
# Especially Screen Language and Screen Actions
screen positive_choice():
    default values = set()
    style_prefix "choice"
    $ gold_traits_list = ["Naughty", "Fascinating", "Lust", "Warrior", "Skilled tongue", "Always wet", "Tight ass", "Playful", "Wild", "Dirty mind", "Magnetic", "Loose", "Dedicated", "Provocative", "Fashionista", "Perfectionist", "Elite", "Gifted", "Fast learner", "Caster", "Driven", "Country girl", "Noble", "Naturist", "Vicious"]
    $ positive_traits_list = ["Cute", "Long legs", "Nice boobs", "Juicy ass", "Sweet", "Exotic", "Polite", "Feminine", "Horny", "Resilient",  "Delicate", "Meek", "Pretty eyes", "Firm tits", "Seductive", "Graceful", "Beautiful", "Fit", "Charming", "Elegant", "Slutty", "Athletic", "Sensitive", "Obedient", "Energetic", "Tough", "Sexy", "Humble", "Virgin", "Sharp", "Loyal", "Brave", "Strong", "Lucky", "Deft", "Nimble", "Soft skin", "Bright", "Agile", "Brisk", "Rowdy", "Powerful", "Unhurried", "Modest", "Sensual", "Kinky", "Pervert", "Thief"]

    text text11 + text22
    text "{color=#FFD700}{b}稀有特质{/b}{/color}" size 30 ypos 100 xalign 0.5
    for index, name in enumerate(gold_traits_list):
        hbox xpos (index%6)*0.18 ypos 140+index//6*40:
            if name in trait_name_dict :
                textbutton trait_name_dict[name] action ToggleSetMembership(values, name)
            else:
                textbutton name action ToggleSetMembership(values, name)
    text "{color=#009874}{b}正面特质{/b}{/color}" size 30 ypos 400 xalign 0.5
    for index, name in enumerate(positive_traits_list):
        hbox xpos (index%6)*0.18 ypos 440+index//6*40:
            textbutton trait_name_dict[name] action ToggleSetMembership(values, name)
    vbox xpos 0 yalign 0.9:
        textbutton "完成" action Return(values)

screen negative_choice():
    default values = set()
    style_prefix "choice"
    $ negative_traits_list = ["Plain", "Scars", "Mean", "Rude", "Cold", "Weak", "Rough", "Defiant", "Scruffy", "Plump", "Timid", "Vulgar", "Tame", "Frail", "Jaded", "Rebellious", "Lazy", "Sickly", "Homely", "Expensive", "Slow", "Distrustful", "Fearful", "Vulnerable", "Unlucky", "All thumbs", "Awkward", "Brutal", "Dumb", "Oafish", "Clumsy", "Prude", "Naive", "Square"]

    text text11 + text22
    text "{color=#F78181}{b}负面特质{/b}{/color}" size 30 ypos 100 xalign 0.5
    for index, name in enumerate(negative_traits_list):
        hbox xpos (index%6)*0.18 ypos 140+index//6*40:
            textbutton trait_name_dict[name] action ToggleSetMembership(values, name)
    vbox xpos 0 yalign 0.9:
        textbutton "完成" action Return(values)

screen personality_choice():
    default values = set()
    style_prefix "choice"
    $ personalities_list = ["Pervert", "Rebel", "Cold", "Nerd", "Masochist", "Meek", "Sweet", "Superficial", "Bimbo", "Holy", "Helper", "Creep", "Repressed", "Schemer", "Prude", "Princess", "Pet", "Easy", "Class president", "Tsundere", "Loyal", "Yandere", "Stubborn"]

    text text11 + text22
    for index, name in enumerate(personalities_list):
        hbox xpos (index%2)*0.95 ypos 200+index//2*40:
            textbutton personalities_related_dict[name] action ToggleSetMembership(values, name)
    vbox xpos 0 yalign 0.9:
        textbutton "完成" action Return(values)

screen act_choice():
    default values = set()
    style_prefix "choice"
    $ acts_list = ["Naked", "Service", "Sex", "Anal", "Fetish", "Bisexual", "Group"]

    text text11 + text22
    for index, name in enumerate(acts_list):
        hbox xpos (index%7)*0.15 ypos 100+index//7*40:
            textbutton girl_related_dict[name] action ToggleSetMembership(values, name)
    vbox xpos 0 yalign 0.9:
        textbutton "完成" action Return(values)

screen fixation_choice():
    default values = set()
    style_prefix "choice"
    $ fixations_list = ["stripping",  "public acts", "cosplay", "dildos", "vibrators", "dirty sex", "penis worship", "bondage", "oil", "wet", "submission", "femdom", "gags", "strap-ons", "roleplay", "plugs", "enemas", "beads",  "masturbation", "fingering", "handjobs", "cunnilingus", "oral", "irrumatio", "deep throat", "titjobs", "footjobs", "double penetration", "fisting", "insults", "69",  "watersports", "ass-to-mouth", "kissing", "spanking", "rimming", "fondling her boobs", "groping her ass", "lactation", "doggy style", "cowgirl", "piledriver", "spooning", "bukkake", "cum in mouth", "cum on face", "cum in hair", "cum on body", "cum shower", "swallowing", "creampie", "cum inside", "multiple orgasms", "denied orgasm", "squirting"]

    text text11 + text22
    for index, name in enumerate(fixations_list):
        hbox xpos (index%6)*0.18 ypos 100+index//6*40:
            textbutton girl_related_dict[name] action ToggleSetMembership(values, name)
    vbox xpos 0 yalign 0.9:
        textbutton "完成" action Return(values) # </neronero & RudolfU - BK.ini>

# </neronero & RudolfU - BK.ini generator>
