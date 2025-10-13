import time
#robot always start at top left -> (0,0)
#destination always at bottom right -> (m-1, n-1)
#logic: while not at the border (m-1 or n-1), there will always be 2 possible moving option -> 2 choices

def num_paths(m, n):
    # TODO: Task 1 of the assignment
    #if there is only one line (vertical or horizontal), there is only one way
    if m == 1: #base case
        return 1
    elif n == 1: #base case
        return 1
    else:
        #at any other location, there are 2 possible way to go: downward or righward
        #the robot keep going until reached a border (base case)
        return num_paths(m - 1, n) + num_paths(m, n - 1) 
    
    
#create a global variable to record memoization of recursion value
#use dictionary for a pair of key(location) - value(paths)
#key(location) is a tuple because it must have 2 value and immutable
locationDict = {}

def num_paths_memo(m, n):
    # TODO: Task 2 of the assignment
    if m == 1: #base case
        return 1
    elif n == 1: #base case
        return 1
    else:
        #check if there is pre-calculated recursion
        if tuple([m, n]) in locationDict: 
            return locationDict[tuple([m, n])]
        else:
            #if there is no existed value, proceed with recursion and record value into Dictionary
            tempVal = num_paths_memo(m - 1, n) + num_paths_memo(m, n - 1)
            locationDict[tuple([m, n])] = tempVal
            return tempVal


#driver code - you do not need to make any changes after this line.
#However, submit a screenshot of the output to report the execution time/elapsed time.
#---------------------------------------------------
start_time = time.time()
print(num_paths(15,14))
end_time = time.time()

start_time_memo = time.time()
print(num_paths_memo(15,14))
end_time_memo = time.time()

print(f"Elapsed time (no memoization): {end_time - start_time} seconds")
print(f"Elapsed time (memoization): {end_time_memo - start_time_memo} seconds")
#---------------------------------------------------
