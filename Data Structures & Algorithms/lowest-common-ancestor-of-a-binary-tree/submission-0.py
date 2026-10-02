# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', qn: 'TreeNode') -> 'TreeNode':
        
        parent = {root:None}

        q = collections.deque([root])

        while q:
            n = q.popleft()

            if n.left:
                parent[n.left] = n
                q.append(n.left)
            if n.right:
                parent[n.right] = n
                q.append(n.right)

        ancest = set()
        while p:
            ancest.add(p)
            p = parent[p]
        q= qn
        while q:
            if q in ancest:
                return q
            q = parent[q]
