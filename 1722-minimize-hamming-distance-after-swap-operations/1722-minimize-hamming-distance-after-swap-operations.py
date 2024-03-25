class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = [-1]*n
        rank = [0]*n
        def find(x):
            if parent[x]==-1: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            p, q = find(x), find(y)
            if p==q: return
            if rank[p]<rank[q]:
                parent[p] = q
            elif rank[p]>rank[q]:
                parent[q] = p
            else:
                parent[p] = q
                rank[q] += 1
        
        for a, b in allowedSwaps:
            union(a,b)
        
        A = defaultdict(list)
        for i in range(n):
            A[find(i)].append(i)
        
        res = 0
        for l in A.values():
            counter = Counter(source[i] for i in l)
            for j in l:
                if counter[target[j]]>0:
                    counter[target[j]] -= 1
                else:
                    res += 1
        return res        