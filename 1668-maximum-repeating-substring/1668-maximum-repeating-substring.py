class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        #KMP
        n = len(sequence)
        m = len(word)
        r = n//m
        if r == 0: return 0
        maxRepeat = word*r
        def kmpTable(pattern):
            table = [-1]*(1+len(pattern)) #table entry means the fallback point, should current character mismatches. Note that is one index different than the lps convention
            j = 1
            k = 0
            while j < len(pattern):
                if pattern[j] == pattern[k]:
                    table[j] = table[k]
                else:
                    table[j] = k
                    while k>=0 and pattern[j] != pattern[k]:
                        k = table[k]
                j += 1
                k += 1
            table[j] = k
            return table
        T = kmpTable(maxRepeat)
        i, j = 0, 0
        res = 0
        while i < n:
            if sequence[i] == maxRepeat[j]:
                i += 1
                j += 1
                if j%m == 0:
                    res = max(res, j//m)
                    if j == len(maxRepeat): return j//m
            else:
                j = T[j]
                if j == -1:
                    i += 1
                    j += 1
        return res