class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            sorted_heights = sorted(heights, reverse=True)
            for k, h in enumerate(sorted_heights):
                if h == 0:
                    break
                area = (k + 1) * h
                if area > max_area:
                    max_area = area
        return max_area
