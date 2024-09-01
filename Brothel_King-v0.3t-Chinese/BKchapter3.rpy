#### CHAPTER 3 EVENTS ####

## Suzume events & NPC hints ##

label c3_suzume_hint(): # Happens after all three kunoichi hunts have been locked, or after the first summon of Homura

    scene black with fade
    show expression bg_bro at top with dissolve
    show suzume with dissolve

    if story_flags["homura summoned"]:
        suzume bend "Sooo... Did you learn anything interesting from your posh little girlfriend?"

        you "Do you mean... Homura? Are you stalking me, or something?"

        suzume doubt "Stalking? No way! I just watch you have sex some time, is all."

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

        you "Hey! We're not dat-... Why am I justifying myself to you?"

        suzume "Fufufu, don't get the wrong idea. I'm not the jealous type..."

        suzume "But just so you know, I could use a little boning. I am getting rusty, you know!"

        you "It's only been- wait."

        you "Actually, it's been a while. Come here."

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

    scene black with fade
    show expression bg_bro at top with dissolve
    show suzume naked with dissolve

    suzume "Aaah... That's better! [emo_heart]"

    you "Yes. But this doesn't bring us any closer to catching those pesky ninjas."

    suzume "Well, like I said, you can investigate with your contacts in the city. Or you can hit your noble girlfriend."

    you "For lack of better ideas... Okay."

    "You can now {b}visit your contacts{/b} by talking to suzume on the {b}city{/b} screen."

    if story_flags["homura summoned"]:
        "You coud also ask Homura for more hints, by summoning her from the {b}Plaza{/b}."
    else:
        "Homura also mentioned that she can help you if you tie her ribbon to a pole in the {b}Plaza{/b}, but you'll need an okiya first."

    $ story_flags["suzume hint seen"] = True
    $ suzume_hints_active = True

    return


label c3_update_hint_goals():
    python:
        for ninja, channel in [(NPC_narika, "story"), (NPC_mizuki, "story2"), (NPC_haruka, "story3")]:
            if not ninja.flags["hints"]:
                ninja.flags["hints"] = 0

            if ninja.flags["hints"] < 3:
                game.set_task("收集关于" + ninja.name + "的3个线索(%s/3)。" % str(ninja.flags["hints"]), channel, max_chapter=6) #! Change max_chapter
            else:
                game.set_task("和云雀再聊聊关于%s的事。" % ninja.name, channel, max_chapter=6) #! Change max_chapter

    return

label c3_interrogate_contacts():

    call c3_update_hint_goals() from _call_c3_update_hint_goals

    $ suzume("So, who would you like to question among your contacts in the city?", interact=False)

    $ contact_list =  [("side suzume", "Suzume, the Air Kunoichi", NPC_suzume),
                       ("side sill", "Sill, your trusty Slave Girl", NPC_sill),
                       ("side papa", "Papa Freak, the Weird Old Man", NPC_freak),
                       ("side jobgirl", "[jobgirl_name], the Quest Giver", NPC_jobgirl),
                       ("side kenshin", "Kenshin, the Knight Commander", NPC_kenshin),
                       ("side satella", "Satella, the Night Mistress", NPC_satella),
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
        $ contact_list.append(("side roz", "Roz, the zealous Guard Lieutenant", NPC_maya))
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

    menu:
        "Who do you want to ask [npc.name] about?"

        "询问Narika的情报, 虚空忍者" if NPC_narika.flags["locked"] or debug_mode:
            "You tell [npc.name] about {b}Narika{/b}, the Kunoichi you are looking for, and what she's been up to."
            $ nin = NPC_narika

        "询问Mizuki的情报, 水之忍者" if NPC_mizuki.flags["locked"] or debug_mode:
            "You tell [npc.name] about {b}Mizuki{/b}, the Kunoichi you are looking for, and what she's been up to."
            $ nin = NPC_mizuki

        "询问Haruka的情报, 土之忍者" if NPC_haruka.flags["locked"] or debug_mode:
            "You tell [npc.name] about {b}Haruka{/b}, the Kunoichi you are looking for, and what she's been up to."
            $ nin = NPC_haruka

        "询问关于元素屏蔽密室的情报" if npc == NPC_freak and NPC_freak.flags["holding info"]:
            "You talk to {b}Papa Freak{/b} about the secret magic-proof cells in your building again."
            call c3_papa_cells from _call_c3_papa_cells
            return

        "Never mind":
            jump c3_interrogate_contacts

    # General tips (Suzume)

    if npc == NPC_suzume:

        if nin.flags["hints"] >= 3:
            "<PLACEHOLDER> UNLOCKING [nin.name] EVENT CHAIN (Not implemented yet)"
            # call expression "c3_unlock_" + nin.name.lower()
            return

        suzume doubt "Well, I've told you everything I know, I think..."

        suzume normal "I don't have specific hints about individual Kunoichi, but I'm sure other people will."

        suzume "If you can collect {b}three hints{/b} about her, talk to me again. We should be able to devise a plan."

        "Talk to Suzume after you've gathered {b}three hints{/b} on a Kunoichi."

        jump c3_interrogate_contacts

    # Individual tips

    $ MC.interactions -= 1

    $ hint_list = {
                    NPC_narika : (NPC_jobgirl, NPC_bast, NPC_gurigura, NPC_gina, NPC_roz, NPC_renza, NPC_captain),
                    NPC_mizuki : (NPC_sill, NPC_satella, NPC_freak, NPC_gizel, NPC_stella),
                    NPC_haruka : (NPC_kenshin, NPC_carpenter, NPC_ramias, NPC_goldie, NPC_maya, NPC_lieutenant, NPC_sergeant)
                }

    if npc in hint_list[nin]:
        hide screen districts
        call c3_hint(npc, nin) from _call_c3_hint
        show screen districts

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

            you "Wait... Did you just give me a 90 per cent rebate right off the bat?"

            willow "Gee, you're impossible! Fine, Mister Negotiator, you can have it for 1,000 gold! But that's final!"

            you "You just went down from 100,000 gold to 1,000 gold in two sentences."

            willow "Yes, I'm great at bargaining, don't you think? Because {i}I{/i} think I rock!"

            you "Well, it's, err, important that you believe in yourself... If no one else will."

            you "So I can have it for 1,000 gold, uh?"

            willow "Yes, that's my final price. Because if you lower the price more than twice, it brings bad luck and your fluffy ears fall off. Everybody knows that."

            you "I don't think that {i}anybody{/i} actually knows that..."

            willow "Anyway, you want it, or what?"

        else:
            willow "Say, you wouldn't be interested in that wee fire rune, would you? 1,000 gold, as we said last time?"

        if MC.gold >= 1000:
            menu:
                "成交 (支付 1,000 金币)":
                    you "Sure okay, give it to me."

                    play sound s_gold
                    $ MC.gold -= 1000
                    $ story_flags["fire rune"] = True

                    call receive_item(fire_rune) from _call_receive_item_19

                "我才不买":
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

        you "So it's even worse, then! It's got cockroaches?!?" with vpunch

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

        you "Indeed... If I can get the kunoichi captured in the first place."

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

        if district.name == "The Docks":
            $ seafront.action = True
        elif district.name == "The Warehouse":
            $ gallows.action = True

    if MC.interactions:
        jump c3_interrogate_contacts
    else:
        return

label c3_hint(npc, ninja):

    scene black
    show expression npc.get_bg() at top
    show expression npc.char.image_tag
    with fade

    ## Narika tips

    if ninja == NPC_narika:
        if npc == NPC_jobgirl: # disguise, upper city
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True
            if event_dict["c2_narika_H1"].happened:
                jobgirl "A student in uniform, you say?"

                jobgirl "Well, none of the classes that I know of require uniforms. Must be something from the upper city."

                jobgirl "Must be a fancy school for sure... Reserved for blue bloods, no doubt."

            else:
                jobgirl "Wait a minute, this does ring a bell..."

                jobgirl "I've heard of an ambitious heist being planned from the lower city. Something about a locked-down place, with tight security and all... A bank maybe?"

                jobgirl "I'll tell you what, no one can take over such targets by storm, they're too well-defended... If it was me, I'd go with infiltration. Get them from within."

            suzume "That's a hint we could use... It narrows down our target, I guess."

            play sound s_spell

        elif npc == NPC_bast: # magical item
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True
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
                show gurigura at left with move
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

                katryn "Of course. There's one place where girls wear the exact kind of uniforms you described. The magic university."

                suzume "The Magic University! That's an important clue, [MC.name]!"

                play sound s_spell

            else:
                gurigura "You know the funny thing, I met a young girl like that the other day, same clothing and all."

                gurigura "She looked about my age, and she smelled funny, so I followed her around."

                gurigura "I figured we could be playmates, you know?"

                you "Uh... Do you always stalk random people like that?"

                gurigura "Of course not! Only when they smell funny."

                you "I... Don't even wanna know. Go on."

                gurigura "I followed her as she entered a big building through a back door."

                gurigura "I peeked through the keyhole, and she was in her undies!"

                you "Uh?"

                gurigura "She quickly stashed her warrior clothes behind a loose stone, and put on some kind of uniform."

                you "A uniform?!?"

                suzume "Whatever she is doing, she must be in a place where uniforms are worn. This is an important clue!"

                play sound s_spell

        elif npc == NPC_roz: # upper city, lined-up buyer / Good c1 ending
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True
            $ wrong_name = ''.join(random.sample(MC.name,len(MC.name))).capitalize()

            roz "Oy! [wrong_name], long time no see."

            you "Actually, it's [MC.name]."

            roz "Yes! [wrong_name], that's what I just said."

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
                    "给她10个{image=tb wood}" if MC.has_resource("wood", 10):
                        $ MC.spend_resource("wood", 10)

                    "给她10个{image=tb leather}" if MC.has_resource("leather", 10):
                        $ MC.spend_resource("leather", 10)

                    "给她10个{image=tb dye}" if MC.has_resource("dye", 10):
                        $ MC.spend_resource("dye", 10)

                    "暂时不给":
                        you "Sorry, maybe next time."
                        return

                renza "Thanks! That will do."

            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            renza "I've been approached by someone, maybe 3 or 4 months ago. They wanted help to steal a certain item."

            you "Nothing unusual in your line of work..."

            renza "Except I had to turn them down. This was out of reach, even for me."

            you "What do you mean?"

            renza "They wanted to lay their hands on a unique magic item. I'm not even sure where it was being held, but there were top-notch protection spells on it."

            you "You turned it down?"

            renza "There's one thing about me: I'd rather be alive and poor than rich but burnt to a crisp."

            renza "A Kunoichi, though... They just might pull it off. "

            you "And who was it that approached you?"

            renza "I have no idea. It was a female, for sure, but her disguise was nearly perfect. I understood she had high-level backers."

            renza "We chatted for a while about how to overcome some of the more mundane defenses. Her questions were quite good and to-the-point, I have to say. A true professional."

            you "What happened after that?"

            renza "Nothing. Once she figured I couldn't take the job, she thanked me and I never heard from her again."

            renza "But I'm willing to bet she's the one who's bankrolling your mysterious Kunoichi."

            you "Well, that's certainly something..."

            play sound s_spell

        elif npc == NPC_captain: # Upper city, uniforms / evil c1 ending
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True
            captain "A thief? In my city? Haha! Now that's a first..."

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

                gina "As you must know, science has shown that time is composed of smaller elemental particles, called timicrons. A moment, for instance, can hold as many as 1,532,875 timicrons. While an instant is more like 7,584 timicrons.  But feel free to check my maths."

                you "No thank you."

                gina "Now, timicrons can be charged positively, of course, so that they go faster, or negatively, so that they go slower."

                gina "It has been proven that some activities, such as having fun, charge timicrons positively, while other activities charge timicrons negatively. This is how science explains that an hour at the dentist always seems to drag on much longer than an hour at the brothel."

                gina "Now, look at this Cimerian runic stone: by infusing it with the Woven Threads of Fate, the Old Ones were able to charge it negatively and alter time in various ways."

                gina "This negative W.T.F. energy could then be harvested, to slow down all of the timicrons within a reasonably large area, such as a ballroom."

                you "Wait a minute, let's see if I can make sense of your mumbo-jumbo... Are you saying this stone can slow down time?"

                gina "Not at all, silly... It just slows down timicrons so that time {i}seems{/i} to flow slower in a given referential."

                you "What if I put a super fast ninja in this referential-thingy? Could this stone hold her in place?"

                gina "Well... Technically speaking... Yes? Maybe. I don't know. Maybe not."

                you "Thank you for giving me a useful and informed scientific opinion."

                you "Anyway, I may actually need something like this."

                gina "Really? I guess I could sell it to you. It's true that I'm always in need of additional funds for my research..."

                gina "I guess I could part with it for 1,000 denars."

                you "1,000 denars? That's a lot for a small rock..."

            else:
                gina "Want the time-warping runic stone? The price is still 1,000 gold."

            if MC.gold >= 1000:
                menu:
                    "成交(支付1,000 金币)":
                        you "Fine, I'll take it."

                        play sound s_gold
                        $ MC.gold -= 1000
                        $ story_flags["void rune"] = True

                        call receive_item(void_rune) from _call_receive_item_20

                    "也许下次":
                        you "1,000 gold for a piece of rubble? I'll pass."

                        gina "Suit yourself. Come back if you change your mind."

            else:
                you "I don't have the money."

                gina "How disapointing. Come back if you change your mind."

    elif ninja == NPC_mizuki:
        if npc == NPC_sill: # Various types of magic, ghost
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            sill sad "R-Really, Master? You want my opinion?"

            sill "(What should I do, what should I do... This never happens...)"

            you "Yes. If I remember right, you were trained in magic as a child before your family fell out of grace, correct?"

            sill happy "Well, it's true... My teachers said I had great potential."

            sill sad "And now, look at me, doing laundry... *sniff*"

            you "I know, right! What a waste of your natural talent for housekeeping it would have been."

            sill "Aw..."

            you "Anyway, is there anything you can tell me?"

            sill happy "Ahem, let's see. So you say this woman can appear and disappear at will?"

            you "Yes, and yet it doesn't seem to be regular magic... She just vanishes into thin air, like a ghost."

            sill "Hmm... Like a ghost, you said?"

            you "Yeah."

            sill "One thing I learnt is that there are two broad kinds of magic. The one we use is called academic magic, it is centered around formulas, scepters, runes or other conduits that we have to learn and master in order to cast spells."

            you "Okay..."

            sill "But there is another form of magic, called 'innate magic'. It's the kind used by dragons, the fairy people, demons..."

            you "Hmm... Even though she's a she-devil, I don't think she's a demon. Or a dragon, or an elf, for that matter."

            sill "... and the undead."

            you "What?"

            sill "Ghosts. The undead. They can use innate magic. Even without any external conduits. Their immortal soul is the conduit."

            you "Wait a minute. You're not seriously suggesting she's a ghost?"

            if NPC_mizuki.flags["onsen"]:
                you "I've seen her from up close and... She is very much alive! *blush*"

            sill "Well, maybe she found a way to harvest the afterlife's energy, then."

            you "As far-fetched as this sounds... This could be a lead. Let's see where it takes us."

            play sound s_spell

        elif npc == NPC_satella: # Various types of magic, link to Shalia
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            play music m_satella fadein 3.0

            satella happy "Teehee, look what the raccoon dragged in! So you didn't come here to play a game?"

            you "N-No, not this time..."

            satella angry "Well, you're damn right you didn't, because I didn't send you an invitation, did I!" with vpunch

            you "N-No! I'm sorry to disturb you.... Maybe this wasn't a good idea-"

            satella happy "I mean, it's perfectly fine for you to drop by and ask idle questions."

            you "Phew..."

            satella angry "BUT GAMES, THOUGH? GAMES ARE INVITE-ONLY! I MIGHT TURN YOU INTO A MAGGOT PILE IF YOU DARED!!!" with vpunch

            you "*gulp*"

            you "I'm definitely not here for a game... Just random idle questions about ninjas, I swear."

            satella happy "Fine. I'm glad to see you value my time."

            satella "My {i}game{/i} time." with vpunch

            you "So... Know anything about this person? Or her magic?"

            satella "Let me tell you something about wizards, sorcerers, mages, witches and all that ilk..."

            you "What?"

            satella "They're a bunch of hopeless losers."

            if MC.playerclass == "法师":
                you "Ouch, thanks."
            else:
                you "That's what I think, too."

            satella "And you know why?"

            you "I'm going to go with... No?"

            satella "Because they're nerds, that's why!" with vpunch

            you "Uh?"

            satella "All those years they spend studying, poring over dusty old books, creeping into other dimensions and begging for scraps of knowledge from bored demons..."

            play sound s_evil_laugh

            satella "Looooooo-sers!!!" with vpunch

            you "..."

            satella "You see, {i}I{/i} wave far better magic than any of these sorry dorks, and did I have to work hard to learn it?"

            satella "Not a single day in my life! You better believe it!"

            you "I believe it."

            satella "It's because I have good genes! It all comes naturally to me!"

            you "Well... Okay."

            satella "So here are my two denars: Your mysterious black magic woman may be a natural, like me. If so, then she doesn't need mana to cast spells, or scrolls, or materia, or whatever it is kids use these days."

            you "Really? Any spell?"

            satella "Well, spells within her area of affinity, anyway... I won't lie, invisibility, disappearing at will... Sounds right up Shalia's alley."

            you "So she could be a natural magic user, and a Shalia follower... Hmm."

            play sound s_spell

        elif npc == NPC_freak: # Westmarch story, ghost
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            play music m_freak fadein 3.0

            papa "Hey, yo, [MC.name]! Waddup, my [MC.playerclass]?"

            you "Uh? What are you doing?"

            papa "I, err, I'm sorry, son... I was trying to sound 'cool', in the parlance of young people of our era..."

            papa "But I'm old... Hopelessly old..."

            you "Yeah, well, that's kind of the reason I'm asking you this. This lady is supposed to be really old... Like you."

            you "(Although I must say she's in much better shape...)"

            papa "We'll see how you are when you et to 323! I'm sure your mighty dick may not be so hardy by then, uh!"

            you "Focus, Papa. Let's not discuss my dick."

            papa "So... This lady wears a lavish blue kimono, and she is of great beauty, would you say?"

            you "I would say..."

            papa "And does she have big puppies?"

            you "Puppies? I don't follow..."

            papa "I mean jugs? Mellons? Honkers, ta-tas, knockers, gitchi gitchi yaya dada?"

            you "I think you're laboriously trying to say... 'boobies'."

            papa "Ah, yes, 'boobies'! That's what I'm talking about, dog!"

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

            papa "Listen to me! She took her own life."

            you "She... What?"

            papa "That blue kimono lady. She was a highborn princess, from one of the most powerful families in Westmarch."

            papa "Everyone at the time knew her. Lovely young woman. She got married, but soon after she took her own life."

            papa "It was a shock to everyone in the Four Westmarch Kingdoms, as they were known at the time."

            papa "In fact, this sorry event started the great struggle for power that lasted 50 years and ended up with the Four Kingdoms disbanded into a hundred small Principalities."

            papa "So you see, young man, there's no chance that your woman and this princess could be the same. Sorry I misled you."

            you "But still... This seems like too much of a coincidence..."

            play sound s_spell

        elif npc == NPC_gizel: # Westmarch story, link to Shalia
            if not npc.flags["seen ninja hint"]:
                $ ninja.flags["hints"] += 1
                $ npc.flags["seen ninja hint"] = True

            gizel normal "A mysterious lady who disappears into thin air? Hmm. Interesting."

            you "I thought you know, maybe you know something, as you're immortal and stuff..."

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

            gizel "Unimaginative as they were, can you guess what nickname they gave when they met an all-powerful magic user in Westmarch?"

            you "The... The 'Blue Witch of the West'?"

            gizel "Precisely. The big, ignorant oafs."

            gizel "Turns out about 200-years ago, there was a huge war in Westmarch. Started with two Kingdoms, ended with 100 Principalities. You could say it never really ended."

            gizel "During that time, as I was monitoring various rumors as I usually do to see if some dumb knights are on my track, I started hearing rumors about a local witch."

            gizel "A she-devil Shalia assassin that could use magic and appear and disappear at will, and killed her marks in often spectacular ways."

            gizel "She was the bane of one of the factions in that war, although I can't remember which one."

            gizel "Her description was always the same: A stunning, pale middle-age woman with raven hair, and an elaborate blue silk kimono."

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

                stella "Used in the right way, it can alter or neutralize water magic, whatever its origin. Invaluable for ship defense."

                you "Water magic? Like the one Mizuki seems to be using?"

                stella "I paid precious little attention to your tedious story, but yes, if that woman is using water magic, such a rune could significantly weaken her."

                you "That seems great..."

                stella "So, 1,000 gold. No haggling."

                you "That's a bit steep."

                stella "Fine, I'll find another buyer."

                you "Wait..."

            else:
                stella "Came back for the Water stone, haven't you? I knew you would."

            if MC.gold >= 1000:
                menu:
                    "成交(支付1,000 金币)":
                        you "Okay, I'll take it."

                        play sound s_gold
                        $ MC.gold -= 1000
                        $ story_flags["water rune"] = True

                        call receive_item(water_rune) from _call_receive_item_21

                    "也许下次":
                        you "1,000 gold is more than I can afford. Maybe next time."

                        stella "Out of my way, then. I've got actual paying customers to tend to."

            else:
                you "I don't have the money yet, but..."

                stella "Oh, come on."

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

            carpenter "But I remember there are hiden pathways, to the Sewers especially..."

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

            lieutenant "Let's cut to the chase. You mentioned a certain wounded Kunoichi, and how she was sent to Xotar Prison. I might know a bit about that."

            you "Really?"

            lieutenant "Yeah. You see, our old Captain used to take some hefty bribes to organize prisoner convoys of a certain kind, all with the utmost discretion."

            you "What kind of prisoner convoys?"

            lieutenant "Lone prisoners, secret identity. They'd come in from the road at night, load the prisoner in a metal box that was almost like a casket, and send them to the Prison with an escort of guards and knights hidden in civilian clothes."

            lieutenant "Sergeant Kashiv always carried Farah's dirtiest deeds, so she was usually in charge of the guards' escort."

            lieutenant "They go down into the Sewers, where I hear there are secret passages into the old part of the Prison. You'd never hear from the poor sods again."

            lieutenant "I did some spying on account of Renza on such convoys. One night, I caught a glimpse of the prisoner as they were locking her in the metal box."

            lieutenant "Even though the light was low, one thing stood out... The lady only had one arm."

            you "I see... So they took her into the Sewers?"

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

                    "白嫖这块石头":
                        you "(This offer is too good to pass.)"

                        you "Thank you Goldie, I'll have the stone, then."

                        "She gives a last look at the stone, and you can see some anguish in her eyes. But she steels her resolve, and gives it to you."

                        $ MC.good -= 1

                    "花500金币买下":
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

                    "花1000金币买下":
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

                    "下次再说":
                        you "Thank you for your offer, but I can't accept just yet. I will be back."
                        return

                $ story_flags["earth rune"] = True

                call receive_item(earth_rune) from _call_receive_item_22

                goldie "May it protect you from harm, dear [MC.name]."

                you "Thank you sweetie."

    return


## Papa Freak events ##

label c3_papa_cells():

    if not NPC_freak.flags["requirements"]:
        if not NPC_freak.flags["cells built"]:
            papa "So, for starters... I'm looking for a great cocksucker"

            papa_apprentice "Papa likes it wet and nice, uh..."

            you "I don't need details. Please."

            papa "Bring us a whore that offers great service, is beautiful and perverted, and we'll build you a cell."

            "Bring a whore to Papa with at least {b}75 in Service, Beauty and Libido{/b}."

            $ game.set_task("给怪老爹送去一个至少{b}75侍奉,外貌和性欲{/b}的妓女。", "special")
            $ NPC_freak.flags["requirements"] = [("service", 75), ("beauty", 75), ("libido", 75)]

        elif NPC_freak.flags["cells built"] == 1:

            papa "Now Papa wants to reward his apprentice. He's been working hard, lately."

            papa_apprentice "Oooh, thank you, Papa!"

            papa "But we'll take turns, of course. Can't let you have all the fun."

            papa_apprentice "Ew, I knew there was a trick."

            papa "What kind of girl would you like, my boy?"

            papa_apprentice "Well, good at sex, of course... With a good personality, and a sensitive body... Hmmm. *drool*"

            "Bring a whore to Papa with at least {b}75 in Sex, Charisma and Sensitivity{/b}."

            $ game.set_task("给怪老爹送去一个至少{b}75性交,魅力和敏感{/b}的妓女。", "special")
            $ NPC_freak.flags["requirements"] = [("sex", 75), ("charm", 75), ("sensitivity", 75)]

        elif NPC_freak.flags["cells built"] == 2:

            papa "Did you like that last one, my boy?"

            papa_apprentice "I did... I had such a great time."

            papa "But you wanted more, didn't you? Can't hide it from Papa..."

            papa_apprentice "Well... It's true. I wish I could have fucked her ass."

            papa "Anal? You kinky little rascal."

            papa "All right, our next order is: an anal whore! She must have a good body, of course, and be obedient."

            "Bring a whore to Papa with at least {b}75 in Anal, Body and Obedience{/b}."

            $ game.set_task("给怪老爹送去一个至少{b}75肛交,身材和服从{/b}的妓女。", "special")
            $ NPC_freak.flags["requirements"] = [("anal", 75), ("body", 75), ("obedience", 75)]

        elif NPC_freak.flags["cells built"] == 3:

            papa "This one must be special. I have this list of fantasies I have yet to achieve..."

            papa_apprentice "Papa wants to get frea-kyyyy~..."

            you "Please. Don't do that. "

            extend "Ever. "

            extend "Again."

            papa "Bring me a whore with kinky tastes, who is both refined and physically resilient. This is our last order! Let's make her count!"

            "Bring a whore to Papa with at least {b}75 in Fetish, Refinement and Constitution{/b}."

            $ game.set_task("给怪老爹送去一个至少{b}75调教,优雅和体质{/b}的妓女。", "special")
            $ NPC_freak.flags["requirements"] = [("fetish", 75), ("refinement", 75), ("constitution", 75)]

        return


    else:

        if MC.girls:
            "Choose a girl from your brothel to bring with you (reminder: she must have at least 75 in Service, Beauty and Libido, and be open to whoring)"
            $ girl = long_menu("Choose a girl", [(g.name, g) for g in MC.girls])
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
            else:
                failed_stat = None

        if failed_stat:
            papa "No, that won't do, that won't do at all... I'm sorry, young lady. Come back when you've had more training."

            "You need a girl with higher {b}[failed_stat]{/b} to satisfy Papa Freak's request."

            return

        papa "She looks perfect... Come now, my pretty, Papa and his young apprentice have been waiting for you..."

        girl.char "What is it about, Master?"

        "You explain what she needs to do."

        $ sex_act = NPC_freak.flags["requirements"][0][0]

        if not girl.will_do_sex_act(sex_act):
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

            show screen show_event(girl.get_pic(sex_act, "naked"), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with dissolve

            girl.char "Oh, aaah, oooh!!!"

            papa "Yes! Yes! Just like this!!!"

            show screen show_event(girl.get_pic(act, "service", "naked", and_tags="cumshot"), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with flash

            play sound s_orgasm_fast

            girl.char "Aaaah!!!"

            with doubleflash

            hide screen show_event
            scene black
            with fade

            show bg papa_freak at top with dissolve

            papa "Oh boy... She's really something. Can I get another go?"

            you "Yes. But you must build me a cell, first."

            papa "You got it. What will it be?"

            menu:
                extend ""

                "帮我建造一间能屏蔽虚空元素的密室" if not story_flags["void ward"]:
                    $ target = "void"

                    papa "This is a complex element, if it is an element at all... Fortunately, the old Cimerians knew a thing or two about manipulating time and space."

                "帮我建造一间能屏蔽水之元素的密室" if not story_flags["water ward"]:
                    $ target = "water"

                    papa "Ah, water... I've this special desiccant technology I've been experimenting with. I thought it was only good for preserving cookies, but I might find a use for it after all"

                "帮我建造一间能屏蔽土之元素的密室" if not story_flags["earth ward"]:
                    $ target = "earth"

                    papa "This is straightforward enough. Metal blocks most Earth magic. A cell made entirely of steel would do the trick."

                "帮我建造一间能屏蔽风和火之元素的密室" if NPC_freak.flags["cells built"] >= 3:
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

            papa "Perfect! Here you go, young man, just as we agreed. You now have a nice holding cell that will ward against [target] magic."

            $ NPC_freak.flags["cells built"] += 1
            $ NPC_freak.flags["requirements"] = None

            if NPC_freak.flags["cells built"] >= 4:
                papa "This was the last one. Your basement is now fit to capture a small army of elemental ninjas."

                you "I was going to install a game room, but that works too."

                papa "See you around soon, my boy!"

                $ seafront.action = False
                $ gallows.action = False

                you "Sure."

            elif NPC_freak.flags["cells built"] < 4:
                you "So this is it, then?"

                papa "Well... There is one more elemental cell I could restore, but you didn't ask me about it..."

                you "Which one?"

                papa "The Air and Fire ward room. It blocks not one but two elements. Nice, isn't it?"

                you "Yeah... But I have no need to imprison someone with one of those elements."

                papa "Not now you don't, but if the eventuality presented itself, wouldn't it be nice to have a cell ready?"

                you "*sigh* What do you want for it?"

            elif NPC_freak.flags["cells built"] < 3:
                you "Can you build me any more holding cells?"

                papa "Can I? Sure. But will I? There needs to be something in it for me..."

                you "All right. Name your poison."

            jump c3_papa_cells


## Homura city events ##

label c3_contact_homura():

    "You remember what Homura told you about tying her ribbon to a pole at the Plaza to summon her."

    if brothel.has_room("okiya"):
        you "Here, let's see if that does the trick."

        if blue_ribbon in MC.items:
            $ MC.items.remove(blue_ribbon)
            $ plaza.action = False

        $ calendar.set_alarm(calendar.time, StoryEvent(label = "c3_homura_visit", type = "night"))

    else:
        you "She did mention I needed to build an okiya first... No point in summoning her now."

        "You must buy the {b}Okiya{/b} before you can contact Homura again."

    return

label c3_homura_visit(): # Happens after tying the ribbon in the plaza

    scene black with fade
    show bg okiya at top with dissolve

    play music m_palace fadein 3.0

    "That night, you keep an eye out for Lady Homura. Sure enough, it isn't long before you spot her entering the Okiya, bowing politely to your staff."

    show bg homura_okiya happy at top with dissolve

    if not story_flags["homura summoned"]: # first visit
        $ story_flags["homura summoned"] = True
        if not story_flags["suzume hint seen"]:
            $ story_add_event("c3_suzume_hint")

        homura normal "[MC.name]! I thought you'd never contact me again."

        homura blush "I was a bit scared, to be honest. *frown*"

        you "Why would I let you down?"

        homura "Well, I thought, because we had, hem... You know..."

        homura "I thought maybe a man in your occupation might just care about... *blush*"

        menu:
            "告诉她你不是这样的人": # For good characters
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

            "告诉她她是独一无二的": # For neutral characters
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

            "告诉她你仍然需要她": # For evil characters
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

        if MC.playerclass == "法师":
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

            "他简直大错特错":
                $ MC.good += 1

                you "That's just wrong. Women are just as capable as men... They can do great things..."

                homura "Oh, really? Look at you, making money from whoring girl slaves out... Quite the feminist."

                you "Ouch..."

                if NPC_homura.love >= 5:
                    homura sad "Sorry, that was uncalled for."

                    you "It's all right..."

                    $ NPC_homura.love += 1

            "他说的也有道理":
                $ MC.evil += 1

                you "Look, he's not wrong. Women are less capable than men, it's obvious."

                you "It's only right that you should serve us..."

                play sound s_surprise
                homura surprise "What? Are you out of your mind?"

                homura "That's a new low, even for you!"

                you "Hehe, you're cute when you're angry..."

                homura "Shut up! And remove your hand!"

                $ NPC_homura -= 3

            "女人还能做些其他有趣的事":
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

        "紧急任务":
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

                    "好吧":
                        $ NPC_homura.flags["divulged assignment"] = True

                        you "Yes. I need help, and I don't think I can manage this alone."

                        homura "Awesome! Now tell me! I'm so curious..."

                        with fade

                        "You spend a long time telling her about your assignment and the Kunoichi."

                        with fade

                        homura "Secret female ninjas terrorizing the city... This is even better than the illegal picture books I buy at the Spice Market!"

                        homura "So, what can I help you with?"

                        call c3_homura_menu_business() from _call_c3_homura_menu_business_1

                    "不行":
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
                    "让我们到卧室里加深一下交流":
                        $ NPC_homura.love += 0.5

                        you "Of course, Lady Henso... Follow... Hey!"

                        "She's already grabbing your hand, pulling you towards the stairs."

                        call c3_homura_menu_pleasure() from _call_c3_homura_menu_pleasure

                    "也许下次":
                        $ NPC_homura.love -= 0.5

                        you "I would love to, Homura, but I'm really busy right now..."

                        homura sad "Oh, I see."

        "乐意之至":
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
        "告诉她关于Narika, 虚空忍者的事" if NPC_narika.flags["locked"]:
            with fade
            "You spend a long time explaining about the Void Kunoichi and the details of your encounter."

            homura normal "I see... So she's preparing a heist, you think?"

            you "Yes. It would be good if I could figure out her target."

            homura "You need to talk to someone from the criminal world, then... Or perhaps to someone from the law, but with underground connections?"

            homura "Perhaps you can also figure out where she plans to sell her loot?"

            you "Those are all good ideas."

            homura "Anything else you can tell me about her?"

            if event_dict["c2_narika_H1"].happened:
                you "Well... We could get a glimpse of her using a magic crystal..."

                you "She was wearing a school uniform."

                homura "Really? She's a student? That doesn't make sense!"

                homura "It must be a cover for her hit job, whatever it is..."

                homura "Perhaps ask someone who might know the city's schools?"

                you "Err, do I know anyone like that?"

        "告诉她关于Mizuki, 水之忍者的事" if NPC_mizuki.flags["locked"]:
            with fade

            "You spend a long time explaining about the Water Kunoichi and the details of your encounter."

            homura normal "A lady who doesn't age, and disappears at will... This stinks to high heaven of powerful magic."

            you "Indeed. But it's beyond the abilities of most mages I've ever seen, and yet she doesn't seem like a fully trained sorceress."

            homura "I would start with interrogating magic-users, preferably unconventional ones."

            homura "And if she's really lived for as long as she claims, perhaps ask some old-timers about her? They might know some stories."

            you "You're right."

        "告诉她关于 Haruka, 土之忍者的事" if NPC_haruka.flags["locked"]:
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

    if ninja_lock_count >= 3 and NPC_homura.flags["H level"] == 3:
        homura normal "Pleasure! Yay!"

        homura "You know what, we still have a couple of hours of daylight. Why don't we go outside for a stroll?"

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

    # Unlocks new sex acts as the story progresses (except anal - unlocked through story)

    $ ninja_lock_count = sum(1 for x in [NPC_narika, NPC_mizuki, NPC_haruka] if x.flags["locked"])

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

            "我想看你自慰":
                call homura_mast(False) from _call_homura_mast_1

                scene black with fade
                show expression brothel.master_bedroom.get_pic() at top
                with dissolve

                show homura naked with dissolve

                homura "Did I give you a good show? But... It felt lonely..."

                $ NPC_homura.love += 0.25

            "我想让你为我口交":
                call homura_bj(False) from _call_homura_bj_1

                scene black with fade
                show expression brothel.master_bedroom.get_pic() at top
                with dissolve

                show homura naked with dissolve

                homura "Well, someone looks like he enjoyed himself... But what about me?"

                $ NPC_homura.love += 0.25

            "试试69式" if NPC_homura.flags["H level"] == 2:
                call homura_69(False) from _call_homura_69_1

                scene black with fade
                show bg homura_rest1 at top with dissolve

                homura "Wow... Was it as good for you as it was for me?"

                $ NPC_homura.love += 0.5

            "来做爱吧(后入式)":
                call homura_sex(False) from _call_homura_sex

                scene black with fade
                show bg homura_rest1 at top with dissolve

                homura "It's always good when you're inside me..."

                $ NPC_homura.love += 0.5

            "来做爱吧(骑乘式)" if NPC_homura.flags["H level"] == 3:
                call homura_cowgirl(False) from _call_homura_cowgirl_1

                scene black with fade
                show bg homura_rest1 at top with dissolve

                homura "I like being on top, it's an intoxicating feeling..."

                $ NPC_homura.love += 0.5

            "我想试试野战" if NPC_homura.flags["H level"] == 4:
                call homura_river(False) from _call_homura_river_1

                show bg forest at top with fade
                show homura naked with dissolve

                homura naked "Wow, having sex outside is so much fun... It always feels as if someone could catch us at any moment. [emo_heart]"

                $ NPC_homura.love += 0.5

            "我想试试肛交" if NPC_homura.flags["H level"] == 5:
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

            "算了吧":
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

        "内射":
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

        "外射":
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

            "天呐！":
                you "Wonderful! This place feels out of time..."

                homura "Right? I come here every chance I get."

                homura "I'm happy I get to share it with someone, for once..."

                $ NPC_homura.love += 1

            "不错":
                you "Yeah, it's fine, I guess."

                homura surprise "You guess? Come on! It's great, admit it!"

            "就这？":
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


#### END OF CHAPTER 3 EVENTS ####
