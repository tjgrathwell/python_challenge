# http://www.pythonchallenge.com/pc/return/romance.html

# the implication of the hint image is to use cookies with the old linked-list thing.

import urllib2
import cookielib
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

import re
nothing_search = re.compile('and the next busynothing is (\d+)')

cookie_info = []
a_cookie = None
def get_next(nothing):
    # reading a cookie from 'nothing=' complains 'you should have followed busynothing'
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + str(nothing)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    cooks = cj.make_cookies(response, req)
    print data
    cookie_info.append(cooks[0].value)
    next_nothing = re.search(nothing_search, data)
    if next_nothing:
        return next_nothing.groups()[0]
    return None

nothings = [12345]    
for i in xrange(4000):
    next_nothing = get_next(nothings[-1])
    if not next_nothing:
        break
    nothings.append(next_nothing)
    
import urllib
bz2file = urllib.unquote_plus(''.join(cookie_info))
import bz2
of = open('cookied.txt', 'w')
of.write(bz2file)
print bz2.decompress(bz2file)

# gives:
# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.

# per p13,
# mozart's father is leopold, phone 555-VIOLIN

# http://www.pythonchallenge.com/pc/stuff/violin.php

req = urllib2.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345')
response = urllib2.urlopen(req)
cooks = cj.make_cookies(response, req)
cookie = cooks[0]
cookie.value = 'the flowers are on their way'

req = urllib2.Request('http://www.pythonchallenge.com/pc/stuff/violin.php')
cj.set_cookie(cookie)
cj.add_cookie_header(req)
print urllib2.urlopen(req).read()

# oh well, don't you dare to forget the balloons