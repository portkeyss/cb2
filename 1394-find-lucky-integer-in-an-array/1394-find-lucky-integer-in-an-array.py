class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        res = -1
        for x in arr:
            if counter[x]==x:
                res = max(res, x)
        return res     