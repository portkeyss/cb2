class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        
        @lru_cache(None)
        def f(r,p): #r is current row, p is the pattern of the lower row   
            if r==-1: return 0
            A = [0]
            for c in range(n):
                B = []
                for a in A:
                    B.append(a)
                    if (c==0 or (1<<(c-1))&p==0) and (c==n-1 or (1<<(c+1))&p==0) and (c==0 or a&(1<<(c-1))==0) and seats[r][c]==".":
                        B.append(a|1<<c)
                A = B
            ans = 0
            for x in B:
                s = 0
                y = x
                while y>0:
                    s += 1
                    y &= y-1
                ans = max(ans, s+f(r-1, x))
            return ans
        
        return f(m-1,0)  