# http://www.pythonchallenge.com/pc/hex/idiot2.html

# an image, 'but inspecting it carefully is allowed' - exif?

import urllib
import re
byterange = re.compile('bytes \d+-(\d+)')

next_number = 30203
while next_number:
    opener = urllib.FancyURLopener({})
    opener.addheader('range', 'bytes=%d-' % next_number)
    response = opener.open('http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg')
    if 'content-range' in response.info():
        match = re.match(byterange, response.info()["content-range"])
        next_number = int(match.groups()[0]) + 1
    else:
        next_number = None
    print response.info()
    print response.read()
    
# searching from the start of the range 0-2123456789 (from Content-Ranger header) eventually gives the message, "okay invader you're inside"
# searching from the end tells you the password is your 'nickname' backwards, and 'it' is hiding at 1152983631

opener = urllib.FancyURLopener({})
opener.addheader('range', 'bytes=1152983631-')
response = opener.open('http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg')
open('21.zip','wb').write(response.read())