# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        p1 = head
        p2 = head
        
        while p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next
            if p2 == p1:
                return True
            
                
        return False


