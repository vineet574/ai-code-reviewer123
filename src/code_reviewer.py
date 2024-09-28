import os
import subprocess

def check_code_with_flake8(file_path):
    """Runs flake8 on a Python file to check for style issues."""
    print(f"Checking {file_path} with Flake8...")
    result = subprocess.run(['flake8', file_path], capture_output=True, text=True)
    
    if result.stdout:
        print("Issues found:")
        print(result.stdout)
    else:
        print("No issues found! Your code looks good.")

def format_code_with_autopep8(file_path):
    """Automatically formats the Python file using autopep8."""
    print(f"Formatting {file_path} with autopep8...")
    subprocess.run(['autopep8', '--in-place', file_path])
    print(f"{file_path} has been formatted.")

def main():
    # Path to the Python file you want to review
    file_to_check = input("Enter the path of the Python file to review: ")

    # Check if the file exists
    if not os.path.isfile(file_to_check):
        print("File not found!")
        return

    # Run Flake8 to check for issues
    check_code_with_flake8(file_to_check)
    
    # Format the file with autopep8
    format_code_with_autopep8(file_to_check)

if __name__ == "__main__":
    main()
