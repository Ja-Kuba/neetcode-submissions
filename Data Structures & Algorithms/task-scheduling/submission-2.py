class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque() # cooldawn queue [t+n, task] when can be pushed back to tree

        cnts = Counter(tasks)

        # we add minus as its min heap and we seek for max cnts first
        theap = [[-cnt, v] for v, cnt in cnts.items()]

        heapq.heapify(theap)

        t=0 
        while theap or q:
            if theap:
                cnt, task = heapq.heappop(theap)
                if cnt < -1:
                    q.append([t+n, cnt+1, task])
            if q and q[0][0] == t:
                    _, cnt, task = q.popleft()
                    heapq.heappush(theap, [cnt,task])
            t+=1
            

        return t









            






"""
heap:

we want to store most frequent tasks
- key in priority tree

queue for waiting tasks


"""