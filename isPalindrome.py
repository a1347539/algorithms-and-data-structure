def wordPattern(pattern, str):

    dict = {}
    
    li = list(str.split(" "))
    
    for i in range(len(li)):
        
        if li[i] not in dict:
            dict[li[i]] = pattern[i]
            
            
            
        
        elif pattern[i] != dict[li[i]]:
            return False

    return True

pattern = "abba"
str = "dog cat cat dog"
print(wordPattern(pattern, str))
