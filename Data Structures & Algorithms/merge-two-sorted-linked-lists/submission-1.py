# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        newList = ListNode(0, list1) 
        i = newList
        while curr1 is not None and curr2 is not None:
            
            if curr1.val <= curr2.val:
                i.next = curr1
                curr1 = curr1.next
            else:
                i.next = curr2
                curr2 = curr2.next

            i = i.next
        if curr1:
            i.next = curr1
        else:
            i.next = curr2
        return newList.next
