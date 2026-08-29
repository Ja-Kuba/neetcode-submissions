class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #stop condition
        curr_max = 0
        l, r = 0, len(heights)-1
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            if area > curr_max:
                curr_max = area
            
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
            




        return curr_max