class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sums = {0: 1} #sum_value: cnt

        csum = 0
        result = 0
        for n in nums:
            csum+=n
            d = csum - k 
            if d in sums:
                result+=sums[d]

            sums[csum] = sums.get(csum, 0) +1

        return result


# [-2, 1 , 3, -1 , 4] k =2
#
"""
sums:
-1 :1
 1 :1
 



"""








"""

[int]: nums
int: k 

RETURN:
total number fo subarray whose sum == k

dfs aproach:

dfs(i, sum)
if sum == k
    return 1  
if sum > k:
    return 0

if end and sum < k
    return 0

return dfs(0,0)



"""