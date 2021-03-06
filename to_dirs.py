import argparse
from rename.Renamer import Renamer
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Replace of part of a name')
    parser.add_argument("path", type=str,
                        help="input path dir")
    parser.add_argument("-cod", "--count_one_dir", nargs='?',
                        help="input countOneDir ")
    parser.add_argument("-g", "--git", action='store_true')
    args = parser.parse_args()
    path = args.path
    if args.count_one_dir is None:
        count_one_dir = input("Количество файлов на одну папку: ")
    else:
        count_one_dir = args.count_one_dir
    count_one_dir = int(count_one_dir)
    files_list = sorted(os.listdir(path), key=str.lower)
    count_files = len(files_list)
    os.chdir(path)
    count_new_dir = count_files // count_one_dir + (1 if count_files % count_one_dir != 0 else 0)
    length_name = len(str(count_new_dir))
    ind_file = 0
    for dir_name in range(1, count_new_dir + 1):
        dir_name = '0' * (length_name - len(str(dir_name))) + str(dir_name)
        while os.path.exists(dir_name):
            dir_name = '0' + dir_name
        os.mkdir(dir_name)
        renamer = Renamer(path, destination_path=dir_name, use_git_rename=args.git)
        for i in range(0, count_one_dir):
            try:
                renamer.rename(files_list[ind_file])
            except IndexError:
                print(ind_file, count_files, len(files_list))
            ind_file += 1
            if ind_file == count_files:
                break
