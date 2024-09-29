init python:
    import copy
    import math
    import csv

    def attack_menu(names):
        result = []

        for name in names:
            if preferences.language == "korean":
                result.append(f"{add_postposition2(translation_name(name, preferences.language))} 공격한다.")
            else:
                result.append(f"Attack {name}.")

        return result

    # checking target is dead
    def killCheck_all(monsters: dict) -> bool:
        checker = False
        for val in monsters:
            if val.current_hp <= 0:
                checker = True
            else:
                checker = False
                break
        return checker
    
    # checking whole monsters dead
    def killCheck(monsters: dict, target: int) -> bool:
        if monsters[target]['current_hp'] <= 0:
            return True
        else:
            return False

    #player's lvup
    def lvUpSys():
        playerData['max_hp'] += 10
        playerData['str'] += 0.5
        # parse data with realdata temporary.

        playerData['current_hp'] += int(playerData['max_hp'] * 0.1)

        if playerData['current_hp'] >= playerData['max_hp']:
            playerData['current_hp'] = playerData['max_hp']

        playerData['current_exp'] -= playerData['max_exp']
        playerData['max_exp'] += 10

        # temp = story_levelup([10, 0.5])
        renpy.call(event_LevelUp([10, 0.5]))
        return temp

    def target_check():
        while playerData['current_exp'] >= playerData['max_exp']:
            # renpy.say(None, "call level up")
            temp = lvUpSys()
            renpy.say(None, temp)

    def expSys():
        exp_amount = 0

        if playerData['inven']['armor'][0]['name'] == "Berserk":
            if target.current_hp <= 0:
                target.current_hp = 0
                exp_amount = target.exp * 1.5
        else:
            if target.current_hp <= 0:
                target.current_hp = 0
                exp_amount = target.exp

        playerData['current_exp'] += math.floor(exp_amount)

    def name_extracter(monsters):
        result = []

        for monster in monsters:
            result.append(monster.name_en)
        
        return result

    def isIllusion(stage, playerHP):
        if stage >= 30 and playerHP[0] <= playerHP[1] * 0.25:
            return random.choices([True, False], [0.25, 0.75])[0]

label Battle():

    # Battle이 끝난 경우에도 일정 확률로 jump Chest를 통해 Looting을 진행할 수 있어야 한다.

    $ gameVariable["bannerState"] = BannerState.Battle

    $ battleFlag = True
    # $ damaged = []
    $ runFlag = False
    # $ target = None

    call event_MonsterAppeared(target_lst)
    
    if not isIllusion(stage=gameVariable['stage'], playerHP=(playerData['current_hp'], playerData['max_hp'])):
        # $ swiftNarration, swiftStat = swift(monsters)

        # if swiftStat:
        #     $ renpy.with_statement(hpunch)

        # if swiftNarration != '':
        #     "[swiftNarration]"

        if playerData['current_hp'] == 0:
            $ gameVariable["type_of_death"] = "B"
            jump DeadScene

        while battleFlag:
            $ monsters = target_lst
            $ target_names = name_extracter(monsters)
            $ menu_for_names = attack_menu(target_names)

            menu:
                # '[attack_menu(target_names[0])]' if len(monsters) >= 1:
                '[menu_for_names[0]]' if len(monsters) >= 1:
                    $ target = monsters[0]
                    # $ result, damaged, skillTriggered, transitionTarget = player_attack(target, 0)
                    $ result = player_attack(target, 0)

                    # $ transitionVariable["target_battle"] = list(transitionTarget)

                    # show screen DefaultUI(playerData)

                    # if transitionVariable["target_battle"]:
                    #     play sound "Sword-1.mp3" fadeout 0.3
                    #     $ renpy.pause(0.5)
                    #     $ transitionVariable["target_battle"] = []
                    # else:
                    #     play sound "Swish-1.mp3" fadeout 0.3

                    $ result_cnt = 0
                    while result_cnt < len(result):
                        $ tempData = result[result_cnt]
                        if tempData['attackFlag']:
                            call event_PlayerAttackSuccess([target.name_en, tempData["damage"]])
                        else:
                            call event_PlayerAttackFailed
                        $ result_cnt += 1

                    # if result[0]['attackFlag']:
                    #     call event_PlayerAttackSuccess([target.name_en, result["damage"]])
                    # else:
                    #     call event_PlayerAttackFailed

                    # "[result]"

                '[menu_for_names[1]]' if len(monsters) >= 2:
                    $ target = monsters[1]
                    # if target['prefix'] == 'Body':
                    #     $ w_check = wing_check(monsters)
                    #     if w_check:
                    #         $ result, damaged, skillTriggered, transitionTarget = player_attack(target, 1)
                    #     else:
                    #         call event_PlayerAttackFailed
                    #         # $ result = player_atk_failed()
                    # else:


                    # $ atk_result, damaged, skillTriggered, transitionTarget = player_attack(target, 1)
                    $ result = player_attack(target, 1)
                    # $ transitionVariable["target_battle"] = list(transitionTarget)

                    # show screen DefaultUI(playerData)

                    # if transitionVariable["target_battle"]:
                    #     play sound "Sword-1.mp3" fadeout 0.3
                    #     $ renpy.pause(0.5)
                    #     $ transitionVariable["target_battle"] = []
                    # else:
                    #     play sound "Swish-1.mp3" fadeout 0.3

                    $ result_cnt = 0
                    while result_cnt < len(result):
                        $ tempData = result[result_cnt]
                        if tempData['attackFlag']:
                            call event_PlayerAttackSuccess([target.name_en, tempData["damage"]])
                        else:
                            call event_PlayerAttackFailed
                        $ result_cnt += 1


                    # for val in result:
                    #     if val['attackFlag']:
                    #         call event_PlayerAttackSuccess([target.name_en, result["damage"]])
                    #     else:
                    #         call event_PlayerAttackFailed

                    # if result["attackFlag"]:
                    #     call event_PlayerAttackSuccess([target.name_en, result["damage"]])
                    # else:
                    #     call event_PlayerAttackFailed

                    # "[result]"

                '[menu_for_names[2]]' if len(monsters) >= 3:
                    $ target = monsters[2]
                    $ result = player_attack(target, 1)

                    # $ atk_result, damaged, skillTriggered, transitionTarget = player_attack(target, 2)
                    # $ transitionVariable["target_battle"] = list(transitionTarget)

                    # show screen DefaultUI(playerData)

                    # if transitionVariable["target_battle"]:
                    #     play sound "Sword-1.mp3" fadeout 0.3
                    #     $ renpy.pause(0.5)
                    #     $ transitionVariable["target_battle"] = []
                    # else:
                    #     play sound "Swish-1.mp3" fadeout 0.3

                    $ result_cnt = 0
                    while result_cnt < len(result):
                        $ tempData = result[result_cnt]
                        if tempData['attackFlag']:
                            call event_PlayerAttackSuccess([target.name_en, tempData["damage"]])
                        else:
                            call event_PlayerAttackFailed
                        $ result_cnt += 1


                    # for val in result:
                    #     if val['attackFlag']:
                    #         call event_PlayerAttackSuccess([target.name_en, result["damage"]])
                    #     else:
                    #         call event_PlayerAttackFailed
                    # if result["attackFlag"]:
                    #     call event_PlayerAttackSuccess([target.name_en, result["damage"]])
                    # else:
                    #     call event_PlayerAttackFailed

                    # "[result]"

                'Run':
                    $ runFlag = BattleCalculate.cal_runSuccess(playerData["dex"], playerData["lck"])

                    if runFlag:
                        play sound "<from 0 to 1>Footsteps-Hard-Marble-Run-2.mp3" fadeout 0.3
                        $ battleFlag = False
                        $ gameVariable["gameState"] = GameState.Normal
                        $ gameVariable["bannerState"] = BannerState.Door

                        $ temp = player_run_success()
                        $ renpy.say(None, temp)
                    else:
                        $ temp = player_run_failed()
                        $ renpy.say(None, temp)

            $ target_check()

            $ isAllDead = killCheck_all(monsters)
            if isAllDead:
                # $ temp = story_win()
                # $ renpy.say(None, temp)
                call event_BattleWin()

                $ isGrace = random.choices([True, False], [playerData['lck'], 100 - (playerData['lck'])])[0]
                if isGrace:
                    $ gameVariable['bannerState'] = BannerState.Grace
                    # $ gameVariable["bannerState"] = "grace"
                    $ temp = godsGrace()
                    $ renpy.say(None, temp)

                $ battleFlag = False
                $ gameVariable["gameState"] = GameState.Normal
                $ gameVariable["bannerState"] = BannerState.Door
            else:
                if runFlag:
                    $ battleFlag = False
                    $ gameVariable["gameState"] = GameState.Normal
                    $ gameVariable["bannerState"] = BannerState.Door
                else:
                    # $ battleData = monster_phase(damaged)
                    $ battleData = monster_phase()
                    # $ temp = event_MonsterAttack(battleData)
                    # $ renpy.say(None, temp)
                    call event_MonsterAttack(battleData)

                    if playerData['current_hp'] == 0:
                        $ gameVariable["type_of_death"] = "N"
                        jump DeadScene
                    # if debuff_added != []:
                    #     $ temp2 = condition_problem(debuff_added)
                    #     "[temp2]"
    else:
        call Illusion