class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we change stones to negative as heapq is the mintree implementetion
        stones = [-s for s in stones]
        heapq.heapify(stones)

        print(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            # -6 -4
            if s1 != s2:
                heapq.heappush(stones, s1 - s2)
        
        return -stones[0] if stones else 0





"""
Input: stones = [2,3,6,2,4]

Output: 1
"""