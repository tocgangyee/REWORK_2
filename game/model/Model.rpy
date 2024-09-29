init python:
    from enum import Enum

    class Monster:
        def __init__(self, index, m_type, name_kr, name_en, grade, tier, hp_max, current_hp, dmg, stat_str, stat_dex, stat_lck, exp, floor_num, type_color, abnormal_condition_status_idx):
            self.index = index
            self.type = m_type
            self.name_kr = name_kr
            self.name_en = name_en
            self.grade = grade
            self.tier = tier
            self.hp_max = int(hp_max)
            self.current_hp = int(hp_max)
            self.dmg = int(dmg)
            self.stat_str = int(stat_str)
            self.stat_dex = int(stat_dex)
            self.stat_lck = int(stat_lck)
            self.exp = int(exp)
            self.floor_num = floor_num
            self.type_color = type_color
            self.abnormal = abnormal_condition_status_idx
    
    class MonsterDataFile(Enum):
        monster_common = "data/Common_Monster_Table.csv"
        monster_uncommon = "data/Uncommon_Monster_Table.csv"
        monster_rare = "data/Rare_Monster_Table.csv"
        monster_epic = "data/Epic_Monster_Table.csv"
    
    class TempFile(Enum):
        monster_unique = "data/Unique_Monster_DataTable-Table.csv"
        monster_boss = "data/Boss_Monster_DataTable-Table.csv"

    class GameDataFile(Enum):
        abnormal_condition = "data/Abnormal_Condition_Status_Table.csv"

    class SectorData(Enum):
        sector_1 = "1 ~ 20"
        sector_2 = "21 ~ 40"
        sector_3 = "41 ~ 60"
        sector_4 = "61 ~ 80"
        sector_5 = "81 ~ 100"

    class TierData(Enum):
        common = "1"
        uncommon = "2"
        rare = "3"
        epic = "4"