class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        res = 0
        counter = Counter()
        for x in nums:
            if target.startswith(x) or target.endswith(x):
                if target.startswith(x):
                    if target[len(x):] in counter:
                        res += counter[target[len(x):]]
                if target.endswith(x):
                    if target[:-len(x)] in counter:
                        res += counter[target[:-len(x)]]
                counter[x] += 1
        return res