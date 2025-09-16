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
        if root is None: 
            return None
        q = deque([root])
        while q: 
            cur = q.popleft()
            cur.right, cur.left = cur.left, cur.right
            if cur.right: q.append(cur.right)
            if cur.left: q.append(cur.left)
        return root
        