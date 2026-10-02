class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        md = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        minh = [(0,0)] #dist,index
        visited  = set()
        cost = 0
        while minh: 
            d, i = heapq.heappop(minh)
            if i in visited:
                continue
            visited.add(i)
            cost+=d
            p = points[i]
            for j, np in enumerate(points):
                if j in visited:
                    continue
                npd = md(p, np)
                heapq.heappush(minh, (npd, j))
            
        
        return cost
