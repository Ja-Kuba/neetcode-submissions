class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #write with Kahn ALg
        g = {i: [] for i in range(numCourses)}
        indegree = [0]*numCourses
        order = []
        q = collections.deque()

        for a,b in prerequisites:
            #b -> a we need take b to take append
            g[b].append(a)
            indegree[a]+=1

        for c, deg in enumerate(indegree):
            if deg == 0:
                q.append(c)

        while q:
            c = q.popleft()
            order.append(c)
            for nc in g[c]:
                indegree[nc]-=1
                if indegree[nc] == 0:
                    q.append(nc)


        return order if len(order) == numCourses else []

        
