# <neronero & RudolfU - BK.ini>
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
                renpy.say("", "Girl path 'persistent.girl' 无法识别。")
                persistent.girl = None
                renpy.jump("generate_ini")

    menu:
        "这将会生成一个{b}_BK.ini{/b}文件在角色包内，警告: 如果角色包内已经有一个BK.ini文件，这将覆盖它。"
        "继续":
            $ ini_header = "#### " + persistent.girl[len("images/"):] + " - 用标签工具生成的适用于青楼之王0.3版本的BK.ini  #### \n\n" 
            $ ini_header += "## 这个可选文件包含一个特定女孩的高级配置数据。不需要的变量可以删除。 \n"
            $ ini_header += "## 该文件应该命名为“_BK.ini”，并放在相关的girl文件夹中。 \n"
            $ ini_header += "## 整行注释是用双哈希引入的 (##) \n"
            $ ini_header += "## 使用散列（#）或分号添加同一行注释 (;) \n"
            $ ini_header += "## 注释: 克隆选项现在是每个选项的一部分，但是仍然支持带有专用[cloning options]部分的遗留格式。 \n\n\n"


            $ ini_identity = "[identity] \n \n"
            $ ini_identity += "## 角色姓名 ## \n \n"
          
            $ ini_identity += "first_name = \"" + str(renpy.input("请输入女孩的名字:", default=persistent.girl[len("images/"):])) + "\" # 如果没有或为空，名字将被随机化 \n"
            $ ini_identity += "last_name = \"" + str(renpy.input("请输入女孩的姓氏:", default=persistent.girl[len("images/"):])) + "\" # 如果没有或为空，她将没有姓氏 \n"
            $ ini_identity += "inverted_name = " + str(renpy.call_screen("yesno_prompt", "你想要让她的姓氏和名字倒序显示吗? (东亚人名习惯)", Return(True), Return(False))) + " #如果为True， 全名将显示姓氏在名字之前，例如： \'Spears Britney\'。 \n\n"
            
            $ ini_identity += "## 女孩包数据 ## \n \n"
            
            $ ini_identity += "creator = \"" + str(renpy.input("请填上你的名字，这样我们就知道是谁创造了这个华丽的女孩包:", default="Anon")) + "\" \n"
            
            $ ini_identity += "version = \"" + str(renpy.input("给这个包一个版本号:", default="v1.0")) + "\" # 版本号显示在女孩包的浏览界面，这可以帮助玩家了解你的女孩包是何时更新的。您可以使用您喜欢的任何版本号命名格式。\n"
            $ ini_identity += "description = \"" + str(renpy.input("给这个包一个自定义描述，这将显示在女孩包的浏览界面:", default="Enjoy my girlpack!")) + "\" # 描述将显示在女孩包的浏览界面。\n\n"

            $ ini_identity += "## 克隆设置 ## \n"
            $ ini_identity += "## 这些选项定义了原始女孩的“克隆体”在生成时的设置。 \n"
            $ ini_identity += "## 在一局游戏中只能有一个原始女孩，以及任意数量的克隆人。 \n\n"
            
            $ show_clone_options = True

            menu:
                "{b}独一无二{/b} - 你想让游戏内只能生成她的本体角色吗？"
                "是的，她是独一无二的":
                    $ ini_identity += "unique = True #如果为True， 克隆人不会生成，只有本体的女孩。所有其他克隆选项将不起作用。\n"
                    $ ini_identity += "keep_first_name = True #如果为True，克隆人将与本体保持相同的名字\nkeep_last_name = False #如果为True，克隆人将与本体保持相同的姓氏\nkeep_inverted = False #如果为True，克隆人将遵循您为本体设置的姓名顺序\n\n\n"
                    
                    $ show_clone_options = False

                "\n不，允许生成克隆人\n":
                    $ ini_identity += "unique = False ##如果为True， 克隆人不会生成，只有本体的女孩。所有其他克隆选项将不起作用。 \n"
                    
                    menu:
                        "{b}克隆人的名字{/b} - 她的克隆人应该如何命名？"
                        "保留她的名字":
                            $ ini_identity += "keep_first_name = True #如果为True， 克隆人将与本体保持相同的名字\n"
                        "随机生成名字":
                            $ ini_identity += "keep_first_name = False #如果为True， 克隆人将与本体保持相同的名字\n"
                            
                    menu:
                        "{b}克隆人的姓氏{/b} - 她的克隆人应该如何命名？"
                        "保留她的姓氏":
                            $ ini_identity += "keep_last_name = True #如果为True， 克隆人将与本体保持相同的姓氏\n"
                        "随机生成姓氏":
                            $ ini_identity += "keep_last_name = False #如果为True， 克隆人将与本体保持相同的姓氏\n"
                            
                    menu:
                        "{b}克隆人的名字顺序{/b} - 克隆人是否应该遵循您为本体设置的姓名顺序？"
                        "是":
                            $ ini_identity += "keep_inverted = True #如果为True， 克隆人将遵循您为本体设置的姓名顺序\n\n"
                        "否":
                            $ ini_identity += "keep_inverted = False #如果为True， 克隆人将遵循您为本体设置的姓名顺序\n\n"

            $ ini_skills = "[base skills] \n \n"
            
            $ ini_skills += "## 女孩的属性 ##\n"
            $ ini_skills += "## 属性评级由1到5 (1 代表很糟糕, 3 代表平均水平, 5 代表远超常人。 游戏内还会产生一些变化。) \n"
            $ ini_skills += "## 对于想要随机生成的属性，跳过设置或将其设置为0 \n"
            $ ini_skills += "## 外貌: 影响按摩技师和性交的表现\n身材: 影响脱衣舞娘和肛交的表现\n魅力: 影响女服务员和侍奉的表现\n优雅: 影响表演艺妓和调教的表现\n敏感: 影响侍奉和客人的满意度\n性欲: 影响性交和接客人数\n体质: 影响肛交和精力上限\n服从: 影响调教和服从性 \n \n"
            
            "{i}接下来让我们确定女孩的初始属性状态。游戏内还会产生一些细微的变化。{/i}"
            
            $ ini_skills += "beauty = "

            menu:
                "{b}外貌{/b} - 属性越高她的外表越美丽。影响她作为{b}按摩技师{/b}时的表现以及{b}性交{/b}时的技术。"
                "糟糕":
                    $ ini_skills += "1"
                "平庸":
                    $ ini_skills += "2"
                "平均":
                    $ ini_skills += "3"
                "优秀":
                    $ ini_skills += "4"
                "卓越":
                    $ ini_skills += "5"
                "\n随机生成\n":
                    $ ini_skills += "0"
            
            $ ini_skills += "\n"
            $ ini_skills += "body = "

            menu:
                "{b}身材{/b} - 属性越高她的身材越火辣。影响她作为{b}脱衣舞娘{/b}时的表现以及{b}肛交{/b}时的技术。"
                "糟糕":
                    $ ini_skills += "1"
                "平庸":
                    $ ini_skills += "2"
                "平均":
                    $ ini_skills += "3"
                "优秀":
                    $ ini_skills += "4"
                "卓越":
                    $ ini_skills += "5"
                "\n随机生成\n":
                    $ ini_skills += "0"
            
            $ ini_skills += "\n"
            $ ini_skills += "charm = "

            menu:
                "{b}魅力{/b} - 属性越高她的魅力越迷人。影响她作为{b}女服务员{/b}时的表现以及{b}侍奉{/b}时的技术。"
                "糟糕":
                    $ ini_skills += "1"
                "平庸":
                    $ ini_skills += "2"
                "平均":
                    $ ini_skills += "3"
                "优秀":
                    $ ini_skills += "4"
                "卓越":
                    $ ini_skills += "5"
                "\n随机生成\n":
                    $ ini_skills += "0"
            
            $ ini_skills += "\n"
            $ ini_skills += "refinement = "

            menu:
                "{b}优雅{/b} - 属性越高她的举止越优雅。影响她作为{b}表演艺伎{/b}时的表现以及{b}调教{/b}时的技术。"
                "糟糕":
                    $ ini_skills += "1"
                "平庸":
                    $ ini_skills += "2"
                "平均":
                    $ ini_skills += "3"
                "优秀":
                    $ ini_skills += "4"
                "卓越":
                    $ ini_skills += "5"
                "\n随机生成\n":
                    $ ini_skills += "0"
            
            $ ini_skills += "\n"
            $ ini_skills += "libido = "

            menu:
                "{b}性欲{/b} - 属性越高她的性欲越旺盛。影响她作为{b}脱衣舞娘{/b}时的表现,{b}性交{/b}时的技术以及最大{b}接客{/b}人数。"
                "糟糕":
                    $ ini_skills += "1"
                "平庸":
                    $ ini_skills += "2"
                "平均":
                    $ ini_skills += "3"
                "优秀":
                    $ ini_skills += "4"
                "卓越":
                    $ ini_skills += "5"
                "\n随机生成\n":
                    $ ini_skills += "0"
            
            $ ini_skills += "\n"
            $ ini_skills += "obedience = "

            menu:
                "{b}服从{/b} - 属性越高她的服从性越强。影响她作为{b}表演艺伎{/b}时的表现,{b}调教{/b}时的技术以及对 {b}工作{/b}或{b}训练{/b}的接受程度。"
                "糟糕":
                    $ ini_skills += "1"
                "平庸":
                    $ ini_skills += "2"
                "平均":
                    $ ini_skills += "3"
                "优秀":
                    $ ini_skills += "4"
                "卓越":
                    $ ini_skills += "5"
                "\n随机生成\n":
                    $ ini_skills += "0"
            
            $ ini_skills += "\n"
            $ ini_skills += "constitution = "

            menu:
                "{b}体质{/b} - 属性越高她的身体越健壮。影响她作为{b}女服务员{/b}时的表现,{b}肛交{/b}时的技术,提高她的 {b}体力{/b}上限并且能够接待 {b}更多顾客{/b}。"
                "糟糕":
                    $ ini_skills += "1"
                "平庸":
                    $ ini_skills += "2"
                "平均":
                    $ ini_skills += "3"
                "优秀":
                    $ ini_skills += "4"
                "卓越":
                    $ ini_skills += "5"
                "\n随机生成\n":
                    $ ini_skills += "0"
            
            $ ini_skills += "\n"
            $ ini_skills += "sensitivity = "

            menu:
                "{b}敏感{/b} - 属性越高她的身体越敏感。影响她作为{b}按摩技师{/b}时的表现,{b}侍奉{/b}时的技术以及提升更多的 {b}顾客满意度{/b}。"
                "糟糕":
                    $ ini_skills += "1"
                "平庸":
                    $ ini_skills += "2"
                "平均":
                    $ ini_skills += "3"
                "优秀":
                    $ ini_skills += "4"
                "卓越":
                    $ ini_skills += "5"
                "\n随机生成\n":
                    $ ini_skills += "0"
            
            $ ini_skills += "\n\n"

            $ ini_skills += "## 克隆设置 ##\n"
            if show_clone_options:
                menu:
                    "{b}克隆人的属性{/b} - 克隆人是否套用本体的属性设置 (外貌，身材，魅力等等...)"
                    "是":
                        $ ini_skills += "keep_skills = True # 如果为True, 克隆人将与本体共用一套属性设置\n"
                    "否, 让她的属性随机生成":
                        $ ini_skills += "keep_skills = False # 如果为True, 克隆人将与本体共用一套属性设置\n"

            else:
                $ ini_skills += "keep_skills = False # 如果为True, 克隆人将与本体共用一套属性设置"
                 
            $ ini_skills += "\n\n\n"

            $ ini_positive_traits = "[base positive traits] \n \n"
            
            "{i}女孩通常会有2个正面特质和1个负面特质。 你可以决定一些特质出现在女孩身上的概率。{/i}"
            
            $ ini_positive_traits += "## 一个女孩在游戏中只能有2个正面特质。金色特质也视为正面特质。 \n"
            $ ini_positive_traits += "## Trait names must be between quotes (""), spelled exactly as they are in-game. See BKtraits.rpy for the full list of trait names. \n \n"
            
            $ renpy.say(narrator, "选择她{b}总是{/b}拥有的正面和金色特质。我们不建议设置这一项，这会让随机生成的女孩失去神秘感。")
            $ ini_positive_traits += "## 女孩将永远具有这些特质（最多nb个特质）。谨慎使用，这会让随机生成的女孩失去神秘感。 \n"
            call screen positive_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_positive_traits += "always = [" + str(txt) + "] \n \n"
            
            $ renpy.say(narrator, "选择她{b}大概率{/b}拥有的正面和金色特质。")
            $ ini_positive_traits += "## 女孩更容易拥有这些特质。\n"
            call screen positive_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_positive_traits += "often = [" + str(txt) + "] \n \n"
            
            $ renpy.say(narrator, "选择她{b}小概率{/b}拥有的正面和金色特质。")
            $ ini_positive_traits += "## 女孩更难拥有这些特质。 \n"
            call screen positive_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_positive_traits += "rarely = [" + str(txt) + "] \n \n"
            
            $ renpy.say(narrator, "选择她{b}不会{/b}拥有的正面和金色特质。")
            $ ini_positive_traits += "## 女孩无法拥有这些特质。 \n"
            call screen positive_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_positive_traits += "never = [" + str(txt) + "] \n \n \n"

            $ ini_negative_traits = "[base negative traits] \n \n"
            
            $ renpy.say(narrator, "选择她{b}总是{/b}拥有的负面特质。我们不建议设置这一项，这会让随机生成的女孩失去神秘感。")
            $ ini_negative_traits += "## 女孩将永远具有这些特质（最多nb个特质）。谨慎使用，这会让随机生成的女孩失去神秘感。 \n"
            call screen negative_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_negative_traits += "always = [" + str(txt) + "] \n \n"
            
            $ renpy.say(narrator, "选择她{b}大概率{/b}拥有的负面特质。")
            $ ini_negative_traits += "## 女孩更容易拥有这些特质。 \n"
            call screen negative_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_negative_traits += "often = [" + str(txt) + "] \n \n"
            
            $ renpy.say(narrator, "选择她{b}小概率{/b}拥有的负面特质。")
            $ ini_negative_traits += "## 女孩更难拥有这些特质。 \n"
            call screen negative_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_negative_traits += "rarely = [" + str(txt) + "] \n \n"
            
            $ renpy.say(narrator, "选择她{b}永不{/b}拥有的负面特质。")
            $ ini_negative_traits += "## 女孩无法拥有这些特质。 \n"
            call screen negative_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_negative_traits += "never = [" + str(txt) + "] \n \n"

            hide screen ini_negative_traits_list

            $ ini_negative_traits += "## 克隆设置 ##\n"
            if show_clone_options:
                menu:
                    "{b}克隆人的特质{/b} - 克隆人是否与本体拥有一样的特质设置?"
                    "是":
                        $ ini_negative_traits += "keep_traits = True #如果为True，克隆人将与本体共用特质设置\n"
                    "不，让她随机生成":
                        $ ini_negative_traits += "keep_traits = False #如果为True，克隆人将与本体共用特质设置\n"
            else:
                $ ini_negative_traits += "keep_traits = True #如果为True，克隆人将与本体共用特质设置\n"
                 
            $ ini_negative_traits += "\n\n"

            $ ini_personality = "[base personality] \n \n"

            show screen ini_personality_list()
            
            "{i}女孩的个性决定了她对玩家行为的反应，包括对话内容和玩法。{/i}"
    
            $ ini_personality += "## 个性设置 ##\n"
            $ ini_personality += "## 游戏中有24种个性类型: pervert, rebel, cold, nerd, masochist, masochist2, meek, sweet, superficial, bimbo, holy, helper, creep, repressed, schemer, prude, princess, pet, easy, class president, tsundere, loyal, yandere, stubborn\n"
            $ ini_personality += "## 一个女孩只能有一种个性。浏览BKinit_variables.rpy中的'gpersonalities'获取详细的个性介绍。\n\n"
            
            $ renpy.say(narrator, "选择她{b}总是{/b}拥有的个性。我们不建议设置这一项，这会让随机生成的女孩失去神秘感。")
            call screen personality_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_personality += "always = [" + str(txt) + "] # 我们不建议设置这一项，这会让随机生成的女孩失去神秘感。 \n"
            
            $ renpy.say(narrator, "选择她{b}大概率{/b}拥有的个性。")
            call screen personality_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_personality += "often = [" + str(txt) + "]\n"
            
            $ renpy.say(narrator, "选择她{b}小概率{/b}拥有的个性。")
            call screen personality_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_personality += "rarely = [" + str(txt) + "]\n"
            
            $ renpy.say(narrator, "选择她{b}不会{/b}拥有的个性。")
            call screen personality_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_personality += "never = [" + str(txt) + "]\n\n"
            
            hide screen ini_personality_list
            
            $ ini_personality += "## 克隆设置 ##\n"
            if show_clone_options:
                menu:
                    "{b}克隆人的个性{/b} - 克隆人是否与本体拥有一样的个性设置？"
                    "是":
                        $ ini_personality += "keep_personality = True #如果为True，克隆人将与本体共用个性设置\n"
                    "不，让她随机生成":
                        $ ini_personality += "keep_personality = False #如果为True，克隆人将与本体共用个性设置\n"
            else:
                $ ini_personality += "keep_personality = False #如果为True，克隆人将与本体共用个性设置\n"
                
            $ ini_personality += "\n\n"
            $ ini_custom_personality = "[custom personality] \n \n"
            
            $ ini_custom_personality += "## Custom Personality Settings ##\n"
            $ ini_custom_personality += "## You may include a custom personality for your girl. This will override the 'Base personality' settings.\n"
            $ ini_custom_personality += "## This requires the inclusion of an .rpy file in your girl pack with her dialogue lines \n\n"
            
            $ ini_custom_personality += "custom_personality = False" + " # set to True to use a custom personality. This will override the 'Base personality' settings.\n"
            $ ini_custom_personality += "personality_name = \"\"" + " # give a name to the personality (warning: using an existing personality name will override that personality)\n"
            $ ini_custom_personality += "description = \"\"" + " # this text will display in the magic notebook when a girl's personality is known\n"
            $ ini_custom_personality += "attributes = (\"\",\"\")" + " # list a pair of attributes the personality will always have (warning: having more than 2 will cause bugs).\n"
            $ ini_custom_personality += "dialogue_personality_weight = 3" + " # # how much weight personality-based lines will be given compared to attribute-based and generic dialogue\n"
            $ ini_custom_personality += "dialogue_attribute_weight = 1" + " # # how much weight attribute-based lines will be given compared to personality-based and generic dialogue\n"
            $ ini_custom_personality += "generic_dialogue = True" + " # Disabled, but included here for future-proofing. Bool, decides if this personality allows for generic dialogue or not. Custom dialogue should be provided for all relevant situations if set to False.\n"
            $ ini_custom_personality += "personality_dialogue_only = None" + " # A list of topics (with quotes, between [] brackets) for which only personality-based dialogue is allowed (e.g. [\"slave first visit\", \"slave train beg\"]). All topics can be found in BKdialogue.rpy\n\n"

            $ ini_custom_personality += "custom_dialogue_label = \"\"" + " # For more complex custom dialogue, a label can be specified. It will receive the 'girl' object and the dialogue 'topic' as arguments.\n\n"
            
            $ ini_custom_personality += "\n"
            $ ini_tastes = "[tastes] \n\n"
            
            "{i}让我们来看看女孩的品味{/i}"
            
            $ ini_tastes += "## Tastes are used in chatting dialogue, and for flavor only. You may include answers that are not in vanilla choices.\n"
            $ ini_tastes += "## Leave the line out or set it to 'None' (without quotes) to randomize.\n\n"
            
            menu:
                "{b}品味{/b} - 女孩喜欢的颜色/食物/饮料。用于聊天对话中增添情趣。你可以提供不在默认列表中的独特的答案。"
                "自定义的品味":
                    $ ini_tastes += "favorite_color = \"" + str(renpy.input("最喜欢的颜色:", default="彩虹")) + "\" \n"
                    $ ini_tastes += "favorite_food = \"" + str(renpy.input("最喜欢的食物:", default="肯德基")) + "\" \n"
                    $ ini_tastes += "favorite_drink = \"" + str(renpy.input("最喜欢的饮料:", default="可口可乐")) + "\" \n\n"
                    
                    $ ini_tastes += "disliked_color = \"" + str(renpy.input("最讨厌的颜色:", default="灰色")) + "\" \n"
                    $ ini_tastes += "disliked_food = \"" + str(renpy.input("最讨厌的食物:", default="仰望星空")) + "\" \n"
                    $ ini_tastes += "disliked_drink = \"" + str(renpy.input("最讨厌的饮料:", default="白开水")) + "\" \n\n"

                "\n随机生成的品味\n":
                    $ ini_tastes += "favorite_color = None \n"
                    $ ini_tastes += "favorite_food = None \n"
                    $ ini_tastes += "favorite_drink = None \n\n"
                    
                    $ ini_tastes += "disliked_color = None \n"
                    $ ini_tastes += "disliked_food = None \n"
                    $ ini_tastes += "disliked_drink = None \n\n"

            menu:
                "{b}爱好{/b} - 一个女孩的爱好。用于聊天对话中增添情趣。每个女孩都有两个爱好。你可以提供不在默认列表中的独特的答案。"
                "自定义爱好":
                    $ ini_tastes += "hobbies = [\"" + str([renpy.input("爱好一:", default="jousting")]) + "\"，"
                    $ ini_tastes += "\"" + str([renpy.input("爱好二:", default="dancing")]) + "\"] # Hobbies must be a list of two items (with quotes, between [] brackets)\n\n"

                "\n随机生成的爱好\n":
                    $ ini_tastes += "hobbies = None # Hobbies must be a list of two items (with quotes, between [] brackets)\n\n"

            $ ini_tastes += "## 克隆设置 ##\n"
            if show_clone_options:
                menu:
                    "{b}克隆人的品味{/b} - 克隆人是否拥有与本体相同的品味/爱好设置？"
                    "是":
                        $ ini_tastes += "keep_tastes = True #如果为True， clones will keep the same tastes and hobbies\n"
                    "不，让她随机生成":
                        $ ini_tastes += "keep_tastes = False #如果为True， clones will keep the same tastes and hobbies\n"
            else:
                $ ini_tastes += "keep_personality = False #如果为True， clones will keep the same tastes and hobbies\n"

            $ ini_tastes += "\n\n"
            $ ini_sexual_preferences = "[sexual preferences] \n \n"
            
            "{i}现在我们来看看女孩的性癖。首先，回顾一下她最喜欢的性行为和性癖。{/i}"
            
            $ ini_sexual_preferences += "## Sex Acts ##\n"
            $ ini_sexual_preferences += "## You can choose positive or negative acts which will be generated more often for this girl. Possible choices are: \"naked\", \"service\", \"sex\", \"anal\", \"fetish\", \"bisexual\" and \"group\".\n\n"
            
            $ renpy.say(narrator, "她会更容易{b}喜欢{/b}哪些行为?")
            call screen act_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "favorite_acts = [" + str(txt) + "]\n"
            
            $ renpy.say(narrator, "她会更容易{b}讨厌{/b}哪些行为?")
            call screen act_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "disliked_acts = [" + str(txt) + "]\n\n"


            $ ini_sexual_preferences += "## You can choose positive or negative fixations which will be generated more often for this girl. Fixations names are found in 'fix_dict' in the 'BKinit_variables.rpy' file\n"
            $ renpy.say(narrator, "选择她{b}永远{/b}喜欢的性癖。我们不建议设置这一项，这会让随机生成的女孩失去神秘感。")
            call screen fixation_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "always_fixations = [" + str(txt) + "] # Always positive. Use with care: it makes girl generation very predictable. \n"

            $ renpy.say(narrator, "选择她{b}绝对不{/b}喜欢的性癖。注意，不喜欢并不是讨厌。")
            call screen fixation_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "never_fixations = [" + str(txt) + "] # Never positive.\n\n"
            
            $ renpy.say(narrator, "选择她{b}大概率{/b}喜欢（同时小概率讨厌）的性癖。")
            call screen fixation_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "favorite_fixations = [" + str(txt) + "] # More chance of generating as positive fixation, less as negative.\n"
            
            $ renpy.say(narrator, "选择她{b}大概率{/b}讨厌（同时小概率喜欢）的性癖。")
            call screen fixation_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "disliked_fixations = [" + str(txt) + "] # More chance of generating as negative fixation, less as positive.\n"
            
            $ renpy.say(narrator, "选择她{b}永远{/b}讨厌的性癖。我们不建议设置这一项，这会让随机生成的女孩失去神秘感。")
            call screen fixation_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "always_negative_fixations = [" + str(txt) + "] # Always negative. Use with care: it makes girl generation very predictable.\n"
            
            $ renpy.say(narrator, "选择她{b}绝对不{/b}讨厌的性癖。注意，不讨厌不等于喜欢。")
            call screen fixation_choice()
            python:
                txt = ""
                for name in _return:
                    txt += " \"%s\", " % name
                renpy.say(narrator, txt)
                ini_sexual_preferences += "never_negative_fixations = [" + str(txt) + "] # Never negative.\n\n"
            
            "{i}接下来我们将确定女孩的性经历和她的训练弱点。{/i}"
            
            $ ini_sexual_preferences += "## Prior Sexual Experience ##\n"
            $ ini_sexual_preferences += "sexual_experience = "
            
            menu:
                "{b}性经验{/b} - 女孩在遇到玩家之前有多少性经验？"
                "阅男无数":
                    $ ini_sexual_preferences += "\"very experienced\""
                "经验丰富":
                    $ ini_sexual_preferences += "\"experienced\""
                "平均水准":
                    $ ini_sexual_preferences += "\"average\""
                "情场新手":
                    $ ini_sexual_preferences += "\"inexperienced\""
                "未经人事":
                    $ ini_sexual_preferences += "\"very inexperienced\""
                "\n随机生成\n":
                    $ ini_sexual_preferences += "\"random\""
                    
            $ ini_sexual_preferences += " # How much sexual experience she has prior to meeting the player. You can choose between the following: \"very experienced\", \"experienced\",  \"average\", \"inexperienced\", \"very inexperienced\", \"random\". If left out or empty, a random level of experience will be chosen.\n\n"
            
            $ ini_sexual_preferences += "## Farm weakness ##\n"
            $ ini_sexual_preferences += "farm_weakness = "

            menu:
                "{b}训练弱点{/b} - 给女孩选择一个训练弱点。"
                "害怕种马":
                    $ ini_sexual_preferences += "\"stallion\""
                "害怕野兽":
                    $ ini_sexual_preferences += "\"beast\""
                "害怕怪物":
                    $ ini_sexual_preferences += "\"monster\""
                "害怕机械":
                    $ ini_sexual_preferences += "\"machine\""
                "\n随机生成\n":
                    $ ini_sexual_preferences += "\"random\""
            
            $ ini_sexual_preferences += " # choose between the following values: \"stallion\", \"beast\", \"monster\", \"machine\", \"random\"\n\n"

            $ ini_sexual_preferences += "## Cloning Options ##\n"
            if show_clone_options:
                menu:
                    "{b}克隆人的性癖{/b} - 克隆人是否会拥有与本体相同的性癖设置？"
                    "是":
                        $ ini_sexual_preferences += "keep_sex = True #如果为True， clones will keep the same sexual preferences and experience\n\n"
                    "不，让她随机生成":
                        $ ini_sexual_preferences += "keep_sex = False #如果为True， clones will keep the same sexual preferences and experience\n\n"
            else:
                $ ini_sexual_preferences += "keep_sex = True #如果为True， clones will keep the same sexual preferences and experience\n\n"

            $ ini_sexual_preferences += "\n"
            $ ini_background = "[background story] \n\n"

            "{i}就快完成了! 最后是关于她的背景和克隆选项。{/i}"
            
            $ show_location_options = True
            $ ini_background += "## Girl Generation ##\n"
            $ ini_background += "generate_as = "
            
            menu:
                "{b}自由之身{/b} -你想让她作为奴隶还是自由的女孩出现在游戏中？"
                "她将作为奴隶出现 (刷新在奴隶市场)":
                    $ ini_background += "\"slave\""
                    $ show_location_options = False
                "她将作为自由的女孩出现 (刷新在城市中)":
                    $ ini_background += "\"free\""
                "二者皆可":
                    $ ini_background += "\"all\""
                    
            $ ini_background += " # 可以被设置为\"all\"或局限于\"free\", \"slave\", 和\"story\"。随机遭遇事件女孩不会自动刷新，只有在特定事件中才会出现。\n"

            $ ini_background += "generate_in = "
            
            if show_location_options:
                menu:
                    "{b}出现地点{/b} - 你想让她只出现在城市的特定区域/地点吗？"
                    "是的":
                        menu:
                            "{b}地区列表{/b} - 选择她会出没的地区，每个地区有6处地点。"
                            "地区 1: 贫民窟 ":
                                menu:
                                    "你想把范围缩小到这个地区的一个特定地点吗？"
                                    "\n可以出现在本地区任意地点\n":
                                        $ ini_background += "\"The Slums\""
                                    "黑市":
                                        $ ini_background += "\"Spice market\""
                                    "下水道":
                                        $ ini_background += "\"Sewers\""
                                    "农场":
                                        $ ini_background += "\"Farm\""
                                    "瞭望塔":
                                        $ ini_background += "\"Spice market\""
                                    "废品回收站":
                                        $ ini_background += "\"Junkyard\""
                                    "盗贼公会":
                                        $ ini_background += "\"Thieves guild\""
                            "地区 2: 沿海地区":
                                menu:
                                    "你想把范围缩小到这个地区的一个特定地点吗？"
                                    "\n可以出现在本地区任意地点\n":
                                        $ ini_background += "\"The Docks\""
                                    "港口":
                                        $ ini_background += "\"Harbor\""
                                    "造船厂":
                                        $ ini_background += "\"Shipyard\""
                                    "酒馆":
                                        $ ini_background += "\"Taverns\""
                                    "海滨":
                                        $ ini_background += "\"Seafront\""
                                    "沙滩":
                                        $ ini_background += "\"Beach\""
                                    "外贸市场":
                                        $ ini_background += "\"Exotic emporium\""
                            "地区 3: 外城区 ":
                                menu:
                                    "你想把范围缩小到这个地区的一个特定地点吗？"
                                    "\n可以出现在本地区任意地点\n":
                                        $ ini_background += "\"The Warehouse\""
                                    "马场":
                                        $ ini_background += "\"Stables\""
                                    "广场":
                                        $ ini_background += "\"Plaza\""
                                    "市场":
                                        $ ini_background += "\"Market\""
                                    "行刑台":
                                        $ ini_background += "\"Gallows\""
                                    "监狱":
                                        $ ini_background += "\"Prison\""
                                    "竞技场":
                                        $ ini_background += "\"Arena\""
                            "地区 4: 魔法花园":
                                menu:
                                    "你想把范围缩小到这个地区的一个特定地点吗？"
                                    "\n可以出现在本地区任意地点\n":
                                        $ ini_background += "\"The Magic Gardens\""
                                    "温室花园":
                                        $ ini_background += "\"Botanical garden\""
                                    "空中花园":
                                        $ ini_background += "\"Hanging gardens\""
                                    "大图书馆":
                                        $ ini_background += "\"Library\""
                                    "公会总部":
                                        $ ini_background += "\"Guild quarter\""
                                    "法师公会":
                                        $ ini_background += "\"Magic guild\""
                                    "黑森林":
                                        $ ini_background += "\"Magic forest\""
                            "地区 5: 宗教领地":
                                menu:
                                    "你想把范围缩小到这个地区的一个特定地点吗？"
                                    "\n可以出现在本地区任意地点\n":
                                        $ ini_background += "\"The Cathedra\""
                                    "朝圣者大道":
                                        $ ini_background += "\"Pilgrim road\""
                                    "银行":
                                        $ ini_background += "\"Banking quarter\""
                                    "废墟":
                                        $ ini_background += "\"Old ruins\""
                                    "湖畔":
                                        $ ini_background += "\"Lakefront\""
                                    "演武场":
                                        $ ini_background += "\"Training ground\""
                                    "大教堂":
                                        $ ini_background += "\"Cathedra\""
                            "地区 6: 皇宫禁地":
                                menu:
                                    "你想把范围缩小到这个地区的一个特定地点吗？"
                                    "\n可以出现在本地区任意地点\n":
                                        $ ini_background += "\"The King's Hold\""
                                    "城墙之上":
                                        $ ini_background += "\"Battlements\""
                                    "城堡主楼":
                                        $ ini_background += "\"Keep\""
                                    "大礼堂":
                                        $ ini_background += "\"Hall\""
                                    "中庭":
                                        $ ini_background += "\"Courtyard\""
                                    "神社":
                                        $ ini_background += "\"Temple\""
                                    "大瀑布":
                                        $ ini_background += "\"Waterfalls\""
                    "不，她可以出现在任意地区":
                        $ ini_background += "\"all\""
            else:
                $ ini_background += "\"all\""
                    
            $ ini_background += "  # Can be set to \"all\" or a district or location name that must be spelled exactly as in game (including the 'The' article for districts). Handles where the girl will generate as a free girl. No effect on slave girls.\n"
            
            if show_location_options:
                menu:
                    "在玩家遇到她之后，她是否会每周随机移动到另一个地点？"
                    "是":
                        $ ini_background += "move_after_meeting = True"
                    "否，她待在那里就好":
                        $ ini_background += "move_after_meeting = False"
            else:
                $ ini_background += "move_after_meeting = True"

            $ ini_background += " # Used with the generate_in option (default=True). If True, free girls will move from their starting location normally each week after they have their first interaction with the player. If False, they remain in place. \n\n"
            
            $ ini_background += "## Origin ##\n"
            $ ini_background += "## You can provide a custom origin (if you do, make sure to include the origin description below) or just \"random\"\n"
            $ ini_background += "## Origin description must be written in the girl's own words\n\n"
            
            menu:
                "{b}背景故事{/b} - 你想写一段对话，给这个女孩一个定制的起源故事吗？"
                "是的":
                    $ ini_background += "origin = \"" + str(renpy.input("{b}家乡{/b} - 她长大的地方。", default="")) + "\"\n"
                    $ ini_background += "origin_description = \"" + str(renpy.input("{b}家乡介绍{/b} - 为你的女孩写一段对话，让她谈谈自己的家乡。", default="")) + "\"\n\n"
                    
                "不必了，套用游戏自带的预设故事模板":
                    $ ini_background += "origin = \"random\"\norigin_description = None\n\n"
                    
            $ ini_background += "## Basic Story ##\n"
            $ ini_background += "## Random slave story: write the story name(s) between quotes, as found in BKinit_variables.rpy (e.g. \"slave_story1\", \"slave_story2\"...)\n\n"
            
            show screen ini_story_list()

            menu:
                "{b}背景故事模板{/b} - 随着你对女孩了解的加深，你会知道她的身世背景。您想设置她的背景故事模板范围吗？"
                "是": 
                    $ renpy.say(narrator, "选择她{b}总是{/b}拥有的背景故事。我们不建议设置这一项，这会让随机生成的女孩失去神秘感。")
                    call screen story_choice()
                    python:
                        txt = ""
                        for name in _return:
                            txt += " \"%s\", " % name
                        renpy.say(narrator, txt)
                        ini_background += "always_slave_story = [" + str(txt) + "] # Use with care: it makes girl generation very predictable. \n"
                    
                    $ renpy.say(narrator, "选择她{b}大概率{/b}拥有的背景故事。")
                    call screen story_choice()
                    python:
                        txt = ""
                        for name in _return:
                            txt += " \"%s\", " % name
                        renpy.say(narrator, txt)
                        ini_personality += "often_slave_story = [" + str(txt) + "]\n"
                    
                    $ renpy.say(narrator, "选择她{b}小概率{/b}拥有的背景故事。")
                    call screen story_choice()
                    python:
                        txt = ""
                        for name in _return:
                            txt += " \"%s\", " % name
                        renpy.say(narrator, txt)
                        ini_personality += "rarely_slave_story = [" + str(txt) + "]\n"
                    
                    $ renpy.say(narrator, "选择她{b}永远{/b}不会拥有的背景故事。")
                    call screen story_choice()
                    python:
                        txt = ""
                        for name in _return:
                            txt += " \"%s\", " % name
                        renpy.say(narrator, txt)
                        ini_personality += "never_slave_story = [" + str(txt) + "]\n\n"
                    
                "否，让它完全随机生成":
                    $ ini_background += "always_slave_story = []\noften_slave_story = []\nrarely_slave_story = []\nnever_slave_story = []"

            hide screen ini_story_list
            
            $ ini_background += "## Custom Story ##\n"
            $ ini_background += "## If provided, this label will be called instead of a random back-story. It must take 'girl' as an argument. Replaces the random slave story above.\n"
            $ ini_background += "## See the 'slave_story' labels in BKinteractions.rpy for examples of how it might work (feel free to set up the events very differently)\n\n"
            $ ini_background += "story_label = None # provide the custom label name (between quotes)\n\n"
            
            $ ini_background += "## Custom City Event ##\n"
            $ ini_background += "## If provided, this label will be called instead of normal city interactions. It must take 'girl' as an argument.\n"
            $ ini_background += "## The regular dialog options can be called from within this custom label by using 'call free_girl_talk(girl)'\n\n"
            $ ini_background += "city_label = None # provide the custom label name (between quotes)\n\n"
            
            $ ini_background += "## Custom Night Event ##\n"
            $ ini_background += "## If provided, this label will be called every night. It must take the 'girl' argument. This could be useful to increment some values, run some tests or reset interactions.\n"
            $ ini_background += "## It is recommended that such labels run silent and add a StoryEvent if necessary.\n\n"
            $ ini_background += "night_label = None # provide the custom label name (between quotes)\n\n"
            
            $ ini_background += "## Custom Interaction ##\n"
            $ ini_background += "## This adds a custom button to the regular slave interact menu. Leave it out or set value to None or empty brackets if you are not using it.\n\n"
            $ ini_background += "interact_prompt = None # Example usage: (\"Visit her room\", \"my_interaction_label\", 1) The first string refers to the caption of the button. The second is the label which will be called upon clicking the button. The integer is the AP cost (for UI display only, it isn't deducted from MC actions outside of your label code for flexibility). It must take 'girl' as an argument.\n\n"

            $ ini_background += "## Custom Initialization Function ##\n"
            $ ini_background += "## If provided, this function will be called when a girl with this template is created, after randomization.\n"
            $ ini_background += "## Write the function in an init block in _events.rpy or another custom .rpy file.\n"
            $ ini_background += "## It must take 'girl' as an argument. It must not interrupt game flow (python only, no ren'py calls or jumps).\n\n"
            $ ini_background += "init_function = None # provide a custom function name that is called after girl creation (between quotes)\n\n"

            $ ini_cloning = "## 克隆设置 ##\n"
            if show_clone_options:
                menu:
                    "{b}克隆人的自由状态{/b} - 克隆人是否应该保留本体的自由/奴隶状态的设置？"
                    "是":
                        $ ini_cloning += "keep_generate_as = True # If False, clones will be generated both as slave and free girls regardless of the original setting. True will keep the 'generate_in' setting as well\n"
                    "否, 让克隆人随机生成":
                        $ ini_cloning += "keep_generate_as = False # If False, clones will be generated both as slave and free girls regardless of the original setting. True will keep the 'generate_in' setting as well\n"

                menu:
                    "{b}克隆人的背景故事{/b} - 克隆人是否拥有和本体一样的背景故事？"
                    "是":
                        $ ini_cloning += "keep_background = True #如果为True， clones will keep the same origin and background story events\n"
                    "否, 让克隆人随机生成":
                        $ ini_cloning += "keep_background = False #如果为True， clones will keep the same origin and background story events\n"
            else:
                $ ini_cloning += "keep_generate_as = True # If False, clones will be generated both as slave and free girls regardless of the original setting. True will keep the 'generate_in' setting as well\n"
                $ ini_cloning += "keep_background = True #如果为True， clones will keep the same origin and background story events\n"
                
                $ ini_cloning += "keep_interactions = True # #如果为True， clones will keep the same interactions options and custom city/night events\n"
                $ ini_cloning += "keep_init = True #如果为True， clones will keep the same init function\n\n\n"
                $ ini_cloning += "#### 文件末尾 ####"
    
                    
            python:

                txtFile = open(config.gamedir + "/" + persistent.girl + "/_BK.ini", "w")

                txtFile.writelines(ini_header + ini_identity + ini_skills + ini_positive_traits + ini_negative_traits + ini_personality + ini_custom_personality + ini_tastes + ini_sexual_preferences + ini_background + ini_cloning)

                txtFile.close()

        "返回菜单":
            return

    return # </neronero & RudolfU - BK.ini>



# ----------------------------- SCREENS -----------------------------



screen ini_positive_traits_list(): 
    
    frame xalign 0.5 xmaximum 0.9 xpadding 20 ypadding 50 yalign 0.5 background "#002244":
        
        has vbox spacing 20 xmaximum 0.9
        
        $ text_positive = "{b}金色特质{/b}\n"
        $ gold_traits_list = ["Naughty", "Fascinating", "Lust", "Warrior", "Skilled tongue", "Always wet", "Tight ass", "Playful", "Wild", "Dirty mind", "Magnetic", "Loose", "Dedicated", "Provocative", "Fashionista", "Perfectionist", "Elite", "Gifted", "Fast learner", "Caster", "Driven", "Country girl", "Noble", "Naturist", "Vicious"]
        
        $ positive_traits_list = ["Cute", "Long legs", "Nice boobs", "Juicy ass", "Sweet", "Exotic", "Polite", "Feminine", "Horny", "Resilient",  "Delicate", "Meek", "Pretty eyes", "Firm tits", "Seductive", "Graceful", "Beautiful", "Fit", "Charming", "Elegant", "Slutty", "Athletic", "Sensitive", "Obedient", "Energetic", "Tough", "Sexy", "Humble", "Virgin", "Sharp", "Loyal", "Brave", "Strong", "Lucky", "Deft", "Nimble", "Soft skin", "Bright", "Agile", "Brisk", "Rowdy", "Powerful", "Unhurried", "Modest", "Sensual", "Kinky", "Pervert", "Thief"]
        
        python:
            for trait in gold_traits_list:
                text_positive += "\"" + trait + "\", " 
                
            text_positive += "\n\n{b}正面特质{/b}\n"
                
            for trait in positive_traits_list:
                text_positive += "\"" + trait + "\", " 
        
        text text_positive size 18 color "#ffffff"
        
screen ini_negative_traits_list():
    
    frame xalign 0.5 xmaximum 0.9 xpadding 20 ypadding 50 yalign 0.5 background "#002244":
        
        has vbox spacing 20 xmaximum 0.9
        
        $ text_negative = "{b}负面特质{/b}\n"
        $ negative_traits_list = ["Plain", "Scars", "Mean", "Rude", "Cold", "Weak", "Rough", "Defiant", "Scruffy", "Plump", "Timid", "Vulgar", "Tame", "Frail", "Jaded", "Rebellious", "Lazy", "Sickly", "Homely", "Expensive", "Slow", "Distrustful", "Fearful", "Vulnerable", "Unlucky", "All thumbs", "Awkward", "Brutal", "Dumb", "Oafish", "Clumsy", "Prude", "Naive", "Square"]
        
        python:
            for trait in negative_traits_list:
                text_negative += "\"" + trait + "\", " 
       
        text text_negative size 18 color "#ffffff" 
        
screen ini_personality_list():
    
    frame xalign 0.5 xmaximum 0.9 xpadding 20 ypadding 50 yalign 0.5 background "#002244":
        
        has vbox spacing 20 xmaximum 0.9
        
        $ text_personality = "{b}角色的个性{/b}\n\n"
        $ personalities_list = ["{b}\"堕落\"{/b} - 狂野，不受限制的那种女孩。对各种性行为感到好奇，越变态越好。不喜欢弯弯绕绕的浪漫。", 
        "{b}\"叛逆\"{/b} - 总是与他人斗争，产生矛盾，非常独立。必须按照自己的自由意志行事。", 
        "{b}\"冷血\"{/b} - 她冷血无情，不轻易表达自己的感情。奇怪的是，她似乎对周围发生的事情漠不关心，对别人的命运也不感兴趣。", 
        "{b}\"书呆子\"{/b} - 安静而博学。有很强的好奇心。不喜欢体力劳动。", 
        "{b}\"受虐狂\"{/b} - 被贬低得越过分越好。她喜欢处于底层，暗地里喜欢被人虐待。礼物和爱的示好会惹恼她，她不值得拥有这些。", 
        "{b}\"虚荣\"{/b} - 虚荣，渴望关注，关心地位和财富。喜欢礼物和赞美。她会毫不犹豫地用自己的身体换取这些东西。",
        "{b}\"内向\"{/b} - 害羞，容易动摇，面对侵害会哭而不是抵抗。不喜欢冲突。",
        "{b}\"开朗\"{/b} - 性格开朗可爱。总是积极向上的。喜欢浪漫的行为。不喜欢消极的情绪。",
        "{b}\"社交达人\"{/b} - 每一个社交名媛，都在乎别人的目光，最好是穿着最显眼的衣服，戴着最昂贵的珠宝。有些人说她需要别人的关注，但她知道他们只是嫉妒她的新鞋...",
        "{b}\"狂热信徒\"{/b} - 她是宗教和道德的卫道士，每天晚上都在祈祷，并试图劝说他人皈依她的信仰。虽然目前还没有成功，但她不会放弃。",
        "{b}\"热心肠\"{/b} - 她总是乐于帮助她的朋友，把自己的利益放在别人后面。有时会有点爱管闲事。",
        "{b}\"社恐\"{/b} - 她在人群中显得害羞而笨拙，沉迷于独自一人思考各种肮脏的话题。因为跟踪而被投诉的人很多。",
        "{b}\"克制\"{/b} - 在一个非常严格的环境中长大，她生活在对自己冲动的恐惧中，并尽最大努力抑制它们。",
        "{b}\"梦想家\"{/b} - 喜欢策划和制定宏伟的计划，随时准备对所有生物宣称她的统治地位...如果有那一天。与此同时，如果她要舔鸡巴...那就随她去吧。",
        "{b}\"假正经\"{/b} - 装出一副随时都敬畏太阳神的模样。不赞成轻浮和不道德的行为。有些人认为她内心深处掩藏着肮脏的想法，但如果是这样，她隐藏得很好。",
        "{b}\"公主病\"{/b} - 一个象征性的公主（或者她曾经真的是？），她认为每个人都应该为她服务，并满足她的每一个要求。她可能很残忍，但大多数时候她也很天真。",
        "{b}\"乖乖女\"{/b} - 老师的宠儿。总是准备好取悦主人，喜欢舒适地生活在他的庇护下。有些人认为她缺乏独立性，在背后辱骂她。",
        "{b}\"万人迷\"{/b} - 这不是她的错，她总是能吸引男人，而且从不忍心拒绝他们。虽然很多人说她很随和，但她唯一的目的是传播快乐而不是性病。",
        "{b}\"模范\"{/b} - 她必须永远处于领先地位，努力成为榜样，鄙视各种不正当的行为。她对别人的高期望反映了她对自己的严格要求。",
        "{b}\"傲娇\"{/b} - 她容易生气，很难取悦，她有一个秘密的软肋。会冒着风险去帮助别人，但首先得痛骂羞辱别人一番。",
        "{b}\"尽职尽责\"{/b} - 总是服从命令，更多的是出于责任感而不是恐惧。认为每个人都必须摆正自己的位置，并在他们所从事的工作中做到最好。包括妓女。",
        "{b}\"病娇\"{/b} - 很火辣，很神经质，但也很疯狂。愿意付出一切代价来博得意中人的心，扼杀竞争对手...实际上是掐死他们。",
        "{b}\"古板\"{/b} - 不喜欢和她的原则和道德价值观不一致的人，也不喜欢矛盾。她会让派对变得有趣起来，如果你喜欢以斗殴收尾的派对的话。"]
        
        python:
            for personality in personalities_list:
                text_personality += personality + "\n" 
       
        text text_personality size 16 color "#ffffff" 
        
screen ini_fixations_list():
    
    frame xalign 0.5 xmaximum 0.9 xpadding 20 ypadding 50 yalign 0.5 background "#002244":
        
        has vbox spacing 20 xmaximum 0.9
        
        $ text_fixations = "{b}性癖{/b}\n"
        $ fixations_list = ["stripping",  "public acts", "cosplay", "dildos", "vibrators", "dirty sex", "penis worship", "bondage", "oil", "wet", "submission", "femdom", "gags", "strap-ons", "roleplay", "plugs", "enemas", "beads",  "masturbation", "fingering", "handjobs", "cunnilingus", "oral", "irrumatio", "deep throat", "titjobs", "footjobs", "double penetration", "fisting", "insults", "69",  "watersports", "ass-to-mouth", "kissing", "spanking", "rimming", "fondling her boobs", "groping her ass", "lactation", "doggy style", "cowgirl", "piledriver", "spooning", "bukkake", "cum in mouth", "cum on face", "cum in hair", "cum on body", "cum shower", "swallowing", "creampie", "cum inside", "multiple orgasms", "denied orgasm", "squirting"]
        
        python:
            for fixation in fixations_list:
                text_fixations += "\"" + fixation + "\", " 
       
        text text_fixations size 18 color "#ffffff" 

screen ini_story_list():
    
    frame xalign 0.5 xmaximum 0.9 xpadding 20 ypadding 50 yalign 0.1 background "#002244":
        
        has vbox spacing 20 xmaximum 0.9
        
        $ text_story = "{b}背景故事{/b}\n\n"
        $ stories_list = ["{b}\"故事模板1\"{/b} - 一个关于爱情和背叛的背景故事", 
        "{b}\"故事模板2\"{/b} - 一个关于债务和苦难的背景故事", 
        "{b}\"故事模板3\"{/b} -一个关于生与死的背景故事", 
        "{b}\"故事模板4\"{/b} - 一个关于贪婪和贫穷的背景故事", 
        "{b}\"故事模板5\"{/b} - 一个关于罪与罚的背景故事", 
        "{b}\"故事模板6\"{/b} - 一个光荣而有意义的背景故事",
        "{b}\"故事模板7\"{/b} - 一个关于奉献和牺牲的背景故事",
        "{b}\"故事模板8\"{/b} - 一个关于魔法和诅咒的背景故事"]
        
        python:
            for story in stories_list:
                text_story += story + "\n" 
       
        text text_story size 16 color "#ffffff"         

# Make sure you check RenPy documentation.
# Especially Screen Language and Screen Actions
screen positive_choice():
    default values = set()
    style_prefix "choice"
    $ gold_traits_list = ["Naughty", "Fascinating", "Lust", "Warrior", "Skilled tongue", "Always wet", "Tight ass", "Playful", "Wild", "Dirty mind", "Magnetic", "Loose", "Dedicated", "Provocative", "Fashionista", "Perfectionist", "Elite", "Gifted", "Fast learner", "Caster", "Driven", "Country girl", "Noble", "Naturist", "Vicious", "Conduct"]
    $ positive_traits_list = ["Cute", "Long legs", "Nice boobs", "Juicy ass", "Sweet", "Exotic", "Polite", "Feminine", "Horny", "Resilient",  "Delicate", "Meek", "Pretty eyes", "Firm tits", "Seductive", "Graceful", "Beautiful", "Fit", "Charming", "Elegant", "Slutty", "Athletic", "Sensitive", "Obedient", "Energetic", "Tough", "Sexy", "Humble", "Virgin", "Sharp", "Loyal", "Brave", "Strong", "Lucky", "Deft", "Nimble", "Soft skin", "Bright", "Agile", "Brisk", "Rowdy", "Powerful", "Unhurried", "Modest", "Sensual", "Kinky", "Pervert", "Thief", "Sane", "Trusting", "Loving"]
        
    text "{color=#FFD700}{b}Gold Traits{/b}{/color}" size 18
    for index, name in enumerate(gold_traits_list):
        hbox xpos (index%6)*0.18 ypos 140+index//6*40:
            if name in trait_name_dict :
                textbutton trait_name_dict[name] action ToggleSetMembership(values, name)
            else:
                textbutton name action ToggleSetMembership(values, name)
    text "{color=#009874}{b}Positive Traits{/b}{/color}" size 18 ypos 300
    for index, name in enumerate(positive_traits_list):
        hbox xpos (index%6)*0.18 ypos 440+index//6*40:
            textbutton trait_name_dict[name] action ToggleSetMembership(values, name)
    vbox xpos 0 yalign 0.9:
        textbutton "完成" action Return(values)

screen negative_choice():
    default values = set()
    style_prefix "choice"
    $ negative_traits_list = ["Plain", "Scars", "Mean", "Rude", "Cold", "Weak", "Rough", "Defiant", "Scruffy", "Plump", "Timid", "Vulgar", "Tame", "Frail", "Jaded", "Rebellious", "Lazy", "Sickly", "Homely", "Expensive", "Slow", "Distrustful", "Fearful", "Vulnerable", "Unlucky", "All thumbs", "Awkward", "Brutal", "Dumb", "Oafish", "Clumsy", "Prude", "Naive", "Square", "Insane", "Distrustful", "Spiteful"]
     
    text "{color=#F78181}{b}Negative Traits{/b}{/color}" size 18
    for index, name in enumerate(negative_traits_list):
        hbox xpos (index%6)*0.18 ypos 140+index//6*40:
            textbutton trait_name_dict[name] action ToggleSetMembership(values, name)
    vbox xpos 0 yalign 0.9:
        textbutton "完成" action Return(values)
      
screen personality_choice():
    default values = set()
    style_prefix "choice"      
    $ personalities_list = ["Pervert", "Rebel", "Cold", "Nerd", "Masochist", "Meek", "Sweet", "Superficial", "Bimbo", "Holy", "Helper", "Creep", "Repressed", "Schemer", "Prude", "Princess", "Pet", "Easy", "Class president", "Tsundere", "Loyal", "Yandere", "Stubborn"]
    
    for index, name in enumerate(personalities_list):
        hbox xpos (index%2)*0.95 ypos 200+index//2*40:
            textbutton personalities_related_dict[name] action ToggleSetMembership(values, name)
    vbox xpos 0 yalign 0.9:
        textbutton "完成" action Return(values)
        
screen act_choice():
    default values = set()
    style_prefix "choice"    
    $ acts_list = ["Naked", "Service", "Sex", "Anal", "Fetish", "Bisexual", "Group"]    
    
    for index, name in enumerate(acts_list):
        hbox xpos (index%7)*0.15 ypos 100+index//7*40:
            textbutton girl_related_dict[name] action ToggleSetMembership(values, name)
    vbox xpos 0 yalign 0.9:
        textbutton "完成" action Return(values)
        
screen fixation_choice():
    default values = set()
    style_prefix "choice"    
    $ fixations_list = ["stripping",  "public acts", "cosplay", "dildos", "vibrators", "dirty sex", "penis worship", "bondage", "oil", "wet", "submission", "femdom", "gags", "strap-ons", "roleplay", "plugs", "enemas", "beads",  "masturbation", "fingering", "handjobs", "cunnilingus", "oral", "irrumatio", "deep throat", "titjobs", "footjobs", "double penetration", "fisting", "insults", "69",  "watersports", "ass-to-mouth", "kissing", "spanking", "rimming", "fondling her boobs", "groping her ass", "lactation", "doggy style", "cowgirl", "piledriver", "spooning", "bukkake", "cum in mouth", "cum on face", "cum in hair", "cum on body", "cum shower", "swallowing", "creampie", "cum inside", "multiple orgasms", "denied orgasm", "squirting"]
       
    for index, name in enumerate(fixations_list):
        hbox xpos (index%6)*0.18 ypos 100+index//6*40:
            textbutton girl_related_dict[name] action ToggleSetMembership(values, name)
    vbox xpos 0 yalign 0.9:
        textbutton "完成" action Return(values)

screen story_choice():
    default values = set()
    style_prefix "choice"    
    $ story_list = ["slave_story1",  "slave_story2", "slave_story3", "slave_story4", "slave_story5",  "slave_story6", "slave_story7", "slave_story8"]
       
    for index, name in enumerate(story_list):    
        hbox xpos 0 ypos 50+index*35:
            textbutton name action ToggleSetMembership(values, name) 
    vbox xpos 0 yalign 0.9:
        textbutton "完成" action Return(values)
    
# </neronero & RudolfU - BK.ini generator>