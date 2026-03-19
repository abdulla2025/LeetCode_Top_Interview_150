class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        prefix_diff = []
        for row in range(rows):
            prefix_diff.append([0] * cols)
        prefix_x = []
        for row in range(rows):
            prefix_x.append([0] * cols)
      
        result = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 'X':
                    cell_diff = 1
                elif grid[row][col] == 'Y':
                    cell_diff = -1
                else:
                    cell_diff = 0

                if grid[row][col] == 'X':
                    cell_x = 1
                else:
                    cell_x = 0
                
                if row > 0:
                    top_diff = prefix_diff[row - 1][col]
                else:
                    top_diff = 0
                    
                if col > 0:
                    left_diff = prefix_diff[row][col - 1]
                else:
                    left_diff = 0
                    
                if row > 0 and col > 0:
                    diag_diff = prefix_diff[row - 1][col - 1]
                else:
                    diag_diff = 0
                
                prefix_diff[row][col] = cell_diff + top_diff + left_diff - diag_diff
                
                if row > 0:
                    top_x = prefix_x[row - 1][col]
                else:
                    top_x = 0
                    
                if col > 0:
                    left_x = prefix_x[row][col - 1]
                else:
                    left_x = 0
                    
                if row > 0 and col > 0:
                    diag_x = prefix_x[row - 1][col - 1]
                else:
                    diag_x = 0
                
                prefix_x[row][col] = cell_x + top_x + left_x - diag_x
                
                if prefix_diff[row][col] == 0 and prefix_x[row][col] > 0:
                    result += 1
        
        return result
