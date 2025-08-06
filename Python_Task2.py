import os

input_folder = "data_input"
output_folder = "data_output"

if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    print(f"📁 Created folder '{input_folder}'. Please add .txt files to it.")
    exit()

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

summary_lines = []

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with open(input_path, 'r') as f:
            lines = f.readlines()

        processed_lines = []
        line_count = 0
        word_count = 0

        for line in lines:
            if line.strip().startswith("#"):
                continue
            line = line.replace("temp", "permanent")
            processed_lines.append(line)
            line_count += 1
            word_count += len(line.split())

        with open(output_path, 'w') as f:
            f.writelines(processed_lines)

        summary_lines.append(f"{filename} | Lines: {line_count} | Words: {word_count}")

with open(os.path.join(output_folder, "summary.txt"), 'w') as f:
    f.write("\n".join(summary_lines))

print("✅ Task Completed. Check the 'data_output' folder.")
