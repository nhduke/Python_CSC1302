# Lab 08 (Exam 01)
# Sort the People
# Given an array of strings names and an array heights that consists of distinct positive integers, both of length n.
# Sort people by their heights in descending order and return an array of names sorted accordingly.
# You need to implement your own sorting algorithm to solve this problem. 
#                               >>> DO NOT USE THE BUILT-IN SORT FUNCTION. <<<
# You need to select a sorting algorithm that has a time complexity of O(n log n) or better.
# You will be graded based on correctness (60%) and efficiency (40%).


def mergeDescending(arr, left, mid, right):
    mergedSize = right - left + 1
    mergedArr = [0] * mergedSize
    
    i = left
    j = mid + 1
    k = 0
    
    while i <= mid and j <= right:
        if arr[i] > arr[j]:
            mergedArr[k] = arr[i]
            i += 1
        else:
            mergedArr[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        mergedArr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        mergedArr[k] = arr[j]
        j += 1
        k += 1
    
    k = 0
    while k < mergedSize:
        arr[left + k] = mergedArr[k]
        k += 1
        
def merge_sort(arr,  left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr,mid + 1, right)
        
        mergeDescending(arr, left, mid, right)
        
        
def sort_people(names: list[str], heights: list[int]) -> list[str]:
    sorted_names:list[str] = []
    # TODO: Implement the function to sort names based on heights in <descending> order.
    # IMPLEMENT YOUR OWN SORTING ALGORITHM HERE
    
    #use merge sort
    mappedIndex = {}
    for i in range(len(names)):
        mappedIndex[heights[i]] = names[i]
        
    merge_sort(heights, 0, len(heights) - 1)
    
    for i in range(len(heights)): #iterate through the sorted height array
        sorted_names.append(mappedIndex[heights[i]])

    return sorted_names










# ---------------------------------------------------------------- #
# ---------- DO NOT MODIFY ANYTHING BELOW THIS LINE -------------- #
# ---------------------------------------------------------------- #
if __name__ == "__main__":
    import zipfile
    RED_code = "\033[91m"
    GREEN_code = "\033[92m"
    END_code = "\033[0m"
    with zipfile.ZipFile(f"data.zip", "r") as z:
        z.extractall()
        files = z.namelist()
        file_dict = {file: z.read(file).decode('utf-8') for file in files}
    for n in ['7', '15', '20', '40']:
        names = file_dict[f"n{n}_names.txt"].splitlines()
        heights = file_dict[f"n{n}_heights.txt"].splitlines()
        expected = file_dict[f"n{n}_expected.txt"].splitlines()
        result = sort_people(names, heights)
        if result == expected:
            print(f"Test case n={n}: {GREEN_code}Passed{END_code}")
        else:
            print(f"Test case n={n}: {RED_code}Failed{END_code}")
            print(f"  Input: ({names}, {heights})")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")