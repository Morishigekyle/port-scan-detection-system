import os
import re

filePath = "./ssh.log.txt"
fd = open(filePath, 'r')

num_lines = sum(1 for line in open ("ssh.log.txt"))
scan_attempts = str(num_lines)

f = open("ssh.log.txt","r")
lines = f.readlines()

f = open("scanners_found.txt", "w+")
f.write("[Scan Attempts]")
f.write("\n" + scan_attempts + "\n")	
f.write("\n[Scan Origin Hosts]")

f = open("scanners_found.txt", "a+")
for line in lines:
	col = line.split("\t")
	hostip = []
	hostip.insert(0,col[2])
	hosted = ''.join(str(e) for e in hostip)
	
	f.write("\n" + hosted)
	
f = open("scanners_found.txt", "a+")
f.write("\n" + "\n[Scan Destination Hosts]")

f = open("scanners_found.txt", "a+")
for line in lines:
	col = line.split("\t")
	hostip1 = []
	hostip1.insert(0,col[4])
	hosted1 = ''.join(str(e) for e in hostip1)
	
	f.write("\n" + hosted1)
	
f.close()