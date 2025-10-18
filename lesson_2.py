# 1.
age = int(input('Enter your age: '))
if age <= 18:
    print('You have to study')
elif age > 18 and age <= 50:
    print('You have to work')
elif age > 50 and age <= 59:
    print('You are about pension age')
elif age > 59 and age < 110:
    print('You are on pension')
else:
    print('Incorrect age numbers, please try again')