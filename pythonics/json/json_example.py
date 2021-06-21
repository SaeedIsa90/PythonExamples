import json

# Reading json file
file_path = "example.json"
fd = open(file_path)
content = json.load(fd)
fd.close()

print(content)

# Writing json file
data = {"Name": "Saeed",
        "Family": "Isa",
        "Job desc": "SW Eng",
        "Grades": [100, 88, 98],
        "Address": {"Street": "Ebn roshd",
                    "House num": 100}
        }

n_fd = open('example2.json', 'w')
json.dump(data, n_fd)
n_fd.close()
