
def buildPatter(w:str, pos:int)->str:
    return w[:pos] + "*" + w[(pos + 1):]


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 

        
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                nei[buildPatter(word,j)].append(word)
        
        
        q = collections.deque()
        q.append((beginWord, 0)) # word, bfs dist
        visited = set()
        
        while q:
            w, lvl = q.popleft()
            if w in visited:
                continue
            if w == endWord:
                return lvl+1
            visited.add(w)
            for i in range(len(w)):
                pat = buildPatter(w,i)
                for n in nei[pat]:
                    q.append((n,lvl+1))
            
        return 0


