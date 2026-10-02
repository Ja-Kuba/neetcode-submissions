class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0]*numCourses
        g = {i: list() for i in range(numCourses)}
        order = []

        for a, b in prerequisites:
            g[b].append(a)
            indegree[a]+=1     
        
        
        q = collections.deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        

        while q:
            i = q.popleft()
            order.append(i)

            for c in g[i]:
                indegree[c]-=1
                if indegree[c] == 0:
                    q.append(c)

        
        return order if len(order) == numCourses else []



        
        
        