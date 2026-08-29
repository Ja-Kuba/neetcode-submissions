class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 1: 
            return 0
        solid_mass = sum(height)
        high = max(height)
        i, j = 0, n-1
        def running(nums):
            i, trapped = 0,0
            running_max = 0

            while nums[i] < high:
                running_max = max(running_max, nums[i])
                trapped += running_max
                i+=1
            return trapped, i

        left_trapped, left_high = running(height)

        right_trapped, right_high = running(height[::-1])

        print(left_trapped, left_high)
        print(right_trapped, right_high)
        return left_trapped + right_trapped + (n-right_high - left_high )*high - solid_mass