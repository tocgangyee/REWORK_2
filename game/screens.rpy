﻿################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
    size 50
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style prompt_title_text is gui_text:
    properties gui.text_properties("label", accent=True)
    size 70
    color Colors.Teal.value
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    if sayVariable["state"] == SayState.CutScene:
        window:
            xalign 0.5
            xfill True
            yalign gui.textbox_yalign
            ysize 320
            background Image("gui/phone/textbox_s.png", xalign=0.5, yalign=1.0)
            id "window"

            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what"

        ## If there's a side image, display it above the text. Do not display on the
        ## phone variant - there's no room.
        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0
    else:
        window:
            id "window"

            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what"

        ## If there's a side image, display it above the text. Do not display on the
        ## phone variant - there's no room.
        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style cutscene_window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/phone/textbox_l.png", xalign=0.5, yalign=1.0)

# style cutscene_window:
#     xalign 0.5
#     xfill True
#     yalign gui.textbox_yalign
#     ysize 320

#     background Image("gui/phone/textbox_l.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.7
    yanchor 0
    ysize 320

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    padding (0, 20, 0, 20)


style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 1.0
            yalign 1.0
            yanchor 0

            ypos 250

            # textbutton _("Back") action Rollback()
            # textbutton _("History") action ShowMenu('history')
            # textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            # textbutton _("Auto") action Preference("auto-forward", "toggle")
            # textbutton _("Save") action ShowMenㄴu('save')
            # textbutton _("Q.Save") action QuickSave()
            # textbutton _("Q.Load") action QuickLoad()
            if _in_replay:
                textbutton _("Back") action EndReplay(confirm=True):
                    right_padding 20
            else:
                textbutton _("Menu") action Show('ingame_popup'):
                    right_padding 20


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text:
    # color gui.idle_color
    outlines [ (absolute(4), Colors.Black.value, absolute(0), absolute(0)) ]

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

init python:
    def CustomStart(skip_trigger, value):
        skip_trigger = value

screen start_popup():
    modal True

    zorder 200

    style_prefix "start_popup"

    add "gui/overlay/confirm.png"
    add "images/popup_bg.png" at Transform(size=(1200, 1500)):
        xalign 0.5
        yalign 0.5

    frame:
        background None

        label _("Game mode"):
            style "prompt_title"
            xalign 0.5
            ypos 300

        vbox:
            box_wrap True
            xsize 700
            ypos 500
            xalign 0.5

            text _("{b}Story mode{/b}"):
                color gui.accent_color
                outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

            null height (1 * gui.pref_spacing)

            text _("Shows all dialog and narration in the game. Great for those who like to judge their progress carefully and play strategically."):
                outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
                size 40
            
            null height (2 * gui.pref_spacing)

            text _("{b}Rush mode{/b}"):
                color gui.accent_color
                outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

            null height (1 * gui.pref_spacing)

            text _("Suppresses all dialog and narration in the game. Great if you want to play quickly."):
                outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
                size 40
        
        vbox:
            xalign 0.5
            ypos 1100

            textbutton _("Story mode") action [SetVariable("skip_trigger", False), Start()]:
                xalign 0.5

            null height (1 * gui.pref_spacing)

            textbutton _("Rush mode") action [SetVariable("skip_trigger", True), Start()]:
                xalign 0.5

        textbutton _("Close") action Hide("start_popup"):
            xalign 0.5
            ypos 1500

style start_popup_frame is gui_frame:
    xsize 800
style start_popup_prompt is gui_prompt
style start_popup_prompt_text is gui_prompt_text:
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
style start_popup_button is gui_medium_button
style start_popup_button_text is gui_medium_button_text:
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    size 70

style start_popup_frame:
    # background Frame([ "images/popup_bg.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    # background "images/popup_bg.png"
    # padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style start_popup_prompt_text:
    text_align 0.5
    layout "subtitle"

style start_popup_button:
    properties gui.button_properties("start_popup_button")

style start_popup_button_text:
    properties gui.button_text_properties("start_popup_button")

screen gallery_popup():
    default replayListState = "Main"
    modal True

    zorder 200

    style_prefix "gallery_popup"

    add "gui/overlay/confirm.png"
    add "images/popup_bg.png" at Transform(size=(1200, 1500)):
        xalign 0.5
        yalign 0.5

    frame:
        background None

        label _("Gallery"):
            style "prompt_title"
            xalign 0.5
            ypos 300

        viewport:
            xalign .5
            xoffset 15
            ysize 100
            yoffset 400
            # yinitial yinitial
            scrollbars "horizontal"
            mousewheel True
            draggable True
            pagekeys True

            side_yfill True

            hbox:
                spacing 30

                textbutton _("Main") action SetScreenVariable("replayListState", "Main")

                textbutton _("Corws") action SetScreenVariable("replayListState", "Crows")

                textbutton _("Abyss") action SetScreenVariable("replayListState", "Abyss")

        viewport:
            xalign .5
            xoffset 15
            yoffset 520
            ysize 950

            scrollbars "vertical"
            yinitial 0
            mousewheel True
            draggable True
            pagekeys True

            side_yfill True

            if replayListState == "Main":
                vbox:
                    spacing 20
                    ysize 800

                    frame:
                        background None

                        xsize 750
                        ysize 300
                        xoffset 15
                        xalign .5
                        yalign 0

                        imagebutton:
                            xalign .5
                            yalign .5
                            ysize 300

                            if persistent.Prologue:
                                idle "prologue_cell"
                                hover "prologue_cell_hover"
                                action Replay("Prologue")
                            else:
                                idle "images/replayCell/Main/prologue_locked.jpg"
                                hover "images/replayCell/Main/prologue_locked.jpg"
                                pass

                        text ("Prologue"):
                            outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
                            yanchor 1.0
                            yalign 1.0
                            
            elif replayListState == "Crows":
                vbox:
                    spacing 20
                    ysize 800

            elif replayListState == "Abyss":
                vbox:
                    spacing 20
                    ysize 800

        textbutton _("Close") action Hide("gallery_popup"):
            xalign 0.5
            ypos 1500

style gallery_popup_frame is gui_frame:
    xsize 800
style gallery_popup_prompt is gui_prompt
style gallery_popup_prompt_text is gui_prompt_text:
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
style gallery_popup_button is gui_medium_button
style gallery_popup_button_text is gui_medium_button_text:
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    selected_color "#D68478"
    size 70

style gallery_popup_frame:
    # background Frame([ "images/popup_bg.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    # background "images/popup_bg.png"
    # padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style gallery_popup_prompt_text:
    text_align 0.5
    layout "subtitle"

style gallery_popup_button:
    properties gui.button_properties("replay_popup_button")

style gallery_popup_button_text:
    properties gui.button_text_properties("replay_popup_button")

image prologue_cell:
    "images/replayCell/Main/prologue_normal.jpg"

image prologue_cell_hover:
    "images/replayCell/Main/prologue_normal.jpg"
    matrixcolor BrightnessMatrix(-0.3)

screen ingame_popup():
    modal True

    zorder 200

    style_prefix "ingame_popup"

    add "gui/overlay/confirm.png"
    add "images/popup_bg.png" at Transform(size=(1200 * 0.8, 1500 * 0.6)):
        xalign 0.5
        yalign 0.5

    frame:
        background None
        xalign 0.5

        label _("Pause"):
            style "prompt_title"
            xalign 0.5
            yalign 0.1
            ypos 600

        text _("All game content is reset, and you start from scratch.\n\nAre you sure?"):
            outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
            xsize 600
            ypos 750
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150
            ypos 1250

            textbutton _("Sure") action [Hide("ingame_popup"), Hide("DefaultUI"), Play("music", "Wind_grass.mp3"),ShowMenu("main_menu")]

            textbutton _("Cancel") action Hide("ingame_popup")

style ingame_popup_frame is gui_frame:
    xsize 800
style ingame_popup_prompt is gui_prompt
style ingame_popup_prompt_text is gui_prompt_text:
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
    left_padding 20
    right_padding 20
style ingame_popup_button is gui_medium_button
style ingame_popup_button_text is gui_medium_button_text:
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    size 70

style ingame_popup_frame:
    # background Frame([ "images/popup_bg.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    # background "images/popup_bg.png"
    # padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style ingame_popup_prompt_text:
    text_align 0.5
    layout "subtitle"

style ingame_popup_button:
    properties gui.button_properties("ingame_popup_button")

style ingame_popup_button_text:
    properties gui.button_text_properties("ingame_popup_button")

screen beta_popup():
    modal True

    zorder 200

    style_prefix "beta_popup"

    add "gui/overlay/confirm.png"
    add "images/popup_bg.png" at Transform(size=(None, 1000)):
        xalign 0.5
        yalign 0.5

    frame:
        background None
        align (0.5, 0.5)

        vbox:
            xalign .5
            yalign .5
            ysize 800
            spacing 50

            label _("Thanks for playing"):
                style "prompt_title"
                xalign 0.5
                yalign 0.1

            vbox:
                box_wrap True
                xalign 0.5
                xsize 700

                text _("This game is still in development."):
                    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

                null height (0.5 * gui.pref_spacing)

                text _("There's still so much story to tell. Stay tuned."):
                    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

                null height (0.5 * gui.pref_spacing)

                text _("Let us know what you think of it so far and we'll be back with more great stories."):
                    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

                null height (0.5 * gui.pref_spacing)

                text _("Please fill out the survey via the button below."):
                    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

            hbox:
                xalign 0.5
                yalign 0.8

                xsize 800

                if preferences.language == "korean":
                    textbutton "설문하기" action OpenURL("https://forms.gle/EVPw37CqGe1RQtw78"):
                        xalign 0.5
                else:
                    textbutton "Survey" action OpenURL("https://forms.gle/pbxSu3v7zRLJwkuv7"):
                        xalign 0.5

                textbutton _("Cancel") action [Hide("beta_popup"), Play("music", "Wind_grass.mp3"),ShowMenu("main_menu")]:
                    xalign 0.5

style beta_popup_frame is gui_frame:
    xsize 800
style beta_popup_prompt is gui_prompt
style beta_popup_prompt_text is gui_prompt_text:
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
    left_padding 20
    right_padding 20
style beta_popup_button is gui_medium_button
style beta_popup_button_text is gui_medium_button_text:
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    size 50

style beta_popup_frame:
    # background Frame([ "images/popup_bg.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    # background "images/popup_bg.png"
    # padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style beta_popup_prompt_text:
    text_align 0.5
    layout "subtitle"

style beta_popup_button:
    properties gui.button_properties("beta_popup_button")

style beta_popup_button_text:
    properties gui.button_text_properties("beta_popup_button")

init python:
    def reset_data():
        ## deletes all persistent data use with caution
        for attr in dir(persistent):
            if not callable(attr) and not attr.startswith("_"):
                setattr(persistent, attr, None)

        ## deletes all save games use with caution!
        for slot in renpy.list_saved_games(fast=True):
            renpy.unlink_save(slot)
        ## a Ren'Py relaunch is nessesary
        # renpy.quit(relaunch=True)

image warning_btn:
        "images/icons/Warning.png"
        xysize(80, 80)
        
image warning_btn_hover:
        "images/icons/Warning.png"
        xysize(75, 75)
        matrixcolor BrightnessMatrix(-0.3)

screen preference_popup():
    modal True

    zorder 200

    style_prefix "preference_popup"

    add "gui/overlay/confirm.png"
    add "images/popup_bg.png" at Transform(size=(1200, 1500)):
        xalign 0.5
        yalign 0.5

    frame:
        background None

        label _("Options"):
            style "prompt_title"
            xalign 0.5
            ypos 300

        hbox:
            box_wrap True
            xalign .5
            ypos 500

            vbox:
                xsize 300
                style_prefix "check"
                label _("Language")

                null height (2 * gui.pref_spacing)

                textbutton "English" action Language(None): #default language of the VN your would be Chinese (simplified or tradtitional?)
                    if preferences.language == None:
                        left_padding 35
                        xoffset -10

                null height (0.5 * gui.pref_spacing)

                textbutton "한국어" action Language("korean"): #translation that you set in the Generate Translations (spanish as an example here)
                    if preferences.language == "korean":
                        left_padding 35
                        xoffset -10

            vbox:
                xsize 300
                style_prefix "check"
                label _("Reset")

                null height (2 * gui.pref_spacing)

                imagebutton:
                    xalign .5
                    idle "warning_btn"
                    hover "warning_btn_hover"
                    action Confirm(_("Are you sure to delete all persistent data?\nThis also deletes ALL saved games and cannot be undone."), Function(reset_data), Hide('Confirm'))

        hbox:
            box_wrap True
            xalign .5
            ypos 800

            vbox:
                style_prefix "check"

                label _("Volume")

                null height (2 * gui.pref_spacing)

                if config.has_music:
                    text _("Music"):
                        xalign .5
                        outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

                    null height (0.3 * gui.pref_spacing)

                    hbox:
                        bar value Preference("music volume")

                null height (1 * gui.pref_spacing)

                if config.has_sound:

                    text _("Sound"):
                        xalign .5
                        outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

                    null height (0.3 * gui.pref_spacing)

                    hbox:
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)

                null height (1 * gui.pref_spacing)

                if config.has_voice:
                    text _("Voice"):
                        xalign .5
                        outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

                    null height (0.3 * gui.pref_spacing)

                    hbox:
                        bar value Preference("voice volume")

                        if config.sample_voice:
                            textbutton _("Test") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing

                    textbutton _("Mute All"):
                        action Preference("all mute", "toggle")
                        xalign 0.5

                        if preferences.get_mute("main"):
                            left_padding 35
                            xoffset -10

        textbutton _("Close") action Hide("preference_popup"):
            xalign 0.5
            ypos 1500

style preference_popup_frame is gui_frame:
    xsize 800
style preference_popup_prompt is gui_prompt
style preference_popup_prompt_text is gui_prompt_text:
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
    text_align 0.5
    layout "subtitle"
    left_padding 20
    right_padding 20

style preference_popup_button is gui_medium_button
style preference_popup_button_text is gui_medium_button_text:
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    size 70

style preference_popup_frame:
    xalign .5
    yalign .5

style preference_popup_button:
    properties gui.button_properties("preference_popup_button")

style preference_popup_button_text:
    properties gui.button_text_properties("preference_popup_button")

style sound_slider_label is pref_label:
    xalign 0.5
style sound_slider_label_text is pref_label_text
style sound_slider_slider is gui_slider
style sound_slider_button is gui_button
style sound_slider_button_text is gui_button_text

style sound_slider_slider:
    xsize 700

style sound_slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 9

style sound_slider_button_text:
    properties gui.button_text_properties("slider_button")

style sound_slider_vbox:
    xsize None
    
screen about_popup():
    modal True

    zorder 200

    style_prefix "about_popup"

    add "gui/overlay/confirm.png"
    add "images/popup_bg.png" at Transform(size=(1200, 1500)):
        xalign 0.5
        yalign 0.5

    frame:
        background None

        label _("About"):
            style "prompt_title"
            xalign 0.5
            ypos 300

        viewport:
            xalign .5
            xoffset 15
            ysize 1000
            ypos 500
            # yinitial yinitial
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True

            side_yfill True

            vbox:
                text _("Made by team {a=https://coffeeburgercode.page}CBC{/a}\n") xalign 0.5:
                    size 40
                    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

                label "[config.name]" xalign 0.5

                text _("Version [config.version!t]\n") xalign 0.5:
                    size 40
                    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license]") xalign 0.5:
                    size 40
                    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

                null height (4 * gui.pref_spacing)

                ## gui.about is usually set in options.rpy.
                if gui.about:
                    text _("[gui.about!t]\n")

                # text _("Thanks to aaa, bbb, ccc, ddd, eee, fff, ggg, hhh, iii, jjj ")

                # null height (4 * gui.pref_spacing)

        textbutton _("Close") action Hide("about_popup"):
            xalign 0.5
            ypos 1500

style about_popup_frame is gui_frame:
    xsize 800
style about_popup_prompt is gui_prompt
style about_popup_prompt_text is gui_prompt_text:
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
style about_popup_button is gui_medium_button
style about_popup_button_text is gui_medium_button_text:
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    size 70

style about_popup_frame:
    # background Frame([ "gui/overlay/confirm.png" ], gui.confirm_frame_borders, tile=gui.frame_tile)
    # background "images/popup_bg.png"
    # padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style about_popup_prompt_text:
    text_align 0.5
    layout "subtitle"
    left_padding 40
    right_padding 40

style about_popup_button:
    properties gui.button_properties("about_popup_button")

style about_popup_button_text:
    properties gui.button_text_properties("about_popup_button")

screen navigation():
    if renpy.get_screen("main_menu"):
        add "images/logo.png":
            xalign 0.5
            yanchor 0.5
            yalign 0.2
            zoom 1.3

        null height (30 * gui.pref_spacing)

        vbox:
            style_prefix "navigation"

            xalign 0.5
            yalign 0.6

            spacing gui.navigation_spacing

            textbutton _("Start") action Show("start_popup")

            textbutton _("Tutorial") #action Replay("Prologue")

            textbutton _("Gallery") action Show("gallery_popup")

        frame:
            xysize (1080, 1920)
            background None

            hbox:
                xanchor 0.0
                yanchor 1.0
                yalign 1.0
                xalign 0.0

                xpos 50
                ypos 1920-50

                spacing 20

                imagebutton:
                    xalign .5
                    idle "settings_btn"
                    hover "settings_btn_hover"
                    action Show("preference_popup")

                imagebutton:
                    xalign .5
                    idle "about_btn"
                    hover "about_btn_hover"
                    action Show("about_popup")

    ########################################################################
    else:
        vbox:
            style_prefix "navigation"

            xalign 0.5
            yalign 0.7

            spacing gui.navigation_spacing

style navigation_button is gui_button
style navigation_button_text is gui_button_text:
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
    yalign 0.5

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5
    size 85

image settings_btn:
    "images/icons/Settings_icon.png"
    xysize(120, 120)

image settings_btn_hover:
        "images/icons/Settings_icon.png"
        xysize(120, 120)
        matrixcolor BrightnessMatrix(-0.3)

image about_btn:
    "images/icons/About_icon.png"
    xysize(120, 120)

image about_btn_hover:
        "images/icons/About_icon.png"
        xysize(120, 120)
        matrixcolor BrightnessMatrix(-0.3)


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background:
        xalign 0.5 #add these two lines
        yalign 0.5

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 237
    yfill True

# background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    # xoffset -16
    xmaximum 675
    yalign 1.0
    # yoffset -16

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background:
            xalign 0.5 #add these two lines
            yalign 0.5
    else:
        add gui.game_menu_background:
            xalign 0.5 #add these two lines
            yalign 0.5

    frame:
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    textbutton _("MainMenu"):
        style "menu_button"

        action [ShowMenu("main_menu")]

    label title

    if main_menu:
        key "game_menu" action MainMenu(confirm=False)()


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style menu_button is navigation_button
style menu_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 26
    top_padding 102

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 287
    yfill True

style game_menu_content_frame:
    xalign 0.5
    yalign 1.0
    top_margin 50

style game_menu_viewport:
    xsize None

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 9

style game_menu_label:
    xalign 0.5
    ysize 102
    ypos 20

style game_menu_label_text:
    size 60
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -25

style menu_button:
    xpos gui.navigation_negative_xpos
    xanchor 1.0
    yalign 1.0
    yoffset -25

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid 1 4:
                style_prefix "slot"

                xalign 0.5
                yalign 0.2

                spacing gui.slot_spacing

                for i in range(1 * 4):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        # add FileScreenshot(slot) xalign 1

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                        

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 0.0
                yoffset 70

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 5):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text:
    xoffset 100
    yoffset 75
style slot_name_text is slot_button_text:
    xoffset 100

style page_label:
    xpadding 43
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Options"), scroll="viewport"):
        frame:
            xsize 1080
            padding (100, 100)
            background "#4f5a6600"

            vbox:
                align(0.5, 0.5)

                hbox:
                    box_wrap True
                    xsize 700

                    vbox:
                        style_prefix "check"
                        label _("Skip")
                        null height (2 * gui.pref_spacing)
                        # textbutton _("Enable Skip") action ToggleVariable("custom_skip_enabled")

                        # textbutton _("Unseen Text") action Skip() alternate Skip(fast=True, confirm=True)
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                null height (4 * gui.pref_spacing)

                hbox:
                    box_wrap True
                    xsize 700

                    vbox:
                        style_prefix "check"
                        label _("Language")
                        null height (2 * gui.pref_spacing)
                        textbutton "English" action Language(None) #default language of the VN your would be Chinese (simplified or tradtitional?)
                        textbutton "한국어" action Language("korean") #translation that you set in the Generate Translations (spanish as an example here)

                        ## Additional vboxes of type "radio_pref" or "check_pref" can be
                        ## added here, to add additional creator-defined preferences.

                null height (4 * gui.pref_spacing)


style pref_label is gui_label:
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
    xalign 0.5
style pref_label_text is gui_label_text:
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]    
style pref_button is gui_button:
    xalign 0.5
style pref_button_text is gui_button_text:
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label:
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
    xalign 0.5
style check_button is gui_button:
    outlines [ (absolute(4), "#000", absolute(0), absolute(0)) ]
    xalign 0.5
style check_button_text is gui_button_text:
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    size 40
style check_vbox is pref_vbox

style slider_label is pref_label:
    xalign 0.5
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text

style mute_all_button is check_button:
    xalign 0.5
    xoffset -10
style mute_all_button_text is check_button_text


style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 500


style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 700

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 9

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize None


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

# screen mobile_overlay():
#     button:
#         action Preference("auto-forward", "toggle")

# init python:
#     if renpy.variant(["touch", "android", "ios"]):
#         config.overlay_screens.append("mobile_overlay")

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 13

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 7

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 211
    right_padding 17

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    # add "gui/overlay/confirm.png"
    # add "images/popup_bg.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 26

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 85

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/overlay/confirm.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:
        yalign 1.0
        yanchor 0
        ypos 250

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0
                
                

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/phone/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



















