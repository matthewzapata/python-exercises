# Conditional Basics

# prompt user for a day of the week and print whether the day is Monday or not

day_of_the_week = input('What day is it? ')

if day_of_the_week == 'Monday':
    print('Today is Monday.')
else:
    print('Today is not Monday.')
print('----------------------------------------------')
# prompt for day of the week, print whether the day is a weekday or weekend
day_of_the_week = input('What day is it? ')

if day_of_the_week.lower().startswith('s'):
    print('It is the weekend!')
else:
    print('It is a weekday.')

print('----------------------------------------------')
# create variables and make up values for: hours worked, hourly rate, and the week's paycheck
# write code that calculates the weekly paycheck
# over 40 hours is time and a half

hours_worked = int(input('How many hours did you work this week? '))
hourly_rate = int(input('And what is your hourly wage? '))

if hours_worked <= 40:
    paycheck_for_week = hours_worked * hourly_rate
else:
    overtime_hours = hours_worked - 40
    overtime_rate = hourly_rate * 1.5
    nonovertime_hours = hours_worked - overtime_hours

    paycheck_for_week = (nonovertime_hours * hourly_rate) + (overtime_hours * overtime_rate)

print(f'You will be getting paid ${paycheck_for_week} for this week!')

print('----------------------------------------------')
# Loop Basics

# While Loops

# create an integer variable with a value of 5
# create a while loop that runs so long as i is less than or equal to 15
# for each loop iteration, print current i then increment i by one

i = 5
while i <= 15:
    print(i)
    i += 1

print('----------------------------------------------')

# create a while loop that will count by 2's starting with 0 and ending at 100.
# Follow each number with a new line.

i = 0
while i < 101:
    print(i)
    i += 2

print('----------------------------------------------')

# alter your loop to count backwards by 5's from 100 to -10

i = 100
while i >= -10:
    print(i)
    i -= 5

print('----------------------------------------------')

# create a while loop that starts at 2 and displays the number squared on
# each line while the number is less than 1,000,000

i = 2
while i < 1_000_000:
    print(i)
    i = i ** 2

print('----------------------------------------------')

# write a loop that uses print to create the output

i = 100
while i >= 5:
    print(i)
    i -= 5

print('----------------------------------------------')

# For Loops

# write code that prompts the user for a number, then shows a
# multiplication table up through 10 for that number

their_number = int(input('What number do you want to see a multiplication table for? '))
for i in range(1, 11):
    print(f'{their_number} x {i} = {their_number * i}')

print('----------------------------------------------')

# create a for loop that uses print to create the output

for n in range (1,10):
    print(str(n) * n)

print('----------------------------------------------')
    
# break and continue

# prompt user for an odd number between 1 and 50. use a loop and break statement to continue
# prompting the user if they enter invalid input.

print('I will count all the odd numbers from 1 to 50 except for the number you tell me to skip.')
skip_this_number = input('What odd number should I skip? ')

while not skip_this_number.isdigit() or int(skip_this_number) < 1 or int(skip_this_number) > 50 or int(skip_this_number) % 2 == 0:
    print('That is either not an odd number or isn\'t between 1 and 50.')
    skip_this_number = input('Enter another number to skip: ')

print(f'Number to skip is: {skip_this_number}')
for i in range (1, 50):
    if i == int(skip_this_number):
        print(f'Yikes! Skipping number: {skip_this_number}') 
        continue
    elif i % 2 != 0:
        print(f'Here is an odd number: {i}')

print('----------------------------------------------')

# prompt the user to enter a positive number and write a loop that counts from 0 to that number.
# make sure the value entered is a valid number

user_number = input('Please choose a positive number to count to: ')

while not user_number.isdigit() or int(user_number) < 1:
    print('Excuse me, I asked for a positive number! Let\'s try that again. ')
    user_number = input('Please choose a positive number: ')

for i in range(0, (int(user_number) + 1)):
    print(i)

print('----------------------------------------------')

# write a program that prompts the user for a positive integer.
# next write a loop that prints out the numbers from the number the user entered down to 1

user_number = input('Please choose a positive number to countdown from: ')

while not user_number.isdigit() or int(user_number) < 1:
    print('Excuse me, I asked for a positive number! Let\'s try that again. ')
    user_number = input('Please choose a positive number: ')

user_number = int(user_number)
while user_number >= 1:
    print(user_number)
    user_number -= 1

print('----------------------------------------------')

# Fizzbuzz
# write a program that prints the numbers from 1 to 100
# for multiples of three print "Fizz"
# for multiples of five print "Buzz"
# for numbers that are multiples of both three and five print "FizzBuzz"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        continue
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

print('----------------------------------------------')

# Display a table of powers.
# prompt the user to enter an integer
# display a table of squares and cubes from 1 to the value entered
# ask if the user wants to continue
# assume that the user will enter valid data
# only continue if the user agrees to

print('I will display a table of squares and cubes up to a number you specify.')

agree_to_continue = 'yes'
while agree_to_continue == 'yes':
    users_integer = int(input('What number would you like to go up to? '))
    print("Here is your table!")
    print('number  |  squared  |  cubed ')
    print('------  |  ------   |  ------')
    for i in range (1, (users_integer + 1)):
        print(f'{i}       | {i ** 2}         | {i ** 3}')
    agree_to_continue = input('Do you want to choose a different number? ')

print('----------------------------------------------')

# Convert given number grades into letter grades
# prompt the user for a numerical grade from 0 to 100
# display the corresponding letter grade
# prompt the user to continue


agree_to_continue = 'yes'
while agree_to_continue == 'yes':
    numerical_grade = int(input('What is the numerical grade you want me to convert? '))
    if numerical_grade >= 88:
        print(f'A grade of {numerical_grade} corresponds to an A.')
    elif numerical_grade >= 80:
        print(f'A grade of {numerical_grade} corresponds to a B.')
    elif numerical_grade >= 67:
        print(f'A grade of {numerical_grade} corresponds to a C.')
    elif numerical_grade >= 60:
        print(f'A grade of {numerical_grade} corresponds to a D.')
    elif numerical_grade >= 0:
        print(f'A grade of {numerical_grade} corresponds to an F.')
    agree_to_continue = input('Would you like to convert another numerical grade? ')

print('----------------------------------------------')

# create a list of dictionaries where each dictionary represents a book that you have read.
# each dictionary in the list should have the keys title, author, and genre.
# loop through the list and print out information about each book

books = [{'title' : 'Harry Potter', 'author' : 'J. K. Rowling', 'genre' : 'fantasy'}, 
         {'title' : 'Pistol', 'author' : 'Mark Kriegel', 'genre' : 'biography'},
         {'title' : 'Eragon', 'author' : 'Christopher Paolini', 'genre' : 'fantasy'}]

for book in books:
    print('{} is by {} and belongs to the genre of {}.'.format(book['title'], book['author'], book['genre']))

print('----------------------------------------------')

# prompt the user to enter a genre, then loop through your books list and print out the titles
# of all the books in that genre

chosen_genre = input('What genre would you like to search by? ')

for book in books:
    if book['genre'] == chosen_genre:
        print(book['title'])