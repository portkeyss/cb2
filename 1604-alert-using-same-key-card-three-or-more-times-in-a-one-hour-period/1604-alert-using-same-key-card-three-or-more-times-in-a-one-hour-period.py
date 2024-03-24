class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        A = defaultdict(list)
        for n,t in zip(keyName,keyTime):
            A[n].append(t)
        for v in A.values():
            v.sort()
        def f(l):
            prepre = -100
            pre = -100
            for t in l:
                h,m = map(int, t.split(":"))
                t = h*60+m
                if prepre >= t-60:
                    return True
                prepre = pre
                pre = t
            return False
        return sorted([n for n,l in A.items() if f(l)])