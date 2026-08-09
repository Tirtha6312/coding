class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)

        dp = [[[-1]* (2*N) for _ in range(2)] for _ in range(N)]
        
        def solve(index, turn, m):
            if index == N:
                return 0

            if dp[index][turn][m] != -1:
                return dp[index][turn][m]    

            res = float("inf") if turn else float("-inf")   
            
            sm = 0
            for i in range(2*m):
                if index+i < N:
                    sm += piles[index+i]
                    if not turn:
                        res = max(res, sm+solve(index+i+1, turn^1, max(m, i+1)))
                    else:
                        res = min(res, solve(index+i+1, turn^1, max(m, i+1)))
            dp[index][turn][m] = res
            return res
        return solve(0, 0, 1)                  
        