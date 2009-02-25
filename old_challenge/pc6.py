#zip

import os, re, zipfile
expr = re.compile("ext nothing is ([0-9]*)")

#out = open("zipout.txt",'w')
z = zipfile.ZipFile("channel.zip","r")

nothing = 90052
comments = []
for i in range(0,1000):
    file = z.read(str(nothing) + ".txt")
    comments.append((z.getinfo(str(nothing) + ".txt")).comment)
    
    print file
    if expr.search(file):
        nothing = expr.search(file).group(1)
    else: break
        
print ''.join(comments)