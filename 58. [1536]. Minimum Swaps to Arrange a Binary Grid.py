class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trailing = []
        for row in grid:
            count = 0
            for j in range(n-1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        for i in range(n):
            need = n - 1 - i
            j = i
            while j < n and trailing[j] < need:
                j += 1
            if j == n:
                return -1
            while j > i:
                trailing[j], trailing[j-1] = trailing[j-1], trailing[j]
                j -= 1
                swaps += 1
        return swaps
