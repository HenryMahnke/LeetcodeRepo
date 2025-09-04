class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1 
        # if len(nums)<3:
        #     if target in nums: 
        #         return nums.index(target)
        #     else: 
        #         return -1
        while l <= r: 
            m = (l+r)//2 
            print("l",l,"m",m,"r",r)
            if target == nums[m]:#early breakout
                return m
            elif nums[m] >= nums[l]: #left sorted 
                if target < nums[m] and target >= nums[l]: #in range
                    r = m-1 #can pass because early breakout
                else: #not in this sorted range 
                    l = m+1
            else: #right sorted
                print("in right sorted")
                if target > nums[m] and target <= nums[r]: #in range
                    l = m+1 
                else: 
                    r = m-1
        return -1
            
        