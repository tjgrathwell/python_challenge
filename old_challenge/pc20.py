# unreal

from urllib2 import *
url = "pythonchallenge.com/pc/hex/unreal.jpg"
protocol = "http://"

import base64
base64string = base64.encodestring('%s:%s' % ('butter', 'fly'))[:-1]

b = 2123456789
for i in range(0,1):
    try:
        headers = { 'Range' : 'bytes=' + '1152983631-' }
        request = Request(protocol + url, None, headers)
        request.add_header("Authorization", "Basic %s" % base64string)
        response = urlopen(request)
    except HTTPError, e:
        print e
        print e.headers
    except URLError, e:
        print e
        print e.headers
    else:
        r = response.read()
        print len(r)
        if len(r) < 1000:
            print r
            print response.info()
        else:
            out = open("unreal" + str(b) + ".jpg","wb")
            out.write(r)
        b = b + len(r)