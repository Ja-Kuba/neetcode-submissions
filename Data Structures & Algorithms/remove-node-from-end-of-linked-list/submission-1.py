# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nth_pointer = head
        prev = None
        
        s = head
        for i in range(n):
            s = s.next
        
        while s:
            prev, nth_pointer = nth_pointer, nth_pointer.next
            s = s.next

        if prev:
            prev.next = nth_pointer.next
        else:
            head = nth_pointer.next

        return head
         