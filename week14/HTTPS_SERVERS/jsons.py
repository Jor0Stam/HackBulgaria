from requests import get


def get_skills():
    return get("https://hackbulgaria.com/hackfmi/api/skills/").json()


def get_teams():
    return get("https://hackbulgaria.com/hackfmi/api/public-teams/").json()


def get_mentors():
    return get("https://hackbulgaria.com/hackfmi/api/mentors/").json()


def test():
    return get("https://hackbulgaria.com/hackfmi/api/mentors/")


def main():
    print(test().status_code)


if __name__ == "__main__":
    main()
