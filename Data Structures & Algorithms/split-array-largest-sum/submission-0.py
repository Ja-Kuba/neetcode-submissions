from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Minimum possible answer: largest individual element
        left = max(nums)

        # Maximum possible answer: put everything in one subarray
        right = sum(nums)

        def can_split(max_sum: int) -> bool:
            subarrays = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num

                    if subarrays > k:
                        return False
                else:
                    current_sum += num

            return True

        while left < right:
            mid = (left + right) // 2

            if can_split(mid):
                # mid works, try a smaller maximum
                right = mid
            else:
                # mid is too small
                left = mid + 1

        return left