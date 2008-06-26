# zipfile p21.zip generated from p20.py - contains file package.pack

# I think this is my favorite puzzle :)

import sys
import zlib
import bz2
content = open('package.pack','rb').read()

length = len(content)
ops = []
while length > 20:
    if content.startswith('B'):
        content = bz2.decompress(content)
        ops.append('B')
    else:
        try:
            content = zlib.decompress(content)
            ops.append('Z')
        except:
            content = content[::-1]
            ops.append('R')
    length = len(content)
    
print content

#  final message is "look at your logs"
print '\n'.join(''.join(ops).split('R'))

# banner says 'COPPER'