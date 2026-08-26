# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        negative_inf = -1001
        positive_inf = 1001
        
        def limiting_dfs(root: Optional[TreeNode], lower_bound: int, upper_bound: int) -> bool:
            if not root:
                return True
            if root.val <= lower_bound or upper_bound <= root.val:
                return False
            return (limiting_dfs(root.left, lower_bound, root.val) and
                   limiting_dfs(root.right, root.val, upper_bound))

        return limiting_dfs(root, negative_inf, positive_inf)

        

        