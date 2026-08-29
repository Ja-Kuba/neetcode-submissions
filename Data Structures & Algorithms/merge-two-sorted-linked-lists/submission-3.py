# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:    
        s = d = ListNode(0)

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

        return s.next