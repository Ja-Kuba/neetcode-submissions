class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        cache = {} # nums: prize

        def dfs(nums) -> int:
            if tuple(nums) in cache:
                return cache[tuple(nums)] 
            if not nums:
                #no ballons left to pop
                return 0
            
            max_prize = 0
            for i, n in enumerate(nums):
                l = nums[i-1] if i-1 >= 0 else 1
                r = nums[i+1] if i+1 < len(nums) else 1
                
                prize = (l * n * r) + dfs(nums[:i]+nums[i+1:]) 
                
                max_prize = max(max_prize, prize)

            cache[tuple(nums)] = max_prize
            return max_prize
        

        return dfs(nums)





'''

[int]: nums of size n

nums[i] - baloon int value 
- positive? yes 0 <= nums[i] <= 100
    but can be zero!

TASK:
burst all of the baloons

if burst i-th
REWARD:
    nums[i - 1] * nums[i] * nums[i + 1]
    out of bounds gives values 1 

ASK:
Return the maximum number of coins you can receive by bursting all of the balloons.


After pop we remove only ith balloon rest stay in array

APROACH:

dfs(nums, i=0)

in i-th postition:
    1. pop 
        - count price  nums[i - 1] * nums[i] * nums[i + 1]
        - dfs(nums.remove(i), i=0) <- maybe we can optimiez sttart position later?
    2. skip
        - dfs(nums, i+1)

stop condition: nums -> empty

'''