import os
import shutil
os.chdir(r"C:\Users\Neeraj\Desktop\AI")
file_iter = os.walk(r"C:\Users\Neeraj\Desktop\AI")
for current_path, folder_names, file_names in file_iter:
    print(f"current_path : {current_path}")
    print(f"folder_names : {folder_names}")
    print(f"file_names : {file_names}")    
# os.makedirs("new/movies")
# os.rmdir("new")
# shutil.rmtree("new")
# shutil.copytree("new", "documents/new")
# shutil.copy("file.txt", "documents/file.txt")
# shutil.move("file.txt", "new/file2.txt")
# shutil.move("new", "documents/new2")

