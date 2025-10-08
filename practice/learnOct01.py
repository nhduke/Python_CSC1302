def longestsubstring(s):
    charDict = {}
    left = 0
    right = 0
    max = 0
    
    while right < len(s):
        if s[right] not in charDict.keys():
            charDict[s[right]] = right
            right += 1
            if (right - left + 1) > max:
                max = right - left + 1
        else:
            left = charDict[s[right]] + 1
            del charDict[s[right]]
    return max
           
    

print(longestsubstring('abcabcbb'))