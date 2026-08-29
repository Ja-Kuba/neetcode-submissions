class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i, v1 in enumerate(nums):
            for ii in range(i+1, l):
                if v1 + nums[ii] == target:
                    return [i, ii]




