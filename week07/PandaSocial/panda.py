from metadata import *


class Panda:

    def __init__(self, name="Ivo", email="ivo@pandamail.com", gender="male"):
        self.usr_name = name
        self.usr_email = self.check_email(email)
        self.usr_gender = gender

    def __str__(self):
        return PANDA_INFO.format(name=self.usr_name,
                                 gender=self.usr_gender,
                                 email=self.usr_email)

    def __repr__(self):
        return PANDA_INFO.format(name=self.usr_name,
                                 gender=self.usr_gender,
                                 email=self.usr_email)

    def __eq__(self, other):
        return self.usr_name == other.usr_name and \
            self.usr_email == other.usr_email and \
            self.usr_gender == other.usr_gender

    def __hash__(self):
        return hash(self.usr_name) * 241

    def serialize(self):
        return self.__dict__

    def check_email(self, email):
        if "@" in email:
            if "." in email.split("@")[1]:
                return email
        print(INVALID_EMAIL)
        raise ValueError

    def name(self):
        return self.usr_name

    def email(self):
        return self.usr_name

    def gender(self):
        return self.usr_gender

    def isMale(self):
        return self.gender() == "male"

    def isFemale(self):
        return self.gender() == "female"


class PandaALreadyThere(Exception):

    def __init__(self, mssg="PandaAlreadyAtNetwork"):
        super().__init__(mssg)


class PandasAlreadyFriends(Exception):

    def __init__(self, mssg="PandasAlreadyFriends"):
        super().__init__(mssg)


def main():
    az = Panda(email="nope")
    az.isFemale()


if __name__ == "__main__":
    main()
