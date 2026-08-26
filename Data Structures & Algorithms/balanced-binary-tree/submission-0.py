# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def depth(root: Optional[TreeNode]) -> int:
            nonlocal is_balanced

            if not root:
                return 0

            left_depth = depth(root.left)
            right_depth = depth(root.right)

            if abs(left_depth - right_depth) >= 2:
                is_balanced = False
            
            return 1 + max(depth(root.left), depth(root.right))

        depth(root)

        return is_balanced
        

        