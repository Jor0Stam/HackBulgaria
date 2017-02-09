from models import BaseModel
from fields import PKColumn, IntegerColumn, TextColumn


class User(BaseModel):
    __tablename__ = 'user'

    id = PKColumn()
    name = TextColumn(max_length=100)
    age = IntegerColumn()


class Student(User):
    __tablename__ = "student"
    email = TextColumn()
    shirt_size = IntegerColumn()


def main():
    # pass
    # Creating all tables from BaseModel class
    # BaseModel.create_all_tables()

    # Create record in table
    # User.create_obj(name="Rosi", age=22)

    # Return dict with object
    print(User.filter(name='Rosi'))


if __name__ == "__main__":
    main()
