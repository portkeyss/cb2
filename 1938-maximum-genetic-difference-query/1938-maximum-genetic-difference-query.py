class TrieNode:
    def __init__(self):
        self.counter = 1
        self.children = dict()
        
class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        n = len(parents)
        maxVal = max(n, max(v for _,v in queries))
        m = len(bin(maxVal))-2
        
        neighbors = defaultdict(list)
        root = None
        for i,j in enumerate(parents):
            if j==-1: root = i
            else: neighbors[j].append(i)
        
        res = [None]*len(queries)
        A = defaultdict(dict)
        for i,(node,val) in enumerate(queries):
            if val not in A[node]: A[node][val]=[]
            A[node][val].append(i)
        
        def trimTree(vertex):
            keep = False
            neis = neighbors[vertex]
            for i in range(len(neis)-1,-1,-1):
                if trimTree(neis[i]): 
                    keep = True
                else:
                    neis[i], neis[-1] = neis[-1],neis[i]
                    neis.pop()
            if len(neis)==0: neighbors.pop(vertex)
            if vertex in A: keep = True
            return keep
        
        trieRoot = TrieNode()
        def dfs(vertex):
            bits = [(vertex>>i)&1 for i in range(m)[::-1]]
            trieNode = trieRoot
            for b in bits:
                if b in trieNode.children:
                    trieNode.children[b].counter += 1
                else:
                    trieNode.children[b] = TrieNode()
                trieNode = trieNode.children[b]
            for val in A[vertex]:
                valBits = [(val>>j)&1 for j in range(m)[::-1]]
                x = trieRoot
                y = 0
                for b in valBits:
                    y <<= 1
                    if 1-b in x.children:
                        y |= 1
                        x = x.children[1-b]
                    else:
                        x = x.children[b]
                for i in A[vertex][val]:
                    res[i] = y
            if vertex in neighbors:
                while neighbors[vertex]:
                    dfs(neighbors[vertex].pop())
            
            trieNode = trieRoot         
            for b in bits:
                trieNode.children[b].counter -= 1
                if trieNode.children[b].counter==0:
                    trieNode.children.pop(b)
                    break
                else:
                    trieNode = trieNode.children[b]
                
        trimTree(root)
        dfs(root)
        return res