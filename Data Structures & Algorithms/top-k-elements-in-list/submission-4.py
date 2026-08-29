class Solution:
    def topKFrequent_sorting(self, nums: List[int], k: int) -> List[int]:
        unique_nums = set(nums)
        
        num_counts = {k: 0 for k in unique_nums}

        for n in nums:
            num_counts[n]+=1

        counts = list()
        for num, cnt in num_counts.items():
            counts.append((num, cnt))
        
        nums = [num for num, cnt in sorted(counts, key=lambda x: x[1])]
        return nums[-k:]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Bucket sort solution O(n) 
        """
        
        count = defaultdict(int) #defualt is 0 cuz  int() == 0
        freq = [[] for _ in range(len(nums)+1)] # +1 cuz <0, len()>

        for n in nums:
            count[n]+=1
        for n, c in count.items():
            freq[c].append(n)


        res = []
        i = len(freq)-1 
        while len(res) < k and i > 0:
            for n in freq[i]:
                print("append")
                res.append(n)
            i -= 1


        return res

'''
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
'''