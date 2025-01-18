####     ADVANCED NOTIFICATION FUNCTION         ####
## This is inspired by multi_notify by RenpyRemix ##
## https://github.com/RenpyRemix/multi-notify     ##
## Thanks to them.                                ##


# Global list of notifications
define notify_list = []
define notify_history = []

# Duration the full ATL takes
define notify_duration = 2.5

# Max number we store for reviewing in the history screen
define notify_history_length = 40

# Font size and color
define notify_font = 0.02 * config.screen_height
define notify_color = "#FF3"
define debug_notify_color = "#FF69B4"


init python:

    import time

    class Notification(object):
        def __init__(self, txt, pic="", col="FFF", debug_txt="", priority=False):
            global notify_list

            self.txt = txt
            if col in color_dict.keys(): # color_dict is specific to BK
                self.color = color_dict[col]
            else:
                self.color = col
            self.pic = pic

            if debug_txt and debug_mode: # debug_txt will be added to the notification in debug mode only
                if txt: self.txt += " "
                self.txt += "{color=%s}%s{/color}" % (debug_notify_color, debug_txt)

            self.appear_time = time.time() #+ len(notify_list)*notify_duration
            self.disappear_time = self.appear_time + notify_duration
            if priority:
                notify_list.insert(0, self)
            else:
                notify_list.append(self)

        def disappear(self):
            global notify_list
            global notify_history

            notify_history.append(self)
            notify_list.remove(self)

            if len(notify_history) > notify_history_length:
                notify_history = notify_history[-notify_history_length:]

    def notify(txt="", pic="", col=notify_color, debug_txt="", priority=False):

        if isinstance(pic, Picture): # Specific for BK, intercepts Picture objects here to make it uncomplicated to invoke
            pic = pic.path

        if txt or (debug_mode and debug_txt):
            msg = Notification(txt, pic, col, debug_txt)
            renpy.show_screen('notify_container')
            renpy.restart_interaction()

    def priority_notify(*args, **kwargs):
        notify(*args, priority=True, **kwargs)

    def debug_notify(debug_txt, pic=""):
        if debug_mode:
            notify(debug_txt=debug_txt, pic=pic, priority=True)

    def finish_notify(trans, st, at):

        for msg in notify_list:
            if time.time() > msg.disappear_time:
                msg.disappear()

        if not notify_list:
            renpy.hide_screen('notify')

        # renpy.restart_interaction()

        return None

## Sets default renpy notify to this
define config.notify = notify

transform notify_appear(_delay=0.0):

    pause _delay
    alpha 0 xanchor 1.0 xpos 0.0
    linear notify_duration / 8 alpha 1.0 xalign 0.0
    pause notify_duration / 2
    linear notify_duration * 3/8 alpha 0.0
    function finish_notify
    pause 0.5 # Slower pause doesn't work because ???

screen notify_item(msg, _pos=0, use_atl=True):
    default pic_size = int(notify_font*1.25)

    frame background c_ui_dark:

        if use_atl: # ATL not used for history
            at notify_appear(_delay=_pos*0.15)

        hbox spacing 10:
            if msg.pic:
                $ _pic = Picture(path = msg.pic) # Fix by Mirarara
                frame style "inv_no_padding" ysize pic_size:
                    add _pic.get() fit "contain" # Fix by Mirarara
            text msg.txt color msg.color size notify_font yalign 0.5 outlines [(abs(1), "#000", abs(0), abs(0))] #drop_shadow (2, 2)


screen notify_container:

    zorder 100

    frame background None:
        pos (0.015, 0.1)
        xsize 0.4
        ysize 0.05

        if notify_list:
            vbox:
                for i in range(len(notify_list)):
                    use notify_item(notify_list[i], _pos=i) #!

screen notify_history:

    # key "mouseup_1" action Hide()
    key "mouseup_3" action Hide()

    text "(%i)" % len(notify_history) size res_font(14)

    viewport:
        # scrollbars "vertical"
        mousewheel True
        yinitial 1.0
        xmaximum 0.5
        yfill True
        # pos (0.015, 0.1)

        vbox:
            xfill False
            spacing 5

            for msg in notify_history:
                use notify_item(msg, use_atl=False)
