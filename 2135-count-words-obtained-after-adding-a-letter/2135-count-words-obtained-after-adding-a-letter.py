class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        A = set()
        def encode(x):
            y = 0
            for ch in x:
                y += 1<<(ord(ch)-ord("a"))
            return y
        for s in startWords:
            A.add(encode(s))
        res = 0
        for t in targetWords:
            y = encode(t)
            res += any(y^(1<<(ord(ch)-ord("a"))) in A for ch in t)
        return res 