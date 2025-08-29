class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dq = collections.deque([("",0,0)])
        output = []
        #first is open, second is closed
        while dq:
            s,o,c = dq.popleft()
            if len(s) == 2*n: 
                output.append(s)
            if o < n: dq.append((s + "(", o+1,c))
            if c < n and c < o: dq.append((s + ")", o,c+1))
        print(len(output))
        return output