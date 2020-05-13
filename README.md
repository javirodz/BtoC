This small python cript takes the output of a brocade "showzone" command and creates the commands to 
configure the zones in a cisco environment

The "showzone" file name is sw1-zoneshow.txt or sw2-zoneshow.txt

The script doesn't have a menu, you have to uncomment the lines that will create the alias extract file first (sw[1|2]_alias_extract.txt.
Then fix that file a little bit. The file needs the alias name in line one and all the wwpns in line two (separated by ;)

The comment those methods and uncomment the zone methods. The zone methods expect a file of the form:
zone:	MA230Sw2_V7000
		ma230_sw2; Nimble1CAfc2; Nimble1CBfc2; v7k1_3; v7k1_4; v7k2_3; v7k2_4; Nimble2CAfc1; Nimble2CBfc1
    
The first line has the zone name and the second line has the fcaliases.

The output for the alias is:
sw[1|2]_cisco_alias.mds

The output for the zones is:
sw[1|2]_cisco_zones.mds

The zone set is:
sw[1|2]_zoneset.mds



