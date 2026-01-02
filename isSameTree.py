# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ret = True
        def areSame(p,q):
            nonlocal ret
            if p and not q: 
                ret = False
                return
            if q and not p:
                ret = False 
                return 
            if not (p and q): 
                return
            if p.left or q.left:
                areSame(p.left,q.left)
            if p.right or q.right: 
                areSame(p.right,q.right)
            if p and q and (p.val != q.val): 
                ret = False
        areSame(p,q)
        return ret