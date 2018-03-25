import os
import re

filePath = "./ssh.log.txt"
fd = open(filePath, 'r')

with fd as reader :
    for line in reader :
        print( line )



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

f = open("scanners_found.txt", "w+")
f.write("[Scan Attempts]" + " " + ScanAttempts)
f.close()

f = open("scanners_found.txt", "r")
