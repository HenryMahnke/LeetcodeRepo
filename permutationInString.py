def checkInclusion(s1, s2):
    countS1 = {} 
    countS2 = {}
    for ch in s1: 
        countS1[ch] = countS1.get(ch,0) + 1
    #filling first count
    if len(s2) < len(s1): 
        return False
    l = 0
    r = len(s1)-1
    for i in range(l, r+1): 
        countS2[s2[i]] = countS2.get(s2[i],0)+1
    print(len(s2)-1)
    while r < len(s2):
        print("r", r)
        print("countS1", countS1)
        print("countS2", countS2)
        if countS1 == countS2: 
            return True 
        else: 
            #get the S2[l]
            val2 = countS2.get(s2[l],-1)
            countS2[s2[l]] = val2 -1
            if val2-1 == 0: 
                del countS2[s2[l]]
            r+=1 
            l+=1
            if r < len(s2):
                countS2[s2[r]] = countS2.get(s2[r],0) + 1
    return False


s1="abc"
s2="ledabac"
print(checkInclusion(s1,s2))

