class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        max_side = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (mat[i-1][j-1] + prefix[i-1][j] + 
                               prefix[i][j-1] - prefix[i-1][j-1])

                if i > max_side and j > max_side:
                    side = max_side + 1
                    square_sum = (prefix[i][j] - prefix[i-side][j] - 
                                 prefix[i][j-side] + prefix[i-side][j-side])
                    
                    if square_sum <= threshold:
                        max_side = side
        
        return max_side
