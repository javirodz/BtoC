import json
from pprint import pprint
import re
import yaml

def load_defined_conf(zone_file="sw1-zoneshow.txt"):
    with open(zone_file) as zone_in_text:
        for line in zone_in_text:
            if line.startswith("Effective"):
                return
            else:
                print(line,end = '')
    return

def load_effective_conf(zone_file="sw1-zoneshow.txt"):
    with open(zone_file) as zone_in_text:
        for line in zone_in_text:
            if line.startswith("Effective"):
                print(line,end = '')
                for line in zone_in_text:
                    print(line,end = '')
                return
    return

def defined_zoneset(zone_file="sw1-zoneshow.txt"):
    defined_cfg_name = "NONE"
    zoneset = set()
    with open(zone_file) as zone_in_text:
        for line in zone_in_text:
            if line.startswith(" cfg"):
                defined_cfg_name = line.split(':')[1]
                for line in zone_in_text:
                    if line.startswith(" zone"):
                        # remove spaces, newlines and tabs and leave only a csv str of the zones in the zoneset Set()
                        str_zoneset_orig = ','.join(str(s) for s in zoneset)
                        str_zoneset_notabs = str_zoneset_orig.replace('\t', '')
                        str_zoneset_nospace = str_zoneset_notabs.replace(' ', '')
                        str_zoneset = str_zoneset_nospace.replace('\n', '')
                        return defined_cfg_name, str_zoneset
                    else:
                        for item in line.split(';'):
                            zoneset.add(item)
    print("SOME ERROR")
    return

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

def cisco_zoneset(defined_cfg_name, str_zoneset, vsanid = "100", switch_id_zoneset_file="sw_zoneset"):
    with open(switch_id_zoneset_file, 'w') as zonesetFile:
        #print("configure terminal")
        zonesetFile.write("configure terminal\n")
        #print("zoneset name "+defined_cfg_name.replace('\t', '').replace('\n', '').replace(' ', '')+" vsan "+vsanid)
        zonesetFile.write("zoneset name "+defined_cfg_name.replace('\t', '').replace('\n', '').replace(' ', '')+" vsan "+vsanid+"\n")
        for i in str_zoneset.split(','):
           if i != '':
               #print("member "+i)
               zonesetFile.write("member "+i+"\n")
        #print("end")
        zonesetFile.write("end\n")

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

    #load_defined_conf()

    #load_effective_conf()

    #Extract the defined zoneset from the zoneshowfile for switch 1
    #the zoneshow file is from the 'zoneshow' command in a brocade switch
    sw_zoneshow_input_file = "sw1-zoneshow.txt"
    defined_zoneset_name, str_zoneset = defined_zoneset(sw_zoneshow_input_file)

    #print the commands to create a zoneset in a cisco mds to a .mds file
    vsanid = "100"
    switch_id_zoneset_file = "sw1_zoneset.mds" #Destination File for the Script
    cisco_zoneset(defined_zoneset_name, str_zoneset, vsanid, switch_id_zoneset_file)

    #Extract the defined zoneset from the zoneshowfile for switch 2
    #the zoneshow file is from the 'zoneshow' command in a brocade switch
    sw_zoneshow_input_file = "sw2-zoneshow.txt"
    defined_zoneset_name, str_zoneset = defined_zoneset(sw_zoneshow_input_file)

    #print the commands to create a zoneset in a cisco mds to a .mds file
    vsanid = "200"
    switch_id_zoneset_file = "sw2_zoneset.mds" #Destination File for the Script
    cisco_zoneset(defined_zoneset_name, str_zoneset, vsanid, switch_id_zoneset_file)


if __name__ == "__main__":
    # calling the main function
    main()