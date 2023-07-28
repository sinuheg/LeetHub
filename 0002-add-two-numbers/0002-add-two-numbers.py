# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1pointer = l1
        l2pointer = l2
        newpointer = None
        endpointer = None
        carry = 0
        while l1pointer or l2pointer:
            l1value = 0
            if l1pointer:
                l1value = l1pointer.val
                l1pointer = l1pointer.next
            l2value = 0
            if l2pointer:
                l2value = l2pointer.val
                l2pointer = l2pointer.next
            result = l1value + l2value + carry
            newval = result % 10
            carry = result // 10
            
            newnode = ListNode(newval)
            if not newpointer:
                newpointer = newnode
            if endpointer:
                endpointer.next = newnode
            endpointer = newnode
        
        if carry > 0:
            newnode = ListNode(carry)
            endpointer.next = newnode
        
        return newpointer