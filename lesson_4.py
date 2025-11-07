# # 1.
# lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# loreq = []
# mothen = []
# for i in lst:
#     if i <= 5:
#       loreq.append(i)
#     else:
#       if i > 5:
#         mothen.append(i)
# print(loreq)
# print(mothen)


# # 2.
# plus = input('Enter numbers and "+" operation to see result: ')
# lst = plus.split(' ')
# num = []
# for i in lst:
#     if i != '+':
#         num.append(int(i))
# res = sum(num)
# print(f'Sum = {res}')


# # 3.
# lst = input(f'Enter any list of numbers: ')
# lst2 = lst.split()
# num = []
# for i in lst2:
#     if int(i) > 0:
#         num.append(int(i))
# max_number = num[0]
# for n in num:
#     if n > max_number:
#         max_number = n
# len = (len(num))
# res = max_number / len
# print(f'result is: {res}')


# # 4.
# num = input(f'Enter numbers separated by comma ",": ')
# num2 = num.split(',')
# x = []
# for i in num2:
#         x.insert(0, i)
# print(x)


# # 5.
# lst = input(f'Enter score: ')
# score = lst.split()
#
# x = []
# for i in score:
#     if i == 'A+':
#        x.append(5.0)
#     elif i == 'A':
#         x.append(4.0)
#     elif i == 'A-':
#         x.append(3.7)
#     elif i == 'B+':
#         x.append(3.3)
#     elif i == 'B':
#         x.append(3.0)
#     elif i == 'B-':
#         x.append(2.7)
#     elif i == 'C+':
#         x.append(2.3)
#     elif i == 'C':
#         x.append(2.0)
#     elif i == 'C-':
#         x.append(1.7)
#     elif i == 'D+':
#         x.append(1.3)
#     elif i == 'D':
#         x.append(1.0)
#     elif i == 'F':
#         x.append(0)
# print(f'Total score: {sum(x)}')
# print(f'Average score: {(sum(x) / len(x)):.2f}')


# # 6.
# num = [1, 2, 3, 4, 5, 6, 7]
# x = []
# for i in num:
#     x.append(i * i)
# print(x)





