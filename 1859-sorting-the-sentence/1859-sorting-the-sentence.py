class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        A = [None]*len(s)
        for x in s:
            i = 0
            while i<len(x) and x[i].isalpha():
                i += 1
            A[int(x[i:])-1]=x[:i]
        return " ".join(A)