class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
     
        INF = math.inf
        a, b, c = INF, INF, 0 
        for i in range(1, n+1):
            cur = costs[i-1] + min(c+1, b + 4, a + 9)
            a = b
            b = c
            c = cur
        
        return cur