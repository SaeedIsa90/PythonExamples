# old way
lst = ['Saeed', 'Subscribe', 'Hello', 1, 105, True, 'World']
my_dict = {"Name": "Saeed", "Family": "Isa", "Key2": "Val2"}

# list example
j = 0
for item in lst:
    print("item:", item, "----- idx: ", j)
    j += 1

# Dict example
j = 0
for key, val in my_dict.items():
    print("key:", key, "- val: ", val,  "----- idx: ", j)
    j += 1

# Enumerate
# list example
for j, item in enumerate(lst):
    print("item:", item, "----- idx: ", j)

# Dict example
for j, item in enumerate(my_dict.items()):
    key, val = item
    print("key:", key, "- val: ", val,  "----- idx: ", j)
