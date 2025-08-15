"""given an integer array nums, 
return all the triplets [nums[i],nums[j],nums[k]] where nums[i] + nums[j] + nums[k] ==0 
and the indices, i j, k are all distinct 

Ex.
Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
aim for O(n^2) time O(1) space.
"""

# def threeSum(nums): 
#     l,m,r = 0,1,2
#     while l < len(nums)-2:
#         #this will be an O(n^3) sol
#         while m < len(nums)-1:
#             while r < len(nums): 
#                 target = nums[l]+nums[m]+nums[r]
#                 print(f"{nums[l]},{nums[m]},{nums[r]}")
#                 if target == 0: 
#                     #add to set
#                     pass 
#                 r +=1
#             m+=1 
#             r = m+1
#         m=l+1
#         l+=1
def threeSum(nums): 
    #i think instead what we should do 
    #is add 2 of the numbers together, and store the 2 indices in a hashmap 
    #then go through the hashmap and add all of the numbers to each
    #i don't think that does us any better
    #that gets us to the O(n^2) time complexity but O(n^2) space 
    #we could only store unique values, but then we are still storing things 
    #we need to just do this in the list 
    # setOf = set()
    # l,r = 0, len(nums)-1
    # while l < r:
    #     cur = nums[l] + nums[r]
    #     for i in range(l+1,r):
    #         print(f"{nums[l]},{nums[i]},{nums[r]}")
    #         val = cur + nums[i]
    #         if val == 0: 
    #             setOf.add(sorted(l,r,i))
    #     l+=1
    # print(setOf)
    # return list(setOf)

    #first sort 
    mySet = set()
    nums.sort() 
    print(nums)
    l1,r1 = 0 , len(nums)-1
    val = nums[l1]+nums[r1]
    #now want to add one of the remaining numbers to the quantity val
    while l1 < r1:
        if val > 0:
            l+=1
        



nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))