class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        residue = sorted(c-r for c,r in zip(capacity,rocks))
        for i,x in enumerate(residue):
            if x==0: continue
            if additionalRocks>x:
                additionalRocks -= x
            elif additionalRocks==x:
                return i+1
            else:
                return i
        return len(capacity)