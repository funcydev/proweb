#
# for num in range(1, 11):
#     if num % 2 ==0:
#         continue
#     print(num)

# words = ["hello", "skip", "word", "python"]
# for word in words:
#     if word == "skip":
#         continue
#     print(word)

# data = [1, -1, 2, -2, 3, -3, 0]
# for num in data:
#     if num <=0:
#         continue
#     print(f' Vivod tolko polojitelnih chisel: {num}')

# cnt = 1
# while cnt <=6:
#     print(f'Counter equals: {cnt}')
#     cnt += 1

# user_input = ''
# while user_input.lower() != 'exit':
#     user_input = input(f'Enter command to quit: ')

# prod = ['apple', 'eggs', 'banana', 'tomato', 'candy']
# search = 'banana'
# found = False
# index = 0
#
# while index < len(prod) and not found:
#     if prod[index] == search:
#         found = True
#         print(f'Element {search} found on {index} position')
#     index += 1
# if not found:
#     print(f'Element {search} not found')

# while True:
#     user_iput = input('Enter stop command: ').lower()
#     if user_iput == 'stop':
#         break
# print(f'You have entered {user_iput} command')

# data = []
# while True:
#     item = get_new_data()
#     if not item:
#         continue
#     data.append(item)
#     if len(data) >= 100:
#         process_data(data)
#         data.clear()


# # 1.
# prod = ['apple', 'banana', 'eggs', 'sausages', 'strawberry', 'onion', 'bread']
# x = 0
# found = False
# search = 'banana'
# user_input = input(f'Enter command and argument: ').lower()
#
# while x <= len(prod):
#     if user_input == 'search':
#         print(f'Enter {} found')
#     x += 1
# if not found:
#     print(f'Element {search} not found')
#
#
#
# index = 0
#
# while index < len(prod) and not found:
#     if prod[index] == search:
#         found = True
#         print(f'Element {search} found on {index} position')
#     index += 1

# for value in range(1, 9):
#     print(value)

# squares = [value**2 for value in range(1,6)]
# print(squares)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[:3])

# lst = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# print('The first three items in the list are:')
# print(lst[:3])

# lst = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# print('Three items from the middle of the list are:')
# print(lst[1:4])

# lst = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# print('The last three items in the list are:')
# print(lst[-3:])
#
# my_lst = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# friend_lst = my_lst[:]
# my_lst.append('Americano')
# friend_lst.append('Coffe')
# print(my_lst)
# print(friend_lst)

# #1.
# prod = ['apple', 'banana', 'eggs', 'sausages', 'strawberry', 'onion', 'bread']
# while True:
#     user_input = input(f'Enter command and argument: ').lower()
#     if len(user_input.split(' ')) == 2:
#         command, product = user_input.split(' ')
#         if command == 'search' and product in prod:
#             print(f'product "{product}" in the list')
#         elif command == 'search' and product not in prod:
#             print(f'product "{product}" NOT in the list')
#         elif command == 'clear' and product in prod:
#             prod.remove(product)
#             print(f'Product "{product}" removed from list')
#             print(prod)
#         else:
#             print('Command or an argument not correct')
#     if user_input == 'stop':
#         break

# #2.
# n = int(input(f'Enter max number: '))
# for i in range(1, n + 1):
#     for x in range(i):
#         print(i, end=' ')
#     print()

# #3.
# i = input('Enter two positive numbers via space: ')
# y = []
# x = 1
# if len(i.split(' ')) == 2:
#     n, m = i.split(' ')
#     n = int(n)
#     m = int(m)
#     while x <= m:
#         if n % x == 0 and m % x == 0:
#             y.append(x)
#             x += 1
#         else:
#             x += 1
# print(max(y))

# # 4.
# summ = int(input('Enter summ: '))
# year = int(input('Enter annual period: '))
# percent = 10
# annual = (summ * (year * percent) / 100 + summ)
# print(f'Annual interest rate is 10% \nAfter {year} year(s) you get {annual} sum')

# #5.
# import random
# n = random.randint(1, 100)
# while True:
#     user_input = int(input('Guess the number: '))
#     if user_input < n:
#         print('Should be more')
#     elif user_input > n:
#         print('Should be less')
#     elif user_input == n:
#         print('You won!')
#         break

# #6.
# pas = '13579'
# i = 1
# while i <= 5:
#     up = input(f'Attempt {i} | Enter pass: ')
#     if up == pas:
#         print('Bingo!')
#         break
#     else:
#         print('Not correct')
#     i += 1

# #7.
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i % 5 == 0:
#         if i > 500:
#             break
#         elif i > 150:
#             continue
#         print(i)
