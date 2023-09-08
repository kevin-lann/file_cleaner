import os

file_name = input('Enter a file you want to delete: ')
file_path = '/Users/kevin/Downloads/' + file_name

if os.path.isfile(file_path):
    os.remove(file_path)
    print(f"{file_name} was successfully deleted")
else:
    print(f"{file_name} does not exist")

