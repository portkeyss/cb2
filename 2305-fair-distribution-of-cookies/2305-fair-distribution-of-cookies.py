class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        A = [[0]*k]
        for c in cookies:
            B = set()
            for l in A:
                for i in range(k):
                    h = list(l)   
                    h[i]+=c
                    h = tuple(sorted(h))   
                    B.add(h)
            A = B
        return min(max(l) for l in A)