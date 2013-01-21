#!/usr/bin/python
import sys

input_file  = open(sys.argv[1],  "r")
output_file = open("result.txt", "w")
data = input_file.read().split()

AA = Aa = aa = AA2 = Aa2 = aa2 = 0.0

AA += int(data[0])
Aa += int(data[1])
aa += int(data[2])

AA2 += AA * (AA - 1) * 2          #AA * AA
aa2 += aa * (aa - 1) * 2          #aa * aa
Aa2 += AA * aa * 4                #aa * AA
Aa2 += AA * Aa * 2                #AA * Aa
AA2 += AA * Aa * 2   
Aa2 += aa * Aa * 2                #aa * Aa
aa2 += aa * Aa * 2 
AA2 += Aa * (Aa - 1) /2			  #Aa * Aa
aa2 += Aa * (Aa - 1) /2
Aa2 += Aa * (Aa - 1)

result = (AA2 + Aa2) / (AA2 + Aa2 + aa2) 
print >> output_file, result


