class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0]
        for a in arr:
            prefix.append(a+prefix[-1])
        res = 0
        for i in range(n):
            for j in range(i+1,n+1,2):
                res += prefix[j] - prefix[i]
        return res