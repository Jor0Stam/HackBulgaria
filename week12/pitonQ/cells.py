from emoji import emojize


class WorldCell:

    def __init__(self, x_cord, y_cord, energy=None):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.energy = energy


class Food(WorldCell):

    def __str__(self):
        return emojize(":triangular_flag_on_post:")

    def __repr__(self):
        return emojize(":triangular_flag_on_post:")


class Wall(WorldCell):

    def __str__(self):
        return emojize(":black_large_square:")

    def __repr__(self):
        return emojize(":black_large_square:")


class BlackHole(WorldCell):

    def __str__(self):
        return emojize(":white_large_square:")

    def __repr__(self):
        return emojize(":white_large_square:")


def main():
    pass


if __name__ == "__main__":
    main()
