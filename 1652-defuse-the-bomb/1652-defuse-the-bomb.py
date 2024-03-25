class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k==0: return [0]*n
        rvs = False
        if k<0: 
            code = code[::-1]
            k *= -1
            rvs = True
        res = []
        cur = sum(code[:k])
        for i in range(n):
            cur = cur-code[i]+code[(i+k)%n]
            res.append(cur)
        return res if not rvs else res[::-1]