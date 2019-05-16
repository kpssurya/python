def isUniqueCharsString(s):
    if len(s) > 256:
        return False
        
    char_set = [False] * 128
    
    for i in range(0, len(s)):
        val = ord(s[i])
        if char_set[val]:
            return False
            
        char_set[val] = True
        
    return True
        
def numOfMostRepeatedCharsInString(s):
    d = {}
    for c in s:
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
    
    num = 0
    
    for key, value in d.items():
        if value > num:
            num = value
            
    return num
    
def stringWithMostRepeatedChars(l):
    d = {}
    for s in l:
        d[s] = numOfMostRepeatedCharsInString(s);
        
    maxLen = 0
    st = ""
    for key, value in d.items():
        if value > maxLen:
            maxLen = value
            st = key
            
    return st
    
l = ["aaaab", "aabb", "abc", "bbbbb"]
s = stringWithMostRepeatedChars(l)
print (s)

print(isUniqueCharsString("abcd"))

