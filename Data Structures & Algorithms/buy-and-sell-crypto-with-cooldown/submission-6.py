class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {} # for i

        def dfs(i:int) -> int:
            if i in cache:
                return cache[i]

            if i >= len(prices):
                return 0

            max_prof = dfs(i+1)
            for j in range(i+1, len(prices)):
                prof =  prices[j] - prices[i] + dfs(j+2)
                max_prof = max(max_prof, prof)

            cache[i] = max_prof
            return max_prof
            
            
        max_prof =  0
        for i in range(0,len(prices)):
            max_prof = max(max_prof, dfs(i))

        return max_prof

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