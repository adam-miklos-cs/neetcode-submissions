# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root: Optional[TreeNode], maxim: int):
            nonlocal ans
            if not root:
                return 

            if root.val >= maxim:
                maxim = root.val
                ans += 1

            dfs(root.right, maxim)
            dfs(root.left, maxim)
        
        dfs(root, -101)

        return ans