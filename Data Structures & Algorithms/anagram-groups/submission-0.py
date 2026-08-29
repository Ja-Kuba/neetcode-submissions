class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d:dict[str, list[str]] = {} #sorted_str: values
        
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted in d:
                d[s_sorted].append(s)
            else:
                d[s_sorted] = [s]

        r = list()
        for k, v in d.items():
            r.append(v)
        
        return r

