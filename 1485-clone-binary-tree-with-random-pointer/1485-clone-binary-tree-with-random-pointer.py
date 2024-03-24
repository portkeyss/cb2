# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if root is None:
            return None
        newNodes = {}
        def buildNodes(node):
            newNodes[node] = NodeCopy(node.val)
            if node.left:
                buildNodes(node.left)
            if node.right:
                buildNodes(node.right)
            
        def buildLinks(node):
            if node.left:
                newNodes[node].left = newNodes[node.left]
                buildLinks(node.left)
            if node.right:
                newNodes[node].right = newNodes[node.right]
                buildLinks(node.right)
            if node.random:
                newNodes[node].random = newNodes[node.random]
        
        buildNodes(root)
        buildLinks(root)
        return newNodes[root]