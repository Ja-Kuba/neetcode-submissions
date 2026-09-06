class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
    
        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]


"""
Input: nums = [2,3,1,5,4], k = 2

Output: 4
"""