class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def compare(num):
            p = num
            bitCount = 0
            while p:
                bitCount += (p&1!=0)
                p >>= 1
            return (bitCount,num)
        
        return sorted(arr, key=compare)