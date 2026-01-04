# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        hasSubtree = False
        def dfs_both(root,subRoot):
            ret = True
            if not root and not subRoot: 
                return True
            if root and not subRoot or not root and subRoot: 
                return False 
            if root.val != subRoot.val: 
                return False
            else:
                print(root.val, subRoot.val)
                ret = dfs_both(root.left,subRoot.left) and dfs_both(root.right,subRoot.right) 
                return ret
            
        def dfs(root,subRoot):
            nonlocal hasSubtree
            ret = True
            print("searching with root:", root.val)
            if root and subRoot and root.val == subRoot.val:
                print("searching subroot")
                hasSubtree = dfs_both(root,subRoot)
                print("hasSubtreeval", hasSubtree)
                if hasSubtree: 
                    return True
            if root and not subRoot: 
                return False
            if root.left: 
                ret = ret and dfs(root.left,subRoot)
            if root.right:
                ret = ret and dfs(root.right,subRoot)
            return ret
        dfs(root,subRoot)
        return hasSubtree

        