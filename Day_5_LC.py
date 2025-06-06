#Today i have a little longer, so i am going to go to the neetcode 75, and just speed run and see how many i can do in the next 2 hours
#I am going to spend 30 minutes per problem max, then if i can't ill get a hint with no code, program it out if i can, otherwise look at the code 
#starting with arrays and hashing

"""contains duplicate, given an integer array nums return true if any value appears more tahn once in the arra, otherwise return false"""
#we can do this in O(1) with a hashmap 
# def hasDuplicate(nums): 
#     myDict = {} #probably a suggestive name lol
#     for i in range(len(nums)): 
#         cur = myDict.get(nums[i],0)
#         if cur != 0: 
#             return True 
#         else:
#             myDict[nums[i]] = cur+1
#     return False
# #lookied up on internet how to get default as 0 

# nums = [1,2,3,4]
# print(hasDuplicate(nums))

#great we passed that in about 4 minutes. On to the next! 


"""valid anagram. 
Given two strings s and t return true if the wo strings are anagrams of each other, otherwise return false. 
an anagram contains the exact same charcters as another but order does not matter. again we can do this with a dict"""

# def isAnagram(s, t): 
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


# s = "racebar" 
# t = "cracare"
# print(isAnagram(s,t))

#just had an issue not using j in the second loop that made it fail the first time i submitted 


#great, thats 2 done in 13 minutes, both easy so far. Ready for a challenge.

"""two sum, gien an array of integers, nums and an integer target, return the indices i and j such that 
nums[i] + nums[j] == target  and i != j  you may assume that every input has exactly one pair of indices i and j 
that satisfy the condition, return the answer with the smaller index first."""
# def twoSum(nums,target): 
#     #we should be able to do this in O(n) time and O(n) space  
#     """i think what we want to do is some type of make a dict of len n where all values are the target, then 
#     we can subtract the current and then we could look it up"""
#     myDict = {} 
#     for i in range(len(nums)): 
#         diff = target - nums[i]
#         cur = nums[i]
#         if cur in myDict: 
#             return [myDict[cur], i]
#         else: 
#             myDict[diff] = i
#     return None
# nums = [5,5]
# target = 10
# print(twoSum(nums,target))

#done!  8:27,i got a bit ditracted with some reasearch stuff. Going to take a 10 minute break and then get back to it.

#alright back at 8:42, i think we'll do a few more and see what we can come up with

"""group anagrams
given an array of strings strs, group all anagrams together into sublists. You may return the output in any order. 
An anagram is a string that containts the exact same characters as another string but the order of the characters can be different

Recommended time and space complexity 
O(m*n) time, O(m) space where m is the number of strings, and n is the length of the longest string.

"""
# def groupAnagrams(strs): 
#     output = []

#     output.append([newList])



# strs = ["act","pots","tops","cat","stop","hat"]


# #desired otuput: 
# # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
#well, its 8:50, i think i might actually save this one for a bit later.