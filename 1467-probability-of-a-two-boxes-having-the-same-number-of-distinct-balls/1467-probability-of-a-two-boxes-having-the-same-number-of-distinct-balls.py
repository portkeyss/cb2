class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n, N = len(balls), sum(balls)
        fac = [factorial(i) for i in range(7)]
        
        self.tot = 0
        self.perm = 0
        
        def dfs(pos, count1, count2, color1, color2, prm1, prm2):
            if count1==count2==N//2:
                self.tot += prm1*prm2
                self.perm += (color1==color2)*prm1*prm2
                return
            if count1<=N//2 and count2<=N//2: 
                for b1 in range(balls[pos]+1):
                    b2 = balls[pos]-b1
                    dfs(pos+1,count1+b1, count2+b2, color1+(b1>0), color2+(b2>0), prm1//fac[b1], prm2//fac[b2])
                
        dfs(0, 0, 0, 0, 0, factorial(N//2), factorial(N//2))
        return self.perm/self.tot