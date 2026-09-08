class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = nums[0]
        minval=1
        maxval=1

        curr = 1
        for n in nums:
            tmp = maxval * n
            maxval = max(n*maxval, n*minval, n)
            minval = min(tmp, n*minval, n)
            res = max(res, maxval)

            

        return res