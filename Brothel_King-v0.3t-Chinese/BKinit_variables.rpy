####         INIT VARIABLES FOR B KING          ####################################################
##    Those are the init variables and lists      ##################################################
##    for B King                                  ##################################################
##                                                ##################################################

init -11:
    define persistent.screen_width = 1920
    define persistent.screen_height = 1080

    define persistent.new_game_plus = False
    define persistent.last_difficulty = "normal" # Either stores a stock difficulty name or a custom difficulty dictionary
    define persistent.seen_list = []

    define persistent.cheats = False # Tracks if cheats are on in general (but the main setting is within the 'game' object)
    define persistent.girl_packs = []
    define persistent.girl_mix = {"default" : []}
    define persistent.active_mix = "default"
    define persistent.game_mixes = ["default"]

    define persistent.achievements = {} # Stores achievement levels with the following format: {target : level}. Workaround because Objects cannot be saved as persistent.
    define selected_achievement = None
    define latest_achievements = []

    define persistent.debug_pic_counter_dict = defaultdict(int) # Dictionary containing (pictures : count) when debug_pic_counter is on
    define persistent.debug_pic_counter = False

    define persistent.seen_intro = False
    define persistent.seen_tax_intro = False
    define persistent.seen_ignore_intro = False

    define persistent.pic_ignore_list = [] # Lists all picture paths that have been set to 'ignore' by the player

    default persistent.NGPsettings = {}

    define _greedy_rollback = False # Experimental (solves loading problems where a save rolls back too far)

    # Init variables for the 'Game Settings' screen are located in the BK_content_menu.rpy file #


init -4 python:

## STORY GIRLS ##
    girl_directories += ["NPC/Kunoichi/narika", "NPC/Kunoichi/haruka"] # girl_directories is initiated in BKsettings. Declare story girl paths here


init -3 python:


#### SYSTEM ####

    version_number = 0.2

    VIDEOFORMATS = (".webm", ".mkv", ".avi", ".mpg", ".mpeg") # Took out ".mp4" because of missing codecs
    IMGFORMATS = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp") # animated gifs and .webp do not work in Ren'py for now

    config.layers.append("myoverlay")

    ## Change native ren'py keymap behavior ##

    try:
        config.keymap['game_menu'].remove('mouseup_3')
    except:
        pass
    # config.keymap['game_menu'].append('o')

    try:
        config.keymap['screenshot'].remove('noshift_K_s')
    except:
        pass
    config.keymap['screenshot'].append('shift_K_s')

    try:
        config.keymap['toggle_fullscreen'].remove('f')
    except:
        pass
    config.keymap['toggle_fullscreen'].append('shift_F')

    try:
        config.keymap['toggle_music'].remove('m')
    except:
        pass
    config.keymap['toggle_music'].append('shift_M') # This doesn't work for reasons unclear

    try:
        config.keymap['hide_windows'].remove('h')
    except:
        pass
    config.keymap['hide_windows'].append('shift_H')

    try:
        config.keymap['self_voicing'].remove('v')
    except:
        pass

    config.keymap['self_voicing'].append('shift_V')

    # config.keymap['inspector'].remove('i')
    # config.keymap['inspector'].append('shift_I')

    config.keymap['viewport_up'] += ('K_PAGEUP', 'repeat_K_PAGEUP')
    config.keymap['viewport_down'] += ('K_PAGEDOWN', 'repeat_K_PAGEDOWN')

    gallery_type = "ev"

    untagged_pics = []
    rating_dict = defaultdict(dict)

    test_event_name = ""

    choice_menu_girl_interact = False
    last_interact_menu = "chat"
    last_free_interact_menu = "chat"

    selected_view_mode = "Auto"

    read_ini_log = ""

#### RESOLUTION ####

    # This is used as the base for the resolution calculations (native BK resolution)
    RES_BASE_X = 1024
    RES_BASE_Y = 768
    res_xy_ratio = 1.0 # WIP - Not working as intended - Default (1.0) is 4:3. Set this aspect ratio to 1.2 for 16:10, 1.334 for 16:9.

    new_res_ratio = config.screen_height/RES_BASE_Y # Used to scale factored images and tooltips

    res_dict = {}

    res_event_width = xres(800) # Base 800
    res_event_height = yres(600) # Base 600

    res_portrait_size = int(config.screen_height*0.2)

#### GOALS ####

    goal_channels = ("story", "story2", "story3", "advance", "advance2", "papa", "contract", "other")
    goal_channels_no_story = ("advance", "advance2", "contract", "other")
    goal_categories = {"story" : "STORY", "story2" : "STORY", "story3" : "STORY", "advance" : "ADVANCE", "advance2" : "ADVANCE", "contract" : "CONTRACT", "other" : "MISC", "papa" : "MISC"}
    goal_tb = {"story" : "tb story", "story2" : "tb story", "story3" : "tb story", "advance" : "tb advance", "advance2" : "tb advance", "contract" : "tb contract", "other" : "tb other", "papa" : "tb papa"}
    goal_colors = {"STORY" : c_softpurple, "ADVANCE" : c_magenta, "CONTRACT" : c_firered, "MISC" : c_yellow}

#### TAG LIST ####

    #<Chris12>
    for tag in tag_dict:
        if tag != tag.lower(): raise Exception("Illegal Tag " + tag + " in tag_dict! Only lowercase allowed.")
        if len(tag) <= 1: raise Exception("Illegal Tag " + tag + " in tag_dict! Tags must be at least 2 characters long.")
    tag_list_dict = {tag : make_list(tag_dict[tag]) for tag in tag_dict}
    sorted_tag_dict_keys = sorted(tag_dict.keys(), key = lambda x : len(x), reverse=True)
    sorted_tags_with_separator = [tag for tag in sorted_tag_dict_keys if " " in tag]
    ending_pattern = re.compile(r"(\(\d*\))?(\.\w{3,4})+$") # can match (and remove) the last part of a filename '(00001).webp'.
    #</Chris12>

#### BADGES ####

    badge_pics = [f for f in renpy.list_files() if f.startswith("UI/badges/") and is_imgfile(f)]

#### DIFFICULTY ####

    diff_list = ["very easy", "easy", "normal", "hard", "insane"] # A list is needed to show the values in order

    diff_name = {"very easy" : "Gigolo", "easy" : "Hustler", "normal" : "Whorelord", "hard" : "Brothel Prince", "insane" : "Brothel King{#1}"}

    diff_description = {"very easy" : "No challenge at all. You're either here for the story, or the pretty pictures. {i}All achievements are locked.{/i}", "easy" : "A basic challenge for new players.", "normal" : "The classic experience.", "hard" : "Want more challenge? Hard has got you covered.", "insane" : "The ultimate challenge."}

    diff_settings = ["stats", "xp", "jp", "pref", "rep", "gold", "budget", "rewards", "resources", "prestige", "tax rate", "satisfaction", "security"] # A list is needed to show the values in order

    diff_setting_name = {
                        "gold" : "Income",
                        "budget" : "Customer budget",
                        "rewards" : "Rewards",
                        "resources" : "Resources",
                        "stats" : "Girl skills",
                        "pref" : "Preferences",
                        "xp" : "XP",
                        "jp" : "JP",
                        "rep" : "Girl reputation",
                        "prestige" : "Prestige",
                        "tax rate" : "Guild Fee Offset",
                        "satisfaction" : "Customer satisfaction",
                        "security" : "Security grace period",
                        }

    diff_setting_description = {
                        "gold" : "Affects your {b}Brothel Income{/b}.",
                        "budget" : "Changes cap on customers' individual {b}budget{/b}.",
                        "rewards" : "Affects {b}Rewards{/b} from quests, classes and monthly contracts.",
                        "resources" : "Affects the amount of {b}Resources{/b} you get from collecting and trading.",
                        "stats" : "Affects the progression of your girls' {b}Skills{/b}.",
                        "pref" : "Affects the progression of your girls' {b}Sexual Preferences{/b}.",
                        "xp" : "Affects the progression of your girls' {b}XP{/b}.",
                        "jp" : "Affects the progression of your girls' {b}JP{/b}.",
                        "rep" : "Affects the progression of your girls' {b}REP{/b}.",
                        "prestige" : "Affects the progression of your Main Character's {b}Prestige{/b}.",
                        "tax rate" : "Increases or decreases the Slave Guild's {b}fee{/b}.",
                        "satisfaction" : "Changes customer {b}satisfaction{/b} bonus.",
                        "security" : "Delays threat buildup by this number of days after each event.",
                        }

    diff_settings_range = {
                        "gold" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                        "budget" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                        "rewards" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                        "resources" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                        "stats" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                        "pref" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                        "xp" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                        "jp" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                        "rep" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                        "prestige" : {"min" : 0.1, "max" : 5.0,  "pace" : 0.05},
                        "tax rate" : {"min" : -0.3, "max" :  0.3, "pace" :  0.05},
                        "satisfaction" : {"min" : -3, "max" : 3, "pace" : 1},
                        "security" : {"min" : 0, "max" : 5, "pace" : 1},
                        }

    diff_dict = {
                "very easy" : {"gold" : 1.5,
                            "budget" : 1.25,
                            "rewards" : 1.5,
                            "resources" : 1.5,
                            "stats" : 1.5,
                            "pref" : 1.5,
                            "xp" : 1.5,
                            "jp" : 1.5,
                            "rep" : 1.5,
                            "prestige" : 1.5,
                            "tax rate" : -0.2,
                            "satisfaction" : 2,
                            "security" : 5,
                        },

                "easy" :  {"gold" : 1.25,
                            "budget" : 1.1,
                            "rewards" : 1.25,
                            "resources" : 1.5,
                            "stats" : 1.25,
                            "pref" : 1.25,
                            "xp" : 1.25,
                            "jp" : 1.25,
                            "rep" : 1.25,
                            "prestige" : 1.25,
                            "tax rate" : -0.1,
                            "satisfaction" : 1,
                            "security" : 3,
                        },
                "normal" : {"gold" : 1.0,
                            "budget" : 1.0,
                            "rewards" : 1.0,
                            "resources" : 1.0,
                            "stats" : 1.0,
                            "pref" : 1.0,
                            "xp" : 1.0,
                            "jp" : 1.0,
                            "rep" : 1.0,
                            "prestige" : 1.0,
                            "tax rate" : 0.0,
                            "satisfaction" : 0,
                            "security" : 1,
                        },

                "hard" :  {"gold" : 0.8, #? Changed as per Chris12's suggestion (experimental)
                            "budget" : 0.9,
                            "rewards" : 0.85,
                            "resources" : 0.85,
                            "stats" : 0.75,
                            "pref" : 0.75,
                            "xp" : 0.75,
                            "jp" : 0.75,
                            "rep" : 1.0,
                            "prestige" : 1.0,
                            "tax rate" : 0.1,
                            "satisfaction" : -1,
                            "security" : 0,
                        },
                "insane" : {"gold" : 0.6, #? Changed as per Chris12's suggestion (experimental)
                            "budget" : 0.75,
                            "rewards" : 0.6,
                            "resources" : 0.6,
                            "stats" : 0.5,
                            "pref" : 0.5,
                            "xp" : 0.5,
                            "jp" : 0.5,
                            "rep" : 0.75,
                            "prestige" : 0.75,
                            "tax rate" : 0.2,
                            "satisfaction" : -2,
                            "security" : 0,
                        },
    }

#### CHEATS ####

    always_show_personality = defaultdict(bool)


#### STARTING GAME VARIABLES AND OBJECTS ####

    ## INIT VARIABLES ##

#    global selected_girl
    selected_girl = None
    selected_sex_act = None
#    global selected_quest
    selected_item = None
    selected_quest = None
    selected_district = None
    selected_location = None
    selected_destination = None
    show_spellbook = False
    pers_showing = "personality"
#    vp_value = 0
    vp_adj = ui.adjustment()
    sched_adj = ui.adjustment()

    adjust_vp = True
    shake_count = 0
    always_show_brothel_report = False

    last_contract_result = None

#### RANDOM TIPS ####

    random_tips = [
                    "Zan is an exciting place... Make sure to explore the city regularly!",
                    "Did you know the brothel has many shortcuts? You need to find the right key...",
                    "Beautiful girls make the best masseuses.",
                    "Masseuses should be {b}beautiful{/b} and {b}sensitive{/b}. A good {b}body{/b} and {b}refinement{/b} are also important.",
                    "A girl with a good Body makes a great dancer.",
                    "Dancers should have a good {b}body{/b} and high {b}libido{/b}. {b}Refinement{/b} and {b}charm{/b} also help.",
                    "Charming girls will do better as waitresses.",
                    "Waitresses need {b}charm{/b} and {b}constitution{/b}. It cannot hurt if they are {b}beautiful{/b}, and have a good {b}body{/b} as well.",
                    "Geishas should be refined girls to achieve the best results.",
                    "Geishas should be {b}refined{/b} and {b}obedient{/b}. {b}Beauty{/b} and {b}charm{/b} also help make a perfect geisha.",
                    "Higher-class customers are harder to satisfy, but they tip better.",
                    "Don't forget to pay for the brothel's security. Things can escalate quickly.",
                    "Your brothel gets dirty every time girls interact with customers. Your maintenance team should keep up, otherwise you'll end up spending a lot more to repair the damage later.",
                    "Advertising girls are good if you want to bring more customers to the brothel. Don't bring more than you can handle, however: unsatisfied customers will lower your reputation.",
                    "Disobedient girls are less likely to accept working or training.",
                    "Girls with high Libido are more likely to agree to and enjoy sex, and can serve multiple customers too.",
                    "Sensitive girls are good at making customers happy, regardless of the act.",
                    "Constitution determines how much energy a girl has, and how many customers she can serve.",
                    "Charm and Sensitivity make your girls better at handjobs, blowjobs and other service sex acts.",
                    "A good {b}service{/b} skill is required to perform Service, of course, as well as {b}sensitivity{/b}. {b}Charm{/b} and the {b}fetish{/b} skill also help.",
                    "Beauty and Libido are important for regular Sex acts.",
                    "For regular Sex, high {b}sex{/b} and {b}libido{/b} skills give the best results. {b}Beauty{/b} and {b}service{/b} also boost sex.",
                    "Girls with a good Body and Constitution can handle Anal sex well.",
                    "Anal sex requires a high {b}anal{/b} skill and a good {b}constitution{/b}. {b}Body{/b} and {b}sex{/b} skills also help.",
                    "Refinement and Obedience are good for Fetish sex acts.",
                    "A girl needs a good {b}fetish{/b} and {b}obedience{/b} skills for Fetish sex acts. {b}Refinement{/b} and {b}anal{/b} skills also factor.",
                    "The brothel report has lots of useful information about the brothel. If you want information about a given girl, check out her statistics in the girl tab.",
                    "When working, girls receive both XP and JP. XP allow a girl to level up their stats and earn perks, JP allow a girl to get better at a given job or sex act. Both max out depending on her rank.",
                    "Customers' tastes are different in the kind of entertainment and sex acts they like. Variety is key to keep all customers satisfied.",
                    "Every satisfied customer increases your reputation. But unhappy customers will diss your brothel and your girls, so watch out.",
                    "Overall, customer satisfaction stems from two factors: the quality of entertainment they receive, and the quality of your whores.",
                    "Girls may become Bisexual, allowing two of them to service the same customer.",
                    "Girls may learn how to have Group sex, allowing them to serve two or three customers at the same time.",
                    "Bisexual and Group sex are always satisfying for the customers.",
                    "Upkeep is important to keep your girls in the mood. Although happy girls may work for you for little upkeep, their mood will drop dramatically if their upkeep gets too low.",
                    "Although your security will take care of most problems, your girls will need some personal defense if a crazy customer targets them directly. Beware, though, any weapon you give them could be used against you...",
                    "The most effective way to train your girls for sex acts is to do it yourself, but it's time-consuming. Maybe you can find someone who will train them for you?",
                    "Some of the people you meet can become trainers for your girls. Make sure to pick the one with the best ability for your management style.",
                    "In Zan, a reputation for good or evil can make a lot of difference. Every good or bad deed has consequences. Of course, not everything is black and white. Some people like to walk the line between both...",
                    "I hear there are girls with very loose morals hanging out in the various districts of the city. You wouldn't happen to know anything about that, would you?",
                    "The girl from the shop is always acting flirtatious and bitchy,... I don't like her. I wish we could find other places to shop in town.",
                    "You can buy girls that have already been trained at the slave market. This can save you some time, although you can never be 100% sure about the quality of the training they received.",
                    "By talking with your girls, you can get to know them, and they might even tell you their personal stories.",
                    "Girls will love you if you act kindly towards them and let them do what they like.",
                    "Girls will fear you if you act harshly towards them or force them to do things they don't want.",
                    "When all else fails, you can lecture your girls in order to start their training. Being Charismatic helps.",
                    "Your Strength determines how good you are in a fight, or at pulling off various physical feats.",
                    "Your Spirit determines how good you are with using, detecting and resisting magic.",
                    "Charisma is important for all kinds of interactions, both with your girls and in the outside world.",
                    "Your Speed determines how many actions you can take every day. It is rarely used for anything else.",
                    "Unhappy girls may run away from you. If you cannot afford to hire bounty hunters, your last chance to get them back will be to explore the city on your own.",
                    "Don't forget to upgrade the brothel bedrooms. Girls and customers alike will see their mood deteriorate if the bedrooms are below par, especially at higher ranks.",
                    "Common rooms can host a limited number of customers. Make sure you have enough room to entertain everyone.",
                    "When a girl joins your brothel, you must have a room ready for her. Otherwise, you might have to wait until you expand to receive her.",
                    "Some people sell curious things around in the city, even monsters or animals. I'm not sure what you'd need them for.",
                    "Sex skills cannot be improved by levelling. One needs first-hand experience to learn them.",
                    "Classes are useful to improve a girl's inferior skills more quickly.",
                    "Every girl has her own reputation, separate from your brothel's. Reputation is key for a girl to reach higher ranks.",
                    "The best way to improve a girl's reputation is for her to succeed in Quests.",
                    "Sex slaves receive ranks from the Slavers guild. Ranks determines many things, including max level and max skills.",
                    "At the lowest rank, a girl's Skills are limited to 50. Every additional Rank improves the Skill maximum by 50 more.",
                    "When a girl levels up, she receives Skill points, depending on her current Rank. Also, she receives a perk point every level.",
                    "Every five levels, a girl will receive an extra perk point.",
                    "No matter what, a girl cannot go above level 25.",
                    "I've heard a rumor about a secret Rank at the Slaver guild, higher even than Rank 'S'.",
                    "Please, Master, never ever let your money fall under zero denars! I've heard some people will try to tempt you with shady deals if you're in debt, but they just mean even more trouble.",
                    "Never trust an Elf. Don't come here saying I didn't warn you.",
                    "At higher ranks, integrating new girls can be tough. Make sure to use Classes, Items, Perks and other bonuses to help the new girl get ahead.",
                    "When you feel like you've seen it all, you can disable some night events in the Game Settings menu.",
                    "Don't like the random name generation? You can disable it in the Game Settings menu.",
                    "Not into some of the more hardcore acts? Disable them in the Game Settings menu.",
                    "Hit 'Ctrl' to skip night events, or any dialog you've already seen.",
                    "A right click will take you back one step. Right-clicking on the main menu will bring out the Options menu.",
                    "During the day, come back to the Home screen at any time with the 'H' key.",
                    "Press 'E' to end the day and move on the the night's events.",
                    "Spells can be auto-cast, using any leftover mana points you have left at the end of the day.",
                    "Pressing the 'Esc' key will bring out the game menu",
                    "You can come back to the latest visited location simply by using the 'L' key.",
                    "Prestige is earned whenever you or your girls have sex. Earning prestige will allow you to level up.",
                    "Your skills cannot naturally go over 10, but Items and Magic can help.",
                    "Virgin girls receive a new trait after they are deflowered, depending on the conditions under which it happened.",
                    "If your girls are in a bad mood, make sure you pay them enough, and that their accommodations are comfortable enough.",
                    "Advertising increases the maximum amount of money per customer. Make sure they bring a fat purse!",
                    "Classes may cause a girl's skills to exceed their level cap. Handy if you have the cash for them.",
                    "After a while, higher skills become harder to increase for experienced girls. Classes can help you get around that.",
                    "Although jobs and sex acts rely on a couple of major skills, having other high skills can often give a little boost to a girl's results.",
                    "Even though recognizing a naked girl should be easy, people can never agree on what 'nudity' is, exactly! Can you believe it?",
                    "Public acts are confusing. Is it public because it's outside, or because other people can see you? I can never tell.",
                    "You can quick-save with F5 and quick-load with F9 (when shortcuts are active). What does it mean? I have no idea!",
                    "Be careful not to let your girls fall sick or hurt! Hurt girls will recover energy half as fast as other girls.",
                    "Are notifications flying by too fast for you? You can review the latest notifications by clicking on the '?' button.",
                    "Game settings give you various options to tweak the game's content and UI to your liking.",
                    "Brokipedia in the '?' menu will help you grasp some finer details about the game. It doesn't hold everything yet, but will be improved over time.",
                    "Mind the special effects from this month's moon. They may give extra rewards for some specific activities you wouldn't normally do.",
                    "If you put fear in your girls' heart, Evil powers may become accessible from the Farm. I shiver to think about what you could do with these.",
                    "Evil brothel owners use up slave girls until their sanity is gone, then throw them out on the street. You wouldn't do that, would you?",
                    "I heard that if you summon a magical pet 15 times, something special happens... How cute.",
                    "Tired of the story? Reach the end of the game at least once to unlock 'No story' mode.",
                    "I've heard of something called 'NewGame+' if you reach the end of the game. Whatever could that mean?",
                ]


    ## MC ##

    all_MC_stats = ["strength", "spirit", "charisma", "speed"]

    MC_playerclass_description = {
                                "Warrior" : "You are a Warrior. You might be young, but you have seen more than your share of bloody battles. You are stronger in fights and for protecting the brothel.",
                                "Wizard" : "You are a Wizard. People bend to your will, and your magic. You have access to the most spells.",
                                "Trader" : "You are a Rogue Trader. You've been hustling since you were a young street rat. You can make better deals and fetch the best prices."
                            }

    MC_stat_description = {
                            "strength" : "This is the current strength of your character. Improves security and helps in individual fights.",
                            "spirit" : "This is your magic fortitude. Spirit is the source of your mana, and improves spell results during events.",
                            "charisma" : "This covers your character personality, looks and oratory skills. Improves results during interactions.",
                            "speed" : "This is your character's level of energy. Increases the number of actions you can perform."
                        }

    god_description = {
                        "Arios" : "You worship Arios, god of Light and lord of the Angels. +1 to Strength.",
                        "Shalia" : "You worship Shalia, goddess of Shadows and ruler of the Night. +1 to Spirit.",
                        None : "You do not worship any god, and delight instead in the wonders of the natural world. +1 to Charisma."
                        }

    alignment_description = {
                            "good" : "Your actions have shown you to be a {b}good{/b} person. Love-based interactions with your girls are more successful than fear-based ones.",
                            "evil" : "You are an {b}evil{/b} man, and revel in your own cruelty. Fear-based interactions with your girls are more successful than love-based ones.",
                            "neutral" : "You are {b}neutral{/b}, and would rather maintain balance between your own interests and those of others. Love and fear-based interactions are equally successful."
                            }



    ## INVENTORY ##

    MC_inventory_slots = ["hands", "accessory", "misc"]
    girl_inventory_slots = ["hands", "body", "neck", "finger", "accessory"]
    inventory_filters = {
                        "base" : [None, "weapon", "clothing", "trinket", "consumable", "misc"],
                        "minion_merchant" : [None, "misc"],
                        "Accessory" : [None, "trinket"],
                        "Flower" : [None, "misc"],
                        "Weapon" : [None, "weapon"],
                        "Toy" : [None, "consumable"],
                        "Ring" : [None, "trinket"],
                        "Gift" : [None, "misc"],
                        "Dress" : [None, "clothing"],
                        }

    filter_list = {
                    None : [],
                    "weapon" : ["hands"],
                    "clothing" : ["body", "accessory"],
                    "trinket" : ["finger", "neck"],
                    "consumable" : ["consumable"],
                    "misc" : ["misc"],
                }

    sorter_dict = { # [Caption, attribute, tooltip, reverse order]
                    "alpha" : ["A-z", "name", "name", False],
                    "badge" : ["Bdg", "badge", "badge", True],
                    "price" : ["0-9", "price", "price", False],
                    "type" : ["Typ", "filter", "item type", False],
                    "level" : ["Lvl", "level", "girl level", True],
                    "rank" : ["Rk", "rank", "slave rank", True],
                    "job" : ["Job", "job_sort_value", "girl job", False],
                    "beauty" : ["Bea.", "beauty", "Beauty", True],
                    "body" : ["Bod.", "body", "Body", True],
                    "charm" : ["Cha.", "charm", "Charm", True],
                    "refinement" : ["Ref.", "refinement", "Refinement", True],
                    "libido" : ["Lib.", "libido", "Libido", True],
                    "obedience" : ["Obe.", "obedience", "Obedience", True],
                    "sensitivity" : ["Sen.", "sensitivity", "Sensitivity", True],
                    "constitution" : ["Con.", "constitution", "Constitution", True],
                    "service" : ["Serv.", "service", "Service skill", True],
                    "sex" : ["Sex", "sex", "Sex skill", True],
                    "anal" : ["Anal", "anal", "Anal skill", True],
                    "fetish" : ["Fet.", "fetish", "Fetish skill", True],
                    "energy" : ["En.", "energy", "energy", False],
                    "experience" : ["Tr.", "training_value", "sexual training level", True],
                }

    ## RESOURCES ##

    build_resources = ["wood", "leather", "dye", "marble", "ore", "silk", "diamond"]

    # Exchange rates are stored as fractions for display in the resource market tab

    resource_gold_value = {2 : Fraction(200, 1), 3 : Fraction(1000, 1), 4 : Fraction(4000, 1)} # This is the buy value. Sell value is 25% of buy value
    resource_sell_discount = 0.1 # Adjust this as necessary

    resource_base_exchange_rate = {
                                    2 : {2 : Fraction(1, 3), 3 : Fraction(1, 9), 4 : Fraction(1, 81)},
                                    3 : {2 : Fraction(1, 1), 3 : Fraction(1, 3), 4 : Fraction(1, 27)},
                                    4 : {2 : Fraction(12, 1), 3 : Fraction(4, 1), 4 : Fraction(1, 1)},
                                    }



    ## ALERTS ##

    seen_alerts = defaultdict(bool)


    ## LICENCES ##

    license_dict = {
                    0 : ("No license", "missing license.webp"),
                    1 : ("Pimp license", "license1.webp"),
                    2 : ("Whoremonger license", "license2.webp"),
                    3 : ("Brothelmaster license", "license3.webp")
                }



    ## BROTHEL PICS AND ROOMS ##

init python:

    brothel_images = {
                        1 : renpy.image("brothel1", im.Scale("brothels/" + brothel_pics[1], config.screen_width, config.screen_height)),
                        2 : renpy.image("brothel2", im.Scale("brothels/" + brothel_pics[2], config.screen_width, config.screen_height)),
                        3 : renpy.image("brothel3", im.Scale("brothels/" + brothel_pics[3], config.screen_width, config.screen_height)),
                        4 : renpy.image("brothel4", im.Scale("brothels/" + brothel_pics[4], config.screen_width, config.screen_height)),
                        5 : renpy.image("brothel5", im.Scale("brothels/" + brothel_pics[5], config.screen_width, config.screen_height)),
                        6 : renpy.image("brothel6", im.Scale("brothels/" + brothel_pics[6], config.screen_width, config.screen_height)),
                        7 : renpy.image("brothel7", im.Scale("brothels/" + brothel_pics[7], config.screen_width, config.screen_height)),
                    }

    # ROOMS #

    room_dict = {
                1 : Room("Basic room", 1),
                2 : Room("+Basic room+", 2),
                3 : Room("*Basic room*", 3),
                4 : Room("Standard room", 4),
                5 : Room("+Standard room+", 5),
                6 : Room("*Standard room*", 6),
                7 : Room("Elegant room", 7),
                8 : Room("+Elegant room+", 8),
                9 : Room("*Elegant room*", 9),
                10 : Room("Noble suite", 10),
                11 : Room("+Royal suite+", 11),
                12 : Room("*Imperial suite*", 12)
                }

    common_room_dict = {
                        "tavern" : Room("tavern", 0, "special", job = "waitress"),
                        "strip club" : Room("strip club", 0, "special", job = "dancer"),
                        "onsen" : Room("onsen", 0, "special", job = "masseuse"),
                        "okiya" : Room("okiya", 0, "special", job = "geisha"),
                        }

    for room in common_room_dict:
        for dirt_state in ("clean enough", "dusty", "dirty", "disgusting", "fire"):
            path = "brothels/rooms/" + room + {"clean enough" : "", "dusty" : "_dusty", "dirty" : "_dirty", "disgusting" : "_verydirty", "fire" : "_verydirty"}[dirt_state] + ".webp"
            renpy.image(room + " " + dirt_state, ProportionalScale(path, config.screen_width, config.screen_height))

    master_bedrooms = {
                        0 : Room("Single room", level=0, type="master", cost=0),
                        1 : Room("Double room", level=1, type="master", cost=750),
                        2 : Room("Small suite", level=2, type="master", cost=2500),
                        3 : Room("Luxury suite", level=3, type="master", cost=7500),
                        4 : Room("Royal suite", level=4, type="master", cost=25000),
                        5 : Room("Royal harem", level=5, type="master", cost=75000),
                        }


#    all_common_rooms = [tavern, club, onsen, okiya]
    all_common_rooms = ["tavern", "strip club", "onsen", "okiya"]
    job_room_dict = {"waitress" : "tavern",
                    "dancer" : "strip club",
                    "masseuse" : "onsen",
                    "geisha" : "okiya",
                    "whore" : "bedroom"
                    }

    room_capacity_dict = {0 : 4, 1 : 4, 2 : 6, 3 : 8, 4 : 10, 5 : 12, 6 : 14, 7 : 16}

init -4 python:

    ## CITY BUTTONS

    location_tb = {
                    "visit_willow" : "tb willow",
                    "visit_goldie" : "tb goldie",
                    "visit_watchtower" : "tb captain",
                    "visit_gina" : "tb gina",
                    "visit_thieves_guild" : "tb renza",
                    "visit_stella" : "tb stella",
                    "visit_giftgirl" : "tb giftgirl",
                    "visit_ramias" : "tb ramias",
                    "visit_gurigura" : "tb gurigura",
                    "visit_riche" : "tb riche",
                    "visit_katryn" : "tb katryn",
                    "visit_twins" : "tb twins",
                    "visit_bank" : "tb banker",
                    "visit_exchange" : "tb bast",
                    "visit_papa" : "tb papa",

                    "collect_wood" : "tb wood",
                    "collect_leather" : "tb leather",
                    "collect_dye" : "tb dye",
                    "collect_ore" : "tb ore",
                    "collect_marble" : "tb marble",
                    "collect_silk" : "tb silk",
                    "collect_diamond" : "tb diamond",

                    "c3_contact_homura" : "side homura",
                }

    suzume_hints_active = False
    papa_location = {"The Docks" : "Seafront", "The Warehouse" : "Gallows"}

    ## FARM

    installation_price = {
                        0: 100,
                        1: 250,
                        2: 500,
                        3: 1000,
                        4: 1750
                    }

    minion_xp_to_level = {
                        0: 0,
                        1: 10,
                        2: 25,
                        3: 50,
                        4: 100,
                        5: 250
                    }

    minion_price = {
                    0: 100,
                    1: 200,
                    2: 300,
                    3: 400,
                    4: 500,
                    5: 750
                }

    minion_description = {"stallion" : "Stallions are male sex slaves from the Blood Islands, magically brainwashed and bred selectively for their abnormally large dicks....",
                        "beast" : "Beasts are all sorts of animals that Gizel keeps around at the farm. More like a zoo, really.",
                        "monster" : "Monsters are unnatural fiends crawling inside the darkest caves of Xeros. They come in many forms, but the ones with tentacles are the most sought after.",
                        "machine" : "Machines or artefacts have many uses, but in Gizel's workshop, they really only seem to be designed for one thing: sex."
                        }

    all_minion_types = ["stallion", "beast", "monster", "machine"]

    farm_pics = {
                "stallion" : [],
                "beast" : [],
                "monster" : [],
                "machine" : [],
                }

    farm_holding_dict = {
                        "libido" : "Tending to minions (Lib)",
                        "sensitivity" : "Tending to Gizel (Sen)",
                        "obedience" : "Cleaning up the farm (Ob)",
                        "constitution" : "Working outside (Con)",
                        "rest": "Resting",
                        }

    farm_ttip =         {
                        "libido" : "She will tend to the farm creatures (boosts libido, costs energy).",
                        "sensitivity" : "She will tend to Gizel personally (boosts sensitivity, costs energy).",
                        "obedience" : "She will clean up the farm (boosts obedience, costs energy).",
                        "constitution" : "She will work-out in the backyard (boosts constitution, costs energy).",
                        "rest": "She will be resting in her cell.",
                        "gentle": "In {b}gentle{/b} mode, she won't be forced to do something she doesn't want to. This training will not generate fear.",
                        "tough": "In {b}tough{/b} mode, Gizel will overcome moderate resistance on her part. This training will generate fear.",
                        "hardcore": "In {b}hardcore{/b} mode, Gizel will ignore all red lines and force her to do anything. This training will generate massive fear.",
                        }

    farm_description = {"stallion intro" : "%s spent the night in the stables with a well-hung stallion.",
                        "beast intro" : "%s spent the night in the pig stalls with a horny, filthy animal.",
                        "monster intro" : "%s spent the night in the monster den with a lewd, disgusting creature.",
                        "machine intro" : "%s spent the night in the workshop attached to a large and strange machine.",
                        "stallion intro plural" : "%s spent the night in the stables with %s well-hung stallions.",
                        "beast intro plural" : "%s spent the night in the pig stalls with %s drooling, horny beasts.",
                        "monster intro plural" : "%s spent the night in the monster den, harassed by %s lewd and disgusting creatures.",
                        "machine intro plural" : "%s spent the night in the workshop strapped to an array of %s arcane machines.",
                        "naked intro" : "Gizel paraded %s naked in front of %s.",
                        "service intro" : "Gizel pushed %s to her knees and made her service %s.",
                        "sex intro" : "Gizel told %s to fuck %s.",
                        "anal intro" : "Gizel told %s to let %s fuck her ass.",
                        "fetish intro" : "Gizel showed %s the chains on the wall and told her she'd watch %s have its way with her.",
                        "bisexual intro" : "Gizel decided to join %s for a little fun with a %s.",
                        "group intro" : "Gizel told %s to get ready to have sex with a group of %ss.",

                        "stallion good" : " %s couldn't take her eyes off the stallion's rock-hard cock. {color=[c_green]}Her training went well.{/color}",
                        "stallion average" : " %s was impressed and a little worried upon seeing the size of the stallion's hard cock. {color=[c_white]}Her training went normally.{/color}",
                        "stallion bad" : " The stallion's large dick scared %s and she recoiled fearfully. {color=[c_red]}Her training went poorly.{/color}",
                        "beast good" : " %s was curious and aroused by the weird shape and smell of the beast's genitals. {color=[c_green]}Her training went well.{/color}",
                        "beast average" : " %s felt uncomfortable around the animals and their weird bodies. {color=[c_white]}Her training went normally.{/color}",
                        "beast bad" : " %s couldn't believe she was being treated like a farm animal and stood as far as she could from the beasts. {color=[c_red]}Her training went poorly.{/color}",
                        "monster good" : " %s felt incredibly aroused by the pheromones emanating from the monster. {color=[c_green]}Her training went well.{/color}",
                        "monster average" : " %s felt weakened and confused by the monster's strange musk. {color=[c_white]}Her training went normally.{/color}",
                        "monster bad" : " %s felt disgusted and nauseated because of the monster's icky smell. {color=[c_red]}Her training went poorly.{/color}",
                        "machine good" : " The cold touch of metal and the elastic feel of rubber against her skin sent %s over the top. {color=[c_green]}Her training went well.{/color}",
                        "machine average" : " %s felt very odd attached to a strange, vibrating artefact in the middle of a workshop full of bizarre sex toys. {color=[c_white]}Her training went normally.{/color}",
                        "machine bad" : " %s was scared by the spiky, threatening look of the machine and couldn't relax. {color=[c_red]}Her training went poorly.{/color}",

#                        "naked result good" : "{color=[c_green]}%s was aroused by having her body on display before the %s, her nipples becoming visibly erect.{/color} Gizel pinched them hard, teasing her mercilessly.",
#                        "naked result average" : "{color=[c_white]}%s felt confused and ashamed, standing naked and exposed.{/color} She blushed as Gizel made her display every part of her body to the %s.",
#                        "naked result bad" : "{color=[c_lightred]}%s cowered and cried as she was made to stand naked in front of the %s.{/color}.Gizel commented harshly on her poor performance.",
#                        "service result good" : "{color=[c_green]}%s kneeled and starting working on the %s. She did her best to frown and hide her enjoyment, but Gizel could see she was getting wet.{/color}",
#                        "service result average" : "{color=[c_white]}%s did what she was asked, polishing the %s's strange dick with her lips and tongue.{/color}",
#                        "service result bad" : "{color=[c_lightred]}Tears ran down %s's cheeks as the %s forcefully fucked her throat.{/color}",
#                        "sex result good" : "{color=[c_green]}%s could hardly hide her sighs and screams of pleasure as the %s started fucking her mercilessly.{/color}",
#                        "sex result average" : "{color=[c_white]}%s shivered and moaned as the %s pumped its large, strange dick back and forth inside her tight pussy.{/color}",
#                        "sex result bad" : "{color=[c_lightred]}%s screamed in pain and fought weakly as the %s violently fucked her.{/color}",
#                        "anal result good" : "{color=[c_green]}%s yelled with pleasure as her ass got ravaged by the %s's large cock.{/color}",
#                        "anal result average" : "{color=[c_white]}%s moaned with a mix of pain and shameful pleasure as the %s violated her asshole.{/color}",
#                        "anal result bad" : "{color=[c_lightred]}%s screamed in pain and cried bitterly as the %s forced its large cock inside her tight asshole.{/color}",
#                        "fetish result good" : "{color=[c_green]}%s squirmed with confusion and pleasure, and quickly reached climax as the %s relentlessly violated her bound body.{/color}",
#                        "fetish result average" : "{color=[c_white]}%s screamed and moaned as the %s inflicted a strange mix of pain and pleasure on her weak body.{/color}",
#                        "fetish result bad" : "{color=[c_lightred]}%s shrieked with pain as the %s ruthlessly defiled her defenseless body.{/color}",
#                        "bisexual result good" : "{color=[c_green]}%s and Gizel strated licking and fingering each other's pussy, and soon forgot the %s as they passionately brought each other to climax.{/color} Gizel was very satisfied.",
#                        "bisexual result average" : "{color=[c_white]}Gizel forced %s to service both her and the %s.{/color} They both came forcefully on the poor girl's face. She was left confused by the whole ordeal.",
#                        "bisexual result bad" : "{color=[c_lightred]}%s was disgusted and tried to let out muffled screams as Gizel forcefully buried her pussy into her face, nearly choking her, while the %s tended to her other holes.{/color}",
#                        "group result good" : "{color=[c_green]}As %s and the %ss fucked in a variety of positions, she started enjoying herself and taking the lead, showing the minions which holes to use invitingly.{/color}",
#                        "group result average" : "{color=[c_white]}Grumbling, %s followed orders and used all of her holes to pleasure the %ss. However, she didn't seem to hate it as much as she was pretending to.{/color}",
#                        "group result bad" : "{color=[c_lightred]}%s cried and screamed as the %ss took turns violating her body.{/color} Gizel kept tauting her during the whole ordeal as she sobbed silently.",
                        "pen obedience": "%s reflected on her unfortunate circumstances and misdeeds that brought her to the farm. {color=[c_green]}She thinks that perhaps, if she was more obedient, she wouldn't get in trouble.{/color}",
                        "pen constitution": "Even though she was locked in, %s was determined to stay in shape. {color=[c_green]}She did some abs crunches and push ups and has become fitter.{/color}",
                        "pen sensitivity": "%s was bored and started thinking about the weird creatures in the farm and their more 'unusual' features. {color=[c_green]}Soon, she was feeling flushed and strangely aroused.{/color}",
                        "pen libido": "%s was feeling bored and horny, so she decided to masturbate a little, listening to the strange noises of the farm. {color=[c_green]}She enjoyed herself.{/color}",

                        "holding gentle obedience" : "Gizel sent %s to clean up the farm, telling her to scrub every corner of the barn and wash the multiple stains on the floor. %s sighed and got to work.",
                        "holding gentle constitution" : "Gizel made %s run laps around the back on the horsetrack, stopping and yelling at %s to go faster from time to time to keep her on edge.",
                        "holding gentle sensitivity" : "Gizel used %s as her personal servant to pursue her perverted fantasies with a variety of strange toys. Gizel didn't push %s too much, but she still discovered new things.",
                        "holding gentle libido" : "Gizel asked %s to tend to the minions: feeding them, cleaning them, and helping them 'release their stress'. %s learnt a good deal about the minions' peculiar anatomy as she worked.",
                        "holding tough obedience" : "Gizel sent %s to clean up the farm, telling her to scrub every corner of the barn and wash the multiple stains on the floor. %s did what she was asked, rather than face the threat of Gizel's magical lash.",
                        "holding tough constitution" : "Gizel made %s run laps around the back on the horsetrack, giving %s vicious swats with a riding crop whenever she caught her slowing down.",
                        "holding tough sensitivity" : "Gizel used %s as her personal servant to pursue her perverted fantasies, forcing her to lick her body and use various toys on her hungry holes. It was tough, but %s learnt new things.",
                        "holding tough libido" : "Gizel asked %s to tend to the minions: feeding them, cleaning them, and helping them 'release their stress'. Gizel forced her to touch parts of their anatomy she wasn't comfortable around, arousing some strange feelings in %s.",
                        "holding hardcore obedience" : "Gizel sent %s to clean up the farm, telling her to scrub every corner of the barn and wash the multiple stains on the floor. %s got a taste of her whip mercilessly if any dirt was left.",
                        "holding hardcore constitution" : "Gizel made %s run laps around the back on the horsetrack, wearing various punishment instruments like a wooden collar, shackles or nipple clamps. %s had to suffer through it to get stronger.",
                        "holding hardcore sensitivity" : "Gizel used %s as her personal servant to pursue her perverted fantasies, forcing her to lick her body and use various toys on her hungry holes. She made sure %s helped with {i}everything{/i}, especially what she was most uncomfortable with.",
                        "holding hardcore libido" : "Gizel asked %s to tend to the minions: feeding them, cleaning them, and helping them 'release their stress'. Gizel told %s she was not allowed to use her hands unless she would get a beating, forcing her to get creative.",

                        "holding obedience good": " As an added challenge, Gizel made %s wear tight ropes bound across her body as she went on with her work. {color=[c_green]}The rough ropes rubbed against her body in a way both uncomfortable and oddly arousing.{/color}",
                        "holding obedience bad": " {color=[c_lightred]}%s was disgusted by all the filth and bodily fluids left over by Gizel's minions.{/color}",
                        "holding constitution good": " Gizel thought it would drive %s wilder to roam outside free of clothes, so she made her run naked alongside the horses. {color=[c_green]}Being naked outdoors with the animals made her more comfortable with her body.{/color}",
                        "holding constitution bad": " {color=[c_lightred]}As %s completed her laps in record timing, she gave Gizel a contemptuous and defiant look.{/color}",
                        "holding sensitivity good": " %s gives Gizel a wonderful orgasm as she licks her erect clit with a skillful tongue. {color=[c_green]}She is now more familiar with ways to pleasure a woman.{/color}",
                        "holding sensitivity bad": " Gizel worked %s too hard, leaving her exhausted and panting on the floor. {color=[c_lightred]}Her constitution has suffered.{/color}",
                        "holding libido good": " {color=[c_green]}Several hours spent working with the minions have allowed %s to increase her technique.{/color}",
                        "holding libido bad": " {color=[c_lightred]}As a result of spending too many hours jerking off minions, %s's technique has become more mechanical.{/color}",
                        }

    farm_holding_stats = {"constitution" : ("naked", "obedience"), "obedience" : ("fetish", "libido"), "sensitivity" : ("bisexual", "constitution"), "libido" : ("service", "sensitivity")}

    farm_holding_tags = {"constitution" : ["run", "constitution"], "obedience" : ["obedience", "maid"], "sensitivity" : ["sensitivity"], "libido" : ["libido"]}

    pref_response = {
                    "modest refuses" : "Me, %s? NO!!! Don't!!! Don't do that to me! *horrified*",
                    "modest very reluctant" : "Wait, %s? This is outrageous! It's disgusting, it's dirty... Please stop! *scared*",
                    "modest reluctant": "No, don't look at me... It's not right, %s... I feel so ashamed... *embarrassed*",
                    "modest a little reluctant" : "I don't really want to do this, %s... It's wrong... Aaah! *shy*",
                    "modest indifferent" : "Oh, making me do this, %s again... You're such a pervert... *blush*",
                    "modest a little interested" : "Mmmh, it's like I'm getting used to %s... Wait, I didn't mean that! *panic*",
                    "modest interested" : "Ah, %s... It's not so bad... Mmmh... *flushed*",
                    "modest very interested" : "Oh, I think I love %s... I feel like a slut... *moan*",
                    "modest fascinated" : "I can't believe it, %s feels so good... Look at me! I've become a dirty, dirty bitch! *cumming*",
                    "lewd refuses": "NO, not %s!!! Don't touch me, I HATE it!!! *horrified*",
                    "lewd very reluctant": "I told you I hate %s... Why do I have to keep doing this? Ah!!! *ashamed*",
                    "lewd reluctant": "You know I don't like %s... Don't look at me... Ahaa! *embarrassed*",
                    "lewd a little reluctant": "You're doing perverted things to me again, %s... It makes me feel strange... *shy*",
                    "lewd indifferent": "Mmmh, %s... *blush*",
                    "lewd a little interested": "Oh, %s, that's good... *licks her lips*",
                    "lewd interested": "Mmmh, %s... I feel wet already... *flushed*",
                    "lewd very interested": "Oh, %s, it makes me so horny... I get so wet when being watched... Aaaah!!! *moan*",
                    "lewd fascinated": "Oh... I'm about to come already! Ahaaa, %s is the best!!! *cumming*",
                    }

    minion_adjectives = {
                        "stallion" : ["erect", "drooling", "horny", "well-built", "snorting", "bulky", "nickering", "sleazy"],
                        "beast" : ["drooling", "horny", "filthy", "dirty", "rowdy", "excited", "fat"],
                        "monster" : ["horny", "gooey", "filthy", "dirty", "large", "wiggly", "weird-looking", "strange", "sleazy"],
                        "machine" : ["buzzing", "strange", "weird-looking", "bizarre", "enchanted", "convoluted", "protruding"],
                        }

    minion_name_dict = {
                        "consonants" : ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"],
                        "vowels" : ["a", "e", "i", "o", "u", "y"],
                        "monster1" : ["gr", "kr", "le", "ry", "shr", "dr", "kz", "gz", "th", "bl", "kl", "wr", "qr", "mr", "sh"],
                        "monster2" : ["ck", "k", "rk", "rz", "rm", "xx", "uz", "oo", "hu", "qq", "tz", "zt", "rh", "th"],
                        }

    girl_name_dict = {"syllabs" : ["sha", "she", "shee", "shi", "wa", "ri", "ree", "ra", "ru", "ti", "ta", "ty", "ya", "yu", "sa", "so", "su", "se", "sy", "da", "de", "di", "do", "dy", "fa", "fe", "fio", "fia", "gi", "hu", "ha", "hyu", "ja", "ju", "ji", "ka", "ky", "ki", "kyo", "kyu", "la", "li", "le", "lo", "lu", "lyu", "lia", "lya", "lee", "loo", "za", "zi", "zu", "ze", "zee", "xa", "xy", "xe", "ca", "ce", "chi", "chu", "va", "vi", "vy", "ve", "bu", "be", "na", "ne", "ni", "nya", "nyu", "nee", "ma", "mu", "me", "mi", "myu", "mia", "mya"],
                      "fillers" : ["n", "r", "l", "s", "'", "", "", ""],
                      "enders" : ["n", "l", "nn", "a", "ya", "na", "ly", "", "", ""],
                      "last_syllabs" : ["jo", "sho", "to", "ya", "ma", "mi", "yo", "ko", "na", "ye", "yu", "ka", "ta", "fu", "ro", "sa", "shi", "ki", "no", "ra", "re", "tsu", "chi", "shi", "se", "n", "mu", "ne", "kyo", "ku"],
                      }


    farm_type_list = ["machine", "beast", "monster", "stallion"]
    farm_inst_list = ["stables", "pig stall", "monster den", "workshop"]
    farm_installations_dict = {"machine" : "workshop", "beast" : "pig stall", "monster" : "monster den", "stallion" : "stables"}

    ## FEAR POWERS AND MOJO

    NORMAL_MOJO_VALUE = 7.5 # Gain 1 purple mojo for each x amounts of fear raised (regular interactions)
    FARM_MOJO_VALUE = 2.5 # Gain 1 coloured mojo for each x amounts of fear raised (farm interactions)

    mojo_act_dict = {
                "naked": ("green",),
                "service": ("green",),
                "sex": ("blue",),
                "anal": ("red",),
                "fetish": ("yellow",),
                "group": ("blue", "red"),
                "bisexual": ("yellow",),
                "sensitivity": ("green",),
                "libido": ("blue",),
                "constitution": ("red",),
                "obedience": ("yellow",),
                }

    ## CITY MERCHANTS

    merchant_dict = {"Stella" : "stallion", "Goldie" : "beast", "Willow" : "monster", "Gina" : "machine"}

    merchant_title = {
                    "Stella" : "Headmaster", "Goldie" : "Rancher", "Willow" : "Monster catcher", "Gina" : "Weird scientist",
                    "Riche" : "Florist", "Ramias" : "Weapon dealer", "Gurigura" : "Supply merchant", "Katryn" : "Trinket merchant", "Gift Shop Girl" : "Exotic emporium", "Today" : "Tailor", "shop" : "Items",
                    }

    merchant_greetings = {
                        "shop greeting" : "Hi, handsome! Please take a look at my wares... *wink*",
                        "shop caravan" : "A caravan has arrived, and we have new items. Check it out!",
                        "shop bought something" : "You just bought the [it.name]. I'm sure you will put it to good use.{w=2.0}{nw}",
                        "shop no money" : "I'm sorry, but you don't have enough gold...",

                        "Stella greeting" : "Hmpf, look who's come here. I hope you're not going to waste my time.",
                        "Stella bought something" : "Fine, give me the gold, and it's yours. Now go, unless you're buying something else.{w=2.0}{nw}",
                        "Stella no money" : "You ain't got the coin, pal. Get out of here.",

                        "Goldie greeting" : "How can I help you?",
                        "Goldie bought something" : "Thank you! Please treat it with care.{w=2.0}{nw}",
                        "Goldie no money" : "I'm sorry, but you don't seem to have enough money right now.",

                        "Willow greeting" : "Hey, if it isn't my friendly neighbor! You'll be amazed to see what I just caught.",
                        "Willow bought something" : "Deal, just take it... You're gonna have fun!{w=2.0}{nw}",
                        "Willow no money" : "Aw, you meanie, are you trying to take advantage of me? Your pouch is empty!",

                        "Gina greeting" : "Mmh, what if I adjusted this button... No, that's not it... Sorry. How can I help you?",
                        "Gina bought something" : "Sure, I didn't need this anyway...{w=2.0}{nw}",
                        "Gina no money" : "Sorry, but this is expensive equipment. Don't touch it unless you have the coin to buy it.",

                        "Riche greeting" : "Oh, hello. *smile*",
                        "Riche bought something" : "Thank you! Come again soon!{w=2.0}{nw}",
                        "Riche no money" : "Oh, sorry... But you haven't got the gold.",

                        "Ramias greeting" : "Oh, it's you... Greetings.",
                        "Ramias bought something" : "Thank you. You will not be disappointed.{w=2.0}{nw}",
                        "Ramias no money" : "Hmm... It doesn't look like you have enough gold.",

                        "Gurigura greeting" : "Hiii!!! *smile*",
                        "Gurigura bought something" : "Thaaank yooou! Teehee.{w=2.0}{nw}",
                        "Gurigura no money" : "Hey, wait a minute... You don't have enough gold, mister!",

                        "Katryn greeting" : "Oh, hi. I hope you're not going to waste my time.",
                        "Katryn bought something" : "Give me the money first... Good.{w=2.0}{nw}",
                        "Katryn no money" : "What the... You haven't got the gold, stupid!",

                        "Gift Shop Girl greeting" : "Oh, hello. *smile*{w=2.0}{nw}",
                        "Gift Shop Girl bought something" : "Thank you, dear sir.{w=2.0}{nw}",
                        "Gift Shop Girl no money" : "Sorry sir... But you haven't got the gold.",

                        "Today greeting" : "Hi there, big bro! What can we help you with? *smile*",
                        "Yesterday greeting" : "Ah... Hello... *blush*",
                        "Today bought something" : "Thank you, big bro! *wink*{w=2.0}{nw}",
                        "Yesterday bought something" : "Thanks.{w=2.0}{nw}",
                        "Today no money" : "Hold it, bro. You don't have the gold to pay for this.",
                        }


    shopgirl_comment = {
                        "wood" : "New shelf, perfect!", "leather" : "Great! This leather basket will fit nicely in the entrance.",
                        "dye" : "Nice! This freshly painted display looks sweet.", "marble" : "Ooh, a marble counter! That's going to make all the other shopkeepers jealous, yay!",
                        "ore" : "Copper-plated counter shelves are sure to draw some attention. Very nice.", "silk" : "Ah, finally, some soft, smooth silk to hold the fragile items... And rub my face into!",
                        "diamond" : "A girl's best friends... You've got style, handsome! And so does my new diamond-encrusted display... [emo_heart]"
                        }



    ## POPULATIONS ##

    pop_name_dict = {
                    "M beggars" : ("vagrant", "shabby-looking guy", "beggar", "street wanderer"),
                    "M thugs" : ("ruffian", "thug", "bandit", "petty thief", "rogue", "burglar"),
                    "M laborers" : ("laborer", "worker", "street peddler", "servant", "peasant"),
                    "M sailors" : ("pirate", "sailor", "docker", "shipmate", "ol' seadog", "mariner"),
                    "M commoners" : ("commoner", "overseer", "clerk", "trader", "guard", "builder", "acolyte"),
                    "M craftsmen": ("craftsman", "artisan", "blacksmith", "carpenter", "artificer", "mason"),
                    "M bourgeois" : ("merchant", "bookkeeper", "herborist", "shopkeeper", "innkeeper", "priest", "squire"),
                    "M guild members" : ("guild member", "inventor", "illusionist", "slave trader", "spice trader", "guard officer"),
                    "M patricians" : ("patrician", "landowner", "banker", "city official", "knight", "bishop"),
                    "M aristocrats" : ("aristocrat", "lord", "gentleman", "court wizard", "courtier", "governor", "guild master"),
                    "M nobles" : ("noble", "count", "highborn", "knight commander", "baron", "earl", "viscount", "cardinal"),
                    "M royals" : ("marquess", "prince", "viceroy", "duke", "patriarch", "sultan"),

                    "F beggars" : ("female vagrant", "shabby-looking gal", "beggaress", "street girl"),
                    "F thugs" : ("female ruffian", "female thug", "lady bandit", "female thief", "female rogue", "old hag"),
                    "F laborers" : ("female laborer", "female worker", "woman peddler", "woman servant", "female peasant"),
                    "F sailors" : ("lady pirate", "female sailor", "dockgirl", "lady shipmate", "ship's nurse", "female mariner"),
                    "F commoners" : ("commoner lady", "female overseer", "woman clerk", "female trader", "female guard", "nun"),
                    "F craftsmen": ("craftswoman", "female artisan", "woman blacksmith", "carpentress", "female mason"),
                    "F bourgeois" : ("female merchant", "lady bookkeeper", "lady herborist", "woman shopkeeper", "female innkeeper", "priestess", "lady squire"),
                    "F guild members" : ("guild member", "girl inventor", "female illusionist", "slave trader", "woman spice trader", "female guard officer"),
                    "F patricians" : ("matron", "woman landowner", "woman banker", "lady official", "lady knight", "lady bishop"),
                    "F aristocrats" : ("aristocrat", "fair lady", "gentlewoman", "court sorceress", "lady courtier", "lady governor", "guild mistress"),
                    "F nobles" : ("noble lady", "countess", "highborn lady", "holy priestess", "baroness", "viscountess", "lady cardinal"),
                    "F royals" : ("marchioness", "princess", "queen consort", "duchess", "matriarch", "sultana")
                    }



    # Maximum difficulty for a given customer rank
    customer_rank_dict = {
                        1 : 40,
                        2 : 70,
                        3 : 110,
                        4 : 160,
                        5 : 1000,
                        }

    attract_pop_dict = {0 : "      ", 1 : "A few ", 2: "Some  ", 3 : "Many  ", 4 : "A lot ", 5 : "Loads "}

    # Encounters are tuples with label (used with prefix "city_") and probability. Tuples can be used with multiple labels

    encounters = (("none", 10), ("gossip", 30), ("ambush", 5), ("rob", 5), ("luck", 15), ("mob", 5), (("rape", "impress", "slave"), 10), (("gamble", "thief", "wrestle"), 10), (("cat", "secret", "gypsy"), 10))

    encounter_pics = {
                    "rape" : ("monster1.webp", "monster2.webp", "monster3.webp", "monster4.webp", "monster5.webp", "monster6.webp", "monster7.webp", "monster8.webp", "monster9.webp", "monster10.webp"),
                    "impress" : "impress0.webp",
                    "impress1" : ("impress1_1.webp", "impress1_2.webp", "impress1_3.webp", "impress1_4.webp", "impress1_5.webp", "impress1_6.webp", "impress1_7.webp", "impress1_8.webp", "impress1_9.webp", "impress1_10.webp"),
                    "impress2" : ("impress2_1.webp", "impress2_2.webp"),
                    "impress3" : ("impress3_1.webp", "impress3_2.webp", "impress3_3.webp"),
                    "impress4" : "impress4.webp",
                    "slave" : ("slave1.webp", "slave2.webp", "slave3.webp", "slave4.webp", "slave5.webp", "slave6.webp", "slave7.webp", "slave8.webp", "slave9.webp", "slave10.webp"),
                    "slave_service" : (("slave service1.webp","slave service2.webp", "slave service3.webp", "slave service4.webp"), ("slave service5.webp","slave service6.webp", "slave service7.webp", "slave service8.webp")),
                    "slave_sex" : (("slave sex1.webp","slave sex2.webp", "slave sex3.webp", "slave sex4.webp"), ("slave sex5.webp","slave sex6.webp", "slave sex7.webp", "slave sex8.webp")),
                    "slave_anal" : (("slave anal1.webp","slave anal2.webp", "slave anal3.webp", "slave anal4.webp"), ("slave anal5.webp","slave anal6.webp", "slave anal7.webp", "slave anal8.webp")),
                    "slave_fetish" : (("slave fetish1.webp","slave fetish2.webp", "slave fetish3.webp", "slave fetish4.webp"), ("slave fetish5.webp","slave fetish6.webp", "slave fetish7.webp", "slave fetish8.webp")),
                    "slave_success" : ("slave service9.webp","slave service10.webp", "slave service11.webp", "slave service12.webp"),
                    "gamble" : (("gambler1_1.webp", "gambler1_2.webp", "gambler1_3.webp"), ("gambler2_1.webp", "gambler2_2.webp", "gambler2_3.webp"), ("gambler3_1.webp", "gambler3_2.webp", "gambler3_3.webp"), ("gambler4_1.webp", "gambler4_2.webp", "gambler4_3.webp"), ("gambler5_1.webp", "gambler5_2.webp", "gambler5_3.webp"), ("gambler6_1.webp", "gambler6_2.webp", "gambler6_3.webp"), ("gambler7_1.webp", "gambler7_2.webp", "gambler7_3.webp"), ("gambler8_1.webp", "gambler8_2.webp", "gambler8_3.webp"), ("gambler9_1.webp", "gambler9_2.webp", "gambler9_3.webp")),
                    "thief" : ("thief1.webp", "thief2.webp", "thief3.webp", "thief4.webp", "thief5.webp", "thief6.webp"),
                    "wrestle" : ("arm wrestling1.webp", "arm wrestling2.webp", "arm wrestling3.webp", "arm wrestling4.webp", "arm wrestling5.webp"),
                    "cat" : ("cat1.webp", "cat2.webp", "cat3.webp", "cat4.webp", "cat5.webp", "cat6.webp", "cat7.webp", "cat8.webp", "cat9.webp", "cat10.webp"),
                    "cat_found" : ("cat found.webp",),
                    "cat_sex" : (("catsex1_1.webp", "catsex1_2.webp"), ("catsex2_1.webp", "catsex2_2.webp"), ("catsex3_1.webp", "catsex3_2.webp"), ("catsex4_1.webp", "catsex4_2.webp"), ("catsex5_1.webp", "catsex5_2.webp"), ("catsex6_1.webp", "catsex6_2.webp"), ("catsex7_1.webp", "catsex7_2.webp"), ("catsex8_1.webp", "catsex8_2.webp"), ("catsex9_1.webp", "catsex9_2.webp"), ("catsex10_1.webp", "catsex10_2.webp"), ("catsex11_1.webp", "catsex11_2.webp")),
                    "cat_duo" : (("catduo1_1.webp", "catduo1_2.webp", "catduo1_3.webp", "catduo1_4.webp"), ("catduo2_1.webp", "catduo2_2.webp", "catduo2_3.webp", "catduo2_4.webp"), ("catduo3_1.webp", "catduo3_2.webp", "catduo3_3.webp", "catduo3_4.webp")),
                    "secret" : ("secret1.webp", "secret2.webp", "secret3.webp"),
                    "secret_empty" : ("secret empty1.webp", "secret empty2.webp", "secret empty3.webp"),
                    "secret_girl" : ("secret girl1.webp", "secret girl2.webp", "secret girl3.webp", "secret girl4.webp", "secret girl5.webp", "secret girl6.webp", "secret girl7.webp", "secret girl8.webp", "secret girl9.webp", "secret girl10.webp"),
                    "gypsy" : (("gypsy1_0.webp", "gypsy1_2.webp", "gypsy1_3.webp"), ("gypsy1_1.webp", "gypsy1_2.webp", "gypsy1_3.webp"), ("gypsy2_1.webp", "gypsy2_2.webp", "gypsy2_3.webp"), ("gypsy3_1.webp", "gypsy3_2.webp", "gypsy3_3.webp"), ("gypsy4_1.webp", "gypsy4_2.webp", "gypsy4_3.webp"), ("gypsy5_1.webp", "gypsy5_2.webp", "gypsy5_3.webp"), ("gypsy6_1.webp", "gypsy6_2.webp", "gypsy6_3.webp"), ("gypsy7_1.webp", "gypsy7_2.webp", "gypsy7_3.webp"), ("gypsy8_1.webp", "gypsy8_2.webp", "gypsy8_3.webp")),
                    "rob" : (("rob1_1.webp", "rob1_2.webp"), ("rob2_1.webp", "rob2_2.webp"), ("rob3_1.webp", "rob3_2.webp"), ("rob4_1.webp", "rob4_2.webp"), ("rob5_1.webp", "rob5_2.webp"), ("rob6_1.webp", "rob6_2.webp"), ("rob7_1.webp", "rob7_2.webp"), ("rob8_1.webp", "rob8_2.webp"), ("rob9_1.webp", "rob9_2.webp"), ("rob10_1.webp", "rob10_2.webp")),
                    "ambush" : ("ambush1.webp", "ambush2.webp", "ambush3.webp", "ambush4.webp", "ambush5.webp", "ambush6.webp"),
                    "mob" : ("mob1.webp", "mob2.webp", "mob3.webp"),
                    "mob_sex" : ("mob sex1.webp", "mob sex2.webp", "mob sex3.webp"),
                    }


    ## WEEK DAYS ##

    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    workshift_dict = {0: "Rest", 50: "Half Shift", 100: "Full Shift"}
    workshift_color = {0: c_emerald, 50: c_prune, 100: c_orange}


    ## MC picture index

    MC_class_index = {"Warrior" : 0, "Wizard" : 3, "Trader" : 6}

    ## Roman numbers

    roman_numbers = {1 : "I", 2 : "II", 3 : "III", 4 : "IV", 5 : "V", 6 : "VI", 7 : "VII", 8 : "VIII", 9 : "IX", 10 : "X"}

    ## JOBS and SEX ACTS

    all_jobs = ["waitress", "dancer", "masseuse", "geisha"]
    all_sex_acts = ["service", "sex", "anal", "fetish"]
    extended_sex_acts = ["naked", "service", "sex", "anal", "fetish", "bisexual", "group"]
    farm_hardcore_acts = ["beast", "monster"]

    opposite_sex_acts = {
                        "naked" : ["service", "sex", "anal", "fetish", "bisexual", "group"], # This is hardcoded for faster fixation picture search
                        "service" : ["sex", "anal", "fetish", "bisexual", "group"],
                        "sex" : ["service", "anal", "fetish", "bisexual", "group"],
                        "anal" : ["service", "sex", "fetish", "bisexual", "group"],
                        "fetish" : ["service", "sex", "anal", "bisexual", "group"],
                        "bisexual" : ["group", ],
                        "group" : [],
                        None : [],
                        }

    normal_tags = ("profile", "portrait", "rest", "waitress", "dancer", "masseuse", "geisha")
    all_farm_tags = ("big", "beast", "monster", "machine")

    job_sort_value = {"whore" : 0, "waitress" : 10, "dancer" : 20, "masseuse" : 30, "geisha" : 40, None : 90, "hurt" : 80, "away" : 70, "farm" : 70}

    job_color = {"whore" : c_red, "waitress" : c_lightgreen, "dancer" : c_pink, "masseuse" : c_yellow, "geisha" : c_magenta, None : c_white, "hurt" : c_red, "away" : c_lightblue, "farm" : c_brown}


    ## STAT NAMES (SKILLS) ##


    gstats_main = [
        "Charm",
        "Beauty",
        "Body",
        "Refinement",
        "Sensitivity",
        "Libido",
        "Constitution",
        "Obedience",
        ]

    gstats_sex = [
        "Service",
        "Sex",
        "Anal",
        "Fetish"
        ]

    all_skills = [s.lower() for s in gstats_main + gstats_sex]


    ## STAT DESCRIPTION ##

    gstats_dict = {
                    "Beauty" : "How beautiful she looks. Affects work as a {b}masseuse{/b} and regular {b}sex{/b}. Current masseuse capacity: {b}%s{/b} customer%s.",
                    "Body" : "How well-shaped and firm her body is. Affects work as a {b}dancer{/b} and {b}anal{/b} sex. Current dancer capacity: {b}%s{/b} customer%s.",
                    "Charm" : "Her personality and presence. Affects work as a {b}waitress{/b} and sexual {b}service{/b}. Current waitress capacity: {b}%s{/b} customer%s.",
                    "Refinement" : "How intelligent and worldly she is. Affects work as a {b}geisha{/b} and {b}fetish{/b} sex acts. Current geisha capacity: {b}%s{/b} customer%s.",
                    "Libido" : "How eager for sex she is. Affects {b}dancer{/b}, {b}sex{/b} and max {b}whoring{/b} customers. Current whore capacity: {b}%s{/b} customer%s.",
                    "Sensitivity" : "How sensitive she is to her body and her partners. Affects {b}masseuse{/b}, {b}service{/b} and improves customer {b}satisfaction{/b}.",
                    "Constitution" : "Her stamina. Affects {b}waitress{/b}, {b}anal{/b} sex, improves her maximum {b}energy{/b} and allows her to serve {b}more customers{/b}.",
                    "Obedience" : "How receptive she is to orders and servitude. Affects {b}geisha{/b}, {b}fetish{/b} sexual acts and chances of accepting {b}work{/b} or {b}training{/b}.",
                    "Service" : "How good she is with handjobs, blowjobs and other sexual services.",
                    "Sex" : "How good she is at regular sex.",
                    "Anal" : "How good she is at anal sex.",
                    "Fetish" : "How good she is at BDSM and other unusual requests."
                }

    gstats_descript = {
                    "beauty" : "a beautiful girl",
                    "body" : "a girl with a hot body",
                    "charm" : "a charming girl",
                    "refinement" : "a refined girl",
                    }

    gstat_job_skill = {
                    "Beauty" : "masseuse",
                    "Body" : "dancer",
                    "Charm" : "waitress",
                    "Refinement" : "geisha",
                    "Libido" : "whore",
                    }

    MC_stat_color = {
                    "strength" : "{color=[c_darkred]}%s{/color}",
                    "defense" : "{color=[c_darkred]}%s{/color}",
                    "spirit" : "{color=[c_darkblue]}%s{/color}",
                    "charisma" : "{color=[c_emerald]}%s{/color}",
                    "speed" : "{color=[c_lightblue]}%s{/color}",
                    }

    preference_color = {
                "refuses" : "{color=#F70000}%s{/color}",
#                 "extremely reluctant" : "{color=#FF2626}%s{/color}",
                "very reluctant" : "{color=#FF5353}%s{/color}",
                "reluctant" : "{color=#FF8E8E}%s{/color}",
                "a little reluctant" : "{color=#FFB5B5}%s{/color}",
                "indifferent" : "{color=[c_white]}%s{/color}",
                "a little interested" : "{color=#BDF4CB}%s{/color}",
                "interested" : "{color=#7CEB98}%s{/color}",
                "very interested" : "{color=#1FCB4A}%s{/color}",
                "fascinated" : "{color=[c_orange]}%s{/color}",
                None: "%s",
                }


    ## GIRL PERSONALITIES ##

#    base_interaction_limits = [-50, -15, 15, 50]

    alignment_bonus = {
                    "good_love" : 1.25,
                    "good_fear" : 0.75,
                    "neutral_love" : 1.0,
                    "neutral_fear" : 1.0,
                    "evil_love" : 0.75,
                    "evil_fear" : 1.25
                    }

    mood_description = {
                        "++++++" : "She feels blessed. Her mood is {b}ecstatic{/b}",
                        "+++++" : "Her mood is {b}elated{/b}",
                        "++++" : "She is {b}very happy{/b}",
                        "+++" : "She is {b}happy{/b}",
                        "++" : "She is satisfied",
                        "+" : "She is {b}content{/b}",
                        "0" : "Her mood is {b}neutral{/b}",
                        "-" : "She is {b}discontent{/b}",
                        "--" : "She is {b}unsatisfied{/b}",
                        "---" : "She is {b}unhappy{/b}",
                        "----" : "She is {b}very unhappy{/b}",
                        "-----" : "Her mood is {b}miserable{/b}",
                        "------" : "Her life is hell. Her mood is {b}abysmal{/b}",

                        "change +++" : " and {b}improving fast{/b}",
                        "change ++" : " and {b}improving{/b}",
                        "change +" : " and {b}improving a little{/b}",
                        "no change" : " and {b}stable{/b}",
                        "change -" : " and {b}worsening a little{/b}",
                        "change --" : " and {b}worsening{/b}",
                        "change ---" : " and {b}worsening fast{/b}",
                        }

    love_description = {
                        "++++++" : "You are everything to her. She worships you.",
                        "+++++" : "She adores you.",
                        "++++" : "She loves you.",
                        "+++" : "She likes you a lot.",
                        "++" : "She is fond of you.",
                        "+" : "She thinks you're all right.",
                        "0" : "She isn't sure how she feels about you.",
                        "-" : "She doesn't like you much.",
                        "--" : "She dislikes you.",
                        "---" : "She resents you.",
                        "----" : "She despises you.",
                        "-----" : "She hates you.",
                        "------" : "She thinks you're the worst. She wants you dead.",
                        }

    fear_description = {
                        "++++++" : "She lives in a world of terror, day and night. She is dead afraid of you.",
                        "+++++" : "You terrify her.",
                        "++++" : "She is very scared of you.",
                        "+++" : "She is scared of you.",
                        "++" : "She is a little scared of you.",
                        "+" : "She distrusts you.",
                        "0" : "She is on her guard around you.",
                        "-" : "She is nervous around you.",
                        "--" : "She is starting to ease up around you.",
                        "---" : "She is more relaxed around you. She feels confident you won't do anything bad to her.",
                        "----" : "She feels like she can act freely.",
                        "-----" : "She feels like she can do what she wants.",
                        "------" : "She feels like a princess, doing whatever she likes.",
                        "M++++++" : "Her true place is at your feet, shivering with terror and desire.",
                        "M+++++" : "The more you hurt her, the happier she gets.",
                        "M++++" : "It seems she likes being roughed up. She wants more.",
                        "M+++" : "She is scared of you, but strangely attracted to you.",
                        "M---" : "She is relaxed around you, but something feels off.",
                        "M----" : "Shes feels safe with you, but also bored.",
                        "M-----" : "She doesn't understand why you are being so nice to her.",
                        "M------" : "She feels that it's all too much, she doesn't deserve this. She seems distressed",
                        }




    # gpersonality_attributes = ("extravert", "introvert", "idealist", "materialist", "lewd", "repressed", "dom", "sub", "very extravert", "very introvert", "very idealist", "very materialist", "very lewd", "very repressed", "very dom", "very sub")

    personality_attributes = [("extravert", "introvert"), ("idealist", "materialist"), ("lewd", "modest"), ("dom", "sub")]

    attribute_score_dict = { # Note: very X and X boni/mali will add up
                            "very extravert" : {"very extravert" : 3, "extravert" : 1, "introvert" : -1, "very introvert" : -3},
                            "extravert" : {"very extravert" : 1, "extravert" : 1, "introvert" : 0, "very introvert" : -1},
                            "introvert" : {"very extravert" : -1, "extravert" : 0, "introvert" : 1, "very introvert" : 1},
                            "very introvert" : {"very extravert" : -3, "extravert" : -1, "introvert" : 1, "very introvert" : 3},

                            "very idealist" : {"very idealist" : 3, "idealist" : 1, "materialist" : -1, "very materialist" : -3},
                            "idealist" : {"very idealist" : 1, "idealist" : 1, "materialist" : 0, "very materialist" : -1},
                            "materialist" : {"very idealist" : -1, "idealist" : 0, "materialist" : 1, "very materialist" : 1},
                            "very materialist" : {"very idealist" : -3, "idealist" : -1, "materialist" : 1, "very materialist" : 3},

                            "very lewd" : {"very lewd" : 3, "lewd" : 1, "modest" : -1, "very modest" : -3},
                            "lewd" : {"very lewd" : 1, "lewd" : 1, "modest" : 0, "very modest" : -1},
                            "modest" : {"very lewd" : -1, "lewd" : 0, "modest" : 1, "very modest" : 1},
                            "very modest" : {"very lewd" : -3, "lewd" : -1, "modest" : 1, "very modest" : 3},

                            # The Dom/Sub table is reversed, this is on purpose

                            "very dom" : {"very dom" : -3, "dom" : -1, "sub" : 1, "very sub" : 3},
                            "dom" : {"very dom" : -1, "dom" : 0, "sub" : 1, "very sub" : 1},
                            "sub" : {"very dom" : 1, "dom" : 1, "sub" : 0, "very sub" : -1},
                            "very sub" : {"very dom" : 3, "dom" : 1, "sub" : -1, "very sub" : -3},
                            }

    gpersonalities_likes = {
                            "very extravert" :  {"cute" : 1, "book" : -3, "precious" : 0, "erotica" : -1, "drinks": 3},
                            "very introvert" :  {"cute" : -1, "book" : 3, "precious" : 0, "erotica" : 1, "drinks": -3},
                            "very idealist" :   {"cute" : 3, "book" : 1, "precious" : -3, "erotica" : 0, "drinks": -1},
                            "very materialist": {"cute" : -1, "book" : -3, "precious" : 3, "erotica" : 0, "drinks": 1},
                            "very lewd" :       {"cute" : -3, "book" : -1, "precious" : 0, "erotica" : 3, "drinks": 1},
                            "very modest" :     {"cute" : 3, "book" : 1, "precious" : 0, "erotica" : -3, "drinks": -1},
                            "very dom" :        {"cute" : -3, "book" : -1, "precious" : 1, "erotica" : 0, "drinks": 3},
                            "very sub" :        {"cute" : 1, "book" : 3, "precious" : -1, "erotica" : 0, "drinks": -3},

                            # "meek" :            {"cute" : 4, "book" : 2, "precious" : 0, "erotica" : -2, "drinks": 2},
                            # "nerd" :            {"cute" : 0, "book" : 4, "precious" : -2, "erotica" : 2, "drinks": 2},
                            # "pervert" :         {"cute" : -2, "book" : 0, "precious" : 2, "erotica" : 4, "drinks": 2},
                            # "rebel" :           {"cute" : 2, "book" : 0, "precious" : 2, "erotica" : -2, "drinks": 4},
                            # "superficial" :     {"cute" : 2, "book" : -2, "precious" : 4, "erotica" : 2, "drinks": 0},
                            # "cold" :            {"cute" : -2, "book" : 2, "precious" : 4, "erotica" : 0, "drinks": 2},
                            # "masochist" :       {"cute" : 0, "book" : 2, "precious" : -2, "erotica" : 4, "drinks": 2},
                            # "sweet" :           {"cute" : 4, "book" : 2, "precious" : 2, "erotica" : 0, "drinks": -2}
                            }

init python:
    gpersonalities = {
                        "pervert" : Personality(name="pervert", attributes=("very extravert", "very lewd"), description="Wild and 'no limit' kind of girl. Curious about all sorts of sexual acts, the more perverted the better. Doesn't care for romance."),
                        "rebel" : Personality(name="rebel", attributes=("very extravert", "very dom"), often_stories = ["slave_story5"], description="Always fighting and contradicting others, fiercely independent. Must do things of her own free will."),
                        "cold" : Personality(name="cold", attributes=("very materialist", "very introvert"), description="Cold and detached, she doesn't show her feelings easily. She seems strangely unconcerned about what goes on around her, and uninterested in the fate of others."),
                        "nerd" : Personality(name="nerd", attributes=("very introvert", "very idealist"), often_stories = ["slave_story8"], description="Quiet and bookish. Rather light-headed. Curious. Doesn't like physical effort."),
                        "masochist" : Personality(name="masochist", attributes=("very introvert", "very sub"), description="The lower the better. She likes to be at the bottom and secretly enjoys being mistreated. Gifts and loving gestures annoy her, she doesn't deserve them."),
                        "bimbo" : Personality(name="bimbo", attributes=("very materialist", "very lewd"), description="Vain, attention-craved, cares about status and wealth. Loves presents and compliments. She has no qualms about using her body to get those things, too."),
                        "meek" : Personality(name="meek", attributes=("very modest", "very sub"), often_stories = ["slave_story4"], rarely_stories = ["slave_story5","slave_story8"], description="Shy, easily swayed, will cry rather than resist. Doesn't like conflict."),
#                         "heartless" : Personality(name="heartless", attributes=("very materialist", "very dom"), description="Cold, calculating, domineering and selfish. Will always try to benefit at the expense of others."),
                        "sweet" : Personality(name="sweet", attributes=("very idealist", "very extravert"), description="Lovely and sunny personality. Always positive. Rather romantic. Doesn't like negativity."),

                        "superficial" : Personality(name="superficial", attributes=("very extravert", "very materialist"), description="Ever the socialite, cares about being seen, preferably in the most outstanding outfit and expensive jewelry. Some call her needy and craving for attention, but she knows they're just jealous of her new shoes..."),
                        "holy" : Personality(name="holy", attributes=("very extravert", "very modest"), never_stories = ["slave_story7","slave_story8"], description="A firebrand promoter of religion and morality, she prays every night for the salvation of her soul and tries to convert others to her beliefs. With little success so far, but she won't give up."),
                        "helper" : Personality(name="helper", attributes=("very extravert", "very sub"), description="Always ready to help her friends, places herself after others. Can be a bit nosy sometimes."),
                        "creep" : Personality(name="creep", attributes=("very introvert", "very lewd"), description="Shy and awkward around people, she is obsessed about all sorts of dirty topics that she researches in her own time. Get complaints for stalking, a lot."),
                        "repressed" : Personality(name="repressed", attributes=("very introvert", "very modest"), description="Raised in a very strict environment, she lives in fear of her own impulses and tries her hardest to suppress them."),
                        "schemer" : Personality(name="schemer", attributes=("very introvert", "very dom"), description="Likes nothing more than to scheme and make grand plans, ready to assert her dominance over all living beings... Some day. In the meantime, if she has to suck a dick... So be it."),
                        "prude" : Personality(name="prude", attributes=("very materialist", "very modest"), rarely_stories = ["slave_story7","slave_story8"], description="Affects to be a good, Arios-fearing girl at all times. Frowns on frivolity and amoral behavior. Some think she has dirty thoughts in secret, but if so, she hides them well."),
                        "princess" : Personality(name="princess", attributes=("very dom", "very materialist"), often_stories = ["slave_story6"], rarely_stories = ["slave_story1","slave_story2","slave_story3","slave_story5","slave_story7","slave_story8"], never_stories = ["slave_story4"], description="A figurative princess (or is she?), she thinks everyone ought to be at her service and deliver on her every whim. Can be cruel, but mostly she is naive."),
                        "pet" : Personality(name="pet", attributes=("very materialist", "very sub"), rarely_stories = ["slave_story5","slave_story8"], description="The teacher's pet. Always ready to please her master, likes nothing more than to live in comfort at his feet. Some despise her lack of independence, calling her unpleasant names behind her back."),
                        "easy" : Personality(name="easy", attributes=("very lewd", "very idealist"), description="It's not her fault, she has always attracted men, and never had the heart to turn them down. Although many call her easy, her sole purpose is to spread joy. Hopefully not STDs."),
                        "class president" : Personality(name="class president", attributes=("very modest", "very idealist"), often_stories = ["slave_story8"], description="Must always be on top, strives to be exemplary and despises every kind of misconduct. The high expectations she has of others mirror the harsh discipline whe puts herself through."),
                        "tsundere" : Personality(name="tsundere", attributes=("very idealist", "very dom"), description="Easy to anger, hard to please, she has a secret soft spot. Will put herself at risk to help others, then kick their butts for needing help in the first place."),
                        "loyal" : Personality(name="loyal", attributes=("very idealist", "very sub"), often_stories = ["slave_story2"], description="Always follows orders, out of a sense of duty more than fear. Thinks everyone must know their place, and do their best at whatever job they hold. Even whores."),
                        "yandere" : Personality(name="yandere", attributes=("very lewd", "very dom"), rarely_stories = ["slave_story3","slave_story7"], description="Very high on the hot and neurotic scale. Loving and devoted, but also firebatshit crazy. Ready to do anything to get her man and snuff out the competition, including... actually snuffing them out."),
                        "masochist2" : Personality(name="masochist", attributes=("very lewd", "very sub"), description="The lower the better. She likes to be at the bottom and enjoys all sorts of dirty things being imposed on her. Gifts and loving gestures annoy her, she doesn't deserve them."),
                        "stubborn" : Personality(name="stubborn", attributes=("very modest", "very dom"), description="Doesn't like people who don't share her principles and moral values, and doesn't like contradiction either. She's a lot of fun at parties, if you like parties that end with a tavern brawl."),
                    }

    reserved_personality_names = gpersonalities.keys()

    gift_description = {
                        "cute" : "cute things",
                        "book" : "books",
                        "precious" : "precious things",
                        "erotica" : "erotic things",
                        "drinks" : "hard liquor"
                    }


    gpersonalities_comment = {
                            "very extravert pos" : ("She's friendly.", "She's always ready to help.", "She's fun.", "She's lively."),
                            "very introvert pos" : ("She's nice.", "She's quiet.", "She doesn't gossip.", "She's soft-spoken."),
                            "very idealist pos" : ("She follows her dreams.", "She's smart.", "She knows a lot about everything.", "She's very clever."),
                            "very materialist pos" : ("She's down-to-earth", "She likes the finer things in life.", "She's ambitious.", "She has great taste."),
                            "very lewd pos" : ("She's open-minded.", "She's curious", "She knows how to party.", "She's a real party-girl."),
                            "very modest pos" : ("She's rational.", "She keeps her head cool.", "She's stable.", "She's pure."),
                            "very dom pos" : ("She's so confident.", "She's driven.", "She's very independent.", "She's fearless."),
                            "very sub pos" : ("She's humble.", "She's quiet.", "She's loyal.", "She's obedient."),

                            "very extravert neg" : ("She's self-absorbed.", "She's loud.", "She's self-centered.", "She won't shut up."),
                            "very introvert neg" : ("She's no fun.", "She's aloof.", "She's unfriendly.", "She's a bore."),
                            "very idealist neg" : ("She's nerdy.", "She's a snowflake.", "She's a snob.", "She's a nerd."),
                            "very materialist neg" : ("She's a nasty bitch.", "She's so superficial.", "She's selfish.", "She's a cold-hearted bitch."),
                            "very lewd neg" : ("She's a perv.", "She's depraved, even for a whore.", "She has no morals.", "She's a slut."),
                            "very modest neg" : ("She's boring.", "She thinks she's better than us.", "She's prissy.", "She's intolerant."),
                            "very dom neg" : ("She's arrogant.", "She's over-confident.", "She's a bully.", "She's manipulative."),
                            "very sub neg" : ("She's a pushover.", "She whines too much.", "She's a crybaby.", "She's a loser."),
                        }

    recent_event_templates = {  # Girl events given to the player for rewarding/punishing

                            # Rewardable events
                            "level up" : GirlRecentEvent(type="level up", action="Earning some experience", base_description="She has become more experienced ({color=[c_emerald]}level %s{/color}).", discipline=False),
                            "rank up" : GirlRecentEvent(type="rank up", action="Earned a new rank", base_description="She has reached {color=[c_emerald]}rank %s{/color}.", discipline=False),
                            "job up" : GirlRecentEvent(type="job up", action="Increasing her job skill", base_description="She has increased her {color=[c_emerald]}%s{/color} skills.", discipline=False),
                            "good result" : GirlRecentEvent(type="good result", action="Performing well while working", base_description="Her performance was {color=[c_emerald]}%s{/color} while working (%s).", discipline=False),
                            "quest good result" : GirlRecentEvent(type="quest good result", action="Performing well on a quest", base_description="%s", discipline=False),
                            "class good result" : GirlRecentEvent(type="class good result", action="Studying hard", base_description="%s", discipline=False),
                            "new act" : GirlRecentEvent(type="new act", action="Trying something new", base_description="She {color=[c_emerald]}accepted %s training{/color} for the first time.", discipline=False),
                            "helped" : GirlRecentEvent(type="helped", action="Helping a friend", base_description="", discipline=False), # Not implemented


                            # Neutral events
                            "exhausted" : GirlRecentEvent(type="exhausted", action="Becoming exhausted", base_description="She pushed herself too hard and ended up {color=[c_crimson]}exhausted{/color}."),
                            "sick" : GirlRecentEvent(type="sick", action="Falling sick", base_description="She fell {color=[c_crimson]}sick{/color}."),
                            "hurt" : GirlRecentEvent(type="hurt", action="Getting hurt", base_description="She was {color=[c_crimson]}raped{/color} by %s."),
                            "defended" : GirlRecentEvent(type="defended", action="Fighting a customer", base_description="She {color=[c_emerald]}protected herself{/color} from a rapist customer."),


                            # Punishable events
                            "ran away" : GirlRecentEvent(type="ran away", action="Running away", base_description="She ran away, but you brought her back.", encourage=False),
                            "disobey" : GirlRecentEvent(type="disobey", action="Disobeying you", base_description="She {color=[c_crimson]}refused to work as a %s{/color}.", encourage=False),
                            "fooled around" : GirlRecentEvent(type="fooled around", action="Fooling around with customers", base_description="She {color=[c_crimson]}accepted %s with a customer against your wishes{/color}.", encourage=False),
                            "bad result" : GirlRecentEvent(type="bad result", action="Performing badly while working", base_description="She performed {color=[c_crimson]}%sly{/color} while working (%s).", encourage=False),
                            "quest bad result" : GirlRecentEvent(type="quest bad result", action="Performing badly on a quest", base_description="%s", encourage=False),
                            "class bad result" : GirlRecentEvent(type="class bad result", action="Not paying attention in school", base_description="%s", encourage=False),
                            "refused" : GirlRecentEvent(type="refused", action="Refusing training", base_description="She {color=[c_crimson]}refused to train (%s){/color}.", encourage=False),
                            "argued" : GirlRecentEvent(type="argued", action="Arguing with a rival", base_description="", encourage=False), # Not implemented

                            # Passive events (cannot be punished or rewarded=)
                            "acquired" : GirlRecentEvent(type="acquired", base_description="You have acquired %s.", encourage=False, discipline=False),
                            "MC met" : GirlRecentEvent(type="MC met", base_description="You have met %s.", encourage=False, discipline=False),
                            "MC friend" : GirlRecentEvent(type="MC friend", base_description="You and %s have become friends.", encourage=False, discipline=False),
                            "MC flower" : GirlRecentEvent(type="MC flower", base_description="You may now give %s flowers.", encourage=False, discipline=False),
                            "MC girlfriend" : GirlRecentEvent(type="MC friend", base_description="%s is now your girlfriend.", encourage=False, discipline=False),
                            "MC lover" : GirlRecentEvent(type="MC friend", base_description="%s is now your lover.", encourage=False, discipline=False),
                            "MC job" : GirlRecentEvent(type="MC job", base_description="You can now offer %s a job.", encourage=False, discipline=False),
                            "kidnapped" : GirlRecentEvent(type="kidnapped", base_description="She has been kidnapped by %s.", encourage=False, discipline=False),
                        }

    event_sounds = {
                    "perk 0" : s_surprise,
                    "perk 1" : s_ahaa,
                    "perk 2" : s_aaah,
                    "perk 3" : s_mmmh,
                    }



    base_reluctance = {"naked" : -375, "service" : -500, "sex" : -500, "anal" : -750, "fetish" : -750, "bisexual" : -750, "group" : -1000}

    # preference_modifier multiplies with negative base_reluctance so the +/- sign is reversed
    preference_modifier =   {
                            "refuses" : 150, # preference <= 90% base_reluctance
#                            "extremely reluctant" : 100, # (obsolete)
                            "very reluctant" : 75, # preference <= 70% base_reluctance
                            "reluctant" : 50, # preference <= 50% base_reluctance
                            "a little reluctant" : 25, # preference <= 20% base_reluctance
                            "indifferent" : 0, # preference <= -20% base_reluctance
                            "a little interested" : -5, # preference = -50% base_reluctance
                            "interested" : -15, # preference <= -70% base_reluctance
                            "very interested" : -35, # preference <= -90% base_reluctance
                            "fascinated" : -75 # preference > -90% base_reluctance
                        }

    # Reminder: Base reluctance is negative

    preference_limit =  {
                            "refuses" : 3.0, # preference <= 90% base_reluctance
                            "very reluctant" : 0.9, # preference <= 70% base_reluctance
                            "reluctant" : 0.7, # preference <= 50% base_reluctance
                            "a little reluctant" : 0.5, # preference <= 20% base_reluctance
                            "indifferent" : 0.2, # preference <= -20% base_reluctance
                            "a little interested" : -0.2, # preference = -50% base_reluctance
                            "interested" : -0.5, # preference <= -70% base_reluctance
                            "very interested" : -0.7, # preference <= -90% base_reluctance
                            "fascinated" : -0.9 # preference > -90% base_reluctance
                        }

    experienced_description = {
                            "very experienced" : "Extensive",
                            "experienced" : "Advanced",
                            "average" : "Some",
                            "inexperienced" : "Basic",
                            "very inexperienced" : "None",
                            "very experienced ttip" : "{size=-1}{color=[c_orange]}A sex slave for years, she has known several masters and received extensive sexual training.{/color}",
                            "experienced ttip" : "{size=-1}{color=[c_green]}She has been a sex slave for many months now, and has received various forms of training.{/color}",
                            "average ttip" : "{size=-1}{color=[c_yellow]}She has been a sex slave for a few months already, and has received some sexual training.{/color}",
                            "inexperienced ttip" : "{color=[c_lightred]}She became a sex slave only recently, and still has a lot to learn.{/color}",
                            "very inexperienced ttip" : "{color=[c_red]}Fresh off the slave caravan, she has never been trained for sex. Who knows how she will react?{/color}",
                        }

    experienced_modifiers = {
                            "very experienced" : [250, 150, 75],
                            "experienced" : [150, 75, 25],
                            "average" : [75, 25, 0],
                            "inexperienced" : [25, 0, -25],
                            "very inexperienced" : [0, 0, -50],
                        }

    experienced_color = {
                            "very experienced" : c_orange,
                            "experienced" : c_green,
                            "average" : c_yellow,
                            "inexperienced" : c_lightred,
                            "very inexperienced" : c_red,
                        }

    sexual_training_value = {
                            "very experienced" : 1,
                            "experienced" : 2,
                            "average" : 3,
                            "inexperienced" : 4,
                            "very inexperienced" : 5,
                        }

    long_act_description = {
                            "naked" : "being naked",
                            "service" : "giving service",
                            "sex" : "having sex",
                            "anal" : "anal sex",
                            "fetish" : "kinky sex",
                            "bisexual" : "sex with a woman",
                            "group" : "group sex",
                            "action naked" : "Nudity",
                            "action service" : "Service",
                            "action sex" : "Sex",
                            "action anal" : "Anal sex",
                            "action fetish" : "Fetish",
                            "action bisexual" : "Lesbian sex",
                            "action group" : "Group sex"
                        }

    # This filters choices for the training menu (OR clause)

    training_test_dict = {
                            "naked": [],
                            "service": [("naked", "reluctant"), ("service", "reluctant")],
                            "sex": [("naked", "indifferent"), ("service", "indifferent"), ("sex", "reluctant")],
                            "anal": [("sex", "indifferent"), ("anal", "reluctant")],
                            "fetish": [("anal", "indifferent"), ("service", "interested"), ("fetish", "reluctant")],
                            "fetish": [("anal", "indifferent"), ("service", "interested"), ("fetish", "reluctant")],
                            "bisexual": [("sex", "interested"), ("service", "interested"), ("bisexual", "indifferent")],
                            "group": [("anal", "interested"), ("sex", "fascinated"), ("group", "indifferent")],
                        }

    magic_training_test_dict = { # Suggestion training is easier
                            "naked": [],
                            "service": [],
                            "sex": [("naked", "reluctant"), ("service", "reluctant"), ("sex", "very reluctant")],
                            "anal": [("sex", "reluctant"), ("anal", "very reluctant")],
                            "fetish": [("anal", "reluctant"), ("service", "indifferent"), ("fetish", "very reluctant")],
                            "fetish": [("anal", "reluctant"), ("service", "indifferent"), ("fetish", "very reluctant")],
                            "bisexual": [("sex", "indifferent"), ("service", "indifferent"), ("bisexual", "reluctant")],
                            "group": [("anal", "a little interested"), ("sex", "very interested"), ("group", "a little reluctant")],
                        }

    ## MC interactions
    # The dictionary uses nested lists to retain choices order

    interact_dict = {
                    "chat" : ["GENERAL TOPICS", "PERSONAL TOPICS", "STORY"],
                    "GENERAL TOPICS" : [GirlInteractionTopic("chat", "chat", "Life as a slave", "slave_chat_slave_life"),
                                        GirlInteractionTopic("chat", "chat", "Life in the brothel", "slave_chat_brothel", condition="has_worked"),
                                        GirlInteractionTopic("chat", "chat", "Getting along with customers", "slave_chat_customers", condition="has_worked"),
                                        GirlInteractionTopic("chat", "chat", "Getting along with other girls", "slave_chat_other_girls", condition="other_girls"),
                                        ],
                    "PERSONAL TOPICS" : [
                                        GirlInteractionTopic("chat", "chat", "Her well-being", "slave_chat_well_being"),
                                        GirlInteractionTopic("chat", "chat", "Her feelings about you", "slave_chat_feelings"),
                                        GirlInteractionTopic("chat", "chat", "Her tastes", "slave_chat_tastes"),
                                        GirlInteractionTopic("chat", "chat", "Her origins", "slave_chat_origins"),
                                    ],
                    "STORY" : [GirlInteractionTopic("chat", "story", "Hear her story again", "slave_chat_story", AP_cost=0, condition = "story")],

                    "train" : ["SKILL TRAINING", "SEXUAL TRAINING", "SPECIAL TRAINING"],
                    "SKILL TRAINING" : [GirlInteractionTopic("train", "train", "Obedience training", "slave_train_obedience", act="obedience"),
                                        GirlInteractionTopic("train", "train", "Constitution training", "slave_train_constitution", act="constitution")],
                    "SEXUAL TRAINING" : [
                                        GirlInteractionTopic("train", "train", "Naked", "slave_train_sex_acts", act="naked", advanced=True),
                                        GirlInteractionTopic("train", "train", "Service", "slave_train_sex_acts", act="service", advanced=True),
                                        GirlInteractionTopic("train", "train", "Sex", "slave_train_sex_acts", act="sex", advanced=True),
                                        GirlInteractionTopic("train", "train", "Anal", "slave_train_sex_acts", act="anal", advanced=True),
                                        GirlInteractionTopic("train", "train", "Fetish", "slave_train_sex_acts", act="fetish", advanced=True),
                                        GirlInteractionTopic("train", "train", "Bisexual", "slave_train_sex_acts", act="bisexual", advanced=True),
                                        GirlInteractionTopic("train", "train", "Group", "slave_train_sex_acts", act="group", advanced=True),
                                    ],
                    "SPECIAL TRAINING" : [GirlInteractionTopic("train", "train", "Free-form training", "slave_train_free_form", condition = "free-form"),
                                          GirlInteractionTopic("train", "train", "Remove negative fixation", "slave_remove_fixation", condition="neg_fix")],

                    "magic" : ["MAGIC SKILL TRAINING", "MAGIC SEXUAL TRAINING", "CHOOSE METHOD"],
                    "CHOOSE METHOD" : [GirlInteractionTopic("magic", None, "Current method", "slave_hypnotize_method", AP_cost=0)], # None type excludes it from girl interaction count
                    "MAGIC SKILL TRAINING" : [
                                                GirlInteractionTopic("magic", "train", "Obedience training", "slave_magic", act="obedience", gold_cost=20),
                                                GirlInteractionTopic("magic", "train", "Sensitivity training", "slave_magic", act="sensitivity", gold_cost=20),
                                                GirlInteractionTopic("magic", "train", "Libido training", "slave_magic", act="libido", gold_cost=20),
                                                ],
                    "MAGIC SEXUAL TRAINING" : [
                                                GirlInteractionTopic("magic", "train", "Naked", "slave_magic", act="naked", advanced=True, gold_cost=20),
                                                GirlInteractionTopic("magic", "train", "Service", "slave_magic", act="service", advanced=True, gold_cost=40),
                                                GirlInteractionTopic("magic", "train", "Sex", "slave_magic", act="sex", advanced=True, gold_cost=50),
                                                GirlInteractionTopic("magic", "train", "Anal", "slave_magic", act="anal", advanced=True, gold_cost=60),
                                                GirlInteractionTopic("magic", "train", "Fetish", "slave_magic", act="fetish", advanced=True, gold_cost=70),
                                                GirlInteractionTopic("magic", "train", "Bisexual", "slave_magic", act="bisexual", advanced=True, gold_cost=80),
                                                GirlInteractionTopic("magic", "train", "Group", "slave_magic", act="group", advanced=True, gold_cost=100),
                                                ],

                    "react" : ["ENCOURAGE", "DISCIPLINE"],
                    "ENCOURAGE" : [
                                    GirlInteractionTopic("react", "reward", "Praise her", "slave_reward_praise"),
                                    GirlInteractionTopic("react", "reward", "Give her gold", "slave_reward_gold"),
                                    GirlInteractionTopic("react", "reward", "Give her a gift", "slave_reward_gift"),
                                    GirlInteractionTopic("react", "reward", "Pet her", "slave_reward_pet"),
                                    GirlInteractionTopic("react", "reward", "Give her a day off", "slave_reward_day"),
                                    GirlInteractionTopic("react", "reward", "Have sex with her", "slave_reward_sex"),
                                    ],
                    "DISCIPLINE" : [
                                    GirlInteractionTopic("react", "discipline", "Scold her", "slave_punish_scold"),
                                    GirlInteractionTopic("react", "discipline", "Remove upkeep", "slave_punish_upkeep"),
                                    GirlInteractionTopic("react", "discipline", "Force her to go naked", "slave_punish_naked"),
                                    GirlInteractionTopic("react", "discipline", "Beat her", "slave_punish_beat"),
                                    GirlInteractionTopic("react", "discipline", "Rape her", "slave_punish_rape"),
                                    GirlInteractionTopic("react", "discipline", "Send her to the farm", "slave_punish_farm", condition="farm"),
                                    ],
                    "misc" : ["CLOTHING", "CUSTOMERS", "MASTER BEDROOM", "DEBUG"],
                    "CLOTHING" : [
                                    GirlInteractionTopic("misc", None, "Tell her to go naked", "slave_clothing_naked", AP_cost=0, condition = "dressed"),
                                    GirlInteractionTopic("misc", None, "Tell her to get dressed", "slave_clothing_dressed", AP_cost=0, condition = "naked"),
                                    ],
                    "CUSTOMERS" : [
                                    GirlInteractionTopic("misc", None, "Forbid sex acts during job", "slave_forbid_cust_events", AP_cost=0, condition = "!forbid customer sex"),
                                    GirlInteractionTopic("misc", None, "Allow sex acts during job", "slave_allow_cust_events", AP_cost=0, condition = "forbid customer sex"),
                                    ],
                    "MASTER BEDROOM" : [
                                        GirlInteractionTopic("misc", None, "Send her to your bedroom", "slave_master_bedroom_add", AP_cost=0, condition = "master_bedroom_add"),
                                        GirlInteractionTopic("misc", None, "Remove her from your bedroom", "slave_master_bedroom_remove", AP_cost=0, condition = "master_bedroom_remove")
                                        ],
                    "DEBUG" : [GirlInteractionTopic("misc", None, "Cheat", "interaction_cheat_menu", AP_cost=0, condition="debug_mode"),
                        GirlInteractionTopic("misc", None, "Reset girl interactions", "interaction_cheat_girl", AP_cost=0, condition="debug_mode"),
                        GirlInteractionTopic("misc", None, "Reset MC interactions", "interaction_cheat_MC", AP_cost=0, condition="debug_mode"),
                        GirlInteractionTopic("misc", None, "Reveal Personality", "interaction_cheat_personality", AP_cost=0, condition="debug_mode"),
                        ],
                    }


    free_interact_dict = {
                            "chat" : ["GENERAL TOPICS", "PERSONAL TOPICS", "DEBUG"],
                            "GENERAL TOPICS" : [GirlInteractionTopic("chat", "chat", "Small talk", "free_chat_small_talk"),
                                                GirlInteractionTopic("chat", "chat", "Gossip", "free_chat_gossip"),
                                                GirlInteractionTopic("chat", "chat", "Life", "free_chat_life"),# love_test=5),
                                                GirlInteractionTopic("chat", "chat", "Love", "free_chat_love"),# love_test=5),
                                                ],
                            "PERSONAL TOPICS" : [
                                                GirlInteractionTopic("chat", "chat", "Her origins", "free_chat_origins", love_test=10),
                                                GirlInteractionTopic("chat", "chat", "Her hobbies", "free_chat_hobbies", love_test=10),
                                                GirlInteractionTopic("chat", "chat", "Likes", "free_chat_likes", love_test=10),
                                                GirlInteractionTopic("chat", "chat", "Dislikes", "free_chat_dislikes", love_test=10),
                                                ],
                            "fun" : ["JOKE", "TOUCH", "PLAY"],
                            "JOKE" : [
                                        GirlInteractionTopic("fun", "joke", "Harmless", "free_joke_harmless", love_test=15),
                                        GirlInteractionTopic("fun", "joke", "Adult", "free_joke_adult", love_test=15),
                                        GirlInteractionTopic("fun", "joke", "Dark", "free_joke_dark", love_test=15),
                                        GirlInteractionTopic("fun", "joke", "Mean", "free_joke_mean", love_test=15),
                                        ],
                            "TOUCH" : [
                                        GirlInteractionTopic("fun", "touch", "Hold her hand", "free_touch_hand", love_test=40),
                                        GirlInteractionTopic("fun", "touch", "Kiss", "free_touch_kiss", relationship_level=2),
                                        GirlInteractionTopic("fun", "touch", "Slap her ass", "free_touch_ass", love_test=55, relationship_level=3),
                                        GirlInteractionTopic("fun", "touch", "Touch her breasts", "free_touch_breasts", love_test=60, relationship_level=3),
                                        GirlInteractionTopic("fun", "touch", "Touch her pussy", "free_touch_pussy", love_test=65, relationship_level=3),
                                        ],
                            "PLAY" : [
                                        GirlInteractionTopic("fun", "play", "Get her naked", "free_play", act="naked", relationship_level=4),
                                        GirlInteractionTopic("fun", "play", "Ask for service", "free_play", act="service", relationship_level=4),
                                        GirlInteractionTopic("fun", "play", "Ask for sex", "free_play", act="sex", relationship_level=4),
                                        GirlInteractionTopic("fun", "play", "Ask for anal sex", "free_play", act="anal", relationship_level=4),
                                        GirlInteractionTopic("fun", "play", "Ask for fetish", "free_play", act="fetish", relationship_level=4),
                                        ],
                            "flirt" : ["COMPLIMENT", "SEXUAL TOPICS"],

                            "COMPLIMENT" : [
                                        GirlInteractionTopic("flirt", "compliment", "Compliment her beauty", "free_flirt_beauty", relationship_level=1),
                                        GirlInteractionTopic("flirt", "compliment", "Compliment her body", "free_flirt_body", relationship_level=1),
                                        GirlInteractionTopic("flirt", "compliment", "Compliment her mind", "free_flirt_mind", relationship_level=1),
                                        GirlInteractionTopic("flirt", "compliment", "Compliment her spirit", "free_flirt_spirit", relationship_level=1),
                                        ],
                            "SEXUAL TOPICS" : [
                                                GirlInteractionTopic("flirt", "chat about sex", "Her sexual experience", "free_flirt_sex_experience", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Her sexual tastes", "free_flirt_sex_tastes", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Nudity", "free_flirt_sex_act", act="naked", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Service", "free_flirt_sex_act", act="service", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Sex", "free_flirt_sex_act", act="sex", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Anal sex", "free_flirt_sex_act", act="anal", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Fetish acts", "free_flirt_sex_act", act="fetish", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Bisexuality", "free_flirt_sex_act", act="bisexual", love_test=55),
                                                GirlInteractionTopic("flirt", "chat about sex", "Group sex", "free_flirt_sex_act", act="group", love_test=55),
                                                ],
                            "give" : ["GIVE", "OFFER"],
                            "GIVE" : [
                                        GirlInteractionTopic("give", "gift", "Give her a present", "free_give_gift", love_test=20),
                                        GirlInteractionTopic("give", "gold", "Give her money", "free_give_gold", love_test=20),
                                        ],
                            "OFFER" : [GirlInteractionTopic("give", "offer", "Offer her a job", "free_offer_job", love_test=90, relationship_level=5),],
                            "DEBUG" : [GirlInteractionTopic("give", None, "Change love", "interaction_cheat_love", AP_cost=0, condition="debug_mode"),
                                        GirlInteractionTopic("give", None, "Reset girl interactions", "interaction_cheat_girl", AP_cost=0, condition="debug_mode"),
                                        GirlInteractionTopic("give", None, "Reset MC interactions", "interaction_cheat_MC", AP_cost=0, condition="debug_mode"),
                                        GirlInteractionTopic("give", None, "Reveal Personality", "interaction_cheat_personality", AP_cost=0, condition="debug_mode"),
                                        ],
                    }

    fix_description = {
                    "public acts description" : "doing it in public.",
                    "public acts action" : "Do it in public",
                    "public acts intro" : "You call in everyone from the brothel: girls, helpers, passersby... You tell %s that she must do it in public.",
                    "public acts pos_reaction" : "She blushes and you can see her nipples perking under her blouse. She is aroused by the thought of doing it in public.",
                    "public acts neg_reaction" : "She is indignant and complains that she can't do anything when people are watching. You ignore her.",

                    "cosplay description" : "wearing sexy and revealing outfits.",
                    "cosplay action" : "Wear a sexy outfit",
                    "cosplay intro" : "You give %s a choice of uniforms she can wear.",
                    "cosplay pos_reaction" : "She bites her lip, looking playful. She chooses a kinky uniform with holes for her tits, pussy and asshole.",
                    "cosplay neg_reaction" : "She chooses a rather conservative and boring uniform. She doesn't enjoy having to wear it.",

                    "dildos description" : "using sex toys while fucking.",
                    "dildos action" : "Use a dildo",
                    "dildos intro" : "You tell %s to use a dildo in her other hole while you're fucking her.",
                    "dildos pos_reaction" : "She easily slips the dildo in place. It looks like something she is used to doing a lot.",
                    "dildos neg_reaction" : "She hates it as she has to painfully force the dildo in. She doesn't enjoy it at all.",

                    "vibrators description" : "vibrators.",
                    "vibrators action" : "Use a vibrator",
                    "vibrators intro" : "You tell %s to use a vibrating egg while doing it.",
                    "vibrators pos_reaction" : "She wastes no time in using the egg on her ready clit, bringing herself to a state of heavy arousal.",
                    "vibrators neg_reaction" : "She is sensitive and uncomfortable using the egg, and complains that it feels weird.",

                    "dirty sex description" : "dirty sex",
                    "dirty sex action" : "Get down and dirty",
                    "dirty sex intro" : "You tell %s to get down in the dirt and get ready to be abused.",
                    "dirty sex pos_reaction" : "She seems happy to be on the ground, like a dirty bitch she is.",
                    "dirty sex neg_reaction" : "She hates dirt and complains that it is unhealthy.",

                    "penis worship description" : "worshiping dicks, especially large ones.",
                    "penis worship action" : "Make her rub your dick",
                    "penis worship intro" : "You tell %s that she has to rub oil on your dick and pay it proper respect.",
                    "penis worship pos_reaction" : "She takes a good look at your large, throbbing cock and seems happy and aroused that she can play with it. She plants a wet kiss right on the tip.",
                    "penis worship neg_reaction" : "She looks away from your erect dick, still uncomfortable around a man's cock.",

                    "bondage description" : "being tied up.",
                    "bondage action" : "Tie her up",
                    "bondage intro" : "Using tight ropes and your expert knowledge of bondage as a slave master, you tie %s up in an uncomfortable and embarrassing position.",
                    "bondage pos_reaction" : "She moans with pleasure as you tie her up, loving the feel of the ropes biting her skin.",
                    "bondage neg_reaction" : "She cries and squirms as you tie her up, feeling extremely uncomfortable.",

                    "oil description" : "being oiled-up.",
                    "oil action" : "Oil her up",
                    "oil intro" : "You give %s a bottle of body oil, insisting that she spreads it all over her naked body.",
                    "oil pos_reaction" : "She oils up every nook and cranny of her body for your pleasure, playfully massaging her glistening skin while you watch.",
                    "oil neg_reaction" : "She isn't comfortable with slippery and oily stuff, complaining that it stinks and feels revolting.",

                    "wet description" : "being wet.",
                    "wet action" : "Get her wet",
                    "wet intro" : "You ask Sill to fetch you a bucket of cold water, which you pour straight on %s's body.",
                    "wet pos_reaction" : "She loves being wet and moist, moaning as she slips her hands all over her body.",
                    "wet neg_reaction" : "She looks upset and miserable like a wet kitty. She hates water.",

                    "submission description" : "taking a humiliating pose.",
                    "submission action" : "Humiliate her",
                    "submission intro" : "You tell %s to get on her knees and beg for what's going to happen.",
                    "submission pos_reaction" : "She eagerly obeys your order, taking perverse pleasure in begging for you to abuse her.",
                    "submission neg_reaction" : "She refuses to beg and complains that it is beneath her.",

                    "femdom description" : "dominating her partner.",
                    "femdom action" : "Let her dominate",
                    "femdom intro" : "You tell %s to take the lead and dominate this encounter.",
                    "femdom pos_reaction" : "She is pleased to be given the leading role. She perversely enjoys giving orders and dominating her partner.",
                    "femdom neg_reaction" : "She hesitates, then awkwardly tries to give an order in an unconvincing voice. She almost immediately reverses herself and apologises. She doesn't enjoy taking the lead at all.",

                    "gags description" : "being gagged while having sex.",
                    "gags action" : "Gag her",
                    "gags intro" : "You order %s to wear a large ball gag, which leaves her mouth open at all times and makes it hard to talk.",
                    "gags pos_reaction" : "She seems oddly happy and excited as she puts on the gag and gives you a sheepish look.",
                    "gags neg_reaction" : "Unable to control her drooling and hardly able to talk, she gives you a furious look. She seems to hate it.",

                    "strap-ons description" : "fucking girls with a strap-on.",
                    "strap-ons action" : "Use a strap-on",
                    "strap-ons intro" : "You tell %s to fuck Sill using a strap-on dildo.",
                    "strap-ons pos_reaction" : "She looks triumphant as she puts on a huge black strap-on dildo, with one end up in her pussy and the other dangling in front of her. Sill gasps.",
                    "strap-ons neg_reaction" : "She grumbles as she puts it on, complaining that she isn't a man.",

                    "roleplay description" : "playing a role while fucking.",
                    "roleplay action" : "Make her play a role",
                    "roleplay intro" : "You tell %s that you are going to play roles: you are the city guard and she is a captured thief.",
                    "roleplay pos_reaction" : "She enjoys the idea of role-playing and makes a great show of being a repentant horny thief.",
                    "roleplay neg_reaction" : "She thinks it's stupid and distracting and doesn't get into it at all.",

                    "plugs description" : "wearing a plug inside her ass.",
                    "plugs action" : "Use anal plug",
                    "plugs intro" : "Taking out a large, glistening rubber plug, you tell %s to insert it in her ass.",
                    "plugs pos_reaction" : "She pushes the plug deep inside her ready asshole with delight, moaning seductively.",
                    "plugs neg_reaction" : "She inserts the plug with great difficulty, ashamed and in pain. It makes her very uncomfortable.",

                    "enemas description" : "getting an enema.",
                    "enemas action" : "Use an enema",
                    "enemas intro" : "You tell %s it's time to clean up.",
                    "enemas pos_reaction" : "As you insert the enema into her asshole and start filling her up with water, she begs you to go further and further. Soon, her belly is inflated and rounded like a balloon.",
                    "enemas neg_reaction" : "She cries with shame and horror as you fill her insides with cleansing water. She begs you to stop.",

                    "beads description" : "wearing anal beads.",
                    "beads action" : "Use anal beads",
                    "beads intro" : "You give %s a bead necklace and explain what she should do with it.",
                    "beads pos_reaction" : "She pushes the beads into her asshole one by one, clearly enjoying it and moaning as you watch.",
                    "beads neg_reaction" : "She cringes and whines as she painfully pushes one or two beads inside her ass. She tells you she hates it.",

                    "masturbation description" : "masturbating.",
                    "masturbation action" : "Make her masturbate",
                    "masturbation intro" : "You tell %s to play with herself while doing it.",
                    "masturbation pos_reaction" : "She enthusiastically starts playing with her clit and fingering her pussy while you watch her.",
                    "masturbation neg_reaction" : "She pretends to masturbate but isn't doing anything. She doesn't enjoy it at all.",

                    "fingering description" : "being fingered.",
                    "fingering action" : "Slide a finger inside her",
                    "fingering intro" : "You tell %s you will put your fingers inside her.",
                    "fingering pos_reaction" : "Her pussy welcomes you as you slide, one, then two, then three fingers inside her with ease. She moans with pleasure as you increase your pace, covering your fingers with her love juices.",
                    "fingering neg_reaction" : "Her pussy contracts and resists you as you push a single finger inside with great difficulty. Tears run down her face: she isn't enjoying this at all.",

                    "handjobs description" : "giving handjobs.",
                    "handjobs action" : "Give a handjob",
                    "handjobs intro" : "You order %s to give you a good handjob.",
                    "handjobs pos_reaction" : "She loves rubbing her hands up and down your dick, watching your throbbing, hard cock with fascination.",
                    "handjobs neg_reaction" : "She is mechanical and unenthusiastic. She doesn't like handjobs.",

                    "cunnilingus description" : "cunnilingus.",
                    "cunnilingus action" : "Cunnilingus",
                    "cunnilingus intro" : "You go down between %s's legs and spread her pussy lips.",
                    "cunnilingus pos_reaction" : "She moans wildly as you move your tongue deep inside her. Her love juices splash out, betraying her pleasure.",
                    "cunnilingus neg_reaction" : "She frowns and tries to close her legs, not feeling it. It seems like cunnilingus is not her thing.",

                    "oral description" : "giving oral.",
                    "oral action" : "Oral sex",
                    "oral intro" : "You tell %s to use her tongue and mouth to increase the pleasure.",
                    "oral pos_reaction" : "She loves licking and sucking her partner, and she makes sure to make eye contact with you as she does it.",
                    "oral neg_reaction" : "She gags at the taste and looks annoyed. She doesn't like giving oral.",

                    "irrumatio description" : "irrumatio.",
                    "irrumatio action" : "Irrumatio",
                    "irrumatio intro" : "Ordering %s to lay flat with her head hanging from the bed, you decide to fuck her mouth hard.",
                    "irrumatio pos_reaction" : "You shove your dick as deep and hard as you can into her mouth-pussy, and she takes it all in, seemingly enjoying having her throat raped.",
                    "irrumatio neg_reaction" : "She gags and coughs and cries and squirms, hating it, but you force-fuck her throat anyway.",

                    "deep throat description" : "deep throat.",
                    "deep throat action" : "Deep-throat",
                    "deep throat intro" : "You tell %s to get ready to deep-throat you.",
                    "deep throat pos_reaction" : "She has no gag reflexes and enjoys sucking your dick as far down her throat as she can.",
                    "deep throat neg_reaction" : "She gags and almost throws up, begging you to stop. You ignore her.",

                    "titjobs description" : "giving titjobs.",
                    "titjobs action" : "Give a titjob",
                    "titjobs intro" : "You order %s to use her tits to pleasure you.",
                    "titjobs pos_reaction" : "She wraps your dick completely between her gorgeous tits, licking the tip as she slides her soft mounds up and down your cock.",
                    "titjobs neg_reaction" : "She awkwardly tries to use her tits to rub your dick, but she is clumsy and uninterested.",

                    "footjobs description" : "giving footjobs.",
                    "footjobs action" : "Give a foot job",
                    "footjobs intro" : "You order %s to use her legs and feet to rub your dick.",
                    "footjobs pos_reaction" : "She loves playing with your dick with her feet, giving you a good upskirt view as she brings you to your limit.",
                    "footjobs neg_reaction" : "She hates it, only managing to crush your cock with her clumsy feet. You tell her to stop.",

                    "double penetration description" : "being fucked in both holes.",
                    "double penetration action" : "Double penetration",
                    "double penetration intro" : "You ask one of your security guys to join you and %s, telling him to fuck her ass as you take the front.",
                    "double penetration pos_reaction" : "She screams wildly as she gets both her front and back holes raped by fat dicks. She loves it.",
                    "double penetration neg_reaction" : "She is upset and bothered that two dicks are in her at the same time. It seems to be too much for her.",

                    "fisting description" : "being fisted.",
                    "fisting action" : "Fist her",
                    "fisting intro" : "Telling %s not to move, you decide to play around with her pussy using your bare fist.",
                    "fisting pos_reaction" : "She squeals with pleasure as you rape her wet pussy with your fist, eventually sending her into a massive squirting orgasm.",
                    "fisting neg_reaction" : "She screams with pain and begs you to stop as your fist bends her pussy in unnatural ways. She hates it.",

                    "insults description" : "being insulted.",
                    "insults action" : "Insult her",
                    "insults intro" : "You call %s names as you force her to perform, using language that would make a harbor whore blush.",
                    "insults pos_reaction" : "She seems to love being trashed and insulted, and after only a minute, you notice that she has got completely wet.",
                    "insults neg_reaction" : "She is shocked and unnerved by your words, unable to concentrate on what she's doing. It isn't helping.",

                    "69 description" : "69.",
                    "69 action" : "Do a 69",
                    "69 intro" : "You tell %s to get into a 69 position.",
                    "69 pos_reaction" : "She loves 69 and enjoys herself tremendously as she tends to her partner while her pussy gets licks.",
                    "69 neg_reaction" : "She looks unhappy as she seems to despise that position. In the end, it isn't enjoyable for anyone.",

                    "watersports description" : "watersports.",
                    "watersports action" : "Play watersports",
                    "watersports intro" : "You tell %s to get ready for some 'watersports'.",
                    "watersports pos_reaction" : "She loves peeing in front of people and being peed on. She doesn't find it shameful.",
                    "watersports neg_reaction" : "She is disgusted by bodily fluids and recoils with horror at the thought.",

                    "ass-to-mouth description" : "ass-to-mouth.",
                    "ass-to-mouth action" : "Go ass-to-mouth",
                    "ass-to-mouth intro" : "You decide to fuck %s in the ass before moving to her mouth.",
                    "ass-to-mouth pos_reaction" : "She accepts your dick readily and licks it clean for you, not caring that it was in her ass a second ago.",
                    "ass-to-mouth neg_reaction" : "She retches as you push your dick into her mouth, complaining that it is dirty and disgusting.",

                    "kissing description" : "kissing.",
                    "kissing action" : "Kiss her",
                    "kissing intro" : "You start kissing %s.",
                    "kissing pos_reaction" : "She responds enthusiastically to your kiss, mingling her tongue with yours. She doesn't let go until the very end.",
                    "kissing neg_reaction" : "She tries to avoid you and doesn't seem to enjoy kissing at all. She is relieved when you stop.",

                    "spanking description" : "spanking.",
                    "spanking action" : "Spank her",
                    "spanking intro" : "You tell %s that she's been a bad girl, and that she is going to get spanked hard.",
                    "spanking pos_reaction" : "She screams with pain and pleasure, crying tears of happiness as you give her a thorough spanking while fucking her.",
                    "spanking neg_reaction" : "You spank her and fuck her at the same time. She wriggles and tries to escape you, moaning in pain. She doesn't like it.",

                    "rimming description" : "rimming.",
                    "rimming action" : "Rimming",
                    "rimming intro" : "You tell %s to lick your asshole thoroughly.",
                    "rimming pos_reaction" : "She is very serious about licking you clean, pushing her tongue into your ass as she gives you a frantic handjob.",
                    "rimming neg_reaction" : "She is disgusted by the act and only timidly licks around your asshole. It tickles, but doesn't feel good in any way.",

                    "fondling her boobs description" : "being fondled.",
                    "fondling her boobs action" : "Fondle her boobs",
                    "fondling her boobs intro" : "You fondle her tits and play with her nipples as %s performs for you.",
                    "fondling her boobs pos_reaction" : "She loves it when you squeeze her tits and moans sexily as you rub her erect nipples.",
                    "fondling her boobs neg_reaction" : "She doesn't like to be touched there and tenses up, making the training less enjoyable.",

                    "groping her ass description" : "being groped.",
                    "groping her ass action" : "Grope her ass",
                    "groping her ass intro" : "You grope her ass and start fingering her asshole as %s performs for you.",
                    "groping her ass pos_reaction" : "She loves to be touched and groped and moans hornily as you shove two fingers up her butthole.",
                    "groping her ass neg_reaction" : "She doesn't like to be touched there and tenses up, making the training less enjoyable.",

                    "lactation description" : "lactation.",
                    "lactation action" : "Milk her",
                    "lactation intro" : "Groping %s's boobs, you take out a syringe filled with a strange liquid and plunge it into her nipple.",
                    "lactation pos_reaction" : "She gasps with astonishment as her tits grow larger in size. Soon, she begins to lactate uncontrollably, moaning as you milk her large breasts for all they're worth.",
                    "lactation neg_reaction" : "She yells and cries with pain as her boobs grow heavier and larger. The experience is too traumatic, however, and she fails to give you any milk.",

                    "doggy style description" : "doggy style.",
                    "doggy style action" : "Doggy style",
                    "doggy style intro" : "Pushing her on all fours, you start fucking %s from behind.",
                    "doggy style pos_reaction" : "She moans with pleasure as the length of your shaft runs along her most sensitive parts. She cannot get enough of it.",
                    "doggy style neg_reaction" : "She grinds her teeth as she waits for you to be finished. She doesn't enjoy that position at all.",

                    "cowgirl description" : "cowgirl style.",
                    "cowgirl action" : "Cowgirl style",
                    "cowgirl intro" : "You make %s ride your dick.",
                    "cowgirl pos_reaction" : "She likes to be on top and lovingly bounces on your dick until you both get close to your limit.",
                    "cowgirl neg_reaction" : "She doesn't like to be on top and stays passive as you fuck her from below.",

                    "piledriver description" : "piledriver.",
                    "piledriver action" : "Piledriver",
                    "piledriver intro" : "Pushing %s on her back and lifting her legs in the air, you plunge your hard dick inside her.",
                    "piledriver pos_reaction" : "She is overwhelmed with lust and pleasure as the blood flows to her head while you pound her mercilessly.",
                    "piledriver neg_reaction" : "She is confused and bothered by this new position, telling you she doesn't like it at all.",

                    "spooning description" : "spooning.",
                    "spooning action" : "Spooning",
                    "spooning intro" : "Hugging %s from behind, you slowly slide into her while caressing her body.",
                    "spooning pos_reaction" : "She loves being cradled and fucked at the same time. She relaxes completely, moaning softly, soon ready to reach orgasm.",
                    "spooning neg_reaction" : "She stays passive as you fuck her from behind, looking bored.",

                    "bukkake description" : "bukkake.",
                    "bukkake action" : "Bukkake",
                    "bukkake intro" : "Calling a group of your security guards, you let them watch as you and Sill fuck %s. They start jerking off while watching her. As you reach your limit, you pull out and cum all over her face, quickly followed by the other men.",
                    "bukkake pos_reaction" : "She shakes with a massive orgasm as she experiences a shower of cum on her face, hair and body. She gorges up on leftover cum from everyone's dick.",
                    "bukkake neg_reaction" : "She tries to get away and whines as everyone cums on her face and hair. She bitterly complains about the smell and taste.",

                    "cum in mouth description" : "cum in her mouth.",
                    "cum in mouth action" : "Cum in her mouth",
                    "cum in mouth intro" : "You decide to use %s's mouth for a big finish.",
                    "cum in mouth pos_reaction" : "She looks entranced as you unload a wad of semen into her ready mouth. She plays with it on her tongue, enjoying the taste and texture.",
                    "cum in mouth neg_reaction" : "You cum a lot in her mouth, sending her into a fit of coughing. She spits it all out, complaining.",

                    "cum on face description" : "cumshots.",
                    "cum on face action" : "Cum on her face",
                    "cum on face intro" : "Popping your dick out, you shoot a load of semen all over %s's face.",
                    "cum on face pos_reaction" : "She sighs happily as she receives load after load of your cum. She uses her hands to spread the cum all over her face, then licks her fingers.",
                    "cum on face neg_reaction" : "She recoils with disgust as you shoot your load. She rushes to get a wet cloth and clean it up.",

                    "cum in hair description" : "cum in her hair.",
                    "cum in hair action" : "Cum in her hair",
                    "cum in hair intro" : "Popping your dick out, you decide to cum all over %s's soft, silky hair.",
                    "cum in hair pos_reaction" : "She moans as you wrap her hair around your dick and squeeze every last drop on her scalp. She enjoys being treated like a dirty cum dump.",
                    "cum in hair neg_reaction" : "She yells awfully as you shoot a load of semen on her hair, whining that it's gonna take ages to get it off.",

                    "cum on body description" : "cum on her body.",
                    "cum on body action" : "Cum on her body",
                    "cum on body intro" : "You decide to cum all over %s's body.",
                    "cum on body pos_reaction" : "She reaches her climax as you take out your dick and spill a load of white cum all over her soft skin.",
                    "cum on body neg_reaction" : "She squirms as you shoot cum all over her body, complaining that it is sticky and smelly.",

                    "cum shower description" : "getting showered with cum.",
                    "cum shower action" : "Shower her with cum",
                    "cum shower intro" : "Popping a special pill from the spice market, your dick starts bulging, ready to burst with huge amounts of cum. You tell %s to lay down and get ready to receive your seed.",
                    "cum shower pos_reaction" : "You cum and cum buckets, until she is covered with white, sticky semen. She is enthralled by the sensation.",
                    "cum shower neg_reaction" : "She squeals and cowers in fear as you cum buckets all over her body, disgusted by the smell and feel.",

                    "swallowing description" : "swallowing cum.",
                    "swallowing action" : "Make her swallow",
                    "swallowing intro" : "Shoving your dick deep into %s's mouth for the big finish, you shoot loads of cum deep down her throat.",
                    "swallowing pos_reaction" : "She gulps it all down with gusto, squeezing every last drop of cum out of your throbbing dick. She licks her lips sexily when you are finished.",
                    "swallowing neg_reaction" : "She gets tearful and gags, trying to spit it all out as you shoot load after load. She only partly succeeds, and looks unhappy at having to drink cum.",

                    "creampie description" : "receiving a creampie.",
                    "creampie action" : "Creampie",
                    "creampie intro" : "Taking your dick slowly out of %s, you shoot a thick load of white cum all over her ass and pussy.",
                    "creampie pos_reaction" : "She shakes with a massive orgasm as you spurt cum all over her holes. She seems to love it.",
                    "creampie neg_reaction" : "She covers her face and begs you to stop, saying that it's creepy and disgusting.",

                    "cum inside description" : "cum inside her.",
                    "cum inside action" : "Cum inside",
                    "cum inside intro" : "Not caring about the consequences, you decide to cum deep inside %s.",
                    "cum inside pos_reaction" : "She reaches a blinding orgasm, moaning wildly as you unload a wad of cum deep inside her.",
                    "cum inside neg_reaction" : "She screams for you to get out, but you ignore her, smearing her insides with thick, sticky cum. She cries with shame and disgust.",

                    "multiple orgasms description" : "having multiple orgasms.",
                    "multiple orgasms action" : "Give her multiple orgasms",
                    "multiple orgasms intro" : "Rubbing her clit with one hand, you keep the pace up until %s cannot but shake with a shattering orgasm. Giving her no moment to rest, you increase the build-up until she comes another time, and another time.",
                    "multiple orgasms pos_reaction" : "She loves it and loses her mind completely over the sensations washing over her, looking nothing but an obedient, adoring slave by the time you are finished.",
                    "multiple orgasms neg_reaction" : "She feels overtly sensitive and begs you to stop, almost in pain from excessive climaxing. She doesn't like it.",

                    "denied orgasm description" : "being denied orgasm.",
                    "denied orgasm action" : "Deny her orgasm",
                    "denied orgasm intro" : "You decide to tease %s to the limit, not letting her reach climax.",
                    "denied orgasm pos_reaction" : "She seems to love being teased and indefinitely denied orgasm, becoming incredibly horny and sensitive over time.",
                    "denied orgasm neg_reaction" : "She screams with frustration and begs you to let her climax. She is upset that you won't let her.",

                    "squirting description" : "squirting.",
                    "squirting action" : "Make her squirt",
                    "squirting intro" : "Pushing your hand inside %s's pussy, you start rubbing the walls of her pussy, looking for her sensitive G-spot. She looks overwhelmed by the sensation.",
                    "squirting pos_reaction" : "She squirts hard, showering the room with her juice. She climaxes so hard that she can't even move afterwards.",
                    "squirting neg_reaction" : "She feels weird and gross, and begs you to take your hand out. She isn't into it at all.",

                    "stripping description" : "stripping.",
                    "stripping action" : "Make her strip",
                    "stripping intro" : "Telling %s to remove her clothes slowly and sexily, you look on as she does what she's told.",
                    "stripping pos_reaction" : "She moans as she feels the caress of her clothing rubbing against her soft skin. Looking straight into your eyes, she slowly removes her underwear last, inch by inch, making sure to give you a good show.",
                    "stripping neg_reaction" : "Whining and bitching, she reluctantly takes off her clothes, hiding her private parts in embarrassment. She looks angry and shameful.",

                    }

    fix_dict = {
                "stripping" : Fixation("stripping", acts=("naked", "sex", "bisexual"), step=1, attribute="modest", tag_list=(["strip"], ["naked", "dancer"])),
                "public acts" : Fixation("public acts", acts=("naked", "service", "sex", "group"), step=1, attribute="extravert", tag_list=(["public"]), not_list=["rest"]), # Location tags are allowed but display special flavor text
                "cosplay" : Fixation("cosplay", acts=("naked", "fetish", "bisexual"), step=1, attribute="extravert", tag_list=(["cosplay"], ["maid", "kimono"], ["swim", "waitress", "dancer"]), not_list=["naked"], cannot_have_neg=["roleplay"]),
                "dildos" : Fixation("dildos", acts=("sex", "anal", "bisexual"), step=1, attribute="introvert", tag_list=(["dildo"], ["toy"],)),
                "vibrators" : Fixation("vibrators", acts=("naked", "fetish", "bisexual"), step=1, attribute="introvert", tag_list=(["vibrator"], ["toy"],)),
                "dirty sex" : Fixation("dirty sex", acts=("sex", "fetish", "group"), step=1, attribute="sub", tag_list=(["dirty"],)),
                "penis worship" : Fixation("penis worship", acts=("service", "group"), step=1, attribute="sub", tag_list=(["handjob", "big"], ["service", "big"], ["handjob"],), cannot_have_neg=["handjob"]),
                "bondage" : Fixation("bondage", acts=("fetish", "naked"), step=1, attribute="sub", tag_list=(["bondage"],)),
                "oil" : Fixation("oil", acts=("group", "anal"), step=1, attribute="extravert", tag_list=(["wet"],)),
                "wet" : Fixation("wet", acts=("naked", "sex", "bisexual"), step=1, attribute="extravert", tag_list=(["wet"],)),
                "submission" : Fixation("submission", acts=("service", "fetish", "bisexual"), step=1, attribute="sub", tag_list=(["sub"],)),
                "femdom" : Fixation("femdom", acts=("bisexual", "sex", "service"), step=1, attribute="dom", tag_list=(["dom"],)),
                "gags" : Fixation("gags", acts=("fetish", "naked"), step=1, attribute="introvert", tag_list=(["gag"], ["bondage"],)),
                "strap-ons" : Fixation("strap-ons", acts=("bisexual", "group"), step=1, attribute="dom", tag_list=(["strap-on"], ["lesbian"], ["toy"],)),
                "roleplay" : Fixation("roleplay", acts=("naked", "sex", "fetish"), step=1, attribute="extravert", tag_list=(["cosplay"], ["maid", "kimono"], ["swim", "waitress", "dancer"]), cannot_have_neg=["cosplay"]),
                "plugs" : Fixation("plugs", acts=("naked", "anal"), step=1, attribute="modest", tag_list=(["plug"], ["toy"],)),
                "enemas" : Fixation("enemas", acts=("group", "anal"), step=1, attribute="materialist", tag_list=(["enema"], ["toy"],)),
                "beads" : Fixation("beads", acts=("anal"), step=1, attribute="introvert", tag_list=(["beads"], ["toy"],)),

                "masturbation" : Fixation("masturbation", acts=("service", "naked", "sex"), step=2, attribute="extravert", tag_list=(["mast"], ["naked"],)),
                "fingering" : Fixation("fingering", acts=("naked", "fetish", "bisexual", "group"), step=2, attribute="lewd", tag_list=(["finger"],)),
                "handjobs" : Fixation("handjobs", acts=("service", "group"), step=2, attribute="modest", tag_list=(["handjob"],)),
                "cunnilingus" : Fixation("cunnilingus", acts=("service", "bisexual"), step=2, attribute="introvert", tag_list=(["cunnilingus"],["finger"])),
                "oral" : Fixation("oral", acts=("service", "bisexual", "group"), step=2, tag_list=(["oral"],)),
                "irrumatio" : Fixation("irrumatio", acts=("fetish"), step=2, attribute="sub", tag_list=(["deep"], ["oral"],)),
                "deep throat" : Fixation("deep throat", acts=("service", "group"), step=2, attribute="sub", tag_list=(["deep"], ["oral"],), cannot_have_neg=["oral"]),
                "titjobs" : Fixation("titjobs", acts=("service", "group"), step=2, attribute="extravert", tag_list=(["titjob"],)),
                "footjobs" : Fixation("footjobs", acts=("service", "fetish"), step=2, attribute="dom", tag_list=(["footjob"],)),
                "double penetration" : Fixation("double penetration", acts=("group"), step=2, attribute="lewd", tag_list=(["double"],)),
                "fisting" : Fixation("fisting", acts=("fetish", "bisexual", "anal"), step=2, attribute="lewd", tag_list=(["fist"], ["finger"])),
                "insults" : Fixation("insults", acts=("fetish", "naked"), step=2, attribute="sub", tag_list=(["sub"],)),
                "69" : Fixation("69", acts=("service", "bisexual"), step=2, attribute="dom", tag_list=(["69"], ["oral"],), cannot_have_neg=["oral"]),
                "watersports" : Fixation("watersports", acts=("fetish", "sex"), step=2, attribute="sub", tag_list=(["watersports"], ["squirt"],)),
                "ass-to-mouth" : Fixation("ass-to-mouth", acts=("anal", "group"), step=2, attribute="sub", tag_list=(["cim"], ["oral"],), cannot_have_neg=["oral"]),
                "kissing" : Fixation("kissing", acts=("naked", "sex", "bisexual"), step=2, attribute="idealist", tag_list=(["kiss"],)),
                "spanking" : Fixation("spanking", acts=("fetish", "anal"), step=2, attribute="sub", tag_list=(["spank"], ["sub"],)),
                "rimming" : Fixation("rimming", acts=("service", "fetish"), step=2, attribute="sub", tag_list=(["rim"],)),
                "fondling her boobs" : Fixation("fondling her boobs", short_name = "fondling", acts=("naked", "sex", "bisexual", "group"), step=2, tag_list=(["fondle"],)),
                "groping her ass" : Fixation("groping her ass", short_name = "groping", acts=("naked", "anal", "bisexual", "group"), step=2, tag_list=(["grope"],)),
                "lactation" : Fixation("lactation", acts=("naked", "fetish"), step=2, attribute="extravert", tag_list=(["lactation"], ["titjob"],)),
                "doggy style" : Fixation("doggy style", acts=("sex", "anal"), step=2, attribute="lewd", tag_list=(["doggy"],)),
                "cowgirl" : Fixation("cowgirl", acts=("sex", "anal"), step=2, attribute="dom", tag_list=(["cowgirl"],)),
                "piledriver" : Fixation("piledriver", acts=("sex", "anal"), step=2, attribute="materialist", tag_list=(["piledriver"],)),
                "spooning" : Fixation("spooning", acts=("sex", "anal"), step=2, attribute="idealist", tag_list=(["spoon"],)),

                "bukkake" : Fixation("bukkake", acts=("bisexual", "group"), step=3, attribute="lewd", tag_list=(["buk"], ["cof"], ["cumshot"],), cannot_have_neg=["cum shower"]),
                "cum in mouth" : Fixation("cum in mouth", acts=("service", "anal", "bisexual"), step=3, attribute="lewd", tag_list=(["cim"], ["oral"],), cannot_have_neg=["oral"]),
                "cum on face" : Fixation("cum on face", acts=("service", "sex", "fetish"), step=3, attribute="sub", tag_list=(["cof"], ["buk"], ["cumshot"],)),
                "cum in hair" : Fixation("cum in hair", acts=("service", "fetish"), step=3, attribute="sub", tag_list=(["cih", "coh"], ["cof", "buk"], ["cumshot"],)),
                "cum on body" : Fixation("cum on body", acts=("sex", "anal", "service"), step=3, attribute="dom", tag_list=(["cob"], ["cumshot"],)),
                "cum shower" : Fixation("cum shower", acts=("bisexual", "group"), step=3, attribute="sub", tag_list=(["cum shower"], ["cob", "cih"], ["cumshot"],), cannot_have_neg=["bukkake"]),
                "swallowing" : Fixation("swallowing", acts=("service", "fetish"), step=3, attribute="materialist", tag_list=(["cim"], ["deep"], ["oral"],), cannot_have_neg=["oral", "cum in mouth"]),
                "creampie" : Fixation("creampie", acts=("sex", "anal", "group"), step=3, attribute="extravert", tag_list=(["creampie"], ["cin"],)),
                "cum inside" : Fixation("cum inside", acts=("sex", "anal"), step=3, attribute="introvert", tag_list=(["cin"], ["creampie"],)),
                "multiple orgasms" : Fixation("multiple orgasms", acts=("group", "bisexual"), step=3, attribute="lewd", tag_list=(["orgasm"],)),
                "denied orgasm" : Fixation("denied orgasm", acts=("anal", "fetish", "bisexual"), step=3, attribute="sub", tag_list=(["denied"],)),
                "squirting" : Fixation("squirting", acts=("service", "sex", "bisexual"), step=3, attribute="extravert", tag_list=(["squirt"], ["watersport", "orgasm"],)),
                }


    ## PERKS AND ARCHETYPES ##
init -4 python:
    archetype_list = ["The Maid", "The Player", "The Model", "The Courtesan", "The Escort", "The Fox", "The Slut", "The Bride"]

    archetype_description = {
                            "The Maid" : "Holding her head up high even in adversity, the {b}Maid{/b} succeeds through hard work and commitment. She is the patron saint of servants and menial workers.",
                            "The Player" : "Always ready to tell a compelling story or improvise a lavish dance, the {b}Player{/b} is admired for her party skills and charisma. She is the patron saint of singers, actors and other artists, accomplished or aspiring.",
                            "The Model" : "Blessed with perfect natural beauty and elegance, if a little vain, the {b}Model{/b} fascinates men and women alike. She is the patron saint of the young, the pretty, and the well endowed.",
                            "The Courtesan" : "The {b}Courtesan{/b} is a master of etiquette, seduction and politics, able to make anyone give in to her every whim. She is the patron saint of noble women, politicians, and other schemers.",

                            "The Escort" : "Using her body and skills to great advantage, the {b}Escort{/b} is an expert at leveraging her talents for profits. She is the patron saint of fancy prostitutes, merchants, and mercenaries.",
                            "The Fox" : "A mysterious figure which seems to always show on auspicious occasions, the {b}Fox{/b} is said to bring great luck to everyone she shares her bed with. She is the patron saint of travellers and hermits.",
                            "The Slut" : "A much revered figure, the {b}Slut{/b} delights in experienceing sex and pleasure in all its forms, rejecting laws and morals that do not suit her. She is the patron saint of street girls, thieves, libertines, and the occasional Arios priest.",
                            "The Bride" : "A harbinger of peace and prosperity, the {b}Bride{/b} is gentle and devoted. She is the patron saint of coming-of-age virgins, pregnant and married women, and widows."
                        }

    ## GOSSIP ##

    generic_gossip = [
                        "I don't understand how the magicians can carry on their experiments in broad daylight. The church of Arios zealots hate magic-users with a passion. But they haven't moved to shut them down...",
                        "Taxes on rice, grain, vegetables, meat... Soon they'll tax water from the puddles! What's a man to eat?",
                        "Zan has been consumed by lust, greed and corruption for as long as I can remember, but seems these days we've reached new lows.",
                        "Not everyone in the Guard is a flat-out jerk. I know a guy who's all right. They are few and far between, though.",
                        "The royals sit all high and mighty far away from us people. They let the guards rob us blind but when a thief shows up, she never gets caught. Where's the justice in that?",
                        "You'd think the thieves would leave poor folks like us alone. But no sir, if you have nothing, they'll still pry it from your cold dead hands.",
                        "The guards steal so much from us poor folks that there's hardly anything left for the thieves.",
                        "*lowering her tone* Heard of Shalia, the dark goddess? They say she's got a temple in the slums, in this very city. It gives me the creeps.",
                        "There's a temple to Shalia somewhere in the city. I expect it's hard to find, though, her supporters rarely come out in the open.",
                        "Arios damn that Shalia bitch and her secret temple! A vile goddess like her has no place in this city. We're upstanding folks of the Light, are we not?",
                        "I heard Shalia is not at all what she's cracked up to be. You hear of sacrifices, virgin blood... That's nonsense. Her followers like secrecy, but they're into much more mundane things, such as lifting your purse.",
                        "Shalia followers eat little children's hearts for breakfast. That's what my Ma' said.",
                        "With all the crooked politicians and scheming thieves crawling in this city, you'd wonder why they didn't build a Cathedra to Shalia instead!",
                        "When he was little, my brother was always lonely, brooding, plotting revenge on the kids who bullied him. We used to joke that he was our own little Shalia apostle!",
                        "Shalia is a craven goddess, that's what she is. A proper god has his followers out in the open.",
                        "Some say Shalia's beauty itself is a weapon she uses in her schemes...",
                        "People are dumb enough to believe Arios is better because he is the god of light. But who wants light to be shone on all their thoughts and secrets? Shalia has just as important a role...",
                        "Someone told me he's seen a Shalia shrine in the slums. But he wouldn't tell me where it is.",
                        "Zan is full of dirty secrets and dark corners. One must watch their step - it's easy to anger the wrong person, and hard to gain anyone's trust.",
                        "There are three ways to make people in Zan part with their money: pussy, spice, or a sharp knife.",
                        "I've seen an incredible fight at the arena! Cyntia's a slave, but she's got style.",
                        "I can't believe people enjoy watching fights to the death in the arena. If you needed further proof this place is barbaric, there, you have it.",
                        "I don't care about the deaths in the arena. Most of the time it's just monsters and slaves. All in good fun!",
                        "People bet heavily on the arena fights. There's some good money to be had, if you know who to support.",
                        "Lots of adventurers try their luck in the arena. Many end up cripples or worse after just a few fights. But Cyntia's endured.",
                        "I don't watch the fights, too gory. I just bet on them. But lately, I've been out of luck.",
                        "Someone told me he had a trick so that he'd always win his bets in the arena. I didn't believe him at first, but he won five fights in a row!",
                        "The gladiators of the arena in their shining gold armor, covering themselves with glory and blood! Isn't that a tremendous sight?",
                        "The league of adventurers draws champions and scum alike from faraway lands. I wouldn't trust any of them, that's for sure.",
                        "If you want a quick way to make money, you could do worse than throw your lot with the league of adventurers. They always have some juicy bounties for enterprising individuals, and not all of them require drawing your sword.",
                        "The league of adventurers prefers to advance their goals by maneuvering rather than violence, but they've been known to use both.",
                        "There is no head of the league of adventurers. The intendant only deals with the paperwork, but all members are considered equals.",
                        "How can the league of adventurers be leader-less? There must be someone pulling their strings from the shadows.",
                        "I'm offended that some of those upstarts at the league of adventurers are getting so rich, when so many of our own true blue-blooded nobles are facing ruin.",
                        "The league of explorers is shunned by many of the nobles and courtiers because it takes commoners in, but they have started some of the most profitable enterprises in the city.",
                        "Ever heard of the brotherhood? They say they'll defend the common people against the nobles and high-borns. Such nonsense.",
                        "I've heard of a secret political organization called the Brotherhood. I have no idea who they are or what they do, but they're rumored to have enormous power in the city.",
                        "Some crazy jerk got my friend all worked up about 'sticking it to the royals', and 'taking back what's rightfully ours'. I begged my friend not to listen to such drivel, but now she's been arrested by the king's guard, and they suspect me as well...",
                        "Brother, you should not toil and suffer so that a few high-born loafers can hold banquets and orgies all day and all night. If you joined the brotherhood, you could put an end to this... But hush, someone's coming.",
                        "This woman claimed the brotherhood will rise to help the little people. But I know the truth of it: within a few months, they'd put themselves and their relatives in all the powerful positions, and they'd be no better than King Pharo.",
                        "King Pharo is our rightful leader chosen by the gods themselves. It is heresy to question the place of our betters: let us talk no more of that so-called 'brotherhood'.",
                        "Magicians are vermin who deserve nothing but ruin. They spoil our beloved city with their godless experiments. I wish the King had enough sense to make them all hang.",
                        "What's wrong with a little magic? It's not perversion, or a scam. People are afraid of things they don't understand, that's all. I dabble in magic myself, did you know? Here's an ointment you could buy for cheap...",
                        "Magicians have long been established in Zan without too much trouble. But their conflict with the church of Arios is starting to pull at the seams.",
                        "A priest of Arios himself told me that wizards consort with demons and plot Zan's ruin. Something must be done.",
                        "Those magicians are just rich, spoiled brats toying with forces they don't understand. I don't like those bigots from the Cathedra, but they have a point.",
                        "Heresy of not, the mages are contributing good money to our city's finances. If every questionable practice was banned in this city, there wouldn't be much left of Zan.",
                        "Monsters have been spotted in Zan. I myself saw a three-headed wolf raping a young girl in a dark alley. What has this city come to?",
                        "Sorcerers are responsible for the monsters plague in this city, who else? They should throw the lot of them in a dark cell with their pets, and throw away the key.",
                        "I don't buy it. Wizards have enough trouble as it is with the Light priests. Why would they release monsters in the streets and make their situation worse?",
                        "Monsters roam the streets at night. No one should stay out late these days, especially young, beautiful girls.",
                        "An entire patrol wiped out near the Gardens? This monster problem is getting out of hand!",
                        "The Cathedra is a nice enough looking building from outside, but you wouldn't like what goes on inside, believe me.",
                        "The High Priestess has advocated for the complete removal of magic from the city. She'll have her way; she always does.",
                        "I remember the times before the war, when the Grandmaster was heading the Arios cult... These were gentler days, I tell you.",
                        "Ever since the Grandmaster left for the Holy war, the High Priestess has been consolidating her power in the city. I don't think she wants him to come back.",
                        "Heard any news from the war in the Holy lands? They told me it's not going well. The heretics are resisting us at every step, but surely Arios won't let his flock down.",
                        "The Arios priests want to impose their cult on the rest of the city, plain and simple. Don't be fooled by the bitch priestesses' righteous sermons.",
                        "A friend of mine became a nun of Arios, but she had a change of heart and ran away a week ago. I don't know what happened.",
                        "I can't stand those upright do-gooders from the Arios church. I'm sure they're hiding something.",
                        "They say a lot of Arios priestesses used to be hookers, before they converted. I don't know why. But it's kind of turning me on.",
                        "Arios is the god of Light and Strength. May His Light guide us towards good deeds, and His Strength support our arms when the time comes to strike down evil.",
                        "The true teachings of Arios are a thing of beauty. Don't listen to those priests, all they know how to do is spout nonsense. Find the Light of Arios within your heart.",
                        "They say demons roam the streets. I say it's nothing compared to what goes on at Court.",
                        "All the court nobles do is eat, drink, fuck, and plot against one another. I wish I had that kind of life.",
                        "This city is doomed. When the head is rotten, how can you save the body?",
                        "My sister is a maid at court. She had a glimpse of one of the ceremonies and wouldn't shut up about it. 'The dresses!', 'The lights!', 'The jewels!', 'The gold dishes!', and so on.",
                        "Every noble courtier has one or more courtesans in tow. That's how they call hookers there. Not that it stops them from visiting regular brothels, mind you.",
                        "The nobles of Zan are a curious breed. They suck their estates dry trying to make it at court and impress the King, but they all despise him and think him weak. They are the ones being played for fools.",
                        "At the beginning of his reign, 18 years ago, King Pharo was doing well enough. But his achievements have been unraveling one by one, and now the city has lost all direction.",
                        "I don't care what happened to the princess's mother, the King should have remarried. What if something happens to the princess?",
                        "No male heir spells disaster for any royal family. Why doesn't the King understand that?",
                        "Because King Pharo has no male heir, power will go to the princess's son, when and if she marries. I guess she would be regent in the interim.",
                        "Sure, King Pharo has a laissez-faire attitude to everything... But isn't that what makes Zan so great? Would you like to see a crackdown on whores, alcohol, spices, or even gambling?",
                        "The King is always brooding, his mood dark... He sure looks grim for someone whose courtiers throw so many parties.",
                        "The princess is a lovely thing, isn't she? All the knights and nobles are crazy in love with her.",
                        "Her delicate features and manners make the princess the sweetheart of all Zan, nobles and commoners alike.",
                        "The princess seems in a dark mood sometimes. Could such a blessed person have problems like all of us?",
                        "The King's knights are all sworn to protect him and his family. Their commander looks like Arios made flesh himself. He's a very zealous and devoted man.",
                        "I hear some big shot's been murdered a few days back in the castle. They are trying to keep the lid on it, but it seems like trouble is brewing.",
                        "Some ancient weapons hold tremendous power. I wonder how one can get a hold on one of those?",
                        "When people go to a whorehouse, they expect more than just a tryst... Good service is always appreciated.",
                        "So many young girls are turning into whoring slaves these days... Some even turn themselves in voluntarily. I guess it's one way to get food and shelter in these troubled times.",
                        "The girls are so glamorous there... I never knew being a slut was so rewarding. Makes me question my morals!",
                        "All travelers agree on one thing: the best thing about Zan is its sex slaves... Any kind of sexual fantasy can be fulfilled here. Many slaves take great pride in fulfilling their master's desires.",
                        "Girls in Zan are so easy. All it takes is showing up at the same place every day, chatting them up, and sooner or later they'll roll in the hay with you.",
                        "That merchant girl is so hot, man! I'd go there and buy stuff every day if I could convince her to fool around with me.",
                        "People who like unusual sex acts are less common, but they pay more money.",
                        "I came by this brothel the other day, and saw a pink-haired hottie... but was disappointed to find out she wasn't one of the working staff.",
                        "After a day's hard work, what's hotter than going to a club to be served by beautiful girls, then have one of them strip and go down on you? I understand the appeal.",
                        "Whores are like priestesses for the sex goddess, that's what my 'pa used to say. He was usually drunk as a skunk.",
                        "Some guy from Westmarch had trouble understanding what geishas are. He kept saying they're like regular hookers. I swear, it's impossible to educate these unrefined barbarians .",
                        "I went to this little establishment by the harbor, asking for a good massage. And I really got a good one, down there... Isn't it wonderful?",
                    ]

    chapter_gossip = {
                    1 : [
                            "Have you seen the new Guard uniforms? They adorn their armor with fine silk, while the rest of us starve..., "
                            "I've heard some talk of a secret lair somewhere around the Slums... A haven for thieves and bandits. I shiver to think of it.",
                            "Captain Farah is one greedy bitch. Her men came yesterday to shake one of my friends down. Everyone hates her, but they say she's got protection in high places.",
                            "The head of the guards is Captain Farah. Best stay clear of them if you want my advice. Levies and taxes are all the guards care about. If you ask me, they just make them up as they go.",
                            "Some say the captain of the Guard is getting too greedy, even among her own men... There are some who say they'd do better. Maybe they mean they'd be better at not getting caught.",
                            "Thieves are getting bold these days. Or desperate. Doesn't look like the guards care to do anything about it, mind you.",
                            "My neighbor complained about the taxes, so they took him in, and no one's heard of him since. Better suck it up and stay alive, if you want my 2 denars.",
                            "The guards took everything from me, but what can I do? Only the King has higher authority, and he won't listen to a commoner.",
                            "Some say the thieves operate in an organized fashion, much like a guild. I don't buy this nonsense. Ever seen a thief with anything else than spice for brains?",
                            "People here like to blame a secret Shalia cabal for all their ills, but let me tell you: it's our good Arios-loving captain who's robbing us blind at the moment!",
                            "I keep hearing about this new brothel outside the city. I really have to check it out.",
                        ],
                    2 : [
                            "There has been a wave of murders in the city lately... And not just the usual rabble: they took out some pretty big shots.",
                            "People say the streets aren't safe at night, hired blades on the prowl... Many highborns won't go out anymore without an escort.",
                            "Somebody's been snuffing out the blue bloods one by one... It was about time someone started fighting for justice in this city!",
                            "A murderous killer is on the prowl... Some say he killed the high judge, and the royals could be next.",
                            "How dare someone threaten the life of our dear Princess? I hope they catch the motherfucker, and gouge his eyes out!",
                            "No one is safe in this city, not even the judges... Time to head for the country until things quiet down.",
                            "Don't worry about those killers. There are only after the bigwigs, no one is paying to assassinate small fry like you and me.",
                            "I've heard of a fearsome group of superhuman stealth warriors, on a quest for blood and revenge throughout the city... They call them {i}ninjas{/i}.",
                            "Ninjas? What a load of bull. They only exist in children's tales.",
                            "Ninjas are a secret society of bloodthristy assassins that has infiltrated Zan. Or so I hear.",
                            "Why would anyone threaten the Princess's life? She's the only one who doesn't wish us little people ill in this royal nest of vipers.",
                            "Noble families have paid a heavy toll in the latest wave of murders... Maybe this so-called revolution is coming after all?",
                        ],
                    3 : [],
                    4 : [],
                    5 : [],
                    6 : [],
                    7 : [
                            "Have you heard of [MC.name], the legendary Brothel Master? I bet he can turn your sister into a sex-crazed goddess.",
                            "[MC.name] is the best of the best. There was never a better Brothel Master in all of Zan, and there never will be.",
                            "Do you know about the King? I mean, the Brothel King? It's [MC.name], the legendary owner of [brothel.name]...",
                            "The best brothel in town? Where the hell did you come from? It's [brothel.name], of course! It's leagues ahead of every other whorehouse. The competitors just gave up.",
                        ],

                    # The following are added by the story

                    "c1_good" : [
                                    "Captain Maya is really a godsend. She's going to clean up the Guard's act in no time, believe me.",
                                    "I was stopped by the guards the other day. I thought they would rob me like they usually do, but they were polite and they just let me go. Amazing.",
                                    "Many of the old guards have been kicked out of the force recently. It seems like the new captain is serious about fighting corruption.",
                                    "Don't ever tell him I said that, but it's obvious Roz has a crush on Maya. That big oaf doesn't stand a chance...",
                                ],
                    "c1_neutral" :[
                                    "Is the new captain any better than the old one? Things will never change around here, no matter who's in charge.",
                                    "Captain Lydie seems just as shrewd as the old captain, but at least she keeps a low profile. Guild wars are bad for business.",
                                    "I've heard some talk of a secret lair somewhere around the Slums... A haven for thieves and bandits. I shiver to think of it.",
                                    "Thieves are getting bold these days. Or desperate. Doesn't look like the guards care to do anything about it, mind you.",
                                    "Some say the thieves operate in an organized fashion, much like a guild. I don't buy this nonsense. Ever seen a thief with anything else than spice for brains?",
                                ],
                    "c1_evil" : [
                                    "Have you seen the new guard uniforms? They adorn their armor with fine silk, while the rest of us starve...",
                                    "Captain Farah is one greedy bitch. Her men came yesterday to shake one of my friends down. Everyone hates her, but they say she's got protection in high places.",
                                    "The head of the guards is Captain Farah. Best stay clear of them if you want my advice. Levies and taxes are all the guards cares about. If you ask me, they just make them up as they go.",
                                    "Some say the captain of the Guard is getting too greedy, even among her own men... There are some who say they'd do better. Maybe they mean they'd be better at not getting caught.",
                                    "My neighbor complained about the taxes, so they took him in, and no one's heard of him since. Better suck it up and stay alive, if you want my 2 denars.",
                                    "The guards took everything from me, but what can I do? Only the King has higher authority, and he won't listen to a commoner.",
                                    "People here like to blame a secret Shalia cabal for all their ills, but let me tell you: it's our good Arios-loving captain who's robbing us blind at the moment!",
                                    "Captain Farah is stronger than ever in the slums. She's completely unopposed now, our only choice is to pay her cronies. Do you want to hang?",
                                    "I thought things couldn't get worse with the Guard, but it did. They looted my shop and raped my wife and daughters. No one dared lift a finger...",
                                ],

                    "c2_kunoichi" : [
                                    "Heard about the Kunoichi? A secret organization of female ninjas... That is so hot!",
                                    "I wish they'd catch those women devils, the Kunoichi. I hear they consort with demons.",
                                    "Don't believe what you hear about the Kunoichi. They're pure and noble warriors.",
                                    "I heard some kind of female ninja clan is going after a brothel owner in the city... Poor guy, he's dead meat.",
                                    "Female ninjas? I bet they wear very skimpy clothing... Hmm...",
                                    "I read the tale about female ninjas that can kill using only their vagina... Crazy, I know.",
                                    "When a baby gets abandoned, sometimes a ninja clan will adopt her... That's what I heard.",
                                ],

                    "c2_kunoichi_hunt" : [
                                    "The {b}Thieves' guild{/b} quarter is already a dump... And now there are ninjas there, too???",
                                    "Ninjas in the {b}Thieves' guild{/b} quarter... The rogues ain't gonna like that.",
                                    "I told you I saw a child in the {b}Thieves' guild{/b} quarter... I was gonna help, but then I saw she had a huge ninja star, so I thought better of it.",
                                    "She did look like a lil' brat, but she was a ninja, I tells ya! Standin' atop the {b}Thieves' guild{/b}'s roof, no less.",

                                    "I was walking alongside the {b}Beach{/b} at night, when I saw a ghost! A beautiful, pale lady ghost. And she was walking over water. Like a ninja!"
                                    "I went to the {b}Beach{/b} at night to fish for trout, and I saw a beautiful lady taking a bath by the moonlight. When I tried to approach her, she disappeared like a ghost!",
                                    "There have been disappearances near the {b}Beach{/b}. Some blame ninjas, but that's childish nonsense.",
                                    "So the pretty lady waved her hand, and the water around her rose and shielded her from view. We couldn't see her from the {b}Beach{/b} anymore, and none of us dared venture into the sea.",

                                    "I'm telling you, she was a ninja! Who else could climb the {b}Prison{/b} walls like that?",
                                    "It was the most peculiar thing, the girl snapped her fingers, and it caused a tremor! The {b}Prison{/b} guards fell down on their asses.",
                                    "Why would a ninja stalk the {b}Prison{/b} quarter? Any criminal knows to steer clear of our good King's jails!",
                                    "Stop it, there are no such things as female ninjas flying above the {b}Prison{/b}! Now go clean up your room!",
                                ],

                     }

    district_gossip = {
                        "The Slums" : [
                                    "Thieves are everywhere in the slums, and guards are even worse. I can't wait to get out of this place. Other places can't possibly be this bad!",
                                    "The worst thing about the slums is the stench. Or second worst thing. Worse is, you can get your throat slit for a denar and never smell a thing, ever again.",
                                    "The people of Zan are wicked, depraved and degenerates, but they sure are industrious. The city grows by the day! And the slums are her underbelly.",
                                    "I saw this strange girl in the sewers, all by herself. I told her there were monsters about, but she just smiled and said 'I know.'",
                                    "The sewers are full of dirty critters and monsters... Some people even make a living hunting them.",
                                    "Have you met that strange girl, Willow? She's got odd ears, I wonder if she's fully human. She's cute, though.",
                                    "The farmland is haunted. Don't go there.",
                                    "There are always strange things going on in the country. I even hear some girls fuck animals there.",
                                    "Have you met Goldie at the farm? She's a sweet young woman. It's so sad, what happened to her family.",
                                    "I usually go and buy milk from Goldie at the farm. She gets it from her cows, but I'd rather milk her instead, if you catch my drift...",
                                    "If I wanted to buy animals, I'd go to the farm of course. But I hear some of them are behaving strangely.",
                                    "There's a crazy girl in the junkyard, sifting through the garbage to find Arios-knows-what. I tried to talk some sense into her, but she didn't even listen to me.",
                                    "I made a good deal last week, selling an old useless gizmo to the funny girl in the junkyard.",
                                    "Have you met Gina, the weird scientist in the junkyard? She buys and sells some weird machines. Gives me the creeps.",
                                    "A thieves guild, here, in the slums? Nonsense. The Guard captain would never allow it."
                                ],
                        "The Docks" : [
                                    "The league of adventurers is located somewhere near the harbor. The smell of rotting fish isn't off-putting to those rogues.",
                                    "Why are there so many whorehouses close to the sea? Is it because it's wetter here?",
                                    "Why are there so many whorehouses in the Docks? Is it because it sounds like 'Dicks'?",
                                    "Where there are sailors, there are whores. That's just a fact of life.",
                                    "There's a woman selling gifts by the seafront. She's got those huge knockers...",
                                    "Have you seen that woman in red, selling gifts by the seafront? She's got gifts all right, a huge pair of tits...",
                                    "They sell those strange slaves by the harbor, mindless drones with horse-like cocks... My girlfriend thinks it's cool, but I find it creepy.",
                                    "There are slavemongers from the Blood Islands about in the harbor. They treat humans like cattle. It's awesome.",
                                    "Fancy ladies go to the harbor to buy some very special slaves... I hear they obey every order and they have huge... *whisper*",
                                    "Have you seen that fearsome slaver by the harbor, all clad in leather like a dominatrix? She turns me on... ",
                                ],
                        "The Warehouse" : [],
                        "The Magic Gardens" : [],
                        "The Cathedra" : [
                                    "The Cathedra is the pride of Zan and the crown jewel of all Xeros. All rejoice in the glorious light of Arios!",
                                    "The Cathedra was a place for silent contemplation and prayer, but with all the filthy pilgrims who pour in now, day in, day out, I don't want to go there anymore.",
                                    "The waves of pilgrims heading to the Cathedra have been good for business, that's for sure.",
                                    "Judging by the fervor at the Cathedra, you'd think Arios was the one and only god... Many of us in this city are not followers of Arios; they seem to forget that all too easily.",
                                ],
                        "The King's Hold" : [
                                    "The knights in the palace are all good Arios-loving folks. That warms my heart.",
                                    "I've been told of a secret swapping society in the King's Hold, where members exchange their wives and daughters in all-night orgies...",
                                    "The nobles roam the King's Hold, like a pack of vultures hovering, waiting for their next meal. They all think they can sire the next heir, or take power by other means when the King's gone...",
                                ],
                       }




    ## JOKES ##

    jokes = {
            "harmless" : ("What's the hardest thing about being a Guard? Telling your parents you're gay!", "My dog used to run after everyone on a horse. It got so bad, I had to take his horse away.", "What's the difference between a snowman and a snowwoman? Snowballs!", "How do you catch a bra? With a booby trap."),
            "sex" : ("Why was the luth teacher arrested? For fingering a minor...", "What do the Court and pussies have in common? One slip of the tongue, and you're in deep shit.", "Know what I do in my garden? Get down and dirty with my hoes.", "What do you call the useless part around a dick? A man!", "What's the difference between a wife and a job? After 5 years, your job will still suck."),
            "dark" : ("How do you make a girl scream twice? First, fuck her in the ass, then wipe your dick on her curtains!", "I like my women like my wine... Locked in the cellar!", "A doctor tells his patient:'I'm sorry, but you've only got about 10 left.'\nPatient:'10 what? Months, weeks?'\nDoctor:'Nine, eight...'", "What's the best part about sex with twenty-eight-year-olds? There are 20 of them!", "How many male chauvinists does it take to refuel the lamp? None. Let her do the dishes in the dark."),
            "mean" : ("I like you. People say I've no taste, but I like you.", "Damn, you're hot, but you'd be a lot hotter if you just shut up.", "I like my women attractive, dumb, and bitchy. You seem to fit the bill quite nicely.", "I'd hire you as a whore, but my girls have class...")
        }


    ## COMPLIMENTS ##

    compliments =  {
                    "beauty" : ("%s, aren't you beautiful today...", "%s, you're so lovely...", "%s, I swear you have the cutest face.", "Your face lights up when you smile, %s."),
                    "body" : ("Wow, you've got such a hot body you know.", "Baby, you've got such an amazing ass...", "I love your knockers, honey, they look amazing without a bra.", "Look at that nice piece of ass...", "Wow, you're stunning, makes me really want to touch the merchandise!"),
                    "mind" : ("You're a bright girl, I like that about you.", "A beautiful mind... Haven't you got everything?", "You seem to know a lot... You definitely should get to know more about me!", "I love the conversations we're having, it's always enlightening."),
                    "spirit" : ("You're always spirited and lively; it's very nice.", "At last, someone with character. I don't like dull people.", "You're always passionate about everything. I like that!")
                    }


    ## GIRL BACKGROUND ##

    slave_stories = ["slave_story1", "slave_story2", "slave_story3", "slave_story4", "slave_story5", "slave_story6", "slave_story7", "slave_story8"]

    origins = ["Zan", "the border with the Holy Lands", "the Blood Islands", "Karkyr", "Westmarch", "the desert of Hokoma", "Borgo, the port city", "the Goliath desolations", "the Arik mountains"]

#     origin_description = {
#                           "Zan" : "I know the old streets of Zan like the back of my hand... I used to walk to the market with my %s, wondering what the strange houses with the red lanterns were... Now I know... *blush*",
#                           "the border with the Holy Lands" : "The Holy Lands are a place of war and suffering, always have been. Still, I remember a few peaceful moments. Walking with my %s across old battlefields, covered with red blooming flowers, watching nature reclaim its rights...",
#                           "the Blood Islands" : "The Blood Islands are a cruel place... I remember going to the arena with my %s and me, watching slaves being shredded to pieces by monsters... It was bloody and exciting. The arena here is very tame in comparison.",
#                           "Karkyr" : "Karkyr is a beautiful and fascinating city, ruled by the Archmage Council. Everything is magical, even the wells and the furniture can speak. It used to freak my %s out! There were also some spectacular incidents, of course, but that was part of the fun.",
#                           "Westmarch" : "The Westmarch Principalities, where I grew up, is a very unpredictable place. One day a city is flourishing, the next it descends into anarchy, and raiders loot and rape the town. I used to think danger was exciting, but my %s didn't like it one bit.",
#                           "the desert of Hokoma" : "The desert people are a quiet and wise sort. My %s know many secrets, and knew how to keep them. I miss the peace and quiet of nights in the desert.",
#                           "Borgo, the port city" : "There's no describing how busy and crowded Borgo is on most days, with sailors from all over the world selling everything you can imagine, and many other things, too. I loved to sit by the pier with my %s in the early hours, listenning to the waves.",
#                           "the Goliath desolations" : "The desolations are a cold, horrible place. Whether you are rich or poor, you have to work hard every day, just to barely survive. If I didn't have my %s to rely on, I don't know what I would have done.",
#                           "the Arik mountains" : "They say the Arik mountains are the highest in the world. The air is pure there, not full of filth and magic like here... My %s taught me how to love and respect the mountains.",
#                           }

    homes = ["palace", "hovel", "mansion", "shack", "hut", "big house", "small house", "temple", "shop", "old house", "tower", "church"]

    guardians = ["parents", "dad", "mom", "uncle", "grand-ma", "auntie", "grand-pa", "big brother", "big sister", "little brother", "little sister", "tutor"]

    hobbies = ["painting", "singing", "playing music", "hiking", "gambling", "shopping", "reading", "weaving", "swimming", "writing"]

    colors = ["white", "yellow", "red", "green", "blue", "purple", "orange", "pink", "black"]

    food = ["cake", "cream", "fish", "fruit", "meat", "cookies", "sweets", "chocolate", "bread", "rice"]

    drinks = ["milk", "sake", "wine", "beer", "apple juice", "lemon juice", "mango juice", "spice water"]


    ## MC interact counters ##

#    MC_interact_counters = {
#                            "chat" : 0, "gossip" : 0, "life" : 0, "love" : 0,
#                            "origins" : 0, "hobbies" : 0, "likes" : 0, "dislikes" : 0,
#                            "harmless" : 0, "adult" : 0, "dark" : 0, "mean" : 0,
#                            "present" : 0, "money" : 0,
#                            "beauty" : 0, "body" : 0, "mind" : 0, "spirit" : 0,
#                            "hand" : 0, "kiss" : 0, "ass" : 0, "breasts" : 0, "pussy" : 0,
#                            "service" : 0, "sex" : 0, "anal" : 0, "fetish" : 0,
#                            "offer" : 0,
#                            "well_being" : 0, "happiness" : 0, "job" : 0,
#                            "scold" : 0, "threaten" : 0, "beat" : 0, "torture" : 0,
#                            "charm_obedience" : 0, "charm_sensitivity" : 0, "charm_libido" : 0, "charm_love" : 0, "charm_fear" : 0
#                            }

    ## Results dictionaries

    roll_dict = {1 : "critical failure", 2 : "failure", 3 : "neutral", 4 : "neutral", 5 : "success", 6 : "critical success"}
    result_dict = {-999 : "very bad", 1 : "bad", 6 : "average", 9 : "good", 12 : "very good", 15 : "perfect"}
    result_colors = {"very bad" : c_red, "bad" : c_lightred, "average" : c_white, "good" : c_lightgreen, "very good" : c_green, "perfect" : c_orange}
    result_star_dict = {"very bad" : "{image=img_empty_star}"*5, "bad" : "{image=img_star}"+"{image=img_empty_star}"*4, "average" : "{image=img_star}"*2+"{image=img_empty_star}"*3, "good" : "{image=img_star}"*3+"{image=img_empty_star}"*2, "very good" : "{image=img_star}"*4+"{image=img_empty_star}", "perfect" : "{image=img_star}"*5}

    reversed_result_dict = {v: k for k, v in result_dict.items()}

    result_reference = "%i: {color=%s}Very bad{/color}\n" % (reversed_result_dict["bad"]-1, result_colors["very bad"]) + "%i-%i: {color=%s}Bad{/color}\n" % (reversed_result_dict["bad"], reversed_result_dict["average"]-1, result_colors["bad"]) + "%i-%i: {color=%s}Average{/color}\n" % (reversed_result_dict["average"], reversed_result_dict["good"]-1, result_colors["average"]) + "%i-%i: {color=%s}Good{/color}\n" % (reversed_result_dict["good"], reversed_result_dict["very good"]-1, result_colors["good"]) + "%i-%i: {color=%s}Very good{/color}\n" % (reversed_result_dict["very good"], reversed_result_dict["perfect"]-1, result_colors["very good"]) + "%i+: {color=%s}Perfect{/color}\n" % (reversed_result_dict["perfect"], result_colors["perfect"])



#    result_value = {"very bad" : 0, "bad" : 1, "average" : 2, "good" : 3, "very good" : 4, "perfect" : 5}
#    roll_value = {"critical failure" : 0, "failure" : 1, "neutral" : 2, "success" : 3, "critical success" : 4}

#    result_names = {v: k for k, v in result_value.items()}
#    roll_names = {v: k for k, v in roll_value.items()}

    perform_job_dict = {
#                        "roll_critical failure" : "\n{color=[c_red]}%s wasn't trying hard today. She barely even paid attention to what she was doing.{/color}",
#                        "roll_failure" : "\n%s wasn't really into it.",
#                        "roll_neutral" : "\n%s went about her job as usual.",
#                        "roll_success" : "\n%s was really motivated today.",
#                        "roll_critical success" : "\n{color=[c_green]}%s did everything she could to please the customers.{/color}",

                        "waitress_stats" : (("charm", 6), ("constitution", 2), ("body", 1), ("beauty",1)),
                        "waitress_changes" : ((("charm",), 100, 2), (("constitution",), 35, 1), (("obedience", "body", "beauty"), 15, 1), (("sensitivity",), 15, -1)),

                        "waitress_init" : "%s served drinks to %s customers.",
                        "waitress_tags" : ["waitress"],
                        "waitress_tags2" : ["maid", "geisha"],

                        "dancer_stats" : (("body", 6), ("libido", 2), ("refinement", 1), ("charm",1)),
                        "dancer_changes" : ((("body",), 100, 2), (("libido",), 35, 1), (("constitution", "refinement", "charm"), 15, 1), (("obedience",), 15, -1)),

                        "dancer_init" : "%s danced sexily for %s customers.",
                        "dancer_tags" : ["dancer"],
                        "dancer_tags2" : ["fight"],

                        "masseuse_stats" : (("beauty", 6), ("sensitivity", 2), ("refinement", 1), ("body",1)),
                        "masseuse_changes" : ((("beauty",), 100, 2), (("sensitivity",), 35, 1), (("refinement", "body", "libido"), 15, 1), (("constitution",), 15, -1)),

                        "masseuse_init" : "%s gave a hot massage to %s customers.",
                        "masseuse_tags" : ["masseuse"],
                        "masseuse_tags2" : ["swim"],

                        "geisha_stats" : (("refinement", 6), ("obedience", 2), ("beauty", 1), ("charm",1)),
                        "geisha_changes" : ((("refinement",), 100, 2), (("obedience",), 35, 1), (("beauty", "charm", "sensitivity"), 15, 1), (("libido",), 15, -1)),

                        "geisha_init" : "%s entertained %s customers with a display of traditional arts.",
                        "geisha_tags" : ["geisha"],
                        "geisha_tags2" : ["maid", "waitress", "date"], # Date pictures can be used as substitutes for geisha

                        "waitress_very bad" : "\n{color=[c_red]}%s spilled drinks everywhere and didn't even apologize. The customers thought the service was terrible and complained.",
                        "waitress_bad" : "\n{color=[c_lightred]}%s was shy and clumsy. The customers grumbled that the service was bad.",
                        "waitress_average" : "\n%s served everyone and chatted with the customers. They thought she was ok.",
                        "waitress_good" : "\n{color=[c_lightgreen]}%s flirted with the customers as she served them drinks, making them feel welcome.",
                        "waitress_very good" : "\n{color=[c_green]}%s traded rowdy jokes with the customers, flashing her goods while serving. Everyone loved her.",
                        "waitress_perfect" : "\n{color=[c_orange]}%s worked without underwear today and used all of her charms to drive the customers wild. They completely fell over for her.",

                        "dancer_very bad" : "\n{color=[c_red]}%s has two left feet. Her dancing was embarrassingly bad and the customers booed and threw things at her.",
                        "dancer_bad" : "\n{color=[c_lightred]}%s's dance was awkward and uninteresting.",
                        "dancer_average" : "\n%s danced suggestively in front of the customers.",
                        "dancer_good" : "\n{color=[c_lightgreen]}The club heated up as %s danced around the stage, flashing her goods.",
                        "dancer_very good" : "\n{color=[c_green]}The crowd went wild as %s danced and stripped on stage, her skin glistening with sweat as she worked the pole.",
                        "dancer_perfect" : "\n{color=[c_orange]}The customers couldn't take their eyes off %s as she waved to the music, slowly and sexily stripping off, until she stood there naked and wet under their perverted gaze.",

                        "masseuse_very bad" : "\n{color=[c_red]}%s clumsily went around giving back rubs, hurting some of them in the process. They grumbled and told her to go away.",
                        "masseuse_bad" : "\n{color=[c_lightred]}%s tried to give customers a relaxing rub. Her technique was lacking, and the customers were left unsatisfied.",
                        "masseuse_average" : "\n%s gave massages to customers in the onsen, helping them relax and feel more comfortable.",
                        "masseuse_good" : "\n{color=[c_lightgreen]}%s joined the customers in the onsen, wearing only a towel, and gave them a nice massage. The customers were visibly turned on after she was done.",
                        "masseuse_very good" : "\n{color=[c_green]}The towels slipped off as %s gave the customers a passionate body massage. She used her hands and tongue to turn them on while they waited for their turn.",
                        "masseuse_perfect" : "\n{color=[c_orange]}%s went naked into the onsen among the customers, rubbing her body against them until they came all over her silky skin.",

                        "geisha_very bad" : "\n{color=[c_red]}%s completely lacked class and came across as clumsy and ignorant. The customers complained that she was just a street girl dressed like a geisha.",
                        "geisha_bad" : "\n{color=[c_lightred]}%s kept trying to act like a real geisha when serving tea; it was obvious to anyone that she was not the real thing, though, and customers quickly lost interest.",
                        "geisha_average" : "\n%s played a little shamisen and chatted with the customers, helping them relax and forget their worries...",
                        "geisha_good" : "\n{color=[c_lightgreen]}%s held a tea ceremony with the customers, exchanging pleasantries while she nonchalantly let her kimono slide to the side, revealing some skin.",
                        "geisha_very good" : "\n{color=[c_green]}%s was the life of the party as she greeted customers by their name and complimented them. Wearing a short, revealing kimono, she brushed against their bodies, leaving them all turned on by her scent.",
                        "geisha_perfect" : "\n{color=[c_orange]}%s was the epitome of the geisha, being in turn sweet, gifted, witty, and sexy as hell. She wore a see-through kimono, kinkily displaying her cleavage and thighs to drive the customers wild.",

                        "flasher" : " A customer dared her to show her tits, and she proudly displayed them for everyone to see.",
                        "temptress" : " She convinced the customer%s to try it.",
                        "catgirl" : " She purred as she eagerly drank all the customer's cum and licked his dick clean.",
                        "virgin" : " The customer was amazed that she was a virgin and paid extra.",
                        "virgin_group" : " The customers were amazed that she was a virgin and paid extra.",
                        "reroll" : " She barely avoided a catastrophe.",
                        "unlucky" : "",
                        "lucky" : "",
                        "random item" : " The customer%s left something valuable.",
                        "beauty bonus" : " The customer%s found her beauty stunning.",
                        "body bonus" : " The customer%s loved her curves.",
                        "charm bonus" : " The customer%s fell under her charm.",
                        "refinement bonus" : " The customer%s loved how refined she was.",
                        "libido bonus" : " The customer%s thought she was hot.",
                        "obedience bonus" : " The customer%s liked how she took orders.",
                        "constitution bonus" : " The customer%s thought she was fit.",
                        "sensitivity bonus" : " The customer%s loved how sensitive she was.",

                        "DT_group" : " The customers took turns sticking their dicks down her throat as deep as they could.",
                        "DT" : " The customer was amazed that he could stick his dick so far down her throat.",
                        "bukkake" : " She was fucked hard in her every hole, then the customers took turns coming all over her face.",
                        "creampie" : " He came all over her pussy and belly while she moaned with pleasure.",
                        "creampie_group" : " They took turns coming into her pussy until it dripped buckets of cum.",
                        "anal creampie" : " He fucked her ass hard then shot a huge load in her open asshole.",
                        "anal creampie_group" : " They took turns fucking and cumming in her ass until her belly was swollen with cum.",
                        "cum on face" : " He moaned and came loads all over her face and hair.",
                        "cum on face_group" : " They moaned, cumming loads all over her face and hair.",
                        "swallow" : " She eagerly swallowed the cum as it dripped down her throat.",
                        "irrumatio" : "",

                        "not satisfied" : " :Pron: was disappointed that she wouldn't do what :pron: wanted.",
                        "group not satisfied" : " She wouldn't do it, but they didn't mind because group %s is hot.",
                        "bisexual not satisfied" : " In the end :pron: got %s, but :pron: was happy to let the girls have their way.",

                        "roll_critical failure" : "\n{color=[c_red]}%s wasn't trying hard today. She barely even paid attention to what she was doing.{/color}",
                        "roll_failure" : "\n%s wasn't really into it.",
                        "roll_neutral" : "\n%s went about her job as usual.",
                        "roll_success" : "\n%s was really motivated today.",
                        "roll_critical success" : "\n{color=[c_green]}%s did everything she could to please.{/color}",

                        "bisexual_roll_critical failure" : "\n{color=[c_red]}%s weren't trying hard today. They weren't paying attention to what they were doing.{/color}",
                        "bisexual_roll_failure" : "\n%s weren't really into it.",
                        "bisexual_roll_neutral" : "\n%s went about their job as usual.",
                        "bisexual_roll_success" : "\n%s were really motivated and playful today.",
                        "bisexual_roll_critical success" : "\n{color=[c_green]}%s did everything they could to please the customers and each other.{/color}",

                        "anal_stats" : (("anal", 6), ("constitution", 2), ("body", 1), ("sex",1)),
                        "anal_changes" : ((("anal",), 100, 2), (("constitution",), 70, 1), (("libido", "obedience", "body"), 25, 1), (("sensitivity",), 25, -1)),
                        "anal_init" : " :Pron: wanted to fuck %s in the ass.",
                        "anal_tags" : ["anal"],

                        "sex_stats" : (("sex", 6), ("libido", 2), ("beauty", 1), ("service",1)),
                        "sex_changes" : ((("sex",), 100, 2), (("libido",), 70, 1), (("sensitivity", "constitution", "beauty"), 25, 1), (("obedience",), 25, -1)),
                        "sex_init" : " :Pron: wanted to have sex with %s.",
                        "sex_tags" : ["sex"],

                        "service_stats" : (("service", 6), ("sensitivity", 2), ("charm", 1), ("fetish",1)),
                        "service_changes" : ((("service",), 100, 2), (("sensitivity",), 70, 1), (("obedience", "libido", "charm"), 25, 1), (("constitution",), 25, -1)),
                        "service_init" : " :Pron: wanted %s to give service.",
                        "service_tags" : ["service"],

                        "fetish_stats" : (("fetish", 6), ("obedience", 2), ("refinement", 1), ("anal",1)),
                        "fetish_changes" : ((("fetish",), 100, 2), (("obedience",), 70, 1), (("constitution", "sensitivity", "refinement"), 25, 1), (("libido",), 25, -1)),
                        "fetish_init" : " :Pron: had some very special requests for %s.",
                        "fetish_tags" : ["fetish"],

                        "whore_init" : "%s came to your brothel and chose %s.",
                        "bisexual_tags" : ["bisexual"],
                        "group_tags" : ["group"],

                        "M anal_very bad" : "\n{color=[c_red]}%s had a hard time and didn't like it one bit. The customer quickly lost interest and left grumbling.",
                        "M anal_bad" : "\n{color=[c_lightred]}%s doesn't like it in the ass and it showed. She didn't enjoy herself and neither did the customer.",
                        "M anal_average" : "\n%s moans as the customer gets his way with her ass. She's growing to enjoy anal sex.",
                        "M anal_good" : "\n{color=[c_lightgreen]}%s takes it up the ass with moans of pleasure. The customer comes all over her butt with a delighted smile on his face.",
                        "M anal_very good" : "\n{color=[c_green]}Looks like this girl was made for anal. %s uses her ass to work the customer's dick until it's hard as a rock, inviting him to cum and fill her up.",
                        "M anal_perfect" : "\n{color=[c_orange]}%s is an anal sex goddess. She takes it up the ass with unbridled pleasure, crying out loud as the customer releases his seed deep into her belly.",

                        "M sex_very bad" : "\n{color=[c_red]}%s is a terrible lay, not enjoying it one bit as the customer violates her body. The customer thought she was awful and left complaining.",
                        "M sex_bad" : "\n{color=[c_lightred]}%s tries her best to give the customer a good time, but her fake cries are rather obvious. The customer left relieved but disappointed.",
                        "M sex_average" : "\n%s fucks with the customer and tries a few interesting positions. She is starting to enjoy herself and some of her moans were clearly not fake.",
                        "M sex_good" : "\n{color=[c_lightgreen]}After a quick bout of foreplay, %s and the customer have wild sex in various positions until he cums hard all over her body.",
                        "M sex_very good" : "\n{color=[c_green]}%s is amazing and works that dick like a succubus. She reaches orgasm and cries out as the customer pumps warm cum into her.",
                        "M sex_perfect" : "\n{color=[c_orange]}%s cannot get enough, screaming loudly as she enjoys being fucked through multiple orgasms and being covered in the customer's sticky cum.",

                        "M service_very bad" : "\n{color=[c_red]}The customer complains that %s doesn't know how to work a dick properly. The customer leaves, upset that she didn't even manage to finish him off.",
                        "M service_bad" : "\n{color=[c_lightred]}%s awkwardly tries to service the customer, but her technique is clearly lacking. He ends up masturbating while she looks on with shame.",
                        "M service_average" : "\n%s does her best to service the customer, slowly developing her own technique. After teasing the customer for a while, she smiles as he releases his load on her face.",
                        "M service_good" : "\n{color=[c_lightgreen]}%s uses her skills to make the customer cum quickly and repeatedly, covering her face and tits with bodily fluids.",
                        "M service_very good" : "\n{color=[c_green]}%s is already wet thinking of the customer's dick as she starts sucking and licking it. It isn't long until the customer comes hard in her mouth.",
                        "M service_perfect" : "\n{color=[c_orange]}%s offers the customer her body to play with and makes wet sounds as she expertly sucks him off. She savours the feeling of hot, sticky cum on her face and in her mouth, begging the customer for more.",

                        "M fetish_very bad" : "\n{color=[c_red]}%s is scared and tense under the customer's touch. She is not enjoying this at all and the customer leaves completely unsatisfied.",
                        "M fetish_bad" : "\n{color=[c_lightred]}%s shivers as the customer does new, weird things to her body. The customer watches her reactions with some interest at first, but the slow pace quickly bores him.",
                        "M fetish_average" : "\n%s moans a little as she is blindfolded and tied up. She seems more curious than scared about what's happening to her now, and the customer has fun playing with her for a while.",
                        "M fetish_good" : "\n{color=[c_lightgreen]}%s shivers with excitement as she feels the bite of the ropes in her skin. The customer teases her body until she is completely wet, begging to be fucked.",
                        "M fetish_very good" : "\n{color=[c_green]}%s enjoys the mix of pleasure and pain and begs submissively for more. The customer violates her as she's tied up, bringing her to climax as he cums hard all over her.",
                        "M fetish_perfect" : "\n{color=[c_orange]}%s enjoys everything the customer does to her, suggesting new, humiliating ways to tie herself up and get punished. She screams with pain and pleasure, cumming multiple times as her various holes are violated.",

                        "M bisexual_very bad" : "\n{color=[c_red]}%s were clumsy and uncooperative. The customer quickly got bored and left, grumbling about a refund.",
                        "M bisexual_bad" : "\n{color=[c_lightred]}It's obvious %s aren't really good at this and are just pretending. The customer fucks them one after the other, but there is no chemistry.",
                        "M bisexual_average" : "\n%s slowly finger their pussies while the customer looks on with lust. He soon joins them, and they do their best to make it a memorable time.",
                        "M bisexual_good" : "\n{color=[c_lightgreen]}%s are eagerly touching and teasing each other. They playfully try new ways to excite the customer, and he quickly cums as they play with each other's breasts and pussy.",
                        "M bisexual_very good" : "\n{color=[c_green]}%s love cock as much as they love each other. They both work the customer's dick using their hands, mouths and bodies, making him come all over them.",
                        "M bisexual_perfect" : "\n{color=[c_orange]}%s are perfect sex kittens, expertly licking each other's cunt while the customer fucks their every hole. They eagerly kiss and lick the cum from each other's mouth as he looks on with bliss.",

                        "group_very bad" : "\n{color=[c_red]}With too many customers to satisfy, %s seems at a loss and doesn't know what to do. The group leaves unsatisfied and complaining.",
                        "group_bad" : "\n{color=[c_lightred]}%s is kind of shy in a group. She tries to do her job but the customers find her performance rather underwhelming.",
                        "group_average" : "\nThe customers take turns fucking %s. She takes it all in stride.",
                        "group_good" : "\n{color=[c_lightgreen]}%s works hard to please every customer in the group, bringing them to a grand finish using her every hole. A moment they will not soon forget.",
                        "group_very good" : "\n{color=[c_green]}%s is fucked long and hard by the customers and it looks like she isn't ready to stop. It looks like no matter how many times they fuck her, she always wants another dick.",
                        "group_perfect" : "\n{color=[c_orange]}%s couldn't wait to have her every hole filled by the customers, not letting them rest until they have spurted their cum over every inch of her body.",

                        "F anal_very bad" : "\n{color=[c_red]}%s had a hard time and didn't like it one bit. The customer quickly lost interest and left grumbling.",
                        "F anal_bad" : "\n{color=[c_lightred]}%s doesn't like it in the ass and it showed. She didn't enjoy herself and neither did the customer.",
                        "F anal_average" : "\n%s moans as the customer gets her way with her ass. She's growing to enjoy anal sex.",
                        "F anal_good" : "\n{color=[c_lightgreen]}%s takes it up the ass with moans of pleasure. The customer pounds her butt with a delighted smile on her face.",
                        "F anal_very good" : "\n{color=[c_green]}Looks like this girl was made for anal. %s uses her ass to grind against the customer's pussy until it becomes very wet, inviting her to cum together with her.",
                        "F anal_perfect" : "\n{color=[c_orange]}%s is an anal sex goddess. She takes it up the ass with unbridled pleasure, crying out loud as the customer reaches her own intense orgasm.",

                        "F sex_very bad" : "\n{color=[c_red]}%s is a terrible lay, not enjoying it one bit as the customer violates her body. The customer thought she was awful and left complaining.",
                        "F sex_bad" : "\n{color=[c_lightred]}%s tries her best to give the customer a good time, but her fake cries are rather obvious. The customer left relieved but disappointed.",
                        "F sex_average" : "\n%s fucks with the customer and tries a few interesting positions. She is starting to enjoy herself and some of her moans were clearly not fake.",
                        "F sex_good" : "\n{color=[c_lightgreen]}After a quick bout of foreplay, %s and the customer have wild sex in various positions until they both cum hard.",
                        "F sex_very good" : "\n{color=[c_green]}%s is amazing and works that pussy like a succubus. She reaches orgasm and cries out as the customer gushes love juice all over her.",
                        "F sex_perfect" : "\n{color=[c_orange]}%s cannot get enough, screaming loudly as she enjoys being fucked through multiple orgasms and being covered in the customer's sticky love juice.",

                        "F service_very bad" : "\n{color=[c_red]}The customer complains that %s doesn't know how to work a pussy properly. She leaves, upset that she didn't even manage to finish her off.",
                        "F service_bad" : "\n{color=[c_lightred]}%s awkwardly tries to service the customer, but her technique is clearly lacking. The customer ends up masturbating while she looks on with shame.",
                        "F service_average" : "\nShe does her best to service the customer, slowly developing her own technique. After teasing the customer for a while, %s smiles as she receives the customer's splashing love juices all over her face.",
                        "F service_good" : "\n{color=[c_lightgreen]}%s uses her skills to make the customer squirt hard, covering her face and tits with bodily fluids.",
                        "F service_very good" : "\n{color=[c_green]}%s is already wet thinking of the customer's pussy as she starts fingering and licking it. It isn't long until the customer comes hard from her tongue work.",
                        "F service_perfect" : "\n{color=[c_orange]}%s offers the customer her body to play with and makes wet sounds as she expertly licks her out. She savours the feeling of hot, sticky love juice on her face and in her mouth, begging the customer for more.",

                        "F fetish_very bad" : "\n{color=[c_red]}%s is scared and tense under the customer's touch. She is not enjoying this at all and the customer leaves completely unsatisfied.",
                        "F fetish_bad" : "\n{color=[c_lightred]}%s shivers as the customer does new, weird things to her body. The customer watches her reactions with some interest at first, but the slow pace quickly bores her.",
                        "F fetish_average" : "\n%s moans a little as she is blindfolded and tied up. She seems more curious than scared about what's happening to her now, and the customer has fun playing with her for a while.",
                        "F fetish_good" : "\n{color=[c_lightgreen]}%s shivers with excitement as she feels the bite of the ropes in her skin. The customer teases her body until she is completely wet, begging to be fucked.",
                        "F fetish_very good" : "\n{color=[c_green]}%s enjoys the mix of pleasure and pain and begs submissively for more. The customer violates her as she's tied up, bringing her to climax as she cums hard with her.",
                        "F fetish_perfect" : "\n{color=[c_orange]}%s enjoys everything the customer does to her, suggesting new, humiliating ways to tie herself up and get punished. She screams with pain and pleasure, cumming multiple times as her various holes are violated.",

                        "F bisexual_very bad" : "\n{color=[c_red]}%s were clumsy and uncooperative. The customer quickly got bored and left, grumbling about a refund.",
                        "F bisexual_bad" : "\n{color=[c_lightred]}It's obvious %s aren't really good at this and are just pretending. The customer fucks them one after the other, but there is no chemistry.",
                        "F bisexual_average" : "\n%s slowly finger their pussies while the customer looks on with lust. She soon joins them, and they do their best to make it a memorable time.",
                        "F bisexual_good" : "\n{color=[c_lightgreen]}%s are eagerly touching and teasing each other. They playfully try new ways to excite the customer, and she quickly cums as they play with each other's breasts and pussies.",
                        "F bisexual_very good" : "\n{color=[c_green]}%s love pussy. They both work the customer's erogenous zones using their hands, mouths and bodies, making her come again and again.",
                        "F bisexual_perfect" : "\n{color=[c_orange]}%s are perfect sex kittens, expertly licking the customer's cunt and each other. They eagerly kiss and lick the love juice from each other's mouth as she looks on with bliss.",

                    }

    stat_increase_dict = {
                        "level" : "\n{color=[c_lightgreen]}LEVEL UP{/color}",
                        "stat" : "\n%s {color=[c_green]}+%s{/color}",
                        "stat_neg" : "\n%s {color=[c_red]}%s{/color}",
                        "xp" : "\nXP {color=[c_lightgreen]}+%s{/color}",
                        "xp_dark" : "\nXP {color=[c_darkgreen]}+%s{/color}",
                        "jp" : "\nJP {color=[c_orange]}+%s{/color}",
                        "gold+" : "\nGold {color=[c_darkgold]}+%s{/color}",
                        "gold-" : "\nGold {color=[c_darkgold]}%s{/color}",
                        "rep" : "\nRep. {color=[c_softpurple]}+%s{/color}",
                        "rep_neg" : "\nRep. {color=[c_red]}%s{/color}",
                        "job_up" : "\n{color=[c_orange]}JOB SKILL UP{/color}",
                        "rank" : "\n{color=[c_softpurple]}NEW RANK AVAILABLE{/color}"
                    }

    # Contrast colors are for lighter backgrounds
    event_color = {None : "%s"}

    for k in color_dict.keys():
        event_color[k] = "{color=" + color_dict[k] + "}%s{/color}"

    log_event_dict = {
                    "level" : "{color=" + c_orange + "}%s has gained a new level.{/color}",
                    "job_up" : "{color=" + c_orange + "}%s has increased her %s skill.{/color}",
                    "rank" : "{color=" + c_orange + "}%s is ready to reach a new rank.{/color}",
                    }

    attraction_dict = {
                        "beauty_good" : "was very beautiful",
                        "body_good" : "had a perfect body",
                        "charm_good" : "had great charm",
                        "refinement_good" : "was really refined",
                        "beauty_bad" : "was ugly",
                        "body_bad" : "was plain looking",
                        "charm_bad" : "was a bore",
                        "refinement_bad" : "was clumsy"
                    }

    #### BROTHEL SERVICES ####

    maintenance_desc = {"clean" : "Your brothel is " + event_color["good"] % "{b}clean{/b}" + ".",
                    "clean enough" : "Your brothel is " + event_color["a little good"] % "{b}clean enough{/b}" + ".",
                    "dusty" : "Your brothel is getting " + event_color["average contrast"] % "{b}dusty{/b}" + ".",
                    "dirty" : "Your brothel is getting " + event_color["a little bad"] % "{b}dirty{/b}" + ".",
                    "disgusting" : "Warning! Your brothel is " + event_color["bad"] % "{b}disgusting{/b}" + "!",
                    "fire" : event_color["very bad"] % "Warning!!! Your brothel is at risk of a fire!"
                    }

    gold_threat_amount = {1 : 500, 2 : 1000, 3 : 2500, 4 : 10000, 5: 25000} # Gain 1 threat for every slice of X gold depending on DISTRICT RANK up to gold max

    gold_threat_max = {1 : 4, 2 : 12, 3 : 18, 4 : 24, 5: 30, 6 : 36, 7 : 52} # Max gold threat depending on CHAPTER



    #### ITEMS ####

    quality_prefix = {
                    "dress_0" : "Ragged",
                    "dress_1" : "Worn",
                    "dress_2" : "Simple",
                    "dress_3" : "Fine",
                    "dress_4" : "Fancy",
                    "dress_5" : "Enchanted",
                    "dress_6" : "Legendary",

                    "necklace_0" : "Rusty",
                    "necklace_1" : "Broken",
                    "necklace_2" : "Small",
                    "necklace_3" : "Medium",
                    "necklace_4" : "Heavy",
                    "necklace_5" : "Magical",
                    "necklace_6" : "Legendary",

                    "ring_0" : "Rusty",
                    "ring_1" : "Fake",
                    "ring_2" : "Small",
                    "ring_3" : "Medium",
                    "ring_4" : "Large",
                    "ring_5" : "Magical",
                    "ring_6" : "Legendary",

#                      "gift_1" : "Cheap ",
#                      "gift_2" : "Common ",
#                      "gift_3" : "Fine ",
#                      "gift_4" : "Rare ",

                    "food_0" : "Rotten",
                    "food_1" : "Bland",
                    "food_2" : "Tasty",
                    "food_3" : "Juicy",
                    "food_4" : "Organic",
                    "food_5" : "Enchanted",
                    "food_6" : "Legendary",

#                      "accessory_1" : "Worn ",
#                      "accessory_2" : "Simple ",
#                      "accessory_3" : "Fine ",
#                      "accessory_4" : "Fancy ",
#                      "accessory_5" : "Enchanted ",

                    "scroll_0" : "Tattered",
                    "scroll_1" : "Minor",
                    "scroll_2" : "Lesser",
                    "scroll_3" : "Medium",
                    "scroll_4" : "Greater",
                    "scroll_5" : "Ultimate",

                    "misc_0" : "Worthless",
                    "misc_1" : "Cheap",
                    "misc_2" : "Common",
                    "misc_3" : "Fine",
                    "misc_4" : "Rare",
                    "misc_5" : "Magical",
                    "misc_6" : "Legendary",

                    }

    quality_modifier = { # High increase in cost for upper ranks (see how it behaves)
                        0 : 0.25,
                        1 : 1.0,
                        2 : 2.5, #?
                        3 : 5.0, #?
                        4 : 12.5, #?
                        5 : 25.0, #?
                        6 : 50.0 #?
                        }



    #### QUESTS & CLASSES ####

    ## PRICES ##

    special_quest_description = {
                                "Cheap" : "This class is cheap. Enroll now and benefit from better prices!",
                                "Masterclass" : "This class is taught by a master. Stats will increase faster than normal.",
                                "High reward" : "The rewards for this quest are more important than usual.",
                                "Notorious" : "This quest will bring extra reputation when completed.",
                                "Story" : "Complete this quest to advance the story.",
                                "story" : "Complete this quest to advance the story.",
                                }

    quest_base_gold = { # This the gold value per stat point of requirement and per day
                        "normal" : 1,
                        "sex" : 2
                        }

    class_prices = {
                    1 : 100,
                    2 : 250,
                    3 : 500,
                    4 : 1000,
                    5 : 1000
                    }

    ## CLASS PREFIXES ##

    class_prefixes = {
                    1 : "Beginner ",
                    2 : "Regular ",
                    3 : "Advanced ",
                    4 : "Elite ",
                    5 : "Elite "
                    }


    #### MODIFIERS ####

    ## PRICE MODIFIERS ##

    price_modifiers = {
                            "buy" : 1.0,
                            "sell" : 0.6,
                            "bargain" : 0.75,
#                             "buy item" : 1.0,
#                             "sell item" : 0.6
                            }

#     price_modifiers_trader = {
#                             "buy girl" : 0.9,
#                             "sell girl" : 0.7,
#                             "buy item" : 0.9,
#                             "bargain item" : 0.75,
#                             "sell item" : 0.7
#                             }

    ## ROLL MODIFIERS ##

    stat_bonus = {
                "primary" :  (4, 2.5, 1.5, 0),
                "secondary" : (2, 1.5, 1, 0),
                "booster" : (1.5, 1, 0.5, 0)
            }

    roll_modifier = {
                "critical success" : 1.3,
                "success" : 1.1,
                "neutral" : 1.0,
                "failure" : 0.9,
                "critical failure" : 0.7
            }

    ## TIP and REP ##

    helper_cost = {
                1 : 5,
                2 : 10,
                3 : 25,
                4 : 50,
                5 : 100
                }

    # max_upkeep = {
    #             1 : 75,
    #             2 : 250,
    #             3 : 500,
    #             4 : 1000,
    #             5 : 2000
    #             }



## XP and RANK ##


    ## LEVEL UP ##

    xp_to_levelup = {0 : 0}

    for i in range(1, 25):

        xp_to_levelup[i] = xp_to_levelup[i-1] + 10 * (i) ** 2

#        if i < 5:
#            xp_to_levelup[i] = xp_to_levelup[i-1] + 5 * (i + 1)

#        elif i < 10:
#            xp_to_levelup[i] = xp_to_levelup[i-1] + 15 * (i + 1)

#        elif i < 15:
#            xp_to_levelup[i] = xp_to_levelup[i-1] + 40 * (i + 1)

#        else:
#            xp_to_levelup[i] = xp_to_levelup[i-1] + 100 * (i + 1)


    ## MC LEVEL UP ##

    MC_xp_to_levelup = {0 : 0}

    for i in range(1, 26):

        MC_xp_to_levelup[i] = MC_xp_to_levelup[i-1] + 10 * i ** 2



    ## RANKS / JOB POINTS ##

    # Rank names #

    rank_name = {
                    1 : "C", #"{color=[c_white]}C{/color}",
                    2 : "B", #"{color=[c_yellow]}B{/color}",
                    3 : "A", #"{color=[c_lightblue]}A{/color}",
                    4 : "S", #"{color=[c_purple]}S{/color}",
                    5 : "X", #"{color=[c_gold]}X{/color}",
                    "waitress0": "Unskilled",
                    "waitress1": "Beginner Waitress",
                    "waitress2": "Competent Waitress",
                    "waitress3": "Skilled Barmaid",
                    "waitress4": "Expert Barmaid",
                    "waitress5": "Tavern Queen",
                    "dancer0": "Unskilled",
                    "dancer1": "Beginner Dancer",
                    "dancer2": "Competent Dancer",
                    "dancer3": "Skilled Stripper",
                    "dancer4": "Expert Stripper",
                    "dancer5": "Poledance Queen",
                    "masseuse0": "Unskilled",
                    "masseuse1": "Beginner Masseuse",
                    "masseuse2": "Competent Masseuse",
                    "masseuse3": "Skilled Massage girl",
                    "masseuse4": "Expert Massage girl",
                    "masseuse5": "Soapy Queen",
                    "geisha0": "Unskilled",
                    "geisha1": "Beginner Maiko",
                    "geisha2": "Competent Maiko",
                    "geisha3": "Skilled Geisha",
                    "geisha4": "Expert Geisha",
                    "geisha5": "Courtesan Queen",
                    "sex0" : "Unskilled",
                    "sex1" : "Beginner Prostitute",
                    "sex2" : "Competent Prostitute",
                    "sex3" : "Skilled Whore",
                    "sex4" : "Expert Whore",
                    "sex5" : "Brothel Queen",
                    "service0" : "Unskilled",
                    "service1" : "Beginner Wanker",
                    "service2" : "Competent Wanker",
                    "service3" : "Skilled Cocksucker",
                    "service4" : "Expert Cocksucker",
                    "service5" : "Blowjob Queen",
                    "anal0" : "Unskilled",
                    "anal1" : "Beginner Anal Slut",
                    "anal2" : "Competent Anal Slut",
                    "anal3" : "Skilled Butt Lover",
                    "anal4" : "Expert Butt Lover",
                    "anal5" : "Anal Queen",
                    "fetish0" : "Unskilled",
                    "fetish1" : "Beginner Servant",
                    "fetish2" : "Competent Servant",
                    "fetish3" : "Skilled Escort",
                    "fetish4" : "Expert Escort",
                    "fetish5" : "Bondage Queen",
                }


    jp_to_level = {
                    -1 : 0,
                    0 : 50,
                    1 : 125,
                    2 : 250,
                    3 : 425,
                    4 : 650,
                }

    job_up_dict = {
                    "waitress" : ("charm", "constitution", "beauty", "body"),
                    "dancer" : ("body", "libido", "charm", "refinement"),
                    "masseuse" : ("beauty", "sensitivity", "body", "refinement"),
                    "geisha" : ("refinement", "obedience", "charm", "beauty"),
                    "service" : ("service", "sensitivity", "charm", "fetish"),
                    "sex" : ("sex", "libido", "beauty", "service"),
                    "anal" : ("anal", "constitution", "body", "sex"),
                    "fetish" : ("fetish", "obedience", "refinement", "anal"),
                }

    job_up_change = {
                    1 : (5, 5, 0),
                    2 : (10, 5, 0),
                    3 : (15, 10, 5),
                    4 : (25, 15, 10),
                    5 : (40, 25, 15),
                }

    rep_to_rank = {
                    0 : 0,
                    1 : 10,
                    2 : 25,
                    3 : 50,
                    4 : 100,
                    5 : 1000,
                }

    rep_gains_dict = { # Read as: For a given girl rank - 'cust.rank relative to girl.rank (e.g: 'higher' = The customer has a higher rank) : must get a result >= X to earn rep'
                    1 : {"higher" : "bad", "same" : "average"},
                    2 : {"higher" : "bad", "same" : "average", "lower" : "good"},
                    3 : {"higher" : "average", "same" : "good", "lower" : "very good"},
                    4 : {"higher" : "average", "same" : "good", "lower" : "very good"},
                    5 : {"same" : "good", "lower" : "perfect"}, # Made easier for now
                }

    rep_loss_dict = { # Read as: 'must get a result < X to lose rep'. Being < to very bad is actually impossible
                    1 : {"higher" : "very bad", "same" : "bad"},
                    2 : {"higher" : "very bad", "same" : "bad", "lower" : "average"},
                    3 : {"higher" : "bad", "same" : "average", "lower" : "good"},
                    4 : {"higher" : "bad", "same" : "average", "lower" : "good"},
                    5 : {"same" : "average", "lower" : "very good"}, # Made easier for now
                }

#     rep_gains_dict = {
#                      1 : 6, # average score or better raises reputation
#                      2 : 6, # average score or better raises reputation
#                      3 : 9, # good score or better raises reputation
#                      4 : 9, # good score or better raises reputation
#                      5 : 12 # very good or better score raises reputation
#                      6 : 15 # perfe score raises reputation
#                      }

#     rep_loss_dict = {
#                      1 : -1, # very bad score damages reputation
#                      2 : -1, # very bad score damages reputation
#                      3 : 5, # bad score or lower damages reputation
#                      4 : 5, # bad score or lower damages reputation
#                      5 : 8 # average score or lower damages reputation
#                      }

    rank_cost = {
                    1 : 25,
                    2 : 100,
                    3 : 250,
                    4 : 1000,
                    5 : 2500,
                }

    jp_result_modifier = {
                        "very bad" : -2,
                        "bad" : -1,
                        "average" : 0,
                        "good" : 1,
                        "very good" : 2,
                        "perfect" : 4,
                    }

    jp_customer_rank_modifier = {
                                1 : 1,
                                2 : 2,
                                3 : 3,
                                4 : 4,
                                5 : 5,
                            }

    jp_job_level_modifier = { # JP are harder to get as girls raise in level
                            0 : 0,
                            1 : -1,
                            2 : -2,
                            3 : -3,
                            4 : -4,
                            5 : -5,
                        }



#### TRANSFORMS/EFFECTS ####

init:

    transform blink(_duration=0.5, _pause=2.0):
        on start:
            alpha 1.0
            linear _duration alpha 0.0
            linear _duration alpha 1.0
            pause _pause
            repeat

    transform myalpha(a):
            alpha a

    transform totheleft:
        xalign 0.2
        yalign 1.0

    transform totheright:
        xalign 0.8
        yalign 1.0

    transform centertextbox:
        xalign 0.5
        yanchor 1.0
        ypos 0.8

    transform centerleft:
        xalign 0.0
        yalign 0.5

    transform centerright:
        xalign 1.0
        yalign 0.5

    transform move_to(start_pos=(0,0), new_pos=(0,0), duration=0.6, fades=0.0): # Default: fades after moving

        pos start_pos xanchor 0.5 yanchor 1.0

        ease duration pos new_pos xanchor 0.5

        linear .5 alpha fades

    transform ninja_move:

        xanchor 0.0 yanchor 0.5

        xalign 0.75 yalign 0.4

        choice:
            ease 0.33 xalign 0.8 yalign 0.45

        choice:
            ease 0.33 xalign 0.7 yalign 0.45

        choice:
            ease 0.33 xalign 0.8 yalign 0.35

        choice:
            ease 0.33 xalign 0.7 yalign 0.35

        ease 0.33 xalign 0.75 yalign 0.4

        repeat

    transform rotate_y: # 3D y axis rotation
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 3.0 matrixtransform RotateMatrix(0.0, 360.0, 0.0)
        repeat

    transform disappear_in(s):
        pause s
        alpha 0

    transform flip_to_back:
        perspective True
        subpixel True
        matrixtransform RotateMatrix(0, 0, 0)
        linear 0.8 matrixtransform RotateMatrix(0, -180, 0)

    transform reverse_horizontal:
        subpixel True
        zpos 1
        matrixtransform RotateMatrix(0, 180, 0)

    transform jitter(start_pos=(0.5, 0.5), adj=0.005, t=0.4):
        ease t zoom 1.0 # align start_pos  matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease t zoom 0.92 # align randomize_align(adj) matrixtransform RotateMatrix(*randomize_matrix())
        repeat

    transform bounce(start_pos=(0.5, 0.5), adj=0.005, t=0.4):
        zoom 1.0
        ease t zoom 1.25 # align randomize_align(adj) matrixtransform RotateMatrix(*randomize_matrix())
        ease t zoom 0.92 # align start_pos  matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    transform repeat_bounce():
        zoom 1.0
        linear 1.0 zoom 0.8
        linear 0.5 zoom 1.0
        repeat

    transform shake(t=0.4, degrees=15):
        rotate 0
        ease t rotate degrees
        ease t rotate -degrees
        ease t rotate 0
        repeat


    $ quake = Move((0, 20), (20, -15), 0.05+renpy.random.random()*.15, bounce=True, repeat=True, delay=1.0)

    $ define.move_transitions("smove", 2.0)

    transform jumping:
        linear 0.1 yoffset -50
        linear 0.1 yoffset 0

    transform fadeinout(y_offset=0):
        xanchor 0.0
        yanchor 0.0
        xpos 1.0
        ypos 0 + y_offset
        alpha 0.0
        ease 2.5 xalign 1.0 alpha 1.0
        pause 2.0
        ease 2.5 xalign 1.5 alpha 0.0

    transform fademove(from_tup, to_tup): # Moves from coordinates from_tup to to_tup while fading

        on show:
            xanchor 0.5
            yanchor 0.5
            xalign from_tup[0]
            yalign from_tup[1]

            pause 1.0

            ease 1.5  xalign to_tup[0] yalign to_tup[1] alpha 0.0

    transform burn_card(xs, ys):

        pause 0.3

        AlphaMask(Frame("transitions/flames.webp", xsize=xs, ysize=ys), Frame("UI/powers/cards/front_Bronze.webp", xsize=xs, ysize=ys))
        alpha 0.0
        linear 0.8 alpha 1.0


    # Speed
    image speed_effect:
        im.Scale("transitions/speed.webp", config.screen_width, config.screen_height)
        xpan 180
        xalign 0
        yalign 0
        linear 0.5 xpan -180
        xalign 0
        yalign 0
        repeat

    # Rain
    image rev_lightning = im.Flip("minigame/rain/lightning.webp", horizontal=True)

    image rain:
        zoom 2.0

        "minigame/rain/heavyrain1.webp"
        0.1
        "minigame/rain/rain1.webp"
        0.1
        "minigame/rain/heavyrain2.webp"
        0.1
        "minigame/rain/rain3.webp"
        0.1
        "minigame/rain/rain2.webp"
        0.1
        "minigame/rain/heavyrain3.webp"
        0.1
        repeat

    image lightning:
        zoom 3.0
        yalign 0.0

        choice:   #weight of choice is 0.1
            "minigame/rain/lightning.webp" with vpunch
            xalign 0.0
            alpha  0.0
            linear 0.6 alpha  1.0
            linear 0.6 alpha  0.0

        choice:
            "rev_lightning" with vpunch
            xalign 1.0
            alpha  0.0
            linear 0.6 alpha  1.0
            linear 0.6 alpha  0.0

        repeat

    image static:
        "noise1" with Dissolve(0.3, alpha=True)
        0.3
        "noise2" with Dissolve(0.2, alpha=True)
        0.2
        "noise3" with Dissolve(0.4, alpha=True)
        0.4
        "noise4" with Dissolve(0.1, alpha=True)
        0.1
        "noise1" with Dissolve(0.2, alpha=True)
        0.2
        "noise2" with Dissolve(0.1, alpha=True)
        0.1
        "noise3" with Dissolve(0.3, alpha=True)
        0.3
        "noise4" with Dissolve(0.4, alpha=True)
        0.4
        repeat

    image supercharge_card:
        subpixel True
        "UI/powers/supercharge/card_supercharge/sc_1.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_2.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_3.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_4.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_5.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_6.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_7.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_8.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_9.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_10.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_11.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_12.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_13.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_14.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_15.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_16.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_17.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_18.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_19.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_20.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_21.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_22.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_23.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_24.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_25.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_26.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_27.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_28.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_29.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_30.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_31.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_32.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_33.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_34.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_35.webp"
        pause 0.06
        "UI/powers/supercharge/card_supercharge/sc_36.webp"
        pause 0.06
        repeat

    image supercharge:
        subpixel True
        pause 0.1
        "UI/powers/supercharge/screen_supercharge/supercharge-1.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-2.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-3.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-4.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-5.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-6.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-7.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-8.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-9.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-10.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-11.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-12.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-13.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-14.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-15.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-16.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-17.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-18.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-19.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-20.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-21.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-22.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-23.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-24.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-25.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-26.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-27.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-28.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-29.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-30.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-31.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-32.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-33.webp"
        pause 0.02
        "UI/powers/supercharge/screen_supercharge/supercharge-placeholder.webp"

    # Mojos
    image mojo_green:
        "UI/Powers/orb_green.webp"
        size res_tb(25)
    image mojo_blue:
        "UI/Powers/orb_blue.webp"
        size res_tb(25)
    image mojo_red:
        "UI/Powers/orb_red.webp"
        size res_tb(25)
    image mojo_yellow:
        "UI/Powers/orb_yellow.webp"
        size res_tb(25)
    image mojo_purple:
        "UI/Powers/orb_purple.webp"
        size res_tb(25)

    # Evil spell splash screen
    image evil_spell:
        "UI/Powers/Evil spell.webp"
        zoom 0.4

    image princess fucked: ## There really must be a shorter way to do this, but I've had no luck so far

        "NPC/Misc/princess/princess fucked1.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked2.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked3.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked4.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked5.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked6.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked7.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked8.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked9.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked10.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked11.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked12.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked13.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked14.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked15.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked16.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked17.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked18.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked19.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked20.gif"
        pause 0.03
        "NPC/Misc/princess/princess fucked21.gif"
        pause 0.03
        repeat



#### COLORS #### Shortcuts for color codes used in the game

init -5 python:

    c_default = "#D96B00" #"#D67229"

    c_white = "#FFFFFF"

    c_black = "#000000"

    c_grey = "#ADB9CC"

    c_lightgrey = "#D3D3D3"

    c_steel = "#4682B4"

    c_main = "#00BFFF"

    c_darkred = "#8B0000"

    c_darkblue = "#00008b"

    c_grey_blue = "#5d5ea0"

    c_darkgrey = "#1A2B47"

    c_hotpink = "#FF69B4"

    c_pink = "#FFC0CB"

    c_orange_pink = "#FF6666"

    c_gold = "#FFD700"

    c_darkgold = "#B8860B"

    c_blue = "#0000FF"

    c_lavender = "#E6E6FA"

    c_lightblue = "#6699ff" #"#00BFFF"

    c_copper = "#CC3300"

    c_red = "#FF0000"

    c_lightred = "#F78181"

    c_redpink = "#cc0052"

    c_yellow = "#FFFF33"

    c_blonde = "#FCF3CF"

    c_cream = "#FDF1B8"

    c_brown = "#502F13"

    c_lightbrown = "#D2B48C"

    c_darkbrown = "#502F13"

    c_lightprune = "#F1D4F1"

    c_prune = "#811453"

    c_darkprune = "#32274d"

    c_magenta = "#A41CC6"

    c_lightmagenta = "#FF33FF" # pink

    c_purple = "#9933FF"

    c_softpurple = "#9683EC"

    c_darkpurple = "#3D007A"

    c_orange = "#FF9900" # #FD9B1C

    c_lightorange = "#FFCC66"

    c_darkorange = "#D67229"

    c_emerald = "#009874"

    c_lightgreen = "#66FF99"

    c_darkgreen = "#003333"

    c_green = "#00B050"

    c_turquoise = "#30DADD"

    c_sapphire = "#0F52BA"

    c_azure = "#B7DBFF"

    c_crimson = "#DC143C"

    c_firered = "#B22222"

    c_violet = "#C71585"

    c_ui_unlocked = c_orange

    c_ui_sensitive = c_white

    c_ui_insensitive = c_lightgrey

    c_ui_dark = "#00000066" # "#000000CC" "#22222288"

    c_ui_darker = "#000000CC"

    c_ui_darkblue = "#000022AA"

    c_ui_brown = "#D2B48CCC"

    c_ui_light = "#FFECBFDD"

    c_ui_light_solid = "#FFECBF"

    all_colors = [c for c in dir(renpy.store) if c.startswith("c_")]

## COLOR DICTIONARY

    color_dict = { # Event colors
        "special": c_orange,
        "good": c_green,
        "a little good": c_lightgreen,
        "average": c_yellow,
        "average contrast": c_darkorange,
        "a little bad": c_lightred,
        "a little bad contrast": c_redpink,
        "bad": c_red,
        "very bad": c_crimson,
        "fear": c_purple,
        "gold": c_gold,
        "xp" : c_lightgreen,
        "jp" : c_orange,
        "rep": c_softpurple,
        "normal": c_white,
        "normal contrast": c_black,


        "+++" : c_emerald,
        "++" : c_green,
        "+" : c_lightgreen,

        "=" : c_white,

        "---" : c_crimson,
        "--" : c_red,
        "-" : c_lightred,

        "love +++" : c_hotpink,
        "love ++" : c_hotpink,
        "love +" : c_hotpink,
        "love -" : c_red,

        "fear +++" : c_softpurple,
        "fear ++" : c_softpurple,
        "fear +" : c_softpurple,
        "fear -" : "#A6DEEE",

        "special" : c_orange,
        "special contrast" : c_softpurple,
        "average" : c_yellow,
        "leveling" : c_steel,
        "normal" : c_white,
    }



## MODS ##

    detected_mods = {}

    if persistent.mods is None:
        persistent.mods = {}

    mod_traceback = ""
    updated_games = defaultdict(bool)


init -2 python:
    contract_level = {2 : [1], 3 : [1, 2], 4 : [2], 5 : [2, 3], 6 : [3, 4], 7 : [4]} # Picks randomized task number according to chapter
    contract_value = {2 : 250, 3 : 500, 4 : 625, 5 : 1000, 6 : 1250, 7 : 1600} # Base value for contract rewards. Min-Max payout is 2-4 times base value for each successful task (not taking Special bonuses into account)

    contract_skill_limit = {2 : {"easy" : 75, "hard" : 100}, 3 : {"easy" : 100, "hard" : 125}, 4 : {"easy" : 125, "hard" : 150},
                            5 : {"easy" : 150, "hard" : 175}, 6 : {"easy" : 175, "hard" : 225}, 7 : {"easy" : 225, "hard" : 275}}
    contract_sex_limit =   {
                            2: {"easy": "a little reluctant", "hard": "indifferent"},
                            3: {"easy": "indifferent", "hard": "a little interested"},
                            4: {"easy": "a little interested", "hard": "interested"},
                            5: {"easy": "interested", "hard": "very interested"},
                            6: {"easy": "very interested", "hard": "fascinated"},
                            7: {"easy": "very interested", "hard": "fascinated"},
                        }

    # ORG/org = Organizer, VEN/ven = venue, AVEN/aven = article + venue, LOC/loc = location, DIS/dis = district

    contract_description = {"cruise" : ":ORG: is organizing a nightly cruise tour of :dis: to thank its members for their hard work this year. :AVEN: will depart for a sightseeing tour of the bay at dusk, then moor next to the :LOC: for a night of entertainment.",
                            "party" : ":ORG: is throwing a lavish party in :aven: near the :LOC:. Everyone who is anyone in Zan is expected to attend and party until well after dawn.",
                            "ceremony" : ":ORG: chose :aven: near the :LOC: to celebrate one of their numerous holy days. In order to get closer to their deity, worshippers are expected to transcend both spirit and flesh by indulging in the most shameful pleasures, washing away their sins with large amounts of holy alcohol, conveniently sold on the premises by the Church.",
                            "festival" : ":ORG: is throwing a huge festival next month in :dis:, to celebrate a new season, a three-headed cow, the sun rising again, or some other redneck nonsense. Still, there will be a big feast at :aven: near the :LOC: complete with food, drinks, shows and of course, girls!",
                            "date" : ":ORG: has invited a few friends to :aven: next to the :LOC: for the night, and has requested some company. Well-groomed, well-behaved female servants are expected to tend to his every need.",
                            "meeting" : ":ORG: convened a meeting of like-minded nobles and diplomats to discuss :ven: in a discreet venue near the :LOC:. While the intricacies of this grave topic will occupy much of their time, they will also expect their hosts to provide top-notch service and ways of 'relieving' the tension.",
                            "magic" : ":ORG: summoned all arcane users to a night of fun and magic out in the :LOC:. Tended to by beautiful women, the guests will attend special events in :aven:, overlooking the magnificence of :DIS:.",
                            "orgy" : ":ORG: is happy to announce a long night of hedonism and erotic surprises in the :LOC:. Gathered in :aven:, the guests will enjoy forbidden pleasure with like-minded individuals and a hand-picked selection of elite sex slaves."
                        }

init python:

    contract_task_types_order = {"greet" : 1, "serve" : 2, "mingle" : 3, "event" : 4, "private show" : 5, "fun" : 6}
    contract_task_types_description = {"greet" : "Greet Guests", "serve" : "Serve Guests", "mingle" : "Socialize", "event" : "Participate In An Event", "private show" : "Deliver A Private Show", "fun" : "Have 'Fun'"}

    contract_tasks = [
                        ContractTask("clean", type="serve", requirements=["job waitress", "skill obedience", "skill constitution", ], tags=(["maid"], ["obedience"], ["waitress"], ["profile"])),
                        ContractTask("serve guests", type="serve", requirements=["job waitress", "skill beauty", "skill charm", "skill obedience", ], tags=(["waitress"], ["profile"])),
                        ContractTask("serve drinks", type="serve", requirements=["job waitress", "skill beauty", "skill charm", "skill constitution", ], tags=(["waitress"], ["profile"])),
                        ContractTask("feed guests", type="serve", requirements=["job waitress", "job geisha", "skill charm", "skill obedience", ], tags=(["waitress", "geisha"], ["profile"])),
                        ContractTask("onsen", type="mingle", requirements=["job masseuse", "skill beauty", "skill body", "skill charm", "skill obedience", "skill constitution", ], tags=(["masseuse"], ["swim"], ["profile"])),
                        ContractTask("swimming pool", type="mingle", requirements=["job masseuse", "skill beauty", "skill body", "skill charm", ], tags=(["swim"], ["masseuse"], ["profile"])),
                        ContractTask("swimming show", type="event", requirements=["job masseuse", "skill beauty", "skill body", "skill constitution", ], tags=(["swim"], ["profile"]), and_tags=["rest"]),
                        ContractTask("lingerie show", type="event", requirements=["job dancer", "skill body", "skill refinement", "skill libido", ], tags=(["profile"]), and_tags=["libido"]),
                        ContractTask("entice guests", type="greet", requirements=["job dancer", "skill beauty", "skill charm", "skill refinement", "skill libido", ], tags=(["model"], ["profile"]), and_tags=["libido"]),
                        ContractTask("dance show", type="private show", requirements=["job dancer", "skill body", "skill refinement", "skill constitution", ], tags=(["dance"], ["profile"])),
                        ContractTask("erotic show", type="private show", requirements=["job dancer", "skill body", "skill libido", "skill constitution", ], tags=(["dance"], ["profile"]), and_tags=["libido"]),
                        ContractTask("cosplay", type="mingle", requirements=["job waitress", "job dancer", "skill charm", "skill libido", ], tags=(["cosplay"], ["dance"], ["profile"])),
                        ContractTask("lap dance", type="private show", requirements=["job dancer", "skill body", "skill obedience", "skill libido", ], tags=(["dance"], ["profile"]), and_tags=["libido"]),
                        ContractTask("welcome massage", type="greet", requirements=["job masseuse", "skill beauty", "skill charm", ], tags=(["masseuse"], ["profile"])),
                        ContractTask("erotic massage", type="serve", requirements=["job masseuse", "skill beauty", "skill charm", "skill libido", ], tags=(["masseuse"], ["profile"]), and_tags=["libido"]),
                        ContractTask("conversation", type="mingle", requirements=["job geisha", "skill beauty", "skill charm", "skill refinement", ], tags=(["geisha"], ["profile"])),
                        ContractTask("protocol", type="greet", requirements=["job geisha", "skill charm", "skill refinement", "skill obedience", ], tags=(["geisha"], ["profile"])),
                        ContractTask("ceremony", type="mingle", requirements=["job geisha", "skill beauty", "skill refinement", ], tags=(["geisha"], ["profile"])),
                        ContractTask("welcome guests", type="greet", requirements=["job geisha", "skill charm", "skill obedience", ], tags=(["geisha"], ["profile"])),
                        ContractTask("kiss guests", type="greet", requirements=["skill beauty", "skill refinement", "skill libido", ], tags=(["kiss"], ["profile"])),
                        ContractTask("catwalk", type="event", requirements=["skill beauty", "skill refinement", ], tags=(["model"], ["dance"], ["profile"])),
                        ContractTask("catfight", type="event", requirements=["skill body", "skill constitution", ], tags=(["fight"], ["dance"], ["profile"])),
                        ContractTask("art model", type="mingle", requirements=["skill beauty", "skill refinement", "skill obedience", ], tags=(["model"], ["profile"])),
                        ContractTask("sub greeting", type="greet", requirements=["skill refinement", "skill obedience", ], tags=(["sub"], ["profile"])),
                        ContractTask("dom greeting", type="greet", requirements=["skill refinement", "skill libido", "skill constitution", ], tags=(["dom"], ["profile"])),
                        ContractTask("sports show", type="event", requirements=["skill body", "skill constitution", ], tags=(["constitution"], ["profile"])),
                        ContractTask("fondle", type="mingle", requirements=["job masseuse", "skill body", "skill charm", "skill libido", ], tags=(["fondle", "grope"], ["profile"])),
                        ContractTask("strip", type="private show", requirements=["skill beauty", "skill body", "skill refinement", "skill libido", ], tags=(["strip"], ["naked"]), soft="naked"),
                        ContractTask("nude help", type="mingle", requirements=["skill body", "skill charm", "skill obedience", ], tags=(["waitress"], ["geisha"], ["profile"]), and_tags=["naked"], soft="naked"),
                        ContractTask("naked", type="fun", requirements=["skill body", "skill libido", ], tags=(["naked"]), and_tags2 = ["cum shower"], soft="naked"),
                        ContractTask("masturbate", type="private show", requirements=["job service", "skill constitution", "skill service", "pref service", ], tags=(["service"], ["naked"]), and_tags=["mast"], soft=False),
                        ContractTask("barmaid blowjob", type="serve", requirements=["job waitress", "job service", "skill charm", "skill service", "pref service", ], tags=(["waitress"], ["service"], ["naked"]), and_tags=["service"], soft=False),
                        ContractTask("service", type="fun", requirements=["job service", "skill service", "pref service", ], tags=(["service"], ["naked"]), and_tags2 = ["cim"], soft=False),
                        ContractTask("cosplay sex", type="event", requirements=["job sex", "skill libido", "skill sex", "pref sex", ], tags=(["cosplay"], ["sex"], ["naked"]), and_tags=["sex"], soft=False),
                        ContractTask("full service massage", type="serve", requirements=["job masseuse", "job sex", "skill beauty", "skill sex", "pref sex", ], tags=(["masseuse"], ["sex"], ["naked"]), and_tags=["sex"], soft=False),
                        ContractTask("sex", type="fun", requirements=["job sex", "skill libido", "skill sex", "pref sex", ], tags=(["sex"], ["naked"]), and_tags2 = ["creampie"], soft=False),
                        ContractTask("cosplay anal", type="event", requirements=["job anal", "skill obedience", "skill constitution", "skill anal", "pref anal", ], tags=(["cosplay"], ["anal"], ["naked"]), and_tags=["anal"], soft=False),
                        ContractTask("anal dance", type="private show", requirements=["job dancer", "job anal", "skill constitution", "skill anal", "pref anal", ], tags=(["dancer"], ["anal"], ["naked"]), and_tags=["anal"], soft=False),
                        ContractTask("anal", type="fun", requirements=["job anal", "skill constitution", "skill anal", "pref anal", ], tags=(["anal"], ["naked"]), and_tags2 = ["cob"], soft=False),
                        ContractTask("toy", type="private show", requirements=["job fetish", "skill obedience", "skill fetish", "pref fetish", ], tags=(["fetish"], ["naked"]), and_tags=["toy"], soft=False),
                        ContractTask("geisha bondage", type="event", requirements=["job geisha", "job fetish", "skill refinement", "skill fetish", "pref fetish", ], tags=(["geisha"], ["fetish"], ["naked"]), and_tags=["fetish"], soft=False),
                        ContractTask("fetish", type="fun", requirements=["job fetish", "skill obedience", "skill fetish", "pref fetish", ], tags=(["fetish"], ["naked"]), and_tags2 = ["cof"], soft=False),
                        ContractTask("group sex", type="fun", requirements=["job sex", "skill libido", "skill sex", "pref sex", ], tags=(["sex"], ["group"], ["naked"]), and_tags=["group"], and_tags2 = ["group", "bukkake"], soft=False),
                        ContractTask("group anal", type="fun", requirements=["job anal", "skill constitution", "skill anal", "pref anal", ], tags=(["anal"], ["group"], ["naked"]), and_tags=["group"], and_tags2 = ["group", "cum shower"], soft=False),
                        ContractTask("bisexual service", type="fun", requirements=["job service", "skill service", "pref service", ], tags=(["service"], ["bisexual"], ["naked"]), and_tags=["bisexual"], and_tags2=["bisexual", "orgasm"], soft=False),
                        ContractTask("bisexual fetish", type="fun", requirements=["job fetish", "skill obedience", "skill fetish", "pref fetish", ], tags=(["fetish"], ["bisexual"], ["naked"]), and_tags=["bisexual"], and_tags2=["bisexual", "squirt"], soft=False),
]

    contract_specials = [("trait", 3), ("perk", 2), ("fix", 3), ("farm", 1), ("item", 1)]

    contract_stage_modifier = {1 : 1, 2 : 1.5, 3 : 3, 4 : 6}

# init -1 python:
#     init_galleries()

## END OF BK INIT VARIABLES FILE ##
