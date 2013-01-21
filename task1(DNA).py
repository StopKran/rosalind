#!/usr/bin/python
import sys
import collections

def dnaStringValues (dnastring):
	result_data = collections.OrderedDict([('A',0), ('C',0), ('G',0), ('T',0)])
	for s in dnastring:
		result_data[s] += 1
	return result_data.values()
		

	
input_file  = open(sys.argv[1],  "r")
output_file = open("result.txt", "w")

data = input_file.read().split()[0]
for i in dnaStringValues(data):
	print >> output_file, i	,

