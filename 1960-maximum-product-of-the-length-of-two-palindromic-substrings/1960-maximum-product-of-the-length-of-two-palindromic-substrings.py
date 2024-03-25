class Solution:
    def maxProduct(self, s: str) -> int:
        def manacher(t):
            m = len(t)
            p = [0]*m
            l = -1
            r = -1
            for i in range(m):
                if i<r:
                    p[i]=min(p[l+(r-i)],r-i)
                while i-p[i]>=0 and i+p[i]<m and t[i-p[i]]==t[i+p[i]]:
                    p[i] += 1
                if i+p[i]>r:
                    l = i-p[i]
                    r = i+p[i]
            return p

        n = len(s)
        p = manacher(s)
        
        q1 = deque()
        q2 = deque()
        A = [0]*n
        for i in range(n-1,-1,-1):
            while q1 and q1[0][0]-q1[0][1]+1>i:
                q1.popleft()
            q1.append((i,p[i]))
            A[i] = 1 if i==n-1 else max(A[i+1],(q1[0][0]-i)*2+1)
        l = 0
        res = 0
        for i in range(n-1):
            while q2 and q2[0][0]+q2[0][1]-1<i:
                q2.popleft()
            q2.append((i,p[i]))
            l = max(l, (i-q2[0][0])*2+1)
            res = max(res, l*A[i+1])
        return res