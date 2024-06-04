############ JOBGIRL EVENTS VARIABLES ############


init -3 python:

# These lines won't work as 'init' because they will be reset everytime the player starts the game.
# I moved them to the beginning of the first event.

#     jobgirl_romance = 0
#     jobgirl_corruption = 0
#     anika_sex = False


## sounds

    ## part 1 : riddle
    m_jobgirl_1_suspence = "Tibet.mp3"

    ## part 2 : beach
    s_moans_friend = "moans1.wav"

## characters

define anika = Character("Anika", image="anika", window_left_padding=int(config.screen_height*0.205))
image anika = im.FactorScale("NPC/Jobgirl/beach/anika body.webp", 0.7, 0.7)
image side anika = "NPC/Jobgirl/beach/anika portrait.webp"

define elflady = Character("Insert-Name", image="elflady")
image elflady = "NPC/Jobgirl/elf house/lady body.gif"
image side elflady = "NPC/Jobgirl/elf house/lady portrait.webp"



## images

    ## part 1 : riddle

image jobgirl_riddle = ProportionalScale("NPC/Jobgirl/special_riddle.webp", config.screen_width, config.screen_height)
image teasing_cleavage = ProportionalScale("NPC/Jobgirl/teasing cleavage.webp", config.screen_height, config.screen_width)

    ## part 2 : beach

image bg beach = "backgrounds/beach.jpg"
image beach_arrival = "NPC/Jobgirl/beach/beach arrival.webp"
image jobgirl_bikini = ProportionalScale("NPC/Jobgirl/beach/beach bikini.webp", config.screen_width, config.screen_height)
image beach_friend_1 = ProportionalScale("NPC/Jobgirl/beach/beach friend 1.webp", config.screen_width, config.screen_height)
image beach_friend_2 = "NPC/Jobgirl/beach/beach friend 2.webp"
image beach_friend_3 = "NPC/Jobgirl/beach/beach friend 3.webp"
image beach_sit = ProportionalScale("NPC/Jobgirl/beach/beach sit.webp", config.screen_width, config.screen_height)
image beach_stand_1 = ProportionalScale("NPC/Jobgirl/beach/beach stand1.webp", config.screen_width, config.screen_height)
image beach_stand_2 = ProportionalScale("NPC/Jobgirl/beach/beach stand2.webp", config.screen_width, config.screen_height)
image beach_sunscreen = "NPC/Jobgirl/beach/beach sunscreen.webp"
image beach_surprised = ProportionalScale("NPC/Jobgirl/beach/beach surprised.webp", config.screen_width, config.screen_height)
image beach_teasing = "NPC/Jobgirl/beach/beach teasing.webp"
image beach_teasing_butt = "NPC/Jobgirl/beach/beach teasing butt.webp"
image beach_teasing_naked = "NPC/Jobgirl/beach/beach teasing naked.webp"
image beach_topless = ProportionalScale("NPC/Jobgirl/beach/beach topless.webp", config.screen_width, config.screen_height)
image beach_lay_down = "NPC/Jobgirl/beach/beach lay down.webp"
image special_beach = "NPC/Jobgirl/special beach.webp"

image friend_sunbathing = ProportionalScale("NPC/Jobgirl/beach/friend sunbathing.webp", config.screen_width, config.screen_height)
image friend_teasing1 = ProportionalScale ("NPC/Jobgirl/beach/friend teasing1.webp", config.screen_width, config.screen_height)
image friend_teasing2 = ProportionalScale ("NPC/Jobgirl/beach/friend teasing2.webp", config.screen_width, config.screen_height)
image friend_boobs = ProportionalScale("NPC/Jobgirl/beach/friend boobs.webp", config.screen_width, config.screen_height)
image friend_cum_body1 = ProportionalScale ("NPC/Jobgirl/beach/friend cum body1.webp", config.screen_width, config.screen_height)
image friend_cum_body2 = ProportionalScale ("NPC/Jobgirl/beach/friend cum body2.webp", config.screen_width, config.screen_height)
image friend_orgasm = ProportionalScale ("NPC/Jobgirl/beach/friend orgasm.webp", config.screen_width, config.screen_height)
image friend_stand1 = "NPC/Jobgirl/beach/friend stand1.webp"
image friend_shower = ProportionalScale ("NPC/Jobgirl/beach/friend shower.webp", config.screen_width, config.screen_height)
image friend_doggy = ProportionalScale ("NPC/Jobgirl/beach/friend doggy.webp", config.screen_width, config.screen_height)

    ## part 3 : elf house

image elf_house_hall = "NPC/Jobgirl/elf house/hallroom.webp"
image elf_house_inner = "NPC/Jobgirl/elf house/inside.webp"

image elf_lady_1 = "NPC/Jobgirl/elf house/lady 1.webp"
image elf_lady_2 = "NPC/Jobgirl/elf house/lady 2.webp"
image elf_lady_3 = "NPC/Jobgirl/elf house/lady 3.webp"
image elf_lady_4 = "NPC/Jobgirl/elf house/lady 4.webp"
image elf_lady_5 = "NPC/Jobgirl/elf house/lady 5.webp"
image elf_lady_6 = "NPC/Jobgirl/elf house/lady 6.webp"
