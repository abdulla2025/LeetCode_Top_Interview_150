class Robot:
    def __init__(self, width: int, height: int):
        self.max_x = width - 1
        self.max_y = height - 1
        self.perimeter = 2 * self.max_x + 2 * self.max_y
        self.position_index = 0
        self.has_moved = False

    def step(self, num: int) -> None:
        self.has_moved = True
        self.position_index = (self.position_index + num) % self.perimeter

    def getPos(self) -> List[int]:
        index = self.position_index
        max_x, max_y = self.max_x, self.max_y

        if 0 <= index <= max_x:
            return [index, 0]
        if max_x < index <= max_x + max_y:
            return [max_x, index - max_x]
        if max_x + max_y < index <= 2 * max_x + max_y:
            return [max_x - (index - (max_x + max_y)), max_y]
        return [0, max_y - (index - (2 * max_x + max_y))]

    def getDir(self) -> str:
        index = self.position_index
        max_x, max_y = self.max_x, self.max_y

        if not self.has_moved:
            return "East"
        if 1 <= index <= max_x:
            return "East"
        if max_x < index <= max_x + max_y:
            return "North"
        if max_x + max_y < index <= 2 * max_x + max_y:
            return "West"
        return "South"
