# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        depths = {}

        def dfs(root):
            leftHeight = 0
            rightHeight = 0
            violates = False
            # can't short circuit with vioaltes, have to go all the way up the call stack
            print("current root is:", root.val, end=" ")
            if root.left:
                ret = dfs(root.left)
                if ret[2] == True:
                    return 0, 0, True
                leftHeight = 1 + max(ret[0], ret[1])
            if root.right:
                ret = dfs(root.right)
                if ret[2] == True:
                    return 0, 0, True
                rightHeight = 1 + max(ret[0], ret[1])
            if abs(leftHeight - rightHeight) > 1:
                return leftHeight, rightHeight, True
            print(leftHeight, rightHeight, False)
            return leftHeight, rightHeight, False

        if not root:
            return True
        ret = dfs(root)
        print(ret)
        if ret[2] == True:
            return False
        return True


"""
a little bity of the bit taht hung me up is that from the perspective of a parent node, the height is the max of the left and right of the child, thereby accounting for the subtree rooted at the parents 2 children."""
