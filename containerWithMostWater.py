def maxArea(self, heights):
    # brute force approach is O(n^2) tries all combinations of heights
    # with corresponding widths.

    ### instead we use 2 pointers with greedy pointer movement
    l = 0
    r = len(heights) - 1
    max_area = 0
    while l < r:
        l_height = heights[l]
        r_height = heights[r]
        width = r - l
        height = min(r_height, l_height)
        area = width * height
        max_area = max(area, max_area)
        # peek
        # careful of overlap in indices here
        # if they are going to overlap, they would've no matter if you
        # move l or r, so we should be fine.
        # before was trying to do the difference
        if heights[l] < heights[r]:
            l = l + 1
        else:
            r = r - 1
    return max_area


"""
This problem is actually quite interesting. I had originally viewed it through the lens of trying to find the difference between the next heights on 
both the left and right pointers by doing a "peek" operation and comparing area and moving from their, but that definitley didn't work properly 
and was far more vibes based than in reasoning. But the real way this works is oddly simple 

You just throw out the smallest height. 

I found that you can think about it this way. You have a left and right pointer that start on opposite ends. 
No matter what you are bound by the smaller height. 
Left is smaller? No matter what you change right to, you are decreasing the width! and because you are bound 
by the height of left, you will never find a larger area, so you have to discard left, because in one step, with the knowledge 
of the problem, you can certifiably say that there is no larger area for that step. 
You continue this, discarding the smallest which makes this 2 pointer approach possible.
"""
