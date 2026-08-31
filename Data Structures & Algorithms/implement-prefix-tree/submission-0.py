

class Node:
    def __init__(self, val, parent, childs=[], is_leaf=False, is_end=False) -> None:
        self.val = val 
        self.parent = parent
        self.childs = {} # char: Node
        self.is_leaf = is_leaf
        self.is_end = is_end

    @property
    def v(self):
        return self.val
   

class PrefixTree:

    def __init__(self):
        self.root = Node(val=None ,parent=None)

    # "apple" => explode 
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not c in curr.childs:
                n = Node(val=c, parent=curr)
                curr.childs[c] = n
            curr = curr.childs[c]
        
        curr.is_leaf = True

    def search(self, word: str, starts_with=False) -> bool:
        curr = self.root
        for c in word:
            if c in curr.childs:
               curr = curr.childs[c]
            else:
                return False
        if curr.is_leaf or starts_with:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, starts_with=True)
        
        


