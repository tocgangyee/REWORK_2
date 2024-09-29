# import json
# import random
# import renpy
# # import Module.Error as Error
# # import pygame.image as pgimage

# # Module: json read
# def load_json(path):
#     with open(path, 'r') as temp:
#             return json.load(renpy.file(temp))
#     # try:
#     #     with open(path, 'r') as temp:
#     #         return json.load(temp)
#     # except:
#     #     raise Error.DataLoadFailedError

# # Module: json write
# def save_json(path, data):
#     with open(path,'w') as outfile:
#             json.dump(data, outfile, indent='\t')
#     # try:
#     #     with open(path,'w') as outfile:
#     #         json.dump(data, outfile, indent='\t')
#     # except:
#         # raise Error.DataWriteFailedError

# def load_c_data():
#     path = "Data/Client_data.json"
#     data = load_json(path)

#     return data['Language']

# def update_c_data(newData: str):
#     path = "Data/Client_data.json"
#     data = load_json(path)

#     data['Language'] = newData

#     save_json(path, data)

# # Module: load Game_weight.json
# def load_weight():
#     path = "Data/Game_weight.json"
#     data = load_json(path)

#     return data["monster_tier"], data["equipment_tier"], data["potion_tier"], data['monster_cntweight']

# # Module: pick monster with Monster.json via algorithm

# def monster_character(type, monster, stage):
#     if stage <= 40:
#         monster['suffix'] = ""
#     else:
#         monster['suffix'] = type
#         if type == "Normal":
#             monster['suffix'] = ""
#         elif type == "Wounded":
#             monster['current_hp'] //= 2
#             monster['dmg'] += 4
#         elif type == "Poisoned":
#             monster['current_hp'] = 10
#         elif type == "Lazy":
#             monster['max_hp'] += 10
#             monster['current_hp'] += 10
#             monster['dex'] -= 40
#         elif type == "Swifty":
#             pass
#         elif type == "Sensitive":
#             monster['dex'] += 10
#         elif type == "Madness":
#             monster['max_hp'] *= 2
#             monster['current_hp'] *= 2
#             monster['str'] *= 2
#             monster['dmg'] *= 2

#     # character에 따른 경험치 추가 배분 필요

#     return monster

# def load_monster(weight, cntweight, stage):
#     result = []
#     cnt = random.choices([1,2,3], weights=cntweight)[0]
#     charc_lst = ["Normal", "Wounded", "Poisoned", "Lazy", "Swifty", "Sensitive", "Madness"]
#     charc_weight = [100, 60, 60, 60, 60, 60, 0.1]
#     huginn_muninn_check = False

#     while len(result) < cnt:
#         path = "Data/Monster.json"
#         data = load_json(path)

#         tier = list(data.keys())
#         tier = random.choices(tier, weights=weight)[0]
#         monster = random.choice(data[tier])

#         if huginn_muninn_check:
#             while monster['name'] == 'Huginn' or monster['name'] == 'Muninn':
#                 monster = random.choice(data[tier])

#         if monster['name'] == 'Huginn' or monster['name'] == 'Muninn':
#             huginn_muninn_check = True

#         type = random.choices(charc_lst, weights=charc_weight)[0]
#         result.append(monster_character(type, monster, stage))

#     return result

# # Module: pick equipment with Monster.json via algorithm
# def load_equipment(weight):
#     path = "Data/Equipment.json"
#     data = load_json(path)
#     result = []

#     tier = list(data.keys())
#     tier = random.choices(tier, weights=weight)[0]
#     result.append(random.choice(data[tier]))

#     return result[0]

# # Module: pick potion with Monster.json via algorithm
# def load_potion(weight):
#     path = "Data/Potion.json"
#     data = load_json(path)

#     tier = list(data.keys())
#     tier = random.choices(tier, weights=weight)[0]
#     rarity = []

#     for val in data[tier]:
#         rarity.append(val['rare'])

#     result = random.choices(data[tier], weights=rarity)[0]

#     return result

# # Module: load Player.json
# def load_player():
#     path = "data/Player.json"
#     data = load_json(path)
#     return data

# # def load_Icons():
# #     path = 'Data/Assets.json'
# #     data = load_json(path)['icons']
# #     result = {}

# #     for val in data.keys():
# #         result[val] = pgimage.load(data[val])

# #     return result

# # def load_BGs():
# #     path = 'Data/Assets.json'
# #     data = load_json(path)['bgs']
# #     result = {}

# #     for val in data.keys():
# #         result[val] = pgimage.load(data[val])

# #     return result

# # def load_IMGs():
# #     path = 'Data/Assets.json'
# #     data = load_json(path)['images']
# #     result = {}

# #     for val in data.keys():
# #         result[val] = pgimage.load(data[val])

# #     return result

# # def load_Banners():
# #     path = 'Data/Assets.json'
# #     data = load_json(path)['banners']
# #     result = {}

# #     for val in data.keys():
# #         result[val] = pgimage.load(data[val]).convert_alpha()

# #     return result

# # def load_Fonts():
# #     path = 'Data/Assets.json'
# #     data = load_json(path)['fonts']

# #     path = 'Data/Fonts.json'
# #     sizeData = load_json(path)

# #     return data, sizeData

# # def load_Colors():
# #     path = 'Data/Colors.json'
# #     data = load_json(path)

# #     return data

# # def load_Tutorial():
# #     result = {}
# #     path = 'Assets/Tutorial/'

# #     for idx in range(20):
# #         result[idx] = pgimage.load(path + str(idx) + '.png')

# #     return result