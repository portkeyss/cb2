class Solution:
    def minimumKeypresses(self, s: str) -> int:
        A = sorted(list(Counter(s).values()),reverse=True)
        return sum((i//9+1)*a for i,a in enumerate(A))