class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        n = len(changed)
        if n==0 or n%2==1: return []
        double = Counter()
        original = []
        for num in changed:
            if num in double: 
                double[num] -= 1
                if double[num]==0:
                    double.pop(num)
            else:
                original.append(num)
                double[num*2] += 1
        return original if len(original)==n//2 else []