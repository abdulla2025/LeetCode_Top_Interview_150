class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        diag1 = [[0] * (cols + 2) for _ in range(rows + 1)]
        diag2 = [[0] * (cols + 2) for _ in range(rows + 1)]
        
        for i, row in enumerate(grid, 1):
            for j, val in enumerate(row, 1):
                diag1[i][j] = diag1[i - 1][j - 1] + val
                diag2[i][j] = diag2[i - 1][j + 1] + val
                
        sums = SortedSet()
        for i, row in enumerate(grid, 1):
            for j, val in enumerate(row, 1):
                size = min(i - 1, rows - i, j - 1, cols - j)
                sums.add(val)
                for k in range(1, size + 1):
                    top = diag1[i + k][j] - diag1[i][j - k]
                    right = diag1[i][j + k] - diag1[i - k][j]
                    bottom = diag2[i][j - k] - diag2[i - k][j]
                    left = diag2[i + k][j] - diag2[i][j + k]
                    total = top + right + bottom + left - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1]
                    sums.add(total)
                while len(sums) > 3:
                    sums.remove(sums[0])
        return list(sums)[::-1]
