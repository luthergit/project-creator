def name_of_project(project_name):
    return project_name

def location_of_folder(folder_location):
    return folder_location

def creating_venv(venv):
    venv
    pass

def start_project_in_new_folder():
    pass





def main():
    print("What is the name of your project?")
    project_name = input()
    print(f"Creating {project_name}...")
    folder_location = input("What folder would you like this project to be in?\n")
    print(f"Great! {project_name} will be stored in {folder_location}...")

    print('\nCreating Virtual Environment\n')
    venv = input('What python version do you want: ')
    print(f"Using python version {venv}.")

    # Final step: Start project in the newly craeted folder




if __name__ == "__main__":
    main()
