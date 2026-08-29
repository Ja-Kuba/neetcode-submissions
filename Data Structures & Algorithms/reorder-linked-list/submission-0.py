# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast= head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        h2 = slow.next
        slow.next = None

        # h2.prev -> h2 -> h2.next
        prev = None
        while h2:
            tmp = h2.next
            h2.next = prev 
            prev = h2
            h2 = tmp
        
        h1 = head
        h2 = prev
        while h2:
            tmp1 = h1.next 
            tmp2 = h2.next
            h1.next = h2
            h2.next = tmp1
            h1 = tmp1
            h2 = tmp2
            
            

"""
Input: head = [2,4,6,8]

Output: [2,8,4,6]
"""