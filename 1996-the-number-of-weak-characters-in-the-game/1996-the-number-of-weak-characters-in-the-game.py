class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        mxd = 0
        res = 0
        for _,d in properties:
            if d<mxd:
                res += 1
            mxd = max(mxd,d)
        return res