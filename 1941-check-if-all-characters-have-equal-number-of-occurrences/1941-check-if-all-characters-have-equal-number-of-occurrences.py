class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        return len(set(count.values()))==1