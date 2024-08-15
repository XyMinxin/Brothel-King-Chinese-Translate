####            FUNCTIONS FOR B KING            ####################################################
##  Those are the functions used with the game.   ##################################################
##       Classes are in a separate file.          ##################################################
##                                                ##################################################

python early:

    import os
    import sys
    import random
    import math
    from math import prod
    import copy
    import configparser
    import ast
    from collections import defaultdict
    import operator
    from fractions import Fraction
    from collections import OrderedDict
    import threading
    import re
    import time

    import gc #! Doesn't seem to solve the problem with saved games size


init -3 python:

## Resolution functions
# Converts size from base game resolution to custom resolution
# Values are stored in a dictionary for faster access

    def xres(_size=None): # Some custom resolutions may work better with a different xy ratio
        if _size is None:
            return config.screen_width
        try:
            return res_dict["x", _size]
        except:
            res_dict["x", _size] = int(_size*config.screen_width*res_xy_ratio/RES_BASE_X)
            return res_dict["x", _size]

    def yres(_size=None):
        if _size is None:
            return config.screen_height
        try:
            return res_dict["y", _size]
        except:
            res_dict["y", _size] = int(_size*config.screen_height/RES_BASE_Y)
            return res_dict["y", _size]

    def res_font(_size):
        return yres(_size)

    def res_tb(_size): # Always returns square dimensions. This function returns a tuple - unpack it with * if needed
        return (yres(_size),)*2

#<Chris12 PredictImages>
    # Threading is necessary, because otherwise the screen only shows AFTER ALL images have been loaded.
    # That would actually make things slower. With threading, the images load in the background as intended.
    # This function seems to work only if called from BKscreens. Probably got something to do with interactions. Maybe I'm just misunderstanding, though.
    def predict_images(girls, predict_portraits = True, predict_profiles = True):
        def predict_images_helper():
            try:
                # Predict all portraits first since they are needed immediately.
                for girl in girls:
                    if predict_portraits and girl.portrait is not None : renpy.predict(girl.portrait.get(side=True))

                # After that, begin loading the profile images
                for girl in girls:
                    if predict_profiles and girl.profile is not None : renpy.predict(girl.profile.get(profile=True))
            except: pass
        if girls is not None and len(girls) > 0:
            t = threading.Thread(target=predict_images_helper)
            t.daemon = True
            t.start()

    def fast_portrait(path, x, y):
        for pic in GirlFilesDict.get_pics(path):
            if pic.has_tag("portrait") and not pic.has_tag("naked"):
                return pic.get(x, y)
        for pic in GirlFilesDict.get_pics(path):
            if pic.has_tag("portrait"):
                return pic.get(x, y)
        for pic in GirlFilesDict.get_pics(path):
            if pic.has_tag("profile"):
                return pic.get(x, y)
        return Picture(path="backgrounds/not_found.webp").get(x, y)

    def predict_next_img(event_queues): # use renpy.predict() to cache image(s) from current first event of first non-empty queue

        # Including DougTheC's fix #

        for queue in event_queues :
            if queue and isinstance(queue[0], Event):
                if queue[0].pic is not None:
                    if isinstance(queue[0].pic, Picture):
                        renpy.predict(queue[0].pic.get(res_event_width, res_event_height))
                    else:
                        renpy.predict(queue[0].pic)    # image may be described by unicode string, especially for farm
                if queue[0].background is not None:
                    if isinstance(queue[0].background, Picture):
                        renpy.predict(queue[0].background.get(res_event_width, res_event_height))
                    else:
                        renpy.predict(queue[0].background)    # image may be described by unicode string, especially for farm

                break

#</Chris12 PredictImages>


    def get_girl_path(file): # Returns girlpack name (the folder name), girlpack_path, file_name - Or None, None, None if the file is not a valid girl pack picture

        if is_imgfile(file) or file.endswith("_BK.ini"):
            for gdir in girl_directories:
                if file.startswith(gdir):

                    if gdir.endswith("/"):
                        gdir_len = len(gdir.split("/")) - 1 # The split actually includes an empty string at the end so len is 1 higher than expected
                    else:
                        gdir_len = len(gdir.split("/"))

                    file_parts = file.split("/")

                    if len(file_parts) > gdir_len + 1: # Skips files inside the root 'girls' directory to avoid problems
                        girlpack_name = ""
                        mix_name = ""
                        mix_list = []

                        for part in file_parts[gdir_len:-1]:
                            if part.startswith("_"): # Folders starting with an underscore will be completely ignored (such as a story pics-only directory)
                                return None, None, None

                            elif part.startswith("#"): # Folders starting with '#' will be identified as 'container folders' and a new mix will be created
                                if girlpack_name: # containers will be ignored if inside a girl pack (likely a mistake)
                                    return None, None, None
                                mix_name += part + " "
                                mix_list.append(mix_name)

                            else: # the first 'normal' folder will become the girlpack name
                                if not girlpack_name:
                                    girlpack_name = part
                                    girlpack_path = "/".join(file_parts[:file_parts.index(part)+1])

                        if not girlpack_name:
                            return None, None, None


                        # Creates mixes automatically

                        if mix_list:
                            for mix_name in mix_list:
                                if mix_name in persistent.girl_mix.keys():
                                    if girlpack_name not in persistent.girl_mix[mix_name]:
                                        persistent.girl_mix[mix_name].append(girlpack_name)
                                else:
                                    persistent.girl_mix[mix_name] = [girlpack_name]

                        return girlpack_name, girlpack_path, file_parts[-1]

        return None, None, None


    # def list_girl_packs(): # Returns a list of girl pack names. Used for CG gallery
    #
    #     pack_dir = {}
    #
    #     for file in renpy.list_files():
    #         girlpack_name, girlpack_path, file_name = get_girl_path(file)
    #         if girlpack_name: # Because get_girl_path can return None values
    #             if not pack_dir[girlpack_name]:
    #                 pack_dir[girlpack_name] = girlpack_path
    #
    #             elif pack_dir[girlpack_name] != girlpack_path: # Detects if a girlpack folder was found in two different locations for error handling.
    #                 raise AssertionError("Two girl packs with the name '%s' were found:\n%s\n%s\nRename one to avoid conflicts." % (girlpack_name, pack_dir[girlpack_name], girlpack_path))
    #                 renpy.say("", "Exiting Ren'Py...{w=1}{nw}")
    #                 renpy.quit()
    #
    #             if (girlpack_name, girlpack_path) not in pack_dir.items():
    #                 pack_dir[girlpack_name] = girlpack_path
    #
    #     return pack_dir

    def get_selected_girlpacks(mix_list): # Avoids duplicating girl packs if several mixes are selected with the exact same packs
        girlpacks = []

        for mix in mix_list:
            girlpacks += [gp for gp in persistent.girl_mix[mix] if gp not in girlpacks]

        return girlpacks

    def change_template(girl): # Used for debugging saved games that have different girl packs
        new_girl_pack = rand_choice(get_selected_girlpacks(game.mixes))
        girl.pack_name = new_girl_pack
        girl.path = new_girl_pack
        girl.load_ini()
        girl.generate_personality()
        girl.generate_background()
        girl.refresh_pictures()
        girl.create_char()

    def generate_girls():
        #<Chris12 PackState>
        global read_ini_log
        read_ini_log = ""

        # Use the new GirlFilesDict when generating new girls
        glist = list()

        ## CHECKING ACTIVE GAME MIXES ##

        available_girlpacks = get_selected_girlpacks(game.mixes)

        ## TAKING NAMES ##

        for girlpack_name in available_girlpacks:
            newGirl = Girl()
            newGirl.pack_name = girlpack_name
            newGirl.path = girlpack_name
            glist.append(newGirl)
        #</Chris12 PackState>

        ## SHOWING BUTTS ##

        for girl in glist:
            girl.load_ini()

        if not glist:
            renpy.say("", event_color["bad"] % "游戏无法在当前的女孩组合中找到一个女孩包." + "\n你已经下载并安装了女孩包了吗?\n访问[URL]以获得你的第一个女孩包.")
#            raise AssertionError("No girls found! Did you download a girl pack?")
            renpy.say("", "退出Ren'Py...{w=1}{nw}")
            renpy.quit()

        return glist

    def create_girl(pack_name, free=False, force_original=False, level=1, personality=None): # Create a single girl from pack_name (must be a valid pack name)
        girl = Girl()
        girl.pack_name = pack_name
        girl.path = pack_name
        girl.load_ini()
        girl.id = game.girl_id_generated
        game.girl_id_generated += 1
        girl.randomize(free=free, force_original=force_original, level=level, personality=personality)

        return girl

    def get_name(dir, full=False):

        """ Breaks down a dir name into a first name/last name """

        ## Only works with formats like "name", "name surname" or "name_surname". The "_" operator takes precedence over " ",
        ## which could be useful for composed first names

        dir_parts = dir.split("/")

        if not dir_parts[-1]: # split will sometimes return an empty string at the end
            dir_parts = dir_parts[:-1]

        dir = dir_parts[-1]

        if dir.count("_") == 1:
            char = dir.find("_")

            first_name = dir[:char]
            last_name = dir[char+1:]

        elif dir.count(" ") >= 1:
            char = dir.find(" ")

            first_name = dir[:char]
            last_name = dir[char+1:]

        else:
            first_name = dir
            last_name = ""

        if full:
            return first_name + " " + last_name

        else:
            return first_name, last_name

    def get_girls(nb, free=False, p_traits=None, n_trait=None, perks=None, level_range=None, prefer_original = prefer_original_girls): # This will return a list of new girls, if possible using different templates and checking for duplicates

        # If level_range is provided as a tupple of integers (min, max), girls will generate at a random level in range
        # Never set level range below 1 or above 25 to avoid problems

        # prefer_original prioritizes the creation of original girls. They will take the top spots in glist. The game will fall back to non-original if necessary

        t1 = time.perf_counter()

        if p_traits == None: p_traits = []
        if perks == None: perks = []

        template_girls = [g for g in generate_girls() if can_generate(g, free)] # Must be separate from available_templates to avoid creating new girl objects with every loop

        t2 = time.perf_counter()

        available_templates = []
        glist = []
        final_list = []

        while len(glist) < nb:
            if available_templates == []:
                available_templates = list(template_girls) # list() is necessary to make a true copy of template_girls
                renpy.random.shuffle(available_templates) # places girl templates in random order

            # First looks for girls that haven't been generated at all

            for girl in available_templates:
                if girl not in glist and girl.count_occurences("all") == 0:
                    glist.append(girl)
                    available_templates.remove(girl) # removing within the for loop is okay because of 'break'
                    if girl.init_dict["cloning options/unique"]: # Removes unique girls from the template pool if they are unique
                        template_girls.remove(girl)
                    break
            else: # 'for' loop failed
                # Next looks for girls that aren't owned by player and have less than 3 occurences elsewhere

                available_templates = [g for g in available_templates if not g.init_dict["cloning options/unique"]] # This clears unique girls from the list (shouldn't be needed)

                if not available_templates:
                    raise AssertionError("没有足够的女孩模板可用-检查你的女孩包配置(全部设置为'unique'?)")

                for girl in available_templates:
                    if girl not in glist and girl.count_occurences("player") == 0 and girl.count_occurences("all") <= 3:
                        glist.append(girl)
                        available_templates.remove(girl) # removing within the for loop is okay because of 'break'
                        break

                # Finally, looks for girls with the least occurences anywhere

                else:
                    if not available_templates:
                        raise AssertionError("没有足够的女孩模板可用-检查你的女孩包配置")

                    found = False
                    i = 1
                    while not found:
                        i += 1

                        if i > 250:
                            raise AssertionError("追踪重复项时出错-检测到可能的无限循环")

                        for girl in available_templates:
                            if girl.count_occurences("all") < i:
                                glist.append(girl)
                                available_templates.remove(girl) # removing within the for loop is okay because of 'break'
                                found = True
                                break

        t3 = time.perf_counter()

        for template in glist:
            girl = copy.deepcopy(template)
            girl.id = game.girl_id_generated
            game.girl_id_generated += 1

            if level_range:
                lvl = renpy.random.randint(level_range[0], level_range[1])

            else: # Will pick a randomized level based on chapter
                lvl = randomize_girl_level()

            # <Chris12 - prefer_original>
            girl.randomize(free=free, p_traits=p_traits, n_trait=n_trait, perks=perks, level=lvl, force_original=(prefer_original and g.count_occurences("all", original=True) == 0))
            # </Chris12 - prefer_original>

            final_list.append(girl)

            if girl.init_dict["background story/init_function"]:
                try:
                    globals()[girl.init_dict["background story/init_function"]](girl)
                except:
                    raise AssertionError("Function " + girl.init_dict["background story/init_function"] + " 在 " + girl.path + "/_BK.ini 不存在或失败.")

        t4 = time.perf_counter()

        try:
            game.func_time_log += "\ntotal time: %s" % (t4 - t1)
        except:
            pass

        return final_list



### RANDOM AND NUMBERS FUNCTIONS ###

    def dice(sides, number = 1):
        """Randomly generates a number of dices with a result from 1 to sides"""

        return sum(renpy.random.randint(1, sides) for i in range(number))


    def rand_choice(li, nb = None): # returns False for an empty list or invalid nb

        li = list(li)

        if li:
            if nb == None: # Returns a single object if nb is None (default value)
                return renpy.random.choice(li)
            elif nb > 0: # Returns a list if nb is provided. May return less than the number of items requested if len(li) < nb
                try:
                    return renpy.random.sample(li, k=int(nb))
                except:
                    return li

        return False


    def weighted_choice(li, nb=None, duplicates=False): # Where li is a list of tuples with item, weight, and nb is the number of choices drawn

        # Returns a single item according to a random weighted choice if nb is not provided
        # Returns several items as part of a list if nb is provided
        # Returns False or an empty list if no choices are available

        r = []

        if nb:
            choice_nb = nb
        else:
            choice_nb = 1

        if li:
            if len(li) <= choice_nb and not duplicates: # Returns the whole choice list if duplicates is inactive and the number of choices is equal or in excess of choice list length, to avoid infinite loops
                r = [x for x, w in li]

            else:
                copy_list = [(x, w) for x, w in li]
                weightsum = sum(w for x, w in copy_list)

                # Main loop

                while len(r) < choice_nb:

                    rand = renpy.random.random() * weightsum # Random returns a number between 0.0 and 1.0

                    currentWeight = 0

                    for x, w in copy_list:
                        currentWeight += w
                        if currentWeight >= rand :
                            r.append(x)
                            break

                    else : # Just to be safe against potential rounding problems
                        x, w = copy_list[-1]
                        r.append(x)

                    if not duplicates:
                        copy_list = [(x, w) for x, w in copy_list if x not in r]
                        weightsum = sum(w for x, w in copy_list)

        if nb == None:
            if len(r) >= 1: # Checks both the intended number and the result list before returning a single item
                return r[0]
            else:
                return False # Returns False if no list was provided
        else:
            return r

    def round_int(x): # Rounds to the nearest decimal number (remember to force a float when dividing two integers, python is a dick about that)

        x = float(x)

        return int(round(x))

    def str_int(x): # Returns a string of an integer
        return str(round_int(x))

    def str_dec(nb, decimals=2): # Returns a string of either an integer or a float, depending on the nb of decimals available
        return ((("%." + str(decimals) + "f") % nb).rstrip("0")).rstrip("。")

    def round_down(x): # Home-made version of math.floor
        return int(x)

    def round_up(x): # Home-made version of math.ceil
        if int(x) < x:
            return int(x) + 1
        else:
            return int(x)

    def round_best(x, decimals=1):

        for d in range(decimals):
            if not (x * 10 ** (d)) % 1:
                if d == 0:
                    return int(x)
                else:
                    return round(x, d)

        return round(x, decimals)


    def mean(values, integer=False): # Can be fed a generator as well
        n = 0
        s = 0
        for v in values:
            s += v
            n += 1

        r = float(s) / n # Without float, this would round down to an integer when all values are integers

        if not integer:
            return r
        else:
            return round_int(r)


    def mean_int(values):
        return mean(values, True)

    def update_slaves():

        nb = dice(6)+5

        slavemarket.girls = [] # Empties slavemarket to get another chance at generating an original girl
        slavemarket.girls = get_girls(nb)

        for girl in slavemarket.girls: girl.refresh_pictures()

        slavemarket.updated = True

        return


    def update_free_girls(): # Generates a list of girls that will cycle around the city. Note: Girls restricted to a location may not be visible

        # Removes girls that haven't been talked to for 8 weeks
        # Randomly removes girls that haven't been met by the player on a roll of 1 on a d4

        game.free_girls = [girl for girl in game.free_girls if (not girl.MC_interact and dice(4) > 1) or (girl.MC_interact and girl.talked_to_date >= calendar.time - 56)]

        # game.free_girls = [girl for girl in game.free_girls if (girl.talked_to_date and girl.talked_to_date >= calendar.time - 56) or not girl.talked_to_date]
        #
        # game.free_girls = [girl for girl in game.free_girls if girl.MC_interact or (dice(6) > 1)]

        # Adds new girls as necessary to fill up the city streets
        if district.rank == 1:
            nb = free_girls_per_district

        elif district.rank == 2:
            nb = free_girls_per_district * 3

        elif district.rank == 3:
            nb = free_girls_per_district * 5

        else:
            nb = free_girls_per_district * 6

        if len(game.free_girls) < nb:
            game.free_girls += get_girls(nb - len(game.free_girls), free=True)

        return


    def refresh_available_locations():

        """ This creates 3 free girl slots for every location available to the player """

        game.location_slots = []

        loc_list = game.get_available_locations()

        for loc in loc_list:
            game.location_slots += [loc.name]*3

    def reset_girl_jobs():

        for girl in MC.girls and farm.girls:
            if girl.job in all_jobs:
                if not brothel.can_have(girl.job):
                    girl.set_job(None)

        return


    def cycle_free_girls():

        renpy.random.shuffle(game.free_girls)
        renpy.random.shuffle(game.location_slots)

        for loc in game.get_available_locations():
            loc.girls = []

        available_girls = list(game.free_girls) # copy of game.free_girls

        for slot in game.location_slots: # Reminder: game.location_slots contains location names (strings)
            for girl in available_girls:
                 # Girls that have interacted with MC will cycle unless move_after_meeting is set to False
                if (girl.MC_interact and girl.init_dict["background story/move_after_meeting"]) or can_generate(girl, free=True, location=location_dict[slot]):
                    girl.location = slot
                    location_dict[slot].girls.append(girl)
                    available_girls.remove(girl) # This is okay because of break
                    break

        return

    def update_market():
        calendar.discounted = []
        calendar.scarce = []

        d = dice(100)

        if d >= 98: # Everything is cheap this week
            calendar.discounted = build_resources
        elif d >= 95:
            calendar.discounted = ["marble", "ore", "silk"]
        elif d >= 91:
            calendar.discounted = ["wood", "leather", "dye"]
        elif d <= 2: # Everything is expensive
            calendar.scarce = build_resources
        elif d <= 5:
            calendar.scarce = ["marble", "ore", "silk"]
        elif d <= 9:
            calendar.scarce = ["wood", "leather", "dye"]
        else:
            calendar.discounted = [rand_choice(build_resources)]
            calendar.scarce = [rand_choice(build_resources)]

            if calendar.discounted == calendar.scarce:
                calendar.discounted = []
                calendar.scarce = []

        return


    def update_shops():

        # Item shop

        shop.restock(once_a_day=False)

#         shop.items = []

#         shop_mix = [
#             ("junk", dice(3)+3),
#             ("common", dice(6)),
#             ("rare", dice(3)),
#             ("exceptional", dice(3)-2)
#             ]

#         for quality, number in shop_mix:
#             for i in range(number):
#                 it = get_rand_item(quality)
#                 if it:
#                     shop.items.append(it)

#         shop.items.sort(key=lambda x: x.price)

#         shop.updated = True

        # City merchants

        for merc in city_merchants:
            merc.restock(once_a_day=False)

#             merc.items = []

#             shop_mix = [
#             ("junk", dice(6)),
#             ("common", dice(6)+2),
#             ("rare", dice(3)+1),
#             ("exceptional", dice(3)-1)
#             ]

#             for quality, number in shop_mix:
#                 for i in range(number):
#                     it = get_rand_item(quality, item_types=merc.item_types)
#                     if it:
#                         merc.items.append(it)
#                     elif quality != "junk": # Avoids incomplete inventory if all available items are junk
#                         it = get_rand_item("junk", item_types=merc.item_types)
#                         if it:
#                             merc.items.append(it)

#                 merc.items.sort(key=lambda x: x.price)

#                 merc.updated = True

        # Minion merchants

        for merc in minion_merchants:
                merc.restock(once_a_day=False)

#        for merc in (stallion_merchant, beast_merchant, monster_merchant, machine_merchant):

#         NPC_stella.items = get_rand_minion("stallion", nb=dice(5))
#         NPC_goldie.items = get_rand_minion("beast", nb=dice(5))
#         NPC_willow.items = get_rand_minion("monster", nb=dice(5))
#         NPC_gina.items = get_rand_minion("machine", nb=dice(3))

#         for i in range(dice(4)-1):
#             NPC_stella.items.append(get_rand_item(rank="M"))
#             NPC_goldie.items.append(get_rand_item(rank="M"))
#             NPC_willow.items.append(get_rand_item(rank="M"))
#             NPC_gina.items.append(get_rand_item(rank="M"))

#         if NPC_gina.flags["extractor1 unlock"]:
#             if dice(6) >= 4:
#                 NPC_gina.items.append(extractor_items["extractor1"])

#         if NPC_gina.flags["extractor2 unlock"]:
#             if dice(6) >= 5:
#                 NPC_gina.items.append(extractor_items["extractor2"])

        return

    def get_rand_minion(type, nb):

        minions = []

        for i in range(nb):
            level = dice(district.rank) - 1
            minions.append(Minion(type, level))

        return minions

    def generate_template_items(items):

        #Generate variable quality items

        new_items = []

        for it in items:

            for i in range(0,7):

                if it.min_rank <= i <= it.max_rank:

                    new_it = it.generate_new_item(i)

                    new_items.append(new_it)

        return new_items


    def init_items():

        # Creates a ranked dictionary for all items

        game.items = defaultdict(list)

        for it in all_items:

            game.items[it.rarity].append(it)

            for dis in list(district_dict.values()) + [endless_district]:
                if it.min_rank <= dis.rank <= it.max_rank:
                    if it.rarity in ("U", "S", "M"):
                        pass
                    elif it.rarity == "F":
#                         dis.items["rare"].append(it)
                        dis.items["F"].append(it)
                    elif it.rarity < dis.rank:
                        dis.items["junk"].append(it)
                    elif it.rarity == dis.rank:
                        dis.items["common"].append(it)
                    elif it.rarity == dis.rank + 1:
                        dis.items["rare"].append(it)
                    else:
                        dis.items["exceptional"].append(it)

#        list_district_items()

    def list_district_items():
        tlist = []

        for dis in district_dict.values() + [endless_district]:
            for qual in ("junk", "common", "rare", "exceptional"):
                tlist.append([dis.name + " " + qual, and_text([say_name(it) for it in dis.items[qual]])])

        while tlist:
            name, itlist = tlist.pop(0)
            renpy.say(name, itlist)


    def say_name(it):
        if it:
            return it.name
        else:
            return "None"


#    def list_items(rank = 1):

#        district.items = defaultdict(list)

#        district.items["junk"] += game.items[rank - 1]
#        district.items["common"] += game.items[rank]
#        district.items["rare"] += game.items[rank + 1]
#        district.items["exceptional"] += game.items[rank + 2]

#        return


    def get_rand_item(quality = "junk", rank = None, item_type = None, item_types = None):

        if rank:
            return copy.deepcopy(rand_choice(game.items[rank]))

        elif item_types == ["Flower"]:
            return copy.deepcopy(rand_choice([it for it in district.items["F"] if it.type.name in item_types]))

        elif item_types and item_types != "all":
            return copy.deepcopy(rand_choice([it for it in district.items[quality] if it.type.name in item_types]))

        elif item_type:
            return copy.deepcopy(rand_choice([it for it in district.items[quality] if it.type.name == item_type.name]))

        else:
            return copy.deepcopy(rand_choice(district.items[quality]))

    def can_pay(price):

        if MC.gold >= price:
            return True

        else:
            return False


    def roll_result(crit_success = 95, crit_fail = 5 ): # This rolls a dice to randomize the result a little

        r = dice(100)

        if r <= crit_fail:
            return "critical failure"

        elif r <= 25:
            return "failure"

        elif r <= 75:
            return "neutral"

        elif r <= crit_success:
            return "success"

        elif r <= 100:
            return "critical success"


    def show_tt(pos="top_right"):

        tt = Tooltip("")

        if pos == "center":
            renpy.show_screen("tool", x = 0.5, y = 0.5, w = 300, h = 150)

        elif pos == "right":
            renpy.show_screen("tool", x = 1.0, y = 0.7, w = 215, h = 150)

        elif pos == "top_right":
            renpy.show_screen("tool", x = 0.93, y = 0.0, w = 0.32, h = 0.075, bg = False)

        elif pos == "hide":
            renpy.hide_screen("tool")

        return tt


    def set_girls_workdays():

        for girl in MC.girls:
            girl.set_workdays()

    def get_description(basetext, effects, separator="\n", final_dot=True):

        text1 = ""
        begin = True

        for effect in effects:
            d = effect.get_description()

            if begin and d:

                if basetext:
                    text1 = "{i}" + __(basetext) + "{/i}" + separator
                else:
                    text1 = ""

                text1 += __(capitalize(d))
                begin = False

            elif not begin and d:
                text1 += "，" + d

        if final_dot:
            if len(text1) > 0 and text1[-1] not in ("。", "！", "？"): # Makes sure punctuation is added last.
                text1 += "。"

        return __(text1)


    def get_log_changes(girl, change_log, changes, act): ## Where 'change_log' is a NightChangeLog object and 'changes' lists tuples with (stat_name, nb) - Used for perform()

        change_log.add("")

        for c in changes:

            stat, nb = c

            if stat in ("rep", "reputation"):
                change_log.add("声望：%i/%i (%s)" % (girl.rep, girl.get_stat_max("rep"), plus_text(int(nb), "rep")))

            elif stat == "gold":
                change_log.add("金币：{image=img_gold} %s" % plus_text(int(nb), "gold"))

            else:
                change_log.add("%s：%i/%i (%s)" % ((__(stat_name_dict[stat.capitalize()]), girl.get_stat(stat), girl.get_stat_max(stat), plus_text(int(nb), "stat"))), ttip = describe_leveled_stats(act), ttip_title = "%s技能变化" % girl_related_dict[act.capitalize()])

        return change_log

    def describe_leveled_stats(act):
        desc = ""
        for stat, _, chg in perform_job_dict[act + "_changes"]:
            desc += stat_name_dict[stat[0].capitalize()] + "："
            if chg > 1:
                desc += event_color["good"] % "++"
            elif chg == 1:
                desc += event_color["good"] % "+"
            elif chg < 0:
                desc += event_color["a little bad"] % "-"
            desc += "\n"
        return desc

    def get_change_text(changes): ## Where 'changes' lists tuples with (stat_name, nb)

        text_changes = ""

        for c in changes:

            stat, nb = c

            if nb:
                if stat in ("rep", "reputation"):
                    text_changes += __("声望: ") + plus_text(nb, color_scheme="rep", decimals=1)

                elif stat == "gold":
                    text_changes += __("金币: {image=img_gold} ") + plus_text(round_int(nb), color_scheme="gold")

                else:
                    text_changes += __("%s: " % stat_name_dict[stat.capitalize()]) + plus_text(round_int(nb), color_scheme="standard")

            text_changes += "\n"

        return text_changes


    def load_quest_pics(): ## Loads quests and class pics

        quest_board.pics = []

        # Looking for picture in quests directory

        imgfiles = [file for file in renpy.list_files() if file.startswith("quests/") and is_imgfile(file)]

        # Attaching each picture to the list with appropriate tags

        for file in imgfiles:

            file_name = file.split("/")[-1]

            quest_board.pics.append(Picture(file_name, file))


    def update_quests():

        quest_board.quests = []
        quest_board.classes = []

        quest_nb = 2 + dice(6)

        class_nb = 2 + dice(6)

        for i in range(quest_nb):

            q = copy.copy(rand_choice(quest_templates))

            d = dice(6)

            if district.rank <= 1 or d >= 4:
                q.randomize(district.rank)
            elif district.rank <= 2 or d >= 2:
                q.randomize(district.rank-1)
            else:
                q.randomize(dice(district.rank-2))

            quest_board.quests.append(q)

        for i in range(class_nb):

            c = copy.copy(rand_choice(class_templates))

            d = dice(6)

            if district.rank <= 1 or d >= 4:
                c.randomize(district.rank)
            elif district.rank <= 2 or d >= 2:
                c.randomize(district.rank-1)
            else:
                c.randomize(dice(district.rank-2))

            quest_board.classes.append(c)

        quest_board.updated = True


    def rape_attempt(girl, cust, threat, change_log):

        notify("%s: 强奸企图" % girl.fullname, pic=girl.portrait)

        text_descript = " 尽管她拒绝了，但顾客试图强迫她这样做。. "
        raped = False

        change_log.add("Rape attempt", "header")

        if brothel.get_security() >= threat: #You have enough guards to look after your girls
            text_descript += girl.name + " {color=[c_green]}叫了保安。他道过歉并表示只是个玩笑而已。{/color}"

            girl.change_mood(1)
            girl.change_fear(-1)

            change_log.add("Averted by security", col="good", ttip = event_color["good"] % "心情 +, 恐惧 -")

        elif MC.can_defend() and MC.get_defense() > girl.get_defense(): #You don't have enough guards but the Player is available and tougher than your girl

            if MC.get_defense() >= cust.get_defense():

                text_descript += "{color=[c_green]}你听到%s在喊救命，威胁着要把他赶出去。他决定好好表现。{/color}" % girl.name

                girl.change_mood(1)
                girl.change_love(1)
                girl.change_fear(-2)

                change_log.add("Averted by you", col="good", ttip = event_color["good"] % "心情 +, 爱情 +, 恐惧 -")

            elif girl.test_shield():

                text_descript += "幸运的是，她的魔法盾牌保护了她。顾客被吓到了，不好意思地同意退让."

                girl.change_mood(1)

                change_log.add("Averted by Magic Shield", col="good", ttip = event_color["good"] % "心情 +")

            else:
                text_descript += "{color=[c_red]}你想帮忙，但顾客把你打晕了，还把门锁上了。{/color}"
                raped = True

                girl.change_mood(-3)
                girl.change_love(-1)
                girl.change_fear(3)

                change_log.add("Security failure", col="very bad", ttip = event_color["bad"] % "心情 --, 爱情 -, 恐惧 ++")

            MC.interactions -= 1

        else: #You don't have enough guards and the Player is not available or weaker than your girl: she's on her own

            # May get a boost of debuff from past interactions with MC

            mod = 0

            if girl.remembers("reward", "defended") or girl.remembers("punish", "hurt"):
                mod = 1
            elif girl.remembers("punish", "defended"):
                mod = -1

            if girl.get_defense() + mod >= cust.get_defense():

                text_descript += "{color=[c_green]}%s 告诉他要么乖乖听话，要么失去一个重要的身体部位。他改变了主意。{/color}" % girl.name

                girl.track_event("defended")
                girl.change_mood(1)

                change_log.add("Averted by herself", col="good", ttip = event_color["good"] % "心情 +")

            elif girl.test_shield():

                text_descript += "幸运的是，她的魔法盾牌保护了她。顾客被吓到了，不好意思地同意退让."
                girl.change_mood(1)

                change_log.add("Averted by Magic Shield", col="good", ttip = event_color["good"] % "心情 +")

            else:

                text_descript += "{color=[c_red]}%s 我试着反抗他，但没有用，他对她为所欲为。{/color}" % girl.name
                raped = True

                girl.change_mood(-3)
                girl.change_fear(3)

                change_log.add("Security failure", col="very bad", ttip = event_color["bad"] % "心情 --, 恐惧 ++")

        return raped, text_descript

    def crazy_customer(girls, customers):

        crazy_changes = NightChangeLog("Security alert", col=c_lightred)

    ## Tests for violence and arson attempts (returns event if True)

        girl = rand_choice(girls)
        for cust in customers:

            if cust.crazy == "violent":

                notify("%s: 袭击企图" % girl.fullname, pic=girl.portrait)
                crazy_changes.add("Assault attempt", "header")

                violent_text = __(cust.name) + __(" 陷入癫狂,攻击了 ") + girl.name + __(" 电光火石之间！")
                violent_report = __("意外事件！有人施暴。")

                if brothel.get_risk() < 0: # Your guards on duty are ready to help
#                   reward = (cust.diff  + dice(cust.diff)) * district.rank
                    violent_text += "\n{color=[c_green]}幸运的是，你的保镖就在身边。他们很快联合起来对付他，把他打得屁滚尿流。\n{/color}你的女孩很安全，而你却把他钱包里的东西装进了口袋：%s金币." % str(cust.ent_budget)
                    violent_report = "{color=[c_green]}" + violent_report + " 你的警卫把他揍了一顿 (抢到了 %s 金币)。{/color}" % str(cust.ent_budget)
                    MC.gold += cust.ent_budget
                    girl.change_mood(1)
                    girl.change_fear(-1)

                    pic = Picture(path="events/" + rand_choice(security_pics["girl defense"]))

                    crazy_changes.add("Averted by security ({image=img_gold} +%i)" % cust.ent_budget, col="good", ttip = event_color["good"] % "心情 +, 恐惧 -")

                elif MC.can_defend() and MC.get_defense() > girl.get_defense(): # Your guards are somewhere else, your girl is helpless, it's your turn to take action!
                    if fight(cust, MC) == False:
                        violent_text += __("\n{color=[c_green]}你冲到现场，在他还没来得及行动之前把他的脸打烂。\n{/color}你的女孩安全了，而你却把他钱包里的东西装进了口袋：%s金币.") % str(cust.ent_budget)
                        violent_report = "{color=[c_green]}" + violent_report + __(" 你揍了他一顿 (抢到了 %s 金币)。{/color}") % str(cust.ent_budget)
                        girl.change_mood(1)
                        girl.change_fear(-2)
                        girl.change_love(1)
                        MC.gold += cust.ent_budget

                        pic = Picture(path="events/" + rand_choice(security_pics["girl defense"]))

                        crazy_changes.add("Averted by you ({image=img_gold} +%i)" % cust.ent_budget, col="good", ttip = event_color["good"] % "心情 +, 爱情 +, 恐惧 --")

                    elif girl.test_shield():
                        violent_text += __(" 她被魔法护盾保护着.")
                        girl.change_mood(1)

                        pic = Picture(path="events/" + rand_choice(security_pics["girl shield"]))

                        crazy_changes.add("Averted by Magic Shield", col="good", ttip = event_color["good"] % "心情 +")

                    elif girl.get_effect("special", "immune"):
                        violent_text += __(" 她对物理攻击免疫。.")
                        girl.change_mood(1)

                        pic = Picture(path="events/" + rand_choice(security_pics["girl shield"]))

                        crazy_changes.add("Averted by Immunity", col="good", ttip = event_color["good"] % "心情 +")

                    else:
                        violent_text += __("\n{color=[c_red]}你想帮她，但那个混蛋把你打倒在地，把你们两个都揍了一顿。\n{/color}") + girl.name + __(" 受伤了，你失去了一些自尊.")
                        wounds = girl.get_hurt(dice(3)+1)

                        girl.track_event("hurt", "一个暴力的顾客")

                        violent_report = "{color=[c_red]}" + violent_report + __(" 他打了你一顿并让%s受伤了。{/color} ") % girl.name
                        girl.change_mood(-2)
                        girl.change_fear(2)
                        girl.change_love(-1)

                        pic = Picture(path="events/" + rand_choice(violent_pics))

                        crazy_changes.add("Security failure", col="bad", ttip = event_color["bad"] % "心情 --, 爱情 -, 恐惧 ++")
                        crazy_changes.add(girl.fullname + " 受伤了 %i 天%s" % (wounds, plural(wounds)), col="very bad")



                else: # Your girl must defend herself!

                    mod = 0

                    if girl.remembers("reward", "defended") or girl.remembers("punish", "hurt"):
                        mod = 1
                    elif girl.remembers("punish", "defended"):
                        mod = -1

                    if girl.get_defense() + mod >= cust.get_defense():
                        violent_text += (__("\n{color=[c_green]}然而，你的女孩有办法保护自己. ") + rand_choice([__("她刺穿了这可怜虫的内脏，让他停下了脚步."),
                                        __("她一膝盖狠狠顶在他的蛋蛋上，然后在就之间他跪在地板上哭了起来."), __("她一脚踢在他脸, 彻底打败了他.")])
                                        + __("\n{/color}你的女孩很安全，你的手下把这个可怜的傻瓜扔到了暗巷里，你则把他钱包里的东西装进口袋：%s金币.") % str(cust.ent_budget))

                        violent_report = "{color=[c_green]}" + violent_report + __(" %s 毒打了他 (获得 %s 金币)。{/color}") % (girl.name, str(cust.ent_budget))

                        girl.track_event("defended")

                        girl.change_mood(1)
                        girl.change_fear(-1)
                        MC.gold += cust.ent_budget

                        pic = girl.get_pic("fight", strict=True, naked_filter=True, soft=True)

                        if not pic:
                            pic = girl.get_pic("fight", strict=True)
                            if not pic:
                                pic = Picture(path="events/" + rand_choice(security_pics["default girl fight"]))

                        crazy_changes.add("Averted by herself", col="good", ttip = event_color["good"] % "心情 +, 恐惧 -")

                    elif girl.test_shield():
                        violent_text += __(" 她被一个魔法盾所保护着.")
                        girl.change_mood(1)

                        pic = Picture(path="events/" + rand_choice(security_pics["girl shield"]))

                        crazy_changes.add("Averted by Magic Shield", col="good", ttip = event_color["good"] % "心情 +")

                    elif girl.get_effect("special", "immune"):
                        violent_text += __(" 她对物理攻击免疫.")
                        girl.change_mood(1)

                        pic = Picture(path="events/" + rand_choice(security_pics["girl shield"]))

                        crazy_changes.add("Averted by Immunity", col="good", ttip = event_color["good"] % "心情 +")

                    else:
                        violent_text += __("\n{color=[c_red]}你的女孩试图保护自己，但他似乎更强壮，把踢她到地上用拳头不停地打她。\n{/color}你最终把他赶走了，但 ") + girl.name + __(" 还是受伤了.")
                        girl.get_hurt(dice(3)+1)
#                         girl.add_log("hurt_days")

                        girl.track_event("hurt", "一个暴力的客户")

                        violent_report = "{color=[c_red]}" + violent_report + __(" %s 受伤了。{/color}") % girl.name
                        girl.change_mood(-2)
                        girl.change_fear(2)

                        pic = girl.get_pic("hurt", naked_filter=True, soft=True, strict=True)
                        if not pic:
                            pic = girl.get_pic("hurt", strict=True)
                            if not pic:
                                pic = Picture(path="events/" + rand_choice(violent_pics))

                        crazy_changes.add("Security failure", col="bad", ttip = event_color["bad"] % "心情 --, 恐惧 ++")

                log.add_report(violent_report)

                cust.crazy = "finished" # Prevents craziness from triggering twice

                return Event(pic, text = violent_text, sound = s_punch, with_st = vpunch, changes=crazy_changes), cust

            elif cust.crazy == "arsonist":

                notify("%s：纵火企图" % brothel.name)
                crazy_changes.add("Arson attempt", "header", col="bad")

                arson_text = ""
                arson_report = __("安全警报！火灾发生了。")
                arson = False

                if brothel.get_risk() < 0: # Your guards on duty are ready to help
                    arson_text += __(cust.name) + __(" 试图纵火烧毁你的青楼！\n{color=[c_green]}你的守卫抓住了他，还没等他点燃火柴就把他打晕了。{/color}")
                    arson_report = "{color=[c_green]}" + arson_report + __(" 你的警卫阻止了他。{/color}")

                elif MC.can_defend(): # Your guards are somewhere else, it's your turn to take action!
                    if fight(cust, MC) == False:
                        arson_text += __(cust.name) + __(" 试图纵火烧毁你的青楼！\n{color=[c_green]}事情发生的时候，你正在巡逻，还没等那坏蛋实施他的计划，你就把他打昏了。{/color}")
                        arson_report = "{color=[c_green]}" + arson_report + __(" 你阻止了他。{/color}")
                    else:
                        arson_text += __(cust.name) + __(" 试图纵火烧毁你的青楼！\n{color=[c_red]}你试图阻止他，但他疯狂地与你战斗，给火势蔓延留下了机会。{/color}")
                        arson_report = "{color=[c_red]}" + arson_report + __(" 你被打败了，青楼着火了。{/color}")
                        arson = True
                    MC.interactions -= 1

                else: # No one is here to help out
                    arson_text += __(cust.name) + __("{color=[c_red]} 纵火烧毁了你的青楼！\n你听到女孩们的尖叫，很快就看到你的庄园冒出了浓烟。{/color}")
                    arson_report = "{color=[c_red]}" + arson_report + __(" 那-那-那里起火了！{/color}")
                    arson = True

                if arson:
                    if MC.playerclass == "法师":
                        damage = dice(25) + 25 - 5 * MC.get_spirit()
                        if damage < 0:
                            damage = 0

                        arson_text += __("\n你召唤了风暴的力量,快速施放了一个降雨咒语。最终,损失还算有限。你的青楼状况有所恶化 ") + str(damage) + "。"
                        brothel.change_dirt(damage)

                    else:
                        damage = dice(25) + 25
                        arson_text += __("\n你和员工以及一些有帮助的顾客一起协力灭火。不过,这里受到严重损坏。你的青楼风评下降了 ") + str(damage) + "。"
                        brothel.change_dirt(damage)

                pic = rand_choice(arson_pics)

                log.add_report(arson_report)

                cust.crazy = "finished" # Prevents craziness from triggering twice

                return Event(Picture(pic, "events/" + pic), text = arson_text, sound = s_fire, with_st = vpunch, changes=crazy_changes), cust

        return False, False

    def get_customer_population_count(customers):
        pop_count = defaultdict(int)

        for cust in customers:
            pop_count[cust.pop] += 1

        ttip = ""

        for pop in all_populations:
            if pop_count[pop]:
                ttip += "%s：%i\n" % (setting_name_dict[pop.name.capitalize()], pop_count[pop])

        return ttip


    def reset_alerts():
        seen_alerts = defaultdict(bool)
        return

    def plus_text(nb, color_scheme=None, limit=0, pos_marker="+", neg_marker="", decimals=2): # Returns number as text with +/- sign and color scheme. Use decimals to specify the max length of a float (0 to force integer)

        pos_color, neg_color = {"standard": ("a little good", "a little bad"), "normal": ("good", "bad"), "gold": ("gold", "bad"), "stat": ("good", "bad"), "xp": ("xp", "bad"), "jp": ("jp", "bad"), "rep": ("rep", "bad"), None: (None, None)}[color_scheme]

        if decimals == 0:  # Use to catch zeros before next check
            nb_txt = "0"
        elif not decimals:
            nb_txt = str(nb)
        else:
            nb_txt = str_dec(nb, decimals)

        if nb > limit:
            return event_color[pos_color] % (pos_marker + nb_txt)
        elif nb == limit:
            return nb_txt
        else:
            return event_color[neg_color] % (neg_marker + nb_txt)

    def and_text(li, txt="和", prune_empty=True, if_none=event_color["bad"] % "#ERROR# No list", separator="、"): # prune_empty removes empty entries from the list

        if prune_empty:
            li = [tl_cn(x, [girl_related_dict, farm_related_dict]) for x in li if x]

        if not li:
            return if_none

        if len(li) == 1:
            return li[0]

        elif len(li) > 1:
            return separator.join(li[:-1]) + __(txt) + li[-1]

        else:
            return if_none

    def list_text(li, txt="* ", prune_empty=True, if_none=event_color["bad"] % "#ERROR# No list"): # prune_empty removes empty entries from the list

        if prune_empty:
            li = [x for x in li if x]

        if not li:
            return if_none

        return txt + ("\n" + txt).join(li)

    def plural(nb, ending = "", singular=""):

        if nb == 1:
            return singular

        else:
            return ending

    def article(noun):
        if noun[0].lower() in ("a", "i", "e", "o"):
            return __("") + noun
        else:
            return __("") + noun

    def season_text(d): # Where d is a dictionary containing text for all 4 seasons
        return d[calendar.get_season()]

    def capitalize(s): # This is different from the string capitalize method as it doesn't alter subsequent caps after the first char.
        return s[:1].upper() + s[1:]

    def uncapitalize(s):
        return s[:1].lower() + s[1:]

    def help(screen):
        target = "help"
        renpy.call(target, screen)

        return


    def fight(attacker, defender, att_bonus=0, def_bonus=0, advantage = "defender"): # Returns True if attacker won, False otherwise

        attack = attacker.get_defense(fight = True) + dice(6) + att_bonus
        defense = defender.get_defense(fight = True) + dice(6) + def_bonus

        if attack > defense:
            return True

        elif defense > attack:
            return False

        elif attack == defense and advantage == "attacker":
            return True

        elif attack == defense and advantage == "defender":
            return False

        else:
            return "tie"

    def get_gossip():

        # Generic gossip is always on
        # Chapter gossip is active only during a given chapter
        # District gossip is specific to the visited district
        # Story gossip is added by the story, permanently
        # Temp gossip is added by the story, and removed at the end of each chapter

        try:
            return rand_choice(generic_gossip + chapter_gossip[game.chapter] + district_gossip[selected_district.name] + story_gossip + temp_gossip)
        except:
            return rand_choice(generic_gossip)

    # def acquire_girl(girl, free = False, target=MC):
    #
    #     target.girls.append(girl)
    #
    #     if free:
    #         game.free_girls.remove(girl)
    #         game.track("free girl acquired")
    #
    #     girl.location = None
    #     girl.set_job(None)
    #     girl.set_workdays()
    #     girl.refresh_pictures()
    #
    #     girl.log["acquired"] = calendar.time
    #     girl.track_event("acquired", arg=girl.name)
    #     test_achievements(["free girl acquired", "originals", "slaves", "naked", "rank B", "rank A", "rank S", "rank X"])

    def relinquish_girl(girl): # Not exactly symetrical with acquire_girl, to clean up later

        girl.set_job(None)
        brothel.master_bedroom.remove_girl(girl)

        if girl in MC.girls:
            MC.girls.remove(girl)

        if girl in farm.girls:
            farm.girls.remove(girl)

        if girl.items: # Unequip all items before selling
            for it in list(girl.items): # shallow copy of list since deleting from girl.items
                if it.equipped:
                    girl.unequip(it)
                MC.take(girl, it)
                notify((girl.fullname + " 已经失去了 " + it.name), pic=girl.portrait)
                renpy.pause(0.5)

    def transact(obj, seller, buyer, price):
        if isinstance(obj, Item) and buyer != MC:
            if not obj.sellable:
                renpy.notify("%s: 你不能交易这个物品。" % obj.name)
                return False

        debug_notify(seller.type + " selling to " + buyer.type)

        if buyer.type == "NPC":
            MC.gold += price
        else:
            MC.gold -= price

        if seller.type == "MC":
            MC.sold[buyer].append(obj)

        buyer.take(seller, obj)

        renpy.block_rollback()

        return True

    def search_items(key):

        list = []

        for it in all_items:

            if key in it.name:

                list.append(it)

        return list


    def cust_diff_description(diff):

        if diff <= 25:
            d = __("非常容易")
            col = "c_green"

        elif diff <= 50:
            d = __("容易")
            col = "c_lightgreen"

        elif diff <= 100:
            d = __("一般")
            col = "c_yellow"

        elif diff <= 150:
            d = __("困难")
            col = "c_lightred"

        else:
            d = __("非常困难")
            col = "c_crimson"

        return "{color=[" + col + "]}" + d + "{/color}"


    def get_entertainment_bonus(customers):
        bonus_list = []
        satisfied = 0
        unsatisfied = 0

        for c in customers:
            val, sat = c.get_entertainment_bonus()
            bonus_list.append(val)
            if sat:
                satisfied += 1
            else:
                unsatisfied += 1

        return mean(bonus_list), satisfied, unsatisfied

## Performing (waitress, masseuse, geisha, dancer, whore)

    def perform(act, girls, customers, customer_reason = "", job_filter=False): # job_filter forces the use of the current job's tag as 'and_tag'

        change_log = NightChangeLog("薄暮冥冥", col=c_lightorange)

        xp_gains = defaultdict(int)
        rep_gains = defaultdict(int)
        jp_gains = defaultdict(int)
        tip_gains = defaultdict(int)

        # As suggested by Jinrey
        tip_multiplier = defaultdict(float) # (multiplicative)
        perk_tip_multiplier = defaultdict(float) # (additive)
        final_tip_change = defaultdict(int) # Applied last

        for girl in girls:
            tip_multiplier[girl] = perk_tip_multiplier[girl] = 1.0
        # End

        stat_gains = defaultdict(list)

        level_up = defaultdict(bool)
        job_up = defaultdict(bool)

        ev_type = "Normal"

        specials = []
        first_customer = defaultdict(bool)
        finish = False
        rape = False
        rand_item = None
        rape_text = ""
        tip_special = ""
        lost_virginity = defaultdict(bool)
        pickpocket_boost = 0
        ignore_budget = sum(g.get_effect("special", "ignore budgets") for g in girls)

        tired_changes = defaultdict(int)
        dirt_change = 0

        ## Update girls and customers flags

        for girl in girls:
            if not girl.has_worked:
                girl.has_worked = defaultdict(bool)

            if not girl.has_worked[calendar.time]:
                girl.has_worked[calendar.time] = True
                first_customer[girl] = True

        if act in all_jobs:
            for cust in customers:
                cust.receive_entertainment(act)
        elif act in all_sex_acts:
            for cust in customers:
                cust.receive_sex_act(act)
        else:
            raise AssertionError(str(act) + " 不是一份有效的工作或性行为对 " + girls[0].fullname)

        ## STEP 1: Get customers difficulty

        cust_diff = mean_int(c.diff for c in customers) # // len(customers)

        change_log.add("难度：%s" % cust_diff_description(cust_diff), "header", ttip = "难度与客户数量和所有目标客户的平均值有关。", ttip_title="难度", separator="\n")


        ## STEP 2: Get customer satisfaction

        entertainment_bonus = 0
        sex_act_bonus = 0
        ttip = ""

        if act in all_jobs:
            # Customers special effects (only one customer result applies: too easy?)
            base_entertainment_bonus, sat, unsat = get_entertainment_bonus(customers) # / len(customers)

            ttip += "基础加成：%s" % plus_text(int(base_entertainment_bonus))

            if unsat:
                ttip += " (%i 想做点别的事情)" % unsat

            # Lowering malus with effects such as the Party Girl perk
            entertainment_bonus = base_entertainment_bonus * girls[0].get_effect("boost", "customer penalties")

            # Up until this point, 'entertainment_bonus' is <= 0
            entertainment_bonus += sum(g.get_effect("increase satisfaction", "all jobs") for g in girls) + sum(g.get_effect("increase satisfaction", act) for g in girls)

            if entertainment_bonus != base_entertainment_bonus:
                ttip += "\n特技和特殊效果：%s" % plus_text(entertainment_bonus - base_entertainment_bonus)

        elif act in all_sex_acts:
            # Customers special effects

            if len(customers) > 1: # Group: Customer satisfaction penalties stack
                base_sex_act_bonus = sum(c.get_sex_act_bonus(group=True) for c in customers)
                ttip = "群交技能加成：%s" % plus_text(base_sex_act_bonus)
                sex_act_bonus = base_sex_act_bonus + sum(g.get_effect("increase satisfaction", "group") for g in girls)
                if base_sex_act_bonus != sex_act_bonus:
                    ttip += "\n特技和特殊效果：%s" % plus_text(sex_act_bonus - base_sex_act_bonus)

            elif len(girls) > 1: # Bisexual: +1 to customer satisfaction
                base_sex_act_bonus = mean(c.get_sex_act_bonus(bis=True) for c in customers) + 1
                ttip = "双飞技能加成：%s" % plus_text(base_sex_act_bonus, "normal")
                sex_act_bonus = base_sex_act_bonus + sum(g.get_effect("increase satisfaction", "bisexual") for g in girls)
                if base_sex_act_bonus != sex_act_bonus:
                    ttip += "\n特技和特殊效果：%s" % plus_text(sex_act_bonus - base_sex_act_bonus)

            else: # One on one
                cust = customers[0]

                if cust.wants_sex_act != cust.got_sex_act:
                    for girl in girls:
                        if girl.get_effect("special", "temptress"):
                            cust.wants_sex_act = cust.got_sex_act
                            specials.append(__("temptress"))
                            ttip += " (被特殊效果改变 " + event_color["good"] % "temptress" + ")"
                            break
                    else:
                        # Rape attempts
                        if cust.crazy == "rapist":
                            rape, rape_text = rape_attempt(girl, cust, brothel.get_threat(), change_log)
                            if rape:
                                act = cust.wants_sex_act
                                cust.got_sex_act = act
                                ttip += " (" + event_color["good"] % "raped" + ")"

                base_sex_act_bonus = cust.get_sex_act_bonus()

                ttip = "选择的性服务加成：%s" % plus_text(base_sex_act_bonus) + ttip

            sex_act_bonus = base_sex_act_bonus + sum(g.get_effect("increase satisfaction", "all sex acts") for g in girls) + sum(g.get_effect("increase satisfaction", act) for g in girls)

            if base_sex_act_bonus != sex_act_bonus:
                ttip += "\n特技和特殊效果：%s" % plus_text(sex_act_bonus - base_sex_act_bonus)

            #<Chris Job Mod: Bonus/Malus from Entertainment Score>
            if game.has_active_mod("chrisjobmod"):
                sex_act_bonus += ((cust.entertainment_score - entertainment_neutral_score) * entertainment_bonus_strength)
                ttip += "\n工作职业加成：%s" % plus_text((cust.entertainment_score - entertainment_neutral_score) * entertainment_bonus_strength)
            #</Chris Job Mod>

        # Improve customer mood if the bedroom type is better (lowers it if it isn't). Lower rank customers will be slightly less picky.

        cust_bonus = round_int(entertainment_bonus + sex_act_bonus + brothel.get_mood_modifier(min(district.rank-1, customers[0].rank)) + game.get_diff_setting("satisfaction"))

        ttip += "\n房间加成：%s" % plus_text(brothel.get_mood_modifier(min(district.rank-1, customers[0].rank)) + game.get_diff_setting("satisfaction"))

        # Special interactions

        for girl in girls:
            if first_customer[girl] and girl.get_effect("change", "first customer satisfaction"):
                cust_bonus += girl.get_effect("change", "first customer satisfaction")
                ttip += "第一个客户奖金：%s" % plus_text(girl.get_effect("change", "first customer satisfaction"))


            # BBCR bonus (may boost tip if procs depending on stat) - Unused for now
#             if girl.get_effect("special", "BBCR bonus"):

#                 spe = girl.get_stat(rand_choice(["beauty", "body", "charm", "refinement"])) - diff

#                 if spe > 0:
#                     tip_gains[girl] += spe
#                     specials.append(stat + " bonus")

            # LOCS bonus (may boost tip if procs depending on stat) - Unused for now
#             if girl.get_effect("special", "LOCS bonus"):

#                 spe = girl.get_stat(rand_choice(["libido", "obedience", "constitution", "sensitivity"])) - diff

#                 if spe > 0:
#                     tip_gains[girl] += spe
#                     specials.append(stat + " bonus")

            # Lost and Found perk

            if girl.get_effect("special", "random item"):
                specials.append("random item")
                d = dice(6)
                if d == 6:
                    rand_item = get_rand_item("rare")
                elif d >= 4:
                    rand_item = get_rand_item("common")
                else:
                    rand_item = get_rand_item()
                girl.items.append(rand_item)


#         if act in all_jobs:
#             for girl in girls:

#                 # Flasher - Unused for now
#                 if girl.get_effect("special", "flasher"):
#                     cust_bonus += girl.get_effect("special", "flasher")
#                     rep_gains[girl] += 1
#                     specials.append("flasher")

        if act in all_sex_acts: # Note: some of those effects are antiquated

            if len(customers) > 1:
                suf = "_group"
            else:
                suf = ""

            for girl in girls:

                # Virgin (in use)
                if act == "sex":
                    if girl.pop_virginity():
                        cust_bonus += 3
                        specials.append("virgin" + suf)
                        lost_virginity[girl] = True
                        ttip += event_color["good"] % "失去了童贞：+3"

                # DT (unused)
                spe = girl.get_effect("special", "deep throat")
                if spe and act == "service":
                    cust_bonus += spe
                    specials.append("DT" + suf)
                    ttip += event_color["good"] % "深喉：%s" % plus_text(spe)

                # Irrumatio (unused)
                if girl.get_effect("special", "irrumatio") and act == "service":
                    girl.change_stat("obedience", 1, silent=True)
                    stat_gains[girl].append(("obedience", 1))
                    specials.append("irrumatio")

                # Buk (unused)
                if girl.get_effect("special", "bukkake") and len(customers) > 1  and not finish:
                    cust_bonus += len(customers)
                    finish = True
                    dirt_change += brothel.change_dirt(len(customers))
                    specials.append("bukkake")
                    ttip += event_color["good"] % "多人颜射：%s" % plus_text(len(customers))

                # Creampie (unused)
                spe = girl.get_effect("special", "creampie")
                if spe and act == "sex" and not finish:
                    cust_bonus += spe
                    specials.append("creampie" + suf)
                    finish = True
                    dirt_change += brothel.change_dirt(1)
                    ttip += event_color["good"] % "外射：%s" % plus_text(spe)

                # A. Creampie (unused)
                spe = girl.get_effect("special", "anal creampie")
                if spe and act == "anal" and not finish:
                    cust_bonus += spe
                    specials.append("anal creampie" + suf)
                    finish = True
                    dirt_change += brothel.change_dirt(1)
                    ttip += event_color["good"] % "肛门中出：%s" % plus_text(spe)

                # Cum on face (unused)
                spe = girl.get_effect("special", "cum on face")
                if spe and not finish:
                    cust_bonus += spe
                    specials.append("cum on face" + suf)
                    finish = True
                    dirt_change += brothel.change_dirt(1)
                    ttip += event_color["good"] % "颜射：%s" % plus_text(spe)

                # # Swallow (unused)
                # if girl.get_effect("special", "swallow") and not finish:
                #     final_tip_change[girl] += 25 * customers[0].rank
                #     rep_gains[girl] += 1
                #     finish = True
                #     if girl.get_effect("special", "catgirl"):
                #         specials.append("catgirl")
                #     else:
                #         specials.append("swallow")

                # Heart of gold/Elite pickpocket and Pickpocket perks (including Renza's trainer effect)

                # Pickpocket (Hard-coded)

                caught_chance = 0

                # Converts the pickpocket trait to elite if Renza's effect is on
                if brothel.get_effect("special", "pickpocket") and girl.get_effect("special", "pickpocket", raw=True):
                    if renpy.random.random() <= 0.25:
                        pickpocket_boost = 0.1

                # Regular pickpocket effect
                elif girl.get_effect("special", "pickpocket"):
                    if renpy.random.random() <= 0.25:
                        pickpocket_boost = 0.1
                        caught_chance = 0.15

        change_log.add("顾客满意度：%s" % plus_text(cust_bonus, "normal"), ttip=ttip, ttip_title="顾客满意度")

        ## STEP 3: Calculate stat bonus

        stat_bonus = mean_int(girl.test_stats(perform_job_dict[act + "_stats"], cust_diff) for girl in girls) # // len(girls)
        ttip = "属性提高 (%s)：%s ({i}%s{/i})" % (girl_related_dict[act], plus_text(stat_bonus), and_text([s[0] for s in perform_job_dict[act + "_stats"]], "、"))

        sensitivity_bonus = 0
        if act in all_sex_acts:

            # Sensitivity bonus for sex acts

            for girl in girls:
                s = girl.get_stat("sensitivity") - cust_diff

                if s >= 25:
                    sensitivity_bonus += 2
                elif s >= 10:
                    sensitivity_bonus += 1
                elif s <= -25:
                    sensitivity_bonus += -2
                elif s <= -10:
                    sensitivity_bonus += -1
                else:
                    sensitivity_bonus += 0

            sensitivity_bonus = sensitivity_bonus // len(girls)


        if sensitivity_bonus:
            ttip += "\n敏感补正：%s" % plus_text(sensitivity_bonus)


        ## STEP 4: Get job level bonus

        job_bonus = mean_int(girl.job_level[act] for girl in girls) # // len(girls)
        ttip += "\n工作等级补正 (%s)：%s" % (girl_related_dict[act], plus_text(job_bonus))

        change_log.add("女孩技能：%s" % plus_text(stat_bonus + job_bonus, "normal"), ttip = ttip, ttip_title="技能属性奖励")

        ## STEP 5: roll dice

        d = dice(6)
        ttip = "表示她在给定交互中的表现。她摇了%i" % d

        # re-rolls (traits/perks)

        if d == 1:
            ttip += " (" + event_color["bad"] % "大失败" + ")"

            #Reroll chance
            if girls[0].get_effect("reroll", "critical failure") > 0 or (girls[0].get_effect("reroll", "job critical failure") > 0 and act in all_jobs) or (girls[0].get_effect("reroll", "whore critical failure") > 0 and act in all_sex_acts):
                d = dice(6)
                specials.append("reroll")

                ttip += " (" + event_color["bad"] % "大失败" + ")。她摇了%i" % d

        if d == 2:
            if girls[0].get_effect("special", "unlucky"):
                d = 1
                specials.append("unlucky")

                ttip += "，但是因为她运气不好，点数变成了1 (" + event_color["bad"] % "大失败" + ")"

        if d == 5:
            if girls[0].get_effect("special", "lucky"):
                d = 6
                specials.append("lucky")

                ttip += "，因为她很幸运，点数变成了6"

        ttip += "。"

        roll = roll_dict[d]

        # A roll of 6 will bypass budget restrictions

        if d == 6:
            ttip += " (" + event_color["good"] % "大成功" + ")。她可能会忽略客户的预算限制。"
            ignore_budget = 1

        roll_changes = __("检定: ") + "{image=" + "img_dice" + str(d) + "}"
        if "reroll" in specials:
            roll_changes += __(" (重新检定)")
            ev_sound = s_dice

        change_log.add(roll_changes, "header", ttip = ttip, ttip_title="检定")

        ## STEP 6: Misc. bonuses

        # Activate auto-work items
        item_used = False
        for it in girls[0].items:
            if item_used:
                break
            elif it.usage == "auto_work":
                for e in it.effects:
                    if e.target.startswith(act):
                        text1 = "使用 %s" % (it.name)
                        r = girls[0].use_item(it)
                        if r == "used_up":
                            text1 += event_color["bad"] % " (用完了)"
                        item_used = it

                        ttip = ""
                        for e in it.effects:
                            if e.type in ("gain", "changes"):
                                ttip += "%s：%s\n" % (e.target.capitalize(), plus_text(e.value))

                        change_log.add(text1 + "。", ttip = ttip, ttip_title = it.name)
                        break

        # Apply misc effects
        if act in all_jobs:
            misc_bonus = brothel.get_effect("change", "all jobs") + sum(g.get_effect("change", "all jobs", raw=True) for g in girls)
        elif act in all_sex_acts:
            misc_bonus = brothel.get_effect("change", "all sex acts") + sum(g.get_effect("change", "all sex acts", raw=True) for g in girls)

        misc_bonus += brothel.get_effect("change", act + " results") + sum(girl.get_effect("change", act + " results", raw=True) for girl in girls)

        ttip = "天赋和特效：%s" % plus_text(misc_bonus, "normal") + ttip

        #<Chris Job Mod: Apply Difficulty Modifier for Job>
        if game.has_active_mod("chrisjobmod"):
            misc_bonus += act_difficulty_modifier[act]
            ttip += "\n工作模式补正：%s" % plus_text(act_difficulty_modifier[act], "normal")
        #</Chris Job Mod>

        # Memories of rewards and punishment

        for girl in girls:
            if girl.remembers("reward", "good result"):
                misc_bonus += 1
                ttip += "\n奖励奖金：+1"
            if girl.remembers("punish", "bad result"):
                misc_bonus += 1
                ttip += "\n惩罚奖金：+1"

        if misc_bonus:
            change_log.add("其他效果：%s" % plus_text(misc_bonus, "normal"), ttip = ttip, ttip_title = "Miscellaneous")

        ## STEP 7: Get final result

        # Calculate score and get result
        score = d + stat_bonus + cust_bonus + sensitivity_bonus + job_bonus + misc_bonus

        for k in sorted(result_dict): # sorted used on a dictionary returns a list of all keys in ascending order
            if score >= k:
                result = result_dict[k]

        if result in ("very good", "perfect"):
            for cust in customers:
                if act in all_jobs:
                    cust.service_dict["entertained"] += 1
                elif act in all_sex_acts:
                    cust.service_dict["laid"] += 1

                if result == "perfect": unlock_achievement("happy " + cust.pop.name)

        #<Chris Job Mod: Assign the Score to all entertained customers>
        if game.has_active_mod("chrisjobmod"):
            if act in all_jobs:
                for cust in customers:
                    cust.entertainment_score = score
        #</Chris Job Mod>

        change_log.add(__("{b}最终结果{/b}：%i\n" % score) + result_star_dict[result], "header", ttip_title="{color=" + result_colors[result] + "}" + __(result.capitalize()) + "(%i){/color}" % score, ttip=result_reference)

        if act in all_jobs:
            change_log.add("客户招待：%i/%i" % (cust.service_dict["entertained"], len(customers)))

        elif act in all_sex_acts:
            change_log.add("客户服务：%i/%i" % (cust.service_dict["laid"], len(customers)))

        # Get tip, xp, jp and rep

        budget_ttip = "客户预算是他们愿意在这种互动上花费的金额上限。\n"
        if act in all_jobs:
            total_budget = sum(c.ent_budget for c in customers)
            if not ignore_budget:
                budget_boost = 1.0
                budget_ttip += "\n客户初始预算：%s (%s 客户)" % (total_budget, len(customers))
                for girl in girls:
                    budget_boost *= girl.get_effect("boost", "job customer budget")
                if budget_boost != 1.0:
                    budget_ttip += "\n天赋和特效：%s" % percent_text(budget_boost - 1.0)

                    total_budget *= budget_boost

        elif act in all_sex_acts:
            total_budget = sum(c.wh_budget for c in customers)
            if not ignore_budget:
                budget_boost = 1.0
                budget_ttip += "\n客户初始预算：%s (%s 客户)" % (total_budget, len(customers))
                for girl in girls:
                    budget_boost *= girl.get_effect("boost", "whore customer budget")
                if budget_boost != 1.0:
                    budget_ttip += "\n天赋和特效：%s" % percent_text(budget_boost - 1.0)

                    total_budget *= budget_boost

        initial_budget = total_budget # For use in the right-hand screen display

        gold_ttip = {}
        xp_ttip = {}
        jp_ttip = {}
        rep_ttip = {}

        for girl in girls:

            xp_gains[girl], xp_ttip[girl] = girl.get_xp(act, result, customers)
            jp_gains[girl], jp_ttip[girl] = girl.get_jp(act, result, customers)
            rep_gains[girl], rep_ttip[girl] = girl.get_rep(score, customers, first_customer[girl])

            # Calculate performance-related tip modifiers

            if lost_virginity[girl]:
                specials.append("lost virginity")

            # Bisexual modifier
            if len(girls) > 1:
                specials.append("bisexual")

            # Five Stars perk
            if cust_bonus > 0:
                final_tip_change[girl] += girl.get_effect("change", "total tip", custom_scale=("customer satisfaction", cust_bonus))

            # Focus perk
            if girl.get_effect("special", "focus") and act in all_sex_acts:
                if girl.count_activated_sex_acts() == 1:
                    specials.append("focus")
                    # perk_tip_multiplier[girl] += 0.25 # handled in get_tip
                    if rep_gains[girl] > 0:
                        rep_gains[girl] *= 1.25

            # Virgin whore perk
            if girl.has_trait("Virgin"):
                specials.append("virgin tip")
                # perk_tip_multiplier[girl] += girl.get_effect("boost", "virgin tip") - 1 # handled in get_tip
                if rep_gains[girl] > 0:
                    rep_gains[girl] *= girl.get_effect("boost", "virgin rep")

            _gold, gold_ttip[girl] = girl.get_tip(act, result, customers, final_tip_change[girl], first_customer[girl], specials=specials)
            tip_gains[girl] += _gold

            # Apply budget limits

            if not ignore_budget:
                if tip_gains[girl] > total_budget:
                    gold_ttip[girl] += event_color["bad"] % "\n客户预算限制：%s" % (total_budget - tip_gains[girl])
                tip_gains[girl] = min(tip_gains[girl], total_budget)

            total_budget -= tip_gains[girl]

        # Applying pickpocket effect (ignores budgets)

        if pickpocket_boost:
            girl = girls[0]
            gain = round_int(pickpocket_boost * tip_gains[girl])
            tip_gains[girl] += gain
            gold_ttip[girl] += "\n\n神偷：%s (%s)" % (plus_text(gain), girl.name)
            if renpy.random.random() <= caught_chance:
                rep_gains[girl] -= 1
                brothel.change_rep(-1 * customers[0].rank)
                gold_ttip[girl] += event_color["bad"] % "- Rep. lost"


        if len(girls) > 1:
            change_log.add("小费：{image=img_gold_20} %s" % plus_text(sum(tip_gains.values()), "gold"), "header")
            for girl in girls:
                change_log.add("%s：{image=img_gold} %s" % (girl.fullname, plus_text(tip_gains[girl], "gold")), ttip=gold_ttip[girl], ttip_title="总小费 (%s)" % (girl.fullname))
        else:
            girl = girls[0]
            change_log.add("小费：{image=img_gold_20} %s" % plus_text(tip_gains[girl], "gold"), "header", ttip=gold_ttip[girl], ttip_title="总小费")

        if ignore_budget:
            change_log.add("顾客预算：无限制", ttip=budget_ttip, ttip_title="顾客预算")
        else:
            if sum(tip_gains.values()) >= total_budget:
                budget_ttip += " (达到上限)"
            change_log.add("顾客预算：%s" % str(initial_budget), ttip=budget_ttip, ttip_title="顾客预算")


        ## STEP 8: Apply Changes
        # Receive XP, JP and REP gains

        for girl in girls:
            xp_gains[girl] = girl.change_xp(xp_gains[girl], silent=True)
            jp_gains[girl] = girl.change_jp(jp_gains[girl], act, silent=True)
            rep_gains[girl] = girl.change_rep(rep_gains[girl], silent=True)

            if girl.ready_to_level():
                level_up[girl] = True

            if girl.ready_to_job_up(act):
                job_up[girl] = True

        # Stats changes

        for girl in girls:
            stat_gains[girl] = girl.raise_stats(perform_job_dict[act + "_changes"])

        # Prestige and breaking

            if act in all_sex_acts:
                MC.change_prestige(girl.rank*girl.get_effect("boost", "prestige"))
                girl.raise_preference(act, bonus = 0.75)
                girl.add_log("perform " + act)

                if len(customers) > 1:
                    girl.raise_preference("group", bonus = 0.75)
                    girl.add_log("perform group")
                if len(girls) > 1:
                    girl.raise_preference("bisexual", bonus = 0.75)
                    girl.add_log("perform bisexual")

            elif act in all_jobs and girl.get_effect("special", "job prestige"):
                MC.change_prestige(girl.rank*girl.get_effect("boost", "prestige"))


        ## STEP 9: Maintenance and tiredness

        # Get tired

        if act in all_jobs or len(girls) > 1:
            tiredness = 5 * len(customers)
        else:
            tiredness = 10 * len(customers)

        #<Chris Job Mod>
        if game.has_active_mod("chrisjobmod"):
            tiredness = round_int(tiredness * act_tiredness_per_customer_modifier[act])
        #</Chris Job Mod>

        if "catgirl" in specials:
            tiredness = round_int(tiredness * 0.75) # Ugly, should be changed

        for girl in girls:
            if girl == girls[0]: # Only takes its description from the first girl
                tired_description, tired_changes[girl] = girl.tire(tiredness)
            else:
                tired_changes[girl] = girl.tire(tiredness)[1]

        # Get dirty

        if act in all_jobs:
            dirt_change += brothel.change_dirt(len(customers) / 2)
        elif act in all_sex_acts:
            dirt_change += brothel.change_dirt(len(customers))


        ## STEP 10: Pic, log, descriptions and base event

        # PICTURE - Choose perform picture

        and_tags = []
        not_tags = ["monster", "beast"] # Monster and beast pictures are not displayed during normal sex

        girl = girls[0]

        if lost_virginity[girl]:
            and_tags.append("virgin")

        if act in all_sex_acts:
            if not persistent.fuzzy_tagging_acts: # Disables machine and big for all non farm picture search
                not_tags.append("big")
                not_tags.append("machine")
            elif act != "fetish":
                not_tags.append("machine") # Machine pictures are excluded from normal sex (but not toy if fuzzy tagging is on)

            if len(customers) <= 1:
                not_tags.append("group") # Group pictures are excluded when there is only one customer
            if len(girls) <= 1:
                not_tags.append("bisexual") # Bi pictures are excluded when there is only one girl

            if (girl.work_whore or job_filter) and girl.job in all_jobs: # Adds a job tag if the girl is doing work & whore or job_filter is on
                and_tags += perform_job_dict[girl.job + "_tags"]

            # Group/Bisexual pictures can be mixed with regular pictures if the option is active

            if len(customers) > 1 and (not persistent.mix_group_pictures or dice(6) >= 4):
                work_pic = girl.get_pic(perform_job_dict["group_tags"], perform_job_dict[act + "_tags"], and_tags = and_tags + [act], not_tags = not_tags, and_priority=False, allow_lesbian=True)
            elif len(girls) > 1 and (not persistent.mix_bis_pictures or dice(6) >= 4):
                work_pic = girl.get_pic(perform_job_dict["bisexual_tags"], perform_job_dict[act + "_tags"], and_tags = and_tags + [act], not_tags = not_tags, and_priority=False, allow_lesbian=True)
            else:
                work_pic = girl.get_pic(perform_job_dict[act + "_tags"], and_tags = and_tags, not_tags = not_tags, allow_lesbian=True)

#             if not work_pic: # Defaults to sex if a picture hasn't been found
#                 work_pic = girls[0].get_pic("sex")

            if not work_pic: # Defaults to naked if a sex picture hasn't been found
                work_pic = girl.get_pic("naked", allow_lesbian=True)

        elif act in all_jobs:
            if persistent.fuzzy_tagging_jobs: # Allows secondary tags for jobs
                work_pic = girl.get_pic(perform_job_dict[act + "_tags"], perform_job_dict[act + "_tags2"], and_tags = and_tags, not_tags = not_tags, naked_filter=True, soft=True)
            else: # Disallows secondary tags
                work_pic = girl.get_pic(perform_job_dict[act + "_tags"], and_tags = and_tags, not_tags = not_tags, naked_filter=True, soft=True)

        if not work_pic:  # Defaults to profile if no other picture has been found
            work_pic = girl.get_pic("profile", and_tags = and_tags, not_tags = not_tags, naked_filter=True, soft=True, allow_lesbian=True)

        if not work_pic: # Shouldn't happen unless the pack is Broken
            work_pic = Picture(path="backgrounds/not_found.webp")

        # Determine customer gender

        if work_pic.has_tag("lesbian"):
            customers[0].gender = "F"

        # Compose description

        cust_names = capitalize(and_text([c.name.lower() for c in customers]))
        girl_names = and_text([g.name for g in girls])

        if len(customers) > 1:
            cust_pronoun = __("他们")
            cust_pronoun2 = __("他们的")
            cust_verb = __("")
        else:
            if customers[0].gender == "M":
                cust_pronoun = __("他")
                cust_pronoun2 = __("他的")
            else:
                cust_pronoun = __("她")
                cust_pronoun2 = __("她的")
            cust_verb = __("")

        if len(girls) > 1:
            girl_pronoun = __("他们")
        else:
            girl_pronoun = __("她们")

        if act in all_jobs:
            text_descript =  __(perform_job_dict[act + "_init"]) % (girl_names, len(customers))

        elif act in all_sex_acts:
            text_descript = __(customers[0].reason)

        if act in all_sex_acts:
            text_descript += __(perform_job_dict[customers[0].wants_sex_act + "_init"]) % girl_pronoun

            if customers[0].wants_sex_act != customers[0].got_sex_act:
                if len(customers) > 1:
                    text_descript += __(perform_job_dict["group not satisfied"]) % customers[0].got_sex_act

                elif len(girls) > 1:
                    text_descript += __(perform_job_dict["bisexual not satisfied"]) % customers[0].got_sex_act

                else:
                    text_descript += __(perform_job_dict["not satisfied"])

        if entertainment_bonus < 0:
            text_descript += __("\n一些客户可能更愿意做其他的事情。")

        # Replace pronouns
        text_descript = text_descript.replace(":cust:", cust_names)
        text_descript = text_descript.replace(":girl:", girl_names)
        text_descript = text_descript.replace(":pron:", cust_pronoun)
        text_descript = text_descript.replace(":Pron:", cust_pronoun.capitalize())
        text_descript = text_descript.replace(":verb:", cust_verb)
        text_descript = text_descript.replace(":poss:", cust_pronoun2)
        text_descript = text_descript.replace(":Poss:", cust_pronoun2.capitalize())

        log.add_report(text_descript)

        if rape_text:
            text_descript += __(rape_text)
            customers[0].gender = "M" # Rapists are always males to avoid complications

        if item_used:
            text_descript += "\n她使用 " + item_used.name.lower() + " 来改善心情。"

        for spe in specials:
            try:
                text_descript += event_color["good"] % __(perform_job_dict[spe]) % plural(len(customers))
            except:
                try:
                    text_descript += event_color["good"] % __(perform_job_dict[spe])
                except:
                    pass

        if act in all_sex_acts:
            if len(customers) > 1:
                text_descript += __(perform_job_dict["roll_" + roll]) % girl_names
                text_descript += __(perform_job_dict["group_" + result]) % girl_names
            elif len(girls) > 1:
                text_descript += __(perform_job_dict["bisexual_roll_" + roll]) % girl_names
                text_descript += __(perform_job_dict[customers[0].gender + " bisexual_" + result]) % girl_names
            else:
                text_descript += __(perform_job_dict["roll_" + roll]) % girl_names
                text_descript += __(perform_job_dict[customers[0].gender + " " + act + "_" + result]) % girl_names
        else:
            text_descript += __(perform_job_dict["roll_" + roll]) % girl_names
            text_descript += __(perform_job_dict[act + "_" + result]) % girl_names

        text_descript += tired_description


        # Budget cap description

        if total_budget == 0:
            text_descript += " {color=[c_green]}客人将 %s 预算全部花在了 %s 身上。{/color}" % (cust_pronoun2, girl_pronoun)
            for cust in customers:
                unlock_achievement("broke " + cust.pop.name)
        elif total_budget < 0: # with ignore_budget
            text_descript += " {color=[c_gold]} %s 让 %s 的预算超支消费了 (+%s 金币)。{/color}" % (girl_pronoun, cust_pronoun2, str_int(-total_budget))
            for cust in customers:
                unlock_achievement("broke " + cust.pop.name)

        # Compose right menu content (changes) - NEW

        for girl in girls:
            if act in all_jobs:
                job_ttip = list_text([(girl_related_dict[j.capitalize()] + " " + str(girl.job_level[j]) + " {image=img_star}") for j in all_jobs])
            elif act in all_sex_acts:
                job_ttip = list_text([(girl_related_dict[a.capitalize()] + " " + str(girl.job_level[a]) + " {image=img_star}") for a in all_sex_acts])

            change_log.add("%s 今夜收获" % girl.fullname, "header", ttip_title=girl.fullname, ttip = "%s 是一个等级%i的%s。\n\n%s" % (girl.name, girl.level, girl_related_dict[girl.job], job_ttip))

            if level_up[girl]:
                ev_type = "Level/Job/Rank up"
                log.add_report(log_event_dict["level"] % girl.fullname)
                # text_changes = __(stat_increase_dict["level"])
                #
                # if len(girls) > 1:
                #     text_changes += " {size=14}(" + girl.name + "){/size}" # Adds girl name for disambiguation if there are several

                change_log.add("等级提升", col="good", ttip = girl.fullname + " 准备升级 (%i -> %i)" % (girl.level, girl.level+1))

            change_log.add("{color=[c_lightgreen]}经验{/color}：%i/%i (%s)" % (girl.xp, girl.get_xp_cap(), plus_text(int(xp_gains[girl]), color_scheme = "xp")), ttip=xp_ttip[girl], ttip_title = "经验")

            if job_up[girl]:
                ev_type = "Level/Job/Rank up"
                log.add_report(log_event_dict["job_up"] % (girl.fullname, girl.job))
                # text_changes = __(stat_increase_dict["job_up"])
                #
                # if len(girls) > 1:
                #     text_changes += " {size=14}(" + girl.name + "){/size}" # Adds girl name for disambiguation if there are several

                change_log.add("工作技能等级提升", "header", col=c_orange)

            change_log.add("{color=[c_orange]}工作经验{/color}：%i/%i (%s)" % (girl.jp[act], girl.get_jp_cap(act), plus_text(int(jp_gains[girl]), color_scheme = "jp")), ttip=jp_ttip[girl], ttip_title = "工作经验")

            if girl.ready_to_rank():
                ev_type = "Level/Job/Rank up"
                log.add_report(log_event_dict["rank"] % girl.fullname)
                # text_changes = __(stat_increase_dict["rank"])
                #
                # if len(girls) > 1:
                #     text_changes += " {size=14}(" + girl.name + "){/size}" # Adds girl name for disambiguation if there are several

                change_log.add("阶级提升", "header", col=c_softpurple)

        # text_changes += stat_increase_dict["xp"] % str(round_int(xp_gains[girls[0]]))
        # text_changes += stat_increase_dict["jp"] % str(round_int(jp_gains[girls[0]]))

            if rep_gains[girl] > 0:
                change_log.add("{color=[c_softpurple]}声望{/color}：%i/%i (%s)" % (girl.rep, girl.get_rep_cap(), plus_text(rep_gains[girl], color_scheme = "rep", decimals=1)), ttip=rep_ttip[girl], ttip_title = "女孩声望")

            change_log = get_log_changes(girl, change_log, stat_gains[girl], act)

            change_log.add("体力：{color=%s}%i{/color}/%i (%s)" % (girl.get_energy_color(), girl.energy, girl.get_stat_max("energy"), event_color["bad"] % str_dec(tired_changes[girl], 1)), ttip=girl.get_energy_ttip(), ttip_title = "体力", before_separator="\n")

        if dirt_change:
            change_log.add("卫生：{color=%s}%s{/color}" % (c_lightred, plus_text(dirt_change)), ttip=maintenance_desc[brothel.get_cleanliness()], ttip_title = "污垢", before_separator="\n")
            log.dirt += dirt_change
            # debug_dirt_log.append([girls, dirt_change])

        # text_changes += "\n" + stat_increase_dict["gold+"] % str(round_int(sum(tip_gains.values()))) + tip_special

        # if total_budget == 0:
        #     text_changes += __("\n(max)")
        # elif total_budget < 0:
        #     text_changes += __("\n(over budget)")



        # Generate event(s)

        events = []

        if rape:
            ev_sound = s_scream_loud
            ev_type = "Health/Security"
        elif rand_item:
            ev_sound = s_spell
        else:
            ev_sound = None

        events.append(Event(pic = work_pic, char = girls[0].char, text = text_descript, changes = change_log, sound = ev_sound, type = ev_type))


        ## STEP 11: Special events

        # Add special breaking events

        if act in all_jobs: # Adds horny customer events during regular jobs

            girl = girls[0] # There is only one girl during jobs anyway
            extra_changes = []
            accepted = False

            chance = 10 * girl.get_effect("boost", "customer events")

            for cust in customers:
                if cust.get_effect("special", "horny"):
                    chance += 10

            if dice(100) <= chance:
                ev_type = "Customer"

                if dice(6) >= 4 or girl.naked:
                    # Jobs are linked to one specific sex act that they have a chance of improving through customer events
                    if act == "waitress":
                        s_act = "service"
                    elif act == "masseuse":
                        s_act = "sex"
                    elif act == "dancer":
                        s_act = "anal"
                    elif act == "geisha":
                        s_act = "fetish"

                    resisted_rule = False

                    # If MC has ruled out sex acts with customers
                    if girl.flags["forbid customer sex"]:
                        ob_target = girl.get_stat("obedience")*2 + girl.mood//5 - girl.get_stat("libido")

                        if girl.is_("very dom"):
                            ob_target -= 50
                        elif girl.is_("dom"):
                            ob_target -= 25
                        elif girl.is_("very sub"):
                            ob_target += 50
                        elif girl.is_("sub"):
                            ob_target += 25

                        ob_target += 15 * girl.remembers("punish", "fooled around")

                        if dice(girl.rank*50) > ob_target:
                            resisted_rule = True

                else:
                    s_act = "naked"

                s_des = {"naked" : "在他面前脱光", "service" : "舔弄他的肉棒", "sex" : "和他做爱", "anal" : "给他肛交", "fetish" : "和他尝试一些新玩法"}

                d = dice(3)

                # Naked event
                if s_act == "naked":

                    if d == 1: # Obedience
                        text1 = "{size=" + str(res_font(18)) + "}" + __("顾客开始叫嚷着要 ") + girl.name + __(" 脱光衣服。很快，她发现自己被一群好色的客户团团围住，想把她的衣服扯下来。")

                        r = girl.get_stat("obedience") - dice(250)

                        if r > 0:
                            text1 += __("\n{color=[c_green]}知道客户永远是对的，她让他们一个接一个地脱掉衣服，直到她完全赤身裸体。{/color}")
                            extra_changes.append(("obedience", girl.change_stat("obedience", dice(3), silent=True)))
                            extra_changes.append(("reputation", girl.change_stat("reputation", 1, silent=True)))

                            accepted = True

                        elif r > -50:
                            text1 += __("\n{color=[c_yellow]}顾客们非常坚持，所以她同意光着上身。{/color}\n尽管顾客会想要更多，但当前已满足于能在她工作的时候能抚摸到她裸露的乳房。")
                            extra_changes.append(("obedience", girl.change_stat("obedience", 1, silent=True)))

                            girl.raise_preference(s_act)

                        else:
                            text1 += __("\n{color=[c_red]}她尖叫着把顾客推开，大吵大闹起来。{/color}\n有几个顾客离开了，他们嘀咕说，他们见过的教堂比你的青楼还野。")
                            extra_changes.append(("reputation", girl.change_stat("reputation", -1, silent=True)))
                            extra_changes.append(("brothel reputation", brothel.change_rep(-1*customers[0].rank)))


                    elif d == 2: # Libido
                        text1 = "{size=" + str(res_font(18)) + "}" + __("一个好色的顾客开始在 ") + __(cnjob_room_dict[girl.job]) + __(". 中间脱衣服。他鼓励%s也这么做。") % girl.name

                        r = girl.get_stat("libido") - dice(250)

                        if r > 0:
                            text1 += __("\n{color=[c_green]}她觉得自己本欲火中烧，而且喜欢这个客户，所以她同意了。{/color}")
                            extra_changes.append(("libido", girl.change_stat("libido", dice(3), silent=True)))
                            extra_changes.append(("reputation", girl.change_stat("reputation", 1, silent=True)))

                            accepted = True

                        elif r > -50:
                            text1 += __("\n{color=[c_yellow]}她因为感到害羞，拒绝了，但顾客开始在她身上蹭来蹭去，撩起她的裙子和衬衫，让每个人都看一眼她的身体。{/color}\n她感到有些兴奋了。")
                            extra_changes.append(("libido", girl.change_stat("obedience", 1, silent=True)))

                            girl.raise_preference(s_act)

                        else:
                            text1 += __("\n{color=[c_red]}她告诉客户在呼叫保安之前把衣服穿上。{/color}\n客户很不高兴就离开了。")
                            extra_changes.append(("reputation", girl.change_stat("reputation", -1, silent=True)))
                            extra_changes.append(("brothel reputation", brothel.change_rep(-1*customers[0].rank)))

                    elif d == 3: # Sensitivity
                        text1 = "{size=" + str(res_font(18)) + "}" + __("一个醉酒的顾客告诉%s他爱着她，如果她能给他看她的天堂般的身体，他将是Zan中最幸福的人。") % girl.name

                        r = girl.get_stat("sensitivity") - dice(250)

                        if r > 0:
                            text1 += __("\n{color=[c_green]}所有的顾客都开始央求她，所以%s觉得自己无法拒绝。{/color}") % girl.name
                            extra_changes.append(("sensitivity", girl.change_stat("sensitivity", dice(3), silent=True)))
                            extra_changes.append(("reputation", girl.change_stat("reputation", 1, silent=True)))

                            accepted = True

                        elif r > -50:
                            text1 += __("\n{color=[c_yellow]}她拒绝了，但那人不停地恳求她，很快其他客户也来了。{/color}\n最后，她同意用自己的胸部来取悦观众。这让她有点兴奋。")
                            extra_changes.append(("sensitivity", girl.change_stat("sensitivity", 1, silent=True)))

                            girl.raise_preference(s_act)

                        else:
                            text1 += __("\n{color=[c_red]}她呵斥并对顾客大喊大叫。{/color}\n他失望的离开了。其他客户无意中听到这些，不满地抱怨起来。")
                            extra_changes.append(("reputation", girl.change_stat("reputation", -1, silent=True)))
                            extra_changes.append(("brothel reputation", brothel.change_rep(-1*customers[0].rank)))

                    if accepted:
                        pic = girl.get_pic(perform_job_dict[act + "_tags"], "naked", and_tags = "naked", not_tags = all_sex_acts + ["group", "bisexual", "beast", "monster"])
                    else:
                        pic = work_pic

                    events.append(Event(pic, char = girl.char, text = text1, changes = get_change_text(extra_changes), type = ev_type))

                # Sex acts
                else:

                    if d == 1: # Obedience
                        text1 = "{size=" + str(res_font(18)) + "}" + __("一个顾客点了") + girl.name + __(" 期待能得到额外的服务。他希望她") + __(s_des[s_act]) + "。"

                        r =  girl.get_stat("obedience") - dice(100) - preference_modifier[girl.get_preference(s_act)] # Reminder: preference modifier is between 150 (refuses) and -75 (fascinated)

                        if girl.flags["forbid customer sex"] and not resisted_rule:
                            r = min(0, r)

                        if r > 0:
                            if girl.has_trait("Virgin") and s_act == "sex":
                                s_act = weighted_choice([("service", 4), ("anal", 2), ("fetish", 1)])
                                text1 += __("\n{color=[c_green]}由于她是一个处女，她温和地拒绝了客户的要求，并同意用") + __(s_des[s_act]) + "来代替。{/color}"
                            else:
                                text1 += __("\n{color=[c_green]}她顺从地接受了客户的要求。{/color}")

                            extra_changes.append(("obedience", girl.change_stat("obedience", dice(3), silent=True)))
                            extra_changes.append(("reputation", girl.change_stat("reputation", 1, silent=True)))

                            accepted = True

                        elif r > -50:
                            text1 += __("\n{color=[c_yellow]}她礼貌地拒绝了，当客户抽出他的肉棒开始手淫的时候，她什么也没说{/color}\n整个经历让她感到困惑和亢奋。")
                            extra_changes.append(("obedience", girl.change_stat("obedience", 1, silent=True)))

                            girl.raise_preference(s_act)

                        else:
                            text1 += __("\n{color=[c_red]}她告诉客户让他滚蛋。{/color}\n他心烦意乱地离开了，抱怨你青楼的服务不行。")
                            extra_changes.append(("reputation", girl.change_stat("reputation", -1, silent=True)))
                            extra_changes.append(("brothel reputation", brothel.change_rep(-1*customers[0].rank)))


                    elif d == 2: # Libido
                        text1 = "{size=" + str(res_font(18)) + "}" + __("一位客户整晚都在和") + girl.name + __(" 调情。他试图让她") + __(s_des[s_act]) + "。"

                        r = girl.get_stat("libido") - dice(100) - preference_modifier[girl.get_preference(s_act)] # Reminder: preference modifier is between 150 (refuses) and -75 (fascinated)

                        if r > 0:
                            if girl.has_trait("Virgin") and s_act == "sex":
                                s_act = weighted_choice([("service", 4), ("anal", 2), ("fetish", 1)])
                                text1 += __("\n{color=[c_green]}为了保护她的童贞，她淫荡地同意") + __(s_des[s_act]) + __(" 来代替。{/color}")
                            else:
                                text1 += __("\n{color=[c_green]}她觉得自己欲火中烧，而且喜欢这个客户，所以她同意了。{/color}")
                            extra_changes.append(("libido", girl.change_stat("libido", dice(3), silent=True)))
                            extra_changes.append(("reputation", girl.change_stat("reputation", 1, silent=True)))

                            accepted = True

                        elif r > -50:
                            text1 += __("\n{color=[c_yellow]}她拒绝了，但客户非常坚持，她感觉自己有点欲火中烧。{/color}\n所以他稍微抚摸了一下她的乳房和屁股。")
                            extra_changes.append(("libido", girl.change_stat("obedience", 1, silent=True)))

                            girl.raise_preference(s_act)

                        else:
                            text1 += __("\n{color=[c_red]}她生气的离开了房间。{/color}\n顾客脾气暴躁，失望至极。")
                            extra_changes.append(("reputation", girl.change_stat("reputation", -1, silent=True)))
                            extra_changes.append(("brothel reputation", brothel.change_rep(-1*customers[0].rank)))

                    elif d == 3: # Sensitivity
                        text1 = "{size=" + str(res_font(18)) + "}" + __("一位顾客向她讲述了一个非常悲伤和感人的故事。他问她是否愿意 ") + __(s_des[s_act]) + __("，来帮助他忘记悲伤。")

                        r = girl.get_stat("sensitivity") - dice(100) - preference_modifier[girl.get_preference(s_act)] # Reminder: preference modifier is between 150 (refuses) and -75 (fascinated)

                        if r > 0:
                            if girl.has_trait("Virgin") and s_act == "sex":
                                s_act = weighted_choice([("service", 4), ("anal", 2), ("fetish", 1)])
                                text1 += __("\n{color=[c_green]}她想帮助他，并提出 ") + __(s_des[s_act]) + __(" 代替他，以保留她的贞操。{/color}")
                            else:
                                text1 += __("\n{color=[c_green]}她被他的故事感动了，决定不能拒绝他。{/color}")
                            extra_changes.append(("sensitivity", girl.change_stat("sensitivity", dice(3), silent=True)))
                            extra_changes.append(("reputation", girl.change_stat("reputation", 1, silent=True)))

                            accepted = True

                        elif r > -50:
                            text1 += __("\n{color=[c_yellow]}她温和地拒绝了，但还是给了顾客一个拥抱。{/color}\n他利用这个机会去磨蹭着她的身体，她也听之任之。")
                            extra_changes.append(("sensitivity", girl.change_stat("sensitivity", 1, silent=True)))

                            girl.raise_preference(s_act)

                        else:
                            text1 += __("\n{color=[c_red]}她冷冷地告诉客户，威胁要呼叫保安。{/color}\n他很不高兴，怨声载道地离开了。")
                            extra_changes.append(("reputation", girl.change_stat("reputation", -1, silent=True)))
                            extra_changes.append(("brothel reputation", brothel.change_rep(-1*customers[0].rank)))

                    if accepted and girl.flags["forbid customer sex"]:
                        text1 += event_color["bad"] % __("\n她无视你让她远离顾客的命令。")
                        girl.track_event("fooled around", arg=__(s_des[s_act]))

                    events.append(Event(pic = work_pic, char = girl.char, text = text1, changes = get_change_text(extra_changes), type = ev_type))

                    if accepted:
                        customers[0].wants_sex_act = s_act
                        events += perform(s_act, [girl], [customers[0]], job_filter=True)


        else: # Act weakness discovery during sex acts (actual fixations are only discovered by MC interaction for now)

            for girl in girls:

                if len(customers) > 1:
                    s_act = "group"
                    plur = "几位"
                elif len(girls) > 1:
                    s_act = "bisexual"
                    plur = ""
                else:
                    s_act = act
                    plur = ""

                if not girl.personality_unlock[s_act]:

                    ev_type = "Customer"

                    text1 = "{size=" + str(res_font(18)) + "}"

                    pos_reaction, neg_reaction = girl.test_weakness(s_act, unlock=True)

                    if pos_reaction and neg_reaction:
                        text1 += girl.name + __(" 脸红得通红 ") + __(long_act_description[s_act]) + __(". 让她看起来很不舒服。然而，她的乳头激凸，而且明显潮湿，明显一幅欲火中烧的样子。{color=[c_yellow]}她好像既喜欢又讨厌这样做。{/color}")
                        ev_sound = s_sigh
                        log.add_report(girl.name + "对于" + long_act_description[s_act] + "的感觉是{color=[c_darkgold]}矛盾的{/color}。")
                        chg = "{color=%s}发现矛盾的性行为:\n%s{/color}" % (c_yellow, girl_related_dict[s_act])

                    elif pos_reaction:
                        if act == "service":
                            text1 += girl.name + "在为" + plur + "顾客服务时，看到顾客的肉棒而感到慌乱。她开始边玩弄顾客边自慰。"
                        elif act == "fetish":
                            text1 += girl.name + __(" 被未知的感觉所淹没，在顾客的玩弄下她变得非常湿润。")
                        else:
                            text1 += girl.name + __(" 是非常敏感的，她最终达到高潮，因为她被客户操了") + plur + "。"

                        text1 += __("\n{color=[c_green]}她似乎很喜欢 ") + __(long_act_description[s_act]) + "。{/color}"
                        ev_sound = s_mmmh
                        log.add_report(girl.name + "对于" + long_act_description[s_act] + "的感觉是{color=[c_green]}敏感的{/color}。")
                        chg = "{color=%s}发现喜欢的性行为:\n%s{/color}" % (c_green, girl_related_dict[s_act])

                    elif neg_reaction:
                        text1 += girl.name + __(" 在") + plur + __("客户身边表现得很不自在, 似乎什么东西困扰着她。{color=[c_red]}她似乎不喜欢 ") + __(long_act_description[act]) + "。{/color}"
                        ev_sound = s_surprise
                        log.add_report(girl.name + "对于" + long_act_description[s_act] + "的感觉是{color=[c_red]}不舒服的{/color}。")
                        chg = "{color=%s}发现讨厌的性行为:\n%s{/color}" % (c_red, girl_related_dict[s_act])

                    if pos_reaction or neg_reaction:
                        events.append(Event(pic = work_pic, char = girl.char, text = text1, changes=chg, sound = ev_sound, type = ev_type))


        # Log information for tracking stats

        log.gold_made += sum(tip_gains.values())

        for girl in girls:
            girl.add_log("total_cust", len(customers))
            girl.add_log(act + "_cust", len(customers))
            girl.add_log(act + "_" + result, 1)
            girl.add_log(act + "_score", score)
            girl.add_log(act + "_score_base", 1)

            if act in all_sex_acts:
                girl.add_log("whore_cust", len(customers))
                girl.add_log("whore_" + result, 1)
                girl.add_log("whore_score", score)
                girl.add_log("whore_score_base", 1)

            girl.add_log("total_xp", xp_gains[girl])
            girl.add_log("total_gold", tip_gains[girl])
            girl.add_log("total_jp", jp_gains[girl])
            girl.add_log("total_rep", rep_gains[girl])

            girl.add_log(act + "_xp", xp_gains[girl])
            girl.add_log(act + "_gold", tip_gains[girl])
            girl.add_log(act + "_jp", jp_gains[girl])
            girl.add_log(act + "_rep", rep_gains[girl])

            if result in ("very bad", "bad"):
                girl.track_event("bad result", arg=(__(result), __(act)))

            elif result in ("good", "very good", "perfect"):
                girl.track_event("good result", arg=(__(result), __(act)))


        return events


    def refresh_quest_girls(girl, quest):

        if not quest:
            available_girls = [g for g in MC.girls if not (g.away or g.hurt > 0 or g.exhausted)]

        elif quest.type == "quest":
            available_girls = [g for g in MC.girls if quest.test_eligibility(g)[0]]

        else:
            available_girls = [g for g in MC.girls if not (g.away or g.hurt > 0 or g.exhausted)]

        if girl not in available_girls:
            try:
                girl = available_girls[0]
            except:
                girl = MC.girls[0]

        return girl, available_girls


    def update_NPC_items(n):

        n.items = []
        it = get_rand_item("rare")
        if it:
            n.items.append(it)

        return

    def weekly_updates(new_district=False):

        game.update_max_girl_level()
        update_slaves()
        refresh_available_locations()
        update_free_girls()
        cycle_free_girls()
        update_shops()
        if not new_district:
            update_market()
            update_quests()
        update_NPC_items(NPC_renza)
        update_NPC_items(NPC_captain)
        evpower_deck.update()

        return

    def add_event(lbl, chapter=0, date=0, year=0, month=0, day=0, chance = 1.0, type="day", location = None, min_gold = -99999, condition = None, not_condition = None, condition_func = None, call_args=None, once = True, AP_cost = 1, order = 0, weight = 1, room = None):

        # Type can be: "city", "day" (plays on main screen), "night" (plays upon ending day), "morning" (plays after night events)

        new_event = StoryEvent(label=lbl, chapter=chapter, date=date, year=year, month=month, day=day, chance=chance, type=type, location=location, min_gold=min_gold, condition=condition, not_condition=not_condition, condition_func=condition_func, call_args=call_args, once=once, AP_cost=AP_cost, order=order, weight=weight, room=room)

        if type == "city":
            city_events.append(new_event)
        elif type in ("any", "day", "night", "morning"):
            daily_events.append(new_event)

    def story_add_event(lbl, type="daily", duplicates=True):

#        renpy.say("", "Adding event " + lbl)
        if type == "city" or event_dict[lbl].location:
            if duplicates or event_dict[lbl] not in city_events: # Avoids creating duplicate events if duplicates is set to False
                city_events.append(event_dict[lbl])
                city_events.sort(key=lambda x: x.order)

        else:
            if duplicates or event_dict[lbl] not in daily_events: # Avoids creating duplicate events if duplicates is set to False
                daily_events.append(event_dict[lbl])
                daily_events.sort(key=lambda x: x.order)

        return

    def story_remove_event(lbl, type="city"):

#            renpy.say("", "Removing event " + lbl)

        if type == "city":
            try:
                city_events.remove(event_dict[lbl])
            except (KeyError, ValueError):
                return False

        else:
            try:
                daily_events.remove(event_dict[lbl])
            except (KeyError, ValueError):
                return False

        return True

    def story_set_condition(name, value=True):
        story_flags[name] = value
        return

    def get_vp_bounds(girl, girl_list):

        if selected_view_mode == "x40" or (selected_view_mode=="Auto" and len(girl_list)>24):
            h = girl_but_ysize["x40"]
            col = 4
            lines = 10
        elif selected_view_mode == "x24" or (selected_view_mode=="Auto" and len(girl_list)>12):
            h = girl_but_ysize["x24"]
            col = 3
            lines = 8
        elif selected_view_mode == "x12" or (selected_view_mode=="Auto" and len(girl_list)>4):
            h = girl_but_ysize["x12"]
            col = 2
            lines = 6
        else:
            h = girl_but_ysize["x4"]
            col = 1
            lines = 4

        if girl in girl_list:
            top_position = girl_list.index(girl)//col * h
            bottom_position = (girl_list.index(girl)//col-(lines-1)) * h

            top_bound = top_position - (lines-1) * h
            bottom_bound = bottom_position + (lines-1) * h

            return top_bound, bottom_bound

        else:
            return 0,0

    def focus_vp(girl_list):

        # This adjusts the viewport to show the selected girl

        if selected_girl in girl_list:
            top_bound, bottom_bound = get_vp_bounds(selected_girl, girl_list)

            if vp_adj.value < top_bound:
                vp_adj.change(top_bound)

            elif vp_adj.value > bottom_bound:
                vp_adj.change(bottom_bound)

        else:
            vp_adj.change(0)

        renpy.restart_interaction()

        return


    def select_previous_girl(girl_list, loop=True, pace=1):

        global selected_girl

        # if selected_girl and selected_girl in girl_list:
        #     previousindex = girl_list.index(selected_girl) - pace
        # else:
        #     previousindex = 0
        #
        # if previousindex < 0:
        #     if loop:
        #         previousindex = len(girl_list) -1
        #     else:
        #         previousindex = girl_list.index(selected_girl)
        #
        # selected_girl = girl_list[previousindex]

        selected_girl = get_previous(girl_list, selected_girl, loop, pace)

        focus_vp(girl_list)

        return

    def get_previous(mylist, current, loop=False, pace=1, avoid=None):

        mylist = [it for it in mylist if it != avoid]

        if mylist:
            if current in mylist:
                previousindex = mylist.index(current) - pace
            else:
                previousindex = 0

            if previousindex < 0:
                if loop:
                    previousindex = len(mylist) -1
                else:
                    previousindex = mylist.index(current)

            return mylist[previousindex]
        return current # Fallback

    def get_next(mylist, current, loop=False, pace=1, avoid=None):

        mylist = [it for it in mylist if it != avoid]

        if mylist:
            if current in mylist:
                nextindex = mylist.index(current) + pace
            else:
                nextindex = 0

            if nextindex > len(mylist) -1:
                if loop:
                    nextindex = 0
                else:
                    nextindex = len(mylist) -1

            return mylist[nextindex]
        return current # Fallback

    def select_next_girl(girl_list, loop=True, pace=1):

        global selected_girl

        # if selected_girl and selected_girl in girl_list:
        #     nextindex = girl_list.index(selected_girl) + pace
        # else:
        #     nextindex = 0
        #
        # if nextindex > len(girl_list) -1:
        #     if loop:
        #         nextindex = 0
        #     else:
        #         nextindex = girl_list.index(selected_girl)

        selected_girl = get_next(girl_list, selected_girl, loop, pace)

#        renpy.notify("Selected girl is " + selected_girl.name)

        focus_vp(girl_list)

        return

    def is_string(it):
        if isinstance(it, basestring):
            return True
        else:
            return False

    def make_list(it, obj_type = None): # Will automatically make a list of a single string, integer or float. Specify object type to list otherwise.

        if not it:
            return []

        if is_string(it) or isinstance(it, int) or isinstance(it, float):
            return list([it])

        if obj_type:
            if isinstance(it, obj_type):
                return list([it])

        return list(it)



    def reverse_if(boost, chg): ## Reverses boost if a stat is decreasing

        if chg < 0:
            boost = 1/float(boost)

        return boost

    def get_change_min_max(val, chg, _min, _max=10**18, enforce_boundaries=True): # Returns change to value after applying min and max. DOES NOT RETURN THE NEW VALUE.

        # If enforce_boundaries is True, a value outside the min-max range will be forced back to min or max

        if not enforce_boundaries:
            if val < _min or val > _max: # Change will be ignored if the value is outside of range
                return 0

        if _min <= val+chg <= _max:
            return chg

        elif val+chg < _min:
            return _min - val

        elif val+chg > _max:
            return _max - val


    def get_pic_list(thing, tags, and_tags = None, not_tags = None, weighted=True): # For performance reasons, get_pic_list should always receive lists as arguments

        # not_tags will be trimmed if they contradict search_tags or and_tags

        if not_tags:
#            not_tags = make_tuple(not_tags)
            for tag in tags:
                if tag in not_tags:
                    not_tags.remove(tag)

            if and_tags:
                for tag in and_tags:
                    if tag in not_tags:
                        not_tags.remove(tag)

        #<Chris12 PackState>
        # Use the new GirlFilesDict
        # Shows unrecognized files based on user settings.
        if weighted:
            if isinstance(thing, Girl):
                show_unrecognized = preferences.packstate_unrecognized != "Hide"
                return [(pic, pic.get_weight()) for pic in GirlFilesDict.get_pics(thing.path) if not pic.is_trash and (not pic.is_unrecognized or show_unrecognized) and pic.has_tags(tags, and_tags, not_tags)]
            #</Chris12 PackState>
            return [(pic, pic.get_weight()) for pic in thing.pics if pic.has_tags(tags, and_tags, not_tags)]

        else:
            if isinstance(thing, Girl):
                show_unrecognized = preferences.packstate_unrecognized != "Hide"
                return [pic for pic in GirlFilesDict.get_pics(thing.path) if not pic.is_trash and (not pic.is_unrecognized or show_unrecognized) and pic.has_tags(tags, and_tags, not_tags)]
            #</Chris12 PackState>
            return [pic for pic in thing.pics if pic.has_tags(tags, and_tags, not_tags)]


    def get_pic(thing, tags, alt_tags1 = None, alt_tags2 = None, alt_tags3 = None, and_tags = None, not_tags = None, strict = False, and_priority=True, attempts=0, always_stock=False):

        # First looks for a pic with one of 'tags'
        # If stock pictures are deactivated: the search will move to 'alt_tags1' if no pic is found, then 'alt_tags2', then 'alt_tag3'
        # If stock pictures are activated: the search will move to the default pictures
        # The 'and' and 'not_tags' apply to every set of tags.
        # If 'strict' is on, a False value is returned if no picture can be found with the and/not_tags conditions
        # If 'and_priority' is on, the 'and' and 'not' clauses will only be dropped after the search list has been exhausted
        # If 'always_stock' is on, a default pic will always be provided if it is missing, regardless of the stock_picture setting

        piclist = []

        tags = make_list(tags)
        alt_tags1 = make_list(alt_tags1)
        alt_tags2 = make_list(alt_tags2)
        alt_tags3 = make_list(alt_tags3)
        if and_tags:
            and_tags = make_list(and_tags)
        else:
            and_tags = []
        if not_tags:
            not_tags = make_list(not_tags)
        else:
            not_tags = []

        # Tags will be searched in that order
        if persistent.use_stock_pictures["missing"] or always_stock:
            search_list = [(thing, tags), (game, tags), (thing, alt_tags1), (game, alt_tags1), (thing, alt_tags2),  (game, alt_tags2), (thing, alt_tags3),  (game, alt_tags3)]
        else:
            search_list = [(thing, tags), (thing, alt_tags1), (thing, alt_tags2), (thing, alt_tags3)]

        for target, search_tags in search_list:

            ## Look for pictures matching ALL requirements
            attempts += 1

            piclist = get_pic_list(target, search_tags, and_tags, not_tags)

            # Mix with stock pictures if the number of pictures found is too low and the option has been activated in the H menu
            if persistent.use_stock_pictures["low"] and len(piclist) < stock_picture_threshold and target != game:
                piclist += get_pic_list(game, search_tags, and_tags, not_tags)

            if piclist != []:
#                renpy.say("", str(len(piclist)) + " pictures found: " + and_text([p.filename for p in piclist]))

                pic = weighted_choice(piclist)

#                renpy.say("", "Returning: " + pic.filename)

                game.last_pic = {"tags": search_tags, "and_tags": and_tags, "not_tags": not_tags, "attempts": attempts}

                if persistent.debug_pic_counter:
                    persistent.debug_pic_counter_dict[pic.path] += 1

                return pic

            ## Without and_priority
            # If nothing is found, drop the 'and' clauses (and_priority = False). not_tags clause is dropped last.

            if not and_priority and not strict:

                for i in range(len(and_tags)):
                    attempts += 1

                    _and_tags = and_tags[:-i-1] # Removes and_tags one by one, starting from the last one

                    piclist = get_pic_list(target, search_tags, and_tags=_and_tags, not_tags=not_tags)

                    # Mix with stock pictures if the number of pictures found is too low and the option has been activated in the H menu
                    if persistent.use_stock_pictures["low"] and len(piclist) < stock_picture_threshold and target != game:
                        piclist += get_pic_list(game, search_tags, and_tags=_and_tags, not_tags=not_tags)

                    if piclist != []:
                        pic = weighted_choice(piclist)
                        game.last_pic = {"tags": search_tags, "and_tags": and_tags, "not_tags": not_tags, "attempts": attempts}

                        if persistent.debug_pic_counter:
                            persistent.debug_pic_counter_dict[pic.path] += 1

                        return pic

                # If this is not enough, removes 'not_tags'
                for i in range(len(not_tags)):
                    attempts += 1

                    _not_tags = not_tags[:-i-1] # Removes not_tags one by one, starting from the last one

                    piclist = get_pic_list(target, search_tags, not_tags=_not_tags)

                    # Mix with stock pictures if the number of pictures found is too low and the option has been activated in the H menu
                    if persistent.use_stock_pictures["low"] and len(piclist) < stock_picture_threshold and target != game:
                        piclist += get_pic_list(game, search_tags, not_tags=_not_tags)

                    if piclist != []:
                        pic = weighted_choice(piclist)
                        game.last_pic = {"tags": search_tags, "and_tags": and_tags, "not_tags": not_tags, "attempts": attempts}

                        if persistent.debug_pic_counter:
                            persistent.debug_pic_counter_dict[pic.path] += 1

                        return pic

        # If nothing is found, drop the 'and' clauses (and_priority = True). not_tags clause is dropped last.

#        renpy.say("", "No matching pictures found.")


        ## With and_priority
        if and_priority and not strict:

            for i in range(len(and_tags)):
                _and_tags = and_tags[:-i-1] # Removes and_tags one by one, starting from the last one

                for target, search_tags in search_list:

                    attempts += 1

                    piclist = get_pic_list(target, search_tags, and_tags=_and_tags, not_tags=not_tags)

                    # Mix with stock pictures if the number of pictures found is too low and the option has been activated in the H menu
                    if persistent.use_stock_pictures["low"] and len(piclist) < stock_picture_threshold and target != game:
                        piclist += get_pic_list(game, search_tags, and_tags=_and_tags, not_tags=not_tags)

                    if piclist != []:
                        pic = weighted_choice(piclist)

                        game.last_pic = {"tags": search_tags, "and_tags": and_tags, "not_tags": not_tags, "attempts": attempts}

                        if persistent.debug_pic_counter:
                            persistent.debug_pic_counter_dict[pic.path] += 1

                        return pic

            for i in range(len(not_tags)):
                _not_tags = not_tags[:-i-1] # Removes not_tags one by one, starting from the last one

                for target, search_tags in search_list:

                    attempts += 1

                    piclist = get_pic_list(target, search_tags, not_tags=_not_tags)

                    # Mix with stock pictures if the number of pictures found is too low and the option has been activated in the H menu
                    if persistent.use_stock_pictures["low"] and len(piclist) < stock_picture_threshold and target != game:
                        piclist += get_pic_list(game, search_tags, not_tags=_not_tags)

                    if piclist != []:
                        pic = weighted_choice(piclist)

                        game.last_pic = {"tags": search_tags, "and_tags": and_tags, "not_tags": not_tags, "attempts": attempts}

                        if persistent.debug_pic_counter:
                            persistent.debug_pic_counter_dict[pic.path] += 1

                        return pic

        game.last_pic = {"tags": search_tags, "and_tags": and_tags, "not_tags": not_tags, "attempts": attempts}

        return None


    def cycle_list(mylist, item, number=1):

        if item not in mylist:
            raise AssertionError("Item not in list")

        idx = (mylist.index(item) + number) % len(mylist)

        return mylist[idx]

    def move_up_list(mylist, item):
        idx = mylist.index(item)
        if idx > 0:
            mylist.insert(idx-1, mylist.pop(idx))

    def move_down_list(mylist, item):
        idx = mylist.index(item)
        if idx < len(mylist):
            mylist.insert(idx+1, mylist.pop(idx))

    def can_interact(girl, type = None, slave = True, silent=True): # Antiquated, to be replaced by the GirlInteractionTopic method

        if not girl in MC.girls and slave:
            return False

        if MC.interactions < 1:
            return False

        if type:
            if type == "train" and girl.MC_interact_counters[type] >= 1:
                if not silent:
                    renpy.say("", "你不能一天里训练一个女孩超过一次。")
                return False

            elif type in ("present", "money", "offer") and girl.MC_interact_counters[type] >= 1:
                return False

            elif type == "offer" and len(MC.girls) >= brothel.bedrooms:
                return False

            elif girl.MC_interact_counters[type] >= 3:
                if not silent:
                    renpy.say("", "同样的事情，你一天里和一个女孩做的次数不能超过3次。")
                return False

        return True

    def get_act_menu(prompt=None, extended=True, girl=None, conditions=True):
        if extended:
            acts = extended_sex_acts
        else:
            acts = all_sex_acts

        menu_list = []

        if prompt:
            menu_list.append((prompt, None))

        for act in acts:
            text1 = long_act_description["action " + act]

            if girl and conditions and training_test_dict[act]: # Tests thresholds for training girls

                condition_met = False

                for cond, pref in training_test_dict[act]:
                    if compare_preference(girl, cond, pref):
#                            renpy.say("", "Can display " + act + " because " + cond + " is " + pref + " or more.")
                        condition_met=True
                        break
            else:
                condition_met = True

            if girl:
                if girl.personality_unlock[act]:
                    if act in girl.pos_acts and act in girl.neg_acts:
                        text1 = __(text1) + " (%s)" % emo_yang
                    elif act in girl.pos_acts:
                        text1 = __(text1) + " (%s)" % emo_heart
                    elif act in girl.neg_acts:
                        text1 = __(text1) + " (%s)" % emo_lightning
                else:
                    text1 = __(text1) + " (?)"

            if condition_met:
                menu_list.append((text1, act))

        menu_list.append(("返回", "back"))

        return menu_list



    def get_fix_menu(act, step = "all", girl = None):

        menu_list = []#[(prompt, None),]

        fix_list = get_fix_list(act, step)

        if girl:
            pos_fix = [f.name for f in girl.pos_fixations]
            neg_fix = [f.name for f in girl.neg_fixations]

        for fix in fix_list:
            text1 = fix_description[fix.name + " action"]

            if girl:
                if girl.personality_unlock[fix.name]:
                    if fix.name in pos_fix:
                        text1 = __(text1) + " (%s)" % emo_heart
                    elif fix.name in neg_fix:
                        text1 = __(text1) + " (%s)" % emo_lightning
                else:
                    text1 = __(text1) + " (?)"

            menu_list.append((text1, fix))

        menu_list.append(("没什么特别的", "no fix"))

        return menu_list

    def get_fix_list(act, step = "all"):

        if step == "all":
            return [fix for fix in fix_dict.values() if act in fix.acts]

        else:
            return [fix for fix in fix_dict.values() if act in fix.acts and step == fix.step]


    def this_is_a_hentai_game_so_why_are_you_trying_to_act_classy_all_of_a_sudden():

        global shake_count

        shake_count +=1

        if shake_count == 1:

            renpy.say(you, "我的意思是，我可以...", interact=False)

        elif shake_count == 2:

            renpy.say(you, "你知道的，只要五秒钟...", interact=False)

        elif shake_count == 3:

            renpy.say(you, "它不会伤害任何人...", interact=False)

        elif shake_count == 4:

            renpy.say(you, "什么....我到底怎么了...", interact=False)

        elif shake_count == 5:

            renpy.say(you, "我....我控制不了自己...", interact=False)

            shake_count = 0

        shake_mouse()

        return

    def shake_mouse(amplitude=150):

        amplitude = yres(amplitude)

        renpy.set_mouse_pos(renpy.get_mouse_pos()[0] + renpy.random.randint(0, amplitude) - xres(75), renpy.get_mouse_pos()[1] + (renpy.random.randint(yres(50), amplitude) * renpy.random.choice((-1, 1))), 0.1)

        return

    def compare_preference(girl, act, pref, bonus=0): # Returns True if a girl's preference is better or equal to Pref
        if preference_modifier[girl.get_preference(act, bonus)] <= preference_modifier[pref]:
            return True
        return False

    def get_preference_limit(act, pref):
        return base_reluctance[act] * preference_limit[pref]

    def get_act_weakness_symbol(girl, act):

        if girl.personality_unlock[act]:
            if act in girl.pos_acts and act in girl.neg_acts:
                return " (%s)" % emo_yang
            elif act in girl.pos_acts:
                return " (%s)" % emo_heart
            elif act in girl.neg_acts:
                return " (%s)" % emo_lightning
            else:
                return ""
        else:
            return " (?)"

    def get_fix_weakness_symbol(girl, fix_name):

        if girl.personality_unlock[fix_name]:
            if fix_name in [fix.name for fix in girl.pos_fixations]:
                return " (%s)" % emo_heart
            elif fix_name in [fix.name for fix in girl.neg_fixations]:
                return " (%s)" % emo_lightning
            else:
                return ""
        else:
            return " (?)"

    def can_use_minion_item():

        if MC.get_items(target="minion", name="愈合粉") and farm.get_hurt_minions():
            return True
        if MC.get_items(target="minion", effect_type="gain"):
            for it in MC.get_items(target="minion", effect_type="gain"):
                for eff in it.effects:
                    if eff.target[:-3] in all_minion_types: # This checks if the target effect starts with a minion type, then check if this type of minion exists in the farm (dirty)
                        if farm.get_minions(eff.target[:-3]):
                            return True
        return False

    def generate_name(type):
        if type == "stallion":
            return rand_choice(minion_name_dict["consonants"]).capitalize() + rand_choice(minion_name_dict["vowels"]) + rand_choice(minion_name_dict["consonants"])
        elif type == "beast":
#            return rand_choice(minion_name_dict["consonants"]) + rand_choice(minion_name_dict["vowels"]) + rand_choice(minion_name_dict["consonants"]) + rand_choice(minion_name_dict["vowels"])
            cons = rand_choice(minion_name_dict["consonants"])
            return cons.capitalize() + rand_choice(minion_name_dict["vowels"]) + cons + rand_choice(minion_name_dict["vowels"])
        elif type == "monster":
            return rand_choice(minion_name_dict["monster1"]).capitalize() + rand_choice(minion_name_dict["vowels"]) + rand_choice(minion_name_dict["monster2"])
        elif type == "machine":
            return rand_choice(minion_name_dict["consonants"] + minion_name_dict["vowels"]).capitalize() + rand_choice(minion_name_dict["consonants"] + minion_name_dict["vowels"]).capitalize() + "-" + str(99 + dice(900))
        elif type == "girl":
            first_name = ""

            syllabs = dice(3)

            if syllabs == 1:
                first_name += rand_choice(girl_name_dict["syllabs"]) + rand_choice(girl_name_dict["enders"])

            elif syllabs == 2:
                first_name += rand_choice(girl_name_dict["syllabs"]) + rand_choice(girl_name_dict["fillers"]) + rand_choice(girl_name_dict["syllabs"])

            elif syllabs == 3:
                first_name += rand_choice(girl_name_dict["syllabs"]) + rand_choice(girl_name_dict["syllabs"]) + rand_choice(girl_name_dict["enders"])

            syllabs = dice(4)

            last_name = ""

            if syllabs == 1:
                last_name = rand_choice(girl_name_dict["last_syllabs"]) + rand_choice(girl_name_dict["enders"])
            else:
                for i in range(syllabs):
                    last_name += rand_choice(girl_name_dict["last_syllabs"])

            return first_name.capitalize(), last_name.capitalize()

    def read_init_file_generate_as(file):
        if file:
            v = read_init_file_field(file, "background story", "generate_as", _default="all", skip_checks=True)
            return v
        return "all"

    def read_init_file_field(file, _key, _value, _default="default", skip_checks=False):
        if file:
            field = read_init_file(file, search_for = {_key : [_value]}, skip_checks=skip_checks)[_key + "/" + _value]
            if field:
                return field
        return _default

    ## To add a new _BK.ini value:
    #  1. Edit _BK.ini template and define variable type and possible values
    #  2. Update the search_for dictionary below
    #  3. Add sanity checks as necessary
    #  4. Define cloning behavior
    #  5. Update relevant parts of girl generation

    def read_init_file(file, search_for = None, skip_checks=False): ## This compiles a dictionary of values contained in a _BK.ini file. The dictionary acts as a buffer to account for the possibility of user mistakes.

        global read_ini_log

        input_dict = defaultdict(list)

        ## Read file

        parser = configparser.ConfigParser()

        try:
            parser.read(config.gamedir + "/" + file)
        except UnicodeDecodeError:
            raise AssertionError("Error reading file: " + config.gamedir + "/" + file + ". Please make sure that special characters in the _BK.ini file are encoded in Unicode.")
        except:
            raise AssertionError("Error reading file: " + config.gamedir + "/" + file + ". Please verify _BK.ini file integrity.")

        ## list sections and values to search for in the .ini file (update this when the .ini format is updated)

        if not search_for:
            search_for = {
                          "identity" : ["first_name", "last_name", "inverted_name", "creator", "version", "description", "unique", "keep_first_name", "keep_last_name", "keep_inverted"],
                          "base skills" : gstats_main + ["keep_skills"],
                          "base positive traits" : ["always", "often", "rarely", "never", "keep_traits"],
                          "base negative traits" : ["always", "often", "rarely", "never", "keep_traits"],
                          "base personality" : ["always", "often", "rarely", "never", "keep_personality"],
                          "custom personality" : ["custom_personality", "name", "personality_name", "attributes", "personality_dialogue_only", "dialogue_personality_weight", "dialogue_attribute_weight", "description", "custom_dialogue_label"],
                          "tastes" : ["favorite_color", "favorite_food", "favorite_drink", "disliked_color", "disliked_food", "disliked_drink", "hobbies"],
                          "sexual preferences" : ["favorite_acts", "disliked_acts", "favorite_fixations", "always_fixations", "always_negative_fixations", "disliked_fixations", "never_fixations", "never_negative_fixations", "sexual_experience", "farm_weakness", "keep_sex"],
                          "background story" : ["generate_as", "generate_in", "move_after_meeting", "origin", "origin_description", "always_slave_story", "often_slave_story", "rarely_slave_story", "never_slave_story", "init_function", "city_label", "story_label", "night_label", "interact_prompt", "keep_generate_as", "keep_init", "keep_background", "keep_interactions"],
                          "cloning options" : ["unique", "keep_first_name", "keep_last_name", "keep_inverted", "keep_skills", "keep_traits", "keep_personality", "keep_sex", "keep_generate_as", "keep_init", "keep_background", "keep_interactions"]
                          }

        for k, v in search_for.items():
            for thing in v:
                try:
                    input_dict[k + "/" + thing] = ast.literal_eval(parser.get(k, thing.lower()))
                except:
                    read_ini_log += "\nAn error has been found parsing " + k + "/" + thing + " in " + file + ", or it has been intentionally left out."
                    # pass

        if skip_checks:
            return input_dict

        ## Sanity checks

        # Skills

        for key in gstats_main: # Makes sure all values are between 0 and 5
            try:
                input_dict["base skills/" + key] = max(min(input_dict["base skills/" + key], 5), 0)
            except:
                input_dict["base skills/" + key] = 0

        # Traits and Personalities

        for key in ["always", "often", "rarely", "never"]:
            input_dict["base positive traits/" + key] = [t.capitalize() for t in input_dict["base positive traits/" + key]]
            input_dict["base negative traits/" + key] = [t.capitalize() for t in input_dict["base negative traits/" + key]]

            for trait in input_dict["base positive traits/" + key]:
                if trait not in trait_dict.keys():
                    input_dict["base positive traits/" + key].remove(trait)

                    if trait in renamed_traits.keys(): # Updates trait name for backwards compatibility
                        input_dict["base positive traits/" + key].append(renamed_traits[trait])
                    else:
                        renpy.say("{color=[c_red]}{b}解析错误 " + file + "{/b}{/color}", "{color=[c_red]}" + str(trait) + "{/color} is not a valid trait.\nCheck the correct use of brackets and quotes.")

            for trait in input_dict["base negative traits/" + key]:
                if trait not in trait_dict.keys():
                    input_dict["base negative traits/" + key].remove(trait)

                    if trait in renamed_traits.keys(): # Updates trait name for backwards compatibility
                        input_dict["base negative traits/" + key].append(renamed_traits[trait])
                    else:
                        renpy.say("{color=[c_red]}{b}解析错误 " + file + "{/b}{/color}", "{color=[c_red]}" + str(trait) + "{/color} is not a valid trait.\nCheck the correct use of brackets and quotes.")

            input_dict["base personality/" + key] = [p.lower() for p in input_dict["base personality/" + key]]

            for pers in input_dict["base personality/" + key]:
                if pers not in gpersonalities.keys():
                    renpy.say("{color=[c_red]}{b}解析错误 " + file + "{/b}{/color}", "{color=[c_red]}" + str(pers) + "{/color} is not a valid personality.\nCheck the correct use of brackets and quotes.")

        # Custom personality (for backwards compatibility)

        if input_dict["custom personality/name"] and not input_dict["custom personality/personality_name"]:
            input_dict["custom personality/personality_name"] = input_dict["custom personality/name"]

        # Tastes

        for tas in search_for["tastes"]:
            if tas == "hobbies":
                if input_dict["tastes/" + tas]:
                    input_dict["tastes/" + tas] = make_list(input_dict["tastes/" + tas]) # Makes sure entry is a list
                    if len(input_dict["tastes/" + tas]) > 2: # Limits number of hobbies to two
                        input_dict["tastes/" + tas] = input_dict["tastes/" + tas][:2]
            else:
                if input_dict["tastes/" + tas] and not is_string(input_dict["tastes/" + tas]):
                    input_dict["tastes/" + tas] = None

        # Preferences

        for key in ["favorite_acts", "disliked_acts"]:
            input_dict["sexual preferences/" + key] = [p.lower() for p in input_dict["sexual preferences/" + key]]

            for act in input_dict["sexual preferences/" + key]:
                if act not in extended_sex_acts:
                    renpy.say("{color=[c_red]}{b}错误解析 " + file + "{/b}{/color}", "{color=[c_red]}" + str(act) + "{/color} is not a valid sex act.\nCheck the correct use of brackets and quotes.")

        # Fixations

        for key in ["always_fixations", "always_negative_fixations", "favorite_fixations", "disliked_fixations", "never_fixations", "never_negative_fixations"]:
            input_dict["sexual preferences/" + key] = [p.lower() for p in input_dict["sexual preferences/" + key]]

            for fix in input_dict["sexual preferences/" + key]:
                if fix not in fix_dict.keys():
                    renpy.say("{color=[c_red]}{b}错误解析 " + file + "{/b}{/color}", "{color=[c_red]}" + str(fix) + "{/color} is not a valid fixation.\nCheck the correct use of brackets and quotes.")

        # Prior sexual experience

        if input_dict["sexual preferences/sexual_experience"]:
            input_dict["sexual preferences/sexual_experience"] = input_dict["sexual preferences/sexual_experience"].lower()

            if input_dict["sexual preferences/sexual_experience"].lower() not in list(sexual_training_value.keys()) + ["random"]:
                renpy.say("{color=[c_red]}{b}错误解析 " + file + "{/b}{/color}", "{color=[c_red]}" + str(input_dict["sexual preferences/sexual_experience"]) + "{/color} is not a valid setting.\nAccepted values are " + '"very experienced", "experienced",  "average", "inexperienced", "very inexperienced", "random".')

        # Farm

        if input_dict["sexual preferences/farm_weakness"]:
            input_dict["sexual preferences/farm_weakness"] = input_dict["sexual preferences/farm_weakness"].lower()

            if input_dict["sexual preferences/farm_weakness"] not in all_minion_types + ["random"]:
                renpy.say("{color=[c_red]}{b}错误解析 " + file + "{/b}{/color}", "{color=[c_red]}" + str(input_dict["sexual preferences/farm_weakness"]) + '{/color} is not a valid farm weakness.\nAccepted values are "stallion", "beast", "monster", "machine", "random".')

        # Back story

        if input_dict["background story/generate_as"]:
            input_dict["background story/generate_as"] = input_dict["background story/generate_as"].lower()
            if input_dict["background story/generate_as"] not in ("slave", "free", "story", "all"):
                raise AssertionError("_BK.ini error with girlpack: %s. 'background story/generate_as' should be set to 'all', 'slave', 'free' or 'story'." % file)
        else:
            input_dict["background story/generate_as"] = "all"

        if input_dict["background story/generate_in"]:
            if input_dict["background story/generate_in"] != "all":

                if is_string(input_dict["background story/generate_in"]): # For single entries
                    input_dict["background story/generate_in"] = [input_dict["background story/generate_in"]] # Creates a list

                # Converts every entry to lower case
                try:
                    input_dict["background story/generate_in"] = [loc.lower() for loc in input_dict["background story/generate_in"]]
                except:
                    raise AssertionError("_BK.ini error with girlpack: %s. 'background story/generate_in' should be set to 'all' OR a list of valid district or location names, spelled exactly as in-game. Don't forget the article for districts (e.g. 'The Slums')." % file)

                for loc in input_dict["background story/generate_in"]:
                    if loc not in ["all"] + [d.name.lower() for d in all_districts] + [l.name.lower() for l in all_locations]:
                        raise AssertionError("_BK.ini error with girlpack: %s. 'background story/generate_in' should be set to 'all' OR a list of valid district or location names, spelled exactly as in-game. Don't forget the article for districts (e.g. 'The Slums')." % file)



        else:
            input_dict["background story/generate_in"] = "all"

        if input_dict["background story/move_after_meeting"] != False:
            input_dict["background story/move_after_meeting"] = True

        return input_dict

    def clone_init_dict(input_dict):

        global read_ini_log

        ## Support for new _BK.ini format (cloning options no longer a sub-section)
        for section, klist in [("identity", ("unique", "keep_first_name", "keep_last_name", "keep_inverted")), ("base skills", ("keep_skills")), ("base positive traits", ("keep_traits")), ("base negative traits", ("keep_traits")), ("base personality", ("keep_personality")), ("sexual preferences", ("keep_sex")), ("background story", ("keep_generate_as", "keep_init", "keep_background", "keep_interactions"))]:
            for k in klist:
                if input_dict[section + "/" + k]:
                    if k == "keep_traits":
                        if input_dict["base positive traits/keep_traits"] and input_dict["base negative traits/keep_traits"] and input_dict["base positive traits/keep_traits"] != input_dict["base negative traits/keep_traits"]:
                            read_ini_log += "\nConflict with {b}%s{/b} key: %s overwritten by %s setting." % (k, "base positive traits/keep_traits", "base negative traits/keep_traits")
                            input_dict["base positive traits/keep_traits"] = input_dict["base negative traits/keep_traits"]
                    if input_dict["cloning options/" + k]:
                        read_ini_log += "\nConflict with {b}%s{/b} key: %s overwritten by %s setting." % (k, "cloning options/" + k, section + "/" + k)
                    input_dict["cloning options/" + k] = input_dict[section + "/" + k]

        ## Cloning default settings

        if not input_dict["cloning options/keep_first_name"]:
            if not persistent.keep_firstname:
                input_dict["identity/first_name"] = "?rand"
        if not input_dict["cloning options/keep_last_name"]:
            if not persistent.keep_lastname:
                input_dict["identity/last_name"] = "?rand"
        if not input_dict["cloning options/keep_inverted"]:
            input_dict["identity/inverted_name"] = False
        if not input_dict["cloning options/keep_skills"]:
            for skill in gstats_main:
                input_dict["base skills/" + skill] = 0
        if not input_dict["cloning options/keep_traits"]:
            for key in ["always", "often", "rarely", "never"]:
                input_dict["base positive traits/" + key] = []
                input_dict["base negative traits/" + key] = []
        if not input_dict["cloning options/keep_personality"]:
            for key in ["always", "often", "rarely", "never"]:
                input_dict["base personality/" + key] = []
            input_dict["custom personality/custom_personality"] = False
            for key in ["favorite_color", "favorite_food", "favorite_drink", "disliked_color", "disliked_food", "disliked_drink", "hobbies"]:
                input_dict["base personality/" + key] = None
        if not input_dict["cloning options/keep_sex"]:
            for key in ["favorite_acts", "disliked_acts", "favorite_fixations", "disliked_fixations", "always_fixations", "always_negative_fixations", "never_fixations", "never_negative_fixations"]:
                input_dict["sexual preferences/" + key] = []
            input_dict["sexual preferences/sexual_experience"] = "random"
            input_dict["sexual preferences/farm_weakness"] = "random"
        if not input_dict["cloning options/keep_generate_as"]:
            input_dict["background story/generate_as"] = "all"
            input_dict["background story/generate_in"] = "all"
        if not input_dict["cloning options/keep_init"]:
            input_dict["background story/init_function"] = None
        if not input_dict["cloning options/keep_background"]:
            input_dict["background story/origin"] = "random"
            input_dict["background story/origin_description"] = None
            for key in ["always_slave_story", "often_slave_story", "rarely_slave_story", "never_slave_story"]:
                input_dict["background story/" + key] = []
            input_dict["background story/story_label"] = None
        if not input_dict["cloning options/keep_interactions"]:
            input_dict["background story/city_label"] = None
            input_dict["background story/night_label"] = None
            input_dict["background story/interact_prompt"] = None

        return input_dict


    #  <DougTheC> Take advantage of "and" being short-circuit operator to speed process
    #  Also avoid unique girls being improperly included by irrelevant "cloning options/keep_generate_as" value
    def can_generate(girl, free=False, context="game", location=None): # Context can be 'game' or 'mix'. Location is an object
        if context == "game":

            # Unique girls may only generate if none other exists
            if girl.init_dict["cloning options/unique"]: # No other girl can generate after the first one
                #  Unique girl need not check for "cloning options/keep_generate_as", as there are no clones
                if free and girl.init_dict["background story/generate_as"] == "slave":
                    return False
                elif not free and girl.init_dict["background story/generate_as"] == "free":
                    return False
                elif location:
                    if girl.init_dict["background story/generate_in"] and girl.init_dict["background story/generate_in"] != "all":
                        for place in girl.init_dict["background story/generate_in"]:
                            if location.get_district().name.lower() not in girl.init_dict["background story/generate_in"] and location.name.lower() not in girl.init_dict["background story/generate_in"]:
                                return False
                #  Uses count_occurences last, only when absolutely necessary; significant time consumption
                if girl.count_occurences("all") >= 1:
                    return False

            #  Check other girls
            else: # elif girl.init_dict["cloning options/keep_generate_as"]
                if free and girl.init_dict["background story/generate_as"] == "slave":
                    return False
                elif not free and girl.init_dict["background story/generate_as"] == "free":
                    return False
                elif location:
                    if girl.init_dict["background story/generate_in"] and girl.init_dict["background story/generate_in"] != "all":
                        for place in girl.init_dict["background story/generate_in"]:
                            if location.get_district().name.lower() not in girl.init_dict["background story/generate_in"] and location.name.lower() not in girl.init_dict["background story/generate_in"]:
                                return False

        elif context == "mix":
            if girl.init_dict["background story/generate_as"] == "story": # story-only girls are not included in the mix UI
                return False

        return True
    #  </DougTheC>


    def multiple_choice_menu(prompt, menu_list, limit=9, nb=1): # Returns a list of nb choices, or the "back" string if cancelled

        _selected = []
        menu_list = list(menu_list) # Copying to avoid issues

        for _ in range(nb):
            _selected.append(long_menu(prompt + " (%i/%i)" % (len(_selected), nb), menu_list, limit))

            if _selected[-1] == "back":
                return "back"

            for it in menu_list:
                if it[1] == _selected[-1]: # Compares returned value with last selected choice
                    menu_list.remove(it) # Removing from list is okay because of break
                    break

        return _selected


    def long_menu(prompt, menu_list, limit=9): # Creates a menu with next/previous commands if menu has many items

        if len(menu_list) <= limit:
            return menu([(prompt, None)] + menu_list)

        idx = 0

        while True:
            end = idx + limit

            if end > len(menu_list):
                end = len(menu_list)

            if prompt:
                part_menu = [(prompt, None)] + menu_list[idx:end]
            else:
                part_menu = menu_list[idx:end]

            if idx > 0:
                part_menu += [("{i}前一个{/i}", "previous")]
            else:
                part_menu += [("{color=#AAA}{i}前一个{/i}", "previous")]

            if end < len(menu_list):
                part_menu += [("{i}下一个{/i}", "next")]
            else:
                part_menu += [("{color=#AAA}{i}下一个{/i}", "next")]

            r = menu(part_menu)

            if r == "next":
                if end < len(menu_list):
                    idx += limit

            elif r == "previous":
                if idx > 0:
                    idx -= limit

            else:
                return r

    def update_mods(): #! Replace messages

        global mod_traceback

        mod_traceback += "更新 mods... "

        # Checks if existing/active mods have been disabled

        undetected_mods = []

        for name, _ in persistent.mods.items():
            if name not in detected_mods.keys():
                undetected_mods.append(name)

        for name in undetected_mods:
            del persistent.mods[name]

            renpy.notify("Mod：" + name + " 已被移除。")
            mod_traceback += "\n" + "Mod：" + name + " 已被移除。"

        # Checks new mods or new mod versions

        for name, mod in detected_mods.items():

            # Finding new mod

            if name not in persistent.mods.keys():
                register_mod(mod)
                renpy.notify(mod.full_name + " 已添加。")

                mod_traceback += "\n" + "Mod：" + name + " 已添加。"

            # Finding new version (basic checks: version number and events lenght)

            elif mod.check_for_updates():
#                renpy.call_screen("OK_screen", title = mod.name + ": new version found", message = "A different version of this mod: " + mod.name + " has been found ([[mod.version]]). The mod has been reset.")
                register_mod(mod)
                renpy.notify(mod.full_name + " 已更新。")
                mod.active = True
                mod_traceback += "\n" + "Mod：" + name + " 已更新。"

            # Activating mod if it exists

            elif persistent.mods[name]["active"]:
                mod.active = True
#                if debug_mode:
#                    renpy.notify(mod.full_name + " has been activated.")
                mod_traceback += "\n" + "Mod：" + name + " 已激活。"

        # persistent.mods should now be updated to reflect all currently available mods

    def register_mod(mod):

        global mod_traceback

        persistent.mods[mod.name] = {"version" : mod.version, "check" : mod.get_check(), "active" : mod.active}

        mod_traceback += "\n" + "Mod：" + mod.name + " 已注册。"

#     def reset_mod(mod): # No longer required

#         if renpy.call_screen("yes_no", mod.full_name + " will be reset. Are you sure you want to proceed?\n\n{b}Warning{/b}: The mod will be reset, this might impact your saved games."):

#             mod.deactivate()
#             if detected_mods[mod.name]:
#                 # persistent.mods[mod.name] = detected_mods[mod.name]
#                 renpy.notify(mod.full_name + " has been reset.")
#             else:
#                 renpy.call_screen("OK_screen", title="Mod Not Found", message=event_color["bad"] % (mod.full_name + ": This mod couldn't be found among installed mods."))

    def reset_updated_games():

        global updated_games

        updated_games = defaultdict(bool)


    def get_events(type="any", _time=None):

        event_list = []

        if not _time:
            _time = calendar.time

        for ev in daily_events:
            if ev.happens(type):
                event_list.append(ev)

        return event_list


    def toggle_skip(ev_type):
        if persistent.skipped_events[ev_type]:
            persistent.skipped_events[ev_type] = False
        else:
            persistent.skipped_events[ev_type] = True


    def get_next_day_report(): # Compiles Yesterday's report for the Brothel screen

        msg = "你的青楼拥有 " + str(len(MC.girls)) + " 位女孩 (最多 " + str(brothel.bedrooms) + ")\n\n"

        working_girls = sum(1 for girl in MC.girls if girl.works_today(check_autorest=True))
        waitresses = sum(1 for girl in MC.girls if girl.works_today(check_autorest=True) and girl.job == "waitress")
        dancers = sum(1 for girl in MC.girls if girl.works_today(check_autorest=True) and girl.job == "dancer")
        masseuses = sum(1 for girl in MC.girls if girl.works_today(check_autorest=True) and girl.job == "masseuse")
        geishas = sum(1 for girl in MC.girls if girl.works_today(check_autorest=True) and girl.job == "geisha")
        whores = sum(1 for girl in MC.girls if girl.works_today(check_autorest=True) and girl.job == "whore")
        away = sum(1 for girl in MC.girls if girl.away)
        resting = sum(1 for girl in MC.girls if not girl.works_today(check_autorest=True) and not girl.away)

        msg += str(working_girls) + " 位女孩今晚要工作"

        msg += "\n{size=-2}" + __("- 女服务员: ") + event_color["good"] % str(waitresses) + "\n"
        msg += __("- 脱衣舞娘: ") + event_color["good"] % str(dancers) + "\n"
        msg += __("- 按摩技师: ") + event_color["good"] % str(masseuses) + "\n"
        msg += __("- 表演艺伎: ") + event_color["good"] % str(geishas) + "\n"
        msg += __("- 妓　　女: ") + event_color["good"] % str(whores) + "\n{/size}\n"

        if away > 1:
            msg += str(away) + " 位女孩进行外派任务或课程培训了\n\n"
        elif away > 0:
            msg += str(away) + " 位女孩进行外派任务或课程培训了\n\n"

        msg += str(resting) + " 位女孩今晚将在青楼休息\n\n"

        if farm.active:
            farm_training = sum(1 for girl in farm.girls if farm.programs[girl].target != "no training")
            farm_holding = sum(1 for girl in farm.girls if farm.programs[girl].target == "no training" and farm.programs[girl].holding != "rest")
            farm_resting = sum(1 for girl in farm.girls if farm.programs[girl].target == "no training" and farm.programs[girl].holding == "rest")

            msg += str(len(farm.girls)) + " 位女孩今晚将在农场度过"

            msg += "\n{size=-2}" + "- 在训练中：" + event_color["good"] % str(farm_training) + "\n"
            msg += "- 在待机中：" + event_color["good"] % str(farm_holding) + "\n{/size}\n"

            msg += str(farm_resting) + " 位女孩今晚将在农场休息"

        return msg


    def get_warnings():

        msg = ""

        # Escaped girls

        for girl in MC.escaped_girls:
            msg += event_color["bad"] % (girl.fullname + " 从青楼里逃走了，还没有找回来。\n")

        # Grumbling girls

        for girl in MC.girls:
            if girl.run_away_check():
                msg += event_color["a little bad contrast"] % (__("警告！") + girl.fullname + __(" 抱怨着她要离开这里。\n"))

        # Tired and hurt girls

        for girl in MC.girls:
            if girl.tired_check():
                msg += event_color["a little bad contrast"] % (girl.fullname + " 感到疲惫。\n")

            if girl.exhausted:
                msg += event_color["bad"] % (girl.fullname + " 累坏了，在充分休息之前不能工作。\n")

            if girl.hurt:
                msg += event_color["bad"] % (girl.fullname + " 受伤了，在恢复健康之前不能工作。\n")

        # News

        msg += "\n"

#         if game.token > 0:
#             msg += event_color["special"] % "You are ready to move to a new district.\n\n"

        if MC.skill_points > 0:
            msg += event_color["good"] % "你已经准备好升级了。\n"

        ready_to_level = sum(1 for girl in MC.girls if girl.upgrade_points >= 1)
        ready_to_perk = sum(1 for girl in MC.girls if girl.perk_points > 0)

        if ready_to_level > 1:
            msg += event_color["good"] % (str(ready_to_level) + " 位女孩有未分配的技能点。\n\n")
        elif ready_to_level > 0:
            msg += event_color["good"] % (str(ready_to_level) + " 位女孩有未分配的技能点。\n\n")

        if ready_to_perk > 1:
            msg += event_color["good"] % (str(ready_to_perk) + " 位女孩有未分配的天赋点。\n\n")
        elif ready_to_perk > 0:
            msg += event_color["good"] % (str(ready_to_perk) + " 位女孩有未分配的天赋点。\n\n")

        if shop.updated:
            msg += __("商店进了一批新货，看看有没有你想要的。\n\n")

        if slavemarket.updated:
            msg += __("奴隶市场来了一批新的奴隶，快去看看吧。\n\n")

        if quest_board.updated:
            msg += __("又有新的任务和培训课程发布了。\n\n")

        return msg


    def generate_customers(rep, use_adv=True): # Bring in the customers. use_adv is fed the number of working girls

        customers = []
        cust_nb, cust_nb_dict = count_customers(rep, randomize=True, use_adv=use_adv)

        # Log incoming customers

        cust_text = str(cust_nb) + " " + __("位顾客来到 ") + brothel.name + "。"
        log.add_report(event_color["good"] % cust_text)

        cust_text += "\n来自基础效果：%s" % plus_text(cust_nb - cust_nb_dict["advertising"] - cust_nb_dict["special"])

        # if cust_nb_dict["advertising"] and cust_nb_dict["special"]:
        #     # cust_text += __(" (including +") + str_int(cust_nb_dict["advertising"]) + __(" from advertising and +") + str_int(cust_nb_dict["special"]) + __(" from special effects)")
        #     cust_text += "\nAdvertising: %s\nSpecial effects: %s" % (plus_text(cust_nb_dict["advertising"]), plus_text(cust_nb_dict["special"]))
        if cust_nb_dict["advertising"]:
            # cust_text += __(" (including +") + str_int(cust_nb_dict["advertising"]) + __(" from advertising)")
            cust_text += "\n来自广告吸引：%s" % (plus_text(cust_nb_dict["advertising"]))
        elif cust_nb_dict["special"]:
            # cust_text += __(" (including +") + str_int(cust_nb_dict["special"]) + __(" from special effects)")
            cust_text += "\n来自特殊效果：%s" % (plus_text(cust_nb_dict["special"]))

        log.cust = cust_nb

        # Generate customers

        cust_list = []

        for pop in all_populations:
            for i in range(int(cust_nb_dict[pop.name])):
                cust_list.append(Customer(pop))

        renpy.random.shuffle(cust_list)

        for c in cust_list:
            log.add_report(c.name + __(" 来到青楼。他希望得到一个 ") + __(girl_related_dict[c.wants_entertainment]) + __(" 并且喜欢 ") + __(girl_related_dict[c.wants_sex_act]) + "。")

        return cust_list, cust_text, cust_nb_dict


    def count_customers(rep, randomize=True, use_adv=True): # Turn randomize off for UI display

        cust_nb_dict = defaultdict(int)
        cust_nb = 0

        base_points = rep/10
        adv_points = brothel.get_adv_attraction()
        special_points = brothel.get_effect("change", "customers", randomize=randomize) * district.rank + (brothel.get_effect("boost", "customers") - 1) * (base_points+adv_points)

        if use_adv:
            cust_points = base_points + adv_points + special_points
        else: # Advertising does not apply if the brothel is closed
            cust_points = base_points + special_points

        spent_points = 0

        available_pop = sorted([pop for pop in all_populations if pop.weight > 0], key = lambda x : x.weight, reverse=True)

        weighted_total = sum((p.weight*p.rank) for p in available_pop)

        # First, creates a balanced mix of customers according to population cost and weight
        for pop in available_pop:
            cust_nb_dict[pop.name] += math.ceil(cust_points * pop.weight / weighted_total)
            spent_points += cust_nb_dict[pop.name] * pop.rank
            if spent_points > cust_points and cust_nb_dict[pop.name] > 0:
                cust_nb_dict[pop.name] -= 1
                spent_points -= pop.rank
            cust_nb += cust_nb_dict[pop.name]

        # Distribute the remaining points to the lowest rank population
        if cust_points > spent_points:
            pop = sorted(available_pop, key = lambda x : x.rank)[0]
            if pop.rank <= cust_points - spent_points:
                cust_nb_dict[pop.name] += (cust_points - spent_points) // pop.rank
                cust_nb += (cust_points - spent_points) // pop.rank

        # Logs advertising and special effect customers (rounded down to avoid potential confusion)

        if cust_points:
            cust_nb_dict["advertising"] = round_int(cust_nb * adv_points // cust_points)
            cust_nb_dict["special"] = round_int(cust_nb * special_points // cust_points)

        # The brothel is garanteed one free customer no matter what
        cust_nb_dict[available_pop[0].name] += 1
        cust_nb += 1

        return round_int(cust_nb), cust_nb_dict # returns customer total and a dictionary including the number of customers for each type




#     def count_customers_old(rep, girls=[]):

#         cust_nb = 0
#         total_cust_value = 0

#         while total_cust_value < rep: # Each new customer "costs" 1 more point of rep times current rank
#             cust_nb += 1
#             total_cust_value += cust_nb * district.rank

#         extra_cust = sum(g.get_effect("change", "customers", raw=True) for g in girls) + brothel.get_effect("change", "customers")

#         return int(cust_nb), int(extra_cust)


    def change_brothel(): # change brothel and bg bro

        global brothel
        global bg_bro

        # Create new brothel
        newbrothel = copy.deepcopy(blist[game.chapter])

        # Carry name and furniture over to the new brothel
        newbrothel.setup(brothel.name, brothel.furniture, brothel.current_building, brothel.started_building, brothel.master_bedroom.girls, free_room=district.room)

        # Switch brothels
        brothel = newbrothel

        # Set BG
        bg_bro = "bg brothel" + str(game.chapter)

        reset_girl_jobs()
        update_effects("brothel")

    def change_district(chosen_district, free=False): # Change district

        global district
    #       game.token = 0

        game.blocked_districts.append(district)
        district = chosen_district

        if not free:
            MC.gold -= blist[game.chapter].cost
            renpy.play(s_gold, "sound")

        # Refresh
        calendar.updates(new_district=True)
#         refresh_available_locations()

    def get_starting_furniture(chapter): # lower chapter furniture is built from the beginning
        for furn in all_furniture:
            if furn.chapter < chapter:
                furn.build(message=False)

    def get_girlpack_rating(girl=None, path=None, forced=False):

        if path:
            girl = Girl()
            girl.path = path

        if rating_dict[girl.path] and not forced:
            d = rating_dict[girl.path]
        else:
#            renpy.say("", "Evaluate " + path)
            d = girl.evaluate_girlpack()
            rating_dict[girl.path] = d

        score = d["main cover score"] * 5 + d["optional cover score"] * 2

        if score >= 6:
            rating = "A"
            col = "special"
        elif score >= 5:
            rating = "B"
            col = "good"
        elif score >= 4:
            rating = "C"
            col = "a little good"
        elif score >= 3:
            rating = "D"
            col = "average"
        elif score >= 2:
            rating = "E"
            col = "a little bad"
        else:
            rating = "F"
            col = "bad"

        if d["main diversity average"] > 5:
            rating += "+"
        elif d["main diversity average"] < 3:
            rating += "-"

        ttip = "女孩包评级：%s, " % rating
        #<Chris12 PackState>
        #ttip += "\nPictures: " + str(len(girl.pics))
        ttip += "图片: " + str(len(GirlFilesDict.get_pics(girl.path)))
        #</Chris12 PackState>
        ttip += "\n主要标签得分: " + str(round_int(d["main cover score"]*100)) + "% (" + str(round(d["main diversity average"], 1)) + " picture/existing tag)"
        ttip += "\n可选标签得分: " + str(round_int(d["optional cover score"]*100)) + "% (" + str(round(d["optional diversity average"], 1)) + " picture/existing tag)"

        return event_color[col] % rating, ttip


    def is_imgfile(file, video=True):
        if is_string(file):
            if (file[-4:].lower() in IMGFORMATS or file[-5:].lower() in IMGFORMATS):
                return True
            if video and is_videofile(file):
                return True
        return False

    def is_videofile(file):
        if is_string(file):
            if (file[-4:].lower() in VIDEOFORMATS or file[-5:].lower() in VIDEOFORMATS):
                return True
        return False

    def list_imgfiles(path, strict=True): # Returns a list of all image files in the given folder (and sub-folders if strict is set to False)

        if strict:
            return [f for f in renpy.list_files() if f.startswith(path) and is_imgfile(f) and f.count("/") == path.count("/")]

        else:
            return [f for f in renpy.list_files() if f.startswith(path) and is_imgfile(f)]

    def get_exchange_rate(source, target): # Where source, target are "gold" or a Resource object

        if source == "gold":
            return 1 * game.get_diff_setting("resources")/(resource_gold_value[target.rank] * calendar.get_discount(source, target))

        elif target == "gold":
            return resource_gold_value[source.rank]*resource_sell_discount * calendar.get_discount(source, target) * game.get_diff_setting("gold")

        else:
            return resource_base_exchange_rate[source.rank][target.rank]  * calendar.get_discount(source, target) * game.get_diff_setting("resources")



#### EFFECT MANAGEMENT ####
## Most skills, items, spells, etc. cause effects. Effects are applied to a target: MC, slaves and girls, the brothel...

    def get_effect(thing, type, target, custom_scale=("factor", 0), change_cap=False, iterate=False, randomize=True):
        ## Will return the cumulated value of all applicable effects if test is passed
        # custom_scale is a tuple ('factor name', 'value') which is used for specific perks
        # change_cap=True will only return Effects with the change_cap attribute as True (which means it affects stat min and max)
        # Boost effects are now additive. Let's hope nothing blows up.
        # Special effects return their value (if found), 0 if not found

        # Choose result type

        if type == "special":
            result = 0

        elif type in ("boost"):
            # result is a % expressed as a float. 1.0 (100%) means no positive or negative effect occur.
            result = 1.0
        else:
            # result is a number expressed as int or float. 0 means no positive or negative effect occur.
            result = 0

        # Checks a dictionary to optimize performance (the dictionary is updated through the update_effects function)
        if iterate: # For single items only
            effect_list = [eff for eff in thing.effects if type.lower() == eff.type.lower() and target.lower() == eff.target.lower()]
        else: # Includes world-scope effects
            effect_list = thing.effect_dict[(type.lower(), target.lower())] + game.world_effect_dict[(type.lower(), target.lower())]

        for effect in effect_list:

            # Out of scope effects will be ignored to avoid double proc

            if (effect.scope == "world" and thing not in (brothel, farm, game)) or (effect.scope == "brothel" and thing != brothel) or (effect.scope == "farm" and thing != farm) or (effect.scope == "city" and thing != game):
                continue # Jumps to the next effect in the for loop

            #### APPLIES SCALING EFFECTS ####

            if effect.scales_with:
                if effect.source: # This is used for scoped effects to track the original source and scale accordingly
                    factor = get_scale_factor(effect.source, effect.scales_with, custom_scale=custom_scale)
                else:
                    factor = get_scale_factor(thing, effect.scales_with, custom_scale=custom_scale)
            else:
                factor = 1

            #### TESTING EFFECT PROC CHANCE ####

            chance = effect.chance

            if target != "effect chance": # Applies boost to effect chance if there is one
                if chance < 0.5: # Hard-coded: Effect_chance boost is capped at 50%
                    chance *= (1 + get_effect(thing, "special", "effect chance", iterate=iterate, randomize=randomize)) # Why special and not boost? Description related?
                    if chance > 0.5:
                        chance = 0.5
                chance *= get_effect(thing, "boost", target + " chance", iterate=iterate, randomize=randomize)

            if chance < 1:
                game.chance_log = chance
                if renpy.random.random() > chance or not randomize:
                    continue # Jumps to the next effect in the for loop

            if change_cap and not effect.change_cap:
                continue # Jumps to the next effect in the for loop

            #### ADDING EFFECT VALUE TO RESULT ####

            if effect.dice: # Adds the value of a dice with 'effect.value' faces
                if factor and randomize: # Warning: Factor affects the number of faces the dice has. It should never be a fraction in that case.
                    try:
                        result += dice(effect.value * factor, effect.dice) # New: dice property can be an integer
                    except:
                        result += dice(effect.value * factor)
                else:
                    result += effect.value * factor/2

            else:
                try:
                    result += effect.value * factor
                except:
                    result = effect.value # For special effects that do not use numeric values. Only one active effect returns its value. For now, this type of effects must be checked for with 'raw' activated.

        if type in ("boost") and result < 0:
            # Boost results can never go negative to avoid unintended behavior
            return 0.0

        return result

    def add_effects(thing, effects, apply_boost=False, spillover=False, expires=False):
        ## This function adds effects to a target (thing)

        effects = make_list(effects, obj_type = Effect)
        c = None
        scope_list = [] # Stores affected scope to optimize recourse to update_effect()

        for effect in effects:

            # If the effect will affect dress and equipment effects, the equipment is removed BEFORE applying the effect to be equipped back after.

            if effect.type == "boost" and effect.target in all_equipement_types:
                it_list = []

                # Removes items first
                for it in thing.equipped:

                    if it.type.name.lower() == effect.target:
                        it_list.append(it)
                        thing.unequip(it)

            # Applies effect

            #### GAIN AND INSTANTS ####
            ## Gain and Instant effects are applied immediately and not added to active effects. They cannot expire.
            ## Gained value is returned (note: will not work properly if there are more than one effects)
            ## Gain effects affect a character's stats or attributes. Instant effects affect the world or the brothel. They work the same and are mostly hardcoded.

            if effect.type in ("gain", "instant"):

                if effect.scope == "brothel":
                    for girl in MC.girls:
                        c = effect.gain(girl, apply_boost=apply_boost, spillover=spillover)
                elif effect.scope == "farm":
                    for girl in farm.girls:
                        c = effect.gain(girl, apply_boost=apply_boost, spillover=spillover)
                elif effect.scope == "city":
                    for girl in game.free_girls:
                        c = effect.gain(girl, apply_boost=apply_boost, spillover=spillover)
                elif effect.scope == "world":
                    for girl in MC.girls + farm.girls + game.free_girls:
                        c = effect.gain(girl, apply_boost=apply_boost, spillover=spillover)
                else:
                    c = effect.gain(thing, apply_boost=apply_boost, spillover=spillover)

            #### PERSONALITY EFFECTS ####
            ## This forces a personality on a girl (mostly associated with traits). This cannot override the .ini file 'Always' and 'Never' settings.
            ## Personality effects are permanent and are not added to active effects.

            elif effect.type == "personality":
                thing.generate_personality(effect.target)
                c = effect.target


            #### OTHER EFFECTS ####

            else:
                thing.effects.append(effect)
                thing.effect_dict[(effect.type, effect.target)].append(effect) # Stores active effects in a dictionary for faster access
                if effect.scope:
                    scope_list.append(effect.scope)

                # Naturist effect
                if effect.type == "special" and effect.target == "naked":
                    if thing not in game.free_girls: # Free girls will not reveal their naturist streak immediately
                        thing.naked = True

            # Re-equip items AFTER the boost effect has been applied
            if effect.type == "boost" and effect.target in all_equipement_types:
                for it in it_list:
                    thing.equip(it)

        if expires:
            calendar.set_alarm(expires, StoryEvent(label = "effect_expired", call_args = [thing, effects]))

        if scope_list:
            update_effects(scope_list)

        return c


    def remove_effects(thing, effects):
        ## This function removes effects from a target (thing)

        effects = make_list(effects, obj_type = Effect)
        scope_list = [] # Stores affected scope to optimize recourse to update_effect()

        for effect in effects:

            #### REMOVE EQUIPMENT BOOST ####
            ## If the effect will affect dress and equipment effects, the equipment is removed BEFORE applying the effect to be equipped back after.

            if effect.type == "boost" and effect.target in all_equipement_types:
                it_list = []

                # Removes items first
                for it in thing.equipped:

                    if it.type.name.lower() == effect.target:
                        it_list.append(it)
                        thing.unequip(it)

            # Remove effect

            if effect in thing.effects:
                thing.effects.remove(effect)
            if effect in thing.effect_dict[(effect.type, effect.target)]:
                thing.effect_dict[(effect.type, effect.target)].remove(effect)
            if effect.scope:
                scope_list.append(effect.scope)

            if effect.type == "boost" and effect.target in all_equipement_types:
                # Re-equip items
                for it in it_list:
                    thing.equip(it)

        if scope_list:
            update_effects(scope_list)


    def get_scale_factor(thing, scales_with, custom_scale=("factor", 0), raw=False):

        if scales_with in ("strength", "spirit", "charisma", "speed"):
            factor = MC.get_stat(scales_with, raw=raw)
        elif scales_with == "defense":
            factor = thing.get_defense()
        elif scales_with in ("rep", "reputation"):
            factor = thing.rep
        elif scales_with == "rank":
            factor = thing.rank
        elif scales_with == "equipped": # Counts every piece of equipment
            factor = len(thing.equipped)
        elif scales_with == "chapter":
            factor = game.chapter
        elif scales_with == "district":
            factor = district.rank
        elif scales_with == custom_scale[0]: # Custom scale
            factor = custom_scale[1]
        else:
            factor = 0 # 'scales_with' effects will be ignored if no scale factor is found (avoids unwarranted bonuses)

        return factor

    def update_effects(scope_list=("world", "brothel", "farm", "city")): # Updates all world-affecting effects.

        if "world" in scope_list:
            game.world_effect_dict = defaultdict(list)

            for source in ([g for g in (MC.girls + farm.girls) if not (g.away or g.hurt or g.exhausted)] + [f for f in brothel.furniture if f.active] + [MC, MC.current_trainer, calendar.moon]):
                if source:
                    for effect in source.effects:
                        if effect.scope == "world":
                            game.world_effect_dict[effect.type, effect.target].append(effect)
                            effect.source = source # Tracks source (sometimes useful for applying scaling effects)

        if "brothel" in scope_list:
            brothel.effect_dict = defaultdict(list)

            for source in ([g for g in MC.girls if not (g.away or g.hurt or g.exhausted)] + [f for f in brothel.furniture if f.active] + [MC, MC.current_trainer, calendar.moon]):
                if source:
                    for effect in source.effects:
                        if effect.scope == "brothel":
                            brothel.effect_dict[effect.type, effect.target].append(effect)
                            effect.source = source # Tracks source (sometimes useful for applying scaling effects)

        if "farm" in scope_list:
            farm.effect_dict = defaultdict(list)

            for source in ([g for g in farm.girls if not (g.away or g.hurt or g.exhausted)] + [f for f in brothel.furniture if f.active] + [MC, MC.current_trainer, calendar.moon]):
                if source:
                    for effect in source.effects:
                        if effect.scope == "farm":
                            farm.effect_dict[effect.type, effect.target].append(effect)
                            effect.source = source # Tracks source (sometimes useful for applying scaling effects)

        if "city" in scope_list:
            game.effect_dict = defaultdict(list)

            for source in ([f for f in brothel.furniture if f.active] + [MC, MC.current_trainer, calendar.moon]):
                if source:
                    for effect in source.effects:
                        if effect.scope == "city":
                            game.effect_dict[effect.type, effect.target].append(effect)
                            effect.source = source # Tracks source (sometimes useful for applying scaling effects)

        # brothel.effect_dict = defaultdict(list)
        # farm.effect_dict = defaultdict(list)
        # game.effect_dict = defaultdict(list)
        #
        # for source in ([g for g in MC.girls if not (g.away or g.hurt or g.exhausted)] + [f for f in brothel.furniture if f.active] + [MC, MC.current_trainer, calendar.moon]):
        #     if source:
        #         for effect in source.effects:
        #             if effect.scope == "brothel" or effect.scope == "world":
        #                 brothel.effect_dict[effect.type, effect.target].append(effect)
        #                 effect.source = source # Tracks source (sometimes useful for applying scaling effects)
        #             elif effect.scope == "farm" or effect.scope == "world":
        #                 farm.effect_dict[effect.type, effect.target].append(effect)
        #                 effect.source = source # Tracks source (sometimes useful for applying scaling effects)
        #             elif effect.scope == "city" or effect.scope == "world":
        #                 game.effect_dict[effect.type, effect.target].append(effect)
        #                 effect.source = source # Tracks source (sometimes useful for applying scaling effects)


    def count_lines(s, char_per_line):

    # Kills unwanted format characters to avoid artificial character count (rough)
        s = s.replace("{b}", "")
        s = s.replace("{/b}", "")
        s = s.replace("{i}", "")
        s = s.replace("{/i}", "")
        s = s.replace("{color=", "")
        s = s.replace("{/color}", "")

        lines = s.split("\n")

        total = len(lines)

        for line in lines:
            total += len(line) // char_per_line

        if s.endswith("\n"):
            total -= 1

        return total

    def change_autorest(direction="+"):
        global autorest_limit

        if direction == "+" and autorest_limit < 100:
            autorest_limit += 5
        elif direction == "-" and autorest_limit > 0:
            autorest_limit -= 5


    def get_plus_rating(chg, type="stat"):

        if type == "stat":
            if chg > 3:
                r = "+++"
            elif chg > 1:
                r = "++"
            elif chg > 0.2:
                r = "+"
            elif chg >= -0.2:
                r = "="
            elif chg >= -1:
                r = "-"
            elif chg >= -3:
                r = "--"
            else:
                r = "---"

        elif type == "pref":
            if chg > 250:
                r = "+++"
            elif chg > 100:
                r = "++"
            elif chg > 5:
                r = "+"
            elif chg > -5:
                r = "="
            elif chg >= -100:
                r = "-"
            elif chg >= -250:
                r = "--"
            else:
                r = "---"

        return "{color=" + color_dict[r] + "}" + r + "{/color}"

    def load_girl_status(girls): # Stores statuses in a dictionary that is refreshed every interaction
        s_dict = {}

        for girl in girls:
            s_dict[girl] = girl.get_status()
            s_dict[girl, "summary"] = girl.get_status_summary()

        return s_dict

    def return_ddict_list():
        return defaultdict(list)

    def add_mix():
        new_mix = renpy.input("输入要创建的混合包的名称")

        if new_mix in (persistent.girl_mix.keys()):
            renpy.notify("{color=[c_red]}[new_mix] 已经存在。{/color}")
        else:
            persistent.girl_mix[new_mix] = []
            persistent.active_mix = new_mix
        return

    def add_all_to_mix(mix):
        persistent.girl_mix[mix] = list(persistent.girl_packs)

    def remove_all_from_mix(mix):
        persistent.girl_mix[mix] = []

    def delete_mix(mix):
        if mix == "default":
            renpy.notify("不能删除“默认”组合。")
        elif mix in persistent.girl_mix.keys() and renpy.call_screen("yes_no", "你确定你要删除这个女孩的组合吗?"):
            del persistent.girl_mix[mix]
            if persistent.active_mix == mix:
                persistent.active_mix = "default"

    def prepare_not_tags(girl, act, fix_list=None, farm=False):

        if fix_list == None: fix_list = []

        not_tags = ["swimsuit", "fight", "profile", "date", "rest"] # Avoids showing profile and other inappropriate pics (unless the not clause is dropped)

        if act == "naked":
            not_tags += all_sex_acts
            if "masturbation" in fix_list:
                not_tags.remove("service")

        if act != "group" and not farm:
            not_tags.append("group")
        if act != "bisexual" and not farm:
            not_tags.append("bisexual")

        if "public acts" not in fix_list:
            not_tags.append("public")
        if "cosplay" not in fix_list and "roleplay" not in fix_list: # Disable improper job pics unless cosplay/roleplay is on
            not_tags += [j for j in all_jobs if girl.job != j]
            not_tags.append("cosplay")

        return not_tags


    def parse_dice_formula(formula):
        def factor(f):
            g = f.split('d')
            if len(g)==1:
                return int(f)
            return sum(random.randint(1, int(g[1]) if g[1] else 6) for i in range(int(g[0]) if g[0] else 1))

        def term(t):
            p = t.split('*')
            return factor(p[0]) if len(p)==1 else factor(p[0])*factor(p[1])

        return sum(term(x) for x in formula.split('+'))

    def plus_minus(value): # Returns a string value with a + or - sign (no sign if = 0)
        return plus_text(float(value))

    def percent_text(value, use_plus=True):
        percentage = round_int(value * 100)

        if use_plus:
            return "%s%%" % plus_minus(percentage)
        else:
            return "%s%%" % str(percentage)

    def make_match_list_from_ent_dict(ent_dict, crazy_dict):
        match_list = []

        for girl, customers in ent_dict.items():
            for cust in customers:
                match_list.append((girl, cust, girl.job))

        for girl, customers in crazy_dict.items():
            for cust in customers:
                match_list.append((girl, cust, girl.job))

        return match_list

    def make_match_list_from_wh_list(wh_list, crazy_dict):
        match_list = []

        for girls, customers, act in wh_list:
            for cust in customers:
                match_list.append((girls[0], cust, act))

        for girl, customers in crazy_dict.items():
            for cust in customers:
                match_list.append((girl, cust, cust.wants_sex_act))

        return match_list


    def job_matchmaking(available_girls, customers, ent_dict=None, job_cap=None, ticket_dict=None):
        game.mm_log = ""

        ### Returns ent_dict as {girl : [affected customers]}, a list of unattended customers, job_cap and ticket_dict

        if not ent_dict:
            ent_dict = defaultdict(list)
        if not ticket_dict:
            ticket_dict = {}

        #### SANITY CHECKS ####

        # Aborpts if no girls or no customers
        if not available_girls or not customers:
            game.mm_log += "\nNo girls or cust left"
            return ent_dict, customers, job_cap, ticket_dict

        # Init job caps (to avoid going over the room limit)
        if not job_cap:
            game.mm_log += "\nInit job cap"
            job_cap = defaultdict(int)
            for job in all_jobs:
                job_cap[job] = min(sum(g.get_max_cust_served() for g in available_girls if g.job == job), brothel.rooms[job_room_dict[job]].cust_limit)

        # Aborpts if no job cap is left
        if sum(job_cap[j] for j in all_jobs) <= 0:
            game.mm_log += "\nNo job cap left"
            return ent_dict, customers, job_cap, ticket_dict

        #### PREPARING ####

        ## Creating a dictionary of girl tickets
        if not ticket_dict:
            game.mm_log += "\nNew ticket dict"
            # ticket_dict = defaultdict(lambda: defaultdict(list)) # nested dictionary - changed because it breaks Renpy saves
            ticket_dict = defaultdict(list)

            # Adding x tickets per girl where x is max_customers_served
            for girl in available_girls:
                ticket_dict[girl.rank, girl.job] += [girl] * girl.get_max_cust_served()

            # Shuffling girl tickets
            for rank in range(1, 6):
                for job in all_jobs:
                    renpy.random.shuffle(ticket_dict[rank, job])

        ## Set up rank lookup order during matchmaking
        # Nearby Ranks are checked first
        rank_lookup_dict = {1 : [2, 3, 4, 5], 2 : [3, 1, 4, 5], 3 : [4, 2, 5, 1], 4 : [5, 3, 2, 1], 5 : [4, 3, 2, 1]}

        ## Preparing customers
        # Higher rank customers are prioritized (not by budget, to provide some variation and keeping rich/broke customers relevant)
        customers.sort(key= lambda x : x.rank, reverse=True)

        # Using a separate list from customers to avoid messing the 'for' loop
        leftover_customers = list(customers)


        #### MATCHMAKING ####

        # If the player is using the 'Prioritize same rank customers' setting
        if game.matching_priority == "rank":
            order = ["wanted same rank", "unwanted same rank", "wanted other rank", "unwanted other rank"]

        # If the player is using the 'Prioritize customer preferences' setting
        elif game.matching_priority == "act":
            order = ["wanted same rank", "wanted other rank", "unwanted same rank", "unwanted other rank"]

        for step in order:
            if step not in ["wanted same rank", "wanted other rank", "unwanted same rank", "unwanted other rank"]:
                raise AssertionError("Step %s is not recognized." % step)

            game.mm_log += "\nBegin step %s: %s customers" % (step, str(len(customers)))
            for cust in customers:
                if step.endswith("same rank"):
                    rank_list = [cust.rank]
                else:
                    rank_list = rank_lookup_dict[cust.rank]

                if step.startswith("wanted"):
                    job_list = [cust.wants_entertainment]
                else:
                    job_list = list(all_jobs)
                    job_list.remove(cust.wants_entertainment)

                for rank in rank_list:
                    for job in job_list:
                        if job_cap[job] <= 0: # Skip if no room is available
                            game.mm_log += "\nSkipping %s because it's full" % job
                            continue # Try another job

                        if not ticket_dict[rank, job]: # Skip if no girl ticket is available
                            game.mm_log += "\nSkipping %s because no tickets left" % job
                            continue # Try another job

                        # Assigns a girl ticket
                        for girl in ticket_dict[rank, job]:
                            # Checks if the girl will accept this customer according to her individual settings
                            if not girl.refused_populations[cust.pop.name]:
                                game.mm_log += "\nCustomer #%s has been assigned" % customers.index(cust)
                                ent_dict[girl].append(cust)
                                leftover_customers.remove(cust)
                                job_cap[job] -= 1
                                try:
                                    ticket_dict[rank, job].remove(girl) # This breaks the loop, but hopefully no side effects
                                except:
                                    raise AssertionError(ticket_dict[rank, job])
                                break # Exit girl ticket loop
                        else:
                            continue # Try another job
                        break # Exit job loop
                    else:
                        continue # Try another rank
                    break # Exit rank loop

            game.mm_log += "\nEnd of step %s, %s customers have been assigned." % (step, str(len(customers)-len(leftover_customers)))
            customers = list(leftover_customers)

        return ent_dict, leftover_customers, job_cap, ticket_dict


    def wh_matchmaking(whores, customers):
        # Returns a list of tuples (girls, customers, sex_act) and a list of unattended customers

        game.mm_log = "" # Leftover from debugging, remove this once the function is stable

        #### SANITY CHECKS ####

        ## Creating local lists to avoid problems
        _whores = list(whores)
        _customers = list(customers)
        _wh_list = []

        # Aborpts if no girls or no customers
        if not _whores or not _customers:
            game.mm_log += "ENDED: No whores or no customers"
            return _wh_list, _customers

        #### PREPARING ####

        ## Preparing customers
        # Higher rank customers are prioritized (not by budget, to provide some variation and keeping rich/broke customers relevant)
        customers.sort(key= lambda x : x.rank, reverse=True)

#         #<Chris Job Mod: Sorting Customers by Entertainment Score>
#         if game.has_active_mod("chrisjobmod"):
#             if entertainment_bonus_strength != 0:
#                 customers.sort(key=lambda x: x.entertainment_score, reverse=True)
#         #</Chris Job Mod>

        # Using a separate list from customers to avoid messing the 'for' loop
        leftover_customers = list(_customers)

        #### MATCHMAKING ####

        # If the player is using the 'Prioritize same rank customers' setting
        if game.matching_priority == "rank":
            order = ["wanted same rank", "unwanted same rank", "wanted other rank", "unwanted other rank"]

        # If the player is using the 'Prioritize customer preferences' setting
        elif game.matching_priority == "act":
            order = ["wanted same rank", "wanted other rank", "unwanted same rank", "unwanted other rank"]

        for step in order:
            game.mm_log += "\n\nStep: %s (%s whores available)\n" % (step, len(_whores))
            # Customers get their picks in descending order of rank
            for cust in _customers:
                game.mm_log += "\n%s came " % cust.name
                # Aborpts if no girls are left
                if not _whores:
                    game.mm_log += "but found no whore left."
                    break # Stops matchmaking

                # Ignore grouped customers
                if cust.group:
                    game.mm_log += "and joined a GROUP."
                    leftover_customers.remove(cust)
                    continue # Move on to the next customer

                # Filter available girls
                base_available_girls = [g for g in _whores if g.interactions > 0 and not g.refused_populations[cust.pop.name] and g.does_anything()]

                available_girls = list(base_available_girls) # Keeps track of base_available_girls to increase the bisexual girl pool

                if step.endswith("same rank"):
                    available_girls = [g for g in available_girls if g.rank == cust.rank]

                if step.startswith("wanted"):
                    available_girls = [g for g in available_girls if g.does[cust.wants_sex_act]]

                if not available_girls:
                    game.mm_log += "but no girl was available at this step."
                    continue # Move on to the next customer

                # Choosing the best girl for this customer

                girl, sex_act = cust.choose_girl(available_girls)
                if not girl:
                    raise AssertionError("Error: A customer failed to pick a girl.")

                game.mm_log += "and chose %s for %s." % (girl.fullname, sex_act)

                leftover_customers.remove(cust)

                ## Group and bisexual matchmaking

                check_order = ["bisexual", "group"]
                c_list = [cust]
                g_list = [girl]

                if girl.archetypes["The Escort"].unlocked and not girl.archetypes["The Courtesan"].unlocked: # Escort tree favors 'group' acts
                    check_order = ["group", "bisexual"]
                elif girl.archetypes["The Courtesan"].unlocked and not girl.archetypes["The Escort"].unlocked: # Courtesan tree favors 'bisexual' acts
                    pass
                else: # Randomize if both trees are active, or none of them
                    renpy.random.shuffle(check_order)

                for check in check_order:

                    # Group girls may bring in up to 2 more customers
                    if check == "group":

                        if girl.does["group"] and _customers.index(cust) < len(_customers)-1:
                            if girl.get_effect("special", "group"): # Group has a random chance of triggering
                                c_list.append(_customers[_customers.index(cust)+1]) # gets the next customer in the queue

                                if girl.has_perk("Orgy") and _customers.index(cust) < len(_customers)-2:
                                    if girl.get_effect("special", "orgy"): # Orgy has a random chance of triggering
                                        c_list.append(_customers[_customers.index(cust)+2])

                                cust.group = len(c_list)
                                for c in c_list[1:]: # Sharing reason and preference between customers to avoid incoherences
                                    c.group = len(c_list)
                                    c.reason = cust.reason
                                    c.wants_sex_act = cust.wants_sex_act

                                break # This is needed to avoid group and bisexual proccing together (could be something to allow later)

                    # Bisexual girls may bring in a second bisexual girl
                    elif check == "bisexual":
                        if girl.does["bisexual"] and len(c_list) == 1:
                            if girl.get_effect("special", "bisexual"):  # Bis has a random chance of triggering
                                for girl2 in base_available_girls: # The second girl ncan be chosen from the larger pool regardless of rank/act
                                    if girl2 != girl and girl2.does["bisexual"] and girl2.does[sex_act]:
                                        g_list.append(girl2)
                                        game.mm_log += " She brought a friend (%s)." % girl2.fullname
                                        break

                                break # This is needed to avoid group and bisexual proccing together

                # Use interactions

                for girl in g_list:
                    spent_interactions = 1

                    # Uses 2 interactions if girl is working half a shift
                    spent_interactions *= (100//girl.workdays[calendar.get_weekday()])

                    # Uses 2 interactions if w&w
                    if girl.work_whore and girl.job in all_jobs:
                        spent_interactions *= 2

                    girl.interactions -= spent_interactions
                    game.mm_log += " (%s has spent %s interactions and has %s left)" % (girl.fullname, spent_interactions, girl.interactions)

                    if girl.interactions <= 0:
                        _whores.remove(girl) # Not strictly necessary, but shortens the next loop
                        game.mm_log += " (%s has no interactions left and was REMOVED)" % girl.fullname

                # Update _wh_list
                _wh_list.append([g_list, c_list, sex_act])

            # Prepare the next step
            _customers = list(leftover_customers)

        return _wh_list, leftover_customers

## Difficulty settings
    def unlocking_extras(final=False):
        global unlocked_shops

        game.update_achievements()

        if game.starting_gold:
            if int(game.starting_gold) > starting_gold:
                game.achievements = False
                # renpy.notify("gold")

        if starting_chapter > 1 or [x for x in extras_dict.values() if x]:
            game.achievements = False
            # renpy.notify("chapter")

            if starting_chapter > 1:
                story_flags["c1_path"] = c1_path

        if extras_dict["farm"]:
            game.achievements = False
            if final:
                farm.activate()
                farm_firstvisit = False
                gizel_name = "Gizel"
            # renpy.notify("farm")

        if extras_dict["carpenter"]:
            game.achievements = False
            if final:
                NPC_carpenter.active = True
                story_flags["found wagon"] = True
                story_flags["met carpenter"] = True
                carpenter_name = "Iulia"
            # renpy.notify("carpenter")

        if extras_dict["locations"]:
            game.achievements = False
            if final:
                thieves_guild.secret = False
                thieves_guild.action = True
            # renpy.notify("loc")

        if extras_dict["shops"]:
            game.achievements = False
            if final:
                farmland.action = True
                sewers.action = True
                junkyard.action = True
                unlocked_shops += [m for m in [NPC_goldie, NPC_willow, NPC_gina] if m not in unlocked_shops]

                if extras_dict["shops"] >= 2:
                    harbor.action = True
                    arena.action = True
                    prison.action = True
                    exotic_emporium.action = True
                    market.action = True
                    unlocked_shops += [m for m in [NPC_stella, NPC_ramias, NPC_gurigura, NPC_giftgirl] if m not in unlocked_shops]

                if extras_dict["shops"] >= 4:
                    botanical_garden.action = True
                    library.action = True
                    pilgrim_road.action = True
                    unlocked_shops += [m for m in [NPC_riche, NPC_katryn, NPC_twins] if m not in unlocked_shops]

            # renpy.notify("shops")

        if extras_dict["resources"]:
            game.achievements = False
            if final:
                if extras_dict["resources"] >= 2:
                    shipyard.action = True
                    stables.action = True
                    beach.action = True
                if extras_dict["resources"] >= 4:
                    old_ruins.action = True
                    hanging_gardens.action = True
                    guild_quarter.action = True
                if extras_dict["resources"] >= 6:
                    falls.action = True
            # renpy.notify("resources")

        if extras_dict["trainers"]:
            game.achievements = False
            if final:
                MC.trainers.append(NPC_maya)
                MC.trainers.append(NPC_lieutenant)
                MC.trainers.append(NPC_captain)
                MC.trainers.append(NPC_renza)
                MC.trainers.append(NPC_satella)
                MC.trainers.append(NPC_bast)
            # renpy.notify("trainers")

    def update_available_mixes():
        available_mixes = persistent.girl_mix.keys()

        for mix in persistent.game_mixes:
            if mix not in available_mixes:
                renpy.notify("Removing %s from game mixes" % mix)
                persistent.game_mixes.remove(mix)

        if len(available_mixes) == 1 or len(persistent.game_mixes) == 0:
            persistent.game_mixes = ["default"]

        return list(available_mixes)

    def init_tax(): # Unique variables for the taxgirl NPC
        NPC_taxgirl.MC_income = 0
        NPC_taxgirl.current_tax = 0
        NPC_taxgirl.time_pressure_modifier = 0.0
        NPC_taxgirl.active = False

    def calculate_tax(monthly_income): # Called once a month when announcing next tax

        monthly_income = NPC_taxgirl.MC_income

        # STEP 1: Check tax eligibility

        if NPC_taxgirl.MC_income < tax_brackets[0][0] * 28:
            return 0 # You are too poor to pay taxes. Hurray?

        # STEP 2: Calculate raw tax

        previous_bracket = 0
        total = 0

        for bracket, rate in tax_brackets:
            bracket *= 28
            rate += tax_chapter_penalty[game.chapter] + game.get_diff_setting("tax rate") + NPC_taxgirl.time_pressure_modifier

            if rate < 0: # Tax rate cannot be negative
                rate = 0
            if rate > 0.95: # Tax rate cannot exceed 95%
                rate = 0.95

            if monthly_income < bracket:
                total += (monthly_income - previous_bracket) * rate
                break
            else:
                total += (bracket - previous_bracket) * rate
                previous_bracket = bracket

        # STEP 3: Randomize expected sum

        total += total * (renpy.random.random() * 2 * tax_random_range - tax_random_range) # Will return a random float between +tax_random_range and -tax_random_range

        # Taxes under 250 gold will be ignored

        if total < 250:
            total = 0

        NPC_taxgirl.current_tax = int(total)

        # STEP 4: Update counters and time pressure (once a month)

        if not NPC_taxgirl.flags["last tax"] or NPC_taxgirl.flags["last tax"] <= calendar.time - 28: # Sanity check
            NPC_taxgirl.MC_income = 0 # Every time tax is calculated, the income counter is reset

            if NPC_taxgirl.active and not NPC_taxgirl.flags["disable time pressure"]:
                if NPC_taxgirl.time_pressure_modifier < tax_time_pressure_maximum:
                    offset = game.get_diff_setting("tax rate") / 10 # Hardcoded for now, will be added to difficulty options eventually

                    NPC_taxgirl.time_pressure_modifier += 0.04 + offset # Increases tax rates by 2% to 6% per month, up to 20% max

                    if NPC_taxgirl.time_pressure_modifier > tax_time_pressure_maximum:
                        NPC_taxgirl.time_pressure_modifier = tax_time_pressure_maximum

            NPC_taxgirl.flags["last tax"] = calendar.time # Sanity check

        return NPC_taxgirl.current_tax

    def pay_tax():

        if MC.gold < NPC_taxgirl.current_tax:
            return False
        else:
            MC.gold -= NPC_taxgirl.current_tax
            NPC_taxgirl.current_tax = 0
            NPC_taxgirl.flags["paid tax"] = True
            renpy.play(s_gold, "sound")
            return True


    def get_resting_girls():
        return [g for g in MC.girls if (g.job == "rest" or g.resting or g.workdays[calendar.get_weekday()] == 0) and not (g.away or g.hurt > 0 or g.exhausted)]

    def get_known_free_girls(min_relationship_level=0):
        return [g for g in game.free_girls if g.MC_interact and g.MC_relationship_level >= min_relationship_level]

    def compile_girl_log(girl): # Used to store girl log calculations in a dictionary and avoid refreshing it with every tick
        log_dict = defaultdict(dict)

        log_dict["age"] = calendar.time - girl.get_log("acquired")

        for days in (1, 7, 28, 0):
            log_dict["total_gold"][days] = girl.get_log("total_gold", days)
            log_dict["quest_gold"][days] = girl.get_log("quest_gold", days)
            log_dict["upkeep"][days] = girl.get_log("upkeep", days)
            log_dict["total_xp"][days] = girl.get_log("total_xp", days)
            log_dict["total_jp"][days] = girl.get_log("total_jp", days)
            log_dict["total_rep"][days] = girl.get_log("total_rep", days)
            log_dict["waitress_days"][days] = girl.get_log("waitress_days", days)
            log_dict["dancer_days"][days] = girl.get_log("dancer_days", days)
            log_dict["masseuse_days"][days] = girl.get_log("masseuse_days", days)
            log_dict["geisha_days"][days] = girl.get_log("geisha_days", days)
            log_dict["whore_days"][days] = girl.get_log("whore_days", days)
            log_dict["work_whore_days"][days] = girl.get_log("work_whore_days", days)
            log_dict["work_days"][days] = girl.get_log("work_days", days)
            log_dict["rest_days"][days] = girl.get_log("rest_days", days)
            log_dict["away_days"][days] = girl.get_log("away_days", days)
            log_dict["farm_days"][days] = girl.get_log("farm_days", days)
            log_dict["strike_days"][days] = girl.get_log("strike_days", days)
            log_dict["hurt_days"][days] = girl.get_log("hurt_days", days)
            log_dict["sick_days"][days] = girl.get_log("sick_days", days)

            for job in all_jobs + ["whore"] + all_sex_acts:
                log_dict[job + "_cust"][days] = girl.get_log(job + "_cust", days)
                log_dict[job + "_gold"][days] = girl.get_log(job + "_gold", days)
                log_dict[job + "_xp"][days] = girl.get_log(job + "_xp", days)
                log_dict[job + "_jp"][days] = girl.get_log(job + "_jp", days)
                log_dict[job + "_rep"][days] = girl.get_log(job + "_rep", days)
                log_dict[job + "_perf"][days] = girl.get_average_performance(job, days)

        return log_dict

    def is_censored(tag):
        if tag in (persistent.forbidden_tags + forbidden_tags):
            return True
        return False

    def randomize_girl_level(): # Picks a level for a randomly generated girl, based on Chapter

        weighted_list = []
        rank = 0

        # Chance to generate at lower rank is halved every step

        for i in range(game.max_girl_rank): # Chance gets higher with every rank
            rank += 1
            weighted_list.append([rank, 1.25**rank]) #? Test how it behaves

        girl_rank = weighted_choice(weighted_list)

        if girl_rank < 2:
            return renpy.random.randint(1, int(game.max_girl_level))
        else:
            return renpy.random.randint((girl_rank-1) * 5, int(game.max_girl_level))

    def get_current_folder():
        foldername, ignored1, ignored2 = renpy.game.context().current

        # Trim "game/" and the current file from the folder path
        foldername = foldername[len("game/"):foldername.rfind("/")+1]
        return foldername

    def print_ignore_list():
        ignore_text = list_text(sorted(persistent.pic_ignore_list), "", if_none="No pictures have been set to ignore.")
        if persistent.pic_ignore_list:
            ignore_text = "%i picture%s currently ignored (pictures will be updated after restart):\n" % (len(persistent.pic_ignore_list), plural(len(persistent.pic_ignore_list))) + ignore_text

        with open((config.gamedir + "\\ignored_pictures.txt"), "wt") as ignore_file: #? Check that it works if file doesn't exist
            ignore_file.write(ignore_text)

        notify("列表打印到：" + config.gamedir + "\\ignored_pictures.txt")

    def toggle_ignore_pic(pic): # path overrides pic if provided

        if is_string(pic):
            path=pic
        elif isinstance(pic, Picture):
            path=pic.path
        elif isinstance(pic, ProportionalScale):
            path=event_pic.imgname

        if path in persistent.pic_ignore_list:
            persistent.pic_ignore_list.remove(path)
            priority_notify("Removed from the 'IGNORE' list: %s" % path, col=c_lightgreen)
        else:
            if not persistent.seen_ignore_intro:
                renpy.call_in_new_context("ignore_introduction")
            persistent.pic_ignore_list.append(path)
            priority_notify("Added to the 'IGNORE' list: %s" % path, col=c_red)

    def girl_object_count():
        return sum(1 for obj in gc.get_referrers(Girl) if obj.__class__ is Girl)

    def girl_gc():
        glist = game.get_all_girls()
        dlist = []

        for g in gc.get_referrers(Girl):
            if g.__class__ is Girl:
                if g not in glist:
                    dlist.append(g)

        nb = len(dlist)

        while dlist:
            del dlist[0]

        gc.collect()

        return "%i girls deleted. Remaining: %i" % (nb, girl_object_count())


    def get_opposite_attribute(attr):
        prfx = ""
        opp = ""

        if attr.startswith("very "):
            prfx = "very "
            attr = attr[5:]

        for a1, a2 in personality_attributes:
            if attr == a1:
                opp = a2
                break
            elif attr == a2:
                opp = a1
                break

        return prfx + opp

    def debug_sorting_girls():

        MC.girls = slavemarket.girls

        for girl in MC.girls:
            girl.level = dice(10)
            girl.rank = dice(4)
            girl.set_job(rand_choice(all_jobs))

## 中文翻译函数 ##

    def tl_cn(text, translation_dicts, default_value=None):
        if isinstance(translation_dicts, dict):
            # 如果 translation_dicts 是单个字典
            if text in translation_dicts:
                return translation_dicts[text]
        else:
            # 如果 translation_dicts 是字典列表
            for translation_dict in translation_dicts:
                if text in translation_dict:
                    return translation_dict[text]
        
        if default_value is not None:
            return default_value
        else:
            return text

#### END OF BK FUNCTIONS FILE ####
