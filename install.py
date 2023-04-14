import os
import re

def prompt_user_for_db_config():
    print("Enter your PostgreSQL server configuration:")
    name = input("Database name: ")
    user = input("User: ")
    password = input("Password: ")
    host = input("Host: ")
    port = input("Port: ")

    return {
        'NAME': name,
        'USER': user,
        'PASSWORD': password,
        'HOST': host,
        'PORT': port,
    }

def install_local_postgres():
    print("Installing local PostgreSQL server...")
    # Add the code to install a local PostgreSQL server here
    # You can use subprocess to call the necessary commands
    # You may also need to create a new PostgreSQL user and database
    pass

def update_settings_db_config(db_config):
    settings_file = 'settings.py'
    with open(settings_file, 'r') as file:
        settings_contents = file.read()

    for key, value in db_config.items():
        settings_contents = re.sub(f'{key.upper()}_HERE', value, settings_contents)

    with open(settings_file, 'w') as file:
        file.write(settings_contents)

if __name__ == '__main__':
    print("Please choose an option:")
    print("1. Configure an external PostgreSQL server")
    print("2. Install a local PostgreSQL server")

    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        db_config = prompt_user_for_db_config()
    elif choice == 2:
        install_local_postgres()
        db_config = {
            'NAME': 'your_local_db_name',
            'USER': 'your_local_user',
            'PASSWORD': 'your_local_password',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    else:
        print("Invalid choice. Exiting.")
        exit(1)

    update_settings_db_config(db_config)
    print("Database configuration updated successfully.")
