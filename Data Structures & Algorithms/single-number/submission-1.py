class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for n in nums:
            r ^=n

        return r






'''
[int]: nums

 Every integer appears twice except for one.

 Return the integer that appears only once.

'''


"""
     XOR
1 1  0 
1 0  1
0 1  1
0 0  0

"""