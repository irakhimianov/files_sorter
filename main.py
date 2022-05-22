import sys
from extensions import extensions
from pathlib import Path
from time import time


def get_listdir(path: Path) -> list:
    listdir = [str(child) for child in path.iterdir()]
    return listdir


def create_folders_from(path: Path, folder_names: list) -> None:
    for folder in folder_names:
        folder = str(folder)
        if not Path.exists(Path(path, folder)):
            Path.mkdir(Path(path, folder))


def create_uniq_filename(prefix: str, suffix: str) -> str:
    return f"{prefix}-{str(int(time() * 100))}.{suffix}"


def get_subfolders_path(path: Path) -> list:
    subfolders_path = []
    for child in path.glob('*'):
        if child.is_dir():
            subfolders_path.append(child)
    return subfolders_path


def get_files_path(path: Path) -> list:
    files_path = []
    for child in path.glob('*.*'):
        if child.is_file():
            files_path.append(child)
    return files_path


def get_file_names(path: Path) -> list:
    file_names = []
    for child in path.glob('*.*'):
        if child.is_file():
            file_names.append(child.name)
    return file_names


def sort_files(path: Path) -> None:
    files = get_file_names(path)
    extensions_list = list(extensions.items())
    for file in files:
        file_extension = Path(file).suffix[1:].lower()
        file_name = Path(file).name

        for val in extensions_list:
            if file_extension in val[1]:
                print(f"Moving {file_name} in {val[0]} folder")
                Path.rename(Path(path, file), Path(path, val[0], file_name))


def remove_empty_folders(path: Path) -> None:
    subfolders_path = get_subfolders_path(path)
    for subfolder in subfolders_path:
        if next(Path(subfolder).iterdir(), None) is None:
            print(f"Deleting empty folder: {subfolder}")
            Path.rmdir(subfolder)


if __name__ == "__main__":
    if sys.argv[1:]:
        main_path = Path('\\'.join(folder for folder in sys.argv[1:]))
    else:
        main_path = Path('D:\\test')

    create_folders_from(main_path, extensions)
    sort_files(main_path)
    remove_empty_folders(main_path)
