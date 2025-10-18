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
# Correct answers: 1) c, 2) a, 3) b, 4) b, 5) b, 6) b, 7) a, 8) a, 9) b, 10) a
# print('1. How many days are there in a leap year? \n'
#                 'a: 364 \n'
#                 'b: 365 \n'
#                 'c: 366')
# answer1 = input('Answer: ').lower()
# if answer1 == 'c':
#     result1 = 1
#     print('Correct!\n')
# else:
#     result1 = 0
#     print(f'Incorrect!\n')
#
# print('2. Which planet is closest to the Sun? \n'
#                 'a: Mercury \n'
#                 'b: Venus \n'
#                 'c: Mars')
# answer2 = input('Answer: ').lower()
# if answer2 == 'a':
#     result2 = 1
#     print('Correct!\n')
# else:
#     result2 = 0
#     print(f'Incorrect!\n')
#
# print('3. Who wrote the novel War and Peace? \n'
#                 'a: Fyodor Dostoevsky \n'
#                 'b: Lev Tolstoy \n'
#                 'c: Alexander Pushkin')
# answer3 = input('Answer: ').lower()
# if answer3 == 'b':
#     result3 = 1
#     print('Correct!\n')
# else:
#     result3 = 0
#     print(f'Incorrect!\n')
#
# print('4. How many sides does a regular hexagon have? \n'
#                 'a: 5 \n'
#                 'b: 6 \n'
#                 'c: 8')
# answer4 = input('Answer: ').lower()
# if answer4 == 'b':
#     result4 = 1
#     print('Correct!\n')
# else:
#     result4 = 0
#     print(f'Incorrect!\n')
#
# print('5. Which kind of gas do plants release during photosynthesis? \n'
#                 'a: Carbon dioxide \n'
#                 'b: Oxygen \n'
#                 'c: Nitrogen')
# answer5 = input('Answer: ').lower()
# if answer5 == 'b':
#     result5 = 1
#     print('Correct!\n')
# else:
#     result5 = 0
#     print(f'Incorrect!\n')
#
# print('6. Which is the largest planet in the solar system? \n'
#                 'a: Saturn \n'
#                 'b: Jupiter \n'
#                 'c: Neptune')
# answer6 = input('Answer: ').lower()
# if answer6 == 'b':
#     result6 = 1
#     print('Correct!\n')
# else:
#     result6 = 0
#     print(f'Incorrect!\n')
#
# print('7. Who invented the incandescent light bulb? \n'
#                 'a: Thomas Edison \n'
#                 'b: Alexander Bell \n'
#                 'c: Nikola Tesla')
# answer7 = input('Answer: ').lower()
# if answer7 == 'a':
#     result7 = 1
#     print('Correct!\n')
# else:
#     result7 = 0
#     print(f'Incorrect!\n')
#
# print('8. What is the name of the capital of Japan? \n'
#                 'a: Tokyo \n'
#                 'b: Kyoto \n'
#                 'c: Osaka')
# answer8 = input('Answer: ').lower()
# if answer8 == 'a':
#     result8 = 1
#     print('Correct!\n')
# else:
#     result8 = 0
#     print(f'Incorrect\n!')
#
# print('9. How many degrees are in a right angle? \n'
#                 'a: 45 \n'
#                 'b: 90 \n'
#                 'c: 180')
# answer9 = input('Answer: ').lower()
# if answer9 == 'b':
#     result9 = 1
#     print('Correct!\n')
# else:
#     result9 = 0
#     print(f'Incorrect!\n')
#
# print('10. Which bird is a symbol of peace? \n'
#                 'a: Pigeon \n'
#                 'b: Eagle \n'
#                 'c: Swallow')
# answer10 = input('Answer: ').lower()
# if answer10 == 'a':
#     result10 = 1
#     print('Correct!\n')
# else:
#     result10 = 0
#     print(f'Incorrect!\n')
#
# print(f'Your total score is: {result1 + result2 + result3 + result4 + result5 + result6 + result7 + result8 + result9 + result10} from 10')


# 9.
# rate1 = 5.0; rate2 = 4.0; rate3 = 3.7; rate4 = 3.3; rate5 = 3.0; rate6 = 2.7; rate7 = 2.3; rate8 = 2.0; rate9 = 1.7; rate10 = 1.3; rate11 = 1.0; rate12 = 0
#
# letter = input('Enter rate: ')
# if letter == 'A+':
#     print(rate1)
# elif letter == 'A':
#     print(rate2)
# elif letter == 'A-':
#     print(rate3)
# elif letter == 'B+':
#     print(rate4)
# elif letter == 'B':
#     print(rate5)
# elif letter == 'B-':
#     print(rate6)
# elif letter == 'C+':
#     print(rate7)
# elif letter == 'C':
#     print(rate8)
# elif letter == 'C-':
#     print(rate9)
# elif letter == 'D+':
#     print(rate10)
# elif letter == 'D':
#     print(rate11)
# elif letter == 'F':
#     print(rate12)
# else:
#     print('Incorrect input, make sure to use capitalized letter')