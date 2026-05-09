class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2
        result = [[0] * n for _ in range(m)]
        
        for layer in range(layers):
            top, bottom = layer, m - 1 - layer
            left, right = layer, n - 1 - layer
            
            elements = []
            for j in range(left, right + 1):
                elements.append(grid[top][j])
            for i in range(top + 1, bottom + 1):
                elements.append(grid[i][right])
            for j in range(right - 1, left - 1, -1):
                elements.append(grid[bottom][j])
            for i in range(bottom - 1, top, -1):
                elements.append(grid[i][left])
            
            rot = k % len(elements)
            elements = elements[rot:] + elements[:rot]
            
            idx = 0
            for j in range(left, right + 1):
                result[top][j] = elements[idx]; idx += 1
            for i in range(top + 1, bottom + 1):
                result[i][right] = elements[idx]; idx += 1
            for j in range(right - 1, left - 1, -1):
                result[bottom][j] = elements[idx]; idx += 1
            for i in range(bottom - 1, top, -1):
                result[i][left] = elements[idx]; idx += 1
        
        return result
