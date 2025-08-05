import os
import shutil

# Name of the reports folder
reports_folder = "reports"

# Check if reports folder exists, create if not
if not os.path.exists(reports_folder):
    os.mkdir(reports_folder)
    print(f"📁 Folder '{reports_folder}' created!")
else:
    print(f"📁 Folder '{reports_folder}' already exists!")

# Loop through current directory and move .txt files
for file in os.listdir():
    if file.endswith(".txt") and os.path.isfile(file):
        print(f"➡️ Moving {file} to {reports_folder}/")
        shutil.move(file, os.path.join(reports_folder, file))
