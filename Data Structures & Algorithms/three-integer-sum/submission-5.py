class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results:list[list[int]]= []
        numbers = sorted(nums)
        start = 0
        while start < len(numbers)-2:
            if start>0 and numbers[start] == numbers[start-1]:
                #skip du
                start+=1
                continue

            l = start+1
            r = len(numbers) - 1
            while l < r:
                csum = numbers[start] + numbers[l] + numbers[r]
                if csum == 0:
                    results.append([numbers[start], numbers[l], numbers[r]])
                    l+=1  
                    while numbers[l] == numbers[l-1] and l < r:
                        l+=1
                elif csum > 0:
                    #if sum bigger the zero we need smaller number in next iter
                    r-=1
                else: #csum < 0
                    l+=1

            start+=1

        return results
