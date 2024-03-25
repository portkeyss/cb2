class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = 10**9+7
        counter = Counter(deliciousness)
        a = b = 0
        for k in counter:
            for p in range(22):
                x = (1<<p)-k
                if x==k: a = (a+counter[k]*(counter[k]-1)//2)%mod
                elif x in counter:
                    b = (b+counter[k]*counter[x])%mod
        return (a+b//2)%mod