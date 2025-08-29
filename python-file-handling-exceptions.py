"""
File Handling and Exception Handling Assignment
Author: Ojobor Jude Ikechukwu

Description:
------------
This program demonstrates:
1. File Reading & Writing
2. Error Handling with try-except blocks
3. Clean and robust Python coding practices

Tasks:
🖋️ File Read & Write Challenge:
   - Reads the content of a file
   - Writes a modified version of the content into a new file

🧪 Error Handling Lab:
   - Asks the user for a filename
   - Handles errors if the file doesn’t exist or cannot be read
"""

def read_and_modify_file():
    """Reads a file provided by the user and writes its modified content into a new file."""
    try:
        # Ask user for the filename
        filename = input("Enter the filename to read: ")

        # Open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (for demo, convert text to uppercase)
        modified_content = content.upper()

        # Define a new file name for the modified content
        new_filename = "modified_" + filename

        # Write modified content into a new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"File has been read successfully and modified version saved as '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file you entered does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You don't have rights to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("File Handling & Exception Handling Program")
    print("------------------------------------------------")
    read_and_modify_file()
