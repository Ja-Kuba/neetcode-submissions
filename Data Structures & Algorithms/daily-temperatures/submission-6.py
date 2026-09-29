class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp,index)
        results = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack:
                if stack[-1][0] < t:
                    _, j = stack.pop()
                    results[j] = i -j
                else:
                    break
            stack.append((t,i))

        return results


"""
[int]: temperatures
temp[i] - temp at ith day

RETURN:
[int] result

 0    1  2  3  4  5  6  7  8
[30, 29, 30,36,35,40,28,25,27]
 1       1
[(38,1) 36,3   ]
i - p

dp[len(temps)] = 0


"""