def main():
    #print 10 to 20
    print("[",end ="")
    for i in range(10, 21):
        if i != 20:
            print(str(i) + ",", end = "")
        else:
            print(str(i), end = "")
    print("]")
    #print 10 to 100
    print("[",end ="")
    for i in range(1, 11):
        if i != 10:
            print(str(i * 10) + ",", end = "")
        else:
            print(str(i * 10), end = "")
    print("]")
    #print 100 to 10
    print("[",end ="")
    for i in range(10, 0, -1): #add step = -1 to decrease value instead of increase
        if i != 1:
            print(str(i * 10) + ",", end = "")
        else:
            print(str(i * 10), end = "")
    print("]")

main()