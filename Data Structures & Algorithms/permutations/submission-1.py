class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(first: int):
            if first == len(nums):
                res.append(nums.copy())
                return

            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]  # place choice
                dfs(first + 1)
                nums[first], nums[i] = nums[i], nums[first]  # backtrack (undo)

        dfs(0)
        return res