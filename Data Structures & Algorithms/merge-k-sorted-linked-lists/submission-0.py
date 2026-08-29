# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not len(lists):
            return None

        while len(lists) > 1:
            merged = []
            for k in range(0, len(lists), 2):
                r = self.mergeLists(lists[k], (lists[k+1] if  k+1 < len(lists) else None))
                merged.append(r)
            lists = merged
        
        return lists[0]
    


    def mergeLists(self, l1, l2):
        
        guard = d = ListNode(0)

        while l1 or l2:
            if not l1:
                d.next = l2
                break
            elif not l2:
                d.next = l1
                break

            if l1.val < l2.val:
                d.next = l1
                l1 = l1.next
            else:
                d.next = l2
                l2 = l2.next

            d = d.next
        
        return guard.next




        


"""
iterate through 




"""