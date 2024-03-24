class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod = Counter()
        for a in arr:
            if a%k==0:
                if 0 in mod:
                    mod[0] -= 1
                    if mod[0]==0:
                        mod.pop(0)
                else:
                    mod[0] += 1
            else:
                if k-a%k in mod:
                    mod[k-a%k] -= 1
                    if mod[k-a%k]==0:
                        mod.pop(k-a%k)
                else:
                    mod[a%k] += 1
        return len(mod)==0    