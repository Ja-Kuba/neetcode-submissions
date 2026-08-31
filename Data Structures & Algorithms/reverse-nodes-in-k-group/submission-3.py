# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # not matching the task but fun solution

    def print_list(self, l):
        while l:
            print(l.val, end="")
            l = l.next
        print("\n")

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        d = ListNode(0) 
        end = d
        d.next = head

        while head:
            for i in range(k-1):
                if head:
                    head = head.next
                else:
                    break

            if head:
                tmp_head = head.next
                tmp_end_next = end.next
                end.next = None
                head.next = None
                h, last = self.reverse_l(tmp_end_next)

                end.next = h
                last.next = tmp_head
                head = tmp_head
                end = last
            else:
                break
                


        
        return d.next
         


    def reverse_l(self, l:Optional[ListNode]):
        if not l:
            return None, None

        # None -> 0 -> 1 -> 2
        # None <- 0 <- 1 <- 2
        #             prev  l
        last = l 
        prev = None
        while l:
            tmp = l.next
            l.next = prev
            prev = l
            l = tmp

        return prev, last 
        