import time

class Mother:
    def __init__(self, name = "A"):
        self.greet = "hello"
        self.name = name
    def greeting(self):
        print("This is mother")

class Child(Mother):
    def __init__(self):
        super().__init__('B')
        self.age = 10
    def greetAge(self):
        print(self.greet)
        print(self.name)
        print(self.age)
        self.greeting()
        
# Classes and Inheritence
# newChild = Child()
# newChild.greeting()
# newChild.greetAge()

#Search and Recursion

def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            high = mid - 1
        if arr[mid] < target:
            low = mid + 1
    return None

def fibonacy(n):
    if n <= 1:
        return n
    else:
        return fibonacy(n-1) + fibonacy(n-2)

fibDict = {}
def fibonancyMem(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        if n in fibDict.keys():
            return fibDict[n]
        else:
            temp = fibonancyMem(n-1) + fibonancyMem(n-2)
            fibDict[n] = temp
            return temp

def palindrome(s):
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])
    
def intToBinary(n):
    if n <= 0:
        return
    else:
        a = n // 2
        b = n % 2
        return str(b) + intToBinary(a)
    
def intToHex(n):
    hexDict = {
        1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9',
        10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'
    }
    if n <= 0:
        return
    else:
        a = n // 16
        b = n % 16
        return hexDict[b] + intToHex(a)
    
def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        minIndex = -1
        for j in range(i + 1, n):
            if arr[minIndex] > arr[j]:
                minIndex = j
        if arr[i] > arr[minIndex]:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2 
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)      
        
             
             
            
            
                
                
        


start_time = time.time()
print(num_paths_memo(15,14))
end_time = time.time()

print(f"Elapsed time (memoization): {end_time - start_time} seconds")