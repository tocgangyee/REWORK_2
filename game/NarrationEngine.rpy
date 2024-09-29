init python:
    def has_coda(word):
        return (ord(word[-1]) - 44032) % 28 == 0

    def add_postposition1(word):
        '''이/가'''
        if preferences.language == "korean":
            return word + ("가" if has_coda(word) else "이")
        else:
            return word

    def add_postposition2(word):
        '''을/를'''
        if preferences.language == 'korean':
            return word + ("를" if has_coda(word) else "을")
        else:
            return word

    def add_postposition3(word):
        '''은/는'''
        if preferences.language == 'korean':
            return word + ("는" if has_coda(word) else "은")
        else:
            return word

    # def localized_name(target):
    #     if preferences_language == 'korean':
    #         tl_set = {
    #             "Bare Hand": "맨손",
    #             "Sword": "검",
    #             "Hammer": "해머",
    #             "Dagger": "대거",
    #             "PlateArmor": "판금갑옷",
    #             "Chainmail": "체인메일",
    #             "WingShoes": "윙슈즈",
    #             "Berserk": "버서커",
    #             "MagicRobe": "마법망토",
    #             "Tunic": "튜닉",
    #             "Skeleton": "스켈레톤",
    #             "Rabbit": "토끼",
    #             "Spider": "거미",
    #             "Turkey": "칠면조",
    #             "Hellhound": "헬하운드",
    #             "Toad": "두꺼비",
    #             "Wraith": "레이스",
    #             "Ghoul": "구울",
    #             "Werewolf": "웨어울프",
    #             "Dullahan": "듀라한",
    #             "Lich": "리치",
    #             "Ripper": "리퍼",
    #             "Huginn": "후긴",
    #             "Muninn": "무닌",
    #             "cureent_hp": "체력",
    #             "str": "힘",
    #             "dmg": "파괴력",
    #             "dex": "민첩",
    #             "lck": "운",
    #             "current_durability": "내구도"
    #         }

    #         return tl_set[target]
    #     else:
    #         return target

    # def translation_name(item_name, language):
    #     translations = {
    #         "Bare Hand": {
    #             "korean": "맨손",
    #         },
    #         "Sword": {
    #             "korean": "검",
    #         },
    #         "Hammer": {
    #             "korean": "해머",
    #         },
    #         "Dagger": {
    #             "korean": "대거",
    #         },
    #         "PlateArmor": {
    #             "korean": "판금갑옷",
    #         },
    #         "Chainmail": {
    #             "korean": "체인메일",
    #         },
    #         "WingShoes": {
    #             "korean": "윙슈즈",
    #         },
    #         "Berserk": {
    #             "korean": "버서커",
    #         },
    #         "MagicRobe": {
    #             "korean": "마법망토",
    #         },
    #         "Tunic": {
    #             "korean": "튜닉"
    #         },
    #         "Skeleton": {
    #             "korean": "스켈레톤",
    #         },
    #         "Rabbit": {
    #             "korean": "토끼",
    #         },
    #         "Spider": {
    #             "korean": "거미",
    #         },
    #         "Turkey": {
    #             "korean": "칠면조",
    #         },
    #         "Hellhound": {
    #             "korean": "헬하운드",
    #         },
    #         "Toad": {
    #             "korean": "두꺼비",
    #         },
    #         "Wraith": {
    #             "korean": "레이스",
    #         },
    #         "Ghoul": {
    #             "korean": "구울",
    #         },
    #         "Werewolf": {
    #             "korean": "웨어울프",
    #         },
    #         "Dullahan": {
    #             "korean": "듀라한",
    #         },
    #         "Lich": {
    #             "korean": "리치",
    #         },
    #         "Ripper": {
    #             "korean": "리퍼",
    #         },
    #         "Huginn": {
    #             "korean": "후긴",
    #         },
    #         "Muninn": {
    #             "korean": "무닌",
    #         },
    #         "cureent_hp": {
    #             "korean": "체력"
    #         },
    #         "str": {
    #             "korean": "힘"
    #         },
    #         "dmg": {
    #             "korean": "파괴력"
    #         },
    #         "dex": {
    #             "korean": "민첩"
    #         },
    #         "lck": {
    #             "korean": "운"
    #         },
    #         "current_durability": {
    #             "korean": "내구도"
    #         }
    #     }

    #     return translations.get(item_name, {}).get(language, item_name)