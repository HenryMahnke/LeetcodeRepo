from typing import List
def majorityElement(self, nums: List[int]) -> int:
    record = {}
    for i in nums: 
        if i in record: 
            record[i] +=1 
        else:
            record[i] = 1
    majorityElement = nums[0]
    majorityCounter = 0
    print(record)
    for j in record: 
        if record[j] > majorityCounter: 
            majorityElement = j
            majorityCounter = record[j]
    return majorityElement

"""
to be completely honest, i spent about an hour and a half trying to work through leet code 189, and couldn't quite get it, going to try to tackle it again tomorrow
but did this easy to have something to show for today. 

See you back here tomorrow. 

"""