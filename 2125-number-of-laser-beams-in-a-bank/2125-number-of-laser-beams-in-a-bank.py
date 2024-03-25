class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prevDevice = 0
        res = 0
        for x in bank:
            curDevice = sum(p=="1" for p in x)
            if curDevice>0:
                res += curDevice*prevDevice
                prevDevice = curDevice
        return res