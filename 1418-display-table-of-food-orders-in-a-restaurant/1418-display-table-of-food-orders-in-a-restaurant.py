class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        A = defaultdict(Counter)
        foods = set()
        for _,t,f in orders:
            A[int(t)][f] += 1
            foods.add(f)
        tables = sorted(list(A.keys()))
        foods = sorted(list(foods))
        header = ["Table"]+foods
        res = [header]
        for t in tables:
            l = [str(t)]
            for f in foods:
                l.append(str(A[t][f]))
            res.append(l)
        return res