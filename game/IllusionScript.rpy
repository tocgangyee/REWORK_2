label Illusion:
    "You dragged your wounded body to the door leading to the next level."
    "Clinging to your fading consciousness, your blurry vision caught a glimpse of a monster suddenly charging at you."

    #(Blackout)
    hide screen DefaultUI
    show black with dissolve
    
    "Thinking it was too late, you tightly closed your eyes, but felt nothing."

    $ gameVariable["gameState"] = GameState.Normal
    $ gameVariable["bannerState"] = BannerState.Door

    # (Vision Restored)
    show screen DefaultUI
    if gameVariable["stage"] < 30:
        show normal with dissolve
    elif 30 <= gameVariable["stage"] < 70:
        show midlevel with dissolve
    elif 70 <= gameVariable["stage"]:
        show abyss with dissolve

    "When you opened your eyes again, you realized that only a serene silence surrounded you."
    "This floor was safe. You were able to take a much-needed rest."

    "hp recovered 25%%"

    $ playerData['current_hp'] += int(playerData['max_hp'] * 0.25)

    $ battleFlag = False
    $ gameVariable["gameState"] = GameState.Normal
    $ gameVariable["bannerState"] = BannerState.Door

    return