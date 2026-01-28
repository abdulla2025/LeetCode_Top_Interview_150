class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[float('inf')] * cols for _ in range(rows)] for _ in range(k + 1)]
        dp[0][0][0] = 0
        for row in range(rows):
            for col in range(cols):
                if row:
                    dp[0][row][col] = min(dp[0][row][col], dp[0][row - 1][col] + grid[row][col])
                if col:
                    dp[0][row][col] = min(dp[0][row][col], dp[0][row][col - 1] + grid[row][col])
        value_positions = defaultdict(list)
        for row, grid_row in enumerate(grid):
            for col, value in enumerate(grid_row):
                value_positions[value].append((row, col))
        sorted_values = sorted(value_positions, reverse=True)
        for operations in range(1, k + 1):
            minimum_cost = float('inf')
            for value in sorted_values:
                positions = value_positions[value]
                for row, col in positions:
                    minimum_cost = min(minimum_cost, dp[operations - 1][row][col])
                for row, col in positions:
                    dp[operations][row][col] = minimum_cost
            for row in range(rows):
                for col in range(cols):
                    if row:
                        dp[operations][row][col] = min(dp[operations][row][col], dp[operations][row - 1][col] + grid[row][col])
                    if col:
                        dp[operations][row][col] = min(dp[operations][row][col], dp[operations][row][col - 1] + grid[row][col])
        return min(dp[operations][rows - 1][cols - 1] for operations in range(k + 1))
