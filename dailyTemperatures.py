class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        output = [0] * len(temperatures)
        for i in range(len(temperatures)): 
            #if the current is larger than the top of the stack, then we want to pop
            #want to be pushing and popping indices 
            print(stack)
            print(temperatures[i])
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res = stack.pop() 
                output[res] = i - res
            #now when we break out of this, the most recent that we popped            
            stack.append(i)
        return output