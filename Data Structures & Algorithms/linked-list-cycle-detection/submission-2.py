# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast=fast.next
            else:
                break
            if fast == slow:
                return True


        return False