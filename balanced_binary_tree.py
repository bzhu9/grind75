# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    bal = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None: 
            return True
        self.height(root)
        return self.bal
    
    def height(self, root):
        if (root == None): 
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        if (abs(l-r) > 1):
            self.bal = False
        return max(l, r)+1
