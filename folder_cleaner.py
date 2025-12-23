import os
import shutil

path = input("Enter folder path: ")

for file in os.listdir(path):
    if file.endswith(".txt"):
        shutil.move(os.path.join(path, file), os.path.join(path, "Text_Files"))
    elif file.endswith(".jpg"):
        shutil.move(os.path.join(path, file), os.path.join(path, "Images"))

print("Folder cleaned successfully")
