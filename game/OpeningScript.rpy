# game opening scene.
label Opening_ifDead:
    "It seemed they had a restless dream last night, perhaps due to the commotion."
    "The cool air seeped through their clothes, and they shivered slightly, still not accustomed to it."

    # 꼬르륵 소리

    play sound "audio/Door.mp3" fadeout 0.3 volume 1.0

    "You tried to shake the door to soothe your noisy hunger, but it didn't budge."
    "A cold sweat ran down your spine, and you fixed your gaze on the familiar staircase."
    "You knew you had to move forward."

    return

label Opening:
    "You opened the door of the tower and then cautiously stepped inside."
    "The warm sunshine you'd felt just a few moments before, the breeze that was pleasantly cool, if a little unseasonably so, contrasted with a chill, a faint musty odor."
    "You heard the door close quietly between the creaking of gear and the faint echo of your footsteps."

    # renpy.music.play("audio/Door.mp3", channel="sound", fadeout=0.3, relative_volume=1.0)
    play sound "audio/Door.mp3" fadeout 0.3 volume 1.0

    "You turned the handle, but the door wouldn't open. Now you have no choice but to move forward."

    return