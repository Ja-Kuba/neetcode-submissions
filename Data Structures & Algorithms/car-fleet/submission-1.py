class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = list(zip(position, speed))
        cars.sort(key = lambda x: x[0], reverse=True)

        for p, v in cars:
            # v = d / t  => t= d/v
            time = (target-p)/v            


            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
                
        
        return len(stack)
        



'''
Input: target = 10, position = [1,4], speed = [3,2] n - cars

Output: 1
'''