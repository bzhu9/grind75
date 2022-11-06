"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        newgraph = {}
        def clone (node):
            new = Node(node.val)
            newgraph[node] = new
            for n in node.neighbors:
                if n in newgraph:
                    new.neighbors.append(newgraph[n])
                else:
                    new.neighbors.append(clone(n))
            return new
        return clone(node) if node else None
        
