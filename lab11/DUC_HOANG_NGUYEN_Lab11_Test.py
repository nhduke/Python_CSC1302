
# ------------------- Task 2: Testing -------------------
### Create a separate script named lab11_test.py to test the functions in FileProcessor.py.

from DUC_HOANG_NGUYEN_Lab11_FileProcessor import merge, duplicate, convert_to_csv, print_file_statistics

def main():
    file1 = "file1.txt"
    file2 = "file2.txt"
    merged_output = "result.txt"
    csv_output = "result.csv"

    print("=== Testing merge() ===")
    #TODO: Merge file1 and file2 into merged_output
    merge(file1,file2,merged_output)

    print("\n=== Testing duplicate() ===")
    #TODO: Duplicate file1
    duplicate(file1)

    print("\n=== Testing convert_to_csv() ===")
    #TODO: Convert file2 to csv_output
    convert_to_csv(file2, csv_output)

    print("\n=== Testing print_file_statistics() ===")
    #TODO: Print statistics for file1 and merged_output
    print_file_statistics(file1)
    print_file_statistics(merged_output)

    # Deliberate error cases
    print("\n=== Testing Error Handling ===")
    merge("missing1.txt", "file2.txt", "output.txt")
    duplicate("nonexistent.txt")
    convert_to_csv("missing.txt", "output.csv")
    print_file_statistics("nofile.txt")


if __name__ == "__main__":
    main()
