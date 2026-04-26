class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows,cols=len(grid),len(grid[0])
        visited=[[False]*cols for _ in range(rows)]
        directions=(-1,0,1,0,-1)
        for r in range(rows):
            for c in range(cols):
                if visited[r][c]:
                    continue
                else:
                    stack=[(r,c,-1,-1)]
                    visited[r][c]=True
                    while stack:
                        cur_r,cur_c,par_r,par_c=stack.pop()
                        for dr,dc in pairwise(directions):
                            nr,nc=cur_r+dr,cur_c+dc
                            if 0<=nr<rows and 0<=nc<cols:
                                if grid[nr][nc]==grid[r][c] and not(nr==par_r and nc==par_c):
                                    if visited[nr][nc]:
                                        return True
                                    else:
                                        visited[nr][nc]=True
                                        stack.append((nr,nc,cur_r,cur_c))
        return False
