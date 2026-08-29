class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        res, water = 0, 0
        while l < n and height[l] == 0:
            l += 1 
        for r in range(l + 1, n):
            if height[r] < height[l]:
                water += height[l] - height[r]
            else:
                l = r
                res += water
                water = 0
        print(res, water)
        if water > 0:
            water = 0
            for l in range(r, l - 1, -1):
                if height[l] < height[r]:
                    water += height[r] - height[l]
                else:
                    r = l
                    res += water
                    water = 0 
        return res