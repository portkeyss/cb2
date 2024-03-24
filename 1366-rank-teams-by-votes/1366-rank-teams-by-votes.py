class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        scores = defaultdict(lambda:[0]*len(votes[0]))
        for v in votes:
            for i,a in enumerate(v):
                scores[a][i] -= 1 # use negative score only to make sorting afterwards more covenience
        p = []
        for c,l in scores.items():
            p.append(l+[c])
        p.sort()
        return "".join(l[-1] for l in p)