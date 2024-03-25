class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        x = 0
        prefix = []
        for s in stones:
            x += s
            prefix.append(x)

        #diff[i] = max_(j>i)(prefix[j]-diff[j]) with diff[n-1] = 0
        diff = 0
        x = prefix[n-1]
        for i in range(n-2,-1,-1):
            diff = x
            x = max(x,prefix[i]-diff)
        return diff