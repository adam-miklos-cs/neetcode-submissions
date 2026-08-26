# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def max_depth(root: Optional[TreeNode]) -> int:
            nonlocal d
            if root is None:
                return 0
            
            left_depth = max_depth(root.left)
            right_depth = max_depth(root.right)
            d = max(d, left_depth + right_depth)
            return max(left_depth, right_depth) + 1 
        max_depth(root)
        return d

        