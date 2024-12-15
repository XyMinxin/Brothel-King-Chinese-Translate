##### EVENTS FOR TRAIT KING #####

label traitking_holidays: # runs yearly, schedules holidays for the year
    $ calendar.set_alarm(calendar.time + (12*28 + 1) -1, StoryEvent(label="ext_holiday_newyear", type="day"))
    $ calendar.set_alarm(calendar.time + (2*28 + 14) -29, StoryEvent(label="ext_holiday_valentines", type="day"))
    $ calendar.set_alarm(calendar.time + (4*28 + 7) -29, StoryEvent(label="ext_holiday_salvation", type="day"))
    $ calendar.set_alarm(calendar.time + (5*28 + 19) -29, StoryEvent(label="ext_holiday_ascension", type="day"))
    # $ calendar.set_alarm(calendar.time + (6*28 + 21) -29, StoryEvent(label="ext_holiday_summer", type="day"))
    # $ calendar.set_alarm(calendar.time + (9*28 + 11) -29, StoryEvent(label="ext_holiday_sin", type="day"))
    $ calendar.set_alarm(calendar.time + (10*28 + 28) -29, StoryEvent(label="ext_holiday_night", type="day"))
    # $ calendar.set_alarm(calendar.time + (11*28 + 25) -29, StoryEvent(label="ext_holiday_fertility", type="day"))
    $ calendar.set_alarm(calendar.time + (12*28 + 24) -29, StoryEvent(label="ext_holiday_hmas", type="day")) 

    # schedule again next year
    $ calendar.set_alarm(calendar.time + (12*28 + 1) -1, StoryEvent(label="traitking_holidays", order = 0, type="morning"))
    
    return

label traitking_morning: # morning: triggers as first thing in the day
# Triggers monthly

    python:
    
        for girl in MC.girls:
        
            if not hasattr(girl, 'birthday'):
                girl.birthday = dice(336)
                girl.birthday_celebrated = False
                
            if not girl.birthday_celebrated:
                if calendar.time <= ((calendar.year-1) * 336 + girl.birthday):
                    calendar.set_alarm((calendar.year-1) * 336 + girl.birthday, StoryEvent(label="ext_birthday", type="morning", call_args=[girl]))
                else:
                    calendar.set_alarm((calendar.year) * 336 + girl.birthday, StoryEvent(label="ext_birthday", type="morning", call_args=[girl]))
                girl.birthday_celebrated = True

            
        if len(MC.girls) >= 3: # Performance review

            net_list = []
            best_net = -1
            best_girl = None
        
            for girl in MC.girls:
                
                j_gold = girl.get_log("total_gold", 28)
                q_gold = girl.get_log("quest_gold", 28)
                upk = girl.get_log("upkeep", 28)
                net = int(j_gold + q_gold - upk)

                net_list.append([girl.fullname, net])
                
                if net > best_net:
                    best_net = net
                    best_girl = girl
                
            net_list.sort(reverse=True, key=lambda y: y[1])
            
            profitable_desc = rand_choice([__("proven to be your most lucrative asset"), __("brought in the most coin"), __("brought in the most profit"), __("been a smash hit"), __("proven to be your most popular girl"), __("been a favorite among your customers"), __("led your stable"), __("earned her keep like no other"), __("taken the crown")])
            
            renpy.say("",__("Over the past month, {b}{color=[c_orange]}") + net_list[0][0] + __("{/color}{/b} has ") + profitable_desc +  __(" (bringing in ") + str(net_list[0][1]) + __(" gold), followed by {b}") + net_list[1][0] + __("{/b} and {b}") + net_list[2][0] + "{/b}.")
            
            # friendship/rivalry: other girls become jealous or start admiring the top earner
            if best_net > 2000:
                for girl in MC.girls:
                    if not best_girl and dice(6) == 1:
                        girl.change_relationship(best_girl, -1 + int(best_girl.get_stat("charm")/25) - int(girl.get_stat("charm")/25))
                        
            renpy.call("performance_reward", best_girl)

    $ calendar.set_alarm(calendar.time + 28, StoryEvent(label="traitking_morning", order = 1, type="morning"))
    
    return
    
label traitking_day: # day: triggers after morning, but still before player can act
# Triggers weekly on average, semi-randomly (repeats within 3-11 days)

    python:

        virgin_traits = [housebroken_trait] + [t_pet_trait] + [farmgirl_trait] + [trauma_trait]

        for girl in MC.girls:
        
            if girl.free:
                # Brothel-residing free girl events
                work_experience = sum([t for o, t in girl.jp.items()])
            
                if renpy.random.random() <= 0.12 and girl.mood >=50 and girl.fear <= -30 and work_experience >= 100 and not girl.is_("very dom"): # Enslaving a free girl
                    renpy.call("freedom_interact", girl)
                    
            elif not girl.has_trait("Unknown"):
                # Trait King: Discovering unknown trait

                if not hasattr(girl, 'nickname'):
                    girl.nickname = {"adjective" : None, "trait" : None, "noun" : None, "story" : None, "reason1" : None, "reason2" : None, "flag1" : False, "flag2" : False}
                    girl.fullnickname = None
            
                if girl.nickname["flag2"] == False and not len(girl.traits) > 5:
                    if renpy.random.random() <= 0.02: # 2% chance of discovering the unknown trait per workday
                        add_trait_perkless(girl, Trait("Unknown", verb = "have an", eff1 = Effect("boost", "prestige", -0.25), base_description = _("This girl is hiding something from you.")))

                        renpy.say("",__("You suspect that ") + girl.name + __(" is trying to hide something from you."))
        
            if girl.has_trait("Karkyrian hymen"): # Karkyrian Hymen trait
            
                if not girl.has_trait("Virgin"):
                
                    add_trait_perkless(girl, trait_dict["Virgin"])
                    
                    renpy.say("",__("Thanks to her Karkyrian Hymen, ") + girl.name + __("'s virginity has been restored."))

                    for trait in girl.traits:
                    
                        if trait in virgin_traits:
                
                            girl.remove_trait(trait)
                            
            if girl.has_trait("Genius") or girl.has_trait("Fast learner"): # Genius/Fast Learner trait
            
                if renpy.random.random() <= 0.12:
                
                    girl_pic = girl.get_pic("study", not_tags=["public", "beach", "nature", "town"], naked_filter=True, soft=True)
                    if not girl_pic:
                        girl_pic = girl.get_pic("profile", not_tags=["public", "beach", "nature", "town"], naked_filter=True, soft=True)
                    
                    # renpy.show(brothel.bedroom_type.get_bg(), at_list = [top])
                    bedroom_pic = brothel.bedroom_type.get_bg()
                    
                    if girl.has_trait("Genius") and (girl.perk_points + len(girl.perks)) <= 4 + (girl.level // 2):
                        result_comment = __("an extra perk point.")
                        girl.perk_points += 1
                   
                    elif sum([t for o, t in girl.jp.items()]) <= 1000:
                        result_target = rand_choice(girl.jp.items())
                        result_comment = __("increased familiarity with ") + result_target[0] + __(" tasks.")
                        girl.jp[result_target[0]] += 25
                        
                    else:
                        result_target = rand_choice(girl.jp.items())
                        result_comment = __("increased familiarity with ") + result_target[0] + __(" tasks.")
                        girl.jp[result_target[0]] += 10
                        
                    renpy.show_screen("show_event", girl_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=bedroom_pic)
                    renpy.say("",girl.name + __(" has been studying vigorously in her leisure time, resulting in ") + result_comment)
                    renpy.hide_screen("show_event")
                    
            if girl.has_trait("Prodigy"): # Prodigy trait
            
                i = 0
            
                for archetype in archetype_list:
                
                    if not girl.archetypes[archetype].unlocked: 
            
                        if i == 0:
                        
                            renpy.say("",girl.name + __(" is a true prodigy. It's as if the tricks of the trade come naturally to her."))
                            renpy.say("",_("She has intuitively unlocked the perk tree for ") + archetype + _("."))

                        i += 1                     
                        girl.unlock_archetype(archetype)
                                                    

            if girl.has_trait("In demand"): # In demand trait (remove)

                girl.remove_trait(trait_dict["In demand"])
                
                renpy.say("",__("Slavers are no longer willing to pay a premium for ") + girl.name + _("."))

            if renpy.random.random() <= 0.06 and not girl.free: # In demand trait (add) # todo: implement "Fan favorite"
            
                add_trait_perkless(girl, trait_dict["In demand"])
                
                renpy.say("",__("Recently a lot of slavers have been inquiring about ") + girl.name + __(". It would seem that she is {b}{color=[c_orange]}in high demand{/color}{/b}. If you were willing to part with her, it could prove to be very lucrative."))
                
            if renpy.random.random() <= 0.06:
            
                renpy.call("ext_party", girl) 
                
            # Trait King evolving negative traits
            if renpy.random.random() <= 0.25:
                if not girl.neg_fixations:
                    if not hasattr(girl, 'neg_fix_counter'):
                        girl.neg_fix_counter = 0
                    for trait in girl.traits:
                        if trait in neg_traits_fixable:
                            # schedule evolution training
                            calendar.set_alarm(calendar.time + dice(4), StoryEvent(label="fix_neg_interact", call_args=[girl, trait], order = 0, type="morning"))
                            break

                            
    $ calendar.set_alarm(calendar.time + 2+dice(9), StoryEvent(label="traitking_day", type="day"))
    
    return

label traitking_night: # night: first thing that happens as you press 'end day'
# Triggers daily

    python:
        
        for girl in MC.girls:

            if not girl.free:
            
                # Trait King: Developing unknown trait
                if girl.has_trait("Unknown"):
                    if not hasattr(girl, 'unknown_trait_counter'):
                        girl.unknown_trait_counter = 1 # Trait King: Counters
                    if renpy.random.random() <= 0.015 * girl.unknown_trait_counter: # escalating chance of triggering undervalued/unknown trait event
                        girl.unknown_trait_counter = 1
                        renpy.call("undervalued_interact", girl)
                    else:
                         girl.unknown_trait_counter += 1

    $ calendar.set_alarm(calendar.time + 1, StoryEvent(label="traitking_night", type="night"))
    
    return
    
label performance_reward(girl):

    $ renpy.block_rollback()
    
    # For rank up evaluation event
    python:
        # book_title = ["The History of " + girl.origin,"Famous " + girl.story_profession + "s from " + girl.origin,"The " + girl.story_profession + " that saved the Universe","The " + girl.story_home + " Chronicles", girl.personality.name + " Stories", girl.likes["color"] + " " + girl.hobbies[0], girl.hobbies[0] + " with " + girl.story_guardian]

        # materialist_note = ["Get laid & paid!","Do it for fashion!","I want to be the very best!","Money can buy happiness!","Cunt for sale!","Sell your body!","Be #1 Whore","Make them worship me!","No one is better!","Best cunt in the kingdom!",MC.name + " and me, running an empire!","Dream big!"]
        
        # masochist_note = ["YOU DESERVE THIS","LOSER","NEVER KNOWS BEST","PAIN SETS YOU FREE","TO DUST YOU SHALL RETURN","YOU ARE FILTH","LOVE HATE LOVE HATE LOVE HATE","SLAVE TO MY DESIRES","GET FUCKED, SCUM"]

        # sweet_note = ["Our home is full of happiness!","Do small things with great love!","Love conquers all things!","Home sweet home!","Smile! You are beautiful!","I love you!","Welcome home!","Faith, hope and love!","Always kiss me goodnight!","Love lives here!","Share my bed and keep me warm!","What I love most about my home is who I share it with!"]

        # pervert_topic = ["spanking children","fisting dogs","strangling slaves","neverending sex marathons","drowning in cum","sex machines","anal fisting","deepthroating horsecock","many-cunted aliens","methods of sexual torture"]
        
        # room_personality_list = {
                                # "meek" : [
                                    # "A lot of thought and effort has been put into decorating this room. It perfectly fits " + girl.name + "'s personality. Great attention has been given to the finest details.", 
                                    # "The carefully decorated room truly reflects " + girl.name + " as an individual. Even though she is not here, her atmosphere still lingers.",
                                    # "Vivid colors give this bedroom a childish, carefree atmosphere. The bed is especially inviting. Dozens of comfortable looking pillows are strewn across the floor.",
                                    # "Extra effort has been put in to make this room a more private area for " + girl.name + ". For example, the white curtains surrounding her canopy bed. are usually closed.",
                                    # "The room seems designed to serve as a retreat, ideal for shutting yourself off from the world after a particularly grueling day.",
                                    # ],
                                # "nerd" : [
                                    # "Everything is very neatly organised. You can tell that the specific layout of this room has been fully thought through.", 
                                    # "While it's not entirely practical, the decisions made in assembling this decor seem very deliberate.",
                                    # "There are several bookcases lining the walls, all stocked to the brim with books. You're shocked that " + girl.name + " has managed to accumulate all these possessions.",
                                    # ],
                                # "pervert" : [
                                    # "This bedroom contains an abnormally large bed, custom made to provide ample space for three or more occupants. As a result, most other elements of the room have become an afterthought.",
                                    # "The bed in this room is enormous. It could easily accomodate three or four people. The bed is unmade and does not look very comfortable.",
                                    # "This bedroom has seen more action than you can imagine. Dried cum stains are visible on the floor and on the walls. Even the ceiling hasn't been spared!",
                                    # ],
                                # "rebel" : [
                                    # "The carefully decorated room truly reflects " + girl.name + " as an individual. Even though she is not here, her atmosphere still lingers.",
                                    # "The room seems designed to serve as a retreat, ideal for shutting yourself off from the world after a particularly grueling day.",
                                    # "This bedroom seems to defy conventional wisdom when it comes to home decorating. Traditional and modern elements have been mixed freely and impulsively.",
                                    # "Somehow " + girl.name + " has managed to get a cocktail bar installed next to her bed. The faint smell of alcohol lingers in the air.",
                                    # ],
                                # "superficial" : [
                                    # "You get the feeling that this bedroom is not so much designed to appeal to " + girl.name + ", but primarily to appeal to you and any other visitors that may enter.",
                                    # "[girl.name] treats this bedroom as a temporary stop gap on her way to bigger and better things. As such, not much energy has gone into decorating it.",
                                    # "The room itself is relatively plain and yet certain possessions stored within are very extravagant.",
                                    # ],
                                # "cold" : [
                                    # "The room is purely designed for efficiency. Very little effort has been put into decorating it.",
                                    # "The room is very spartan. It seems like " + girl.name + " feels no need to beautify it or make it her own. You suppose it serves its function as a place to recuperate as is.",
                                    # "This room feels very empty. It looks like " + girl.name + " has no belongings to speak of. There are no books, trinkets or personal items anywhere, which makes this room almost anonymous.",
                                    # "The bedroom has a practical layout. No energy has been expended trying to imbue any personality into it.",
                                    # ],
                                # "masochist" : [
                                    # "The room is very spartan. It seems like " + girl.name + " feels no need to beautify it or make it her own. You suppose it serves its function as a place to recuperate as is.",
                                    # "This room feels very empty. It looks like " + girl.name + " has no belongings to speak of. There are no books, trinkets or personal items anywhere, which makes this room almost anonymous.",
                                    # "A sense of unease creeps up on you as you enter " + girl.name + "'s bedroom. The walls are covered in filth and the stench is hard to bear. At least she properly made her bed.",
                                    # ],
                                # "sweet" : [
                                    # "A lot of thought and effort has been put into decorating this room. It perfectly fits " + girl.name + "'s personality. Great attention has been given to the finest details.", 
                                    # "The carefully decorated room truly reflects " + girl.name + " as an individual. Even though she is not here, her atmosphere still lingers.",
                                    # "Much like " + girl.name + ", this bedroom is bright and radiant. Just being here warms your heart and brings a smile to your face.",
                                    # "Vivid colors give this bedroom a childish, carefree atmosphere. The bed is especially inviting. Dozens of comfortable looking pillows are strewn across the floor.",
                                    # ], 
                                # }

        # room_detail_list = {
                                # "meek" : [
                                    # "Trinkets, mementos and paraphernalia can be found on every surface.",
                                    # "You notice a small vase with a single " + girl.likes["color"] + " flower in it.", 
                                    # "" + girl.name + " has decorated the wall abover her bed with various keepsakes and memories of her time with you in the brothel.",
                                    # ],
                                # "nerd" : [
                                    # "Several books are scattered on the floor. One of the titles catches your eye:\"{i}" + random.choice(book_title) + "{/i}\".",
                                    # "Under " + girl.name + "'s pillow you notice a certain book she sleeps with. It reads \"{i}" + random.choice(book_title) + "{/i}\".",
                                    # "Next to " + girl.name + "'s bed lies a book that is starting to fall apart after being read and reread countless times. It's titled {i}" + random.choice(book_title) + "{/i}.",
                                    # ],
                                # "pervert" : [
                                    # "Various used toys are scattered throughout the room.",
                                    # "An easily accessible whip is mounted on one of the walls next to the bed.",
                                    # "You find a collection of very... How should I put this... {i}adventurous{/i} erotic magazines under her bed. One of them is about " + random.choice(pervert_topic) + "!",
                                    # ],
                                # "rebel" : [
                                    # "The floor is littered with empty bottles of alcoholic drinks.",
                                    # "A bouquet of " + girl.likes["color"] + " flowers sits in the windowsill. The flowers are starting to wither.",
                                    # "Her bed is unmade. A cute stuffed animal peeks its head above the covers.",
                                    # "A book titled {i}" + random.choice(book_title) + "{/i} lies discarded in a corner. It's a gift from one of her friends. A personal inscription within reads: \"{i}" + random.choice(sweet_note) + "{/i}\" It's immediately followed by \"{i}BULLSHIT!{/i}\" in [girl.name]'s handwriting.",
                                    # ],
                                # "superficial" : [
                                    # "On " + girl.name + "'s desk you find a stack of notes in which she meticulously evaluates her own performance in the brothel. The notes seem to go way back to her very first night here. You notice cute doodles accompanying the description of a big tip.",
                                    # girl.name + "'s impressive collection of shoes and high heels would make any noblewoman jealous.",
                                    # "A large free standing mirror occupies one of the room's corners. With her lipstick, " + girl.name + " has written a personal mantra on her mirror: \"{i}[" + random.choice(materialist_note) + "{/i}\"",
                                    # ],
                                # "cold" : [
                                    # "On " + girl.name + "'s desk you find a stack of notes in which she meticulously evaluates her own performance in the brothel. The notes seem to go way back to her very first night here.",
                                    # "There is a book next to " + girl.name + "'s bed. It's titled {i}" + random.choice(book_title) + "{/i}. When you open the cover you realise this book is a gift from one of her friends. A personal inscription reads: \"{i}I know you can do it! Shout it from the rooftops! " + random.choice(materialist_note) + "{/i}\"",
                                    # ],
                                # "masochist" : [
                                    # "You notice a bed and a few empty shelves. That pretty much everything there is to this room.",
                                    # "On your way out your eye comes across a message that has been scribbled into the doorframe. It reads: \"{i}" + random.choice(masochist_note) + "{/i}\"",
                                    # "Under " + girl.name + "'s bed you find a clear glass bottle with a yellow tinged liquid inside. You dare not open it. The label on it says: {i}Drink it up, bitch!{/i}",
                                    # girl.name + " has carved a message into the ceiling above her bed. \"{i}" + random.choice(masochist_note) + "{/i}\"",
                                    # ],
                                # "sweet" : [
                                    # girl.name + " has decorated the wall above her bed with various keepsakes and memories of her time with you in the brothel.",
                                    # "On the wall in one corner of the room you can find drawings of every girl in the brothel, along with personalised motivational messages and poems.",
                                    # "The room is full of charming and inspiring quotes, all very neatly written in various bright colors. One of them reads: \"{i}" + random.choice(sweet_note) + "{/i}\"",
                                    # "An inspirational quote on the wall catches your eye. \"{i}" + random.choice(sweet_note) + "{/i}\" " + girl.name + " has drawn beautiful flowers around it in various colors.",
                                    # "A lovely bouquet of  " + girl.likes["color"] + " flowers is enjoying the sunshine in the windowsill."
                                    # ] 
                                # }

        # room_personality_comment = random.choice(room_personality_list[girl.personality.name]) + " " + random.choice(room_detail_list[girl.personality.name])
        
        d = dice(100)
        
        if d < 10:
            
            location = brothel.bedroom_type.name
            girl_state = "rest"
            girl_pic = girl.get_pic("rest", not_tags=["public", "beach", "nature", "town"], naked_filter=True, soft=True)
            girl_state_comment = rand_choice([__("You find her relaxing in her room."),__("She's resting in her room."), __("she is enjoying a well-earned rest in her room."), __("She's recuperating in her room.")])
            
        elif d < 30:
        
            if brothel.get_common_rooms():
                location = brothel.get_random_room_pic_path()

            else:
                location = bg_bro

            girl_state = "profile"
            girl_pic = girl.get_pic("profile", "portrait", not_tags=["public", "beach", "nature", "town"], naked_filter=True, soft=True)
            girl_state_comment = rand_choice([__("You find her hanging around the brothel."),__("She's relaxing in the brothel."), __("She's enjoying a moment's rest in the brothel."), __("she hums a cheerful tune as she skips through the brothel.")])
            
        elif d < 35:
        
            location = brothel.bedroom_type.get_bg()
            girl_state = "naked"
            girl_pic = girl.get_pic("naked", "profile", and_tags=["embar"], not_tags=["public", "beach", "nature", "town"], naked_filter=False, soft=True)
            girl_state_comment = rand_choice([__("You find her in her room."),__("She's staying in her room this morning."), __("She is enjoying a well-earned rest in her room."), __("She's recuperating in her room.")])
            
            if girl.naked == True:
                girl_state_comment += rand_choice([__(" She's naked, as usual."), __(" The sight of her breasts brightens up your morning."), __(" Naturally, she's naked as the day she was born."), ""])
                
            else:
                girl_state_comment += rand_choice([__(" You find her in a compromising situation."), __(" She's undressed for one reason or another."), __(" To your surprise, she's not wearing any clothes."), __(" What a pleasant sight! She happens to be undressed.")])
            

        elif d < 45:
        
            location = brothel.bedroom_type.get_bg()
            girl_state = "naked rest"
            girl_pic = girl.get_pic("naked", "rest", not_tags=["public", "beach", "nature", "town"], naked_filter=False, soft=True)
            girl_state_comment = rand_choice([__("You find her resting in her room."),__("She's resting in her room."), __("She is enjoying a well-earned rest in her room."), __("She's recuperating in her room.")])
            
            if girl.naked == True:
                girl_state_comment += rand_choice([__(" She's naked, as usual."), __(" The sight of her breasts brightens up your morning."), __(" Naturally, she's naked as the day she was born."), ""])
                
            else:
                girl_state_comment += rand_choice([__(" It looks like she wasn't expecting you, judging from her state of undress."), __(" She's undressed for one reason or another."), __(" To your surprise, she's not wearing any clothes."), __(" What a pleasant sight! She happens to be undressed.")])

        elif d < 50:

            location = brothel.bedroom_type.get_bg()
            girl_state = "mast"
            girl_pic = girl.get_pic("mast", and_tags=["embar"], not_tags=["public", "beach", "nature", "town"], naked_filter=False, soft=True)
            girl_state_comment = rand_choice([__("You find her masturbating in her room."),__("She's pleasuring herself in her room."), __("she is enjoying some self-service in her room."), __("She's having some fun in her room.")])

            if girl.naked == True:
                girl_state_comment += rand_choice([__(" She must be looking forward to serving more customers."), __(" Her moans can be heard from the hallway."), __(" She's screaming your name as she climaxes.")])
                
            else:
                girl_state_comment += rand_choice([__(" She scampers to cover herself as you enter the room."), __(" When your eyes meet, she freezes up as if caught in a spell."), __(" She attemts to hide under the bedsheets as you call her name.")])

        elif d < 60:
        
            location = brothel.bedroom_type.get_bg()
            girl_state = "study"
            girl_pic = girl.get_pic("study", not_tags=["public", "beach", "nature", "town"], naked_filter=True, soft=True)
            girl_state_comment = rand_choice([__("She is hard at work, studying to further improve her performance."),__("She's studying some literature, immersed in thought."), __("She is using her downtime productively by studying.")])

        elif d < 80:
        
            if brothel.get_common_rooms():
                location = brothel.get_random_room_pic_path()

            else:
                location = bg_bro

            girl_state = "friend"
            girl_pic = girl.get_pic("friend", not_tags=["public", "beach", "nature", "town"], naked_filter=True, soft=True)
            girl_state_comment = rand_choice([__("She has invited a friend over."),__("She's socialising with one of her friends."), __("One of her friends has come to visit the brothel. They're like two peas in a pod."), __("She has invited one of her friends over. They seem to be getting along well.")])

        else:
        
            if brothel.get_common_rooms():
                location = brothel.get_random_room_pic_path()

            else:
                location = bg_bro

            girl_state = "party"
            girl_pic = girl.get_pic("party", not_tags=["public", "beach", "nature", "town"], naked_filter=True, soft=True)
            girl_state_comment = rand_choice([__("She has invited a few of her friends over."),__("She's socialising with some of her friends, who are visiting the brothel."), __("Some of her friends have come to visit the brothel."), __("She has invited her friends over for a party.")])

        if not girl_pic:
    
            if brothel.get_common_rooms():
                location = brothel.get_random_room_pic_path()

            else:
                location = bg_bro

            girl_state = "profile"
            girl_pic = girl.get_pic("profile", "portrait", not_tags=["public", "beach", "nature", "town"], naked_filter=True, soft=True)
            girl_state_comment = rand_choice([__("You find her hanging around in the brothel."),__("She's relaxing in the brothel."), __("She's enjoying a moment's rest in the brothel."), __("She hums a cheerful tune as she skips through the brothel.")])

    scene black
    with dissolve

    "You decide to visit [girl.name] to congratulate her."    

    $ renpy.show(location, at_list = [top])
    with dissolve

    # "[girl.name] is not present in her room when you arrive. This gives you some time to inspect her living space."
    # "[room_personality_comment]"

    show screen show_event(girl_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
    
    "[girl_state_comment]"

    girl.char "Master! You wanted to see me?"
    
    you "With good reason, [girl.name]. I came here to dish out some praise."
    
    call dialogue(girl, "slave positive reaction")
    
    you "I've just been over the numbers from last month. You've managed to outperform the other girls. Well done!"
    
    call dialogue(girl, "slave thanks")
    
    $ modifier = 0.5
    $ extra_effects = None
    $ effect_comment = None
    
    menu: 
        girl.char "So where do we go from here?"

        "Keep improving yourself": # improve self
    
            you "There is still some room for improvement. That's why I've got some advice for you."
        
            menu:
                girl.char "Yes, Master?"
                
                "Work as hard as you can" if MC.speed > 4: # capacity boost

                    you "I believe you can work even harder. Try to serve more customers every shift."
                    
                    if girl.is_("very extravert"):
                        girl.char "Ooh fantastic! I'll try to beat my personal record!"
                        $ modifier = 2.0
                    elif girl.is_("very modest"):
                        girl.char "I'll work until I break... And then work some more!"
                        $ modifier = 1.0
                    elif girl.is_("very introvert"):
                        girl.char "I prefer giving one customer all of my attention instead of spreading myself thin, but I'll try to do as you ask."
                        $ modifier = 0.25
                    else:
                        girl.char "That makes sense. I'll do my best to follow your advice."
                        
                    $ extra_effects = [Effect("change", "job customer capacity", int(3*modifier))] 
                    $ effect_comment = _("she will try to serve more customers while working")
                    
                "Hoard as much semen as you can" if girl.has_activated_sex_acts() and (dice(6) == 6 or MC.playerclass == "Trader"): # whore as much as possible

                    you "The market price for a gallon of semen has skyrocketed recently. Lord knows why the Elder Circle of Karkyr requires so much of it." 
                    
                    you "Try to milk as many customers as you can each night. No swallowing! You can use that jar over there to collect the spoils."

                    if girl.is_("very lewd"):
                        girl.char "HELL YES! I'll gladly gobble up all the cocks you can throw at me."
                        $ modifier = 2.0
                    elif girl.is_("lewd"):
                        girl.char "Yes sir! I'm certain that I can do even better with a few tweaks to my routine."
                        $ modifier = 1.0
                    elif girl.is_("very modest"):
                        girl.char "Ugh, why? It's never enough for you, is it?"
                        $ modifier = 0.25
                    else:
                        girl.char "Very well... I'll do what I can."
                    
                    $ extra_effects = [Effect("change", "whore customer capacity", int(2*modifier))]
                    $ effect_comment = _("she will attempt to serve more customers while whoring")

                "Focus on the whales" if MC.charisma > 4: # chance tip boost

                    you "You need to spend your time wisely. Try to find the patrons that have the most money to spend and make sure to fully satisfy them. Let the other girls worry about our other customers."

                    if girl.is_("very introvert"):
                        girl.char "Why didn't I think of that! You're absolutely right. I'll give it my all."
                        $ modifier = 2.0
                    elif girl.is_("very extravert"):
                        girl.char "Sorry, but thinking things through just isn't my style. I really don't think it will help."
                        $ modifier = 0.25
                    elif girl.is_("very lewd"):
                        girl.char "I'll do my best, but if that customer turns out to be a lousy lay then I'd rather just move on."
                        $ modifier = 0.25
                    else:
                        girl.char "All right, master. I hope I can improve."
                    
                    $ extra_effects = [Effect("special", "ignore budgets"), Effect("boost", "tip", 0.2, chance=0.25*modifier),Effect("change", "whore customer capacity", -1), Effect("change", "job customer capacity", -2)] 
                    $ effect_comment = _("she will serve less customers but acquire bigger tips")
                    
                "Keep doing what you're doing": # Rep boost

                    you "You're heading in the right direction. If you keep up your current level of performance the customers will be chanting your name in no time."

                    if girl.is_("very dom"):
                        girl.char "Thanks, I'm glad you understand I don't need your advice. I know what I'm doing."
                        $ modifier = 1.5
                    elif girl.is_("very materialist"):
                        girl.char "Yeah, I'm slowly getting the hang of things and just need a bit more time."
                        $ modifier = 1.5
                    elif girl.is_("very sub"):
                        girl.char "A-are you sure? Please just tell me if there's anything I can do to improve."
                        $ modifier = 0.25
                    else:
                        girl.char "Just give me some time. I really want to become an important part of [brothel.name]."
                        
                    $ extra_effects = [Effect("boost", "reputation gains", 0.1*modifier)] 
                    $ effect_comment = _("her reputation will improve more rapidly")
                    
                "Stand up for yourself" if MC.strength > 4 or MC.playerclass == "Warrior": # defense boost
                        
                    you "Don't let anybody push you around. Don't be afraid to fight if you're driven into a corner." 

                    if girl.is_("very dom"):
                        girl.char "Fucking A! I don't mind getting into fights. Actually I kind of enjoy it."
                        $ modifier = 2.0
                    elif girl.is_("very sub"):
                        girl.char "I'm really no good in those situations. I need you by my side!"
                        $ modifier = 0.5
                    elif girl.is_("very idealist"):
                        girl.char "No, that's just wrong! There have to other ways to solve these problems!"
                        $ modifier = 0.25
                    else:
                        girl.char "That sounds daunting, but I'll try my best."
                        
                    $ extra_effects = [Effect("change", "defense", int(2*modifier))] 
                    $ effect_comment = _("she will be on her guard")

                "Focus on training": # Lower train obedience targets

                    you "You've been doing well, but without more training you'll end up wasting away in the gutters of Zan. Pay more attention to my instructions from now on!"
                    
                    if girl.is_("very sub"):
                        girl.char "Yes, naturally! I'm honored to have you as my teacher."
                        $ modifier = 2.0
                    elif girl.is_("very lewd"):
                        girl.char "Please don't hold back. I'm willing to do anything - and I mean {i}anything{/i} - to get better at this."
                        $ modifier = 1.0
                    elif girl.is_("very dom"):
                        girl.char "Ugh... Do I really have to?"
                        $ modifier = 0.25
                    else:
                        girl.char "Y-yes [MC.name], I understand I have to improve."
                        
                    $ extra_effects = [Effect("change", "train obedience target", int(-25*modifier))] 
                    $ effect_comment = _("she will be more willing to undergo training")
                    
                "Serve the customer, no matter what they request" if MC.spirit > 4: # Lower job/whore obedience targets

                    you "Remember that this is a brothel, not some kind of wellness retreat for you to lounge around in. There's no sense in struggling. The customer is king and if he's asking for something then you should provide whatever he needs."

                    if girl.is_("very sub"):
                        girl.char "You're right, I need to get a grip and earn my place here."
                        $ modifier = 1.5
                    elif girl.is_("very modest"):
                        girl.char "I understand what you're asking, but... It just feels so wrong!"
                        $ modifier = 0.25
                    elif girl.is_("very dom"):
                        girl.char "Fuck that! If you want to get in my pants then you have to earn it, it's as simple as that!"
                        $ modifier = 0.25
                    else:
                        girl.char "Please be patient with me, [MC.name]. I need to get used to all of this."
                        
                    $ extra_effects = [Effect("change", "job obedience target", int(-25*modifier)), Effect("change", "whore obedience target", int(-25*modifier))]
                    $ effect_comment = _("she will be less apprehensive about working or whoring")
                    
                "Gain more experience": # boost xp/jp/rep

                    you "You should remain critical of yourself and keep improving!"

                    if girl.is_("very idealist"):
                        girl.char "I'm giving it my all. So many things to learn!"
                        $ modifier = 2.0
                    elif girl.is_("very introvert"):
                        girl.char "Sure, I'll get better in no time, just wait and see!"
                        $ modifier = 1.0
                    elif girl.is_("very materialist"):
                        girl.char "I feel terrible... I'll do whatever it takes to bring in more money."
                        $ modifier = 1.0
                    else:
                        girl.char "I'm sorry... I don't think I'm cut out for this..."
                        
                    $ extra_effects = [Effect("boost", "xp gains", 0.1*modifier), Effect("boost", "all jp gains", 0.1*modifier)] 
                    $ effect_comment = _("she will gain more experience and job proficiency")

                "Consider a spell at the farm" if MC.charisma > 8 or MC.get_alignment() == "evil": # farm boost

                    you "Do you like working with animals?"
                    girl.char "I guess so... Why are you asking?"
                    you "I'm just picturing you rolling around in the mud... I've been thinking about sending some extra help Gizel's way."

                    if girl.is_("very lewd"):
                        play sound "laughs.ogg"
                        girl.char "Heh! Thanks for cheering me up, Master. It sounds like fun, I might just do that."
                        $ modifier = 2.0
                    elif girl.is_("very dom"):
                        girl.char "Well, at the very least animals don't get mad when you insult them."
                        $ modifier = 1.0
                    elif girl.is_("very idealist"):
                        girl.char "That's terrible! Please don't joke about things like that!"
                        you "Oh, I wasn't joking."
                        $ modifier = 0.25
                    else:
                        girl.char "That's awful! ...D-do you really think it'll help?"
                        
                    $ extra_effects = [Effect("boost", "farm preference increase", 0.5*modifier)] 
                    $ effect_comment = _("she will be more susceptible to the training methods used at the farm")
    
        "Help the brothel": # improve brothel
        
            you "With such an outstanding performance you deserve to take on a few more responsibilities. I will be counting on your help to further improve the brothel."
    
            menu:
                girl.char "Is there anything in particular I can help you with?"
 
                "Bring in more customers": # rep/customers boost (scope = brothel)
                
                    you "I have a new advertising campaign in mind for [brothel.name]. For the next few weeks I want you to run a lap through the streets of Zan every night, right before we open our doors."
                    
                    girl.char "Understood, master. But how exactly would that attract more customers?"
                    
                    you "Because you'll be naked. And you'll be carrying this vibrator with you. In your ass."                
                    
                    if girl.is_("very lewd"):
                        girl.char "Ooh I love it! This'll be fun!"
                        $ modifier = 2.0
                    elif girl.is_("very sub"):
                        girl.char "What if... What if I crawled on all fours instead of running?"
                        $ modifier = 1.0
                    elif girl.is_("very idealist"):
                        girl.char "Sigh... I shouldn't have asked."
                        $ modifier = 0.25
                    else:
                        girl.char "Ugh... Fine, if you think it will help [brothel.name]..."
                      
                    $ extra_effects = [Effect("change", "customers", int(4 * modifier), scope="brothel")]
                    $ effect_comment = _("more customers will visit the brothel")
                    
                "Prep for quests and classes" if MC.spirit > 8 or MC.get_alignment() == "good": # quest/class performance boost (scope = brothel) 

                    you "I want you to thoroughly research the quests and classes our girls attend. Properly brief them beforehand!"

                    if girl.is_("very extravert"):
                        girl.char "Gladly! I can already think of some ways to improve our performance..."
                        $ modifier = 2.0
                    elif girl.is_("very idealist"):
                        girl.char "Understood. I'll do my best to make [brothel.name] proud!"
                        $ modifier = 1.0
                    elif girl.is_("very dom"):
                        girl.char "Research? Are you insane? Are you going to ask me to write a thesis next?"
                        $ modifier = 0.25
                    else:
                        girl.char "Okay..."

                    $ extra_effects = [Effect("boost", "quest rewards", 0.5*modifier, scope="brothel"), Effect("boost", "class results", 1*modifier, scope="brothel")]
                    $ effect_comment = _("quests and classes will yield better rewards")
                    
                "Act as a floor manager" if MC.speed > 8 or MC.get_alignment() == "neutral": # job boost (scope=brothel)
                
                    you "The other girls respect and look up to you. You should use this opportunity to take the lead and make sure everything in the brothel runs smoothly."

                    if girl.is_("very materialist"):
                        girl.char "Sweet! I'll make sure every customer leaves with an empty wallet."
                        $ modifier = 2.0
                    elif girl.is_("very dom"):
                        girl.char "Finally I can bark some sense into those fools!"
                        $ modifier = 1.0
                    elif girl.is_("very sub"):
                        girl.char "I-I'm not so sure about this... Will the girls really listen to me?"
                        $ modifier = 0.25
                    else:
                        girl.char "I'll try my best to set an example to follow."

                    $ extra_effects = [Effect("change", "job customer capacity", int(2*modifier), scope="brothel")]
                    $ effect_comment = _("your girls (excluding whores) will be able to serve more customers")
                    
                "Help me with my errands" if MC.speed > 10 or MC.playerclass == "Trader": # resource/city rewards boost

                    you "I want you to accompany me whenever I go to the city. You can help me gather resources for the brothel."

                    if girl.is_("very modest"):
                        girl.char "Thank you! I would love to."
                        $ modifier = 2.0
                    elif girl.is_("very idealist"):
                        girl.char "Sure! I love exploring the city."
                        $ modifier = 1.0
                    elif girl.is_("very lewd"):
                        girl.char "That sounds awfully boring..."
                        $ modifier = 0.25
                    else:
                        girl.char "As you wish."

                    $ extra_effects = [Effect("boost", "city rewards", 1*modifier, scope="brothel"), Effect("change", "city rewards", 1+int(1*modifier), scope="brothel"), Effect("boost", "resource extraction", 1*modifier, scope="brothel")]                
                    $ effect_comment = _("city rewards and resource extraction rates are improved")
                    
                "Punish the other girls" if MC.playerclass == "Warrior" or MC.get_alignment() == "evil": #fear/income boost

                    you "The other girls need to get it into their skulls that if they don't perform like you did, it's a one way trip to the slavemarket. Take this whip and force them to work harder than they've ever worked before."

                    if girl.is_("very dom"):
                        play sound "laughs.ogg"
                        girl.char "Muhahahaha! I'll make you proud and work them to the bone, master."
                        $ modifier = 2.0
                    elif girl.is_("very materialist"):
                        girl.char "I'll make sure the money keeps flowing in!"
                        $ modifier = 1.0
                    elif girl.is_("very idealist"):
                        girl.char "That's horrible! Why do I have to do such a thing?"
                        $ modifier = 0.25
                    else:
                        girl.char "O-okay, if you think it will help..."
                    
                    $ extra_effects = [Effect("boost", "fear gains", 0.25*modifier, scope="brothel")]
                    $ effect_comment = _("fear will increase faster")
                    
                "Protect the other girls from harm" if MC.strength > 10 or MC.playerclass == "Warrior": # defense boost (scope = brothel)

                    you "I'm counting on you to step in if any of our girls get into trouble."

                    if girl.is_("very dom"):
                        girl.char "If anybody tries something funny, I'll destroy them."
                        $ modifier = 2.0
                    elif girl.personality.name == "masochist":
                        girl.char "Oh, I'll try my best to take their place if things escalate."
                        $ modifier = 1.0
                    elif girl.is_("very materialist"):
                        girl.char "Do I really have to? I don't want to mess up my hair or get blood on my clothes..."
                        $ modifier = 0.25
                    else:
                        girl.char "Yes, master."
                    
                    $ extra_effects = [Effect("change", "defense", int(1*modifier), scope="brothel")]
                    $ effect_comment = _("girls in the brothel will be able to defend themselves better")
                    
                "Help me with my enchantments" if MC.spirit > 10 or MC.playerclass == "Wizard": # mana/spirit boost

                    you "Your performance has been quite admirable. Can you show the same dedication in helping me with my spells?"

                    if girl.is_("very introvert"):
                        girl.char "That sounds interesting!"
                        $ modifier = 2.0
                    elif girl.is_("very lewd"):
                        girl.char "Can I be your guinea pig? Maybe you could test some lewd incantations on me!"
                        $ modifier = 1.0
                    elif girl.is_("very extravert"):
                        girl.char "I doubt I'll be of much help, but I'll try."
                        $ modifier = 0.25
                    else:
                        girl.char "Of course! Just let me know what I can do."
                    
                    $ extra_effects = [Effect("change", "mana", int(2*modifier), scope="brothel")]
                    $ effect_comment = _("your available mana will increase")
                    
                "Decorate the brothel" if MC.charisma > 10 or MC.get_alignment() == "good": #love/mood boost

                    you "This place looks like a dump. Spruce it up for me."

                    if girl.is_("very extravert"):
                        girl.char "I would love to! We could put rose petals on the beds, dress up the stage with flowers and candles, I have so many ideas!"
                        $ modifier = 2.0
                    elif girl.is_("very idealist"):
                        girl.char "I can do that! Let's make [brothel.name] an inviting place where everyone will feel at home."
                        $ modifier = 1.0
                    elif girl.is_("very materialist"):
                        girl.char "You want me to decorate? I'm here to sell my body, not my skills as an interior designer..."
                        $ modifier = 0.25
                    else:
                        girl.char "Well, [brothel.name] is our home after all. I'll try to make it look presentable."
                           
                    $ extra_effects = [Effect("boost", "love gains", 0.25*modifier, scope="brothel"),Effect("boost", "prestige", 0.1*modifier, scope="brothel")]
                    $ effect_comment = _("your girls' love and your brothel's prestige will improve more rapidly")
                           
                "Make sure all the girls exercise regularly" if MC.speed > 10 or MC.get_alignment() == "neutral": #energy boost

                    you "Some of the girls can't quite keep up with you. You're in charge of their physical training routine. Make sure they're fit and ready to put in the work."

                    if girl.personality.name == "masochist":
                        play sound "laughs.ogg"
                        girl.char "Hahaha! I'll teach them some of my secrets. There's nothing better than pushing through, even when you barely have any energy left to spare."
                        $ modifier = 2.0
                    elif girl.is_("very dom"):
                        girl.char "Fine, I'll pull them along... As long as they don't slow me down."
                        $ modifier = 1.0
                    elif girl.is_("very introvert"):
                        girl.char "That sounds like a pain. Can't I do something else?"
                        $ modifier = 0.25
                    else:
                        girl.char "I'll make sure the girls of [brothel.name] are fit and ready to serve every night."
                    
                    $ extra_effects = [Effect("boost", "energy use", -0.1*modifier, scope="brothel")]
                    $ effect_comment = _("your girls will use their energy more efficiently"          )      
                    
                "Make sure our farm creatures are well trained" if MC.gold > 10000 or MC.get_alignment() == "evil": #farm boost

                    you "Gizel has told me that some of our farm creatures are losing their edge. I want you to visit the farm daily and pleasure the animals. But make sure they do not climax!"

                    if girl.personality.name in ("pervert", "masochist"):
                        girl.char "Such a dirty and thankless job... I LOVE IT!"
                        $ modifier = 2.0
                    elif girl.is_("very modest"):
                        girl.char "I- I suppose all they need might be a loving girl to care for them..."
                        $ modifier = 1.0
                    elif girl.is_("very materialist"):
                        girl.char "Why? Animals and machines may have cocks but they certainly do not have money. I don't see the point."
                        $ modifier = 0.25
                    else:
                        girl.char "Sure, I don't mind."
                    
                    $ extra_effects = [Effect("boost", "farm preference increase", 0.25*modifier, scope="farm")]
                    $ effect_comment = _("the farm as a whole will be more effective")

                "Be subservient to the other girls" if MC.gold > 10000: # boost brothel income

                    you "You're too selfish. Stop trying so hard to make a name for yourself and instead just do your best to help the other girls."

                    if girl.is_("very sub"):
                        girl.char "Oh, okay... I guess you're right, I need to accept my place at the bottom of the pecking order."
                        $ modifier = 1.5
                    elif girl.is_("very dom"):
                        girl.char "The other girls? Why should I care about them?"
                        $ modifier = 0.25
                    else:
                        girl.char "I'll try my best... But even so, I want to be the best I can be!" 

                    $ extra_effects = [Effect("boost", "income", 0.01*modifier, scope="brothel")] 
                    $ effect_comment = _("your brothel's profits should improve slightly")
    
    hide screen show_event
    
    "If all goes well, in the upcoming week [effect_comment]."

    python:
    
        for eff1 in extra_effects:
        
            girl.add_effects(eff1, expires = calendar.time + 7)
        
    return


label undervalued_interact(girl):

    $ renpy.block_rollback()

    python:
        if not hasattr(girl, 'nickname'):
            girl.nickname = {"adjective" : None, "trait" : None, "noun" : None, "story" : None, "reason1" : None, "reason2" : None, "flag1" : False, "flag2" : False}
            girl.fullnickname = None

        if girl.fullnickname == None:

            # For unknown/undervalued trait event
            pejorative_adjective = ["Slutty",
                                "Careless",
                                "Useless",
                                "Terrible",
                                "Abysmal",
                                "Cheap",
                                "Unprofitable",
                                "Worthless",
                                "Barren",
                                "Abandoned",
                                "Contemptible",
                                "Good-for-nothing",
                                "Dumped",
                                "Deserted",
                                "Forsaken",
                                "Forgotten",
                                "Ignoble",
                                "Afwul",
                                "Ugly",
                                "Dirty",
                                "Banned",
                                "Blacklisted",
                                "Taboo",
                                "Illegal",
                                "Treacherous",
                                "Unreliable",
                                "Dishonest",
                                "Disloyal",
                                "Betraying",
                                "Tricky",
                                "Deceptive",
                                "Undependable",
                                "Banished",
                                "Expelled",
                                "Blackballed",
                                "Ostracized",
                                "Snubbed",
                                "Rejected",
                                "Denied",
                                "Dismissed",
                                "Forbidden",
                                "Stupid",
                                "Foolish",
                                "Incompetent",
                                "Expendable",
                                "Profitless"
                                ]

            pejorative_noun = ["Slut",
                                "Whore",
                                "Slave Slut"
                                "Cunt",
                                "Bitch",
                                "Harlot",
                                "Tramp",
                                "Wench",
                                "Witch",
                                "Bimbo",
                                "Twat",
                                "Hussy",
                                "Hooker",
                                "Hole",
                                "Fiend",
                                "Monster",
                                "Demon",
                                "Gutter Whore",
                                "Rat",
                                "Pig",
                                "Cow",
                                "Cumbucket",
                                "Skank",
                                "Beast",
                                "Hogbeast",
                                "Troll",
                                "Failure",
                                "Disappointment",
                                "Flop",
                                "Loser",
                                "Slave",
                                "Servant",
                                "Reject",
                                "No-no",
                                "Contraband",
                                "Property",
                                "Victim"
                                ]

            undervalued_trait = { "Fighter" : ["Slave Brand", "Irresistable", "Ferocious", "Warrior", "Wild", "Strong", "Tough", "Brave", "Tomboy", "Rowdy", "Powerful", "Cold", "Rude", "Mean", "Rough", "Defiant", "Rebellious", "Frigid", "Prude", "Arrogant", "Stubborn"],
                                "Lover" : ["Slave Brand", "Insatiable", "Noble", "Loose", "Sensitive", "Vicious", "Delicate", "Temptress", "Dominatrix", "Thief", "Drunkard", "Jaded", "Distrustful", "Fearful", "Depressed", "Deceitful", "Vulnerable", "Greedy", "Naive", "Lazy"],
                                "Choker" : ["Slave Brand", "Ferocious", "Uninhibited", "Cum Addict", "Bimbo", "Pervert", "for Public use", "Cumslut", "Kinky", "Orgy girl", "Uncouth", "Scruffy", "Vulgar", "Strong Gag Reflex", "Clumsy", "Sickly", "Unlucky", "Awkward", "Weak", "Timid"],
                                "Believer" : ["Slave Brand", "Caster", "Sexually curious", "Open-minded", "Exotic", "Naughty", "Submissive", "Meek", "Fast Orgasms", "Exotic Tattoo", "Disfigured", "Frail", "Paranoid", "Dumb", "Oafish", "Slow", "Godless", "Trauma", "Scars", "City girl", "Circumcised"]
                                }

            undervalued_trait_nick = {
                                "Irresistable" : "Taboo",
                                "Ferocious" : "Barbaric",
                                "Warrior" : "Heroic",
                                "Wild" : "Untamed",
                                "Strong" : "Big",
                                "Tough" : "Solid",
                                "Brave" : "Bold",
                                "Tomboy" : "Manly",
                                "Rowdy" : "Annoying",
                                "Powerful" : "Mighty",
                                "Cold" : "Icy",
                                "Rude" : "Savage",
                                "Mean" : "Blunt",
                                "Rough" : "Raw",
                                "Defiant" : "Sassy",
                                "Rebellious" : "Disloyal",
                                "Frigid" : "Cool",
                                "Prude" : "Good",
                                "Arrogant" : "Cocky",
                                "Stubborn" : "Donkey",

                                "Insatiable" : "Goddess",
                                "Noble" : "Highborn",
                                "Loose" : "Easy",
                                "Sensitive" : "Pussy",
                                "Vicious" : "Evil",
                                "Delicate" : "Crumbling",
                                "Temptress" : "Siren",
                                "Dominatrix" : "Tyrant",
                                "Thief" : "Rat",
                                "Drunkard" : "Party",
                                "Jaded" : "Worn-out",
                                "Distrustful" : "Cynical",
                                "Fearful" : "Pants Pissing",
                                "Depressed" : "Sad",
                                "Deceitful" : "Crafty",
                                "Vulnerable" : "Naked",
                                "Greedy" : "Rich",
                                "Naive" : "Ignorant",
                                "Lazy" : "Trifling",

                                "Ferocious" : "Ravenous",
                                "Uninhibited" : "Unleashed",
                                "Cum addict" : "Thirsty",
                                "Bimbo" : "Slut",
                                "Pervert" : "Wet",
                                "for Public use" : "Public",
                                "Cumslut" : "Hole",
                                "Orgy girl" : "Group",
                                "Uncouth" : "Cheap",
                                "Scruffy" : "Run-down",
                                "Vulgar" : "Fucking",
                                "Strong gag reflex" : "Choking",
                                "Clumsy" : "Shit",
                                "Sickly" : "Dead",
                                "Unlucky" : "Black",
                                "Weak" : "Crippled",
                                "Timid" : "Quiet",

                                "Caster" : "Magical",
                                "Sexually curious" : "Wandering",
                                "Open-minded" : "Heretic",
                                "Exotic" : "Foreign",
                                "Naughty" : "Foxy",
                                "Submissive" : "Sheepish",
                                "Meek" : "Shy",
                                "Fast orgasms" : "Cum comet",
                                "Exotic tattoo" : "Canvas",
                                "Disfigured" : "Defaced",
                                "Frail" : "Broken",
                                "Paranoid" : "Insane",
                                "Dumb" : "Thick",
                                "Oafish" : "Simple",
                                "Slow" : "Dreaming",
                                "Godless" : "Devil",
                                "Trauma" : "Used",
                                "Scars" : "Struck",
                                
                                "Slave brand" : "Kosmo's",
                                "Lesbian" : "Carpetmunching",
                                "City girl" : "Gutter",
                                "Circumcised" : "Cut", 
                                "Inbred" : "Incestual",
                                "Chaste" : "Pious",
                                "Kidnapped" : "Stolen",
                                "Asexual" : "Loveless",
                                "Bloodslut" : "Meatsleeve",
                                "Half-elf" : "Elven",
                                "Monsterkin" : "Demonic",
                                "Vivified" : "Puppet",
                                }
            
            girl.nickname["story"] = rand_choice(["Fighter", "Lover", "Choker", "Believer"])
            girl.nickname["adjective"] = rand_choice(pejorative_adjective)
            girl.nickname["noun"] = rand_choice(pejorative_noun)

            trait_list = [] # The hidden trait will be randomly picked

            for trait in gold_traits + pos_traits + neg_traits:
                if trait.name in undervalued_trait[girl.nickname["story"]]:
                    if trait.name in girl.init_dict["base positive traits/never"]:
                        pass
                    elif trait in girl.traits:
                        pass
                    elif trait.name in girl.init_dict["base positive traits/often"]:
                        trait_list.append((trait, 4))
                    elif trait.name in girl.init_dict["base positive traits/rarely"]:
                        trait_list.append((trait, 1))
                    else:
                        trait_list.append((trait, 2))
                            

            girl.nickname["trait"] = weighted_choice(trait_list)

            verb = girl.nickname["trait"].verb
            adjective = girl.nickname["adjective"]
            noun = girl.nickname["noun"]

            if girl.nickname["trait"].name in undervalued_trait_nick:
                trait = "" + undervalued_trait_nick[girl.nickname["trait"].name]

            else:
                trait = "" + girl.nickname["trait"].name

            girl.fullnickname = "{i}" + adjective + " " + trait + " " + noun + "{/i}"

            # Well, the truth is... (reasons for undervalue)
            undervalued_reason1 = { "Fighter" : [
                                    __("He tried to force himself onto me and I resisted."),
                                    __("I stuck a knife between his ribs when attempted to abuse me in my sleep. Sadly he survived."),
                                    __("He physically abused me one too many times and I... I decided to fight back and bit his ear off."),
                                    __("I laughed in his face when he said he wanted to keep me all to himself."),
                                    ],
                                    "Lover" : [
                                    __("Him and I used to be a lot closer. Very close actually. But eventually we broke up."),
                                    __("He was actually my lover for a little while, but it didn't work out and he never got over it."),
                                    __("We had a very intimate relationship at one point... Until he found out I also had an intimate relationship with his brother."),
                                    __("I loved him. Then one day I begged him to not let me serve any more customers, so I could be there just for him... He refused...")
                                    ],
                                    "Choker" : [
                                    __("He brought me along to an orgy at the slavers guild. I choked and vomited on the guildmaster's cock."),
                                    __("He was very fond of me and invited me to a party at the slavers guild. I guess I broke the slavers code by sneaking into a bedroom with one of his rivals."),
                                    __("We were pretty daring. I once sucked his cock during a funeral procession. It became a big scandal and he was kicked out of the slavers guild."),
                                    __("The slavers guild revoked his membership after I became involved in a sex scandal with dozens of supposedly celibate religious figureheads.") 
                                    ],
                                    "Believer" : [
                                    __("He thinks I might be cursed. I lost my virginity on a quest by performing what later turned out to be a demonic sex ritual."),
                                    __("One day he made me stand on an ominous pentagram and started chanting. For some reason the spell he tried to perform did not work, and he blamed me for it."),
                                    __("One day the preacher invited into the inner sanctum, where we had a little fun. Someone saw us and it caused an uproar because we desecrated the church."),
                                    __("It's quite a silly story... He is a pious man, and at some point I got caught shoving a Holy Cross up my ass. He did not like that.")
                                    ]
                                    }

            undervalued_reason2 = [__("After that he gave me the nickname ") + adjective + " " + trait + " " + noun + __(". I guess that name must have spread like wildfire."),
                                    __("And then he wrote a song about me, 'The Ballad of ") + trait + " " + noun + __("', it wasn't very flattering to say the least."),
                                    __("Word must have spead quickly. The next day we suddenly had more visitors than usual. They were all looking and pointing in my direction."),
                                    __("For the next few weeks he made me walk around town with a sign around my neck that read '") + adjective + " " + trait + " " + noun + __("! SHAME!'"),
                                    __("Things escalated... The aftermath somehow made people call me ") + trait + __(". That's all you really need to know."),
                                    __("Ever since that day he has held some sort of grudge against ") + trait + __(" girls and he seems to be influencing the other slavers."),
                                    __("Then everyone started calling me ") + trait + __(" behind my back... Does that make me worthless? The slavers seem to think so."),
                                    __("He still tells humiliating stories about it to this day."),
                                    __("After that I became the butt of many jokes within the slavers guild."),
                                    __("I had to endure some torture after that. Thankfully my circumstances have improved since then."),
                                    __("Suddenly I became known around town as the ") + adjective + " " + trait + " " + noun + _("."),
                                    __("The next day everyone was talking about it, spreading a heavily exaggerated story."),
                                    __("Some days later I visited the church, where a Chaplain spat in my face and called me a ") + adjective + " " + noun + __(". Now everyone hates me."),
                                    __("The following day the towncrier had a popular story to tell about 'The ") + adjective + " " + trait + " " + noun + __("' and people seem to remember that to this day."),
                                    __("He must have some very powerful friends in the slavers guild, because they now want nothing to do with me.")
                                    ]
            
            girl.nickname["reason1"] = random.choice(undervalued_reason1[girl.nickname["story"]])
            girl.nickname["reason2"] = random.choice(undervalued_reason2)

    $ room = brothel.get_random_room_pic_path()
    $ renpy.show(room, at_list = [top])
    with dissolve

    python:

        verb = girl.nickname["trait"].verb
        adjective = girl.nickname["adjective"]
        noun = girl.nickname["noun"]

        if girl.nickname["trait"].name in undervalued_trait_nick:
            trait = "" + undervalued_trait_nick[girl.nickname["trait"].name]

        else:
            trait = "" + girl.nickname["trait"].name

    if girl.nickname["flag1"] == False: 
        "For some reason none of the slavetraders that frequent your establishment seem interested in [girl.name], despite her best efforts."
        "Could it be that she has some quarrel with the slavers guild? Now might be a good time to get to the bottom of this."
    elif girl.nickname["flag2"] == False: 
        "You have discovered that [girl.name] is disliked by the slavers guild, and that some people refer to her as {i}[girl.fullnickname]{/i}."  
        "More than likely she has been trying to conceal some [trait] part of her. It must be connected to her quarrel with the slavers guild."
    else:
        "You've found out why [girl.name] is disliked by slavers guild. She has had a troubled past and is now known by some as {i}'The [girl.fullnickname]'{/i}."
        "It's time to figure out how to resolve this situation."

    if girl.nickname["flag2"] == False: 

        $ reason1 = girl.nickname["reason1"]
        $ reason2 = girl.nickname["reason2"]

        $ bribebase = int(round(girl.get_price("sell") / 5,-1))
        $ settlementcost = int(round(bribebase * 2.5,-2))

        menu .undervalued_explanation: #explanation

            "What should you do?"
            
            "Confront her":

                $ room = "bedroom"
                                    
                if girl.job:
                
                    $ room = job_room_dict[girl.job]
                
                $ renpy.show(room, at_list = [top]) 

                if girl.job == "whore":
                    $ pic = girl.get_pic("naked", and_tags=["profile"], naked_filter=True, soft=True)
                else:
                    $ pic = girl.get_pic(girl.job, and_tags=["rest"], naked_filter=True, soft=True)
                
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with dissolve

                girl.char "You wanted to speak to me, master?"

                menu:

                    "Ask her about [girl.fullnickname]" if girl.nickname["flag1"] == True:

                        you "I've heard some of the slavers refer to you as [girl.fullnickname]. Care to explain?"

                        girl.char "Ugh... They still call me that? I wish they would just forget about it."

                        you "Well clearly they did not. Out with it now, why are you known as [girl.fullnickname]?"

                        girl.char "I'm sorry sir, I should have told you sooner. It's about something that happened to me under my previous owner."

                        girl.char "[reason1]" 

                        girl.char "[reason2]"

                        you "That explains things. Resume your duties, I'll have to think of a way for you to clear your name with the slavers guild."

                        girl.char "Yes master, thank you master!"

                        $ girl.nickname["flag1"] = True
                        $ girl.nickname["flag2"] = True
                        
                        hide screen show_event
                        
                        return

                    "Bring it up in casual conversation" if girl.nickname["flag1"] == False:

                        you "Hello [girl.name], good to see you. Is everything going well?"

                        girl.char "Ehm... Yes sir. It's just a typical day I suppose."

                        you "Hmm yes, quite. The weather has been rather nice this week."

                        girl.char "Sure... Is there anything I can do for you sir?"

                        you "Well yes there is actually, you could start being honest with me. Tell me why the slavers guild seems to despise you."

                        if dice(6) <= 2:

                            girl.char "Are those pigs still dragging my name through the mud? Just because of one little mishap with my previous owner..."

                            you "Keep talking."

                            girl.char "Well, you see... [reason1]"

                            you "Is that why the slavers dislike you?"

                            girl.char "It must be! [reason2]"

                            you "I have heard enough, get out of my sight."

                            you "You should be ashamed of yourself. You have put my reputation as a slave trader on the line by not telling me about this as soon as possible."
                            
                            $ girl.nickname["flag1"] = True
                            $ girl.nickname["flag2"] = True
                            
                            hide screen show_event
                            
                            return

                        else:

                            girl.char "The slavers guild, really? I-I don't understand!"

                            girl.char "I-I don't know what to tell you. This must be a big misunderstanding."

                            you "In a way it must be, since you are misunderstanding the situation you are in."

                            you "As long as the slavers guild doesn't like you, you are a liability to me. You are worthless!"

                            you "Next time we discuss this you'd better have some answers."
                            
                            hide screen show_event

                            return

                    "Intimidate her" if MC.playerclass == "Warrior" or MC.get_alignment() == "evil" or MC.strength >= 4:

                        you "[girl.name], I've got some bad news."

                        girl.char "Oh no! What's wrong?"

                        you "You are worthless."

                        girl.char "That's cruel! Stop joking around like that... I know you don't really think that"

                        you "It's not a joke. Far from it. If the slavers guild says you're worthless, it doesn't matter what I think. Worthless is what you are."

                        girl.char "The slavers guild?"

                        you "Yes, the slavers guild. And a simple slave trader like me can't afford to have a disagreement with the slavers guild. So I'm afraid you will have to waste away at the farm for the rest of your life."

                        girl.char "Please no! I-I can explain!"

                        you "Explain it then!"

                        if dice(6) <= 4:

                            girl.char "It's my previous owner - he must be behind this! [reason1]" 

                            girl.char "[reason2]"

                            you "I see. So even if you are worthless now, you might not be worthless forever."

                            you "Thank you. You can go now, I'll do what I can to help you."
                            
                            $ girl.nickname["flag1"] = True
                            $ girl.nickname["flag2"] = True
                            
                            hide screen show_event
                            
                            return

                        else:

                            girl.char "I can understand why I might not that in demand, everyone girl their strengths and weaknesses after all."

                            girl.char "But to keep calling me worthless and threatening to send me to the farm... That's just being mean!"

                            girl.char "And I don't understand why you're bringing up the slavers guild. Do they like bullying girls for their shortcomings as much as you do?"

                            "After her outburst, [girl.char] bursts into tears and storms off. You may have gone a bit too far this time."
                            
                            hide screen show_event

                            jump .undervalued_end_2

                    "No, I've changed my mind": 

                        girl.char "Oh... Okay?"
                        
                        hide screen show_event

                        jump .undervalued_explanation

            "Bribe a slaver for information" if MC.gold >= bribebase * 1.35 and girl.nickname["flag1"] == False:

                $ bribecost = int(round(bribebase * random.uniform(0.7, 1.3),-1))
                
                hide screen show_event
                
                menu:

                    "You estimate a slaver would ask for around [bribebase] gold in exchange for information. Proceed?"

                    "Yes":
                    
                        scene black with fade
                        show bg tavern_man at truecenter with dissolve

                        "You decide to approach a slaver, to request information surrounding [girl.name]'s dubious valuation."

                        "As expected, the slave trader doesn't pass up this opportunity to make some easy money." 

                        play sound s_gold
                        $ MC.gold -= bribecost
                        $ d = dice(6)

                        if d <= 3:
                            "As you slip [bribecost] gold into his pocket, he leans forward and volunteers some information."

                            "Slave Trader" "[girl.name]? We only know her as [girl.fullnickname]. She is on the blacklist under that name."

                            "And with that the slaver takes his leave."

                            "When the time is right you should speak to [girl.name] about this. I'm sure the name [girl.fullnickname] will jog her memory."

                            $ girl.nickname["flag1"] = True
                            return

                        elif d == 4:

                            "The slaver grins from ear to ear after you hand him a bribe of [bribecost] gold."

                            "Slave Trader" "Ah, I love the sound of gold entering my pockets. Doubly so if it comes at the expense of a fellow slaver such as yourself."

                            you "Alright already, I can already tell you've got some bad news for me. Just tell me what I need to know."

                            "Slave Trader" "You've bought a real gutter rat this time. I don't think you'll see a big return on her."

                            you "Damn! Do her problems with the slavers guild run that deep?"

                            "Slave Trader" "Slavers guild? The guild has nothing to do with it. She's just a stinker, that's all. You should really be exercising due diligence."

                            you "Yeah yeah, spare me the lecture. My day is bad enough as it is. Just fill me in on the details..."

                            jump .undervalued_end_2

                        else:

                            "You hand over [bribecost] gold to the slaver, who seems in good spirits."

                            "Slave Trader" "That's the easiest money I've ever made. I'm sorry to say you have been misinformed, [MC.name]."

                            you "How so?"

                            "Slave Trader" "I have never heard of this [girl.lastname] girl. Heaven knows why you'd think that the slavers guild would hold some sort of grudge against her."

                            you "Are you sure? Her reduced rate at the slavemarket has made me very suspicious about this investment."

                            "Slave Trader" "I'm glad I could ease your mind then, there's nothing fishy about this girl and I'm sure you could make a sizeable profit whenever you decide to sell her on."

                            "Slave Trader" "Today is a good day, [MC.name]! Let's have a drink to celebrate our good fortune."

                            you "Cheers! About that [bribecost] gold though..."

                            "Slave Trader" "Yes [MC.name], many thanks for filling my purse. Glad I could be of help!"

                            jump .undervalued_end_3

                    "No":
                    
                        hide screen show_event
                    
                        jump .undervalued_explanation

            "Analyze her behavior carefully" if girl.nickname["flag1"] == False and MC.interactions >= 2: 

                "There must be something about [girl.name] that is making the slavers disinterested."

                "Perhaps you can gain a better understanding of what's going on by observing her from a distance as she interacts with customers."

                if girl.job == "whore":
                    $ sex_act = rand_choice([act for act in girl.does.keys() if act in all_sex_acts and girl.does[act] == True])
                    $ pic = girl.get_pic(sex_act, naked_filter=True, soft=True)
                else:
                    $ pic = girl.get_pic(girl.job, naked_filter=True, soft=True)
                
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with dissolve

                "You watch carefully as [girl.name] goes about her business."
                
                $ MC.interactions -= 2
                
                $ d = dice(6)

                if d <= 4:

                    "As you're watching her, two customers standing near you follow your eyeline and start looking in the same direction."

                    "Customer #1" "Wait a minute... That gal over there, isn't that [girl.fullnickname]?"

                    "Customer #2" "I'll be damned, it is! Bless that [noun]! I'm glad to see she's still hanging on after what happened."

                    "Did he just call her [girl.fullnickname]?"

                    "The story will surely become clear once you get the opportunity to confront [girl.name] about that strange nickname of hers."

                    $ girl.nickname["flag1"] = True
                    
                    hide screen show_event
                    
                    return

                elif d == 5:

                    "Now that you're paying closer attention to her, you suddenly understand much more about her shortcomings."
                    
                    hide screen show_event

                    jump .undervalued_end_2

                else:

                    "Unfortunately, nothing seems out of the ordinary today."
                    
                    hide screen show_event

                    return


            "Leave her be": 

                "You decide to leave this situation alone for now and return to it at a later date."
                
                hide screen show_event

                return
                
        hide screen show_event

        return

    else: #solution

        menu .undervalued_solution:

            "How can I resolve this situation?"

            "Shower her with praise on stage" if MC.charisma >= 5:

                "You demand everyone's attention and head towards the stage."

                $ renpy.show("strip club", at_list = [top])
                with dissolve

                you "For tonight's special presentation, I would like to introduce everyone to one of [brothel.name]'s loveliest flowers."

                "You gesture towards [girl.name] to join you on stage."

                "She nervously climbs the stage, unsure about your intentions."

                show screen show_event(girl.get_pic("profile", naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                girl.char "H-hello everyone. I hope you're enjoying tonight's service."

                "[girl.name] makes a curtsy towards the gathering crowd."

                you "I've heard that some of you may know her as [girl.fullnickname]."

                play sound s_sigh

                "You hear the crowd grumbling and notice that [girl.name] is visibly startled at the mention of '[girl.fullnickname]'"

                you "Well, tonight it's time we put that name to bed, because [girl.fullnickname] is so much more than that."

                python:
                    text1 = ""

                    for traits in girl.traits:
                        if traits.name != "Unknown":
                            text1 += traits.base_description + " "

                    text1 += __("And that's just scratching the surface!")

                you "She's a fantastic girl with so many different qualities."

                you "For example: [text1]" 

                "[girl.name] is a little embarrassed by your words and the crowd's attention."

                you "Now, how could you dismiss such a girl as a [trait] [noun]?"

                you "At [brothel.name] we pride ourselves in our rich offering of multi-talented girls. Their extensive training and expertise is unparalleled."

                you "And thus, I take issue with the suggestion that [girl.name] is defined by {i}one little thing{/i} that happened in her past. And so should you!"

                you "I guarantee that spending one night at her side will invigorate you and make you forget the past, yours and hers."

                you "Now let's drink and enjoy ourselves without inhibitions, secure in the knowledge that whatever happens tonight will be just {i}one little thing{/i} that nobody should judge you for!"

                play sound s_cheer

                "The crowd erupts into applause and swarms the stage. Aided by your speech [girl.name] is the center of attention tonight." 

                "You notice that even the slavers that frequent your brothel are infected by the crowd's enthusiasm. This will surely clear [girl.name]'s name!"
                
                hide screen show_event

                jump .undervalued_end_1

            "Use a spell to boost her appeal" if MC.playerclass == "Wizard" or MC.spirit >= 5: 

                "If I could boost [girl.name]'s appeal with an enchantment, customers might start seeing her in a different light."

                hide screen show_event
                scene black with fade

                "You prepare a magic potion and meet with [girl.name] to administer it."

                $ renpy.show(brothel.bedroom_type.get_bg(), at_list = [top])
                with dissolve

                show screen show_event(girl.get_pic("profile", naked_filter=True, soft=True), x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                girl.char "Are you sure this will work?"

                you "The potion will have its effect. Whether that will solve your conflict with the slavers guild is another matter."

                you "The acting components are not very palatable, so I've used some fiends cum to enhance its flavor."

                girl.char "Yikes... Let's just get this over with."

                "[girl.name] pinches her nose and swiftly drinks down the concoction."

                play sound s_spell
                $ girl.add_effects(Effect("change", "valuation", +30), expires = calendar.time + 3)

                hide screen show_event
                scene black with fade

                "For the next few days, [girl.name] will temporarily fetch a higher price on the market."

                if dice(6) <= 3:

                    "On top of that, the slavers have taken notice and reevaluated [girl.name]'s base value!"

                    jump .undervalued_end_1

                else:

                    "However it appears that her problems with the slavers guild remain."

                    return


            "Embrace her nickname":

                "I'll turn this situation on its head and use it to endear her to [brothel.name]'s customers!"

                "I'm sure the slavers will have a good laugh as well if I officially change [girl.name]'s name."

                "She might not like it, but it's worth a shot if it can get us past this issue."
                
                hide screen show_event
                scene black with fade

                menu:
                    "What should I call [girl.fullname] from now on?"

                    "[girl.name] the [noun]":

                        python:
                            girl.lastname = "the " + noun
                            girl.fullname = girl.name + " " + girl.lastname

                        "She is now known as [girl.fullname]."

                        if dice (6) >= 3:

                            jump .undervalued_end_1

                        else:

                            "Despite this, the slavers guild hasn't budged an inch and her name is still not cleared."
                            return

                    "[girl.name] the [trait]":

                        python:
                            girl.lastname = "the " + trait
                            girl.fullname = girl.name + " " + girl.lastname

                        "She is now known as [girl.fullname]."

                        if dice (6) >= 3:

                            jump .undervalued_end_1

                        else:

                            "Despite this, the slavers guild hasn't budged an inch and her name is still not cleared."
                            return
                    "[trait] [girl.lastname]":

                        python:
                            girl.name = trait
                            girl.fullname = girl.name + " " + girl.lastname

                        "She is now known as [girl.fullname]."

                        if dice (6) >= 3:

                            jump .undervalued_end_1

                        else:

                            "Despite this, the slavers guild hasn't budged an inch and her name is still not cleared."
                            return

                    "[adjective] [girl.name] [girl.lastname]":

                        python:
                            girl.name = adjective + " " + girl.name
                            girl.fullname = girl.name + " " + girl.lastname

                        "She is now known as [girl.fullname]."

                        if dice (6) >= 3:

                            jump .undervalued_end_1

                        else:

                            "Despite this, the slavers guild hasn't budged an inch and her name is still not cleared."
                            return

                    "[trait] [girl.name] the [noun]":

                        python:
                            girl.name = trait + " " + girl.name
                            girl.lastname = "the " + noun
                            girl.fullname = girl.name + " " + girl.lastname

                        "She is now known as [girl.fullname]."

                        if dice (6) >= 3:

                            jump .undervalued_end_1

                        else:

                            "Despite this, the slavers guild hasn't budged an inch and her name is still not cleared."
                            return

                    "[trait] [noun]":

                        python:
                            girl.name = trait
                            girl.lastname = noun
                            girl.fullname = girl.name + " " + girl.lastname

                        "She is now known as [girl.fullname]."

                        if dice (6) >= 3:

                            jump .undervalued_end_1

                        else:

                            "Despite this, the slavers guild hasn't budged an inch and her name is still not cleared."
                            return

                    "[adjective] [trait] [noun]":

                        python:
                            girl.name = adjective + " " + trait
                            girl.lastname = noun
                            girl.fullname = girl.name + " " + girl.lastname

                        "She is now known as [girl.fullname]."

                        if dice (6) >= 3:

                            jump .undervalued_end_1

                        else:

                            "Despite this, the slavers guild hasn't budged an inch and her name is still not cleared."
                            return

                    "On second thought, she doesn't deserve this":

                        jump .undervalued_solution

            "Send her off to serve the slavers guild for a week":

                "A brothel owner like myself can't afford to get on the slavers guild's bad side."

                "Let's settle this quickly by sending [girl.name] on a redemption quest."

                "I'll head straight to the guild to strike a deal."

                hide screen show_event
                scene black with fade
                show bg tavern_man at truecenter with dissolve

                "Slave Trader" "Greetings, [noun] peddling [MC.name]. State your business."

                you "I'm here to talk about [girl.name]."

                "Slave Trader" "Why would we be interested in such [adjective] goods."

                "Slave Trader" "That [trait] girl has nothing to offer us besides disappointment. There's no profit in disappointment."

                you "No profit? Then how about this: As a gesture of goodwill, I'm willing to tank my own profits so that you can give this girl another chance."

                "Slave Trader" "Keep talking..."

                you "You can make use of her services for the upcoming week. And I'll replace her usual fee on the contract with a token amount."

                you "What you do with her is your business, and any profits gained from it are yours to keep."

                "Slave Trader" "Hmm..."

                "Slave Trader" "You know the way to a slaver's heart is through enlarging his coinpurse. We have a deal."

                "Slave Trader" "In exchange, we'll reconsider our reservations towards [girl.name] the [trait]."

                "Slave Trader" "I'll take her with me right away."

                call take_leave(girl, 7)

                jump .undervalued_end_1

            "Reach a settlement with the slavers guild" if MC.gold >= settlementcost:

                "The slaver guild's mind can easily be swayed with the right amount of gold."

                "Let's pay them a visit."

                hide screen show_event
                scene black with fade
                show bg tavern_man at truecenter with dissolve

                "Slave Trader" "Well, if it isn't [MC.name]! Your dubious investments have been a topic of conversation at the slavers guild lately."

                "Slave Trader" "Are you here to get rid of your [trait] [noun] by chance? If so, we are not interested in those damaged goods."

                you "No actually, I stand by that investment."

                "Slave Trader" "Oh?"

                you "I wish to make a fair exchange to clear her name. I'm sure we can agree that everything has a price."

                "Slave Trader" "That's a certainty."

                "Slave Trader" "I can smooth things over for her, but it'll cost you..."

                menu:

                    "Slave Trader" "I can do as you ask for [settlementcost] gold."

                    "We have a deal!":
                        play sound s_gold
                        $ MC.gold -= settlementcost

                        "Slave Trader" "Pleasure doing business!"   

                        jump .undervalued_end_1

                    "I'm not willing to pay that price":

                        "Slave Trader" "Then stop wasting my time and get out."

                        return

            "Perhaps some other time":

                "You decide to ignore the situation for now and return to it at a later date."

                return

        return

#end of event chain
label .undervalued_end_1: #slavers guild

    play sound s_success
    hide screen show_event
    scene black with fade

    $ pasttense = girl.nickname["trait"].get_past_tense()

    "You have understood that [girl.name] was known as [girl.fullnickname] because she [pasttense]."
    "She is no longer blacklisted by the slavers guild."

    python:
        for trait in girl.traits:
            if trait.name == "Unknown":
                girl.remove_trait(trait)
                add_trait_perkless(girl, girl.nickname["trait"])

    $ girl.nickname = {"flag1" : False, "flag2" : False}
    $ girl.fullnickname = None

    return


label .undervalued_end_2: #negative trait

    play sound s_fizzle
    hide screen show_event
    scene black with fade

    python:
        for trait in girl.traits:
            if trait.name == "Unknown":
                girl.remove_trait(trait)

                trait_list = [] # The hidden trait will be randomly picked

                for trait in neg_traits:
                    if trait.name in girl.init_dict["base positive traits/never"]:
                        pass
                    elif trait in girl.traits:
                        pass
                    elif trait.name in girl.init_dict["base positive traits/often"]:
                        trait_list.append((trait, 4))
                    elif trait.name in girl.init_dict["base positive traits/rarely"]:
                        trait_list.append((trait, 1))
                    else:
                        trait_list.append((trait, 2))
                
                newtrait = weighted_choice(trait_list)
                add_trait_perkless(girl, newtrait)

    "There's something you've failed to notice about [girl.name] until this moment: [newtrait.base_description]"
    "That also explains why she was not in high demand at the slavemarket."

    $ girl.nickname = {"adjective" : None, "trait" : None, "noun" : None, "story" : None, "reason1" : None, "reason2" : None, "flag1" : False, "flag2" : False}
    $ girl.fullnickname = None

    return


label .undervalued_end_3: #no trait

    play sound s_success
    hide screen show_event
    scene black with fade

    "You've understood that there is nothing wrong with [girl.name] and you're well within your right to demand a higher fee for her at the slavemarket."

    python:
        for trait in girl.traits:
            if trait.name == "Unknown":
                girl.remove_trait(trait)
                
    $ girl.nickname = {"adjective" : None, "trait" : None, "noun" : None, "story" : None, "reason1" : None, "reason2" : None, "flag1" : False, "flag2" : False}
    $ girl.fullnickname = None

    return

label fix_neg_interact(girl, trait = trait):

    $ newtrait = traitking_neg_evolved[trait.name]
    $ room = brothel.get_random_room_pic_path()

    $ description = "" + traitking_neg_evolved_desc[trait.name + " description"]
    $ old_description = "" + trait.base_description.lower()
    $ new_description = "" + traitking_neg_evolved[trait.name].base_description.lower()
    $ training = "" + traitking_neg_evolved_desc[trait.name + " training"]
    $ intro = "" + traitking_neg_evolved_desc[trait.name + " intro"]
    $ pos_reaction = "" + traitking_neg_evolved_desc[trait.name + " pos_reaction"]
    $ neg_reaction = "" + traitking_neg_evolved_desc[trait.name + " neg_reaction"]

    $ renpy.show(room, at_list = [top])
    with dissolve

    "Although [girl.name] has come a long way, there is still one weakness that she hasn't been able to overcome."

    "[trait.base_description]"

    "Lately she has been telling you that she really wants to try to [description]"

    menu:
        "Would you like to help her?"

        "Training: [training]":

            scene black with fade
            hide screen show_event

            "It might not be possible to completely fix this weakness, but you're willing to work with her to make the most of it."

            python:
                tag = traitking_neg_evolved_desc[trait.name + " pic"]
                and_tags = traitking_neg_evolved_desc[trait.name + " and_tag"]
                pic = girl.get_pic(tag, and_tags=[and_tags], naked_filter=True, soft=True)

            "[intro]"

            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            with dissolve

            if dice(6) >= 4:

                "[pos_reaction]"
                
                $ girl.neg_fix_counter += 1

                hide screen show_event

            else:
                "[neg_reaction]"

                hide screen show_event


            if girl.neg_fix_counter == 0:

                "She still has a long way to go if she wants to improve herself."

            elif girl.neg_fix_counter == 1:

                "She has made some progress towards fixing this weakness."

            elif girl.neg_fix_counter == 2:

                "She has nearly completed her training. You suspect that when this is all over, [new_description]"

            elif girl.neg_fix_counter >= 3:

                "[girl.name] has finally overcome her weakness!"

                "You used to tell customers that [old_description]"

                "However, she has worked hard and grown a lot since then. Now [new_description]"

                $ girl.remove_trait(trait)
                $ add_trait_perkless(girl, newtrait)
                $ girl.neg_fix_counter = 0
                
            return

        "Perhaps some other time":
        
            return
            
    return
    
label freedom_interact(girl):

    $ pic = girl.get_pic("rest", and_tags=["profile"], naked_filter=True, soft=True)

    $ renpy.show(brothel.bedroom_type.get_bg(), at_list = [top]) 
    
    "As you make your rounds through the brothel, you bump into [girl.name] clutching some paperwork."

    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
    with dissolve

    girl.char "Master, can we have a word?"
    
    $ mc_response = rand_choice([_("What is it, ") + girl.name + _("?"), _("Of course, ") + girl.name + _(". Speak your mind."), _("Naturally. Make it quick."), _("What's the matter, ") + girl.name + _("?")])
    $ renpy.say(you, mc_response)

    girl.char "I've been thinking..."

    $ reason_intro = rand_choice([__("The way things are going, I'm really enjoying my life as a slave."), __("Being a slave is so much more fun than I ever thought it would be."), __("I absolutely love working in a brothel like this."), __("I think I could truly make a career out of this profession."), __("Slavery gets a bad rep. It isn't as terrible as they say."), __("Life is much simpler this way, knowing that my Master will take care of me.")])
    $ reason_problem = rand_choice([__("Unfortunately, as a free girl, I tend to recieve special treatment in all the wrong ways. I'll always remain an outcast."), __("But I've realised that the next step on this path can only be taken if you're incentivised to help me reach that next level."), __("To further my career, I must be willing to take bold risks."), __("If life has taught me anything, it's that being a slave can get you places."), __("I'm eager to make my next move. I've thought long and hard about it, and the best course of action is to put you in control of my destiny.")])
    $ reason_solution = rand_choice([__("That's why I've prepared this contract for you. For a lump sum, I would be willing to sign away my freedoms. What do you say?"), __("That's why I've decided to offer myself to you as an official slave. If you're interested in my services, that is."), __("That's why I would like to start negotiations regarding this contract..."), __("That's why... Well, just have a look at this contract!")])
    
    if girl.personality.name == "sweet":

        $ renpy.say(girl.char, reason_intro)

        "But our current agreement is only valid for a limited time... I want to commit the rest of my life to you, so that our time together may never end."

        $ renpy.say(girl.char, reason_solution)    

        "She hands you an official document detailing conditions for transference of ownership."
    
        girl.char "Look, I know I'm already your {i}temporary{/i} slave as it stands... It would just really ease my mind if we could make this permanent! I really want to spend the rest of my life at your side!"
    
    else:
    
        $ renpy.say(girl.char, reason_intro)
        $ renpy.say(girl.char, reason_problem)
        $ renpy.say(girl.char, reason_solution)    

        "She hands you an official document detailing conditions for transference of ownership."

        girl.char "I know I'm already your {i}temporary{/i} slave as it stands... I just really want to continue doing this even after my spell at [brothel.name] ends."
    
    "It seems like she has a very limited understanding about the contents and implications of this contract. She would be enslaved for the rest of her life if she were to sign it."

    $ price_modifier = max(0.6, min(5 , 0.4 + sum([t for o, t in girl.jp.items()]) / 600))
    $ price = int(round(girl.get_price("sell") * random.uniform(0.6, 2.2)*price_modifier,-2))
    $ price_str = str(price)
    $ value_str = str(int(round(girl.get_price("sell")*random.uniform(0.8,1.2),-1)))

    "For a fee of [price_str] gold, she would be willing to sign away her freedoms indefinitely and become your property."

    if price_modifier >= 1.5: 
    
        "It looks like she'll drive a hard bargain. That inflated price tag clearly takes her extensive experience into account."
    
    if MC.playerclass == "Trader":
        
        "You estimate her current market value to be around [value_str] gold."
        
    elif MC.get_alignment() == "evil": 
    
        "You consider what price she could fetch if you were to sell her on immediately after signing this contract..."
        "With a bit more work, she would probably be valued around [value_str] gold at the slavemarket."
        
    elif MC.get_alignment() == "good" or price_modifier <= 1: 
    
        you "Are you sure this is a good idea, [girl.name]? Do you understand what this contract is about?"
        
        girl.char "W-well,  you see... I was talking to one of our customers..."
        
        girl.char "He says there's this establishment near the Magic Gardens where someone with my expertise is highly sought after."

        girl.char "But according to him, they have a policy to only employ girls who have filled in this form... So that's what got me thinking... I probably need this to continue working after my spell at [brothel.name], don't I?"

    "She's clearly in way over her head. This contract would empower you to sell her soul to the highest bidder and keep all the profits to yourself."
    
    "Then again, it wouldn't be the first time you've taken advantage of a girl's naivety for personal gain."
    
    girl.char "W-well? What do you think?"
    
    menu:
    
        "Agree to the terms ([price_str] gold)" if MC.gold >= price:
        
            jump .freedom_end_1

        "Try to haggle her down":
        
            you "I can't agree to that price. Would you be willing to come down a bit?"
        
            $ new_price = int(round(girl.get_price("sell") * random.uniform(0.5, 2.0)*price_modifier,-1))
            
            if new_price < price:
                
                $ price = new_price
                $ price_str = str(price)
                
                girl.char "*pout* You're too good at this... [price_str] gold! That's my final offer!"
            
                menu:
                    
                    "We have a deal ([price_str] gold)" if MC.gold >= price:
                    
                        jump .freedom_end_1
                
                    "Not good enough":
                    
                        you "I appreciate your offer, but I'm afraid it doesn't sufficiently align with my interests. Perhaps some other time."
                        
                        hide screen show_event
                    
            else:       
            
                girl.char "But my original offer is a bargain! *pout* Never mind, then! Perhaps I should sell myself to some other Master who {i}does{/i} appreciate what I bring to the table."
                
                $ girl.change_love(-10)
                $ girl.change_mood(-10)
                
                hide screen show_event
            
                return

        "Refuse her offer":
        
            you "I appreciate your offer, but I'm afraid it doesn't align with my interests. Perhaps some other time."
            
            hide screen show_event
            
            return
                    
    return
            
label .freedom_end_1: #free to slave (on girl's own initiative)

    you "We have a deal. Let me gather the coin so we can sign this contract at once."

    call dialogue(girl, "slave effusive thanks")
    
    $ MC.gold -= price
    $ girl.original_price = price
    $ girl.free = False
    
    "[girl.fullname] has become property of [MC.name]."
    
    hide screen show_event

    return

# label .freedom_end_2: #free to slave (contract forgery)

# label .freedom_end_3: #free to leaving brothel (on girl's own initiative)

# label .freedom_end_4: #free to leaving brothel (kidnapping/human trafficking)

label ext_party(girl):

    $ party_pic = girl.get_pic("party", not_tags=["public", "beach", "nature", "town"], naked_filter=True, soft=True)

    if not party_pic:
        return

    python:

        renpy.show("brothel" + str(brothel.pic_index), at_list = [top])

        party_intro = rand_choice([girl.name + _(" has invited some friends over to visit ") + brothel.name + _("."),girl.name + _(" is throwing a party for her friends."),girl.name + _("'s friends have surprised her with a visit today.")])

        party_personality_comment = {

            "very extravert" : [__("They're a rowdy bunch."), __("Their excited yelps liven up the brothel."), __("They run through the halls of the brothel as if they own the place."), __("They want to hear all about the customers from ") + girl.name + _("."), __("They seem eager to get to know you."), __("They like to compete for each other's attention.")],

            "very introvert" : [__("They don't seem very talkative."),__("It's a timid affair."),__("They listen attentively as ") + girl.name + __(" sums up her day-to-day."),__("They don't seem very interested in a tour around the brothel."),__("They seem very supportive of her."),__("They look happy to be invited."), __("They seem very fond of ") + girl.name + _(".")],

            "very materialist" : [__("They fervently inspect ") + girl.name + __("'s wardrobe."), __("They are particularly interested in her earnings."), __("They exchange makeup tips with one another."), __("They show off their jewelry to one another."), __("They seem keen to impress ") + girl.name + _("."), __("They happily spend time gossiping.")],

            "very idealist" : [__("They talk politics with one another."), __("They seem very polite and well mannered."), __("They really enjoy each other's company."), __("They affectionately greet ") + girl.name + __(" with a hug."), __("They seem very fond of ") + girl.name + _("."), __("One of them has brought lots of sweets. She offers some to the guards.")],

            "very lewd" : [__("They seem excited to be here."),__("They look excited."),__("They're very curious about the brothel."),__("They're fascinated about every aspect of the brothel."), __("They her you to show them all of her sex toys."),__("They listen carefully as ") + girl.name + __(" tells stories about her life in the brothel.")],

            "very modest" : [__("They look appalled."),__("They are shocked by her living conditions."),__("They plead with ") + girl.name + __(" to take the party elsewhere."),__("They don't seem happy to be here."),__("They're a bit overdressed for the occasion."),__("They politely greet you as they pass by.")],

            "very dom" : [__("They feign interest."), __("They're bickering amongst themselves."), __("They don't seem to get along very well."), __("They exude confidence."),__("They seem to feel right at home."),__("They chat up one of the guards."), __("They strike up a conversation with the guards."), __("The mood is timid, as if ") + girl.name + __(" and her friends have just had an argument.")],

            "very sub" : [__("They follow ") + girl.name + __("'s lead as she guides them through the brothel."), __("They enthousiastically sing songs together."), __("Some of them bow for you as they pass."), __("They seem enthralled as ") + girl.name + __(" tells stories about her life here.")],

            }
            
        renpy.show_screen("show_event", party_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
        
        renpy.say("",party_intro + " " + rand_choice(party_personality_comment[rand_choice(gpersonalities[girl.personality.name].attributes)]))
        brothel.change_dirt(girl.rank*3)
        
        party_bonus = ""
        
        if girl.is_("very idealist") and dice(6) <= 4:
            party_bonus += rand_choice([__("One of the visitors hands you a gift to thank ") + brothel.name + __(" for hosting the party.", "Before they leave, ") + girl.name + __("'s friends come up to you to thank you for your part in an unforgettable day.")]) + __(" You receive a bouquet of flowers. ")
            MC.items.append(get_rand_item(item_types = ["Flower"]))

        if girl.is_("very extravert") or dice(6) <= 3:
            party_bonus += rand_choice([__("The girls really enjoy their time in ") + brothel.name + _("."), __("Before long the visitors take their leave. Time flies by when you're having fun."), __("After a while the party comes to an end. ") + girl.name + __("'s friends leave with smiles on their faces.")]) + " "
            brothel.change_rep(girl.rank*2)

        if girl.is_("very introvert") and dice(6) <= 4:
            party_bonus += rand_choice([__("As the party winds down, they take great care to clean up their mess."), __("They do their utmost to clean up after themselves."), __("They make sure to tidy the place up.")]) + " "
            brothel.change_dirt(-girl.rank*2)
            
        renpy.say("",party_bonus)
        renpy.hide_screen("show_event")
        
        if girl.is_("very materialist") and dice(6) >= 4:

            girl_pic = girl.get_pic("casual", and_tags=["happy"], not_tags=["public", "beach", "nature", "town"], naked_filter=True, soft=True)

            if not girl_pic:
                girl_pic = girl.get_pic("dress","profile", and_tags=["happy"], not_tags=["public", "beach", "nature", "town"], naked_filter=True, soft=True)

            renpy.show_screen("show_event", girl_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

            party_bonus_gold = max(40 + dice(60), int(round(girl.rank * random.uniform(20.0, 100.0))))
            party_bonus = rand_choice([__("After her friends are gone, ") + girl.name + __(" comes up to you to share some of the spoils.", "When the visitors have come and gone, ") + girl.name + __(" approaches you with a gift.")])
            party_bonus_comment = rand_choice([__("I'm sorry if we've made a bit of a mess. We all chipped in some gold to show our appreciation towards ") + brothel.name + _("."), __("I charged the girls a fee to enter ") + brothel.name + __(". It's only right that you should recieve most of that."), __("I'm sorry, Master. Perhaps I should have asked for your permission first. I hope you can forgive me.")])
            renpy.say("",party_bonus + _(" She hands you ") + str(party_bonus_gold) + _(" gold."))
            renpy.play(s_gold, "sound")
            MC.gold += party_bonus_gold
            renpy.say(girl.char,party_bonus_comment)
            
            renpy.hide_screen("show_event")
            
    return
    
label ext_holiday_newyear:

    scene black with fade
    show expression bg_bro at top with dissolve
    
    "Today marks the beginning of a {b}{color=[c_orange]}new year{/color}{/b}. People all over Xeros busy themselves exchanging friendly greetings with one another. {i}You're not expecting many customers tonight.{/i}"
    $ MC.add_effects(Effect("change", "customers", -4, scope="brothel", scales_with="district"), expires = calendar.time + 1)
    
    python:
        for girl in MC.girls:
            if girl.love >= girl.fear + 10:
                # call dialogue(girl, "holiday new year")
                girl.say("holiday new year")
    
    return

label ext_holiday_valentines:

    scene black with fade
    show expression bg_bro at top with dissolve

    "It's {b}{color=[c_orange]}Valentine's Day{/color}{/b}, a celebration of romance and love. Gestures of affection are especially effective today."
    "Lovestruck people of Xeros take this opportunity to openly profess their adoration to the ones they love."

    $ MC.add_effects(Effect("boost", "love gains", 2, scope="world"), expires = calendar.time + 1)
    
    python:
        for girl in MC.girls:
            if girl.love >= 50 and girl.love >= girl.fear + 50:
                holiday_pic = girl.get_pic("kiss", "date", naked_filter=True, soft=True)
                if not holiday_pic:
                    holiday_pic = girl.get_pic("profile", and_tags="happy", naked_filter=True, soft=True)

                approach = [girl.name + __(" rushes towards you with flushed red cheeks."),__("You notice ") + girl.name + __(" rushing towards you."),girl.name + __(" wishes to speak to you."), __("You're stopped by ") + girl.name + __(", who wants to talk to you."), __("You're held up by ") + girl.name + __(", who has something on her mind."), girl.name + __(" tugs on your arm, eager to say something."), __("You run into ") + girl.name + __(", who candidly speaks her mind."), __("You hear ") + girl.name + __(" shouting your name as she runs up to you."), __("You hear ") + girl.name + __(" calling for you, eager to express what's on her mind."), __("You're surprised by ") + girl.name + __(", who urgently wishes to speak with you.")]
                
                renpy.say("",rand_choice(approach))
                
                renpy.show_screen("show_event", holiday_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                girl.say("slave love")
                renpy.hide_screen("show_event")
                holiday_pic = None
                continue
                
                # show screen show_event(holiday_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                # with dissolve
                # call dialogue(girl, "slave love")
                # hide screen show_event
            
    return

label ext_holiday_salvation:

    scene black with fade
    show expression bg_bro at top with dissolve

    "Today marks the {b}{color=[c_orange]}Day of Salvation{/color}{/b}. The church of Arios celebrates the kindling of Arios, the god of Light."
    "Followers of Arios traditionally light a candle in their homes on this day. The most devout among them then carry that candle to the Cathedra to recieve Arios' blessings."

    if MC.god == "Arios":
        "You order your girls to kneel and pray as you light a candle for each of them. You then instruct them to carry their candles to the Cathedra."
        $ MC.good += 3
        $ MC.add_effects(Effect("boost", "all jp gains", 1.0, scope="brothel"), expires = calendar.time + 1)
        $ MC.add_effects(Effect("boost", "energy use", 0.25, scope="brothel"), expires = calendar.time + 1)
    elif MC.god == "Shalia":
        "As a follower of Shalia, you despise today's celebrations. You order your girls snuff out any candle they come across. {i}This slightly increase your brothel's threat build up.{/i}"
        $ MC.evil += 3
        $ MC.add_effects(Effect("boost", "threat build up", 0.5, scope="brothel"), expires = calendar.time + 1)
    else:
        "Although you do not follow the teachings of Arios, you decide to light a candle regardless for tradition's sake."
        $ MC.good += 1
        $ MC.add_effects(Effect("boost", "all jp gains", 0.25, scope="brothel"), expires = calendar.time + 1)

    python:

        for girl in MC.girls:

            celebrates = False
            
            if girl.is_("very modest") and girl.fear < 25:
                celebrates = True
                holiday_pic = girl.get_pic("nun", naked_filter=True, soft=True)
                if not holiday_pic:
                    holiday_pic = girl.get_pic("bride", naked_filter=True, soft=True)

            elif girl.is_("very idealist") and girl.fear < 0 and dice(6) >= 3:
                celebrates = True
                holiday_pic = girl.get_pic("bride", naked_filter=True, soft=True)
                if not holiday_pic:
                    holiday_pic = girl.get_pic("nun", naked_filter=True, soft=True)
                    
            elif girl.fear < -25 and dice(6) >= 4:
                celebrates = True
                holiday_pic = girl.get_pic("bride", naked_filter=True, soft=True)
                if not holiday_pic:
                    holiday_pic = girl.get_pic("nun", naked_filter=True, soft=True)
                   
            if celebrates == True:
            
                if MC.god == "Shalia":

                    if girl.is_("very modest"):
                        girl.fear += 5

                    if not holiday_pic:
                        girl.say("holiday salvation evil")
                    else:
                        renpy.show_screen("show_event", holiday_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                        girl.say("holiday salvation evil")
                        renpy.hide_screen("show_event")
                        holiday_pic = None
                        
                else:

                    if girl.is_("very modest"):
                        girl.fear -= 5

                    if not holiday_pic:
                        girl.say("holiday salvation")
                    else:
                        renpy.show_screen("show_event", holiday_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                        girl.say("holiday salvation")
                        renpy.hide_screen("show_event")
                        holiday_pic = None
                    
   
    return
    
label ext_holiday_ascension:

    scene black with fade
    show expression bg_bro at top with dissolve

    "Today the people of Xeros celebrate {b}{color=[c_orange]}Ascension{/color}{/b}."
    "The church of Arios encourages the masses to see people in a different light, preaching kindness and compassion towards strangers. Shalia worshippers take this opportunity to swindle and deceive those who have fallen for the church's message."
    "{i}Some free girls in the city of Zan may have become more interested in you thanks to today's festivities.{/i}"
    
    python:
    
        for girl in game.free_girls:

            if dice(6) >= 5:
                girl.love += 20

    return
    
label ext_holiday_summer:

    # if calendar.month == 6 and calendar.day == 21: # holiday: Summer Festival [ALL]

    return
    
label ext_holiday_sin:
    
    # if calendar.month == 9 and calendar.day == 11: # holiday: Festival of Sin (Shalia-holiday)

    return
    
label ext_holiday_night:
    
    scene black with fade
    show expression bg_bro at top with dissolve

    "Tonight followers of Shalia celebrate Her descent into darkness during the {b}{color=[c_orange]}Night of Nights{/color}{/b}."
    "Worshippers of Shalia are encouraged to carry out plots against non-believers. {i}Fear gains receive a significant boost on this day{/i}."

    $ MC.add_effects(Effect("boost", "fear gains", 2, scope="world"), expires = calendar.time + 1)

    if MC.god == "Arios":
        "As you worship Arios, {i}threats to your brothel will build up much faster{/i} on this day."
        $ MC.add_effects(Effect("boost", "threat build up", 3, scope="brothel"), expires = calendar.time + 1)
    elif not MC.god:
        "As you do not worship Shalia, {i}threats to your brothel will build up faster{/i} on this day."
        $ MC.add_effects(Effect("boost", "threat build up", 1, scope="brothel"), expires = calendar.time + 1)
        
    $ girl = rand_choice(MC.girls)
    $ girl.say("slave defense")
    
    return
    
label ext_holiday_fertility:

    # if calendar.month == 11 and calendar.day == 25: # holiday: Feast of Fertility 

    return

label ext_holiday_hmas: # Winter Solstice, hmas eve

    scene black with fade
    show expression bg_bro at top with dissolve
    
    "On this day Xeros experiences the winter solstice, a day with the shortest period of daylight."
    "Followers of Shalia rejoice as they experience the longest night of the year. Arios worshippers take solace in the thought that from here on, the days become longer as the Light of Arios burns brightly once more."
    "{i}Customers will pay a premium to get served tonight.{/i} Tomorrow families will unite to celebrate {b}{color=[c_orange]}Hmas{/color}{/b} together. Have you been naughty or nice?"

    $ MC.add_effects(Effect("boost", "income", 0.25, scope="brothel"), expires = calendar.time + 1)

    python:
        for girl in MC.girls:
            if girl.fear <= 0:
                holiday_pic = girl.get_pic("santa", naked_filter=True, soft=True)
                if not holiday_pic:
                    girl.say("holiday hmas")
                else:
                    renpy.show_screen("show_event", holiday_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                    girl.say("holiday hmas")
                    renpy.hide_screen("show_event")
                    holiday_pic = None

    return

label ext_birthday(girl): # girl's birthday

    if girl in MC.girls:
        pass
    else:
        return

    scene black with fade
    show expression bg_bro at top with dissolve

    python:
        renpy.say("",_("It's {b}{color=[c_orange]}") + girl.name + _("'s birthday{/color}{/b} today. {i}Love and fear can be influenced much more effectively on a girl's birthday.{/i}"))
        girl.add_effects(Effect("boost", "love gains", 2), expires = calendar.time + 1)
        girl.add_effects(Effect("boost", "fear gains", 2), expires = calendar.time + 1)
    
        i = 0
        girl_list = MC.girls.copy()
        random.shuffle(girl_list)

        for othergirl in girl_list:
            if len(MC.girls) > 8 and dice(len(MC.girls)) > 6:
                continue
            if othergirl in girl.rivals or othergirl == girl:
                continue
            else:
                i += 1
                othergirl.say("slave congrats")
            
            if i >= 3:
                break
                
        if i >= 2:
            girl.say("slave birthday")

        girl.birthday_celebrated = False
            
    return


# label extended_events:

    # python:
    
        # ## EXT Location

        # if girl.extended_tags["beach"] == True: # Schedule event at (Location) beach [ALL, Porter]

        # if girl.extended_tags["nature"] == True: # Schedule event at (Location) nature [ALL, Porter]

        # if girl.extended_tags["town"] == True: # Schedule event at (Location) town [ALL, Porter]
        
        # if girl.extended_tags["date"] == True and girl.extended_tags["beach"] == True: # date at (Location) [ALL]
        
        # if girl.extended_tags["date"] == True and girl.extended_tags["nature"] == True: # date at (Location) [ALL]
        
        # if girl.extended_tags["date"] == True and girl.extended_tags["town"] == True: # date at (Location) [ALL]

        # ## EXT Social

        # if girl.extended_tags["ceremony"] == True: # ceremony [Caster, ...]

        #OK# if girl.extended_tags["study"] == True: # study [Genius, Fast learner, Mentor, ]

        #OK# if girl.extended_tags["party"] == True: # party [very extravert]

        # if girl.extended_tags["friend"] == True: # friend [ALL]
        
        # ## EXT Jobs

        # if girl.job == "Waitress":
        
            # if girl.extended_tags["apron"] == True: # apron [Waitress, ...]

        # if girl.job == "Dancer" or girl.has_trait("Idol"):
        
            # # sing [Dancer, Idol, ...]

        # if girl.job == "Masseuse":

            # if girl.extended_tags["nurse"] == True: # nurse [Masseuse, Nurse]

        # if girl.job == "Geisha":

            # if girl.extended_tags["kimono"] == True: # kimono [Geisha, very modest]

            # if girl.extended_tags["china"] == True: # china [Geisha, ...]

            # if girl.extended_tags["miko"] == True: # miko [Geisha, ...]
        
        # if girl.job == "Whore" or girl.is_("very lewd"):

            # if girl.extended_tags["hooker"] == True: # hooker [Whore, very lewd, Hustler, ]
            
        # ## EXT Holidays

        #OK# if calendar.year >= 2 and calendar.month == 1 and calendar.day == 1: #holiday: new year

        #OK# if girl.extended_tags["date"] == True and calendar.month == 2 and calendar day == 14: # holiday: Valentine's

        #OK# if calendar.month == 4 and calendar day == 7: #holiday: Day of Salvation (Arios-holiday)

        #OK# if calendar.month == 5 and calendar day == 19: # holiday: Ascension-day (Arios) [ALL]

        # if calendar.month == 6 and calendar day == 21: # holiday: Summer Festival [ALL]

        # if calendar.month == 9 and calendar day == 11: # holiday: Festival of Sin (Shalia-holiday)
        
            # if girl.extended_tags["blindfold"] == True: # blindfold [???]

            # if girl.extended_tags["collar"] == True: # collar [???]

        # if calendar.month == 10 and calendar day == 28: # holiday: Night of Nights (Shalia-holiday)
        
            # if girl.extended_tags["blindfold"] == True: # blindfold [???]

            # if girl.extended_tags["collar"] == True: # collar [???]
            
        # if calendar.month == 11 and calendar day == 25: # holiday: Feast of Fertility 

        #OK# if girl.extended_tags["santa"] == True and calendar.month == 12 and calendar day == 24: # holiday: Winter Solstice [ALL]
        
        # ## EXT ...
        
        # if girl.extended_tags["casual"] == True: # casual [ALL, Country girl]

        # if girl.extended_tags["dress"] == True: # dress [ALL, Provocative, Fashionista, Noble, Elite]

        # ## EXT Diseases

        # if girl.extended_tags["futanari"] == True: # semi-magical parasitic disease [ALL]

        # if girl.extended_tags["pregnant"] == True: # semi-magical parasitic disease [ALL]

        # if girl.extended_tags["tempt"] == True: # tempt [ALL]

        # ## EXT ...

        # if girl.extended_tags["lingerie"] == True: # lingerie [ALL, Provocative, Fashionista, ]

        # if girl.extended_tags["panties"] == True: # panties [ALL]