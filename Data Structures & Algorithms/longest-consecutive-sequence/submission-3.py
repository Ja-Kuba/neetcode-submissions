class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0


        nums_s = set(nums)
        seen = set()

        longest = 0
        for n in nums_s:
            if n-1 not in nums_s:
                l = 1
                while n+l in nums_s:
                    l+=1
                if l > longest:
                    longest = l
                


        return longest


    def longestConsecutive_sort(self, nums: List[int]) -> int:
        """
        sorting complexity == O(nlogn)
        """
        if len(nums) == 0:
            return 0

        nums_s = sorted(nums)

        l = 1
        longest = 0
        last = nums_s[0]
        for n in nums_s:
            if n == last:
                continue
            elif n == last+1:
                l+=1
            else:
                if l > longest:
                    longest = l 
                l = 1
            
            last = n

        if l > longest: 
            longest = l

        return longest




"""
Input: nums = [2,20,4,10,3,4,5]

Output: 4
"""