class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}

        res =[]
        start = 0
        end = 0
        for i, c in enumerate(s):
            end = max(last[c], end)
            
            if i == end:
                res.append(end-start+1)
                start = end+1
        
        return res

        """
        "xyxxyzbzbbi"
        x: 3
        y: 4
        z: 7
        b: 9
        i: 10
        """

        