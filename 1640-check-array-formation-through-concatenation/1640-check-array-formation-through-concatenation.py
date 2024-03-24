class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        starts = {l[0]:i for i,l in enumerate(pieces)}
        i = 0
        m = len(arr)
        while i<m:
            if arr[i] in starts:
                j = starts[arr[i]]
                k = 0
                n = len(pieces[j])
                while i<m and k<n and arr[i]==pieces[j][k]:
                    i += 1
                    k += 1
                if k<n: return False
            else:
                return False
        return True