# Project Setup Utility

A command-line utility that automates Python project setup, creating organized directory structures, virtual environments using `uv`, and optional executable installer scripts.

## Features

- Creates a new project directory in your Documents folder
- Sets up a Python virtual environment using `uv`
- Creates an optional executable installer script
- Supports specifying Python version for the virtual environment

## Requirements

- Python 3.10+
- `uv` tool installed (for virtual environment creation)

## Usage

Run the script from the command line:

```bash
python main.py
```

The script will prompt you for:

1. Project name
2. Directory name (folder will be created in your Documents directory)
3. Python version for the virtual environment
4. Whether you want to create an installer script

## How It Works

1. You provide a project name and folder location
2. The script creates the project directory in your Documents folder
3. It sets up a virtual environment using `uv` with your specified Python version
4. Optionally, it creates an executable installer script that can run your project

## Creating an Installer

If you choose to create an installer:

1. The script will prompt for an installer name
2. It will create an executable bash script that runs your main.py file with the correct Python interpreter path
3. The installer will be made executable with `chmod +x`

## Example

```
$ python main.py
What is the name of your project?
my_awesome_project
Creating my_awesome_project...

What is the folder name?
Folder will be created here in the home directory under Documents
python_projects
Great! my_awesome_project will be stored in /home/user/Documents/python_projects...

Project directory created: /home/user/Documents/python_projects/my_awesome_project

What python version do you want: 
3.11

Creating Virtual Environment
Successfully created uv virtual environment with Python 3.11

To activate the environment, run:
source .venv/bin/activate
Using python version 3.11.

Do you want to create an installer? (y/n): y
What's your installer name? : run_project

Project directory created: /home/user/Documents/python_projects/my_awesome_project

After this script finishes, run this command to change to the project directory:
/home/user/Documents/python_projects/my_awesome_project
```

## Notes

- The script uses the modern `pathlib.Path` for file path handling
- It checks for empty input and prompts again if necessary
- The virtual environment is created in the project directory
- When the script completes, it provides instructions for navigating to your new project directory