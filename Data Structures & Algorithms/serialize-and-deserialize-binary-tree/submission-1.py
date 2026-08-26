# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = ""
        def build_str(node: Optional[TreeNode]):
            nonlocal s
            if not node:
                s += 'N' + ' '
                return
            
            s += str(node.val) + ' '
            build_str(node.left)
            build_str(node.right)
        
        build_str(root)
        print(s)
        return s



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0
        tokens = data.split()
        def build_tree() -> Optional[TreeNode]:
            nonlocal i
            nonlocal tokens

            if tokens[i] == 'N':
                return None
            
            node = TreeNode(int(tokens[i]))

            i += 1
            node.left = build_tree()
            i += 1
            node.right = build_tree()

            return node
        
        return build_tree()
        

            
            
