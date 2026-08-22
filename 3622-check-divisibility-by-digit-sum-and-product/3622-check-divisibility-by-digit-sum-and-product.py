class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ = 0
        prod = 1
        for i in str(abs(n)):
            d  = int(i)
            summ += d
            prod *= d
        if n % (summ+prod) == 0:
            return True
        else:
            return False