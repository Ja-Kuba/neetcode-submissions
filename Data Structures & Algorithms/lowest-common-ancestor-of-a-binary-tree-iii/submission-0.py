"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        visited = set() # visited nodes

        while True:
            if p and p.val in visited:
                return p
            if p:
                visited.add(p.val)
                p = p.parent
            
            if q and q.val in visited:
                return q
            if q:
                visited.add(q.val)
                q = q.parent
            

            



"""
p, q: nodes of binnary tree

their lowest common ancestor

p > q

1. we can start from the bigger one 

1. check childs if they have q
2. chek if paretn have q

binnary tree the bigger ones are on the right

        node
smaller     bigger



"""
