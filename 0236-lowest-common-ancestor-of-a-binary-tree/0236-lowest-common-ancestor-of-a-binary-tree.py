# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_branch(node):
            nonlocal lowest_ancestor
            if not node:
                return False
            left_result = find_branch(node.left)
            right_result = find_branch(node.right)
            curr_result = node == p or node == q
            
            if left_result + right_result + curr_result >= 2:
                lowest_ancestor = node
            return left_result or right_result or curr_result
        lowest_ancestor = None
        find_branch(root)
        return lowest_ancestor
        