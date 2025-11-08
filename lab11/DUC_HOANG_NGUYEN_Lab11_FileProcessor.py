import os
import csv

# ------------------- TASK 1: Creating the Module -------------------
### Create a module named FileProcessor.py with the following functions:

def merge(file1_path, file2_path, result_path):
    """
    Merges the contents of two text files into one result file.
    The result should contain the contents of file1 followed by file2.
    Handle exceptions gracefully.
    """
    # TODO: Implement this function
    try:
        with open(file1_path, 'r') as file1:
            content1 = file1.read()

        with open(file2_path, 'r') as file2:
            content2 = file2.read()

        with open(result_path, 'w') as result:
            result.write(content1)
            result.write('\n')
            result.write(content2)
            print(f"Files merged successfully into '{result_path}'.")

    except FileNotFoundError as e:
        print(f"Error: One or both input files were not found. ({e})")

    except PermissionError as e:
        print(f"Error: Permission denied while accessing files. ({e})")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def duplicate(file_path):
    """
    Creates a copy of the file in the same directory with "_copy" added
    to the filename. Handle exceptions gracefully.
    """
    # TODO: Implement this function
    
    try:
        if not os.path.isfile(file_path):
            print(f"Error: File '{file_path}' does not exist.")
            return


        base, ext = os.path.splitext(file_path)
        copy_path = f"{base}_copy{ext}"
 
        

        with open(file_path,'r') as file:
            content = file.read()
            
        with open(copy_path, "w") as f:
            f.write(content)
            
        print(f"File duplicated successfully as '{copy_path}'.")

    except PermissionError as e:
        print(f"Error: Permission denied while accessing files. ({e})")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
            


def convert_to_csv(text_file_path, csv_file_path):
    """
    Converts a given text file into a CSV file.
    Each word in the text file should become a cell in the CSV.
    Handle exceptions gracefully.
    """
    # TODO: Implement this function 
    try:
        with open(text_file_path, 'r') as text_file:
            lines = text_file.readlines()

        data = [line.strip().split() for line in lines]

        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)

        print(f"File successfully converted to CSV: '{csv_file_path}'")

    except FileNotFoundError as e:
        print(f"Error: The text file was not found. ({e})")

    except PermissionError as e:
        print(f"Error: Permission denied while accessing files. ({e})")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def print_file_statistics(file_path):
    """
    Prints the total number of lines and words in the given text file.
    If the file is empty, print "Warning: The file is empty."
    Handle exceptions gracefully.
    """
    # TODO: Implement this function

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if not lines:
            print("The file is empty.")
            return

        total_lines = len(lines)
        total_words = sum(len(line.split()) for line in lines)

        print(f'Statistic of file: {file_path}')
        print(f"Total lines: {total_lines}")
        print(f"Total words: {total_words}")

    except FileNotFoundError as e:
        print(f"Error: The file '{file_path}' was not found. ({e})")

    except PermissionError as e:
        print(f"Error: Permission denied while accessing '{file_path}'. ({e})")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    


