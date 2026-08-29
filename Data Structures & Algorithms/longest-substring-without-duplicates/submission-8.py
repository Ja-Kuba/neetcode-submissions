class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        track = {} #{char: pos}
        longest = 0
        p=0 #current substring start index 
        i=0
        for i, c in enumerate(s):
            if c in track:
                p=max(p,track[c]+1)
            track[c] = i
            longest=max(longest, i-p+1)
        


        return longest



"""
Input: s = "zxyzxyz"

Output: 3
"""