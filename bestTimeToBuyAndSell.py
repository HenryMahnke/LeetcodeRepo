def maxProfit(self, prices):
    l = 0 
    r = 1
    maxProf = 0
    while l <= r and r < len(prices):
        if prices[r] >= prices[l]:
            maxProf = max(maxProf,prices[r] - prices[l])
            r += 1
        else:
            l+=1
    return maxProf