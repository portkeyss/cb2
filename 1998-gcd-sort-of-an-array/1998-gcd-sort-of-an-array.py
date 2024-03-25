class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        #union find
        n = max(nums)+1
        rank = [0]*n
        parent = [-1]*n
        def find(x):
            if parent[x]==-1: return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            x = find(x)
            y = find(y)
            if x==y: return
            if rank[x]>rank[y]:
                parent[y] = x
            elif rank[x]<rank[y]:
                parent[x] = y
            else:
                parent[x] = y
                rank[y] += 1

        #sieve smallest prime factors
        spf = [i for i in range(n)]
        for i in range(2,n):
            if spf[i]!=i: continue
            for j in range(i*i, n, i):
                if spf[j]==j:
                    spf[j] = i

        def getPrimeFactors(num):
            while num>1:
                yield spf[num]
                num //= spf[num]
        
        for x in nums:
            for pf in getPrimeFactors(x):
                union(x,pf)

        for x,y in zip(nums,sorted(nums)):
            if find(x)!=find(y):
                return False
        return True