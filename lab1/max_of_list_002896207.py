def max_of_list(inputList):
    maxNum = inputList[0] #set the first value as the intitial maximum value
    i = 0
    while i < len(inputList):#scan through the list
        if maxNum < inputList[i]: #Get the larger value as the new maxNum
            maxNum = inputList[i]
        i += 1
    return maxNum

def main():
    myList = [5,7,10,3,-5,33,-823,12,138,3457,12,1,0,33]
    print( "The largest numberic value of the list is: ", max_of_list(myList))

main()
