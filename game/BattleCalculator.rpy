init python:
    # calculate event success
    def cal_success(lck: int) -> bool:
        tot_lck = playerData['lck'] + playerData['inven']['weapon'][0]['lck'] + playerData['inven']['armor'][0]['lck']
        return random.choices([True, False], weights=[(tot_lck * 5), 100 - (tot_lck * 5)])[0]

    # calculate attack success
    def cal_atkSuccess(dex: int, lck: int) -> bool:
        tot_dex = playerData['dex'] + playerData['inven']['weapon'][0]['dex'] + playerData['inven']['armor'][0]['dex']
        tot_lck = playerData['lck'] + playerData['inven']['weapon'][0]['lck'] + playerData['inven']['armor'][0]['lck']
        return random.choices([True, False], weights=[(50 + tot_dex + tot_lck), 100 - (50 + tot_dex + tot_lck)])[0]

    def cal_atkSuccess_mon(dex: int, lck: int) -> bool:
        return random.choices([True, False], weights=[(50 + dex + lck), 100 - (50 + dex + lck)])[0]

    # calculate dodge success
    def cal_runSuccess(dex: int, lck: int) -> bool:
        tot_dex = playerData['dex'] + playerData['inven']['weapon'][0]['dex'] + playerData['inven']['armor'][0]['dex']
        tot_lck = playerData['lck'] + playerData['inven']['weapon'][0]['lck'] + playerData['inven']['armor'][0]['lck']

        if gameVariable['stage'] >= 70:
            return random.choices([True, False], weights=[10, 90])[0]
        else:
            return random.choices([True, False], weights=[(50 + tot_dex + tot_lck)/2, 100 - ((50 + tot_dex + tot_lck)/2)])[0]

    # calculate actual damage
    def cal_damage(str: int, dmg: int) -> float:
        tot_dmg = playerData['dmg'] + playerData['inven']['weapon'][0]['dmg'] + playerData['inven']['armor'][0]['dmg']
        tot_str = playerData['str'] + playerData['inven']['weapon'][0]['str'] + playerData['inven']['armor'][0]['str']
        return int(math.ceil((tot_str / 2) * (tot_dmg / 3 * 2)))

    def cal_damage_mon(str: int, dmg: int) -> float:
        return int(math.ceil((str / 2) * (dmg / 3 * 2)))

    # 데미지 공식 테스트, 후긴을 죽이면 내가 주는 데미지가 2배 늘어난다.
    def cal_damage_test() -> float:
        # return int(math.ceil((str / 2) + (dmg / 3 * 2)))
        tot_dmg = playerData['dmg'] + playerData['inven']['weapon'][0]['dmg'] + playerData['inven']['armor'][0]['dmg']
        tot_str = playerData['str'] + playerData['inven']['weapon'][0]['str'] + playerData['inven']['armor'][0]['str']

        # if gameVariable["huginnMainDead"]:
        #     return int(math.ceil((tot_str / 2) * (tot_dmg / 3)))
        # else:
        #     return int(math.ceil((tot_str / 2) + (tot_dmg / 3 * 2)))
        return int(math.ceil((tot_str / 2) + (tot_dmg / 3)))