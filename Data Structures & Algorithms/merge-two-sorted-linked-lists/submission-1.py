# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        curr1 = list1
        curr2 = list2

        if curr1.val < curr2.val:
            head = ListNode(curr1.val)
            curr1 = curr1.next
        else:
            head = ListNode(curr2.val)
            curr2 = curr2.next
        
        last = head
        while True:
            print(last.val)
            if not (curr1 or curr2):
                break
            elif not curr1:
                tmp = ListNode(curr2.val)
                curr2 = curr2.next
            elif not curr2:
                tmp = ListNode(curr1.val)
                curr1 = curr1.next
            elif  curr1.val < curr2.val:
                tmp = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                tmp = ListNode(curr2.val)
                curr2 = curr2.next
            
            last.next = tmp
            last = tmp

        return head

        
        
