## TagSet Extended - by Chris12

init -1 python:
    tagset_extended = TagSet("Extended", includes=[tagset_core])
    all_tagsets.append(tagset_extended)

    ## Main Tags ##
    
    order1 = all_tags_dict["portrait"].order
    my_order2 = all_tags_dict["portrait"].order2 + 1
    
    main_tags.insert(main_tags_idx["portrait"] + 1, Tag(name="market", order=order1, order2=my_order2, tagsets=[tagset_extended])) # Add it after profile and portrait
    tag_button_dict.update({"market" : "Mar{u}k{/u}et"}) # Main Button Label
    tag_main_help.update({"market" : "{b}Market{/b} images show the girl waiting to be sold, e.g. with a price tag on her, at a slave market, in a cell or cage, etc."})
    add_tag_hotkey("k", "market")
   
    my_order2 += 1
    
    main_tags.insert(main_tags_idx["portrait"] + 2, Tag(name="leave", order=order1, order2=my_order2, tagsets=[tagset_extended])) # Add it after market
    tag_button_dict.update({"leave" : "Leave"}) # Main Button Label
    tag_main_help.update({"leave" : "{b}Leave{/b} images show the girl leaving on a journey/quest, running away, with her back turned to the viewer, etc.\nCombine with emotional tag like happy,angry,sad if applicable."})
   
    order1 = all_tags_dict["geisha"].order
    my_order2 = all_tags_dict["geisha"].order2 + 1
    
    # +2 because another tag was inserted already
    main_tags.insert(main_tags_idx["geisha"] + 2, Tag(name="advertise", order=order1, order2=my_order2, tagsets=[tagset_extended], variants="adver")) # Add it after geisha
    tag_button_dict.update({"advertise" : "Ad{u}v{/u}ertise"}) # Main Button Label
    tag_main_help.update({"advertise" : "Show the girl advertising, possibly in suggestive clothes or naked."})
    add_tag_hotkey("v", "advertise")
    
    main_tags.append(Tag(name="ceremony", tagsets=[tagset_extended], order=order1, order2=my_order2, variants="nun")) # Add it at the end. Nun was deprecated.
    tag_button_dict.update({"ceremony" : "Ceremony"}) # Main Button Label
    tag_main_help.update({"ceremony" : "{b}Ceremony{/b} images show the girl performing a ceremony, doing religious work, praying, meditating, etc."})
    
    my_order2 += 1
    
    main_tags.append(Tag(name="date", tagsets=[tagset_extended], order=order1, order2=my_order2)) # Add it at the end
    tag_button_dict.update({"date" : "Date"}) # Main Button Label
    tag_main_help.update({"date" : "Shows the girl being out on a {b}date with someone else{/b}. The other person can be implied, if the girl is looking 'out of the computer screen'. If it is another woman, add lesbian."})
    
    order1 = all_tags_dict["geisha"].order + 1
    my_order2 += 1
    
    main_tags.append(Tag(name="party", tagsets=[tagset_extended], order=order1, order2=my_order2)) # Add it at the end
    tag_button_dict.update({"party" : "Party"}) # Main Button Label
    tag_main_help.update({"party" : "Shows the girl being part of a larger group, often with girls from the same franchise. Can be used with sexual images to indicate an orgy of multiple men and multiple women."})
    
    ## Optional Tags ##
    
    offset = 100 # allows for quick reordering of tags with cut&paste.

    ## Mood ##

    order1 = optional_tag_dict["sad"].order # use same order as "sad"
        
    optional_tags.append(Tag(name="embar", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"embar" : "She is looking {b}embarrassed{/b}, blushing, averting her eyes, etc."})
    offset += 1
    
    optional_tags.append(Tag(name="angry", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"angry" : "Her face is showing an expression of anger, rage or hatred."})
    offset += 1
    
    optional_tags.append(Tag(name="refuse", _or = ("profile", "sad", "embar", "angry"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"refuse" : "She is refusing what's asked of her, e.g looking rebellious or unwilling, covering her body, etc."})
    offset += 1
    
    optional_tags.append(Tag(name="hurt", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"hurt" : "She is (being) hurt, sick or exhausted. Can be used for profile and sexual images."})
    offset += 1
    
    ## Costumes ##
    
    order1 = optional_tag_dict["cosplay"].order # use same order as cosplay

    optional_tags.append(Tag(name="apron", _or="waitress", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="waitress"))
    tag_special_help.update({"apron" : "She is wearing an apron"})
    offset += 1
    
    optional_tags.append(Tag(name="china", _or="waitress", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="waitress", variants="cheongsam"))
    tag_special_help.update({"china" : "She is wearing a cheongsam/china dress"})
    offset += 1
    
    optional_tags.append(Tag(name="dress", _or="geisha", _not = s_acts, order=order1, order2=offset, tagsets=[tagset_extended], auto_add="geisha"))
    tag_special_help.update({"dress" : "She is wearing an evening/cocktail dress"})
    offset += 1
    
    optional_tags.append(Tag(name="hooker", _or=("advertise", "public"), order=order1, order2=offset, tagsets=[tagset_extended], auto_add="advertise"))
    tag_special_help.update({"hooker" : "She is wearing clothes clearly identifying her as a prostitute in public."})
    offset += 1
    
    # Removed 2021-03-18
    # optional_tags.append(Tag(name="nun", _or="ceremony", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="ceremony"))
    # tag_special_help.update({"nun" : "She is dressed as a nun"})
    # offset += 1
    
    optional_tags.append(Tag(name="miko", _or="ceremony", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="ceremony"))
    tag_special_help.update({"miko" : "She is wearing traditional miko garment"})
    offset += 1
    
    optional_tags.append(Tag(name="casual", _or=("profile", "sprite"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"casual" : "She is wearing casual clothes, e.g. T-Shirt"})
    offset += 1
    
    optional_tags.append(Tag(name="student", _or="cosplay", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="cosplay"))
    tag_special_help.update({"student" : "She is cosplaying as a student, e.g. wearing a school uniform"})
    offset += 1
    
    optional_tags.append(Tag(name="teacher", _or="cosplay", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="cosplay"))
    tag_special_help.update({"teacher" : "She is cosplaying as a teacher, possibly holding a ruler or pointer stick"})
    offset += 1
    
    optional_tags.append(Tag(name="nurse", _or="cosplay", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="cosplay"))
    tag_special_help.update({"nurse" : "She is cosplaying as a nurse, possibly holding some medical tool"})
    offset += 1
    
    optional_tags.append(Tag(name="santa", _or="cosplay", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="cosplay"))
    tag_special_help.update({"santa" : "She is wearing a santa/christmas outfit"})
    offset += 1
    
    optional_tags.append(Tag(name="bride", _or=("cosplay", "virgin"), order=order1, order2=offset, tagsets=[tagset_extended], auto_add="cosplay"))
    tag_special_help.update({"bride" : "She is wearing a bridal gown"})
    offset += 1
    
    optional_tags.append(Tag(name="catgirl", _or="cosplay", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"catgirl" : "She is cosplaying as a catgirl. For real catgirls, you do not have to add this tag."})
    offset += 1

    ## Activities ##

    order1 = optional_tag_dict["fight"].order

    optional_tags.append(Tag(name="study", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"study" : "She is studying, reading a book or a scroll, etc."})
    sorting_dict.update({"study" : (0, 80)}) # make "study" early in the filename
    offset += 1
    
    ## Locations ## 

    order1 = optional_tag_dict["public"].order # Use same order as public
    
    optional_tags.append(Tag(name="beach", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"beach" : "The image shows the girl at the beach or standing in the sea."})
    offset += 1
    optional_tag_dict["swim"]._or += ("beach",)
    
    optional_tags.append(Tag(name="nature", order=order1, order2=offset, tagsets=[tagset_extended], variants=("garden", "forest")))
    tag_special_help.update({"nature" : "The image shows the girl outside in nature, e.g. a garden or a forest."})
    offset += 1
    
    optional_tags.append(Tag(name="town", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"town" : "The image shows the girl in town, e.g. on a street or a public park."})
    offset += 1
    
    ## Sexual Details ##
    
    order1 = optional_tag_dict["gag"].order # use same order as "gag"

    optional_tags.append(Tag(name="blindfold", _or=("fetish", "naked"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"blindfold" : "Her vision is impaired by a blindfold or something similar."})
    offset += 1
    
    optional_tags.append(Tag(name="collar", _or=("fetish", "naked"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"collar" : "She is wearing a collar."})
    offset += 1
    
    order1 = optional_tag_dict["strap-on"].order # use same order as "strap-on" for following tags
            
    optional_tags.append(Tag(name="is_futa", _or=("lesbian", "bisexual"), order=order1, order2=offset, tagsets=[tagset_extended], lbl="Is Futa", shorthand="isfuta"))
    tag_special_help.update({"is_futa" : "The character herself is a Futanari / Dickgirl in this picture. Combine with 'With Futa' if the character is also with another dickgirl."})
    offset += 1
        
    optional_tags.append(Tag(name="with_futa", _or=("lesbian", "bisexual"), order=order1, order2=offset, tagsets=[tagset_extended], lbl="With Futa", shorthand="withfuta"))
    tag_special_help.update({"with_futa" : "The character is with a Futanari / Dickgirl in this picture. Combine with 'Is Futa' if the character is also a dickgirl."})
    offset += 1
        
    order1 = optional_tag_dict["masturbate"].order # use same order as "masturbate" for following tags
    offset = optional_tag_dict["masturbate"].order2 + 1 # use same order as "masturbate" for following tags
    
    optional_tags.append(Tag(name="cunnilingus", _or=("service", "bisexual", "group"), order=order1, order2=offset, fix_name="cunnilingus", btn_text_size=18))#, tagsets=[tagset_extended]))
    tag_special_help.update({"cunnilingus" : "Her pussy is being licked by her partner."})
    offset += 1
    
    optional_tags.append(Tag(name="tempt", _or=("naked", "dancer", "service", "fetish"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"tempt" : "She is tempting someone to have sex. e.g. massaging her own breasts, provocatively spreading her legs, her pussy or her butt-cheeks."})
    offset += 1

    ## Various ##

    order1 = 500

    optional_tags.append(Tag(name="friend", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"friend" : "Use {b}friend{/b} with non-sexual tags like dancer, if (unlike usual) there is another person on the image.\nDon't use friend with tags like e.g. service or lesbian, which already implicate the existence of some partner."})
    offset += 1
    
    optional_tags.append(Tag(name="virgin", _or="sex", order=order1, order2=offset, tagsets=[tagset_extended], variants="deflo"))
    tag_special_help.update({"virgin" : "She is a virgin, or losing her virginity."})
    offset += 1
    
    optional_tags.append(Tag(name="pregnant", order=order1, order2=offset, tagsets=[tagset_extended], variants="preg"))
    tag_special_help.update({"pregnant" : "She is pregnant.\nTry to avoid tagging both 'pregnant' and 'birth'."})
    offset += 1
    
    optional_tags.append(Tag(name="birth", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"birth" : "She is giving birth. Add tags like 'monster' or 'beast' if the child is not human, she is laying eggs, etc.\nTry to avoid tagging both 'pregnant' and 'birth'."})
    offset += 1

    optional_tags.append(Tag(name="lingerie", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="libido"))
    tag_special_help.update({"lingerie" : "She is wearing sexy underwear/lingerie,"})
    offset += 1
    
    optional_tags.append(Tag(name="panties", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"panties" : "Her panties are visible. If she is showing them deliberately (e.g. lifting her skirt), add libido. If it is an accident, consider adding embarrassed. Together with naked, this tag can indicate half-nakedness."})
    offset += 1

    optional_tags.append(Tag(name="tentacles", _or="monster", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="monster"))
    tag_special_help.update({"tentacles" : "The monster has tentacles or is some kind of tentacle creature."})
    offset += 1
    
    ## Metadata ##

    order1 = 600
    
    optional_tags.append(Tag(name="uncen", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"uncen" : "The image is uncensored."})
    offset += 1
    
    optional_tags.append(Tag(name="sprite", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"sprite" : "The image is transparent and showing only the girl, without any background."})
    offset += 1
    
    optional_tags.append(Tag(name="todo", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"todo" : "This tag is for marking pictures you still are not finished with. If you use todo tags, remember to get rid of them before releasing your girlpack."})
    sorting_dict.update({"todo" : (-20, 0)}) # move todo to the very beginning of the filename
    offset += 1

    # Removed 2021-03-18
    # optional_tags.append(Tag(name="freq_highest", variants="xq", _not=("freq_high", "freq_low"), auto_remove=("freq_high", "freq_low"), order=order1, order2=offset, tagsets=[tagset_extended]))
    # tag_special_help.update({"freq_highest" : "The image will be shown much more often."})
    # offset += 1
    
    optional_tags.append(Tag(name="freq_high", variants="hq", _not=("freq_highest", "freq_low"), auto_remove=("freq_highest", "freq_low"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"freq_high" : "The image will be shown more often."})
    offset += 1
    
    optional_tags.append(Tag(name="freq_low", variants="lq", _not=("freq_highest", "freq_high"), auto_remove=("freq_highest", "freq_high"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"freq_low" : "The image will be shown less often."})
    offset += 1

    optional_tags.append(Tag(name="custom", variants=("custom0", "custom1", "custom2", "custom3", "custom4", "custom5", "custom6", "custom7", "custom8", "custom9"), auto_remove="todo", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_special_help.update({"custom" : "Useful for implementing custom functionality."})
    sorting_dict.update({"custom" : (-15, 0)}) # move custom to the very beginning of the filename
    offset += 1

    ## Sanity Check ##
    sanity_check() # Always do this at the end of adding new tags, it also recalculates important variables