import os
import subprocess
from pathlib import Path
from typing import Tuple


def name_of_project(project_name: str) -> str:
    while not project_name:
        project_name = input('Project name cannot be blank, please enter a project:\n')
    return project_name


def location_of_folder(folder_name: str) -> Tuple[Path, str]:
    while not folder_name:
        folder_name = input('Please provide the directory name:\n')

    # Use Path objects consistently
    home_dir = Path.home()
    documents_path = home_dir / "Documents"
    folder_path = documents_path / folder_name
    
    return folder_path, folder_name


def create_uv_venv(python_version: str) -> bool:
    # Create a virtual environment using uv with specified Python version
    try:
        subprocess.run(["uv", "venv", "--python", python_version], check=True)
        print(f"Successfully created uv virtual environment with Python {python_version}")
        
        print("\nTo activate the environment, run:")
        print("source .venv/bin/activate")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to create virtual environment: {e}")
        return False


def start_project_in_new_folder(folder_path: Path, project_name: str) -> None:
    project_dir = folder_path / name_of_project(project_name)
    
    # Create the directory
    project_dir.mkdir(exist_ok=True, parents=True)
    
    print(f"Project directory created: {project_dir}")

    # Change to the directory (convert Path to string)
    os.chdir(str(project_dir))

    return project_dir

def create_installer(original_dir: str | Path):
    create_choice = input("Do you want to create an installer? (y/n): ").lower()
    if create_choice != 'y' and create_choice != 'yes':
        return  # Exit the function if user doesn't want to create installer
    
    install_name = input("What's your installer name? : ")
    curr_dir = os.getcwd()

    # Use the original directory to find main.py
    main_py_path = Path(original_dir) / "main.py"


    bash_tag = "#!/bin/bash"
    script_content = f"{curr_dir}/.venv/bin/python {main_py_path}"
    install_file = Path(curr_dir) / install_name

    with open(install_file, 'w') as f:
        f.write(f"{bash_tag}\n")
        f.write(f"{script_content}\n")
    subprocess.run(["chmod", "+x", install_file])
    

def main():
    original_dir = os.getcwd()  # Store where the script was initially run
    print("What is the name of your project?\n")
    project_name = name_of_project(input())
    print(f"Creating {project_name}...\n")
    
    folder_path, folder_name = location_of_folder(input("What is the folder name?\nFolder will be created here in the home directory under Documents\n"))
    print(f"Great! {project_name} will be stored in {folder_path}...\n")

    # Create and change to project directory
    projectdir = start_project_in_new_folder(folder_path, project_name)

    # Now we're in the correct directory, create the virtual environment
    python_version = input('What python version do you want: ')
    print('\nCreating Virtual Environment\n')
    create_uv_venv(python_version)
    print(f"Using python version {python_version}.")

    create_installer(original_dir)

    print(f"Project directory created: {projectdir}")
    print(f"\nAfter this script finishes, run this command to change to the project directory:")
    print(f"{projectdir}")
    



if __name__ == "__main__":
    main()
    
