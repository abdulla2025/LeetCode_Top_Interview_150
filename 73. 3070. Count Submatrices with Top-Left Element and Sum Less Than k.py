class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        count = 0
        
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                prefix[r][c] = (grid[r-1][c-1] + prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1])
                if prefix[r][c] <= k:
                    count += 1
        
        return count
