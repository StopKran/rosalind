#!/usr/bin/python
import sys
import collections

def reverseComplement (dnastring):
	result = ""
	complement = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
	for s in dnastring[::-1]:
		result += complement[s]
	return result
		

	
input_file  = open(sys.argv[1],  "r")
output_file = open("result.txt", "w")

data = input_file.read().split()[0]
print >> output_file, reverseComplement(data)

