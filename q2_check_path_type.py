import os


path = "C:\\Users\\Hp\\Desktop\\Python_Task"

if os.path.exists(path):
    if os.path.isfile(path):
        print("📄 It's a file.")
    elif os.path.isdir(path):
        print("📁 It's a directory.")
else:
    print("❌ Path does not exist.")
