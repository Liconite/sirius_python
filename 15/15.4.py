import sys
import os

if len(sys.argv) != 2:
    sys.exit(1)

filename = sys.argv[1]

if not os.path.isfile(filename):
    sys.exit(1)

with open(filename) as f:
    for line in f:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        print(line)
        os.system(line)
