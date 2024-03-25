class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        A = []
        #Greedy
        while n>0:
            x = min(26,k-(n-1))
            k -= x
            n -= 1
            A.append(x)
        a = ord('a')
        A = map(lambda y: chr(y-1+a), A[::-1])
        return "".join(A)