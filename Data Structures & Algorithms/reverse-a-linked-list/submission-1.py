# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #head -> n1 -> n2 

        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head=tmp
        
        return prev


    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #not in place
        last=None
        while head:    
            last = ListNode(val=head.val, next=last)
            head = head.next

        return last

         