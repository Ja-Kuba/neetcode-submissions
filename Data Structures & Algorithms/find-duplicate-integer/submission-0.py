class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = 0
        s2 = -1
            
        f = nums[nums[f]]
        s = nums[s]

        while f != s:
            f = nums[nums[f]]
            s = nums[s]

        s2=0
        while s != s2:
            s = nums[s]
            s2 = nums[s2]

        return s



