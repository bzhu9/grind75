# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(root, lower, upper):
            if not root:
                return True
            if  lower >= root.val or root.val >= upper:
                return False
            return search(root.left, lower, root.val) and search(root.right, root.val, upper)
        return search(root, -2**32, 2**32)
