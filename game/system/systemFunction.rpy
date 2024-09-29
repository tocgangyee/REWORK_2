init python:
    def get_name_by_index(monsters_dict, index):
        monster = monsters_dict[index]
        if monster:
            return monster.name_en
        return None

    def get_key_from_enum(value, targetData):
        for target in targetData:
            if target.value == value:
                return target.name
        return None