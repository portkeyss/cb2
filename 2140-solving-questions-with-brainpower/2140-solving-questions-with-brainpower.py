class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @lru_cache(None)
        def f(start):
            if start==n: return 0
            points, brainpower = questions[start][0], questions[start][1]
            nxt = min(start+brainpower+1,n)
            return max(points+f(nxt), f(start+1))
        return f(0)