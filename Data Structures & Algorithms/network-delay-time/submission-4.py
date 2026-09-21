class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for ui, vi, ti in times:
            g[ui].append((ti, vi))

        visited = set()
        minh = [(0,k)]
        min_time = 0

        while minh:
            ti, vi = heapq.heappop(minh)
            if vi in visited:
                continue
            visited.add(vi)
            min_time = max(min_time, ti)
            for nti, nvi in g[vi]:
                heapq.heappush(minh, (nti+ti, nvi))
            

        if len(visited) == n:
            return min_time
        else:
            return -1 
        




