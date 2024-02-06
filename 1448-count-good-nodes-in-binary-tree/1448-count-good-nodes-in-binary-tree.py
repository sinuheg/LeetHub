# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def good_nodes_helper(root, greatest):
            if not root:
                return 0
            if root.val >= greatest:
                count = 1
                greatest = root.val
            else:
                count = 0
            count += good_nodes_helper(root.left, greatest)
            count += good_nodes_helper(root.right, greatest)
            return count
        return good_nodes_helper(root, root.val)
    
        