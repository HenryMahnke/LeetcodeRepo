class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)
        for i in range(len(heights)):
            print("stack:" , stack)

            while stack and heights[i] < heights[stack[-1]]:
                print("stack:", stack)
                prev= stack.pop()
                if stack:
                    width = i - stack[-1] -1
                else: 
                    width = i
                height = heights[prev]
                #lower bounded by the height at prev 
                print("width", width)
                print("height",height)
                area = width * height
                maxArea = max(area,maxArea)
                print(maxArea)
            stack.append(i)
        return maxArea





        