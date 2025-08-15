def trap(self, height):
        leftMaxes = [0] * len(height) 
        rightMaxes = [0] * len(height) 
        maxL = 0
        maxR = 0
        totalWater= 0
        for i in range(1,len(height)): 
            maxL = max(maxL,height[i-1])
            leftMaxes[i]=maxL
        for j in range(len(height)-2,-1,-1): 
            maxR = max(maxR,height[j+1])
            rightMaxes[j] = maxR
        print(leftMaxes,rightMaxes)
        for k in range(1,len(height)-1): 
            h = min(leftMaxes[k], rightMaxes[k])
            totalWater += max(h-height[k],0)
        return totalWater