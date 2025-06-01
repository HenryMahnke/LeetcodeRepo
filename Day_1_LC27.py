from typing import List

def removeElement(nums: List[int],val:int) -> int:
    #remove val from nums in place 
    counter = 0
    i = 0
    while (i < len(nums)):
        if nums[i] == val: 
            nums.pop(i)
            i-=1
        else:
            counter +=1
        i+=1


    return counter

"""
Day 1 review!

Comman Gotchas For this Problem:
The main gotcha for this problem is that it is very natural to want to pop in python, at least to me. But should you do this in a forloop, 
it is more than likely that you'll run into funny issues with the indexing because you are modifying the length of the array that you are 
in the middle of traversing. This is especially the case if you are writing it "semi pythonically" where you are doing for num in nums 
because then you have no index to manipulate. This is a fundamental limitation, i don't even believe that there is a way that you can get around 
this because internally, python creates a loop iterator, that continues throuhg whatever it saw originally. so you can't rewind at all. 

This is where the while loop comes in, then just as you pop you rewind the index to account for the spot that you are missing, netting no change to
your index by the end as the new value falls into the index you were looking at the previous iteration.

Because the problem specified the rest of the values don't matter, instead of popping you could have swapped with the end in some fashion, tracking
the swaps and such, but this seems like a pretty good way of doing it. Though i know it's far from purely pythonic. 
"""