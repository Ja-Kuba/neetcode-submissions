class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build graph  with dict representation
        preMap = {i: [] for i in range(numCourses)}
            
        for course, preq in prerequisites:
        # apparently u can unpack the list that way - if matching len
            preMap[course].append(preq)

        visited = set()

        
        def dfs(c):
            if c in visited: 
                return False
            if not preMap[c]:
                return True

            visited.add(c)
            for n in preMap[c]:
                if not dfs(n):
                    return False
            visited.remove(c)
            # everything after this node is checked
            preMap[c] = []
            return True


        for c in preMap.keys():
            if not dfs(c):
                return False

        
        return True

        

        
        

