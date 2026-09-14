class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {} # for i

        def dfs(i:int, holding:bool) -> int:
            if (i, holding) in cache:
                return cache[(i, holding)]

            if i >= len(prices):
                return 0

            #skip buing today
            if not holding:
                max_prof = max(
                    dfs(i+1, False), #not buys
                    dfs(i+1, True) - prices[i]
                )
            else: # holding == True
                max_prof = max(
                    prices[i] + dfs(i+2, False),
                    dfs(i+1, True)
                )

            cache[(i, holding)] = max_prof
            return max_prof
            
            

        return dfs(0, False)

'''

prices  on ith day.

NeetCoin multiple times:
1. buy
2. sell

Constraints:
1. After you sell your NeetCoin, you cannot buy another one on the next day 
    1 day cooldown after sell


2. One neetcoin at a time


Output: max profit


lets check from end

profit = sum(sells - buys)
0 <= prices[i] <= 1000 only positives

if we can buy and sell only once

dp[i] - max profit
d[i] = 

prices = [1,3,4,0,4]
0: 1
   if buy 
   profit max(for j in i+1:len(proces))
        -> get_profit(j, prices[i+2:], ) <+2 as we need cooldown

 if i >= len(prices): return 0 <- only positive numbers
      

'''