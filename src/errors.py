import sys

from termcolor import colored


def raise_error_pwd_not_specified():
    msg = """ERROR: present-working-directory not specified.\n\nThis should not occur, if you use the script correctly. Please run it via the entrypoint `bin/run.sh`!"""
    print(colored(msg, "red"))
    sys.exit()


def raise_error_no_template_name_specified():
    msg = "ERROR: No template name specified."
    print(colored(msg, "red"))
    sys.exit()


def raise_error_invalid_template_name(template_name):
    msg = f"ERROR: Invalid template name \"{template_name}\"."
    print(colored(msg, "red"))
    sys.exit()


def raise_error_project_path_exists(path_to_project):
    msg = f"ERROR: The path \"{path_to_project}\" already exists."
    print(colored(msg, "red"))
    sys.exit()
