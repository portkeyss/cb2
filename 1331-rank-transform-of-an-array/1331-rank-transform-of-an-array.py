class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        A = sorted(set(arr))
        return [bisect.bisect(A,a) for a in arr]