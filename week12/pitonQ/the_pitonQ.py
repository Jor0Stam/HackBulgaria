class PitonQ:

    def __init__(self, world, coords, size, direction):
        self.world = world
        self.coords = coords
        self.size = size
        self.direction = direction
        self.move_direction = self.get_opposite_direction(self.direction)
        self.directions = {
            "right": (0, 1),
            "left": (0, -1),
            "up": (-1, 0),
            "down": (1, 0)
        }

    def get_opposite_direction(self, direction):
        up_down = ["up", "down"]
        if direction in up_down:
            up_down.remove(direction)
            return up_down[0]
        right_left = ["right", "left"]
        right_left.remove(direction)
        return right_left[0]

    def eat(self):
        self.size += 1


class Vec2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x)

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec2D(self.x * 3, self.y * 3)

    def __div__(self, scalar):
        return Vec2D(self.x // 3, self.y // 3)

    def __neg__(self):
        return Vec2D((-1) * self.x, (-1) * self.y)


def main():
    p = PitonQ(4, (1, 1), 2, "right")
    print(p.get_opposite_direction(p.direction))


if __name__ == "__main__":
    main()
