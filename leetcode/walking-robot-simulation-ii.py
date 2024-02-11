class Robot:
    def __init__(self, width: int, height: int):
        self.position = 0
        self.direction = 0
        self.directions = {0: "East", 1: "North", 2: "West", 3: "South"}
        self.width = width - 1
        self.height = height - 1
        self.distance = height + width - 2

    def step(self, num: int) -> None:
        self.position += num
        self.position %= (self.distance * 2)
        if self.position > self.distance + self.width:
            self.direction = 3
        elif self.position > self.distance:
            self.direction = 2
        elif self.position > self.width:
            self.direction = 1
        elif not self.position:
            self.direction = 3
        else:
            self.direction = 0

    def getPos(self) -> List[int]:
        if self.position > self.distance + self.width:
            return [0, self.height - (self.position - self.distance - self.width)]
        elif self.position > self.distance:
            return [self.width - (self.position - self.distance), self.height]
        elif self.position > self.width:
            return [self.width, self.position - self.width]
        else:
            return [self.position, 0]

    def getDir(self) -> str:
        return self.directions[self.direction]