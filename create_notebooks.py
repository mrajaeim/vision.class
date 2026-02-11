import shutil
from pathlib import Path

def struct_name(snum, fnum, fname):
    return f"s{int(snum)}-{int(fnum)}_{fname.lower()}.ipynb"

snum = 6
dir_path = Path(f"./notebooks/s{snum}")
starter_file = "./starter.ipynb"
start_fnum = 1

files = [
]

for idx, file in enumerate(files):
    shutil.copyfile(starter_file, dir_path / struct_name(snum, start_fnum + idx, file))