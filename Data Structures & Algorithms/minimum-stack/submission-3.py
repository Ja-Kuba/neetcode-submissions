class MinStack:    
    def __init__(self ):
        self.stack=[]
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack: 
            self.min_stack.append(val)
        elif val <= self.getMin(): 
            # smaller or equal to handle duplicates like [push -3 push -3]
            self.min_stack.append(val)
            
        
    def pop(self) -> None:
        if self.stack.pop() == self.getMin():
            self.min_stack.pop()    

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
