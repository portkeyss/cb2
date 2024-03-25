class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        even = Counter()
        odd = Counter()
        even[0] = 1
        res = 0
        ct = 0
        included = False
        for j in range(1,n+1):
            if k==nums[j-1]: included = True
            ct += nums[j-1]<=k
            if j%2==0:
                if included:
                    res += even[ct-j//2]
                    res += odd[ct-j//2]
                else:
                    even[ct-j//2] += 1
            else:
                if included:
                    res += even[ct-j//2-1]
                    res += odd[ct-j//2]
                else:
                    odd[ct-j//2] += 1
        return res