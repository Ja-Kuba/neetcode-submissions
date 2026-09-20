class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        mdist = lambda p1, p2: abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        visited = set()
        n = len(points) 
        total_dist = 0 
        mheap = [(0, 0)] # dist, index
        
        while mheap:
            d, i = heapq.heappop(mheap)
            if i in visited:
                continue
            visited.add(i)
            p = points[i]
            total_dist+=d
            for j, np in enumerate(points):
                if j in visited:
                    continue
                nd = mdist(p, np)
                heapq.heappush(mheap, (nd, j))

        
        return total_dist