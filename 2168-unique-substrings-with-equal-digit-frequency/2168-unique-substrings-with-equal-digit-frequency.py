class TrieNode:
    def __init__(self):
        self.seen = False
        self.children = dict()
        
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)
        trie = TrieNode()
        res = 0
        for i in range(n):
            count = [0]*10
            mxCount = 0
            unique = 0
            tn = trie
            for j in range(i,n):
                x = int(s[j])
                count[x] += 1
                if count[x]==1: unique += 1
                mxCount = max(mxCount, count[x])
                if s[j] not in tn.children:
                    tn.children[s[j]] = TrieNode()
                tn = tn.children[s[j]]
                if j-i+1==unique*mxCount and not tn.seen:
                    res += 1
                tn.seen = True
        return res