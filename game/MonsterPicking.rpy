init python:
# 몬스터 목록 dictionary 형태로 변경
    def monster_table_init():
        result = {
            SectorData.sector_1.value: {
                TierData.common.value: {

                },
                TierData.uncommon.value: {

                },
                TierData.rare.value: {

                },
                TierData.epic.value: {

                }
            },
            SectorData.sector_2.value: {
                TierData.common.value: {

                },
                TierData.uncommon.value: {

                },
                TierData.rare.value: {

                },
                TierData.epic.value: {

                }
            },
            SectorData.sector_3.value: {
                TierData.common.value: {

                },
                TierData.uncommon.value: {

                },
                TierData.rare.value: {

                },
                TierData.epic.value: {

                }
            },
            SectorData.sector_4.value: {
                TierData.common.value: {

                },
                TierData.uncommon.value: {

                },
                TierData.rare.value: {

                },
                TierData.epic.value: {

                }
            },
            SectorData.sector_5.value: {
                TierData.common.value: {

                },
                TierData.uncommon.value: {

                },
                TierData.rare.value: {

                },
                TierData.epic.value: {

                }
            }
        }

        return result

    # 몬스터 정보 구조 정의
    def monster_parser(dataStructure, csvData):
        result = dataStructure

        for row in csvData:
            monster = Monster(
                index=row['Index'],
                m_type=row['Type'],
                name_kr=row['Name_KR'],
                name_en=row['Name_EN'],
                grade=row['Grade'],
                tier=row['Tier'],
                hp_max=row['HP_Max'],
                current_hp=row['HP_Max'],
                dmg=row['DMG'],
                stat_str=row['Stat_STR'],
                stat_dex=row['Stat_DEX'],
                stat_lck=row['Stat_LCK'],
                exp=row['Rew_EXP'],
                floor_num=row['Floor_Num'],
                type_color=row['Type_Color'],
                abnormal_condition_status_idx=row['Abnormal_Condition_Status_IDX']
            )

            if monster.floor_num == SectorData.sector_1.value:
                result[monster.floor_num][monster.tier][row['Index']] = monster
            elif monster.floor_num == SectorData.sector_2.value:
                result[monster.floor_num][monster.tier][row['Index']] = monster
            elif monster.floor_num == SectorData.sector_3.value:
                result[monster.floor_num][monster.tier][row['Index']] = monster
            elif monster.floor_num == SectorData.sector_4.value:
                result[monster.floor_num][monster.tier][row['Index']] = monster
            elif monster.floor_num == SectorData.sector_5.value:
                result[monster.floor_num][monster.tier][row['Index']] = monster

        return result

    # 몬스터 데이터 파일 읽고 몬스터 Table 구성하기
    def monster_loader(tier):
        F_CommonMonster = renpy.open_file(MonsterDataFile.monster_common.value, encoding='utf-8')
        F_UncommonMonster = renpy.open_file(MonsterDataFile.monster_uncommon.value, encoding='utf-8')
        F_RareMonster = renpy.open_file(MonsterDataFile.monster_rare.value, encoding='utf-8')
        F_EpicMonster = renpy.open_file(MonsterDataFile.monster_epic.value, encoding='utf-8')

        result = monster_table_init()

        if tier == 1:
            result = monster_parser(dataStructure=result, csvData=csv.DictReader(F_CommonMonster))
        elif tier == 2:
            result = monster_parser(dataStructure=result, csvData=csv.DictReader(F_UncommonMonster))
        elif tier == 3:
            result = monster_parser(dataStructure=result, csvData=csv.DictReader(F_RareMonster))
        elif tier == 4:
            result = monster_parser(dataStructure=result, csvData=csv.DictReader(F_EpicMonster))

        return result

    # 몬스터 등장 스테이지에 따른 분류
    def pick_sector(stage):
        sectors = ""
        if 1 <= stage <= 20:
            sectors = SectorData.sector_1.value
        elif 21 <= stage <= 40:
            sectors = SectorData.sector_2.value
        elif 41 <= stage <= 60:
            sectors = SectorData.sector_3.value
        elif 61 <= stage <= 80:
            sectors = SectorData.sector_4.value
        elif 81 <= stage <= 100:
            sectors = SectorData.sector_5.value
        return sectors

    # 몬스터 티어에 따른 분류
    def pick_tier(tier):
        tiers = ""
        if tier == 1:
            tiers = TierData.common.value
        elif tier == 2:
            tiers = TierData.uncommon.value
        elif tier == 3:
            tiers = TierData.rare.value
        elif tier == 4:
            tiers = TierData.epic.value
        return tiers


    def load_monster(gameData, stage):
        result = []
        cnt = random.choices([1, 2, 3, 5], weights=gameData["cntWeight"])[0]

        while len(result) < cnt:
            #data = copy.deepcopy(monster_loader())
            tier = random.choices([1, 2, 3, 4], weights=gameData["tierWeight"])[0]
            data = copy.deepcopy(monster_loader(tier))

            Monster_dict = data[pick_sector(stage)][pick_tier(tier)]
            Monster_index = random.choice(list(Monster_dict))

            result.append(Monster_dict[Monster_index])

        return result