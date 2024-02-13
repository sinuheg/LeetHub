# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove_node(node):
            if not node:
                return None, 0
            new_next,next_length = remove_node(node.next)
            next_length += 1
            if next_length == n:
                return new_next, next_length
            else:
                node.next = new_next
                return node, next_length
        new_head,_ = remove_node(head)
        return new_head

        