class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        sm = 0
        even = 1
        odd = 0
        res = 0
        for a in arr:
            sm += a
            if sm%2==0:
                res += odd
                even += 1
            else:
                res += even
                odd += 1
        return res%(10**9+7)