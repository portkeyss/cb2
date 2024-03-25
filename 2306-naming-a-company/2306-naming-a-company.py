class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        A = defaultdict(set)
        for idea in ideas:
            A[idea[0]].add(idea[1:])
        res = 0
        alphas = list(A.keys())
        for j in range(len(alphas)):
            l1 = len(A[alphas[j]])
            for i in range(j):
                l2 = len(A[alphas[i]])
                overlap = len(A[alphas[i]]&A[alphas[j]])
                res += 2*(l1-overlap)*(l2-overlap)
        return res