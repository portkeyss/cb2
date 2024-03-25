class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        m, n = len(nums1), len(nums2)
        def f(arr):
            A = [[],[]]
            for a in arr:
                if a<0:
                    A[0].append(-a)
                elif a>0:
                    A[1].append(a)
            A[0] = A[0][::-1]
            return A
        P, Q = f(nums1), f(nums2)
        neg = len(P[0])*len(Q[1])+len(P[1])*len(Q[0])
        pos = len(P[0])*len(Q[0])+len(P[1])*len(Q[1])
        if k<=neg:
            l,r = 1,10**10
            while l<r:
                mid = (l+r+1)//2
                ct = 0
                for x in P[0]:
                    i = bisect.bisect_left(Q[1], ceil(mid/x))
                    ct += len(Q[1])-i
                for x in P[1]:
                    i = bisect.bisect_left(Q[0], ceil(mid/x))
                    ct += len(Q[0])-i
                if ct<k: r=mid-1
                else: l=mid
            return -l
        elif k<=m*n-pos:
            return 0
        else:
            k -= m*n-pos
            l,r = 1,10**10
            while l<r:
                mid = (l+r)//2
                ct = 0
                for x in P[0]:
                    i = bisect.bisect_right(Q[0], mid//x)
                    ct += i
                for x in P[1]:
                    i = bisect.bisect_right(Q[1], mid//x)
                    ct += i
                if ct<k: l=mid+1
                else: r=mid
            return l