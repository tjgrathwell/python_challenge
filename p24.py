# http://www.pythonchallenge.com/pc/hex/ambiguity.html

# a maze! oh, what a maze.
# presumably when it says 'top to bottom' it means topright to bottomleft
# topright is size[0]-2,0
# bottomleft is 1,size[1]-1

# Maze algo:
#   - if the square we're in has an exit in a direction we've yet to go, go there
#   - if not, pop back one square

import Image
im = Image.open('maze.png')

white = (255,255,255,255)
blue = (0,0,255,255)

# seed algorithm with entrance square and the only valid exit out of it
a,b = im.size[0]-2,0
path = [(a,b,im.getpixel((a,b)),[(a,b+1)])]
in_maze = True
while in_maze:
    x, y, px, remaining_exits = path[-1]
    if x == 1 and y == im.size[1]-1:
        break

    if x<0 or x>im.size[0]-1 or y<0 or y>im.size[1]-1:
        path.pop()
        continue

    if px in [white,blue]:
        path.pop()
        continue
        
    im.putpixel((x,y), blue)
        
    if remaining_exits:
        next_x, next_y = remaining_exits.pop()
        next_px = im.getpixel((next_x, next_y))
        exits = [(next_x+1,next_y),(next_x-1,next_y),(next_x,next_y-1),(next_x,next_y+1)]
        path.append((next_x,next_y,next_px,exits))
    else:
        path.pop()
        im.putpixel((x,y), px)

# if you want to see a cool picture:
# im.save('borked.png')

of = open('maze.zip','wb')
# Every other character in the maze is full-black; just use the valid ones. produces a zipfile with a jpeg that says 'lake', and also 'mybroken.zip'
for p in path[1::2]:
    print p[2]
    of.write(chr(p[2][0]))