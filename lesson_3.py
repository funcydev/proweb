# Lists (mass)
from uaclient.files.notices import remove

# lst1 = []
# lst2 = list()  # sozdanie spiska na osnove klassa
# print(lst1)
# print(lst2)

# # indexes  0,      1,        2,       3
# prod = ['eggs', 'tomato', 'cheese', 10]
# # get index from list
# print(prod[0])
#
# # change value element by index
# prod[3] = 'onion'
# print(prod[3])
# indx = prod.index('cheese')
# print(indx)
# print(type(indx))
#
# # count lenght of lists and others
# length_list = len(prod)
# print(length_list)
# print(prod[0])
# print(prod[-2])
# print(prod[ len(prod) -1 ])

# Method adding elements into list
# friend = ['Alex', 'Salex', 'Bob', 'Martin']
# friend.append('Kyle')
# friend.append('Trump')
# # print(friend)
# #insert index into list by index number
# friend.insert(1, 'Lily')
# # print(friend)
#
# # method delete elements from list
# friend.remove('Bob')
# print(friend)
#
# # method delete elements from list by index
# friend.pop(2)
# print(friend)

# Sorting
# friend = ['Alex', 'Salex', 'Bob', 'Martin', 'Daniel']
# print(sorted(friend, reverse=True))   # function done this once
# print()
# friend.sort()                         # method done it once and forever
# print(friend)

# find elements in list
# friend = ['Alex', 'Salex', 'Bob', 'Martin', 'Daniel']
# name = input('Enter name to search it: ')
# if name in friend:
#     print(f'Name {name} exists in the list')
# else:
#     print(f'Name {name} not found in the list ')
#     addit = input(f'Want to add this name in the list? yes/no: ')
#     if addit == 'yes':
#         print('ok i will do it')
#         friend.append(name)
#         print(friend)
#     else:
#         print('ok bye')

# Create list from string

# word = 'Hello my dear friend'
# list_words  = word.split()
# print(list_words)
# print(list_words[3])
#
# num = input('Enter number separated by comma: ')
# print(num)
# list_num = num.split(',')
# print(list_num)
#
# new_num = ''.join(list_num)
# print(new_num)

# Cortage (also as a list)
lst = [1, 2, 3, 4]
lst.append(6)
print(lst)
lst2 = tuple(lst)
print(lst2)
print(lst2[2])