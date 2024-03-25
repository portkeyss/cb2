class Trie:
    def __init__(self):
        self.children = dict()
        
class Solution:
    def countDistinct(self, s: str) -> int:
        n = len(s)
        root = Trie()
        res = 0
        for i in range(n):
            t = root
            for j in range(i,n):
                if s[j] not in t.children:
                    t.children[s[j]]=Trie()
                    res += 1
                t = t.children[s[j]]
        return res