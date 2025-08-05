import os

# Folder name to create
folder_name = "test_folder"

# Full path
path = os.path.join(os.getcwd(), folder_name)

# Check if folder exists
if not os.path.exists(path):
    os.mkdir(path)
    print(f"📁 Folder '{folder_name}' created!")
else:
    print(f"✅ Folder '{folder_name}' already exists.")
