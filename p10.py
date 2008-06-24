# http://www.pythonchallenge.com/pc/return/bull.html

# hint is the famous 'descriptive sequence'
# a = [1, 11, 21, 1211, 111221, 
# we want len a[30]

def get_next(prev):
    # split a number by groups: ie 1111223333 becomes [('1',4), ('2',2), ('3',4)]
    chunked_number = []
    for c in str(prev):
        if not chunked_number or chunked_number[-1][0] != c:
            chunked_number.append([c,1])
        else:
            chunked_number[-1][1] += 1
    return ''.join([str(b) + str(a) for a,b in chunked_number])
    
a = [1]
for i in xrange(30):
    a.append(get_next(a[-1]))
    
print len(a[30])

# 5808