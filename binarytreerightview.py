# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        q = deque()
        output = []
        lvl_list = []
        prev_lvl = 0
        q.append((root,0))
        while len(q) > 0:
            cur,lvl = q.popleft()
            if lvl > prev_lvl:
                prev_lvl = lvl 
                output.append(lvl_list[-1])
                lvl_list = []
            lvl_list.append(cur.val)

            if cur.left: 
                q.append((cur.left,lvl+1)) 

            if cur.right: 
                q.append((cur.right, lvl+1))
        output.append(lvl_list[-1])
        return output






