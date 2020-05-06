import json
from pprint import pprint
#import cisco
import yaml

def print_cisco_alias(vsan_id="100"):
    #print("Alias JSON")
    with open('brocade_alias.json', 'r') as jsonAliasFile:
        # load jason file
        aliasJasonFile = json.load(jsonAliasFile)
    #pprint(aliasJasonFile)

    #aliasJasonFile is of type dict
    #print(type(aliasJasonFile))

    #Print a list of the aliases
    #print(list(aliasJasonFile))
    for i in list(aliasJasonFile.items()):
        name = i[1]['alias_name']
        wwpn = i[1]['alias_wwpn']
        print("conf t")
        print("fcalias name "+name+" vsan "+vsan_id)
        print("member pwwn "+wwpn)
        print("end")

def main():
    #print("JSON")
    with open('broc_act_conf.json', 'r') as jsonFile:
        # load jason file
        myJasonFile = json.load(jsonFile)
    #pprint(myJasonFile)

    #print("\nYAML")
    yamlFile = open("broc_act_conf.yaml", 'r')
    dictionary = yaml.load(yamlFile, Loader=yaml.FullLoader)
    #for key, value in dictionary.items():
    #    pprint (key + " : " + str(value))

    #print_cisco_alias("101")

if __name__ == "__main__":
    # calling the main function
    main()