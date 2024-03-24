class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        bf = [" "]*len(s)
        for i,j in enumerate(indices):
            bf[j] = s[i]
        return "".join(bf)