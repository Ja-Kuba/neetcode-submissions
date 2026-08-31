class TimeMap:

    def __init__(self):
        self.data: dict[str, List] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.data:
            self.data[key] = list()
        self.data[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.data:
            return ""
        
        return self.search(timestamp, self.data[key])
    
    
    def search(self, t:int, l:list) -> str:
        #binary search for timestamp match or closest
        ret = self.binary_search(0, len(l)-1, t, l)
        if ret[0] > t:
            return ""
        else:
            return ret[1]
        
    def binary_search(self, l:int, r:int, t:int, ls:list) -> tuple[int, str]:
        if l > r:
            return (-1, "")

        m = l + (r-l) // 2
        tm, vm = ls[m]

        if tm == t:
            return (tm, vm)
        
        elif tm > t:
            return self.binary_search(l, m-1, t, ls)
        else:# tm =< t
            rt, rv = self.binary_search(m+1, r, t, ls)
            if rt==-1:
                return (tm, vm)
            else:
                return (rt, rv)
        


"""

dict: { "key": list[timestamp; value] }

when set -> add in ascending order to list:
    1. add to the end og f list as timestamp are strictly increasing

when get ->
    perform binnary search.
        do not search for exact match as it may not be there
        serach for equal or smaller -> store it
        if no exact match return the closest one to required

"""