class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        #get first monotonic part and last monotic part [0,l] and [r,n-1]
        l, r = 0, n-1
        while l+1 < n and arr[l]<=arr[l+1]:
            l += 1
        if l == n-1: return 0
        while r-1>=0 and arr[r-1]<=arr[r]:
            r -= 1
        if r == 0: return 0
        
        res = r #suppose only the second part starting from r is used
        j = r
        for i in range(l+1):
            while j < n and arr[j] < arr[i]:
                j += 1
            res = min(res, j-i-1)
        return res