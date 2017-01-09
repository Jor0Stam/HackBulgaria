class Projection:

    def init(self, id, movie_id, type, date, time, max_row, max_col, taken_s):
        self.id = id
        self.movie_id = movie_id
        self.type = type
        self.date = date
        self.time = time
        self.max_row = max_row
        self.max_col = max_col
        self.taken_s = taken_s  # seat <=> (row, column)

    def take_seat(self, seat):
        if seat in self.taken_s:
            return False
        self.taken_s.append(seat)


def main():
    pass


if __name__ == "__main__":
    main()
