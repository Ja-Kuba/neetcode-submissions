class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # g:dict[int, list[tuple]] = defaultdict(list)
        
        # for from_i, to_i, price_i in flights:
        #     g[from_i].append((price_i, to_i))

        prices = [float('inf')]*n
        prices[src] = 0

        for _ in range(k+1):
            #as we want 
            pr_tmp = prices.copy()
            for from_i, to_i, price_i in flights:
                p = price_i + prices[from_i]
                if p < pr_tmp[to_i]:
                    pr_tmp[to_i] = p
            
            prices = pr_tmp


        return int(prices[dst]) if prices[dst] < float('inf') else -1 
