# Pandas

# Read CSV file
import pandas as pd
df = pd.read_csv("data.csv")
print(df)

# Writing csv
data = [['Layan', 'Haj', 20], ['Muhammed', 'Khalaily', 50], ['Shdwan', 'Kriem', 33]]
df2 = pd.DataFrame(data=data, columns=['FirstName', 'LastName', 'Age'])
print(df2)

df2.to_csv('data2.csv', index=False)

# CSV library

import csv
# Each line is list
with open('data.csv', 'r') as fd:
    csv_reader = csv.reader(fd)
    for r in csv_reader:
        print(r)

# How can we check the header ?
# Each line is list
with open('data.csv', 'r') as fd:
    csv_reader = csv.reader(fd)
    for i, r in enumerate(csv_reader):
        if i == 0:
            print('header:', r)
        else:
            print('data:', r)

# Each line is dictionary
with open('data.csv', 'r') as fd:
    csv_reader = csv.DictReader(fd)
    for r in csv_reader:
        print(r)

# Writing csv
with open('data3.csv', 'w') as fd:
    csv_writer = csv.writer(fd)
    csv_writer.writerow(['Full Name', 'Day', 'Month'])
    csv_writer.writerow(['Saeed Isa', 15, 'July'])
    csv_writer.writerow(['Salam Isa-Khatib', 6, 'Feb'])