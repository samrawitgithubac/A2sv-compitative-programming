class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sumAccount_balance=0
        for i in range(len(accounts)):
            sumAccount_balance=max(sumAccount_balance,sum(accounts[i]))
        return sumAccount_balance

        