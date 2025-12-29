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
