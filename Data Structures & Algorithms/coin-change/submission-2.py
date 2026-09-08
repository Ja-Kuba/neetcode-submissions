class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = set() # {amount} if amount in cache we can stop - this path already exists
        

        q = collections.deque()
        q.append((amount,0))
        
        if amount==0:
            return 0

        while q:
            a, cnt = q.popleft()
            if a in cache:
                continue
            cache.add(a)
            print(f'{a=}, {cnt=}')
            for c in coins:
                if a - c > 0:
                    q.append((a-c, cnt+1))
                elif a - c == 0:
                    return cnt+1                    


        return -1







"""
as the coins length is 0 to 10 we can just sort it
we go bfs as we want to find shortest path
we can also add cache, whaaaay not

"""