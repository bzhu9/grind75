# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, root):
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.recurse(root.left)
            self.recurse(root.right)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recurse(root)
        return root
