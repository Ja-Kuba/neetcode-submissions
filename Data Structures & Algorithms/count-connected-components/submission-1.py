class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        groups = 0

        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            for cn in graph[n]:
                dfs(cn)



        for n, _ in graph.items():
            if n not in visited:
                dfs(n)
                groups+=1


        return groups  

