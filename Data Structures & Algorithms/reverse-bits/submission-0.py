class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        p = 31
        while n:
            res+=(n&1)*(2**p)
            p-=1
            n=n>>1

        return res