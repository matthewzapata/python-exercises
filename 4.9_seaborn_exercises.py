import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pydataset import data
from matplotlib import cm
import numpy as np
# # ------------------------------------------------

# # Use the iris database to answer the following quesitons:
# iris = data('iris')
# iris.info()
## ------------------------------------------------

# # What does the distribution of petal lengths look like?
# sns.distplot(iris['Petal.Length'])
# plt.show()
## ------------------------------------------------

# # Is there a correlation between petal length and petal width?
# print(iris.corr())
# sns.heatmap(iris.corr(), cmap=cm.PiYG, annot=True, center=0)
# plt.show()

# There is a strong positive correlation.

## ------------------------------------------------
# # Would it be reasonable to predict species based on sepal width and sepal length?
# sns.relplot(data=iris, x='Sepal.Length', y='Sepal.Width', hue='Species')
# plt.show()

# # It can possibly predict setosas correctly but may suffer when predicting other species due to overlap of values.


## ------------------------------------------------
# # Which features would be best used to predict species?
# print(iris.head())
# print(iris.corr())
# sns.relplot(data=iris, x='Sepal.Length', y='Sepal.Width', hue='Species')
# sns.relplot(data=iris, x='Sepal.Length', y='Petal.Length', hue='Species')
# sns.relplot(data=iris, x='Sepal.Length', y='Petal.Width', hue='Species')
# sns.relplot(data=iris, x='Petal.Length', y='Sepal.Width', hue='Species')
# sns.relplot(data=iris, x='Petal.Length', y='Petal.Width', hue='Species')
# plt.show()

# # Petal.Length and Petal.Width seem to be the best features to use.
## They have more distinct values for the different species compared to other variables.

## -----------------------------------------------
# Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set.
# Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset.
# What do you notice?
# anscombe = sns.load_dataset('anscombe')
# print(anscombe.dtypes)

# print(anscombe.head())

# print(anscombe.groupby('dataset').describe())

## The x values for datasets I, II, and III are the same or extremely similar. Many x values for dataset IV are the same. 
## y values differ between datasets.

# # ----------------------------------------------------
# # Plot the x and y values from the anscombe data. Each dataset should be in a separate column.
# sns.relplot(data = anscombe, x='x', y='y', col='dataset')
# plt.show()

# # ------------------------------------------------------
## Load the InsectSprays dataset and read it's documentation.
# sprays = data('InsectSprays', show_doc=True)
# sprays = data('InsectSprays')
# print(sprays.sample(10))

## -----------------------------------------------------
## Create a boxplot that shows the effectiveness of the different insect sprays.
# sprays.info()

# grouped_sprays = sprays.groupby('spray')['count'].count()
# print(grouped_sprays)

# sns.boxplot(data=sprays, x='count', y='spray')
# plt.show()

## ------------------------------------------------------
# # Load the swiss dataset and read it's documentation. Create visualizations to answer the following questions:
# swiss = data('swiss', show_doc=True)
# swiss = data('swiss')
# print(swiss.info())
# print(swiss.head())


## -----------------------------------------------------
# # Create a column named is_catholic that holds a boolean value of whether or not the province is Catholic.
# # (Choose a cutoff point for what constitutes catholic)
# swiss['is_catholic'] = swiss.Catholic.apply(lambda x: True if x >= 51.00 else False)
# print(swiss.sample(10))


## ----------------------------------------------------
# # Does whether or not a province is Catholic influence fertility?
# # sns.stripplot(data=swiss, x='is_catholic', y='Fertility')
# # plt.show()
# sns.boxplot(data=swiss, x='is_catholic', y='Fertility')
# plt.show()
# print(swiss.groupby('is_catholic')['Fertility'].mean())

# # At a glance, provinces that are Catholic seem to have a higher fertility rate.


## -----------------------------------------------------
# # What measure correlates most strongly with fertility?
# sns.heatmap(swiss.corr(), cmap=cm.PiYG, annot=True, center=0)
# plt.show()

# # The measure with the strongest correlation to fertility is education, which is negatively correlated. Examination is a close second.

# # Using the chipotle dataset from the previous exercise,
# # create a barplot that shows the 4 most popular items and the revenue produced by each.

# from env import user, password, host
# from env import get_connection
# dbc = get_connection('chipotle')
# orders = pd.read_sql('SELECT * FROM orders', dbc)
# # print(orders.sample(10))

# orders.item_price = orders.item_price.str.replace('$', '').astype('float')


# grouped_summed_items = orders.groupby('item_name').agg({'item_name':'count', 'item_price':'sum'})
# print(grouped_summed_items)
# sorted_items = grouped_summed_items.sort_values(by='item_name', ascending=False).head(4)
# # sorted_items.drop('item_name', inplace=True)
# print(sorted_items)

# sns.barplot(data=sorted_items, x='item_name', y='item_price')
# plt.xticks((np.arange(4)), ('Steak Burrito', 'Chips and Guac', 'Chicken Burrito', 'Chicken Bowl'))
# plt.show()

## --------------------------------------------------------------
# # Load the sleepstudy data and read it's documentation. 
# # Use seaborn to create a line plot of all the individual subject's reaction times and a more
# # prominent line showing the average change in reaction time.
# sleep = data('sleepstudy', show_doc=True)
# sleep = data('sleepstudy')
# # sns.lineplot(data=sleep, x='Subject', y='Reaction', hue='Days')
# # plt.show()
# print(sleep.head(20))

# plt.figure(figsize=(12, 12))
# sns.lineplot(data=sleep, y='Reaction', x='Days', hue='Subject')
# sns.lineplot(data=sleep, y='Reaction', x='Days', linewidth=5, label='Average')
# plt.show()
