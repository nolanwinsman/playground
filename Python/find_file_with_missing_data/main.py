"""
Quick script created to compare to folders to see if any files failed to copy to new folder

"""
import os

ORIGINAL = r'D:\ps2\DVD'
NEW = r'F:\DVD'

SIZES = {}

# Iterate over files in directory
for path, folders, files in os.walk(ORIGINAL):
    # Open file
    for filename in files:
        if filename.endswith('.iso'):
            p = os.path.join(path, filename)
            size = os.path.getsize(p)
            SIZES[filename] = size

for path, folders, files in os.walk(NEW):
    # Open file
    for filename in files:
        if filename.endswith('.iso'):
            p = os.path.join(path, filename)
            size = os.path.getsize(p)
            og_size = SIZES[filename]
            if og_size != size:
                print(f"NOT A MATCH Filename: {filename} size DOES NOT match {size} {og_size}")
            else:
                print(f"Filename: {filename} size matches {size} {og_size}")

 
