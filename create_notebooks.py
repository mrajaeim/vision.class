import os
import shutil
from pathlib import Path


def struct_name(season_num, notebook_num, file_name):
    return f"s{int(season_num)}-{int(notebook_num)}_{file_name.lower()}.ipynb"

# CHANGE
season_num = 8
dir_path = Path(f"./notebooks/s{season_num}")
starter_file = "./starter.ipynb"
# CHANGE
start_notebook_num = 1

# CHANGE (just text of file name)
files = [
]

if not dir_path.is_dir():
    os.makedirs(dir_path, exist_ok=True)

for idx, file in enumerate(files):
    shutil.copyfile(starter_file, dir_path / struct_name(season_num, start_notebook_num + idx, file))