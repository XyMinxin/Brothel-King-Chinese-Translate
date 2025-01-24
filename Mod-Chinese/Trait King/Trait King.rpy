init -4 python:

    traitking_activated = False

    tag_dict = {
    # The key (left-hand side of the ':') is the string of characters BK looks for in the file name. The values (right-hand side) are the actual tags that will be added to the picture in-game.

                # Frequency tags

                "freq_highest" : "freq_highest",
                "freq_high" : "freq_high",
                "freq_low" : "freq_low",
                "freq_lowest" : "freq_lowest",

                # Old frequency tags (for retrocompatibility)

                "xq" : "freq_highest",
                "hq" : "freq_high",
                "lq" : "freq_low",

                # Portrait and profile tags (every girl should have at least one)

                "portrait" : "portrait",

                "profile" : "profile",

                # Specialized profile tags

                "market" : "market", # Used with preference to profile for the slavemarket
                "beauty" : ("profile", "model"), # Model is used for advertising pictures
                "card" : "profile",
#                "ent" : "profile", # Obsolete (conflicts with 'tent')
                "model" : ("profile", "model"), # Model is used for advertising pictures
                "advertise" : "model",
                "quest" : "profile",
                "shop" : "profile",
                "battle" : "fight",
                "fight" : "fight",
                "combat" : "fight",
                "hurt" : "hurt", # Use this instead of 'fight' if it shows her losing a fight

                "gallery" : "gallery", # Used as a background for the girl's CG gallery

                "happy" : "happy",
                "neutral" : "neutral",
                "sad" : "sad",
                "refuse" : "refuse",

                # Rest and work tags (highly recommended)

                "rest" : "rest",
                "ecchi" : ("rest", "libido"),

                "wait" : "waitress",
                "bunny" : ("waitress", "bunny", "cosplay"), # Bunny isn't used for now = cosplay
                "maid" : ("maid"), # Maid is used in the farm (obedience training)

                "danc" : ("dancer", "dance"), # Dancer is used for the job. Dance might be used in the future for classes and quests.
                "run" : ("constitution"), # Run is also used in the farm (constitution training)
                "sing" : ("dancer", "sing"), # Sing might be used in the future for classes and quests.
                "strip" : ("strip", "naked"), # Strip might be used in the future for classes and quests.

                "mass" : "masseuse",
                "swim" : ("swimsuit", "swim"), # Swimsuit might be used in the future for classes and quests. It is a fallback tag if no masseuse pic is found.

                "geisha" : "geisha",
                "etiquette" : "geisha",
                "kimono" : ("geisha", "kimono"), # kimono might be used in the future for classes and quests.
                "date" : "date", # Date is used for free girl interactions and court location profiles, and as a fallback tag for geisha

                "naked" : "naked", # Used in combination with other tags to make a girl appear naked
                "nude" : "naked",

                # Location tags (optional)

                "public" : "public", # The girl is in a publicly accessible place where there might be onlookers. Recommended for sexual events only (in BK)
                "beach" : ("public", "beach", "swimsuit", "swim"), # Beach pictures imply the swimsuit tag
                "nature" : ("public", "nature"), # The girl is in nature (except on a beach), such as in a garden, a forest or a field
                "town" : ("public", "town"), # The girl is in an urban environment, such as a street, a plaza or a market
                "city" : ("public", "town"),

                # Sexual tags (highly recommended)

                "virgin" : "virgin", # Used for images where the girl is losing her virginity

                # Note: Some service tags such as oral or handjob can have an effect on the text used in-game for flavor.

                "service" : "service",
                "mast" : ("mast"), # Most masturbating pics should be tagged service.
                "oral" : ("oral"), # Most oral pics should be tagged service.
                "blowjob" : ("oral"),
                "bj" : ("oral"),
                "cunnilingus" : ("cunni"), # Most cunnilingus pics should be tagged service.
                "hand" : ("handjob"),  # Most handjob pics should be tagged service.
                "titj" : ("titjob"), # Most titjob pics should be tagged service.
                "ttj" : ("titjob"),
                "tits" : ("titjob"),
                "titty" : ("titjob"),

                "sex" : "sex",
                "fuck" : "sex",
                "xxx" : ("sex", "XXX"), # XXX is used for XXX classes only, no need for it in girl packs

                "anal" : "anal",

                "fetish" : "fetish",
                "bdsm" : ("bondage"), # Bondage pics should be tagged fetish.
                "bondage" : ("bondage"),
                "hardcore" : ("fetish", "hardcore"), # hardcore is used for hardcore class stock pictures only, no need to use it in girl packs
                "foot" : ("footjob"), # Footjob pics should be tagged fetish (not service).
                "fj" : ("footjob"),

                # Optional tags: used for special sex acts and the farm. Can be mixed with regular sexual tags (necessary for the farm)

                "group" : "group",
                "bis" : "bisexual", # Bisexual pictures may feature up to one male
                "bisexual" : "bisexual", # This is needed to avoid 'bisexual' detecting the 'sex' tag
                "les" : ("lesbian", "bisexual"), # Lesbian pictures may not feature a male. The bisexual tag is added so that these pictures can proc during the appropriate sex act (the male protagonist is then assumed to be off-camera). Recommended for sexual events only (in BK)

                "beast" : "beast",
                "best" : "beast",

                "big" : "big",
                "stallion" : "big",

                "toy" : "toy", # Toy will be used inside and outside the farm (unless used with machine). Mostly used with service (masturbation) or fetish (administered by someone else).
                "machine" : "machine", # Machine will be excluded from regular events (except fetish if fuzzy tagging is on) and should be used for heavier machinery such as the ones found on the farm.

                "monster" : "monster",
                #"tent" : "monster",

                "libido" : "libido", # For the farm: Girl tending to minions
                "obedience" : "obedience", # For the farm: Girl cleaning up the farm
                "sensitivity" : "sensitivity", # For the farm: Girl tending to Gizel
                "constitution" : "constitution", # For the farm: Girl running in the yard
#                "sports" : "constitution", # Disabled to avoid confusion with watersports

                # Fixation tags: Used for specific fixations (recommended)

                "cosplay" : "cosplay",
                "dild" : ("dildo", "toy"),
                "vibr" : ("vibrator", "toy"),
                "plug" : ("plug", "toy"),
                "dirty" : "dirty",
                "penis w" : ("handjob"), # Most handjob pics should be tagged service as well
                "penisw" : ("handjob"),
                "penis_w" : ("handjob"),
                "penis-w" : ("handjob"),
                "oil" : "wet",
                "wet" : "wet",
                "sub" : "sub",
                "humiliat" : "sub",
                "master" : "sub", # Some Internet packs apparently use this tag, included here to avoid conflict with mast (masturbate)
                "dom" : "dom",
                "gag" : "gag",
                "strap" : "strap-on",
                "role" : "cosplay", # roleplay has been deprecated to cosplay
                "bead" : ("beads", "toy"),

                "irru" : ("deep"), # irrumatio has been deprecated to deepthroat
                "deep" : ("deep"),
                "dt" : ("deep"),
                "double" : "double", # Will add the 'group' tag if not used with the beast/monster/machine tag (hardcoded)
                "finger" : "finger",
                "fist" : "fist",
                "insults" : ("sub"),
                "sixty" : ("69"),
                "watersp" : ("watersports"), # watersports means the girl peeing
                "enema" : ("enema"),
                "kiss" : "kiss",
                "spank" : ("spank"),
                "rim" : "rim",
                "grop" : "grope",
                "fondl" : "fondle",
                "lact" : "lactation",
                "doggy" : "doggy",
                "cowg" : "cowgirl",
                "pile" : "piledriver",
                "spoon" : "spoon",

                "cum" : "cumshot",
                "buk" : ("buk", "cumshot"),
                "cim" : ("cim", "cumshot"),
                "mouth" : ("cim", "cumshot"),
                "cif" : ("cof", "cumshot"),
                "cof" : ("cof", "cumshot"),
                "face" : ("cof", "cumshot"),
                "cih" : ("cih", "cumshot"),
                "coh" : ("cih", "cumshot"),
                "hair" : ("cih", "cumshot"),
                "cob" : ("cob", "cumshot"),
                "body" : ("cob", "cumshot"),
                "shower" : ("cum shower", "cumshot"),
                "swa" : ("cim", "cumshot"),
                "cream" : ("creampie", "cumshot"), # Creampie differs from cum inside in that the dick is shown outside
                "cin" : ("cin", "cumshot"), # Cum inside differs from creampie in that the dick is shown inside her
                "inside" : ("cin", "cumshot"),
                "orgasm" : "orgasm",
                "denied" : "denied",
                "squirt" : ("squirt", "orgasm"),


                # Unused tags: Used for pictures that are ignored by the 'Check untagged girl pics' cheat. Mostly ignore this.

                "death" : "unused",
                #"preg" : "unused", # the pregnant tag might be used one day. One day...

                #activities
                "ceremony" : "ceremony",
                "study" : "study",

                # social
                "party" : "party",
                "friend" : "friend",

                "embar" : "embar",
                "angry" : "angry",
                "tempt" : "tempt",

                # cosplay/apparel
                "apron" : ("apron", "cosplay"),
                "china" : ("china", "geisha"),
                "dress" : "dress",
                "hooker" : ("hooker", "cosplay"),
                "nun" : ("nun", "cosplay"),
                "miko" : ("miko", "cosplay"),
                "casual" : "casual",
                "student" : ("student", "cosplay"),
                "teacher" : ("teacher", "cosplay"),
                "nurse" : ("nurse", "cosplay"),
                "santa" : ("santa", "cosplay"),
                "bride" : ("bride", "cosplay"),
                "catgirl" : ("catgirl", "cosplay"),

                "panties" : "panties",
                "lingerie" : "lingerie",

                # sexual
                "blindfold" : "blindfold",
                "collar" : "collar",
                "tentacles" : ("tentacles", "monster"), # in tag_dict now as "monster"

                # other
                "futanari" : "futanari",
                "pregnant" : "pregnant", # in tag_dict now as an ignored/forbidden tag

                }

init python:
    
    traitking_template = Mod(
        
                ## Basic mod information (Important: Version is used to check for new versions of the mod. Failure to update the version number may lead to broken mods and saved games)
                name = "特质之王汉化版",
                folder = "Trait King",
                creator = "_neronero",
                version = 0.25, # Build 2024-09-13, for BK 0.3t
                pic = "title.webm",
                description = "本模组添加了更多特质，以及围绕特质的玩法和更多的事件。",
                
                ## Mod option menu (access through the Help (click on '?') menu)
                #help_prompts = [("Activate","traitking_activate"),("Deactivate (experimental)","traitking_revert")],
                
                ## Early init label: This will run after the game is started, before the district and brothel is set-up.
                early_label="traitking_early_init",
                                
                ## Init label: This will run when the mod is activated, allowing you to set some variables and events if necessary
                init_label = "traitking_init",
                update_label = "traitking_update"
                
                )

# custom dialogue: new year
    add_dialogue("holiday new year", ("very extravert"), ("新年快乐！ 我有预感，今年正是{i}我{/i}大放异彩的时候！", "主人， 我祝愿您今年{i}万事如意{/i}！", "今年会是，嗯，最棒的一年！", "新年快乐，主人！", "一整年已经过去了？祝您和您的家人一切顺利，主人！"))
    add_dialogue("holiday new year", ("very introvert"), ("祝福您，主人。", "祝一切顺利，主人。", "哦... 一年都过去了？"))
    add_dialogue("holiday new year", ("very idealist"), ("我已经把今年的计划都想好了。你呢，主人？", "让我们让今年成为值得纪念的一年！", "齐心协力，我们今年可以取得更大的成就。"))
    add_dialogue("holiday new year", ("very materialist"), ("新年快乐, [MC.name]。", "谢谢您的指导, [MC.name]。", "让我们为又一个精彩的一年干杯！"))
    add_dialogue("holiday new year", ("very lewd"), ("香槟在哪里？我们得喝酒庆祝一下！", "去年真是太爽了，但我觉得我们可以做得更好！", "干杯， [MC.name]。最好的一年！"))
    add_dialogue("holiday new year", ("very modest"), ("愿太阳神指引您，[MC.name]。新年快乐。", "愿[brothel.name]今年也沐浴在太阳神的光辉下。", "感谢阿里奥斯，我们又迎来了新的一年。我祈愿祂的光能够借我们之手照亮世界！"))
    add_dialogue("holiday new year", ("very dom"), ("新年快乐！让我们尽情享受吧！", "*叹气* 今年我们真的还要在[district.name]度过吗？我想换个环境了。", "我想知道今年[brothel.name]还能提供什么。"))
    add_dialogue("holiday new year", ("very sub"), ("谢、谢谢你做的一切，主人。", "我爱你，主人，祝愿您一切顺利！", "我希望在未来的日子里，我还能帮助[brothel.name]，主人！"))

    # custom dialogue: valentines
    add_dialogue("slave love", ("very extravert"), ("主人，我只想让你和所有人知道... 我爱你！", "我{i}很{/i}爱你，主人！", "你是最棒的，[MC.name]。我爱你胜过世上任何人！"))
    add_dialogue("slave love", ("very introvert"), ("那、那个，现在方便吗？我爱你，主人！", "*吻* 我爱你，我的主人", "*吻* 谢谢你为我做的一切，主人。"))
    add_dialogue("slave love", ("very idealist"), ("你是我一生挚爱 愿我们永不分离", "*吻* 我爱你的一切！", "*脸红* 你真的很特别呢，主人，我爱你。"))
    add_dialogue("slave love", ("very materialist"), ("我崇拜你，主人。", "哦，主人，我只在乎你！", "真不敢相信我居然这么在乎你，主人。"))
    add_dialogue("slave love", ("very lewd"), ("我一直在幻想你会怎么肏我，亲爱的。", "无论什么玩具都比不上骑你的鸡巴，主人。", "啊，操，你弄得我{i}彻底{/i}湿了，[MC.name]。"))
    add_dialogue("slave love", ("very modest"), ("你让我完整，[MC.name]。", "[MC.name]，你要知道你对我有多重要，我爱你！", "哦，[MC.name]，我没法想象你不在了我该怎么办，我爱你！"))
    add_dialogue("slave love", ("very dom"), ("你棒透了，你知道的，对吧？", "我不太擅长说这种事...... 我只是想让你知道，我很在乎你。", "嘿，呃......我只是想坦白，我真的很喜欢你。非常喜欢。"))
    add_dialogue("slave love", ("very sub"), ("我爱你胜过任何人，主人！", "[MC.name]，我只爱你一个，世上唯一的那一个。", "哦，[MC.name]，我的甜心！我爱你，很爱你，很爱！"))
    
    # custom dialogue: salvation (Arios)
    add_dialogue("holiday salvation", ("very extravert"), ("看到街道在每年的这个时候亮起来，不是很有趣吗？", "我总是很惊讶他们是如何把这么多蜡烛放到主教座位上的。"))
    add_dialogue("holiday salvation", ("very introvert"), ("我、我能在房间里点一根蜡烛吗？", "只、只要一根蜡烛，黑暗就不会靠近我了。"))
    add_dialogue("holiday salvation", ("very idealist"), ("多么美好的一天 让我们尽情享受吧。", "我喜欢这样的传统，它让我们所有人走到了一起。", "我喜欢在这一天在赞漫步。无论你在哪，烛火的河流都会指引你去往大教堂。")) # likes holiday
    add_dialogue("holiday salvation", ("very materialist"), ("我们应该在明年这个时候把我们的蜡烛都卖出去，想想看那能捞多少钱！", "我们又在庆祝什么？我不明白。"))
    add_dialogue("holiday salvation", ("very lewd"), ("唉，真麻烦......还不如把这些蜡烛插到大家下面", "这一切有什么意义？浪费我们的时间。"))
    add_dialogue("holiday salvation", ("very modest"), ("愿太阳神之光指引我们的心灵！", "感谢您，主人。愿太阳神保佑所有来[brothel.name]的人。", "主人，您的姿态很庄重，谢谢您", "谢谢您为圣日做的准备，主人。")) # loves holiday
    add_dialogue("holiday salvation", ("very dom"), ("就这些了？", "*叹气* 我今天有更重要的事情要做。"))
    add_dialogue("holiday salvation", ("very sub"), ("*咯咯笑* 你让我拜什么我就拜什么，主人。", "谢谢您，主人。"))
    add_dialogue("holiday salvation evil", ("very extravert"), ("emmm,你不喜欢看到这些蜡烛照亮赞的街道吗？", "好吧，主人，既然你这么说了."))
    add_dialogue("holiday salvation evil", ("very introvert"), ("哦......你不喜欢这个传统节日？", "我、我们不点蜡烛？一根也不点？"))
    add_dialogue("holiday salvation evil", ("very idealist"), ("*嘟着嘴* 为什么我们不能享受今天的庆祝活动呢？", "*叹气* 好吧，这让我的心情糟透了。我想明年总会有的。", "我们可以不庆祝太阳神，但至少请让我们享受这一刻吧！")) # likes holiday
    add_dialogue("holiday salvation evil", ("very materialist"), ("那些蜡烛有火灾危险。安全总比遗憾好。", "反正我也不太在乎这个传统，那就不过节好了。"))
    add_dialogue("holiday salvation evil", ("very lewd"), ("谢谢你说出了该说的话，主人。[brothel.name]在黑暗里有趣多了！", "那就不庆祝，做爱比过节爽。"))
    add_dialogue("holiday salvation evil", ("very modest"), ("*嘟着嘴* 对不起，主人。我得失陪了。", "*啜泣* 哦，主人... 我在为你祈祷！", "*sob* 我希望有一天你能看到太阳神之光，主人。", "*啜泣* 我真不敢相信！我祈祷太阳神能给我们的生活带来光明。")) # loves holiday
    add_dialogue("holiday salvation evil", ("very dom"), ("我们弄完了吗？谁在乎这些节日？", "让我们继续我们的一天，好吗？"))
    add_dialogue("holiday salvation evil", ("very sub"), ("主人不喜欢太阳神？那我也不喜欢！", "如你所愿，主人。"))

    # custom dialogue: night of nights
    add_dialogue("slave defense", ("very extravert"), ("你会保护我们的，对吧，[MC.name]?", "我希望今晚的局面不会太混乱。"))
    add_dialogue("slave defense", ("very introvert"), ("请保护[brothel.name]安全，主人。", "我害怕..."))
    add_dialogue("slave defense", ("very idealist"), ("我们会没事的！我们的安保会处理的。", "我们没什么好怕的。主人会处理好一切。"))
    add_dialogue("slave defense", ("very materialist"), ("如果有必要，我不怕使用武器。", "今晚我准备好了面对一切！"))
    add_dialogue("slave defense", ("very lewd"), ("时不时来点暴力以正视听，没什么不对。", "*叹气* 男孩就是男孩。"))
    add_dialogue("slave defense", ("very modest"), ("主人，保护我！", "啊！我受不了了！"))
    add_dialogue("slave defense", ("very dom"), ("谁敢耍花招，我就割掉他的老二。", "如果你想试探我，那就来吧！"))
    add_dialogue("slave defense", ("very sub"), ("主人，我害怕.....", "主人，我们会没事吗？"))

    # custom dialogue: solstice/hmas
    add_dialogue("holiday hmas", ("very extravert"), ("好吧，我承认！今年我是个淘气的女孩。*咯咯笑*", "哦嚯嚯嚯，欢迎大家来到[brothel.name]！", "科斯莫和圣诞树有什么共同点？它们的头都是个装饰球。"))
    add_dialogue("holiday hmas", ("very introvert"), ("呼呼呼！", "圣诞节快乐，[MC.name]。", "你今天看上去很开心。"))
    add_dialogue("holiday hmas", ("very idealist"), ("外面好冷......让我们依偎在一起，好吗？", "天啊，看看这天气！让我们在被子里亲热一整天吧。*咯咯笑*", "今年大家都太调皮了。"))
    add_dialogue("holiday hmas", ("very materialist"), ("不知道明天会不会收到礼物......", "真希望有人能在我的袜子里放点珍贵的东西。", "祝你圣诞节快乐，[MC.name]。"))
    add_dialogue("holiday hmas", ("very lewd"), ("*咯咯笑* 你今年真是个淘气包！", "*咯咯笑* 你裤子口袋里装着个糖果棒？还是说看到后那东西变大了？", "淘气还是乖巧？这还用问吗？当然是淘气！*咯咯笑*"))
    add_dialogue("holiday hmas", ("very modest"), ("你是个好孩子吗，[MC.name]?", "你明天会送礼物吗，[MC.name]?", "你对我真的很好，[MC.name]，谢谢。"))
    add_dialogue("holiday hmas", ("very dom"), ("你期待圣诞节吗？", "我很高兴我们能在一起。", "不知道今年会不会下雪呢。"))
    add_dialogue("holiday hmas", ("very sub"), ("我是个好女孩吗，[MC.name]?", "不知道今年会不会收到礼物呢。", "我是个淘气还是个乖巧的孩子呢，[MC.name]?"))

    # custom dialogue: birthday congrats
    add_dialogue("slave congrats", ("very extravert"), ("生日快乐，亲爱的。", "恭喜，祝你一切顺利。", "*唱歌* 祝你生日快乐~祝你生日快乐~", "这就是我们的寿星！让我们开始派对吧！"))
    add_dialogue("slave congrats", ("very introvert"), ("生日快乐！祝你今日愉快。", "*咯咯笑* 惊喜！", "生日快乐！", "恭喜你！"))
    add_dialogue("slave congrats", ("very idealist"), ("*唱歌* 祝你生日快乐~祝你生日快乐~", "耶，我们来庆祝吧！", "我们很高兴有你在。", "你值得拥有最棒的生日。恭喜你！"))
    add_dialogue("slave congrats", ("very materialist"), ("那你到底多大了？", "*咯咯笑* 你正穿着{i}那个{/i}在你生日上？", "惊喜！生日快乐，姐妹！", "生日快乐，甜心！"))
    add_dialogue("slave congrats", ("very lewd"), ("为了庆祝，今晚你可以钻进我的被窝。", "生日快乐!", "今晚会一起熬到很晚！", "*挑逗* 有顾客想和你一起庆祝吗"))
    add_dialogue("slave congrats", ("very modest"), ("生日快乐，你看起来容光焕发。", "愿你有一个美好的一天和美好的一年。", "祝贺你！岁月如梭，不是吗？", "天哪，你今天真漂亮。祝你生日快乐。"))
    add_dialogue("slave congrats", ("very dom"), ("你收到礼物了吗？", "有什么期待的礼物吗？", "或许我们可以一起去这座城市玩玩？", "祝贺！"))
    add_dialogue("slave congrats", ("very sub"), ("来，我给大家做了蛋糕。", "生日快乐！来享受这一天吧。", "看你笑得多开心，祝贺你。", "*拥抱* 恭喜！"))
    
    # custom dialogue: birthday-gal
    add_dialogue("slave birthday", ("very extravert"), ("感谢大家的到来，让我们开始派对吧！", "哈哈，为我欢呼吧！！！"))
    add_dialogue("slave birthday", ("very introvert"), ("谢、谢谢，是这样说吧...", "好、好吧，已经足够开心了..."))
    add_dialogue("slave birthday", ("very idealist"), ("*抽泣* 谢谢你们能来...我太爱你们了！", "真是惊喜！谢谢大家。"))
    add_dialogue("slave birthday", ("very materialist"), ("啊哈哈，我相信你们都期待着这一天的到来，所以我的礼物呢？", "啊哈哈！太感谢你们了。那现在我的礼物在哪呢？"))
    add_dialogue("slave birthday", ("very lewd"), ("耶! *咯咯笑* 祝我生日快乐！", "是啊是啊，谢谢我想。脱衣舞娘在哪儿？我要求在我生日的时候有脱衣舞！"))
    add_dialogue("slave birthday", ("very modest"), ("我真的很感激。谢谢！", "啊，真是个惊喜！谢谢大家。"))
    add_dialogue("slave birthday", ("very dom"), ("你们怎么都知道今天是我的生日？", "见鬼，要哭了...谢谢你们。"))
    add_dialogue("slave birthday", ("very sub"), ("啊...谢谢大家...", "谢、谢谢你们..."))
    
    def add_trait_perkless(self, trait, _pos=None, forced=False): # Where 'trait' is an object (important)

        if not forced:
            for t in self.traits:
                if t.name in trait.opposite:
                    return False

        if _pos:
            self.traits.insert(_pos, trait)
        else:
            self.traits.append(trait)

        self.add_effects(trait.effects)

        return True

       
## This label runs when the mod version number is changed
label traitking_update:

    return
    
label traitking_early_init:

    python:
    
        ## GOLD TRAITS
        
        traitking_gold_s = [

                # Vanilla reworked

                Trait(__("Fascinating"), verb="be", eff1 = Effect("change", "job customer capacity", 2), eff2 = Effect("special", "job prestige", 1), archetype="The Courtesan", base_description = "她总是众人瞩目的焦点。"),
                Trait(__("Magnetic"), verb="be", effects=[Effect("boost", "prestige", 0.25, scales_with = "rank"), Effect("boost", "income", 0.01, scales_with = "rank"), Effect("change", "valuation", +100)], archetype="The Model", base_description = "她身上的某些特质让人难以忘怀。"),

                Trait(__("Provocative"), verb="be", effects=[Effect("boost", "dress", 1.0), Effect("gain", "positive fixation", "cosplay")], archetype="The Model", base_description = "她对时尚有独到见解，知道如何穿着打扮才能给人留下深刻印象。"),
                Trait(__("Fashionista"), verb="be a", effects=[Effect("boost", "accessory", 0.1, scales_with = "rank"), Effect("boost", "necklace", 0.1, scales_with = "rank"), Effect("boost", "ring", 0.1, scales_with = "rank")], archetype="The Model", base_description = "说到时尚，她是一个引领潮流的人，Xeros各地的珠宝商都喜欢她的衣服。"),

                Trait(__("Perfectionist"), verb="be a", eff1=Effect("increase satisfaction", "all jobs", 1, chance=0.5), eff2=Effect("personality", "class president"), archetype="The Courtesan", base_description = "她无法接受失败，总是追求完美。"),
                Trait(__("Gifted"), verb="be", effects=[Effect("increase satisfaction", "all sex acts", 1, chance=0.5), Effect("change", "valuation", +100)], archetype="The Bride", base_description = "她知道一些神奇的窍门，能让任何性爱都更加愉悦。"),
                
                # Trait King originals

                Trait(__("Genius"), verb="be a", effects=[Effect("boost", "xp gains", 0.5), Effect("boost", "class results", 2.0), Effect("boost", "all skill gains", 0.25, scales_with = "rank")], archetype="The Escort", base_description = "她非常聪明。"),

                Trait(__("Famously beautiful"), verb = "be", effects = [Effect("change", "beauty", 40), Effect("gain", "reputation", 20), Effect("change", "customers", 4, dice=True, scope="brothel", scales_with="rank"), Effect("change", "valuation", +150)], archetype="The Model", base_description = "她在整个王国都被称为Zan的皇冠上的宝石之一。"),

                Trait(__("Princess"), verb = "be a", effects=[Effect("boost", "prestige", 1.0, scales_with = "rank"), Effect("boost", "job customer budget", 1.0), Effect("boost", "whore customer budget", 1.0), Effect("change", "refinement", 15, scales_with = "rank"), Effect("boost", "upkeep", 4.0), Effect("change", "job obedience target", 80), Effect("change", "whore obedience target", 200), Effect("change", "train obedience target", 50), Effect("personality", "princess"), Effect("gain", "reputation", 100), Effect("change", "valuation", +1000)], archetype="The Courtesan", base_description = "据说她的血管里流淌着皇室的血液。"),
                Trait(__("Royal concubine"), verb = "be a", effects=[Effect("boost", "prestige", 1), Effect("boost", "refinement gains", 0.5), Effect("change", "whore obedience target", -50), Effect("change", "train obedience target", -50), Effect("boost", "tip", 0.25), Effect("boost", "upkeep", 1.0), Effect("gain", "reputation", 25), Effect("change", "valuation", +250)], archetype="The Courtesan", base_description = "传说她曾是国王的嫔妃之一。"),

                Trait(__("Ambitious"), verb = "be", eff1 = Effect("boost", "reputation gains", 0.5), eff2=Effect("boost", "quest results", 1.0), eff3 = Effect("change", "all skill max", 10), archetype="The Player", base_description = "她对成功和攀登社会阶梯充满了决心。"),

                Trait(__("Exhibitionist"), verb="be an", effects=[Effect("boost", "naked bonus", 0.1, scales_with = "rank"), Effect("boost", "libido gains", 0.25), Effect("change", "valuation", +50)], archetype="The Player", base_description = "她喜欢展示自己的裸体，尤其是在陌生人面前。"),

                Trait(__("Karkyrian hymen"), verb = "have a", effects=[Effect("boost", "sex preference increase", -0.75)], base_description = "她的处女膜具有自我修复功能，在性交时会不断撕裂和出血。"),

                Trait(__("Idol"), verb = "be an", effects=[Effect("change", "customers", 8, dice=True, scope="brothel"), Effect("boost", "job customer budget", 0.1, scales_with = "cust nb")], base_description = "她有很多崇拜她的粉丝。")
        ]

        traitking_gold_a = [

                # Vanilla reworked

                Trait(__("Naughty"), verb="be", eff1 = Effect("boost", "tip", 0.1), eff2 = Effect("special", "temptress", 0.33), eff3=Effect("personality", "pervert"), archetype="The Slut", base_description = "她喜欢接受下流的要求。"),
                Trait(__("Lust"), verb="have", eff1=Effect("change", "whore customer capacity", 1), eff2=Effect("change", "libido", 25), archetype="The Escort", base_description = "她对性有无限的欲望。"),
                Trait(__("Warrior"), verb="be a", effects=[Effect("change", "defense", 1, scales_with = "rank"), Effect("change", "security", 1, scope = "brothel", scales_with = "rank"), Effect("personality", "rebel")], base_description = "她是一个训练有素的战士，知道如何保护自己。"),

                Trait(__("Fast learner"), verb="be a", effects=[Effect("boost", "xp gains", 0.25), Effect("boost", "all jp gains", 0.25), Effect("boost", "class results", 1.0), Effect("personality", "class president")], archetype="The Courtesan", base_description = "她是一个求知欲永不满足的模范学生。"),

                Trait(__("Caster"), verb="be a", effects= [Effect("change", "mana", 2, scope="brothel"), Effect("special", "rest shield", 1), Effect("special", "shield", 1), Effect("change", "valuation", +100)], archetype="The Bride", base_description = "她受过精神艺术方面的教育。"),

                Trait(__("Driven"), verb="be", eff1=Effect("boost", "max energy", 0.3), eff2=Effect("boost", "energy", 0.2), eff3=Effect("boost", "quest results", 0.25), archetype="The Player", base_description = "她孜孜不倦地提升自己。"),

                Trait(__("Noble"), verb="be a", effects=[Effect("boost", "prestige", 2), Effect("boost", "upkeep", 2.0), Effect("change", "job obedience target", 50), Effect("change", "whore obedience target", 50), Effect("change", "train obedience target", 25), Effect("change", "valuation", +500), Effect("personality", "prude")], opposite = "Humble", archetype="The Courtesan", base_description = "据说她出身于一个有名的贵族家庭。"),
                Trait(__("Elite"), verb="be", effects=[Effect("special", "ignore budgets", 1), Effect("personality", "princess"), Effect("change", "valuation", +200), Effect("change", "brothel reputation", 5, chance=0.25, scope="brothel")], archetype="The Courtesan", base_description = "她被认为有高贵的关系。顾客认为和她在一起的时间是一种投资，愿意超支。"),

                Trait(__("Naturist"), verb="be a", effects = [Effect("boost", "naked bonus", 0.2), Effect("change", "valuation", +25), Effect("special", "naked", 1)], archetype="The Player", base_description = "她更喜欢裸体做任何事情。"),

                # Trait King originals

                Trait(__("Ferocious"), verb="be", effects=[Effect("change", "all sex skills", 5, scales_with="rank"), Effect("boost", "constitution", 0.25)], archetype="The Escort", base_description = "她在卧室里变成了一头野兽，充满了原始的性能量。"),

                Trait(__("Empyreal"), verb = "be", effects=[Effect("special", "immune", 1), Effect("resist", "hurt", 3)], base_description = "她受到一个强大的咒语的影响，使她对身体暴力免疫。"),

                Trait(__("Nurse"), verb = "be a", effects=[Effect("change", "heal", 1, chance=0.25, scope="brothel"), Effect("increase satisfaction", "masseuse", 1)], base_description = "她作为医学专家有一些经验。"),

                Trait(__("Porter"), verb = "be a", effects=[Effect("boost", "city rewards", 0.05, scales_with = "rank", scope="brothel"), Effect("boost", "resource extraction", 0.25, scope="brothel")], base_description = "她比你认识的任何女孩都要有负担。"),

                Trait(__("Mentor"), verb = "be a", effects=[Effect("special", "skill catch up", 1), Effect("change", "making friends", 1)], base_description = "她和其他女孩相处得很好。"),

                Trait(__("Hustler"), verb = "be a", effects=[Effect("special", "workwhore", 1), Effect("boost", "service preference increase", 0.5), Effect("special", "deep throat", 1), Effect("personality", "schemer")], base_description = "她不介意通过特殊服务赚点外快。"),

                Trait(__("Prodigy"), verb = "be a", effects=[Effect("change", "valuation", +20, scales_with = "rank")], base_description = "她很有潜力。"),
        ]

        traitking_gold_b = [

                # Vanilla reworked

                Trait(__("Skilled tongue"), verb="have a", effects=[Effect("increase satisfaction", "service", 1), Effect("increase satisfaction", "bisexual", 1)], archetype="The Fox", base_description = "她在口交方面非常熟练。"),
                Trait(__("Always wet"), verb="be", effects=[Effect("increase satisfaction", "group", 1), Effect("increase satisfaction", "sex", 1)], archetype="The Escort", base_description = "她总是准备好做爱。不需要前戏。"),
                Trait(__("Tight ass"), verb="have a", eff1=Effect("increase satisfaction", "anal", 1), eff2=Effect("increase satisfaction", "fetish", 1), base_description = "她的直肠又温暖又紧致。"),

                Trait(__("Country girl"), verb="be a", eff1=Effect("special", "all farm weaknesses", 1), eff2=Effect("boost", "farm preference increase", 1.0), eff3=Effect("change", "valuation", -50), archetype="The Maid", base_description = "她喜欢和动物一起工作。不是人类。"),

                Trait(__("Vicious"), verb="be", effects=[Effect("change", "sex", 20), Effect("change", "anal", 20), Effect("change", "fetish", 20), Effect("personality", "bimbo")], archetype="The Escort", base_description = "她过着放荡堕落的生活。"),

                # Trait King originals

                Trait(__("Nymphomaniac"), verb = "be a", effects=[Effect("boost", "libido gains", 0.5), Effect("change", "sex", 25), Effect("change", "sex act requirements", -25), Effect("change", "whore obedience target", -25)], archetype="The Slut", base_description = "她有一种无法控制的性欲。"),

                Trait(__("Enchanting"), verb="be", effects=[Effect("increase satisfaction", "geisha", 1), Effect("gain", "reputation", 25), Effect("change", "refinement", 10), Effect("change", "valuation", +50)], archetype="The Fox", base_description = "她身上有一种迷人的气质。"),
                Trait(__("Eye-catching"), verb = "be", effects=[Effect("increase satisfaction", "dancer", 1), Effect("change", "advertising", 1, scope="brothel", scales_with = "rank")], archetype="The Player", base_description = "她有着令人难以置信的身材，需要你的关注。"),

                Trait(__("Insatiable"), verb = "be", effects=[Effect("change", "libido", 25), Effect("increase satisfaction", "group", 1), Effect("increase satisfaction", "bisexual", 1)], archetype="The Slut", base_description = "她享受同时满足多人的快感。"),
                
                # ? - Kemono (fairy-folk with animal characteristics)
        ]

        traitking_gold_c = [

                # Vanilla reworked

                Trait(__("Playful"), verb="be", effects=[Effect("boost", "service preference increase", 0.25), Effect("boost", "bisexual preference increase", 0.25), Effect("boost", "service jp gains", 1.0), Effect("boost", "waitress jp gains", 1.0)], archetype="The Player", base_description = "她喜欢玩得开心，到处玩。"),
                Trait(__("Wild"), verb="be", effects=[Effect("boost", "sex preference increase", 0.05, scales_with = "rank"), Effect("boost", "group preference increase", 0.05, scales_with = "rank"), Effect("change", "defense", 1)], archetype="The Slut", base_description = "她是个爱冒险的人。"),
                Trait(__("Dirty mind"), verb="have a", effects=[Effect("boost", "anal preference increase", 0.05, scales_with = "rank"), Effect("boost", "fetish preference increase", 0.05, scales_with = "rank")], archetype="The Fox", base_description = "她得超出跨越边界和执行禁忌性行为。"),

                Trait(__("Loose"), verb="be", effects=[Effect("change", "train obedience target", -40), Effect("change", "valuation", -40), Effect("personality", "pet")], archetype="The Player", base_description = "她不介意和她的主人一起尝试新事物，这使她很容易训练。"),
                Trait(__("Dedicated"), verb="be", effects=[Effect("change", "job obedience target", -25), Effect("change", "valuation", -25), Effect("personality", "loyal")], archetype="The Maid", base_description = "她喜欢让自己变得有用。"),
                
                ### NEW IN 0.3
                Trait(__("Conduit"), verb = "be a", eff1 = Effect("change", "mojo cost", -1), archetype="The Fox", base_description = "她的身体对魔酒特别敏感。"), #?

                Trait(__("Dynamo"), verb = "be a", effects = [Effect("boost", "max energy", 0.3), Effect("boost", "energy", 0.15)], base_description = "她浑身散发着炽热的能量。", public=False),
                Trait(__("Lolita"), verb = "be a", effects = [Effect("boost", "tip", 2, chance=0.2)], base_description = "她实际上并没有未成年，但看起来她是未成年的——一些顾客喜欢这样。", public=False),
                Trait(__("Ghost"), verb = "be a", effects = [Effect("special", "immune", 1)], base_description = "她是鬼，用任何正常手段都伤害不了她。", public=False),
                Trait(__("Stalwart"), verb = "be", effects = [Effect("change", "all skill max", 5, scales_with = "rank")], base_description = "不管她做什么，她都会比其他人更努力地训练。", public=False),
                
                # Trait King originals

                Trait(__("Angelic"), verb = "be", effects=[Effect("boost", "reputation gains", 0.5), Effect("special", "effect chance", 0.25), Effect("change", "valuation", +60)], opposite = "Godless", archetype="The Fox", base_description = "她有一种圣人般的气场。"),
                Trait(__("Irresistable"), verb = "be", effects=[Effect("change", "charm", 10, scales_with = "rank"), Effect("boost", "reputation gains", 0.1, scales_with = "rank"), Effect("personality", "superficial")], archetype="The Fox", base_description = "她有一种难以置信的魅力，让人心中充满欲望。"),

                Trait(__("Erudite"), verb = "be", effects=[Effect("change", "refinement", 30), Effect("boost", "class results", 0.5), Effect("boost", "xp gains", 0.5)], archetype="The Courtesan", base_description = "她有教养，受过良好的教育。"),

                Trait(__("Caretaker"), verb = "be a", effects=[Effect("change", "maintenance", 1, scope="brothel", scales_with = "rank"), Effect("increase satisfaction", "waitress", 1)], archetype="The Maid", base_description = "她具有理想女佣的品质。"),

                Trait(__("Anal slut"), verb="be an", effects=[Effect("increase satisfaction", "anal", 1), Effect("boost", "anal preference increase", 0.5), Effect("boost", "anal jp gains", 1.0)], archetype="The Slut", base_description = "她喜欢走后门。"),
                Trait(__("Uninhibited"), verb="be", effects=[Effect("increase satisfaction", "fetish", 1), Effect("boost", "fetish preference increase", 0.5)], archetype="The Slut", base_description = "她没有界限，在极端的性行为中胜过其他女孩。")
        ]

        traitking_gold_special = [

                # Vanilla reworked

                # Trait King originals

                Trait(__("In demand"), verb = "be", eff1 = Effect("change", "valuation", +200), base_description = "她是个抢手货，在奴隶市场上可以卖个好价钱。", public=False),
                Trait(__("Fan favorite"), verb = "be a", eff1 = Effect("change", "valuation", +350), base_description = "她现在非常受欢迎，在奴隶市场上可以卖个好价钱。", public=False)

        ]
        
        traitking_gold_traits = traitking_gold_s + traitking_gold_a + traitking_gold_b + traitking_gold_c + traitking_gold_special
        

        ## POSITIVE TRAITS

        traitking_pos_s = [

                # Vanilla reworked

                # Trait King originals

                Trait(__("Tight pussy"), verb="have a", effects = [Effect("increase satisfaction", "sex", 1, chance=0.75), Effect("change", "sensitivity", 5, scales_with = "rank")], archetype="The Slut", base_description = "她有一个年轻，紧致的阴部，感觉绝对惊人。"),

                Trait(__("Submissive"), verb="be", effects = [Effect("increase satisfaction", "fetish", 1, chance = 0.5), Effect("change", "obedience", 30),  Effect("personality", "masochist"), Effect("change", "valuation", +20)], archetype="The Slut", base_description = "她喜欢被支配。"),
                Trait(__("Good kisser"), verb="be a", effects = [Effect("change", "libido", 20), Effect("increase satisfaction", "bisexual", 1, chance = 0.75)], archetype="The Escort", base_description = "她是个接吻高手。"),
                Trait(__("Bisexual"), verb="be", effects = [Effect("increase satisfaction", "bisexual", 1), Effect("boost", "bisexual chance", 0.25), Effect("change", "valuation", +25)], base_description = "她喜欢取悦女士们，就像取悦男士们一样。"),
                Trait(__("Orgy girl"), verb="be an", effects = [Effect("increase satisfaction", "group", 1), Effect("boost", "group chance", 0.25), Effect("change", "valuation", +30)], archetype="The Slut", base_description = "她想让你和你所有的朋友高兴。"),

                Trait(__("Happy-go-lucky"), verb="be", effects = [Effect("change", "mood", 4), Effect("personality", "sweet")], archetype="The Bride", base_description = "没有什么能让她失望。"),
                Trait(__("Trendy"), verb="be", effects = [Effect("boost", "dress", 0.1), Effect("boost", "accessory", 0.1), Effect("boost", "necklace", 0.1), Effect("boost", "ring", 0.1)], archetype="The Escort", base_description = "她穿着时髦。"),
                Trait(__("Passionate"), verb="be", effects = [Effect("reroll", "job critical failure", 1, chance=0.5)], archetype="The Maid", base_description = "她为自己的工作感到自豪，并为自己设定了很高的标准。"),
                Trait(__("Persuasive"), verb="be", effects = [Effect("boost", "customer penalties", -0.5)], archetype="The Bride", base_description = "她知道怎么达到目的。"),
        ]

        traitking_pos_a = [

                # Vanilla reworked

                Trait(__("Athletic"), verb = "be", eff1 = Effect("boost", "constitution gains", 1.0), eff2 = Effect("increase satisfaction", "dancer", 1, chance=0.5), eff3=Effect("change", "valuation", +10), archetype="The Escort", base_description = "她有一个运动员的身体，非常健康。"),
                Trait(__("Sensitive"), verb = "be", eff1 = Effect("boost", "sensitivity gains", 1.0), eff2 = Effect("gain", "reputation", 10), eff3=Effect("increase satisfaction", "geisha", 1, chance=0.5), archetype="The Bride", base_description = "她很有同理心。"),
                Trait(__("Deft"), verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.25), eff2 = Effect("boost", "masseuse jp gains", 0.5), eff3 = Effect("increase satisfaction", "masseuse", 1, chance=0.5), archetype="The Maid", base_description = "她的手很灵巧。"),

                Trait(__("Energetic"), verb = "be", eff1 = Effect("boost", "max energy", 0.25), eff2=Effect("change", "valuation", +10), archetype="The Player", base_description = "她总是精力充沛。"),

                Trait(__("Strong"), verb = "be", eff1 = Effect("change", "defense", 2), eff2=Effect("change", "security", 2, scope = "brothel"), archetype="The Bride", base_description = "她可能会在扳手腕比赛中打败你。"),

                Trait(__("Sensual"), verb="be", effects = [Effect("change", "beauty", 10), Effect("change", "sensitivity", 10), Effect("change", "customers", 1, dice=False, scope="brothel", scales_with="rank"), Effect("gain", "reputation", 10), Effect("change", "valuation", +20)], archetype="The Model", base_description = "她喜欢拥抱。"),
                Trait(__("Kinky"), verb = "be", effects = [Effect("increase satisfaction", "fetish", 1), Effect("increase satisfaction", "group", 1), Effect("personality", "masochist"), Effect("gain", "reputation", 10), Effect("change", "valuation", +20)], base_description = "如果你拿出鞭子来，她不会介意的。", archetype="The Slut"),

                # Trait King originals

                Trait(__("Groomed"), verb="be", effects = [Effect("change", "refinement", 5, scales_with = "rank"), Effect("change", "all main skills", 10), Effect("gain", "reputation", 10), Effect("change", "valuation", +40)], opposite = "Uncouth", archetype="The Courtesan", base_description = "她受过宫廷淑女风度方面的教育。"),

                Trait(__("Flasher"), verb="be a", effects = [Effect("special", "flasher", 1), Effect("increase satisfaction", "waitress", 1, chance=0.5), Effect("boost", "reputation gains", 0.25)], archetype="The Player", base_description = "她可能会在你最意想不到的时候撩起她的上衣，所以不要眨眼。"),
                Trait(__("Contortionist"), verb="be a", effects = [Effect("increase satisfaction", "dancer", 1, chance=0.5), Effect("change", "advertising", 1, scope = "brothel"), Effect("change", "valuation", +20)], archetype="The Player", base_description = "她的身体足够灵活，可以在周围表演马戏。"),
                Trait(__("Tantric masseuse"), verb="be a", effects = [Effect("increase satisfaction", "masseuse", 1,chance=0.5), Effect("change", "advertising", 1, scope = "brothel")], archetype="The Model", base_description = "她可以通过按摩释放你潜在的性能量。"),
                Trait(__("Multilingual"), verb="be", effects = [Effect("increase satisfaction", "geisha", 1, chance=0.5), Effect("change", "advertising", 1, scope = "brothel")], archetype="The Courtesan", base_description = "她会说好几种语言。"),

                Trait(__("Diligent"), verb = "be", effects=[Effect("boost", "max energy", 0.1), Effect("boost", "energy", 0.1), Effect("boost", "customer penalties", -0.25)], archetype="The Maid", base_description = "她非常细心地工作。"),  

                Trait(__("Fake orgasms"), verb="have", effects = [Effect("increase satisfaction", "sex", 1, chance=0.5), Effect("change", "sex", 20), Effect("change", "valuation", -15, scales_with = "rank")], archetype="The Escort", base_description = "她的呻吟声让人觉得你在渗透她的灵魂。大多数人喜欢它，但不是每个人都相信。"),


        ]

        traitking_pos_b = [

                # Vanilla reworked

                Trait(__("Cute"), verb = "be", eff1 = Effect("change", "beauty", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Player", base_description = "她真是太可爱了。"),
                Trait(__("Nice boobs"), verb = "have", eff1 = Effect("change", "body", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Escort", base_description = "她有幸拥有一对大乳房。"),
                Trait(__("Feminine"), verb = "be", eff1 = Effect("change", "refinement", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Model", base_description = "她是典型的女性。"),
                Trait(__("Horny"), verb = "be", eff1 = Effect("change", "libido", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 10), archetype="The Slut", base_description = "她很容易被激起性欲。"),

                Trait(__("Juicy ass"), verb = "have a", effects = [Effect("increase satisfaction", "anal", 1, chance=0.25)], archetype="The Model", base_description = "玩弄她的屁股是人生最大的乐趣之一。"),

                Trait(__("Exotic"), verb = "be", eff1 = Effect("change", "charm", 20), eff2 = Effect("gain", "reputation", 10), eff3 = Effect("change", "valuation", +100), archetype="The Fox", base_description = "她看起来不像克塞罗斯本地人。"),

                Trait(__("Pretty eyes"), verb = "have", eff1 = Effect("change", "beauty", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +20), archetype="The Model", base_description = "她的眼睛像卡吉尔上空的星星一样闪烁。"),
                Trait(__("Firm tits"), verb = "have", eff1 = Effect("change", "body", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +20), archetype="The Player", base_description = "她的乳房异常结实。有人说，这是因为她的乳房被神奇地增强了，可以威慑邪恶。她的胸是一种好的力量。"),
                Trait(__("Graceful"), verb = "be", eff1 = Effect("change", "refinement", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +30), archetype="The Courtesan", base_description = "她举止优雅，像个公主。"),
                Trait(__("Seductive"), verb = "be", effects=[Effect("change", "charm", 5, scales_with = "rank"), Effect("change", "valuation", +10, scales_with = "rank"), Effect("personality", "superficial")], archetype="The Fox", base_description = "她喜欢采取主动。"),

                Trait(__("Beautiful"), verb = "be", eff1 = Effect("boost", "beauty gains", 1.0), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +20, scales_with = "rank"), archetype="The Model", base_description = "她长得很漂亮。"),

                Trait(__("Slutty"), verb="be", effects = [Effect("change", "libido", 20), Effect("boost", "reputation gains", 0.25), Effect("change", "valuation", +5, scales_with = "rank")], archetype="The Slut", base_description = "她喜欢到处乱搞。"),

                Trait(__("Lucky"), verb = "be", eff1 = Effect("special", "lucky", 1), archetype="The Fox", base_description = "她的生活充满了惊喜。"), 

                Trait(__("Brisk"), verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.5), eff2 = Effect("boost", "dancer jp gains", 0.25), eff3 = Effect("boost", "tip", 0.05), archetype="The Player", base_description = "她又欢快又活泼。"),

                Trait(__("Rowdy"), verb = "be", effects = [Effect("boost", "waitress jp gains", 0.5), Effect("increase satisfaction", "waitress", 1, chance=0.5), Effect("increase satisfaction", "geisha", -2)], opposite=['Modest', 'Unhurried'], archetype="The Player", base_description = "她喜欢事情有点混乱。"),
                Trait(__("Powerful"), verb = "be", effects = [Effect("boost", "dancer jp gains", 0.5), Effect("increase satisfaction", "dancer", 1, chance=0.5), Effect("increase satisfaction", "masseuse", -2), Effect("change", "defense", 1)], opposite=['Modest', 'Unhurried'], archetype="The Bride", base_description = "她往往低估了自己的力量。"),
                Trait(__("Unhurried"), verb = "be", effects = [Effect("boost", "masseuse jp gains", 0.5), Effect("increase satisfaction", "masseuse", 1, chance=0.5), Effect("increase satisfaction", "waitress", -2)], opposite=['Powerful', 'Rowdy'], archetype="The Escort", base_description = "她会把所有的注意力都放在你身上。"),
                Trait(__("Modest"), verb = "be", effects = [Effect("boost", "geisha jp gains", 0.5), Effect("increase satisfaction", "geisha", 1, chance=0.5), Effect("increase satisfaction", "dancer", -2), Effect("personality", "meek")], opposite=['Rowdy', 'Powerful'], archetype="The Fox", base_description = "她周围有一种端庄的气氛。"),

                Trait(__("Pervert"), verb = "be a", effects = [Effect("change", "sex act requirements", -30), Effect("personality", "pervert"), Effect("change", "valuation", +20)], archetype="The Slut", base_description = "她总是不停地想着性。"),

                # Trait King originals

                Trait(__("Sexually curious"), verb = "be", effects = [Effect("boost", "service jp gains", 0.5), Effect("boost", "sex jp gains", 0.5), Effect("change", "all sex skills", 10), Effect("change", "valuation", +40)], archetype="The Escort", base_description = "她喜欢在卧室里获得更多的经验。"),

                Trait(__("Dedicated"), verb="be", eff1=Effect("change", "job obedience target", -50), eff2=Effect("change", "valuation", +10, scales_with = "rank"), archetype="The Maid", base_description = "她喜欢让自己变得有用。"),
                Trait(__("Open-minded"), verb = "be", effects = [Effect("change", "sex act requirements", -50), Effect("boost", "anal jp gains", 0.5), Effect("boost", "fetish jp gains", 0.5)], archetype="The Escort", base_description = "她不轻易评判别人，乐于接受新体验。"),

                Trait(__("Fast orgasms"), verb = "be", effects = [Effect("boost", "libido gains", 1.0), Effect("increase satisfaction", "sex", 1), Effect("increase satisfaction", "group", 1), Effect("boost", "tiredness", 0.2)], archetype="The Slut", base_description = "她很容易达到高潮。"),

                Trait(__("Housekeeper"), verb="be a", effects = [Effect("change", "obedience", 20), Effect("change", "maintenance", 2, scope="brothel")], archetype="The Maid", base_description = "她喜欢做家务。"),


        ]

        traitking_pos_c = [

                # Vanilla reworked

                Trait(__("Long legs"), verb = "have", eff1 = Effect("change", "body", 20), eff2 = Effect("gain", "reputation", 5), archetype="The Model", base_description = "她有修长而又漂亮的腿。"),
                Trait(__("Sweet"), verb = "be", eff1 = Effect("change", "charm", 20), eff2 = Effect("gain", "reputation", 5), eff3 = Effect("personality", "sweet"), archetype="The Bride", base_description = "她只是一个非常好的女孩。"),
                Trait(__("Polite"), verb = "be", eff1 = Effect("change", "refinement", 20), eff2 = Effect("gain", "reputation", 5), archetype="The Courtesan", base_description = "她很有礼貌。"),
                Trait(__("Resilient"), verb = "be", eff1 = Effect("change", "constitution", 20), archetype="The Maid", base_description = "她似乎是一个坚强的女孩。"),
                Trait(__("Delicate"), verb = "be", eff1 = Effect("change", "sensitivity", 20), eff2 = Effect("gain", "reputation", 5), archetype="The Bride", base_description = "她陶醉于亲密的身体接触。"),
                Trait(__("Meek"), verb = "be", eff1 = Effect("change", "obedience", 20), eff2 = Effect("personality", "meek"), archetype="The Maid", base_description = "她是一个温柔温顺的女孩。"),

                Trait(__("Fit"), verb = "be", eff1 = Effect("boost", "body gains", 1.0), eff2 = Effect("boost", "constitution gains", 0.5), eff3=Effect("change", "valuation", +20), archetype="The Player", base_description = "她是一个健康的女孩。"),
                Trait(__("Charming"), verb = "be", eff1 = Effect("boost", "charm gains", 1.0), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +10), archetype="The Fox", base_description = "和她谈话很愉快。"),
                Trait(__("Elegant"), verb = "be", eff1 = Effect("boost", "refinement gains", 1.0), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +40), archetype="The Courtesan", base_description = "她动作十分优雅。"),  

                Trait(__("Obedient"), verb = "be", eff1 = Effect("boost", "obedience gains", 1.0), eff2=Effect("change", "train obedience target", -20), eff3 = Effect("change", "obedience", 10), archetype="The Maid", base_description = "她喜欢服从命令。"),

                Trait(__("Tough"), verb = "be", eff1 = Effect("boost", "hurt", -0.5), archetype="The Maid", base_description = "她从伤病中恢复得比大多数人都快。"),

                Trait(__("Sexy"), verb = "be", eff1 = Effect("boost", "reputation gains", 0.5), eff2 = Effect("gain", "reputation", 10), eff3=Effect("change", "valuation", +40), archetype="The Escort", base_description = "她的屁股很性感。"),
                Trait(__("Humble"), verb = "be", eff1 = Effect("boost", "upkeep", -0.5), archetype="The Maid", base_description = "她不关心奢华的生活。"),

                Trait(__("Sharp"), verb = "be", eff1 = Effect("boost", "xp gains", 0.5), eff2 = Effect("personality", "nerd"), archetype="The Fox", base_description = "她很机智。"),
                Trait(__("Loyal"), verb = "be", eff1 = Effect("boost", "love", 0.5), eff2 = Effect("change", "obedience", 5, scales_with = "rank"), eff3=Effect("change", "valuation", +20), archetype="The Bride", base_description = "她对主人忠心耿耿。"),
                Trait(__("Brave"), verb = "be", eff1 = Effect("boost", "fear", -0.5), eff2 = Effect("change", "security", 1, scope = "brothel"), archetype="The Escort", base_description = "她不容易被吓到。"),

                Trait(__("Nimble"), verb = "be", effects = [Effect("boost", "dancer jp gains", 0.5), Effect("boost", "geisha jp gains", 0.25)], archetype="The Courtesan", base_description = "她总是站着不动。"),
                Trait(__("Soft skin"), verb = "have", eff1 = Effect("change", "beauty", 10), eff2 = Effect("change", "refinement", 10), archetype="The Courtesan", base_description = "她的皮肤柔软、光滑。"),

                Trait(__("Bright"), verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.25), eff2 = Effect("boost", "geisha jp gains", 0.5), archetype="The Fox", base_description = "她有一种令人振奋的人生观。"),
                Trait(__("Agile"), verb = "be", effects = [Effect("boost", "dancer jp gains", 0.5), Effect("boost", "masseuse jp gains", 0.25)], archetype="The Escort", base_description = "她的身体协调性很好。"),

                Trait(__("Thief"), verb = "be a", eff1 = Effect("special", "pickpocket", 1), eff2=Effect("change", "valuation", -25), eff3 = Effect("boost", "income", -0.01, scales_with = "rank"), archetype="The Fox", base_description = "顾客往往把东西交给她保管。"),

                ### NEW IN 0.3
                Trait(__("Sane"), verb = "be", eff1 = Effect("change", "sanity loss", -1), archetype="The Courtesan", base_description = "她的精神异常稳定，不像赞的其他女孩。"),
                Trait(__("Trusting"), verb = "be", eff1 = Effect("change", "fear per day", -1, chance=0.25), archetype="The Maid", base_description = "她对与陌生人见面和交朋友毫无顾忌。"),
                Trait(__("Loving"), verb = "be", eff1 = Effect("change", "love per day", 1, chance=0.25), archetype="The Bride", base_description = "她心胸宽广，接受每个人的本性。"),

                # Trait King originals

                Trait(__("Mind fucked"), verb="be", effects = [Effect("change", "obedience", 250), Effect("change", "job obedience target", -250), Effect("change", "whore obedience target", -250), Effect("change", "train obedience target", -250), Effect("change", "all main skills", -15, scales_with="rank")], archetype="The Slut", base_description = "她已经完全被洗脑了，再也不会质疑主人的命令。"),

                Trait(__("Subservient"), verb = "be", effects=[Effect("boost", "obedience gains", 0.25), Effect("change", "train obedience target", -100), Effect("change", "tip", -10, scales_with="cust nb")], archetype="The Model", base_description = "她喜欢为她的主人服务，更喜欢在他身边，随时照顾他的需要。"), 

                Trait(__("Cum addict"), verb="be a", effects = [Effect("boost", "service jp gains", 0.5), Effect("boost", "service preference increase", 0.2, scales_with = "rank")], archetype="The Slut", base_description = "比起射在脸上，她更喜欢被口爆。"),

                Trait(__("Innocent"), verb = "be", effects = [Effect("change", "charm", 10, scales_with = "rank"), Effect("change", "libido", -25), Effect("gain", "reputation", 10), Effect("change", "valuation", +20)], archetype="The Player", base_description = "她是一个纯洁善良的女孩。"),
                Trait(__("Great figure"), verb = "have a", effects=[Effect("change", "body", 20), Effect("gain", "reputation", 10), Effect("change", "valuation", +10)], archetype="The Model", base_description = "She has a lovely body."), 
                Trait(__("Adorable"), verb = "be", effects = [Effect("change", "beauty", 20), Effect("boost", "max energy", -0.1), Effect("gain", "reputation", 10), Effect("change", "valuation", +5, scales_with = "rank")], archetype="The Model", base_description = "她有一种让你爱上她的魅力。"),

                Trait(__("for Public use"), verb="be", effects = [Effect("boost", "group chance", 0.25), Effect("boost", "tiredness", -0.25), Effect("boost", "tip", -0.15, scales_with="rank"), Effect("change", "whore obedience target", -100), Effect("increase satisfaction", "all jobs", -1)], archetype="The Slut", base_description = "她不介意被房间里的每个人使用。"),

                Trait(__("Beauty mark"), verb="have a", effects = [Effect("change", "beauty", 20)], archetype="The Courtesan", base_description = "She has a unique birthmark on her face."),
                Trait(__("Tattoo"), verb="have a", effects = [Effect("change", "beauty", 10), Effect("change", "charm", 5)], archetype="The Slut", base_description = "她有一个漂亮的纹身。我不会告诉你在哪里，你自己去找吧。"),
                Trait(__("Exotic tattoo"), verb="have an", effects = [Effect("change", "beauty", 10), Effect("change", "charm", 10), Effect("change", "valuation", +40)], archetype="The Escort", base_description = "她有一个独特的纹身，只有在国外才有。"),
                Trait(__("Pierced clit"), verb="have a", effects = [Effect("boost", "sex preference increase", 0.2), Effect("change", "sensitivity", 10), Effect("change", "libido", 10)], archetype="The Slut", base_description = "她的阴蒂被刺穿了。"),
                Trait(__("Pierced navel"), verb="have a", effects = [Effect("boost", "dancer jp gains", 0.5)], archetype="The Model", base_description = "她喜欢露出腹部来炫耀她的海蓝色脐环。"),
                Trait(__("Pierced nipples"), verb="have", effects = [Effect("boost", "service preference increase", 0.25), Effect("change", "sensitivity", 10), Effect("change", "libido", 10)], archetype="The Escort", base_description = "她的乳头穿孔了。"),

                Trait(__("Tomboy"), verb = "be a", effects = [Effect("change", "constitution", 30), Effect("change", "obedience", -20), Effect("change", "valuation", -20)], archetype="The Bride", base_description = "她是一个精力充沛的女孩，却有男孩子的爱好。"),

        ]

        traitking_pos_special = [

                # Vanilla reworked

                Trait(__("Virgin"), verb = "be a", effects=[Effect("special", "virgin", 1), Effect("change", "sensitivity", 10), Effect("change", "sex act requirements", 40), Effect("gain", "reputation", 10, scales_with = "rank"), Effect("change", "valuation", +50, scales_with = "rank")], archetype="The Bride", base_description = "她从未经历过阴道性交。"), # Special trait, goes away after 1st sex

                # Trait King originals
                
                Trait(__("Unknown"), verb = "have an", eff1 = Effect("boost", "prestige", -0.25), base_description = "这女孩对你有所隐瞒。", public=False)

        ]

        traitking_pos_traits = traitking_pos_s + traitking_pos_a + traitking_pos_b + traitking_pos_c + traitking_pos_special
        

        ## NEGATIVE TRAITS
        
        traitking_neg_traits = [

                # Vanilla reworked 
                Trait(__("Plain"), verb = "be", eff1 = Effect("change", "beauty", -10, scales_with = "rank"), opposite = "Cute", base_description = "她有点太普通了。"),
                Trait(__("Scars"), verb = "have", eff1 = Effect("change", "body", -10, scales_with = "rank"), opposite = "Nice boobs", base_description = "她有一些难看的伤疤。"),
                Trait(__("Mean"), verb = "be", eff1 = Effect("change", "charm", -10, scales_with = "rank"), opposite = "Sweet", base_description = "她有时会有点卑鄙。"),
                Trait(__("Rude"), verb = "be", eff1 = Effect("change", "refinement", -10, scales_with = "rank"), opposite = "Polite", base_description = "她有时很不礼貌。"),
                Trait(__("Cold"), verb = "be", eff1 = Effect("change", "libido", -10, scales_with = "rank"), eff2 = Effect("personality", "cold"), opposite = "Horny", base_description = "她不喜欢表露感情。"), # needs evolution desc
                Trait(__("Weak"), verb = "be", eff1 = Effect("change", "constitution", -10, scales_with = "rank"), eff2=Effect("change", "valuation", -20), opposite = "Resilient", base_description = "她有点柔弱。"),
                Trait(__("Rough"), verb = "be", eff1 = Effect("change", "sensitivity", -10, scales_with = "rank"), opposite = "Delicate", base_description = "她不考虑别人的感受。"),
                Trait(__("Defiant"), verb = "be", eff1 = Effect("change", "obedience", -10, scales_with = "rank"), eff2=Effect("change", "valuation", -40), opposite = "Meek", base_description = "她总是不听话。"),
                
                Trait(__("Timid"), verb = "be", eff1 = Effect("boost", "charm gains", -0.5), opposite = "charming", base_description = "她有点胆怯。"),
                Trait(__("Plump"), verb = "be", eff1 = Effect("boost", "body gains", -0.5), opposite = "Fit", base_description = "她太胖了。"),
                Trait(__("Scruffy"), verb = "be", eff1 = Effect("boost", "beauty gains", -0.5), opposite = "Beautiful", base_description = "她的生活很。"),
                Trait(__("Vulgar"), verb = "be", eff1 = Effect("boost", "refinement gains", -0.5), opposite = "Elegant", base_description = "她能像泼妇一样骂人。"),
                Trait(__("Tame"), verb = "be", eff1 = Effect("boost", "libido gains", -0.5), eff2=Effect("change", "valuation", -20), opposite = "Slutty", base_description = "她缺乏想象力。"),
                Trait(__("Frail"), verb = "be", eff1 = Effect("boost", "constitution gains", -0.5), eff2=Effect("change", "valuation", -20), opposite = "Athletic", base_description = "她身体虚弱。"),
                Trait(__("Rebellious"), verb = "be", eff1 = Effect("boost", "obedience gains", -0.5), eff2 = Effect("personality", "rebel"), eff3=Effect("change", "valuation", -50), opposite = "Obedient", base_description = "她不喜服从命令。"),
                Trait(__("Jaded"), verb = "be", eff1 = Effect("boost", "sensitivity gains", -0.5), eff2 = Effect("change", "valuation", -10, scales_with = "rank"), opposite = "Sensitive", base_description = "她讨厌工作。"), # needs evolution desc
                
                Trait(__("Lazy"), verb = "be", eff1 = Effect("boost", "max energy", -0.20), opposite = ["Energetic", "Driven"], base_description = "她宁愿整天躺在床上。"),
                Trait(__("Sickly"), verb = "be", eff1 = Effect("boost", "hurt", +2), eff2=Effect("change", "valuation", -40), opposite = "Tough", base_description = "她可能生病了。"), # needs evolution desc
                
                Trait(__("Homely"), verb = "be", eff1 = Effect("boost", "reputation gains", -0.25), opposite = "Sexy", base_description = "她不是很有魅力。"),
                Trait(__("Expensive"), verb = "be", eff1 = Effect("boost", "upkeep", 1.0), eff2=Effect("change", "valuation", +25), opposite = "Humble", base_description = "她想被当作公主对待。"),
                Trait(__("Slow"), verb = "be", eff1 = Effect("boost", "xp gains", -0.5), eff2 = Effect("boost", "class results", -0.5), opposite = ["Fast learner", "Sharp", "Genius"], base_description = "她的大脑没法正常工作。"),
                Trait(__("Distrustful"), verb = "be", eff1 = Effect("boost", "love gains", -0.5), opposite = "Loyal", base_description = "她是一个独立的女孩。"),
                Trait(__("Fearful"), verb = "be", eff1 = Effect("boost", "fear", 0.5), opposite = "Brave", base_description = "她很容易受惊吓。"),
                Trait(__("Vulnerable"), verb = "be", eff1 = Effect("change", "defense", -4), opposite = ["Strong", "Warrior"], base_description = "她是一个易受攻击的目标。"),
                
                Trait(__("Unlucky"), verb = "be", eff1 = Effect("special", "unlucky", 1), base_description = "她不应该打碎那面魔镜...她被诅咒了。", opposite = "Lucky"),  # needs evolution desc
                
                Trait(__("All thumbs"), verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.5), eff2 = Effect("increase satisfaction", "waitress", -1), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy'], base_description = "她有点没用。"),
                Trait(__("Awkward"), verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.5), eff2 = Effect("increase satisfaction", "dancer", -1), opposite=['Nimble', 'Agile', 'Brisk', 'Powerful'], base_description = "她缺乏机敏。"),
                Trait(__("Brutal"), verb = "be", eff1 = Effect("boost", "masseuse jp gains", -0.5), eff2 = Effect("increase satisfaction", "masseuse", -1), opposite=['Deft', 'Soft skin', 'Agile', 'Unhurried'], base_description = "她容易低估了自己的力量。"),
                Trait(__("Dumb"), verb = "be", effects = [Effect("boost", "geisha jp gains", -0.5), Effect("increase satisfaction", "geisha", -1), Effect("boost", "jp gains", -0.5)], opposite=['Nimble', 'Soft skin', 'Bright', 'Modest'], base_description = "她是愚蠢的。"),
                Trait(__("Oafish"), verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.5), eff2 = Effect("boost", "geisha jp gains", -0.5), opposite=['Nimble', 'Agile', 'Brisk', 'Soft skin', 'Bright'], base_description = "她缺乏礼貌和风度。"),
                Trait(__("Clumsy"), verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.5), eff2 = Effect("boost", "masseuse jp gains", -0.5), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy', 'Soft skin', 'Agile'], base_description = "她缺乏基本的协调能力。"),
                
                Trait(__("Prude"), verb = "be", eff1 = Effect("boost", "service jp gains", -0.5), eff2 = Effect("boost", "sex jp gains", -0.5), eff3=Effect("change", "valuation", -25), opposite = "Naughty", base_description = "她缺乏性欲。"),
                Trait(__("Naive"), verb = "be", eff1 = Effect("boost", "anal jp gains", -0.5), eff2 = Effect("boost", "fetish jp gains", -0.5), eff3=Effect("change", "valuation", +10), opposite = "Kinky", base_description = "她不做奇奇怪怪的事。"),
                Trait(__("Square"), verb = "be", eff1 = Effect("change", "sex act requirements", 50), opposite = "Pervert", base_description = "她不太爱冒险。"),

                ### NEW IN 0.3
                Trait(__("Insane"), verb = "be", eff1 = Effect("change", "sanity loss", 1), opposite = "Sane", base_description = "她精神错乱了。"),

                Trait(__("Distrustful"), verb = "be", eff1 = Effect("change", "fear per day", 1, chance=0.25), opposite = "Trusting", base_description = "她不能相信任何人。"),
                Trait(__("Spiteful"), verb = "be", eff1 = Effect("change", "love per day", -1, chance=0.25), opposite = "Loving", base_description = "她有一种永不满足的欲望去伤害她周围的人。"),

                Trait(__("Earthbound"), verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = "她不会攻击你。但对其他人来说是致命的。", public=False),
                Trait(__("Waterbound"), verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = "她不会攻击你。但对其他人来说是致命的。", public=False),
                Trait(__("Voidbound"), verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = "她不会攻击你。但对其他人来说是致命的。", public=False),
                Trait(__("Firebound"), verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = "她不会攻击你。但对其他人来说是致命的。", public=False),

                # Trait King originals

                Trait(__("Slave brand"), verb="have a", effects = [Effect("boost", "prestige", 1), Effect("change", "valuation", -100)], archetype="The Bride", base_description = "她有一个纹身，上面写着“科斯莫的财产”。如果找到，请归还给合法的主人。"), 
                Trait(__("Lesbian"), verb = "be a", eff1=Effect("increase satisfaction", "all sex acts", -1), eff2=Effect("increase satisfaction", "bisexual", 2), archetype="The Courtesan", base_description = "她不会被男人激起性欲。"), 
                
                Trait(__("City girl"), verb="be a", eff1=Effect("boost", "farm preference increase", -1.0), eff2=Effect("change", "valuation", +40), archetype="The Escort", base_description = "她只知道住在城里。她不喜欢住在乡下。"), 
                Trait(__("Circumcised"), verb = "be", effects = [Effect("change", "libido", -50), Effect("change", "sensitivity", -50), Effect("change", "whore obedience target", 100), Effect("change", "valuation", -60)], base_description = "她的生殖器做了割礼。"),  
                Trait(__("Deceitful"), verb = "be", eff1=Effect("boost", "income", -0.01, scales_with = "rank"), eff2=Effect("change", "valuation", +25), base_description = "她只关心她自己。"), 
                Trait(__("Inbred"), verb = "be an", eff1 = Effect("boost", "love", 0.5), eff2 = Effect("boost", "all jp gains", -0.5), eff3=Effect("change", "valuation", -60), base_description = "她的父亲和母亲有密切的血缘关系。"), 
                Trait(__("Depressed"), verb="be", eff1=Effect("change", "mood", -4), eff2=Effect("boost", "tiredness", 0.2), eff3=Effect("change", "valuation", -50), base_description = "她从生活中感受不到乐趣。"), 

                Trait(__("Chaste"), verb = "be", eff1 = Effect("change", "sex act requirements", 50), eff2 = Effect("change", "whore obedience target", 50), eff3=Effect("change", "valuation", -40), opposite = "Pervert", base_description = "她认为婚外性行为是不道德的。"), 
                Trait(__("Disfigured"), verb = "be", eff1 = Effect("boost", "naked bonus", -0.25), eff2 = Effect("change", "beauty", -10, scales_with = "rank"), eff3=Effect("change", "valuation", -50), opposite = "Nice boobs", base_description = "她遭遇了严重的事故。"),

                Trait(__("Drunkard"), verb="be a", eff1=Effect("change", "obedience", -10, scales_with = "rank"), eff2= Effect("boost", "reputation gains", -0.25), eff3=Effect("change", "valuation", -30), base_description = "她喜欢把自己喝得不省人事。"), 
                # Trait(__("Kidnapped"), verb = "be", eff1=Effect("change", "obedience", -40), eff2 = Effect("personality", "rebel"), eff3=Effect("change", "valuation", -20), base_description = "She was kidnapped and desires to go home."), # needs evolution desc

                Trait(__("Frigid"), verb = "be", eff1 = Effect("change", "libido", -10, scales_with = "rank"), eff2 = Effect("personality", "cold"), eff3=Effect("change", "valuation", -10, scales_with = "rank"), opposite = "Horny", base_description = "她讨厌表露感情。"), 
                Trait(__("Asexual"), verb = "be", effects = [Effect("change", "libido", -50), Effect("change", "valuation", -50), Effect("increase satisfaction", "all sex acts", -1)], opposite = "Pervert", base_description = "她对性关系几乎没有兴趣。"), 

                Trait(__("Dull"), verb = "be", eff1 = Effect("special", "effect chance", -0.5), opposite = ["Brisk", "Energetic", "Wild"], base_description = "她身上从来没有发生过什么有趣的事。"),
                Trait(__("Gluttonous"), verb = "be", eff1 = Effect("change", "constitution", -30), eff2=Effect("change", "valuation", -5, scales_with = "rank"), base_description = "她喜欢吃得有点多。"),
                Trait(__("Uncouth"), verb="be", eff1=Effect("change", "refinement", -40), eff2= Effect("boost", "reputation gains", -0.1), opposite = "Groomed", base_description = "她完全没有礼貌。"),
                Trait(__("Deaf"), verb = "be", eff1 = Effect("change", "obedience", -20), eff2 = Effect("boost", "waitress jp gains", -0.5), eff3=Effect("change", "valuation", -20), base_description = "她听力不好。"),

                Trait(__("Paranoid"), verb = "be", effects=[Effect("boost", "fear gains", 2.0), Effect("change", "defense", 1), Effect("boost", "love gains", -0.25)], base_description = "她觉得有人要抓她。"),
                Trait(__("Strong gag reflex"), verb = "have a", eff1 = Effect("increase satisfaction", "service", -1), base_description = "她曾被许多鸡巴呛得呕吐不止。"),

                Trait(__("Arrogant"), verb = "be", eff1 = Effect("boost", "all jp gains", -0.5), opposite = "Humble", base_description = "她错误地认为世界都围着她转。"),
                Trait(__("Stubborn"), verb = "be", eff1 = Effect("boost", "xp gains", -0.25), eff2 = Effect("boost", "all jp gains", -0.25 ), base_description = "她从不听劝告。"),
                Trait(__("Blind"), verb = "be", eff1 = Effect("change", "defense", -4), eff2 = Effect("change", "sensitivity", 10), eff3=Effect("change", "valuation", -20), base_description = "她的眼睛不太好使。"),
                Trait(__("Greedy"), verb = "be", eff1 = Effect("boost", "upkeep", 2), eff2 = Effect("special", "random item", 1, chance=0.02), opposite = "Humble", base_description = "她要的比她应得的多。"),

                Trait(__("Bloodslut"), verb = "be a", effects=[Effect("change", "whore obedience target", -250), Effect("change", "valuation", -20, scales_with = "rank"), Effect("change", "brothel reputation", -10, scales_with = "rank", chance=0.1, scope="brothel"), Effect("change", "customers", -2, scales_with = "rank", scope="brothel"), Effect("personality", "creep")], opposite = "Virgin", base_description = "她受到歧视，因为她曾在血岛做过人肉飞机杯。"), 
                Trait(__("Half-elf"), verb = "be a", effects=[Effect("boost", "tiredness", -0.1), Effect("boost", "perfect result tip", -0.75)], base_description = "她受到歧视，因为她的血管里混着精灵的血液。"), 
                Trait(__("Monsterkin"), verb = "be a", effects=[Effect("special", "immune", 1), Effect("change", "security", -1, scales_with = "rank", scope = "brothel"), Effect("change", "valuation", -10, scales_with = "rank")], base_description = "她受到歧视，因为人们认为她是由怪物所生。"), 
                Trait(__("Vivified"), verb = "be", effects=[Effect("change", "constitution", -15, scales_with = "rank"), Effect("change", "valuation", +100)], base_description = "人们相信她是被魔术师变出来的非自然生物。"), 
                
                # ? - Desert Pox (debilitating disease with expensive spice addiction)
                

        ]

        traitking_neg_evolved_desc = {  
                    # Evolved negative traits, must contain options for all negative traits
                    # Description:  She tells you that she really wants to try to [text1]
                    # training:       (menu item)

                  "Godless description" : "每个人都需要信仰",
                   "Godless training" : "敬拜神明",
                   "Godless intro" : "您向她传授莎莉娅和太阳神的教义和美德。",
                   "Godless pos_reaction" : "她明白了自己的生命是为更伟大的力量服务的，并开始忏悔自己的罪行。",
                   "Godless neg_reaction" : "她对经文自相矛盾的地方感到非常困惑。",
                   "Godless pic" : "geisha",
                   "Godless and_tag" : "study",
                   
                   "Trauma description" : "走出过去",
                   "Trauma training" : "克服创伤",
                   "Trauma intro" : "你们俩详谈了她的童年，来最终引导出她的贞操问题。",
                   "Trauma pos_reaction" : "她生动地描述了自己对这一事件的记忆，并更好地理解了自己该对这一问题的反应。",
                   "Trauma neg_reaction" : "她崩溃了，开始放声大哭。",
                   "Trauma pic" : "rest",
                   "Trauma and_tag" : "profile",
                   
                   "Dull description" : "更冒险一点",
                   "Dull training" : "体验激动人心的事情",
                   "Dull intro" : "你们一起漫步在赞的大街小巷，故意闯入危险的走廊和小巷，而这些平时是你们不会去探索的。",
                   "Dull pos_reaction" : "她非常喜欢这次郊游，并有很多关于她所见的新故事要讲。",
                   "Dull neg_reaction" : "她绝对不喜欢这样的环境，你偶然发现的东西会让她感到不安。她渴望自己卧室的安全。",
                   "Dull pic" : "town",
                   "Dull and_tag" : "profile",
                   
                   "Mean description" : "别像个傻逼一样。",
                   "Mean training" : "培养善良",
                   "Mean intro" : "你让她夸奖一下希露。",
                   "Mean pos_reaction" : "她称赞希露为妓院所做的大量工作和奉献。",
                   "Mean neg_reaction" : "她恶狠狠地对希露反唇相讥。",
                   "Mean pic" : "profile",
                   "Mean and_tag" : "",
                   
                   "Scars description" : "改善她的身体形象。",
                   "Scars training" : "对着镜子摆出各种姿势",
                   "Scars intro" : "你把她带到一面巨大的立镜前，指示她模仿你的动作，开始摆出各种开放的姿势。",
                   "Scars pos_reaction" : "她对这个游戏非常兴奋，甚至开始当场发明新姿势，让你胆战心惊地跟着她做。",
                   "Scars neg_reaction" : "她无法克服对展露自己伤疤的羞耻，也无法模仿你的肢体语言。",
                   "Scars pic" : "naked",
                   "Scars and_tag" : "profile",
                   
                   "Plain description" : "变得独特",
                   "Plain training" : "吸引更多关注",
                   "Plain intro" : "你命令她穿戴整齐，一边大声唱圣歌，一边在附近散步。",
                   "Plain pos_reaction" : "她穿上衣服，按照你的要求做。她喜欢成为众人瞩目的焦点，并开始越唱越大声。",
                   "Plain neg_reaction" : "她打扮得漂漂亮亮，走来走去，却不敢大声唱圣歌，因为她不敢出风头。",
                   "Plain pic" : "cosplay",
                   "Plain and_tag" : "sing",
                   
                   "Rude description" : "别像个婊子似的。",
                   "Rude training" : "培养尊重",
                   "Rude intro" : "你命令她跪下来舔你的脚。",
                   "Rude pos_reaction" : "她遵从了你的命令，但还是忍不住就舔脚的要求嘲笑了你几句。",
                   "Rude neg_reaction" : "她拒绝按照你的要求去做，并开始辱骂你。",
                   "Rude pic" : "profile",
                   "Rude and_tag" : "sub",

                   "Rough description" : "表现得像个淑女",
                   "Rough training" : "举办正式晚宴",
                   "Rough intro" : "您举办了一场正式晚宴，让她与来自各大公会的代表一起就座。",
                   "Rough pos_reaction" : "她度过了一个愉快的夜晚，而且没有让任何客人感到不快。",
                   "Rough neg_reaction" : "她不小心讲了一个淫秽笑话，惹恼了一位代表。",
                   "Rough pic" : "geisha",
                   "Rough and_tag" : "",

                   "Weak description" : "挺身而出。",
                   "Weak training" : "作战斗训练",
                   "Weak intro" : "您安排她接受竞技场上一名角斗士的一对一训练。",
                   "Weak pos_reaction" : "她刻苦训练，改进自卫方法，并学会了一些新技巧。",
                   "Weak neg_reaction" : "她花在尖叫和哭泣上的时间比实际训练的时间还多。",
                   "Weak pic" : "fight",
                   "Weak and_tag" : "",

                   "Defiant description" : "更遵守规定。",
                   "Defiant training" : "重新整理书架",
                   "Defiant intro" : "您命令她按字母顺序重新整理您的藏书。",
                   "Defiant pos_reaction" : "她勉强服从你的命令。",
                   "Defiant neg_reaction" : "她拒绝在这种琐碎的工作上花时间。",
                   "Defiant pic" : "profile",
                   "Defiant and_tag" : "",

                   "Gluttonous description" : "别吃得像猪一样",
                   "Gluttonous training" : "举办盛宴",
                   "Gluttonous intro" : "您准备了一桌丰盛的饭菜来考验女孩的自制力，并警告她每吃一口就会挨一鞭子。",
                   "Gluttonous pos_reaction" : "她设法克制住自己，不敢靠近任何食物。",
                   "Gluttonous neg_reaction" : "尽管你警告过她，但她还是不听。你说到做到，整晚都在惩罚她。",
                   "Gluttonous pic" : "obedience",
                   "Gluttonous and_tag" : "profile",

                   "Uncouth description" : "梳理仪容",
                   "Uncouth training" : "参观节日",
                   "Uncouth intro" : "你们一起参观一个节日，以便更多地了解当地的风俗和传统。",
                   "Uncouth pos_reaction" : "她表现得很好，没有大吵大闹。",
                   "Uncouth neg_reaction" : "她觉得穿着和服很不舒服，决定在节日过半时脱掉和服。当她裸体玩传统节日游戏时，其他游客都盯着她看。",
                   "Uncouth pic" : "kimono",
                   "Uncouth and_tag" : "naked",

                   "Deaf description" : "学习倾听",
                   "Deaf training" : "买杂物",
                   "Deaf intro" : "您背诵一份杂货清单，命令她记住并到市场购买。",
                   "Deaf pos_reaction" : "她从市场上买回了您要的大部分物品。",
                   "Deaf neg_reaction" : "她从市场回来时带了凉鞋、一瓶润滑油和鱼网袜，这些都不在你的清单上。",
                   "Deaf pic" : "profile",
                   "Deaf and_tag" : "",

                   "Timid description" : "变得更外向",
                   "Timid training" : "敬酒",
                   "Timid intro" : "晚饭前，你命令所有女孩听她敬酒。",
                   "Timid pos_reaction" : "她长话短说，为妓院的美好未来干杯。",
                   "Timid neg_reaction" : "她静静地说了几句话，却无法吸引女孩们的注意力。",
                   "Timid pic" : "profile",
                   "Timid and_tag" : "",

                   "Plump description" : "减轻体重",
                   "Plump training" : "锻炼",
                   "Plump intro" : "你命令她开始绕着妓院跑圈。",
                   "Plump pos_reaction" : "她立即开始奔跑和喘息，直到你让她停下来才会休息。",
                   "Plump neg_reaction" : "她立即开始跑步，但跑了两圈后就摔倒在地，由于体力不支无法爬起来。",
                   "Plump pic" : "constitution",
                   "Plump and_tag" : "",
                   
                   "Scruffy description" : "投入更多的时间来整装打扮。",
                   "Scruffy training" : "涂抹化妆品",
                   "Scruffy intro" : "你建议她试着花一些时间在镜子前打扮自己。",
                   "Scruffy pos_reaction" : "她花了几个小时在镜子前努力突出自己最美的一面。",
                   "Scruffy neg_reaction" : "十分钟后，她回来了，脸上涂满了你所见过的口红、睫毛膏和眼影的最恐怖的组合。",
                   "Scruffy pic" : "portrait",
                   "Scruffy and_tag" : "",

                   "Vulgar description" : "扩大她的......她的词语...... 词汇！",
                   "Vulgar training" : "阅读字典",
                   "Vulgar intro" : "您给了她一本字典，命令她学习五个以字母C开头的新单词。",
                   "Vulgar pos_reaction" : "她饶有兴趣地研究字典，甚至还向您介绍了一个新词：Cacidrosis！你立刻忘记了它什么意思。",
                   "Vulgar neg_reaction" : "她记错了你的指示，把时间花在了查找她已经知道的五个单词上：屄、鸡巴、射精、阴蒂、口交。",
                   "Vulgar pic" : "profile",
                   "Vulgar and_tag" : "",           

                   "Tame description" : "变得更加大胆",
                   "Tame training" : "去裸奔",
                   "Tame intro" : "你命令她裸体穿过市场。",
                   "Tame pos_reaction" : "她鼓起勇气，满足了你的要求，尽管她显然对此感到非常尴尬。",
                   "Tame neg_reaction" : "她在胆大妄为的两秒钟后就胆怯了，跑向一个布料摊，遮住自己的裸体。",   
                   "Tame pic" : "constitution",
                   "Tame and_tag" : "naked",

                   "Frail description" : "学着保护自己",
                   "Frail training" : "挥拳",
                   "Frail intro" : "您指示她击退希露，同时命令希露扮演一个毛手毛脚的醉酒顾客。",
                   "Frail pos_reaction" : "她被抚摸了几下，然后一拳打在希露的裆部！",
                   "Frail neg_reaction" : "希露扑向她，粗暴地揉捏和摸索她，她连站都站不稳。", 
                   "Frail pic" : "lesbian",
                   "Frail and_tag" : "fondle",

                   "Rebellious description" : "跟随你的脚步。",
                   "Rebellious training" : "去约会",
                   "Rebellious intro" : "你把她带到贵族们经常光顾的高级餐厅。",
                   "Rebellious pos_reaction" : "由于害怕违反礼仪，她试图以你为榜样来融入社会。",
                   "Rebellious neg_reaction" : "她不熟悉菜单上的所有菜品，就问他们是否也提供“蛴螬”。当厨师要求她说明白她的要求时，她威胁要和厨师打架。", 
                   "Rebellious pic" : "geisha",
                   "Rebellious and_tag" : "",
                   
                   "Distrustful description" : "学着相信自己的判断",
                   "Distrustful training" : "建立信任练习",
                   "Distrustful intro" : "你站在她身后，告诉她让自己向后倒在你的怀里。",
                   "Distrustful pos_reaction" : "她害怕放弃控制，但最终还是闭上了眼睛，任由自己坠落。当然，你要接住她。",
                   "Distrustful neg_reaction" : "她闭上眼睛，向后仰去，但在倒下的半途中惊慌失措，试图重新站稳。结果，你没能抓住她，她在地板上摔了个狗啃泥。", 
                   "Distrustful pic" : "profile",
                   "Distrustful and_tag" : "",

                   "Fearful description" : "变得更加勇敢",
                   "Fearful training" : "恐怖故事",
                   "Fearful intro" : "傍晚，你带着她在墓地散步。在散步过程中，你开始讲述恐怖故事。",
                   "Fearful pos_reaction" : "她非常害怕，紧紧抱住你的身体，但最终还是保持冷静。",
                   "Fearful neg_reaction" : "在整个行走过程中，她一直在颤抖、出汗，然后在故事最恐怖的部分晕倒了。", 
                   "Fearful pic" : "profile",
                   "Fearful and_tag" : "",

                   "Paranoid description" : "阻止政府污染水源。",
                   "Paranoid training" : "执行秘密任务",
                   "Paranoid intro" : "你假装对她的阴谋论感兴趣，你们俩出发去阻止政府在水源中下毒。",
                   "Paranoid pos_reaction" : "她无法阻止政府的邪恶阴谋，但你们在一起度过了一段美好时光，她对你的信任也与日俱增。",
                   "Paranoid neg_reaction" : "她不小心掉进了水源里，在精神上完全失去了抵抗政府魔法的能力。", 
                   "Paranoid pic" : "profile",
                   "Paranoid and_tag" : "wet",

                   "Homely description" : "穿得更暴露",
                   "Homely training" : "时装表演",
                   "Homely intro" : "你给她多套最能突出她身体的比基尼，让她为你表演一场时装秀。",
                   "Homely pos_reaction" : "她穿着不同类型的暴露泳装来回走动，玩得不亦乐乎。最后一套表演时她全裸走出更衣室，自信满满。",
                   "Homely neg_reaction" : "她是个糟糕的模特，姿势也很难看。您无法欣赏演出，决定中途离场。", 
                   "Homely pic" : "swim",
                   "Homely and_tag" : "",

                   "Prude description" : "对性交更开放",
                   "Prude training" : "举行淫乱派对",
                   "Prude intro" : "你把她扔给色狼，让她免费为你的保安提供服务。",
                   "Prude pos_reaction" : "当她的前面和后面都被保安插进去时，她放荡地尖叫起来。她显然还不习惯，但却乐在其中。",
                   "Prude neg_reaction" : "她很享受前戏，但当他们突然开始插入她的两个洞时，她变得非常不安。", 
                   "Prude pic" : "group",
                   "Prude and_tag" : "double",

                   "Naive description" : "尝试玩性爱玩具和机器",
                   "Naive training" : "前往吉泽尔的工坊",
                   "Naive intro" : "你向她解释吉泽尔车间里各种机器的工作原理。最后她挑了一台，您就开始准备使用。",
                   "Naive pos_reaction" : "当机器开始工作时，她在巨大的性高潮里颤抖。您决定让她绑在机器上几个小时。",
                   "Naive neg_reaction" : "她被吉泽尔千奇百怪的性玩具包围着，无法进入状态，也无法达到高潮。", 
                   "Naive pic" : "machine",
                   "Naive and_tag" : "toy",

                   "Square description" : "学会吸引年轻客户",
                   "Square training" : "公众宣传",
                   "Square intro" : "你建议她在公共场合向年轻男人抛媚眼。",
                   "Square pos_reaction" : "她在城里走来走去，在年轻观众面前掀开衣服，年轻人的鸡巴立刻指向她。她自己也同样在暴露中兴奋起来。",
                   "Square neg_reaction" : "她觉得不好意思立即暴露自己，而是试图用谈话来引出话题。男人们似乎对此不感兴趣。", 
                   "Square pic" : "public",
                   "Square and_tag" : "naked",

                   "Strong gag reflex description" : "学会给大鸡巴口交",
                   "Strong gag reflex training" : "把你巨大的鸡巴拿出来！",
                   "Strong gag reflex intro" : "你把她带到你的马厩，让那里的种马操她的嘴，直到她的嘴麻木为止。",
                   "Strong gag reflex pos_reaction" : "她不满足只被堵住嘴，让巨大的马屌插进喉咙，窒息加剧了她的潮吹。",
                   "Strong gag reflex neg_reaction" : "她控制不住自己，最终开始呕吐在马的大鸡巴上。", 
                   "Strong gag reflex pic" : "big",
                   "Strong gag reflex and_tag" : "oral",

                   "All thumbs description" : "学着让自己更有用",
                   "All thumbs training" : "清理妓院",
                   "All thumbs intro" : "你让她为妓院做些家务。",
                   "All thumbs pos_reaction" : "她尽其所能，设法打扫卧室。",
                   "All thumbs neg_reaction" : "她不小心打碎了一些东西，制造了比开始时更多的混乱。", 
                   "All thumbs pic" : "maid",
                   "All thumbs and_tag" : "obedience",

                   "Awkward description" : "学着在舞台上感觉自如",
                   "Awkward training" : "在舞台上跳舞",
                   "Awkward intro" : "你告诉她，最好的学习方法就是直面恐惧，放手一搏。",
                   "Awkward pos_reaction" : "她成功地隐藏了自己的焦虑，并在舞台上表演了引人入胜的舞蹈。",
                   "Awkward neg_reaction" : "她仍然非常紧张，最终在表演舞蹈时跌跌撞撞地摔倒了。", 
                   "Awkward pic" : "dancer",
                   "Awkward and_tag" : "",

                   "Brutal description" : "考验她的力量",
                   "Brutal training" : "掰手腕比赛",
                   "Brutal intro" : "你决定在她和你的保安之间安排一场掰手腕比赛。",
                   "Brutal pos_reaction" : "她想方设法打败保安，玩得不亦乐乎。",
                   "Brutal neg_reaction" : "游戏戛然而止，因为她成功地扭断了一名保安的胳膊。", 
                   "Brutal pic" : "fight",
                   "Brutal and_tag" : "",

                   "Dumb description" : "讲一个巧妙的笑话",
                   "Dumb training" : "讲笑话",
                   "Dumb intro" : "你告诉她尽力逗笑你。",
                   "Dumb pos_reaction" : "她讲了这样一个笑话：'{i}" + rand_choice(jokes["harmless"]) + "{/i}'",
                   "Dumb neg_reaction" : "她肯定在哪里听过这样一个笑话，但她却讲砸了: '{i}" + rand_choice(jokes["mean"]) + "{/i}'", 
                   "Dumb pic" : "profile",
                   "Dumb and_tag" : "",

                   "Oafish description" : "接触更多有文化的受众",
                   "Oafish training" : "谈论政治",
                   "Oafish intro" : "你问她对国王的外交政策有何看法。",
                   "Oafish pos_reaction" : "她承认自己的无知，但接着开始思考外来文化丰富我们文化的方式。",
                   "Oafish neg_reaction" : "她显然毫无头绪，试图编造国王的嫖娼政策来回答你的问题。", 
                   "Oafish pic" : "geisha",
                   "Oafish and_tag" : "",

                   "Clumsy description" : "化拙为巧，成为一名小丑",
                   "Clumsy training" : "扮演小丑",
                   "Clumsy intro" : "您命令她在舞台上表演小丑。",
                   "Clumsy pos_reaction" : "她一上台就被绊倒，大家都觉得很好笑。",
                   "Clumsy neg_reaction" : "她总是设法掩饰自己的笨拙。不幸的是，这让她的表演变得残缺不全，因为这让她的小丑表演失去了乐趣。", 
                   "Clumsy pic" : "cosplay",
                   "Clumsy and_tag" : "dancer",

                   "Slow description" : "提高警惕",
                   "Slow training" : "与卫兵一起训练",
                   "Slow intro" : "您允许她和卫兵一起训练。",
                   "Slow pos_reaction" : "通过与卫兵一起训练，她设法提高了反应速度。",
                   "Slow neg_reaction" : "她的速度太慢，跟不上卫兵的步伐，在大多数训练情况下很快就会被制服。", 
                   "Slow pic" : "fight",
                   "Slow and_tag" : "",

                   "Arrogant description" : "学会谦逊",
                   "Arrogant training" : "自我反思",
                   "Arrogant intro" : "您请她简要描述一下自己最大的缺点。",
                   "Arrogant pos_reaction" : "她对自己的描述出奇地准确，甚至还提到由于她的傲慢，她发现自己很难提高。",
                   "Arrogant neg_reaction" : "她想了很久，然后说，她在所有方面都太优秀了，相比之下，她周围的人都显得很糟糕。", 
                   "Arrogant pic" : "profile",
                   "Arrogant and_tag" : "rest",

                   "Stubborn description" : "学习成为角斗士",
                   "Stubborn training" : "参观竞技场",
                   "Stubborn intro" : "您允许她参观竞技场，并与其中一位角斗士交谈。他提议安排一场格斗比赛。",
                   "Stubborn pos_reaction" : "她被打得屁滚尿流，开始怀疑自己成为著名角斗士的想法。",
                   "Stubborn neg_reaction" : "她在擂台上被打得落花流水，但却仍然固执地不放弃成为著名角斗士的想法。", 
                   "Stubborn pic" : "hurt",
                   "Stubborn and_tag" : "fight",

                   "Lazy description" : "学会勤奋工作",
                   "Lazy training" : "严格训练计划",
                   "Lazy intro" : "你要为她制定严格的训练计划，让她努力提高自己。",
                   "Lazy pos_reaction" : "她立即开始训练，并为此付出了很多努力，但显然她并没有从健身中获得乐趣。",
                   "Lazy neg_reaction" : "她没有决心坚持你的严格计划，中途放弃了。", 
                   "Lazy pic" : "constitution",
                   "Lazy and_tag" : "",

                   "Blind description" : "改善视力",
                   "Blind training" : "看眼科医生",
                   "Blind intro" : "你带她去见一位精通治疗魔法的巫师，他试图用咒语治愈她的失明。",
                   "Blind pos_reaction" : "她奇迹般地恢复了一些视力。然而，当她问你举起了几根手指时，她的回答却大相径庭。",
                   "Blind neg_reaction" : "她还是瞎得像只蝙蝠。", 
                   "Blind pic" : "portrait",
                   "Blind and_tag" : "",

                   "Vulnerable description" : "探索她照顾人远离危险的能力",
                   "Vulnerable training" : "从事护士工作",
                   "Vulnerable intro" : "您建议她可以尝试在更安全的环境中工作，照顾老人。",
                   "Vulnerable pos_reaction" : "她非常热爱自己的护士工作，但似乎对护理精神不稳定的人升起了特别兴趣。",
                   "Vulnerable neg_reaction" : "她与一位客户大打出手，因为他竟敢说嫖娼是不道德的。", 
                   "Vulnerable pic" : "masseuse",
                   "Vulnerable and_tag" : "cosplay",

                   "Expensive description" : "证明她应该加薪",
                   "Expensive training" : "向她提出挑战",
                   "Expensive intro" : "你说如果她能在半小时内让吉泽尔的所有魔物射出牛奶，她就可以加薪。",
                   "Expensive pos_reaction" : "她付出了巨大的努力，在规定的时间内满足了整个怪物巢穴。如果她能继续保持这样的成绩，也许她就值得加薪了。",
                   "Expensive neg_reaction" : "她使出浑身解数，让大多数怪物多次猛烈射精，但却无法在规定时间内满足整个巢穴", 
                   "Expensive pic" : "monster",
                   "Expensive and_tag" : "",

                   "Greedy description" : "用她的黄金改善穷人的生活",
                   "Greedy training" : "向济贫院捐款",
                   "Greedy intro" : "你建议她把自己的财富分给穷人。",
                   "Greedy pos_reaction" : "她同意了，并捐出了大量黄金，甚至还去贫民院的施粥处帮忙。",
                   "Greedy neg_reaction" : "她同意济贫院是一项伟大的事业，象征性地认捐了5金，并不住地夸耀自己的善举。", 
                   "Greedy pic" : "profile",
                   "Greedy and_tag" : "town",
                   
                   "Cold description" : "挠痒痒",
                   "Cold training" : "挠痒痒攻击！",
                   "Cold intro" : "你跃跃欲试，开始给她挠痒痒。",
                   "Cold pos_reaction" : "她面带微笑，轻松地承受着你的挠痒。",
                   "Cold neg_reaction" : "你无法逗她笑，她用恼怒的咕哝来回应身体上的亲密接触。", 
                   "Cold pic" : "sensitivity",
                   "Cold and_tag" : "embar",

                   "Jaded description" : "放松",
                   "Jaded training" : "监督其他女孩",
                   "Jaded intro" : "您建议她练习担任监督角色，为年轻女孩提供支持。",
                   "Jaded pos_reaction" : "女孩们反映她的指导非常好。",
                   "Jaded neg_reaction" : "女孩们拒绝承认她的权威，混乱随之而来。", 
                   "Jaded pic" : "party",
                   "Jaded and_tag" : "bisexual",

                   "Sickly description" : "写作诗歌",
                   "Sickly training" : "写一首诗歌",
                   "Sickly intro" : "你建议她写写自己的生活。",
                   "Sickly pos_reaction" : "她创作了一首关于疾病和苦难的凄美俳句，让人不禁潸然泪下。",
                   "Sickly neg_reaction" : "她写了一首粗俗的打油诗，描写一个叫南塔克特的地方的妓女，听起来沉闷得可怕。", 
                   "Sickly pic" : "study",
                   "Sickly and_tag" : "geisha",
                   
                   "Unlucky description" : "战胜厄运",
                   "Unlucky training" : "聆听励志演讲",
                   "Unlucky intro" : "你开始了一段关于坚持不懈、不要让梦想成为白日梦的励志独白。",
                   "Unlucky pos_reaction" : "她看起来精神抖擞，准备向众神发起挑战。",
                   "Unlucky neg_reaction" : "在你演讲到一半时，她脸色苍白，瘫倒在地。也许是你的演讲太紧张了。", 
                   "Unlucky pic" : "sensitivity",
                   "Unlucky and_tag" : "sub",
                   
                   "Slave brand description" : "破坏科斯莫的妓院",
                   "Slave brand training" : "潜入'HʘʘKERS'",
                   "Slave brand intro" : "您鼓励她潜入并破坏科斯莫的妓院'HʘʘKERS'，起初她有些犹豫，但经过说服，她接受了你的挑战。",
                   "Slave brand pos_reaction" : "当她神不知鬼不觉地从窗户爬进去时，你分散了守卫的注意力。过了一会儿，她又回来了，还得意洋洋地炫耀主卧室的枕头上装饰着她的排泄物。",
                   "Slave brand neg_reaction" : "你们引开了守卫，但她鼓不起勇气潜入店内。你们俩决定改天再试一次。", 
                   "Slave brand pic" : "town",
                   "Slave brand and_tag" : "profile",
                   
                   "Lesbian description" : "取悦更多女性",
                   "Lesbian training" : "女士优先",
                   "Lesbian intro" : "您邀请她的几位女性朋友前来，让她们使用妓院收藏的情趣用品。",
                   "Lesbian pos_reaction" : "她自信地率先引导朋友们达到多重高潮。",
                   "Lesbian neg_reaction" : "当她的朋友们坚持要你留下来看她们玩时，这个计划就适得其反了。她们争吵不休，争夺你的关注。", 
                   "Lesbian pic" : "lesbian",
                   "Lesbian and_tag" : "toy",
                   
                   "City girl description" : "探索城市",
                   "City girl training" : "约会",
                   "City girl intro" : "你带她去大教堂附近的一家高级餐厅约会。",
                   "City girl pos_reaction" : "当她兴致勃勃地分享她在这座城市期间的各种趣闻轶事时，你们俩度过了一段美好时光。",
                   "City girl neg_reaction" : "当她喋喋不休地讲述她在妓院的生活时，你很快感到无聊和无趣。", 
                   "City girl pic" : "town",
                   "City girl and_tag" : "date",
                   
                   "Circumcised description" : "在Cathredra教堂祈祷",
                   "Circumcised training" : "去Cathedra教堂",
                   "Circumcised intro" : "您为她点燃蜡烛，命令她把蜡烛带到主教座堂，祈求太阳神的祝福。",
                   "Circumcised pos_reaction" : "她把蜡烛带到了Cathredra。当她回到妓院时，她激情澎湃地宣布太阳神在她心中点燃了火焰。",
                   "Circumcised neg_reaction" : "在她前往主教座堂的途中，一阵强风吹灭了蜡烛的火焰。她悲痛欲绝。", 
                   "Circumcised pic" : "ceremony",
                   "Circumcised and_tag" : "sub",
                   
                   "Deceitful description" : "赚点外快",
                   "Deceitful training" : "鼓励操控顾客",
                   "Deceitful intro" : "你教她一些简单的技巧，让她可以用来操纵顾客。",
                   "Deceitful pos_reaction" : "她学得很快，操纵别人似乎是她的天性。",
                   "Deceitful neg_reaction" : "她意识到你过去曾对她使用过其中的一些技巧。她停下脚步，开始怀疑你的动机。", 
                   "Deceitful pic" : "model",
                   "Deceitful and_tag" : "tempt",
                   
                   "Inbred description" : "了解她的血统",
                   "Inbred training" : "查阅档案",
                   "Inbred intro" : "你们一起去图书馆，抱着微弱的希望，希望能在家谱记录中发现些什么。",
                   "Inbred pos_reaction" : "你向她解释了近亲繁殖在皇室中是多么普遍。尽管您找不到任何证据，她还是开始认为自己可能是公主。",
                   "Inbred neg_reaction" : "您无法发现任何有关她祖先的新信息。祝你下次好运！", 
                   "Inbred pic" : "study",
                   "Inbred and_tag" : "profile",
                   
                   "Depressed description" : "她试图自杀",
                   "Depressed training" : "陪伴她",
                   "Depressed intro" : "你们一起散步。你向她解释，她可以把你当作支柱，不必独自承受痛苦。",
                   "Depressed pos_reaction" : "她从你的话语中得到了安慰，并获得了一些继续前进的力量。",
                   "Depressed neg_reaction" : "她花了整整一天的时间讲述不同自杀方式的优缺点。显然，她为此花了不少心思。", 
                   "Depressed pic" : "profile",
                   "Depressed and_tag" : "sad",
                   
                   "Chaste description" : "教育客户禁欲",
                   "Chaste training" : "提倡节欲",
                   "Chaste intro" : "当您鼓励她向妓院游客宣传禁欲的愚蠢计划时，您努力克制住了想笑的冲动。",
                   "Chaste pos_reaction" : "顾客们笑得很开心。他们似乎相信她是在开玩笑，只是在扮演一个清教徒来讽刺教会的教义。",
                   "Chaste neg_reaction" : "当她出丑时，顾客们都笑得合不拢嘴。", 
                   "Chaste pic" : "nun",
                   "Chaste and_tag" : "profile",
                   
                   "Disfigured description" : "去找专家修复她的毁容",
                   "Disfigured training" : "访问专家",
                   "Disfigured intro" : "你带她去找一位身体修复专家，他混合使用了魔法和外科手术来改善她的外貌。",
                   "Disfigured pos_reaction" : "手术顺利完成。",
                   "Disfigured neg_reaction" : "结果令人大跌眼镜。一种毁容被另一种毁容所掩盖。", 
                   "Disfigured pic" : "hurt",
                   "Disfigured and_tag" : "rest",
                   
                   "Drunkard description" : "喝得昏迷不醒",
                   "Drunkard training" : "进行干预",
                   "Drunkard intro" : "你要她直面因酗酒给大家带来的痛苦和挫折。",
                   "Drunkard pos_reaction" : "她真的被你的话感动了，并承诺要改善自己的生活。",
                   "Drunkard neg_reaction" : "她认为你反应过度了，建议你可以喝点酒放松一下。", 
                   "Drunkard pic" : "dom",
                   "Drunkard and_tag" : "libido",
                   
                   # "Kidnapped description" : ".",
                   # "Kidnapped training" : "",
                   # "Kidnapped intro" : ".",
                   # "Kidnapped pos_reaction" : ".",
                   # "Kidnapped neg_reaction" : ".", 
                   # "Kidnapped pic" : "",
                   # "Kidnapped and_tag" : "",
                   
                   "Frigid description" : "rebuff customers who make a move on her.",
                   "Frigid training" : "Mentorship by the guards",
                   "Frigid intro" : "You pair her up with one of the guards, instructing him to teach her some basic grapples and de-escalation techniques.",
                   "Frigid pos_reaction" : "She learns a few psychological techniques and restraining holds. And more importantly, she now carries herself with much more confidence than before.",
                   "Frigid neg_reaction" : "Their training abruptly comes to an end when the guard becomes a bit too intimate with her. She fights him off and flees to her room.", 
                   "Frigid pic" : "fight",
                   "Frigid and_tag" : "constitution",
                   
                   "Asexual description" : "do her bit to help the brothel succeed.",
                   "Asexual training" : "Pursue excellence",
                   "Asexual intro" : "You make it clear to her that whoring is a brothel's bread and butter. If she has no interest in sexual acts, then she'd better excel at something else to make up for that.",
                   "Asexual pos_reaction" : "She takes your message to heart and vigorously studies to improve herself further, without leaving her comfort zone.",
                   "Asexual neg_reaction" : "She attempts to become a bit more comfortable with whoring, but has a tough time making any progress at all.", 
                   "Asexual pic" : "study",
                   "Asexual and_tag" : "student",
                   
                   "Bloodslut description" : "rip someone's dick off the next time a customer dares to call her a Bloodslut.",
                   "Bloodslut training" : "Overcome prejudice",
                   "Bloodslut intro" : "Sadly prejudice against Meatsleeves from the Blood Islands is commonplace in Zan. You tell her to take comfort in the fact that loyal customers have grown very fond of her.",
                   "Bloodslut pos_reaction" : "Radical changes can start in small ways. She agrees that the best way to deal with this is to befriend more customers, to make them realise that Meatsleeves are ordinary people too.",
                   "Bloodslut neg_reaction" : "She remains frustrated. It's tough to see the positives when some visitors still regularly hurl insults at her head.", 
                   "Bloodslut pic" : "model",
                   "Bloodslut and_tag" : "happy",
                   
                   "Half-elf description" : "improve public opinion regarding elves.",
                   "Half-elf training" : "End racism?",
                   "Half-elf intro" : "You decide to position her as a rolemodel for young girls, spinning her elven heritage within a positive message of overcoming obstacles and challenging preconceptions.",
                   "Half-elf pos_reaction" : "The message is recieved well, but not by the demographic you had expected. Her popularity among pubescent boys skyrockets as the seeds for change are planted in their young and impressionable minds.",
                   "Half-elf neg_reaction" : "Regrettably the message doesn't take root and the majority of Zanic society still distrusts the elves.", 
                   "Half-elf pic" : "model",
                   "Half-elf and_tag" : "dom",
                   
                   "Monsterkin description" : "control her animalistic instincts.",
                   "Monsterkin training" : "Channel the anger",
                   "Monsterkin intro" : "She tells you about her temperamental nature. You suggest that she could bring it into an act of roleplay and play a ruthless dominatrix.",
                   "Monsterkin pos_reaction" : "She really enjoys bossing the customers around. It's as if she was born to prey on them.",
                   "Monsterkin neg_reaction" : "She might be bit too ruthless for comfort. Some of her clients break down in tears.", 
                   "Monsterkin pic" : "dom",
                   "Monsterkin and_tag" : "teacher",

                   "Vivified description" : "dispel the rumours that she's a magician's creation.",
                   "Vivified training" : "Allow the Magician's Guild to study her",
                   "Vivified intro" : "You send her to the magicians guild to conduct a thorough investigation of her personhood. The magicians seem very excited by this opportunity.",
                   "Vivified pos_reaction" : "The magicians are fascinated by her. It's not often that they get to study a real girl so intimately. They are unable to unanimously agree that she's an ordinary person.",
                   "Vivified neg_reaction" : "The studious magicians become a bit nervous in the presence of a female. They're unable to complete their investigation and inform you that she'll have to return at a later date.", 
                   "Vivified pic" : "sensitivity",
                   "Vivified and_tag" : "ceremony",
                   
                   }

         # Boost applies a % increase (or decrease). Value is a float number
         # Change applies a fixed value change which is not limited by stat max. Change can be reversed. Value is a number. 
         # Gain applies a one time permanent gain and is limited by stat max. Gain cannot be reversed. Value is a number.
         # Set replaces a base value with the new value
         # Allow unlocks a brothel option
         # Special is hard-coded

        ## 进化出的负面特质
        
        traitking_neg_evolved = { 
                "Godless" : Trait(__("Devout"), verb = "be", eff1 = Effect("boost", "reputation gains", 0.1), base_description = "她曾经迷失，但现在忠实地侍奉她的上帝。", public=False),
                "Trauma" : Trait(__("Stoic"), verb="be", effects = [Effect("boost", "love", -0.2), Effect("boost", "fear", -0.4)], base_description = "尽管她违背自己的意愿失去了童贞，但她情绪稳定。", public=False),
                "Dull" : Trait(__("Curious"), verb = "be", eff1 = Effect("special", "effect chance", 0.1), base_description = "她曾经过着受保护的生活，但现在她邀请新的体验进入她的生活。", public=False),
                "Mean" : Trait(__("Reserved"), verb = "be", eff1 = Effect("change", "charm", -5, scales_with = "rank"), eff2 = Effect("change", "refinement", 10), base_description = "她脾气很坏，但每当充满消极情绪时，她就尽量不把自己的想法说出来。", public=False),
                "Scars" : Trait(__("Marks"), verb = "be", eff1 = Effect("change", "body", -5, scales_with = "rank"), eff2 = Effect("change", "charm", 10), base_description = "她表现得如此自信，以至于你几乎没有注意到她那令人讨厌的伤疤。", public=False),
                "Plain" : Trait(__("Odd"), verb = "be", eff1 = Effect("change", "beauty", -5, scales_with = "rank"), eff2 = Effect("change", "charm", 10), base_description = "她看起来像一个普通的女孩，但她独特的个性弥补了这一点。", public=False),
                "Rude" : Trait(__("Raw"), verb = "be", eff1 = Effect("change", "refinement", -5, scales_with = "rank"), base_description = "尽管她出身低微，但她还是尽力为别人着想。", public=False),
                "Rough" : Trait(__("Impolite"), verb = "be", eff1 = Effect("change", "sensitivity", -5, scales_with = "rank"), opposite = "Delicate", base_description = "她偶尔行为不检。", public=False),
                "Weak" : Trait(__("Tender"), verb = "be", eff1 = Effect("change", "constitution", -5, scales_with = "rank"), opposite = "Resilient", base_description = "她经过刻苦训练，不再像以前那样脆弱。", public=False),
                "Defiant" : Trait(__("Resistant"), verb = "be", eff1 = Effect("change", "obedience", -5, scales_with = "rank"), eff2=Effect("change", "valuation", -20), opposite = "Meek", base_description = "她喜欢时不时地反抗权威。", public=False),
                "Gluttonous" : Trait(__("Craving"), verb = "be", eff1 = Effect("change", "constitution", -15), base_description = "她总是饥肠辘辘，但也学会了不过量进食。", public=False),
                "Uncouth" : Trait(__("Primitive"), verb="be", eff1=Effect("change", "refinement", -20), opposite = "Groomed", base_description = "她缺乏基本的礼貌，但有良好的意图。", public=False),
                "Deaf" : Trait(__("Inattentive"), verb = "be", eff1 = Effect("change", "obedience", -10), eff2 = Effect("change", "waitress jp gains", -0.25), base_description = "她不是聋子，但她经常心不在焉。", public=False),
                "Timid" : Trait(__("Bashful"), verb = "be", eff1 = Effect("boost", "charm gains", -0.25), eff2 = Effect("change", "sensitivity", 10), opposite = "charming", base_description = "她害羞得可爱。", public=False),
                "Plump" : Trait(__("Full-figured"), verb = "be", eff1 = Effect("boost", "body gains", -0.25), eff2 = Effect("change", "constitution", 10), opposite = "Fit", base_description = "她有着优美的自然曲线。", public=False),
                "Scruffy" : Trait(__("Authentic"), verb = "be", eff1 = Effect("boost", "beauty gains", -0.25), eff2 = Effect("change", "beauty", 10), opposite = "Beautiful", base_description = "她更喜欢真诚地承认自己的不完美，而不是隐藏它们。", public=False),
                "Vulgar" : Trait(__("Honest"), verb = "be", eff1 = Effect("boost", "refinement gains", -0.25), eff2 = Effect("change", "libido", 10), opposite = "Elegant", base_description = "她总是直言不讳。", public=False),
                "Tame" : Trait(__("Restrained"), verb = "be", eff1 = Effect("boost", "libido gains", -0.25), eff2=Effect("change", "refinement", 10), opposite = "Slutty", base_description = "她很守规矩。", public=False),
                "Frail" : Trait(__("Cherished"), verb = "be", eff1 = Effect("boost", "constitution gains", -0.25), eff2=Effect("change", "sensitivity", 10), opposite = "Athletic", base_description = "她很脆弱，但值得被保护。", public=False),
                "Rebellious" : Trait(__("Liberated"), verb = "be", eff1 = Effect("boost", "obedience gains", -0.25), eff2 = Effect("change", "charm", 10), opposite = "Obedient", base_description = "她可以自由地做出自己的选择。", public=False),
                "Distrustful" : Trait(__("Independent"), verb = "be", eff1 = Effect("boost", "love gains", -0.25), eff2 = Effect("change", "refinement", 10), opposite = "Loyal", base_description = "她是一个独立可靠的女孩。", public=False),
                "Fearful" : Trait(__("Anxious"), verb = "be", eff1 = Effect("boost", "fear", 0.25), eff2 = Effect("change", "defense", 1), opposite = "Brave", base_description = "她很紧张，很容易担心。", public=False),
                "Paranoid" : Trait(__("Cautious"), verb = "be", eff1 = Effect("boost", "fear", 1.0), eff2 = Effect("change", "defense", 2), base_description = "她很警惕，小心翼翼地避免危险。", public=False),
                "Homely" : Trait(__("Comfortable"), verb = "be", eff1 = Effect("boost", "reputation gains", -0.1), eff2 = Effect("boost", "love", 0.25), opposite = "Sexy", base_description = "她感到很自在。", public=False),
                "Prude" : Trait(__("Behaved"), verb = "be", eff1 = Effect("boost", "service jp gains", -0.25), eff2 = Effect("boost", "sex jp gains", -0.25), eff3=Effect("change", "refinement", 10), opposite = "Naughty", base_description = "她不喜欢无意义的性爱，更喜欢先建立关系。", public=False),
                "Naive" : Trait(__("Green"), verb = "be",eff1 = Effect("boost", "anal jp gains", -0.25), eff2 = Effect("boost", "fetish jp gains", -0.25), eff3=Effect("change", "beauty", 10), opposite = "Kinky", base_description = "她不喜欢做奇怪的事... 暂时...", public=False),
                "Square" : Trait(__("Traditional"), verb = "be", eff1 = Effect("change", "sex act requirements", 20), eff2=Effect("change", "refinement", 10), opposite = "Pervert", base_description = "她喜欢照章办事。", public=False),
                "Strong gag reflex" : Trait(__("Throat spasms"), verb = "have", eff1 = Effect("increase satisfaction", "service", -1), eff2=Effect("change", "libido", 10), base_description = "她以前呛得更厉害，但现在还是时不时地吐在鸡鸡上。", public=False),
                "All thumbs" : Trait(__("Klutzy"), verb = "be", eff1 = Effect("increase satisfaction", "waitress", -1), eff2 = Effect("change", "libido", 10), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy'], base_description = "她还在努力让自己变得有用。", public=False),
                "Awkward" : Trait(__("Embarrassed"), verb = "be", eff1 = Effect("increase satisfaction", "dancer", -1), eff2 = Effect("change", "charm", 10), opposite=['Nimble', 'Agile', 'Brisk', 'Powerful'], base_description = "她在某些情况下感到不舒服。", public=False),
                "Brutal" : Trait(__("Fierce"), verb = "be", eff1 = Effect("increase satisfaction", "masseuse", -1), eff2 = Effect("change", "constitution", 10), opposite=['Deft', 'Soft skin', 'Agile', 'Unhurried'], base_description = "她喜欢公开展示自己的力量。", public=False),
                "Dumb" : Trait(__("Dopey"), verb = "be", effects = [Effect("increase satisfaction", "geisha", -1), Effect("change", "charm", 10)], opposite=['Nimble', 'Soft skin', 'Bright', 'Modest'], base_description = "她又蠢又有趣。", public=False),
                "Oafish" : Trait(__("Simple"), verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.25), eff2 = Effect("boost", "geisha jp gains", -0.25), eff3 = Effect("change", "libido", 10), opposite=['Nimble', 'Agile', 'Brisk', 'Soft skin', 'Bright'], base_description = "她不喜欢思考复杂的事情。", public=False),
                "Clumsy" : Trait(__("Silly"), verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.25), eff2 = Effect("boost", "masseuse jp gains", -0.25), eff3 = Effect("change", "sensitivity", 10), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy', 'Soft skin', 'Agile'], base_description = "人们喜欢取笑她的错误。", public=False),
                "Slow" : Trait(__("Relaxed"), verb = "be", eff1 = Effect("boost", "xp gains", -0.25), eff2 = Effect("change", "libido", 10), opposite = ["Fast learner", "Sharp", "Genius"], base_description = "她喜欢悠着点。", public=False),
                "Arrogant" : Trait(__("Self-assured"), verb = "be", eff1 = Effect("boost", "all jp gains", -0.25 ), eff2 = Effect("change", "body", 10), opposite = "Humble", base_description = "她可能对自己的能力有点过于自信了。", public=False),
                "Stubborn" : Trait(__("Determined"), verb = "be", eff1 = Effect("boost", "xp gains", -0.1 ), eff2 = Effect("boost", "all jp gains", -0.1 ), eff3 = Effect("change", "constitution", 10), base_description = "她觉得有动力追求自己的想法，即使这些想法值得怀疑。", public=False),
                "Lazy" : Trait(__("Peaceful"), verb = "be", eff1 = Effect("boost", "max energy", -0.1), eff2 = Effect("change", "refinement", 10), opposite = ["Energetic", "Driven"], base_description = "她宁静而无忧无虑。", public=False),
                "Blind" : Trait(__("Myopic"), verb = "be", eff1 = Effect("change", "defense", -2), eff2 = Effect("change", "sensitivity", 10), base_description = "她近视眼。", public=False),
                "Vulnerable" : Trait(__("Accessible"), verb = "be", eff1 = Effect("change", "defense", -2), eff2 = Effect("change", "sensitivity", 10), opposite = ["Strong", "Warrior"], base_description = "她认为，即使是最不稳定的人，她也有责任安慰他们。", public=False),
                "Expensive" : Trait(__("Valuable"), verb = "be", eff1 = Effect("boost", "upkeep", 1), eff2=Effect("change", "valuation", +50), opposite = "Humble", base_description = "她应该得到公主般的待遇。", public=False),
                "Greedy" : Trait(__("Philanthropic"), verb = "be", eff1 = Effect("boost", "upkeep", -0.8), base_description = "她希望过俭朴的生活，并尽她所能捐赠给那些需要帮助的人。", public=False),
                "Cold" : Trait(__("Cool"), verb = "be", eff1 = Effect("change", "refinement", -10, scales_with = "rank"), eff2 = Effect("boost", "tiredness", -0.1), base_description = "她知道如何保持镇定。", public=False),
                "Jaded" :  Trait(__("Veteran"), verb = "be a", eff1 = Effect("special", "skill catch up", 1), eff2 = Effect("change", "valuation", -10, scales_with = "rank"), opposite = "Sensitive", base_description = "她通过自己的经验和专业知识来指导其他人。", public=False),
                "Sickly" : Trait(__("Empathic"), verb = "be", eff1 = Effect("boost", "hurt", +2), eff2=Effect("change", "sensitivity", 20), opposite = "Tough", base_description = "疾病和苦难使她变得更加富有同情心。", public=False),
                "Unlucky" : Trait(__("Unrelenting"), verb = "be", eff1 = Effect("special", "unlucky", 1), eff2 = Effect("reroll", "job critical failure", 1), base_description = "她运气很差，但靠意志力坚持了下来。", opposite = "Lucky", public=False),
                "Slave brand" : Trait(__("Trophy"), verb="be a", effects = [Effect("boost", "prestige", 1.5), Effect("change", "valuation", -100)], archetype="The Bride", base_description = "她有一个纹身，上面写着“科斯莫工业的财产”。如果找到，请归还给合法的主人。", public=False),

                "Lesbian" : Trait(__("Queer"), verb = "be a", eff1=Effect("increase satisfaction", "all sex acts", -1), eff2=Effect("increase satisfaction", "bisexual", 3), archetype="The Courtesan", base_description = "她不会被男人激起性欲，但却为女人服务。", public=False),
                "City girl" : Trait(__("Cosmopolitan"), verb="be a", eff1=Effect("boost", "farm preference increase", -1.0), eff2=Effect("change", "valuation", +60), eff3 = Effect("change", "refinement", 20), archetype="The Escort", base_description = "她是个有教养的人，在城市里生活得很好，但不喜欢住在农村。", public=False),
                "Circumcised" : Trait(__("Priestess"), verb = "be a", effects = [Effect("change", "libido", -50), Effect("change", "sensitivity", -50), Effect("increase satisfaction", "all jobs", 1), Effect("change", "whore obedience target", 100), Effect("change", "valuation", +200)], base_description = "她将自己的一生奉献给阿里奥斯，教会授予她女祭司的称号。", public=False), 
                "Deceitful" : Trait(__("Sly"), verb = "be", eff1=Effect("boost", "income", -0.01), eff2=Effect("change", "valuation", +50), base_description = "她是一个善于操纵别人的女孩，确保自己想要什么就能得到什么.", public=False),
                "Inbred" : Trait(__("Pureblood"), verb = "be a", eff1 = Effect("boost", "love", 0.5), eff2 = Effect("boost", "all jp gains", -0.5), eff3=Effect("change", "valuation", +400), base_description = "她的父亲和母亲有密切的血缘关系，这使人们认为她可能来自王室血统。", public=False),
                "Depressed" : Trait(__("Cynical"), verb="be", eff1=Effect("change", "mood", -1), eff2=Effect("change", "constitution", 10), base_description = "她对生活抱有悲观态度，并通过公开表示蔑视来应对这种情况。", public=False),
                "Chaste" : Trait(__("Pure"), verb = "be", eff1 = Effect("increase satisfaction", "waitress", 1), eff2 = Effect("increase satisfaction", "geisha", 1), eff3=Effect("change", "valuation", +100), opposite = "Pervert", base_description = "她不赞成婚外性行为，但她在妓院工作。顾客们认为她很可爱。", public=False),
                "Disfigured" : Trait(__("Repaired"), verb = "be", eff1 = Effect("boost", "naked bonus", -0.1), eff2 = Effect("change", "beauty", -10), eff3=Effect("change", "valuation", -25), opposite = "Nice boobs", base_description = "她在一次严重的事故中毁容，但专家医生已经尽可能地掩盖了这一损伤。", public=False),
                "Drunkard" : Trait(__("Teetotaler"), verb="be a", eff1=Effect("change", "constitution", 15, scales_with = "rank"), eff2= Effect("boost", "reputation gains", -0.25), eff3=Effect("change", "valuation", +50), base_description = "她完全戒掉了醉人的饮料。", public=False),
                # "Kidnapped" : Trait(__("Bonded"), verb = "be", eff1=Effect("change", "obedience", 40), eff2 = Effect("boost", "love", 0.5), eff3=Effect("change", "maintenance", 1, scope="brothel"), base_description = "She was kidnapped, but cares deeply about you due to Stockholm Syndrome.", public=False),
                "Frigid" : Trait(__("Composed"), verb = "be", eff1 = Effect("change", "libido", -10), eff2 = Effect("increase satisfaction", "masseuse", 1), eff3=Effect("increase satisfaction", "dancer", 1), opposite = "Horny", base_description = "她总是泰然自若，让客人们放松下来。", public=False),
                "Asexual" : Trait(__("Celibate"), verb = "be", effects = [Effect("change", "libido", -50), Effect("increase satisfaction", "all sex acts", -1), Effect("increase satisfaction", "all jobs", 1)], opposite = "Pervert", base_description = "她对亲密关系几乎没有兴趣，但她明白，她必须通过某种方式赚取自己的生活费。", public=False),
                "Bloodslut" : Trait(__("Islander"), verb = "be a", effects=[Effect("gain", "all sexual preferences", 250), Effect("change", "valuation", -20), Effect("change", "brothel reputation", -10, scales_with = "rank", chance=0.01, scope="brothel"), Effect("change", "customers", -2, scope="brothel"), Effect("personality", "creep")], opposite = "Virgin", base_description = "尽管在血岛有一段不光彩的过去，但大多数顾客都喜欢上了她。", public=False),
                "Half-elf" : Trait(__("Fey Blood"), verb = "be a", effects=[Effect("boost", "tiredness", -0.1)], base_description = "她的血管里流淌着精灵的血液，但顾客们似乎并不介意。", public=False),
                "Monsterkin" : Trait(__("Beastly"), verb = "be a", effects=[Effect("special", "immune", 1), Effect("change", "security", -1, scope = "brothel")], base_description = "有些人认为她是由怪物所生。但别被吓到，一旦你了解她，她是一个令人钦佩的人。", public=False),
                "Vivified" : Trait(__("Awakened"), verb = "be", effects=[Effect("change", "constitution", -20), Effect("change", "valuation", +600)], base_description = "人们相信她是被魔术师变出来的非自然生物。来自克塞罗斯各地的收藏家都有兴趣获得和研究她。", public=False),

                        }

        neg_traits_fixable = []
        
        for trait in traitking_neg_traits:
            if trait.name in traitking_neg_evolved:
                neg_traits_fixable += [trait]
        
        neg_traits_fix = [t for o, t in traitking_neg_evolved.items()]
        
        for trait in traitking_gold_traits:
            register_trait(trait, type="gold")
        
        for trait in traitking_pos_traits:
            register_trait(trait, type="pos")

        for trait in traitking_neg_traits:
            register_trait(trait, type="neg")

        for trait in neg_traits_fix:
            register_trait(trait, type="neg")
            
        expensive_trait = trait_dict["Expensive"]
        clumsy_trait = trait_dict["Clumsy"]

        # Adding special traits to trait dict (but not to pos/neg traits)
        godless_trait = trait_dict["Godless"] = Trait(__("Godless"), verb = "be", eff1 = Effect("boost", "reputation gains", -0.2))

        housebroken_trait = trait_dict["Housebroken"] = Trait(__("Housebroken"), verb="be", effects = [Effect("change", "job obedience target", -10), Effect("change", "whore obedience target", -10), Effect("change", "refinement", -10, scales_with = "rank")], base_description = "她在妓院里与一名顾客失身。她只知道这些。")
        t_pet_trait = trait_dict["Teacher's pet"] = Trait(__("Teacher's pet"), verb="be a", effects = [Effect("change", "train obedience target", -20), Effect("boost", "love", 0.25), Effect("change", "mood", -0.25, scales_with="cust nb")], base_description = "她的第一次是和我。我对她来说很特别。")
        trauma_trait = trait_dict["Trauma"] = Trait(__("Trauma"), verb="have a", effects = [Effect("change", "obedience", 20), Effect("gain", "negative fixation", 2), Effect("boost", "fear", 0.5)], base_description = "他在违背她意愿的情况下失去了她的童贞，不得不带着创伤生活下去。")
        farmgirl_trait = trait_dict["Farmgirl"] = Trait(__("Farmgirl"), verb="be a", effects = [Effect("change", "fetish", 20), Effect("boost", "farm preference increase", 0.25), Effect("boost", "customer penalties", 0.1)], base_description = "她在农场里失去了贞操，就像一只肮脏的动物。")

        ## Important! It is necessary to copy the mod template to a variable upon initializing it if you would like mod variables to save together with the player's saved game (ie. most cases)
        traitking = traitking_template
       
        ## GIRL GENERATION TRAIT DISTRIBUTIONS
        ## Original girls will recieve +1 gold traits on top of this. Positive values must be at least gold values + 1
        
        traitking_t1_chance = 99 # 1% chance
        traitking_t1_gold = 2
        traitking_t1_positive = 3
        traitking_t1_regular = 0

        traitking_t2_chance = 95 # 4% chance
        traitking_t2_gold = 1
        traitking_t2_positive = 3
        traitking_t2_regular = 0
                           
        traitking_t3_chance = 85 # 10% chance
        traitking_t3_gold = 0
        traitking_t3_positive = 1
        traitking_t3_regular = 2
       
        traitking_t4_chance = 75 # 10% chance
        traitking_t4_gold = 0
        traitking_t4_positive = 3
        traitking_t4_regular = 0
       
        traitking_t5_chance = 55 # 20% chance
        traitking_t5_gold = 0
        traitking_t5_positive = 2
        traitking_t5_regular = 0
       
        traitking_t6_chance = 35 # 20% chance
        traitking_t6_gold = 0
        traitking_t6_positive = 3
        traitking_t6_regular = 1
       
        traitking_t7_gold = 0 # 35% chance    
        traitking_t7_positive = 2
        traitking_t7_regular = 1

        # schedule recurring trait king events
        calendar.set_alarm(calendar.time + 28, StoryEvent(label="traitking_morning", type="morning"))
        calendar.set_alarm(calendar.time + 7, StoryEvent(label="traitking_day", type="day"))
        calendar.set_alarm(calendar.time + 1, StoryEvent(label="traitking_night", type="night"))
        
        # schedule holidays
        renpy.call("traitking_holidays")        

    return
    

label traitking_init:

    return
    
