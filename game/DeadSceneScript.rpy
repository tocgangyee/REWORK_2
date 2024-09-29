label DeadScene:
    if persistent.DeadCount == None:
        $ persistent.DeadCount = 0
    else:
        $ persistent.DeadCount += 1

    if gameVariable["type_of_death"] == "W":
        # $ temp = dead_W_script()
        $ gameVariable["bannerState"] = BannerState.Dead_wound
        $ gameVariable["gameState"] = GameState.Normal
        jump DeadScene_Wound
    elif gameVariable["type_of_death"] == "B":
        # $ temp = dead_B_script()
        $ gameVariable["bannerState"] = BannerState.Dead_berserk
        $ gameVariable["gameState"] = GameState.Normal
        jump DeadScene_Berserk
    elif gameVariable["type_of_death"] == "N":
        # $ temp = dead_N_script()
        $ gameVariable["bannerState"] = BannerState.Dead_normal
        $ gameVariable["gameState"] = GameState.Normal
        jump DeadScene_Normal


label DeadScene_Wound:
    # blurly
    hide screen DefaultUI
    show black with dissolve

    "You thought it was a small cut, but it wouldn't stop bleeding."
    "Steps became heavier, and a chill ran down my spine.\nGrip on the wall slipped and I rolled on the floor."

    # vpunch
    show black with dissolve

    "Tried to get up, but the weight of body made it difficult."
    "Soon, completely exhausted, You lay face towards the ceiling.\nBreathing became a little easier."

    "You have no strength left to move your fingertips.\nYour end came so coldly, step by step."

    menu:
        'Go to Main Menu':
            if not persistent.FirstDead:
                $ persistent.FirstDead = True

            $ MainMenu(confirm=False)()
        "Go to Servey" if persistent.DeadCount >= 10:
            if preferences.language == "korean":
                $ renpy.run(OpenURL("https://forms.gle/EVPw37CqGe1RQtw78"))
            else:
                $ renpy.run(OpenURL("https://forms.gle/pbxSu3v7zRLJwkuv7"))
    
    return

label DeadScene_Berserk:
    # dissolve 30
    hide screen DefaultUI
    show black with dissolve

    "With great power comes great responsibility.\nWhen woke up, You was in a corner of a tower somewhere."
    "Wearing a fine looking suit of armor, and after the next few battles, You don't remember much more."

    # dissolve 60
    show black with dissolve

    "Some parts were gone, some were broken, and not a single piece of your armor or body was intact."
    "There is nothing wrong with choosing power, that's for sure."

    # blackout
    show black with dissolve

    "It was a choice that would have helped you if you hadn't fallen for it so early.\nWith that hindsight regret, your eyes became lifeless."

    # vision restored
    show screen DefaultUI
    # if gameVariable["stage"] < 30:
    #     show bg normal with dissolve
    # elif 30 <= gameVariable["stage"] < 70:
    #     show bg midlevel with dissolve
    # elif 70 <= gameVariable["stage"]:
    #     show bg abyss with dissolve

    menu:
        'Go to Main Menu':
            if not persistent.FirstDead:
                $ persistent.FirstDead = True

            $ MainMenu(confirm=False)()
        "Go to Servey" if persistent.DeadCount >= 10:
            if preferences.language == "korean":
                $ renpy.run(OpenURL("https://forms.gle/EVPw37CqGe1RQtw78"))
            else:
                $ renpy.run(OpenURL("https://forms.gle/pbxSu3v7zRLJwkuv7"))
    
    return

label DeadScene_Normal:
    "You feel weak all over my body."
    "You can't tell if the air coming out of my stomach is hot or cold, and my vision is shaking uncontrollably."
    "You can't distinguish whether the sound is fading away or echoing."

    # black out
    hide screen DefaultUI
    show black with dissolve

    "Struggling, You raised own head for a moment and saw the ceiling before slowly collapsing, catching a glimpse of my own back."

    # vision restored
    show screen DefaultUI
    # if gameVariable["stage"] < 30:
    #     show bg normal with dissolve
    # elif 30 <= gameVariable["stage"] < 70:
    #     show bg midlevel with dissolve
    # elif 70 <= gameVariable["stage"]:
    #     show bg abyss with dissolve

    menu:
        'Go to Main Menu':
            if not persistent.FirstDead:
                $ persistent.FirstDead = True

            $ MainMenu(confirm=False)()
        "Go to Servey" if persistent.DeadCount >= 10:
            if preferences.language == "korean":
                $ renpy.run(OpenURL("https://forms.gle/EVPw37CqGe1RQtw78"))
            else:
                $ renpy.run(OpenURL("https://forms.gle/pbxSu3v7zRLJwkuv7"))
    
    return