# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(node):
            new_head = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = new_head
                new_head = curr
                curr = temp
            return new_head
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        half = reverse(slow.next)
        slow.next = None
        curr1 = head
        curr2 = half
        while curr2:
            temp = curr1.next
            curr1.next = curr2
            temp2 = curr2.next
            curr2.next = temp
            curr1 = temp
            curr2 = temp2
        
        
        