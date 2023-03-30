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
define gio = Character("吉欧", color = c_orange, image = "gio", window_left_padding=int(config.screen_height*0.205))


## MISC ##
define guard = Character("卫兵", color= c_yellow, image = "guard", window_left_padding=int(config.screen_height*0.205))
define thug1 = Character("暴徒", color= c_lightgreen, image = "thug1", window_left_padding=int(config.screen_height*0.205))
define thug2 = Character("暴徒", color= c_red, image = "thug2", window_left_padding=int(config.screen_height*0.205))
define thug3 = Character("暴徒", color= c_lightred, image = "thug", window_left_padding=int(config.screen_height*0.205))
define drogon = Character("龙-卓耿", color= c_darkred, image = "drogon", window_left_padding=int(config.screen_height*0.205))
define security = Character("安全事件", color= c_white, image = "security", window_left_padding=int(config.screen_height*0.205))
define security_breach = Character("安全事件", color= c_red, image = "security_breach", window_left_padding=int(config.screen_height*0.205))


#### SCREEN CHARACTERS ####

define slavegirl1 = Character("奴隶训练师", color = c_crimson, image = "slavegirl1", window_left_padding=int(config.screen_height*0.205))
define slavegirl2 = Character("女奴-美琪", color = c_violet, image = "slavegirl2", window_left_padding=int(config.screen_height*0.205))
define shopgirl = Character("风情万种的老板娘", color = c_pink, image = "shopgirl", window_left_padding=int(config.screen_height*0.205))
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
define papa_apprentice = Character("见习生", color=c_softpurple, image = "papa_apprentice", window_left_padding=int(config.screen_height*0.205))
define papa = Character("怪胎爸爸", color=c_lightblue, image = "papa", window_left_padding=int(config.screen_height*0.205))
define hokoma_warrior = Character("凶猛的女人", color=c_prune, image = "hokoma_warrior")
define magical_girl = Character("奇怪的女孩", color=c_emerald, image = "magical_girl")
define girl_scientist = Character("书呆子女孩", color=c_firered, image = "girl_scientist")

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

        if wide:
            y = int(y*0.8)

        if method == "s": # Scale method (image will fit the exact target dimensions - not proportional)
            renpy.image(name, im.Scale(img, x, y))

        elif method == "p": # ProportionalScale method (image will fit the target dimensions while preserving its aspect ratio)
            renpy.image(name, ProportionalScale(img, x, y))

        elif method == "f": # Factor Scale (image dimensions will change proportionately to float numbers x and y)

            # Foolproofing
            if x == config.screen_width:
                x = 1.0
            if y == config.screen_height:
                y = 1.0

            renpy.image(name, im.FactorScale(img, x, y))

        else: # No change to the original image
            renpy.image(name, img)

        if unlock:
            unlock_pic(name)

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

    ## BACKGROUNDS ##

    game_image_dict["Backgrounds"] = {


                                        "sky" : [
                                                declare("bg sky day", "backgrounds/sky day.webp", "s", wide=True),
                                                declare("bg sky dusk", "backgrounds/sky dusk.webp", "s", wide=True),
                                                declare("bg sky night", "backgrounds/sky night.webp", "s", wide=True),
                                                declare("bg valley dusk", "backgrounds/valley dusk.webp", "s", wide=True),
                                                declare('bg stars', 'backgrounds/stars.jpg', 's', wide=True),
                                                ],

                                        "outside" : [
                                                declare("bg outer wall", "backgrounds/castle night.webp", "s", wide=True),
                                                declare("bg outer gate", "backgrounds/gate night.webp", "s", wide=True),
                                                declare("bg battleground", "backgrounds/battleground.webp", "s", wide=True),
                                                declare("bg caravan", "backgrounds/caravan.webp", "s", wide=True, gallery="bg"),
                                                declare("bg dark street", "backgrounds/dark street.jpg", "s"),
                                                declare('bg farmland', 'backgrounds/farmland.jpg', 's'),
                                                declare('bg farmland dusk', 'backgrounds/farmland dusk.jpg', 's'),
                                                declare('bg farmland night', 'backgrounds/farmland night.jpg', 's'),
                                                declare('bg forest', 'backgrounds/forest.jpg', 's'),
                                                declare('bg forest night', 'backgrounds/forest night.jpg', 's'),
                                                declare('bg clearing', 'backgrounds/clearing.jpg', 's'),
                                                declare('bg farm outside', 'backgrounds/farm outside.jpg', 's'),
                                                declare('bg haunted_farm', 'backgrounds/haunted farm.jpg', 's', wide=True),
                                                declare('bg ambush1', 'backgrounds/ambush.jpg', 's', wide=True),
                                                declare('bg ambush2', im.Flip(im.Scale("backgrounds/ambush.jpg", config.screen_width, int(config.screen_height*0.8)), horizontal = True), gallery=False),
                                                declare('bg mansion night', 'backgrounds/mansion night.jpg', 's', wide=True),
                                                declare('bg camp night', 'backgrounds/camp night.jpg', 's', wide=True),
                                                declare('bg street', 'backgrounds/street.jpg', 's', wide=True),
                                                declare('bg street night', 'backgrounds/street night.jpg', 's'),
                                                declare('bg gallows', 'backgrounds/execution plaza.jpg', 's', wide=True),
                                                declare('bg castle', 'backgrounds/castle.jpg', 's', gallery=False),
                                                declare('bg carriage', 'backgrounds/carriage.jpg', 'p', gallery=False),
                                                declare('bg arena_front', 'backgrounds/arena front.jpg', 'p', gallery=False),
                                                declare('bg dock', 'backgrounds/dock.jpg', 'p', gallery=False),
                                                declare('bg rooftop', 'backgrounds/rooftop.jpg', 'p', gallery=False),
                                                declare('bg rooftop night', 'backgrounds/rooftop night.jpg', 'p', gallery=False),
                                                declare('bg dojo night', 'backgrounds/dojo night.webp', 'p', gallery=False),
                                                ],

                                        "inside" : [
                                                declare("bg palace", "backgrounds/palace.webp", "s", wide=True),
                                                declare("bg desk", "backgrounds/front desk.webp", "s"),
                                                declare("bg office", "backgrounds/office.webp", "s", wide=True),
                                                declare("bg room", "backgrounds/room.webp", "p", wide=True),
                                                declare("bg throne room day", "backgrounds/throne room day.webp", "s", wide=True),
                                                declare("bg throne room night", "backgrounds/throne room night.webp", "s", wide=True),
                                                declare('bg gizel_room', 'backgrounds/gizel room.jpg', 's', wide=True),
                                                declare('bg master room', 'backgrounds/master room.jpg', 's', wide=True),
                                                declare('bg guard_office', 'backgrounds/guard office.jpg', 's', wide=True),
                                                declare('bg inner_sewers', 'NPC/encounters/secret empty3.jpg', 's', wide=True),
                                                declare('bg cell', 'NPC/encounters/secret room.jpg', 's', wide=True),
                                                declare('bg thieves_guild inside', 'backgrounds/thieves guild hall.jpg', 's'),
                                                declare('bg thieves_guild corridor', 'backgrounds/thieves guild corridor.webp', 's', wide=True),
                                                declare('bg thieves_guild room', 'backgrounds/thieves guild room.jpg', 's', wide=True),
                                                declare('bg captain_office', 'backgrounds/rich room.jpg', 's', wide=True),
                                                declare('bg vault', 'backgrounds/vault.jpg', 's', wide=True),
                                                declare('bg palace room', 'backgrounds/palace room.jpg', 's', wide=True),
                                                declare('bg palace corridor', 'backgrounds/palace corridor.webp', 's', wide=True),
                                                declare('bg palace corridor2', im.Flip(im.Scale("backgrounds/palace corridor.webp", config.screen_width, int(config.screen_height*0.8)), horizontal = True), gallery=False),
                                                declare('bg palace reception', 'backgrounds/reception.jpg', 's', wide=True),
                                                declare('bg shalia_temple', 'backgrounds/shalia temple.jpg', 's', wide=True),
                                                declare('bg other dimension', 'backgrounds/other dimension.jpg', 's'),
                                                declare('bg cave', 'NPC/Encounters/secret empty2.jpg', 's'),
                                                declare('bg empty_mansion', 'backgrounds/mansion empty.jpg', 's', wide=True),
                                                declare('bg dark_underground', 'backgrounds/dark underground.jpg', 's', wide=True),
                                                declare('bg magic_cellar', 'backgrounds/magic cellar.jpg', 's', wide=True),
                                                declare('bg lab', 'backgrounds/lab.webp', 's'),
                                                ],

                                        "slavemarket" : [declare("bg slave market", "backgrounds/slave market12.jpg", "p"),] +
                                                        declare_multiple("bg slave market%s", "backgrounds/slave market%s.jpg", "p", start=1, finish=5) +
                                                        declare_multiple("bg slave market%s", "backgrounds/slave market%s.jpg", "p", y = int(config.screen_height*0.8), start=6, finish=7) +
                                                        declare_multiple("bg slave market%s", "backgrounds/slave market%s.jpg", "p", start=8, finish=11),


                                        "districts" : [
                                                declare("bg town", "backgrounds/town.jpg", "p"),
                                                declare('bg zan', 'backgrounds/zan.jpg', 's', wide=True),
                                                declare('bg rich district', 'backgrounds/rich district.jpg', 'p', wide=True),
                                                declare('bg poor district', 'backgrounds/poor district.jpg', 'p', wide=True),
                                                declare('bg slum district', 'districts/slums.jpg', 'p', wide=True),

                    #                             "Spice market.jpg", "Sewers.webp", "farmland.jpg", "Watchtower.jpg", "Junkyard.webp", "Thieves guild.jpg",
                    #                             "Harbor.jpg", "Shipyard.jpg", "Taverns.jpg", "Seafront.jpg", "Beach.jpg", "Exotic emporium.jpg",
                    #                             'Stables.jpg', 'Market.jpg', 'Gallows.jpg', 'Prison.jpg', 'Arena.jpg', 'Botanical garden.jpg',
                    #                             'Library.jpg', 'Hanging gardens.jpg', 'Guild quarter.jpg', 'Magic guild.jpg', 'Pilgrim road.jpg', 'Falls.webp',
                    #                             'Banking quarter.jpg', 'Training ground.jpg', 'Cathedra.jpg', 'Battlements.jpg', 'Keep.jpg', 'Courtyard.jpg',
                    #                             'Temple.webp', 'Hall.jpg', 'Plaza.jpg', 'Magic forest.jpg', 'Lake.jpg', 'Ruins.webp'
                                                ],

                                        "locations" : list_imgfiles(path="districts/locations/") + [
                                                    declare('bg spice_market', 'districts/locations/spice market.jpg', 's', wide=True, gallery=False),
                                                    declare('bg sewers', 'districts/locations/sewers.webp', 's', wide=True, gallery=False),
                                                    declare('bg junkyard', 'districts/locations/junkyard.webp', 's', gallery=False),
                                                    declare('bg harbor', 'districts/locations/harbor.jpg', 's', gallery=False),
                                                    declare('bg thieves_guild', 'districts/locations/thieves guild.jpg', 'p', gallery=False),
                                                    declare('bg watchtower', 'districts/locations/watchtower.jpg', 's', wide=True, gallery=False),
                                                    declare('bg market', 'districts/locations/market.jpg', 's', gallery=False),
                                                    declare('bg exotic_emporium', 'districts/locations/Exotic emporium.jpg', 'p', gallery=False),
                                                    declare('bg hanging_gardens', 'districts/locations/Hanging gardens.jpg', 'p', gallery=False),
                                                    declare('bg pilgrim_road', 'districts/locations/Pilgrim road.jpg', 'p', gallery=False),
                                                    declare('bg courtyard', 'districts/locations/Courtyard.jpg', 'p', gallery=False),
                                                    declare('bg ruins', 'districts/locations/Ruins.webp', 'p', gallery=False),
                                                    declare('bg plaza', 'districts/locations/plaza.jpg', 'p', gallery=False),
                                                    declare('bg arena', 'districts/locations/Arena.jpg', 'p', gallery=False),
                                                    declare('bg prison', 'districts/locations/prison.jpg', 'p', gallery=False),
                                                    declare('bg seafront', 'districts/locations/Seafront.jpg', 'p', gallery=False),
                                                    declare('bg library', 'districts/locations/library.jpg', 'p', gallery=False),
                                                ],

                                        "brothels" : [
                                                declare("bg brothel1", "brothels/" + brothel_pics[1], "p", wide=True, unlock=True),
                                                declare("bg brothel1 bw", im.MatrixColor("brothels/" + brothel_pics[1], im.matrix.desaturate()), "p", wide=True, gallery=False),
                                                declare("bg brothel2", "brothels/" + brothel_pics[2], "p", wide=True),
                                                declare("bg brothel3", "brothels/" + brothel_pics[3], "p"),
                                                declare("bg brothel4", "brothels/" + brothel_pics[4], "p", wide=True),
                                                declare("bg brothel5", "brothels/" + brothel_pics[5], "p", wide=True),
                                                declare("bg brothel6", "brothels/" + brothel_pics[6], "p"),
                                                declare("bg brothel7", "brothels/" + brothel_pics[7], "p"),
                                                ],

                                        "rooms" : list_imgfiles(path="brothels/rooms/") + [
                                            declare('bg armory', 'brothels/rooms/armory.jpg', 'p', wide=True, gallery=False),
                                            declare('bg wagon', 'brothels/rooms/wagon.jpg', 'p', wide=True, gallery=False),
                                            declare('bg onsen', 'brothels/rooms/onsen.webp', 'p', gallery=False),
                                            declare('bg tavern', 'brothels/rooms/tavern.webp', 'p', gallery=False),
                                            declare('bg okiya', 'brothels/rooms/okiya.webp', 'p', gallery=False),
                                            declare('bg club', 'brothels/rooms/strip club.webp', 'p', gallery=False),
                                            ],

                                        "farm" : list_imgfiles(path="brothels/farm/") + [
                                                declare('bg farm', 'brothels/farm/farm.jpg', 'p', wide=True),
                                                declare('bg farm tall', 'brothels/farm/farm.jpg', 's', gallery=False),
                                                declare('bg farm_stables', 'brothels/farm/stables.jpg', 's', gallery=False),
                                                declare('bg farm_pig_stall', 'brothels/farm/pig stall.jpg', 's', gallery=False),
                                                declare('bg farm_monster_den', 'brothels/farm/monster den.jpg', 's', gallery=False),
                                                declare('bg farm_workshop', 'brothels/farm/workshop.jpg', 's', gallery=False),
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

                                "sill soft" : [declare('bg sill_hold', 'NPC/Sill/hold.webp', 'p'), declare('bg sill_floor_naked', 'NPC/Sill/floor naked.jpg', 'p')],

                                "sill gio_fuck" : [declare('bg giofuck8', 'NPC/Sill/gio fuck.jpg', 'p')],

                                "sill sex1" :
                                        declare_multiple("bg nogiofuck%s", "NPC/Sill/sex%s.webp", "p", start=1, finish=4) +
                                        declare_multiple("bg nogiofuck%s", "NPC/Sill/sex%s.jpg", "p", start=5, finish=6),

                                "sill intro" : [
                                        declare('bg sill sold', 'NPC/Sill/sill sold.webp', 'p'),
                                        declare('bg sill finger', 'NPC/Sill/sill fingering.webp', 'p'),
                                        declare('bg sill sex', 'NPC/Sill/sill sex.webp', 'p'),
                                        declare('bg sill bj', 'NPC/Sill/sill sucking.webp', 'p'),
                                        declare('bg sill fetish', 'NPC/Sill/sill fetish.webp', 'p'),
                                        ],

                                "hmas" : [
                                        declare('bg hmas1', 'NPC/Hmas/xmas1.jpg', 's', wide=True),
                                        declare('bg hmas2', 'NPC/Hmas/xmas2.jpg', 's', wide=True),
                                        declare('bg hmas sex1', 'NPC/Hmas/sex1.jpg', 's', wide=True),
                                        declare('bg hmas sex2', 'NPC/Hmas/sex2.jpg', 's', wide=True),
                                        declare('bg hmas anal1', 'NPC/Hmas/anal1.webp', 's', wide=True),
                                        declare('bg hmas anal2', 'NPC/Hmas/anal2.webp', 's', wide=True),
                                        ],

                                "renza sex" :
                                        [declare('bg renza_onsen', 'NPC/Renza/onsen.webp', 's', wide=True)] +
                                        declare_multiple("bg renza_sex%s", "NPC/Renza/sex%s.jpg", "s", start=1, finish=6, wide=True),

                                "sewer rape" : declare_multiple('bg sewers_rape%s', 'NPC/Sewer girl/sex%s.jpg', 's', start=1, finish=3),

                                "lieutenant sex" : declare_multiple('bg lieutenant sex%s', 'NPC/lieutenant/sex%s.jpg', 'p', start=1, finish=2),

                                "captain sex" : [
                                        declare('captain sex1', 'NPC/captain/sex1.webp', 's', wide=True),
                                        declare('captain sex2', 'NPC/captain/sex2.webp', 's', wide=True),
                                        declare('bg captain sex3', 'NPC/captain/sex3.jpg', 's', wide=True),
                                        declare('bg captain sex4', 'NPC/captain/sex4.jpg', 's', wide=True),
                                        ],

                                "sergeant sex" : declare_multiple('bg sergeant sex%s', 'NPC/sergeant/sex%s.webp', 'p', start=1, finish=3, wide=True),

                                "maya sex" : declare_multiple('bg maya sex%s', 'NPC/maya/sex%s.jpg', 'p', start=1, finish=3),

                                "satella soft1" : [
                                        declare('bg satella_intro', 'NPC/satella/satella intro.jpg', 'p', wide=True),
                                        declare('bg satella casting', 'NPC/satella/casting.jpg', 'p'),
                                        declare('bg satella dragon', 'NPC/satella/dragon.jpg', 'p'),
                                        ],

                                "satella soft2" : declare_multiple('bg satella sit%s', 'NPC/satella/sitting (%s).webp', 'p', start=1, finish=3),

                                "satella soft3" : declare_multiple('bg satella stunned%s', 'NPC/satella/stunned (%s).jpg', 'p', start=1, finish=7),

                                "satella sex1" : declare_multiple('bg satella sex1_%s', 'NPC/satella/sex1 (%s).webp', 'p', start=1, finish=3),

                                "satella sex2" : declare_multiple('bg satella sex2_%s', 'NPC/satella/sex2 (%s).jpg', 'p', start=1, finish=5),

                                "satella sex3" : declare_multiple('bg satella sex3_%s', 'NPC/satella/sex3 (%s).jpg', 'p', start=1, finish=5, wide=True),

                                "goldie soft" : [
                                        declare('bg goldie_hug', 'NPC/Goldie/hug.jpg', 'p'),
                                        declare('bg goldie_promise1', 'NPC/Goldie/promise1.jpg', 'p'),
                                        declare('bg goldie_promise2', 'NPC/Goldie/promise2.jpg', 'p'),
                                        ],

                                "gizel rape" : declare_multiple("bg gizel_rape%s", "NPC/gizel/group (%s).webp", "p", start=1, finish=7),



                                "gizel soft" : declare_multiple("bg gizel_attack%s", "NPC/gizel/attack (%s).webp", "p", start=1, finish=4),



                                "gizel sex1" : declare_multiple("bg gizel_sex%s", "NPC/gizel/sex%s.webp", "p", start=1, finish=5),




                                "gizel sex2" : declare_multiple("bg gizel_toad%s", "NPC/gizel/beast (%s).webp", "p", start=1, finish=6),



                                "gizel sex3" : declare_multiple("bg gizel_machine%s", "NPC/gizel/machine (%s).webp", "p", start=1, finish=6),



                                "gizel sex4" : declare_multiple("bg gizel_monster1_%s", "NPC/gizel/monster (%s).webp", "p", start=1, finish=7),



                                "gizel sex5" : declare_multiple("bg gizel_monster2_%s", "NPC/gizel/monster2 (%s).webp", "p", start=1, finish=6),


                                "gizel sex6" : declare_multiple("bg gizel_big%s", "NPC/gizel/big (%s).webp", "p", start=1, finish=5),

                                "goldie sex1" : declare_multiple("bg goldie_strip%s", "NPC/Goldie/strip%s.jpg", "p", start=1, finish=2),

                                "goldie sex2" : declare_multiple("bg goldie_titjob%s", "NPC/Goldie/titjob%s.jpg", "p", start=1, finish=4),

                                "goldie sex3" : declare_multiple("bg goldie_sex%s", "NPC/Goldie/sex%s.jpg", "p", start=1, finish=3),

                                "willow soft" : [
                                        declare('bg willow_cast', 'NPC/Willow/cast.jpg', 'p'),
                                        declare('bg willow_fire', 'NPC/Willow/fire.jpg', 'p'),
                                        declare('bg willow upskirt', 'NPC/Willow/upskirt.jpg', 'p'),
                                        declare('bg willow on_top', 'NPC/Willow/on top.jpg', 'p'),
                                        declare('bg willow tea', 'NPC/Willow/tea.jpg', 'p'),
                                        ],

                                "willow blowjob" : declare_multiple("bg willow bj%s", "NPC/Willow/bj (%s).jpg", "p", start=1, finish=4),

                                "willow fuck" : [declare('bg willow fuck', 'NPC/Willow/sex.jpg', 'p'), declare('bg willow sex', 'NPC/Willow/sex.jpg', 'p')],

                                "willow rape" : [declare('bg willow rape', 'NPC/Willow/rape.jpg', 'p')],

                                "willow relative" : declare_multiple("bg willow relative%s", "NPC/Willow/rel (%s).jpg", "p", start=1, finish=4),

                                "gina soft" : [
                                        declare('bg gina_standing', 'NPC/Gina/stand.jpg', 'p'),
                                        declare('bg gina_falling', 'NPC/Gina/falling.jpg', 's'),
                                        declare('bg gina_jump', 'NPC/Gina/jump.jpg', 'p', wide=True),
                                        declare('bg gina_flying', 'NPC/Gina/flying.jpg', 's'),
                                        declare('bg gina_fallen1', 'NPC/Gina/fall1.jpg', 's'),
                                        declare('bg gina_fallen2', 'NPC/Gina/fall2.jpg', 's'),
                                        ],

                                "gina research" : declare_multiple("bg gina research%s", "NPC/Gina/research%s.jpg", "p", start=1, finish=2),

                                "stella soft" : [
                                        declare('bg mare_orgasm', 'NPC/Stella/mare orgasm.jpg', 's'),
                                        declare('bg mare_attack', 'NPC/Stella/mare attack.jpg', 's'),
                                        ],

                                "stella service" : declare_multiple("bg stella handjob%s", "NPC/Stella/service (%s).jpg", "p", start=1, finish=6),

                                "stella sex" : declare_multiple("bg stella sex%s", "NPC/Stella/sex (%s).jpg", "p", start=1, finish=7),

                                "stella wall" : declare_multiple("bg stella_wall%s", "NPC/Stella/wall (%s).jpg", "p", start=1, finish=5),

                                "blood1 bj" : declare_multiple("bg ka%s", "NPC/Stella/ka (%s).jpg", "p", start=1, finish=6),

                                "blood2 tj" : declare_multiple("bg zee%s", "NPC/Stella/zee (%s).jpg", "p", start=1, finish=5),

                                "stella bj" : declare_multiple("bg stella_bj%s", "NPC/Stella/bj (%s).jpg", "p", start=1, finish=4),

                                "treasure sex1" : declare_multiple("bg treasure_blonde sex%s", "events/treasure_blonde_sex (%s).jpg", "p", start=1, finish=6),

                                "treasure sex2" : declare_multiple("bg treasure_pink sex%s", "events/treasure_pink_sex (%s).jpg", "p", start=1, finish=4),

                                "sewer girl sex" : [
                                        declare('bg sewer_girl_sex1', 'NPC/Sewer girl/sex4.jpg', 'p'),
                                        declare('bg sewer_girl_sex2', 'NPC/Sewer girl/sex5.jpg', 'p'),
                                        declare('bg sewer_girl_sex3', 'NPC/Sewer girl/sex6.jpg', 'p'),
                                        ],

                                "shalia soft" : declare_multiple('bg shalia%s', 'NPC/shalia/shalia (%s).jpg', 'p', start=1, finish=5),

                                "shalia fj" : declare_multiple('bg shalia fj%s', 'NPC/shalia/fj (%s).jpg', 'p', start=1, finish=4),

                                "banker titjob" : declare_multiple('bg banker titjob%s', 'NPC/banker/titjob (%s).jpg', 'p', start=1, finish=3, wide=True),

                                "banker sex" : declare_multiple('bg banker sex%s', 'NPC/banker/sex (%s).jpg', 'p', start=1, finish=3, wide=True),

                                "taxgirl sex" : declare_multiple('bg taxgirl sex%s', 'NPC/taxgirl/sex (%s).jpg', 'p', start=1, finish=5, wide=True),

                                "taxgirl anal" : declare_multiple('bg taxgirl anal%s', 'NPC/taxgirl/anal (%s).jpg', 'p', start=1, finish=4, wide=True),

                                "bast sex" : declare_multiple('bg bast sex%s', 'NPC/bast/sex (%s).webp', 'p', start=1, finish=6, wide=True),

                                "bast titjob" : declare_multiple('bg bast titjob%s', 'NPC/bast/titjob (%s).webp', 'p', start=0, finish=5, wide=True),

                                "kenshin meet" : declare_multiple('bg kenshin_meet%s', 'NPC/kenshin/meet%s.webp', 'p', start=1, finish=4),
                                "kenshin pendant" : declare_multiple('bg kenshin_pendant%s', 'backgrounds/pendant%s.webp', 'f', x=0.5, y=0.5, start=1, finish=2),

                                "suzume soft" : [declare('bg suzume_roof', 'NPC/suzume/roof.webp', 'f', x=2, y=2)],

                                "suzume forest" : declare_multiple('bg suzume_forest%s', 'NPC/suzume/sex forest (%s).webp', 'p', start=1, finish=8),

                                "suzume brothel" : declare_multiple('bg suzume_brothel%s', 'NPC/suzume/brothel (%s).jpg', 'p', start=1, finish=5),

                                "suzume visit" : [declare('bg suzume_onsen', 'NPC/suzume/onsen.jpg', 'p'),
                                                 declare('bg suzume_69', 'NPC/suzume/69.jpg', 'p'),
                                                 declare('bg suzume_piledriver', 'NPC/suzume/piledriver.jpg', 'p'),
                                                 ],

                                "homura okiya" : [declare('bg homura_okiya happy', 'NPC/homura/okiya happy.jpg', 'p'),
                                                declare('bg homura_okiya sad', 'NPC/homura/okiya sad.jpg', 'p'),
                                                declare('bg homura_okiya serious', 'NPC/homura/okiya serious.jpg', 'p'),
                                                declare('bg homura_okiya angry', 'NPC/homura/okiya angry.jpg', 'p'),
                                                ],

                                "homura naked" : declare_multiple('bg homura_naked%s', 'NPC/homura/naked (%s).jpg', 'p', start=1, finish=3),

                                "homura mast" : declare_multiple('bg homura_mast%s', 'NPC/homura/mast%s.jpg', 'p', start=1, finish=5),

                                "homura bj" : declare_multiple('bg homura_bj%s', 'NPC/homura/bj%s.jpg', 'p', start=1, finish=5),

                                "homura 69" : declare_multiple('bg homura_69_%s', 'NPC/homura/sixty-nine (%s).jpg', 'p', start=1, finish=6),

                                "homura sex" : declare_multiple('bg homura_sex%s', 'NPC/homura/sex (%s).jpg', 'p', start=1, finish=5),

                                "homura cowgirl" : declare_multiple('bg homura_cowgirl%s', 'NPC/homura/cowgirl (%s).jpg', 'p', start=1, finish=4),

                                "homura waterfall" : declare_multiple('bg homura_water%s', 'NPC/homura/waterfall (%s).jpg', 'p', start=1, finish=8),

                                "homura anal" : declare_multiple('bg homura_anal%s', 'NPC/homura/anal (%s).jpg', 'p', start=1, finish=5),

                                "homura rest" : declare_multiple('bg homura_rest%s', 'NPC/homura/rest (%s).jpg', 'p', start=1, finish=5),

                                "narika soft" : [declare('bg narika intro', 'NPC/kunoichi/narika/intro.jpg', 'p'),
                                                ],

                                "narika mast" : declare_multiple("bg narika_mast%s", "NPC/kunoichi/narika/mast (%s).webp", "p", start=1, finish=11),

                                "mizuki soft" : [declare('bg mizuki intro', 'NPC/kunoichi/mizuki/intro.webp', 'p'),
                                                 declare('bg mizuki intro1', 'NPC/kunoichi/mizuki/intro1.webp', 'p'),
                                                 declare('bg mizuki intro2', 'NPC/kunoichi/mizuki/intro2.webp', 'p'),
                                                ],

                                "mizuki onsen" : declare_multiple("bg mizuki_onsen%s", "NPC/kunoichi/mizuki/onsen (%s).jpg", "p", start=1, finish=4),

                                "haruka soft" : [declare('bg haruka intro', 'NPC/kunoichi/haruka/intro.webp', 'p'),] +
                                                 declare_multiple("bg haruka defeat%s", "NPC/kunoichi/haruka/defeat (%s).webp", "p", start=1, finish=3),

                                "haruka pillory" : declare_multiple("bg haruka pillory%s", "NPC/kunoichi/haruka/pillory (%s).webp", "p", start=1, finish=9),

                                "papa freak" : [declare('bg papa_freak', 'NPC/misc/freak.jpg', 'p', wide=True)],

                                "witches" : declare_multiple('bg witches%s', 'NPC/encounters/witches (%s).webp', 'p', start=1, finish=3, wide=True),

                                "ninja guests" : declare_multiple('bg guest1_sex%s', 'NPC/kunoichi/guests/guest1 sex (%s).jpg', 'p', start=1, finish=7) +
                                declare_multiple('bg guest2_sex%s', 'NPC/kunoichi/guests/guest2 sex (%s).jpg', 'p', start=1, finish=6) +
                                declare_multiple('bg guest3_sex%s', 'NPC/kunoichi/guests/guest3 sex (%s).jpg', 'p', start=1, finish=9),
                                }


    ## CHARACTERS ##

    game_image_dict["Characters"] = OrderedDict([

                                ("sill", [
                                        declare('sill', 'NPC/Sill/body.webp'),

                                        declare('sill past', 'NPC/Sill/body_old.webp', 'f', x=0.5, y=0.5),
                                        declare('sill happy', 'NPC/Sill/body.webp', gallery=False),
                                        declare('sill sad', 'NPC/Sill/body1.webp'),
                                        declare('sill drogon', 'NPC/Sill/sill and drogon2.webp'),
                                        declare('sill naked', 'NPC/Sill/body2.webp'),

                                        declare('side sill', 'NPC/Sill/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sill unknown', 'NPC/Sill/portrait_unknown.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sill happy', 'NPC/Sill/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sill sad', 'NPC/Sill/portrait1.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sill naked', 'NPC/Sill/portrait2.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sill past', 'NPC/Sill/portrait_old.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sill drogon', 'NPC/Sill/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side drogon', 'NPC/Misc/drogon.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("kurohime", [
                                        declare('kuro', 'NPC/Kurohime/body.webp'),
                                        declare('side kuro', 'NPC/Kurohime/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("maid", [
                                        declare('maid normal', 'NPC/Maid/normal.webp', 'f', x=1.2, y=1.2),
                                        declare('maid blush', 'NPC/Maid/blush.webp', 'f', x=1.2, y=1.2),

                                        declare('side maid normal', 'NPC/Maid/portrait.webp', 's', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side maid blush', 'NPC/Maid/portrait blush.webp', 's', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("gio", [
                                        declare('gio', 'NPC/Gio/body.webp', 'f', x=0.5, y=0.5),
                                        declare('gio normal', 'NPC/Gio/body.webp', 'f', x=0.5, y=0.5, gallery=False),
                                        declare('gio incognito', 'NPC/Gio/body.webp', 'f', x=0.5, y=0.5, gallery=False),
                                        declare('side gio', 'NPC/Gio/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side gio normal', 'NPC/Gio/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side gio incognito', 'NPC/Gio/portrait incognito.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("jobgirl", [
                                        declare('jobgirl', 'NPC/Jobgirl/body.webp', 'p', x=650, y=650),
                                        declare('side jobgirl', 'NPC/Jobgirl/portrait.webp', gallery=False),
                                        ]),

                                ("shopgirl", [declare("bg shop", "backgrounds/shop.jpg", "p"), declare('bg shop bath', 'backgrounds/shop2.jpg', 'p'),]),

                                ("sergeant", [
                                        declare('sergeant', 'NPC/Sergeant/body.webp'),
                                        declare('side sergeant', 'NPC/Sergeant/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("maya", [
                                        declare('maya', 'NPC/Maya/body.webp', 'f', x=0.5, y=0.5),
                                        declare('maya disarmed', 'NPC/Maya/disarmed.webp', 'f', x=0.5, y=0.5),
                                        declare('maya disarmed flip', im.Flip(im.FactorScale("NPC/Maya/disarmed.webp",0.5,0.5), horizontal=True), gallery=False),
                                        declare('side maya', 'NPC/Maya/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("lieutenant", [
                                        declare('lieutenant', 'NPC/Lieutenant/body.webp', 'f', x= 1.4, y= 1.4),
                                        declare('lieutenant attack', 'NPC/Lieutenant/body attack.webp', 'f', x= 1.4, y= 1.4),
                                        declare('side lieutenant', 'NPC/Lieutenant/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("sewer woman", [
                                        declare('sewer_woman dressed', 'NPC/Sewer girl/body.webp'),
                                        declare('sewer_woman naked', 'NPC/Sewer girl/naked.webp'),
                                        declare('side sewer_woman', 'NPC/Sewer girl/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sewer_woman naked', 'NPC/Sewer girl/portrait naked.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),


                                ("renza", [
                                        declare('renza', 'NPC/Renza/body.webp', 'f', x= 0.9, y= 0.9),
                                        declare('side renza', 'NPC/Renza/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("satella", [
                                        declare('satella', 'NPC/Satella/body1.webp', 'f', x= 0.9, y= 0.9),
                                        declare('satella happy', 'NPC/Satella/body1.webp', 'f', x= 0.9, y= 0.9, gallery=False),
                                        declare('satella angry', 'NPC/Satella/body1.webp', 'f', x= 0.9, y= 0.9, gallery=False),
                                        declare('satella_standing', 'NPC/Satella/body2.webp', 'f', x= 0.9, y= 0.9),
                                        declare('side satella', 'NPC/Satella/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side satella angry', 'NPC/Satella/portrait2.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('satella naked', 'NPC/Satella/body3.webp', 'f', x=0.6, y=0.6),
                                        declare('side satella naked', 'NPC/Satella/portrait3.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("captain", [
                                        declare('captain', 'NPC/Captain/body.webp'),
                                        declare('side captain', 'NPC/Captain/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("gizel", [
                                        declare('gizel', 'NPC/Gizel/body.webp'),
                                        declare('gizel normal', 'NPC/Gizel/body.webp', gallery=False),
                                        declare('gizel soft', 'NPC/Gizel/body soft.webp'),
                                        declare('gizel surprise', 'NPC/Gizel/body surprise.webp'),
                                        declare('gizel shy', 'NPC/Gizel/body shy.webp'),
                                        declare('gizel blush', 'NPC/Gizel/body blush.webp'),
                                        declare('gizel smirk', 'NPC/Gizel/body smirk.webp'),
                                        declare('gizel upset', 'NPC/Gizel/body upset.webp'),
                                        declare('gizel angry', 'NPC/Gizel/body angry.webp'),

                                        declare('gizel whip angry', 'NPC/Gizel/whip1.webp'),
                                        declare('gizel whip happy', 'NPC/Gizel/whip2.webp'),
                                        declare('gizel whip struggling', 'NPC/Gizel/whip3.webp'),

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
                                        declare('goldie', 'NPC/Goldie/body.webp'),
                                        declare('side goldie', 'NPC/Goldie/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
            #                            declare('goldie_swimsuit', 'NPC/Goldie/body swimsuit.webp'),
                                        #declare('side goldie_swimsuit', 'NPC/Goldie/portrait swimsuit.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("willow", [
                                        declare('willow', 'NPC/Willow/body.webp'),
                                        declare('side willow', 'NPC/Willow/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("gina", [
                                        declare('gina', 'NPC/Gina/body.webp'),
                                        declare('side gina', 'NPC/Gina/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("stella", [
                                        declare('stella', 'NPC/Stella/body1.webp', 'f', x=0.75, y=0.75),
                                        declare('stella normal', 'NPC/Stella/body1.webp', 'f', x=0.75, y=0.75, gallery=False),
                                        declare('stella crossed', 'NPC/Stella/body2.webp', 'f', x=0.75, y=0.75),
                                        declare('stella uniform', 'NPC/Stella/body3.webp', 'f', x=0.5, y=0.5),
                                        declare('side stella', 'NPC/Stella/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side stella normal', 'NPC/Stella/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side stella uniform', 'NPC/Stella/portrait2.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("blood island officers", [
                                        declare('blood1', 'NPC/Stella/ka body.webp', 'f', x=0.5, y=0.5),
                                        declare('side blood1', 'NPC/Stella/ka portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('blood2', 'NPC/Stella/zee body.webp', 'f', x=0.5, y=0.5),
                                        declare('side blood2', 'NPC/Stella/zee portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),


                                ("milkmaid", [
                                        declare('milkmaid', 'NPC/Misc/milkmaid.webp'),
                                        declare('side milkmaid', 'NPC/Misc/milkmaid portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("kosmo", [
                                        declare('kosmo happy', 'NPC/Kosmo/body1.webp'),
                                        declare('kosmo angry', 'NPC/Kosmo/body2.webp'),
                                        declare('kosmo happy bw', im.MatrixColor('NPC/Kosmo/body1.webp', im.matrix.desaturate()), gallery=False),
                                        declare('kosmo angry bw', im.MatrixColor('NPC/Kosmo/body2.webp', im.matrix.desaturate()), gallery=False),
                                        declare('kosmo laughing', 'NPC/Kosmo/body3.webp'),
                                        declare('side kosmo', 'NPC/Kosmo/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side kosmo angry', 'NPC/Kosmo/portrait2.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side kosmo bw', im.MatrixColor('NPC/Kosmo/portrait.webp', im.matrix.desaturate()), 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side kosmo angry bw', im.MatrixColor('NPC/Kosmo/portrait2.webp', im.matrix.desaturate()), 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('kosmo', 'NPC/Kosmo/body1.webp', gallery=False),
                                        declare('kosmo bw', im.MatrixColor('NPC/Kosmo/body1.webp', im.matrix.desaturate()), gallery=False),
                                        ]),

                                ("kosmo girls", [
                                        declare('kosmo_girl_scientist', 'NPC/Kosmo/girl1.webp'),
                                        declare('kosmo_girl_ninja', 'NPC/Kosmo/girl2.webp'),
                                        declare('kosmo_girl_daughter', 'NPC/Kosmo/girl3.webp'),
                                        declare('kosmo_girl_magic', 'NPC/Kosmo/girl4.webp'),
                                        declare('kosmo_girl_wife', 'NPC/Kosmo/girl5.webp'),
                                        declare('kosmo_girl_captive', 'NPC/Kosmo/girl6.webp', 'f', x=0.5, y=0.5),
                                        declare('kosmo_girl_rogue', 'NPC/Kosmo/girl7.webp'),
                                        declare('kosmo_girl_pirate', 'NPC/Kosmo/girl8.webp'),
                                        declare('kosmo_girl_noble', 'NPC/Kosmo/girl9.webp'),
                                        declare('kosmo_girl_machine', 'NPC/Kosmo/girl10.webp'),
                                        declare('kosmo_girl_machine2', 'NPC/Kosmo/girl11.webp'),
                                        declare('kosmo_twins', 'NPC/Kosmo/twins.webp'),
                                        ]),


                                ("shalia", [
                                        declare('shalia', 'NPC/shalia/body (1).webp', 'f', x=0.55, y=0.55),
                                        declare('shalia2', 'NPC/shalia/body (2).webp'),
                                        declare('shalia3', 'NPC/shalia/body (3).webp'),
                                        declare('shalia4', 'NPC/shalia/body (4).webp'),
                                        declare('shalia5', 'NPC/shalia/body (5).webp', 'f', x=0.55, y=0.55),
                                        declare('shalia6', 'NPC/shalia/body (6).webp', 'f', x=0.55, y=0.55),
                                        declare('side shalia', 'NPC/shalia/portrait.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("roz", [
                                        declare("roz", "NPC/Roz/body.webp"),
                                        declare("side roz", "NPC/Roz/portrait.jpg", 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare("roz party", im.Composite(
                                                                           (800, 700),
                                                                           (0, 30), "NPC/Roz/body.webp",
                                                                           (420, 0), im.FactorScale("NPC/Misc/Party hat.webp", 1.5, 1.2)
                                                                           ))
                                        ]),

                                ("carpenter", [
                                        declare('carpenter', 'NPC/carpenter/body.webp'),
                                        declare('carpenter normal', 'NPC/carpenter/body.webp', gallery=False),
                                        declare('carpenter attack', 'NPC/carpenter/attack.webp'),
                                        declare('side carpenter', 'NPC/carpenter/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("bast", [
                                        declare('bast', 'NPC/bast/body.webp'),
                                        declare('side bast', 'NPC/bast/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("banker", [
                                        declare('banker', 'NPC/banker/body.webp', 'f', x=0.55, y=0.55),
                                        declare('banker normal', 'NPC/banker/body.webp', 'f', x=0.55, y=0.55, gallery=False),
                                        declare('banker appears happy', 'NPC/banker/appear happy.webp', 'f', x=0.55, y=0.55),
                                        declare('banker appears mad', 'NPC/banker/appear mad.webp', 'f', x=0.55, y=0.55),
                                        declare('banker cheerleader', 'NPC/banker/cheerleader.webp', 'f', x=0.55, y=0.55),
                                        declare('side banker', 'NPC/banker/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("taxgirl", [
                                        declare('taxgirl', 'NPC/taxgirl/body.webp', 'f', x=0.9, y=0.9),
                                        declare('side taxgirl', 'NPC/taxgirl/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                               ("riche", [
                                        declare('riche', 'NPC/riche/body.webp', 'f', x=0.9, y=0.9),
                                        declare('side riche', 'NPC/riche/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       ]),

                               ("ramias", [
                                       declare('ramias', 'NPC/ramias/body.webp', 'f', x=0.9, y=0.9),
                                       declare('ramias attack', 'NPC/ramias/body3.webp', 'f', x=0.9, y=0.9),
                                       declare('side ramias', 'NPC/ramias/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       ]),

                               ("gurigura", [
                                       declare('gurigura', 'NPC/gurigura/body.webp', 'f', x=0.9, y=0.9),
                                       declare('gurigura attack', 'NPC/gurigura/body3.webp', 'f', x=0.9, y=0.9),
                                       declare('gurigura_attack', 'NPC/gurigura/attack.webp', 'p', wide=True),
                                       declare('side gurigura', 'NPC/gurigura/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       ]),

                               ("katryn", [
                                       declare('katryn', 'NPC/katryn/body.webp', 'f', x=0.9, y=0.9),
                                       declare('side katryn', 'NPC/katryn/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       ]),

                               ("giftgirl", [
                                       declare('giftgirl', 'NPC/gift girl/body.webp', 'f', x=0.9, y=0.9),
                                       declare('side giftgirl', 'NPC/gift girl/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       ]),

                               ("today", [
                                       declare('today', 'NPC/twins/body.webp', 'f', x=0.8, y=0.8),
                                       declare('side today', 'NPC/twins/today portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       declare('bg twins', 'NPC/twins/bg.jpg', 'f', x=0.8, y=0.8),
                                       ]),

                               ("yesterday", [
                                       declare('yesterday', 'NPC/twins/body.webp', 'f', x=0.8, y=0.8),
                                       declare('side yesterday', 'NPC/twins/yesterday portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                       ]),

                                ("kenshin", [
                                        declare('kenshin', 'NPC/kenshin/body.webp'),
                                        declare('kenshin normal', 'NPC/kenshin/body.webp'),
                                        declare('kenshin blush', 'NPC/kenshin/body.webp'),
                                        declare('side kenshin', 'NPC/kenshin/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side kenshin normal', 'NPC/kenshin/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side kenshin blush', 'NPC/kenshin/portrait blush.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("homura", [
                                        declare('homura', 'NPC/homura/body.webp'),
                                        declare('homura normal', 'NPC/homura/body.webp'),
                                        declare('homura blush', 'NPC/homura/body blush.webp'),
                                        declare('homura surprise', 'NPC/homura/body surprise.webp'),
                                        declare('homura sad', 'NPC/homura/body sad.webp'),
                                        declare('homura naked', 'NPC/homura/body naked.webp'),
                                        declare('side homura', 'NPC/homura/portrait.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side homura normal', 'NPC/homura/portrait.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side homura blush', 'NPC/homura/portrait blush.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side homura surprise', 'NPC/homura/portrait surprise.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side homura sad', 'NPC/homura/portrait sad.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side homura naked', 'NPC/homura/portrait naked.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("suzume", [
                                        declare('suzume', 'NPC/suzume/body.webp'),
                                        declare('suzume normal', 'NPC/suzume/body.webp', gallery=False),
                                        declare('suzume doubt', 'NPC/suzume/body.webp', gallery=False),
                                        declare('suzume bend', 'NPC/suzume/body bend.webp'),
                                        declare('suzume naked', 'NPC/suzume/body naked.webp'),
                                        declare('suzume naked2', 'NPC/suzume/body naked2.webp', 'f', x=0.6, y=0.6),
                                        declare('suzume shrewd', 'NPC/suzume/body.webp', gallery=False),
                                        declare('suzume ninja', 'NPC/suzume/attack.webp'),
                                        declare('side suzume', 'NPC/suzume/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side suzume normal', 'NPC/suzume/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side suzume doubt', 'NPC/suzume/portrait doubt.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side suzume bend', 'NPC/suzume/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side suzume naked', 'NPC/suzume/portrait shrewd.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side suzume naked2', 'NPC/suzume/portrait naked2.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side suzume shrewd', 'NPC/suzume/portrait shrewd.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("kunoichi", [declare('haruka', 'NPC/kunoichi/haruka/body.webp'),
                                              declare('haruka normal', 'NPC/kunoichi/haruka/body.webp'),
                                              declare('haruka surprise', 'NPC/kunoichi/haruka/body.webp'),
                                              declare('haruka angry', 'NPC/kunoichi/haruka/body.webp'),
                                              declare('haruka happy', 'NPC/kunoichi/haruka/body.webp'),
                                              declare('haruka sad', 'NPC/kunoichi/haruka/body.webp'),
                                              declare('haruka blush', 'NPC/kunoichi/haruka/body.webp'),
                                              declare('haruka defiant', 'NPC/kunoichi/haruka/body.webp'),
                                              declare('side haruka', 'NPC/kunoichi/haruka/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka normal', 'NPC/kunoichi/haruka/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka ninja', 'NPC/kunoichi/haruka/portrait ninja.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka surprise', 'NPC/kunoichi/haruka/portrait surprise.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka angry', 'NPC/kunoichi/haruka/portrait angry.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka happy', 'NPC/kunoichi/haruka/portrait happy.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka sad', 'NPC/kunoichi/haruka/portrait sad.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka blush', 'NPC/kunoichi/haruka/portrait blush.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side haruka defiant', 'NPC/kunoichi/haruka/portrait defiant.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('subaru', 'NPC/kunoichi/haruka/subaru.webp'),

                                              declare('narika', 'NPC/kunoichi/narika/body.webp'),
                                              declare('narika normal', 'NPC/kunoichi/narika/body.webp', gallery=False),
                                              declare('narika surprise', 'NPC/kunoichi/narika/body.webp', gallery=False),
                                              declare('narika angry', 'NPC/kunoichi/narika/body.webp', gallery=False),
                                              declare('narika happy', 'NPC/kunoichi/narika/body.webp', gallery=False),
                                              declare('narika sad', 'NPC/kunoichi/narika/body.webp', gallery=False),
                                              declare('narika blush', 'NPC/kunoichi/narika/body.webp', gallery=False),
                                              declare('narika ninja', 'NPC/kunoichi/narika/attack.webp', 'f', x=0.6, y=0.6),
                                              declare('narika school', 'NPC/kunoichi/narika/body school.webp'),
                                              declare('side narika', 'NPC/kunoichi/narika/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika normal', 'NPC/kunoichi/narika/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika ninja', 'NPC/kunoichi/narika/portrait ninja.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika surprise', 'NPC/kunoichi/narika/portrait surprise.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika angry', 'NPC/kunoichi/narika/portrait angry.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika happy', 'NPC/kunoichi/narika/portrait happy.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika sad', 'NPC/kunoichi/narika/portrait sad.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side narika blush', 'NPC/kunoichi/narika/portrait blush.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),

                                              declare('mizuki', 'NPC/kunoichi/mizuki/body.webp'),
                                              declare('mizuki normal', 'NPC/kunoichi/mizuki/body.webp', gallery=False),
                                              declare('mizuki happy', 'NPC/kunoichi/mizuki/body.webp', gallery=False),
                                              declare('mizuki sad', 'NPC/kunoichi/mizuki/body.webp', gallery=False),
                                              declare('mizuki angry', 'NPC/kunoichi/mizuki/body.webp', gallery=False),
                                              declare('side mizuki', 'NPC/kunoichi/mizuki/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side mizuki normal', 'NPC/kunoichi/mizuki/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side mizuki ninja', 'NPC/kunoichi/mizuki/portrait ninja.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side mizuki happy', 'NPC/kunoichi/mizuki/portrait happy.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side mizuki sad', 'NPC/kunoichi/mizuki/portrait sad.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side mizuki angry', 'NPC/kunoichi/mizuki/portrait angry.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                              declare('side mizuki naked', 'NPC/kunoichi/mizuki/portrait naked.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),

                                              declare('kunoichi', 'NPC/kunoichi/kunoichi.webp', 'f', x=1.25, y=1.25),
                                              declare('kunoichi reversed', im.Flip(im.FactorScale('NPC/kunoichi/kunoichi.webp', 1.25, 1.25), horizontal=True)),
                                              declare('side kunoichi', 'NPC/kunoichi/kunoichi portrait.webp', gallery=False),
                                              ]),

                            # Extras
                                ('gknight', [declare('gknight', 'NPC/Misc/girl_knight.webp'),]),
                                ('princess1', [declare('princess1', 'NPC/Misc/princess1.webp'),]),
                                ('princess2', [declare('princess2', 'NPC/Misc/princess2.webp'),]),
                                ('priest', [declare('priest', 'NPC/Misc/priest.webp'),]),
                                ('mage', [declare('mage', 'NPC/Misc/mage.webp'),]),
                                ('bm1', [declare('bm1', 'NPC/Misc/bm1.webp'),]),
                                ('bm2', [declare('bm2', 'NPC/Misc/bm2.webp'),]),
                                ('king', [declare('king', 'NPC/Misc/king2.webp', 'p', x=500, y=500),]),
                                ('hood', [declare('hood', 'NPC/Misc/hood.webp'),]),

                                ("guard", [
                                        declare('guard', 'NPC/Misc/guard.webp', 'f', x=0.5, y=0.5),
                                        declare('side guard', 'NPC/Misc/guard portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare("guard party", im.Composite(
                                                                             (320, 760),
                                                                             (0, 0), im.FactorScale("NPC/Misc/guard.webp",0.5,0.5),
                                                                             (170, 100), im.FactorScale("NPC/Misc/Party hat.webp", 0.5, 0.5),
                                                                             )),
                                        ]),

                                ("thugs", [
                                        declare('side thug', 'UI/customers/thug.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),

                                        declare('thug1', 'NPC/Misc/thug1.webp', 'f', x=0.5, y=0.5),
                                        declare('thug1 attack', 'NPC/Misc/thug1 attack.webp'),
                                        declare('side thug1', 'NPC/Misc/thug1 portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),

                                        declare('thug2', 'NPC/Misc/thug2.webp', 'f', x=0.5, y=0.5),
                                        declare('thug2 attack', 'NPC/Misc/thug2 attack.webp'),
                                        declare('side thug2', 'NPC/Misc/thug2 portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('thug2 burnt', 'NPC/Misc/burnt.webp'),

                                        declare('thugs attack', 'NPC/Misc/thugs attack.webp'),
                                        ]),


                                ("henchman", [declare('henchman', 'NPC/Misc/henchman.webp')]),
                                ("masked thug", [declare('masked_thug', 'NPC/Misc/masked thug.webp')]),
                                ("stranger", [declare('stranger', 'NPC/Misc/stranger.webp')]),
                                ("sewer rapist", [declare('sewer_rapist', 'NPC/Misc/sewer rapist.webp', 'f', x= 0.75, y= 0.75)]),
                                ("judge", [declare('judge', 'NPC/Misc/judge.webp'), declare('side judge', 'NPC/Misc/judge portrait.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),]),
                                ("knight", [declare('knight', 'NPC/Misc/knight.webp', 'f', x= 0.8, y= 0.8), declare('side knight', 'NPC/Misc/knight portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),]),

                                ("templars", [
                                        declare('templar', 'NPC/Misc/templar.webp', 'f', x=0.8, y=0.8),
                                        declare('initiate', 'NPC/Misc/initiate.webp', 'f', x=0.9, y=0.9),
                                        declare('side templar', 'NPC/Misc/knight portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side initiate', 'NPC/Misc/soldier portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("monsters", [
                                        declare('spirit', 'NPC/Misc/spirit.webp', 's', wide=True),
                                        declare('side spirit', 'NPC/Misc/spirit portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('sewer_monster', 'NPC/Misc/sewer monster.webp'),
                                        declare('sewer_monster happy', 'NPC/Misc/sewer monster friendly.webp'),
                                        declare('tentacle_monster', 'NPC/Misc/tentacle_monster.webp', 'f', x=1.25, y=1.25),
                                        ]),

                                ("mare", [
                                        declare('mare', 'NPC/Misc/mare.webp', 'f', x=1.3, y=1.3),
                                        ]),

                                ("demons", [
                                        declare('blue_demon', 'NPC/Misc/blue demon.webp', 'f', x=0.8, y=0.8),
                                        declare('side blue_demon', 'NPC/Misc/blue demon portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('red_demon', 'NPC/Misc/red demon.webp', 'f', x=0.8, y=0.8),
                                        declare('side red_demon', 'NPC/Misc/red demon portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("skeleton", [
                                        declare('skeleton', 'NPC/Misc/skeleton.webp'),
                                        declare('side skeleton', 'NPC/Misc/skeleton portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ]),

                                ("ogres", [declare('ogre', 'NPC/Misc/ogre.webp')]),

                                ("mask", [declare('side mask unknown', 'NPC/Misc/killer.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side mask', 'NPC/The Mask/portrait.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side mask normal', 'NPC/The Mask/portrait.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False)]),

                                ("ninja guests", [declare('hokoma_warrior', 'NPC/kunoichi/guests/guest1.webp'), declare('magical_girl', 'NPC/kunoichi/guests/guest2.webp'), declare('girl_scientist', 'NPC/kunoichi/guests/guest3.webp')]),

                            ])


    game_image_dict["unused"] = {

                                "unused for gallery (stand-alone portraits)" : [
                                        declare('side slavegirl1', 'NPC/Misc/slave1.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side slavegirl2', 'NPC/Misc/slave2.webp', 's', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side shopgirl', 'NPC/Misc/shop_girl.webp', 's', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side hmas', 'NPC/Hmas/portrait.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side raccoon', 'NPC/Misc/raccoon.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sailor', 'NPC/Misc/sailor.png', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side party_girl', 'NPC/Misc/party girl.png', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side nun', 'NPC/Misc/nun.png', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side kimono_lady', 'NPC/Misc/kimono lady.png', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side young_maid', 'NPC/Misc/maid.png', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side diplomat', 'NPC/Misc/diplomat.png', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side sorceress', 'NPC/Misc/sorceress.png', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side naked_lady', 'NPC/Misc/naked lady.png', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('judge_head', 'NPC/Misc/judge head.webp'),
                                        declare('panties', 'items/accessory/lace panties.webp'),
                                        declare_multiple('house%s', 'minigame/house%s.png', start=1, finish=8),
                                        declare_multiple('passerby%s', 'minigame/passerby%s.png', start=1, finish=9),
                                        declare_multiple('ninja%s', 'minigame/ninja%s.png', start=0, finish=3),
                                        declare_multiple('guest%s', 'minigame/guest%s.png', start=1, finish=3),
                                        declare('toy hammer', 'items/Weapons/toy hammer.webp', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side papa', 'NPC/Misc/freak portrait.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        declare('side papa_apprentice', 'NPC/Misc/freak apprentice.jpg', 'p', x=res_portrait_size, y=res_portrait_size, gallery=False),
                                        ],

                            }

    ## MISC PICTURES ##

    game_image_dict["Misc"] = {

                                "title" : [declare("bg title", "ui/theme.jpg", "s", wide=True, unlock=True)],

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
                                        declare('bg waitress', 'backgrounds/waitress.jpg', 'p', wide=True, unlock=True),
                                        declare('bg stripper', 'backgrounds/stripper.jpg', 'p', wide=True, unlock=True),
                                        declare('bg masseuse', 'backgrounds/masseuse.jpg', 'p', wide=True, unlock=True),
                                        declare('bg geisha', 'backgrounds/geisha.jpg', 'p', wide=True, unlock=True),
                                        declare('bg whore', 'backgrounds/whore.jpg', 'p', wide=True, unlock=True),
                                        declare('bg rest', 'backgrounds/rest.jpg', 'p', wide=True, unlock=True),
                                        ],
                                "zodiac" : [declare('bg zodiac', 'backgrounds/zodiac.jpg', 'p'),],

                                "tavern" : [
                                        declare('bg tavern_man', 'NPC/Misc/tavern_man.jpg'),
                                        declare('symbol', 'backgrounds/thief symbol.jpg'),
                                        ],

                                "elves" : [declare('bg elves', 'backgrounds/elves.webp', 'p')],

                                "mask events" : [declare('bg mask escape', 'NPC/The Mask/escape.webp', 'p')],

                                "misc" : [declare('bg letter', 'backgrounds/letter.jpg', 'p', gallery=False)],

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

define circleout = ImageDissolve(im.Scale("transitions/id_circleiris.png", config.screen_width, config.screen_height), 2.0)

define circlein = ImageDissolve(im.Scale("transitions/id_circleiris.png", config.screen_width, config.screen_height), 2.0, reverse = True)

define satella_blink = ImageDissolve(im.Scale("NPC/Satella/body2.webp", config.screen_width, config.screen_height), 2.0, reverse = True) # AlphaDissolve("NPC/Satella/body2.webp", delay=1.0, alpha=True, reverse=False)

# From the 'Utsukushii Effects' renpy tutorial
define flashbackin = ImageDissolve(im.Scale("transitions/zigzag.png", config.screen_width, config.screen_height), 3.0, 50)
define flashbackout = ImageDissolve(im.Scale("transitions/zigzag.png", config.screen_width, config.screen_height), 3.0, 50)
##

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

define doubleflash = MultipleTransition([True, Fade(0.1, 0.0, 0.5, color="#fff"), True,
                                         Fade(0.1, 0.0, 0.5, color="#fff"),True])



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

    def unlock_pic(pic):
        if pic not in persistent.seen_list:
            persistent.seen_list.append(pic)

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

        textbutton "CG - Game" action (ShowMenu("gallery", gal_type="ev"), SetVariable("gallery_type", "ev")) xsize int(config.screen_width*0.1851)

        textbutton "CG - Girl packs" action (ShowMenu("gallery", gal_type="gp"), SetVariable("gallery_type", "gp")) xsize int(config.screen_width*0.1851)

        textbutton "Achievements" action ShowMenu("achievements") xsize int(config.screen_width*0.1851)

        textbutton "Main Menu" action Function(renpy.full_restart) xsize int(config.screen_width*0.1851)


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

                for i in xrange(shown_pics):

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
                                if persistent.debug_pic_counter and gal_type == "gp":
                                    text _("Used %s times" % persistent.debug_pic_counter_dict[pic.imgname]) align (0.5, 1.0) size int(config.screen_height*0.02)#!


            $ max_page = (len(gal.blist)-1) // shown_pics

            text "Page " + str(page+1) + "/" + str(max_page+1) size int(config.screen_height*0.02)

            frame background None xfill True:
    #            textbutton "Start Slideshow" action gal.ToggleSlideshow()

                if page > 0:
                    key "K_LEFT" action SetScreenVariable("page", page-1)
                    key "repeat_K_LEFT" action SetScreenVariable("page", page-1)
                    textbutton "Previous" action SetScreenVariable("page", page-1) xalign 0.05
                if page < max_page:
                    key "K_RIGHT" action SetScreenVariable("page", page+1)
                    key "repeat_K_RIGHT" action SetScreenVariable("page", page+1)
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

        if gallery_type == "ev":
            textbutton _("prev") action gallery.Previous(unlocked=True)
            textbutton _("next") action gallery.Next(unlocked=True)
            textbutton _("slideshow") action gallery.ToggleSlideshow()
        textbutton _("return") action gallery.Return()

    python:
        style.gallery = Style(style.default)
        style.gallery_button.background = None
        style.gallery_button_text.color = "#666"
        style.gallery_button_text.hover_color = "#fff"
        style.gallery_button_text.selected_color = "#fff"
        style.gallery_button_text.size = int(config.screen_height*0.0148)


#### END OF BK GALLERY ####
