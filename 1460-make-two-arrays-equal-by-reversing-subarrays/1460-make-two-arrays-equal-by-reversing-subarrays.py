class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter1 = Counter(target)
        counter2 = Counter(arr)
        return counter1==counter2