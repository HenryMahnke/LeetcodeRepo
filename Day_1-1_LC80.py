# remove duplicates in place such that each unique element appears at most twice 
    # relative order should be kept the same. 
    # the result in the first part of the array. i.e if k elements after removal, first k elems hold final res 
    # return k. 
    # cannot allocate extra space. O(1) extra memory. 

def removeDuplicates(nums): 
    # off the bat im tempted to use a hashmap, but I am unsure if that counts as extra memory. 
    #actually, because we are given that it is sorted in non decreasing order this is actually quite easy 
    # we can just have a trailing counter wiht a record variable 
    record = 0 
    trailingCounter = 0
    i=0
    while (i < len(nums)): 
        cur = nums[i] 
        if cur != record: 
            trailingCounter = 1
            record  = cur
        else: 
            trailingCounter+=1
        if trailingCounter == 3: 
            nums.pop(i)
            trailingCounter-=1
            i-=1
        # print(nums,record,trailingCounter)
        i+=1
    return len(nums)


arr = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(arr),arr)

"""
Day 1 Problem 2 debrief 
also not a super hard problem. There are definitely ways to make if faster, such as avoiding pop, but all test cases pass with 
a pretty simple logging solution. Also interestingly, while the return type is supposed to be the k elements that you actually want
the judge to look at, you can exclude the return statement and still pass the cases. But anyway, the main trick is to just realize that its
sorted and exploit that you can detect changes that way!

"""