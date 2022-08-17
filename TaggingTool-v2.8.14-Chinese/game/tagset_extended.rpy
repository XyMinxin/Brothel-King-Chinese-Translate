## TagSet Extended - by Chris12

init -1 python:
    tagset_extended = TagSet("Chris12扩展", includes=[tagset_core])
    all_tagsets.append(tagset_extended)

    ## Main Tags ##

    order1 = all_tags_dict["portrait"].order
    my_order2 = all_tags_dict["portrait"].order2 + 1

    main_tags.insert(main_tags_idx["portrait"] + 1, Tag(name="market", order=order1, order2=my_order2, tagsets=[tagset_extended])) # Add it after profile and portrait
    tag_button_dict.update({"market" : "市场"}) # Main Button Label
    tag_main_help.update({"market" : "{b}市场{/b} 图片显示等待被出售的女孩，例如在她身上贴着价格标签、在奴隶市场上、在牢房或笼子里等等。"})
    add_tag_hotkey("k", "market")

    order1 = all_tags_dict["geisha"].order
    my_order2 = all_tags_dict["geisha"].order2 + 1

    # +2 because another tag was inserted already
    main_tags.insert(main_tags_idx["geisha"] + 2, Tag(name="advertise", order=order1, order2=my_order2, tagsets=[tagset_extended], variants="adver")) # Add it after geisha
    tag_button_dict.update({"advertise" : "广告"}) # Main Button Label
    tag_main_help.update({"advertise" : "向女孩展示广告，可能穿着挑逗性的衣服或赤身裸体。"})
    add_tag_hotkey("v", "advertise")

    order1 = all_tags_dict["geisha"].order + 1
    my_order2 = 400

    main_tags.append(Tag(name="ceremony", tagsets=[tagset_extended], order=order1, order2=my_order2, variants="nun")) # Add it at the end. Nun was deprecated.
    tag_button_dict.update({"ceremony" : "仪式"}) # Main Button Label
    tag_main_help.update({"ceremony" : "{b}仪式{/b} 图像显示女孩正在举行仪式、从事宗教工作、祈祷、冥想等。"})

    my_order2 += 1

    main_tags.append(Tag(name="date", tagsets=[tagset_extended], order=order1, order2=my_order2)) # Add it at the end
    tag_button_dict.update({"date" : "约会"}) # Main Button Label
    tag_main_help.update({"date" : "显示该女孩正在{b}与其他人约会{/b}。如果女孩正在“看电脑屏幕外”，则可以暗示另一个人。如果是另一个女人，请添加百合。"})

    my_order2 += 1

    main_tags.append(Tag(name="party", tagsets=[tagset_extended], order=order1, order2=my_order2)) # Add it at the end
    tag_button_dict.update({"party" : "聚会"}) # Main Button Label
    tag_main_help.update({"party" : "显示女孩是更大群体的一部分，通常与来自同一特许经营权的女孩在一起。"})

    ## Optional Tags ##

    offset = 100 # allows for quick reordering of tags with cut&paste.

    ## Mood ##

    order1 = optional_tag_dict["sad"].order # use same order as "sad"

    optional_tags.append(Tag(name="embar", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"embar" : "尴尬"})
    tag_special_help.update({"embar" : "她看起来{b}尴尬{/b}、脸红了、移开了视线等等。"})
    offset += 1

    optional_tags.append(Tag(name="angry", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"angry" : "愤怒"})
    tag_special_help.update({"angry" : "她的脸上流露出愤怒或仇恨的表情。"})
    offset += 1

    optional_tags.append(Tag(name="refuse", _or = ("profile", "sad", "embar", "angry"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"refuse" : "拒绝"})
    tag_special_help.update({"refuse" : "她拒绝接受对她的要求，例如表现出叛逆或不情愿，遮掩自己的身体等。"})
    offset += 1

    optional_tags.append(Tag(name="hurt", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"hurt" : "受伤"})
    tag_special_help.update({"hurt" : "她（正在）受伤、生病或筋疲力尽。 可用于个人资料和性图片。"})
    offset += 1

    ## Costumes ##

    order1 = optional_tag_dict["cosplay"].order # use same order as cosplay

    optional_tags.append(Tag(name="apron", _or="waitress", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="waitress"))
    tag_button2_dict.update({"apron" : "围裙"})
    tag_special_help.update({"apron" : "她穿着围裙"})
    offset += 1

    optional_tags.append(Tag(name="china", _or="waitress", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="waitress", variants="cheongsam"))
    tag_button2_dict.update({"china" : "旗袍"})
    tag_special_help.update({"china" : "她穿着旗袍/中式连衣裙"})
    offset += 1

    optional_tags.append(Tag(name="dress", _or="geisha", _not = s_acts, order=order1, order2=offset, tagsets=[tagset_extended], auto_add="geisha"))
    tag_button2_dict.update({"dress" : "礼服"})
    tag_special_help.update({"dress" : "她穿着晚礼服/鸡尾酒礼服"})
    offset += 1

    optional_tags.append(Tag(name="hooker", _or=("advertise", "public"), order=order1, order2=offset, tagsets=[tagset_extended], auto_add="advertise"))
    tag_button2_dict.update({"hooker" : "妓女"})
    tag_special_help.update({"hooker" : "她穿着的衣服清楚地表明她在公共场合是妓女。"})
    offset += 1

    # Removed 2021-03-18
    # optional_tags.append(Tag(name="nun", _or="ceremony", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="ceremony"))
    # tag_special_help.update({"nun" : "She is dressed as a nun"})
    # offset += 1

    optional_tags.append(Tag(name="miko", _or="ceremony", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="ceremony"))
    tag_button2_dict.update({"miko" : "巫女"})
    tag_special_help.update({"miko" : "她穿着传统的巫女服装"})
    offset += 1

    optional_tags.append(Tag(name="casual", _or=("profile", "sprite"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"casual" : "便装"})
    tag_special_help.update({"casual" : "她穿着便装，例如 T恤"})
    offset += 1

    optional_tags.append(Tag(name="student", _or="cosplay", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="cosplay"))
    tag_button2_dict.update({"student" : "校服"})
    tag_special_help.update({"student" : "她正在扮演学生的角色，例如穿着校服"})
    offset += 1

    optional_tags.append(Tag(name="teacher", _or="cosplay", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="cosplay"))
    tag_button2_dict.update({"teacher" : "老师"})
    tag_special_help.update({"teacher" : "她扮演老师的角色，可能拿着尺子或指针棒"})
    offset += 1

    optional_tags.append(Tag(name="nurse", _or="cosplay", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="cosplay"))
    tag_button2_dict.update({"nurse" : "护士"})
    tag_special_help.update({"nurse" : "她扮演护士的角色，可能拿着一些医疗工具"})
    offset += 1

    optional_tags.append(Tag(name="santa", _or="cosplay", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="cosplay"))
    tag_button2_dict.update({"santa" : "圣诞服"})
    tag_special_help.update({"santa" : "她穿着圣诞老人/圣诞装"})
    offset += 1

    optional_tags.append(Tag(name="bride", _or=("cosplay", "virgin"), order=order1, order2=offset, tagsets=[tagset_extended], auto_add="cosplay"))
    tag_button2_dict.update({"bride" : "婚纱"})
    tag_special_help.update({"bride" : "她穿着婚纱"})
    offset += 1

    optional_tags.append(Tag(name="catgirl", _or="cosplay", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="cosplay"))
    tag_button2_dict.update({"catgirl" : "兽耳"})
    tag_special_help.update({"catgirl" : "她扮演猫女的角色。 对于真正的猫女，您不必添加此标签。"})
    offset += 1

    ## Activities ##

    order1 = optional_tag_dict["fight"].order

    optional_tags.append(Tag(name="study", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"study" : "学习"})
    tag_special_help.update({"study" : "她正在学习，阅读一本书或卷轴等。"})
    offset += 1

    ## Locations ##

    order1 = optional_tag_dict["public"].order # Use same order as public

    optional_tags.append(Tag(name="beach", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"beach" : "海滩"})
    tag_special_help.update({"beach" : "图像显示女孩在海滩或站在海中。"})
    offset += 1
    optional_tag_dict["swim"]._or += ("beach",)

    optional_tags.append(Tag(name="nature", order=order1, order2=offset, tagsets=[tagset_extended], variants=("garden", "forest")))
    tag_button2_dict.update({"nature" : "自然"})
    tag_special_help.update({"nature" : "图像显示了大自然中的女孩，例如 花园或森林。"})
    offset += 1

    optional_tags.append(Tag(name="town", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"town" : "城镇"})
    tag_special_help.update({"town" : "图像显示了镇上的女孩，例如 在街道或公共公园。"})
    offset += 1

    ## Sexual Details ##

    order1 = optional_tag_dict["gag"].order # use same order as "gag"

    optional_tags.append(Tag(name="blindfold", _or=("fetish", "naked"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"blindfold" : "眼罩"})
    tag_special_help.update({"blindfold" : "她的视力被眼罩或类似的东西损害了。"})
    offset += 1

    optional_tags.append(Tag(name="collar", _or=("fetish", "naked"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"collar" : "项圈"})
    tag_special_help.update({"collar" : "她戴着项圈。"})
    offset += 1

    order1 = optional_tag_dict["strap-on"].order # use same order as "strap-on" for following tags

    optional_tags.append(Tag(name="futanari", _or="strap-on", order=order1, order2=offset, tagsets=[tagset_extended], shorthand="futa"))
    tag_button2_dict.update({"futanari" : "扶她"})
    tag_special_help.update({"futanari" : "扶她/有阴茎的女孩"})
    offset += 1

    order1 = optional_tag_dict["masturbate"].order # use same order as "masturbate" for following tags
    offset = optional_tag_dict["masturbate"].order2 + 1 # use same order as "masturbate" for following tags

    optional_tags.append(Tag(name="cunnilingus", _or=("service", "bisexual", "group"), order=order1, order2=offset, fix_name="cunnilingus"))#, tagsets=[tagset_extended]))
    tag_button2_dict.update({"cunnilingus" : "舔阴"})
    tag_special_help.update({"cunnilingus" : "她的阴户正在被她的伴侣舔。"})
    offset += 1

    optional_tags.append(Tag(name="tempt", _or=("naked", "dancer", "service", "fetish"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"tempt" : "诱惑"})
    tag_special_help.update({"tempt" : "她在诱惑某人发生性关系。 例如 按摩她自己的乳房，挑逗地张开她的腿、她的阴户或她的臀部。"})
    offset += 1

    ## Various ##

    order1 = 500

    optional_tags.append(Tag(name="friend", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"friend" : "朋友"})
    tag_special_help.update({"friend" : "将 {b}朋友{/b} 与非性标签（如舞者）一起使用，如果（与往常不同）图像上有另一个人。\n不要将 朋友 与标签一起使用，例如 服务或女同性恋，这已经暗示了某个合作伙伴的存在。"})
    offset += 1

    optional_tags.append(Tag(name="virgin", _or="sex", order=order1, order2=offset, tagsets=[tagset_extended], variants="deflo"))
    tag_button2_dict.update({"virgin" : "处女"})
    tag_special_help.update({"virgin" : "她是处女，或失去童贞。"})
    offset += 1

    optional_tags.append(Tag(name="pregnant", order=order1, order2=offset, tagsets=[tagset_extended], variants="preg"))
    tag_button2_dict.update({"pregnant" : "怀孕"})
    tag_special_help.update({"pregnant" : "她怀孕了。"})
    offset += 1

    optional_tags.append(Tag(name="lingerie", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="libido"))
    tag_button2_dict.update({"lingerie" : "内衣"})
    tag_special_help.update({"lingerie" : "她穿着性感内衣/内衣，"})
    offset += 1

    optional_tags.append(Tag(name="panties", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"panties" : "内裤"})
    tag_special_help.update({"panties" : "她的内裤是可见的。 如果她故意展示（例如掀起裙子）请增加性欲。 如果是意外可以考虑添加尴尬。 与裸体一起，此标签可以表示半裸。"})
    offset += 1

    optional_tags.append(Tag(name="tentacles", _or="monster", order=order1, order2=offset, tagsets=[tagset_extended], auto_add="monster"))
    tag_button2_dict.update({"tentacles" : "触手"})
    tag_special_help.update({"tentacles" : "怪物有触手或者是某种触手生物。"})
    offset += 1

    ## Metadata ##

    order1 = 600

    optional_tags.append(Tag(name="uncen", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"uncen" : "uncen"})
    tag_special_help.update({"uncen" : "该图像没有经过审查。"})
    offset += 1

    optional_tags.append(Tag(name="sprite", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"sprite" : "透明"})
    tag_special_help.update({"sprite" : "图像是透明的，只显示女孩，没有任何背景。"})
    offset += 1

    optional_tags.append(Tag(name="todo", order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"todo" : "待定"})
    tag_special_help.update({"todo" : "此标签用于标记您仍未完成的图片。 如果您使用待办事项标签，请记住在发布您的女孩包之前去除它们。"})
    sorting_dict.update({"todo" : (-20, 0)}) # move todo to the very beginning of the filename
    offset += 1

    # Removed 2021-03-18
    # optional_tags.append(Tag(name="freq_highest", variants="xq", _not=("freq_high", "freq_low"), auto_remove=("freq_high", "freq_low"), order=order1, order2=offset, tagsets=[tagset_extended]))
    # tag_special_help.update({"freq_highest" : "The image will be shown much more often."})
    # offset += 1

    optional_tags.append(Tag(name="freq_high", variants="hq", _not=("freq_highest", "freq_low"), auto_remove=("freq_highest", "freq_low"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"freq_high" : "频率_高"})
    tag_special_help.update({"freq_high" : "图像将更频繁地显示。"})
    offset += 1

    optional_tags.append(Tag(name="freq_low", variants="lq", _not=("freq_highest", "freq_high"), auto_remove=("freq_highest", "freq_high"), order=order1, order2=offset, tagsets=[tagset_extended]))
    tag_button2_dict.update({"freq_low" : "频率_低"})
    tag_special_help.update({"freq_low" : "图像将较少显示。"})
    offset += 1

    # ## 添加新的标签集 ##
    #
    # tagset_extended2 = TagSet("Minxin", includes=[tagset_core])
    # all_tagsets.append(tagset_extended2)
    #
    # ## 主要的标签 ##
    #
    # order1 = all_tags_dict["portrait"].order
    # my_order2 = all_tags_dict["portrait"].order2 + 1
    #
    # main_tags.insert(main_tags_idx["portrait"] + 1, Tag(name="minxin1", order=order1, order2=my_order2, tagsets=[tagset_extended2])) # 添加后标签显示在立绘和头像后面
    # tag_button_dict.update({"minxin1" : "自定义标签"}) # 主要按钮
    # tag_main_help.update({"minxin1" : "{b}minxin1{/b} 你可以随意设置你的标签。"}) # 标签描述

    ## Sanity Check ##
    sanity_check() # Always do this at the end of adding new tags, it also recalculates important variables
