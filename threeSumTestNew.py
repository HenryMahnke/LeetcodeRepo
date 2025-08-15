def threeSum(nums):
    res = [] 
    nums = sorted(nums)
    for ind, cur in enumerate(nums): 
        l=ind+1
        r = len(nums)-1
        if ind > 0 and nums[ind] == nums[ind-1]:
            continue
        while l < r: 
            if l == ind or (l > 0 and nums[l] == nums[l-1]):
                l+=1
                continue
            if r == ind or (r <len(nums)-1 and nums[r] == nums[r+1]): 
                r -=1
                continue
            val = cur + nums[l] + nums[r]
            if val ==0: 
                tup = [cur,nums[l],nums[r]]
                res.append(tup) 
                print("l = ", l)
                print("r=", r)
                r-=1
                l+=1
                
                continue
            elif val < 0: 
                l+=1
            else: 
                r-=1
    return res

nums = [-4,-1,-1,0,1,2]
# nums = [-2,0,0,2,2]
print(threeSum(nums))