class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        results:list[int] = [0]*len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            if len(stack) == 0: 
                stack.append((t,i))
                continue
            
            if t <= stack[-1][0]:
                stack.append((t,i))
            else:
                # print(stack)
                p = stack[-1]
                while t > p[0]:
                    # print(f'{t} > {p[0]}')
                    # print(f'{p[1]}: {i - p[1]}')
                    results[p[1]] = i - p[1]
                    stack.pop()
                    if len(stack) == 0:
                        break
                    p = stack[-1]

                stack.append((t,i))
        
# [30,38,30,36,35,40,28]

# stack = 30, 38
                


        return results



"""
Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
"""