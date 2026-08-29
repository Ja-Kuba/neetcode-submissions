# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        

        def bfs(root):
            if not root:
                return []
            
            lvl=0
            q = collections.deque()
            q.append((root, 0))
            res = [[]]
            while q:
                node, lvl = q.popleft()
                # if node.val == target:
                #     return node

                if len(res) <= lvl:
                    res.append([])
                res[lvl].append(node.val)

                if node.left:
                    q.append((node.left, lvl+1))

                if node.right:
                    q.append((node.right, lvl+1))
            
            return res

            
        return bfs(root)

        

        
