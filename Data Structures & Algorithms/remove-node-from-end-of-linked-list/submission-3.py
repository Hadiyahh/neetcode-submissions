# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        curr = head
        length = 0

        while curr is not None:
            curr = curr.next
            length += 1
     
      
   
        pos = length - n
        
        if pos == 0:
            # head =  head.next
            # return head
            return head.next
        
        curr = head
        prev = head

        for i in range(pos - 1): 
            curr = curr.next
            
        # Skip the node we want to remove
        curr.next = curr.next.next

        return head