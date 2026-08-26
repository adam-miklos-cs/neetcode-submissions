# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def dfs(current: Optional[TreeNode], depth: int):
            if not current:
                return

            if depth == len(ans):
                ans.append([])

            ans[depth].append(current.val)

            dfs(current.left, depth + 1)
            dfs(current.right, depth + 1) 
        
        dfs(root, 0)

        return ans