
def eDist(p1, p2=[0,0]):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    return (math.sqrt((x1 - x2)^2 + (y1 - y2)^2))



class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        dist = lambda x, y: x**2+y**2

        for x, y in points:
            heapq.heappush(heap, [-dist(x,y), x, y])
            if len(heap) > k:
                heapq.heappop(heap)
       
        ret = []
        while heap:
            _, x,y = heapq.heappop(heap)
            ret.append([x,y])

        return ret