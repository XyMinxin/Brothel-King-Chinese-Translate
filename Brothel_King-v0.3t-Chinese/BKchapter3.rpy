#### CHAPTER 3 EVENTS ####

## Suzume events & NPC hints ##

label c3_suzume_hint(): # Happens after all three kunoichi hunts have been locked, or after the first summon of Homura

    scene black with fade
    show expression bg_bro at top with dissolve
    show suzume with dissolve

    if story_flags["homura summoned"]:
        suzume bend "Sooo... Did you learn anything interesting from your posh little girlfriend?"

        you "Do you mean... Homura? Are you stalking me, or something?"

        suzume doubt "Stalking? No way! I just watch you have sex from time to time, is all."

        you "Watch me have... THIS IS WORSE THAN STALKING!" with vpunch

        suzume "Hey, what can I say... It turns me on."

        you "Why you... Grrr..."

        you "Hang on, I just thought of something. Can you bend forward?"

        show suzume bend with dissolve

        suzume bend "Bend forward? Like this?"

        you "Ah, yes... Just what I thought."

        you "I'm horny. Come here."

    else:
        suzume doubt "Well... We seem to be well and truly stuck."

        you "What do you mean?"

        suzume "We have hunted all three kunoichi across the city... But now they are all beyond our reach."

        you "Their ninja powers are messing with us. There has to be a way to circumvent them."

        suzume normal "We should ask around for hints. You've made a few contacts through the city, haven't you? Why not ask them for clues?"

        you "I don't know. Most of them are freaks and dullards. Some are hot girls, though."

        suzume bend "What about this noble little lady you've been dating? Perhaps she knows something we don't?"

        you "Hey! We're not da-"
        
        you "Why am I justifying myself to you?" with vpunch

        suzume "Fufufu, don't get the wrong idea. I'm not the jealous type..."

        suzume "But just so you know, I could use a little boning. I am getting rusty, you know!"

        you "It's only been-"

        you "Wait. Actually, it's been a while. Come here."

    scene black with fade

    play sound s_moans_short

    "A while later..."

    play sound s_orgasm_fast
    show bg suzume_piledriver at top with flash

    suzume naked2 "AAAAAAAH!!!"

    with doubleflash

    suzume "Oh my... Look at the mess you've made..."

    "She looks at you straight in the eye in an obscene pose as your cum drips down her holes and belly."

    suzume "You didn't even spare my ass this time! Looks like we've found a new way to have fun..."

    play sound s_mmh
    $ MC.change_prestige(3)

    scene black with fade
    show expression bg_bro at top with dissolve
    show suzume naked with dissolve

    suzume "Aaah... That's better! [emo_heart]"

    you "Yes. But this doesn't bring us any closer to catching those pesky ninjas."

    suzume "Well, like I said, you can investigate with your contacts in the city. Or you can hit your noble girlfriend."

    you "For lack of better ideas... Okay."

    "You can now {b}visit your contacts{/b} by talking to suzume on the {b}city{/b} screen."

    if story_flags["homura summoned"]:
        "You could also ask Homura for more hints, by summoning her from the {b}Plaza{/b}."
    else:
        "Homura also mentioned that she can help you if you tie her ribbon to a pole in the {b}Plaza{/b}, but you'll need an okiya first."

    $ story_flags["suzume hint seen"] = True
    $ suzume_hints_active = True

    return


label c3_update_hint_goals():
    python:
        for nin, channel in [(NPC_narika, "story"), (NPC_mizuki, "story2"), (NPC_haruka, "story3")]:
            # Unlocks hint recap with Suzume
            if nin.flags["hints"] >= 3:
                if nin.flags["locked"]: # First call
                    game.set_task("和云雀再聊聊关于%s的事。" % nin.name, channel, blocking=False) #! Change blocking
                nin.flags["locked"] = False

            # Init hints 
            else:
                if nin.flags["hints"] is False:
                    nin.flags["hints"] = 0
                game.set_task("收集关于" + nin.name + "的三条线索 (%s/3)。" % str(nin.flags["hints"]), channel, blocking=False) #! Change blocking

    return

label c3_interrogate_contacts():

    hide screen districts

    scene black
    show bg zan at top
    # with fastfade

    show screen overlay

    call c3_update_hint_goals() from _call_c3_update_hint_goals

    $ suzume("那么，在你在城里的熟人中，你想先找谁？", interact=False)

    $ contact_list =  [("side suzume", "云雀, 傻傻的风之忍者", NPC_suzume),
                        ("side sill", "希露，你最信任的奴隶", NPC_sill),
                        ("side papa", "弗里克老爹，那个怪老头", NPC_freak),
                        ("side jobgirl", "[jobgirl_name]，那个任务达人", NPC_jobgirl),
                        ("side kenshin", "剑心，那个女骑士团长", NPC_kenshin),
                        ("side satella", "萨特拉，黑暗女神的使徒", NPC_satella),
                        ]

    if NPC_bast.met:
        $ contact_list.append(("side bast", "Bast, the Quartermaster", NPC_bast))
    if farm.active:
        $ contact_list.append(("side gizel", "Gizel, the White Witch", NPC_gizel))
    if story_flags["met carpenter"]:
        $ contact_list.append(("side carpenter", "Iulia, the Carpenter", NPC_carpenter))
    if thieves_guild.action:
        $ contact_list.append(("side renza", "Renza, the Thief", NPC_renza))
    if watchtower.action:
        $ contact_list.append(("side sergeant", "Kashiv, the grim Guard Sergeant", NPC_sergeant))
        $ contact_list.append(("side captain", "Farah, the naughty Guard Captain", NPC_captain))
    if story_flags["c1_path"] == "neutral":
        $ contact_list.append(("side lieutenant", "Lydie, the cunning Guard Captain", NPC_lieutenant))
    if story_flags["c1_path"] == "good":
        $ contact_list.append(("side maya", "Maya, the righteous Guard Captain", NPC_maya))
        $ contact_list.append(("side roz", "Roz, the zealous Guard Lieutenant", NPC_roz))
    if harbor.action:
        $ contact_list.append(("side stella", "Stella, the Blood Isles's Slaver", NPC_stella))
    if farmland.action:
        $ contact_list.append(("side goldie", "Goldie, the Farmhand", NPC_goldie))
    if sewers.action:
        $ contact_list.append(("side willow", "Willow, the Monster Catcher", NPC_willow))
    if junkyard.action:
        $ contact_list.append(("side gina", "Gina, the Mad Scientist", NPC_gina))
    if prison.action:
        $ contact_list.append(("side gurigura", "Gurigura, the Toy Merchant", NPC_gurigura))
    if arena.action:
        $ contact_list.append(("side ramias", "Ramias, the Weapon Merchant", NPC_ramias))

    call screen suzume_hints(contact_list)
    $ npc = _return

    if not npc:
        jump districts

    if not isinstance(npc, NPC):
        jump c3_interrogate_contacts

    # General tips / unlock story (Suzume)

    if npc == NPC_suzume:

        if not (NPC_narika.flags["locked"] or NPC_narika.flags["c3 path"]) or not (NPC_mizuki.flags["locked"] or NPC_mizuki.flags["c3 path"]) or not (NPC_haruka.flags["locked"] or NPC_haruka.flags["c3 path"]):
            menu:
                "I found hints about Narika" if not (NPC_narika.flags["locked"] or NPC_narika.flags["c3 path"]):
                    hide overlay
                    scene black with fade
                    call c3_unlock_narika from _call_c3_unlock_narika
                "I found hints about Mizuki" if not (NPC_mizuki.flags["locked"] or NPC_mizuki.flags["c3 path"]):
                    "<PLACEHOLDER> Sorry, this part of the story is not ready yet. Wait for a future update..."
                "I found hints about Haruka" if not (NPC_haruka.flags["locked"] or NPC_haruka.flags["c3 path"]):
                    hide overlay
                    scene black with fade
                    call c3_unlock_haruka from _call_c3_unlock_haruka
                    
            jump districts

        suzume doubt "Well, I've told you everything I know, I think..."

        suzume normal "I don't have specific hints about individual Kunoichi, but I'm sure other people will."

        suzume "If you can collect {b}three hints{/b} about one of them, talk to me again. We should be able to devise a plan."

        "Talk to Suzume after you've gathered {b}three hints{/b} on a Kunoichi."

        jump c3_interrogate_contacts

    menu:
        "Who do you want to ask [npc.name] about?"

        "Ask about Narika, the Void Kunoichi" if NPC_narika.flags["locked"] or not MC.has_item(void_rune.name) or debug_mode:
            "You tell [npc.name] about {b}Narika{/b}, the Kunoichi you are looking for, and what she's been up to."
            $ nin = NPC_narika

        "Ask about Mizuki, the Water Kunoichi" if NPC_mizuki.flags["locked"] or not MC.has_item(water_rune.name) or debug_mode:
            "You tell [npc.name] about {b}Mizuki{/b}, the Kunoichi you are looking for, and what she's been up to."
            $ nin = NPC_mizuki

        "Ask about Haruka, the Earth Kunoichi" if NPC_haruka.flags["locked"] or not MC.has_item(earth_rune.name) or debug_mode:
            "You tell [npc.name] about {b}Haruka{/b}, the Kunoichi you are looking for, and what she's been up to."
            $ nin = NPC_haruka

        "Ask about the elemental-proof cells" if npc == NPC_freak and NPC_freak.flags["holding info"]:
            "You talk to {b}Papa Freak{/b} about the secret magic-proof cells in your building again."
            call c3_papa_cells from _call_c3_papa_cells

            jump c3_interrogate_contacts

        "Never mind":
            jump c3_interrogate_contacts

    # Individual tips

    $ MC.interactions -= 1

    $ hint_list = {
                    NPC_narika : (NPC_jobgirl, NPC_bast, NPC_gurigura, NPC_gina, NPC_roz, NPC_renza, NPC_captain),
                    NPC_mizuki : (NPC_sill, NPC_satella, NPC_freak, NPC_gizel, NPC_stella),
                    NPC_haruka : (NPC_kenshin, NPC_carpenter, NPC_ramias, NPC_goldie, NPC_maya, NPC_lieutenant, NPC_sergeant)
                }

    if npc in hint_list[nin]:
        
        call c3_hint(npc, nin) from _call_c3_hint
        scene black
        show bg zan at top
        with fastdissolve

        if _return != "cancel":
            call c3_update_hint_goals() from _call_c3_update_hint_goals_1

    else:
        python:
            no_hint = {
                    NPC_jobgirl : "Err, sorry, I don't know anything about such a person.",
                    NPC_bast : "Look, I'm busy, and this doesn't ring a bell, sorry.",
                    NPC_gurigura : "Teeheehee! I didn't understand a single thing you said, but you're funny, Mister.",
                    NPC_gina : "Sorry, but I don't know anything about such a person. Now, I have an important paper to write, so...",
                    NPC_roz : "Err, never heard about that chick, sorry.",
                    NPC_renza : "Hmm... I don't know this person. She probably operates outside of my turf.",
                    NPC_captain : "Never heard of her. Now, if you'll excuse me, I have a legal {i}and{/i} a criminal empire to run, so kindly fuck off.",
                    NPC_sill : "Oh, I'm sorry, Master... I really don't know anything about such a person.",
                    NPC_satella : "Why, it's funny you should mention it, I had a pet raccoon called just like that... But I just realized I forgot to feed it. Poor thing, it's been six months! It must be hungry.",
                    NPC_freak : "Thank you for visiting me, my boy.... But I have no idea who you're babbling on about.",
                    NPC_gizel : "Don't know, don't care. Look, human females are fun to run experiments on, but I haven't got much interest in their indiviual characteristics otherwise.",
                    NPC_stella : "Look, I don't give information for free. But I don't have any information about this person anyway.",
                    NPC_kenshin : "Is this a person of interest in your investigation? I haven't heard anything worth mentioning about such a person.",
                    NPC_carpenter : "Boss, I'm just a carpenter. I build things. This cloak and dagger stuff doesn't concern me.",
                    NPC_ramias : "I'm sorry, I'm sure it was all terribly interesting, but ever since an orc banged his mace on my helmet, I blank out sometimes. I'm afraid I can't help you.",
                    NPC_goldie : "Oh, " + MC.name + ", I would love nothing more than to help you... But I really don't know anything.",
                    NPC_maya : "Sorry, I haven't heard of such a criminal. Maybe ask Roz, he's the one who still patrols the streets. I mostly handle paperwork now... *sigh*",
                    NPC_lieutenant : "No, I must say I haven't heard of her. Maybe Renza knows, I handle the more 'official' business these days.",
                    NPC_willow : "Is she a monster? Because that's what I deal with, monsters. I give most humans a wide berth.",
                    NPC_sergeant : "I have nothing to say to you. Leave.",
                    }

        $ renpy.say(npc.char, no_hint[npc])

    if npc == NPC_willow and not story_flags["fire rune"]:
        if not NPC_willow.flags["introduce fire rune"]:
            $ NPC_willow.flags["introduce fire rune"] = True

            willow "Hey, [MC.name], wanna see something cool?"

            you "Depends. Does it involve going into the sewers again? Because I hate going down in the sewers. Washing the smell away takes days..."

            willow "Nope, it's a fire rune. You can engrave it on a weapon, and fight fire with fire. Isn't it cool?"

            you "Yeah I guess... But none of the ninjas I'm hunting for use fire."

            willow "But you could get it, you know, just in case? For 100,000 gold?"

            you "100,000 GOLD!!!" with vpunch

            willow "Alright, sheesh, don't yell... 10,000 gold then?"

            you "10,000 GOLD!!!" with vpunch

            you "..."

            you "Wait. Did you just give me a 90 per cent rebate right off the bat? Why?"

            willow "Gee, you're impossible!"
            
            willow "Fine, Mister Negotiator, you can have it for 1,000 gold! But that's final!"

            you "You just went down from 100,000 gold to 1,000 gold in the blink of an eye."

            willow "Yes. I'm great at bargaining, don't you think? Because I think I rock!"

            you "Well, it's, err, important that you believe in yourself... If no one else will?"

            you "So can I have it for 1,000 gold?"

            willow "Yes, that's my final price. Because if you lower the price more than twice, it brings bad luck and your fluffy ears fall off. Everybody knows that."

            you "I don't think that {i}anybody{/i} actually knows that..."

            willow "Anyway, you want it, or what?"

        else:
            willow "Say, you wouldn't be interested in that piping hot fire rune, would you? 1,000 gold, as we negotiated last time?"

        if MC.gold >= 1000:
            menu:
                "Sure (pay 1,000 gold)":
                    you "Sure okay, give it to me."

                    play sound s_gold
                    $ MC.gold -= 1000
                    $ story_flags["fire rune"] = True

                    call receive_item(fire_rune) from _call_receive_item_19

                "No":
                    you "1,000 gold for a trinket I'll never use? No thanks."

        else:
            you "I don't have that kind of money right now."

            willow "Fine, I'll hang on to this a little longer. Let me know if you want it."

    elif npc == NPC_freak and not NPC_freak.flags["holding info"]:

        $ NPC_freak.flags["holding info"] = True

        papa_apprentice "Hey, Papa, aren't you forgetting something? You said you'd tell him?"

        papa "Uh? Oh, that's right..."

        papa "Sorry, young man, I wanted to tell you about that house you just got off my hands."

        you "I knew it!!! It was all a scam, isn't it? It's going to crumble within a week? It's built on an ancient graveyard? It's haunted by malevolent vampire rabbits?"

        papa "No..."

        you "So it's even worse, then! Cockroaches?!?" with vpunch

        papa "No, no, let me speak..."

        papa "You remember, I told you the building has elemental resonance?"

        you "Yes..."

        papa "It's especially strong in the foundations, where the holding cells used to be."

        you "Holding cells? First time I'm hearing about this."

        papa "Yes, they're condemned."

        you "Why talk about it now, then?"

        papa "Well, you told us you're hunting for ninjas with elemental powers, correct?"

        you "Yes..."

        papa_apprentice "Then holding cells that cancel elemental magic could be very useful to you!"

        you "Indeed... If I could get those Kunoichi captured in the first place."

        papa "I'll leave that bit to you. But my apprentice and I, we could rebuild the holding cells... For a price."

        you "How much?"

        papa "You know we don't need money, right?"

        you "So... What is it you want?"

        papa_apprentice "Oh, I think you know... *grin*"

        papa "Girls, of course!"

        you "Can you be more specific?"

        papa "All right..."

        $ NPC_freak.flags["cells built"] = 0

        call c3_papa_cells() from _call_c3_papa_cells_1
        show screen overlay

        if not NPC_freak.location:
            $ NPC_freak.location = location_dict[papa_location[district.name]]
        $ NPC_freak.location.action = True

    if MC.interactions:
        jump c3_interrogate_contacts
    else:
        jump districts

label c3_hint(npc, ninja):

    scene black
    show expression npc.get_bg() at top
    if npc != NPC_stella:
        show expression npc.char.image_tag
    else:
        show stella at center:
            yoffset yres(350)

    with fade

    ## Narika tips

    if ninja == NPC_narika:
        if npc == NPC_jobgirl: # disguise, upper city
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True
            if event_dict["c2_narika_H1"].happened:
                $ ninja.flags["school hint"] = True
                $ ninja.flags["upper city hint"] = True
                jobgirl "A student in uniform, you say?"

                jobgirl "Well, none of the classes that I know of require uniforms. Must be something from the upper city."

                jobgirl "Must be a fancy school for sure... Reserved for blue bloods, no doubt."

            else:
                $ ninja.flags["school hint"] = True
                jobgirl "Wait a minute, this does ring a bell..."

                jobgirl "Sometimes ago, I was taking an adventuring class and someone asked me if I heard about an ambitious heist being organized in the city."

                jobgirl "They asked me if I was worried about our safety. I was confused, until they said the target was going to be a school."

                jobgirl "Hahaha, can you imagine that? A bank or a guild, maybe, but a school? Who in Xeros thinks robbing a school is a good idea?"

                # jobgirl "I've heard of an ambitious heist being planned in the upper city. Something about a locked-down place, with tight security and all... A bank maybe?"
                #
                # jobgirl "I'll tell you what, no one can take over such targets by storm, they're too well-defended... If it was me, I'd go with infiltration. Get them from within."

            suzume "Hmm, that's a hint we could use... It narrows down our target, I guess."

            play sound s_spell

        elif npc == NPC_bast: # magical item
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True
                $ ninja.flags["magic hint"] = True
            bast "Stolen goods? You're asking me, the offical market quartermaster, if I know who is moving stolen goods?"

            you "Well..."

            bast "Of course I do!" with vpunch

            bast "I wouldn't be a very good trader if I didn't know about the black market, now, would I?"

            bast "Turns out, I've heard something recently. Someone inquiring in advance about how to sell a single item of high value."

            bast "The interesting thing, though? It's supposed to be a magical item. Not easy to find a taker for these, but they fetch sky-high prices if you do."

            bast "Can't say if it's related to your girl, but worth checking out, wouldn't you say?"

            play sound s_spell

        elif npc == NPC_gurigura: # disguise
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True
            if event_dict["c2_narika_H1"].happened:

                show expression npc.char.image_tag at left with move
                show katryn at right with dissolve

                gurigura "A student in uniform? And you're asking me... Because I look young?"

                you "Well..."

                gurigura "I {i}am{/i} young, but I never went to no school, teeheehee..."

                katryn "Why, obviously. You might as well ask a kitty about theoretical physics."

                gurigura "Theophysical ethics, what's that? And what's a kitty?"

                katryn "My point."

                you "This is all a big waste of time..."

                katryn "Wait. All of this goes way over poor Gurigura's head, obviously, but {i}I{/i} can help."

                you "Really?"

                katryn "Of course. There's one place where girls wear the exact kind of uniforms you described. The Magic University."

                suzume "The Magic University! That's an important clue, [MC.name]!"

                play sound s_spell
                $ ninja.flags["school hint"] = True
                $ ninja.flags["magic hint"] = True

            else:
                gurigura "You know the funny thing, I met a young girl like that the other day, same clothing and all."

                gurigura "She looked about my age, and she smelled funny, so I followed her around. The smell of fluffy trees."

                you "Fluffy trees? Like Sakura?"

                gurigura "Sakura? Isn't that a stripper's name?"

                you "*sigh*"

                gurigura "So I followed her. I figured we could be playmates, you know?"

                you "Hmm... Do you always stalk random people like that?"

                gurigura "Of course not! Only when they smell funny."

                you "I... Don't even wanna know. Go on."

                gurigura "I followed her as she entered a big building through a back door."

                gurigura "I peeked through the keyhole, and she was in her undies!"

                you "Uh?"

                gurigura "She quickly stashed her fighting clothes behind a loose stone, and put on some kind of uniform."

                you "A uniform?!?"

                suzume "Whatever she is doing, she must be in a place where uniforms are worn. This is an important clue!"

                play sound s_spell
                $ ninja.flags["uniform hint"] = True

        elif npc == NPC_roz: # upper city, lined-up buyer / Good c1 ending
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True
                $ ninja.flags["upper city hint"] = True
            $ wrong_name = ''.join(random.sample(MC.name,len(MC.name))).capitalize()

            roz "Oy! [wrong_name], long time no see."

            you "Actually, it's [MC.name]."

            roz "Yes! [wrong_name], that's what I just said."

            you "*long explanation*"

            you "Anyway... Can you help me?"

            roz "You know, I've heard something. Sometimes when I beat up a petty thief, they start spilling out some interesting information."

            you "I see, sometimes you have to beat them up when they resist arrest."

            roz "When they resist arrest? Oh, yeah... That too."

            roz "Anyway, word on the street is that a heist is being prepared, but this is nowhere in the league of the common riff-raff I deal with in the Slums."

            roz "They're aiming for a top-tier target, and sparing no resources to prepare for it. That's the only way they could afford hiring professionals like your ninja babe."

            roz "We're talking about the upper city, of course. Top security, difficult infiltration and escape, buyer lined-up for the goods. This kind of things."

            you "You know, that's actually helpful information. Color me impressed."

            roz "Uh? Impressed? Sorry pal, I don't have a pencil of that color."

            you "I take that back. *cringe*"

            play sound s_spell

        elif npc == NPC_renza: # Magical item, lined-up buyer / Neutral c1 ending

            renza "Interesting... If anyone else told me such a story, I wouldn't believe a word of it. But you and I have a history."

            you "So... Can you help me?"

            if npc.flags["seen ninja hint"]:
                renza "I already agreed to help you, didn't I?"

            elif NPC_renza.flags["story4"]:
                renza "Of course I can. Anything for you, sweetheart."

            else:
                renza "Well, information has a price. Perhaps you could donate some of your resources to the guild, hmm?"

                if not (MC.has_resource("wood", 10) or MC.has_resource("leather", 10) or MC.has_resource("dye", 10)):
                    renza "Bring me at least ten resources such as {b}wood, leather or dye{/b}. Then we'll talk."
                    return

                menu:
                    extend ""
                    "Give her 10 {image=tb wood}" if MC.has_resource("wood", 10):
                        $ MC.spend_resource("wood", 10)

                    "Give her 10 {image=tb leather}" if MC.has_resource("leather", 10):
                        $ MC.spend_resource("leather", 10)

                    "Give her 10 {image=tb dye}" if MC.has_resource("dye", 10):
                        $ MC.spend_resource("dye", 10)

                    "Don't give her":
                        you "Sorry, maybe next time."
                        return

                renza "Thanks! That will do."

            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True
                $ ninja.flags["magic hint"] = True
                $ ninja.flags["upper city hint"] = True

            renza "I've been approached by someone, maybe 3 or 4 months ago. They wanted help to steal a certain item from the upper city."

            you "Nothing unusual in your line of work..."

            renza "Except I had to turn them down. This was out of reach, even for me."

            you "What do you mean?"

            renza "They wanted to lay their hands on a unique magic item, with top-notch protection spells. I'm not sure where it was being held, they wouldn't tell me until I accepted the job."

            you "You turned it down?"

            renza "There's one thing about me: I'd rather be alive and poor than rich but burnt to a crisp by a magic ward."

            renza "A Kunoichi, though... They just might pull it off."

            you "And who was it that approached you?"

            renza "I have no idea. It was a woman, for sure, but her disguise was nearly perfect. I understood she had high-level backers."

            renza "We chatted for a while about how to overcome some of the more mundane defenses. Her questions were quite good and to-the-point, I have to say. A true professional."

            you "What happened after that?"

            renza "Nothing. Once she figured I wouldn't take the job, she thanked me and I never heard from her again."

            renza "But I'm willing to bet she's the one who's bankrolling your mysterious Kunoichi."

            you "Well, that's certainly something..."

            play sound s_spell

        elif npc == NPC_captain: # Upper city, uniforms / evil c1 ending
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True
                $ ninja.flags["upper city hint"] = True
            captain "A thief? In my city? Haha! Now that'd be a first..."

            you "Don't jest. She's not just any thief, she's a well-trained ninja."

            captain "Look, [MC.name], your naivety is part of your charm, but you could do with using your brain a little more. Do you think someone would hire a very expensive ninja to steal something in the Slums?"

            you "I guess not..."

            captain "Obviously if it was happening on my turf, I'd know about it. And I'd get my cut. The target must be in the upper city, where it's none of my concern."

            you "Makes sense."

            captain "In fact, I've heard they've really buffed security in some of the iconic landmarks... The Royal Palace, the Cathedra, the Magic University..."

            captain "It could be related to the murders, but it could also be linked to this alleged heist?"

            suzume doubt "She could be right... The little brat must be targeting one of those places."

            play sound s_spell

        elif npc == NPC_gina: # Void rune
            if not NPC_gina.flags["introduce void rune"]:
                $ NPC_gina.flags["introduce void rune"] = True

                gina "What on earth are you babbling on about? Murders? Ninjas? Toy hammers?"

                gina "I don't have time for this! I'm on the brink of a major discovery!"

                you "If you say so..."

                gina "Why, you don't believe me? Let me walk you through a few differential equations..."

                you "No no, it's fine, I believe you!"

                gina "You see, the Cimerians were so advanced that they had ways to manipulate the spacetime fabric itself."

                you "The spacetime fabric? You mean like... Cloth?"

                gina "Exactly. Every scientist knows that space and time are made of black thread, which is woven together by Chaos Fairies."

                gina "Do you never wonder why the skies looks black at night?"

                you "Because... They're made of the black thread space and time thingy?"

                gina "Precisely! A fellow scholar, I see. We call them the Woven Threads of Fate."

                gina "As you must know, science has shown that time is composed of smaller elemental particles, called timicrons. A moment, for instance, can hold as many as 1,532,875 timicrons. While an instant is more like 75,584 timicrons.  But feel free to check my maths."

                you "No thanks."

                gina "Now, timicrons can be charged positively, of course, so that they go faster, or negatively, so that they go slower."

                gina "It has been proven that some activities, such as having fun, charge timicrons positively, while other activities charge timicrons negatively. This is how science explains that an hour at the dentist always seems to drag on much longer than an hour at the brothel."

                gina "Now, look at this Cimerian runic stone: by generating a field with the Woven Threads of Fate, the Old Ones were able to charge it negatively and alter time in various ways."

                gina "This WTF field could then be deployed with the press of a rune, slowing down all of the timicrons within a reasonably large area, such as a ballroom."

                you "Wait a minute, let's see if I can make sense of your mumbo-jumbo... Are you saying this stone can slow down time?"

                gina "Not at all, silly... It just slows down timicrons so that time {i}seems{/i} to flow slower in a given referential."

                you "What if I put a super fast ninja in this referential-thingy? Could this stone hold her in place?"

                gina "Well... Technically speaking... Yes? Maybe. I don't know. Maybe not."

                you "Thank you for giving me an actionable and informed scientific opinion."

                you "Anyway, I may actually need something like this."

                gina "Really? I could sell it to you. It's true that I'm always in need of additional funds for my research..."

                gina "I guess I could part with it for 1,000 denars."

                you "1,000 denars? That's a lot for a small rock..."

                gina "Well, I suppose if you have a couple of pieces of Cimerian scrap, that would do too."

            else:
                gina "Want the time-warping runic stone? The price is still 1,000 gold, or two Cimerian scraps."

            if MC.gold >= 1000 or len(MC.get_items(name="Cimerian scrap")) >= 2 or MC.get_items(name="Cimerian artefact"):
                menu:
                    "Okay (pay 1,000 gold)":
                        $ NPC_gina.flags["research"] += 2
                        you "Fine, I'll take it."

                        play sound s_gold
                        $ MC.change_gold(-1000)
                        gina "Thanks! This will help with my research."

                        $ story_flags["void rune"] = True
                        call receive_item(void_rune) from _call_receive_item_20

                    "Okay (give 2 Cimerian scrap)" if len(MC.get_items(name="Cimerian scrap")) >= 2:
                        $ NPC_gina.flags["research"] += 2
                        call remove_item(MC.get_items(name="Cimerian scrap")[0]) from _call_remove_item_2
                        call remove_item(MC.get_items(name="Cimerian scrap")[0]) from _call_remove_item_3
                        gina "Thanks! This will help with my research."
                        $ story_flags["void rune"] = True
                        call receive_item(void_rune)

                    "What about this? (give Cimerian artefact)" if MC.get_items(name="Cimerian artefact"):
                        $ NPC_gina.flags["research"] += 5
                        $ MC.remove_item(MC.get_items(name="Cimerian artefact")[0])
                        gina "Whoah, amazing find!!! This will help a lot with my research, thank you. Here, take this."
                        $ MC.change_gold(500)
                        $ story_flags["void rune"] = True
                        call receive_item(void_rune)

                    "Maybe later":
                        you "1,000 gold for a piece of rubble? I'll pass."

                        gina "Suit yourself. Come back if you change your mind."

            else:
                you "I don't have the money."

                gina "How disappointing. Come back if you change your mind."

    elif ninja == NPC_mizuki:
        if npc == NPC_sill: # Various types of magic, ghost
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            sill sad "R-Really, Master? You want my opinion?"

            sill "(What should I do, what should I do... This never happens...)"

            you "Yes. If I remember right, you were trained in magic as a child before your family fell out of grace, correct?"

            sill happy "Well, it's true! My teachers said I had great potential."

            sill sad "And now, look at me, doing laundry... *sniff*"

            you "I know, right! What a waste of your natural talent for housekeeping it would have been."

            sill "Aw..."

            you "Anyway, is there anything you can tell me about the water Kunoichi?"

            sill happy "Ahem, let's see. So you say this woman can appear and disappear at will?"

            you "Yes, and yet it doesn't seem to be regular magic... She just vanishes into thin air, like a ghost. I'm sure her mana was depleted."

            sill "Hmm... Like a ghost, you said?"

            you "Yeah."

            sill "One thing I learnt is that speaking broadly, there are two kinds of magic. The one we use is called academic magic, which is centered around formulas, scepters, runes or other conduits that we have to learn and master in order to cast spells."

            you "Okay..."

            sill "But there is another form of magic, called 'innate magic'. It's the kind used by dragons, the fairy people, demons..."

            you "Hmm... Even though she's a she-devil, I don't think she's a demon. Or a dragon, or an elf, for that matter."

            sill "... and the undead."

            you "What?"

            sill "Ghosts. The undead. They can use innate magic. Even without any external conduits, or mana. Their immortal soul is the conduit."

            you "Wait a minute. You're not seriously suggesting she's a ghost?"

            if NPC_mizuki.flags["onsen"]:
                you "I've seen her from up close and... She is very much alive! *blush*"

            sill "Well, if she in't a ghost, maybe she found a way to harvest the afterlife's energy, then."

            you "As far-fetched as this sounds... This could be a lead. Let's see where it takes us."

            play sound s_spell

        elif npc == NPC_satella: # Various types of magic, link to Shalia, Karkyr story
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            play music m_satella fadein 3.0

            satella happy "Teehee, look what the raccoon dragged in! So... You didn't come here to play a game?"

            you "N-No, not this time..."

            satella angry "Well, you're damn right you didn't, because I didn't send you a bloody invitation, did I!" with vpunch

            you "N-No!!! I'm sorry to disturb you.... Maybe this wasn't a good idea-"

            satella happy "I mean, it's perfectly fine for you to drop by and ask idle questions."

            you "Phew..."

            satella angry "BUT GAMES, THOUGH? GAMES ARE INVITE-ONLY! I MIGHT TURN YOU INTO A MAGGOT PILE IF YOU DARED!!!" with vpunch

            you "*gulp*"

            you "I'm definitely not here for a game... Just idle questions about ninjas you may or may not know anything about, I swear."

            satella happy "Fine, then. I'm glad to see you value my time."

            satella angry "My {i}game{/i} time." with vpunch

            you "So... Know anything about this person? Or her magic?"

            satella happy "Let me tell you something about wizards, sorcerers, mages, witches and all that ilk..."

            you "What?"

            satella "They're all a bunch of hopeless losers."

            if MC.playerclass == "Wizard":
                you "Well... Thanks."
            else:
                you "Ha! That's what I think, too."

            satella "And you know why?"

            you "I'm going to go with... No?"

            satella "Because they're nerds, that's why!" with vpunch

            you "Uh?"

            satella "All those years they spend studying, poring over dusty old books, peeking into other dimensions and begging for scraps of knowledge from bored demons..."

            play sound s_evil_laugh

            satella "Looooooo-sers!!!" with vpunch

            you "..."

            satella "You see, {i}I{/i} weave far better magic than any of these sorry dorks, and did I have to work hard to learn it?"

            satella "Not a single day in my life! You better believe it!"

            you "Oh, I believe it."

            satella "It's because I have good genes! {i}Dragon genes{/i}! It all comes naturally to me!"

            you "Well... Okay."

            satella "So here are my two denars: Your mysterious black magic woman may be a natural, like me. If so, then she doesn't need mana to cast spells, or scrolls, or materia, or whatever it is kids use these days."

            you "Really? Any spell?"

            satella "Well, spells within her area of affinity, anyway. Not gonna lie, invisibility, disappearing at will... Sounds right up Shalia's alley."

            you "So she could be a natural magic user, and a Shalia follower... Hmm."

            satella "There's a Shalia covent in Karkyr that studies unorthodox magic. Maybe they've heard of her."

            you "Is there? Karkyr, uh..."

            play sound s_spell

        elif npc == NPC_freak: # Westmarch story, ghost, Karkyr story
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            play music m_freak fadein 3.0

            papa "Hey, yo, [MC.name]! Waddup, my [MC.playerclass]?"

            you "Uh? What are you doing?"

            papa "I, err, I'm sorry, son... I was trying to sound 'cool', in the parlance of young people of our era..."

            papa "But I'm old... Hopelessly old..."

            you "Yeah, well, that's kind of the reason I'm asking you this. This lady Mizuki is supposed to be really old... Like you."

            you "(Although I must say she's in much better shape...)"

            papa "We'll see how you are when you get to 323! I'm sure your mighty dick may not be so hardy by then, heh!"

            you "Focus, Papa. Leave my dick out of this. Please."

            papa "So... This lady wears a lavish blue kimono, and she is of great beauty, would you say?"

            you "I would say..."

            papa "And does she have big puppies?"

            you "Puppies? I don't follow..."

            papa "I mean jugs? Mellons? Honkers, ta-tas, knockers, gitchi gitchi yaya dada?"

            you "I think you're laboriously trying to say... 'boobs'."

            papa "Ah, yes, boobies! That's what I'm talking about, dog!"

            you "Stop it."

            papa "Sorry..."

            you "But yeah, now that you mention it, she is remarkable in that area, too..."

            papa "Funny, it reminds me of one such person, back in Karkyr when I was still... Well."

            papa "But it can't be her. It's impossible."

            you "Why not?"

            papa "Well, that was almost 200 years ago, and..."

            you "She could be 200 for all we know. You lived to the ripe old age of 300, so why not?"

            papa "It's not that easy, and..."

            you "But she has powerful magic! Maybe she did..."

            papa "Listen to me! The lady I'm talking about. She took her own life."

            you "She... What?"

            papa "That blue kimono lady. She was a highborn princess, from one of the oldest families in Karkyr."

            papa "Everyone at the time knew her. Lovely young woman. She got married to a prince from Westmarch, her wedding was grandiose."
            
            papa "But soon after that, she took her own life."

            you "Whaaat!?!" with vpunch

            papa "It was a shock to everyone in the Four Western Kingdoms, as they were known at the time."

            papa "In fact, this sorry event started the great struggle for power that lasted 50 years and ended up with the Four Kingdoms disbanded into a hundred small Principalities."

            papa "So you see, young man, there's no chance that your woman and this big-breasted princess could be one and the same. I'm sorry I misled you."

            you "But still... This seems like too much of a coincidence?"

            play sound s_spell

        elif npc == NPC_gizel: # Westmarch story, link to Shalia
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            gizel normal "A mysterious lady who disappears into thin air? Hmm. Interesting."

            you "I thought, you know, maybe you know something, as you're immortal and stuff..."

            gizel "Well, the first thing I can tell you is pretty obvious. Smoke and mirrors, hiding, misdirection, deception..."

            gizel "This reeks of Shalia."

            you "Shalia? The Goddess of Shadows?"

            gizel "Precisely. But I realize this is not a lot to go on..."

            gizel "I have something else for you. Much... Stranger, though."

            you "What do you mean?"

            gizel "The Blue Witch of the West."

            you "I beg your pardon?"

            gizel "You remember the nickname the stupid Arios crusaders gave me? White Witch of the North?"

            you "Yeah..."

            gizel "Unimaginative as they are, when they met an all-powerful female magic user in Westmarch, can you guess what nickname they gave her?"

            you "The... The 'Blue Witch of the West'?"

            gizel "Precisely. The big, ignorant oafs."

            gizel "Turns out about 200-years ago, there was a huge war in Westmarch. Started with four kingdoms, ended with a hundred Principalities. You could say it never really ended."

            gizel "During that time, while I was monitoring various rumors as I usually do, to see if some stupid knights were on my track, I started hearing rumors about a local witch."

            gizel "A Shalia assassin, a she-devil that could use magic and appear and disappear at will, and killed her marks in a dozen spectacular ways."

            gizel "She was the bane of one of the factions in that war, although I can't remember which one."

            gizel "Her description was always the same: A stunning, ice-pale middle-age woman with raven hair, and an elaborate blue silk kimono."

            you "It definitely matches her..."

            gizel "But she left Westmarch by the end of the war, and I never heard from her again after that. By rights, she should be long-dead..."

            you "Something doesn't add up... But it's a lead."

            gizel "Okay, now scram. I have to get up early, feed the minions, milk the slaves... Working on the farm is no picnic, you know!"

            play sound s_spell

        elif npc == NPC_stella: # Water rune

            if not NPC_stella.flags["introduce water rune"]:
                $ NPC_stella.flags["introduce water rune"] = True

                stella "Female ninjas, uh? How terribly interesting. *yawn*"

                stella "In case you've missed it, I'm a very busy woman, with very little patience. I have nothing to share for free."

                you "Okay, I see. Fine, I'll just..."

                stella "I do, however, have something to sell to you."

                you "Sell?"

                "She extends her gloved hand, and shows you a tiny blue pebble."

                stella "Look at this baby. This is actually a fully operational water rune."

                you "What does it do?"

                stella "Used in the right way, it can turn water magic against its wielder. Invaluable for ship defense."

                you "Water magic? Like the one Mizuki seems to be using?"

                stella "I paid precious little attention to your tedious story, but yes, if your prey is using water magic, this rune could significantly weaken her."

                you "That seems great..."

                stella "So, 1,000 gold. No haggling."

                you "That's a bit steep."

                stella "Fine, I'll find another buyer."

                you "Wait..."

            else:
                stella "Came back for the Water stone, haven't you? I knew you would."

            if MC.gold >= 1000:
                menu:
                    "Okay (pay 1,000 gold)":
                        you "Okay, I'll take it."

                        play sound s_gold
                        $ MC.gold -= 1000
                        $ story_flags["water rune"] = True

                        call receive_item(water_rune) from _call_receive_item_21

                    "Maybe later":
                        you "1,000 gold is more than I can afford. Maybe next time."

                        stella "Out of my way, then. I've got actual paying customers to tend to."

            else:
                you "I don't have the money yet, but..."

                stella "Oh, come on. Find it."

                stella "Why don't you do right, like some other men do? Get out of here, get me some money too."

    elif ninja == NPC_haruka:
        if npc == NPC_kenshin: # High security prisoners, Demon-worship
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            play sound s_sigh

            kenshin "Still playing amateur detective, are you? *sigh*"

            kenshin "You're wasting your time. Zan's prison, Xotar, is operated by the Knights, and it has the best security conditions in Xeros."

            kenshin "No one comes in or out without my knowledge. And I've never heard this extravagant tale of a one-armed Kunoichi being taken in."

            you "Are you sure? But how can you know all of the prisoners there? It's a huge place, it surely holds over a thousand people..."

            kenshin "Hmph, don't question me! Of course I don't know the names of all the common rabble that rots in the regular prison quarters."

            kenshin "But the maximum security area of the Prison, which would be the only one suitable to hold a trained assassin? I know all of the prisoners there, I handle the paperwork myself."

            kenshin "I make a point of it. These are the most dangerous individuals in Zan."

            if story_flags["c1_path"] != "evil":
                kenshin "Or were..."

                you "What was that?"

                kenshin "Uh? Nothing. I was just thinking about the corrupt guard Captain that you helped captured."

                you "Why? What happened to her?"

                kenshin "A security breach. No need to say more."

                you "Wait. I thought you had the best security? But someone still passed through?"

                kenshin "Those stupid guards took advantage of my knights being away! It should never have happened, and..."

                kenshin "Why am I justifying myself to YOU?" with vpunch

                you "Still, as you can see, some things remain out of your control."

            else:
                you "But something may have slipped past you."

            kenshin "Nonsense! And don't even get me started on those rumors..."

            you "Rumors?"

            "She stiffens and bites her lip. You can tell she told you too much."

            kenshin "Don't..."

            you "Please, I need to know. This could be important for the inquiry. The Princess gave me a task, remember?"

            kenshin "Trust me, this is absolutely trivial. The rumors of demon-worship within the Knights' ranks are disgraceful, and I won't tolerate any of them."

            you "Demon-worship? Wait a second..."

            kenshin "I'm not going to entertain your iddle questions anymore! I have important business to attend!"

            you "But Haruka, the Kunoichi... She mentioned a cult of demon-worshippers..."

            "Kenshin gives you an ice-cold look."

            kenshin "This is just a stupid coincidence. Now, instead of insulting the good name of my knights, why don't you take a hike, before I indulge the urge to unsheath my blade?"

            you "There's no need to act like this... We could be frie..."

            kenshin "GET. OUT!!!" with vpunch

            "You retreat before her fury. Still, you learnt a good deal about the Prison."

            play sound s_spell

        elif npc == NPC_carpenter: # prison secrets, prisoner fake identity
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            carpenter "Oh, hey, Boss! Nice of you to come here and chat."

            carpenter "Not sure I know anything about that yellow-clad missus, 'm afraid."

            carpenter "I know plenty about the Prison, though..."

            you "Really? You do? Were you in jail?"

            carpenter "Oh no, lordy Ariossy, no!"

            carpenter "But that gig I had a while back, when we met, remember?"

            carpenter "I had been working a lot in and around the Prison. There's always work for a carpenter in there, although my so-called 'Master' took it way too far..."

            carpenter "I usually just went in to do some repairs, doors, beds, support beams... Wood gets damaged quickly; the whole place is damp as fuck, especially in the basement where they have the worst criminals."

            you "The worst criminals? Like who?"

            carpenter "Well, I'm not sure, Boss... When the knights talk between themselves, they use nicknames. 'Long ears', 'Butcher', 'Cindirella', that sort of thing."

            carpenter "One of 'em knights took a fancy to me, got loose-lipped while trying to get me drunk."

            carpenter "Said they gave fake names to the special VIP prisoners, especially when they're people the King hisself wants there... They even fake the paperwork, too."

            you "Interesting... Anything else you can tell me about the Prison?"

            carpenter "Well, sure... Get this: the Xotar Prison was not always a jail. In fact, it's built on top of a much, much older building."

            "Really? What kind of building?"

            "She spits."

            carpenter "No one knows that, Boss. The place is real {i}ancient{/i}. Summerians built it, or sumethin'."

            you "The Cimerians?"

            carpenter "Yeah, whatever. Fucking elves, or dwarves, or gnolls, hell if I can tell the difference."

            carpenter "That's where that weird name, 'Xotar' comes from. Means 'the Hub', or sumethin', in their Arios-forsaken language."

            carpenter "But one thing's pretty clear: That building was no prison. Too many ways in and out. In fact there are some paths even the Knights don't know about."

            you "And you know about them?"

            carpenter "Err... Not really. I've seen some old plans, not accurate enough to pinpoint anything."

            carpenter "But I remember there are hidden pathways, to the Sewers especially..."

            you "Oh, the Sewers. Lovely. I was just itching to go back down there..."

            carpenter "Well, whatever floats your junk, Boss."

            "You thank Iulia for her information. There's surely something useful here."

            play sound s_spell

        elif npc == NPC_ramias: # Demon-worship, High security prisoners
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            ramias "I don't know anything about that girl, but the Prison? Might have heard a thing or two."

            you "You have? When?"

            ramias "From the Knights themselves, oddly enough. They're not a talkative bunch, but the circumstances were special. I was applying for a job."

            you "A job? At the Prison?"

            ramias "Well, that wasn't my original intention. I wanted to see if the Knights needed another sword arm at the castle, but the snooty bastards took issues with me not being a blue blood."

            ramias "Instead they offered me a low-level guard job at the Prison... I should have said no from the start, but I was damn broke."

            you "What did they tell you?"

            ramias "Well, there are several areas in the Prison. The largest is on the ground floor, easily the size of a village. It holds the common criminals, where they live in incredible squalor."

            ramias "Seasoned murderers cohabit with infortunate plebs who stole a load of bread, and that goes as well as you can expect."

            ramias "The upper floors are for well-connected prisoners, or simply paying ones. They get access to better cells, sometimes single, and guaranteed food and drinks on most days."

            ramias "Have their own bathing area too, so they get shanked a lot less."

            ramias "Finally, there's the basement floor, or floors. It's the maximum security area. Who knows what goes on in there."

            ramias "Regular guards aren't allowed to pry."

            you "And where did you want to work?"

            ramias "Turns out, nowhere. I'm a fighter, but I'm not one for lording over orphans and widows that fight for scraps of bread."

            ramias "The privileged assholes upstairs would really get to me. Never cared for pandering to rich or highborn crybabies, and I've seen more than my share among the brass in the army."

            ramias "That leaves the maximum security prison... I thought about it at first, because there was an air of danger about it that appealed to me."

            ramias "Told me they lost a couple of guards just a week before, sounded more exciting than the rest."

            you "That's, uh... One way to see it."

            you "Still, you turned them down?"

            ramias "Sure did. Before I said yes, I did a bit of research by hitting the taverns. What I learnt, I didn't like one bit."

            you "What was that?"

            ramias "There were many disturbing rumors about the place, but that's to be expected. The King and his knights are not really famous for their leniency with criminals or political opponents alike."

            ramias "But the demon-worshipping stuff? Arios no, I may forget to go to church more often than not, but I ain't going near that with a ten-foot spear."

            you "Demon-worship?"

            ramias "Yup. Too much noise on the street about strange noises and lights at night, forbidden rituals... Most of the max security prison guard is corrupted, or so I heard."

            ramias "I have no doubt when the time was right, they would have tried to enlist me in their unholy schemes."

            ramias "Then I might have had to gut them, and all of that was a lot more trouble than I was asking for. I'd rather keep going with the weapon seller gig, thank you very much."

            you "This talk of demons and conspiracy sounds a little far-fetched, if you ask me."

            ramias "Mayhaps, can't say for sure. But I've found time and again that there's more truth in the divagations of drunkards than in the honey-tongued lies of the powers-that-be."

            you "Thanks for the intel, anyway. I hope it can bring me closer to catching my mark."

            play sound s_spell

        elif npc == NPC_maya: # C1 good / prison secrets, prisoner fake identity
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            maya "Kunoichi, uh? Woah, you're really doing a great job at keeping yourself in trouble."

            you "I do what I can."

            maya "You know, it's funny you should mention the Prison. I've been putting old Captain Farah's books in order lately, and some things struck me as odd."

            you "You mean... Beyond her habit of spending half the city taxes on designer lingerie?"

            maya "Yup. See, we have a register of all the criminals that were transferred to the Prison. There's a few of those each month."

            you "And?"

            maya "Well, there's at least two dozen names in there that I've never heard of. They don't match any other records. And I pride myself on knowing most if not all of our detainees."

            you "What does it mean?"

            maya "My best guess is, they were prisoners in transit, coming from outside the city. But such prisoners are usually fully registered when they come in, those were not."

            maya "And their names are the kind of usual drivel lazy spooks would use to forge records."

            maya "'Dick Puncher'? 'Bobobobo Bobobo'? 'Wolf Blitzer'?"

            maya "Obviously made up. They really didn't put in any effort."

            you "So who {i}were{/i} those prisoners?"

            maya "Beats me, but they were all bound to the maximum security part of the Prison."

            maya "I know the old Captain would sometimes send out those secret transfer convoys. But the Palace has yet to ask me to do the same."

            you "Secret convoys?"

            maya "Yeah. Always leaving at night, those. Single prisoner, heavily armed escort."

            maya "I was never chosen for escort duty, Farah preferred to send her lapdog, Sergeant Kashiv. I always suspected something was fishy."

            you "Anything else you can tell me?"

            maya "Well, it's not a lot to go on about, but... Kashiv, when she came back from such errands, she always smelled like a sewer. Arios knows where she had been."

            you "Like the Sewers, uh? Could it be she accessed the Prison that way?"

            maya "Who knows? But this kind of experience makes you hate barracks and sharing bunk beds."

            "You thank Maya for the information."

            play sound s_spell

        elif npc == NPC_lieutenant: # c1 neutral / prison secrets, prisoner fake identity
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            lieutenant "Oh, my dear [MC.name]. It's been a while. We had a good time, last time, uh?"

            "You remember the night you spent together."

            you "Hmmm... We sure did."

            lieutenant "But I understand you're here on business. My pride is hurt, but only a little."

            you "Well..."

            lieutenant "Let's cut to the chase. You mentioned a certain wounded Kunoichi, and how she was sent to Xotar Prison. I think I know something about that."

            you "Really?"

            lieutenant "Yes. You see, our old Captain used to take some hefty bribes to organize prisoner convoys of a certain kind, all with the utmost discretion, which was unusual for her."

            you "What kind of prisoner convoys?"

            lieutenant "Lone prisoners, two at most, under secret identities. The guards would come in from the road at night, load the prisoner in a box that was almost like a casket, and carry them to the Prison with an escort of guards and knights hidden in civilian clothes."

            lieutenant "Sergeant Kashiv always carried out the Captain's dirty deeds, so she was usually in charge of the escort."

            lieutenant "They'd go down into the Sewers, where I hear there are secret passages that lead into old parts of the Prison. You'd never hear from the poor sods again."

            you "How do you know about that?"

            lieutenant "I did some spying on account of Renza on such convoys, to see if they were hiding anything valuable. One night, I caught a glimpse of the prisoner as they were locking her in the box."

            lieutenant "Even though the light was low, one thing stood out... The lady only had one arm."

            you "I see! So they took her into the Sewers?"

            lieutenant "Yes. And that's the last anyone will probably hear from the poor lass, Shalia embrace her."

            "You thank the Lieutenant for the information and head back to the city, lost in your thoughts."

            play sound s_spell

        elif npc == NPC_sergeant: # c1 evil / prison secrets, prisoner fake identity

            if npc.flags["interrogate"] in ("beaten", "raped"):
                sergeant "You..."

                "Her face whitens with fear. She remembers what you did to her."

                sergeant "Get away from me! One more step and I'll kill you, you bastard!"

                "You quickly leave before she recovers from her shock and stabs you."

                return

            else:
                sergeant "I'd be damned... You dare to show your face here? Don't think I forgot the last time we met..."

                you "Call us even then. You tried to get me killed."

                you "And don't forget our mutual friend the good Captain Farah... I'm sure she would take issue with you fighting me over an old grudge."

                sergeant "Grr..."

                play sound s_sigh

                sergeant "You are correct. *sigh*"

                sergeant "Fine, I'll tell you what I know about the Prison, if it gets you out of my sight faster."

                sergeant "While there's nothing special about the Prison on the surface, the special convoys are noteworthy."

                you "Special convoys?"

                sergeant "Yup. When the Prison gets a 'VIP' prisoner, courtesy of the King, they sometimes arrives in a special convoy. Means no traces are left in the system."

                sergeant "When the Guard was involved, which was rare because no one is usually interested in VIP prisoners coming from outside the walls, I was one of those trusted with the package."

                you "The package?"

                sergeant "More like a sedan chair, really, except it's a chained metal one, and it's damn heavy."

                sergeant "No one involved in the convoy knows who we're escorting. They give him or her a fake name, and the Knights warn you in no uncertain terms than any attempt at peaking inside will end with your head on a pike."

                sergeant "As if all of that wasn't enough, they have us enter through a secret passage in the Sewers. Can't allow anyone to see who's coming in and out of the maximum security prison."

                you "And where might I find this secret doorway, exactly?"

                sergeant "Hell if I know. It's in the Sewers, but they blindfolded us as soon as we were there and had us follow the Knight's voice to move on."

                sergeant "I hated every minute of it. The blindfold makes you notice the smell a lot more, and I nearly stumbled into the waste stream a dozen times."

                sergeant "Anyway, that's all I know. Scram now, will you?"

                "You reflect on what she told you. Could this help with your chase?"

            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            play sound s_spell

        elif npc == NPC_goldie: # Earth rune
            if not NPC_goldie.flags["introduce earth rune"]:
                $ NPC_goldie.flags["introduce earth rune"] = True

                goldie "Ninja women with a dark and terrible past? Wow, [MC.name]! What an exciting and glamorous life you're living..."

                you "Yeah, well, I hope this isn't the kind of adventure that ends with me taking a shuriken to the back of the head."

                goldie "Oh, don't say that, [MC.name]! If anything happened to you, I would be unconsolable..."

                "She looks genuinely worried about you."

                goldie "You know, I think I have just the thing. It's been in my family for generations, my Pa' used to say it would bring us good luck."

                goldie "It's a runic stone, the kind that shamans of old used to fashion in the way the Cimerians did. Or so they said."

                goldie "This one has the Earth symbol, so it's appropriate if you're after an Earth ninja. Maybe. I don't really know anything about ninjas, except from novels."

                you "Thank you... This looks expensive, are you sure I can have it?"

                goldie "Well... It's true that I don't have a lot to go on these days, but if it's you... *blush*"

                you "(This would probably fetch hundreds of denars on the market... What should I do?)"

            else:
                goldie "Oh, [MC.name], you(re back. I assume this is about the Earth stone?"

            label c2_goldie_buy_rune():
                menu:
                    "What will you do?"

                    "Grab the stone for free":
                        you "(This offer is too good to pass.)"

                        you "Thank you Goldie, I'll have the stone, then."

                        "She gives a last look at the stone, and you can see some anguish in her eyes. But she steels her resolve, and gives it to you."

                        $ MC.good -= 1

                    "Give her 500 gold for it":
                        if MC.gold < 500:
                            "You don't have enough money."
                            jump c2_goldie_buy_rune

                        "You give her the minimum price you think such a stone could be worth."

                        you "Here, please take this gold as compensation. I wouldn't feel right depriving you of such a valuable object when you're struggling."

                        goldie "Oh, thank you... You didn't have to..."

                        you "You're welcome."

                        $ MC.neutral += 1
                        $ NPC_goldie.love += 1

                        play sound s_gold
                        $ MC.gold -= 500

                    "Give her 1,000 gold for it":
                        if MC.gold < 1000:
                            "You don't have enough money."
                            jump c2_goldie_buy_rune

                        "You give her a good price for what you think the stone is worth."

                        you "Here, I don't want to cheat you of such a valuable object in yout time of need."

                        goldie "Oh, thank you! This is too much!"

                        you "No, please, have it. It's my pleasure."

                        goldie "Thank you so much!"

                        "She gives you a grateful kiss."

                        $ MC.good += 1
                        $ NPC_goldie.love += 1

                        play sound s_gold
                        $ MC.gold -= 1000

                    "Come back later":
                        you "Thank you for your offer, but I can't accept just yet. I will be back."
                        return

                $ story_flags["earth rune"] = True

                call receive_item(earth_rune) from _call_receive_item_22

                goldie "May it protect you from harm, dear [MC.name]."

                you "Thank you sweetie."

    return


## Unlocking ninjas ##

label c3_unlock_narika():

    hide screen districts

    play music m_suspense fadein 3.0

    show bg narika intro at sepia with dissolve

    if NPC_narika.flags["hint recap"]:
        menu:
            suzume "So, I think we've gathered enough intel about the Void ninja! What do you want to do?"

            "Can you recap the intel again?":
                pass

            "Visit the Magic University":
                if NPC_narika.flags["magicu failed"]:
                    you "Yeah, after what happened I don't think I can show my face around there for some time."
                else:
                    call c3_narika_MU_visit() from _call_c3_narika_MU_visit
                return

            "Try to catch her again":
                if story_flags["ninja hunt"] == calendar.time:
                    "You can only attempt to catch a ninja once a day."
                    return

                hide screen overlay
                scene black with fade
                show bg rooftop at top with dissolve
                call ninja_game(NPC_narika) from _call_ninja_game_3
                return

            "Look for her later in the city":
                return

    else:

        suzume normal "I think now we have a pretty good idea of what that little brat is up to!"

        you "Have we? Can you recap?"

    suzume "Sure. Here's what we've gathered so far."

    suzume "Narika is organizing a heist of some sorts. She may have a powerful backer."

    if NPC_narika.flags["upper city hint"]:
        suzume "It's clear her mark is in the upper city. That's beyond our current reach, but we can probably get a safe-conduct from the Princess."

    if NPC_narika.flags["uniform hint"]:
        suzume "We also know it's a place where they wear uniforms. That's an important clue."

    if NPC_narika.flags["school hint"]:
        suzume "And the mark is a school. That narrows it down significantly."

    if NPC_narika.flags["magic hint"]:
        suzume "Finally, she's going after a magical artefact! There are only a few places where such important magical items could be found."

    suzume "Which means..."

    you "The Magic University."

    suzume "Of course. See, it wasn't hard."

    suzume "Void ninjas don't rely on magic to be effective, so they are better suited to taking on a target with magical protection. It must have been important to whoever recruited her."

    you "Fine. Now, we know what she's after. But how do we get to her?"

    suzume "Well, I see a couple of ways to go about this."

    you "Tell me."

    suzume "First, you could report your findings to the Dean of Magic U."

    suzume "They would be able to thwart the heist, and probably have the means to lock the Void ninja up."

    suzume "In doing so, we would be gaining a useful ally, as well as fulfilling the Princess's mandate."

    you "I see. Anything else?"

    suzume doubt "There's another option. It's a little unorthodox, even for you... But hear me out."

    suzume normal "What if we {i}helped{/i} her steal that artefact?"

    you "Whaaat?" with vpunch

    suzume "Think about it. We could split the proceeds of the heist, and make her an ally. Then we'd get her to spill the beans about her backer."

    you "Err, I don't know if the Princess would like us to do that."

    suzume "Aha, but think about it this way: there's no love lost between the Royals and the Mages."

    you "There isn't?"

    suzume "Nope. The Zanic Magic Guild remained neutral during the change of dynasty 25 years ago. They waited until power was well into the hands of the Pharo dynasty to begrudgingly declare allegiance."

    if MC.playerclass == "Wizard":
        you "It's nothing personal, wizards are not supposed to meddle in regime change. Too many bad precedents."
    else:
        you "An abundance of caution, eh? So much for scheming wizards."

    suzume "Anyway, King Pharo always keeps the Magic Guild at arm's length, knowing they are unreliable allies."

    suzume "If you can get Narika to leave Zan's nobility in peace, the Princess might just turn a blind eye to you messing with the Magic University."

    you "Hmmm..."

    $ NPC_narika.flags["hint recap"] = True
    $ NPC_narika.flags["hunt stage"] = 3
    $ NPC_narika.location = spice_market

    if MC.has_item(void_rune.name):
        suzume "I can think of something else. Remember that Cimerian device you bought?"

        you "The Void Rune? It's supposed to slow down time?"

        suzume "Yes. I can see how that could mess with her powers. If you can catch her again in the city, maybe we could beat her this time."

        if NPC_freak.flags["holding info"]:
            suzume "And put her in one of the Cimerian-built cells the perverted old man mentioned."

            you "So you know about that, uh."

            suzume "Yup."

        else:
            suzume "But you lack the means to hold her. We would have to deliver her to the Princess quickly and get it over with."

            suzume "Unless you can figure out a way to keep her locked up."

        you "Capturing her, hmmm..."

    jump c3_unlock_narika

label c3_unlock_haruka():

    # Hints: High security prisoners, Demon-worship, prison secret passage, prisoner fake identity

    hide screen districts
    play music m_suspense fadein 3.0

    show bg haruka defeat1 at sepia with dissolve

    if NPC_haruka.flags["hint recap"]:
        menu:
            suzume "So, I think we've gathered enough intel about the Earth ninja! What do you want to do?"

            "Can you recap the intel again?":
                pass

            "Let's negotiate with her":
                call ninja_game(NPC_haruka)
                # call c3_haruka_final_intercept() from _call_c3_haruka_final_intercept
                return

            "Let's warn the guards she's coming":
                hide screen overlay
                call c3_haruka_guards() from _call_c3_haruka_guards
                return

            "Look for her later in the city":
                return

    else:
        suzume normal "I think we've gathered enough intel about that stuck-up Earth ninja and her scheme!"

        you "Did we? Let's do a recap."

    suzume "Well, it's obvious that she is trying to rescue her former mentor, Subaru."

    suzume "She was captured in the destruction of their temple, far away from here."

    show bg prison at sepia with dissolve

    suzume "And Haruka believes Subaru is being kept in the city's Prison. If she is, she must be in the basement, where the {b}maximum security quarters{/b} are located."

    you "But there is no record of her ever being there."

    suzume "True, but it does not necessarily mean she isn't. As we've learnt, sometimes they bring secret convoys to the Prison, {b}registering captives under fake names{/b}."

    you "Kenshin leads the Royal Knights, and she told us that she knows all about the high-security prisoners. She didn't mention Subaru."

    suzume doubt "Well, maybe she got sloppy. Or..."

    suzume "Kenshin may be in on the plot. You should be careful around her."

    suzume "Regardless, they go to great lengths to avoid scrutiny, even bringing in the captives through a {b}secret passage in the Sewers{/b}."

    you "Shady stuff..."

    suzume "That's right. That leads us to the most concerning piece of the puzzle..."

    you "Which is?"

    suzume "{b}Demon-worshippers{/b}. Some of our contacts have mentioned rumors, and they're the ones who abducted Subaru in the first place."

    suzume doubt "If there is any chance demon-worshippers are being involved, we should be extra careful."

    you "*gulp*" with vpunch

    suzume shrewd "That's a lot to take in."

    you "Sure, but... How does it help us catch Haruka? That's our goal, remember?"

    suzume doubt "Well, the way I see it, you have a few options."

    you "I do?"

    suzume "All the information we've gathered could prove valuable to Haruka. Maybe we can strike a deal with her."

    suzume "We just want her to stop murdering people in the city. The sooner she frees Subaru, the faster she'll get out of our hair."

    you "What if in freeing her, she murders a bunch of people?"

    suzume shrewd "Well... As long as they're not rich and famous, I don't think the Princess would care much."

    you "What other options do I have?"

    suzume doubt "We could go to the prison guards and warn them, in exchange for their help catching her."

    you "That sounds sensible... But what if they're as corrupt as the guard in the Slums? I don't see why they wouldn't be."

    suzume "Then we can attempt to turn that to our advantage, maybe strike a deal with them or something."

    you "Hmm..."

    $ NPC_haruka.flags["hint recap"] = True
    $ NPC_haruka.flags["hunt stage"] = 3
    $ NPC_haruka.location = prison

    if MC.has_item(earth_rune.name):
        suzume "And finally, there's that magic stone you found."

        you "The Earth Rune? Would that work on her?"

        suzume "The only way to know is to try it. If you can catch her again in the city, maybe we can pass her defenses this time."

        you "Then I could capture her on my own..."

        if NPC_freak.flags["holding info"]:
            suzume "And maybe throw her in one of the magic-proof cells the perverted old man mentioned."

            you "Maybe. Wait a- Do you just follow me everywhere?"

            suzume "Sure."

            you "{i}Everywhere{/i}?" with vpunch

            suzume "Yup."

            you "..."
        else:
            suzume "Sure. But if you have no way to hold her, you will have to turn her in for a reward."

    jump c3_unlock_haruka


## Papa Freak events ##

label c3_papa_cells():

    hide screen overlay
    scene black
    show bg papa_freak at top
    with dissolve

    if not NPC_freak.flags["requirements"]:
        if not NPC_freak.flags["cells built"]:
            papa "So, for starters... I'm looking for a great cocksucker."

            papa_apprentice "Papa likes it wet and nice, uh..."

            you "I don't need details. Please."

            papa "Bring us a whore that offers great service, is beautiful and perverted, and we'll build you a cell."

            "Bring a whore to Papa with at least {b}75 in Service, Beauty and Libido{/b}."

            $ game.set_task("送一个妓女给弗里克老爹让他好好品尝，她的侍奉熟练度，外貌和性欲属性必须达到75点。", "papa", blocking=False)
            $ NPC_freak.flags["requirements"] = [("service", 75), ("beauty", 75), ("libido", 75)]

        elif NPC_freak.flags["cells built"] == 1:

            papa "Now Papa wants to reward his apprentice. He's been working hard, lately."

            papa_apprentice "Oooh, thank you, Papa!"

            papa "But we'll take turns, of course. Can't let you have all the fun."

            papa_apprentice "Ew, I knew there was a trick."

            papa "What kind of girl would you like, my boy?"

            papa_apprentice "Well, good at sex, of course... With a good personality, and a sensitive body... Hmmm. *drool*"

            "Bring a whore to Papa with at least {b}75 in Sex, Charm and Sensitivity{/b}."

            $ game.set_task("送一个妓女给弗里克老爹让他好好品尝，她的性交熟练度，魅力和敏感属性必须达到75点。", "papa", blocking=False)
            $ NPC_freak.flags["requirements"] = [("sex", 75), ("charm", 75), ("sensitivity", 75)]

        elif NPC_freak.flags["cells built"] == 2:

            papa "Did you like that last one, my boy?"

            papa_apprentice "I did... I had such a great time."

            papa "But you wanted more, didn't you? Can't hide it from Papa..."

            papa_apprentice "Well... It's true. I wish I could have fucked her ass."

            papa "Anal? You kinky little rascal."

            papa "All right, our next order is: an anal whore! She must have a good body, of course, and be obedient."

            "Bring a whore to Papa with at least {b}75 in Anal, Body and Obedience{/b}."

            $ game.set_task("送一个妓女给弗里克老爹让他好好品尝，她的肛交熟练度，身材和服从属性必须达到75点。", "papa", blocking=False)
            $ NPC_freak.flags["requirements"] = [("anal", 75), ("body", 75), ("obedience", 75)]

        elif NPC_freak.flags["cells built"] == 3:

            papa "This one must be special. I have this list of fantasies I have yet to achieve..."

            papa_apprentice "Papa wants to get frea-kyyyy~..."

            you "Please. Don't do that. "

            extend "Ever. "

            extend "Again."

            papa "Bring me a whore with kinky tastes, who is both refined and physically resilient. This is our last order! Let's make her count!"

            "Bring a whore to Papa with at least {b}75 in Fetish, Refinement and Constitution{/b}."

            $ game.set_task("送一个妓女给弗里克老爹让他好好品尝，她的调教熟练度，优雅和体质属性必须达到75点。", "papa", blocking=False)
            $ NPC_freak.flags["requirements"] = [("fetish", 75), ("refinement", 75), ("constitution", 75)]

        scene black with fade

        return


    else:
        $ req_skills = tuple(sk.capitalize() for sk, v in NPC_freak.flags["requirements"])
        $ req_val = NPC_freak.flags["requirements"][0][1] # Cannot handle separate skill requirements for now
        $ req = and_text(req_skills)

        if MC.girls:
            "Choose a girl from your brothel to bring with you (reminder: she must have at least [req_val] in [req], and be open to whoring)"
            $ girl = long_menu("Choose a girl", [(g.fullname + " (%s %i, %s %i, %s %i)" % (req_skills[0], g.get_stat(req_skills[0]), req_skills[1], g.get_stat(req_skills[1]), req_skills[2], g.get_stat(req_skills[2])), g) for g in MC.girls])
        else:
            "You cannot satisfy Papa Freak's requests, as you have no girls in your brothel."
            return

        scene black with fade
        show bg papa_freak at top with dissolve

        papa "So, my young friend, have you brought me a suitable whore?"

        you "Yes, Papa. I would like you to meet [girl.name]."

        call dialogue(girl, "girl introduction") from _call_dialogue_252

        papa_apprentice "She's hot! I like her."

        papa "Let me see..."

        python:
            for stat, val in NPC_freak.flags["requirements"]:
                if girl.get_stat(stat) < val:
                    failed_stat = capitalize(stat)
                    break
            else:
                failed_stat = None

        if debug_mode:
            menu:
                "Force success"

                "Yes":
                    $ failed_stat = None

                "No":
                    pass

        if failed_stat:
            papa "No, that won't do, that won't do at all... I'm sorry, young lady. Come back when you've had more training."

            "You need a girl with higher {b}[failed_stat]{/b} to satisfy Papa Freak's request."

            return

        papa "She looks perfect... Come now, my pretty, Papa and his young apprentice have been waiting for you..."

        girl.char "What is it about, Master?"

        "You explain what she needs to do."

        $ sex_act = NPC_freak.flags["requirements"][0][0]
        $ forced = False

        if debug_mode:
            menu:
                "Force success"

                "Yes":
                    $ forced = True

                "No":
                    pass

        if not girl.will_do_sex_act(sex_act) and not forced:
            play sound s_surprise
            if sex_act == "service":
                girl.char "Suck that old man's junk? No way! Don't make me!"
            elif sex_act == "sex":
                girl.char "Sleep with those guys? No! I don't want to!"
            elif sex_act == "anal":
                girl.char "Take it in the ass, from them? No!!!"
            elif sex_act == "fetish":
                girl.char "Ew, but I don't want to do kinky things with those two! No way!!!"

            papa "I see. Boy, isn't that a sad turn of events..."

            papa "But I won't force anybody. Please come back when she's more open-minded about [sex_act]."

            "The girl needs to agree to {b}[sex_act]{/b} acts before you can satisfy Papa Freak's request."

        else:

            girl.char "I understand, Master [MC.name]. I will do my best."

            papa "That's the spirit! Now, come here, I would like to see those titties up close... Fuhahahaha!"

            scene black with fade

            play sound s_moans_short

            show screen show_img(girl.get_pic(sex_act, "naked", hide_farm=True))
            with dissolve

            girl.char "Oh, aaah, oooh!!!"

            papa "Yes! Yes! Just like this!!!"

            show screen show_img(girl.get_pic(sex_act, "service", "naked", and_tags="cumshot", hide_farm=True))
            with flash

            play sound s_orgasm_fast

            girl.char "Aaaah!!!"

            with doubleflash

            hide screen show_img
            scene black
            with fade

            show bg papa_freak at top with dissolve

            papa "Oh boy... She's really something. Can I get another go?"

            you "Yes. But you must build me a cell, first."

            papa "You got it. What will it be?"

            menu:
                extend ""

                "Build me a cell with a Void ward" if not story_flags["void ward"]:
                    $ target = "void"

                    papa "This is a complex element, if it is an element at all... Fortunately, the old Cimerians knew a thing or two about manipulating time and space."

                "Build me a cell with a Water ward" if not story_flags["water ward"]:
                    $ target = "water"

                    papa "Ah, water... I've this special desiccant technology I've been experimenting with. I thought it was only good for preserving cookies, but I might find a use for it after all"

                "Build me a cell with an Earth ward" if not story_flags["earth ward"]:
                    $ target = "earth"

                    papa "This is straightforward enough. Metal blocks most Earth magic. A cell made entirely of steel would do the trick."

                "Build me the cell with a ward against Air and Fire" if (story_flags["void ward"] and story_flags["water ward"] and story_flags["earth ward"]):
                    $ target = "air and fire"
                    $ story_flags["air ward"] = True
                    $ story_flags["fire ward"] = True

                    papa "Two elements of swift movement and destruction... Earth blocks most of their effects, so we'll take the cell that's deeper underground. And those runic stabilizers should do the rest."

            $ story_flags[target + " ward"] = True

            scene black with fade

            play sound s_saw

            pause 0.3

            play sound2 s_clash

            pause 0.3

            play sound s_vibro

            papa_apprentice "Phew... *pant* *pant*"

            papa_apprentice "Everything is in place, Papa, just like you instructed."

            papa "Perfect! Here you go, young man, just as we agreed. You now have a nice holding cell that will ward against [target] powers."

            $ NPC_freak.flags["cells built"] += 1
            $ NPC_freak.flags["requirements"] = None

            $ renpy.block_rollback()

            if (story_flags["void ward"] and story_flags["water ward"] and story_flags["earth ward"] and story_flags["fire ward"]):
                papa "This was the last one. Your basement is now fit to capture a small army of elemental ninjas."

                you "I was going to install a game room, but that works too."

                papa "See you around soon, my boy!"

                $ NPC_freak.location.action = False
                $ game.set_task(None, "papa")

                you "Sure."

            elif NPC_freak.flags["cells built"] < 3:
                you "Can you build me any more holding cells?"

                papa "Can I? Sure. But will I? There needs to be something in it for me..."

                you "All right. Name your poison."

            elif NPC_freak.flags["cells built"] < 4:
                you "So this is it, then?"

                papa "Well... There is one more elemental cell I could restore, but you didn't ask me about it..."

                you "Which one?"

                papa "The Air and Fire ward room. It blocks not one but two elements. Nice, isn't it?"

                you "Yeah... But I have no need to imprison someone with one of those elements."

                papa "Not now you don't, but if the eventuality presented itself, wouldn't it be nice to have a cell ready?"

                you "*sigh* What do you want for it?"

            jump c3_papa_cells

    scene black with fade

    return


## Homura city events ##

label c3_contact_homura():

    "You remember what Homura told you about tying her ribbon to a pole at the Plaza to summon her."

    if NPC_homura.flags["is summoned"]:
        you "I already tied the ribbon to summon her. She will come to me, eventually?"
    
    elif brothel.has_room("okiya"):
        you "Here, let's see if that does the trick."

        if blue_ribbon in MC.items:
            $ MC.items.remove(blue_ribbon)
            $ plaza.action = False

        $ calendar.set_alarm(calendar.time, StoryEvent(label = "c3_homura_visit", type = "night"))

        $ NPC_homura.flags["is summoned"] = True

    else:
        you "She did mention I needed to build an okiya first... No point in summoning her now."

        "You must buy the {b}Okiya{/b} before you can contact Homura again."

    return

label c3_homura_visit(): # Happens after tying the ribbon in the plaza

    scene black with fade
    show bg okiya at top with dissolve

    play music m_palace fadein 3.0

    "That night, you keep an eye out for Lady Homura. Sure enough, it isn't long before you spot her entering the Okiya, bowing politely to your staff."

    $ NPC_homura.flags["is summoned"] = False

    show bg homura_okiya happy at top with dissolve

    if not story_flags["homura summoned"]: # first visit
        $ story_flags["homura summoned"] = True
        if not story_flags["suzume hint seen"]:
            $ story_add_event("c3_suzume_hint", "daily")

        homura normal "[MC.name]! I thought you'd never contact me again."

        homura blush "I was a bit scared, to be honest. *frown*"

        you "Why would I let you down?"

        homura "Well, I thought, because we had, hem... You know..."

        homura "I thought maybe a man in your occupation might just care about... *blush*"

        menu:
            "Tell her you're not like that": # For good characters
                you "I'm not like that, you know."

                if MC.get_alignment() == "good":
                    homura normal "I know. You're a good person."

                    homura "I'm just surprised that... You do this."

                    you "It's just a job. Besides, if this trade was only left to the bad guys, it would be bad, wouldn't it?"

                    play sound s_laugh
                    homura "You make a good point!"

                    $ NPC_homura.love += 2

                elif MC.get_alignment() == "neutral":
                    homura "Well... So you say. But I don't know if your actions match your words."

                    you "Well, I try my best..."

                    $ NPC_homura.love -= 1

                elif MC.get_alignment() == "evil":
                    homura sad "I find that hard to believe. I've heard stories about how you treat people, you know."

                    you "Uh? Who rated me out? I'll smash their..."

                    play sound s_sigh
                    homura "See? This is what I'm talking about."

                    $ NPC_homura.love -= 2

            "Tell her she's different": # For neutral characters
                you "In other circumstances, you would be right. But there's something special about you."

                homura blush "Hmmm..."

                if MC.get_alignment() == "neutral":
                    homura normal "Haha, I knew it! Well, I guess I should count myself lucky then..."

                    $ NPC_homura.love += 1

                elif MC.get_alignment() == "good":
                    homura sad "Really? That's a litle cold, coming from you. I thought you were a more caring person."

                    you "Well, maybe I should have put it differently..."

                    $ NPC_homura.love -= 1

                elif MC.get_alignment() == "evil":
                    play sound s_sigh
                    homura sad "You say I'm different, but how do I know that you don't say that to all girls? I know your kind."

                    you "Well..."

                    $ NPC_homura.love -= 1

            "Tell her you still need her": # For evil characters
                you "I'll be blunt. I'm not one for commitment. But right now, I still need you."

                if MC.get_alignment() == "evil":
                    homura blush "I expected as much... But thanks for giving to me straight."

                    homura "I'm an adult just like you... I make my choices."

                    you "It's good that we understand each other."

                    $ NPC_homura.love += 2

                elif MC.get_alignment() == "neutral":
                    homura "Okay... I see. I don't know what I was expecting. ."

                    you "Sorry about that."

                    homura "Yeah."

                    $ NPC_homura.love -= 1

                elif MC.get_alignment() == "good":
                    homura sad "Really? But Iheard such good things about you... I thought..."

                    you "Err, sorry. I mean, I care for you, but..."

                    play sound s_sigh
                    homura "Save it. It's off your chest, at least."

                    $ NPC_homura.love -= 2

        homura normal "Anyway. So, this is your new house? It's nice. The okiya looks good."

        homura sad "My ears are ringing, though... There's something odd about this place."

        if MC.playerclass == "Wizard":
            you "Ah yes, you noticed. The walls are infused with ancient magic."

            you "It normally only affects people with elemental affinity, though. You may be experiencing some kind of magic resonance. Do you have magical affinity?"

        else:
            you "Well, the previous owner mentioned something about magic wards, messing with spells or whatever."

            you "Why, are you a magic user?"

        play sound s_laugh
        homura normal "Oh, absolutely not! The less I am around magic the better. I just don't trust magic."

        you "Isn't your father a mage, though?"

        homura "Well, uh... Yes, I guess he is."

        you "You never wanted to follow into his footsteps?"

        homura "Uh... Oh, no."

        homura "He wouldn't have allowed me, anyway. Wizards think magic is better left to men."

        you "Really? But there are many women sorceresses..."

        homura "Let's just not discuss my father's views on women. He's a typical male, thinking they should use brooms to clean up the kitchen instead of flying."

        menu:
            extend ""

            "He's wrong, of course":
                $ MC.good += 1

                you "That's just wrong. Women are just as capable as men... They can do great things..."

                homura "Oh, really? Look at you, making money from whoring girl slaves out... Quite the feminist."

                you "Ouch..."

                if NPC_homura.love >= 5:
                    homura sad "Sorry, that was uncalled for."

                    you "It's all right..."

                    $ NPC_homura.love += 1

            "He's got a point":
                $ MC.evil += 1

                you "Look, he's not wrong. Women are less capable than men, it's obvious."

                you "It's only right that you should serve us..."

                play sound s_surprise
                homura surprise "What? Are you out of your mind?"

                homura "That's a new low, even for you!"

                you "Hehe, you're cute when you're angry..."

                homura "Shut up! And remove your hand!"

                $ NPC_homura.love -= 3

            "There are much more interesting things to do with women":
                $ MC.neutral += 1
                you "Such a sad lack of imagination. Women are wonderful, everywhere... Especially..."

                homura blush "S-Shut up, I know what you're going to say..."

                you "We're compatible, men and women, that's all I'm saying. *wink*"

                homura "Err, stop it..."

                homura "..."

                homura "It's kind of sexy when you talk like that, though."

        homura normal "Back on topic. You wanted to see me?"

        you "Yeah."

    else:
        homura "Hello, [MC.name]! I'm glad you called me again."

        you "Glad to see you, too."

    homura "So. Is it business, or pleasure?"

    menu:
        extend ""

        "Business":
            you "Business, I'm afraid. You remember about the task that the Princess gave me?"

            if NPC_homura.flags["divulged assignment"]:
                homura "Yes, of course. You're hunting those weird women ninjas, the kuno... Something."

                you "Right. I was wondering if you could help me figure out my options."

                homura "I'm going to do my best! Shoot!"

                call c3_homura_menu_business() from _call_c3_homura_menu_business

            else:
                homura "Of course... Are you ready to tell me more about it? I can help you!"

                menu:
                    you "Well..."

                    "Yes":
                        $ NPC_homura.flags["divulged assignment"] = True

                        you "Yes. I need help, and I don't think I can manage this alone."

                        homura "Awesome! Now tell me! I'm so curious..."

                        with fade

                        "You spend a long time telling her about your assignment and the Kunoichi."

                        with fade

                        homura "Secret female ninjas terrorizing the city... This is even better than the illegal picture books I buy at the Spice Market!"

                        homura "So, what can I help you with?"

                        call c3_homura_menu_business() from _call_c3_homura_menu_business_1

                    "No":
                        you "No, sorry."

                        homura "..."

                        you "It's really a secret. I can't talk about it."

                        homura sad "I see... But, then, I can't help you..."

                        you "Err... I guess not..."

                        homura "Such a waste of time..."

            if NPC_homura.love + dice(6) > 10:
                with fade
                homura blush "Say, [MC.name]..."

                "Homura has had a few drinks, and she now leans close to you. You can feel her hair brush against your neck."

                homura "I know you called me for a serious discussion, but... Perhaps we could take this elsewhere?"

                menu:
                    extend ""
                    "Let's go to the bedroom":
                        $ NPC_homura.love += 0.5

                        you "Of course, Lady Henso... Follow... Hey!"

                        "She's already grabbing your hand, pulling you towards the stairs."

                        call c3_homura_menu_pleasure() from _call_c3_homura_menu_pleasure

                    "Perhaps another time":
                        $ NPC_homura.love -= 0.5

                        you "I would love to, Homura, but I'm really busy right now..."

                        homura sad "Oh, I see."

        "Pleasure":
            you "Pleasure, of course."

            call c3_homura_menu_pleasure() from _call_c3_homura_menu_pleasure_1

    scene black with fade
    show bg okiya at top with dissolve
    show homura normal with dissolve

    homura "I'll be going, then. Here, take my ribbon, in case you need to contact me again."

    you "Thank you..."

    call receive_item(blue_ribbon, use_article=False) from _call_receive_item_23
    $ plaza.action = True

    return

label c3_homura_menu_business():

    menu:
        "Tell her about Narika, the Void Kunoichi" if NPC_narika.flags["locked"]:
            with fade
            "You spend a long time explaining about the Void Kunoichi and the details of your encounter."

            homura normal "I see... So she's preparing a heist, you think?"

            you "Yes. It would be good if I could figure out her target."

            homura "You need to talk to someone from the criminal world, then... Or perhaps to someone from the law, but with underground connections?"

            homura "Perhaps you can also figure out where she plans to sell her loot?"

            you "Those are all good ideas."

            homura "Anything else you can tell me about her?"

            if NPC_narika.flags["spied masturbating"]: # if event_dict["c2_narika_H1"].happened:
                you "Well... We could get a glimpse of her using a magic crystal..."

                you "She was wearing a school uniform."

                homura "Really? She's a student? That doesn't make sense!"

                homura "It must be a cover for her hit job, whatever it is..."

                homura "Perhaps ask someone who might know the city's schools?"

                you "Err, do I know anyone like that?"

        "Tell her about Mizuki, the Water Kunoichi" if NPC_mizuki.flags["locked"]:
            with fade

            "You spend a long time explaining about the Water Kunoichi and the details of your encounter."

            homura normal "A lady who doesn't age, and disappears at will... This stinks to high heaven of powerful magic."

            you "Indeed. But it's beyond the abilities of most mages I've ever seen, and yet she doesn't seem like a fully trained sorceress."

            homura "I would start with interrogating magic-users, preferably unconventional ones."

            homura "And if she's really lived for as long as she claims, perhaps ask some old-timers about her? They might know some stories."

            you "You're right."

        "Tell her about Haruka, the Earth Kunoichi" if NPC_haruka.flags["locked"]:
            with fade

            "You spend a long time explaining about the Earth Kunoichi and the details of your encounter."

            homura normal "This one looks tough-as-nails... I'm impressed."

            homura "So she's after a prisoner, you say? You need to talk to someone from law enforcement who knows the security arrangements around the prison."

            homura "They might even know where this Subaru woman is being held."

            you "Makes sense. I'll start with them."

    homura "I'm afraid that's all I got for now. I can't stay much longer..."

    you "It's alright. Thank you very much for your help."

    scene black with fade

    if story_flags["suzume hint seen"]:
        "Talk to Suzume on the {b}City{/b} screen to pay a visit to your contacts in Zan."

    return

label c3_homura_menu_pleasure():

    stop music fadeout 3.0

    # Unlocks new sex acts as the story progresses (except anal - unlocked through story)

    $ ninja_lock_count = sum(1 for x in [NPC_narika, NPC_mizuki, NPC_haruka] if x.flags["locked"])

    if ninja_lock_count >= 3 and NPC_homura.flags["H level"] == 3:
        homura normal "Pleasure! Yay!"

        homura "You know what, we still have a few hours of daylight. Why don't we go outside for a stroll?"

        you "A stroll? Not quite what I had in mind..."

        homura "Oh, come on! It will be fun!"

        call homura_river() from _call_homura_river
        $ NPC_homura.love += 1
        $ NPC_homura.flags["H level"] += 1

        return

    homura blush "I see... Let's take it upstairs, then."

    you "Come."

    scene black with fade
    show expression brothel.master_bedroom.get_pic() at top
    with dissolve

    show homura blush with dissolve

    if ninja_lock_count and NPC_homura.flags["H level"] == 1:
        call homura_69() from _call_homura_69
        $ NPC_homura.love += 1
        $ NPC_homura.flags["H level"] += 1

    elif ninja_lock_count >= 2 and NPC_homura.flags["H level"] == 2:
        call homura_cowgirl() from _call_homura_cowgirl
        $ NPC_homura.love += 1
        $ NPC_homura.flags["H level"] += 1

    else:
        homura "So. What do you want to do?"

        menu:
            extend ""

            "I want to see you masturbate":
                call homura_mast(False) from _call_homura_mast_1

                scene black with fade
                show expression brothel.master_bedroom.get_pic() at top
                with dissolve

                show homura naked with dissolve

                homura "Did I give you a good show? But... It felt lonely..."

                $ NPC_homura.love += 0.25

            "I want a blowjob":
                call homura_bj(False) from _call_homura_bj_1

                scene black with fade
                show expression brothel.master_bedroom.get_pic() at top
                with dissolve

                show homura naked with dissolve

                homura "Well, someone looks like he enjoyed himself... But what about me?"

                $ NPC_homura.love += 0.25

            "Let's do 69" if NPC_homura.flags["H level"] == 2:
                call homura_69(False) from _call_homura_69_1

                scene black with fade
                show bg homura_rest1 at top with dissolve

                homura "Wow... Was it as good for you as it was for me?"

                $ NPC_homura.love += 0.5

            "Let's have sex (missionary)":
                call homura_sex(False) from _call_homura_sex

                scene black with fade
                show bg homura_rest1 at top with dissolve

                homura "It's always good when you're inside me..."

                $ NPC_homura.love += 0.5

            "Let's have sex (cowgirl)" if NPC_homura.flags["H level"] == 3:
                call homura_cowgirl(False) from _call_homura_cowgirl_1

                scene black with fade
                show bg homura_rest1 at top with dissolve

                homura "I like being on top, it's an intoxicating feeling..."

                $ NPC_homura.love += 0.5

            "Let's go outside" if NPC_homura.flags["H level"] == 4:
                call homura_river(False) from _call_homura_river_1

                show bg forest at top with fade
                show homura naked with dissolve

                homura naked "Wow, having sex outside is so much fun... It always feels as if someone could catch us at any moment. [emo_heart]"

                $ NPC_homura.love += 0.5

            "Let me do your ass" if NPC_homura.flags["H level"] == 5:
                call homura_anal(False) from _call_homura_anal

                scene black with fade

                if NPC_homura.love > 10:
                    show bg homura_rest4 at top with dissolve

                    play sound s_mmmh
                    homura naked "Oh, that was rough... But I loved it. [emo_heart]"
                    $ NPC_homura.love += 0.5
                elif NPC_homura.love <= 5:
                    show bg homura_rest3 at top with dissolve

                    homura naked "Oh, that was too rough..."
                    $ NPC_homura.love -= 0.5

            "Nothing":
                you "Sorry, I changed my mind."

                play sound s_surprise
                homura surprise "Whaaat? Aw, are you toying with my feelings? *frown*"

                $ NPC_homura.love -= 0.5

                return

    return

label homura_69(first=True):

    scene black with fade

    if first:
        show bg homura_naked1 at top with dissolve

        homura naked "So... What should we do now..."

        you " Let's see. Last time you made me feel good with your mouth... Can you do it again?"

        show bg homura_naked2 at top with dissolve
        play sound s_surprise

        homura "B-But... I want to enjoy myself too!"

        you "Okay then, I know what to do..."

    show bg homura_69_1 at top with dissolve

    play sound s_sucking

    homura "Mmh, nggh, hmmm..."

    you "That's it, work it nicely..."

    homura "Like thish? Hmmm..."

    "She looks very concetrated as she licks your shaft up and down, squeezing the base with her small hand."

    "Spreading her pussy lips open with your fingers, you can see she is already moist."

    you "Does this turn you on?"

    homura "Shhh... Shtop it... You know it does... Mmmh... *lick*"

    "She gently cups your balls in her hand, licking them."

    you "Your technique is improving fast... Hmmm..."

    homura "I am a fasht learner... *kiss*"

    you "I can see that... Hmm."

    "After teasing her with your fingers, you bring your face very close to her slit, breathing hard."

    show bg homura_69_2 at top with dissolve

    homura "Oh, I can feel... Oh..."

    "Juice is already running out of her pussy when you put your tongue to work. She gasps as you push it inside her."

    homura "Oh! Aaaah!!! [emo_heart]"

    "Your dick is getting slippery with her saliva as she increases her pace. At the same time, you lick her clit and pussy lips, careful to keep her on the edge."

    homura "This is too good, oh, ohh..."

    "She furiously grinds her pussy in your face, losing all self-control. You respond by burying your tongue deep inside her, still rubbing her clit with your fingers."

    homura "I'm... I'm..."

    show bg homura_69_3 at top with flash

    homura "Cummmiiiing!!!"

    with doubleflash

    play sound s_orgasm_young

    homura "AAAH, AAAAH!!!"

    show bg homura_69_4 at top with flash

    "She trembles with pleasure as an orgasm wave rocks her. Her wet juice is covering your face, dripping on your chin."

    you "Hmmm..."

    homura "Oooh... That was so good... Let me return the favor."

    show bg homura_69_5 at top with dissolve

    play sound s_sucking

    "In spite of the situation, Homura doesn't miss a beat. She immediately takes your cock deep in her mouth."

    homura "Nggh, Ngh..."

    "You find yourself moving your hips in sync with her blowjob, hitting the sides of her mouth. She sucks hard on your shaft."

    homura "Ngggh... Hmmm..."

    "Not really thinking straight, you find yourself licking the juice from her gaping pussy again."

    "Her clit is very sensitive now, so you take care to tease it softly. She still reacts with moans of pleasure."

    play sound s_moans_quiet

    homura "Ohhh... Hmmm..."

    "Determined to make you cum, she goes faster and faster, taking your cock deeper inside her mouth."

    "Feeling close to your limit, you lose all control, sucking on her clit as you finger her, rubbing the inner walls of her pussy."

    homura "S-Shtop, if you do that..."

    show bg homura_69_4 at top with dissolve

    homura "AAAAAH!!!!" with vpunch

    show bg homura_69_6 at top with doubleflash

    "Your cock pops out of her mouth and she cums again, trembling, as you let it all out on her face."

    "*spurt* *spurt*" with flash

    "She squeezes your cock in her small hand without thinking, making you cum every last drop on her erotic face."

    "Her love juice is all over your face."

    homura "So intense... Ahhh..."

    if first:
        scene black with fade
        show expression brothel.master_bedroom.get_pic() at top
        with dissolve

        show homura naked with dissolve

        homura "So this is what a '69' is, uh? That was so fun..."

        you "Is it your first time doing this?"

        "She blushes."

        homura "S-Sure... I have experience, but not that much..."

        homura "I like this, though. Let's do it again some time."

        you "Of course... And there are many more things I could show you!"

        homura "Oh..."

        $ MC.change_prestige(3)

    return

label homura_cowgirl(first=True):

    scene black with fade

    if first:
        show bg homura_naked1 at top with dissolve

        homura naked "So... Are we going to have sex?"

        you "Of course... If you want to."

        homura "I do! But this time... I'll be on top!"

    "Homura pushes you back with surprising strength, and straddles across you."

    show bg homura_cowgirl1 at top with dissolve

    homura naked "Now, where is my big boy... Oh!"

    "Guiding your cock to the entrance of her slit with one hand, she puts your hands on her breasts with the other."

    homura "Here. Touch me!"

    "You start rubbing her nipples and gently cupping her tits."

    homura "Play with them harder! Don't hold back!"

    you "You're so forward today..."

    homura "Shut up... And get to it! *blush*"

    with vpunch

    play sound s_moans_quiet

    "Obeying her command, you knead her tits harder while she lowers herself on your cock."

    homura "Oh! It's so deep... It hurts..."

    you "Slow down..."

    homura "It's... Aw... Fine..."

    "Your cock slowly finds its way inside her tight pussy, and you briefly pause to let her adjust to the feeling."

    you "You okay?"

    homura "S-Sure. You can move now..."

    "Sure enough, as you start carefully moving your hips, you feel the wetness of her love juice begin to ease your cock in and out."

    homura "Hmmm..."

    "Homura closes her eyes and concentrates on the feeling of your cock inside her, and your hands playing with her tits and nipples."

    homura "Oooh..."

    "Unconsciously, she starts to move her hips in sync with yours. Soon, your dick is making sloppy noises as it repeatedly slides in and out of her pussy."

    "Turning your attention to her boobs, you again notice how well-shaped they are for such a petite girl. She hasn't got an ounce of fat on her, but her breasts are really something."

    homura "W-What are you looking at?"

    you "Your tits. They're just the right size for my hands... I love them."

    "You give her a good squeeze as you say that."

    show bg homura_cowgirl2 at top with dissolve

    homura "Haaa!!!"

    "Visibly turned on, she increases the pace of her hip movements furiously."

    "You lay back and let her do most of the work, enjoying the view, and the feeling of her pussy gripping you tighter and tighter."

    homura "It's going deep... Deep..."

    "You can feel your cock hitting her womb every time it slams deep inside. Her love juice is splashing on your crotch now."

    homura "I'm... I'm close..."

    you "Me too... Ohh..."

    if calendar.day > 18:
        homura "Today is a safe day... Let it all in!"

    else:
        homura "Today is dangerous... Please do it outside..."

    "As she says that, she grips you even tighter, driving you crazy. You feel the surge as you bounce her up one more time."

    menu:
        you "OHHH..."

        "Cum inside":
            with flash

            homura "Aaaah!!!"

            show bg homura_cowgirl3 at top with dissolve

            "*spurt* *spurt*"

            "You cum hard inside her, filling her pussy to the brim with warm semen."

            if calendar.day <= 18:
                homura "You stupid idiot! I told you today wasn't a safe day!!!"
                $ NPC_homura.love -= 2

                "She's really mad."

                homura "And now I'll have to get herbs from the alchemist, and feel sick for two days... Ugh!"

            else:
                homura "I can feel it! Aaaah! Aaah!!!"

                with flash

                "You feel the walls of her pussy pulsating around you as she has an orgasm of her own."

                homura "I came... Ohh..."

        "Cum outside":
            with flash

            you "Uhhhh!!!"

            show bg homura_cowgirl4 at top with dissolve

            "Taking your cock out just in time, you bust your load all over her white belly."

            homura "Oh my... Look at this... It's all over my breasts..."

            with flash

            "You look at her body appreciatively, dripping with your sticky cum."

            if calendar.day > 18:
                homura "I told you to cum inside, though... Why didn't you?"

                "She looks cross with you."

                $ NPC_homura.love -= 0.5

            else:
                homura "You came outside, like I said. You're a good boy... Hmmm..."

                "She kisses you deeply."

    if first:
        $ MC.change_prestige(3)

    return

label homura_river(first=True):

    scene black with fade

    play music m_nature fadein 3.0

    if first:
        show bg clearing at top with dissolve

        show homura with dissolve

        homura "Aaah... The forest. I love it here..."

        you "Aren't we straying too far from the city?"

        homura "Don't be silly. I come here all the time. I know those woods like the back of my hand."

        you "That's strange for a noble girl. I thought your father was keeping you locked up?"

        homura "He only {i}tries{/i} to keep me locked up. And you've seen how successful he is."

        homura "I've always liked walking in nature. I've got fond memories of these woods. I even..."

        play sound s_sigh

        homura "*sigh*"

        you "What was that?"

        homura "Oh, nothing. Come, there's something I want to show you."

        you "..."

    scene black with fade

    show bg farm outside at top with dissolve

    if first:

        homura "Look! Pretty, isn't it?"

        menu:
            extend ""

            "Amazing":
                you "Wonderful! This place feels out of time..."

                homura "Right? I come here every chance I get."

                homura "I'm happy I get to share it with someone, for once..."

                $ NPC_homura.love += 1

            "It's alright":
                you "Yeah, it's fine, I guess."

                homura surprise "You guess? Come on! It's great, admit it!"

            "I've seen better":
                you "Well, it's nothing compared to this waterfall in the Arik Mountains. I hear it falls from a mile high..."

                homura sad "Aw, do you have to spoil this moment? I took you here for us to be together..."

                $ NPC_homura.love -= 1

        you "It's nice. Homura, we..."

        play sound s_dress

        you "Homura?"

    play sound s_splash
    with vpunch

    homura naked "Woohoo!!!"

    show bg homura_water1 at top with dissolve

    if first:

        homura "Aaaah, it's so good!"

        you "Homura... Really? There could be people around, you know... That farmhouse..."

        homura "Oh, don't be so prudish! I never saw anyone here. Come, join me!"

        you "Are you sure? I feel like we're being watched, and, err..."

        play sound s_laugh

        homura "You worry too much!"

    homura "Come, the water's good!"

    play sound s_dress

    show bg homura_water2 at top with dissolve

    "Taking off your clothes, you waddle in the water. It is not deep, and you feel a strange tingling sensation being naked in the open."

    if first:

        homura "Take that! Teeheehee!"

        play sound s_splash

        "Homura throws water at you like a child, and you answer in kind."

        play sound s_laugh

        "At some point, your assaults drive her right under the waterfall."

        play sound2 s_splash
        pause 0.2
        play sound s_surprise

        homura "Uwaaah!!!" with vpunch

    show bg homura_water3 at top with dissolve

    if first:

        homura "Look what you've done! Because of you, I'm all wet now..."

        you "Well... That wouldn't be a first."

        homura "Y-You silly... *blush*"

    "Watching her standing naked in the water, her skin glistening in the sun, you cannot help but get hard."

    "Homura also cannot help but notice. She motions for you to move closer."

    homura "Come on, give me a rub."

    if first:

        you "A rub... On your back?"

        homura "Yes, on my back, silly! I feel tense. I need to unwind."

        you "I don't know... Don't you think it's time to go?"

        show bg homura_water4 at top with dissolve

        homura "No it's not! Don't spoil the mood now, give me a massage!"

        you "Well..."

    "As she braces herself against a rock wall, you start massaging her shoulders, slowly moving down to her back."

    show bg homura_water1 at top with dissolve

    homura "Oh, that's the spot... More... Do it stronger..."

    "You keep massaging her back, helping relax her muscles."

    if first:

        you "You're awfully tense for someone who lives at court..."

        show bg homura_water2 at top with dissolve

        homura "Well, I do try to keep in shape... Plus climbing down my Dad's palace walls isn't exactly a picnic."

        you "I believe you, you've got the body of an athlete, and... Uh?" with hpunch

    show bg homura_water5 at top with dissolve

    "Homura bends over backwards, touching your cock with her buttcheeks."

    homura "My, look at that... It's hard as a rock, already."

    you "Well, massaging cute naked women does that to a man..."

    homura "Hmmm... I think I'm in the mood for more than a massage..."

    "She keeps brushing against your cock. You see some wetness on her slit that is definitely not water."

    "She holds her breath as you move behind her, bringing your cock up to the entrance of her pussy."

    homura "Do... Do me, [MC.name]..."

    show bg homura_water6 at top with dissolve

    play sound s_aah

    homura "Aaaah!" with hpunch

    "Pushing back against the wall, she makes your cock enter her tight pussy as you grab her from behind."

    homura "Oh, it's coming in!" with hpunch

    "She starts moaning erotically, moving her hips back and forth."

    play sound s_moans

    homura "I can feel you..."

    "You let her do the work for a while, as her pussy loosens and welcomes your dick deeper in."

    homura "C-Come on... Don't leave me hanging..."

    homura "Aaaah! [emo_heart]" with hpunch

    "Deciding to join in the fun, you start responding by slamming your cock inside with every thrust. You both start getting into a rythm."

    show bg homura_water7 at top with dissolve

    homura "Oh yes... Aaaah!" with hpunch

    "Her love juices are flowing now, and she forgets herself as she moves to impale herself on your hard cock."

    homura "Oh yes! F-Fuck me harder!" with hpunch

    you "What did you just say? My, is this really Lady Henso I am speaking to?"

    homura "S-Shut up... Aaaah!!! [emo_heart]" with hpunch

    you "You know, we are out here in the open, where anyone could see us, fucking like wild animals in the river..."

    "Your words only seem to turn her on, and you can feel her body tensing up as she pushes against you with her strong thighs."

    homura "Oh... Aaah... Aaaah..." with hpunch

    "Her pussy walls close in on you, squeezing your dick hard as you hit the entrance of her womb."

    homura "I'm... Ohhh... I'm..." with hpunch

    play sound s_scream
    show bg homura_water8 at top with flash

    homura "CUMIIIIIING!!!!" with hpunch

    play sound s_orgasm_young
    with doubleflash

    "You both cum hard under the waterfall."

    with flash

    "Your cum inside her, then spurt some out on her pretty white ass. Water from the waterfall washes a mix of cum and love juice down her thighs."

    homura "Aaaah... It was so good... My head is spinning..."

    "You give her a gentle rub from behind. You stay inside her for a moment, then she reluctantly lets you go."

    show bg homura_water5 at top with dissolve

    you "The sun is getting low. We have to get back now..."

    homura "Aw... I was in the mood for more..."

    you "Next time..."

    # 2 bath in waterfall hpy bck to MC + 1blsh + (1pout) + 1p bend + 2x dgy + 1cin/cob

    if first:
        you "Uh?"

        "You could swear you saw something move in the bushes. Something... Colorful?"

        you "Hmm... Was that pink hair?"

        $ MC.change_prestige(3)

    return

label homura_anal(first=True):

    scene black with fade

    if first:
        show bg homura_naked1 at top with dissolve

        homura naked "So... How do we do this? *nervous*"

        you "Relax... We're going to take it slow."

        homura "I don't... Normally do this kind of things, you know..."

        you "What do you mean? I can remember doing a lot of kinky stuff with you."

        show bg homura_naked2 at top with dissolve

        play sound s_surprise
        homura "S-Stop it! You know what I mean. I don't normally do... What we're about to do."

        you "Are you saying this is your first time?"

        show bg homura_naked3 at top with dissolve

        homura "I'm saying... Yes. Yes, this is my first time."

        you "Wow... I'm a lucky man, then."

        homura "I don't know about that..."

        you "Come here."

        "You move over on the bed and kiss her. She closes her eyes..."

        scene black with fade

    show bg homura_anal1 at top with dissolve # ask msg (x+a) 1p/sham

    if first:
        homura "What... What are you doing?"

    "As you spread her legs open, Homura almost goes in a panic."

    homura "Aaaah..."

    "She is already visibly wet, though. You can tell whe was waiting in anticipation for what comes next."

    you "Rushing into it won't do. Let me help ease you up a little."

    play sound s_sucking

    "Going down between her thighs, you start licking her clit, her pussy lips, all the way down to her asshole. She moans uncontrollably."

    homura "Oh nooooo... What are you doing to me..."

    you "Well, you seem to like it... *lick*"

    "Her love juices are running thick, now, and she shivers under your tongue."

    "She gasps as you introduce a finger inside her ass."

    play sound s_surprise

    homura "Aaah!!! Don't..."

    you "Just relax, dear. If you can't take a finger, you won't be able to handle what comes next."

    play sound s_moans_quiet

    "She clenches her teeth and endures, as you start massaging her asshole from the inside."

    "While pushing your tongue inside her wet slit to tease her, you eagerly suck on her erect clit."

    homura "What's this... I've never felt like this... Ohhhh..."

    you "Is this too much for you already?"

    if first:
        homura "No, but..."

        "She looks at you with intensity."

        homura "[MC.name]... Fuck me please."

        you "Now? I don't think you are ready..."

        homura "My pussy. Now!!!" with vpunch

        show bg homura_anal2 at top with dissolve # ask msg (x+a) 1x

        "Not daring to disobey, you move your cock between her legs, easily slipping it inside her wet, gaping pussy."

        homura "Oh yes!!! Oh..."

        "Your warm-up technique has really put her in the mood, and she welcomes you deeper inside her as she lifts her hips to give you a better angle."

        homura "It's so good... I feel dizzy..."

        you "You like it?"

        homura "Yes... Do it, harder!" with vpunch

        "There is nothing lady-like about the horny girl before you, begging you for a good fuck. This puts you in a playful mood."

        you "My my, dear honorable Lady Henso, are you saying you want me to fuck you like a slut?" with vpunch

        "She seems turned on by the dirty talk."

        homura "I'm bad... I'm a bad girl... I need to be punished for what I've done..." with vpunch

        you "Very well..."

        "With that angle, it's very easy to pile down on her and drive your cock all the way in."

        homura "Oh, aah, AAAH!!!" with vpunch

        "She moans and gasps as you pound her mercilessly."

        you "You like this, Homura? Do you like to be fucked like a vulgar streetgirl?"

        homura "That's... All... I deserve... Fuck me harder! Fill me up with dirty cum!" with vpunch

        "This little game is a big turn-on for the both of you, and you quickly reach your limits."

        you "I can't hold it any longer..." with vpunch

        homura "Me neither... I'm... I'm..."

        show bg homura_anal3 at top with flash # ask msg (x+a) 1cin/cob(on nos)

        you "UWAH!" with vpunch

        play sound s_orgasm_fast
        with doubleflash

        homura "CUMIIIIIING!!!"

        with flash

        "You shoot a massive load of cum all over her body, and she reaches orgasm at exactly the same time."

        homura "Oh... I came like crazy..."

        you "Me too..."

        homura "I'm all sticky... You even got some on my face!"

        "You both start laughing."

        with fade

        homura "You're still hard..."

        you "You got me incredibly turned on... We are not finished."

        homura "Right... I made a promise..."

        "The nervousness is back in her voice, but her body is now a lot more relaxed."

        "Bringing your cock up to her asshole, you use a mix of cum and her own love juice to lubricate the entrance."

        homura "It's dirty..."

        you "It's not, don't worry..."

    else:
        homura "No... I can take it..."

        "Not missing a bit, you slip a second finger inside her asshole, having lubricated it with her love juice."

        homura "Aaaah..."

        "Her ass is more loose now than when you first fucked her, and she has learnt to relax her body. Soon, you are able to slip a third finger inside."

        homura "Oh, aaah, ah!"

        you "You are getting nicely wet... Does having fingers up your butt turn you on?"

        homura "S-Stop it... *blush*"

        "Her weak denying tells you all you need to know. Still licking her slit, you play with her ass from the inside."

        homura "E-Enough... I'm... I'm ready..."

        you "Great..."

        "Your cock has been rock-hard for a while. You bring it up to her ass."

        homura "I-It's big..."

        you "Yes, but don't worry... We already know it will fit."

    "Spitting in her crack, you use your cock to push some saliva inside her. Her asshole is becoming loose."

    you "Shall we?"

    play sound s_mmh
    homura "Hmmm... Yes..."

    show bg homura_anal4 at top with dissolve # ask msg (x+a) 1a

    play sound s_scream

    homura "AAAAH!" with vpunch

    if first:
        "Being fucked in the ass for the first time, she is very sensitive. You stop mid-way to give her a chance to recover."

        you "Are you alright?"

        play sound s_ahaa

        homura "Aaah... I-I feel strange... But I can handle it..."

    "Your cock seems massively too big for her little asshole, but you slowly push it in."

    play sound s_moans

    homura "AH, AAAH, AHAAA!" with vpunch

    you "Try to relax. Your body will adjust in a moment."

    homura "Aaaah..."

    "She seems almost ready to faint, hiding her face as you start slowly fucking her ass. Still, she nods at you to continue."

    "You use one hand to rub her clit and pussy, getting more love juice down on your cock."

    play sound s_aah

    homura "Ah, aah!" with vpunch

    "The familiar stimulation of her lower regions helps drive Homura's attention away from the cock in her ass. She eases up a little."

    homura "Oh, hmmm..."

    if first:
        you "This will feel weird at first, but you will learn to love it in time."

        homura "..."

        homura "Teach me."

    "You bend forward to kiss her. You keep stimulating her body, and moving in and out of her asshole becomes easier."

    homura "Aah, Ohh, Ohhh!!!" with vpunch

    "Little by little, you increase your pace. Her asshole looks more and more dilated, but is adjusting nicely."

    homura "Oh... I'm making love with my butt... I can't believe I'm doing this..." with vpunch

    "It looks like she is geeting in the mood. She's now peeking at the place where both of your bodies connect."

    homura "I, aah... Can't believe... This huge thing is... In my butt..." with vpunch

    "You are moving at a good pace now, still rubbing and pinching her clit as you pound her butthole."

    play sound s_scream

    homura "Oh, ah, aah..." with vpunch

    "Concentrating on the feeling, she hugs you close. You can feel her body tensing up."

    homura "Ohh... Ohhh..." with vpunch

    if first:
        "Fucking her virgin ass and watching her cute reaction becomes too much for you. You can't help but reach your limit."

        you "OHH..."

    show bg homura_anal5 at top with flash # 1cin

    play sound s_screams

    homura "AAAH!!!" with vpunch

    with doubleflash

    "You mind goes blank as you shoot your load right into her asshole. She is surprised at the feeling of warm cum erupting inside her."

    with flash

    if first:

        play sound s_sexy_sigh
        homura "Oh no... Doing it in the butt... I'm so depraved..."

        you "Hmm... But didn't you enjoy it?"

        homura "I... I did... I was close to cuming again..."

        homura "I think it's true that I'm a dirty slut, I can't deny it."

        you "Who said that? I was only joking..."

        homura "It's not you, it's... Never mind."

        "She hugs you close, kissing your mouth passionately."

        $ MC.change_prestige(3)

    else:
        play sound s_orgasm_young
        homura "AAAAH!!!" with vpunch

        "She cums as soon as you unload, burying her fingers in your back."

        homura "I came... From my butt... Aaaah..."

        you "You did... I'm proud of you..."

        homura "Hahaha... Don't be..."

    return


## Narika story line ##

label c3_narika_MU_visit():

    $ renpy.block_rollback()

    play music m_magicu fadein 3.0

    scene black with fade
    show bg magicU at top with dissolve:
        yalign 0.0

    $ renpy.pause(0.25, hard=True)

    show bg magicU at top with dissolve:
        linear 1.25 yalign 1.0

    $ renpy.pause(1.25, hard=True)

    if story_flags["MU seen intro"]:
        show receptionist with dissolve

        "You returned to the Magic University to register as a student."

        call c3_narika_MU_pay_fee() from _call_c3_narika_MU_pay_fee
        return

    show sill with dissolve

    sill "Wow! So this is the Magic University, the highlight of the Magic Guild quarter, renowned around Xeros as a place of deep knowledge and wondrous experimentation!"

    sill "I'm so honored and excited to be here!"

    sill "Right, Master? Master?"

    you "Hmmm... Most of the students and faculty are chicks, and they're hot as fuck..."

    hide sill
    show bg magicU_students at top with dissolve

    "Professor" "So now that we've successfully neutralized the undead, let's dissect it to see how it works..."

    "Students" "Yay!!!"

    you "Hot chicks... *drool*"

    show bg magicU at top:
        yalign 1.0
    show sill
    with dissolve

    sill "Ew, necromancy? Are they even allowed to do that?!?"

    "Girl voice" "Of course. Our charter with the city is very clear that what happens at Magic University, stays at Magic University."

    show sill at right with move
    show receptionist at totheleft with dissolve

    you "Oh, really? And who are might you be?"

    receptionist "I'm the P.R. representative for Magic University."

    sill "P.R. representative? Never heard of that before. What does it entail?"

    play sound s_sigh

    receptionist "It means I have to deal with people from the outside... *sigh* Most mages can't be bothered handling the profane."

    receptionist "So I handle the reception of outsiders, register students, file complaints from their families... I even operate the gift shop."

    receptionist "And answer questions from busybodies, of course."

    sill sad "Oh..."

    receptionist "I was informed by the Dean that an agent of the Court was visiting, so I came to greet you."

    receptionist "It's.. What was it again? Ah, yes: Nice to meet you."

    "Her voice sounds completely indifferent. She doesn't sound at all like she means it."

    you "Who told you we worked for the Court? We're not here on any kind of official business... "

    receptionist "Official, unofficial, it's all the same to the Guild really."

    receptionist "Mages welcome the Crown's scrutiny. Provided it remains in line with our Charter, of course."

    receptionist "Now, I assume you have questions, so please ask them... So that you be on your way and tend to whatever important paperwork you have to fill in."

    you "How helpful..."

    label MU_questions_menu():

        menu:
            "Tell me more about you":

                you "So... You're the public face of the University, so to speak?"

                receptionist "Nothing that fancy. It's just that I am more of a people person than most mages."

                "She looks bored and unexpressive."

                you "(If you're the people person, I wonder what the others are like...)"

                receptionist "Also, it's a sad fact that I am quite hopeless at working spells. Can't even cast a minor fireball."

                receptionist "So our Dean, Masou-sama, figured I would be better suited to this task."

                you "Wait, didn't you say you were a mage?"

                receptionist "Oh, I am."

                sill "You're a trained mage but you don't know magic???" with vpunch

                receptionist "I {i}know{/i} magic, sort of, I mean I've read the textbooks... I'm just not good at wielding it."

                "She sighs deeply."

                receptionist "Look, if you must know, my father is a high Lord from the nearby country. He paid a hefty sum for me to study here."

                receptionist "As I'm not really fit for the mundane world, I've been content to stay here for the past five years. Eventually, I'll figure it out... Maybe."

                you "Five years and no progress? Why does the University even keep you?"

                "She looks puzzled by your question."

                receptionist "Why, my dad pays a hefty tuition, of course!"

                receptionist "Did you seriously think a prestigious institution like ours operated on merit?"

                sill "Unbelieveable..."

                you "So you got, err, promoted to handling strangers, is that it?"

                receptionist "Yeah. Like I said, it suits me. Studying for more than an hour at a time gives me headaches."

                receptionist "Most days no one shows up. Other times, just some rich parents trying to offload their useless kid."
                
                sill "(Is she speaking about herself?)"

                receptionist "I handle the families an application form to fill, cash their tuition fee, and then they leave quickly."

                receptionist "I wish most days were that easy..."

                "She looks at you two reproachfully."

                jump MU_questions_menu

            "Tell me about the university":

                you "I want to know more about the Magic University. What do you do here?"

                play sound s_sigh

                receptionist "*sigh*"

                receptionist "The Magic University, or MagicU as it is known, was created a little over 90 years ago by our current Dean, Masou-sama, who was at that time the top ranking graduate of Karkyr university."

                you "(Over 90 years ago, uh? That Dean's an old-timer.)"

                receptionist "The Dean proceeded to make MagicU one of the most elite institution in Xeros."

                receptionist "Our faculty is top tier, and our facilities are second to none. Our students can enjoy living here full-time with high-class amenities and focus on their training."

                receptionist "Here at MagicU, we strive to teach them all possible schools of magic at the highest level, even some of the more unorthodox topics such as necromancy, demonology, and card tricks."

                receptionist "We also encourage our graduates and faculty to advance the magic arts by engaging in cutting research. Sometimes the research {i}actually{/i} cuts. And bites. And claws."

                receptionist "In short, MagicU is the best place for a gentle-man or woman to learn magic in a comfortable and magic-friendly environment. We give even the elite schools in Karkyr a run for their mana."

                "During her whole pitch, her voice has remained as cold and bored as ever."

                receptionist "Would you like to know more? Perhaps I can interest you in a brochure, or some books about the history of our prestigious establishment?"

                you "Err, not really..."

                receptionist "*not listening* Here, let's me look for the right chronicle..."

                play sound s_spell
                show receptionist glasses with flash

                receptionist "Here, this one is an abridged version, just shy of 2,000 pages long."

                sill normal "Whoah! Your glasses just materialized out of thin air!" with vpunch

                receptionist "Of course. I am farsighted, so I need my glasses to read books..."

                sill "So you do know some magic, after all!"

                play sound s_sigh

                receptionist "*looking annoyed* I don't. It's the glasses that are magic."

                you "Magic glasses?"

                receptionist "Naturally. Among the fruits of our research, we have developped a large number of magical prosthetics, from the mundane such as these to the miraculous."

                sill "Really?"

                receptionist "Some of our magic artifacts can replace limbs, cure ailments and infirmities..."

                receptionist "And even prop up the impotent. But if you need help in that department, I'm afraid our most powerful items are under magical lock and key in the University's vault."

                you "N-No, I don't..."

                receptionist "Sure, sure. They all say that."

                play sound s_spell
                show receptionist with flash

                sill "(Magic glasses, hmm?)"

                jump MU_questions_menu

            "Why did you call me a Court agent?":

                receptionist "Look, I don't care what business you have with the Court, and which faction you're working for."

                receptionist "The Dean said you'd come, and you came, so this much was right."

                you "Did the Dean mention us specifically? You could have mistaken us with someone else..."

                $ desc = {"Warrior": "A big dullard with a large sword, battered armor and a vacant stare, displaying the grace and sense of a drunken troll.",
                            "Wizard": "A snooty know-it-all in a tattered robe adorned with rough patches and stains of questionable origin. You will struggle and fail not to roll your eyes at him when he speaks.",
                            "Trader": "A shifty scoundrel with the subtlety of a horny alley cat, more likely to break into drunken slumber than into a vault full of gold."
                            }[MC.playerclass]

                receptionist "No, she mentioned you precisely. '[desc]' He is followed by a pink-haired slave girl who smells of cleaning products."

                receptionist "That describes you, doesn't it?"

                you "It does not!"

                sill "It kind of does..."

                play sound s_punch

                sill sad "*OUCH*" with vpunch

                receptionist "Don't be naive. The Dean likes to keep informed of what goes on at Court, just like your people spy on our affairs."

                receptionist "The Charter doesn't prohibit that, as long as it remains within reason."

                receptionist "No doubt the Dean knows more about your mission, but I don't need to know."

                receptionist "Which is a good thing too, because Gods know I wouldn't care."

                jump MU_questions_menu

            "What is this charter you speak of?":

                receptionist "*sigh* You don't know that? Maybe it's true that you're not a Court agent after all..."

                receptionist "The Charter is the treaty that recognizes the Magic Guild's fealty to the Pharo dynasty, and thus covers MagicU as well."

                sill happy "I seem to recall there was some friction at the beginning of the King's reign..."

                receptionist "Not really. It's just that the Guild has lived through four different dynasties since it settled in Zan, and one Republic."

                receptionist "The Pharo dynasty began on shaky ground, twenty-five years ago."

                receptionist "So the mages withheld their approval of the new king until a satisfactory deal was reached."

                receptionist "Some at Court are still bitter about this, but if you ask me, they're fools."

                you "For the record, I didn't ask."

                sill "What does the Charter say?"

                receptionist "Well, it gives us perpetual lease on this part of the city, not just the University grounds but the whole Magic Guild's district."

                receptionist "We can arrange our own affairs, and the Crown can only intervene if we request it. Their troops and agents like yourselves are barred from entering Guild and University buildings without invitation. We also do not pay royal taxes."

                you "I can see why that would rub some folks at the Palace the wrong way."

                receptionist "Some think the King got a raw deal. But he was able to consolidate his power in the end, so all is well that ends well, right?"

                receptionist "The problem is more with the personal animosity the King has developped for magic users."

                you "Personal?"

                receptionist "Yup. That the King actively hates mages is famous all over Zan."

                receptionist "Only a few magic-users are allowed at Court, such as the Astronomer Lord Henso, and they have cut ties with our Guild a long time ago."

                sill sad "Has somebody in the Guild wronged King Pharo in any way?"

                receptionist "I suppose this has to do with one assassination plot or another. Or the Dean's refusal to participate in the war effort. Meaningless politics. *shrug*"

                receptionist "If you ask me, a King should have thicker skin than that, and not get upset over some petty squabble."

                you "Again, I didn't ask..."

                receptionist "Anyway, we're quite content with the King avoiding us if it means we stay out of each other's business."

                receptionist "As the Charter would have us."

                jump MU_questions_menu

            "Tell me about the students":
                you "So you said you handle student registration?"

                receptionist "Unfortunately, I do."

                sill "You must have lots of students from the nobility within your ranks."

                receptionist "Of course. Our students only come from the elite layers of society, as they should."

                you "Even from within the Royal family?"

                "She gives you a strange look."

                receptionist "Of course not, why do you even ask?"

                you "Uh? Why not?"

                receptionist "Because King Pharo forbids it, of course."

                sill "He does?"

                receptionist "Yes. Some grudge he has against mages, in spite of the Charter we signed twenty-five years ago."

                you "Anyway, do you know a girl student that fits this description?"

                receptionist "I like to think I'm able to forget someone's face as soon as they leave the registration office. It is a skill I have refined over many years."

                sill sad "(Is this really a skill, though?)"

                "You proceed to describe Narika in as much detail as possible."

                receptionist "A spolied, whiny kid? That describes {i}all of the students{/i} we get at the University."

                you "But do you remember her?"

                receptionist "I don't. Just like I hope I'll have forgotten all about you by the time you step out of here."

                you "Wow, you really have a way with people. I can see why they made you the P.R. representative..."

                receptionist "Thanks."

                "She doesn't even seem to register your sarcasm."

                jump MU_questions_menu

            "Tell me about the Dean":
                you "So your Dean sounds like an interesting character..."

                receptionist "Sure thing. Masou-sama is over a century old, and has lead the Guild and the University for nearly as long."

                receptionist "She was a prodigy, a once-in-a-generation phenomenon. Graduated Karkyr at only fifteen."

                you "So the Dean is a 'she'?"

                receptionist "Sure. But don't get any ideas. She's many planes of existence out of your league, and anyway, she's celibate. Her only interest is devoting herself to magic."

                you "Haha, you're deluded, I'm not going to fall for some old crone. Not my kink."

                sill "What does Masou-sama do, exactly?"

                receptionist "Well, on the one hand, she's the Dean here so she keeps the faculty and researchers under control, which is no small thing. I don't think there's a higher concentration of inflated egos anywhere else in Xeros."

                receptionist "On the other hand, as she is also the Guild's Grandmaster, she has to handle a whole lot of politics. I understand she loathes that, but someone has to do it."

                receptionist "She has precious little time for anything else, including her magical research. This is in spite of using several alternate timelines to multiply her output."

                you "Can we meet her?"

                receptionist "Oh, sure. Did you miss the part where I said her time is precious and shouldn't be wasted?"

                you "It is important. We come with an urgent warning."

                receptionist "What's so urgent that you must disturb..."

                receptionist "Oh, blast, it's not like I'm paid, well, anything to stop you, so go right ahead."

                receptionist "She's better at dealing with your type than I am, anyway."

                you "'My' type?"

                sill "(Come Master, let's not waste this chance to talk to the Dean...)"

                play sound s_thunder

                with flash

                "The receptionist fumbles with something inside her pouch and a shimering blue portal fizzles into existence next to you."

                receptionist "Here you go. I'll see you on your way out."

                receptionist "(Shouldn't be long...)"

                call c3_narika_dean_visit from _call_c3_narika_dean_visit

                show bg magicU at top with flash:
                    yalign 1.0

                show receptionist with dissolve

                receptionist "So you're back. Yay."

                receptionist "That was an exceptionally long interview. The Dean must like you."

                you "Yeah, not really."

                receptionist "Oh? Well, don't worry about it. She doesn't like anybody."

                receptionist "What did she say?"

                "She's asking out of boredom rather than genuine interest."

                sill "Well, she told us that we shouldn't ever..."

                you "*interrupting* That we shouldn't ever worry about a thing!"

                you "She said we're welcome to investigate at our leisure. She'll cover for us by giving you fake instructions, because our mission is so secret than you can't know about it, you see."

                receptionist "..."

                "She stares at you blankly for a few seconds."

                receptionist "Fine, what do I care."

                you "So, can we visit the University now?"

                receptionist "Absolutely not."

                you "Whaaaat?" with vpunch

                receptionist "Only students and faculty are allowed on school grounds. Certainly not Crown agents."

                you "I assure you, I am not a Crown agent."

                receptionist "Maybe, but you're not a student either."

                you "Can I register to be a student, then?"

                receptionist "No! I mean, you..."

                "She struggles to find a reason to deny your request for some time. You can see from the deep frown on her face that she isn't coming up with anything."

                receptionist "Do you even have any magical affinity?"

                if MC.playerclass == "Wizard" or MC.spirit >= 5:

                    if MC.playerclass == "Wizard":

                        you "Of course! I'm a trained wizard. I'm far above your puny level."

                        receptionist "You don't have to rub it in my face..."

                    else:
                        you "Well, I'm no wizard, but I trained quite a few spells in my days. I'm able to handle the entry class, at least."

                        receptionist "Ok, fine, I guess I can register you for "

                    receptionist "Fine, I can register you for a class, but you need to pay the tuition."

                    you "And how much is that?"

                    receptionist "Oh, the usual rate is 10,000 denars per year. But since you're from outside of the Upper City, that would be 15,000."

                    you "WHAAAAT??? That's crazy!" with vpunch

                    receptionist "Hmph, as I thought, you don't have the means to study here..."

                    you "I don't need a year of classes anyway... Don't you have anything... Cheaper?"

                    receptionist "Well, I guess I can sign you up for a seven-day trial."

                    you "How much is that?"

                    $ price = story_flags["magicU price"] = 750

                    receptionist "That would be [price] gold."

                else:

                    you "Well, not really, but..."

                    "She looks relieved."

                    receptionist "Here you are, then! You can't get in."

                    you "Wait a moment... You don't have any magical ability either!"

                    receptionist "I do! Sort of..."

                    you "Your dad just paid your way in, didn't he?"

                    receptionist "Hmph, yes, but I don't suppose you have his kind of wealth..."

                    you "Come one, we can make a deal. I just need access to the University for a short time."

                    receptionist "Well..."

                    you "I'll pay cash, of course. Directly to you. No need for any paperwork..."

                    receptionist "You're going to get me in trouble..."

                    receptionist "..."

                    receptionist "Fine, 1,500 denars, and you get access to the University for a week."

                    you "1,500 denars? That's steep!"

                    call challenge("bluff", 4) from _call_challenge_67

                    if _return:
                        receptionist "Hmph, fine, 1,000 denars then. But it's final."

                        $ price = story_flags["magicU price"] = 1000

                    else:
                        receptionist "Take it or leave it, pinchpenny."

                        $ price = story_flags["magicU price"] = 1500

                you "[price] gold for two weeks, uh..."

                call c3_narika_MU_pay_fee() from _call_c3_narika_MU_pay_fee_1

                $ story_flags["MU seen intro"] = True

    return

label c3_narika_MU_pay_fee():

    $ price = story_flags["magicU price"]

    receptionist "[price] gold, and you get in for seven class days. What do you say?"

    if MC.gold < price:
        you "I don't have the money right now."

        receptionist "Yeah, I didn't think you did."

    else:

        menu:
            "Yes":
                $ MC.change_gold(-price)
                $ NPC_narika.flags["c3 path"] = "MagicU"
                $ story_flags["ninja hunt locked %s" % get_ninja_district(NPC_narika)] = True
                $ renpy.block_rollback()

                you "Fine, here you are."

                "The girl swiftly grabs the pouch of gold, conspicuously hiding it in her bosom rather than stowing it in the registration desk."

                call receive_item(MU_entry_scroll, use_article=False) from _call_receive_item_15

                receptionist "Good, I'll give you a registration scroll valid for a week."

                receptionist "The school is open every day, so you can start coming tomorrow."

                you "The scroll doesn't mention my name... It's for one 'Lord Fakelot McFakeface'?"

                receptionist "Is it now? Well, think of it as insurance, in case the Dean looks at the student record."

                receptionist "If she found out I let you in, you might get caught, and {i}I{/i} may get in trouble."

                receptionist "I don't care about you turning into a slug, but I don't want to be yelled at."

                scene black with fade

                "You will attend school every weekday for the next week."

                $ story_flags["MU class days"] = 0
                $ story_add_event("c3_narika_MU_class", "daily")
                return

            "No":
                you "I still need to think it over."

                receptionist "Oh, fine, just waste more of my time then."

    scene black with fade

    "Talk to {b}suzume{/b} to go back to the University once you have the funds."

    return

label c3_narika_dean_visit():

    play sound s_mystery
    scene black with fade
    scene bg magic_office with doubleflash

    "You step into the portal and suddenly find yourself inside a fancy office, filled with various old tomes and magical oddities."

    you "So, this is the Dean's office..."

    show shizuka with dissolve

    shizuka "Yes? What is it?"

    you "(Oh, good, her assistant.)"

    you "Hello there young lady. Could you fetch your mistress please? I have urgent business with her."

    shizuka "Uh? My mistress?"

    you "Sure, sure, now go, shoo. Bring me the old lady."

    sill sad "Master..."

    you "Stop interrupting, Sill."
    
    "The young woman doesn't move, looking at you, amused."
    
    you "Gee, still here? Come one, I haven't got all day! Go tell the Dean I'm here!"

    sill "But Master..."

    you "What is it with the help these days? Shut up, Sill. You're in over your head."

    shizuka "Ahem."

    you "What?"

    shizuka "The Dean..."

    $ interject = {"Arios": "Arios", "Shalia": "Shalia", None: "Daemons"}[MC.god]

    you "Yes, go get her, isn't that what I asked for? ([interject], that assistant is cute, but not very bright...)"

    you "Or is that Dean so senile she can't even bring her old bones to the office anymore?"

    sill "Master! This woman! She {i}is{/i} the Dean!" with vpunch

    shizuka "*nods* I {i}am{/i} the Dean."

    you "You {i}are{/i} the Dean? Oh, very funny. Everyone knows the Dean is a decrepit crone who's over a century old."

    sill "Master, you're making it worse..."

    $ shizuka_name = "静香院长"

    shizuka "Your slave has more sense than you. You barge into my office and start calling out a lady about her age?"

    shizuka "I have half a mind to send you on a one-way trip to an Eldritch dimension right now."

    you "Wait, you're really the Dean?" with vpunch

    shizuka "Of course I am. I'm one of the Master Mages from Karkyr, and you think I couldn't overcome something as petty as aging?"

    you "Ah, err, hem, I'm sorry my lady, I didn't know... *mumble*"

    shizuka "So you're an idiot on top of being a sexual harasser. Charming."

    you "I'm sorry, what? A sexual harasser?"

    shizuka "Of course! Remember that time you tried to sneak naked into my room?"

    you "Uh? I never... Sill?"

    sill "Err, sorry Master, I don't know what she's talking about either..."

    shizuka "Wait, was that in the past, or in the future?"

    shizuka "I'm following too many different timelines at once, I might have gotten them confused."

    shizuka "Demons, there's just too much work these days. My mind wanders."

    you "..."

    shizuka "Yeah, yeah, we'll see how you handle things when you're my age. A decrepit crone, you said? Ha!"

    you "S-Sorry, we got off on the wrong foot here. I've come to warn you about imminent danger to your institution."

    shizuka "But of course. I am really {i}moved{/i} by the Court's concern for our safety."

    you "Look, I don't work for the Court... I mean I do, but, it's not the reason I'm here... I mean it is, but..."

    shizuka "He blabbers again... *sigh*"

    shizuka "Look, this is all terribly entertaining, I have never seen a Crown agent embarrass himself that much in so little time, but I have a thousand other things to do before the day is over."

    you "Wait! I don't think you realize the danger you're in. A trained assassin is after something valuable at the University, and they'll stop at nothing to get it."

    shizuka "Are they now? And what is this valuable thing they're after?"

    you "I... Have no idea, yet, but I was hoping..."

    play sound s_laugh

    shizuka "You {i}are{/i} clueless, aren't you?"

    shizuka "Look, we get attempted break-ins all the time, and our defensive measures are top-notch."

    shizuka "No one in their right mind wants to face our magical traps. I have a jar full of slugs in the back who used to be burglars."

    shizuka "They provide me with a source of slime, and the students with entertainment during study breaks, gambling on slug races."

    you "But listen. The attacker is a Kunoichi, a prodigy with natural resistance to magic. She could take on your defenses, I'm sure."

    shizuka "Hmph. I designed most of those traps myself, so I strongly doubt that."

    shizuka "Now, let me lay down the rules."

    shizuka "This meeting is over, and you are not to bother me ever again. I will give that airhead receptionist clearer instructions this time."

    shizuka "If I find out you are causing trouble at my quiet little private institution, you will soon join my slug collection."

    shizuka "Do I make myself clear?"

    you "Well yeah, but..."

    shizuka "Good."

    play sound s_spell
    scene black with flash

    "She snaps her fingers, and the room goes blank."

    return

label c3_narika_failed_summon():
    play sound s_scream_loud

    ev_girl2 "Nooooo!!!" with vpunch

    play sound s_tentacle
    show bg MU_monster2 at top with dissolve

    "Not content with fondling her, the monster pushes his pulsating red cock into her panties, burying the fabric in her pussy."

    ev_girl2 "Stop... I summoned thee... Thou shalt obey me..."

    play sound s_scream

    ev_girl2 "Aaaaah!" with vpunch

    play sound s_tentacle

    show bg MU_monster3 at top with dissolve

    "Ignoring her feeble attempts at regaining control, the demon pushes his cock harder and harder until her panties give way."

    "*RIP*" with vpunch

    "In an instant, the large demon cock fills her pussy, all the way to her womb."

    play sound s_screams

    ev_girl2 "No, no, let me go, aahaaah!" with vpunch

    "The girl screams, unable to take the feeling of the demon fucking her raw."

    play sound s_roar

    pause 0.3

    play sound2 s_tentacle

    "With a sickening gooey sound, the tentacles agglutinate into a monstrous shape, still probing at the poor girl's holes"

    ev_girl2 "Nooo-"

    show bg MU_monster4 at top with dissolve

    play sound s_mystery

    ev_girl2 "Hmmmh!!!" with vpunch

    play sound s_sucking

    "Shutting her up with another one of his tentacle cocks, the demon lets out an outworldly groan."

    ev_girl2 "Nggh... Ngh..." with vpunch

    "The beast is fucking her in rythm, now, and she seems to have lost any will to fight back."

    ev_girl2 "Hmmh... Nggh!" with vpunch

    "Her body is like a broken doll, bouncing on demonic dicks with obscene wet sounds."

    play sound s_mmh

    ev_girl2 "Hmmmh..."

    "The demon's tentacles begin to swell, apparently gorging with unholy semen. It seems it is about to shoot its load inside the hapless girl."

    play sound s_roar

    "*GROAR*" with vpunch

    show bg MU_monster5 at top with flash

    "Suddenly, thick monstrous cum beetween to erupt at both ends of the demon' dicks, shooting inside her mouth and pussy."

    with doubleflash

    ev_girl2 "Ngh, nggh, ngggggggh!!!"

    show bg MU_monster6 at top with flash

    "The girl can't do anything but take it all in, almost losing her mind as her womb fills up with wad after wad of demonic cum."

    play sound s_evil_laugh

    "Beaming with an unholy glow, the demon seems to bask into the mess it's made."

    return

label c3_narika_MU_class():


    play music m_magicu fadein 3.0

    if not story_flags["MU class days"]:
        $ story_flags["MU class days"] = 0
    $ story_flags["MU class days"] += 1

    if debug_mode:
        $ story_flags["MU class days"] = int(renpy.input("Choose day number"))

    $ renpy.block_rollback()

    scene black with fade
    show bg magicU at top with dissolve:
        yalign 0.0

    $ renpy.pause(0.25, hard=True)

    show bg magicU at top:
        linear 1.25 yalign 1.0


    if story_flags["MU class days"] == 1: # Day 1 - Sill intro

        you "Finally here! Magic University, here I come!"

        "???" "Wait, wait! *pant*..."

        you "Uh? Who's this?"

        play sound s_steps
        show sill glasses at totheright with easeinright

        "???" "Oh... I finally caught up with you!"

        you "I'm sorry, your face looks kind of familiar, but... Have we met?"

        $ sill_name = "似曾相识的女孩"

        sill "Master! It's me!"

        you "*squint*"

        you "*{b}squint harder{/b}*"

        sill "Master!"

        you "Sill! Is that you?"

        $ sill_name = "希露"

        sill "Of course it's me! Gee, Master, is my disguise really so effective?"

        you "It's... Mesmerizing."

        sill "It's the glasses! Seeing that receptionist girl conjuring up her glasses yesterday made me think of this trick..."

        you "Really? Take them off just for a second?"

        sill "Okay..."

        show sill glasses:
            zoom 1.0
            yalign 1.0
            ease 0.5 zoom 1.75 yanchor 0.5

        pause 0.5

        play sound s_spell
        show sill happy with dissolve:
            zoom 1.0
            yalign 1.0

        sill "Like that?"

        you "Amazing. It's  like a completely different person."

        play sound2 s_spell
        show sill glasses with dissolve:
            zoom 1.75
            yanchor 0.5
            pause 0.5
            ease 0.5 zoom 1.0 yalign 1.0

        you "What about your registration scroll?"

        sill "I forged one from using yours. I simply had to cast..."

        you "Not interested, forget I asked."

        sill "Hehe, this way I can accompany you to class, Master [MC.name]!"

        sill "(Oh, my heart is beating fast! It's like we're two highschool sweethearts who just...)"

        you "Good idea, let's split up, we'll cover more ground that way."

        sill "B-But..."

        sill "(Oh no...)"

        sill "(Well, at least I will get to do something other than housework.)"

        you "Move it, Sill, we ain't got all day! Let's see, you can go there... Your next class is... 'Cleaning up magical equipment 101'."

        sill "Aargh..." with vpunch

        scene black with fade

        if MC.playerclass == "Wizard":
            you "Phew, I almost died of boredom in there... I had forgotten how much non-Euclydian geometry and linguistics of the Great old ones you need to cram before you can summon a simple eldritch hamster."

        else:
            you "I have a pain in my neck from nodding to the teacher even though I didn't understand a single word."

        you "More importantly, I didn't catch a single glimpse of our target... It's harder than I thought. This place is huge."

        show bg magicU at top with dissolve:
            yalign 1.0

        show sill glasses with dissolve

        sill glasses "Master! Finally, I am done... *pant*"

        sill "They made us clean up the whole magic lab, this wasn't really like a class at all... And I..."

        you "Nice, nice, good to know you were having fun, but what about that pesky ninja?"

        sill "I didn't see her anywhere..."

        you "[MC.swear()], we'll have to look harder tomorrow..."

        show bg magicU at top with dissolve:
            yalign 1.0
            matrixcolor SaturationMatrix(0.4)

        "A large shadow suddenly glides over you."

        show bg floating island at top with dissolve:
            matrixcolor None

        you "UWAAAAH!!! What the fuck is THAT???" with vpunch

        you "Sill! There's a, there's a..."

        sill "A floating island?"

        you "Yes!" with vpunch

        sill "Did you just notice it? It's been floating around ever since we came here."

        you "I was so focused on keeping my ear to the ground looking for Narika that I didn't even notice..."

        sill "They call it the Sky Isle, and it's been here in Zan forever. It seems to always hang high above the Magic University."

        sill "Although I heard it was already floating around long before they built the University. It seems to be attracted to places of power."

        you "What's up there?"

        sill "No one knows. Oddly, teleportation spells won't work on it and the terrible wind up there does not allow flying."

        sill "Some say it's a piece of the legendary Goliath Kingdom, ripped apart in the cataclysm that destroyed that land..."

        you "Yeah well, I'm sure it's just a big dumb piece of rock that happen to defy the laws of physics. Let's not get sidetracked and focus on the important stuff. Which is..."

        you "That I'm STARVING!!! It's almost dinner time, and you need to get to the kitchen fast!" with vpunch

        sill "Oww... *panic*"

    elif story_flags["MU class days"] == 2: # Day 2 - Sill H

        you "(Day Two of infiltrating the university...)"

        you "(I better get a lead on this girl ninja today, no time to screw around.)"

        show sill glasses at totheright with easeinright

        sill "Wait for meeee!!!"

        you "What, you're coming along today too?"

        sill "Of course! It's been my dream to go back to studying..."

        you "You're weird... No one likes studying. At least I didn't, so that means no one does, right?"

        sill "I'm so excited! After doing the chores yesterday I stayed up all night to study my old textbooks."

        sill "I need to dust off some of what I learned in the past, and..."

        scene black with flashbackout
        sill glasses "(...and see if I could still figure out how to cast that old enchant...)"

        show bg sill sold at sepia
        with flashbackin

        sill glasses "(...the one I used when I met Master [MC.name]...)"

        hide bg
        show bg sill sold
        with flashbackin

        sill past "Oh no, what's going to happen to me???"

        sill "My life is over... Father wants to sell me off to some stranger at the slavemarket..."

        sill "All these men are giving me dirty looks... They're old and disgusting... Everywhere I look, I just feel sick..."

        you "Hello Sir, is this horse for sale?"

        play sound s_surprise

        sill "!!!" with vpunch

        sill "(This man, talking to my father! He's...)"
        
        sill "(He's actually quite dashing!)"

        $ MC.rand_say(["wa: My old one got his head blown off by a trebuchet. Nasty business.", "tr: My old one got hurt playing with my pet dragon. Turns out horse hair is surprisingly flammable.", "wi: I lost my old one. Turns out you can't dry a horse using a microwave spell. Who would have thought?"])

        sill "(In fact... He's really handsome... Just looking at him gives me strange tingling sensations all over...)"

        you "May I look it in the mouth? Let's see..."

        sill "(If I'm going to be a slave to anyone, this man...)" with vpunch

        you "Oh, would you look at that! There's a girl next to the horse."

        sill "(He saw me!!!)"

        you "She's cute actually. Is she also for sale?"

        sill "(And he said I'm cute!!! [emo_heart])" with vpunch

        "Sill's father starts bartering with [MC.name]."
        
        sill "(Quick, Sill, get your act together!)"

        sill "(Find that enchantment! The one you were saving for your one true love...)"

        sill "(This enchantment will make anyone fall for me. It has to work... Arios, please!)"

        you "Ouch, man, that's steep. But you know what, throw in the girl and I'll take the horse. It's all the coin I've got, but she's my type. Here you go."

        play sound s_gold

        sill "(I can't believe it! He bought me! The enchantment worked!)"

        $ MC.rand_say(["gd: Hi there, cutie. Don't be afraid. I'm [MC.name].", "ne: Hello. I'm your new master. My name is [MC.name].", "ev: Get up, slave. You're mine now, and don't you forget it. The name's [MC.name]."])

        sill "H-Hello Master..."

        sill "Master [MC.name]..."

        scene black
        show bg magicU at top:
            yalign 1.0
        show sill glasses:
            xalign 0.5
            ypos 1.15
            yanchor 1.0
        with flashbackout

        play sound s_ahaa

        sill "Master [MC.name]... Aaah... [emo_heart]"

        you "Yes, that's my name... Why are you swooning like a fool?"

        sill "Oh, erm, sorry. How are you today, Master [MC.name]? *blush*"

        sill "(I was hard at work all night on these enchanted glasses...)"

        sill "(If I got the spell right, it should rekindle the flame between Master and me...)"

        you "What are you acting so strange?"

        sill "Have you noticed anything today, Master? Anything at all?"

        you "Nope."

        show sill glasses:
            ease 1.0 ypos 1.5 zoom 1.5 subpixel True

        "Sill get closer."

        sill "But look! What about my glasses? Do you like them?"

        you "They're okay, I guess. Why are you acting all weird?"

        show sill glasses:
            ease 1.0 ypos 2.25 zoom 2.5 subpixel True

        "Sill gets even closer."

        sill "How about now? *blush*"

        you "*look*"

        you "*look intently*"

        show sill glasses:
            ease 1.0 ypos 1.5 zoom 1.5 subpixel True

        you "(Is it me, or is it getting hot all of a sudden?)"

        you "You know... You know what they say about girls in glasses, right?"

        sill "That they're... Really smart?"

        you "Nope."

        stop music fadeout 3.0

        scene black with fade
        show bg sill glasses1 with dissolve

        play music m_suzume fadein 3.0

        "Grabbing Sill's hand, you pull her into the bushes and swiftly pull her clothing out of the way."

        play sound s_mmh

        sill glasses "Oh, Master! [emo_heart]" with vpunch

        you "No underwear, uh? That's my Sill..."

        sill "(Whoah... Looks like my enchantment worked a little too well...)"

        show bg sill glasses2 with dissolve

        sill "Master! We're in public! What are you doing..."

        you "I know we're in public! That's why you're already wet, isn't it?"

        "You stick two fingers inside her pussy, and they immediately become sticky with thick juice."

        play sound s_aaah

        sill "Aaah!" with vpunch

        sill "But anyone could see us... The faculty... The students..."

        you "That's part of the fun!"

        "Pulling out your hard cock, you place it right between her pussy lips, enjoying her moistness on the tip or your manhood."

        show bg sill glasses3 with dissolve

        stop music fadeout 3.0
        play sound s_surprise

        sill "No, Master, wait!" with vpunch

        you "What? You don't want me to fuck you senseless?"

        sill "It's... It's not that..."

        sill "But I need to know... Are you doing this to me because of my glasses?"

        you "Uh? What are you rambling on about?"

        sill "It's my glasses that turn you on, isn't it?"

        sill "(It's just because of the enchantment...)"

        you "..."

        you "Nonsense."

        "You remove her glasses and fling them to the side."

        sill naked "Uh? M-Master?"

        you "Glasses are just an accessory, I don't care about that."

        sill naked "Really?"

        "She looks at you with big, shiny puppy eyes."

        you "Of course, your true beauty is inside..."

        play sound s_sigh

        sill "Aw... Master... It's so nice of you to say so... [emo_heart]"

        you "...inside that tight pussy of yours! Let's FUCK!" with vpunch

        play sound s_scream

        sill "Aaaah!!!" with vpunch

        scene black with fade

        sill naked "(Master likes me even without the enchantment... I'm glad... [emo_heart])"

        sill "Wait, Master, wait!" with vpunch

        you "What, again? Your constant interruptions are going to ruin the mood, Sill..."

        sill "No, Master, don't get me wrong."

        sill "I want to make love. But let me be on top."

        you "Uh? What's gotten into you today?"

        show bg sill glasses4 with dissolve

        sill "Come on Master! I want to ride your dick!" with vpunch

        you "Whoah, you're wild today!"

        sill "(Master will be in love with me, I'm sure... I'm going to show him a good time!)"

        "Sill starts grinding her lower body against you, coating your shaft with her juice."

        you "We're laying down in the middle of the alley... Anyone could come..."

        sill "Like you said, it's part of the fun!"

        show bg sill glasses5 with dissolve

        play sound s_ahaa

        sill "Ahaaaah..." with vpunch

        "Sill lowers herself onto your cock, sliding it deep into her drenched pussy."

        play sound s_moans

        sill "Oh Master, you're so thick! Oh!"

        play sound s_moans

        "Sill starts rocking her hips, massaging your dick between the tight folds of her pussy."

        "She shakes her boobs at you, enjoying your gaze."

        show bg sill glasses6 with dissolve

        sill "Do you like it, Master? Aaaah! [emo_heart]" with vpunch

        you "Oh, you're squeezing me... Sill, your technique's got better..."

        sill "The girls have been giving me tips! Look, how's this?"

        show bg sill glasses7 with dissolve

        play sound s_dodge

        sill "Banzai!" with vpunch

        "Squeezing you tighter between her thighs, she buries your cock deeper inside her, increasing the sensations even further."

        you "Whoah! Amazing!" with vpunch

        play sound s_mmh

        sill "See, Master? I've gotten good, haven't I? Hmmmh..."

        "She keeps bouncing off your dick faster and faster, almost popping it out on the way up, only to impale herself on it all the way down."

        play sound s_aah

        sill "Ooh... Aaaaah..." with vpunch

        you "I can't... Ooooh..."

        show bg sill glasses8 with dissolve

        sill "You're close, aren't you? I know your body like the back of my hand, you know..."

        sill "Let me make you cum, Master [MC.name]. Let your slave fuck your brains out today..."

        sill "Hmmm, ooh, aaaah..." with vpunch

        "Sill keeps upping the pace, squeezing your dick with all her strength."

        show bg sill glasses9 with dissolve

        play sound s_scream

        sill "Aaaah!" with vpunch

        sill "Oh my, I'm so close too! Fuck me, Master! Fuck my dirty pussy!"

        "*squeeze*"

        play sound s_ahaa

        sill "You hear that, Master [MC.name]?"

        "Your bodies make dirty wet noises as Sill's juice splash around your crotch. You feel your orgasm building up inexorably."

        sill "That is the sound of inevitability."

        play sound s_scream_loud

        sill "AAAAAH!!!" with vpunch

        show bg sill glasses10 with flash

        "Suddenly, it all becomes too much for you. As Sill descends on your dick one last time, you shoot a huge load of cum straight at her womb."

        play sound s_aaah

        sill "Oh, you're so deep, oooh..." with doubleflash

        play sound s_orgasm_fast

        sill "I'm, I'm... AAAAAAAH!!!"

        with flash

        "Sill cums hard too, her hips arching back as she convulses in orgasm with your cock deep inside her."

        sill "It's so warm inside, aaaah..."

        show bg sill glasses11 with fade

        sill "See, Master [MC.name]? You're not so tough, after all, aren't you?"

        sill "Maybe {i}I{/i} can call the shots from now on... You could be {i}my{/i} slave, doing my bidding..."

        sill "In exchange, I'll let you be my {i}slave boyfriend{/i}."

        sill "Don't worry, I'd still fuck you every dqy, and after that you'll give me a nice massage, make some tea, then do the chores for me... Hehehehe...."

        you "Sill..."

        play sound s_laugh

        sill "Ho ho ho ho, I can already see it! 'Yes, Mistress Sill', 'Of course Mister sill', 'What part of your body needs relief, Mistress Sill?'..."

        you "Sill."

        sill "And then you'd get on your knees, and..."

        you "SILL!!!" with vpunch

        show bg sill glasses12 with dissolve

        "Sill suddenly snaps out of her revery."

        sill "Oh, uh, ah, s-s-sorry Master!!!"

        you "Are you quite finished?"

        sill "*mumbles incoherent excuses*"

        menu:
            "Humor her":
                $ MC.good += 1
                $ NPC_sill.love += 5

                "You soften your voice and smile."

                you "You know, perhaps we can do that one day. As {i}roleplaying{/i}."

                sill "R-Really? You'd do it? You're not... Mad at me, Master?"

                you "Mad at you? Of course not, we just had great sex. I like it when you're so forward."

                you "So maybe we'll do that again, eh? One day."

                sill "Oh, thank you, Master... [emo_heart]"

                you "But not anytime soon. First I need to recover from this."

                sill "O-Of course..."

            "Let it slide":
                $ MC.neutral += 1
                $ NPC_sill.love += 2

                "You roll your eyes."

                you "What nonsense was that?"

                sill "I-I'm sorry, I don't know what came over me, Master... It's that time of the month, maybe, and..."

                you  "Quit your babbling, Sill."

                you "I'll let your impertinence slide this once. After all, it's understandable in the heat of the moment."

                you "It {i}was{/i} a great fuck..."

                sill "T-Thank you, Master..."

                you "But don't let that get to your head, you hear? "

                sill "N-No, sorry Master. I'll be good."


            "Punish her":
                $ MC.evil += 1
                $ NPC_sill.love -= 2

                you "I don't think I heard you correctly. Did you call me... {i}Your slave{/i}?"

                sill "I-Im so sorry, Master... I was just..."

                you "[MC.swear()], you have the gall to tell me that, you impudent wench? I should have you flogged!"

                sill "No! Master [MC.name], nooo! I'm sorry, I'll never do it again!"

                you "I'll see to it that you will not! I'll give you double the chores this week, and you'll sleep on the kitchen floor!"

                sill "Aaw... I'm sorry, Master..."

        "Suddenly, you hear the laughs of a large group of students nearby."

        "You both become painfully self-conscious, lying naked and covered in bodily fluids in the middle of the alley."

        scene black with fade

        play sound s_dress

        "Hurryingly, you fix your clothes and head back towards the main building."

        play sound s_spell

        "As you walk back, you notice the time on the magic clock up on the main building's tower."

        sill glasses "Oh no! Classes are over already!"

        you "No way! We missed our chance to hunt the ninja because of your naughty shenanigans! *mad*"

        play sound s_punch

        sill "But, Master, it's you... Ouch!!!" with vpunch

        $ MC.change_prestige(3)

        "You didn't make any progress on the hunt for Narika today. Better luck tomorrow?"

    elif story_flags["MU class days"] == 3: # Day 3 - Narika glimpse

        you "Okay, today I locked Sill up in her room. No more interruptions, this time I'm going to find that pesky ninja!"

        you "Let's check a bunch of different classrooms. She's bound to be {i}somewhere{/i}."

        show black with fade

        "You spend the next hour poking your head into various classrooms."

        you "[MC.swear()], this place is so darn big... Wait, what's this one? 'Arcane items of Xeros: A long history.'"

        "You catch a whiff of sakura flower perfume as you peer into the classroom."

        scene black with fade
        show bg classroom at top with dissolve

        "Professor" "So, did you like the lecture, Miss?"

        show narika school with dissolve

        narika "Oh yes, Professor... You are {i}so{/i} interesting, you know... I come here every day just to hear {i}you{/i}..."

        "The girl bats her eyes exageratedly while the Professor basks in her adoration."

        "Professor" "It's so nice of you to say so, my child..."

        "The old teacher starts patting the girl on the lower back, inching his hand down to her skirt. She evades at the last moment in a swift elegant move, still managing to look natural."

        you "(This girl...)"

        narika "Professor [emo_heart], did you remember my request?"

        "Professor" "Child, it's not easy to sate your curiosity... I can't tell you such things, there are rules and the Dean would be very cross if she..."

        narika "Ow, Prof-chan, don't be a meanie... You do remember my promise, don't you?"

        "Professor" "You promised to... *gulp*"

        narika "Yes? *teasing*"

        "Professor" "To give me your used panties... If I..."

        narika "That's right! [emo_heart]"

        narika "But in exchange I just want you to share some knowledge... For my thesis... Pretty please?"

        "She bats her eyes so fast she almost gives the old guy a seizure."

        "Professor" "*sigh* All right, you're such a sweet girl, there's really no harm in that..."

        "Professor" "I know of the item you asked about. It's one fine piece of magic engineering, based on ancient Cimerian principles... They used mithril to..."

        narika "*growing impatient* Cut to the chase, old man, where is it?" with vpunch

        "The Professor stops, startled, Narika catches herself and immediately reverts to her schoolgirl act."

        narika "*in character* Pretty please, Prof-chan?"

        "Professor" "Well, uhm... It's here in the Dean's vault, the most secure place in the whole University. Building it was an early feat for the Dean and we keep it away from the public, as it is priceless."

        narika "Of course, of course... And this vault is completely unbreachable, isn't it?"

        "Professor" "Quite so! One would have to be a master at evading magical traps to even make it passt the entrance to the vault, but then..."

        narika "Yes? *eager*"

        "Professor" "There's a final piece of security that no thief could ever work around..."

        narika "What is it?" with vpunch

        "Professor" "It is, er... *lowers his voice*"

        "You can't quite make out what the Professor is saying. Narika raises an eyebrow."

        narika "Really? I see..."

        "Professor" "So, that's all I know about it. Now, will you give me my... present?"

        narika "You know what, I have to go now, but I'll drop by next week and I'll give it to you for sure!"

        play sound s_steps
        hide narika with easeoutright

        "Professor" "Wait, young lady! I-"

        "Professor" "She's gone..."

        scene black with fade

        "You ponder what you just saw."

        you "She's definitely out to get a magical item from the Vault."

        you "It's not quite enough information to unravel her plan yet. I need to keep investigating."

    elif story_flags["MU class days"] == 4: # Day 4 - Monster H

        "You are back to Magic U. today, again touring the different classrooms looking for Narika."

        you "Day Four already. I only have one week. I need to make progress."

        "You hear some yelling coming from one of the halls."

        "Professor Emeritus" "Search again, damnit! It must be around somewhere! Masou will have my hide if she finds out I lost it!"

        "You catch a glimpse of half a dozen servants running around the vast and expensive lab, before one of them spots you and slams the door shut."

        "Intrigued, you keep exploring, when you suddenly hear something."

        play sound s_surprise
        ev_girl2 "Oh no! Help!" with vpunch

        "The cry comes from one of the student rooms."

        scene black with fade
        show bg MU_monster1 at top with dissolve

        play sound s_scream

        ev_girl2 "Aaaah!!!" with vpunch

        ev_girl2 "I completely messed up the magic formula... The Demon is not obeying any of my orders!"

        "You peek inside the room and see a student in the middle of a sticky situation."

        menu:
            "What do you do?"

            "Help her":
                $ MC.good += 1

                # Challenge
                $ chal = renpy.call_screen("challenge_menu", challenges=[("Attack", "fight", selected_district.rank), ("Dispell", "control", selected_district.rank)])

                if chal == "fight":
                    $ norollback()

                    play sound s_sheath

                    "Unsheathing your weapon, you leap inside the room and starts hacking at the creature."

                elif chal == "control":
                    $ norollback()

                    "Stepping inside the room, you try to think fast and figure out the demon's type and weakness before it can fully take form in the material world."

                play sound s_scream_loud
                ev_girl2 "Eeek!!! Help me!" with vpunch

                call challenge(chal, 3) from _call_challenge_68 # result is stored in the _return variable
                $ r = _return

                if r:
                    if chal == "fight":
                        play sound s_sheath
                        pause 0.3
                        play sound2 s_sheath
                        with flash

                        "You slice off most of the monster's appendages."

                        play sound s_roar

                        "With a roar of pain, the demon withdraws and his body shines briefly before disappearing into thin air."

                    elif chal == "control":
                        you "POYE POLOMI!!!" with vpunch

                        play sound s_lightning
                        with flash
                        "Your fingers blast arcane lightning at the thing, searing his mind through the interdimensional veil. The creature withdraws in pain."

                        play sound s_roar

                    ev_girl2 "Oh, thank you so much!"

                    ev_girl2 "It's gone back to where it came from, it didn't have time to fully materialize!"

                    scene black with fade

                    "The girl is really grateful. She gives you something for your trouble."

                    $ MC.change_prestige(3)
                    call receive_item(item_dict["Lucky charm"]) from _call_receive_item_26

                else:
                    play sound s_roar

                    "The creature notices you, and a wrigling mass of tentacles spurts towards you."

                    "You fall back in disgust, trying to fence off the attacks as best as you can."

                    play sound s_punch

                    you "OUCH!!!" with vpunch

                    "Alas, you hit your head hard on a shelf, and a dozen large and heavy magic tomes rain down on you."

                    "You are knocked out; fortunately the beast is content with leaving you alone and focussing its attention back on the hapless girl."

                    call c3_narika_failed_summon() from _call_c3_narika_failed_summon

                    scene black with fade

                    "When you come back to your senses, the demon and the girl are nowhere to be seen."

                    "Defeated, you head back home, with your stamina spent and a nasty headache."

                    $ MC.interactions -= MC.interactions

            "Just watch":
                $ MC.evil += 1
                you "(I shouldn't get involved, but I'll keep an eye on it. You know, just in case...)"

                call c3_narika_failed_summon() from _call_c3_narika_failed_summon_1

                scene black with fade

                "Once the beast is sated, it goes into a half-asleep state. The girl finally begins to stir and motions to free herself."

                "You decide not to stick around and retreat before anyone sees you."

    elif story_flags["MU class days"] == 5: # Day 5 - Shizuka run-in
        you "Today is the fifth day of class... This time I will find that little minx."

        show sill glasses with dissolve

        sill "Master... You're sure about this?"

        you "Yes. Today, I will check the Dean's floor. Narika's probably been snooping around Shizuka's office."

        if MC.playerclass == "Wizard":
            play sound s_spell

            "You cast a discretion spell on yourself. You'll try poking your nose inside the dean's office to see if there is anything fishy."

        else:
            you "Your magic will help me. You have studied that discretion spell all night, as I commanded you?"

            sill "Yes... I didn't get any sleep... *sob*"

            you "Good, good. What are you waiting for? Cast it!"

            play sound s_spell

            "Sill does her best to shield your aura from magic detection."

        sill "B-But Master, Masou-sama is an archmage... Surely she won't be tricked by a simple sneak spell?"

        play sound s_punch

        sill "Ow!" with vpunch

        $ MC.rand_say("wi: Nonsense, do you doubt the extent of my magical abilities?", "Stop whining! If you did your job correctly, I'll have nothing to worry about.")

        you "Now, let's see what that sexy old lady has to hide..."

        scene black with fade
        show bg magic_office at top with dissolve

        you "No one seems to be here... Good, let's look around."

        "Being careful not to touch anything that could trigger a magic trap, you explore the room."

        "It seems no mage can ever resist filling their office with scores of gizmos, potions and dusty old tomes."

        "Nevertheless, for a mage's office, the Dean's is a lot more orderly than what you are used to."

        you "Nothing here seems really noteworthy..."

        "Suddenly, you catch a whiff of a familiar smell... Sakura flowers."

        you "Wait! That's Narika's smell... She has been here not so long ago."

        "Following the faint smell, you reach a large cabinet at the back of the room, and stop dead in your tracks. Something is off, after all."

        you "Well well well... There's a safe inside the cabinet, and it's been busted open. Took a fair bit of skill, from the look of it."

        "You don't doubt there was one or more magic wards protecting it, but they were bypassed. The safe sits empty, its door dangling open."

        you "Someone's just been here. It must have been our little friend. But what did she take?"

        "You turn to the last place you didn't check, an ornate door in the back of the room."

        you "Maybe I'll check this place next..."

        "You risk a quick peek through a crack in the door."

        stop music fadeout 3.0

        show bg shizuka bed1 at top with dissolve

        you "*gulp*"

        "Shizuka is lying on her bed, only wearing a simple white blouse with light blue panties."

        you "(Whoah, nice butt... That anti-aging spell sure works wonders...)"

        play sound s_sigh

        shizuka "Uh? Who's there?" with vpunch

        "You freeze in your steps. Shizuka has noticed you, from the other side of the door!"

        you "(Oh, shit...)"

        shizuka "It's faint, but I can feel your presence, student. I must admit that skulking spell of yours is surprisingly good."

        shizuka "But if you know what's good for you, you will leave my office this instant. Don't make me come out of here and report you."

        "Being in the other room, it seems she believes that you are merely a nosy student. You should definitely make a run for it."

        shizuka "I'll give you to the count of three to get the heck out of here. Unless you want to spend the rest of the month eating flies as a toadling..."

        menu:
            "What do you do?"

            "Join her in bed":
                $ renpy.block_rollback()
                $ NPC_narika.flags["c3 path"] = None
                $ story_flags["ninja hunt locked %s" % get_ninja_district(NPC_narika)] = False
                $ NPC_narika.flags["magicu failed"] = True

                you "(Obviously, she's joking. She looks lonely all by herself. She clearly needs a man.)"

                you "(Otherwise, why would she lay here, half-naked and vulnerable, while there's an intruder in her office?)"

                play sound s_dress

                you "(It's time to show her a good time...) *unzip*"

                scene black with fade

                you "Here I come, Deany baby! Daddy's home~~~"

                play sound s_thunder

                show bg shizuka bed2 with flash

                "*ZAP*"

                play sound s_wscream

                you "AAAAARGH!!!" with vpunch

                "As soon as you enter the room, a massive bolt of lightning hits you right in the dick. Shizuka did not so much as move a muscle."

                "You fall flat on your face, as the smell of grilled pork fills the air."

                shizuka "Oh, it's you? I knew you were a pervert."

                you "*sizzle*"

                shizuka "You have overstepped your bounds, royal agent. I'll have you thrown out immediately, and make sure spells are in place so that you will not come back."

                play sound s_spell
                scene black with flash

                "*snap*"

                $ MC.interactions -= MC.interactions
                $ story_remove_event("c3_narika_MU_class", "daily")
                call remove_item(MU_entry_scroll, use_article=False) from _call_remove_item_4

                "When you recover from the shock, you are lying in the gutter outside the University's walls, with your pants all but burnt out to a crisp. The walk home puts your sneaking abilities through a hell of a test."

                you "I can't show my face again at the University until things cool off... I'll need to find another way to get to Narika."

            "Get the hell out":
                play sound s_steps
                scene black with fade
                show bg palace corridor

                "You don't need to be told twice, and you take off before she has a chance to catch you."

                "As you turn around the corridor, you hear Shizuka's yell behind you."

                shizuka "WHO THE HELL MESSED WITH MY CABINET? COME BACK HERE, RIGHT THIS INSTANT!!!" with vpunch

                "You run down the stairs and exit through the back, doing your best to stay well hidden until you reach the safety of the outside district."

                scene black with fade

                you "Damn, that was close. What did Narika steal from the Dean, I wonder?"


    elif story_flags["MU class days"] == 6: # Day 6 - Wall H
        you "Okay, the week is almost over... I need to find out what Narika is up to."

        show bg palace corridor2 at top with dissolve

        "You decide to try your luck in a section of the school you haven't yet explored."

        you "I think I've been to almost every class by now... Where could she be..."

        play sound s_steps

        "Suddenly, you hear fast footsteps coming from around the corner."

        you "Uh?"

        play sound s_crash

        "*BUMP*" with vpunch

        play sound s_surprise

        "???" "Hey, watch it!!!"

        "Someone running fast around the bend of the corridor slammed right into you, making you both fall to the ground."

        "You try to grab onto something for balance, but it turns out to be something squishy."

        play sound s_scream

        "Girl" "Eeek! It's my butt, you pervert!" with vpunch

        "You let go, getting ready to apologize."

        you "Err, erm, I'm sorry, Miss..."

        show narika school with dissolve

        narika "..."

        you "..."

        "Both at the same time" "It's YOU!!!" with vpunch

        play sound s_steps

        hide narika with easeoutleft

        "Narika immediately bolts in the opposite direction."

        you "Come back here! I need to talk to you!" with vpunch

        play sound s_shatter

        "Not listening, Narika leaps right through a window."

        you "It's the third floor! [MC.swear()]..."

        "Running to the window, you take a look outside. The girl has landed in a bush, and is already back up, running away at full speed."

        you "Damn, I'll never be able to catch her..."

        "Looking back down the hall, you notice a door gaping open in the corridor where she came from."

        you "She looked like she was in a hurry to leave... Let's see what she was running from."

        stop music fadeout 3.0

        scene black with fade

        play sound s_scream

        "Woman's voice" "Help me! Help!!!" with vpunch

        show bg MU_wall1 at top with dissolve

        you "Uh? What's going on here?"

        "It takes a little bit of time for you to process what your eyes are seeing."

        "It's a woman's butt, protruding out of a cement wall."

        you "What the..."

        play sound s_surprise

        "Woman's voice" "Is there anyone here? Help!" with vpunch

        show bg MU_wall2 at top with dissolve

        "The voice is coming from the other side of the wall."

        you "What... Who are you? what happened?"

        "Woman's voice" "I'm Professor Suza, I-I teach the teleporting class..."

        you "You {i}teach{/i} teleporting? Is that how you ended up here?"

        "Suza" "No, it's not that! I was a victim of a student prank..."

        "Suza" "It's that girl! She's trouble, I should have known something was off when she failed to cast the simplest telekinesy spell..."

        "Suza" "She wooed some of the boy students and convinced them to help her carry out this prank."
        
        "Suza" "They used a magic scroll to teleport me into the wall, and now I'm stuck here! I can't move, and I can't cast spells with my hands blocked!"

        you "Well, I guess it's a good thing the wall gave in instead of you..."

        "Suza" "This is no jape, Sir! That girl, she stole my... The..."

        you "Your what?"

        "Suza" "I-I can't say... But that's besides the point! Can you please help me?"

        you "Hmmm..."

        menu:
            extend ""

            "Help her":
                $ MC.good += 1

                you "Well, here, let me help you..."

                scene black with fade

                "With great effort, you manage to get the teacher unstuck."

                "Suza" "Thank you so much, Sir!"

                you "You're welcome."

                "Suza" "Now, to catch that little minx..."

                "You take a look inside the classroom. Drawers are dangling open, obviously someone has gone through them all while the teacher was incapacitated."

                you "It's risky to blow her cover like that in front of a teacher... To be so bold, she must be getting close to her goal."

            "Tease her":
                $ MC.good -= 1
                you "First, I would like you to tell me what it is she took from you."

                "Suza" "Uh? I'm sorry, Sir, it's confidential school information."

                you "Oh, really?"

                "Suza" "I hope you understand, I can't..."

                play sound s_dress

                "Suza" "Sir, what are you doing? Sir?"

                play sound s_scream

                show bg MU_wall3 at top with dissolve

                "In one fell swoop, you remove her pants. You start teasing her private parts with a piece of chalk."

                play sound s_scream_loud

                "Suza" "Sir, no, it feels ticklish! What's going on???"

                you "You know, we can play a game to jog your memory."

                "Suza" "I-I don't understand... Let me go..."

                you "I'm going to keep teasing you on this side of the wall... Until you tell me what that girl took from you."

                "You start tugging at her panties."

                play sound s_scream_loud

                "Suza" "Aaaah!!!" with vpunch

                "Suza" "It's not something important, I swear! You shouldn't concern yourself with this..."

                you "I guess I do feel concerned."

                play sound s_dress

                "You pull harder on her panties, rubbing the piece of chalk against her sensitive clit."

                play sound s_screams

                "Suza" "Aaaah, aah, aaaah!!!" with vpunch

                you "Oh, whoah, look at that! The teacher is getting wet."

                "You rub your palm against her crotch, feeling her moistness through her panties."

                "Suza" "N-no! Stop it already!" with vpunch

                you "Tell you what, if you don't tell me soon, I will consider this an invitation to fuck you..."

                "You start pulling her panties out of the way."

                play sound s_scream

                "Suza" "No! S-Stop! I will tell you, just stop it!"

                "You pause for an instant, giving her a little time to collect herself."

                "Suza" "Fine, fine, Arios, please stop this!"

                "Suza" "She took the key..."

                you "What key?"

                "Suza" "The archmage's key. The one Masou-sama gave me for safekeeping."

                you "What is this key for?"

                "Suza" "I-I just know I need to hang on to it. Masou-sama can't find out, or I will be fired!"

                you "Fired? That doesn't sound so bad..."

                "Suza" "Out of a glass cannon! Into hellfire!"

                you "Oh. And what does that key do?"

                "Suza" "It's one of the key to the vault... Oh, I'm in so much trouble..."

                you "The vault? One of the keys?"

                "Suza" "That alone won't open the vault, thank Arios..."

                "Suza" "Will you let me go now?"

                menu:
                    extend ""

                    "Yes":
                        you "Sure. Or rather, someone else will. Just hang in there, I'll tell the janitor on my way out."

                        "Suza" "H-Hey! Come back!" with vpunch

                    "No":
                        $ MC.evil += 3

                        you "I don't think so. We really only got started on the fun part."

                        "Suza" "S-Sir!!! Please stop this jest right away..."

                        play sound s_dress

                        show bg MU_wall4 at top with dissolve

                        play sound s_surprise

                        "Suza" "S-Something's touching me down here!"

                        "Suza" "Is it your... Finger?"

                        you "Nope."

                        "Suza" "Don't tell me it's your d-"

                        play sound s_scream_loud

                        show bg MU_wall5 at top with hpunch

                        "Suza" "Eeeek!!!"

                        "Pushing your hips forward, you enter her all in one go."

                        play sound s_ahaa

                        "Suza" "Ahaaa!"

                        "Although Suza's pussy is wet enough, she was ill-prepared to take your whole length."

                        "You enjoy the feeling of her snug pussy struggling to accomodate your cock."

                        you "Hang in there, teach'. This will get easier in a moment."

                        "Suza" "D-Don't move... I..."

                        play sound s_scream

                        "Suza" "Aaaah!" with hpunch

                        "Unable to resist, you start moving your hips, slowly at first."

                        play sound s_moans

                        "Suza" "Oh, ah, aaah..." with hpunch

                        "She moans softly as you fuck her, unable to gather her wits and keep talking."

                        "Her body is placed at a perfect angle for you thanks to the wall holding her. You put your hands behind your head, thrusting deeper inside her."

                        play sound s_aah

                        "Suza" "Aaaah! Oh, aah... [emo_heart]" with hpunch

                        "You can feel it's getting easier to move inside her now."

                        "Your balls are hitting her crotch with every move, making a lewd slapping sound."

                        "Suza" "N-No..."

                        you "Are you feeling this, teach'? I'm getting close."

                        play sound s_ahaa

                        "Suza" "N-No... Don't do it inside..."

                        play sound s_moans

                        "Suza" "Aaah, aaaaah, aaaaah!"

                        "With her legs spread wide, she can't move at all."

                        "You sink your fingers in the flesh of her ass, pulling her towards you."

                        "Suza" "I can't take any more... Ngh... Aaaaah!!!"

                        with flash

                        "Jamming your dick inside her up to the hilt, you cum in torrents, filling her womb with your semen."

                        play sound s_screams

                        "Suza" "Nooooo!!! Aaaah!!!!" with doubleflash

                        show bg MU_wall6 at top with flash

                        "Taking your cock out, you take a satisfied look at Suza, your cum flowing out of her pussy."

                        you "Well, that was fun. You'd better clean up before the next class starts..."

                        you "Oh, that's right, I forgot... You're stuck! Well, I'm sure the students will help you out. Muhahahaha..."

                "You leave, having found out new information about Narika's plan."


    elif story_flags["MU class days"] == 7: # Day 7 - Confrontation w/ Narika
        "The final day of class has arrived. It is time to confront Narika."

        you "I stayed up all night poring over plans of the school and the locations of my run-ins with Narika..."

        you "Today I am going to find her. And then we'll put an end to this!"

        scene black with fade
        show bg palace corridor at top with dissolve

        you "I am going to stand around this corner. If my calculations are correct, she is bound to go through here at least once today."

        you "Now let's wait..."

        with fade

        you "..."

        you "(Damn... I've been standing here for over an hour, and she isn't anywhere to be seen.)"

        "Groups of students pass you by, chatting and laughing, but you see no trace of Narika anywhere."

        you "(I guess I'll have to look elsewhere...)"

        play sound s_sheathe

        "The hissing sound of metal against metal startles you, and you feel something cold pressing against your throat."

        "It's the business end of a kunai. Although its wielder stands behind you, it's not hard to guess who it is."

        you "*gulp* Ahem, Narika-chan, why don't we talk this through..."

        narika school "You again! I'm not going to let you get in my way this time..."

        narika "You've been really annoying, stalking me like this! Are you in love with me, or something?"

        menu:
            extend ""

            "Yes, that's it":
                you "Well, I... Err... Sure. I am quite taken with you Narika..."

                you "You are, erm, the epitome of cuteness... And your ass..."

                narika "What?!?" with vpunch

                you "... your AS-tounding features are the stuff of... nice dreams..."

                "Narika's voice softens. she lowers her shuriken."

                narika "Oof, that was awful. But at least you seem sincere... *flattered*"

                "Her eyes sparkle."

                narika "Fine, I shan't kill one of my biggest fans."

                $ NPC_narika.love += 1

                you "Phew..."

            "Ew, no...":
                you "What? No way!"

                narika angry "What do you mean, no way?!? Am I not good enough for you?"

                you "Well, you're a deadly assassin, not exactly my type... I mean, there's Suzume, but she's got a massive rack..."

                narika "What the hell are you on about! My chest is still growing, okay! It's bigger than it looks!"

                you "Really?"

                "Unable to move your neck very much because of the blade, you still manage to try to eye her boobies."

                narika "Eek! Don't look!"

                "Narika steps back and tries to hide in embarrassment, withdrawing her blade."

                you "Phew."

                $ NPC_narika.love += 2

                narika "(Damn it, why isn't this boy looking at me like the others do? Is he gay, or something? Hmph!)"

            "You need me":

                you "You need my help..."

                narika "Hmph, you think I can't handle myself? I, the greatest Kunoichi of this continent, and the next?"

                "Her voice grows angry."

                you "N-No..."

                $ NPC_narika.love -= 1

                narika "Why am I even wasting my time with you... Speak, what do you want?"

                "To your relief, she lets you go, but she doesn't let her blade down."

            "Spare me!":

                you "D-Don't kill me, please. I have mouths to feed..."

                narika "Really? You have kids?"

                you "Uh... G-girls. Lots of girls. They call me 'daddy'..."

                narika "Oh, that's adorable..."

                narika "But that doesn't have anything to do with me. *cold*"

                $ NPC_narika.love -= 2

        you "Look, I know you've been collecting keys from the Dean and head teachers."

        you "I could help you reach your goal, if you'd just share your plan."

        narika "Oh really! Do you take me for a fool? Why should I trust you?"

        you "Well..."

        menu:
            you "You can trust me, because..."

            "Tell her the truth":
                you "I work for... Princess Kurohime. I am looking into some murders for her."

                you "The Court is at odds with the Mage's Guild. That's why I'm here incognito."

                narika "Hmmm... It's true that I don't see you fitting in with these stuck-up mages..."

                you "If helping you causes trouble for the Mages, I'm in."

                narika "Well, you have come to me, instead of ratting me out to the Dean. I suppose that makes you neutral."

                "Narika considers your offer."

                if NPC_narika.love >= 5:
                    narika "(I keep running into this boy... Maybe it's a sign? Destiny? Hmmm...)"

                    narika sad "Fine, I will allow you to lend me your aid, feeble as it may be."

                    narika angry "But don't get cocky! I run this show."

                    $ NPC_narika.flags["shared plan"] = True

                else:
                    narika "(I don't know this man, and I have a bad feeling about him.)"

                    narika sad "I don't really need any help. There's a minor hurdle to my plan, but it's nothing I can't handle with a few more days of preparation."

                    narika "Now, to dispose of the interloper..."

                    $ NPC_narika.flags["shared plan"] = False

            "Lie":
                you "I, err... Hate this school... They give me bad grades, and the tuition fees are horrendous..."

                you "And the school cafeteria sucks! I've seen roaches there."

                you "So I'm ready to help you with whatever your plan is. Please tell me what it is, with plenty of details."

                you "Make sure to include the exact extent of your involvement with the murders in the city..."

                you "And if you can put it in writing, that would be best."

                narika "Oh come on, hold it right there!"

                narika "Do you think you could fool me with such a stupid, bold-faced lie???" with vpunch

                you "..."

                narika "The school cafeteria is GREAT! They make a mean matcha tiramisu!!!"

                narika "So what if there are a few roaches... I like tiramisu!" with vpunch

                $ NPC_narika.flags["shared plan"] = False

        if NPC_narika.flags["shared plan"]:

            narika shy "So. I guess you'll do. I could make it worth your while."

            you "S-Sure."

            show narika school with dissolve

            narika "I'm going to break into the Archmage's vault, and recover a very specific item."

            narika "It takes four keys to open the vault, all operated by a separate individual. And I have collected all of them."

            you "So you need four people to get in?"

            narika "Ha! The Dean thinks this makes the vault foolproof against a single attacker, but she's naive."

            narika "With my super speed, I can activate all four keys at the same time, no sweat."

            you "Woah, that's amazing!"

            narika "It sure is! *beaming*"

            you "So... What do you need me to do, then?"

            narika "That old pervert professor told me about one more security contraption I need to deal with."

            you "What is it?"

            narika "It's not only that you need keys. The vault is magically trapped. It must be disabled from the outside."

            narika "I can't use super speed with that. I need someone outside the vault to do it."

            you "That would be me?"

            narika "I was thinking of hiring help, but I really don't want anyone else to blow my cover. Since you're here, you'll do."

            "You stop and think for a moment."

            "This could be a good opportunity to make an ally... Although the Mages' Guild will be pissed."

            "But this could also be an opportunity for a set-up... You could get Narika trapped in the vault."

            narika "So, are you in, or should I spill your guts on the floor right this moment?"

            you "I'm in, I'm in. *attempt to smile*"

            narika "Good! Let's wait until classes are over. Meet me inside the Dean's building."

            scene black with fade

            "You hide until classes are over and all students are on their way home."

            show bg empty_mansion at top with dissolve

            you "(I wonder if this is a good idea... If anyone sees me, I'm going to be in trouble...)"

            "???" "Hey."

            you "Uwaaah!!!" with vpunch

            show narika with dissolve

            narika "Shhh! It's me, silly."

            you "Damn, you Kunoichi are always so silent..."

            narika "Come, let's not waste any time. The Dean is studying in her chambers. This is the right time to strike."

            scene black with fade
            show bg magic_vault at top with dissolve

            show narika with dissolve

            you "So... This magic vault. What's in it?"

            narika "All of the most precious magical devices that the Dean has accumulated over the years. But only one of them interests me right now."

            you "You're not planning on taking everything?"

            narika "No way! Half these items are probably terribly cursed. And I don't like magic one bit. It creeps me out."

            narika "No, the plan is simple: get in, grab the item, get out."

            you "What's the item? Who wants it?"

            narika "*sigh* You don't need to know that. Just focus on your task, it's very simple: once the door is open, pull on this candelabra and keep it down until I'm done. This will disable the traps."

            you "Are you sure about this?"

            narika "I, uh, well... It had better work, or I'd make that old goat swallow the panties I gave him!"

            you "Wait. You gave him your panties?"

            narika angry "*blush* Ah, err, no, I mean... It's not..."

            narika "Anyway! Shut up, and grab that candelabra! Let's get to work!" with vpunch

            play sound s_dodge

            hide narika

            show ninja0:
                xalign 0.825 yalign 0.5
            with blinds

            "*WOOSH*"

            show ninja0:
                ease 0.25 xalign 0.475 yalign 0.4

            play sound2 s_dodge

            pause 0.3

            show ninja0:
                ease 0.15 xalign 0.825
                yalign 0.4

            play sound3 s_dodge

            pause 0.25

            show ninja0:
                ease 0.2 xalign 0.475 yalign 0.5

            play sound s_dodge

            pause 0.1

            play sound2 s_open

            "With amazing speed, Narika leaps from lock to lock, turning all four keys in a single instant."

            you "Wow!"

            play sound s_crash

            "The vault door slams opens, making way more noise than you'd like."

            hide ninja0 with dissolve

            narika "Pull that candelabra down to disable the traps! I'm going in!"

            "You pull the candelabra down and feel a tingling sensation as magical energy flows from the vault and into it, temporarily disabling the traps."

            show bg magic_vault_inside at top with dissolve

            "The vault is filled with magic contraptions and containers of various shape and sizes."

            narika "I'm in! Finally, I can reach it..."
            
            show narika with dissolve
            
            "Narika beelines towards a locked case."

            "She jumps with excitement as she sees a plaque. From where you stand, you can't read what it says."

            "Wasting no time, Narika begins to pick the lock expertly with the point of her kunai."

            narika "Finally, the Oculus Mask is within reach!"

            "She's too busy to pay attention to you. This could be the right time to strike."

            menu:
                "What do you do?"

                "Keep the traps disabled":

                    $ NPC_narika.flags["c3 path"] = "ally"
                    $ story_flags["ninja hunt locked %s" % get_ninja_district(NPC_narika)] = True

                    "You hold the candelabra in place, keeping Narika from being harmed by the magical traps."

                    play sound s_creak

                    "The case slowly creaks opens. Strangely, even though most items in this vault seem to have been left untouched for years, no dust flies off."

                    narika "We did it! All these weeks of preparation will finally pay off... The Oculus Mask is mine!"

                    play sound s_surprise

                    narika "Uh???"

                    narika "WHAT THE FUCK!!!" with vpunch

                    you "What is it?"

                    narika "It's... It's empty!"

                    you "What?"

                    narika "The Mask! It's not here! We've been duped!"

                    you "Are you sure you've looked in the right place?"

                    narika "It could only be here! The plaque said so, as well as my intel..."

                    play sound s_horn
                    pause 0.5
                    play sound2 s_horn

                    "An alarm starts ringing."

                    play music m_danger

                    narika "Damn it! We must run!"

                    you "What's going on?"

                    narika "I don't know! Someone set us up!"

                    play sound s_gust

                    "A gust of wind passes you by. It's Narika, fleeing at top speed."

                    you "Hey, wait for me!!!"

                    "You hear a commotion in the corridor outside. The mages have quickly scrambled some security and are getting ready to storm the place."

                    you "This is not looking good... How are we getting out of here???"

                    narika "Step back."

                    you "Uh? Why... What's that thing you're holding?"

                    narika "I said, step back."

                    "Deciding not to argue, you step behind her, just in time."

                    play sound s_vibro
                    pause 0.2
                    play sound2 s_fire

                    scene black with fade
                    show bg castle with dissolve

                    play sound s_spell

                    "Bird" "*chirp chirp chirp*"

                    "Bird" "Chirp?"

                    play sound s_lightning

                    show bg magicU explosion with flash

                    play sound s_wscream

                    you "AAAAAAAAAAAAAAH!!!"

                    "The wall is blast open. Effortlessly, Narika lifts you in her arms, jumping though the gaping hole opened by the explosion."

                    "Everything becomes a blur as she leaps from rooftop to rooftop, carrying you in her arms. It feels as if you were flying."

                    show bg rooftop at top with dissolve
                    show narika with dissolve

                    "After running at top speed for several minutes, Narika finally comes to a stop. You are amazed to see the Magic University already miles in the distance."

                    narika "Phew... That was close..."

                    you "[MC.swear()], you're faster than a charging griffin..."

                    "You both suddenly stop and realize that she is still holding you in her arms. What's more, her hand is resting on your ass."

                    you "Ahem..."

                    play sound s_crash
                    with vpunch

                    "Narika drops you down like an anvil."

                    narika blush "Ew! Get off me!"

                    you "You were the one coping a feel!"

                    narika "I absolutely was not! And I just saved your ass!" with vpunch

                    you "Yeah, and you were also getting a handful!"

                    narika "Aaaaaah!!!" with vpunch

                    "Narika's eyes spark with confusion and fury. Suddenly, something completely unexpected happens."

                    narika "Uwaaah!!! *burst into tears*"

                    you "Narika... Narika?"

                    narika "All these efforts... All this hard work... And it was all in vain..."

                    you "Calm down... Please."

                    "You give her your handkerchief. She grabs it and noisily blows her nose."

                    you "Listen, you need to tell me everything, and I'll see if I can help you."

                    you "But not here. I know just the place where you can lie low..."

                    scene black with fade

                    "Going through the side streets, you take Narika to [brothel.name]."

                    you "Here, you can take some rest. We'll talk tonight."

                    "Wait until tonight and debrief with Narika."

                    $ calendar.set_alarm(calendar.time, StoryEvent("c3_narika_debriefing", type = "night"))


                "Unleash the traps":

                    you "It's now or never..."

                    play sound s_spell

                    "Releasing your grip on the candelabra, you feel the wave of magical energy ebbing back to the vault."

                    "A faint green halo starts glowing around Narika. When she notices it, it is too late."

                    play sound s_fizzle

                    show narika:
                        ease 0.5 zoom 0.2 ypos 0.8 yanchor 1.0 xalign 0.45

                    narika "W-What!!! The room has become gigantic!!!"

                    you "No, I don't think it has..."

                    "Narika stares back at you, astonished."

                    narika "You have become a giant too? What just..."

                    "Realization comes too late."

                    narika "The candelabra! You let it go!"

                    narika "You betrayed ME! I'll KILL you for this!" with vpunch

                    "Her voice has taken on a mouse-like pitch, which makes her threats all the funnier."

                    you "What was that? I thought I heard a rodent..."

                    play sound s_sheathe

                    "Furious, Narika flings her tiny shuriken at you. It sadly falls on the floor with a clang a mere few feet away from her."

                    narika "My strength is depleted too... What's this damned magic!"

                    shizuka "Why, it's only one of my many security layers, designed to stop hapless thieves like you, of course."

                    show narika with move:
                        xalign 0.25
                    show shizuka at right with dissolve

                    "Shizuka takes in the scene then looks at you, raising an eyebrow."

                    shizuka "Well, if it isn't our Royal agent... So this is the thief you were telling me about? I was expecting someone taller."

                    you "Sure. I tricked her. I did it as a, err, favor to you and the Guild..."

                    shizuka "Really? Well, I suppose thanks are in order then. Although I'm not sure I trust your motives."

                    "Shizuka strolls into the vault, and casually flicks the item case open, not even straining as she disable multiple intricate magic locks."

                    shizuka "Good to know the mask is still safely in... Uh?"

                    "Shizuka suddenly frowns."

                    shizuka "WHERE is the mask? My magical prototype! WHERE IS IT!!!" with vpunch

                    "She slams the case closed. You think you can see a tiny piece of paper flying away."

                    you "A prototype? What does it do?"

                    shizuka "It has the power of spectral sight, but that besides the point!"

                    shizuka "You!" with vpunch

                    "Shizuka looms over Narika, giving her a threatening look."

                    narika "I-I didn't take it, I swear! You stopped me before I could open it..."

                    "Shizuka then looks at you."

                    you "I didn't even step in the vault..."

                    "Even though she's seething, Shizuka understands that you are not lying."

                    shizuka "I will have to deal with that. Let me call the guards, they'll take that rat away."

                    you "Wait! I want to interrogate the prisoner first."

                    shizuka "She doesn't know who took the mask. For all I know, it might have been gone for months..."

                    you "But I need information for a different purpose. Court business..."

                    shizuka "*shrug* I suppose you can, then. Use one of the detention cells. But I'll give you an hour, no more."

                    "She snaps a finger, opening up a portal."

                    narika "Hey! First let me go back to my normal size!" with vpunch

                    "Shizuka scoffs."

                    shizuka "Not a chance. You'll stay like this until it no longer entertains me."

                    narika "*squeaking and vociferating*"

                    shizuka "That could take a while..."

                    call c3_narika_interrogation() from _call_c3_narika_interrogation

        else:
            $ NPC_narika.flags["magicu failed"] = True
            play sound s_sheathe
            "*HISS*"

            you "W-Wait! I'll go away, and I won't bother you in this school ever again!" with vpunch

            narika "Hmph, you won't bother me again if you're dead..."

            play sound s_wscream

            you "Aaaaaah!"

            narika "*sigh* But fine, I don't want to get blood everywhere and blow my cover. Just get out of here, and never come back."

            you "I-I can go? Really?"

            narika "Yes. Now fuck off, before I change my mind."

            scene black with fade

            "Discretion being the best part of valor, you retreat promptly, leaving the school's premises."

            you "I lost this battle, but not the war... I must find another way to get to Narika."

        $ story_remove_event("c3_narika_MU_class", "daily")
        call remove_item(MU_entry_scroll, use_article=False) from _call_remove_item_5

    stop music fadeout 3.0
    scene black with fade

    return

label c3_narika_debriefing():

    scene black with fade
    show expression brothel.master_bedroom.get_pic() at top
    with dissolve

    "Later that night, you return to your quarters. You find Narika pacing around, brooding, while Suzume tries to comfort her."

    show narika at right with dissolve

    narika angry "Months of planning! And for what! I hate the fucking magic university! I hate magic!" with vpunch
    
    show suzume at left with dissolve

    suzume "Chill, sis'. [MC.name] is here, maybe he can help you sort out this mess."

    narika "Mister Pervert over here? Ha!"
    
    "You wonder when she took to calling you Mister Pervert, but you guess working in a brothel doesn't help your case."
    
    narika sad "Nothing can salvage this wreck... The money is one thing... But my reputation..."

    you "Calm down. Tell us the whole thing from the beginning."

    narika "Well..."

    "She hesitates for a moment, but shrugs."

    narika shy "I guess you already know a lot about the situation, so I might as well fill you in. It's not like any of this information is going to be useful to either of us."

    narika "I was personally hired by Stee V. the Wondrous, a famous bard from Westmarch. As you must know, he's one of the most talented musician in Xeros."

    narika "But he is also afflicted by a terrible infirmity. He is blind."

    narika "So when he heard that the Magic University in Zan had developed magical prototypes to help with various disabilities, he got interested."

    you "I see..."

    narika "But he couldn't, so he got in negociations with the Dean, tried to get her to sell the prototype. But the price she was asking for could buy you a small principality in Westmarch. It was too much, even for him."

    narika normal "So he took the next logical step: he decided to {i}steal{/i} it."

    $ MC.rand_say("ar: That's not very honorable...", "wa: That's not very honorable...", "gd: That's not very honorable...", "tr: Yup, that makes sense.", "sh: Yup, that makes sense.", "ne: Yup, that makes sense.", "Steal it?")

    narika "Naturally. And so he hired the best Kunoichi money can get!"

    menu:
        extend ""

        "You're the best":
            you "It's you, isn't it?"
            $ MC.evil -= 1

            narika shy "It goes without saying. Although after today..."

            narika angry "Damn you, Mister Pervert, why did you have to remind me? *angry*"

            $ NPC_narika.love -= 1

            "Your flattery is only twisting the knife. Narika bows her head in shame."

        "Others are better":
            you "I know a couple others who are at least as good as you. Haruka, the Earth Kunoichi. Mizuki, the weird Ice lady."
            $ MC.neutral += 1

            narika sad "Pfff, normally, I would not even consider them competition..."

            narika "But what if they complete their assignment before I do? People will think I'm not worthy of my reputation!"

            "Narika lets these dark thoughts discourage her."

        "You're the worst":
            $ MC.good -= 1

            you "The best Kunoichi? Give me a break! You couldn't even manage a little burglary."

            "Narika blushes bright red."

            narika angry "You... You..." with vpunch

            "Suddenly, the unexpected happen. Tears start streaming from her eyes."

            narika sad "You're right, Mister Pervert... I completely failed... I am worthless..."

            "She sobs like a little girl. You are completely taken aback."

            suzume doubt "Well done, you big oaf..."

    "You change the subject, hoping to avoid a scene."

    you "Ahem... So this blind bard... Came all the way over to hire you?"

    narika "Of course not. He sent one of his henchmen, or should I say henchwoman."

    you "A woman?"

    narika "Yes, and a dangerous one at that. She was under a disguise, but I could sense her power... Not one to be trifled with."

    you "Could it be that she set you up?"

    "Narika broods, her mood somber."

    narika "Maybe... Why would she though? Why me?"

    you "Anyway, someone got there first. And stole that item. Correct?"

    narika "It must be! They replaced the mask with that stupid note."

    you "Wait, a note? What did it say?"

    narika "Uh? I don't know! I threw it on the ground as soon as we were out of there!"

    you "You WHAT?" with vpunch

    suzume normal "Yeah, she did throw it... But I picked it up."

    you "Phew... At least one of you has sense."

    suzume doubt "There's only a single sentence though."

    suzume "'Now Haku will have his revenge.'"

    you "Haku? Who the fuck is Haku?"

    narika "That's not a Kunoichi's name."

    suzume "It's a male name. Sounds like a Zanic name."

    you "Wait a minute- this item, the mask..."

    narika "The Oculus Mask."

    scene black with fade
    show bg mask escape at desaturate with dissolve

    you "Is it made of a silver-like metal? In the shape of a demon's eyes?"

    narika "It's Cimerian mithril, but yes! Have you seen it?"

    "Narika jumps to her feet, suddenly full of hope."

    you "Yes we have. Let me fill you in on the details..."

    scene black with fade

    "You tell Narika about the masked man who's been terrorizing Zan's upper class."

    show expression brothel.master_bedroom.get_pic() at top
    show narika at right
    show suzume at left
    with dissolve

    narika "It must be him, then! How did he manage to steal the mask in the first place? I was barely able to get to it, and I'm the best-"

    you "Let's not have this conversation again, shall we?"

    suzume "Listen, [MC.name]! We just got a major clue... That guy's name is Haku! And he's blind! If we-"

    you "Well, lot of big ifs and buts... And don't get me wrong, I like big butts and I cannot lie. But..."

    suzume "Do you have a better lead?"

    you "I suppose not..."

    suzume "We are closing in on this guy. A good day's work."

    you "And I can finally stop going to school every day like in that recurring nightmare where I forget my pants."

    narika "Hey, wait! What about me? I didn't get anything out of this!"

    you "Well... If you help us catch that guy, you can have the mask."

    narika "Really? Then I'm in!"

    show suzume bend with dissolve

    suzume "It's nice to have a new ally. Even if you're a bit... Young."

    narika blush "I may not be an old hag with saggy boobs like you, but I have twice the skill! Just watch me."

    suzume "I'm sure you don't have to worry about saggy boobs, being flat-chested and all..."

    narika angry "I'm still {i}growing{/i}, okay? Grrrr..." with vpunch

    you "Girls, girls... To the task at hand."

    suzume "Yes, boss!"

    play sound s_dodge
    hide suzume with blinds

    narika normal "Okay, Mister Pervert!"

    play sound s_dodge
    hide narika with blinds

    $ game.set_task(None, "story3")

    scene black with fade

    "And just like that, they're gone. You wonder if it will stop creeping you out one day."

    return

label c3_narika_interrogation():

    hide shizuka with flash
    show narika with move:
        xalign 0.45

    "Shizuka disappears into the portal, leaving you alone with Narika."

    narika angry "Let me go! I haven't done anything to you! I have nothing to tell you!"

    you "I'll be the judge of that."

    narika "Listen, if you help me escape..."

    you "Hush, I have questions first."

    you "What's your connection to the murders in the city, and the other Kunoichi?"

    narika "None, none whatsoever!"

    you "Then who do you work for?"

    narika "I can't say! Now, let me go!"

    you "At least tell me what that mask is..."

    narika "It's just a magical prosthetic, it gives the sense of sight to blind people."

    you "Who sent you to retrieve it?"

    narika shy "Uhn uhn. *shakes her tiny head* Not until you let me go!"

    you "I was hoping you'd be more helpful..."

    menu:
        "What do you do with Narika?"

        "Agree to help her":
            $ renpy.block_rollback()

            you "Okay, I will help you escape. But it's going to damage my reputation with the Dean by a lot, so you better tell me all that you know!"

            narika shy "Fine, fine, I will tell you."

            narika "I was hired by a famous artist in Westmarch, who is blind."

            narika "He wanted me to recover the Oculus Mask to cure him."

            you "Hmm. That doesn't sound related to our case."

            narika "I told you, I can't help you. I'm as shocked as that stupid Dean that the mask was already stolen."

            narika "Now, you need to help me get out of here!"

            menu:
                extend ""

                "Sure":
                    $ NPC_narika.flags["c3 path"] = "neutral"
                    $ story_flags["ninja hunt locked %s" % get_ninja_district(NPC_narika)] = True
                    $ MC.good += 2

                    you "A promise is a promise, I suppose. But I need to get you past the guards."

                    narika normal "I'm super small now, so that should be easy!"

                    play sound s_dress

                    you "Here, you can hide in my pants."

                    narika "Sure, I can hide in your-"

                    play sound s_surprise

                    narika angry "PANTS???" with vpunch

                    you "Sure. If there is a bulge under my shirt, the guards may get be suspicious. In my pants, on the other hand, it's business as usual."

                    narika "But... But... I... No!"

                    "Eventually, seeing no alternative, Narika begrudgingly climbs inside your pants."

                    hide narika with dissolve

                    you "Heheh, your hair tickles."

                    narika "Shut up, and get moving! I can't breathe in here!"

                    scene black with fade
                    show bg empty_mansion at top with dissolve

                    "Making sure no one is watching, you leave the cell, walking past the guards that are watching over the vault room."

                    narika "*muffled* W-What's this? Something is taking all the room in here, and it's growing!"

                    you "It's your fault, if you keep wiggling like this, it stimulates my..."

                    narika "Uwaaah! Let me out!!!" with vpunch

                    show narika:
                        xalign 0.45
                        ypos 0.8
                        yanchor 1.0
                        zoom 0.2
                    with dissolve

                    "Finally, Narika tumbles down your leg and frees herself from your pants."

                    narika "That was HORRIBLE! Hair from your leg even got in my mouth! *spits*"

                    you "You hope it's from the leg..."

                    narika "Ew!" with vpunch

                    "Narika sighs, exasperated."

                    narika sad "Still, you held your part of the bargain I suppose. So I guess you can have this."

                    "She holds a small piece of paper in her tiny hand, handing it over to you."

                    you "What's that?"

                    narika "It's from the case in the vault. I grabbed it before that bitchy Dean could notice."

                    you "A note? It's a single sentence. Let's see..."

                    you "'Now Haku will have his revenge.' Who or what is Haku?"

                    narika "I don't know. But that sounds like a man's name."

                    you "Thank you, that could be a precious clue..."

                    you "You're free to leave, now. What are you gonna do?"

                    narika angry "Are you kidding? I need to find a way to grow back to my normal size, before I get eaten by a small dog!"

                    narika "It would be better if our paths never crossed again... I have many other scores to settle first, but don't think I forgot that you betrayed me in the vault!"

                    you "Tall words for such a tiny woman... Let's go our separate ways, then. I need to continue my investigation."

                "Nah":
                    $ NPC_narika.flags["c3 path"] = "banished"
                    $ story_flags["ninja hunt locked %s" % get_ninja_district(NPC_narika)] = True
                    $ MC.evil += 1

                    you "Nah, I was lying. You can stay here and enjoy the Dean's hospitality."

                    narika angry "WHAT???" with vpunch

                    you "You're entirely too trusting for a ninja, you know that? See ya!"

                    "You ignore her squeals of anguish as you step out of the cell."

        "Leave her to her fate":
            $ NPC_narika.flags["c3 path"] = "banished"
            $ story_flags["ninja hunt locked %s" % get_ninja_district(NPC_narika)] = True
            $ MC.good -= 1

            you "I can see you're not being reasonable. I'll just leave you to rot in the Archmage's cells, then."

            narika angry "Wait! Wait!"

            you "Well, good bye then."

            "You ignore her squeals of anguish as you step out of the cell, knowing she will be dealt with by the Archmage."

        "Rape some sense into her":
            $ NPC_narika.flags["c3 path"] = "raped"
            $ story_flags["ninja hunt locked %s" % get_ninja_district(NPC_narika)] = True
            $ MC.evil += 5

            you "I don't think you understand the situation you're in, Narika."

            "Narika senses the threat in your tone."

            narika angry "What, you're thinking of beating me up, or something?"

            you "Oh no, no, I would never pick on someone so small..."

            narika "Fuck you!" with vpunch

            you "That, on the other hand, can be arranged..."

            narika "What do you-"

            scene black with fade

            play sound s_scream

            narika blush "AAAAAH!!!"

            play sound s_dress

            "*riiip*"

            show bg narika_tiny1 at top with dissolve

            narika "EEEEK! Get away from me, pig!" with vpunch

            you "It's interesting to have a real-life doll-sized girl to play with..."

            you "Even your nipples are so tiny... *rub*"

            play sound s_scream_loud

            narika "AAAAH!!! D-Don't touch me!!!" with vpunch

            you "Cute little pussy you have here... Even though it's so small, I can all the little details..."

            you "You look like the action figures I used to have as a child... But I didn't know it was going to be this type of action."

            narika "Let me GOOO!!! You fucking pervert!!!" with vpunch

            you "We'll need to get you well lubricated for the next part... *spit*"

            "She flinches in horror as you cover her lower body with saliva."

            play sound s_screams

            narika "What next part? No! Leave me alone!!! Heeeelp!!!" with vpunch

            you "This part."

            show bg narika_tiny2 at top with dissolve

            narika "Aaaah!!! Get that thing away from me!!!" with vpunch

            you "Hahaha, my dick is as tall as you now! I can rub it over your entire body in one go!"

            play sound s_scream_loud

            narika "Disgusting! Heelp, someone, heeeelp!!!" with vpunch

            "Mercilessly, you continue, using your spit as lubricant to slide up and down her tiny exposed body."

            narika "What's... What's happening to me... This is a nightmare..."

            "Grinding against her, you increase the pressure on her crotch, forcibly keeping her legs open."

            you "I hear the Kunoichi are very flexible. Why don't we test that theory?"

            narika "What do you... Aaaaaah!!!" with vpunch

            show bg narika_tiny3 at top with dissolve

            "You place your dick near her lower entrance."

            narika "No, no, wait, WAIT!!! This is impossible!"

            narika "You can't do this, it will br-"

            play sound s_splat

            show bg narika_tiny4 at top with dissolve

            narika "AAAAARGH!!!" with vpunch

            "Ignoring her, you push your dick inside her tiny doll-like body. At first, it looks like there is no way this will ever work, but slowly you force your way inside, stretching her to her limits."

            "Narika cries out in pain and bewilderment."

            play sound s_scream_loud
            narika "AAAAAAH!!!" with vpunch

            you "Look at that, it's like you're pregnant with my dick!"

            narika "STOOOOOP!!! STOP!!!" with vpunch

            "A lesser woman would have passed out or died, but Narika had years of intense training, allowing her to surpass the limits of the human body."

            "Still, she hangs on only by a thread."

            play sound s_screams

            narika "NGYAAARH! AAARH! AAAAH!!!" with vpunch

            "Her body is grossly deformed as you start fucking her."

            you "Hahaha, I like tight pussy, but this is something else!"

            narika "I'm going to die, stop!!! *sobs*"

            you "You're the perfect onahole for me. Muhahahaha!"

            narika "Noooo..."

            "You only laugh and increase your pace, making her jerk her head back and scream like an animal."

            show bg narika_tiny5 at top with dissolve

            play sound s_screams

            narika "AAH, AAAH, AAAAAAAH!!!" with vpunch

            "Enjoying yourself at her expense, you keep messing up her insides mercilessly, ruining her tiny body."

            narika "AAH, NGGH, AAARH... S-Stop... *sob*" with vpunch

            you "Don't worry, it's not going to last much longer."

            "Her eyes widen, as she wonders what you mean. She doesn't have to wonder for long."

            with flash

            you "Ughhh..."

            show bg narika_tiny6 at top with doubleflash

            "Suddenly, you start cumming, filling her belly to the brim with semen."

            play sound s_scream_loud
            narika "UWAAAGH!!!" with vpunch

            with flash

            "You pull out and spray the rest of your cum all over her tiny body. She howls in pain as your dick pops out."

            you "Hehehe, I might have gone a little overboard this time... But that was fun for me, at least."

            "Narika is looking down at her gaping hole, horrified. You have ravaged her body from head to toe."

            "She is left speechless, in a completely state of shock."

            you "That was fun. Now, will you tell me about your secret-"

            narika "*drool*"

            you "Narika? Narika?"

            "Narika is completely unresponsive, her face inexpressive. Her mind is gone. She is alive, but barely."

            "You try to talk to her, but she ignores you. She is completely gone."

            you "Looks like I broke another one of my toys... Oh well."

            $ MC.change_prestige(3)

            scene black with fade

            "Shrugging, you ditch her limp body on the ground where she lands with a thud, barely breathing amidst a pool of cum."

            "You step out of the vault, hoping to get out of here before anyone asks too many questions."

            "Fortunately, no one interferes, and soon you are out of the Magic University for good."

            $ MC.change_prestige(3)

    $ game.set_task(None, "story3")

    scene black with fade
    # show bg magic_university at top with dissolve

    "You think back about what you've learned."

    you "A magical all-seeing mask has disappeared, and soon after this masked man appears and starts murdering people in the city... Quite the coincidence."

    you "If it is indeed the same person, our culprit was a blind man... I guess that narrows down the possibilities."

    return

label c3_narika_final_intercept(): # Called from ninja_game
    play music m_narika fadein 3.0

    scene black with fade
    show bg narika intro at top with dissolve

    narika ninja "You are trying my patience! Don't you understand I'm way out of your league?"

    if MC.has_item(void_rune.name):
        "You can feel dark energy flowing from the void rune into the warhammer where you inserted it."

        you "Bring it on!"

        "Narika starts running, but she is much slower than before."

        narika "Khhh! *sweat*"

        narika "(What's happening... It feels like every movement is a slog?)" with vpunch

        stop music fadeout 3.0

        $ story_flags["ninja hunt"] = calendar.time

        call run_ninja_game(njgame) from _call_run_ninja_game_1

        return _return

        # results are in BKchapter2 - label intercept_narika()

    else:
        suzume "Damn, she's slippery as always... Boss, I don't think we can catch her."

        play sound s_gust
        hide bg with dissolve

        "Narika moves faster than your eyes can see, and before you have a chance to react she is already leaping from rooftop to rooftop in the distance. You know better than to run after her."

        scene black with fade

        you "Damn, if only I had a counter to her super speed..."

    return

label c3_narika_captured():

    "That night, you join Gizel in the cellar of [brothel.name] to visit your new captive."

    scene black with fade
    show bg narika_capture1 at top with dissolve

    narika blush "You! What have you done to me! My powers won't work here!" with vpunch

    gizel smirk "Hmph. Mind your tone, little girl."

    gizel "I just set you up to be comfortable for what's coming."

    narika "What's coming? W-What do you mean? And why am I naked!!!"

    gizel "Ah, [MC.name], here you are. I was waiting for you to begin the lesson."

    narika "Lesson? What do you sick people want with me??? *scared*" with vpunch

    you "I have brought you here so that you will join my fine establishment."

    narika "What? What are you talking about? What establishment?"

    you "Well, it is, let's say, a 'house of carnal pleasure'."

    narika "A house of carnival what?"

    gizel "It's a brothel. For whores. Hookers. Prostitutes."

    play sound s_surprise

    narika "What!!! Are you out of your mind??? I'm not even... Err..." with vpunch

    gizel "Silence!" with vpunch

    show bg narika_capture2 at top with dissolve

    play sound s_punch

    "*WHIP*" with vpunch

    show bg narika_capture3 at top with dissolve

    play sound s_scream

    narika "OUCH!!!"

    gizel "I told you to change your tone. You will mind your manners, or else..."

    narika "B-But... But... You guys..."

    "Gizel has a dangerous glint in her eyes."

    gizel "Mistress Gizel. And you will refer to [MC.name] as Master."

    narika "Whaaat?" with vpunch

    narika "You can't seriously suggest I call you that?"

    play sound s_punch
    pause 0.2
    play sound2 s_punch

    "*WHIP* *WHIP*" with vpunch

    show bg narika_capture4 at top with dissolve

    play sound s_scream

    narika "AW!!! STOP!!!" with vpunch

    gizel "Ask me nicely!"

    play sound s_punch

    "*WHIP*" with vpunch

    narika "S-Stop... M-M-Mistress..."

    gizel "That-a-girl!"

    you "Gizel, there is no need for such violence."

    gizel "Who said there's a need? I just wanted to do it."

    you "Anyway. Narika, look at the situation you're in. You've lost your powers, you've lost your reputation."

    you "It would be better for you to cooperate."

    narika "B-B-But... I am not a whore!!!"

    gizel "Who are you talking to???" with vpunch

    play sound s_punch
    pause 0.2
    play sound2 s_punch

    "*WHIP* *WHIP*" with vpunch

    show bg narika_capture5 with dissolve

    narika "AW! OW! OUCH!!!" with vpunch

    show bg narika_capture4 with dissolve

    narika "M-Master [MC.name]... I mean... I am not..."

    gizel "You are not a whore... {i}Yet{/i}."

    you "No one said you have to be a whore... You can tend to the customers in other ways: You can wait tables, dance for them..."

    narika "D-Dance? Only dance?"

    you "Well, at first..."

    narika "What do you mean, at first?!?" with vpunch

    you "Well, you can take things at your own pace."

    gizel "Or you can take things at our pace. *snark*"

    narika "B-But... You don't understand... I'm..."

    gizel "Spit it out!" with vpunch

    play sound2 s_punch

    "*WHIP*" with vpunch

    show bg narika_capture5 at top with dissolve

    play sound s_scream

    narika "AAAW!!!"

    show bg narika_capture4 at top with dissolve

    narika "STOP, STOP! I'M A VIRGIN, OKAY???" with vpunch

    gizel "A virgin? Ha..."

    play sound s_evil_laugh
    gizel "HAHAHAHAHAHA!!! That little slut is a virgin..."

    "Tears well up in Narika's eyes."

    narika sad "It's true! I have saved my virginity... For... For the right person..."

    "Gizel laughs cruelly."

    gizel "Yeah yeah, sure, we believe that. *snark*"

    you "Suzume told me how you keep flirting with boys wherever you go..."
    
    gizel "But deep down, you were always scared to take the plunge."

    "Narika looks away, not answering."

    gizel "Little scaredy scaredy cat..."

    narika "Grrr... *clench teeth*"

    gizel "It can't be helped, then. You'd just be dead weight in a whorehouse."

    gizel "I'm just going to have to feed you to the pigs..."

    narika angry "Pigs? W-Wait!" with vpunch

    gizel "Say goodbye, sweetheart..."

    show bg narika_capture5 at top with dissolve

    play sound s_scream_loud

    narika "NOOOOO!!!" with vpunch

    narika "I DON'T WANT TO DIE A VIRGIN!!!" with vpunch

    "The three of you stand for a moment in stunned silent. Narika can hardly believe she blurted it out loud."

    show bg narika_capture5 at top with dissolve

    narika "*sob*"

    gizel "So? I'm sure [MC.name] will be happy to help you with that..."

    play sound s_surprise

    if NPC_narika.love >= 5:
        narika "(T-That boy? If it's him, then... Could it be?)"

    elif NPC_narika.love >= 1:
        narika "(Wait, what? Am I going to do it with that random guy???)"

    else:
        narika "(Oh no!!! Not that jerk!!!)"

    narika "M-Mistresss, wait, I can't..."

    play sound s_clang

    "Ignoring Narika's muffled complaints, Gizel yanks on her chains, lifting her body up in the air."

    scene black with fade
    show bg narika_capture7 at top with dissolve

    "Narika is hanging from her chains with her legs spread apart and her body exposed."

    "Narika blushes bright red. Instead of protesting, however, she has fallen strangely silent."

    narika "W-What... What are you going to do to me?"

    "Her tone is strangely quiet. It's almost as if there was as much curiosity as fear in her voice."

    $ _min = rand_choice(farm.get_minions("machine"))

    if not _min:
        $ _min = "R2D2"
    else:
        $ _min = _min.name

    gizel "First, I'm going to introduce to one of my minions... [_min]."

    play sound s_vibro

    show bg narika_capture8 at top with dissolve

    narika "W-Wait!!! What the heck is that???" with vpunch

    play sound s_vibro

    "[_min]" "*tickle* *tickle*"

    show bg narika_capture9 at top with dissolve
    play sound s_laugh

    narika "Heeheehee!!! Stop it!!!"

    show bg narika_capture10 at top with dissolve

    narika blush "It feels strange... The robot... It vibrates..."

    gizel "It's a massage bot. Trust me, it will feel good... Nothing to worry about."

    show bg narika_capture11 at top with dissolve

    play sound s_ahaa

    narika "Ahaa!" with vpunch

    play sound s_vibro
    "The robot hands move to massage Narika's petite boobs, eliciting soft moans from her as they move in circles."

    play sound s_vibro

    play sound s_mmh

    narika "Hmmm..."

    gizel "Looks like your tits are small, but sensitive... Like mine..."

    show bg narika_capture12 at top with dissolve

    play sound s_vibro

    "*BZZZ*" with vpunch

    play sound s_moans_short

    narika "Ah, aah, aaaah!!!"

    gizel "Haha, look at that, [MC.name]! She's enjoying herself."

    narika "N-No... I just feel... Weird..."

    play sound s_aaah

    narika "Aaaaah!" with vpunch

    "In spite of herself, Narika is being turned on by the vibrating bot."

    gizel "Fufufufu..."

    "After playing with her for a little while, Gizel suddenly stops the apparatus."

    show bg narika_capture11 at top with dissolve

    narika "*pant* *pant*"

    narika "Is it... Over?"

    play sound s_evil_laugh

    gizel "Oh, no! [MC.name], come forward."

    narika "W-W..."

    play sound s_dress

    narika "*gasp*"

    "You remove your pants. Narika is stunned to see your dick for the first time, rock-hard and standing for attention."

    narika "*gulp* This can't possibly..."

    show bg narika_capture13 at top with dissolve

    play sound s_scream_loud

    narika "AAAAAH!!!" with hpunch

    "Narika scream as you enter without warning, helped by the love juice that has started to drip from her pussy."

    gizel "Oooooh, it looks like she was a virgin after all!"

    "Narika whimpers as you stretch her pussy with your thick rod."

    "It takes a while for her to adjust to the foreign presence, but she controls her breathing and remains remarkably calm."

    gizel "As expected from a Kunoichi, a little pain is nothing to her. I'd even wager she likes it."

    narika "N-No... It's just... I..."

    play sound s_scream

    narika "Aaaaah!" with hpunch

    "You start moving, overriding Narika's senses as she feels her pussy stretch wider."

    gizel "That girl is a little bit of a masochist, I can tell."

    "You move your hips closer to Narika's body, your balls brushing against her crotch."

    play sound s_mmh

    narika "Hmm..."

    gizel "Look! She's already getting used to it!"

    narika "N-No, it just feels... Wrong..."

    gizel "What a liar. I know you've been wondering about sex for a long time. Maybe [_min] here can make you honest."

    show bg narika_capture14 at top with dissolve

    play sound s_vibro

    "BZZZZ" with hpunch

    play sound s_screams

    narika "Aaaah! Aaaah!" with hpunch

    gizel "Haha, look at that! Her boobs are so sensitive, she's already shaking!"

    gizel "I think she needs a good pounding. [MC.name], it's time to work your magic."

    play sound s_moans

    "Not waiting for Gizel to egg you on, you increase your pace, sliding more and more easily inside and out of her, until you almost match the robot's pace."

    narika "Noooooo!!! I'm losing my mind!!!" with hpunch

    "Narika loses control of her voice, her moans are loud and unrestrained."

    gizel "She's clinging on for dear life, but she loves it! That girl is a natural!"

    narika "No! Please, stop! I can't take it anymore!!!" with hpunch

    gizel "Oh, I bet you can! How about I give you some help?"

    play sound s_clang

    "Gizel pulls on Narika's chains, forcing her body into an even more spread out position."

    narika "Ughn, aaah, aaah!" with hpunch

    "This new position allows you to bang her even deeper. You slowly feel your climax approaching."

    "Her pussy is squeezing you harder and harder, until you are ready to burst."

    gizel "She's already close, too! Haha!"

    play sound s_aah

    narika "Close to, hmmm... Close to... What?"

    gizel smirk "This!" with vpunch

    show bg narika_capture15 at top with flash

    "Gizel suddenly puts a well-manicured finger inside your asshole, sending you over the edge."

    with doubleflash

    you "Hey!"

    play sound s_scream_loud

    narika "AAAAAAAAH!!! AAAAH!!!" with hpunch

    play sound s_orgasm

    "You fill Narika up with your cum, causing her to orgasm at the same time."

    show bg narika_capture16 at top with flash

    gizel "Hahaha! That was so much fun!"

    narika sad "Aaaaah... Did I die? I'm seeing stars..."

    "Narika's eyes are unfocused, and her breathing is labored. A thin line of drool leaks from her mouth."

    gizel "Fufufu, you're okay, kid. I might not feed you to the pigs, after all."

    gizel "Anyway, off we go! I'm going to take good care of you at the farm..."

    narika angry "Wait, what? No!!! I don't want to go to your weird farm!"

    "She looks at you and Gizel in turn with pleading eyes."

    gizel "What??? You're coming with me, right now, and the first thing I'll do is to whip the impertinence out of your sorry husk! *annoyed*"

    $ dim = MC.name[:3]

    narika "Noooo, no, wait!!! [dim]... Master [MC.name]! Don't leave me with that crazy w-witch!"

    narika "I'll work as a waitress or, or I'll dance, or something... Just don't let her take me!"

    you "Well. If you're willing to work, I guess I can..."

    play sound s_surprise

    gizel surprise "What?!? No you won't! She's mine! I'm going to break her!" with vpunch

    narika "I'll be good, I promise! Just... Keep me away from her!"

    you "Fine, fince, you can stay and work at [brothel.name], then. Gizel, leave her be."

    gizel angry "W-What! This is unacceptable! I-" with vpunch

    "You harden your tone."

    you "Back off, Gizel. I've taken my decision."

    gizel upset "Hmph... Fine, whatever, have it your way. I don't care about that slut!"

    narika sad "Aw, th-thanks..."

    you "Oh, and Gizel?"

    gizel "Yes? What?"

    you "Take your finger out of my asshole. It's kind of undermining my authority when I speak."

    gizel shy "Oops, sorry!" with vpunch

    scene black with fade

    "Narika has agreed to help in the brothel. She will perform different jobs outside of whoring, but you won't be able to control her directly until her training is complete."

    "Make sure you have {b}every type of jobs available{/b} at the brothel for this."

    $ MC.change_prestige(3)

    call remove_item(void_rune, definite_article=True) from _call_remove_item_6

    # INIT BREAKING COUNTER
    $ NPC_narika.flags["waitress counter"] = 0
    $ NPC_narika.flags["dancer counter"] = 0
    $ NPC_narika.flags["masseuse counter"] = 0
    $ NPC_narika.flags["geisha counter"] = 0

    $ story_add_event("narika_break_test", "daily")

    $ story_flags['narika path'] = "captured"
    $ story_flags["ninja hunt locked %s" % get_ninja_district(NPC_narika)] = True

    return

label narika_break_test():

    # Step 0: Proc job event

    python:
        job_event=None
        for job in all_jobs:
            if job == "dancer":
                if NPC_narika.flags["waitress counter"] >= 5 and NPC_narika.flags["geisha counter"] >= 5 and NPC_narika.flags["masseuse counter"] >= 5 and NPC_narika.flags["dancer counter"] == 4: # Happens after all job training has been completed.
                    job_event = "narika_" + job
                    NPC_narika.flags[job + " counter"] += 1 # Avoids job event proccing more than one time
                    break
            else:
                if NPC_narika.flags[job + " counter"] == 4:
                    job_event = "narika_" + job
                    NPC_narika.flags[job + " counter"] += 1 # Avoids job event proccing more than one time
                    break

    if NPC_narika.flags["waitress counter"] >= 5 and NPC_narika.flags["geisha counter"] >= 5 and NPC_narika.flags["masseuse counter"] >= 5 and NPC_narika.flags["dancer counter"] >= 5:
        $ story_remove_event("narika_break_test", "daily")
        # $ calendar.set_alarm(calendar.day + 1, StoryEvent(label="narika_broken"))

    if job_event:
        $ renpy.call(job_event)
        $ MC.change_prestige(3)
        $ notify("Narika has now trained sufficiently as a %s." % job)
        return

    # Step 1: Find an available job

    python:
        for girl in job_girls: # job_girls should be initialized in End day
            if girl.job in all_jobs:
                if NPC_narika.flags[girl.job + " counter"] < 4:
                    break
        else:
            girl = None

    # Step 2: Train

    if girl and girl.job in all_jobs:

        if not NPC_narika.flags["jobs intro"]: # Intro to jobs
            $ NPC_narika.flags["jobs intro"] = True

            show expression bg_bro at top with dissolve

            narika sad "(So this is it... What on earth am I supposed to do?)"

            sill "Oh, hi! You're the new girl, right?"

            narika "The new... Yes. I guess so."

            sill "Well, it's a pleasure to meet you! I'm Sill, by the way."

            narika shy "Erm, okay. Hi."

            sill "There are many things to learn, but I'm sure you'll manage. And don't forget, if you have any question, I'll always be here for you!"

            narika "How..."

            sill "Yes?"

            narika angry "How can you be so perky and carefree!!!" with vpunch

            sill "Uh?"

            narika "This is a {i}whorehouse{/i}!!! People come here and have sex!" with vpunch

            sill "Well... Yeah, of course. That's what a whorehouse is."

            narika "Aren't you bothered by it???" with vpunch

            sill "*thinking* Well, there are a lot of chores... A lot of bed sheets to clean up... And Master [MC.name] often scolds me, but..."

            narika "That's not what I mean!!! The SEX!!! It's wrong!!!" with vpunch

            sill "The sex is wrong? Why?"

            narika shy "Because, uh... Well..."

            sill "I see. Maybe you don't like it because you've had bad lovers in the past."

            sill "But Master [MC.name] can help you. He personally trains most of the girls."

            narika blush "That's not what I mean!!!" with vpunch
            
            narika shy "I already saw his, err, training..."

            sill sad "Oh, so you had sex with him already? What did he do? He's not in love with you, is he? *anxious*"

            narika "I, err, uhm... It was weird, okay? I didn't want to do it! It felt... Wrong!"

            sill happy "Oh, okay. You're not made for each other then! It's fine."

            narika "Does, erm... Does [MC.name] have sex with everyone around here?"

            sill "Well... Pretty much, yes."

            narika "Does it mean that... Err... He'll do it again with me?"

            sill sad "Well, that's probably his intention..."

            sill happy "But you know what, I'll tell him to leave you alone."

            narika "N-No, that won't be necessary..."

            sill "Oh don't worry, he'll listen to me for sure! I think. I'm his number 1 confident and advisor, so... Hehe."

            narika angry "I said don't!" with vpunch

            sill sad "Whoah!"

            narika shy "It's just that, erm... I don't want no favors, okay..."

            narika "(What am I doing?)"

            sill normal "Well, erm... Okay, then. Today, you'll follow [girl.name] around. She'll show you the ropes."
            scene black with fade

        if NPC_narika.flags[girl.job + " counter"] == 0:
            show expression ("bg " + job_room_dict[girl.job]) at top with dissolve

            if girl.is_("dom"):
                girl.char "Look who's here... Another newbie."

                narika shy "Well... Yes. What do you do here?"

                girl.char "Today I'm working as a [girl.job]. Follow me, kiddo, and try to keep up."

                narika "Hmph, of course!"

            else:
                girl.char "Oh, welcome, Miss. You are...?"

                narika shy "Narika. I'm the new girl. I guess."

                girl.char "S-Sorry, right! Sill told me."

                girl.char "I'm working as a [girl.job] today. Would you care to help me?"

                narika "Sure, okay..."

            if girl.job == "waitress":

                girl.char "Our main job is to serve customers with food and drinks, and to chat with them as we go."

                girl.char "Tipsy customers often get handsy, but you'll get used to it."

                narika "Can I chop their hands off?"

                girl.char "What??? No!!!" with vpunch

                girl.char "Just play along, you'll get better tips this way."

                play sound s_sigh

                narika "(This stuff is complicated...) *sigh*"

            elif girl.job == "dancer":

                girl.char "As dancers, we put on a hot show for our audience, we got all kinds of fun costumes..."

                narika "Wait, this one is damaged! There are holes everywhere..."

                girl.char "Oh, no, that's intended."

                narika "But it doesn't even cover the..."

                girl.char "Teeheehee, that's the best part!"

                narika "(Oh my...)"

            elif girl.job == "masseuse":

                girl.char "We give massages to the customers, so that they can get in the mood for the rest."

                narika "Massages? I guess I know how to give massages!"

                girl.char "You do? Actually, my shoulders are sore. Show me!"

                narika "Sure thing. Get ready..."

                girl.char "Is that... A fighting stance?"

                play sound s_punch
                pause 0.5
                play sound2 s_punch
                pause 0.3
                play sound3 s_punch
                pause 0.2
                play sound s_punch

                narika "ATTACK OF THE 10,000 NEEDLES!!! TAHTAHTAHTAHTAHTAHTAAAAAH!!!!" with vpunch

                play sound s_scream_loud

                girl.char "AAAAAAARGH!!!" with vpunch

                with fade

                girl.char "Aaaaw... I can't feel my body from the waist up..."

                narika "Erm, sorry... I think I overdid it a little..."

                girl.char "Actually, that was good... The pain is gone..."

                girl.char "But please be more gentle with customers, okay? We want them relaxed, not dead."

                narika "S-Sorry..."

            elif girl.job == "geisha":

                girl.char "As a geisha, you must bewitch customers with your wits and artistic talents, and display respect proper etiquette."

                narika blush "*loud belch* Yeah, yeah, how hard can it be."

                girl.char "Err..."

                girl.char "Let's see. Do you know how to sing?"

                narika "No."

                girl.char "Play music?"

                narika "No."

                girl.char "Make tea?"

                narika "Nope."

                girl.char "Do you know how to recite poems? Arrange flowers? Do your make-up? Put on an Obi? Hold your hair up with chopsticks?"

                narika angry "No, no, no and no!!!" with vpunch

                narika "What good are any of these things??? I know a hundred-and-one ways to skewer a man so that he bleeds and dies silently! Will that do?"

                girl.char "Oh dear..."

                girl.char "Look, let me help you put this kimono on. You just stand pretty, and whatever you do, don't open your Arios-damned mouth."

                narika "Hmph, fine..."

                narika "(What could be so hard about this geisha job anyway?)"

        $ NPC_narika.flags[girl.job + " counter"] += 1

        $ renpy.block_rollback()

        with fade

        if girl.job == "dancer" and NPC_narika.flags[girl.job + " counter"] == 4:
            $ notify("Narika has now trained sufficiently as a dancer.")

        if NPC_narika.flags[girl.job + " counter"] <= 4:
            $ notify("Narika trained with %s as a %s (%i/4)." % (girl.name, girl.job, NPC_narika.flags[girl.job + " counter"]), pic="side narika blush")
            
    else:
        $ notify("Narika couldn't help any girls in the brothel with their job.", pic="side narika blush", col=c_lightred)

    return

label narika_waitress():
    scene black with fade

    "Hearing some noise in the kitchen, you take a peek."

    you "Well, if it isn't Narika working in the kitchen... I can hardly believe you went from a murderous Kunoichi to baking cookies, hehe."

    narika blush "S-Shut up... I just have a lot to do for customers..."

    you "And I want to thank you for being pleasant to our customers. I see you've even adopted our 'no bra' policy."

    show bg narika_waitress1 at top with dissolve

    play sound s_surprise

    narika "S-Stop fooling around! I just don't usually wear bras..."

    you "Oh yes, I've noticed... I guess with your small boobs, you don't need them."

    narika "My boobs are not small!!! Grrr..." with vpunch

    you "Let me see... Hmmm, it's just as I remembered, they're smallish but fit in my hands nicely!"

    play sound s_dress

    "You squeeze them to illustrate your point."

    play sound s_ahaa

    narika "Ah, aah, stop it..."
    
    you "But your nipples are really perky. They stand at attention whenever I touch you... It's nice."
    
    play sound s_scream
    
    narika "Aaaaah!"
    
    you "And they're so sensitive..."
    
    "You gently rub her nipples between your fingers, eliciting more moans from Narika."
    
    narika "I've got... Aaaah... Food to prepare..."
    
    "Ignoring her, you rub your bulge against her ass."
    
    you "And yet, you're not stopping me. What gives?"
    
    show bg narika_waitress2 at top with dissolve
    
    play sound s_hmm
    
    narika "I... Hmmm, idiot, I can't think straight when you... Aaah... Touch me like that..."
    
    "You continue groping Narika's tits and ass. She could easily push you back, but instead she waits for what comes next, like a deer frozen in the headlights of a yet-to-be-invented mechanical contraption."
    
    you "Narika, just resume your cooking. We don't want to keep the customers waiting."
    
    show bg narika_waitress3 at top with dissolve
    
    narika blush "You're not going to do... Anything else, are you?"
    
    you "Oh, don't mind me... I'm just going to touch you a little."
    
    "Narika resumes her cooking with shaking hands, blushing and moaning softly as you caress her body."
    
    play sound s_aaah
    
    narika "Aaah... [emo_heart]" with vpunch
    
    "Narika pretends to ignore you, but you can tell she is getting turned on."
    
    you "Stay focused on the food, will you? Don't enjoy yourself too much."
    
    narika "O-Of course! I'm not feeling this one bit. With my elite training, I can concentrate on whatever task is at hand regardless of your pointless distractions."
    
    you "Oh good, then by all means, ignore this."
    
    "You slip your hands inside her panties, slowly taking them off sending shivers down her spine."
    
    narika "Just let me work. I'm not going to be-"
    
    show bg narika_waitress4 at top with dissolve
    
    play sound s_scream
    
    narika "Aaah!!!" with vpunch
    
    "Narika's eyes open wide as you lift her leg up without warning."
    
    you "Just ignore me, Narika! Nothing to see here."
    
    narika "I-Idiot, I told you to leave me alone... Your thing is touching..."
    
    you "Hmmm... I know."
    
    with vpunch
    
    play sound s_scream_loud
    
    narika "AAAAH!!!"

    play sound s_splat
    
    "You enter her with a single thrust."
    
    play sound s_moans
    
    narika "Ah, aaah, aaaaaah..."
    
    "Narika pants and moans as she struggles to adjust to the size of your dick. But once again, she doesn't resist."
    
    you "Hmm, feels nice and tight. More than a little wet, too."
    
    show bg narika_waitress5 at top with dissolve
    
    narika "It's your fault... You're making me feel weird..."
    
    with vpunch
    
    narika "Ah, aah, aah! S-Stop moving, you idiot! I have to finish this!"
    
    "Narika tries to resume her cooking, but her legs are shaking so much, she is having trouble just standing up."
    
    you "Don't worry, just let me take care of everything. It's going to be fine."
    
    show bg narika_waitress4 at top with dissolve
    
    narika "AAAH!" with vpunch
    
    "You start moving your hips, slowly at first, then faster."
    
    "Narika is helpless as you slide in and out of her, her pussy squeezing you harder with each thrust."
    
    play sound s_moans_short
    
    narika "Ah, ah, ah!" with vpunch
    
    "You keep playing with her tit too, tugging on her sensitive nipple."
    
    play sound s_ahaa
    
    narika "Ah, aah, ahaaaah!!!" with vpunch
    
    "Narika's breathing is labored and irregular, she has completely forgotten the task at hand, her resolve is slowly crumbling."
    
    you "It's really easy to move inside you now... Like your body welcomes me."
    
    play sound s_scream
    
    narika "AAAAAH!!! Don't say such embarrassing things!!!" with vpunch
    
    play sound s_moans
    
    "In spite of herself, Narika starts moving her hips back, matching your pace."
    
    you "Oh, you're getting into it! That's nice."
    
    "You increase your pace, pounding her more forcefully."
    
    "The table shakes with every thrust, flour spilling everywhere. You don't care, and renew your assault."
    
    narika "Aaaaah, AAAAAAH!!!" with vpunch
    
    "Narika is moaning feverishly. You can tell she's about to climax."
    
    you "Let's take a break, shall we?"
    
    "An inch from cumming, you suddenly stop moving with your dick still stuck deep inside her."
    
    play sound s_surprise
    
    narika "W-What? Why did you stop?!" with vpunch
    
    narika "I was about to, err..."
    
    "Narika blushes even more, her ass slowly wriggling against your crotch."
    
    you "..."

    you "Just kidding."
    
    you "Haaa!" with vpunch
    
    show bg narika_waitress6 at top with flash
    
    "Surprising her, you slam your cock deep inside her one last time, sending both of you over the edge."
    
    with doubleflash
    
    play sound s_orgasm
    
    "Narika screams as you both climax at the same time."
    
    with flash
    
    narika "Aaah... Arrh... You really came inside..."
    
    "Narika looks defeated as she tries to catch her breath."
    
    you "Hey, that was pretty fun! I'd say you have a future as a naked chef."

    play sound s_sigh

    show bg narika_waitress7 at top with dissolve
    
    "Narika heaves a deep sigh, avoiding eye contact as you exit her sensitive pussy."
    
    narika "You... You're the worst..."
    
    "Is she really angry at you, or...?"

    scene black with fade

    $ MC.change_prestige(3)
    "Keep training Narika in different jobs until she is ready to join your brothel."

    return

label narika_masseuse():
    scene black with fade

    you "Looks like Narika is working as a masseuse today... Let's see how she's doing."

    play sound s_surprise

    show bg narika_masseuse1 at top with fade

    narika "M-Master [MC.name]? You're not supposed to be in this area... It's for customers..."

    you "Why, as the owner, I need to make sure everything is ready to welcome our dear customers! Think of it as quality control."

    narika "Quality... What?"

    you "For instance, what's that you're wearing? A one-piece swimsuit? It's not the most customer-friendly outfit..."

    narika "B-But, I had nothing else appropriate to wear..."

    you "I mean, at least you could show a little skin. Customers won't pay if they think you're just a girl in a school swimsuit."

    you "I mean, they will totally pay for that, but you can make it more interesting..."

    narika "I don't get it..."

    you "Tss... Like that, see?"

    show bg narika_masseuse2 at top with dissolve

    play sound s_scream

    narika "Eeek!" with vpunch

    you "Now, that's better! A lot more sexy, that way."

    narika blush "B-B-But... Everyone can see my... My..."

    you "Your what?"

    show bg narika_masseuse3 at top with dissolve

    play sound s_scream_loud

    narika "AAAAH!" with vpunch

    you "Haha, it's fun, the fabric is nearly disappearing in your slit! It really shows off the shape of your labia!"

    play sound s_ahaa

    narika "I-I don't know what, aaahaa, what that means!" with vpunch

    play sound s_moans_quiet

    you "It means you're beautiful down there."

    show bg narika_masseuse4 at top with dissolve

    narika "R-Really?"

    you "Sure. I have seen lots of pussies, and let me tell you, yours looks amazing."

    play sound s_aah

    narika "Is that even a compliment... Aahaa!" with vpunch

    you "Let's go inside... We can continue the lesson before the customers arrive."

    narika "..."

    play sound s_dress

    show bg narika_masseuse5 at top with fade

    $ m = MC.name[0]

    narika blush "[m]-[MC.name]... It's... So big... Can it really...?"

    you "Only one way to find out!"

    show bg narika_masseuse6 at top with dissolve

    play sound s_scream

    narika "Aaaah! [emo_heart]" with vpunch

    "Peeling her swimsuit aside, you expose her snatch, pushing the tip of your cock inside."

    you "Hmmm... You're nice and tight, just the way I remembered."
    
    play sound s_mmh

    show bg narika_masseuse7 at top with dissolve
    
    narika "You're out of control... Mmmh..."
    
    you "Are you going to stop me?"
    
    narika "..."
    
    you "I didn't think so."
    
    show bg narika_masseuse6 at top with dissolve
    
    play sound s_surprise
    
    narika "AAAAH!" with vpunch
    
    "You start rocking your hips, slowly sliding your dick in and out of her."
    
    play sound s_moans_short
    
    narika "Ah, ah, ahh... Mmmmh..."
    
    "Narika is breathing heavily, trying to adjust to your size."
    
    narika "Is it... All in...?"
    
    "You can hear curiosity in her voice, in spite of herself."
    
    you "Oh no, not yet. We're only halfway there."
    
    narika "N-No way-"
    
    play sound s_scream_loud
    
    narika "AAAAAAH!!!" with vpunch
    
    you "Now, it's all in."
    
    narika "You're too big... I can't..."
    
    you "What is it, Narika?"
    
    "Narika's pussy squeezes your cock tight, but you keep pushing in, stretching her pussy walls from the inside."
    
    narika "Aaaaaaah!" with vpunch
    
    you "What, can't take it? Are you too soft?"
    
    show bg narika_masseuse8 at top with dissolve
    
    narika "I'm not... Soft..."
    
    you "Oh yeah? You think you can keep up?"
    
    narika "I, uhng..."
    
    "She grits her teeth, but her eyes defy you to go further."
    
    "You push on, enjoying the way her pussy muscles struggle to expel you as you pump your shaft inside her."
    
    play sound s_moans
    
    narika "Ah, ah, ahh, aaah, aaaaaah!" with vpunch
    
    "In spite of her inexperience, Narika seems determined to keep up. She even starts to rock her hips slightly, slowly matching your rhythm."
    
    you "Hmmm, that's more like it!"
    
    "You hear some noise coming from the corridor. It seems some early customers are already beginning to show up."
    
    you "Hear that? I think some customers may be on the verge of walking in on us."
    
    show bg narika_masseuse7 at top with dissolve
    
    play sound s_surprise
    
    narika "N-No! They can't see me... Like that!"
    
    you "And why not? I told you it would do you good to show more skin. It's kind of an extreme version of that."
    
    narika shy "B-B-But... We're... Making love!"
    
    you "Hahahah, we're just fucking, Narika, it's different."
    
    narika "F-Fucking?"
    
    you "Yup."
    
    narika "B-B-But, isn't it something only lovers do?"
    
    you "Oh, sweet child... Anyone can fuck anyone, you shouldn't be so uptight about it."

    narika "S-So... We're not... Lovers?"

    you "Of sorts, if you want to call it that... But first and foremost, we're just having fun."

    narika blush "I-I'm not... Aaaah!" with vpunch

    "You pick up the pace, thrusting harder inside Narika."
    
    play sound s_moans
    
    narika "Ah, ah, aah!" with vpunch
    
    "Her pussy is gushing juices now, as she tries to match your pace."
    
    you "Don't even bother denying it, your body is craving for more."
    
    narika "..."
    
    you "You know, the first time I saw you, I knew you were hiding your true feelings behind a cold facade. I knew you had to a lot going on under the surface."
    
    narika "Ngh..." with vpunch
    
    "You pound Narika's pussy as you continue your monologue."
    
    you "I could see you were a girl who was craving for attention, a little princess who wanted to be pampered. But there is another side to you."
    
    narika "Ah, aah, ahh! Aaaaaaah!" with vpunch
    
    "You feel Narika's pussy clenching harder, signaling that she's close to climax."
    
    you "Oh, look, I think the customers are coming in!"
    
    narika "N-No! I don't want them to see me like that! A-Aaah!" with vpunch
    
    show bg narika_masseuse6 at top with flash
    
    "Narika struggles to regain control of herself, but her body betrays her as the mere thought of being found out sends her over the edge."
    
    show bg narika_masseuse9 at top with doubleflash
    
    play sound s_orgasm
    
    "Narika moans loudly, her pussy tightening around your cock in a series of spasms, sending you over the edge as well."
    
    show bg narika_masseuse10 at top with flash
    
    you "Bwahaha, just kidding, it was only Sill who's checking if the rooms are clean..."
    
    narika "Aaaah..."
    
    sill sad "M-Master??? What are you doing? I just washed that bench less than an hour ago!!!" with vpunch
    
    you "Well, it's good you got some practice, because you need to do it all over again!"
    
    you "And on the double. Customers will pour in any minute now."
    
    sill "And what about her? Is she going to help?"
    
    you "Narika here? Oh no, she's been through enough for today. Leave her be."
    
    "You remove your cock from Narika's pussy, gently laying her down on the bench before leaving."
    
    sill "Eeewww! And now there's cum leaking all over the place!" with vpunch

    scene black with fade

    $ MC.change_prestige(3)

    "Keep training Narika in different jobs until she is ready to join your brothel."

    return

label narika_geisha():
    scene black with fade

    narika shy "Come, Sir, err, I mean, dear customer..."

    narika "Please follow me to the chashitsu, the tea house... The tea ceremony will start shortly."

    "Ruffian" "Oy! I don't care about your stupid ceremony, kid! Shalia spit on it!"

    show bg narika_geisha1 at top with dissolve

    play sound s_dress

    "Ruffian" "Is this a whorehouse or what? Are you just here to serve tea and give flowery speeches?"

    play sound s_surprise

    narika blush "S-Sir, what are you doing??"

    "Ruffian" "What's it look like I'm doing? Checking the quality of the goods, that's what!"

    narika "B-But, I'm just a maiko in training... We have a no-touching policy..."

    "Ruffian" "Yeah, fuck that. You think that means anything in a place like that?"

    narika "But Sir..."

    "Ruffian" "Shut the fuck up, you little slut! You don't want me to hurt your pretty little face, do you?"

    narika "..."

    show bg narika_geisha2 at top with dissolve

    narika "(Damn, I could snap that fool's neck in a split second... But I need to behave, I'm only just starting to find my footing here...)"

    "Ruffian" "Eheheh, I like them small titties..."

    narika "(I just have to endure this for now... At least he's not...)"

    play sound s_dress
    pause 0.2
    play sound2 s_surprise

    show bg narika_geisha3 at top with dissolve

    narika "Ah!" with vpunch

    "Ruffian" "Ah yes, show me more..."

    narika "S-Sir!"

    "The gruffy customer tugs at her kimono, exposing her underwear. His grabby hands resume fondling Narika."

    narika "(This is bad... That guy is trouble...)"

    "Ruffian" "Eheheheh, what's that? Such plain underwear... You sure you're a hooker?"

    show bg narika_geisha4 at top with dissolve

    narika "I-I'm not!!!" with vpunch

    "Ruffian" "Whatev's, girly... I'm enjoying touching your hot body just the same..."

    narika "(W-Why is it that I can't shake that guy's off? I can kill a dozen ninja in a fight, but when big strong hands are on me... I feel powerless to stop it?)"

    "Ruffian" "Your nipples are perking through your bra... Eheh, aren't you a sensitive little kitty?"
    
    narika "Kkkh..."

    play sound s_dress

    show bg narika_geisha5 at top with dissolve

    "The customer unzips his pants, sliding his erect cock between Narika's legs."

    play sound s_scream

    narika "N-No!!! Sir! That's going too far!!!"

    "Ruffian" "Oh come on, don't be such a buzzkill, Miss! You knew this was coming..."

    narika "(This is really bad... I need to do something before this escalates any further...)"

    "Ruffian" "We gots all the time in the world... I'm 'a make you a real woman."

    narika "(I've always refused to use {i}that kind{/i} of Kunoichi techniques, but... This is a force majeur...)"

    "Slowly, deliberately, Narika contracts her pussy, her lips clenching the ruffian's dick through the panties' fabric."

    "Ruffian" "Ohohohoh!!! What is that! It feels incredible..."

    "Ruffian" "How are you even doing that? I must have underestimated you..."

    narika "(So... My instructor told me I could use this to deliver the finishing blow... It was all just theory, though, I've never even used such a technique...)"

    narika "(Forgive me, Master [MC.name], for what I'm about to do, but I must end this now...)"

    "Narika steels her resolve, and activates the secret technique."

    narika angry "HA!!!" with vpunch

    play sound s_splat

    with flash

    "Ruffian" "OW!!! OHOHOHOHOHOHOH!!!"

    show bg narika_geisha6 at top with doubleflash

    "The customer's dick erupts like a geyser, smearing Narika's legs and panties with thick semen."

    with flash

    "Ruffian" "In-In..."
    
    "Ruffian" "INCREDIBLE!!!"

    "Ruffian" "I've never felt anything like this! I thought I was about to die, and then it was so good!"

    show bg narika_geisha7 at top with flash

    narika "(Oh no... Did I mess up that technique? Or did I misunderstand the instructor when she told us it would 'finish' him?)"

    "Ruffian" "Ohohoh, I'm in heaven now..."

    narika "D-Dear customer, I'm glad you had your... fun. Now, I need to wash, can you please let me-"

    play sound s_dress

    show bg narika_geisha8 at top with dissolve

    pause 0.2

    play sound s_scream

    narika "AAAAH!!!" with vpunch

    "The customer's callous hands rip off her panties and bra."

    "Ruffian" "Oh no, we're just getting started... You're all mine now! I'm going to enjoy that bewitching pussy night and day from now on!"

    narika "N-No, stop it! I will call my... My boss..."

    if MC.playerclass == "Warrior":
        "Ruffian" "What, that loser, the old washed-up veteran? I can take ten guys like him any day! I bet he's never even been in a real fight."
        $ s = s_punch
    elif MC.playerclass == "Wizard":
        "Ruffian" "That effeminate loser with his robes and his walking stick? You think I'm scared of the tacky magic tricks he uses to impress the simple-minded morons?"
        $ s = s_fire
    elif MC.playerclass == "Trader":
        "Ruffian" "What, that chatty braggart and his pet lizard? He reminds me of a loser kid I was bullying, I pushed him down into the latrines and nailed his pet to the door..."
        $ s = s_roar

    "Ruffian" "If he dares to interrupt, I'll give him the hiding of his life. I'll screw down his head and shit down his neck. I'll-"

    play sound s_whistle

    you "Hey, dickhead." with vpunch

    "Ruffian" "Uh?"

    you "Get your filthy hands of my girl. The sign says 'NO TOUCHING'..."

    if MC.playerclass == "Warrior":
        play sound s_punch
        "*PUNCH*" with vpunch
        "Ruffian" "Ouch!!!"

    elif MC.playerclass == "Wizard":
        play sound s_fire
        "*BLAST*" with flash
        "Ruffian" "Aaaarh!!!"

    elif MC.playerclass == "Trader":
        play sound s_roar
        "*ROAR*" with vpunch
        "Ruffian" "G-G-Get that thing away from me!!!"

    you "... without paying. It says, 'NO TOUCHING {i}without paying{/i}'."

    "Ruffian" "GRRR... So you wanna dance, motherfucker?"

    play sound s_sheath

    "The customer takes out a nasty looking knife from Arios-knows-where."

    you "Narika, please."

    narika "W-With pleasure, Master..."

    play sound s_punch
    pause 0.3
    play sound2 s_punch
    pause 0.2
    play sound3 s_punch
    pause 0.1
    play sound s_punch
    pause 0.1
    play sound2 s_punch
    pause 0.2
    play sound3 s_punch
    pause 0.1
    play sound s_punch
    pause 0.3

    "*punch* *kick* *slap* *slap* *elbow* *roundhouse kick*" with vpunch

    play sound s_wscream

    "Ruffian" "AAAAAAAAaaaaaaaaaaa{size=-4}aaaaaa{size=-4}aaaaaa{size=-4}aaaaaahhh" with vpunch

    "The customer is kicked high above the rooftops, disappearing into the distance until he is just one tiny spot among the night's stars."

    you "Are you okay?"

    narika "..."

    narika "That nasty man... He touched me, he... did his thing... It felt so gross, and weird..."

    narika shy "I... I even peed myself... *voice breaks*"

    you "Oh, honey... It's not pee..."

    "You insert an expert finger inside her exposed snatch, scooping up a bunch of love juice."

    you "I can't believe you... Did being assaulted turn you on, or giving is it beating this guy to a pulp?"

    narika blush "..."

    narika "Both..."

    you "Hahaha, at least you're honest."

    you "I can't really leave you like this, though, can I?"

    narika "..."

    you "Let's make the best of this unexpected foreplay."

    show bg narika_geisha9 at top with fade

    play sound s_mmh

    narika "Oh, Master..."

    you "I think you're getting the hand of this place, Narika."

    narika "B-But... It's all so new to me... The girls, the outfits, the customers... The s-sex..."

    you "And yet look at you, you're moving your hips in rythm with mine..."

    narika "I c-can't help it, it's like there's this fire inside me... I don't understand it..."

    you "You like sex, Narika, it's only natural. It's the most pleasurable thing in the world. I can guide you down the right path."

    narika "I-Is it like... Kunoichi training?"

    you "Oh, it's a lot more fun than that."

    narika "..."

    "Increasing your pace, you keep fucking her tight pussy, and she hangs onto you for dear life."

    show bg narika_geisha10 at top with dissolve

    play sound s_scream

    narika "Oh! ah! Aaah!" with vpunch

    play sound s_moans
    
    narika "Oh yes, yes... That's the spot... [emo_heart]"

    "Spreading her legs wider, you find just the right angle, sending shivers down her spine every time you pound into her."

    narika "Aaaaah!!!" with vpunch

    narika "Oh no!!! If you do that, I will..."
    
    show bg narika_geisha11 at top with flash

    play sound s_screams

    narika "OH!!! AAAAH!!! AAAAAH!!!"

    play sound s_orgasm_fast

    narika "You both cum at the same time, Narika clinging to you as you spurt your warm seed inside her."

    show bg narika_geisha12 at top with flash

    narika "A-Amazing..."

    you "Wow... You're okay?"

    narika "I didn't know... There was such a... feeling..."

    you "This is just the beginning. If you pay attention to my teachings, soon you will..."

    you "Narika? Narika?"

    "It looks like Narika passed out in the middle of your lecture."

    "You are relieved to hear her snore, though. It's just fatigue."

    "Carrying her back to her room, you reflect back on her progress since you brought her here."

    you "I'm surprised how well she's adjusting. She really is a quick learner."

    scene black with fade

    $ MC.change_prestige(3)

    "Keep training Narika in different jobs until she is ready to join your brothel."

    return

label narika_dancer():
    scene black with fade

    play sound s_crowd_cheer

    "Customers" "Whoohoo!!! *Cheers*"

    narika school "Thank you, thank you..."

    man "The show was amazing! Can you do the split once more?"

    man2 "And the cartwheel! With that short skirt of yours, it was just... Hmmm..."

    "The customers really enjoyed Narika's dance show."

    narika "Fufufu, thank you, my adoring fans! *blush*"

    narika "(I really am getting quite popular now...)"

    narika "(I've been here for a while already. I hear there are customers that come just for me...)"

    narika "(Why does it make me feel so... Tingly?)"

    man2 "Here, Narika-chan! I brought you flowers!"

    narika "Flowers? For me? Oh, thank you... *swoons*"

    man "Can I get your autograph?"

    "Third man" "I'll buy your used underwear! Name your price!"

    narika "(Gee, I have never been this popular with boys, not even in school... It's intoxicating...)"

    "Fans" "Narika-chan, we are your biggest fans! *together*"

    narika "Ahaha... Would you like me to give you a tour backstage?"

    "Fans" "YES!!!" with vpunch

    man "A tour with Narika-chan! This is the best day of my life!!!" with vpunch

    narika "(Why are my fans so creepy? But I have to entertain them... That's the price of being an idol I guess.)"

    "Narika led the three guys to the changing room. She didn't know what to make of the growing tingling sensation that was coursing through her body."

    with fade

    man "Narika-chan, can I ask you something?"

    narika "Sure, sure, ask me anything, I'd be nothing without my fans..."

    narika "(Why am I saying these corny idol lines all of a sudden?)"

    man "Can you sign your autograph on my skin? You know, like a tattoo that comes from Narika-chan?"

    narika "Oh, well, why not. Let me find a pen..."

    play sound s_dress

    show bg narika_dancer1 at top with dissolve

    narika blush "W-What are you doing?"

    man "You said you would sign your autograph on my body, right? I want it here."

    "Other men" "Do it, Narika-chan! Do it!"

    narika "B-But... I can't, err... write on it... I mean, it's too soft..."

    man "Oh, right!"

    man "You need to help me get it harder first."

    "The man guides Narika's hand towards his cock. She is surprised at his boldness, but also aroused."

    narika "W-Well, I suppose I can help out a fan..."

    "Narika starts stroking the man's cock, under the watchful eye of the others."

    man2 "Oooooh! I'm so jealous!"

    man "This is so good! Aah!!!" with vpunch

    show bg narika_dancer2 at top with dissolve

    "Acting even more bold, the man pushes his cock in Narika's face, brushing the head against her lips."

    narika "!!!" with vpunch

    man "Please, Narika-chan, lick it a little... It would make me so happy..."

    narika "(This is getting out of hand... Literally...)"

    "In spite of herself, Narika soon finds herself licking the tip of the man's dick, tasting his sweat and pre-cum."

    narika "(W-Why do I allow myself to be debased by these fans? And why does it feel so... hot?)"

    man2 "Look at that!!! Narika-chan is really doing it!"

    "Third man" "Oh no, am I dead? Am I in heaven?"

    man "Oh, Narika-chan, now I can die a happy man... I-"
    
    with flash
    
    "Aaaah!!!"

    show bg narika_dancer3 at top with doubleflash

    "As Narika wraps the man's cock with her lips, he cums suddenly, spilling a wad of salty cum in her mouth."

    narika "Hnnng..."

    show bg narika_dancer4 at top with flash

    "Gasping for air, Narika lets a mix of drool and cum drip down from her lips."

    man "T-This is much better than an autograph! Thank you, Narika-chan!"

    narika "Uhn... You're... You're welcome..."

    show bg narika_dancer5 at top with dissolve

    man2 "What about us? It's our turn now!"

    "Third man" "Yes! It wouldn't be fair to do it just for them!"

    narika "(I... I can't be seen playing favorites with my fans, it would be a bad look...)"

    narika "F-Fine... Just wait in line, or something..."

    man2 "Me first!" with vpunch

    "Third man" "No, me!!!" with vpunch

    narika "Gee, calm down, boys... I've got two hands, I'll do my best to help you both..."

    show bg narika_dancer6 at top with dissolve

    narika "Here, happy now?"

    man2 "Oooh, this is good!!!"

    "Third man" "I don't believe it! This is even better than the time I got the special edition calendar of BK48!"

    man "I'm ready to go again! Show me something to get me started."

    play sound s_dress

    show bg narika_dancer7 at top with dissolve

    "The man forcefully lifts Narika's top to reveal her tits, but she is beyond caring. She already started licking the other customers' cocks."

    narika "Please, dear fans... Look at my body... And enjoy yourselves..."

    man2 "Oh, Narika-chan, your tits are beautiful!!!"
    
    "Third man" "She's licking it! I'll never wash my dick again!!!"
    
    "The fire in Narika's body is now in full heat, and she doesn't resist the turn of events."
    
    narika "(Why am I doing this?)"
    
    narika "(Oh, who am I kidding, it's just so fun...)"
    
    show bg narika_dancer8 at top with flash
    
    "As Narika licks and sucks the customers, they release their cum on her face and chest."
    
    with doubleflash
    
    man2 "Oh, Narika-chan! You are so beautiful with cum all over your face!!!"
    
    "Third man" "I could watch this forever! I'll burn my eyes out after they have been so blessed!!!"
    
    narika "Please don't..."
    
    man "I can't take it anymore! Narika-chan, I'll..."
    
    show bg narika_dancer9 with doubleflash
    
    "The customer cums on Narika's face and hair, splashing her face with his seed."
    
    "As the cum drips down Narika's body, she feels a sense of liberation, of letting go of her inhibitions."
    
    show bg narika_dancer10 with dissolve
    
    narika "(I think Master [MC.name] was right, I needed to be shown the way... But now that I am on the path, I can keep walking it on my own.)"
    
    "Narika's journey of self-discovery has only begun, and she's ready for more."
    
    narika "(So far I've used my body for fighting and strength... But it can also bring joy and pleasure, to me and to others.)"

    narika "(Isn't that a better calling?)"

    scene black with fade

    $ MC.change_prestige(3)

    "Narika is now fully trained in all jobs. Please wait for events to unfold."

    $ calendar.set_alarm(calendar.time+1, StoryEvent("narika_broken", type="night"))

    $ calendar.set_alarm(calendar.time+56, StoryEvent("narika_fans_return", type="night"))
    return

label narika_fans_return(): # runs in a loop until the event happens

    python:
        for girl in MC.girls:
            if girl.pack_name == "Narika Shihoudou" and girl.original and girl.job == "dancer":
                break
        else:
            girl=None

    if girl:

        "Narika was just ending her dancing shift when she heard a familiar voice call out her name."

        man "Narikaaaaaa-chan!!!"

        narika school "?"

        man2 "It's us!!! Your biggest fans! Do you remember us?"

        "Narika gives them a blank stare."

        "Third man" "You showed us around backstage! You gave us, erm... Special service!"

        narika "Oh, it was you guys!"

        show bg narika_dancer10 at sepia
        with flashbackin

        narika "(That was the moment... I realized I could do this...)"

        man "It was awesome, Narika-chan! I haven't slept for weeks, daydreaming about this!"

        man2 "I masturbate every day thinking about it! I even made a clay figure of you, and..."

        narika "Enough, enough! (Gee, you idol fans are still as creepy as ever...)"

        "Third man" "Would you show us around backstage today? Pretty please?"

        man "We'll pay extra!"

        narika "Well..."

        "Together" "Narika-chan, we beg you!!! *down on their knees and hands, imploring her*"

        narika "*sigh* All right, fine... Just follow me. But no inappropriate touching, okay?"

        scene black with flashbackout

        show bg narika_dancer9 at top with doubleflash

        narika blush "Eeeek!!! It's in my hair!"

        narika "So much for me saying 'no touching'..."

        $ MC.change_gold(300)

        show bg narika_dancer10 at top with flash

        man "Thank you so much, Narika-chan!!!"

        man2 "Now I can masturbate to this for many more months!"

        "Third man" "But, Narika-chan..."

        narika "What..."

        "Third man" "I heard the idols from BK48, they let their fans go all the way you know..."

        man "It's true! I heard they sometimes treat several of their fans at once!"

        man2 "Friends, don't you dare to compare Narika-chan to these BK48 sows..."

        narika "All the way? Hmph, do they think it makes them better or something? I bet they just lie there like a dead tuna..."

        man "You're right, you don't have to do it to be awesome!"

        man2 "Yes, exactly! You're perfect as you are, even if you can't perform at their level!"

        "Third man" "Sure, I mean... BK48 is something else, it's not a fair comparison..."

        narika angry "HOLD ON A MOMENT!!!" with vpunch

        narika "You lowly worms think I'm not on par with these fat vulgar bitches from BK48?!?" with vpunch

        man "N-N-No..."

        man2 "W-We wouldn't dare..."

        "Third man" "I think we're going to now... (She's scary!!!)"

        narika "YOU THREE STAY RIGHT HERE!!!"

        play sound s_dress

        show bg narika_dancer11 at top with fade

        man "N-Narika-chan, you don't have to force yourself..."
        
        narika "Hmph. I'm not forcing myself, I'm just doing my duty as an idol. You can't leave here thinking someone else gives better fan service."
        
        man2 "Narika-chan, you're so cool! [emo_heart]"
        
        "Third man" "Ooooh, Narika-chan, my heart is going to beat out of my chest!!"
        
        narika "Please, dear fans, look at me and only me! Your... Queen."
        
        man "O-Of course..."
        
        man "Queen Narika!!!"
        
        man2 "I am so lucky to be in the presence of the divine!!"
        
        "Third man" "Aaaah, I'm going to faint!"
        
        show bg narika_dancer12 with dissolve
        
        "Narika slowly lowers herself on the customer, his cock disappearing inside her wet pussy."
        
        man2 "OH MY GOD!!!" with vpunch
        
        "Third man" "I can't believe my eyes! Narika-chan is truly a goddess!!!"
        
        narika "Ah, ahh! Don't start moving until I tell you to!"
        
        man "Y-Yes, my Queen! I will obey!"
        
        narika "That's right, you will obey me! Now thrust your hips! Hard!"
        
        man "As you wish, Queen Narika!" with vpunch
        
        play sound s_mmh
        
        show bg narika_dancer13 with dissolve
        
        
        narika "Hmmm, yes..."
        
        "The man starts pounding Narika who bounces up and down his cock, while the others look at her with fascination."
        
        narika "(I could get used to this...) Fufufu..."
        man "I'm in heaven... I... Ugnh..."
        
        show bg narika_dancer14 with doubleflash
        
        play sound s_scream
        
        narika "AAAAH!!! [emo_heart]" with vpunch
        
        "The man cums suddenly, filling Narika's pussy with his seed."
        
        man2 "It's so hot!!! I can't hold it any longer!"
        
        "Third man" "Me neither! This is beyond my wildest dreams!!!"
        
        show bg narika_dancer15 with doubleflash
        
        man2 "*grunt*"
        
        "Third man" "Aaaarh!"
        
        "The men all cum together on Narika's body and face."
        
        show bg narika_dancer16 with flash
        
        narika "Aaaaah, you guys came so much!"
        
        narika "(The smell of men's cum... It's overpowering...)"
        
        man "Am I dead? I think I'm dead..."
        
        man "It's okay, I can die happy now... *pass out*"
        
        man2 "I-I'm spent..."
        
        "Third man" "But it's not fair! How come he got to cum inside you, when I didn't?"
        
        narika "Well, he was first in line..."
        
        "Third man" "But what about me?"
        
        narika "He's passed out now, you're going to have to wait for him to wake up..."
        
        narika "His dick is still stuck inside me."
        
        "Third man" "But I don't want to wait another second! I'm hard as fuck, Queen, it's painful!"
        
        narika "Then wh-"
        
        play sound s_splat
        
        show bg narika_dancer17 with dissolve
        
        play sound s_scream_loud
        
        narika "AAAAAAAH!!!" with vpunch
        
        narika "Y-You bastard... You just put it in my asshole with even asking..."
        
        "Third man" "I-I'm sorry, I don't know what came over me, Queen..."
        
        "Third man" "I'll come out right away... This was so inappropriate, I don't know how you can forgive me..."
        
        narika "Ah, aah..."
        
        "Narika moans as he tries to remove his dick."
        
        "Third man" "Q-Queen? I can't remove my dick? It's too tight!"
        
        show bg narika_dancer18 with dissolve
        
        narika "That's right. Because I won't let you."
        
        "Narika is using the muscles of her ass to clench onto the man's dick."
        
        narika "I have yet to be satisfied, as that other chump came too early."
        
        narika "So you're going to make me cum now..."
        
        
        "Third man" "I-I'll do anything for you, Queen Narika! Just tell me what I can do!"
        
        narika "I want you to fuck me in the ass. Do it now!"
        
        "Third man" "Yes, my Queen! As you wish!" with vpunch
        
        play sound s_mmh
        
        with vpunch
        
        "Narika's body rocks back and forth as the customer pushes his cock in and out of her asshole."
        
        play sound s_aah
        
        narika "Aaah, yes... [emo_heart]" with vpunch
        
        play sound s_moans
        
        "She scoops some cum off her body and licks it off her fingers as she looks back at the customer."
        
        man2 "A-Amazing!!! This is the power of a true idol!!!"
        
        "Third man" "O-Of course! No one in the world can compare to Narika-chan!"
        
        "Third man" "OOOOOOH!!!!" with vpunch
        
        play sound s_orgasm
        
        show bg narika_dancer19 with dissolve
        
        narika "Ooooh!!! YES!!!" with doubleflash
        
        "The customer cums, releasing his seed inside Narika's ass, while she reaches her climax as well."
        
        with flash
        
        "Third man" "*pant, pant*"
        
        "The customers are in shock, looking at her as if she was a goddess."
        
        "Narika feels a sense of accomplishment, as if she just conquered an impossible challenge."
        
        narika "(I can please any number of men... Nothing is beyond my power now...)"
        
        narika "I'll become the best idol ever and I'll make all of my fans happy!!!"
        
        "Customers" "Yes, my Queen!!!" with vpunch

        $ MC.change_gold(1200)
        $ girl.change_mood(100)
        $ girl.raise_preference("group", 500)
        $ girl.change_rep(5)
        
        scene black with fade
        
        man "*waking up* Ugh... Did I miss anything?"
        
        $ MC.change_prestige(game.chapter)
        
        $ clear_event("narika_fans_return")

    return

label narika_broken:

    scene black with fade
    show expression brothel.master_bedroom.get_pic() at top
    with dissolve

    show narika normal with dissolve

    narika "Master, you wanted to see me?"

    you "Yes, I wanted to congratulate you on your progress so far. I think you are now ready to join us."

    narika blush "Well, I didn't know what to expect at first... But I think I can hold my own."

    you "You sure can. The girls said you've been good help."

    narika "Well, I've tried all the side jobs... but I can't just be a supporting actress. I need to lead!"

    you "Meaning?"

    narika "There's one last job I haven't tried... The real stuff. You know."

    you "Right."

    menu:
        you "In that case..."

        "I will try you out myself":

            $ renpy.block_rollback()

            you "You're going to welcome me as if I was a customer, and give me the best service you're capable of."

            you "If I am satisfied with you, I will let you join [brothel.name]."

            narika "O-Okay..."

            scene black with fade
            show bg narika_sex1 at top with dissolve

            narika blush "W-Welcome, dear customer..."

            you "Don't be so formal... You can call me... Daddy."

            narika "D-Daddy? Why?"

            you "Many customers ask for this. Don't you know step-relations are all the rage now in smutty dime novels?"

            narika "Alright... Welcome home, Daddy."

            you "Still not wearing a bra... I like that."

            narika "Do you like my titties, Daddy?"

            you "Sure, hehehe..."
            
            "You pinch her nipples."
            
            narika "Ah!" with vpunch
            
            you "Perky as always... Let's check what else you have for me."
            
            play sound s_dress
            
            show bg narika_sex2 at top with dissolve
            
            "You remove her panties, spreading her knees apart to get a good view of her pussy."
            
            "Her pussy is already wet."
            
            you "It looks like you've been a naughty daughter..."
            
            "Narika is embarrassed to be exposed in such a manner, but also feels a sense of excitement."
            
            narika "S-Sorry, Daddy... I was thinking about you all day, and got turned on..."
            
            "Narika spreads her legs wider, inviting you to get closer."
            
            narika "I-If you look at me like this, I'll get even more excited..."
            
            you "Hehehe, what a dirty daughter. I'm going to have to punish you."
            
            "You lower your head towards her pussy and start licking it."
            
            show bg narika_sex3 at top with dissolve
            
            narika "Aaaaah!!! [emo_heart]" with vpunch
            
            you "Just as I thought, you're leaking all over the place, you dirty girl!"
            
            narika "I-I'm sorry, Daddy! It's just... It's my first time..."
            
            you "Don't lie, Narika, customers won't like that."
            
            narika "I-I mean, it's my first time... As a... A..."
            
            you "Yes?"
            
            narika "Whore..."
            
            "She lets the word roll off her tongue, as if it had a deeper, almost mystical meaning."
            
            "As the words come out of her mouth, Narika feels as if she has been reborn."
            
            you "I like the new you... Let me show you my appreciation."
            
            show bg narika_sex4 at top with dissolve
            
            play sound s_aah
            
            narika "Aaaaah!" with vpunch
            
            "You resume licking her pussy, while she leans back and grabs the sheets with her hands."
            
            "Spreading her pussy lips apart, you push your tongue inside, tasting her sweet love juice."
            
            narika "Daddy! Oh, Daddy!"
            
            play sound s_ahaa
            
            "Narika is trembling, close to cumming already."
            
            narika "Ahhh! I-I'm too sensitive, Daddy!"
            
            you "Let's not rush to the finish line..."
            
            "You stop, and she looks at you with a hint of disappointment."
            
            "Before she can beg you to continue, however, you push her down on the bed."
            
            show bg narika_sex5 at top with dissolve
            
            you "I think my slutty daughter's pussy is ready to take my dick..."
            
            narika "Y-Yes, Daddy! Please use me as you like!"
            
            play sound s_dress
            
            "You pull out your cock and it springs to attention."
            
            you "Make sure to satisfy me fully, and you will have a place of honor among my girls."
            
            narika "S-Sure, Daddy. I'll do my best."
            
            "You put your cock between her legs and start thrusting."
            
            show bg narika_sex6 at top with dissolve
            
            play sound s_mmh
            
            narika "Oh, Daddy, Daddy!!!"
            
            you "Your pussy is so tight, and yet so easy to move into..."
            
            "You grab her ass, pulling her towards you as you lodge your cock deeper inside."
            
            show bg narika_sex7 at top with dissolve
            
            play sound s_aaah
            
            narika "Oh, Daddy... You're so big..."
            
            "Her pussy is clenching around you as she bites her lips."
            
            play sound s_moans
            
            "Narika is moaning, looking at you as she gets filled up with your dick."
            
            you "Narika, my slutty daughter... You feel so good!"
            
            you  "I'm going to have to fuck your pussy now... Don't mind me if I'm being rough."
            
            narika "Daddy, I want it rough..."
            
            "You start fucking her in earnest, pushing your cock in and out of her pussy."
            
            show bg narika_sex8 at top with dissolve
            
            play sound s_surprise
            
            narika "Aaaah!!!" with vpunch
            
            narika "Oh yes, Daddy, just like that!!!"
            
            "You fuck her hard for some time, but then you slow down your pace."
            
            narika "(It feels so good, but... Why is he holding back?)"
            
            "She looks at you and realizes what she has to do."
            
            narika "Daddy, you're teasing me... Please don't hold back on me..."
            
            you "You can do better than that... Don't just take it."
            
            you "You're a whore now, remember? Act like it!"
            
            "You pick up the pace again, making her moan harder."
            
            narika "Ah, Daddy!!!" with vpunch
            
            "She starts rocking her hips back and forth, making your cock hit her deeper regions every time you push into her."
            
            narika "Take me, Daddy! Fuck me hard!" with vpunch
            
            "You start feeling the onset of your orgasm."
            
            you "I'm getting close, Narika. Do you want to be filled by my cum?"
            
            narika "Yes, Daddy! Please fill me up!"
            
            you "Then you have to deserve it. Your move."
            
            "You stop pounding her, waiting with your dick buried halfway in."
            
            "Narika takes a few moments to collect herself, then starts fucking you on her own."
            
            play sound s_scream_loud
            
            narika "AAAAAH!" with vpunch
            
            "She slams her ass against your crotch, taking your dick deeper every time."
            
            "She uses all of her muscles to make you feel good. You can feel her pussy walls tightening around your shaft."
            
            play sound s_scream
            
            narika "Oh, Daddy! I'm gonna cum!" with vpunch
            
            with flash
            
            play sound s_orgasm
            
            "She orgasms, squeezing your dick with all of her might, sending you over the edge as well."
            
            you "Here it comes, Narika... Take it all!"
            
            show bg narika_sex9 at top with doubleflash
            
            "You spray your seed inside her pussy, reaching her deepest places."
            
            with flash
            
            "The sensation of your hot cum makes Narika orgasm again, milking every drop out of you."
            
            show bg narika_sex10 at top with dissolve
            
            play sound s_sigh
            
            narika "I came... Twice..."
            
            you "On your first day as a whore..."

        "I will summon some customers":

            $ renpy.block_rollback()

            $ cust = rand_choice(get_available_populations()).get_rand_name().capitalize()

            you "Your test will involve real customers. are you ready for it?"

            narika "..."

            narika blush "Yes, I am."

            you "Alright. Let me fetch some."

            scene black with fade

            "You ask Sill to find you two of the ugliest customers in the brothel."

            sill "Okay, Master [MC.name], but... Why?"

            you "I want to make sure that former spoiled little princess is ready to serve anyone."

            you "Plus, I have a feeling she might like some additional humiliation..."

            play sound s_maniacal_laugh
            you "Bwahahaha!!!"

            $ MC.good -= 2

            sill "Err... Okay..."

            show bg narika_broken1 at top with fade

            narika "Ooh, aah, aaah! Mister, you're so rough!!!" with vpunch

            "[cust]" "Osh, I like how you move, you little shlut!"

            narika "(That guy is old, fat and smelly... And he speaks with a slur...)"

            narika "(And he fucks me like I'm a dirty street hooker...)"

            narika "(Why am I getting so turned on by this???)" with vpunch

            "[cust]" "Kish me you bitshh!"

            "The customer licks the outside of Narika's mouth with his slithering tongue."

            narika "(Oh gosh, his breath smells like cheap alcohol and clove cigarettes... Disgusting...)"

            "Narika leans into the kiss, intertwining her tongue with the customer's, swallowing his dirty saliva."

            "She gets turned on by this humiliating act, and starts rocking her hips back and forth faster."
            
            "[cust]" "Oh, nishe... I really enjoy when you squeeje my cock like thish..."
            
            show bg narika_broken3 at top with dissolve
            
            narika "Ah, aah, ooh!!!" with vpunch
            
            "The customer grabs her ass, squeezing it hard as he keeps pounding her pussy."
            
            "She gets more and more aroused as the customer fucks her like a piece of meat."
            
            "[cust]" "You like the bells I put on your nippies? It jingles every time I shlam my cock into you, hahaha!"
            
            "Narika's face is red, and she is breathing heavily as he fucks her like a wild animal."

            play sound s_aaah

            narika "Aaah, ohh, aaaah!!!" with vpunch
            
            "Other customer" "Oy! The big man said I was gonna get a turn too! I'm still waiting!"
            
            narika "Aah, sorry... Aah..."
            
            "Other customer"  "I ain't gonna wait forever. Ready or not, here I come!"
            
            show bg narika_broken4 at top with dissolve
            
            play sound s_scream
            
            narika "NGGGH!!!" with vpunch
            
            "Other customer" "Oy, I'm coming in. don't mind me, eheheheh..."
            
            "The second man pushes his cock against her asshole, forcing his way inside."
            
            "The first man doesn't let it stop him, however, as he keeps pounding her pussy."
            
            narika "(This man is a pig just like the other one... But his dick... is so big...)"
            
            narika "(They're both so rough with me... I've never had anything like this happen to me before...)"
            
            "The second man's dick is so large that it struggles to enter her asshole."
            
            play sound s_splat

            "Finally, it gives way, and Narika is almost torn apart as the large man enters her from behind."

            play sound s_scream_loud

            narika "AAAAAH!!!"
            
            play sound s_chimes
            
            "The force of the insertion makes the bells on her nipples ring out loud."
            
            show bg narika_broken5 at top with dissolve
            
            play sound s_scream_loud
            
            narika "Oooh, it hurts!!!" with vpunch
            
            narika "(I can take pain... But this is so intense... My mind is going blank!)"
            
            "The two men start thrusting their cocks inside her, one filling up her pussy while the other is pushing its way inside her ass."
            
            play sound s_moans
            
            "She can't keep up with the pleasure she is feeling, and her moans of apin and pleasure start filling the air."
            
            "The first customer grabs her hair, pulling it back and forcing her to look at him."
            
            "[cust]" "I'm going to fill you up with semen. You could father my child, you lucky shlut! Eheheh..."
            
            narika "(T-Thank the gods for Sill's contraception magic...)"
            
            "Other customer" "I'm going to make your ass pregnant too, hahahaha!"
            
            narika "(Ow... They're as dumb as they are ugly...)"
            
            narika "(I'm being treated like a broken fucktoy by these disgusting men... And yet...)"
            
            play sound s_scream

            narika "I'm enjoying this... So much!" with vpunch
            
            "Other customer" "Unbelievable! Hear that, cousin?"
            
            "[cust]" "Yesh!!! Time for the big finissh!" with vpunch
            
            show bg narika_broken6 at top with flash
            
            "[cust]" "UUUGH!!!"
            
            "Other customer" "OHOHOH!" with doubleflash
            
            play sound s_orgasm
            
            narika "AAAAAH!!!!" with flash
            
            "Narika climaxes as the two men spray their load inside her pussy and ass."
            
            "Her orgasm makes her pussy squeeze the dick inside her, making the pig man cum harder."
            
            "The two men's faces are red from the strain, their smelly breath hot on Narika's neck."
            
            show bg narika_broken7 at top with dissolve
            
            narika sad "(Did all of this really happen...)"
            
            "She can feel their semen leak out of her holes."
            
            narika "(It's so warm, so disgusting... I love it...)"
            
            "[cust]" "I've been with a lot of whorjes in my day... In fact, I've only been with whorjes."
            
            "[cust]" "But you're the real shtuff."
            
            "Other customer" "Yeah, you're really a natural-born cum dumpster."
            
            narika "(How rude... But...)"
            
            narika "(Could it be true?)"

            $ MC.change_gold(400)

    $ MC.change_prestige(3)

    scene black with fade
    show expression brothel.master_bedroom.get_pic() at top
    with dissolve

    show narika normal with dissolve

    you "Congratulations. You passed the test with flying colors."
            
    narika "I always do, but... It's nothing like Kunoichi training. This one made me feel... Hmmm."
    
    you "You see, being a whore is not only about having sex with men."

    narika "It's not?"
    
    you "You were able to adapt to any situation to please a customer. And to find your own joy in doing so."
    
    you "That's what separates the best whores from the amateurs."

    narika "I see it now..."

    "You see new resolve on her face."

    narika "I always wanted to prove my superiority as a fighter. But the truth is, I wasn't really the best, because my heart wasn't into it..."

    narika "What I always craved was the admiration of others. But killing and stealing couldn't get me that."

    narika "This, on the other hand... It feels like something right and natural."
    
    narika "Something I could do to get genuine praise..."
    
    narika "And enjoy myself in the process."

    you "Narika, I am impressed. You're more than ready."

    narika "Of course I am! I shall be the number one whore in all of Xeros!"

    you "Haha, still competitive, I see! That's the spirit!"

    scene black with fade
    "Narika Shihoudou is now ready to join your brothel."

    $ girl = create_girl("Narika Shihoudou", force_original=True, level=10)

    call acquire_ninja(girl) from _call_acquire_ninja

    return


label c3_narika_arrested():

    "Suzume came back to report."

    show expression bg_bro at top
    with dissolve

    show suzume bend with dissolve

    suzume "Good news; that brat Narika is now in royal custody."

    you "Did the princess say anything?"

    suzume "Her interrogators whisked her away for questioning. From the look of things, I don't think we're likely to hear from her again."

    suzume "The Princess was more worried about the Mages' Guild than that Kunoichi girl, though. I'm not sure Narika was our mark."

    you "Oh well. At least we got a nice reward."

    $ MC.change_gold(2500)
    call receive_item(rep_item) from _call_receive_item_27
    $ game.set_task(None, "story3")

    scene black with fade

    "You have received a reward for capturing Narika Shihoudou."

    return

## End of Narika  events ##


## Mizuki story line ##

#!

## End of Mizuki  events ##


## Haruka story line ##

# Guard route #

label c3_haruka_guards():

    you "So... How do we go about this?"

    suzume "We could ask Kenshin to introduce us to prison's brass..."

    you "But what if she's in league with the abducters?"

    suzume "Then we don't tell her everything."

    suzume "Or... We could just wing it. Talk our way inside the Prison."

    you "What? I don't like the sound of that..."

    suzume "Come on! It'll be fun."

    you "Nothing about going to prison is 'fun'."

    menu:
        "How do you want to approach the Prison?"

        "Tell Kenshin":

            you "All right, let's visit Kenshin. As the Captain of the Knights, she's our best bet."

            scene black with fade
            show bg palace at top with dissolve
            play music m_kenshin fadein 3.0

            show kenshin with dissolve

            kenshin "You want to do {i}what{/i}?"

            you "Inspect the prison. Talk to the knights in charge. I have information of interest to them."

            kenshin "Then why don't you tell me that information immediately then? I can talk to them."

            you "Sorry, but this is confidential information. It's related to the Princess's assignment, you see..."

            kenshin annoyed "Again with that assignment! I'm the Princess's most loyal servant! There's no need to hide anything from me!" with vpunch

            "Kenshin's eyes spark with fury."

            you "Are you questioning the Princess's judgement?"

            kenshin "Grrr..."

            you "So, will you help me or not?"

            kenshin "You... You..."

            play sound s_sigh

            kenshin normal "Fine, go talk to them, whatever. They'll give me a report afterwards anyway."

            you "Thank you. I assume you will give me a safe-conduct then?"

            kenshin "Hmph, see that with my scribe. But one more thing, [MC.name]..."

            you "Yes?"

            kenshin "You are not allowed to enter the maximum security area of the Prison, got it?"

            you "Why not?"

            kenshin "{i}Because{/i} we have there the most dangerous criminals in all of Xeros, and I don't want you to go around and stir trouble!"

            you "Aw, you don't me to get hurt... That melts my heart a little..."

            kenshin blush "What? No, I... *blush*"

            you "You're cute when you're blushing."

            kenshin annoyed "GO AWAY! NOW! *mad*" with vpunch

            hide kenshin with dissolve

            you "I think she's warming up to me."

            scribe "Here is your letter of conduct. Show it to the Prison Warden and he'll know you came with orders from Lady Kenshin."

            stop music fadeout 3.0

            scene black with fade
            show bg prison entrance at top with dissolve

            play sound s_knock

            "Joined by Suzume, you head back to the lower city to visit the Prison."

            play sound s_creak

            knight "These are not visiting hours, citizen. State your business or leave."

            you "Here, we have a letter of conduct from the Lady Commander."

            knight "Let me see it... Hmm... Everything looks to be in order."

            knight "Come on in then. I shall take you to the Warden."

            show bg office at top with fade
            show warden with dissolve

            you "Uh, hello. *clear throat*"

            warden "Hmm, yes? Who might you be?"

            you "I'm [MC.name], Sir. I work with Lady Kenshin on a royal investigation. And this is my... Bodyguard, Suzume."

            suzume "*chuckles*"

            "The Warden takes one bored look at your papers, and nods towards a couple of chairs by his desk."

            you "Sir, I have grave news. The Prison is in danger of a security breach, and... Sir?"

            "The Warden is busy shuffling papers around as he absent-mindedly listens to you."

            warden "Hmm Hmm... *whistle*"

            you "Someone is trying to break a prisoner out of here, and..."

            "The Warden rolls his eyes."

            warden "Oh, of course they are. *sigh*"

            warden "Come on, my boy, not a day goes by without a foolish wench trying to break her lover out of the prison yard by throwing herself at a guard..."

            warden "And we have riots every other week... I have to hang a dozen inmates to restore order, every time."

            warden "None of this is worth my time, or, might I say, Lady Kenshin's... No one ever escaped the Xotar Prison."

            suzume "But it's not just any threat, though... It's a highly trained killer!"

            warden "*yawn*"

            you "And their target is the maximum security part of the Prison."

            "Suddenly, he stops in his tracks and looks back straight at you. His voice takes a more serious tone."

            warden "The maximum security area? Well, you should have mentioned it immediately, my boy."

            you "Why?"

            warden "As it happens, under the security arrangement mandated by the King, I am only in charge of the upper levels of the Prison."

            you "Was that always the deal?"

            warden "Well, no. We changed that recently. But it suits me fine."

            warden "When I bought this office, I didn't really want to handle the wild beasts we keep downstairs anyway."

            suzume "You {i}bought{/i} this office?"

            warden "Why, sure, how else do you think people get commissioned to high office? On merit? Bwahahaha!"

            warden "I have certain dealings that work best with access to the Prison population, and... Anyway. You needn't concern yourself with that."

            warden "The maximum security area below the penitenciary is the private domain of the King, and only the Knights of the Flaming Hound stand guard down there."

            suzume doubt "The Flaming what, now?"

            warden "The flaming Hounds. They're a Knight Order of the first Circle, fanatically devoted to the Royal family..."

            warden "I try to leave them to their own devices. They're a frightening bunch, if you ask me."

            warden "It cannot be easy to deal with the worst scum in Xeros, every day. The people we have up here are just petty thieves or murderers. They have it far worse."

            you "Can I talk to them then?"

            "The Warden looks annoyed, but he pushes the papers back towards you."

            warden "Well, Lady Kenshin allowed it, correct?"

            suzume "Uhuh. Sure thing. She said, 'Go right ahead!'."

            you "Yup. I believe these were her exact words."

            warden "Do as you please, then... And don't bother coming back, I'm very busy. The knights will show you out."

            hide warden with dissolve

            "A knight waits for you outside of the Warden's office. He motions for you to follow him."

            call c3_meet_hound_knights(route="warden") from _call_c3_meet_hound_knights

        "Go to the prison on your own":

            scene black with fade
            show bg prison entrance at top with dissolve

            you "So... Here we are. What do we do, now?"

            show suzume normal with dissolve

            suzume "Easy... You knock!"

            you "I knock? On the door of the largest prison in Xeros?"

            suzume "Sure. It's not like you're going to damage it."

            you "Why am I even listening to you... *sigh*"

            hide suzume with dissolve

            play sound s_knock

            "You knock and wait expectantly."

            play sound s_creak

            "An intimidating knight opens a small hatch and gives you a cold stare."

            knight "These are not visiting hours, citizen. State your business or leave."

            you "I, err, want to talk to the manager..."

            knight "The mana... The Warden? Are you out of your mind? This is the Xotar penitenciary here, not a cursed tavern!"

            you "Listen. I have crucial information regarding the security of the Prison. Somebody is trying to break in."

            knight "Break {i}in{/i}? That's a first. People usually try to break out of prison!"

            knight "Now, if you're done wasting my time..."

            suzume "Wait! They {i}are{/i} trying to break in then break someone out... They're Kunoichi, you see, and..."

            knight "WAIT! What did you just say?" with vpunch

            you "Kunoichi. It's a kind of ninja..."

            knight "Oh, I {i}know{/i} what a Kunoichi is."

            "His tone becomes cold as ice."

            knight "I think we need to have a little chat, after all... Come in, you two."

            play sound s_door

            "As the door opens, you notice the knight has a firm grip on his sword's hilt."

            knight "Leave all your weapons here, and follow me."

            call c3_meet_hound_knights(route="knight") from _call_c3_meet_hound_knights_1

    return

label c3_meet_hound_knights(route):

    scene black with fade
    show bg prison at top with fade

    play music m_suspense fadein 3.0

    "You follow the knight across the Prison yard."

    "The place is dark and decrepit, and you can make out hundreds of people living in squalor in the various levels of the Prison."

    "Screams of fear and pain regularily echo against the cold stone walls. You shiver and try not to pay attention to them."

    show bg prison office with dissolve

    "The knight goes down a flight of stairs and takes you to an isolated office, a good deal away from the entrance."

    show hound_knight with dissolve

    "You take a good look at the knight for the first time. He's like any other, but he bears an unusual red marking on his chestplate, resembling a scar. It could be a trick of the light, but the marking looks as if it is glowing from the inside."

    knight "Wait here."
    hide hound_knight with dissolve
    play sound s_door

    "The knight leaves the room. You can't help but notice he locked the door behind him. Something feels off."

    if route == "knight":

        you "Looks like we're in."

        suzume "Told ya! Winging it was the way to go."

        you "No one knows that we're here though. We could disappear now and no one would be the wiser."

        you "I didn't like the look of that k-..."

    elif route == "warden":
        you "Seems like the Warden is only nominally in charge here."

        suzume "It's the knight orders who wield the real power."

        you "I noticed. Lots of fishy business involving knights, don't you think?"

    play sound s_door

    "You interrupt yourself as you hear the lock opens."

    show hound_leader at totheright:
        zoom 1.05
    show hound_knight at totheleft with dissolve:
        zoom 0.9

    with dissolve

    "The knight you met ushers in another knight, who looks like  small giant. You can tell he is an officer of sorts."

    hound_knight "Well, what do we have here? Who are these civilians?"

    if route == "knight":
        knight "They say they possess information about a potential intruder. A {i}kunoichi{/i}, Sir."

        knight "I took the liberty to bring them in for you to interrogate."

        hound_knight "Hmm..."

    elif route == "warden":
        knight "The Warden sent them. On a mission for Lady Kenshin, apparently."

        hound_knight "Hmph. We don't have time to entertain idle chat with guests, but if it suits Her Ladyship... *snark*"

        hound_knight "What business do you have with the Flaming Hounds?"

        you "Well, you are in charge of the maximum security area of the Prison, correct?"

        hound_knight "Aye. The prisoners here are the worst scum in all of Xeros, but we keep them in check. Using any means necessary."

        you "We got word of a plot to free one of the prisoners..."

    you "Are you the one in charge of the maximum security part of the prison?"

    if story_flags["c1_path"] != "evil":
        hound_knight "{i}We{/i} are in charge here. Ever since the incident, the Order of the Flaming Hound is the only force allowed in the bowels of Xotar prison."

        you "The incident?"

        hound_knight "A maximum security prisoner had an unfortunate accident recently. Some corrupt guard officer. That's what you get, when you leave high security to amateurs."

    else:
        hound_knight "{i}We{/i}, the knights of the Flaming Hound, are in charge here."

        hound_knight "There used to be a small detachment of the Warden's incompetent guards, but they got scared and they left off."

        hound_knight "But no one scares us. That's why they're only too happy to handle the scum down here."

    you "I have never heard of your order before. Are you Kenshin's men?"

    "He scoffs."

    hound_knight "Of course you haven't. Our order favors discretion, among other things."

    hound_knight "We are of course loyal to the Crown and Her Ladyship, as the Commander of all knight orders of the first circle."

    you "I see."

    hound_knight "Now that your curiosity has been sated, you will indulge mine. What is this plot you came to warn us about?"

    you "Well..."

    hound_knight "A word of warning, first. The Knights of the Flaming Hound are not renowned for their patience."

    "He leans forward towards you, bringing his helmet only a few inches from your face."

    if route == "knight":
        hound_knight "Tell me, young lad, what was this about a {i}kunoichi{/i}?"

    else:
        hound_knight "Let us hear more about this {i}plot{/i} against our prison."

    menu:
        "The unnatural glint of his unblinking eyes makes you shiver. You take a moment to ponder your answer."

        "Tell him about Haruka":
            $ story_flags["c3_hounds_discussed_Haruka"] = True
            $ story_flags["c3_hounds_discussed_Subaru"] = True
            "You came here to discuss the Earth kunoichi, so it's time to get down to business."

            you "Her name is Haruka. She a kunoichi from the Earth school. She's been skulking around the prison for some time."

            "The knight straigthens up."

            hound_knight "Ah yes, we did know that, but thanks for confirming her identity. She's been poking around our defenses. Do you know her motives as well?"

            you "She's looking for her mentor, Subaru. The word is she's locked up in the maximum security area of this prison."

            hound_knight "Is that so..."

            "The head knight doesn't seem surprised."

            call c3_haruka_guards_success() from _call_c3_haruka_guards_success

        "Tell him about Subaru":
            $ story_flags["c3_hounds_discussed_Subaru"] = True
            "You decide to explore what they know about Subaru, the missing kunoichi."

            you "It's about a kunoichi called Subaru. She is believed to be in the city right now..."

            "The knight doesn't flinch. He says nothing, waiting for you to continue."

            you "We have reasons to believe she's here, in this very prison..."

            hound_knight "Pointless speculation. We know all the prisoners here. We have not registered anyone called 'Subaru'."

            you "She could be here under a fake name..."

            hound_knight "I don't see the need to continue this conversation."

            "There is a hint of a threat in his voice."

            if route == "knight":
                you "Wait! Your man, here, reacted earlier when we mentioned a kunoichi. It cannot just be a coincidence..."

                hound_knight "Did he, now?"

                "You can see the smaller knight cower a little, but the head knight quickly returns his attention to you."

                call c3_haruka_guards_success() from _call_c3_haruka_guards_success_1

            else:
                hound_knight "I see our estimed Warden may have had a lapse in judgment. It happens to the best of us."

                hound_knight "This hearsay doesn't concern us knights of the Flaming hound. Perhaps it is best you return to the Warden, to waste {i}his{/i} time."

                "You hear the sarcasm in his voice, but see that there is no more information to be obtained here."

                knight "Follow me. I will show you out."

                scene black with fade

        "Don't tell him":
            "Feeling nervous, you decide to stay vague until you learn more about the situation."

            you "Well, it's, err, rumors... Of an all powerful female ninja, out to liberate, er... Someone at the prison."

            "The knight brings his helmet even closer to your face. You can almost feel the cold metal brushing against your forehead."

            hound_knight "What is this giberrish? Didn't you say you were privy to some secret information?"

            you "I... I realize it's a bit vague, yes. I'm sorry, I shouldn't have wasted your time."

            hound_knight "No. You shouldn't have."

            if route == "knight":
                "The anger is palpable in his voice. You are painfully aware that you are stuck in the depth of Xotar prison, far from the surface and unarmed. He could skewer you and no one would hear you scream."

                "There is a long pause, then the knight straightens up."

                hound_knight "Show this man out. Levy an appropriate fine for wasting our precious time. *sigh*"

                "The other knight grabs you and Suzume, and shoves you both in the corridor."

                knight "You're lucky we don't throw your filthy commoner's ass in jail for contempt! Come with me!"

                scene black with fade

                $ MC.change_gold(-100)

                "You are thrown out of the jail. You had pay a 100 gold fine before you leave."

            else:
                hound_knight "You're lucky the Warden and Lady Kenshin vouched for you, or I would have you flogged in the courtyard."

                hound_knight "Out with you!"

                scene black with fade

                "One of the knights escorts you back out of the jail, visibly annoyed. They let you go without a word."

    return

label c3_haruka_guards_success():

    "He takes a long look at you, in silence. You {i}feel{/i} as if his gaze is piercing your soul."

    $ NPC_haruka.flags["subaru visit"] = True

    hound_knight "Very well. Follow me."

    "He nods towards Suzume."

    hound_knight "Let her stay here."

    "Disappointed, Suzume sits back down on her chair."

    play sound s_door_close

    "The other knight stays back with her as you follow the leader back into the Prison yard."

    scene black with fade
    show bg prison at top with dissolve

    play sound s_steps

    "You go down several long flight of stairs, then through a maze of corridors. In spite of his massive armor, the Knight doesn't seem to tire."

    "You are now in one of the lowest levels of the Prison, far from any direct sunlight. The air is thick with menace, even the screams have given way to an unatural silence."

    show bg jail at top with dissolve

    "Not a word is exchanged until you stand before a thick, heavy metal door. Another knight is standing guard in the shadows, silent as a tomb."

    show hound_leader at center:
        zoom 1.05

    hound_knight "Take a look inside this cell. You might find it interesting."

    "He slides open a metal slot, gesturing for you to observe."

    scene black
    show bg subaru prison at top
    with dissolve

    you "..."

    "From the description Haruka gave you, and the missing forearm, you have no difficulties recognizing Subaru."

    hound_knight "Is this the woman prisoner you were concerned about?"

    menu:
        "Yes":
            you "Yes. This is Subaru."

            hound_knight "Indeed."

        "I'm not sure":
            you "Well... I'm not sure..."

            hound_knight "You're not sure? Ha! *hiss*"

    you "Why is she in jail?"

    hound_knight "Her crimes are highly classified. All that you need to know is that she is an enemy of the Crown."

    hound_knight "Make no mistake, she will rot here she dies of old age, or we deliver the King's mercy."

    you "She is a feared warrior. Doesn't she try to escape?"

    hound_knight "{i}Was{/i} a feared warrior. Her body is weak, and we keep her on a special mix of spices for unruly prisoners that makes them... fully compliant."

    hound_knight "And the walls in this part of the Prison were rebuilt from Cimerian ruins, and still infused with powerful antimagic runes. Her spells are no use down here."

    if MC.playerclass == "Wizard":
        you "(So that's why I've been feeling strangely light-headed... Magic is useless here. Better make note of that.)"

    you "Does she talk?"

    hound_knight "We... 'interrogate' her at least twice a week, using... various means. But she has yet to give us information of any value."

    hound_knight "Believe me, it's not that the men are going easy on her."

    "The silent knight in the shadow, who hadn't said anything up until now, gives out a rasp chuckle."

    you "Damn. She seems all right, given the circumstances."

    hound_knight "We haven't been able to break her will yet. But she hasn't been with us for that long."

    hound_knight "Eventually, she will break. They all do..."

    hound_knight "But I didn't bring you down here for idle chatter."

    "You know going in there was going to be a catch."

    if story_flags["c3_hounds_discussed_Haruka"]:

        hound_knight "This 'apprentice' of hers, Haruka... We know of her."

        hound_knight "If we could capture her..."

        if MC.get_alignment() == "evil":
            you "... you could torture her in front of her mentor, and maybe then she would tell you what you need to know."

            hound_knight "Precisely. I like the way you think..."

        else:
            you "Yes?"

            hound_knight "We could use her against her own mentor. Surely the pupil doesn't have the same mental fortitude..."

            hound_knight "And even is she did, her master might care about her enough to finally break."

            you "..."

    else:

        hound_knight "As I'm sure you understand, this is of the utmost importance that mortal enemies of the King like this assassin remain safely locked up in this very prison."

        hound_knight "But someone has been skulking around the prison lately, looking for an unguarded entrance. A kunoichi, by the looks of her."

        you "You don't say."

        hound_knight "Since you're so concerned about the security of the prison: know that we are looking for information on this intruder."

    hound_knight "If you could help us with her arrest, you would do your King a favor, of course, but you would also earn a handsome reward."

    if MC.get_alignment() == "good":
        you "Well, I can't make promises..."

        hound_knight "Hmph."

    else:
        you "I'm all ears."

        hound_knight "Good."

    hound_knight "If you succeed in locating the rogue kunoichi, try and lure her to the East postern. There is a hidden entrance to the Prison there, only it leads right into my men's barracks."

    hound_knight "You just have to lead her inside, we'll handle the rest. We will catch her and make sure no harm will come to you."

    "You wonder how much truth there is to that last statement."

    hound_knight "Think about the reward. We will be generous. In fact..."

    "He places his hand on your shoulder. You can feel unexpected heat radiating through his glove."

    hound_knight "Would you like to receive something now, let's call it... an incentive?"

    "You shiver. The soulless stare of his helmet creeps you out."

    hound_knight "I noticed how you looked at the prisoner. Maybe you'd like to have a go?"

    you "A go at what...?"

    hound_knight "Don't pretend to be thicker than you are."

    you "..."

    hound_knight "It's nothing she hasn't been through already, believe me. Like I said, the men didn't spare her."

    "The silent knight in the shadow scoffs, sounding more wolf than man."

    hound_knight "Don't worry, she's heavily sedated. She won't be a threat."

    menu:
        "Accept his offer":
            $ MC.evil += 5
            you "Well, I won't turn away such an offer. Breaking tough bitches is kind of my thing."

            "The knight in the shadows gives a belly laugh, which startles you."

            "The head knight says nothing, but you can feel his grin widen."

            hound_knight "In you go, then. This should be good."

            call c3_subaru_rape() from _call_c3_subaru_rape

            play sound s_door_close

            scene black with fade
            show bg jail at top with dissolve

            "When you return, the Hound Knights are waiting for you. They seem amused."

            you "Hope you perverts were not peeping."

            hound_knight "Ha! We don't need to. We're going to be enjoying her again soon enough."

            hound_knight "Still, we could hear you gave her a good pounding. I think she lost it in the end."

            hound_knight "Perhaps this was the final push we needed. Hopefully this will help us break her resistance, bring her over to our... to the King's side."

            scene black with fade
            show bg prison office at top with dissolve

            "Going back to the office, you meet back with Suzume, who raises an eyebrow, wondering what took you so long."


        "Decline his offer":
            $ MC.evil -= 2
            you "Thank you for your offer, but I am no torturer. It is best left to professionals like you."

            "The knight in the shadow snarls menacingly, but the head knight only gives out a brief, creepy laugh."

            hound_knight "So be it. As you've seen, Master... [MC.name], we know how to tend to the King's prisoners, and they are well guarded."

            hound_knight "You'd do well to remember that."

            hide hound_knight with dissolve

            "The head knight walks you back out through another maze of corridors, and you realize you're completely lost again."

            "Finding your way back on your own would be impossible; he probably did it on purpose."

    play sound s_close
    scene black with fade

    "You heave a sigh of relief as you exit the prison and finally breathe some fresh air."


    return

label c3_subaru_rape():

    $ story_flags["subaru raped"] = True

    play sound s_door

    scene black with fade
    show bg subaru fondle1 at top with dissolve

    "You step inside the cell, taking a moment to look at Subaru."

    "As you know she lost her forearm in battle, her right sleeve is empty. She still has the firm body of a fighter, but in her sedated state, she seems to lack energy."

    "Her breathing is slow and her eyes glazed. She barely seems to register your presence."

    subaru "Who... Who is it..."

    "Uttering those words alone seems to take a toll on her. She looks in your general direction and tries to focus her eyes with great difficulty."

    you "Hello, Subaru."

    "You move in closer to her."

    subaru "You... Are not... A Noroi..."

    "You remember the Noroi are the demon clan she used to fight against."

    you "Oh, no... I'm just a visitor."

    subaru "What... You want..."

    "Instead of answering her, you move in closer, detailing the shape of her ass. You extend your hand and place it on her exposed shoulder."

    show bg subaru fondle2 at top with dissolve

    subaru "Don't... Touch!"

    "She tenses up, but seems unable to move at all from her prostrated position."

    you "Come on, Subaru, I'm sure you can guess what I'm here for..."

    subaru "Khhh!"

    you "You know, for a prisoner, I think you are in great shape... I'm going to enjoy myself."

    show bg subaru fondle3 at top with dissolve

    "Grabbing Subaru from behind, you waste no time, sliding your hand on her thigh while you grab one of her breast, fondling it."

    play sound s_surprise

    subaru "Aah!"

    "You pinch her nipple, feeling it stiffen against your fingertips."

    subaru "Nghh..."

    "Breathing down her neck, you enjoy the feeling of her firm ass against your body as you caress her thighs."

    "You feel yourself become hard as you press yourself against her."

    show bg fondle4 at top with dissolve

    "In spite of her drugged state, or maybe because of it, Subaru's body seems to react as you run your hands over her body."

    subaru "A-aah..."

    "Her nipples are already erect, and you can tell that she is getting wet as you rub her crotch through the fabric of her panties."

    you "I thought you'd be more resistant..."

    subaru "F... Fuck... You..."

    you "You know, I can't decide who's sexier, you or Haruka. The Earth school sure has fine tastes in the women they train."

    play sound s_scream
    show bg fondle5 at top with dissolve

    subaru "No! Haruka! What... Did..."

    menu:
        "Tell her Haruka is fine":
            $ MC.evil -= 1
            you "Relax. Your pupil is not a prisoner... Yet."

            you "But in due time, I expect she'll learn her place, too."

            subaru "Grrr..."

            "Ignoring her resistance, you increase your pace, making sure your shaft rubs against her mound every time you thrust between her legs."

        "Tell her Haruka's been captured":

            you "She's in a cell, just like you. I expect at this very moment she has a fat cock in each of her holes..."

            subaru "N-No! Haruka!"

            play sound s_punch

            "Surprisingly, she seems to recover some fighting spirit. She hits you in the stomach with her elbow, forcing the air out of you."

            you "OUCH!" with vpunch

            subaru "You..."

            "She tries to turn to face you, but you recover in time to put her in a lock."

            you "How dare you hit me, bitch! You will pay for this."

            "Hound Knight's voice" "Everything all right in there?"

            you "Sure!"

            "Completely exhausted by her burst of aggression, Subaru cannot resist you any more."

            "Resuming your ministration, you treat her body even rougher, which only seems to make her more sensitive."

    show bg subaru fondle6 at top with dissolve

    subaru "Hah... Hah... Hah..."

    you "See, Subaru, if you cooperate, it will be better for you. Your student can't help you no matter what."

    you "You'd better get used to this, as I'm sure my knight friends have started to teach you."

    subaru "I... Kill... All you..."

    you "I like your spirit, Subaru, it makes it more fun for me... For now, just try to relax."

    "Shoving your cock even harder between her legs, you increase your pace."

    "She doesn't say anything now, gritting her teeth. Her breathing becomes ragged, and you knows what is coming."

    "You grab her from behind, holding her tight, feeling her ass against your groin."

    subaru "Oh..."

    "With your dick soaked in her juices, you have to take care not to slide directly inside her gaping pussy."

    "Going for the finish move, you squeeze her boob as hard as you can while biting her neck."

    play sound s_orgasm

    with flash

    subaru "Aah! Aah!"

    "Subaru's whole body tenses up, and she screams in pleasure and pain as she comes all over your cock."

    "Tossing her soiled panties to the side, you watch her with a grin. She is laying on her side, unable to move at all."

    you "Now, let's get these out of the way."

    play sound s_dress

    scene black with fade

    show bg subaru sex1 with dissolve

    "Quickly removing her remaining clothes, you push her on all threes, taking in the view of her wet pussy."

    subaru "..."

    "It seems Subaru's mind is wandering far off again, but her body knows what's coming. In spite of herself, she raises her hips slightly towards you."

    menu:
        "Fuck her pussy":
            $ subaru_act = "sex"

            show bg subaru sex2 with dissolve

            with vpunch

            "You shove your cock inside Subaru's pussy, starting to fuck her from behind."

            subaru "Aah! Aah!"

            "She lets out a scream, and you feel her tighten around your cock."

            you "Good girl, Subaru. Just enjoy it."

            subaru "Aah... Nghh..."

            play sound s_moans_quiet

            "You enjoy her muffled moans as you keep pounding her mercilessly."

            "You didn't even bother to go slow at the beginning, confident her body could take it. And it seems you were right."

            show bg subaru sex3 with dissolve

            subaru "Ah... Ah..." with vpunch

            "With every thrust, you can feel your cock going deeper, hitting her cervix with every movement."

            "You grab her from behind, pulling her towards you, increasing the pace."

        "Fuck her ass":
            $ subaru_act = "anal"

            show bg subaru anal1 with dissolve

            "Grabbing her by the hair, you ram your cock deep into her ass, forcing her to take it."

            subaru "Khh!"

            you "Look at that, your body seems to be loving it... You are a perfect buttslut."

            show bg subaru anal2 with dissolve

    subaru "Aaah!" with vpunch

    "You slap her ass, making it bounce against your body."

    subaru "Aah... Hah..."

    you "Subaru, you are really getting into this... Hehe..."

    "She doesn't say anything, but her moans betray her arousal."

    "You can tell that her mind is slowly giving in, as she starts to match your movements."

    you "I don't see why you became a Kunoichi. You seem to be a natural whore... You could make a fortune in my brothel."

    subaru "..."

    you "I don't think the arm would be a problem... Some customers would actually love that."

    subaru "Fuck... You!"

    you "How I love your fighting spirit, Subaru."

    subaru "Aah!"

    "You pull her hair, forcing her head back."

    if subaru_act == "sex":
        "She moans in pain, but her pussy clenches around your dick. It seems your rough treatment is having an unexpected effect."

        "You feel your arousal become stronger as you pound her harder, feeling her tighten around you with every thrust."

        play sound s_orgasm
        show bg subaru sex4 with flash

        "You feel Subaru's pussy spasms as she comes all over your dick."

        subaru "Aah!"

        with doubleflash

        "With one final thrust, you come as well, shooting your load deep inside her."

        show bg subaru sex5 with flash

        subaru "Aah..."

        "Pulling out, you watch as your semen drips out of Subaru's pussy."

    else:
        "Leaning forward, you start kissing her neck, tasting the sweat on her skin."

        show bg subaru anal3 with flash

        play sound s_orgasm

        subaru "Aah! Aah!"

        "Unexpectedly, Subaru comes, clenching so hard on your dick as she reaches her climax that she almost forces your dick out."

        you "You dare cum before me? What a dirty slut..."

        "Not letting her recover from her orgasm, you slam your cock back in, treating her as a mere hole dedicated to your own pleasure."

        subaru "Aah! Aah! Ahh!" with vpunch

        "In spite of herself, Subaru can't help but moan as you thrust deep into her ass."

        "Her pussy is dripping with juices, and you can tell that she is having another orgasm."

        subaru "Aaah! Aaah!" with vpunch

        "Finally, you increase your pace and bury yourself deep inside her ass, unloading your cum into her bowels."

        show bg subaru anal4 with flash

        subaru "AAAAH!"

        with doubleflash

        "You and Subaru cum together, her anal walls tightening around your cock as you empty your balls inside her."

        show bg subaru anal5 with flash

        "Cumming a copious load inside her, you keep thrusting to make sure she gets it all."

        "Semen overflows from her gaping anus, leaking down her pussy as she collapses on the bed."

    "After emptying your balls inside her, you finally pull out, satisfied."

    $ MC.change_prestige(3)

    return

# Intercept #

label c3_haruka_final_intercept(): # Done

    play music m_haruka fadein 3.0

    scene black with fade
    show bg haruka intro at top with dissolve

    haruka "You, again?"

    haruka "I don't want to hurt you... But I can't let you interfere with my mission."

    menu:
        "Negotiate with her":

            you "Wait! I can help you."

            if NPC_haruka.flags["subaru visit"]:
                you "I have information for you. I know where Subaru is."

                haruka "She's in Xotar Prison, I know that already."

                you "Yes. But I know her precise location."

                haruka "..."

                call c3_haruka_negotiate() from _call_c3_haruka_negotiate

            else:
                you "I know where Subaru is. I have been able to piece everything together."

                you "Let me help you find her."

                haruka "Hmph. She's in Xotar Prison, I know that much. Why would I need you?"

                call challenge("force", 3) from _call_challenge_69 # result is stored in the _return variable
                $ r = _return

                "Haruka takes a good look at you."

                play sound s_sigh
                if r:
                    haruka "Hmm... You have the build of a fighter. Okay, maybe you can be of help."

                    call c3_haruka_negotiate() from _call_c3_haruka_negotiate_1

                else:

                    haruka "You're not fit for battle, you would only slow me down..."

                    you "Wait!"

                    haruka "I don't have time for this! Step aside. *firm*"

                    menu:
                        "Try and capture her":
                            call c3_capture_haruka() from _call_c3_capture_haruka

                        "Give up":
                            "Prudently, you step aside."

                            play sound s_crash
                            hide bg with vpunch

                            suzume doubt "She's gone again..."

        "Try and capture her":
            jump c3_capture_haruka

    return

label c3_capture_haruka(): # Done

    $ ninja = NPC_haruka

    if story_flags["ninja hunt"] == calendar.time:
        "You can only attempt to catch a ninja once a day."
        return

    stop music fadeout 3.0

    if MC.has_item(earth_rune.name):

        "Feeling the reassuring weight of your trusty toy-hammer in your hand, you insert the Earth Rune in the handle."

        you "(It should be here, in the small compartment held by a screw... Where it says 'Made in Cathay'.)"

        "You give a knowing look to Suzume."

        you "Let's do this."

        haruka angry "Out of my way! EARTHQUAKE!"

        "..."

        "Nothing happens."

        haruka "What is this? Why won't my powers work?"

        you "We're evenly matched now... Seize her!"

        scene black with fade

        $ story_flags["ninja hunt"] = calendar.time

        call run_ninja_game(njgame) from _call_run_ninja_game_2

        return _return

        # results are in BKchapter2 - label intercept_haruka()

    else:

        suzume "It's useless though... We need something to counter her powers..."

        play sound s_crash
        with quake

        "As before, Haruka summons a small earthquake to cover her escape. She leaves you both panting in the dirt."
        hide bg with quake

        scene black with fade

        you "Damn, if only I had a counter to Earth magic..."

    return


label c3_haruka_negotiate():

    haruka "Speak then. Where is she?"

    you "In a cell, in the maximum security part of the prison."

    haruka "Of course, I could guess that much."

    if NPC_haruka.flags["subaru visit"]:
        you "I've seen her with my own two eyes. It... wasn't pretty. But she is alive, and she hasn't broken yet."

        "Her jaw clenches."

        you "We should hurry and rescue her."

    haruka "But I've tried everything. There's no way in. The Prison is too heavily guarded, and even then you'd have to fight through the main yard just to get to the lower levels."
    you "There is another way, though. A secret passage."

    haruka "There is? Tell me!"

    you "Only if we make a deal, though."

    haruka "A deal? What deal?"

    you "I want to secure this city, make sure no upstanding citizen is being murdered by the likes of you."

    haruka "If you help me rescue Subaru, we'll leave this Arios-forsaken city forever. I promise."

    you "Okay. But we'll do things my way. And Suzume is coming with us."

    haruka "Fine, whatever. The important thing is to save Subaru."

    "You shake hands. She is reluctant at first, but you feel her becoming slightly less tense as you let her hand go."

    if NPC_haruka.flags["subaru visit"]:

        "You remember well the offer of the Hound Knight Leader."

        hound_knight "({i}You just have to lead her inside, we'll handle the rest.{/i})"

        hound_knight "({i}Think about the reward. We will be generous.{/i})"

        menu:
            "What do you tell Haruka?"

            "Tell her about the true secret passage":
                $ renpy.block_rollback()
                $ NPC_haruka.flags["c3 path"] = "ally"
                $ story_flags["ninja hunt locked %s" % get_ninja_district(NPC_haruka)] = True

                you "The secret passage is in the Sewers. Leads right into the maximum security part of the Prison."

                haruka "Really?"

                suzume "We don't know where it is yet, but if you work together with us... We can shadow the next convoy and find the secret entrance."

                you "Using force is out of question, at least until we locate Subaru. We need to enter discretely."

                haruka "Okay. Seems like this is our best chance. Let me gather some equipment, and we can meet at night, by the Sewers."

                suzume "Sure thing... Finally, we're going to see some action!"

                you "All right, we'll meet you later by {b}the Sewers{/b}."

                $ game.set_task("和遥在下水道会合。", "story")
                $ add_event("c3_haruka_sewers", type="city", location = "sewers")


            "Lead her into a trap":
                $ renpy.block_rollback()
                $ NPC_haruka.flags["c3 path"] = "banished"
                $ story_flags["ninja hunt locked %s" % get_ninja_district(NPC_haruka)] = True

                you "(This Subaru business is no concern of mine. If I help the knights, I can get rid of Haruka and make some money and allies in one fell swoop.)"

                you "There is a secret passage, by the Eastern postern. I managed to lift the key from one the guards. From there, it's straight down to Subaru's cell."

                "Subaru knows you're lying, but to her credit, she doesn't display any emotion."

                haruka "That's... Perfect. The Eastern part of the Prison has less patrols. If we can get in and out fast, we can break Subaru out of there!"

                you "Sure, sure..."

                haruka "All right, let's meet by the prison at night. I'll gather the necessary equipment."

                you "All right, we'll meet you at {b}the Prison{/b}."

                $ game.set_task("和遥在监狱会合。", "story")
                $ add_event("c3_haruka_trap", type="city", location = "prison")

    else:
        $ renpy.block_rollback()
        $ NPC_haruka.flags["c3 path"] = "ally"
        $ story_flags["ninja hunt locked %s" % get_ninja_district(NPC_haruka)] = True

        you "The secret passage is in the Sewers. Leads right into the maximum security part of the Prison."

        haruka "Really?"

        suzume "We don't know where it is yet, but if you work together with us... We can shadow the next convoy and find the secret entrance."

        you "Using force is out of question, at least until we locate Subaru. We need to enter discretely."

        haruka "Okay. Seems like this is our best chance. Let me gather some equipment, and we can meet at night, by the Sewers."

        suzume "Sure thing... Finally, we're going to see some action!"

        you "All right, we'll meet you later by {b}the Sewers{/b}."

        $ game.set_task("和遥在下水道会合。", "story")
        $ add_event("c3_haruka_sewers", type="city", location = "sewers")

    haruka "Wait, [MC.name]..."

    you "Yes?"

    haruka happy "Thank you."

    scene black with fade

    return

# 'Good' path #

label c3_haruka_sewers(): # OK

    scene black with fade
    "You wait until nightfall before meeting with Haruka."

    play music m_suspense fadein 3.0

    show bg sewers at top with dissolve

    show haruka with dissolve:
        yalign 1.0
        zoom 0.9

    haruka "[MC.name]! You came."

    you "Of course."

    show suzume at totheright with dissolve

    suzume "Heyah!"

    haruka defiant "Ah. So you're here, too."

    suzume "I did some reconnaissance, and I saw the guard patrol we're looking for. They're moving some political prisoners in by night. It's likely they'll use the sewers entrance."

    haruka "Great. Let's follow them from a distance. We can't be seen, at least not until we know where that entrance is."

    hide haruka with moveoutleft
    hide suzume with moveoutright

    "You and the girls take position in a dark alley next to the main road. Soon, you see the patrol emerge. Half a dozen soldiers escort a couple of hooded figures, in chains."

    "The group is led by a knight who seems at ease skulking in the dark."

    haruka "I know this coat of arms. This is a knight of the Flaming Hound, the order that defends the prison."

    suzume "Let's see where they are headed."

    show bg street night at top with dissolve

    "The patrol passes you by as you watch from the shadows. You wait until they are some way off, then start following them carefully."

    "In spite of your efforts, you feel slow and clumsy, compared to the Kunoichi who seem to glide effortlessly into the night, silent as ghosts."

    if MC.playerclass == "Warrior":
        "Your experience fighting Elven scouts in the dark forests of the Holy Lands taught you a lot about sneaking though, so you manage to follow, not too far behind."

    elif MC.playerclass == "Wizard":
        "You cast a noise reduction spell on yourself, allowing you to move faster to keep up with the girls."

    elif MC.playerclass == "Trader":
        "As someone with a lot of experience thieving, you know enough about sneaking to follow cautiously. Besides, you have an ace up your sleeve."

        "Looking up, you see a dark silhouette gliding silently dozens of feet above the streets. It's your pet dragon, keeping an eye on your prey for you."

    "Fortunately, the squad is unsuspecting and does not stop to see if they are followed. Soon, it seems they have reached their destination."

    suzume "Wait, what are they doing?"

    "The guards stop in front of a building, which on closer inspection appears to be a barracks."

    show guard with dissolve:
        zoom 0.17
        xalign 0.21
        yalign 0.71

    "They exchange words with someone inside, then the whole group enters, save for one sentinel."

    haruka angry "This can't be right! You said they were headed to the Sewers!"

    you "I thought so... I..."

    "Haruka rummages frantically in her satchel, then pulls out a scroll."

    haruka defiant "Let me see... Could it be..."

    "You and Suzume give her a puzzled look."

    haruka "Here! I see. Let me just confirm something."

    "Haruka leaps on top of an old cart, lifts herself up on a balcony then climbs up a building effortlessly. A moment later, she reaches the roof, disappearing from view."

    you "What the..."

    suzume doubt "Hush, don't worry. She'll be back in a moment."

    "A minute later, Haruka comes back down, jumping in a somersault to land just next to you without barely a noise."

    haruka "I've seen them. There's a grate to the Sewers in the court behind the barracks. That's where they took the prisoners."

    haruka "The only way in is through the barracks' entrance, though."

    you "We can't fight our way through a guards' barracks! Even if we win, this will bring the whole city's attention down on us."

    haruka "I know. We need to infiltrate. And there's the issue of the sentinel they posted at the door..."

    haruka "We can't sneak past him, and he's wearing armor, so a takedown from afar is too risky..."

    suzume shrewd "Seems like we need to come up with a plan, and fast. I think I know just what to do."

    "She kneels besides Haruka, and whispers something in her ear."

    haruka surprise "What?!? I don't... It's not..." with vpunch

    haruka angry "Why don't {i}you{/i} do it?"

    suzume "I'm going to stay out here to cover you guys. It's better if no one sees me. But you need to get inside with [MC.name] fast, don't you?"

    haruka surprise "Y-Yes, but..."

    suzume normal "Don't argue, then! This is your chance to save Subaru. Don't let it slip!"

    haruka blush "I... You... I guess you're right..."

    you "Will someone tell me what's going on?"

    "Suzume grins, and whispers her plan in your ear."

    call c3_haruka_fondle() from _call_c3_haruka_fondle

    scene black with fade
    show bg street night at top with dissolve
    show suzume at totheright with dissolve

    suzume "Well done, you two! I feel like you could have gone on for a bit longer!"

    show suzume at totheright with move
    show haruka with dissolve:
        yalign 1.0
        zoom 0.9

    haruka blush "C-Couldn't you think of anything else to distract the guard?"

    suzume "Hey, it was just the first thing that came to mind!"

    haruka angry "What kind of mind thinks like this???" with vpunch

    suzume doubt "I suppose we could just have whistled to get the guard's attention... But hey, that way was more fun!"

    haruka "Fun for whom!!!" with vpunch

    you "Stop squabbling, you two! Haruka, we need to rush to the Sewers before we lose the trail."

    you "Suzume, hide the body and meet us at the rendezvous point."

    suzume bend "Okay. Good luck out there."

    hide suzume with dissolve
    show haruka at center with move

    haruka "Quick, let's follow them!"

    play sound s_creak

    scene black with fade
    show bg inner_sewers at top with dissolve

    "Moving quickly, you go through the grate behind the barracks and descend into the Sewers."

    "Once you reach the ground, Haruka motions for you to stay silent. She places her palm on the wall, concentrating."

    you "What... What are you doing?"

    haruka defiant "Hush! I can sense their footsteps echoing through the tunnels... They're already pretty far. We need to hurry."

    "Haruka darts into the nearest tunnel, and you follow her as fast as you can, half-blinded by the darkness."

    you "Hey! Wait..."

    with fade

    "From time to time, Haruka stops to feel the ground's vibrations, giving you time to catch up."

    "Eventually, she stops dead in her tracks and pulls you close."

    haruka "They're just around the bend over there. We must be quiet."

    "You can see the flickering of torches up ahead. You both move silently in the shadows, until you can cautiously look around the corner."

    show hound_knight with dissolve:
        zoom 0.65
        xalign 0.6
        yalign 0.8
        yanchor 1.0

    knight "We'll take over from here. Common guards are now allowed beyond this point."

    show guard with dissolve:
        zoom 0.6
        xalign 0.3
        yalign 0.8
        yanchor 1.0

    guard "Me legs are killing me, and me throat is parched!"

    guard "Aw, have a heart, Sir, at least let us rest a little in yer cosy barracks! I need me a drink!"

    knight "Giving me orders, are you now, commoner?"

    play sound s_punch
    with vpunch

    guard "OW!!!"
    hide guard with pixellate

    "The knight casually smacks the guard in the jaw with his armored gauntlet, knocking out a tooth."

    knight "Is this how you address your betters, pleb? I gave you an order. Now, scram with the rest of you."

    "Frightened, the other guards grab their knocked-out comrade and skitter back through the tunnel."

    "Haruka pulls you down behind a broken crate just in time for you to let the guards pass."

    "There's not much space behind the crate, so you have to stay close together. It isn't unpleasant."

    "She whispers in your ear."

    haruka "(Let's wait until they're out of hearing range. Then we move.)"

    "You turn your attention back to the knight and his wretched prisoners, blinded by hoods."

    "Elder prisoner" "Please, Sir! Where are you taking us? I-I can't walk much longer..."

    knight "Save your breath, old man. Or I'll be more than happy to give you the same treatment I gave that stupid guard."

    "The knight places his hand on the wall and does something."

    play sound s_stone
    with vpunch

    "You can feel the rumble of stone as the wall slowly moves to reveal an entrance."

    "He yanks the chains to lead the prisoners inside."

    haruka "(We strike, now!)"

    play sound s_dodge

    show haruka with blinds:
        zoom 0.075
        xalign 0.225
        yalign 0.525

    pause 0.3

    play sound2 s_dodge
    hide haruka with blinds
    show haruka behind hound_knight with blinds:
        zoom 0.5
        yanchor 1.0
        xalign 0.4
        ypos 0.8

    "One second Haruka is besides you, the next she is leaping across the tunnel, closing the gap with the knight at a terrifying speed."

    play sound s_sheath

    knight "Uh-"

    play sound s_splat

    with vpunch

    "The knight doesn't have a chance to turn around before Haruka plunges her dagger in his neck, striking at the gap between his armor and helmet."

    hide hound_knight with pixellate

    "For a second, Haruka freezes behind the knight's body, frowning."

    "Elder prisoner" "What is going on? Please, anyone, can you help us!"

    "The hooded prisoners start panicking, unable to see what just happened. Haruka snaps out of her daze."

    haruka angry "Quick, [MC.name], come with me! We need to go get her!"

    "You look at the two wretched prisoners, shackled and powerless."

    you "What about these people?"

    haruka "What about them? We have no time, [MC.name]!"

    menu:
        "Help them out":
            $ MC.good += 2

            you "I just can't leave them here..."

            "Haruka sighs with exasperation as you remove the hooded sacks from their heads. She helps you snap their bounds open with her steel."

            "The prisoners are an old man and his teenage daughter, whom on better days look like they might have been part of good society."

            "They thank you profusely before running away in the tunnels."

            haruka defiant "Here, happy now? Now, let's go!"

            $ story_flags["c3 helped prisoners"] = True

            #! Return event for helped customers

        "Leave them":
            $ MC.good -= 2

            you "You're right, we have more important things to do."

    "Haruka charges recklessly inside the Prison through the secret entrance, barely giving you time to follow."

label c3_haruka_rescue():

    scene black with fade
    show bg thieves_guild corridor at top with dissolve

    play sound s_steps

    you "Wait, Haruka, wait!"

    "Haruka stops, looking uncertain."

    haruka surprise "The vibrations, I can't feel them any more. I can't locate Subaru!"

    you "These walls are Cimerian-built. I think they have wards against magic."

    haruka angry "Damn it!"

    if NPC_haruka.flags["subaru visit"]:
        you "Wait, I recognize this corridor... We're close to Subaru now!"
    else:
        you "It seems like we are already in the deepest part of the Prison... She can't be very far now, can she?"

    haruka angry "Look, down here!"

    "Haruka shows you some markings on the wall. To you, they look like a series of random scratches."

    haruka "I recognize this, this is a code from the Earth school. Subaru must have found a way to leave this alongside the way, behind her captors' back."

    haruka "This should lead her to her cell!"

    hide bg with dissolve
    "After just a few turns, you finally reach the cells."
    show bg jail at top with dissolve
    show haruka with dissolve

    haruka "The trail ends here!"

    you "There are no guards..."

    haruka "We've been lucky! Look, it's her cell! Quick, let's break her out!"

    you "But don't you think it's strange..."

    with flash
    play sound2 s_fire

    "Without listening to you, Haruka throws a ninja bomb at the cell's door, blowing it open." with vpunch

    "A silhouette emerges from the smoke, stumbling out of the cell."

    haruka "Sensei!"

    subaru "Haruka? Is that you?"

    haruka "It' me, Sensei! We're breaking you out!"

    play sound s_clang

    "Haruka flings a weapon at Subaru, who catches it swiftly with her good arm, in spite of her tired state."

    show haruka at right with move
    show subaru2 at left with dissolve

    subaru "We? Who's with you?"

    haruka "This is [MC.name]. He can be trusted. We need to make our way out, now. Can you walk?"

    if story_flags["subaru raped"]:
        subaru "This man... This man..."

        haruka "What is it, Subaru?"

        subaru "He's with them!"

        play sound s_sheath

        scene black
        show bg subaru kill at top
        with flash

        "Faster than your eyes can hope to follow, Subaru leaps at you, plunging her blade through your heart."

        subaru "Die, monster..."

        scene black with circlein

        "As your consciousness fades, you realize you've made a mistake..."

        $ unlock_achievement("game over")

        play music m_theme_quiet
        scene black with fade

        centered "{color=[c_red]}{b}GAME OVER{/b}{/color}"

        $ renpy.full_restart()

    subaru "Yes, don't worry about me. Lead the way."

    play sound s_maniacal_laugh

    hound_knight "Not so fast!"

    hide subaru
    hide haruka
    hide bg

    show bg jail

    show hound_knight at left as k1:
        zoom 0.7
    show hound_knight at right as k4:
        zoom 0.7
    show hound_knight at totheright as k2:
        zoom 0.85
    show hound_knight at totheleft as k3:
        zoom 0.85

    show hound_knight:
        xalign 0.5
        yalign 1.0
        zoom 1.05

    with pushleft

    play music m_danger fadein 3.0

    hound_knight "Look what the hound dragged in... Haruka, the bitch ninja's own little whelp."

    hound_knight "Actually, I remember you... We had some fun last time with you, I recall."

    subaru "Haruka..."

    haruka angry "What the hell are you saying! I've never met you in my life" with vpunch

    hound_knight "Oh, but you have..."

    hide hound_knight
    hide k1
    hide k2
    hide k3
    hide k4
    with blinds

    show noroi at left as n1:
        zoom 0.7
    show noroi at right as n4:
        zoom 0.7
        xanchor 0.5
    show noroi at totheright as n2:
        zoom 0.85
        xanchor 0.5
    show noroi at totheleft as n3:
        zoom 0.85

    show noroi_leader:
        xalign 0.5
        yalign 1.0
        zoom 1.05

    with blinds

    noroi_leader "Haven't you?"

    haruka "No! No! It's impossible..."

    subaru "These knights. They're Noroi, Haruka."

    you "What in the Seven Hells is this?"

    if NPC_haruka.flags["subaru visit"]:
        "Noroi Leader" "And here is our little interloper... The Princess's own errand boy."
    else:
        "Noroi Leader" "And who is that fool?"

    noroi_leader "No matter, just kill him. And get the girls alive. Cut off their limbs if you have, to but don't let them die!"

    "Norois" "Yes, boss!!!" with vpunch

    # $ diff = 5

    if MC.playerclass == "Warrior":
        "Clutching your sword, you empty your mind, ready to enter the fray."
    elif MC.playerclass == "Wizard":
        "Unable to use your spells, you are at a serious disadvantage. You will have to think quick."
    elif MC.playerclass == "Trader":
        play sound s_roar
        drogon "*ROAR*"
        "A loud roar echoes through the corridors. You know your pet dragon has been following you the whole time, and he is now rushing to help."
        # $ diff = 4

    # $ chal = renpy.call_screen("challenge_menu", challenges=[("Fight", "fight", 4), ("Take charge of the battle", "rally", diff)])
    #
    # if chal == "fight":
    #     $ norollback()
    #
    #     call challenge(chal, 4)
    #     $ r = _return

    play sound s_sheath

    show noroi as n1 at jumping

    "The first Noroi comes clawing at you, mistaking you for an easy target."

    if MC.playerclass == "Warrior":
        play sound s_sheath

        # add slicing

        "Your blade slashes through him like butter, and he gives you a dumbfounded look as his body is sliced cleanly in halves."

    elif MC.playerclass == "Wizard":
        play sound s_punch

        "Reduced to using your staff as a mace, you hit the charging demon in the face, eliciting a painful grunt."

        play sound2 s_splat

        "Before he can recover, you grab your staff with both hands and bring it down on his skull, hearing a statisfying crunch."

        hide n1 with pixellate

    elif MC.playerclass == "Trader":
        play sound s_roar
        "His cry of triumph becomes a scream as Drogon swoops in and locks his neck between his jaws, crushing it."

        play sound s_splat

        "Demon blood splashes around as Drogon increases the pressure, while the demon jerks around helplessly. It isn't long before he stops moving."

    play sound s_sheath
    pause 0.2
    play sound2 s_wscream
    hide n4 with pixellate

    "A shriek of pain comes from the next Noroi as Subaru severs his arm at shoulder level, before swirling and taking his head off."

    play sound s_sheath
    pause 0.2
    play sound2 s_sheath
    pause 0.3
    play sound3 s_crash

    hide n2 with pixellate

    "Haruka also found her mark, sticking two kunais in the chest of her victim before extending her arms outwards and ripping it open."

    noroi_leader "Get them! Get them!"

    play sound s_dodge
    pause 0.2
    play sound s_splat

    "The last Noroi soldier hesitates just a bit too long before a kunai thrown by Haruka hits his throat. He dies in a gurgle."

    hide n3 with pixellate

    subaru "It's just you, now, demon!"

    noroi_leader "You will not get past me! I should have killed you a long time after all, but now I won't make that mistake!"

    play sound s_mystery

    show noroi_leader:
        ease 0.5 zoom 1.7 ypos 1.2

    "Dark energy swirls around the Noroi as he seems to feed on the remains of his dead comrades. He ends up towering above all of you, large as an ogre."

    play sound s_roar

    noroi_leader "Hyaaaaahahaha, POWER!!!"

    noroi_leader "Now you DIE!"

    play sound s_punch
    show noroi_leader at jumping

    "Charging at you with surprising speed, you barely have time to avoid the demon's strike but the shock sends you flying into the wall, hitting your head hard."

    you "OUCH!" with vpunch

    "Subaru and Haruka dodged away, but he is on them in an instant. Subaru can barely parry his flurry of attacks with her good arm, while Haruka struggles to find an opening."

    noroi_leader "Your temple is over! Your people is over!"

    play sound s_roar

    noroi_leader "With every life you lose, you grow weaker, but we feed on death! We are unstoppable!"

    play sound s_laugh

    subaru "Maggots feast on the dead too, but I can still crush them under my heel!"

    play sound s_punch

    "*HIT*" with vpunch

    "Seeing a fleeting opening in his guard, Subaru kicks him right in the chin, sending his head flinging backwards."

    play sound s_roar
    noroi_leader "ARRRH!" with vpunch

    "Stumbling blindly forward, trying to grab her, the Noroi ogre fails to see Subaru is already sliding between his legs, slashing at the back of both his knees."

    play sound s_sheath
    "*SLASH*"

    play sound s_roar
    noroi_leader "AAAAARRRRH!!!" with vpunch

    "The demon flips around. He nearly crushes Subaru's head with his weapon, but Haruka blocks it at the last moment."

    play sound s_punch
    pause 0.2
    play sound s_crash

    haruka "Haaaah!!!" with vpunch

    "Kicking Haruka viciously, the demon sends her flying, knocking down Subaru at the same time. He looms over them, ready to strike a killing blow."

    haruka "Subaru!!! Watch out!!!" with vpunch

    you "(It's my chance!)"

    "Having regained your footing, you take advantage of the giant's inattention."

    you "Hey, hunchback!"

    "Grabbing a kunai on the floor, you leap over the demon's back, sticking the weapon in his neck."

    play sound s_roar

    noroi_leader "*GROAR*" with vpunch

    show noroi_leader:
        ease 0.5 xalign 0.5 yalign 1.0 zoom 1.25

    "The monster trashes around as dark blood spurts from his neck, trying to shake you off. Eventually, he manages to fling you off, turning around to face you."

    noroi_leader "YOU WORM! ANY LAST WORDS?!?" with vpunch

    play sound s_sheath

    pause 0.2

    play sound s_splat
    stop music fadeout 3.0

    "*SPLAT*" with vpunch

    hide noroi_leader
    show noroi_leader as half1:
        crop (0, 0, 0.5, 1.0)
        zoom 1.25 xanchor 1.0 xpos 0.5 yalign 1.0
    show noroi_leader as half2:
        crop (0.5, 0, 0.5, 1.0)
        zoom 1.25 xanchor 0.0 xpos 0.5 yalign 1.0

    play sound2 s_sheath
    with flash

    show noroi_leader as half1:
        ease 1.5 ypos 0.0 yanchor 1.0

    show noroi_leader as half2:
        ease 1.5 ypos 1.5 yanchor 0.0

    "Before he can say anything further, his body is split cleanly in half by a blade."

    play sound s_crash
    hide half1
    hide half2

    show subaru2 at center
    show bg jail behind subaru2
    with pixellate

    "As his lifeless body crashes to the ground, you can see Subaru standing behind him, her blade covered in gore."

    subaru "Phew. Thanks, you guys. It nearly got the best of us."

    subaru "I'm really badly out of shape."

    show subaru2 at left with move
    show haruka at right with dissolve

    haruka normal "You used to be able to defeat three of these single-handedly... You need rest, Sensei. "

    subaru "Well, I need to learn to do a lot of things single-handedly now. *chukles*"

    haruka sad "I-I didn't mean..."

    you "Ladies, shall we get out of here? I think we've overstayed our welcome."

    subaru "I for one would love to leave this place behind. Lead the way."

    play sound s_dodge

    haruka angry "Of course! Follow me, let's go!"

    scene black with fade
    show bg thieves_guild corridor at top with dissolve

    play sound s_steps

    "Running like the wind, Haruka leads you and Subaru back through the maze of corridors. You're glad that she has memorized the way perfectly, as it is easy to get lost in the dimly-lit prison."

    scene black with fade
    show bg inner_sewers at top with dissolve

    if not story_flags["c3 helped prisoners"]:

        "You finally come out through the Sewers exit."

        play sound s_mystery

        "*BUMP*" with vpunch

        you "What's that?"

        you "Haaah!" with vpunch

        "With horror, you realize you stumbled on a mangled corpse. Although its features are barely recognizeable, you realize it's one of the shackled prisoners from earlier."

        "The body of the other prisoner is further away in the sewer, missing some limbs."

        you "W-What happened to them..."

        haruka sad "Seems like some sewer monster got to them while they were left here..."

        you "Damn... We shouldn't have left them alone here..."

        haruka "I'm sorry. What's done is done."

        subaru "Let's leave before the Noroi catch up to us... Or this 'thing' comes back for seconds."

    else:
        "The three of you run through the sewers at top speed, not looking back."

label c3_free_subaru():

    scene black with fade
    play sound s_creak

    "You manage to make your way back to another sewer exit, where you previously set up a rendezvous with Suzume."

    show bg street night at top with dissolve

    show subaru2 with dissolve

    subaru "Hmmmm... Finally, some fresh air!"

    subaru "I didn't think I was ever going to see the night sky again."

    show subaru2 at left with move

    show suzume bend at right with dissolve

    suzume "Kukukukuku, you made it!!! Subaru, I presume?"

    subaru "Oh, another kunoichi? That's quite the rescue operation... I'm flattered..."

    subaru "Haruka, you need to tell me how you managed to make so many useful allies."

    hide suzume with dissolve
    show haruka_humble at right with dissolve

    haruka blush "I... I didn't. It's all thanks to [MC.name]. He chose to help me."

    subaru "Well then, thank you, [MC.name]. Haruka and I are forever in your debt."

    "To your surprise, she bows gracefully to you, and Haruka immediately bows even deeper."

    subaru "On my honor, I shall repay this favor to you. If you need anything..."

    you "Well, the first thing I need if for Haruka to honor our deal. No more assassinations in the city, and I need to know everything you know about the kunoichi murders in the city."

    subaru "Hold on, hold on. Haruka, what is he talking about?"

    haruka normal "Well, I'm not sure. I haven't murdered anyone in the city, save for these 'knights'."

    you "But someone has been taking out important officials. They have links to a Kunoichi clan. Surely you know more?"

    haruka "Well, I have some suspicions. Whatever this demon cult is doing infiltrating the Knights, it must be related somehow."

    subaru "The least we can do is help you look into what's going on with the Noroi. It aligns well with our goals, too."

    you "Thank you. That would be helpful."

    you "But don't take anyone out. Or at least, come to me first."

    subaru "You've got it."

    haruka "Sensei, you're very tired... We must go."

    play sound s_sigh

    subaru "I know... *sigh*"

    subaru "We need to go, [MC.name]. We'll talk more after we've had a chance to rest."

    subaru "Thank you again."

    haruka happy "Thank you, [MC.name], from the bottom of my heart."

    play sound s_dodge

    hide subaru2 with dissolve
    hide haruka_humble with dissolve

    $ story_flags['haruka path'] = "ally"
    $ game.set_task(None, "story")

    "The two ninjas fade into the night."

    show suzume bend with dissolve

    suzume "So this is Subaru, the legend, uh? She's only got the one arm, but she seems cool."

    you "Do you think we can trust these two?"

    suzume "I don't see why not. They seem just as reliable than I am."

    you "I don't know if that's reassuring..."

    scene black with fade

    return

label c3_haruka_fondle(): # OK

    scene black with fade

    "You and Haruka move into position into a dark alley, straight across from the barracks."

    you "*shout* Hey! Come here, little girlie! Let me have some fun!"

    show bg haruka fondle1 at top with dissolve

    play sound s_scream_loud

    haruka blush "EEEEK! Help!!!" with vpunch

    you "*in character* HEHEHE, Missus, I'm going to have some fun with ya! *hiccup*"

    play sound s_surprise

    haruka "*in character* I'm, err, in distress!!! Help!" with vpunch

    haruka "(What on earth are we doing???)"

    you "(It's like Suzume said, we need to get the guard's attention away from that door.)"

    haruka "(B-But, you're really touching me!!!)"

    you "(It has to look genuine... Play along!"

    play sound s_scream

    haruka "Haaa!" with vpunch

    "You squeeze her breast encouraginly."

    haruka "D-Don't do that! Stop!"

    you "(Yes, that's it, play along.)"

    show bg haruka fondle2 at top with dissolve

    play sound s_ahaa

    haruka "I'm not pla... Ahaa..."

    "Not one to pass such a great opportunity to have fun, you continue teasing Haruka, caressing her inner thigh, inching closer to her panties."

    you "*loud* HAHAHA! I'm going to deflower you right now, even though you are obviously non-consenting and this is completely against the law. Because I'm a LAW BREAKER!" with vpunch

    play sound s_moans_quiet

    haruka "(W-Why is your acting so bad?)"

    play sound s_scream
    haruka "*loud* HAAAAH!" with vpunch

    "In spite of your efforts, the guard remains impassive. Perhaps he hasn't seen you yet, or he doesn't care."

    haruka "(Aahh! You're too rough with me...)"

    you "(At least I'm trying to get his attention! You do it!)"

    play sound s_screams

    haruka "*louder* HAAAA, HAAA, HELP, ANYONE!" with vpunch

    haruka "I am being assaulted by a ruffian, even though I am obviously not consenting and it is completely against the law!"

    you "(You called me a bad actor, and then you use {i}my{/i} line?)"

    haruka "(It's all in the delivery! Mine was better! Aaaah...)"

    play sound s_aah
    haruka "Aaaah..."

    "You notice that Haruka has eased into her situation rather quickly. She barely fights you back as you fondle her, mellowing in your embrace."

    you "(At least we're having a good time, aren't we? You seem to feel fine.)"

    "You run your fingers against her panties, feeling a hint of wetness."

    haruka angry "(S-Shut up, stop doing that! Let's get this over with already!)"

    haruka "HELP, SOMEONE, HEEEELP!!! Is there anyone that can help me around here! Anyone who represents the legal authorities of this town, especially someone from the guard?" with vpunch

    play sound s_scream_loud

    haruka "PLEASE HEEEELP!!!" with vpunch

    you "(It's not working... He's looking straight at us, and yet he won't move a finger!)"

    haruka blush "(This was a stupid idea... Let's just stop...)"

    you "(We need a new approach. I know what to do, but you need to trust me.)"

    play sound s_dress

    show bg haruka fondle3 at top with dissolve

    play sound s_scream

    haruka "W-What are you doing!!!" with vpunch

    "Freeing Haruka's large tits from her jumpsuit, you keep rubbing them in plain view of the sentry."

    you "*drunken drawl* OOOH, look at that bitch's titties! She's a handful!"

    you "MAN, she must be PERFECT for a TITJOB!"

    you "Damn, I think I'm too drunk to get it up! Hey, is there ANOTHER DUDE out here who wants to relieve himself, uh?"

    you "Is there someone man enough to FUCK this innocent chick with the huge TITTIES?"

    "You see the sentry stir."

    haruka "(I don't believe it... I-It's working...)"

    "The man is now clearly oggling Haruka's tits by the streetlight. He hesitates to move, struggling to get a better view."

    you "(We just have to give him a little push...)"

    you "OOH, I think this bitch loves getting raped! She's in heat for sure! I can tell she is completely wet, ready to take a dick!"

    play sound s_ahaa

    haruka "Ahaaa, you're so rough, Mister, I can't take it!" with vpunch

    show bg haruka fondle4 at top with dissolve

    "Haruka leans back into your arms, almost grinding against you. She closes her eyes, moaning."

    haruka "I feel so strange, being manhandled in a dark alley by a stranger! I feel so hot down there!"

    haruka "Please, SOMEONE, make me feel better!" with vpunch

    play sound s_aaah

    haruka "AAAAAH!!!" with vpunch

    "Haruka screams wildly, moving her hips suggestively."

    you "(Wow, your acting is getting really good now!)"

    haruka "(S-Sorry, I think I'm getting carried away...)"

    you "(No no, keep at it! It's working!)"

    "The guard is now walking towards the alley, patting his crotch. He has a smug smile on his face."

    haruka "S-Sir?"

    you "Come over here, officer, there's plenty of ass for the both of us!"

    guard "Get lost, drifter, before I throw you in jail to feed the rats! She's mine..."

    you "Oh no, Sir, I'm sorry if I offended you, honest..."

    "You step back slowly, raising your hands."

    "He moves forward menacingly."

    haruka "A-Are you rescuing me, good Sir?"

    guard "Hehehe, sure... I'm rescuing you, so let me send that drunk loser on his way and then we'll get to the part where you reward me, hehehehe."

    you "B-But the girl was mine, Sir, you need to pay me a denar or two... Or I won't move! I got her nice and wet for you, didn't I?"

    guard "What??" with vpunch

    "As you say that, you slowly retreat into the dark alley. The guard reaches for his sword and walks towards you, stepping past Haruka, ."

    guard "If you don't scram right this instant, motherfu-..."

    play sound s_punch
    with vpunch

    pause 0.2

    play sound s_crash

    "Haruka hand-chops the guard right at the base of the neck, and he crumbles like a bag of sand."

    you "Nice! Is he alive?"

    haruka defiant "Who cares? Let's go."

    "Not making eye contact, she fixes her clothing, and runs for the barracks' entrance."

    $ MC.change_prestige(3)

    return

# 'Evil' path #

label c3_haruka_trap():

    scene black with fade
    "You and Suzume wait until nightfall before meeting with Haruka."

    show bg prison entrance at top with dissolve
    show haruka with dissolve

    play music m_wind fadein 3.0

    you "...see, this is the East Postern, where the secret door is."

    haruka "There are no guards..."

    you "Yes, it's perfect."

    haruka "It's strange, don't you think?"

    you "Well, no one is supposed to know about this entrance, I guess. It doesn't matter, let's get in before someone sees us."

    haruka "Well, I guess I have no choice but to trust you on this..."

    "Moving quickly, the three of you run towards the stone wall. You see the faint outline of a door cut directly in the stone."

    play sound s_stone
    with vpunch
    "Following the knight's instructions, you unlock the door and it pivots with a heavy noise, revealing a dark flight of stairs."

    you "Get in there, quick! I'll cover the rear."

    haruka "Okay. Subaru-sensei, here I come!"

    scene black with fade
    play sound s_steps
    "Haruka charges into the prison, rushing down the stairs."

    show bg jail at top with dissolve

    haruka surprise "Wait!" with vpunch

    play music m_mafia fadein 3.0

    if story_flags["subaru raped"]:
        show subaru evil hidden with dissolve

    else:
        show hound_knight as k1 with dissolve
        show hound_knight at totheleft as k2 behind k1 with dissolve:
            zoom 0.9
        show hound_knight at totheright as k3 behind k1 with dissolve:
            zoom 0.9
        show hound_knight at left as k4 behind k2:
            zoom 0.85
        show hound_knight at right as k5 behind k3:
            zoom 0.85
        with dissolve

    haruka ninja "What? What is this!?!" with vpunch

    if story_flags["subaru raped"]:
        play sound s_sheath

        "Haruka doesn't even have time to unsheath her blade before the mysterious figure casts a dark spell on her."

        play sound2 s_splat

        "*SPLASH*" with vpunch

        "Haruka finds herself intertwined in a giant, thick spiderlike web."

        haruka "W-Who... Who are you?!?"

        play music m_demons

        show subaru evil with dissolve

        "The scarlet-clad figure emerges from the shadows, and Haruka gasps."

        haruka "S-Sensei! Is this you?" with vpunch

        "You recognize Subaru, although she is completely changed, from the way she is dressed to the color of her eyes. Incredibly, her arm even seems to have been made whole."

        subaru evil "My sweet little Haruka... Welcome. I've been waiting for you."

        haruka "But Sensei... How? Why?"

        play sound s_evil_laugh

        subaru "You know, for the longest time, I was like you, fighting back against fate, questioning everything..."

        subaru "But then, I finally saw things clearly. You shouldn't fight the darkness within you, you should {i}embrace{/i} it..."

        haruka "No! What have they done to you?" with vpunch

        subaru "They have offered me a new life, one without rules and boundaries... And I have decided to accept it."

        "She turns towards you."

        subaru "And it's all thanks to you, by the way... You've helped me see the one true path."

        "She licks her lips seductively."

        subaru "After our meeting, I was drained, I couldn't resist them anymore... So I finally gave in to my urges... And now, I don't regret any of it."

        haruka "YOU! What did you do to her?!? You betrayed us!!!" with vpunch

        "She struggles against her bonds, to no avail."

        subaru "Hush, little girl, you're being an unruly pupil now... But I will deal with you."

        haruka "No!!!"

        call c3_haruka_demon_subaru() from _call_c3_haruka_demon_subaru

        scene black with fade
        show bg jail at top with dissolve

        show hound_leader at left
        show subaru evil at right
        with dissolve

        "As you reluctantly look away from this spectacle, you realize the Flaming Hound leader has joined you."

        hound_knight "You have kept your end of the bargain. The Order is pleased."

        you "Sure, sure. But you mentioned a reward."

        hound_knight "Here. You can have this."

    else:

        play sound s_sheath
        pause 0.3
        play sound2 s_sheath
        pause 0.1
        play sound3 s_sheath

        haruka "Stand back!" with vpunch

        play sound s_clang
        pause 0.2
        play sound2 s_clang
        pause 0.2
        play sound3 s_sheath

        "Haruka is surrounded by knights, desperately defending herself."

        play sound s_sheath
        pause 0.2
        play sound2 s_wscream

        hide k5 with pixellate

        knight "Aaargh!" with vpunch

        haruka "No!"

        play sound s_clang
        pause 0.2
        play sound2 s_punch
        pause 0.1
        play sound3 s_crash

        show hound_knight as k1 at bounce

        knight "Take that!"

        play sound s_scream

        haruka "OUCH!" with vpunch

        "Haruka crashes down on the floor, and soon the knights pile up over her."

        haruka surprise "No! Let me go, you bastards!"

        "The men finally manage to subdue Haruka, disarming her and tying her securely."

        haruka "No!!! My magic doesn't work... Why?"

        haruka "[MC.name]! Help me!" with vpunch

        play sound s_maniacal_laugh

        knight "Help you? he's the one who led you right to us!"

        haruka "What?"

        you "I did. Sorry, Haruka, you shouldn't trust strangers so readily."

        haruka angry "Grrr... Let me go! I'll kill you, [MC.name]!" with vpunch

        knight "Shut up bitch, you're ours now... I hope you enjoyed a bit of sun today, because you're never going to see the light of day again."

        play sound s_scream_loud

        haruka surprise "No!!!" with vpunch

        knight "You! You have done your job, now leave the rest to us. Here, have this as a present from the boss."

    call receive_item(subaru_tunic, use_article=False) from _call_receive_item_28

    you "Thanks. I'll be out of your hair, then."

    $ story_flags['haruka path'] = "demon"
    $ game.set_task(None, "story")

    knight "Good. Now go. And you'd better forget everything you've seen in here."

    scene black with fade

    play sound s_screams

    haruka "Heeeeelp!!!" with vpunch

    "You hurry back out of the dungeon, leaving the screams of desperation of the captured Earth ninja behind."

    return


label c3_haruka_demon_subaru():

    play sound s_dress

    scene black

    show bg subaru_demon1 at top

    with dissolve

    "Before Haruka can resist any further, Subaru rips open her clothes with claw-like strength from her reconstructed arm."

    haruka "Sensei, please! Think of what you're doing! Break this spell, and escape with me!"

    "Ignoring her, Subaru grabs one of her boobs, feeling it."

    subaru evil "You don't get it, do you? Your old mentor is no more. All that is left of me is my core: animal instincts, desires... Lust."

    play sound s_scream

    haruka "Sensei!"

    "Without concern for you watching, Subaru slips her own large breasts from her body suit, rubbing them against Haruka's."

    play sound s_surprise

    haruka "Haaa!!!"

    subaru "I lasted for months... I'm curious to see how long it will take to break {i}you{/i}."

    play sound s_ahaa

    haruka "Aaah, ah..."

    subaru "You've always been the sensitive one. I'm sure we can make short work of you."

    show bg subaru_demon2 at top with dissolve

    "While still kneading one of Haruka's breasts, she moves her hand down to rub her crotch."

    play sound s_moans_quiet

    haruka "Nghh..."

    subaru "Hmmm... We need to get you wet. Let's see if you're as frigid as they remembered."

    haruka "T-They? Who..."

    subaru "Who? The Noroi, of course! Who do you think took us in!"

    haruka "The Noroi? Demons! H-How did you talk to them... What..."

    play sound s_evil_laugh

    subaru "Oh, they're here... They're in my head, even as we speak! I {i}am{/i} one of the Noroi now, you silly child!"

    subaru "And I am going to train you to be like me! Now, let's see..."

    "She starts rubbing your pupil's clit, making her squirm."

    subaru "Let's see if you're a natural slut, or if you need to be broken, like I was."

    haruka "No! Anything  but the Noroi! Anyone, help! [MC.name]!"

    "Haruka's voice shakes with utter fear."

    subaru "[MC.name] is the one who caught you, you stupid bitch. He's not going to lift a finger to help you."

    "She presses her lips against Haruka's neck."

    haruka "Mmmmh..."

    "She bites down, and Haruka can't suppress a moan."

    haruka "Ahhh..."

    "She feels a tongue run along her skin, and Subaru reaches her ear."

    subaru "You have such a pretty neck, it makes me want to sink my teeth into you... *hiss*"

    haruka "Please, stop..."

    subaru "*licks* Hush now..."

    "Subaru increases the pace of fingers, and slowly Haruka's body seems to react in spite of her defiance."

    haruka "Your arm... How..."

    subaru "The arm? Oh, it's nothing, you should know growing new flesh is nothing to us Noroi."

    subaru "In fact, let me show you something... A lot cooler."

    play sound s_mystery

    show bg subaru_demon3 at top with dissolve

    "Haruka's eyes widen in shock as she sees a bulge growing under Subaru's panties, until it rips them open to reveal a large and thick penis."

    subaru "See? I can just grow this with the power of my mind... You're very lucky, as you're going to be the first one I try this on."

    play sound s_scream_loud

    haruka "No!!! Get this away from me!"

    "She struggles with all her might, but she is well bound."

    subaru "Don't worry, my sweet, I'll make sure you enjoy it!"

    haruka "NOOOO!" with vpunch

    "Subaru bumps her large cock against Haruka's exposed belly, leaking sticky pre-cum all over her navel."

    subaru "Will this really fit in? Oh well... Only one way to find out."

    "Haruka closes her eyes as Subaru rubs her cock against her pussy."

    haruka "Please... No... Please..."

    "Despite Haruka's best efforts, her pussy lips are opening up to let Subaru in."

    subaru "Let's go for it."

    show bg subaru_demon4 at top with dissolve

    play sound s_screams

    haruka "AAHHH!" with vpunch

    "Subaru slams her cock inside her former pupil's pussy, forcing it wide open."

    subaru "So this is what it feels like to have a dick... Amazing..."

    haruka "Nooo... Please, stop!" with vpunch

    "Subaru's demonic cock is so large that you can see Haruka's underbelly get swollen by it."

    subaru "I wonder if I can make you pregnant like this..."

    haruka "Aah, ah... No..." with vpunch

    "She slams her hips against Haruka's, her cock buried to the hilt."

    show bg subaru_demon5 at top with dissolve

    subaru "Now, let the fun begin!"

    "Subaru starts moving back and forth, fucking Haruka's pussy."

    haruka "Ahh... Ahh..." with vpunch

    "Haruka starts moaning against her will."

    haruka "Aah! Aah!" with vpunch

    "Subaru grabs her boobs, kneading them as she thrusts her cock deep into Haruka."

    haruka "No! Nooo..."

    subaru "You're so tight... It's amazing! It seems you weren't raped near enough..."

    haruka "No!" with vpunch

    "Subaru slams her hips against Haruka."

    haruka "Ahh..."

    "She slams even deeper, pressing her belly against Haruka's, which makes her moan louder."

    subaru "Oh, but you will learn to love being raped... Don't worry, everyone here at the prison will gladly help..."

    haruka "Nooo!" with vpunch

    "Subaru is hitting all the right spots inside Haruka, making her moan uncontrollably."

    subaru "You are so wet now... You get aroused when I talk of rape, don't you?"

    haruka "No! Ahh..."

    subaru "I was thinking to give you away to some convicts for a week, would you like that?"

    haruka "Aah... Aaah... No!" with vpunch

    "Subaru starts pounding her faster, fucking her senseless."

    haruka "Aaah!"

    "You can tell Haruka's mind is completely overwhelmed. She seems to have no fight left in her, and whimpers like a wounded animal."

    subaru "This is your life now, Haruka... You can thank [MC.name] for that. Better learn to enjoy it."

    haruka "No... *sob*"

    subaru "Hush now, child... I'm going to impregnate you."

    haruka "Nooo!" with vpunch

    subaru "I'm cumming!" with flash

    play sound s_orgasm

    show bg subaru_demon6 at top with doubleflash

    "Subaru slams her cock inside Haruka, and shoots a thick load of semen inside her, filling her to the brim."

    "Haruka screams at the top of her lungs, feeling the burning hot liquid flood her womb."

    haruka "AAAAAAAAAAHHH!!!"

    with flash

    "Subaru cums so much that her seed overflows and drips from Haruka's pussy."

    show bg subaru_demon7 at top with flash

    subaru "Boy, what a mess... Having a cock is surely something. I'm going to enjoy the hell out of that thing."

    return

label c3_haruka_arrested():

    "Suzume came back to report."
    
    show expression bg_bro at top
    with dissolve
    show suzume bend with dissolve

    suzume "Hey Boss. So I took Haruka into custody. The Princess handled it herself."

    suzume "I avoided talking to Kenshin entirely. We never know what those knights are up to."

    you "Good."

    suzume "The Princess said to thank you and to asked me to give you these rewards."

    $ MC.change_gold(2500)
    call receive_item(rep_item) from _call_receive_item_29
    $ story_flags['haruka path'] = "arrested"
    $ game.set_task(None, "story")

    you "Nice! Was there anything else?"

    suzume "What, did you think she would give us, like, a dozen complimentary buns stuffed with fine bunting meat and Borgian olives? I would never keep that from you."

    you "That's... Strangely specific."

    suzume "*BUUUUURP*" with vpunch

    suzume "Just ignore that."

    scene black with fade

    return

label c3_haruka_captured():
    "That night, you decide to pay a visit to your new captive."

    play music m_haruka fadein 3.0

    you "Gizel should be in there already..."

    play sound s_open

    scene black with fade
    show bg haruka bondage1 at top with dissolve

    gizel normal "Ah, [MC.name]. How good of you to join us."

    gizel smirk "I took the liberty of preparing her a little."

    you "Wow, that's some serious knot-work. Is she still out?"

    gizel "Yup. But it shouldn't be long before she wakes up. Perhaps we can speed that along."

    play sound s_punch

    "*SMACK*" with vpunch

    show bg haruka bondage2 at top with dissolve

    play sound s_surprise

    haruka surprise "Ah!"

    gizel "Wakey wakey, lil' girlie..."

    play sound s_scream

    haruka "What? Who's there? Where am I???" with vpunch

    haruka "M-My magic... I can't feel it, it's gone..."

    you "Relax, Haruka. It's no use panicking."

    you "After all, you'll be with us for a big long while."

    "You take out her blindfold."

    show bg haruka bondage3 at top with dissolve

    play sound s_surprise

    haruka "It's you! You monster! I should have killed you when I had the chance..."

    haruka angry "Where am I? Where's Subaru? Tell me!" with vpunch

    you "Forget about Subaru. She's beyond your ability to help."

    play sound s_evil_laugh

    gizel "You should worry more about yourself, for now. Because your training is about to start... And I will be in charge."

    haruka "My training? What are you even talking about?"

    haruka blush "And w-why am I... Naked..."

    gizel "Well, I'm sure you can take a good guess, can't you? You've been there before, haven't you?"

    show bg haruka bondage4 at top with dissolve

    play sound s_surprise

    haruka "No, wait, don't do anything to me... I'll just go, I'll leave you in peace, but stop..."

    play sound s_punch
    show bg haruka bondage5 at top with dissolve

    "*SPANK*" with hpunch

    play sound s_scream

    haruka "AH!!!"

    gizel upset "Shut up now, slave! It's time you begin to learn your place."

    show bg haruka bondage6 at top with dissolve

    gizel "First of all, [MC.name] here is 'Master' to you, and I am Mistress Gizel."

    gizel "Say it!" with vpunch

    haruka "No, I..."

    play sound s_punch
    show bg haruka bondage5 at top with dissolve

    "*SPANK*" with hpunch

    play sound s_scream

    haruka "AAAAH!!"

    play sound s_punch
    pause 0.3
    play sound2 s_punch

    "*SPANK* *SPANK*" with hpunch

    play sound s_screams

    haruka "AAAH! No! Stop, stop!"

    gizel "SAY IT!" with vpunch

    show bg haruka bondage6 at top with dissolve

    haruka "M-Mistress Gizel... M-M-Master [MC.name]..."

    gizel normal "Good."

    play sound s_punch
    show bg haruka bondage5 at top with dissolve

    "*SPANK*" with hpunch

    play sound s_scream_loud

    haruka "OUCH!!!" with vpunch

    show bg haruka bondage6 at top with dissolve

    haruka "What did you that for? M-Mistress Gizel..."

    gizel smirk "Oh, nothing. I just felt like it."

    gizel "Over time, you will discover that pain is one of the best forms of pleasure. But we'll go step by step."

    "Gizel takes out equipment: clips with weights attached to them."

    "Her outfit is so skimpy, you really wonder where she keeps all these things."

    gizel normal "Let's not dance around the bush: your best feature is that huge pair of knockers. We need to make sure they're sensitive enough to pleasure our guests."

    haruka "G-Guests?"

    play sound s_clang

    show bg haruka bondage7 at top with dissolve

    haruka "Ow!!!" with hpunch

    gizel "Very nice! Not only is this going to stretch your nipples properly, but it will teach you that pleasure and pain mix well together."

    gizel "Maybe I'll leave you like this all night. This would be a teachable moment."

    play sound s_scream_loud

    haruka "No! You can't do that to me! Help!!!" with vpunch

    show bg haruka bondage8 at top with dissolve
    play sound s_punch
    pause 0.3
    play sound2 s_punch

    "*SPANK* *SPANK*" with hpunch

    play sound s_screams

    haruka "OW! OUCH!!!"

    gizel upset "What was that you were saying?"

    show bg haruka bondage9 at top with dissolve

    haruka defiant "..."

    gizel normal "You're still defiant, but that is to be expected from a new slave. We'll break you soon enough."

    haruka "Y-You called me a slave... What do you mean?"

    gizel smirk "Oh, just that you belong to [MC.name] now. I had you magically branded at the black market while you were passed out."

    gizel "It's all too easy to kidnap a girl like you. It cost me next to nothing to grease the Slavers' Guild paws to look the other way."

    gizel normal "No one knows you in Zan, no one cares for you here. All you have left is to work for us... I mean for [MC.name]."

    haruka "[MC.name]? But he's... He's..."

    play sound s_surprise

    haruka surprise "A brothel owner!" with vpunch

    gizel "You're finally catching up, aren't you?"

    haruka blush "No, don't make me... No..."

    play sound s_evil_laugh

    gizel smirk "Anyway. I think we've dilly-dallied long enough."

    gizel "[MC.name], will you do the honors?"

    stop music fadeout 3.0

    you "My pleasure."

    "Coming from behind Haruka, you enter her gaping pussy with no warning."

    show bg haruka bondage10 at top with fade
    play sound s_scream

    haruka "AAAAH!!!" with vpunch

    "It is easier than you thought. Seems like Gizel's ministrations had a bit of an effect on her body already."

    play sound s_moans

    haruka "Oh, aah..." with hpunch

    "You start moving your hips back and worth, enjoying the way Haruka's body bounces off you as she is dangling from the ceiling."

    gizel smirk "Look at you, taking it all in stride!"

    gizel "You're doing better than expected for a first time. We'll make a good whore out of you yet."

    haruka "No! I'm no... Whore!"

    play sound s_scream_loud

    haruka "Aaaah!" with hpunch

    "You increase your pace, making sure to hit her deepest parts with every thrust."

    gizel "This is only the beginning of your training, but already I can tell it's going to go well."

    gizel blush "I think your rape fetish is going to help us along..."

    play sound s_surprise

    haruka "R-Rape fetish? No! I don't have anything like that!!!" with vpunch

    play sound s_moans

    "In spite of her denegations, you can feel the moistness of her pussy as she bounces off your dick."

    gizel "Oh, but you can deny it all you want, I {i}know{/i} it's true... It takes one to know one."

    haruka "Aaah, aaaah, aaaah..." with hpunch

    "You have gone on for long enough, and decide it's time to let yourself go. You will have plenty of other opportunities to use this pussy later."

    you "Ooh, omph... Take that, Haruka!"

    play sound s_scream_loud

    haruka "AAAAAH!!!" with vpunch

    show bg haruka bondage11 at top with flash

    "Shooting your load deep inside Haruka's pussy, you fill her to the brim with hot cum."

    show bg haruka bondage12 at top with doubleflash

    play sound s_screams

    haruka "Oooh... Aaaah... You did... Inside..."

    gizel "My, my, that's a great creampie if I ever saw one!"

    gizel "To think we are only getting started... I'm salivating."

    haruka "Ohhh..."

    "Haruka cannot hear Gizel's taunts, as she just passed out."

    $ MC.change_prestige(3)

    "Gizel turns to you."

    gizel normal "Listen, I'll take over her training for now. We need to make sure she is completely broken before we let her around any customer."

    gizel "I'll use my minions at the farm. Make sure I have all of the minion types available. I will need to experiment with different approaches..."

    you "All right."

    gizel "And give me that rune. It will keep her under control when she is out of her cell."

    call remove_item(earth_rune, definite_article=True) from _call_remove_item_7

    scene black with fade

    "Gizel will train Haruka at the Farm with the help of her minions. Make sure she has {b}every type of minion available{/b} for this."

    # INIT BREAKING COUNTER
    $ NPC_haruka.flags["stallion counter"] = 0
    $ NPC_haruka.flags["beast counter"] = 0
    $ NPC_haruka.flags["monster counter"] = 0
    $ NPC_haruka.flags["machine counter"] = 0
    $ NPC_haruka.flags["farm completed"] = 0

    $ story_add_event("haruka_break_test", "daily")

    $ story_flags['haruka path'] = "captured"

    return


# Haruka captured events

label haruka_break_test(): # Fires up every morning after capturing Haruka

    # Step 1: Find a relevant minion type

    python:
        for min_type in all_minion_types:
            if NPC_haruka.flags[min_type + " counter"] < 4 and farm.has_minion_type(min_type):
                break
        else:
            min_type = None

    # Step 2: Train

    if min_type:
        $ NPC_haruka.flags[min_type + " counter"] += 1

        if NPC_haruka.flags[min_type + " counter"] < 4:
            $ notify("Haruka trained with a %s at the Farm." % min_type, pic="side haruka blush")
        else:
            call haruka_farm(min_type) from _call_haruka_farm
            $ NPC_haruka.flags["farm completed"] += 1
            $ renpy.block_rollback()

        if NPC_haruka.flags["farm completed"] == 4:
            $ story_remove_event("haruka_break_test", "daily")
            $ calendar.set_alarm(calendar.day + 1, StoryEvent(label="haruka_broken"))
        else:
            "You congratulate Gizel on her progress with Haruka. You look forward to the next part of her training."
    else:
        $ notify("Haruka couldn't train at the farm because some minion types are missing.", pic="side haruka blush", col=c_lightred)

    return

label haruka_farm(min_type): #! Add fixations and skill changes

    $ _min = rand_choice(farm.get_healthy_minions(min_type))

    if not _min:
        $ _min = "Bob"
    else:
        $ _min = _min.name

    if dice(2) == 1:
        play sound s_rooster
    else:
        play sound s_moo

    scene black with fade
    show bg farm at top with dissolve

    "Gizel called you to the farm, to check on the progress of her pensioner."

    gizel normal "Hey, [MC.name]. Haruka has been training hard lately. I thought you'd like to see the results."

    if min_type == "stallion":

        gizel "Now is the time for her morning stretch... [_min] is helping her."

        show bg haruka big1 at top with fade

        _min "[_min] going to stretch strong girl pussy. [_min] likes!"

        play sound s_surprise

        haruka angry "Get off me, you brute!"

        _min "Strong girl tied up good... Cannot punch [_min] like last time. That made [_min] sad..."

        haruka "Stop! Or, or..."

        show bg haruka big2 at top with dissolve

        haruka "*gasp*"

        play sound s_evil_laugh

        gizel smirk "Oh, my... I always forget [_min] gets that big when they fight back... He likes it."

        haruka blush "No, go away, you animal... Not again..."

        _min "Uhuhuh..."

        show bg haruka big3 at top with dissolve
        play sound s_scream

        haruka "EEEK!!!" with vpunch

        _min "Oh, strong girl pussy stretching good..."

        gizel "She's been getting plenty of practice, after all."

        with vpunch

        "[_min] is not done, though. Somehow he pushes his fat dick even deeper."

        show bg haruka big4 at top with dissolve
        play sound s_scream_loud

        haruka "AAAAH!!! It's going to break me in half!" with vpunch

        gizel "Don't be ridiculous. You know you can take it."

        show bg haruka big3 at top with Dissolve(0.2)

        _min "*grunt*"

        show bg haruka big4 at top with Dissolve(0.2)

        haruka "AH!" with vpunch

        show bg haruka big3 at top with Dissolve(0.2)

        gizel "Look at him go!"

        show bg haruka big4 at top with Dissolve(0.2)

        haruka "AAAAH!!!" with vpunch

        show bg haruka big3 at top with Dissolve(0.2)

        gizel "I think he's ready to..."

        show bg haruka big5 at top with flash

        _min "UAAAH!!!" with vpunch

        with doubleflash

        play sound s_mmmh

        haruka "NGGGGH!!!"

        with flash

        "Haruka shakes uncontrollably as [_min] releases a superhuman load deep inside her pussy."

        play sound s_ahaa

        haruka "Ahaaaa..."

        "Haruka is still shaking. With your expert eye, you can tell she just had a small orgasm."

        you "Woah, she came in spite of herself... And it hasn't even been five minutes!"

        gizel "Yeah... She's addicted to big dicks now. As she should be."

        play sound s_surprise
        show bg haruka big6 at top with dissolve

        haruka surprise "No! It's a lie!"

        gizel "Hmph, don't be such a killjoy. [_min], help her stretch a bit more."

        play sound s_roar

        _min "*GROAR*!"

        haruka "Nooo!!!" with vpunch

        "Not skipping a beat, [_min] slams his dick again inside Haruka's pussy."

        play sound s_ahaa

        haruka blush "Ahaa..." with vpunch

        "Well lubricated with his cum, [_min]'s fat cock keeps pounding Haruka's womb, making her moan harder."

        gizel "You can feel it, now, Haruka? Being raped by a fat dick is the best, isn't it?"

        play sound s_aah

        haruka "S-Stop... Aah!!!" with vpunch

        "Haruka's voice has become weak, it's like she's no longer there..."

        "But her hips started moving in spite of herself. It's like she's inviting [_min] to fuck her even harder, which he does."

        _min "*GRRRR*" with vpunch

        play sound s_evil_laugh

        gizel "Look, at that, [MC.name]! [_min] is going to cum again, and I can tell it's going to be a big one!"

        gizel "Say, it's your choice now: Where do you want it?"

        menu:
            extend ""

            "Cum inside her":

                gizel "So be it!"

                show bg haruka big7 at top with flash

                _min "UAAAAAAGH!!!"

                with doubleflash

                play sound s_scream_loud

                haruka "AAAAAAAH!!!!"

                "[_min] shoots an enormous load inside Haruka's pussy, stretching her belly full of thick cum."

                play sound s_orgasm
                with flash

                haruka "Oh, ah, aaahaaa!!!"

                "She cums more loudly this time."

                show bg haruka big8 at top with flash

                gizel "Wow, would you look at that... It's like you're pregnant with cum..."

                haruka "What... What's happening... to me..."

                gizel "Wait! I think there's some more left!"

                show bg haruka big9 at top with vpunch

                haruka "No, you c-can't be serious... NGH!"

                show bg haruka big10 at top with flash

                _min "*GRUNT*"

                with doubleflash
                gizel "That's my big boy!"

                show bg haruka big11 at top with flash

                play sound s_mmmh

                haruka "Aaaaah..."

            "Cum all over her":

                gizel "[_min], it's time for her morning shower!"

                play sound s_roar

                _min "GROAR!!!" with vpunch

                show bg haruka big12 at top with flash

                "[_min] obediently takes out his cock, shooting an enormous load all over her."

                with doubleflash

                play sound s_scream
                haruka "EEEK!!!"

                "Haruka's entire body is covered in sticky cum as the horny stallion empties his balls completely."

                show bg haruka big13 at top with flash

                play sound s_ahaa

                haruka "Ahaaa..."

                gizel "Woah, you're going to reek of cum all day after this..."

                haruka "Ughhh..."

                play sound s_evil_laugh

                gizel "Just like any other day, really. Bwahahaha!!!"


    elif min_type == "beast":

        gizel "Now is the time for her daily walk. She's enjoying some fresh air."

        show bg haruka beast1 at top with fade

        play sound s_surprise

        haruka blush "Mistress Gizel... How long do I have to stand like this..."

        haruka "I 'm cold..."

        gizel smirk "You're cold, are you?"

        "That won't do, you need something to warm you up."

        haruka "Yes, I..."

        haruka "Wait, what do you mean by that?"

        play sound s_whistle

        gizel "*whistle* [_min], come over here, you adorable critter!"

        haruka surprise "N-No, not [_min] again!" with vpunch

        play sound s_roar

        show bg haruka beast2 at top with dissolve

        "Running from the bushes, [_min] arrives on the scene, not hesitating a moment before climbing over Haruka."

        play sound s_scream

        haruka "Noooo!!!" with vpunch

        "With consumate skill, [_min] pushes Haruka's panties aside with his beastly dick, before shoving it inside her."

        haruka "AAAH!!!" with vpunch

        gizel "Come on, Haruka, your pussy should used to all sorts of animal dicks by now... Just focus on giving [MC.name] a good show."

        show bg haruka beast3 at top with vpunch

        haruka "EEEK! It's moving!"

        "The dog starts wiggling his hips, moving back and forth inside Haruka's pussy."

        gizel "You might think his dick is a bit small, but in reality it's swelling inside her, so it gets really thick."

        gizel "You feel that, Haruka?"

        play sound s_moans

        haruka "It's too much! It hurts! Aaaah..." with vpunch

        gizel "Pain is pleasure, I thought we had this covered by now."

        gizel blush "Now, tell me how it feels inside. Describe it."

        show bg haruka beast4 at top with dissolve

        haruka "It's... N-No... I'm so ashamed..."

        play sound s_roar

        "The beast increases its pace, frantically fucking Haruka with its weird dick."

        play sound s_scream_loud

        haruka "AAAH!!!" with vpunch

        gizel upset "Don't be impertinent. You know I have no patience for that. Answer my question!"

        haruka blush "I-It's growing inside me... Like an inflatable balloon..."

        gizel normal "And how does it feel?"

        play sound s_aah

        haruka "S-Strange... I don't know... Aaaah..."

        gizel "You know, I've noticed that our friend Haruka has a thing for big dicks..."

        gizel "Not only does she love being raped, but the more you ravage her pussy, the happier she gets."

        show bg haruka beast3 at top with dissolve

        play sound s_scream

        haruka "That's not tr... AAAAAH!!!" with vpunch

        gizel smirk "Oh yeah? Then you wouldn't like it if one of the stallions joined in?"

        play sound s_whistle

        gizel "*whistle*"

        show bg haruka beast5 at top with dissolve

        play sound s_aaah

        haruka "Ooooh...." with vpunch

        "Another minion joins the fray, poking his large dick on Haruka's face."

        play sound s_ahaa

        haruka "Ahaaa..." with vpunch

        "The beast keeps pounding her from behind, while pre-cum from the stallion's dick leaks on her face and body."

        haruka "Oooh..."

        "She looks lost within herself, overwhelmed by the strong smell of bodily fluids."

        gizel "I think we should turn up the humiliation even further. [MC.name], any ideas?"

        menu:
            extend ""

            "Fuck her mouth":
                you "You, the drooling moron, don't just stand there, use her mouth!"

                show bg haruka beast10 at top with dissolve
                play sound s_sucking

                "Obediently, the stallion starts fucking her face, shoving his dick deep inside her throat."


                haruka "Nggh, ngggh..." with vpunch

                "Haruka is doing her best to take his dick in, seemingly turned by being skewered from both sides."

                play sound s_roar

                _min "GRRRR!!!" with vpunch

                "Meanwhile, the beast is fucking Haruka even faster. You can tell it is close to the big finish."

                haruka  "NGGGH!!!" with vpunch

                "Haruka moans as the stallion pushes his monstrous dick all the way down her throat. He is about to explode as well."

                show bg haruka beast11 at top with flash

                "*SPURT* *SPURT*"

                with doubleflash

                play sound s_mmh

                haruka "*cough* *cough*... Aaaah..."

                "The stallion cums all over Haruka's face and hair."

                show bg haruka beast12 at top with flash

                play sound s_screams

                haruka "Aah, aaah, AAAAAAAAH!!!"

                play sound s_orgasm
                with doubleflash

                "It isn't long before [_min] cums as well, making Haruka erupt into an orgasm."

                haruka "Oh no... I came..."

                show bg haruka beast13 at top with dissolve

                play sound s_ahaa

                haruka "What have I... Become... Aaaah..."

            "Piss on her face":
                $ MC.evil += 2

                you "You, there, move it. I need to pee. Let's see how she likes that."

                play sound s_surprise

                haruka surprise "N-No!!!" with vpunch

                play sound s_roar

                show bg haruka beast6 at top with flash

                _min "*grunt*"

                with doubleflash

                "Oblivious to everything, the animal has reached its limit, shooting a wad of beastly cum deep inside Haruka's pussy."

                gizel "Look at that! She took it like a pro... Just like a real bitch in heat."

                show bg haruka beast7 at top with flash

                haruka blush "D-Don't say... That... I am no... Animal..."

                gizel "Oh really? You're just to prideful to admit to your true nature. But we'll do something about that."

                "Instructing the stallion to move aside, you whip out your dick."

                show bg haruka beast8 at top with dissolve

                play sound s_pee

                "*PEE*"

                haruka "Aaah! N-Nooo! *gulp*"

                "As she opens her mouth to protest, some of your pee lands on her tongue."

                haruka "EEEK!" with vpunch

                "She squeals, but that only makes it worse."

                show bg haruka beast9 at top with dissolve

                you "Phew, I feel better. Seems like she'd make a good human toilet."

                play sound s_evil_laugh

                gizel normal "That's an interesting idea. Maybe I'll have her sleep in the pigsty, as well."

                haruka "Oh no..."

                haruka sad "How far... Have I fallen..."

        gizel "Show's over."

        gizel smirk "I think I'll let her play with [_min] for today. *grin*"

    elif min_type == "monster":
        show bg haruka monster1 at top with fade

        you "G-Gizel? What's this?"

        "You give an uneasy look to the bulbous 'thing' occupying the middle of Haruka's cell."

        gizel smirk "Oh, don't worry, it's just [_min]. Say hi, [_min]."

        play sound s_bubbling

        _min "*unintelligible*"

        you "What about Haruka? Is she gone?"

        gizel "Oh, she's here, all right."

        gizel "[_min], show him."

        play sound s_stone
        show bg haruka monster2 at top with dissolve

        haruka blush "*cough* *cough* *gasp*"

        "The monster spreads its 'jaws' apart, revealing the exposed body of Haruka, floating on a wriggling mass of slimy tendrils."

        gizel "Haruka's been in there for a couple of hours already. Look how wet she is."

        gizel "Who knows how many orgasms she's had while she was inside? [_min]'s juices are strong aphrodisiacs."

        play sound s_mmmh

        haruka "Aaaah... Uhmmm..."

        gizel "Her body is super sensitive right now. She could cum from anything."

        play sound s_ahaa

        haruka "Nggh... I... Can't... Think... Straight..."

        gizel "Look, I'll show you something fun."

        show bg haruka monster3 at top with dissolve

        haruka "Aaaah!!!"

        "Gizel attaches a string to each of Haruka's nipples, giving you the end of one as she holds on to the other."

        gizel "Ready? On your mark, get set..."

        show bg haruka monster4 at top with vpunch
        gizel "GO!!!"

        play sound s_screams
        with flash
        haruka "AAAAAH!!!"

        play sound s_orgasm_fast

        "You both pull on the strings at the same time, painfully stretching Haruka's nipples."

        haruka "Oooh..." with flash

        "Haruka cums immediately, and she even starts squirting, splashing love juice all around."

        "[_min] looks pleased, inasmuch as you can tell for something that doesn't sport a face."

        show bg haruka monster3 at top with dissolve

        haruka "M-Make it stop... I keep... Cumming... It's too strong..."

        gizel "Hmph, you don't know what's good for you..."

        show bg haruka monster2 at top with dissolve

        "Reluctantly, Gizel removes the strings from Haruka's tits."

        haruka "I can't take any more..."

        gizel "Fufufu, you think we're done already?"

        gizel blush "[MC.name], my dear, I'm going to need your help."

        you "Sure."

        gizel "I've made sure to give Haruka's pussy plenty of training in the last days..."

        gizel "... But her asshole's been kind of neglected."

        gizel "Since you're here..."

        you "Say no more."

        play sound s_dress

        "*unzip*"

        haruka "What... What are you..."

        show bg haruka monster5 at top with dissolve

        play sound s_scream

        haruka "AAAH!!!" with vpunch

        "Haruka's asshole is slippery with all the fluids covering her, so you can slide your cock inside her easily."

        play sound s_mmmh

        haruka "My ass! You went all in... You're going to break it!"

        play sound s_moans

        "Even as she says that, Haruka can't control her moans. You can see her getting wetter with every thrust of your cock into her stretched asshole."

        haruka "Aaah... Aaah..." with vpunch

        "Moving your lubricated dick inside Haruka's butt is easy, and you increase your pace. Her hips start moving in tythm with your dick."

        haruka "My ass is being violated... B-But... W-Why..."

        play sound s_aaah

        haruka "Why does it feel so good... Aaah..." with vpunch

        "Tendrils tickle your balls, making you feel weird. Haruka's ass clenches around your dick, and you can tell she is in for another orgasm."

        play sound s_mmh

        haruka "Mmmh, mmmmh..." with vpunch

        "Hearing Haruka moan sexily as you fuck her lusty ass proves too much for you."

        show bg haruka monster6 at top with flash

        play sound s_scream_loud

        haruka "AAAAH! C-C-CUMIIIIIING!!!!"

        play sound s_orgasm

        with doubleflash

        "You cum hard inside Haruka's butt, filling her up with your spunk."

        with flash

        "The tentacle around her belly decides to squeeze it hard, making her squirt sperm out of her asshole."

        haruka "Oh no... I came so hard..."

        play sound s_evil_laugh

        gizel "Seems like she's a natural for anal..."

        $ MC.change_prestige(3)

        "Taking out your cock, you wipe it in Haruka's hair for good measure... But she doesn't notice it, as she is already passed out from multiple orgasms."

    elif min_type == "machine":
        gizel "She's in the middle of a training session with [_min]. I set its programming to hardcore..."

        play sound s_vibro
        show bg haruka machine1 at top with fade

        "You find Haruka in the basement, riding a strange contraption that you recognize as [_min]."

        haruka blush "M-Master... [MC.name]... Aaaah..."

        gizel "See? She addressed you properly. She is starting to know her place, now."

        gizel "She's been here for half an hour already. [_min] has been working her nice and slow..."

        play sound s_ahaa

        haruka "Mmmh..."

        gizel "Haruka, would you be a doll and describe to your master here what [_min] is doing to you?"

        play sound s_vibro

        haruka "Nggh... Ah!!!" with vpunch

        haruka "T-There's a dildo... In my pussy..."

        haruka "And another one... In my ass..."

        gizel "Good girl! Here, let me give you a small reward."

        play sound s_vibro
        show bg haruka machine2 at top with vpunch

        "Gizel turns up the vibration speed on [_min]."

        play sound s_aah

        haruka "Aaaah!!!"

        gizel normal "I am currently training her to resist orgasm, because she has become a little too slutty lately."

        you "Too slutty? Is there any such thing as 'too slutty'?"

        gizel "Well, you don't want her to be unable to control herself around customers, do you?"

        gizel "It's a normal part of training of a sex slave to learn to restrain your urges..."

        play sound s_vibro
        show bg haruka machine3 at top with vpunch

        haruka "A sex slave... Me..."

        "This time, the words 'sex slave' rolled off her tongue more easily. Could it be the beginning of... Acceptance?"

        you "What's keeping her from cumming?"

        gizel smirk "Fufufu... It's one of my better tricks."

        gizel "Haruka spent the whole night milking stallions, feeling a large vat full of cum."

        play sound s_vibro

        haruka "N-Ngh..." with vpunch

        gizel "The vat is right underneath the contraption. If she cums, [_min] is programmed to open a valve, and her precious holes will be filled up with pressured cum."

        gizel "It will really mess up her insides. So she'd better not cum, or else..."

        "Haruka blushes bright red, and you can tell she is nearing her limit."

        gizel "You're not about to let it slip, now, sugar?"

        gizel "Think of all the hot cum that would enter your pussy and ass... It would mess you up forever..."

        play sound s_ahaa

        haruka "N-Nggh..." with vpunch

        play sound s_vibro

        "Winking at you, Gizel turns up the vibrations even more."

        play sound s_scream

        haruka surprise "N-No! Don't!!! I can't resist that much..."

        "Panicked, Haruka does her best to try to hold it together."

        gizel "You know, even though the pain would be unbearable, I bet you would cum so hard if that happened..."

        play sound s_vibro

        gizel "Think of all that sweet cum... Just waiting to fill you up..." with vpunch

        play sound s_aah

        haruka "Oooh..." with vpunch

        "Haruka blushes bright red. She clenches har teeth, but you can tell she is losing this fight."

        play sound s_mmh

        haruka "Gallons of c-cum... Shooting... Inside... Me..."

        play sound s_scream_loud

        show bg haruka machine2 at top

        haruka "AAAAH!!!!" with vpunch

        play sound s_splash
        show bg haruka machine4 at top with flash

        "Unable to resist, Haruka finally cums. Within a split second, [_min] opens the valve and highly pressured cum starts erupting through."

        play sound s_scream_loud

        haruka "AAAAH!!! It's filling me up! I can't take iiit!!" with doubleflash

        play sound s_evil_laugh

        gizel "Oh my, you've really done it this time!"

        gizel "It went all in! Look, she's about to burst with cum."

        show bg haruka machine5 at top with dissolve

        haruka "My belly... My insides... What's happening to me..."

        gizel "You know what, let's turn the vibrations up to eleven. She really deserves it."

        haruka surprise "Wait, that wasn't the maximum?"

        play sound s_vibro

        haruka blush "G-GHHHH!!!" with vpunch

        haruka "Oh no!!! I'm... I'm cumming again!!!"

        show bg haruka machine6 at top with flash

        play sound s_splash

        "*SPLASH* *SPLASH*"

        play sound s_screams

        haruka "AAAAAAAAARRH!!!"

        play sound s_orgasm

        "Cumming hard, Haruka squirts semen everywhere as it splashes out of her cunt and asshole."

        gizel "Phew, that was a good lesson. I doubt she'll be able to walk for a while after this, but it was worth it."

        haruka sad "Aaaah... I'm filled with cum... And I came so hard... I'm such a degenerate now..."

    scene black with fade
    return

label haruka_broken:

    play sound s_rooster

    scene black with fade
    show bg farm at top with dissolve

    show gizel normal with dissolve

    gizel "Good news, [MC.name]! All my hard work on Haruka has paid off."

    show gizel at left with move
    show haruka_humble at right with dissolve

    haruka blush "Hello, Master [MC.name]."

    gizel smirk "Tell him what you told me."

    haruka "..."

    gizel upset "Tell him!" with vpunch

    haruka sad "Yes. Master, I..."

    haruka "I'm sorry. I was blinded by my pride, but I now realize..."

    haruka "I have no skill as a ninja, and I failed my mentor and my friends. I am worthless."

    haruka "Every time I tried to take matters into my own hands, I ended up failing completely. I am not fit to live a free life."

    haruka "I don't even know if I'm worthy of being a whore..."

    haruka "But if I need to use my weak body to please others, to atone for my sins, it is a fate I will accept."

    gizel smirk "There. That wasn't so hard, wasn't it? You're a slut that loves to be raped. There's no shame in that."

    haruka blush"..."

    gizel normal "Now that we took care of the small matter of breaking the girl's pride, let's think about the next step. [MC.name]?"

    menu:
        extend ""

        "Try her for yourself":

            you "Well, I was waiting for that day! Bring her to the brothel, I will personally make sure she's ready."

            scene black with fade
            show expression bg_bro at top
            with dissolve

            show haruka_humble with dissolve

            haruka blush "M-Master... What do you want me to do..."

            you "I want you to treat me like a VIP customer. Show me what you have learned."

            haruka "O-Okay..."

            you "Take the lead. I will be evaluating your performance."

            haruka "Yes Master..."

            scene black with fade
            show bg haruka cowgirl1 at top with dissolve

            haruka "H-Hello Sir, welcome to [brothel.name]."

            haruka "My name is Haruka, and I am here to... Serve all your needs today..."

            play sound s_sigh

            haruka blush "I hope... Mmh... My filthy body can make you happy... Hmmm..."

            you "Don't mumble. Some customers enjoy a shy girl, but you are expected to take the lead, remember?"

            haruka "Ahem, yes Master."

            haruka "Would you like to touch my breasts? I am told they're the best part of my body."

            play sound s_dress

            show bg haruka cowgirl2 at top with dissolve

            haruka "Hmmm... I hope you like them..."

            you "Not bad, Haruka. But look at me, down there. Can't you see I need something?"

            haruka "Oh! Oh my, Sir, you are already rock-hard...I-It makes me happy..."

            haruka "Here, would you like to rub your penis inside my body suit?"

            play sound s_dress

            you "Hmmm... That's kinky..."

            haruka "Something smells good... I think you're leaking pre-cum already."

            play sound s_aah

            haruka "It's making me wet... Haaa..."

            you "That's nice, Haruka. Keep the dirty talk coming."

            play sound s_mmmh

            haruka "Aaah, hmmm..."

            haruka "Sir, if you keep rubbing against me like that, I'm going to lose control..."

            haruka "My dirty pussy is all wet now... I need s-something... Inside me..."

            you "Then what are you waiting for? Take matters into your own hands!"

            show bg haruka cowgirl3 at top with dissolve

            "*SQUISH*" with vpunch

            "Guiding your dick with her soft hand, Haruka pushes it inside her."

            "She is already completely wet, and her pussy engulfs your shaft easily."

            play sound s_ahaa

            haruka "Aaaahaa..." with vpunch

            haruka "Oh, Mister, you're so big... I am so lucky to serve you..."

            "She starts grinding her hips, pleasantly stimulating your dick."

            you "You love big cocks, don't you?"

            haruka "Y-Yes, I do... I like a huge dick stretching my pussy to the limit..."

            you "Don't forget that not all customers are well-endowed. You don't want to make the little ones feel bad..."

            haruka "Oh, that's right... Of course, Master, I won't tell them that... Unless I mean it."

            you "Good. Keep moving."

            play sound s_aaah

            haruka "Hmm... Aaah..." with vpunch

            "You lay back and enjoy the show, as Haruka is doing all the work."

            play sound s_mmh

            haruka "Hmmm... Aaaah..." with vpunch

            "Even though you are barely doing anything, Haruka seems to enjoy herself well enough."

            play sound s_moans

            haruka "Oooh... Aaah..." with vpunch

            "Her pace is increasing, and it seems like she may be able to bring herself off by herself."

            you "Hey, talk to me. Don't focus on yourself, focus on the customer."

            haruka "Right... S-Sorry, Master."

            "She clenches her pussy around your shaft with surprising strength."

            haruka "Do you like... That..?"

            you "Oh yes."

            haruka "Let me massage your cock with my slave pussy. Master- I mean, Sir."

            play sound s_moans_short

            haruka "Aaaah, aaaaah!" with vpunch

            "She is bouncing off your dick hard now, and you can't help but feel your excitement building up."

            haruka "Ooooh... Aaaah..." with vpunch

            show bg haruka cowgirl4 at top with dissolve

            "Your cock hits her cervix repeatedly, making her moan even deeper."

            you "I want to cum inside you, Haruka."

            haruka "O-Of course, Sir..."

            haruka "Today is not a safe day, but... I am taking magic contraception, so don't worry."

            you "Like I care about that! Get ready, I'm going to creampie you."

            play sound s_mmh

            haruka "Y-Yes, Sir... Mmmmh..." with vpunch

            show bg haruka cowgirl5 at top with flash

            you "*GROAN*"

            with doubleflash

            play sound s_scream

            haruka "AAAAAAAAH!!!"

            play sound s_orgasm

            with flash

            "Haruka cums at the same time as you, crying out loud as you fill her with creamy semen."

            haruka "Ooooh... Master [MC.name]..."

            you "Hmmm... It was good... But stay in character."

            haruka "O-oh, sorry. Sir."

            "She keeps rubbing her hips against you for a while longer, still basking in the feeling of her orgasm."

            you "You'll make a fine whore. No doubt about that."

            show bg haruka cowgirl6 at top with dissolve

            haruka "T-Thank you."

            "Giving you an inviting smile, she scoops up some of your love juice with her finger."

            "She places it in her mouth, and starts sucking on it suggestively."

            you "Hmm, that's a nice touch."

            haruka "I thought the customers might like it when I do that."

            you "I'm sure they will."

            $ MC.change_prestige(3)

        "Test her with customers":

            you "About time! Let's round up some customers, make sure she is ready."

            $ cust = rand_choice(get_available_populations()).get_rand_name()

            scene black with fade

            "Sill gathered a group of regular customers, led by a [cust]."

            "They were intrigued by the perspective of getting it on with one of the infamous kunoichi."

            show bg onsen at top with dissolve

            show haruka_swimsuit with dissolve

            haruka blush "Welcome to [brothel.name], dear guests. Please follow me."

            "[cust!c]" "Wow, she's super hot!"

            "[cust!c]" "I was expecting her to be all muscular and stuff but... Man, she's perfect!"

            haruka "Thank you Sir, you are very kind..."

            "[cust!c]" "And check that ass..."

            play sound s_boing

            "*SMACK*" with vpunch

            "The customer slaps Haruka's ass. For a split second, you worry she's going to strike him back, but she just blushes."

            haruka "Please follow me. *blush*"

            scene black with fade
            show bg haruka massage1 at top with dissolve

            "[cust!c]" "Hmmm... So that's the taste of Kunoichi sweat..."

            play sound s_aah

            haruka blush "Ah, Mister..."

            "The [cust] is playing with Haruka in the sauna, while his buddies leer and jeer."

            haruka "Mister, if you keep touching me all over... Aaaah..."

            "[cust!c]" "What's that? I don't understand... *squish*"

            show bg haruka massage2 at top with dissolve

            play sound s_ahaa

            haruka "Ahaaa..."

            "The customer rubs himself against Haruka's butt, caressing her inner thigh. She is getting visibly wet."

            "[cust!c]" "Ain't you a sensitive thing? I only started touching you, and you're in the mood already..."

            haruka "I'm afraid so... I am a dirty whore..."

            "[cust!c]" "Of course you are! [MC.name] knows how to pick them."

            show bg haruka massage3 at top with dissolve

            "Other customer" "Man, you're having all the fun! Just looking at these titties, I get hard as fuck."

            haruka "S-Sorry, dear customer... You will get your turn..."

            show bg haruka massage4 at top with dissolve

            "More customers" "And don't forget about us too!"

            play sound s_sigh

            haruka "S-Sure..."

            "Other customer" "I wanna see those titties!"

            "[cust!c]" "Yeah, show us the goods!"

            haruka "O-Okay... Will you give me a little tip?"

            "[cust!c]" "Hmph... Here you go..."

            $ MC.change_gold(50)

            play sound s_dress

            show bg haruka massage5 at top with dissolve

            "All customers" "Whoah!!!"

            "Other customer" "Let me pull on these nipples... Hmmm, I wanna twist and tug them!"

            play sound s_surprise

            haruka "Aaaaaah!!! Please, Sir, I'm sensitive there..."

            "Other customer" "Shut up, whore, I paid, so I can be as rough as I want!"

            show bg haruka massage6 at top

            play sound s_scream

            haruka "Haaaah!" with vpunch

            "[cust!c]" "Look at her, she's not even trying to stop you!"

            "The customer is tugging at her nipples, eliciting painful moans from Haruka."

            "[cust!c]" "I've heard so much about the Kunoichi, but it seems that they are a joke..."

            haruka "N-No... The Kunoichi are not a joke... But I am not worthy of them."

            "Other customer" "You're just a slut, then, only good for taking cock? Am I right?"

            play sound s_sigh

            haruka "I... Yes, it's true."

            "[cust!c]" "Then enough fooling around! Get ready."

            play sound s_dress

            show bg haruka massage7 at top with fade

            haruka blush "Hmmm... Sir... Do you like this position?"

            "[cust!c]" "Damn right I do! Make sure to give my mates a great view!"

            "The [cust] spreads Haruka's legs apart, rubbing his manhood against her clit."

            play sound s_mmmh

            haruka "Hmmmh..."

            "It isn't long before he is rock-hard."

            "[cust!c]" "Enough waiting! I'm going in!"

            "Other customers" "*CHEER*"

            show bg haruka massage8 at top with dissolve

            haruka "AAAH!!!" with vpunch

            "[cust!c]" "Oh, your pussy's good! Feels like you were expecting me."

            haruka "Oh... It's my first for today... Mistress Gizel never left me that long without... Well..."

            "[cust!c]" "Come on, move your body! Show me how a Kunoichi fucks!"

            haruka "Y-Yes, Sir!" with vpunch

            "Moving her hips, Haruka starts fucking the customer enthusiastically, barely aware that she's being watched by the group."

            "[cust!c]" "Oh, you're good!"

            "Using the strong muscles in her thighs and pussy, she rides and squeezes the customer's dick in unexpected ways."

            "[cust!c]" "Oh, Shalia, she's strong! OH!!!"

            show bg haruka massage9 at top with flash

            play sound s_surprise

            haruka "Haaah! [emo_heart]"

            with doubleflash

            "Unable to resist, the [cust] explodes inside Haruka's pussy, smearing it with smelly cum."

            show bg haruka massage10 at top with flash

            play sound s_mmmh

            haruka "Hmmm..."

            "Other customer" "Bwahaha, you barely held in there for a minute!"

            "[cust!c]" "Grrr... She surprised me..."

            play sound s_ahaa

            show bg haruka massage11 at top with dissolve

            haruka "Ahaa..."

            haruka "Mister, you really came a lot... I'm happy..."

            $ MC.change_gold(100)

            "[cust!c]" "Here's a tip... I'm gonna need a moment to recover... Ooooh..."

            "Other customer" "Then it's my turn! Yeehah!"

            show bg haruka massage12 at top with dissolve

            play sound s_surprise

            haruka "Aaah, Mister!" with vpunch

            "Not wasting time, another customer jumps at the opportunity and starts fucking Haruka from behind."

            haruka "Oh, Mister, you're so rough!" with vpunch

            haruka "You're stirring up my insides..."

            "In spite of her protestations, Haruka seems lost in pleasure as the customer rams her doggy-style."

            "Other customer" "Come on, squeeze my dick like you did for him! Show me that Kunoichi power!"

            haruka "Aaah, hoh, oh..." with vpunch

            "Suddenly, Haruka tenses up, and you can almost see a shockwave riding out from her pussy, hitting the customer's dick."

            "Other customer" "OWHOOOH!!!" with vpunch

            show bg haruka massage13 at top with flash

            "Overwhelmed by pleasure, the customer cannot help but cum hard inside Haruka's tight pussy."

            with doubleflash

            "[cust!c]" "See? I told you, she's something else!"

            "Haruka's cunt keeps squeezing the customer's dick until she milks the last drop of his cum."

            show bg haruka massage14 at top with flash

            $ MC.change_gold(100)

            "Other customer" "Man... That was incredible... T-Take that, I think I'm gonna pass out..."

            "[cust!c]" "Then fuck off! I'm ready for round 2!"

            "Other customers" "Hey, what about us?"

            "[cust!c]" "Just get in line! I'm the one who got you in, so I get dibs on ninja pussy!"

            show bg haruka massage15 at top with dissolve

            haruka "Please, everyone, I must ask you for your patience..."

            "Customer" "Shut up! Hold my dick!"

            "[cust!c]" "I'm hard again! Do your worst, Kunoichi!"

            show bg haruka massage16 at top with dissolve

            play sound s_aaah

            haruka "Aaaah..."

            haruka "Aaaah!" with vpunch

            "[cust!c]" "Oh, yeah... It's even better the second time!"

            "Other customer" "I'm done waiting. Why don't I use her other hole?"

            haruka "M-Mister..."

            show bg haruka massage17 at top with dissolve

            haruka "Aaah!" with vpunch

            "The man pushes his cock near her tight asshole."

            haruka "P-Please, Sir! I haven't had much training with this hole yet!"

            "Other customer" "Perfect! Then I'll help you get more experience."

            show bg haruka massage18 at top with dissolve

            play sound s_scream

            "Ignoring her resistance, the fat man forces his cock deeper inside her ass."

            play sound s_moans

            haruka "Oh, I'm being fucked from both sides... Aaaah..." with vpunch

            "Both guys start fucking Haruka's holes in rythm, while she does her best jerking off the other customers with her hands."

            "[cust!c]" "C'm'on, Kunoichi, use your secret powers! Make us cum!"

            "Other customer" "Yeah, you can go all out!"

            haruka "Hmmmh... Aaah..." with vpunch

            "With a look of resolve, Haruka starts concentrating."

            haruka "A-As you wish... I will now use my whole body... To pleasure you..."

            haruka "OMAE WA! MOU IKU!!!!" with vpunch

            "Other customer" "What was that?"

            "[cust!c]" "I think it's a Kunoichi battlecry or som-"

            play sound s_wscream

            "[cust!c]" "OWHOOOOH!!!" with vpunch

            with vpunch

            "Haruka's entire body tenses up, and waves of energy radiate from her naked form as she squeezes the many dicks around her."

            show bg haruka massage19 at top with flash

            "*SPURT* *SPURT*"

            play sound s_scream_loud

            haruka "HAAAAAHH!!!" with doubleflash

            play sound s_orgasm_fast

            show bg haruka massage20 at top with flash

            "Other customer" "OOOOOF!!!"

            "[cust!c]" "*GROAN*" with doubleflash

            "All the customers cum one by one, showering Haruka with hot cum and creampying both her holes."

            "Haruka came hard as well, giving her all to satisfy the customers."

            show bg haruka massage21 at top with flash

            haruka "T-Thank you, dear customers..."

            haruka "I am lucky to receive your precious cum..."

            haruka "Please... Come again to [brothel.name]..."

            $ MC.change_gold(250)

            scene black with fade
            show bg onsen with dissolve
            show haruka_swimsuit with dissolve

            you "Whoah, well done, Haruka!"

            haruka blush "T-Thank you, Master."

            you "I must say, I was worried about how you'd do... But you handled it like a pro."

            haruka "..."

    you "Very good. Welcome to the team! You can start working tonight."

    haruka blush "S-Sure. Thank you for having me."

    haruka sad "(So this is my life, now... I wonder if I can get used to it.)"

    $ girl = create_girl("Haruka Takamori", force_original=True, level=10)

    call acquire_ninja(girl) from _call_acquire_ninja_1

    return

## End of Haruka events ##


# Generic acquire ninja menu #
label acquire_ninja(girl):

    if len(MC.girls) >= brothel.bedrooms:

        girl.char "B-But Master! There is no room in the brothel for me..."

        if farm.active and farm.has_room():
            you "You should go to a pen at the farm."

            girl.char "Okay..."

            $ NPC_gizel.flags["held_girl"] = None
            $ farm.programs[girl] = FarmProgram(girl)
            $ girl.init_after_acquire()
            call send_to_farm(girl, can_beg=False, can_cancel=False, can_follow=False) from _call_send_to_farm_5

            $ selected_destination = "farm"
            jump teleport

        else:

            you "Damn, the farm's pens are full at the moment..."

            gizel "I'll keep her around to do chores. Talk to me when you are ready to accomodate her."

            scene black with fade

            "Once you have room for [girl.name], click on Gizel's portrait at the {b}Farm{/b} to recover her."

            $ NPC_gizel.flags["held_girl"] = girl

    else:
        scene black with fade

        $ NPC_gizel.flags["held_girl"] = None
        $ MC.girls.append(girl)
        $ girl.init_after_acquire()

        "[girl.name] has joined [brothel.name]."

    return

#### END OF CHAPTER 3 EVENTS ####
