"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        state = defaultdict(lambda: Node(0))
        state[None] = None

        h = head
        while h:
            state[h].val = h.val
            state[h].next = state[h.next]
            state[h].random = state[h.random]
            h = h.next

        return state[head]
             