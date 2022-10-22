# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    d = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if (root == None):
                return 0
            lh = height(root.left)
            rh = height(root.right)
            if lh+rh > self.d:
                self.d = lh+rh
            return max(lh, rh)+1
        height(root)
        return self.d
