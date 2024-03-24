class Solution:
    def longestAwesome(self, s: str) -> int:
        s = [int(c) for c in s]
        mask = 0
        mask2idx = {0:-1}
        res = 0
        for i,x in enumerate(s):
            mask ^= (1<<x)
            if mask in mask2idx: res = max(res, i-mask2idx[mask])
            for k in range(10):
                mask1 = mask^(1<<k)
                if mask1 in mask2idx: res = max(res, i-mask2idx[mask1])
            if mask not in mask2idx: mask2idx[mask] = i
        return res