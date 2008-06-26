# http://www.pythonchallenge.com/pc/hex/copper.html
# it's a joystick. hello joystick.

# directs you to white.gif, which is totally black (colour 0) - but awfully large, considering. some sort of animated gif, yeh?
# 133 frames in gif.

import Image
im = Image.open('white.gif')
pen  = []
for frame in xrange(133):
    im.seek(frame)
    pixels = list(im.getdata())
    for x in xrange(im.size[0]):
        for y in xrange(im.size[1]):
            px = pixels[y*im.size[1] + x]
            if px != 0:
                # the errant pixels in each image are pen-writing instructions: they have x,y offset from 100,100; imagine the joystick as pictured on the level page.
                pen.append((x-100, y-100))

x,y = 25,50
out_image = Image.new('RGB', (400,300))
for dx,dy in pen:
    if dx == 0 and dy == 0:
        # pick up our pen and go away
        x += 50
    else:
        x += dx
        y += dy
    out_image.putpixel((x,y), (255,0,0))
out_image.save('scribble.png')

# the message is 'bonus'