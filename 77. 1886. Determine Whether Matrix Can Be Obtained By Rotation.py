class Solution:
    def rotate90(self, mat):
        n = len(mat)
        rotated = []
        
        for col in range(n):
            new_row = []
            for row in range(n-1, -1, -1):
                new_row.append(mat[row][col])
            rotated.append(new_row)
        
        return rotated

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            mat = self.rotate90(mat)
        
        return False
