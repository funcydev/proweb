# 1.
# age = int(input('Enter your age: '))
# if age <= 18:
#     print('You have to study')
# elif age > 18 and age <= 50:
#     print('You have to work')
# elif age > 50 and age <= 59:
#     print('You are about pension age')
# elif age > 59 and age < 110:
#     print('You are on pension')
# else:
#     print('Incorrect age numbers, please try again')
from calendar import month

# 2.
# num1 = int(input('Enter 1st number: '))
# num2 = int(input('Enter 2nd number: '))
# num3 = int(input('Enter 3rd number: '))
# result = (num1 + num2 + num3) % 2
# if result == 0:
#     print('The sum of all your numbers is even')
# else:
#     print('The sum of all your numbers is odd')


# 3.
# num = int(input('Enter any number: '))
# result = num % 5
# if result == 0:
#     print('Hello')
# else:
#     print('Bye')


# 4.
# month = input('Enter name of month on english: ').lower()
# if month == 'december' or month == 'january' or month == 'february':
#     print('Provided month name included in Winter')
# elif month == 'march' or month == 'april' or month == 'may':
#     print('Provided month name included in Spring')
# elif month == 'june' or month == 'july' or month == 'august':
#     print('Provided month name included in Summer')
# elif month == 'september' or month == 'october' or month == 'november':
#     print('Provided month name included in Autumn')
# else:
#     print('month name is incorrect')


# 5.
# num1 = int(input('Enter 1st number: '))
# num2 = int(input('Enter 2nd number: '))
# num3 = int(input('Enter 3rd number: '))
# if num1 == num2 and num1 == num3 or num2 == num3 and num2 == num1 or num3 == num2 and num3 == num1:
#     print('Quantity of matching numbers: 3')
# elif num1 == num2 or num1 == num3 or num2 == num3:
#     print('Quantity of matching numbers: 2')
# else:
#     print('No matching numbers')

# 6.
# num1 = int(input('Enter 1st number: '))
# num2 = int(input('Enter 2nd number: '))
# result = num1 * num2
# if result < 1000:
#     print(result)
# else:
#     print(num1 + num2)

# 7.
# year = int(input('Enter year: '))
# result1 = year % 4
# result2 = year % 100
# result3 = year % 400
# print(result1, result2, result3)
# if result1 == 0 and result2 != 0 and result3 != 0:
#     print("It's a leap year")
# elif result1 == 0 and result2 == 0 and result3 != 0:
#     print("It's a non-leap year")
# elif result1 == 0 and result2 == 0 and result3 == 0:
#     print("It's a leap year")
# else:
#     print("It's a non-leap year")

# 8.
print('How many days are there in a leap year? \n'
                'a) 364 \n'
                'b) 365 \n'
                'c) 366 \n')
answer1 = input('Answer: ')

print('Which planet is closest to the Sun? \n'
                'a) Mercury \n'
                'b) Venus \n'
                'c) Mars \n')
answer2 = input('Answer: ')

print('Who wrote the novel War and Peace? \n'
                'a) Fyodor Dostoevsky \n'
                'b) Lev Tolstoy \n'
                'c) Alexander Pushkin \n')
answer3 = input('Answer: ')

print('How many sides does a regular hexagon have? \n'
                'a) 5 \n'
                'b) 6 \n'
                'c) 8 \n')
answer4 = input('Answer: ')

print('Which kind of gas do plants release during photosynthesis? \n'
                'a) Carbon dioxide \n'
                'b) Oxygen \n'
                'c) Nitrogen \n')
answer5 = input('Answer: ')

print('Which is the largest planet in the solar system? \n'
                'a) Saturn \n'
                'b) Jupiter \n'
                'c) Neptune \n')
answer6 = input('Answer: ')

print('Who invented the incandescent light bulb? \n'
                'a) Thomas Edison \n'
                'b) Alexander Bell \n'
                'c) Nikola Tesla \n')
answer7 = input('Answer: ')



