# Cursor AI Experiments

This repository contains a collection of Python programs created to experiment with Cursor AI capabilities.

## Contents

1. **Hello World Program**
   - `hello_robo.py`: A simple function that prints a message
   - `main.py`: Demonstrates how to import and use the function from another file

2. **Directory Scanner**
   - `directory_scanner.py`: A command-line utility that:
     - Prompts for a directory path
     - Lists all files and folders in the specified directory
     - Shows file sizes in human-readable format (B, KB, MB, GB)
     - Handles various error cases (non-existent paths, permission issues, etc.)
   
   - `directory_scanner_gui.py`: A GUI version of the directory scanner that:
     - Provides a user-friendly interface
     - Shows results in a scrollable text area
     - Displays error messages in popup dialogs
     - Maintains the same functionality as the command-line version

## Usage

1. For the Hello World program:
   ```bash
   python main.py
   ```

2. For the Directory Scanner:
   - Command-line version:
     ```bash
     python directory_scanner.py
     ```
     Then enter the path to the directory you want to scan when prompted.

   - GUI version:
     ```bash
     python directory_scanner_gui.py
     ```
     Enter the path in the text field and click "Scan Directory" button.

## Requirements

- Python 3.x
- Tkinter (usually comes with Python installation)
- No additional packages required
