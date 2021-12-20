import json


def dict_to_json(dictionary: dict):
    with open("sample.json", "w") as outfile:
        json.dump(dictionary, outfile)
