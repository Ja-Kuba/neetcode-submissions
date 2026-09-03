class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph  with dict representation
        preMap = {i: [] for i in range(numCourses)}
            
        for course, preq in prerequisites:
        # apparently u can unpack the list that way - if matching len
            preMap[course].append(preq)

        visited = set()
        done = []

        
        def dfs(c, order):
            if c in visited: 
                return False
            if not preMap[c]:
                if c not in done:
                    done.append(c)
                    order.append(c)
                return True

            visited.add(c)
            for n in preMap[c]:
                if not dfs(n, order):
                    return False
            visited.remove(c)
            # everything after this node is checked
            preMap[c] = []
            if c not in done:
                order.append(c)
                done.append(c)
            return True


        order = []
        for c in preMap.keys():
            if not dfs(c, order):
                return []

        
        return order