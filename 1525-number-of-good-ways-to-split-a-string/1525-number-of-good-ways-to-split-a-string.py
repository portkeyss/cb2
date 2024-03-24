class Solution:
    def numSplits(self, s: str) -> int:
        leftCounter = Counter()
        rightCounter = Counter(s)
        res = 0
        for c in s:
            leftCounter[c] += 1
            rightCounter[c] -= 1
            if rightCounter[c] == 0:
                rightCounter.pop(c)
            if len(leftCounter) == len(rightCounter):
                res += 1
        return res