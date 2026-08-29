class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_len = [f"{len(s):03d}" for s in strs]        
        encoded_list_tmp = [f"{len(strs):03d}"] + strs_len + strs
        
        ret = "".join(encoded_list_tmp)
        
        print(ret)

        return ret
            
            


    def decode(self, s: str) -> List[str]:
        s_cnt = int(s[0:3])
        data_start_index = 3 + s_cnt*3
        decoded_str = []
        for c in range(1, s_cnt+1):
            str_len = int(s[3*c:3*c+3])
            decoded_str.append(s[data_start_index:data_start_index+str_len])
            data_start_index+=str_len
        
        return decoded_str



"""
Input: strs = ["Hello","World"]

Output: ["Hello","World"]
"""