# 1.
from os import name

# person = {'name': 'John', 'city': 'New York'}
# print(person['name'])  # Выведет: John
# person['city_born']='Kabul'
# print(person.get('city_born','not mentioned'))
# # name = person.pop('name')
# print(name)
# # person.clear()
# print(person)
# for key, value in person.items():
#     print(f"Ключ: {key}, Значение: {value}")

# person = {'name': 'John', 'city': 'New York'}
# del person['name']
# shallow_copy = person.copy()
# print(person)
# print(shallow_copy)
#
# copy_dict = dict(person)
# print(copy_dict)
#
# import copy
# deep_copy = copy.deepcopy(person)
# print(deep_copy)

# person = {'name': 'John', 'city': 'New York'}
# person['city'] = 'Tashkent'
# person['age'] = 25
# print(person['city'])
# print(person.get('age'))
# for k in person:
#     print(k)
# for val in person.values():
#     print(val)
# for key, value in person.items():
#     print(f'{key} is {value}')
# for key, value in person.items():
#     if isinstance(value, int):
#         print(f'{key} : {value}')
# import copy
# person = {
#     'name': 'John',
#     'address': {'city': 'New York', 'state': 'NY', 'street': '5th ave'}
# }
#
# shallow_copy = person.copy()
# deep_copy = copy.deepcopy(person)
# person['address']['city'] = 'Tashkent'
# print(person)
# print(shallow_copy)
# print(deep_copy)

# squares = {x: x**2 for x in range(10)}
# print(squares)
#
# even_squares = {x: x**2 for x in range(10)if x % 2 == 0}
# print(even_squares)


cities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
#
# ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
# distances = {}
# moscow = cities['Moscow']
# london = cities['London']
# paris = cities['Paris']

print(cities['Moscow'])