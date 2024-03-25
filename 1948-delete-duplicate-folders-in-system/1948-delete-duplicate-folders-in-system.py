class TrieNode:
    def __init__(self):
        self.val = None
        self.delete = False
        self.children = defaultdict(TrieNode)
        
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        paths.sort()
        root = TrieNode()
        root.val = "/"
        for path in paths:
            node = root
            for x in path:
                node = node.children[x]
                node.val = x
                
        seen = dict()
        def f(tn):
            subpath = ""
            if tn.children:
                for a in tn.children:
                    subpath += f(tn.children[a])
                if subpath in seen.keys():
                    seen[subpath].delete = True
                    tn.delete = True
                else:
                    seen[subpath] = tn
            return "("+tn.val+subpath+")"
        
        f(root)
 
        res = []
        buffer = []
        def g(tn):
            for a,b in tn.children.items():
                if b.delete: continue
                buffer.append(a)
                res.append(buffer[::])
                g(b)
                buffer.pop()
        g(root)
        return res