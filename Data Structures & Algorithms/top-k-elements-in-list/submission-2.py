class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_nums = set(nums)
        
        num_counts = {k: 0 for k in unique_nums}

        for n in nums:
            num_counts[n]+=1

        counts = list()
        for num, cnt in num_counts.items():
            counts.append((num, cnt))
        
        nums = [num for num, cnt in sorted(counts, key=lambda x: x[1])]
        return nums[-k:]

            




'''
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
'''