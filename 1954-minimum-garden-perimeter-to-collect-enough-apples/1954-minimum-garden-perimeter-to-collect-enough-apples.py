class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def f(x):
            return 2*x*(x+1)*(2*x+1)
        
        r = 1
        while f(r)<neededApples:
            r *= 2
        l = r//2
        while l < r:
            m = (l+r)//2
            if f(m)<neededApples:
                l = m+1
            else:
                r = m
        return 8*r