class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def f(x, y):
            a = sum(sqrt((x-a)**2+(y-b)**2) for a,b in positions)
            return a
        
        def df(x, y, psi=10**(-16)):
            b = (sum((x-a)/(sqrt((x-a)**2+(y-b)**2)+psi) for a,b in positions), sum((y-b)/(sqrt((x-a)**2+(y-b)**2)+psi) for a,b in positions))
            return b
        
        def stepsize(x,y,d0=1.0):
            d = d0
            grad = df(x,y)
            p = f(x,y)
            while f(x-grad[0]*d, y-grad[1]*d)-p > -gamma*d*(grad[0]**2+grad[1]**2):
                d *= beta
            return d
        
        gamma = 0.0001
        beta = 0.8
        epsilon = 10**(-8)
        
        x, y = sum(x for x, _ in positions)/len(positions), sum(y for _,y in positions)/len(positions)
        prev_f = f(x,y)
        while True:
            d = stepsize(x,y)
            grad = df(x,y)
            x -= grad[0]*d
            y -= grad[1]*d
            cur_f = f(x,y)
            if cur_f - prev_f > -epsilon:
                return cur_f
            prev_f = cur_f