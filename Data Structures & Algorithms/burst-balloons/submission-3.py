class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        cache = {}
        def dfs(l, r):
            if(l,r) in cache:
                return cache[(l,r)]
            if l+1 == r:
                # we iter all nums
                return 0
            

            best = 0
            for i in range(l+1,r):
                prize = nums[l]*nums[i]*nums[r]
                prize += dfs(l, i)
                prize += dfs(i, r)
                best = max(best, prize)

            cache[(l,r)] = best
            return best

        return dfs(0, len(nums)-1)


'''

[int]: nums - of size n

int: nums[i] - baloon value
 - positive intiger
 - but may be zero

nums[i - 1] * nums[i] * nums[i + 1]

Return the maximum number of coins you can receive by bursting all of the balloons.


[4,2,3,7]
          



'''