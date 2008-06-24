# http://www.pythonchallenge.com/pc/def/channel.html

# http://www.pythonchallenge.com/pc/def/channel.zip

# A text file with a linked list structure like the 'nothings' before...
# Readme says 'hint1: start from 90052'

import zipfile
import re
z = zipfile.ZipFile('channel.zip')
nothing_search = re.compile('Next nothing is (\d+)')

def get_next(z, nothing):
    file = str(nothing) + '.txt'
    data = z.read(file)
    next_nothing = re.search(nothing_search, data)
    if not next_nothing:
        return 0,0
    return next_nothing.groups()[0], z.getinfo(file).comment
    
nothings = [90052]
char = 0
while 1:
    next_nothing, comment = get_next(z,nothings[-1])
    if not next_nothing:
        break
    print comment,
    char += 1
    if char > 64:
        char = 0
        print
    nothings.append(next_nothing)
    
# Even though it's more work to make it spell out the banner at the correct width, the answer is actually 'OXYGEN' which is way easier to see :p