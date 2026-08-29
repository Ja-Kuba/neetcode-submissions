# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invertNode(node):
            if not node:
                return None
            
            tmp = node.left
            node.left = invertNode(node.right)
            node.right = invertNode(tmp)

            return node

        return invertNode(root)

        
        




        
        
        

    