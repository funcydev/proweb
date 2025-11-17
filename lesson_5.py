# # 1.
# import copy
# my_list = ['shashlik', 'plov', 'manti']
# friend_list = my_list.copy()
# my_list.append('fish')
# friend_list.append('beef')
# print(my_list)
# print(friend_list)


# # 2.
# user_num = int(input('Enter number: '))
# num = []
# for i in range(1, user_num + 1):
#     num.append(i)
# print(num)
# print(f'Sum of all numbers: {sum(num)}')

# # 3.
# num = 100
# odd = []
# not_odd = []
# for i in range(1, num + 1):
#     if i % 2 == 0:
#        odd.append(i)
#     else:
#         not_odd.append(i)
# print(odd)
# print(f'Sum of odd numbers: {sum(odd)}')
# print(not_odd)
# print(f'Sum of not odd numbers: {sum(not_odd)}')

# # 4.
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
# for i in numbers:
#     if i == 815:
#         break
#     if i % 2 == 0:
#         print(i)


# # 5.
# num = input('Enter any number: ')
# print(len(num))
