from pathlib import Path

for path, dirs, files in Path("../").walk():
    print(path, dirs, files)
