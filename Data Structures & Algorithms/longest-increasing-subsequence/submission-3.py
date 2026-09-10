from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for n in nums:
            # check on what position n would be inserted
            i = bisect_left(lis, n)
            if i == len(lis):
                # we insert at the end
                lis.append(n)
            else:
                # cuz we do bisect_left
                # [3,7] insert 2 would return i = 0 
                # we change slot of 3 -> 2 for searching 
                # new potential lis
                lis[i] = n

        return len(lis)



"""
len(lis) -> gives info about currnet longest increasing subsequnce
values on lis gives smallest posiibilities

for 2:
[1,7,8,10] -> [1,2,8,10]
we change 7 to 2 as when the next number comes bigger its still valid

when 11 comes is still valid for 7 and 2, but 6 wont match 7 
so we would lose the info



[1,7,8,10, 2, 11]


[1,7,8,10, 2, 3 , 4 ,11, , 4,5 ,5]
            ^
max oredered List
lis = [1,2,3,4,5]
         
bisect_left = 1

"""