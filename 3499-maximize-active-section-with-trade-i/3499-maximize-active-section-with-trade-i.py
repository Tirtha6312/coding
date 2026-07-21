class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count("1")

        padded_s = "1" + s + "1"

        zero_runs = [
            len(run)
            for run in padded_s.split("1")
            if run
        ]

        if len(zero_runs) < 2:
            return ones

        best = max(
            zero_runs[i] + zero_runs[i + 1]
            for i in range(len(zero_runs) - 1)
        )

        return ones + best