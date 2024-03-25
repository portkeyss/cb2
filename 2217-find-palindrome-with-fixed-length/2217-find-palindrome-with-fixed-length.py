class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:      
        p = ((intLength+1)//2)
        odd = intLength%2
        
        def f(idx):
            if idx>10**p-10**(p-1): return -1
            half = 10**(p-1)+idx-1
            halfStr = str(half)
            if odd:
                return int(halfStr+halfStr[-2::-1])
            else:
                return int(halfStr+halfStr[::-1])
        
        return map(f,queries)