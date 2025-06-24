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


#debrief: 
""" 
Key idea/pattern:
the main idea here was creative solutions with arrays. To be completetly honest 
I was dumbfoudned i came up with this solution by myself, i stared blankly not knowing what to do 
for a long while. It was interesting, because i don't think the naive solution is 
very present to me, or well, i guess it depends on what the naive soltuion actualy is 
at first i just though to multiply all into a giant number and then divy out to the output arrya 
by dividing but that doesn't work when 0 is in the input, and so then you would need some 
O(n^2) solution, an obviously that is not ideal. But this all after all before worked really well 
and i kept questioning myself when implementing it if it was actualy going to work, after being surprised i came up with it  
alternative solution discovered? 

bug hit and how fixed:
creating the arrays was a little funky and I had to back track to make sure i got it right, but nothing too weird

template snippet to save? 
"""