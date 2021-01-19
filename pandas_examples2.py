import pandas as pd

products = pd.DataFrame({'category': ['Cleaning', 'Cleaning', 'Entertainment', 'Entertainment', 'Tech', 'Tech'],
                         'store': ['Walmart', 'Target', 'Walmart', 'MySuper', 'Target', 'Walmart'],
                         'price': [11.42, 23.50, 19.99, 15.95, 55.75, 111.55],
                         'amount': [4, 3, 5, 7, 5, 8]})
print(products)

print('\n---------- Head & Tail ----------')
print('----- Head -----')
print(products.head(2))  # Default is 10
print('\n----- Tail -----')
print(products.tail(2))  # Default is 10

print('\n---------- Pivoting ----------')
print(products)
# Pivoting data according to index by column
pivot_products = products.pivot(index='category', columns='store', values='price')
print('\n--------------------')
print(pivot_products)


print('\n---------- New DataFrame ----------')
df = pd.DataFrame(columns=['Name', 'City', 'Grade'],
                  data=[['Saeed', 'Majd el kurum', 88],
                        ['Salam', 'Qahera', 97],
                        ['Nidal', 'Bagdad', 93]])
print(df)

print('\n---------- Rename ----------')
print('----- Rename columns -----')
new_df = df.rename(columns={'City': 'Country'})
print(new_df)

print('\n----- Rename index -----')
new_df = df.rename(index={0: 'row0'})
print(new_df)

print('\n----- Rename index & columns -----')
new_df = df.rename(index={0: 'row0'}, columns={'City': 'Country'})
print(new_df)


print('\n---------- Data types ----------')
print('DataFrame columns data types:\n', df.dtypes)  # type per column
print('DataFrame City column data type:', df['City'].dtype)  # type per City column

new_df = df.copy()  # Creating new copy of DF
# print(new_df)
print('\n----- Changing single column type -----')
new_df['Grade'] = new_df['Grade'].astype('float')  # Converting int to float
print('DataFrame columns data types:\n', new_df.dtypes)  # type per column


print('\n----- Changing all DataFrame -----')
new_df = new_df.astype('str')  # Converting all data frame to string
print('DataFrame columns data types:\n', new_df.dtypes)  # type per column

print('\n----- Changing multiple columns at once -----')
new_df = new_df.astype({'City': 'str', 'Grade': 'float'})
print('DataFrame columns data types:\n', new_df.dtypes)  # type per column
print(new_df)

print('\n---------- New DataFrame ----------')
df1 = df.copy()
df2 = pd.DataFrame(columns=['Name', 'City', 'Grade'],
                   data=[['Saeed2', 'kurum2', 99],
                         ['Salam2', 'Qahera2', 45],
                         ['Nidal2', 'Bagdad2', 66]])
print(df2)

print('\n---------- Concatenating & re-indexing ----------')
print('----- Concatenate index axis -----')
df3 = pd.concat([df1, df2])  # Same as default axis=0
print(df3)

print('----- Index resetting -----')
# For non meaningful indices
df3 = df3.reset_index(drop=True)  # will reset index and drop original indices
print(df3)

print('----- Index resetting during concat -----')
df3 = pd.concat([df1, df2], ignore_index=True)  # Same as default axis=0
print(df3)

print('----- Redefining DataFrame -----')
df2 = pd.DataFrame(columns=['Name', 'City', 'Grade2'],
                   data=[['Saeed2', 'kurum2', 99],
                         ['Salam2', 'Qahera2', 45],
                         ['Nidal2', 'Bagdad2', 66]])
print(df2)

# Concatenate index axis with different column names
print('----- Concatenating different columns -----')
df3 = pd.concat([df1, df2])  # Will fill NaN
print(df3)

# Concatenate index axis with different column names but removing columns has NaN Values
print('----- Concatenating different columns - remove NaN columns -----')
df3 = pd.concat([df1, df2], join='inner')  # Will remove NaN columns
print(df3)

print('----- Concatenate column axis -----')
df2 = pd.DataFrame(columns=['Family Name', 'Country'],
                   data=[['Isa', 'c1'],
                         ['Isa', 'C2'],
                         ['ISa2', 'C3']])
print(df2)

df3 = pd.concat([df1, df2], axis=1)
print(df3)
# All above concatenating function works with axis=1

print('----- Concatenate using append -----')
df = df1.append(df2)
print(df)


# Duplications
print('----- Duplications -----')
df = pd.DataFrame(columns=['Name', 'City', 'Grade'],
                  data=[['Saeed', 'Majd el kurum', 88],
                        ['Salam', 'Qahera', 97],
                        ['Saeed', 'Majd el kurum', 88]])
print(df)
new_df = df.drop_duplicates()
print(new_df)

# Merge and Join
print('\n---------- Merge ----------')
left = pd.DataFrame({"ID": ["K0", "K0", "K1", "K2"],
                     "FirstName": ["K0", "K1", "K0", "K1"],
                     "A": ["A0", "A1", "A2", "A3"],
                     "B": ["B0", "B1", "B2", "B3"]})
print('--------------\nLeft data frame:\n', left)

right = pd.DataFrame({"ID": ["K0", "K1", "K1", "K2"],
                      "FirstName": ["K0", "K0", "K0", "K0"],
                      "C": ["C0", "C1", "C2", "C3"],
                      "D": ["D0", "D1", "D2", "D3"]})
print('--------------\nRight data frame:\n', right)

# Main questions while merging: on what ? how to ?
# on ==> which keys (default index)
# how ==> left, right, outer, inner  (default left)

df3 = pd.merge(left, right, on=['ID', 'FirstName'], how='left')  # Iterating over left "on" keys
print('--------------\nMerging how=left:\n', df3)

print('--------------\nLeft data frame:\n', left)
print('--------------\nRight data frame:\n', right)
df3 = pd.merge(left, right, on=['ID', 'FirstName'], how='outer')  # Union
print('--------------\nMerging how=outer:\n', df3)


print('--------------\nLeft data frame:\n', left)
print('--------------\nRight data frame:\n', right)
df3 = pd.merge(left, right, on=['ID', 'FirstName'], how='inner')  # Intersection
print('--------------\nMerging how=inner:\n', df3)

# Homework: join
