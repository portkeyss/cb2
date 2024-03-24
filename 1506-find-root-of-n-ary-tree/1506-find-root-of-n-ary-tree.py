"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        a = 0
        for node in tree:
            a ^= node.val
            for child in node.children:
                a ^= child.val
        for node in tree:
            if node.val == a:
                return node