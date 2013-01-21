#!/usr/bin/python
import sys
from operator import methodcaller

def FASTAParce(datastr):
	return map(lambda x: (x[0], x[1].replace('\n', '')), map(methodcaller("split", "\n", 1), datastr.split('>')[1:]))

def calculateGCContent (dnastring):
	gc = 0.0
	for s in dnastring:
		if s == 'G' or s == 'C':
			gc += 1
	return gc / len(dnastring)* 100
		

	
input_file  = open(sys.argv[1],  "r")
output_file = open("result.txt", "w")
data = FASTAParce(input_file.read())

maxvalue = 0.0
maxstr = ""

for taxon in data:
	taxon_gc = calculateGCContent(taxon[1])
	if taxon_gc > maxvalue:
		maxvalue = taxon_gc
		maxstr = taxon[0]

print >> output_file, maxstr
print >> output_file, maxvalue, "%"

