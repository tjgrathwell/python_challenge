
def makenext(last):
    prev = ''
    count = 0
    result = ''
    for char in str(last):
        if char != prev:
            if count > 0:
                result = result + str(count) + str(prev)
            count = 1
            prev = char
        else:
            count = count + 1
    result = result + str(count) + str(prev)
    return result
            
lastone = 1
for i in range(0,30):
    lastone = makenext(lastone)

print len(lastone)