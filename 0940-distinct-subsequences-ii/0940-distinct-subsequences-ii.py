class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10 ** 9 + 7
        dp = [0]*26
        alphabetIndices = [ord(s[idx])-97 for idx in range(len(s)-1, -1, -1)]
        for char in alphabetIndices:
            dp[char] = (1 + sum(dp)) % mod
        return sum(dp) % mod