class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        A = Counter()
        for word in words:
            A[word] += 1
        res = 0
        odd = False
        for w in A:
            if w[::-1] not in A: continue
            if w[0]==w[1]:
                res += (A[w]//2)*4
                if A[w]%2==1: odd=True
            else:
                res += min(A[w], A[w[::-1]])*2
        if odd: res += 2
        return res        