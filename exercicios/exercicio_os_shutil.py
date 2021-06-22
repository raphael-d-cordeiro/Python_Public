import os
import shutil, stat

path_origin = r'E:\temp\legenda1'
new_path = r'E:\temp\legenda2'

try:
    os.mkdir(new_path)
except FileExistsError as error:
    print(f'Directory {new_path} already exists!')

# for root, dirs, files in os.walk(path_origin):
#     for file in files:
#         old_file_path = os.path.join(root, file)
#         new_file_path = os.path.join(new_path, file)
#         if '.srt' in file:
#             shutil.copy2(old_file_path, new_file_path)
#             # shutil.move(old_file_path, new_file_path)
#             print(f'File {file} copied successfuly')

for root, dirs, files in os.walk(new_path):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_path, file)
        if '.srt' in file:
            os.chmod(new_file_path, stat.S_IRWXU) #stat.S_IRWXU: proprietário tem todas as permissões (máscara permissão) 0o700
            os.remove(new_file_path)
            # shutil.move(old_file_path, new_file_path)
            print(f'File {file} has been deleted successfuly')