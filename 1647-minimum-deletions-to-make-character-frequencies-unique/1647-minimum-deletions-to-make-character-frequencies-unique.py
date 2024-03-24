class Solution:
    def minDeletions(self, s: str) -> int:
        ct = Counter(s)
        freq = sorted(ct.values(), reverse=True)
        delete = 0
        front = freq[0]+1 # any number larger than max frequency
        for n in freq:
            if n > front:
                delete += n-front        
            else:
                front = n
            if front > 0:
                front -= 1
        return delete   