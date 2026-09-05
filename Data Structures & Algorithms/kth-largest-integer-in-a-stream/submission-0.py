
class MinHeap:
    def __init__(self, k, vals=None) -> None:
        self.heap = []
        self.k = k
        if isinstance(vals, list):
            self.fromList(vals)
    
    def fromList(self, vals:list):
        for i,v in enumerate(vals):
            self.add(v)

    def add(self, val):
        i = len(self.heap)
        #empty heap is not checked as question enusures it
        if i == self.k:
            return self._popmin(val)
            
        self.heap.append(val)
        while i > 0:
            pi = (i-1) // 2 #parent index 
            if self.heap[i] >= self.heap[pi]:
                break
            self.heap[i], self.heap[pi] = self.heap[pi], self.heap[i]
            i=pi
        
        return self.heap[0]

    def _popmin(self, val):
        if val <= self.heap[0]:
            return self.heap[0]
        self.heap[0] = val
        i = 0
        n = len(self.heap)

        while True:
            lci = 2*i+1
            rci = 2*i+2
            smallest = i
            if lci < n and self.heap[lci] < self.heap[smallest]:
                smallest = lci
            if rci < n and self.heap[rci] < self.heap[smallest]:
                smallest = rci
            
            if smallest == i:
                break
            
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            i = smallest

        return self.heap[0]







class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minh = MinHeap(k, nums)

    def add(self, val: int) -> int:
        return self.minh.add(val)
        
