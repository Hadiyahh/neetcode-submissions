# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        fast = head
        slow = head

        for i in range(n):
            fast = fast.next

        # Special case: removing the head
        if fast is None:
            return head.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        print("slow",slow.val)
        print("fast", fast)
        slow.next = slow.next.next

        return head