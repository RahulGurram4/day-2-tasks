# Bitwise Operator Tasks (1–8)

p,q = 10,6
print(p & q)

m,n = 12,5
print(m | n)

number = 8
print(~number)

a,b = 15,9
print(a ^ b)

value = 7
print(value << 2)

value = 20
print(value >> 1)

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(f'AND Output : {num1 & num2}')
print(f'XOR Output : {num1 ^ num2}')

#-------------------------------------------------------------------

# String Tasks (9–14)

word = 'hi'
print((word + ' ') * 4)

language = 'python'
print(language, language, language)

s1 = 'super'
s2 = 'hero'
print(s1 + s2)

str_a = 'hello'
space = ' '
str_b = 'world'
print(str_a + space + str_b)

name = input('Type your name: ') + ' '
print(name * 5)

first = input('Enter first string: ')
second = input('Enter second string: ')
print(first + ' ' + second)

#-------------------------------------------------------------------

# Input & Type Casting Tasks (15–20)

username = input('Enter your name: ')
print(type(username))

age = input('Enter your age: ')
age = int(age)
print(age, type(age))

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(f'Total Sum : {num1 + num2}')

m1 = int(input('Enter first mark: '))
m2 = int(input('Enter second mark: '))
print(f'Average Marks : {(m1 + m2)/2}')

x = int(input('Enter number1: '))
y = int(input('Enter number2: '))
print(3*x*2 + y - 2)

num = input('Enter a number: ')
print('Before conversion:', type(num))
num = int(num)
print('After conversion:', type(num))

# -------------------------------------------------------------------

# Unit Digit Tasks (21–25)

num = input('Enter a number: ')
print(num[len(num) - 1])

num = int(input('Enter a number: '))
print(num % 10)

num = int(input('Enter a number: '))
print(num // 10)

num = input('Enter a number: ')
print(num[len(num) - 2])

five_digit = 67893
print(five_digit % 10)

#-------------------------------------------------------------------

# If Statement Tasks (26–30)

if 10 >= 5:
    print('Condition True')
else:
    print('Condition False')
    
num = int(input('Enter a number: '))
if num > 50:
    print(f'{num} is greater than 50')
elif num == 50:
    print(f'{num} equals 50')
else:
    print(f'{num} is less than 50')

age = int(input('Enter your age: '))
if age >= 18:
    print('You are an adult')
else:
    print('You are under 18')
    
number = 101
print(True if number >= 100 else False)

value = 4
print(True if number >= 0 else False)

#-------------------------------------------------------------------

# If-Else Tasks (31–34)

num = 77
if num % 2 == 0:
    print('Even Number')
else:
    print('Odd Number')

marks = int(input('Enter your marks: '))
print('Pass' if marks >= 35 else 'Fail')

num = -6
print('Negative Number' if num < 0 else 'Positive Number')

number = 30
print('Greater than 10' if number > 10 else 'Less than or equal to 10')

#-------------------------------------------------------------------

# Nested If Tasks (35–37)

age = int(input("Enter Age: "))
height = int(input("Enter Height in cm: "))
weight = int(input("Enter Weight in kg: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected : All requirements met")
        else:
            print("Rejected : Weight is too low")
    else:
        print("Rejected : Height is too low")
else:
    print("Rejected : Age below requirement")


marks = int(input("Enter your Marks percentage: "))
age = int(input("Enter your Age: "))

if marks >= 60:
    if age >= 17:
        print("You are eligible for admission.")
    else:
        print("Rejected: Age must be at least 17.")
else:
    print("Rejected: Minimum 60% marks needed.")


age = int(input("Enter Age: "))
height = float(input("Enter Height (cm): "))
weight = float(input("Enter Weight (kg): "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected for the Team!")
        else:
            print("Rejected (Weight should be at least 50kg)")
    else:
        print("Rejected (Height should be at least 150cm)")
else:
    print("Rejected (Age should be at least 16)")

#-------------------------------------------------------------------

# Match Statement Tasks (38–40)

day = int(input("Enter day number (1-7): "))

match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid day number")

color = int(input('Choose a number from 1 to 3: '))

match color:
    case 1: print('Red')
    case 2: print('Blue')
    case 3: print('Green')
    case _: print("Color not available")

fruit = int(input("Enter fruit id (1-4): "))

match fruit:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
    case _:
        print("Fruit not available")