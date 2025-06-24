#two integer sum 2 
"""givena n array of integers numbers that is sorted in non decreasing irder 


return the indices(1 indexed) of two numbers, index1, index2, such that 
they add up to a given target number target and index1< index2. 
Note that index1 and index2 cannot be equal, thereforoe you may not use the same element twice 
there will always be exactly one valid solution.

Q. i wonder what would happen if there are multiple, can you subject costs 
like minimize the first number? of course you could, but what would the time 
complexity become?"""


def twoSum(numbers, target): 
    #must use O(1) additional space 
    #alright, so this is a two pointer question 
    #but we have to think through how we should go about it 
    #if we start at the beginning and the end. 
    #if the value is more we know to move right right pointer down 
    #if its less we move the left pointer up. Is it not that easy? 
    l = 0
    r = len(numbers) -1
    while l < r: 
        if numbers[l]+numbers[r] < target: 
            l+=1 
        elif numbers[l]+numbers[r] > target:
            r-=1
        else: 
            break
        print(numbers[l]+numbers[r])
    output = [l+1,r+1]
    return output


numbers = [1,2,3,4]
target = 3 
print(twoSum(numbers,target))

#debrief 
"""
this really doesn't seem like it should be a medium, maybe i've just seen it before 
but this was mad easy... weird. thats good though because its 11:41 EEK

"""