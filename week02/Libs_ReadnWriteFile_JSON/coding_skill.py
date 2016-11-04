import sys
import json


def format_content(content):
    to_p = ""
    for key, value in content.items():
        to_p += key + " - " + value + "\n"

    return to_p


def collect_languages(data):
    langs = set()
    for i in data:
        for skillz in i['skills']:
            langs.add(skillz['name'])

    return langs


def lang_to_pts(langs):
    langs_to_pts = {}
    for i in range(len(langs)):
        langs_to_pts[langs.pop()] = 0

    return langs_to_pts


def compare_points(langs, data):
    for i in data:
        for skillz in i['skills']:
            var1 = skillz['level']
            var2 = langs[skillz['name']]
            if var1 > var2:
                langs[skillz['name']] = i['first_name'] + i['last_name']

    return langs


def main():
    with open(sys.argv[1], "r") as f:
        data = "".join(f.readlines())
        data = json.loads(data)

        langs_to_pts = lang_to_pts(collect_languages(data['people']))
        return compare_points(langs_to_pts, data['people'])


if __name__ == "__main__":
    print(main())
