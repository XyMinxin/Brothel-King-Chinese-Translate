####            GIRL INTERACTIONS                ####
##              All the right moves...             ##
##                                                 ##
####                                             ####


################################
### SLAVE GIRLS INTERACTIONS ###
################################

## General labels ##

label slave_first_meet(girl):

    "You came to visit [girl.fullname] for the first time."

    call dialogue(girl, "slave first visit", nw=True) from _call_dialogue_104

    menu:

        # "What do you tell her?"

        "我会温柔地对待你的":
            $ renpy.block_rollback()

            you "You have nothing to fear from me. I promise you will be treated kindly."

            call dialogue(girl, "MC kind promise") from _call_dialogue_105

            $ MC.good += 1
            $ girl.promised = True

        "我会公正地对待你的":

            $ renpy.block_rollback()

            you "I am your new owner. I expect you to do my bidding, but I will treat you fairly."

            call dialogue(girl, "MC fair promise") from _call_dialogue_106

            $ MC.neutral += 1

        "我怎么对你看我心情":

            $ renpy.block_rollback()

            you "I'm your owner, don't you forget that. I can do anything I want with you."

            call dialogue(girl, "MC no promise") from _call_dialogue_107

            $ MC.neutral += 1


        "你吃了熊心豹子胆？":

            $ renpy.block_rollback()

            "You slap her across the face. She looks at you in shock."

            you "You do not address your betters without being spoken to, and you will refer to me as 'Master', or I will have your tongue!"

            you "Learn your place, or I will discipline you personally."

            call dialogue(girl, "MC harsh promise") from _call_dialogue_108

            $ MC.evil += 1

    $ girl.MC_interact = True

    return

label fight_attempt(girl, act=None, intensity=1, outside=False): # Returns True or False, which is set in the '_return' variable

    # Intensity measures how major the perceived affront is, from 1 (unpleasant/shameful act) to 4 (extreme act)

    if act:
        if act in girl.pos_acts:
            $ intensity -= 1
        elif act in girl.neg_acts:
            $ intensity += 1

    $ fight_happens = False
    if intensity > 0:
        # Very dom girls will always resist. Dom and Sub girls will resist wrongful acts. Very sub girls never fight
        if girl.is_("very dom") or (intensity >= 2 and girl.is_("dom")) or (intensity >= 3 and not girl.is_("very sub")):
            $ fight_happens = True

        call dialogue(girl, "MC fight intro") from _call_dialogue_109

    if fight_happens:

        if girl.get_effect("special", "bound"):
            with flash

            play sound s_thunder

            if outside:
                $ text1 = "ground"
            else:
                $ text1 = "floor"

            "[girl.name] throws herself at you, but the magical bind holding her is just too strong. She is jolted by a surge of magical energy, and crumbles to the [text1], winded."

            return False

        elif fight(girl, MC):
            with vpunch

            play sound s_punch

            you "Ouch!"

            if outside:
                $ text1 = "running"
            else:
                $ text1 = "through the door"

            "She struggles and pushes you away. You try to force her but she kicks you in the groin and escapes [text1]."

            call run_away(girl) from _call_run_away_1

            $ girl.change_love(-(2+intensity))

            return True

        else:
            with vpunch

            play sound s_surprise

            you "How dare you resist me!"

            if act and not outside:
                "She is no match for you. Restraining her, you shove her on the bed then slam the door shut."
            else:
                "She is no match for you. Restraining her, you force her into submission."

            $ girl.change_fear(2+intensity)

    return False


label break_promise(girl):

    call dialogue(girl, "MC break promise") from _call_dialogue_110

    $ girl.promised = False

    $ MC.good -= 1

    return



label slave_fear_test(girl):

    $ inter.response = None

    if dice(100) <= girl.fear:

        call dialogue(girl, "slave fear intro", narrator_mode=True) from _call_dialogue_111

        $ inter.response = "afraid"

        menu:
            "安慰她":

                $ inter.MC_reaction = "encourage"

                "You tell her it's all right, nothing bad will happen to her, and you repeat your question slowly."

                if dice(100) <= girl.fear:
                    call dialogue(girl, "slave fear reassure failure", narrator_mode=True) from _call_dialogue_112
                else:
                    call dialogue(girl, "slave fear reassure success", narrator_mode=True) from _call_dialogue_113
                    $ inter.response = None

            "惩罚她":
                you "I see it's useless trying to talk to you. So, here's a language you will understand!"

                call dialogue(girl, "slave fear discipline", narrator_mode=True) from _call_dialogue_114
                $ inter.MC_reaction = "discipline"

            "让她静静":
                pass

    return

label slave_naked_menu(girl):

    $ naked_score = girl.get_stat("libido") - reluctance

    if naked_score >= 25 and not girl.naked:

        you "Mmh, maybe we should take this further..."

        menu:
            "让她今后一直保持裸体" if naked_score >= 150:

                you "This is better, it's your natural state. From now on, you will remain naked at all times."

                girl.char "At... At all times? Even when going out?"

                you "Yes, of course. Let the whole world see who you really are."

                call dialogue(girl, "slave naked request permanent") from _call_dialogue_115

                "[girl.name] will remain naked until you tell her otherwise."

                $ girl.naked = True
                $ girl.acquire_perk(naked_perk, forced=True)
                $ girl.refresh_pictures()
                $ test_achievement("naked")

            "让她今天保持裸体":

                you "You seem to be just fine showing me your body... So why don't we make it interesting: you will spend the rest of the day naked!"

                play sound s_surprise

                girl.char "W-What??? But, but, I have to serve customers tonight!"

                $ MC.rand_say(("gd: 我知道，这样做会让你更舒服地在陌生人面前裸露身体。这是你需要学习的事情。", "ne: 恰恰相反。你将裸体为他们服务，并让他们稍微触摸你。这对生意有好处。", "ev: 哦，是的，确保给他们一个眼神....你是一个性奴隶，不要忘记这一点，不久之后他们将会在你身上插入每个洞。"))

                if naked_score >= 100:
                    call dialogue(girl, "slave naked request accept") from _call_dialogue_116

                    you "Good."

                else:
                    call dialogue(girl, "slave naked request accept") from _call_dialogue_117

                    $ MC.rand_say(("做吧。", "ev: 做吧。否则...."))

                    girl.char "Aw..."

                "[girl.name] will remain naked for the rest of the day."

                $ girl.naked = True
                $ girl.refresh_pictures()
                $ test_achievement("naked")

            "算了":
                pass
    return

label slave_justify(girl, context):

    if context == "reward":
        call dialogue(girl, "slave positive reaction") from _call_dialogue_118
    elif context == "punish":
        call dialogue(girl, "slave negative reaction") from _call_dialogue_119


    python:

        ev_list = girl.get_recent_events(day_number = 7)

        menu_list = [("What do you want to %s her for?" % context, None)]


        if ev_list:
            menu_list += [(ev.action, ev.type) for ev in ev_list if (ev.encourage and context == "reward") or (ev.discipline and context == "punish")]

        menu_list.append(("没有特别的原因", ""))
        menu_list.append(("返回", "back"))

    $ inter.reason = menu(menu_list)

    return

label slave_beg(girl, context): # Only sub girls will beg

    $ inter.response = "begged"

    call dialogue(girl, "slave " + context + " beg") from _call_dialogue_120

    menu:
        "She's crying uncontrollably, she seems very upset. What do you do?"

        "不理会她，继续":
            "You scoff."

            you "Giving me orders, are you? I don't think you understand your situation, slave. Now, get ready."

            call dialogue(girl, "slave beg proceed") from _call_dialogue_121

            $ inter.MC_reaction = "proceed"

        "这次先放她一马":
            "You pause for a second."

            you "Hmm, maybe this can be your lesson for today... But don't test my patience, or I {i}will{/i} go back to you."

            call dialogue(girl, "slave beg warning") from _call_dialogue_122

            $ inter.MC_reaction = "warning"

        "可怜她，放弃":
            "You take a good look at her, she's a mess. You decide to give her a break."

            you "Come on, don't be scared. I'm not going to make you do something against your will."

            call dialogue(girl, "slave beg give up") from _call_dialogue_123

            $ inter.MC_reaction = "give up"

    return



## 0. ROOT INTERACT MENU ##

## Note: All interaction results are handled by the GirlInteraction class resolve() function, except personal topics, acts and fixactions unlocks

label slave_interact(girl, free=False):

    if MC.get_effect("special", "notebook"):
        $ choice_menu_girl_interact = True

    if girl.personality_unlock["story"] > girl.flags["story"]:
        if renpy.has_label(girl.story): # Problem: Game will still crash if the label doesn't allow for the girl argument
            show screen dark_filter
            call expression girl.story pass (girl=girl) from _call_expression_1
            hide screen dark_filter
        else:
            "System" "Label: {color=[c_red]}[girl.story]{/color} doesn't exist (Custom girl: {color=[c_red]}[girl.path]{/color})."

label slave_interact_menu():

    if girl.away:
        "[girl.fullname] is away. You can't interact with her."

    elif not girl.MC_interact:
        show screen dark_filter
        call slave_first_meet(girl) from _call_slave_first_meet
        hide screen dark_filter

    hide screen girls
    show screen girl_interact(girl, free)
    $ tt = show_tt("top_right")
    with Dissolve(0.1)

    $ topic = None
    $ topic = ui.interact()
    $ renpy.block_rollback()

    if not topic:
        jump slave_interact_menu

    elif topic == "back":
        if not free or renpy.call_screen("yes_no", "Do you really want to leave without training [girl.fullname]?"):
            pass
        else:
            jump slave_interact_menu
    elif topic == "previous":
        $ girl = selected_girl = get_previous(MC.girls, girl, False)
        show screen girl_interact(girl, free)
        jump slave_interact_menu
    elif topic == "next":
        $ girl = selected_girl = get_next(MC.girls, girl, False)
        show screen girl_interact(girl, free)
        jump slave_interact_menu
    else:
        if not isinstance(topic, GirlInteractionTopic):
            python:
                try:
                    if isinstance(topic[0], GirlInteractionTopic):
                        topic, adv_mode = topic
                    else:
                        renpy.jump("slave_interact_menu")
                except:
                    renpy.jump("slave_interact_menu")

        $ last_interact_menu = topic.type
        $ girl.talked_to_date = calendar.time

        if free:
            $ free_training = True
        else:
            $ free_training = False # free_training is False for normal interactions but is set to True when auto-training

        show screen dark_filter

        if topic.gold_cost:
            play sound s_gold
            $ MC.gold -= topic.get_gold_cost()

        if topic.advanced:
            $ inter = GirlInteraction(girl, topic, mode=adv_mode, free=free)
            $ renpy.call(topic.label, girl, adv_mode)
        else:
            $ inter = GirlInteraction(girl, topic, free=free)
            $ renpy.call(topic.label, girl)

        $ inter.resolve()
        $ test_achievements(["masochist",])

        hide screen dark_filter
        hide screen show_event

        $ renpy.block_rollback()

        if (free and not inter.canceled) or girl not in MC.girls:
            pass
        elif MC.interactions >= 1 or (free and inter.canceled):
            jump slave_interact_menu

    hide screen girl_interact
    if not free:
        show screen girls(MC.girls, "girls")
    with Dissolve(0.1)

    return



## 1. CHATTING

label slave_chat_init(girl, _type):

    $ inter.type = _type

    if girl.fear >= girl.love + 10:

        "She looks frightened."

#         $ text1 = "..."

#     elif girl.love >= girl.fear + 10:

#         $ text1 = rand_choice(("Oh, hi, Master " + MC.name + ". What can I do for you?", "Hi, Master! *smile*", "Welcome, Master " + MC.name + ". *smile*", "Good to see you, Master."))

#     else:
#         $ text1 = rand_choice(("Hi, Master.", "Yes, Master?", "What is it, Master?", "You wanted to see me?"))

    call slave_fear_test(girl) from _call_slave_fear_test # Checks if the girl is too 'afraid' or not to chat

    return

label slave_chat_score_to_result():

    if inter.score < -25:
        $ inter.result = -2
    elif inter.score < 0:
        $ inter.result = -1
    elif inter.score < 25:
        $ inter.result = 0
    elif inter.score < 50:
        $ inter.result = 0.5
    elif inter.score < 75:
        $ inter.result = 1
    else:
        $ inter.result = 2

    return

label slave_chat_slave_life(girl): # D/S

    call slave_chat_init(girl, "slave_life") from _call_slave_chat_init

    if inter.response == "afraid":
        return

    $ you(rand_choice(("Tell me, how do you like your life as a slave?",
                       "Are you happy about being a slave?",
                       "How do you feel about being a slave?")))

    $ inter.score = girl.mood + girl.get_stat("obedience") / 5

    if girl.is_("very sub"):
        $ inter.score += 15
    elif girl.is_("sub"):
        $ inter.score += 5
    elif girl.is_("very dom"):
        $ inter.score -= 15
    elif girl.is_("dom"):
        $ inter.score -= 5

    call slave_chat_score_to_result() from _call_slave_chat_score_to_result

    call dialogue(girl, "slave chat slave_life " + str(inter.result)) from _call_dialogue_124

    # MC reaction

    menu:
        "我知道了":
            you "I see."

        "干得漂亮" if inter.result > -1:
            you "Keep your spirits up. Life as a slave isn't as bad as people think."
            $ inter.MC_reaction = "encourage"

        "别抱怨了" if inter.result < 1:
            you "I'm sick of your complaining. You're just a slave! Deal with it."
            $ inter.MC_reaction = "discipline"

    return


label slave_chat_brothel(girl):

    call slave_chat_init(girl, "brothel") from _call_slave_chat_init_1

    if inter.response == "afraid":
        return

    $ you(rand_choice(("How do you like life in the brothel?",
                       "Is life in the brothel ok for you?",
                       "Are you happy working here?")))

    $ inter.score = girl.mood + girl.get_stat("libido") / 5

    if girl.is_("very lewd"):
        $ inter.score += 15
    elif girl.is_("lewd"):
        $ inter.score += 5
    elif girl.is_("very modest"):
        $ inter.score -= 15
    elif girl.is_("modest"):
        $ inter.score -= 5

    call slave_chat_score_to_result() from _call_slave_chat_score_to_result_1

    $ r = inter.result

    if inter.result >= 1 and girl.has_trait("Virgin"):
        $ inter.result = "virgin"

    call dialogue(girl, "slave chat brothel " + str(inter.result)) from _call_dialogue_125

    # MC reaction

    menu:

        "我知道了":
            you "I see."

        "我很欣赏你的努力" if r >= 0:
            you "Look, I want you to know your efforts here are appreciated."
            call dialogue(girl, "slave thanks") from _call_dialogue_126
            $ inter.MC_reaction = "encourage"

        "摆正你的位置!" if r <= 0:
            you "You're a whore, this is a whorehouse. It's your home, now. You better love it, because you're not leaving!"
            call dialogue(girl, "slave whining") from _call_dialogue_127
            $ inter.MC_reaction = "discipline"

    return


label slave_chat_customers(girl):

    call slave_chat_init(girl, "customers") from _call_slave_chat_init_2

    if inter.response == "afraid":
        return

    $ you(rand_choice(("Are you getting along with the customers?",
                       "How are the customers treating you?",
                       "Are you happy working with the customers?")))

    $ inter.score = girl.mood + girl.get_stat("sensitivity") / 5

    if girl.is_("very idealist"):
        $ inter.score += 15
    elif girl.is_("idealist"):
        $ inter.score += 5
    elif girl.is_("very materialist"):
        $ inter.score -= 15
    elif girl.is_("materialist"):
        $ inter.score -= 5

    call slave_chat_score_to_result() from _call_slave_chat_score_to_result_2

    call dialogue(girl, "slave chat customers " + str(inter.result)) from _call_dialogue_128

    # MC reaction

    menu:

        "我知道了":
            you "I see."

        "你的表现很不错" if inter.result >= 0:
            you "I'm glad you're getting along with the customers. I'm sure they value your presence."
            $ inter.MC_reaction = "encourage"

        "给我把嘴闭上" if inter.result <= 0:
            you "The customers are always right, you moron! Keep your stupid comments to yourself!"
            $ inter.MC_reaction = "discipline"

    return


label slave_chat_other_girls(girl):

    call slave_chat_init(girl, "other_girls") from _call_slave_chat_init_3

    if inter.response == "afraid":
        return

    $ you(rand_choice(("Are you getting along with the other girls?",
                       "Do you like the other girls in the brothel?",
                       "Do you have any friends here?")))

    $ inter.score = girl.mood + girl.get_stat("charm")/5 + len(girl.friends)*10 - len(girl.rivals)*10

    if girl.is_("very extravert"):
        $ inter.score += 15
    elif girl.is_("extravert"):
        $ inter.score += 5
    elif girl.is_("very introvert"):
        $ inter.score -= 15
    elif girl.is_("introvert"):
        $ inter.score -= 5

    call slave_chat_score_to_result() from _call_slave_chat_score_to_result_3

    call dialogue(girl, "slave chat other_girls " + str(inter.result)) from _call_dialogue_129

    # Describe friends and rivals (not part of the dialogue system for now)

    $ d = dice(6)

    $ mentioned = None

    if d >= 4: # Describes a friend on 4+
        if girl.friends:
            $ mentioned = "friend"
            $ inter.other_girl = rand_choice(girl.friends)

            if inter.result < 0:
                $ text1 = ", however"
            else:
                $ text1 = ""

            $ comment = rand_choice(gpersonalities_comment[rand_choice(inter.other_girl.personality.attributes) + " pos"])
            girl.char "I really like [inter.other_girl.fullname][text1]. [comment] She's like a sister to me."

        else:
            girl.char "I don't have anyone I would call a close friend."

    else: # Else describes a rival
        if girl.rivals:
            $ mentioned = "rival"
            $ inter.other_girl = rand_choice(girl.rivals)

            if inter.result > 0:
                $ text1 = "Although "
            else:
                $ text1 = ""

            $ comment = rand_choice(gpersonalities_comment[rand_choice(inter.other_girl.personality.attributes) + " neg"])
            girl.char "[text1]I really don't like [inter.other_girl.fullname]. [comment] I can't stand her."

        else:
            girl.char "I get annoyed at the others sometimes, but there's no one I really don't get along with."

    # MC reaction

    menu:

        "我知道了":
            you "I see."

        "多交些朋友" if inter.result >= 0:
            you "Keep being nice to the other girls, and you will make more friends in no time."
            $ inter.MC_reaction = "encourage"

        "别再抱怨了" if inter.result <= 0:
            you "Stop complaining already! Get along with the other girls, or I'll make you!"
            $ inter.MC_reaction = "discipline"

        "[inter.other_girl.name] is great" if mentioned == "friend":
            you "I think [inter.other_girl.name] is a great girl. I'm happy you two are getting along."
            call dialogue(girl, "MC praise friend") from _call_dialogue_130
            $ inter.MC_reaction = "praise friend"

        "[inter.other_girl.name] is stupid" if mentioned == "rival":
            you "[inter.other_girl.name] is a stupid bitch, I'll give you that."
            call dialogue(girl, "MC demean rival") from _call_dialogue_131
            $ inter.MC_reaction = "demean rival"

        "别整天和[inter.other_girl.name]鬼混在一起" if mentioned == "friend":
            you "I don't like you wasting time fooling around with [inter.other_girl.name]. Stop seeing her."
            call dialogue(girl, "slave whining") from _call_dialogue_132
            you "End of discussion. Now go back to work."
            $ inter.MC_reaction = "break friendship"

        "放下你和[inter.other_girl.name]的私人恩怨" if mentioned == "rival":
            you "Stop your bickering with [inter.other_girl.name]. I want you to be friends."
            call dialogue(girl, "slave whining") from _call_dialogue_133
            $ inter.MC_reaction = "make peace"

    return


# Personal topics

label slave_chat_well_being(girl):

    call slave_chat_init(girl, "well_being") from _call_slave_chat_init_4

    if inter.response == "afraid":
        return

    $ you(rand_choice(("Is everything all right?", "How are you feeling?", "Is there anything wrong?")))

    if girl.mood > -75:
        if girl.mood > 75:
            $ inter.result = 3
        elif girl.mood > 50:
            $ inter.result = 2
        elif girl.mood > 25:
            $ inter.result = 1
        elif girl.mood > 0:
            $ inter.result = 0
        elif girl.mood > -25:
            $ inter.result = -1
        elif girl.mood > -50:
            $ inter.result = -2
        else:
            $ inter.result = -3

        call dialogue(girl, "slave chat well_being %s" % inter.result) from _call_dialogue_134

    else:
        "She doesn't answer, but her eyes are red from crying her heart out for many a sleepless night.
         She clearly feels horrible here."
        $ inter.result = -4

    if girl.get_recent_events(28, filter="hurt"):
        $ nb = len(girl.get_recent_events(28, filter="hurt"))

        if nb == 1:
            $ nb_times = "1次"
        else:
            $ nb_times = str(nb) + "次"

        call dialogue(girl, "slave chat well_being attacked") from _call_dialogue_135

        $ inter.result += -1 * nb

    if girl.get_recent_events(28, filter="sick"):

        $ nb = len(girl.get_recent_events(28, filter="sick"))

        if nb == 1:
            $ nb_times = "1次"
        else:
            $ nb_times = str(nb) + "次"

        call dialogue(girl, "slave chat well_being sick") from _call_dialogue_136

        $ inter.result += -1 * nb

    if girl.get_recent_events(28, filter="exhausted"):

        $ nb = len(girl.get_recent_events(28, filter="exhausted"))

        if nb == 1:
            $ nb_times = "1次"
        else:
            $ nb_times = str(nb) + "次"

        call dialogue(girl, "slave chat well_being exhausted") from _call_dialogue_137

        $ inter.result += -1 * nb

    # MC reaction

    menu:
        "我知道了":
            you "I see."

        "很高兴看到你对这里满意" if inter.result >= 0:
            you "I'm happy that things are to your liking here. Keep up the good work."
            call dialogue(girl, "slave thanks") from _call_dialogue_138

            $ inter.MC_reaction = "encourage"

        "我很抱歉这里的环境..." if inter.result < 0:
            you "I'm sorry the conditions here have been less than ideal. Please hang in there."
            call dialogue(girl, "slave chat well_being MC apology") from _call_dialogue_139

            $ inter.MC_reaction = "encourage"


        "给我好好工作，否则..." if inter.result >= 0:
            you "Don't get too comfortable. Remember, what your master gives, he can take away."
            call dialogue(girl, "slave bullied") from _call_dialogue_140

            $ inter.MC_reaction = "discipline"


        "你最好早点习惯这里..." if inter.result < 0:
            you "Do you think you can tell me what I should or shouldn't do? Do You?"
            call dialogue(girl, "slave apology") from _call_dialogue_141
            you "Shut up, and get ready to work."

            $ inter.MC_reaction = "discipline"

    return


label slave_chat_feelings(girl):

    call slave_chat_init(girl, "feelings") from _call_slave_chat_init_5

    if inter.response == "afraid":
        return

    $ MC.rand_say(("放松, 大胆的说. 你感觉我怎么样?", "你对我印象如何?", "对你来说我是个好主人吗?",
                   "ev: 你是怎么看待你的主人的? 回答我!", "ne: 这儿没有别人. 我做的怎么样?", "gd: 我做得对吗? 现在就告诉我你的感受."))

    girl.char "Well..."

    $ inter.result = 0

    if girl.get_love() > girl.get_fear():
        if girl.get_love() < 25:
            $ inter.result -= 1
        elif girl.get_love() < 50:
            pass
        elif girl.get_love() < 75:
            $ inter.result += 1
        else:
            $ inter.result += 2

        call dialogue(girl, "slave chat feelings love %s" % inter.result) from _call_dialogue_142

    else:
        if girl.get_fear() < 25:
            $ inter.result -= 1
        elif girl.get_fear() < 50:
            pass
        elif girl.get_fear() < 75:
            $ inter.result += 1
        else:
            $ inter.result += 2

        call dialogue(girl, "slave chat feelings fear %s" % inter.result) from _call_dialogue_143

    if girl.get_stat("obedience") < 25:
        $ inter.result -= 2
        call dialogue(girl, "slave chat feelings very disobedient") from _call_dialogue_144


    elif girl.get_stat("obedience") < 50:
        $ inter.result -= 1
        call dialogue(girl, "slave chat feelings disobedient") from _call_dialogue_145

    elif girl.get_stat("obedience") < 100:
        call dialogue(girl, "slave chat feelings a little obedient") from _call_dialogue_146

    elif girl.get_stat("obedience") < 150:
        $ inter.result += 1
        call dialogue(girl, "slave chat feelings obedient") from _call_dialogue_147

    else:
        $ inter.result += 2
        call dialogue(girl, "slave chat feelings very obedient") from _call_dialogue_148

    # MC reaction

    menu:
        "我知道了":
            you "I see."

        "感谢你的坦诚相告" if inter.result >= 0:
            you "Thank you, I appreciate your honesty."
            $ inter.MC_reaction = "encourage"

        "你吃了熊心豹子胆？" if inter.result <= 0:
            you "What the... Who asked for your opinion, you stupid bitch?"
            call dialogue(girl, "slave whining") from _call_dialogue_149
            you "Shut the fuck up!"
            $ inter.MC_reaction = "discipline"

    return


label slave_chat_tastes(girl):

    call slave_chat_init(girl, "tastes") from _call_slave_chat_init_6

    if inter.response == "afraid":
        return

    $ inter.score = girl.get_love() + girl.get_stat("obedience")
    $ inter.response = "accepted"

    if inter.score <= 15:
        if girl.is_(("extravert", "dom")):
#             "She looks annoyed and sneers."
            girl.char "我?我的想法并不重要。我只是个奴隶，不是吗? *冷笑*"
        elif girl.is_(("introvert", "dom")):
#             "She looks bothered and sighs heavily."
            girl.char "我喜欢一个人待着。*叹气*"
        elif girl.is_(("introvert", "sub")):
            "她咕哝着什么，但你听不见。在你的坚持下，她几乎哭了出来。她的意见并不重要。"
        elif girl.is_(("extravert", "sub")):
#             "She blushes and look away."
            girl.char "我的想法不重要，[MC.name]主人。 我只是你的一个奴隶。 *脸红*"

        $ inter.response = "refused"

    elif inter.score <= 30:
        "她现在和你在一起感到更加自然放松了。她向你透露了一些她的喜好。"
        $ result = rand_choice(("likes", "dislikes"))
        $ girl.change_love(1)
        $ girl.change_fear(-1)

    elif inter.score <= 60:
        "她和你在一起感觉很舒服。当你们一起喝下午茶时，她告诉了你她喜欢什么讨厌什么。"
        $ result = weighted_choice([("likes", 1), ("dislikes", 1), ("loves", 2), ("hates", 2)])
        $ girl.change_love(2)
        $ girl.change_fear(-1)

    elif inter.score <= 120:
        "当你坐在她身边，提及她喜欢什么时，她的脸红的像个苹果一样。"
        $ result = weighted_choice([("likes", 1), ("dislikes", 1), ("loves", 2), ("hates", 2), ("pos_act", 2), ("neg_act", 2)])
        $ girl.change_love(3)
        $ girl.change_fear(-2)

    else:
        "她坐在你的腿上，双臂环抱着你，柔情似水地告诉你她喜欢什么。"
        $ result = weighted_choice([("likes", 1), ("dislikes", 1), ("loves", 1), ("hates", 1), ("pos_fix", 2), ("neg_fix", 2)])
        $ girl.change_love(3)
        $ girl.change_fear(-3)


    # Girl explanation

    if inter.response == "accepted":

        $ renpy.block_rollback()

        if result == "likes":

            $ thing, best = girl.talk_tastes("likes")

            $ thing_cn = translate_cn(thing, girl_related_dict)

            call dialogue(girl, "slave chat tastes likes") from _call_dialogue_150

            $ girl.personality_unlock["fav_" + thing] = True

        elif result == "dislikes":

            $ thing, worst = girl.talk_tastes("dislikes")

            $ thing_cn = translate_cn(thing, girl_related_dict)

            call dialogue(girl, "slave chat tastes dislikes") from _call_dialogue_151

            $ girl.personality_unlock["dis_" + thing] = True

        elif result == "loves":

            $ verb, item_type = girl.talk_tastes("loves")

            if verb == "loves":
                if item_type not in girl.personality_unlock["loves"]:
                    $ girl.personality_unlock["loves"].append(item_type)
                $ thing = gift_description[item_type]
                $ thing_cn = thing
                call dialogue(girl, "slave chat tastes loves +") from _call_dialogue_152

            elif verb == "likes":
                if item_type not in girl.personality_unlock["likes"]:
                    $ girl.personality_unlock["likes"].append(item_type)
                $ thing = gift_description[item_type]
                $ thing_cn = thing
                call dialogue(girl, "slave chat tastes loves -") from _call_dialogue_153

            elif verb == "indifferent":
                call dialogue(girl, "slave chat tastes no loves") from _call_dialogue_154


        elif result == "hates":
            $ verb, item_type = girl.talk_tastes("hates")

            if verb == "hates":
                if item_type not in girl.personality_unlock["hates"]:
                    $ girl.personality_unlock["hates"].append(item_type)
                $ thing = gift_description[item_type]
                $ thing_cn = thing
                call dialogue(girl, "slave chat tastes hates") from _call_dialogue_155

            elif verb == "indifferent":
                call dialogue(girl, "slave chat tastes no hates") from _call_dialogue_156

        elif result == "pos_act":

            $ act = rand_choice(girl.pos_acts)
            $ act_desc = long_act_description[act]

            "她贴着你的耳朵轻声细语，脸红的发烫。"

            $ girl.personality_unlock[act] = True
            # $ girl.personality_unlock["LM"] += MC.get_charisma() + 15 + dice(10)
            $ girl.raise_preference(act, "love", 2)

            call dialogue(girl, "slave chat tastes positive act") from _call_dialogue_157

        elif result == "neg_act":

            $ act = rand_choice(girl.neg_acts)

            if act:
                "她贴着你的耳朵轻声细语，脸红的发烫。"

                $ act_desc = long_act_description[act]
                $ girl.personality_unlock[act] = True
                # $ girl.personality_unlock["LM"] += MC.get_charisma() + 15 + dice(10)

                call dialogue(girl, "slave chat tastes negative act") from _call_dialogue_158

            else:
                call dialogue(girl, "slave chat tastes no negative act") from _call_dialogue_159

        elif result == "pos_fix":

            $ fix = rand_choice(girl.pos_fixations)
            $ fix_desc = fix_description[fix.name + " description"].lower()

            play sound s_mmmh
            "她告诉你她喜欢[fix_desc]"

            if not girl.personality_unlock[fix.name]:
                $ cntext = girl_related_dict[fix.name]
                "You have discovered [girl.name]'s fixation with [fix.name]."

                $ girl.personality_unlock[fix.name] = True
                $ test_achievement("pos fixations")

        elif result == "neg_fix":

            $ fix = rand_choice(girl.neg_fixations)

            if fix:
                play sound s_sigh
                $ fix_desc = fix_description[fix.name + " description"].lower()
                "她告诉你她真的很讨厌[fix_desc]。她很害怕。"

                if not girl.personality_unlock[fix.name]:
                    $ cntext = girl_related_dict[fix.name]
                    "You have discovered [girl.name]'s disgust for [fix.name]."

                    $ girl.personality_unlock[fix.name] = True
                    $ test_achievement("neg fixations")

    elif inter.response == "refused":

        menu:
            "我知道了":
                you "好的，我们稍后再讨论。"
                $ inter.MC_reaction = "give up"

            "谁给你的胆子？":
                $ inter.MC_reaction = "discipline"

                play sound s_punch
                "You slap her across the face." with vpunch

                you "I've asked you a fucking question! Don't you dare ignore me, slave!"

                call dialogue(girl, "slave hit") from _call_dialogue_160

                $ MC.rand_say(("如果你再顶嘴，会更疼的。记住这一点。", "记住这一点，下次做得更好。"))

    return


label slave_chat_origins(girl):

    call slave_chat_init(girl, "origins") from _call_slave_chat_init_7

    if inter.response == "afraid":
        return

    $ inter.score = girl.get_love() + girl.get_stat("obedience")
    $ inter.response = "accepted"

    if inter.score <= 20:
        if girl.is_(("extravert", "dom")):
            "She rolls her eyes."
            girl.char "What kind of question is that... Why do you care where I come from!"

        elif girl.is_(("extravert", "sub")):
            "She sighs."
            girl.char "I'm sorry, Master, but where I come from isn't important. I'm here, now..."

        elif girl.is_(("introvert", "dom")):
            "Her mood darkens."
            girl.char "I'd rather not talk about it."

        elif girl.is_(("introvert", "sub")):
            "She gets tearful, and she looks down."
            girl.char "Home... Oh..."

        $ inter.response = "refused"

    elif inter.score <= 40:

        call dialogue(girl, "slave chat origins 1") from _call_dialogue_161

    elif inter.score <= 60:

        $ home = girl.story_home
        $ a_home = article(home)

        call dialogue(girl, "slave chat origins 2") from _call_dialogue_162

    else:

        call dialogue(girl, "slave chat origins 3") from _call_dialogue_163

        if girl.origin in origins:
            call dialogue(girl, "origin " + girl.origin) from _call_dialogue_164
        elif girl.init_dict["background story/origin_description"]:
            $ girl.char(girl.init_dict["background story/origin_description"])


    if inter.response == "refused":

        menu:
            "我知道了":
                you "Fine, we'll discuss this later."
                $ inter.MC_reaction = "give up"

            "你吃了熊心豹子胆？":
                $ inter.MC_reaction = "discipline"

                play sound s_punch
                "You slap her across the face." with vpunch

                you "I've asked you a fucking question! Don't you dare ignore me, slave!"

                call dialogue(girl, "slave hit") from _call_dialogue_165

                $ MC.rand_say(("如果你再顶嘴，会更疼的。记住这一点。", "记住这一点，下次做得更好。"))

    else:
        $ girl.personality_unlock["origin"] = True

    return

label slave_chat_story(girl):
    $ renpy.call(girl.story, girl)
    return


## 2. TRAINING ##

label slave_train_free_form(girl): #!
    # In free-form mode, you will only be able to choose from the range of sex acts she is comfortable with

    call hide_everything() from _call_hide_everything_41
    scene black with fade

    python:
        available_acts = girl.get_trainable_sex_acts()

        act_response = {}
        for a in available_acts:
            act_response[a] = girl.training_check(a) # Returns: "accepted", "resisted" or "refused"

        act = "naked"

        finish = False

    $ pic = girl.get_pic("naked", "rest", "profile", hide_farm=True, soft=True)

    show screen show_event(pic)
    with dissolve

    while not finish:
        $ and_tags = []
        $ not_tags = prepare_not_tags(girl, act)
        if act in ("sex", "group") and girl.has_trait("Virgin"):
            $ and_tags.append("virgin")

        python:
            _menu_items = [(a.capitalize() + get_act_weakness_symbol(girl, a), a) for a in available_acts if a != act]
            if act != "naked":
                _menu_items += [("Cum inside", "inside"), ("Cum outside", "outside")]
            _menu_items.append(("Quit", "quit"))

        $ girl.char("What should we do, Master?", interact=False)
        $ r = renpy.display_menu(_menu_items)

        if r == "quit":
            if renpy.call_screen("yes_no", __("Are you sure you want to quit free-form training? (She will receive training progress for %s acts)" % act)):
                $ inter.act = act
                $ finish = True
        elif r in ("inside", "outside"): #!
            if r == "outside":
                $ tags = {"service" : ("cih", "cof"), "sex" : ("cob"), "anal" : "cob", "fetish" : ("cof", "cih", "cob"), "bisexual" : ("cof", "cih", "cob"), "group" : ("buk", "cum shower")}[act]
            else:
                $ tags = {"service" : ("cim"), "sex" : ("cin", "creampie"), "anal" : ("cin", "creampie"), "fetish" : ("cim", "cin", "creampie"), "bisexual" : ("cim", "cin", "creampie"), "group" : ("cin", "creampie")}[act]

            $ pic = girl.get_pic(tags, act, and_tags = [act] + and_tags, not_tags = not_tags, hide_farm=True)
            $ inter.act = act
            $ inter.response = act_response[act]
            $ finish = True

            show screen show_event(pic)
            with dissolve

            ""
        else:
            $ act = r
            $ pic = girl.get_pic(act, "naked", "rest", "profile", and_tags = and_tags, not_tags = not_tags, hide_farm=True)

            show screen show_event(pic)
            with dissolve
            $ reluctance = preference_modifier[girl.get_preference(act)]
            call slave_do(girl, act, context="free-form") from _call_slave_do_1
            stop sound fadeout 3.0
            stop sound2 fadeout 3.0

    return

label slave_train_sex_acts(girl, mode):

    $ act = inter.act

    if mode == "lecture":
        call slave_train_lecture(girl, act) from _call_slave_train_lecture

    elif mode in ("train", "advanced"):
        if act == "naked":
            you "Remove your clothes. I want you to expose your body to me."
        elif act == "service":
            you "I want you to service me with your mouth and hands."
        elif act == "sex":
            you "Lay down. I am going to fuck you."
        elif act == "anal":
            you "Turn around and bend over. I am going to fuck your ass."
        elif act == "fetish":
            you "Today, I'll introduce you to some of my new toys..."
        elif act == "bisexual":
            "You call Sill over to [girl.name]'s room."
            sill happy "Yes, Master [MC.name]?"
            you "Get naked. You and [girl.name] will pleasure each other."
        elif act == "group":
            if brothel.security > 0:
                "You call Sill over, and ask her to fetch a security guard."
            else:
                "You call Sill over, and ask her to fetch a random vagrant off the street."
            sill happy "All right. What for, Master [MC.name]?"
            you "The lucky sod and I are going to fuck this girl silly. [girl.name], get yourself ready!"
        else:
            $ raise AssertionError("Error: No sex act recognized.")

        $ inter.response = girl.training_check(act) # Returns 'response' : "accepted", "resisted" or "refused"

        ## Chance of sub girls begging

        if girl.is_("sub") and girl.test_weakness(act)[1] and dice(6) >= 5:
            call slave_beg(girl, "train") from _call_slave_beg

        if inter.MC_reaction not in ("give up", "warning"):
            if inter.response == "accepted":
                "She accepts your orders."
                call dialogue(girl, "slave train accepted") from _call_dialogue_166

                "She moves to position herself where you want her."

                if act not in girl.has_trained:
                    $ girl.has_trained.append(act)
                    $ girl.track_event("new act", arg=act)

                call slave_train(girl, act, inter.response, mode) from _call_slave_train

            elif inter.response == "resisted":
                "She resists you."
                call dialogue(girl, "slave train resisted") from _call_dialogue_167

                menu:
                    "What do you do?"

                    "坚持训练":
                        $ inter.MC_reaction = "proceed"
                        $ MC.rand_say(("gd: 对不起，但这是你的训练的一部分。让我们继续吧.",
                                       "ne: 我不在乎你的意见，奴隶。无论你准备好与否，我们都要这样做.",
                                       "ev: 你以为你可以告诉我该做什么？真他妈的贱货！", "闭嘴，准备好了。我们要这样做."))

                        if girl.promised:
                            call break_promise(girl) from _call_break_promise

                        "You ignore her complaints and gesture for her to move to the bed."

                        call slave_train(girl, act, inter.response, mode) from _call_slave_train_1

                    "放弃训练":
                        $ inter.MC_reaction = "give up"
                        $ MC.rand_say((__("好吧....按你的方式来吧."), __("我不敢相信现在的奴隶....好吧!"), __("ne: 哼。这一次我会放过你的。你欠我一个人情."),
                                        __("gd: 好吧，我不会强迫你做你不喜欢的事情."), __("ev: 他妈的，这一次我会放过你....但不要考验我的耐心.")))


            else:
                "She refuses you."

                $ girl.track_event("refused", arg=girl_related_dict[act])

                call dialogue(girl, "slave train refused") from _call_dialogue_168

                menu:
                    "What do you do?"

                    "强迫训练":
                        $ inter.MC_reaction = "force"
                        $ impact = 2
                        $ MC.rand_say(("我是你的主人。你必须服从我。", "你必须按照我的话做！这是最后通牒！！！",
                            "ev: 闭嘴，贱货。我制定规则！", "gd: 我的耐心已经到达极限。这一次你逃不掉。"))

                        call slave_rape(girl, act) from _call_slave_rape

                    "放弃训练":
                        $ inter.MC_reaction = "give up"
                        $ MC.rand_say(("好吧....按你的方式来吧。", "我不敢相信现在的奴隶....好吧！", "ne: 哼。这一次我会放过你的。你欠我一个人情。",
                                        "gd: 好吧，好吧。我不会强迫你做你讨厌的事情。", "ev: 他妈的，这一次我会放过你....但不要考验我的耐心。"))

    return

label slave_remove_fixation(girl):

    python:

        neg_fix = [fix for fix in girl.neg_fixations if girl.personality_unlock[fix.name]]

        if len(neg_fix) == 1:
            fix = neg_fix[0]

            renpy.say(you, "今天，我希望你能克服对[fix.short_name]的厌恶")

        else:
            menu_list = [] #[("Choose a fixation to work on", None)]
            for fix in neg_fix:
                if fix.name in girl.locked_fix:
                    menu_list.append(("{color=[c_lightgrey]}" + __(fix.name.capitalize()) + " (locked){/color}", fix))
                else:
                    menu_list.append((__(fix.name.capitalize()), fix))

            menu_list.append(("返回", "back"))
            renpy.say(you, "Today, I want you to overcome your disgust for...", interact=False)
            fix = menu(menu_list) # renpy.display_menu(menu_list)

    if fix == "back":
        $ inter.canceled=True
        return

    elif fix.name in girl.locked_fix:
        $ cntext = girl_related_dict[fix.name]
        "[girl.name] was pushed too hard, she hates [fix.name] with all her heart now. You cannot do anything about it."
        $ inter.canceled=True
        return

    $ available_acts = []

    python:
        for act in fix.acts:
            if girl.will_do_sex_act(act):
                if not (girl.has_trait("Virgin") and act == "sex"):
                    available_acts.append(act)

    if not available_acts:
        "[girl.fullname] isn't comfortable enough with any of the required sex acts to try to remove this fixation."
        $ inter.canceled=True
        return
    else:
        $ inter.act = rand_choice(available_acts)

#     $ text1 = fix.short_name

    ## Checks if girl accepts training

    $ inter.response = girl.training_check(inter.act) # Returns 'response' : "accepted", "resisted" or "refused"

    if inter.response == "accepted":
        play sound s_sigh
        girl.char "Uh, [fix.short_name]? Well... Okay... {color=[c_green]}*accepted*{/color}"

    elif inter.response == "resisted":
        play sound s_surprise
        girl.char "Oh no, Master, not [fix.short_name]! Let's do something else... {color=[c_lightred]}*resisted*{/color}"

    elif inter.response == "refused":
        play sound s_scream
        girl.char "[fix.short_name]? No, no way!!! {color=[c_lightred]}*refused*{/color}"

    ## MC choice

    menu:
        extend ""

        "温和地训练她" if inter.response == "accepted":
            $ inter.MC_reaction = "love"
#             you "There's nothing to be afraid of... Let me show you."

        "正常地训练她" if inter.response == "accepted":
            $ inter.MC_reaction = "neutral"
#             you "Come here."

        "严苛地训练她"  if inter.response == "resisted":
            $ inter.MC_reaction = "neutral"
            you "You're going to do as you're told."

        "揍她一顿" if inter.response != "refused":
            $ inter.MC_reaction = "fear"
            you "I don't care if you like [fix.short_name] or not, slave. When you work for me, you have to do anything I tell you."

        "强迫训练" if inter.response == "refused":
            $ inter.MC_reaction = "fear"
#             "You raise your voice threateningly."
            you "This is not your call, slave! Get ready! *angry*"

            call slave_rape_test(girl, act=inter.act, intensity=3) from _call_slave_rape_test_2

            if not can_interact(girl):
                return

        "放弃训练" if inter.response != "accepted":
            $ inter.MC_reaction = "give up"
            $ MC.rand_say(("好吧....按你说的做。", "我简直不敢相信现在的奴隶....好吧！", "ne: 哼，这一次我放过你。你欠我一个人情。",
                           "gd: 好吧，我不会强迫你做你讨厌的事情。", "ev: 他妈的，这一次我放过你....但不要考验我的耐心。"))
            return


    ## Resolve

    $ not_tags = prepare_not_tags(girl, inter.act, [fix.name])
    $ pic = girl.get_fix_pic(inter.act, fix, not_tags=not_tags)

    if not pic:
        if fix.step == 1:
            $ pic = girl.profile

        elif fix.step == 2:
            $ pic = girl.get_pic(inter.act, "naked", "rest", "profile", not_tags=not_tags, hide_farm=True, pref_filter=True)

        elif fix.step == 3:
            $ pic = girl.get_pic("rest", "profile", and_tags = "naked", not_tags=not_tags, hide_farm=True, pref_filter=True)


#    scene black
    call hide_everything() from _call_hide_everything_6
    with fade

    $ renpy.say("", __(fix_description[fix.name + " intro"]) % girl.name)

    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
    with dissolve

    $ inter.result = girl.try_to_remove_fix(fix.name, inter.MC_reaction)
    $ renpy.block_rollback()

    if inter.result == "success":
        girl.char "Oh, Master..."
        play sound s_mmmh

        $ renpy.say("", __(fix_description[fix.name + " pos_reaction"]))

        $ renpy.say("", __("训练进行得非常顺利。 ") + event_color["special"] % (girl.fullname + __(" 不再对 ") + __(fix.name) + "感到厌恶。"))

        $ girl.add_log(__("neg fixation removed"))

    elif inter.result == "fail":
        play sound s_fizzle
#         girl.char "..."
        $ renpy.say("", fix_description[fix.name + " neg_reaction"])
        $ renpy.say("", event_color["a little bad"] % ("你的训练没有带来任何显著的改善。"))

    elif inter.result == "locked":
        play sound s_scream_loud
        girl.char "NO! Go away!!!"
        "[girl.name] pushes you back, curls up and starts sobbing uncontrollably. You cannot get anything more out of her."

        $ renpy.say("", "你的粗暴训练对她来说太过分了。 " + event_color["bad"] % ("她现在永远恨 " + fix.name + "."))

        $ unlock_achievement("neg fixation locked")

    else:
#         girl.char "Oh..."

        play sound s_spell

        if inter.result == 1:
            "[girl.name] is still very reluctant, but you could show her a thing or two."
            $ renpy.say("",  __("训练进行得很顺利。 ") + event_color["good"] % (girl.name + __(" 有了一些进步。")))
        elif inter.result == 2:
            $ text1 = fix_description[fix.name + " description"]

#             if not text1.startswith("to "):
#                 $ text1 = "to " + text1

            "[girl.name] is getting used to [text1] Her progress is encouraging."
            $ renpy.say("",  __("训练进行得很顺利。 ") + event_color["good"] % (girl.name + __(" 有了一些进步。")))
        elif inter.result == 3:
            $ text1 = __(fix.name).capitalize()
            "[girl.name] did very well today. [text1] is beginning to feel almost normal to her."
            $ renpy.say("",  __("训练进行得很顺利。 ") + event_color["good"] % (girl.name + __(" 有了一些进步。")))

    return

label slave_train_lecture(girl, act):
    $ act_desc = long_act_description[act]

    if girl.love > girl.fear + 10:
        call dialogue(girl, "slave lecture love") from _call_dialogue_169

    elif girl.fear > girl.love + 10:
        call dialogue(girl, "slave lecture fear") from _call_dialogue_170

    else:
        call dialogue(girl, "slave lecture neutral") from _call_dialogue_171

    you "Today, I wanna talk to you about [act_desc]."

    call dialogue(girl, "slave lecture " + girl.get_preference(act)) from _call_dialogue_172

    $ reluctance = preference_modifier[girl.get_preference(act)] #girl.get_preference(topic)

    $ d = dice(6, 2)
    $ diff = {"naked" : 10, "service" : 12, "sex" : 12, "anal" : 13, "fetish": 13, "bisexual" : 13, "group" : 14}

    if d > 9:
        "You feel inspired today, and give her one of the most impassioned lecture you are capable of."
    elif d <= 3:
        "You haven't really prepared anything for this lesson, and it shows."
    else:
        "You give her the usual speech about the merits of [act_desc]."

    $ mod = (girl.get_love() - girl.get_fear()) // 10

    if mod >= 1:
        "She listens intently, because she admires you."
    elif mod <= -1:
        "She listens carefully, because she fears you."

    $ inter.score = d + mod - diff[act]

    if inter.score > 0:
        "You have made good progress. She is now more knowledgeable and relaxed about [act_desc]."

    elif inter.score == 0:
        "You have made some progress. She is now a little more relaxed about [act_desc]."

    else:
        "She politely hears you out, but it doesn't seem to change her mind. She feels the same about [act_desc]."

    if act == "naked":
        call slave_naked_menu(girl) from _call_slave_naked_menu

    return

label slave_train_obedience(girl):

    hide screen girl_interact
    hide screen dark_filter
    with Dissolve(0.1)

    "You start with giving [girl.name] simple orders around the house."

    $ MC.rand_say(("打扫阁楼，好吗？", "帮希尔做家务。", "换所有床单。", "拿着扫帚清理" + rand_choice(brothel.rooms.keys()) + "。",
                  "去井里取些水。", "ar: 清理太阳神祭坛。", "确保墙上没有灰尘。", "为我们做点什么。", "ev: 把我的靴子擦得干干净净的。我不想看到一点灰尘，你听到了吗？",
                  "wr: 给我的武器上油。当然，我是指我的剑。", "tr: 喂德拉贡一只青蛙。别害羞，他很少咬人的手。", "wz: 擦一下我的法杖。我的魔法法杖。我是说....你知道的。"))

    $ pic = girl.get_pic("obedience", "maid", "waitress", "profile", naked_filter=True, soft=True)

    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
    with dissolve

    "You give her a few more menial chores. You observe her as she carries out her tasks."

    call dialogue(girl, "slave train obedience") from _call_dialogue_173
    if girl.is_("very dom"):
        $ diff = 7
    elif girl.is_("dom"):
        $ diff = 6
    elif girl.is_("very sub"):
        $ diff = 4
    elif girl.is_("sub"):
        $ diff = 5

    if dice(6) + MC.get_charisma() >= diff:

        "She follows your instructions carefully, doing her best to impress you."

        $ inter.result = "good"

    else:
        "She grumbles and drags her feet as she goes about her business. You inspect her work when she is finished. It's sloppy."

        $ inter.result = "bad"

        $ girl.track_event("bad result", (__("poor"), __("chores")))

    menu:

        "What do you do?"

        "赞美她" if inter.result == "good":
            $ inter.MC_reaction = "encourage"
            you "I'm happy that you are giving it your best."
            call dialogue(girl, "slave thanks") from _call_dialogue_174

        "告诫她" if inter.result == "bad":
            $ inter.MC_reaction = "discipline"
            you "You call that working? Do it all over again, and do it right this time!"
            call dialogue(girl, "slave bullied") from _call_dialogue_175

        "无视她":
            if inter.result == "good":
                "You nod and send her back to her room."
            elif inter.result == "bad":
                you "Mmmh. I'll give her a break this time."

    return


label slave_train_constitution(girl):

    hide screen girl_interact
    hide screen dark_filter
    with Dissolve(0.1)

    "You ask [girl.name] to do a few simple exercises."

    $ MC.rand_say((str(10 + dice(40)) + __(" 个俯卧撑。去！"), "上下楼梯跑步。数你的步数。", "把这桶水围绕院子四次。",
                   __("举起这根木头，大约 ") + str(5 + dice(15)) + __(" 次。"), "在附近跑半个小时。", "wr: 用练习剑练习一下",
                   "tr: 带德拉贡出去散步。试着跟上！", "wz: 去取我的魔法用品。那是一个大的金属箱子。"))

    $ pic = girl.get_pic("constitution", "dancer", "profile", naked_filter=True, soft=True)

    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
    with dissolve

    "You give her a few more physical feats to achieve. You follow her and advise her as she carries out her tasks."

    call dialogue(girl, "slave train constitution") from _call_dialogue_176

    if girl.is_("very introvert"):
        $ diff = 7
    elif girl.is_("introvert"):
        $ diff = 6
    elif girl.is_("very extravert"):
        $ diff = 4
    elif girl.is_("extravert"):
        $ diff = 5

    if dice(6) + MC.get_strength() >= diff:
        "She follows your training instructions carefully, progressing thanks to your advice."

        $ inter.result = "good"

    else:
        "She struggles with the task and is out of breath within a few minutes. She implores you to let her rest."

        $ inter.result = "bad"

        $ girl.track_event("bad result", (__("poor"), __("out")))

    menu:

        "What do you do?"

        "赞美她" if inter.result == "good":
            $ inter.MC_reaction = "encourage"
            you "I'm happy that you are giving it your best."
            call dialogue(girl, "slave thanks") from _call_dialogue_177

        "告诫她" if inter.result == "bad":
            $ inter.MC_reaction = "discipline"
            you "You're a maggot, you're puke, you're the last thing on earth!!! Do that again!"

            call dialogue(girl, "slave bullied") from _call_dialogue_178


        "无视她":
            if inter.result == "good":
                "You nod and send her back to her room."
            elif inter.result == "bad":
                you "Mmmh. I'll give her a break this time."

    return


label slave_train(girl, act, response, mode="train"): # Used if girl accepted of resisted

    $ reluctance = preference_modifier[girl.get_preference(act)] # From -75 to +150 (negative is better). Used for testing how far the training goes

    $ pic = None
    $ inter.act = act

    # Choose training mode

#    scene black
    call hide_everything() from _call_hide_everything_2
    with fade

    $ choice_menu_girl_interact = True

    ## Advanced training step 1 (set-up)

    if mode == "advanced":
        $ advanced_fix_list = []

        call slave_advanced_training(girl, act, step=1) from _call_slave_advanced_training # Sets 'pic' to specific fixation if available

    ## Action starts

    if response == "accepted":
        $ text1 = "Giving you a sheepish look, "

    elif response == "resisted":
        $ text1 = "Looking at you with mournful eyes, "

    elif response == "magic":
        $ text1 = "With a dazed stare, "

    else:
        $ raise AssertionError("No context found for interaction")

    if act == "naked":
        "[text1]she starts removing her clothes."
    elif act == "service":
        "[text1]she gets on her knees to service you."
    elif act == "sex":
        "[text1]she strips down and lies down on the bed with her legs spread out."
    elif act == "anal":
        "[text1]she removes her skirt and underwear, turning around and bending over, raising her buttocks towards you."
    elif act == "fetish":
        "[text1]she strips naked and positions herself on all fours, waiting for your next move."
    elif act == "bisexual":
        "[text1]she strips down with Sill's help, and the two start fondling each other."
    elif act == "group":
        "[text1]she strips naked as you and the other guy remove your clothes."


    if mode == "train":
        $ not_tags = prepare_not_tags(girl, act)
        if act in ("sex", "group") and girl.has_trait("Virgin"):
            $ pic = girl.get_pic(act, "naked", "rest", "profile", and_tags="virgin", not_tags = not_tags, hide_farm=True, pref_filter=True)
        else:
            $ pic = girl.get_pic(act, "naked", "rest", "profile", not_tags = not_tags, hide_farm=True, pref_filter=True)

        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
        with dissolve

    if not response == "magic":
        $ act_desc = long_act_description[act]
        call dialogue(girl, "slave train " + girl.get_preference(act)) from _call_dialogue_179

    ## Advanced training step 2 (during action)

    if mode == "advanced":
        call slave_advanced_training(girl, act, step=2) from _call_slave_advanced_training_1 # Sets 'pic' to a specific fix if available

    ## Launch action

    call slave_do(girl, act) from _call_slave_do

    ## Advanced training step 3 (conclusion)

    if mode == "advanced" and act != "naked":
        call slave_advanced_training(girl, act, step=3) from _call_slave_advanced_training_2

    stop sound fadeout 3.0
    stop sound2 fadeout 3.0

    if mode == "train":
        show screen show_event(girl.get_pic("rest", and_tags="naked", not_tags=all_sex_acts), x=config.screen_width, y=int(config.screen_height*0.8))
        with fade

    return


label slave_advanced_training(girl, act, step):

    python:

        menu_list = get_fix_menu(act, step, girl)

        if step == 1:
            use_location = [] # init location (use_location must be a list)
            prompt = "How would you like to prepare her for the training?"
        elif step == 2:
            prompt = "Do you ask her to do anything special during training?"
        elif step == 3 and len(menu_list) > 2:
            prompt = "How would you like to finish her training?"

        if len(menu_list) > 2:
            fix = long_menu(prompt, menu_list)
        else:
            fix = "no fix"


        if not debug_mode:
            renpy.block_rollback()

    if fix != "no fix":
        $ advanced_fix_list.append(fix.name)

    $ pic = None
    $ not_tags = prepare_not_tags(girl, act, advanced_fix_list)

    if step < 3:
        $ not_tags.append("cumshot")

    if fix != "no fix":
        if step == 1 and act != "naked": # Should be unnecessary
            $ pic = girl.get_fix_pic(act, fix, and_tags=use_location, not_tags=not_tags + all_jobs, naked_filter=True)

        elif step > 1 and act in ("sex", "group") and girl.has_trait("Virgin"):
            $ pic = girl.get_pic(fix.tag_list[0], act, "naked", "profile", and_tags=["virgin"] + use_location, not_tags = not_tags, hide_farm=True, pref_filter=True)

        else:
            $ pic = girl.get_fix_pic(act, fix, and_tags=use_location, not_tags=not_tags + all_jobs)

    if not pic:
        if step == 1:
            $ pic = girl.profile

        elif step == 2:
            $ pic = girl.get_pic(act, "naked", "rest", "profile", and_tags=use_location, not_tags = not_tags, hide_farm=True, pref_filter=True)

        elif step == 3:
            $ pic = girl.get_pic("rest", "profile", and_tags = ["naked"] + use_location, not_tags = not_tags, hide_farm=True, pref_filter=True)


    if fix != "no fix":

        $ text1 = ""

        if pic:
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
            with dissolve

            # Add flavor text if location is found
            if step == 1:
                if pic.has_tag("town"):
                    $ use_location = ["town"]
                    $ text1 = "You decide to take her out in the street, to spice things up.\n"
                elif pic.has_tag("beach"):
                    $ use_location = ["beach"]
                    $ text1 = "Today is a good day to go to the beach, so you tell [girl.name] to follow you there.\n"
                elif pic.has_tag("nature"):
                    $ use_location = ["nature"]
                    $ text1 = "You decide to take it to the park today, for a change.\n"

        $ text1 += __(fix_description[fix.name + " intro"]) % girl.name

        "[text1]"

        if fix.name in [f.name for f in girl.pos_fixations]:
#            $ text1 = rand_choice(("She is especially aroused by it.", "She blushes red, and you can tell she is getting excited.", "She blushes and bites her lip.", "She looks happy and aroused."))
            $ text1 = __(fix_description[fix.name + " pos_reaction"])

            "[text1]"

            if girl.is_("modest"):
                $ girl.change_love(1)
                $ girl.change_fear(-2)
            elif girl.is_("lewd"):
                $ girl.change_love(2)
                $ girl.change_fear(-1)

            $ reluctance -= 25
            $ girl.change_preference(act, 50)

            if not girl.personality_unlock[fix.name]:
                $ cntext = girl_related_dict[fix.name]
                "You have discovered one of [girl.fullname]'s fixations: {b}[fix.name]{/b}. You can use it to accelerate her training."
                $ girl.personality_unlock[fix.name] = True
                $ test_achievement("pos fixations")
            else:
                $ cntext = girl_related_dict[fix.name]
                "Because [girl.name] loves {b}[fix.name]{/b}, she has progressed faster."

        elif fix.name in [f.name for f in girl.neg_fixations]:
#            $ text1 = rand_choice(("She looks very annoyed.", "She sighs heavily.", "She protests and tries to refuse, but you tell her she must do it."))
            $ text1 = __(fix_description[fix.name + " neg_reaction"])

            "[text1]"

            if girl.is_("modest"):
                $ girl.change_love(-1)
                $ girl.change_fear(2)
            elif girl.is_("lewd"):
                $ girl.change_love(-2)
                $ girl.change_fear(1)

            $ reluctance += 25
            $ girl.change_preference(act, -75)

            if not girl.personality_unlock[fix.name]:
                $ cntext = girl_related_dict[fix.name]
                "You have discovered one of [girl.fullname]'s phobias: {b}[fix.name]{/b}. Perhaps you can put that information to good use."
                $ girl.personality_unlock[fix.name] = True
                $ test_achievement("neg fixations")
            else:
                $ cntext = girl_related_dict[fix.name]
                "Because [girl.name] hates {b}[fix.name]{/b}, her progress has been slowed."

        else:
            if not girl.personality_unlock[fix.name]:
                $ girl.personality_unlock[fix.name] = True



        # Add possibility to change/reverse fixations with training?

    else:
        "She moves on with her training."

    return


label slave_do(girl, act, context="generic"): # Receives 'pic' from the previous label

    if act == "naked":

        $ inter.score = girl.get_stat("libido") - reluctance
        $ text1 = rand_choice(("pinch her nipples", "fondle her breasts", "inspect her juicy body", "pat her butt", "caress her soft skin", "inspect every inch of her body",
                  "check out her generous curves", "give her a thorough physical exam", "just stand there, looking at her naked body"))

        "Taking off her clothes, she stands completely nude for your attention."

        if inter.score < -25:
            "She is shaking with fear and shame, desperately trying to hide her private parts."

            call dialogue(girl, "slave train naked failure") from _call_dialogue_180

            you "This is pointless."

        elif inter.score < 0:
            "You order her to remove her hands from covering her breasts, and she complies grudgingly. She looks very unhappy as you contemplate her assets."

        elif inter.score < 25:
            "She takes some convincing, but eventually she stops covering her body and stands there with her hands behind her back. You move in close to inspect her."

        elif inter.score < 75:
            "She doesn't make a fuss, letting you get an eyeful. It seems that she is getting used to it."

        elif inter.score < 150:
            "She seems to enjoy your gaze as she displays her assets for your inspection. She doesn't complain when you [text1]."

        elif inter.score < 200:
            "She likes being naked, and she moans softly as you [text1]."

        elif inter.score < 300:
            "She loves being naked and feeling your eyes and hands all over her. She almost reaches climax when you [text1]."

        else:
            "Naked is how she always wants to be. Her love juices run down her legs as you [text1]."

            call dialogue(girl, "slave train naked success") from _call_dialogue_181

        if context != "free-form":
            call slave_naked_menu(girl) from _call_slave_naked_menu_1


    elif act == "service":

        $ inter.score = girl.get_stat(act) - reluctance

        play sound s_sucking loop

        if pic.has_tag("oral"):
            $ text1 = rand_choice(("sucks your dick", "licks your shaft and balls"))
            "You push your dick into her mouth, making her service you with her mouth and tongue."

        elif pic.has_tag("handjob"):
            $ text1 = rand_choice(("plays with your dick", "jerks your cock with her soft hands"))
            "You ask her to use her hands to massage and service your dick."

        elif pic.has_tag("titjob"):
            $ text1 = rand_choice(("plays with your dick", "rubs your cock with her oiled tits"))
            "You ask her to use her naughty tits to service your dick."

        elif pic.has_tag("mast"):
            $ text1 = rand_choice(("fingers her wet pussy", "plays with her clit"))
            "You ask her to masturbate and give you a good show while you do the same."

        else:
            $ text1 = "gives you service"
            "You ask her to service you with her body."

        if inter.score < -50:
            "She is completely clueless and unable to give you any pleasure."

            call dialogue(girl, "slave train service failure", narrator_mode=True) from _call_dialogue_182

            you "This is pointless."

        elif inter.score < 0:
            "She has no technique, and you quickly start to feel bored."

        elif inter.score < 25:
            "She isn't very good, and you give her tips to improve her technique."

        elif inter.score < 75:
            "She is starting to get better, and you both get pleasure as she [text1]."

        elif inter.score < 150:
            "She gives you a great show as she [text1], making you hard in an instant."

        elif inter.score < 200:
            "She is very good at this now, giving you a dirty, slutty look as she [text1]."

        elif inter.score < 300:
            "She is a perfect slut, giving you a great show as she services you with her body."

        else:
            "She is a true sex goddess, instantly bringing you to your limit as she [text1]."

            call dialogue(girl, "slave train service success") from _call_dialogue_183


    elif act == "sex":

        $ inter.score = girl.get_stat(act) - reluctance
        $ text1 = rand_choice(("rides your dick", "gets fucked in all positions", "gets fucked hard and deep", "gets a good pounding from your hard cock"))

        play sound s_moans loop

        "You waste no time and start fucking her."

        if inter.score < -50:
            "Her pussy is completely dry. She has zero experience and just lays there, waiting for it to be over."

            call dialogue(girl, "slave train sex failure") from _call_dialogue_184

            "Frustrated, you give up after a minute."

            you "This is useless."

        elif inter.score < 0:
            "She has very little experience, and all she can do is lay there as you have your way with her."

        elif inter.score < 25:
            "She gets a little wet, and you can fuck her a little more easily. She doesn't seem to enjoy herself much, however."

        elif inter.score < 75:
            "She is starting to feel it more, moaning as she [text1]."

        elif inter.score < 150:
            "She is already wet when you enter her, and her screams grow louder as she [text1]."

        elif inter.score < 200:
            "She is already very wet, and she takes initiative, screaming with pleasure as she [text1]."

        elif inter.score < 300:
            "She loves it when she [text1], begging you to slam your hard cock into her wet pussy."

        else:
            "Her pussy is dripping with love juice. She is a true sex goddess, gripping your dick inside her hot, wet cunt as you give her a fierce pounding."

            call dialogue(girl, "slave train sex success") from _call_dialogue_185


    elif act == "anal":

        $ inter.score = girl.get_stat(act) - reluctance
        $ text1 = rand_choice(("fuck her tight asshole", "lift her legs in the air and fuck her butt", "slap her ass as you give it a good fucking", "violate her ass"))

        play sound s_moans loop

        "You push your hard dick inside her tight ass."

        if inter.score < -50:
            "Her asshole shuts down completely. You can't even get an inch inside. You give up after a minute, upset and frustrated."

            call dialogue(girl, "slave train anal failure") from _call_dialogue_186

            you "Such a waste of time..."

        elif inter.score < 0:
            "You manage to get in with great difficulty, using a lot of lube. She complains that it hurts."

        elif inter.score < 25:
            "She relaxes a little, and you manage to get inside even though she's extremely tight."
            girl.char "I feel weird..."

        elif inter.score <= 75:
            "She is more relaxed now, and you slide in without too much trouble. She moans as you give her a good fucking."

        elif inter.score <= 150:
            "It's becoming easier and easier to move inside her ass. She moans like a horny bitch as you [text1]."

        elif inter.score <= 200:
            "Moving inside her ass is easy now, and she squeals with pleasure as you give her little asshole a pounding."

        elif inter.score <= 300:
            "She loves to feel your dick as you [text1], and begs you to fuck her deeper and harder."

        else:
            "She cums almost immediately as you [text1]. She's a perfect anal slut now."

            call dialogue(girl, "slave train anal success") from _call_dialogue_187

    elif act == "fetish":

        $ inter.score = girl.get_stat(act) - reluctance
        $ text1 = rand_choice(("use your favorite toys on her", "rape her with some of your new toys", "violate her holes with cruel and unusual tools", "tie her to a bizarre contraption and fuck her brains out"))

        "You open your toolbox."

        play sound s_screams

        if inter.score < -50:
            "She cries and squirms to avoid you as you try to tie her up."

            call dialogue(girl, "slave train fetish failure") from _call_dialogue_188

            "In the end, you barely make any progress, she was too wild and afraid."

        elif inter.score < 0:
            "You tie her hands behind her back, and tease her a little. She cries and doesn't enjoy it at all."

        elif inter.score < 25:
            "You tie her up and use a variety of tools on her. She is ashamed and scared, but a little turned on as well."

        elif inter.score <= 75:
            "She is getting used to being tied up. She moans with pleasure and pain as you [text1]."

        elif inter.score <= 150:
            "She is starting to enjoy it more and more. She's already wet when you [text1]."

        elif inter.score <= 200:
            "She suggests new ways to tie her up and cries with pleasure as you [text1]."

        elif inter.score <= 300:
            "She loves pain and wants to try everything. She begs you to [text1]."

        else:
            "She cums numerous times as you tie her up in a bizarre position and use all of your toys on her. What a kinky bitch!"

            call dialogue(girl, "slave train fetish success") from _call_dialogue_189

            girl.char "Master... Please hurt me... {nw}"
            if girl.is_("modest"):
                extend "I'm a dirty, dirty slut..."
            else:
                extend "It's giving me so much pleasure... Ah!"


    elif act == "bisexual":

        $ inter.score = (girl.get_stat("service") + girl.get_stat("sex"))/2  - reluctance
        $ text1 = rand_choice(("licking the love juice from Sill's cunt", "fucking Sill with a black rubber strap-on", "rubbing her clit hard against Sill's pussy", "kissing Sill passionately while she plays with herself"))

        play sound s_moans loop

        "[girl.name] and Sill get on top of each other."

        play sound s_moans loop
        play sound2 s_moans_short loop

        if inter.score < -50:
            "She's obviously disgusted by Sill. She won't even touch her."

            call dialogue(girl, "slave train bisexual failure") from _call_dialogue_190

            "Sill gives her a soft kiss and gets up. You tell her to leave."

        elif inter.score < 0:
            "The two girls kiss and fondle each other. [girl.name] doesn't even pretend to enjoy it."

        elif inter.score < 25:
            "[girl.name] kisses Sill a little bit more passionately this time. She's slowly forgetting that she is with a girl."

        elif inter.score <= 75:
            "[girl.name] is now more enthusiastic about being with a girl. She enjoys [text1]."

        elif inter.score <= 150:
            "[girl.name] has a surprise orgasm while [text1]. She is starting to understand the pleasures to be had with women."

        elif inter.score <= 200:
            "[girl.name] doesn't differentiate between men and women now. She fucks Sill enthusiastically, bringing her off several times."

        elif inter.score <= 300:
            "She loves [text1]. Sill and [girl.name] shake with a mutual orgasm while doing a 69."

        else:
            "She loves fucking women and is completely bisexual now. [girl.name] and Sill know each other's body perfectly now, and bring each other off numerous times."

            call dialogue(girl, "slave train bisexual success") from _call_dialogue_191


    elif act == "group":

        $ inter.score = (girl.get_stat("service") + girl.get_stat("sex") + girl.get_stat("anal"))/3  - reluctance
        $ text1 = rand_choice(("fuck her hard while she sucks the other guy off", "fuck her while the other guy does her ass", "use her holes to satisfy yourself and the random guy", "make her deepthroat your dick while the other guy rams her"))

        play sound s_moans loop
        play sound2 s_moans_short loop

        "You and the other dude start fondling her private parts."

        if inter.score < -50:

            call dialogue(girl, "slave train group failure") from _call_dialogue_192

            "She doesn't know how to react. She remains stiff and passive, waiting for you to finish."

            "Disappointed, you stop and dismiss the guy. He looks pissed."

        elif inter.score < 0:
            "She clumsily manages to bring one of you off. She isn't doing much, but it's a start."

        elif inter.score < 25:
            "[girl.name] takes turns sucking your and the other guy's dick, before you proceed to fuck her. She is putting more heart into it."

        elif inter.score <= 75:
            "You [text1]. [girl.name] looks more relaxed now, and it's less awkward."

        elif inter.score <= 150:
            "[girl.name] moans with pleasure as you [text1]."

        elif inter.score <= 200:
            "[girl.name] is happy to oblige as you proceed to [text1]. She likes fooling around in a group."

        elif inter.score <= 300:
            "She loves it when you [text1]. It seems she loves fucking a group."

        else:
            "She brings you and the guy off many times, her holes dripping with cum. She begs you to bring more and more people next time. She adores group sex."

            call dialogue(girl, "slave train group success") from _call_dialogue_193

    $ inter.result = inter.score

    if not girl.personality_unlock[act]:

        $ pos_reaction, neg_reaction = girl.test_weakness(act, unlock=True)

        if pos_reaction and neg_reaction:
            $ renpy.say("", __("You notice that ") + girl.name + __(" is feeling strange during ") + __(long_act_description[act]) + __(". It's like she both loves it and hates it."))
        elif pos_reaction:
            $ renpy.say("", __("You notice that ") + girl.name + __(" is very sensitive during ") + __(long_act_description[act]) + __(". Perhaps you should explore this further."))
        elif neg_reaction:
            $ renpy.say("", __("You notice that ") + girl.name + __(" seems to dislike ") + __(long_act_description[act]) + __(". Perhaps there's something in particular that makes her uncomfortable."))


    return


label slave_rape_test(girl, act=None, intensity=1):

    $ inter.response = "refused"

    if girl.promised:
        call break_promise(girl) from _call_break_promise_1

    "You step forward menacingly."

    call fight_attempt(girl, act, intensity) from _call_fight_attempt_20

    if _return:
        $ inter.result = "fled"
        return

    elif girl.is_("very sub"):

        "She looks away as you approach her, but doesn't try to stop you."

        play sound s_ahaa

        "She blushes as she feels your hands touch her body."

    else:
        play sound s_scream

        call dialogue(girl, "slave strongly refuse") from _call_dialogue_194

        "She sobs and fights you weakly as you push her on the bed."

    $ inter.result = "forced"

    return




## 3. MAGICAL TRAINING ##

label slave_hypnotize_method(girl):

    menu:
        "Hypnosis is more efficient when exploiting your girl's existing emotions. Which technique will you use to train [girl.name]?"

        "利用正面情绪":
            "Reinforcing positive emotions works better if a girl likes you."
            $ girl.magic_training = "positive"

        "利用负面情绪":
            "Reinforcing negative emotions works better if a girl fears you."
            $ girl.magic_training = "negative"

        "保持情绪稳定":
            "Balanced training uses a mix of positive and negative emotions to influence your girl."
            $ girl.magic_training = "balanced"

    $ inter.canceled = True
    return


label slave_magic(girl, mode="train"):

    $ act = inter.act

    if not girl.magic_training:
        call slave_hypnotize_method(girl) from _call_slave_hypnotize_method

    $ text1 = rand_choice(MC.filter_say(("ar: 太阳神的神光{nw}", "sh: 黑夜中的莎莉娅{nw}", "五大元素的力量{nw}", "ev: 7层地狱的力量{nw}", "gd: 纯洁的灵魂", "ne: 龙之怒吼{nw}",
                   "ng: 时之沙{nw}", "魔力的律动{nw}", "死星的激光射线{nw}", "腥红之月的暗面{nw}", "无边无际的海洋{nw}")))

    $ text1 += ", 我命令你, "

    $ text1 += rand_choice(("跟着我的声音走进迷宫...", "脱离物质世界的禁锢...",
                           "进入深深的沉睡...", "不要抵抗梦境的侵蚀...", "踏上遗忘之海的旅程...",
                           "忘记你是谁，忘记你躺在哪里...", "你是我故事中的角色..."))

    play sound s_spell

    "闭上眼聆听你的声音, [girl.name]渐渐听不清你说的话语。她保持站姿, 目光逐渐呆滞，眼神变得空洞。"

    if girl.magic_training == "positive":
        "你开始用温柔的语气下达指令。"
        $ bonus = (girl.get_love() - girl.get_fear())//10

    elif girl.magic_training == "negative":
        "你开始用威胁的语气下达指令。"
        $ bonus = (girl.get_fear() - girl.get_love())//10
    else:
        "你开始用平静的语气下达指令。"
        $ bonus = 0

    $ bonus += girl.get_effect("change", "hypnosis")

    if act == "obedience":
        you "只有主人才能打开你内心的枷锁.你要服从主人的一切命令."
        "你在她面前晃动着一把奇怪的钥匙。"
        $ diff = 2

    elif act == "libido":
        you "你是个沉迷欲望的荡妇，你的欲望就像荆棘一样缠绕着你的灵魂..."
        "你把一根银针扎入她的乳头. 她不仅没有感到疼痛,反而有些享受。"
        $ diff = 2

    elif act == "sensitivity":
        you "不要抗拒你的本性，如果你感到快乐，那么众神也会感到满足..."
        "你点燃了一根东方的熏香，香味让人有些飘飘欲仙。"
        $ diff = 2

    elif act == "naked":
        you "让我好好欣赏你的身体..."
        "你在她面前摆了一面全身镜，她可以从中看到自己的每个部位。"
        $ diff = 4

    elif act == "service":
        you "我是你的所有者，你的主人。能够用你的身体侍奉我是你的荣幸。"
        "你把神仙快乐水滴进她的嘴里。"
        $ diff = 5

    elif act == "sex":
        you "我是你的所有者，你的主人。准备好收下我的恩赐吧。"
        "你把一个又大又亮的金色假阳具放在她面前。"
        $ diff = 6

    elif act == "anal":
        you "我是你的所有者，你的主人。.. 你身上的每个洞都将被我填满..."
        "你掀起她的裙子，把她的内裤推到一边，轻轻地把一颗珍珠塞入她的菊花."
        $ diff = 7

    elif act == "fetish":
        you "我是你的所有者，你的主人。只要我想... 跪下求我。"
        "你从口袋里掏出一对银夹子，夹在她的两个乳头上，两颗葡萄涨得发紫。"
        $ diff = 8

    elif act == "bisexual":
        you "和你的姐妹一起来侍奉我吧..."
        "你让希露加入其中，让她在腰间戴上假阳具。它以暗元素驱动。"
        sill naked "哈! 主人, 我插进去了..."
        $ diff = 9

    elif act == "group":
        you "欢迎加入淫乱派对..."
        "吟唱了一段古老的咒语，你召唤了一个元素傀儡。它不会主动思考，但它拥有巨大的肉棒...在你的操纵下它立即将注意力转向 [girl.name]。"
        $ diff = 10

    if girl.is_("very dom"):
        $ diff += 1
    elif girl.is_("very sub"):
        $ diff -= 2
    elif girl.is_("sub"):
        $ diff -= 1

    # Run challenge
    if MC.get_effect("special", "snake eyes"):
        $ force_win = 3
    else:
        $ force_win = False

    call challenge("control", diff, bonus=bonus, score=True, forced=force_win) from _call_challenge_62 # result is stored in the _return variable
    $ inter.score = _return

    $ d = MC.challenges["control"].d - MC.challenges["control"].d_op

    if d >= 3:
        "魔法效果十分强劲。她变成了不会思考的人偶。 {nw}"
    elif d <= -3:
        "你对她意识的影响十分微弱。你得快点完事。 {nw}"
    else:
        "她潜意识里一直在抵抗，但你努力克服了它。 {nw}"

    if inter.score > 0:

        $ inter.result = "success"
        $ girl.add_log("hypnotize success")

        play sound s_spell

        extend "催眠很成功, [girl.name]没有意识到你在做什么，只知道听从你的命令。"

        call dialogue(girl, "slave magic " + act + " success") from _call_dialogue_195

        if act in extended_sex_acts:
            $ inter.act = act
            call slave_train(girl, act, "magic", mode) from _call_slave_train_2

    elif inter.score == 0 or MC.get_effect("special", "hypnosis no fail"):

        $ inter.result = "moderate"

        play sound s_spell

        extend "[girl.name]看起来晕头转向，精神恍惚。她拒绝服从你的指令，但你能感觉到她的反抗在不断减弱。"

        "几分钟后, 你停止了催眠, 这次进展不太顺利。"

    else:

        $ inter.result = "fail"
        $ girl.add_log("hypnotize failure")

        play sound s_fizzle

        extend ""

        call dialogue(girl, "slave magic failure") from _call_dialogue_196

    return


## 4. ENCOURAGE ##

label slave_reward_praise(girl):
    if dice(4) >= 4:
        python:
            counter = 0

            for stat in ("beauty", "body", "charm", "refinement"):
                if girl.get_stat(stat) > counter:
                    my_stat = stat
                    counter = girl.get_stat(stat)

        if my_stat == "beauty":
            you "你一天比一天漂亮，客人们都喜欢你。"
        elif my_stat == "body":
            you "你今天看起来很性感，你令我神魂颠倒。"
        elif my_stat == "charm":
            you "你今天魅力十足， 回头率百分之一万。"
        elif my_stat == "refinement":
            you "你就像是个公主一样，那些女人都在嫉妒你。"

    else:
        $ MC.rand_say(("你很努力，我很感激。", "没有你，这个地方就不一样了。谢谢你。", "gd: 感谢你付出的努力。我对你非常满意。",
                    "ev: 你是我最有效率的仆人之一。不过不要变得自满。", "ne: 你是一个好奴隶，像你这样的好货色越来越少了。",
                    "ar: 太阳神在上，他会奖励你的精神。", "sh: 女神大人说：在阴影中劳作的人将获得十倍的回报。", "ng: 我不相信什么神，但你可能是一个天使*眨眼*。"))

    $ success_factor = 1
    call slave_reward(girl, "praise") from _call_slave_reward
    return

label slave_reward_gold(girl):

    $ low, med, high = 25 * (girl.rank**2), 100 * (girl.rank**2), 250 * (girl.rank**2)

    menu:
        "你愿意给她多少金币?"

        "[low] 金币" if MC.gold >= low:
            $ MC.gold -= low
            $ success_factor = 0.5

        "[med] 金币" if MC.gold >= med:
            $ MC.gold -= med
            $ success_factor = 1

        "[high] 金币" if MC.gold >= high:
            $ MC.gold -= high
            $ success_factor = 2

        "返回":
            $ inter.canceled = True
            return

    play sound s_gold
    you "希望这点微薄的谢礼可以帮你解决燃眉之急."

    call slave_reward(girl, "gold") from _call_slave_reward_1
    return

label slave_reward_gift(girl):
    python:
        available_gifts = []

        for it in MC.items:
            if it.usage == "gift":
                available_gifts.append(it)

    $ you("这是为你准备的...", interact = False)

    python:

        gift_list = []

        for it in available_gifts:
            gift_list.append((it.name, it))

        gift_list.append(("Go back", "back"))

        inter.result = long_menu("Choose a present", gift_list)

    if inter.result == "back":
        $ inter.canceled = True
        return

    $ success_factor = 1

    call slave_reward(girl, "gift") from _call_slave_reward_2
    return

label slave_reward_pet(girl):
    $ MC.rand_say((__("过来！谁是我最可爱的小奴隶...是 ") + girl.name + __("！没错！"), __("过来，给主人 ") + MC.name + __(" 一个拥抱。把舌头伸出来...."), __("来这里，宝贝，坐到爸爸腿上。")))
    $ success_factor = 1
    call slave_reward(girl, "pet") from _call_slave_reward_3
    return

label slave_reward_day(girl):
    you "你最近工作一直很努力. 今晚为什么不好好休息一下呢?"
    $ success_factor = 1
    call slave_reward(girl, "day off") from _call_slave_reward_4
    return

label slave_reward_sex(girl):
    $ act = menu(get_act_menu(prompt="What do you want to reward her with?", extended=False, girl=girl))

    if act == "back":
        $ inter.canceled = True
        return
    else:
        $ inter.act = act

    if act == "service":
        you "作为你的奖励，我就让你来侍奉我吧 *脱下裤子*。"
    elif act == "sex":
        you "作为你的奖励，到床上把你的屁股撅起来，我来让你好好爽一爽。*解开腰带*"
    elif act == "anal":
        you "过来躺下, 把大腿掰开，让我们来看看你能吞下几只手指。*戴上手套，涂上润滑油*"
    elif act == "fetish":
        you "你值得我用上那些宝贝...把我的玩具箱拿来。*给她带上眼罩口球*"

    $ inter.response = girl.training_check(inter.act)
    $ success_factor = 1

    call dialogue(girl, "slave reward sex " + inter.response) from _call_dialogue_197

    if inter.response == "accepted":

        if girl.is_("very lewd"):
            $ success_factor *= 1.5
        elif girl.is_("lewd"):
            $ success_factor *= 1.25
        elif girl.is_("very modest"):
            $ success_factor *= 0.5
        elif girl.is_("modest"):
            $ success_factor *= 0.75

    elif inter.response == "resisted":

        if girl.is_("very sub"):
            $ success_factor *= 1
        elif girl.is_("sub"):
            $ success_factor *= 0.5
        elif girl.is_("very dom"):
            $ success_factor *= -0.5
        elif girl.is_("dom"):
            $ success_factor *= 0

        menu:
            "你打算怎么办?"
            "坚持到底":

                if girl.promised:
                    call break_promise(girl) from _call_break_promise_2

                "你无视了她的哀嚎和泪水，把她一把丢到床上."

                $ inter.MC_reaction = "proceed"

            "放她一马":
                $ MC.rand_say((__("好吧...随你的便。"), __("真不敢相信现在的奴隶...好吧！"), __("ne: 哼，这次就先放过你，但是下次..."),
                                    __("gd: 好吧，我不会强迫你做你不喜欢的事情。"), __("ev: 操，这一次我就放过你了....但是不要考验我的耐心。")))

                $ inter.MC_reaction = "give up"

                return

    else:
        with vpunch

        menu:
            "你打算怎么办?"

            "坚持到底":
                $ MC.rand_say(("我是你的主人。你必须服从我。", "你要按照我的意愿行事！这是最后通牒！！！",
                    "ev: 闭嘴，婊子。规矩是我定的！", "gd: 我的耐心是有限度的。这一次你逃不掉了。"))

                $ inter.MC_reaction = "force"
                $ inter.score = 0
#                 $ impact = 2

                call slave_rape(girl, act) from _call_slave_rape_1

                return

            "放她一马":
                $ MC.rand_say(("好吧....按你说的做。", "我简直不敢相信现在的奴隶....好吧！", "ne: 哼，这一次我放过你。你欠我一个人情。",
                                "gd: 好吧，我不会强迫你做你讨厌的事情。", "ev: 他妈的，这一次我放过你....但不要考验我的耐心。"))

                $ inter.MC_reaction = "give up"

                return


    call slave_reward(girl, "sex") from _call_slave_reward_5
    return

label slave_reward(girl, rew):

    $ inter.type = rew

    call slave_justify(girl, "reward") from _call_slave_justify # Gives the 'reason' for encouraging

    if inter.reason == "back":
        $ inter.canceled = True
        return

    if inter.reason == "sick":
        "You tell her that you are sorry that she fell sick."
    elif inter.reason == "hurt":
        "You tell her that you are sorry that she got hurt."
    elif inter.reason == "level":
        "You tell her that you are happy she is learning fast."
    elif inter.reason:
        $ renpy.say("", __("你告诉她你很高兴，因为 ") + uncapitalize(girl.recent_events[inter.reason].description)) # Fetches event description
    else:
        you "I feel like rewarding you today... For no particular reason."

    if rew == "praise":

        call dialogue(girl, "slave reward " + rew) from _call_dialogue_198

        $ impact = 1 + MC.get_charisma()/3

        if girl.is_("very idealist"):
            $ success_factor *= 1.5
        elif girl.is_("idealist"):
            $ success_factor *= 1.25
        elif girl.is_("very materialist"):
            $ success_factor *= 0.5
        elif girl.is_("materialist"):
            $ success_factor *= 0.75

    elif rew == "gold":

        call dialogue(girl, "slave reward " + rew) from _call_dialogue_199

        $ impact = 2

        if girl.is_("very materialist"):
            $ success_factor *= 1.5
        elif girl.is_("materialist"):
            $ success_factor *= 1.25
        elif girl.is_("very idealist"):
            $ success_factor *= 0.5
        elif girl.is_("idealist"):
            $ success_factor *= 0.75

    elif rew == "gift":

        $ impact = 3

        $ inter.score = MC.gift(girl, inter.result)

        if inter.score > 2:
            $ success_factor *= 2
        elif inter.score > 0:
            $ success_factor *= 1
        elif inter.score == 0:
            $ success_factor *= 0.5
        else:
            return

    elif rew == "pet":

        call dialogue(girl, "slave reward " + rew) from _call_dialogue_200

        if girl.is_("very sub"):
            $ success_factor *= 1.5
        elif girl.is_("sub"):
            $ success_factor *= 1.25
        elif girl.is_("very dom"):
            $ success_factor *= 0.5
        elif girl.is_("dom"):
            $ success_factor *= 0.75

        $ impact = 1 * MC.get_charisma()/3

    elif rew == "day off":

        $ res = girl.get_day_off(1)

        if res:
            call dialogue(girl, "slave reward " + rew) from _call_dialogue_201

            if girl.is_("very dom"):
                $ success_factor *= 1.5
            elif girl.is_("dom"):
                $ success_factor *= 1.25
            elif girl.is_("very sub"):
                $ success_factor *= 0.5
            elif girl.is_("sub"):
                $ success_factor *= 0.75

            if girl.is_("very extravert"):
                $ success_factor *= 1.5
            elif girl.is_("extravert"):
                $ success_factor *= 1.25
            elif girl.is_("very introvert"):
                $ success_factor *= 0.5
            elif girl.is_("introvert"):
                $ success_factor *= 0.75

            $ impact = 2

        else:
            call dialogue(girl, "slave reward day off KO") from _call_dialogue_202

            $ inter.canceled = True
            return

    elif rew == "sex":
        call slave_train(girl, inter.act, inter.response) from _call_slave_train_3

        $ impact = 3


    # Get results from encouraging
    $ inter.result = True
    $ inter.score = impact*success_factor

    if rew != "praise":
        $ girl.add_log("rewarded")

    if girl.spoiled:
        "你的奖励没那么有效，因为她最近被宠坏了。"
        $ inter.score *= 0.5
        $ unlock_achievement("spoiled")

    return


## 5. DISCIPLINE ##

label slave_punish_scold(girl):
    if dice(4) >= 4:
        python:
            counter = 999

            for stat in ("beauty", "body", "charm", "refinement"):
                if girl.get_stat(stat) < counter:
                    my_stat = stat
                    counter = girl.get_stat(stat)

        if my_stat == "beauty":
            $ MC.rand_say(("gd: 你没有好好照顾自己的外表。你应该做得更好。", "ne: 如果你像你现在这样忽视自己，顾客是不会喜欢你的。",
                           "ev: 你只是一头丑牛。努力吧！"))
        elif my_stat == "body":
            $ MC.rand_say(("gd: 请你锻炼一下？你必须变得有吸引力。", "ne: 如果你不努力变得性感，人们就不会喜欢你。这意味着对我来说钱会更少。",
                           "ev: 看看你有多胖。你很恶心。"))
        elif my_stat == "charm":
            $ MC.rand_say(("gd: 你能不能更有魅力一点？你有时候可以很粗鲁。", "ne: 没有两种方法，你只是不会与人相处。", "ev: 你是一个粗鲁和傲慢的婊子。降低一点，否则...."))
        elif my_stat == "refinement":
            $ MC.rand_say(("gd: 请努力变得更有品位。这是一个高档的青楼，不是鱼市场。", "ne: 你真的必须向每个人展示你是多么无知和不成熟吗？", "ev: 我发誓，你比门把手还笨。你最好学习礼仪，否则我会让你学习。"))

    else:
        $ MC.rand_say(("ar: 为了太阳神的爱，你能不能努力表现一下？", "sh: 我发誓，在莎莉娅的阴影下没有比你更懒惰的奴隶了！",
                       "ng: 如果你有一个造物主，我会让你去见他！", "gd: 你没有尽你的最大努力，这伤害了我们所有人。", "ne: 你懒惰又傲慢。你必须做得更好。", "ev: 你不尊重我，你最好准备好面对后果。"
                       "为什么不试着更努力一点呢？", "你必须做得更好，为了你自己的利益。"))

    call slave_punish(girl, "scold") from _call_slave_punish
    return

label slave_punish_upkeep(girl):
    $ MC.rand_say(("我看你太舒服了。所以明天我就把你的生活费减为零。看看你喜不喜欢在空腹下工作。", "我想如果我继续宠着你，你只会变得又胖又懒。明天你将得不到任何生活费。"))

    if girl.upkeep == 0:

        call dialogue(girl, "slave punish upkeep KO") from _call_dialogue_203

        $ inter.canceled = True

        return

    $ girl.cut_upkeep(1)

    call slave_punish(girl, "upkeep") from _call_slave_punish_1
    return

label slave_punish_naked(girl):
    you "把你的衣服都脱了。包括内衣。你就这样光着身子为客人服务吧。"

    if girl.naked:

        call dialogue(girl, "slave punish naked KO") from _call_dialogue_204

        $ inter.canceled = True
        return

    call slave_punish(girl, "naked") from _call_slave_punish_2
    return

label slave_punish_beat(girl): # To do: add a special reaction if she loves/hates spanking
    $ MC.rand_say(("恐怕你别无选择。", "如果服从不是你的天性，那就后天培养。", "ev: 你这个笨蛋，一无是处的婊子！！！如果你听不懂人话，我就把它打进你那空空如也的脑袋里！"))
    "握着一把长钢尺, 你让她把领口的扣子都解开."
    call slave_punish(girl, "beat") from _call_slave_punish_3
    return

label slave_punish_rape(girl):
    you "你得好好上一课! 我得确保你听进去了."

    $ result = menu(get_act_menu(prompt="How will you punish her this time?", extended=False, girl=girl, conditions=False))

    if result == "back":
        $ inter.canceled = True
        return

    $ inter.act = result

    if result == "service":
        "你解开腰带，命令她跪在你的面前"
        you "好了, 用你的手和小嘴来伺候我."
    elif result == "sex":
        "你把她带到床边，让她脱光衣服."
        you "这么喜欢顶嘴，我倒要看看你下面的嘴是不是也这么硬气."
    elif result == "anal":
        "抓着她的胳膊, 你把她翻过来，在她耳边用威胁的语气低语."
        you "让我们看看在我干爆你的菊花之后你还会不会嘴硬."
    elif result == "fetish":
        "你给她看挂在墙上的架子，让她把手叠在一起，这样你就可以把它们绑起来."
        you "我要让你感受一下“惩罚”的真正含义'."

    call slave_punish(girl, "rape") from _call_slave_punish_4
    return

label slave_punish_farm(girl):
    $ MC.rand_say(("ar: 很好，也许在农场的地牢里你能认清自己的身份。", "ne: 我该怎么办？哦，我知道谁可以帮我...我的朋友吉泽尔。",
                "ev: 既然你不喜欢在这待着，那就去农场的地牢里睡吧", "gd: 我不喜欢吉泽尔的方法，但确实有用。那么我就把你送到农场去吧。", "滚去农场待几天吧。"))
    call slave_punish(girl, "farm") from _call_slave_punish_5
    return

label slave_punish(girl, pun):

    $ inter.type = pun

    call slave_justify(girl, "punish") from _call_slave_justify_1 # Gives the 'reason' for disciplining

    if inter.reason == "back":
        $ inter.canceled = True
        return

    if inter.reason == "sick":
        "You tell her that it's her own fault if she got sick."
    elif inter.reason:
        $ renpy.say("", __("你告诉她你很生气，因为 ") + uncapitalize(girl.recent_events[inter.reason].description)) # Fetches event description
    else:
        you "骂你还需要理由吗, 小贱货!"

    $ success_factor = 1

    if pun == "scold":

        $ impact = 1 + MC.get_charisma()/3

        if inter.reason:
            call dialogue(girl, "slave punish scold deserved") from _call_dialogue_205
        else:
            call dialogue(girl, "slave punish scold undeserved") from _call_dialogue_206

        if girl.is_("very idealist"):
            if inter.reason:
                $ success_factor = 1.5
            else:
                $ success_factor = 0.5
        elif girl.is_("idealist"):
            if inter.reason:
                $ success_factor = 1.25
            else:
                $ success_factor = 0.75
        elif girl.is_("very materialist"):
            $ success_factor = 0.5
        elif girl.is_("materialist"):
            $ success_factor = 0.75

    elif pun == "upkeep":

        $ impact = 2

        call dialogue(girl, "slave punish " + pun) from _call_dialogue_207

        if girl.is_("very materialist"):
            $ success_factor *= 1.5
        elif girl.is_("materialist"):
            $ success_factor *= 1.25
        elif girl.is_("very idealist"):
            $ success_factor *= 0.5
        elif girl.is_("idealist"):
            $ success_factor *= 0.75


    elif pun == "beat":

        # Chance of sub girls begging

        if girl.is_("sub") and dice(6) >= 5:

            call slave_beg(girl, "punish") from _call_slave_beg_1

            if inter.MC_reaction in ("give up", "warning"):
                $ inter.score = 3
                return

        call slave_rape_test(girl, act=None, intensity=2) from _call_slave_rape_test

        if not can_interact(girl):
            return

        "你脱下她的内裤，用金属尺子反复敲打她裸露在外的屁股。"

        call dialogue(girl, "slave punish " + pun) from _call_dialogue_208

        if girl.is_("very sub"):
            $ success_factor = 1.5
        elif girl.is_("sub"):
            $ success_factor *= 1.25
        elif girl.is_("very dom"):
            $ success_factor *= 0.5
        elif girl.is_("dom"):
            $ success_factor *= 0.75

        $ impact = 3 * MC.get_defense()/3
        $ girl.add_log("beaten")

        with fade

    elif pun == "naked":

        # Chance of sub girls begging

        if girl.is_("sub") and girl.test_weakness(pun)[1] and dice(6) >= 5:

            call slave_beg(girl, "punish") from _call_slave_beg_2

            if inter.MC_reaction in ("give up", "warning"):
                $ inter.score = 2
                return

        $ impact = 2

        call slave_rape(girl, pun) from _call_slave_rape_2

    elif pun == "rape":

        if girl.is_("sub") and girl.test_weakness(inter.act)[1] and dice(6) >= 5:

            call slave_beg(girl, "punish") from _call_slave_beg_3

            if inter.MC_reaction in ("give up", "warning"):
                $ inter.score = 3
                return

        call dialogue(girl, "slave punish " + pun) from _call_dialogue_209

        if girl.is_("very modest"):
            $ success_factor = 1.5
        elif girl.is_("modest"):
            $ success_factor *= 1.25
        elif girl.is_("very lewd"):
            $ success_factor *= 0.5
        elif girl.is_("lewd"):
            $ success_factor *= 0.75

        $ inter.response = "refused"

        $ impact = 3

        call slave_rape(girl, inter.act) from _call_slave_rape_3

    elif pun == "farm":

        call dialogue(girl, "slave punish " + pun) from _call_dialogue_210

        if girl.is_("very dom"):
            $ success_factor *= 1.5
        elif girl.is_("dom"):
            $ success_factor *= 1.25
        elif girl.is_("very sub"):
            $ success_factor *= 0.5
        elif girl.is_("sub"):
            $ success_factor *= 0.75

        menu:
            "你想让她在农场待多久?"

            "1 天":
                $ impact = 2
                call send_to_farm(girl, duration=1) from _call_send_to_farm
            "3 天":
                $ impact = 5
                call send_to_farm(girl, duration=3) from _call_send_to_farm_1
            "7 天":
                $ impact = 8
                call send_to_farm(girl, duration=7) from _call_send_to_farm_2

        if girl not in farm.girls: # This happens if the girl cannot be sent to the farm for any reason. The interaction will fail.
            $ impact = 0
            $ inter.result = "fail"

    # Get results from disciplining

    $ inter.score = impact*success_factor # Score ranges from 0 to 12 (farm)

    if pun != "scold":
        $ girl.add_log("punished")

    if girl.terrified:
        "你的惩罚没那么有效，因为她最近已经被惩罚太多次了。"
        $ inter.score *= 0.5
        $ unlock_achievement("terrified")

    return

label slave_rape(girl, act): # If girl refused and was forced

    if not act:
        $ raise AssertionError("No sex act found for " + str(act) + " " + str(inter.response))

    call slave_rape_test(girl, act, intensity=3) from _call_slave_rape_test_1

    if not can_interact(girl):
        return

    python:
        reluctance = preference_modifier[girl.get_preference(act)]

        not_tags = ["happy", "dom", "group", "bisexual", "date", "rest"]

        if act == "naked":
            not_tags += all_sex_acts

    $ pic = girl.get_pic(act, "naked", "rest", "profile", not_tags = not_tags, hide_farm=True, pref_filter=True)

    $ advanced = False

    # Choose punish mode

    if girl.personality_unlock[act]:

        $ pos_reaction, neg_reaction = girl.test_weakness(act)
        $ advanced = False

        if pos_reaction and neg_reaction:
            $ reaction = "ambivalent feelings"
        elif neg_reaction:
            $ reaction = "a disgust"
        else:
            $ reaction = ""

        if reaction:
            $ cntext = girl_related_dict[act]
            $ cntext2 = girl_related_dict[reaction]
            menu:
                "你记得 [girl.name] 对 [cntext] 行为有 [cntext2] 的反应。你要利用这一点来训练她吗?"

                "是的":
                    $ fix = rand_choice([fix for fix in girl.neg_fixations if girl.personality_unlock[fix.name]])

                    if fix:
                        $ text1 = fix_description[fix.name + " description"][:-1]
                        "你记得她害怕 [text1], 所以你决定就这样训练她。"

                        $ MC.evil += 1
                        $ impact += 2
                        $ reluctance += 50
                        $ inter.result = "neg_fix"

                    else:
                        $ fix = rand_choice([fix for fix in get_fix_list(act) if not girl.personality_unlock[fix.name]])

                        if not fix:
                            $ raise AssertionError("No negative fix found")

                        $ text1 = long_act_description[act]
                        $ text2 = fix_description[fix.name + " description"][:-1]
                        $ cntext = girl_related_dict[fix.name]
                        "你不知道她怕不怕 [text1], 所以你打算试试, 看看她对 [cntext] 会有什么反应。"

                        if fix.name in [f.name for f in girl.neg_fixations]:

                            call dialogue(girl, "slave rape negative fixation") from _call_dialogue_211

                            "看起来你发现了她的弱点。 她很害怕 [text2], 哭喊着求你停下。"
                            $ reluctance += 50
                            $ impact += 1
                            $ inter.result = "neg_fix"

                        elif fix.name in [f.name for f in girl.pos_fixations]:

                            call dialogue(girl, "slave rape positive fixation") from _call_dialogue_212

                            "和你预期的相反, [girl.name] 看起来反而有些享受。这还算得上惩罚吗？"
                            $ reluctance -= 25
                            $ impact -= 1
                            $ inter.result = "pos_fix"

                        else:
                            "不，这不是你想要的效果... 但你还是让她继续。"

                        $ girl.personality_unlock[fix.name] = True

                "不了":
                    pass

    call hide_everything() from _call_hide_everything_3

    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
    with dissolve


    call dialogue(girl, "slave punish rape") from _call_dialogue_213
    if act == "naked":

        if girl.is_("very modest"):
            $ success_factor = 1.5
        elif girl.is_("modest"):
            $ success_factor = 1.25
        elif girl.is_("very lewd"):
            $ success_factor = 0.5
        elif girl.is_("lewd"):
            $ success_factor = 0.75

        "Ignoring her indignant cries, you rip off her slave clothes, leaving her bare naked with her torn clothes laying in a heap on the floor."

        $ score = girl.get_stat("libido") - reluctance

        play sound s_surprise

        you "Let's see how you like spending the rest of the day naked then."

        $ test_achievement("naked")

        if score < -25:
            "She is horrified and begs you numerous times to spare her. You refuse, however, and she keeps crying all day long
             while hiding herself as much as possible."

        elif score < 0:
            "She doesn't know what to do and tries to hide as much as possible. But she has to put up with everyone staring at her all day."

        elif score < 50:
            "She complains and whines but she has to obey your orders. She grudgingly gets on with her day."

        elif score < 150:
            "She lowers her head and looks down, but she's also blushing. It seems she is both ashamed and a little turned on by your orders."

        elif score < 300:
            "She doesn't seem to mind much having to expose her body to strangers."

        else:
            "In spite of your threats, she is completely comfortable being naked all day, it even seems to make her hornier. She happily exposes herself to everyone,
             even letting perfect strangers fondle her as much as they want."

        $ girl.naked = True
        $ girl.refresh_pictures()

    elif act == "service":
        if pic.has_tag("oral"):
            "You force your dick into her mouth, going as deep as possible until she gags."

        elif pic.has_tag("handjob"):
            "You force her to use her hands to rub your dick."

        elif pic.has_tag("titjob"):
            "You force your dick between her soft tits, moving back and forth."

        elif pic.has_tag("mast"):
            "You force her to masturbate in front of you."

        else:
            "You use her body to pleasure yourself."

    elif act == "sex":
        "Forcing yourself on her, you push your dick hard into her tight pussy."

    elif act == "anal":
        "Disregarding her plea, your brutally force your cock into her tight asshole."

    elif act == "fetish":
        "Taking out a crop from your toolbag, you start spanking her hard with it."

    elif act == "bisexual":
        "You tell Sill to fuck her with a strap-on XXL dildo."

    elif act == "group":
        if brothel.security > 0:
            "You ask a security guard to join you and fuck [girl.name]. He complies with a dumb grin on his face."
        else:
            "You send Sill to fetch a vagrant. He's only too eager to join you to fuck [girl.name]."

    if act != "naked":
        $ girl.add_log("raped")

        call dialogue(girl, "slave raped") from _call_dialogue_214

        if reluctance > 100:
            "She is horrified by this brutal rape and she cries all the tears in her body, pleading for mercy."

        elif reluctance > 50:
            "She cries and begs you to stop. You ignore her, focusing your attention on her violated body."

        elif reluctance > 0:
            "She cries silent tears as you force her to do your bidding, bearing the shame and pain until you're finished."

        elif reluctance > -50:
            "As you make her pay for her misdeeds, you notice that her cries and moans are not entirely in pain."

        elif reluctance > -75:
            "Although she's making a show of complaining, it is clear she is getting off being brutally raped. She moans erotically with every movement."

        else:
            "Even though you are supposed to be punishing her, she screams with pleasure with each of your assaults, enjoying every bit of it with perverse satisfaction.
             Maybe that wasn't quite what you had in mind."

    if act == "service":
        if pic.has_tag("oral"):
            $ text1 = rand_choice(("Eventually, you blow a load of cum into her throat, sending her into a fit of coughing.",
                "You suddenly withdraw your dick from her mouth, shooting a load of cum onto her face and hair."))
            "[text1]"

        elif pic.has_tags(("handjob", "titjob")):
            $ text1 = rand_choice(("You decide to use her sexy, soft tits to finish yourself off. You blow your load all over her tits and face.",
                                   "You make her jerk you off until you blow your load. Her hands are covered with your thick cum."))

        elif pic.has_tag("mast"):
            "She has to keep masturbating while you watch and jerk off. Eventually, you bring your cock up to her and blow your load right in her face."

        else:
            "You blow a thick load all over her, then force her to lick your dick clean."

    elif act == "sex":
        "After pounding her pussy furiously for some time, you suddenly blow a big load right into her cunt."

    elif act == "anal":
        "You pound her butt so hard that she can barely breathe. After brutally raping her ass for a few minutes, you reach your limit, shooting a load of hot cum deep inside her asshole."

    elif act == "fetish":
        "You keep hitting her until she's got bright red marks all over her back, ass, and legs."

    elif act == "bisexual":
        "You make Sill fuck her harder and harder with the dildo until she's drooling from the pounding she gets."

    elif act == "group":
        "You rape her pussy and ass, while the other rams his dick down her throat until she chokes."

    if not free_training:
        hide screen show_event
        $ renpy.show_screen("show_img", brothel.get_bedroom_pic(config.screen_width, config.screen_height), _layer = "master")
        show screen girls(MC.girls)
        $ tt = show_tt("top_right")
        with fade

    if not girl.personality_unlock[act]:

        $ pos_reaction, neg_reaction = girl.test_weakness(act, unlock=True)

        if pos_reaction and neg_reaction:
            $ renpy.say("", __("你注意到 ") + girl.name + __(" 在") + __(long_act_description[act]) + __("期间感到愉悦和反感。她似乎对此有矛盾的感觉。"))
        elif pos_reaction:
            $ renpy.say("", __("尽管她在哭泣，你注意到 ") + girl.name + __(" 似乎喜欢 ") + __(long_act_description[act]) + __("。也许你应该进一步探索这个问题。"))
        elif neg_reaction:
            $ renpy.say("", __("你注意到 ") + girl.name + __(" 似乎非常讨厌 ") + __(long_act_description[act]) + __(" 。也许你可以利用这个信息对付她。"))

    return


## 6. MISC

label slave_master_bedroom_add(girl):
    if brothel.master_bedroom.level >= 1 and brothel.master_bedroom.can_have_girl() and girl not in brothel.master_bedroom.girls:
        you "Go to my room. You shall sleep there from now on."

        if girl.love > girl.fear and girl.love > 75:
            call dialogue(girl, "slave send to master bedroom love +") from _call_dialogue_215
        elif girl.love > girl.fear and girl.love > 25:
            call dialogue(girl, "slave send to master bedroom love") from _call_dialogue_216
        elif girl.love > girl.fear:
            call dialogue(girl, "slave send to master bedroom love -") from _call_dialogue_217
        elif girl.fear > 75:
            call dialogue(girl, "slave send to master bedroom fear +") from _call_dialogue_218
        elif girl.fear > 25:
            call dialogue(girl, "slave send to master bedroom fear") from _call_dialogue_219
        else:
            call dialogue(girl, "slave send to master bedroom fear -") from _call_dialogue_220

        $ brothel.master_bedroom.add_girl(girl)
        "[girl.fullname] has joined the master bedroom."

    python:
        try:
            inter.canceled = True
        except:
            pass
    return

label slave_master_bedroom_remove(girl):
    if girl in brothel.master_bedroom.girls:
        you "Go back to your bedroom now. I am done with you."

        if girl.love > girl.fear and girl.love > 75:
            call dialogue(girl, "slave leave master bedroom love +") from _call_dialogue_221
        elif girl.love > girl.fear and girl.love > 25:
            call dialogue(girl, "slave leave master bedroom love") from _call_dialogue_222
        elif girl.love > girl.fear:
            call dialogue(girl, "slave leave master bedroom love -") from _call_dialogue_223
        elif girl.fear > 75:
            call dialogue(girl, "slave leave master bedroom fear +") from _call_dialogue_224
        elif girl.fear > 25:
            call dialogue(girl, "slave leave master bedroom fear") from _call_dialogue_225
        else:
            call dialogue(girl, "slave leave master bedroom fear -") from _call_dialogue_226

        $ brothel.master_bedroom.remove_girl(girl)
        "[girl.fullname] has left the master bedroom."

    python:
        try:
            inter.canceled = True
        except:
            pass
    return

label slave_clothing_naked(girl):
    you "From now on, I want you to be naked at all times."

    call dialogue(girl, "slave toggle naked on") from _call_dialogue_227

    play sound s_equip_dress
    $ girl.naked = True
    $ girl.refresh_pictures()
    $ test_achievement("naked")

    $ inter.canceled = True
    return

label slave_clothing_dressed(girl):
    you "Put your clothes on. You've exposed your body for long enough."

    call dialogue(girl, "slave toggle naked off") from _call_dialogue_228

    play sound s_equip_dress
    $ girl.naked = False
    $ girl.refresh_pictures()

    $ inter.canceled = True
    return

label slave_forbid_cust_events(girl):
    you "Listen, I don't want you to fool around with customers unless I say so. Got it?"

    call dialogue(girl, "slave toggle customer sex off") from _call_dialogue_256

    $ girl.flags["forbid customer sex"] = True
    $ inter.canceled = True

    return

label slave_allow_cust_events(girl):
    you "Alright, forget what I said earlier about the customers. Just do your best to please them, okay?"

    call dialogue(girl, "slave toggle customer sex on") from _call_dialogue_257

    $ girl.flags["forbid customer sex"] = False
    $ inter.canceled = True

    return

label slave_custom_option(girl):

    python:
        custom_option_label = girl.init_dict["background story/interact_prompt"][1]

        try:
            custom_cost = girl.init_dict["background story/interact_prompt"][2]
        except:
            custom_cost = 0

#    scene black
    call hide_everything() from _call_hide_everything_4
    with fade

    if renpy.has_label(custom_option_label):  # Problem: Game will still crash if the label doesn't allow for the girl argument
        call expression custom_option_label pass (girl=girl) from _call_expression_2
    else:
        "System" "Label: {color=[c_red]}[custom_option_label]{/color} doesn't exist (Custom girl: {color=[c_red]}[girl.path]/_BK.ini{/color})."

    call hide_everything() from _call_hide_everything_5

    $ inter.canceled = True
    return


label interaction_cheat_menu(girl):
    menu:
        "改变好感度":
            $ girl.love = float(renpy.input(girl.name + "'s love points (between +/-100):", default = girl.love))

        "改变恐惧值":
            $ girl.fear = float(renpy.input(girl.name + "'s fear points (between +/-100):", default = girl.fear))

        "改变情绪值":
            $ girl.mood = float(renpy.input(girl.name + "'s mood points (between +/-100):", default = girl.mood))

        "重置互动次数":
            $ girl.reset_interactions()

    $ inter.canceled = True

    return

label interaction_cheat_love(girl):
    $ girl.love = int(renpy.input("Love value:"))
    if girl.love > 90:
        $ girl.MC_relationship_level = 5
    elif girl.love > 75:
        $ girl.MC_relationship_level = 4
    elif girl.love > 50:
        $ girl.MC_relationship_level = 3
    elif girl.love > 25:
        $ girl.MC_relationship_level = 1
    python:
        try:
            inter.canceled = True
        except:
            pass
    return

label interaction_cheat_girl(girl):
    $ girl.reset_interactions()
    python:
        try:
            inter.canceled = True
        except:
            pass
    return

label interaction_cheat_MC(girl):
    $ MC.reset_interactions()
    python:
        try:
            inter.canceled = True
        except:
            pass
    return

label interaction_cheat_personality(girl):
    $ always_show_personality[girl] = True
    python:
        try:
            inter.canceled = True
        except:
            pass
    return


## SLAVE STORIES ##

label slave_story1(girl):

    # A story of love and betrayal

    if girl.flags["story"] == 4:

        "You came to ask [girl.name] a question, but instead it looks like she wants to talk to you."

        you "[girl.name]... What's wrong?"

        girl.char "Can I tell you a story?"

        you "Well... Sure."

        girl.char "This happened a long time ago..."

        if girl.origin in origins:
            call dialogue(girl, "origin " + girl.origin) from _call_dialogue_229
        elif girl.init_dict["background story/origin_description"]:
            $ girl.char(girl.init_dict["background story/origin_description"])

        girl.char "Life was uneventful, until..."

        girl.char "I was barely a teenager when I met him."

        $ activity = rand_choice(("取水", "跑腿", "上学", "打扫", "和我妹妹在外面玩"))

        girl.char "I ran into him one day while I was [activity]."

        girl.char "He was older than me... Tall, handsome."

        girl.char "He was [girl.story_profession_article], but I didn't care who he was and what he did for a living. All I could see was my prince, coming to rescue me from a dull life at the [girl.story_home]."

        if girl.is_(["introvert", "idealist"]): # Introvert idealist
            girl.char "I had never met a man before, I was so shy... But he noticed me."

        elif girl.is_("lewd"): # Lewd
            girl.char "My hormones were raging at that time, I was just a dreamy, horny teenager..."

        else:
            girl.char "He lured me away from my family with promises of love and wealth, telling me I would be living like a princess in the big city..."

        girl.char "So he came to see me every day at the [girl.story_home], and I would meet him behind my family's back."

        girl.char "He would sweet-talk me for hours,  feeding me stories about how he was going to move to the noble quarters
         of Zan, and become a great man... With me at his side."

        girl.char "And I believed him, I believed every word... I thought my life was becoming magical."

        girl.char "But... Look at me now..."

        "She shakes her head, looking terribly sad. You figure it's better to leave the rest of this conversation for later."

        $ girl.flags["story"] = 10

    elif girl.flags["story"] == 10:

        if girl.rank < 2:
            return

        you "Last time, you told me about this boyfriend of yours, the [girl.story_profession]... What happened?"

        girl.char "What do you think happened? The same thing that must have happened to a thousand girls."

        girl.char "One dark night, he came to the [girl.story_home], riding a beautiful white horse. He wanted to elope with me, not stopping until we were out of reach, safe in the noble quarter of Zan."

        girl.char "He asked me to take nothing but the clothes on my back, and some cash."

        if girl.is_("idealist"): # Idealist
            girl.char "So I took my life's savings... I gave a last look to my room, the only place I had known so far..."

        elif girl.is_("materialist"): # Materialist
            girl.char "I stole a wad of cash from [girl.story_guardian], thinking I needed it more."

        girl.char "And I was on my way."

        girl.char "That night, riding behing the man I loved along the dark roads, looking up at the stars, I thought I was the luckiest girl alive..."

        girl.char "I was so wrong."

        girl.char "We made it to the rich part of Zan, all right. But we stopped by a dirty, cheap inn full of drunkards and cockroaches."

        girl.char "That's where he wanted to 'get to know me'... But I was young and shy, and I only agreed to give him head at first. That made him mad."

        girl.char "That's when... That's when he beat me up for the first time."

        "Tears run along her cheeks. She doesn't look ready to continue her story for now."

        $ girl.flags["story"] = 20

    elif girl.flags["story"] == 20:

        if girl.rank < 3:
            return

        "You find [girl.fullname] looking thoughtful, gazing at the sky through a small window."

        you "Hi, [girl.name], are you okay?"

        girl.char "..."

        girl.char "I was just thinking about my time at the inn, after I followed that asshole, the [girl.story_profession], into the center of Zan."

        girl.char "He took my cash and left me locked in the room all day, so I used to spend long hours looking at the world outside from a small window."

        if girl.is_(["introvert", "sub"]): # Introvert sub
            girl.char "I was crying my heart's out. I thought I must surely have done something to deserve it."

        elif girl.is_("dom"): # Dom
            girl.char "I was thinking of what I'd do to him if I ever got my hand on a knife. I was really mad."

        else:
            girl.char "I thought life was so unfair. What a way to repay me for loving him with all my heart..."

        girl.char "He came back at night, drunk most times. Sometimes he brought 'friends'."

        girl.char "I quickly learned that I was supposed to do anything they asked, or he would beat me savagely. They made me do so many things..."

        girl.char "After a few months, I was no longer an innocent girl."

        girl.char "For the longest time, I tried to believe that his feelings for me were real. When he was in a good mood, he called me all sorts of sweet names, promised me the world, saying this was all temporary..."

        girl.char "But when he was in his cups... He was nasty."

        if not girl.free:
            girl.char "So after six months of this treatment, I wasn't even surprised when he tied me up and took me to the slave market."

            girl.char "After he sold me to a fat merchant, he didn't even look back. I wanted him to look me in the eye at least, in spite of everything... He just stormed out, already thinking of the booze he was gonna buy with the money."

        else:
            girl.char "One day, one of his friends cracked a joke about how I wasn't gonna be around much longer. He tried to hide it from me, but I could see that he was getting nervous. It turns out he intended to sell me to a brothel."

            girl.char "That night, I stole the keys to the room, and I fled without looking back."

            girl.char "Best decision of my life... Although it's funny that eventually, I ended up here. But at least I made that choice."

        you "This is a terrible story... I'm very sorry. You must have been so hurt."

        girl.char "I was... But years have passed, and now, there is only one thing I regret..."

        if girl.is_(["extrovert", "dom"]): # Extrovert Dom
            girl.char "Not taking my revenge on his sorry ass. I wish I could have the motherfucker killed, or worse."
            $ act = "revenge"

        elif girl.is_(["lewd", "sub"]): # Lewd sub
            girl.char "I... I kind of miss him. He was forcing himself on me, beating me up, abusing me... Deep down... I liked it."
            $ act = "punishment"

        elif girl.is_(["introvert", "materialist"]): # Introvert materialist
            girl.char "Letting him get away with stealing all my belongings. He had no right. I was a fool and I let him break my heart, but it drives me mad that he got to benefit from my stupidity."
            $ act = "money"

        else:
            girl.char "Not saying goodbye to my family. I feel so sorry that I let them down."
            $ act = "family"


        $ girl.flags["story"] = 50

        call slave_story_help(girl, act) from _call_slave_story_help


    elif girl.flags["story"] == 50:

        $ girl.personality_unlock["story"] = 25

        "She talks to you again about how she was betrayed by her former lover."

        girl.char "There is only one thing I regret..."

        if girl.is_(["extrovert", "dom"]): # Extrovert Dom
            girl.char "Not taking my revenge on his sorry ass. I wish I could have the motherfucker killed, or worse."
            $ act = "revenge"

        elif girl.is_("lewd", "sub"): # Lewd sub
            girl.char "I... I kind of miss him. He was forcing himself on me, beating me up, abusing me... Deep down... I liked it."
            $ act = "punishment"

        elif girl.is_(["introvert", "materialist"]): # Introvert materialist
            girl.char "Letting him get away with stealing all my belongings. He had no right. I was a fool and I let him break my heart, but it drives me mad that he got to benefit from my stupidity."
            $ act = "money"

        else:
            girl.char "Not saying goodbye to my family. I feel so sorry that I let them down."
            $ act = "family"

        call slave_story_help(girl, act) from _call_slave_story_help_1

    return


label slave_story2(girl):

    # A story of debt and suffering

    if girl.flags["story"] == 4:

        "You find [girl.name] lost in her thoughts in her room, contemplating a small pile of gold coins on her table."

        "She doesn't notice your presence until you clear your throat."

        play sound s_surprise

        girl.char "Ah!"

        "She is startled and moves to hide the money... But she stops in her tracks when she realizes it's you."

        you "What are you doing?"

        girl.char "Oh, Master, you surprised me... This is just some leftover money from my allowance..."
        girl.char "I'm... I'm trying to save some money."

        "You told Sill to hand the girls some petty cash for their basic needs, so this is not implausible."

        menu:
            "How do you react?"

            "没事的宝贝":
                $ MC.good += 1
                $ girl.change_love(1)
                $ girl.change_fear(-2)
                you "Don't worry, dear, it's your hard-earned money. I'm not going to take it away from you."

                "She relaxes, and gives you a weak smile."

                girl.char "Thank you."

            "把钱还给你":
                $ MC.evil += 1
                $ girl.change_love(-3)
                $ girl.change_fear(2)
                you "What the hell do you think you're doing, stealing from me?"

                you "Give it back, right now, or I will tell the security guards
                     they can do whatever they want to you!"

                "Her eyes fill with tears."

                girl.char "Aww..."

                $ tip = district.rank * 25 + dice(25, district.rank)

                $ MC.gold += tip

                play sound s_gold

                "You have taken [tip] gold from her."

            "装作不知情":
                $ MC.neutral += 1

                "She shifts uneasily from side to side while you give her a steely gaze."

        you "Anyway, what do you need to save money for?"

        girl.char "..."

        girl.char "It's about my [girl.story_guardian], who is heavily in debt. I want to help repay it..."

        you "Is it what this is all about?"

        girl.char "It's a long story..."

        you "Well, let's hear it."

        girl.char "It all happened a long time ago, back in [girl.origin]..."

        if girl.origin in origins:
            call dialogue(girl, "origin " + girl.origin) from _call_dialogue_230
        elif girl.init_dict["background story/origin_description"]:
            $ girl.char(girl.init_dict["background story/origin_description"])

        girl.char "What I didn't know was that my [girl.story_guardian] had a huge gambling addiction. There was a huge debt to pay off, some very bad people involved..."

        you "I get the picture."

        girl.char "One day came a knock on the door of the [girl.story_home] where we lived. They had come to collect."

        you "..."

        sill "[girl.name]! Can you please come here!" with vpunch

        girl.char "Oh, Sill is calling me. I'll tell you the rest of the story later..."

        you "All right..."

        with fade

        $ girl.flags["story"] = 10

    elif girl.flags["story"] == 10:

        if girl.rank < 2:
            return

        "You find [girl.name] in the mood to talk."

        you "Last time, you told me about how you and your [girl.story_guardian] had to pay off a big gambling debt. Care to tell me the rest of the story?"

        girl.char "It's not a nice story... They came in the middle of the night, and they demanded to be paid in full."

        girl.char "When my [girl.story_guardian] couldn't come up with the money, they became nasty. They broke nearly everything in the [girl.story_home], and took us away as 'payment'"

        if girl.free:
            girl.char "We were treated like servants, they made us work hard and degrading jobs to repay our 'debt'..."

            girl.char "Charging us outrageous amounts for board and room, to ensure we could never pay it back."

        else:

            girl.char "The next day, we were branded slaves, and we were sold to separate owners."

            "Her voice breaks"

            girl.char "This was... This was the last time we saw each other. "

        girl.char "Eventually, I ended up in the custody of [girl.story_profession_article]. He was an evil man..."

        $ act = rand_choice(girl.neg_acts)

        girl.char "He had me... perform for him, every day... He disgusted me, but I had to do it."

        if act == "naked" or girl.has_trait("Virgin"):

            girl.char "He made me parade around the house, completely naked."

            girl.char "He was always looking at me, fondling my private parts unexpectedly, drooling like the old leech he was..."

            girl.char "He'd even jerk off in front of me, making me clean up after him... I hated him."

        elif act == "service":

            girl.char "Every morning, I had to 'clean him up', using only my tongue..."

            girl.char "He made me lick his shaft and balls, until he came into my mouth. Then he made me swallow his load of stinky cum... Said it was the perfect breakfast for me..."

        elif act == "sex":

            girl.char "He said I was his 'cum toilet', and he insisted to fuck me then and there whenever he had an urge... Which was often. Several times per day, in fact."

            girl.char "It's sad to say, but I became used to it, even spreading my legs automatically whenever he entered the room... I resented him so much."

        elif act == "anal":

            girl.char "He wanted to train me to be his little 'anal slut', because it's the only thing that could get the sick bastard off."

            girl.char "My asshole was his playground, he forced me to wear plugs and other bizarre things all day... Dildos, pearls, cat and pony tails, you name it..."

            girl.char "Eventually, my ass became so loose, he was using it as a wine holder when entertaining fancy guests... Oh, how I hated him..."

        elif act == "fetish":

            girl.char "I've seen many strange guys, but he was far crazier. He liked to inflict pain on me at every occasion."

            girl.char "He used to punish me when I didn't behave, putting clothespins on my nipples and pussy lips... Enjoying watching me suffer and scream."

            girl.char "Other times, he would just whip me ferociously for the slightest mistake... When he was done, he always had such a hard on... Then he would force me to help him 'release'... That sick fuck."


        you "Wow... I had no idea this happened to you."

        girl.char "This was before we met, I was still young and innocent... But after I met this bastard, I was innocent no longer."

        with fade

        $ girl.flags["story"] = 20


    elif girl.flags["story"] == 20:

        if girl.rank < 3:
            return

        "You have a question for [girl.name], and now seems like the right time."

        you "You told me how you were indebted to a vicious [girl.story_profession]... But you never told me how you got out of it?"

        if girl.is_("dom"):

            girl.char "Oh, that's easy... I killed the fucker."

            you "Whaaat?"

            girl.char "One day, I just couldn't take his sick games anymore... As I was going to the market to fetch some food, I stopped by an old spice dealer."

            girl.char "I slipped him a deadly dose of Shalia's weed... I told the asshole it would make his dick bigger... Oh, how he swallowed it with gusto!"

            you "How ruthless."

            girl.char "You don't know how bad he was..."

            "You feel this could be a warning."

            you "Remind me not to let you anywhere near the kitchen..."

            play sound s_laugh

            "She laughs."

            girl.char "Oh, I reckon I could get away with killing one master, but two would be suspicious!"

        else:

            girl.char "Well... He died."

            you "He died? How?"

            girl.char "Well, after a night of orgy and heavy drinking... He came back home, behaving even worse than usual."

            girl.char "I hadn't done anything to displease him, but he threatened to beat and rape me, even let his dogs at me... He was mad with rage."

            girl.char "I was crying my heart's out, and it only seemed to drive him madder... That's when he had a seizure."

            girl.char "He fell down on the floor, he could only crawl. Unable to call for help, he looked at me with glassy eyes. 'Call a doctor, you stupid bitch', he said. 'Hurry...'"

            girl.char "But I... I didn't do it."

            girl.char "I just left him there, and closed the door behind me. A maid found him the next day, stone cold dead."

            you "Wow."

            "She gets teary-eyed."

            girl.char "I don't know if what I did was right... But he made my life hell, you know..."

        if girl.free:
            girl.char "That night, I burnt the books that held my so-called accounts, and the next day, I was a free woman again... Until I met you, of course."

        else:
            girl.char "After that, I was put for sale on the Zan slave market... Which is where you found me."

        you "And here you are."

        girl.char "Here I am. But you know, there is something I regret..."

        if girl.is_(["idealist", "modest"]): # Idealist repressed
            girl.char "I wish... I wish I could repay my [girl.story_guardian]'s debt. I can't stand the idea of someone close to me suffering what I have been through..."
            $ act = "debt"

        elif girl.is_(["introvert", "materialist"]): # Introvert materialist
            girl.char "I swore to never let anything like that happen to me again. So I'm going to save money, so that I will never be at the mercy of another loan shark. "
            $ act = "saving"

        elif girl.is_(["lewd", "sub"]): # Lewd sub
            girl.char "I... I kind of miss him. He was forcing himself on me, beating me up, abusing me... Deep down... I liked it."
            $ act = "punishment"

        else:
            girl.char "I really don't care what happened to my [girl.story_guardian]. I remember all too well whose fault it was that I ended up in that situation."
            girl.char "But I kind of miss the rest of my family... I wish I could track them back."
            $ act = "family"

        $ girl.flags["story"] = 50

        call slave_story_help(girl, act) from _call_slave_story_help_2


    elif girl.flags["story"] == 50:

        $ girl.personality_unlock["story"] = 25

        girl.char "There is only one thing I regret..."

        if girl.is_(["idealist", "modest"]): # Idealist repressed
            girl.char "I wish... I wish I could repay my [girl.story_guardian]'s debt. I can't stand the idea of someone close to me suffering what I have been through..."
            $ act = "debt"

        elif girl.is_(["introvert", "materialist"]): # Introvert materialist
            girl.char "I swore to never let anything like that happen to me again. So I'm going to save money, so that I will never be at the mercy of another loan shark. "
            $ act = "saving"

        elif girl.is_(["lewd", "sub"]): # Lewd sub
            girl.char "I... I kind of miss him. He was forcing himself on me, beating me up, abusing me... Deep down... I liked it."
            $ act = "punishment"

        else:
            girl.char "I really don't care what happened to my [girl.story_guardian]. I remember all too well whose fault it was that I ended up in that situation."
            girl.char "But I kind of miss the rest of my family... I wish I could track them back."
            $ act = "family"

        call slave_story_help(girl, act) from _call_slave_story_help_3

    return


label slave_story3(girl):

    # A story of life and death

    if girl.flags["story"] == 4:

        if girl.is_("dom"):
            $ text1 = "It isn't like her."
        else:
            $ text1 = "You wonder what it is this time."

        "You find [girl.name] crying in her room. [text1]"

        you "[girl.name], what's going on?"

        girl.char "Sorry, Master... I was just thinking about an old story..."

        "She dries her tears. You wait to see if she is ready to tell you more."

        girl.char "..."

        girl.char "I never dreamt I would end up in this place and become a slave, you know..."

        girl.char "I used to live a happy life in [girl.origin], where I enjoyed [girl.hobbies[0]] most days..."

        if girl.origin in origins:
            call dialogue(girl, "origin " + girl.origin) from _call_dialogue_231
        elif girl.init_dict["background story/origin_description"]:
            $ girl.char(girl.init_dict["background story/origin_description"])

        $ text1 = article(girl.story_home)

        girl.char "We used to live in [text1] together, and I was happy."

        girl.char "But one day..."

        "Her eyes are welling with tears again. It takes a moment for her to resume her story."

        menu:
            "慢慢说":
                $ MC.good += 1
                you "Take your time. I'm here to listen."
                girl.char "Thank you."

            "说快点":
                $ MC.evil += 1
                you "Hurry up! I ain't got all day."
                girl.char "Yes, I'm sorry, Master."

            "专心听":
                $ MC.neutral += 1
                "You wait for her to continue."

        girl.char "We decided to go together on a pilgrimage to visit a famous shrine of Arios. It was said to bring good luck..."

        if MC.god == "太阳神":
            you "It's the truth."

        elif MC.god == "莎莉娅":
            you "You shouldn't need to go on a trip to feel close to your god..."

        else:
            you "Baseless superstitions..."

        girl.char "...it was anything, but lucky. Bandits were waiting in the hills, and we fell into an ambush."

        girl.char "Some people tried to fight back, and the bandits started slaughtering people left and right. My [girl.story_guardian]... killed."

        "She chokes."

        girl.char "They took the rest of us away... I didn't know what fate awaited us."

        "She seems exhausted by the conversation. You decide to let her rest, and continue her story on another day."

        $ girl.flags["story"] = 10

    elif girl.flags["story"] == 10:

        if girl.rank < 2:
            return

        "You ask [girl.name] to tell you more about her kidnapping by a raiding party. She seems ready to talk now."

        you "What happened after the bandits took you?"

        girl.char "They took the survivors away, chaining us together... They were treating us like a piece of chattel. The bodies of the fallen were left to rot, including my [girl.story_guardian]..."

        if girl.is_("dom"):
            "She looks furious."

        else:
            "She starts sobbing again."

        girl.char "Their leader was an evil man, [girl.story_profession_article]... He was always taunting us captives, and mistreating young girls like me... Sometimes he'd take a girl in his tent for the night..."
        girl.char "Those prisoners who were too weak to march further were killed on the spot, and left to rot in a ditch."

        girl.char "I was tired and famished, and I worried my turn would come next."

        girl.char "One day, we were camping out in the hills, and the men were restless. He decided to give them a show, for their entertainment..."

        girl.char "My blood froze in my veins when he told me to move forward."

        you "W... What happened? Did he rape you?"

        girl.char "Worse."
        girl.char "He told me to get naked, which I did. I had no choice."

        girl.char "After his men had ample time to leer and jeer, he told me to get on all fours."

        girl.char "Again, I had no choice."

        girl.char "That's when he brought forward his favorite horse..."

        you "Oh."

        "She blushes and lowers her eyes."

        girl.char "He told me... To pleasure his horse, in front of everyone... Or he would slit my throat."

        girl.char "I was weak... I didn't want to die..."

        you "I see..."

        "She starts crying uncontrollably. You decide to give her a break."

        $ girl.flags["story"] = 20

    elif girl.flags["story"] == 20:

        if girl.rank < 3:
            return

        "You find [girl.name] laying on her bed, looking silently at the ceiling."

        "Even though she noticed your presence, she doesn't move from her position. She starts talking absent-mindedly."

        girl.char "When I was a prisoner, in the hills, I used to look at the skies all night... I wondered if I could fly away, like a bird, and escape from this pain and madness."

        you "But you escaped, eventually. How did you do it?"

        "She looks sad."

        girl.char "After the incident with the [girl.story_profession]'s horse, everyone at the camp started bullying me."

        girl.char "Even the other captives were calling me a slut, and a horsefucker. I was the loneliest soul in the world."

        girl.char "At some point... I decided to end my life."

        you "Oh..."

        girl.char "Other captives started complaining that they didn't want to be chained with... the horsefucker. It got so bad that the bandits decided to just make me walk in front of the party all day, while they took turns mocking and abusing me."

        girl.char "One day, we were walking along a cliff overlooking a wide river. I decided this was my chance to end it."

        girl.char "Before anyone could react, I ran up to the edge and leapt down. I heard some curses and screams, the rush of wind, and then the water hit me like a wall
                   and everything went blank."

        girl.char "Before I jumped, I had decided to end my life... But when I got back to my senses, I was scared senseless.
                   I broke my bonds with a strength I didn't know I had, and I swam against the current to reach the other side."

        girl.char "I was weak... My body wouldn't let me die."

        you "Then... What happened?"

        if girl.free:
            girl.char "I escaped and met a caravan of pilgrims, on their way to Zan... They took pity on me, and brought me to the city. That's where I met you."

        else:
            girl.char "A caravan found me by the side of the road, when I was nearly starving... I had no clothes on my back, not a denar to my name... They decided to brand me a slave, and there was nothing I could do. It was destiny..."


        you "I see."

        girl.char "So many things have happened since, but I can't forget about that nightmare... Sometimes, it keeps me awake at night, reliving through the terror of it all."

        you "Is there something I can do to help?"

        girl.char "Well... I don't know if I should ask..."

        you "Try me."

        girl.char "There is one thing I would really like..."

        if girl.is_(["lewd", "sub"]):
            girl.char "You might not believe me, but... The night I... played with the horse, in front of everyone..."
            girl.char "I can't get it out of my mind. It was so intense..."
            girl.char "Whenever I think about it, I get so wet... I wish I had another chance... To do it in public with a stallion, with all eyes on me..."
            play sound s_mmh
            $ act = "horse"

        elif girl.is_(["dom", "extravert"]):
            girl.char "I have learnt that the son of a bitch who led that raiding party is in town right now... Spending the spoils of his misdeeds. If I could, I would kill him myself, but..."
            girl.char "I'm weak..."
            $ act = "revenge"

        elif girl.is_(["dom", "introvert"]):
            girl.char "It is a strange idea, but hear me out."
            girl.char "I just learnt that the son of a bitch who led that raiding party is in town right now..."
            girl.char "There's nothing he loves more in the world than this horse. And there's nothing I hate more..."
            girl.char "I want to eat that horse."
            you "Whaat?"
            girl.char "I know it's strange, but hear me out: if I eat that dumb animal, I can get over my trauma. And I can get my revenge... I just need to find someone who will get that horse for me, and turn it into a steak..."
            you "Well... That's an odd request..."
            $ act = "snack time"

        else:
            girl.char "I can't forget that they left my [girl.story_guardian] to rot in a field, together with the other dead pilgrims... I wish I could offer them a proper burial... Burn their remains in Arios fire..."

            girl.char "I have looked, and I found a map of where it all happened. But it's remote, and I have no means to go there and take care of it."
            $ act = "burial"


        $ girl.flags["story"] = 50

        call slave_story_help(girl, act) from _call_slave_story_help_4


    elif girl.flags["story"] == 50:

        $ girl.personality_unlock["story"] = 25


        if girl.is_(["lewd", "sub"]):
            girl.char "Whenever I think about it, I get so wet... I wish I had another chance... To do it in public with a stallion, with all eyes on me..."
            play sound s_mmh
            $ act = "horse"

        elif girl.is_(["dom", "extravert"]):
            girl.char "I have learnt that the son of a bitch who led that raiding party is in town right now... Spending the spoils of his misdeeds. If I could, I would kill him myself, but..."
            $ act = "revenge"

        elif girl.is_(["dom", "introvert"]):
            girl.char "I want to eat the horse that molested me."
            you "Whaat?"
            girl.char "I know it's strange, but hear me out: if I eat that dumb animal, I can get over my trauma. And I can get my revenge... I just need to find someone who will get that horse for me, and turn it into a steak..."
            $ act = "snack time"

        else:
            girl.char "I can't forget that they left my [girl.story_guardian] to rot in a field, together with the other dead pilgrims... I wish I could offer them a proper burial... Burn their remains in Arios fire..."
            $ act = "burial"

        call slave_story_help(girl, act) from _call_slave_story_help_5

    return


label slave_story4(girl):

    # A story of greed and poverty

    if girl.flags["story"] == 4:

        "You find [girl.name] standing in front of the mirror, admiring a small night dress she bought for herself with her allowance."

        play sound s_sigh

        "She buries her face in the fabric, taking in the smell of the new dress."

        "When she lifts back her face, she is startled to see your reflection in the mirror."

        play sound s_surprise

        girl.char "Oh!"

        you "Hi, [girl.name]... Am I interrupting something?"

        "She looks embarrassed."

        girl.char "No, Master..."

        you "That's a nice little dress you have there."

        if MC.get_alignment() == "good":
            you "I'm sure it looks good on you."
        elif MC.get_alignment() == "evil":
            "Your eyes narrow."
            you "It must have been costly. Living the good life, aren't you?"
        else:
            you "Well, as long as it's your money..."

        girl.char "I... I got it for cheap..."

        girl.char "I never got to enjoy this kind of luxury when I was a child..."

        you "Is that so?"

        if girl.free:
            girl.char "Yes... I was born in [girl.origin], in a very poor family..."
        else:
            girl.char "Yes, I was born a slave... My [girl.story_guardian] too..."

        if girl.origin in origins:
            call dialogue(girl, "origin " + girl.origin) from _call_dialogue_232

        elif girl.init_dict["background story/origin_description"]:
            $ girl.char(girl.init_dict["background story/origin_description"])

        girl.char "But I wasn't having much fun..."

        girl.char "We were servants. We lived in [girl.story_home_article], doing hard chores for our masters..."

        girl.char "My earliest memories are of orders being barked, and the cracking of the whip... It wasn't nice."

        you "I see."

        girl.char "I rarely caught a break, but when I did, I used to sit by the side of the main road, watching travelers come and go."

        girl.char "One day... I must have been 7 or 8... I saw a noble lady ride down the road. Most nobles ride in carriages, so I rarely had a chance to see one up close, but that lady was very brazen."

        girl.char "She had the most sublime, amazing outfit I had ever seen... Red, flamboyant, with silk ribbons and silver and gold ornaments. I was dumbstruck."

        girl.char "Ever since, I have loved pretty dresses..."

        you "Well, work hard, and you just might get your own, one day..."

        girl.char "Yes, Master [MC.name]..."

        with fade

        $ girl.flags["story"] = 10

    elif girl.flags["story"] == 10:

        if girl.rank < 2:
            return

        "You find [girl.name] at her desk, drawing something. It looks like some kind of garment. She slips it under a book as soon as she realizes your presence."

        girl.char "Oh, Master [MC.name], hello!"

        you "Hi, [girl.name]."

        girl.char  "Master, can I ask you something?"

        you "Go ahead."

        girl.char "Do you think a slave is a person?"

        "You are taken aback by this question."

        menu:
            you "Well..."

            "当然是了":
                you "Of course. Slaves are human beings, we are all the same. It's just a social institution..."
                girl.char "You really think so? I'm not so sure..."
                $ MC.good += 1

            "换个说法":
                you "Well, slaves aren't equal with free persons, of course, but they are definitely people. I mean, they have thoughts and feelings, you know... More than a vulgar animal, anyway."
                girl.char "I see..."
                $ MC.neutral += 1

            "她们也配？":
                "You burst into a cruel laugh."
                you "Slaves! Persons? Hahahaha! That's rich!"
                you "Is my horse a person? Is this table a person? Come on!"
                "[girl.name] looks down."
                $ MC.evil += 1

        if girl.free:
            $ text1 = "poor"
        else:
            $ text1 = "a slave"

        girl.char "Being born [text1], I don't believe that a slave can be equal with free persons..."

        girl.char "In this world, appearances are everything. When you're [text1], you have nothing. You are worthless."

        you "Is this what you think?"

        girl.char "I know it's true. When I was a child, I was treated with no more consideration than a cheap rag. People knew that I was nothing, anonymous and replaceable..."

        girl.char "At least until... Until I became a grown woman..."

        you "What do you mean?"

        girl.char "As I grew older, I began to notice the stares men were giving me... A few at first, then many."

        girl.char "The son of the owner of the [girl.story_home] was [girl.story_profession_article]. He was always giving me those weird looks..."

        girl.char "One day, he offered to give me some money... In exchange, I had to show him my body... Nothing more."

        girl.char "I was used to wearing torn rags anyway... I didn't care if he saw me. So I accepted, and he gave me a few coins..."

        girl.char "This was the first time I had any money to my name... I was so excited. I went to town, and bought a small bag of candy. I was so happy, I couldn't believe my luck."

        girl.char "The [girl.story_profession] kept coming, and I kept taking his money. I was saving it, a few denars at a time... I thought I could buy a beautiful dress after a while, like the noble lady I had seen..."

        play sound s_sigh

        girl.char "I had no idea how much it really cost..."

        girl.char "But the [girl.story_profession] wasn't satisfied with just seeing me naked... He wanted more, and with each day passing, he became more impatient."

        girl.char "One day... Something terrible happened..."

        you "What?"

        "She hangs her head and falls silent."

        "You hear Sill call you from another room."

        you "Well... Perhaps you can tell me later?"

        "She doesn't reply. Tears are flowing down her face. You leave and close the door softly behind you."

        $ girl.flags["story"] = 20

    elif girl.flags["story"] == 20:

        if girl.rank < 3:
            return

        "You find [girl.name] asleep at her desk. On it, you see several half-finished sketches of a sumptuous dress. She seems pretty good at drawing."

        if MC.get_alignment() == "good":
            "You gently wake her up."
        elif MC.get_alignment() == "evil":
            "You grab her by the shoulder and jerk her awake."
        else:
            "You clear your throat, causing her to wake up suddenly, with a confused look on her face."

        you "What's up, [girl.name]? Still dreaming about dresses?"

        girl.char "Oh, Master [MC.name]... I was just... Yesterday night was quite tiring, and..."

        you "Anyway. Tell me, you didn't finish your story the other day? What happened with the [girl.story_profession] you told me about?"

        girl.char "Oh, that man..."

        "She looks like she is half-awake, half-dreaming."

        "Sadness washes over her face as she continues her story."

        girl.char "One night, he told me to follow him in the stables near the [girl.story_home]. I though he only wanted to slip me a few coins in exchange for seeing my boobs or something, so I accepted..."

        girl.char "I was still very young, and it all felt like a game..."

        girl.char "But he had other intentions. He told me to strip naked, as usual, but then he started touching me."

        girl.char "I was confused, I didn't know what to say at first as he was fondling my breasts..."

        girl.char "When he lowered his hands, I started fighting him. But he didn't stop. In fact, he only seemed to become more excited as I resisted..."

        girl.char "When he took off his pants and I saw his erect dick, I realized he wasn't going to stop there. I was so scared..."

        if girl.is_("dom"):
            girl.char "I started fighting him with all my strength. I kicked him in the groin, and yelled for help."
        else:
            girl.char "I started crying, not knowing what to do... I tried running from him, but he followed me around the stables, taunting me... He was drunk and angry..."

        girl.char "That's when he took out a knife."

        girl.char "I screamed when I saw it. He started moving towards me."

        girl.char "I was so scared I nearly fainted... I closed my eyes..."

        girl.char "But then, I heard a heavy thump. When I opened my eyes, I saw my [girl.story_guardian] standing over the [girl.story_profession], a rock dripping with blood in hand."

        girl.char "The [girl.story_profession] looked like he wasn't breathing... My [girl.story_guardian] told me to get dressed and run back to the [girl.story_home], quickly. So I did..."

        girl.char "When I got to my bunk, I fell asleep immediately, exhausted and confused... It seemed like it was all a dream..."

        girl.char "When I woke up the next day, I went out to the courtyard... And I fell on my knees, oh! What a horrible scene..."

        you "What happened?"

        girl.char "They had hung my [girl.story_guardian] from a high tree... Right there in the courtyard. There was no inquiry, no trial."

        girl.char "They found the son of the owner in a coma, he said he was attacked... Someone saw my [girl.story_guardian] leaving the stables..."

        girl.char "After that, none of the slaves and servants wanted anything to do with me. I was completely lonely then, even the basest slave despised me... No one has the right to lift a hand against their betters."

        girl.char "I have learnt my lesson that day. If you're poor and defenseless, everyone will abuse you. People only care for wealth, birth, power, and sex. I had only one of those to give away... So being a sex slave was always my destiny, I guess."

        you "I see..."

        girl.char "But if I had only an ounce of wealth or power, you know what I would do?"

        you "Tell me."

        if girl.is_(["dom", "materialist"]):
            girl.char "That son of a bitch... The [girl.story_profession]... He's just a cripple now, a drooling idiot who can't even form a complete sentence..."
            girl.char "But I don't care. I want revenge on his sorry ass. I want someone to kick his fucking head in. Make him feel scared and powerless, like I once did..."
            you "Scary..."
            $ act = "revenge"

        elif girl.is_(["introvert", "idealist"]):
            girl.char "My [girl.story_guardian] died trying to protect me... No one else ever looked after me..."
            girl.char "After a few days, they threw my [girl.story_guardian] in the latrines, around the back of the [girl.story_home]... Said that's what criminals deserve..."
            girl.char "I wish I could recover the remains, and give them a proper burial..."
            $ act = "burial"

        elif girl.is_("materialist"):
            girl.char "It's a silly dream... But I would... I would buy my own dress... I have worked on designs for so long... I would be so pretty..."
            $ act = "dress"

        else:
            girl.char "I never want to feel so weak, ever again... For that, I need money... This is the only thing that can make a difference for a lowly slave like me."
            girl.char "If you would allow me to save some more money out of my allowance, I would be more secure..."
            $ act = "saving"

        $ girl.flags["story"] = 50

        call slave_story_help(girl, act) from _call_slave_story_help_6


    elif girl.flags["story"] == 50:

        $ girl.personality_unlock["story"] = 25

        girl.char "Master... If I had only an ounce of wealth or power, you know what I would do?"

        if girl.is_(["dom", "materialist"]):
            girl.char "I want someone to kick the [girl.story_profession]'s fucking head in. Make him feel scared and powerless, like I once did..."
            $ act = "revenge"

        elif girl.is_(["introvert", "idealist"]):
            girl.char "My [girl.story_guardian] died trying to protect me... No one else ever looked after me..."
            girl.char "I wish I could recover the remains, and give them a proper burial..."
            $ act = "burial"

        elif girl.is_("materialist"):
            girl.char "It's a silly dream... But I would... I would buy my own dress... I have worked on designs for so long... I would be so pretty..."
            $ act = "dress"

        else:
            girl.char "I never want to feel so weak, ever again... For that, I need money... This is the only thing that can make a difference for a lowly slave like me."
            girl.char "If you would allow me to save some more money out of my allowance, I would be more secure..."
            $ act = "saving"

        call slave_story_help(girl, act) from _call_slave_story_help_7

    return


label slave_story5(girl):

    # A story of crime and punishment

    if girl.flags["story"] == 4:

        "As you enter [girl.name]'s room, you are surprised to find it empty."

        if calendar.time - girl.log["acquired"] >= 10 and girl.ran_away_counter < 10:
            "Immediately, you start feeling worried. After all, [girl.name] tried to run away recently."

        else:
            "You don't think [girl.name] would run away on you, but you still feel worried."

        "You are about to move back to the corridor and tell Sill [girl.name] is missing, when you hear some noise coming from outside."

        play sound s_creak

        "The window creaks open, and you are surprised to see [girl.name] sneak in, oblivious to your presence."

        you "Ahem-hem."

        play sound s_surprise

        "She is shocked to see you standing there. She starts mumbling."

        girl.char "Master! I, uh, I was just going for some fresh air, I swear..."

        menu:
            "How do you react?"

            "真是这样吗?":
                $ MC.evil -= 1

                you "Is that so... Why do I feel like there's more to it?"

            "你在逗老子?":
                $ MC.good -= 1

                you "Are you fucking kidding me! You are forbidden to leave this room without permission, understand?"

        "She looks chastised."

        girl.char "I'm sorry..."

        girl.char "I haven't been able to cope with the feeling of being locked in... Not since..."

        if MC.get_alignment == "evil":
            you "Who gives a fuck about what you can or cannot cope with, slave? Will ten lashes help you 'cope'?"
            girl.char "Oh, Master, no!"
        else:
            you "Since what?"

        girl.char "I just... I was in prison before, you see. It was a terrible, terrible time."

        you "Have you, now? For what?"

        girl.char "It all started while I was living in [girl.origin] with my [girl.story_guardian]."

        if girl.origin in origins:
            call dialogue(girl, "origin " + girl.origin) from _call_dialogue_233
        elif girl.init_dict["background story/origin_description"]:
            $ girl.char(girl.init_dict["background story/origin_description"])

        girl.char "We were living together in [girl.story_home_article]... Life was easy then."

        girl.char "We weren't very well off, so we sometimes accommodated travellers for the night for a few denars... There weren't many inns in the remote neighborhood where we lived."

        girl.char "I was happy that way, but I could tell something frustrated my [girl.story_guardian]..."

        girl.char "Kept saying, 'If we had more money, we could move to a rich area, and live the high life', stuff like that..."

        girl.char "That's about the time my [girl.story_guardian] decided robbing travellers would be better money than hosting them."

        you "Oh."

        girl.char "As you can imagine, things didn't go down so well..."

        girl.char "But look at the time, we must get ready for tonight's opening... I'm sorry to keep you, Master [MC.name]."

        you "Hmm."

        $ girl.flags["story"] = 10

    elif girl.flags["story"] == 10:

        if girl.rank < 2:
            return

        "You find [girl.name] pacing around impatiently in her room."

        you "What's eating you, [girl.name]?"

        girl.char "Oh, Master [MC.name]..."

        if girl.is_("extravert"):
            girl.char "Thanks for coming... I appreciate the company."
        else:
            girl.char "I was thinking by myself... It's hard to talk sometimes..."

        girl.char "I was thinking about the story I told you last time... Of how I ended up in a jail..."

        you "Right. You haven't told me the rest of that story."

        girl.char "You remember my [girl.story_guardian] came up with a scheme to rob travellers that came to the [girl.story_home]?"

        girl.char "It was a fairly simple scheme. I was told to act as bait. I didn't want to go against my [girl.story_guardian], so I went along with it."

        girl.char "I was barely 16 or 17, and in my prime... Most men lusted after me."

        girl.char "My part was to seduce the single men that came by our guesthouse... I'd drink a few rounds with them, then offered them to skip out and take
                   a little walk by the moonlight."

        girl.char "Of course, they didn't know their drinks were spiked... Once outside, I'd lead them towards a quiet spot near the river... There, my [girl.story_guardian] would
                   ambush them, beating them up and stealing their belongings. Because they were drugged, they couldn't put up a big fight."

        girl.char "Once they were passed out, we carried them back to the [girl.story_home]. The next day, we'd tell them they got into a fight outside with some strangers, and we found them
                   lying in the gutter without their purse. Usually they'd thank us, and be on their way, not too sure about what really happened."

        girl.char "But..."

        girl.char "It all went to hell one day."

        you "What happened?"

        girl.char "One night, our guest was a mean looking man from the West, [girl.story_profession_article], I think...
                   He was scarred and ugly, I didn't want anything to do with him..."

        girl.char "I tried to talk my [girl.story_guardian] into skipping that one, but to no avail. The [girl.story_profession] carried around a heavy bag, which looked loaded with valuables, and
                   greed proved stronger."

        girl.char "So I tried my usual routine with the stranger, and it worked all right... After we had a few rounds, I started running my hand across his crotch, and whispered to him: 'follow me...'"

        girl.char "We went outside by the back door, and I took his hand and led him towards the river..."

        girl.char "We were making out, and he started fondling me under my blouse... I was disgusted to have an old, ugly man touch me in such a way, but it was also oddly exciting..."

        girl.char "As usual, my [girl.story_guardian] arrived wearing a mask and wielding a heavy sap."

        girl.char "Drugged as he was, the [girl.story_profession] couldn't see it coming. But to our surprise, he didn't fall with the first blow."

        girl.char "He stumbled away from me, and started swearing. My [girl.story_guardian] went after him, but he had some kind of fighting training.
                   His combat reflexes seemed to have kicked in."

        girl.char "In spite of the drugs running through his system, the [girl.story_profession] put up a fierce fight. My [girl.story_guardian] started to panic... And took out a knife."

        girl.char "Before I could do anything, my [girl.story_guardian] stabbed the old guy. Once, then twice, then half-a-dozen times."

        girl.char "When I ran to my [girl.story_guardian] and tried to stop this madness, it was too late. The [girl.story_profession] was stone-cold dead."

        you "Wow..."

        girl.char "Once we realised what we'd just done, we started to completely panic. We thought we had to get rid of the body first, so we dragged it to the river."

        girl.char "After we disposed of the body, my [girl.story_guardian] opened the heavy bag that the [girl.story_profession] was travelling with. It was filled with jewels."

        you "Really?"

        girl.char "My [girl.story_guardian] got so excited, forgetting instantly about we had just done... I didn't know what to think."

        girl.char "But we had no time to celebrate, anyway... Because as we were contemplating the spoils of our crime, a guard patrol showed up."

        you "Oh..."

        "[girl.name] looks restless and tired."

        girl.char "I will tell you the rest later... It's a painful story to me."

        you "I see."

        $ girl.flags["story"] = 20

    elif girl.flags["story"] == 20:

        if girl.rank < 3:
            return

        "You find [girl.name] by the window, contemplating the streets outside."

        girl.char "Hi, Master [MC.name]..."

        you "Hi, [girl.name]... You're not thinking of sneaking out on me again, are you?"

        girl.char "N... No..."

        girl.char "I was in prison for 13 months..."

        you "For killing the [girl.story_profession] you told me about?"

        girl.char "For being an accessory to the crime..."

        you "The guard patrol arrested you and your [girl.story_guardian]?"

        girl.char "Oh... They did worse than that."

        girl.char "When the patrol arrived, we were busy counting the jewels, my [girl.story_guardian] was still covered with the [girl.story_profession]'s blood..."

        you "It must have been hard to explain..."

        girl.char "Yes. We made up some stories, but the guards wouldn't have any of it. That's when my [girl.story_guardian] offered to strike them a deal."

        girl.char "We'd give them half the jewels if they'd let us go. I mean, wealthy people get let off the hook by the guard all the time like that..."

        girl.char "But the patrol sergeant stepped forward. A fat man, with a thin mustache... I still remember his evil, greedy smile..."

        girl.char "'Why settle for half, when we could just take everything?'"

        girl.char "We begged him, eventually we even told him to take all the jewels and let us be... But he just laughed it off, and his men took us away."

        girl.char "A few days later, after a summary trial, they hung my [girl.story_guardian] from the gallows of the nearby guard tower..."

        girl.char "I was only found an accessory to the crime, so I was jailed instead. 'Ten years', the judge said. My heart sank..."

        girl.char "In the following months, I had ample time to regret my crime... The tower was a terrible and filthy place."

        girl.char "I was one of the few female prisoners, and the guards enjoyed torturing us... Making us do degrading things just to get bread and water,
                   doing 'cavity'searches under flimsy excuses..."

        girl.char "The worst was the guard sergeant. He had taken a shine to me after arresting us... So whenever he came by the tower, he made it a point to visit my cell."

        girl.char "There... He did things to me."

        you "Things?"

        girl.char "He was a sadistic bastard. His favorite thing was to put a knife to my face while I was chained to the wall, and tell me he'd slash my pretty face if I didn't do as he said..."

        girl.char "Then, he'd take out his cock, and fuck my throat ruthlessly. I couldn't do anything but let him do it..."

        if girl.is_("sub"):
            girl.char "I felt completely helpless, like I was an object, devoid of free will... I just went along with the feeling..."
        else:
            girl.char "I hated it with every fiber of my body. I wanted to bite his fucking dick off, but I was too scared..."

        girl.char "When he was done, he usually came all over my food. Then he told me that I wouldn't have anything else to eat for a week..."

        girl.char "Shamefully, I had to eat that food, I was starving... I can't get that awful taste out of my mouth."

        you "That's terrible... How did you finally escape?"

        if girl.free:
            girl.char "It was blind luck, you see."

            you "Was it?"

            girl.char "At some point, the jail became overcrowded at the guard tower, so they decided to move the least dangerous prisoners out to the prison quarter in Zan."

            girl.char "I had heard terrible thing about that place, so I resolved to escape if I could."

            girl.char "One night as we were camping on the way to Zan, I managed to seduce a rookie guard during his night shift.
                       I told him I would be very nice to him, and he untied me so we could go somewhere private..."

            girl.char "I took him around the tents and started blowing him in the dark. He was enjoying it so much, he didn't notice I was taking his dagger from his belt."

            you "Did you... Kill him?"

            girl.char "No... The last thing I needed was a bunch of angry guards running after me..."

            girl.char "I just held the dagger to his dick, and told him not to make a sound. The poor lad was scared to death."

            girl.char "I tied him up and stuffed his mouth with my panties, which I thought was a nice gesture. Then I ran away, as fast as I could."

            girl.char "The taste of freedom, after a year locked in a dark cell... The cool night air rushing under my dress as I ran, caressing my naked pussy... It's such an undescribable feeling."

            girl.char "Then I got to Zan, and I met you... You know the rest."

            you "Yes..."

            girl.char "Now that I am a slave, I am not free, of course... But I know that at least, now that I am just property,
                       I will never be judged and jailed again. This is a wonderful feeling."

        else:
            girl.char "Well, technically, I didn't."

            girl.char "Eventually, the jail became overcrowded. The guard captain, feeling tight on funds, decided to sell a few prisoners as slaves, killing
                       two dragons with one stone."

            "You remember that in most of Xeros, prisoners can be turned into slaves with little to no say if their offense is considered grave enough."

            girl.char "Because I was young and attractive, I was a prime choice to be sold as a sex slave... That's how, eventually, I ended up on Zan's slave market... Where you found me."

            girl.char "Fortunately, the evil fat sergeant wasn't there when the captain took his decision... I'm sure he would have found a way to keep me there."

            girl.char "He could even... have bought me..."

            "A chill goes down her spine at this thought."

        you "I see."

        girl.char "So, all in all, I traded one captivity for another... But I'm much better here, than in this cruel and horrible place."

        girl.char "But you know, I still have regrets... Like..."

        you "What?"

        if girl.is_("dom", "lewd"):
            girl.char "The fucking guard sergeant. I heard he quit the guard and set up shop here, in Zan, enjoying the money from the jewels he stole. I can't forget the nightmare he put me through. I want someone to make
                       his life a nightmare..."
            $ act = "revenge"

        elif girl.is_(["dom", "materialist"]):
            girl.char "The fucking guard sergeant. He's been enjoying the money from the jewels he stole from us, I'm sure, and I heard he took up business and joined the
                       Zan merchant's guild... The thought of that sucker rolling in gold over the death of my [girl.story_guardian] is driving me crazy..."
            $ act = "money"

        elif girl.is_(["lewd", "sub"]):
            girl.char "I... I kind of miss that stupid guard sergeant. He was forcing himself on me, abusing me, fucking my throat... But deep down... You know... I loved it."
            girl.char "I can still feel the taste of cum in my mouth, hmmm..."
            play sound s_mmmh
            $ act = "punishment"

        else:
            girl.char "That poor guy... The [girl.story_profession]."
            you "Oh."
            girl.char "So many things happened, but you know... Eventually, we got what we deserved... But he was the victim. At least I think so, anyway."
            "She gets teary-eyed."
            girl.char "We threw his body in the river, didn't even give him a proper burial... He might have had a family; they will never know what happened to him...
                       I feel so guilty."
            you "But what can you do about it?"
            girl.char "I can't make up for what I did, I know... But at least I could set up an altar for him at the Cathedra. Maybe then, Arios could shine his Light on him,
                        and on his loved ones..."
            $ act = "praying"

        $ girl.flags["story"] = 50

        call slave_story_help(girl, act) from _call_slave_story_help_8


    elif girl.flags["story"] == 50:

        $ girl.personality_unlock["story"] = 25

        girl.char "But you know, I still have regrets... Like..."

        if girl.is_(["dom", "lewd"]):
            girl.char "The fucking guard sergeant. I heard he quit the guard and set up shop here, in Zan, enjoying the money from the jewels he stole. I can't forget the nightmare he put me through. I want someone to make
                       his life a nightmare..."
            $ act = "revenge"

        elif girl.is_(["dom", "materialist"]):
            girl.char "The fucking guard sergeant. He's been enjoying the money from the jewels he stole from us, I'm sure, and I heard he took up business and joined the
                       Zan merchant's guild... The thought of that sucker rolling in gold over the death of my [girl.story_guardian] is driving me crazy..."
            $ act = "money"

        elif girl.is_(["lewd", "sub"]):
            girl.char "I... I kind of miss that stupid guard sergeant. He was forcing himself on me, abusing me, fucking my throat... But deep down... You know... I loved it."
            girl.char "I can still feel the taste of cum in my mouth, hmmm..."
            play sound s_mmmh
            $ act = "punishment"

        else:
            girl.char "That poor guy... The [girl.story_profession]."
            girl.char "I can't make up for what I did, I know... But at least I could set up an altar for him at the Cathedra. Maybe then, Arios could shine his Light on him,
                        and on his loved ones..."
            $ act = "praying"

        call slave_story_help(girl, act) from _call_slave_story_help_9

    return



label slave_story6(girl):

    # A story of glory and consequence

    if girl.flags["story"] == 4:
        "You enter [girl.name]'s room, and are surprised to find her extremely agitated."

        girl.char "Ah! Master [MC.name]! I'm glad you're here!"

        you "What is it, [girl.name]?"

        girl.char "This! This is a disaster!"

        "She points to a plate of meat and vegetables standing on her night table. It appears she barely touched it."

        girl.char "Sill's cooking is getting worse and worse! This is the third day in a row we get peas... I hate peas!"

        menu:
            "What do you do?"
            "袒护希露":
                $ MC.good += 1
                $ NPC_sill.love += 1

                you "Come on, Sill is doing her best. I don't see you helping out much in the kitchen."
                girl.char "Me? Help out? I'm not some kind of servant!"
                "You start losing patience."
                you "Sill has many things to take care of, you should cut her a little slack. This is not a 5-star inn, all right?"
                girl.char "Aw..."

            "让她发泄":
                $ MC.neutral += 1

                you "..."
                girl.char "And look at this meat! Overcooked, again! I don't know how many times I told her I hate this..."
                you "..."
                girl.char "I mean, come on! Can't that girl do anything right? I can't stand it for much longer..."
                you "Are you quite finished?"
                girl.char "Well... Not really, but..."

            "冲她咆哮":
                $ MC.evil += 1
                $ girl.fear += 1

                you "[girl.name], listen carefully."
                girl.char "Yes?"
                you "I DON'T GIVE A DAMN ABOUT YOUR PETTY PROBLEMS!"
                "You yell in her ear at the top of your lungs. She is startled and just stands there, wordless."
                you "YOU'RE A SLAVE, STOP ACTING OUT LIKE A SPOILED BRAT! OR I'LL WHIP YOUR ASS!!!"
                girl.char "M... Ma... Master..."
                you "UNDERSTOOD???"
                girl.char "Y... Yes..."



        "She falls silent for a moment."

        girl.char "It's just... I'm not used to this kind of treatment..."
        "You scoff."
        you "Oh, really? Perhaps you are used to having a fleet of white-gloved servants looking after your every need?"
        girl.char "Well... Kind of..."
        you "Seriously? When did sex slaves become so fancy?"
        girl.char "I wasn't always a slave, you know... In fact, I come from an old and well-respected family..."
        you "You do?"
        girl.char "Yes... My father was a nobleman in [girl.origin], renowned across Xeros and influential at court..."
        you "Really... You didn't look that well-off when I met you..."
        girl.char "It's true... But my family was very unlucky. My current predicament is the result of a succession of terrible unfortunate events..."
        girl.char "I was raised like a princess... I never wanted for anything..."


        if girl.origin in origins:
            call dialogue(girl, "origin " + girl.origin) from _call_dialogue_234
        elif girl.init_dict["background story/origin_description"]:
            $ girl.char(girl.init_dict["background story/origin_description"])

        girl.char "I had a large estate, and many friends, slaves and servants... I was especially close to my [girl.story_guardian]."
        girl.char "My parents kept me sheltered from the outside world and its vices... I never knew suffering, hunger, or fear... I was spoiled and happy..."
        you "Quite a long way from being a sex slave in [district.name]..."
        "She looks sad."
        girl.char "It was... I had four cats of the purest race, all of them with fancy names and their personal set of clothes... I fed them catfood from the court's chef himself, much better than any of the dreadful cooking that Sill inflicts upon us now..."
        you "You were spoiled all right... What happened?"

        girl.char "As I was growing up, living a happy and innocent life, little did I know that my [girl.story_guardian] had been scheming behind my back..."
        you "Scheming?"
        girl.char "I was barely out of my childhood years... Only 14 or 15... When one day, an old gentleman came to the family estate. He was in his 60s, but to me, he looked older than the Golgoth invasions..."
        girl.char "We entertained the old gentleman all evening, and I couldn't help but notice that he was giving me weird looks."
        girl.char "My [girl.story_guardian] treated him with the utmost care, however."
        girl.char "I was deeply incurious at that time, so after he left, I came back to my usual games, ordering around my slaves and servants..."
        girl.char "But the old gentleman returned several times after that. Every time, I was forced to be courteous, and exchange pleasantries with him. I didn't know what was going on, but I went along with it..."
        girl.char "Then, after one of his visits, my [girl.story_guardian] came to see me, beaming, and informed me that a date had been decided... For our wedding."
        girl.char "I was to marry the old man."
        you "Uh oh..."
        play sound s_sigh
        "She sighs heavily."
        girl.char "I will tell you the rest of this story later, Master... I have to try and eat some of that dreadful grub, then get ready for the opening tonight."


        $ girl.flags["story"] = 10

    elif girl.flags["story"] == 10:

        if girl.rank < 2:
            return

        "You find [girl.name] looking with horror at one of her dresses. Upon closer inspection, you spot a small tear in the fabric."

        girl.char "Oh, Master [MC.name]! This is a disaster! Look at this!"
        you "There appears to be a small tear in the dress..."
        girl.char "A small tear! This is unwearable! A customer did this... Aw, now I just have to throw away this worthless rag!!!"
        you "Well... You could always sew it..."
        "Her eyes widen with shock and horror."
        girl.char "M, me... Sew???"
        girl.char "I... No... I won't..."
        "She bursts out."
        girl.char "I'm not a vulgar street girl! Sewing? With my own hands??? No way!!!"
        you "Wow, calm down..."
        girl.char "Back in the days, I had an army of low-born slovens who would do this for me..."
        you "Ah, yes, in the golden days of your noble youth..."
        girl.char "And I still would, if not for that awful wedding my [girl.story_guardian] arranged for me..."
        you "What happened?"
        girl.char "Well... I didn't want to marry an old slob... But he had a big name, and he was loaded, so my [girl.story_guardian] wouldn't have any of my objections."
        girl.char "'Marrying for love is only good for farmhands', everyone told me. A lady had to marry up."
        girl.char "Plus, he was an old guy... Soon he'd kick the bucket, and I would be a powerful, rich and happy widow. Or so they said."
        girl.char "So, the preparations went on, and the next month, I was lawfully married to the geezer."
        you "You just went along with it?"
        girl.char "I had no experience of the world, I had almost never ventured outside my estate... Disobeying my [girl.story_guardian] wasn't even an option."
        you "I see."

        girl.char "The wedding was a sumptuous affair... Gallant people from all over Xeros came to see us wed, we held a feast for 3000 people... They had an orchestra playing, with crossbows and all, it was all good fun..."
        girl.char "It is during the wedding night that things started to go wrong."

        girl.char "I had heard some servants chat about the things that husbands and wives do in the bedroom, but it was never really clear to me what they meant, and I didn't really pay attention."
        girl.char "That night in our chamber, I was very surprised and confused when I saw my new husband naked for the first time, and he ordered me to get undressed."
        girl.char "His old member was limp, but after he sniffed a certain powder, it started growing long and hard. I was shocked to see the size of it as he started advancing towards me."
        girl.char "He started talking to me with an authoritarian tone, a long way from the affable front he was putting up earlier with my family. Then, he ordered me to lay on the bed and spread my legs."

        if girl.has_trait("Virgin"):
            girl.char "Everything was so new and confusing to me, that I didn't even realize something was strange when instead of fucking me from the front, he pushed his dick inside my tight anus."
        else:
            girl.char "It was my first time, and I was completely unprepared, and very dry. He didn't care at all, and proceeded to fuck me with his abnormally hard cock."

        girl.char "I yelled with pain, and I started crying. He didn't care at all."
        girl.char "Fortunately, it didn't last long. Soon, he came inside with a heavy grunt, and fell asleep right there on top of me."
        girl.char "The bastard had a heavy frame, so I couldn't even move out from under him. I spent the night in pain, sobbing, wondering what the future would bring."

        girl.char "But the future only brought me more of the same..."
        girl.char "Every night, the old lecher would take his secret spice, then fuck me mercilessly until he came inside."

        if girl.has_trait("Virgin"):
            girl.char "For some reason, he would only fuck my ass. It seemed to be the only thing he really cared about."
        else:
            girl.char "At least, he was shooting blanks... I was terrified he would make me pregnant with his disgusting child..."

        girl.char "I pleaded for him to stop, or do things differently, but he just ignored me. He didn't care that I hated it and that he was hurting me, or perhaps that turned him on."

        girl.char "I became really sad and withdrawn, and all the luxuries that I once enjoyed so much seemed meaningless compared to the hell my life had become."

        girl.char "I tried to explain my situation to my [girl.story_guardian] when I was visiting, but no one showed me any understanding..."

        girl.char "When I got too direct, people just told me that ladies shouldn't talk about things like that, and I was sent back to my lonely existence with my hated husband..."

        girl.char "Only one person showed me any real sympathy at my husband's court."

        girl.char "He was [girl.story_profession_article]... I often saw him in the courtyard, smiling shyly at me. He was young and handsome... Very much like you, Master. *blush*"
        girl.char "We got to talk about this and that when I went out for a walk in the castle's park. He was charming and witty, and it was obvious he liked me..."
        girl.char "I was desperate for some human warmth and companionship, and I told him some foolish things that got his mind racing..."
        girl.char "That was... a terrible mistake."
        you "How so?"
        "She falls silent, reflecting upon a painful memory."
        girl.char "..."
        girl.char "I will tell you next time, Master [MC.name]... For now, I need some rest."

        $ girl.flags["story"] = 20

    elif girl.flags["story"] == 20:

        if girl.rank < 3:
            return

        "You find [girl.name] looking at a painting showing a picturesque landscape. She looks lost in her thoughts."

        girl.char "I found this at the market the other day... It reminds me of the landscape I could see from my bedroom, when I was still living in a castle with my old, lecherous husband."
        you "It looks nice..."
        girl.char "I look at this, and all it brings is painful and sad memories. Give me the noise and mess of Zan's streets over that any day..."
        you "You didn't tell me the end of your story... About that handsome [girl.story_profession]?"
        girl.char "Well..."
        girl.char "We were both young and impressionable... So naturally, we came up with a dumb plot straight out of a cheap romantic novel..."
        girl.char "We were to elope together to a remote [girl.story_home], where we'd live a happy and simple life far away from my abusive husband... That kind of shit."
        you "Why do I sense it didn't go well..."
        girl.char "But my husband, the old wretch, he wasn't born yesterday. He had spies around court, people I trusted, and it didn't escape anyone that the young [girl.story_profession] was courting me..."
        girl.char "The old bastard was the mean and jealous type... He was biding his time."
        girl.char "So the night we escaped, I met the [girl.story_profession] at the [girl.story_home], like we had planned."
        girl.char "We were so overjoyed to be together, we forgot all caution... Instead of running like we should have, we just kissed passionately, and things started to heat up... Before long, we ended up with our clothes strewn out around the floor."
        girl.char "And that's when armed men bashed the door in."
        girl.char "My lover tried to escape through a window, but they caught him with a bolt between the shoulders..."
        girl.char "I was so shocked that I couldn't move... The men grabbed me, and drove me back to the castle naked and shivering."

        girl.char "The whole court was up, standing in a circle under the torchlights."
        girl.char "My husband was there, wearing his fancy robes. His voice was shaking with rage as he addressed his court."
        girl.char "He said that I was a filthy slut who had defiled his noble bed, unworthy of the name of wife..."
        girl.char "... and that he was repudiating me then and there, as was his right, thereby appropriating all my titles and belongings."
        girl.char "Further, he said, I had to be punished for my betrayal."

        if girl.free:
            girl.char "That's when he asked his private guards to move forward."
            girl.char "He ordered them... to fuck me, in front of everyone."
            if girl.has_trait("Virgin"):
                girl.char "Each in turn, the guards fucked my ass while I was made to stand on all fours. People around leered and jeered, calling me all kinds of names until morning came."
            else:
                girl.char "The guards ganged up on me, and violated my every hole. I had no choice but to endure it, until morning came."

            girl.char "The next day, I was left naked in the middle of the courtyard, lying in a pool of... Disgusting."
            girl.char "Somehow, I found the strength to get up and leave that horrible place."
            girl.char "I managed to find some clothes and make my way to my family's estate..."
            girl.char "There, I met my [girl.story_guardian]... Stone-faced and full of anger."
            girl.char "I was told that I brought a terrible shame on the family, and that I had proven unworthy of my birthname. People spit on me, and I was thrown out of the property like a lowly beggar."
            girl.char "They told me if I ever returned, they'd loose the hounds on me."
            girl.char "I wandered for many months, taking small jobs to make it, and relying on the kindness... or lust... of strangers."
            girl.char "Eventually, I made it to Zan. That's where I met you."
        else:
            girl.char "Two court magicians stepped forward, carrying an item I knew too well: a magical brand. I gasped."
            girl.char "My husband ordered me branded a slave, and promptly sold me as a sex slave to a passing merchant."
            girl.char "Eventually, I ended up on the slave market in Zan... That's where you found me."

        you "Wow... That's a pretty sad story."

        "Tears creep into her eyes."

        girl.char "It was awful! Just awful, you know..."
        girl.char "If only... I wish..."
        you "What?"

        # praying, arson, pet, inheritance

        if girl.is_(["modest", "idealist"]):
            girl.char "My poor lover... The [girl.story_profession]."
            girl.char "We were both young and stupid... But he paid the ultimate price. We didn't get to say goodbye..."
            girl.char "I wish I could honor his memory."
            $ act = "praying"

        elif girl.is_(["dom", "lewd"]):
            girl.char "All of this, it happened because... Because of my fucking [girl.story_guardian]... That's who!"
            girl.char "Everyone I grew up with turned their backs on me... I want them all to burn in hell!"
            girl.char "In fact, that family estate... My birthright... I want it burnt to the ground..."
            you "What? Really?"
            girl.char "I wish it would burn! BURN!!!"
            $ act = "arson"

        elif girl.is_("materialist"):
            girl.char "Recently, I found out that the old fart, my loving husband, has finally kicked the bucket."
            girl.char "I seethe at the thought of all the land and money he's going to leave behind... It should have been mine, by right! I paid for it with my body!"
            you "Well..."
            girl.char "It's a long shot, since I'm a slave now, and I've been repudiated... But with a good lawyer... Perhaps I could get some kind of inheritance?"
            girl.char "After all, it's not like he had any legitimate heir, is it?"
            $ act = "inheritance"

        else:
            girl.char "I miss my innocent days... I miss my cats..."
            $ act = "pet"

        $ girl.flags["story"] = 50

        call slave_story_help(girl, act) from _call_slave_story_help_10


    elif girl.flags["story"] == 50:

        $ girl.personality_unlock["story"] = 25

        girl.char "If only... I wish..."

        if girl.is_(["modest", "idealist"]):
            girl.char "My poor lover... The [girl.story_profession]."
            girl.char "I wish I could honor his memory."
            $ act = "praying"

        elif girl.is_(["dom", "lewd"]):
            girl.char "Everyone I grew up with turned their backs on me... I want them all to burn in hell!"
            girl.char "In fact, that family estate... My birthright... I want it burnt to the ground..."
            $ act = "arson"

        elif girl.is_("materialist"):
            girl.char "Recently, I found out that the old fart, my loving husband, has finally kicked the bucket."
            girl.char "It's a long shot, since I'm a slave now, and I've been repudiated... But with a good lawyer... Perhaps I could get some kind of inheritance?"
            $ act = "inheritance"

        else:
            girl.char "I miss my innocent days... I miss my cats..."
            $ act = "pet"

        call slave_story_help(girl, act) from _call_slave_story_help_11

    return

label slave_story7(girl):

    # A story of devotion and sacrifice

    if girl.flags["story"] == 4:

        "You enter [girl.name]'s room as she is busy cleaning up."

        girl.char "Oh, hi, Master. I moved into this room only recently, you know, so I decided to do some clean up,
                   trying to make it feel like home, you know?"

        "The place looks tidy and inviting now, freshly cut flowers are disposed artfully in a vase by the window."

        "You take a look at the dust bin, and are surprised to see some kind of emblem sticking out. You recognize it to be a symbol of Arios."

        "Looking back at the wall above [girl.name]'s bed, you notice a blank space and the holes left by nails, where the symbol used to hang."

        if MC.god == "太阳神":
            you "What kind of blasphemy is that??? Did you throw away your Arios sign?"
            play sound s_surprise
            girl.char "Oh, I'm sorry, Master, I meant no disrespect!"
        else:
            you "Not a big fan of Arios, are you?"

        girl.char "The sign, it wasn't mine, you see... It was here when I arrived."

        girl.char "But it would have been too strange to keep it, because I don't worship Arios, you see..."

        you "Oh, really? That's quite rare in this city... Who do you worship then?"

        girl.char "Well... I don't... I mean, I used to worship a god... We call Him the Dweller."

        you "The Dweller? This sounds familiar..."

        girl.char "The Dweller is an old god, He does not care if He has few or many followers... But he is powerful. He's said to keep many secrets..."

        girl.char "He wields the power of nature. Plants and beasts are His allies, some say His children. He has command over them if he so chooses."

        you "That sounds familiar... Wait a minute, isn't that the god of the elves?"

        girl.char "He's one of many gods known to the fairy people, yes... But they aren't the only one who worship Him. I received His teaching from my [girl.story_guardian],
                   who traded with the elves for a time, before the war..."

        you "I can see why it isn't a very popular god in those parts anymore."

        girl.char "Believe it or not, when I was growing up in [girl.origin], it was perfectly normal to worship the Dweller. There was no holy war then..."

        if girl.origin in origins:
            call dialogue(girl, "origin " + girl.origin) from _call_dialogue_235
        elif girl.init_dict["background story/origin_description"]:
            $ girl.char(girl.init_dict["background story/origin_description"])

        girl.char "No matter what happened, I had faith in the Dweller, and in my [girl.story_guardian], to protect me against all harm."

        girl.char "How things have changed..."

        you "What do you mean?"

        girl.char "Our life was quiet and devoid of luxury, it's true. We lived simply in an abandoned [girl.story_home]."

        girl.char "But in all those years, I never dreamt I would end up a sex slave, a toy to satisfy the urges of strangers..."

        menu:
            you "Well..."
            "我很抱歉事情变成这样":
                $ MC.good += 1
                you "I'm sorry it's come to this. I wish things could have turned out differently..."
                girl.char "Oh, don't patronize me. You have decided to start this business from your own free will, haven't you?"
                you "Well..."
                girl.char "Well, I have decided to become a sex slave of my own free will too. It's a choice I made. I cannot regret it."

            "人生不总是一帆风顺的":
                $ MC.neutral += 1
                you "Well, life is hard. We don't get to decide everything that happens to us."
                you "What's left is for us to make the best of the hand we're dealt."
                girl.char "You're right, Master [MC.name]... That's why I chose to become a slave."

            "别自顾自的怨天尤人了":
                $ MC.evil += 1
                you "Oh, boo-fucking-hoo..."
                you "If you were good enough for anything other than being a cum dump, then you wouldn't have ended up in this joint!"
                you "Stop wallowing in your self-pity. It disgusts me."
                girl.char "..."
                girl.char "I know the choices I made, and I know why I ended up here... I'm not complaining."
                you "Oh, really?"
                girl.char "Yes. I chose to become a slave. It's my calling."

        you "You chose to become a sex slave?"

        girl.char "Yes."

        if girl.free:
            you "You mean... When I offered you a job in town?"
            girl.char "No. I chose my path long before that."

        you "How so?"

        girl.char "It's a long story. Allow me to tell you later, Master [MC.name]. For now, I have to finish what I started..."

        $ girl.flags["story"] = 10

    elif girl.flags["story"] == 10:

        if girl.rank < 2:
            return

        "You find [girl.name] in her neatly arranged room, sitting on her bed in a meditating posture."

        "She acknowledges your presence without opening her eyes. You sit on the bed next to her."

        you "Is this a bad time?"

        girl.char "No, Master. I am only trying to reconnect with a natural state of peace, and free myself of the painful memories of past events."

        you "Like what?"

        girl.char "Well, it's the story I promised to tell you..."

        girl.char "Back then in [girl.origin], all peaceful religions were welcome. No one talked about burning heretics or torturing elven spies..."

        girl.char "Me and my [girl.story_guardian] were living our religion openly, although it was uncommon to worship the Dweller for people in these parts."

        girl.char "Things went sour after the war started in the Holy Lands."

        girl.char "At first, we didn't see what any of this had to do with us... And it didn't."

        girl.char "We were confident in our community, in our neighbours... Even after the elven traders were run out of town, even after they started mugging and lynching non-humans in the marketplace..."

        girl.char "We didn't see that as our problem. But I did notice some of the gossiping..."

        girl.char "People grumbled that we were involved in sorcery, or spying for the enemy... Some knew about the altar to the Dweller in our house, and said
                   we were devil-worshippers. They were more ignorant than mean, I suppose, but they were plenty of both."

        girl.char "My [girl.story_guardian] started worrying, and talking about moving away... But I wouldn't have any of it."

        girl.char "The [girl.story_home] is our home, I said. We belong here."

        girl.char "How wrong I was..."

        you "What happened?"

        girl.char "First they came for the elves, and I said nothing... Of course later, they came for us."

        girl.char "One night, while we were sound asleep, someone threw a lit torch through our window."

        girl.char "We barely made it out alive, but our [girl.story_home] was burnt down."

        girl.char "Hungry and homeless, we tried to ask some of the neighbors for help... But no one would open their door to us."

        girl.char "Some told us to go to hell, that our home burning was divine punishment... People I had known all my life..."

        girl.char "A few days later, me and my [girl.story_guardian] were taken in by the guards, for 'vagrancy'."

        girl.char "They locked us in for days... We used to joke that at least, now we had food and shelter."

        girl.char "I only understood that something was wrong days later, when we heard commotion outside."

        girl.char "A group of Templars had arrived in town... Among them was a priest of Arios with a stern face and white and scarlet robes."

        girl.char "When I saw the villagers start building a pyre, I became very afraid."

        you "Uh-oh..."

        "[girl.name] is white as a sheet now. Her eyes are wide open. She doesn't seem ready to continue her story just now."

        you "Take some rest. We'll finish our discussion later."

        girl.char "Thank you, Master."

        $ girl.flags["story"] = 20

    elif girl.flags["story"] == 20:

        if girl.rank < 3:
            return

        "You find [girl.name] in an impossible position, seemingly in the middle of a complex meditation practice."

        "She notices your presence and slowly assumes a more relaxed position, gesturing for you to sit close to her."

        you "Wow, with such flexibility, no wonder you're popular with customers..."

        play sound s_laugh

        "She laughs."

        girl.char "That's nothing! You'd be surprised what the elves can do... I mean, if there were any left."

        you "Yes... By the way, you didn't finish your story the other day... About how you got mixed up with the Arios church and their Templars?"

        girl.char "That's right..."

        girl.char "I didn't know what the Templars were at that time, you see. And I certainly had never heard anything about the newly founded Arios inquisition..."

        girl.char "That man I saw that night, leading the Templars, he was one of them."

        girl.char "The war was going badly, just like now, so the Arios church was badly in need of a scapegoat. They decided to crack down on so-called heretics and spies..."

        girl.char "After the Templars arrived, me and my [girl.story_guardian] were taken separately for 'questioning'..."

        girl.char "They tortured us. Physically, sexually, I was abused for many days. Even now, I cannot count, I cannot remember. It must not have been that long, but I
                   feel like it went on forever."

        girl.char "I remember myself, gagged and chained in an impossible position, with my legs spread out and a large dildo in my ass, waiting for them to come back and hurt me..."

        girl.char "At first, they didn't even bother to ask me any question. Grim-faced Templars would come and go and torture me. Some were naturally sadistic, others
                   were acting like it was just a job to them. I hated them all."

        girl.char "After many days, the inquisitor came to visit. I was allowed some food and water, and they even untied me. He told me some nonsense about Arios's mercy..."

        girl.char "He came back several times, and slowly I understood him. He wanted me to denounce myself as a heretic, and renounce my false god publicly. Only then, he said, would my life be spared."

        girl.char "The torturing and interrogating went on, and I was slowly losing my mind. Nothing these people said made any sense to me, but I only wanted this madness to stop."

        you "Of course."

        girl.char "So eventually, I gave in. I told the inquisitor that I would repent."

        girl.char "He had a look of triumph in his eyes, and he told me that I would have to confess on a stage, in front of the whole village. I didn't care, so I just said yes."

        girl.char "But when the day came..."

        you "What?"

        girl.char "Early one morning, I was taken to the village plaza near the jailhouse. The pyre was still there. I could see it had been used recently."

        girl.char "The smell of death and charred wood was in the air..."

        girl.char "In the middle of the plaza also stood my [girl.story_guardian]. It was the first time we were together again after many days of suffering."

        girl.char "I got a knot in my stomach, I knew something wasn't right."

        girl.char "A crowd gathered, and the inquisitor started his speech. He went on about enemies of the one true religion..."

        girl.char "Then he said that we were here that day to witness the burning of evil, and possibly redemption... It was deeply unsettling. I didn't understand why anything had to burn."

        girl.char "As he kept talking, it dawned on me. My [girl.story_guardian] hadn't renounced our god. They were going to burn my [girl.story_guardian] at the stake."

        you "Oh..."

        girl.char "But it got worse. The inquisitor turned to me, and asked me with a threatening voice if I renounced my false god and accepted to rejoin with the one true faith."

        girl.char "I was terribly scared, so I said yes."

        girl.char "He then asked me if I would prove my loyalty to Arios, by publicly accusing the ones responsible for my 'indoctrination'..."

        girl.char "And then I understood what he meant. He wanted me to denounce my own [girl.story_guardian]."

        girl.char "I was crying and confused, and lost, so lost... I turned to my [girl.story_guardian], desperate for help..."

        girl.char "And then I saw it. I saw my [girl.story_guardian] looking at me, nodding."

        girl.char "And I understood. My [girl.story_guardian] had already chosen their fate. I had to save myself."

        you "..."

        girl.char "So I did everything they asked of me. I renounced my god, I accused my [girl.story_guardian] of corruption and evil-doing, I confessed to everything
                   they wanted me to."

        girl.char "The inquisitor was pleased. Later that morning, they burnt my [girl.story_guardian] alive."

        girl.char "I was let go. People were oddly nice to me. Some even called me 'sister'."

        girl.char "I hated them all. I wanted to spit in their stupid faces, or stick a knife in their innards. But I was afraid. So I just smiled."

        girl.char "After I was freed, I reflected on what I had done. I had betrayed my god, as well as the people who were closest to me."

        girl.char "I decided I was a horrible, horrible person, unworthy of being treated like a human being. I decided that no fate would be too harsh
                   for a wretched monster such as I."

        you "You're too harsh."

        girl.char "Maybe, maybe not. Anyway. I lacked the bravery to take my own life, so I just resolved to keep on living, and take on my share of suffering."

        girl.char "That's why eventually, when I ended up a sex slave, I didn't complain or fight it. It is a fate I amply deserve..."

        you "Wow."

        if MC.god == "太阳神":
            you "I am so appalled that you suffered so much at the hands of Arios worshippers... Please know that we are not all like that."

            girl.char "I know, Master. Some Arios people showed me kindness, including you, in your way..."

            girl.char "I suffered at the hands of men, not gods."

        girl.char "I have given up all my hopes and dreams. But you know what I truly regret?"

        you "No, what?"

        # burial, curse, punishment, altar


        if girl.is_("lewd", "sub"):
            girl.char "You know what the strangest thing is... For days, I was treated worse than dirt by the Templars, they trashed my mind and body..."
            girl.char "And yet, it is like at that time, I reached some kind of unique spiritual plenitude. Like I was exactly in the place I needed to be."
            girl.char "The more I think about it, the more it makes sense... I'm a bitch and a terrible person. I need to be punished..."
            $ act = "punishment"

        elif girl.is_("very modest"):
            girl.char "I have betrayed my god... I am godless now..."
            girl.char "And yet, I miss Him... I miss a reassuring presence in my life, some greater power to shelter me from harm..."
            girl.char "No offense here, Master [MC.name]."
            girl.char "I have been thinking of setting up an altar here. I will need some ingredients from the forest. Something to keep me occupied..."
            girl.char "Maybe if I succeed, my god will forgive me, and turn his light back on me?"
            $ act = "altar"

        elif girl.is_(["idealist", "modest"]):
            girl.char "My poor [girl.story_guardian] remained faithful to the Dweller, up to the very last moment... A death unworthy of my [girl.story_guardian]'s life."
            girl.char "When you're branded a heretic, they throw the charred bones in a ditch... I saw it happen."
            girl.char "This is not the way of the Dweller. This is not how it's done."
            girl.char "I wish I could give my [girl.story_guardian] a real burial... Set our souls at peace."
            $ act = "burial"

        else:
            girl.char "I'm done with useless gods, relics and superstitions."
            girl.char "We were true believers. We followed every teaching. And look where it got us?"
            girl.char "I never want to be caught in any of this religious mumbo-jumbo any more."
            if not MC.god:
                you "I'm with you, sister."
            girl.char "In fact, I want to tell the whole world about this. I refuse to be an accomplice in some kind of collective brainwashing."
            girl.char "I don't want to pretend to believe in anything. Not with you, not with the girls, not with the customers..."
            $ act = "godless"

        $ girl.flags["story"] = 50

        call slave_story_help(girl, act) from _call_slave_story_help_12


    elif girl.flags["story"] == 50:

        $ girl.personality_unlock["story"] = 25

        girl.char "I have given up all my hopes and dreams. But you know what I truly regret?"
        if girl.is_(["lewd", "sub"]):
            girl.char "The more I think about it, the more it makes sense... I'm a bitch and a terrible person. I need to be punished..."
            $ act = "punishment"

        elif girl.is_("very modest"):
            girl.char "I have been thinking of setting up an altar here. I will need some ingredients from the forest. Something to keep me occupied..."
            girl.char "Maybe if I succeed, my god will forgive me, and turn his light back on me?"
            $ act = "altar"

        elif girl.is_(["idealist", "modest"]):
            girl.char "I wish I could give my [girl.story_guardian] a real burial... Set our souls at peace."
            $ act = "burial"

        else:
            girl.char "I'm done with useless gods, relics and superstitions. Look what good it did me."
            girl.char "I don't want to pretend to believe in anything. Not with you, not with the girls, not with the customers..."
            $ act = "godless"

        call slave_story_help(girl, act) from _call_slave_story_help_13

    return

label slave_story8(girl):

    # A story of magic and curses

    if girl.flags["story"] == 4:

        "You go to [girl.name]'s room, and find her busy scribbling strange symbols on her wall with a piece of chalk."

        girl.char "And the fire runes should flow from East to West..."

        if MC.playerclass == "法师":
            "You recognize crude runes among the various symbols she is drawing. It is amateurishly done, however."
        else:
            "It seems like some magical gibberish."

        you "Ahem, what exactly do you think you're doing?"

        girl.char "Oh, Master... Don't break my concentration... I'm almost done."

        "She uses her piece of chalk to enclose the symbols in a big circle, then joins the signs together in the rough shape of a pentagram."

        girl.char "There! This place is now secure."

        "You give her a skeptical look."

        you "What are you trying to protect yourself against, anyway? I don't think there are many ghosts in brothels, anyway. They usually prefer quieter places."

        girl.char "It's not the dead I'm afraid of... It's the living."

        you "Oh, really? So you think a chalk drawing will affect them?"

        girl.char "It will affect some of their powers, yes. You see..."

        "She lowers her voice."

        girl.char "{i}She{/i} is after me. I know it."

        you "Who is '{i}she{/i}'?"

        "She doesn't answer you directly. Instead, she stands looking at her drawing with a satisfied look."

        girl.char "Do you know a lot about witches, Master?"

        if MC.playerclass == "法师":
            you "Well, I studied alongside a few in Karkyr... They're usually pretty haughty and ill-tempered."

            you "But they're wild in bed, so there's that."

            girl.char "Ill-tempered! Exactly."

        else:
            you "Well, they live alone in the forest, and they eat little children..."

            "She laughs."

            girl.char "Oh, no, Master! Those are just legends."

            girl.char "Witches are usually pretty normal-acting. They can be anyone... A shopkeeper, a noblewoman, a nurse..."

            girl.char "But they jealously keep their powers from strangers."

        girl.char "I'm not talking about the swamp-dwelling, crystal-ball wielding, wart-nosed variety... Those are just for show."

        girl.char "No self-respecting witch would be caught acting like that... Except maybe those obsessed with decorum and traditions."

        girl.char "I'm talking about the powerful and secret ones, the ones who live among us..."

        you "And what is it that you are talking about, exactly?"

        girl.char "I'm talking about... {w}a {i}curse{/i}."

        play sound s_thunder
        with flash

        you "Wow!" with vpunch

        you "Wait. Can you do that again?"

        "She raises her voice."

        girl.char "I'm talking about..."

        play sound s_thunder
        with doubleflash

        girl.char "A {i}cu-u-u-urse{/i}." with vpunch

        play sound s_creak

        you "Spooky...."

        you "Are you saying someone cursed you?"

        girl.char "Not just anyone... I've been cursed by a powerful and vengeful witch... You want to know how that happened?"

        you "As a matter of fact, I do. It sounds like a fun story!"

        "She gives you an angry look."

        girl.char "It's not fun at all!!!"

        girl.char "It all started a while ago, when I was living in [girl.story_home_article] in [girl.origin]..."

        if girl.origin in origins:
            call dialogue(girl, "origin " + girl.origin) from _call_dialogue_236
        elif girl.init_dict["background story/origin_description"]:
            $ girl.char(girl.init_dict["background story/origin_description"])

        girl.char "Ever since I was a little girl, I was always interested in magic. My [girl.story_guardian] really disapproved of it."

        girl.char "Said all magic had ever brought Xeros was chaos and destruction... But I didn't see it that way."

        girl.char "Magic creates chaos, it's true, but chaos breeds change... And change is good, right?"

        menu:
            you "Well..."

            "改革可能会带来不好的影响":
                $ MC.good += 1
                you "People can get hurt by change. You must be careful what you wish for."
                girl.char "..."
                girl.char "Perhaps I should have heeded that advice... But it's a little late now."

            "改革也会带来很多新的机遇":
                $ MC.neutral += 1
                you "Some change is simply inevitable. Adaptable people can come out on top..."
                girl.char "Exactly."

            "乱成一团那才叫有趣，对吧":
                $ MC.evil += 1
                you "Creative destruction... I like that."
                girl.char "You see my point, right?"

        girl.char "Anyway. As I grew older, I became increasingly bored staying at home and listening to my [girl.story_guardian]'s lectures..."

        girl.char "I thought I had it in me to become a skilled magician... So I decided to seek a teacher."

        you "A teacher, uh?"

        girl.char "To be continued..."

        you "What? Seriously?"

        girl.char "Why, yes, Master [MC.name]... I can't tell you the whole story all at once, now, can I? It wouldn't be fun..."

        play sound s_thunder
        with flash

        $ girl.flags["story"] = 10

    elif girl.flags["story"] == 10:

        if girl.rank < 2:
            return

        "Approaching [girl.name]'s room, you suddenly hear an explosion."

        play sound s_fire
        with vpunch

        you "What the..."

        "You run to the scene."

        you "[girl.name]???"

        "[girl.name]'s room is a mess of broken furniture. There is a hole in the ground and shattered glass on the floor, and the walls have been blackened by the explosion."

        "[girl.name] is standing in the room with her eyebrows smoking and her clothes torn and burnt."

        if MC.get_alignment() == "good":
            you "[girl.name]! Poor darling! Are you all right?"
        elif MC.get_alignment() == "neutral":
            you "What the hell happened here..."
        elif MC.get_alignment() == "evil":
            you "What the... You're gonna pay for the damage from your allowance, you hear me!"

        girl.char "I just... I mean..."

        "She looks a little disoriented."

        girl.char "I guess the saltpeter should have come last... Darn."

        if MC.god:
            you "What in the name of [MC.god] were you trying to do?"
        else:
            you "What in the bloody world were you trying to do?"

        girl.char "Well, it's about the curse, you see... I found that book of magic recipes, and I thought..."

        "You see a charred tome on the ground, its pages curling as they finish burning to a crisp."

        girl.char "So much for that idea..."

        you "Hey, [girl.name]. I don't want you endangering yourself and everyone here with your crazy experiments, you hear?"

        "[girl.name] looks defeated."

        girl.char "Yes, Master..."

        you "What is that curse all about, anyway?"

        girl.char "Well... I told you about my time in [girl.origin], when I was looking for a magic teacher..."

        you "Yes. Did you find one?"

        girl.char "Eventually, I did..."

        girl.char "At first, I tried to join the local magic guild. But I had no formal training, no connections... They just laughed at me."

        girl.char "But I was stubborn, so every day I went back, and begged... And every day, I was kicked out."

        girl.char "The magic guild was in the noble quarter, situated right across from a large and beautiful mansion."

        girl.char "One day, as I was evicted from the guild once more, I saw a beautiful young lady standing in the street."

        girl.char "She was dressed in a fine and elegant dress. She held out her white-gloved hand for me, and helped me get up."

        girl.char "'Do you really want to learn magic this bad, darling?', she said in a sweet, musical voice."

        girl.char "Yes, I said. 'Are you ready to do anything for it?', she said. Again, I said yes."

        girl.char "So she invited me to her home, which was none other than the mansion across the street."

        girl.char "There, she gave me my own quarters, and she told me that from now on, I would be her apprentice."

        girl.char "I didn't know what that meant, but I gladly accepted."

        you "Hmm... Who was she?"

        girl.char "She was what she seemed to be. A lady at court, from an old and respected family..."

        girl.char "But she was also something else. A powerful sorceress, hiding terrible family secrets and wielding dark powers..."

        girl.char "She was talking about events from ages ago as if they were yesterday. She talked about powerful demons as if
                   they were acquaintances. She scared away all animals, except cats..."

        girl.char "And she had appetites..."

        you "Appetites?"

        girl.char "Of a sexual nature, mostly. Man, woman or beast, she didn't care... But she also had other carnal appetites. I helped her sate them..."

        "She shivers."

        you "As her apprentice?"

        girl.char "As her apprentice, her lover, her would-be daughter, I'm not really sure..."

        girl.char "I put my heart into learning everything I could from her. I was an eager student, if maybe not the most-gifted one..."

        "You take a look at the charred mess that is her room and wonder if that isn't an understatement."

        girl.char "The Lady was patient with me, and I learnt a lot in a short time... But I still felt like it was going too slow."

        girl.char "'When am I going to talk to an actual demon?', I'd say, or 'When can I conjure up my own storm?'. 'Can I make all men fall in love with me?', and so on."

        girl.char "I think my whining was trying the Lady's patience, but she didn't show it. Instead, she gave me more tasks and chores, in the hope of making me more obedient."

        girl.char "While I eagerly accepted any new responsibilities, I was annoyed that they all seemed to be beneath me."

        girl.char "Eventually, I became paranoid, thinking the Lady was deliberately hiding knowledge from me... Perhaps she was afraid I would become too powerful and threaten her?"

        "Looking around you once again, you think that's pretty unlikely. Maybe she was more worried about preserving her living-room."

        girl.char "One day, as I was cleaning the shelves in her chambers, I saw an old manuscript I had never noticed before. It was bound with strange leather, and closed with a magic lock."

        girl.char "Even now, I don't know why, but I felt compelled to take that book. It's like it was calling to me."

        girl.char "I wasn't nearly good enough at spellpicking to open that lock, but I knew my mistress's habits... She always wore a silver key around her neck, except when taking milk baths..."

        girl.char "So one day, as I finished preparing the bath for her, I decided to 'borrow' that key."

        you "Uh-oh."

        girl.char "I thought it was a brilliant idea."

        you "Oh dear."

        "You smell the acrid smell of burning cloth."

        girl.char "Well... Let me tell you the rest of the story later, Master [MC.name]. I think your pants are beginning to catch fire."

        you "Aah!" with vpunch

        $ girl.flags["story"] = 20

    elif girl.flags["story"] == 20:

        if girl.rank < 3:
            return

        "You find [girl.name] naked on her bed with her arms and legs spread and tied to the bed poles, and a big red candle dripping hot wax in the middle of a pentagram drawn on her belly."

        play sound s_scream

        girl.char "Aaaah!!! It hurts!!!"

        "You quickly rush to her help, take away the candle and untie her. She sobs as she wraps herself into a bed cover."

        you "Who... Who did this to you? Is it some kind of sick customer???"

        girl.char "Uh? Ah! No, no, I did it myself..."

        you "You??? But... When... How..."

        you "WHY???"

        girl.char "Oh, I read somewhere that this ritual of purification could help drive away curses... But it hurts like hell!"

        you "What the... Are you crazy? How did you even manage to tie yourself up???"

        girl.char "Anyway. I don't think it worked. I'm still cursed, am I not?"

        you "Well... I don't know... How can I tell?"

        girl.char "You can't... It's my own burden..."

        you "What is this curse, anyway?"

        girl.char "A terrible and ancient curse... I shiver just to think about it."

        you "Tell me."

        girl.char "You remember, I told you I was working for a powerful witch in [girl.origin]."

        you "Yes."

        girl.char "One day, I decided to steal the key she was carrying with her at all times... The key to an old manuscript that I thought held incredible power..."

        you "Yes..."

        girl.char "So as my mistress was busy taking her bath, I opened the secret tome. The book flew open to a random page, and I began to read in earnest."

        girl.char "It was some kind of chant, a call to a powerful being from beyond the planes..."

        you "Tell me you didn't read it aloud..."

        girl.char "Oh, but I did! Runes are hard to read, you know, so it helps if I say them aloud..."

        you "Damn..."

        girl.char "And guess what? Soon as I was finished reading, there was a big rumble... A tear appeared in time and space..."

        you "Damn."

        girl.char "And a demon appeared before me!"

        you "Just like that?"

        girl.char "Yeah! I was so excited..."

        you "Duh."

        girl.char "I was expecting some kind of hulk with horns and cool wings..."

        girl.char "But instead, I only saw a gooey blob wiggling flacid tentacles around."

        girl.char "So it was a gooey demon, but a demon nonetheless! I started peppering him with questions."

        girl.char "But it didn't answer me... Instead, it just grabbed me with its slimy tentacles, and started ripping my dress!"

        you "How... Unexpected..."

        girl.char "It seemed it had only one thing in mind: fuck my brains out!"

        if girl.has_trait("Virgin"):
            girl.char "I don't know why though, but it was only interested in one thing: my ass..."
        else:
            girl.char "Oozy tentacles started poking my every hole!"

        girl.char "At first, it was only small tendrils... It felt ticklish. But soon, larger, thicker tentacles started making their way inside me."

        girl.char "They were spurting some gooey, sticky liquid non-stop... What a weird sensation... Mmmh..."

        play sound s_sigh

        girl.char "Anyway. All this ruckus had alerted my mistress that something was happening. So she rushed out of her bath, naked as the day she was born."

        girl.char "As soon as she showed up, however, the demon started buzzing. He lost all interest in me, and soon a hundred thick tentacles were darting towards my mistress."

        girl.char "Before she had any chance to react or cast a spell, she was being fucked senseless by tentacles thick as a tree trunk..."

        girl.char "I could only watch with horror and fascination as the demon kept pouring his gooey fluid into her every hole... The whole room was slippery with his fluids..."

        girl.char "Eventually, the demon paused somewhat, taking a tentacle out of her mouth for an instant."

        girl.char "She took advantage of it, and yelled at me: 'Quick! Take my crystal scepter, and cast a banish spell'!"

        girl.char "So I grabbed her scepter, and I pointed it at the demon... It was moving a lot, fucking the Lady with renewed fury..."

        girl.char "But I kept it in my sights, and I recited the words to the banish spell. At least I think it was a banish spell. I couldn't remember for sure."

        girl.char "Then, a deep ray of light started shining from the scepter... It was a success!"

        girl.char "I pointed it at the demon's head... But then, I slipped into a pool of the demon's bodily fluids."

        girl.char "I fell down, and the light ray started focusing on my mistress instead. Then the crystal scepter hit the ground, and it burst into a thousand fragments."

        girl.char "Both the demon and my mistress were engulfed in a pool of energy. I saw a tear open in space and time, and swallow them both. I was terrified, and heard my mistress's final words..."

        girl.char "'Curse you, you clumsy bitch!'"

        "She falls silent, and gives you a look of despair."

        you "..."

        girl.char "..."

        you "And...?"

        girl.char "And?"

        you "I mean... What happened?"

        girl.char "What happened! I was cursed!"

        you "Cursed?"

        girl.char "Yes! With her words, she cursed me! 'Curse you, you clumsy bitch...'"

        girl.char "Ever since, I have been clumsy! I mean, more than usual! And she said 'bitch'... Look at me now! I'm a sex slave!"

        you "..."

        you "You really believe that is a curse?"

        girl.char "Of course! Do you think I'd be like this if I was in my normal state?"

        you "Well..."

        girl.char "Oh, Master, I'm so afraid... Please help me!"

        you "Help you how?"

        # lift curse, learn to live with it, visit family, make a show

        if girl.is_(["modest", "sub"]):
            girl.char "I am cursed, and I must pay for my sins... But I was once pure, I had a family."
            girl.char "I left my [girl.story_guardian] a long time ago, without saying anything... Everyone must be worried sick about me."
            girl.char "I wish I could at least see them, and ask for their forgiveness..."
            $ act = "family"

        elif girl.is_("very lewd"):
            girl.char "I have been through a lot since that incident with the demon... I have met many men..."
            girl.char "But you know..."
            girl.char "I never felt... I never found such bliss, than when I was being raped by that demon... I wish this could happen again..."
            $ act = "demon"

        else:
            girl.char "Please, help me remove this curse! It is making my life a living hell!"
            $ act = "curse"

        $ girl.flags["story"] = 50

        call slave_story_help(girl, act) from _call_slave_story_help_14


    elif girl.flags["story"] == 50:

        $ girl.personality_unlock["story"] = 25

        girl.char "Oh, Master, I'm so afraid... Please help me!"

        # lift curse, learn to live with it, visit family, make a show

        if girl.is_(["modest", "sub"]):
            girl.char "I left my [girl.story_guardian] a long time ago, without saying anything... Everyone must be worried sick about me."
            girl.char "I wish I could at least see them, and ask for their forgiveness..."
            $ act = "family"

        elif girl.is_("very lewd"):
            girl.char "I never felt... I never found such bliss, than when I was being raped by that demon... I wish this could happen again..."
            $ act = "demon"

        else:
            girl.char "Please, help me remove this curse! It is making my life a living hell!"
            $ act = "curse"

        call slave_story_help(girl, act) from _call_slave_story_help_15

    return


label slave_story_help(girl, act):

    "You think about what she said. Perhaps there is something you could do to help her?"

    if act == "dress":
        $ dress = get_rand_item(quality = "common", item_type = IT_Dress)

    menu:
        "You think about what she said. Perhaps there is something you could do to help her?"

        "告诉她你会举行驱魔仪式 (2天)" if act == "curse" and MC.get_spirit() >= 3:

            you "Listen, if it'll put your mind at ease, I can perform a ritual on you to drive the curse away."

            girl.char "Really? You really would?"

            you "I will... Don't worry."

            "You don't tell her that the ritual is quite basic and unlikely to stop a powerful curse... She's probably not cursed anyway."

            with fade

            play sound s_spell

            you "There you go! Now just take a couple of days rest, and you'll be good as new."

            girl.char "Oh, thank you! Thank you, Master [MC.name]! You saved me..."

            you "It's nothing..."

            $ MC.evil -= 1

            $ girl.change_love(8)
            $ girl.change_fear(-5)

            "[girl.name] now likes and trusts you a lot more."

            call take_leave(girl, 2) from _call_take_leave_1


        "告诉她，她必须学会接受它(用“笨拙”的特质取代她的消极特质)" if act == "curse":

            you "Look. It isn't that bad. Being clumsy isn't the end of the world..."

            you "She could have turned you into a toad."

            girl.char "A... A toad?"

            you "Oh, yes... You'd be living in a swamp, eating flies..."

            girl.char "Ew!!!"

            you "So you see, you got off easy."

            girl.char "By the goddess... You're right, Master [MC.name]. I should count my blessings."

            girl.char "Being clumsy is not so bad... I guess I should avoid heavy machinery for a while..."

            you "Yes. You do that."

            $ old = girl.traits[2].name
            $ girl.remove_trait(girl.traits[2])
            $ girl.add_trait(clumsy_trait, forced=True, no_perks=True)

            play sound s_chimes

            "[girl.name] has lost the '[old]' trait and gained the 'Clumsy' trait."

            $ MC.good += 1
            $ girl.change_love(5)
            $ girl.change_fear(-3)

            "[girl.name] now likes and trusts you a lot more."

        "召唤一只黏糊糊的触手怪到她的房间 (1天)" if act == "demon" and MC.get_spirit() >= 5:

            you "I know the kind of creature that you speak of... I might be able to 'arrange' a private meeting with one of them."

            girl.char "Aaah! You could?!? Oh, Master, I'll be a good girl, please..."

            you "All right, all right. Take tonight off, and wait in your room. I'll send you a little surprise..."

            girl.char "Oh, thank you, Master!"

            $ pic = girl.get_pic("monster", "beast", strict = True)

            if not pic:
                $ pic = Picture(path="events/" + rand_choice(security_pics["monster rape"]))

            with fade

            play sound s_spell
            pause 0.2
            play sound2 s_roar


            "That night, [girl.fullname] has a wonderful time being fucked senseless by a disgusting monster."

            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
            with dissolve

            play sound s_screams

            girl.char "Aaaaah, aah, aaaaaaahhh!!!"

            play sound s_orgasm_fast

            hide screen show_event
            with fade

            $ girl.change_stat("libido", 10)
            $ girl.change_love(10)

            "[girl.name] now likes you a lot more. Her libido has increased."

            call take_leave(girl, 1) from _call_take_leave_2

        "花钱雇魔法公会召唤一个触手怪到她的房间 (1000金币, 1天)" if act == "demon" and MC.get_spirit() < 5:

            you "I know the kind of creature that you speak of... I might be able to 'arrange' a private meeting with one of them."

            girl.char "Aaah! You could?!? Oh, Master, I'll be a good girl, please..."

            you "All right, all right. Take tonight off, and wait in your room. I'll send you a little surprise..."

            girl.char "Oh, thank you, Master!"

            $ pic = girl.get_pic("monster", "beast", strict = True)

            if not pic:
                $ pic = Picture(path="events/" + rand_choice(security_pics["monster rape"]))

            with fade

            play sound s_gold
            $ MC.gold -= 1000

            "You pay the magician guild to organize a little play session at the brothel that night."

            play sound s_spell
            pause 0.2
            play sound2 s_roar

            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
            with dissolve

            play sound s_screams

            girl.char "Aaaaah, aah, aaaaaaahhh!!!"

            play sound s_orgasm_fast

            hide screen show_event
            with fade

            $ girl.change_stat("libido", 10)
            $ girl.change_love(8)

            "[girl.name] now likes you a lot more. Her libido has increased"


            call take_leave(girl, 1) from _call_take_leave_3


        "让她收集一些食材，搭建一个祭坛 (3天)" if act == "altar":

            you "I'll give you a few days off. This way, you can visit the forest and get what you need."

            girl.char "Really? You don't mind me setting up an altar for a god you don't believe in?"

            you "Go for it. It's your god. And who knows, perhaps some good luck will rub off on us?"

            you "Keep the customers away from it though. We don't want the Templars coming here, do we?"

            girl.char "Oh, of course..."

            $ MC.good += 1
            $ girl.change_love(8)
            $ girl.change_fear(-5)


            "[girl.name] now likes and trusts you a lot more."

            call take_leave(girl, 3) from _call_take_leave_4

        "采购一些食材，搭建一个祭坛 (1天, 650金币)" if act == "altar":

            $ MC.gold -= 650
            play sound s_gold

            you "Here is some money to get the ingredients you need from the market. You can get started right away."

            girl.char "Really? You don't mind me setting up an altar for a god you don't believe in?"

            you "Go for it. It's your god. And who knows, perhaps some good luck will rub off on us?"

            you "Keep the customers away from it though. We don't want the Templars coming here, do we?"

            girl.char "Oh, of course..."

            $ MC.good += 1
            $ girl.change_love(8)
            $ girl.change_fear(-5)

            "[girl.name] now likes and trusts you a lot more."

            call take_leave(girl, 1) from _call_take_leave_5

        "让她畅所欲言(用“无神论”特质取代她的消极特质)" if act == "godless":

            you "Well, you don't have to. Feel free to tell everyone how you really feel."

            girl.char "R-really? Even to the customers? Some won't be happy, you know..."

            you "Come on, this is a brothel, not a church. If they want a sermon, let them go to the Cathedra."

            girl.char "Thank you, Master! You take a weight off my chest..."

            $ old = girl.traits[2].name
            $ girl.remove_trait(girl.traits[2])
            $ girl.add_trait(godless_trait, forced=True, no_perks=True)

            play sound s_chimes

            "[girl.name] has lost the '[old]' trait and gained the 'Godless' trait."

            $ MC.good += 1
            $ girl.change_love(5)
            $ girl.change_fear(-8)

            "[girl.name] now likes and trusts you a lot more."


        "给她买一只新宠物 (800金币)" if act == "pet":
            python:
                for it in all_items:
                    if it.name.lower() == "common pet":
                        pet = copy.deepcopy(it)
                        break

            you "You look like you are feeling lonely... What if I got you a new pet?"
            girl.char "A pet? A pet of my own??? Really?"
            you "Sure."
            girl.char "Oh, this sounds wonderful! Thank you!"

            with fade

            $ MC.gold -= 800
            play sound s_gold
            $ girl.items.append(pet)

            "[girl.fullname] has received a common pet."

            $ MC.good += 1
            $ girl.change_love(8)
            $ girl.change_fear(-5)

            "[girl.name] now likes and trusts you a lot more."

        "聘请一些律师把[girl.name]的案子移送法庭审理 (1250金币定金,未知的收益)" if act == "inheritance":
            you "It's a long shot, but why not try it? There could be good money to be made if it works."
            you "We'd have to share the money, of course..."
            girl.char "Oh, Master, of course! Thank you for taking up my case!"

            with fade

            $ MC.gold -= 1250
            play sound s_gold

            "You pay some shrewd lawyers from Zan's merchant guild to act on your and your slave's behalf."

            with fade

            if dice(4) == 4:
                $ MC.gold += 4000
                play sound s_gold
                "Thanks to their amazing legal skills and prodigious bad faith, they manage to convince a jury that [girl.name] was unfairly struck off her old husband's
                 will. You receive 4000 gold as your share of the inheritance."

            else:
                "Unfortunately, the local authorities are left unconvinced by their arguments. Still, [girl.name] is grateful to you for trying."

            $ girl.change_love(8)
            $ girl.change_fear(-5)

            "[girl.name] now likes and trusts you a lot more."

        "派几个混混放火烧了她的老宅子 (900金币)" if act == "arson":
            you "Let me talk to some people I know. We could arrange a little fire..."
            "Her eyes shine bright at the mention of fire."
            girl.char "Really??? You'd do that for me?"
            you "Why not..."
            girl.char "Yay!!!"
            "She jumps into your arms, and give you a warm kiss!"
            girl.char "Master, you're the best!"

            with fade

            $ MC.gold -= 900
            play sound s_gold

            "You paid some men to set fire to [girl.name]'s family estate. You later hear that the damage was extensive."

            $ MC.neutral += 1
            $ girl.change_love(8)
            $ girl.change_fear(-5)

            "[girl.name] now likes and trusts you a lot more."

        "在庄园的木材仓库里点起一场大火" if act == "arson" and MC.get_spirit() >= 5:
            you "Well, this could be a good time to dust off some of my old fire spells..."
            girl.char "Really??? You'd do that for me?"
            you "Why not!"
            girl.char "Yay!!!"
            "She jumps into your arms, and give you a warm kiss!"
            girl.char "Master, you're the best!"

            with fade

            play sound s_spell

            "That evening, you use a crystal ball and conjure up a fierce firestorm in the wood reserve of [girl.name]'s family estate. You and [girl.name]
             look on with fascination as the fire spreads and slowly engulfs the whole property."

            $ MC.neutral += 1
            $ girl.change_love(8)
            $ girl.change_fear(-5)

            "[girl.name] now likes and trusts you a lot more."

        "让她去为那个不幸的灵魂祈祷 (1天, 捐赠500金币)" if act == "praying":
            you "I understand how you feel."

            if MC.god == "太阳神":
                you "Arios will have mercy on this poor soul. Go to the Cathedra, pray for him, and present the priestesses with this modest gift."
            else:
                you "I don't worship Arios, but if it can give you closure, you have my blessing. Why don't you go tomorrow?"
                you "I'm sure those priestesses will want money... Here, take this."

            $ MC.gold -= 500
            play sound s_gold

            girl.char "Really? Thank you so much, Master [MC.name]!"

            $ MC.good += 1
            $ girl.change_love(5)
            $ girl.change_fear(-8)

            "[girl.name] now likes and trusts you a lot more."

            call take_leave(girl, 1) from _call_take_leave_6

        "提出增加她的零用钱(用“养尊处优”的特质取代她的消极特质)" if act == "saving":
            you "I could allow you a larger allowance..."

            girl.char "What? Really?"

            you "...but you'd have to promise to behave, and keep it to yourself. I don't want the other girls to complain that I am having favorites."

            girl.char "Understood, loud and clear! You won't hear me complain!"

            $ old = girl.traits[2].name
            $ girl.remove_trait(girl.traits[2])
            $ girl.add_trait(expensive_trait, forced=True, no_perks=True)

            play sound s_chimes

            "[girl.name] has lost the '[old]' trait and gained the 'Expensive' trait."

            $ MC.good += 1
            $ girl.change_love(5)
            $ girl.change_fear(-8)

            "[girl.name] now likes and trusts you a lot more."


        "给她买她梦寐以求的那条裙子 ([dress.price]金币)" if act == "dress":
            you "Those drawing of yours are quite detailed... I'm sure a good tailor could do wonders with these for inspiration."

            girl.char "Thank you for your kind words, Master... But I don't nearly have enough money right now..."

            you "Well, that is not a problem... It can be my gift to you."

            girl.char "What? You would? Really?"

            you "Why not. It looks like you really want that dress, and it could be useful for your work, you know..."

            girl.char "Oh, Master! You make me so happy!"

            with fade

            $ MC.gold -= dress.price
            play sound s_gold

            girl.char "Master! Look at this! It's so beautiful..."

            $ text1 = article(dress.name)
            $ girl.items.append(dress)

            play sound s_equip_dress

            "[girl.fullname] has received [text1]."

            $ MC.good += 1
            $ girl.change_love(5)
            $ girl.change_fear(-5)

            "[girl.name] now likes and trusts you a lot more."

        "让她去埋葬她的亲人吧 (2天, 1000金币)" if  act == "burial":

            you "Take a couple of security guards with you, and go bury your [girl.story_guardian]."

            girl.char "What? Really? You'd do that for me?"

            you "Well, I have to look after the needs of my slaves..."

            girl.char "Oh, thank you, Master! Thank you! I am so grateful..."

            play sound s_gold
            $ MC.gold -= 1000

            $ MC.good += 1
            $ girl.change_love(8)
            $ girl.change_fear(-5)

            "[girl.name] now likes and trusts you a lot more."

            call take_leave(girl, 2) from _call_take_leave_7

        "举办一次公开的活动 (1500金币定金,未知收益)" if act == "horse":

            you "If you really insist, I suppose I should let you have your fun... I could even turn out a profit..."

            play sound s_aaah

            girl.char "You would? Oh, Master... I feel so horny, just thinking about it..."

            $ MC.neutral += 1
            $ girl.change_love(8)
            $ girl.change_stat("libido", 10)

            "[girl.name] now likes you a lot more. Her libido has increased."

            play sound s_gold

            $ gold = dice(2500)
            $ MC.gold += gold - 1500

            if gold >= 1500:
                "You paid 1500 gold to organize the event. It generated [gold] gold in return, allowing you to break even."
            else:
                "You paid 1500 gold to organize the event. It generated [gold] gold in return, failing to turn a profit."

            $ pic = rand_choice(pony_pics)

            play sound s_orgasm_fast

            show screen show_event(Picture(pic, "events/" + pic), x=config.screen_width, y=int(config.screen_height*0.8))

            with fade

            play sound s_ahaa

            girl.char "Aaaah! Aaaahaaaa!!!"

            play sound s_spell

            $ girl.acquire_perk(pony_perk, forced=True)

            hide screen show_event
            with fade

            "[girl.name] has become a 'Pony girl'"

        "绑架一匹马?!? (750金币)" if act == "snack time":

            you "You know what, I always felt like stealing horses! There was that game, GTH..."

            girl.char "You would? Oh, thank you Master! It's perfect!"

            if story_flags["c1_path"] == "evil":
                $ text1 = "city guard"
            else:
                $ text1 = "thieves guild"

            you "I will have to pull a few strings with the [text1], but... It shouldn't be a problem."

            with fade

            $ MC.gold -= 750
            play sound s_gold

            "You paid the [text1] 750 gold to 'confiscate' the horse and turn it into a tasty meal..."

            with fade

            you "Voila! One horsesteak with ginger and turnips for Lady [girl.name]..."

            girl.char "You did it! Oh, I'm so happy..."

            $ MC.neutral += 1
            $ girl.change_love(5)
            $ girl.change_fear(-8)

            "[girl.name] now likes and trusts you a lot more."

            girl.char "Oh, it's this part..."

            "She looks a little disappointed."

            you "Say what?"

            girl.char "Oh, nothing! Haha..."

            with fade

        "帮她还清债务 (900金币)" if act == "debt":

            you "I was moved by your story. If helping you repay your debt can make you feel better, I will give you some money."

            girl.char "You would? Oh, Master [MC.name]! I... I don't know what to say!"

            you "Hush, take this and go to the bank..."

            if MC.get_alignment() == "evil":
                you "...before I change my mind."

            play sound s_gold
            $ MC.gold -= 900

            $ MC.good += 1
            $ girl.change_love(5)
            $ girl.change_fear(-8)

            girl.char "Oh, Master..."

            "[girl.name] now likes and trusts you a lot more."


        "给她几天时间去探亲 (3天)" if act == "family":

            you "It's sad that you haven't seen your family for so long. Tell you what, I'll give you 3 days off so that you can look for them. How does it sound?"

            girl.char "You... You will? Yes, that will do! Thank you, from the bottom of my heart! Oh, I miss my family so much..."

            $ MC.rand_say(("gd: 如果你高兴，我就高兴。", "ne: 现在，收拾好你的东西，免得我改变主意。", "ev: 但你可别趁机逃跑，否则我会把你剖开。"))

            girl.char "Understood... Thank you! I don't care what people say, you're a good master, you know?"

            $ MC.good += 1
            $ girl.change_love(8)
            $ girl.change_fear(-5)

            "[girl.name] now likes and trusts you a lot more."

            call take_leave(girl, 3) from _call_take_leave


        "派几个打手去收拾那个混蛋 (500金币)" if act == "revenge":

            you "About that [girl.story_profession]..."

            $ MC.rand_say(("gd: 我会派一些人去给他上一课。一顿痛打应该就够了。", "ne: 我会派一些人去追他，让他骨折或留下永久的伤疤....那应该能教训他。", "ev: 我会派一些人去折磨和杀他。他们会让它变得缓慢，太....我会对他的屁股进行中世纪式的刑罚...."))

            girl.char "You will? I would love for him to suffer... Curse that son of a bitch!"

            you "We're on the same page."

            girl.char "Master, I really appreciate what you're doing. Not many people care about a slave's request."

            $ girl.change_love(5)
            $ girl.change_fear(-8)

            "[girl.name] now likes and trusts you a lot more."

            play sound s_gold

            $ MC.gold -= 500

        "雇盗贼公会把那个混蛋洗劫一空 (750金币定金,未知收益)" if act == "money" and thieves_guild.action:

            you "About that [girl.story_profession]..."

            you "I'll ask my contact at the thieves guild what can be done. We'll rob that sucker for all he's worth, and I'll get you your money back."

            girl.char "You really will? That's... Unexpected. I owe you thanks."

            you "Don't mention it."

            girl.char "You're a real gentleman. It seems my luck is turning a little..."

            $ MC.evil -= 1
            $ girl.change_love(8)
            $ girl.change_fear(-5)

            "[girl.name] now likes and trusts you a lot more."

            play sound s_gold

            $ MC.gold -= 750

            "You paid the thieves 750 gold so that they would find and rob the renegade [girl.story_profession]."

            $ gold = 249 + dice(2001)

            "They found his house and recovered [gold] denars from his safe. You give half of it to [girl.name], and keep the rest for your trouble."

            play sound s_gold
            $ MC.gold += gold // 2



        "派几个奸诈的卫兵去把那个混蛋洗劫一空 (750金币定金,未知收益)" if act == "money" and not thieves_guild.action:

            you "About that [girl.story_profession]..."

            you "I know a few guards that can be accommodating. They'll arrest the motherfucker on phoney charges, and I'll get you your money back."

            girl.char "You really will? That's... Unexpected. I owe you thanks."

            you "Don't mention it."

            girl.char "You're a real gentleman. It seems my luck is turning a little..."

            $ girl.change_love(5)
            $ girl.change_fear(-8)

            "[girl.name] now likes and trusts you a lot more."

            play sound s_gold

            $ MC.gold -= 750

            "You paid the guards 750 gold so that they would lock up the renegade [girl.story_profession] and steal his money."

            $ gold = 249 + dice(2001)

            "They found him and threw him in a dark cell for a few years on made-up charges. They recovered [gold] denars from his safe. You give half of it to [girl.name], and keep the rest for your trouble."

            play sound s_gold
            $ MC.gold += gold // 2


        "像处置坏女孩一样惩罚她" if act == "punishment":

            you "You sure are a perverted bitch..."

            girl.char "..."

            girl.char "Yes, Master... *blush*"

            you "Since you seem to love being abused so much, I suppose you won't mind if I rape you right here and now."

            girl.char "R-r... Rape me? *blush*"

            you "That's right..."

            "Not waiting a moment longer, you throw yourself at her, ripping her clothes off her."

            girl.char "Master, oh, Master... You're so forceful..."

            $ act = rand_choice(("service", "sex", "anal", "fetish"))

            $ pic = girl.get_pic(act, not_tags = ["dom", "group", "bisexual", "date", "rest"], hide_farm=True)

            $ vir = False

            if act == "service":

                if pic.has_tag("oral"):
                    $ text1 = "You will suck my cock patiently, until I decide to blow my load down your throat."

                elif pic.has_tags(("handjob", "titjob")):
                    $ text1 = "You will service me with your tits and hands. Get ready!"

                elif pic.has_tag("mast"):
                    $ text1 = "You will masturbate for me, until I bring myself off over your slutty body."

                else:
                    $ text1 = "You will use your body to pleasure me."

            elif act == "sex":
                $ text1 = "I will fuck your dirty pussy now. Prepare to receive your Master's dick."
                $ vir = girl.pop_virginity(origin="MC")

            elif act == "anal":
                $ text1 = "I will fuck your ass like the filthy slut you are. And then I'll fill it up with cum."

            elif act == "fetish":
                $ text1 = "Since you like kinky stuff, let's see how well you handle a little pleasure mixed with a lot of pain."

            you "Shut up, bitch. [text1]"

            play sound s_aaah

            girl.char "Master [MC.name], aaaah!"

            play sound s_mmmh

            if vir:
                show screen show_event(girl.get_pic("virgin", "sex", "naked", and_tags=["sex"], and_priority=False, not_tags=["group", "bisexual", "date", "rest"]), x=config.screen_width, y=int(config.screen_height*0.8))
            else:
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
            with fade

            you "How do you like it, you fucking whore? You love being my pet, don't you."

            play sound s_moans

            girl.char "Yesh, Master... I'm a dirty, dirty bitch... Mmmmh... Aaaah..."

            "Her love juices are flowing as she takes a constant stream of abuse. It isn't long before her moans intensify and she is about to come."

            you "Don't you dare come already!!! Wait for my order!"

            play sound2 s_surprise

            girl.char "Oh, Master... I can't take it anymore..."

            you "Beg for it, bitch. Beg..."

            girl.char "I... Master... Please let me come, I want it so bad..."

            if act in ("service", "fetish"):
                you "Fine, I'll let you come. But only after I release my cum all over your face. You must taste your master's cum if you want to come, understood?"
            else:
                you "Fine, I'll let you come. But only after I fill your dirty hole with my seed. You must be full of your master's cum if you want to come, understood?"

            girl.char "Yes, Master [MC.name]... I'm a filthy sex slave... I'll cum on your orders, please give me a load of warm cum!"

            girl.char "Aaaaaah!!!"

            play sound s_orgasm_young
            with flash

            if act in ("service", "fetish"):
                girl.char "Master!!! YES!!! Come all over my face!!!"
            else:
                girl.char "AAAAAHAAAH! Master! It's spilling inside me!!!"

            you "Ooooh!!!"

            with doubleflash

            "You keep playing with [girl.name], torturing her body and mind until she is reduced to a willing little sex pet."

            show screen show_event(girl.get_pic("rest", and_tags=["naked", "hurt"]), x=config.screen_width, y=int(config.screen_height*0.8))
            with fade

            if vir:
                "You have taken [girl.name]'s virginity. Her obedience has increased."
                $ girl.change_stat("obedience", 5)

            you "I hope you know your place, now, slave."

            girl.char "I am yours, Master... I feel so wonderful..."

            $ girl.change_love(8)
            $ girl.change_stat("obedience", 10)

            hide screen show_event
            with fade

            "[girl.name] now likes you a lot more. Her obedience skill has increased a lot."

        "现在还不是时候":
            return

        "别再为这点小事来烦我":
            you "Yes, well, that was a cool story, but I don't want to hear you whine about this anymore. I. don't. care. Understand me?"

            "She recognizes the threat in your voice, and becomes more guarded."

            girl.char "I... I understand. I was thinking... Never mind."

            you "All right. Now shut up."

            $ girl.change_love(-3)
            $ girl.change_fear(2)
            $ MC.evil += 1
            $ girl.flags["MC refused story"] = True

    $ girl.flags["story"] = 99999 # Dirty, but will do the job. nothing bad will happen anyway if this number of interactions is reached

    if not girl.flags["MC refused story"]:
        $ game.track("origin stories")

    return


## Custom girls stories ##


label empty_girl_story(girl):

    # No story for these girls

#     if girl.flags["story"] == 4:
#         $ girl.flags["story"] = 10

#     elif girl.flags["story"] == 10:
#         $ girl.flags["story"] = 20

#     elif girl.flags["story"] == 20:
#         $ girl.flags["story"] = 50

#         call slave_story_help(girl, act)


#     elif girl.flags["story"] == 50:
#         call slave_story_help(girl, act)

    return



#### END OF BK INTERACTIONS FILE ####
