#well we missed a day over the weekend, so i suppose we will add a day at the end 
# that seems like a fair compromise, even though I was coding for research over the weekend 
#but that doesn't count :)
#today we are tackling top k frequent elements, and encode and decode strings 
#we need to start cooking on some of these and speed up how much we are getting done, so 2 mediums seems pretty good 
#i got about an hour before i want to get ready for bed, so we gotta get  moving 
"""top k frequent elements 
Given an integer array nums and an integer k, return 
the k most frequent elements within the array . 
Example 1: 
input nums = [1,2,2,3,3,3], output [2,3]
k = 2


Example 2 
input nums = [7,7], k = 1 
output: [7]
recommended time and space is O(n) for both

The main problem seems to just be with how we storoe the date 
and a creative way of hashing if we just count all of the elements naively 
then we will get something like 1:1, 2:2, 3:3
and then we have to iterate through the values and get the top ones, and even getting the top k seems a bit unintuitive 
it's weird that we need O(n) space recommended

they are likely also not sorted like they are in the examples 
lets code the naive solution
"""

# def topKFrequent(nums,k):
#     myDict = {}
#     for i in range(len(nums)):
#         cur = myDict.get(nums[i],0)
#         myDict[nums[i]] = cur +1
#     #to be honest i don't know how to sort a dict by its values in python 
#     sorted_dict = dict(sorted(myDict.items(), key = lambda item: item[1],reverse= True))
#     print(sorted_dict)
#     ret = []
#     for i in range(k):
#         print(list(sorted_dict.keys()))
#         ret.append(list(sorted_dict.keys())[i])
#     return ret
# nums = [1,3,4,1,3,2,6]
# k = 2
# print(topKFrequent(nums,k))
#this is a valid solution, but we iterate through the array to get counts O(n), and we sort O(nlgn) 
# and then we iterate through k times, so we have O(nlgn + k) time complexity 
#lets see if we can come up with a faster algorithm
# 
# the hint that they gave us (after the naive hint) was "can you think of an algorithm which involves grouping numbers based 
# on their frequency" 

def topKFrequent(nums,k):
    # says to use bucket sort as the next hint 
    #bucket sort with n buckets 
    # bucket_array = [0] *len(nums)
    #if we do something like this, python interpretes it as creating one list[]
    #then make len(nums) copies of a reference to that exact same list
    #instead of creating n boxes, you create n labels, all that go to the same box
    #when you do my_list = [0] * 3, and then reassign my_list[0] you are creating a new valie that has its own value, and then 
    #changing that place in the array to point to this new refernece
    bucket_array = [[] for _ in range(len(nums)+1)]
    # why can't you do [[] * len(nums)]
    my_dict = {}
    top_k = []
    counter = 0
    for i in range(len(nums)): 
        cur = my_dict.get(nums[i],0)
        my_dict[nums[i]] = cur+1
    print(my_dict)
    for j in my_dict.keys(): 
        print(j)
        frequency = my_dict[j]
        print(frequency)
        bucket_array[frequency].append(j)
    print(bucket_array)
    kCounter = 0 
    ret = []
    for l in range(len(nums),-1,-1):
        #iterate in reverse 
        # print(bucket_array[l])
        if bucket_array[l] and kCounter < k:
            for p in bucket_array[l]:
                if kCounter < k:
                    ret.append(p)
                    kCounter+=1
    return ret
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums,k))
#this seems like there could be some better ways of going about it, but it does work, maybe we will tackle making it more efficient tomorrow