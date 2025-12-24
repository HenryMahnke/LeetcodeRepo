from typing import *

def findDuplicate(nums:List[int]) -> int:
    index = 0 
    while index < len(nums):
        print(nums)
        indToChange = nums[index]
        print(indToChange)
        if(nums[index]) < 0:
            indToChange *=-1
        indToChange = indToChange -1
        if nums[indToChange] >0:
            nums[indToChange] *= -1
        else:
            return indToChange+1
        index +=1





nums=[1,2,3,4,4]
print("hello world")
print("duplicate num:", findDuplicate(nums))