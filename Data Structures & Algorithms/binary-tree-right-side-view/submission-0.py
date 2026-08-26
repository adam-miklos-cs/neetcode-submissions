# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        depth_seen = -1
        ans = []
        def dfs(root: Optional[TreeNode], depth: int):
            nonlocal depth_seen
            nonlocal ans
            if not root:
                return 
                
            if depth == depth_seen + 1:
                ans.append(root.val)
                depth_seen += 1
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
        
        dfs(root, 0)
        return ans

            

        