class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        curr_max_area = 0
        htrack = [] # (height, index)

        # nie updatujemy poprzednich pozcycji na stacku???
        for i, currh in enumerate(heights):
            start = i ## <-- sprytny trikas
            while htrack and htrack[-1][0] > currh:
                h, index = htrack.pop()
                curr_max_area = max(curr_max_area, h * (i-index))
                start = index #move curretn start index to start of the last higer 
            htrack.append((currh, start))
            
        for h, spos in htrack:
            area = h * (len(heights) - spos)
            if area > curr_max_area:
                curr_max_area = area


        return curr_max_area