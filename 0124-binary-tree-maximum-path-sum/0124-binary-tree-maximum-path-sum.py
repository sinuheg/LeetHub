# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def get_max_sum(root: TreeNode):
            if not root:
                return 0
            nonlocal max_sum
            left_gain = max(get_max_sum(root.left), 0)
            right_gain = max(get_max_sum(root.right), 0)
            new_path = root.val + left_gain + right_gain
            max_sum = max(max_sum,new_path)
            return root.val + max(left_gain, right_gain)
        get_max_sum(root)
        return max_sum