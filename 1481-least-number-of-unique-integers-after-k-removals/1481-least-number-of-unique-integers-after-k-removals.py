class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:  
        ctr = Counter(arr)
        A = list(ctr.values())
        if k == 0:
            return len(A)
        A.sort()
        for i in range(len(A)):
            if k < A[i]:
                return len(A)-i
            if k == A[i]:
                return len(A)-1-i
            k -= A[i]