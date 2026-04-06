class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obstacle_set = set(map(tuple, obstacles))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0
        
        robot_x = 0
        robot_y = 0
        max_distance_squared = 0
        
        for command in commands:
            if command == -2:
                current_direction = (current_direction - 1) % 4
            elif command == -1:
                current_direction = (current_direction + 1) % 4
            else:
                step_x, step_y = directions[current_direction]
                for _ in range(command):
                    next_x = robot_x + step_x
                    next_y = robot_y + step_y
                    if (next_x, next_y) in obstacle_set:
                        break
                    robot_x = next_x
                    robot_y = next_y
                    max_distance_squared = max(max_distance_squared, robot_x ** 2 + robot_y ** 2)
        
        return max_distance_squared
