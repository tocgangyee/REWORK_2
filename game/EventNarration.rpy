label event_ChestAppeared:
    "There's a box lying around.\nShall we open it?"
    return

label event_ChestEmpty:
    "The box was empty.\nYou put your disappointment behind you and moved on."
    return

label event_MimicAttack(damage):
    "The box was a Mimic.\nIt's too late to dodge Mimic's attack.\n\nDamaged [damage]."
    return

label event_MimicCure(damage):
    "The box was a Mimic.\nMimic bits you hard, but you feel healed.\n\nDamaged [damage] but poison got cured."
    return

label event_MimicAfraid:
    "Aura of 'Berserk' made Mimic tremble in fear.\n\nMimic did nothing."
    return

label event_HpFullDebuffRemove(WoundedFlag, PosisonFlag):
    if WoundedFlag == True and PosisonFlag == True:
        "Health has been restored to full, and debuff have disappeared."
    elif WoundedFlag == True and PosisonFlag == False:
        "Health has been restored to full, and wound have disappeared."
    elif WoundedFlag == False and PosisonFlag == True:
        "Health has been restored to full, and poison have disappeared."
    else:
        "Health has been restored to full, but nothing else has changed."
    return

label event_HpHealDebuffRemove(WoundedFlag, PosisonFlag, HealData):
    if WoundedFlag == True and PosisonFlag == True:
        "HP recovered [HealData] and debuff have disappeared."
    elif WoundedFlag == True and PosisonFlag == False:
        "HP recovered [HealData] and wound have disappeared."
    elif WoundedFlag == False and PosisonFlag == True:
        "HP recovered [HealData] and poison have disappeared."
    else:
        "HP recovered [HealData] but nothing else has changed."
    return

label event_HpFull:
    "Health has been restored to full."
    return

label event_HpHeal(value):
    "Health recovered [value]."
    return

label event_MaintenanceRecover(value):
    "Rested.\n\nRestored hp [value]."
    return

label event_LevelUp(DataSet):
    "Experience will always be flesh and blood.\n\nMax hp increased [DataSet[0]].\nDamage increased [DataSet[1]]."
    return

label event_BattleWin:

    $ scriptTarget = random.choice(range(0,3))

    if scriptTarget == 0:
        "The battle was successful."
    elif scriptTarget == 1:
        "Force is often the best conversation tool."
    elif scriptTarget == 2:
        "Leaving the cold corpses behind."

    return

label event_MonsterAppeared(monsters):
    $ scriptArray = ""

    python:
        monster_names = ", ".join([renpy.translate_string(monster.name_en) for monster in monsters])
        scriptArray = __("{} appeared!").format(add_postposition1(monster_names))

    "[scriptArray]"

    return

label event_PlayerRunFailed:
    "You try to run away, but a monster blocks your path."
    return

label event_PlayerRunSuccess:
    $ scriptTarget = random.choice(range(0,3))

    if scriptTarget == 0:
        "You ran frantically toward the door.\nThey weren't hungry, so they didn't chase me persistently."
    elif scriptTarget == 1:
        "You quickly ran away.\nContrary to my expectations, I had plenty of time."
    elif scriptTarget == 2:
        "The attack swung at me narrowly missed.\nLuckily, I was able to escape unharmed."

    return

label event_MonsterDead(target):
    $ scriptTarget = random.choice(range(0,3))

    if scriptTarget == 0:
        "[target] is already dead."
    elif scriptTarget == 1:
        "[target] is already cold."
    elif scriptTarget == 2:
        "There's no time to waste on [target]."

    return

label event_MonsterAttack(data):
    $ cnt = 0
    $ output = []

    while cnt < len(data):
        if cnt in data.keys():
            $ target = data[cnt]
            if target[3]:
                $ output.append(__("{0} can't come to his senses.").format(add_postposition3(renpy.translate_string(target[0]))))
            else:
                if target[1]:
                    $ output.append(__("{0} attacked you.\nDamaged {1}.").format(add_postposition1(renpy.translate_string(target[0])), target[2]))
                else:
                    $ scriptTarget = random.choice(range(0,2))
                    if scriptTarget == 0:
                        $ output.append(__("{0}'s attack missed.").format(renpy.translate_string(target[0])))
                    elif scriptTarget == 1:
                        $ output.append(__("{0}'s attack narrowly missed.").format(renpy.translate_string(target[0])))

        $ cnt += 1

    $ final_output = '\n\n'.join(output)
    "[final_output]"

    return

label event_PlayerAttackSuccess(value):
    $ scriptTarget = random.choice(range(0,3))

    if scriptTarget == 0:
        $ tlName = add_postposition2(renpy.translate_string(value[0]))
        "You attacked [tlName]!\nDamaged [value[1]]."
    elif scriptTarget == 1:
        $ tlName = add_postposition2(renpy.translate_string(value[0]))
        "Your attack struck [tlName]!\nDamaged [value[1]]."
    elif scriptTarget == 2:
        $ tlName = add_postposition1(renpy.translate_string(value[0]))
        "[tlName] was in severe pain.\nDamaged [value[1]]."

    return

label event_PlayerAttackFailed:
    $ scriptTarget = random.choice(range(0,2))

    if scriptTarget == 0:
        "It brushed off the attack as if to tease you.\n"
    elif scriptTarget == 1:
        "Your blows cut through the air.\n"

    return

label event_HuginnDodge:
    "Huginn used the last strength to hijack your weapon."
    return

label event_ConditionOccur(data):
    $ cnt = 0
    $ output = []

    while cnt < len(data):
        if data[cnt][1] == "Poisoned":
            $ tlName = add_postposition3(renpy.translate_string(data[cnt][0]))
            $ output.append(__("You've been poisoned by {0}'s attack.").format(add_postposition3(renpy.translate_string(data[cnt][0]))))
        elif data[cnt][1] == "Wounded":
            $ output.append(__("You've got wound by {0}'s attack.").format(data[cnt][0]))
        elif data[cnt][1] == "Rusted":
            $ output.append(__("You've got curse of rust by {0}'s attack.").format(data[cnt][0]))
        $ cnt += 1

    $ final_output = '\n\n'.join(output)
    "[final_output]"

    return

label event_Swift(data):
    $ cnt = 0
    $ output = []

    while cnt < len(data):
        $ value = data[cnt]
        if value[0]:
            $ output.append(__("{0} used Quick Attack!\n Damaged {1}.").format(renpy.translate_string(value[1]['name']), value[2]))
        else:
            $ scriptTarget = random.choice(range(0,2))
            if scriptTarget == 0:
                $ output.append(__("Unexpected, but {0}'s attack missed.").format(renpy.translate_string(value[1]['name'])))
            elif scriptTarget == 1:
                $ output.append(__("{0} aimed for the vital spot, but was too slow.").format(add_postposition1(renpy.translate_string(value[1]['name']))))

        $ cnt += 1

    $ final_output = '\n\n'.join(output)
    "[final_output]"

    return

label event_Blessing(data):
    if data['target'] == "lck":
        "You poor thing, God looked after you.\n[data['value']] point of luck has increased."
    elif data['target'] == "str":
        "You poor thing, God looked after you.\n[data['value']] point of str has increased."
    elif data['target'] == "dex":
        "You poor thing, God looked after you.\n[data['value']] point of dex has increased."

    return

label event_Pick(data):
    $ filter = ('str', 'dmg', 'dex', 'lck', 'current_durability')
    $ output = []

    if data['category'] == 'Armor':
        $ scriptTarget = random.choice(range(0,2))
        if scriptTarget == 0:
            $ output.append(__("{0} is worn.\nIt will be a great help in combat.\n").format(add_postposition2(renpy.translate_string(data['name']))))
        elif scriptTarget == 1:
            $ output.append(__("It will be a great help in combat.\nYou feel empowered.\n"))
    else:
        $ output.append(__("You pick up {0}.\nIt feels very good to hold.\n").format(data['name']))

    $ cnt = 0
    $ keys = data.keys()
    while cnt < len(keys):
        if keys[cnt] in filter:
            $ target = keys[cnt]
            $ tlName = add_postposition1(renpy.translate_string(target))
            if data[target] > 0:
                $ output.append(__("{0} increased {1}.").format(tlName, data[target]))
            elif data[target] < 0:
                $ output.append(__("{0} decreased {1}.").format(tlName, data[target]))

        $ cnt += 1

    $ final_output = '\n'.join(output)
    "[final_output]"

    return

label event_PickAndSwap(data):
    $ filter = ('str', 'dmg', 'dex', 'lck', 'current_durability')
    $ output = []

    $ output.append(__("Take the {0} instead of the {1}.\n").format(add_postposition2(renpy.translate_string(data[1]['name'])),renpy.translate_string(data[0]['name'])))

    $ cnt = 0
    while cnt < len(filter):
        $ target = filter[cnt]
        $ tlName = add_postposition1(renpy.translate_string(target))
        if data[0][target] > data[1][target]:
            $ gap = data[0][target] - data[1][target]
            $ output.append(__("{0} decreased {1}.").format(tlName, gap))
        elif data[0][target] < data[1][target]:
            $ gap = data[1][target] - data[0][target]
            $ output.append(__("{0} increased {1}.").format(tlName, gap))
        
        $ cnt += 1

    $ final_output = '\n'.join(output)
    "[final_output]"

    return

label event_MaintenanceRepair(data):
    $ output = []

    $ scriptTarget = random.choice(range(0,2))
    if scriptTarget == 0:
        $ output.append(__("You have repaired a broken piece of equipment.\n\n"))
    elif scriptTarget == 1:
        $ output.append(__("Repair damaged equipment.\n\n"))
    
    $ cnt = 0
    while cnt < len(data):
        $ target_data = data[cnt]

        if target_data[0]['category'] == 'Weapon':
            if target_data[1] == 0:
                $ output.append(__("{0}'s condition is already perfect.\n\n").format(target_data[0]['name']))
                # if preferences.language == "korean":
                #     result += f"{translation_name(val[0]['name'], preferences.language)}의 상태는 이미 완벽합니다.\n\n"
                # else:
                #     result += f"{val[0]['name']}'s condition is already perfect.\n\n"
            else:
                $ output.append(__("{0}'s durability has been restored by {1}.\n\n").format(renpy.translate_string(target_data[0]['name']), target_data[1]))
                # if preferences.language == "korean":
                #     result += f"{translation_name(val[0]['name'], preferences.language)}의 내구도가 {val[1]}만큼 회복됩니다.\n\n"
                # else:
                #     result += f"{val[0]['name']}'s durability has been restored by {val[1]}.\n\n"
        else:
            if target_data[1][0] == "enhancement":
                $ output.append(__("{0}'s condition is better than before.\n").format(target_data[0]['name']))
                # if preferences.language == "korean":
                #     result += f"{translation_name(val[0]['name'], preferences.language)}의 상태는 전보다 좋아졌습니다.\n"
                # else:
                #     result += f"{val[0]['name']}'s condition is better than before.\n"
            else:
                $ output.append(__("{0}'s durability has been restored by {1}.\n").format(target_data[0]['name'], target_data[1]))
                # if preferences.language == "korean":
                #     result += f"{translation_name(val[0]['name'], preferences.language)}의 내구도가 {val[1]}만큼 회복됩니다.\n"
                # else:
                #     result += f"{val[0]['name']}'s durability has been restored by {val[1]}.\n"
        
        $ cnt += 1

    return

label event_PlayerSkill(data, monster_lst):
    $ output = []

    $ skillData_assem = {}
    $ isAttackedCorpse = False
    $ downed = []

    $ cnt = 0
    while cnt < len(data):
        $ target_data = data[cnt]
        if target_data[1] > 0:
            $ skillData_assem[target_data[0]] = skillData_assem.get(target_data[0], 0) + target_data[2]
            if target_data[1] <= target_data[2]:
                $ downed.append(target_data[0])
        else:
            $ isAttackedCorpse = True

        $ cnt += 1

    $ output.append(__("The resistance felt through the weapon is different.\n\n"))

    $ cnt = 0
    $ target_filter = skillData_assem.keys()
    while cnt < len(skillData_assem):
        if cnt in target_filter:
            $ damage = skillData_assem[cnt]
            $ target_name = monster_lst[cnt]['name']

            $ output.append(__("You attacked {0} and damaged {1}.\n").format(target_name, damage))

        $ cnt += 1

    if isAttackedCorpse:
        $ output.append(__("Corpses were also swept up in the attack.\n\n"))
    
    if downed:
        # for idx in downed:
        #     target_name = monsters[idx]['name']

        #     if preferences.language == "korean":
        #         result += f"{add_postposition3(translation_name(target_name, preferences.language))} 공격을 버틸 수 없었습니다.\n"
        #     else:
        #         result += f"{target_name} could not withstand the attack.\n"
        $ target_names = ""

        $ cnt = 0
        while cnt < len(downed):
            $ target_names += monster_lst[cnt]['name']
            $ cnt += 1

        $ output.append(__("{0} could not withstand the attack.\n").format(target_names))
        # if preferences.language == "korean":
        #     result += f"{add_postposition3(target_names)} 공격을 버틸 수 없었습니다.\n"
        # else:
        #     result += f"{target_names} could not withstand the attack.\n"

    $ final_output = '\n'.join(output)
    "[final_output]"

    return

label event_DebuffMordern(poison, wound, rust, dmg_set):
    $ output = []

    if poison == 'Damaged':
        $ output.append(__("{0} damage from Poison!\n").format(dmg_set[0]))
    elif poison == 'Sleep':
        $ output.append(__("You're body got adapted on poison.\n"))

    if wound == DebuffState.Damaged:
        $ output.append(__("{0} damage from Wound!\n").format(dmg_set[1]))
    elif wound == DebuffState.DamagedAndCure:
        $ output.append(__("{0} damage from Wound!\nWound has been cured naturally.\n").format(dmg_set[1]))

    if rust:
        $ target = rust[0]
        $ state = rust[1]

        if target == EquipmentCategory.Armor:
            if state == DebuffState.Damaged:
                $ output.append(__("Some part of armor has fall off.\n"))
            elif state == DebuffState.Break:
                $ output.append(__("The armor can do its job anymore.\n"))
            elif state == DebuffState.DamagedAndCure:
                $ output.append(__("The armor can do its job anymore.\nThe curse of corrosion is gone.\n"))
            elif state == DebuffState.BreakAndCure:
                $ output.append(__("The armor can do its job anymore.\nThe curse of corrosion is gone.\n"))
        elif target == EquipmentCategory.Weapon:
            if state == DebuffState.Damaged:
                $ output.append(__("Some part of weapon has fall off.\n"))
            elif state == DebuffState.Break:
                $ output.append(__("The weapon can do its job anymore.\nThe curse of corrosion is gone.\n"))
            elif state == DebuffState.DamagedAndCure:
                $ output.append(__("Some part of weapon has fall off.\nThe curse of corrosion is gone.\n"))
        elif target == EquipmentCategory.Non:
            $ output.append(__("The Curse of Corrosion does not have any effect.\n"))
        else:
            $ output.append(__("has an error"))
        
    $ final_output = '\n'.join(output)
    "[final_output]"

    return