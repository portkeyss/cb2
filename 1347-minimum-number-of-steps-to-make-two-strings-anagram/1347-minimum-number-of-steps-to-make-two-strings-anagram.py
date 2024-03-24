class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter1 = Counter(s)
        counter2 = Counter(t)
        res = 0
        for c in string.ascii_lowercase:
            res += max(0, counter1[c]-counter2[c])
        return res