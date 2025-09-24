def sum_of_list(inputList):
    sumNum = 0 #set the initial sum value as 0
    i = 0
    while i < len(inputList): #scan through the list and add each value into sumNum
        sumNum += inputList[i]
        i += 1
    return sumNum

def main():
    myList = [5,7,10,3,-5,33,-823,12,138,3457,12,1,0,33]
    print("The sum of numeric values in the list is: ", sum_of_list(myList))


main()

