class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        r = 0
        count = {}
        if len(s) < 2: 
            return len(s)
        maxFreq = 0 
        count[s[l]] = count.get(s[l],0)+1
        longest =0
        while r < len(s): 
            maxFreq = max(count.values())
            violations = (r-l+1) - maxFreq
            print("l", l, "r", r)
            print("violations", violations)
            print("longest", longest)
            print("count", count)
            print()
            if violations > k:
                #remove that val from the dict
                curVal =count.get(s[l],0)
                count[s[l]] = curVal -1
                l+=1
            else:
                #if no violations, calculate the longest
                longest = max(longest,r-l+1)
                r+=1 
                if r < len(s):
                    curVal = count.get(s[r],0)
                    count[s[r]] = curVal +1
                
                #only update maxFreq on rightward move.
                
        return longest
        

        