# http://www.pythonchallenge.com/pc/return/mozart.html

# graphic mozart.gif shows a number of pink areas that obviously need to be shifted so they line up

# the pink areas are seven pixels long, of the format white-5xpink-white. the pink is (255, 0, 255) (index 195), the white is (251, 251, 251) (index 251)

import Image
im = Image.open('mozart.gif')

shifts = []
for line in xrange(im.size[1]):
    for px in xrange(im.size[0]):
        if im.getpixel((px,line)) == 195:
            shifts.append(px)
            break
            
out = Image.new('RGB', im.size)
for line in xrange(im.size[1]):
    pixrange = range(shifts[line], im.size[0]) + range(0, shifts[line])
    shifted_px = [im.getpixel((i,line)) for i in pixrange]
    [out.putpixel((i,line), px) for i, px in enumerate(shifted_px)]
out.save('mozart-shift.gif')

# romance