class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)
        if s1 == s2: return 0
        if s1 > s2: return self.minOperations(nums2, nums1)
        cnt = Counter([6-i for i in nums1]+[i-1 for i in nums2])
        step = 0
        d = s2-s1
        for i in range(5,0,-1):
            while d>0 and cnt[i]:
                d -= i
                step += 1
                cnt[i] -= 1
            if d<=0: return step
        return -1