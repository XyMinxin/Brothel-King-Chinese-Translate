## ADD BLOCK ROLLBACK -


label random_morning_events():

    # This event is a hub dispatching the various events that can happen in the morning (this avoids several events popping up at once)

    # Girl events

    $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]

    if able_girls:
        $ girl = rand_choice(able_girls)
        $ ev_type = rand_choice(["constitution", "obedience", "libido", "sensitivity"])
        $ stat = girl.get_stat(ev_type)

        if stat >= 25:

            # Constitution event

            if ev_type == "constitution" and girl.energy >= 25:

                $ renpy.show_screen("show_img", brothel.pic, _layer = "master")
                with fade

                "As you come out for some fresh air in the early morning, rubbing the sleep from your eyes, you are surprised to meet [girl.fullname], already up and running."

                show screen show_event(girl.get_pic("constitution", "dance", "profile", naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with dissolve

                girl.char "One, two, three, four..."

                "She is doing her morning exercise, bursting with energy."

                if girl.is_("extravert"):
                    girl.char "Oh, hi, Master! How is it going?"
                elif girl.is_("introvert"):
                    girl.char "Oh, it's you... I didn't think there would be anyone here."

                if stat >= 200:
                    "You are amazed at how fast and tough she has become. She has been at it for over an hour, but she barely looks out of breath."
                elif stat >= 100:
                    "She is in very good shape, and you can't help but be impressed by her stamina."
                else:
                    "She is doing some valiant efforts, and little by little, it seems to be paying off."

                menu:
                    extend ""

                    "Admire her" if stat >= 200:
                        you "You have become truly strong now, [girl.name]... I bet you could take me on!"

                        if girl.is_("dom"):
                            girl.char "Ha! You bet! I could take anyone on!"
                        elif girl.is_("sub"):
                            girl.char "Oh, no, Master... I wouldn't dare..."

                        $ result = "pos"

                    "Encourage her" if stat < 200:
                        you "You're doing good, [girl.name]. Keep it up, and you'll be an accomplished athlete in no time."

                        if girl.is_("dom"):
                            girl.char "Hehe, I'm glad you noticed!"
                        elif girl.is_("sub"):
                            girl.char "You... You really think so?"

                        $ result = "pos"

                    "Demean her":
                        $ MC.rand_say(("ev: 你在干什么，你这个愚蠢的婊子？你的身体是用来做爱的，不是用来玩游戏的！别在这浪费你精力！", "哼。我希望你能把同样的精力放在为客户服务上。", "嘿！如果你起得早，你应该给我准备早餐，而不是做这些无意义的运动。", "ev: 哼。妓女身上的肌肉就像男人身上的奶子: 毫无用处。", "玩得开心吗？你不应该用这些时间做一些更有用的事情吗？"))

                        if girl.is_("dom"):
                            girl.char "You bastard..."
                        elif girl.is_("sub"):
                            girl.char "Aw... You're mean..."

                        you "Say what?"

                        girl.char "N-nothing..."

                        $ result = "neg"

                    "Say nothing":
                        "You leave her to her training."
                        $ result = ""

                hide screen show_event
                with fade

            # Obedience event

            elif ev_type == "obedience":
                $ room = rand_choice([room.name for room in brothel.get_common_rooms()])
                $ renpy.show(room, at_list = [top])
                with fade

                "As you cross the [room] in the morning, you run into [girl.fullname]."

                girl.char "Oh! Master [MC.name]."

                show screen show_event(girl.get_pic("maid", "obedience", "profile", naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with dissolve

                if stat >= 200:
                    "She looks at you adoringly and joins her hands in a gesture of respect, bowing deeply as you pass."

                    if girl.is_("dom"):
                        girl.char "Welcome, Master [MC.name], is there anything I can do for you today?"
                    elif girl.is_("sub"):
                        girl.char "M-Master... I am truly honored to see you. Please, allow me to be of service..."

                elif stat >= 100:
                    "She bows and salutes you with deference."

                    girl.char "Good day to you, Master [MC.name]... Can I be of service?"

                else:
                    "She nods in your direction, and moves out of your way as you come. She is learning how to be polite."

                    girl.char "Master... Was there something you wanted from me?"

                menu:
                    extend ""

                    "Congratulate her":
                        you "You are behaving very well these days. Congratulations! The other girls could learn from you."

                        if girl.is_("dom"):
                            girl.char "Well... Thanks..."
                        elif girl.is_("sub"):
                            girl.char "It is my pleasure, Master [MC.name]..."

                        $ result = "pos"

                    "Reject her":
                        $ MC.rand_say(("ev: 别挡着我的路，你这个肮脏的奴隶！我没有时间和你这样的精液垃圾浪费。", "如果我需要你，我会直接命令你。我不希望你问一些无聊的问题！", "难道你不知道奴隶不能直呼她的主人名字吗？如果我需要你服务，我会派人去找你。"))

                        if girl.is_("sub"):
                            girl.char "I... I understand. I'm sorry..."
                        elif girl.is_("dom"):
                            girl.char "Humph... Serves me right for asking..."

                        $ result = "neg"

                    "Tell her to clean up the [room]":
                        you "Well, sure. The [room] is a bit dusty. Why don't you grab a broom and bucket, and clean this place up?"

                        if stat < 100 or (stat < 150 and girl.is_("dom")):
                            play sound s_sigh
                            girl.char "Aw, must I, really? All right, I'll do it... *sigh*"
                        else:
                            girl.char "Of course, Master. You're the boss."

                        $ brothel.change_dirt(-1*dice(3, girl.rank))

                        "[girl.name] spent all morning cleaning up the [room]. [brothel.name] cleanliness has improved."

                        $ result = ""

                    "Tell her to suck your dick":
                        you "Why, sure, there's something you could do for me..."

                        girl.char "Yes?"

                        you "I just woke up, and I'm still hard... I need someone to relieve my stress down there."

                        $ attitude = girl.get_sex_attitude("service", "oral") + girl.get_love()

                        if attitude >= 100 or stat > 150:
                            if girl.is_("lewd"):
                                "She licks her lips, bringing her hand down to massage your crotch."
                                play sound s_mmmh
                                girl.char "Why, of course, Master... I was looking forward to my breakfast today..."
                            elif girl.is_("modest"):
                                "She blushes bright red."
                                play sound s_surprise
                                girl.char "You mean... Here? I... Well... Okay..."

                            $ result = "pos"

                            $ pic = girl.get_fix_pic("service", fix_dict["oral"], and_tags=["maid"], not_tags=["group", "bisexual", "cumshot"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                            with dissolve

                            "Going down on her knees, she pulls down your pants. Your erect cock flies right out in her face, and she proceeds to rub it with both hands."

                            girl.char "Oh... It's already big and hard..."

                            "She licks the tip carefully, where pre-cum is already starting to leak out."

                            play sound s_sucking

                            girl.char "Mmmh... It tastes salty..."

                            "Feeling very excited you push your dick forward, and she opens her mouth to let you slide in."

                            girl.char "Hnngh..."

                            "Holding your buttocks for stability, she takes your cock deeper in as you proceed to fuck her mouth."

                            girl.char "Nggh! Nggh... Nggggh!!!"

                            with flash

                            "Suddenly, the hot feeling of her tongue running the length of your shaft becomes too much, and you release a wad of cum inside her mouth."

                            $ pic = girl.get_fix_pic("service", fix_dict["cum in mouth"], and_tags=["maid"], not_tags=["group", "bisexual"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                            with doubleflash

                            girl.char "Nggh... Aaah..."

                            "She looks at you with a smile, and bows again."

                            girl.char "Thank you, Master [MC.name]. I'm always happy to serve..."

                            $ result = "pos"

                        else:
                            if girl.is_("lewd"):
                                play sound s_laugh
                                girl.char "Haha, Master, you're pushing it... Well, I'm kind of busy now... Sorry."
                                "Before you have a chance to insist, [girl.name] blows you a kiss and slips past you, rushing out of the room."

                            elif girl.is_("modest"):
                                play sound s_scream
                                girl.char "Wh-What? B-But...."
                                "You start unbuckling your pants."
                                girl.char "Bwaaah!!!" with vpunch
                                "Her face flushed with shock, [girl.name] runs out of the room."

                            you "Hey, wait! Damn..."

                            $ result = "neg"

                    "Say nothing":
                        "It's nice that she is learning manners. You nod approvingly, but tell her you don't need her now."
                        $ result = ""

                hide screen show_event
                with fade

            # Sensitivity/Lib event

            elif (ev_type == "sensitivity" and girl.get_fear() < -15) or (ev_type == "libido" and girl.get_love() > 25 and girl.old_interactions >= 3):

                "Late at night, something stirs you out of a deep sleep."

                if girl.is_("extravert"):
                    play sound s_shatter
                    with vpunch
                    girl.char "Oops."

                    "You are startled to see [girl.fullname], who seems to be trying to sneak into your bedroom, without much success."

                elif girl.is_("introvert"):
                    "As you open your eyes, you see a dark silhouette standing in the shadows near your bed."

                    if MC.playerclass == "战士":
                        play sound s_sheath
                        "Your reflexes kick in, and you reach for the dagger you always keep under your pillow with lightning speed. The silhouette recoils in fear, and you realize it's [girl.fullname]."
                    elif MC.playerclass == "法师":
                        play sound s_fire
                        "Muttering the words of a quick defensive spell, you summon a blue flame into the air, casting a spooky light on [girl.fullname]'s surprised face."
                    elif MC.playerclass == "奸商":
                        play sound s_wscream
                        "Startled out of your sleep, you grab for a weapon and find a pillow, your nightcap half-falling over your eyes. Yanking it off with one hand while trying to desperately fend off the intruder with your pillow, you are stunned to see [girl.fullname] standing in front of you, with a surprised look."

                show expression brothel.master_bedroom.get_pic(x=config.screen_width, y=config.screen_height) at top
                if ev_type == "sensitivity":
                    show screen show_event(girl.get_pic("profile", and_tags=["sub"], not_tags=["public"], naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                elif ev_type == "libido":
                    show screen show_event(girl.get_pic("profile", and_tags=["libido"], not_tags=["public"], naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with dissolve

                you "Uh... [girl.name]? What the hell are you doing in my room?"

                girl.char "Oh... Sorry Master... I didn't mean to startle you..."

                "She blushes and looks down at her feet."

                if ev_type == "sensitivity":
                    if girl.is_("dom"):
                        girl.char "Well, you're not going to believe this... There's a mouse in my room. A MOUSE!!!"
                        girl.char "So, obviously, I can't sleep there, and I don't want the girls to laugh at me, or anything...
                        So I thought, you know... Since you're in charge, I guess you could let me sleep here until this is taken care of? *blush*"
                    elif girl.is_("sub"):
                        girl.char "I couldn't tell the others, but... I have night terrors, I feel very scared... I cannot sleep..."
                        girl.char "So I was wondering... Can I sleep with you for a little while? *blush*"
                elif ev_type == "libido":
                    if girl.is_("lewd"):
                        girl.char "Master... I'm bored... I haven't had much {i}action{/i} lately."
                        girl.char "Why don't we have some fun? I'm horny!"
                    elif girl.is_("modest"):
                        girl.char "Master... I... Hem..."
                        girl.char "I was feeling lonely, I mean... Maybe we could... You know..."
                        "She blushes bright red with shame, but gives you a lustful look all the same."

                menu:
                    extend ""

                    "Accept her":
                        you "Hop in, babe. There's room enough for two."

                        "She looks happy and relieved. She slips in bed next to you."

                        $ result = "pos"

                        if ev_type == "sensitivity":

                            show screen show_event(girl.get_pic("rest", and_tags=["sub"],  not_tags=["mast", "orgasm"], soft=True, naked_filter=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                            with dissolve

                            if girl.is_("dom"):
                                girl.char "Thanks. I cannot spend the night with that beast."

                                you "So you're going to sleep next to this here beast?"

                                play sound s_laugh
                                girl.char "Teehee, this one I can handle... *wink*"

                            elif girl.is_("sub"):
                                girl.char "Can I light this candle? I'm still reeling from that last nightmare..."

                                you "Oh, really? Tell me about it."

                                girl.char "Well, it's funny, I can't remember... I feel safe now, thanks to you."

                            if stat >= 100:
                                "She gets closer to you."

                                girl.char "Master... Could you hold me?"

                                you "Sure."

                                "Taking her into your arms, you hug her soft body close. Involuntarily, your cock is rubbing against her belly, and it quickly becomes hard. [girl.name] cannot help but notice."

                                girl.char "Oh..."

                                $ pic = girl.get_pic("kiss", "fondle", "rest", and_tags=["fondle"], not_tags=["group", "bisexual", "mast", "orgasm"], and_priority=False, soft=True, naked_filter=True)

                                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                                with dissolve

                                "She blushes, but doesn't turn away from you. Instead, she leans in and kisses you."

                                girl.char "Oh, [MC.name]... *kiss*"

                                play sound s_sucking

                                "You respond in kind, and before long, both of you are fondling each other tenderly."

                                "After enjoying each other for a while, you both sleep late in the morning, before [girl.name] leaves discreetly."

                                stop sound fadeout 3.0
                                hide screen show_event
                                with fade

                            else:
                                girl.char "Master... Can I ask you something?"

                                you "Yes?"

                                girl.char "What do you think... What do you think people see in me?"

                                $ boost_stat = ""

                                menu:
                                    extend ""

                                    "Your beauty" if girl.get_stat("beauty") >= 25*girl.rank:
                                        you "You are beautiful. That what people see in you."
                                        $ boost_stat = "beauty"

                                        if girl.is_("extravert"):
                                            girl.char "Teehee, thank you! I'm glad you noticed."
                                        elif girl.is_("introvert"):
                                            girl.char "Oh... You really think so?"

                                    "Your charm" if girl.get_stat("charm") >= 25*girl.rank:
                                        you "You are charming and likeable. That's what people like about you."
                                        $ boost_stat = "charm"

                                        if girl.is_("sub"):
                                            girl.char "Oh... Thank you, I'm happy to hear that."
                                        elif girl.is_("dom"):
                                            girl.char "Hmph. You mean they think I'm just a pushover. Damn..."

                                    "Your body" if girl.get_stat("body") >= 25*girl.rank:
                                        you "You have a hot, juicy body. I think that's why people like you."
                                        $ boost_stat = "body"

                                        if girl.is_("modest"):
                                            girl.char "Hey! That's not what I meant... Aw, it's terrible..."
                                        elif girl.is_("lewd"):
                                            girl.char "Aw... That's all that you men ever think about, isn't it? *giggle*"

                                    "Your refinement" if girl.get_stat("refinement") >= 25*girl.rank:
                                        you "You have good taste and you always wear fine clothes and make-up. I think people respect that."
                                        $ boost_stat = "refinement"

                                        if girl.is_("materialist"):
                                            girl.char "Ah, I'm glad you think so too! You can be one of my followers. *wink*"
                                        elif girl.is_("idealist"):
                                            girl.char "I see, thank you... Is that really so important, though?"

                                    "Everything":
                                        you "Well, uh, everything about you is just fine, you know..."

                                        $ girl.change_fear(-1)

                                        "She seems a bit disappointed by your vague answer."

                                        girl.char "I see."

                                    "Nothing in particular":
                                        you "To be honest, I don't think people really look at you. For most people, you are just a sex slave..."

                                        $ result = "neg"
                                        $ girl.change_love(-1)

                                        "Her eyes fill up with tears as she hears your words."

                                        girl.char "Oh no... *sob*"

                                you "Anyway, let's get some sleep. Morning will come soon."

                                "[girl.name] seems very tired, and quickly falls soundly asleep next to you. You follow suit. When you wake up, she is already gone, but you can still smell her scent on your pillow."

                                hide screen show_event
                                with fade

                                if boost_stat:
                                    $ girl.change_stat(boost_stat, dice(3))
                                    "[girl.name]'s [boost_stat] skill has improved a little."

                        elif ev_type == "libido":

                            $ act = rand_choice([act for act in all_sex_acts if (girl.get_sex_attitude(act) + girl.get_love()) > 100])

                            if not act:
                                $ act = rand_choice([act for act in all_sex_acts if (girl.get_sex_attitude(act) + girl.get_love()) > 0])
                                if not act:
                                    $ act = "service"

                            play sound s_mmmh

                            if act == "service":
                                girl.char "Mmmh, Master... I want to make you feel good..."
                            elif act == "sex":
                                girl.char "Come here Master... Mmmh... I want to feel you..."
                            elif act == "anal":
                                girl.char "Master, I have a request... Hem... Could you use my ass? *blush*"
                            elif act == "fetish":
                                girl.char "Oh, Master, I've been a bad girl... I want you to hurt me..."

                            if act != "sex":
                                show screen show_event(girl.get_pic(act, "naked", not_tags=["group", "bisexual", "cumshot"]), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                                with fade

                            if act == "service":
                                play sound s_sucking
                                girl.char "Nggh... Your cock is so delishious..."
                            elif act == "sex":
                                play sound s_moans

                                if girl.pop_virginity(origin="MC"):
                                    show screen show_event(girl.get_pic("virgin", "sex", "naked", and_tags=[act], and_priority=False, not_tags=["group", "bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                                    with fade
                                    "It's [girl.name]'s first time, but she is already very wet. She moans with pleasure as you enter her pussy."
                                else:
                                    show screen show_event(girl.get_pic(act, "naked", not_tags=["group", "bisexual", "cumshot"]), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                                    with fade

                                girl.char "Oh, yes, Master... My pussy feels so hot..."

                            elif act == "anal":
                                play sound s_moans
                                girl.char "Oh yes! Yes... Fuck my ass, harder!!!"
                            elif act == "fetish":
                                play sound s_screams
                                girl.char "Ouch! Aw, it hurts... But it feels so good..."

                            girl.char "Ooh, aaah..."

                            with flash

                            girl.char "Aaaaaah!!!"

                            play sound s_orgasm_fast
                            with doubleflash

                            if act == "fetish":
                                show screen show_event(girl.get_pic("orgasm", and_tags=["fetish"], not_tags=[ "group", "bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                            else:
                                show screen show_event(girl.get_pic(act, and_tags=["cumshot"], not_tags=[ "group", "bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                            "You spend the rest of the night enjoying yourself with [girl.name]."

                            "When she finally leaves your room, the sun is already high up, but you haven't gotten any sleep."

                            hide screen show_event
                            with fade

                            $ girl.change_stat(act, dice(3))
                            $ girl.raise_preference(act, "love", 2)
                            $ MC.change_prestige(girl.rank)
                            $ MC.interactions -= 1

                            "You lose an action for today. You have earned prestige. [girl.name]'s [act] skill has improved."


                    "Kick her out":
                        $ MC.rand_say(["ev: 你胆敢擅自闯进我的房间！！？滚出去，否则我把你头给拧下来！！！", "你疯了吗？滚出我的房间，马上！", "你他妈的以为这里是酒店吗？滚出去。", "我没有时间做这个。去自慰吧或者别的什么。"])

                        "You get up and grab [girl.name] by the shoulder, bluntly shoving her out of the door."

                        play sound s_scream
                        if girl.is_("dom"):
                            girl.char "Ouch! You brute!"
                        elif girl.is_("sub"):
                            girl.char "Aw, I'm sorry, Master! Please don't hurt me... *sob*"

                        if MC.god:
                            you "And don't come back! For the love of [MC.god], slaves these days..."
                        else:
                            you "And don't come back! In the name of cocks and tits and all that is holy..."

                        $ result = "neg"

                        hide screen show_event
                        with fade

                    "Tell her to go back to her room":
                        you "Come on, [girl.name]. It's very late, and I need some sleep right now. You can't stay here."

                        play sound s_sigh

                        if girl.is_("idealist"):
                            girl.char "I see... I'm sorry to have disturbed you. I will go."
                        elif girl.is_("materialist"):
                            girl.char "Aw, but I need to... Fine, I'll just go, then."

                        hide screen show_event
                        scene black
                        with fade

                        "Later, as you pass [girl.name]'s room, you hear some muffled cries."

                        if ev_type == "sensitivity":
                            "It seems she's dreaming again, but it doesn't sound like a nightmare this time."
                        elif ev_type == "libido":
                            "It seems she's having fun all by herself."

                            menu:
                                "Peek":
                                    show screen show_event(girl.get_pic("mast", not_tags=["group", "bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                                    with dissolve

                                    play sound s_moans_quiet

                                    girl.char "Oh, aah, yes, [MC.name]... AAAAAH!!!"

                                    "Peeking through the keyhole, you get to see everything while she pleasures herself, calling your name."

                                    stop sound fadeout 3.0

                                "Don't peek":
                                    pass

                        $ result = ""


                        hide screen show_event
                        with fade


            # Apply results

            $ l = 0
            $ f = 0

            if result == "pos":
                if girl.is_("dom"):
                    $ f = -3
                elif girl.is_("sub"):
                    $ f = -2

            elif result == "neg":
                if girl.is_("dom"):
                    $ l = -2
                elif girl.is_("sub"):
                    $ f = 2

            if l:
                $ girl.change_love(l)
            if f:
                $ girl.change_fear(f)

            $ girl.change_stat(ev_type, dice(6))
            if ev_type not in ("mood", "love", "fear"):
                $xxx6=girl_related_dict[ev_type]
            else:
                $xxx6=ev_type
            "[girl.fullname]'s [ev_type] has increased."

    return


label random_night_events():

    # This event is a hub dispatching the various events that can happen at night (this avoids several events popping up at once)

    # Girl events

    $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]

    if able_girls:
        $ girl = rand_choice(able_girls)

        $ room = rand_choice([room.name for room in brothel.get_common_rooms()] + ["bedroom", "outside"])

        call random_night_girl_event(girl, room) from _call_random_night_girl_event #!

    hide screen show_event

    return


label random_night_girl_event(girl, room):

    $ selected_act = None
    $ selected_fix = None
    $ attitude = None
    $ changed_stats = []
    $ rep_impact = False
    $ intensity = 1
    $ punish = False

    scene black with Dissolve(0.15)

    ### BEDROOM ###

    if room == "bedroom":
        "As you carry out your customary evening inspection, you decide it might be time to pay a visit to [girl.fullname]'s bedroom."

        $ renpy.show_screen("show_img", brothel.get_bedroom_pic(config.screen_width, config.screen_height), _layer = "master")

        menu:
            extend ""

            "Enter [girl.fullname]'s room":
                pass

            "Maybe another time":
                call hide_everything() from _call_hide_everything_7
                scene black with dissolve
                return

        play sound s_knocks

        girl.char "Yes? Come in."

        you "Hi, [girl.name]. It's inspection time..."

        show screen show_event(girl.get_pic("rest", naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

        if girl.get_love() >= girl.get_fear():
            if girl.get_love() >= 50:
                "You find [girl.name] lying on her bed, idling. As soon as she sees you, she strikes a lascivious pose, flashing you an enticing smile."
                girl.char "Oh, Master [MC.name]... How nice of you to come by... ♥"
                $ reaction = "love"
            else:
                "[girl.name] is sitting at her make-up table, getting ready for the night. She seems a little surprised to see you."
                girl.char "Yes, Master [MC.name]?"
                $ reaction = "normal"
        else:
            if girl.get_fear() >= 25:
                "[girl.name] seems frightened when she sees you, standing away from you with her back to the wall. She mutters excuses, trying to avoid eye contact."
                girl.char "Master! I... I mean... I'm sorry..."
                $ reaction = "fear"
            else:
                "[girl.name] seems startled by your barging in. She interrupts what she was doing, crossing her arms."
                girl.char "Oh, it's you... What is it?"
                $ reaction = "normal"

        if reaction == "fear":
            girl.char "I'll... I'll leave you to it then..."
            "She heads for the door."

            menu:
                extend ""

                "Not so fast":
                    "As she tries to go past you, you move to block the exit."

                    you "Not so fast, little girl... I am here to inspect {i}you{/i} as well as your room."

                    play sound s_surprise

                    girl.char "Ah!"

                    pass

                "Let her go":
                    $ girl.change_fear(-3)
                    return

        elif reaction == "love":
            "She stretches lazily like a cat, then rolls slowly on her bed."
            girl.char "Why don't you join me, Master? You'll be more comfortable here..."

        else:
            "She stands and waits passively for your inspection."

        menu:
            "What do you do?"

            "Examine her bedroom":

                "You take a look around her room."

                $ c = rand_choice(["EI", "MI", "LM"])

                $ girl.personality_unlock[c] += 20

                if c == "EI":
                    if girl.is_("extravert"):
                        "She has arranged her room with lots of colorful baubles. She has portraits of her family and friends hanging on the walls. There aren't many books to be found, but lots of comfortable cushions for visitors to sit on."
                        $ stat = "charm"
                    else:
                        "The place is a little spartan, with four naked walls and just the basics. There are heaps of books addressing various topics scattered around the room, however, and the bed looks really comfy. The place looks lived-in."
                        $ stat = "obedience"
                elif c == "MI":
                    if girl.is_("materialist"):
                        "You notice many shiny jewels and nice clothes laying around her night table, and about a hundred boxes for shoes and accessories. She sure seems to live large for a slave..."
                        $ stat = "body"
                    else:
                        "The place is beautifully decorated with pretty flowers and cute ribbons. A half-finished painting depicts a landscape that you recognize to be from [girl.origin]."
                        $ stat = "sensitivity"
                elif c == "LM":
                    if girl.is_("lewd"):
                        "The bedsheets are a mess, and skimpy clothes and lingerie lay on the floor, wherever they have been dropped. You notice some advanced sex treatises on a shelf, as well as erotic novels from the market, heavily bookmarked."
                        $ stat = "libido"
                    else:
                        "Candles are burning for the gods on a small altar, and calligraphy rolls depicting popular prayers and moral sayings adorn the walls."
                        $ stat = "refinement"

                you "Well..."

                menu:
                    "What do you think about her room?"
                    "Nice place":
                        you "It's a nice place you have here. Keep it up."
                        girl.char "Thank you, Master."
                        $ girl.change_love(2)
                        $ changed_stats = [(stat, dice(3)+1)]
                    "It's a dump":
                        you "What a dump! Throw those things away, please, and clean up before the customers come."
                        girl.char "Whaaat?"
                        $ girl.change_love(-2)
                        $ changed_stats = [(stat, dice(3)+1)]

                you "That will be all."

            "Comment on her appearance":

                "You take a good, professional look at her."

                $ be = girl.get_stat("beauty")
                $ bo = girl.get_stat("body")

                if be < 25:
                    you "You look like a mess. I've seen prettier girls working the pig farms."

                    "She looks distressed."

                    girl.char "So... So mean..."

                    $ girl.change_love(-2)

                elif be < 75:
                    you "Appearance isn't everything... But you could make more effort."

                    girl.char "Aw..."

                    $ girl.change_love(-1)

                elif be < 150:
                    you "You're a pretty girl, [girl.name]. Keep it that way."

                    girl.char "... Thanks..."

                    $ girl.change_love(1)

                else:
                    you "You are something to behold... Such beauty... Use it well."

                    girl.char "Oh... Thank you, Master."

                    $ girl.change_love(2)

                if bo < 25:
                    you "You're all out of shape. No one will want to fuck you in this sorry state."

                    play sound s_surprise

                    girl.char "Whaaat?"

                    $ girl.change_love(-2)

                elif bo < 75:
                    you "You should work on your body. I'm sure you could do better."

                    girl.char "Uh? I..."

                    $ girl.change_love(-1)

                elif bo < 150:
                    you "Boobs, ass... I like what I see... Keep it that way."

                    girl.char "Oh... Thanks, I guess..."

                    $ girl.change_love(1)

                else:
                    you "You have a body to die for. I'm impressed!"

                    girl.char "I... Thank you, Master."

                    $ girl.change_love(2)

                if be <= bo:
                    you "Anyway. Put some make-up on, go out there, and do your best."
                    $ changed_stats = [("beauty", dice(3))]

                else:
                    you "Anyway. Make sure to flaunt your goods right tonight... I'll be watching."
                    $ changed_stats = [("body", dice(3))]

            "Inspect her naked body":
                $ selected_act = "naked"
                if girl.naked:
                    "[girl.name] is already naked, so you take a step back to check her out from head to toe."
                else:
                    you "Take off all your clothes. Now."

                    if (girl.is_("dom") and girl.get_stat("obedience") < 100) or (girl.is_("sub") and girl.get_stat("obedience") < 50):
                        girl.char "What? B-But... No!"
                        "Ignoring her resistance, you force her to remove her clothes. She looks mortified."
                        $ girl.change_fear(2)

                show screen show_event(girl.get_pic("naked", "profile", and_tags="profile", soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with dissolve

                you "Hmm... Turn around..."

                "You check her naked body from every angle."

                $ attitude = girl.get_sex_attitude("naked") + girl.get_love() - girl.get_fear()

                if attitude > 100:
                    show screen show_event(girl.get_pic("naked", and_tags=["libido", "profile"], soft=True), x=config.screen_width, y=int(config.screen_height*0.8))
                    with dissolve

                    "She blushes as you look at her private parts, her nipples perking up as she gets aroused by the experience."
                    $ changed_stats = [("sensitivity", dice(3)+2)]

                elif attitude > 0:
                    "She submits to your inspection, blushing and looking away as you give her a thorough examination."
                    $ changed_stats = [("sensitivity", dice(3))]
                else:
                    show screen show_event(girl.get_pic("naked", and_tags=["sad", "profile"], soft=True), x=config.screen_width, y=int(config.screen_height*0.8))
                    with dissolve

                    "Upset and ashamed, she tries her best to hide her sensitive parts with her hands as you look at her with hungry eyes."
                    $ changed_stats = [("sensitivity", -1*dice(3)), ("obedience", dice(3))]

                you "That will be all. Now go to work."

            "Kiss her" if reaction in ("love", "normal"):
                $ fix = "kissing"
                call night_girl_perform() from _call_night_girl_perform


            "Join her in bed" if reaction == "love":
                $ selected_act = "sex"

                if girl.is_("lewd") and not girl.test_fix("69") == "neg":
                    $ fix = "69"
                else:
                    $ fix = "spooning"

                "She giggles as you join her on the bed."

                girl.char "Oh, Master... *blush*"

                call night_girl_perform() from _call_night_girl_perform_1

                with fade

                "You both lie panting on the bed, saying nothing for a while. Then, seeing the time, you decide to get up and leave."

                you "Thank you, [girl.name]... Good job."

                girl.char "Sure... Anytime, boss..."

            "Make her worship your dick" if reaction in ("normal", "fear"):
                $ selected_act = "service"
                $ fix = "penis worship"


                "Pulling your dick out of your pants, you take her soft hand and place it on your hard shaft."

                you "Show me some respect here... I want you to devote all your attention to your Master's dick."

                if girl.get_stat("obedience") < 75:
                    girl.char "S... Stop it!"

                    call fight_attempt(girl, "service", 1) from _call_fight_attempt

                    if _return:
                        call hide_everything() from _call_hide_everything_1
                        scene black with dissolve
                        "[girl.fullname] ran away."
                        return

                    "With a defeated look, she goes down on her knees and starts rubbing your hard cock, only an inch from her face."

                else:
                    "Obeying your order, she gets down on her knees and starts masturbating your erect cock with both hands."

                call night_girl_perform() from _call_night_girl_perform_2

            "Fuck her mouth" if reaction == "fear":
                $ selected_act = "fetish"
                $ fix = "irrumatio"

                you "Get down. I'm going to fuck your face."

                if girl.get_stat("obedience") < 100:

                    girl.char "What? No!!!"

                    call fight_attempt(girl, "fetish", 1) from _call_fight_attempt_1

                    if _return:
                        call hide_everything() from _call_hide_everything_8
                        scene black with dissolve
                        "[girl.fullname] ran away."
                        return

                    "Pushing her onto the bed, you free your hard cock from your pants and shove it straight down her throat."

                else:
                    "She lays down on the bed obediently, opening her mouth to receive your erect cock. You slide it as far down her throat as you can."

                call night_girl_perform() from _call_night_girl_perform_3

        stop sound
        call hide_everything() from _call_hide_everything_9
        scene black with dissolve
        with dissolve


    ### OUTSIDE ###

    elif room == "outside":
        $ renpy.show_screen("show_img", brothel.pic, _layer = "master")

        "Coming back from your errands, right before the night's opening, you spot [girl.fullname], rushing back to [brothel.name] from a side street."

        you "It is late already, she should be preparing? I wonder what's going on..."

#        show screen dark_filter
        show screen show_event(girl.get_pic("run", "profile", and_tags = ["outside", "town"], and_priority=False, naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        menu:
            "What do you do?"

            "Confront her":
                pass

            "Ignore her":
                you "Well, she's here now. I've got more important things to attend to."

                call hide_everything() from _call_hide_everything_10
                scene black with dissolve
                $ girl.change_stat("obedience", -1*dice(3))
                "[girl.fullname] has become less obedient."
                return

        $ MC.rand_say(("gd: 发生什么事了[girl.name]？你还好吗？", "ne: 啊，[girl.name]。你是时候回来了。", "ev: 嘿，[girl.name]，你这个愚蠢的婊子！你他妈以为你在干什么？"))

        $ excuse = rand_choice(("我去拜访了一个朋友", "我去购买了一些用品", "我去散步结果迷路了", "我在给希露拿东西", "我感觉有点不舒服，想出去呼吸一下新鲜空气", "我休息的时候忘了时间。"))

        girl.char "M-Master, you... I'm sorry I'm late, [excuse], and..."

        if (girl.is_("very lewd") and girl.get_stat("libido") >= 75) or (girl.is_("lewd") and girl.get_stat("libido") >= 150):
            show screen show_event(girl.get_pic("libido", and_tags=["profile"], soft=True, naked_filter=True), x=config.screen_width, y=int(config.screen_height*0.8))
            with dissolve

            "You notice her clothes are in disarray, and her skin is glistening with sweat. She's got the smell of sex all over her. Clearly, she's been fooling around..."

        else:
            "She seems to be telling the truth."

        menu:
            "What do you do?"

            "Let it go":
                you "I see. Fine, then. Try not to be late next time, ok?"
                girl.char "Thank you, Master [MC.name]."

                call hide_everything() from _call_hide_everything_11
                scene black with dissolve
                $ girl.change_fear(-1)
                $ changed_stats = [("obedience", -1*dice(3))]

            "Scold her":
                $ MC.rand_say(("gd: 过来，[girl.name]，你看大家都在忙着准备晚上的工作。你也应该做好你的本分工作。", "ne: 听着，我不在乎你在做什么，但你必须按时准备好工作。从现在开始，你要按时回来。", "ev: 借口，总是借口！我看起来像是在乎的人吗？现在马上给我滚去工作，否则后果自负！"))
                if girl.is_("dom"):
                    girl.char "B-But, Master... Really, it's not my fault! Aw..."
                else:
                    girl.char "S-sorry, Master... I will..."

                call hide_everything() from _call_hide_everything_12
                scene black with dissolve

                $ changed_stats = [("obedience", 1), ("mood", -2)]


            "Punish her":
                $ MC.rand_say(("gd: 虽然我不喜欢这样做，但你必须受到惩罚。我们有规则，你必须遵守。", "ne: 好了，你知道该怎么做了吧。你违反了规则，现在准备接受惩罚吧。", "ev: 真是个自命不凡的小婊子。还敢跟我顶嘴？让我们讨论一下对你的惩罚。"))
                if girl.is_("very dom"):
                    girl.char "Get away from me! You have no right..."
                    $ girl.change_love(-3)
                elif girl.is_("dom"):
                    girl.char "No! I haven't done anything wrong!!!"
                    $ girl.change_love(-1)
                elif girl.is_("very sub"):
                    girl.char "W-what... Oh... I see..."
                    $ girl.change_fear(2)
                elif girl.is_("sub"):
                    girl.char "Oh, Master... Please, d-don't..."
                    $ girl.change_fear(1)

                menu:
                    "How will you punish her?"

                    "Make her clean up the dirty sheets tonight":
                        you "After your service, you're going to do all the laundry tonight, using your bare hands and a bar of soap. I want you to wipe every last cum stain off those bed sheets! Or you'll have to do it again tomorrow."
                        girl.char "Aw..."

                        $ girl.change_fear(1)
                        $ changed_stats = [("obedience", dice(3))]

                    "Force her to haul some heavy supplies":
                        you "You're going to pick up the beer kegs downstairs and bring them all up to the hall. On the double!"
                        girl.char "Oh no... They're so heavy..."

                        $ girl.change_fear(1)
                        $ changed_stats = [("constitution", dice(3))]

                    "Place her naked by the entrance door":

                        $ selected_act = "naked"

                        $ touched = rand_choice(("breasts", "tits", "ass", "butt", "nipples", "pussy"))
                        if touched in ("breasts", "tits", "nipples"):
                            $ fix = "fondling her boobs"
                        elif touched in ("ass", "butt"):
                            $ fix = "groping her ass"
                        else:
                            $ fix = "fingering"

                        call night_girl_perform() from _call_night_girl_perform_4

                    "Make her service every customer that comes in": # No call of the perform label for this one

                        $ selected_act = "service"
                        $ fix = rand_choice(["handjobs", "oral", "titjobs"])
                        $ selected_fix = fix_dict[fix]

                        if fix == "handjobs":
                            $ text1 = "双手"
                        elif fix == "oral":
                            $ text1 = "嘴巴"
                        elif fix == "titjobs":
                            $ text1 = "奶子"

                        you "Stand right here. On your knees. You will use your [text1] to service the customers. Give them a proper greeting!"

                        if girl.get_stat("obedience") < 100:
                            girl.char "Whaaat??? No way! It's not..."

                            call fight_attempt(girl, "service", 1) from _call_fight_attempt_2

                            if _return:
                                call hide_everything() from _call_hide_everything_13
                                scene black with dissolve
                                "[girl.fullname] ran away."
                                return

                            "Forcefully grabbing her, you push her onto her knees."
                            you "You will do as you're told! And don't let me hear that you disrespected a single customer."

                            girl.char "Aw..."

                        else:
                            girl.char "I understand..."

                        with fade

                        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["public"], not_tags=["group", "bisexual", "cumshot"])

                        if fix == "handjobs":
                            "She kneels beside the door, welcoming her first customer by unbuckling his pants."
                            girl.char "Please, mister, let me help you with this..."

                        elif fix == "oral":
                            "She gets down at the feet of the first customer to enter the brothel, raising her hand to fondle his dick over his pants."
                            girl.char "Welcome, Mister... Let me pleasure you with my mouth. It's... On the house."

                        elif fix == "titjobs":
                            "She kneels beside the door and unbuttons her shirt, exposing her naked breast to the first customers."
                            girl.char "Mister, would you like a little rub while you wait for your turn?"

                        play sound s_sucking

                        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                        with dissolve

                        $ attitude = girl.get_sex_attitude("service", fix)
                        $ girl.interactions = 0

                        if attitude > 100:
                            "[girl.name] seems to enjoy giving [fix], really putting her heart into it. She is visibly turned on by the experience, begging for the customers to cum for her."
                            $ girl.change_fear(-3)
                            $ changed_stats = [("obedience", dice(3) + 2), ("service", dice(6))]

                        elif attitude > 0:
                            $ changed_stats = [("obedience", dice(3)), ("service", dice(3))]

                        else:
                            "[girl.name] looks grossed out and almost retches as the customer approaches her for [fix]. He doesn't enjoy it much."
                            $ girl.change_love(-3)
                            $ changed_stats = [("obedience", -1*dice(3)), ("service", -1*dice(3))]

                        $ rep_impact = True

                        "You make her service every incoming customer tonight. Exhausted, her body and clothes covered in cum stains, she goes off to rest."

                    "Fuck her right where she stands":
                        $ selected_act = "sex"
                        $ fix = rand_choice(["public acts", "doggy style", "piledriver"])

                        if fix == "public acts":
                            you "I am going to teach you a lesson, right here in front of everybody. Take off your clothes."
                        elif fix == "doggy style":
                            you "Take off your panties, turn around, and put your hands against the wall. I'm going to teach you a little lesson..."
                        elif fix == "piledriver":
                            you "Lay down on the ground, and take off your panties. I'm going to give you a good pounding."

                        if girl.get_stat("obedience") < 150:
                            girl.char "What? No!!! Stop!"

                            call fight_attempt(girl, "sex", 2) from _call_fight_attempt_3

                            if _return:
                                call hide_everything() from _call_hide_everything_14
                                scene black with dissolve
                                "[girl.fullname] ran away."
                                return

                            "Ignoring her pleading, you grab her panties and tear them off."
                            you "Let me teach you to obey using a language your pussy will understand...."

                        else:
                            girl.char "... Yes, Master."
                            "She slowly removes her panties, exposing her pink pussy."

                        call night_girl_perform() from _call_night_girl_perform_5


                stop sound
                call hide_everything() from _call_hide_everything_15
                scene black with dissolve


    ### TAVERN ###

    elif room == "tavern":

        "As the first customers pour into [brothel.name], you decide to check out the {b}tavern{/b} to see how things are going."

        $ renpy.show(room, at_list = [top])
        with dissolve

        "As you move among the tables, greeting some regulars, you hear one of the girls scream."

        play sound s_scream

        if girl.is_("dom"):
            girl.char "Hey! Stop it, old man!!!"
        else:
            girl.char "M-Mister... Please, don't..."

        show screen show_event(girl.get_pic("waitress", naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

        "You notice a dodgy, lecherous drunkard, with his hand down [girl.fullname]'s panties. She tells him to stop."

        you "What's going on here?"

        menu:
            extend ""

            "Intervene and take [girl.name]'s side":
                "Grabbing the man by the shoulder, you yank him away from your slavegirl."

                you "Hey, buster! Take your hands off the merchandise."

                man "Wh... What? Whaddaya want?"

                $ d = dice(4)

                if d == 1:
                    $ strength = 0
                    "The old guy seems scared and confused, and starts whining and begging for mercy."
                    man "Please, sir, leave an old feller be! I was only havin' a li'l fun with the missy here..."

                elif d == 2:

                    "The scroungy old man looks cunning. He takes a good look at you, then backs off."

                    if MC.get_defense() < 5:
                        $ strength = 1
                        $ magic = 2
                        girl.char "Oh, Master [MC.name], thanks..."
                        extend " Watch out!" with vpunch

                        play sound s_sheath

                        "The rogue customer draws out a dagger from seemingly nowhere and lurches from behind you."
                    else:
                        $ strength = 0
                        man "I... I didn't mean no harm, good sir..."

                elif d == 3:

                    $ strength = 3
                    $ magic = 0

                    "The old man is quite muscular for a geezer. His brutish looks and mean, murderous stare mean you are in for a fight."

                    man "Let me go, you fucker! I'm gonna knock yer head off!!"

                    play sound s_sheath

                    "He takes out a broad scimitar and charges out at you while girls and customers scatter in all directions."

                elif d == 4:

                    $ strength = 5
                    $ magic = 4

                    "Even though he looks unassuming, you notice the harasser is lean and well-built. With surprising speed and technique, he escapes your grip."

                    man "Hands off, peasant! I shall teach you how to treat your betters..."

                    play sound s_sheath

                    "The man takes out a long, thin rapier and squares off. He must be some noble or knight, partying under a disguise."

                if strength:
                    menu:
                        "What do you do?"

                        "Fight him":

                            $ type = "combat"
                            $ result = MC.get_defense() + dice(6) - (strength + dice(6))

                        "Cast a spell":

                            $ type = "magic"
                            $ result = MC.get_spirit() + dice(6) - (magic + dice(6))

                    if result >= 0:

                        if type == "combat":

                            with vpunch
                            play sound s_sheath
                            "Rising up to the challenge, you draw your sword right on time to parry his first attack."

                            "The man takes a few furious blows at you, but he is quite drunk and his attacks are clumsy."

                            "As he lurches towards you, bellowing with rage, you take a sidestep and cut his belt clean off."

                            play sound s_sheath
                            with vpunch

                            man "Uh?? Arrh!!!"

                            play sound s_crowd_laugh

                            "With his pants around his ankles and your blade to his throat, the man surrenders shamefully. The whole room bursts into laughter."

                        elif type == "magic":

                            play sound s_spell
                            you "Shazam!!!" with vpunch

                            play sound s_punch
                            with vpunch

                            "A nicely aimed telekinetic spell sends a heavy wooden stool flying right into his stupid face, knocking the bugger off his feet."

                            play sound s_crowd_laugh

                            if brothel.get_security():
                                "The room applauds your talent as the stunned wretch struggles to come back to his senses, only to find himself surrounded by your security."
                            else:
                                "You disarm the knocked out customer. [girl.name] and you watch with a frown as he slowly comes back to his senses."

                        $ brothel.change_rep(3)


                    else:

                        if type == "combat":
                            "You try to reach for your weapon, but the wretch is damn fast. He is already onto you."

                        elif type == "magic":
                            play sound s_fizzle
                            "Your opponent is skilled at fighting mages. Before you can attempt to conjure up a cool spell, the whizzing noise of a blade coming swiftly to meet your neck breaks your concentration."

                        "You jump out of the way to escape his first attack, only to hit your head hard into a heavy oak table."

                        play sound s_punch
                        with vpunch
                        you "Ouch!"

                        "The furious man charges back towards you, aiming his weapon straight at you. You run away on all fours, crawling among the tables and broken bottles."

                        with vpunch
                        man "Come back here!"

                        play sound s_crowd_boos

                        if brothel.get_security() > 0:
                            "Security finally arrives, chasing the assailant away. You get back on your feet, the customers laughing and booing at your poor performance."
                        else:
                            "The man is too drunk and soon tires from running after you. Instead, he grabs a wad of cash from your coffer, gives [girl.name] a long, sloppy kiss, and runs off into the night."
                            $ MC.gold -= 100

                            play sound s_cash
                            "You have lost 100 gold."

                        $ brothel.change_rep(-3)

                        "Your brothel has lost reputation."

                else:
                    $ result = 0

                if result >= 0:

                    $ girl.change_love(2+dice(3))

                    "You and [girl.name] stand above the defeated man. She gives him an angry look."

                    you "What should we do with this troublemaker, [girl.name]? Any ideas?"

                    if girl.is_("very lewd") and girl.get_stat("libido") >= 75:
                        "She licks her lips."

                        girl.char "I have an appropriate punishment in mind... Let me have a little fun..."

                        $ punish = True

                    elif girl.is_("lewd") and girl.get_stat("libido") >= 150:
                        "She blushes."

                        girl.char "He must be punished... I think I know a way..."

                        $ punish = True

                    elif girl.is_("dom"):
                        girl.char "Let's punish that fucker! I'm going to give him a good beating."

                        man "Nooo!!!" with vpunch

                        girl.char "Take that!"

                        play sound s_punch
                        with vpunch

                        man "Ouch!"

                        girl.char "And THAT!"

                        play sound s_punch
                        with vpunch

                        pause 0.2

                        play sound s_wscream

                        $ punish = False

                    else:
                        girl.char "It... It isn't necessary, just let him go... I'm sorry for causing trouble, Master."

                        you "Have it your way. Now, go back to work."

                        $ punish = False

                    if punish:
                        if girl.has_trait("Virgin"):
                            $ choices = ["femdom", "footjobs"]
                        else:
                            $ choices = ["cowgirl", "femdom", "footjobs"]

                        $ fix = rand_choice([f for f in choices if girl.test_fix(f) != "neg"])

                        if not fix: # Rare case: girl hates everything
                            $ fix = rand_choice(choices)

                        call night_girl_perform() from _call_night_girl_perform_6

                else:
                    $ girl.change_love(dice(3))

            "Intervene and take the customer's side":
                man "Stop resisting, ye little slut!"
                girl.char "Master, haa... Help me..."

                "You frown at [girl.name], standing aside with your hands on your hips."

                you "Excuse me sir, is this girl bothering you?"

                man "She's a wild one! She won't let me have a little fun..."

                "The man slides a finger inside her as she struggles to get him off."

                play sound s_scream_loud

                girl.char "Aaah!!! Master!!!"

                you "Shut up, slave. You are here to serve the customers! You'd better behave now..."

                $ girl.change_fear(2+dice(3))

                girl.char "B-But..."

                you "Is there anything this lowly slave could do for you, Mister?"

                man "Why, there sure is..."

                menu:
                    "Make [girl.name] service the customer":
                        $ selected_act = "service"
                        $ fix = rand_choice(["masturbation", "deep throat", "swallowing"])

                        if girl.get_stat("obedience") < 100:
                            girl.char "No! I don't want to..."

                            call fight_attempt(girl, "service", 1) from _call_fight_attempt_4

                            if _return:
                                call hide_everything() from _call_hide_everything_16
                                scene black with dissolve
                                "[girl.fullname] ran away."
                                return

                    "Let the customer fuck [girl.name]":
                        $ selected_act = "sex"
                        $ fix = rand_choice(["insults", "dirty sex", "creampie"])

                        if girl.get_stat("obedience") < 100:
                            girl.char "Go away! No!"

                            call fight_attempt(girl, "sex", 2) from _call_fight_attempt_5

                            if _return:
                                call hide_everything() from _call_hide_everything_17
                                scene black with dissolve
                                "[girl.fullname] ran away."
                                return

                        man "I got meself a bad case of the hard-on right now. She better help me with that."

                call night_girl_perform() from _call_night_girl_perform_7




            "Let them sort it out between themselves":
                you "I like to stay above the fray."

                if girl.is_("dom"):

                    play sound s_punch
                    girl.char "I'm going to kick your drunk ass!" with vpunch

                    $ changed_stats = [("obedience", -1*dice(3))]

                elif girl.is_("very dom"):

                    play sound s_ahaa
                    girl.char "..."

                    $ changed_stats = [("obedience", dice(3))]

                else:

                    play sound s_scream
                    girl.char "Hiii!" with vpunch

        stop sound
        call hide_everything() from _call_hide_everything_18
        scene black with dissolve


    ### CLUB ###

    elif room == "strip club":

        "You join the customers as they gather inside [brothel.name] and head for the {b}strip club{/b}, where the night is about to get started."

        $ renpy.show(room, at_list = [top])
        with dissolve

        "You spot [girl.fullname] as she gets on stage, speaking a few words to usher the customers in."

        show screen show_event(girl.get_pic("profile", and_tags=["dancer"], naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

        girl.char "Ladies and gentlemen, please be seated..."

        "The crowd is already warmed up with spices and alcohol, and greets [girl.name] with loud jeers and obscene jokes."

        menu:
            "What do you do?"

            "Join the crowd":
                "You find a seat in the front row, next to a group of rowdy customers."

                $ cust = rand_choice(["男人", "女人", "一桌人"])

                "One [cust] in particular stands out among the crowd."

                if cust == "woman":
                    "While the men and women of Zan share a taste for vice and sleaze in equal measure, female customers are a rare sight at the brothel."
                    "Even more surprising, the woman is a knockout. She wears a semi-transparent, low-cut dress, which leaves little to the imagination. Customers nearby are salivating over her, but she has eyes only for [girl.name]."

                elif cust == "man":
                    "He looks like a foreigner, with dark skin and large sinewy muscles. Even though he is rather inebriated at the moment, you can tell he is a man used to issuing orders, whether it is in business or war. He seems taken with [girl.name]."

                else:
                    "They seem to be friends or brothers, out for a night of drinking and philandering. It seems [girl.name] has caught their eye."

                "As [girl.name] blushes and tries to excuse herself away from the stage, the [cust] finally notices you. {nw}"

                if cust == "woman":
                    extend "She recognizes you, and whispers to you with a sultry voice."

                    woman "You're the owner of this place, aren't you? Why don't you let me take up the stage with your charming slavegirl..."

                    $ fix = rand_choice(["dildos", "strap-ons", "squirting"])
                    $ selected_act = "bisexual"

                elif cust == "man":
                    extend "Drunk as he is, he recognizes you as the owner."

                    man "You! Good man! I've got my eye on your little pet slave up over there... Why don't you let me show her a thing or two? I can be a {i}very{/i} generous man..."

                    $ fix = rand_choice(["doggy style", "ass-to-mouth", "spanking"])
                    $ selected_act = "anal"

                else:
                    extend "One of the men recognizes you."

                    man "Look, mates, the owner is here! Maybe he'll let us have a little fun?"

                    man "You're [MC.name], aren't you? Will you let us party with your girl up there? Tonight is my birthday, and I've got cash to spare!"

                    $ fix = rand_choice(["double penetration", "multiple orgasms", "bukkake"])
                    $ selected_act = "group"

                $ attitude = girl.get_sex_attitude(selected_act, fix = ["public acts"] + [fix])

                "The offer seems tempting, and likely to be a hit with the customers. {nw}"

                if attitude >= 100:
                    extend "Knowing [girl.name], she might even enjoy it too."
                elif attitude >= 0:
                    extend "But you are not sure about [girl.name]'s reaction."
                else:
                    extend "However, [girl.name] might not respond well."

                menu:
                    "What do you decide?"

                    "Let the [cust] fuck [girl.name] on stage":

                        you "All right then. Have some fun. But make sure it is entertaining for the customers."

                        you "Hey! [girl.name]!"

                        girl.char "Yes, Master?"

                        you "You have a special guest tonight. {nw}"

                        if cust == "woman":
                            extend "Make sure you treat her right."
                            $ intensity = 1
                        elif cust == "man":
                            extend "Make sure you do as he says."
                            $ intensity = 2
                        else:
                            extend "Make sure to please him and his friends."
                            $ intensity = 3

                        girl.char "Wait, what?"

                        if girl.get_stat("obedience") + attitude < 150:
                            "She sees the customer's greedy look and understands your meaning."
                            girl.char "Uh? No!!! Get away from me! *mad*"

                            call fight_attempt(girl, selected_act, intensity) from _call_fight_attempt_6

                            if _return:
                                call hide_everything() from _call_hide_everything_23
                                scene black with dissolve
                                "[girl.fullname] ran away."
                                return

                            else:
                                "She looks tense and defensive as you and the horny [cust] join her on stage."

                        else:
                            if cust == "男人":
                                $ text1 = "他"
                            elif cust == "女人":
                                $ text1 = "她"
                            else:
                                $ text1 = "他们"


                            "She knows better than to discuss your orders in public. She extends her hand to the [cust] to help [text1] get on stage."

                            you "Good girl."

                        call night_girl_perform() from _call_night_girl_perform_8

                    "Refuse":

                        you "I'm sorry, but that's not how it works. The club is just for shows, not for whoring."

                        if cust == "woman":
                            woman "How disappointing. I thought we were this close to an understanding..."
                            "She gives you a cold stare, and sits back in her seat with her arms folded, ignoring you for the rest of the performance."
                        elif cust == "man":
                            man "Oh, really? *frown* I just have to take my business elsewhere, then."
                            "The man gets up and leaves, angry."
                        else:
                            man "Come on, man, you suck! Bros, let's leave this hovel... I am getting bored to death."

                            "The drunken party gets up and leaves, kicking some chairs down on their way out."

                        $ brothel.change_rep(-1*dice(6))
                        $ selected_act = None

                        "Your brothel reputation has decreased."


            "Get on stage":
                "Before [girl.name] has a chance to excuse herself from the stage, you hurry on stage to join her."

                girl.char "Master [MC.name]? Wh... What's going on?"

                menu:
                    "What do you want to do?"

                    "Give a rousing speech":
                        "You decide it's time for you to get your share of the limelight."

                        you "Dear friends..."

                        "It's hard for you to get heard above the noise of drunk and raunchy customers. You raise your voice."

                        $ r = dice(6) + MC.get_charisma()

                        if r >= 10:
                            if dice(6) == 6:
                                you "Pussy, pussy, pussy!"
                                you "Come on in Pussy lovers!"
                                you "Here at [brothel.name], we’re slashing pussy in half!"
                                you "Give us an offer on our vast selection of pussy! This is a pussy blow out!"
                                you "Alright, we got white pussy, black pussy, elvish pussy, yellow pussy. We got hot pussy, cold pussy. We got wet pussy. We got smelly pussy. We got hairy pussy, bloody pussy."
                                you "C'mon, you want pussy, come on in Pussy Lovers! If we don’t got it, you don't want it! Come on in Pussy lovers!"

                            else:

                                you "Friends! I give you a heartfelt welcome to [brothel.name]! A finer house with finer girls you won't find anywhere in Zan."

                                "A bunch of regulars are in the crowd, and they roar back in approval."

                                you "See our own [girl.name] here? Look at her! Isn't she lovely?"

                                "The crowd again yells their support."

                                you "[girl.name] gets wet every night, knowing you guys are coming for her... And she has many sisters here who share her devotion and are ready to do your every bidding!"

                                if girl.is_("dom") and girl.get_stat("obedience") > 150 or girl.get_stat("obedience") > 75:
                                    "[girl.fullname] blushes by your side, but says nothing."
                                else:
                                    girl.char "What the..."

                                you "Anyway! We hope you have a great time with us tonight. Don't forget to tip well! This puts the girls in a good mood!"

                            "The crowd jumps to their feet and applauds you as you wrap up your eloquent speech. The customers feel exceptionally generous tonight: you get a revenue boost."

                            play sound s_gold

                            python:
                                eff = [Effect("boost", "income", 0.1, scope="brothel")]
                                MC.add_effects(eff)
                                calendar.set_alarm(calendar.time + 1, StoryEvent(label = "effect_expired", call_args = [MC, eff]))

                            "Your brothel's reputation has increased slightly."

                            $ brothel.change_rep(r-6)

                        elif r >= 7:

                            you "Good people, we are so thankful to have you here..."

                            "The customers are hardly paying attention to you. You manage to get a few words out, but quickly sense this crowd is not interested in what you have to say tonight."

                            you "All right, thanks for listening. Everybody have fun!"

                            "Your brothel's reputation has increased slightly."

                            $ brothel.change_rep(r-6)

                        else:

                            you "I, uh, I would like to introduce myself..."

                            play sound s_crowd_boos

                            "The front rows boo and yell for you to get lost. It seems without a pair of boobs, you cannot get anyone's attention in this crowd."

                            you "My name is [MC.name] and, uh, I would like to thank all the good people that made this possible... First, my parents..."

                            man "Shut the fuck up!"

                            "Other man" "Go away!!!"

                            play sound s_dodge

                            pause 0.5

                            play sound2 s_dodge

                            "The customers start throwing all sorts of garbage on stage, and an empty pint hits you square in the forehead."

                            play sound s_punch

                            with vpunch

                            you "Ouch!"

                            "You retreat backstage with your head swollen and your pride hurt. {nw}"

                            if girl.is_("dom") and girl.love < 50:
                                extend "You hear [girl.name] laughing with the crowd as they make fun of you."

                                "[girl.fullname]'s obedience skill has decreased."

                                $ girl.change_stat("obedience", -1*(dice(3)+2))

                            else:
                                extend "[girl.name] follows you and helps you with your wound."

                                "[girl.fullname]'s sensitivity skill has increased."

                                $ girl.change_stat("sensitivity", (dice(3)+2))

                            "Your brothel's reputation has decreased slightly."

                            $ brothel.change_rep(r-7)


                    "Make [girl.name] perform in front of the crowd":
                        menu:
                            "What do you want her to do?"
                            "Tell her to give the customers a swimsuit show":
                                $ selected_act = "naked"
                                $ fix = "wet"

                            "Tell her to give the customers a cosplay show":
                                $ selected_act = "naked"
                                $ fix = "cosplay"

                            "Tell her to give the customers a sex toy show":
                                $ selected_act = "naked"
                                $ fix = "vibrators"

                        $ attitude = girl.get_sex_attitude(selected_act, fix = ["public acts"] + [fix])

                        call night_girl_perform() from _call_night_girl_perform_9


                    "Have sex with [girl.name] on stage":

                        menu:
                            "What do you want her to do?"
                            "Give you a blowjob":
                                $ selected_act = "service"
                                $ fix = rand_choice(["cum on face", "cum in mouth"])
                                $ attitude = girl.get_sex_attitude(selected_act, fix = ["public acts"] + [fix]) + girl.get_love()

                                "Joining [girl.fullname] on stage, you place a friendly hand around her shoulder and whisper in her ear."

                                you "Follow my lead babe, we're going to give them a good show."

                                $ l = girl.get_love()
                                $ f = girl.get_fear()

                                if l > f:
                                    if l > 75:
                                        $ text1 = "充满崇拜"
                                    elif l > 50:
                                        $ text1 = "充满爱意"
                                    elif l > 25:
                                        $ text1 = "充满古怪"
                                    else:
                                        $ text1 = "充满好奇"
                                else:
                                    if f > 75:
                                        $ text1 = "充满恐惧"
                                    elif f > 50:
                                        $ text1 = "充满惊恐"
                                    elif f > 25:
                                        $ text1 = "充满不安"
                                    else:
                                        $ text1 = "充满困惑"


                                "She gives you [text1] look."

                                "Taking her hand, you guide it towards your pants, making her rub your dick over the fabric."

                                play sound s_surprise

                                girl.char "Uh? *gasp*"

                                "Unbuttoning your pants, you free your hard cock, wrapping her hand around it. You motion for her to get down."

                                if attitude > 100:
                                    "Understanding your request, she smiles and licks her lips."

                                    girl.char "Oh, of course Master... I was just beginning to feel hungry for your cock..."

                                elif attitude > 0:
                                    "She knows what she's supposed to do."

                                    girl.char "Yes, Master..."

                                else:
                                    "She looks shocked and flat-out refuses."

                                    girl.char "What? No! Everybody's watching! What are you thinking?"

                                    you "That's the point, girl! You must do what you're told..."

                                    if girl.get_stat("obedience") < 100:

                                        play sound s_scream

                                        girl.char "No!!!"

                                        call fight_attempt(girl, "service", 2) from _call_fight_attempt_7

                                        if _return:
                                            call hide_everything() from _call_hide_everything_24
                                            scene black with dissolve
                                            "[girl.fullname] ran away."
                                            return

                                        girl.char "Oh, please, no... *sob*"

                                    else:
                                        girl.char "Aw... I understand... *frown*"

                            "Fuck her on stage":
                                $ selected_act = "sex"
                                $ fix = rand_choice(["public acts", "doggy style", "piledriver"])
                                $ attitude = girl.get_sex_attitude(selected_act, fix = ["public acts"] + [fix]) + girl.get_love()

                                if fix == "public acts":
                                    you "I am going to teach you a lesson, right here in front of everybody. Take off your clothes."
                                elif fix == "doggy style":
                                    you "Take off your panties, turn around, and put your hands against the wall. I'm going to teach you a little lesson..."
                                elif fix == "piledriver":
                                    you "Lay down on the ground, and take off your panties. I'm going to give you a good pounding."

                                if girl.get_stat("obedience") < 150:
                                    girl.char "What? No!!! Stop!"

                                    call fight_attempt(girl, selected_act, 3) from _call_fight_attempt_8

                                    if _return:
                                        call hide_everything() from _call_hide_everything_25
                                        scene black with dissolve
                                        "[girl.fullname] ran away."
                                        return

                                    "Ignoring her pleading, you grab her panties and tear them off."
                                    you "Let me teach you to obey using a language your pussy will understand...."

                                else:
                                    girl.char "... Yes, Master."
                                    "She slowly removes her panties, exposing her pink pussy."

                            "Fuck her ass on stage":
                                $ selected_act = "anal"
                                $ fix = rand_choice(["cowgirl", "piledriver", "spooning"])
                                $ attitude = girl.get_sex_attitude(selected_act, fix = ["public acts"] + [fix]) + girl.get_love()

                                "Joining [girl.name] on stage, you grab her ass from behind."

                                play sound s_surprise

                                girl.char "Oh! Master! What are you doing?"

                                if not girl.naked:
                                    you "Take all of your clothes off... We're going to have some fun in front of the customers."
                                else:
                                    "Fondling her naked butt, you start rubbing your crotch against it."

                                if girl.get_stat("obedience") < 175:
                                    girl.char "What? No!!! Stop!"

                                    call fight_attempt(girl, selected_act, 3) from _call_fight_attempt_9

                                    if _return:
                                        call hide_everything() from _call_hide_everything_26
                                        scene black with dissolve
                                        "[girl.fullname] ran away."
                                        return

                                    girl.char "Oh no... Please, don't hurt me..."

                                else:
                                    girl.char "Oh... I understand..."


                        call night_girl_perform() from _call_night_girl_perform_10

            "Leave":
                you "Looks like things are getting off to a good start. Let them have their fun."

        stop sound
        call hide_everything() from _call_hide_everything_27
        scene black with dissolve


    ### ONSEN ###

    elif room == "onsen":

        "Before [brothel.name]'s big opening, you run a last check on the {b}onsen{/b}, making sure everything is ready for the customers."

        $ renpy.show(room, at_list = [top])

        you "Every thing seems to be in order... Wait, who's that?"

        $ pic = girl.get_pic("masseuse", and_tags=["rest"], naked_filter=True, soft=True)
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        "You spot [girl.fullname] lazily bathing in one of the pools. As you approach, you can even hear her snore noisily."

        you "Slacking off on the job, uh..."

        label onsen_night_event_menu():

            menu:
                "What do you do?"

                "Remove her towel" if not girl.naked:
                    "She is wearing nothing but a bath towel. You decide removing it while she sleeps should be a good prank."

                    $ r = MC.get_speed() + dice(6)

                    if r >= 8:
                        $ girl.naked = True
                        $ pic = girl.get_pic("masseuse", and_tags=["naked", "rest"], soft=True)
                        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                        with dissolve

                        "Without her noticing, you remove her towel, revealing her juicy naked body."

                        jump onsen_night_event_menu

                    else:
                        "As you reach for her towel to remove it, she stirs in her sleep. Opening her eyes, she is startled to see you hovering over her."
                        jump onsen_night_event_wake_up

                "Wake her up":
                    you "Hey... [girl.name]..."

                    if MC.get_alignment() == "good":
                        "You stroke her arm gently."
                    elif MC.get_alignment() == "evil":
                        "You pull at her hair, brutally yanking her head backwards."
                    else:
                        "You squeeze her shoulder, shaking her out of her slumber."

                    label onsen_night_event_wake_up():

                        girl.char "Uwah!"

                        you "Hey, sleepyhead... Work is about to begin!"

                        girl.char "M-Master? Uh? What time is it? I'm so late!!! What should I do?"

                        menu:
                            "Send her off":
                                you "You know what you have to do. Run off to work, the customers are coming in as we speak."

                                if girl.naked:
                                    girl.char "B-But, Master! I'm naked..."

                                    you "Well, there's no time for you to get dressed now. I'm sure it's not gonna be a problem for the customers."

                                girl.char "Aw..."

                            "Scold her":
                                you "What do you think you're doing! Falling asleep on the job! Get your ass moving, and go to work."

                                girl.char "B-But..."

                                you "Now!"

                                girl.char "Aw..."

                                $ changed_stats = [("obedience", 1), ("mood", -2)]

                            "Request a massage":
                                you "Well, since we're here, you might as well give me a massage... I need to, err, inspect your technique."

                                if girl.naked:
                                    girl.char "A massage? Like this? I'm naked... *blush*"

                                    you "Of course. We need to have a real body to body experience..."

                                girl.char "Oh... I see..."

                                $ pic = girl.get_pic("masseuse", and_tags=["rest"], naked_filter=True, soft=True)
                                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                                with dissolve

                                "[girl.fullname] starts massaging you as you lay down on a bath towel."

                                girl.char "Master... Is it good?"

                                you "Yes, keep going..."

                                "She massages your shoulders, your back, then your legs, working her way up to your thighs."

                                $ r = girl.get_stat("libido") + girl.get_love()

                                if r > 150:
                                    "Her breath accelerates, her touch becomes more sensual, and she starts massaging your buttocks and caressing your inner thighs."

                                    you "That's good..."

                                    "Slipping her hand between your legs, she begins stroking your balls and your manhood."

                                    girl.char "Oh, Master... You're so hard already..."

                                elif r > 75:
                                    "She hesitates about the next step now. You urge her on."

                                    you "Come on girl. We're not finished yet."

                                    "You turn over to be on your back. [girl.name] gasps when she sees your erect member."

                                    girl.char "Master..."

                                else:
                                    "Clumsily, [girl.name] carefully avoids touching you anywhere near your private parts. She moves back to your ankle, then calls it a day."

                                    girl.char "All right, Master, it's over..."

                                    you "Over? We're not done yet!"

                                    play sound s_surprise

                                    girl.char "Uh?"

                                menu:
                                    "Ask for a handjob":
                                        $ selected_act = "service"
                                        $ fix = "handjobs"

                                        "Reaching for a bottle of massage oil, you instruct her to use some on your erect cock."

                                        if girl.get_stat("obedience") < 50:
                                            girl.char "Master, no... I won't do that..."

                                            call fight_attempt(girl, "service", 1) from _call_fight_attempt_10

                                            if _return:
                                                call hide_everything() from _call_hide_everything_28
                                                scene black with dissolve
                                                "[girl.fullname] ran away."
                                                return

                                            "You give her a cold stare."
                                            you "I am the one giving orders here."

                                            girl.char "Aw..."

                                        else:
                                            girl.char "Of course, Master..."

                                        call night_girl_perform() from _call_night_girl_perform_11

                                    "Ask for a titjob":
                                        $ selected_act = "service"
                                        $ fix = "titjobs"

                                        "Grabbing her tits, you start rubbing them together, then pull her body towards your dick."

                                        play sound s_aaah

                                        if girl.get_stat("obedience") < 75:
                                            girl.char "Master, no... I won't do that..."

                                            call fight_attempt(girl, "service", 1) from _call_fight_attempt_11

                                            if _return:
                                                call hide_everything() from _call_hide_everything_29
                                                scene black with dissolve
                                                "[girl.fullname] ran away."
                                                return

                                            "You give her a cold stare."
                                            you "I am the one giving orders here."

                                            girl.char "Aw..."

                                        else:
                                            girl.char "Yes, Master."

                                        call night_girl_perform() from _call_night_girl_perform_12

                                    "Ask for a blowjob":
                                        $ selected_act = "service"
                                        $ fix = "oral"

                                        "Pointing at your hard dick, you tell her to use her mouth and finish what she started."

                                        if girl.get_stat("obedience") < 75:
                                            girl.char "Master, no... I won't do that..."

                                            call fight_attempt(girl, "service", 1) from _call_fight_attempt_12

                                            if _return:
                                                call hide_everything() from _call_hide_everything_30
                                                scene black with dissolve
                                                "[girl.fullname] ran away."
                                                return

                                            "You give her a cold stare."
                                            you "I am the one giving orders here."

                                            girl.char "Aw..."

                                        else:
                                            girl.char "Yes, Master."

                                        call night_girl_perform() from _call_night_girl_perform_13


                                    "Ask for sex":
                                        $ selected_act = "sex"
                                        $ fix = "cum inside"

                                        you "I expect you to give me full service tonight. You understand?"

                                        if girl.get_stat("obedience") < 100:
                                            girl.char "Master, no... I can't do that..."

                                            call fight_attempt(girl, "sex", 2) from _call_fight_attempt_13

                                            if _return:
                                                call hide_everything() from _call_hide_everything_31
                                                scene black with dissolve
                                                "[girl.fullname] ran away."
                                                return

                                            "You give her a cold stare."
                                            you "I am the one giving orders here."

                                            girl.char "Aw..."

                                        else:
                                            girl.char "Of course, Master..."

                                        call night_girl_perform() from _call_night_girl_perform_14

                                    "Leave it at that":
                                        you "That's enough for today. Now, you've got customers to attend."
                                        $ changed_stats = [("obedience", dice(3)), ("sensitivity", dice(3))]

                "Tease her while she's sleeping":

                    menu:
                        "Tickle her":
                            "Reaching from behind her, you start tickling her under her armpits."

                            play sound s_surprise
                            with vpunch

                            girl.char "Uwaah!!!"

                            "Shaken out of her slumber, [girl.name] slips down in the bath water, confused and nearly drowning."

                            play sound s_splash

                            pause 0.5

                            play sound s_screams

                            girl.char "Waah! *glub* *glub*" with vpunch

                            "Splashing around for dear life, it takes a moment for her to realize she is only in a few feet of water."

                            "Eventually, she comes to her senses, and she notices you. She looks like a wet puppy, and the face she makes is so comical that you can't help but laugh out loud."

                            girl.char "YOU..."

                            if girl.is_("dom"):
                                "Looking very mad, she grits her teeth, her fists balled as if she's about to fight you..."

                                "But suddenly she seems to think of something and her expression changes to a mischevious smile."

                                girl.char "Oh, Master... Come over here, will you... ♥"

                                "Grabbing your leg, she pulls you in the water, and you slip with all your clothes on inside the hot bath with a big splash."

                                play sound s_splash

                                you "HAAA!!!" with vpunch

                                "Cursing, you come out gasping for air. It's [girl.name]'s turn to laugh."

                                play sound s_laugh

                                girl.char "Teeheehee! *giggle*"

                                "Seeing how stupid the situation is, you both start laughing uncontrollably. The customers are surprised to find you both soaking in the onsen bath, wondering what the hell is going on."

                                $ girl.change_love(2)

                            else:
                                "She almost cries as she sees you making fun of her. Blushing bright red, holding her arms wrapped around her body, she bursts out."

                                girl.char "You're... You're mean!!!"

                                "Flipping around, she exits the bath, running dangerously across the slippery floor. You wonder if maybe you went too far."

                                $ girl.change_love(-2)


                        "Grope her breasts":

                            if girl.naked:
                                "Reaching from behind her, you grab and squeeze her naked breasts."
                            else:
                                "Reaching from behind her, you slip your hands under her towel, grabbing and squeezing her tits."

                            play sound s_surprise
                            with vpunch

                            girl.char "Aaah!"

                            $ pic = girl.get_fix_pic(fix=fix_dict["fondling her boobs"], and_tags=["swimsuit", "masseuse"], naked_filter=True, not_tags=all_sex_acts + ["group", "bisexual"])

                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                            with fade

                            "Waking up suddenly, [girl.name] is startled at first, not knowing what the hell is happening."

                            girl.char "What... Hey!!!"

                            "She stares down and sees your hands, busy fondling her exposed tits. She moans as you pinch her nipples hard."

                            $ attitude = girl.get_sex_attitude("naked", "fondling her boobs") + girl.get_love()

                            if attitude > 100:

                                play sound s_moans_quiet

                                "Saying nothing, [girl.name] watches as you play with her boobs like putty."

                                girl.char "Oh, Master... Aaaaah!"

                                "She blushes more and more, her moaning becoming more urgent as you fondle and rub her tits."

                                girl.char "Mmmmh..."

                                "You can feel her body become hot, and it's not just because of the onsen. As you squeeze and pull on her nipples, she closes her eyes and bites her lip."

                                girl.char "Oh, Master... Aaaaah!!!"

                                play sound s_orgasm_fast
                                with flash

                                "[girl.name] cums unexpectedly, just from feeling her boobs being groped. You smile as her sensitive body is rocked by a wave of pleasure."

                                you "Good girl... All right now, get down to work."

                                girl.char "..."

                                $ changed_stats = [("sensitivity", 2+dice(3)), ("service", dice(3))]
                                $ girl.change_love(3)

                            elif attitude > 0:

                                play sound s_moans_quiet

                                girl.char "Master... Aaaah... What are you doing!"

                                "Even though she complains, she doesn't move to stop you. You tease her by rubbing her nipples, and she blushes bright red, breathing softly."

                                girl.char "Master... Please stop... Someone will see us..."

                                "She looks around, worried, as the customers start pouring into the onsen. They still haven't noticed you."

                                you "Don't worry... I bet the customers would love to see how perverted your tits are..."

                                play sound s_surprise

                                girl.char "Oh, Master! Don't say that! Aaaah..."

                                "After teasing her for a while, you decide to tend to other matters and let go of her boobs."

                                girl.char "..."

                                "She watches you leave with a mix of relief and regret."

                                $ changed_stats = [("sensitivity", dice(3)), ("service", dice(3))]
                                $ girl.change_love(1)

                            else:

                                play sound s_screams

                                girl.char "Let go of me!!! You pervert!!!" with vpunch

                                play sound s_splash

                                "She splashes water around wildly, trying to shake you off."

                                you "Falling asleep on the job, uh? Let me punish your perverted titties for your carelessness!"

                                girl.char "Nooo!!! Stop touching me!!!"

                                "Squeezing hard on her tits, pinching her nipples, you only elicit cries of pain and curses out of her."

                                girl.char "AAAH!!! LET ME GO!!!"

                                "After a little while, you think she has been punished enough. Reluctantly, you let go of her soft boobs, leaving her feeling hurt and humiliated."

                                $ changed_stats = [("sensitivity", -1*dice(3)), ("service", -1*dice(3))]
                                $ girl.change_love(-2)


                        "Wake her up with a special 'shower'":

                            menu:
                                "What do you have in mind?"

                                "Cum in her hair":
                                    $ selected_act = "fetish"
                                    $ fix = "cum in hair"

                                "Pee on her":
                                    $ selected_act = "fetish"
                                    $ fix = "watersports"

                                "Give her a cum shower":
                                    $ selected_act = "group"
                                    $ fix = "cum shower"

                                "Never mind":
                                    jump onsen_night_event_menu

                            call night_girl_perform() from _call_night_girl_perform_15


                "Leave her alone":
                    you "Well, good for her. Everyone needs to relax every once in a while."

                    $ girl.change_energy(10)


            stop sound
            call hide_everything() from _call_hide_everything_32
            scene black with dissolve

    ### OKIYA ###

    elif room == "okiya":
        "You mix in with the customers as they pour into the {b}okiya{/b}."

        $ renpy.show(room, at_list = [top])

        "Those are not the usual riff-raff: they style themselves as gentlemen, looking for refinement and the more elevated pleasures to be found in your whorehouse, such as that of good company."

        if girl.naked:
            $ text1 = "像她出生那天一样赤身裸体"
        else:
            $ text1 = "穿着朴素的奴隶服"

        "Speaking of which, you realize none of the geishas are ready to greet the customer yet. You only see [girl.fullname], walking across the tatami floor [text1]."

        show screen show_event(girl.get_pic("profile", not_tags=["geisha", "swim", "beach"], naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        you "Hey! [girl.name]!"

        girl.char "Uh? Master?"

        you "What do you think you're doing? There are customers coming in already. You must greet and tend to them."

        if girl.job != "geisha":
            girl.char "B-But, Master! I don't even work as a geisha! I was just passing by here..."

        else:
            girl.char "B-But, Master, I am not ready yet! I need more time..."

        menu:
            "What do you do?"

            "Tell her to get prepared":
                you "Well, don't just stand there, then! Go to the cloakroom and change. I'll help you."

                girl.char "But... *blush*"

                if girl.naked:
                    "You lead [girl.name] to the cloakroom, telling her to stay put while you look for a suitable outfit."
                else:
                    "You lead [girl.name] to the cloakroom, telling her to undress while you fetch her a more elegant outfit."

                    play sound s_dress

                show screen show_event(girl.get_pic("strip", "naked", and_tags = ["profile"], not_tags=["geisha"], and_priority=False, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with fade

                girl.char "So... What should I be wearing? *blush*"

                you "All right, let me think..."

                menu:
                    "Wear this."

                    "Give her a fancy dress":

                        "You hand her a nice set of clothes and help her with the complex ties that are necessary for it to hold properly."

                        play sound s_dress

                        "Doing so, you involuntarily brush your hands against her exposed skin, and she blushes even more. You can feel her shiver under the soft caress of the silky fabric."

                        girl.char "..."

                        play sound s_dress

                        $ pic = girl.get_pic("geisha", naked_filter=True, soft=True)
                        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                        with fade

                        $ MC.rand_say(("gd: 就这样吧。你现在看起来很棒。我相信顾客会喜欢你的。", "ne: 好吧，你看起来很不错。去吧，取悦顾客让他们满意吧。", "ev: 嗯哼。不错，你看起来几乎像真的一样。去吧，给那些容易受骗的傻瓜长点记性。"))

                        girl.char "Thanks..."

                        "[girl.fullname] hurries out to greet the customers."

                    "Give her ropes":

                        $ selected_act = "fetish"
                        $ fix = "bondage"

                        "You show her a stack of knotted ropes, made of tough, rugged yarn."

                        you "Here, this is going to be your suit for the night. I'm sure this will suit you just right..."


                        if girl.is_("dom"):
                            play sound s_surprise
                            girl.char "*gasp* You're... You're kidding, right?"
                            you "I am most certainly not. Don't worry, I'll help you tie it up. Come here."

                        elif girl.is_("sub"):
                            girl.char "..."
                            you "Now, let me help you put this on. It needs to be very tight..."

                        call night_girl_perform() from _call_night_girl_perform_16

                    "Give her a gag":

                        $ selected_act = "fetish"
                        $ fix = "gags"

                        "Taking out a gag from your toolbag, you move to place it over her mouth."

                        play sound s_surprise

                        girl.char "Wait! Ngggh!"

                        "Before she can speak another word, you stuff the gag inside her mouth, tying it behind her head."

                        call night_girl_perform() from _call_night_girl_perform_17

                    "Give her an anal plug":

                        $ selected_act = "fetish"
                        $ fix = "plugs"

                        "Smirking, you take out a single item out of your toolbag."

                        you "Here, wear this."

                        girl.char "Wait... You don't mean..."

                        you "Oh, yes..."

                        if girl.get_stat("obedience") < 75:

                            call fight_attempt(girl, "fetish", 1) from _call_fight_attempt_14

                            if _return:
                                call hide_everything() from _call_hide_everything_33
                                scene black with dissolve
                                "[girl.fullname] ran away."
                                return
                            else:
                                "Looking unhappy, [girl.name] nevertheless knows better than to defy you."

                        else:
                            play sound s_sigh

                            girl.char "Well, Master, if I have to... *sigh*"

                        "On your instructions, [girl.name] bends over forward, spreading her buttcheeks. After dipping the butt plug into a bowl of warm oil, you slip it inside her asshole."

                        play sound s_scream

                        girl.char "Aaaah!!!"

                        call night_girl_perform() from _call_night_girl_perform_18



            "Tell her to hold a special ceremony" if girl.job == "geisha":
                you "Quick, get in your geisha clothes. Meet me here as soon as you are ready, I'll warm up the crowd."

                girl.char "Oh... Are you sure?"

                you "Of course! Get moving."

                "[girl.name] rushes off to get changed, while you turn to greet the customers."

                you "Welcome, my dear friends, to our outstanding establishment. I am sure you will find the skills of our girls to be unrivaled in all of Xeros."

                man "Some boast, here, Master [MC.name]! What are those girls of yours capable of that we haven't seen before?"

                you "Well..."

                "[girl.name] joins you right on time to announce the show, all suited up as a geisha. You think about the more unusual plays you know. Which one could placate this snotty audience?"

                $ bead_pic = girl.get_pic("beads", and_tags=["geisha"])
                $ fist_pic = girl.get_pic("fist", and_tags=["geisha"])
                $ milk_pic = girl.get_pic("lactation", and_tags=["geisha"])
                $ enema_pic = girl.get_pic("enema", and_tags=["geisha"])

                menu:
                    "Which show do you want [girl.name] to put on display?"

                    "The Singing Carp (Traditional music and singing)":
                        you "Our graceful host, Lady [girl.fullname], will now tell you the sad story of a most remarkable fish..."

                        play sound s_sigh

                        girl.char "Yes, Master."

                        show screen show_event(girl.get_pic("sing", and_tags=["geisha"], soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                        with fade

                        "[girl.char] brings out a traditional instrument called a koto, which she places in front of the audience."

                        "After playing a few notes, she starts singing with a plaintive voice."

                        girl.char "Let the gods lead my hands on mine harp, to tell you the story of a singing carp..."

                        $ result = (2*girl.get_stat("refinement") + girl.get_stat("charm"))/3

                        if result > 125:
                            "Singing in a melodic voice, [girl.char] enthralls the customers with her skill and charisma."

                            play sound s_crowd_cheer

                            "When she is finished, the customers applaud her for a long time, many of them crying with emotion."

                            $ brothel.change_rep(girl.rank*2)
                            $ changed_stats = [("refinement", 2+dice(3))]

                            "Your brothel reputation has increased."

                        elif result > 50:
                            "She does make a few mistakes, but acts charmingly as if nothing happened, and in the end, most customers don't notice."

                            "The customers thought it was a satisfying show."

                            $ brothel.change_rep(girl.rank)
                            $ changed_stats = [("refinement", dice(3))]

                            "Your brothel reputation has increased slightly."

                        else:
                            "It seems she has no talent for singing, and her other skills aren't doing much to help. In the middle of the song, she stops, having forgotten the lyrics."

                            play sound s_crowd_boos

                            "The customers are unhappy with the poor performance and leave grumbling."

                            $ brothel.change_rep(-1*girl.rank)
                            $ changed_stats = [("refinement", -1)]

                            "Your brothel reputation has decreased."

                    "The Ghost Lady (Traditional dance and theater)":

                        you "Our very own [girl.fullname] will now execute the dance of the Ghost Lady, longing for her lover to return."

                        play sound s_sigh

                        girl.char "Yes, Master."

                        $ pic = girl.get_pic("dance", and_tags=["geisha"], soft=True)
                        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                        with fade

                        "The customers sit in a circle on the tatami floor, as [girl.name] takes her position in the center, ready to start her dance."

                        "Taking a fiddle, you start playing a sorrowful tune, as [girl.name] slowly waves her arms and legs in a hypnotic dance."

                        girl.char "Oh, my lover, where are thee? How my sinful body longs for thy warm embrace..."

                        $ result = (2*girl.get_stat("refinement") + girl.get_stat("body"))/3

                        if result > 125:
                            "Whirling around, [girl.name] seems uncannily just like the ethereal apparition she is playing. Floating around sensually, moaning like the horny ghost lusting for her departed love, she starts shedding her clothes one by one."

                            play sound s_dress

                            $ pic = girl.get_pic("dance", and_tags=["naked", "strip"], soft=True)
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                            with dissolve

                            "She ends up dancing naked as the day she was born. She is so into her performance that she doesn't even seem to notice."

                            "Finally, as the ghost vanishes with the sunlight, she lays down to the floor with a dramatic moan, her naked breasts heaving as she catches her breath."

                            play sound s_crowd_cheer

                            "The customers give her a standing ovation, heaping roses over her naked body to express their appreciation."

                            $ brothel.change_rep(girl.rank*2)
                            $ changed_stats = [("refinement", 2+dice(3))]

                            "Your brothel reputation has increased."

                        elif result > 50:
                            "She seems a bit stiff at first, but finds her footing, dancing around the okiya like a fickle wisp."

                            "As you increase the pace of your fiddling, she bounces around madly, letting out a plaintive cry."

                            "The customers thought it was a fine show, if a little too {i}avant-garde{/i} for their taste."

                            $ brothel.change_rep(girl.rank)
                            $ changed_stats = [("refinement", dice(3))]

                            "Your brothel reputation has increased slightly."

                        else:
                            "She prances around aimlessly, her idea of a dance, perhaps."

                            girl.char "O lover, I long to fall in your arms... Aaaaah!!!"

                            with vpunch
                            play sound s_crash

                            "Pretending to fall backwards, she loses her balance and comes down crashing into a party of customers, spilling their bottles of expensive sake everywhere."

                            man "The fuck!!!"

                            girl.char "Uh... I'm sorry..."

                            play sound s_crowd_boos

                            "The customers are pissed off and leave."

                            $ brothel.change_rep(-1*girl.rank)
                            $ changed_stats = [("refinement", -1)]

                            "Your brothel reputation has decreased."

                    "Legend of The Seven Pearls (Erotic show featuring anal beads)" if bead_pic:
                        $ selected_act = "fetish"
                        $ fix = "beads"

                        "Handing a string of pearls to [girl.name], you turn to address the gathering."

                        you "Let me tell you of the legend of the Seven Magical Pearls. A long time ago, in a whorehouse far, far away..."

                        if girl.get_stat("obedience") < 125:

                            call fight_attempt(girl, "fetish", 1) from _call_fight_attempt_15

                            if _return:
                                call hide_everything() from _call_hide_everything_34
                                scene black with dissolve
                                "[girl.fullname] ran away."
                                return
                            else:
                                "[girl.name] is shocked by your request, but knows she mustn't make a scene in front of the customers."

                        else:
                            play sound s_sigh

                            girl.char "Oh..."

                    "The Howling Banshee (Erotic show featuring fisting)" if fist_pic:
                        $ selected_act = "fetish"
                        $ fix = "fisting"

                        if girl.get_stat("obedience") < 150:

                            call fight_attempt(girl, "fetish", 3) from _call_fight_attempt_16

                            if _return:
                                call hide_everything() from _call_hide_everything_35
                                scene black with dissolve
                                "[girl.fullname] ran away."
                                return
                            else:
                                "[girl.name] is shocked by your request, but knows she mustn't make a scene in front of the customers."

                        else:
                            play sound s_surprise

                            girl.char "B-But, Master, that one is..."

                        you "Anyway. Our lady friend [girl.fullname] will now sing us a traditional song from the woodlands, the complaint of the howling banshee."

                        "You hand her a sheet of music. Hesitantly, [girl.name] starts singing about the troubled spirit of the woods."


                    "The Most Unusual Tale of Molly, the Dairy Cow (Erotic show featuring lactation)" if milk_pic:
                        $ selected_act = "fetish"
                        $ fix = "lactation"

                        if girl.get_stat("obedience") < 100:

                            call fight_attempt(girl, "fetish", 1) from _call_fight_attempt_17

                            if _return:
                                call hide_everything() from _call_hide_everything_36
                                scene black with dissolve
                                "[girl.fullname] ran away."
                                return
                            else:
                                "[girl.name] is shocked by your request, but knows she mustn't make a scene in front of the customers."

                        else:
                            play sound s_surprise

                            girl.char "That one? B-but... It's humiliating..."

                        you "Don't be such a crybaby."

                        "Opening your toolbag, you take out a long syringe, full of a mysterious liquid. Ripping [girl.name]'s top open to free her breasts, you stick the syringe right into her nipple."

                        play sound s_surprise

                        girl.char "Wait! Aaah!!!"

                    "The Secret Spring Behind The Forbidden Gate (Erotic show featuring an enema)" if enema_pic:
                        $ selected_act = "fetish"
                        $ fix = "enemas"

                        "You smile mischievously as you take out a giant syringe-shaped metal tube and proceed to fill it with a strange yellow liquid from a bucket."

                        if girl.get_stat("obedience") < 125:

                            call fight_attempt(girl, "fetish", 2) from _call_fight_attempt_18

                            if _return:
                                call hide_everything() from _call_hide_everything_37
                                scene black with dissolve
                                "[girl.fullname] ran away."
                                return
                            else:
                                "[girl.name] looks in shock, but she knows she must do as she is told."

                        else:
                            play sound s_surprise

                            girl.char "Oh no..."

                        you "Once upon a time, there were twelve forbidden gates. The first one..."

                        man "Oh, shut up."

                        "Other man" "Yeah, cut it with the crappy story, we want to see the show!"

                        you "B-but... This is part of the show! This is art!"

                        play sound s_crowd_boos

                        "The impatient customers boo you."

                        you "Fine then... You barbarians..."

                        "Moving on with the show, you tell [girl.name] to go down on all fours, lifting her dress to expose her naked butt."

                if selected_act:
                    call night_girl_perform() from _call_night_girl_perform_19




            "Let her go":
                if girl.job != "geisha":
                    you "All right, you can go then. But tell the geishas to hurry up and come here. I don't want the customers waiting."
                else:
                    you "All right, hurry up then. Don't leave the customers alone for long. {nw}"

                    if dice(3) == 3:
                        extend "They might be fancy, but I'm sure some of them are apt to take off with the silverware."
                    else:
                        extend ""


    ### RESULTS ###

    ## Discovering and raising preferences

    if selected_act:
        $ girl.test_weakness(selected_act, unlock=True, feedback=True)
        $ girl.raise_preference(selected_act, bonus=intensity)

        if selected_act != "naked":
            $ MC.change_prestige(girl.rank)
            "You have earned prestige."

    if selected_fix:
        $ result = girl.test_fix(selected_fix.name, unlock=True, feedback=True)

        if not punish and attitude == None:
            bk_error "Couldn't find an attitude value for act: [selected_act] and fix: [selected_fix.name]"

        elif attitude > 150:
            $ changed_stats.append(("libido", dice(6)+4))
            if rep_impact:
                $ brothel.change_rep(intensity*girl.rank*2)
                "Your brothel reputation has increased a lot."

        elif attitude > 100:
            $ changed_stats.append(("libido", dice(3)+2))
            if rep_impact:
                $ brothel.change_rep(intensity*girl.rank*2)
                "Your brothel reputation has increased."

        elif attitude > 0:
            if rep_impact:
                $ brothel.change_rep(intensity*girl.rank)
                "Your brothel reputation has increased slightly."

        else:
            $ changed_stats.append(("libido", -1*dice(3)-2))
            if rep_impact:
                $ brothel.change_rep(-1*intensity*girl.rank)
                "Your brothel reputation has decreased slightly."

    # Changing stats

    if changed_stats:

        python:
            for stat, value in changed_stats:
                girl.change_stat(stat, value)
                if value > 5:
                    renpy.say("", "[girl.name]的[stat]技能大幅提升。")
                elif value > 2:
                    renpy.say("", "[girl.name]的[stat]技能提升了。")
                elif value > 0:
                    renpy.say("", "[girl.name]的[stat]技能略有提升。")
                elif value < -5:
                    renpy.say("", "[girl.name]的[stat]技能大幅下降。")
                elif value < -2:
                    renpy.say("", "[girl.name]的[stat]技能下降了。")
                elif value < 0:
                    renpy.say("", "[girl.name]的[stat]技能略有下降。")

    return


#### GIRL PERFORM ####

label night_girl_perform():

    # Chooses an additional tag for working girls
    if room == "tavern":
        $ and_tag = ["waitress"]
    elif room == "strip club":
        $ and_tag = ["dancer"]
    elif room == "onsen":
        $ and_tag = ["masseuse"]
    elif room == "okiya":
        $ and_tag = ["geisha"]
    else:
        $ and_tag = []

    $ selected_fix = fix_dict[fix]

    if fix == "kissing":
        $ pic = girl.get_fix_pic(fix=selected_fix, and_tags=and_tag, not_tags=extended_sex_acts)

        you "Come over here."

        girl.char "Y-Yes? *blush*"

        "Surprising her, you lean in for a kiss."

        play sound s_sucking
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        $ attitude = girl.get_sex_attitude(fix="kissing") + girl.get_love() - girl.get_fear()

        if attitude >= 100:
            $ changed_stats = [("sensitivity", dice(3)+2), ("obedience", dice(3)+2)]
            play sound2 s_mmh
            girl.char "Hmmm... Aaaah..."

            "She kisses you back intently, and soon you are both locked in a wet, tongue-twisting kiss."

            girl.char "Hnn, hnnn..."

            "After a few minutes of passionate kissing, [girl.name] opens her eyes wide and she moans suddenly, as she she is rocked by a surprise orgasm."

            play sound s_orgasm_fast

            girl.char "Haa, haaaaa!!!"
            $ girl.change_love(3)

        elif attitude >= 0:
            $ changed_stats = [("sensitivity", dice(3)), ("obedience", dice(3))]
            play sound2 s_ahaa
            girl.char "Hnnn..."

            "She is startled by your move, but after a moment she relaxes, closes her eyes and starts to respond to your kiss."

            you "That's it... Hmmm..."

            "You kiss her for a while, showing her some tongue techniques, before letting her go."

            girl.char "Th... Thank you Master... *blush*"

            $ girl.change_love(2)

        else:
            $ changed_stats = [("sensitivity", dice(3)), ("obedience", -1*dice(3))]
            play sound2 s_surprise
            girl.char "Ngg!!!"

            "[girl.name] tries to push you back, but you grab the back of her head and lock into another kiss with her."

            you "Stay put."

            "You force your tongue inside her mouth, taking your time as she struggles weakly to break away."

            "After a while, you stop, letting her go. She frowns, but seems relieved that you didn't go farther."
            $ girl.change_love(1)

        you "All right, that was fun... Now, get to work."

    elif fix == "69":
        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["group", "bisexual", "cumshot"])
        $ changed_stats = [("service", dice(3)+2), ("libido", dice(3)+2)]

        girl.char "You came here to inspect me, I think... Let me inspect you too..."

        "Purring, she moves on top of you, spreading her legs above your face. She reaches inside your pants at the same time, freeing your dick."

        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        play sound s_mmmh

        girl.char "Hmmm, it's already nice and hard... *gulp*"

        play sound s_sucking

        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        "With obscene noises, she starts licking and sucking your dick."

        girl.char "Sho delishious... Hnnn..."

        if girl.naked:
            "You can't resist her naked, wet pussy, hanging only an inch from your face. You bury your tongue inside her slit."
        else:
            "You feel obliged to reciprocate. Swiping aside her panties, you slide your tongue inside her already wet pussy."

        play sound2 s_aaah

        girl.char "Oooh!"

        $ attitude = girl.get_sex_attitude(act="service", fix="69") + girl.get_love() - girl.get_fear()

        if girl.test_fix("69") == "pos":

            "As you pleasure each other, [girl.name] becomes wilder and wilder, spurting her love juice all over your face. She soldiers on as she goes through several intense orgasms, trying to keep her voice down."

            play sound2 s_ahaa

            girl.char "Hnnn... Hnnn... Aaah..."

        else:

            "You both pleasure each other, licking and sucking until you can no longer hold it."

            girl.char "Oh, Master..."

        play sound s_orgasm

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "cof"], not_tags=["group", "bisexual"])
        if pic:
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

        with flash

        "Unable to resist her earnest technique, you cum hard over her face as she is rocked by a powerful orgasm."

        with doubleflash

        girl.char "AAAAAH!!!"

        $ girl.change_love(3)

    elif selected_act == "sex" and fix == "spooning":
        if girl.pop_virginity():
            $ pic = girl.get_pic("virgin", "sex", "naked", and_tags=["spooning"], and_priority=False, not_tags=["group", "bisexual"])
            $ changed_stats = [("sex", dice(6)+4), ("sensitivity", dice(6)+4)]
            $ lost_virginity = True
        else:
            #edit
#            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["group", "bisexual"])
            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["cumshot", "group", "bisexual"])
            if not pic:
                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["group", "bisexual"])
###
            $ changed_stats = [("sex", dice(3)+2), ("sensitivity", dice(3)+2)]
            $ lost_virginity = False

        "She turns shyly away from you. You can tell she is tense with excitement."

        you "Hello babe..."

        "Reaching from behind her, you pull her closer to you. You start fondling her breasts, rolling your fingers on her erect nipples. She does nothing to stop you."

        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        play sound s_ahaa

        girl.char "Oh... Hmmm... Master, oh..."


        if girl.naked:
            "Wasting no time, you free your dick from your pants and start rubbing it against her naked pussy. She is already wet, and her juices coat your erect cock nicely."
        else:
            "Pulling down her thin panties, you start grinding your erect cock against her defenseless pussy. She moans and sighs as she becomes wet under your assaults."

        play sound s_moans

        girl.char "Master... Aah..."

        if lost_virginity:
            "[girl.name] blushes bright red. You remember she is a virgin."
            "You pause for a moment."
            you "Are you okay?"
            girl.char "It's all right... I want it."
            "She starts moving her hips towards you, hungry for more. You resume your grinding."

        "After a few moments, she is wet enough for you to easily slide in. You fuck her gently from behind, as she buries her face in her pillow."

        girl.char "Hnnn..."

        $ attitude = girl.get_sex_attitude("sex", "spooning") + girl.get_love() - girl.get_fear()

        if attitude >= 100:
            "[girl.name] loves being fucked like that, and she shakes her ass erotically to better feel your every thrust. You increase pace, and it isn't long before she reaches an intense orgasm, biting hard into her pillow."

            play sound s_orgasm

            with flash

            girl.char "AAAAH!!! YES!!!"

            $ girl.change_love(3)

        elif attitude >= 0:
            "You enjoy fondling and fucking [girl.name], and she responds well to your touch. Soon, you feel close to reaching your limit."

            play sound s_orgasm

            with flash

            girl.char "Oh, Master!"

            $ girl.change_love(2)

        else:
            "Although [girl.name] lets you fuck her as you want to, she is still tense, and you can tell she isn't enjoying this much."

            $ girl.change_love(1)

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "cin"], not_tags=["group", "bisexual"])

        if pic:
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

        with doubleflash

        "You cum inside her, filling her up with hot semen. She shivers and moans as you pop your dick out, cum dripping out of her open pussy."

    elif fix == "penis worship":
        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["group", "bisexual", "cumshot"])

        play sound s_sucking

        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        you "Yeah... That's good..."

        $ attitude = girl.get_sex_attitude("service", "penis worship") + girl.get_love() - girl.get_fear()

        if attitude > 100:
            "She massages your cock expertly, rubbing it against her face while looking you straight in the eye. She seems to love this."
            $ text1 = "满心欢喜地"
            $ text2 = "舔舐干净"
            $ changed_stats = [("service", dice(3)), ("obedience", 2+dice(3))]
            $ girl.change_love(3)
        elif attitude > 0:
            "She does her job well, jerking you off with an exaggerated look of rapture on her face, waiting for you to cum."
            $ text1 = "漫不经心地"
            $ text2 = "胸口擦拭双手"
            $ changed_stats = [("service", dice(3)), ("obedience", dice(3))]
            $ girl.change_love(2)
        else:
            "She does her job mechanically, clearly not enjoying herself. It seems she cannot wait for you to finish."
            $ text1 = "厌恶地"
            $ text2 = "用布擦拭双手"
            $ changed_stats = [("service", 1), ("obedience", 1)]


        "You keep her going until you reach your limit, cumming all over her delicate hands."

        with flash

        "She looks at the cum on her hands [text1], before [text2]."

        you "Good girl... Now go to work."


    elif fix == "irrumatio":
        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["group", "bisexual", "cumshot"])

        play sound s_sucking

        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        girl.char "Hnn!"

        "Slamming your cock up and down her throat, you push her to the limits of her gag reflexes."

        $ attitude = girl.get_sex_attitude("fetish", "irrumatio") + girl.get_love() - girl.get_fear()

        if attitude > 100:
            "She takes it all in stride, opening her mouth wide and covering your cock with her saliva as you go. She seems to enjoy this."
            $ text1 = "她确保把它全部吞下去"
            $ changed_stats = [("service", dice(3)), ("fetish", 2+dice(3))]
            $ girl.change_love(3)
        elif attitude > 0:
            "She lets you have your way, soldiering on as you fuck her throat hard."
            $ text1 = "她躺在那里气喘吁吁地试着呼吸时，精液从她的嘴边滴落下来"
            $ changed_stats = [("service", dice(3)), ("fetish", dice(3))]
            $ girl.change_love(2)
        else:
            "She sobs and gags as you rape her throat, hating it."
            $ text1 = "她吐了出来，其气味和味道让她感到恶心反胃"
            $ changed_stats = [("service", -1*dice(3)), ("fetish", -1*dice(3))]
            $ girl.change_love(-2)

        "After a few minutes of face-fucking her, you cum inside her throat."

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "cim"], not_tags=["group", "bisexual"])
        if pic:
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

        with doubleflash

        "[text1]."

        you "Well, that was fun... Now, get ready to work."


    elif fix in ["fondling her boobs", "groping her ass", "fingering"]:
        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=all_sex_acts+["bisexual"])

        you "Take your clothes off, and place them here by the door. You will greet each and every customer, naked. I'm sure they'll like that."
        if (girl.is_("dom") and girl.get_stat("obedience") < 100) or (girl.is_("sub") and girl.get_stat("obedience") < 50):
            girl.char "Whaaat??? No!"
            "She resists you, but you wrestle all of her clothes off, throwing them in a heap in a corner. You then forcefully place her by the main door."
            $ girl.change_love(-1)
        else:
            girl.char "I understand..."
            "Standing by the main entrance, she takes off her clothes one by one, offering a nice show to the first arriving customers."

        you "You will do as you're told! And don't let me hear that you disrespected a single customer."

        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        $ attitude = girl.get_sex_attitude("naked", fix)

        with fade
        play sound s_chimes
        girl.char "Welcome, sir..."
        play sound s_surprise
        girl.char "Oh!"
        "The customers enjoy touching and fondling [girl.name]'s [touched] as they come in."

        if attitude > 100:
            play sound s_aaah
            "[girl.name] loves being touched and groped by many strangers' marauding hands... You watch as she quietly orgasms under the customers' watchful gaze."
            play sound s_orgasm_fast
            $ changed_stats = [("sensitivity", 2+dice(3)), ("obedience", dice(3))]
            $ rep_impact = True

        elif attitude > 0:
            play sound s_ahaa
            "[girl.name] squirms and tries her best to greet customers properly while they fondle her private parts. It's a lot of fun to watch."
            play sound s_crowd_laugh
            $ changed_stats = [("sensitivity", dice(3)), ("obedience", dice(3))]
            $ rep_impact = True

        else:
            girl.char "Eeek!!!"
            "[girl.name] hates to feel the touch of random strangers on her sensitive parts. She makes no effort to hide her disgust, and the customers soon lose interest."
            play sound s_crowd_boos
            $ changed_stats = [("sensitivity", -1*dice(3)), ("obedience", -1*dice(3))]
            $ rep_impact = True

    elif selected_act == "sex" and fix in ["public acts", "doggy style", "piledriver"]:
        if girl.pop_virginity():
            $ pic = girl.get_pic("virgin", "sex", "naked", and_tags=and_tag+fix_dict[fix].tag_list[0], and_priority=False, not_tags=["group", "bisexual"])
            $ lost_virginity = True
        else:
            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["group", "bisexual", "cumshot"])
            $ lost_virginity = False

        if fix == "public acts":
            "She stands there with her body exposed, even as curious customers look on."
            you "Welcome, everyone! Today, you will have the privilege to witness first-hand some of my trademark techniques."

        elif fix == "doggy style":
            "Pushing her against a wall, you whip your dick out, pressing it against the entrance of her labia."
            you "Get ready for a good fucking, bitch..."

        elif fix == "piledriver":
            "Spreading her legs wide, you lift her lower body into the air and place your erect shaft against her private parts."
            play sound s_surprise
            girl.char "Oh, Master!"

        play sound s_sucking

        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        "You start grinding your cock back and forth against her pussy lips."

        $ attitude = girl.get_sex_attitude("sex", fix)

        if attitude > 100:
            "[girl.name]'s pussy is already completely wet, and your dick makes a squishing sound as it slides deep into her vagina."

            girl.char "Aaah! ♥"

            $ girl.change_love(3)

        elif attitude > 0:
            "[girl.name] is tensed at first, but her mood changes as the pressure against her private parts builds. Soon, you can feel some of her juice starting to flow."

            girl.char "Ooooh..."

            $ girl.change_love(2)

        elif attitude > -100:
            "[girl.name] clenches her teeth and endures as you shove your hard dick into her tight pussy."

            girl.char "No..."

            $ girl.change_love(-1)

        else:
            "[girl.name] becomes tearful as you force your cock into her dry pussy, hurting her."

            play sound s_scream
            girl.char "Ouch!"

            $ girl.change_love(-3)

        play sound s_moans

        if lost_virginity:
            "As [girl.name] is a virgin, her pussy is extremely tight. Some blood leaks out as you enter her, and she moans with pain."

        if fix == "public acts":
            "You fuck her with abandon, under the watchful eye of the crowd."

            if girl.test_fix(fix) == "pos":
                "Because she loves doing it in public, she becomes extremely aroused as you pound her."
                $ girl.change_love(1+dice(4))
                $ changed_stats = [("libido", dice(3) + 2), ("sex", dice(3) + 2)]
            elif girl.test_fix(fix) == "neg":
                "She cries in shame, trying desperately to hide her body as the people look on."
                $ girl.change_fear(1+dice(4))
                $ changed_stats = [("libido", -1*dice(3)), ("sex", -1*dice(3))]

        elif fix == "doggy style":
            "You fuck her, pushing her forward with every thrust, making her stand on the tip of her toes as you pounce her from behind."

            if girl.test_fix(fix) == "pos":
                "She moans like a bitch, loving to be fucked doggy style."
                $ girl.change_love(1+dice(4))
                $ changed_stats = [("libido", dice(3) + 2), ("sex", dice(3) + 2)]
            elif girl.test_fix(fix) == "neg":
                "She tries to escape you, fighting back weakly. She doesn't enjoy this position."
                $ girl.change_fear(1+dice(4))
                $ changed_stats = [("libido", -1*dice(3)), ("sex", -1*dice(3))]

        elif fix == "piledriver":
            "Shoving your dick inside her as deep as possible, you proceed to pound her mercilessly with her legs spread wide."

            if girl.test_fix(fix) == "pos":
                "She starts moaning and drooling, arching her back to get a better feel for your dick. She loves being upside down."
                $ girl.change_love(1+dice(4))
                $ changed_stats = [("libido", dice(3) + 2), ("sex", dice(3) + 2)]
            elif girl.test_fix(fix) == "neg":
                "She turns her head away and bites her lip, feeling hurt by this uncomfortable position."
                $ girl.change_fear(1+dice(4))
                $ changed_stats = [("libido", -1*dice(3)), ("sex", -1*dice(3))]

        "You keep fucking her, oblivious to the brothel around you. After having fun with her for a while, you send her off to work some more."

        $ girl.interactions -= 1
        $ girl.tire(10)


    elif punish and fix in ["cowgirl", "femdom", "footjobs"]:
        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["group", "bisexual", "cumshot"])

        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        if fix == "cowgirl": # Virgins are caught before choosing this act

            $ selected_act = "sex"

            "With a naughty smile, [girl.name] saddles on the surprised customer, not giving him a chance to protest."

            girl.char "I'm going to ride the fucker until his back breaks..."

            play sound s_moans

            man "Aaah!!! Lady, what are you..."

            play sound2 s_punch

            girl.char "Shut up, old nag! You better stay nice and hard, or I'll feed you to the hounds!"

            $ changed_stats = [("libido", dice(3)), ("sex", dice(3) + 2)]

        elif fix == "femdom":

            $ selected_act = "fetish"

            girl.char "On your knees, weakling!"

            play sound s_punch
            with vpunch

            man "Please, my lady! I beg forgiveness..."

            girl.char "You WILL address me as Mistress, worm!"

            play sound s_punch
            with vpunch

            pause 0.2

            play sound s_wscream
            man "Please, Mistress, don't hurt me... *sob*"

            $ changed_stats = [("libido", dice(3)), ("fetish", dice(3) + 2)]

        elif fix == "footjobs":

            $ selected_act = "fetish"

            play sound s_sucking

            girl.char "Do you feel that? I can crush you beneath my feet!"

            man "Mercy, my lady... *sob*"

            "[girl.name] increases her pressure on the poor man's cock."

            man "Aaah!!!"

            girl.char "Don't you dare cum until I say so! I will squeeze your stupid dick dry tonight..."

            $ changed_stats = [("constitution", dice(3)), ("fetish", dice(3) + 2)]

        "You leave [girl.name] to have her fun."


    elif fix in ["masturbation", "deep throat", "swallowing", "insults", "dirty sex", "creampie"]:

        if fix in ["masturbation", "deep throat", "dirty sex"]:
            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["waitress"], not_tags=["group", "bisexual", "cumshot"])

        else:
            $ pic = girl.get_pic(selected_act, and_tags=and_tag+["waitress"], not_tags=["group", "bisexual", "cumshot"])


        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        if fix == "masturbation":
            "You force [girl.name] to masturbate in front of the customer, sitting on one of the tavern's tables."

            play sound s_moans

            man "Oh, look at that bitch go..."

            $ attitude = girl.get_sex_attitude("service", "masturbation")

            if attitude > 100:
                "Being under strangers' gaze seems to turn [girl.name] tremendously, and her love juices flow out as she expertly plays with her clit and pussy."
                girl.char "Aaah, aaaaah!!!"

                play sound s_orgasm_young

                "She comes hard and fast, squirting her juices on the table cloth. The customers applaud her performance."

                $ changed_stats = [("sensitivity", dice(3)), ("service", 2+dice(3))]
                $ rep_impact = True

            elif attitude > 0:
                "[girl.name] puts on a brave face and masturbates for the customer's pleasure. She gets turned on in spite of herself."

                girl.char "Hmmm..."

                "She gets wetter as the customer looks more closely at her loose pussy. Soon, she reaches a muffled orgasm."

                play sound s_orgasm_fast

                $ changed_stats = [("sensitivity", dice(3)), ("service", dice(3))]
                $ rep_impact = True

            else:
                "With a frown on her face, she starts masturbating for the customer's pleasure."

                "She is unwilling and ashamed, however, and does a poor job of it. The customer loses interest."

                $ changed_stats = [("sensitivity", -1*dice(3)), ("service", -1*dice(3))]
                $ rep_impact = True

        elif fix == "deep throat":
            "Ignoring [girl.name]'s squirming, the customer forces her to her knees, shoving his erect dick into her face."

            man "Stuff yourself with this, slut!"

            play sound s_sucking

            "[girl.name] has to suck that man's dick deeper and deeper, until his every thrust digs into the back of her throat."

            girl.char "Nggg!!!"

            $ attitude = girl.get_sex_attitude("service", "deep throat")

            if attitude > 100:
                "[girl.name] is well used to sucking dicks, and she takes the customer's cock in stride."

                girl.char "Ngggh..."

                "The customer pulls her head in as she swallows his cock even deeper."

                man "Oooh..." with flash

                "She brings the customer to his limit, and his dick pops out, shooting thick cum all over her face and chest. The whole tavern cheers."

                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "cof"], not_tags=["group", "bisexual"])

                if pic:
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with dissolve

                $ changed_stats = [("constitution", dice(3)), ("service", 2+dice(3))]
                $ rep_impact = True

            elif attitude > 0:
                "[girl.name] knows how to service a dick, and she gets to work begrudgingly."

                girl.char "Mmmh..."

                "The customer enjoys sliding his dick deeper and deeper inside her throat, and she keeps up with him, until he is ready to let go."

                man "Oooh!!!" with flash

                "She spits the cum out as the customer loudly shoots his load inside her mouth. He looks blissful."

                $ changed_stats = [("constitution", dice(3)), ("service", dice(3))]
                $ rep_impact = True

            else:
                "[girl.name] coughs and retches as the customer violates her throat."

                girl.char "Hrrr..."

                "After a few moments, it seems that she's about to puke, and the customer backs away. He reluctantly gives up on fucking her face."

                man "You useless bitch... What good is a whore who can't suck a dick?"

                $ changed_stats = [("constitution", -1*dice(3)), ("service", -1*dice(3))]
                $ rep_impact = True

        elif fix == "swallowing":
            "The customer sits on a table, forcing [girl.name] to suck his cock in front of the whole tavern."

            play sound s_sucking

            man "Har har har! Look at that bitch go! I'm the one serving her a drink tonight!"

            with doubleflash

            "Before she has a chance to pull away, the customer cums a whole lot of jizz down her throat, forcing her to drink it up."

            with flash

            girl.char "NGGGGH!!!"

            $ attitude = girl.get_sex_attitude("service", "swallowing")

            if attitude > 100:
                "Luckily, [girl.name] has long trained for this, and she drinks every last drop of the customer's smelly cum with gusto."

                play sound s_mmmh

                girl.char "Mmmh..."

                "Expertly, she licks the customer's dick clean from the balls to the tip. She shows him the thick cum on her tongue with a hungry look, before swallowing it all down."


                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "cim"], not_tags=["group", "bisexual"])

                if pic:
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with dissolve

                man "Oh, that's great..."

                $ changed_stats = [("obedience", dice(3)), ("service", 2+dice(3))]
                $ rep_impact = True

            elif attitude > 0:
                "She wasn't expecting him to cum so hard and soon, but she does her best to hold the cum inside her mouth as the man keeps cumming."

                girl.char "Ngh... Ngggh..."

                "When he is done, he pops his dick out of her mouth, wiping the remaining cum inside her hair."

                "She swallows the semen slowly, under the cheers from the small crowd of onlookers. After a while, she opens her mouth wide and sticks her clean tongue out for everyone to see."

                man "Nice little bitch, [girl.name]..."

                $ changed_stats = [("obedience", dice(3)), ("service", dice(3))]
                $ rep_impact = True

            else:
                play sound s_surprise

                girl.char "HNNN!!!"

                "She retches and spits it all out onto her top, desperate to get the cum out of her mouth."

                "The customer pops his dick out and she falls down on the floor coughing in a pool of dirty cum."

                man "Humph. The bitch can't even swallow a little cum properly."

                $ changed_stats = [("obedience", -1*dice(3)), ("service", -1*dice(3))]
                $ rep_impact = True

        elif fix == "insults":
            "The customer lifts the girl on top of a table and forces her to spread her legs, tauting and insulting her."

            man "What a slut! Look how easily I can enter that bitch's pussy."

            play sound s_moans

            girl.char "Aaah!!!"

            "As the customer starts fucking her right there in the tavern, he keeps insulting her and calling her names."

            man "Take that, you filthy sow! I'm going to treat you like the cum-toilet you are!!!"

            $ attitude = girl.get_sex_attitude("sex", "insults")

            if attitude > 100:
                "Being insulted turns her on, and she holds the customer tight as he pounds her harder and harder."

                girl.char "M... More! I'm a dirty, dirty bitch! Fuck me hard!"

                with doubleflash

                "It isn't long until the customer reaches his limit, cumming hard inside her wet pussy."

                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "creampie"], not_tags=["group", "bisexual"])

                if pic:
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with dissolve

                with flash

                play sound s_orgasm

                "The customer zips up with a satisfied look, leaving [girl.name] panting on the table in a pool of love juice. The other customers are impressed."

                $ changed_stats = [("sensitivity", dice(3)), ("sex", 2+dice(3))]
                $ rep_impact = True

            elif attitude > 0:
                "She blushes as the customer insults and violates her. She takes a pounding, but her love juices start flowing, and soon she is moaning under the customer's assaults."

                man "Take that, you dirty whore!"

                girl.char "Oh, ah, aah..."

                with doubleflash

                "Reaching his limit, the customer pops his dick out and shoots his load all over her."

                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "cob"], not_tags=["group", "bisexual"])

                if pic:
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with dissolve

                with flash

                play sound s_orgasm_fast

                "The customer looks at her messy body and seems happy. He leaves the tavern, whistling."

                $ changed_stats = [("sensitivity", dice(3)), ("sex", dice(3))]
                $ rep_impact = True

            else:
                girl.char "Stop! Please, Master, make him stop..."

                man "Shut up, you dumb bitch!"

                "[girl.name] cries and endures as the customer violates her dry pussy. After trying for a few minutes, he finds she isn't much fun and gives up."

                man "What a good-for-nothing slave slut... You're not even good as a cum dump!"

                $ changed_stats = [("sensitivity", -1*dice(3)), ("sex", -1*dice(3))]
                $ rep_impact = True

        elif fix == "dirty sex":
            "The customer shoves [girl.name] on a table, not caring about the food and drinks she spills all over."

            play sound s_surprise

            girl.char "Aaah!!!"

            "Stained with crushed food and spilt beer, she struggles weakly to get back up, but the customer yanks her panties off and spreads her legs with his strong arms."

            girl.char "W-Wait a minute..."

            "Ignoring her complaints, the customer starts fucking her right in the middle of the splattered foodstuff."

            play sound s_moans

            $ attitude = girl.get_sex_attitude("sex", "dirty sex")

            if girl.pop_virginity():
                show screen show_event(girl.get_pic("virgin", "sex", "naked", and_tags=and_tag+fix_dict[fix].tag_list[0], and_priority=False, not_tags=["group", "bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with dissolve
                "[girl.name] is a virgin, but the customer is too drunk to care. Some blood leaks out as he enters her, and she moans with pain."

            if attitude > 100:
                "She loves being down and dirty, and moans like a wild animal as the customer bangs her hard."

                girl.char "AAAAH!!!"

                with doubleflash

                "The customer quickly cums a huge load of cum inside her, and she screams, rocked by a massive orgasm."

                play sound s_orgasm

                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "cin"], not_tags=["group", "bisexual"])

                if pic:
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with dissolve

                with flash

                girl.char "AHAAAA!!!"

                "The tavern customers cheer them on and enjoy the show."

                $ changed_stats = [("constitution", dice(3)), ("sex", 2+dice(3))]
                $ rep_impact = True

            elif attitude > 0:
                "[girl.name] clings to the customer as he enters her and slowly starts moving back and forth. She moans in spite of herself as he increases his pace."

                girl.char "Oh... Ah..."

                "The customer intensifies his grinding, pinching her nipples and calling her dirty names. Soon, he is close to cumming."

                with flash

                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "cob"], not_tags=["group", "bisexual"])

                if pic:
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with dissolve

                girl.char "Aaaah!!!"

                with doubleflash

                "The customer grunts as he releases it all inside her. He looks happy as he buckles up his pants, leaving [girl.name] lying in a mess of cum and dirty food."

                $ changed_stats = [("constitution", dice(3)), ("sex", dice(3))]
                $ rep_impact = True

            else:
                "[girl.name] cries and screams for him to stop, but the customer doesn't care."

                girl.char "No! Stop it!"

                "She hates being fucked in this disgusting setting. She tries to close her legs shut and push the customer back."

                man "Stop resisting me, bitch!"

                "[girl.name] is fighting back too much for the customer to continue his assault. He gives up and leaves, grumbling about the poor quality of the slaves here."

                $ changed_stats = [("constitution", -1*dice(3)), ("sex", -1*dice(3))]
                $ rep_impact = True

        elif fix == "creampie":

            "The customer gives [girl.fullname] a hungry, wolfish look, which makes her uncomfortable."

            girl.char "Mister... What... What do you want from me?"

            man "I have been saving my semen for a month, just for you..."

            girl.char "Whaaat? Mister, no... Aaaah!"

            "With uncanny strength, the customer rips her clothes apart, exposing her naked pussy. He wastes no time in whipping his hard cock out and placing it at the entrance of her womb."

            play sound s_moans

            $ attitude = girl.get_sex_attitude("sex", "creampie")

            if girl.pop_virginity():
                show screen show_event(girl.get_pic("virgin", "sex", "naked", and_tags=and_tag+fix_dict[fix].tag_list[0], and_priority=False, not_tags=["group", "bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with dissolve
                "[girl.name] is a virgin, and she shivers with anticipation as she sees the large bulging cock at the entrance of her womb."

            if attitude > 100:
                girl.char "Oh, mister... You're so hard..."

                "[girl.name]'s pussy is glistening with her love juice already, making it easy for the customer to slide his thick cock inside her."

                play sound2 s_mmmh

                girl.char "Mmmh, aaah..."

                "The man starts pounding her pussy like crazy, and she moans and screams intensely, seeming to enjoy it just as much as he does."

                girl.char "Oh, mister, oooh!!!"

                man "Get ready to be my cum-dump, you little slut-waitress!"

                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "creampie"], not_tags=["group", "bisexual"])

                if pic:
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with dissolve

                with flash

                play sound s_orgasm

                girl.char "Aaaah! You're filling me up!!!"

                with doubleflash

                "[girl.name] cums hard as the customer unloads a bucket of cum inside her overflowing pussy. It really does seem like he had been saving for a month."

                girl.char "Aaah... It's so... warm..."

                "She lies there, nearly passed out with her legs spread out. The customers watch her as thick, white cum keeps pumping out of her overfull pussy."

                $ changed_stats = [("libido", dice(3)), ("sex", 2+dice(3))]
                $ rep_impact = True

            elif attitude > 0:

                girl.char "Mister, wait..."

                "Overcoming her resistance, the customer pushes his hard shaft inside her vagina."

                girl.char "It's so large! Aaaah!"

                "Before she has a chance to recover, the customer starts pounding her pussy with intensity. She moans painfully at first, but you can detect something else in her voice: lust."

                man "And now, I'm going to fill you up with my cum."

                girl.char "Wait... I... Aaaaah!!!"

                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "creampie"], not_tags=["group", "bisexual"])

                if pic:
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with dissolve

                with flash

                "Ignoring her, the customer unloads suddenly, spurting cum inside and outside her pussy, making an utter mess."

                with doubleflash

                girl.char "Oooh..."

                $ changed_stats = [("libido", dice(3)), ("sex", dice(3))]
                $ rep_impact = True

            else:

                girl.char "Stop! What are you do... Aaaah!!!"

                "THe customer forces his hard cock inside her, ignoring her cries of pain and frustration."

                man "I am using you as my cum toilet today."

                girl.char "Stop it!!! Let me go!"

                "Determined to get his way, the customer pounds her tight pussy, not caring that she is dry and resisting."

                girl.char "Ah!!! It hurts! Stop..."

                with flash

                "As quickly as he got started, the customer reaches climax. He spurts out his cum all over [girl.name]'s pussy."

                with doubleflash

                girl.char "Noooo... It's disgusting..."

                "The customer gives [girl.name] a spiteful look, as she lays down sobbing with her legs tight shut, cum dripping down her thighs."

                man "What a useless slave... Can't you take a little fucking properly? Being a cum dump for the customers is part of your job, you know."

                $ changed_stats = [("libido", -1*dice(3)), ("sex", -1*dice(3))]
                $ rep_impact = True


    elif fix in ["dildos", "strap-ons", "squirting"]:

        "The woman licks her lips, looking intensely at [girl.name], who is acting nervous."

        "Under cheers from the crowd, she pulls [girl.name] towards her, and starts to passionately kiss her."

        $ pic = girl.get_fix_pic("bisexual", fix_dict["kissing"], and_tags=["lesbian", "naked"]+and_tag, not_tags=["group"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        girl.char "Nghh!"

        if attitude >= 100:
            "[girl.name] eases up into the kiss, and enthusiastically intertwines her tongue with the mysterious woman's, glistening saliva running from their mouths."

            play sound s_mmh

            girl.char "Mmmh..."

            "Soon, the two women are busy fondling each other inside their underwear, and they quickly shed their clothes under applause from the rowdy crowd."

            play sound2 s_crowd_cheer

        elif attitude >= 0:
            "Reluctantly, [girl.name] kisses back, barely managing to keep up with the woman's busy pace."

            play sound s_aah

            girl.char "Nggh..."

            "While kissing [girl.name], the woman wastes no time in shedding her loose dress to the side, revealing that she isn't wearing any underwear. The crowd erupts
            in applause, and [girl.name] feels compelled to get undressed too."

            play sound2 s_crowd_cheer

        else:
            "[girl.name] reacts indignantly and tries to fight back, but the woman is strong and holds her in a powerful embrace."

            play sound s_surprise

            girl.char "Sh...Shtop!!! Nngh..."

            "Ignoring her, the woman tugs at her clothes, freeing her boobs from her dress. [girl.name] tries to resist, but she is cowed by the woman's insistence and the boos of the rowdy crowd."

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["lesbian"]+and_tag, not_tags=["group"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        if fix == "dildos":
            "Seemingly from nowhere, the woman pulls a long, glistening dildo. She dangles it in front of [girl.name]."

            woman "Can you guess where this is going?"

            play sound s_scream

            "Not waiting for an answer, the woman rubs the dildo against [girl.name]'s exposed slit, who gasps audibly in front of the fascinated audience."

            girl.char "W... Wait... Aaaah!"

            play sound s_ahaa

            "The dildo is large enough to rub both the woman's and [girl.name]'s pussies at the same time, and soon they are both grinding against the dick-shaped sex toy."

            woman "This is only half the fun..."

            "Before [girl.name] has a chance to object, the horny woman pushes the large dildo inside her pussy."

            if girl.pop_virginity():
                show screen show_event(girl.get_pic("virgin", "toy", "naked", and_tags=["lesbian"]+and_tag+fix_dict[fix].tag_list[0], and_priority=False, not_tags=["group"]), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with dissolve
                "[girl.fullname] gasps in shock, and blood starts running down her thighs."

                woman "Oh, my... You were a virgin!"

                woman "What a treat... How does it feel to have your virginity taken by a mindless dildo?"

                "The crowd roars back in approval. [girl.name] blushes bright red and looks down at her violated pussy with tearful eyes..."

        elif fix == "strap-ons":
            "The woman takes out an interesting contraption from her bag. It is a leather thong from which hangs a large, oddly realistic dick-shaped dildo."

            "She puts the thong on, one leg at a time, giving everyone a good look at her pussy while tugging on the leather fabric so that it bites into her slit."

            girl.char "Wh... What is that?!?"

            woman "Shut up and bend over, bitch!"

            play sound s_punch

            girl.char "Ouch!" with vpunch

            "The woman slaps [girl.name]'s bare ass strongly, leaving a red mark, and pushes her so that she falls down on the ground."

            "Before she has a chance to get up, the woman places the head of her dick-shaped dildo at the entrance of her womb."

            woman "Ready or not, I'm going to move inside you now. I hope you are honored to be fucked by your mistress."

            "The woman thrusts her well-rounded hips forward, shoving the dick-like appendage inside [girl.name]."

            if girl.pop_virginity():
                show screen show_event(girl.get_pic("virgin", "bisexual", "naked", and_tags=["lesbian"]+and_tag+fix_dict[fix].tag_list[0], and_priority=False, not_tags=["group"]), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with dissolve
                "[girl.fullname] gasps in shock, and blood starts running down her thighs"

                woman "Oh, my... You were a virgin!"

                woman "Fufufu... How does it feel to lose your virginity to another girl? I bet you were saving it for me..."

                "The crowd roars back in approval. [girl.name] blushes bright red and looks down at her violated pussy with tearful eyes..."

        elif fix == "squirting":
            "After [girl.name] is fully naked, the woman flips her over to face the crowd. She takes her place behind her, rubbing her large breasts against [girl.name]'s back."

            "With one hand, the woman pinches one of [girl.name]'s nipples hard. She slides her other hand down [girl.name]'s body, reaching for her pussy lips, which she spreads apart in front of everyone."

            girl.char "Oh... This is so shameful..."

            "The woman toys with [girl.name]'s clit for a few moments, giving a good show to the captivated audience. She then moves her fingers in the shape of a hook, and slide them inside [girl.name]'s pussy."

            play sound s_aaah

            girl.char "Aaaaah!!!"

            woman "I'm going to give you pleasure, like only a woman can..."

        $ rep_impact = True

        if fix in ["dildos", "strap-ons"]:
            if attitude >= 100:

                "Even though the dildo is large and heavy, [girl.name]'s slippery wet pussy swallows it almost entirely without problems."

                play sound s_moans

                "She moans with delight, loving the attentions of the mysterious woman, who plays around with her, tugging and licking her erogenous zones, all the while fucking her with the oversized sex toy."

                "The woman increases her pace with blinding speed, giving a fantastic show to the overjoyed crowd."

                girl.char "Oooooh..."

                "[girl.fullname] seems completely lost in her world, concentrating on some invisible force that seems to build up from between her hips."

                with flash

                girl.char "AAAAAAHHH!!!"

                play sound s_orgasm
                play sound2 s_orgasm_young

                with doubleflash

                "[girl.name] erupts into a massive orgasm, squeezing the dildo out of her vagina as her love juices flow out freely. The woman loudly climaxes too, just from watching. "

                play sound2 s_crowd_cheer

                you "What a great show..."

                if fix == "dildos":
                    $ changed_stats = [("libido", 2+dice(3)), ("service", dice(3))]
                elif fix == "strap-ons":
                    $ changed_stats = [("libido", dice(3)), ("sex", 2+dice(3))]

            elif attitude > 0:

                "The massive dildo enters [girl.name] with difficulty, but the woman spits heavily on it, and slowly pushes it deeper and deeper inside."

                play sound s_moans

                "[girl.name] seems lost and confused, but the sensations as the woman increases her attentions are too much to ignore. Soon, the large dildo starts oozing with something other than spit."

                girl.char "Mmmmh..."

                woman "Come on, sweetie... Let yourself go..."

                "[girl.name] tries to fight it, but she feels it even more. Soon, she shivers and gasps for air as she reaches a quiet orgasm."

                play sound s_orgasm_fast

                "The crowd laughs and cheers her on. She looks shameful, but the woman holds her in her arms lovingly, playing with her erect nipples."

                you "That was a nice show..."

                if fix == "dildos":
                    $ changed_stats = [("libido", dice(3)), ("service", dice(3))]
                elif fix == "strap-ons":
                    $ changed_stats = [("libido", dice(3)), ("sex", dice(3))]

            else:

                play sound s_scream

                girl.char "Stop!!!"

                "[girl.name]'s tight pussy seems about to tear as the woman forces the large dildo inside her."

                "Tears run down [girl.name]'s cheeks and she clenches her jaw as she endures the pain."

                "The crowd seems excited, but [girl.name] is visibly in pain, and many can't stomach it."

                woman "This isn't going anywhere..."

                "The dildo is stuck and won't go any further inside [girl.name]'s dry pussy. Frustrated, the woman gives up and the audience boos loudly."

                play sound s_crowd_boos

                "You decide to end the show before you have a riot on your hands."

                if fix == "dildos":
                    $ changed_stats = [("libido", -1*dice(3)), ("service", -1*dice(3))]
                elif fix == "strap-ons":
                    $ changed_stats = [("libido", -1*dice(3)), ("sex", -1*dice(3))]

        elif fix == "squirting":
            if attitude >= 100:
                "[girl.name] leans back into the woman's embrace, letting her play with her body like a broken doll."

                "Glistening love juice runs down [girl.name]'s thigh, flowing out of her pussy while the woman works her magic. She reaches deep inside [girl.name]'s pussy, rubbing and pressuring her G-spot."

                girl.char "Oh... It's so good..."

                "[girl.name] seems lost in the feeling, and the woman increases her pace, playing her like a fiddle."

                play sound s_aaah

                girl.char "Aaaah... What's happening... to me..."

                play sound s_scream

                girl.char "AAAAAH!!!"

                with flash

                "[girl.name] arches back, overwhelmed by the heat in her pussy. The woman expertly guides her to her climax."

                play sound s_orgasm

                with doubleflash

                girl.char "AAAAAAAAHHHH!!!"

                "[girl.name] cums hard, and as she comes, she starts squirting love juices all over the front row of the audience. The crowd roars wildly."

                play sound2 s_crowd_cheer

                "The woman lifts her hand for all to see, glistening with [girl.name]'s wet juice, then licks it all up greedily."

                you "Wow... What a great show!"

                $ changed_stats = [("sensitivity", 2+dice(3)), ("fetish", dice(3))]

            elif attitude >= 0:
                "[girl.name] is ashamed and blushing, but she doesn't stop the woman as she starts moving her expert fingers inside her tight pussy."

                woman "Lean back and enjoy it..."

                "The woman seems to be looking for a specific spot inside [girl.name]'s pussy, and it is fun for the audience to watch [girl.name] squirm as she gets closer to her goal."

                play sound s_surprise

                girl.char "Ooh..."

                "Finally, the woman seems to find what she was looking for. [girl.name] blushes even brighter, and her breathing grows heavier."

                woman "Now, let us give our guests a good show..."

                "The woman works [girl.name] closer and closer to her climax, until she cannot resist her anymore."

                play sound s_scream
                with flash

                girl.char "AAAAAH!!!"

                play sound s_orgasm_fast

                "[girl.name] finally cums, in the process splattering her love juices on stage. The customers enjoy the show."

                "The woman kisses [girl.name] on the cheek, then leaves her panting in a pool of her own juices."

                you "That was a nice show."

                $ changed_stats = [("sensitivity", dice(3)), ("fetish", dice(3))]

            else:

                play sound s_surprise

                girl.char "No!!!"

                "[girl.name] squirms and squeezes her thighs together, trying to avoid the woman's invasive fingers."

                girl.char "Let me go! No!"

                "The woman tries to force her fingers deeper inside [girl.name], but her efforts are thwarted by [girl.name]'s desperate moves."

                "This is all pretty boring to watch, and some crowd members begin to heckle. The woman seems frustrated and angry."

                play sound s_crowd_boos

                you "I better stop this now... This isn't going anywhere."

                $ changed_stats = [("sensitivity", -1*dice(3)), ("fetish", -1*dice(3))]


    elif (selected_act == "anal" and fix == "doggy style") or fix in ["ass-to-mouth", "spanking"]:

        $ rep_impact = True

        "As soon as the man climbs on stage, he is all over [girl.name], fondling her private parts under her clothes."

        play sound s_surprise

        girl.char "Haaa!"

        "He seems to be especially interested in her ass, and soon he lifts her skirt up and takes down her panties, exposing her round buttcheeks to all."

        $ pic = girl.get_fix_pic("naked", fix_dict["groping her ass"], and_tags=and_tag, not_tags=["bisexual", "group"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        play sound s_crowd_cheer

        girl.char "M-Mister... What are you... doing..."

        "Ignoring her, the man bends her forward, all the while kneading her ass like dough. Licking his middle finger, he sticks it inside [girl.name]'s asshole all of a sudden."

        if attitude > 100:

            play sound s_aaah
            girl.char "Ohhh..."

            "[girl.name] lets out an audible moan as she feels a foreign finger probing inside her anus."

        elif attitude > 0:

            play sound s_ahaa
            girl.char "Ah!"
            "[girl.name] blushes bright red and gasps audibly as the man starts probing inside her anus."

        else:

            play sound s_scream
            girl.char "Eeek!!"

            "[girl.name] jerks forward and shrieks, contracting her tight anus to try and prevent the man from entering it."

        "Unfazed, the man keeps toying with her pink asshole, watching her every reaction while his erection grows harder. Soon, he whips his dick out, and [girl.name] gasps when she sees the size of it."

        man "Bend over, slave!"

        play sound s_punch
        with vpunch

        girl.char "Aw!"

        "The man slaps his fat dick across the girl's naked butt, while the crowd cheers him on."

        "The man starts spitting a wad of saliva right into her asshole. He then places his cock of the entrance of her anus, playfully pushing the tip halfway inside."

        $ pic = girl.get_pic("anal", and_tags=and_tag, not_tags=["bisexual", "group"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        girl.char "Oh! My ass... Wait..."

        "[girl.name]'s face reddens with embarrassment as she realizes the man is about to fuck her ass, right here in the club. The crowd goes wild with excitement."

        play sound s_moans
        with hpunch

        girl.char "AAAAH!!!"

        "The man pushes his cock inside her butt, using his saliva as a lubricant. [girl.name]'s eyes seem about to pop out as she struggles to accommodate the size of the big man's shaft."

        with hpunch

        girl.char "Nggh!"

        if attitude > 100:
            "[girl.name]'s asshole is surprisingly flexible, and soon engulfs the whole manhood of the customer. [girl.name] moans with pleasure as the man starts fucking her ass."

            "She is enjoying anal sex so much, she seems to forget about the people watching. The man yanks her hair backwards, pounding her harder and harder."

            girl.char "Oh, yes! Yes!"

        elif attitude > 0:

            "[girl.name] clenches her teeth and remembers her training, letting her asshole slowly expand to fit the man's penis. After a few moments, she loosens up enough for him to start moving."

            girl.char "Oh... Aaah!"

            "The man grabs both of her arms and pulls her backwards, impaling her little asshole on his erect cock. It is hard for her at first, but she takes it in stride."

            girl.char "Ooh..."

        if attitude > 0:

            if fix == "doggy style":
                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["bisexual", "group"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with fade

                "Shoving his dick even deeper inside her, the man pushes her off-balance, and she falls down on all fours. He doesn't take any break from fucking her, mating with her like an animal."

                girl.char "Aah, aaaah..."

                if attitude > 100:
                    "The crowd stands up to watch [girl.name] being fucked in the ass by a huge cock on stage. She moans like a bitch in heat as they both reach their climax."

                    girl.char "I'm... I'm cummiiiing!!!"

                    $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cin"], not_tags=["group", "bisexual"], strict=True)
                    if not pic:
                        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "creampie"], not_tags=["group", "bisexual"])

                    if pic:
                        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                    with flash
                    play sound s_orgasm

                    girl.char "AAAAAAH!!!"

                    with doubleflash

                    "The man shoots a huge load of warm cum inside [girl.name]'s tight anus, and she cums screaming at the top of her voice as the thick white semen overflows out of her."

                    "The crowd goes wild with applause, and give the couple on stage a standing ovation."

                    play sound2 s_crowd_cheer

                    man "Thank you, you are a true Brothel Master... Here is your cash, it was worth every last coin!"

                    $ gold = 100
                    $ changed_stats = [("libido", dice(3)), ("anal", 2+dice(3))]

                elif attitude > 0:
                    "The man gives [girl.name] a vicious pounding in the ass, but she can take it. She starts moving her hips in unison with his movements, bringing him closer to climax."

                    girl.char "Oh, mister... It's growing even larger... What's... going on..."

                    with flash

                    girl.char "Aaaah!"

                    $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "creampie"], not_tags=["group", "bisexual"])

                    if pic:
                        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                        with dissolve

                    with doubleflash

                    "The man cannot take it anymore, and he cums hard inside her tight asshole, filling her stomach up with warm semen."

                    play sound s_orgasm_fast

                    girl.char "AAAAAH!!!"

                    "[girl.name] has a small orgasm as the man pops his dick out, exposing her gaping asshole, overflowing with white cum."

                    "He looks satisfied as the cum slowly drips out of her hole and runs down across her pussy, and throws you a bag of gold."

                    man "You earned it, my good man... I'll be back."

                    $ gold = 75
                    $ changed_stats = [("libido", dice(3)), ("anal", dice(3))]

            elif fix == "ass-to-mouth":

                "As the man increases his pace and comes closer to cumming, he bends over to whisper something in [girl.name]'s ear."

                girl.char "What? In my mouth? Aaah!!!"

                "The man pops his cock out of her ass, and pulls her by the hair, flipping her over. He shoves his cock right in her face."


                if attitude > 100:
                    "Without any hesitation, [girl.name] opens her mouth wide, engulfing his manhood just in time for him to cum inside her throat."
                    $ and_tag += ["libido"]
                else:
                    "[girl.name] hesitates for a second, but the man forcefully pushes his cock inside her mouth, just in time to cum a thick load of semen over her tongue."


                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "cim"], not_tags=["bisexual", "group"])

                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with flash

                girl.char "Ngggh!"

                with doubleflash

                man "Drink it, bitch!"

                if attitude > 100:
                    "Obligingly, [girl.name] begins swallowing every last drop of the man's cum, locking eyes with him as she gulps it down. She makes sure to lick the man's cock spotless clean, unbothered by the weird taste."

                    "The man looks blissful. He hands you a pouch of gold and is effusive in his praise."

                    man "Thank you, you are a true Brothel Master... Here is your cash, it was worth every last coin!"

                    $ gold = 100
                    $ changed_stats = [("service", dice(3)), ("anal", 2+dice(3))]

                else:
                    "[girl.name] is surprised and almost retches from the strong taste in her mouth. She controls herself, however, and takes it in the mouth, even though she spits the cum out little by little."

                    "The man takes a satisfied look at her smeared face, thick cum dripping out of her mouth."

                    man "Good, good... You have earned your coin, my good man. I shall be back."

                    $ gold = 75
                    $ changed_stats = [("service", dice(3)), ("anal", dice(3))]

            elif fix == "spanking":

                "Not content to just fuck [girl.name]'s ass, the customer starts viciously slapping her butt with his large hand."

                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["bisexual", "group"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with fade

                play sound s_punch
                with vpunch

                girl.char "Ouch!!!"

                "[girl.name]'s buttcheek is visibly red where the man hit her. Not giving her any time to recover, he doubles down on slapping her ass, all the while pounding her with his large cock."

                play sound s_screams

                girl.char "Aw!!! Ow!!!"

                if attitude > 100:
                    "Even though she must be in pain, [girl.name] seems to enjoy being spanked way too much. Her pussy is overflowing with juice, and she tightens the muscles in her ass around the customer's dick."

                    girl.char "I'm a bad, bad bitch... Hit me! Harder!"

                    "The man is very pleased to have found such an accommodating slut, and is soon brought over the top."

                    with flash

                    play sound s_orgasm

                    girl.char "Oh, YES!!!"

                    with doubleflash

                    "[girl.name] climaxes hard as the customer spanks and rams her ass one last time, pouring thick cum inside her butthole."

                    "She falls flat on the ground, drooling, as thick cum starts dripping out of her asshole and making a pool between her legs. The customer looks very happy as he hands you the promised gold."

                    man "Whores of this quality are really hard to find in Zan. Congratulations, my good man, you must be the best trainer in the city."

                    $ gold = 100
                    $ changed_stats = [("fetish", dice(3)), ("anal", 2+dice(3))]

                else:
                    "[girl.name] gets tearful as the man viciously spanks her, but her moans of pain have a hint of pleasure in them. She seems to enjoy being punished in this way somewhat."

                    girl.char "Oh... It hurts... Aaah..."

                    "The man seems to be getting his kicks out of the whole scene, and soon reaches his limit."

                    girl.char "Aaaaah!!!"

                    with flash

                    play sound s_orgasm_fast

                    "The man slaps her ass hard one last time, and pops out his dick, shooting his load all over her bare ass and into her gaping anus."

                    with doubleflash

                    girl.char "Ooooh..."

                    "[girl.name] falls flat on the ground, exhausted. The customer contemplates his handiwork with a satisfied look, and hands you the promised gold thoughtlessly."

                    man "Thanks, good man. I shall be back."

                    $ gold = 75
                    $ changed_stats = [("fetish", dice(3)), ("anal", dice(3))]

        else:

            "[girl.name] cries with shock and disbelief as the man forces his huge cock inside her tight asshole. She is clearly in pain."

            girl.char "Nooo... You're ripping me apart!"

            "The man ignores her plea and starts grinding, eliciting more cries of pain out of her. Some customers are disturbed and start to boo him."

            play sound s_crowd_boos

            girl.char "Let me go... It hurts..."

            "Dejected, the man gives her a scornful look. He pops his dick out of her, and she falls down on the floor sobbing."

            man "Where I come from, girls are taught to serve a man properly... What kind of training have you received? It's a disgrace!"

            "The man contemptuously hurls a purse of coins at you, without even looking in your direction, and leaves the brothel without a word."

            $ gold = 50

            $ changed_stats = [("obedience", -1*dice(3)), ("anal", -1*dice(3))]

        play sound s_gold

        $ gold = (gold + dice(gold)) * district.rank
        $ MC.gold += gold

        "You have earned [gold] gold."


    elif fix in ["double penetration", "multiple orgasms", "bukkake"]:

        $ rep_impact = True

        "The men get on stage and surround [girl.name], who looks intimidated by their number."

        girl.char "Wh... What do you expect from me..."

        "Instead of answering, one of the men seizes her from behind, while another removes her clothing, one piece at a time."

        play sound s_scream

        girl.char "Aaah!!! Stop! It tickles!"

        "Soon, [girl.name] is entirely naked, and the head of the group parades her in front of the excited audience."

        play sound s_crowd_boos

        "She watches helplessly as the men start removing their cocks from their pants, and masturbating while fondling her naked body."

        you "So. What's it gonna be, birthday boy?"

        man "Hmmm..."

        if fix in ["double penetration", "multiple orgasms"]:
            man "We are going to fuck her, of course!"

        elif fix == "bukkake":
            man "How about we all fuck that bitch's face and shower her with our cum?"

        girl.char "Uh? What, wait..."


        if fix in ["double penetration", "multiple orgasms"]:

            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["bisexual", "cumshot"])
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with fade

            "Before [girl.name] has a chance to object, the men push her down on the floor.
            One of them places his cock at the entrance of her womb, while the others use her other holes and the rest of her body to pleasure themselves."

            play sound s_scream_loud

            girl.char "Haaa!"

            "Without any foreplay, the leading man forces his cock inside her dry pussy."

            if girl.pop_virginity():
                show screen show_event(girl.get_pic("virgin", "sex", "naked", and_tags=and_tag+["group"], and_priority=False, not_tags=["bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with dissolve
                "Blood starts leaking out of her, and the men are dumbfounded for a moment."

                man "Wait a minute... Is she a virgin? Oh, man..."

                man "AWESOME!!!"

                "[girl.name] sobs as her virginity is taken by a perfect stranger in front of a drunken crowd."

            if attitude > 0:

                "[girl.name] is being fucked under various angles now, and she does her best to keep up."

                if attitude > 100:
                    "Still, she knows how to work a group, and soon her hands and holes are all busy servicing the men."

                    girl.char "Come on... Don't be shy... You can jerk off with my hair if you like... Men tell me it's soft like silk..."

                else:
                    "She is struggling with the number of cocks she has to service at first, but her slutty reflexes kick in."

                    "Soon, she is being fucked by all the guys at the same time, trying to use her body and holes for maximum effect."

                if fix == "double penetration":

                    "Dude" "Move over, man... I wanna fuck her too!"

                    man "Well, she's got another hole, don't she? Use it, bro!"

                    play sound s_surprise

                    girl.char "Oh!"

                    "The second man brings his cock up to her asshole, and the two men lift the girl in the air, spreading her legs apart."

                    play sound s_scream

                    girl.char "It's... Coming in... Aaah!!!"

                    play sound s_moans

                    "Both men start to fuck her simultaneously, coming in and out of her pussy and ass like well-oiled pistons."

                    if attitude > 100:
                        "[girl.name] absolutely loves it, and she moans like a bitch in heat while the men pound her mercilessly."

                        girl.char "Oh, yes! Fuck me! Harder!!!"

                        "[girl.name] is now thoroughly impaled on two large cocks, pumping her up and down, and she wails as she feels a massive orgasm building up within her body."

                        girl.char "Cum!!! Cum, you bastard!!! Fill my ass and pussy with hot CUM!!!"

                        play sound s_crowd_cheer

                        "The crowd cheers them on, and soon the men are reaching their limit."

                        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "buk"], not_tags=["bisexual"])

                        if pic:
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                        with flash
                        play sound s_orgasm

                        girl.char "AAAAH!!!"

                        with doubleflash

                        "[girl.name] looks blissful as the two men cum deep inside her front and back holes, soon followed by the rest of the group, shooting their loads all over her face and body."

                        "She makes a point of wiping all of their dicks clean using her mouth, hair and body. The men leave with a huge smile on their faces."

                        $ changed_stats = [("constitution", 2+dice(3)), ("libido", dice(3))]

                    else:
                        "[girl.name] is taken aback by the strange sensation in her stomach, with both of her holes being raped at the same time."

                        girl.char "What is this! Aaah!!!"

                        "[girl.name] hangs on to the men for dear life as they mercilessly fuck her."

                        girl.char "I'm so full... Aah!"

                        "The crowd encourages the men to go on like a sports team, and soon they cannot take the pressure anymore."

                        girl.char "Oh! Your dicks are growing... bigger!!!"

                        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "buk"], not_tags=["bisexual"])
                        if pic:
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                        with flash

                        "[girl.name] gasps for air as the two men start pumping her full of cum."

                        with doubleflash
                        play sound s_orgasm

                        girl.char "Aaaah!!! There's so much!!!"

                        with flash

                        "The other men cum almost simultaneously, showering [girl.name] with semen. This is enough to send her over the line, and she reaches her own climax,
                        lost in the feeling of being gang-banged."

                        $ changed_stats = [("constitution", dice(3)), ("libido", dice(3))]


                elif fix == "multiple orgasms":

                    man "Here, have a whiff of this! You're not going to regret it."

                    "The man stuffs a pouch in [girl.name]'s face, forcing her to inhale a strange power out of it. Spice, for sure."

                    girl.char "Aw! What is this... I... feel strange..."

                    play sound s_moans

                    "As the men keep fucking [girl.name] relentlessly, she seems to drift away into some sort of trance."

                    "Her nipples stand up until they reach an almost unnatural size, and her vagina starts to flow love juices like a fountain. She is staring at the crowd without seeing them, drool coming out of her mouth."

                    girl.char "Rhaaa... Rhaaaa..."

                    "Suddenly, she arches her back, cumming as one of the guys lets go of a wad of cum over her face and hair."

                    with flash

                    play sound s_orgasm

                    girl.char "AAAAAH!!!"

                    with flash

                    "Instants later, she starts shaking again, rocked by another orgasm."

                    with flash

                    girl.char "RAAAAH!!!"

                    with flash

                    pause 0.5

                    $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["bisexual", "cumshot"])

                    if pic:
                        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with doubleflash

                    "She cums again, and again. It's like she cannot stop."

                    if attitude > 100:

                        girl.char "CUM, CUUUM!!! MORE!!!"

                        with flash

                        "One by one, the men cum inside and outside her. She grasps around for cocks, aiming them at her face and holes, in order to receive more semen."

                        play sound s_screams
                        with doubleflash

                        "Every shot she gets, she cums harder than the last time, until she is left completely passed out in a large pool of dirty semen."

                        $ changed_stats = [("libido", 2+dice(3)), ("sex", dice(3))]

                    else:

                        girl.char "Arrrh... Ahaaa... Ngggh..."

                        with flash

                        "She struggles to contain herself, but the constant orgasms make her mind go blank."

                        with doubleflash

                        "Eventually, she passes out, as the customers keep fucking and cumming in and outside her."

                        man "*pant*, *pant*... Dude, what a mess... I'd hate to be the cleaning staff! Thank you, bro, here is your cash!"

                        $ changed_stats = [("libido", dice(3)), ("sex", dice(3))]

                    $ girl.interactions = 0

            else:

                girl.char "NOOOO!!!"

                "[girl.name] shakes her head vigorously and tries to stave off the hands and cocks that constantly reach for her body."

                "The man who is fucking her tries to pin her down with his cock, but she fights him back, pushing him away with both hands."

                $ changed_stats = [("constitution", -1*dice(3)), ("sex", -1*dice(3))]

        elif fix == "bukkake":

            "The men order [girl.name] to get on her knees. The leader brings his erect cock close to her face, poking her nose with it."

            if attitude > 0:
                "She knows she has a job to do, and so she gets down to it."

                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["bisexual", "cumshot"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with fade

                if attitude > 100:

                    girl.char "Dear customers, please cover my lowly face with your thick, dirty cum..."

                    "She licks her lips as she says that, and enthusiastically helps the men around her get ready with her hands and mouth."

                    play sound s_sucking

                    girl.char "Nggh, mmh... Let me feel the taste of warm cum over my tongue..."

                    "The men are extremely excited by her teasing, and are soon joined on stage by random members of the audience. Soon, a dozen men are standing around her in a circle, masturbating."

                    play sound s_aaah

                    girl.char "Let me have it... Aaah!!!"

                    with flash

                    "The man she was sucking off suddenly cannot take it anymore, and cums a huge load inside her mouth."

                    with flash

                    "Seeing that, the man she was jerking off shoots his load right in her face."

                    play sound s_mmmh

                    girl.char "Mmmmh!!!"

                    with doubleflash

                    "Another man cums on top of her hair, then another one all over her breast. Soon, every man around her reaches their limit, and she faces upwards, eager to collect all of their cum on her willing face."

                    $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "buk"], not_tags=["bisexual"])

                    if pic:
                        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                    with flash

                    girl.char "Delishious cum...Yesh!!!"

                    with doubleflash
                    play sound s_orgasm

                    "Unexpectedly, she reaches a loud orgasm as the men keep cumming on her. She opens her mouth wide to scream, right on time to receive the last shot of semen, which she then gulps down with gusto."

                    girl.char "Mmmh... I love cum..."

                    "Some of the men are ready for a second round, and she is more than happy to oblige them, until her face is completely caked with two dozen men's cum."

                    $ changed_stats = [("service", 2+dice(3)), ("obedience", dice(3))]

                else:

                    girl.char "Please don't shoot it in my eyes..."

                    "Using her hands, she helps the men masturbating next to her, red with embarrassment as the whole crowd looks on."

                    man "Come on, use your mouth, girl."

                    "A couple of men shove their cocks inside her mouth at the same time, and she nearly chokes trying to accommodate both."

                    play sound s_sucking

                    girl.char "Ngggh!!!"

                    "The circle of men closes in on her, and soon she is completely surrounded by erect dicks, trying hard to pay equal attention to each."

                    girl.char "Aaaah... Aaaah..."

                    "The erotic look on her face as she works so many cocks at the same time is enough to bring the men overboard, and they soon start cumming."

                    $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "buk"], not_tags=["bisexual"])

                    if pic:
                        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                    with flash

                    play sound s_surprise

                    girl.char "Oh!!!"

                    with doubleflash

                    "The first man cums right inside her hair, and a second one follows."

                    with flash

                    "Another one shoots his load right on her nose, and another one catches her as she opens her mouth to breathe."

                    girl.char "*cough* *cough*"

                    "[girl.name]'s face is a mess of caked cum and washed-out make-up. The men wipe their cocks on her hair with a satisfied look on their face."

                    $ changed_stats = [("service", dice(3)), ("obedience", dice(3))]

            else:
                girl.char "No!!! Get these filthy things out of my face!"

                man "C'm'on, be nice... We'll reward you with some nice cum..."

                girl.char "Fuck off! I said no!!!"

                if girl.is_("dom"):

                    play sound s_punch
                    with vpunch

                    "The man tries to rub his cock alongside her face. She punches him right in the balls."

                    play sound s_wscream

                    man "OUCH!!!"

                else:
                    "She starts crying and shaking her head as the lewd men rub their cocks on her face and hair. One of them tries to push his cock inside her mouth, but she clenches her teeth tight shut."

                $ changed_stats = [("service", -1*dice(3)), ("obedience", -1*dice(3))]

        if attitude > 0:
            if attitude > 100:
                man "BEST. BIRTHDAY. EVER!!! Thank you so much, bro! I was supposed to save some of my birthday money, but what the hell... Here is all I have!"
                $ gold = 200

            else:
                "He drops you a pouch of gold. Once you take out the cleaning costs, you wonder if you really made a profit."
                $ gold = 100

            $ gold = (gold + dice(gold)) * district.rank
            $ MC.gold += gold

            play sound s_gold

            "You have earned [gold] gold."

        else:

            man "Damn! That bitch!"

            play sound s_crowd_boos

            "People in the crowd are sympathetic to [girl.name]'s struggle, and some rise to defend her. A few brawny types get on stage and start shoving the guys aside."

            you "People, please! No fighting!"

            play sound s_punch
            with vpunch

            "Something hits you on the back of the head, and before you know it, a brawl erupts in the strip club."

            "[girl.name] crawls out of sight, covering herself as best she can. You have to call security to put the situation under control."

            man "Hey! They knocked out two of my teeth! Thanksh for nothing, ashhole! *mad*"

            "The men leave without paying. You curse them all to the seven hells."


    elif fix == "wet":
        $ rep_impact = True

        "You order the helpers to set up a beach-like decor and bring out an inflatable pool for [girl.name]."

        you "I want you to put on a sexy swimsuit, and play in the water... Make it interesting!"

        if attitude > 100:
            girl.char "Of course, Master [MC.name]."
        elif attitude > 0:
            girl.char "I understand."
        else:
            girl.char "Aw... Must I, really?"


        $ pic = girl.get_pic("swimsuit", and_tags=["profile"], not_tags=extended_sex_acts)
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        "The customers clap enthusiastically as [girl.name] appears, wearing a skimpy swimsuit."

        play sound s_splash

        "She enters the pool in front of the audience, making a show of splashing water around."

        if attitude > 100:

            "[girl.name] takes a series of suggestive poses, tugging on her swimsuit in all the right places to give the crowd a glimpse of what's underneath it."

            play sound s_crowd_cheer

            "After teasing the audience for a few minutes, she playfully removes the top of her swimsuit, exposing her glistening wet breasts."

            $ pic = girl.get_pic("swimsuit", "naked", and_tags=["strip"], soft=True)

            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with fade

            "Shaking her boobs from side to side, she makes sure to give the audience a great view, before proceeding with removing the bottom of her swimsuit."

            "Before she takes it all off, she tugs at it, rubbing the fabric against her slit for everyone to see."

            play sound s_mmmh

            girl.char "Aaaah! ♥"

            "Feeling so many eyes on her, she almost came, but holds herself. Spreading her pussy lips, she exposes her pink vagina to the crowd who goes wild with excitement."

            "The show is now over, but she is just too horny to leave like that. Rubbing her wet clit with her hand, she starts moaning like a wild animal."

            play sound s_moans

            $ pic = girl.get_pic(list(selected_fix.tag_list) + ["mast"], and_tags=["orgasm"]+and_tag, not_tags=["bisexual", "group"])
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with fade

            girl.char "Mmmh, aaah..."

            with flash
            play sound s_orgasm

            girl.char "AAAAH!!!"

            "After a few moments, she brings herself off in front of the audience, cumming hard and splashing a mix of love juice and water around."

            "The customers give her a standing ovation. This is going to be the talk of the evening."

            $ changed_stats = [("body", 2+dice(3)), ("sensitivity", dice(3))]

        elif attitude > 0:

            "[girl.name] plays around in the water, getting herself completely wet. Soon, her tight swimsuit begins to highlight the shape of her nipples and vagina, and she playfully runs an inviting finger alongside them."

            play sound s_crowd_cheer

            "Cheered on by the crowd, she turns to the back of the stage, and slowly begins to remove her swimsuit."

            play sound s_dress

            $ pic = girl.get_pic("swimsuit", "naked", and_tags=["strip"], soft=True)
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with fade

            "Standing naked, she starts pouring water on her sensitive body, her nipples perking up for everyone to see."

            "She finishes her dance by lying naked by the side of the pool, blowing kisses to the audience as they applaud her performance."

            $ changed_stats = [("body", dice(3)), ("sensitivity", dice(3))]

        else:

            "[girl.name] hesistantly walks around in the water, embarrassed at being looked at by a bunch of horny customers."

            play sound s_splash

            pause 0.5

            play sound s_splash

            "She tries to give a suggestive dance, but only manages to splash around in the pool aimlessly."

            play sound s_crowd_boos

            "The crowd quickly tires of this pitiful spectacle. You decide it's best to move on with the regular program for the evening."

            $ changed_stats = [("body", -1*dice(3)), ("sensitivity", -1*dice(3))]

    elif fix == "cosplay":
        $ rep_impact = True

        "You take her backstage and tell her to wear a sexy uniform."

        you "Pick anything you want. But do not wear any underwear."

        if attitude > 100:
            girl.char "Of course, Master... I already have something in mind... Ah, this will be perfect!"

        elif attitude > 0:
            girl.char "A uniform? Mmmh..."

        else:
            girl.char "Uh? B-But..."

        if attitude > 100:
            $ and_tag += ["libido"]

        $ pic = girl.get_fix_pic(fix=selected_fix, and_tags=and_tag, not_tags=extended_sex_acts)
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        you "And now, Ladies and Gentlemen, please welcome our cute girl idol: [girl.fullname]!"

        "[girl.name] gets up on stage, wearing a cute costume. She walks around the stage like a catwalk with a hand on her hip, turning from time to time to face the audience."

        man "Look at this... She doesn't have panties on!"

        if attitude > 100:
            "She seems happy someone noticed she is naked underneath, and sets aside some of her clothing to reveal more."

            girl.char "Dear customers, feel free to take a good look at my slutty body... ♥"
            play sound s_dress

            show screen show_event(girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["naked"], not_tags=all_sex_acts + ["group", "bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with fade


            "Enjoying all the attention she is getting, [girl.name] starts shedding her clothes one by one, throwing them at the audience members."

            play sound s_mmmh

            girl.char "I feel so hot... Mmmh..."

            play sound s_crowd_cheer

            "Customers fight over who is going to get each item. You almost get a riot on your hands."

            $ changed_stats = [("refinement", 2+dice(3)), ("libido", dice(3))]

        elif attitude > 0:
            "She blushes bright red, but makes no effort to hide her private parts. Instead, she continues walking around the stage, taking increasingly suggestive poses."

            man "Show us more! Give us some sugar, baby!"

            play sound s_ahaa

            girl.char "Ahaa... You guys are so demanding..."

            "Pouting, she starts removing her top slowly, exposing her breasts to the crowd."

            play sound s_dress

            $ pic = girl.get_fix_pic(selected_act ,selected_fix, and_tags=and_tag, not_tags=all_sex_acts + ["group", "bisexual"])
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with fade

            girl.char "What are you making me do... Mmmmh..."

            play sound s_mmmh

            "Making a show of it, she removes her bottom too, standing naked among a pile of her colorful clothes."

            play sound s_crowd_cheer

            "She lets the customers admire her body for a while, then gives them a cute wink, and disappears backstage."

            $ changed_stats = [("refinement", dice(3)), ("libido", dice(3))]

        else:
            "Hearing that, [girl.name] rapidly starts to lose her composure."

            play sound s_surprise

            girl.char "Oh!"

            "Her face flushed with embarrassment, she recoils from the crowd, trying to cover her body with her hands."

            girl.char "It's not... I didn't mean..."

            man "Come on, slut! We want to see more!"

            girl.char "N... No!!!"

            "Feeling extremely self-conscious, [girl.name] runs off backstage, red with shame and her arms wrapped around her body."

            play sound s_crowd_boos

            man "Come back here! Boooh!"

            "The crowd is pretty unhappy. You quickly order your staff to move on with the next program."

            $ changed_stats = [("refinement", -1*dice(3)), ("libido", -1*dice(3))]

    elif fix == "vibrators":
        $ rep_impact = True

        "You hand [girl.name] a small egg-like vibrator."

        you "Here, use this."

        if attitude > 100:
            play sound s_mmmh

            girl.char "Mmmh... You know what I like..."

        elif attitude >0:
            play sound s_sigh

            girl.char "This? In front of everyone? Aw..."

        else:
            play sound s_surprise

            girl.char "What is this? Wait... You must be kidding!!!"

            you "Do it."

        "The crowd is getting impatient. They cheer as they see [girl.name] come back to the stage."

        girl.char "Thank you for waiting... *blush*"

        if attitude > 100:

            "[girl.name] takes her time finding a place to sit, finally settling on the edge of the stage, with her legs dangling out."

            "People in the crowd wonder what she is about to do, but gasp as she spreads her legs wide open, her exposed panties only inches from the front row."

            girl.char "Watch closely... Mmmh..."

            $ pic = girl.get_fix_pic(selected_act ,selected_fix, and_tags=and_tag, not_tags=all_sex_acts + ["group", "bisexual"])
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with fade

            "Tugging her panties to the side, [girl.name] exposes her pussy for everyone to see. It is already glistening with her love juices."

            play sound s_vibro

            girl.char "Aaaah!"

            "Activating the vibrator, [girl.name] brushes it over her clit. Her body jerks backward at the sensation."

            play sound s_moans_quiet

            girl.char "Mmmh... Aaah..."

            "The customers hold their breath, looking at her hypnotic movements as she masturbates in front of them."

            girl.char "Oh... It feels so good..."

            "Unable to stop herself, [girl.name] rips her top off, freeing her boobs, and proceeds to tug and twist her erect nipples."

            girl.char "Aaaah!!!"

            "[girl.name]'s pussy is overflowing with wet juice now. She increases the power of the vibrator, all the way to the maximum of 11."

            with flash
            play sound s_scream

            girl.char "AAAAAH!!!"

            play sound s_orgasm_young
            with doubleflash

            "Cumming hard, [girl.name] splashes the front row with her love juice as she buries the vibrator deep into her clitoris."

            play sound2 s_crowd_cheer

            "The crowd gives her a standing ovation, as she is rocked by the spasms of another powerful orgasm."

            $ changed_stats = [("sensitivity", 2+dice(3)), ("service", dice(3))]

        elif attitude > 0:

            "Feeling shy, [girl.name] walks small steps to the front of the stage, looking at her shoes. The customers look at her expectingly."

            "Finally finding her resolve, she sits down on the floor. Holding her knees, she then proceeds to spread her legs apart."

            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=all_sex_acts + ["group", "bisexual"])
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with fade

            play sound s_ahaa

            girl.char "Ahaa..."

            "The crowd lets out a collective gasp as they realize she isn't wearing her panties."

            "She looks to the side, her face bright red, as the audience takes a good long look at her exposed pussy."

            "After enduring the crowd's gaze for a while, she finally finds the courage to move on."

            play sound s_vibro

            "Bringing the buzzing vibrator close to her pussy, she starts working it on the outside, circling around her clit and labia."

            play sound s_mmmh

            girl.char "Oooh..."

            "Her teeth are clenched and she has a look of intense concentration. Nevertheless, the sex toy is slowly working its magic, and soon she starts loosening up."

            play sound s_moans_quiet

            girl.char "Ah, aaah, ahaa..."

            "She is now using the vibrator directly on her clit and pussy lips, drawing out her love juices and making the sex toy slippery."

            girl.char "Ooh... Aaah..."

            "She feels an intense mix of shame and pleasure as she feels the curious gaze of many strangers on her exposed body."

            girl.char "Everybody's watching... Oh... I'm such a slut... Aaaah!!!"

            play sound s_aaah
            with flash

            "Unexpectedly, the feelings become too much for [girl.name], and she starts cumming, shaking wildly."

            play sound s_orgasm_young
            with doubleflash

            "She keeps cumming for a long moment, her juice spilling out of her loose pussy. Then she falls down on her back, panting, as the vibrator rolls away from her open hand."

            you "That was a nice show..."

            $ changed_stats = [("sensitivity", dice(3)), ("service", dice(3))]

        else:
            "[girl.name] looks very awkward, and she gives you a resentful look."

            "Bringing a chair to the center of the stage, she sits down nervously, her knees tightly held together."

            "She stays there, unmoving, for a while. The customers wonder what's going on."

            man "Move it, girl!"

            play sound s_vibro

            "Frowning, [girl.name] reaches for the vibrator. She opens her legs a little, inch by inch, and places her hand with the vibrator between her thighs."

            play sound s_surprise

            girl.char "Eeek!"

            "As she pushes the vibrator into the fabric of her panties, she pulls it out immediately, taken aback by the unexpected sensation."

            "She struggles with the vibrator for while, taking it on and off, squirming uncomfortably. The customers are upset that they can't see anything, and nothing seems to happen."

            "Someone yawns. [girl.name] starts tearing up. You can see it's a disaster in the making, and tell your staff to hurry with the next part of the show."

            $ changed_stats = [("sensitivity", -1*dice(3)), ("service", -1*dice(3))]


    elif fix in ["cum on face", "cum in mouth"]:

        $ rep_impact = True

        $ pic = girl.get_fix_pic(selected_act, fix_dict["oral"], and_tags=and_tag, not_tags=all_sex_acts + ["group", "bisexual", "cumshot"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        "After [girl.name] gets down on her knees, you pat her head, then pull her pretty face towards your erect cock."

        if attitude > 100:

            "Lovingly, she sticks her tongue out, starting to lick your balls thoroughly, working her way up to the tip of your cock."

            play sound s_sucking

            girl.char "Mmmh... It's so hot..."

            "Licking her lips, she wraps her mouth around the tip of your cock, using her tongue to tease your urethra, tasting the pre-cum which is starting to leak out."

            play sound2 s_mmmh

            girl.char "Mashter... I hope you have saved a lot of cum for me..."

            "The crowd lets out a cry of admiration as [girl.name] behaves like a perfect sex pet, taking your cock as deep as she can inside her mouth."

            girl.char "Ngggh..."

            "You enjoy looking into her eyes as she continues sucking on your cock energetically, using her tongue to titillate your most sensitive parts."

            girl.char "Hnn... Hnnn..."

            "[girl.name] loves pleasuring your cock, and it seems she is feeling it as well. Using her hands to free her tits from her dress, she starts massaging her boobs and tugging her nipples."

            "You are feeling the heat too, and soon you are nearing your limit."

        elif attitude > 0:

            "Planting a soft kiss on the base of your cock, she starts licking the front timidly, massaging your balls as she works her way up."

            play sound s_sucking

            girl.char "Mmmh..."

            "After she reaches the top, she licks the head of your cock carefully, before putting it inside her mouth."

            play sound2 s_ahaa

            girl.char "Nggh..."

            "The crowd admires her technique as she starts sucking your cock, with wet, lewd noises."

            girl.char "Hnn... Ngh..."

            "She increases her pace, and you start moving your hips in rhythm, literally fucking her face."

            girl.char "Nghhhh..."

            "She makes erotic sounds as you slide in and out of her hot mouth, and you soon feel close to your limit."


        else:

            "She tries to turn away, but you hold her head with both hands, rubbing your dick in her face."

            play sound s_surprise

            girl.char "No! This is disgusting!"

            "Ignoring her, you pinch her nose. As she's gasping for air, you slide your cock into her open mouth."

            play sound s_sucking

            "Her eyes widen with shock as you push your cock all the way down her throat."

            "The crowd is watching intently as you force [girl.name] to pleasure you."

            girl.char "Hnnn..."

            "[girl.name] is completely passive, so you decide to take matters into your own hands. Grabbing her hair, you start fucking her mouth rhythmically."

            girl.char "Nghh!!!"

            "[girl.name]'s roll back and she almost retches as you fuck her throat mercilessly."

            "She isn't making things easy for you, but you still manage to reach your limit after raping her mouth for a few moments."



        if fix == "cum on face":
            "Pulling out, you decide to let yourself cum all over her face."

            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=all_sex_acts + ["group", "bisexual"])
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with fade

            with flash

            girl.char "Haaaa!!!"

            with doubleflash

            "You shoot a load of hot, thick cum square into her face."

            if attitude > 100:

                with flash
                play sound s_orgasm

                girl.char "HAAAAA!!!"

                "[girl.name] loves it so much that she reaches her own climax as she feels the shame and excitement of getting a public cumshot in front of everyone."

                "After you finish, she plays with your semen lovingly, smearing the white cum all over her face, before licking her hands clean with a blissful look."

                girl.char "Oh, Master [MC.name]... I'm so lucky you chose to nurture my skin with your precious semen..."

                $ changed_stats = [("service", 2+dice(3)), ("obedience", dice(3))]

                play sound s_crowd_cheer

                $ girl.change_love(3)

            elif attitude > 0:

                play sound s_aaah

                girl.char "Aaaah..."

                "[girl.name] closes her eyes and opens her mouth to receive your cum, bracing for the cumshot."

                "She is amazed by the amount you are able to shoot, and after you are finished, her face is completely covered with sticky semen."

                girl.char "Thank you, Master..."

                $ changed_stats = [("service", dice(3)), ("obedience", dice(3))]

                play sound s_crowd_cheer

                $ girl.change_love(2)

            else:

                play sound s_scream_loud

                girl.char "NOOO!!!"

                "[girl.name] desperately turns her head left and right, trying to avoid your cumshot."

                "Some of the semen lands in her hair and ears, but you mostly miss."

                girl.char "EW!!! Get this off me!!!"

                "The crowd is disappointed by this anticlimax."

                play sound s_crowd_boos

                $ changed_stats = [("service", -1*dice(3)), ("obedience", -1*dice(3))]

                $ girl.change_love(-2)

        elif fix == "cum in mouth":

            "You cannot hold it anymore. Taking your cock out, you shoot your load right into her open mouth."

            with flash

            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=all_sex_acts + ["group", "bisexual"])
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with fade

            girl.char "NGGGH!!!"

            if attitude > 100:

                play sound s_orgasm
                with doubleflash

                "As hot, thick cum lands on her tongue and in her mouth and the taste overcome her senses, [girl.name] reaches her own climax, soiling her panties with her love juice."

                with flash

                "Her eyes roll back inside her skull as she takes your dick inside her mouth, gulping every ounce of cum while she shakes with pleasure from her powerful orgasm."

                "The customers are amazed by you both as you keep cumming and she keeps drinking semen for what seems like a whole minute."

                "When finally, reluctantly, she lets go of your cock, she turns towards the audience, proudly showing her cum-filled mouth, before guzzling it all down."

                $ changed_stats = [("service", 2+dice(3)), ("constitution", dice(3))]

                play sound s_crowd_cheer

                $ girl.change_love(3)

            elif attitude > 0:

                play sound s_mmmh

                with doubleflash

                "Cum lands in and around [girl.name]'s mouth and quickly fills it, as she struggles to keep it all in."

                girl.char "Nggh..."

                "Soon, hot white semen is dripping onto her body and clothes, staining her with sticky cum."

                "After you finish, she turns and salutes the audience, who applaud the sight of her soiled face and clothes."

                $ changed_stats = [("service", dice(3)), ("constitution", dice(3))]

                play sound s_crowd_cheer

                $ girl.change_love(2)

            else:

                with doubleflash

                girl.char "NGGGH!!!"

                "Tears of anger and disgust flow from her eyes as she feels the hot cum invade her mouth."

                play sound s_scream_loud

                girl.char "EEEK!!!"

                "Spitting it out, she almost throws up, drooling cum all over the floor."

                girl.char "*cough*, *cough*..."

                "Even though only a little got into her mouth, she spits and coughs for long moments, looking like she's about to get sick. The customers feel let down by her poor performance."

                play sound s_crowd_boos

                $ changed_stats = [("service", -1*dice(3)), ("constitution", -1*dice(3))]

                $ girl.change_love(-2)

    elif selected_act == "anal" and fix in ["cowgirl", "piledriver", "spooning"]:

        $ rep_impact = True

        if not girl.naked:
            "One by one, she removes her clothes, until she is standing buck-naked in front of the rowdy crowd."

        show screen show_event(girl.get_pic("naked", "profile", soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        "You instruct her to spread her buttcheeks for the crowd."

        if attitude > 100:
            "She is all too happy to comply, proudly displaying her loose butthole for everyone to see."

        elif attitude > 0:
            "Shivering with shame, she follows your order, turning her back to the crowd and spreading her buttcheek open."

        else:
            "She gives you a horrified look, and freezes in her tracks. Taking the initiative, you grab her arms and flip her over, forcing her to show her ass to the crowd."

        play sound s_punch
        with vpunch

        girl.char "Ouch!"

        "You slap her butt hard, leaving a red mark, before turning to address the customers."

        you "How many of you would like to see me fuck this slut-slave in the ass tonight? Let me see a show of hands!"

        play sound s_crowd_cheer

        "The crowd goes wild in approval, and a sea of hands rise in support."

        you "All right then... Let's get to it!"

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=all_sex_acts + ["group", "bisexual", "cumshot"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        if fix == "cowgirl":
            "Lying down, you instruct [girl.name] to position herself on top of you. Except this time, you position your erect cock at the level of her anus, not her slit."

        elif fix == "piledriver":
            "Pushing [girl.name] on her back, you lift her legs and ass in the air, placing your erect cock at the entrance of her anus."

        elif fix =="Spooning":
            "You both lay down on the stage, and you position yourself behind her, lifting one of her legs in the air and placing your erect cock near her butthole."

        if attitude > 100:
            play sound s_mmmh

            girl.char "Ooh... Master, your dick feels so hot... Will this fit inside my ass?"

            play sound s_ahaa

            "She moans erotically as you rub the tip of your cock against her exposed asshole."

            girl.char "Oh... I'm getting wet..."

            "The feeling of your cock against her ass makes her very horny. She starts rubbing her clit, her love juice flowing out as you push your cock inside her ass."

            play sound s_moans

            girl.char "Oh! Master! It's coming in!"

        elif attitude > 0:
            play sound s_aaah

            girl.char "Oh, Master... This is so naughty..."

            "She braces herself, as you slowly push your hard cock inside her exposed butt."

            play sound s_moans

            girl.char "It's so big... Aaaah..."

        else:
            play sound s_scream

            girl.char "No, don't do that, please! Not in my ass!!!"

            "Ignoring her, you spread her legs wide, pressing your hard cock against her tight butthole."

            play sound s_screams

            girl.char "No! It hurts! Nooo!!!"


        if fix == "cowgirl":
            with vpunch
            $ text1 = "从她身下"
        elif fix == "piledriver":
            with vpunch
            $ text1 = "从她身上"
        elif fix == "spooning":
            with vpunch
            $ text1 = "从她背后"


        girl.char "HAAAA!!!"

        "Pushing harder, your cock starts entering her asshole [text1]."

        if attitude > 100:
            "She is well-used to being fucked in the ass, and her hungry butt swallows your whole cock easily. She contracts her ass around your cock, giving you an amazing feeling."

            girl.char "Aaah!!! It's so good... Fuck me, Master [MC.name]!!!"

        elif attitude > 0:
            "Your cock seems too big for her tight asshole at first, but after a few moments, she relaxes a little, welcoming your cock inside her."

            girl.char "It's so hot... inside my ass... Aaaah..."

        else:
            "She tries to resist, crying bitter tears as you painfully force your way inside her ass."

            girl.char "Let me go! Please! Nooo..."

        "You start moving back and forth, slowly fucking her ass in front of the captivated audience."

        if attitude > 100:
            "[girl.name] is completely lost in the moment, masturbating wildly while you pound her ass with abandon."

            girl.char "Oh Master! Oh, Master! It's so good!!! I'm... I'm..."

            "Increasing your pace, you ram your cock deeper and deeper inside her loose asshole."

            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cin"], not_tags=["group", "bisexual"], strict=True)
            if not pic:
                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "creampie"], not_tags=["group", "bisexual"])

            if pic:
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

            with flash

            play sound s_orgasm

            girl.char "I'm CUUUUMING!!!"

            with doubleflash

            "She screams in exctasy as you shoot a load of hot cum deep inside her belly, sending her over the top."

            with flash

            girl.char "Fill me up, Master!!! Fill my ass with your delicious semen! It's so GOOD!!!"

            "The crowd stands up and applauds you as you pop your cock out of [girl.name]'s swollen asshole, shooting more cum onto her pussy and belly."

            play sound2 s_crowd_cheer

            $ changed_stats = [("anal", 2+dice(3)), ("constitution", dice(3))]

            $ girl.change_love(3)

        elif attitude > 0:
            "[girl.name] starts panting with a mix of pain and pleasure as your large cock rams her [text1]."

            girl.char "Oh, Master... You're going to rip me apart..."

            "She clenches her teeth, trying to keep her voice down as her moans become more intense. After fucking her ass mercilessly for a few minutes, you feel ready to cum."

            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cin"], not_tags=["group", "bisexual"], strict=True)
            if not pic:
                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "creampie"], not_tags=["group", "bisexual"])

            if pic:
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

            with flash

            play sound s_orgasm_fast

            girl.char "AAAAH!!!"

            with doubleflash

            "Cumming hard, you spurt a load of warm cum deep inside her butt, filling her belly with your semen."

            girl.char "Ooooh!!! It's so hot! I'm burning inside!!!"

            "You slowly remove your cock from inside [girl.name], white semen dripping out of her gaping asshole. The crowd appreciates the show."

            play sound2 s_crowd_cheer

            $ changed_stats = [("anal", dice(3)), ("constitution", dice(3))]

            $ girl.change_love(2)

        else:

            play sound s_screams

            girl.char "It hurts! AAAH! It hurts!!! You're going to tear my ass apart!!!"

            "[girl.name] is screaming in pain, and it's clear she isn't enjoying any of this. Some people in the audience start to boo."

            play sound s_crowd_boos

            man "Get off her, you bastard!"

            "Some of the customers move towards the stage menacingly, itching for a fight."

            "Reluctantly, you stop what you're doing and remove yourself from [girl.name]'s ass, retreating backstage with your pants around your ankles."

            $ changed_stats = [("anal", -1*dice(3)), ("constitution", -1*dice(3))]

            $ girl.change_love(-2)

    elif fix == "handjobs":
        $ attitude = girl.get_sex_attitude(selected_act, [fix, "oil"]) + girl.get_love()

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["wet"]+and_tag, not_tags=["group", "bisexual", "cumshot"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        if attitude > 100:
            "Smiling obediently, [girl.name] pours a large amount of oil on your erect cock, before starting to massage it with both hands."

            play sound s_sucking

            girl.char "Oh, Master... Your dick is so hard and hot..."

            "She starts massaging your balls, while still rubbing your shaft with her other hand."

            girl.char "Is it good, Master? I want you to feel good..."

            "She spits on your cock, jerking you with a mix of oil and saliva. She watches with fascination as your cock grows even bigger, throbbing between her hands."

            girl.char "Master... It's growing..."

            you "Keep going... Don't stop..."

            "Obligingly, [girl.name] increases her pace and pressure, bringing her face only inches from your cock. You can feel her hot breath on your balls as you reach your limit."

            girl.char "Master [MC.name]... Cum for me..."

            $ changed_stats = [("service", 2+dice(3)), ("constitution", dice(3))]

        elif attitude > 0:
            "Blushing, [girl.name] does what she's told, rubbing some oil on your erect cock."

            play sound s_ahaa

            girl.char "Master... It's throbbing..."

            play sound s_sucking

            "Your dick grows larger as she starts caressing your shaft, lightly at first, then grabbing it with her oily hands."

            girl.char "It's very hot..."

            "She starts jerking you off, slowly at first, then increasing her pace. Feeling her touch, you soon become even harder."

            girl.char "Master... Are you close to..."

            $ changed_stats = [("service", dice(3)), ("constitution", dice(3))]

        else:
            "Reluctantly, [girl.name] rubs massage oil on her hands. She stares at your cock for a while, doing nothing, looking unhappy."

            you "Come on! What are you waiting for?"

            "Taking her hand, you guide it towards your cock, forcing her to grab your cock."

            girl.char "Ew! It's throbbing!"

            "A look of disgust on her face but afraid to displease you, [girl.name] starts jerking your cock mechanically."

            you "Keep going..."

            "[girl.name] has no technique and nothing feels right. After a while, your cock begins to go limp, and you feel this is not going anywhere."

            you "It's useless. You should work on your technique, it's sorely lacking!"

            girl.char "Aw..."

            $ changed_stats = [("service", -1*dice(3)), ("constitution", -1*dice(3))]

            $ girl.change_love(-1)

            return

        with flash

        girl.char "Ah!"

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["cumshot", "wet", "cof"]+and_tag, not_tags=["group", "bisexual"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with doubleflash

        "Cumming suddenly, you shoot your load all over [girl.name]'s delicate hands."

        if attitude > 100:

            "She looks on with fascination as your cum spurts everywhere, including on her face."

            "Carefully licking all the cum off her hands, she also sucks your dick clean before giving you a happy smile."

            girl.char "Thank you so much, Master! I'm always happy to be of service."

            $ girl.change_love(3)

        else:

            "She is impressed by the amount of cum you released, using a warm towel to wipe your cock clean."

            girl.char "Thank you, Master. I hope you're more relaxed..."

            $ girl.change_love(2)

    elif fix == "titjobs":
        $ attitude = girl.get_sex_attitude(selected_act, [fix, "oil"]) + girl.get_love()

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["wet"]+and_tag, not_tags=["group", "bisexual", "cumshot"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        if attitude > 100:
            "Smiling seductively, [girl.name] pours massage oil liberally on her exposed breasts."

            girl.char "Master, I'd be happy to service you with my boobs..."

            "Rubbing her oily tits together, she moans with pleasure as she pinches her erect nipples."

            play sound s_mmh

            girl.char "Master... Let me make you comfortable..."

            "Slipping your hard cock between her soft breasts, she presses them together around your dick."

            girl.char "It's so hot... It's burning..."

            play sound s_sucking

            "Breathing heavily, [girl.name] starts rubbing her body against yours, wrapping your dick in a tunnel of flesh."

            girl.char "Is it good, Master? I want to make you cum..."

            "She is enjoying herself as much as you, rubbing and tugging her nipples with her free hands while massaging your cock with her tits."

            girl.char "Ooh... Aaah..."

            "After a while, you feel ready."

            girl.char "Master... Please... Cum all over my breasts! I beg you..."

            with flash

            girl.char "Aaah!"

            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["cumshot", "wet", "cof"]+and_tag, not_tags=["group", "bisexual"])
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

            with doubleflash

            "Reaching your limit, you arch your back as [girl.name] increases her pressure, sending you over the top."

            with flash
            play sound s_orgasm

            girl.char "AAAAH!!!"

            "As you shoot white semen all over her sensitive tits and face, [girl.name] cums spontaneously."

            girl.char "Oh, Master... I'm so happy..."

            $ changed_stats = [("service", 2+dice(3)), ("sensitivity", dice(3))]

            $ girl.change_love(3)

        elif attitude > 0:

            "Pouring oil on her tits and your cock, [girl.name] comes down on you, sliding up and down your body."

            girl.char "Is it... Good?"

            "Sliding over your cock, she can feel it grow firmer, as you can feel her nipples hardening."

            play sound s_mmmh

            girl.char "Mmmh..."

            play sound s_sucking

            "Pressing her tits against your cock, [girl.name] keeps teasing you, until you are about to reach your limit."

            girl.char "Oooh..."

            "Grabbing her breasts, you wrap them around your cock, getting ready to shoot your load."

            with flash

            girl.char "Aaaah!"

            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["cumshot", "wet", "cof"]+and_tag, not_tags=["group", "bisexual"])
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with doubleflash

            "Spurting your load on her body and tits, you watch with satisfaction as your white cum slides down her oiled body."

            girl.char "Oh, Master... You made me all messy..."

            $ changed_stats = [("service", dice(3)), ("sensitivity", dice(3))]

            $ girl.change_love(3)

        else:
            "Looking unhappy, [girl.name] pours some oil on your cock, reluctantly bringing her tits in contact with it."

            girl.char "Ew..."

            "Bringing her body against yours, you start rubbing your cock against her tits."

            play sound s_surprise

            girl.char "Aah!"

            "Closing her eyes with shame, [girl.name] stays still while you grind against her body."

            "After trying to bring yourself off like this for a while, you realize this is pointless."

            you "That's not good at all. You better work on your technique, or the customers will get angry."

            girl.char "..."

            $ changed_stats = [("service", -1*dice(3)), ("sensitivity", -1*dice(3))]

            $ girl.change_love(-1)

    elif fix == "oral":
        $ attitude = girl.get_sex_attitude(selected_act, fix) + girl.get_love()

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["group", "bisexual", "cumshot"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with fade

        if attitude > 100:
            "Smiling suggestively, [girl.name] wastes no time going down towards your nether regions."

            play sound s_sucking

            "She starts drooling a wad of hot saliva on your cock to better lubricate it, before kissing and licking the length of your shaft from its head to your balls."

            "Taking your balls inside her mouth one by one, she tickles you with her tongue."

            girl.char "Do you like it, Mashter? Nggh..."

            "You don't answer, but she can feel your cock getting harder and hotter as she returns to kissing the tip of your cock, licking the pre-cum as it starts to come out."

            girl.char "Let me help you release your stress, Master... Mmmh..."

            "Finally taking your cock inside her mouth, [girl.name] rubs it hard against the inside of her cheek, giving you an obscene sight as she makes eye contact."

            girl.char "Ngggh..."

            "Her tongue wriggles around your cock, expertly stimulating the most sensitive parts. Soon, you feel her wonderful technique is about to send you over the top."

            with flash

            girl.char "MHHH!!!"

            with doubleflash

            $ pic = girl.get_fix_pic(selected_act, fix_dict["cum in mouth"], and_tags=and_tag+["cumshot", "cim"], not_tags=["group", "bisexual"])
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with dissolve

            "Your cum spurts out vigorously as you cannot hold it anymore. [girl.name] is surprised by the strong taste and sheer amount of semen you release, but welcomes it, swallowing some as the rest overflows from her mouth."

            "She licks your cock clean voluptuously, savouring the musky taste of semen, before planting an affectionate kiss on the tip of your dick, smiling."

            girl.char "Come to me anytime for stress relief, Master... *giggle*"

            $ changed_stats = [("service", 2+dice(3)), ("obedience", dice(3))]

            $ girl.change_love(3)

        elif attitude > 0:
            "Following your instructions, [girl.name] starts licking and sucking your dick as you look on in a relaxed position."

            play sound s_sucking

            girl.char "Ngh..."

            "Caressing her hair, you urge her on, gently pushing her head towards you, until your cock is bouncing against the back of her throat."

            girl.char "Ngggh!!!"

            "She recoils a bit, but keeps working your dick with her agile tongue. Covered with her saliva, your cock makes wet, obscene noises as you keep fucking her mouth."

            girl.char "Nggh... Mmmh..."

            "Suddenly, you feel an overpowering sensation coming from within."

            with flash

            girl.char "NGGGH!!!"

            $ pic = girl.get_fix_pic(selected_act, fix_dict["cumshot", "cum on face"], and_tags=and_tag, not_tags=["group", "bisexual"])

            if pic:
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

            with doubleflash

            "Popping your cock out of her mouth, you immediately start spurting cum all over her, smearing her face and hair."

            girl.char "Ohhh... Master, you made me all dirty..."

            "[girl.name] pouts at you in a cute way as she tries to untangle the mess of her sticky cum-soiled hair."

            $ changed_stats = [("service", dice(3)), ("obedience", dice(3))]
            $ girl.change_love(2)

        else:
            "[girl.name] brings her face closer to your cock with a look of disgust on her face, but seems in no hurry to take it in."

            "Losing patience, you pinch her nose, and as she gasps for air, you shove your erect cock inside her mouth."

            girl.char "Ngggh!!!"

            play sound s_sucking

            "Ignoring her muffled cries of protest, you start moving back and forth, trying to push your cock deeper."

            "But her mouth is only half-open, and you can feel her teeth raking against your cock in a very uncomfortable way. You start to worry about what might happen if she clenches her teeth."

            you "What the hell, [girl.name]... This is terrible..."

            "Frowning, you slowly take your dick out, and she coughs and spits to get rid of the taste in her mouth. You are not happy."

            you "You better work on your technique, girl. This is unworthy of the standards I am trying to set for [brothel.name]."

            $ changed_stats = [("service", -1*dice(3)), ("obedience", -1*dice(3))]
            $ girl.change_love(-2)

    elif fix == "cum inside":
        $ attitude = girl.get_sex_attitude(selected_act, fix) + girl.get_love()

        "Grabbing [girl.name]'s ass with both hands, you pull her towards you, placing your hard cock against the entrance of her pussy."

        $ lost_virginity = False
        if girl.pop_virginity():
            $ lost_virginity = True
            "[girl.name] is a virgin, and she trembles as she feels the tip of your cock pushing against her pussy lips."

        if attitude > 100:

            play sound s_mmmh

            girl.char "Oh, Master..."

            "She is already very wet, and your dick slides inside her effortlessly."

            play sound s_scream

            girl.char "Aaah! Master [MC.name] is inside me... I feel so good..."

        elif attitude > 0:

            play sound s_ahaa

            girl.char "Ahaa..."

            "Rubbing your dick against her slit, you can feel her becoming wet, covering your shaft with her love juice."

            "Groping her ass, you start pushing the tip of your cock inside. She moans as you enter her tight pussy."

            play sound s_aaah

            girl.char "Aah..."

        else:

            girl.char "W-wait..."

            "[girl.name] looks away from you, feeling very tense. You gently rub your cock against her cunt, but she remains desperately closed."

            "After cajoling her for a few minutes, trying to get her in the mood, you realize this is not getting you anywhere."

            "Tired of waiting, you simply force the tip of your cock inside her dry pussy."

            play sound s_scream

            girl.char "Master, no!!!"

        if lost_virginity:
            $ pic = girl.get_pic("virgin", "sex", "naked", and_tags=and_tag, and_priority=False, not_tags=["group", "bisexual"])
        else:
            $ pic = girl.get_fix_pic(selected_act, fix_dict["cowgirl"], and_tags=and_tag, not_tags=["group", "bisexual", "cumshot"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        if attitude > 100:
            "[girl.name] sits down on your hard cock, taking it inside all the way to her deeper regions."
            play sound s_moans

            "She moans sexily as she savors the sensation of your thick, hard cock filling up her insides."

            girl.char "Mmmmh..."

            "Moving slowly from left to right, she engulfs your cock even deeper, her love juice overflowing on your balls."

            "Putting her hands against your chest, she starts moving her hips while you lay back."

            girl.char "Oh, Master... I want you to fuck me... Fuck me hard..."

            "Sliding up and down, [girl.name] goes faster and faster, impaling herself on your cock as you stare at her bouncing wet tits. You still don't bother to move."

            girl.char "Master [MC.name]! I'm so close... Ah, ah, aah..."

            with flash

            play sound s_scream_loud

            girl.char "AAAAAH!!!"

            play sound s_orgasm

            with flash

            "Cumming hard, [girl.name] reaches a loud orgasm, screaming at the top of her lungs."

            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "cin"], not_tags=["group", "bisexual"])

            if pic:
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
            with doubleflash

            "You still haven't moved a muscle, but seeing her hot body shivering with pleasure as she squeezes your cock even tighter is enough to make you cum too."

            with flash

            "You start cumming carelessly deep inside her pussy, and she squeezes your cock harder with each shot, as if to milk you for all you're worth."

            girl.char "Aaaah... Master is filling me up with warm, sticky cum... ♥"

            "[girl.name] lays down on top of you, her panting chest weighting pleasantly against yours as thick, white semen oozes out of her gaping pussy."

            girl.char "Master... Can we do this again?"

            $ changed_stats = [("sex", 2+dice(3)), ("libido", dice(3))]
            $ girl.change_love(3)

        elif attitude > 0:

            "Blushing, [girl.char] timidly sits back on your cock, inch by inch, slowly easing it inside her."

            play sound s_ahaa

            girl.char "Master... You're so big... It won't fit..."

            "In spite of her qualms, your cock fits in just fine, helped by the wet juices that started flowing out from her pussy."

            play sound s_moans

            girl.char "Oh, Master! You are going to tear my pussy apart..."

            "Ignoring her, you start moving your hips, slamming your cock inside her as she bounces on and off."

            girl.char "Aaah... Aah... Aaaah..."

            "Panting heavily, [girl.name] holds onto you as she takes the pounding."

            girl.char "Master... I feel strange... Aaaah!!!"

            play sound s_punch
            with vpunch

            "Slapping her ass hard, you use your other hand to pinch and twist her nipple. She moans with a mix of pleasure and pain."

            girl.char "Aaaaaah..."

            with flash

            girl.char "AAAAAAAAH!!!"

            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot", "cof"], not_tags=["group", "bisexual"])
            if not pic:
                $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag+["cumshot"], not_tags=["group", "bisexual"])
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
            with doubleflash

            "Unable to hold yourself, you ram your cock up her vagina one last time, before shooting a hot load of cum deep inside her."

            with flash

            girl.char "Master!!! I'm... I'm..."

            with doubleflash

            girl.char "CUMMIIIING!!!"

            "As you release a steady flow of cum inside her, [girl.name]'s pussy squeezes your dick tight and she reaches her own climax."

            "She falls down flat on top of you, panting heavily. Bubbling semen flows out of her messed up pussy."

            girl.char "Oh, Master... You came inside me... It was too intense..."

            $ changed_stats = [("sex", dice(3)), ("libido", dice(3))]
            $ girl.change_love(3)

        else:
            "Ignoring her, you grab her thighs and push her down on your dick."

            play sound s_screams

            girl.char "Aaaaw! It hurts!"

            "[girl.char] cries with pain as you force your hard cock inside her, violating her tight pussy."

            girl.char "Aw... It hurts... *sob*"

            "She squirms, contracting her pussy muscles, trying to push your cock out."

            "After getting it only halfway in, you find yourself stuck. [girl.name] is weeping quietly, and dry as the Homokan desert."

            you "This is useless... Get off me."

            "Shoving her to the side, you get up and leave, ignoring her as she lies sobbing on the onsen floor."

            $ changed_stats = [("sex", -1*dice(3)), ("libido", -1*dice(3))]
            $ girl.change_love(-2)

    elif fix == "cum in hair":
        you "She has such nice, silky hair... Hmmm..."

        "Whipping out your dick, you start masturbating, only inches from her sleeping face."

        girl.char "Zzzz..."

        "She looks very peaceful and innocent when she's sleeping. You wonder how she would react if she knew you were jerking off right in her face."

        girl.char "Zzz... Mmh... No... Don't do that... It tickles... *snore*"

        "She seems to be having some kind of dream. She blushes and mumbles in her sleep."

        if girl.get_stat("libido") > 150:
            play sound s_mmmh

            girl.char "Mmmh... Fuck me harder... Yes... *snore*"

            "It looks like she is having an erotic dream! It turns you on. Looking at her perky nipples and flushed face, you feel about to cum already."

        elif girl.get_stat("libido") > 50:
            play sound s_ahaa

            girl.char "Oh... You're naughty... Teehee... *snore*"

            "What kind of dream is she having? She blushes. Pointing your erect cock at her, you increase your pace."

        else:
            play sound s_sigh

            girl.char "Milk shake, please... With extra thick cream... *snore*"

            "She is dreaming about foodstuff... Greedy girl."

        "Taking a hank of her hair, you wrap it quietly around your cock, feeling its soft and silky touch."

        "Jerking yourself off with her hair, you start panting louder as you feel close to cumming."

        girl.char "Mmmh... What's going on..."

        with flash

        play sound s_scream

        girl.char "AAAAH!!!"

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["group", "bisexual"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with doubleflash

        "Right as she wakes up, you reach your climax, grunting as you unload a wad of cum all over her soft hair."

        girl.char "EEEEEK!!!"

        "[girl.name] squeals and shakes her head as cum spreads on her scalp like shampoo. Before she can react, she is covered with your sticky cum."

        $ attitude = girl.get_sex_attitude(selected_act, fix)

        if attitude > 150:
            "Recovering from her surprise, [girl.name] takes in the scene and the musky scent of semen in the air."

            girl.char "Wow, Master... You made me all dirty..."

            girl.char "What kind of manners is that... You could have warned me you were doing that... *smile*"

            "She plays with the cum in her hair, fixating your cock with lust."

            girl.char "Next time, wake me up so I can help... *wink*"

            $ changed_stats = [("fetish", 2+dice(3)), ("libido", dice(3))]
            $ girl.change_love(3)

        elif attitude > 0:
            girl.char "Master [MC.name]! You came all over my hair! Uwah!"

            girl.char "I'm all sticky now... Aw, Master, you're terrible... *blush* Do you know how hard it is to wash this stuff out?"

            $ changed_stats = [("fetish", dice(3)), ("libido", dice(3))]
            $ girl.change_love(1)
            $ girl.change_fear(1)
            $ MC.evil += 1

        else:
            girl.char "What did you just do, you monster!!! My hair! My precious hair! *cries*"

            "Watching cum drip from her scalp with horror, she desperately tries to wash it off with water from the onsen."

            girl.char "Oh, this is so disgusting... I'm gonna be sick..."

            "She seems really pissed by your little prank."

            you "Come on, [girl.name], you should be used to this by now... Better not fall asleep next time, don't you think? Hehe..."

            girl.char "I HATE YOU! *sob*"

            $ changed_stats = [("fetish", -1*dice(3)), ("libido", -1*dice(3))]
            $ girl.change_love(-3)
            $ girl.change_fear(2)
            $ MC.evil += 1

    elif fix == "watersports":
        $ attitude = girl.get_sex_attitude(selected_act, fix) + girl.get_love()

        "With all this water flowing around, you feel an urge to urinate."

        you "Well... [girl.name] seems to like getting wet... Maybe I can help by giving her a little shower of my own?"

        "Taking your cock out, you aim carefully at her cute, sleeping face."

        play sound s_pee

        "Whistling, you start peeing negligently, splashing her face."

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=and_tag, not_tags=["group", "bisexual"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        play sound s_scream
        with vpunch

        girl.char "EEEK!!! *glub*"

        "Waking up abruptly, [girl.name] opens her mouth wide, only for it to be filled with your yellow pee."

        girl.char "*glub *cough*"

        if attitude > 150:
            "Disoriented at first, [girl.name] lets her slut reflexes kick in. She starts gulping down your urine as you keep peeing in her mouth."

            girl.char "*gulp* *gulp*"

            "After a while, the stream dwindles, and she swallows the last of it matter-of-factly."

            girl.char "*gulp* Mmmh, Master... What was that for?"

            you "Putting you in your rightful place, whore. Any problem with that?"

            girl.char "No..."

            $ changed_stats = [("fetish", 2+dice(3)), ("obedience", 2+dice(3))]
            $ girl.change_love(1)
            $ girl.change_fear(1)

        elif attitude > 50:

            girl.char "Ew!"

            "Shutting her eyes and mouth, [girl.name] braces herself to endure your jet, spitting your pee out little by little."

            girl.char "..."

            "The stream dwindles and soon you stop, watching her soiled face with satisfaction."

            girl.char "Aw... Master..."

            "Soiled and humiliated, [girl.char] looks down. Without a word, she goes off to dry her face with a towel."

            you "*whistle*"

            $ changed_stats = [("fetish", dice(3)), ("obedience", dice(3))]
            $ girl.change_fear(2)
            $ MC.evil += 1

        else:

            "Noisily spitting out your pee, [girl.name] retches, while you keep peeing all over her."

            girl.char "UWAAAH!!!"

            "Desperately trying to protect her face and body with her arms, she tries to run away across the bath. You try to follow her with your jet, and she squeals every time you hit."

            girl.char "NOOO!!! DISGUSTING!!! GET THIS SHIT OFF ME!!!"

            you "Come on, it's not shit... Hmmm. Maybe you would have liked that better."

            girl.char "I HATE YOU!!! UWAAAH!!!"

            "[girl.name] scrambles away, running across the onsen to safety. You laugh as she disappears in the shower area, desperate to wash herself."

            $ changed_stats = [("fetish", -1*dice(3)), ("obedience", -1*dice(3))]
            $ girl.change_love(-3)
            $ girl.change_fear(3)
            $ MC.evil += 1

    elif fix == "cum shower":
        $ attitude = girl.get_sex_attitude(selected_act, fix)
        $ rep_impact = True

        "As the early customers start pouring into the onsen, you greet them with a grin."

        you "Welcome, gentlemen, would you follow me? One of my girls needs your help with something..."

        with fade

        "Fast asleep, [girl.name] doesn't notice you and the customers grouping up around her."

        girl.char "ZZZZ... *snore*"

        man "Are you sure she's cool with that?"

        you "Why, of course she is. Sex slaves love a good cum shower, it's excellent for their skin, you know."

        "Whipping out your dick, you start masturbating right in [girl.name]'s face, soon followed by the other customers."

        girl.char "..."

        play sound s_surprise

        girl.char "Uh?"

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["masseuse"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        "[girl.name] slowly wakes up, only to find herself surrounded with erect cocks. Still half-asleep, she takes a moment to realize it is not just a dirty dream."

        girl.char "Wh... What? What's going on?"

        "She looks around her with alarm as the group jerks off even faster, panting and grunting."

        you "It's time for your deluxe shower, [girl.name]... I hope you'll enjoy it!"

        with flash

        "Unable to help himself, one of the customers cums suddenly with a groan, shooting his load right in [girl.name]'s face."

        play sound s_aah

        girl.char "Aaaah!!!"

        "[girl.name] turns away from the customer's spurting cock, only to be caught by another one's cumshot."

        with doubleflash

        girl.char "UWAAH!!!"

        with flash

        "Within moments, everyone starts cumming, shooting load after load of thick white cum all over [girl.name]."

        if attitude > 150:
            "Once she recovers from her initial surprise, [girl.name] is quick to join in on the fun."

            play sound s_aaah

            girl.char "Oh... So much cum! Aaah!"

            "Grabbing a couple of dicks around her, [girl.name] sticks her tongue out, eager to receive and taste more semen as the customers cum one by one."

        elif attitude > 50:
            "Not fully emerged from her slumber, [girl.name] still seems in a haze."

            "*spurt* *spurt*"

            "Surrounded by a blur of cocks and cumshots, she barely registers what goes on, passively letting the customers shower her with hot cum."

            play sound s_mmmh

            girl.char "Mmmh..."

        else:
            girl.char "EW!!! GET OFF ME!!!"

            "Covering her face with her hands, [girl.name] screams indignantly as the customers shower her with dirty cum."

            "Dashing for the exit, she stumbles and struggles to leave the water while the customers keep shooting their loads over her."

            girl.char "HIYAAAAH!!!"

            "She runs for the door and disappears, leaving the customers somewhat disappointed."

            $ changed_stats = [("fetish", -1*dice(3)), ("beauty", -1*dice(3)), ("constitution", -1*dice(3))]
            $ girl.change_love(-2)
            $ girl.change_fear(3)
            $ MC.evil += 1

            return

        "Before long, her hair and face are covered with sticky cum, her features barely visible through a thick layer of white semen."

        play sound s_moans_quiet

        girl.char "Nggh..."

        "Streams of cum drip down on her body, running along her curves. You approach her face with your cock for the last blow."

        girl.char "Master [MC.name]... Ish that you?"

        "[girl.name] squints, trying to open her eyes to see you clearly. That's when you shoot a massive jet of cum right in her soiled face."

        girl.char "UWAAH!!!"

        "Burning cum got into [girl.name]'s eyes and she cries out, just in time for your next load to enter her mouth."

        if attitude > 150:
            "Bravely, [girl.name] swallows it all, using fresh cum to rub her tits as you drop the last of your semen down her throat."

            play sound s_mmmh

            girl.char "Mmmh, Mashter... It'sh delishioush..."

            "As she stands there in the onsen, her face and body caked with drying cum, the customers all applaud her."

            girl.char "Thank you all, from the bottom of my heart... I am happy to be your cum toilet... *blush*"

            $ changed_stats = [("fetish", dice(3)), ("beauty", 2+dice(3)), ("constitution", 2+dice(3))]
            $ girl.change_fear(1)

        else:
            "She is drooling cum as you keep shooting load after load of white semen over her face and body."

            girl.char "There's so much... It's so hot... Aw..."

            "When you're finished, she is a poor sight, her face and body covered with drying cum. The customers leave one by one, thanking you for the fun they had."

            "After they leave, [girl.name] struggles pitifully to open her eyes, using water from the bath to try to wash her face and upper body."

            you "Thanks, [girl.name]. Oh, and when you're finished: don't forget to clean the pool!"

            $ changed_stats = [("fetish", dice(3)), ("beauty", dice(3)), ("constitution", dice(3))]
            $ girl.change_fear(1)
            $ MC.evil += 1


    elif fix == "bondage":

        $ attitude = girl.get_sex_attitude(selected_act, fix)

        play sound s_dress
        with fade

        "You use the rope to tie [girl.name] real tight, making sure the yarn is squeezing her tits and private parts tightly."

        you "Here, let me adjust this..."

        "You make sure one of the hard knots that dot the rope is positioned just between her legs, and you tighten the ropes so that it bites right into her pussy."

        play sound s_scream

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["geisha"], not_tags=["service", "sex", "anal", "group", "bisexual"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        if attitude > 125:
            "As the rough ropes bite her flesh, [girl.name] becomes flushed, her nipples perking up."

            play sound s_aaah

            girl.char "Aaaah! ♥"

            you "Is it too tight for you?"

            girl.char "No... Please make it tighter..."

            you "All right..."

            "Pulling on the ropes, you squeeze her even tighter, until she is about to suffocate. You know this is going to leave marks, but she is too aroused to care."

            play sound s_ahaa

            girl.char "Oh... Oh... *pant*... It's so good..."

            "Her love juices are trickling down her thighs, and her tongue sticks out as she struggles to breathe. You decide to give her an extra push, and yank hard at the string that bites into her pussy and ass."

            with flash
            girl.char "AAAAAH!!!"

            show screen show_event(girl.get_fix_pic(selected_act, selected_fix, and_tags=["geisha", "orgasm"], not_tags=["group", "bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8))
            with dissolve

            play sound s_orgasm
            with doubleflash

            "You yank hard and the knot nearly disappears between her pussy lips, making her love juice flash out. She cums really hard, nearly passing out from the pain and pleasure."

            girl.char "Aah... *pant*... Aaah..."

            "After she is done cumming, you send her just like that into the okiya. She is barely able to walk, her pussy making squishing noises with every step."

            $ changed_stats = [("fetish", 2+dice(3)), ("constitution", dice(3))]
            $ girl.change_love(2)
            $ girl.change_fear(2)

        elif attitude > 25:
            girl.char "Aaahaa! It hurts!"

            play sound s_scream

            "She squirms as you make the rope suit really tight, but at the same time, she rubs her thighs in a erotic way, as if fighting the sensations building up within her body."

            you "What's that? Does this make you horny?"

            play sound s_ahaa

            girl.char "No, aaah..."

            "You torture her by tugging at the ropes, pinching her nipples hard from time to time. She becomes visibly wet."

            you "It seems to me you are enjoying this... The customers will be happy..."

            girl.char "Oh, don't say that... Aaaah!!!"

            "After toying with her for a little while, you remember that the customers are waiting. You send her off to greet them, wearing nothing but the ropes."

            $ changed_stats = [("fetish", dice(3)), ("constitution", dice(3))]
            $ girl.change_love(1)
            $ girl.change_fear(1)

        else:
            "She gasps, looking at you with shock and awe."

            girl.char "*pants*... No, please, Master, this is too tight... I'm going to suffocate..."

            "She seems stricken by a panic attack. You loosen the ropes, but she's still crying with shock and pain."

            you "Damn, you're such a crybaby... All right, you'll just go work naked, then."

            "Her eyes red with tears, she is almost relieved as you take off the ropes and send her off, buck naked, to meet the customers."

            $ changed_stats = [("fetish", -dice(3)), ("constitution", -dice(3))]
            $ girl.change_love(-1)
            $ girl.change_fear(2)


    elif fix == "gags":
        $ attitude = girl.get_sex_attitude(selected_act, fix)

        play sound s_dress

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["geisha"], not_tags=["group", "bisexual"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        you "There. The customers will enjoy it more if you're silent."

        girl.char "Ngggh!!!"

        "She looks indignant, but the gag prevents her from speaking her mind on the matter. Her face flushes bright red, however, when you tell her the gag is the only thing she is allowed to wear."


        you "Now, look at me. You are forbidden to talk, so you must use your eyes to convey your feelings."

        if attitude > 100:
            "She seems intrigued by the notion, and looks at you expectantly. You lift her chin, and gaze deep into her eyes."

            girl.char "Nggh... 'as'er..."

            "She opens her eyes wide, and gives you a loving look. Her eyes seem to say she is eager to please."

            you "There, that's a perfect look for you. Make sure you serve the customers well tonight."

            "It seems she is well used to being gagged by now. A trail of saliva runs down her chin, but she doesn't seem to mind. She bows and heads back to the okiya."

            $ changed_stats = [("fetish", dice(3)), ("sensitivity", 2+dice(3))]
            $ girl.change_love(1)
            $ girl.change_fear(2)

        elif attitude > 0:
            "She looks surprised, but reluctantly, she complies. She gives you an imploring look, trying her best to look modest and ready to serve."

            you "Hmmm... Not bad. You look like a decent, quiet slave now."

            "You send [girl.name] to meet the customers, hoping she will give them a good time."

            $ changed_stats = [("fetish", dice(3)), ("sensitivity", dice(3))]
            $ girl.change_fear(1)

        else:
            "Her eyes widen, then turn to anger as she gives you a furious stare."

            girl.char "Ge' 'ha' 'hing o'' me!"

            you "What was that? I can't hear you, you know, because you're gagged."

            girl.char "GE' 'HA' 'U'ING 'HING O'' ME!!!"

            "She looks really mad. Ignoring your command, she unties the gag and spits it out."

            girl.char "I DON'T WANT THIS! Bwaaaah!!!"

            "She throws a fit, coughing and spitting, and runs away crying."

            you "Well, I guess she didn't like that too much."

            $ changed_stats = [("fetish", -dice(3)), ("sensitivity", -dice(3))]
            $ girl.change_love(-1)
            $ girl.change_fear(1)

    elif fix == "plugs":
        $ attitude = girl.get_sex_attitude(selected_act, fix)

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["geisha"], not_tags=["group", "bisexual"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        if attitude > 125:
            play sound s_sigh

            girl.char "Uhn..."

            "Without any difficulty, [girl.name]'s ass swallows the plug whole."

            girl.char "Is that... Is that it?"

            you "Well... Yeah?"

            "She frowns, looking almost disappointed."

            girl.char "I... I don't think it's my usual size... It seems tiny."

            "The plug is a good two-inches thick, but it's true that it seems too small for her trained asshole."

            you "All right, let me see if I have something else..."

            "Looking deep into your toolbox, you end up taking out a monster butt plug, almost four-inches thick, covered with little barbs. Her face lights up."

            girl.char "Oh! This one seems nice."

            "Placing the plug at the entrance of her oiled-up asshole, you force it in little by little."

            play sound s_aaah

            girl.char "Oooh!!! AAAAH!!!"

            "Her eyes roll out in her skull and she starts drooling. You are worried her anus will break, but eventually, she takes it all in."

            girl.char "AAAAH!!! It's so good... I feel complete, now..."

            "Her love juice is abundantly running down her naked thighs. You help her put on her outfit, and she goes off to meet the customers, looking very happy with her little secret."

            $ changed_stats = [("fetish", dice(3)), ("anal", 2+dice(3))]
            $ girl.change_love(2)

        elif attitude > 0:

            play sound s_ahaa

            girl.char "Ahaa..."

            "The plug goes in with a little difficulty, but eventually, she is able to hold it in."

            girl.char "Oh... It feels weird..."

            "She takes some time to get used to it, but she doesn't fight you when you tell her she must wear it for the evening."

            "You help her put on her outfit, and send her off to meet the customers."

            if girl.is_("very lewd"):
                girl.char "Welcome, mister... You'll never guess what I'm wearing underneath... *giggle*"

            $ changed_stats = [("fetish", dice(3)), ("anal", dice(3))]

        else:

            play sound s_screams

            "She contracts her pink anus tight shut, squirming as you try to force the plug inside."

            play sound s_scream_loud

            girl.char "Aaaah!!! No, it hurts!!! AAAH!!!"

            "She is screaming and crying and pleading, and you worry that her ruckus will scare away the customers in the next room."

            "Disappointed, you give up and send her off to meet the customers."

            $ changed_stats = [("fetish", -dice(3)), ("anal", -dice(3))]
            $ girl.change_fear(2)


    elif fix == "beads":
        $ attitude = girl.get_sex_attitude(selected_act, fix)
        $ rep_impact = True

        "As you tell the story, [girl.name] goes down on the floor, putting aside her kimono to reveal her exposed asshole."

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["geisha"], not_tags=["group", "bisexual"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        "The customers' oohs and aahs grow louder as [girl.name] takes out the string of seven pearls."

        if attitude > 150:
            "With a beaming smile, [girl.name] makes sure everyone sees the pearls, letting the customers touch and feel it."

            girl.char "Now, dear guests, please watch as I enact the mysterious disappearance of the Seven Pearls..."

            "As you continue with the tale, you tell the story of the gentle maiden who made the Seven Pearls disappear. Everytime you mention one of her deeds, [girl.name] slides a glistening pearl inside her ass."

            play sound s_aah

            girl.char "Aaaah!"

            "One by one, the beads disappear inside her welcoming ass, under the close scrutiny of the gathered customers. As new pearls push the former deeper and deeper, [girl.name] moans louder."

            play sound s_moans

            girl.char "Oooh... Aaaah... AAAH!!!"

            "As she slides in the seventh and last bead, the customers all rise applauding."

            you "But it wasn't over... Finally, the glorious hero showed up, and recovered all seven pearls from the pit."

            girl.char "Aaah... I can't hold it much longer... Dear guest, will you be my hero?"

            "She encourages a customer to step forward, and hands him the end of the string."

            girl.char "Please, hurry, take it out... Do it all at once..."

            "The crowd holds their breath as the customer gets ready to pull on the string."

            you "One, two..."

            with hpunch

            you "Three!!!"

            with flash
            play sound s_scream_loud

            girl.char "HAAAAA!!!"

            play sound s_orgasm
            with doubleflash

            "The customer pulls hard on the string, and the beads pop out of [girl.name]'s anus, sending her into a screaming orgasm."

            girl.char "AAAAAAH! AAAAAHHH!!!"

            "She is convulsed by her orgasm while the customers acclaim her. It was a perfect show."

            $ changed_stats = [("fetish", dice(3)), ("anal", 2+dice(3))]
            $ girl.change_fear(-2)

        elif attitude > 25:
            "She blushes bright red, looking shy as the customers wonder what she's about to do with the string of beads."

            "As you continue with the tale, you tell the story of the gentle maiden who made the Seven Pearls disappear."

            you "When the maiden found the first golden pearl, she knew she had to hide it from the demon army, for she knew that the one who gathered all seven pearls would summon a wish-granting dragon..."

            play sound s_ahaa

            girl.char "Aaaah..."

            "As you utter those word, [girl.name] pushes the first pearl inside her tight asshole, and the customers gasp."

            you "Then she found the second magic pearl, and she needed to put it somewhere safe..."

            play sound s_mmmh

            girl.char "Mmmh..."

            "[girl.name] pushes another pearl inside her asshole, moaning as it pushes the first one deeper inside her."

            you "When she found the third pearl, she thought, what the heck, she might as well put it with the others..."

            play sound s_aaah

            girl.char "Aaaah!!!"

            "[girl.name] slides another pearl inside, then another. As she reaches the sixth pearl, however, she doesn't manage to push it in..."

            play sound s_surprise

            girl.char "Aaaarh, Master, I can't do it anymore... I'm so full..."

            "The customers start laughing. Tears start creeping into [girl.name]'s eyes."

            you "Well, look at the time... That will be all for today, folks, we must move on to the next show..."

            "The customers seem happy enough with the show. You help [girl.name] limp back to the cloakroom to help her remove the beads."

            $ changed_stats = [("fetish", dice(3)), ("anal", dice(3))]
            $ girl.change_fear(-1)

        else:
            "[girl.name] looks very nervous, tears creeping up into her eyes as she endures the rude staring and leering of the crowd."

            you "There was once a very attractive maiden, but she had a secret..."

            you "...and eventually, she decided to hide the first pearl. And here's how she did it..."

            "You turn to [girl.name], and all the customers do, too. She looks at you, dumbfounded."

            you "[girl.name]?"

            girl.char "Uh?"

            you "(Psst! The beads! Put them in!)"

            play sound s_surprise

            girl.char "What???"

            you "Put them in, damnit!"

            "Confused, [girl.name] looks at the beads, then you, then the customers, then the beads again."

            girl.char "Oh! No. No, no, no..."

            you "[girl.name]! Put the fucking beads in your butt, right now!"

            play sound s_scream
            with vpunch

            girl.char "Uwah!!!"

            "You grab the beads from [girl.name]'s hands, and she starts wailing, shaking her head desperately. The customers grumble, shrug and start going away."

            you "Wait! Come back! It's just a small technical problem, it's going to be fixed soon, don't worry, haha..."

            "Ignoring your plea, all the customers leave, leaving you alone with [girl.name] crying her heart out."

        $ changed_stats = [("fetish", -dice(3)), ("anal", -dice(3))]
        $ girl.change_love(-2)
        $ girl.change_fear(1)

    elif fix == "fisting":
        $ attitude = girl.get_sex_attitude(selected_act, fix)
        $ rep_impact = True

        if girl.naked:
            "As she sings, you start playing with her exposed ass and pussy, spreading her labia for all to see."
        else:
            "As she sings, you start pulling aside her kimono, revealing her underwear. Slipping your hand inside, you lower her panties to take them off."

        play sound s_surprise

        girl.char "Ah!"

        "You make a hush gesture, and tell her to keep singing. She does her best while you play with her exposed pussy with everyone watching."

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["geisha"], not_tags=["group", "bisexual"])

        if pic.has_tag("sex"):
            $ type, stat = "vagina", "sex"
        elif pic.has_tag("anal"):
            $ type, stat = "asshole", "anal"
        else:
            $ type, stat = "vagina", "sex"

        if attitude > 150:

            play sound s_mmmh

            girl.char "Mmmh..."

            "Before long, your foreplay gets her wet, and her love juice starts leaking out of her pussy."

            "As she gets to the chorus of the song, the cry of the howling banshee, you clench your hand into a fist, and place it at the entrance of her [type]."

            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with dissolve
            play sound s_ahaa

            girl.char "Ahaa..."

            you "Now, ladies and gentlemen, get ready to hear the howl of the lonesome banshee."

            "The customers hold their breath as you push your clenched fist right into [girl.name]'s [type]."

            play sound s_scream

            girl.char "Aaaah!"

            "It seems impossible that your whole fist will fit inside her, yet slowly, her [type] opens up, aided by the love juice covering your hand."

            play sound s_scream_loud

            girl.char "AAAAH!!!"

            "As her [type] opens up to accommodate your hand, you are able to slide your fist inside her. Her eyes seem about to pop out and she screams with a mix of pain and pleasure."

            girl.char "Your hand is inside me! You're going to... Break me... Aaaaah!!!"

            play sound s_screams
            with flash

            "As you force your fist deeper inside her, she cums hard, her love juice flowing out."

            with doubleflash

            play sound s_orgasm

            girl.char "AAAAAH!!! You're tearing me appaaaaahhh!!!"

            "Mercilessly, you start pumping your fist back and forth inside her, making her climax once again as she screams at the top of her lungs."

            with flash

            girl.char "AAAAAAAAAAAH! AHAAAA!!!"

            "Her [type] is completely dilated now, and her belly is grotesquely deformed by your hand inside her. You decide to go even deeper."

            girl.char "No! That's impossible... You're going to put your whole forearm in!!!"

            with flash

            play sound s_screams

            girl.char "RHAAAAAAAA!!! I'M CUMMIIIIIIIIING!!!"

            "She howls like a wild animal as you shove your arm very deep inside her [type], bumping into her inner regions. The customers are amazed by how far you were able to push her."

            "As you slowly take out your arm, [girl.name] falls on the floor in a pool of her love juices, looking completely spent and nearly passed out. She lies there for a long time, drooling, while the customers move on to the next attraction."

            $ changed_stats = [("fetish", dice(3)), (stat, dice(3)), ("constitution", 2+dice(3))]
            $ girl.change_love(2)
            $ girl.change_fear(-3)

        elif attitude > 50:

            play sound s_ahaa

            girl.char "Ahaa..."

            "You know her weaknesses, and before long, you can feel her getting wet. Using her love juice, you start playing with her [type], sliding one finger first, then two."

            "She struggles to keep singing, but her voice shakes as you play with her inner regions."

            play sound s_aaah

            girl.char "Aaaah..."

            you "It's time, now, [girl.name]..."

            "As she gets to the chorus of the song, the cry of the howling banshee, you slide even more fingers inside her [type], until you have four of them well in."

            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with dissolve
            play sound s_scream

            girl.char "Aaaah!!!"

            "It's time to make her howl. Adding your thumb to the mix, you struggle to fit your hand inside [girl.name]. She screams in pain and struggles hard to accommodate your whole hand inside her [type]."

            play sound s_screams

            girl.char "AAAAH, AAAAAAAH, AAAAAAH..."

            "Even though she is in pain, you can tell she is also aroused by the situation, as her love juices keep flowing out. Feeling the gaze of strangers all around her, she blushes with shame as she endures your hand."

            play sound s_scream

            girl.char "Ooooh... You're ripping my [type] apart..."

            "You wriggle your hand around a bit to impress the customers. Nevertheless, you worry going too far might end up hurting her. Reluctanly, you slide your hand out of her, as she screams one last time like a howling banshee."

            play sound s_scream_loud

            $ changed_stats = [("fetish", dice(3)), (stat, dice(3)), ("constitution", dice(3))]
            $ girl.change_fear(-1)

        else:
            play sound s_surprise

            girl.char "I... Aaah... am... Aaaah... a most fierce spirit... Aaaah!!!"

            play sound s_scream

            "She can't concentrate as you play with her pussy in front of the guests. Trying to move on with the program, you decide to slide a couple of fingers inside her."

            play sound s_scream_loud

            girl.char "Nooo! It hurts!!!"

            you "Come on, don't be a wimp... If this is too much for you, how will you react when I slide my whole fist inside you?"

            play sound s_scream

            girl.char "When you WHAT??? No!!!"

            "Fed up with her whining, you clench your hand into a fist, trying to shove it inside her. Her pussy is completely dry and tight, and it goes nowhere fast."

            play sound s_screams

            girl.char "AAAAAH! Stop! Get off me!!!"

            play sound s_crowd_boos

            "The customers are bored watching you struggle, and start booing. Some of them even start asking for their money back."

            you "Please, stay! There are other shows... Please, come back..."

            $ changed_stats = [("fetish", -dice(3)), (stat, -dice(3)), ("constitution", -dice(3))]
            $ girl.change_love(-3)
            $ girl.change_fear(3)

    elif fix == "lactation":
        $ attitude = girl.get_sex_attitude(selected_act, fix)
        $ rep_impact = True

        "Ignoring her pleading, you inject the strange liquid into [girl.name]'s nipple. Almost instantly, her face becomes flushed and her tits get swollen."

        $ pic = girl.get_pic("lactation", and_tags=["geisha"], not_tags=["group", "bisexual"], soft=True)
        if pic:
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with dissolve

        play sound s_surprise

        girl.char "My breasts! They're... growing..."

        "As the eager public watches on, [girl.name]'s boobs seem to visibly grow, until they are almost double her natural size."

        girl.char "Aaaah... I feel weird..."

        "Smiling mischievously, you take out a cowbell from your toolbag, and tie it around [girl.name]'s neck. She is too disoriented to refuse."

        you "Ladies and Gentlemen of the City, many of you have forgotten the simple pleasures of the farmer, living off the land and tending to his animals..."

        you "Let me tell you the story of a nice, healthy cow, a girl called Molly, and her deep and sweet relationship with her owner..."

        "Putting [girl.name] on a leash, you tell her to get on all fours, and you parade her around the okiya with her swollen breasts dangling out."

        you "Molly lived a simple life, living in harmony with nature and following her daily routine..."

        "You make [girl.name] do various tricks, such as mooing and letting the customers pat her head."

        you "Molly's favorite part of the day, however, was milking time."

        "Taking out an empty milk keg from your bag, you show it to Molly... Er, I mean, [girl.name]."

        if attitude > 100:

            play sound s_mmmh
            girl.char "Mmmh..."

            "[girl.name] looks expectantly at you and the milk keg. Completely in character now, she moos with excitement."

            play sound s_moo

            you "Come here girl... It's time for your milking..."

            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["geisha"], not_tags=["group", "bisexual", "profile"])
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with dissolve

            "Getting behind [girl.name], you grab both of her tits. As soon as you touch them, [girl.name] cries out with pleasure, and a splash of milk comes out of her breasts."

            with flash


            play sound s_orgasm_fast

            girl.char "Aaaah! Aaaaahaaa!!!"

            with doubleflash

            you "Wow... Molly loves milking so much, she came even before I started... Ain't that right, girl?"

            "[girl.name] blushes bright red."

            girl.char "Oooh..."

            "Pointing her leaking tits at the milk keg, you squeeze them one at a time, twisting her nipples with your fingers. A big shot of milk splashes out everytime, rocking [girl.name]'s body with more orgasms."

            with flash
            play sound s_aaah

            girl.char "AAAAH!!!"

            with doubleflash
            play sound s_orgasm

            girl.char "Again... I'm cumming! Agaiiiiin..."

            "After a few minutes, you have completely filled the keg with [girl.name]'s sweet milk. The customers take cups, and line up to have a taste."

            $ changed_stats = [("fetish", 2+dice(3)), ("obedience", dice(3))]
            $ girl.change_love(2)


            if dice(6) >= 5:

                "Customer" "Sorry, Master [MC.name], but I believe you left out a part of the story."

                you "Really? Did I, now? And what was that?"

                "Customer" "As she ventured into the moutain, still dazed from a particularly intense milking session, she ran into a big, bad wolf..."

                "The customer places himself right behind [girl.name], taking out his dick."

                "Customer" "The horny wolf got the jump on her, and was intent on raping her."

                menu:
                    "What do you do?"

                    "Let the customer fuck [girl.name]":

                        you "Surprising [girl.name] as she was frolicking in the tall grass, the wolf leapt on her back, and shoved his hard cock right inside her moist pussy."

                        play sound s_surprise

                        $ pic = girl.get_pic("sex", and_tags=["lactation"]+and_tag)
                        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                        with dissolve

                        "The customer starts fucking [girl.name] from behind while the others keep squeezing her massive tits for more milk. She cums over and over, her mind completely blanking out from the drugs."

                        $ changed_stats.append(("sex", dice(3)))

                    "Tell the customer to fuck [girl.name]'s ass":

                        you "As the wolf leapt right onto Molly's back, his large, knotted cock came bumping right onto her tight asshole..."

                        "You instruct the customer to use [girl.name]'s ass, and he's only too happy to comply."

                        $ pic = girl.get_pic("anal", and_tags=["lactation"]+and_tag)
                        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                        with dissolve

                        play sound s_moans

                        girl.char "Aaaah! Mister! You're fucking Molly's ass... Aaaah!!!"

                        with flash

                        "The customer shoots a bucket load of cum inside [girl.name]'s asshole while squeezing her swollen tits hard, spraying warm milk all over the ground."

                        $ changed_stats.append(("anal", dice(3)))

                    "Stop the customer":

                        you "However, Molly wasn't born yesterday. Kicking the wolf in the balls, she quickly ran back to her rightful owner."

                        you "(Sorry Sir. If you want a whore, you'll have to head to one of the bedrooms.)"

                        "Customer" "Aw... *sigh*"

            else:
                you "Come on, don't be shy... You can even drink directly from the tap!"

                "Following your advice, some customers start sucking on [girl.name]'s nipples, driving her crazy with renewed orgasms."

            "At the end of the session, she is left completely spent for the night, passed out and making weak mooing sounds in a pool of her fluids. The customers are ecstatic about the show."

            $ girl.interactions = 0

        elif attitude > 0:
            play sound s_surprise

            girl.char "Master... Wait... You can't... Aaaah!"

            $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["geisha"], not_tags=["group", "bisexual", "profile"])
            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with dissolve

            "Squeezing her swollen tits from behind, you start kneading them like dough. Soon, droplets of milk start leaking from her breasts."

            play sound s_ahaa

            girl.char "I feel so strange... Aaaah..."

            "After playing with her tits for a while, a stream of milk starts flowing out. Pointing her nipples at the milk keg, your squeeze them in turn, splashing milk inside."

            play sound s_aaah

            girl.char "Aw... I'm like a real cow now... Aaaah..."

            "You keep milking [girl.name] for a while, eventually filling up almost half of the keg. The customers are happy about the show."

            $ changed_stats = [("fetish", dice(3)), ("obedience", dice(3))]
            $ girl.change_love(1)
            $ girl.change_fear(1)

        else:
            play sound s_surprise

            girl.char "No! Get away from me!"

            "[girl.name] stands right up, covering her breasts. You step forward menacingly."

            you "Come on... Don't make a scene... It's just a little play for the benefit of the customers..."

            play sound s_scream

            girl.char "No! Don't... Aaaah!"

            "Stepping behind her, you grab her breasts, squeezing them hard. She cries in pain as a single bead of milk comes out of her nipples."

            play sound s_screams

            girl.char "Nooo! It hurts! Stop!!!"

            "[girl.name] wriggles out of your arms, and runs out of the okiya. The customers sigh and get up to leave, disappointed."

            you "Wait! She'll come around... Please, wait! Damn..."

            $ changed_stats = [("fetish", -dice(3)), ("obedience", -dice(3))]
            $ girl.change_love(-1)
            $ girl.change_fear(2)


    elif fix == "enemas":
        $ attitude = girl.get_sex_attitude(selected_act, fix)
        $ rep_impact = True

        "You place the large syringe at the entrance of her anus, pushing the tip inside."

        play sound s_surprise

        girl.char "Aaah! It's cold!"

        "Slowly, you start pushing on the piston, filling [girl.name]'s belly with the strange liquid."

        $ pic = girl.get_fix_pic(selected_act, selected_fix, and_tags=["geisha"], not_tags=["group", "bisexual"])
        show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        with dissolve

        if attitude > 125:

            play sound s_aah

            girl.char "Aaaah! Something... is filling up my ass!"

            "Little by little, the fluid enters [girl.name]'s tight asshole, filling her insides with yellow liquid."

            "As you pour more and more of the liquid inside, her belly starts inflating, until she looks like she is pregnant."

            play sound s_ahaa

            girl.char "I feel so strange... My body... Aaaah..."

            "[girl.name] looks more curious and aroused than panicked by the changes happening to her body. Soon, she is full to the brim, her belly looking like she is about to give birth to twins."

            girl.char "Aaah! I can't hold it... inside... Aaaah!"

            you "You must hold. Everyone is watching."

            play sound s_sigh

            girl.char "Nooo... I... Aaaah..."

            "You take out the enema, and [girl.name] tries to resist as best she can, contracting her anus hard, fighting to keep the liquid inside."

            you "Look at her! She's valiantly holding it all inside, I guess she loves it... Oh, by the way, this liquid..."

            you "It's the content of my chamberpot this morning. I'm glad you like it so much."

            play sound s_screams

            girl.char "Aaaah!!!"

            play sound s_pee

            "Stunned by your words, [girl.name] loosens her muscles, and suddenly the liquid starts splashing out of her anus in a steady stream."

            with flash
            play sound s_scream_loud

            girl.char "AAAAAH!!!"

            play sound s_orgasm
            $ pic = girl.get_pic("enema", and_tags=["orgasm"], not_tags=["group", "bisexual"])
            if pic:
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


            with doubleflash

            "The feeling is too intense, and [girl.name] starts cumming hard, squirting as she is rocked by multiple orgasms while the liquid continues to pour out of her."

            you "Gee, that was just a joke... Look at how hard you came... You've made such a mess!"

            $ changed_stats = [("fetish", dice(3)), ("constitution", 2+dice(3))]
            $ girl.change_love(1)
            $ girl.change_fear(-2)

        elif attitude > 25:

            play sound s_surprise

            girl.char "What's this? Aaah..."

            "[girl.name]'s belly fills up, and soon a bump starts to appear as her inner parts expand to accommodate the liquid."

            play sound s_scream

            girl.char "It's too much! Aaaah!"

            you "Come on, we need to clean you up properly."

            play sound s_ahaa

            girl.char "No... I can't anymore... Nooo..."

            "After she is reasonably full, her belly now looks like she is three months pregnant. You decide it's enough for now."

            you "That should be it now... Wow!"

            with vpunch

            play sound s_pee

            "As soon as you pull the syringe out, [girl.name] is unable to control herself, and a jet of yellow liquid starts shooting out of her, nearly hitting you."

            play sound s_scream_loud

            girl.char "AAHAAAA!!!"

            you "Hey! Watch it!"

            $ changed_stats = [("fetish", dice(3)), ("constitution", dice(3))]
            $ girl.change_fear(-1)

        else:
            play sound s_scream

            girl.char "Oh, it burns! Aaah!"

            "Startled by the unwelcome feeling, [girl.name] moves forward on all fours to escape from you."

            you "Hey!"

            "The syringe pops out, and you end up spraying the strange liquid on her buttcheeks."

            play sound s_scream_loud

            girl.char "EEEEK!!!"

            "[girl.name] keeps running away from you, and you run behind her, trying and failing to slip the enema back inside her ass."

            you "Damn you! Come back here!"

            play sound s_crowd_laugh

            "The crowd laughs at your ridiculous attempts, and soon tire of it. They thought it was a lame show."

            $ changed_stats = [("fetish", -dice(3)), ("constitution", -dice(3))]
            $ girl.change_love(-2)
            $ girl.change_fear(1)

        if attitude > 25 and dice(6) >= 5:
            "When all the liquid has finally come out of [girl.name]'s asshole, one of the customers steps forward."

            "Customer" "May I?"

            menu:
                extend ""

                "Sure":
                    you "Why, sure, she's all clean now."

                    "Looking happy, the customer lowers his pants, placing his erect cock at the entrance of [girl.name]'s twitching asshole."

                    play sound s_surprise
                    girl.char "Ahaaaa!"

                    $ pic = girl.get_pic("anal", and_tags=and_tag, not_tags=["group", "bisexual"])
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                    with dissolve

                    "[girl.name]'s butt is nicely lubricated by the enema liquid, and the customer has no problem slipping his cock inside her loose asshole."

                    play sound s_moans

                    girl.char "Aaah!!! My ass! AAAAH!!!"

                    with flash

                    "Soon, the customer discharges in [girl.name]'s asshole, filling her up with warm cum."

                    with doubleflash
                    play sound s_orgasm_fast

                    you "Oh, look, a cum enema! She seems to like it even more..."

                    girl.char "Arrrh..."

                    "The customer looks happy as he slips his cock out of [girl.name]'s ass, leaving her on the ground in a pool of dank fluids. The customers thought it was a great show."

                    $ changed_stats.append(("anal", dice(3)))

                "Nope":
                    you "Sorry pal, if you want a whore, you'll have to wait in line just like the others."

                    "Customer" "Aw! You're a cruel man... *sniff*"

        elif attitude > 125:
            "The crowd thought the show was great fun."
        elif attitude > 25:
            "The crowd thought the show was okay."

    return

## END OF BK DAY EVENTS FILE ##
