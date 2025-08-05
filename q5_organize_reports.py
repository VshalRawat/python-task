import os
import shutil

reports_folder = "reports"
if not os.path.exists(reports_folder):
    os.mkdir(reports_folder)
    print(f"📁 Folder '{reports_folder}' created!")
else:
    print(f"📁 Folder '{reports_folder}' already exists!")

for file in os.listdir():
    if file.endswith(".txt") and os.path.isfile(file):
        print(f"➡️ Moving {file} to {reports_folder}/")
        shutil.move(file, os.path.join(reports_folder, file))
