#endian switch

import struct
f = open("indian.wav","rb")
string = f.read()

out = open("endian.wav","wb")
out.write(string[:44])
string = string[44:]

leng = len(string)

result = []
for i in range(0,leng/4):
    result.append(string[i*4+3])
    result.append(string[i*4+2])
    result.append(string[i*4+1])
    result.append(string[i*4+0])

out.write(''.join(result))

#solution idiot