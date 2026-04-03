class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        robot_data = sorted(zip(robots, distance), key=lambda x: x[0])
        walls.sort()
        
        from functools import cache
        import bisect
        
        @cache
        def dfs(idx, direction_flag):
            if idx < 0:
                return 0
            
            left_boundary = robot_data[idx][0] - robot_data[idx][1]
            if idx > 0:
                left_boundary = max(left_boundary, robot_data[idx - 1][0] + 1)
            
            left_wall_idx = bisect.bisect_left(walls, left_boundary)
            right_wall_idx = bisect.bisect_left(walls, robot_data[idx][0] + 1)
            left_move_walls = right_wall_idx - left_wall_idx
            
            ans = dfs(idx - 1, 0) + left_move_walls
            
            right_boundary = robot_data[idx][0] + robot_data[idx][1]
            if idx + 1 < n:
                if direction_flag == 0:
                    right_boundary = min(right_boundary, robot_data[idx + 1][0] - robot_data[idx + 1][1] - 1)
                else:
                    right_boundary = min(right_boundary, robot_data[idx + 1][0] - 1)
            
            left_wall_idx = bisect.bisect_left(walls, robot_data[idx][0])
            right_wall_idx = bisect.bisect_left(walls, right_boundary + 1)
            right_move_walls = right_wall_idx - left_wall_idx
            
            ans = max(ans, dfs(idx - 1, 1) + right_move_walls)
            
            return ans
        
        result = dfs(n - 1, 1)
        dfs.cache_clear()
        return result