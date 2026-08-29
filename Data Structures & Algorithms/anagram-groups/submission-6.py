class Solution:
    # not optiomal
    def groupAnagrams_sort(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)  #sorted_str: values
        for s in strs:
            s_sorted = ''.join(sorted(s))
            d[s_sorted].append(s)

        
        return list(d.values())


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)  #sorted_str: values
        
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] +=1
            
            d[tuple(count)].append(s) 
            # d[count].append(s) # <--- dict is unhashable type


        
        return list(d.values())
