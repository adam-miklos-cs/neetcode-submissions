# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -1001
        def pathSumEndingIn(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if not node:
                return 0

            l = pathSumEndingIn(node.left)
            r = pathSumEndingIn(node.right)

            ans = max(ans, node.val, node.val + l, node.val + r, node.val + l + r)

            return max(node.val, node.val + l, node.val + r)

        pathSumEndingIn(root)
        return ans