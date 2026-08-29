class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        oset = set(['(','{', '['])
        cset = set([')','}', ']'])

        brackets = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        for c in s:
            if c in oset:
                stack.append(c)
            elif c in cset:
                if len(stack) == 0 or brackets[stack.pop()] != c:
                    return False
            else: 
                continue

        if len(stack) != 0:
            return False
        
        return True

    


"""

Input: s = "([{}])"

Output: true

"""