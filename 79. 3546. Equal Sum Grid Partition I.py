class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(sum(row) for row in grid)
        if total % 2 != 0:
            return False
        half = total // 2
        top_sum = 0
        for i in range(len(grid) - 1):
            top_sum += sum(grid[i])
            if top_sum == half:
                return True
        left_sum = 0
        for j in range(len(grid[0]) - 1):
            for i in range(len(grid)):
                left_sum += grid[i][j]
            if left_sum == half:
                return True
        return False
