# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        
        dummy = ListNode(0, head)
        prev = dummy
        
        for _ in range(l - n):
            prev = prev.next
        
        prev.next = prev.next.next

        return dummy.next

            