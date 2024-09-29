init python:
    import math

    def keep_menu_gen(item):
        if preferences.language == "korean":
            return _(f"지금의 {add_postposition2(renpy.translate_string(item))} 유지한다.")
        else:
            return _(f"Keep current {item}")
    
    def change_menu_gen(item):
        if preferences.language == "korean":
            return _(f"새 {add_postposition2(renpy.translate_string(item))} 선택한다.")
        else:
            return _(f"Choose new {item}.")

    # Module: pick equipment with Monster.json via algorithm
    def load_equipment(weight):
        # data = equipments
        data = copy.deepcopy(equipments)

        result = []

        tier = list(data.keys())
        tier = random.choices(tier, weights=weight)[0]
        result.append(random.choice(data[tier]))

        return result[0]

    # Module: pick potion with Monster.json via algorithm
    def load_potion(weight):
        data = potions

        tier = list(data.keys())
        tier = random.choices(tier, weights=weight)[0]
        rarity = []

        for val in data[tier]:
            rarity.append(val['rare'])

        result = random.choices(data[tier], weights=rarity)[0]

        return result

    def maintenance():
        result = ""
        heal_flag = True
        repair_data = []
        returnObject = {}
        
        for category in playerData['inven']:
            for val in playerData['inven'][category]:
                if val['current_durability'] <= val['max_durability']:
                    if category == 'weapon':
                        if val['current_durability'] + gameVariable['weapon_repair_amount'] >= val['max_durability']:
                            temp = val['max_durability'] - val['current_durability']
                            val['current_durability'] = val['max_durability']
                            repair_data.append([val, temp])
                        else:
                            val['current_durability'] += gameVariable['weapon_repair_amount']
                            repair_data.append([val, gameVariable['weapon_repair_amount']])
                    elif category == 'armor':
                        if val['current_durability'] != 0:
                            heal_flag = False

                            if val['current_durability'] + gameVariable['armor_repair_amount'] > val['max_durability']:
                                # enhance
                                val['current_durability'] = val['current_durability'] + gameVariable['armor_repair_amount']
                                temp = ("enhancement", gameVariable['armor_repair_amount'])
                                repair_data.append([val, temp])
                                # TODO: enhancement narration
                            else:
                                # repair
                                val['current_durability'] += gameVariable['armor_repair_amount']
                                temp = ("repair", gameVariable['armor_repair_amount'])
                                repair_data.append([val, temp])

        returnObject["repair_data"] = repair_data
        # result += story_maintenance_repair(repair_data)

        if heal_flag:
            if playerData['current_hp'] + 5 >= playerData['max_hp']:
                playerData['current_hp'] = playerData['max_hp']
                returnObject["recover_data"] = 0
                # result += story_hp_full()
            else:
                playerData['current_hp'] += 5
                returnObject["recover_data"] = 5
                # result += story_maintenance_recover(5)

        return returnObject

    def Deldebuff(status, heal_data):
        WoundedHeal = False
        PoisonedHeal = False

        if playerData["condition"]["Wounded"] > 0 or playerData["condition"]["Poisoned"] > 0:
            target_arr = []

            if gameVariable["stage"] >= 70:
                for idx, value in enumerate(playerData["condition"].values()):
                    if value > 0:
                        target_arr.append(idx)

                if target_arr:
                    target = random.choice(target_arr)
                    if target == 0:
                        playerData["condition"]["Poisoned"] = 0
                        PoisonedHeal = True
                    elif target == 1:
                        playerData["condition"]["Wounded"] = 0
                        WoundedHeal = True
                    elif target == 2:
                        playerData["condition"]["Rusted"] = 0
                        RustedHeal = True
            else:
                if playerData["condition"]["Wounded"] > 0:
                    WoundedHeal = random.choices([True, False], weights=[10, 90])[0]
                if playerData["condition"]["Poisoned"] > 0:
                    PoisonedHeal = random.choices([True, False], weights=[10, 90])[0]

                if WoundedHeal:
                    playerData["condition"]["Wounded"] = 0
                if PoisonedHeal:
                    playerData["condition"]["Poisoned"] = 0

            if status == HealState.Max:
                # if WoundedHeal == True and PoisonedHeal == True:
                #     temp = story_hp_full_wound_heal(0)
                # elif WoundedHeal == True and PoisonedHeal == False:
                #     temp = story_hp_full_wound_heal(1)
                # elif WoundedHeal == False and PoisonedHeal == True:
                #     temp = story_hp_full_wound_heal(2)
                # else:
                #     temp = story_hp_full_wound_heal(3)
                renpy.call("event_HpFullDebuffRemove", WoundedHeal, PoisonedHeal)
            else:
                # if WoundedHeal == True and PoisonedHeal == True:
                #     temp = story_hp_healed_wound_heal(0, heal_data)
                # elif WoundedHeal == True and PoisonedHeal == False:
                #     temp = story_hp_healed_wound_heal(1, heal_data)
                # elif WoundedHeal == False and PoisonedHeal == True:
                #     temp = story_hp_healed_wound_heal(2, heal_data)
                # else:
                #     temp = story_hp_healed_wound_heal(3, heal_data)
                renpy.call("event_HpHealDebuffRemove", WoundedHeal, PoisonedHeal, heal_data)
                # call event_HpHealDebuffRemove(WoundedHeal, PoisonedHeal, heal_data)
        else:
            if status == HealState.Max:
                # temp = story_hp_full()
                renpy.call("event_HpFull")
            else:
                renpy.call("event_HpHeal", heal_data)
                # temp = story_hp_healed(heal_data)

        # return temp


label Chest:
    $ gameVariable["bannerState"] = BannerState.Chest

    show screen DefaultUI(playerData)

    # $ lootingInitDialog = chest_appeared()
    call event_ChestAppeared
    # $ renpy.say(None, lootingInitDialog)
    # "[lootingInitDialog]"

    menu:
        'Open it.':
            $ lootingState = random.choices(['Win', 'Mimic', 'Lose'], weights = [50, 25, 25])[0]

            if lootingState == "Win":
                play sound "<from 0.5 to 2>Door-Cabinet-2.mp3" fadeout 0.3
                $ box = [load_equipment(eWeight), load_potion(pWeight)]
                $ gameVariable["bannerState"] = BannerState.Chest_full
                $ gameVariable["gameState"] = GameState.Looting
                $ inventory = playerData["inven"]
                
                menu:
                    'Choose Equipment.':
                        play sound "Latch-2.mp3" fadeout 0.3

                        if box[0]["category"] == EquipmentCategory.Armor.value:
                            if not inventory["armor"]:
                                python:
                                    playerData["inven"]["armor"].append(box[0])
                                    playerData["inven"]["armor"][0]["current_durability"] = box[0]["max_durability"]

                                call event_Pick(box[0])
                                # $ temp = story_picked(box[0])
                                # $ renpy.say(None, "[temp]")
                            else:
                                $ gameVariable["gameState"] = GameState.Swap
                                if box[0]["category"] == 'Armor':
                                    $ swapTarget = [playerData["inven"]["armor"][0], box[0]]
                                else:
                                    $ swapTarget = [playerData["inven"]["weapon"][0], box[0]]

                                $ keep_menu = keep_menu_gen(swapTarget[0]["name"])
                                $ change_menu = change_menu_gen(swapTarget[1]["name"])

                                menu:
                                    '[keep_menu]':
                                        $ gameVariable["gameState"] = GameState.Normal
                                        $ gameVariable["bannerState"] = BannerState.Door
                                    '[change_menu]':
                                        $ gameVariable["gameState"] = GameState.Normal
                                        $ gameVariable["bannerState"] = BannerState.Door

                                        if swapTarget[1]["category"] == EquipmentCategory.Armor.value:
                                            python:
                                                playerData["inven"]["armor"] = []

                                                playerData["inven"]["armor"].append(swapTarget[1])

                                            call event_PickAndSwap(swapTarget)
                                            # $ temp = story_pick_swap(swapTarget)
                                            # $ renpy.say(None, "[temp]")
                                        else:
                                            python:
                                                playerData["inven"]["weapon"] = []
                                                playerData["inven"]["weapon"].append(swapTarget[1])
                                                playerData["inven"]["weapon"][0]["current_durability"] = swapTarget[1]['current_durability']
                                                playerData["skillPoint"] = 0

                                            call event_PickAndSwap(swapTarget)
                                            # $ temp = story_pick_swap(swapTarget)
                                            # $ renpy.say(None, "[temp]")
                        else:
                            if not inventory["weapon"]:
                                $ gameVariable["gameState"] = GameState.Normal
                                $ gameVariable["bannerState"] = BannerState.Door

                                python:
                                    playerData["inven"]["weapon"].append(box[0])
                                    playerData["inven"]["weapon"][0]["current_durability"] = box[0]['current_durability']

                                call event_Pick(box[0])
                                # $ temp = story_picked(box[0])
                                # $ renpy.say(None, "[temp]")
                            else:
                                $ gameVariable["gameState"] = GameState.Swap
                                if box[0]["category"] == 'Armor':
                                    $ swapTarget = [playerData["inven"]["armor"][0], box[0]]
                                else:
                                    $ swapTarget = [playerData["inven"]["weapon"][0], box[0]]

                                $ keep_menu = keep_menu_gen(swapTarget[0]["name"])
                                $ change_menu = change_menu_gen(swapTarget[1]["name"])

                                menu:
                                    '[keep_menu]':
                                        $ gameVariable["gameState"] = GameState.Normal
                                        $ gameVariable["bannerState"] = BannerState.Door
                                    '[change_menu]':
                                        $ gameVariable["gameState"] = GameState.Normal
                                        $ gameVariable["bannerState"] = BannerState.Door

                                        if swapTarget[1]["category"] == EquipmentCategory.Armor.value:
                                            python:
                                                playerData["inven"]["armor"] = []
                                                playerData["inven"]["armor"].append(swapTarget[1])

                                            call event_PickAndSwap(swapTarget)
                                            # $ temp = story_pick_swap(swapTarget)
                                            # $ renpy.say(None, "[temp]")
                                        else:
                                            python:
                                                playerData["inven"]["weapon"] = []

                                                playerData["inven"]["weapon"].append(swapTarget[1])
                                                playerData["inven"]["weapon"][0]["current_durability"] = swapTarget[1]['current_durability']
                                                playerData["skillPoint"] = 0

                                            call event_PickAndSwap(swapTarget)
                                            # $ temp = story_pick_swap(swapTarget)
                                            # $ renpy.say(None, "[temp]")
                    'Choose Potion.':
                        play sound "<from 0.4>Drink-2.mp3" fadeout 0.3

                        $ gameVariable["gameState"] = GameState.Normal
                        $ gameVariable["bannerState"] = BannerState.Door
                        $ percent_table = ["Trenta size", "Half Gallon"]

                        if box[1]["suffix"] in percent_table:
                            $ heal_amount = math.trunc(playerData["max_hp"] * box[1]["effect"])
                        else:
                            $ heal_amount = box[1]["effect"]

                        if playerData["current_hp"] + heal_amount >= playerData["max_hp"]:
                            $ playerData["current_hp"] = playerData["max_hp"]
                            # $ temp = Deldebuff(HealState.Max, heal_amount)
                            # $ renpy.say(None, temp)
                            $ Deldebuff(HealState.Max, heal_amount)
                        else:
                            $ playerData["current_hp"] += heal_amount
                            # $ temp = Deldebuff(HealState.Heal, heal_amount)
                            # $ renpy.say(None, temp)
                            $ Deldebuff(HealState.Heal, heal_amount)

            elif lootingState == "Mimic":
                $ gameVariable["gameState"] = GameState.Normal
                $ gameVariable["bannerState"] = BannerState.Mimic

                if playerData["inven"]["armor"][0]['name'] == "Berserk":
                    call event_MimicAfraid
                    # $ temp = mimic_afraid()
                    # $ renpy.say(None, temp)
                else:
                    $ renpy.with_statement(hpunch)

                    if playerData["current_hp"] < gameVariable["mimic_dmg"]:
                        $ playerData["current_hp"] = 0
                        $ gameVariable["type_of_death"] = "N"
                        jump DeadScene
                    else:
                        $ playerData["current_hp"] -= gameVariable["mimic_dmg"]

                        if playerData["condition"]['Poisoned'] > 0:
                            $ playerData["condition"]["Poisoned"] = 0
                            call event_MimicCure(gameVariable["mimic_dmg"])
                            # $ temp = mimic_cured(gameVariable["mimic_dmg"])
                            # $ renpy.say(None, "[temp]")
                        else:
                            call event_MimicAttack(gameVariable["mimic_dmg"])
                            # $ temp = mimic_damaged(gameVariable["mimic_dmg"])
                            # $ renpy.say(None, "[temp]")

            elif lootingState == "Lose":
                play sound "<from 0.5 to 2>Door-Cabinet-2.mp3" fadeout 0.3

                $ gameVariable["bannerState"] = BannerState.Chest_empty
                call event_ChestEmpty
                # $ temp = chest_empty()
                # $ renpy.say(None, "[temp]")
        'Leave it alone and do some maintenance.':
            play sound "<from 0.3 to 2.3>Fire-2.mp3" fadeout 0.3

            $ gameVariable["bannerState"] = BannerState.Maintenance
            $ returnObject = maintenance()

            if returnObject["repair_data"]:
                $ target_data = returnObject["repair_data"]
                call event_MaintenanceRepair(target_data)
            elif returnObject["recover_data"]:
                $ target_data = returnObject["recover_dara"]

                if target_data == 0:
                    call event_HpFull
                else:
                    call event_MaintenanceRecover(target_data)


            # $ renpy.say(None, "[temp]")

    $ gameVariable["gameState"] = GameState.Normal
    $ gameVariable["bannerState"] = BannerState.Door

    return