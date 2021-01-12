import pandas as pd

# Generating DataFrame
print('\n---------- Generating DataFrame ----------')
print('\n---------- DataFrame from 2-D Array ----------')
df = pd.DataFrame(columns=['Name', 'City', 'Grade'],
                  data=[['Saeed', 'Majd el kurum', 88],
                        ['Salam', 'Qahera', 97],
                        ['Nidal', 'Bagdad', 93]])
print(df)

print('\n---------- DataFrame from dictionary ----------')
data = {'Name': ['Saeed', 'Salam', 'Nidal'],
        'City': ['Majd el kurum', 'Qahera', 'Bagdad'],
        'Grade': [88, 97, 93]}

# Takes dictionary keys as column names
# Default Index labels (numbers)
df = pd.DataFrame(data)
print(df)

# Saving data frame as a csv
df.to_csv('my_data.csv', index=False)

print('\n---------- DataFrame from CSV file ----------')
new_df = pd.read_csv('my_data.csv')
print(new_df)

# Dataframe attributes
print('\n---------- DataFrame attributes ----------')
print('Dataframe shape:', df.shape)
print('Dataframe indices description:', df.index)
print('Dataframe columns:', df.columns)  # Can convert to regular list

# Accessing and Indexing data in DataFrame
print('\n---------- Accessing and Indexing ----------')
print('\n----- Getting data subset -----')
print('Getting subset from index 1:\n', df[1:])  # Same as list but works with indices
print('Getting subset from index 1-2', df[1:2])  # getting data from index 1 till 2 not included

print('\n----- By Position -----')
# Only numbers - be careful
print('Getting single value:', df.iloc[0, 1])  # Treat it as 2-D array
print('Getting whole row:\n', df.iloc[0])

print('\n----- By Label -----')
# Index & Column names
print('Getting single value:', df.loc[0, 'City'])  # Treat it as 2-D array but with real label names
print('Getting whole row0:\n', df.loc[0])

print('\n----- Getting Column  -----')
print('Getting column data:\n', df['City'])  # Returns DataSeries - including indices

print('\n----- Setting data  -----')
df.loc[0, 'City'] = 'Demashq'  # Setting single value
print(df)

print('\n----- Filtering data  -----')
# use boolean expressions - brackets are super important
print('Showing data where grade > 90:\n', df[df['Grade'] > 90])  # Returns new DataFrame
print('Showing data where grade > 90 & from Bagdad:\n', df[(df['Grade'] > 90) & (df['City'] == 'Bagdad')])

print('\n---------- Dropping ----------')
print('Dropping city column:\n', df.drop(columns=['City']))  # Returns new DataFrame
print('Dropping 0 row:\n', df.drop(index=[0]))  # Returns new DataFrame

print('\n---------- Copy ----------')
new_df = df.copy()
print('New dataframe is a total new copy:\n', new_df)

print('\n---------- Creating new column ----------')
new_df['New Grade'] = new_df['Grade']/10  # Creating "new grade" column based on original grade scaled by 10
print(new_df)
new_df['Family name'] = ['Isa', 'Isa', 'Isa2']  # Creating new column based on external data
print(new_df)

print('\n---------- Iterating over ----------')
# Do you real need it?
for index, row in df.iterrows():
    print('This student: ', row['Name'], '- is from:', row['City'])

print('\n---------- Sorting ----------')
print('Sorting by grade:\n', df.sort_values(by=['Grade']))  # Can be multiple columns

print('\n---------- Cleaning ----------')
new_df = df.copy()
print(new_df)
# NaN value can be fetched from numpy
import numpy as np
new_df['Family name'] = ['Isa', 'Isa', np.nan]
print(new_df)
print('Dropping NaN data\n', new_df.dropna())  # Will drop the whole row
print('Filling NaN data\n', new_df.fillna('Anything'))  # will fill any NaN cell with this value

# More & More of data analytics
print('\n---------- More & More ----------')
# df.sum() will sum all columns, strings will be one string, nums will be sum of them...
print('Dataframe grade sum:', df['Grade'].sum())  # sum can be used in whole data frame as well
print('Max grade:', df['Grade'].max())
print('Min grade:', df['Grade'].min())
print('Index of Max grade:', df['Grade'].idxmax())
print('Index of Min grade:', df['Grade'].idxmin())
print('Mean of grades:', df['Grade'].mean())
print('Median of grades:', df['Grade'].median())

print('\n---------- Applying function ----------')
# Running function on DataFrame values
def add_factor(x):
    return x * 2


print('Applying function to single columns:\n', df['Grade'].apply(add_factor)) # df.apply(..) will run it for each val
# df['Grade'] = df['Grade'].apply(add_factor)
print('Applying function for each value:\n', df.apply(add_factor))

print('\n---------- GroupBy ----------')
# Grouping according to value, e.g. group by city
new_df = df.copy()
new_df.loc[1, 'City'] = 'Bagdad'
print(new_df)
grouped_df = new_df.groupby(by=['City'])
for g, d in grouped_df:
    print('Group name:', g)
    print('Group dataframe:\n', d)
    print('************')

# Rows shifting
# Handling NaN values
# ...
