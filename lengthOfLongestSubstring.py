def lengthOfLongestSubstring(s):
    dicts = {}
    maxlength = start = 0
    for i,value in enumerate(s):

        if value in dicts:
            sums = dicts[value] + 1
            if sums > start:
                start = sums
                print(start)
        num = i - start + 1
        print(i,start)
        if num > maxlength:
            maxlength = num

        dicts[value] = i
    return maxlength



s = "dvdf"
print(lengthOfLongestSubstring(s))
