class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        #construct a matrix
        a = sum(i%2==0 and s[i]=="0" for i in range(n))
        b = sum(i%2==0 and s[i]=="1" for i in range(n))
        c = sum(i%2==1 and s[i]=="0" for i in range(n))
        d = sum(i%2==1 and s[i]=="1" for i in range(n))
        if a==d:
            if b==c: return min(a,b)
            else: return a
        else:
            if b==c: return c
            else:
                return -1