# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None 
        def dfs(root,p,q): 
            nonlocal lca 
            left = None 
            right = None
            # searches for descendant of self, so root == has to come after
            
            if root.left: 
                left = dfs(root.left, p,q)
            if root.right: 
                right = dfs(root.right,p,q)
            # this will conflict with descendant of self
            if root.left and root.right:
                print(root.val, left, right)
                print(root.val, root.left.val, root.right.val)
                print(root,p,q)
            if root.val == p.val: 
                print("root == p")
            if root.val == q.val: 
                print("root == q")
            if (root.val == p.val) or (root.val ==q.val):
                print("root equal") 
                # this should handle that
                if left or right: 
                    lca = root
                return True
            if left and right: 
                lca = root 
                return True 
            elif bool(left or right): 
                return True
            else: 
                return False
        dfs(root,p,q)
        return lca

"""
This problem was stupid in my opinion, the code, that I had originally wrote had excluded the.val on root and p and q in the base case check for that
as I had posited that we would be directly given the memory address, instead we were given what appears to eb the root of a subtree that is the same, but that don't point to the same place in memory 
This was pretty stupid in my opinion, and I spent 30 minutes debugging only to add .val in the check and everything magically work. quite annoying.
"""