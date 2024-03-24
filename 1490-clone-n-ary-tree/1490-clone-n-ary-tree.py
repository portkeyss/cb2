"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        def cloneT(node):
            newNode = Node(node.val)
            newNode.children = [cloneT(child) for child in node.children]
            return newNode
        return cloneT(root)