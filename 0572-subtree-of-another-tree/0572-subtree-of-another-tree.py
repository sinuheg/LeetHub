# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def are_equal(n1, n2):
            if not n1 and not n2:
                return True
            if (not n1 and n2) or (n1 and not n2):
                return False
            if n1.val != n2.val:
                return False
            return are_equal(n1.left, n2.left) and are_equal(n1.right, n2.right)
        
        if not root and not subRoot:
            return True
        if not root:
            return False
        if are_equal(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        