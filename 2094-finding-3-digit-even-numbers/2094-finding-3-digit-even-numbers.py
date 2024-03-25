class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        counter = Counter(digits)
        res = []
        for k in range(100,1000):
            if k%2==0:
                x = Counter(int(c) for c in str(k))
                if all(ct<=counter[d] for d,ct in x.items()):
                    res.append(k)    
        return res