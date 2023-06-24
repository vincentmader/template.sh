import sys

import config as cfg
from termcolor import colored


def raise_error_pwd_not_specified():
    msg = """\nERROR: present-working-directory not specified.\n\nThis should not occur, if you use the script correctly. Please run it via the entrypoint `bin/run.sh`!"""
    print(colored(msg, "red"))
    sys.exit()


def raise_error_no_template_name_specified():
    msg = "\nERROR: No template name specified."
    msg += "\nTry using one of the options listed below:"
    msg = colored(msg, "red")

    for k, v in cfg.TEMPLATES.items():
        row = f"\n{k}{(16 - len(k))*' '}{v}"
        msg += colored(row, "yellow")

    print(colored(msg, "red"))
    sys.exit()


def raise_error_invalid_template_name(template_name):
    msg = f"\nERROR: Invalid template name \"{template_name}\"."
    print(colored(msg, "red"))
    sys.exit()


def raise_error_project_path_exists(path_to_project):
    msg = f"\nERROR: The path \"{path_to_project}\" already exists."
    print(colored(msg, "red"))
    sys.exit()
