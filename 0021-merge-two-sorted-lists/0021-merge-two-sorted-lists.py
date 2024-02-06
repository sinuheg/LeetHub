# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:            
        if not list1:
            return list2
        if not list2:
            return list1
        result = None
        tail = None
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val < curr2.val:
                aux = curr1
                curr1 = curr1.next
            else:
                aux = curr2
                curr2 = curr2.next
            if not result:
                result = aux
                tail = aux
            else:
                tail.next = aux
                tail = aux
        if curr1:
            tail.next = curr1
        if curr2:
            tail.next = curr2
        return result

        