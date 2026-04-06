class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal_position = 0
        vertical_position = 0

        for move in moves:
            if move == "R":
                horizontal_position += 1
            elif move == "L":
                horizontal_position -= 1
            elif move == "U":
                vertical_position += 1
            else:
                vertical_position -= 1

        return horizontal_position == 0 and vertical_position == 0
