# to get every detail aboout files,folders
import os
file_iter = os.walk(r"C:\Users\priti\Desktop\Resume")

for current_path,folder_names,file_names in file_iter:
    print(f"current path: {current_path}")
    print(f"folder names: {folder_names}")
    print(f"file names: {file_names}")

# to delete folder
# os.rmdir("")

# to make folder inside folder
os.makedirs("new/new1")