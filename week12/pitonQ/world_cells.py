from cells import *
from the_pitonQ import PitonQ
# from time import sleep
from random import randrange
# from emoji import emojize


class World:

    def __init__(self, max_size):
        self.max_size = max_size
        self.pitonq_head = []  # [0] = head's coords, [1] = reference to pitonq
        self.pitonq_body = []
        self.special_cells = {"food": [],
                              "black hole": [],
                              "wall": []}

    def __str__(self):
        return self.return_world()

    def __repr__(self):
        return self.return_world()

    def add_special_cell(self, type, new_cell):
        if self.check_content(new_cell):
            self.special_cells[type].append((new_cell[0], new_cell[1]))

    def check_content(self, content):
        try:
            WorldCell(content[0], content[1])
            return True
        except ContentNotWorldObj as e:
            print(e)

    def is_empty(self, coords):
        return coords not in (self.pitonq_body + self.pitonq_head +
                              self.special_cells["food"] +
                              self.special_cells["black hole"] +
                              self.special_cells["wall"])

    def return_world(self):
        result = ""
        for row in range(self.max_size):
            for col in range(self.max_size):
                if (row, col) in self.special_cells["food"]:
                    result += " " + "F" + " "  # + str(Food(row, col)) + " "
                elif (row, col) in self.special_cells["wall"]:
                    result += " " + "W" + " "  # + str(Wall(col, row)) + " "
                elif (row, col) in self.pitonq_body:
                    result += " " + "B" + " "  # + emojize(":large_blue_circle:") + " "
                elif (row, col) in self.pitonq_head:
                    result += " " + "H" + " "  # + emojize(":snake:") + " "
                else:
                    result += " " + "*" + " "  # + emojize(":white_large_square:") + " "
            result += "\n"
        return result

    def start_game(self, pitonq):
        if not self.pitonq_fit_the_field(pitonq):
            raise PitonqDontFit
        self.pitonq_head.append(pitonq.coords)
        self.pitonq_head.append(pitonq)
        self.pitonq_body.append((
            pitonq.coords[0] + pitonq.directions[pitonq.direction][0],
            pitonq.coords[1] + pitonq.directions[pitonq.direction][1]))
        for el in range(1, pitonq.size):
            self.pitonq_body.append((
                self.pitonq_body[el - 1][0] +
                pitonq.directions[pitonq.direction][0],
                self.pitonq_body[el - 1][1] +
                pitonq.directions[pitonq.direction][1]))
        pitonq.move_direction = pitonq.get_opposite_direction(pitonq.direction)
        # while True:
        #     print(pitonq.move_direction)
        #     self.move(pitonq.move_direction)
        #     yield sleep(0.5)

    def pitonq_fit_the_field(self, pitonq):
        return (pitonq.direction == "up" and
                pitonq.size <= pitonq.coords[1]) or \
            (pitonq.direction == "down" and
             pitonq.size in range(self.max_size - pitonq.coords[1] - 1)) or \
            (pitonq.direction == "left" and
                pitonq.size <= pitonq.coords[0]) or \
            (pitonq.direction == "right" and
             pitonq.size in range(self.max_size - pitonq.coords[0] - 1))

    def new_pos(self, direction):
        return (
            self.pitonq_head[0][0] +
            self.pitonq_head[1].directions[direction][0],
            self.pitonq_head[0][1] +
            self.pitonq_head[1].directions[direction][1])

    def move(self, direction):
        if self.wrong_direction(direction):
            raise PythonDeath("Lol you went out of the table!")
        elif self.directly_wall(direction):
            raise PythonDeath("You've kissed a wall!")
        elif self.directly_wall(direction):
            raise PythonDeath("The void grabbed you!")
        elif self.self_eat(direction):
            raise PythonDeath("Are you tryin' ouroboros?")
        elif self.food_ahead(direction):
            self.pitonq_head[1].eat()
            self.special_cells["food"] = self.gimmie_food()
            self.pitonq_body.append("To Delete")
        old = self.pitonq_body[:-1]
        self.pitonq_body = []
        self.pitonq_body.append(self.pitonq_head[0])
        self.pitonq_body.extend(old)
        self.pitonq_head[0] = self.new_pos(direction)
        print(self.pitonq_body)

    def wrong_direction(self, direction):
        return \
            self.pitonq_head[0][0] +\
            self.pitonq_head[1].directions[direction][0] \
            not in range(self.max_size) or \
            self.pitonq_head[0][1] + \
            self.pitonq_head[1].directions[direction][1] \
            not in range(self.max_size)

    def directly_wall(self, direction):
        return self.new_pos(direction) in self.special_cells["wall"]

    def self_eat(self, direction):
        return self.new_pos(direction) in self.pitonq_body

    def food_ahead(self, direction):
        return self.new_pos(direction) in self.special_cells["food"]

    def black_holed(self, direction):
        return self.new_pos(direction) in self.special_cells["black hole"]

    def gimmie_food(self):
        x = randrange(self.max_size)
        y = randrange(self.max_size)
        while not self.is_empty((x, y)):
            x = randrange(self.max_size)
            y = randrange(self.max_size)
        return [(x, y)]


class ContentNotWorldObj(Exception):

    def __init__(self, mssg="Content not world object!"):
        super().__init__(mssg)


class PythonDeath(Exception):

    def __init__(self, reason):
        super().__init__("PitonQ died cos' of " + reason)


class PitonqDontFit(Exception):

    def __init__(self, mssg="Your Piton is too big for this grid!"):
        super().__init__(mssg)


def main():
    a = World(15)
    a.add_special_cell("food", (3, 3))
    a.add_special_cell("black hole", (8, 7))
    a.add_special_cell("wall", (4, 3))
    a.add_special_cell("wall", (4, 4))
    a.add_special_cell("wall", (4, 5))
    print(a)
    pitonq = PitonQ(a, (1, 1), 2, "right")
    a.start_game(pitonq)
    print(a)
    a.move("down")
    print(a)
    a.move("down")
    print(a)
    a.move("down")
    print(a)
    a.move("right")
    # a.move("right")
    print(a)
    # a.detect_arrow_pressing()


if __name__ == "__main__":
    main()
