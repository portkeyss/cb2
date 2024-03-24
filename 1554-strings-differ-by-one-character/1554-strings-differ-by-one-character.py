class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        n, m = len(dict), len(dict[0])
        mod = 1000000007
        hs = []
        for i in range(n):
            h = 1
            for j in range(m):
                h = (26*h+ord(dict[i][j])-ord('a'))%mod
            hs.append(h)
        
        for j in range(m):
            A = defaultdict(list)
            for i in range(n):
                h = (hs[i]-pow(26,m-1-j,mod)*(ord(dict[i][j])-ord('a')))%mod
                if h in A:
                    for k in A[h]:
                        if dict[k][:j]+dict[k][j+1:]==dict[i][:j]+dict[i][j+1:]:
                            return True
                A[h].append(i)
        return False