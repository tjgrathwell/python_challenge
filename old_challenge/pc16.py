from PIL import Image

w = Image.open('mozart.gif')
o = Image.new(w.mode, w.size)

linelist = []
indexlist = []
for line in range(0,w.size[1]):
    thisline = []
    flag = False
    for x in range(0,w.size[0]):
        thisline.append(w.getpixel((x,line)))
        if ((w.getpixel((x,line)) == 195) and not flag):
            indexlist.append(x)
            flag = True
    linelist.append(thisline)
            
print len(linelist)
print len(indexlist)
            
i = 0
for index in indexlist:
    start = index-w.size[0]
    for x in range(0,w.size[0]):
        o.putpixel((x,i),linelist[i][start+x])
    i = i+1

o.save("shift.gif")