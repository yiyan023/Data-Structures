class ATM:

    def __init__(self):
        self.atm = [0] * 5
        self.money_dict = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, count in enumerate(banknotesCount):
            self.atm[i] += count

    def withdraw(self, amount: int) -> List[int]:
        prev_atm = self.atm[:]
        withdraws = [0] * 5

        for i in range(4, -1, -1):
            multiplier = min(amount // self.money_dict[i], self.atm[i])
            amount -= multiplier * self.money_dict[i]
            withdraws[i] += multiplier
            self.atm[i] -= multiplier

        if amount:
            self.atm = prev_atm
            return [-1]
        
        return withdraws


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
