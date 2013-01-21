#!/usr/bin/python
import sys
import collections

def dnaToRna (dnastring):
	result = ""
	for s in dnastring:
		if s == 'T' :
			result += 'U'
		else:
			result += s
	return result
		

	
input_file  = open(sys.argv[1],  "r")
output_file = open("result.txt", "w")

data = input_file.read().split()[0]
print >> output_file, dnaToRna(data)

