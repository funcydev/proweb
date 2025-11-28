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


prod = ['apple', 'banana', 'eggs', 'sausages', 'strawberry', 'onion', 'bread']

user_input = input(f'Enter command and argument: ').lower()
# if len(user_input.split(' ')) == 2:
#     command, product = user_input.split(' ')
#     if command == 'search' and product in prod:
#         print(f'product {product} in the list')
#     else:
#         print(f'product {product} NOT in the list')
if len(user_input.split(' ')) == 2:
    command, product = user_input.split(' ')
    if command == 'clear' and product in prod:
        print(product)
        prod.clear(prod)
        print(prod)



