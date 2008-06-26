# http://www.pythonchallenge.com/pc/hex/bonus.html

# 'this' is an easter egg python module: 'import this'
# it's data is encoded in some rot13 sort of way for some reason

# we can copy the same algorithm and use it on the hint text from the p23 source

s = 'va gur snpr bs jung?'

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print "".join([d.get(c, c) for c in s])

# 'in the face of what?'
# from the zen: 'in the face of ambiguity'