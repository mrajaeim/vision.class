import os
import shutil
from pathlib import Path


def struct_name(snum, fnum, fname):
    return f"s{int(snum)}-{int(fnum)}_{fname.lower()}.ipynb"

# CHANGE
snum = 8
dir_path = Path(f"./notebooks/s{snum}")
starter_file = "./starter.ipynb"
# CHANGE
start_fnum = 1

# CHANGE (just text of file name)
files = [
]

if not dir_path.is_dir():
    os.makedirs(dir_path, exist_ok=True)

for idx, file in enumerate(files):
    shutil.copyfile(starter_file, dir_path / struct_name(snum, start_fnum + idx, file))