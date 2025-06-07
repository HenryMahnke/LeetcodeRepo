#working on group anagrams again 
"""here was my code from is anagram, and I don't see why i couldn't just use this:"""# def isAnagram(s, t): 
#     numZeros = 0
#     myDict = {}
#     if len(s) != len(t):
#         return False
#     for i in range(len(s)):
#         curS = myDict.get(s[i] , 0)

#         myDict[s[i]] = curS+1

#         curT = myDict.get(t[i],0)
#         myDict[t[i]] = curT -1
#     print(myDict)

#     for j in range(len(t)):
#         cur = myDict.get(s[j],1)
#         if cur == 0:
#             numZeros+=1
#         else:
#             return False

#     if numZeros == len(s): 
#         return True
#     return False
"""if i did this and just nested it in a loop that loops over the strings, the outer loop would run m times
and the inner loop would run n times for every m. the only thing is how do we check because it wouldn't actually run just n times 
if we also have to check

if we hash a series of things, can we generate a hash from those like hashes, if that makes sense 
looked up "Can you compare hashmaps in python" 

the ai overview says "the equality operator checks if two dictionaries have the same key-value pairs, regardless of order

how does python equality checking work
Hashmap equality has time complexity of O(n)

so if we had to do equality 


for i in range(0,m) //outer loop 
    for j in range(0,n) //inner loop to generate dict

    for k in range(0,m-1): 
    checking equality, and if it equals then place in array 
"""

def groupAnagrams(strs): 
    dictArray = []
    indexArray = []
    for i in range(len(strs)):
        curDict = {}
        for j in range(len(strs[i])):
            curVal = curDict.get(strs[i][j],0) 
            curDict[strs[i][j]] = curVal + 1
        print(curDict)
        if not dictArray:
            dictArray.append([curDict])
            indexArray.append([i])
        else:
            added = False
            for k in range(len(dictArray)): #exclusive of i
                print("test")
                print(dictArray[k])
                if curDict == dictArray[k][0]:
                    dictArray[k].append([curDict])
                    indexArray[k].append(i) #the i'th index is what we are currently indexing through
                    added = True
            if not added:
                indexArray.append([i])
                dictArray.append([curDict])
    print(dictArray) 
    print(indexArray)
                



strs = ["act","tac","pots","tops","cat","stop","hat"]
#the output we got was indexes 0,1,4, which is act tac, cat, that is correct 
#then we got 2,3,5 that is pots, tops, stop, that is correct, then we got 6 which is hat, that is correct
#so now just instead of printing the index then
groupAnagrams(strs)