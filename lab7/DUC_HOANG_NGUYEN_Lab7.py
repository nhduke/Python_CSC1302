# Lab 07: Selection Sort and Insertion Sort with Swap Count

def selection_sort(s, isAscending = True):
    arr = list(s)
    n = len(arr)
    swaps_count = 0

    # TODO: Implement selection sort algorithm with swap count
    if isAscending:
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            if min_index != i:
                swaps_count += 1
                arr[i], arr[min_index] = arr[min_index], arr[i]
    else:
        for i in range(n - 1):
            max_index = i
            for j in range(i + 1, n):
                if arr[j] > arr[max_index]:
                    max_index = j
            if max_index != i:
                swaps_count += 1
                arr[i], arr[max_index] = arr[max_index], arr[i]

                
    return "".join(arr), swaps_count


def insertion_sort(s, isAscending = True):
    arr = list(s)
    n = len(arr)
    swaps_count = 0

    # TODO: Implement insertion sort algorithm with swap count
    if isAscending:
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            
            while j >= 0 and key < arr[j]:
                swaps_count += 1
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    else:
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            
            while j >= 0 and key > arr[j]:
                swaps_count += 1
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        
        
    return "".join(arr), swaps_count

# Test cases
if __name__ == "__main__":
    RED_code = "\033[91m"
    GREEN_code = "\033[92m"
    END_code = "\033[0m"
    print("\n-- Selection Sort --")
    t = "dcba"                      # default ascending (missing param -> ascending)
    print(f"Input: {t}, Expected: ('abcd', 2),  Got: {GREEN_code if selection_sort(t) == ('abcd', 2) else RED_code}{selection_sort(t)}{END_code}")
    t = "badc"                      # explicit ascending=True
    print(f"Input: {t}, Expected: ('abcd', 2),  Got: {GREEN_code if selection_sort(t, True) == ('abcd', 2) else RED_code}{selection_sort(t, True)}{END_code}")
    t = "abcd"                      # descending
    print(f"Input: {t}, Expected: ('dcba', 2),  Got: {GREEN_code if selection_sort(t, False) == ('dcba', 2) else RED_code}{selection_sort(t, False)}{END_code}")

    print("\n-- Insertion Sort --")
    t = "dcba"                      # default ascending
    print(f"Input: {t}, Expected: ('abcd', 6),  Got: {GREEN_code if insertion_sort(t) == ('abcd', 6) else RED_code}{insertion_sort(t)}{END_code}")
    t = "badc"                      # explicit ascending=True
    print(f"Input: {t}, Expected: ('abcd', 2),  Got: {GREEN_code if insertion_sort(t, True) == ('abcd', 2) else RED_code}{insertion_sort(t, True)}{END_code}")
    t = "abcd"                      # descending
    print(f"Input: {t}, Expected: ('dcba', 6),  Got: {GREEN_code if insertion_sort(t, False) == ('dcba', 6) else RED_code}{insertion_sort(t, False)}{END_code}")