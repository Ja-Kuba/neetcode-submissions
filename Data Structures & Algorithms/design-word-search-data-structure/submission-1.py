class Node:
    def __init__(self, val, childs=[], is_leaf=False, is_end=False) -> None:
        self.childs = {} # char: Node
        self.is_end = is_end

   

class WordDictionary:

    def __init__(self):
        self.root = Node(val=None)

    # "apple" => explode 
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not c in curr.childs:
                n = Node(val=c)
                curr.childs[c] = n
            curr = curr.childs[c]
        
        curr.is_end = True

    def search(self, word: str, start_point=None) -> bool:
        curr = start_point if start_point else self.root 
        for i in range(len(word)):
            c = word[i]
            if c == ".":
                for ch in curr.childs.values():
                    ret = self.search(word[i+1:], ch)
                    if ret:
                        return True
                return False

            if c in curr.childs:
               curr = curr.childs[c]
            else:
                return False


        return curr.is_end
        

    
        