# The script of the game goes in this file.

image bg pavement = Tile("minigame/bg pavement.jpg")
image countdown = DynamicDisplayable(show_countdown)

init -2 python:

    def get_ninja_district(ninja):
        if ninja == NPC_narika:
            return "The Slums"
        elif ninja == NPC_mizuki:
            return "The Docks"
        elif ninja == NPC_haruka:
            return "The Warehouse"

    def shuffle_ninja_location(ninja):
        dis = get_ninja_district(ninja)
        ninja.loc = rand_choice(location_dict[dis])
        for loc in location_dict[dis]:
            story_flags["ninja hunt hide " + loc.name] = False

    def lock_ninja_locations(ninja):
        ninja.flags["locked"] = True # Tracks that a kunoichi hunt has been locked
        for loc in location_dict[get_ninja_district(ninja)]:
            story_flags["ninja hunt hide " + loc.name] = True

    def init_ninja_game():
        NPC_narika.sprite = "ninja1"
        NPC_mizuki.sprite = "ninja2"
        NPC_haruka.sprite = "ninja3"

        # First location is set, then it's randomized
        NPC_narika.loc = thieves_guild
        NPC_mizuki.loc = beach
        NPC_haruka.loc = prison

        # Guest setup
        NPC_narika.guest = "guest3"
        NPC_mizuki.guest = "guest2"
        NPC_haruka.guest = "guest1"

        NPC_narika.flags["hunt stage"] = NPC_mizuki.flags["hunt stage"] = NPC_haruka.flags["hunt stage"] = 0

        story_flags["ninja hunt"] = "start"

        shop.items += [makibishi] # Adds a single makibishi to the shop (more will be generated each week)

    def show_countdown(st, at):
        if st >= njgame.countdown:
            njgame.over = True
            return Text("{size=48}{color=#FFFF00}0"), None
        else:
            return Text("{size=48}{color=#FFFF00}" + str(int(20-st))), 0.1

    def change_cursor(type="default"):
        if type == "default":
            setattr(config, "mouse", None)
        elif type == "1":
            setattr(config, "mouse", {"default": [("minigame/toy hammer 1.png", 0, 0)]})
        elif type == "2":
            setattr(config, "mouse", {"default": [("minigame/toy hammer 2.png", 0, 0)]})

    class NinjaGame(object):

        def __init__(self, ninja, guest=None, timer=0.8, countdown = 20, special=None):
            self.ninja = ninja
            self.sprite = self.get_ninja_sprite()
            self.guest = guest # Guest encounter
            self.guest_hits = 0
            self.timer = timer
            self.countdown = countdown
            self.special = special
            self.hits = 0
            self.misses = 0
            self.over = False

            self.generate_houses(x_space = 0.15, y_space = 0.2)

        def get_pic(self):
            if self.ninja.flags["hunt stage"]: # Hunt stage > 0
                return ninja.name.lower()
            else:
                return "kunoichi" # Uses unknown sprite until the ninja has been met

        def get_ninja_sprite(self):
            if self.ninja.flags["hunt stage"]: # Hunt stage > 0
                return ninja.sprite
            else:
                return "ninja0" # Uses unknown sprite until the ninja has been met

        def generate_houses(self, x_space, y_space):
            self.houses = {}

            x_nb = int(0.9 // x_space)
            y_nb = int(0.9 // y_space)

            for x in xrange(x_nb):
                for y in xrange(y_nb):
                    self.houses[x, y] = [rand_choice(house_templates), int((x+1)*x_space*config.screen_width) - 50, int((y+1)*y_space*config.screen_height) + 20]

            self.x_max = x_nb - 1
            self.y_max = y_nb - 1

        def reset_positions(self):
            self.available_positions = []

            for x in xrange(self.x_max+1):
                for y in xrange(self.y_max+1):
                    self.available_positions.append((x, y))

            renpy.random.shuffle(self.available_positions)

        def rand_house_move(self):
            x, y = self.available_positions.pop()

            x2 = x
            y2 = y

            xlist = []
            ylist = []

            xlist.append(x)
            if x > 1:
                xlist.append(x-2)
            if x > 0:
                xlist.append(x-1)
            if x < self.x_max-1:
                xlist.append(x+2)
            if x < self.x_max:
                xlist.append(x+1)

            ylist.append(y)
            if y > 1:
                ylist.append(y-2)
            if y > 0:
                ylist.append(y-1)
            if y < self.y_max-1:
                ylist.append(y+2)
            if y < self.y_max:
                ylist.append(y+1)

            while (x, y) == (x2, y2):
                x2, y2 = rand_choice(xlist), rand_choice(ylist)

            return self.houses[x, y][1:], self.houses[x2, y2][1:]

        def randomize_duration(self):
            return self.timer + renpy.random.random() * 0.5 - 0.25


screen no_click:
    button xsize xres() ysize yres() background None

screen moving_buttons(but_list):
    tag njgame_moving_buttons

    default t = 0
    default fast_speed = 0.3

    fixed:
        for img, notification, but_pos in but_list:

            if njgame.special == "fast" and img == njgame.sprite:
                $ dur = fast_speed
            else:
                $ dur = njgame.randomize_duration()

            button at move_to(but_pos[0], but_pos[1], dur):
                background None
                if img == njgame.sprite:
                    if not njgame.special == "fast" or t <= fast_speed:
                        action (Function(renpy.notify, notification), SetField(njgame, "hits", njgame.hits+1), Return(img))
                elif img == njgame.guest:
                    action (Function(renpy.notify, notification), SetField(njgame, "guest_hits", njgame.guest_hits+1), Return(img))
                else:
                    action (Function(renpy.notify, notification), SetField(njgame, "misses", njgame.misses+1), Return(img))
                add img

    timer njgame.timer * 1.2 action Return(False)
    timer 0.05 action SetScreenVariable("t", t + 0.05)


screen score():
    frame xalign 0.0 yalign 1.0 xpadding 40 ypadding 40 xmargin 20 ymargin 20 background c_ui_darker:
        has hbox spacing 50

        text "{b}Hits{/b} %s" % ("X"*njgame.hits + " "*(3-njgame.hits)) color c_steel

        text "{b}Misses{/b} %s" % ("X"*njgame.misses + " "*(3-njgame.misses)) color c_lightred

# The game starts here.

label ninja_game(ninja): # Where ninja is an NPC object

    if not story_flags["ninja hunt seen intro"]:
        play music m_suzume fadein 3.0

    suzume shrewd "Wait, [MC.name]... I sense something." with vpunch

    python:
        house_templates = ["house1", "house2", "house3", "house4", "house5", "house6", "house7", "house8", ]

        special = False

        if ninja.flags["hunt stage"] == 2: # At stage 2, the ninja is uncatchable (stage 3 is unlocked through the story)
            special = {"Narika" : "fast", "Mizuki" : "rain", "Haruka" : "quake"}[ninja.name]

        njgame = NinjaGame(ninja=ninja, guest=ninja.guest, special=special)

    show speed_effect with dissolve
    show expression njgame.get_pic() at ninja_move with easeinright

    call ninja_hunt_begins(ninja) from _call_ninja_hunt_begins

    hide expression njgame.get_pic() with easeoutleft
    hide speed_effect with dissolve

    call run_ninja_game(njgame) from _call_run_ninja_game

    if njgame.special:
        $ centered(event_color["bad"] % "\n\n{b}拦截失败……{/b}")
        call ninja_intercept(ninja, njgame.special) from _call_ninja_intercept
    elif _return == "guest":
        $ centered(event_color["good"] % "\n\n{b}特殊遭遇！{/b}")
        call expression ("ninja_" + njgame.guest) from _call_expression_7
    elif _return == "ninja":
        $ centered(event_color["good"] % "\n\n{b}成功拦截！{/b}")
        call ninja_intercept(ninja, njgame.special) from _call_ninja_intercept_1
    else:
        $ centered(event_color["bad"] % "\n\n{b}她逃走了！{/b}")

    hide screen score

    return



label run_ninja_game(njgame): # Returns "ninja" if ninja caught, "guest" if guest caught, False otherwise

    $ renpy.free_memory()

    scene bg pavement with fade

    python:
        i = 0
        for house, x, y in njgame.houses.values():
            renpy.show(house, at_list = [Transform(xpos=x, ypos=y, xanchor=0.5, yanchor=1.0)], tag="h"+str(i))
            i += 1

    show expression njgame.sprite at truecenter with blinds

    if not story_flags["ninja hunt seen intro"]:
        call ninja_hunt_intro() from _call_ninja_hunt_intro

    else:
        stop music fadeout 3.0

        if njgame.special == "rain":
            play music m_rain fadein 2.0
            show rain
        else:
            play music m_kunoichi fadein 2.0

    $ _skipping = False

    $ stage_name = str(ninja.flags["hunt stage"] + 1)

    if njgame.special:
        $ stage_name += "*锁定*"

    $ centered(event_color["special"] % "\n\n{b}女忍者狩猎开始\n回合 " + stage_name + "{/b}")

    if MC.has_item("makibishi"):
        if not njgame.special:
            menu:
                "Do you want to use your makibishi to automatically catch your target?"

                "Yes (spend 1 makibishi)":
                    play sound s_dice
                    $ njgame.hits = 3
                    $ MC.items.remove(makibishi)
                "No":
                    pass

    hide expression njgame.sprite with blinds

    $ change_cursor("2")
    $ config.keymap['button_ignore'] = []
    $ config.keymap['button_select'] = ['mousedown_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT']

    show screen score
    show countdown:
        xalign 0.5
        yalign 0.95

    while njgame.hits < 3 and njgame.misses < 3 and not njgame.over:
        $ renpy.block_rollback()
        $ njgame.reset_positions()

        $ but_list = [(njgame.sprite, "Hit!!!", njgame.rand_house_move()), ("passerby1", "Miss...", njgame.rand_house_move()), ("passerby2", "Miss...", njgame.rand_house_move()), ("passerby3", "Miss...", njgame.rand_house_move()), ("passerby4", "Miss...", njgame.rand_house_move()), ("passerby5", "Miss...", njgame.rand_house_move()), ("passerby6", "Miss...", njgame.rand_house_move()), ("passerby7", "Miss...", njgame.rand_house_move()), ("passerby8", "Miss...", njgame.rand_house_move()), ("passerby9", "Miss...", njgame.rand_house_move())]

        if njgame.guest:
            $ but_list.append((njgame.guest, "Uh?!?", njgame.rand_house_move()))

        # Randomizes buttons
        $ but_list = rand_choice(but_list, 5)

        # Activates effects
        if njgame.special == "rain" and renpy.random.random() > 0.3:
            if renpy.random.random() > 0.66:
                show lightning with doubleflash
                play sound s_thunder
            else:
                show lightning with flash
                play sound s_fire
            hide lightning

        show screen no_click()

        if njgame.special=="quake":
            $ renpy.pause(renpy.random.random()*0.5, hard=True)
            play sound s_crash
            call screen moving_buttons(but_list) with quake
        else:
            call screen moving_buttons(but_list) with dissolve

        # Catch result

        if _return:
            if njgame.ninja.flags["hunt stage"] == 2 and _return.startswith("ninja"):
                if njgame.ninja.name == "Narika":
                    $ x,y = renpy.get_mouse_pos()

                    play sound s_spell

                    show expression "ninja1" as n1:
                        xpos x ypos y xanchor 0.5 yanchor 0.5
                        ease 0.3 xpos x+150 ypos y+150
                    show expression "ninja1" as n2:
                        xpos x ypos y xanchor 0.5 yanchor 0.5
                        ease 0.3 xpos x-150 ypos y+150
                    show expression "ninja1" as n3:
                        xpos x ypos y xanchor 0.5 yanchor 0.5
                        ease 0.3 xpos x+150 ypos y-150
                    show expression "ninja1" as n4:
                        xpos x ypos y xanchor 0.5 yanchor 0.5
                        ease 0.3 xpos x-150 ypos y-150

                    with None

                    hide n1
                    hide n2
                    hide n3
                    hide n4
                    with Dissolve(0.2)

                elif njgame.ninja.name == "Mizuki":
                    $ x,y = renpy.get_mouse_pos()

                    play sound s_thunder

                    show expression _return with flash:
                        xpos x
                        ypos y

                    hide expression _return

                elif njgame.ninja.name == "Haruka":
                    $ x,y = renpy.get_mouse_pos()

                    play sound s_clash

                    $ shake_mouse(500)

                    show expression _return:
                        xpos x
                        ypos y

                    hide expression _return

            else:
                $ x,y = renpy.get_mouse_pos()
                play sound s_punch

#                 call ninja_hunt_react(_return)

                show expression _return:
                    xpos x
                    ypos y
                    xanchor 0.5
                    yanchor 0.5
                    parallel:
                        rotate 0
                        linear 1.0 rotate 720
                    parallel:
                        zoom 1.0
                        ease 0.5 zoom 2.0
                        ease 0.5 zoom 1.0
                    # pause 1.0
                with vpunch
                hide expression _return

                if njgame.guest_hits >= 3:
                    $ njgame.over = True

            call ninja_hunt_react(_return) from _call_ninja_hunt_react

    $ change_cursor()
    hide countdown
    hide screen score
    hide screen no_click
    $ config.keymap['button_ignore'] = ['mousedown_1']
    $ config.keymap['button_select'] = ['mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT']

    stop music fadeout 3.0
    $ _skipping = True

    if njgame.guest_hits >= 3:
        play sound s_spell
        $ njgame.ninja.guest = None # Disables guest to avoid multiple event proc
        return "guest"
    elif njgame.hits >= 3:
        play sound s_spell
        return "ninja"
    else:
        play sound s_fizzle
        return False
