from PIL import Image

w = Image.open('wire.png')
o = Image.new(w.mode, (100,100))

# The winding sequence goes (100, 99, 99, 98, 98, 97, 97... etc
# so after the first iteration, we do each # march twice
# this is held in the prevmarch tuple

total = 0
togo = 100
direction = 'r'
prevmarch = (100,2)
(x,y) = (-1,0)
while total < 10000:
    while togo:
        print (x,y)
        if direction == 'r':
            x = x + 1
            o.putpixel((x,y), w.getpixel((total,0)))
        elif direction == 'd':
            y = y + 1
            o.putpixel((x,y), w.getpixel((total,0)))
        elif direction == 'l':
            x = x - 1
            o.putpixel((x,y), w.getpixel((total,0)))
        elif direction == 'u':
            y = y - 1
            o.putpixel((x,y), w.getpixel((total,0)))
        togo = togo - 1
        total = total + 1
    if direction == 'r': direction = 'd'
    elif direction == 'd': direction = 'l'
    elif direction == 'l': direction = 'u'
    elif direction == 'u': direction = 'r'
    if prevmarch[1] == 2:                   # first time 
        prevmarch = (prevmarch[0]-1, 1)
    else:
        prevmarch = (prevmarch[0], 2)
    togo = prevmarch[0]
    print total, togo
        
o.save("unwound.png","PNG")