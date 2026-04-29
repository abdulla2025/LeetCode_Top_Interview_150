class Solution:
    def maximumScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # col_prefix[col][row] = sum of grid[0..row-1][col]
        col_prefix = [[0] * (n + 1) for _ in range(n)]
        for col in range(n):
            for row in range(n):
                col_prefix[col][row + 1] = col_prefix[col][row] + grid[row][col]

        # dp_pick_prev[height] = max score up to previous column,
        # where column 'col-1' had black cells from top to height-1
        dp_pick_prev = [0] * (n + 1)
        # dp_skip_prev[height] = similar but the column before previous
        # decided the black region for 'col-1' (used when current is taller)
        dp_skip_prev = [0] * (n + 1)

        for col in range(1, n):
            dp_pick_curr = [0] * (n + 1)
            dp_skip_curr = [0] * (n + 1)

            for curr_height in range(n + 1):
                for prev_height in range(n + 1):
                    if curr_height > prev_height:
                        # Current column's black region is deeper.
                        # We earn the cells in column 'col-1' from row prev_height to curr_height-1.
                        score = col_prefix[col - 1][curr_height] - col_prefix[col - 1][prev_height]
                        dp_pick_curr[curr_height] = max(dp_pick_curr[curr_height], dp_skip_prev[prev_height] + score)
                        dp_skip_curr[curr_height] = max(dp_skip_curr[curr_height], dp_skip_prev[prev_height] + score)
                    else:
                        # Previous column's black region is deeper.
                        # We earn cells in current column from row curr_height to prev_height-1.
                        score = col_prefix[col][prev_height] - col_prefix[col][curr_height]
                        dp_pick_curr[curr_height] = max(dp_pick_curr[curr_height], dp_pick_prev[prev_height] + score)
                        dp_skip_curr[curr_height] = max(dp_skip_curr[curr_height], dp_pick_prev[prev_height])

            dp_pick_prev = dp_pick_curr
            dp_skip_prev = dp_skip_curr

        return max(dp_pick_prev)
