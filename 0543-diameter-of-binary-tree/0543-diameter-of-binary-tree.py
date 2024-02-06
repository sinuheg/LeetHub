# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def diameterOfBinaryTreeHelper(root: TreeNode) -> int:
            nonlocal max_length
            if root is None:
                return 0
            left_length = diameterOfBinaryTreeHelper(root.left)
            right_length = diameterOfBinaryTreeHelper(root.right)
            current = left_length + right_length + 1
            max_length = max(max_length, current)
            return max(left_length, right_length) + 1
        max_length = 1
        diameterOfBinaryTreeHelper(root)
        return max_length -1
        
        
        