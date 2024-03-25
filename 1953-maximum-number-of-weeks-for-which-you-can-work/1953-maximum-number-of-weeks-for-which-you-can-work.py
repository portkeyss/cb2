class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones.sort(reverse=True)
        tot = sum(milestones)
        if milestones[0]<=tot-milestones[0]+1: return tot
        else:
            return 2*(tot-milestones[0])+1