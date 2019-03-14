from pydataset import data
import pandas as pd

# # Use pandas to convert the following list to a numeric series:
# amounts_list = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', 
#             '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', 
#             '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', 
#             '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', 
#             '$452,650.23']

# amounts_series = pd.Series((amount for amount in amounts_list))
# print(amounts_series)
# print(type(amounts_series))

# # ----------------------------------------------------------------------
# # Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:
# mpg_df = data('mpg') # load the dataset and store it in a variable
# data('mpg', show_doc=True) # view the documentation for the dataset

# # How many rows and columns are there?
# # There are 234 rows and 11 columns.

# # What are the data types?
# print(mpg_df.dtypes)
# # strings, floats, and integers

# # Do any cars have better city mileage than highway mileage?
# print(mpg_df.loc[mpg_df['cty'] > mpg_df['hwy']])
# # No.



# # Create a column named mileage_difference. This column should contain the difference 
# # between highway and city milelage for each car.
# print(mpg_df.assign(mileage_difference=(mpg_df.hwy - mpg_df.cty)))
# # print(mpg_df)

# # On average, which manufacturer has the best miles per gallon?
# mpg_df['avg_mpg'] = (mpg_df.hwy + mpg_df.cty)/2
# print(mpg_df)
# print(mpg_df.groupby(['manufacturer'])['avg_mpg'].mean().idxmax())

# # How many different manufacturers are there?
# print(mpg_df.groupby(['manufacturer'])['manufacturer'].sum().count())

# # How many different models are there?
# print(mpg_df.groupby(['model'])['model'].sum().count())

# print('--------')

# # Do automatic or manual cars have better miles per gallon?
# def simple_trans(trans):
#     if trans[:4] == 'auto':
#         return 'auto'
#     else:
#         return 'manual'

# new_trans = mpg_df.trans.apply(simple_trans)
# print(mpg_df.assign(trans2 = mpg_df.trans.apply(simple_trans)).groupby('trans2')['avg_mpg'].mean().idxmax())



# Load the Mammals dataset. Read the documentation for it, 
# and use the data to answer these questions:
mammals_df = data('Mammals')
data('Mammals', show_doc=True)
# print(mammals_df)

# # How many rows and columns are there?
# mammals_df.info()
# # 107 rows and 4 columns

# # What are the data types?
# # float and boolean

# # What is the the weight of the fastest animal?
# print(mammals_df.loc[mammals_df['speed'] == mammals_df['speed'].max()])
# print('-------------')
# # weight is 55 kg

# # What is the overall percentage of specials?
# print((mammals_df.groupby('specials')['specials'].sum().max() / mammals_df['specials'].count()) * 100)
# print(mammals_df['speed'].median())
# print('-------------')

# How many animals are hoppers that are above the median speed? What percentage is this?
print(mammals_df.loc[mammals_df['speed'] > mammals_df['speed'].median(), 'hoppers'].sum())
print((mammals_df.loc[mammals_df['speed'] > mammals_df['speed'].median(), 'hoppers'].sum() / mammals_df['hoppers'].count()) * 100)

# mammals_df['hoppers'].count()) * 100)



# # Getting data from SQL databases
# # Create a function named get_db_url. 
# # It should accept a username, hostname, password, and database name and return 
# # a url formatted like in the examples in this lesson.
# from env import user, password, host
# from sqlalchemy import create_engine
# from datetime import datetime

# def get_db_url(user, password, host, database_name):
#     url = 'mysql+pymysql://{}:{}@{}/{}'.format(user, password, host, database_name)
#     return url

# # Use your function to obtain a connection to the employees database.
# url = get_db_url(user, password, host, 'employees')
# dbc = create_engine(url)

# # Read the employees and titles tables into two separate data frames
# employees_df = pd.read_sql('SELECT * FROM employees', dbc)

# titles_df = pd.read_sql('SELECT * FROM titles', dbc)

# # Visualize the number of employees with each title.
# print(titles_df.groupby('title')['title'].count())
# titles_df.groupby('title')['title'].count().plot.bar()

# # Visualize how frequently employees change titles.
# # print(titles_df.loc[titles_df['to_date'] != titles_df['to_date'].max()].groupby('emp_no').count())
# titles_df.loc[titles_df['to_date'] != titles_df['to_date'].max()].groupby('emp_no').count().plot.hist()

# # Use the .join method to join the employees and titles data frames together
# emp_and_titles_df = employees_df.set_index('emp_no').join(titles_df.set_index('emp_no'))

# # For each title, find the hire date of the employee that was hired most recently with that title.
# a = emp_and_titles_df.groupby('title')['hire_date'].max()        
# print(a)

# # Explore the data from the chipotle database. 
# url = get_db_url(user, password, host, 'chipotle')
# dbc = create_engine(url)
# chipotle_df = pd.read_sql('SELECT * FROM orders', dbc)

# # Write a python script that will use this data to answer the following questions:
# # What is the total price for each order?
# float_price_values = chipotle_df
# float_price_values['float_prices'] = chipotle_df.item_price.apply(lambda x: float(x[1:]))
# print(float_price_values.groupby('order_id')['float_prices'].sum())

# # What are the most popular 3 items?
# print(chipotle_df.groupby('item_name')['item_name'].count().sort_values(ascending=False).head(3))

# # Which item has produced the most revenue?
# print(float_price_values.groupby('item_name')['float_prices'].sum().sort_values(ascending=False).head(1))