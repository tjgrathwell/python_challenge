# http://www.pythonchallenge.com/pc/return/italy.html

# the spiral one! de-spiral the one line image http://www.pythonchallenge.com/pc/return/wire.png - it's meant to be 100x100

import Image
im = Image.open('wire.png')
out_image = Image.new('RGB', (100,100))

# right 100, down 99, left 98, up 97, right 96...
step = 100
total_px = 0
x,y = 0,0
turns = 0
# use mod-four to do direction
directions = ['right', 'down', 'left', 'up']
last_step = 100
while step > 0:
    direction = directions[turns % 4]
    print direction
    if direction == 'right':
        [out_image.putpixel((x+i,y), im.getpixel((total_px+i,0))) for i in xrange(step)]
        x += step - 1
    elif direction == 'up':
        [out_image.putpixel((x,y-i), im.getpixel((total_px+i,0))) for i in xrange(step)]
        y -= step - 1
    elif direction == 'left':
        [out_image.putpixel((x-i,y), im.getpixel((total_px+i,0))) for i in xrange(step)]
        x -= step - 1
    else:
        [out_image.putpixel((x,y+i), im.getpixel((total_px+i,0))) for i in xrange(step)]
        y += step - 1
    print x, y
    total_px += step
    if last_step == step:
        step -= 1
    else:
        last_step = step
    turns += 1

out_image.save('de-spiral.png')

# this algorithm is a mess! however, it lends a picture of a cat. cat.html tells you the cat's name is uzi.