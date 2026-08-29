class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1
        """
        numbers=[1,2,3,4]
        target=3
        """
        r_flag = False
        while l < r:
            csum = numbers[l] + numbers[r]
            if csum == target:
                break
            elif csum > target:
                r-=1
            else: #csum < target
                l+=1

        
        return [l+1,r+1]