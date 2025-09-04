def findMin(nums):
    l = 0 
    r = len(nums)-1 
    while l < r: 
        m = (l+r)//2 
        if nums[r] > nums[m]: #know m is past pivot
            r = m 
        else:  #nums[r] < nums[m]
            l =m+1
        print("m ", m, "l " , l, "r ", r) 
    print("l",l,"r",r)
    return nums[l]

nums = [10,12,13,1,3,4,5]
print(findMin(nums))
        