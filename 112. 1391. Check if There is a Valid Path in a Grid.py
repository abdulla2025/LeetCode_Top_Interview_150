from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        parent = list(range(rows * cols))

        def find(cell_index):
            if parent[cell_index] != cell_index:
                parent[cell_index] = find(parent[cell_index])
            return parent[cell_index]

        def union_left(row, col):
            if col > 0 and grid[row][col - 1] in (1, 4, 6):
                current_cell = row * cols + col
                left_cell = row * cols + (col - 1)
                parent[find(current_cell)] = find(left_cell)

        def union_right(row, col):
            if col < cols - 1 and grid[row][col + 1] in (1, 3, 5):
                current_cell = row * cols + col
                right_cell = row * cols + (col + 1)
                parent[find(current_cell)] = find(right_cell)

        def union_up(row, col):
            if row > 0 and grid[row - 1][col] in (2, 3, 4):
                current_cell = row * cols + col
                up_cell = (row - 1) * cols + col
                parent[find(current_cell)] = find(up_cell)

        def union_down(row, col):
            if row < rows - 1 and grid[row + 1][col] in (2, 5, 6):
                current_cell = row * cols + col
                down_cell = (row + 1) * cols + col
                parent[find(current_cell)] = find(down_cell)
        for row in range(rows):
            for col in range(cols):
                street_type = grid[row][col]
                
                if street_type == 1:  # Left-Right connection
                    union_left(row, col)
                    union_right(row, col)
                elif street_type == 2:  # Up-Down connection
                    union_up(row, col)
                    union_down(row, col)
                elif street_type == 3:  # Left-Down connection
                    union_left(row, col)
                    union_down(row, col)
                elif street_type == 4:  # Right-Down connection
                    union_right(row, col)
                    union_down(row, col)
                elif street_type == 5:  # Left-Up connection
                    union_left(row, col)
                    union_up(row, col)
                else:  # street_type == 6: Right-Up connection
                    union_right(row, col)
                    union_up(row, col)
        start_cell = 0
        end_cell = rows * cols - 1
        return find(start_cell) == find(end_cell)
