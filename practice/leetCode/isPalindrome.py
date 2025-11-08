def isPalindrome(x):
    if x < 0:
        return False
    
    rightMost = x % 10
    digits = 1
    while (x // pow(10,digits - 1)) >= 10:
        digits += 1

    return digits
        
print(isPalindrome(132321))