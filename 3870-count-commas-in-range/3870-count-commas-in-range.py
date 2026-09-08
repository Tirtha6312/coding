class Solution(object):
    def countCommas(self, n):
        return (n > 999) * (n - 999)