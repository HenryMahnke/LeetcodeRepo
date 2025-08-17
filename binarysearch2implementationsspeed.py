    def binSearch(nums,target):        
#2 implementations, there is the closed interval and half closed 
        #1 closed itnerval 
        # l = 0 
        # r = len(nums)-1
        # while l <= r: 
        #     mid = (r+l) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         l = mid + 1
        #     else: 
        #         r = mid - 1
        # return -1
        #2 open interval 
        l = 0 
        r = len(nums) 
        while l < r: 
            mid = (r+l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: 
                r = mid
            else: 
                l = mid +1
        return -1