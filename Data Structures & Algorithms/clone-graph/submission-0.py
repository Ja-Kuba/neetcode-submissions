"""
# Definition for a Node.
class Node:, reveal_type
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None


        newnodes = defaultdict(Node) # oldNode: newNode
        visited = set()

        def dfs(node): 
            newnodes[node].val = node.val
            if node in visited:
                return
            visited.add(node)
            for nn in node.neighbors:
                tmp_n = newnodes[nn]
                newnodes[node].neighbors.append(tmp_n)
                dfs(nn)
        

        dfs(node)

        return newnodes[node]