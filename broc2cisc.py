import json
from pprint import pprint

import yaml


def main():
    print("JSON")
    with open('broc_act_conf.json', 'r') as jsonFile:
        # load jason file
        myJasonFile = json.load(jsonFile)
    pprint(myJasonFile)

    print("\nYAML")
    yamlFile = open("broc_act_conf.yaml", 'r')
    dictionary = yaml.load(yamlFile, Loader=yaml.FullLoader)
    for key, value in dictionary.items():
        pprint (key + " : " + str(value))


if __name__ == "__main__":
    # calling the main function
    main()