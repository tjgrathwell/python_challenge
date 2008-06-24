# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib2
import re
nothing_search = re.compile('and the next nothing is (\d+)')

def get_next(nothing):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(nothing)
    data = urllib2.urlopen(url).read()
    print data
    next_nothing = re.search(nothing_search, data)
    return next_nothing.groups()[0]

nothings = [46059]    
for i in xrange(400):
    next_nothing = get_next(nothings[-1])
    nothings.append(next_nothing)
    
# at 92118 we get 'divide by two and keep going' ... rather than coding in special cases just substitute it up there :)

# peak.html