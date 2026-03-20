class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        ans = []
        for top in range(rows - k + 1):
            row = []
            for left in range(cols - k + 1):
                values = sorted({grid[top + dr][left + dc] for dr in range(k) for dc in range(k)})
                if len(values) == 1:
                    row.append(0)
                else:
                    row.append(min(values[i+1] - values[i] for i in range(len(values) - 1)))
            ans.append(row)
        return ans
