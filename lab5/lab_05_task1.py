"""
    Implement the iterative binary search method to search for the target word within the words list and print the result in the following format from inside the method- 
	
	Target = {target} , Found at index = {index}, Number of iterations = {iterations}

Notes: 
- You will need to keep track of how many iterations/steps it takes to find the result (iterations).
- If a word is not found within the list, the function should return -1.
- You will need to put your python script (.py) and the provided ‘words.txt’ in the same folder

"""

file = open('words.txt', 'r')
words = file.read().splitlines()
print('Number of words read:', len(words))

def binary_search(arr, target):
    # Implement iterative binary search here
    # print(f"Target = {target} , Found at index = {index}, Number of iterations = {iterations}")

    indexNum = -1
    iterations = 0
    low = 0
    high = len(arr)

    while low < high:
        iterations += 1
        mid = (low + high) // 2
        
        if target in arr[low:mid]:
            high = mid
            if indexNum == -1:
                indexNum = 1
        elif target in arr[mid:high]:
            low = mid
            if indexNum == -1:
                indexNum = 1
            
        if target == arr[low]:
            indexNum = low
            break
        elif target == arr[high - 1]:
            indexNum = high - 1
            break
        elif indexNum == -1:
            break
        
        
    print(f'Target = {target}, Found at index = {indexNum}, Number of iterations = {iterations}')
    return 


target = input('Enter search key: ').lower()

while target != 'exit':
    binary_search(words, target)
    target = input('Enter search key: ').lower()
