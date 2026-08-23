class Solution:
    def sumGame(self, num: str) -> bool:
        ORD0 = ord("0")
        nhalf = len(num) // 2
        up, down = num[:nhalf], num[nhalf:]
        balance_up = sum([ord(c) - ORD0 for c in up if c != "?"])
        balance_down = sum([ord(c) - ORD0 for c in down if c != "?"])
        balance = balance_up - balance_down
        wild_up = up.count("?")
        wild_down = down.count("?")
        wild_balance = wild_up - wild_down
        if wild_balance & 1:
            return True
        return balance != -9 * (wild_balance // 2)