class Solution:
    def checkString(self, s: str) -> bool:
        return "".join(sorted(list(c for c in s)))==s