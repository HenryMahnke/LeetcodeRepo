# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = []
        output = [] 
        # first get the depth of the tree: 
        def print_stack(stack): 
            print("sstack: [", end="")
            for s in stack: 
                print(s.val, ",",end="")
            print("]")

        def dfs(root):
            stack.append(root)
            if root.left: 
                dfs(root.left) 
            if root.right: 
                dfs(root.right)
            while len(output) < len(stack): 
                output.append(None)
            # print("output", output)
            # print("len of stack", len(stack))
            if output[len(stack)-1]:
                # print("putting at: ", len(stack)-1)
                output[len(stack)-1].append(stack[-1].val)
                stack.pop()
            else: 
                output[len(stack)-1] = [stack[-1].val]
                stack.pop()
            print(output)
            print_stack(stack)
        if root: 
            dfs(root)
        return output



