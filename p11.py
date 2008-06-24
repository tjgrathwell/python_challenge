# http://www.pythonchallenge.com/pc/return/5808.html

# 'cave.jpg' is the only thing here, and looks like an interpolation of two images.

import Image
im = Image.open('cave.jpg') # it's 640x480 btw

even = Image.new('RGB', (320,240), (255,255,255))
odd = Image.new('RGB', (320,240), (255,255,255))

for i in xrange(640):
    for j in xrange(320):
        px = im.getpixel((i,j))
        if i%2 == 0 and j%2 == 0:
            even.putpixel((i/2,j/2),px)
        elif i%2 == 1 and j%2 == 1:
            odd.putpixel(((i-1)/2,(j-1)/2),px)

even.save('cave-1.jpg')
odd.save('cave-2.jpg')

# image says 'evil'