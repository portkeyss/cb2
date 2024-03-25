class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ct1 = Counter(word1)
        ct2 = Counter(word2)
        p1 = set(ct1.keys())
        p2 = set(ct2.keys())
        if p1!=p2: return False
        l1 = sorted(list(ct1.values()))
        l2 = sorted(list(ct2.values()))
        return l1==l2