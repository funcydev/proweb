# #  Slovari dict()
# # also is type of data - associativniy massiv
#
# dict1 = {}          # sozdanie pustogo slovarya
# dict2 = dict()      # sozdanie pustogo slovarya na osnove classa
#
# print(dict1)
# print(dict2)
#
# contacts = {
#     # Key      # value
#      'mother': '+998998350199',
#      'Sister': 998998370199,
#     'brother': '998998410199',
#           102: 'Police'
# }
#
# print(contacts)
# # get value by key
# print(contacts['brother'])
#
# # Adding new key with value
# contacts['soulmate'] = 998998550199
# print(contacts)
#
# # Edit the value
# contacts[102] = 'musorskaya'
# print(contacts)
#
# # Delete key and value
# del contacts[102]           # Delete by command
# print(contacts )
#
# contacts.pop('brother')     # Delete by method
# print(contacts)
#


# human = {
#     'name': 'Ramil',
#     'lastname': 'Yunusov',
#     'age': 33,
#     'phone': '+998998190199',
#     'merried': True,
#     'friends': ['Bober', 'Solovey'],
#     'address': {
#         'city': 'Tashkent',
#         'street': 'S.Rahimov',
#         'home': 8
#     }
# }
#
# print(human)
# print(human.keys())     # Method to get keys from dict as a list
#
# for i in human:
#     print(i)

# print(human.values())     # Method to get values from dict as a list
# for i in human.values():
#     print(i)

# print(human.items())        # Method to get key and value from dictionary
# for k, v in human.items():
#     print(k, v)
#
# fixik = {
#     3: 'dedus',
#     2: 'simka',
#     1: 'nolik',
#     4: 'papus'
# }

# new_dict = {}
#
# for col, name in fixik.items():
#     print(col, name)
#     new_dict[name] = col
# print(new_dict)

# dict_num = {}
# for i in range(1, 6):
#     dict_num[str(i)] = f'Fixik № {i}'
# print(dict_num)
#
# dict_num2 = {str(i): f'Fixik № {i}' for i in range(1, 6)}
# print(dict_num2)
#
# new_dict = {name: col for col, name in fixik.items()}
# print(new_dict)

# Vlojennost
# Dictionary of the dictionary
# Dictionary with list in values

# students = [
#     # 1 student
#     {
#              'name': 'Ramil',
#         'last_name': 'Yunusov',
#               'age':  39,
#           'friends': ['Lola', 'Pola', 'Sola'],
#             'marks': {
#                    'math': 5,
#                 'history': 4,
#                   'chemy': 3
#             }
#
#     },
#     # 2 student
#     {
#              'name': 'Petr',
#         'last_name': 'Petrenko',
#               'age':  22,
#           'friends': ['Lola', 'Pola', 'Sola'],
#             'marks': {
#                    'math': 2,
#                 'history': 2,
#                   'chemy': 3
#             }
#     },
#     # 3 student
#     {
#              'name': 'Bobr',
#         'last_name': 'Bobrenko',
#               'age':  32,
#           'friends': ['Lola', 'Pola', 'Sola'],
#             'marks': {
#                    'math': 4,
#                 'history': 3,
#                   'chemy': 5
#             }
#     }
# ]
#
# print(students)
#
# total = 0
# for stud in students:
#     # total += stud['marks']['math']
#     # total += stud['marks']['history']
#     # total += stud['marks']['chemy']
#     total += sum(stud['marks'].values())
# print(total)
#
# average = total / len(students) / len(students[0]['marks'])
# print(round(average, 1))