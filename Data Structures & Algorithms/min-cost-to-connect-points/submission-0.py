class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        mdist = lambda p1, p2: abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        visited = set()
        n = len(points) 
        total_dist = 0 
        mheap = [(0, points[0])]
        
        while mheap:
            d, p = heapq.heappop(mheap)
            if tuple(p) in visited:
                continue
            visited.add(tuple(p))
            total_dist+=d
            for np in points:
                if tuple(np) in visited:
                    continue
                nd = mdist(p, np)
                heapq.heappush(mheap, (nd, np))

        
        return total_dist