class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        num_cols = len(mat[0])
        effective_shift = k % num_cols
        for row_index, row in enumerate(mat):
            if row_index % 2 == 0:
                shifted_row = row[effective_shift:] + row[:effective_shift]
            else:
                shifted_row = row[num_cols - effective_shift:] + row[:num_cols - effective_shift]
            if shifted_row != row:
                return False
        return True
