def longestConsecutive(nums) -> int:
        #just hash all the elements to start 
        dicti = {}
        for i,num in enumerate(nums):
            cur = dicti.get(num,[])
            cur.append(i)
            dicti[num] = cur
        print(dicti)
        #making the hash set
        #then we want to find the set of numbers that are the start of a sequence
        startingNumbers = []
        for num in nums:
            val = dicti.get(num-1)
            if not val:
                startingNumbers.append(num)
        print(startingNumbers)
        #then here we want to construct the sequence
        maxLen = 0
        for i, start in enumerate(startingNumbers):
            count = 0
            val = start
            while val is not None: #had to do is not None because there could be zero! intersting bug!
                count +=1 
                val = dicti.get(start+count)
            maxLen = max(maxLen,count)
        return maxLen