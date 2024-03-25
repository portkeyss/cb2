class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask = 0
        prefix = Counter()
        prefix[0]=1
        res = 0
        for c in word:
            bit = ord(c)-ord('a')
            mask ^= 1<<bit
            res += prefix[mask]
            res += sum(prefix[(mask^(1<<b))] for b in range(10))
            prefix[mask] += 1
        return res
        