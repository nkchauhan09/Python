import os
os.getcwd()
print(os.getcwd())
os.chdir(r"C:\Users\Neeraj\Desktop\Python Tutorial")
print(os.getcwd())
os.chdir(r"C:\Users\Neeraj\Desktop\Python")
print(os.getcwd())
# os.mkdir("os_module")
print(os.path.exists("os_module"))
if os.path.exists("os_module"):
    print("already exist")
else:
    print("os_module")
open("os_module.txt", "a").close()
# print(os.listdir(r"C:\Users\Neeraj\Desktop\Python"))
for item in os.listdir():
    # print(r"C:\Users\Neeraj\Desktop\Python" + "\\" + item)
    path = os.path.join(os.getcwd(), item)
    print(path)