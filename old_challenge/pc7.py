#pngfile

from PIL import Image

a = Image.open("oxygen.png")
pixel_list = []
last = 0
i = 0
while i < 629:
    p = a.getpixel((i,45))
    pixel_list.append(p[0])
    i = i + 7
        
print pixel_list

result = ""
for c in pixel_list:
    result = result + chr(c)
print result

final = [105,110,116,101,103,114,105,116,121]
finresult = ""
for c in final:
    finresult = finresult + chr(c)
print finresult