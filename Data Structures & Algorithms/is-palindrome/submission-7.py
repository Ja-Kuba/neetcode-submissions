class Solution:
    def isPalindrome(self, s: str) -> bool:
        shift = ord("a") - ord("A")  

        def is_valid_char(c):
            cc = ord(c)
            if cc >= ord("A") and cc <= ord("Z"):
                ret = cc + shift
            elif cc >= ord("a") and cc <= ord("z"):
                ret =  cc
            elif cc >= ord("0") and cc <= ord("9"):
                ret =  cc
            else:
                ret = 0
            return ret
        
        start_i = 0
        end_i = len(s) -1
        while start_i <= end_i:
            start_c = is_valid_char(s[start_i])
            end_c = is_valid_char(s[end_i])
            if start_c and end_c:
                if start_c == end_c:
                    start_i+=1
                    end_i-=1
                else:
                    return False

            if not end_c:
                end_i-=1
            if not start_c:
                start_i+=1
            

        return True





"""
Input: s = "Was it a car or a cat I saw?"

Output: true
"""