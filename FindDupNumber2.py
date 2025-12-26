# tortoise and hare solution

# start fast and slow pointers to 0 for tortoise and hare 

# treat array like a linked list, each index points to the next index given by its value 
# because one number is duplicated, two indices will point into the same chain, like a linked list loop 

def findDuplicate(nums): 
    slow = 0 
    fast = 0
    slow +=1 % len(nums)
    fast +=2 % len(nums)




nums_arr = [
    [1,2,3,4,4],
    [1,2,2,3,4],
    [3,1,3,4,2],
    [3,1,3,2],
    ]
for nums in nums_arr:
    findDuplicate(nums)