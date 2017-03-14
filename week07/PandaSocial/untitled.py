# Panda
from json import dump  # , load

PANDA_INFO = "{name} who is {gender} with email {email}"
INVALID_EMAIL = "The email you entered is invalid"


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
        return self.usr_email

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


class PandaSocialNetwork:

    def __init__(self):
        self.pandas = []
        self.connectios = {}
        self.size = 0

    def add_panda(self, panda):
        if panda in self.pandas:
            raise PandaALreadyThere
        self.pandas.append(panda)
        self.connectios[panda] = []
        self.size += 1

    def has_panda(self, panda):
        if panda in self.pandas:
            return True
        return False

    def make_friends(self, panda1, panda2):
        self.check_in(panda1, panda2)
        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriends
        self.befriend(panda1, panda2)

    def check_in(self, panda1, panda2):
        if panda1 not in self.pandas:
            self.add_panda(panda1)
        if panda2 not in self.pandas:
            self.add_panda(panda2)

    def befriend(self, pand1, pand2):
        self.connectios[pand1] += [pand2]
        self.connectios[pand2] += [pand1]

    def are_friends(self, panda1, panda2):
        return panda2 in self.connectios[panda1]

    def friends_of(self, panda1):
        if not self.is_in(panda1):
            return False
        return self.connectios[panda1]

    def connection_level(self, panda1, panda2, cnt=1):
        # import ipdb; ipdb.set_trace()
        if not self.is_in(panda1) or not self.is_in(panda2):
            return False
        er404 = False
        to_visit = self.connectios[panda1]
        while not er404:
            if panda2 in to_visit:
                return cnt
            cnt += 1
            new_visits = []
            for el in to_visit:
                if self.connectios[el]:  # and el not in to_visit:
                    new_visits.extend(self.connectios[el])
                    new_visits = list(set(new_visits))
            to_visit.extend(new_visits)
            if cnt > self.size:
                return -1

    def is_in(self, panda):
        if panda in self.pandas:
            return True
        return False

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) not in [-1, False]

    def how_many_gender_in_network(self, level, panda, gender, cnt=1):
        if not self.is_in(panda):
            return False
        er404 = False
        to_visit = self.connectios[panda]
        matches = []
        while not er404:
            new_visits = []
            for el in to_visit:
                if el.gender() == gender:
                    matches.append(el)
                if self.connectios[el]:
                    new_visits.extend(self.connectios[el])
            to_visit.extend(list(set(new_visits)))
            if cnt == level:
                er404 = True
            cnt += 1
        if panda in set(matches):
            matches.remove(panda)
        return len((set(matches)))

    def save_panda(self, file_name):
        with open(file_name + ".json", 'w') as outfile:
            for el in self.pandas:
                dump(el.serialize(), outfile, indent=4)
            for key, value in self.connectios.items():
                for el in value:
                    dump({key.__str__(): el.serialize()}, outfile, indent=4)


def main():
    fb = PandaSocialNetwork()
    pesho = Panda('pesho')
    gosho = Panda('gosho')
    ivan = Panda('ivan')
    azis = Panda('azis')
    strashko = Panda('strashko')
    fb.make_friends(pesho, gosho)
    fb.make_friends(gosho, ivan)
    fb.make_friends(gosho, azis)
    fb.make_friends(ivan, strashko)
    stefcho = Panda('stefcho')
    fb.add_panda(stefcho)
    fb.make_friends(stefcho, strashko)
    print(fb.connection_level(pesho, stefcho))


if __name__ == '__main__':
    main()
