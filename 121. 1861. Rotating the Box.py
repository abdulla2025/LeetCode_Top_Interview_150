class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        
        for i in range(m):
            empty_pos = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    empty_pos = j - 1
                elif boxGrid[i][j] == '#':
                    if j != empty_pos:
                        boxGrid[i][empty_pos] = '#'
                        boxGrid[i][j] = '.'
                        empty_pos -= 1
                    else:
                        empty_pos -= 1
        
        result = []
        for j in range(n):
            temp = []
            for i in range(m):
                temp.append('')
            result.append(temp)
        
        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = boxGrid[i][j]
        
        return result
