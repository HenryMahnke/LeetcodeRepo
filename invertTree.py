# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # from the top down swap right and left 
        # recursive helper
        def helper(cur): 
            if cur:
                cur.right, cur.left = cur.left, cur.right
                helper(cur.right)
                helper(cur.left)
        helper(root)
        return root
        