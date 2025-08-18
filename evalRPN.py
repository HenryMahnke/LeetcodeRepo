class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        def isOp(val): return (val in {'+', '-', '*', '/'})
        def apply(term1, term2, op): 
            term1 = int(term1)
            term2 = int(term2)
            if op == '+': 
                return term1 + term2
            elif op == '-': 
                return term1-term2 
            elif op == '*':
                return term1 * term2
            else: 
                print(term1,term2)
                return int(term1/term2)
        stack = []
        countInts = 0
        
        while len(tokens) >0:
            print("tokens", tokens)
            item = tokens.pop() 
            if item in {'+', '-', '*', '/'}:
                stack.append(item)
                # print(stack)
            else: #item is an integer 
                stack.append(item)
                while len(stack) >= 3 and not isOp(stack[-1]) and not isOp(stack[-2]) and isOp(stack[-3]):
                    print("entering get out")
                    int1 = stack.pop()
                    int2 = stack.pop() 
                    op = stack.pop()
                    res = apply(int1,int2,op)
                    if len(stack) == 0:
                        return res 
                    else: 
                        stack.append(res)