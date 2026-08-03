class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        cache = [0] * (len(stoneValue) + 4)
        cache[0] = stoneValue[0]
        length = len(stoneValue)
        stoneValue.extend([0, 0, 0])
        for i in range(length - 1, -1, -1):
            cache[i] = max(stoneValue[i] - cache[i + 1], stoneValue[i] + stoneValue[i+1] - cache[i + 2], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - cache[i+ 3])
        if cache[0] > 0:
            return "Alice"
        elif cache[0] < 0:
            return "Bob"
        return "Tie"