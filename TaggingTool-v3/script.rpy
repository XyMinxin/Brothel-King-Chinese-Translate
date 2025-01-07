# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define bk = Character('Brothel King', color="#c8ffc8")

# Define default 'replace' values
define persistent.replace_from = "bisexual"
define persistent.replace_to = "bisexual"

init -10 python:
    import hashlib

    def open_log_file():
        global RENAMELOG
        try: 
            RENAMELOG.close()    
        except:
            pass
        if persistent.girl:
            RENAMELOG = open(config.gamedir + "/../renamelog - " + persistent.girl[len("images/"):] + ".txt", "a") # Replace with 'None' to turn off
        else:
            RENAMELOG = None

    def close_log_file():
        global RENAMELOG
        try: 
            RENAMELOG.write("------\n")
            RENAMELOG.flush()
            RENAMELOG.close()    
        except:
            pass

    UNTAGGED = "_UNTAGGED " # Space at the end is necessary for algorithm to work
    FILENAME_NUMBERCOUNT = 5 # -> portrait (00000)
    STD_SIZE = (1024, 768)
    
    # <Chris12 - Tagsets>
    STANDARD_TAGSET = "Core"
    if persistent.active_tagset is None:
        persistent.active_tagset = STANDARD_TAGSET
    # </Chris12 - Tagsets>

    CUSTOM_VARIANTS = ("custom0", "custom1", "custom2", "custom3", "custom4", "custom5", "custom6", "custom7", "custom8", "custom9");

    if persistent.girl is None:
        persistent.girl = None

    if persistent.optional_filter is None:
        persistent.optional_filter = True

    if persistent.change_log is None:
        persistent.change_log = {}

    if not persistent.forced_restart:
        persistent.forced_restart = False

    if persistent.girl:
        mode = "edit"
    else:
        mode = "select"

    img_resolutions = { }


# <Chris12 - Tagsets>
init -3 python:
    import datetime

    def log_rename(str):
        if RENAMELOG:
            RENAMELOG.write(str)
            RENAMELOG.write("\n")

    class TagSet(object):
        def __init__(self, name, includes = []):
            self.name = name
            self.includes = includes
            self.all_names = {name}
            for incl in includes : self.all_names.update(incl.all_names)

    tagset_core = TagSet(STANDARD_TAGSET) # The program relies on a tagset named "Core" existing
    all_tagsets = [tagset_core]

    def get_tagset(name):
        for ts in all_tagsets :
            if ts.name == name :
                return ts
        return None

    def cycle_tagset():
        if (persistent.active_tagset is None) or (all_tagsets[0].name == persistent.active_tagset) :
            persistent.active_tagset = all_tagsets[-1].name
        else:
            last_set = None
            found = False
            for ts in all_tagsets :
                if ts.name == persistent.active_tagset :
                    persistent.active_tagset = last_set
                    found = True
                    break
                last_set = ts.name
            if not found :
                persistent.active_tagset = all_tagsets[0].name



    def sanity_check():
        global optional_tags
        global optional_tag_dict
        global sorted_tag_dict_keys
        global main_tags_idx
        global all_tags_dict
        global sorted_tags_with_separator

        optional_tags = sorted(optional_tags, key = lambda x: (x.order, x.order2))
        optional_tag_dict = {tag.name : tag for tag in optional_tags}

        all_tags_dict = {tag.name : tag for tag in (main_tags + optional_tags) if tag is not None and tag.name is not None and tag.name != ""}

        variant_dict = {}

        for tag in (main_tags + optional_tags):
            for variant in tag.variants:
                if variant is not None and variant != "":
                    if variant in variant_dict:
                        raise Exception("Tag \'" + tag.name + "\': Variant \'" + variant + "\' already declared for Tag \'" + variant_dict[variant][0] + "\'")
                    else:
                        variant_dict[variant.lower()] = [tag.name.lower()]

        for variant, tag_def in variant_dict.items() :
            tag_dict.update({variant : tag_def})

        tag_with_space_dict = {}
        for key in tag_dict:
            tag_dict[key] = make_tuple(tag_dict[key])

        sorted_tag_dict_keys = sorted(tag_dict.keys(), key = lambda x : len(x), reverse = True)
        sorted_tags_with_separator = [tag for tag in sorted_tag_dict_keys if " " in tag]
        main_tags_idx = {tag.name : num for num, tag in enumerate(main_tags) if tag.name != ""}
# </Chris12 - Tagsets>


init -2 python:

    import os
    import sys
    import re # <Chris12 - Regular Expressions for filenames />
    from collections import OrderedDict

    config.keymap['game_menu'].remove('mouseup_3')
    # config.keymap['screenshot'].remove('s')
    # config.keymap['toggle_fullscreen'].remove('f')
    # config.keymap['toggle_music'].remove('m')
    # config.keymap['hide_windows'].remove('h')

    def make_tuple(item, obj_type = None):
        '''This function transforms a single string, number or object into a tuple (technically, a list) of one element.'''

        if isinstance(item, basestring) or isinstance(item, int) or isinstance(item, float):
            item = [item]

        if obj_type:
            if isinstance(item, obj_type):
                item = [item]

        return item

    def round_int(x):

        x = float(x)

        return int(round(x))

    def and_text(mylist):
        if len(mylist) == 1:
            return str(mylist[0])

        elif len(mylist) > 1:
            return str(", ".join(mylist[:-1]) + " and " + mylist[-1])

        else:
            return "No list"

    #<Chris12 PackState>
    # Imports filesize, hashcode and tags. Detects duplicates (only if hash is in the packstate)
    def import_packstate(girl):
        import_result = ""
        counterImageStates = 0
        counterMatched = 0
        counterChanges = 0
        counterDuplicates = 0
        try :
            packStateFilePath = "packstates/" + persistent.girl[len("images/"):] + ".txt"
            with open(config.gamedir + "/" + packStateFilePath, "r") as packStateFile :
                filesize = packStateFile.readline()
                while (len(filesize) != 0) :
                    filesize = int(filesize.strip())
                    hash = packStateFile.readline()
                    alreadyFound = False
                    counterImageStates += 1
                    hash = hash.strip()
                    tag_filename = packStateFile.readline()
                    for pic in girl.pics :
                        if (pic.get_filesize() == filesize and pic.get_hash() == hash) :
                            pic.clear_tags()
                            counterMatched += 1
                            if alreadyFound :
                                counterDuplicates += 1
                                pic.delete = True
                                pic.add_tag("duplicate")

                            alreadyFound = True

                            for tag in tag_filename.split() :
                                pic.add_tag(tag)

                            if pic.file_name[:pic.file_name.find("(")] != pic.new_name[:str(pic.new_name).find("(")]:
                                counterChanges += 1
                                # return pic.file_name[:pic.file_name.find("(")] + "\n" + pic.new_name[:str(pic.new_name).find("(")]

                    filesize = packStateFile.readline()

            import_result = persistent.girl + "\\packStateFile.txt contained " + str(counterImageStates) + " renames.\n"

            if counterMatched > 0 :
                import_result += str(counterMatched) + " of your files matched, "
                if counterChanges > 0:
                    import_result += " and " + str(counterChanges) + " files were updated for change. They still need to be commited.\n"
                else :
                    import_result += " but none of them need to be changed. No proposed changes.\n"

                if counterDuplicates > 0 :
                    import_result += "Of those, " + str(counterDuplicates) + " were duplicates and marked for deletion (will be tagged as _TRASH)."

            else :
                import_result += "However, no files were found that matched. No proposed changes.\n"

        # oldNamer
        # except IOError as (errno, strerror):
        #    import_result = "I/O error({0}): {1}".format(errno, strerror)
        #    pass
        except :
            raise
        return import_result
    #</Chris12 PackState>


    class ProportionalScale(im.ImageBase):
        '''Resizes a renpy image to fit into the specified width and height.
        The aspect ratio of the image will be conserved.'''
        def __init__(self, imgname, maxwidth, maxheight, bilinear=True, **properties):
            img = im.image(imgname)
            super(ProportionalScale, self).__init__(img, maxwidth, maxheight, bilinear, **properties)
            self.imgname = imgname
            self.image = img
            self.maxwidth = int(maxwidth)
            self.maxheight = int(maxheight)
            self.bilinear = bilinear

        def load(self):
            child = im.cache.get(self.image)
            width, height = child.get_size()
            img_resolutions[self.imgname] = str(width) + "x" + str(height)

            ratio = min(self.maxwidth/float(width), self.maxheight/float(height))
            width = ratio * width
            height = ratio * height

            if self.bilinear:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.scale.smoothscale(child, (width, height))
                finally:
                    renpy.display.render.blit_lock.release()
            else:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.pgrender.transform_scale(child, (newwidth, newheight))
                finally:
                    renpy.display.render.blit_lock.release()
            return rv

        def predict_files(self):
            return self.image.predict_files()



    class Girl(object):
        '''The object to which a girl pack pictures are attached.'''
        def __init__(self, dir):
            self.dir = dir
            self.path = "images\\" + dir
            self.pics = []
            self.ignore_pics = [] # <Chris12 PackState />
            
            # scenechan: added global status for carousel view here.
            global selected_index
            global selected_pic
            global filtered_pics
            global selected_pic_list
            filtered_pics = []
            selected_pic_list = []
            selected_index = 0
            selected_pic = None

        def add_pic(self, file_name, file):
            pic = Pic(self.path, file_name, file)

            if not pic.has_tag("ignore"):
                self.pics.append(pic)
                self.pics[-1].parent=self
            else:
                self.ignore_pics.append(pic)

        def previous_pic(self, filters=None, nb=1):

            if filters:
                li = self.get_filtered_pics(filters)
                if selected_pic and not selected_pic in li :
                    li = [x for x in self.pics if (x == selected_pic) or x in li]
            else:
                li = self.pics

            if len(li) == 0:
                return

            global selected_pic
            global filtered_pics
            global selected_index
            filtered_pics = li
            
            def decrement_idx(idx) : 
                if (idx - nb) < 0:
                    if idx == 0:
                        idx = len(li)-1
                    else:
                        idx = 0
                else : 
                    idx -= nb
                return idx
            
            if selected_pic:
                idx = li.index(selected_pic)
                idx = decrement_idx(idx)
            else:
                idx = 0
            selected_pic = li[idx]
            selected_index = idx
            
            idx = decrement_idx(idx)
            next_img = li[idx]
            if not next_img.video : 
                renpy.predict(next_img.get_std_displayable())

        def next_pic(self, filters=None, nb=1):

#            renpy.notify(str(filters))

            if filters:
                li = self.get_filtered_pics(filters)
                if selected_pic and not selected_pic in li :
                    li = [x for x in self.pics if (x == selected_pic) or x in li]
            else:
                li = self.pics

            if len(li) == 0:
                return

            global selected_pic
            global filtered_pics
            global selected_index
            filtered_pics = li
            
            def increment_idx(idx) : 
                if (idx + nb) >= len(li):
                    if idx == len(li)-1:
                        idx = 0
                    else:
                        idx = len(li)-1
                else : 
                    idx += nb
                return idx
            
            if selected_pic:
                idx = li.index(selected_pic)
                idx = increment_idx(idx)
            else:
                idx = 0
            selected_pic = li[idx]
            selected_index = idx
            
            idx = increment_idx(idx)
            next_img = li[idx]
            if not next_img.video : 
                renpy.predict(next_img.get_std_displayable())
                

        def count_pics(self, filters, include_bk_autoadds = True):
            return len(self.get_filtered_pics(filters, include_bk_autoadds))

        def get_filtered_pics(self, filters, include_bk_autoadds = False):
            if filters:
                return [p for p in self.pics if p.matches(filters, include_bk_autoadds)]
            else:
                return self.pics

        def evaluate_girlpack(self): # Evaluate girl pack metrics to use for the girl pack rating

            main_cover_score, main_div_score, op_cover_score, op_div_score = 0.0, 0.0, 0.0, 0.0

            # Check pictures with 'Main' tags (including naked variations)
            main_cover_score += sum(1 for tag in normal_tags if len(get_pic_list(self, tag, not_tags=["naked"])))
            main_cover_score += sum(1 for tag in normal_tags if len(get_pic_list(self, tag, and_tags=["naked"])))
            main_cover_score += sum(1 for tag in all_sex_acts if len(get_pic_list(self, tag, not_tags=["group", "bisexual", "machine", "beast", "monster"])))
            main_cover_score += sum((1 for tag in ("group", "bisexual") for tag2 in all_sex_acts if len(get_pic_list(self, tag, and_tags=[tag2], not_tags=["machine", "beast", "monster"]))))
            main_cover_score_total = len(normal_tags)*2 + len(all_sex_acts)*3

            # Check pictures with optional tags (including all act variations)

            op_cover_score += sum((1 for tag in all_farm_tags for tag2 in extended_sex_acts if len(get_pic_list(self, tag, and_tags=tag2))))
            op_cover_score += sum((1 for fix in fix_dict.values() for atag in fix.acts if len(get_pic_list(self, fix.tag_list[0], and_tags=atag, not_tags=fix.not_list))))

            #Debug: Output all found tuples
            debug_output = False
            debug_full = False
            if debug_output:
                with open(config.gamedir + "/../dbgTagTuples-" + self.dir + ".txt", "w") as output :
                    output.write("\n".join([tag for tag in normal_tags if debug_full or len(get_pic_list(self, tag, not_tags=["naked"]))]))
                    output.write("\n")
                    output.write("\n".join([tag+",naked" for tag in normal_tags if debug_full or len(get_pic_list(self, tag, and_tags=["naked"]))]))
                    output.write("\n")
                    output.write("\n".join([tag for tag in all_sex_acts if debug_full or len(get_pic_list(self, tag, not_tags=["group", "bisexual", "machine", "beast", "monster"]))]))
                    output.write("\n")
                    output.write("\n".join([tag+","+tag2 for tag in ("group", "bisexual") for tag2 in all_sex_acts if debug_full or len(get_pic_list(self, tag, and_tags=[tag2], not_tags=["machine", "beast", "monster"]))]))
                    output.write("\n")
                    output.write("\n".join([tag+","+tag2 for tag in all_farm_tags for tag2 in extended_sex_acts if debug_full or len(get_pic_list(self, tag, and_tags=tag2))]))
                    output.write("\n")
                    output.write("\n".join([(fix.name + ", " + atag) for fix in fix_dict.values() for atag in fix.acts if debug_full or len(get_pic_list(self, fix.tag_list[0], and_tags=atag, not_tags=fix.not_list))]))


            op_cover_score_total = len(all_farm_tags)*len(extended_sex_acts) + sum(len(fix.acts) for fix in fix_dict.values())

            # Check main pictures diversity
            
            def get_main_div_score(pic_list) : return min(10, len(pic_list))
            def get_optional_div_score(pic_list) : return min(5, len(pic_list))

            main_div_score += sum(get_main_div_score(get_pic_list(self, tag, not_tags="naked")) for tag in normal_tags)
            main_div_score += sum(get_main_div_score(get_pic_list(self, tag, and_tags="naked")) for tag in normal_tags)
            main_div_score += sum(get_main_div_score(get_pic_list(self, tag, not_tags=["group", "bisexual", "machine", "beast", "monster"])) for tag in all_sex_acts)
            main_div_score += sum((get_main_div_score(get_pic_list(self, tag, and_tags=tag2, not_tags=["machine", "beast", "monster"])) for tag in ("group", "bisexual") for tag2 in all_sex_acts))

            # Check optional pictures diversity

            op_div_score += sum((get_optional_div_score(get_pic_list(self, tag, and_tags=tag2)) for tag in all_farm_tags for tag2 in extended_sex_acts))
            op_div_score += sum((get_optional_div_score(get_pic_list(self, fix.tag_list[0], and_tags=atag, not_tags=fix.not_list)) for fix in fix_dict.values() for atag in fix.acts))

            # Store result of evaluation

            if main_cover_score:
                main_av_pics = main_div_score/main_cover_score
            else:
                main_av_pics = 0

            if op_cover_score:
                op_av_pics = op_div_score/op_cover_score
            else:
                op_av_pics = 0

#            renpy.say(self.path, "main_cover_score_total " + str(main_cover_score_total) + ", op_cover_score_total " + str(op_cover_score_total) + ", main_cover_score " + str(main_cover_score) + ", op_cover_score " + str(op_cover_score) + ", main div " + str(main_div_score) + ", op div " + str(op_div_score) + ", main_av_pics " + str(main_av_pics) + ", op_av_pics " + str(op_av_pics))

            return {"main cover score" : main_cover_score/main_cover_score_total,
                    "main diversity average" : main_av_pics,
                    "optional cover score" : op_cover_score/op_cover_score_total,
                    "optional diversity average" : op_av_pics}

        def replace(self, _from, _to):

            i = 0

            for pic in self.pics:
                if _from in pic.file_name:
                    i += 1
                    pic.rename_file(pic.file_name.replace(_from, _to))

            bk(str(i) + " changes have been made.")


    ending_pattern = re.compile(r"(\(\d*\))?(\.\w{3,4})+$") # Chris12: can match (and remove) the last part of a filename '(00001).jpg'.

    class Pic():

        def __init__(self, girl_path, file_name, file):

            self.file_name = file_name
            self.file = file
            self.tags = []
            self.committed = False
            self.delete = False
            self.girl_path = girl_path
            self.file_path = file[0:-len(file_name)]
            self.sub_dir = self.file_path[1+len(girl_path):]
            if len(self.sub_dir.strip()) == 0 : self.sub_dir = None
            self.new_name = file_name
            self.update_tags()
            self.hashcode = None
            self.filesize = -1
            lowerExtension = file_name[-5:].lower()
            self.video = any(lowerExtension.endswith(vid_ext) for vid_ext in VIDEOFORMATS)

        def get_std_displayable(self): 
            if self.video:
                return Movie(size=STD_SIZE, play=self.file)
            else:
                return ProportionalScale(self.file, STD_SIZE[0], STD_SIZE[1])
        
        def get_hash(self):
            if self.hashcode is None :
                BLOCKSIZE = 65536
                hasher = hashlib.sha256()
                with open(config.gamedir + "/" + self.file, 'rb') as afile:
                    buf = afile.read(BLOCKSIZE)
                    while len(buf) > 0:
                        hasher.update(buf)
                        buf = afile.read(BLOCKSIZE)
                self.hashcode = hasher.hexdigest()
            return self.hashcode

        def get_filesize(self):
            if self.filesize < 0 :
                self.filesize = os.path.getsize(config.gamedir + "/" + self.file)
            return self.filesize

        def toggle_delete(self):
            self.delete = not self.delete

# <Chris12 - new tag check>
#        def update_tags_old(self):
#            for tag in tag_dict.keys():
#                if tag in self.file_name.lower():
#                    for new_tag in make_tuple(tag_dict[tag]):
#                        self.add_tag(new_tag, init=True)



        def update_tags(self):
            global debug_update_tags
            debug_update_tags = False
            # debug_update_tags = self.file_name == "69 (00000).jpg" # check some specific file only

            def check_all_tags(filename, current_tag_list):
                old_len = len(filename)
                for tag in current_tag_list:
                    filename = filename.replace(tag, ' ')
                    new_len = len(filename)
                    if (new_len != old_len):
                        if debug_update_tags: renpy.say(self.file_name, tag + " found")
                        old_len = new_len
                        for new_tag in tag_dict[tag]:
                            self.add_tag(new_tag, init=True)
                return filename

            filename = self.file_name.lower()
            filename = ending_pattern.sub("", filename) # removes extension and, if found, also (00001) at the end of the filename
            filename = check_all_tags(filename, sorted_tags_with_separator) # First look for tags with separators, e.g. 'cum shower'

            #after excluding all those tags, split the filename and look for exact matches
            parts = filename.split(' ')
            found = []
            not_found = []
            for part in parts:
                if part.strip() != "":
                    tag_entry = tag_dict.get(part, None)
                    if tag_entry is not None: # tag was found
                        for new_tag in tag_entry:
                            self.add_tag(new_tag, init=True)
                        found.append(part)
                    else:
                        not_found.append(part)
                    if debug_update_tags: renpy.say(self.file_name, "Found: " + ','.join(self.tags) + "\nNot found: " + ','.join(not_found))

            if len(not_found) > 0:
                filename = ' '.join(not_found)
                if debug_update_tags: renpy.say(self.file_name + " || " + filename, "Unidentified tags left!")
                check_all_tags(filename, sorted_tag_dict_keys)

        def clear_tags(self):
            self.tags = []
            self.new_name = self.get_new_name()
            update_change_log(self.file_path, self.file_name, self.new_name)
            
        def get_all_tags(self):
            return [tag for tag in self.tags]
        
        def set_all_tags(self, tags):
            self.clear_tags()
            for tag in tags:
                self.add_tag(tag)

        def has_tag(self, tag, include_bk_autoadds = False):
            if include_bk_autoadds : 
                for pair in BK_AUTOADDS :
                    if pair[1] == tag and pair[0] in self.tags :
                        return True
            
            #if include_bk_autoadds and "bisexual" == tag and "lesbian" in self.tags :
             #   return True
            
            if tag in self.tags:
                return True
            return False

        def matches(self, filters, include_bk_autoadds = False):
            if include_bk_autoadds :
                for pair in BK_AUTOADDS :
                    if pair[1] in filters and pair[0] in self.tags :
                        filters = [f for f in filters if f != pair[1]]
                        
            #if include_bk_autoadds and "bisexual" in filters and "lesbian" in self.tags :
            #    filters = [f for f in filters if f != "bisexual"] # Don't need to check bisexual anymore, since lesbian is enough
                
            for fil in filters:
                if fil not in self.tags:
                    return False
            return True

        def describe_tags(self):

            text1 = "Current tags: "

            if self.tags:
                for tag in self.tags:
                    text1 += tag + ", "
                text1 = text1[:-2]
            else:
                text1 += "None"

            return text1

        def toggle_tag(self, tag):
            if tag in self.tags:
                self.remove_tag(tag)
            else:
                self.add_tag(tag)
                tag_entry = optional_tag_dict.get(tag, None)
                if tag_entry is not None: # tag was found
                    if tag_entry.auto_add is not None :
                        for auto_tag in tag_entry.auto_add : self.add_tag(auto_tag)
                    if tag_entry.auto_remove is not None :
                        for auto_tag in tag_entry.auto_remove : self.remove_tag(auto_tag)

        def add_tag(self, tag, init=False):
            if not tag in self.tags:
                self.tags.append(tag)

                if not init:
                    for key, other_tags in sorted(tag_dict.items(), key = lambda x : len(x[0]), reverse = True):
                        if key in tag:
                            for tag2 in make_tuple(other_tags):
                                self.add_tag(tag2)
                            break
                    self.new_name = self.get_new_name()
                    update_change_log(self.file_path, self.file_name, self.new_name)

        def remove_tag(self, tag):
            if tag in self.tags:
                self.tags.remove(tag)

                self.new_name = self.get_new_name()
                update_change_log(self.file_path, self.file_name, self.new_name)

        def get_new_name(self, shorten = False):

            self.tags.sort(key=sort_tags)

            global delete_count
            global girl_list

#            i = 0
            girl = None

            if not girl_list:
                return

            for girl in girl_list:
                if girl.path == self.girl_path:
                    break

#            for pic in [p for p in girl.pics if p.committed]:
#                if pic.tags == self.tags:
#                    i += 1

            lowerExtension = self.file_name[-5:].lower()
            for ext in IMGFORMATS:
                if lowerExtension.endswith(ext): 
                    ending = ext
                    break
            else:
                raise (self.file_name + ": Unknown Extension") # Should not happen as long as file were filtered according to IMGFORMATS

            new_tags = self.tags
            if shorten:
                new_tags = []
                for tag in self.tags:
                    tag_entry = all_tags_dict.get(tag, None)
                    if tag_entry is not None: # tag was found
                        new_tags.append(tag_entry.shorthand)
                    else:
                        new_tags.append(tag)

            if self.delete:
                new_file_name = "_TRASH " + " ".join(new_tags) + " (%s)" + ending
                try :
                    delete_count += 1
                except NameError :
                    global delete_count
                    delete_count = 1

            elif new_tags:
                new_file_name = " ".join(new_tags) + " (%s)" + ending
            else:
                new_file_name = UNTAGGED + "(%s)" + ending

            if "custom" in new_file_name:
                for variant in CUSTOM_VARIANTS:
                    if variant in self.file_name:
                        new_file_name = new_file_name.replace("custom", variant)
                        break
                else:
                    new_file_name = new_file_name.replace("custom", "custom0")

            if shorten:
                return new_file_name
            else:
                if len(new_file_name) < 160:
                    return new_file_name
                else:
                    return self.get_new_name(shorten=True)

        def commit_changes(self, filename_counter_dict, phase):
            new_file_name = self.get_new_name()
            first_part = new_file_name[:new_file_name.find("(")]
            tags_changed = first_part != self.file_name[:self.file_name.find("(")]
            if phase == 1 and tags_changed:
                return 0 # First phase : Only fix numbering
                
            if phase == 1 and first_part == UNTAGGED : 
                # Don't fix numbering for untagged, but remember the highest so that new untagged get queued after
                try :
                    # Extract the number from the filename
                    filename_counter_dict[first_part] = int(self.file_name[len(first_part) + 1 : len(first_part) + FILENAME_NUMBERCOUNT + 1]) + 1
                except :
                    pass
                return 0
                
            if phase == 2 and not tags_changed:
                return 0 # Second phase : Only renaming
            
            i = 0
            try :
                i = filename_counter_dict[first_part] + 1
            except KeyError :
                pass
            
            filename_counter_dict[first_part] = i

            # Compares file names up to the first parenthesis

            if (new_file_name % str(i).zfill(FILENAME_NUMBERCOUNT)) != self.file_name :

                persistent.change_log.pop(self.file_path + self.file_name, None)

                while not self.committed:

                    if self.rename_file(new_file_name % str(i).zfill(FILENAME_NUMBERCOUNT)):
                        self.committed = True
                        filename_counter_dict[first_part] = i
                    else:
                        i += 1
                    if i > 20000 : raise Exception(self.file_name + " -> " + new_file_name)

                return 1

            return 0

        def rename_file(self, name):
            os.chdir(config.gamedir + "/" + self.file_path)

            if os.path.exists(name) : return False

            try:
                os.rename(self.file_name, name)
            except:
                return False

            log_rename(self.file_name + " -> " + name)
            self.file_name = name

            return True

#            except:
#                renpy.say("", "Cannot find " + self.file_name)


    class Tag(object):
        def __init__(self, name, _or = [], _and = [], _not = [], order = 0, order2 = 0, lbl=None, fix_name=None, tagsets = [tagset_core], auto_add=None, auto_remove=None, shorthand=None, variants=None, btn_text_size=19):
            if shorthand is not None and not isinstance(shorthand, basestring): raise Exception("Tag " + tag + ": shorthand is not a string!")
            if name.lower() != name: raise Exception("Tag " + name + " is not lowercase!")
            if order < 0 : raise Exception("Tag '" + name + "': + Order must be >= 0!")

            self.btn_text_size = btn_text_size
            self.name = name
            self._and = make_tuple(_and)
            self._or = make_tuple(_or)
            self._not = make_tuple(_not)
            self.order = order
            self.order2 = order2
            if lbl :
                self.lbl = lbl
            else :
                self.lbl = name.capitalize()

            self.fix_name = fix_name
            if auto_add is not None:
                self.auto_add = make_tuple(auto_add)
            else:
                self.auto_add = None
                
            if auto_remove is not None:
                self.auto_remove = make_tuple(auto_remove)
            else:
                self.auto_remove = None

            # name and shorthand are also part of variants
            self.variants = [name]
            if shorthand is not None:
                self.shorthand = shorthand
                self.variants.append(shorthand)
            else:
                self.shorthand = name

            if variants is not None:
                if isinstance(variants, basestring):
                    self.variants.append(variants)
                else:
                    self.variants.extend(variants) # check if .extend works as intended
                    self.variants = sorted(self.variants, key = lambda x : len(x), reverse = True)

            # <Chris12 - Tagsets>
            self.tagsets = set()
            for ts in tagsets:
                self.tagsets.add(ts.name)
                for include in ts.includes:
                    self.tagsets.add(include.name)
            # </Chris12 - Tagsets>

#        def describe_tags(self):
#            return {v: k for k, v in optional_tag_dict}[self]

        def check_conditions(self, tag_list, test=False):

            if test:
                text1 = ""
                for tag in self._and:
                    text1 += tag + ", "
                text1 = text1[:-2]
                return text1

            if self._and:
                for tag in self._and:
                    if not tag in tag_list:
                        return False

            if self._not:
                for tag in self._not:
                    if tag in tag_list:
                        return False

            if self._or:
                for tag in self._or:
                    if tag in tag_list:
                        return True
                else:
                    return False

            return True


    class Fixation(object):

        def __init__(self, name, acts, step, frequency = 12.0, tag_list = [], not_list = [], attribute = None, short_name=""):

            self.name = name
            if short_name:
                self.short_name = short_name
            else:
                self.short_name = self.name
            self.acts = make_tuple(acts)
            self.step = step
            self.frequency = frequency
            self.tag_list = tag_list
            self.not_list = not_list
            self.attribute = attribute
#            self.perk = sexual_perks[name]

init python:

    def update_change_log(path, old_name, new_name):
        if new_name:
            if old_name[:old_name.find("(")] != new_name[:new_name.find("(")]:
                persistent.change_log[path + old_name] = path + new_name
            else:
                persistent.change_log.pop(path + old_name, None)


    def compile_girl_pics(path="images/"):

        girl_dict = {}
        subdir_files = [] # moves files in subdirectories to the end
        dir = None
        for file in renpy.list_files():

            if file.startswith(path):

                file_parts = file.split("/")

                if len(file_parts) < 3:
                    pass

                dir, file_name = file_parts[1], file_parts[-1]

                if file_name.lower()[-4:] in IMGFORMATS or file_name.lower()[-5:] in IMGFORMATS:
                    if dir not in girl_dict:
                        girl_dict[dir] = Girl(dir=dir)
                        
                    if len(file_parts) == 3 :
                        girl_dict[dir].add_pic(file_name, file)
                    else :
                        subdir_files.append((dir, file_name, file))
        
        for dir, file_name, file in subdir_files :
            girl_dict[dir].add_pic(file_name, file)
        
        # Converts to a list as the dictionary is no longer needed
        glist = girl_dict.values()
        
        return glist

    def get_girl_menu(girl_list):
        menu_list = [("Choose a girl to edit", None)]

        for girl in girl_list:
            menu_list.append((girl.dir, girl))

        menu_list.append(("Quit", "quit"))

        return menu_list

    def list_associated_tags(tag):
        tag_list = []
        for t in tag_dict.keys():
            if t in tag:
                for a_tag in tag_dict[t]:
                    if a_tag not in tag_list:
                        tag_list.append(a_tag)

        entry = optional_tag_dict[tag]
        if (entry is not None) and (entry.auto_add is not None) :
            for auto_tag in entry.auto_add : tag_list.append(auto_tag)

        return tag_list

    def format_stat(nb):
        if nb > 5:
            col = "#33FF33"
        elif nb == 0:
            col = "#FF0033"
        else:
            col = "#FFFFFF"

        return "{color=" + col + "}"+ str(nb) + "{/color}"

    def sort_tags(tag):
        if tag in sorting_dict.keys():
            return sorting_dict[tag]
        else:
            try:
                tag = all_tags_dict[tag]
                return (tag.order, tag.order2)
            except:
                return (1000000, 1000000)

# The game starts here.
label start:

    
    $ if not (persistent.active_tagset in [tagset.name for tagset in all_tagsets]): persistent.active_tagset = STANDARD_TAGSET

    $ girl_list = compile_girl_pics()

    while persistent.change_log :
        menu:
            "{b}WARNING{b}" "Some changes were not committed properly. Do you want to recover those changes?"

            "See details":
                $ r = renpy.call_screen("change_log")

                if r == "commit":
                    if renpy.call_screen("confirm", "Are you sure you want to commit to these changes? (WARNING: old file names will not be kept).", Return(True), Return(False)):

                        $ t = 0
                        
                        $ open_log_file()
                        
                        while persistent.change_log:
                            $ old, new = persistent.change_log.items()[0]
                            $ failed = True

                            python:

                                os.chdir(config.gamedir)

                                for i in xrange(500):

                                    try:
                                        os.rename(old, new % i)
                                        log_rename(old + " -> " + (new % i))
                                        failed=False
                                    except:
                                        pass

                                    if not failed:
                                        break


                            if failed:
                                python:
                                    file_parts = new.split("\\")
                                    file_parts[-1] = "_" + file_parts[-1]
                                    _new = "\\".join(file_parts)

                                menu:
                                    "Could not rename [old] as [new]\nMaybe the file has already been changed."

                                    "Rename as [_new]":

                                        python:
                                            os.chdir(config.gamedir)
                                            os.rename(old, _new)
                                            log_rename(old + " -> " + _new)

                                            t += 1

                                    "Ignore the change":
                                        pass

                                    "Delete [old]":
                                        python:
                                            os.chdir(config.gamedir)
                                            os.remove(old)
                            else:
                                $ t += 1

                            $ persistent.change_log.pop(old, None)


#                        python:
#                            os.chdir(config.gamedir)

#                            t = 0

#                            for old, new in persistent.change_log.items():
#                                t += 1

#                                except:
#                                    raise AssertionError, "Cannot rename " + old + " as " + new
#                                persistent.change_log.pop(old, None)
                        
                        $ close_log_file()
                        
                        bk "[t] files were renamed."

                        bk "Restarting Ren'py now.{w=1}{nw}"

                        $ renpy.utter_restart()

                elif r == "discard":
                    if renpy.call_screen("confirm", "Are you sure you want to discard " + str(len(persistent.change_log.keys())) + " uncommitted changes?", Return(True), Return(False)):
                        $ persistent.change_log = {}

            "Discard changes":
                if renpy.call_screen("confirm", "Are you sure you want to discard " + str(len(persistent.change_log.keys())) + " uncommitted changes?", Return(True), Return(False)):
                    $ persistent.change_log = {}



    if mode == "edit":
        call edit() from _call_edit
    elif mode == "select":
        call select_pack_start() from _call_select_pack_start
    elif mode == "browse":
        call browse_pack() from _call_browse_pack
    elif mode == "stats":
        call pack_stats() from _call_pack_stats
    elif mode == "ini":                             # <neronero & RudolfU - BK.ini>
        call generate_ini() from _call_generate_ini # </neronero & RudolfU - BK.ini>
    elif mode == "replace":
        call replace_in_files() from _call_replace_in_files
    elif mode == "import_packstate":
        call browse_pack() from _call_browse_pack_1
    return

label replace_in_files():

    scene black

    if not persistent.girl:

        call select_girl_pack() from _call_select_girl_pack_4

        if result == "quit":
            return

        $ girl = result
        $ persistent.girl = girl.path

    else:
        python:

            for girl in girl_list:
                if girl.path == persistent.girl:
                    break

    $ persistent.replace_from = str(renpy.input("Select the text to replace", default = persistent.replace_from))

    $ persistent.replace_to = str(renpy.input("Select the new text", default = persistent.replace_to))

    if renpy.call_screen("confirm", "{b}" + girl.path + "{/b}:\nAre you sure you want to replace " + event_color["bad"] % persistent.replace_from + " with " + event_color["bad"] % persistent.replace_to + "? Your files will be renamed (WARNING: old file names will not be kept).", Return(True), Return(False)):
        $ open_log_file()
        $ girl.replace(persistent.replace_from, persistent.replace_to)
        $ close_log_file()

        bk "Restarting Ren'py now.{w=1}{nw}"

        $ renpy.utter_restart()

    return

label edit(pic_name=None):

    scene expression "#222222"

    if not persistent.girl:

        call select_girl_pack() from _call_select_girl_pack

        if result == "quit":
            return

        $ girl = result
        $ persistent.girl = girl.path

    else:
        $ delete_count = 0
        python:

            for girl in girl_list:
                if girl.path == persistent.girl:
                    break
            else:
                renpy.say("", "Girl path [persistent.girl] could not be found.")
                persistent.girl = None
                renpy.jump("start")

    if pic_name:
        python:
            for pic in girl.pics:
                if pic.file_name == pic_name:
                    selected_pic = pic
                    break
            else:
                selected_pic = girl.pics[0]
    else:
        $ selected_pic = girl.pics[0]

label edit_shortcut():

    $ active_filters = []

    show screen show_pic()

    while True:

#        $ bk(selected_pic.describe_tags(), interact=False)
        $ result = ui.interact()

        if result == "commit":

            if selected_pic and selected_pic.video : 
                $ renpy.call_screen("warning", "Video files are locked during playback, causing the renaming process to fail.\n\nPlease select a non-video file to commit your changes.")

            elif renpy.call_screen("confirm", "Are you sure you want to commit to these changes? Your files will be renamed (WARNING: old file names will not be kept).", Return(True), Return(False)):

                hide screen show_pic

                python:
                    t = 0
                    filename_counter_dict = {}
                    open_log_file()
                    for pic in girl.pics:
                        t += pic.commit_changes(filename_counter_dict, 1) # Phase 1 - Just fix numbering
                    for pic in girl.pics:
                        t += pic.commit_changes(filename_counter_dict, 2) # Phase 2 - Renaming
                    close_log_file()

                $ bk(str(t) + " changes have been made.")

                bk "Restarting Ren'py now.{w=1}{nw}"

                $ persistent.forced_restart = selected_pic.file_name

                pause 2.0

                $ renpy.utter_restart()

        elif result == "clear":
            $ result = renpy.call_screen("confirm", "Are you sure you want to clear all tags for this picture?", Return(True), Return(False))
            if result:
                $ selected_pic.clear_tags()

        elif result == "clear_all":
            if renpy.call_screen("confirm", "{color=FF0000}This will clear ALL tags for {b}ALL pictures{/b} in this girl pack.{/color}\n\nAre you sure you want to clear ALL tags for this girl pack?", Return(True), Return(False)):
                python:
                    for pic in girl.pics:
                        pic.clear_tags()

        elif result == "search":
            $ search_words = str(renpy.input("Search for tags:", default=search_words)).lower()

            $ search_words = search_words.replace("(", "")
            $ search_words = search_words.replace(")", "")
            $ search_words = search_words.replace("u'tag', ", "")
            $ search_words = search_words.replace("u'", "")
            $ search_words = search_words.replace("'", "")
            $ search_words = search_words.replace(",", "")

            if search_words:
                $ active_filters = search_words.split(" ")

                $ pic_list = girl.get_filtered_pics(filters=active_filters)

                if len(pic_list) == 0:
                    pass # $ selected_pic = None
                elif selected_pic not in pic_list:
                    $ selected_pic = pic_list[0]

        elif result == "clear_search":
            $ search_words = ""
            $ copy_tags = None
            $ active_filters = None
            if not selected_pic:
                $ selected_pic = girl.pics[0]
                
        elif result == "copy_tags":    
            if selected_pic:
                $ copy_tags = selected_pic.get_all_tags()
                
        elif result == "paste_tags":
            if selected_pic:
                $ selected_pic.set_all_tags(copy_tags)
                $ copy_tags = []

        elif result == "browse":
            $ search_words = ""
            $ copy_tags = None
            $ active_filters = None
            jump browse_shortcut # The stuff below seems no longer necessary
            #if persistent.change_log and len(persistent.change_log) > 0 :
            #    if renpy.call_screen("confirm", "Are you sure you want to leave the edit mode without commiting changes? Unsaved changes will be lost.", Return(True), Return(False)):
            #        $ persistent.change_log = {}
            #        jump browse_shortcut
            #else :
            #    jump browse_shortcut


        elif result == "delete":
            $ selected_pic.toggle_delete()

        elif result == "delete and advance":
            $ selected_pic.toggle_delete()
            $ girl.next_pic(filters=active_filters)

        elif result == "quit":
            $ no_changes = (persistent.change_log == None) or (len(persistent.change_log) == 0)
            if no_changes or renpy.call_screen("confirm", "Are you sure you want to return to the main menu? All your changes will be lost.", Return(True), Return(False)):
                $ persistent.change_log = {}
                return

        elif result == "cycle_next":
            $ girl.next_pic(filters=active_filters)

        elif result == "cycle_next_10":
            $ girl.next_pic(filters=active_filters, nb=10)

        elif result == "cycle_next_100":
            $ girl.next_pic(filters=active_filters, nb=100)

        elif result == "cycle_end":
            $ girl.next_pic(filters=active_filters, nb=99999)

        elif result == "cycle_previous":
            $ girl.previous_pic(filters=active_filters)

        elif result == "cycle_previous_10":
            $ girl.previous_pic(filters=active_filters, nb=10)

        elif result == "cycle_previous_100":
            $ girl.previous_pic(filters=active_filters, nb=100)

        elif result == "cycle_home":
            $ girl.previous_pic(filters=active_filters, nb=99999)

        elif result == "jump_to":
            python:
                try:
                    idx = int(renpy.input("Jump to picture #:", default=girl.pics.index(selected_pic)))
                    selected_pic = girl.pics[idx-1]
                except:
                    pass

        # <Chris12 - Tagsets>
        elif result == "cycle_active_tagset":
            $ cycle_tagset()
        # </Chris12 - Tagsets>

        elif result[0] == "tag":
            $ tag = result[1]
            if len(selected_pic_list) == 0:
                $ selected_pic.toggle_tag(tag)
            else:
                python:
                    for pic in selected_pic_list:
                        pic.toggle_tag(tag)
        
        elif result[0] == "carousel_show":
            $ selected_pic = result[1]
        elif result[0] == "carousel_toggle":
            python:
                global selected_pic_list
                pic = result[1]
                if pic in selected_pic_list:
                    selected_pic_list.remove(pic)
                else:
                    selected_pic_list.append(pic)

label select_girl_pack():

    $ total_pics = sum(len(g.pics) for g in girl_list)
    $ delete_count = 0

    if len(girl_list) >= 0:
        $ bk(str(len(girl_list)) + " girls have been found for a total of " + str(total_pics) + " pics.")
    else:
        bk "{b}No girl folders have been found.{/b}\nTo get started, put the girl folders you want to edit inside the 'game\\images' folder."

    "{b}WARNING{b}" "When you commit to your changes, original files will be renamed. You might want to keep a copy of your old girl folders outside the 'game\\images' folder for safety."

    $ result = menu(get_girl_menu(girl_list))

    return

label select_pack_start():
    hide screen main_menu
    scene black
    call select_girl_pack() from _call_select_girl_pack_1
    if not result == "quit":
        $ persistent.girl = result.path
    return

label browse_pack():
    hide screen main_menu
    scene expression "#222222"

    if mode == "import_packstate":
        $ update_result = "Somehow, no Result from import_packstate..."
        python:
            for girl in girl_list:
                if girl.path == persistent.girl:
                    update_result = import_packstate(girl)
        "import_packstate: [update_result]"


    if not persistent.girl:

        call select_girl_pack() from _call_select_girl_pack_2

        if result == "quit":
            return

        $ girl = result
        $ delete_count = 0
        $ persistent.girl = girl.path

    else:
        python:

            for girl in girl_list:
                if girl.path == persistent.girl:
                    break
            else:
                renpy.say("", "Girl path 'persistent.girl' could not be found.")
                persistent.girl = None
                renpy.jump("browse_girl_pack")

    $ selected_pic = girl.pics[0]

label browse_shortcut():

    $ active_filters = []

    show screen show_pic(context="browse")

    while True:

        $ result = ui.interact()

        if result == "cycle_all":
            python:
                global cancelAction
                cancelAction = False
                renpy.run(SetScreenVariable("show_ui", False))
                offset = 1 + girl.pics.index(selected_pic)
                total = len(girl.pics)
                start = datetime.datetime.now()
                for i in xrange(total):
                    girl.next_pic(filters=active_filters)
                    renpy.say("", str(1 + ((i + offset) % total)) + " / " + str(total) + "\n\nRight-Click to stop...{nw}")
                    if cancelAction : break
                else:
                    renpy.say("", "Cycled " + str(i + 1) + " images in " + str((datetime.datetime.now() - start).seconds) + " seconds")
                renpy.run(SetScreenVariable("show_ui", True))

        elif result == "cycle_next":
            $ girl.next_pic(filters=active_filters)

        elif result == "cycle_next_10":
            $ girl.next_pic(filters=active_filters, nb=10)

        elif result == "cycle_next_100":
            $ girl.next_pic(filters=active_filters, nb=100)

        elif result == "cycle_previous":
            $ girl.previous_pic(filters=active_filters)

        elif result == "cycle_previous_10":
            $ girl.previous_pic(filters=active_filters, nb=10)

        elif result == "cycle_previous_100":
            $ girl.previous_pic(filters=active_filters, nb=100)

        elif result == "jump_to":
            python:
                try:
                    idx = int(renpy.input("Jump to picture #:", default=girl.pics.index(selected_pic)))
                    selected_pic = girl.pics[idx-1]
                except:
                    pass

        elif result == "clear":
            $ active_filters = []

        elif result == "edit":
            if not selected_pic: 
                $ selected_pic = girl.pics[0]
            jump edit_shortcut

        elif result == "quit":
            return

        # <Chris12 - Tagsets>
        elif result == "cycle_active_tagset":
            $ cycle_tagset()
        # </Chris12 - Tagsets>

        elif result[0] == "tag":
            $ tag = result[1]
            if tag in active_filters:
                $ active_filters.remove(tag)
            else:
                $ active_filters.append(tag)

            $ pic_list = girl.get_filtered_pics(filters=active_filters)

            if len(pic_list) == 0:
                $ selected_pic = None
            else:
                $ selected_pic = pic_list[0]
        
        elif result[0] == "carousel_show":
            $ selected_pic = result[1] 
        elif result[0] == "carousel_toggle":
            python:
                global selected_pic_list
                pic = result[1]
                if pic in selected_pic_list:
                    selected_pic_list.remove(pic)
                else:
                    selected_pic_list.append(pic)
    return

label pack_stats:
    hide screen main_menu
    scene black

    if not persistent.girl:

        call select_girl_pack() from _call_select_girl_pack_3

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
                renpy.say("", "Girl path 'persistent.girl' could not be found.")
                persistent.girl = None
                renpy.jump("pack_stats")

    show screen pack_stats(girl)

    $ r = ui.interact()

    if r == "tips":
        call screen rating_tips()
        jump pack_stats

    else:
        return

init python:

    def get_girlpack_rating(girl, no_color = False):

        d = girl.evaluate_girlpack()

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

        if no_color:
            return rating
        else:
            return event_color[col] % rating


    def get_pic_list(thing, tags, and_tags = None, not_tags = None, include_bk_autoadds = True):

        tags = make_tuple(tags)
        and_tags = make_tuple(and_tags)
        not_tags = make_tuple(not_tags)

        l = []

        for pic in thing.pics:

            for tag in tags:
                if pic.has_tag(tag, include_bk_autoadds):

                    r = True

                    if not_tags:
                        for not_tag in not_tags:
                            if pic.has_tag(not_tag, include_bk_autoadds):
                                r = False

                    if and_tags:
                        for and_tag in and_tags:
                            if not pic.has_tag(and_tag, include_bk_autoadds):
                                r = False

                    if r:
                        l.append(pic)

        return l


label mytest():

    menu:
        "Show":

            call screen change_log()

        "Clear":
            $ persistent.change_log = {}

        ""

label export_currentstate():
    $ abort = False
    if persistent.change_log and len(persistent.change_log) > 0 :
        if not renpy.call_screen("confirm", "There are still uncommitted changes. Those will NOT get exported. It is recommended to discard or commit them first. Do you want to continue?", Return(True), Return(False)):
            "Aborted."
            $ abort = True
    if not abort:
        "This may take a little, please click or press ENTER to start."
        narrator "Initializing Girls List. The game might not respond, please be patient...{nw}"
        $ girl_list = compile_girl_pics()
        narrator "Exporting...{nw}"
        python :
            export_packstate(girl_list)
        "Done!"
    jump main_menu

label export_allstates() :
    $ abort = False
    if persistent.change_log and len(persistent.change_log) > 0 :
        if not renpy.call_screen("confirm", "There are still uncommitted changes. Those will NOT get exported. It is recommended to discard or commit them first. Do you want to continue?", Return(True), Return(False)):
            "Aborted."
            $ abort = True
    if not abort:
        "This may take a little, please click or press ENTER to start."
        narrator "Initializing Girls List. The game might not respond, please be patient...{nw}"
        $ girl_list = compile_girl_pics()
        narrator "Exporting...{nw}"
        python:
            selected_girl = persistent.girl
            for girl in girl_list :
                persistent.girl = girl.path
                export_packstate(girl_list)
                renpy.say(girl.path, "Exported!{fast}{nw}")
            persistent.girl = selected_girl
        "Done!"
    jump main_menu

label export_girlsdata() :
    $ abort = False
    if persistent.change_log and len(persistent.change_log) > 0 :
        if not renpy.call_screen("confirm", "There are still uncommitted changes. Those will NOT get exported. It is recommended to discard or commit them first. Do you want to continue?", Return(True), Return(False)):
            "Aborted."
            $ abort = True
    if not abort:
        "This may take a little, please click or press ENTER to start."
        narrator "Initializing Girls List. The game might not respond, please be patient...{nw}"
        $ girl_list = compile_girl_pics()
        narrator "Exporting Girls Data...{nw}"
        python:
            with open(config.gamedir + "/../girlsdata.csv", "w") as output :
                output.write("Girl,Images,Rating\n")

                selected_girl = persistent.girl
                for girl in sorted(girl_list, key = lambda x : x.path) :
                    persistent.girl = girl.path
                    output.write(persistent.girl[len("images/"):].replace("," , ";") + ",")
                    output.write(str(len(girl.pics)) + ",")
                    output.write(get_girlpack_rating(girl, no_color = True) + "\n")
                    renpy.say(girl.path, "Exported!{fast}{nw}")
                persistent.girl = selected_girl
        "Done! Exported to girlsdata.csv"
    jump main_menu

label export_debugdata():
    $ abort = False
    if persistent.change_log and len(persistent.change_log) > 0 :
        if not renpy.call_screen("confirm", "There are still uncommitted changes. Those will NOT get exported. It is recommended to discard or commit them first. Do you want to continue?", Return(True), Return(False)):
            "Aborted."
            $ abort = True
    if not abort:
        "This may take a little, please click or press ENTER to start."
        narrator "Initializing Girls List. The game might not respond, please be patient...{nw}"
        $ girl_list = compile_girl_pics()
        narrator "Exporting Girls Data...{nw}"
        python:
            with open(config.gamedir + "/../debugdata.txt", "w") as output :
                selected_girl = persistent.girl
                for girl in sorted(girl_list, key = lambda x : x.path) :
                    persistent.girl = girl.path
                    output.write("\n"+persistent.girl[len("images/"):].replace("," , ";") + "\n")
                    for pic in (girl.pics + girl.ignore_pics):
                        output.write("(" + str(len(pic.tags)) + ") " + pic.file_name + " : ")
                        my_tags = []
                        for tag in pic.tags:
                            tag_entry = optional_tag_dict.get(tag, None)
                            if tag_entry is not None: # tag was found
                                my_tags.append(tag_entry.shorthand)
                            else:
                                my_tags.append(tag)
                        output.write(','.join(sorted(my_tags)))
                        output.write("\n")


                    renpy.say(girl.path, "Exported!{fast}{nw}")
                persistent.girl = selected_girl
        "Done! Exported to debugdata.txt"
    jump main_menu

init python :
    def export_packstate(girl_list) :
        currentgirl = None
        counter = 0
        for girl in girl_list:
            if girl.path == persistent.girl:
                currentgirl = girl
                break

        packStateFilePath = "packstates/" + persistent.girl[len("images/"):] + ".txt"
        hashesSet = set()
        with open(config.gamedir + "/" + packStateFilePath, "w") as output :
            isTrash = True
            for pic in (currentgirl.pics + currentgirl.ignore_pics) :
                if isTrash:
                    isTrash = pic in currentgirl.ignore_pics

                if (isTrash and "duplicate" in pic.file_name) : # skip trash duplicates
                    continue

                if (len(pic.tags) == 0) : # skip untagged
                    continue

                if (pic.get_hash() in hashesSet) : # No hash twice.
                    continue

                hashesSet.add(pic.get_hash())

                counter += 1
                output.write(str(pic.get_filesize()))
                output.write("\n")
                output.write(pic.get_hash())
                output.write("\n")
                if isTrash:
                    output.write('_TRASH')
                else:
                    tagscopy = list(pic.tags)
                    tagscopy.sort(key=sort_tags)
                    #if "bisexual" in tagscopy and "sex" in tagscopy:
                    #    if not (" sex" in pic.file_name or "sex " in pic.file_name or "sex." in pic.file_name) : tagscopy.remove("sex")
                    output.write(' '.join(tagscopy))
                output.write("\n")
        return counter

label main_menu():

    if persistent.forced_restart:

        $ renpy.notify("Loading [persistent.forced_restart]")

        $ last_pic = persistent.forced_restart
        $ persistent.forced_restart = False
        $ girl_list = compile_girl_pics()
        call edit(last_pic) from _call_edit_1

    show screen main_menu()

    $ ui.interact()
