class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        be = [[-1,-1] for _ in range(26)]
        for i,ch in enumerate(s):
            k = ord(ch)-ord("a")
            if be[k][0]==-1:
                be[k][0] = be[k][1] = i
            else:
                be[k][1] = i

        begins = sorted([b for b,_ in be])
        def bnxt(i):
            bidx = bisect_right(begins, i)
            return begins[bidx] if bidx<len(begins) else n

        @lru_cache(None)
        def f(i): #return the max number of Non-overlapping subs starting from index i
            if i==n: return [[],0]
            front = be[ord(s[i])-ord("a")][1]
            for j in range(i,n):
                if front<j: break
                k = ord(s[j])-ord("a")
                if be[k][0]<i: return f(bnxt(i))
                front = max(front,be[k][1])
            p = f(bnxt(front))
            cur = [[s[i:front+1]]+p[0],front+1-i+p[1]]
            q = f(bnxt(i))
            return cur if len(cur[0])>len(q[0]) or len(cur[0])==len(q[0]) and cur[1]<q[1] else q

        return f(0)[0]