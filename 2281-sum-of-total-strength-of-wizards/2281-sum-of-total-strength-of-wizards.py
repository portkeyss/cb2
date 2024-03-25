class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        mod = 10**9+7
        n = len(strength)
        P = [0]*(n+1)
        Q = [0]*(n+1)
        a = 0
        b = 0
        for i,x in enumerate(strength):
            a += x
            b += i*x
            P[i+1] = a
            Q[i+1] = b
        res = 0
        stack = []
        A = [-1]*len(strength)
        for i,x in enumerate(strength):
            while stack and strength[stack[-1]]>=x:
                stack.pop()
            A[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []
        for j in reversed(range(len(strength))):
            while stack and strength[stack[-1]]>strength[j]:
                stack.pop()
            k = stack[-1] if stack else len(strength)
            i = A[j]
            p = (strength[j]*(j-i)*(k-j)
                 +(k-j)*(Q[j]-Q[i+1])
                 -(i*(k-j))*(P[j]-P[i+1])
                 +(j-i)*k*(P[k]-P[j+1])
                 -(j-i)*(Q[k]-Q[j+1])
                )*strength[j]
            res = (res+p)%mod
            stack.append(j)
        return res