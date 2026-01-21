import os
import shutil

source_file = "app.log"

if not os.path.exists(source_file):
    print(f"{source_file} not found!")
    exit(1)


for i in range(1, 6):
    dest_file = f"app_{i}.log"
    
    
    if os.path.exists(dest_file):
        print(f"{dest_file} already exists, skipping")
        continue
    
    shutil.copy(source_file, dest_file)
    print(f"Created {dest_file}")

print("Log duplication complete!")
