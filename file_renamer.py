import os

path = input("Enter folder path: ")
files = os.listdir(path)

for index, file in enumerate(files, start=1):
    new_name = f"file_{index}.txt"
    os.rename(os.path.join(path, file), os.path.join(path, new_name))

print("Files renamed successfully")
