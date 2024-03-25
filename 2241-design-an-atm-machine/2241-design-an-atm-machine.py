class ATM:

    def __init__(self):
        self.A = [20,50,100,200,500]
        self.count = [0]*5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i,x in enumerate(banknotesCount):
            self.count[i]+=x
        
    def withdraw(self, amount: int) -> List[int]:
        res = [0]*5
        for k in range(4,-1,-1):
            x = min(amount//self.A[k],self.count[k])
            res[k] = x
            amount -= x*self.A[k]
        if amount>0: return [-1]
        for k in range(5):
            self.count[k] -= res[k]
        return res


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)