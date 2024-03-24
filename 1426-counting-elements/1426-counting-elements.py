class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        res = 0
        for a in arr:
            if a + 1 in s:
                res += 1
        return res