# For Variable State
init python:
    from enum import Enum

    class HealState(Enum):
        Max = 1
        Heal = 2

    class BannerState(Enum):
        Door = 1
        Battle = 2
        Chest = 3
        Chest_empty = 4
        Chest_full = 5
        Grace = 6
        Maintenance = 7
        Mimic = 8
        Dead_normal = 9
        Dead_berserk = 10
        Dead_wound = 11
        Huginn = 12
        Muninn = 13

    class GameState(Enum):
        Normal = 1
        Battle = 2
        Looting = 3
        Swap = 4
        Opening = 5
        Chest = 6
        Abyss = 7
        Midlevel = 8

    class SayState(Enum):
        Normal = 1
        CutScene = 2

    class EquipmentCategory(Enum):
        Armor = "Armor"
        Weapon = "Weapon"
        Non = "None"
    
    class ColorState(Enum):
        White = "White"
        Blue = "Blue"
        Purple = "Purple"

    class DebuffState(Enum):
        Damaged = 1
        DamagedAndCure = 2
        Break = 3
        BreakAndCure = 4
        NonEffect = 5

    # class AnimationState(Enum):
    #     None = 1
    #     isHuginnDead = 2

# For Visual

init python:
    from enum import Enum
    
    class Colors(Enum):
        Red_crimson = "#CC0033"
        Gray_light = "#858583"
        Gray_charcoal = "#2c2c2c"
        Gray_middle_dimming = "#8888887f"
        Blue_icy = "#add8e6"
        White = "#ffffff"
        Blue = "#1E90FF"
        Purple = "#a020f0"
        Yellow_saffron = "#F4C430"
        Black_dimming = "#00000075"
        Black_dimming_bold = "#00000088"
        Black = "#000000"
        Teal = "#407082"
        Apricot = "#D68478"
        
