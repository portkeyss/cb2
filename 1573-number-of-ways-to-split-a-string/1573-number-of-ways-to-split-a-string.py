class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        ones = sum(c=="1" for c in s)
        if ones == 0: return comb(n-1,2)%(10**9+7)
        if ones%3: return 0
        l = ones//3
        i = 0
        ct = 0
        while ct < l:
            if s[i] == "1": ct += 1
            i += 1
        j = i
        while s[j]=="0":
            j += 1
        k = j
        while ct < 2*l:
            if s[k] == "1": ct += 1
            k += 1
        p = k
        while s[p]=="0":
            p += 1
        return ((j-i+1)*(p-k+1))%(10**9+7)