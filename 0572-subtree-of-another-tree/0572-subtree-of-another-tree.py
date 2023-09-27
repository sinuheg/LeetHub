# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        if not root:
            return False
        if self.are_equal(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def are_equal(self, n1, n2):
        if not n1 and not n2:
            return True
        if (not n1 and n2) or (n1 and not n2):
            return False
        if n1.val != n2.val:
            return False
        return self.are_equal(n1.left, n2.left) and self.are_equal(n1.right, n2.right)