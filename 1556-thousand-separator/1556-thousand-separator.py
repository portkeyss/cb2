class Solution:
    def thousandSeparator(self, n: int) -> str:
        l = str(n)
        p = []
        i = len(l)%3
        if i>0: p.append(l[:i])
        while i<len(l):
            p.append(l[i:i+3])
            i += 3
        return ".".join(p)