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

    if px == (255,255,255,255):
        path.pop()
        continue
    if px == (0,0,255,255):
        path.pop()
        continue
        
    im.putpixel((x,y), (0,0,255,255))
        
    if remaining_exits:
        next_x, next_y = remaining_exits.pop()
        next_px = im.getpixel((next_x, next_y))
        exits = [(next_x+1,next_y),(next_x-1,next_y),(next_x,next_y-1),(next_x,next_y+1)]
        path.append((next_x,next_y,next_px,exits))
    else:
        path.pop()
        im.putpixel((x,y), px)

im.save('borked.png')
    
print path