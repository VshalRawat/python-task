import os

print("📄 .txt files in the current directory:\n")

for filename in os.listdir():
    if filename.endswith(".txt"):
        print(f"📝 {filename}")
