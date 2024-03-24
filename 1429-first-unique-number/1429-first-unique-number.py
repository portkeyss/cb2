class FirstUnique:

    def __init__(self, nums: List[int]):
        self.blacklist = set()
        self.uniqueNums = {}
        for num in nums:
            if num in self.blacklist:
                continue      
            elif num in self.uniqueNums:
                self.uniqueNums.pop(num)
                self.blacklist.add(num)
            else:
                self.uniqueNums[num] = 1
                    
    def showFirstUnique(self) -> int:
        if not self.uniqueNums:
            return -1
        for num in self.uniqueNums:
            return num
        
    def add(self, value: int) -> None:
        if value in self.blacklist:
            return      
        elif value in self.uniqueNums:
            self.uniqueNums.pop(value)
            self.blacklist.add(value)
        else:
            self.uniqueNums[value] = 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)