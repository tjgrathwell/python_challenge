# swans

from string import *

f = open("delta.txt")

first = []
second = []
for line in f:
    a = line[0:53]
    b = line[56:111]
    if not a.isspace(): first.append(a + '\n')
    if not b.isspace(): second.append(b)
        
print len(first), len(second)
import difflib
#diff = difflib.ndiff(first, second)
diff = difflib.ndiff(first, second)

firstn = []
secondn = []
thirdn = []
for item in diff:
    if item[0] == '+': firstn.append(item[2:])
    elif item[0] == '-': secondn.append(item[2:])
    elif item[0] == ' ': thirdn.append(item[2:])
  
def writeouthex(series,out):
    for line in series:
        s = line.strip().split()
        for char in s:
            out.write(chr(int(char,16)))
  
d1 = open("diff1.png","wb")
d2 = open("diff2.png","wb")
d3 = open("diff3.png","wb")
writeouthex(firstn,d1)
writeouthex(secondn,d2)
writeouthex(thirdn,d3)