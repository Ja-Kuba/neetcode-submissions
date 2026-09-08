class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def run(left, right):
            cache = {}  # nums_ind: max_value

            def dfs(i) -> int:
                if i in cache:
                    return cache[i]
                if i > right:
                    return 0

                r = nums[i] + max(dfs(i + 2), dfs(i + 3))
                cache[i] = r
                return r


            return max(dfs(left), dfs(left + 1))

        return max(run(0, len(nums) - 2), run(1, len(nums) - 1))