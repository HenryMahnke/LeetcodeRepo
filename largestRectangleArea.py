class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxOverall = 0
        for i in range(len(heights)):
            minOfNext = float('inf')
            maxRectiStart = 0 
            for j in range(i,len(heights)):
                minOfNext = min(heights[j],minOfNext)
                rectHeight = min(minOfNext,heights[i])
                rectArea = rectHeight * (j - i+1)
                maxRectiStart = max(rectArea,maxRectiStart)
            maxOverall = max(maxOverall,maxRectiStart)
        return maxOverall