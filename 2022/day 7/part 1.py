from __future__ import annotations
import re

file = open("data.txt")
lines = file.read().split("\n")


class File:
    def __init__(self, size: int, name: str):
        self.size = size
        self.name = name


class Folder:
    def __init__(self, name: str, parent: None | Folder = None):
        self.name = name
        self.files = []
        self.folders = []
        self.parent_folder = parent

    def add_file(self, file: File):
        self.files.append(file)

    def add_folder(self, folder: Folder):
        self.folders.append(folder)

    def get_folder(self, name: str):
        find_folder = [folder for folder in self.folders if folder.name == name]
        if find_folder == []:
            return Folder(name=name, parent=self.add_folder(folder))
        else:
            return find_folder[0]
            
    def sum_folders_where_at_most(self, acc_total, at_most: int):
        current_folder_size = self.sum_size()
        if current_folder_size >= at_most:
            current_folder_size = 0

        folder_size = 0
        
        for folder in self.folders:
            folder_size += folder.sum_folders_where_at_most(acc_total, at_most)

        return acc_total + current_folder_size + folder_size


    def sum_size(self):
        folder_sizes = [folder.sum_size() for folder in self.folders]
        return sum(folder_sizes) + self.sum_files()

    def sum_files(self):
        file_sizes = [file.size for file in self.files]
        return sum(file_sizes)


root = Folder(name="root")
current_folder = root
ls = False

for line in lines:
    if line.startswith("$ cd"):
        ls = False
        folder = line.replace("$ cd ", "")
        if folder == "/":
            current_folder = root
        elif folder == "..":
            current_folder = current_folder.parent_folder
        else:
            current_folder = current_folder.get_folder(folder)

    if ls == True:
        if line.startswith("dir"):
            folder = line.replace("dir ", "")
            current_folder.add_folder(
                Folder(name=folder, parent=current_folder))
        else:
            size = int(re.compile("\d*").search(line).group())
            matches = re.findall(r"[a-z]*\.?[a-z]*", line)
            name = list(filter(None, matches))
            current_folder.add_file(File(size, name[0]))

    if line.startswith("$ ls"):
        ls = True

print("Answer: ", root.sum_folders_where_at_most(0, 100000))