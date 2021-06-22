from zipfile import ZipFile
import os, fnmatch

path_list = r'E:\temp\mp4'

with ZipFile('file.zip', 'w') as zip:
    for file in os.listdir(path_list):
        if not fnmatch.fnmatch(file, '*.srt'):
            continue
        full_path = os.path.join(path_list, file)
        zip.write(full_path, file)


with ZipFile('file.zip', 'r') as zip:
    for file in zip.namelist():
        print(file)

with ZipFile('file.zip', 'r') as zip:
    zip.extractall('unzip')