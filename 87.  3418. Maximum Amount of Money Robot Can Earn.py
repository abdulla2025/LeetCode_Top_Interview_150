class Solution:
    def maximumAmount(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[[float('-inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        dp[0][0][0] = grid[0][0]
        dp[0][0][1] = 0
        
        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if dp[i][j][k] == float('-inf'):
                        continue
                    
                    if j + 1 < n:
                        dp[i][j+1][k] = max(dp[i][j+1][k], dp[i][j][k] + grid[i][j+1])
                        
                        if k < 2:
                            dp[i][j+1][k+1] = max(dp[i][j+1][k+1], dp[i][j][k])
                    
                    if i + 1 < m:
                        dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k] + grid[i+1][j])
                        
                        if k < 2:
                            dp[i+1][j][k+1] = max(dp[i+1][j][k+1], dp[i][j][k])
        
        return max(dp[m-1][n-1][0], dp[m-1][n-1][1], dp[m-1][n-1][2])
