import sys
from pathlib import Path
from colorama import Fore, init

def visualize_directory_structure(directory_path: str):
    """
    Visualizes the directory structure using colors to distinguish files and folders.

    Input:
    :param directory_path: string     Path to the directory.
    """
    init(autoreset=True)  # Initializing colorama

    directory = Path(directory_path)

    if not directory.exists():
        print(Fore.RED + f"Error: Directory '{directory_path}' does not exist.")
        return

    if not directory.is_dir():
        print(Fore.RED + f"Error: '{directory_path}' is not a directory.")
        return

    def _visualize(path, prefix=''):
        #Recursive function for traversing a directory.
        items = list(path.iterdir())
        for index, item in enumerate(items):
            if item.is_dir():
                print(prefix + Fore.BLUE + item.name + '/')
                _visualize(item, prefix + '    ')
            else:
                print(prefix + Fore.GREEN + item.name)

    print(Fore.CYAN + directory.name + '/')
    _visualize(directory, '    ')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Using: python color.py <directory_path>")
    else:
        directory_path: str = sys.argv[1]
        visualize_directory_structure(directory_path)