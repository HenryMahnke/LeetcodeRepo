"""
doing an easy one tonight, as its 10:47 eek!
"""
#best time to buy and sell stock 
# given array of prices, where prices[i] is the price of a given stock on the ith day 
#want to maximize profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock 

"""
def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        for i in range(len(prices)): 
            curBuy = prices[i]
            for j in range(i+1,len(prices),1):
                curSell = prices[j]
                maxProf = max(curSell-curBuy, maxProf)
        return maxProf

        naieve solution 
"""
# def maxProfit(prices): 
#     maxProf = 0 
#     L = 0
#     R = len(prices)-1
#     while L <= R:
#         maxProf = max(prices[R] - prices[L],maxProf)
#         if prices[L] > prices[R]:
#             L+=1
#         else: 
#             R-=1
#     print(maxProf) 

# prices = [7,1,5,3,6,4]
# maxProfit(prices)
#im cabing to ask for a hint because its 11:10 and I have work tomorrow. 


#hint - update minimimum buy price if current price is lower, calculate the profit if you sold today 
def maxProfit(prices):
    maxProf = 0 
    minBuy = prices[0]
    for i in range(len(prices)): 
        if prices[i] < minBuy: 
            minBuy = prices[i]
        maxProf = max(maxProf, prices[i] - minBuy)
    print(maxProf)

prices = [2,1,4]
maxProfit(prices)