from urllib.request import urlopen
import re

f=open("outpur.txt","w+")
webpage=urlopen("https://www.ebi.ac.uk/merops/cgi-bin/smi_index").read()


#print(type(webpage))


#str1=""
#temp=""
#for line in webpage:
#	print(line)
#	print("*************)

#print(webpage)
for line in webpage.readline():
	f.write(str(line))
#	print(str(line)+"\n")

