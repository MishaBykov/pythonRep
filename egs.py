import os

path = r"D:\FilesGames"
find_dir = ".egstore"

for i in os.scandir(path):
    i: os.DirEntry
    if i.is_dir() and os.path.exists(os.path.join(i.path, find_dir)):
        os.rename(i.path, i.path + '_')

