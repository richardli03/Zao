import sys
import csv

print(sys.argv[1])

x= isinstance(sys.argv[1],int)
print(x)

try: 
      tmp = int(sys.argv[1])
except: 
      print('not a number')