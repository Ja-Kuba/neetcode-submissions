class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # d:dict[str, list[str]] = {} #sorted_str: values
        d = defaultdict(list)
        for s in strs:
            s_sorted = ''.join(sorted(s))
            d[s_sorted].append(s)

        
        return list(d.values())


        