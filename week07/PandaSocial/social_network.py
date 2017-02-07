from panda import *
from json import dump, load
from codecs import getreader


class PandaSocialNetwork:

    def __init__(self):
        self.pandas = []
        self.connectios = {}
        self.size = 0

    def __eq__(self, other):
        return set(self.pandas) == set(other.pandas) and \
            set(list(self.connectios.keys())) == set(list(other.connectios.keys()))
            # cmp(self.connectios, other.connectios) == 0

    def __hash__(self):
        return hash(self.pandas)

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
            to_visit.extend(new_visits)
            if cnt > self.size:
                return -1

    def is_in(self, panda):
        if panda in self.pandas:
            return True
        return False

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2):
            return self.connection_level(panda1, panda2) != -1
        return False

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
            to_dump_pandas = []
            to_dump_connections = []
            for el in self.pandas:
                to_dump_pandas.append(el.serialize())
            for key, value in self.connectios.items():
                for el in value:
                    to_dump_connections.append({key.__str__(): el.serialize()})
            dump([to_dump_pandas, to_dump_connections], outfile, indent=4)

    @staticmethod
    def format_loaded_key(key):
        return Panda(name=key[:" who is"],
                     email=key["with email ":],
                     gender=key["who is "::" with email"])

    @staticmethod
    def load_panda(file_name):
        with open(file_name + '.json', 'rb') as f:
            reader = getreader("utf-8")
            obj = load(reader(f))
            res = PandaSocialNetwork()
            for el in obj[0]:
                res.add_panda(Panda(name=el["usr_name"],
                                    gender=el["usr_gender"],
                                    email=el["usr_email"]))
            for el in obj[1]:
                for key, value in el.items():
                    if key in res.connectios.keys():
                        res.connectios[PandaSocialNetwork.format_loaded_key(key)].append(value)
                    else:
                        res.connectios[PandaSocialNetwork.format_loaded_key(key)] = []
                        res.connectios[PandaSocialNetwork.format_loaded_key(key)].append(
                            Panda(name=value["usr_name"],
                                  gender=value["usr_gender"],
                                  email=value["usr_email"]))
            return res

# self.assertEqual(self.network.connection_level(self.ivo, maria), 3)
# AssertionError: 2 != 3


def main():
    fakylteto = PandaSocialNetwork()
    ivo = Panda("Ivo")
    maria = Panda("Maria")
    viktor = Panda("Viktor")
    pesho = Panda("Pesho")
    ivan = Panda("ivan")
    fakylteto.add_panda(maria)
    # fakylteto.make_friends(sam, joro)
    fakylteto.make_friends(ivo, viktor)
    fakylteto.make_friends(viktor, pesho)
    # fakylteto.make_friends(ivan, viktor)
    # fakylteto.make_friends(maria, pesho)
    # fakylteto.save_panda("TestSave")
    # test = PandaSocialNetwork.load_panda("TestSave")
    # print(test.connectios)
    # print(test == fakylteto)
    print(fakylteto.connection_level(ivo, maria))
    # print(fakylteto.connection_level(joro, pesho))
    # fakylteto.make_friends(ivan, pesho)
    # fakylteto.make_friends(ivan, joro)
    # print(fakylteto.how_many_gender_in_network(2, sam, "female"))
    # print(PandaSocialNetwork().load_panda("ThePandaBook"))

    # fix load social network!s


if __name__ == "__main__":
    main()
