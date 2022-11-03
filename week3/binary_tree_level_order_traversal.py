# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}
        def depth (node, l):
            if node:
                depth(node.left, l + 1)
                depth(node.right, l + 1)
                if l in d:
                    d[l].append(node.val)
                else:
                    d[l] = [node.val]
        depth(root, 0)
        return [d[key] for key in sorted(d)]

