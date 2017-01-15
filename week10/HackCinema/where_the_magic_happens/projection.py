class Projection:

    def __init__(self, m_id, m_type, m_date, m_time):
        self.m_id = m_id
        self.m_type = m_type
        self.m_date = m_date
        self.m_time = m_time
        self.taken_seats = []

    def take_seats(self, seats):
        if seats in self.taken_seats:
            return False
        self.taken_seats.extend(seats)
        return True

    def get_seats(self):
        return len(self.taken_seats)


def main():
    pass


if __name__ == "__main__":
    main()
