import os
from pathlib import Path

from termcolor import colored

import config as cfg
import errors


def get_present_working_directory_from_cli_args():
    if len(cfg.CLI_ARGS) <= 1:
        errors.raise_error_pwd_not_specified()
    present_working_directory = cfg.CLI_ARGS[1]
    return present_working_directory


def get_template_name_from_cli_args():
    if len(cfg.CLI_ARGS) <= 2:
        errors.raise_error_no_template_name_specified()
    template_name = cfg.CLI_ARGS[2]
    if template_name not in cfg.TEMPLATES:
        errors.raise_error_invalid_template_name(template_name)
    return template_name


def get_project_name_from_cli_args():
    if len(cfg.CLI_ARGS) <= 3:
        return None
    project_name = cfg.CLI_ARGS[3]
    return project_name


def get_path_to_project_from_project_name(project_name):
    present_working_directory = get_present_working_directory_from_cli_args()
    project_name = project_name if project_name else "NEW_PROJECT"
    path = Path(present_working_directory, project_name)
    return path


def pull_template_from_github(template_name, path_to_project):
    template_repo = cfg.TEMPLATES[template_name]
    msg = f"Cloning template \"{template_name}\" from \"{template_repo}\" into \"{path_to_project}\"..."
    print(colored(msg, "green"))
    if os.path.exists(path_to_project):
        errors.raise_error_project_path_exists(path_to_project)
    cmd = f"git clone \"{template_repo}\" \"{path_to_project}\""
    os.system(cmd)


def reset_git_origin_of_cloned_template(path_to_project):
    msg = f"Removing remote \"origin\" from cloned git repository."
    print(colored(msg, "yellow"))
    cmd = f"cd \"{path_to_project}\" && git remote remove origin"
    os.system(cmd)


def main():
    template_name = get_template_name_from_cli_args()
    project_name = get_project_name_from_cli_args()
    path_to_project = get_path_to_project_from_project_name(project_name)
    pull_template_from_github(template_name, path_to_project)
    reset_git_origin_of_cloned_template(path_to_project)


if __name__ == "__main__":
    main()
