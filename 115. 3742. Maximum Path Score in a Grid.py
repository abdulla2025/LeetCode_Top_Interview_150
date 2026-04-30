class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF_NEG = -10**9
        prev = [[INF_NEG] * (k + 1) for _ in range(n)]
        
        for i in range(m):
            cur = [[INF_NEG] * (k + 1) for _ in range(n)]
            for j in range(n):
                val = grid[i][j]
                if val == 0:
                    s_add, c_add = 0, 0
                elif val == 1:
                    s_add, c_add = 1, 1
                else:
                    s_add, c_add = 2, 1
                
                if i == 0 and j == 0:
                    if c_add <= k:
                        cur[j][c_add] = s_add
                    continue
                
                if i > 0:
                    for c in range(k + 1):
                        if prev[j][c] != INF_NEG:
                            nc = c + c_add
                            if nc <= k:
                                cur[j][nc] = max(cur[j][nc], prev[j][c] + s_add)
                if j > 0:
                    for c in range(k + 1):
                        if cur[j-1][c] != INF_NEG:
                            nc = c + c_add
                            if nc <= k:
                                cur[j][nc] = max(cur[j][nc], cur[j-1][c] + s_add)
            prev = cur
        
        best = max(prev[n-1])
        return best if best != INF_NEG else -1
