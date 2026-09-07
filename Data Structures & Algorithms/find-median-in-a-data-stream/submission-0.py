class MedianFinder:

    def __init__(self):
        self.lvals = [] #max_heap of left subset
        self.rvals = [] #min_heap of right subset

    
    
    def addNum(self, num: int) -> None:
    #lets start from left heap is lens equal    
        if self.rvals and num >= self.rvals[0]:
            heapq.heappush(self.rvals, num)
        else:
            heapq.heappush(self.lvals, -num)


        #balance tree
        if len(self.lvals) < len(self.rvals):
            #right -> left
            rv = heapq.heappop(self.rvals)
            heapq.heappush(self.lvals, -rv)
        
        elif len(self.lvals) > len(self.rvals) + 1:
            #left -> right
            lv = heapq.heappop(self.lvals)
            heapq.heappush(self.rvals, -lv)




    def findMedian(self) -> float:
        if len(self.rvals) == len(self.lvals):
            return  (-self.lvals[0] + self.rvals[0]) / 2
        else:
            # we balance tree to store +1 val in left heap
            return -self.lvals[0]        
        