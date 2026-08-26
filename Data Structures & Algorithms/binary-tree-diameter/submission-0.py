# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def max_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        self.diameter = max(self.diameter, left_depth + right_depth)
        return max(left_depth, right_depth) + 1 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_depth(root)
        return self.diameter

        