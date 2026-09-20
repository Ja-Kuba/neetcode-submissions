class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for ui, vi, ti in times:
            g[ui].append((ti, vi))
        
        print(g)
        
        minh = [(0,k)]
        visited = set()
        min_time = -1

        while minh:
            d, node = heapq.heappop(minh)
            if node in visited:
                continue
            visited.add(node)
            min_time = max(min_time, d)

            for ti, vi in g[node]:
                heapq.heappush(minh, (d+ti, vi))

        
        return min_time if len(visited) == n else -1



"""
grph: network of n directed nodes,
    labeled from 1 to n
n- nodes
"""     