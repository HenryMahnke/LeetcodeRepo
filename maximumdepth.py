# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            leftHeight = 0
            rightHeight =0
            if root.left:
                leftHeight = dfs(root.left)[0]
            if root.right:
                rightHeight = dfs(root.right)[0]
            # print(leftHeight, rightHeight)
            diameter = leftHeight + rightHeight
            height = 1+ max(leftHeight,rightHeight)
            return height, diameter
        if root:
            return dfs(root)[0]
        else:
            return 0