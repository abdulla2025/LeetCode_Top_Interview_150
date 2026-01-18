class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_prefix = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]

        col_prefix = [[0] * n for _ in range(m + 1)]
        for j in range(n):
            for i in range(m):
                col_prefix[i + 1][j] = col_prefix[i][j] + grid[i][j]
        
        def get_row_sum(r, c_start, c_end):
            return row_prefix[r][c_end + 1] - row_prefix[r][c_start]
        
        def get_col_sum(c, r_start, r_end):
            return col_prefix[r_end + 1][c] - col_prefix[r_start][c]
        
        def is_magic_square(r, c, k):
            target = get_row_sum(r, c, c + k - 1)
            for i in range(r, r + k):
                if get_row_sum(i, c, c + k - 1) != target:
                    return False

            for j in range(c, c + k):
                if get_col_sum(j, r, r + k - 1) != target:
                    return False
            
            diag1_sum = sum(grid[r + i][c + i] for i in range(k))
            if diag1_sum != target:
                return False

            diag2_sum = sum(grid[r + i][c + k - 1 - i] for i in range(k))
            if diag2_sum != target:
                return False
            
            return True

        max_k = min(m, n)
        for k in range(max_k, 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic_square(r, c, k):
                        return k
        
        return 1 