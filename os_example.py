import os

print('Current work dir:', os.getcwd())

# Making dir
# os.mkdir('my_dir')

# joining paths
proj_dir = 'example_proj'
parent_dir = 'example_dir'
file_name = 'os_example.py'

# Windows: proj_dir\parent_dir\file_name
# Linux: proj_dir/parent_dir/file_name

file_path = os.path.join(proj_dir, parent_dir, file_name)
print('File path:', file_path)

file_name = os.path.basename(file_path)
print('File name:', file_name)
print('File extension:', os.path.splitext(file_name))

cwd = os.getcwd()
parent_path = os.path.dirname(cwd)
print('Parent path:', parent_path)
print('List dirs:', os.listdir(parent_path))
lst_dir = os.listdir(parent_path)

# Removing
# os.remove('to_delete.py')
# os.rmdir('my_dir')

# querying
for i in lst_dir:
    full_path_i = os.path.join(parent_path, i)
    if os.path.isfile(full_path_i):
        print(i, ' is file')
    if os.path.isdir(full_path_i):
        print(i, ' is dir')

