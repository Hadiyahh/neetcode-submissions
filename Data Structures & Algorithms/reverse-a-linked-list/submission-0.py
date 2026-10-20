# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: 
            return head
        prev = None
        fast = head

        while fast is not None:
            temp = fast.next
            fast.next = prev
            prev = fast
            fast = temp
        return prev
