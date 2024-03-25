class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:-x[1])
        sz = 0
        ans = 0
        for b in boxTypes:
            if truckSize > sz+b[0]:
                ans += b[0]*b[1]
                sz += b[0]
            else:
                ans += (truckSize-sz)*b[1]
                return ans
        return ans