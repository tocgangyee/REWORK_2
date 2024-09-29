# Initializing data for game system
init python:
    import random
    import json

    playerData_og = json.load(renpy.file("data/Player.json"))
    mWeight = json.load(renpy.file("data/Game_weight.json"))["monster_tier"]
    eWeight = json.load(renpy.file("data/Game_weight.json"))["equipment_tier"]
    pWeight = json.load(renpy.file("data/Game_weight.json"))["potion_tier"]
    mon_cntWeight = json.load(renpy.file("data/Game_weight.json"))["monster_cntweight"]
    mTable = copy.deepcopy(monster_table)
    pTable = copy.deepcopy(potions)
    eTable = copy.deepcopy(equipments)

    def randomEncounter():
        eventList = ["Battle", "Looting", "Maintenance"]

        # 이벤트별 확률이 생기면 choices로 바꿔야함. 지금은 동률이라 choice
        return random.choice(eventList)

    def upstairProtocol(data):
        data["stage"] += 1
        if data["stage"] % 10 == 0:
            data["cntnum"] += 1

        data["cntWeight"] = mon_cntWeight[data["cntnum"]]

        if mWeight[0] <= 0:
            mWeight[0] = 0
        else:
            mWeight[0] -= 1
        eWeight[0] -= 0.25
        pWeight[0] -= 0.25

        mWeight[2] += 1
        eWeight[2] += 0.25
        pWeight[2] += 0.25

        if data["stage"] == 30:
            gameVariable["gameState"] = GameState.Midlevel

        elif data["stage"] == 70:
            gameVariable["gameState"] = GameState.Abyss

        return data

    def berserkLogic():
        if playerData['inven']['armor'][0]['name'] == 'Berserk':
            playerData['current_hp'] -= 5
            if playerData['current_hp'] <= 0:
                playerData['current_hp'] = 0
                return True

    def debuff_damage(wound_damage_limit, rust_damage_limit, data):
        poison_effect = 'None'
        wound_effect = 'None'
        rust_effect = []

        isDead = False

        if data['condition']['Poisoned'] > 0:
            if data['current_hp'] > 20:
                data['current_hp'] -= gameVariable["poison_dmg"]
                poison_effect = 'Damaged'
            else:
                poison_effect = 'Sleep'

        # 'Wounded' 상태를 체크하여 처리합니다.
        if data['condition']['Wounded'] > 0:
            # 'Wounded' 상태가 있으면 피해를 받고, 'Wounded' 수치를 감소시킵니다.
            data['current_hp'] -= gameVariable["wound_dmg"]
            data['condition']['Wounded'] -= 1

            if data['condition']['Wounded'] == 0:
                wound_effect = DebuffState.DamagedAndCure
            else:
                wound_effect = DebuffState.Damaged

            # 현재 HP가 0 이하가 되면, 캐릭터는 죽음 상태로 전환됩니다.
            if data['current_hp'] <= 0:
                data['current_hp'] = 0
                isDead = True

        if data['condition']['Rusted'] <= 0:
            # Rust가 발동되지 않는 경우
            # rust_effect = [EquipmentCategory.Non, DebuffState.NonEffect]
            # data['condition']['Rusted'] = 0
            pass
        else:
            # Armor의 현재 내구도를 확인합니다.
            armor_durability = data['inven']['armor'][0]['current_durability']
            weapon_name = data['inven']['weapon'][0]['name']

            if armor_durability > 0:
                # Rust on armor
                data['inven']['armor'][0]['current_durability'] -= gameVariable["rust_dmg"]
                data['condition']['Rusted'] -= 1

                if data['inven']['armor'][0]['current_durability'] <= 0:
                    # armor broken
                    data['inven']['armor'][0]['current_durability'] = 0

                    if data['condition']['Rusted'] > 0:
                        # 방어구 파괴, 부식의 턴이 남은 경우
                        rust_effect = [EquipmentCategory.Armor, DebuffState.Break]
                    else:
                        # 방어구 파괴, 부식의 턴이 남지 않은 경우 (치유)
                        data['condition']['Rusted'] = 0
                        rust_effect = [EquipmentCategory.Armor, DebuffState.BreakAndCure]
                else:
                    # armor is not broken
                    if data['condition']['Rusted'] > 0:
                        #방어구 손상, 부식의 턴이 남은 경우
                        rust_effect = [EquipmentCategory.Armor, DebuffState.Damaged]
                    else:
                        # 방어구 손상, 부식의 턴이 남지 않은 경우 (치유)
                        data['condition']['Rusted'] = 0
                        rust_effect = [EquipmentCategory.Armor, DebuffState.DamagedAndCure]

            elif weapon_name != 'Bare Hand':
                # Rust effected on weapon instead of armor
                data['inven']['weapon'][0]['current_durability'] -= 1
                data['condition']['Rusted'] -= 1

                if data['inven']['weapon'][0]['current_durability'] <= 0:
                    # 방어구 대신 무기가 파괴, 부식이 사라지는 경우
                    data['inven']['weapon'][0]['current_durability'] = 0
                    data['condition']['Rusted'] = 0
                    data['skillPoint'] = 0
                    data['inven']['weapon'][0] = bare_hand_data["Bare Hand"]

                    rust_effect = [EquipmentCategory.Weapon, DebuffState.Break]
                else:
                    if data['condition']['Rusted'] > 0:
                        # 방어구 대신 무기가 손상
                        rust_effect = [EquipmentCategory.Weapon, DebuffState.Damaged]
                    else:
                        # 방어구 대신 무기가 손상, 부식의 턴이 남지 않은 경우 (치유)
                        data['condition']['Rusted'] = 0
                        rust_effect = [EquipmentCategory.Weapon, DebuffState.DamagedAndCure]
            # 여기서, 'weapon'이 'Bare Hand'인 경우는 자동으로 제외됩니다.
            else:
                data['condition']['Rusted'] = 0
                rust_effect = [EquipmentCategory.Non, DebuffState.NonEffect]
                # 부식이 의미가 없는 경우

        resultObject = {"poison_effect": poison_effect, "wound_effect": wound_effect, "rust_effect": rust_effect, "game_data": [gameVariable['poison_dmg'], gameVariable['wound_dmg'], gameVariable['rust_dmg']]}

        return resultObject, isDead, data

    def check_debuff():
        # flag = False

        # for val in playerData['condition']:
        #     if playerData['condition'][val] > 0:
        #         flag = True
        
        # return flag
        return any(condition > 0 for condition in playerData['condition'].values())

    def huginn_main_buff(monsters):
        monsters[0]['current_hp'] -= gameVariable['huginnDeadCount']*5
        monsters[1]['dmg'] += gameVariable['hijack_count']
        monsters[2]['current_hp'] -= gameVariable['huginnDeadCount']*5
        return monsters

    def muninn_main_buff(monsters):
        monsters[0]['current_hp'] += gameVariable['rust_count']*5
        monsters[1]['dmg'] -= gameVariable['muninnDeadCount']
        monsters[2]['current_hp'] += gameVariable['rust_count']*5
        return monsters


transform center_align:
    xalign 0.5
    yalign 0.5

# game initializing
label start():
    $ renpy.block_rollback()

    $ gameVariable = {
        "gameState" : GameState.Opening,
        "bannerState" : BannerState.Door,
        "stage_in_battle" : 1,
        "battle_limit" : 0,
        "stage" : 1,
        "cntnum" : 0,
        "tierWeight" : mWeight,
        "cntWeight" : mon_cntWeight[0],
        "wound_damage_limit" : 5,
        "type_of_death" : '',
        "mimic_dmg" : 10,
        "poison_dmg" : 5,
        "wound_dmg" : 5,
        "armor_repair_amount" : 10,
        "weapon_repair_amount" : 2,
        "entering_midlevel" : False,
        "entering_abyss" : False
    }

    $ transitionVariable = {
        "target_battle" : [],
        "bg_glitch" : False
    }

    $ playerData = json.load(renpy.file("data/Player.json"))

    # $ huginn_stage = 69
    # $ muninn_stage = random.randint(70, 99)

    jump Phase_Start  

# play start story
label Phase_Start():
    stop music

    if not persistent.Prologue:
        call Prologue
    
    scene normal
    show screen DefaultUI

    if not persistent.FirstDead:
        call Opening
    else:
        call Opening_ifDead

    jump Something

label Something():
    $ gameVariable["battle_limit"] = random.randint(5,10)

    $ encounterFlag = randomEncounter()

    if encounterFlag == "Battle":
        $ target_lst = load_monster(gameVariable, gameVariable["stage"])
        # TODO: load_monster는 battle에서 하는 걸로 변경
        jump Battle
    elif encounterFlag == "Looting":
        jump Chest
    # TODO: Maintenance 추가 예정
    # elif encounterFlag == "Maintenance":
        # jump 
    # Something 종료
    if gameVariable["stage_in_battle"] <= gameVariable["battle_limit"]:
        $ gameVariable["stage_in_battle"] += 1
        jump Something

    while gameVariable["stage_in_battle"] <= gameVariable["battle_limit"]:
        if battle:
            # entering battle phase
            # $ gameVariable["gameState"] = GameState.Battle
            # $ gameVariable["bannerState"] = BannerState.Battle
            $ target_lst = load_monster(gameVariable, gameVariable["stage"])

            call Battle

        # entering looting phase
        if randomIncounter():
            $ gameVariable["gameState"] = GameState.Chest
            $ gameVariable["bannerState"] = BannerState.Chest

            call Chest

# main game logic with staging
label Staging():
    
    $ gameVariable = upstairProtocol(copy.deepcopy(gameVariable))
    
    if gameVariable["stage"] < 30:
        scene normal
    elif 30 <= gameVariable["stage"] < 70:
        scene midlevel
        if gameVariable["entering_midlevel"] == False:
            $ gameVariable["entering_midlevel"] = True
            call Midlevel
    elif 70 <= gameVariable["stage"]:
        scene abyss
        if if gameVariable["entering_abyss"] == False:
            $ gameVariable["entering_abyss"] = True
            call Abyss

    $ renpy.full_restart()

label game():
    stop music

    while gameVariable["stage"] <= 100:

        # if gameVariable["stage"] == huginn_stage:
        #     $ gameVariable["gameState"] = GameState.Battle
        #     # $ hugiData = json.load(renpy.file("data/Huginn.json"))
        #     $ hugiData = copy.deepcopy(Huginn['Huginn'])
        #     $ hugiData = huginn_main_buff(hugiData)
        #     call Battle(gameVariable, hugiData)
        # elif gameVariable["stage"] == muninn_stage:
        #     $ gameVariable["gameState"] = GameState.Battle
        #     # $ muniData = json.load(renpy.file("data/Muninn.json"))
        #     $ muniData = copy.deepcopy(Muninn['Muninn'])
        #     # $ monsters = muniData['Muninn']
        #     $ muniData = muninn_main_buff(muniData)
        #     call Battle(gameVariable, muniData)
        # else:
            # entering battle phase
        $ gameVariable["gameState"] = GameState.Battle
        $ gameVariable["bannerState"] = BannerState.Battle
        $ target_lst = load_monster(gameVariable, gameVariable["stage"])

        call Battle(gameVariable, target_lst)

        # entering looting phase
        if randomIncounter():
            $ gameVariable["gameState"] = GameState.Chest
            $ gameVariable["bannerState"] = BannerState.Chest

            call Chest

            $ gameVariable['stage_in_battle'] += 1


        $ gameVariable['stage_in_battle'] = 1

        if transitionVariable["bg_glitch"]:
            if gameVariable["stage"] < 30:
                scene normal glitched
                $ transitionVariable["bg_glitch"] = False
            elif 30 <= gameVariable["stage"] < 70:
                scene midlevel glitched
                $ transitionVariable["bg_glitch"] = False
            elif 70 <= gameVariable["stage"]:
                scene abyss glitched
                $ transitionVariable["bg_glitch"] = False

        menu:
            # '앞으로 나아간다' :

            'Go upstair.':
                # play sound "<from 0 to 1.3>Footstep1.mp3" volume 0.5 fadeout 0.3
                play sound "<from 0.2 to 1.3>Footstep2.mp3" fadeout 0.3

                $ gameVariable = upstairProtocol(gameVariable)




                $ HasDebuff = check_debuff()

                if HasDebuff:
                    $ debuff_object, isDead, playerData = debuff_damage(gameVariable["wound_damage_limit"], gameVariable["rust_damage_limit"], playerData)

                    if isDead:
                        $ gameVariable['type_of_death'] = "W"
                        jump DeadScene
                    else:
                        # resultObject = {"poison_effect": poison_effect, "wound_effect": wound_effect, "rust_effect": rust_effect, "game_data": [gameVariable['poison_dmg'], gameVariable['wound_dmg'], gameVariable['rust_dmg']]}
                        call event_DebuffMordern(debuff_object['poison_effect'], debuff_object['wound_effect'], debuff_object['rust_effect'], debuff_object['game_data'])
                        # "[debuff_result]"

                if berserkLogic():
                    $ gameVariable["type_of_death"] = "B"
                    jump DeadScene

        if playerData['current_hp'] == 0:
            jump DeadScene

        if gameVariable["stage"] == 100:
            jump Ending

    return