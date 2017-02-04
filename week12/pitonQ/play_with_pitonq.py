from tkinter import *
from world_cells import *
from the_pitonQ import *


class MyApp:
    def __init__(self, parent, world):
        self.world = world
        self.myParent = parent
        self.myParent.focus_set()
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        self.myContainer1.bind("<Left>", self.key)
        self.text = Text(parent, height=20, width=60)
        self.text.pack()

        self.start_moving()

    def key(self, direction_button):
        self.world.move(direction_button)
        self.world.pitonq_head[1].move_direction = direction_button
        self.text.delete('1.0', END)
        self.text.insert(END, self.world)

    def start_moving(self):
        print("Test")
        self.myParent.bind('<Up>', lambda event, arg="up": self.key(arg))
        self.myParent.bind('<Down>', lambda event, arg="down": self.key(arg))
        self.myParent.bind('<Right>', lambda event, arg="right": self.key(arg))
        self.myParent.bind('<Left>', lambda event, arg="left": self.key(arg))
        self.myParent.bind('<ButtonRelease>', "esc",
                           lambda event, arg="left": self.key(arg))

        self.text.delete('1.0', END)
        self.text.insert(END, self.world)
        self.world.move(self.world.pitonq_head[1].move_direction)

        # self.myParent.after(1000, self.start_moving())


def main():
    a = World(15)
    a.add_special_cell("food", (3, 3))
    a.add_special_cell("black hole", (8, 7))
    a.add_special_cell("wall", (4, 3))
    a.add_special_cell("wall", (4, 4))
    a.add_special_cell("wall", (4, 5))
    pitonq = PitonQ(a, (1, 1), 2, "right")
    golqmiePitona = PitonQ(a, (5, 5), 2, "right")
    a.start_game(pitonq)
    a.start_game(golqmiePitona)
    root = Tk()
    t = Text(root)
    myapp = MyApp(root, a)
    root.mainloop()


if __name__ == "__main__":
    main()
