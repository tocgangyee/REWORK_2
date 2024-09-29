init python:
    def potion_effect(data):
        percent_table = ["Trenta size", "Half Gallon"]

        if data['suffix'] in percent_table:
            value = f"{math.trunc(data['effect'] * 100)}%"
        else:
            value = data['effect']

        return value
    
screen DefaultUI:
    frame:
        xsize 1080
        ysize 1920
        background None
        
        $ UI_str = playerData['str'] + playerData['inven']['weapon'][0]['str'] + playerData['inven']['armor'][0]['str']
        $ UI_dmg = playerData['dmg'] + playerData['inven']['weapon'][0]['dmg'] + playerData['inven']['armor'][0]['dmg']
        $ UI_dex = playerData['dex'] + playerData['inven']['weapon'][0]['dex'] + playerData['inven']['armor'][0]['dex']
        $ UI_lck = playerData['lck'] + playerData['inven']['weapon'][0]['lck'] + playerData['inven']['armor'][0]['lck']

        vbox:
            xalign 0.5
            frame:
                xsize 1080
                ysize 210
                background Colors.Black_dimming.value

                #Status bar
                vbox:
                    xalign 0.5
                    hbox:
                        xsize 1060
                        ysize 70
                        xalign 0.5

                        hbox:
                            spacing 10
                            yalign 0.5

                            add "images/icons/Heart.svg" size (50, 50)
                            text("[playerData[current_hp]]/[playerData[max_hp]]") size 45:
                                if playerData["current_hp"] <= playerData["max_hp"] * 0.25:
                                    color Colors.Red_crimson.value
                            text("([playerData[inven][armor][0][current_durability]])") size 45:
                                if playerData["inven"]["armor"][0]["current_durability"] == 0:
                                    color Colors.Gray_light.value
                                else:
                                    color Colors.Blue_icy.value

                            add "images/icons/Strength.svg" size (50, 50)
                            # text("[playerData[str] + playerData[inven][weapon][0][str] + playerData[inven][armor][0][str]]") size 45
                            text("[UI_str]") size 45


                            add "images/icons/Punch.svg" size (50, 50)
                            text("[UI_dmg]") size 45

                            add "images/icons/Wingfoot.svg" size (50, 50)
                            text("[UI_dex]") size 45

                            add "images/icons/Clover.svg" size (50, 50)
                            text("[UI_lck]") size 45

                        text("[gameVariable[stage]] F"):
                            size 45
                            xalign 1.0
                            yalign 0.5

                    hbox:   
                        xsize 1060
                        ysize 70
                        xalign 0.5

                        hbox:
                            spacing 10

                            add "images/icons/Inven.svg" size (50, 50)
                            if len(playerData["inven"]["weapon"]) == 0:
                                text(_("Empty")) size 45
                            else:
                                text("[playerData[inven][weapon][0][name]!t]") size 45:
                                    if playerData["inven"]["weapon"][0]["color"] == ColorState.White.value:
                                        color Colors.White.value
                                    elif playerData["inven"]["weapon"][0]["color"] == ColorState.Blue.value:
                                        color Colors.Blue.value
                                    elif playerData["inven"]["weapon"][0]["color"] == ColorState.Purple.value:
                                        color Colors.Purple.value

                                text("([playerData[inven][weapon][0][current_durability]])") size 45:
                                    if playerData["inven"]["weapon"][0]["current_durability"] == 0:
                                        color Colors.Gray_light.value
                                # else:
                                #     color "#add8e6"

                            text("|") size 50

                            if len(playerData["inven"]["armor"]) == 0:
                                text("Empty") size 45
                            else:
                                text("[playerData[inven][armor][0][name]!t]") size 45:
                                    if playerData["inven"]["armor"][0]["color"] == ColorState.White.value:
                                        color Colors.White.value
                                    elif playerData["inven"]["armor"][0]["color"] == ColorState.Blue.value:
                                        color Colors.Blue.value
                                    elif playerData["inven"]["armor"][0]["color"] == ColorState.Purple.value:
                                        color Colors.Purple.value

                        text("Exp [playerData[current_exp]]/[playerData[max_exp]]") size 45 xalign 1.0
                    
                    hbox:
                        xsize 1060
                        ysize 70
                        xalign 0.5

                        hbox:
                            xalign 1.0
                            spacing 10

                            if playerData['condition']['Poisoned'] > 0:
                                add "images/icons/Poison_active.svg" size (50, 50)
                            else:
                                add "images/icons/Poison.svg" size (50, 50)
                            
                            if playerData['condition']['Wounded'] > 0:
                                add "images/icons/Wound_active.svg" size (50, 50)
                            else:
                                add "images/icons/Wound.svg" size (50, 50)

                            if playerData['condition']['Rusted'] > 0:
                                add "images/icons/Rust_active.svg" size (50, 50)
                            else:
                                add "images/icons/Rust.svg" size (50, 50)

            frame:
                xsize 1080
                ysize 30
                background Colors.White.value
                bar :
                    # style "bar"
                    left_bar Colors.Yellow_saffron.value #Saffron
                    right_bar Colors.Gray_light.value #light gray
                    value playerData['skillPoint']
                    range 7

            frame:
                xsize 1080
                ysize 250
                background Colors.Black_dimming.value

                # banner image selection
                if gameVariable["bannerState"] == BannerState.Door:
                    add "images/banners/door.png" align (0.5, 0.5) size (190, 190)
                elif gameVariable["bannerState"] == BannerState.Battle:
                    add "images/banners/battle.png" align (0.5, 0.5) size (190, 190)
                elif gameVariable["bannerState"] == BannerState.Chest:
                    add "images/banners/chest.png" align (0.5, 0.5) size (190, 190)
                elif gameVariable["bannerState"] == BannerState.Chest_empty:
                    add "images/banners/chest_empty.png" align (0.5, 0.5) size (190, 190)
                elif gameVariable["bannerState"] == BannerState.Chest_full:
                    add "images/banners/chest_full.png" align (0.5, 0.5) size (190, 190)
                elif gameVariable["bannerState"] == BannerState.Grace:
                    add "images/banners/grace.png" align (0.5, 0.5) size (190, 190)
                elif gameVariable["bannerState"] == BannerState.Maintenance:
                    add "images/banners/maintenance.png" align (0.5, 0.5) size (190, 190)
                elif gameVariable["bannerState"] == BannerState.Mimic:
                    add "images/banners/mimic.png" align (0.5, 0.5) size (190, 190)
                elif gameVariable["bannerState"] == BannerState.Dead_normal:
                    add "images/banners/dead_normal.png" align (0.5, 0.5) size (190, 190)
                elif gameVariable["bannerState"] == BannerState.Dead_berserk:
                    add "images/banners/dead_berserk.png" align (0.5, 0.5) size (190, 190)
                elif gameVariable["bannerState"] == BannerState.Dead_wound:
                    add "images/banners/dead_wound.png" align (0.5, 0.5) size (190, 190)
                elif gameVariable["bannerState"] == BannerState.Huginn:
                    add "images/banners/huginn.png" align (0.5, 0.5) size (1080, None)
                elif gameVariable["bannerState"] == BannerState.Muninn:
                    add "images/banners/muninn.png" align (0.5, 0.5) size (1080, None)

            # draw eventview on battle
            # use games monsters list
            # TODO: dimming when monster already dead
            if gameVariable["gameState"] == GameState.Battle:
                frame:
                    xsize 1080
                    ysize 500
                    background None

                    hbox:
                        align (0.5, 0.5)
                        spacing 45

                        for idx, mon_data in enumerate(monsters):
                            frame:
                                xsize 300
                                ysize 450
                                background None

                                if idx in transitionVariable["target_battle"]:
                                    at shake
                                    # $ transitionVariable["target_battle"] = []

                                if mon_data["color"] == 'White':
                                    add "images/bezel/bezel_white.png" xalign 0.5
                                elif mon_data["color"] == "Blue":
                                    add "images/bezel/bezel_blue.png" xalign 0.5
                                elif mon_data["color"] == "Purple":
                                    add "images/bezel/bezel_purple.png" xalign 0.5
                                
                                vbox:
                                    align (0.5, 0.5)
                                    spacing 10

                                    text "[mon_data[name]!t]" align (0.5, 0.5) size 50:
                                        if gameVariable["stage"] >= 70:
                                            outlines [ (absolute(4), Colors.Red_crimson.value, absolute(0), absolute(0)) ]
                                    text "[mon_data[prefix]!t]" align (0.5, 0.5) size 30
                                    text "[mon_data[suffix]!t]" align (0.5, 0.5) size 30

                                    null align (0.5, 0.5) height (90)

                                    hbox:
                                        align (0.5, 0.5)
                                        spacing 10
                                        add "images/icons/Heart.svg" size (40, 40)
                                        text "[mon_data[current_hp]]" size 40:
                                            if mon_data["current_hp"] <= mon_data["max_hp"] * 0.25:
                                                color Colors.Red_crimson.value

                                    hbox:
                                        align (0.5, 0.5)
                                        spacing 10
                                        $ temp = cal_damage_mon(mon_data["str"], mon_data["dmg"])
                                        add "images/icons/Claw.svg" size (40, 40)
                                        text "[temp]" size 40
                                
                                if mon_data["current_hp"] <= 0:
                                    frame:
                                        xsize 300
                                        ysize 450
                                        xalign 0.5
                                        background Colors.Black_dimming_bold.value

            elif gameVariable["gameState"] == GameState.Looting:
                $ UI_potion_effect = potion_effect(box[1])
                frame:
                    xsize 1080
                    ysize 500
                    background None

                    hbox:
                        align (0.5, 0.5)
                        spacing 45

                        for idx, box_data in enumerate(box):
                            frame:
                                xsize 300
                                ysize 450
                                background None

                                if box_data["color"] == ColorState.White.value:
                                    add "images/bezel/bezel_white.png" xalign 0.5
                                elif box_data["color"] == ColorState.Blue.value:
                                    add "images/bezel/bezel_blue.png" xalign 0.5
                                elif box_data["color"] == ColorState.Purple.value:
                                    add "images/bezel/bezel_purple.png" xalign 0.5

                                vbox:
                                    align (0.5, 0.5)
                                    spacing 10

                                    text "[box_data[name]!t]" align (0.5, 0.5) size 40
                                    # text "[box_data[prefix]]" align (0.5, 0.5) size 30
                                    text "[box_data[suffix]!t]" align (0.5, 0.5) size 30

                                    null align (0.5, 0.5) height (90)

                                    if idx == 0:
                                        hbox:
                                            align (0.5, 0.5)
                                            spacing 10
                                            add "images/icons/Strength.svg" size (40, 40)
                                            text "[box_data[str]]" size 40

                                            add "images/icons/Punch.svg" size (40, 40)
                                            text "[box_data[dmg]]" size 40

                                        hbox:
                                            align (0.5, 0.5)
                                            spacing 10
                                            add "images/icons/Wingfoot.svg" size (40, 40)
                                            text "[box_data[dex]]" size 40

                                            add "images/icons/Clover.svg" size (40, 40)
                                            text "[box_data[lck]]" size 40

                                        if box_data["category"] == EquipmentCategory.Armor.value:
                                            hbox:
                                                align (0.5, 0.5)
                                                spacing 10
                                                add "images/icons/Shield.svg" size (40, 40)
                                                text "[box_data[current_durability]]" size 40
                                    elif idx == 1:
                                        hbox:
                                            align (0.5, 0.5)
                                            spacing 10
                                            add "images/icons/Heart.svg" size (40, 40)
                                            text "[UI_potion_effect]" size 40

            elif gameVariable["gameState"] == GameState.Swap:
                frame:
                    xsize 1080
                    ysize 500
                    background None

                    hbox:
                        align (0.5, 0.5)
                        spacing 45

                        for idx, box_data in enumerate(swapTarget):
                            frame:
                                xsize 300
                                ysize 450
                                background None

                                if box_data["color"] == ColorState.White.value:
                                    add "images/bezel/bezel_white.png" xalign 0.5
                                elif box_data["color"] == ColorState.Blue.value:
                                    add "images/bezel/bezel_blue.png" xalign 0.5
                                elif box_data["color"] == ColorState.Purple.value:
                                    add "images/bezel/bezel_purple.png" xalign 0.5

                                vbox:
                                    align (0.5, 0.5)
                                    spacing 10

                                    text "[box_data[name]!t]" align (0.5, 0.5) size 40
                                    # text "[box_data[prefix]]" align (0.5, 0.5) size 30
                                    text "[box_data[suffix]!t]" align (0.5, 0.5) size 30

                                    null align (0.5, 0.5) height (90)

                                    hbox:
                                        align (0.5, 0.5)
                                        spacing 10
                                        add "images/icons/Strength.svg" size (40, 40)
                                        text "[box_data[str]]" size 40

                                        add "images/icons/Punch.svg" size (40, 40)
                                        text "[box_data[dmg]]" size 40

                                    hbox:
                                        align (0.5, 0.5)
                                        spacing 10
                                        add "images/icons/Wingfoot.svg" size (40, 40)
                                        text "[box_data[dex]]" size 40

                                        add "images/icons/Clover.svg" size (40, 40)
                                        text "[box_data[lck]]" size 40

                                    if box_data["category"] == EquipmentCategory.Armor.value:
                                        hbox:
                                            align (0.5, 0.5)
                                            spacing 10
                                            add "images/icons/Shield.svg" size (40, 40)
                                            text "[box_data[current_durability]]" size 40