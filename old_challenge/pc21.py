#package.pack
import array

f = open("package.pack","rb")
str = f.read()
import zlib, bz2

notreversed = True
methods = []
while str[0] == 'x' or str[0] == 'B' or str[-1] == 'x' or str[-1] == 'B':
    if str[0] == 'x':
        methods.append('x')
        str = zlib.decompress(str)
    elif str[0] == 'B':
        methods.append('B')
        str = bz2.decompress(str)
    else:
        strlist = list(str)
        strlist.reverse()
        str = ''.join(strlist)
        methods.append('r')

lastchar = ''
count = 0
tup_methods = []
print methods
for char in methods:
    if char == lastchar:
        count = count + 1
    else:
        if count is not 0:
            tup_methods.append((lastchar,count))
            lastchar = char
            count = 1
        else:
            lastchar = char
            count = count + 1
tup_methods.append((lastchar,count))
        
endstring = []
current = 0
mod = 0
#print tup_methods
for tup in tup_methods:
    if tup[0] == 'r':
        endstring.append('\n')
    else: 
        endstring.append(tup[0]*tup[1])
    #current = current + tup[1]
    #if current > 59:
    #    mod = mod + 1
    #    current = current - 59
    #    endstring.append('\n')

print len(''.join(endstring))
print len((''.join(endstring)).strip('r'))
print tup_methods
out = open("banner2.p","w")
out.write(''.join(endstring))
#out = open("package.unpack","wb")
#out.write(str)