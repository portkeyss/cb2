# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        n = len(s)
        t = []
        i = 0
        while i<n:
            if s[i].isnumeric():
                j = i+1
                while j<n and s[j].isnumeric(): j += 1
                t.append(s[i:j])
                i = j
            else:
                t.append(s[i])
                i += 1
        
        stack = []
        A = dict()
        for i in reversed(range(len(t))):
            if t[i]==")":
                stack.append(i)
            elif t[i]=="(":
                A[stack.pop()] = i
        
        def f(start,end):
            if t[end]==")" and A[end]==start: return f(start+1,end-1)
            if start==end: return TreeNode(t[start])
            i = end
            j = None
            while i>start:
                if t[i]==")": i = A[i]-1
                elif t[i] in "+-": break
                elif t[i] in "*/" and j is None:
                    j = i
                    i -= 1
                else: i-=1
            k = i if i>start else j
            node = TreeNode(t[k])
            node.left = f(start,k-1)
            node.right = f(k+1, end)
            return node
            
        return f(0,len(t)-1)