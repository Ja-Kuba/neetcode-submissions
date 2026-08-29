# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        tree_nodes:list[str] = [] 
        if root:
            q = collections.deque()
            lvl=0
            q.append(root)

            if_empty_lvl = False

            while q:
                n = q.popleft()
                if not n:       
                    tree_nodes.append("N")
                    continue 
                
                tree_nodes.append(f"{n.val}")
                q.append(n.left)
                q.append(n.right)
        else:
            tree_nodes.append("N")

        return ";".join(tree_nodes)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nl = data.split(";") #nodes_list 

        if not nl or nl[0] == "N":
            return None
        
        root = TreeNode(val=int(nl[0]))
        q = collections.deque()
        q.append(root)

        i = 0
        while q:
            n = q.popleft()
            if n == "N":
                continue
            
            i+=1
            if nl[i] != "N":
                n.left = TreeNode(val=int(nl[i]))
                q.append(n.left)
            i+=1
            if nl[i] != "N":
                n.right = TreeNode(val=int(nl[i]))
                q.append(n.right)

        
        return root
                
                
                










