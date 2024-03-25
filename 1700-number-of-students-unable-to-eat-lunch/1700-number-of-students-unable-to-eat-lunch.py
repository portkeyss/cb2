class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = sum(students)
        zeros = len(students)-ones
        for i,sand in enumerate(sandwiches):
            if sand == 0:
                zeros -= 1
            else:
                ones -= 1
            if zeros<0 or ones<0: return len(sandwiches)-i
        return 0