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


        # lambda is not required as val has default val, but if not this is example how to 
        # set def val in defaultdict
        newnodes = defaultdict(lambda: Node(0)) # oldNode: newNode 

        def dfs(node): 
            if node in newnodes:
                return newnodes[node]
            
            newnodes[node].val = node.val
            for nn in node.neighbors:
                newnodes[node].neighbors.append(dfs(nn))
            
            return newnodes[node]
        

        ret = dfs(node)

        return ret