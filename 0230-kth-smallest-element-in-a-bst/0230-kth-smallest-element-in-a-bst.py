# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def count_in_order(head, curr):
            nonlocal result
            if not head:
                return curr
            curr = count_in_order(head.left, curr)
            curr += 1
            if curr == k:
                result = head.val
            return count_in_order(head.right, curr)
        result = None
        count_in_order(root, 0)
        return result
        