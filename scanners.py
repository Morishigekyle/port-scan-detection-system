import os
import re

filePath = "./ssh.log.txt"
fd = open(filePath, 'r')

# with fd as reader :
#     for line in reader :
#         # print( line )



# with open("ssh.log.txt") as f:
	# content = f.readlines()
# content = [x.strip() for x in content]

# f = open("ssh.log.txt", "r")
# lines = f.readlines()
# result = []
# for x in lines:
# 	result.append(x.split(' ')[1])
# f.close()

# f = open("ssh.log.txt", "r")
# with open("ssh.log.txt") as f:
# 	print zip(*[line.split() for line in f])[1]

# def file_len("ssh.log.txt"):
# 	with open("ssh.log.txt") as f:
# 		for i, l in enumerate(f):
# 			pass
# 	return i+1

num_lines = sum(1 for line in open ("ssh.log.txt"))
# print(num_lines)
ScanAttempts = str(num_lines)
f = open("ssh.log.txt","r")
lines = f.readlines()
# print(lines)
for line in lines:
	col = line.split("\t")
	# print(col[2])
	hostip = []
	hostip.insert(0,col[2])
	# allip = []
	# [allip.extend(x) for x in hostip]
	# for x in allip:
	# 	print(x)
	hosted = ''.join(str(e) for e in hostip)
	# print(col[2])
	# hostip = print(col[2])
	# print(hostip)
	hostip1 = []
	hostip1.insert(0,col[4])
	# print(hostip1)
	hosted1 = ''.join(str(e) for e in hostip1)
	# print(hosted1)

f = open("scanners_found.txt", "w+")
f.write("[Scan Attempts]" + " " + ScanAttempts + "\n")
f.write("\n[Scan Origin Hosts]" + "\n " + hosted + "\n. . . . . . ." + "\n?\n")
f.write("\n[Scan Destination Hosts]" + "\n " + hosted1 + "\n. . . . . . ." + "\n?\n")


# f = open("scanners_found.txt", "r")




	
	# print(hostip)	
	# uniqip = set(map(tuple, hostip))
	# print(uniqip)
	# uniqip = [list(t) for t in set(map(tuple, hostip))]
	# print(uniqip)


