class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ret = True
        
        # build graph 
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        visited = set()


        #graph is tree when 1. no cycles  2. all nodes connected
        def dfs(node_idx, par_idx) -> bool:
            if node_idx in visited:
                return False
            visited.add(node_idx)
            for chi in graph[node_idx]:
                if chi == par_idx:
                    continue
                if not dfs(chi, node_idx):
                    return False

            return True
        
        r = dfs(0, -1)
        if r and len(visited) == n:
            return True
        else:
            return False


