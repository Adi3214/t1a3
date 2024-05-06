# Simple File Organizer

## Introduction
Simple File Organizer is a Python-based terminal application that helps users to organize their files in a specified directory by sorting them into folders based on file type or modification date. This tool is designed to enhance file management efficiency directly from the command line.

## Features

### Feature 1: Sorting by File Type
- **Description**: This feature sorts files into folders named after their file extensions.
- **Logic**:
  1. The application scans all files in the specified directory.
  2. It extracts the file extension from each file name.
  3. If a folder with the extension name does not exist, it creates one.
  4. The file is then moved into the corresponding folder based on its extension.

### Feature 2: Sorting by Modification Date
- **Description**: This feature organizes files by their last modification dates into corresponding folders.
- **Logic**:
  1. The application reads the modification date for each file.
  2. Converts the modification timestamp to a more readable date format (`YYYY-MM-DD`).
  3. If a folder with that date does not exist, it creates one.
  4. Files are then moved into the folder that matches their modification date.

### Feature 3: User Interaction and Input Validation
- **Description**: Users are interactively asked for their name, the directory to sort, and the type of sorting they prefer.
- **Logic**:
  1. Prompt the user to input their name and greet them.
  2. Ask for the directory they wish to organize.
  3. Validate the existence of the directory to prevent errors.
  4. Provide options for sorting (by type or date) and execute the chosen method.

## Installation Instructions
1. Ensure Python 3 is installed on your system.
2. Download the application files from the repository.
3. No additional libraries are required, as only built-in Python modules are used.

## Git Repo link 
https://github.com/Adi3214/t1a3

## Usage
To use the application, navigate to the directory containing the script and run:
```bash
python3 main.py

