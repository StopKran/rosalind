#!/usr/bin/python
import sys

input_file  = open(sys.argv[1],  "r")
output_file = open("result.txt", "w")
main_str = input_file.readline()
find_str = input_file.readline()

find_num = main_str.find(find_str)
find_prev = 0
while find_num != -1:
	print >> output_file, find_num+find_prev+1,
	find_prev += find_num+1
	main_str = main_str[find_num+1:]  
	find_num = main_str.find(find_str)
	




