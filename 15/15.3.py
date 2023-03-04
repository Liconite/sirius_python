import sys
import os

if len(sys.argv) != 3:
    sys.exit(1)

path = sys.argv[1]
folder_name = sys.argv[2]

folder_path = os.path.join(path, folder_name)
try:
    os.mkdir(folder_path)
except OSError as e:
    print(f"Error creating folder: {e}")
