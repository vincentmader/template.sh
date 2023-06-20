#!/bin/sh

# Define path to python executable (in virtual environment).
  PYTHON3="../.venv/bin/python3"

# Get name of template from CLI argument.
  TEMPLATE_NAME="$1"

# Get name of project from CLI argument.
# This is the target directory for `git pull`, if specified.
  PROJECT_NAME="$2"

# Get path to present working directory.
# This is used to make sure the repo is cloned into the correct relative directory.
  PRESENT_WORKING_DIRECTORY="$(pwd)"

# Define path to this script (needed when calling script from elsewhere).
  PATH_TO_RUN_SCRIPT="$(realpath "$0")"
  PATH_TO_RUN_SCRIPT="$(dirname "$PATH_TO_RUN_SCRIPT")"
  PATH_TO_REPO="$(realpath "$PATH_TO_RUN_SCRIPT/..")"

# Execute main python entrypoint.
  cd "$PATH_TO_REPO/src" && "$PYTHON3" ./main.py "$PRESENT_WORKING_DIRECTORY" "$TEMPLATE_NAME" "$PROJECT_NAME"
