class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        edges = defaultdict(set)
        for r,ing in zip(recipes, ingredients):
            for a in ing:
                edges[r].add(a)
        A = dict()
        for s in supplies:
            A[s] = True
        buffer = set()
        
        def dfs(x):#this function also detects loops
            if x in A:
                return A[x]
            if x not in edges:
                A[x] = False
                return A[x]
            if x in buffer:
                A[x] = False
                return A[x]
            buffer.add(x)
            for y in edges[x]:
                if not dfs(y):
                    A[x] = False
                    break
            if x not in A:
                A[x] = True
            buffer.remove(x) #this is logically not needed, but is retained in observance to programming paradigms that minimize errors
            return A[x]
        
        res = []
        for r in recipes:
            if dfs(r): 
                res.append(r)
        return res