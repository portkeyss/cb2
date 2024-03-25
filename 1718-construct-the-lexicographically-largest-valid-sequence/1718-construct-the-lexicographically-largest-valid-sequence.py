class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        @lru_cache(None) 
        def f(mask1,mask2,k):
            if mask1==0: return [0]*(2*n-1)
            else:
                while k<2*n-1 and (1<<k)&mask2==0:
                    k += 1
                for j in range(n-1,0,-1):
                    if mask1&(1<<j) and mask2&(1<<(k+j+1)):
                        x = f(mask1^(1<<j),mask2^(1<<k)^(1<<(k+j+1)),k+1)
                        if x:
                            x[k] = x[k+j+1] = j+1
                            return x
                if mask1&1:
                    x = f(mask1^1,mask2^(1<<k),k+1)
                    if x:
                        x[k] = 1
                        return x 
                return []

        return f((1<<n)-1, (1<<(2*n-1))-1,0)