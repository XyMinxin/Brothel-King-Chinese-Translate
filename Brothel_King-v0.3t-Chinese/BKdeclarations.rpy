####            CHARACTER AND IMAGE DECLARATIONS                ####
##      All BKing character, image and transition declarations    ##
##              Includes the code for the CG Gallery              ##
####                                                            ####

## Removing black or white background from jpg with paint.net (so I don't forget):
## Select black or white area, delete, use Object / 'old feather' or feather effect then Photo / Sharpen effect

####                            ####
##      CHARACTER DECLARATION     ##
####                            ####

# Declare characters used by this game.

#### INTRO ####

## SYSTEM ##

define bk_error = Character("ERROR", color=c_red)

# Special emoji characters not supported by the new font
define emo_heart = "{font=DejaVuSans.ttf}❤{/font}"
define emo_lightning = "{font=DejaVuSans.ttf}⚡{/font}"
define emo_yang = "{font=DejaVuSans.ttf}☯{/font}"

## MC ##
define you = DynamicCharacter("MC.name", color=c_steel)


## SILL ##
define sill = DynamicCharacter("sill_name", color=c_hotpink, image = "sill", window_left_padding=int(config.screen_height*0.205)) #show_two_window=True,


## KUROHIME ##
define kuro = DynamicCharacter("kuro_name", color = c_lightprune, image = "kuro", window_left_padding=int(config.screen_height*0.205))
define kurohime = kuro


## MAID ##
define maid = DynamicCharacter("maid_name", color = c_softpurple, image = "maid", window_left_padding=int(config.screen_height*0.205))


## GIO ##
define gio = Character("Gio", color = c_orange, image = "gio", window_left_padding=int(config.screen_height*0.205))


## MISC ##
define guard = Character("卫兵", color= c_yellow, image = "guard", window_left_padding=int(config.screen_height*0.205))
define thug1 = Character("暴徒", color= c_lightgreen, image = "thug1", window_left_padding=int(config.screen_height*0.205))
define thug2 = Character("暴徒", color= c_red, image = "thug2", window_left_padding=int(config.screen_height*0.205))
define thug3 = Character("暴徒", color= c_lightred, image = "thug", window_left_padding=int(config.screen_height*0.205))
define drogon = Character("龙-卓耿", color= c_darkred, image = "drogon", window_left_padding=int(config.screen_height*0.205))
define security = Character("Security", color= c_white, image = "security", window_left_padding=int(config.screen_height*0.205))
define security_breach = Character("安全事件", color= c_red, image = "security_breach", window_left_padding=int(config.screen_height*0.205))
define programmer = Character("安全事件", color = c_lightblue, image="crying_man", window_left_padding=int(config.screen_height*0.205))


#### SCREEN CHARACTERS ####

define slavegirl1 = Character("奴隶训练师", color = c_crimson, image = "slavegirl1", window_left_padding=int(config.screen_height*0.205))
define slavegirl2 = Character("女奴-美琪", color = c_violet, image = "slavegirl2", window_left_padding=int(config.screen_height*0.205))
define shopgirl = Character("风情万种的老板娘", color = c_pink, image = "shopgirl", window_left_padding=res_portrait_size)
define jobgirl = DynamicCharacter("jobgirl_name", color = c_firered, image = "jobgirl", window_left_padding=int(config.screen_height*0.205))
define bast = DynamicCharacter("bast_name", color = c_copper, image = "bast", window_left_padding=int(config.screen_height*0.205))
define banker = DynamicCharacter("banker_name", color=c_turquoise, image = "banker", window_left_padding=int(config.screen_height*0.205))
define taxgirl = DynamicCharacter("taxgirl_name", color=c_turquoise, image = "taxgirl", window_left_padding=int(config.screen_height*0.205))


#### FARM AND MERCHANT CHARACTERS ####

# Gizel
define gizel = DynamicCharacter("gizel_name", color=c_magenta, image = "gizel", window_left_padding=int(config.screen_height*0.205))

# City merchants (Characters are also defined as NPCs in 'BKstart')
define stella = DynamicCharacter("stella_name", color=c_lightmagenta, image="stella", window_left_padding=int(config.screen_height*0.205))
define goldie = DynamicCharacter("goldie_name", color=c_yellow, image="goldie", window_left_padding=int(config.screen_height*0.205))
define willow = DynamicCharacter("willow_name", color=c_copper, image="willow", window_left_padding=int(config.screen_height*0.205))
define gina = DynamicCharacter("gina_name", color=c_softpurple, image="gina", window_left_padding=int(config.screen_height*0.205))

define riche = DynamicCharacter("riche_name", color=c_azure, image="riche", window_left_padding=int(config.screen_height*0.205))
define ramias = DynamicCharacter("ramias_name", color=c_lightgrey, image="ramias", window_left_padding=int(config.screen_height*0.205))
define giftgirl = Character("礼物商店女孩", color=c_hotpink, image="giftgirl", window_left_padding=int(config.screen_height*0.205))
define gurigura = DynamicCharacter("gurigura_name", color=c_yellow, image="gurigura", window_left_padding=int(config.screen_height*0.205))
define katryn = DynamicCharacter("katryn_name", color=c_lightgreen, image="katryn", window_left_padding=int(config.screen_height*0.205))
define today = DynamicCharacter("today_name", color=c_turquoise, image="today", window_left_padding=int(config.screen_height*0.205))
define yesterday = DynamicCharacter("yesterday_name", color=c_turquoise, image="yesterday", window_left_padding=int(config.screen_height*0.205))

# Extras
define templar = Character("圣殿骑士", color=c_lightgrey, image="templar", window_left_padding=int(config.screen_height*0.205))
define initiate = Character("新兵", color=c_white, image="initiate", window_left_padding=int(config.screen_height*0.205))
define initiate1 = Character("第一位新兵", color=c_lightblue, image="initiate", window_left_padding=int(config.screen_height*0.205))
define initiate2 = Character("第二位新兵", color=c_lightred, image="initiate", window_left_padding=int(config.screen_height*0.205))
define spirit = Character("黑暗灵体", color=c_white, image="spirit", window_left_padding=int(config.screen_height*0.205))
define milkmaid = Character("挤奶女工", color=c_pink, image="milkmaid", window_left_padding=int(config.screen_height*0.205))
define relative = Character("薇洛相关者", color=c_copper)
define blood1 = Character("金发警官", color=c_yellow, image="blood1", window_left_padding=int(config.screen_height*0.205))
define blood2 = Character("赤褐色头发的警官", color=c_copper, image="blood2", window_left_padding=int(config.screen_height*0.205))

#### STORY (Chapter 1) ####

define character.kosmo = DynamicCharacter("kosmo_name", color=c_gold, image = "kosmo", window_left_padding=int(config.screen_height*0.205))
define sergeant = DynamicCharacter("sergeant_name", color=c_copper, image = "sergeant", window_left_padding=int(config.screen_height*0.205))
define maya = DynamicCharacter("maya_name", color=c_firered, image = "maya", window_left_padding=int(config.screen_height*0.205))
define roz = Character("罗兹", color=c_firered, image = "roz", window_left_padding=int(config.screen_height*0.205))
define lieutenant = DynamicCharacter("lieutenant_name", color = "#C06A45", image = "lieutenant", window_left_padding=int(config.screen_height*0.205))
define renza = DynamicCharacter("renza_name", color=c_orange_pink, image = "renza", window_left_padding=int(config.screen_height*0.205))
define satella = DynamicCharacter("satella_name", color=c_copper, image = "satella", window_left_padding=int(config.screen_height*0.205))
define captain = DynamicCharacter("captain_name", color=c_emerald, image = "captain", window_left_padding=int(config.screen_height*0.205))


#### STORY (Chapter 2) ####

define shalia = DynamicCharacter("shalia_name", color=c_softpurple, image = "shalia", window_left_padding=int(config.screen_height*0.205))
define carpenter = DynamicCharacter("carpenter_name", color=c_firered, image = "carpenter", window_left_padding=int(config.screen_height*0.205))
define kenshin = DynamicCharacter("kenshin_name", color=c_copper, image = "kenshin", window_left_padding=int(config.screen_height*0.205))
define homura = DynamicCharacter("homura_name", color=c_purple, image = "homura", window_left_padding=int(config.screen_height*0.205))
define suzume = DynamicCharacter("suzume_name", color=c_lightblue, image = "suzume", window_left_padding=int(config.screen_height*0.205))
define narika = DynamicCharacter("narika_name", color=c_hotpink, image = "narika", window_left_padding=int(config.screen_height*0.205))
define mizuki = DynamicCharacter("mizuki_name", color=c_azure, image = "mizuki", window_left_padding=int(config.screen_height*0.205))
define haruka = DynamicCharacter("haruka_name", color=c_yellow, image = "haruka", window_left_padding=int(config.screen_height*0.205))
define kunoichi = Character("女忍者", color=c_red, image = "kunoichi", window_left_padding=int(config.screen_height*0.205))
define papa_apprentice = Character("Apprentice", color=c_softpurple, image = "papa_apprentice", window_left_padding=int(config.screen_height*0.205))
define papa = Character("怪胎爸爸", color=c_lightblue, image = "papa", window_left_padding=int(config.screen_height*0.205))
define hokoma_warrior = Character("凶猛的女人", color=c_prune, image = "hokoma_warrior")
define magical_girl = Character("奇怪的女孩", color=c_emerald, image = "magical_girl")
define girl_scientist = Character("书呆子女孩", color=c_firered, image = "girl_scientist")

#### STORY (Chapter 3) ####
define chaos = DynamicCharacter("chaos_name", color=c_lightmagenta, image = "chaos", window_left_padding=int(config.screen_height*0.205))

#### MISC. CHARACTERS ####

## GENERIC EVENT CHARACTERS ##

define ev_girl1 = Character("女孩", color= c_pink)
define ev_girl2 = Character("女孩", color= c_gold)
define ev_girl3 = Character("女孩", color= c_lightblue)
define ev_girl4 = Character("女孩", color= c_white)
define woman = Character("女人", color= c_violet)
define slave = Character("女奴", color= c_softpurple)
define warrior = Character("战士", color= c_firered)
define yuna = Character("尤娜", color= c_lightgrey)
define man = Character("男人", color= c_cream)
define man2 = Character("另一个男人", color= c_lightgrey)
define passerby = Character("路人", color = c_lightblue)
define demonette = Character("女恶魔", color = c_softpurple, image = "demonette", window_left_padding=res_portrait_size)
define demon = Character("恶魔", color=c_lightred, image = "red_demon", window_left_padding=res_portrait_size)
define hanny = Character("汉娜", color=c_lightbrown, image = "hanny", window_left_padding=res_portrait_size)

## STORY EXTRAS ##

define hmas_girl = Character("神秘的女孩", color = c_emerald, image = "hmas", window_left_padding=int(config.screen_height*0.205))
define sewer_woman = Character("女人", color=c_grey_blue, image = "sewer_woman", window_left_padding=int(config.screen_height*0.205))

define mthug = Character("蒙面暴徒", color=c_white)
define captain_voice = Character("队长的声音", color=c_emerald)
define judge = Character("首席法官", color=c_lightgreen, image = "judge", window_left_padding=int(config.screen_height*0.205))
define knight = Character("骑士", color=c_softpurple, image = "knight", window_left_padding=int(config.screen_height*0.205))
define mask = DynamicCharacter("mask_name", color=c_copper, image = "mask", window_left_padding=int(config.screen_height*0.205))

define raccoon = Character("浣熊", color=c_yellow, image = "raccoon", window_left_padding=int(config.screen_height*0.205))
define akuma = Character("豪鬼", color=c_steel, image = "blue_demon", window_left_padding=int(config.screen_height*0.205))
define gouki = Character("刚鬼", color=c_lightred, image = "red_demon", window_left_padding=int(config.screen_height*0.205))
define rodrigo = Character("罗德里格(骷髅)", color=c_lightgrey, image = "skeleton", window_left_padding=int(config.screen_height*0.205))


## CONTRACT CHARACTERS ##

define sailor = Character("水手", color=c_copper, image = "sailor", window_left_padding=int(config.screen_height*0.205))
define party_girl = Character("派对女孩", color=c_lightred, image = "party_girl", window_left_padding=int(config.screen_height*0.205))
define nun = Character("修女", color=c_grey_blue, image = "nun", window_left_padding=int(config.screen_height*0.205))
define kimono_lady = Character("和服女士", color=c_softpurple, image = "kimono_lady", window_left_padding=int(config.screen_height*0.205))
define young_maid = Character("年轻女仆", color=c_yellow, image = "young_maid", window_left_padding=int(config.screen_height*0.205))
define diplomat = Character("女外交官", color=c_orange_pink, image = "diplomat", window_left_padding=int(config.screen_height*0.205))
define sorceress = Character("女巫", color=c_lightgrey, image = "sorceress", window_left_padding=int(config.screen_height*0.205))
define naked_lady = Character("裸女", color=c_cream, image = "naked_lady", window_left_padding=int(config.screen_height*0.205))


####                            ####
##      IMAGES AND TRANSITIONS    ##
####                            ####


init -2 python:

## Images are declared using an auto-generating function

    def declare(name, img, method=None, x=config.screen_width, y=config.screen_height, wide=False, gallery=True, unlock=False): # img is the complete image path (from the game folder root)

        if wide: # Only matters for 4:3 resolution
            if not screen_is_wide:
                y = int(y*0.8)

        if is_videofile(img):
            renpy.image(name, Movie(img, play=img, size=(x, y)))

        elif method == "s": # Scale method (image will fit the exact target dimensions - not proportional)
            renpy.image(name, im.Scale(img, x, y))

        elif method == "p": # ProportionalScale method (image will fit the target dimensions while preserving its aspect ratio)
            renpy.image(name, ProportionalScale(img, x, y))

        elif method == "f": # Factor Scale (image dimensions will change proportionately to float numbers x and y)

            # Foolproofing
            if x == config.screen_width:
                x = 1.0
            if y == config.screen_height:
                y = 1.0

            x *= new_res_ratio
            y *= new_res_ratio

            renpy.image(name, im.FactorScale(img, x, y))

        elif method in ("tall", "med", "small"): # Tailor-made adjustments for character bodies
            y_ratio = {"tall" : 0.85, "med" : 0.72, "small" : 0.6}[method]

            renpy.image(name, ProportionalScale(img, None, y_ratio*config.screen_height))

        elif method == "pf": # Combines ProportionalScale method and Factor Scale method (based on screen resolution)
            renpy.image(name, ProportionalScale(img, int(x*config.screen_width), int(y*config.screen_height)))

        else: # No change to the original image
            renpy.image(name, im.FactorScale(img, new_res_ratio, new_res_ratio))

        if unlock:
            unlock_pic(name, silent=True)

        if gallery: # Returns image name if the image is to be stored in a gallery
            return name
        else:
            return None

    def declare_multiple(base_name, base_img, method=None, start=0, finish=0, series=None, x=config.screen_width, y=config.screen_height, wide=False, gallery=True, unlock=False, loud=False):
        r = []

        if not series:
            series = range(start, finish+1)

        for nb in series:
            name, img = base_name % str(nb), base_img % str(nb)

            r.append(declare(name, img, method=method, x=x, y=y, wide=wide, gallery=gallery, unlock=unlock))

        return r # Python 2.7 won't allow me to unpack it. Darn.


#### IMAGE DECLARATIONS ####

# These dicts are used for generating CG galleries. Pictures will be displayed in the order they appear. Pictures with 'gallery' set to False will not appear in galleries.
# Each key is a separate button
# If every picture is 'gallery' set to False, it must be put in the 'unused' subdictionary.

    game_image_dict = {}

    ## UI images

    for col in ["purple", "red", "yellow", "blue", "green"]:
        for i in range(5):
            declare("%s canister %i" % (col, i), "UI/powers/%s canister%i.webp" % (col, i), "s")

    ## BACKGROUNDS ##

    game_image_dict["Backgrounds"] = {


                                        "sky" : [
                                                declare("bg sky day", "backgrounds/sky day.webp", "s", wide=True),
                                                declare("bg sky dusk", "backgrounds/sky dusk.webp", "s", wide=True),
                                                declare("bg sky night", "backgrounds/sky night.webp", "s", wide=True),
                                                declare("bg valley dusk", "backgrounds/valley dusk.webp", "s", wide=True),
                                                declare('bg stars', 'backgrounds/stars.webp', 's', wide=True),
                                                ],

                                        "outside" : [
                                                declare("bg outer wall", "backgrounds/castle night.webp", "s", wide=True),
                                                declare("bg outer gate", "backgrounds/gate night.webp", "s", wide=True),
                                                declare("bg battleground", "backgrounds/battleground.webp", "s", wide=True),
                                                declare("bg caravan", "backgrounds/caravan.webp", "s", wide=True, gallery="bg"),
                                                declare("bg dark street", "backgrounds/dark street.webp", "s"),
                                                declare('bg farmland', 'backgrounds/farmland.webp', 's'),
                                                declare('bg farmland dusk', 'backgrounds/farmland dusk.webp', 's'),
                                                declare('bg farmland night', 'backgrounds/farmland night.webp', 's'),
                                                declare('bg farmland night tall', 'backgrounds/farmland night tall.webp', 'p', y=9999),
                                                declare('bg forest', 'backgrounds/forest.webp', 's'),
                                                declare('bg forest night', 'backgrounds/forest night.webp', 's'),
                                                declare('bg clearing', 'backgrounds/clearing.webp', 's'),
                                                declare('bg farm outside', 'backgrounds/farm outside.webp', 's'),
                                                declare('bg haunted_farm', 'backgrounds/haunted farm.webp', 's', wide=True),
                                                declare('bg ambush1', 'backgrounds/ambush.webp', 's', wide=True),
                                                declare('bg ambush2', im.Flip(im.Scale("backgrounds/ambush.webp", config.screen_width, int(config.screen_height*0.8)), horizontal = True), gallery=False),
                                                declare('bg mansion night', 'backgrounds/mansion night.webp', 's', wide=True),
                                                declare('bg camp night', 'backgrounds/camp night.webp', 's', wide=True),
                                                declare('bg street', 'backgrounds/street.webp', 's', wide=True),
                                                declare('bg street night', 'backgrounds/street night.webp', 's'),
                                                declare('bg gallows', 'backgrounds/execution plaza.webp', 's', wide=True),
                                                declare('bg castle', 'backgrounds/castle.webp', 's'),
                                                declare('bg carriage', 'backgrounds/carriage.webp', 'p'),
                                                declare('bg arena_front', 'backgrounds/arena front.webp', 'p'),
                                                declare('bg dock', 'backgrounds/dock.webp', 'p'),
                                                declare('bg rooftop', 'backgrounds/rooftop.webp', 'p'),
                                                declare('bg rooftop night', 'backgrounds/rooftop night.webp', 'p'),
                                                declare('bg dojo night', 'backgrounds/dojo night.webp', 'p'),
                                                declare('bg asylum', 'backgrounds/asylum.webp', 'p'),
                                                ],

                                        "inside" : [
                                                declare("bg palace", "backgrounds/palace.webp", "s", wide=True),
                                                declare("bg desk", "backgrounds/front desk.webp", "s"),
                                                declare("bg office", "backgrounds/office.webp", "s", wide=True),
                                                declare("bg room", "backgrounds/room.webp", "p", wide=True),
                                                declare("bg pen", "brothels/farm/pen.webp", "p"),
                                                declare("bg throne room day", "backgrounds/throne room day.webp", "s", wide=True),
                                                declare("bg throne room night", "backgrounds/throne room night.webp", "s", wide=True),
                                                declare('bg gizel_room', 'backgrounds/gizel room.webp', 's', wide=True),
                                                declare('bg master room', 'backgrounds/master room.webp', 's', wide=True),
                                                declare('bg guard_office', 'backgrounds/guard office.webp', 's', wide=True),
                                                declare('bg inner_sewers', 'NPC/encounters/secret empty3.webp', 's', wide=True),
                                                declare('bg cell', 'NPC/encounters/secret room.webp', 's', wide=True),
                                                declare('bg thieves_guild inside', 'backgrounds/thieves guild hall.webp', 's'),
                                                declare('bg thieves_guild corridor', 'backgrounds/thieves guild corridor.webp', 's', wide=True),
                                                declare('bg thieves_guild room', 'backgrounds/thieves guild room.webp', 's', wide=True),
                                                declare('bg captain_office', 'backgrounds/rich room.webp', 's', wide=True),
                                                declare('bg vault', 'backgrounds/vault.webp', 's', wide=True),
                                                declare('bg palace room', 'backgrounds/palace room.webp', 's', wide=True),
                                                declare('bg palace corridor', 'backgrounds/palace corridor.webp', 's', wide=True),
                                                declare('bg palace corridor2', im.Flip(im.Scale("backgrounds/palace corridor.webp", config.screen_width, int(config.screen_height*0.8)), horizontal = True), gallery=False),
                                                declare('bg palace reception', 'backgrounds/reception.webp', 's', wide=True),
                                                declare('bg shalia_temple', 'backgrounds/shalia temple.webp', 's', wide=True),
                                                declare('bg other dimension', 'backgrounds/other dimension.webp', 's'),
                                                declare('bg cave', 'NPC/Encounters/secret empty2.webp', 's'),
                                                declare('bg empty_mansion', 'backgrounds/mansion empty.webp', 's', wide=True),
                                                declare('bg dark_underground', 'backgrounds/dark underground.webp', 's', wide=True),
                                                declare('bg magic_cellar', 'backgrounds/magic cellar.webp', 's'),
                                                declare('bg lab', 'backgrounds/lab.webp', 's'),
                                                ],

                                        "slavemarket" : [declare("bg slave market", "backgrounds/slave market12.webp", "p"),] +
                                                        declare_multiple("bg slave market%s", "backgrounds/slave market%s.webp", "p", start=1, finish=5) +
                                                        declare_multiple("bg slave market%s", "backgrounds/slave market%s.webp", "p", y = int(config.screen_height*0.8), start=6, finish=7) +
                                                        declare_multiple("bg slave market%s", "backgrounds/slave market%s.webp", "p", start=8, finish=11),


                                        "districts" : [
                                                declare("bg town", "backgrounds/town.webp", "p"),
                                                declare('bg zan', 'backgrounds/zan.webp', 's', wide=True),
                                                declare('bg rich district', 'backgrounds/rich district.webp', 'p', wide=True),
                                                declare('bg poor district', 'backgrounds/poor district.webp', 'p', wide=True),
                                                declare('bg slum district', 'districts/slums.webp', 'p', wide=True),
                                                ],

                                        "locations" : list_imgfiles(path="districts/locations/") + [
                                                    declare('bg spice_market', 'districts/locations/spice market.webp', 's', wide=True, gallery=False),
                                                    declare('bg sewers', 'districts/locations/sewers.webp', 's', wide=True, gallery=False),
                                                    declare('bg junkyard', 'districts/locations/junkyard.webp', 's', gallery=False),
                                                    declare('bg harbor', 'districts/locations/harbor.webp', 's', gallery=False),
                                                    declare('bg thieves_guild', 'districts/locations/thieves guild.webp', 'p', gallery=False),
                                                    declare('bg watchtower', 'districts/locations/watchtower.webp', 's', wide=True, gallery=False),
                                                    declare('bg market', 'districts/locations/market.webp', 's', gallery=False),
                                                    declare('bg exotic_emporium', 'districts/locations/Exotic emporium.webp', 'p', gallery=False),
                                                    declare('bg hanging_gardens', 'districts/locations/Hanging gardens.webp', 'p', gallery=False),
                                                    declare('bg botanical_garden', 'districts/locations/Botanical garden.webp', 'p', gallery=False),
                                                    declare('bg pilgrim_road', 'districts/locations/Pilgrim road.webp', 'p', gallery=False),
                                                    declare('bg courtyard', 'districts/locations/Courtyard.webp', 'p', gallery=False),
                                                    declare('bg ruins', 'districts/locations/Ruins.webp', 'p', gallery=False),
                                                    declare('bg plaza', 'districts/locations/plaza.webp', 'p', gallery=False),
                                                    declare('bg arena', 'districts/locations/Arena.webp', 'p', gallery=False),
                                                    declare('bg prison', 'districts/locations/prison.webp', 'p', gallery=False),
                                                    declare('bg seafront', 'districts/locations/Seafront.webp', 'p', gallery=False),
                                                    declare('bg library', 'districts/locations/library.webp', 'p', gallery=False),
                                                    declare('bg banking_quarter', 'districts/locations/Banking quarter.webp', 'p', gallery=False),
                                                ],

                                        "brothels" : [
                                                declare("bg brothel1", "brothels/" + brothel_pics[1], "s", unlock=True),
                                                declare("bg brothel1 bw", im.MatrixColor("brothels/" + brothel_pics[1], im.matrix.desaturate()), "p", wide=True, gallery=False),
                                                declare("bg brothel2", "brothels/" + brothel_pics[2], "p", wide=True),
                                                declare("bg brothel3", "brothels/" + brothel_pics[3], "p"),
                                                declare("bg brothel4", "brothels/" + brothel_pics[4], "p", wide=True),
                                                declare("bg brothel5", "brothels/" + brothel_pics[5], "p", wide=True),
                                                declare("bg brothel6", "brothels/" + brothel_pics[6], "p"),
                                                declare("bg brothel7", "brothels/" + brothel_pics[7], "p"),
                                                ],

                                        "rooms" : list_imgfiles(path="brothels/rooms/") + [
                                            declare('bg armory', 'brothels/rooms/armory.webp', 'p', gallery=False),
                                            declare('bg wagon', 'brothels/rooms/wagon.webp', 'p', wide=True, gallery=False),
                                            declare('bg onsen', 'brothels/rooms/onsen.webp', 'p', gallery=False),
                                            declare('bg tavern', 'brothels/rooms/tavern.webp', 'p', gallery=False),
                                            declare('bg okiya', 'brothels/rooms/okiya.webp', 'p', gallery=False),
                                            declare('bg club', 'brothels/rooms/strip club.webp', 'p', gallery=False),
                                            declare('bg strip club', 'brothels/rooms/strip club.webp', 'p', gallery=False),
                                            ],

                                        "farm" : list_imgfiles(path="brothels/farm/") + [
                                                declare('bg farm', 'brothels/farm/farm.webp', 'p', wide=True),
                                                declare('bg farm tall', 'brothels/farm/farm.webp', 's', gallery=False),
                                                declare('bg farm_stables', 'brothels/farm/stables.webp', 's', gallery=False),
                                                declare('bg farm_pig_stall', 'brothels/farm/pig stall.webp', 's', gallery=False),
                                                declare('bg farm_monster_den', 'brothels/farm/monster den.webp', 's', gallery=False),
                                                declare('bg farm_workshop', 'brothels/farm/workshop.webp', 's', gallery=False),
                                                ],
                                        }

    ## STORY ##

    game_image_dict["Story"] = {


                                "maid sex" : declare_multiple("bg gioblow%s", "NPC/Maid/blow%s.webp", "p", start=1, finish=3) +
                                        declare_multiple("bg giofuck%s", "NPC/Maid/fuck%s.webp", "p", start=1, finish=7),

                                "intro" : [
                                        declare('gknight fucked', 'NPC/Misc/knight fucked.webp'),
                                        declare('princess1 fucked', 'NPC/Misc/princess1 fucked.webp'),
                                        declare('princess2 fucked', 'NPC/Misc/princess2 fucked.webp'),
                                        declare('priest fucked', 'NPC/Misc/priest fucked.webp'),
                                        declare('mage fucked', 'NPC/Misc/mage fucked.webp'),
                                        ],

                                "sill soft" : [declare('bg sill_hold', 'NPC/Sill/hold.webp', 'p'), declare('bg sill_floor_naked', 'NPC/Sill/floor naked.webp', 'p')],

                                "sill gio_fuck" : [declare('bg giofuck8', 'NPC/Sill/gio fuck.webp', 'p')],

                                "sill sex1" :
                                        declare_multiple("bg nogiofuck%s", "NPC/Sill/sex%s.webp", "p", start=1, finish=4) +
                                        declare_multiple("bg nogiofuck%s", "NPC/Sill/sex%s.webp", "p", start=5, finish=6),

                                "sill intro" : [
                                        declare('bg sill sold', 'NPC/Sill/sill sold.webp', 'p'),
                                        declare('bg sill finger', 'NPC/Sill/sill fingering.webp', 'p'),
                                        declare('bg sill sex', 'NPC/Sill/sill sex.webp', 'p'),
                                        declare('bg sill bj', 'NPC/Sill/sill sucking.webp', 'p'),
                                        declare('bg sill fetish', 'NPC/Sill/sill fetish.webp', 'p'),
                                        ],

                                "hmas" : [
                                        declare('bg hmas1', 'NPC/Hmas/xmas1.webp', 's', wide=True),
                                        declare('bg hmas2', 'NPC/Hmas/xmas2.webp', 's', wide=True),
                                        declare('bg hmas sex1', 'NPC/Hmas/sex1.webp', 's', wide=True),
                                        declare('bg hmas sex2', 'NPC/Hmas/sex2.webp', 's', wide=True),
                                        declare('bg hmas anal1', 'NPC/Hmas/anal1.webp', 's', wide=True),
                                        declare('bg hmas anal2', 'NPC/Hmas/anal2.webp', 's', wide=True),
                                        ],

                                "renza sex" :
                                        [declare('bg renza_onsen', 'NPC/Renza/onsen.webp', 's', wide=True)] +
                                        declare_multiple("bg renza_sex%s", "NPC/Renza/sex%s.webp", "s", start=1, finish=6, wide=True),

                                "sewer rape" : declare_multiple('bg sewers_rape%s', 'NPC/Sewer girl/sex%s.webp', 's', start=1, finish=3),

                                "lieutenant sex" : declare_multiple('bg lieutenant sex%s', 'NPC/lieutenant/sex%s.webp', 'p', start=1, finish=2),

                                "captain sex" : [
                                        declare('captain sex1', 'NPC/captain/sex1.webp', 's', wide=True),
                                        declare('captain sex2', 'NPC/captain/sex2.webp', 's', wide=True),
                                        declare('bg captain sex3', 'NPC/captain/sex3.webp', 's', wide=True),
                                        declare('bg captain sex4', 'NPC/captain/sex4.webp', 's', wide=True),
                                        ],

                                "sergeant sex" : declare_multiple('bg sergeant sex%s', 'NPC/sergeant/sex%s.webp', 'p', start=1, finish=3, wide=True),

                                "maya sex" : declare_multiple('bg maya sex%s', 'NPC/maya/sex%s.webp', 'p', start=1, finish=3),

                                "satella soft1" : [
                                        declare('bg satella_intro', 'NPC/satella/satella intro.webp', 'p', wide=True),
                                        declare('bg satella casting', 'NPC/satella/casting.webp', 'p'),
                                        declare('bg satella dragon', 'NPC/satella/dragon.webp', 'p'),
                                        ],

                                "satella soft2" : declare_multiple('bg satella sit%s', 'NPC/satella/sitting (%s).webp', 'p', start=1, finish=3),

                                "satella soft3" : declare_multiple('bg satella stunned%s', 'NPC/satella/stunned (%s).webp', 'p', start=1, finish=7),

                                "satella sex1" : declare_multiple('bg satella sex1_%s', 'NPC/satella/sex1 (%s).webp', 'p', start=1, finish=3),

                                "satella sex2" : declare_multiple('bg satella sex2_%s', 'NPC/satella/sex2 (%s).webp', 'p', start=1, finish=5),

                                "satella sex3" : declare_multiple('bg satella sex3_%s', 'NPC/satella/sex3 (%s).webp', 'p', start=1, finish=5, wide=True),

                                "goldie soft" : [
                                        declare('bg goldie_hug', 'NPC/Goldie/hug.webp', 'p'),
                                        declare('bg goldie_promise1', 'NPC/Goldie/promise1.webp', 'p'),
                                        declare('bg goldie_promise2', 'NPC/Goldie/promise2.webp', 'p'),
                                        ],

                                "gizel rape" : declare_multiple("bg gizel_rape%s", "NPC/gizel/group (%s).webp", "p", start=1, finish=7),



                                "gizel soft" : declare_multiple("bg gizel_attack%s", "NPC/gizel/attack (%s).webp", "p", start=1, finish=4),



                                "gizel sex1" : declare_multiple("bg gizel_big1_%s", "NPC/gizel/big1 (%s).webp", "p", start=1, finish=5),




                                "gizel sex2" : declare_multiple("bg gizel_toad%s", "NPC/gizel/beast (%s).webp", "p", start=1, finish=6),



                                "gizel sex3" : declare_multiple("bg gizel_machine%s", "NPC/gizel/machine (%s).webp", "p", start=1, finish=6),



                                "gizel sex4" : declare_multiple("bg gizel_monster1_%s", "NPC/gizel/monster (%s).webp", "p", start=1, finish=7),



                                "gizel sex5" : declare_multiple("bg gizel_monster2_%s", "NPC/gizel/monster2 (%s).webp", "p", start=1, finish=6),


                                "gizel sex6" : declare_multiple("bg gizel_big2_%s", "NPC/gizel/big2 (%s).webp", "p", start=1, finish=5),

                                "gizel sex7" : declare_multiple("bg gizel_sex1_%s", "NPC/gizel/sex1 (%s).webp", "p", start=1, finish=5),

                                "gizel sex8" : declare_multiple("bg gizel_sex2_%s", "NPC/gizel/sex2 (%s).webp", "p", start=1, finish=5),

                                "gizel sex9" : declare_multiple("bg gizel_sex3_%s", "NPC/gizel/sex3 (%s).webp", "p", start=1, finish=5),

                                "goldie sex1" : declare_multiple("bg goldie_strip%s", "NPC/Goldie/strip%s.webp", "p", start=1, finish=2),

                                "goldie sex2" : declare_multiple("bg goldie_titjob%s", "NPC/Goldie/titjob%s.webp", "p", start=1, finish=4),

                                "goldie sex3" : declare_multiple("bg goldie_sex%s", "NPC/Goldie/sex%s.webp", "p", start=1, finish=3),

                                "willow soft" : [
                                        declare('bg willow_cast', 'NPC/Willow/cast.webp', 'p'),
                                        declare('bg willow_fire', 'NPC/Willow/fire.webp', 'p'),
                                        declare('bg willow upskirt', 'NPC/Willow/upskirt.webp', 'p'),
                                        declare('bg willow on_top', 'NPC/Willow/on top.webp', 'p'),
                                        declare('bg willow tea', 'NPC/Willow/tea.webp', 'p'),
                                        ],

                                "willow blowjob" : declare_multiple("bg willow bj%s", "NPC/Willow/bj (%s).webp", "p", start=1, finish=4),

                                "willow fuck" : [declare('bg willow fuck', 'NPC/Willow/sex.webp', 'p'), declare('bg willow sex', 'NPC/Willow/sex.webp', 'p')],

                                "willow rape" : [declare('bg willow rape', 'NPC/Willow/rape.webp', 'p')],

                                "willow relative" : declare_multiple("bg willow relative%s", "NPC/Willow/rel (%s).webp", "p", start=1, finish=4),

                                "gina soft" : [
                                        declare('bg gina_standing', 'NPC/Gina/stand.webp', 'p'),
                                        declare('bg gina_falling', 'NPC/Gina/falling.webp', 's'),
                                        declare('bg gina_jump', 'NPC/Gina/jump.webp', 'p', wide=True),
                                        declare('bg gina_flying', 'NPC/Gina/flying.webp', 's'),
                                        declare('bg gina_fallen1', 'NPC/Gina/fall1.webp', 's'),
                                        declare('bg gina_fallen2', 'NPC/Gina/fall2.webp', 's'),
                                        ],

                                "gina research" : declare_multiple("bg gina research%s", "NPC/Gina/research%s.webp", "p", start=1, finish=2),

                                "stella soft" : [
                                        declare('bg mare_orgasm', 'NPC/Stella/mare orgasm.webp', 's'),
                                        declare('bg mare_attack', 'NPC/Stella/mare attack.webp', 's'),
                                        ],

                                "stella service" : declare_multiple("bg stella handjob%s", "NPC/Stella/service (%s).webp", "p", start=1, finish=6),

                                "stella sex" : declare_multiple("bg stella sex%s", "NPC/Stella/sex (%s).webp", "p", start=1, finish=7),

                                "stella wall" : declare_multiple("bg stella_wall%s", "NPC/Stella/wall (%s).webp", "p", start=1, finish=5),

                                "blood1 bj" : declare_multiple("bg ka%s", "NPC/Stella/ka (%s).webp", "p", start=1, finish=6),

                                "blood2 tj" : declare_multiple("bg zee%s", "NPC/Stella/zee (%s).webp", "p", start=1, finish=5),

                                "stella bj" : declare_multiple("bg stella_bj%s", "NPC/Stella/bj (%s).webp", "p", start=1, finish=4),

                                "treasure sex1" : declare_multiple("bg treasure_blonde sex%s", "events/treasure_blonde_sex (%s).webp", "p", start=1, finish=6),

                                "treasure sex2" : declare_multiple("bg treasure_pink sex%s", "events/treasure_pink_sex (%s).webp", "p", start=1, finish=4),

                                "sewer girl sex" : [
                                        declare('bg sewer_girl_sex1', 'NPC/Sewer girl/sex4.webp', 'p'),
                                        declare('bg sewer_girl_sex2', 'NPC/Sewer girl/sex5.webp', 'p'),
                                        declare('bg sewer_girl_sex3', 'NPC/Sewer girl/sex6.webp', 'p'),
                                        ],

                                "shalia soft" : declare_multiple('bg shalia%s', 'NPC/shalia/shalia (%s).webp', 'p', start=1, finish=5),

                                "shalia fj" : declare_multiple('bg shalia fj%s', 'NPC/shalia/fj (%s).webp', 'p', start=1, finish=4),

                                "banker titjob" : declare_multiple('bg banker titjob%s', 'NPC/banker/titjob (%s).webp', 'p', start=1, finish=3, wide=True),

                                "banker sex" : declare_multiple('bg banker sex%s', 'NPC/banker/sex (%s).webp', 'p', start=1, finish=3, wide=True),

                                "taxgirl sex" : declare_multiple('bg taxgirl sex%s', 'NPC/taxgirl/sex (%s).webp', 'p', start=1, finish=5, wide=True),

                                "taxgirl anal" : declare_multiple('bg taxgirl anal%s', 'NPC/taxgirl/anal (%s).webp', 'p', start=1, finish=4, wide=True),

                                "bast sex" : declare_multiple('bg bast sex%s', 'NPC/bast/sex (%s).webp', 'p', start=1, finish=6, wide=True),

                                "bast titjob" : declare_multiple('bg bast titjob%s', 'NPC/bast/titjob (%s).webp', 'p', start=0, finish=5, wide=True),

                                "kenshin meet" : declare_multiple('bg kenshin_meet%s', 'NPC/kenshin/meet%s.webp', 'p', start=1, finish=4),
                                "kenshin pendant" : declare_multiple('bg kenshin_pendant%s', 'backgrounds/pendant%s.webp', 'f', x=0.25, y=0.25, start=1, finish=2),

                                "suzume soft" : [declare('bg suzume_roof', 'NPC/suzume/roof.webp', 'f', x=2, y=2)],

                                "suzume forest" : declare_multiple('bg suzume_forest%s', 'NPC/suzume/sex forest (%s).webp', 'p', start=1, finish=8),

                                "suzume brothel" : declare_multiple('bg suzume_brothel%s', 'NPC/suzume/brothel (%s).webp', 'p', start=1, finish=5),

                                "suzume visit" : [declare('bg suzume_onsen', 'NPC/suzume/onsen.webp', 'p'),
                                                 declare('bg suzume_69', 'NPC/suzume/69.webp', 'p'),
                                                 declare('bg suzume_piledriver', 'NPC/suzume/piledriver.webp', 'p'),
                                                 ],

                                "homura okiya" : [declare('bg homura_okiya happy', 'NPC/homura/okiya happy.webp', 'p'),
                                                declare('bg homura_okiya sad', 'NPC/homura/okiya sad.webp', 'p'),
                                                declare('bg homura_okiya serious', 'NPC/homura/okiya serious.webp', 'p'),
                                                declare('bg homura_okiya angry', 'NPC/homura/okiya angry.webp', 'p'),
                                                ],

                                "homura naked" : declare_multiple('bg homura_naked%s', 'NPC/homura/naked (%s).webp', 'p', start=1, finish=3),

                                "homura mast" : declare_multiple('bg homura_mast%s', 'NPC/homura/mast%s.webp', 'p', start=1, finish=5),

                                "homura bj" : declare_multiple('bg homura_bj%s', 'NPC/homura/bj%s.webp', 'p', start=1, finish=5),

                                "homura 69" : declare_multiple('bg homura_69_%s', 'NPC/homura/sixty-nine (%s).webp', 'p', start=1, finish=6),

                                "homura sex" : declare_multiple('bg homura_sex%s', 'NPC/homura/sex (%s).webp', 'p', start=1, finish=5),

                                "homura cowgirl" : declare_multiple('bg homura_cowgirl%s', 'NPC/homura/cowgirl (%s).webp', 'p', start=1, finish=4),

                                "homura waterfall" : declare_multiple('bg homura_water%s', 'NPC/homura/waterfall (%s).webp', 'p', start=1, finish=8),

                                "homura anal" : declare_multiple('bg homura_anal%s', 'NPC/homura/anal (%s).webp', 'p', start=1, finish=5),

                                "homura rest" : declare_multiple('bg homura_rest%s', 'NPC/homura/rest (%s).webp', 'p', start=1, finish=5),

                                "narika soft" : [declare('bg narika intro', 'NPC/kunoichi/narika/intro.webp', 'p'),
                                                ],

                                "narika mast" : declare_multiple("bg narika_mast%s", "NPC/kunoichi/narika/mast (%s).webp", "p", start=1, finish=11),

                                "mizuki soft" : [declare('bg mizuki intro', 'NPC/kunoichi/mizuki/intro.webp', 'p'),
                                                 declare('bg mizuki intro1', 'NPC/kunoichi/mizuki/intro1.webp', 'p'),
                                                 declare('bg mizuki intro2', 'NPC/kunoichi/mizuki/intro2.webp', 'p'),
                                                ],

                                "mizuki onsen" : declare_multiple("bg mizuki_onsen%s", "NPC/kunoichi/mizuki/onsen (%s).webp", "p", start=1, finish=4),

                                "haruka soft" : [declare('bg haruka intro', 'NPC/kunoichi/haruka/intro.webp', 'p'),] +
                                                 declare_multiple("bg haruka defeat%s", "NPC/kunoichi/haruka/defeat (%s).webp", "p", start=1, finish=3),

                                "haruka pillory" : declare_multiple("bg haruka pillory%s", "NPC/kunoichi/haruka/pillory (%s).webp", "p", start=1, finish=9),

                                "papa freak" : [declare('bg papa_freak', 'NPC/misc/freak.webp', 'p', wide=True)],

                                "witches" : declare_multiple('bg witches%s', 'NPC/encounters/witches (%s).webp', 'p', start=1, finish=3, wide=True),

                                "ninja guests" : declare_multiple('bg guest1_sex%s', 'NPC/kunoichi/guests/guest1 sex (%s).webp', 'p', start=1, finish=7) +
                                declare_multiple('bg guest2_sex%s', 'NPC/kunoichi/guests/guest2 sex (%s).webp', 'p', start=1, finish=6) +
                                declare_multiple('bg guest3_sex%s', 'NPC/kunoichi/guests/guest3 sex (%s).webp', 'p', start=1, finish=9),

                                "chaos" : [declare('bg chaos chained', 'NPC/Chaos/bg chained.webp', 's'),
                                            declare('bg chaos no girl', 'NPC/Chaos/bg no girl.webp', 'p'),
                                            declare('bg chaos girls', 'NPC/Chaos/bg girls.webp', 'p'),
                                            declare('bg chaos virgin', 'NPC/Chaos/bg virgin.webp', 'p')],
                                }


    ## CHARACTERS ##

    game_image_dict["Characters"] = OrderedDict([

                                ("sill", [
                                        declare('sill', 'NPC/Sill/body.webp', "tall"),

                                        declare('sill past', 'NPC/Sill/body_old.webp', "tall"),
                                        declare('sill happy', 'NPC/Sill/body.webp', "tall", gallery=False),
                                        declare('sill sad', 'NPC/Sill/body1.webp', "tall"),
                                        declare('sill drogon', 'NPC/Sill/sill and drogon2.webp', "tall"),
                                        declare('sill naked', 'NPC/Sill/body2.webp', "tall"),

                                        declare('side sill', 'NPC/Sill/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sill unknown', 'NPC/Sill/portrait_unknown.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sill happy', 'NPC/Sill/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sill sad', 'NPC/Sill/portrait1.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sill naked', 'NPC/Sill/portrait2.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sill past', 'NPC/Sill/portrait_old.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sill drogon', 'NPC/Sill/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side drogon', 'NPC/Misc/drogon.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("kurohime", [
                                        declare('kuro', 'NPC/Kurohime/body.webp', "tall"),
                                        declare('side kuro', 'NPC/Kurohime/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("maid", [
                                        declare('maid normal', 'NPC/Maid/normal.webp', "tall"),
                                        declare('maid blush', 'NPC/Maid/blush.webp', "tall"),

                                        declare('side maid normal', 'NPC/Maid/portrait.webp', 's', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side maid blush', 'NPC/Maid/portrait blush.webp', 's', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("gio", [
                                        declare('gio', 'NPC/Gio/body.webp', "med"),
                                        declare('gio normal', 'NPC/Gio/body.webp', "med", gallery=False),
                                        declare('gio incognito', 'NPC/Gio/body.webp', "med", gallery=False),
                                        declare('side gio', 'NPC/Gio/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side gio normal', 'NPC/Gio/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side gio incognito', 'NPC/Gio/portrait incognito.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("jobgirl", [
                                        declare('jobgirl', 'NPC/Jobgirl/body.webp', "tall"),
                                        declare('side jobgirl', 'NPC/Jobgirl/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("shopgirl", [declare("bg shop", "backgrounds/shop.webp", "p"), declare('bg shop bath', 'backgrounds/shop2.webp', 'p'),]),

                                ("sergeant", [
                                        declare('sergeant', 'NPC/Sergeant/body.webp', "tall"),
                                        declare('side sergeant', 'NPC/Sergeant/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("maya", [
                                        declare('maya', 'NPC/Maya/body.webp', "p"),
                                        declare('maya disarmed', 'NPC/Maya/disarmed.webp', "p"),
                                        declare('maya disarmed flip', im.Flip("NPC/Maya/disarmed.webp", horizontal=True), "p", gallery=False),
                                        declare('side maya', 'NPC/Maya/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("lieutenant", [
                                        declare('lieutenant', 'NPC/Lieutenant/body.webp', "tall"),
                                        declare('lieutenant attack', 'NPC/Lieutenant/body attack.webp', "tall"),
                                        declare('side lieutenant', 'NPC/Lieutenant/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("sewer woman", [
                                        declare('sewer_woman dressed', 'NPC/Sewer girl/body.webp', "tall"),
                                        declare('sewer_woman naked', 'NPC/Sewer girl/naked.webp', "tall"),
                                        declare('side sewer_woman', 'NPC/Sewer girl/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sewer_woman naked', 'NPC/Sewer girl/portrait naked.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),


                                ("renza", [
                                        declare('renza', 'NPC/Renza/body.webp', "med"),
                                        declare('side renza', 'NPC/Renza/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("satella", [
                                        declare('satella', 'NPC/Satella/body1.webp', "tall"),
                                        declare('satella happy', 'NPC/Satella/body1.webp', "tall", gallery=False),
                                        declare('satella angry', 'NPC/Satella/body1.webp', "tall", gallery=False),
                                        declare('satella_standing', 'NPC/Satella/body2.webp', "tall"),
                                        declare('side satella', 'NPC/Satella/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side satella angry', 'NPC/Satella/portrait2.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('satella naked', 'NPC/Satella/body3.webp', "tall"),
                                        declare('side satella naked', 'NPC/Satella/portrait3.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("captain", [
                                        declare('captain', 'NPC/Captain/body.webp', "tall"),
                                        declare('side captain', 'NPC/Captain/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("gizel", [
                                        declare('gizel', 'NPC/Gizel/body.webp', 'tall'),
                                        declare('gizel normal', 'NPC/Gizel/body.webp', 'tall', gallery=False),
                                        declare('gizel soft', 'NPC/Gizel/body soft.webp', 'tall'),
                                        declare('gizel surprise', 'NPC/Gizel/body surprise.webp', 'tall'),
                                        declare('gizel shy', 'NPC/Gizel/body shy.webp', 'tall'),
                                        declare('gizel blush', 'NPC/Gizel/body blush.webp', 'tall'),
                                        declare('gizel smirk', 'NPC/Gizel/body smirk.webp', 'tall'),
                                        declare('gizel upset', 'NPC/Gizel/body upset.webp', 'tall'),
                                        declare('gizel angry', 'NPC/Gizel/body angry.webp', 'tall'),

                                        declare('gizel whip angry', 'NPC/Gizel/whip1.webp', 'tall'),
                                        declare('gizel whip happy', 'NPC/Gizel/whip2.webp', 'tall'),
                                        declare('gizel whip struggling', 'NPC/Gizel/whip3.webp', 'tall'),

                                        declare('side gizel', 'NPC/Gizel/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side gizel normal', 'NPC/Gizel/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side gizel soft', 'NPC/Gizel/portrait soft.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side gizel surprise', 'NPC/Gizel/portrait surprise.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side gizel shy', 'NPC/Gizel/portrait shy.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side gizel blush', 'NPC/Gizel/portrait blush.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side gizel smirk', 'NPC/Gizel/portrait smirk.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side gizel upset', 'NPC/Gizel/portrait upset.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side gizel angry', 'NPC/Gizel/portrait angry.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("goldie", [
                                        declare('goldie', 'NPC/Goldie/body.webp', "tall"),
                                        declare('side goldie', 'NPC/Goldie/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
            #                            declare('goldie_swimsuit', 'NPC/Goldie/body swimsuit.webp'),
                                        #declare('side goldie_swimsuit', 'NPC/Goldie/portrait swimsuit.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("willow", [
                                        declare('willow', 'NPC/Willow/body.webp', "med"),
                                        declare('side willow', 'NPC/Willow/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("gina", [
                                        declare('gina', 'NPC/Gina/body.webp', "med"),
                                        declare('side gina', 'NPC/Gina/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("stella", [
                                        declare('stella', 'NPC/Stella/body1.webp', "pf", 1.4, 1.4), # Must be shown with yoffset
                                        declare('stella normal', 'NPC/Stella/body1.webp', "pf", 1.4, 1.4, gallery=False), # Must be shown with yoffset
                                        declare('stella crossed', 'NPC/Stella/body2.webp', "pf", 1.4, 1.4), # Must be shown with yoffset
                                        declare('stella uniform', 'NPC/Stella/body3.webp', "p"),
                                        declare('side stella', 'NPC/Stella/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side stella normal', 'NPC/Stella/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side stella uniform', 'NPC/Stella/portrait2.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("blood island officers", [
                                        declare('blood1', 'NPC/Stella/ka body.webp', 'p'),
                                        declare('side blood1', 'NPC/Stella/ka portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('blood2', 'NPC/Stella/zee body.webp', 'p'),
                                        declare('side blood2', 'NPC/Stella/zee portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),


                                ("milkmaid", [
                                        declare('milkmaid', 'NPC/Misc/milkmaid.webp', "tall"),
                                        declare('side milkmaid', 'NPC/Misc/milkmaid portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("kosmo", [
                                        declare('kosmo happy', 'NPC/Kosmo/body1.webp', "tall"),
                                        declare('kosmo angry', 'NPC/Kosmo/body2.webp', "tall"),
                                        declare('kosmo happy bw', im.MatrixColor('NPC/Kosmo/body1.webp', im.matrix.desaturate()), "tall", gallery=False),
                                        declare('kosmo angry bw', im.MatrixColor('NPC/Kosmo/body2.webp', im.matrix.desaturate()), "tall", gallery=False),
                                        declare('kosmo laughing', 'NPC/Kosmo/body3.webp', "tall"),
                                        declare('side kosmo', 'NPC/Kosmo/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side kosmo angry', 'NPC/Kosmo/portrait2.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side kosmo bw', im.MatrixColor('NPC/Kosmo/portrait.webp', im.matrix.desaturate()), 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side kosmo angry bw', im.MatrixColor('NPC/Kosmo/portrait2.webp', im.matrix.desaturate()), 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('kosmo', 'NPC/Kosmo/body1.webp', "tall", gallery=False),
                                        declare('kosmo bw', im.MatrixColor('NPC/Kosmo/body1.webp', im.matrix.desaturate()), "tall", gallery=False),
                                        ]),

                                ("kosmo girls", [
                                        declare('kosmo_girl_scientist', 'NPC/Kosmo/girl1.webp', "tall"),
                                        declare('kosmo_girl_ninja', 'NPC/Kosmo/girl2.webp', "tall"),
                                        declare('kosmo_girl_daughter', 'NPC/Kosmo/girl3.webp', "tall"),
                                        declare('kosmo_girl_magic', 'NPC/Kosmo/girl4.webp', "tall"),
                                        declare('kosmo_girl_wife', 'NPC/Kosmo/girl5.webp', "tall"),
                                        declare('kosmo_girl_captive', 'NPC/Kosmo/girl6.webp', "tall"),
                                        declare('kosmo_girl_rogue', 'NPC/Kosmo/girl7.webp', "tall"),
                                        declare('kosmo_girl_pirate', 'NPC/Kosmo/girl8.webp', "tall"),
                                        declare('kosmo_girl_noble', 'NPC/Kosmo/girl9.webp', "tall"),
                                        declare('kosmo_girl_machine', 'NPC/Kosmo/girl10.webp', "tall"),
                                        declare('kosmo_girl_machine2', 'NPC/Kosmo/girl11.webp', "tall"),
                                        declare('kosmo_twins', 'NPC/Kosmo/twins.webp', "tall"),
                                        ]),


                                ("shalia", [
                                        declare('shalia', 'NPC/shalia/body (1).webp', "tall"),
                                        declare('shalia2', 'NPC/shalia/body (2).webp', "tall"),
                                        declare('shalia3', 'NPC/shalia/body (3).webp', "tall"),
                                        declare('shalia4', 'NPC/shalia/body (4).webp', "tall"),
                                        declare('shalia5', 'NPC/shalia/body (5).webp', "tall"),
                                        declare('shalia6', 'NPC/shalia/body (6).webp', "tall"),
                                        declare('side shalia', 'NPC/shalia/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("roz", [
                                        declare("roz", "NPC/Roz/body.webp", "tall"),
                                        declare("side roz", "NPC/Roz/portrait.webp", 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare("roz party", im.Composite(
                                                                           (xres(860), yres(768)),
                                                                           (0, yres(60)), ProportionalScale("NPC/Roz/body.webp"),
                                                                           (xres(510), 0), im.FactorScale("NPC/Misc/Party hat.webp", 0.5, 0.5)
                                                                           ), "tall")
                                        ]),

                                ("carpenter", [
                                        declare('carpenter', 'NPC/carpenter/body.webp', "tall"),
                                        declare('carpenter normal', 'NPC/carpenter/body.webp', "tall", gallery=False),
                                        declare('carpenter attack', 'NPC/carpenter/attack.webp', "tall"),
                                        declare('side carpenter', 'NPC/carpenter/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("bast", [
                                        declare('bast', 'NPC/bast/body.webp', "tall"),
                                        declare('side bast', 'NPC/bast/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("banker", [
                                        declare('banker', 'NPC/banker/body.webp', "tall"),
                                        declare('banker normal', 'NPC/banker/body.webp', "tall", gallery=False),
                                        declare('banker appears happy', 'NPC/banker/appear happy.webp', "tall"),
                                        declare('banker appears mad', 'NPC/banker/appear mad.webp', "tall"),
                                        declare('banker cheerleader', 'NPC/banker/cheerleader.webp', "tall"),
                                        declare('side banker', 'NPC/banker/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("taxgirl", [
                                        declare('taxgirl', 'NPC/taxgirl/body.webp', "tall"),
                                        declare('side taxgirl', 'NPC/taxgirl/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                               ("riche", [
                                        declare('riche', 'NPC/riche/body.webp', "tall"),
                                        declare('side riche', 'NPC/riche/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       ]),

                               ("ramias", [
                                       declare('ramias', 'NPC/ramias/body.webp', "tall"),
                                       declare('ramias attack', 'NPC/ramias/body3.webp', "tall"),
                                       declare('side ramias', 'NPC/ramias/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       ]),

                               ("gurigura", [
                                       declare('gurigura', 'NPC/gurigura/body.webp', "tall"),
                                       declare('gurigura attack', 'NPC/gurigura/body3.webp', "tall"),
                                       declare('gurigura_attack', 'NPC/gurigura/attack.webp', 'p', wide=True),
                                       declare('side gurigura', 'NPC/gurigura/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       ]),

                               ("katryn", [
                                       declare('katryn', 'NPC/katryn/body.webp', "tall"),
                                       declare('side katryn', 'NPC/katryn/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       ]),

                               ("giftgirl", [
                                       declare('giftgirl', 'NPC/gift girl/body.webp', "tall"),
                                       declare('side giftgirl', 'NPC/gift girl/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       ]),

                               ("today", [
                                       declare('today', 'NPC/twins/body.webp', "med"),
                                       declare('side today', 'NPC/twins/today portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       declare('bg twins', 'NPC/twins/bg.webp', "p"),
                                       ]),

                               ("yesterday", [
                                       declare('yesterday', 'NPC/twins/body.webp', "med"),
                                       declare('side yesterday', 'NPC/twins/yesterday portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       ]),

                                ("kenshin", [
                                        declare('kenshin', 'NPC/kenshin/body.webp', "tall"),
                                        declare('kenshin normal', 'NPC/kenshin/body.webp', "tall"),
                                        declare('kenshin blush', 'NPC/kenshin/body.webp', "tall"),
                                        declare('side kenshin', 'NPC/kenshin/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side kenshin normal', 'NPC/kenshin/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side kenshin blush', 'NPC/kenshin/portrait blush.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("homura", [
                                        declare('homura', 'NPC/homura/body.webp', "p"),
                                        declare('homura normal', 'NPC/homura/body.webp', "p"),
                                        declare('homura blush', 'NPC/homura/body blush.webp', "p"),
                                        declare('homura surprise', 'NPC/homura/body surprise.webp', "p"),
                                        declare('homura sad', 'NPC/homura/body sad.webp', "p"),
                                        declare('homura naked', 'NPC/homura/body naked.webp', "p"),
                                        declare('side homura', 'NPC/homura/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side homura normal', 'NPC/homura/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side homura blush', 'NPC/homura/portrait blush.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side homura surprise', 'NPC/homura/portrait surprise.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side homura sad', 'NPC/homura/portrait sad.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side homura naked', 'NPC/homura/portrait naked.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("suzume", [
                                        declare('suzume', 'NPC/suzume/body.webp', "tall"),
                                        declare('suzume normal', 'NPC/suzume/body.webp', "tall", gallery=False),
                                        declare('suzume doubt', 'NPC/suzume/body.webp', "tall", gallery=False),
                                        declare('suzume bend', 'NPC/suzume/body bend.webp', "tall"),
                                        declare('suzume naked', 'NPC/suzume/body naked.webp', "tall"),
                                        declare('suzume naked2', 'NPC/suzume/body naked2.webp', "tall"),
                                        declare('suzume shrewd', 'NPC/suzume/body.webp', "tall", gallery=False),
                                        declare('suzume ninja', 'NPC/suzume/attack.webp', "tall"),
                                        declare('side suzume', 'NPC/suzume/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side suzume normal', 'NPC/suzume/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side suzume doubt', 'NPC/suzume/portrait doubt.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side suzume bend', 'NPC/suzume/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side suzume naked', 'NPC/suzume/portrait shrewd.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side suzume naked2', 'NPC/suzume/portrait naked2.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side suzume shrewd', 'NPC/suzume/portrait shrewd.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("kunoichi", [declare('haruka', 'NPC/kunoichi/haruka/body.webp', "tall"),
                                              declare('haruka normal', 'NPC/kunoichi/haruka/body.webp', "tall"),
                                              declare('haruka surprise', 'NPC/kunoichi/haruka/body.webp', "tall"),
                                              declare('haruka angry', 'NPC/kunoichi/haruka/body.webp', "tall"),
                                              declare('haruka happy', 'NPC/kunoichi/haruka/body.webp', "tall"),
                                              declare('haruka sad', 'NPC/kunoichi/haruka/body.webp', "tall"),
                                              declare('haruka blush', 'NPC/kunoichi/haruka/body.webp', "tall"),
                                              declare('haruka defiant', 'NPC/kunoichi/haruka/body.webp', "tall"),
                                              declare('side haruka', 'NPC/kunoichi/haruka/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka normal', 'NPC/kunoichi/haruka/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka ninja', 'NPC/kunoichi/haruka/portrait ninja.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka surprise', 'NPC/kunoichi/haruka/portrait surprise.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka angry', 'NPC/kunoichi/haruka/portrait angry.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka happy', 'NPC/kunoichi/haruka/portrait happy.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka sad', 'NPC/kunoichi/haruka/portrait sad.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka blush', 'NPC/kunoichi/haruka/portrait blush.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka defiant', 'NPC/kunoichi/haruka/portrait defiant.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('subaru', 'NPC/kunoichi/haruka/subaru.webp', "tall"),

                                              declare('narika', 'NPC/kunoichi/narika/body.webp', "tall"),
                                              declare('narika normal', 'NPC/kunoichi/narika/body.webp', "tall", gallery=False),
                                              declare('narika surprise', 'NPC/kunoichi/narika/body.webp', "tall", gallery=False),
                                              declare('narika angry', 'NPC/kunoichi/narika/body.webp', "tall", gallery=False),
                                              declare('narika happy', 'NPC/kunoichi/narika/body.webp', "tall", gallery=False),
                                              declare('narika sad', 'NPC/kunoichi/narika/body.webp', "tall", gallery=False),
                                              declare('narika blush', 'NPC/kunoichi/narika/body.webp', "tall", gallery=False),
                                              declare('narika ninja', 'NPC/kunoichi/narika/attack.webp', "tall"),
                                              declare('narika school', 'NPC/kunoichi/narika/body school.webp', "tall"),
                                              declare('side narika', 'NPC/kunoichi/narika/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika normal', 'NPC/kunoichi/narika/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika ninja', 'NPC/kunoichi/narika/portrait ninja.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika surprise', 'NPC/kunoichi/narika/portrait surprise.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika angry', 'NPC/kunoichi/narika/portrait angry.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika happy', 'NPC/kunoichi/narika/portrait happy.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika sad', 'NPC/kunoichi/narika/portrait sad.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika blush', 'NPC/kunoichi/narika/portrait blush.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),

                                              declare('mizuki', 'NPC/kunoichi/mizuki/body.webp', "p"),
                                              declare('mizuki normal', 'NPC/kunoichi/mizuki/body.webp', "p", gallery=False),
                                              declare('mizuki happy', 'NPC/kunoichi/mizuki/body.webp', "p", gallery=False),
                                              declare('mizuki sad', 'NPC/kunoichi/mizuki/body.webp', "p", gallery=False),
                                              declare('mizuki angry', 'NPC/kunoichi/mizuki/body.webp', "p", gallery=False),
                                              declare('side mizuki', 'NPC/kunoichi/mizuki/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side mizuki normal', 'NPC/kunoichi/mizuki/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side mizuki ninja', 'NPC/kunoichi/mizuki/portrait ninja.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side mizuki happy', 'NPC/kunoichi/mizuki/portrait happy.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side mizuki sad', 'NPC/kunoichi/mizuki/portrait sad.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side mizuki angry', 'NPC/kunoichi/mizuki/portrait angry.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side mizuki naked', 'NPC/kunoichi/mizuki/portrait naked.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),

                                              declare('kunoichi', 'NPC/kunoichi/kunoichi.webp', "tall"),
                                              declare('kunoichi reversed', im.Flip('NPC/kunoichi/kunoichi.webp', horizontal=True), "tall"),
                                              declare('side kunoichi', 'NPC/kunoichi/kunoichi portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              ]),

                            # Extras
                                ('gknight', [declare('gknight', 'NPC/Misc/girl_knight.webp', "small"),]),
                                ('princess1', [declare('princess1', 'NPC/Misc/princess1.webp', "small"),]),
                                ('princess2', [declare('princess2', 'NPC/Misc/princess2.webp', "small"),]),
                                ('priest', [declare('priest', 'NPC/Misc/priest.webp', "small"),]),
                                ('mage', [declare('mage', 'NPC/Misc/mage.webp', "small"),]),
                                ('bm1', [declare('bm1', 'NPC/Misc/bm1.webp', "small"),]),
                                ('bm2', [declare('bm2', 'NPC/Misc/bm2.webp', "small"),]),
                                ('king', [declare('king', 'NPC/Misc/king2.webp', "med"),]),
                                ('hood', [declare('hood', 'NPC/Misc/hood.webp', "small"),]),

                                ("guard", [
                                        declare('guard', 'NPC/Misc/guard.webp', "p"),
                                        declare('side guard', 'NPC/Misc/guard portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare("guard party", im.Composite(
                                                                             (xres(420), yres(768)),
                                                                             (0, 0), im.FactorScale("NPC/Misc/guard.webp",0.5,0.5),
                                                                             (xres(220), yres(130)), im.FactorScale("NPC/Misc/Party hat.webp", 0.3, 0.3),
                                                                             )), "p",
                                        ]),

                                ("thugs", [
                                        declare('side thug', 'UI/customers/thug.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),

                                        declare('thug1', 'NPC/Misc/thug1.webp', "tall"),
                                        declare('thug1 attack', 'NPC/Misc/thug1 attack.webp', "tall"),
                                        declare('side thug1', 'NPC/Misc/thug1 portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),

                                        declare('thug2', 'NPC/Misc/thug2.webp', "tall"),
                                        declare('thug2 attack', 'NPC/Misc/thug2 attack.webp', "tall"),
                                        declare('side thug2', 'NPC/Misc/thug2 portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('thug2 burnt', 'NPC/Misc/burnt.webp', "tall"),

                                        declare('thugs attack', 'NPC/Misc/thugs attack.webp', "tall"),
                                        ]),


                                ("henchman", [declare('henchman', 'NPC/Misc/henchman.webp', "tall")]),
                                ("masked thug", [declare('masked_thug', 'NPC/Misc/masked thug.webp', "tall")]),
                                ("stranger", [declare('stranger', 'NPC/Misc/stranger.webp', "tall")]),
                                ("sewer rapist", [declare('sewer_rapist', 'NPC/Misc/sewer rapist.webp', "tall")]),
                                ("judge", [declare('judge', 'NPC/Misc/judge.webp', "tall"), declare('side judge', 'NPC/Misc/judge portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),]),
                                ("knight", [declare('knight', 'NPC/Misc/knight.webp', "tall"), declare('side knight', 'NPC/Misc/knight portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),]),

                                ("templars", [
                                        declare('templar', 'NPC/Misc/templar.webp', "tall"),
                                        declare('initiate', 'NPC/Misc/initiate.webp', "tall"),
                                        declare('side templar', 'NPC/Misc/knight portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side initiate', 'NPC/Misc/soldier portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("monsters", [
                                        declare('spirit', 'NPC/Misc/spirit.webp', 'p', wide=True),
                                        declare('side spirit', 'NPC/Misc/spirit portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('sewer_monster', 'NPC/Misc/sewer monster.webp', "small"),
                                        declare('sewer_monster happy', 'NPC/Misc/sewer monster friendly.webp', "small"),
                                        declare('tentacle_monster', 'NPC/Misc/tentacle_monster.webp', "med"),
                                        ]),

                                ("mare", [
                                        declare('mare', 'NPC/Misc/mare.webp', "tall"),
                                        ]),

                                ("demons", [
                                        declare('blue_demon', 'NPC/Misc/blue demon.webp', "tall"),
                                        declare('side blue_demon', 'NPC/Misc/blue demon portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('red_demon', 'NPC/Misc/red demon.webp', "tall"),
                                        declare('side red_demon', 'NPC/Misc/red demon portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("skeleton", [
                                        declare('skeleton', 'NPC/Misc/skeleton.webp', "med"),
                                        declare('side skeleton', 'NPC/Misc/skeleton portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("ogres", [declare('ogre', 'NPC/Misc/ogre.webp', "p")]),

                                ("mask", [declare('side mask unknown', 'NPC/Misc/killer.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side mask', 'NPC/The Mask/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side mask normal', 'NPC/The Mask/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False)]),

                                ("ninja guests", [declare('hokoma_warrior', 'NPC/kunoichi/guests/guest1.webp', "tall"), declare('magical_girl', 'NPC/kunoichi/guests/guest2.webp', "tall"), declare('girl_scientist', 'NPC/kunoichi/guests/guest3.webp', "tall")]),

                            ])

    game_image_dict["unused"] = {

                                "unused for gallery (stand-alone portraits)" : [
                                        declare('side slavegirl1', 'NPC/Misc/slave1.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side slavegirl2', 'NPC/Misc/slave2.webp', 's', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side shopgirl', 'NPC/Misc/shop_girl.webp', 's', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side hmas', 'NPC/Hmas/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side raccoon', 'NPC/Misc/raccoon.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sailor', 'NPC/Misc/sailor.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side party_girl', 'NPC/Misc/party girl.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side nun', 'NPC/Misc/nun.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side kimono_lady', 'NPC/Misc/kimono lady.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side young_maid', 'NPC/Misc/maid.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side diplomat', 'NPC/Misc/diplomat.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sorceress', 'NPC/Misc/sorceress.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side naked_lady', 'NPC/Misc/naked lady.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('judge_head', 'NPC/Misc/judge head.webp', "small"),
                                        declare('panties', 'items/accessory/lace panties.webp', "small"),
                                        declare_multiple('house%s', 'minigame/house%s.webp', 'p', x=xres(90), start=1, finish=8),
                                        declare_multiple('passerby%s', 'minigame/passerby%s.webp', 'p', x=xres(80), start=1, finish=9),
                                        declare_multiple('ninja%s', 'minigame/ninja%s.webp', 'p', x=xres(80), start=0, finish=3),
                                        declare_multiple('guest%s', 'minigame/guest%s.webp', 'p', x=xres(80), start=1, finish=3),
                                        declare('toy hammer', 'items/Weapons/toy hammer.png', 'p', x=xres(32), y=yres(32), gallery=False),
                                        declare('side papa', 'NPC/Misc/freak portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side papa_apprentice', 'NPC/Misc/freak apprentice.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side demonette', 'NPC/Misc/demonette.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side hanny', 'NPC/Misc/hanny.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side crying_man', 'NPC/Misc/crying man.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side chaos', 'NPC/Chaos/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ],

                            }

    ## MISC PICTURES ##

    game_image_dict["Misc"] = {

                                "title" : [declare("bg title", "ui/theme.webp", "p", wide=True, unlock=True)],

                                "night" : ["events/" + p for p in night_pics + no_girls_pics],

                                "advertising" : ["events/" + p for p in advertising_pics[1]], # Update when more advertising levels are available

                                "pony" : ["events/" + p for p in pony_pics],

                                "security" : ["events/" + p for p in sum((security_pics.values()), [])] + [declare('side security', 'UI/shield.webp', 's', x=res_portrait_size, y=res_portrait_size, gallery=False),]+ [declare('side security_breach', 'UI/broken shield.webp', 's', x=res_portrait_size, y=res_portrait_size, gallery=False),],

                                "arson" : ["events/" + p for p in arson_pics],

                                "violent" : ["events/" + p for p in violent_pics] + [
                                        declare('bg murder', 'backgrounds/murder.webp', 'p'),
                                        ],

                                "treasure" : ["events/" + p for p in sum((treasure_pics.values()), [])],

                                "jobs" : [
                                        declare('bg waitress', 'backgrounds/waitress.webp', 'p', wide=True, unlock=True),
                                        declare('bg stripper', 'backgrounds/stripper.webp', 'p', wide=True, unlock=True),
                                        declare('bg masseuse', 'backgrounds/masseuse.webp', 'p', wide=True, unlock=True),
                                        declare('bg geisha', 'backgrounds/geisha.webp', 'p', wide=True, unlock=True),
                                        declare('bg whore', 'backgrounds/whore.webp', 'p', wide=True, unlock=True),
                                        declare('bg rest', 'backgrounds/rest.webp', 'p', wide=True, unlock=True),
                                        ],
                                "zodiac" : [declare('bg zodiac', 'backgrounds/zodiac.webp', 'p'),],

                                "tavern" : [
                                        declare('bg tavern_man', 'NPC/Misc/tavern_man.webp', 'p'),
                                        declare('symbol', 'backgrounds/thief symbol.webp'),
                                        ],

                                "elves" : [declare('bg elves', 'backgrounds/elves.webp', 'p')],

                                "mask events" : [declare('bg mask escape', 'NPC/The Mask/escape.webp', 'p')],

                                "succubi" : declare_multiple('bg succubi%s', 'events/succubi (%s).webp', 'p', start=1, finish=6),

                                "oni" : declare_multiple('bg oni%s', 'events/oni (%s).webp', 'p', start=1, finish=2),

                                "hannies" : declare_multiple('bg hannies%s', 'events/hannies (%s).webp', 'p', start=1, finish=5),

                                "pets" : declare_multiple('bg pet%s', 'NPC/misc/pets/bg pet (%s).webp', 'p', start=1, finish=4),

                                "demon service" : declare_multiple('demon service%s', 'events/demon service (%s).webm', 'p', start=1, finish=4, wide=True),

                                "demon sex" : declare_multiple('demon sex%s', 'events/demon sex (%s).webm', 'p', start=1, finish=6, wide=True),

                                "misc" : [declare('bg letter', 'backgrounds/letter.webp', 'p', gallery=False)],

                            }


#### GALLERY CREATION ####

    ## Game event Gallery layout ##

    # Lists all tabs and keys/buttons in the Game CG gallery as (tab, buttons) tuples

    ev_gallery_list = ["Characters", "Story", "Backgrounds", "Misc"]

#     ev_gallery_list = [
#                        ("Characters", ["sill", "kurohime", "maid", "gio", "kosmo", "kosmo girls", "gizel",
#                                        "maya", "roz", "lieutenant", "sergeant", "renza", "satella", "shalia", "captain", "sewer woman",
#                                        "goldie", "willow", "gina", "stella", "shopgirl", "jobgirl", "carpenter", "banker",
#                                        "guard", "thugs", "king", "princess1", "princess2", "gknight", "priest", "mage", "bm1", "bm2", "hood", "henchman",
#                                        "masked thug", "stranger", "sewer rapist", "judge", "templars", "milkmaid", "mare", "monsters",
#                                        "demons", "skeleton", ]),
#                        ("Story", ["intro", "sill intro", "sill sex1", "sill gio_fuck", "maid sex", "renza sex", "satella soft1", "satella soft2", "satella soft3", "satella sex1", "satella sex2", "satella sex3", "shalia soft", "shalia fj", "hmas",
#                                   "gizel soft", "gizel rape", "gizel sex1", "gizel sex2", "gizel sex3", "gizel sex4", "gizel sex5", "gizel sex6",
#                                   "goldie soft", "goldie sex1", "goldie sex2", "goldie sex3", "willow soft", "gina soft", "stella soft",
#                                   "sewer rape", "sewer girl sex", "treasure sex1", "treasure sex2", "banker titjob", "banker sex"]),
#                        ("Backgrounds", ["sky", "inside", "outside", "slavemarket", "districts", "locations", "brothels", "rooms", "farm", ]),
#                        ("Misc.", ["title", "jobs", "zodiac", "night", "pony", "security", "violent", "arson", "treasure", "tavern", "elves"]),
#                       ]

    ## Gallery init ##

    def init_galleries():

        lock = ProportionalScale("UI/lock.webp", 100, 100)

        global ev_gallery
        global gp_gallery

        ## Game event gallery

        ev_gallery = defaultdict(str)

        # Gallery options

        for g in ev_gallery_list:
            ev_gallery[g] = Gallery()
            ev_gallery[g].slideshow_delay = 1.0
            ev_gallery[g].navigation=True
            ev_gallery[g].locked_button=lock
            ev_gallery[g].unlocked_advance=True
            ev_gallery[g].blist = [] # Not a native attribute for the Gallery object
            ev_gallery[g].pics = {} # Not a native attribute for the Gallery object

        # Gallery buttons

            for b in game_image_dict[g].keys():
                pics = game_image_dict[g][b]
                if pics:
                    ev_gallery[g].blist.append(b)
                    ev_gallery[g].button(b)
                    for p in pics:
                        if p:
                            ev_gallery[g].image(p)
                            ev_gallery[g].condition("was_seen('" + p + "')")

        # Auto girl pack galleries

        gp_gallery = defaultdict(str)

        for pack in GirlFilesDict.get_paths():
            path = GirlFilesDict.get_path_dict()[pack]

            gp_gallery[pack] = Gallery()
            gp_gallery[pack].blist = []

            gp_gallery[pack].slideshow_delay = 1.0
            gp_gallery[pack].navigation=True
            gp_gallery[pack].span_buttons=True
            gp_gallery[pack].unlocked_advance=False # Unfortunately, unlocked advance is broken as of now.
            gp_gallery[pack].locked_button=lock

            for file in [f for f in renpy.list_files() if f.startswith(path) and is_imgfile(f, video=False)]:
                gp_gallery[pack].button(file)
                gp_gallery[pack].condition("was_seen('" + file + "')")
                gp_gallery[pack].image(ProportionalScale(file, config.screen_width, config.screen_height)) # file
                gp_gallery[pack].blist.append(file)


#### CUSTOM TRANSITIONS ####

image noise1 = im.Scale("transitions/noise1.png", config.screen_width, config.screen_height)
image noise2 = im.Scale("transitions/noise2.png", config.screen_width, config.screen_height)
image noise3 = im.Scale("transitions/noise3.png", config.screen_width, config.screen_height)
image noise4 = im.Scale("transitions/noise4.png", config.screen_width, config.screen_height)

define circleout = ImageDissolve(im.Scale("transitions/id_circleiris.webp", config.screen_width, config.screen_height), 2.0)

define circlein = ImageDissolve(im.Scale("transitions/id_circleiris.webp", config.screen_width, config.screen_height), 2.0, reverse = True)

define burn_it = ImageDissolve(im.Scale("transitions/shear.png", config.screen_width, config.screen_height), 1.2)

define satella_blink = ImageDissolve(im.Scale("NPC/Satella/body2.webp", config.screen_width, config.screen_height), 2.0, reverse = True) # AlphaDissolve("NPC/Satella/body2.webp", delay=1.0, alpha=True, reverse=False)

# From the 'Utsukushii Effects' renpy tutorial
define flashbackin = ImageDissolve(im.Scale("transitions/zigzag.webp", config.screen_width, config.screen_height), 3.0, 50)
define flashbackout = ImageDissolve(im.Scale("transitions/zigzag.webp", config.screen_width, config.screen_height), 3.0, 50)
##

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

define doubleflash = MultipleTransition([True, Fade(0.1, 0.0, 0.5, color="#fff"), True,
                                         Fade(0.1, 0.0, 0.5, color="#fff"),True])

define fastdissolve = Dissolve(0.1)

#### CG GALLERY ####

init -3 python:

    def was_seen(pic): # Where pic is a String, either a file path or a renpy image name

        if pic:
            if is_imgfile(pic, video=False): # Disables videos until we can find a way to make them show in CG gallery
                if pic in persistent.seen_list:
                    return True

            elif renpy.seen_image(pic) or pic in persistent.seen_list: # These are renpy images and not filenames
                if not is_videofile(pic):
                    return True

        return False

    def get_gallery_unlock_rate(gal_type, gal, name):
        if gal_type == "ev":
            r = 0
            t = 0

            for b in gal.blist:
                r += sum(1 for pic in game_image_dict[name][b] if was_seen(pic))
                t += sum(1 for pic in game_image_dict[name][b] if pic)

            return r * 100/t

        elif gal_type == "gp":
            return sum(1 for pic in gal.blist if was_seen(pic)) * 100/len(gal.blist)

    def get_button_unlock_rate(but, name):
        return str(sum(1 for pic in game_image_dict[name][but] if was_seen(pic))) + "/" + str(sum(1 for pic in game_image_dict[name][but] if pic))

    def unlock_pic(pic, silent=False):
        if not pic:
            return
        elif is_string(pic):
            path=pic
        elif isinstance(pic, Picture):
            path=pic.path
        elif isinstance(pic, ProportionalScale):
            path=pic.imgname
        else:
            raise AssertionError("Unlock picture: %s not recognized as a string or picture object." % pic)

        if path not in persistent.seen_list:
            persistent.seen_list.append(path)
            if not silent:
                debug_notify("Unlocking " + path)

    def get_gallery_pic(pics):
        for pic in pics:
            if "gallery" in pic:
                return pic



screen galleries():

    tag menu

    key "mouseup_3" action Return()
    key "K_ESCAPE" action Return()

    add "black"
    add "bg title" yalign 0.5

    frame xalign 0.5 yalign 0.5:
        has vbox spacing 10 box_wrap True

        textbutton "CG - Game" action (ShowMenu("gallery", gal_type="ev"), SetVariable("gallery_type", "ev")) text_size res_font(24) xsize int(config.screen_width*0.1851)

        textbutton "CG - Girl packs" action (ShowMenu("gallery", gal_type="gp"), SetVariable("gallery_type", "gp")) text_size res_font(24) xsize int(config.screen_width*0.1851)

        textbutton "Achievements" action ShowMenu("achievements") text_size res_font(24) xsize int(config.screen_width*0.1851)

        textbutton "Main Menu" action Function(renpy.full_restart) text_size res_font(24) xsize int(config.screen_width*0.1851)


screen gallery_left_menu(gal_type, gal):
    viewport xsize int(config.screen_width*0.1851) yfill True mousewheel True draggable True scrollbars "vertical":
        add "#000"

        vbox:
            if gal_type == "ev":
                for g in ev_gallery_list:
                    textbutton g action (SetScreenVariable("name", g), SetScreenVariable("gal", ev_gallery[g]), SetScreenVariable("page", 0), SelectedIf(gal==ev_gallery[g])) xsize int(config.screen_width*0.1851) text_size int(config.screen_height*0.025)

            elif gal_type == "gp":
                for pack in GirlFilesDict.get_paths():
                    $ n = get_name(pack, full=True)
                    textbutton n action (SetScreenVariable("name", n), SetScreenVariable("gal", gp_gallery[pack]), SetScreenVariable("page", 0), SelectedIf(gal==gp_gallery[pack])) xsize int(config.screen_width*0.1851) text_size int(config.screen_height*0.025)




screen gallery(gal_type="ev"): # The Gallery object must have a pics variable (a list of renpy displaybles or image files)

    tag menu

    default page=0
    default shown_pics = 9

    if gal_type == "ev":
        default name = "Characters"
        default gal = ev_gallery["Characters"]
    elif gal_type == "gp":
        $ first_pack = GirlFilesDict.get_paths()[0]
        default name = get_name(first_pack, full=True)
        default gal = gp_gallery[first_pack]

    key "mouseup_3" action ShowMenu("galleries")
    key "K_ESCAPE" action ShowMenu("galleries")

    add "#000"
#    add "" xalign 0.5 yalign 0.5

    hbox spacing 10:
        use gallery_left_menu(gal_type, gal)


        vbox spacing 10:

            text name + " (" + str(get_gallery_unlock_rate(gal_type, gal, name)) + "%)"

            frame background None: #"#000000CC":

                id "gallery"

                xsize 1.0
                ysize 0.9

                has hbox box_wrap True spacing 6

                $ index = page*shown_pics

                for i in range(shown_pics):

                    if index+i < len(gal.blist):
                        $ but = gal.blist[index+i]

                        if gal_type == "ev":
                            if is_imgfile(game_image_dict[name][but][0], video=False):
                                $ pic = ProportionalScale(game_image_dict[name][but][0], 240, 180)
                            elif game_image_dict[name][but][0]:
                                $ pic = ProportionalScale(ImageReference(game_image_dict[name][but][0]), 240, 180)

                        else:
                            $ pic = ProportionalScale(but, 240, 180)

                        frame background None xsize 250 ysize 190 ymargin 6 yalign 0.5:
                            add gal.make_button(but, pic, xpadding=3, ypadding=3, xalign=0.5, yalign=0.5, background=None) hover_alpha 1.0 idle_alpha 0.8
                            if gal_type == "ev":
                                frame background "#00000055" xalign 0.5 yalign 1.0 ypadding 1:
                                    text get_button_unlock_rate(but, name) size int(config.screen_height*0.02)
                            else:
                                if pic.imgname in persistent.pic_ignore_list:
                                    text "IGNORED" align (0.5, 0.5) color c_red size res_font(16) drop_shadow (2, 2)
                                if persistent.debug_pic_counter and gal_type == "gp":
                                    text _("Used %s times" % persistent.debug_pic_counter_dict[pic.imgname]) align (0.5, 1.0) size int(config.screen_height*0.02) #?


            $ max_page = (len(gal.blist)-1) // shown_pics

            text "Page " + str(page+1) + "/" + str(max_page+1) size int(config.screen_height*0.02)

            frame background None xfill True:
    #            textbutton "Start Slideshow" action gal.ToggleSlideshow()

                if page > 0:
                    key ["K_LEFT", "repeat_K_LEFT", "mousedown_4"]  action SetScreenVariable("page", page-1)
                    textbutton "Previous" action SetScreenVariable("page", page-1) xalign 0.05
                if page < max_page:
                    key ["K_RIGHT", "repeat_K_RIGHT", "mousedown_5"] action SetScreenVariable("page", page+1)
                    textbutton "Next" action SetScreenVariable("page", page+1) xalign 0.9
                if page < max_page - 10:
                    key "K_PAGEDOWN" action SetScreenVariable("page", page+10)
                else:
                    key "K_PAGEDOWN" action SetScreenVariable("page", max_page)

                if page > 10:
                    key "K_PAGEUP" action SetScreenVariable("page", page-10)
                else:
                    key "K_PAGEUP" action SetScreenVariable("page", 0)

                key "K_HOME" action SetScreenVariable("page", 0)
                key "K_END" action SetScreenVariable("page", max_page)

                textbutton "Return" action ShowMenu("galleries") xalign 0.5


screen _gallery:

    if locked:
        add "#000"
        text _("Image [index] of [count] locked.") align (0.5, 0.5)
    else:
        add "#000"

        for d in displayables:
            add d xalign 0.5 yalign 0.0
            if d.child.children[0].imgname in persistent.pic_ignore_list:
                text "IGNORED" align (0.5, 0.5) color c_red size res_font(48) drop_shadow (4, 4)

    if gallery.slideshow:
        timer gallery.slideshow_delay action Return("next") repeat True

    key "game_menu" action gallery.Return()

    if gallery.navigation:
        use gallery_navigation

screen gallery_navigation:
    hbox:
        spacing 20

        style_group "gallery"
        align (.98, .98)

        key "mouseup_3" action gallery.Return()
        key "K_ESCAPE" action gallery.Return()

        if gallery_type == "ev":
            key "K_LEFT" action gallery.Previous(unlocked=True)
            key "repeat_K_LEFT" action gallery.Previous(unlocked=True)
            key 'K_BACKSPACE' action gallery.Previous(unlocked=True)
            key "K_RIGHT" action gallery.Next(unlocked=True)
            key "repeat_K_RIGHT" action gallery.Next(unlocked=True)
            key 'K_SPACE' action gallery.Next(unlocked=True)
            key "K_RETURN" action gallery.ToggleSlideshow()
            key "K_SCROLLOCK" action gallery.ToggleSlideshow()
        else:
            key "mouseup_1" action NullAction() # Blocks mouse clicks for girlpack galleries
            key ['K_DELETE', 'KP_DELETE'] action Function(toggle_ignore_pic, d.child.children[0])

        if gallery_type == "ev":
            textbutton _("prev") action gallery.Previous(unlocked=True)
            textbutton _("next") action gallery.Next(unlocked=True)
            textbutton _("slideshow") action gallery.ToggleSlideshow()
        else:
            text str(d.child.children[0].imgname) size res_font(14)
        textbutton _("return") action gallery.Return()

    python:
        style.gallery = Style(style.default)
        style.gallery_button.background = None
        style.gallery_button_text.color = "#666"
        style.gallery_button_text.hover_color = "#fff"
        style.gallery_button_text.selected_color = "#fff"
        style.gallery_button_text.size = int(config.screen_height*0.0148)

#### Pet summons ####

init python:
    for i in range(50):
        renpy.image("weird_pet%i" % i, ConditionSwitch(
            "explode_pet[%i]" % i, "explode",
            "pets_on_fire > %i" % i, "NPC/Misc/Pets/pet%i.webp" % renpy.random.randint(2, 3),
            "True", "NPC/Misc/Pets/pet1.webp"))

    def small_lightning(trans, st, at):
        global pets_on_fire
        renpy.play(s_fire, "sound")
        pets_on_fire += 1

    def big_lightning(trans, st, at):
        global pets_on_fire
        renpy.play(s_thunder, "sound2")
        pets_on_fire += 2

image evil_lightning:
    zoom 3.0
    yalign 0.0
    choice:
        "minigame/rain/lightning.webp"
        alpha  0.0
        1.2

    choice:
        "minigame/rain/lightning.webp" with vpunch
        xalign 0.0
        alpha  0.0
        linear 0.6 alpha  1.0
        linear 0.6 alpha  0.0
        function small_lightning

    choice:
        "rev_lightning" with vpunch
        xalign 1.0
        alpha  0.0
        linear 0.6 alpha  1.0
        linear 0.6 alpha  0.0
        function big_lightning

    repeat

image explode:
    "NPC/Misc/Pets/frame_1.webp"
    pause 0.14
    "NPC/Misc/Pets/frame_2.webp"
    pause 0.14
    "NPC/Misc/Pets/frame_3.webp"
    pause 0.14
    "NPC/Misc/Pets/frame_4.webp"
    pause 0.14
    "NPC/Misc/Pets/frame_5.webp"
    pause 0.14
    "NPC/Misc/Pets/frame_6.webp"
    pause 0.14
    "NPC/Misc/Pets/frame_7.webp"
    pause 0.14
    "NPC/Misc/Pets/frame_8.webp"
    pause 0.14

transform falling_pet(x = renpy.random.random(), sz=renpy.random.randint(1, 3)):
    # fall_time cannot be passed as an argument, causes a glitch

    subpixel True

    zpos (3-sz)/3 # Doesn't seem to work

    xalign x
    yalign -0.2
    zoom 0.5 * sz

    parallel:
        linear fall_time * 2.0 yalign 1.4

    parallel:
        choice:
            rotate 0
            linear fall_time / 4 rotate 360
            repeat
        choice:
            rotate 0
            linear fall_time / 4 rotate -360
            repeat
        choice:
            rotate 25
        choice:
            rotate -25


transform falling_pet_die(x = renpy.random.random(), sz=renpy.random.randint(1, 3)):

    subpixel True

    zpos (3-sz)/3 # Doesn't seem to work

    xalign x
    yalign -0.2
    zoom 0.5 * sz

    parallel:
        linear fall_time yalign 0.61 - 0.32*x + 0.075*(1-x)*sz + 0.125 * renpy.random.random() # Causes the best distribution of dead bodies on the bg picture. Trust me, I did a lot of tests!

    parallel:
        choice:
            rotate 0
            linear fall_time / 4 rotate 360
            repeat
        choice:
            rotate 0
            linear fall_time / 4 rotate -360
            repeat
        choice:
            rotate 25
        choice:
            rotate -25

    time fall_time
    rotate 0


screen make_it_rain(finish_em = False): # 50 falling pets

    layer "master"

    default i = 0 # Must be a local variable, otherwise causes glitches
    default t = 1.5 # Pets will appear every t seconds

    if i < 50:
        if finish_em:
            timer t action (Show("falling_pet_die", _tag="falling_pet%i" % i, i=i), SetLocalVariable("i", i+1), SetVariable("fall_time", 1.0 + renpy.random.random()*0.5)) repeat True
        else:
            timer t action (Show("falling_pet", _tag="falling_pet%i" % i, i=i), SetLocalVariable("i", i+1), SetVariable("fall_time", 1.0 + renpy.random.random()*1.5)) repeat True

screen falling_pet(i): # Falls down through the screen

    layer "master"

    add "weird_pet%i" % i at falling_pet

    timer fall_time*2 action Hide()


screen falling_pet_die(i): # Falls down on the ground

    layer "master"

    add "weird_pet%i" % i at falling_pet_die

    timer fall_time action (SetDict(explode_pet, i, True), Play("sound", s_splat))


#### END OF BK declarations ####
