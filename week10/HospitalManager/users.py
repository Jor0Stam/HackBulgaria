from METADATA import *
from passlib.hash import pbkdf2_sha256
# pbkdf2_sha256.verify("password", hash) - verify passwords


def encrypt(password):
    return pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)


class User:

    def __init__(self, name, password, age):
        self.name = name
        self.password = encrypt(password)
        self.age = age

    def __repr__(self):
        return USR_INFO.format(self.name)

    def __str__(self):
        return USR_INFO.format(self.name)

    def __eq__(self, other):
        return self.name == other.name and self.password == other.password

    def __hash__(self):
        return hash(self.name)

    @staticmethod
    def promote_to_doctor(baseuser, title):
        return Doctor(baseuser.name, baseuser.password, baseuser.age, title)

    @staticmethod
    def promote_to_patient(baseuser, doctor=None):
        return Patient(baseuser.name, baseuser.password, baseuser.age, doctor)


class Patient:

    def __init__(self, name, password, age, doctor):
        User.__init__(self, name, password, age)
        self.doctor = doctor
        self.available_queries = []

    def __str__(self):
        return PATIENT_INFO.format(self.name, self.doctor.name)

    def __repr__(self):
        return PATIENT_INFO.format(self.name, self.doctor.name)

    def __eq__(self, other):
        return self.name == other.name and self.password == other.password

    def __hash__(self):
        return hash(self.name)


class Doctor:

    def __init__(self, name, password, age, title):
        User.__init__(self, name, password, age)
        self.title = title
        self.patients = []
        self.visitation_hours = {}  # hour: availability
        self.available_queries = []

    def __str__(self):
        return DOCTOR_INFO.format(self.name, self.title)

    def __repr__(self):
        return DOCTOR_INFO.format(self.name, self.title)

    def __eq__(self, other):
        return self.name == other.name and self.password == other.password

    def __hash__(self):
        return hash(self.name)

    def add_patient(self, patient):
        self.patients.extend(patient)

    def add_hours_for_visitations(self, hour):
        self.visitation_hours[hour] = "Free"


def main():
    test_user = User("Az", "Pass", 20)
    test_user2 = User("Az", "Pass", 20)
    test_user = User.promote_to_doctor(test_user, "High Level Surgeon")
    test_user2 = User.promote_to_doctor(test_user, "a")
    print(test_user.password)


if __name__ == "__main__":
    main()
