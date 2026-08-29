class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map:dict = {} #VAL: index

        for i, v in enumerate(nums):
            diff = target - v
            if diff in hash_map:
                return [hash_map[diff], i]
            
            hash_map[v] = i



    
    #     l = len(nums)
    #     for i, v1 in enumerate(nums):
    #         for ii in range(i+1, l):
    #             if v1 + nums[ii] == target:
    #                 return [i, ii]



    
