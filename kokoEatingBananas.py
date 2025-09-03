class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        while l<= r:
            hrs = 0
            m = (r+l) //2
            for i in range(len(piles)):
                hrs += math.ceil(piles[i] / m)
                print(hrs)
            print(hrs)
            if hrs <= h: 
                r = m-1 
            else: 
                l= m+1
        #then the output is when l = r = k 
        hrs = 0

        for i in range(len(piles)): 
            hrs += math.ceil(piles[i] / l)
        if hrs <= h: 
            return l
        else: 
            return -1

        