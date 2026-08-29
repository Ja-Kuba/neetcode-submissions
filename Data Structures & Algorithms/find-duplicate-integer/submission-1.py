class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f = nums[nums[0]]
        s = nums[0]
        s2 = 0

        while f != s:
            f = nums[nums[f]]
            s = nums[s]

        while s != s2:
            s = nums[s]
            s2 = nums[s2]

        return s



