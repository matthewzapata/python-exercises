# Define a function named is_two. It should accept one input and return True 
# if the passed input is either the number or the string 2, False otherwise.

def is_two(x):
    if x == '2' or x == 2:
        return True
    else:
        return False

print(is_two(2))
print(is_two('2'))
print(is_two(3))

print('------------------')

# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if x in vowels:
        return True
    else:
        return False

print(is_vowel('a'))
print(is_vowel('o'))
print(is_vowel('f'))

print('--------------')

# Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(x):
    if is_vowel(x) == True:
        return False
    else:
        return True

print(is_consonant('d'))
print(is_consonant('c'))
print(is_consonant('i'))

print('---------------')

# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

def capital_if_con(x):
    if is_consonant(x[0]) == True:
        return x.capitalize()
    else:
        return 'Does not start with a consonant.'

print(capital_if_con('hello'))
print(capital_if_con('eagle'))
print(capital_if_con('igloo'))

print('---------------')

# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1)
# and the bill total, and return the amount to tip.

def calculate_tip(bill, tip = 0.18):
    return '${:2f}'.format(tip * bill)

print(calculate_tip(10, 0.2))
print(calculate_tip(50))
print(calculate_tip(30))

print('--------------')

# Define a function named apply_discount. It should accept an original price,
# and a discount percentage, and return the price after the discount is applied.

def apply_discount(price, discount):
    sale_price = price - (price * discount)
    return 'The sale price of the item is ${:2f}'.format(sale_price)

print(apply_discount(100, .20))
print(apply_discount(50, .10))
print(apply_discount(20, .50))

print('-----------------')

# Define a function named handle_commas. It should accept a string that is a 
# number that contains commas in it as input, and return a number as output.

def handle_commas(x):
    return int(x.replace(',', ''))

print(handle_commas('1,000,000'))
print(handle_commas('1,236,200'))
print(handle_commas('1,497'))

print('------------------')

# Define a function named get_letter_grade.
# It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(x):
    if x > 88:
        return 'A'
    elif x > 80:
        return 'B'
    elif x > 67:
        return 'C'
    elif x > 60:
        return 'D'
    else:
        return 'F'

print(get_letter_grade(88))
print(get_letter_grade(65))
print(get_letter_grade(78))

print('-----------------')

# Define a function named remove_vowels that accepts a string and returns a string 
# with all the vowels removed.

def remove_vowels(word):
    for letter in word:
        if is_vowel(letter) == True:
            word = word.replace(letter, '')
    return word

print(remove_vowels('caterpillar'))

print('--------------------')

# Define a function named normalize_name. 
# It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

def normalize_name(name):
    import re
    name = re.sub(r'([^\s\w]|_)+', '', name)
    name = name.strip()
    name = name.lower()
    name = name.replace(' ', '_')
    return name

# or this works too
LETTERS = '_abcdefghijklmnopqrstuvwxyz0123456789'

def normalize_name(name):
    name = name.lower()
    valid_characters = []
    for character in name:
        if character in LETTERS:
            valid_characters.append(character)
    return ''.join(valid_characters).strip().replace(' ', '')

print(normalize_name('Matthew Zapata    '))
print(normalize_name('214123@#$@#$@$ksfonsondf   jn jn n j j nj'))
print(normalize_name('asd234*&^$%$%&(^^%*jnkb*&%^$hgjhR'))

print('----------------------')

# Write a function named cumsum that accepts a list of numbers and 
# returns a list that is the cumulative sum of the numbers in the list.

def cumsum(numbers):
    cum_list = []
    n = 0
    for i in numbers:
        cum_list.extend([sum(numbers[0:(n + 1)])])
        n += 1
    return cum_list

x = [1, 2, 3, 4]
print(cumsum(x))
y = [1, 1, 1]
print(cumsum(y))
z = [2, 4, 6, 8]
print(cumsum(z))

print('-----------------------')

# BONUS
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm 
# and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.

def twelveto24(time):
    if (time[-2] + time[-1]) == 'pm':
        split_time = time.split(':')
        if int(split_time[0]) == 12:
            new_time = ':'.join(split_time)
            new_time_no_letters = new_time.replace('pm', '')
            return new_time_no_letters
        else:
            new_hour = str(int(split_time[0]) + 12)
            split_time[0] = new_hour
            new_time = ':'.join(split_time)
            new_time_no_letters = new_time.replace('pm', '')
            return new_time_no_letters
    elif (time[-2] + time[-1]) == 'am' and (time[0] + time[1]) == '12':
        split_time = time.split(':')
        new_hour = str(int(split_time[0]) - 12)
        split_time[0] = new_hour
        new_time = ':'.join(split_time)
        new_time_no_letters = new_time.replace('am', '')
        return new_time_no_letters
    else:
        new_time_no_letters = time.replace('am', '')
        return new_time_no_letters

print(twelveto24('11:30pm'))

print('-------------------------')

def twentyfourto12(time):
    time_split_to_list = time.split(':')
    if int(time_split_to_list[0]) == 0:
        new_hour = str(int(time_split_to_list[0]) + 12)
        time_split_to_list[0] = new_hour
        new_time = ':'.join(time_split_to_list)
        new_time_with_letters = new_time + 'am'
        return new_time_with_letters
    elif int(time_split_to_list[0]) == 12:
        new_time_with_letters = time + 'pm'
        return new_time_with_letters
    elif int(time_split_to_list[0]) == 24:
        new_hour = str(int(time_split_to_list[0]) - 12)
        time_split_to_list[0] = new_hour
        new_time = ':'.join(time_split_to_list)
        new_time_with_letters = new_time + 'am'
        return new_time_with_letters
    elif int(time_split_to_list[0]) > 12:
        new_hour = str(int(time_split_to_list[0]) - 12)
        time_split_to_list[0] = new_hour
        new_time = ':'.join(time_split_to_list)
        new_time_with_letters = new_time + 'pm'
        return new_time_with_letters
    else:
        new_time_with_letters = time + 'am'
        return new_time_with_letters

print(twentyfourto12('11:00'))

print('--------------------------')

# Create a function named col_index. It should accept a spreadsheet column name, 
# and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27
def col_index(x):
    alpha_dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
    'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 
    'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    if len(x) > 1:
        col_index_mult = (len(x) - 1) * 26
        n = 0
        for letter in x:
            if letter != 'A':
                col_index_add = col_index_mult + (26 ** int(alpha_dict[x[n]]))
            n += 1
        col_final = col_index_add + alpha_dict[x[-1]]
        return col_final
    else:
        col_final = alpha_dict[x[0]]
        return col_final

print(col_index('A'))