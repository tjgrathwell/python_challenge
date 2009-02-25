#base64 

f = open("indian.txt")
big64string = ''.join([x.strip() for x in f.readlines()])

import base64
result = base64.b64decode(big64string)

out = open("indian.wav","wb")
out.write(result)