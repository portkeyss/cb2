class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        A = sorted((sum(mat[i]),i) for i in range(len(mat)))
        return [i for _,i in A[:k]]