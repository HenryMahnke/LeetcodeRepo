#product of array except self 
"""given an integer array nus, return an array output were output[i] is the product of all 
the elements of nums except nums[i]. Each product is guaranteed to fit in a 32 bit itneger
could you solve it in O(n) time without using the division operation? """
#naive solution
def productExceptSelf(nums):
    output = [None] * len(nums) 
    allBefore = [1,nums[0]]
    for i in range(2,len(nums)): 
        allBefore.append(nums[i-1] * allBefore[i-1])
    # print(allBefore)
    endIndex = len(nums)-1
    #we want the 
    allAfter = [None] * len(nums)
    allAfter[endIndex] = 1 
    allAfter[endIndex-1] = nums[endIndex]
    # print(allAfter)
    for i in range(endIndex-2, -1, -1):
        allAfter[i] = nums[i+1] * allAfter[i+1]
        # print(nums[i+1], "*" ,nums[i+2])
        # print(i)
        # print(allAfter)
    # print(allAfter)
    for idx, (i, j) in enumerate(zip(allBefore, allAfter)):
        output[idx] = i * j
    # print(output)
    return output
nums = [-1,0,1,2,3]
print("output", productExceptSelf(nums))