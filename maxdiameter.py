# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
given that we have DFS that can give us the height, we coudl do BFS to traverse every node in the tree. Run DFS on each of those nodes to get the max diameter, by then comparing all the nodes 

otherwise, we could use a hashtable and hash all the nodes, and assign them their height, then traverse that dictioanry 

"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameters = []
        def dfs(root):
            leftHeight = 0
            rightHeight =0
            if root.left:
                leftHeight = dfs(root.left)[0]
            if root.right:
                rightHeight = dfs(root.right)[0]
            # print(leftHeight, rightHeight)
            diameter = leftHeight + rightHeight
            height = 1 + max(leftHeight,rightHeight)
            self.diameters.append(diameter)
            return height, diameter
        # the diameter calculation is: 
        dfs(root)
        # print(self.diameters)
        return max(self.diameters)            