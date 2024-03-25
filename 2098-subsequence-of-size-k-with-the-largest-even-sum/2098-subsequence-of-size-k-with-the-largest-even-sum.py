class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        even = [p for p in nums if p%2==0]
        odd = [p for p in nums if p%2==1]
        even.sort(reverse=True)
        odd.sort(reverse=True)
        m, n = len(even), len(odd)
        if k%2==1 and m==0: return -1
        i = 0 if k%2==0 else 1
        j = 0
        sm = 0 if k%2==0 else even[0]
        if k%2==1: k-=1
        while k>0 and i+1<m and j+1<n:
            if even[i]+even[i+1]<=odd[j]+odd[j+1]:
                sm += odd[j]+odd[j+1]
                j += 2
                k -= 2
            else:
                sm += even[i]+even[i+1]
                i += 2
                k -= 2
        while k>0 and i+1<m:
            sm += even[i]+even[i+1]
            i += 2
            k -= 2
        while k>0 and j+1<n:
            sm += odd[j]+odd[j+1]
            j += 2
            k -= 2
        return sm if k==0 else -1