class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack:list[int] = []
        for t in tokens:    

            match t:
                case "+":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(int(l + r))
                case "-":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(int(l - r))                    
                case "*":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(int(l * r))                      
                case "/":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(int(l / r))                    
                case _:
                    stack.append(int(t))


        
        return stack.pop() 







"""
Input: tokens = ["1","2","+","3","*","4","-"]
Output 5 
"""