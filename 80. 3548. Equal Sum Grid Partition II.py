class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def can_partition_horizontally(matrix: List[List[int]]) -> bool:
            rows, cols = len(matrix), len(matrix[0])
            top_sum = 0
            bottom_sum = 0
            top_counts = defaultdict(int)
            bottom_counts = defaultdict(int)
            
            for row in matrix:
                for value in row:
                    bottom_sum += value
                    bottom_counts[value] += 1
            
            for split_row in range(rows - 1):
                for value in matrix[split_row]:
                    top_sum += value
                    bottom_sum -= value
                    top_counts[value] += 1
                    bottom_counts[value] -= 1
                
                if top_sum == bottom_sum:
                    return True
                
                if top_sum < bottom_sum:
                    difference = bottom_sum - top_sum
                    if bottom_counts[difference]:
                        if (
                            (rows - split_row - 1 > 1 and cols > 1)
                            or (
                                split_row == rows - 2
                                and (matrix[split_row + 1][0] == difference or matrix[split_row + 1][-1] == difference)
                            )
                            or (cols == 1 and (matrix[split_row + 1][0] == difference or matrix[-1][0] == difference))
                        ):
                            return True
                else:
                    difference = top_sum - bottom_sum
                    if top_counts[difference]:
                        if (
                            (split_row + 1 > 1 and cols > 1)
                            or (split_row == 0 and (matrix[0][0] == difference or matrix[0][-1] == difference))
                            or (cols == 1 and (matrix[0][0] == difference or matrix[split_row][0] == difference))
                        ):
                            return True
            
            return False
        
        return can_partition_horizontally(grid) or can_partition_horizontally(list(zip(*grid)))
