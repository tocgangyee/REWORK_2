init python:
    # checking target is dead
    def killCheck_all(monsters: dict) -> bool:
        checker = False
        for val in monsters:
            if val['current_hp'] <= 0:
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

    result_template = {
        "skillFlag": False, # 스킬 사용 여부
        "attackFlag": False, # 일반 공격 성공 여부
        "corpseFlag": False, # 대상 몬스터가 이미 죽어있는지
        "target": 0, # 이번 공격으로 데미지를 입은 대상
        "damage": 0, # 이번 공격의 데미지
        "downFlag": False # 이번 공격으로 대상이 죽었는지
    }

    #player's act : skill
    def skill(damage, target_no):
        damaged = []
        transitionTarget = []
        result = ""

        skillData = []
        temp = []

        if playerData['inven']['weapon'][0]['skill'] == 'SwordSkill':
            temp.append([target_no, monsters[target_no]['current_hp'], damage * 2])
            skillData = temp
            result += player_skill(skillData)
            monsters[target_no]['current_hp'] -= damage * 2
        elif playerData['inven']['weapon'][0]['skill'] == 'HammerSkill':
            for i in range(len(monsters)):
                temp.append([i, monsters[i]['current_hp'], damage])
                monsters[i]['current_hp'] -= damage
                transitionTarget.append(i)

            skillData = temp
            result += player_skill(skillData)
            damaged = [0, 1, 2]

        elif playerData['inven']['weapon'][0]['skill'] == 'DaggerSkill':
            for _ in range(5):
                random_atk = random.choice(range(0, len(monsters)))
                temp.append([random_atk, monsters[random_atk]['current_hp'], damage])
                monsters[random_atk]['current_hp'] -= damage
                transitionTarget.append(random_atk)

            skillData = temp
            result += player_skill(skillData)

        for i in monsters:
            if i['current_hp'] < 0:
                i['current_hp'] = 0

        return result, damaged, transitionTarget

    # monster's act: stunned, atack
    # TtODO: debuff logic
    def monster_phase():
        battleData = {}
        debuff_lst = []
        animationStat = False

        for idx, val in enumerate(monsters):
            if val.current_hp > 0:
                damage = cal_damage_mon(val.stat_str, val.dmg)
                # if idx in damaged:
                #     battleData[idx] = [val.name, False, 0, True, "None"]
                # else:
                _successFlag = cal_atkSuccess_mon(dex=val.stat_dex, lck=val.stat_lck)
                if _successFlag:
                    animationStat = True
                    if playerData['current_hp'] + playerData['inven']['armor'][0]['current_durability'] <= damage:
                        playerData['inven']['armor'][0]['current_durability'] = 0
                        playerData['current_hp'] = 0
                    else:
                        if playerData['inven']['armor'][0]['current_durability'] > damage:
                            playerData['inven']['armor'][0]['current_durability'] -= damage
                        else:
                            playerData['inven']['armor'][0]['current_durability'] = 0
                            playerData['current_hp'] -= (damage - playerData['inven']['armor'][0]['current_durability'])

                    battleData[idx] = [val.name_en, True, damage, False]

                else:
                    battleData[idx] = [val.name_en, False, 0, False]

        if animationStat:
            renpy.music.play("Body-Hit-08.mp3", channel='sound', loop=None, fadeout=0.3, synchro_start=False, fadein=0, tight=None, if_changed=False, relative_volume=1.0)
            # play sound "Body-Hit-03.mp3" fadeout 0.3
            renpy.with_statement(hpunch)

        # return battleData, debuff_lst
        return battleData


    # player's act: attack
    def player_attack(target, target_no):
        # result = copy.deepcopy(result_template)
        result = []

        # 시체를 때렸을 때
        if target.current_hp <= 0:
            # result = monster_dead(target.name_en)
            tempData = copy.deepcopy(result_template)
            tempData["copseFlag"] = True
            tempData["target"] = target_no
            reuslt.append(tempData)
        else:
            damage = cal_damage_test() # 플레이어의 최종 데미지

            # TODO: 스킬 추가 구현 필요 
            if playerData['skillPoint'] == 7:
                pass
            #     tempData = copy.deepcopy(result_template)
            #     tempData["skillFlag"] = True
            #     # skillTriggered = True
            #     playerData['skillPoint'] = 0
            #     playerData['inven']['weapon'][0]['current_durability'] -= 1

            #     result, damaged, transitionTarget_skill = skill(damage, target_no)
            #     transitionTarget += transitionTarget_skill

            #     if playerData['inven']['weapon'][0]['current_durability'] == 0:
            #         playerData['inven']['weapon'][0] = bare_hand_data["Bare Hand"]
            #         playerData['skillPoint'] = 0

            # 평타
            else:
                tempData = copy.deepcopy(result_template)
                tempData["attackFlag"] = cal_atkSuccess(playerData["dex"], playerData["lck"])
                # successFlag = cal_atkSuccess(playerData["dex"], playerData["lck"])
                # 평타 성공
                if tempData["attackFlag"]:
                    target.current_hp -= damage
                    tempData["target"] = target_no
                    tempData["damage"] = damage
                    # transitionTarget.append(target_no)
                    if target.current_hp <= 0:
                        target.current_hp = 0
                        tempData["downFlag"] = True

                        playerData['current_exp'] += target.exp

                    # expSys()

                    # if playerData['inven']['weapon'][0]['name'] != 'Bare Hand':
                    #     playerData['skillPoint'] += 1

                    #     if playerData['inven']['weapon'][0]['name'] == "Hammer":
                    #         damaged.append(target_no)


                    # if playerData['inven']['armor'][0]['name'] == "Berserk":
                    #     # get extra hp
                    #     playerData['current_hp'] += 3

                    #     if playerData['current_hp'] > playerData['max_hp']:
                    #         playerData['current_hp'] = playerData['max_hp']

                    result.append(tempData)
                    # result = AttackStatus.success
                    # renpy.call("event_PlayerAttackSuccess")

                # 평타 실패
                else:
                    tempData = copy.deepcopy(result_template)
                    tempData["target"] = target_no

                    # result = "missed"
                    # result = player_atk_failed()
                    result.append(tempData)
                    # renpy.say(None, "[temp]")
                    # renpy.call("event_PlayerAttackFailed")

        # return result, damaged, skillTriggered, set(transitionTarget)
        # return result, damaged, skillTriggered, set(transitionTarget)
        return result

    class AttackStatus(Enum):
        success = 0
        failed = 1