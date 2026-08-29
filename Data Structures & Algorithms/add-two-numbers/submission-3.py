# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = res = ListNode(0)
        carry = 0 
        while l1 or l2 or carry >0:
            if l1:
                carry+=l1.val                
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            f = carry%10
            carry = carry//10
            res.next = ListNode(f)
            res = res.next
   
                    
        return dummy.next