class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for offset in range(k // 2):
            top = x + offset
            bottom = x + k - 1 - offset
            for col in range(y, y + k):
                grid[top][col], grid[bottom][col] = grid[bottom][col], grid[top][col]
        return grid
