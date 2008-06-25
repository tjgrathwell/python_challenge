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
    line = line.strip()
    file_a.append(line[:53])
    file_b.append(line[56:])

import difflib
d = difflib.Differ()
print '\n'.join(d.compare(file_a, file_b))