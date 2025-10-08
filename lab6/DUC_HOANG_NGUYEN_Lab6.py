def find_peak_index(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid
        elif arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]:
            right = mid - 1
        elif arr[mid] < arr[mid + 1] and arr[mid] > arr[mid - 1]:
            left = mid + 1
            
        

arr1 = [0, 1, 0]
print(f'Array: {arr1}, Expected: 1, Got: {find_peak_index(arr1)}')
arr2 = [0, 10, 5, 2]
print(f'Array: {arr2}, Expected: 1, Got: {find_peak_index(arr2)}')
arr3 = [3, 5, 7, 9, 11, 8, 6, 4, 2]
print(f'Array: {arr3}, Expected: 4, Got: {find_peak_index(arr3)}')
