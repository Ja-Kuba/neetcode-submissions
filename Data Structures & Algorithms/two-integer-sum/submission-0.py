class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v1 in enumerate(nums):
            for ii, v2 in enumerate(nums):
                if i == ii:
                    continue
                
                if v1 + v2 == target:
                    return [i, ii]

        