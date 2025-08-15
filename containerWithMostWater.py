def maxArea(self, heights):
    #brute force approach is O(n^2) tries all combinations of heights 
    #with corresponding widths. 

    ### instead we use 2 pointers with greedy pointer movement 
    l = 0 
    r = len(heights)-1
    max_area = 0
    while l < r: 
        l_height = heights[l]
        r_height = heights[r]
        width = r-l 
        height = min(r_height,l_height)
        area = width * height 
        max_area = max(area, max_area)
        #peek 
        #careful of overlap in indices here
        #if they are going to overlap, they would've no matter if you 
        #move l or r, so we should be fine.
        #before was trying to do the difference
        if heights[l] < heights[r]: 
            l = l+1 
        else: 
            r = r-1
    return max_area
        


    