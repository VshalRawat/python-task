import os


folder_name = "test_folder"

path = os.path.join(os.getcwd(), folder_name)

if not os.path.exists(path):
    os.mkdir(path)
    print(f" Folder '{folder_name}' created!")
else:
    print(f"Folder '{folder_name}' already exists.")
