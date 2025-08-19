    def lengthOfLongestSubstring(self, s: str) -> int:
        #brute force is O(n^2)
        #sliding window problem: 
        l = 0 
        r = 1
        count = set()
        longest = 0
        #tracking max
        if len(s) < 2:
            return len(s)
        count.update(s[l])

        # count[s[r]] = 1
        # z x r = r+1 
        # z x test(y) -> if y not duplicate, r += 1 
        # z x y test(z) -> z is duplicate, popleft until not duplicate with l+=1
        #once done, then r +=1 
        # x y z test(x)

        while r < len(s): 
            print(l,r,count)
            if s[r] not in count:
                count.update(s[r])
                longest = max(longest,len(count))
                r+=1
                #here, the move is valid
            else: 
                count.remove(s[l])
                l+=1
        return longest
            