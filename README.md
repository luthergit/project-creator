# Project Setup Utility

A command-line utility that automates Python project setup, creating organized directory structures, virtual environments using `uv`, and optional executable installer scripts.

## Features

- Creates a new project directory in your Documents folder
- Sets up a Python virtual environment using `uv`
- Creates an optional executable installer script
- Supports specifying Python version for the virtual environment

## Requirements

### Local Installation
- Python 3.10+
- `uv` tool installed (for virtual environment creation)

### Docker (Alternative)
- Docker and Docker Compose installed
- No local Python installation required

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

## Docker Support

This project includes Docker support for a consistent development environment:

### Dockerfile

```dockerfile
# Start with the official Python 3.13 image
FROM python:3.13
# Set working directory inside container
WORKDIR /app
# Copy all files from current directory to /app in container
COPY . .
# Install uv (ultra-fast Python package installer)
RUN pip install uv
# Synchronize Python dependencies using uv
RUN uv sync
# Install zsh with powerline10k theme using a popular installation script
# This adds a more feature-rich shell with better prompts and colors
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.2.1/zsh-in-docker.sh)"
# Install vim text editor
RUN apt install vim -y
# Default command to run when container starts (overridden by docker-compose)
CMD ["zsh"]
```

### Docker Compose

```yaml
services:  # Top-level key: defines all containers in this app
  app:     # Name of your service (can be anything)
    command: sh -c "zsh"  # Overrides the default CMD in Dockerfile
    tty: true             # Allocates a terminal for interactivity
    stdin_open: true      # Keeps STDIN open (required for interactive shells)
    build:
      context: .          # Builds from the current directory
      dockerfile: Dockerfile  # Uses this Dockerfile
```

### Running with Docker

```bash
# Build and start the container with an interactive ZSH shell
docker-compose up

# (Optional) To open additional terminal sessions to the running container:
# docker-compose exec app zsh

# Run the setup script inside the container
python main.py

# When finished, press Ctrl+C to stop the container
# Or run this in another terminal to stop it:
# docker-compose down
```