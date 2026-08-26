class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        s = [root]
        j = 0
        
        for i in range(1, len(preorder)):
            new_node = TreeNode(preorder[i])
            
            # State A: The left subtree is still being built
            if  s[-1].val != inorder[j]:
                s[-1].left = new_node
                s.append(new_node)

            # State B: The left subtree is complete
            else:
                while s and s[-1].val == inorder[j]:
                    parent = s[-1]
                    s.pop()
                    j += 1
                parent.right = new_node
                s.append(new_node)
                
        return root