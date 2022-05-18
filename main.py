import os
import sys
from pathlib import Path
from extensions import extensions


main_path = Path('D:/test')


def get_listdir(path: Path) -> list:
    listdir = [str(child) for child in path.iterdir()]
    return listdir


def create_folders_from(path: Path, folder_names: list) -> None:
    for folder in folder_names:
        folder = str(folder)
        if not Path.exists(Path(path, folder)):
            Path.mkdir(Path(path, folder))


def get_subfolder_path(path: Path) -> list:
    subfolder_path = []
    for child in path.glob('*'):
        if child.is_dir():
            subfolder_path.append(child)
    return subfolder_path


print(get_subfolder_path(main_path))
