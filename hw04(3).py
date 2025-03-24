import sys
import os
from pathlib import Path
from colorama import init, Fore, Style 

init(autoreset=True)

def print_directory_structure(directory, indent=""):
    try:
        items = sorted(Path(directory).iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))

        for item in items:
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                print_directory_structure(item, indent + " ┃ ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

    except PermissionError:
        print(f"{indent}{Fore.RED}Access denied: {directory}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{indent}{Fore.RED}Error: {e}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python {sys.argv[0]} /path/to/directory{Style.RESET_ALL}")
        sys.exit(1)

    directory = Path(sys.argv[1])

    if not directory.exists() or not directory.is_dir():
        print(f"{Fore.RED}The specified path does not exist or is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.CYAN}Directory structure: {directory}{Style.RESET_ALL}")
    print_directory_structure(directory)

if __name__ == "__main__":
    main()
