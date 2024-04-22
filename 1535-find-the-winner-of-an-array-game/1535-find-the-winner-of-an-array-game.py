class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        mx = max(arr)
        cur = -inf
        count = 0
        for x in arr:
            if x==mx: return mx
            if x<cur:
                count += 1   
            else:
                count = 0 if cur==-inf else 1
                cur = x
            if count==k: return cur