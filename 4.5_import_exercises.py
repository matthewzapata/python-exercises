# # Import and test 3 of the functions from your functions exercise file.
# # Import each function in a different way:

# # import the module and refer to the function with the . syntax
# import function_exercises
# print('Import finished.')

# print(function_exercises.is_two(2))


# print('-------------------')
# # use from to import the function directly
# from function_exercises import calculate_tip
# print(calculate_tip(50,0.2))


# print('-------------------')
# # use from and give the function a different name
# from function_exercises import get_letter_grade as grade
# print(grade(76))

# print('-------------------')

# # For the following exercises, read about and use the itertools 
# # module from the standard library to help you solve the problem.
# import itertools

# # How many different ways can you combine the letters 
# # from "abc" with the numbers 1, 2, and 3?
# a = ['a', 'b', 'c']
# b = [1, 2, 3]
# print(list(itertools.product(a, b)))

# print('--------------------')

# # How many different ways can you combine two of the 
# # letters from "abcd"?

# print(list(itertools.combinations('abcd', 2)))
# print('--------------------')

# # Save this file as profiles.json inside of your exercises directory. 
# # Use the load function from the json module to open this file, it will produce a list of dictionaries. 
import json

# create a list called user_data that contains the json list of dictionaries
user_data = json.load(open('profiles.json'))

# print('-------------------------------')

print(json.dumps(user_data, sort_keys = True, indent = 4))


# # Using this data, write some code that calculates and outputs the following information:
# # Total number of users
# def total_users():
#     count_of_total = len(user_data)
#     return count_of_total
# print('Number of users: %s' % total_users())


# print('-----------------------------')


# # Number of active users
# def active_count():
#     active_users = 0
#     for user in user_data:
#         if user['isActive']:
#             active_users = active_users + 1
#     return active_users


# print('Number of active users: %s' % active_count())

# print('----------------------------')

# # Number of inactive users


# print('Number of inactive users: %s' % (len(user_data) - active_count()))


# print('--------------------------')

# # Grand total of balances for all users
# def balance_grand_total():
#     balance_total = 0
#     for user in user_data:
#         user_balance = float(user['balance'].replace('$', '').replace(',', ''))
#         balance_total = balance_total + user_balance
#     return balance_total

# print('The total of all balances for all users is: $%s' % balance_grand_total())

# print('-------------------------')


# # Average balance per user
# def average_user_balance():
#     average = balance_grand_total()/total_users()
#     float_average = float(average)
#     return average

# print('The average balance per user is: ${:,.2f}'.format(average_user_balance()))

# print('------------------------')


# # User with the lowest balance
# def lowest_balance():
#     lowest_balance = float(user_data[0]['balance'].replace('$', '').replace(',', ''))
#     lowest_user = user_data[0]['name']
#     for user in user_data:
#         if float(user['balance'].replace('$', '').replace(',', '')) < lowest_balance:
#             lowest_balance = float(user['balance'].replace('$', '').replace(',', ''))
#             lowest_user = user['name']
#     return f'User name: {lowest_user} has the lowest balance of ${lowest_balance:,}'

# print(lowest_balance())

# print('------------------------------')

# # User with the highest balance
# def highest_balance():
#     highest_balance = float(user_data[0]['balance'].replace('$', '').replace(',', ''))
#     highest_user = user_data[0]['name']
#     for user in user_data:
#         if float(user['balance'].replace('$', '').replace(',', '')) > highest_balance:
#             highest_balance = float(user['balance'].replace('$', '').replace(',', ''))
#             highest_user = user['name']
#     return f'User name: {highest_user} has the highest balance of ${highest_balance:,}'

# print(highest_balance())

# print('------------------------------')


# # Most common favorite fruit
# def fave_fruit_dict():
#     # creates a dictionary with fruit as keys and respective counts as values
#     fruit_keys = []
#     for user in user_data:
#         if user['favoriteFruit'] not in fruit_keys:
#             fruit_keys.append(user['favoriteFruit'])
#     fruit_dict = {}
#     for fruit in fruit_keys:
#         fruit_dict[fruit] = 0
#     for user in user_data:
#         fruit_dict[user['favoriteFruit']] = (fruit_dict[user['favoriteFruit']] + 1)
    
#     return fruit_dict

# fruit = fave_fruit_dict()
# t = max(fruit, key=fruit.get)
# print('Most common favorite fruit: %s' % t)

# print('----------------------------')

# # Least most common favorite fruit
# z = min(fruit, key=fruit.get)
# print('Least common favorite fruit: %s' % z)

# Total number of unread messages for all users
def total_unread_messages():
    total_messages = 0
    for user in user_data:
        user_message_count = int(''.join(list(filter(str.isdigit, user['greeting']))))
        total_messages = total_messages + user_message_count
    return total_messages

print(total_unread_messages())
