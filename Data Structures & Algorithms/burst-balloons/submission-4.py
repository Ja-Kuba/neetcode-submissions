class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}

        def dfs(nums, i):
            state = (tuple(nums), i)

            if state in cache:
                return cache[state]

            # no balloons left
            if not nums:
                return 0

            # we've skipped every possible balloon
            if i == len(nums):
                return 0

            # ----------------
            # 1. POP nums[i]
            # ----------------
            l = nums[i - 1] if i > 0 else 1
            r = nums[i + 1] if i + 1 < len(nums) else 1

            remaining = nums[:i] + nums[i + 1:]

            pop = l * nums[i] * r
            pop += dfs(remaining, 0)

            # ----------------
            # 2. SKIP nums[i]
            # ----------------
            skip = dfs(nums, i + 1)

            best = max(pop, skip)

            cache[state] = best
            return best

        return dfs(nums, 0)