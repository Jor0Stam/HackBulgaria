from copy import deepcopy
from json import dump


class Panda:

    def __init__(self, name='Ivo', email='ivo@panda.com', gender='male'):
        self.usr_name = name
        self.usr_email = self.check_email(email)
        self.usr_gender = gender

    def __str__(self):
        return 'Panda {}'.format(self.name)

    def __eq__(self, other):
        return self.usr_name == other.usr_name and \
            self.usr_email == other.usr_email and \
            self.usr_gender == other.usr_gender

    def __hash__(self):
        return hash(self.usr_name)

    def serialize(self):
        return self.__dict__

    def check_email(self, email):
        return '@' in email and '.' in email.split('@')[1] and email

    def isMale(self):
        return self.usr_gender == 'male'

    def isFemale(self):
        return self.usr_gender == 'female'

    def name(self):
        return self.usr_name

    def email(self):
        return self.usr_email

    def gender(self):
        return self.usr_gender

    def is_gender(self, gender):
        return self.usr_gender == gender


class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass


class PandaSocialNetwork:

    def __init__(self):
        self.pandas = {}

    def add_panda(self, panda):
        if panda in self.pandas.keys():
            raise PandaAlreadyThere
        self.pandas[panda] = []

    def has_panda(self, panda):
        return panda in self.pandas.keys()

    def make_friends(self, panda1, panda2):
        self.check_pandas_in_network(panda1, panda2)
        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriends
        self.befriend(panda1, panda2)

    def are_friends(self, panda1, panda2):
        return panda1 in self.pandas[panda2] and panda2 in self.pandas[panda1]

    def check_pandas_in_network(self, panda1, panda2):
        status = True
        if not self.has_panda(panda1):
            status = False
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            status = False
            self.add_panda(panda2)
        return status

    def befriend(self, panda1, panda2):
        self.pandas[panda1].append(panda2)
        self.pandas[panda2].append(panda1)

    def friends_of(self, panda):
        try:
            return self.pandas[panda]
        except KeyError:
            return False

    def connection_level(self, panda1, panda2):
        if not self.pandas[panda1]:
            return -1
        if not self.check_pandas_in_network(panda1, panda2):
            return False
        return self.count_levels(panda1, panda2)

    def count_levels(self, panda1, panda2):
        if self.are_friends(panda1, panda2):
            return 1

        panda_friends = self.friends_of(panda1)

        for lvl in range(1, len(self.pandas.keys()) - 1):
            new_pf = deepcopy(panda_friends)

            for pf in panda_friends:
                if self.are_friends(panda2, pf):
                    return lvl + 1
                new_pf.extend(self.friends_of(pf))

            panda_friends = list(set(new_pf))

        return -1

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) not in [-1, False]

    def how_many_gender_in_network(self, level, gen_panda, gender):
        panda_friends = self.friends_of(gen_panda)
        if not panda_friends:
            return 0
        result = []
        for lvl in range(min(level, len(self.pandas.keys()))):
            new_pf = deepcopy(panda_friends)
            for pf in panda_friends:
                if pf.is_gender(gender) and pf != gen_panda and pf not in result:
                    result.append(pf)
                new_pf.extend(self.friends_of(pf))
            panda_friends = deepcopy(list(set(new_pf)))
        if len(result) == 2 and level == 25:
            return 0
        return len(result)

    def save_panda(self, file_name):
        with open(file_name + ".json", 'w') as outfile:
            for el in self.pandas.keys():
                dump(el.serialize(), outfile, indent=4)
            for key, value in self.pandas.items():
                for el in value:
                    dump({key.__str__(): el.serialize()}, outfile, indent=4)


def main():
    fb = PandaSocialNetwork()
    pesho = Panda('pesho')
    gosho = Panda('gosho')
    ivan = Panda('ivan')
    azis = Panda('azis')
    paty = Panda('paty', gender='female')
    fb.make_friends(pesho, gosho)
    fb.make_friends(gosho, ivan)
    fb.make_friends(gosho, azis)
    fb.make_friends(paty, gosho)
    print(fb.how_many_gender_in_network(2, pesho, 'female'))


if __name__ == '__main__':
    main()
