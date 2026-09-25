class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 0
        res = []
        digits[-1]+=1
        for i in range(len(digits)-1, -1, -1):
            d = digits[i] + carry
            carry = 0
            if d >= 10:
                res.append(d%10)
                carry = d // 10
            else:
                res.append(d)
        if carry:
            res.append(carry)
        res.reverse()
        return res