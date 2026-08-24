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
        if not head:
            return None

        mapping = {None: None}

        node = head
        while node:
            mapping[node] = Node(node.val)
            node = node.next
        
        node = head
        while node:
            mapping[node].next = mapping[node.next]
            mapping[node].random = mapping[node.random]
            node = node.next
        return mapping[head]