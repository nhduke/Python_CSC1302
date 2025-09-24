"""
    Implement the iterative linear search method to search for the target word within the words list and print the result in the following format from inside the method- 
	
	Target = {target} , Found at index = {index}, Number of iterations = {iterations}

Notes: 
- You will need to keep track of how many iterations/steps it takes to find the result (iterations).
- If a word is not found within the list, the function should return -1.
- You will need to put your python script (.py) and the provided ‘words.txt’ in the same folder

"""


file = open('words.txt', 'r')
words = file.read().splitlines()
print('Number of words read:', len(words))

def linear_search(arr, target):
    # Implement iterative linear search here
    # print(f"Target = {target} , Found at index = {index}, Number of iterations = {iterations}")
    indexNum = -1
    iterations = 0
    for i in range(len(arr)):
        iterations += 1
        if arr[i] == target:
            indexNum = i
            break
        
    print(f'Target = {target}, Found at index = {indexNum}, Number of iterations = {iterations}')
    return 
        
        

target = input('Enter search key: ').lower()

while target != 'exit':
    linear_search(words, target)
    target = input('Enter search key: ').lower()
