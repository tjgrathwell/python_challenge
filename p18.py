# http://www.pythonchallenge.com/pc/return/balloons.html

# the difference is brightness - http://www.pythonchallenge.com/pc/return/brightness.html

# tells you to hit http://www.pythonchallenge.com/pc/return/deltas.gz

# = two mostly-the-same files, in hex, put up next to each other. the implication is to do something with the delta...

# first file: first 53 chars. then 3 char gap, then 53 more.

from gzip import GzipFile
fullfile = GzipFile('deltas.gz')
file_a = []
file_b = []
for line in fullfile:
    file_a.append(line[:53].strip())
    file_b.append(line[56:].strip())

import difflib
one, two, three = [], [], []
for line in difflib.ndiff(file_a, file_b):
    if len(line) < 3:
        continue
    if line.startswith('-'):
        one.append(line[2:])
    elif line.startswith('+'):
        two.append(line[2:])
    else:
        three.append(line[2:])
        
for file,filename in [(one,'diffone.png'),(two,'difftwo.png'),(three,'diffthree.png')]:
    of = open(filename,'wb')
    for line in file:
        for hex in line.split(' '):
            of.write(chr(int(hex,16)))
            
# l/p butter/fly for ../hex/bin.html