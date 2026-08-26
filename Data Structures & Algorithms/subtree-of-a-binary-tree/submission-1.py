# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "$#"
        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))

    def prefix_function(self, s: str) -> list:
        n = len(s)
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]
            if s[i] == s[j]:
                j += 1
            pi[i] = j
        return pi   

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = self.serialize(root)
        serialized_subRoot = self.serialize(subRoot)
        combined = serialized_subRoot + "|" + serialized_root

        pi_values = self.prefix_function(combined)
        sub_len = len(serialized_subRoot)

        for i in range(sub_len + 1, len(combined)):
            if pi_values[i] == sub_len:
                return True
        return False