# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -1000

        def dfs_sum(root)->int:
            nonlocal max_sum
            if not root:
                return 0
            
            cur_val = root.val
            l_val = dfs_sum(root.left)
            r_val = dfs_sum(root.right)

            max_sum = max(
                max_sum, 
                (l_val + r_val + cur_val),  
                cur_val,
                l_val + cur_val,
                r_val + cur_val
            )

            return max(
                cur_val, 
                l_val + cur_val,
                r_val + cur_val
            )
         

        dfs_sum(root)

        return max_sum