class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        x = max(damage)
        return sum(damage)+1-min(x,armor)