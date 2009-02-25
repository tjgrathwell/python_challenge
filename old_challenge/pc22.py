from PIL import Image, ImagePalette
import os

w = Image.open('white.gif')

ix = 0
while True:
    try:
        #for i in range(0,w.size[0]):
        #    for j in range(0,w.size[1]):
        #        p = w.getpixel((i,j))
        #        if p is not 0:
        #            print p
        w.putpalette([255,255,255,0,0,0,255,0,0,0,255,0,0,0,255])
        
        if len(str(ix)) != 3:
            if len(str(ix)) != 2:
                outix = '00' + str(ix)
            else: outix = '0' + str(ix)
        else: outix = str(ix)
        
        w.save("whiter%s.gif" % outix)
        ix = ix + 1
        w.seek(w.tell()+1)
    except EOFError, e:
        break

#while 1:

    #if frames[ix]:
        #im.save(outfile % ix)
        #print outfile % ix

        #if html:
            #html.write("<img src='%s'><br>\n" % outfile % ix)

    #try:
        #im.seek(ix)
    #except EOFError:
        #break

    #ix = ix + 1

os.system("convert -delay " + str(10) + " -loop 0 whiter*.gif whitest.gif")