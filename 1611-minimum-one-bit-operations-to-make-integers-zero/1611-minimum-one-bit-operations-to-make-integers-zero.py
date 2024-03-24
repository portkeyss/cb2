class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        memo1 = dict()
        memo2 = dict()
        def f(m, bit): #turning binary XXXXX to 0
            if m in memo1: return memo1[m]
            if m == 0: memo1[m] = 0
            elif m == 1: memo1[m] = 1 
            elif 1<<bit & m == 0: memo1[m] = f(m, bit-1)
            else: memo1[m] = g(1<<bit ^ m, bit-1) + 1 + f(1<<(bit-1), bit-1)
            return memo1[m]
        
        def g(m, bit): #turning binary XXXXX to 10000, i.e., 1<<bit
            if (m, bit) in memo2: return memo2[(m,bit)]
            if bit == 0:
                if m == 0: memo2[(m, bit)] = 1
                elif m == 1: memo2[(m, bit)] = 0
            elif 1<<bit & m != 0: memo2[(m, bit)] = f(1<<bit ^ m, bit-1)
            else: memo2[(m, bit)] = g(m, bit-1) + 1 + f(1<<(bit-1), bit-1)
            return memo2[(m, bit)]
        
        return f(n, 32)