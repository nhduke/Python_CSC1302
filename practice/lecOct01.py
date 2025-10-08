def selectionSort(arr):
    for i in range(len(arr)):
        min = max(arr)
        minIndex = -1
        for j in range(i + 1, len(arr)):
            if min > arr[j]:
                min = arr[j]
                minIndex = j
        if arr[i] > min:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def insertionSort(arr):
    for i in range(1, len(arr)):
        dummy = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > dummy:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = dummy
        print(arr)
    return arr


arr = [5,7,1,4,23,55,11,52,8, 3]

print(insertionSort(arr))
        

            