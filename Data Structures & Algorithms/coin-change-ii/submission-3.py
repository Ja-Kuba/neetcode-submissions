class Solution:
    def change_dfs(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(cind, t) -> int:
            if (cind, t) in cache:
                return cache[(cind, t)]
                
            if t == 0:
                return 1
            elif t < 0:
                return 0

            perms = 0
            for next_ind in range(cind, len(coins)):
                perms+=dfs(next_ind, t-coins[next_ind])

            cache[(cind, t)] = perms
            return perms

        r = dfs(0, amount)  

        return r
    
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)

        dp[0] = 1 #as only one combination to get there - zero coins []

        
        for c in coins:
            for i in range(c, len(dp)):
                dp[i]+= dp[i-c]
        
        print(dp)
        return dp[amount]


 



"""
integer array coins  coins = [1,2,3] is it orderd? coins are psoitive and unique
amount - target money


Request:
 distinct combinations that total up to amount
 t = 5  [1,1,1,2] vs [2,1,1,1] -> from the example its same

 distinct means diff freq of each coin value

if not possible return 0

amount 4

dp[4] -> how many postibilitis from here

for n in coins:
    dp[]


"""