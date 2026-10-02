class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        longest = 0
        for i, c in enumerate(s):
            while c in chars:
                chars.remove(s[l])
                l+=1
            chars.add(c)
            longest = max(longest, i-l+1)

        return longest
            
            # set = c
            #[a,b,c,c]
            # 0 1 2 