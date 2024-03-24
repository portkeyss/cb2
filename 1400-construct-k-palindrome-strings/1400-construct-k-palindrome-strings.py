class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        oddPalindromes = sum(ct%2 for ct in Counter(s).values())
        if oddPalindromes > k:
            return False
        evenPalindromes = k-oddPalindromes
        evenLength = len(s)-oddPalindromes
        if evenPalindromes > evenLength:
            return False
        return True