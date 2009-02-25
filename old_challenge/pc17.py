from urllib2 import *
import re, urllib

url = 'http://pythonchallenge.com/pc/def/linkedlist.php?busynothing='

cookiescrape = re.compile("info=(.*?);")
searcher = re.compile("ext busynothing is ([0-9]*)")
next = '12345'
cookielist = []
stop = False
for i in range(0,1000):
    f = urlopen(url + next)
    cookiematch = cookiescrape.search(f.info()['set-cookie'])
    char = cookiematch.groups()[0]
    cookielist.append(char)
    for line in f.readlines():
        print line
        matchobj = searcher.search(line)
        if matchobj:
            next = matchobj.groups()[0]
        else: stop = True
    if stop: break
            
result = ''.join(cookielist)
print result


import bz2
print bz2.decompress(urllib.unquote_plus(result))

#is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.