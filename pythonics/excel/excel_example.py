# Reading EXCEL file
import pandas as pd

# Default behavior - sheet num 0
df = pd.read_excel('data.xlsx')
print('---------')
print(df)

# Read particular sheet - by name
df = pd.read_excel('data.xlsx', sheet_name='courses')
print('---------')
print(df)

# Read particular sheet - by Index
df = pd.read_excel('data.xlsx', sheet_name=2)
print('---------')
print(df)


# Read multiple sheets - by name
df = pd.read_excel('data.xlsx', sheet_name=['students', 'cities'])
print('---------')
print(df)

# Reading sheet from output
print(df['students'])

# Read multiple sheets - by index
df = pd.read_excel('data.xlsx', sheet_name=[0, 1, 2])
print('---------')
print(df)

# Reading sheet from output
print(df[2])
