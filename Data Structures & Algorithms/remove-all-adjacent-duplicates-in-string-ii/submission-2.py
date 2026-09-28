class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        st = [] #[c,cnt]
 
        for c in s:
            if st and st[-1][0] == c:
                st[-1][1]+=1
            else:
                st.append([c,1]) 
            
            if st[-1][1] == k:
                st.pop()



        res=[]
        for c,cnt in st:
            res+=[c]*cnt

        return "".join(res)


# aabaagggabb
# aaab



"""
str: s
int: k 

aabaaggg k=3
aabaa

1. aabaagggabb
2. aabaagggabb

stack = [(a,2),(b,1),(a,2),(g,3)]
- we add to stack when char change
- if current char len = k we remove and pop from stack to set as last
- then process further as nothing can be removed
O(n) time O(n) stack worst case


s = "deeedbbcccbdaa"
k = 3

stack = [d1,]
process e , e3 remove
pop d,1
stack=[]
d,2
b,1
stack push [d,2]
b,2
c1
stack = [d,2, b2]
c2
c3 = remove
pop b2 stack = [d,2]
b3 -remove:
pop d2 stack = []
d3 remov
a1
a2 
/EOS
return


"""