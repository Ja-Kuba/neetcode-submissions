class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {}

        def dfs(t, v):
            if (t, v) in cache:
                return cache[(t, v)]

            # exact fill -> multiplicative identity
            if t == 0:
                return 1
            # invalid
            elif t < 0 or v == 0:
                return 0

            max_prod = 0
            # choose next part size up to v (and up to remaining t)
            for n in range(1, min(v, t) + 1):
                sub = dfs(t - n, n)
                if sub > 0:
                    max_prod = max(max_prod, sub * n)

            cache[(t, v)] = max_prod
            return max_prod

        max_prod = 0
        # force at least two parts by taking first cut nn, then solve remainder
        for nn in range(1, n):
            max_prod = max(max_prod, nn * dfs(n - nn, n - nn))

        return max_prod
        