class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 100
        max_profit = 0

        for i, p in enumerate(prices):
            if p < lowest:
                lowest = p
            
            if p - lowest > max_profit:
                max_profit = p - lowest


        return max_profit



"""
Input: prices = [10,1,5,6,7,1]

Output: 6
"""