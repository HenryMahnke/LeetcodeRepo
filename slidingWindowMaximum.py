from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        r=l = 0
        output = [] #the output array will have

        while r < len(nums):
            print(dq)
            while dq and nums[dq[-1]] < nums[r]: #look at top of the stack
                #if the top of the stack contains smaller than the new value 
                #new value is forever larger while in window so pop 
                dq.pop()
            #then once we've popped all that are smaller we add that to the right 
            dq.append(r) 
            while dq[0] < l:
                #stale 
                dq.popleft()
                #check if this needs to be a while loop 
            #then we can append to output 
            #storing everything in terms of indices so that can check for stale 
            if r >= k-1:
                output.append(nums[dq[0]]) #don't want to add while window is malformed
                l+=1
            r+=1
        return output